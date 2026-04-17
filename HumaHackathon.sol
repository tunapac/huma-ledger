// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract HumaHackathon {
    address public admin;
    uint256 public totalPrizePool;

    struct Submission {
        string projectHash;
        address developer;
        bool rewarded;
    }

    mapping(uint256 => Submission) public submissions;
    uint256 public submissionCount;

    constructor() {
        admin = msg.sender;
    }

    function submitProject(string memory _hash) public {
        submissionCount++;
        submissions[submissionCount] = Submission(_hash, msg.sender, false);
    }

    function rewardDeveloper(uint256 _id, uint256 _amount) public {
        require(msg.sender == admin, "Only Admin can reward");
        require(!submissions[_id].rewarded, "Already rewarded");
        // Logic to transfer $HUMA goes here
        submissions[_id].rewarded = true;
    }
}
