# Takes n dataframe and describes their columns

class MultiDfDescriptor():
    
    def __init__(self, *args):
        self.args = args
        
    def empty_values(self): 
        column = []
        rows = []
        n_columns = []
        empty_values = []
        distinct_values = []
        nan_values = []
        
        for idx, df in enumerate(self.args):
            rows.append('----')
            column.append(f'Df_{idx + 1}')
            empty_values.append('----')
            distinct_values.append('----')
            nan_values.append('----')
            n_columns.append('----')
            
            if isinstance(df, pd.DataFrame):
                for i in df.columns:
                    empty_values.append(df.loc[df[i]=='', i].count())
                    distinct_values.append(df[i].nunique())
                    column.append(i)
                    rows.append(df[i].shape[0])
                    n_columns.append(df.shape[1])
                    nan_values.append(df[i].isna().sum())
            else:
                print(f'Item is not a dataframe')
            
        empty_dic = {'Columns': column,
                     'N.Rows': rows,
                     'N.Columns' : n_columns,
                     'Distinct' : distinct_values,
                     'Empty':empty_values,
                     'Isna' : nan_values}
    
        return pd.DataFrame(empty_dic)
