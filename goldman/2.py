# Two opposite co -ordiantes of rectangle are given and check whether two triangle overlap each other or not.
"""Input:
L1=(0,2)
R1=(1,1)
L2=(-2,-3)
R2=(0,2)

Output:
0
    """
    
def is_overlap(l1, r1 , l2, r2):
    
    if l1[0] > r2[0] or r1[0] < l2[0]:
        return 0
    
    if l1[1] < r2[1] or r1[1] > l2[1]:
        return 0
    
    return 1 

if __name__ == "__main__":
    ordinates = list(map(int,input().split()))
    
    l1 = [ordinates[0],ordinates[1]]
    r1 = [ordinates[2],ordinates[3]]
    l2 = [ordinates[4],ordinates[5]]
    r2 = [ordinates[6],ordinates[7]]
    
    res = is_overlap(l1, r1, l2, r2)
    print(res)    
    