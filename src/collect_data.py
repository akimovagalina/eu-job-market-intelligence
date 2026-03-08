import requests
import pandas as pd
import os
import time

# Base API URL
base_url = "https://www.arbeitnow.com/api/job-board-api"

# Список для всех вакансий
all_jobs = []

# начинаем с первой страницы
page = 1

while True:

    print(f"Collecting page {page}...")

    url = f"{base_url}?page={page}"

    try:
        response = requests.get(f"{BASE_URL}?page={page}")

        # если API вернул ошибку — остановить сбор
        if response.status_code != 200:
            print(f"API stopped responding. Status code: {response.status_code}")
            break

        data = response.json()

        # если вакансий больше нет
        if not data["data"]:
            print("No more jobs found.")
            break

        for job in data["data"]:
            jobs.append(job)

        page += 1

        # небольшая пауза чтобы не словить лимит API
        time.sleep(1)

    except requests.exceptions.RequestException as e:
        print("Request error:", e)
        break

    except ValueError:
        print("Invalid JSON response")
        break

    jobs = data.get("data", [])

    # если вакансий больше нет — выходим
    if not jobs:
        print("No more jobs found.")
        break

    all_jobs.extend(jobs)

    page += 1

    # пауза чтобы не перегружать API
    time.sleep(2)

# создаём DataFrame
df = pd.DataFrame(all_jobs)

# путь к папке проекта
base_dir = os.path.dirname(os.path.dirname(__file__))
data_dir = os.path.join(base_dir, "data")

os.makedirs(data_dir, exist_ok=True)

output_file = os.path.join(data_dir, "raw_jobs.csv")

# сохраняем файл
df.to_csv(output_file, index=False)

print("Data successfully saved!")
print(f"Total jobs collected: {len(df)}")
