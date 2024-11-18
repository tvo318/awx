# Generated by Django 4.2.10 on 2024-08-27 14:20

from django.db import migrations

SAML_AUTH_CONF_KEYS = [
    'SAML_AUTO_CREATE_OBJECTS',
    'SOCIAL_AUTH_SAML_CALLBACK_URL',
    'SOCIAL_AUTH_SAML_METADATA_URL',
    'SOCIAL_AUTH_SAML_SP_ENTITY_ID',
    'SOCIAL_AUTH_SAML_SP_PUBLIC_CERT',
    'SOCIAL_AUTH_SAML_SP_PRIVATE_KEY',
    'SOCIAL_AUTH_SAML_ORG_INFO',
    'SOCIAL_AUTH_SAML_TECHNICAL_CONTACT',
    'SOCIAL_AUTH_SAML_SUPPORT_CONTACT',
    'SOCIAL_AUTH_SAML_ENABLED_IDPS',
    'SOCIAL_AUTH_SAML_SECURITY_CONFIG',
    'SOCIAL_AUTH_SAML_SP_EXTRA',
    'SOCIAL_AUTH_SAML_EXTRA_DATA',
    'SOCIAL_AUTH_SAML_ORGANIZATION_MAP',
    'SOCIAL_AUTH_SAML_TEAM_MAP',
    'SOCIAL_AUTH_SAML_ORGANIZATION_ATTR',
    'SOCIAL_AUTH_SAML_TEAM_ATTR',
    'SOCIAL_AUTH_SAML_USER_FLAGS_BY_ATTR',
]


def remove_saml_auth_conf(apps, scheme_editor):
    setting = apps.get_model('conf', 'Setting')
    setting.objects.filter(key__in=SAML_AUTH_CONF_KEYS).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('conf', '0013_remove_radius_auth_conf'),
    ]

    operations = [
        migrations.RunPython(remove_saml_auth_conf),
    ]