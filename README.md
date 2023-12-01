<div align="center">
  <img src="https://github.com/kanugurajesh/Restaurant/assets/120458029/38824a97-4cc0-4a16-9d7b-42ca6c0604bd" alt="Restaurant" width="200" height="200">
</div>

# Restaurant

Welcome to the Restaurant Application! This application allows you to explore the menu, reserve seats, and seamlessly integrates with Google Maps for an enhanced dining experience.

## Features

### 1. Menu Exploration
- Browse through a diverse menu with a wide range of delicious dishes.
- View detailed descriptions, prices, and images for each menu item.

### 2. Reservation System
- Easily reserve seats for your desired date and time.
- Receive instant confirmation and updates on your reservation status.

### 3. Google Maps Integration
- Find the restaurant location effortlessly using Google Maps integration.
- Get directions and discover nearby points of interest.

### 4. Virtual Environment Setup
- Simplified steps to set up a virtual environment for project isolation.
- Ensure smooth deployment and avoid conflicts with other Python projects.

### 5. Database Management
- Perform migrations to set up and manage the database.
- Keep your data organized and efficiently retrieve information.

### 6. Customizable Port Configuration
- Run the application on a default port (8000) or specify a custom port for flexibility.
- Easily adapt to your preferred environment and configurations.

### 7. Fedora Compatibility
- Step-by-step guide for setting up the virtual environment on Fedora.
- Ensure a smooth installation process on Fedora-based systems.


### Prerequisites
1. python installed on your machine(3.8+)

### setting up the project
1. setup virtualenv
2. switch into the virtualenv
3. Install the required modules <code>pip install -r requirements.txt</code>
4. perform migrations <code>python manage.py makemigrations</code>
5. migrate the database <code>python manage.py migrate</code>

### run the project
1. run the project by running the command <code>python manage.py runserver</code>
2. By default the port is 8000 but if you want to run on another port enter the port number after the runserver ( e.g <code>python manage.py runserver 8001 </code> it runs the project on 8001 port )

### setting up virtual env in fedora
1. Run the command <code>python -m venv myenv</code> this command creates an virtual environment
2. Now activate the virtual environment <code>source myenv/bin/activate</code>
3. Install the required modules by running the command <code>pip install -r requirements.txt</code>

## DEMO
<a href="https://youtu.be/Q5FUZfroKzA?feature=shared"><img src="https://github.com/kanugurajesh/Restaurant/assets/120458029/b3e6e45a-943e-4c2e-8fa4-9b8a09ff46bc" alt="demo" width="200" height="200"/></a>
