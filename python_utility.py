import argparse
import sys

def calc(args):
    if args.c == "add":
        return args.x+args.y

    elif args.c == "mul":
        return args.x*args.y

    elif args.c == "div":
        return args.x/args.y

    elif args.c == "rem":
        return args.x%args.y

if __name__== '__main__':
    parser= argparse.ArgumentParser()
    parser.add_argument('--x', type= float,default=1.0,help='Enter the first number. This is a utlity for calculation')

    parser.add_argument('--y', type= float,default=3.0,help='Enter a Second number.This is a utlity for calculation')

    parser.add_argument('--c', type= str,default="add",help='Enter the operation/Calculations to be performed.This is a utlity for calculation')

    args= parser.parse_args()
    sys.stdout.write(str(calc(args)))
