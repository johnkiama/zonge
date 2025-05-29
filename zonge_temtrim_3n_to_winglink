import os

# Configuration
directory = '/home/seismics/Music/kgn_tem1'  # Change this to your target directory
text_to_replace = 'skp     Tx   Station  Freq Cmp Amps Win Time   Magnitude  RampAppRes    Depth    %Mag'        # Text you want to replace
replacement_text = 'skp Tx-Coord Station  Freq Cmp Amps Win Time   Magnitude  RampAppRes    Depth     %Mag'       # New text

# Iterate through all text files in the directory
for filename in os.listdir(directory):
    if filename.endswith('o.avg'):
        file_path = os.path.join(directory, filename)

        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace the text
        updated_content = content.replace(text_to_replace, replacement_text)

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f'Updated: {filename}')
