# digiqt

1. for updating the top 250 movies rating in the database, we could have a lambda function with cron job or schedule of the task of celery with request python library that run every or something!


2. since our use-case can is sorting, searching and reading kind of stuff. i think probably go with NoSQL database like MongoDB however i'll be using sql database with indexing on fields like name, rating date, etc
, however, I'll be using Redis databse for the cacheing

3. for logging of aws lambda function we couold use CloudWatch and for django level we can use django's defautl django loging module.

4. we can aslo use trasction sort of things then lambda get's fauilded in that case we can revert to their acutally stage.
5. for testing api response time(profiling  ) i have used dajngo tool bar


![1](/django_tool_bar/cache_details.png)
![2](/django_tool_bar/data_from_cache.png)

![3](/django_tool_bar/sql_query_details_can_see_that_no_query_movie_list.png)



djagno admin user name and pass and url
username: jamil
password: hellohello
url: localhost:8000/admin


used black linting
used slug field for SEO purpose
used VSCode for Coding




The project will be available at 127.0.0.1:8000.

    python 3.8
    Django 3.x







could be done/improvements 

    1. django logging modulde
    2. o-auth toolkit
    3. slug field for SEO purpose(not needed in apis)
    4. override djagno's default user module
    5. deployment on heroku with CD 





tools/technoliges  that have used

    - django drf for api
    - filter and search  drf filter
    - for debug django tool bar
    - redis for performance
    - sqlite for database 



