import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
df = pd.read_csv("inventory.csv")

# 총 재고 가치 계산
df["total_value"] = df["price"] * df["quantity"]

# 원본 데이터 따로 저장
df_all = df.copy()

print("=== 전체 재고 데이터 ===")
print(df)


# 전체 그래프 먼저 생성
all_summary = df_all.groupby("category")["total_value"].sum()

plt.figure(figsize=(8, 5))
all_summary.plot(kind="bar")
plt.title("Total Inventory Value (All Categories)")
plt.xlabel("Category")
plt.ylabel("Total Value")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("all_category_inventory_value.png")

# 파이 차트 생성 (전체 기준)
plt.figure(figsize=(6, 6))
all_summary.plot(kind="pie", autopct='%1.1f%%')
plt.title("Inventory Value Distribution by Category")
plt.ylabel("")  # y축 제거 (깔끔하게)

plt.savefig("category_distribution_pie.png")
plt.show()

# 사용자 입력 받기
threshold = int(input("\n재고 부족 기준 수량을 입력하세요 (예: 10): "))
category_input = input("특정 카테고리만 보려면 입력하세요 (없으면 Enter): ")

# 카테고리 필터 적용
if category_input:
    df = df[df["category"] == category_input]

# 카테고리별 재고 가치
print("\n=== 카테고리별 총 재고 가치 ===")
category_summary = df.groupby("category")["total_value"].sum()
print(category_summary)

# 재고 부족 상품
print("\n=== 재고 부족 상품 ===")
low_stock = df[df["quantity"] < threshold]

if low_stock.empty:
    print("모든 상품의 재고가 충분합니다.")
else:
    print("⚠️ 재고 부족 경고!")
    print(low_stock[["product_name", "category", "quantity"]])

# TOP 3 상품
print("\n=== 재고 가치 TOP 3 상품 ===")
top_items = df.sort_values(by="total_value", ascending=False).head(3)
print(top_items[["product_name", "category", "total_value"]])

# 그래프 생성
plt.figure(figsize=(8, 5))
category_summary.plot(kind="bar")
plt.title(f"{category_input if category_input else 'All'} Category Inventory Value")
plt.xlabel("Category")
plt.ylabel("Total Value")
plt.xticks(rotation=0)
plt.tight_layout()              

# 이미지 파일로 저장
plt.savefig("category_inventory_value.png")

# 그래프 화면에 표시
plt.show()
