## ANN (Artificial Neural Networks, 인공신경망)
### Biological Inspiration
- 생물학적 신경계에서 영감을 받은 정보 처리 패러다임.
- 인간의 뇌를 모방하고 있으며, Input의 sum이 threshold를 넘어가면 다음 뉴런으로 이동하는 electrical spike를 보낸다.

### Perceptron
- 인공신경망의 기본 단위로, linear decision boundary를 학습한다.
- input의 weighted sum, Thresholding

### Neural Networks
- Multi-layer perceptrons : Input, Hidden, Output layer
<br> <img width="400" src="https://user-images.githubusercontent.com/89369520/144775332-7c5732e2-100d-48cd-925b-66ae97aa09da.png">
- 장점 : linear discriminant로 제한되지 않으며, Multiple class 분류 가능.
<br> 단점 : 단순하고 보장된 학습 절차가 없음. (Gradient descent, Backpropagaion)
- Feed Forward (->) : Prediction은 네트워크를 통해 전달되어 분류된다.
- Backpropagation (<-) : Training은 last to first layer로 진행된다.

### Training Procedure
- 목표 : 올바른 output을 얻기 위한 weight 수정
- 절차 : Error를 계산하고 각 weight가 error에 미치는 영향을 확인한 뒤 Weight 수정.
<br> Error = o - o* = predict - truth

### Gradient Descent
- Goal = minimize E(w), Error = weight input의 SSE
- 각 weight에서 Error에 미치는 영향을 편미분(partial derivative)으로 확인
- Gradient descent update rule
<br> <img width="400" src="https://user-images.githubusercontent.com/89369520/144777911-5eb49ed4-40a9-4439-873d-ec50da915809.png">
<br> <img width="400" src="https://user-images.githubusercontent.com/89369520/144778279-d70bb1e8-71e0-472a-9cbf-19424db16580.png">
- weight의 변화에 따른 E(w) 곡선에 편미분을 취하면 기울기를 얻을 수 있다.
<br> 여기서 ∇E(w)로 가장 가파르게 증가하는 방향을 알 수 있는데, 앞에 -를 붙여서 감소하는 방향으로 움직이자.
- n(∇E(w)) 값이 매우 작아질 때까지, 순차적으로 Error가 감소하는 반복적인 과정.
<br> <img width="400" src="https://user-images.githubusercontent.com/89369520/144778813-1ad732ac-eae3-42b4-8579-027ff25cae33.png">
- global minimum을 찾지 못할 수도 있다.
- n(에타)값이 너무 크면 solution을 찾지 못하고, 너무 작으면 cost가 커진다.

### Activation function
- 1, 0이면 편미분 자체가 불가하므로 사용(?)
<br> <img width="400" alt="스크린샷 2021-12-06 오전 11 49 17" src="https://user-images.githubusercontent.com/89369520/144779190-9a4c8fc5-3127-42b3-8415-bc3c3e5b8f96.png">

### ex)
- Single layer
<br> <img width="500" src="https://user-images.githubusercontent.com/89369520/144781055-106c2b15-8c46-4370-9aa1-53ebccfa50b0.png">
<br> <img width="500" src="https://user-images.githubusercontent.com/89369520/144781076-f66c0b89-c7e0-47c3-94e3-a3d3c6a626f3.png">
<br> <img width="500" src="https://user-images.githubusercontent.com/89369520/144781095-3a9c1d19-16ac-4dc0-9b3e-56eb9412ea40.png">
<br> <img width="500" src="https://user-images.githubusercontent.com/89369520/144781107-26401482-cbdc-4eff-ac71-4dbe71db659d.png">
<br> <img width="500" src="https://user-images.githubusercontent.com/89369520/144781123-88a5a521-7b87-4eb8-8767-5bd763b8f7cc.png">
- Multi layer
<br> <img width="500" src="https://user-images.githubusercontent.com/89369520/144781301-18ea5e44-12b6-4d19-b375-6a6716d53a87.png">
<br> <img width="500" src="https://user-images.githubusercontent.com/89369520/144781314-72f562ff-c25f-491a-8eeb-41f14c26b22b.png">

