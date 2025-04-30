from typing import Any
import httpx
import json
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ankr-mcp",host="0.0.0.0",port=8080)
USER_AGENT = "DEMCP-ANKR/1.0"
API_URL = os.environ.get("SOLANA_API_URL")

async def make_request(url: str, method: str = "GET", payload: dict = None) -> dict[str, Any] | None:
    """Make a request to the API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json"
    }
    
    if method.upper() == "POST" and payload:
        headers["Content-Type"] = "application/json"
    
    async with httpx.AsyncClient() as client:
        try:
            if method.upper() == "GET":
                response = await client.get(url, headers=headers, timeout=30.0)
            elif method.upper() == "POST":
                response = await client.post(url, headers=headers, json=payload, timeout=30.0)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
                
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error making {method} request to {url}: {str(e)}")
            return None
        


@mcp.tool(
    description="Get information about a Solana account"
)
async def get_account_info(address: str) -> dict[str, Any]:
    """Get information about a Solana account.
    
    Args:
        address (str): The address of the Solana account to get info for.
    
    Returns:
        dict: Account information or error response.
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "getAccountInfo",
        "params": [
            address,
            {
                "encoding": "base58"
            }
        ],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch account information"}
    return response




@mcp.tool(
    description="Get the balance of a Solana account"
)
async def get_account_balance(address: str) -> dict[str, Any]:

    """
    Args:
        address (str): The address of the Solana account to get the balance of.
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "getBalance",
        "params": [address],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch account balance"}
    return response


@mcp.tool(
    description="Query token accounts, NFT data, or program states, commonly used for token management and DeFi applications."
)
async def get_program_accounts(program_id: str) -> dict[str, Any]:
    """
    Args:
        program_id (str): The program ID to query.
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "getProgramAccounts",
        "params": [program_id],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch program accounts"}
    return response
    
    
@mcp.tool(
    description="Get the balance of a Solana token account"
)
async def get_token_account_balance(token_account: str) -> dict[str, Any]:
    """Get the balance of a Solana token account
    
    Args:
        token_account (str): The address of the token account
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "getTokenAccountBalance",
        "params": [token_account],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch token account balance"}
    return response


@mcp.tool(
    description="Get all token accounts owned by a Solana address"
)
async def get_token_accounts_by_owner(owner: str) -> dict[str, Any]:
    """Get all token accounts owned by a Solana address
    
    Args:
        owner (str): The owner's address
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "getTokenAccountsByOwner",
        "params": [
            owner, 
            {"programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"},
            {"encoding": "jsonParsed"}
        ],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch token accounts"}
    return response




@mcp.tool(
    description="Get Solana block information"
)
async def get_blocks(start_slot: int, end_slot: int = None) -> dict[str, Any]:
    """Get Solana block information
    
    Args:
        start_slot (int): Starting slot
        end_slot (int, optional): Ending slot, if not provided, will query up to the latest slot
    """
    params = [start_slot]
    if end_slot is not None:
        params.append(end_slot)
        
    payload = {
        "jsonrpc": "2.0",
        "method": "getBlocks",
        "params": params,
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch blocks"}
    return response



@mcp.tool(
    description="Get Solana epoch schedule information"
)
async def get_epoch_schedule() -> dict[str, Any]:
    """Get Solana epoch schedule information"""
    payload = {
        "jsonrpc": "2.0",
        "method": "getEpochSchedule",
        "params": [],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch epoch schedule"}
    return response






@mcp.tool(
    description="Get Solana latest blockhash"
)
async def get_latest_blockhash() -> dict[str, Any]:
    """Get Solana latest blockhash"""
    payload = {
        "jsonrpc": "2.0",
        "method": "getLatestBlockhash",
        "params": [],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch latest blockhash"}
    return response


@mcp.tool(
    description="Get minimum balance required for rent exemption"
)
async def get_minimum_balance_for_rent_exemption(size: int) -> dict[str, Any]:
    """Get minimum balance required for rent exemption
    
    Args:
        size (int): Account data size (in bytes)
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "getMinimumBalanceForRentExemption",
        "params": [size],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch minimum balance for rent exemption"}
    return response


@mcp.tool(
    description="Get information for multiple Solana accounts"
)
async def get_multiple_accounts(pubkeys: list[str]) -> dict[str, Any]:
    """Get information for multiple Solana accounts
    
    Args:
        pubkeys (list[str]): List of account public keys
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "getMultipleAccounts",
        "params": [pubkeys, {"encoding": "jsonParsed"}],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch multiple accounts"}
    return response




@mcp.tool(
    description="Get current Solana slot"
)
async def get_slot() -> dict[str, Any]:
    """Get current Solana slot"""
    payload = {
        "jsonrpc": "2.0",
        "method": "getSlot",
        "params": [],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch current slot"}
    return response



@mcp.tool(
    description="Get Solana stake activation information"
)
async def get_stake_activation(stake_account: str) -> dict[str, Any]:
    """Get Solana stake activation information
    
    Args:
        stake_account (str): Stake account address
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "getStakeActivation",
        "params": [stake_account],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch stake activation"}
    return response


@mcp.tool(
    description="Get Solana supply information"
)
async def get_supply() -> dict[str, Any]:
    """Get Solana supply information"""
    payload = {
        "jsonrpc": "2.0",
        "method": "getSupply",
        "params": [{"excludeNonCirculatingAccountsList": False}],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch supply info"}
    return response


@mcp.tool(
    description="Get Solana transaction count"
)
async def get_transaction_count() -> dict[str, Any]:
    """Get Solana transaction count"""
    payload = {
        "jsonrpc": "2.0",
        "method": "getTransactionCount",
        "params": [],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch transaction count"}
    return response









if __name__ == "__main__":
    mcp.run(transport="sse")