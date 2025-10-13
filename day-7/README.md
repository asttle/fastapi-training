Command 1: pip install -t dependancies -r requirements.txt  
to bundle all dependancies required for our main file
Command 2: (cd dependancies; zip ../aws_lambda_artifact.zip -r .)
Create zip artifact for aws lambda including all dependancies
Command 3: zip aws_lambda_artifact.zip -u main.py  
add our main.py to zip artifact
In AWS lambda edit runtime settings to use main.handler where we use mangum to define handler, by default it would be something lambda etc 