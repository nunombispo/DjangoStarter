from decouple import config


def site_settings(request):
    return {
        'SITE_TITLE': config('SITE_TITLE', default='Django Starter'),
        'SITE_FOOTER_LINK': config('SITE_FOOTER_LINK', default='https://developer-service.io/'),
        'SITE_FOOTER_LINK_TITLE': config('SITE_FOOTER_LINK_TITLE', default='Developer Service'),
        'SITE_FOOTER_COPYRIGHT': config('SITE_FOOTER_COPYRIGHT', default='2023'),
        'SITE_FOOTER_TWITTER_LINK': config('SITE_FOOTER_TWITTER_LINK', default='https://twitter.com/DevAsService'),
    }
