import os


def read_original_data(basepath):
    """Return list of design smells .ini files for further processing

    Input: path to design smells directory
    """
    files = []
    for file in os.listdir(basepath):
        path = os.path.join(basepath, file)
        if os.path.isdir(path):
            # skip hidden directories
            continue
        else:
            if path.endswith('.ini'):
                files.append(path)
    print("design smells .ini files", files)
    return files
