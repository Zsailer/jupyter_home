from jupyter_server.extension.handler import ExtensionHandler


class MainHandler(ExtensionHandler):

    # patch namespace to inject frontends into html page.
    @property
    def template_namespace(self):
        tn = super(MainHandler, self).template_namespace
        tn['frontends'] = self.frontends
        return tn

    def get(self):
        html = self.render_template("main.html")
        self.write(html)

    post = put = get
