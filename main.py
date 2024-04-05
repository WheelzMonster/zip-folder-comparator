from datetime import datetime
from zip_folder import zip_folder
from compare_zip_sizes import compare_zip_sizes
from compare_folders_by_hash import compare_folders_by_hash

folder_to_zip = "./andrea"
og_zip_file = 'C:/Users/louis/Documents/andrea.zip'


def main():
    today_date = datetime.today().strftime('%Y-%m-%d')
    output_zip_file = f'{today_date}_andrea.zip'
    zip_folder(folder_to_zip, output_zip_file)

    if compare_zip_sizes(output_zip_file, og_zip_file):
        print("The sizes of the zip files are the same.")
    else:
        print("The sizes of the zip files are different.")

    if compare_folders_by_hash(output_zip_file, og_zip_file):
        print("The contents of the folders are the same.")
    else:
        print("The contents of the folders are different.")


if __name__ == '__main__':
    main()
