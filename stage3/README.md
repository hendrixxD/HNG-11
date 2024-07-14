## Messaging System with RabbitMQ/Celery and Python Application behind Nginx

### Objective: Deploy a Python application behind Nginx that interacts with RabbitMQ/Celery for email sending and logging functionality.

1. Requirements:
  - Local Setup:
    Install RabbitMQ and Celery on your local machine.

  - Set up a Python application with the following functionalities:
    - An endpoint that can accept two parameters: `?sendmail` and `?talktome`.
    Endpoint Functionalities:
      - `?sendmail`: When this parameter is passed, the system should:
        - Send an email using `SMTP` to the value provided (e.g., `?sendmail=destiny@destinedcodes.com`).

  - Use RabbitMQ/Celery to queue the email sending task.
  - Ensure the email-sending script retrieves and executes tasks from the queue.
  - `?talktome:` When this parameter is passed, the system should:
    - Log the current time to `/var/log/messaging_system.log`.
    - the logs should be available on the endpoint : logs
  - Nginx Configuration:
    - Cnfigure Nginx to serve your Python application.
    - Ensure proper routing of requests to the application.
  - Endpoint Access:
    - Use `ngrok` to expose your local application endpoint for external access.
    - Provide a stable endpoint for testing purposes.
  - Documentation and Walk-through:
    - Record a screen-captured walk-through of the entire setup and deployment process.
    - Ensure the video covers:
      - RabbitMQ/Celery setup.
      - Python application development.
      - Nginx configuration.
      - Sending email via SMTP.
      - Logging current time.
      - Exposing the endpoint using ngrok.
      - Submit the endpoint and screen recording.
   - Submission Details:
     - Submission Requirements:
       - Provide the ngrok endpoint for testing.
       - Submit the screen recording walk-through.
       - Ensure all requirements are met and the application functions correctly.
 - Evaluation Criteria:
     - Functionality: All specified features must work correctly.
     - Clarity:
       - Code and configurations must be well-documented.
     - Presentation:
       - The screen recording should be clear and comprehensive.

### File Structure
```
-- stage3
   -- app
      -- __init__.py
      -- config.py
      -- task.py
      -- views.py
   -- ngix
      -- messaging
   -- .env
   -- .gitignore
   -- celery_worker.py
   -- run.py
   -- requirements.txt
   -- README.md
```
<hr>

### submision requirments met

1. sending email using SMTP at `/sendmail` endpoint
2. Logging the current time at `/talktome` endpoint
3. serrving the application using nginx
4. exposing the endpoint using ngrok and tested as well [here]('https://be96-2a05-d018-184-c400-9a02-51f8-f2db-19e5.ngrok-free.app/?sendmail=devhendrixx@gmail.com').

_NOTE_
How to run the app:
- spin up flask server:

  ```ssh
  python3 run.py
  ```
- spin up celery:

  ```ssh
  celery --app celery_worker.celery worker
  ```
- the application is served behind nginx and endpoints exposed using `ngrok`

  ```ssh
  ngrok http 80
  ```
 
  but dont wory, `ngrok` is already running in the background, you can go ahead with testing the endpoints at:
  - `sending mail`: https://be96-2a05-d018-184-c400-9a02-51f8-f2db-19e5.ngrok-free.app/?sendmail=devhendrixx@gmail.com
  - `logging the current time`: https://be96-2a05-d018-184-c400-9a02-51f8-f2db-19e5.ngrok-free.app/?talktome
  - `fetching logs`: https://be96-2a05-d018-184-c400-9a02-51f8-f2db-19e5.ngrok-free.app/logs

There is a file: `filer_perm.sh`:
  - you may get permission denied on `/var/log/messaging_system.log` when spinning up flask server
  - to solve that:
    ```ssh
    sudo bash file_perm.sh
    ```
    Or
    ```ssh
    bash file_perm.sh
    ```
    which ever that works for ya.
      

