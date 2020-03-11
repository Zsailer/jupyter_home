from .app import JupyterHome  # noqa

def _jupyter_server_extension_paths():
    return [
        {
            'module': 'jupyter_home',
            'app': JupyterHome
        }
    ]