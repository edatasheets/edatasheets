import subprocess

# Read the content of readmetext.md and write it to support-docs/README.md
with open('readmetext.md', 'r') as infile, open('support-docs/README.md', 'w') as outfile:
    outfile.write(infile.read())

CUR = 5
directories = [
    "common/", "clock/", "data_converter/", "hardware/", "ic_io/", "ic_microcontroller/",
    "ic_misc/", "logic/", "memory/", "passives/", "power/", "semiconductor/", "sensor/",
    "storage/", "undefined/"
]

for A in directories:
    print(f"Processing directory: {A} with version 4.{CUR}")
    result = subprocess.run(['go', 'run', 'readmescript.go', f'part-spec/{A}', f'4.{CUR}'], capture_output=True, text=True)
    if result.stdout:
        with open('support-docs/README.md', 'a') as outfile:
            outfile.write(result.stdout)
    CUR += 1