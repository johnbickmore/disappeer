"""
test_displaysentrequestcontroller.py

Test suite for the popup module DisplaySentRequestController.
Should display host address and key dict info

Copyright (C) 2018 Disappeer Labs
License: GPLv3
"""

import unittest
from unittest.mock import MagicMock, patch
from disappeer.popups.displaysentrequest import displaysentrequestcontroller
from disappeer.popups.displaysentrequest import displaysentrequestview
from disappeer.popups.bases import basepopupcontroller
from disappeer.gpg.helpers import gpgpubkeyvalidator
import tkinter


gpg_pub_key_string = '''-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1

mQENBFkV2wYBCADhSKS5957Y/3NPYUO6RVYpTPScMxULQ5fR2bwIZYMvSjZ7rdPM
zlcCg7MbXvFBrzbRKebzt1tmhntBjzi0HnpPcsTslQZyOfiZ3plfiQXGZMdL83t4
g/nxP6i3+TfXafalUnr2Zp3vk9ClWyBFS1Bmzqz97w4S8uhrvMal/TklDJ+3MY8F
vsPpaOgZvCgG27vyoQnay+mVkWgC+bOFnl9tjXCSr2a1seHJpUCmJgT/qba3wVI2
NUdq9fHChY9ug1BHTFm7HvFWntRKPT+682lm3iS8kssdacxFxpheRwj6Qdk+yRQO
Ht+I8T/GtCEF0HlscYhg+7JbLnxMdYhKctTjABEBAAG0N21hY3Rvd2VyIChEZWZh
dWx0IGNvbW1lbnQgbWVzc2FnZSkgPG1hY3Rvd2VyQGVtYWlsLmNvbT6JAT4EEwEC
ACgFAlkV2wYCGy8FCQGqfjoGCwkIBwMCBhUIAgkKCwQWAgMBAh4BAheAAAoJEFWk
Wpn+ReVA4i8IAIW0JB7VEI+q0n2+exWu7uITB6OmSvJ+xadEP6sUwf02Eghppiyg
u181ZE9TpspMNscTxyv03bK9yMqbNgpNQ6LUKzD90Qlut9gl9whxCVDI78VGrCXf
YjTfG5kowCU2mIhJIpUAdb8ufvqZFYo2BnRrsj/heu9+JSYRevs+yTADo2gJGOZQ
LOm+ra8BXyw5SYAwfO+YzyuXw5ITkXppxvL2jvLf62OGNSPF3nEbS/EebJZENtw7
F0fh+9xKao+mJIX6bjAgUlIWvaqsu6W7DKeNf/flYoCnddnP06FvgjCMC9G2II9p
qVw+Ytr7XLZuvjqx84VimuK6y4+DY6shhOC5Ag0EWRXbBhAIALCVLle15qOSsQwr
0sbJ2+sN57ZzNfYOZMUqZbC9YCOPDDu54UtY2nB6oJ54PJZBGp4Fmd5oQgBYuntL
9BMj22MFgWH9Ia8RUuAImGScaGT0/BVyueeWygag0T7AuCN2Mkoed7GaA3Vv3rJf
YdBwlY6rGiIy68iWMFd4E4LCf8XTC6twufvaw0gKS4LuFLCmxEsKYIrRfYDT/MtU
b+tz+g+mxAmolGN7j7WyAdhYNNGKSh3N+AZQbBDUK0Mbrr0sdKOEJBCrN72jygGm
BfIgAkJFQ4XaG/AJ/sOgvXN3vXvzEFQrPgOVVmmVPoBOdU97kzETcEg+ZyQtOSAg
fFi20bMAAwUH/2KnoIigeKqhs8MbGGxEFJHsVxTAMxCj8A+p73+KLEtwm4DSziff
ggxnsPxEAPqwopIErB6DB2DPNVr6b4txQVIh/oe4zMhEpONi9GyTgINChNcjf7VW
Gu7So4s7y1FE2e14Xx/CsI7pICQa/FYZPmTEFOxF6vgPqnp3H2gfR7rG3FsrXZdr
mn9Aov4jCBbOBJ8Ucgfv3F0AIDs32qvuCusjYHRFggzdgtK4D92H5VidE+F0sdJK
314VtZVGcCnrvyNV/OKJ+LsKnskgGOWyYItEm5XJ8BIz1b9MBvXcGrSPPUeAonbE
6Ayl6ogjCn6l1Gn/h/JcsvawNSZLz2rYBjSJASUEGAECAA8FAlkV2wYCGwwFCQGq
fjoACgkQVaRamf5F5UCSkAgAx7gC2263ZPSTQZCJE8uJHeD9Ybik7o1/txaIICMV
vzBxIOBOSSOMVjwxJhQwkj3//WQjBmqNghlsIq5Rfwnj4bNSTrZj8pqDtoqYv1fg
WVhZv4mFF7Uw+O42Y/TC9rAU/pzvDIyUW6pLEOUMv0uUT7vqWFN8+ELGZrWQwSVL
8q6eBOhLuwq67ee4wFWc3EUh3BL1nTWfoUeJgWLJqgUIWsXK0UMhkTjuIJTRArxA
Htuy1Idq3WBJq0xL2apEfuaZTYlcbaKabieg62kseAwMsALEetBDljtUK7tkCWIS
9bB+QnZSJ1naxflAI/TtxVoLlyWRz3Mw5MxzDayjI7nYxA==
=IF8v
-----END PGP PUBLIC KEY BLOCK-----'''


