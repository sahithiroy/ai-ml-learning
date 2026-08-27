'''
Ensemble Methods
│
├── Bagging
│     └── Random Forest
│
├── Boosting
│     ├── AdaBoost
│     ├── Gradient Boosting
│     ├── XGBoost
│     └── LightGBM
│
└── Voting
Random Forest is:
Many Decision Trees + Randomness + Voting
It is an ensemble of Decision Trees.

Instead of creating one Decision Tree
This is extremely important.

Why is it called Random Forest?

Because we introduce randomness in two main ways.

Randomness #1 — Random samples

Suppose our original dataset contains:

1000 students

Instead of giving every tree exactly the same dataset, we create different samples.
7. Randomness #2 — Random features

Suppose we have 10 features:

Study Hours
Attendance
Previous Score
Age
Sleep Hours
Assignments
...

A normal Decision Tree could consider all features when looking for a split.

Random Forest makes each tree consider a random subset of features at each split.
                    Original Dataset
                           ↓
                  Bootstrap Sampling
                           ↓
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
       Dataset 1        Dataset 2        Dataset 3
          ↓                ↓                ↓
       Tree 1             Tree 2          Tree 3
          ↓                ↓                ↓
     Random Features   Random Features   Random Features
          ↓                ↓                ↓
       Prediction        Prediction       Prediction
          ↓                ↓                ↓
          └────────────────┼────────────────┘
                           ↓
                    Combine Predictions
                           ↓
                 ┌─────────┴─────────┐
                 ↓                   ↓
            Classification       Regression
                 ↓                   ↓
            Majority Vote         Average
                 ↓                   ↓
               Final               Final
            Prediction          Prediction
'''
import numpy as np


class DecisionTree:

    def __init__(
        self,
        max_depth=3,
        min_samples_split=2,
        max_features=None
    ):

        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.max_features = max_features

        self.tree = None
    def gini_impurity(self, y):

        if len(y) == 0:
            return 0

        classes, counts = np.unique(
            y,
            return_counts=True
        )

        probabilities = counts / len(y)

        gini = 1 - np.sum(
            probabilities ** 2
        )

        return gini


    def split_data(
        self,
        X,
        y,
        feature_index,
        threshold
    ):

        left_mask = (
            X[:, feature_index] <= threshold
        )

        right_mask = (
            X[:, feature_index] > threshold
        )

        X_left = X[left_mask]
        y_left = y[left_mask]

        X_right = X[right_mask]
        y_right = y[right_mask]

        return (
            X_left,
            y_left,
            X_right,
            y_right
        )

    def find_best_split(self, X, y):

        best_gini = float("inf")
        best_feature = None
        best_threshold = None

        n_features = X.shape[1]


        if self.max_features is None:

            feature_indices = np.arange(
                n_features
            )

        else:

            number_of_features = min(
                self.max_features,
                n_features
            )

            feature_indices = np.random.choice(
                n_features,
                number_of_features,
                replace=False
            )


        for feature_index in feature_indices:

            feature_values = np.unique(
                X[:, feature_index]
            )

            for threshold in feature_values:

                (
                    X_left,
                    y_left,
                    X_right,
                    y_right
                ) = self.split_data(
                    X,
                    y,
                    feature_index,
                    threshold
                )

                # Ignore invalid splits

                if (
                    len(y_left) == 0
                    or
                    len(y_right) == 0
                ):

                    continue


                gini_left = self.gini_impurity(
                    y_left
                )

                gini_right = self.gini_impurity(
                    y_right
                )

                n = len(y_left) + len(y_right)

                weighted_gini = (

                    (len(y_left) / n)
                    * gini_left

                    +

                    (len(y_right) / n)
                    * gini_right
                )

                if weighted_gini < best_gini:

                    best_gini = weighted_gini

                    best_feature = feature_index

                    best_threshold = threshold

        return (
            best_feature,
            best_threshold,
            best_gini
        )


    def majority_class(self, y):

        classes, counts = np.unique(
            y,
            return_counts=True
        )

        index = np.argmax(counts)

        return classes[index]

    def build_tree(
        self,
        X,
        y,
        depth=0
    ):

        number_of_samples = len(y)

        number_of_classes = len(
            np.unique(y)
        )

        prediction = self.majority_class(
            y
        )

        # ------------------------------------------------------
        # STOP CONDITION 1
        # ------------------------------------------------------

        if number_of_classes == 1:

            return {
                "type": "leaf",
                "prediction": prediction
            }

        # ------------------------------------------------------
        # STOP CONDITION 2
        # ------------------------------------------------------

        if depth >= self.max_depth:

            return {
                "type": "leaf",
                "prediction": prediction
            }

        # ------------------------------------------------------
        # STOP CONDITION 3
        # ------------------------------------------------------

        if (
            number_of_samples
            <
            self.min_samples_split
        ):

            return {
                "type": "leaf",
                "prediction": prediction
            }

        # ------------------------------------------------------
        # Find best split
        # ------------------------------------------------------

        (
            best_feature,
            best_threshold,
            best_gini
        ) = self.find_best_split(
            X,
            y
        )

        # ------------------------------------------------------
        # No valid split
        # ------------------------------------------------------

        if best_feature is None:

            return {
                "type": "leaf",
                "prediction": prediction
            }

        # ------------------------------------------------------
        # Split
        # ------------------------------------------------------

        (
            X_left,
            y_left,
            X_right,
            y_right
        ) = self.split_data(
            X,
            y,
            best_feature,
            best_threshold
        )

        # ------------------------------------------------------
        # Build left subtree
        # ------------------------------------------------------

        left_subtree = self.build_tree(
            X_left,
            y_left,
            depth + 1
        )

        # ------------------------------------------------------
        # Build right subtree
        # ------------------------------------------------------

        right_subtree = self.build_tree(
            X_right,
            y_right,
            depth + 1
        )

        # ------------------------------------------------------
        # Return node
        # ------------------------------------------------------

        return {

            "type": "node",

            "feature": best_feature,

            "threshold": best_threshold,

            "gini": best_gini,

            "left": left_subtree,

            "right": right_subtree
        }


    # ==========================================================
    # 6. FIT TREE
    # ==========================================================

    def fit(self, X, y):

        X = np.array(
            X,
            dtype=float
        )

        y = np.array(y)

        self.tree = self.build_tree(
            X,
            y
        )


    # ==========================================================
    # 7. PREDICT ONE SAMPLE
    # ==========================================================

    def predict_sample(
        self,
        x,
        node
    ):

        # ------------------------------------------------------
        # Leaf
        # ------------------------------------------------------

        if node["type"] == "leaf":

            return node["prediction"]

        feature = node["feature"]

        threshold = node["threshold"]

        # ------------------------------------------------------
        # Go left
        # ------------------------------------------------------

        if x[feature] <= threshold:

            return self.predict_sample(
                x,
                node["left"]
            )

        # ------------------------------------------------------
        # Go right
        # ------------------------------------------------------

        else:

            return self.predict_sample(
                x,
                node["right"]
            )


    # ==========================================================
    # 8. PREDICT
    # ==========================================================

    def predict(self, X):

        X = np.array(
            X,
            dtype=float
        )

        predictions = []

        for x in X:

            prediction = (
                self.predict_sample(
                    x,
                    self.tree
                )
            )

            predictions.append(
                prediction
            )

        return np.array(
            predictions
        )


