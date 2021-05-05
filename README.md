# Courses Catalogue (CCatalogue)

This is a simple web application which supports CRUD operations with the Catalogue of Courses.
It is based on Flask framework.

## Dependencies

List of dependencies and required modules

## Preset

Set up Flask-related environment variables:

```bash
export FLASK_APP=ccatalogue
export FLASK_ENV=development
```

Initialize the database

```bash
flask init-db
```

## Run

Run the application:

```bash
flask run
```

It will start the web-applicaiton server on port 5000:

http://127.0.0.1:5000

## Test

Application contains the next number of endpoints:

```text
Request type	Endpoint		Consumes	Produces		Description

GET 		courses/		-		json (list(object))	get list of all courses
GET		courses?name={name}	-		json (object)		get courses filtered by name
GET		courses?date={date}	-		json (list(object))	get courses filtered by date
POST 		courses/		json		json (id)		add course to the catalogue
GET		courses/{id}		-		json (object)		get course details
PUT		courses/{id}		json		json (object)		update course
DELETE		courses/{id}		-		json (id)		delete course
```

