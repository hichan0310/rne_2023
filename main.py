import numpy as np
import math
from math import pi, sin, cos

size = 4
conv_size = 2 * size + 1
# 위 : 0번
# 오른쪽 : 1번
# 아래 : 2번
# 왼쪽 : 3번

result = []


def getline(image):
    image = np.pad(image, ((size, size), (size, size)), 'constant', constant_values=0)
    # ************** 여기에서 초기 좌표, 초기 각도 알아내고 followline 호출해야 함 **************
    #                    추가로 result에 새 리스트 생성해서 초기 좌표 넣어야 함


def followline(image, grad, position):
    result[-1].append(position)
    conv = np.array([list(map(lambda x: x if abs(x) <= pi / 2 else 0,
                              list(map(lambda x: x if x < pi else x - 2 * pi,
                                       [(0 if x - size == 0 and y - size == 0
                                         else (
                                                  -pi / 2 if x - size == 0 and y - size > 0
                                                  else (
                                                      pi / 2 if x - size == 0 and y - size < 0
                                                      else (-math.atan(
                                                          (y - size) / (
                                                                  x - size)) if x - size > 0
                                                            else pi - math.atan(
                                                          (y - size) / (
                                                                  x - size)))))
                                              - grad + 4 * pi) % (2 * pi)
                                        for x in range(conv_size)])))) for y in
                     range(conv_size)])
    conv_result = image[position[0] - size:position[0] + size + 1, position[1] - size:position[1] + size + 1] * conv
    num, sum = 0, 0
    for x in conv_result:
        for y in x:
            if y != 0:
                num += 1
                sum += y
    if num == 0:
        exit()
    new_grad_difference = sum / num
    new_grad=grad + new_grad_difference
    new_position = (position[0] + cos(new_grad), position[1] + sin(new_grad))
    followline(image, new_grad, new_position)

