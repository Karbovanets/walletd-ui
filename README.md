# Karbo Wallet UI

Desktop GUI for **walletd** (Payment Gate) — the Karbo RPC wallet service.

A lightweight Electron wrapper that provides a full-featured interface for managing wallets, sending transactions, and accessing all walletd RPC methods. No browser extensions, no CORS proxies — just a native app that talks directly to your walletd instance.

![Karbo Wallet UI](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

### Wallet Management
- **Multiple addresses** — create, import, delete, and manage multiple addresses in a single wallet
- **Full balance view** — available and locked balances per address and total
- **Address filtering** — search/filter addresses in the sidebar
- **Key export** — view secret keys and mnemonic seed for any address

### Transactions
- **Full transaction history** — paginated, sorted newest-first, with lazy block loading
- **Complete transaction details** — click any transaction to see all transfers, payment ID, extra field, confirmations, fee, unlock time
- **Full transaction hashes** — no truncation, monospace font, click-to-copy
- **Unconfirmed transactions** — clearly marked pending transactions
- **Send with Payment ID** — optional 64-char hex payment ID support
- **Configurable anonymity** — set mixin/ring size per transaction
- **Change address selection** — choose where change goes
- **Delayed transactions** — create, list, send, or delete delayed (unsigned) transactions

### Tools
- **Validate address** — check if an address is valid, view its public keys
- **Sign & verify messages** — cryptographic message signing and verification
- **Transaction proof** — generate proof of payment to a destination
- **Reserve proof** — prove balance ownership with optional message
- **Import by secret key** — import existing address via spend secret key
- **Import tracking address** — view-only address import via spend public key

### walletd Integration
- **Built-in launcher** — configure and launch walletd directly from the app
- **Structured settings** — GUI form for all walletd CLI options (no need to remember flags)
- **Command preview** — see the exact command before launching
- **Auto-launch** — optionally start walletd when the app opens
- **Connection settings** — point to any walletd instance (local or remote)
- **SSL & RPC auth support** — configure HTTPS and basic authentication

### UI
- **Dark theme** — designed for comfortable extended use
- **Live sync status** — synced/syncing/offline indicator with block height and peer count
- **Toast notifications** — non-intrusive feedback for all operations
- **Status bar** — block height, peers, version, minimum fee at a glance
- **Auto-polling** — balances and transactions refresh every 30 seconds

## Supported walletd RPC Methods

All 31 Payment Gate JSON RPC methods are supported:

| Category | Methods |
|---|---|
| **Wallet** | `save`, `reset`, `export`, `getStatus`, `getAddresses`, `getAddressesCount` |
| **Addresses** | `createAddress`, `createAddressList`, `deleteAddress`, `hasAddress`, `validateAddress` |
| **Keys** | `getViewKey`, `getSpendKeys`, `getMnemonicSeed` |
| **Balances** | `getBalance` |
| **Transactions** | `getTransactions`, `getTransaction`, `getTransactionHashes`, `getUnconfirmedTransactionHashes`, `sendTransaction` |
| **Delayed TX** | `createDelayedTransaction`, `getDelayedTransactionHashes`, `deleteDelayedTransaction`, `sendDelayedTransaction` |
| **Proofs** | `getTransactionSecretKey`, `getTransactionProof`, `getReserveProof` |
| **Signing** | `signMessage`, `verifyMessage` |
| **Blocks** | `getBlockHashes` |

## Installation

### Download

Grab the latest release for your platform from the [Releases](../../releases) page:

- **Windows**: `.exe` installer or portable `.exe`
- **Linux**: `.AppImage` or `.deb`
- **macOS**: `.dmg`

### Build from Source

Requires [Node.js](https://nodejs.org/) 18+.

```bash
git clone https://github.com/user/karbo-walletd-ui.git
cd karbo-walletd-ui
npm install
npm start          # run in development
npm run build      # build distributable for your platform
```

## Usage

### Quick Start

1. **Start walletd** externally or configure it in the app's Settings tab
2. **Launch Karbo Wallet UI**
3. The app connects to `http://127.0.0.1:16000/json_rpc` by default

### Connect to an Existing walletd

1. Go to the **Settings** tab
2. Enter the **walletd RPC URL** (e.g., `http://192.168.1.100:16000/json_rpc`)
3. Click **Save Settings**

### Launch walletd from the App

1. Go to the **Settings** tab
2. Click **Browse** and select your `walletd` executable
3. Fill in the wallet file, password, and other options
4. Click **Preview Command** to verify
5. Click **Launch walletd**

### walletd Launch Options

The Settings page provides a structured form for all walletd CLI parameters:

| Setting | Flag | Description |
|---|---|---|
| Container file | `-w` | Path to wallet file |
| Container password | `-p` | Wallet password |
| Generate container | `-g` | Create new wallet |
| Deterministic | `--deterministic` | Deterministic key generation |
| View/Spend key | `--view-key`, `--spend-key` | Import from keys |
| Mnemonic seed | `--mnemonic-seed` | Import from seed |
| Bind address | `--bind-address` | RPC listen address |
| Bind port | `--bind-port` | RPC listen port (default: 16000) |
| Node mode | `--local` | Local or remote node |
| Daemon address | `--daemon-address` | Remote daemon host |
| Daemon port | `--daemon-port` | Remote daemon port (default: 32348) |
| Testnet | `--testnet` | Use testnet |
| Log file | `--log-file` | Log output path |
| Log level | `--log-level` | 0 (FATAL) to 6 (TRACE) |
| SSL | `--rpc-ssl-enable` | Enable HTTPS |
| RPC auth | `--rpc-user`, `--rpc-password` | HTTP basic auth |

## Architecture

```
Karbo Wallet UI (Electron)
├── main.js        — Main process: window, RPC proxy, walletd launcher
├── preload.js     — Secure IPC bridge (context isolation)
├── index.html     — UI: all tabs, modals, and logic
└── package.json   — Build config for electron-builder
```

The app does **not** bundle walletd — it's a pure UI wrapper. Users point to their own walletd binary or connect to a running instance.

RPC calls go through Electron's main process (no CORS issues, no browser proxy needed). SSL and HTTP Basic Auth are handled transparently.

## Development

```bash
npm start              # launch in dev mode
npm run pack           # build unpacked app (for testing)
npm run build:win      # build Windows installer + portable
npm run build:linux    # build AppImage + deb
npm run build:mac      # build dmg
```

## License

MIT
