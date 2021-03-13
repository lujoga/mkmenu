# mkmenu

Generate PDF from multiple images on a web page

## Requirements

* Python 3.6+
  * `beautifulsoup4`
* ImageMagick

## Usage

```
$ ./mkmenu.py -h
usage: mkmenu.py [-h] [-o OUTPUT] [--select SELECT] [--strip] page

positional arguments:
  page                  web page to extract images from

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output file (default: "menu.pdf")
  --select SELECT       specify which tags to select (default: "img")
  --strip               strip query and fragment parts from image URLs
```

`--select` supports CSS selector syntax
