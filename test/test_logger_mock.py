import snapshottest
from unittest.mock import Mock, patch
import hearthsim
from test.utils import patch_logger


class TestClass(snapshottest.TestCase):
    def test_logger(self):
        arguments = []
        def side_effect(arg):
            arguments.append(arg)

        mock = Mock()  # mock object
        mock.info = Mock(side_effect=side_effect)  # mock method

        with patch('hearthsim.utils.logger.LOGGER', mock):
            hearthsim.utils.logger.LOGGER.info('hi')
            hearthsim.utils.logger.LOGGER.info('there')

            logger_output = '\n'.join(arguments)
            self.assertMatchSnapshot(logger_output)

    @patch_logger
    def test_logger_with_decorator(self, logger_arguments):
        hearthsim.utils.logger.LOGGER.info('hi')
        hearthsim.utils.logger.LOGGER.info('there')

        logger_output = '\n'.join(logger_arguments)
        self.assertMatchSnapshot(logger_output)
