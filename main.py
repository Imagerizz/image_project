from src.pipeline.preprocess import copy_kaggle_dataset_to_raw, download_dataset


if __name__ == '__main__':
    print('Start downloading dataset...')
    download_dataset()
    print('Copying dataset...')
    copy_kaggle_dataset_to_raw("fareselmenshawii")
