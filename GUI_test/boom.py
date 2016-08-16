'''
An example script to demonstrate Gooey's recovery from Client errors.

(It fails because it's supposed to)

'''

import time
from gooey import Gooey
from gooey import GooeyParser

# ascii art credit:
# http://www.chris.com/ascii/index.php?art=objects/explosives
NO_BOOM = r"""
          ,--.!,
       __/   -*-
     ,d08b.  '|`
     0088MM
     `9MMP'
  hjm
"""

BOOM = r"""
     _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____
       KAA-BOOOOOOM
"""



@Gooey(monospace_display=True)
def main():
    parser = GooeyParser(description='This Demo will raise an error!')


    parser.add_argument("name", type=str, default='Enter Name')
    parser.add_argument("age", type=int)
    parser.add_argument("gender", choices=["Female","Male"], default="Female")
    parser.add_argument("animal", choices=["Dogs","Cats"], default="Dogs")
    parser.add_argument("feet", type=int, default=5)
    parser.add_argument("inches", type=int, default=3)
 
    args = parser.parse_args()
    print args.name

if __name__ == '__main__':
  main()
