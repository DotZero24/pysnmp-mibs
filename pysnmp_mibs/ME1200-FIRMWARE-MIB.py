#
# PySNMP MIB module ME1200-FIRMWARE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/ME1200-FIRMWARE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:00 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
me1200SwitchMgmt, = mibBuilder.importSymbols("CISCOME1200-MIB", "me1200SwitchMgmt")
ME1200DisplayString, = mibBuilder.importSymbols("ME1200-TC", "ME1200DisplayString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
me1200FirmwareMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28))
me1200FirmwareMIB.setRevisions(('2014-12-16 00:00', '2014-02-18 00:00', '2014-01-29 00:00', '2014-01-20 00:00',))
if mibBuilder.loadTexts: me1200FirmwareMIB.setLastUpdated('201412160000Z')
if mibBuilder.loadTexts: me1200FirmwareMIB.setOrganization('Cisco Systems, Inc')
class ME1200StatusImageType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("bootloader", 0), ("activeFirmware", 1), ("alternativeFirmware", 2))

class ME1200UploadImageType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("bootloader", 0), ("firmware", 1))

class ME1200UploadStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("none", 0), ("success", 1), ("inProgress", 2), ("errIvalidIp", 3), ("errTftpFailed", 4), ("errBusy", 5), ("errMemoryInsufficient", 6), ("errInvalidImage", 7), ("errWriteFlash", 8), ("errSameImageExisted", 9), ("errUnknownImage", 10), ("errFlashImageNotFound", 11), ("errFlashEntryNotFound", 12), ("errCrc", 13), ("errImageSize", 14), ("errEraseFlash", 15), ("errIncorrectImageVersion", 16), ("errDownloadUrl", 17), ("errInvalidUrl", 18))

