import codecs
import os

class ConfigUtils:
    def __init__(self):
        self.values = {}

        # Parse the default config file
        self._parse_config_file(os.path.join("tools", "parameters.txt"))

    def _parse_config_file(self, filename):
        with codecs.open(filename, encoding="utf-8") as file:
            for line in file.readlines():

                # If the line is blank or is a comment, ignore
                if not line.strip() or line.startswith("#"):
                    continue

                # Split off anything after any # values
                line = line.split("#")[0]

                if "=" not in line:
                    print(f"Error parsing config: line is not parsable:\n{line}")
                    continue

                key, value = line.split("=", 1)
                self.values[key.strip()] = value.strip()

    def get_doku_wiki_username(self):
        return self.values["DOKU_WIKI_USERNAME"]

    def get_doku_wiki_password(self):
        return self.values["DOKU_WIKI_PASSWORD"]
