from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from argparse import ArgumentParser
from pathlib import Path


context = {
    'title': 'Resume',
    'author': 'Andrew Hoyt',
    'date': datetime.now(),
    'margin': '1in',
}





def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-i", "--input",
        type=Path,
        default=Path("resume.md.tpl")
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path('resume.md')
    )

    args = parser.parse_args()

    env = Environment(
        loader=FileSystemLoader(args.input.parent)
    )

    tpl = env.get_template(args.input.name)
    with args.output.open('w') as file:
        file.write(tpl.render(**context))
    


if __name__ == "__main__":
    main()
