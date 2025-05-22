import datetime
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import ReminderScheduled

class ActionScheduleInactivityReminder(Action):
    """Agenda um lembrete para 2 minutos no futuro."""

    def name(self) -> Text:
        return "action_schedule_inactivity_reminder"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        return [
            ReminderScheduled(
                "EXTERNAL_inactivity_reminder",  # Intent que será acionada
                trigger_date_time=datetime.datetime.now()
                + datetime.timedelta(minutes=2),  # Daqui a 2 minutos
                name="inactivity_reminder",       # Nome do lembrete (útil para cancelar, mas não precisaremos)
                kill_on_user_message=True,       # IMPORTANTE: Cancela automaticamente se o usuário responder!
            )
        ]

class ActionReactToInactivityReminder(Action):
    """Envia a mensagem de inatividade quando o lembrete é acionado."""

    def name(self) -> Text:
        return "action_react_to_inactivity_reminder"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_inactivity_reminder")

        # Opcional: Você pode agendar outro lembrete aqui se quiser
        # return [ReminderScheduled(...)]

        return []