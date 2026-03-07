# EU Job Market Intelligence

Интерактивный проект для анализа вакансий **Data Analysts / Data Specialists** в Европе.  
Проект собирает данные с открытого API, очищает их, анализирует ключевые навыки и визуализирует информацию на дашборде.

---

## Структура проекта
eu-job-market-intelligence/
├── data/
│   ├── raw_jobs.csv        # Сырые вакансии (не добавлены в GitHub)
│   └── clean_jobs.csv      # Очищенные вакансии (не добавлены в GitHub)
├── src/
│   ├── collect_data.py     # Сбор вакансий через API
│   ├── clean_jobs.py       # Очистка и нормализация данных
│   ├── analyze_jobs.py     # Анализ вакансий и навыков
│   └── dashboard.py        # Streamlit дашборд
├── requirements.txt        # Все необходимые зависимости
└── README.md               # Этот файл
---

## Установка

1. Клонируем репозиторий:

```bash
git clone https://github.com/<your-username>/eu-job-market-intelligence.git
cd eu-job-market-intelligence
2.	Создаем и активируем виртуальное окружение:
python3 -m venv venv
source venv/bin/activate  # Mac / Linux
# или
venv\Scripts\activate     # Windows

2.	Создаем и активируем виртуальное окружение:
python3 -m venv venv
source venv/bin/activate  # Mac / Linux
# или
venv\Scripts\activate     # Windows

3. Анализ вакансий
python src/analyze_jobs.py

4. Запуск дашборда
streamlit run src/dashboard.py
Дашборд откроется в браузере по адресу: http://localhost:8501.

Особенности проекта
	•	Сбор вакансий через API arbeitnow.com.
	•	Очистка HTML в описаниях вакансий.
	•	Выделение навыков и подсчет их количества.
	•	Визуализация ключевых KPI и топ-10 навыков.
	•	Фильтры по странам, remote / on-site, должностям.
	•	Дашборд на Streamlit с интерактивными графиками и таблицами.

⸻

Важно
	•	CSV-файлы с данными (raw_jobs.csv, clean_jobs.csv) не включены в репозиторий.
	•	Для воспроизведения проекта нужно сначала запустить collect_data.py и clean_jobs.py.

⸻

Технологии
	•	Python 3.13
	•	pandas
	•	requests
	•	Streamlit
	•	Altair
	•	collections (Counter)
	•	re, ast, os

⸻

Автор

Акимова Галина
GitHub￼ | LinkedIn￼
