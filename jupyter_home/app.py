from jinja2 import Environment, FileSystemLoader

from jupyter_server.extension import ExtensionApp

from .paths import DEFAULT_STATIC_FILES_PATH, DEFAULT_TEMPLATE_PATH_LIST
from .handler import MainHandler


class JupyterHome(ExtensionApp):

    name = "jupyter-home"
    load_other_extensions = True
    frontend = False

    template_paths = DEFAULT_TEMPLATE_PATH_LIST
    static_paths = DEFAULT_STATIC_FILES_PATH

    default_url = '/home'

    def initialize_templates(self):
        self.jinja2_env = Environment(
            loader=FileSystemLoader(self.template_paths), 
            autoescape=True,
            **self.jinja2_options
        )

        # Add the jinja2 environment for this extension to the tornado settings.
        self.settings.update(
            {
                "{}_jinja2_env".format(self.extension_name): self.jinja2_env 
            }
        )

    def initialize_handlers(self):
        self.handlers.append(
            ('/home', MainHandler)
        )


main = JupyterHome.launch_instance