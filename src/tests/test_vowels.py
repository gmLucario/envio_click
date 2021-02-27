from handlers.section_a import get_vowels_summary
from models.response import VowelSummary


def test_get_vowels_summary_expected_result():
    result = get_vowels_summary("lola la trailera")
    assert isinstance(result, VowelSummary)


def test_get_vowels_summary_just_letters():
    result = get_vowels_summary("lola COMO estas JamOn")
    assert result.new_line == "lule CUMU istes JemUn"
    assert result.vowels_count == 8


def test_get_vowels_summary_letters_nums():
    result = get_vowels_summary("lola COMO estas JamOn 123124")
    assert result.new_line == "lule CUMU istes JemUn 123124"
    assert result.vowels_count == 8


def test_get_vowels_summary_just_spaces():
    result = get_vowels_summary("   ")
    assert result.new_line == "   "
    assert result.vowels_count == 0
