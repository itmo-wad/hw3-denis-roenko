# hw3-denis-roenko

## Optimal part
Web application, which can authenticate user with password:

1. User registration on http://localhost:5000/register/ 
2. User authentication on http://localhost:5000/login/
3. User`s personal cabinet on http://localhost:5000/cabinet/
4. On the cabinet page, user can press "Log out" button, which send him to http://localhost:5000/logout/ endpoint.

The information about user`s authentication is stored in flask session. On register and login endpoints it is created. The logout endpoint destroys session and sends user to login page.