# ==============================================================
# RANDOM FOREST
# ==============================================================

class RandomForest:

    def __init__(
        self,
        n_trees=10,
        max_depth=3,
        min_samples_split=2,
        max_features=None
    ):

        self.n_trees = n_trees

        self.max_depth = max_depth

        self.min_samples_split = (
            min_samples_split
        )

        self.max_features = max_features

        self.trees = []


    # ==========================================================
    # 1. BOOTSTRAP SAMPLING
    # ==========================================================

    def bootstrap_sample(self, X, y):

        n_samples = X.shape[0]

        # Randomly select rows
        # with replacement

        indices = np.random.choice(
            n_samples,
            n_samples,
            replace=True
        )

        X_sample = X[indices]

        y_sample = y[indices]

        return X_sample, y_sample


    # ==========================================================
    # 2. FIT RANDOM FOREST
    # ==========================================================

    def fit(self, X, y):

        X = np.array(
            X,
            dtype=float
        )

        y = np.array(y)

        self.trees = []

        print("=" * 60)

        print(
            "BUILDING RANDOM FOREST"
        )

        print("=" * 60)

        print(
            f"Number of trees: "
            f"{self.n_trees}"
        )


        # ------------------------------------------------------
        # Build each tree
        # ------------------------------------------------------

        for i in range(
            self.n_trees
        ):

            print(
                f"\nBuilding Tree "
                f"{i + 1}"
            )

            # ----------------------------------------------
            # Bootstrap sample
            # ----------------------------------------------

            X_sample, y_sample = (
                self.bootstrap_sample(
                    X,
                    y
                )
            )

            # ----------------------------------------------
            # Create tree
            # ----------------------------------------------

            tree = DecisionTree(

                max_depth=self.max_depth,

                min_samples_split=(
                    self.min_samples_split
                ),

                max_features=(
                    self.max_features
                )
            )

            # ----------------------------------------------
            # Train tree
            # ----------------------------------------------

            tree.fit(
                X_sample,
                y_sample
            )

            # ----------------------------------------------
            # Store tree
            # ----------------------------------------------

            self.trees.append(
                tree
            )


        print("\n" + "=" * 60)

        print(
            "RANDOM FOREST TRAINING COMPLETE"
        )

        print("=" * 60)


    # ==========================================================
    # 3. PREDICT
    # ==========================================================

    def predict(self, X):

        X = np.array(
            X,
            dtype=float
        )

        all_predictions = []


        # ------------------------------------------------------
        # Get prediction from every tree
        # ------------------------------------------------------

        for tree in self.trees:

            predictions = tree.predict(
                X
            )

            all_predictions.append(
                predictions
            )


        # Convert to NumPy array

        all_predictions = np.array(
            all_predictions
        )


        # ------------------------------------------------------
        # Majority voting
        # ------------------------------------------------------

        final_predictions = []


        for sample_index in range(
            X.shape[0]
        ):

            predictions_for_sample = (
                all_predictions[
                    :,
                    sample_index
                ]
            )

            classes, counts = np.unique(
                predictions_for_sample,
                return_counts=True
            )

            majority_index = np.argmax(
                counts
            )

            final_prediction = classes[
                majority_index
            ]

            final_predictions.append(
                final_prediction
            )


        return np.array(
            final_predictions
        )


    # ==========================================================
    # 4. ACCURACY
    # ==========================================================

    def accuracy(
        self,
        y_actual,
        y_predicted
    ):

        return np.mean(
            y_actual == y_predicted
        )


