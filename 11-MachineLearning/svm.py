'''Absolutely. Let's understand Support Vector Machines (SVM) from scratch, especially the two important ideas:

Maximum Margin
Kernel Trick

I'll use a simple Pass/Fail example.

1. What is SVM?

SVM = Support Vector Machine.

It is a supervised machine learning algorithm mainly used for:

Classification
Regression

For classification, the basic idea is:

Find the best boundary that separates different classes.

Suppose we have students:

Fail = 0
Pass = 1

And we have two features:

Study Hours
Attendance

Imagine the data looks like this:

Attendance
   ↑
90 |                    P   P
   |                 P   P
80 |              P
   |
70 |         F
   |      F     F
60 |   F   F
   |
   +----------------------------→ Study Hours
       1   2   3   4   5   6

We want to separate:

F = Fail
P = Pass

SVM tries to find a decision boundary.

2. What is a decision boundary?

For two features, the boundary can be a line.

For example:

Attendance
   ↑
90 |                 P P
   |              P P
80 |           P
   |          /
70 |    F    /
   |  F    /
60 | F F  /
   |     /
   +----------------------→ Study Hours

The line separates:

Left side  → Fail
Right side → Pass

This is called the:

Decision boundary / Hyperplane

3. But there are many possible lines

This is where SVM becomes interesting.

Suppose we have:

F F F        |        P P P
F F          |        P P
F F F        |        P P P

We could draw many different lines:

        |             /
        |            /
        |           /

or:

       / 
      /
     /

or:

         |
         |
         |

Many lines could separate the classes.

So SVM asks:

Which separating line is the best?

The answer is:

The line with the maximum margin.

4. What is Margin?

This is the most important SVM concept.

Imagine:

Fail points

F F F        |        P P P
F F          |        P P
F F F        |        P P P
             ↑
        Decision boundary

The margin is the distance between the decision boundary and the closest points from each class.

Conceptually:

Fail             Boundary             Pass

 F F                 |                 P P
 F                   |                   P
                     |
<------ margin ------> <------ margin ------>

So:

Margin = distance from boundary to closest data points
	​

5. Maximum Margin

Now suppose we have two possible boundaries.

Boundary A
F F F    | P P P
         ↑
      small margin
Boundary B
F F F        |        P P P
             ↑
        larger margin

SVM chooses:

Boundary B
	​


because it has a larger margin.

That's why it's called:

Support Vector Machine with Maximum Margin

6. Why do we want a large margin?

Because we want the model to generalize to unseen data.

Suppose our boundary is extremely close to the training points:

F F F | P P P
      |

A small amount of noise could cause a new point to be classified incorrectly.

But with a large margin:

F F F       |       P P P

the boundary is more robust.

Think of the margin as a buffer zone.

Fail area | Buffer | Pass area

A larger buffer generally gives better separation.

7. What are Support Vectors?

Now we come to the name Support Vector Machine.

The points closest to the decision boundary are called:

Support Vectors

Example:

Fail points:

F   F   F
       F  ← Support Vector


             | ← Decision Boundary


       P     ← Support Vector
P   P   P

The support vectors are important because they determine the margin.

If you move a point far away:

F

            F

it may not change the boundary much.

But if you move a support vector:

       F ← important
             |
             | boundary

the optimal boundary can change significantly.

So:

Support Vectors determine the margin/boundary
	​

8. Maximum Margin mathematically

For a linear SVM, the decision boundary is:

w
T
x+b=0

For two-dimensional data:

w
1
	​

x
1
	​

+w
2
	​

x
2
	​

+b=0

The distance from a point to the boundary is related to:

∣∣w∣∣
∣w
T
x+b∣
	​


SVM wants to maximize the margin.

This is equivalent to minimizing:

2
1
	​

∣∣w∣∣
2

subject to the classification constraints.

You don't need to memorize the derivation yet. The intuition is:

Minimize model complexity
        ↓
while correctly separating classes
        ↓
Produces maximum margin
9. What if the data isn't linearly separable?

This is where the Kernel Trick comes in.

Consider this dataset:

            P P P
         P       P

       F   F F F   F

         P       P
            P P P

Suppose:

P = Pass
F = Fail

The Pass points form a circle around the Fail points.

Can we separate them with a straight line?

No.

Any straight line would cut through one of the classes.

       P P
     P  F  P
    P F F F P
     P  F  P
       P P

A straight line won't work.

10. What do we do?

We transform the data into a higher-dimensional space.

This is the basic intuition behind the:

Kernel Trick

Suppose our original features are:

x
1
	​

,x
2
	​


We can create another feature:

x
3
	​

=x
1
2
	​

+x
2
2
	​


Now the circular data can become easier to separate.

11. Visual intuition for the Kernel Trick

Originally:

2D space

        P P P
      P       P
     P   FFF   P
      P       P
        P P P

Not linearly separable.

Now imagine transforming it:

Original 2D
     ↓
Kernel transformation
     ↓
Higher-dimensional space
     ↓
Linear separation becomes possible

Conceptually:

Original space:

     P
   P   P
  P F F P
   P F P
     P

             ↓

Higher-dimensional space:

P P P P       ← one side

      |

      | boundary

      |

F F F F       ← other side

We don't necessarily calculate the transformed coordinates explicitly.

That's the clever part.

12. Why is it called the Kernel Trick?

Suppose we wanted to transform every point into a high-dimensional space.

That could become computationally expensive.

Instead, a kernel function calculates the similarity between points in a way that behaves as though the transformation had been performed.

Conceptually:

K(x
i
	​

,x
j
	​

)=ϕ(x
i
	​

)
T
ϕ(x
j
	​

)

Where:

x
i
	​

,x
j
	​

 = original points
ϕ(x) = transformation into higher-dimensional space
K = kernel function

The trick is:

We calculate the similarity directly without explicitly calculating the high-dimensional transformation.

That's the kernel trick.

13. Common kernels
Linear Kernel
K(x
i
	​

,x
j
	​

)=x
i
T
	​

x
j
	​


Used when the data is approximately linearly separable.

Polynomial Kernel
K(x
i
	​

,x
j
	​

)=(x
i
T
	​

x
j
	​

+c)
d

Can model polynomial relationships.

RBF / Gaussian Kernel

One of the most commonly used kernels:

K(x
i
	​

,x
j
	​

)=e
−γ∣∣x
i
	​

−x
j
	​

∣∣
2

This can create complex nonlinear decision boundaries.

14. RBF intuition

RBF essentially asks:

"How similar are these two points?"

If two points are close:

A ● ● B

high similarity.

If they are far apart:

A ●                    ● B

low similarity.

So the model can create nonlinear boundaries around groups of points.

15. Linear SVM vs Kernel SVM
Linear SVM
Data
 ↓
Straight line
 ↓
Class 0 | Class 1

Example:

F F F | P P P
      |
      boundary
Kernel SVM
Data
 ↓
Kernel
 ↓
Nonlinear boundary
 ↓
Complex separation

Example:

       P P P
     P       P
    P   F F   P
     P       P
       P P P

The boundary could be circular.

16. Soft Margin

Real-world data isn't always perfectly separable.

For example:

F F F
F F    P
       P P
   F   P

There may be some overlapping points.

SVM allows some points to be on the wrong side of the boundary.

This is called a:

Soft Margin

The parameter C controls the trade-off.

17. What does C mean?

Very roughly:

Large C
C = 100

The model strongly penalizes misclassification.

It tries very hard to classify training points correctly.

Potential problem:

Training accuracy ↑
Overfitting risk ↑
Small C
C = 0.1

The model allows more mistakes to obtain a wider margin.

Margin ↑
More training mistakes allowed
Potential generalization ↑

So:

C↑⇒fewer training errors, narrower margin
	​

C↓⇒more errors allowed, wider margin
	​

18. What does gamma mean for RBF?

For the RBF kernel, gamma controls how far the influence of a training point reaches.

Small gamma

A point has a broader influence:

       ●
   <--------->

The boundary tends to be smoother.

Large gamma

A point has a very local influence:

    ●
   <->

The boundary can become very complicated.

Therefore:

Small gamma
    ↓
Smooth boundary
    ↓
Potential underfitting

Large gamma
    ↓
Complex boundary
    ↓
Potential overfitting
19. Putting everything together

Here's the complete SVM picture:

                       SVM
                        |
            ┌───────────┴───────────┐
            ↓                       ↓
       Linear SVM              Kernel SVM
            ↓                       ↓
      Find boundary          Transform conceptually
            ↓                       ↓
      Maximum Margin         Higher-dimensional space
            ↓                       ↓
      Support Vectors        Find separation
                                    ↓
                             Nonlinear boundary
20. Compare with the algorithms you've learned

You've now learned several very different approaches.

Logistic Regression
Linear boundary
       ↓
Sigmoid
       ↓
Probability
Decision Tree
Feature
  ↓
Question
  ↓
Split
  ↓
Question
  ↓
Prediction
Random Forest
Many Decision Trees
        ↓
      Voting
XGBoost
Tree 1
  ↓
Correct errors
  ↓
Tree 2
  ↓
Correct errors
  ↓
Tree 3
SVM
Find boundary
      ↓
Maximize margin
      ↓
Support vectors
      ↓
Best separation

And when the data isn't linearly separable:

SVM
 ↓
Kernel Trick
 ↓
Higher-dimensional representation
 ↓
Nonlinear separation
The easiest way to remember SVM

Remember these four words:

Boundary → Margin → Support Vectors → Kernel

Boundary

Where do I separate the classes?

Margin

How far can I keep the boundary from the closest points?

Support Vectors

Which points determine that margin?

Kernel

What if a straight line cannot separate the data?

That gives you the core intuition of SVM maximum margin + kernel trick.'''



