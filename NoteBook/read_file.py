def read_file(fn, ext=None):
    "can be a url, will call pd read_.. for the ext type"
    import pandas as pd
    import os
    if(ext!=None):
        ft="." + ext
    else:
        st=os.path.splitext(fn)
        ft=st[-1]
    if ft=='.tsv':
        df=pd.read_csv(fn, sep='\t')
    elif ft=='.csv':
        df=pd.read_csv(fn)
    elif ft=='.txt':
        df=pd.read_csv(fn, sep='\n')
    else:
        df="no reader, can !wget the file"
    return df
