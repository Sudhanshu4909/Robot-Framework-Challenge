# robot_api/views.py
from django.http import JsonResponse
from .models import TestCase
import os
from robot.api import TestSuiteBuilder
import json
from django.views.decorators.csrf import csrf_exempt
from robot.api import TestSuiteBuilder
import tempfile


@csrf_exempt
def execute_tests(request):
    if request.method == 'POST':
        try:
            tests_data = json.loads(request.body)
            tests = tests_data.get('tests')
            if tests:
                # Create temporary test file dynamically
                temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.robot')
                temp_file.write("*** Settings ***\n")
                temp_file.write("Library    SeleniumLibrary\n")  # Import SeleniumLibrary
                temp_file.write("*** Test Cases ***\n")

                # Write each test case to the temporary file
                for test_index, test in enumerate(tests, start=1):
                    test_title = test['title']
                    test_steps = "\n".join(test['steps'])
                    if test_title and test_steps:
                        temp_file.write(f"{test_title}\n")
                        temp_file.write(f"    {test_steps}\n")
                    else:
                        return JsonResponse({"status": "error", "message": f"Test case {test_index} is missing title or steps."}, status=400)
                
                temp_file.close()
                temp_file_path = temp_file.name
                
                # Build the test suite
                suite = TestSuiteBuilder().build(temp_file_path)
                
                # Execute the test suite
                result = suite.run(output=None)

                # Clean up temporary file
                os.unlink(temp_file_path)
                # Prepare statistics dictionary
                statistics = {
                    "total": result.statistics.total.total,
                    "passed": result.statistics.total.passed,
                    "failed": result.statistics.total.failed,
                    "skipped": result.statistics.total.skipped
                }

                # Prepare response JSON
                response_data = {
                    "status": "success",
                    "statistics": statistics,
                    "overall_status": result.return_code,
                    "test_results": []
                }
                for test, test_result in zip(suite.tests, result.suite.tests):
                    response_data["test_results"].append({
                        "name": test.name,
                        "status": test_result.status,
                        "message": test_result.message
                    })

                # Return the response
                return JsonResponse(response_data)
            else:
                return JsonResponse({"status": "error", "message": "No test data provided."}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON format."}, status=400)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)