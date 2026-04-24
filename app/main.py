from os import mkdir, path, remove


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        return

    move_command, file_original, file_moved = command_parts
    if move_command != "mv" or not path.isfile(file_original):
        return
    if file_moved.endswith("/"):
        file_moved = path.join(file_moved, path.basename(file_original))
    if path.isfile(file_moved):
        return

    if (path.dirname(path.abspath(file_original))
            != path.dirname(path.abspath(file_moved))):
        path_parts = path.normpath(path.dirname(file_moved)).split(path.sep)
        # path_parts.remove("")   # for Linux
        path_moved = ""
        for part in path_parts:
            path_moved = path.join(path_moved, part)
            if not path.isdir(path_moved):
                mkdir(path_moved)

    with (
        open(file_original, "r") as fobj_original,
        open(file_moved, "w") as fobj_moved
    ):
        for line in fobj_original.readlines():
            fobj_moved.write(line)
    remove(file_original)
