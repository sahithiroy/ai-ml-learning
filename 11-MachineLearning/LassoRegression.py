import numpy as np
class LassoRegression:
    def __init__(self,learning_rate,epchos,lambda_):
        self.slope=None
        self.intercept=None
        self.learning_rate=learning_rate
        self.epchos=epchos
        self.lambda_=lambda_
        self.loss_history=[]
    def predict(self,X):
        return self.slope*X+self.intercept
    def mse(self,y_actual,y_predicted):
        return np.mean((y_actual-y_predicted)**2)
    def l1_penalty(self):
        return self.lambda_*abs(self.slope)
    def calculate_loss(self,y_actual,y_predicted):
        mse_loss=self.mse(y_actual,y_predicted)
        penalty_loss=self.l1_penalty()
        total_loss=mse_loss+penalty_loss
        return total_loss
    def fit(self, X, y):
        X = np.array(X, dtype=float)
        y = np.array(y, dtype=float)
        m = len(X)
        self.slope = 0.0
        self.intercept = 0.0
        for epoch in range(self.epchos):
            y_predicted = self.predict(X)
            error = y_predicted - y
            mse_gradient = ((2 / m)*np.sum(X * error))
            l1_gradient = (self.lambda_*np.sign(self.slope))
            total_gradient = (mse_gradient+l1_gradient )
            intercept_gradient = ((2 / m)*np.sum(error))

            self.slope = (self.slope-self.learning_rate*total_gradient)

            self.intercept = (
                self.intercept
                -
                self.learning_rate
                *
                intercept_gradient
            )

            new_predictions = self.predict(X)

            loss = self.calculate_loss(
                y,
                new_predictions
            )

            self.loss_history.append(loss)

            if epoch % 1000 == 0:

                print(
                    f"Epoch: {epoch:5d} | "
                    f"Loss: {loss:.6f} | "
                    f"Slope: {self.slope:.4f} | "
                    f"Intercept: {self.intercept:.4f}"
                )


        print("\nTraining Complete!")

        print(
            f"Slope: {self.slope:.4f}"
        )

        print(
            f"Intercept: {self.intercept:.4f}"
        )
if __name__ == "__main__":

    print("=" * 60)
    print("L1 REGULARIZATION - LASSO FROM SCRATCH")
    print("=" * 60)


    # ----------------------------------------------------------
    # Dataset
    # ----------------------------------------------------------

    X = np.array([
        1,
        2,
        3,
        4,
        5
    ])

    y = np.array([
        2,
        4,
        5,
        8,
        10
    ])


    print("\nDataset:")

    print("X:", X)
    print("Y:", y)


    # ----------------------------------------------------------
    # Create model
    # ----------------------------------------------------------

    model = LassoRegression(
        learning_rate=0.01,
       epchos=10000,
        lambda_=0.1
    )


    # ----------------------------------------------------------
    # Train
    # ----------------------------------------------------------

    print("\n" + "=" * 60)
    print("TRAINING")
    print("=" * 60)

    model.fit(X, y)


    # ----------------------------------------------------------
    # Predictions
    # ----------------------------------------------------------

    print("\n" + "=" * 60)
    print("PREDICTIONS")
    print("=" * 60)

    predictions = model.predict(X)


    for i in range(len(X)):

        print(
            f"X = {X[i]} "
            f"→ Predicted = {predictions[i]:.4f} "
            f"→ Actual = {y[i]}"
        )


    # ----------------------------------------------------------
    # Final evaluation
    # ----------------------------------------------------------

    mse = model.mse(
        y,
        predictions
    )

    penalty = model.l1_penalty()

    total_loss = model.calculate_loss(
        y,
        predictions
    )


    print("\n" + "=" * 60)
    print("FINAL EVALUATION")
    print("=" * 60)

    print(
        f"MSE: {mse:.4f}"
    )

    print(
        f"L1 Penalty: {penalty:.4f}"
    )

    print(
        f"Total Loss: {total_loss:.4f}"
    )
