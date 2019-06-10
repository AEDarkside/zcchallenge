#secrets and configs
subdomain = 'https://zcchallenge.zendesk.com/api/v2/'
api_url = 'tickets/'
content_type = '.json'
list_url = 'tickets.json?sort_by=id&sort_order=desc'
per_page = '&per_page='
ticket_limit = '25'
api_user = 'zc.chen0411@gmail.com'
api_pwd = 'TWE5NDA0MTE='

error_code = {
    '400': '\nError code: 400, Bad Request',
    '401': '\nError code: 401, Unauthorized Please check your username and password.',
    '403': '\nError code: 403, API has refused your request please check you have the nessacery permissions.',
    '404': '\nError code: 404, The resources you are requesting is not found.',
    '500': '\nError code: 500, Internal Server Error - Please contact Zendesk Support Team.',
    '502': '\nError code: 502, Bad Gateway - if problem continued please contact Zendesk Support Team.',
    '503': '\nError code: 503, Service Unavaliable - Please comeback later or contact Zendesk Support Team.',
    '504': '\nError code: 504, Gateway Timeout - please try it later.',
}

