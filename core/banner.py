#!/usr/bin/env python3
#coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#   Lulz-CSRF     #
#-:-:-:-:-:-:-::-:-:#

#Author: kroketon lulzbin
#This module requires Lulz-CSRF
#https://github.com/lulzbinbashspider/Lulz-CSRF

# Just for some fancy benner to appear at beginning

import time
from Lulz-CSRF import __version__
import Lulz-CSRF.core.colors

colors = Lulz-CSRF.core.colors.color()

SLEEP_TIME = 0


def banner():
    """Display the program banner"""
    print("\n\n")
    time.sleep(SLEEP_TIME)
    print(
        colors.ORANGE
        + "     _____       _____       _____      _____       _____                                    "
    )
    time.sleep(SLEEP_TIME)
    print(
        colors.RED
        + "  __"
        + colors.ORANGE
        + "|"
        + colors.RED
        + "__ "
        + colors.ORANGE
        + "  |_  "
        + colors.RED
        + "__"
        + colors.ORANGE
        + "|"
        + colors.RED
        + "___ "
        + colors.ORANGE
        + " |_  "
        + colors.RED
        + "__"
        + colors.ORANGE
        + "|"
        + colors.RED
        + "___  "
        + colors.ORANGE
        + "|_  "
        + colors.RED
        + "_"
        + colors.ORANGE
        + "|"
        + colors.RED
        + "____ "
        + colors.ORANGE
        + "|_"
        + colors.RED
        + "   _"
        + colors.ORANGE
        + "|"
        + colors.RED
        + "____ "
        + colors.ORANGE
        + "|_ "
        + colors.RED
        + " _____   _____  ______  ______  "
    )
    time.sleep(SLEEP_TIME)
    print(
        colors.RED
        + " \  `  /    "
        + colors.ORANGE
        + "|"
        + colors.RED
        + "|   ___|   "
        + colors.ORANGE
        + "|"
        + colors.RED
        + "|  _  _|   "
        + colors.ORANGE
        + "|"
        + colors.RED
        + "|   ___|  "
        + colors.ORANGE
        + "| "
        + colors.RED
        + "|   _  |  "
        + colors.ORANGE
        + "|"
        + colors.RED
        + "|  _ ,' /     \|  _   )|   ___| "
    )
    time.sleep(SLEEP_TIME)
    print(
        colors.RED
        + "  >   <     "
        + colors.ORANGE
        + "|"
        + colors.RED
        + " `-.`-.    "
        + colors.ORANGE
        + "|"
        + colors.RED
        + "|     \    "
        + colors.ORANGE
        + "|"
        + colors.RED
        + "|   ___|  "
        + colors.ORANGE
        + "|"
        + colors.RED
        + " |    __|  "
        + colors.ORANGE
        + "|"
        + colors.RED
        + "|     \ |  -  || |_  { |   ___| "
    )
    time.sleep(SLEEP_TIME)
    print(
        colors.RED
        + " /__/__\   "
        + colors.ORANGE
        + "_|"
        + colors.RED
        + "|______|  "
        + colors.ORANGE
        + "_|"
        + colors.RED
        + "|__|\__\ "
        + colors.ORANGE
        + " _|"
        + colors.RED
        + "|___|   "
        + colors.ORANGE
        + " _|"
        + colors.RED
        + " |___|   "
        + colors.ORANGE
        + " _|"
        + colors.RED
        + "|__|\__\\\_____/|______)|______| "
    )
    time.sleep(SLEEP_TIME)
    print(
        colors.ORANGE
        + "    |_____|     |_____|     |_____|    |_____|     |_____| \n\n"
    )
    time.sleep(SLEEP_TIME)


