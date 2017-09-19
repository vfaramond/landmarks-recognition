# Landmarks recognition

This repository contains Python scripts and notebooks to generate classification models for 25 landmarks.

Five notebooks are present in the `notebooks/` folder:
* `1 - Basic CNN` which creates a model from a basic CNN ;
* `2 - Data Augmentation` which used the same basic CNN with data augmentation ;
* `3 - Bottleneck features` which uses the bottleneck features from a pre-trained VGG16 CNN ;
* `4 - Fine-tuning` which fine-tunes the last convolutional block of a pre-trained VGG16 CNN ;
* `5 - Adversarial examples with FGSM` which generates adversarial examples with FGSM (Fast Gradient Sign Method) ;
* `6 - Cleverhans benchmark` which bencharmks our basic CNN model with `cleverhans` package using FGSM attack.

The five notebooks were run on a `p2.xlarge` [AWS EC2](https://aws.amazon.com/ec2/) instance using the [Deep Learning AMI](https://aws.amazon.com/marketplace/pp/B06VSPXKDX).

## Local development

First, make sure you have [Python 3](https://www.python.org/downloads/) installed on your machine, along with the following packages :
- [tqdm](https://github.com/tqdm/tqdm)
- [Tensorflow](https://www.tensorflow.org/install/)
- [Keras](https://keras.io/#installation)
- [cleverhans](https://github.com/tensorflow/cleverhans)

The dataset comes from [here](http://landmark3d.codeplex.com).
A Python script is provided to download all the images:

```
$ python3 utils/download_data.py 'train'
$ python3 utils/download_data.py 'validation'
```

It can take several hours depending on your internet connection speed.

Once all the photos are in the `data` folder, run a cleanup script in order to remove not found images :
```
$ python utils/dataset_cleanup.py
```

You can now execute the notebooks on your local environment !
