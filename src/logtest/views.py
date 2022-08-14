from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    logger.critical(f"critical log...")
    logger.error(f"error log...")
    logger.warning(f"warning log...")
    logger.info(f"Info log...")
    logger.debug(f"debug log...")

    return HttpResponse('Hello World')