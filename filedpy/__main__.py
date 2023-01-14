"""File Downloader entry point script."""
# filedpy/__main__.py

from filedpy import cli, __app_name__

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()