import re

def load_and_merge_one_trial(folder_path, prefix):

    df_acc = pd.read_csv(os.path.join(folder_path, f'{prefix}_accel.csv'))
    df_acc.columns = ['time', 'ax', 'ay', 'az']

    df_gyro = pd.read_csv(os.path.join(folder_path, f'{prefix}_gyro.csv'))
    df_gyro.columns = ['timeg', 'gx', 'gy', 'gz']

    df_orio = pd.read_csv(os.path.join(folder_path, f'{prefix}_orientation.csv'))
    df_orio.columns = ['timeo', 's', 'i', 'j', 'k']

    df = pd.concat([
        df_acc.reset_index(drop=True),
        df_gyro.drop(columns = ['timeg']).reset_index(drop=True),
        df_orio.drop(columns = ['timeo']).reset_index(drop = True)
        
    ], axis=1)

    # IMPORTANT: if you process with fall_dataset, remember to change this code below to
    # df_features = extract_peak(df)
    df_features = extract_window(df)
    df_features['trial'] = prefix
    
    return df_features


def load_all_file(folder_path):
    all_data = []

    prefixes = sorted({
        re.search(r'(U\d+_R\d+)', f).group(1)
        for f in os.listdir(folder_path)
        if f.endswith('.csv')
        and int(re.search(r'U(\d+)', f).group(1)) <= 12
        # 12 files for train and 3 files for test
    })

    for prefix in prefixes:
        all_data.append(load_and_merge_one_trial(folder_path, prefix))

    return pd.concat(all_data, ignore_index=True)
