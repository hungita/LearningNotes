import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import StratifiedKFold

# 通过stacking获取新的特征，减少内存的同时，又能保留完整特征的信息
def getStackFeature(df_,seed_):
    skf = StratifiedKFold(n_splits=5,random_state=seed_,shuffle=True)
    train = df_.loc[train_index]
    test = df_.loc[test_index]
    train_user = pd.Series()
    test_user = pd.Series(0,index=list(range(test_x.shape[0])))
    for train_part_index,evals_index in skf.split(train,train_y):
        EVAL_RESULT = {}
        train_part = lgb.Dataset(train.loc[train_part_index],label=train_y.loc[train_part_index])
        evals = lgb.Dataset(train.loc[evals_index],label=train_y.loc[evals_index])
        bst = lgb.train(params_initial,train_part,
              num_boost_round=NBR, valid_sets=[train_part,evals],
              valid_names=['train','evals'],early_stopping_rounds=ESR,
              evals_result=EVAL_RESULT, verbose_eval=VBE)
        train_user = train_user.append(pd.Series(bst.predict(train.loc[evals_index]),index=evals_index))
        test_user = test_user+pd.Series(bst.predict(test))
    return train_user,test_user