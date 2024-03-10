"""
Neural machine translation starter.
"""
# pylint: disable= too-many-locals
import json
from config.constants import PROJECT_ROOT
from config.lab_settings import LabSettings
from core_utils.llm.time_decorator import report_time
from lab_8_llm.main import RawDataImporter, RawDataPreprocessor

@report_time
def main() -> None:
    """
    Run the translation pipeline.
    """
    settings = LabSettings(PROJECT_ROOT / 'lab_8_llm' / 'settings.json')
    importer = RawDataImporter(settings.parameters.dataset)
    importer.obtain()

    preprocessor = RawDataPreprocessor(importer.raw_data)
    result = preprocessor.analyze()
    assert result is not None, "Demo does not work correctly"


if __name__ == "__main__":
    main()
