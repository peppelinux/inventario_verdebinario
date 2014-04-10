from settings import MEDIA_URL, MEDIA_ROOT#, WEB_HOST
from datetime import datetime

def URLs(request):
        return {
                'MEDIA_URL': MEDIA_URL,
		'MEDIA_ROOT': MEDIA_ROOT,
		#'image_random' : RandomHeadSimple(),
		#'IMAGE_NOTIZIECAMPUS' : UltimoNotizieCampus(),
		#'WEB_HOST': WEB_HOST,
                }   


def DATEs(request):
        return {
                'TODAY': datetime.today(),
                }   
