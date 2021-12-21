## SVM
### Support Vector Machine
- <img width="400" src="https://user-images.githubusercontent.com/89369520/146880653-a4de2726-a90b-4a40-82af-bb77b5850651.png">
- Maximize the margin = Better generalization

### SVM : Linearly Separable Case
- g(x) = wx + w0 # Linear discriminant
<br> if g(x(k)) > 0, Z(k) = +1 # class label
<br> if g(x(k)) < 0, Z(k) = -1
- SV는 separating hyperplane에 가장 가까운 vector samples입니다. (가장 분류하기 어려운 vector)
- g(x) = wx + w0
<br> = w( x+r*w/||w||) + w0
<br> = r||w|| (wx^a + w0 = 0)
<br> r = g(x)/||w||
- Maximize margin = 2/||w|| = b

### SVM : Non-linearly Separable Case
- <img width="400" src="https://user-images.githubusercontent.com/89369520/146882719-b49220d0-1ac9-4c96-9075-d52d3ea212f8.png">
#### Approach 1 : Slack Variables
 - 완벽한 linear hyperplane을 찾을 수 없으니, 변수를 추가, Margin을 변경하여 일부를 허용하자.
 <br> <img width="400" alt="스크린샷 2021-12-21 오후 3 34 46" src="https://user-images.githubusercontent.com/89369520/146882965-e8cc30e7-e5e1-450c-bc85-6fe4c7f51e45.png">

#### Accroach 2 : Non-linear Mapping
- 더 높은 차원으로 변형하게 되면, 선형으로 쉽게 분류가 가능한 경우가 많다. (가장 일반적인 technician)
<br> <img width="400" src="https://user-images.githubusercontent.com/89369520/146883122-4aacfa5e-b78a-4e11-a0e8-24e8075d6fa2.png">
- 문제를 완벽하게 이해하고 사용하는 경우는 적기 때문에, 많은 수의 feature를 사용하게 될 가능성이 높다.
<br> dimension까지 늘어난다면, 더 많은 feature로 더 오래걸리고, 부정확하고, data의 양도 늘어나면서 전반적인 cost가 올라간다.

#### Kernel trick
- dot product(inner, 내적)으로, 고차원 공간에서 작업을 수행할 필요가 없다.
- Kernel functions : Linear, Polynomial, Gaussian radial basis, Sigmoid

### SVM Summary
- Advantages
<br> – 멋진 이론에 근거합니다.
<br> – 우수한 generalization 특성을 갖고 있습니다.
<br> – Objective Func.에 로컬 최소값이 없습니다.
<br> – Non-linear Disc. func. 찾는 데 사용할 수 있습니다.
<br> – Classifier's complexity는 변환된 공간의 차원성보다는 SV 수로 특징지어집니다.
- Disadvantages
<br> – 다른 방법보다 느린 경향이 있습니다.
<br> – 2차 프로그래밍은 계산 비용이 많이 듭니다.
