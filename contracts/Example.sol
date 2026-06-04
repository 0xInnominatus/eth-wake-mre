// SPDX-License-Identifier: MIT
pragma solidity ^0.8.23;

contract Example
{
	address public weth;
	constructor(address _weth)
	{
		weth = _weth;
	}
}