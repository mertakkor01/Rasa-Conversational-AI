# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
import pandas as pd
from rasa_sdk import Action, Tracker
from rasa_sdk.events import Restarted, SlotSet, AllSlotsReset, FollowupAction
from rasa_sdk.executor import CollectingDispatcher

data = pd.read_csv('styles.csv', on_bad_lines='skip')

class ActionProvideInfoWithID(Action):

    def name(self) -> Text:
        return "action_provide_info_item"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        verify_order_number = int(tracker.get_slot("order_number"))
        
        # add if check, if number is in dataset
        if verify_order_number in data.id:
            dispatcher.utter_message(text="Your order with order number {} has been shipped and will be at your location soon. ".format(verify_order_number))
        
        else:
            dispatcher.utter_message(text="Sorry, I couldn't find your order number. Please check and start again.")
            return [Restarted()]
        
        return []


    class ActionVerifyStatusEmail(Action):

        def name(self) -> Text:
            return "action_verify_status_email"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
            verify_email = tracker.get_slot("email")
            
            dispatcher.utter_message(text="Your order saved to {} will be coming soon to your location.".format(verify_email))
            return []



# class AskForColourChange(Action):

#     def name(self) -> Text:
#         return "action_ask_for_colour_change"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         # verify_color = tracker.get_slot("color")
        
#         colourList = []
        

#         dispatcher.utter_message(text="Cheking your order with order number {} ".format(verify_oder_number))

        #return []

        

# class SetSlotsBefore(Action):

#     def name(self) -> Text:
#         return "action_setting_slots"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         intent = tracker.get_intent_of_latest_message()


#         if intent == "order_status_with_email":
#             return [SlotSet('email': 'mert.akkor@unitn.it')]
#         else:
#             return []


class ActionVerifyItem(Action):

    def name(self) -> Text:
        return "action_verify_item"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        verify_color = tracker.get_slot("color")
        verify_category = tracker.get_slot("category")
        

        dispatcher.utter_message(text="You mean, {} {}, right?".format(verify_color, verify_category))
        return []



class ActionVerifyRefundID(Action):

    def name(self) -> Text:
        return "action_verify_refund_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        verify_order_number = int(tracker.get_slot("order_number"))
        
        if verify_order_number in data.id:
            dispatcher.utter_message(text="Found your order with ID, {}, are you sure you want to start a refund?".format(verify_order_number))
        else:
            dispatcher.utter_message(text="Sorry, I couldn't find your order number. Please check and start again.")
            return [Restarted()]

        return []



class ActionVerifyRefundCategory(Action):

    def name(self) -> Text:
        return "action_verify_refund_category"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        verify_color = tracker.get_slot("color")
        verify_category = tracker.get_slot("category")
        

        dispatcher.utter_message(text="You want to refund your order, {} {}, right?".format(verify_color, verify_category))
        return []


class ActionVerifyRefundEmail(Action):

    def name(self) -> Text:
        return "action_verify_refund_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        verify_email = tracker.get_slot("email")
        
        dispatcher.utter_message(text="Found your order with email, {}, are you sure you want to start a refund?".format(verify_email))
        return []


class ActionRestart(Action):
    def name(self) -> Text:
        return "action_bye"

    def run(self, dispatcher, tracker, domain):
        # output a message saying that the conversation will now be
        # continued by a human.
        # pause tracker
        # undo last user interaction
        dispatcher.utter_message("Bye!")
        return [Restarted()]


class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_default_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker, # Intents, entities, conversations
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Something went wrong please start again!")

        # Revert user message which led to fallback.
        return [Restarted()]


# class ActionOrderNumber(Action):

#     def name(self) -> Text:
#         return "action_order_number"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         order_num = tracker.get_slot("order_number")
#         print(order_num)
#         dispatcher.utter_message("{} is this your order number?".format(order_num))
        
#         return []