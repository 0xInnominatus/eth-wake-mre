// SPDX-License-Identifier: MIT
pragma solidity ^0.8.23;

import { ERC20 } from "./ERC20.sol";

contract Example
{
	string public name;

	constructor(ERC20 token)
	{
		name = token.name();
	}
}