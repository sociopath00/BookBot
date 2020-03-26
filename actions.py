# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from helper.queries import fetch_data
from rasa_sdk.events import SlotSet, AllSlotsReset


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionBooksByAuthor(Action):

    def name(self) -> Text:
        return "action_books_by_author"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        author_name = next(tracker.get_latest_entity_values("author"), None)
        print(author_name)
        print("Hello")
        data = fetch_data("author", author_name, "name")
        dispatcher.utter_message(json_message={"msg": "Hey, Following books are written by {}".format(author_name),
                                 "data": data})
        return [AllSlotsReset()]


class ActionAuthorByBook(Action):

    def name(self) -> Text:
        return "action_author_by_book"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        book_name = next(tracker.get_latest_entity_values("book"), None)
        print(book_name)
        data = fetch_data("name", book_name, "author")
        dispatcher.utter_message(json_message={"msg": "Hey, Author of {} is {}".format(book_name, data[0]),
                                 "data": data})
        return [AllSlotsReset()]
