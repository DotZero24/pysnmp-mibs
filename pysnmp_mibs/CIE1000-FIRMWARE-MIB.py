#
# PySNMP MIB module CIE1000-FIRMWARE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CIE1000-FIRMWARE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:11:39 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
CIE1000DisplayString, = mibBuilder.importSymbols("CIE1000-TC", "CIE1000DisplayString")
cie1000SwitchMgmt, = mibBuilder.importSymbols("CISCO-IE1000-MIB", "cie1000SwitchMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
cie1000FirmwareMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28))
cie1000FirmwareMib.setRevisions(('2014-12-16 00:00', '2014-10-10 00:00', '2014-07-01 00:00',))
if mibBuilder.loadTexts: cie1000FirmwareMib.setLastUpdated('201412160000Z')
if mibBuilder.loadTexts: cie1000FirmwareMib.setOrganization('Cisco Systems, Inc.')
class CIE1000FirmwareStatusImageEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("bootloader", 0), ("stage2Bootloader", 1), ("activeFirmware", 2), ("alternativeFirmware", 3))

class CIE1000FirmwareUploadImageEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("bootloader", 0), ("firmware", 1))

class CIE1000FirmwareUploadStatusEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("none", 0), ("success", 1), ("inProgress", 2), ("errIvalidIp", 3), ("errTftpFailed", 4), ("errBusy", 5), ("errMemoryInsufficient", 6), ("errInvalidImage", 7), ("errWriteFlash", 8), ("errSameImageExisted", 9), ("errUnknownImage", 10), ("errFlashImageNotFound", 11), ("errFlashEntryNotFound", 12), ("errCrc", 13), ("errImageSize", 14), ("errEraseFlash", 15), ("errIncorrectImageVersion", 16), ("errDownloadUrl", 17), ("errInvalidUrl", 18), ("errInvalidPath", 19), ("errInvalidFilename", 20))

