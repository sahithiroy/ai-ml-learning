'''With KNN:

Training data
     ↓
Store the data
     ↓
New point arrives
     ↓
Calculate distances
     ↓
Find K closest points
     ↓
Vote
     ↓
Prediction

So KNN is called a:

Lazy Learning algorithm

because it doesn't do much work during training.
Small K
   ↓
Very local
   ↓
Sensitive to noise
   ↓
Overfitting risk


Large K
   ↓
Very general
   ↓
Ignores local patterns
   ↓
Underfitting risk
                  Training Data
                       ↓
                  Store the data
                       ↓
                 New data point
                       ↓
                Calculate distance
                       ↓
                 Sort distances
                       ↓
                  Select K nearest
                       ↓
             ┌─────────┴─────────┐
             ↓                   ↓
       Classification        Regression
             ↓                   ↓
       Majority vote           Average
             ↓                   ↓
          Prediction          Prediction'''

import numpy as np
class KNN:
    def __init__(self,k=3):
        self.k=k
        self.X_train=None
        self.y_train=None
    def fit(self,X,y):
        self.X_train=np.array(X,dtype=float)
        self.y_train=np.array(y)
        print("="*60)
        print("KNN TRAINING")
        print("="*50)
        print(
            f"Training samples: "
            f"{len(self.X_train)}"
        )

        print(
            f"Number of features: "
            f"{self.X_train.shape[1]}"
        )

        print(
            f"K value: {self.k}"
        )

        print("\nTraining Complete!")
    def euclidean_distance(self,x1,x2):
        distance=np.sqrt(np.sum((x1-x2)**2))
        return distance
    def predict_sample(self,x):
        distances=[]
        for i in range(len(self.X_train)):
            distance=self.euclidean_distance(x,self.X_train[i])
            distances.append((distance,self.y_train[i]))
        distances.sort(key=lambda item:item[0])
        k_neighbors=distances[:self.k]
        print("\nNew Point:", x)

        print("Nearest Neighbors:")
        for distance,label in k_neighbors:
            print(
                f"Distance = "
                f"{distance:.4f}, "
                f"Class = {label}"
            )
        labels=[label for distance,label in k_neighbors]
        classes,counts=np.unique(labels,return_counts=True)
        majority_index=np.argmax(counts)
        prediction=classes[majority_index]
        return prediction
    def predict(self,X):
        X=np.array(X,dtype=float)
        predictions=[]
        for x in X:
            prediction=self.predict_sample(x)
            predictions.append(prediction)

        return np.array(predictions)
    def accuracy(self,y_actaul,y_predicted):
        accuarcy=np.mean(y_actaul==y_predicted)
        return accuarcy
if __name__ == "__main__":

    # ==========================================================
    # DATASET
    #
    # Feature 1 = Study Hours
    # Feature 2 = Attendance
    #
    # 0 = Fail
    # 1 = Pass
    # ==========================================================

    X = np.array([

        [1, 50],
        [2, 55],
        [2, 60],
        [3, 65],
        [3, 70],

        [4, 75],
        [5, 80],
        [5, 85],
        [6, 90],
        [6, 95]

    ])

    y = np.array([

        0,
        0,
        0,
        0,
        0,

        1,
        1,
        1,
        1,
        1

    ])

    # ==========================================================
    # FEATURE NAMES
    # ==========================================================

    feature_names = [

        "Study Hours",
        "Attendance"

    ]

    print("FEATURES:")
    print(feature_names)

    print("\nTARGET:")
    print(y)

    # ==========================================================
    # CREATE MODEL
    # ==========================================================

    model = KNN(
        k=3
    )

    # ==========================================================
    # TRAIN
    # ==========================================================

    model.fit(
        X,
        y
    )

    # ==========================================================
    # PREDICTIONS
    # ==========================================================

    print("\n" + "=" * 60)
    print("TRAINING DATA PREDICTIONS")
    print("=" * 60)

    predictions = model.predict(
        X
    )

    for i in range(
        len(X)
    ):

        result = (

            "PASS"

            if predictions[i] == 1

            else

            "FAIL"

        )

        print(

            f"Student {i + 1}: "
            f"Study Hours = {X[i][0]}, "
            f"Attendance = {X[i][1]}, "
            f"Actual = {y[i]}, "
            f"Predicted = {predictions[i]} "
            f"→ {result}"

        )

    # ==========================================================
    # ACCURACY
    # ==========================================================

    accuracy = model.accuracy(
        y,
        predictions
    )

    print("\n" + "=" * 60)
    print("MODEL EVALUATION")
    print("=" * 60)

    print(
        f"Accuracy: {accuracy:.2%}"
    )

    # ==========================================================
    # NEW STUDENTS
    # ==========================================================

    new_students = np.array([

        [2.5, 62],

        [4.5, 82],

        [3.5, 72],

        [5.5, 92]

    ])

    print("\n" + "=" * 60)
    print("NEW STUDENT PREDICTIONS")
    print("=" * 60)

    new_predictions = model.predict(
        new_students
    )

    for i in range(
        len(new_students)
    ):

        result = (

            "PASS"

            if new_predictions[i] == 1

            else

            "FAIL"

        )

        print(

            f"Student {i + 1}: "
            f"Study Hours = "
            f"{new_students[i][0]}, "
            f"Attendance = "
            f"{new_students[i][1]} "
            f"→ {result}"

        )

        
