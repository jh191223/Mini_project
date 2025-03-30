from utils import anonymize_text, anonymize_csv

print(anonymize_text("홍길동, 010-1234-5678, gilhong@gmail.com"))
# 출력: 홍**, 010-****-5678, g*****@gmail.com

# 샘플 CSV 데이터 비식별화 테스트
anonymized_file = anonymize_csv("sample.csv")
print(f"변환된 파일 저장 위치: {anonymized_file}")
