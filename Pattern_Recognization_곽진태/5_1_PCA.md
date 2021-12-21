## Linear Transformation (Non-Linear Demensional Reduction)
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
<br><img width="300" src="https://user-images.githubusercontent.com/89369520/141425347-84d88d9e-2e2e-4b5f-b234-8620754085ce.png">

### Shift by mean
- data에서 sample mean 빼기
<br><img width="200" src="https://user-images.githubusercontent.com/89369520/141425769-56324cb6-401e-49be-8012-f43086c22da9.png">
<br>PCA는 분산으로 이야기 하므로 data의 값이 얼마나 큰지는 의미없다. 0, 0으로 줌심을 옮겨주자.
<br><img width="300" src="https://user-images.githubusercontent.com/89369520/141425448-8b3f7227-cd49-4127-8f01-5436a4a7aff9.png">

### Derivation
- 차원 𝑚 < d를 갖는 부분공간 subspace W에서 D의 가장 정확한 표현을 찾는다.
- 행렬이란 선형변환이고, 하나의 벡터 공간을 선형적으로 다른 벡터 공간으로 mapping하는 기능을 가진다. 따라서 W에 있는 어떠한 벡터도 Σaiei로 쓸 수 있으며, x1은 Σa1iei 로 쓸 수 있다.(a11e1+a12e2이므로) 그래서 재구성에서 오는 오류의 합을 다음과 같이 쓸 수 있다.
<br><img width="300" src="https://user-images.githubusercontent.com/89369520/141438774-c5e81119-884e-45c3-863c-3a1c9dd046c7.png">
- 전체 에러는 다음과 같으며, 최소화 하는데 목적이 있다.
<br>여기서 S는 Covariance matrix에서 n-1이 곱해진 값이다.(분산에서 나눠진 n-1)
<br><img width="300" src="https://user-images.githubusercontent.com/89369520/141609581-c70b1527-4685-4275-9864-53a5b36f3b92.png">
- 앞쪽 data는 constant하므로, 전체 에러를 최소화하는 방법은 minus이후의 식을 maximization 하는 것이다. 식을 풀면 다음과 같은 해를 가진다.
<br><img width="150" src="https://user-images.githubusercontent.com/89369520/141609626-b2e1dd35-bb06-423c-bd79-5b1f54d68338.png">
- λi를 고유값(eigenvalue), ei를 고유벡터(eigenvector)라 한다.
- J를 minimization하기 위해서 λi값이 가장 큰 eigenvector를 골라야 한다.
<br><img width="400" src="https://user-images.githubusercontent.com/89369520/141609730-243fa545-73b5-4c63-bcf7-95c829619a10.png">
- First, Second Principle Component
<br><img width="300" src="https://user-images.githubusercontent.com/89369520/141609911-38572cd6-c3ee-4edd-9887-64605981090f.png">

### Approximation
- Eigenvector를 Eigenvalue 값의 내림차순으로 정렬한 뒤, 가장 큰 몇개만 가져와서 사용한다. (몇개만 가져와도 충분히 Variance를 담을 수 있다)
<br><img width="300" src="https://user-images.githubusercontent.com/89369520/141610008-c6040b6f-bca9-4c85-a27f-1104fce81bcb.png">

### PCA Steps 요약 !
-<img width="400" src="https://user-images.githubusercontent.com/89369520/141610052-88f73766-5d5d-4854-92b2-21cd5d07dbc2.png">

### 추가검색!
#### 고유벡터(Eigenvectors)와 주성분분석(PCA), 공분산 행렬(Covariance Matrix) 및 엔트로피(Entropy)
- https://m.blog.naver.com/dusrnwk/221683976650

1. 고유벡터
- 행렬이 작용하는 힘의 방향, 행렬을 분해(decomposition)하는데 사용된다.

2. 주성분분석, PCA
- 고차원 데이터에서 패턴을 찾는 도구
<br> 데이터를 인공신경망에 입력하기 전의 전처리과정에서 사용된다.
<br> 데이터의 범위를 재조정하고 평균으르 0으로 맞춰줌으로써 중요한 차원을 골라준다.
<br> = 중요한 feature를 골라준다

- 선형 회귀 분석과 유사하게 데이터에서 의미있는 선, 혹은 축을 찾는 과정
<br> 각각의 축은 하나의 주성분이며, 차원 수만큼 존재하는데 PCA는 어떤 축이 더 중요한지 우선순위를 구하는 것

- 첫번째 주성분은 분산이 가장 큰, 가장 긴 선
<br> 두번째 주성분은 첫번째 주성분으로 표현할 수 없는 축 중에서 가장 큰 분산

3. 공분산 행렬, Covariance Matrix
- 데이터의 분산과 공분산을 이용하여 만든 행렬
<br> 공분산이란, 2개 확률변수의 상관정도를 나타낸다.

- 정방 행렬의 값을 각 변수의 분산(대각성분) 공분산(대각성분 제외)로 채운 것이 바로 공분산 행렬
<br> 공분산 행렬에서 고유벡터와 고유값을 찾는 것은 데이터의 주성분을 찾는 것과 같다. 왜냐하면 고유벡터는 행렬이 어떤 방향으로 힘을 가하는지를 표현하는데, 이것은 데이터가 어떤 방향으로 분산이 큰지를 구하는 것과 같기 때문이다.

- 어떤 행렬 A에 대하여 벡터 v가 선형변환을 하는 경우, A의 고유벡터는 행렬 A가 벡터 v에 작용하는 힘의 방향을 나타낸다. 만일 이 행렬 A가 공분산 행렬의 경우에는 A의 고유벡터는 데이터가 어떤 방향으로 분산되어 있는지, 어떤 방향으로 힘이 작용하는지를 나타낸다.

- 고유값은 각 고유벡터에 해당하는 상관계수일 뿐이다. 우리가 다루는 행렬이 공분산행렬일 경우, 그 행렬의 고유값은 각 축에 대한 공분산 값이 된다. 그리고 고유값이 큰 순서대로 고유벡터를 정렬하면 결과적으로 중요한 순서대로 주성분을 구하는 것이 된다.

- 고차원 변수의 경우 시각화하기 어렵기 때문에 변수의 상관 관계를 파악하기 어렵다. 이럴때 공분산을 이용하면 각 변수의 값과 부호를 통해 변수의 관계를 쉽게 알 수 있다.
