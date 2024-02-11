import logging


from src.ticktick_api import TicktickApi
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.ExtensionCustomAction import \
    ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.RenderResultListAction import \
    RenderResultListAction
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction
from ulauncher.api.shared.event import (ItemEnterEvent, KeywordQueryEvent,
                                        PreferencesEvent,
                                        PreferencesUpdateEvent)
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem





logger = logging.getLogger(__name__)

class TicktickCaptureExtension(Extension):
    todoist_api = TicktickApi()

    def __init__(self):
        super(TicktickCaptureExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())
        self.subscribe(PreferencesEvent, PreferencesEventListener())
        self.subscribe(PreferencesUpdateEvent,
                       PreferencesUpdateEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension: TicktickCaptureExtension):
        text = event.get_argument() or None

        if not text:
            return RenderResultListAction([ExtensionResultItem(
                icon='images/icon.png',
                name='Type something to capture',
                on_enter=HideWindowAction()
            )])

        return RenderResultListAction([
            ExtensionResultItem(
                icon='images/icon.png',
                name='Capture "%s"' % text,
                description='Hit enter to capture this task in your inbox!',
                on_enter=ExtensionCustomAction(text, keep_app_open=True)
            )
        ])

class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension: TicktickCaptureExtension):
        task_name = event.get_data()
        logger.info("Capturing task: %s" % task_name)

        result = extension.todoist_api.add_task(task_name)

        if result:
            message = result
            logger.error(message)
            return RenderResultListAction([ExtensionResultItem(
                icon='images/icon.png',
                name=message,
                description='Press enter to dismiss',
                on_enter=HideWindowAction()
            )])

        message = "Task captured: %s" % task_name
        logger.info(message)
        return RenderResultListAction([ExtensionResultItem(
            icon='images/icon.png',
            name=message,
            description='Press enter to dismiss',
            on_enter=HideWindowAction()
        )])

class PreferencesEventListener(EventListener):
    def on_event(self, event, extension: TicktickCaptureExtension):
        extension.keyword = event.preferences["keyword"]
        extension.todoist_api.set_token(event.preferences["api_token"])

class PreferencesUpdateEventListener(EventListener):
    def on_event(self, event, extension: TicktickCaptureExtension):
        if event.id == "api_token":
            extension.todoist_api.set_token(event.preferences["api_token"])

if __name__ == "__main__":
    TicktickCaptureExtension().run()