import numpy as np
class SVM:
    def __init__(self,learning_rate=0.001,lambda_param=0.01,n_iterations=1000):
        self.learning_rate=learning_rate
        self.lambda_param=lambda_param
        self.n_iterations=n_iterations

        self.weights=None
        self.bias=None
    def hinge_loss(self,y,scores):
        losses=np.maximum(0,1-y*scores)
        return np.mean(losses)
    def fit(self,X,y):
        X=np.array(X,dtype=float)
        y=np.array(y,dtype=float)
        n_samples=X.shape[0]
        n_features=X.shape[1]
        self.weights=np.zeros(n_features)
        self.bias=0.0
        print("="*50)
        print("TRAINING SVM")
        print("="*60)
        for itertaion in range(self.n_iterations):
            scores=(np.dot(X,self.weights)+self.bias)
            margin_condition=(y*scores<1)
            dw=(self.lambda_param*self.weights)
            if np.any(margin_condition):
                dw-=(np.dot(X[margin_condition].T,y[margin_condition])/n_samples)
            db=0
            if np.any(margin_condition):
                db=-np.sum(y[margin_condition])/n_samples
            self.weights-=(self.learning_rate*dw)
            self.bias-=(self.learning_rate*db)
            if (itertaion%100==0 or itertaion==self.n_iterations-1):
                hinge=self.hinge_loss(y,scores)
                regularization=(0.5*self.lambda_param*np.sum(self.weights**2))
                total_loss=hinge+regularization
                print(
                    f"Iteration "
                    f"{itertaion:4d} | "
                    f"Loss = "
                    f"{total_loss:.6f}"
                )


        print("\nTraining Complete!")

        print(
            "\nWeights:",
            self.weights
        )

        print(
            "Bias:",
            self.bias
        )
    def decision_function(self,X):
        X=np.array(X,dtype=float)
        scores=(np.dot(X,self.weights)+self.bias)
        return scores
    def predict(self,X):
        scores=self.decision_function(X)
        predictions=np.where(scores>=0,1,-1)
        return predictions
    def accuracy(Self,y_actual,y_predicted):
        return np.mean(y_actual==y_predicted)

