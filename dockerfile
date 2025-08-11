FROM python:3.10-slim
ENV TOKEN='8369392797:AAHwTSC8JnwL8INDF-hOnuyzzKC3RqU_2wI'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py" ]