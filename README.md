# Code Cabin - PP4: Iteration 1

## [Link to live website](https://code-cabin-d74544e083a8.herokuapp.com//)

## **Purpose of the Project**

To create a booking website for a "Code Cabin" company, where users can sign up to book a relaxing stay in a lovely remote Irish cabin (With top-tier broadband and amenities of-course!), so they can get away from a busy distracting life, and have something of a getaway holiday, just them and their coding needs.
Users will be able to book, view, update and delete their own bookings on a user profile page.
Users will be able to publicly rate their stays/experiences with the Code Cabin (after staff approval/screening) as well as submit comments/feedback directly to the site owners.

Early Wireframe Prototype
![Home Page Wireframe](static/docs/readme-images/index.html.png)

![Booking Page Wireframe](static/docs/readme-images/booking.html.png)

## **Instructions**

Section To be completed --
![blankscreenshot](static/docs/readme-images/)

## **Research & Planning**

Section To be completed --
ERD was created to guide django database model developemnt.

**Understanding the Target Problem**
Section To be completed --

**Audience Needs/Stories**
Section To be completed -- See Repository Issues/Project for Iteration 1 User Stories for temporary presentation

**Search For Suitable Technologies**
Section To be completed --

## **Initial Planning**

Section To be completed --

## **Features**

Section To be completed --

- Input any valid booking selection on the "Booking" Page. This is silently stored in the backend, pending future "availability validation". The user is then currently forwarded to the home/index page.

- Register, Login, Logout, with the relevant nav buttons.

- View a tranquil page of nothing but some peaceful static links. Very soothing.

### **Technology Used**

Section To be completed --

1.  Python
    Programming Language used to write the app.
2.  Django ...
3.  Firefox https://www.mozilla.org/en-US/firefox/new/
    Used as the main browser of the project (Browsing, Editing, Screenshot capabilities)
4.  Chrome https://www.google.com/intl/en_ie/chrome/
    Used as alt browser of the project (Testing)

### **Possible Future Features to Implement**

Section To be completed --

Ideas for future possible features include;

## **Testing**

Section To be completed --

### **General Testing Process**

Primary testing through the development process was done via the CodeAnywhere python terminal, running the Django server locally.
python3 manage.py runserver. With followup testing on the Heroku Live site, after update deployment.

I would then test to see that changes reflected design intent. (IE check newly added features work, database was correctly updated etc.

Automated testing and comprehensive overall testing regime to be ramped up. Possible Test Driven Development in future iterations.

### **Hardware**

This application was tested primarily tested using;

- my Desktop PC (Windows 10 1440p widescreen monitor) (Firefox & Chrome)
- My Google Pixel 6a Phone (firefox)

### **Software**

Section To be completed --

### **Validator Testing**

Section To be completed --

### **Automated Testing**

Section To be completed --

### **Bugs Encountered**

Section To be completed --

### **Unfixed Bugs**

Section To be completed --

Bug#1
Entire amazing website is not currently presenting in reality. Appears to be mostly nothing.

Steps to reproduce:

1. Open the website.

2. Despair.

## **Deployment**

Section To be completed --

Codeanywhere
The site was developed using Codeanywhere Browser Workspace. This was done by:

1. Creating an account with GitHub and creating a GitHub repository with the project name.

...

Section To be completed --

Heroku

1. Create a free https://heroku.com/ account, and validate it (You may want to investigate your organization's student credits policy if you have access to any)
2. Set password after validating email.
3. On the Heroku Dashboard default screen, click "create app"
4. go to the settings screen and down to the config vars section.
5. Add a "CREDS" var and as the arg add your credentials if you have any. I would recommend trying to stick to one set of creds and one file if possible.
6. Add a "PORT" var and give it the arg 8000.
7. if you are using custom additional creds, add the lines of code I screenshot above in "bugs encountered" to your controllers/default.js file in get pod.
8. Add the custom var names and args to the heroku.com settings page as above for CREDS.

9. Move to the deployment tab
10. Enable automatic deploys, then this time, hit the manually deploy page.
11. When it's finished, click the "open the app" link and view your template page.

Section To be completed --

## **Credits**

Section To be completed --

Assorted Links and resources used so far:

All site/project images are currently from pexels.com and are not copyrighted.

https://docs.djangoproject.com/en/3.1/topics/auth/default/#the-login-required-decorator - to be implemented

https://www.youtube.com/watch?v=wm009U623RU darshandev HTMS system in Django
https://www.youtube.com/watch?v=-9dhCQ7FdD0&t=1799s ^^^^^ booking availability function

Specific keywords for filtering model queries
https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups

https://stackoverflow.com/questions/1506901/cleanest-and-most-pythonic-way-to-get-tomorrows-date

https://www.youtube.com/watch?v=MZwKoi0wu2Q – crispyform example tut

https://github.com/django-crispy-forms/crispy-bootstrap5 for bootstrap 5 crispyforms

https://www.agiliq.com/blog/2019/01/django-createview/ form --> Database research

https://stackoverflow.com/questions/69488047/how-to-pass-the-username-to-the-member-who-fill-a-form current form implementation solution

https://www.youtube.com/watch?v=733hsTRPID4 use of form|pipe solution in template tag to render with crispyforms package.

Code Institute Materials/Practice Project
My Code institute Mentor - Rohit Sharma who has been very encouraging and supportive during this project iteration.
