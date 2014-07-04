import cherrypy
from mako.template import Template
from random import randint

from contextlib import contextmanager
import os


class MainApp:
    @cherrypy.expose
    def default(self, *args, **kwargs):
        #return 'Hello World'
        page = Template(filename='./template/page.html')
        return page.render(data='Random Number : '+str(randint(1,100)))
    #
#


#

@contextmanager
def serve():
    cherrypy.config.update({
    'engine.autoreload.on': False,
    'tools.sessions.on': True,
    'server.socket_host': '127.0.0.1',
    'server.socket_port': 8080,
    })

    config = dict()
    '''config = {
    '/content': {
    'tools.staticdir.on': True,
    'tools.staticdir.dir': os.path.abspath(os.path.join(os.curdir, 'content')),
    }
    }'''
    root = MainApp()
    cherrypy.tree.mount(root, '/', config)

    cherrypy.engine.start()

    yield

    cherrypy.engine.stop()
    cherrypy.engine.exit()

#

if __name__ == '__main__':
    with serve():
        print('\n *** Press Enter to exit web server ***\n')
        input()
    #
#

