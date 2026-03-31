# 📊 Python Inventory Analysis / 재고 데이터 분석 프로젝트

## 🇺🇸 Overview
This is a beginner-level Python project using pandas to analyze inventory data.

The project reads a CSV file, processes the data, and performs basic analysis such as calculating total inventory value, grouping by category, and filtering low-stock items.

This project was inspired by my previous warehouse management system (WMS) experience, focusing on data handling and analysis.

---

## 🇰🇷 개요
이 프로젝트는 **pandas**를 활용하여 재고 데이터를 분석하는 Python 입문 프로젝트입니다.

CSV 파일을 읽어 데이터를 처리하고, 총 재고 가치 계산, 카테고리별 집계, 재고 부족 상품 필터링 등의 기능을 구현했습니다.

이전 WMS 프로젝트 경험을 바탕으로 데이터 처리 및 분석 흐름을 학습하는 것을 목표로 진행했습니다.

---

## 🚀 Features / 주요 기능

### 🇺🇸
- Load inventory data from CSV
- Calculate total inventory value (`price * quantity`)
- Group data by category
- Filter low-stock items

### 🇰🇷
- CSV 파일 기반 재고 데이터 로딩
- 총 재고 가치 계산 (`price * quantity`)
- 카테고리별 데이터 집계
- 재고 부족 상품 필터링

---

## 🛠 Tech Stack

- Python
- pandas

---

## 📂 Project Structure
python_study/
 ├── main.py
 ├── inventory.csv
 └── README.md

---

## 📌 Key Implementation / 핵심 구현
🇺🇸
	•	Used pandas DataFrame to process tabular data
	•	Applied column-based operations for calculations
	•	Used groupby() for aggregation
	•	Implemented conditional filtering

🇰🇷
	•	pandas DataFrame을 활용한 표 형태 데이터 처리
	•	컬럼 연산을 통한 데이터 계산
	•	groupby()를 활용한 집계 처리
	•	조건 기반 데이터 필터링 구현

 
 ---
 ## 💡 What I Learned / 배운 점
 🇺🇸
	•	Basic usage of pandas for data processing
	•	Understanding differences between SQL and Python-based data handling
	•	Structuring a simple data analysis workflow

🇰🇷
	•	pandas를 활용한 데이터 처리 기초
	•	SQL과 Python 기반 데이터 처리 방식의 차이 이해
	•	간단한 데이터 분석 흐름 구성 경험

---
## 🔜 Future Improvements / 향후 개선
🇺🇸
	•	Add data visualization using matplotlib
	•	Expand dataset for more realistic analysis

🇰🇷
	•	matplotlib을 활용한 시각화 기능 추가
	•	데이터 확장 및 분석 기능 고도화

---
## 📈 Visualization / 시각화

### Category-wise Total Inventory Value / 카테고리별 총 재고 가치
![Category Inventory Value](category_inventory_value.png)
