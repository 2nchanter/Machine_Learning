![12381](https://user-images.githubusercontent.com/89369520/131438143-40972c65-808b-49ca-9a35-0f6c5575eaf8.jpeg)

## 1-1 오리엔테이션

인공지능을 구현하는 기술인 머신러닝을 탐험하자. 기계를 학습시켜서 인간의 판단을 위임하는 기술.

`준비물 : 상상력, 절망하는 엔지니어`

공부와 문제의 관계. 공부는 왜 필요하지? 문제를 해결하기 위해.
- 문제가 크고 절망적인 나의 일이라면, 공부는 구원자가 될텐데,
- 해결하고자하는 문제가 작고 사소한 남의 일이라면, 공부자체가 문제를 키워서 우리를 억압하는 독재자가 된다.
- 문제의 크기가 클수록, 공부의 양이 작을 수록 좋다.

앞으로 문제는 크게 키우고, 최소한의 공부로 *공부의 효용을 뇌에 자주 증명*함으로써 쇼핑이나 게임처럼 즐기게 만들것이다.

> 설레이고 즐겁게!

## 1-2 머신러닝이란?

`결정 = 비교 + 선택`

무엇이 더 좋은지, 더 나쁜지 비교할 수 있다면, 선택은 기계적인 일이다.
<br> 기계가 스스로 비교할 수 있도록 만들자.

우리의 두뇌가 가진 판단능력을 확장해서, 우리의 두뇌가 더 빠르게 결정하게 돕는 기가막힌 도구.
> 나의 두뇌를 더욱 두뇌답게.

## 1-3 꿈

의지만으로는 습관을 이기기 쉽지 않다.
<br>하지만 습관의 지속적인 영향을 주는 환경이 바뀌면 습관은 서서히 바뀐다.
<br>환경은 습관을 이긴다. 의지만으로 습관을 바꾼다는건 무모한 일인것 같다.
<br>의지로 환경을 조정해서, 환경이 습관을 바꾸도록 우회전략을 짜보자.

## 1-4 궁리하는 습관

`일 = 꿈 + 능력`

일단 원리, 수학, 코딩은 빼고 일단 머신러닝의 사용자가 되어보자.
>'머신러닝을 사용하도록 궁리하는 상태'를 만들어보자.

## 1-5 Teachable, 1-6 모델

https://teachablemachine.withgoogle.com/

1. Class1 : 손톱 / 손톱을 꺠무는 이미지를 저장
<br>Class2 : 정상 / 정상 이미지 저장
<br>`컴퓨터가 학습할 데이터를 모았다!`

2. Train Model로 학습을 시킨 후 Preview를 보자.
<br>`'보여주지 않은 사진'임에도 기계가 판단하여 확률로 보여줌.`

3. 기계가 학습을 제대로 했을까?
<br>어떤 사진에는 정확하게 판단을 못한다.
<br>`학습에 사용한 자료가 부족/부정확 하기 때문이다.`
<br>1. 부족하기 때문에, 더 많은 사진을 더한다.
<br>2. 부정확하기 때문에, 몇몇 사진을 뺀다.

4. 사진을 제거하고 보자.
<br>`더 정확한 판단능력을 갖게 되었다.`

>사람이 경험과 공부를 통해 더욱 정교한 판단력을 갖게 되는 것과 비슷하다.

5. Export model로 다운로드 받을 수도 있다.
<br>압축을 풀면, 아래와 같은 파일들이 나오는데
- metadata.json
- model.json
- weights.bin
>이것들이 우리가 `추측`을 하기 위해 `학습`시킨 판단력, `Model` 이다, Machine Learning의 핵심이다.

## 1-7 머신러닝머신(?)

https://ml-app.yah.ac/ -> .json 파일 3종을 업로드 해서 앱으로 만들어보자.

'80% 이상일 때 alert 했으면 좋겠는데?','20% 이하는 정상이라고 띄웠으면.'

## 1-8 애플리케이션

>같은 것을 가리키는 다른 말.

- 애플리케이션, 'App'lication
<br>: 어떤 기능을 부품으로 해서 만든 완제품, 부품을 `응용` 한 것.
<br>-> 머신러닝의 모델이라는 부품을 응용해서 만들었으므로, 머신러닝 애플리케이션
- 프로그램, Program : `시간 순서`, 기계가 알아 듣도록 순서대로 적은 것.

## 1-9 모르면 마법, 알면 기술

사물인터넷 = 코딩 + 네트워크 + 전자공학 + 기계공학

- ex) 레모네이드 카페 사장.
<br>레몬을 얼마나 준비해야 할까?
<br>온도<->판매량 : 내일의 온도를 안다면, 내일 얼마나 준비해야 할지 알겠구나.
<br>현실은 날짜, 유행, 경쟁자 등등애도 영향을 받는다.
>머신러닝이 이 공식을 자동으로 만들어준다.

제목, 환경, 불만족, 꿈 / 금기! 기술적인 한계를 고려하지 말자.

https://bit.ly/ml-other-plan 참고해보자.
<br> https://bit.ly/ml-my-plan 공유해보자.


## 1-10 교양의 끝

교양으로 멈출 시,
<br> 직업으로 머신러닝을 수련한 동료를 찾으면 됩니다. -> 뛰어난 전문가가 많아져 있을 것입니다.
<br> 더욱 강력해져 있을 머신러닝 기계를 이용하면 됩니다. -> 더 쉽고, 강력한 머신러닝 기계가 있을 것입니다.
<br> 필요한 공부를 찾아서 하면 됩니다. -> 더 쉬운 공부법이 개발되어 있을 것입니다.

