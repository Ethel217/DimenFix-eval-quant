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
|**Image Segmentation**|fix row, rescale | 700 iters| row_rescale.bin| 0.9754| 0.270| 0.2743| 0.5623| 0.7475|
|**Image Segmentation**|fix col, rescale | 700 iters| col_rescale.bin| -| -| -| -| -|
|**Image Segmentation**|fix class, rescale, avg order, switched from fix row | 100 switching + 300 regular|row_class_avg_rescale_100_300.bin| 0.9944| 0.7031| 0.0972| 0.7564| 0.5492|
|**Cell Type**|disable| remove * dimensions|base.bin|0.9951| 0.5440|-|0.8880|0.7460|
|**Cell Type**|fix imputedY| remove * dimensions| imputedY.bin| 0.9300| 0.3060|-| 0.5983| 0.5338|
|**Cell Type**|fix subclass(GMCS), random order, rescale| | subclassGMCS_rescale_random.bin|0.9877|0.5160|TODO | 0.8478| 0.6415|
|**Cell Type**|fix subclass(GMCS), avg order, rescale| | subclassGMCS_rescale_avg.bin| 0.9907| 0.5213| TODO| 0.8664| 0.7001|
|**Brain Cells**|disable| remove unassigned dimensions| not suitable for metric eval|


input init: input dataset will be set null when restart

700 iters, image segmentation

| File Name                           | Continuity | Trustworthiness | OutContin  | Steadiness | Cohesiveness |
|-------------------------------------|------------|----------------|------------|------------|--------------|
| avg_order_220.bin                  | 0.6981     | 0.9853         | 0.1103     | 0.7513     | 0.5437       |
| avg_rescale_220.bin                | 0.7058     | 0.9886         | 0.1138     | 0.7177     | 0.5695       |
| base_220.bin                        | 0.7564     | 0.9958         | 0.3449     | 0.9085     | 0.7581       |
| col_class_avg_rescale_220.bin       | 0.7106     | 0.9935         | 0.1095     | 0.7626     | 0.5861       |
| col_rescale_220.bin                 | 0.5532     | 0.9819         | 0.2952     | 0.6343     | 0.7415       |
| random_order_220_0.bin              | 0.6846     | 0.9867         | 0.0626     | 0.6355     | 0.4988       |
| random_order_220_1.bin              | 0.6914     | 0.9839         | 0.0666     | 0.6795     | 0.4823       |
| random_order_220_2.bin              | 0.6667     | 0.9866         | 0.0268     | 0.6334     | 0.5388       |
| random_order_220_3.bin              | 0.6987     | 0.9891         | 0.1074     | 0.7561     | 0.5463       |
| random_order_220_4.bin              | 0.6629     | 0.9872         | 0.0963     | 0.7203     | 0.5502       |
| random_rescale_220_1.bin            | 0.7110     | 0.9883         | 0.0888     | 0.7582     | 0.5867       |
| random_rescale_220_2.bin            | 0.7135     | 0.9901         | 0.0718     | 0.7432     | 0.5240       |
| random_rescale_220_3.bin            | 0.7168     | 0.9908         | 0.0757     | 0.7111     | 0.5774       |
| random_rescale_220_4.bin            | 0.7219     | 0.9905         | 0.0358     | 0.7606     | 0.5326       |
| random_rescale_220_5.bin            | 0.7150     | 0.9890         | 0.0764     | 0.7116     | 0.5726       |
| row_class_avg_rescale_220.bin       | 0.7058     | 0.9885         | 0.0639     | 0.6442     | 0.5330       |
| row_rescale_220.bin                 | 0.5192     | 0.9701         | 0.2417     | 0.5934     | 0.7327       |

| File Name                           | Continuity | Trustworthiness | OutContin  | Steadiness | Cohesiveness |
|-------------------------------------|------------|----------------|------------|------------|--------------|
| avg_order_42.bin                   | 0.7022     | 0.9856         | 0.1618     | 0.6898     | 0.6440       |
| avg_rescale_42.bin                 | 0.7075     | 0.9893         | 0.1478     | 0.7618     | 0.6242       |
| base_42.bin                         | 0.7570     | 0.9961         | 0.3394     | 0.9125     | 0.7790       |
| col_class_avg_rescale_42.bin        | 0.7074     | 0.9920         | 0.1137     | 0.7362     | 0.5367       |
| col_rescale_42.bin                  | 0.5547     | 0.9864         | 0.2949     | 0.7029     | 0.8485       |
| random_order_42_1.bin               | 0.7057     | 0.9873         | 0.1996     | 0.7552     | 0.5786       |
| random_order_42_2.bin               | 0.6797     | 0.9885         | 0.0858     | 0.7163     | 0.5271       |
| random_order_42_3.bin               | 0.6762     | 0.9869         | 0.1416     | 0.7140     | 0.5519       |
| random_order_42_4.bin               | 0.6832     | 0.9799         | 0.0674     | 0.6456     | 0.4974       |
| random_order_42_5.bin               | 0.6821     | 0.9835         | 0.0588     | 0.6662     | 0.5396       |
| random_rescale_42_1.bin             | 0.7204     | 0.9899         | 0.1308     | 0.7174     | 0.5368       |
| random_rescale_42_2.bin             | 0.7218     | 0.9926         | 0.1079     | 0.7603     | 0.5184       |
| random_rescale_42_3.bin             | 0.7183     | 0.9920         | 0.0734     | 0.7727     | 0.5171       |
| random_rescale_42_4.bin             | 0.7098     | 0.9887         | 0.0934     | 0.7261     | 0.5370       |
| random_rescale_42_5.bin             | 0.7185     | 0.9919         | 0.0506     | 0.7049     | 0.4918       |
| row_class_avg_rescale_42.bin        | 0.7061     | 0.9878         | 0.0945     | 0.7450     | 0.5230       |
| row_rescale_42.bin                  | 0.5148     | 0.9658         | 0.2302     | 0.5452     | 0.7298       |


