# True-Value-Access-Task
Here is the task for managing users data using django rest framework

<h2>Usage :</h2>
Please clone this repository for run this project.


    python manage.py makemigrations

    python manage.py migrate

    python manage.py runserver
    
   In your web browser enter these addresses

<h4>http://127.0.0.1:8000/account/api/users:</h4>
<h3>GET</h3>
<ul>
    <li>To list all the users.</li>
    <li>Also support some query parameters.</li>
  <h4>* Pagination</h4>
  <h4>* Searching by firstname and lastname</h4>
  <h4>* Ordering</h4>
</ul>
<h3>POST</h3>
<ul>
    <li>To create a new user</li>
</ul>
<h4>http://127.0.0.1:8000/account/api/users/id:</h4>
<h3>GET</h3>
<ul>
    <li>To get the details of the user</li>
</ul>
<h3>PUT</h3>
<ul>
    <li>To Update the details of the user</li>
</ul>
<h3>DELETE</h3>
<ul>
    <li>To delete the user</li>
</ul>
