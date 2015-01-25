from toontown.catalog.CatalogItem import CatalogItem
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.estate import HouseGlobals


class CatalogHouseItem(CatalogItem):
    def makeNewItem(self, houseType):
        self.houseType = houseType

        CatalogItem.makeNewItem(self)

    def decodeDatagram(self, di, versionNumber, store):
        CatalogItem.decodeDatagram(self, di, versionNumber, store)

        self.houseType = di.getUint8()

    def encodeDatagram(self, dg, store):
        CatalogItem.encodeDatagram(self, dg, store)

        dg.addUint8(self.houseType)

    def output(self, store = -1):
        return 'CatalogHouseItem(%s%s)' % (self.houseType, self.formatOptionalData(store))

    def getBasePrice(self):
        return ToontownGlobals.getHousePriceById(self.houseType)

    def getTypeName(self):
        return TTLocalizer.HouseTypeName

    def getName(self):
        return TTLocalizer.getHouseNameById(self.houseType)

    def saveHistory(self):
        return 1

    def isGift(self):
        return False

    def getPicture(self, avatar):
        self.model = loader.loadModel(HouseGlobals.houseModels[self.houseType])
        frame = self.makeFrame()
        self.model.reparentTo(frame)
        self.hasPicture = True
        return (frame, None)

    def cleanupPicture(self):
        CatalogItem.cleanupPicture(self)

        self.model.detachNode()
        self.model = None

    def recordPurchase(self, avatar, optional):
        if avatar:
            print 'Buying a house'
        return ToontownGlobals.P_ItemAvailable