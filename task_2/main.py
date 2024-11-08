import numpy as np
import unittest


departments = {
    'Engineering': 4,
    'Marketing': 3,
    'Finance': 5,
    'HR': 2,
    'Science': 4
}

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def calculate_department_mean_threat_score(threat_scores):

    return np.mean(threat_scores)

def calculate_aggregated_threat_score(department_scores, department_importances):

    weighted_scores = [
        mean_score * importance
        for mean_score, importance in zip(department_scores, department_importances)
    ]
    total_importance = sum(department_importances)
    aggregated_score = sum(weighted_scores) / total_importance
    return min(max(aggregated_score, 0), 90)

class TestAggregatedThreatScore(unittest.TestCase):
    def setUp(self):

        self.departments = departments
        self.department_importances = list(self.departments.values())

    def test_calculate_department_mean_threat_score(self):

        threat_scores = generate_random_data(45, 10, 100)
        mean_score = calculate_department_mean_threat_score(threat_scores)
        self.assertGreaterEqual(mean_score, 0)
        self.assertLessEqual(mean_score, 90)

    def test_calculate_aggregated_threat_score(self):
        mean_scores = [50, 52, 49, 48, 51]
        aggregated_score = calculate_aggregated_threat_score(mean_scores, self.department_importances)
        self.assertGreaterEqual(aggregated_score, 0)
        self.assertLessEqual(aggregated_score, 90)

    def test_high_importance_department_with_high_score(self):
        mean_scores = [30, 35, 85, 25, 30]
        aggregated_score = calculate_aggregated_threat_score(mean_scores, self.department_importances)
        self.assertGreaterEqual(aggregated_score, 0)
        self.assertLessEqual(aggregated_score, 90)

    def test_balanced_departments(self):
        mean_scores = [50, 52, 49, 51, 50]
        importances = [3, 3, 3, 3, 3]
        aggregated_score = calculate_aggregated_threat_score(mean_scores, importances)
        self.assertAlmostEqual(aggregated_score, 50, delta=5)

    def test_different_user_counts(self):
        engineering = generate_random_data(40, 10, 200)
        marketing = generate_random_data(40, 10, 50)
        finance = generate_random_data(40, 10, 150)
        hr = generate_random_data(40, 10, 10)
        science = generate_random_data(40, 10, 120)

        mean_scores = [
            calculate_department_mean_threat_score(engineering),
            calculate_department_mean_threat_score(marketing),
            calculate_department_mean_threat_score(finance),
            calculate_department_mean_threat_score(hr),
            calculate_department_mean_threat_score(science)
        ]

        aggregated_score = calculate_aggregated_threat_score(mean_scores, self.department_importances)
        self.assertGreaterEqual(aggregated_score, 0)
        self.assertLessEqual(aggregated_score, 90)

    def test_edge_case_low_and_high_scores(self):
        mean_scores = [10, 15, 85, 20, 12]
        aggregated_score = calculate_aggregated_threat_score(mean_scores, self.department_importances)
        self.assertGreaterEqual(aggregated_score, 0)
        self.assertLessEqual(aggregated_score, 90)

if __name__ == '__main__':
    unittest.main()