me1200FirmwareMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1))
me1200FirmwareStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3))
me1200FirmwareStatusImageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 1), )
if mibBuilder.loadTexts: me1200FirmwareStatusImageTable.setStatus('current')
me1200FirmwareStatusImageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 1, 1), ).setIndexNames((0, "ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageNumber"))
if mibBuilder.loadTexts: me1200FirmwareStatusImageEntry.setStatus('current')
me1200FirmwareStatusImageNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: me1200FirmwareStatusImageNumber.setStatus('current')
me1200FirmwareStatusImageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 1, 1, 2), ME1200StatusImageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200FirmwareStatusImageType.setStatus('current')
me1200FirmwareStatusImageName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 1, 1, 3), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200FirmwareStatusImageName.setStatus('current')
me1200FirmwareStatusImageVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 1, 1, 4), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200FirmwareStatusImageVersion.setStatus('current')
me1200FirmwareStatusImageBuiltDate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 1, 1, 5), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200FirmwareStatusImageBuiltDate.setStatus('current')
me1200FirmwareStatusImageCodeRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 1, 1, 6), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200FirmwareStatusImageCodeRevision.setStatus('current')
me1200FirmwareStatusImageUpload = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 2))
me1200FirmwareStatusImageUploadStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 2, 1), ME1200UploadStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200FirmwareStatusImageUploadStatus.setStatus('current')
me1200FirmwareStatusSwitchTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3), )
if mibBuilder.loadTexts: me1200FirmwareStatusSwitchTable.setStatus('current')
me1200FirmwareStatusSwitchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3, 1), ).setIndexNames((0, "ME1200-FIRMWARE-MIB", "me1200FirmwareStatusSwitchSwitchId"))
if mibBuilder.loadTexts: me1200FirmwareStatusSwitchEntry.setStatus('current')
me1200FirmwareStatusSwitchSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: me1200FirmwareStatusSwitchSwitchId.setStatus('current')
me1200FirmwareStatusSwitchChipId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3, 1, 2), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200FirmwareStatusSwitchChipId.setStatus('current')
me1200FirmwareStatusSwitchBoardType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3, 1, 3), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200FirmwareStatusSwitchBoardType.setStatus('current')
me1200FirmwareStatusSwitchPortCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200FirmwareStatusSwitchPortCnt.setStatus('current')
me1200FirmwareStatusSwitchProduct = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3, 1, 5), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200FirmwareStatusSwitchProduct.setStatus('current')
me1200FirmwareStatusSwitchVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3, 1, 6), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200FirmwareStatusSwitchVersion.setStatus('current')
me1200FirmwareStatusSwitchBuiltDate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3, 1, 7), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200FirmwareStatusSwitchBuiltDate.setStatus('current')
me1200FirmwareControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 4))
me1200FirmwareControlGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 4, 1))
me1200FirmwareControlGlobalsSwapFirmware = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 4, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200FirmwareControlGlobalsSwapFirmware.setStatus('current')
me1200FirmwareControlImageUpload = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 4, 2))
me1200FirmwareControlImageUploadDoUpload = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 4, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200FirmwareControlImageUploadDoUpload.setStatus('current')
me1200FirmwareControlImageUploadImageType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 4, 2, 2), ME1200UploadImageType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200FirmwareControlImageUploadImageType.setStatus('current')
me1200FirmwareControlImageUploadUrl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 4, 2, 3), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200FirmwareControlImageUploadUrl.setStatus('current')
me1200FirmwareMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2))
me1200FirmwareMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2, 1))
me1200FirmwareMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2, 2))
me1200FirmwareStatusImageTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2, 2, 1)).setObjects(("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageType"), ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageName"), ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageVersion"), ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageBuiltDate"), ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageCodeRevision"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200FirmwareStatusImageTableInfoGroup = me1200FirmwareStatusImageTableInfoGroup.setStatus('current')
me1200FirmwareStatusImageUploadInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2, 2, 2)).setObjects(("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageUploadStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200FirmwareStatusImageUploadInfoGroup = me1200FirmwareStatusImageUploadInfoGroup.setStatus('current')
me1200FirmwareStatusSwitchTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2, 2, 3)).setObjects(("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusSwitchChipId"), ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusSwitchBoardType"), ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusSwitchPortCnt"), ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusSwitchProduct"), ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusSwitchVersion"), ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusSwitchBuiltDate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200FirmwareStatusSwitchTableInfoGroup = me1200FirmwareStatusSwitchTableInfoGroup.setStatus('current')
me1200FirmwareControlGlobalsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2, 2, 4)).setObjects(("ME1200-FIRMWARE-MIB", "me1200FirmwareControlGlobalsSwapFirmware"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200FirmwareControlGlobalsInfoGroup = me1200FirmwareControlGlobalsInfoGroup.setStatus('current')
me1200FirmwareControlImageUploadInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2, 2, 5)).setObjects(("ME1200-FIRMWARE-MIB", "me1200FirmwareControlImageUploadDoUpload"), ("ME1200-FIRMWARE-MIB", "me1200FirmwareControlImageUploadImageType"), ("ME1200-FIRMWARE-MIB", "me1200FirmwareControlImageUploadUrl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200FirmwareControlImageUploadInfoGroup = me1200FirmwareControlImageUploadInfoGroup.setStatus('current')
me1200FirmwareMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2, 1, 1)).setObjects(("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageTableInfoGroup"), ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageUploadInfoGroup"), ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusSwitchTableInfoGroup"), ("ME1200-FIRMWARE-MIB", "me1200FirmwareControlGlobalsInfoGroup"), ("ME1200-FIRMWARE-MIB", "me1200FirmwareControlImageUploadInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200FirmwareMIBCompliance = me1200FirmwareMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("ME1200-FIRMWARE-MIB", me1200FirmwareStatus=me1200FirmwareStatus, me1200FirmwareStatusSwitchVersion=me1200FirmwareStatusSwitchVersion, me1200FirmwareStatusSwitchChipId=me1200FirmwareStatusSwitchChipId, me1200FirmwareMIBConformance=me1200FirmwareMIBConformance, me1200FirmwareStatusSwitchBoardType=me1200FirmwareStatusSwitchBoardType, me1200FirmwareMIBCompliances=me1200FirmwareMIBCompliances, me1200FirmwareStatusSwitchBuiltDate=me1200FirmwareStatusSwitchBuiltDate, me1200FirmwareStatusSwitchTableInfoGroup=me1200FirmwareStatusSwitchTableInfoGroup, me1200FirmwareMIBCompliance=me1200FirmwareMIBCompliance, me1200FirmwareMIB=me1200FirmwareMIB, me1200FirmwareMIBObjects=me1200FirmwareMIBObjects, me1200FirmwareStatusImageName=me1200FirmwareStatusImageName, me1200FirmwareControl=me1200FirmwareControl, ME1200UploadStatus=ME1200UploadStatus, me1200FirmwareControlImageUploadInfoGroup=me1200FirmwareControlImageUploadInfoGroup, ME1200UploadImageType=ME1200UploadImageType, me1200FirmwareStatusImageTable=me1200FirmwareStatusImageTable, me1200FirmwareStatusSwitchPortCnt=me1200FirmwareStatusSwitchPortCnt, ME1200StatusImageType=ME1200StatusImageType, me1200FirmwareStatusSwitchTable=me1200FirmwareStatusSwitchTable, me1200FirmwareStatusImageUploadStatus=me1200FirmwareStatusImageUploadStatus, PYSNMP_MODULE_ID=me1200FirmwareMIB, me1200FirmwareStatusSwitchSwitchId=me1200FirmwareStatusSwitchSwitchId, me1200FirmwareMIBGroups=me1200FirmwareMIBGroups, me1200FirmwareStatusImageVersion=me1200FirmwareStatusImageVersion, me1200FirmwareControlGlobalsInfoGroup=me1200FirmwareControlGlobalsInfoGroup, me1200FirmwareStatusImageUploadInfoGroup=me1200FirmwareStatusImageUploadInfoGroup, me1200FirmwareControlImageUploadImageType=me1200FirmwareControlImageUploadImageType, me1200FirmwareStatusSwitchEntry=me1200FirmwareStatusSwitchEntry, me1200FirmwareControlImageUploadDoUpload=me1200FirmwareControlImageUploadDoUpload, me1200FirmwareStatusImageEntry=me1200FirmwareStatusImageEntry, me1200FirmwareControlGlobalsSwapFirmware=me1200FirmwareControlGlobalsSwapFirmware, me1200FirmwareControlImageUpload=me1200FirmwareControlImageUpload, me1200FirmwareControlImageUploadUrl=me1200FirmwareControlImageUploadUrl, me1200FirmwareStatusImageNumber=me1200FirmwareStatusImageNumber, me1200FirmwareStatusSwitchProduct=me1200FirmwareStatusSwitchProduct, me1200FirmwareStatusImageCodeRevision=me1200FirmwareStatusImageCodeRevision, me1200FirmwareStatusImageBuiltDate=me1200FirmwareStatusImageBuiltDate, me1200FirmwareStatusImageTableInfoGroup=me1200FirmwareStatusImageTableInfoGroup, me1200FirmwareStatusImageUpload=me1200FirmwareStatusImageUpload, me1200FirmwareStatusImageType=me1200FirmwareStatusImageType, me1200FirmwareControlGlobals=me1200FirmwareControlGlobals)
