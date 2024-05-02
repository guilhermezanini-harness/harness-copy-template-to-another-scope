# Harness Template Copier

This Python script facilitates copying templates across different scopes (e.g., from organization scope to project scope and vice versa) in the Harness platform. It utilizes the `harness_py_sdk` to interact with the Harness API.

## Prerequisites

Before using this script, ensure you have the following:

- **Python 3 or Higher**: The script requires Python 3 or higher to run.
- **Harness Platform API Key**: You'll need an API key to authenticate with the Harness API. You can create a personal API key through your Harness account.
- **Account Identifier**: This identifier is necessary for authenticating with the Harness API. You can find this identifier in the URL when you're logged into your Harness account. For example, in the URL `https://app.harness.io/ng/account/Fak3Acc0unt1D/settings/overview`, the account identifier is `Fak3Acc0unt1D`.

## Installation

1. **Clone the Repository**

   Clone this repository to your local machine using:
   ```bash
   git clone <repository-url>
   ```

2. **Install Dependencies**

   Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Configure the script by setting the following environment variables in your system or in an `.env` file:

- `HARNESS_PLATFORM_API_KEY`: Your Harness API key.
- `HARNESS_ACCOUNT_IDENTIFIER`: The identifier for your Harness account.
- `HARNESS_TEMPLATE_REFERENCE`: (Optional) The reference identifier for the template.
- `HARNESS_PROJECT_IDENTIFIER`: (Optional) The project identifier where the template is located.
- `HARNESS_ORG_IDENTIFIER`: (Optional) The organization identifier where the template is located.
- `HARNESS_TEMPLATE_PROJECT_TARGET`: (Optional) The target project identifier for the template.
- `HARNESS_TEMPLATE_ORG_TARGET`: (Optional) The target organization identifier for the template.

## Usage

To run the script, use the following command:

```bash
python main.py
```

The script performs several actions:

1. Initializes the Harness service using the API key and account identifier.
2. Fetches the stable template YAML from the specified scope.
3. Modifies the template YAML according to the target scope.
4. Creates a new template pipeline with the modified template.
5. Saves the new template identifier to an environment variable `OUTPUT_TEMPLATE_IDENTIFIER`.

Ensure all required environment variables are properly set before executing the script.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests for any enhancements. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [Apache-2.0 License](LICENSE).
