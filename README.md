# PoseNet_Ros_pkg

## PoseNet을 Ros2의 pkg로 만들기

Ros2에서 PoseNet을 실행하기 위해 test와 관련된 파일을 가져왔다.
- model.py
- test.py
- solver.py
- pose_utils.py

이미지를 Publish하기 위한 노드를 제작하였다.
posenet_publisher
publish 데이터로 image msg를 사용하였고, 이미지를 publish가능한 데이터로 바꾸기 위해 Cv_Bridge
