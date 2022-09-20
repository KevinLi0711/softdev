def not_string(str):
    if not (str[:3] == "not"):
        return "not " + str
    else:
        return str