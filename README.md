# University Learning Management System

---


## Functions
### Teacher
First the teacher will apply for job,if he/she gets selected there accounts will be made and approved by the admin, after approval only teacher can access their dashboard.
After account approval by admin, teacher can take attendance of any class and view their attendance later.
Teacher can also publish/announce notice to student like submission of assignments.
Teacher can also Add/Upload Video Lecture to Students

## Student
First student will take admission/signup.
When their account is approved by admin, only then the student can access their dashboard.
After account approval by admin the student can view their details like attendance.
Student can't view attendance of other student.
Student can't announce, they can only view.

### Admin
First admin will signup for a account.
After login they can see how many student/teacher wants to get job/admission in their school.
They can approve or delete/cancel the request.
They can update any student/teacher details.
Admin can announce notice also.



- Anyone can become Admin

## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :

``` python -m pip install -r requirements.txt ```


- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```





