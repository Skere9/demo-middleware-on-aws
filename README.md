## ##############################
##
## Note for DEVOPS 
##
## ##############################

# Sources
# http://blog.shippable.com/how-to-deploy-to-elastic-beanstalk-part-1 
# http://blog.shippable.com/how-to-deploy-to-elastic-beanstalk-part-2 *** this is good
# Additional 
# https://blog.eq8.eu/article/common-aws-elasticbeansalk-docker-issues-and-solutions.html 
# https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker.html
# https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80

# Online Repositories 
# http://www.github.com 
# http://www.dockerhub.com  
# http://aws.amazon.com  

#################################
# PART 1: INITIAL SETUP
#################################

# Setup - AWS Elastic Beanstalk
eb init
eb create skere9/demo-python-mw-container:nativeEBDeployment
# Setup - Docker Hub
docker login --username=skere9 --password=bubbatest 

#################################
# PART 2: From here on out - this is the ongoing work
#################################

# Local Git
git add .
git commit 

# GitHub - push
git push

# Local Docker build
docker build -rm=true -t skere9/demo-middleware-on-aws:nativeEBDeploymenT .
[OPTIONAL] docker-compose up --build


docker push skere9/demo-middleware-on-aws:nativeEBDeployment 

# Deploy to AWS Elastic Beanstalk
eb deploy skere9/demo-python-mw-container:nativeEBDeployment

#################################
# PART 3: Test online
#################################

GUI       : https://s3.amazonaws.com/dbt-test-this/index.html/ 
Middleware: https://demo-middleware-on-aws-dev.us-east-1.elasticbeanstalk.com/

