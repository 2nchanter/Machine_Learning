# Week1. 머신러닝 개요

## 01.Machine Learning의 개념
`인공 지능의 한 분야로, 컴퓨터가 학습할 수 있도록 하는 알고리즘과 기술을 개발하는 분야`

주어진 데이터를 통해서,
1. 독립변수와 종속변수간의 관계로 모델을 만드는 것.
2. 데이터의 특징을 찾아내는 모델을 만드는 것.

```
'x로 y를 예측하고 싶다.'

회귀분석의 경우,
y^ = f^(x) + ε

y : 종속변수
f() : 모델
x : 독립변수
ε : (우리가 맞출 수 없는)오차항
^ : 우리가 추측한 상태

# 우리는 모집단 전체가 아닌 우리가 아는 일부분으로만 학습시키기 때문에 '추측한 상태'가 된다.
```

## 02.지도학습과 비지도학습
### 1. 지도학습(Supervised learning)
- input/output, labeled data
<br>연속성(숫자) 변수 -> `회귀 모형(Regression)` / ex) 주식가격예측
<br>이산형(문자) 변수 -> `분류 모형(Classification)` / ex) 공정 불량 여부 탐지

### 2. 비지도학습(Unsupervised learning)
- input, un-labeled data
<br>유사한 데이터끼리 그룹화 -> `군집 분석(Clustering)` / ex) 고객 segmentatation
<br>독립변수들의 차원을 축소화 -> `PCA`

### 3. 강화학습(reinforcement learning)
- No data set, state & action, Simulation, Decision making
<br>수 많은 시뮬레이션을 통해 현재의 선택이 미래에 보상이 최대가 되도록 학습 / ex) 알파고

## 03.Machine Learning의 종류
### Supervised learning
#### 1. 선형 회귀분석(Linear regression)
- `직선을 모델링해서 y를 추측`
- 인과관계 파악이 쉽지만, 비선형 관계(2차)에서는 표현이 어렵다.
<br><img width="400" alt="스크린샷 2021-09-01 오전 11 30 23" src="https://user-images.githubusercontent.com/89369520/131602039-d7db05d6-9dd9-4c94-bdde-de020e87b8f0.png">

#### 2. 의사결정나무(Decision tree)
- `독립 변수의 조건에 따라 종속변수를 분리`
- 직관적이나, 과적합(overfitting)이 잘 일어난다. (ensemble learning의 기초)
<br>과적합이란? 학습 데이터에는 잘 맞지만, 실제 데이터에서 문제가 있는 상태.
<br><img width="400" alt="스크린샷 2021-09-01 오전 11 31 38" src="https://user-images.githubusercontent.com/89369520/131602132-5d19e92d-bf36-4c85-aba5-49c21bfda897.png">

#### 3. KNN(K-Nearest neigbor)
- `주변 k개를 기준으로 신규 데이터를 어느쪽에 더 가까운지 분류해서 포함함.`
- k처럼 사람이 지정해주는 변수를 hyperparameter.
<br><img width="400" alt="스크린샷 2021-09-01 오전 11 32 09" src="https://user-images.githubusercontent.com/89369520/131602182-85f15faf-2563-4778-a256-7cff189445e6.png">

#### 4. Neural Network
- `input. hidden, output으로 구성. 각 노드의 가중치를 업데이트하며 학습`
<br><img width="400" alt="스크린샷 2021-09-01 오전 11 34 34" src="https://user-images.githubusercontent.com/89369520/131602433-817034bc-6d3e-4ea9-a240-d5863e665d40.png">

#### 5. SVM(Support Vector Machine)
- `Class간의 거리가 최대가 되도록 decision boundary를 만드는 방법`
- 학습하는 과정 내에서 어느정도 오차를 허용하기 때문에 decision boundary가 좋아짐.
<br>하지만 학습시간이 너무 오래 걸림, 2000대 초반 모델
<br><img width="400" alt="스크린샷 2021-09-01 오전 11 43 16" src="https://user-images.githubusercontent.com/89369520/131603233-9f33ed53-71f7-49a5-9cac-b1e690acc773.png">

#### 6. Ensemble Learning
- `여러 개의 모델을 결합하여 사용`하는데
<br>기본모델, classifier/base learner로는 decision tree가 많이 사용됨.
- 대표적으로 3가지. bagging, random forest, boosting.
- 어떻게 하면 다양한 base learner를 만들 수 있을까?
<br><img width="400" alt="스크린샷 2021-09-01 오전 11 43 40" src="https://user-images.githubusercontent.com/89369520/131603274-6c212cc9-a0ad-4e36-b8fe-e6ced48cc9fd.png">

### Un-Supervised learning
#### 7. K-means clustering
- 군집분석으로, `Label 없이 데이터들을 k개로 군집화`
- k에 따라 성능차가 큼
<br><img width="400" alt="스크린샷 2021-09-01 오전 11 44 01" src="https://user-images.githubusercontent.com/89369520/131603303-ea95750e-d13e-4c13-9105-8a3cf9d1aae9.png">

