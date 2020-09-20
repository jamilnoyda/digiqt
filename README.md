# digiqt

1. for updating the top 250 movies rating in the database, we could have a lambda function with cron job or schedule of the task of celery with request library of python that runs every or something!

2. since our use-case is sorting, searching and reading kind of stuff. I think probably go with NoSQL database like MongoDB however I'll be using SQL database with indexing on fields like name, rating date, etc
, I'll be using Redis database for the caching

3. for logging of AWS lambda function we could use CloudWatch and for Django level, we can use Django's default django logging module.

4. we can also use trasction sort of things then lambda get's fauilded in that case we can revert to their actually stage.

5. for testing API response time(profiling) I have used django tool bar


![1](/django_tool_bar/cache_details.png)

![2](/django_tool_bar/data_from_cache.png)

![3](/django_tool_bar/sql_query_details_can_see_that_no_query_movie_list.png)


djagno admin username, pass and url
- **username:** jamil
- **password:** hellohello
- **url:** localhost:8000/admin

used black linting
used slug field for SEO purpose
used VSCode for Coding

The project will be available at 127.0.0.1:8000.

    python 3.8
    Django 3.x

could be done/improvements 

    1. django logging module
    2. o-auth toolkit
    3. slug field for SEO purpose(not needed in APIs)
    4. override djagno's default user module
    5. deployment on heroku with CD

tools/technologies  that have used

    - Django drf for api
    - filter and search  drf filter
    - django tool bar for debugging
    - Redis for performance
    - SQLite for database
