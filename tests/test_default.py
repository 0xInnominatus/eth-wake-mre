from wake.testing import *
from pytypes.contracts.Example import Example

# Print failing tx call trace
# def revert_handler(e: TransactionRevertedError):
#     if e.tx is not None:
#         print(e.tx.call_trace)

WETH = Address("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")

@chain.connect(
    accounts=2,
    chain_id=1,
    fork="https://eth-mainnet.g.alchemy.com/public")
# @on_revert(revert_handler)
def test_default():
    example = Example.deploy(WETH)
    assert example.weth() == WETH
