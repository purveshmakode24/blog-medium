# BMedium
An online publishing platform. 

> BMedium is an online publishing platform. The platform is an example of social journalism, having a hybrid collection of amateur and professional people and publications, or exclusive blogs or publishers on BMedium, and is regularly regarded as a blog host..

#### Checkout "Disqus - A simple SAAS based discussion platform backend services using DRF" :point_right: [here](https://github.com/purveshmakode24/disqus-saas-drf)

### Live	
https://blog-medium.herokuapp.com

### Installation
- Fork the repo.
- Clone the repo.
```
git clone https://github.com/purveshmakode24/BMedium.git
```
```
cd BMedium
```
- Install dependencies
```
pip install -r requirements.txt
```

### Setup for Developement

- Set `DEBUG = True` in settings.py
- Uncomment the DATABASES settings for development and Comment the DATABASES settings for Production in settings.py.

### Database Migrations 

```
python manage.py makemigrations
```
```
python manage.py migrate
```

### Running
```
python manage.py runserver
```
- Head over to localhost:8000 in your browser.

## Contribution Guidelines
If you're new to contributing to Open Source on Github, please check out [this contribution guide](https://opensource.guide/how-to-contribute/) for more details on how issues and pull requests work.
