# Week4. 머신러닝의 시작 - 회귀분석, 회귀분석 심화
## 01.회귀분석이란
### 회귀분석이란
#### `Supervised learning`(지도 학습)
- Y = f(x)에서, x와 y의 관계에 대하여 함수를 모델링 하는 것
<br> `regression`(회귀): 입력 변수 x에 대해서 연속형 출력 변수 y를 예측
<br> `classification`(분류) : 입력 변수 x에 대해서 이산형 출력 변수 y를 예측

#### `linear regression`(선형회귀) / `non-linear regression`(비선형회귀)
- classification model과 구분하긴 하지만, 대부분의 분류모델(ex. SVM, Decision Tree)로도 regression이 가능하다.

#### `단순 선형 회귀분석`
- 변수가 1개 일 때, X와 Y가 선형관계에 있다고 가정하고 적합한다. 2개 이상일때는? 다중 선형 회귀 분석.
<br> 우리가 알고 싶은 식 : y = β0 + β1X + ε (β1 : 기울기, β0 : 절편, ε : noise)
<br> 우리가 추정 해야 하는 식 : y^ = β0^ + β1^X

>어떻게 추정할까?
<br> 여러 개의 직선 중 가장 좋은 직선은?
<br> = `직선과 데이터의 차이가 평균적으로 가장 작아지는 직선`

## 02.회귀계수를 추정하는 방법
### 회귀계수추정
#### 어떻게 추정할까?
- 실제 값과 우리가 추정한 값의 차이가 적으면 좋겠다.
<br><img width="300" alt="스크린샷 2021-09-08 오전 7 53 57" src="https://user-images.githubusercontent.com/89369520/132420524-65a7c667-81d7-4fc0-a66e-dc94128c4880.png">
<br> `residual`(잔차) : ei = yi - yi^
<br> `SSE`(Error Sum of Squares, 잔차의 제곱합) : SSE = Σ ei^2 = e1^2 + ... + en^2

- Q1. 굳이 SSE를 최소화 시키는 이유? 
<br> - A1. residual의 합이 0이 되는 해는 많아 유일한 해를 찾지 못한다.
<br> - Q2. 그럼 residual의 절대값의 합을 최소화 하면 되지 않나?
<br> - A2. 절대값의 합은 미분이 불가능하다.

#### `Least Square Method`(최소자승법)
- <img width="400" alt="스크린샷 2021-09-08 오전 8 18 19" src="https://user-images.githubusercontent.com/89369520/132422197-5683e993-b1f0-4519-acda-295997742e33.png">
- <img width="400" alt="스크린샷 2021-09-08 오전 8 18 39" src="https://user-images.githubusercontent.com/89369520/132422224-604e5254-c357-4db2-9322-b8157860f242.png">

## 04.회귀계수에 대한 검정
### 회귀계수에 대한 검정
#### 선형 회귀의 정확도 평가
