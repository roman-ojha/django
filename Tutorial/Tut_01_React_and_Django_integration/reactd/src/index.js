/*
  -> now firstly we will build the react app:
      -> npm run build

  -> so firstly we need to connect "template" and react static assets
      -> so in build/index.html file
      -> so now in djang/djang/settings.py we will add react template in there:
          -> os.path.join(BASE_DIR, 'reactd/build')
      -> now we can use this template so now we need to connect to our urls.py file:
          -> from django.views.generic import TemplateView
           path('', TemplateView.as_view(template_name='index.html')),

      -> now we also want to connect to static and all those react static files for that we will go to 'settings.py' file:
          -> STATICFILES_DIRS = [
                os.path.join(BASE_DIR, 'reactd/build/static')]

      -> NOTE: through this configration every time we have to do:
            -> npm run build
            -> to build the application so that djano project can read the react app


    => if we want to use rest api for our need then firstly we have to create a 'views.py' and route path in 'urls.py' 
            -> and then to solve the 'CORS' policy error we have to install 
              -> pip install django-cors-headers
            -> then we have to add some code inside our 'settings.py':
                -> If you are happy for any domain to access your API then you can set the following:
                    -> CORS_ORIGIN_ALLOW_ALL = True
                -> If you do this, you will also need to set the following:
                    -> ALLOWED_HOSTS = ['*']
                    
                    -> MIDDLEWARE = [
                      'corsheaders.middleware.CorsMiddleware',
                      ]

                -> NOTE: Or Only enable CORS for specified domains:
                      -> CORS_ORIGIN_ALLOW_ALL = False
                      -> CORS_ORIGIN_WHITELIST = (
                          'http//:localhost:8000',
                          )

    => Github repo to understand in depth:
        -> https://github.com/divanov11/Django-React-NotesApp
*/


import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