cie1000FirmwareMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1))
cie1000FirmwareStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3))
cie1000FirmwareStatusImageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 1), )
if mibBuilder.loadTexts: cie1000FirmwareStatusImageTable.setStatus('current')
cie1000FirmwareStatusImageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 1, 1), ).setIndexNames((0, "CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageNumber"))
if mibBuilder.loadTexts: cie1000FirmwareStatusImageEntry.setStatus('current')
cie1000FirmwareStatusImageNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cie1000FirmwareStatusImageNumber.setStatus('current')
cie1000FirmwareStatusImageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 1, 1, 2), CIE1000FirmwareStatusImageEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000FirmwareStatusImageType.setStatus('current')
cie1000FirmwareStatusImageName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 1, 1, 3), CIE1000DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000FirmwareStatusImageName.setStatus('current')
cie1000FirmwareStatusImageVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 1, 1, 4), CIE1000DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000FirmwareStatusImageVersion.setStatus('current')
cie1000FirmwareStatusImageBuiltDate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 1, 1, 5), CIE1000DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000FirmwareStatusImageBuiltDate.setStatus('current')
cie1000FirmwareStatusImageCodeRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 1, 1, 6), CIE1000DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000FirmwareStatusImageCodeRevision.setStatus('current')
cie1000FirmwareStatusImageUpload = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 2))
cie1000FirmwareStatusImageUploadStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 2, 1), CIE1000FirmwareUploadStatusEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000FirmwareStatusImageUploadStatus.setStatus('current')
cie1000FirmwareStatusSwitchTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3), )
if mibBuilder.loadTexts: cie1000FirmwareStatusSwitchTable.setStatus('current')
cie1000FirmwareStatusSwitchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3, 1), ).setIndexNames((0, "CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchSwitchId"))
if mibBuilder.loadTexts: cie1000FirmwareStatusSwitchEntry.setStatus('current')
cie1000FirmwareStatusSwitchSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cie1000FirmwareStatusSwitchSwitchId.setStatus('current')
cie1000FirmwareStatusSwitchChipId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3, 1, 2), CIE1000DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000FirmwareStatusSwitchChipId.setStatus('current')
cie1000FirmwareStatusSwitchBoardType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3, 1, 3), CIE1000DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000FirmwareStatusSwitchBoardType.setStatus('current')
cie1000FirmwareStatusSwitchPortCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000FirmwareStatusSwitchPortCnt.setStatus('current')
cie1000FirmwareStatusSwitchProduct = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3, 1, 5), CIE1000DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000FirmwareStatusSwitchProduct.setStatus('current')
cie1000FirmwareStatusSwitchVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3, 1, 6), CIE1000DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000FirmwareStatusSwitchVersion.setStatus('current')
cie1000FirmwareStatusSwitchBuiltDate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3, 1, 7), CIE1000DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000FirmwareStatusSwitchBuiltDate.setStatus('current')
cie1000FirmwareControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 4))
cie1000FirmwareControlGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 4, 1))
cie1000FirmwareControlGlobalsSwapFirmware = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 4, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000FirmwareControlGlobalsSwapFirmware.setStatus('current')
cie1000FirmwareControlImageUpload = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 4, 2))
cie1000FirmwareControlImageUploadDoUpload = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 4, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000FirmwareControlImageUploadDoUpload.setStatus('current')
cie1000FirmwareControlImageUploadImageType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 4, 2, 2), CIE1000FirmwareUploadImageEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000FirmwareControlImageUploadImageType.setStatus('current')
cie1000FirmwareControlImageUploadUrl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 4, 2, 3), CIE1000DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000FirmwareControlImageUploadUrl.setStatus('current')
cie1000FirmwareMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2))
cie1000FirmwareMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2, 1))
cie1000FirmwareMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2, 2))
cie1000FirmwareStatusImageTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2, 2, 1)).setObjects(("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageNumber"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageType"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageName"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageVersion"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageBuiltDate"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageCodeRevision"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000FirmwareStatusImageTableInfoGroup = cie1000FirmwareStatusImageTableInfoGroup.setStatus('current')
cie1000FirmwareStatusImageUploadInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2, 2, 2)).setObjects(("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageUploadStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000FirmwareStatusImageUploadInfoGroup = cie1000FirmwareStatusImageUploadInfoGroup.setStatus('current')
cie1000FirmwareStatusSwitchTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2, 2, 3)).setObjects(("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchSwitchId"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchChipId"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchBoardType"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchPortCnt"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchProduct"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchVersion"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchBuiltDate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000FirmwareStatusSwitchTableInfoGroup = cie1000FirmwareStatusSwitchTableInfoGroup.setStatus('current')
cie1000FirmwareControlGlobalsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2, 2, 4)).setObjects(("CIE1000-FIRMWARE-MIB", "cie1000FirmwareControlGlobalsSwapFirmware"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000FirmwareControlGlobalsInfoGroup = cie1000FirmwareControlGlobalsInfoGroup.setStatus('current')
cie1000FirmwareControlImageUploadInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2, 2, 5)).setObjects(("CIE1000-FIRMWARE-MIB", "cie1000FirmwareControlImageUploadDoUpload"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareControlImageUploadImageType"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareControlImageUploadUrl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000FirmwareControlImageUploadInfoGroup = cie1000FirmwareControlImageUploadInfoGroup.setStatus('current')
cie1000FirmwareMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2, 1, 1)).setObjects(("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageTableInfoGroup"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageUploadInfoGroup"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchTableInfoGroup"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareControlGlobalsInfoGroup"), ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareControlImageUploadInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000FirmwareMibCompliance = cie1000FirmwareMibCompliance.setStatus('current')
mibBuilder.exportSymbols("CIE1000-FIRMWARE-MIB", cie1000FirmwareControlImageUploadImageType=cie1000FirmwareControlImageUploadImageType, CIE1000FirmwareUploadStatusEnum=CIE1000FirmwareUploadStatusEnum, cie1000FirmwareControlImageUploadInfoGroup=cie1000FirmwareControlImageUploadInfoGroup, cie1000FirmwareStatusImageType=cie1000FirmwareStatusImageType, cie1000FirmwareStatusImageCodeRevision=cie1000FirmwareStatusImageCodeRevision, cie1000FirmwareStatusSwitchBuiltDate=cie1000FirmwareStatusSwitchBuiltDate, cie1000FirmwareControlImageUploadUrl=cie1000FirmwareControlImageUploadUrl, cie1000FirmwareStatusImageNumber=cie1000FirmwareStatusImageNumber, cie1000FirmwareMibGroups=cie1000FirmwareMibGroups, cie1000FirmwareMib=cie1000FirmwareMib, cie1000FirmwareStatusSwitchPortCnt=cie1000FirmwareStatusSwitchPortCnt, cie1000FirmwareControlGlobals=cie1000FirmwareControlGlobals, cie1000FirmwareStatusSwitchProduct=cie1000FirmwareStatusSwitchProduct, cie1000FirmwareStatusSwitchChipId=cie1000FirmwareStatusSwitchChipId, cie1000FirmwareControlGlobalsSwapFirmware=cie1000FirmwareControlGlobalsSwapFirmware, cie1000FirmwareStatusSwitchTable=cie1000FirmwareStatusSwitchTable, cie1000FirmwareControl=cie1000FirmwareControl, cie1000FirmwareStatusSwitchSwitchId=cie1000FirmwareStatusSwitchSwitchId, cie1000FirmwareStatusImageUploadInfoGroup=cie1000FirmwareStatusImageUploadInfoGroup, cie1000FirmwareControlGlobalsInfoGroup=cie1000FirmwareControlGlobalsInfoGroup, cie1000FirmwareStatusSwitchBoardType=cie1000FirmwareStatusSwitchBoardType, cie1000FirmwareStatus=cie1000FirmwareStatus, cie1000FirmwareStatusSwitchTableInfoGroup=cie1000FirmwareStatusSwitchTableInfoGroup, cie1000FirmwareMibObjects=cie1000FirmwareMibObjects, cie1000FirmwareMibCompliance=cie1000FirmwareMibCompliance, cie1000FirmwareStatusImageName=cie1000FirmwareStatusImageName, cie1000FirmwareStatusImageUpload=cie1000FirmwareStatusImageUpload, cie1000FirmwareMibCompliances=cie1000FirmwareMibCompliances, CIE1000FirmwareStatusImageEnum=CIE1000FirmwareStatusImageEnum, cie1000FirmwareStatusImageEntry=cie1000FirmwareStatusImageEntry, cie1000FirmwareStatusSwitchVersion=cie1000FirmwareStatusSwitchVersion, cie1000FirmwareControlImageUpload=cie1000FirmwareControlImageUpload, cie1000FirmwareStatusImageUploadStatus=cie1000FirmwareStatusImageUploadStatus, cie1000FirmwareStatusSwitchEntry=cie1000FirmwareStatusSwitchEntry, cie1000FirmwareControlImageUploadDoUpload=cie1000FirmwareControlImageUploadDoUpload, PYSNMP_MODULE_ID=cie1000FirmwareMib, cie1000FirmwareMibConformance=cie1000FirmwareMibConformance, cie1000FirmwareStatusImageTable=cie1000FirmwareStatusImageTable, cie1000FirmwareStatusImageVersion=cie1000FirmwareStatusImageVersion, cie1000FirmwareStatusImageBuiltDate=cie1000FirmwareStatusImageBuiltDate, CIE1000FirmwareUploadImageEnum=CIE1000FirmwareUploadImageEnum, cie1000FirmwareStatusImageTableInfoGroup=cie1000FirmwareStatusImageTableInfoGroup)
