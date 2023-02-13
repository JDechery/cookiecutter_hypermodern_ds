import sys
from subprocess import CalledProcessError, run


def system_command_exists(command):
    try:
        run(["which", command], check=True, capture_output=True)
        return True
    except CalledProcessError:
        return False


def main():
    if not system_command_exists("git"):
        print("Cannot find git executable. Aborting.")
        sys.exit(1)

    if not system_command_exists("python3"):
        print("Cannot find python3 executable. Aborting.")
        sys.exit(1)

    if not system_command_exists("poetry"):
        print("Cannot find poetry executable. Aborting.")
        sys.exit(1)


main()
