import subprocess
from enum import Enum


def parse_flag(value):
    if value == "true":
        return "set"
    return "unset"


class CELArgumentParser:

    def __init__(self, exe_location):
        self.exe_location = exe_location
        self.data = {"--transparent": "0xFFFFFF00"}

    def parse_cel(self, cel):
        info_command = f"{self.exe_location} info {cel}"
        info_result = subprocess.run(info_command, stdout=subprocess.PIPE)

        section = ""
        for line in info_result.stdout.splitlines():
            line = line.decode("utf-8")

            # Parse into a key and value
            key, value = [x.replace("-", "").split("(")[0].strip() for x in line.split(":", 1)]

            # Values can be nested under others, so remember the top-level section
            if line.startswith(" -"):
                section = line.split("-")[1].split(":")[0].strip()

            if key == "skip":
                self.data["--ccb-skip"] = parse_flag(value)
            elif key == "last":
                self.data["--ccb-last"] = parse_flag(value)
            elif key == "npabs":
                self.data["--ccb-npabs"] = parse_flag(value)
            elif key == "spabs":
                self.data["--ccb-spabs"] = parse_flag(value)
            elif key == "ppabs":
                self.data["--ccb-ppabs"] = parse_flag(value)
            elif key == "ccbpre":
                self.data["--ccb-ccbpre"] = parse_flag(value)
            elif key == "yoxy":
                self.data["--ccb-yoxy"] = parse_flag(value)
            elif key == "acsc":
                self.data["--ccb-acsc"] = parse_flag(value)
            elif key == "alsc":
                self.data["--ccb-alsc"] = parse_flag(value)
            elif key == "acw":
                self.data["--ccb-acw"] = parse_flag(value)
            elif key == "accw":
                self.data["--ccb-accw"] = parse_flag(value)
            elif key == "twd":
                self.data["--ccb-twd"] = parse_flag(value)
            elif key == "lce":
                self.data["--ccb-lce"] = parse_flag(value)
            elif key == "ace":
                self.data["--ccb-ace"] = parse_flag(value)
            elif key == "maria":
                self.data["--ccb-maria"] = parse_flag(value)
            elif key == "pxor":
                self.data["--ccb-pxor"] = parse_flag(value)
            elif key == "useav":
                self.data["--ccb-useav"] = parse_flag(value)
            elif key == "packed":
                self.data["--packed"] = value
            elif key == "plutpos":
                self.data["--ccb-plutpos"] = parse_flag(value)
            elif key == "bgnd":
                if section == "flags":
                    self.data["--ccb-bgnd"] = parse_flag(value)
                elif section == "pre0":
                    self.data["--pre0-bgnd"] = parse_flag(value)
            elif key == "noblk":
                self.data["--ccb-noblk"] = parse_flag(value)
            elif key == "literal":
                self.data["--pre0-literal"] = parse_flag(value)
            elif key == "uncoded":
                self.data["--coded"] = str(not value == "true")
            elif key == "rep8":
                self.data["--pre0-rep8"] = parse_flag(value)
            elif key == "lrform":
                self.data["--lrform"] = value
            elif key == "bpp":
                self.data["--bpp"] = line.split("(")[1].split("b")[0]

        result_command = []
        for key, value in self.data.items():
            result_command += [key, value]

        return result_command
