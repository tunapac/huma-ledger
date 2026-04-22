class HumaSocialLayer:
    def __init__(self):
        self.comments = []
        self.ratings = {} # {video_id: [stars]}

    def post_comment(self, user_id, video_id, text):
        # Verification happens here
        comment_entry = {"user": user_id, "video": video_id, "text": text, "verified": True}
        self.comments.append(comment_entry)
        print(f"\n[SOCIAL]: {user_id} commented on {video_id}: '{text[:20]}...'")

    def rate_content(self, user_id, video_id, stars):
        if 1 <= stars <= 5:
            if video_id not in self.ratings:
                self.ratings[video_id] = []
            self.ratings[video_id].append(stars)
            avg = sum(self.ratings[video_id]) / len(self.ratings[video_id])
            print(f"[RATING]: {video_id} is now rated {avg:.1f} stars by {len(self.ratings[video_id])} users.")

if __name__ == "__main__":
    social = HumaSocialLayer()
    social.post_comment("Sovereign_User_1", "Vid_Sat_National", "Great win today!")
    social.rate_content("Sovereign_User_1", "Vid_Sat_National", 5)
