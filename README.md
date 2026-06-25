# Lulz-CSRF
Lulz-CSRF is an advanced Cross Site Request Forgery (CSRF/XSRF) Audit and Exploitation Toolkit. Equipped with a Powerful Crawling Engine and Numerous Systematic Checks, it is now able to detect most cases of CSRF vulnerabilities,their related bypasses and futher generate (maliciously) exploitable proof of concepts with each found vulnerability. For more info on how XSRFProbe works, see XSRFProbe Internals on wiki.

install manual;

pip install requests

pip install bs4

pip install request

pip install stringdist

pip install tld

pip install yattag

OR

pip install -r requirements.txt


![srf2](https://github.com/BasHB00M01001/xsrfpr0b3-/assets/112975863/c457d163-c5b1-44c0-9eed-69edc2c0081e)
Performs several types of checks before declaring an endpoint as vulnerable.
Can detect several types of Anti-CSRF tokens in POST requests.
Features a powerful crawler which features continuous crawling and scanning.
Out of the box support for custom cookie values and generic headers.
Accurate Token-Strength Detection and Analysis using various algorithms.
Can generate both normal as well as maliciously exploitable CSRF PoCs.
Follows a redirect when there is a 30x response.
Well documented code and highly generalised automated workflow.
The user is in control of everything whatever the scanner does.
Has a user-friendly interaction environment with full verbose support.
Detailed logging system of errors, vulnerabilities, tokens and other stuffs.
 ![srf](https://github.com/BasHB00M01001/xsrfpr0b3-/assets/112975863/8d64c042-719f-46c3-8d09-c12d840150a3)


Do not use this tool on a live site!

It is because this tool is designed to perform all kinds of form submissions automatically which can sabotage the site. Sometimes you may screw up the database and most probably perform a DoS on the site as well.

Test on a disposable/dummy setup/site!
Disclaimer:

Usage of xsrfkroke for testing websites without prior mutual consistency can be considered as an illegal activity. It is the final user's responsibility to obey all applicable local, state and federal laws. The author assumes no liability and is not exclusively responsible for any misuse or damage caused by this program.
Author's Words:
This project is based entirely upon my own research and my own experience with web applications on Cross-Site Request Forgery attacks. You can try going through the source code which is highly documented to help you understand how this toolkit was built. Useful pull requests, ideas and issues are highly welcome. If you wish to see what how XSRFProbe is being developed, check out the Development Board.
