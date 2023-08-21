echo %ACCOUNT_ID%

aws ecr get-login-password --profile %AWS_CLI_PROFILE% --region %REPOSITORY_REGION% | docker login --username AWS --password-stdin %ACCOUNT_ID%.dkr.ecr.%REPOSITORY_REGION%.amazonaws.com
docker build -t %REPOSITORY_NAME% .
docker tag %REPOSITORY_NAME%:latest %ACCOUNT_ID%.dkr.ecr.%REPOSITORY_REGION%.amazonaws.com/%REPOSITORY_NAME%:latest
docker push %ACCOUNT_ID%.dkr.ecr.%REPOSITORY_REGION%.amazonaws.com/%REPOSITORY_NAME%:latest
