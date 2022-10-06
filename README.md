# basteln (tinkern)

### tkskript.py

#### Remove the password for ALL files in given path (still needs a password)

- need "pdftk" installed (just tested with Ubuntu 22.04 -> "sudo apt install pdftk")
- non recursive (ignores directory's in path)
- creates a Folder in given path (without/)
- threading for a but parallel workload to be a bit faster ^^
- uses threading, time, subprocess, os and sys (i know... a lot of stuff, improve it =P)
- pipes all warnings to >/dev/null 2>&1


> copy of pdftk --help:
```
SECURITY CONSIDERATIONS
       Passing a password as a command line parameter is insecure because it
       can get saved into the shell's history and be accessible by other users
       via /proc. Use the keyword PROMPT and input any passwords via standard
       input instead.
```

---
### servo.py

Eine kleines Programm um mit Servomotoren am Raspberry umzugehen.

Verwendet wurde die Bibliothek
[__gpiozero__](https://gpiozero.readthedocs.io/en/stable/)

Ich hab mich auch ein bisschen mit einem Argument Handler auseinander gesetzt.


Viel Glück =)
