# Deployment Instructions
## Technology Stack

- aws cli
- python3
- scanpy
- anndata
- umap
- numpy
- pandas
- scikit-learn

## Download dataset

1. **Download in this folder** :
	Run this AWS CLI shell in `/code`:

	```bash
	aws s3 sync s3://saturn-public-data/cancer-immunotherapy-challenge/data/ ./ --no-sign-request
	```

## Train and predict
1. **Run python shell and output** :
	Run python shell in `/code`:

	```bash
	python3 run.py
	```

	When print `Completed all`, the solutions were updated. 