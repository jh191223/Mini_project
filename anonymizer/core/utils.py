import pandas as pd
import os
import re

# 특정 값 마스킹 함수
def mask_value(value, mask_length=4):
    """값의 마지막 부분을 '*'로 마스킹"""
    value = str(value)
    if len(value) > mask_length:
        return value[:-mask_length] + '*' * mask_length
    return '*' * len(value)

# 전화번호 마스킹 함수 (가운데 자리 * 처리)
def mask_phone(value):
    """전화번호 가운데 4자리 * 처리"""
    value = str(value)
    return re.sub(r'(\d{3})-\d{4}-(\d{4})', r'\1-****-\2', value)

# 이메일 마스킹 함수 (사용자명만 * 처리)
def mask_email(value):
    """이메일 주소에서 @ 앞부분을 *로 마스킹"""
    value = str(value)
    match = re.match(r'([^@]+)@(.+)', value)
    if match:
        user, domain = match.groups()
        return '*' * len(user) + '@' + domain
    return '*' * len(value)  # 이메일 형식이 아니면 전체 마스킹

# 컬럼명을 영어로 변환하는 매핑
COLUMN_MAPPING = {
    '이름': 'name',
    '전화번호': 'phone',
    '이메일': 'email'
}

# CSV 비식별화 함수
def anonymize_csv(csv_file_path):
    # CSV 파일 읽기 (UTF-8로 인코딩)
    df = pd.read_csv(csv_file_path, encoding="utf-8-sig")

    # 컬럼명 변환 (한글 → 영어)
    df.rename(columns=COLUMN_MAPPING, inplace=True)

    # 컬럼명 소문자로 변환
    df.columns = df.columns.str.lower().str.strip()

    # 비식별화 수행
    if 'name' in df.columns:
        df['name'] = df['name'].apply(mask_value)
    if 'phone' in df.columns:
        df['phone'] = df['phone'].apply(mask_phone)
    if 'email' in df.columns:
        df['email'] = df['email'].apply(mask_email)  # ✅ 이메일 마스킹 변경됨!

    # 비식별화된 파일 저장 경로
    anonymized_file_path = csv_file_path.replace(".csv", "_anonymized.csv")
    df.to_csv(anonymized_file_path, index=False, encoding="utf-8-sig")

    # HTML 미리보기 반환
    return anonymized_file_path, df.head(5).to_html()
