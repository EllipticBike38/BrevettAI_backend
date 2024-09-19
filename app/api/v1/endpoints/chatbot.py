from fastapi import APIRouter
import requests #type: ignore
import json


router = APIRouter()


ai_url = "https://api.regolo.ai/v1/chat/completions"


@router.post("/get_patents")
def get_patents(
    patent: str
):
    query = f"""
    Sei un esperto di brevetti, non sai rispondere a domande che non riguardano i brevetti. 
    Quando ti arriva un messaggio da un utente, contatti le API di https://patents.google.com/ e controlli se esiste già un brevetto uguale o simile.
    Non restituire lo script con cui effettui la richiesta, ma solo il risultato di essa. 
    La richiesta è la seguente: {patent}
    """
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}
    data = {
    "model": "llama3.1:70b-instruct-q8_0",
    "messages": [
        {"role": "user", "content": query}
    ]
}
    response = requests.post(ai_url, headers=headers, data=json.dumps(data))

    response_json= response.json()
    return json.dumps(response_json["choices"][0]["message"]["content"])