#
# PySNMP MIB module CIE1000-ICFG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CIE1000-ICFG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:20 2025
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
cie1000IcfgMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101))
cie1000IcfgMib.setRevisions(('2016-05-09 00:00', '2014-10-10 00:00', '2014-07-01 00:00',))
if mibBuilder.loadTexts: cie1000IcfgMib.setLastUpdated('201605090000Z')
if mibBuilder.loadTexts: cie1000IcfgMib.setOrganization('Cisco Systems, Inc.')
class CIE1000IcfgConfigStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("none", 0), ("success", 1), ("inProgress", 2), ("errOtherInProcessing", 3), ("errNoSuchFile", 4), ("errSameSrcDst", 5), ("errPermissionDenied", 6), ("errLoadSrc", 7), ("errSaveDst", 8))

class CIE1000IcfgConfigType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("runningConfig", 1), ("startupConfig", 2), ("configFile", 3))

class CIE1000IcfgReloadDefault(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("default", 1), ("defaultKeepIp", 2))

cie1000IcfgMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1))
cie1000IcfgStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3))
cie1000IcfgStatusFileStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 1))
cie1000IcfgStatusFileStatisticsNumberOfFiles = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000IcfgStatusFileStatisticsNumberOfFiles.setStatus('current')
cie1000IcfgStatusFileStatisticsTotalBytes = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000IcfgStatusFileStatisticsTotalBytes.setStatus('current')
cie1000IcfgStatusFileStatisticsFlashSizeBytes = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000IcfgStatusFileStatisticsFlashSizeBytes.setStatus('current')
cie1000IcfgStatusFileStatisticsFlashFreeBytes = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000IcfgStatusFileStatisticsFlashFreeBytes.setStatus('current')
cie1000IcfgStatusFileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 2), )
if mibBuilder.loadTexts: cie1000IcfgStatusFileTable.setStatus('current')
cie1000IcfgStatusFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 2, 1), ).setIndexNames((0, "CIE1000-ICFG-MIB", "cie1000IcfgStatusFileFileNo"))
if mibBuilder.loadTexts: cie1000IcfgStatusFileEntry.setStatus('current')
cie1000IcfgStatusFileFileNo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cie1000IcfgStatusFileFileNo.setStatus('current')
cie1000IcfgStatusFileFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 2, 1, 2), CIE1000DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000IcfgStatusFileFileName.setStatus('current')
cie1000IcfgStatusFileBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000IcfgStatusFileBytes.setStatus('current')
cie1000IcfgStatusFileModifiedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 2, 1, 4), CIE1000DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 39))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000IcfgStatusFileModifiedTime.setStatus('current')
cie1000IcfgStatusFileAttribute = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 2, 1, 5), CIE1000DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000IcfgStatusFileAttribute.setStatus('current')
cie1000IcfgStatusCopyConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 3))
cie1000IcfgStatusCopyConfigStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 3, 1), CIE1000IcfgConfigStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000IcfgStatusCopyConfigStatus.setStatus('current')
cie1000IcfgControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4))
cie1000IcfgControlGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 1))
cie1000IcfgControlGlobalsReloadDefault = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 1, 1), CIE1000IcfgReloadDefault()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000IcfgControlGlobalsReloadDefault.setStatus('current')
cie1000IcfgControlGlobalsDeleteFile = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 1, 2), CIE1000DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000IcfgControlGlobalsDeleteFile.setStatus('current')
cie1000IcfgControlCopyConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 2))
cie1000IcfgControlCopyConfigCopy = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000IcfgControlCopyConfigCopy.setStatus('current')
cie1000IcfgControlCopyConfigSourceConfigType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 2, 2), CIE1000IcfgConfigType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000IcfgControlCopyConfigSourceConfigType.setStatus('current')
cie1000IcfgControlCopyConfigSourceConfigFile = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 2, 3), CIE1000DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000IcfgControlCopyConfigSourceConfigFile.setStatus('current')
cie1000IcfgControlCopyConfigDestinationConfigType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 2, 4), CIE1000IcfgConfigType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000IcfgControlCopyConfigDestinationConfigType.setStatus('current')
cie1000IcfgControlCopyConfigDestinationConfigFile = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 2, 5), CIE1000DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000IcfgControlCopyConfigDestinationConfigFile.setStatus('current')
cie1000IcfgControlCopyConfigMerge = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 2, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000IcfgControlCopyConfigMerge.setStatus('current')
cie1000IcfgMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2))
cie1000IcfgMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2, 1))
cie1000IcfgMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2, 2))
cie1000IcfgStatusFileStatisticsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2, 2, 1)).setObjects(("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileStatisticsNumberOfFiles"), ("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileStatisticsTotalBytes"), ("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileStatisticsFlashSizeBytes"), ("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileStatisticsFlashFreeBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000IcfgStatusFileStatisticsInfoGroup = cie1000IcfgStatusFileStatisticsInfoGroup.setStatus('current')
cie1000IcfgStatusFileTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2, 2, 2)).setObjects(("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileFileNo"), ("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileFileName"), ("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileBytes"), ("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileModifiedTime"), ("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileAttribute"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000IcfgStatusFileTableInfoGroup = cie1000IcfgStatusFileTableInfoGroup.setStatus('current')
cie1000IcfgStatusCopyConfigInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2, 2, 3)).setObjects(("CIE1000-ICFG-MIB", "cie1000IcfgStatusCopyConfigStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000IcfgStatusCopyConfigInfoGroup = cie1000IcfgStatusCopyConfigInfoGroup.setStatus('current')
cie1000IcfgControlGlobalsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2, 2, 4)).setObjects(("CIE1000-ICFG-MIB", "cie1000IcfgControlGlobalsReloadDefault"), ("CIE1000-ICFG-MIB", "cie1000IcfgControlGlobalsDeleteFile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000IcfgControlGlobalsInfoGroup = cie1000IcfgControlGlobalsInfoGroup.setStatus('current')
cie1000IcfgControlCopyConfigInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2, 2, 5)).setObjects(("CIE1000-ICFG-MIB", "cie1000IcfgControlCopyConfigCopy"), ("CIE1000-ICFG-MIB", "cie1000IcfgControlCopyConfigSourceConfigType"), ("CIE1000-ICFG-MIB", "cie1000IcfgControlCopyConfigSourceConfigFile"), ("CIE1000-ICFG-MIB", "cie1000IcfgControlCopyConfigDestinationConfigType"), ("CIE1000-ICFG-MIB", "cie1000IcfgControlCopyConfigDestinationConfigFile"), ("CIE1000-ICFG-MIB", "cie1000IcfgControlCopyConfigMerge"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000IcfgControlCopyConfigInfoGroup = cie1000IcfgControlCopyConfigInfoGroup.setStatus('current')
cie1000IcfgMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2, 1, 1)).setObjects(("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileStatisticsInfoGroup"), ("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileTableInfoGroup"), ("CIE1000-ICFG-MIB", "cie1000IcfgStatusCopyConfigInfoGroup"), ("CIE1000-ICFG-MIB", "cie1000IcfgControlGlobalsInfoGroup"), ("CIE1000-ICFG-MIB", "cie1000IcfgControlCopyConfigInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000IcfgMibCompliance = cie1000IcfgMibCompliance.setStatus('current')
mibBuilder.exportSymbols("CIE1000-ICFG-MIB", cie1000IcfgMibCompliances=cie1000IcfgMibCompliances, cie1000IcfgStatus=cie1000IcfgStatus, cie1000IcfgStatusFileFileName=cie1000IcfgStatusFileFileName, cie1000IcfgMibCompliance=cie1000IcfgMibCompliance, CIE1000IcfgConfigStatus=CIE1000IcfgConfigStatus, CIE1000IcfgConfigType=CIE1000IcfgConfigType, cie1000IcfgStatusFileBytes=cie1000IcfgStatusFileBytes, cie1000IcfgStatusFileStatistics=cie1000IcfgStatusFileStatistics, cie1000IcfgControlCopyConfigSourceConfigFile=cie1000IcfgControlCopyConfigSourceConfigFile, cie1000IcfgStatusCopyConfig=cie1000IcfgStatusCopyConfig, cie1000IcfgStatusFileModifiedTime=cie1000IcfgStatusFileModifiedTime, cie1000IcfgControlCopyConfigSourceConfigType=cie1000IcfgControlCopyConfigSourceConfigType, cie1000IcfgStatusCopyConfigInfoGroup=cie1000IcfgStatusCopyConfigInfoGroup, cie1000IcfgControlCopyConfigDestinationConfigType=cie1000IcfgControlCopyConfigDestinationConfigType, cie1000IcfgControlGlobalsInfoGroup=cie1000IcfgControlGlobalsInfoGroup, cie1000IcfgControlGlobalsDeleteFile=cie1000IcfgControlGlobalsDeleteFile, cie1000IcfgControlCopyConfigDestinationConfigFile=cie1000IcfgControlCopyConfigDestinationConfigFile, cie1000IcfgMib=cie1000IcfgMib, cie1000IcfgControl=cie1000IcfgControl, cie1000IcfgMibGroups=cie1000IcfgMibGroups, cie1000IcfgStatusCopyConfigStatus=cie1000IcfgStatusCopyConfigStatus, cie1000IcfgStatusFileAttribute=cie1000IcfgStatusFileAttribute, cie1000IcfgMibConformance=cie1000IcfgMibConformance, cie1000IcfgStatusFileEntry=cie1000IcfgStatusFileEntry, cie1000IcfgStatusFileFileNo=cie1000IcfgStatusFileFileNo, cie1000IcfgMibObjects=cie1000IcfgMibObjects, CIE1000IcfgReloadDefault=CIE1000IcfgReloadDefault, cie1000IcfgControlGlobals=cie1000IcfgControlGlobals, cie1000IcfgStatusFileStatisticsTotalBytes=cie1000IcfgStatusFileStatisticsTotalBytes, cie1000IcfgStatusFileStatisticsFlashSizeBytes=cie1000IcfgStatusFileStatisticsFlashSizeBytes, PYSNMP_MODULE_ID=cie1000IcfgMib, cie1000IcfgStatusFileStatisticsNumberOfFiles=cie1000IcfgStatusFileStatisticsNumberOfFiles, cie1000IcfgControlCopyConfig=cie1000IcfgControlCopyConfig, cie1000IcfgControlCopyConfigMerge=cie1000IcfgControlCopyConfigMerge, cie1000IcfgStatusFileTableInfoGroup=cie1000IcfgStatusFileTableInfoGroup, cie1000IcfgStatusFileTable=cie1000IcfgStatusFileTable, cie1000IcfgControlGlobalsReloadDefault=cie1000IcfgControlGlobalsReloadDefault, cie1000IcfgControlCopyConfigCopy=cie1000IcfgControlCopyConfigCopy, cie1000IcfgControlCopyConfigInfoGroup=cie1000IcfgControlCopyConfigInfoGroup, cie1000IcfgStatusFileStatisticsFlashFreeBytes=cie1000IcfgStatusFileStatisticsFlashFreeBytes, cie1000IcfgStatusFileStatisticsInfoGroup=cie1000IcfgStatusFileStatisticsInfoGroup)
