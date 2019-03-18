# Debugger example

## Description

Demonstration of the debugger functionality.
Using contracts from OpenZeppelin (https://github.com/OpenZeppelin/openzeppelin-solidity), create a mintable ERC20 and debug its transactions.


## Instructions

Download and compile the contracts by running

```bash
./get_zeppelin_contracts.sh
solitude compile
```

Run ganache, deploy the contract and make some transactions

```bash
python token_launch.py
```

This script will deploy the contract, mint 1000 tokens, and transfer 100 tokens, printing the transaction hash.
Then it will wait, keeping ganache alive until terminated by Ctrl-C.

Open another terminal (in the same working directory) and run the debugger, with the transaction hash as argument.

```bash
solitude debug $TXHASH
```

The command-line debugger provides a gdb-like interface for debugging.
If you are **debugging the mint transaction** (the first one), you can set a breakpoint on the the '_mint' function and then resume the execution.

```
break _mint
continue
```

When the _mint function is found, you can see the call stack and function parameters with the backtrace command

```
backtrace
```

You can step a few instructions forward with `next`, until variable `_totalSupply` is increased, and show its new value

```
next
next
... (just hit Enter to repeat the last command)

info locals
print _totalSupply
```

Finally, `quit` the debugger

```
quit
```
