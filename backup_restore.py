import subprocess
import datetime
import os

# MySQL connection details
host = 'localhost'
user = 'bowie'
password = '030709'
database = 'mansys'

def get_backup_file_path():
    # Get the path to the Desktop directory for the current user
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    return os.path.join(desktop_path, f"{database}_backup.sql")

def backup_database():
    try:
        # Get backup file path
        backup_file = get_backup_file_path()

        # Construct mysqldump command with full path
        dump_command = f"/usr/bin/mysqldump -h {host} -u {user} -p{password} {database} > {backup_file}"
        
        # Execute the command in shell
        subprocess.run(dump_command, shell=True, check=True)
        
        print(f"Backup completed: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during backup: {e}")

def restore_database(backup_file):
    try:
        # Construct mysql command
        restore_command = f"mysql -h {host} -u {user} -p{password} {database} < {backup_file}"
        
        # Execute the command in shell
        subprocess.run(restore_command, shell=True, check=True)
        
        print(f"Restore completed from: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during restore: {e}")


#backup_database()
# Uncomment the line below and provide the backup file path to restore from the backup
restore_database("/home/bowie/Desktop/mansys_backup.sql")