| Model                                | Continuity | Trustworthiness | OutContin | Steadiness | Cohesiveness |
|--------------------------------------|------------|----------------|------------|------------|--------------|
| avg_order_-695.bin                  | 0.6977     | 0.9890         | 0.1486     | 0.7527     | 0.5856       |
| avg_rescale_-695.bin                 | 0.6877     | 0.9850         | 0.1146     | 0.6493     | 0.5798       |
| base_-695.bin                        | 0.7569     | 0.9966         | 0.3558     | 0.9125     | 0.7440       |
| col_class_avg_rescale_-695.bin       | 0.7102     | 0.9889         | 0.0736     | 0.7557     | 0.5579       |
| col_rescale_-695.bin                 | 0.5416     | 0.9793         | 0.2746     | 0.6151     | 0.7767       |
| random_order_-695_1.bin              | 0.6745     | 0.9849         | 0.1250     | 0.7345     | 0.5921       |
| random_order_-695_2.bin              | 0.6923     | 0.9882         | 0.1310     | 0.7716     | 0.5518       |
| random_order_-695_3.bin              | 0.6852     | 0.9831         | 0.0755     | 0.7141     | 0.5405       |
| random_order_-695_4.bin              | 0.6695     | 0.9821         | 0.1552     | 0.7173     | 0.6053       |
| random_order_-695_5.bin              | 0.7015     | 0.9880         | 0.1102     | 0.7514     | 0.5397       |
| random_rescale_-695_1.bin            | 0.7152     | 0.9912         | 0.0867     | 0.7777     | 0.5358       |
| random_rescale_-695_2.bin            | 0.7204     | 0.9909         | 0.0393     | 0.7748     | 0.5262       |
| random_rescale_-695_3.bin            | 0.7116     | 0.9883         | 0.0556     | 0.7354     | 0.5102       |
| random_rescale_-695_4.bin            | 0.7145     | 0.9885         | 0.0528     | 0.7446     | 0.5226       |
| random_rescale_-695_5.bin            | 0.7161     | 0.9879         | 0.1005     | 0.7491     | 0.5358       |
| row_class_avg_rescale_-695.bin       | 0.7119     | 0.9876         | 0.1159     | 0.7089     | 0.5408       |
| row_rescale_-695.bin                 | 0.5186     | 0.9635         | 0.2711     | 0.5361     | 0.7541       |


500 iters, Iris, fix sepal_length, perplexity 30 (TODO: might cause trouble...), push every 20
clipping mode is set to exact clip, overlap = 0

| Filename                   | Continuity | Trustworthiness | OutContin | Steadiness | Cohesiveness |
|---------------------------|------------|------------------|-----------|------------|---------------|
| avg_clip_493.bin          | 0.6953     | 0.9797           | 0.4820    | 0.9264     | 0.7074        |
| base_493.bin              | 0.7680     | 0.9897           | 0.5227    | 0.9229     | 0.7872        |
| clip_0_sepal_493.bin      | 0.6920     | 0.9809           | 0.5127    | 0.9014     | 0.8025        |
| disable_order_clip_493.bin| 0.7327     | 0.9841           | 0.7467    | 0.9364     | 0.7546        |
| random_rescale_493.bin    | 0.7567     | 0.9870           | 0.5107    | 0.9331     | 0.7515        |
| rescale_avg_493.bin       | 0.7607     | 0.9889           | 0.3787    | 0.9212     | 0.7721        |

