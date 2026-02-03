def test_import() -> None:
    import jmaplib

    assert jmaplib.Client  # type: ignore[truthy-function]
    assert jmaplib.methods
    assert jmaplib.models
    assert jmaplib.errors
