'''PCA — Principal Component Analysis

PCA is a dimensionality reduction technique.

Its main purpose is:

Take many related features and represent them using fewer new features while preserving as much important variation/information as possible.

The most important thing to understand is that PCA does not simply select existing columns.

It creates new features called Principal Components.

1. Start with a real-world problem

Imagine a company has data about customers.

They have 5 features:

Customer	Age	Income	Spending	Purchases	Visits
A	22	30	40	5	8
B	25	35	45	6	9
C	28	40	50	8	10
D	45	80	85	25	30
E	50	90	90	30	35

We have:

5 features

But suppose we have a much larger dataset:

10,000 customers
100 features

Now we have a problem.

Some features may contain very similar information.

For example:

Income
Purchases
Spending

might be strongly related.

So instead of giving the model all 100 features, we may want something like:

100 features
      ↓
     PCA
      ↓
10 principal components

That's dimensionality reduction.

2. But what exactly does PCA do?

This is the key idea.

Suppose we have only two features:

X1 = Study Hours
X2 = Exam Preparation

Imagine the data looks like this:

Exam Preparation
       ↑
       |
       |              ●
       |            ●
       |          ●
       |        ●
       |      ●
       |    ●
       |  ●
       +----------------------→ Study Hours

Notice something?

As study hours increase, exam preparation also tends to increase.

The data has a strong diagonal direction.

PCA looks at the data and says:

"Most of the variation is happening along this diagonal direction."

That becomes:

Principal Component 1 (PC1)
3. PCA creates a new coordinate system

Originally:

Feature 1
Feature 2

After PCA:

PC1
PC2

The important thing is:

PC1 and PC2 are not the original features.

They are combinations of the original features.

For example, conceptually:

PC1=0.7X
1
	​

+0.7X
2
	​


and:

PC2=0.7X
1
	​

−0.7X
2
	​


The actual numbers are calculated from the data.

So PCA is basically rotating the coordinate system to find better directions.

4. What does "better direction" mean?

PCA asks:

Which direction captures the maximum variance in the data?

Variance means, roughly:

How much the data varies/spreads in a particular direction.

Imagine:

             ●
          ●
       ●
    ●
 ●

There is a lot of variation along this diagonal.

But very little variation perpendicular to it.

So PCA says:

PC1 → captures lots of variation
PC2 → captures very little variation

Therefore, maybe we can remove PC2.

Instead of:

2 dimensions

we keep:

1 dimension

while retaining most of the important variation.

5. Simple numerical example

Suppose PCA produces:

Component	Explained Variance
PC1	85%
PC2	15%

That means:

PC1 → 85%
PC2 → 15%

If we keep only PC1:

Original:


X1
X2


      ↓ PCA


PC1

We reduced:

2D→1D

while retaining approximately:

85%

of the variance.

6. Now imagine 100 features

Suppose you have:

100 features

PCA might produce:

PC1 → 30%
PC2 → 20%
PC3 → 12%
PC4 → 8%
PC5 → 5%
...

Maybe the first 20 components contain:

95% of the variance

Then you could do:

100 features
      ↓
     PCA
      ↓
20 components
      ↓
95% variance retained

This is the real power of PCA.

7. Important: PCA doesn't just delete columns

This is a common misunderstanding.

Suppose your original features are:

Age
Income
Spending
Purchases
Visits

PCA does not necessarily say:

Keep:
Age
Income


Delete:
Spending
Purchases
Visits

Instead it creates:

PC1
PC2
PC3
...

For example, conceptually:

PC1=0.1(Age)+0.5(Income)+0.6(Spending)+0.4(Purchases)+0.4(Visits)

So PC1 is a weighted combination of the original features.

8. Why would we want this?

There are several real-world reasons.

Reason 1 — Too many features

Imagine:

1,000 features

Your model might become:

More computationally expensive
More difficult to visualize
Potentially more difficult to model

PCA can reduce:

1,000 features
       ↓
50 components
9. Real-world example: image recognition

This is a classic example.

Suppose you have an image:

28 × 28 pixels

That's:

28×28=784

features if each pixel is represented as a feature.

So:

One image
 ↓
784 features

Suppose you have:

100,000 images

That's a huge feature space.

You could investigate whether PCA can compress the representation:

784 pixel features
       ↓
      PCA
       ↓
50 components

Now you have:

784 → 50

while retaining a chosen amount of variance.

This can reduce computational cost for some downstream models.

10. Real-world example: finance

Suppose a bank tracks:

Interest rate
Inflation
GDP
Unemployment
Stock prices
Currency rates
Bond prices
...

There may be many correlated variables.

For example:

Interest rate
Bond price
Inflation
GDP

can have relationships.

Instead of using dozens or hundreds of correlated variables, PCA can identify a smaller set of directions representing major patterns in the data.

For example:

50 financial indicators
        ↓
       PCA
        ↓
5 components

The components might capture broad patterns such as:

PC1 → overall market movement
PC2 → inflation-related variation
PC3 → interest-rate-related variation
...

Those labels are interpretations we give afterward; PCA itself only gives mathematical components.

11. Real-world example: medical data

Imagine a medical dataset with:

Blood pressure
Heart rate
Cholesterol
BMI
Blood glucose
...

Some variables may be correlated.

Suppose there are:

100 measurements

PCA could transform them into:

100 features
      ↓
     PCA
      ↓
10 components

Researchers can then explore whether the major patterns in the measurements can be represented using fewer dimensions.

For actual medical decision-making, PCA would need careful validation and shouldn't be assumed to preserve clinically important information merely because it preserves statistical variance.

12. PCA for visualization

This is another very common use.

Suppose your dataset has:

50 features

You can't easily visualize 50 dimensions.

So:

50 features
     ↓
PCA
     ↓
2 components
     ↓
X-axis = PC1
Y-axis = PC2

Then you can plot:

PC2
 ↑
 |
 |      ● ● ●
 |    ● ● ●
 |
 |                   ● ●
 |                 ● ● ●
 +--------------------------→ PC1

This can help you visually investigate whether groups or patterns exist.

13. PCA before machine learning

Suppose you're building a classification model.

Your dataset has:

500 features

You might try:

Original data
     ↓
500 features
     ↓
PCA
     ↓
50 components
     ↓
Logistic Regression
     ↓
Prediction

Why?

Because PCA may reduce redundancy and the dimensionality of the input.

But there is an important point:

PCA isn't automatically better.

You should compare model performance with and without PCA using proper validation.

14. PCA and feature scaling

This is extremely important.

Suppose you have:

Age:       20–60
Income:    20,000–200,000

PCA is based on variance/covariance, so a feature with a much larger numerical scale can dominate.

Therefore, a common workflow is:

Raw Data
   ↓
Standardization
   ↓
PCA
   ↓
Machine Learning Model

For example:

z=
σ
x−μ
	​


This puts features on comparable scales.

15. How PCA works internally

You don't need to memorize every equation yet, but understand the flow.

Original Data
      ↓
Standardize / center
      ↓
Calculate covariance structure
      ↓
Find directions of maximum variance
      ↓
Find principal components
      ↓
Rank components
      ↓
Select top components
      ↓
Transform original data

Mathematically, PCA is commonly implemented using Singular Value Decomposition (SVD).

You may also learn it through the covariance matrix and its eigenvectors/eigenvalues.

16. What are eigenvectors and eigenvalues doing here?

At a high level:

Eigenvectors

Tell PCA:

Which directions should I look at?

Eigenvalues

Tell PCA:

How much variance/information is captured in each direction?

For example:

Eigenvector 1 → direction of PC1
Eigenvalue 1 → amount of variance in PC1


Eigenvector 2 → direction of PC2
Eigenvalue 2 → amount of variance in PC2

Then PCA sorts the components by their explained variance.

17. How do we choose the number of components?

Suppose you have:

100 features

and PCA gives:

PC1 → 40%
PC2 → 25%
PC3 → 15%
PC4 → 8%
PC5 → 5%
...

Cumulative:

PC1                 40%
PC1 + PC2           65%
PC1 + PC2 + PC3     80%
PC1 + ... + PC4     88%
PC1 + ... + PC5     93%

If you decide to retain around 90–95% variance, you might choose:

5 components

So:

100 features
    ↓
PCA
    ↓
5 components
18. One important limitation

PCA maximizes variance, not necessarily predictive usefulness.

Suppose:

Feature A → huge variance but unrelated to target


Feature B → small variance but extremely useful for prediction

PCA may prioritize Feature A's direction.

Therefore:

High explained variance does not automatically mean better prediction.

This is why you should evaluate your downstream model.

19. PCA vs selecting the best features

These are different.

Feature selection

You keep original features:

100 features
   ↓
Select
   ↓
10 original features
PCA

You create new features:

100 features
   ↓
PCA
   ↓
10 new components

This distinction is very important.

20. PCA in one real-world workflow

Let's say you're working for an e-commerce company.

You have:

1 million customers


200 features

Some features are correlated.

Your workflow could be:

Customer Data
      ↓
Clean missing values
      ↓
Scale numerical features
      ↓
PCA
      ↓
200 features
      ↓
30 components
      ↓
Train model
      ↓
Evaluate

Then compare:

Model without PCA
       VS
Model with PCA

For example:

Without PCA
Accuracy = 89%


With PCA
Accuracy = 90%

PCA might be useful.

But if:

Without PCA
Accuracy = 91%


With PCA
Accuracy = 84%

then PCA may be hurting your predictive performance, and you shouldn't use it just because it reduces dimensions.

21. The easiest way to remember PCA

Think of a photograph.

You have a huge image containing lots of information.

You want to compress it while keeping the most important patterns.

PCA essentially says:

"Which directions in this data contain the most variation? Let's keep those directions and discard directions that contribute relatively little variance."

So:

100 features
      ↓
       PCA
      ↓
PC1 ─────────────── Most information
PC2 ───────────
PC3 ───────
PC4 ───
PC5 ──
...
      ↓
Keep first few
      ↓
Reduced dataset
22. PCA vs the models you've learned

PCA is not really a prediction algorithm like:

Linear Regression
Logistic Regression
Decision Tree
Random Forest
XGBoost
SVM
KNN

Instead, think of PCA as a preprocessing/transformation technique:

                 Data
                   ↓
              Standardize
                   ↓
                  PCA
                   ↓
          Reduced representation
                   ↓
        ┌──────────┼──────────┐
        ↓          ↓          ↓
    Logistic      SVM       KNN
   Regression
23. Interview answer

If an interviewer asks:

"What is PCA?"

You can say:

PCA, or Principal Component Analysis, is a dimensionality reduction technique that transforms correlated features into a smaller number of new, uncorrelated features called principal components. The first component captures the maximum possible variance, the second captures the maximum remaining variance subject to being orthogonal to the first, and so on. We use PCA for dimensionality reduction, visualization, compression, and sometimes as preprocessing before machine learning models.'''

