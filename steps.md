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
