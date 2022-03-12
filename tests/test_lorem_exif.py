#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_lorem_exif.py
----------------------------------

Tests for `lorem_exif` module.
"""
import unittest

from lorem_exif.lorem_exif import LoremExif


class TestCleanExif(unittest.TestCase):
    def test_path_does_not_exist(self):
        with self.assertRaises(FileNotFoundError, msg="File does not exist"):
            LoremExif(["qqqqqqqqqddddddddvvvvv.png"])

    def test_path_exists(self):
        """If this fails, add a test.png file to the test directory."""
        self.assertTrue(LoremExif(["./test.png"]).path_exists("./test.png"))

    def test_extension_not_supported(self):
        """If this fails, add a test.txt file to the test directory."""
        with self.assertRaises(ValueError, msg="File extension not supported"):
            LoremExif(["test.txt"])

    def test_main_input_type(self):
        self.main = LoremExif(["test.png"])
        self.assertIsInstance(self.main, LoremExif)
        self.assertIsInstance(self.main.img_paths, list)
        self.assertIsInstance(self.main.img_paths[0], str)

    def test_possible_extensions(self):
        self.assertEqual(
            LoremExif(["test.png"]).possible_extensions,
            [".jpeg", ".jpg", ".png", ".gif", ".bmp"],
        )

    def test_image_path_is_none(self):
        with self.assertRaises(TypeError, msg="Argument must be a list of strings"):
            LoremExif()

    def test_len_of_img_paths_is_0(self):
        with self.assertRaises(ValueError, msg="Argument must have at least one file specified"):
            LoremExif([])

    def test_img_paths_element_is_not_str(self):
        with self.assertRaises((AttributeError, TypeError)):
            LoremExif([1])

    def test_image_extension_is_same(self):
        ce = LoremExif(["test.png"])
        ce.clean_files()
        result = LoremExif([ce.next_name])
        ce.revert_rename()
        self.assertEqual(ce.next_name.split(".")[1], result.img_paths[0].split(".")[1])

    def test_result_exif_type(self):
        ce = LoremExif(["test.png"])
        ce.clean_files()
        result = LoremExif([ce.next_name])
        ce.revert_rename()

        self.assertIsNone(result.metadata())

    def test_rename_files_default_is_true(self):
        self.assertEqual(LoremExif(["test.png"]).rename_files, True)

    def test_main_input_name(self):
        self.assertEqual(LoremExif(["test.png"]).img_paths[0], "test.png")

    def test_print_class(self):
        self.assertEqual(LoremExif(["test.png"]).__class__.__name__, "LoremExif")

    def test_size_of_img_paths(self):
        self.assertEqual(LoremExif(["test.png"]).__sizeof__(), 1)

    def test_help_command(self):
        self.assertEqual(
            LoremExif(["test.png"]).help_command(),
            (
                "Usage: lorem_exif.py [options] [file]\n"
                "Options:\n"
                "--print\tPrints all metadata from the image\n"
                "--norename\tDoes not rename the file\n"
                "--help\t\tPrints this help message\n"
            ),
        )

    def test_image_manip(self):
        ce = LoremExif(["test.png"])
        ce.clean_files()
        self.assertIsNone(ce.metadata())
        ce.revert_rename()

"""class TestImageManip(unittest.TestCase):
    def setUp(self) -> None:
        self.main = LoremExif(["test.png"])

    # metadata exists
    def test_clear_metadata_type(self):
        self.assertIsNotNone(self.main.metadata())
        self.assertIsInstance(self.main.metadata(), dict)

    def test_clear_metadata_size(self):
        self.assertGreater(len(self.main.metadata()), 0)

    

    def tearDown(self) -> None:
        self.main.revert_rename()
        del self.main
"""
