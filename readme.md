Hi!

This is a Flask project by David Cha on behalf of Eva Prokop and the cats she saves in my hometown, New York City.

Much of it has been pieced together from various Flask tutorials, all available online.

In the event that anyone actually reads this and has a question, just shoot me a message thru GitHub!

Thanks,

Dave

NB: config.py was removed in a later-than-initial commit since I had an email in there that I wouldn't want necessarily displayed. For this project to work, a config.py file should be within the same folder as runserver.py. Below is the proper layout:

# csrf on and secret key
CSRF_ENABLED = True
SECRET_KEY = 

# mail settings
MAIL_SERVER = 
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 
MAIL_PASSWORD = 

# db settings
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/catabase'
#DATABASE_CONNECT_OPTIONS = {}