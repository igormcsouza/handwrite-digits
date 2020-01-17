# Handwrite Digits Classifier
This extract was inpired by PyImageSearch, case studies edition 3!

## How to find the data?
The data will be mounted on docker! Nevertheless you may find them [here](https://www.kaggle.com/c/digit-recognizer/data) or type the command below on terminal

    wget -O data.zip https://bit.ly/2RvHoZB

## How to run it
First, test data,

    python train.py --dataset /data/train.csv --model /weights/model.cpickle

Then classify the model, you may use any handwrite-digit picture you have for test, I also provide one for you,

    python classify.py --model /weights/model.cpickle --image /data/test.jpg

