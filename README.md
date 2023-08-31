# basteln (tinkern)

## tkskript.py

### Remove the password for ALL files in given path (still needs a password)

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

## Threading example

When this script ends, all containing threads are terminated, regardless of whether the tasks have been processed.
Either one implements a runner-variable that is set one down with each completed task. At the end there is then something like
```python3
while(variable > 0):
    s.th()
```
>There are certainly more elegant solutions to this problem, but I can't think of them right now.

To disable threading, the following lines should be left out or uncommented commented out code lines 

Comment out (write a # at the beginning of the line):
- Line 27
- Line 30
- Line 50
- Line 53

Comment (remove # at the beginning of the line):
- Line 28
- Line 37
- Line 38
- Line 51
- Line 59
- Line 60

---
## servo.py

Eine kleines Programm um mit Servomotoren am Raspberry umzugehen.

Verwendet wurde die Bibliothek
[__gpiozero__](https://gpiozero.readthedocs.io/en/stable/)

Ich hab mich auch ein bisschen mit einem Argument Handler auseinander gesetzt.


Viel Glück =)

---
## eyes.py

Eine mini python Spielerei.
Es soll ein einfaches ASCII Gesicht anzeigen, das sich umschaut.

Aktuell ist das ding noch zu hibbelig.

### Eingaben zur Laufzeit:
(Enter nicht vergessen *nur der letzte eingegebene Buchstabe wird gewertet*)
- ? = mini Hilfe anzeigen
- q oder Q oder 0 oder e oder E Beendet das Programm

Leider noch ein klein bissche buggy und etwas hacky

#### mögliche verbesserungen:
- statt überall print, einen Puffer einsetzen. So könnte man auch mehrzeilig Arbeiten
- mehr Eingaben zur Laufzeit
- mehr Gesichter
- mehr Zeichen möglich, UTF-8 bzw Ascii ist recht begrenzt (keine Ahnung ob Python3 das kann)


