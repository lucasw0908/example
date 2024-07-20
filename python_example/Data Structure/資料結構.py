school = [
    {
        "name": "CKHS",
        "club": [
            ("電研", "CKEISC"), 
            ("資訊", "CKINFOR")
        ]
    },
    {
        "name": "TFG",
        "club": [
            ("資訊", "FGISC")
        ]
    },
]

print(school[0]["club"][0][0]) # 電研
print(school[0]["club"][0][1]) # CKEISC

print(school[0]["club"][1][0]) # 資訊
print(school[0]["club"][1][1]) # CKINFOR

print(school[1]["club"][0][0]) # 資訊
print(school[1]["club"][0][1]) # FGISC