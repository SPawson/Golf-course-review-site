<h1>Play Golf! | Code Institute Third Milestone Project</h1>


<p>This project is a data driven application, which has been designed with golfers in mind. The application is useful
    and informative to its end users and will allow them access to a greater breadth of golf course knowledge. Driven by
    the community aspect of the site, this will allow site to be especially engaging, as users can influence the courses
    themselves.</p>

<p>The application includes a number of features, such as a login system, which allows users to register themselves, so
    that they can interact with the site and leave reviews. This extends to admin users, who are able to create ,read
    ,update and delete(CRUD)the golf courses themselves. The site also includes features such as allowing users the
    ability to search for courses based on criteria, and been able to manage CRUD functionality surrounding their
    reviews.</p>

<p>The web application can be viewed on Heroku via the following address:
    <a target="_blank"
        href="https://play-golf-course-finder.herokuapp.com/">https://play-golf-course-finder.herokuapp.com/</a></p>

</hr>
<h2>UX</h2>

<h3>Overview</h3>

<p>The main focus of this application is to allow golfers the ability to search for and review golf courses around
    England. This means therefore, that the whole design of the application is to further enhance the users experience
    to ensure it is as easy to use the interact with the sites features.</p>

<h3>Wireframes</h3>
<p> During the development stage of my project I generated some wireframes for both the mobile and desktop approaches
    using Balsamiq. Throughout the course of developing the website, I have deviated from the wireframes in certain
    sections. This is mainly due to me discovering a better design during the development, or issues with implementing
    the feature. </p>



<p>The wireframes have been uploaded with the rest of my project and can be viewed <a target="_blank"
        href="documents/Wireframes">here.</a></p>

<h3>User Stories</h3>
<p>In the development stage of the project, I generated a number of user stories which heavily influenced the design
    decisions taken throughout the development of the application. They are as follows:</p>

<ul>
    <li>As a user, I would like to be able to find new, popular courses to play around the country.</li>

    <li>As a user, I would like to be able to find golf courses which have a good reputation so as to ensure its
        quality.</li>

    <li>As a user, I would like to discover new golf courses that I haven’t played before.</li>

    <li>As a user, I would like to create reviews in order to allow me to share my experience of a golf course with
        other users.</li>

    <li>As a user, I would like to see featured and popular courses when I first enter the site.</li>

    <li>As a user, I would like to go directly to the golf courses website.</li>

    <li>As a user, I would like to be able to manage a number of aspects around the creation and management of golf
        courses on the website.</li>

</ul>

<h2>Features</h2>

<h3>Existing Features</h3>

<h4>Feature 1 – User Registration</h4>
<p> The user is able to register as a member of the site, in order to access features of site, such as being able to
    leave reviews. The feature was implemented as I needed to provide a secure way to enable user to interact with the
    site and give traceability to the reviews that were being left on the site. It is not a necessity for users to
    register in order to use the site, however this greatly enhances their experience. </p>

<h4>Feature 2 – User Login</h4>
<p> If the user has valid login details, they are able to log into the site which enables them to access more features.
    The feature was implemented in this way to allow only registered users certain privileges when interacting with the
    site. If this was not the case, anybody could access these features, which could lead to issues. Another element of
    this feature is to distinguish between admin users, as admin users have further features which can be taken
    advantage of, which will be explained later. </p>

<h4>Feature 3 – Standard Registered Users</h4>
<p> The standard user has access to all features regarding the review system. The feature was implemented in this way to
    ensure that only traceable users had the ability to affect the content that appeared on the website. For obvious
    reasons, this is quite an important feature, as it prevents spam, security risks and other such issues that could be
    present from all users having access to the review system. </p>

<h4>Feature 4 – Review System</h4>
<p> The review system allows users to create and manage reviews that they may want to leave on selected golf courses.
    The reason this system was implemented was to make the website more engaging and authentic. This is because dynamic
    content created by users such as reviews, helps to add value to a user’s visit. Furthermore, having this ability is
    fundamental to the functionality of this site, as reviews are able to allow users to actively contribute to the
    rankings of the golf courses on the website. This all helps to increase the usability of the site for other members.
</p>

<h4>Feature 5 – Administrative user</h4>
<p> An administrative user has access to more features of the course such as the Golf course management system. The
    feature was implemented in this way in order to allow only select users the ability to create and manage the golf
    courses on the site. This is important as it means that only trusted individuals are able to update content for the
    courses, meaning no malicious actions can be taken affect rival courses for instance. </p>

<h4>Feature 6 – Golf Course Management System</h4>
<p> The golf course management system allows admin users to create and manage golf courses for other users of the site
    to interact with. The main reason this system was implemented was to ensure that only verified users would be able
    to access some of the most critical features of the site. By limiting the course content management to certain
    users, this means that greater control can be taken in order to ensure only correct information is posted on the
    site in regard to the various golf courses on the site. The management system main focus is to allow users to not
    only create new golf courses on the site, but also gives them the ability to edit and also delete courses. This
    would prove very useful in situations where an aspect of a site changes such as the par of the course. </p>

