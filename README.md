# Lorem Exif

## The metadata remover

### What is this?

This is a command line tool to remove the metadata from one or more images and optionally rename them to something some random lorem ipsum text.

### Why Lorem Ipsum to rename files?

To obfuscate natural language. Feel free to change the source.

### Install

``` 
python3 -m pip install -r requirements.txt 
```

This project uses Pillow.

### How to use

First make sure you're in the right folder
```
cd lorem_exif
```
Then, to remove exif data from a ".jpeg", ".jpg", ".png", ".gif", ".bmp" file

```
python3 lorem_exif.py <file_path> 
```

To disable rename and remove metadata from all file/s
```
python3 lorem_exif.py --norename <file_path>
```

To get help
```
python3 lorem_exif.py --help 
```

To print image metadata
```
python3 lorem_exif.py --print <file_path> 
```

### Run tests

This project uses the unittest library. Make sure there is always a 'test.png' and a 'test.txt' (or any extensions) file so tests can start

A python virtual environment (venv) is recommended. 

Go into the tests folder:

``` 
cd tests 
```

and execute  

``` 
python3 -m unittest 
```
