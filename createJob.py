from flask import Flask, render_template, request, redirect, url_for
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'job'

@app.route("/CreateJob", methods=['GET', 'POST'])
def registration():
    return render_template('CreateJobs.html')

@app.route("/addJob", methods=['POST'])
def AddCompany():
    job_title = request.form['title']
    job_location = request.form['location']
    min_req = request.form['minReq']
    
    insert_sql = "INSERT INTO job VALUES (%s, %s, %s)"
    cursor = db_conn.cursor()
    
    try:
        cursor.execute(insert_sql, (job_title, job_location, min_req))
        db_conn.commit()
        
        # # Uplaod image file in S3 #
        # company_image_file_name_in_s3 = "company-name-" + str(company_name) + "_image_file"
        # s3 = boto3.resource('s3')
        
        # try:
        #     print("Data inserted in MariaDB RDS... uploading image to S3...")
        #     s3.Bucket(custombucket).put_object(Key=company_image_file_name_in_s3, Body=image)
        #     bucket_location = boto3.client('s3').get_bucket_location(Bucket=custombucket)
        #     s3_location = (bucket_location['LocationConstraint'])

        #     if s3_location is None:
        #         s3_location = ''
        #     else:
        #         s3_location = '-' + s3_location

        #     object_url = "https://s3{0}.amazonaws.com/{1}/{2}".format(
        #         s3_location,
        #         custombucket,
        #         company_image_file_name_in_s3)

        # except Exception as e:
        #     return str(e)
        
    finally:
        cursor.close()

    print("New Job Added Successfully")
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)