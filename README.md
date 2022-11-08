# Setting up SageMaker Studio with Jupyter Lab 3 using CDK

Please review the contents of this repository in its entirety to understand how CDK works in CloudFormation Stacks.

## Prerequisites:

* The AWS Command Line Interface (https://aws.amazon.com/cli/) (AWS CLI) is installed
* The AWS CDK is installed (https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_install)
* The user has permissions to create and deploy CDK/CloudFormation resources as defined in the scripts outlined in the following.
* Python 3+
* Basic knowledge of Amazon SageMaker Studio.

**Security**: It is advisable to scope down the AmazonSageMakerFullAccess permissions in the IAM role created in the *sagemaker_studio_construct.py* depending on user requirements.

### Step 1: First, let’s clone the code repository to your local directory.

`git clone https://github.com/aws-samples/aws-cdk-native-sagemaker-studio.git`

### Step 2: Make sure you are in the new directory cloned from github.

`cd <Path to directory>`

### Step 3: Create a virtual environment:

* macOS/Linux: `python3 -m venv .cdk-venv`
* Windows: `python3 -m venv .cdk-venv`

### Step 4: Activate the virtual environment after it is created:

* macOS/Linux: source `.cdk-venv/bin/activate`
* Windows: `.cdk-venv\Scripts\activate.bat`
* Powershell `.cdk-venv\Scripts\activate.ps1`

### Step 5: Install the required dependencies:

`pip3 install -r requirements.txt`

**[Optional]** At this point you can now synthesize the CloudFormation template for this code.

`cdk synth`

### Step 6: To deploy your AWS CDK stack, run the following commands from the project’s root directory within your terminal window. 

`aws configure`

`cdk bootstrap --app "python3 -m cdk.app"`

`cdk deploy --app "python3 -m cdk.app"`

Review the resources AWS CDK creates in your AWS account and enter yes (y) when prompted to deploy the stack.

It may take some time for the stack to deploy, check its status in the terminal or the AWS CloudFormation console.

### Cleanup

Follow the steps to delete the SageMaker Domain (https://docs.aws.amazon.com/sagemaker/latest/dg/gs-studio-delete-domain.html)

then run `cdk destroy`

When asked to confirm the deletion of the respective stacks select/enter yes "y"


## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

