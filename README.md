# CAPSTONE Final Project

## Personal Portfolio Application with Blog Functionality

My capstone project is a responsive personal portfolio web application with blogging functionality. The project is implemented with Django, WYSIWYG editor, CSS, JavaScript and HTML. I have used SQLite as a database. By using Django from backend, I will be able to dynamically create, read, update and delete the features of the website from the Django admin panel. The frontend of the website has the following 6 sections: 

## Home Section
When users visit my homepage they will see my personal photo ID and My Greeting's. I have created a model in Django that will collect my brand name, greeting1, greeting 2 and main image from backend and display it on the frontend to users. All of this can be changed dynamically without affecting the aesthetics of design.

## About Section
The about section consist of an image, Main title, profession and a brief description. All contents can be changed through Django admin platform. This is accomplished by creating about Model section in my models.py file.  

## Skills Section
I created a Category Model and inside each category, I included many skills. This is accomplished by customising the admin.py file using Tabularinline feature . This is type of design enables me to upgrade my website dynamically when I acquire a new skill without hard coding inside the HTML file.

## Portfolio Section
In my models.py file, I created a Portfolio model that consist of Title of the Portfolio, Image and a YouTube link section. Here when the user hover around the image, the image will blur and there will be View on YouTube link. If the user click the link, he/she will be redirected to see live demo of my projects. 

## Blog Section

 In my blog section viewers can view all my articles. The blog section will only show the image, Category, title and snippets of the article. Here the blogs are organized in reverse chronology manner. If the user hover around and click the title of the blog, he/she will be redirected to the blog-detail page. I have installed Djnago-ckeditor WYSIWYG editor to edit the blog. 



## Contact Section Page

Here if the user wants to send me a message, they can use the contact form. I have created a Django Contact Model and I have employed Django list display method on the admin.py file to configure the admin section of the incoming messages. Once, the user successfully sent the message, he/she will be notified using sweet alert JavaScript plugin. 

## Distinctiveness and Complexity

## Distinctiveness

* For my final project I built a personal portfolio web app with CRUD capability. 
* It is designed in order to promote myself in the web and to write various blogs after completion of my Harvard cs50   course.


## Complexity

* The website was built with a single page application in mind. However, since I will be posting unlimited blogs, I have incorporated an infinite horizontal scrolling of blogs for users by employing a carousel of blogs.
* The detail section of the blogs are rendered in a separate blog detail pages. 
* The admin pages of the personal web app is customized.
* I created a JavaScript main.js file in order to create a fluid user interface to achieve the SPA capability.

## What is Contained in each file created
In order to achieve this I created portfolio app inside the myportofolio djnago project. Inside the portfolio app, I created models inside models.py file, then after making migrations, I registered the models in the admin.py file, then I created functions inside the views.py file and finally I created the urls.py file and I created url routes. In order to render app, I created templates folder. Inside the template file, I created index.html to render the single web app. Then I created base..html and blog_detail.html pages to render the full blog post.
Since the project utilizes various media files, I created media_root folder that will store all my pictures inside picture, profile and portfolio folders. Furthermore, since the project requires JS and css files, I created a static folder and inside I created another aseets folders which will store all my JavaScript, CSS, IMG and sass files under thier respective folder name. Moreover, Since the CKEditor requires djnago collectstatic command, after running the command I created static_root folder which includes admin, assets and ckeditor folders. Finally, inside the main myportfolio djnago project folder, I have created README.md and requirements.txt files. 

## Getting started:
Install all the dependencies of this project by typing `pip install -r requirements.txt`
- Migrate the database by typing `python manage.py migrate` on the command line
- Run the project locally by typing `python manage.py runserver` on the command line
- You project will be accessible in your localhost or local network.

## Project YouTube Demo
- YouTube link: https://youtu.be/ruuJp1glRvk