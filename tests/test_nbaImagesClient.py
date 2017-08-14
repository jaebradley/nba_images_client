from unittest import TestCase


from nba_images_client.client import NbaImagesClient
from nba_images_client.models import Team, FileType


class TestNbaImagesClient(TestCase):
    def test_get_team_logo(self):
        logo = NbaImagesClient.get_team_logo(team=Team.BOSTON_CELTICS)
        self.assertIsNotNone(logo)
        self.assertEqual(b'GIF87a\x96\x00\x96\x00\x87\x00\x00\xff\xff\xff\xfe\xfe\xfe\xfd\xfd\xfd\xfc\xfd\xfd\xfc\xfc\xfc\xfc\xfc\xfb\xfb\xfc\xfc\xfb\xfb\xfb\xfa\xfa\xfa\xf8\xfb\xf9\xf9\xf9\xf9\xf7\xf7\xf7\xf6\xf6\xf6\xf4\xf7\xf6\xf4\xf4\xf4\xf3\xf3\xf3\xef\xf6\xf3\xea\xf4\xef\xf2\xf2\xf1\xf1\xf1\xf0\xee\xee\xee\xe7\xf2\xed\xed\xec\xec\xea\xe9\xe9\xe8\xe8\xe7\xe1\xef\xe8\xd8\xea\xe2\xd9\xe7\xe0\xe5\xe4\xe4\xe4\xe3\xe3\xd1\xe3\xdb\xe1\xe0\xdf\xdf\xde\xde\xdb\xda\xda\xd1\xd9\xd5\xd5\xd4\xd4\xd4\xd3\xd2\xd0\xd0\xcf\xce\xcd\xcc\xcb\xca\xc9\xc7\xc6\xc5\xc5\xc4\xc3\xc3\xc2\xc1\xbb\xdb\xcc\xb1\xd6\xc5\xa9\xd1\xbe\xa2\xce\xb9\xb5\xc4\xbb\x99\xc9\xb2\x8f\xc4\xab\x88\xc0\xa5\xbf\xbe\xbd\xbe\xbc\xbb\xbc\xba\xb9\xa1\xbb\xae{\xba\x9c\xb7\xb6\xb4\xb5\xb3\xb2\xb2\xb1\xaf\xaf\xae\xac\xae\xac\xab\xac\xab\xa9\xa9\xa7\xa6\xa7\xa5\xa3\x93\xaa\x9el\xb1\x91c\xad\x8aW\xa7\x82\xe8\x9el\xe7\x9dk\xa3\xa1\x9f\xa2\xa0\x9e\x9f\x9d\x9c\xe4\x9bj\xe0\x99i\xdb\x95g\xd2\x90d\xc9\x8b`\x9c\x9a\x98\xc3\x87^\x9a\x98\x97\xbc\x83[\xb1|W\x98\x96\x94\x96\x94\x92\x92\x90\x8d\x8f\x8d\x8b\x8c\x8b\x89\x8b\x89\x87\x89\x86\x83\x86\x84\x81\x85\x82\x80\x81\x7f|}{xM\xa0yD\x9dtG\x94o8\x96i3\x93f.\x91b\'\x8d]#\x8bZ\x1c\x88U\x16\x83P\x0b~H\x07}E\x04|C\x01zA\x01y@\x00y@\xa8vT\xa0qQ\x8coK{xuyvtxurwrn\x98lN\x95jL\x8dlK\x89mJ\x86kI\x83iH~hM\x86eI|eEyeE{bD\x84`Fw`D{ZCspmpmjljfjgdpcGhebkaCdc]d`N^`@a_[U`?N`AFa>>b>q\\CmX?b]XiW?mR>cQ=][T[WT[UN^O?WUOJWGPPK\x9a8 \x998 \x967 \x947 \x917 \x8b6!\x855!\x805!z4!aK:]G7RKBTF7UD6U@3N@2JICGEAHA:@B;I=1D=6?<7t3"o2"k2"d1#_1$Y0$S.#C8-=82C2)L-$G-$?+$\x0fs?\x1cm>\tu?\x07m<\x07l<\x05v?\x04r>\x05o=\x03x@\x01x@\x01w?\x00x@\x02v?\x03t>1f>7d>$j>\'f=\x10`8\x10]7\x11[6\x12Y5\x08j;\nh:\x0bf:\x0cc9\x0e`8 P4\x18P2\x1dI1\x1aK0\x13W5\x15T4\x16Q32?4&@. A-!>,\x1dG/\x1fC.850.7+72,)2(#;+$9*&5)5/*3/*2-)+.\')0\'.,\'4+%/+\'.*&.*%.)%-*%-)%,*%,\x00\x00\x00\x00\x96\x00\x96\x00@\x08\xff\x00\x01\x08\x1cH\xb0\xa0\xc1\x83\x08\x13*\\\xc8\xb0\xa1\xc3\x87\x10#J\x9cH\xb1\xa2\xc5\x8b\x183j\xdc\xc8\xb1\xa3G\x8b\x01B\x06@\xa1\t\x97\xa8O\xb6\x82}\xfa\x04\xea\xd4\xae)\x0e\x02\xc8\x04@3\x80\xcd\x9b7\'l\x91\xe7\xaf\xa7\xbfv[8\x04\x18J\xb4(\x80\xa3H\x93*]\xca\xb4\xa9\xd3\xa7P\xa3J=\x1a \x00\x85]\x9f\xb2f%%\xac\x14\xb0P\x9f\xc2\x865\xb5\xeb\x93\xd9O\xa5\xc6\xb5Y\xdb&\x9c\xbf\xb7\xfeV\xe1a\xb4\xacM\x9bh\x89&\xb1\xd2t\xe4\x82\x04\'\xe5\xb2\xb5\x19L\xb8\xf0\xb3o\xff<\x9d\x08\xc08\x00\x80\xc7\x90#K\x9eL\xb9\xb2\xe5\xcb\x983\x03\x08\x10\x00A\xaaO\xa0C\xdf\xc2w\xea\x93i`\xc0\x84\x91\xfa\xc4\xfa\x167f\xd7\xe2\x15\xc2!\xcb_\xa6\x104V1y\xb3\xa4U\xaf(D\x88(YB\xc4\x95\xbf\xe3%f\x1027\xceY\x9b\xe7\xd0\xdb\xac\x08\x10cM\x1b3\x102\xb41f\xcf\x10\x82\x00\x01\x00\x88\xff\x1fO\xbe\xbc\xf9\xf3\xe8\xd3\xab_/>@\x00\x01\x8a\xe25\x83\x11\xc0\x00\x8c3m\xf2\xebocm\x90\x1d\x80D\xa4\xa8\xb8\x82\xe1\x01\xadu\x9e\xbaP\x81\xf2c\x90\x14V\xb3\xa2\x10\xa1H\x91\t\xaa:D4j|\x92%\xc0G\x90!A\nP\xc4\xadM\x9b5\x1e\x02\x04\xd0\x10\xa0\xc5\x1a\x16\x01\x82\xb8\x93\x13\xc0&\x00\x9c9u\xee\xe4\xd9\xd3\xe7O\xa0:\x03\x04\xa0\xe2\xaeY\x1b\xa4H\xd5\x08\x89\xa0A\r4Y\x0b\x02L\x95\xc0\xca\xd2\x12"M\x88l\xedE!\xc0\xd7\xaf9\x18\xb5!\x8b\x0cN%V\x81\\\xc1!\xd6\xc6\xad\x1fW\x814\t\x08P\xd7n\x88W\x07\x02\xec\xe5\xcb\x17C9fm\xda\x08\xa9\x10 \x80\x01\x16_\xd6$\xfb\xa7#@\x00\x00\x91%O\xa6\\\xd9\xf2e\xcc\x98\x03\x04\xc8\xf2\xaeM\x1b\x18\x01D\x8b^\xb1\xe6\xd9\xab\x00\xa9U\xaf\x0e0"\x16\xaa|\xaf$\x04\xa0\x1d\xe0\x88\x11B\x99~\xf0\x98D(\xc0o(\xe9\x98\x11\xc3\x03\x07\xff\xce\xa4)\x01\x94\x07\xe0\x00"\xc0\xf3\xe7\x84\x02L\xa7^}:\x83rm\xb4k_c&\x8c\x87\x00A\xea\xfd\x08\x10\x00\xc0y\xf4\xe9\xd5\xafg\xdf\xde\xfd\xfa\x00\x01J\xf8S\x16&\x80\x06\x16,Z\xb4p\xd1\xa6\r@Y\x01\x06\x12,h\xb0\xe0\x87N\xc9\xda0d\x98H\x92$G\x90\x1c\r#\x06\x07\xce\xb26\x1a5n\x1b\x14`D\x8e\x00"G\xca)\x10\xe0$\xca\x94\x01\x18\xbck\xd3fL\x80\x982Wl\xf3g!@\x00\x00:w\xf2\xec\xe9\xf3\'\xd0\xa0>\x03\x04\x80\xe2\xae\r\x0b\x16h\x06\xb4h\xe3aE\x9b6\xe5\x18\x04\xa8j\xf5j\xd5\x10[\xc6\xb5i3\xac\r18p$M\x82c\x16\x8e\x1e?\xc3\xf4\xc0\xe9\xe3\xe8\x10\xb26m\x88\xb5\x89\xf4\x87P\x80\xbc\x0cjq!\x11\xe0/\x14\x10\x01\x06\x13\x1eL\xc1\\\x9b6\x1b\x02\x08i\xe3\xd8C\x800\xfer\x04\x08\x00\xe02\xe6\xcc\x9a7s\xee\xec\xd9s\x80\x005\xfa)k\xb3"\xc0\x8d6\xffm\xd2D\x08\xf0\xa5\x8d\xb9\x10\x01f\xd3\xaeM{\x8e?\x7f\xae\xe0\xe8\xe9\x15(\x11\x1cF\xc8\x12\x05\xea\xe5\xef8\xf2\xe4\xc7a\x05h\xee<\xc0\t~n\x88P\xa7.h\t\x91V\xab\xdad\xb8\xd1f\x0c\x84\x00\x01 \xa8\xd1\xe6oD\x80\x00\x00\xd6\xb3o\xef\xfe=\xfc\xf8\xf2\xe7\xb7\x0f`\x1fJ=em\xf6\xb7AS\x06`\x80\x152\x0cxi\xa3LV\x87\x00\x0b\x196l\xe4\x0fbD\x7f\xf9:\xc4Y\xe7\x0fcF\x8d\'\x02t\xf4\xe8q\x07\x93"\xb7>}\xca\x05\xae\xcd\xb36+Y\xb2\xe4\xe6\x0fG\x00\x99\x00h\xd6\xb4y\x13gN\x9d;y\xf6\xa4\x19\x00\xa8\x0f\x7f\xd6\xda\xacis\x14)\xd2k$\xb4\xf8s*\'@T\xa9Qy\xf8\xe34\xc7_V\xadY\xe7\x04\x08\xc0`G&t\xd7\xda\x945[\x16\\\xa9O\xa2\xda5k\xf3\x96Y\xba|3\x02\xd4\x05p\x17o^\xbd{\xf9\xf6\xf5\xfb\x17p`\xbd\x01\x08;\xb8B\x0f\x1e\xb76\x8b\xd1q\xff\xf1\xf7\xd8\x9f\xba6\x93\'{S\x10 \x80\x13cm8w\xf6\xfc\xf9\xb3\xb3p\xf8D}\xfa\xb4*@j\x00\xabY\xb7v\xfd\x1avl\xd9\xb3i\xd7\xb6\x1d;@\x00\t\xfex\xf7\xf6\xfd\x9bw,\x1f\x9cr\x040~\x1c9\x00\xe5\xcb\x97\x07\x08@\x82\xd7.\x1a\x01\x02\x00\xb0~\x1d{v\xed\xdb\xb9w\xf7\xfe\x1d|\xf8\xef\x01\xc8\x977\x1f\x00@z\xf5\xeb\xd9\xb7w\xaf>@\xfc\xf8\x00\xe8\xd7\xb7\x7f\x1f\x7f~\xfd\xfb\xf9\xf7\xf7\x0f\x10\x80\xc0\x81\x04\x0b\x1a<\x880\xa1\xc2\x85\x0c\x1b:|\x081\xa2\xc4\x89\x14+Z\xbc\x881\xa3\xc6\x8d\x1c;z\xfc\x082\xa4H\x89\x01J\x9a\x04\x802\xa5\xca\x95,[\xba|\t3\xa6\xcc\x994k\xce\x0c\x80\xd3G\xb0Q\x9fz\xf6\x1c\x05\xec\x93\xd0\xa1\x9fB}\x12\xa5\xaa\x9d?x\xe3\x8e\xb5ic\xcd\x9f\xd4\xa9S{M\xc2\x93h\xd8\xb5tm\xba\xb6\x81\xb6m\\\xbd|\x8ar0\x08\x80\x16-\x80\xb5l\xdb\xba}\x0b7\xff\xae\xdc\xb9t\xeb\xbe\r\x10\x80\xc3\xadO|?\x85\xca%l\xd4\xa7\xc1\x9ft\t\x13\xf5)\xb1bQ\xdf\xda8v\x8c\xee\x12\xb56\xc3\xfa\xc4\xdaAb\xd1\x13"D\xa2\xdc\x91\xe7/\xf4\xbb6\xa4K\x9b>M\x9a\x19\xb8|F\x02\xb8\x0e\x00 \xb6\xec\xd9\xb4k\xdb\xbe\x8d;\xb7\xee\xdb\x01\x02X\xa8\x15\xee\x99:[\x9f\x8a\x1b\xe7E\xea\x93rR\xed\x90\x14p\xc0 \x80\xf4\xe9\x01|l\xaa\xa1\xef\x8d\x92$D\x88$\x91\x12\x85\t\x13y\xfeP\xa1\x12DdS\x80\xf5\xec\x0b@ag\xac\xcd\x97\x04\x01\x0c\x94i\x83?\x7f\x18\x19\xeaj]\x00\x18 \x00\x00\x82\x05\r\x1eD\x98P\xe1B\x86\n\x03<4\x84N\x8d\x86\x00\x15-\x06H@\xa6\xcd\xb9\x1a\x01<\x12\x18$\x88\x08\x91(s$\x04@\x992\xc0\x07\x1d\x17\x8c\x1c\xaa\x93\x84\xc8L"L\x88\x10\x892K\x9e\x1e8pb\x1d\x08\x10T\xe8\xd0\xa1H\xc2\xb5is#\x80\x8b6h\xda<}\x8aNQ\x00\xaa\xff\x00\xac^\xc5\x9aU\xebV\xae]\xbd\x02\x08\x10@\x0b<!\x01*\x9ci\xa3\xc6C\x80\x1bm\xda\x98\xa3\x10@\xae\\\x0b\x96\x98\xb8Y\x02(\t\x11\xbe\x96\x1a\xa9\x08\x108\xc0\x88\x19\x02\x02\x04\x983!\xc0\xe2\xc5?V\xcd\xaat\x89G\x00\xca\x95-\xe3\xd8\x11@\xf3f\xce%\xd2\xb5i\xe3%@\x800mL\x9b\x86\xb7%@\x00\x00\xad]\xbf\x86\x1d[\xf6l\xda\xb2\x03\xdc\xae%\xee\x8c\x172m|\xffns\xeeD\x00\xe2\xc5\x8d\x1f/1%@\x00\x1dH\x02\x1c\x90#\t\xcet8\xbd\xe0Lk\xc3\xac\r$8\x89\x12E\xeb$ \x80\x00D\x04j\x90\x08\x90>G\xa6\x13\x01\xdc\xbf\x87\xef\xbe\x07\xb66\xf5\xed\xb7\t\x03C\x88\xb8Z\x01\xfc\x03\x04 p \xc1\x82\x06\x0f"LX0@\x80\x05\xfe\xba\xb5\x89(q\xe2\xb7\x19\x01.b\xcc\x98Q\x00\xa7>p>J\x8b\x06g\xa4$T\x89\xda\xa0L\xd9F\x1a\x9c\x96x\xfc\xc0A\x85#@\x80\x0eX\x02\xe0\xff\xcc\x89%\x00\xcf\x9e>\x03\xd0\xf8\xd6f(\xd1\xa2\xe4d\x05H\n`)\xd3\xa6N\x9fB\x8d*\x15j\x80\x00[\xe0\xb5\xc9\xaauk\x9bt%\x02\x80\r+V,\x14z}\xe0\xa0\xbd\x04\tY\xb16n\xddF\x82#W\xda#<\xd1\xa8I\xba\xc4\xaa\x97\xabB\x01\xfe\x82\xd0\x12`p\x80\x03\\L\x1c\x08\xa0Xq\x8eom\x1eC~\x9c\x86\xc5\x98zH\x02\x04\x00\xa0y3\xe7\xce\x9e?\x83\x0e-\x1a@\x80\xd2q\xe29\x8b\x11`u\x80\x06a\xda\xc0nc\xad\x10\x81\x00\xb6o\xe3\x0e0\xc2\x1f\xef+\x99\xfc\x01\x0f.|\xb8pX\x01\x8e#\x0f`\xa4\t\x91&\xf8F\xe1bB\xc4\xce\x92TD\x18\xb5\xc9\xae}L\x85\x1b\xf5\xa8\x04\x08\x0f`<\xf9\xf2\xe6\xcf\xa3O\xaf~}\xfa\x00\x01\x0eP\x8a\xf7\xacL\x04\x19mX\x04\xc8\xef"M\x9b\xfem\x00b\xf3D\x08\x16,}t\x16\x04X\xf0\xca_C\x7f\x98\xf2U\xc1\xe2\x8fb\xc5\x8a\xb0\x04\x04\xd0\xb8q\xff\xa3\nY\xefJ}\xfa\x14\xca\\\x1b\x93\'O\x1a\xab7\'@K\x00/a\xc6\x949\x93fM\x9b7q\xda\x0c\xb0\x13\x05=x\xc6\xda\x04\x15*4\x9c\xbfU\x9a\xe8\xd0Yd\x8f\x197o\xb0\xfcE\x95*\xb5^\xb66W\xb1f\xd5zu\xdc\xa9O\xa5\xe2m\xb3\xb7nD\x00\xb3\x00\xd0\xa6U\xbb\x96m[\xb7o\xe1\xc6\x95;\x17m\x00\xbb\x01\xaad*\xe4\x8f\xaf\xbfz\xecz\xd1\xf37\xeb\x12\xa5\x1c\'<\xd9K\xd6\x86qc\xc6\xcd\xb4\x89K\xd7\x8f^\xa1\x1c\x0e\x02d\xd6\xbc\xe9S.\x1d\x01\x02\x00\x10=\x9ati\xd3\xa7Q\xa7V\xbd\x9au\xeb\xd3\x01`\xff\xa0\x83E\x9f?\xdb\xb7\xfd\xe5K\x11\x80w\xef\xde\x00\x80\x07\x17>|x\x80\x003\xfc\xa1\x08\x10\x00@s\xe7\xcf\xa1G\x97>\x9dzu\xeb\xd7\xb1g\xd7\xbe\x9d{w\xef\xdf\xc1\x87\x17?\x9e|y\xf3\xe7\xd1\xa7W\xbf\x9e}{\xf7\xef\xe1\xc7\x97?\x9f~}\xfb\xf7\xf1\xe7\xd7\xbf\x9f\x7f\xff\xea\xff\x00\x03\x08\x1c\x18\xe0@\x80\x83\x08\x03\x00X\xc8\xb0a\xc3\x00\x10#J\x84\x08\xa0\xa2\xc5\x8b\x183j\xdc\xc8\xb1\xa3\xc7\x8f C\x06\x08\x80\x80R\xa9O(Q\xe2\x13\xf5\xa9\xa5KQ\xc0L\x04\x9893\x04\x94A\xaf\xf4\xf9\xdb\xc9\xb3g\xcfz\xfe\xd65\xca\xa2#D\x80\xa3H\x03\x00X\xca\xb4\xa9\xd3\xa7P\xa3J\x9dJ\xb5*\xd5\x00\x01\x90\x9c\xfa\xf4\xe9\x14\xbeS\x9f>\xd9\xb2\xf5\xa9\xacYR\xb8>}\x02\xc5\xae\x8d[\xb7\xdb\xfc\xc9\x9d\x9b\xaf\\\x9b6\xc4\x86\xc1y\x84\xcc\xd1?g\xd6\xb0,\xc0\x91\xad\x8d\xe16\xc9\xc6\xc5\xcb\xc7\x85B\x80\xc7\x01\x00H\x9eL\xb9\xb2\xe5\xcb\x983k\xde\xccyr\x80\x005N}\x1aM\xfaS\xb0[\x9fR\x7f\x02\x05\x0c\xd7\xa7\xd7\xb0\xcd\xb5\x99\xdd\xe6\x9a?\x7f\xd8\xda\x10k\x93\x08N%Z?(\xf0\xc0\xe4\xaf\xb8\xbf\x7f\xc9\xda(_\xce\xbcy7w\xb0B\x04\x98\x0e\xa0\xba\xf5\xeb\xd8\xb3k\xdf\xce\xbd\xbb\xf7\xee\x01\xc2g\xff\x02\xb6\x0b\xd7)P\x9f\xd2\x7f\x1a\x15\x0c\xd8\xa8O\x9fn\xe1\x03vkT)a\xd9\xda\xe8\xd7\xdf\xed\x9f7\x80\x81\x06]\x18t\xc7\x0e\xabv\xfe\xf8\x01"\x12E\x9e?\x88\xc6\xdaL\xa4X\x91\xa2\x97\x04\x01\x02\x0c\x90Q\xad^#\t\x01D\x02 Y\xd2\xe4I\x94)U\xaed\xd92e\x00\x98\xb1J\xe5\n\x86k\xd4\'\x9c\x9fB\t\x13\xf5\xe9S0\\\xa1\x82\xd1\xfbA @\x80\x02\x8a\xac\x1c\xc1\x94\xe9\x81\x8f&v\x88\x10\xa9\x13\xc5\x8d\x947L\x98\xf8\xf3\xd7\xeb\xc9\x12:\x01\xc4Z\xd8bNY\x1b\xb4g\x02$8\xd3\xc6\xed[\xb7\xdc\xfeU\tP\x17\xc0]\xbcy\xf5\xee\xe5\xdb\xd7\xef_\xc0\x00\x02\x0c\xd6\xf1O[\x1b\xc4\x88\xb9\xa5\xfb\xc5K\x97\xb0^\xea\xea\xdd9\x14`P\x80\x00\x85\x02l\xe6\xec\xa4\xc9$"\xa1\x8b\xa0r%\xc8\r\x13"o\xfc\xf9\x93\x17\x85H\x93Z\x0b\x02\xcc\xa6M\xfb\x02\xa7jm\xda\xacY\xd3\xc6\xf7\x18\x0f\x01\x02\x08\x88p\xe6\xff\x9f\x91\x00\xc9\x01,g\xde\xdc\xf9s\xe8\xd1\xa5O\x87\x1e\xc0z\xa6tm\xb4\xb7\x19\xe3!@\x00\r_\xda\xb41\x06\xcbB\x80\x1eQ\x88\xd8\x99\x11\xc0\xfd\xfb\xf7\x02\x10\xd5!R\xa4\x8e 7\x80\xec$!\xd2\xdf?\xc0%\xbfT\x04(h\xf0 \xc2\x10\xe5\xa0\xb5A\xa3!\xc0\x903\x15 \x94\xf9R\xa6\xcd;N\x016\x02\xe8\xe8\xf1#\xc8\x90"G\x92,\xe91\x00\xca8\xf0\xda\xb41\xd3B@\x00\x08A\xd4\xb4i\xc3\xac\x9c\x84\x00:\xa1\xb8r\x15\x85\t\x11"E`\x05(j\xf4D\x1f=\x89\x18\xf5AE\xe4)\x11@\xed\xa4E:\x04\xe7\xcf,8\x9a\x0eHp\x82\xa2\xc0\x07E\x04\x02\x90-[\x16\x84\xb96j\xd7\xaa\x15\xe3"\x81\x90xs\x02\xd0\x05`\xf7.\xde\xbcz\xf7\xf2\xed\xeb7@\x00\t\xf9\xba\x95\xf1\x10\xe0p\x861m\x16?\xf3T \x00\xe4\x00\x9a\x94\x08"2\t\x10\x91\xccwh\x04\xe8\xdc\x99D ?\x8c\xb8\xadB\xe2#\xd3\xa0\x10\xffSVIc\x04\'\x90\xabY\x13\x02\xd0\xaeM\xfb\x04\xa6\x00\xbaw\xf3\x9eP\xaeY\x9b1\x01\x02\x0cic\xdc\xb8\xb5|\x14\x02\x04\x00\xe0\xfc9\xf4\xe8\xd2\xa7S\xafN=@\x00\x0c\xfe\xb8\xc9\x08\xe0\xa2\rx\x19\x01\\\xb4\xb1\x86$\x00\xfa\xf4\xe8\x0f\xf8\x00DD\x89\x1d%uP\x04P0\'D\x80\xfc\xf91(\x12\x10\x00`\x00\x81<|\xc11\x88\xc7S\x00\x85\x0b\x19\x06@\xf2!@D\x89\x13\x03t\xd1\xd6\x06cF\x8c\x19\x02\x80\xd1g!@\x00\x00#I\x964y\x12eJ\x95\'\x03\xb4T\x14\xaeML\x993\xb1\x1d\tp\x13gN\x9c&8-\x08\xf03\xc0\x88\x1a\x01\x02\x08@\x84\x07N%(Z\xbe\xb5q\xda\x06\x12\x1c8\x92~\x04\xb0\xaa\xe0J\x97\x00[\x03H\xa0\x13\x00lX\xb1a\xb9hk\xd3\xe6K\x00\x03\x1aVx\x08\x00#\x1d\xa2\x00s\x01\xd4\xb5{\x17o^\xbd{\xf9\xe2\r\x10\xc0\x82\xbfma\x02\xdcX\x93\x06M\xe26m\xe0=\xff\x08\xf0\x18rd\xc9\x8fk \x02\x81\xa9\x93\xb16m\x18\xc1\x81\x93J\x8f\x1fG\x8f\xe0\x94\xee3\xacMjr\xfd\xfc\xa1\x08\x90\x05C\x00\xd9\x01\x18\x0c\np\x1bw\xee\xdb#\xd2\xb5\xf1\xfd\x1bx7\x7f\x08\x02\x04\x00p\x1cyr\xe5\xcb\x997w\xae<@\x80\x0e\xfe\xb4\x89\t \xa3Mv\xedm\xce]\x08\xf0\x1d|x\xf1\x01F\xd0\xca\x03\'\x122Fm\x86\xf5\x91t\t\x0e\xa46\xf3\xa5\xb5\x89\x06\x87X\x1bF\xc5\xa2U:\x020\xc0\x07(\x01\n\x1a<1#\x80\xc2\x85\x0c\x03\x80P\xd7\xa6M\x9a1\x14+\x9a\xb9\x96O@\x80\x00\x00:z\xfc\x082\xa4\xc8\x91$A\x068\x99)\\\x9b!7\xda\xdc\x08\x10\xa0A\x996\xdd\xa6\x04\xb8\x893\'N\x04\xaf\xda\xf8\x8c\x06\xe7\x10\x9c\xa1\x93*\xc1\xe9\xd3\xa6\r$F\xc8\x121\xd2\x13\x89\x1a\xb16m\x18\xfd\xe1\x14 \xeb\x858\x01\xba\x06X\xd0\x08I\x80\xb1d\xcb\xce9\xd6F\xcd\x8a\x00l\x03d0\xd3F\xff\xdd\x9c\x00\x01\x00\xd8\xbd\x8b7\xaf\xde\xbd|\xfb\xee\r\x10\xc0\x82>n^\x02\x18\x0e\xd3f\xc8\x976m\xb4u\t\x009\xb2d\xc9\x05:\xb5\xb9<\r\x0e\x9eUz\xdaxnC\xccQ18p\xfc\xb49\xddfX\x9b6\xc5\xe0\xe4\x99\x12 v\x1c\x06\x01j\xd7\xde\x12 \xb7\xee\xdcr\xb2\xb5i\xb3\xa2\xc1\x996\xc4]\x04\x00\xb3\xae@\x80\x00\x00\x9a;\x7f\x0e=\xba\xf4\xe9\xd4\xa7\x07\x08 A\x1e\xb66\xdce\x04\xf8\x1e\x00\x82\x986\xe6:\x048\x8f>=\xfa\x12\xfe\xfc\xa1\x82\x03\xa7R\xa0am\x86\xb1A6\xad\r$8p\x02\xb1\x02\x98\xcf\xdf@\x82\x03K\x04@\x18@\x05,O\xf4,=\xe1c\xa7H\x94voZ!:\xd7\xa6\x8d\x8b/m<~l\x13N\x16\x81\x00\x01\x00\x9cD\x99R\xe5J\x96-]\xbe\x0c\x10S\x8b\xbbf+\x02\xdch\xd3&M\x84\x00_\xda\xb4Qw"\xc0P\xa2E\x87\x1e\xa8\xe5\xcf\x9f<\x7fM\xf3\xfd\x99D\xcf\xdfT\xaa\xffU\xad\xfa\x08\x90Uk\x887D\x88\x14\xb1\x94/\t\x11>I\xdc\xd8\x892,\xc0Z\x16g\xda\xac\x08@\xe6\x9f\x91\x00\x01\x00\xdc\xc5\x9bW\xef^\xbe}\xfd\xfe\xcd\x1b@\xf0\xa0x\xcd\xda\x1cF\xdc&\x86\x86/m\xda\xa8\xcb\x11@\xf2d\xca\x01\x9c\xf8\xc3\xec\xcf\xd3\x0e,\xbe\xfc}\x06\x1d:\xb4<\n\x01L\x9f\x0e\x90\xa3\t\x11)\xb8>\xe5*\xc2\xc4U\xbb\'\xc4\xda\xdc\xc6}[Y=+\x01|\x03\x00\x1e\\\xf8p\xe2\xc5\x8d\x1fGn<@\x00\x13\xfa\xb0\xb51\x13@\xbat\x19h*D \xd3\x06\x9a9(\x02\x02|\x07\x1f\xe0\x81<\x7f\xe5\xcd\xfb\xab\xb2\xc3\xdfz\xf6\xed\xb1\x04\x80\x1f_~\x00\x13\xc2>}*\xd5\xad\xcd~\xfe\xfd\xdb\x00\x0cG\xefC\x80\x00\x00\x0e"L\xa8p!\xc3\x86\x0e\x1fB<\x18`\xa2\tz\xe1\xdaxI\x10\x00\xc2\x976\x1e?\xb6Q\xb6\xa3C>\x7f\xfe\xe6\x15\xaa\xd5\xa8\xd1\x96\x149\x1a\xe5\x93\xb3\xa0\x96\xbf\x9a6m\xa2\xff\x08\xa0s\'\x05,\xed\xc4\xb5\t*\xee\xd6\xa7O\xb9\x94\xb5I\xaa\xd4\xd9\xb9u \x02@\x05 u*\xd5\xaaV\xafb\xcd\xaau+\xd6\x00^\x7f\xe4\x0b\xd7f,Y\xb2\xcd\xb2\xa5\xf3\xa7Vm>B*\x04\x04\x88\xdb\xc3\x1f\xdd\xbav\xdd\x8d\xd3\xc6\xac\r\xdf\xbe~\xfbb\xc3\xf5\xe9\x13\xa9om\x9a\x9d\x93W#\x00c\x00\x8e\x1fC\x8e,y2\xe5\xca\x96/c\x86\x1c`\xb3\x82,\xfa\xd4Ak#z\xf45\x7f\xed.\xa1\xaaT\xa9\x17\xb46m\xba\xe1\xb0\xe0\xc9\x9f\xbfz\xe0\xb2\xb5\xc9\xad{7o\xde\xee@}\xd2\x95\x0f\n\x81\x00\xc6\x01 O\xae|9\xf3\xe6\xce\x9fC\x8f.}:\x80\x00\xd6\x03\x98@\xa4\xcf]#O\xfe\xbe\xfbC\xd7f\xfcxn?\x02\x04\x98\xa2\xac\r\xfb\xf6\xee\xdf\xb7i\x86\xad\x1e\xbd. \x02\xfc(\xf5\xc9V\x95\x00\x01\x00\x02\x108\x90`A\x83\x07\x11&T\xb8\x90aC\x84\x01\x02T\xf1GC\x9f?\x8b\x16\xf5UZU\xcb\xff_/\x7f\x1f?\xfe\xf37\xd2_\xadL[r|\x08\xb0\x92\xe5J\x00/\x03\x04pRJ\x17\x8a\x00\x01\x00\xe4\xd4\xb9\x93gO\x9f?\x81\x06\x15:\x94\xa8\xcf\x00\x010\xac\xf3\xb7\x94iS\xa7\\~\xcc)\x84!@U\x00W\xb1f\xd5z5@WJ\xbcf\x04\x08\x00\x80lY\xb3g\xd1\xa6U\xbb\x96m[\xb7o\xd7\x06\x90\x8bB\x96\x93#Y\xe2\xbc\x9a\xa7#@\xdf\xbe\x00\x00\x07\x16<\x98\xf0\xe0\x00\x871q\x08\x10\x00@c\xc7\x8f!G\x96<\x99re\xcb\x971gn\x1c \x00\x00\xcf\x9fA\x87\x16=\x9ati\xd3\xa7Q\xa7V\xbd\x9auk\xd7\xafa\xc7\x96=\x9bvm\xdb\xb7q\xe7\xd6\xbd\x9bwo\xdf\xbf\x81\x07\x17>\x9cxq\xe3\xc7\x91\'W\xbe\x9cys\xe7\xcf\xa1G\x97>\x9dzu\xeb\xd7\xb1g\xd7\xbe\x9d{w\xef\xad\x03\x84\x17?><\x00\xf3\xe7\xd1\xa7?\x1f\x80}\xfb\x00\x00\xe0\xc7\x97?\x9f~}\xfb\xf7\xf1\xe7\xd7\xbf\x9f\xbf\xfc\x00\xff\x00\x03\x08\x0c0\x02\x8b\xa6V\xfex\xa5B\xa4cB\x80\x87\x01\x00H\x9c\x08 \x80\xc5\x8b\x17K\xf0\xe8\xb1\x03A\x80\x8f \x03\x00\x18I\xb2\xa4\xc9\x93(S\xaa\\\xc9\xb2\xa5\xcb\x95\x01b"\xe8\x82\x0b\xd4\xa7\x9b\xc0N}\xda\xb9\xb3\xd4\xaa\x10\x01\x82\n\x1d\xaa\xa0D\x8f-\xf2\xfc)]\xaat^\x16\x1c\x1f\x04\x04\x98Ju*\x80\xabX\xb3j\xdd\xca\xb5\xab\xd7\xaf`\xc3\x8a\xbd\x1a \x80\x00:\xa5>\xa9U\x0bJ\xd8\xa7\xb7p\xdf\x82j\xd5A\x00\t+\xaf\xfc\xd5S7\xee\x9c\xbf\xbf\x80\x03\xcbK\x05\t^7c\xd7\xc2\xc1\xfb\xe7\xef\xd5\x14\x0e\x01"K\x06@\xb9\xb2\xe5\xcb\x983k\xde\xcc\xb9\xb3\xe7\xcd\x01\x02<he+\x18\xb0Q\x9fR\x97\xd2\xf5\xa9\xb5\xebO\xb7>}\xb2\x85\x0eZ\x9b\xdbm\x9e\xd9\xf3\xc7\xbb\xb7?_\xd1\x18\x1d\x823\xac\x8d2wm\xda<\xc3\xe4)Y\x1bg\xdc\xd4\xfdk\xc7%D\x80\xeb\x01\x00h\xdf\xce\xbd\xbb\xf7\xef\xe0\xc3\x8b\xff\x1fO\xbe{\x80\xf3\x9a>\xa9\xff4J\xd8\xa9O\xbaJ}\x9aO\x9f\x97\xa8O\xf8sek\xc3\xbf\x8d8\x80\xfe\x04\n\xec\xd5\x87Q\x1b\x84\xc3\xe0\xc0\xd1\xb3I\x9f\xa2\x14\x13\xaexkS\xd1b\xc5n\xee|\xfd(\x10\xc0c\x00\x00!E\x8e$Y\xd2\xe4I\x94)U\xae\x04\x10 @\t\\\x9fd\xce$\x85O\xd8\'\x9c8G\t#\xf5\xc9\xe7\'Q\xe1\xda\x0cmC\xce\x9f\xbf~\xde\xf4D\xcb\x93h\x18#s\xb0\xa8p\xf8\xe0\x84\x93\xbesm\xb4n\xe5\xca\xd5\x18:\x7ft,\x04 \x0b\xc0\xecY\xb4i\xd5\xaee\xdb\xd6\xed\xdb\xb7\x01\x02\xcc8\xf5\xc9\xee\xdd[\xc2@}\xe2\xfbiW\xb0O\x81\x05\x7f2\xd7\xc6p\x1be\xfeV!k\xd3\x86\x99#V\x83,lI\x05\xc8\xdfe\xcc\xdf\xdal\xe6\xdc\xd9s\x1bh\xe8\xd6\xcd\x08P:\x00\x00\xd4\xa9U\xaff\xdd\xda\xf5k\xd8\xb1]\x07\x08 @\xd7)[\xb8t\xe1\xcb\x15\xea\xd3oP\xbb\x84\x8d\xfa\xf4)\xff\x14.^\xc2\x82\xed\xba\xd6\xc6\xb9sn\xef\xdaH\xa3\xf6\xea\x83\x15KJ\x9aDaB\x84\x08+\x7f\xe1\xeb9kS\xde\xfc\xf9\xf3k\xbcx)3\xee\x1f\x97\x03\x01\xe4\x03\xa0_\xdf\xfe}\xfc\xf9\xf5\xef\xe7\xdf??\xc0\x00\x01\x8c\x94\xfad\xf0\xe0\'S\xf8r\x81\xfa\x04\x8a\x97\xb0Q\x9f&\x82b\xd7\xe6\xa2\xb6p\xec\xfc\xf9\xcbg\x05\x84&)\x80\xfc\xf9\xcb\x97\xcaR\xbb7D,\xf9kY.\\\xb662g\xd2\x0c3 \x80\x07\x0f\x02\x02\xdc8\xe6.\x13\x83\x00B\x01\x10-j\xf4(\xd2\xa4J\x972mz4\x00\xd4\x1a\xa7>}\nuK\xd8.Q\x9f\xb6\xde\x02\x06\xea\x940P\x9fB\xb1\xbbV\x0e\xcb\x87\x00\x84\xda\x1dq\xb0\xa5\x8b\xa1$n\x88\x10qC\xe4n\x12>M\xda\xf9\xf3\x97O\x91\x84\x00\x16\xaa\x94\xb3\xd6\xe6\xf0a4\x01\x12\xa0i\xe3\xf8\xc6\x8d4m\xb4\xd5\x8b# @\x00\x00\x9a7s\xee\xec\xf93\xe8\xd0\xa2Gs\x0e`\xba\x86?x\xff\xb6>\xb1n\xfd\xc9V\xaeO\xb2O\xe1\x03\x96)D\x80\xdc\xb9\x15P\xc9\xa1\xa0\x90\x04yo\x9e\x10!\xf2\x04P\x11"M\x98\x00\xf2\xe7/\n*7\x93\x02P\xa7\xfe\x81\x139fm\xd6h\x08\xd0"M\x9b\xf0\xe2\xc3c\xcb\x97"\x00z\x00\xea\xd7\xb3o\xef\xfe=\xfc\xf8\xf2\xe7\x03\x08`\x9fP\xbcgm\xdatkg\x0b \xa8O\x03\x83}\xfad\n\x98\xac\x0b=\nY\xa9% @\xc4\x88\x0c\xec\x00\x9a%\x85\xc8\x12TJ\x88t\xec\x98\xca\x9f\xbf;\xbd\xa4\xbc\x81\x12\x00eJ\x94#\xcamk#\xc6E\x033mh\xb6I\x13c\x80\x00/\xf1\x1a\x15\x08\x10\x00@P\xa1C\x89\x165z\x14i\xd2\xa4\x01\x02pX\xf7\xcd\x0c\x0b2m\xa8Vm\x93\xacM\x9bq\xa8\x88\xdc!0\'\x00\x82-\x01(\xa08R\x85\xca\x15+\x94\xa2\xf0\x01$\xa8\x0e\x11&RRY\x8a\xe2F\xca\x12"ER\xcd\x08\xf0\x17p\xe0\x00\x12\x14Yks\xb8\xcd\x9a \r\x02\x04\xff\x88\x11$\xc0\x8ao\xeb.\x04\x08\x00\x00sf\xcd\x9b9w\xf6\xfc\x19\xb4\xe7\x00\x01j\xfc\xd3\xd6\x06\x8d\x0c\x03\x01 \x04Q\xd3\x06v\x9bm\x8d\x14\xec!\xa2D\xd1\x02(?p\x8c@\x10\x00x\x00\x1a\x82\x88\xb8A\xd5\x84H\xf2&\x96\x94\x10q\xfe\xbc\xce\x88\x00\xd3\xa9W\xafN\xe1\xd5\xb16m`\x04\x88\xa0\xa6E\x00!g*$ \xa6\xefD\x80\x00\x00\xd8\xb7w\xff\x1e~|\xf9\xf3\xe9\xc3\x0f\x10\xe0\x84\xbflf\xc4\x84\xf9\x02\xd0\xcb\x10\r\x01\x02\xacX\x93\xac\xdc\x88\x00\x01\n,JB\xc4\x8e\x8f\x00\x14+V$P\x85U\x13"J\x9e0!\x022$\x91%\xae*\xa1\x1a\xc4!\x80\xca\x95,Y\xaa0\xc7\xac\x8d\x98\x04\x11\xcex\x81\x10\xa6\x8dNm\xfeP\x04\x08\x00 \xa8\xd0\xa1D\x8b\x1a=\x8a4\xe9\xd0\x00\x01B\xe8\xe36\xc6@\x80\x00\x1e\xc2\x90)c\xe6L\x1bnX\x02x\x15\xb0\xc5\x8d+W\x96\xdcD\x91\x13 \xadZ\x06\x9b\xfe\\\xd2\xe4\xe9\xff\r\x13"t\x93\xb0\x12\xd4\x8eU*T\xbd\xe0\xfc\xf9q\x05G\x15C\x880\x048\x8c81\xa2mm\xd6\xc08\xd3&\xb2\xe44\xdb\xfc\x91\x08\x10\x00\x80\xe6\xcd\x9c;{\xfe\x0c:\xb4h\xcd\x01\x02`\xa0w\xad\x8d\xea6a<\x04\x08P\xc1L\x1bqH\x02\xd8\x16`I\x8a\x1b"\xbcy\xcb+\x10 x\xf0\x1d\x81\x1e\xb5\x99\xf6h\x92+;w\xda\xb9zD\xacM\xb4D\x93.\x05\xa2\x11 \xbbv9=\x02x\xff\x0e\x9eK\xb76\xe4\xdb\xa8\x19\xb2"\x80z\x16\xe2\xda9\x08\x10\x00\x80\xfc\xf9\xf4\xeb\xdb\xbf\x8f?\xbf\xfe\x00\xfc1\x85\x03\xd8F\x8d\x18!a\xd2\xb4i\x93FL\x9bp<\x02<\x0cp\x04\x90+"J\x00\x11\xc1h\xe9C\x00\x8e\x1ck\x04jC,\x9a\xa3>\x8b\\\xf5i\xd7\'\xd1#j\xd1\xf0\xb4\x9bd$\xc0L\x9a3\x11\xe5\x08\x90S\xe7N+\xd7\xda\xb4q\x11 \x80\x8c3m\x8c\xb69\x87(\xc0R\x00M\x9d>\x85\x1aU\xeaT\xaa\xffT\x03\x04\xa0\xf1\x0f\x8d\x86\x00\x06\\$\x08P\xe1L\x9b6\xd7v\x04@\x8bv\x0b\x13K\x80R\t"\x12\xb7\x89\x16\x1e\x01\xec\x06(\xb0J\x92\xa7\x1e\x0b8\x0c\x12\x10@0\x07N\xa8\xf4\xf4\xaa4(\xc0b\xc6\x8d3\x8d\x08\x10Y\xf2d+\xdd\xda\xb4Y\x11\xc0C\x1b\xce\x9c\xa1\xfd\xc3\x11 \x00\x00\xd2\xa5M\x9fF\x9dZ\xf5j\xd5\x01\\{\xfa\x06#\xc0\x8d6\xb5\x85\x04`\xd1\xe6\x19\xa6\x00\xbd}\x07P1K\x90\xa5&\xa8\xde\x00"B\x08A\x9c\x0e\x01\x9c?\x0f\xb0\x03G\x00\xea\xd4q\xac\x82\x93\xbd\x17\x87\x00\xdd\xbd\x7f\x9f\x81"\xc0x\xf2\xe5\t\xc8r\xd6f\r\x8b!j\xda\xbc\'\xf3\x85\x9a\xa7\x00\xf5\x01\xdc\xc7\x9f_\xff~\xfe\xfd\xfd\x03\x04 p \x80\x00\x01v\xfc{\x16&\xc0\x00\x19g\x84@\x080\xa4\x8d\xba\x10\x01.b\xc4\x88@\xd5\x12"I\x04\r\n \xf2\x00\x8e\x19\x05\x02\xa0D\xc4#\x00\xcb\x00?\xd25;\x04\x07\xce\x1f.\x01n\xe2\xff\xcc\x19\x80\xcb\x82\x00>\x7f\x02\r@\xe3[\x9b\xa2F\x8bz\x080\xc4_\x8a\x00\x01\x00@\x8d*u*\xd5\xaaV\xafV\r\x10`\x8e\xba6m\xd6\xdc\xf0`\xc0\x83\x8c5m\xb6i\t\xa0v-[\xb5\x02j\xf8\x02\x11`\xee\xdc)\x01\xee\x9e`\x05\xc7\xd5\x85\x00V\xc2\xb5i\xf3h\x1a\x1c8\x95x\x04H\x1c\xc0J\x95\x00\x8e\x1d\x1b\n y2\xe5\xc9\x88\x92\xb5i\xe3%\x83\x80\x00\x9e\x03\xc8x\xa7%@\x00\x00\xa6O\xa3N\xadz5\xeb\xd6\xaa\x03\xc0\xf6D\xae\r\xed\xda\xb6\xc3\xe1\x08\xa0{7o\xde$\xba\x08\x08 \xbc\x0b\x82\x00\x02\xba\xe8\x81\x03\'\xcf<p\xc8\xda@\x97\x06g\xfa\x9f,\x01\xae\xe3(1\x05A\x80\xee$\xaa\x04\x08/~\xbc\xf8)\xdd\xda\xb4As\xa6\r\xfb \x01X\x90{\x15`>\x80\xfa\xf6\xef\xe3\xcf\xaf\x7f?\x7f\xfc\x01\x00\x06 \x90\xcf\xda\x97\x007\xda$T\xd8\xe6\x1d\x88\x00\x0f!F\x94\x18`\xc6\x0e\x15\xf9\xa8,@\x94\xad\xffM48p\xfe\xa0\xea\xd3\x86X"b\x89\x18\xb5Q\xd9\r\x89\x04:\\\x02\xd0\xd8\x11\x80f\x0e.U\x02\xe4\xd4\xb93\xe7\x8com\x80\x06\x15zm^\x00\xa3\x00\x90&U\xba\x94iS\xa7O\x97\x06\x08\x10\xc2\xdf\xb10\x01\xb0fm\xd0\xa6M\xb9\x00_\xc1\x86\x15+VB\'em\xda0#\x96\x08\x0e+8o\xe1\xe0\x81\x03\x07\x12\xb16w\xdb$\xf3\x85@\x00\x97\x00\x7f\x01\x1b\n0\x98p\xe1\xc1\x17\xce\xb5i\x93\xa6L\xe3\xc6d\xccp\xf37!@\x00\x00\x971g\xd6\xbc\x99sg\xcf\x9a\x03\x04\x08\xe1\xef\x98\x98\x002\xda\xa4V\xdd\xe6]\x81\x00\xafa\xc7\x96\xfd\xba\x84,bmp\xe3\xa6\x06\xc7U\x1e6m\x80G\x8b\xc6\xc8\xcf\xb06\xc5\x86!\xdb\x84%@\x8d\x12\x01\xa0GG\xf2!@u\xeb\xd7\x03\\8\xd7\xa6\r\x99\x00\xdf\xc1\xaf\xe8\xe6\x8fA\x80\x00\x00\xd0\xa7W\xbf\x9e}{\xf7\xef\xd7\x07\x08@\xc1\x1f74c\xcc\xb4\xd1\xbf\xbf\r\xb8\x11\xff\x00\x03\x08\x1cH\xb0 \x87Xz\xe0\xc0\x89\x14\rN"=pf\xf9\x196\xadX\x9b\x8bm\x1c\xc1q\x94\xc8O\x1bF\x97p\x04\x08\x10\x87B\x80\x93\'% \t\xc0\xb2\xa5\xcb\x00$\xc0\xb5\x99I\xb3\xa6\xb8u\x01r\x02\xd8\xc9\xb3\xa7\xcf\x9f@\x83\n\xf5\x19\xa0h-qm\x92\xb6Q\x13\xa3\x05\x996m\xb0\xf5\x08@\xb5\xaaU\xab8\xc61r\x94\x08\x8e\x9e>p\xc2\xce\xc2\x83gY\x9b6\xc5\xda\xa8\x9d\x06\xa7m\xa2Hz&e\t@w\xcb\x87\x00x\xf1j\x11\x10\xa0\xaf\xdf\xbfP\xac\xb5\x19\x1cF\x86\x8c j\xda\xb4\t\xc7)\x80c\x00\x90#K\x9eL\xb9\xb2\xe5\xcb\x94\x03\x04\x88\x83\xaeM\x0b\x0fmV\x18\x80\x11\x00F\x1be\x85\x02\xa8^\xcdz5\x8aomb\'\x9a\xd6\x06\x0f\x1c8\xb3\xe0\xc0\xc1C\xed\x11\x9ei\x91\xe0\xc0\xd1\xb3\xac\x8dqi\xd4"\xcd\n\x11\xa0y\x95\x19\x1c~\xc4\xf9AaP\x80\xeb\xd8\xb3{j\xd6\xe6F\x00\x030\x86\xac\xff\x08\xe0\xa1\x8d;*\x01\x02\x00X\xcf\xbe\xbd\xfb\xf7\xf0\xe3\xcb\x87\x1f @\x8d~\xcfZ4\x90\x11\xe0F\x1b\x80.V\xb4i\xf3\x8dF\x00\x84\t\x15*<\xa2\xad\xcdCip\xe0\xb8\x82\xa3\'\xd1#dm\xf4\xc0\xe1\xf8\xa8\xcd\xb0bmD\xb6\x81\x04\x87\xd5\x87\x00)\xe3\x04`\xc9\xf2\xc3\x91\x001e\xc6\xccA\xaeM\x1b\r\x01\xce\xb4\xe1\t#\xc0\x10\x7f#\x02\x04\x00P\xd4\xe8Q\xa4I\x95.e\xaa4\xc0SO\xe1\xda\x04\xc9\x00cM\x1b\xacX\x9d\xc9"\x10\xc0\xebW\xb0`\x7fx\xeb#\xed\x10\x1cI\x93\xe0\x10k\xd3vX\x1bip\xe0\xe0i\xd3fZ\xb4H}\xa2=\x82\x03GQ\x00\xc0=f\x04 L\xd8\x88\x84\x00\x89\x15#(\xd7\xc6\xf1\x986\x91\xdb\x84\x19P\x01\x9c\xa1\x00\x99\x01l\xe6\xdc\xd9\xf3g\xd0\xa1E\x87\x0e\x10\x00G?hmT\xb7\t#\xa3\x85\x904m\xbam\tP\xdb\xf6\xed\xdbP\xfc\xf5\x82\xd3\xfbR\xa46\xc1\x85\xb7a\xa3\x07\xff\xceq<\x95\xcc\xf5\xf3\xd7\xbc9\x8f\x00\xd1\x03pZ\x10\x00A\x8dXo\xb2\xd4\xb2B\x02\x0b\x95\x03\x8d\x8c\xb5!_\xde<7\x7f$\x02\x04\x00\xd0\xde\xfd{\xf8\xf1\xe5\xcf\xa7O?\xc0\xfdA\xe8\xda\xb4\x19\x12 \x01@\x17B2\x04\xc8\x80\x86\x9b\x9c\x00\n\x172\\X\xc0\x97?}\x7f\xe0\x04\x9a\x14\xa9M\xa2h\xc8\xf2\xe0\x813\xa9\x9d\xbf\x90"G\xea{\x10\xe0$\xca-O\xa20yC\xe4\xa5 &Iz\x8dk#\xa4B\x9a6hdh\x08\xd3\xa6\x8d\xbb+\x01\x02\x00(j\xf4(\xd2\xa4J\x972m\n @\x00\x05\xbe\xc6\xb5\xc9\x10`L\x9b\xac.\x02\x04i\x93\xcdP\x80\xb0b\xc7\x8aU\xe1\xcf\x9f>=\xb3\xfc\xed\x93\x04\x07\x8e\x9fY\xfe\xe6\xd2\xad[\x97P\x80\xbcz\x17\xccjB\xe4\xaf\x1b"D\x00)I\x92\xea\r\xb2\x047n$\xc8\xf0eE\x801\xea<\x05\xa8\x0c\xe02\xe6\xcc\x9a7s\xee\xec\xf9\xf3\xe5\x00\x018\xd0\xbb&$@\x02\x18\xffB4\x04\xc8\x80\xa6M\x1bc\xaf\x1c\x04\xa8m\xfbv\xed,\xfev\xf3\xee\xed\xfbw\xef\x0f\x01\x86\x13\x9f!\x85\x08\x11A\xc1\xf0=!R\x87\x08*&n\x9e\xc9\xf0\xf0\xa5M\x1b1\x02*\x84\xf3\xe5 @\x00\x00\xe2\xc7\x93/o\xfe<\xfa\xf4\xea\xc9\x07\x08\x10"_\xb56_b\xb0\x08\x92\xa6\r\xfe\xfc\xdf\xac\x04\xe8\xef\x1f`\x00\x81\x03=\xf9\xf3\xa7\xef\n\x14z\xfe\x186t\xf8\x90!\x92\x00\x13)\x06\xc8\xa2\x84\x08 ]\x9fr%!"\xc9\x8e\x9d7\xd0\xda\x944\xd9\x06\xcd\xb8u\x14\x02\x04\x00\xf0\x12fL\x993i\xd6\xb4ysf\x80\x00\x1c\xda\x8dk\xf3\x13(\x99\x00\x01\x04\x08i\xf3\xac\x1c\x89\x00K\x996\xc5\x90\xcf_\xd4\xa8\xeb\xb2\xa8\xe0a\x04\x8a\x95A\xb1\xfcu\xf5\xea/N\x00\xb1c\xc5\x16\xd8C\xa4\x88\xaeO\xa4X\xcdR\xc7*R\x1b\xb9s\xe7\xaa\x93\xf5 @\x00\x00{\xf9\xf6\xf5\xfb\x17p`\xc1\x83\x03\x07\x08\xa0\xe0\xd5\xb96\x8b]\x08\xff\x88\x10\xc0\xc3\x9a \t\xbe\xb41V\xaeF\x00\xcd\x9b7\xf7\xf0\xf7\x19\xf4g\x1fY\xfc\x956}Z\x16\x81\x00\xabY\xb3\xe6p)\x15\xa9O\x9f\xda5ks\x1bw\xeef\xf1\x1a\x05\xf0\r\x00xp\xe1\xc3\x89\x177~\x1c9\xf2\x00\xcb\xab\xd4\xcb\xd6f\x83\x0040\x02\x04\xc8\x10 \x80\x8b6m\x98\x85\x93\xb3\x80A\x80\x00\x07\x02\x94\xa7\xe2\x0f}z\x7fUt\xf8s\xff\x1e\xfe\x88\x00\xf3\xe9\xd7\xa7@\x08\xd7\xa7O\xa6\xac\xb5\xf1\x0f\xb0\x8d\xc0\x81m\xaa\xf9\xe3\x11 !\x80\x85\x0c\x1b:|\x081\xa2\xc4\x89\x14\x17\x06\x08\x80\xa1\xd69g_\x12\xc8H\x10\xc0@\x906$K\xb6\xe9\x12 \x96\xbf\x95\x99\x14\x04\xa8\xe1/&\x16LF\x90(\xf2\x873gN-\x01z\xfa\xecI!\x8e\xbad\xca\x80}:\xba\x8bY\x9b\xa5L\xdb<\x8b\xf7\xeaA\x80\x00\x00\xaaZ\xbd\x8a5\xab\xd6\xad\\\xbbz\xc5\x1a l\x8d|\xe4\xdax\xf1@\xa6\x8d\xda\xb5j\xad\x998\xe2/\xff\xae\xa2\x00\x0e\x02\xd8\xbd\x1bG\xdf\tz\xfe\xfa\xfa\xed\xeb\x0bA\x80\xc1\x01>d)w\xadY\x9b\xc5m\x9a\xc9\x03\xf5\xe9V\xb66\x94)3S\xd7\xceD\x80\xcd\x00:{\xfe\x0c:\xb4\xe8\xd1\xa4K\x9b\x1e\x1d \xb5\x11\x7f\xe3\xda\xb8~\r\xbb\xdb\x94F\xfej\xbf*A \x80\xee\xdd*\xfc\xf9\xd3\xe7/\xb8\xf0\xe0]\xba\xc0:\'\x0eZ\x9b\xe5\xcc\x9bc\xb3\xf5\xe9\x13\xa9om\xda8K\xa7\x0fG\x80\xed\x00\xba{\xff\x0e>\xbc\xf8\xf1\xe4\xcb\x9b?\x1f =\x0ez\xea\x98\xb5y\x0f\x1f~\xb2z\xfef\xadr\xe5j\xd5\xbcWF$\x08\x00\xa8\xc8\xdf@\x82\x04\xed\x1dk\x93P\xe1B\x86m\xc4\xdd\xfa\xf4\tX6e\xf0\xd6\x9d\x08\x90\x11\xc0F\x8e\x1d=~\x04\x19R\xe4H\x92%;\x06@\xd9\x81S=km\\\xbet\x89\xcd\x9f\xabM\x85\n\xedi\xd7F\xa79\x14\x9c\xfc\xfd\x04z\x0eZ\x1b\xa2E\x8d\x1e-\n\x8e\xd4\xa7\\\xf1\xfa!\xa2\x10@*\x00\xaa\xffU\xad^\xc5\x9aU\xebV\xae]\xbdj\r\x106\x80\n_\xf5\xb09k\x93\xb6\xcd8N\xfe\xdc\xfa\x83\'\xeeY\x9b6\xcd\n\x05\x08@\xa1\x8a\xb66}\xfd\xfe\x05\x1c\xd8X\xb0O\x9fN\xc9\t\x908\x00\x00\xc6\x8d\x1d?\x86\x1cY\xf2d\xca\x95-_\x0e\x909\x00\x87B\xfe\xdeq\x83V\xab\x8b?\xd2\xfe\xce\xb5A\x8dZ\x9c\x89\x00\x01\xac$k\x13[\xf6l\xda\xb2\x9ba\x8b\xa7o\x0b\xafO\x9fn\xa1\x08\x10\x00\xc0p\xe2\xc5\x8d\x1fG\x9e\\\xf9r\xe6\xcd\x9d\x17\x0f\x10=\xfa\x07N\x88<\xf9\xc3\xee\xef]\x9b6\xc6\xae\xa9{\x07%@\x00\x1f\xda\xda\x9cG\x9f\x1e=\xb4k\xe8\xfe\xb5\xe3\x82!\xc0|\x0c\xba>\xe1\x82\x12 \x00\x00\xfe\xfd\xfd\x03\x04 p \xc1\x82\x06\x0f"L\xa8p!C\x85\x01\x1eV\xa9\x85\xc5\x1fE\x8a\xf9$\xad\xe2\x02\xa2W\x9f}\xfe>\xc6{\x06\xcd\xd8\xb6j\xe2\xc0\xc1\xeb\xe7o\xde \x1e\x0c\x02\xc0\x8c\x19\x93\x0b\xa8\\(\x02\x04\xff\x00\xa0s\'\xcf\x9e>\x7f\x02\r*t(\xd1\xa2@\x03\x04\x98\xe1/\xcb:\x7fN\x9f\xfas\xd5\xce\x1f\xd5\xaa\xfe\xf2\xe5\x18\x81A@\x80\xae^\xbf\x02\x08+6@\x00\x1c\xb8v\xa9\x08\x10\x00\x00\xdb\xb6n\xdf\xc2\x8d+w.\xdd\xbav\xef\xc6\r\xa0\x17\x93\xbf\xbe~\xff\x02nT"@\x07O\x16\x02 F\x0c`1\xe3\xc6\x8d\x03\x04@\xf0k\x17\x8d\x00\x01\x00`\xce\xacy3\xe7\xce\x9e?\x83\x0e-zt\xe7\x00\x010(\xda\xe2o5\xeb\xd6\xf2\x90\xe0\x802G\x07\x85\x00\xb6\x03\x00\xc8\xad{7o\xdd\x01~[\xc1\xa7"@\x00\x00\xc6\x8f#O\xae|9\xf3\xe6\xce\x9fC\x8f\xce<\x00\xf5\x1f\x88f\xbc\xf2\xa7}\xbb\x8f\x00\xde\xbf{\x07 ~<\xf9\xf2\xe6\x01\x04\x08@A\xdf\x89\x00\x01\x00\xc0\x8f/\x7f>\xfd\xfa\xf6\xef\xe3\xcf\xaf\x7f?\xfe\x00\xfe\x01\x1e\xd0\x81\xa8P\xa1*\x1f\x02$\x04\xb0\x90aC\x87\x0f!.\x0c\x10\x80C\x00\x8b\x000f\xd4\xb8\x91ZcG\x8f\x1fA\x86\x149rd\x00\x93\'M\x02P\xb9\x92eK\x97/[\x06\x90\t\x80fM\x9b7q\xe6\xd4\xb9\x93gO\x9f?\x81\x06\x15:\x94hQ\xa3G\x91&U\xba\x94iS\xa7O\xa1F\x95:\x95jU\xabW\xb1f\xd5\xba\x95kW\xaf_\xc1\x86\x15;\x96lY\xb3g\xd1\xa6\xcd\x19\x10\x00;', logo)
