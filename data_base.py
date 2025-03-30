import pandas as pd
import random
import faker

# Faker 라이브러리로 가짜 데이터 생성
fake = faker.Faker()

# 200개의 더미 데이터 생성
data = []
for _ in range(200):
    name = fake.name()
    phone_number = fake.phone_number()
    email = fake.email()
    data.append([name, phone_number, email])

# DataFrame으로 변환
df = pd.DataFrame(data, columns=['이름', '전화번호', '이메일'])

# CSV 파일로 저장
csv_file_path = "dummy_data.csv"
df.to_csv(csv_file_path, index=False)

print(f"{csv_file_path} 파일이 생성되었습니다.")
