import argparse
import os
import sys
import threading
import urllib.request
from functools import partial
from multiprocessing.pool import ThreadPool
from tqdm import tqdm


DATASET_DIRECTORY = os.path.join(os.path.dirname(
    __file__), '../dataset/landmark3d_v1.0')
DATA_DIRECTORY = os.path.join(os.path.dirname(
    __file__), '../data')


def get_lines_number(file_path):
    """Return the number of lines in the given file."""
    return sum(1 for line in open(file_path, 'r'))


def download_dir(lock, idx, directories, list_file, destination_directory):
    """Download the images corresponding to a given directory."""
    dir = directories[idx]

    file_path = os.path.join(DATASET_DIRECTORY, dir, list_file)

    n_lines = get_lines_number(file_path)

    with lock:
        progress = tqdm(
            total=n_lines,
            position=idx,
            desc=dir,
        )

    for line in open(file_path):
        line_data = line.split('\t')
        file_name = line_data[0]
        url = line_data[1]

        images_directory = os.path.join(destination_directory, dir)

        if not os.path.exists(images_directory):
            os.makedirs(images_directory)

        file_path = os.path.join(images_directory, file_name)

        if not os.path.exists(file_path):
            urllib.request.urlretrieve(url, file_path)

        with lock:
            progress.update(1)

    with lock:
        progress.close()


def main():
    parser = argparse.ArgumentParser(description="Script to download images")
    parser.add_argument("data_type", help="Whether 'train' or 'validation'")
    args = parser.parse_args()

    if args.data_type in ['train', 'validation']:
        destination_directory = os.path.join(DATA_DIRECTORY, args.data_type)
        list_file = 'list_db.txt' if args.data_type == 'train' else 'list_test.txt'
    else:
        parser.error('data_type argument has not a valid value.')

    directories = os.listdir(DATASET_DIRECTORY)
    n_directories = len(directories)

    pool = ThreadPool(n_directories)
    lock = threading.Lock()

    for i in range(n_directories):
        pool.apply_async(download_dir, args=(
            lock, i, directories, list_file, destination_directory))

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
