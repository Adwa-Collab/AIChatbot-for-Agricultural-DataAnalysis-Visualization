from flask import request, jsonify
from redash.handlers.base import (
    BaseResource
)
import requests


class ChatResource(BaseResource):
    def post(self):
        try:
            value = request.get_json()
            question = value.get('question')

            question_answer = requests.post("https://116f-185-107-56-154.ngrok-free.app/api/chat", json={"message": question})


            if question_answer.status_code == 200:
                api_response = question_answer.json()
                answer = api_response.get("data")

                response_data = {"answer": answer}
                return jsonify(response_data), 200

            else:
                return jsonify({"error": "An error occurred"}), 500


        except Exception as error:
            return jsonify({"error": f"An error occurred {error}"}), 500
