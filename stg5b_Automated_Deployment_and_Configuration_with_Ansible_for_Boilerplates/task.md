# Automated Deployment and Configuration with Ansible for Boilerplates
Overview: You will be assigned one of the 7 boilerplates from Stage 4.
  - [here](https://github.com/hngprojects/hng_boilerplate_csharp_web/tree/devops)

Your task is to set up a new instance of the assigned boilerplate using Infrastructure as Code (IaC) with Ansible. The setup should include the following:
1. Clone and Deploy:
   - Clone the DevOps branch of your boilerplate repository to a Linux server.
   - Deploy the boilerplate application on the server.
2. Install Dependencies:
   - Install all dependencies required for your boilerplate to run, including databases and messaging queues.
3. Setup PostgreSQL:
   - Configure a PostgreSQL database.
   - Save the admin user and credentials in `/var/secrets/pg_pw.txt`.
4. Messaging Queue:
   - Set up any required messaging queue (e.g., RabbitMQ, Redis).
5. Application Configuration:
   - Ensure your application starts on port `3000`.
   - Set up Nginx to reverse proxy your application to `port 80`.
6. Logging:
   - Configure stderr logs to be saved in `/var/log/stage_5b/error.log` and stdout logs in `/var/log/stage_5b/out.log`.
   - Ensure both log files are owned by the hng user.
     
 ## Instructions:
  1. User and Directory Setup:
     - Create a user named hng with sudo privileges.
     - Clone your repository into the `/opt` directory with the name `stage_5b (i.e., /opt/stage_5b)`, and ensure it is owned by the hng user.
  2. Database and Dependencies:
     - Install PostgreSQL and save the admin credentials in `/var/secrets/pg_pw.txt`.
     - Install all application dependencies, including databases and messaging queues, and configure the environment variables or application settings accordingly.
  3. Application and Proxy Setup:
     - Ensure the application is running on `127.0.0.1:3000` without exposing port `3000` externally.
     - Install Nginx 1.26 and configure it to reverse proxy requests from port 80 to your application.
  4. Logging Configuration:
     - Set up logging so that
       - _stderr logs_ are written to `/var/log/stage_5b/error.log`, and
       - _stdout logs_ to `/var/log/stage_5b/out.log`, with both files owned by the hng user.

**Grading**
A mentor will run the Ansible playbook using the command:
  ```ssh
   ansible-playbook main.yaml -b
  ```
 with an `inventory.cfg` configuration file on a fresh `Ubuntu 22.04 server` with `Python 3.12`.
 
Ensure there are no errors during execution, as mentors will not be responsible for fixing any issues.

_NOTE: Do not containerize any of the applications._

**_In your Ansible file, specify hosts as hng (i.e., host: hng), as this is what will be used in the inventory file._**

<hr></hr>

_stage 5b Individual Task_ 
