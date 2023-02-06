# StudyBud - A demo project built Django - Python.
<p> To run the server: To go Project folder and run this command <b>python3 manage.py runserver<b></p>

<h2>Database & Admin Panel</h2>
<h4>Database related commands:</h4>
<ul>
    <li>1st run the command: "python manage.py migrate" to create the required tables for Admin, auth, contenttypes and sessions</li>
    <li>In the base app directory: Create the model class within "models.py" file. </li>
    <li>then create a migration file using command: "python manage.py makemigrations". It will create the migration file for the latest models classes.</li>
    <li>then run the command: "python manage.py migrate" to the migration files to create the tables</li>
</ul>
<h4>Adminpanel related commands:</h4>
<ul>
    <li>1st to open the default Admin Dashboard enter the url(http://127.0.0.1:8000/admin) into your browser.</li>
    <li>Now, its asking to enter the super admin user and password</li>
    <li>To create a super user from the command type: "python manage.py createsuperuser" and then follow the instructions.</li>
</ul>