# Function to suggest a statistical test
def suggest_test(data_type, comparison_type):
    # Dictionary to map data type and comparison type to test
    tests = {
        ("parametric", "mean"): "t-test",
        ("parametric", "mean (more than two groups)"): "ANOVA",
        ("parametric", "proportion"): "z-test",
        ("parametric", "correlation"): "Pearson's correlation",
        ("parametric", "variance"): "F-test",
        ("non-parametric", "mean"): "Mann-Whitney U test",
         ("non-parametric", "mean (more than two groups)"): "Kruskal-Wallis test",
        ("non-parametric", "proportion"): "binomial test",
        ("non-parametric", "correlation"): "Spearman's rank correlation",
        ("non-parametric", "variance"): "Levene's test"
    }
    
    # Return the suggested test
    return tests[(data_type, comparison_type)]

# Ask the user about the data type and comparison type
data_type = input("Is your data parametric or non-parametric?\n")
# Ask the user about the comparison type
# Ask the user about the comparison type

ans2comp = ['mean', 'mean (more than two groups)', 'proportion', 'correlation', 'variance']

while True:
    print("What do you want to compare?")
    print("1. mean")
    print("2. mean (more than two groups)")
    print("3. proportion")
    print("4. correlation")
    print("5. variance")
    
    
    input_comparison_type = int(input("Enter the number of your choice: "))
    if 0  < input_comparison_type <= 5:
        comparison_type = ans2comp[input_comparison_type - 1]
        break
    else:
        print("That's not an option mate. Try again.")
        
    # if comparison_type == 1:
    #     comparison_type = "mean"
    #     break
    # elif comparison_type == 2:
    #     comparison_type = "mean (more than two groups)"
    #     break
    # elif comparison_type == 3:
    #     comparison_type = "proportion"
    #     break
    # elif comparison_type == 4:
    #     comparison_type = "correlation"
    #     break
    # elif comparison_type == 5:
    #     comparison_type = "variance"
    #     break
    # else:
    #     print("That's not an option mate. Try again.")

#Suggest a statistical test based on the answers
test = suggest_test(data_type, comparison_type)

#Print the suggested test
print(f"You should use the {test} test.")

class StatTestLookup:
    def __init__(self, tests):
        self.tests = tests
    
    def get_test(self, distribution, comparison_type):
        return self.tests[(distribution, comparison_type)]
    
    def add_test(self, distribution, comparison_type, test_name):
        self.tests[(distribution, comparison_type)] = test_name

tests = {
        ("parametric", "mean"): "t-test",
        ("parametric", "mean (more than two groups)"): "ANOVA",
        ("parametric", "correlation"): "Pearson's correlation",
        ("parametric", "variance"): "F-test",
        ("non-parametric", "mean"): "Mann-Whitney U test",
         ("non-parametric", "mean (more than two groups)"): "Kruskal-Wallis test",
        ("non-parametric", "proportion"): "binomial test",
        ("non-parametric", "correlation"): "Spearman's rank correlation",
        ("non-parametric", "variance"): "Levene's test"
    }

lookup = StatTestLookup(tests)
# print(type(lookup))
# Example usage
print(lookup.get_test("parametric", "mean"))  # Output: "t-test"
print(lookup.get_test("non-parametric", "correlation"))  # Output: "Spearman's rank correlation"

lookup.add_test("parametric","proportion", "z-test")
