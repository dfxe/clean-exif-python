#!/usr/bin/env python3
import os
import sys

import PIL.Image
import PIL.ExifTags
import random
from enum import Enum


class Commands(Enum):
    PRINT = "--print"
    HELP = "--help"
    NORENAME = "--norename"


class LoremExif:
    next_name: str

    def __init__(self, img_paths: list):
        """Constructor, checks if the image exists and if it has the valid extension and sets the image paths accordingly.
        Skips all commands"""

        self.possible_extensions = [".jpeg", ".jpg", ".png", ".gif", ".bmp"]
        self.rename_files = True
        self.img_paths = img_paths

        self.next_name = ""
        temp = []

        if img_paths is None:
            raise TypeError("Argument must be a list of strings")
        if len(img_paths) == 0:
            raise ValueError("Argument must have at least one file specified")
        if not isinstance(img_paths[0], str):
            raise TypeError("Argument must be a list of strings")
        if len(img_paths) == 1 and (img_paths[0]) == Commands.NORENAME.value:
            raise ValueError("Argument must have at least one file specified")

        for item in img_paths:
            if item in [
                Commands.HELP.value,
                Commands.PRINT.value,
                Commands.NORENAME.value,
            ]:
                continue
            if self.path_exists(item):
                ext_check = False
                for ext in self.possible_extensions:
                    if item.endswith(ext):
                        ext_check = True
                        temp.append(item)
                        break
                if not ext_check:
                    raise ValueError("File extension not supported")

            else:
                raise FileNotFoundError(f"File does not exist")

        if len(temp) > 0:
            self.img_paths = temp

    def metadata(self, img_path=None):
        """Returns all metadata from an image, or the metadata of the first image if no arguments are specified."""
        if img_path is None:
            img_path = self.img_paths[0]
        if not self.path_exists(img_path):
            return None
        exif_data = PIL.Image.open(img_path)._getexif()
        if exif_data:
            return {
                PIL.ExifTags.TAGS[k]: v
                for k, v in exif_data.items()
                if k in PIL.ExifTags.TAGS
            }
        return None

    def print_all_metadata(self):
        for img_path in self.img_paths:
            print(self.metadata(img_path))

    def clean_files(self):
        for image_path in self.img_paths:
            self.__clear_metadata(image_path)

    @staticmethod
    def help_command():
        # Returns a help message
        return (
            "Usage: lorem_exif.py [options] [file]\n"
            "Options:\n"
            "--print\tPrints all metadata from the image\n"
            "--norename\tDoes not rename the file\n"
            "--help\t\tPrints this help message\n"
        )

    def revert_rename(self):
        """Renames the file with the new name."""
        os.rename(self.next_name, "test.png")

    @staticmethod
    def path_exists(path: str) -> bool:
        return os.path.exists(path)

    def __clear_metadata(self, path_of_image_to_clean):
        """Make a copy of the image without the metadata from the original."""
        image = PIL.Image.open(path_of_image_to_clean)
        data = list(image.getdata())
        image_without_exif = PIL.Image.new(image.mode, image.size)
        image_without_exif.putdata(data)

        self.next_name = (
            self.__get_new_file_name() + "." + path_of_image_to_clean.split(".")[-1]
        )
        try:
            image_without_exif.save(
                os.path.dirname(path_of_image_to_clean) + "/" + self.next_name
                if len(os.path.dirname(path_of_image_to_clean)) > 0
                else self.next_name
                if self.rename_files
                else path_of_image_to_clean
            )
            os.remove(path_of_image_to_clean)
        except PermissionError:
            print("Permission denied")

    def __get_new_file_name(self):
        """Returns a random name with Lorem ipsum content."""
        next_name = ""
        with open("file_name_source.txt") as names_file:
            lines = (
                names_file.read()
                .replace("\n", "")
                .replace(".", "")
                .replace(",", "")
                .lower()
                .split(" ")
            )
            lines = [x for x in lines if len(x) > 3]
            next_name += "-".join(random.sample(lines, 3))
        return next_name

    def __sizeof__(self) -> int:
        return len(self.img_paths)


if __name__ == "__main__":
    ce = LoremExif(sys.argv[1:])
    if Commands.HELP.value in ce.img_paths:
        print(ce.help_command())
    elif Commands.PRINT.value in ce.img_paths:
        ce.print_all_metadata()
    elif Commands.NORENAME.value in ce.img_paths:
        ce.rename_files = False
        ce.clean_files()
    else:
        ce.clean_files()
