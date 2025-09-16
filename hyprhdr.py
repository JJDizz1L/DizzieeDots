import re
from pathlib import Path

def toggle_monitor_settings(filepath):
    """
    Toggles the 'cm' and 'bitdepth' settings in the monitors.conf file.

    If 'cm = auto' and 'bitdepth = 8', it changes them to 'cm = hdr' and 'bitdepth = 10'.
    Otherwise, it changes 'cm = hdr' and 'bitdepth = 10' to 'cm = auto' and 'bitdepth = 8'.

    Args:
        filepath (str): The path to the monitors.conf file.
    """
    try:
        # Check if the path is absolute, if not, assume it's in the user's home directory
        monitors_conf_path = Path(filepath)
        if not monitors_conf_path.is_absolute():
            monitors_conf_path = Path.home() / ".config/hypr/monitors.conf"

        with open(monitors_conf_path, 'r') as f:
            content = f.read()

        # Check for the current state
        is_auto_8bit = re.search(r'cm\s*=\s*auto', content) and re.search(r'bitdepth\s*=\s*8', content)

        if is_auto_8bit:
            # Change to HDR settings
            new_content = re.sub(r'cm\s*=\s*auto', 'cm = hdr', content)
            new_content = re.sub(r'bitdepth\s*=\s*8', 'bitdepth = 10', new_content)
            print("Changed settings to HDR (cm = hdr, bitdepth = 10).")
        else:
            # Change to SDR settings (assuming it's currently HDR)
            new_content = re.sub(r'cm\s*=\s*hdr', 'cm = auto', content)
            new_content = re.sub(r'bitdepth\s*=\s*10', 'bitdepth = 8', new_content)
            print("Changed settings to SDR (cm = auto, bitdepth = 8).")

        # Write the updated content back to the file
        with open(monitors_conf_path, 'w') as f:
            f.write(new_content)

        print(f"File '{monitors_conf_path}' updated successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{monitors_conf_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# The path to your monitors.conf file
# Use the full path for better reliability
config_file_path = Path.home() / ".config/hypr/monitors.conf"

# Run the script
toggle_monitor_settings(config_file_path)
