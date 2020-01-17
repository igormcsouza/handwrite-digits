from sklearn.externals import joblib
from sklearn.svm import LinearSVC
from handwritedigits.hog import HOG
from handwritedigits import dataset
from tqdm import tqdm # Progress Bar!
import argparse

ap = argparse.ArgumentParser()
ap.add_argument(
    "-d", "--dataset", required = True,
    help = "path to the dataset file"
)
ap.add_argument(
    "-m", "--model", required = True,
    help = "path to where the model will be stored"
)
args = vars(ap.parse_args())

(digits, target) = dataset.load_digits(args["dataset"])
data = []

print("[INFO] Applying HOG")
hog = HOG(orientations = 18, pixelsPerCell = (10, 10),
cellsPerBlock = (1, 1), transform = True)

print("[INFO] Organizing dataset")
for image in tqdm(digits):
    image = dataset.deskew(image, 20)
    image = dataset.center_extent(image, (20, 20))

    hist = hog.describe(image)
    data.append(hist)

print("[INFO] Fitting data using LinearSVC")
model = LinearSVC(random_state = 42)
model.fit(data, target)

print("[INFO] Saving model")
joblib.dump(model, args["model"])