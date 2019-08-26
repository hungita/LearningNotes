import time
from sklearn.metrics import roc_auc_score


def evalsLoss(cols):
    print('Runing...')
    s = time.time()
    clf.fit(train_part_x[:,cols],train_part_y)
    ypre = clf.predict_proba(evals_x[:,cols])[:,1]
    print(time.time()-s,"s")
    return roc_auc_score(evals_y[0].values,ypre)
print('开始进行特征选择计算...')
all_num = int(len(se)/100)*100
print('共有',all_num,'个待计算特征')
loss = []
break_num = 0
for i in range(100,all_num,100):
    loss.append(evalsLoss(col[:i]))
    if loss[-1]>baseloss:
        best_num = i
        baseloss = loss[-1]
        break_num+=1
    print('前',i,'个特征的得分为',loss[-1],'而全量得分',baseloss)
    print('\n')
    if break_num==2:
        break
print('筛选出来最佳特征个数为',best_num,'这下子训练速度终于可以大大提升了')