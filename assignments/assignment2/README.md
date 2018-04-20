## Requirements

You will be building a set of REST APIs for a blockchain crypto-currency. In this assignment, you need to build APIs for the wallet and transaction entities using Flask framework. The data must be persisted into SQLite DB.

### What is wallet?

Wallet entity holds the individual account with a balance. The wallet can recevie and can transfer value from other wallets.

### 1. Create Wallet

POST /wallets

```js
{   
    "id" : "1233445665353", 
    "balance": 5,
    "coin_symbol": "FOO_COIN"
}
```

### 2. Get Wallet

GET /wallets/1233445665353

```js
{   
    "id" : "1233445665353", 
    "balance": 5,
    "coin_symbol": "FOO_COIN"
}
```

### 3. Delete Wallet

DELETE /wallets/1233445665353


### 4. Transfer Asset

POST /txns

```js
{
    "from_wallet": "2342452454", 
    "to_wallet": "1233445665353", 
    "amount": 10, 
    "time_stamp": "2018-12-13 14:46:33.942971", 
    "txn_hash": "5e0e3bd986d1ab40725cb9cae4c7a071eef71195074a4bcd240b37b862ace3f4"
}
```

### 5. Get Txn

GET /txns/5e0e3bd986d1ab40725cb9cae4c7a071eef71195074a4bcd240b37b862ace3f4

```js
{
    "status": "pending",
    "from_wallet": "2342452454", 
    "to_wallet": "1233445665353", 
    "amount": 10, 
    "time_stamp": "2018-12-13 14:46:33.942971", 
    "txn_hash": "5e0e3bd986d1ab40725cb9cae4c7a071eef71195074a4bcd240b37b862ace3f4"
}
```

