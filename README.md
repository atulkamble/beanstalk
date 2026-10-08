# AWS Elastic Beanstalk – Training Notes

Topics: Introduction, Website Hosting, Environment Management, Cloning, Domain Name Swapping, and Application Management.

## 1. Introduction to AWS Elastic Beanstalk

AWS Elastic Beanstalk is a Platform as a Service (PaaS)-style AWS service used to deploy, manage, and scale web applications without manually configuring the underlying infrastructure.

### Key points to remember

- Supports Java, Python, Node.js, PHP, Ruby, .NET, Go, and Docker.
- Automatically provisions EC2, Load Balancer, Auto Scaling, and monitoring resources as required.
- Supports application versioning and environment management.
- Supports Single Instance and Load Balanced environments.
- Provides environment cloning and CNAME swapping.
- Elastic Beanstalk has no additional service charge; underlying AWS resources are billed.

## 2. Terms and Definitions

| Term                   | Definition                                            |
| ---------------------- | ----------------------------------------------------- |
| Application            | Logical container for environments and versions       |
| Application Version    | Deployable application code                           |
| Environment            | Running application infrastructure                    |
| Platform               | Runtime and operating system configuration            |
| Web Server Environment | Handles HTTP/HTTPS requests                           |
| Worker Environment     | Processes background tasks, commonly using SQS        |
| CNAME                  | DNS hostname assigned to an environment               |
| Environment Clone      | New environment copied from an existing configuration |
| CNAME Swap             | Exchanges Elastic Beanstalk environment URLs          |
| Rolling Deployment     | Updates instances in batches                          |
| Immutable Deployment   | Deploys using new instances before replacing old ones |
| Health Monitoring      | Tracks application and environment health             |

## 3. Elastic Beanstalk Architecture

Example load-balanced web server environment. Single-instance environments do not require a load balancer.

Request flow: Browser → Environment URL → Load Balancer → EC2 → Web Application.

## 4. Website Hosting – Hands-On Lab

Objective: Deploy a basic Python Flask website using Elastic Beanstalk.

### Step 1: Create project

```
mkdir beanstalk-webapp
cd beanstalk-webapp
```

### Step 2: Create `application.py`

```
from flask import Flaskapplication = Flask(__name__)@application.route("/")def home():    return """    <h1>AWS Elastic Beanstalk</h1>    <p>Website deployed successfully!</p>    """if __name__ == "__main__":    application.run()
```

### Step 3: Create `requirements.txt`

```
Flask>=3.0,<4.0
```

### Step 4: Deploy using AWS Console

1. Open AWS Console → Elastic Beanstalk.
2. Select Create application.
3. Application name: `beanstalk-webapp`.
4. Environment tier: `Web server`.
5. Platform: `Python` (supported version).
6. Application code: Upload ZIP.
7. Choose Single instance for a simple lab.
8. Configure service role, EC2 instance profile, networking, and security.
9. Submit and wait for environment health to become Green.
10. Open the environment domain URL.

Create the ZIP:

```
zip -r app.zip application.py requirements.txt
```

### Step 5: Verify

```
curl -I http://YOUR-ENVIRONMENT-URL
```

The response should show `200 OK` when the website is healthy.

## 5. Environment Management

| Operation          | Purpose                                    |
| ------------------ | ------------------------------------------ |
| Create             | Provision a new environment                |
| Deploy             | Publish a new application version          |
| Configure          | Change EC2, scaling, networking, variables |
| Restart App Server | Restart the application server             |
| Rebuild            | Recreate environment resources             |
| Clone              | Copy environment configuration             |
| Swap Domain        | Exchange environment CNAMEs                |
| Terminate          | Delete environment resources               |

### AWS CLI commands

Install and configure EB CLI on macOS:

```
brew install awsebcli

eb --version
aws configure
```

Initialize and create:

```
eb init
eb create dev-env
```

During `eb init`, select the AWS Region, application, Python platform, and SSH preferences. Creating an environment also requires the appropriate IAM roles and configuration.

Common commands:

```
eb list
eb status
eb health
eb deploy
eb logs
eb open
eb printenv
```

Update configuration:

```
eb config
```

Terminate environment:

```
eb terminate dev-env
```

## 6. Creating Environment Clones

Environment cloning creates another environment with configuration based on an existing environment.

### Architecture

### Console steps

1. Elastic Beanstalk → Environments.
2. Select `production-env`.
3. Actions → Clone environment.
4. Enter new environment name `staging-env`.
5. Review configuration.
6. Select Clone.

### AWS CLI

