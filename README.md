# Flask-application

It is a developed RESTful API based on Flask. The interface supports methods for searching for a movie by *id*, *title*, and release *year*, as well as issuing *recommendations* at the user's request. This application works with a database of IMBD movies taken from the site https://datasets.imdbws.com/title.basics.tsv.gz

The program consists of two files. `main.py` launches Flask application and calls file data retrieval `methods.py`. Optionally, the program can be run from the Docker container, having previously built the image, and without it.



## Dockerizing app

**If you don't need to run this application from Docker, you must skip the below commands and run the following commands after them**
+ `docker build -t movies .`
+ `docker run -d -p 5000:5000 movies`

## Application launch and test requests
The application is launched in the standard way using the python command, if you use any command line or using the launch buttons in your development environment.
The next step is to check the server is working. Alternatively, you can simply write `127.0.0.1:5000` to your address bar. You will see the **Hello** message in a simple html page.

In this application, *three GET requests* and *one POST request* are implemented according to the application description at the beginning. This is described in the `main.py` file.

### The first option is using a browser
+ #### GET by id
  ![](https://github.com/TheEverglow/Flask-app/blob/main/screenshots/movie_id.PNG "Необязательный титул")
+ #### GET by title
   ![](https://github.com/TheEverglow/Flask-app/blob/main/screenshots/movie.PNG "Необязательный титул")
+ #### GET by release year
   ![](https://github.com/TheEverglow/Flask-app/blob/main/screenshots/year.PNG "Необязательный титул")
+ #### POST for recommendations (with using any software, for example, on the screen it can be seen POST request in Chrome extension that is called as "RESTED") 
   The request body contains a JSON document containing a non-empty list of binary movie ratings, that is, (movie_id, rating) pairs. For example, `127.0.0.1:5000/suggest/3` means a request to issue 3 recommendations. 
   The response body contains a JSON document containing a list of H recommended movies in the format (movie_id, number). Movie rating (predicted rating) is generated randomly in the file methods. The list of films is sorted in descending order of rating. The recommendations cannot include those films that the user has already rated (that is, those that came in the request body).
   
   ![](https://github.com/TheEverglow/Flask-app/blob/main/screenshots/suggest.PNG "Необязательный титул")
   
### The second option is using a `curl` command for console
+ #### Curl GET by id
  ```
  $ curl -X GET 127.0.0.1:5000/movie_id/tt0000022
  ```
  Request result
  ```
  {
    "tconst": "tt0000022",
    "titleType": "short",
    "primaryTitle": "Blacksmith Scene", 
    "originalTitle": "Les forgerons",   
    "isAdult": "0",
    "startYear": "1895",
    "endYear": "\\N",
    "runtimeMinutes": "1",
    "genres\n": "Documentary,Short\n"   
  }
  ```
+ #### Curl GET by title
  ```
  $ curl -X GET 127.0.0.1:5000/movie/Carmencita
  ```
  Request result
  ```
  [
    {
      "tconst": "tt0000001",
      "titleType": "short",
      "primaryTitle": "Carmencita",
      "originalTitle": "Carmencita",
      "isAdult": "0",
      "startYear": "1894",
      "endYear": "\\N",
      "runtimeMinutes": "1",
      "genres\n": "Documentary,Short\n"
    },
    {
      "tconst": "tt0453643",
      "titleType": "short",
      "primaryTitle": "Carmencita",
      "originalTitle": "Carmencita",
      "isAdult": "0",
      "startYear": "1897",
      "endYear": "\\N",
      "runtimeMinutes": "\\N",
      "genres\n": "Short\n"
    }
  ]
  ```
+ #### Curl GET by release year
  ```
  $ curl -X GET 127.0.0.1:5000/year/1894
  ```
  Request result
  ```
  {
    "tconst": "tt8742740",
    "titleType": "short",
    "primaryTitle": "Chat En Chute Libre",
    "originalTitle": "Chat En Chute Libre",
    "isAdult": "0",
    "startYear": "1894",
    "endYear": "\\N",
    "runtimeMinutes": "\\N",
    "genres\n": "Short\n"
  }
  ```
+ #### Curl POST for recommendations
  ```
  $ curl -d '{ "likes": { "tt0000001": 1, "tt0000002": 0, "tt00000010": 0 }}' -H "Content-Type: application/json" -X POST 127.0.0.1:5000/suggest/5
  ```
  Requset result
  ```
  {
    "ratings": {
      "tt5368654": 0.8040031576345136,
      "tt8339638": 0.6780302124054454,
      "tt8645720": 0.37887919587478647,
      "tt0459963": 0.3745079668387131,
      "tt0173364": 0.33233496168265964,
      "tt10933950": 0.037933429676038855
    }
  }
  ```
