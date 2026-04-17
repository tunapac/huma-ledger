// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract HumaAudit {
    function verifyProject(uint256 _supply, uint256 _liquidity) public pure returns (bool) {
        // Requirement: Liquidity must be at least 10% of total supply value
        if (_liquidity < (_supply / 10)) {
            return false;
        }
        return true;
    }
}
