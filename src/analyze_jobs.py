import os
import pandas as pd
from collections import Counter

# ---------------------------
# 0. Путь к clean_jobs.csv
# ---------------------------
# Берём корень проекта (на уровень выше src)
base_dir = os.path.dirname(os.path.dirname(__file__))
data_dir = os.path.join(base_dir, "data")
input_file = os.path.join(data_dir, "clean_jobs.csv")

# ---------------------------
# 1. Загружаем данные
# ---------------------------
df = pd.read_csv(input_file)
print(f"Всего вакансий: {len(df)}\n")

# ---------------------------
# 2. Кол-во вакансий по странам
# ---------------------------
jobs_by_country = df["location"].value_counts()
print("Топ-10 стран по количеству вакансий:")
print(jobs_by_country.head(10))
print("\n")

# ---------------------------
# 3. Доля Remote / On-site
# ---------------------------
remote_counts = df["remote"].value_counts(normalize=True) * 100
print("Процент вакансий Remote vs On-site:")
print(remote_counts)
print("\n")

# ---------------------------
# 4. Топ-скиллы
# ---------------------------
# Колонка skills хранит списки навыков в виде строки, преобразуем в список
df["skills_list"] = df["skills"].apply(lambda x: eval(x) if pd.notna(x) else [])

# Собираем все навыки в один список
all_skills = [skill for sublist in df["skills_list"] for skill in sublist]
skills_counter = Counter(all_skills)

print("Топ-10 навыков:")
for skill, count in skills_counter.most_common(10):
    print(f"{skill}: {count}")
print("\n")

# ---------------------------
# 5. Среднее количество навыков на вакансию
# ---------------------------
avg_skills = df["skills_count"].mean()
print(f"Среднее количество навыков на вакансию: {avg_skills:.2f}\n")

# ---------------------------
# 6. KPI-блок
# ---------------------------
total_jobs = len(df)
percent_remote = round(remote_counts.get(True, 0), 1)

print("KPI:")
print(f"Всего вакансий: {total_jobs}")
print(f"% Remote: {percent_remote}")
print(f"Среднее навыков на вакансию: {avg_skills:.2f}")