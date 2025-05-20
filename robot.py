import os

print("Welcome to Robot Speaker..")

while True:
    # Ask user for input
    text = input("Enter what you want me to say (or 's' to stop): ")
    
    # Stop if user enters 's'
    if text.lower() == 's':
        break

    # Escape single quotes to prevent PowerShell errors
    safe_text = text.replace("'", "''")

    # PowerShell command to use Windows text-to-speech
    command = (
        f'powershell -Command "Add-Type -AssemblyName System.Speech; '
        f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{safe_text}\')"'
    )

    # Run the command
    os.system(command)
