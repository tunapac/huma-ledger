// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract HumaBridgeVault {
    address public administrator;
    uint256 public totalLocked;

    event Deposit(address indexed user, uint256 amount, string humaAddress);

    constructor() {
        administrator = msg.sender; // Set to Tunapac Tier 2 Address
    }

    // This function locks REAL ETH into the vault for the Huma Mesh
    function lockFunds(string memory _humaAddress) public payable {
        require(msg.value > 0, "Must send ETH to lock");
        totalLocked += msg.value;
        emit Deposit(msg.sender, msg.value, _humaAddress);
    }
}
