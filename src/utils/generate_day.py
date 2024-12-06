import click
import os

def generate_day(day: int, force: bool = False):

    generate_input_file(day, force)
    generate_src_file(day, force)

def generate_input_file(day: int, force: bool):
    data_path = "data"
    input_file_path = f"{data_path}/{day}.in"
    if os.path.isfile(input_file_path) and not force:
        return
    open(input_file_path, "w")

def generate_src_file(day: int, force: bool):
    src_file_path = f"src/{day}.py"

    # If you want to add some template field, do it so here.
    TEMPLATE_CONFIG = {
        "day": day
    }

    if os.path.isfile(src_file_path) and not force:
        return

    with open("src/utils/day_template", "r") as template:
        with open(src_file_path, "w") as src_file:
            for l in template.readlines():
                if not "{{" in l or not "}}" in l:
                    src_file.write(l)
                    continue
                for k,v in TEMPLATE_CONFIG.items():
                    l = l.replace("{{" + k + "}}", str(v))
                src_file.write(l)

@click.command()
@click.option('-d', '--day', default=1, help='Number of the day.')
@click.option('--force', is_flag=True)
def generate(day,force):
    if day > 25 or day <= 0:
        click.echo(f"Invalid day. Accepted range is [1,25]")
    generate_day(day=day, force=force)


if __name__ == "__main__":
    generate()