<h4>Feature 7 – Featured Course</h4>
<p>The home page contains a featured course section, which highlights a random course from the database, every time the
    user visits the homepage. This was implemented in this way to expose users to different courses that they may not
    normally come across or know existed. This is also very beneficial to course owners, as it may encourage more
    golfers to come and visit their golf course. </p>

<h4>Feature 8 – Popular Courses</h4>
<p>The home page contains a number of popular courses, which are filtered based on the number of reviews each course
    has. The reason the feature has been implemented in this way, is that a course with more reviews, is more likely to
    be of a higher quality, due to the number of golfers playing there. This again will allow users to be exposed to
    courses that they not have seen before, which could give them a new place to play. </p>


<h4>Feature 9 – Course Search</h4>
<p>The site contains a comprehensive search system, which allows users to search for golf courses by either name,
    region, rating or a combination of all three. The reason this feature was implemented was to allow users a quick and
    efficient way to search the courses that the website contains. This will allow users to search for the courses they
    are interested in and may also allow them to find courses that they haven’t seen before. Users are able to see the
    important information from </p>

<h3>Features left to implement</h3>

<p>The following features are things I would like to include in the future. Currently a limit in time or lack of
    understanding has prevented me from implementing these features in the current build. However, I will look to add
    these going forward. </p>

<h4>Feature 1 – User Management Screen</h4>
<p>One feature I would like to add to the application going forward would be a user management screen, that
    administrators could only access. This would allow admins to enable over users administrator rights. This would be
    useful as it would streamline the current system of Course owners having to get in touch with the site owners in
    order to request changes/new courses to be implemented.</p>

<h4>Feature 2 – Search functionality on manage course system</h4>
<p>Another feature I would like to add to the application going forward would be to add a search function similar to
    that on the search part of the site. This would streamline the process for administrators when it came to finding
    specific courses to manage. Currently admins are required to find the course in the list or searching for the course
    and viewing it in the standard way, which could be considered inefficient. By adding this feature, it will make it
    easier for admins to manage the sites content.</p>

<h4>Feature 3 – Search functionality on manage review system</h4>
<p>One other feature that I would like to add to the application in future would be to add a search function similar to
    the one described above to the manage review system. This would make it more efficient for users with a large number
    of reviews to quickly find the specific one they are looking for, which would improve the user experience. </p>

<hr>

<h2>Technologies Used</h2>

<h3>HTML, CSS & JavaScript</h3>
<p>Used as the base languages in this project:</p>
<ul>
    <li>HTML: <a target="_blank" href="https://www.w3.org/html/">https://www.w3.org/html/</a></li>
    <li>CSS: <a target="_blank" href="https://www.w3.org/Style/CSS/">https://www.w3.org/Style/CSS/</a></li>
    <li>JavaScript: <a target="_blank"
            href="https://www.w3.org/standards/webdesign/script">https://www.w3.org/standards/webdesign/script</a></li>
</ul>

<h3>Materialize</h3>
<p>
    The project uses the Materialize framework and a start template in order to assist with the styling and look of the
    website. This can be seen with items such as the forms, card and parallax images.
</p>
<a target="_blank" href="https://materializecss.com/">https://materializecss.com/</a>

<h3>JQuery</h3>
<p>The project uses JQuery to help execute certain Materialize and JavaScript features such as with DOM manipulation and
    modal functionality .</p>
<a target="_blank" href="https://jquery.com/">https://jquery.com/</a>

<h3>Google Fonts</h3>
<p>The project uses Google Fonts to provide the ‘Roboto’ font that is used as the applications main font.</p>
<a target="_blank" href="https://fonts.google.com/">https://fonts.google.com/</a>

<h3>Font Awesome</h3>
<p>Used in order to provide a variety of Icons such as the ones used in the social section in the footer.</p>
<a target="_blank" href="https://fontawesome.com/">https://fontawesome.com/</a>

<h3>Microsoft’s VS Code</h3>
<p>VS Code has been used throughout the project as my IDE. </p>
<a target="_blank" href="https://code.visualstudio.com/">https://code.visualstudio.com/ </a>

<h3>Git & GitHub</h3>
<p>Git and GitHub have been used throughout the project as a way to manage version control of the web application and
    its code. </p>
<a target="_blank" href="https://github.com/">https://github.com/</a>

<hr>

<h2>Resources</h2>

<p>Throughout the course of the project I also used the following resources to assist me in creating the application:
</p>

<ul>
    <li><a target="_blank" href="https://www.w3schools.com/">https://www.w3schools.com/</a></li>
    <li><a target="_blank" href="https://stackoverflow.com">https://stackoverflow.com</a></li>
    <li><a target="_blank" href="https://tinypng.com/">https://tinypng.com/</a></li>
    <li><a target="_blank" href="https://developer.mozilla.org/en-US/">https://developer.mozilla.org/en-US/</a></li>
    <li><a target="_blank" href="https://www.quora.com/">https://www.quora.com</a></li>
    <li><a target="_blank" href="https://www.google.com/">https://www.google.com</a></li>
    <li><a target="_blank" href="https://www.youtube.com/">https://www.youtube.com</a></li>

