# Week3. 머신러닝을 위한 수학 - 확률, 통계, 미분
## 09.수학적 개념 이해 - 미분의 개념
### 미분의 개념
- `평균 변화율` : f(b)-f(a)/b-a
<br> x가 변할 때, y의 변화량
- `순간 변화율` : f'(a)
<br> 평균 변화율의 극한 값, a 접선에서의 기울기
<br> b점이 a점으로 한없이 가까워질 때, a점에서의 순간변화율

- 다항함수 미분 및 미분 기본 공식 : {cf(x)}' = cf'(x), {f(x)+g(x)}' = f'(x)+g'(x)
- 곱의 미분 : {f(x)g(x)}' = f'(x)g(x)+f(x)g'(x)
- 합성함수 미분 : f(g(x))' = f'(g(x))g'(x)
- 지수함수 미분 : {e^x}' = e^x, {a^x}' = a^xlna
- 로그함수 미분 : {lnx}' = 1/x, {logax}' = 1/xlna

### 미분의 활용
- `극대값, 극소값` : f'(x)=0인 지점이 극대값!

## 10.수학적 개념 이해 - Likelihood, 확률분포함수
### Likelihood : [최대우도법(MLE)](https://angeloyeo.github.io/2020/07/17/MLE.html)
- 확률분포함수, `Probability disturibution function`
<br> 주어진 확률분포가 있을 때, 관측값이 얼마의 확률로 존재하는가
<br> - 확률밀도함수, Probability density function / PDF : 연속형
<br> - 확률질량함수, Probability mass function : 이산형

- 가능도 함수, `Likelihood function`
<br> 우리가 가진 자료를 가장 잘 설명하는 모수는 무엇일까?
<br> - 찾고자하는 파라미터 θ에 대하여 다음과 같이 편미분하고 그 값이 0이 되도록 하는 θ를 찾는 과정을 통해 likelihood 함수를 최대화 시켜줄 수 있는 θ를 찾을 수 있다.

## 11.수학적 개념 이해 - MLE 개념
### Likelihood
- Likelihood function
<br> 수치적으로 이 가능도를 계산하기 위해서는 각 데이터 샘플에서 후보 분포에 대한 높이(즉, likelihood 기여도)를 계산해서 다 곱한 것을 이용할 수 있을 것이다.
<br><img width="400" src="https://user-images.githubusercontent.com/89369520/132119445-c302027c-5050-4f58-947f-2b21f5675fb9.png">

- Maximum Likelihood Estimator / `MLE`
<br>Likelihood를 최대로 만드는 모수의 값
<br><img width="600" src="https://user-images.githubusercontent.com/89369520/132119608-e75b5e75-16d7-467d-baf8-150660edb7c4.png">
<br><img width="400" src="https://user-images.githubusercontent.com/89369520/132119513-53590a56-dd40-4a03-b520-c6da61509778.png">

## 12.수학적 개념 이해 - MLE 계산방법
<img width="500" src="https://user-images.githubusercontent.com/89369520/132144111-baaf4baf-d82b-4a1e-8869-10f48645f621.png">
- u0, a^2(λ)에 대한 Likelihood function에 log 취해서 도함수 값이 0인 u0^, λ^를 구한다.
<br> log 취해도 최고점은 같다.

## 13.수학적 개념 이해 - Matrix 정의 및 성질
### Matrix 표기법
 - Matrix
 - Vector : 행, 열의 수가 1인 경우. row vector, cloumn vector.
 - Trnspose and symmetric : 행열전환 / A -> A^T
<br> A = A^T 일 떄, 두개는 Symmetric이다.
 - Scalar : 원소 하나.
 - Identity matrix : I, 대각선 원소가 모두 1, 나머지 0인 matrix
 - Diagonal matrix : diag(a1,,,an), 대각선 원소값만 바뀌고, 나머지 0인 matrix
 - Equality : 모든 i, j에 대하여 aij = bij 이면 A = B
 - 합, 차, 곱의 성질
<br> - 상수배 : B = kA
<br> - 행렬곱 : A = (m x p), B = (p x n) => C = AB = (m x n) / 일반적으로 AB =/ BA
- 내적 : row vector와 column vector의 곱
<br>  - 행렬 곱의 성질 : AB = 0 이더라도 A, B 어느것도 0이 아닐 수 있다.
- 