if __name__ == "__main__":


    # ==========================================================
    # DATASET
    #
    # Feature 1 = Study Hours
    # Feature 2 = Attendance
    #
    # -1 = Fail
    # +1 = Pass
    # ==========================================================

    X = np.array([

        [1, 60],
        [2, 65],
        [2, 70],
        [3, 68],
        [3, 75],

        [4, 80],
        [5, 85],
        [5, 90],
        [6, 88],
        [6, 95]

    ])


    y = np.array([

        -1,
        -1,
        -1,
        -1,
        -1,

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

    model = SVM(

        learning_rate=0.001,

        lambda_param=0.01,

        n_iterations=1000

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

    print(
        "PREDICTIONS"
    )

    print("=" * 60)


    predictions = model.predict(
        X
    )


    scores = model.decision_function(
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

            f"Study Hours = "
            f"{X[i][0]}, "

            f"Attendance = "
            f"{X[i][1]}, "

            f"Score = "
            f"{scores[i]:.4f}, "

            f"Actual = "
            f"{y[i]}, "

            f"Predicted = "
            f"{predictions[i]} "

            f"→ {result}"

        )


    # ==========================================================
    # EVALUATION
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
    # TEST NEW STUDENTS
    # ==========================================================

    new_students = np.array([

        [2.5, 70],

        [4.5, 82],

        [3.0, 72],

        [5.5, 92]

    ])


    new_predictions = model.predict(
        new_students
    )


    new_scores = model.decision_function(
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
            f"{new_students[i][1]}, "

            f"Score = "
            f"{new_scores[i]:.4f} "

            f"→ {result}"

        )


