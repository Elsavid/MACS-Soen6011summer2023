# Career Services Application
## About the project 
The overall goal is to develop a web application that serves as a career service platform for employees and job-seeking candidates. The platform allows job seekers to create and maintain their portfolios,browsing the posts, while allowing employers to post job listings. The employer can also review applications and offer interview for candidates matching their job requirements. Candidates can track their applications and see status updates. The admin can manage all user accounts, profiles, jobs, application. This application will have a secure login procedure and ensure that no one can crack it easily.

### Objective
The objective of this project is to develop a comprehensive career services platform that facilitates the connection between job-seeking students and employers. The project will be a web application where it can access at any time and anywhere.
The objective of this project follow as:
Students/Candidates can register and create their profiles, upload resumes to this web application so that employers can access their personal profile.
Students/Candidates can browse, filter a list of available job postings and apply for one or more jobs.
Employers can create one or more job postings and track candidates who have apply for their job postings
Employers can either accept the application from students/candidates or reject it.
System administrators should have the right to create/delete accounts, tracking/managing job postings and applications.

### Core Feature
The core feature of this application is allowing employers to find the right candidates for each of their job openings, while also allowing candidates to apply to each of these jobs.	

User Registration and Authentication: Allow students and employers to create individual accounts using their email addresses and secure passwords. Implement a login system for users to authenticate themselves in the platform.

Job Posting and Management: Allow employers to post job openings. Enable employers to manage their job postings, review applicants, and track the hiring process. Enable students to browse available job postings and apply for the job. 

Student/Candidate Profile Management: Enable students to create, browse, update their professional profiles including resume, work experience, skill set and so on. Enable employers to see students profiles.

Tracking System: Tracking applications. Employer can review and offer interview for candidates matching their job requirements. Candidates can see their applications and get updates of status for being selected or rejected by employers.

Admin Management: Allow admins to manage all user accounts, applications, job postings and profiles.

Data Security and Privacy: The login credentials are high security which does not allow people other than the user to access their account.



## Built With
**Front-end**
* [React](https://react.dev/) - The library used for front-end.
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - The programming language used for front-end.
* [NodeJS](https://nodejs.org/en/about) - Supporting front end as cross-platform JavaScript runtime environment.
  
**Backend-end**
* [Flask](https://flask.palletsprojects.com/en/2.3.x/) - The lightweight python microservice framework used for back-end.
* [Flask-login](https://flask-login.readthedocs.io/en/latest/) - The python framework used for Flask microservice user and session management. 
* [MongoDB](https://www.mongodb.com/) - The database used.
  

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
Step 1 : Ensure you have the mentioned applications downloaded and able to verify by obtaining their versions in your system.
Step 2 : Follow the backend instructions to have the backend able to receive data.
Step 3 : Open a Terminal and locate the front end folder and use cd to enter into the folder
>cd fe-career-platform

Step 4: Type the command to have your front end running smoothly as well.
>npm start

(For Windows user: Enable running scripts on your system by running the following command if it is in Restricted mode)
>Set-ExecutionPolicy RemoteSigned 



## Authors
**Front-end**
* [Mayra Ruiz](https://github.com/meyruiz) 40260627
* [Lei Zhou](https://github.com/Autosleep) 27291515

**Back-end**
* [Alor Ebubechukwu](https://github.com/Alor-e) 40254055
* [Sharon Chatragadda](https://github.com/SecretAgentShh) 40229448 
* [Haoyue Zhang](https://github.com/Elsavid) 40202064 
* [Mengqi Liu](https://github.com/paullmq8) 40221432

## Roadmap 
This project adapts **Agile** development process. The duration of the project is 6 weeks; Each iteration takes between 1.5 to 2.5 weeks long, there are 4 iterations in total.

* [Sprint 1](https://github.com/meyruiz/MACS-Soen6011summer2023/milestone/1) - Sprint 1 backlog

* [Sprint 2](https://github.com/meyruiz/MACS-Soen6011summer2023/milestone/2) - Sprint 2 backlog

* [Sprint 3](https://github.com/meyruiz/MACS-Soen6011summer2023/milestone/3) - Sprint 3 backlog

* [Sprint 4](https://github.com/meyruiz/MACS-Soen6011summer2023/milestone/4) - Sprint 4 backlog
  
See the [open issues](https://github.com/meyruiz/MACS-Soen6011summer2023/issues) for a full list of proposed open issues and plans.


## Documentation 
The documentation is available on [here](https://github.com/meyruiz/MACS-Soen6011summer2023/wiki) 

[Minutes](https://github.com/meyruiz/MACS-Soen6011summer2023/wiki/Minutes) - Meeting minutes

[Sprint 1](https://github.com/meyruiz/MACS-Soen6011summer2023/wiki#sprint1)  - Sprint 1 documentation 

[Sprint 2](https://github.com/meyruiz/MACS-Soen6011summer2023/wiki#sprint2)  - Sprint 2 documentation

[Sprint 3](https://github.com/meyruiz/MACS-Soen6011summer2023/wiki#sprint3)  - Sprint 3 documentation

[Sprint 4](https://github.com/meyruiz/MACS-Soen6011summer2023/wiki#sprint4)   - Sprint 4 documentation

## Backend Environment Setup
**MongoDB Docker Setup**
```
$docker pull mongo
$docker run -d -p 27017:27017 -v {/your/local/directory}:/data/db --name mymongo mongo:latest


$brew install mongosh
$mongosh localhost:27017

or in linux 
$docker exec -it mymongo mongosh


basic mongodb commands:
>show dbs
>db.user.insert({ "name": "soen6011_db" })
>use soen6011_db
>show collections
>db.users.find()
```

**Flask Framework Setup**
```
$git clone git@github.com:meyruiz/MACS-Soen6011summer2023.git
$cd be-career-platform
$python3 -m venv venv
$source venv/bin/activate
$pip3 install -r requirements.txt
$flask run
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

