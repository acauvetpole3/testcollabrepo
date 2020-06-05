#!/usr/bin/python3
########################################
# @filename: LEDloop.py
# @author: jai cauvet
#
# @description: reads analog data from an MCP3008 and prints
# 
# copyright 2020
#
########################################

from gpiozero import MCP3008
import time
import sys
import logging

def main(lr):
    logging.info("Staring main loop")
    try:
        lr_int = int(lr)
        photoresistor = MCP3008(lr_int)
        while True:
            print (photoresistor.value)
            time.sleep(.03)
    except KeyboardInterrupt:
        # handle keyboard interrupt #
        logging.info("Exiting LEDLoop.py")
        sys.exit(0)
    except Exception, e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        sys.exit(2)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        lr = sys.argv[1]
    elif len(sys.argv) == 1:
        lr = 0
    else:
        print "{0} syntax: python {0} [photoresistor_id]"
    try:
        sys.exit(main(lr))
    except KeyboardInterrupt:
        # handle keyboard interrupt #
        logging.info("Exiting LEDLoop.py")
        sys.exit(0)
    except Exception, e:
        indent = len(sys.argv[0]) * " "
        sys.stderr.write(sys.argv[0] + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  help")
        sys.exit(2)
