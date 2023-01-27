## Algorithm Description
### Overview
I'm a newer to this machine learning and biology challenge, and have enjoyed to participate and learn a lot.
For me, this challenge one may simply split into two parts:
1. One perturbation condition leads to a cell gene expression.
2. A cell gene expression represents a cell state.

### Part one
How to get the cell gene expression for one perturbation condition?
I thought many ways, but one way is convenient for me to implement, and by which I just want to start to learn to run success first in this challenge. There may be a relevance between genes, which I use a "distance" to metric them, but that were still not familiar to me now, and I just suppose that the perturbation condition gene would be zero, and others would be the distance value. So the simple implement would be to calculate the mean of every gene differencies in every cell.
Eventually, I would get the gene expression vector.

### Part two
How to predict the state?
If I get the predict gene expression vector, I could just predict the state by classfier, for we know every cell's gene expression and its state, so I used the poly classfier to train, but my environment is bad and not wait so long, just want to run success first, so the parament `max_iter` used just 10.
So I could get the predict output now. That's my simple try for this, Thx.