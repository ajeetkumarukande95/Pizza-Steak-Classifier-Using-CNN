# Pizza-Steak-Classifier-Using-CNN

# DATASET LINK:
!wget https://storage.googleapis.com/ztm_tf_course/food_vision/pizza_steak.zip

Note:
You can use CNNs for image data as well as text data. CNNs exploit local relationships very well.
An image has patterns which are very well spatially correlated on a local scale (i.e., we don't have per pixel patterns, rather they span in a spatial location with a definite structure).
So if a sentence has a structure which is influenced more by local nearby relationships (in the context of the NLP problem), CNNs will work really well.

Examples:
Simple image classification, whether a picture of food contains pizza or a steak.
Detect whether or not an object appears in an image (i.e., did a specific car pass through the security cameras).

Steps:

Getting the dataset:
Where to keep/host large datasets in case > gdrive storage.
Dataset fetching scripts.
Common dataset sources for different kinds of problems.
Version controlling or putting the dataset in a remote repo: dvc.

Preparing the dataset:
Making sure it's the right size.
Dataset directory structure/Creating a CustomDataset Class.
Augmentation techniques.
Noise removal.
Batch Data Loader, prefetching (Important for large datasets).
Creating a baseline model.

Experimenting with large models (on a small training subset).

Fitting and monitoring the training:

TensorBoard, Weights & Biases.

Visualizing the predictions.

Evaluating the model.

Improving the model.

Comparing the models.

Making a prediction with the trained model.
