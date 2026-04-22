import time

class HumaStudentMiner:
    def __init__(self, student_huma_id):
        self.huma_id = student_huma_id
        self.tuition_credits = 0.0
        self.pocket_huma = 0.0

    def study_and_mine(self):
        print(f"\n[STUDENT-NODE]: {self.huma_id} is active.")
        print("[STATUS]: Validating Mesh while accessing HumaNovel...")
        try:
            while True:
                time.sleep(10)
                # Earn 0.1 for Tuition and 0.05 for Personal use per cycle
                self.tuition_credits += 0.1
                self.pocket_huma += 0.05
                print(f" -> Tuition: {self.tuition_credits:.2f} | Wallet: {self.pocket_huma:.2f} HUMA", end="\r")
        except KeyboardInterrupt:
            print(f"\n[SAVED]: Session ended. Credits secured for {self.huma_id}")

if __name__ == "__main__":
    miner = HumaStudentMiner("huma_Student_Uni_001")
    miner.study_and_mine()
