def write_to_file(filename,data):
    with open(filename,"w",encoding="utf-8") as f:
        f.write(data)

    return True

def read_from_file(filename):
    try:
        with open(filename,"r") as f:
            return f.read()
    except FileNotFoundError:
        print(filename,"does not exist")
        return ""