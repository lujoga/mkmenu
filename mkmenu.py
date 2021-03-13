#!/usr/bin/env python3

from argparse import ArgumentParser
from bs4 import BeautifulSoup
from os.path import join, splitext
from subprocess import run
from tempfile import TemporaryDirectory
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.request import urlopen

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-o', '--output', default='menu.pdf', help='output file (default: "menu.pdf")')
    parser.add_argument('--select', default='img', help='specify which tags to select (default: "img")')
    parser.add_argument('--strip', action='store_true', help='strip query and fragment parts from image URLs')
    parser.add_argument('page', help='web page to extract images from')
    args = parser.parse_args()

    soup = BeautifulSoup(urlopen(args.page).read(), 'html.parser')
    images = soup.select(args.select)
    width = len(str(len(images)))

    with TemporaryDirectory() as tmpdir:
        files = []
        for i, img in enumerate(images):
            src = img.get('src')
            parts = urlsplit(src)
            if args.strip:
                src = urlunsplit((parts.scheme, parts.netloc, parts.path, '', ''))
            print(f'{i:{width}}', src, '=>', end=' ')

            name = join(tmpdir, f'{i:0{width}}{splitext(parts.path)[1]}')
            with open(name, 'wb') as f:
                f.write(urlopen(urljoin(args.page, src)).read())

            files.append(name)
            print(name)
        print()

        argv = ['convert'] + files + [args.output]
        print('$', ' '.join(argv))
        run(argv, check=True)
        print('done')
