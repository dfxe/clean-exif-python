# import test
import unittest
from clean_exif import CleanExif


class TestCleanExif(unittest.TestCase):
    def test_path_does_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            CleanExif(["qqqqqqqqqddddddddvvvvv.png"])

    def test_path_exists(self):
        ce = CleanExif(["test.png"])
        self.assertTrue(ce.__path_exists("test.png"))

    """def test_extension_not_supported(self):
        self.assertRaises(
            ValueError,
            "File extension not supported",
        )

    def test_main_input_type(self):
        self.main = CleanExif(["test.png"])
        self.assertIsInstance(self.main, CleanExif)
        self.assertIsInstance(self.main.img_paths, list)
        self.assertIsInstance(self.main.img_paths[0], str)

    def test_possible_extensions(self):
        self.assertEqual(
            self.main.possible_extensions,
            [".jpeg", ".jpg", ".png", ".gif", ".bmp"],
        )

    # validation tests
    def test_image_path_is_none(self):

        self.assertIsNone(ce.img_paths)
        self.assertRaises(TypeError, "Argument must be a list of strings")

    def test_len_of_img_paths_is_0(self):

        self.assertLessEqual(len(self.main.img_paths), 0)
        self.assertRaises(ValueError, "Argument must have at least one file specified")

    def test_img_paths_element_is_not_str(self):

        self.assertRaises(TypeError, "Argument must be a list of strings")

    def test_rename_file_sole_command(self):

        self.assertRaises(
            ValueError,
            "Argument must have at least one file specified",
        )

    # metadata fn
    def test_result_exif_type(self):
        self.assertIsNone(self.result_img.metadata())

    def test_image_extension_is_same(self):
        self.assertEqual(
            self.main.img_paths[0].split(".")[-1],
            self.result_img.img_paths[0].split(".")[-1],
        )

    # classes
    def test_rename_files_default_is_true(self):
        self.assertEqual(self.main.rename_files, True)

    def test_main_input_name(self):
        self.assertEqual(self.main.img_paths[0], "test.png")

    def test_print_class(self):
        self.assertEqual(self.main.__class__.__name__, "CleanExif")

    def test_size_of_img_paths(self):
        self.assertEqual(self.main.__sizeof__(), 1)

    # commands
    def test_help_command(self):
        self.assertEqual(
            self.main.help_command(),
            (
                "Usage: clean_exif.py [options] [file]\n"
                "Options:\n"
                "--print\tPrints all metadata from the image\n"
                "--norename\tDoes not rename the file\n"
                "--help\t\tPrints this help message\n"
            ),
        )"""


"""class TestImageManip(unittest.TestCase):
    def setUp(self) -> None:
        self.main = CleanExif(["test.png"])

    # metadata exists
    def test_clear_metadata_type(self):
        self.assertIsNotNone(self.main.metadata())
        self.assertIsInstance(self.main.metadata(), dict)

    def test_clear_metadata_size(self):
        self.assertGreater(len(self.main.metadata()), 0)

    def test_image_manip(self):
        self.main.clean_files()
        self.assertIsNone(self.main.metadata())

    def tearDown(self) -> None:
        self.main.backwards_rename()
        del self.main
"""
