## Pattern Recognition
### Dimensionality Reduction, 차원 축소
#### Curse odimensionality, 차원의 저주
- feature가 늘어날 수록 성능은 좋아지지만, 더 이상 추가해도 성능이 급감하는 곳이 있다. training data에만 overfitting되고, complexity도 높아지기 때문이다.
- irrelevant(무관계)하거나 redundant(중복)한 feature들을 잘 골라내야 한다.

#### Number of sample
- 보통 feature가 10배 더 많아야 하지만, classifier가 complex할 수록 sample/feature ratio가 기하급수적으로 더 높아야 한다.

#### `Dimensionality Reduction, 차원 축소`
- 그렇다면 feature를 어떻게 줄일 수 있을까? dimension을 reduce하자.
1. appropriate `subset`을 찾아내자.
2. `Transforming`(Combining)하자.

### 1. Feature Selection
#### Feature Selection
- Exhaustive search는 impractical하므로, 크게 아래 두가지 방법이 있다.
- a. `Filter`
<br> Objective function은 classifier와 독립적이며, class 간 거리나, 통계적 의존성 등만을 고려한다.
<br> 속도는 빠르지만, 함수가 단조로워 높은 성능을 기대하기는 어렵다.
- b. `Wrapper`
<br> Objective function은 classification algorithm을 사용하며, predictive accuracy로 판단한다.
<br> 속도는 느리지만, classifier에 fit하다.

#### Naive search
- performance 순서대로 기능 정렬상위 m개 기능 선택
• 단, 특징 상관관계(또는 의존성)는 고려되지 않는다.

### 2. Linear Transformation
#### Feature Extraction
- 

### Principal Component Analysis
#### `PCA, 주 성분 분석



