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


tests for mushrooms: 1000 iters, perplexity 30, fix_iter 10

fix cat 0 3 5 and last one
3 random inits
compare rescale, clip and random ordering

0: 2 cat, only random
3/5/last: random 3 times + avg

results
{'0_clip_random_0_42.bin': {'Continuity': np.float64(0.39203594288527827), 'Trustworthiness': np.float64(0.9973294037382646), 'OutContin': 0.01010585918266864, 'Steadiness': np.float64(0.8082302785117852), 'Cohesiveness': np.float64(0.7630676890112587)}, '0_rescale_random_0_42.bin': {'Continuity': np.float64(0.39495322501230923), 'Trustworthiness': np.float64(0.9973188547240897), 'OutContin': 0.015706548498276702, 'Steadiness': np.float64(0.8357889949706497), 'Cohesiveness': np.float64(0.7665380310007213)}, '22_clip_avg_42.bin': {'Continuity': np.float64(0.38420728705071394), 'Trustworthiness': np.float64(0.9970062826825506), 'OutContin': 0.036853766617429694, 'Steadiness': np.float64(0.7645377569837238), 'Cohesiveness': np.float64(0.7283825383467272)}, '22_clip_random_0_42.bin': {'Continuity': np.float64(0.3627646479566716), 'Trustworthiness': np.float64(0.9966190675230117), 'OutContin': 0.029049729197439363, 'Steadiness': np.float64(0.7519246129303632), 'Cohesiveness': np.float64(0.7175866076700224)}, '22_clip_random_1_42.bin': {'Continuity': np.float64(0.35199409158050227), 'Trustworthiness': np.float64(0.9964365190263137), 'OutContin': 0.019128508124076633, 'Steadiness': np.float64(0.761514676106721), 'Cohesiveness': np.float64(0.7166190786140018)}, '22_clip_random_2_42.bin': {'Continuity': np.float64(0.3697439684884294), 'Trustworthiness': np.float64(0.996770492708641), 'OutContin': 0.006782373215164954, 'Steadiness': np.float64(0.7577577818943589), 'Cohesiveness': np.float64(0.7154660341067114)}, '22_rescale_avg_42.bin': {'Continuity': np.float64(0.39442392909896606), 'Trustworthiness': np.float64(0.9973727929918477), 'OutContin': 0.046331856228459214, 'Steadiness': np.float64(0.7598891499577153), 'Cohesiveness': np.float64(0.7066960796159643)}, '22_rescale_random_0_42.bin': {'Continuity': np.float64(0.3921959625800099), 'Trustworthiness': np.float64(0.9972570164606823), 'OutContin': 0.03354258985721296, 'Steadiness': np.float64(0.770848741472506), 'Cohesiveness': np.float64(0.7213877721844402)}, '22_rescale_random_1_42.bin': {'Continuity': np.float64(0.39299606105366813), 'Trustworthiness': np.float64(0.9973518740948364), 'OutContin': 0.0485228951255543, 'Steadiness': np.float64(0.7743245878101905), 'Cohesiveness': np.float64(0.7268904185089322)}, '22_rescale_random_2_42.bin': {'Continuity': np.float64(0.3943500738552437), 'Trustworthiness': np.float64(0.9973820804963408), 'OutContin': 0.024593796159527153, 'Steadiness': np.float64(0.7792284177869618), 'Cohesiveness': np.float64(0.7326886834766673)}, '3_clip_avg_42.bin': {'Continuity': np.float64(0.387136878385032), 'Trustworthiness': np.float64(0.9971107557226314), 'OutContin': 0.06115214180206842, 'Steadiness': np.float64(0.7890816129897738), 'Cohesiveness': np.float64(0.7025269688977467)}, '3_clip_random_0_42.bin': {'Continuity': np.float64(0.37986213687838505), 'Trustworthiness': np.float64(0.9965879821634979), 'OutContin': 0.028508124076809246, 'Steadiness': np.float64(0.7580658354053167), 'Cohesiveness': np.float64(0.7044245487906986)}, '3_clip_random_1_42.bin': {'Continuity': np.float64(0.3698424421467258), 'Trustworthiness': np.float64(0.9963179978387044), 'OutContin': 0.04478089611029059, 'Steadiness': np.float64(0.7625515885075612), 'Cohesiveness': np.float64(0.7121240815557077)}, '3_clip_random_2_42.bin': {'Continuity': np.float64(0.37379369768586906), 'Trustworthiness': np.float64(0.9964426565517576), 'OutContin': 0.0259354997538157, 'Steadiness': np.float64(0.7442055575522901), 'Cohesiveness': np.float64(0.7209884104119029)}, '3_rescale_avg_42.bin': {'Continuity': np.float64(0.3928729689807977), 'Trustworthiness': np.float64(0.9969934186235323), 'OutContin': 0.0555145248645997, 'Steadiness': np.float64(0.7820820844418248), 'Cohesiveness': np.float64(0.7052564050085743)}, '3_rescale_random_0_42.bin': {'Continuity': np.float64(0.3961349089118661), 'Trustworthiness': np.float64(0.9970756748234274), 'OutContin': 0.048535204332841426, 'Steadiness': np.float64(0.7906231053073522), 'Cohesiveness': np.float64(0.7164122268780885)}, '3_rescale_random_1_42.bin': {'Continuity': np.float64(0.3918389955686854), 'Trustworthiness': np.float64(0.9970984867439925), 'OutContin': 0.048227474150664536, 'Steadiness': np.float64(0.79721057373932), 'Cohesiveness': np.float64(0.7084899982857298)}, '3_rescale_random_2_42.bin': {'Continuity': np.float64(0.3895371738060069), 'Trustworthiness': np.float64(0.9969378772820991), 'OutContin': 0.03652141802067948, 'Steadiness': np.float64(0.795049392163897), 'Cohesiveness': np.float64(0.7083919763175888)}, '5_clip_avg_42.bin': {'Continuity': np.float64(0.38474889217134417), 'Trustworthiness': np.float64(0.9970494867325463), 'OutContin': 0.035376661742983685, 'Steadiness': np.float64(0.771058818984353), 'Cohesiveness': np.float64(0.7320476744919142)}, '5_clip_random_0_42.bin': {'Continuity': np.float64(0.3826193993106844), 'Trustworthiness': np.float64(0.9970070675207041), 'OutContin': 0.01919005416051198, 'Steadiness': np.float64(0.7655855227134607), 'Cohesiveness': np.float64(0.7292903385329228)}, '5_clip_random_1_42.bin': {'Continuity': np.float64(0.37134416543574594), 'Trustworthiness': np.float64(0.99701926515042), 'OutContin': 0.006093057607090116, 'Steadiness': np.float64(0.7567566927230089), 'Cohesiveness': np.float64(0.73331012765503)}, '5_clip_random_2_42.bin': {'Continuity': np.float64(0.37255046774987693), 'Trustworthiness': np.float64(0.99683026185328), 'OutContin': 0.018439192516001866, 'Steadiness': np.float64(0.7581474918752411), 'Cohesiveness': np.float64(0.7405180304019883)}, '5_rescale_avg_42.bin': {'Continuity': np.float64(0.39417774495322505), 'Trustworthiness': np.float64(0.9973583592565224), 'OutContin': 0.027708025603150947, 'Steadiness': np.float64(0.7824489001515565), 'Cohesiveness': np.float64(0.745115250186552)}, '5_rescale_random_0_42.bin': {'Continuity': np.float64(0.39054652880354507), 'Trustworthiness': np.float64(0.9972323266971852), 'OutContin': 0.04207287050713961, 'Steadiness': np.float64(0.7704405064195772), 'Cohesiveness': np.float64(0.748528063907026)}, '5_rescale_random_1_42.bin': {'Continuity': np.float64(0.38980797636632203), 'Trustworthiness': np.float64(0.99732556455898), 'OutContin': 0.015731166912850748, 'Steadiness': np.float64(0.7684550479641041), 'Cohesiveness': np.float64(0.7293965131605005)}, '5_rescale_random_2_42.bin': {'Continuity': np.float64(0.39177744953225013), 'Trustworthiness': np.float64(0.9972677036185168), 'OutContin': 0.03477351058591819, 'Steadiness': np.float64(0.7891287466940393), 'Cohesiveness': np.float64(0.7483418641541261)}}