import heapq

courses = [
    {
        "name": "Machine Learning",
        "interest": "AI",
        "difficulty": 9,
        "prerequisite": True,
        "probability": 0.95,
        "utility": 95
    },
    {
        "name": "Data Science",
        "interest": "AI",
        "difficulty": 7,
        "prerequisite": False,
        "probability": 0.90,
        "utility": 90
    },
    {
        "name": "Cyber Security",
        "interest": "Security",
        "difficulty": 8,
        "prerequisite": True,
        "probability": 0.85,
        "utility": 88
    },
    {
        "name": "Web Development",
        "interest": "Programming",
        "difficulty": 5,
        "prerequisite": False,
        "probability": 0.80,
        "utility": 82
    },
    {
        "name": "Cloud Computing",
        "interest": "Networking",
        "difficulty": 4,
        "prerequisite": False,
        "probability": 0.75,
        "utility": 78
    }
]

print("SMART COURSE RECOMMENDATION SYSTEM")

interest = input(
    "Enter your interest (AI/Security/Programming/Networking): "
)

skill = int(input("Enter your skill level (1-10): "))

prerequisite_input = input(
    "Completed prerequisites? (yes/no): "
)

prerequisite = prerequisite_input.lower() == "yes"

# Priority Queue
priority_queue = []

for course in courses:
    heuristic = abs(skill - course["difficulty"])

    # Fixed: Added course name to avoid dictionary comparison error
    heapq.heappush(
        priority_queue,
        (heuristic, course["name"], course)
    )

print("\nSEARCH PROCESS")

searched_courses = []

while priority_queue:
    score, name, course = heapq.heappop(priority_queue)

    print("Exploring Course ->", course["name"])

    searched_courses.append(course)

print("\nCONSTRAINT CHECKING")

valid_courses = []

for course in searched_courses:

    print("\nChecking Constraints for", course["name"])

    if course["interest"].lower() != interest.lower():
        print("Rejected -> Interest mismatch")
        continue

    print("Interest matched")

    if skill < course["difficulty"] - 2:
        print("Rejected -> Difficulty too high")
        continue

    print("Skill constraint satisfied")

    if course["prerequisite"] and not prerequisite:
        print("Rejected -> Prerequisite missing")
        continue

    print("Prerequisite satisfied")

    valid_courses.append(course)

print("\nPROBABILITY ANALYSIS")

for course in valid_courses:
    print(
        course["name"],
        "Success Probability =",
        course["probability"]
    )

print("\nDECISION MAKING")

best_course = None
best_utility = -1

for course in valid_courses:

    expected_utility = (
        course["utility"] * course["probability"]
    )

    print(
        course["name"],
        "Expected Utility =",
        expected_utility
    )

    if expected_utility > best_utility:
        best_utility = expected_utility
        best_course = course

print("\nFINAL RECOMMENDATION")

if best_course:

    print(
        "\nRecommended Course :",
        best_course["name"]
    )

    print("\nEXPLANATION")
    print("Reason 1 : Matches your interest")
    print("Reason 2 : Suitable for your skill level")
    print("Reason 3 : Passed prerequisite constraints")
    print("Reason 4 : High probability of success")
    print("Reason 5 : Highest expected utility")

else:
    print("No suitable course found")

print("\nSYSTEM COMPLETED")