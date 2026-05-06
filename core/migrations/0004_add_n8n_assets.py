from django.db import migrations


def create_n8n_assets(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectAsset = apps.get_model('core', 'ProjectAsset')

    try:
        proj = Project.objects.get(title__iexact='n8n Agent Workflow Project')
    except Project.DoesNotExist:
        # no project to attach assets to
        return

    static_base = '/static/portfolio/projects'

    assets = [
        {
            'title': 'n8n - Orchestrator Flow',
            'asset_type': 'image',
            'external_url': f"{static_base}/n8n-screenshot-1.svg",
            'caption': 'Orchestrator and intake flow',
            'order': 1,
        },
        {
            'title': 'n8n - Pricing & Scheduling',
            'asset_type': 'image',
            'external_url': f"{static_base}/n8n-screenshot-2.svg",
            'caption': 'Pricing lookup and webhook response',
            'order': 2,
        },
    ]

    for a in assets:
        ProjectAsset.objects.create(
            project=proj,
            title=a['title'],
            asset_type=a['asset_type'],
            external_url=a['external_url'],
            caption=a['caption'],
            order=a['order'],
        )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_project_biggest_challenge_project_business_problem_and_more'),
    ]

    operations = [
        migrations.RunPython(create_n8n_assets, migrations.RunPython.noop),
    ]
