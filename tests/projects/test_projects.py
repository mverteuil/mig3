from projects import models as projects


def test_project_statistics(project_with_tests):
    """Should contain accurately aggregated statistics about the project's relationships."""
    statistics = project_with_tests.statistics
    assert statistics.target_count == projects.Target.objects.filter(project=project_with_tests).count()
    assert statistics.module_count == projects.Module.objects.filter(project=project_with_tests).count()
    assert statistics.test_count == projects.Test.objects.filter(module__project=project_with_tests).count()