# ==============================================================
# MAIN
# ==============================================================

if __name__ == "__main__":

    # ==========================================================
    # DATA
    #
    # Feature 0 = Study Hours
    # Feature 1 = Attendance
    # Feature 2 = Previous Score
    # ==========================================================

    X = np.array([

        [1, 60, 40],

        [2, 65, 45],

        [3, 70, 50],

        [4, 80, 65],

        [5, 85, 75],

        [6, 90, 80],

        [2, 60, 48],

        [5, 88, 72],

        [3, 75, 55],

        [6, 95, 85]

    ])


    # ==========================================================
    # TARGET
    #
    # 0 = Fail
    # 1 = Pass
    # ==========================================================

    y = np.array([

        0,
        0,
        0,
        1,
        1,
        1,
        0,
        1,
        0,
        1

    ])


    # ==========================================================
    # FEATURE NAMES
    # ==========================================================

    feature_names = [

        "Study Hours",

        "Attendance",

        "Previous Score"

    ]


    print("FEATURES:")

    print(
        feature_names
    )

    print("\nTARGET:")

    print(y)


    # ==========================================================
    # CREATE RANDOM FOREST
    # ==========================================================

    model = RandomForest(

        n_trees=10,

        max_depth=3,

        min_samples_split=2,

        # None means use all features.
        #
        # For Random Forest, you can use:
        #
        # max_features=2
        #
        # to randomly select 2 features
        # at every tree split.

        max_features=2
    )


    # ==========================================================
    # TRAIN
    # ==========================================================

    model.fit(
        X,
        y
    )


    # ==========================================================
    # TRAINING PREDICTIONS
    # ==========================================================

    print("\n" + "=" * 60)

    print(
        "PREDICTIONS"
    )

    print("=" * 60)


    predictions = model.predict(
        X
    )


    for i in range(
        len(X)
    ):

        print(

            f"Student {i + 1}: "

            f"Actual = {y[i]}, "

            f"Predicted = "
            f"{predictions[i]}"

        )


    # ==========================================================
    # ACCURACY
    # ==========================================================

    accuracy = model.accuracy(
        y,
        predictions
    )


    print("\n" + "=" * 60)

    print(
        "MODEL EVALUATION"
    )

    print("=" * 60)


    print(
        f"Accuracy: "
        f"{accuracy:.2%}"
    )


    # ==========================================================
    # NEW STUDENTS
    # ==========================================================

    new_students = np.array([

        [2.5, 68, 48],

        [5.5, 90, 78],

        [3.5, 72, 60]

    ])


    new_predictions = model.predict(
        new_students
    )


    print("\n" + "=" * 60)

    print(
        "NEW STUDENT PREDICTIONS"
    )

    print("=" * 60)


    for i in range(
        len(new_students)
    ):

        result = (

            "Pass"

            if new_predictions[i] == 1

            else

            "Fail"

        )


        print(

            f"Student {i + 1}: "

            f"Study Hours = "
            f"{new_students[i][0]}, "

            f"Attendance = "
            f"{new_students[i][1]}, "

            f"Previous Score = "
            f"{new_students[i][2]} "

            f"→ {result}"

        )