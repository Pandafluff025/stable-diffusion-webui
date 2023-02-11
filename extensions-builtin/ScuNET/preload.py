<<<<<<< HEAD
import os
from modules import paths


def preload(parser):
    parser.add_argument("--scunet-models-path", type=str, help="Path to directory with ScuNET model file(s).", default=os.path.join(paths.models_path, 'ScuNET'))
=======
import os
from modules import paths


def preload(parser):
    parser.add_argument("--scunet-models-path", type=str, help="Path to directory with ScuNET model file(s).", default=os.path.join(paths.models_path, 'ScuNET'))
>>>>>>> ea9bd9fc7409109adcd61b897abc2c8881161256
