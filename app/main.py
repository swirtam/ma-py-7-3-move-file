from os import makedirs, path, rename


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        return

    move_command, file_original, file_moved = command_parts
    if move_command != "mv" or not path.isfile(file_original):
        return
    if not path.splitext(path.basename(file_moved))[1]:
        file_moved = path.join(file_moved, path.basename(file_original))
    if path.isfile(file_moved):
        return

    file_original = path.abspath(file_original)
    file_moved = path.abspath(file_moved)
    if path.dirname(file_moved) != path.dirname(file_original):
        makedirs(path.dirname(file_moved), exist_ok=True)
    rename(file_original, file_moved)
