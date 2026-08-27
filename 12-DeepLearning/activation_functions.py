'''What is an activation function?

An activation function decides what a neuron should output after calculating its weighted sum.

A neuron first calculates:

z=w
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

+⋯+w
n
	​

x
n
	​

+b

Then:

a=f(z)

where f is the activation function.

So:

Inputs
  ↓
Weighted sum
z = Wx + b
  ↓
Activation function
a = f(z)
  ↓
Output of neuron
Why do activation functions exist?

This is the most important question.

Without an activation function, a neural network would basically perform only linear operations.

Suppose we have:

z
1
	​

=W
1
	​

x+b
1
	​


and then another layer:

z
2
	​

=W
2
	​

z
1
	​

+b
2
	​


Substitute z
1
	​

:

z
2
	​

=W
2
	​

(W
1
	​

x+b
1
	​

)+b
2
	​


which becomes:

z
2
	​

=W
2
	​

W
1
	​

x+W
2
	​

b
1
	​

+b
2
	​


That's still just:

z
2
	​

=Wx+b

So stacking 10 linear layers without nonlinear activation is still essentially one linear transformation.

That's why activation functions exist:

They introduce non-linearity, allowing neural networks to learn complex patterns and functions such as XOR.

1. Sigmoid

The sigmoid function is:

σ(x)=
1+e
−x
1
	​


Its output is always between 0 and 1.

Add More
1
2
3
4
5
−1
−2
−3
−4
−5
1
2
3
4
−1
−2
−3
0,0
Give feedback

Roughly:

output
  1 |              ______
    |            /
0.5 |----------/
    |        /
  0 |_______/____________
             x
What does it do?

If:

z=10

sigmoid gives a value close to:

1

If:

z=−10

it gives a value close to:

0

If:

z=0

it gives:

0.5
Why was sigmoid useful?

It is useful when we want something that behaves like a probability.

For example:

P(spam)=0.92
Problem with sigmoid

For very large positive or negative values, the curve becomes almost flat.

That causes very small gradients.

This is called the vanishing gradient problem.

Therefore, sigmoid is generally not preferred for hidden layers of modern deep networks.

It is still very useful in the output layer for binary classification.

2. Tanh

Tanh is:

tanh(x)=
e
x
+e
−x
e
x
−e
−x
	​


Its output is between:

−1 and 1
Add More
1
2
3
4
5
−1
−2
−3
−4
−5
1
2
3
−1
−2
−3
0,0
Give feedback

Roughly:

output


  1 |             ______
    |           /
  0 |----------●----------
    |        /
 -1 |_______/
             x
Important difference from sigmoid

Sigmoid:

0→1

Tanh:

−1→1

And:

tanh(0)=0

So tanh is zero-centered, which can make optimization better than sigmoid in some settings.

Problem

Tanh can also suffer from vanishing gradients.

So it is less common than ReLU in modern deep networks.

3. ReLU

Now we get to one of the most important activation functions.

ReLU = Rectified Linear Unit

ReLU(x)=max(0,x)

It means:

If x<0:

ReLU(x)=0

If x>0:

ReLU(x)=x

So:

x < 0 → 0


x > 0 → x

Example:

x	ReLU(x)
-3	0
-1	0
0	0
2	2
5	5
Why is ReLU so popular?

Because it is simple and computationally cheap.

More importantly, for positive values it doesn't saturate like sigmoid/tanh.

For positive x:

ReLU
′
(x)=1

So gradients can flow more effectively through many layers.

That's one reason ReLU became extremely popular in deep learning.

ReLU's problem: Dead neurons

There's one important problem.

For:

x<0

ReLU outputs:

0

and its gradient is also 0 in that region.

A neuron can therefore become effectively inactive:

Input
 ↓
Negative values
 ↓
ReLU
 ↓
0
 ↓
No useful gradient

This is called the dying ReLU problem.

That's one motivation for newer activation functions.

4. GELU

GELU = Gaussian Error Linear Unit

Its formula is:

GELU(x)=xΦ(x)

where Φ(x) is the standard normal cumulative distribution function.

You don't need to memorize the complicated formula initially.

The intuition is much more important.

ReLU says:

"If x is positive, let it through; if negative, block it."

GELU is more gradual.

Instead of a hard cutoff:

ReLU:


negative → BLOCK
positive → PASS

GELU behaves more like:

very negative → mostly blocked
slightly negative → partially allowed
near zero → partially allowed
positive → increasingly allowed

So GELU provides a smooth nonlinear transformation.

GELU is especially associated with modern Transformer architectures.

5. SiLU

SiLU = Sigmoid Linear Unit

It is:

SiLU(x)=xσ(x)

Since:

σ(x)=
1+e
−x
1
	​


we can write:

SiLU(x)=
1+e
−x
x
	​


It is also commonly called Swish.

Add More
5
10
15
20
25
30
35
−5
−10
5
10
−5
−10
−15
−20
−25
0,0
Give feedback

The important idea:

SiLU smoothly scales the input using a sigmoid gate.

Instead of ReLU's sharp cutoff:

ReLU:


       /
      /
-----●

SiLU is smooth:

       /
     /
   /
__/

It can allow some negative values through rather than completely killing them.

6. So why do we have so many activation functions?

This is an excellent question.

Think about the evolution:

Sigmoid
Smooth
0 → 1

Good for probabilities, but can suffer from vanishing gradients.

↓

Tanh
Smooth
-1 → 1

Better zero-centered behavior, but still can have vanishing gradients.

↓

ReLU
max(0,x)

Simple, fast, and much better for deep networks.

But:

Dead ReLU problem

↓

GELU / SiLU
Smooth nonlinear functions

Designed to provide more gradual behavior and often work very well in modern neural networks.

7. Compare them visually
Add More
1
2
3
4
5
−1
−2
−3
−4
−5
1
2
3
4
−1
−2
−3
0,0
Give feedback

The key shapes to remember:

Function	Output	Main idea	Common use
Sigmoid	0 to 1	Probability-like output	Binary output layer
Tanh	-1 to 1	Zero-centered sigmoid-like function	Some older/specialized networks
ReLU	0 to ∞	Keep positive values	Very common hidden-layer activation
GELU	roughly -0.17 to ∞	Smooth gating	Transformers, modern networks
SiLU	roughly -0.28 to ∞	Smooth sigmoid gating	Modern deep networks
8. The biggest idea: non-linearity

Suppose we have:

Input
  ↓
Linear operation
  ↓
Linear operation
  ↓
Linear operation
  ↓
Output

Even though there are multiple layers, mathematically this can collapse into one linear operation.

So:

Multiple linear layers
        ↓
Still linear
        ↓
Cannot learn complex nonlinear relationships

But:

Linear
  ↓
ReLU
  ↓
Linear
  ↓
ReLU
  ↓
Linear

Now the network can learn nonlinear relationships.

That's the real reason activation functions exist.

9. Connection to XOR

Remember our XOR problem?

XOR:


1       0


0       1

A single linear boundary cannot separate it.

An MLP uses:

Linear transformation→Nonlinear activation→Linear transformation

This allows it to create a much more complex decision boundary.

So the chain is:

Perceptron

→ only linear decision boundary

MLP without activation

→ still effectively linear

MLP + nonlinear activation

→ can learn nonlinear patterns

→ XOR becomes possible.

⭐ What you should remember for your notes
Activation function

An activation function is a mathematical function applied to a neuron's weighted sum to introduce non-linearity into a neural network.

Why do we need it?

Without nonlinear activation functions, stacking multiple neural-network layers would still result in essentially a linear model, limiting the network's ability to learn complex patterns.

The five functions

Sigmoid

1+e
−x
1
	​


→ 0 to 1
→ useful for binary probability output
→ vanishing gradient issue

Tanh

tanh(x)

→ -1 to 1
→ zero-centered
→ can have vanishing gradients

ReLU

max(0,x)

→ simple and fast
→ very common
→ dying ReLU problem

GELU

xΦ(x)

→ smooth gating
→ widely used in modern Transformer architectures

SiLU

xσ(x)

→ smooth gating
→ used in many modern deep-learning architectures

One sentence to memorize:

Activation functions introduce non-linearity, allowing neural networks to learn complex relationships that a purely linear model cannot represent.'''