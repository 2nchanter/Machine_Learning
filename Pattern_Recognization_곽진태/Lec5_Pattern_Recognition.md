# Pattern Recognition
## Dimensionality Reduction, 차원 축소
### Curse odimensionality, 차원의 저주
- feature가 늘어날 수록 성능은 좋아지지만, 더 이상 추가해도 성능이 급감하는 곳이 있다. training data에만 overfitting되고, complexity도 높아지기 때문이다.
- irrelevant(무관계)하거나 redundant(중복)한 feature들을 잘 골라내야 한다.

### Number of sample
- 보통 feature가 10배 더 많아야 하지만, classifier가 complex할 수록 sample/feature ratio가 기하급수적으로 더 높아야 한다.

### `Dimensionality Reduction, 차원 축소`
- 그렇다면 feature를 어떻게 줄일 수 있을까? dimension을 reduce하자.
1. appropriate `subset`을 찾아내자.
2. `Transforming`(Combining)하자.

## 1. Feature Selection
### Feature Selection
- Exhaustive search는 impractical하므로, 크게 아래 두가지 방법이 있다.
- a. `Filter`
<br> Objective function은 classifier와 독립적이며, class 간 거리나, 통계적 의존성 등만을 고려한다.
<br> 속도는 빠르지만, 함수가 단조로워 높은 성능을 기대하기는 어렵다.
- b. `Wrapper` (아래 예시들은 대부분 Wrapper 방식으로 진행됨)
<br> Objective function은 classification algorithm을 사용하며, predictive accuracy로 판단한다.
<br> 속도는 느리지만, classifier에 fit하다.

### `Naive search`
- performance 순서대로 기능 정렬한 뒤, `상위 m개 Feature 선택`한다.
- 단, feature correlation(or dependence)는 고려되지 않는다.

### Sequential Forward Selection (`SFS`)
- 과정
<br> 1. Empty subset에서 시작
<br> 2. 1개 추가했을때 가장 좋은 성능인 feature를 찾음
<br> 3. 해당 feature를 집합에 포함시킨 subset을 채택
<br> 4. 2번으로 감 (optimal일 때까지 반복)
- optimal subset이 작을 때 우수한 성능을 보이며, 단점으로 한번 추가한 feature는 제거할 수 없다.

### Sequential Backward Selection (`SBS`)
- 과정
<br> 1. Full subset에서 시작
<br> 2. 1개 제거했을때 가장 좋은 성능인 feature를 찾음
<br> 3. 해당 feature를 집합에서 제거시킨 subset을 채택
<br> 4. 2번으로 감 (optimal일 때까지 반복)
- optimal subset이 클 때 우수한 성능을 보이며, 단점으로 한번 제거한 feature는 추가할 수 없다.

### Bidirectional Search (`BDS`)
- SFS와 SBS를 같이 사용한다.
<br> SFS에서 선택한 Feature는 SBS에서 제거하지 않으며,
<br> SBS에 제거한 Feature는 SFS에서 선택하지 않는다.

### Plus-L Minus-R Selection (`LRS`)
- BDS와 같이 같이 사용하는데, 계수가 L과 R로 다르다.
- 단점은 case마다, L 및 R의 최적값을 예측할 방법이 없다. (heuristics)
- ex) L > R 일 경우,
<br> Empty subset에서 시작하며, L개 추가 - R개 제거 과정을 반복한다.

### `Sequential Floating Forward Selection` (`SFFS`)
- Empty subset에서 시작한다.
- Forward 진행하여 feature가 추가될 때, 추가된 feature 외 다른 것을 제거하고 더 좋은 성능의 subset이 있는지 비교한다. 계속 backward 검증하다가 더 optimal한 subset이 없다면 다시 forward 진행한다.

### `Sequential Floating Backward Selection` (`SFBS`)
- Full subset에서 시작한다.
- Backward 진행하여 feature가 제거될 때, 제거된 feature외 다른 것을 추가하고 더 좋은 성능의 subset이 있는지 비교한다. 계속 foward 검증하다가 더 optimal한 subset이 없다면 다시 backward 진행한다.
<br><img width="500" src="https://user-images.githubusercontent.com/89369520/141403008-8a1bde7a-bdc3-49d9-abfc-7e44e625ef0b.png">

## 2. Linear Transformation
### Feature Extraction
- x에 W를 곱해서 Rd를 Rd'으로 차원을 낮춰보자.
1. Principal Component Anaiysls, `주 성분 분석(PCA)`
<br> data를 가장 잘 나타내는 것 찾기
2. Linear Discriminant Analysis, `선형 판별 분석(LDA)`
<br> 데이터를 가장 잘 구분하는 것 찾기

## 1. Principal Component Analysis
### `PCA, 주 성분 분석`
- 아이디어 : 저 차원 공간에서 가장 정확한 데이터 표현 찾기
- Data의 variance가 가장 잘 표현되는, 가장 큰 방향으로 projection 하는 것이 좋다.
<br> projection 후 좌표계를 변환한다. 또한 새 데이터 y의 Var이 이전 데이터 x의 var와 동일하다.