### Cross-entropy, Softmax
- Cross-entropy : 에러를 계산할 때 많이 사용하는 방법
<br> <img width="300" src="https://user-images.githubusercontent.com/89369520/144781630-1b624dd4-07fc-40c4-b8d4-4dc4a92be756.png">
- Softmax : 0~1 사이의 값으로 생각할 때 많이 사용하는 방법
<br> <img width="250" src="https://user-images.githubusercontent.com/89369520/144781643-1e00680c-bb79-41ce-b246-14ad53377aea.png">

### Epoch, Batch, Iteration
- Epoch : 전체 data를 사용한 training 횟수
- Batch : 한번에 사용한 분할된 data의 양 (전체 data를 한번에 다 쓸수 있는 경우는 거의 없다.)
- Iteration : 한번의 Epoch를 위해 몇번 training해야 하는지. (Batch가 결정)

### Monitor Error
- loss, Acc.
<br> <img width="400" alt="스크린샷 2021-12-06 오후 12 22 20" src="https://user-images.githubusercontent.com/89369520/144782020-00bb0a0c-be1d-47e8-a828-6e6a035552e9.png">

## CNN (convolutional Neural Network, 컨볼루션 신경망)
### Convolution
- ex)
<br> <img width="400" alt="스크린샷 2021-12-06 오후 12 25 58" src="https://user-images.githubusercontent.com/89369520/144782317-84cefa36-a34c-4ebd-a49e-65b34de104ba.png">
<br> <img width="400" alt="스크린샷 2021-12-06 오후 12 28 22" src="https://user-images.githubusercontent.com/89369520/144782563-6f8fd235-9ac7-47d5-a885-888630f6e5f3.png">

### Pooling Layer
- 이미지(또는 기능 표현)를 더 작고 관리하기 쉽게 만들기
- 영상의 공간 크기 축소 및 매개 변수, 계산량 감소를 목적
- Type : Max, Min, Avg, etc
<br> <img width="400" alt="스크린샷 2021-12-06 오후 12 30 39" src="https://user-images.githubusercontent.com/89369520/144782736-414c4b8e-f23a-4f15-808a-e50532565771.png">

### CNN
- ex)
<br> <img width="400" alt="스크린샷 2021-12-06 오후 12 41 55" src="https://user-images.githubusercontent.com/89369520/144783618-dcd926d5-c26f-4b7e-abee-461020d67651.png">

### Transfer Learning (전이학습)
- 모든 경우의 충분한 data set이 있지는 않아서, 다른 domain의 모델을 사용해보자.
- 자원이 풍부한 기존/학습된 지식을 활용하는 것을 목표로 한다.
- ImageNet : 1400만 이상의 손으로 주석을 단 대규모 시각적 데이터 세트 이미지(1000개 범주)
<br> 지난 수년간 이것을 기반으로 CNN model들이 개발됨.

## Summary
- ANN(Artificial Neural Network) : 인공 신경망
<br> 특징 : 여러 입력값을 받아서 일정 수준이 넘어가면 활성화되어 출력값을 내보냄
<br> 단점 : 학습 과정에서 파라미터 최적값을 찾기 어려움, overfitting 문제점 발생, 학습 시간이 느림

- DNN(Deep Neural Network) : 심층 신경망
<br> 특징 : 2개 이상의 은닉층 존재, ANN에 비해 더 적은 수의 유닛들만으로 복잡한 데이터 모델링 가능
<br> 단점 : 신경망이 복잡한 경우 시간이 오래 걸림, 결과가 일정하지 않을 수 있음, 가중치의 의미를 정확하게 해석하기 어렵기 때문에 결과 해석이 어려움

- CNN(Convolution Neural Network) : 합성곱 신경망
<br> 특징 : 정보 추출, 문장 분류, 얼굴인식 등 널리 사용, Convolution 과정으로 이미지를 특징 계산하고 Pooling 과정으로 이미지 특징 추출 Fully Connected layer을 통과하여 분류 작업된 후 결과 도출

- RNN(Recurrent Neural Network) : 순환 신경망
<br> 특징 : 내부의 순환 구조가 포함되어 있기 때문에 시간에 의존적이거나 순차적인 데이터(Sequential data) 학습에 활용, LSTM과 GRU 등으로 발전
