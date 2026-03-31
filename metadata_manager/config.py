try:
    from pyutils.utils import Dir_util
    PROJ_DIR = Dir_util.get_cur_dir(__file__)
except ImportError:
    from pathlib import Path
    PROJ_DIR = Path(__file__).parent.resolve()

import os

OUTPUT_DIR = os.path.join(PROJ_DIR, "output")
if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)
