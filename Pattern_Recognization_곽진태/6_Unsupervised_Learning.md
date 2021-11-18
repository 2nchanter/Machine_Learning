## Unsupervised Learning, 비지도학습
### Unsupervised Learning, 비지도학습
- Supervised Learning, 지도학습 : Data, Label
- `Unsupervised learning, 비지도학습` : Only data, No label
<br> - 왜 하는가? class 수도 모르고, 알아도 labeling 해야 하므로. 데이터 구조에 대한 통찰력 확보

#### Clustering
- 데이터 내에서 자연 군집 찾기
- Cluster 내에 있는 data point들은 거리가 가까워야하고, 밖에 있다면 멀어야 좋은 cluster.
- 구성요소
<br> - A. `Proximity measure` : similarity measure는 비슷할 수록 값이 크다. dissimil- 은 비슷할 수록 값이 작다.
<br> - B. `Objective function` : clustering이 잘 되었는지 판단하는 목적함수.
<br> - C. `Algorithm` : clustering 해줌
- 일단 특정한 갯수로 fix하고 시작한다. 비지도학습은 data를 잘 모르기 때문에 이걸 정할 수가 없다.
#### A. Proximity measure
- Euclidean distance
- Manhattan (city block) distance
- Chebyshev distance
- Cosine similarity
- Correlation coefficient
#### B. Objective function
- Sum of Squared Errors(SSE)
#### C. Algorithm
- Iterative algorithm, K-means Clustering
#### C-1. K-means Clustering
- 
#### Hierarchical Clustering
- 


