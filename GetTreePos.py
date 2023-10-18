from math import log


def get_pos(point=None,points=31):
    if point is None:
        return None
    pos = {}
    count = -1
    pointlist = get_pointlist(points)
    for x in point:
        count += 1
        if x == "null" : continue
        pos[x] = pointlist[count]
    return pos


# #这是一个5层二叉树的全坐标，从1开始一共31个Node
# pointlist = [                                                       (16,5)
             
#                                     ,(8,4)                                                              ,(24,4)

#                         ,(4,3)                          ,(12,3)                         ,(20,3)                         ,(28,3)

#                 ,(2,2)          ,(6,2)          ,(10,2)         ,(14,2)         ,(18,2)         ,(22,2)         ,(26,2)         ,(30,2)

#              ,(1,1) ,(3,1)  ,(5,1)  ,(7,1)  ,(9,1)  ,(11,1) ,(13,1) ,(15,1) ,(17,1) ,(19,1) ,(21,1) ,(23,1) ,(25,1) ,(27,1) ,(29,1) ,(31,1)]
#                           (2^4,logn)                      (2^4 + 2^5 * (2^0-1), 5)
#                       (2^3,logn - 1)                      (2^3 + 2^4 * (2^1-1), 4)
#                   (2^2,logn - 2)   (2^2 + 2^3,logn - 2)   (2^2 + 2^3 * (2^2-1), 3)
#               (2^1,2)            (2^1+2^2)                (2^1 + 2^2 * (2^3-1), 2)
#           (2^0 + 2*(1-1),1) (2^0+2*(2-1)) (2^0+2*2) ····  (2^0 + 2^1 * (2^4-1), 1)

def get_pointlist(points):
    deep = int(log(points,2))+1
    res  =[]
    for n in range(deep):
        for i in range(2**n):
            res.append((2**(deep-n-1)+2**(deep-n)*i,deep-n))
    return res