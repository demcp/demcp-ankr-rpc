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

[Specify your license]

## Contributing

[Optional: Add contributing guidelines] 