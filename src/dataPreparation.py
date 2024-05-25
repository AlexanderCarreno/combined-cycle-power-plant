
def data_preparation(df):
    df = df.rename({'AT': 'T'}, axis=1)
    # df = df.drop(['RH'], axis=1)
    x = df[['T', 'V', 'AP', 'RH']]
    y = df['PE']
    return [x , y]