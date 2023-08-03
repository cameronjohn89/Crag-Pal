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

## PostgreSQL

I have chosen PostgreSQL as the database system for my Flask API application for several reasons:
Reliability: PostgreSQL is known for its reliability and stability, making it a robust choice for handling critical data and applications.
Scalability: PostgreSQL can handle large amounts of data and is designed to scale well as the data size and application load grow.
ACID Compliance: PostgreSQL follows the ACID (Atomicity, Consistency, Isolation, Durability) properties, ensuring data integrity and consistency even in the face of system failures.
Open-Source: PostgreSQL is an open-source database system, which means it is free to use and has a large community of developers contributing to its development and improvement.
Extensibility: PostgreSQL allows the creation of custom data types, functions, and extensions, making it flexible and customizable to specific application needs.

Drawbacks compared to other database systems:
Complexity: PostgreSQL can be more complex to set up and manage compared to some other databases, especially for users who are new to relational databases.
Resource Consumption: PostgreSQL might require more system resources in terms of memory and CPU compared to lightweight databases like SQLite.
Learning Curve: If developers are already familiar with other database systems, the learning curve to work with PostgreSQL might be steeper.
Performance: While PostgreSQL is generally performant, other databases like NoSQL databases (e.g., MongoDB) might offer better performance for certain use cases, especially in scenarios with high write-intensive workloads.
No Native JSON Support: Although PostgreSQL has improved support for JSON data in recent versions, other NoSQL databases excel in handling JSON data natively.
Ultimately, the choice of database system depends on the specific requirements and characteristics of the application. PostgreSQL is an excellent choice for many scenarios due to its reliability, robustness, and extensive feature set adn this is why I have chosen to use it for this API. Importantly to note, other databases might be better suited for specific use cases, especially when it comes to handling specific data types or performance optimization that could be included in later versions of this API.

## ERD

User Entity:
user_id (primary key)
username
email
password
first_name
last_name
created_at
updated_at

Crag Entity:
crag_id (primary key)
name
location
description
created_at
updated_at

Route Entity:
route_id (primary key)
crag_id (foreign key referencing Crag entity's primary key)
user_id (foreign key referencing User entity's primary key)
name
difficulty_level
type
description
photo
created_at
updated_at

Country Entity:
country_id (primary key)
name
created_at
updated_at

Climb Entity:
climb_id (primary key)
user_id (foreign key referencing User entity's primary key)
route_id (foreign key referencing Route entity's primary key)
date
notes
created_at
updated_at

These are the entities of the climbing application, which are users, crags, routes, countries, and climbs.
The User entity represents the climbers using the application, with associations to routes and climbs. The Crag entity represents the climbing locations, associated with routes. The Route entity represents climbing routes, associated with crags and users. The Country entity represents the countries associated with crags. The Climb entity represents the logging of climbs by users on specific routes.

## Database Relations
User Entity:
One user can log multiple climbs.
One user can have multiple collections of climbs.

Crag Entity:
One crag can have multiple climbing routes.
One crag can be located in one country.

Route Entity:
One route belongs to one crag.
One route can be logged in multiple climbs.

Country Entity:
One country can have multiple crags.

Climb Entity:
One climb is performed by one user.
One climb logs one route.

When looking at these relationships, I can define the database relations using foreign keys:

User to Climb:
The user_id in the Climb table is a foreign key that references the user_id in the User table.

Crag to Route:
The crag_id in the Route table is a foreign key that references the crag_id in the Crag table.

Route to Climb:
The route_id in the Climb table is a foreign key that references the route_id in the Route table.

Crag to Country:
The country_id in the Crag table is a foreign key that references the country_id in the Country table.

These foreign key relationships ensure that the data in my database is properly connected and allows for efficient querying and retrieval of related information.
When defining my database models using SQLAlchemy, I will use these foreign key relationships to specify the associations between the entities.

## ORM

An Object-Relational Mapping (ORM) is a programming technique that allows developers to interact with a relational database using object-oriented programming principles. ORM libraries provide a way to map database tables to object classes and simplify database interactions. Here are the key functionalities and benefits of using an ORM:
Abstraction of Database Operations: ORM abstracts away the complexities of SQL queries and database interactions. Developers can work with high-level object-oriented code instead of writing raw SQL queries, making the code more readable and maintainable.
Cross-Platform Support: ORM libraries typically support multiple database systems, allowing developers to switch between different database backends without changing the application code.
Data Modeling: ORM provides a way to define data models as Python classes (or other programming language classes). These classes represent database tables, and each instance of the class corresponds to a row in the table. This modeling simplifies database schema design and keeps the code organized.
CRUD Operations: ORM simplifies common database operations, such as creating, reading, updating, and deleting records (CRUD operations). Developers can use object-oriented methods like save(), delete(), and query() instead of writing SQL statements for each operation.
Data Validation: ORM often includes built-in data validation features that help ensure data integrity and prevent invalid data from being stored in the database.
Relationships and Joins: ORM handles complex relationships between tables and allows developers to perform JOIN operations without writing explicit SQL joins.
Database Migration: Many ORM frameworks support database migration tools, making it easier to manage changes in the database schema over time without manually writing SQL migration scripts.
Performance Optimization: Advanced ORM implementations can optimize database queries automatically, reducing the number of queries and minimizing data retrieval overhead.
Security: ORM libraries help prevent SQL injection attacks by using parameterized queries and escaping user input properly.
Unit Testing: ORM can facilitate unit testing by providing mock database implementations, allowing developers to test their code without interacting with the actual database.
Code Reusability: ORM allows developers to encapsulate database operations in model classes, making it easier to reuse code across different parts of the application.
In summary, ORM simplifies database interactions by providing a high-level object-oriented interface, promoting code organization, and improving overall developer productivity. It abstracts the complexities of database management, making it easier to work with databases and reducing the amount of boilerplate code in the application.

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
- Create a climbing route or problem.
- Few existing routes and problems.
- Select a route and log your climb by providing the necessary details.
- View your logged climbs and track your climbing progress.

## API Endpoints

auth_controller.login              POST     /login
auth_controller.register           POST     /register
crag_controller.create_crag        POST     /crag
crag_controller.get_crag_by_id     GET      /crag/<int:crag_id>
crag_controller.get_crags          GET      /crag
route_controller.create_route      POST     /route
route_controller.get_route         GET      /route/<int:route_id>
route_controller.log_climb         POST     /route/<int:route_id>/climbs
static                             GET      /static/<path:filename>
user_controller.create_collection  POST     /users/<int:user_id>/collections
user_controller.get_user           GET      /user/<int:user_id>
user_controller.update_user        PUT      /user/<int:user_id>

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.