```
aws elasticbeanstalk create-environment \
  --application-name beanstalk-webapp \
  --environment-name staging-env \
  --cname-prefix staging-webapp-unique \
  --template-name staging-config \
  --version-label v1
```

This example assumes the saved configuration template `staging-config` and application version `v1` already exist. To clone an existing environment directly, use the console's Clone environment action.

Remember: A clone has separate resources and costs. Check environment variables, secrets, database connections, and DNS before using it.

## 7. Domain Name Swapping (CNAME Swap)

Purpose: Switch traffic between two Elastic Beanstalk environments without changing the application code.

### Blue-Green Deployment Architecture

Conceptual blue-green cutover: the production hostname moves from Blue to Green after the CNAME swap.

### Console steps

1. Create Blue environment (Version 1).
2. Create Green environment (Version 2).
3. Test Green environment.
4. Open Elastic Beanstalk → Environments.
5. Select environment → Actions → Swap environment URLs.
6. Select the other environment.
7. Confirm swap.

### AWS CLI

```
aws elasticbeanstalk swap-environment-cnames \
  --source-environment-name blue-env \
  --destination-environment-name green-env
```

Verify environment URLs:

```
aws elasticbeanstalk describe-environments \
  --application-name beanstalk-webapp \
  --query 'Environments[*].[EnvironmentName,CNAME,Health]' \
  --output table
```

Important: A CNAME swap exchanges Elastic Beanstalk environment CNAMEs, not custom Route 53 DNS records. Custom domains should reference the appropriate stable environment hostname. DNS caching can delay cutover, and existing connections may continue temporarily.

## 8. Application Management

| Feature               | Purpose                                  |
| --------------------- | ---------------------------------------- |
| Application Versions  | Track releases                           |
| Deployments           | Update running applications              |
| Configuration         | Manage platform and environment settings |
| Environment Variables | Configure runtime values                 |
| Logs                  | Troubleshoot applications                |
| Monitoring            | View metrics and health                  |
| Scaling               | Adjust instance capacity                 |
| Saved Configurations  | Reuse environment settings               |

### Common deployment commands

```
# Deploy current application
eb deploy

# Check environment status
eb status

# View logs
eb logs

# View environment health
eb health

# List application environments
eb list
```

### Environment variables

```
eb setenv APP_ENV=production LOG_LEVEL=info
```

View variables:

```
eb printenv
```

Avoid placing passwords or API keys directly in commands. Use AWS Secrets Manager or Systems Manager Parameter Store integrations for secrets.

## 9. Deployment Policies

| Policy                        | Behavior                                    | Use Case                    |
| ----------------------------- | ------------------------------------------- | --------------------------- |
| All at Once                   | Updates all instances together              | Development                 |
| Rolling                       | Updates instances in batches                | Standard deployment         |
| Rolling with Additional Batch | Adds capacity during update                 | Reduced capacity impact     |
| Immutable                     | Launches replacement instances              | Safer production deployment |
| Traffic Splitting             | Sends a portion of traffic to new instances | Canary testing              |

## 10. Important Points to Remember

1. Elastic Beanstalk manages infrastructure provisioning and application deployments.
2. Applications contain application versions and environments.
3. Each environment has its own infrastructure and URL.
4. Single-instance environments are suitable for basic labs.
5. Load-balanced environments support scaling and higher availability.
6. Cloning copies environment configuration into a new environment.
7. CNAME swapping supports blue-green deployments.
8. A swap does not migrate databases, sessions, or application data.
9. CloudWatch helps monitor metrics and logs.
10. Terminate unused environments to avoid unnecessary charges.

## 11. Quick Practical Lab Sequence

| Step | Activity                             | Expected Result              |
| ---- | ------------------------------------ | ---------------------------- |
| 1    | Create Python Flask application      | Website code ready           |
| 2    | Create Elastic Beanstalk application | Application created          |
| 3    | Create `blue-env`                    | Version 1 hosted             |
| 4    | Open environment URL                 | Website accessible           |
| 5    | Modify website content               | Version 2 ready              |
| 6    | Clone/create `green-env`             | Second environment available |
| 7    | Deploy Version 2 to Green            | Updated website hosted       |
| 8    | Test Green                           | Health checks pass           |
| 9    | Swap environment CNAMEs              | Production URL targets Green |
| 10   | Verify and clean up                  | Deployment validated         |

Official documentation: AWS Elastic Beanstalk Developer Guide

Training outcome: Students should be able to deploy a website, manage application environments, clone configurations, perform blue-green deployments using CNAME swapping, and troubleshoot basic Elastic Beanstalk applications.
