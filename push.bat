echo %ACCOUNT_ID%

aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin %ACCOUNT_ID%.dkr.ecr.ap-northeast-1.amazonaws.com
docker build -t cost_manage .
docker tag cost_manage:latest %ACCOUNT_ID%.dkr.ecr.ap-northeast-1.amazonaws.com/cost_manage:latest
docker push %ACCOUNT_ID%.dkr.ecr.ap-northeast-1.amazonaws.com/cost_manage:latest