def banabout():  # some fancy banner stuff :p
    print(
        colors.BLUE
        + "   [---]            "
        + colors.GREY
        + "Lulz-CSRF,"
        + colors.RED
        + " A"
        + colors.ORANGE
        + " Cross Site Request Forgery "
        + colors.RED
        + "Audit Toolkit          "
        + colors.BLUE
        + "[---]"
    )
    time.sleep(SLEEP_TIME)
    print(
        colors.BLUE
        + "   [---]                                                                           [---]"
    )
    time.sleep(SLEEP_TIME)
    print(
        colors.BLUE
        + "   [---]   "
        + colors.PURPLE
        + "                    "
        + colors.GREEN
        + "~  Author : "
        + colors.CYAN
        + "Lulzbinbash  ~                   "
        + colors.BLUE
        + "     [---]"
    )
    time.sleep(SLEEP_TIME)
    print(
        colors.BLUE
        + "   [---]   "
        + colors.CYAN
        + "                   ~  github.com / "
        + colors.GREY
        + "lulzbinbashider/"
    time.sleep(SLEEP_TIME)
    print(
        colors.BLUE
        + "   [---]                                                                           [---]"
    )
    time.sleep(SLEEP_TIME)
    print(
        colors.BLUE
        + "   [---]  "
        + colors.ORANGE
        + "                         ~  Version "
        + colors.RED
        + __version__
        + colors.ORANGE
        + "  ~                           "
        + colors.BLUE
        + "  [---]\n"
    )
    time.sleep(SLEEP_TIME)

               ``;`                              
             `,+@@@+                              
           .+@@@@@@@;                            
        `;@@@@@@@@@@@                            
       +@@@@@@@@@@@@@:                            
     ;@@@@@@@@@@@@@@@@                            
   `@@@@@@@@@@@@@@@@@@`                          
   `@@@@@@@@@@@@@@@@@@#                          
    .@@@@@@@@@@@@@@@@@@,                          
     :@@@@@@@@@@@@@@@@@@      .'@@                
      #@@@@@@@@@@@@@@@@+;  .+@@@@@                
      `@@@@@@@@@@@@@#;;+@+#@@@#:`                
       #@@@@@@@@@@';'@@@@@@@:`                    
       `@@@@@@@+;;+@@@@@##`                      
        .@@@#;;+@@@@@#+',.,'.                    
         +;;'#@@@@#+;`      ,:                    
         .#@@@@#++:  @.    ...`                  
      `'@@@@#++'. +  .#++;;+  +                  
    ,@@@@@#++:``::+   `',:+,. ,                  
  `@@@@#, #+` ',.`'.   +` ``  `,  .+              
   @@:`  ,+. ,`:``.:   '. .',+++   #              
   ``    #+`++,.`:,``    :`+@@'@@@@'    ````      
         #'`#+:`.,`:` .@@@+@#  +`.      :  `:    
         #:: +.`,.., `@@,#@':. +        :   '    
         #: ` ',:`,, @#``    + +        ' `,;    
         #: ` `:''`  @` #:.. , '        #+++:    
         #: ,     ;#'#  + :   `:         #++      
         #; '     `''         ,          '.      
         ;' '                 #         `@#      
          #.;                ;`       ,#.:;      
          `+;               '.        @   `      
           :#;            `@:        :`  `,      
            .#+;        `'+.'        +            
              .@++#'+@+@++` ;@.     '            
               `' ., ` #:`# `+.#+  :.            
                ., :  @#;.`;`:  `#@.              
                 +``,.;`@+,. '#                  
                 @' ' ;`@:+`#`;`                  
                `#+  ,'`#  :.  '                  
                ' #.  :`#` '`. +                  
                # +.  .:+: :`. .                  
               `, +,   ..+ '`   :                
               ;` #+@:,:#.;``   '                
               #'##:#+.  : `;   ;                
               #. #:      `'`   :                
                  #,        `   .     
 ____ _          ___   ____ _    _____  _____ ___           _   _ 
/ ___ | | ___ __ / _ \ / ___| | _|___ / |_   _/ _ \__      _| \ | |
| |   | |/ / '__| | | | |   | |/ / |_ \   | || | | \ \ /\ / /  \| |
| |___|   <| |  | |_| | |___|   < ___) |  | || |_| |\ V  V /| |\  |
\____ |_|\_\_|   \___/ \____|_|\_\____/___|_| \___/  \_/\_/ |_| \_|  
                                     |_____|                       


🅵🆄🅲🅺 🆃🅷🅴 🆂🆈🆂🆃🅴🅼

HⒶcKt1v1st ⒶnⒶrchyst Ⓐn0nym0uS
ᴡ3 Ⓐʀ3 Ⓐɴ0ɴʏᴍ0ᴜS ᴡ3 Ⓐʀ3 ʟ3ɢ10ɴ, ᴡ3 ᴅ0ɴ’ᴛ ꜰ0ʀɢ1ᴠ3 ᴡ3 ᴅ0ɴ’ᴛ ꜰ0ʀɢ3ᴛ ,3xp3ct uS
