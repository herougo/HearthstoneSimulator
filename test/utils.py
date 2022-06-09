from unittest.mock import Mock, patch


def generate_class(name, base_class):
    return type(name, (base_class,), {})


def patch_logger(f):
    def final_function(self, *args, **kwargs):
        logger_arguments = []

        def side_effect(arg):
            logger_arguments.append(arg)

        mock = Mock()  # mock object
        mock.info = Mock(side_effect=side_effect)  # mock method

        with patch('hearthsim.utils.logger.LOGGER', mock):
            f(self, logger_arguments, *args, **kwargs)

    return final_function