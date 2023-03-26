import openai


class ChatGPT:
    """
    Simple class that exposes just one method "ask" that allow us to
    do question to ChatGPT
    """

    def __init__(self,
                 engine="text-davinci-003",  # Trained model selected,
                 api_key=""):
        """
        Create a ChatGPT object selecting the model we would like to use:
        Official documentation https://platform.openai.com/docs/api-reference/models/list

        To be able to call the ChatGPT API we need to create a API key

        Official documentation: https://platform.openai.com/docs/api-reference/authentication
        """
        self.engine = engine

        # If the API key is empty then warn the user and stops
        if api_key == "" or api_key is None:
            raise Exception(
                "Give me an API key!!!! (╯°□°）╯︵ ┻━┻. \n Docs: https://platform.openai.com/docs/api-reference/authentication")

        openai.api_key = api_key

    def ask(self,
            question: str,
            max_length_of_response: int = 2048) -> str:
        # Actually perform the question to the OpenAI API
        completion = openai.Completion.create(
            engine=self.engine,
            prompt=question,
            n=1,  # Nomber of responses we want to get
            max_tokens=max_length_of_response)

        return completion.choices[0].text
