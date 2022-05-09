import os.path as osp 
import glob 
import random 


def random_bg(dir_path:str, ext="png") -> str: 
    """ return an image path in random 
    """
    img_list = glob.glob(osp.join(dir_path, f"*.{ext}"))
    random.shuffle(img_list)

    return random.choice(img_list)