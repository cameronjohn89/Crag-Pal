# Crag Pal

Crag Pal is a web application that allows climbers to search for climbing crags, post new problems or routes, log their climbs, and manage their climbing collection. Users can search for crags by location, log climbs on specific routes, and keep track of their climbing achievements.
Although there is some websites with crags and routes/problems, they fall short. Normally you would need a specific websites for a geographical location to show the most updated crags/climbs. Ie. UKC for the United Kingdom and some of Europe, The Crag for Australia/Oceania, 27 Crags or Climb Europe for most of Europe. As mentioned this websites do have other locations but aren't as up to date as their counterpart. The difference between my application and these is also the edition of social media type posting and interactions that would be allowed on the API.
I believe that this API is hitting a hole in the market and fixing the lack of overall completeness the other sites have for different global regions.

## Features

- Create a new user/Login to existing user
- Search for climbing crags by location
- Create and post new routes/problems
- Log climbs on specific routes
- View detailed information about crags and routes
- Track personal climbing progress
- Manage user profile and preferences
- Interact with other user profiles

## Technologies Used

- Python
- Flask
- SQLAlchemy (ORM)
- PostgreSQL (Database)
- Marshmallow
- JavaScript
- Blinker
- Click
- Werkzeug
- Psycopg2
- Jinja2

## Installation

1. Clone the repository: `git clone https://github.com/cameronjohn89/Crag-Pal`
2. Navigate to the project directory: `cd crag-pal`
3. Install the required dependencies: `pip3 install -r requirements.txt`
4. Set up the database (PostgreSQL) and update the database configuration in `config.py`
5. Run the application: `python app.py`
6. Access the application in your browser at `http://localhost:5000`

## Usage

- Visit the homepage to search for climbing crags and browse available routes.
- Create an account or log in to start logging your climbs.
- Select a route and log your climb by providing the necessary details.
- View your logged climbs and track your climbing progress.

## API Endpoints

- `/crags` - GET: Retrieve a list of all crags
- `/crags/<crag_id>` - GET: Retrieve details of a specific crag
- `/routes` - GET: Retrieve a list of all routes
- `/routes/<route_id>` - GET: Retrieve details of a specific route
- `/routes` - POST: Create a new climbing route
- `/routes/<route_id>/climbs` - POST: Log a climb on a route

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.


