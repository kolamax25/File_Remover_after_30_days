import os
import shutil
import time

def remove_folder(path):

    if not shutil.rmtree(path):

        print(f"{path} has been removed successfully")

    else:

        print(f"Unable to delete " + path)

def remove_file(path):

    if not os.remove(path):

        print(f"{path} has been removed successfully")

    else:

        print(f"Unable to delete " + path)

def get_file_or_folder_age(path):

    ctime = os.stat(path).st_ctime

    return ctime


def main():

    deleted_folders_count = 0
    deleted_files_count = 0

    path = "/PATH_TO_DELETE"

    days = 30

    seconds = time.time() - (days * 86400)

    if os.path.exists(path):

        for root_folder, folders, files in os.walk(path):

            if seconds >= get_file_or_folder_age(root_folder):

                remove_folder(root_folder)
                deleted_folders_count += 1

                break

            else:

                for folder in folders:

                    folder_path = os.path.join(root_folder, folder)

                    if seconds >= get_file_or_folder_age(folder_path):

                        remove_folder(root_folder)
                        deleted_folders_count += 1  

                for file in files:

                    file_path = os.path.join(root_folder, file)

                    if seconds >= get_file_or_folder_age(file_path):

                        remove_file(root_folder)
                        deleted_files_count += 1  

        else:

            if seconds >= get_file_or_folder_age(path):

                remove_file(path)
                deleted_files_count += 1
    
    else:

        print(f"In total {deleted_folders_count} folders were deleted")
        print(f"In total {deleted_files_count} files were deleted")

if __name__ == '__main__':
    main()