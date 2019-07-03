from quickweb import controller
from random import randint


class Controller(object):

    @controller.publish
    def default(self, *args, **kwargs):
        return "Hello OpenShift "+str(randint(0, 100))