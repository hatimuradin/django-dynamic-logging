from django.db import models
from logtest.utils import AutoNameEnum
from enum import auto
from django_enum_choices.fields import EnumChoiceField
from logtest.log_utils import enable_logger, disable_logger
import logging
from logtest.handlers import SplunkHandler

class HandlerTypes(AutoNameEnum):
    CONSOLE = auto()
    SPLUNK = auto()

# Create your models here.
class LoggerSettings(models.Model):
    enable = models.BooleanField(verbose_name="Enable", default=True)
    handler = EnumChoiceField(
        HandlerTypes, verbose_name="TradeType", default=HandlerTypes.CONSOLE
    )

    def save(self, *args, **kw):
        old = type(self).objects.get(pk=self.pk) if self.pk else None
        super(LoggerSettings, self).save(*args, **kw)
        if old and old.enable != self.enable: # Field has changed
            if self.enable == True:
                enable_logger()
            else:
                disable_logger()
        if old and old.handler != self.handler:
            logger = logging.getLogger()
            if self.handler == HandlerTypes.SPLUNK:
                logger.handlers = []
                hndl = SplunkHandler()
                hndl.setLevel(logging.DEBUG)
                formatter = logging.Formatter('[%(asctime)s] {%(module)s} [%(levelname)s] - %(message)s')
                hndl.setFormatter(formatter)
                logger.handlers.append(hndl)
            elif self.handler == HandlerTypes.CONSOLE:
                logger.handlers = []
                hndl = logging.StreamHandler()
                hndl.setLevel(logging.DEBUG)
                formatter = logging.Formatter('[%(asctime)s] {%(module)s} [%(levelname)s] - %(message)s')
                hndl.setFormatter(formatter)
                logger.handlers.append(hndl)   

        