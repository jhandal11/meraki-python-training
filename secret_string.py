class SecretString:
    '''A not-at-all secure way to store a secret string.'''

    def __init__(self, plain_string, pass_phrase, private_string="This is a private string"):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase
        self._private_string = private_string

    def decrypt(self, pass_phrase):
        '''Only show the string if the pass_phrase is correct.'''
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ''

    def _private_get_the_private_string(self):
        return self._private_string

    def public_get_the_private_string(self):
        return self._private_get_the_private_string()


if __name__ == "__main__":

    secret_string = SecretString("Meraki: Top Secret", "switch")

    # Give the wrong Pass Phrase
    print(secret_string.decrypt("server"))

    #print(secret_string.decrypt("switch"))

    # Creates an error, __plain_test was name mangeled
    #print(secret_string.__plain_text)

    # No error, _private_string can be accessed like any other attribute
    print(secret_string._private_string)

    """ No error both public_get_the_private_string and
        _private_get_the_private_string are accessible
        convention indicates that the programmer wants you
        to use public_get_the_private_string
    """
    print(secret_string.public_get_the_private_string())
    print(secret_string._private_get_the_private_string())

    #print(secret_string._SecretString__plain_string)
    #print(secret_string._SecretString__pass_phrase)