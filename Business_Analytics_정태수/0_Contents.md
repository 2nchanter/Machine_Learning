## Business_Analytics_정태수
### [1_1_선형대수](https://github.com/2nchanter/Machine_Learning/blob/main/Business_Analytics_%EC%A0%95%ED%83%9C%EC%88%98/1_1_%EC%84%A0%ED%98%95%EB%8C%80%EC%88%98.md#%EC%84%A0%ED%98%95%EB%8C%80%EC%88%98)
#### 1. 선형대수의 기본 요소
- 스칼라와 벡터, 벡터의 차원, 벡터 활용 예시, 벡터 연산, 벡터 종류
- 행렬, 행렬의 종류, 선형방정식, 선형연립방정식, 가우스 소거법, 기본 행 연산
- 가역행렬, 역행렬(구하기), Determinant(행렬식)
#### 2. 벡터공간과 부분공간
- 선형결합, span, 해 조건(vector equation)
#### 3. 선형변환
#### 4. 최소제곱법
- Least Squares Problem, over determined system
- orthogonal vectors(직교 벡터), Error Sum of Squares(SSE)
#### 5. 고유값과 고유벡터, 고유값 분해
- eigenvalue, eigenvector(고유값, 고유벡터)
- eigendecomposition(대각화분해)
- characteristic equartion(특성방정식)
- covariance matrix(공분산행렬)

### [1_2_최적화](https://github.com/2nchanter/Machine_Learning/blob/main/Business_Analytics_%EC%A0%95%ED%83%9C%EC%88%98/1_2_%EC%B5%9C%EC%A0%81%ED%99%94.md#%EC%B5%9C%EC%A0%81%ED%99%94%EC%99%80-%EC%88%98%EB%A6%AC%EA%B3%84%ED%9A%8D%EB%B2%95)
#### 1. 최적화와 수리계획법
- optimization(최적화), 최적화 및 수리계획법 모형 개요
#### 2. 미적분 기초
- derivative(미분), partial derivative(편미분), activation function(활성화 함수)
- Gradient(그래디언트)
<br> - Gradient descent(∇f), Derivate Term(미분계수), Learning Rate(학습 속도)
#### 3. 비선형 계획법 개요
- Global maximum, Global minimum, Stationary Points(안정점), Saddle point(안장점)
#### 4. 수치 최적화 알고리즘
- Numerical Optimization Algorithms, 머신러닝과 경사하강법, Batch(Full-batch gradient descent), 경사하강법 예시, 경사하강법 확장(Adam : RMSProp + Momentum)
#### 5. 라그랑지 승수와 제약식 있는 최적화

### [2_선형회귀분석](https://github.com/2nchanter/Machine_Learning/blob/main/Business_Analytics_%EC%A0%95%ED%83%9C%EC%88%98/2_%EC%84%A0%ED%98%95%ED%9A%8C%EA%B7%80%EB%B6%84%EC%84%9D.md#%EC%84%A0%ED%98%95%ED%9A%8C%EA%B7%80%EB%B6%84%EC%84%9D)
#### 1. Prediction(예측)

- 예측이란?, 예측 vs 분류, 예측모형 개요
#### 2. Linear Regression(다중선형회귀모형)
- 2-1. 선형회귀모델 개요
<br> - 회귀분석, 선형회귀분석, 다중회귀분석
- 2-2. 선형회귀와 최소제곱법
<br> - 선형회귀모델
- 2-3. 선형회귀모형의 타당성 검토
<br> - 모형의 타당성 검토, 점 추정, 구간 추정, 결정 계수
#### 3. 예측성능 평가척도
- 성능평가
<br> - Avg error, MSE, MAE, MAPE
#### 4. 변수선택 방법
- 변수선택의 필요성, 모형선택의 기준, 변수선택 절차, 변수선택(SFS, SBS등), Adjusted-R^2(수정 결정계수)

### [3_로지스틱_회귀분석](https://github.com/2nchanter/Machine_Learning/blob/main/Business_Analytics_%EC%A0%95%ED%83%9C%EC%88%98/3_%EB%A1%9C%EC%A7%80%EC%8A%A4%ED%8B%B1_%ED%9A%8C%EA%B7%80%EB%B6%84%EC%84%9D.md#%EB%A1%9C%EC%A7%80%EC%8A%A4%ED%8B%B1-%ED%9A%8C%EA%B7%80%EB%B6%84%EC%84%9D)
#### 알고리즘 종류
- Decision Tree, Logistic Regression, Random Forest, SVM, Neural Network
#### Logistic Regression
- sigmoid function
- Odds, log odds, 식 유도
#### 결과 해석
- 어떤 모델이 더 좋은가?
- logistic regression의 회귀계수의 의미
- 실제 결과데이터, 해석

### [4_정규화_모델](https://github.com/2nchanter/Machine_Learning/blob/main/Business_Analytics_%EC%A0%95%ED%83%9C%EC%88%98/4_%EC%A0%95%EA%B7%9C%ED%99%94_%EB%AA%A8%EB%8D%B8.md#%EC%A2%8B%EC%9D%80-%EB%AA%A8%EB%8D%B8%EC%9D%B4%EB%9E%80)
#### 좋은 모델이란?
- Explanatory modeling, Predictive modeling
- Expected MSE
- Bias, Variance
- regularization 모델
<br> - Ridge, Lasso, Elastic Net

### [5_의사결정나무](https://github.com/2nchanter/Machine_Learning/blob/main/Business_Analytics_%EC%A0%95%ED%83%9C%EC%88%98/5_%EC%9D%98%EC%82%AC%EA%B2%B0%EC%A0%95%EB%82%98%EB%AC%B4.md#decision-tree)
#### decision tree : classification
- decision tree 개요, Recursive partitioning, Pruning the tree
- impurity 지표 - Entropy, Gini index
- IG (Information Gain)
- Pruning the tree(가지치기), Cost complexity(비용복잡도)

#### decision tree : regression
#### 분류모델 평가지표
- Accuracy, Precision, Recall, Specificity, Type 1 Error, Type 2 Error, F1 Score
- ROC, AUC

### [6_인공신경망](https://github.com/2nchanter/Machine_Learning/blob/main/Business_Analytics_%EC%A0%95%ED%83%9C%EC%88%98/6_%EC%9D%B8%EA%B3%B5%EC%8B%A0%EA%B2%BD%EB%A7%9D.md#%EC%9D%B8%EA%B3%B5%EC%8B%A0%EA%B2%BD%EB%A7%9D)
- Perceptron, Loss function, Activation function, Gradient
- MLP(XOR proplem), 과적합 방지, Vanishing gradient problem(ReLU)
