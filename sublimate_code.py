import os
import json
import argparse


PARAMS_CONF = {"color", "font-style", "font-size", "font-weight"}


def load_json_conf(file_path):
    """
    Load configuration saved in JSON file

    Parameter:
        file_path (str) : Path of file

    Return:
        (dict) : Configuration data
    """
    assert isinstance(file_path, str), "Path must be a string"
    assert os.path.exists(file_path), "File path don't exist"

    with open(file_path, "r") as f:
        data_conf = json.load(f)

    return data_conf


def sublimate_keyword(code, keyword, conf_keyword):
    """
    Sublimate keyword with HTML tag
    
    Parameters:
        code (str) : Code to be treated
        keyword (str) : Keyword to sublimate
        conf_keyword (dict) : Configuration for the sublimation

    Return:
        (str) : Code with sublimation of the keyword
    """
    assert isinstance(code, str) , "code must be a string"
    assert isinstance(keyword, str) , "keyword must be a string"
    assert isinstance(conf_keyword, dict), "conf_keyword must be a dictionnary"

    for key in conf_keyword : assert key in PARAMS_CONF, f"{key} is not a parameter of configuration"

    style = ""

    if "color"       in conf_keyword : style += f"color: {conf_keyword['color']};"
    if "font-style"  in conf_keyword : style += f"font-style: {conf_keyword['font-style']};" 
    if "font-size"   in conf_keyword : style += f"font-size: {conf_keyword['font-size']};"
    if "font-weight" in conf_keyword : style += f"font-weight: {conf_keyword['font-weight']};"

    return code.replace(keyword, f"<span style = \"{style}\">{keyword}</span>")


def sublimate(code, conf):
    """
    Sublimate code

    Parameters:
        code (str) : code to be treated
        conf (dict) : Configuration for sublimation

    Return:
        (str) : New code with HTML tags
    """
    assert isinstance(code, str),  "Code must be a string"
    assert isinstance(conf, dict), "conf must be a dictionnary"

    for keyword in conf:
        code = sublimate_keyword(code, keyword, conf[keyword])

    return code


if __name__ == "__main__":
    conf = load_json_conf("conf_files/python.json")

    code = """import numpy as np
if a == True : print("salut")
if a == False : print("merde")
"""

    print(sublimate(code,  conf))

