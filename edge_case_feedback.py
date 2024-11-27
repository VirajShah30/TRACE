from typing import List, Dict, Any
import ast
import re

class EdgeCaseFeedback:
    def __init__(self, llm_model):
        self.llm_model = llm_model
        self.test_case_history = []
        
    def analyze_problem(self, problem_statement: str) -> List[str]:
        """Analyze problem statement to identify potential edge cases"""
        edge_conditions = []
        
        # Look for numerical bounds
        numerical_patterns = [
            r'(\d+)\s*(?:<=|>=|<|>)',  # Look for numerical comparisons
            r'between\s+(\d+)\s+and\s+(\d+)',  # Look for range specifications
            r'(?:maximum|minimum|max|min)\s+(\d+)'  # Look for extremes
        ]
        
        # Look for special input conditions
        special_conditions = [
            'empty',
            'null',
            'negative',
            'zero',
            'maximum',
            'minimum'
        ]
        
        # Generate edge cases based on patterns found
        for pattern in numerical_patterns:
            matches = re.finditer(pattern, problem_statement.lower())
            for match in matches:
                edge_conditions.extend(self._generate_boundary_tests(match))
                
        # Add special condition tests
        for condition in special_conditions:
            if condition in problem_statement.lower():
                edge_conditions.append(f"Test {condition} input case")
                
        return edge_conditions
    
    def generate_test_cases(self, problem_statement: str, generated_code: str) -> List[Dict[str, Any]]:
        """Generate specific test cases based on edge conditions"""
        edge_conditions = self.analyze_problem(problem_statement)
        test_cases = []
        
        for condition in edge_conditions:
            # Use the LLM to generate specific test inputs for each edge condition
            prompt = f"""
            For the following code and edge condition, generate a test case:
            
            Code:
            {generated_code}
            
            Edge Condition:
            {condition}
            
            Generate a test case in the format:
            Input: <input_value>
            Expected Output: <expected_output>
            """
            
            test_case = self._generate_test_case_with_llm(prompt)
            test_cases.append({
                'condition': condition,
                'test_case': test_case
            })
            
        return test_cases
    
    def evaluate_test_cases(self, generated_code: str, test_cases: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Evaluate code against generated test cases"""
        results = {
            'passed_cases': [],
            'failed_cases': [],
            'feedback': ''
        }
        
        for test_case in test_cases:
            try:
                # Create a safe execution environment
                local_dict = {}
                exec(generated_code, {'__builtins__': {}}, local_dict)
                
                # Execute test
                test_result = self._execute_test(local_dict, test_case['test_case'])
                
                if test_result['passed']:
                    results['passed_cases'].append(test_case)
                else:
                    results['failed_cases'].append({
                        **test_case,
                        'actual_output': test_result['actual_output']
                    })
            except Exception as e:
                results['failed_cases'].append({
                    **test_case,
                    'error': str(e)
                })
        
        # Generate feedback for failed cases
        results['feedback'] = self._generate_feedback(results['failed_cases'])
        return results
    
    def _generate_boundary_tests(self, match) -> List[str]:
        """Generate boundary test descriptions from regex matches"""
        values = [int(x) for x in match.groups() if x]
        edge_cases = []
        
        for value in values:
            edge_cases.extend([
                f"Test value exactly at {value}",
                f"Test value just below {value} ({value-1})",
                f"Test value just above {value} ({value+1})"
            ])
        
        return edge_cases
    
    def _generate_test_case_with_llm(self, prompt: str) -> Dict[str, Any]:
        """Use LLM to generate specific test case"""
        # Implementation would use self.llm_model to generate test case
        # Return format: {'input': input_value, 'expected_output': expected_output}
        pass
    
    def _execute_test(self, local_dict: Dict[str, Any], test_case: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a single test case"""
        # Implementation would execute the test and return results
        pass
    
    def _generate_feedback(self, failed_cases: List[Dict[str, Any]]) -> str:
        """Generate feedback based on failed test cases"""
        feedback = []
        
        for case in failed_cases:
            feedback.append(f"""
            Edge Case: {case['condition']}
            Input: {case['test_case']['input']}
            Expected: {case['test_case']['expected_output']}
            Actual: {case.get('actual_output', 'Error: ' + case.get('error', 'Unknown error'))}
            """)
        
        return "\n".join(feedback)

    def update_test_history(self, test_results: Dict[str, Any]):
        """Update test case history for tracking improvements"""
        self.test_case_history.append(test_results)