## 04.모형의 적합성 평가 및 실험설계 - 1
### 0. 모형의 적합성을 평가하는 방법
<br><img width="400" alt="스크린샷 2021-09-01 오후 5 02 23" src="https://user-images.githubusercontent.com/89369520/131635151-68b2fc5b-07cd-4589-ad37-9379057da785.png">
```
MSE - 평균제곱오차, 제곱 된 값은 항상 양수이므로 커짐, 낮을 수록 좋음.
Flexibility - 복잡도, 얼마나 이 모양이 복잡한가.

노랑 : 검증 데이터, 학습 데이터 모두 MSE가 높음. underfitting.
파랑 : 원하는 f(). MSE, 복잡도도 살짝 증가함.
초록 : 학습 데이터에 overfitting됨.
```

### 1. 기본 데이터 분할(Traning-Validation-Test)
- original data set =
<br>+ 0.5 `training data` : 학습 데이터, 모형 f를 추정하는데 필요
<br>+ 0.3 `validation data` : 검증 데이터, 추정한 모형 f가 적합한지 검증함
<br>+ 0.2 `test data` : 평가 데이터, 최종적으로 선택한 모형의 성능을 평가

- 검증 데이터(validation data)를 보고 k값(hyperparameter)을 조정하는데,
<br>이런 현상을 validation에 overfitting 되었다고 한다.

- training data에 어떤 data가 속하느냐에 따라 MSE 값은 달라지므로,
<br>실험에 따라 여러번 진행하기도 한다.

### 2. k-Fold 교차검증(k-Fold Cross Validation)
>'아 이 데이터는 학습에 들어갔으면 하는데...'
><br>'데이터 수가 좀 적은것 같은데...'

`5개 혹은 10개의 fold로 나누고`, 순서대로 validation에 사용하며 나온 성능을 평균내어 성능지표로 사용한다.

### 3. LOOCV(Leave-One-Out Cross Validation)
>'와 데이터 너무 적다'
><br>'k-Fold 써도 너무 다르게 나온다'

`데이터 1개가 1개 fold`가 되어 학습한다. 성능 평균내는 방식은 동일. (+- %)

## 05.모형의 적합성 평가 및 실험설계 - 2
### 0. 데이터 분석과정
`raw data` - `전처리 된 data` - `실험설계` - `Model`

### 1. 전처리
- `'어떠한 변수가 결과에 영향을 미칠까?'`를 생각하고 합리적인 근거로 데이터 병합 및 파생변수(feature)를 만들어야 한다.
- raw data의 feature와, 재생산한 feature로 ML을 돌리는 것은 큰 차이가 있다.
<br>합리적으로 기존 feature들을 + - * / 한다면, 더 시작적으로 잘 보여서 잘 판단할 수 있게 된다. 머신도!

### 2. 실험설계
- `Traning-Validation-Test` 
- ex) class imbalance (?) 한 경우, 실제 데이터의 비율과 동일하게 sampling을 해야된다.
<br>총 데이터의 비율이 9:1이면, training data도 9:1, validation 9:1로 맞춰서 실험하는 것이 좋다. (층화 추츨) ???

## 06.과적합(Overfitting)이란
- `training data에 너무 잘 맞지만, validation data나 test data에는 맞지 않는 현상`
<br>data가 적거나, 모형이 복잡하면 복잡할수록 잘 일어난다.
<br><img width="700" alt="스크린샷 2021-09-01 오후 8 00 29" src="https://user-images.githubusercontent.com/89369520/131660323-f147bd85-a9e5-4ca6-b6a4-4e96053b4441.png">
<br> 실제 값과 예측 값에 대한 성능 지표 `MSE`는, 예측 모델의 분산`Var`과 모델이 예측할 수 있는 정도 `Bias`와 어쩔 수 없는 오차 `𝜖`로 이루어져 있다.

```
오류제곱의 평균(Mean Squared Error) = 감소 가능한 오류(redicible error) + 감소 불가능한 오류(irredicible error)
                                   = 분산(variance) + 편파성(bias)
```
- variance : 다른 학습 데이터를 이용했을 때, f^이 변하는 정도
<br>Bias : 추측한 값과 실제 데이터의 다른 정도
<br>따라서 복잡할수록 variance가 높아지며, 간단할 수록 bias가 높아진다. 이 trade-off 관계에서 최소값을 찾는 것이 포인트.
<br><img width="300" alt="스크린샷 2021-09-01 오후 8 22 32" src="https://user-images.githubusercontent.com/89369520/131662952-a3b44b0a-0bba-4725-be18-265149deba41.png">

>Q1. Overfitting은 딱 맞는건데 왜 안좋은거야?
<br>A1. 우리가 갖고있는 data가 모집단이 아니라서 안좋은 것.

>Q2. Training-Validation-Test를 Random하게 가져가면 Overfitting되도 여기저기 잘맞는거 아닐까?
<br>A2. 완벽한 random은 없으며, 표본은 모집단을 대표할 수가 없다. 
