# _*_ coding:utf-8 _*_
'''
����������һ�ֻ��ֽ�������
����˼���ǣ�
1���ȴ�������ȡ��һ������Ϊ��׼����һ���ǵ�һ������
2����������������ȫ�ŵ������ұߣ�С�ڻ����������ȫ�ŵ�������ߡ�
3���ٶ����������ظ��ڶ�����ֱ��������ֻ��һ������
�����л�������ʱ���ɱ��ð�������������Ѿ��ź���
ƽ��ʱ�临�Ӷ�O(nlogn)
'''

def swift(alist,left,right):
    low = left
    hight = right
    item = alist[left]
    while low < hight:
        #����������С��item����
        while alist[hight] > item and low < hight:
            hight -= 1
        #�ҵ��󻻵�item���
        if low < hight:
            alist[low] = alist[hight]
            low += 1
        #���������Ҵ���item����
        while alist[low] < item and low < hight:
            low += 1
        #�ҵ��󻻵�item�ұ�
        if low < hight:
            alist[hight] = alist[low]
            hight -= 1
    #item��λ
    alist[low] = item
    return low

    
def quick(alist):
    left = 0
    right = len(alist) - 1
    #��������
    if left < right:
        mid = swift(alist,left,right)
        swift(alist,left,mid-1)
        swift(alist,mid+1,right)
    return alist
    
    
if __name__ == "__main__":
    alist = [23,4,66,23,4,66,43,14,8,32,43,14,8,32]
    print quick(alist)

    