import os
import unittest
import tempfile

from copy_directory import copy_directory


class TestCopyStaticToPublic(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.src = os.path.join(self.temp_dir.name, "static")
        self.dst = os.path.join(self.temp_dir.name, "public")
        os.mkdir(self.src)

        # Create nested structure and test files
        os.mkdir(os.path.join(self.src, "subdir"))
        with open(os.path.join(self.src, "file1.txt"), "w") as f:
            f.write("Hello from root")

        with open(os.path.join(self.src, "subdir", "file2.txt"), "w") as f:
            f.write("Hello from subdir")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_successful_copy(self):
        copy_directory(self.src, self.dst)

        self.assertTrue(os.path.exists(os.path.join(self.dst, "file1.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.dst, "subdir", "file2.txt")))

        with open(os.path.join(self.dst, "file1.txt")) as f:
            self.assertEqual(f.read(), "Hello from root")

        with open(os.path.join(self.dst, "subdir", "file2.txt")) as f:
            self.assertEqual(f.read(), "Hello from subdir")

    def test_existing_public_is_deleted(self):
        # Create a fake "public" dir before copying
        os.mkdir(self.dst)
        with open(os.path.join(self.dst, "old.txt"), "w") as f:
            f.write("Old content")

        copy_directory(self.src, self.dst)

        # old.txt should be gone
        self.assertFalse(os.path.exists(os.path.join(self.dst, "old.txt")))

    def test_missing_source_raises_error(self):
        with self.assertRaises(FileNotFoundError):
            copy_directory(
                os.path.join(self.temp_dir.name, "does_not_exist"), self.dst
            )


if __name__ == "__main__":
    unittest.main()
