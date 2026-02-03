# This file uses for merging file adls and fall with ratio 5:1

ACTIVITY_TARGET = {
    "D05": 340, "D07": 320, "D09": 240, "D08": 220, # High Risk
    "D04": 250, "D06": 250, "D10": 250,             # Medium
    "D01": 150, "D02": 150, "D03": 200, "D11": 150  # Low
}

def physics_filter(df, activity_code):

    # Check unit of acc
    if len(df) == 0: return df
    mean_svm = df["acc_mean"].mean() 
    
    if mean_svm > 5.0: 
        # Đơn vị  m/s^2 (trọng lực ~ 9.8)
        SVM_THR = 12.0  # ~1.2g (Lọc bỏ đứng yên 9.8)
        JERK_THR = 150.0 
    else:
        # Đơn vị là g (trọng lực ~ 1.0)
        SVM_THR = 1.2
        JERK_THR = 15.0


    # 2. Giữ lại mẫu: Có va chạm mạnh 
    # Tuy nhiên: Với nhóm D01 (Walk), D02 (Jog) -> lọc nhẹ nhàng là đủ
    if activity_code in ["D01", "D02", "D03"]:
        svm_limit = SVM_THR * 0.9 
    else:
        svm_limit = SVM_THR

    df_filtered = df[
        (df["impact_max"] >= svm_limit) | 
        (df["jerk_max"] >= JERK_THR)
    ].reset_index(drop=True)
    
    return df_filtered

def cut_exact(df, target, seed=42):
    if len(df) <= target:
        return df
    return df.sample(n=target, random_state=seed)

def build_dataset(data_folder):
    dataset = []
    print(f"{'ACTIVITY':<10} | {'RAW':<6} | {'FILTER':<6} | {'FINAL':<6} | {'STATUS'}")
    print("-" * 50)

    for file in sorted(os.listdir(data_folder)): 
        if not file.endswith(".csv"):
            continue

        # Xử lý tên file: Lấy 3 ký tự đầu (D01.csv, F01.csv )
        activity_code = file[:3].upper() 
        
        path = os.path.join(data_folder, file)
        try:
            df = pd.read_csv(path)
        except:
            continue # Bỏ qua file lỗi

        df["activity_code"] = activity_code
        # ========== 1. XỬ LÝ FALL (F01-F08) ==========
        if activity_code.startswith("F"):
            dataset.append(df)
            print(f"{activity_code:<10} | {len(df):<6} | {'---':<6} | {len(df):<6} | KEEP FALL")
            continue

        # ========== 2. XỬ LÝ ADL (D01-D11) ==========
        if activity_code in ACTIVITY_TARGET:
            
            # Lọc đặc trưng vật lý 
            df_phys = physics_filter(df, activity_code)
            
            # Cắt số lượng vừa đủ ( tỉ lệ rf 5:1 )
            target_n = ACTIVITY_TARGET[activity_code]
            df_final = cut_exact(df_phys, target_n)

            dataset.append(df_final)
            print(f"{activity_code:<10} | {len(df):<6} | {len(df_phys):<6} | {len(df_final):<6} | ADL DONE")

    # Gộp dataset
    if len(dataset) > 0:
        final_df = pd.concat(dataset, ignore_index=True)
        return final_df
    else:
        return pd.DataFrame()
