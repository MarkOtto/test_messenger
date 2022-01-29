# API-backend for simple messaging

## How to run

1. Install docker-compose (v1.26.0 works)
2. Update the environment variables in .env.dev
3. Build the images and run the containers in detached mode using:

    ```sh
    $ cp .env.dev_example .env.dev 
    $ docker-compose build
    $ docker-compose up -d
    ```

4. Create database & superuser
   
    ```sh
    $ docker-compose exec web python manage.py migrate
    $ docker-compose exec web python manage.py createsuperuser 
    ```

5. Visit localhost:8000/admin for administrating your application.

## How to use

1. The example is working on http://89.108.78.225:8000


2. The link for Postman collection with requests:

   https://www.getpostman.com/collections/d6ac1d2494bce5b29311  


3. Enter Django admin
   
   superuser credentials:

   
       user1   
       123456aZ


4. Create New user with login + password

* POST Token = /api/token/ • to get users's token (credentials must be provided in request's body)
* POST Send = /api/send/ • to send the message (token must be provided in request's header, message details in body)   
* GET Messages = /api/messages/ • to list all the messages for the user (token must be provided in request's header, pagination parameter /?page=2 in url)
* GET Inbox = /api/inbox/ • to list inbox messages for the user (token must be provided in request's header, pagination parameter /?page=2 in url)
* GET Sent = /api/sent/ • to list sent messages for the user (token must be provided in request's header, pagination parameter "/?page=2" in url)
* GET Users = /api/users/ • to list users / address book (token must be provided in request's header)
* GET Message = /api/message/ • to get message details (token must be provided in request's header, id parameter "/1" in url).



