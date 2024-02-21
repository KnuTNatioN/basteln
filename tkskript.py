#!/usr/bin/env python3

import os
import sys
import subprocess

def unlock_pdfs(folder_path, password):
    # Überprüfen, ob der Ordner existiert
    if not os.path.exists(folder_path):
        print(f"Der Ordner '{folder_path}' existiert nicht.")
        return

    # Durchsuchen Sie den Ordner nach PDF-Dateien
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".pdf"):
                pdf_file = os.path.join(root, filename)
                output_dir = os.path.join(root, "without")
                os.makedirs(output_dir, exist_ok=True)
                output_file = os.path.join(output_dir, filename)

                # Verwenden Sie pdftk, um das Passwort zu entfernen
                try:
                    subprocess.run(["pdftk", pdf_file, "input_pw", password, "output", output_file])
                    print(f"Passwort für '{pdf_file}' entfernt und als '{output_file}' gespeichert.")
                except Exception as e:
                    print(f"Fehler beim Entfernen des Passworts für '{pdf_file}': {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Verwendung: python3 unlock_pdfs.py <Ordnerpfad> <Passwort>")
    else:
        folder_path = sys.argv[1]
        password = sys.argv[2]
        unlock_pdfs(folder_path, password)
