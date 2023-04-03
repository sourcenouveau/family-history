# py -m venv venv
# pip install pyyaml
# .\venv\Scripts\Activate.ps1

from pathlib import Path

import yaml


def read_data(data_path):
    with open(data_path, "r") as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(e)


def main():
    places_data_dir = Path("_data/places")
    data_paths = places_data_dir.glob("**/*.yml")

    for data_path in sorted(data_paths):
        item_path = Path("items", "_places", *data_path.parts[2:-1], data_path.stem + ".md")

        if item_path.is_file():
            continue

        data_file = read_data(data_path)

        enclosure_path = places_data_dir / Path(data_file["enclosing_place_key"] + ".yml")
        enclosure_data = read_data(enclosure_path)

        with open(item_path, "w") as item_file:
            title = data_file["name"]

            # TODO: Build titles
            # - Town: Name, State Abbrev
            # - County: Name, State Abbrev
            # - State: Name
            # - Country: Name
            #
            #if data_file["division"] in ("county", "town"):
            #    title += f", {}"

            item_data = {
                "title": title,
                "key": data_path.stem
            }
            item_file.write(yaml.dump(item_data, explicit_start=True))
            item_file.write("---\n")


if __name__ == "__main__":
    main()
