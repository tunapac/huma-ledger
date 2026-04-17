class HumaSovereignLedger {
    constructor() {
        this.totalSupply = 700000000;
        this.repaymentVault = 0.0;
        this.serviceCutPercentage = 0.15;
        this.facilityLimit = 250000000.0;
    }

    processTransaction(sender, receiver, amount) {
        const cutAmount = amount * this.serviceCutPercentage;
        const netTransfer = amount - cutAmount;
        this.repaymentVault += cutAmount;

        console.log(`\n--- Transaction Detail ---`);
        console.log(`Amount: ${amount} HUMA | Vault Cut: ${cutAmount} HUMA`);
        this.checkFacilityStatus();
    }

    checkFacilityStatus() {
        const progress = (this.repaymentVault / this.facilityLimit) * 100;
        console.log(`Progress: ${progress.toFixed(6)}%`);
    }
}

const ledger = new HumaSovereignLedger();
ledger.processTransaction("Alice", "Bob", 1000000);
