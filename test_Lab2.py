# CSC 122
# Tests for Lab2
# Acreage Calculator programm

import os.path
import sys
from HW1 import main
from tud_tests import *

def test_Lab2():
    
    try:
        exists = os.path.exists("HW1.py")
        assert exists == True
    except:
        sys.exit()
    
    # Test 1
    set_keyboard_input([34570])
    main()
    output = get_display_output()

    assert output == [
        "Enter the square feet of the area to convert to acres: ",
        "\n345000 square feet is equal to 7.92 acres."
        ]
    
    # Test 2
    set_keyboard_input([198000])
    main()
    output = get_display_output()

    assert output == [
        "Enter the square feet of the area to convert to acres: ",
        "\n198000 square feet is equal to 4.55 acres."
        ]

    # Test 3
    set_keyboard_input([50000])
    main()
    output = get_display_output()
    
    assert output == [
        "Enter the square feet of the area to convert to acres: ",
        "\n50000 square feet is equal to 1.15 acres."
        ]

    # Test 4
    set_keyboard_input([21870])
    main()
    output = get_display_output()
    
    assert output == [
        "Enter the square feet of the area to convert to acres: ",
        "\n21870 square feet is equal to 0.5 acres."
        ]
