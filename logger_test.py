import pytest
import logger

""" Tests for the Logger class in Herd Immunity """

def test_logger_init():
    """check to make sure that the logger instantiator is working"""
    log = logger.Logger("new_file")
    assert log.file_name == "new_file"

""" unsure how to write the tests that just log to file """
# def test_write_metadata():
#     """ test that file is written correctly"""
#     pop_size = 10
#     vacc_percentage = 0.5
#     virus_name = "test virus"
#     mortality_rate = 0.5
#     basic_repro_num = 0.5
#
#     assert
