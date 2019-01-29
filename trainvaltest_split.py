import numpy as np
import pandas as pd

def trainvaltest_split_by (df, dfstring, trainsize, valsize, seed = 42):
    uniqueids = df[dfstring].unique()
    np.random.RandomState(seed)
    np.random.shuffle(uniqueids)
    train_ids, val_ids, test_ids =  np.split(uniqueids, [int(trainsize*len(uniqueids)), int((trainsize+valsize)*len(uniqueids))])
    
    train_ids_pd = pd.DataFrame (train_ids)
    val_ids_pd = pd.DataFrame (val_ids)
    test_ids_pd = pd.DataFrame (test_ids)

    train_ids_pd.columns = [dfstring]
    val_ids_pd.columns = [dfstring]
    test_ids_pd.columns = [dfstring]
       
    train = df.merge(train_ids_pd , how = 'right', on = dfstring)
    val = df.merge(val_ids_pd , how = 'right', on = dfstring)
    test = df.merge(test_ids_pd , how = 'right', on = dfstring)

    return train, val, test
