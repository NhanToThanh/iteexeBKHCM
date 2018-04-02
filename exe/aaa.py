from twisted.web import server, resource
#from twisted.internet import reactor, endpoint
class Simple(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return "<html>Hello, world!</html>"
site = server.Site(Simple())
#endpoint = endpoints.TCP4ServerEndpoint(reactor, 8080)
#endpoint.listen(site)
#reactor.run()