하지만, 직업으로 삼아볼까? 한다면 더 나아가야한다.

## 1-11 직업의 시작

>현실을 데이터화 할 수 있다면, 복잡한 현실에서 발견하기 어려운 통찰을 단순해진 데이터로부터 찾아낼 수 있다.

데이터 과학, data science : 데이터를 만들고, 만들어진 데이터를 이용하는 일.
<br>데이터 공학, data engineering : 데이터를 다루는 도구를 만들고,
도구를 관리하는 일

## 1-12 표

- 행(row)
```
개체(instance)
관측치(observed value)
기록(record)
사례(example)
경우(case)
```

- 열(column)
```
특성(feature)
속성(attribute)
변수(variable)
field
```

## 1-13 독립변수와 종속변수

독립변수 = 원인이 되는 열 (원인은 결과와 상관없이 '독립'적이기 때문에)
<br>종속변수 = 결과가 되는 열 (결과는 원인에 '종속'되어 발생했기 때문에)

독립변수와 종속변수의 관계를 인과관계라고 하며, 인과관계는 상관관계에 포함된다.

>특성들 사이의 관계를 파악하는 것은 매우 어렵고, 조심스럽게 접근해야 하는 작업이다.
<br>적은 수의 데이터를 가지고 상관관계가 있다고 단정하면 안된다.
<br>또한 나아가 서로 상관관계를 맺고 있을 뿐인데, 인과관계라고 단정해도 안된다.

[기획서 제출](https://docs.google.com/forms/d/e/1FAIpQLSfcJi6CJSVfiY6aDRfEZO-nRl99H4QCU7LKl_xWVlMzS3Rd6g/viewform) / 
[기획서 구경](https://docs.google.com/spreadsheets/d/1mdCb-xRYBAsAOeiC7miyQgcMqVzCpg_67OmfdGRvVAY/edit#gid=1783703437)

## 1-14 심리전

>같은 대상이라고 할지라도 그것을 도구로 생각하는 사람과
>공부거리로 생각하는 사람은 완전히 다른 마음을 갖게 됩니다.

## 1-15 머신러닝의 분류

지도학습, supervised learning -> 정답이 있는 문제를 해결하는 것
<br>비지도학습, supervised learning -> 무언가에 대한 관찰을 통해 새로운 의미나 관계를 밝혀내는 것
<br>강화학습, reinforcement learning -> 더 좋은 보상을 받기 위해서 수련하는 것

## 1-16 지도학습

독립변수와 종속변수로 이루어진 충분히 많은 데이터를 수집하여 훈련시켜 모델을 만듬.

## 1-17 회귀, 1-18 분류

가지고 있는 데이터에 `독립변수`와 `종속변수`가 있고, 종속변수가
<br>ㄴ 숫자일 때 -> 회귀, regression
<br>ㄴ 이름일 때 -> 분류, classification
<br>를 이용하면 된다.

## 1-19 군집화

>관측치(행)를 그룹핑 해주는 것

Q. 분류, classification vs 군집화, clustering
<br>A. 어떤 대상들을 구분해서 `그룹을 만드는 것`이 군집화라면,
<br>분류는 어떤 `대상이 어떤 그룹에 속하는지`를 판단하는 것이다.

## 1-20 연관규칙학습

>특성(열)을 그룹핑 해주는 것

Association rule learning (장바구니 학습!)
<br>추천해주는 프로그램.

## 1-21 비지도학습 정리

- 비지도학습 : 탐험적
<br>미지의 세계를 파악하며 탐험하듯, `데이터들의 성격을 파악`하는 것이 목적
<br>독립변수나 종속변수의 구분이 중요하지 않으며, `데이터만 있으면` 된다.

- 지도학습 : 역사적
<br>과거의 원인과 결과를 바탕으로 미래에 `어떤 결과를 초래하는지 추측`하는 것이 목적
<br>원인인 `독립변수`와 결과인 `종속변수`가 꼭 필요하다.

## 1-22 강화학습

reinforcement learning

지도학습은 배움을 통해 발전하는데, 강화학습은 경험을 통해 발전한다.
```
게임 -> 환경, environment
상태 -> 상태, state
상/벌 -> 보상, reward
행동 -> 행동, action
게이머 -> 에이전트, agent
판단력 -> 정책, policy
```
`환경``상태`에 따라 더 많은 `보상`을 받을 수 있는 `행동`을 `에이전트`가 할 수 있도록 하는 `정책`을 만드는 것.

## 1-23 머신러닝지도

<img width="801" alt="스크린샷 2021-08-31 오후 12 29 34" src="https://user-images.githubusercontent.com/89369520/131437203-9481c5cd-ce38-4de8-9e3d-fb6a2be2159d.png">

## 1-24 수업을 마치며

>어떤 분야에 어떤 부품이 있고, 그 부품이 언제 필요한지 안다면 그 사람은 그 분야의 생산자입니다.
<br>생산을 어렵고, 아무나 할 수 없는 것이라고 지레 짐작하지 말아주세요.
<br>철학적인 의미로서 머신러닝 엔지니어가 되신 것을 축하드립니다.
<br>현실적인 의미로서 머신러닝 엔지니어가 언젠가 되시길 응원합니다.
