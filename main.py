import pandas as pd

# CSV 파일 읽기
df = pd.read_csv("inventory.csv")

# 총 재고 가치 계산
df["total_value"] = df["price"] * df["quantity"]

print("=== 전체 재고 데이터 ===")
print(df)

print("\n=== 카테고리별 총 재고 가치 ===")
category_summary = df.groupby("category")["total_value"].sum()
print(category_summary)

print("\n=== 재고 부족 상품 (10개 미만) ===")
low_stock = df[df["quantity"] < 10]
print(low_stock[["product_name", "category", "quantity"]])
