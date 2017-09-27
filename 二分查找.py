# _*_ coding:utf-8 _*_
'''
���ַ���������Ҫ��1��˳��洢�ṹ��2�������Ѿ��ź���
˼�룺���ؼ��ֺ������м�λ�õ�Ԫ�رȽϣ������Ȳ��ҽ������������зָ�Ϊ�������У�����ؼ��ִ����м�Ԫ�أ��ں������в��ң�������ǰ�����в��ң��ظ�֮ǰ�Ĺ���ֱ���鵽�����߹ؼ��ֲ���������
�����Ҵ���log2n + 1
ƽ�����ҳ��� �Ƚϴ���/���г���
'''

def bsearch(alist,item):
    low = 0
    high = len(alist) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if alist[mid] > item:
            high = mid - 1
        elif alist[mid] < item:
            low = mid + 1
        else:
            return mid
    return

    
if __name__ == "__main__":
    alist = [2,5,12,15,26,35,66]
    print bsearch(alist,2)