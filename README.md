# CoZaPraci

CoZaPraci is a website where people can share their honest descriptions of their previous or current jobs as well as some of the stereotypes and misconceptions 
connected with their profession.

It is currently deployed at [https://cozapraci.up.railway.app/](https://cozapraci.up.railway.app/).

The motivation for this project was a similar page called https://whatforwork.com/. Since I was not able to find something similar in czech language I decided 
to build my own. 

Technologies used are [Django](https://www.djangoproject.com/) framework for BE and Django templates + [django-unicorn](https://www.django-unicorn.com/) for FE. 

###  How to run the project locally 

1, Install all dependencies from `requirements.txt` into virtual enviroment.

2, Navigate to `cozapraci/settings.py` and set `DEBUG = True`.

3, In the same file set a variable `SECRET_KEY` with a generated string (you can generate one [here](https://django-secret-key-generator.netlify.app/) for example).

4, Create DB migrations and run them `python manage.py makemigrations` `python manage.py migrate`

5, Run the local server with `python manage.py runserver`
