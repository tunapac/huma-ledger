// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract HumaListing {
    address public admin;
    uint256 public listingFee = 1000 * 10**18; // 1000 HUMA

    struct Project {
        string name;
        string website;
        bool isApproved;
    }

    mapping(address => Project) public projects;

    constructor() {
        admin = msg.sender;
    }

    function applyForListing(string memory _name, string memory _url) public payable {
        // In a real scenario, check for 1000 HUMA payment here
        projects[msg.sender] = Project(_name, _url, false);
    }

    function approveProject(address _projectAddress) public {
        require(msg.sender == admin, "Only Tier 2 Admin can approve");
        projects[_projectAddress].isApproved = true;
    }
}
