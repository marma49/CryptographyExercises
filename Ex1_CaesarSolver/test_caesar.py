import caesar
import unittest

class TestCaesar(unittest.TestCase):
    def testCaesarCipherShiftMinus200(self):
        self.assertEqual(caesar.caesarCipher("In restaurants, pizza can be baked in an oven", -200), "Qv zmabiczivba, xqhhi kiv jm jisml qv iv wdmv")

    def testCaesarCipherShift200(self):
        self.assertEqual(caesar.caesarCipher("In restaurants, pizza can be baked in an oven", 200), "Af jwklsmjsflk, harrs usf tw tscwv af sf gnwf")

    def testCaesarCipherShift473(self):
        self.assertEqual(caesar.caesarCipher("In restaurants, pizza can be baked in an oven", 473), "Ns wjxyfzwfsyx, uneef hfs gj gfpji ns fs tajs")
    
    def testCeasarBreakerENGText1(self):
        text = "Hm qdrsztqzmsr, ohyyz bzm ad azjdc hm zm nudm vhsg ehqd aqhbjr zanud sgd gdzs rntqbd, zm dkdbsqhb cdbj nudm, z bnmudxnq adks nudm."
        self.assertEqual(caesar.ceasarBreaker(text), """In restaurants, pizza can be baked in an oven with fire bricks above the heat source, an electric deck oven, a conveyor belt oven.""")
        
    def testCeasarBreakerENGText2(self):
        text = "Jifuhx vyauh ni zilg chni u lywiahctuvfy ohcnuls uhx nyllcnilcuf yhncns uliohx nby gcxxfy iz nby 10nb wyhnols ohxyl nby Jcumn xshumns."
        self.assertEqual(caesar.ceasarBreaker(text), "Poland began to form into a recognizable unitary and territorial entity around the middle of the 10th century under the Piast dynasty.")

    def testCeasarBreakerDEText1(self):
        text = "Xolwb xcy xlyc Nycfohayh Jifyhm Yhxy xym 18. Dublbohxylnm pih xyh Huwbvulmnuunyh mychyl Miopyluhcnun vyluovn, ylfuhany Jifyh gcn xyg Pylnlua pih Pylmucffym mychy Ohuvbuhacaeycn 1918 tolowe."
        self.assertNotEqual(caesar.ceasarBreaker(text), "Durch die drei Teilungen Polens Ende des 18. Jahrhunderts von den Nachbarstaaten seiner Souveränität beraubt, erlangte Polen.")

if __name__ == '__main__':
    unittest.main()