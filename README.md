# PatchTracker (Backend)

<<<<<<< HEAD
## Description

> This repository contains the backend system of an application designed to display patch notes for Valorant and League of Legends. 

##
=======
> This repository contains the backend system of an application designed to display patch notes for Valorant. 

## Tech stack

* Django
* PostgreSQL
* Django Rest Framework (DRF)
* Beautiful Soup (bs4)

## Functionality
This Django-based backend collects data by scraping third party websites using bs4. The scraped data is stored into a PostgreSQL database via Django's ORM.
The data is accessed and served through the API developed using Django Rest Framework.

The backend provides the data to the front end developed in Swift. It utilizes the API to fetch and display the patch notes and other information like Valorant episodes and their respective versions.
You can access to the frontend repo here: https://github.com/Diegowh/PatchTracker-ios-app

## Default localhost API Root:
http://127.0.0.1:8000/ValorantPatchTracker/

### Endpoints
* GET `/episodes/`: Return all Episodes for Valorant (including Closed Beta).
* GET `/patchnotes/`: Return all Versions/Patch Notes for Valorant.
* GET `/contents/`: Return all content for each Version/Patch note for Valorant.
* GET `/contents/?patch_note=<patch_note_id>`: Returns the content for a specific patch note.

## Installation and Setup
> Here are the steps to run the backend on your local machine:

### Prerequisites
* Python 3.11.1
* Django 4.2.1
* PostgreSQL

### Steps
1. Clone the Repository
```
git clone https://github.com/Diegowh/PatchTracker-Backend.git
```
2. Set up a Virtual Environment and activate it
```
python -m venv .venv
```
3. Install the Dependencies
```
pip install -r requirements.txt
```
4. Create and configure the .env File: There is a `.env.example` file in the repository. Use this file as a reference to create your own `.env` file. Replace the placeholder values in your new `.env` file with your actual PostgreSQL database credentials.
5. Set up the Database:
```
psql -U postgres -c "CREATE DATABASE mydatabase"
```
6. Run the Migrations:
```
python manage.py makemigrations
python manage.py migrate
```
7. Update the Database:
```
python manage.py update_db
```
8. Run the Server:
```
python manage.py runserver
```

## Future scope

In the pipeline is the addition of League of Legends data to the app, allowing users to view the patch notes of both Valorant and LoL through a single, unified interface.

## Contributions

This project is open to contributions.

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit/) - see the LICENSE file for details.
>>>>>>> e78fb1255f6a04f43d2530ebaf1417fcd6dce78f
