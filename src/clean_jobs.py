import pandas as pd
import os
import re

# путь к папке проекта
base_dir = os.path.dirname(os.path.dirname(__file__))
data_dir = os.path.join(base_dir, "data")

# файлы
input_file = os.path.join(data_dir, "raw_jobs.csv")
output_file = os.path.join(data_dir, "clean_jobs.csv")

# загружаем данные
df = pd.read_csv(input_file)

print(f"Raw jobs loaded: {len(df)}")

# ---------------------------
# 1. Удаляем дубликаты
# ---------------------------
df = df.drop_duplicates(subset=["slug"])

# ---------------------------
# 2. Очищаем HTML из description
# ---------------------------
def remove_html(text):
    if pd.isna(text):
        return text
    clean = re.sub("<.*?>", "", text)
    return clean

df["description_clean"] = df["description"].apply(remove_html)

# ---------------------------
# 3. Нормализуем remote
# ---------------------------
df["remote"] = df["remote"].fillna(False)

# ---------------------------
# 4. Создаем список навыков
# ---------------------------

skills_list = [
    "python",
    "sql",
    "aws",
    "docker",
    "kubernetes",
    "spark",
    "airflow",
    "tableau",
    "power bi",
    "excel",
    "pandas",
    "numpy",
    "scala",
    "java",
    "git"
]

def extract_skills(text):

    if pd.isna(text):
        return []

    text = text.lower()

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills

df["skills"] = df["description_clean"].apply(extract_skills)

# ---------------------------
# 5. Количество навыков
# ---------------------------
df["skills_count"] = df["skills"].apply(len)

# ---------------------------
# 6. Оставим нужные колонки
# ---------------------------

columns_to_keep = [
    "slug",
    "company_name",
    "title",
    "location",
    "remote",
    "created_at",
    "description_clean",
    "skills",
    "skills_count"
]

df = df[columns_to_keep]

# ---------------------------
# 7. Сохраняем файл
# ---------------------------

df.to_csv(output_file, index=False)

print("Clean dataset saved!")
print(f"Total clean jobs: {len(df)}")