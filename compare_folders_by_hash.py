from calculate_folder_hash import calculate_folder_hash


def compare_folders_by_hash(folder_path1, folder_path2):
    hash1 = calculate_folder_hash(folder_path1)
    hash2 = calculate_folder_hash(folder_path2)

    return hash1 == hash2

