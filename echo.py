#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""


__author__ = "Shaquon" 


import sys
import argparse


def create_parser():
    """Creates parser"""
    parser = argparse.ArgumentParser(description="Perform transformation on input text.")
    parser.add_argument("-u", "--upper", help="convert text to uppercase", action="store_true")
    parser.add_argument("-l", "--lower", help="convert text to lowercase", action="store_true")
    parser.add_argument("-t", "--title", help="convert text to titlecase", action="store_true")
    parser.add_argument("text", help="text to be manipulated")
    return parser


def main(args):
    """Echo flags"""
    parser = create_parser()
    if not args:
        parser.print_usage()
        sys.exit()
        
    args = parser.parse_args(args)
    text = args.text

    if args.upper:
        text = text.upper()
    elif args.lower:
        text = text.lower()
    elif args.title:
        text = text.title()

    return text


if __name__ == '__main__':
    print(main(sys.argv[1:]))