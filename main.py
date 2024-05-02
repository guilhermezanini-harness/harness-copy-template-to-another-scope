import os
import yaml

from harness_py_sdk import sdk


def main():
    api_key = os.environ.get('HARNESS_PLATFORM_API_KEY')

    account_identifier = os.environ.get('HARNESS_ACCOUNT_IDENTIFIER')

    # Optional - Organization where the template is located
    template_reference = os.environ.get('HARNESS_TEMPLATE_REFERENCE', None)

    # Optional - Project where the template is located
    project_identifier = os.environ.get('HARNESS_PROJECT_IDENTIFIER', None)

    # Optional - Org where the template is located
    org_identifier = os.environ.get('HARNESS_ORG_IDENTIFIER', None)

    project_target_identifier = os.environ.get('HARNESS_TEMPLATE_PROJECT_TARGET', None)
    org_target_identifier = os.environ.get('HARNESS_TEMPLATE_ORG_TARGET', None)

    # Initialize the HarnessService with the API key and account identifier.
    harness_api = sdk.HarnessService(api_key, account_identifier)
    # Fetch the YAML for the template used in the pipeline.
    template_response = harness_api.fetch_stable_template_yaml(
        template_reference,
        org_identifier,
        
        project_identifier
    )

    template_yaml = yaml.safe_load(template_response['template']['yaml'])

    if(project_target_identifier):
        template_yaml['template']['projectIdentifier'] = project_target_identifier

    if(org_target_identifier):
        template_yaml['template']['orgIdentifier'] = org_target_identifier

    template_to_create_payload = {
        "template_yaml": yaml.dump(template_yaml),
        "is_stable": True
    }

    create_template_pipeline_response = harness_api.create_template_pipeline(
        template_to_create_payload,
        org_target_identifier,
        project_target_identifier
    )

    os.environ["OUTPUT_TEMPLATE_IDENTIFIER"] = create_template_pipeline_response['identifier']

main()