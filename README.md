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

│   └── run_pipeline.py     # Запуск всего пайплайна автоматически

│   └── setup_github.sh     # Скрипт для первоначальной настройки репозитория на GitHub

├── requirements.txt        # Все необходимые зависимости

└── README.md               # Этот файл

└── .gitignore              # Не переносим некоторые файлы в репозиторий на GitHub

---

## Установка

1. Клонируем репозиторий:

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

3. Устанавливаем зависимости
pip install -r requirements.txt

**Использование**
1.	Собрать и очистить данные, проанализировать рынок и увидеть дашборд:
python src/run_pipeline.py

2.	Запустить интерактивный дашборд отдельно (Streamlit):
streamlit run src/dashboard.py

3.	Настройка GitHub (однократно, после клонирования):
bash setup_github.sh

Особенности проекта
	•	Сбор вакансий через API arbeitnow.com.
	•	Очистка HTML в описаниях вакансий.
	•	Выделение навыков и подсчет их количества.
	•	Визуализация ключевых KPI и топ-10 навыков.
	•	Фильтры по странам, remote / on-site, должностям.
	•	Дашборд на Streamlit с интерактивными графиками и таблицами.

⸻

Примечания
	•	Файл data/raw_jobs.csv и data/clean_jobs.csv можно не пушить на GitHub (добавлен в .gitignore), если нужно только хранить код и визуализации.
	•	Скрипт run_pipeline.py собирает новые вакансии, очищает их, анализирует и выводит KPI в консоль.
	•	Для автоматического обновления проекта на GitHub можно добавить в run_pipeline.py команды git add, commit и push.

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
