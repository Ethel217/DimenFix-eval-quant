## Quantitative Evaluation for DimenFix-t-SNE

### Datasets

Actual data files are not included.

| Dataset | Description | Classes | Instances | Dimensionality | Status |
|---------|------------|---------|-----------|---------------|----------|
| **MNIST (full)** | Images of handwritten digits | 10 | 70,000 | 784 |ready|
| **Iris**  | Flower features (sepal & petal measurements) | 3 | 150 | 4 |ready|
|**Image Segmentation**| Images | 7 | 2310|19 |ready|
|**Fashion MNIST**| Images ||||||||
|**Cell Type**| cells |-|||ready|
|**Brain Cells**| cells | - | | |ready|

### Metrics

Implemented in quantitative.py

| Metric | Description | Source | Status |
|---------|------------|---------|-----------|
|**Trustworthiness**|any unexpected nearest neighbors in the output space are penalised in proportion to their rank in the input space.|scikit-learn| ready|
|**Continuity**|Closest k-Neighbors Preservation|impl|ready|
|**Continuity Excluding Same Class**|k-Neighbors outside class|impl | ready|
|**Steadiness & Cohesiveness**| Inter-cluster distortion |||
|**Label-T&C**|

### Results

| Dataset | DimenFix | Comment| FileName | Trustworthiness | Continuity| Excl Continuity | Steadiness | Cohesiveness| Label-T| Label-C|
|----|-----|------|----|---|------|------|-----|------|----|----|
|**MNIST (full)**|disable|baseline| |
|**MNIST (full)**|fix class, random order|
|**MNIST (full)**|fix class, avg order|
|**Image Segmentation**|disable|baseline|base.bin|0.9972|0.7567|0.3449|0.9127|0.7217|
|**Image Segmentation**|fix class, clip, random order |k = 10|random_order.bin|0.9885|0.6686| 0.0534|0.7173|0.5424|
|**Image Segmentation**|fix class, clip, avg order ||avg_order.bin|0.9914|0.6806 | 0.1717| 0.6774| 0.6023|
|**Image Segmentation**|fix class, rescale, random order ||random_rescale.bin| 0.9927 | 0.7090| 0.0350| 0.6959| 0.5243|
|**Image Segmentation**|fix class, rescale, avg order ||avg_rescale.bin| 0.9954| 0.7149| 0.1104| 0.7116| 0.5559|
|**Image Segmentation**|fix row, rescale | 1000 iters| row_rescale.bin| 0.9754| 0.270| 0.2743| 0.5623| 0.7475|
|**Image Segmentation**|fix class, rescale, avg order, switched from fix row | 100 switching + 300 regular|row_class_avg_rescale_100_300.bin| 0.9944| 0.7031| 0.0972| 0.7564| 0.5492|
|**Cell Type**|disable| remove * dimensions|base.bin|0.9951| 0.5440|-|0.8880|0.7460|
|**Cell Type**|fix imputedY| remove * dimensions| imputedY.bin| 0.9300| 0.3060|-| 0.5983| 0.5338|
|**Cell Type**|fix subclass(GMCS), random order, rescale| | subclassGMCS_rescale_random.bin|0.9894|0.4978|TODO | 0.8575| 0.6783|
|**Cell Type**|fix subclass(GMCS), avg order, rescale| | subclassGMCS_rescale_avg.bin| 0.9864| 0.4951| TODO| 0.8355| 0.6379|
|**Brain Cells**|disable| remove xxx dimensions|
