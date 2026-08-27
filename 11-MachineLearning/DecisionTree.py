import numpy as np
class DecisionTree:
    def __init__(self,max_depth=3,min_sample_spilt=2):
        self.max_depth=max_depth
        self.min_sample_spilt=min_sample_spilt
        self.tree=0
    def gini_impurity(self,y):
        if len(y)==0:
            return 0
        classes,counts=np.unique(y,return_counts=True)
        probabilities=counts/len(y)
        gini=1-np.sum(probabilities**2)
        print("gini",gini)
        return gini
    def calculate_split_gini(self,y_left,y_right):
        n=len(y_left)+len(y_right)
        gini_left=self.gini_impurity(y_left)
        gini_right=self.gini_impurity(y_right)
        weighted_gini=((len(y_left)/n)*gini_left+(len(y_right)/n)*gini_right)
        return weighted_gini
    def split_data(self,X,y,feature_index,threshold):
        left_mask=X[:,feature_index]<=threshold
        right_mask=X[:,feature_index]>threshold
        X_left=X[left_mask]
        y_left=y[left_mask]
        X_right=X[right_mask]
        y_right=y[right_mask]
        return X_left,y_left,X_right,y_right
    def find_est_split(self,X,y):
        best_gini=float("inf")
        best_feature=None
        best_threshold=None
        n_features=X.shape[1]
        for feature_index in range(n_features):
            feature_values=np.unique(X[:,feature_index])
            for threshold in feature_values:
                X_left,y_left,X_right,y_right=self.split_data(X,y,feature_index,threshold)
                if len(y_left)==0 or len(y_right)==0:
                    continue
                gini=self.calculate_split_gini(y_left,y_right)
                if gini<best_gini:
                    best_gini=gini
                    best_feature=feature_index
                    best_threshold =threshold
        return best_feature,best_threshold,best_gini
    def majority_class(self,y):
        classes,counts=np.unique(y,return_counts=True)
        index=np.argmax(counts)
        return classes[index]
    def build_tree(self,X,y,depth=0):
        number_of_samples=len(y)
        number_of_classes=len(np.unique(y))
        prediction=self.majority_class(y)
        if number_of_classes==1:
            return{
                "type":"leaf",
                "prediction":prediction
            }
        if depth>=self.max_depth:
            return {
                "type":"leaf",
                "prediction":prediction
            }
        if number_of_samples<self.min_sample_spilt:
            return {
                "type":"leaf",
                "prediction":prediction
            }
        best_feature,best_threshold,best_gini=(self.find_est_split(X,y))
        if best_feature is None:
            return {
                    "type":"leaf",
                    "prediction":prediction
                }
        X_left,y_left,X_right,y_right=self.split_data(X,y,best_feature,best_threshold)
        print(
            "  " * depth
            + f"Depth {depth}: "
            f"Feature {best_feature} <= {best_threshold} "
            f"| Gini = {best_gini:.4f}"
        )
        left_subtree=self.build_tree(X_left,y_left,depth+1)
        right_subtree=self.build_tree(X_right,y_right,depth+1)
        return {
            "type":"node",
            "feature":best_feature,
            "threshold":best_threshold,
            "gini":best_gini,
            "left":left_subtree,
            "right":right_subtree
        }
    def fit(self,X,y):
        X=np.array(X,dtype=float)
        y=np.array(y)
        print("=" * 60)
        print("BUILDING DECISION TREE")
        print("=" * 60)

        self.tree = self.build_tree(X, y)

        print("\nTraining Complete!")
    def predict_sample(self,x,node):
        if node["type"]=="leaf":
            return node["prediction"]
        feature=node["feature"]
        threshold=node["threshold"]
        if x[feature]<=threshold:
            return self.predict_sample(x,node["left"])
        else:
            return self.predict_sample(x,node["right"])
    def predict(self,X):
        X=np.array(X,dtype=float)
        predictions=[]
        for x in X:
            prediction=self.predict_sample(x,self.tree)
            predictions.append(prediction)
        return np.array(predictions)
    def accuracy(self,y_actual,y_predicted):
        return np.mean(y_actual==y_predicted)
