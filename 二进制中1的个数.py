# _*_ coding:utf-8 _*_
'''
λ�Ʊ���������Ҫ�ߺܶ�
'''

def _count1(num):
    flag = 1
    cou = 0
    while flag < 65536:
        if (num & flag):
            cou += 1
        flag = flag << 1
    print cou
    

def _count2(num):
    '''
    һ������1������ԭ�� �� &���㣬�൱�ڰѸ����������ƣ����ұߵ�1���0
    '''
    cou = 0
    while num:
        num = num & (num-1)
        cou += 1
    print cou
   
   
def _count3(num):
    '''
    2�Ĵ��������������У�ֻ��һ��1
    '''
    if num & (num-1) == 0:
        print num
     
     

    
   
if __name__=="__main__":
    #_count1(110)
    #_count2(110)
    _count3(5)