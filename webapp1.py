import cherrypy

from contextlib import contextmanager


class MainApp:
    @cherrypy.expose
    def default(self, *args, **kwargs):
        return 'Hello World'

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
    root = MainApp()
    cherrypy.tree.mount(root, '/', config)

    cherrypy.engine.start()

    #yield
    input("Enter to exit...")

    cherrypy.engine.stop()
    cherrypy.engine.exit()

#

if __name__ == '__main__':
    serve()
    #with serve():
        #print('\n *** Press Enter to exit web server ***\n')
        #input()
    #
#

