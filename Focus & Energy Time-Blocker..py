from datetime import datetime

class FocusEnergyTracker:
    def __init__(self, target_hours=6.0):
        self.target_hours = target_hours
        self.sessions = []

    def get_current_energy_level(self):
        # Peak energy is assumed around 10 AM, dropping toward late evening
        current_hour = datetime.now().hour
        if 8 <= current_hour <= 12:
            return "⚡ Peak Energy (Great for deep, complex work)"
        elif 13 <= current_hour <= 16:
            return "☕ Post-Lunch Slump (Best for routine/admin tasks)"
        elif 17 <= current_hour <= 21:
            return "🌙 Evening Wind-down (Best for light review/planning)"
        else:
            return "💤 Low Energy / Off-Hours (Rest recommended)"

    def log_session(self, duration_minutes, task_name):
        self.sessions.append({"minutes": duration_minutes, "task": task_name})
        print(f"✓ Logged: {duration_minutes} mins on '{task_name}'")

    def show_dashboard(self):
        total_minutes = sum(s["minutes"] for s in self.sessions)
        total_hours = total_minutes / 60.0
        remaining_hours = max(0.0, self.target_hours - total_hours)
        progress = min(100.0, (total_hours / self.target_hours) * 100)

        # Dynamic break suggestion based on session fatigue
        if total_minutes > 0 and total_minutes % 90 == 0:
            break_advice = "🛑 Take a 15–20 minute walk/rest now (90-min cycle complete)."
        else:
            break_advice = "🟢 You are good to keep going or take a short 5-min stretch."

        print("\n" + "═" * 45)
        print("     🧠 FOCUS & ENERGY TIME-BLOCKER     ")
        print("═" * 45)
        print(f"🎯 Daily Target     : {self.target_hours:.1f} hours")
        print(f"⏱️ Focused Time Spent : {total_hours:.2f} hours ({progress:.0f}%)")
        print(f"⏳ Remaining Goal   : {remaining_hours:.2f} hours")
        print("─" * 45)
        print(f"🔋 Current Energy   : {self.get_current_energy_level()}")
        print(f"💡 Break Advisory   : {break_advice}")
        print("═" * 45)

# --- Example Usage ---
if __name__ == "__main__":
    tracker = FocusEnergyTracker(target_hours=5.0)

    # Log completed focus sessions
    tracker.log_session(45, "Python Coding Practice")
    tracker.log_session(45, "Reading Documentation")

    # Show dashboard and personalized energy advice
    tracker.show_dashboard()
