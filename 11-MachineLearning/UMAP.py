'''UMAP — explained from scratch

UMAP stands for Uniform Manifold Approximation and Projection.

It is a nonlinear dimensionality-reduction technique, similar to t-SNE.

The simplest way to understand it is:

UMAP takes high-dimensional data and creates a lower-dimensional representation, usually 2D or 3D, while trying to preserve which points are close to each other.

It is especially useful for visualizing complex, high-dimensional data.

1. Start with a real-world example

Imagine you work with images.

Each image is represented by:

Image
 ↓
784 features

For example, a 28 × 28 grayscale image has:

28×28=784

pixel values.

So you have:

10,000 images
      ↓
Each image has 784 features

You can't easily visualize 784 dimensions.

UMAP can transform:

784 dimensions
       ↓
      UMAP
       ↓
2 dimensions

Now you can plot the result.

2. What does UMAP try to preserve?

Suppose in the original 784-dimensional space:

Image A
Image B

are very similar.

UMAP tries to put them close together in the 2D representation:

● A
 ● B

If another image is very different:

● A ● B






                       ● C

So the main idea is:

Similar points should generally remain near each other.

This is called preserving local neighborhood structure.

3. Why is UMAP called nonlinear?

Some datasets have complicated structures that cannot be represented well using a simple straight-line transformation.

For example:

        ● ● ●
      ●       ●
     ●         ●
      ●       ●
        ● ● ●

The structure is curved.

Linear techniques such as PCA may not capture this structure well.

UMAP can learn a nonlinear representation.

So:

PCA
 ↓
Linear transformation


UMAP
 ↓
Nonlinear transformation
4. PCA vs UMAP

This is very important.

PCA asks:

"What directions contain the most variance?"

100 features
     ↓
    PCA
     ↓
20 components
UMAP asks more like:

"Which observations are neighbors, and how can I represent those relationships in fewer dimensions?"

100 features
     ↓
   UMAP
     ↓
2D representation

So:

PCA → variance


UMAP → neighborhood structure
5. UMAP vs t-SNE

These two are often confused.

Both are useful for visualization.

t-SNE

Strongly focuses on:

Local neighborhoods

UMAP

Also focuses strongly on local neighborhoods, but often preserves more global structure than t-SNE.

Think:

t-SNE
Local structure ⭐⭐⭐⭐⭐
Global structure ⭐⭐




UMAP
Local structure ⭐⭐⭐⭐⭐
Global structure ⭐⭐⭐⭐

This is an intuition, not a strict guarantee.

6. A visual example

Suppose your high-dimensional data contains three groups:

Original high-dimensional data


Group A
● ● ● ●


Group B
          ● ● ● ●


Group C
                    ● ● ● ●

UMAP may produce:

                Group A
                 ● ●
                ● ● ●




         Group B
          ● ● ●
         ● ● ●




                         Group C
                          ● ● ●
                         ● ●

You can now visually inspect:

Are there groups?
Are groups overlapping?
Are there outliers?
Are classes mixed together?
Are there continuous transitions?
7. Real-world example: customer segmentation

Suppose an e-commerce company has:

100,000 customers

and for each customer:

Age
Income
Purchases
Browsing history
Products viewed
Time spent
Categories
...

Maybe you have:

200 features

You want to understand whether customers naturally form groups.

You can do:

200 features
      ↓
    UMAP
      ↓
2 dimensions
      ↓
Visualization

You might see:

              ● ● ●
            ● ● ● ●
             ● ●




                          ● ● ●
                        ● ● ● ●
                         ● ●




        ● ● ●
       ● ● ●

Now you can investigate:

Cluster 1 → Frequent buyers
Cluster 2 → Occasional buyers
Cluster 3 → New customers

But remember:

UMAP itself did not create these business labels.

You interpret the patterns using the original features and domain knowledge.

8. UMAP for image embeddings

This is a very useful real-world application.

Suppose a neural network creates:

Image
 ↓
Neural Network
 ↓
512-dimensional embedding

You have:

100,000 images

Each image:

512 dimensions

Use UMAP:

512D embeddings
       ↓
      UMAP
       ↓
2D

Then visualize.

You might see:

Cars              Dogs


● ● ●             ● ● ●
● ● ●             ● ● ●
 ● ●               ● ●




        Cats


       ● ● ●
      ● ● ●

This can help determine whether your neural network's embeddings contain meaningful structure.

9. UMAP for NLP

Suppose you have text embeddings:

"cat"
"dog"
"lion"
"car"
"truck"
"bus"

Each could be represented by hundreds of dimensions.

For example:

Text
 ↓
Embedding model
 ↓
768 dimensions

Then:

768D
 ↓
UMAP
 ↓
2D

You might see:

Animals


● cat
● dog
● lion




Vehicles


● car
● truck
● bus

This can help you explore the embedding space.

10. Is UMAP a machine-learning model?

This is a subtle point.

UMAP is an unsupervised dimensionality-reduction algorithm.

But it is not usually what we mean when we say:

"Train a model to predict the target."

For example:

Logistic Regression
     ↓
Predict Pass/Fail

while:

UMAP
 ↓
Create lower-dimensional representation

So UMAP is more like a representation/transformation technique.

11. Can UMAP be used before a model?
Yes, sometimes.

For example:

1000 features
     ↓
UMAP
     ↓
50 dimensions
     ↓
Classifier

But you shouldn't automatically assume this improves the model.

You must compare:

Model A:
Original features
       ↓
Classifier
       ↓
Performance




Model B:
UMAP features
       ↓
Classifier
       ↓
Performance

If UMAP improves validation performance and is appropriate for your use case, it may be useful.

But for a general-purpose, stable preprocessing transformation, PCA is often the first technique I'd try.

12. Why isn't UMAP always used before models?

Because dimensionality reduction can remove information that your prediction model needs.

Imagine:

Original data
100 features

UMAP:

100 features
 ↓
2 features

You may preserve useful neighborhood structure but lose information that matters for predicting your target.

Therefore:

A beautiful UMAP plot does not mean you have a good predictive representation.

This is extremely important.

13. UMAP for visualization vs UMAP for prediction
Visualization

Very common:

High-dimensional data
       ↓
      UMAP
       ↓
      2D
       ↓
      Plot
Prediction

Possible:

High-dimensional data
       ↓
      UMAP
       ↓
Reduced features
       ↓
Classifier

But you must validate it.

14. UMAP parameters

Two important parameters you'll encounter are:

n_neighbors

This controls how many neighboring points UMAP considers when learning the structure.

Think:

Small n_neighbors
       ↓
Focus more on local structure


Large n_neighbors
       ↓
Consider broader structure

For example:

UMAP(n_neighbors=15)
min_dist

This controls how tightly points can be packed together in the low-dimensional representation.

Conceptually:

Small min_dist
      ↓
Clusters can appear more tightly packed




Large min_dist
      ↓
Points are encouraged to remain more spread out

Example:

UMAP(
    n_neighbors=15,
    min_dist=0.1
)
15. Don't confuse n_neighbors with K

If you learned KNN and K-Means:

KNN:
K = number of neighbors


K-Means:
K = number of clusters

UMAP:

n_neighbors
=
size of the neighborhood used to learn the manifold structure

It does not mean:

Number of clusters.

16. What is "manifold"?

You'll often hear this word with UMAP.

A simple intuition:

A manifold is a lower-dimensional structure hidden inside a higher-dimensional space.

Imagine a sheet of paper:

2D sheet

Now bend it:

        ______
      /
     /
____/

The sheet is still fundamentally 2D even though it is sitting inside 3D space.

Similarly, your data may have:

100 dimensions

but the meaningful structure might lie on a much lower-dimensional shape.

UMAP tries to uncover and represent that structure.

You don't need the advanced mathematical definition initially.

17. UMAP vs PCA vs t-SNE

This is the table I'd recommend remembering:

	PCA	t-SNE	UMAP
Linear?	Yes	No	No
Main goal	Compression/reduction	Visualization	Visualization/reduction
Focus	Variance	Local structure	Local + broader structure
2D visualization	Yes	Excellent	Excellent
Can be used as preprocessing	Yes	Less common	Sometimes
New-data transformation	Yes	Traditionally less straightforward	Yes
Handles nonlinear structure	No	Yes	Yes
Usually fast	Yes	Often slower	Often faster than t-SNE
18. When should I choose UMAP?

Use UMAP when you have a question like:

"I have high-dimensional data and I want to understand its structure."

Examples:

Image embeddings
       ↓
      UMAP
       ↓
Visualize




Text embeddings
       ↓
      UMAP
       ↓
Visualize




Gene-expression data
       ↓
      UMAP
       ↓
Explore groups
19. When should I choose PCA instead?

Use PCA when your goal is more like:

"I have many features and want a compact representation that captures as much variance as possible."

For example:

500 features
      ↓
PCA
      ↓
50 components
      ↓
Machine learning model

PCA is often the first thing I'd try for linear dimensionality reduction.

20. When should I choose t-SNE?

Use t-SNE when your main question is:

"What do the local neighborhoods of my high-dimensional data look like?"

For example:

Image embeddings
       ↓
     t-SNE
       ↓
     2D plot

It's excellent for exploratory visualization, but the visualization can be sensitive to parameters and should not be over-interpreted.

21. UMAP in a real ML project

Imagine you're building an image classifier.

You have:

100,000 images

Your neural network produces:

512-dimensional embeddings

You want to investigate the embeddings.

Your workflow:

                Images
                   ↓
             Neural Network
                   ↓
           512D embeddings
                   ↓
                 UMAP
                   ↓
                  2D
                   ↓
                Plot
                   ↓
       ┌───────────┼───────────┐
       ↓           ↓           ↓
    Similar      Mixed       Outliers
    groups       classes

This can help you understand:

whether embeddings separate classes
whether classes overlap
whether there are unusual samples
whether there are potentially meaningful subgroups

Then you still evaluate the actual classifier using appropriate metrics.'''