import subprocess
import datetime
import os

# MySQL connection details
host = 'localhost'
user = 'root'
password = '030709'
database = 'mansys'

def get_desktop_path():
    # Get the path to the Desktop directory for the current user
    home = os.path.expanduser("~")
    return os.path.join(home, "Desktop")

def backup_database():
    try:
        # Get Desktop path
        backup_dir = get_desktop_path()

        # Create a timestamped backup file name
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        backup_file = os.path.join(backup_dir, f"{database}_backup_{timestamp}.sql")

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
        restore_command = f"mysql -h {host} -u {user} -p {password} {database} < {backup_file}"
        
        # Execute the command in shell
        subprocess.run(restore_command, shell=True, check=True)
        
        print(f"Restore completed from: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during restore: {e}")

backup_database()