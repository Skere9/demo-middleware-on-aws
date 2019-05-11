

git add .
git commit 
git push

docker build -t skere9/demo-middleware-on-aws:nativeEBDeploymenT .
[OPTIONAL] docker-compose up --build
docker push skere9/demo-middleware-on-aws:nativeEBDeployment 


