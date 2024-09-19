## End to End Machine Learning Project


## Steps for deploying prject in AWS

we will use Elastic Beanstalk and CodePipeline


# 1. Prepare Your Code Repository
    - Ensure your code is in a source control system (GitHub, AWS CodeCommit, Bitbucket, etc.). You will connect this repository to CodePipeline.
# 2. Create an Elastic Beanstalk Application
    - Log in to AWS Management Console:
    - Go to the Elastic Beanstalk Console.
  Create an Application:
    - Click on Create a new application.
    - Fill in the Application name and Description.
  Select Platform:
    - Choose the platform (e.g., Python, Node.js, Docker, etc.) for your project.
    - If your platform requires specific settings (like Node.js version), select the version.
  Configure the Environment:
    - Select Web server environment for most projects.
    - For Application code, choose how you want to deploy your code:
    - Either upload a ZIP file of your code directly (which you'll change later with CodePipeline), or choose a sample application.
  Configure Additional Options (Optional):
    - You can configure environment variables, instance types, auto-scaling, and more.
    - Configure the database if needed (RDS can be added here).
  Create the Environment:
    - Once done, click Create environment.
    - Elastic Beanstalk will create your application environment, which might take a few minutes.
# 3. Create AWS CodePipeline
    - Go to the CodePipeline Console:
    - Navigate to the CodePipeline Console.
    - Click Create pipeline.
  Name Your Pipeline:
    - Give your pipeline a name and click Next.
  Configure Source Stage:
     - Select your source provider (e.g., GitHub, AWS CodeCommit, Bitbucket).
     - Follow the prompts to connect your repository and branch.
  Configure Build Stage (Optional):
     - If your project requires a build stage (e.g., compiling, running tests), select AWS CodeBuild.
      -Otherwise, you can skip the build stage.
     - If you use CodeBuild, you'll need to set up a buildspec.yml file in your project repository to define the build process.
  Configure Deploy Stage:
     - For the Deploy provider, select Elastic Beanstalk.
     - Choose the Elastic Beanstalk application and environment you created earlier.
     - Review and Create:
     - Review your settings and click Create pipeline.
# 4. Trigger a Deployment
      - Once the pipeline is created, every time you push a new commit to your repository (e.g., GitHub), CodePipeline will automatically trigger the pipeline.
      - The pipeline will pull the source code, run a build if configured, and deploy it to your Elastic Beanstalk environment.
# 5. Monitor and Manage Deployment
   Elastic Beanstalk Console:
     - Go to the Elastic Beanstalk console to monitor the environment's health, logs, and performance metrics.
     - You can also configure environment variables, scaling, load balancing, and other settings through the console.
   CodePipeline Console:
      - Monitor the status of the pipeline stages (source, build, deploy) to ensure successful deployment.
  CloudWatch:
      - Use CloudWatch to monitor logs and performance data of your application.







# Additional tips-

There is issues and difficulties i faced, so by practicing these steps i resolve them.

sometime, there is an importing error happen when i import file from the src module, it give me there is no src module present in your project.
so, for resolving this error i use this command for run the file - 

      python -m src.components.data_ingestion
      
      instead of this -
    
      python -m  src\components\data_ingestion.py