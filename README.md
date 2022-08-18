# PoseNet_Ros_pkg

## PoseNet을 Ros2의 pkg로 만들기

Ros2에서 PoseNet을 실행하기 위해 test와 관련된 파일을 가져왔다.
- model.py
- data_loader.py
- solver.py
- pose_utils.py

이미지를 Publish하기 위한 노드를 제작하였다.
posenet_publisher
publish 데이터로 image msg를 사용하였고, 이미지를 publish가능한 데이터로 바꾸기 위해 Cv_Bridge를 이용

## 8.12 

posenet_publisher 노드 제작완료.

data_loader.py실행시 pytorch가 잘 설치되있음에도 <No moudle named 'torch'> 오류 발생 
 - Anaconda가 설치되어있어 패키지가 anaconda3 evns에 설치되어 패키지를 찾지 못하는 오류.
 - Anaconda를 제거하여 오류 해결
 
## 8.13

posenet_publisher <-> subscriber 통신 구현
- subscriber node에서 posenet 실행 오류 (오류 해결중)
- 이미지 파일 통신 확인

## 8.16

posenet 실행시 data_loader를 못받는 오류 발생 
- data_loader 패키지에서 이미지를 읽지 못하는 오류, 코드를 수정하여 해결
- pos_out, ori_out 출력 확인

![image](https://user-images.githubusercontent.com/80799025/185359334-36c10185-ce62-4807-af68-fde62918fd84.png)


## 8.18
- posenet 이미지 publish시 image path를 입력받아오도록 설정
- posenet 결과 정상 출력 확인 및 기존 train파일의 라벨링값과 비교하여 오차확인, 예상된 오차범위내 오차 발생

![image](https://user-images.githubusercontent.com/80799025/185362564-8f43ac00-ea9c-410b-905a-04dd78622060.png)
