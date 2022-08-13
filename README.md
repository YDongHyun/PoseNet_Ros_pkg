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

posenet_pulisher 노드 제작완료.

data_loader.py실행시 pytorch가 잘 설치되있음에도 <No moudle named 'torch'> 오류 발생 
 - Anaconda가 설치되어있어 패키지가 anaconda3 evns에 설치되어 찾지못하였음.
 - Anaconda를 제거하
