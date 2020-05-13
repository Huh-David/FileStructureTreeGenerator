import os


def create_tree(uri: str, ident=0, max_steps=-1, last_dir=False, inverse_ident=0) -> str:
    string = ""
    if ident == 0:
        string += uri.rpartition("/")[-1]
        string += "\n"
    content = os.listdir(uri)  # save all files in var
    for file in content:
        inverse_ident_temp = inverse_ident
        is_directory = os.path.isdir(uri + "/" + file)  # check if more folders are in there
        if content.index(file) != len(content) - 1:
            for x in range(ident):
                if last_dir and inverse_ident_temp > 0:
                    string += "   "
                    inverse_ident_temp -= 1
                else:
                    string += "│  "
            string += "├──"
        else:
            for x in range(ident):
                if last_dir and inverse_ident_temp > 0:
                    string += "   "
                    inverse_ident_temp -= 1
                else:
                    string += "│  "
            string += "└──"
        string += file
        string += "\n"
        if is_directory:
            if max_steps == 0:
                continue
            elif ident == 0 and not last_dir and content.index(file) == len(content) - 1:
                string += create_tree(uri + "/" + file, ident + 1, max_steps - 1, True, inverse_ident + 1)
            elif last_dir and content.index(file) == len(content) - 1:
                string += create_tree(uri + "/" + file, ident + 1, max_steps - 1, True, inverse_ident + 1)
            elif last_dir:
                string += create_tree(uri + "/" + file, ident + 1, max_steps - 1, True, inverse_ident)
            else:
                string += create_tree(uri + "/" + file, ident + 1, max_steps - 1)

    return string


path = "your_path"  # path of folder to structure
tree = create_tree(path, 0, -1)
print(tree)