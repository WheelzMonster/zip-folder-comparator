import os


def compare_zip_sizes(zip_file1, zip_file2):
    size1 = os.path.getsize(zip_file1)
    size2 = os.path.getsize(zip_file2)

    print(size1, size2)

    return size1 == size2