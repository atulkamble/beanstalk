```
powershell run as admin >> 
choco install python 
python -m ensurepip --upgrade

git --version
python --version
python -m pip --version OR pip --version 

git clone https://github.com/atulkamble/beanstalk.git
cd beanstalk
code .

python -m venv venv
source venv/bin/activate
OR 
python -m venv venv
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
python app.py

http://localhost:5000

rm -f app.zip
zip -r app.zip application.py requirements.txt Procfile static/
unzip -l app.zip

OR 

Compress-Archive -Path app.py, requirements.txt -DestinationPath app.zip -Force

1. Search Elastic Beanstalk 
2. envirnment >> create environemnt 
3. 
app - webapp 
environment - webapp-env 
4. upload code >> local >> upload app.zip 


brew install awsebcli
pip install --upgrade awsebcli

eb --version
eb init

eb create dev-env
eb deploy 

eb terminate dev-env

sudo systemctl cat web

sudo systemctl status web --no-pager
sudo tail -n 50 /var/log/web.stdout.log
sudo tail -n 30 /var/log/nginx/error.log
sudo tail -n 30 /var/log/eb-engine.log
cat /var/app/current/Procfile
curl -i http://127.0.0.1:8000/health


```

# 14-11-2026 
```
// developer app - devloper - stack - python-flask

1. git clone https://github.com/atulkamble/beanstalk.git
2. cd beanstalk
3. open in VS Code 
code .
4. terminal >>

python --version
pip --version 

pip install -r requirements.txt 
python app.py 

http://localhost:5000 

// on windows >> powershell 

powershell run as admin >> 

choco install python 
python -m ensurepip --upgrade

python -m venv venv
source venv/bin/activate
OR 
python -m venv venv
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
python app.py

// stage - beanstalk 

1. search - aws beanstalk 
2. create env 
3. create app
4. upload app.zip // tip get file from this repo https://github.com/atulkamble/beanstalk
5. wait for deployment 
6. check app url >> copy >> browser paste 

http://myapp-env.eba-qcc6z5pj.us-east-1.elasticbeanstalk.com/

7. Alias Record to Route53 

Create Record - A 

Select Service - Elastic Beanstalk
Select Region - N.Virginia (us-east-1)
Select Env - select eb-env
Add Record 

atulkamble.in

8. delete A record protection plan, delete A record from Route53 domain
9. delete env 
10. delete app
11. delete bucket policy 
12. empty bucket
13. delete bucket
14. crosscheck ec2, lb, asg, sg
```
