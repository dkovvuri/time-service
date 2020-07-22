# Blue-Green Lambda Deployment Orchestrator

This project includes the following components:

1. **CodeCommit** - Stores the code for the application in a cloud based Git Repository.

1. **CodePipeline** - Fetches the source-code from CodeCommit and builds a deployable artifact using CodeBuild. The artifact is a processed template that is then deployed using CloudFormation as the last stage in the pipeline. The pipeline includes a manual approval stage where the pipeline orchestrator approves execution of the change-set.

1. **CloudFormation** - AWS native IaC tool. 

1. **API Gateway** - A gateway for APIs that can be integrated with AWS services. 

1. **Lambda** - The serverless compute platform for deploying the application in a `python3.7` runtime.

1. **CodeDeploy** - The continous-deployment service that shows a blue-green deployment for Lambda.