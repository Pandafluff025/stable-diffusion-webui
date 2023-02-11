<<<<<<< HEAD
import os
from modules import paths


def preload(parser):
    parser.add_argument("--lora-dir", type=str, help="Path to directory with Lora networks.", default=os.path.join(paths.models_path, 'Lora'))
=======
import os
from modules import paths


def preload(parser):
    parser.add_argument("--lora-dir", type=str, help="Path to directory with Lora networks.", default=os.path.join(paths.models_path, 'Lora'))
>>>>>>> ea9bd9fc7409109adcd61b897abc2c8881161256
