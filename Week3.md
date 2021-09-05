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
<br> 각 x당 확률의 합 데이터가 어떤 분포로부터 나왔을 가능도.
<br> - 찾고자하는 파라미터 θ에 대하여 다음과 같이 편미분하고 그 값이 0이 되도록 하는 θ를 찾는 과정을 통해 likelihood 함수를 최대화 시켜줄 수 있는 θ를 찾을 수 있다.

## 11.수학적 개념 이해 - MLE 개념
### Likelihood
- Likelihood function
<br><img width="400" src="https://user-images.githubusercontent.com/89369520/132119445-c302027c-5050-4f58-947f-2b21f5675fb9.png">

- Maximum Likelihood Estimator / `MLE`
<br>Likelihood를 최대로 만드는 모수의 값
<br><img width="600" src="https://user-images.githubusercontent.com/89369520/132119608-e75b5e75-16d7-467d-baf8-150660edb7c4.png">
<br><img width="400" src="https://user-images.githubusercontent.com/89369520/132119513-53590a56-dd40-4a03-b520-c6da61509778.png">


