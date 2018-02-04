"""Copyright (c) 2014-2018, Nathaniel Yodock
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."""

import sys

offset = 0
output = ""
buf = "  "
length = len(sys.argv)
infile = ""
outfile = ""

if (length == 1):
    print("Type 'python HexaDump /?' for help.")
    sys.exit(1)

if (length > 2):
    print("HexaDump only takes one arg.")
    print("Type 'python HexaDump /?' for help.")
    sys.exit(2)

if (sys.argv[1] == "/?"):
    print("")
    print("usage: python HexaDump [file] [/?] [/l]")
    print("")
    print("file - The file that will be read by HexaDump")
    print("/? - Displays the help prompt and exits.")
    print("/l - Displays the license prompt and exits.\n")
    sys.exit(0)

elif (sys.argv[1] == "/l"):
    print(__doc__)
    sys.exit(0)

else:
    try:
        file = open(sys.argv[1], 'rb')
        data = file.read()
        file.close()

        for c in data:
            if (offset % 16 == 0):
                output += "{:08x}    ".format(offset)

            output += "{:02x} ".format(c)

            if ((c > 32) and (c < 127)):
                buf += chr(c)
            else:
                buf += "."

            offset += 1

            if (offset % 16 == 0):
                buf += "\n"
                output += buf
                buf = "  "

        if (offset % 16 != 0):
            offset = 16 - (offset % 16)

            for i in range(offset):
                output += "   "

        output += buf
        print(output)
        sys.exit(0)

    except FileNotFoundError as e:
        print("Error: This file doesn't exist!")
        sys.exit(3)
