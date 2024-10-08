import os 
import sys 
from dataclasses import dataclass 

from catboost import CatBoostRegressor 
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 
from sklearn.neighbors import KNeighborsRegressor 
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException 
from src.logger import logging
from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "XGB Regressor": XGBRegressor(),
                "CatBoost Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            model_report: dict = evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test,
                                                 y_test=y_test, models=models)

            if not model_report:
                raise CustomException("Model evaluation failed, no results generated.")

            # To get the best model score from the report
            best_model_score = max(sorted(model_report.values()))

            # To get the best model name from the report
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No suitable model found with a score above 0.6")

            logging.info(f"Best model found: {best_model_name} with score: {best_model_score}")

            # Saving the best model
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            # Predicting with the best model
            predicted = best_model.predict(X_test)

            # Calculating R^2 score
            r2_value = r2_score(y_test, predicted)
            logging.info(f"R^2 Score: {r2_value}")

            return r2_value  # Return the R2 score for further use if needed

        except Exception as e:
            raise CustomException(e, sys)