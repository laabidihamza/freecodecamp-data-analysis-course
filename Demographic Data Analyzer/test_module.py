from demographic_data_analyzer import analyze_demographic_data

result = analyze_demographic_data()
for key, value in result.items():
    print(f"{key}: {value}")
