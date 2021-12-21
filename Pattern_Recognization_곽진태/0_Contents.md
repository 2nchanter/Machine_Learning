
### Pattern_Recognization_곽진태

#### Lec1 : Fundamentals
- Fundamental
- Terminology
- How Pattern Recognition works?
<br> - `Design cycle`

#### Lec2 : Desicion Theory
- Bayesian Decision Theory
<br> - only prior, + posterior, `Bayes' Rule`
<br> - `Discriminant Function, Decison Boundary`, Gaussian Density
- Bayesian Networks
<br> - `Naive Bayesian Network`
- Performance Evaluation
<br> - Classification Errors
<br> - `ROC curve, AUC`

#### Lec3 : [SVM](https://github.com/2nchanter/Machine_Learning/blob/main/Pattern_Recognization_%EA%B3%BD%EC%A7%84%ED%83%9C/3_SVM.md#svm)
- Linear Discriminant Function
- `Support Vector Machine`
- SVM - Linearly Separable Case
- SVM - Non-linearly Separable Case
<br> - Slack Variables
<br> - Non-linear Mapping
<br> - XOR Problen (다시 듣기)

#### Lec4 : Feature Extraction
- `Statistical features`
<br> - Skewness, Kurtosis
- `Geometric features`
<br> - Compactness, Curvature, Diameter, B-box, Moments, Object Orientation
- `Texture features` (여기서부터 4강 다시)
<br> - Image Gradient, Edge Detection, Discrete Gradient, Operators, Sobel, Canny
- Gray Level Co-occurrence Matrix(GLCM)
- Fourier Transform
- Gabor filter
- Local Binary Pattern(LBP)
- 
#### Lec5 : Dimentionality Reduction
- [Dimentionality Reduction](https://github.com/2nchanter/Machine_Learning/blob/main/Pattern_Recognization_%EA%B3%BD%EC%A7%84%ED%83%9C/5_Dimensionality_Reduction.md#dimensionality-reduction-%EC%B0%A8%EC%9B%90-%EC%B6%95%EC%86%8C)
<br> - `Curse of dimensionality`
- [Feature Selection](https://github.com/2nchanter/Machine_Learning/blob/main/Pattern_Recognization_%EA%B3%BD%EC%A7%84%ED%83%9C/5_Dimensionality_Reduction.md#1-feature-selection-linear-dimensional-reduction)
<br> - Filter Method, `Wrapper Method`
<br> - Naive search, Sequence Forward Selection(SFS), SBS, Bidirectional Search(BDS), Plus-L Minus-R Selection(LRS), `SFFS`, `SFBS`
- [Linear Transformation](https://github.com/2nchanter/Machine_Learning/blob/main/Pattern_Recognization_%EA%B3%BD%EC%A7%84%ED%83%9C/5_Dimensionality_Reduction.md#2-linear-transformation-non-linear-demensional-reduction)
- [`Principal Component Analysis(PCA)`](https://github.com/2nchanter/Machine_Learning/blob/main/Pattern_Recognization_%EA%B3%BD%EC%A7%84%ED%83%9C/5_Dimensionality_Reduction.md#1-principal-component-analysis)

#### Lec6 : Unsupervised Learning
- [Partitioning Clustering](https://github.com/2nchanter/Machine_Learning/blob/main/Pattern_Recognization_%EA%B3%BD%EC%A7%84%ED%83%9C/6_Unsupervised_Learning.md#partitioning-clustering-%EB%B6%84%ED%95%A0-%EA%B5%B0%EC%A7%91%ED%99%94)
<br> - Clustering : Proximity measure, Object function, Algorithm
<br> - `K-means Clustering` : Sequence, local minimum
- [Hierarchical Clustering](https://github.com/2nchanter/Machine_Learning/blob/main/Pattern_Recognization_%EA%B3%BD%EC%A7%84%ED%83%9C/6_Unsupervised_Learning.md#hierarchical-clustering-%EA%B3%84%EC%B8%B5%EC%A0%81-%EA%B5%B0%EC%A7%91%ED%99%94)
<br> - Agglomerative, Divisive

#### Lec7 : ANN, CNN
- [ANN (Artificial Neural Networks)](https://github.com/2nchanter/Machine_Learning/blob/main/Pattern_Recognization_%EA%B3%BD%EC%A7%84%ED%83%9C/7_ANN_CNN.md#ann-artificial-neural-networks-%EC%9D%B8%EA%B3%B5%EC%8B%A0%EA%B2%BD%EB%A7%9D)
<br> - Biological Inspiration, Perceptrons, Neural Networks
<br> - Training Procedure, Gradient Descent, Activation Function ex) single layer, Multi layer
<br> - cross entropy, Epoch, Batch, Iteration
- [CNN (Convolutional Neural Networks)](https://github.com/2nchanter/Machine_Learning/blob/main/Pattern_Recognization_%EA%B3%BD%EC%A7%84%ED%83%9C/7_ANN_CNN.md#cnn-convolutional-neural-network-%EC%BB%A8%EB%B3%BC%EB%A3%A8%EC%85%98-%EC%8B%A0%EA%B2%BD%EB%A7%9D)
<br> - Convolution, Pooling layer, ex)
<br> - Transfer Learning, Summary
