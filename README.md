# textract-api-dev

A dockerized web service extracting text from any document for development enviorment.

Use [textract](https://github.com/deanmalmgren/textract) to extract text and [flask](https://github.com/pallets/flask) to server requests.

## Useage

```bash
curl --form file=@test.docx http://127.0.0.1:5000/textract
```