| Filename                   | Continuity | Trustworthiness | OutContin | Steadiness | Cohesiveness |
|---------------------------|------------|------------------|-----------|------------|---------------|
| avg_clip_702.bin          | 0.7027     | 0.9811           | 0.4913    | 0.9287     | 0.6932        |
| base_702.bin              | 0.7680     | 0.9883           | 0.5220    | 0.9438     | 0.7513        |
| clip_0_sepal_702.bin      | 0.6753     | 0.9788           | 0.5233    | 0.8874     | 0.7911        |
| disable_order_clip_702.bin| 0.7500     | 0.9857           | 0.5107    | 0.9471     | 0.7695        |
| random_rescale_702.bin    | 0.7567     | 0.9856           | 0.5007    | 0.9378     | 0.7875        |
| rescale_avg_702.bin       | 0.7213     | 0.9808           | 0.3567    | 0.9289     | 0.7776        |

| Filename                   | Continuity | Trustworthiness | OutContin | Steadiness | Cohesiveness |
|---------------------------|------------|------------------|-----------|------------|---------------|
| avg_clip_931.bin          | 0.7020     | 0.9813           | 0.4773    | 0.9179     | 0.6621        |
| base_931.bin              | 0.7807     | 0.9889           | 0.5373    | 0.9477     | 0.7600        |
| clip_0_sepal_931.bin      | 0.6907     | 0.9811           | 0.5200    | 0.8918     | 0.8091        |
| disable_order_clip_931.bin| 0.7720     | 0.9875           | 0.5207    | 0.9557     | 0.7682        |
| random_rescale_931.bin    | 0.7627     | 0.9877           | 0.5693    | 0.9529     | 0.7594        |
| rescale_avg_931.bin       | 0.7527     | 0.9857           | 0.3587    | 0.9274     | 0.7489        |


ESR, 1000 iters, perplexity 50, push every 20
random fix multiple features
class: only compare disable - clip/rescale, scale ranges with density
clip: 1 overlap: full coverage
fixed features: X
2 17 63 87 100

| Filename                  | Continuity | Trustworthiness | OutContin | Steadiness | Cohesiveness |
|---------------------------|------------|------------------|-----------|------------|--------------|
| clip_disable_-335.bin     | 0.1142     | 0.7308           | 0.0187    | 0.6063     | 0.4768       |
| rescale_disable_-335.bin  | 0.1533     | 0.7572           | 0.0162    | 0.6131     | 0.4311       |
| x100_-335.bin             | 0.0335     | 0.6651           | 0.0246    | 0.5889     | 0.7135       |
| x17_-335.bin              | 0.0324     | 0.6642           | 0.0239    | 0.5930     | 0.7008       |
| x2_-335.bin               | 0.0308     | 0.6592           | 0.0217    | 0.5895     | 0.7193       |
| x63_-335.bin              | 0.0342     | 0.6678           | 0.0251    | 0.6070     | 0.7108       |
| x87_-335.bin              | 0.0346     | 0.6667           | 0.0245    | 0.6016     | 0.7149       |
| clip_disable_-846.bin     | 0.1182     | 0.7357           | 0.0189    | 0.6158     | 0.4588       |
| rescale_disable_-846.bin  | 0.1534     | 0.7604           | 0.0151    | 0.6128     | 0.4444       |
| x100_-846.bin             | 0.0331     | 0.6617           | 0.0233    | 0.5809     | 0.7024       |
| x17_-846.bin              | 0.0329     | 0.6662           | 0.0248    | 0.6042     | 0.6921       |
| x2_-846.bin               | 0.0308     | 0.6596           | 0.0222    | 0.5836     | 0.7354       |
| x63_-846.bin              | 0.0329     | 0.6640           | 0.0246    | 0.5821     | 0.7009       |
| x87_-846.bin              | 0.0342     | 0.6659           | 0.0242    | 0.5929     | 0.7132       |
| clip_disable_883.bin      | 0.1175     | 0.7358           | 0.0191    | 0.6093     | 0.4840       |
| rescale_disable_883.bin   | 0.1540     | 0.7610           | 0.0166    | 0.6155     | 0.4355       |
| x100_883.bin              | 0.0334     | 0.6645           | 0.0251    | 0.5912     | 0.7420       |
| x17_883.bin               | 0.0323     | 0.6633           | 0.0251    | 0.5989     | 0.6964       |
| x2_883.bin                | 0.0307     | 0.6603           | 0.0224    | 0.5901     | 0.7287       |
| x63_883.bin               | 0.0341     | 0.6679           | 0.0252    | 0.5883     | 0.7227       |
| x87_883.bin               | 0.0344     | 0.6660           | 0.0252    | 0.5944     | 0.7096       |

| Filename        | Continuity | Trustworthiness | OutContin | Steadiness | Cohesiveness |
|----------------|------------|------------------|-----------|------------|--------------|
| base_-335.bin  | 0.1995     | 0.8085           | 0.1230    | 0.6779     | 0.6501       |
| base_-846.bin  | 0.1981     | 0.8076           | 0.1204    | 0.6812     | 0.6114       |
| base_883.bin   | 0.1983     | 0.8072           | 0.1199    | 0.6687     | 0.6572       |
