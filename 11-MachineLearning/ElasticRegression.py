import numpy as np
class ElasticRegression:
    def __init__(self,learning_rate,epchos,lambda_l1,lambda_l2):
        self.slope=None
        self.intercept=None
        self.learning_rate=learning_rate
        self.epchos=epchos
        self.lambda_l1=lambda_l2
        self.lambda_l2 = lambda_l2
        self.loss_history=[]
    def predict(self,X):
        return np.dot(X, self.slope) + self.intercept
    def mse(self,y_actual,y_predicted):
        return np.mean((y_actual-y_predicted)**2)
    def calculate_l2_penalty(self):
        return self.lambda_l2*np.sum(self.slope**2)
    def calculate_l1_penalty(self):
        return self.lambda_l1*np.abs(self.slope)
    def calculate_loss(self,y_actual,y_predicted):
        mse_loss=self.mse(y_actual,y_predicted)
        l1_penalty_loss=self.calculate_l1_penalty()
        l2_penalty_loss=self.calculate_l2_penalty()
        total_loss=mse_loss+l1_penalty_loss+l2_penalty_loss
        return total_loss
    def fit(self, X, y):
            X = np.array(X, dtype=float)
            y = np.array(y, dtype=float)
            m = len(X)
            n_features = X.shape[1]
            self.slope = np.zeros(n_features)
           
            self.intercept = 0.0
            for epoch in range(self.epchos):
                y_predicted = self.predict(X)
                error = y_predicted - y
                mse_gradient = ((2 / m)*np.dot(X.T, error))
                l1_gradient = (self.lambda_l1*np.sign(self.slope))
                l2_gradient=(self.lambda_l2*np.sign(self.slope))
                total_gradient = (mse_gradient+l1_gradient+l2_gradient )
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
                    f"Loss: {loss} | "
                    f"Weights: {self.slope} | "
                    f"Intercept: {self.intercept:.4f}"
                )
    
    
            print("\nTraining Complete!")
    
            print(
                f"Slope: {self.slope}"
            )
    
            print(
                f"Intercept: {self.intercept:.4f}")
if __name__ == "__main__":

    print("=" * 60)
    print("ELASTIC REGRESSION FROM SCRATCH")
    print("=" * 60)


    # ==========================================================
    # DATASET
    #
    # Two features:
    #
    # X1 = Study Hours
    # X2 = Previous Score
    # ==========================================================

    X = np.array([

        [1, 50, 6, 10],

        [2, 55, 7, 20],

        [3, 60, 6, 30],

        [4, 65, 8, 40],

        [5, 70, 7, 50],

        [6, 75, 8, 60],

        [7, 80, 7, 70],

        [8, 85, 8, 80]

    ])

    y = np.array([

        52,
        58,
        64,
        71,
        77,
        84,
        90,
        96

    ])


    print("\nDataset:")

    print("X:")
    print(X)

    print("\ny:")
    print(y)


    # ==========================================================
    # CREATE RIDGE MODEL
    # ==========================================================

    model = ElasticRegression(
        learning_rate=0.00001,
        epchos=10000,
        lambda_l1=0.01,
        lambda_l2=0.01
    )


    # ==========================================================
    # TRAIN
    # ==========================================================

    print("\n" + "=" * 60)
    print("TRAINING")
    print("=" * 60)

    model.fit(X, y)


    # ==========================================================
    # PREDICTIONS
    # ==========================================================

    print("\n" + "=" * 60)
    print("PREDICTIONS")
    print("=" * 60)

    predictions = model.predict(X)


    for i in range(len(X)):

        print(
            f"Actual: {y[i]:.2f} "
            f"→ Predicted: {predictions[i]:.2f}"
        )
    mse = model.mse(
        y,
        predictions
    )

    l2_penalty = model.calculate_l2_penalty()

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
        f"L2 Penalty: {l2_penalty:.4f}"
    )

    print(
        f"Total Ridge Loss: {total_loss}"
    )