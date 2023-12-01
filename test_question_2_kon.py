import kon
import pytest

def test_kira_kon():
    result = kon.kira_kon(3,2)
    assert result == 18.851999999999997

def test_kon(monkeypatch, capsys):
    # Define a function to simulate multiple user inputs
    user_inputs = ["3.56", "2.56"]

    def mock_input(_):
        return user_inputs.pop(0)

    # Use the function to simulate user input
    monkeypatch.setattr('builtins.input', mock_input)

    # Call the main function, which uses input() and prints the result
    kon.main()

    # Capture the printed output
    captured = capsys.readouterr()
    assert captured.out.strip() == "Isipadu kon = 33.98"