from jinja2 import Environment, FileSystemLoader

from jupyter_server.extension.application import ExtensionApp, ExtensionAppJinjaMixin

from .paths import DEFAULT_STATIC_FILES_PATH, DEFAULT_TEMPLATE_PATH_LIST
from .handler import MainHandler


class JupyterHome(ExtensionAppJinjaMixin, ExtensionApp):

    name = "jupyter-home"
    extension_name = "jupyter_home"
    extension_url = '/home'

    template_paths = DEFAULT_TEMPLATE_PATH_LIST
    static_paths = DEFAULT_STATIC_FILES_PATH

    def initialize_settings(self):
        extensions = self.serverapp._enabled_extensions
        frontends = {}
        for mod, extapp in extensions.items():
            if isinstance(extapp, ExtensionApp):
                if extapp.extension_name != self.extension_name:
                    frontends[extapp.extension_name] = extapp
        self.settings['jupyter_home_frontends'] = frontends

    def initialize_handlers(self):
        self.handlers.append(
            ('/home', MainHandler)
        )


main = JupyterHome.launch_instance