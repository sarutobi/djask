# -*- coding: utf-8 -*-

import logging
from django.template.response import TemplateResponse

from crowdtask.models import Application

logger = logging.getLogger(__name__)

def apps_list(request):
    logger.debug("apps list requested from %s" % request.META['REMOTE_ADDR'])
    return TemplateResponse(request, 'apps_list.html',
        { 'apps': Application.objects.all(),
        }
    )
