## Unsupervised Learning, 비지도학습
- Supervised Learning, 지도학습 : Data, Label
- `Unsupervised learning, 비지도학습` : Only data, No label
<br> - 왜 하는가? class 수도 모르고, 알아도 labeling 해야 하므로. 데이터 구조에 대한 통찰력 확보

## Partitioning Clustering, 분할 군집화
### Clustering
- 데이터 내에서 자연 군집 찾기
- Cluster 내에 있는 data point들은 거리가 가까워야하고, 밖에 있다면 멀어야 좋은 cluster.
- 구성요소
<br> - A. `Proximity measure` : similarity measure는 비슷할 수록 값이 크다. dissimil- 은 비슷할 수록 값이 작다.
<br> - B. `Objective function` : clustering이 잘 되었는지 판단하는 목적함수.
<br> - C. `Algorithm` : clustering 해줌
- 일단 특정한 갯수로 fix하고 시작한다. 비지도학습은 data를 잘 모르기 때문에 이걸 정할 수가 없다.

### A. Proximity measure
- Euclidean distance : 직선거리, 최단거리
- Manhattan (city block) distance : 각 축에서 차의 합
- Chebyshev distance : 각 축에서 차이 중 가장 큰 값
- Cosine similarity : 원점에서부터 두 data까지 그은 선 사이의 각도
- Correlation coefficient : 상관계수(높을수록 비슷)

### B. Objective function
- Sum of Squared Errors(SSE)
<br> - cluster 내의 |data - 평균| 제곱의 합
<br> - cluster의 형태가 circle or ellipses일 때 용이하다.
<br> - 하지만 SSE는 동일한 크기의 군집을 선호하기 때문에, 자연 군집의 크기가 매우 다른 경우에는 적절하지 않다.
<br> - <img width="250" src="https://user-images.githubusercontent.com/89369520/142587203-39c282e4-fe7c-4474-8898-6a36890a28b1.png">
<br> - <img width="250" src="https://user-images.githubusercontent.com/89369520/142587323-26d457ee-7dff-4f7d-ab7c-24a24753a572.png">

### C. Algorithm
- 좋은 clustering을 Exhaustive search하는 것은 불가능하다.
- Iterative algorithm, 반복 알고리즘
<br> - 먼저 의미있는 구분점을 찾는다.(최적의 정답이 아님)
<br> - 반복 : objective function이 개선되는 방향으로 sample을 다른 cluster로 하나씩 계속 옮긴다.
<br> - 옮기는 방법은 뭐가 있을까?

### C-1. `K-means Clustering`
- Sequence
<br> 0. Object Function은 SSE이며, cluster 내 data 수를 임의로 k개로 지정해놓고 시작.
<br> 1. Initialize
<br> - 1-1. k cluster의 center를 cluster 내에 있는 data중 임의로 하나 선택한다.
<br> - 1-2. 각 data를 가장 가까운 center에 할당하여 cluster를 구성한다.
<br> <img width="150" src="https://user-images.githubusercontent.com/89369520/142590137-4bad5345-3595-474b-8dfd-9c9e3dc7ca86.png">
<br> 2. cluster 내 data들의 평균을 구해서 새로운 center point를 지정한다.
<br> <img width="150" src="https://user-images.githubusercontent.com/89369520/142590209-14264f19-b585-4118-8725-281cb777c8e4.png">
<br> 3. 재지정된 center point(mean)에 가까운 data들로 re-clustering 한다.
<br> <img width="150" src="https://user-images.githubusercontent.com/89369520/142590231-7d9b9bcb-bbb1-4e55-943e-372780a748d0.png">
<br> 4. 3번에서 cluster 구성이 변화했다면, 2번으로 돌아가 반복한다.
<br> END. Iterate하다보면 변하지 않는 cluster가 만들어진다.

- Does it work?
<br> <img width="300" src="https://user-images.githubusercontent.com/89369520/142591005-27da0606-3141-4463-b90b-76b4da3780cd.png">

- Global minimum?
<br> 각 iteration에서 더 나은 cluster를 찾는 효과적인 algorithm이다.
<br> 하지만 start point에 따라서 항상 Global minimum(최적해)가 아닌 `Local minimum`을 찾아줄 수도 있다는 단점이 있다.

### Hierarchical Clustering, 계층적 군집화
- Approaches
<br> 1. Agglomerative (bottom up)
<br> - n개의 singleton cluster에서 시작하여, 가장 유사한 cluster를 병합하여 계층을 구성
<br> 2. Divisive (top down)
<br> - 전체를 하나의 cluster로 시작하며, worst cluster를 분할하며 계층을 구성

#### Agglomerative
- 가장 가까운 singleton을 찾아서 merge.
- Distance measure
<br> - d min, max, avg, mean
- Single linkage (Nearest neighbor)
<br> - d min(Di, Dj) = min||x - y||, Di와 Dj에서 가장 가까운 거리에 있는 point의 거리
<br> - elongated cluster가 잘 만들어지며, noise에 취약하다.
- Farther linkage (Farthest neighbor)
<br> ex) <img width="400" src="https://user-images.githubusercontent.com/89369520/143546060-4b21529f-d292-47a5-a740-0f8b6e48d1a8.png">
<br> - d max(Di, Dj) = max||x - y||, Di와 Dj에서 가장 먼 거리에 있는 point의 거리
<br> - compact cluster가 잘 만들어지며, data 분포가 elongated할 때는 문제가 있다.
<br> ex) <img width="300" src="https://user-images.githubusercontent.com/89369520/143546028-58354b0c-0933-4341-94e6-942e3b2f00da.png">

#### Agglomerative vs Divisive
- Agglomerative는 global structure가 아닌 pairwise만을 고려한다.
<br> Divisive가 상대적으로 맹목적인 global structure 인식이 적다.
