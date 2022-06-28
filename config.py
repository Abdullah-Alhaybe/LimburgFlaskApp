# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'MasterUser'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '6ced922b-3610-477f-8fe9-b007848501a2'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '3c0e3f6e-669e-4278-b912-f7cff843c4e1'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = ''
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '2454cd7c-e94a-4ab6-966e-b431286ce359'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = ''
    
    # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = 'Arbeidsmarktregiolimburg@daatonderzoek.nl'
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = 'SjZ0FQWYFNUCwSYL1gXE!'
