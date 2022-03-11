# Lorem Exif

## The metadata remover

### What is this?

This is a command line tool to remove metadata from image + rename image.

### Why Lorem Ipsum to rename files?

To obfuscate natural language. Feel free to change the source.

### Install

``` python3 -m pip install -r requirements.txt ```

This project uses Pillow.

### How to use

To remove exif data from a ".jpeg", ".jpg", ".png", ".gif", ".bmp" file\
``` python3 clean_exif.py <file_path> ```

To disable rename and remove metadata from all file/s\
``` python3 clean_exif.py --norename <file_path> ```

To get help\
``` python3 clean_exif.py --help ```

To print image metadata\
``` python3 clean_exif.py --print <file_path> ```

### Run tests

This project uses the unittest library. Make sure there is always a 'test.png' and a 'test.txt' (or any extensions) file so tests can start\
Go into the tests folder:\
``` cd tests ```

and execute  

``` python3 -m unittest ```
