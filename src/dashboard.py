import os
import pandas as pd
from collections import Counter
import streamlit as st
import ast  # безопасная альтернатива eval

# ---------------------------
# 0. Загружаем clean dataset
# ---------------------------
base_dir = os.path.dirname(os.path.dirname(__file__))
data_dir = os.path.join(base_dir, "data")
input_file = os.path.join(data_dir, "clean_jobs.csv")

df = pd.read_csv(input_file)

# ---------------------------
# 1. Заголовок
# ---------------------------
st.title("EU Job Market Intelligence")
st.write("Интерактивный дашборд вакансий Data Analysts / Data Specialists в Европе")

# ---------------------------
# 2. Сайдбар фильтров
# ---------------------------
st.sidebar.header("Фильтры")

# Фильтр по странам (несколько)
countries = df["location"].sort_values().unique()
selected_countries = st.sidebar.multiselect("Выберите страны", countries, default=countries[:5])

# Фильтр по remote
remote_filter = st.sidebar.selectbox("Remote?", ["All", "Remote", "On-site"])

# ---------------------------
# 3. Применяем фильтры
# ---------------------------
filtered_df = df[df["location"].isin(selected_countries)]

if remote_filter == "Remote":
    filtered_df = filtered_df[filtered_df["remote"] == True]
elif remote_filter == "On-site":
    filtered_df = filtered_df[filtered_df["remote"] == False]

# ---------------------------
# 3.1 Фильтр по должности
# ---------------------------
job_titles = sorted(filtered_df["title"].dropna().unique())

# Динамический default: первый элемент, если список не пуст
default_titles = [job_titles[0]] if len(job_titles) > 0 else []

selected_titles = st.sidebar.multiselect(
    "Выберите должность", job_titles, default=default_titles
)

if selected_titles:
    filtered_df = filtered_df[
        filtered_df["title"].str.lower().apply(lambda x: any(title.lower() in x for title in selected_titles))
    ]

# ---------------------------
# 4. KPI
# ---------------------------
st.subheader("KPI по выбранным фильтрам")

total_jobs = len(filtered_df)
percent_remote = round(filtered_df["remote"].mean() * 100, 1) if total_jobs > 0 else 0
avg_skills = filtered_df["skills_count"].mean() if total_jobs > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Всего вакансий", total_jobs)
col2.metric("% Remote", percent_remote)
col3.metric("Среднее навыков на вакансию", round(avg_skills, 2))

# ---------------------------
# 5. Топ-10 навыков
# ---------------------------
def parse_skills(skills_str):
    """Безопасно преобразует строку в список"""
    try:
        return ast.literal_eval(skills_str)
    except (ValueError, SyntaxError):
        return []

filtered_skills = [skill for sublist in filtered_df["skills"].apply(parse_skills) for skill in sublist]
skills_counter = Counter(filtered_skills)

if filtered_skills:
    top_skills_df = pd.DataFrame(skills_counter.most_common(10), columns=["Skill", "Count"])
    st.subheader("Топ-10 навыков")
    st.bar_chart(top_skills_df.set_index("Skill"))
else:
    st.write("Нет навыков для выбранных фильтров")

# ---------------------------
# 6. Таблица вакансий
# ---------------------------
st.subheader("Вакансии")
if not filtered_df.empty:
    st.dataframe(filtered_df[["title", "company_name", "location", "remote", "skills_count", "skills"]])
else:
    st.write("Нет вакансий для выбранных фильтров")