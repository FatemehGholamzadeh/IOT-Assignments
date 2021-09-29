import matplotlib.pyplot as plt
import numpy as np
list = [[["Gateway:1  initialLoRaBW:125"],[3447,2023,20755],[7307,4382,37789],[14168,6437,57863]] ,
            [["Gateway:1  initialLoRaBW:250"] ,[3466,1785,20687],[7243,3570,37325],[11448,538491,57913]] ,
              [["Gateway:1  initialLoRaBW:500"] ,[1,1679,20868],[1909,3189,37642],[5985,4842,57753]] ,
              [["Gateway:2  initialLoRaBW:125" ],[3560,2057,21084],[11023,4345,37375],[16060,6443,57761]] ,
              [["Gateway:2  initialLoRaBW:250" ],[6904,1791,20859],[14586,3582,37573],[18677,5384,57956]] ,
              [["Gateway:2  initialLoRaBW:500" ],[1,1687,21054],[5425,3199,37718],[9455,4734,57699]] ,
              [["Gateway:3  initialLoRaBW:125" ],[11381,2018,20704],[22806,4349,37406],[30942,6457,58205]] ,
              [["Gateway:3  initialLoRaBW:250" ],[3484,1673,20812],[18246,3557,37353],[31724,53388,58040]] ,
              [["Gateway:3  initialLoRaBW:500" ],[1,1667,20744],[7314,3175,37350],[9529,4952,58107]]
              ]

labels = ['5', '10', '15']
y_pos = np.arange(len(labels))


# for i in range(9):
#
#     rate = []
#     for j in range(1,4):
#       rate.append(float(list[i][j][0] / list[i][j][2]))
#
#     print(list[i][0])
#     plt.plot(y_pos,rate)
#     plt.xticks(y_pos,labels)
#     plt.xlabel('number of nodes')
#     plt.ylabel('Packets Recieved Rate')
#     plt.title(list[i][0])
#     plt.show()



for i in range(9):

    energy = []
    for j in range(1,4):
      energy.append(float(list[i][j][1] / list[i][j][0]))

    print(list[i][0])
    plt.pie(y_pos,energy)
    plt.xticks(y_pos,labels)
    plt.xlabel('number of nodes')
    plt.ylabel('Energy Consumed')
    plt.title(list[i][0])
    plt.show()