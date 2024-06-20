import logging
from django.http.response import HttpResponse
from django.contrib.auth.models import User


# creating the logger object
# where we are providing the same name as this current module name '__name__' (logdemo.views)
logger = logging.getLogger(__name__)
# and you can do that to all of the files to use logger in you application so that you can organize these logging and analyze them later


def index(request):
    logger.info("Testing the logger!")
    try:
        User.objects.get(pk=1)
    except User.DoesNotExist:
        logger.error("user with Id %s doesn't exist", 1)
    except Exception as e:
        logger.critical(e)
    return HttpResponse("Hello world")
