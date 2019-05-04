from builds import models as builds


def test_manager_create(target, version, builder_account, test_results):
    """Should create build with results."""
    builds.Build.objects.create_build("0", target, version, builder_account, test_results)
