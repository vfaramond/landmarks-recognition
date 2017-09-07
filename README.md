# Landmark recognition system

First, make sure you have [Python 3](https://www.python.org/downloads/) installed on your machine, along with the following packages :
- [tqdm](https://github.com/tqdm/tqdm)
- [Tensorflow](https://www.tensorflow.org/install/)
- [Keras](https://keras.io/#installation)


## Dataset
The dataset comes from [here](http://landmark3d.codeplex.com).
A Python script is provided to download all the images:

```
$ python3 utils/download_data.py 'train'
$ python3 utils/download_data.py 'validation'
```

It can take several hours depending on your internet connection speed.

Once all the photos are in the `data` folder, run a cleanup script in order to remove not found images :
```
$ python3 utils/dataset_cleanup.py
```

## Build the model
A Python script is provided to build a simple CNN:

```
$ python3 utils/cnn_model.py
```

The model is saved in the `models/` folder.
