'''INPUT
  X
  ↓
Linear equation
  z = b0 + b1X
  ↓
Sigmoid
  p = 1 / (1 + e^-z)
  ↓
Probability
  0 ≤ p ≤ 1
  ↓
Binary Cross-Entropy
  Loss = -[y log(p) + (1-y) log(1-p)]
  ↓
Average loss over all samples
  ↓
Gradient
  dw = (1/m) Xᵀ(p-y)
  ↓
Gradient Descent
  w = w - learning_rate × dw
  ↓
Update b
  b = b - learning_rate × db
  ↓
Repeat
  ↓
Loss decreases
  ↓
Better probabilities'''
import numpy as np
class LogisticRegression:
    def __init__(self):
        self.intercept=None
        self.slope=None
        self.loss_history=[]
    def fit(self,X,Y):
        X_mean=np.mean(X)
        Y_mean=np.mean(Y)
        numerator=(X_mean-X)*(Y_mean-Y)
        denominator=(X_mean-X)**2
        self.slope=numerator/denominator
        self.intercept=Y-(self.slope*X)
    def sigmoid(self,z):
        return 1 / (1 + np.exp(-z))


        
    def predict(self,X):
        threshold=0.5
        z=self.intercept+(self.slope*X)
        probability=1/1-np.exp(-z)
        predictions=(probability >= threshold).astype(int)
        return predictions,probability
    def binary_cross_entropy(self,y_actual,probability):
        epsilon = 1e-15

        probability = np.clip(
            probability,
            epsilon,
            1 - epsilon
        )

        loss = -np.mean(
            y_actual * np.log(probability)
            +
            (1 - y_actual) * np.log(1 - probability)
        )

        return loss
    def fit_gradient_descent(self,X,Y,learning_rate=0.01,epochs=1000):
        X = np.array(X, dtype=float)
        Y = np.array(Y, dtype=float)
        m = len(X)

        self.slope = 0.0
        self.intercept = 0.0

        for epoch in range(epochs):
            z = self.intercept + self.slope * X

            probability = self.sigmoid(z)

            loss = self.binary_cross_entropy(
                Y,
                probability
            )

            self.loss_history.append(loss)
            error = probability - Y
            slope_gradient = (
                1 / m
            ) * np.sum(
                X * error
            )
            intercept_gradient = (
                1 / m
            ) * np.sum(error)

            self.slope = (
                self.slope
                -
                learning_rate * slope_gradient
            )

            self.intercept = (
                self.intercept
                -
                learning_rate * intercept_gradient
            )
            if epoch % 1000 == 0:

                print(
                    f"Epoch: {epoch:5d} | "
                    f"Loss: {loss:.6f} | "
                    f"Slope: {self.slope:.4f} | "
                    f"Intercept: {self.intercept:.4f}"
                )


        print("\nTraining Complete!")

        print(f"Slope: {self.slope:.4f}")

        print(f"Intercept: {self.intercept:.4f}")

    def evaluate(self,y_actual,Y_predict):
        TP=np.sum((y_actual==1) & (Y_predict==1))
        TN=np.sum((y_actual==0) & (Y_predict==0))
        FN=np.sum((y_actual==1) & (Y_predict==0))
        FP=np.sum((y_actual==0) & (Y_predict==1))
        #Out of all predictions, how many did I get correct?
        print("Evaluate")
        print("="*50)
        print("\nConfusion Matrix:")

        print(
            f"TN = {TN}    FP = {FP}"
        )

        print(
            f"FN = {FN}    TP = {TP}"
        )

        print("=" * 60)
        accuary=(TP+TN)/(TP+TN+FP+FN)
        print("Accuarcy:" ,accuary)
        #When my model predicted Positive, how often was it actually Positive?
        precision=TP/(TP+FP)
        print("Precision: ",precision)
        #Out of all the actual Positive cases, how many did my model find?
        recall=TP/(TP+FN)
        print("Recall",recall)
        F1Score=((2*precision*recall)/precision+recall)
        print("F1Score",F1Score)

if __name__=="__main__":
    X=np.array([1,2,3,4])
    Y=np.array([0,0,1,1])
    print("=" * 50)
    print("LOGISTC REGRESSION FROM SCRATCH")
    print("=" * 50)
    print("\nDataset:")
    print("Study Hours (X):", X)
    print("Pass/Fail (Y):", Y)
    print()
    normal_model=LogisticRegression()
    normal_model.fit(X,Y)
    print("PREDICTIONS")
    print("=" * 50)
    predictions,probabilties = normal_model.predict(X)
    
    for i in range(len(X)):
        print(f"Study Hours: {X[i]} → Predicted Score: {predictions[i]:.2f} (Actual: {Y[i]})")
    print('Loss of function')
    print("="*50)
    entropy_loss=normal_model.binary_cross_entropy(Y,probabilties)
    print(entropy_loss)
    print("EVALUATE")
    print("="*50)
    normal_model.evaluate(Y,predictions)
    print("TESTING WITH NEW DATA")
    print("=" * 50)
    new_hours = np.array([2.5, 6, 7,5])
    new_predictions ,new_probabilties= normal_model.predict(new_hours)
    for i in range(len(new_hours)):
        print(f"Study Hours: {new_hours[i]} → Predicted Score: {new_predictions[i]:.2f}")

    print("GRADIENT DESCENT")
    gradient_model=LogisticRegression()
    gradient_model.fit_gradient_descent(X,Y)
    print("PREDICTIONS")
    print("=" * 50)
    predictions,probabilties = gradient_model.predict(X)
    
    for i in range(len(X)):
        print(f"Study Hours: {X[i]} → Predicted Score: {predictions[i]:.2f} (Actual: {Y[i]})")
    print('Loss of function')
    print("="*50)
    entropy_loss=gradient_model.binary_cross_entropy(Y,probabilties)
    print(entropy_loss)
    print("TESTING WITH NEW DATA")
    print("=" * 50)
    new_hours = np.array([2.5, 6, 7,5])
    new_predictions,new_probabilties = gradient_model.predict(new_hours)
    for i in range(len(new_hours)):
        print(f"Study Hours: {new_hours[i]} → Predicted Score: {new_predictions[i]:.2f}")

    print("EVALUATE")
    print("="*50)
    gradient_model.evaluate(Y,predictions)




'''Evaluation decision process
Step 1 — Look at the confusion matrix

First ask:

How many:

TP?
TN?
FP?
FN?

This tells you what kind of mistakes the model is making.

↓

Step 2 — Check class balance

Ask:

Are my classes balanced?

For example:

Class 0 → 50%
Class 1 → 50%

Balanced.

But:

Class 0 → 98%
Class 1 → 2%

Highly imbalanced.

If the data is imbalanced, don't rely on Accuracy alone.

↓

Step 3 — Decide which mistake matters more

Ask:

Is FP worse or FN worse?

This is the most important business/domain question.

15. If False Positive is worse

Example:

Spam detection

FP:
Normal email → incorrectly marked spam

You don't want too many false positives.

Therefore:

Precision is important
	​


You might accept somewhat lower Recall to obtain higher Precision.

16. If False Negative is worse

Example:

Disease screening

FN:
Disease → model says no disease

This can be dangerous.

Therefore:

Recall is important
	​


You want to catch as many positive cases as possible.

17. If both FP and FN matter

Use:

F1
	​


For example:

Fraud detection

You don't want:

Too many innocent customers flagged

but you also don't want:

Too much fraud missed

So Precision and Recall both matter.

18. What about Accuracy?

Use Accuracy when:

Classes are reasonably balanced
+
FP and FN have similar importance

Then Accuracy is a useful metric.

19. What about ROC-AUC?

Use ROC-AUC when you want to understand:

"Does the model generally separate the two classes well across thresholds?"

It's particularly useful for comparing classifiers or examining ranking performance.

But for highly imbalanced problems, also consider Precision-Recall curves / PR-AUC, because they can give a more informative picture of positive-class performance.
                 Logistic Regression
                         │
                         ↓
                Check Confusion Matrix
                         │
                         ↓
                  Check Class Balance
                         │
             ┌───────────┴───────────┐
             ↓                       ↓
         Balanced                Imbalanced
             │                       │
             ↓                       ↓
       Accuracy useful       Don't rely on Accuracy
                                     │
                                     ↓
                         Look at Precision/Recall
                                     │
                    ┌────────────────┴───────────────┐
                    ↓                                ↓
              FP is worse                       FN is worse
                    ↓                                ↓
                Precision                         Recall
                    │                                │
                    └────────────────┬───────────────┘
                                     ↓
                           Both matter?
                                     ↓
                                    F1
                                     │
                                     ↓
                          Probability quality?
                                     ↓
                                  Log Loss
                                     │
                                     ↓
                     Ranking/separation across
                          thresholds?
                                     ↓
                                 ROC-AUC
'''