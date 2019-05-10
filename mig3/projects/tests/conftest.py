import random
import string

import pytest

from accounts import models as accounts
from .. import models as projects


@pytest.fixture
def project(db) -> projects.Project:
    """Create a Project and Project."""
    return projects.Project.objects.create(name="Test Project")


@pytest.fixture
def project_with_tests(project, target):
    """Create a Project with Target, Modules and Tests."""
    for module_index in range(5):
        module = project.module_set.create(path=f"test_path/test_module{module_index}")
        for test_index in range(random.randint(1, 5)):
            module.test_set.create(name=f"test_{string.ascii_letters[test_index]}")
    return project


@pytest.fixture
def target(project) -> projects.Target:
    """Create a Project and Target."""
    return project.target_set.create(name="Test Target")


@pytest.fixture
def version(db) -> projects.Version:
    """Create a UserAccount and Version."""
    user_account = accounts.UserAccount.objects.create_user(email="user@example.com")
    return user_account.version_set.create(hash="a1" * 20)
