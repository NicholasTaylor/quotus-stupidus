#!/usr/bin/python3.8

import sys, os

def arg_check(arg):
    if len(arg) < 3:
        print('Please include proper file path arguments.\nExample syntax: ./quotus-stupidus.py [input path] [output path]')
        return False
    elif not os.path.exists(arg[1]):
        print('Input file doesn\'t exist or path invalid. Please try again.')
        return False
    else:
        return True

def stupify(arg):
    if  not arg_check(arg):
        return
    else:
        input_path = arg[1]
        output_path = arg[2]
        input = ''
        with open(input_path,'r') as input_file:
            input += input_file.read()
        output = input.replace('“','"').replace('”','"').replace('‘','\'').replace('’','\'').replace('—','-').replace('–','-')
        with open(output_path,'w+') as output_file:
            output_file.write(output)
        print('Output file generated successfully')
        return

stupify(sys.argv)
