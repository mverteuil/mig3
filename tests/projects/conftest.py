import random
import string

import pytest


@pytest.fixture
def project_with_tests(project, primary_target):
    """Create a Project with Target, Modules and Tests."""
    for module_index in range(5):
        module = project.module_set.create(path=f"test_path/test_module{module_index}")
        for test_index in range(random.randint(1, 5)):
            module.test_set.create(name=f"test_{string.ascii_letters[test_index]}")
    return project
