// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract HumaLaunchpad {
    struct Project {
        string name;
        uint256 totalRaised;
        uint256 launchTime;
        bool active;
    }

    mapping(address => Project) public projects;
    uint256 public constant LISTING_FEE = 1000 * 10**18; // 1000 HUMA

    event ProjectLaunched(string name, address owner);

    function startupProject(string memory _name) public payable {
        // Logic: Require payment in $HUMA or $ATOM
        projects[msg.sender] = Project(_name, 0, block.timestamp, true);
        emit ProjectLaunched(_name, msg.sender);
    }

    // Vesting: Releases funds slowly to protect the Huma Economy
    function releaseFunds() public {
        require(projects[msg.sender].active, "No project found");
        // Only allow 10% release per month logic goes here
    }
}
