import csv
from flask import Flask,render_template,request,Response,jsonify


app=Flask(__name__)   


# with open('students.csv', 'w', newline='') as csvfile:
#     fieldnames = ['Student ID','Student Name','Gender','DateOfBirth','City','State','EmailId','Qualification','Stream']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'Student ID': '123','Student Name': 'lo','Gender': 'Male', 'DateOfBirth': '15/7/77','City': 'Chennai', 'State': 'TN','EmailId': 'lo@gmail.com', 'Qualification': 'BE','Stream': 'ECE'})


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/addstudent", methods =["GET", "POST"])
def addstudent():
    if request.method == "POST":
        Student_ID=request.form.get("studentid")
        Student_Name=request.form.get("studentname")
        Gender=request.form.get('gender')
        DateOfBirth=request.form.get("dateofbirth")
        City=request.form.get("city")
        State=request.form.get("state")
        EmailId=request.form.get("email")
        Qualification=request.form.get("qualification")
        Stream=request.form.get("stream")
        data=[Student_ID,Student_Name,Gender,DateOfBirth,City,State,EmailId,Qualification,Stream]
        with open('students.csv', 'a', newline='') as csvfile:
            fieldnames = ['Student ID','Student Name','Gender','DateOfBirth','City','State','EmailId','Qualification','Stream']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Student ID': Student_ID,'Student Name': Student_Name,'Gender': Gender, 'DateOfBirth': DateOfBirth ,'City': City, 'State': State,'EmailId': EmailId, 'Qualification': Qualification,'Stream': Stream})
        return render_template('index.html')
    else:
        return render_template('add-student.html')

@app.route("/searchstudent")
def searchstudent():
    return render_template('search-student.html')

@app.route("/displaystudents")
def displaystudents():
    rows=[]
    with open('students.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)
    return render_template('display-students.html',rows=rows)

if __name__=='__main__':
    app.run(debug=True)