if __name__=="__main__":
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

    # ----------------------------------------------------------
    # TARGET
    #
    # 0 = Fail
    # 1 = Pass
    # ----------------------------------------------------------

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

    # ----------------------------------------------------------
    # FEATURE NAMES
    # ----------------------------------------------------------

    feature_names = [
        "Study Hours",
        "Attendance",
        "Previous Score"
    ]

    print("FEATURES:")
    print(feature_names)

    print("\nTARGET:")
    print(y)

    # ----------------------------------------------------------
    # CREATE MODEL
    # ----------------------------------------------------------

    model = DecisionTree(
        max_depth=3,
        min_sample_spilt=2
    )

    # ----------------------------------------------------------
    # TRAIN
    # ----------------------------------------------------------

    model.fit(X, y)

    # ----------------------------------------------------------
    # PREDICTIONS ON TRAINING DATA
    # ----------------------------------------------------------

    print("\n" + "=" * 60)
    print("PREDICTIONS")
    print("=" * 60)

    predictions = model.predict(X)

    for i in range(len(X)):

        print(
            f"Student {i + 1}: "
            f"Actual = {y[i]}, "
            f"Predicted = {predictions[i]}"
        )

    # ----------------------------------------------------------
    # ACCURACY
    # ----------------------------------------------------------

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

    # ----------------------------------------------------------
    # TEST WITH NEW STUDENTS
    # ----------------------------------------------------------

    new_students = np.array([

        [2.5, 68, 48],
        [5.5, 90, 78],
        [3.5, 72, 60]

    ])

    new_predictions = model.predict(
        new_students
    )

    print("\n" + "=" * 60)
    print("NEW STUDENT PREDICTIONS")
    print("=" * 60)

    for i in range(len(new_students)):

        result = (
            "Pass"
            if new_predictions[i] == 1
            else "Fail"
        )

        print(
            f"Student {i + 1}: "
            f"Study Hours = {new_students[i][0]}, "
            f"Attendance = {new_students[i][1]}, "
            f"Previous Score = {new_students[i][2]} "
            f"→ {result}"
        )

'''17. Random Forest vs XGBoost

This comparison is extremely important.

Random Forest	XGBoost
Bagging	Boosting
Trees are mostly independent	Trees are sequential
Random samples	Corrects previous errors
Random feature subsets	Uses gradients
Majority voting for classification	Adds tree contributions
Mainly reduces variance	Mainly reduces bias, with regularization
Easier to understand	More complex
Usually robust with little tuning	Often very strong with careful tuning

The easiest way to remember:

Random Forest

Tree 1 ─┐
Tree 2 ─┤
Tree 3 ─┼──→ Vote → Final
Tree 4 ─┤
Tree 5 ─┘

versus:

XGBoost

Tree 1
  ↓
Correction
  ↓
Tree 2
  ↓
Correction
  ↓
Tree 3
  ↓
Correction
  ↓
Final
18. Random Forest analogy

Imagine 10 doctors independently examine a patient.

Doctor 1 → A
Doctor 2 → A
Doctor 3 → B
Doctor 4 → A
...

Then they vote.

That's similar to Random Forest.

19. XGBoost analogy

Now imagine one doctor examines the patient.

Another doctor looks specifically at what the first doctor missed.

Then another doctor looks at what both missed.

Doctor 1
   ↓
Missed something
   ↓
Doctor 2 focuses on it
   ↓
Still something missed
   ↓
Doctor 3 focuses on it

That's the intuition behind boosting.

20. The complete XGBoost intuition

Keep this flow in your notes:

                    DATA
                      ↓
              Initial Prediction
                      ↓
                Calculate Loss
                      ↓
               Calculate Gradient
                      ↓
             Build Decision Tree
                      ↓
             Calculate Correction
                      ↓
              Apply Learning Rate
                      ↓
             Update Prediction
                      ↓
                Loss decreases
                      ↓
              Build next tree
                      ↓
             Calculate new errors
                      ↓
             Build another tree
                      ↓
                    Repeat
                      ↓
              Final XGBoost Model
The one-line definition

XGBoost is a gradient-boosting algorithm that builds decision trees sequentially, with each new tree learning how to improve the errors of the current ensemble, while using learning rate and regularization to control overfitting.

And the most important distinction from what you've learned so far is:

Random Forest = many independent trees
	​

XGBoost = trees that learn sequentially from previous errors
	​
'''