</ul>

<hr>

<h2>Testing</h2>
<p>All testing that I have completed in regards to the user story can be viewed on a separate document <a
        target="_blank" href="documents/Testing/Testing.md">here</a></p>

<h3>Issues Encountered</h3>
<p>Throughout the course of my testing, I discovered a few bugs which I have detailed below:</p>
<ul>
    <li>One issue that I encountered in my testing, was when viewing paginated content and refreshing on the page. This
        would cause the application to error which would require me to load another page. </li>
    <li>Another issue that I encountered was with my search functionality. I found that when searching in lower case or
        only typing parts of a courses it wouldn’t retrieve the correct course, e.g. typing ‘Selby’ wouldn’t bring back
        ‘Selby Golf Course’ </li>
    <li>I also encountered an issue where my login system would not use if the user did not enter their email address
        exactly how they entered it, in terms of capitalization. This meant that a user wouldn’t be able to login
        despite the email being correct. </li>
    <li>One other issue I encountered was when trying to populate a form with existing information, using the WTForms
        package. This meant that the form wouldn’t load the correct information, when a user loaded the existing form.
    </li>

</ul>

<h3>Steps taken to resolve issues</h3>
<ul>

    <li> When I had initially created my pagination system, I hadn’t used page numbers. Instead I created this just with
        a Boolean check to see if there was another set of content to load. As a result, this meant once the user had
        entered into the pagination system, if they refreshed the page, the site wouldn’t know where user was in the
        pagination set hence the error. In order to rectify the issue, I had to refactor my existing code to utilise
        page numbers, which meant that the if a user refreshed in the pagination system the site would know what content
        should be shown based on the page number in the URL. This was especially good for me, as it helped me to
        understand pagination a lot more. </li>

    <li>When diagnosing the issue with the search system, I found that it was looking for an exact match to the value
        that was entered in the search system. As a result, if a user only entered a part name, this wouldn’t match with
        any records in the database. In order to rectify this, I had to use a $Regex (Regular Expression) operator. This
        would allow me to search the records in the DB based on terms which matched the Course Name field. This
        ultimately allowed the user to be able to search with key words, such as Selby, Valley etc.</li>

    <li>I found that when the user attempted to login to the site using the correct email, but with a capital letter for
        instance. This would prevent the user from logging in and would result in it appearing to the user that the user
        details were incorrect. I found the issue was with the part of login function where it searched the DB for a
        matching email. As my records are all stored in lowercase, this meant the user would never be found as the terms
        didn’t match failing the login. TO rectify this, I had to change this by making sure the email entered was put
        into a lowercase format first and then used to search the DB. This allowed me to resolve the issue. </li>

    <li>I found that when a user tried to edit an existing item such as a course, the information would not load
        correctly after I implemented WTForms for my form control. I found the solution to this issue was to preload the
        form with an object of the data on instantiation of the form class. This meant that the form would be given all
        the information it required in order to load the form correctly.</li>

</ul>

<h2>Deployment</h2>

<p>I have deployed this project using Heroku and this can be found here: <a target="_blank"
        href="https://play-golf-course-finder.herokuapp.com/ "> https://play-golf-course-finder.herokuapp.com/</a></p>
<p>In order to deploy Play Golf! the following steps were taken:</p>

<ol>

    <li>I firstly logged into Heroku and created a new application on the EU server as this is my closest region.</li>

    <li>Once the application was setup, I created my environment variables in order to allows the application to connect
        to the MongoDB database and to utilise its secret key.</li>


    <li>Once the environment was setup I set the Heroku application as a remote git origin, which would allow me to push
        my project to the application.</li>


    <li>Before pushing the project, I firstly had to create a requirements file using the python pip tool. This creates
        a file which when run, will allow pip to download all of the necessary dependencies in order to allow the
        application to run. </li>


    <li>Another file that needed creating before deployment is the Procfile. This file basically tells the Heroku server
        that Python is the language that is used.</li>

    <li>Once these files have been created, the file could be pushed to Heroku which deployed the site. </li>

</ol>

<hr>

<h2>Credits</h2>

<h3>Images</h3>
<h4>Disclaimer</h4>
<p>Please note this project is for educational purposes only. </p>


<ul>

    <li>Images used in the slider and parallax sections were obtained from<a href=”https://unsplash.com/”
            target=”_blank”>Unsplash</a></li>

    <li>Knight for the back of the card image was taken from Google images</li>

</ul>
<h3>Acknowledgements</h3>
<p>The website takes inspiration from the Code Institutes Task Manager – Mini Application and the Parallax template
    created by Materialize.</p>

<p>Thank you to members of the Slack community for assistance when I was encountering issues during the development and
    to my family friends for assisting with the testing of this website.</p>