class TestImports(unittest.TestCase):

    def test_basecontroller(self):
        self.assertEqual(basepopupcontroller, displaysentrequestcontroller.basepopupcontroller)

    def test_peercontactview(self):
        self.assertEqual(displaysentrequestview, displaysentrequestcontroller.displaysentrequestview)

    def test_gpgpubkeyvalidator(self):
        self.assertEqual(gpgpubkeyvalidator, displaysentrequestcontroller.gpgpubkeyvalidator)


class TestClassBasics(unittest.TestCase):

    def setUp(self):
        self.click_command = "<ButtonRelease-1>"
        self.onion = 'xyz.onion'
        self.root = tkinter.Tk()
        with patch.object(displaysentrequestcontroller.gpgpubkeyvalidator, 'GPGPubKeyValidator'):
            self.x = displaysentrequestcontroller.DisplaySentRequestController(self.root, gpg_pub_key_string, self.onion)

    def test_instance(self):
        self.assertIsInstance(self.x, displaysentrequestcontroller.DisplaySentRequestController)

    def test_instance_basecontroller(self):
        self.assertIsInstance(self.x, basepopupcontroller.BasePopupController)

    def test_root_attribute_set(self):
        self.assertEqual(self.x.root, self.root)

    def test_title_attribute(self):
        target = 'Sent Request Peer Info'
        self.assertEqual(target, self.x.title)

    def test_gpg_pub_key_attribute_set(self):
        self.assertEqual(self.x.gpg_pub_key, gpg_pub_key_string)

    def test_host_addr_attribute_set(self):
        self.assertEqual(self.x.address, self.onion)

    def test_validator_attribute_is_validator(self):
        self.x = displaysentrequestcontroller.DisplaySentRequestController(self.root, gpg_pub_key_string, self.onion)
        self.assertIsInstance(self.x.pubkey_validator, gpgpubkeyvalidator.GPGPubKeyValidator)

    def test_validator_called_with_pubkey(self):
        self.x = displaysentrequestcontroller.DisplaySentRequestController(self.root, gpg_pub_key_string, self.onion)
        self.assertEqual(self.x.pubkey_validator.target_pubkey, self.x.gpg_pub_key)

    def test_view_instantiated_if_validator_is_valid(self):
        self.assertIsInstance(self.x.view, displaysentrequestview.DisplaySentRequestView)

    def test_view_instantiated_with_window_and_validator_key_dict(self):
        self.assertEqual(self.x.view.window, self.x.window)
        self.assertEqual(self.x.view.address, self.x.address)
        self.assertEqual(self.x.view.key_dict, self.x.pubkey_validator.key_dict)

    def test_config_event_bindings_calls_bind_on_cancel_button(self):
        self.x.view = MagicMock()
        target = self.x.view.cancel_button.bind = MagicMock()
        self.x.config_event_bindings()
        target.assert_called_with(self.click_command, self.x.cancel_button_clicked)


    @patch.object(displaysentrequestcontroller.DisplaySentRequestController, 'config_event_bindings')
    def test_config_event_bindings_method_called_by_constructor(self, mocked):
        x = displaysentrequestcontroller.DisplaySentRequestController(self.root, gpg_pub_key_string, self.onion)
        self.assertTrue(mocked.called)