import numpy as np
class PCA:

      def __init__(self,n_components):
        
        self.n_components=n_components
        self.components=None
        self.mean=None
        self.explained_variance_ratio=None
      def fit(self,X):
          self.mean=np.mean(X,axis=0)
          X_centered=X-self.mean
          cov_matrix=np.cov(X_centered,rowvar=False)
          eigenvalues,eigenvectors=np.linalg.eigh(cov_matrix)
          sorted_indices=np.argsort(eigenvalues)[::-1]
          sorted_eigenvalues=eigenvalues[sorted_indices]
          sorted_eigenvectors=eigenvectors[:,sorted_indices]
          self.components=sorted_eigenvectors[:,:self.n_components]
          total_variance=np.sum(sorted_eigenvalues)
          self.explained_variance_ratio=sorted_eigenvalues[:self.n_components]/total_variance

      def transform(self,X):
          X_centered=X-self.mean
          return np.dot(X_centered,self.components)
      def fit_transform(self,X):
          self.fit(X)
          return self.transform(X)
if __name__ == "__main__":
    # Generate random synthetic dataset (100 samples, 4 features)
    np.random.seed(42)
    X = np.random.randn(100, 4)

    # Instantiate and run PCA from scratch (reduce from 4D -> 2D)
    pca = PCA(n_components=2)
    X_projected = pca.fit_transform(X)

    print("Original Data Shape: ", X.shape)
    print("Projected Data Shape:", X_projected.shape)
    print("Explained Variance Ratio per Component:", pca.explained_variance_ratio)
        
