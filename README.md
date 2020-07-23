# Blue-Green Lambda Deployment Orchestrator

This project includes the following components:

1. **CodeCommit** - Stores the code for the application in a cloud based Git Repository.

1. **CodePipeline** - Fetches the source-code from CodeCommit and builds a deployable artifact using CodeBuild. The artifact is a processed template that is then deployed using CloudFormation as the last stage in the pipeline. The pipeline includes a manual approval stage where the pipeline orchestrator approves execution of the change-set.

1. **CloudFormation** - AWS native IaC tool. 

1. **API Gateway** - A gateway for APIs that can be integrated with AWS services. 

1. **Lambda** - The serverless compute platform for deploying the application in a `python3.7` runtime.

1. **CodeDeploy** - The continous-deployment service that shows a blue-green deployment for Lambda.

## Requirements

1. Git 
1. AWS CLI

## Steps to Deploy the Solution

1. Deploy the Infrastructure Pipeline:

Using AWS-CLI:

```bash
aws cloudformation deploy --template-file ./infrastructure.yml \
                          --stack-name DevOps-Artifact \
                          --parameter-overrides Email=<EMAIL> \
                          --capabilities CAPABILITY_IAM
```
Replace `EMAIL` in the above command with the email ID where you'd like to recieve approval notifications.

1. The pipeline created has a manual approval stage. A SNS topic and an email subscription would be created in the step above. Please check your email and confirm the subscription.

1. Commit code from the `application` folder into the CodeCommit repository created in the stack above:

```bash
    git clone <REPOSITORY_URL>
    cp -R application/* Time-Service/
    cd Time-Service/ 
    git add .
    git commit -m "Initial Commit"
    git push
```
The `REPOSITORY_URL` is available in the stack outputs.

1. After the above step, you're application should now start deploying through CodePipeline. You will need to approve the deployment for the application to be successfully deployed.

1. After the pipeline execution completes, we are all set to test the `time-series` API:


