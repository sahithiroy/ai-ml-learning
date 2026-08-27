import numpy as np
class LinearRegression:
    def __init__(self):
        self.slope=None
        self.intercept=None
    def fit(self,X,Y):
        X_mean=np.mean(X)
        Y_mean=np.mean(Y)
        numerator=np.mean((X-X_mean)*(Y-Y_mean))
        denominator=np.mean((X-X_mean)**2)
        self.slope=numerator/denominator

        self.intercept=Y_mean-(X_mean*self.slope)
        print(f"Training Complete!")
        print(f"Slope (m): {self.slope:.4f}")
        print(f"Intercept (c): {self.intercept:.4f}")
        print(f"Equation: Y = {self.slope:.4f}X + {self.intercept:.4f}")
    def predict(self,x):
        if self.slope is None or self.intercept is None:
            raise Exception("model not trained yet")
        return self.slope*x+self.intercept
    def calculate_mse(self,y_actual,y_predict):
        return np.mean((y_actual-y_predict)**2)
    def calculate_mae(self,y_actual,y_predict):
        return np.mean((y_actual-y_predict))
    def calculate_rmse(self,y_actual,y_predict):
        mse= np.mean((y_actual-y_predict)**2)
        return np.sqrt(mse)
    def residual(self,Y,Y_predict):
        Y_mean=np.mean(Y)
        Y_mean_predict=np.mean(Y_predict)
        ss_total=np.mean((Y-Y_mean)**2)
        ss_res=np.mean((Y_predict-Y_mean_predict)**2)
        return 1-(ss_res/ss_total)
    def calculate_gradient(self,X,Y,predictions):
        m=len(X)
        error=predictions-Y
        gradient_intercept=(2/m)*np.sum(error)
        gradient_slope=(2/m)*np.sum(error*X)
        return gradient_intercept,gradient_slope
    def fit_gradient_descent(self,X,Y,learning_rate=0.01,epochs=1000):

        X = np.array(X, dtype=float)
        Y = np.array(Y, dtype=float)
        self.learning_rate = learning_rate
        self.slope = 0.0
        self.intercept = 0.0
        self.cost_history = []
        print("\nGradient Descent Training")
        print(f"Learning Rate: {learning_rate}")
        print(f"Epochs: {epochs}")

        for epoch in range(epochs):
            predictions = (
                self.slope * X
                + self.intercept
            )

            error = predictions - Y
            gradient_intercept, gradient_slope = (
                self.calculate_gradient(
                    X,
                    Y,
                    predictions
                )
            )

            self.intercept = (
                self.intercept
                - learning_rate * gradient_intercept
            )

            self.slope = (
                self.slope
                - learning_rate * gradient_slope
            )
            new_predictions = (
                self.slope * X
                + self.intercept
            )

            cost = self.calculate_mse(
                Y,
                new_predictions
            )

            self.cost_history.append(cost)

            # Print progress
            if epoch % 100 == 0:

                print(
                    f"Epoch {epoch}: "
                    f"Cost = {cost:.6f}, "
                    f"Slope = {self.slope:.4f}, "
                    f"Intercept = {self.intercept:.4f}"
                )

        print("\nGradient Descent Training Complete!")

        print(f"Slope: {self.slope:.4f}")
        print(f"Intercept: {self.intercept:.4f}")

        print(
            f"Equation: Y = "
            f"{self.slope:.4f}X + "
            f"{self.intercept:.4f}"
        )
    def evaluate(self,y,predictions):
        mse = model.calculate_mse(y, predictions)
        print(f"\nMean Squared Error (MSE): {mse:.4f}")
        print("\n" + "=" * 50)
        mae = model.calculate_mae(y, predictions)
        print(f"\nMean absolute Error (MAE): {mae:.4f}")
        print("\n" + "=" * 50)
        rmse = model.calculate_rmse(y, predictions)
        print(f"\nMean square root Error (RMSE): {rmse:.4f}")
        print("\n" + "=" * 50)
        res = model.residual(y, predictions)
        print(f"\nResidual: {res:.4f}")
        print("\n" + "=" * 50)


if __name__=="__main__":
    X = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 5, 4, 5])
    print("=" * 50)
    print("LINEAR REGRESSION FROM SCRATCH")
    print("=" * 50)
    print("\nDataset:")
    print("Study Hours (X):", X)
    print("Exam Scores (Y):", y)
    print()
    model = LinearRegression()
    model.fit(X, y)
    print("\n" + "=" * 50)
    print("PREDICTIONS")
    print("=" * 50)
    predictions = model.predict(X)
    for i in range(len(X)):
        print(f"Study Hours: {X[i]} → Predicted Score: {predictions[i]:.2f} (Actual: {y[i]})")
    model.evaluate(y,predictions)
    print("\n")
    print("=" * 60)
    print("2. GRADIENT DESCENT")
    print("=" * 60)

    gradient_model = LinearRegression()

    gradient_model.fit_gradient_descent(
        X,
        y,
        learning_rate=0.01,
        epochs=1000
    )


    # ------------------------------------------------------------
    # Predictions
    # ------------------------------------------------------------

    predictions_gradient = gradient_model.predict(X)

    print("\nPredictions:")

    for i in range(len(X)):

        print(
            f"Study Hours: {X[i]} "
            f"→ Predicted: {predictions_gradient[i]:.2f} "
            f"| Actual: {y[i]}"
        )


    # ------------------------------------------------------------
    # Residuals
    # ------------------------------------------------------------

    residuals_gradient = (
        gradient_model.residual(
            y,
            predictions_gradient
        )
    )

    print("\nResiduals:")

    print(residuals_gradient)


    # ------------------------------------------------------------
    # Evaluation
    # ------------------------------------------------------------

    gradient_model.evaluate(
        y,
        predictions_gradient
    )
    print("\n")
    print("=" * 60)
    print("3. NORMAL EQUATION vs GRADIENT DESCENT")
    print("=" * 60)

    print("\nParameter Comparison:")

    print(
        f"Normal Equation → "
        f"Slope = {model.slope:.6f}, "
        f"Intercept = {model.intercept:.6f}"
    )

    print(
        f"Gradient Descent → "
        f"Slope = {gradient_model.slope:.6f}, "
        f"Intercept = {gradient_model.intercept:.6f}"
    )

    print("TESTING WITH NEW DATA")
    print("=" * 50)
    new_hours = np.array([2.5, 6, 7])
    new_predictions = model.predict(new_hours)
    for i in range(len(new_hours)):
        print(f"Study Hours: {new_hours[i]} → Predicted Score: {new_predictions[i]:.2f}")
    
'''8. Example of a GOOD model

Suppose:

Training:
R²   = 0.91
RMSE = 5.2

Testing:
R²   = 0.89
RMSE = 5.6

This is generally encouraging.

Why?

Because training and testing performance are reasonably close.

Training → 91%
Testing  → 89%

The model seems to generalize well.

9. Example of OVERFITTING

Suppose:

Training:
R² = 0.99

Testing:
R² = 0.55

That's a warning sign.

The model learned the training data extremely well but performs much worse on unseen data.

This is overfitting.

Think:

Training data
     ↓
Model memorizes patterns
     ↓
Excellent training score
     ↓
New data
     ↓
Poor performance
10. Example of UNDERFITTING

Suppose:

Training:
R² = 0.40

Testing:
R² = 0.38

Both are poor.

The model isn't even learning the training data well.

This can indicate underfitting.

Training → Poor
Testing  → Poor
11. What should we actually check?

When evaluating Linear Regression, I would use this checklist:

① MAE

Ask:

How far are predictions from actual values on average?

Lower = better

② MSE

Ask:

How large are the squared errors?

Lower = better

Especially useful when you want large errors to be penalized more.

③ RMSE

Ask:

What is the typical prediction error in the original target units?

Lower = better

④ R²

Ask:

How much variance does the model explain?

Higher is generally better.

⑤ Train vs Test

Ask:

Does the model perform similarly on unseen data?

This is extremely important for detecting overfitting.

⑥ Residuals

Look at:

Residual=Actual−Predicted

You want residuals to look roughly like random noise, rather than showing a systematic pattern.'''