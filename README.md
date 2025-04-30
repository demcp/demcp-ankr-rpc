# DEMCP-ANKR: Solana Blockchain API MCP Service

A FastMCP service that provides a comprehensive set of tools for interacting with the Solana blockchain. This MCP (Multi-Chain Protocol) service wraps Solana RPC API endpoints into easily accessible tools that can be integrated with AI assistants.

## Features

- Account information retrieval
- Token balance queries
- Program account management
- Block and transaction data access
- Epoch and network status information
- Stake account monitoring
- Supply and transaction statistics

## Prerequisites

- Python 3.10+
- Docker (for containerized deployment)
- Solana API endpoint URL

## Installation

### Using Docker

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd demcp-ankr
   ```

2. Build the Docker image:
   ```bash
   docker build -t demcp-ankr .
   ```

3. Run the container:
   ```bash
   docker run -p 8080:8080 -e SOLANA_API_URL="<your-solana-api-url>" demcp-ankr
   ```

### Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set the Solana API URL environment variable:
   ```bash
   export SOLANA_API_URL="<your-solana-api-url>"
   ```

3. Run the service:
   ```bash
   python src/ankr.py
   ```

## API Tools

The service exposes the following Solana blockchain interaction tools:

- `get_account_info` - Retrieve detailed information about a Solana account
- `get_account_balance` - Check the SOL balance of an account
- `get_program_accounts` - Query token accounts, NFT data, or program states
- `get_token_account_balance` - Get the balance of a specific token account
- `get_token_accounts_by_owner` - List all token accounts owned by an address
- `get_blocks` - Retrieve block information for specific slots
- `get_epoch_schedule` - Get epoch scheduling information
- `get_latest_blockhash` - Retrieve the latest block hash
- `get_minimum_balance_for_rent_exemption` - Calculate minimum balance for rent exemption
- `get_multiple_accounts` - Get information for multiple accounts simultaneously
- `get_slot` - Retrieve the current slot number
- `get_stake_activation` - Get stake activation information
- `get_supply` - Retrieve total supply information
- `get_transaction_count` - Get the total transaction count

## Environment Variables

- `SOLANA_API_URL`: Required. The Solana RPC API endpoint URL.

## Integration with AI Tools

This MCP service is designed to be integrated with AI assistants supporting the MCP protocol. The tools can be accessed through the standard MCP interface at port 8080.

## Security Notes

- Never expose your API keys in the source code
- Use environment variables for sensitive configuration
- Consider implementing rate limiting for production deployments

## License

MIT License

Copyright (c) 2023 DEMCP-ANKR

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contributing

We welcome contributions to the DEMCP-ANKR project!

### How to Contribute

1. **Fork the Repository**: Fork the repository to your GitHub account.

2. **Clone the Forked Repository**: Clone your fork locally on your machine.
   ```bash
   git clone https://github.com/yourusername/demcp-ankr.git
   cd demcp-ankr
   ```

3. **Create a Branch**: Create a new branch for your feature or bug fix.
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Changes**: Implement your changes, adhering to the existing code style.

5. **Test Your Changes**: Ensure your changes don't break existing functionality.

6. **Commit Your Changes**: Commit with a clear and descriptive message.
   ```bash
   git commit -m "Add feature: your feature description"
   ```

7. **Push to GitHub**: Push your changes to your forked repository.
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request**: Open a pull request from your fork to the main repository.

### Code Standards

- Follow PEP 8 style guidelines for Python code
- Write descriptive docstrings for all functions and classes
- Include appropriate error handling
- Add unit tests for new features

### Reporting Issues

If you find a bug or have a suggestion for improvement:

1. Check if the issue already exists in the GitHub issues
2. If not, create a new issue with a descriptive title and detailed information

Thank you for contributing to make DEMCP-ANKR better! 