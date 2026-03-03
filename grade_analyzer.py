#Task 1 — Process the Scores
def process_scores(students):
    averages = {}
    for name, scores in students.items():
        #  2 decimal tak round 
        avg = sum(scores) / len(scores)
        averages[name] = round(avg, 2)
    return averages

#Task 2 — Classify the Grades
def classify_grades(averages):
    results = {}
    
    A_grade = 90
    B_grade = 75
    C_grade = 60
    
    for name, avg in averages.items():
        if avg >= A_grade:
            grade = 'A'
        elif avg >= B_grade:
            grade = 'B'
        elif avg >= C_grade:
            grade = 'C'
        else:
            grade = 'F'
        results[name] = (avg, grade)
    return results

#Task 3 — Generate the Report
def generate_report(classified, passing_avg=70):
    print("===== Student Grade Report =====")
    passed_count = 0
    total_students = len(classified)

    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed_count += 1
        
        # Formatting for alignment
        print(f"{name:<10} | Avg: {avg:<5.2f} | Grade: {grade} | Status: {status}")

    print("================================")
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed_count}")
    print(f"Failed         : {total_students - passed_count}")
    
    return passed_count

# Main Block
if __name__ == "__main__":
    # Sample Data
    student_data = {
        "Alice": [85, 90, 78, 92],
        "Bob": [60, 65, 55, 70],
        "Clara": [95, 98, 92, 100]
    }

    # Sequence mein calls
    avg_dict = process_scores(student_data)
    classified_dict = classify_grades(avg_dict)
    total_passed = generate_report(classified_dict)