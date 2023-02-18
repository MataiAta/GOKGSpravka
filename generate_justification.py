import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "text-davinci-002"

def generate_justification(project_name):
prompt = f"""СПРАВКА-ОБОСНОВАНИЕ к проекту постановления Кабинета Министров Кыргызской Республики "{project_name}".
1. Цель и задачи {generate_text("Цель и задачи")}
2. Описательная часть {generate_text("Описательная часть")}
3. Прогнозы возможных социальных, экономических, правовых, правозащитных, гендерных, экологических, коррупционных последствий {generate_text("Прогнозы возможных социальных, экономических, правовых, правозащитных, гендерных, экологических, коррупционных последствий")}
4. Информация о результатах общественного обсуждения {generate_text("Информация о результатах общественного обсуждения")}
5. Анализ соответствия проекта законодательству {generate_text("Анализ соответствия проекта законодательству")}
6. Информация о необходимости финансирования {generate_text("Информация о необходимости финансирования")}
7. Информация об анализе регулятивного воздействия {generate_text("Информация об анализе регулятивного воздействия")}
Министр ________________________ (подпись)"""

response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7
)

return response.choices[0].text
def generate_text(prompt):
model = openai.Completion.create(
engine=model_engine,
prompt=prompt,
max_tokens=1024,
n=1,
stop=None,
temperature=0.7
)
return model.choices[0].text
