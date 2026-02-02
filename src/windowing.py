
def extract_window_to_second(data, window = 50):
    sample = []

    for i in range(0, len(data) - window + 1, window):
        window_data = data.iloc[i : i + window ]
        features = extract_features_window(window_data)
        sample.append(features)

    return pd.DataFrame(sample) 


def extract_peak_to_window(data, window = 25):
    data['svm'] = np.sqrt(data['ax']**2 + data['ay']**2 + data['az']**2)
    peak_index = data['svm'].idxmax()

    sample = []
    
    for shift in range(-2, 3):
        center = peak_index + shift
        start = center - window
        end   = center + window

        if start < 0 or end >= len(data):
            continue

        window_event = data.iloc[start:end]
        if len(window_event) != 2 * window:
            continue
        
        features = extract_features_window(window_event)

        sample.append(features)
    return pd.DataFrame(sample)



