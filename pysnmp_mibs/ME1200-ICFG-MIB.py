#
# PySNMP MIB module ME1200-ICFG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/ME1200-ICFG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:39 2025
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
me1200IcfgMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101))
me1200IcfgMIB.setRevisions(('2014-02-18 00:00', '2014-01-29 00:00', '2014-01-09 00:00',))
if mibBuilder.loadTexts: me1200IcfgMIB.setLastUpdated('201402180000Z')
if mibBuilder.loadTexts: me1200IcfgMIB.setOrganization('Cisco Systems, Inc')
class ME1200ConfigStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("none", 0), ("success", 1), ("inProgress", 2), ("errOtherInProcessing", 3), ("errNoSuchFile", 4), ("errSameSrcDst", 5), ("errPermissionDenied", 6), ("errLoadSrc", 7), ("errSaveDst", 8))

class ME1200ConfigType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("runningConfig", 1), ("startupConfig", 2), ("configFile", 3))

class ME1200ReloadDefault(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("default", 1), ("defaultKeepIp", 2))

me1200IcfgMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1))
me1200IcfgStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3))
me1200IcfgStatusFileStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 1))
me1200IcfgStatusFileStatisticsNumberOfFiles = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200IcfgStatusFileStatisticsNumberOfFiles.setStatus('current')
me1200IcfgStatusFileStatisticsTotalBytes = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200IcfgStatusFileStatisticsTotalBytes.setStatus('current')
me1200IcfgStatusFileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 2), )
if mibBuilder.loadTexts: me1200IcfgStatusFileTable.setStatus('current')
me1200IcfgStatusFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 2, 1), ).setIndexNames((0, "ME1200-ICFG-MIB", "me1200IcfgStatusFileFileNo"))
if mibBuilder.loadTexts: me1200IcfgStatusFileEntry.setStatus('current')
me1200IcfgStatusFileFileNo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: me1200IcfgStatusFileFileNo.setStatus('current')
me1200IcfgStatusFileFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 2, 1, 2), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200IcfgStatusFileFileName.setStatus('current')
me1200IcfgStatusFileBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200IcfgStatusFileBytes.setStatus('current')
me1200IcfgStatusFileModifiedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 2, 1, 4), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 39))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200IcfgStatusFileModifiedTime.setStatus('current')
me1200IcfgStatusFileAttribute = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 2, 1, 5), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200IcfgStatusFileAttribute.setStatus('current')
me1200IcfgStatusCopyConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 3))
me1200IcfgStatusCopyConfigStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 3, 1), ME1200ConfigStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200IcfgStatusCopyConfigStatus.setStatus('current')
me1200IcfgControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4))
me1200IcfgControlGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 1))
me1200IcfgControlGlobalsReloadDefault = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 1, 1), ME1200ReloadDefault()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200IcfgControlGlobalsReloadDefault.setStatus('current')
me1200IcfgControlGlobalsDeleteFile = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 1, 2), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200IcfgControlGlobalsDeleteFile.setStatus('current')
me1200IcfgControlCopyConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 2))
me1200IcfgControlCopyConfigCopy = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200IcfgControlCopyConfigCopy.setStatus('current')
me1200IcfgControlCopyConfigSourceConfigType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 2, 2), ME1200ConfigType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200IcfgControlCopyConfigSourceConfigType.setStatus('current')
me1200IcfgControlCopyConfigSourceConfigFile = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 2, 3), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200IcfgControlCopyConfigSourceConfigFile.setStatus('current')
me1200IcfgControlCopyConfigDestinationConfigType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 2, 4), ME1200ConfigType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200IcfgControlCopyConfigDestinationConfigType.setStatus('current')
me1200IcfgControlCopyConfigDestinationConfigFile = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 2, 5), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200IcfgControlCopyConfigDestinationConfigFile.setStatus('current')
me1200IcfgControlCopyConfigMerge = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 2, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200IcfgControlCopyConfigMerge.setStatus('current')
me1200IcfgMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2))
me1200IcfgMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2, 1))
me1200IcfgMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2, 2))
me1200IcfgStatusFileStatisticsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2, 2, 1)).setObjects(("ME1200-ICFG-MIB", "me1200IcfgStatusFileStatisticsNumberOfFiles"), ("ME1200-ICFG-MIB", "me1200IcfgStatusFileStatisticsTotalBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200IcfgStatusFileStatisticsInfoGroup = me1200IcfgStatusFileStatisticsInfoGroup.setStatus('current')
me1200IcfgStatusFileTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2, 2, 2)).setObjects(("ME1200-ICFG-MIB", "me1200IcfgStatusFileFileName"), ("ME1200-ICFG-MIB", "me1200IcfgStatusFileBytes"), ("ME1200-ICFG-MIB", "me1200IcfgStatusFileModifiedTime"), ("ME1200-ICFG-MIB", "me1200IcfgStatusFileAttribute"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200IcfgStatusFileTableInfoGroup = me1200IcfgStatusFileTableInfoGroup.setStatus('current')
me1200IcfgStatusCopyConfigInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2, 2, 3)).setObjects(("ME1200-ICFG-MIB", "me1200IcfgStatusCopyConfigStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200IcfgStatusCopyConfigInfoGroup = me1200IcfgStatusCopyConfigInfoGroup.setStatus('current')
me1200IcfgControlGlobalsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2, 2, 4)).setObjects(("ME1200-ICFG-MIB", "me1200IcfgControlGlobalsReloadDefault"), ("ME1200-ICFG-MIB", "me1200IcfgControlGlobalsDeleteFile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200IcfgControlGlobalsInfoGroup = me1200IcfgControlGlobalsInfoGroup.setStatus('current')
me1200IcfgControlCopyConfigInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2, 2, 5)).setObjects(("ME1200-ICFG-MIB", "me1200IcfgControlCopyConfigCopy"), ("ME1200-ICFG-MIB", "me1200IcfgControlCopyConfigSourceConfigType"), ("ME1200-ICFG-MIB", "me1200IcfgControlCopyConfigSourceConfigFile"), ("ME1200-ICFG-MIB", "me1200IcfgControlCopyConfigDestinationConfigType"), ("ME1200-ICFG-MIB", "me1200IcfgControlCopyConfigDestinationConfigFile"), ("ME1200-ICFG-MIB", "me1200IcfgControlCopyConfigMerge"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200IcfgControlCopyConfigInfoGroup = me1200IcfgControlCopyConfigInfoGroup.setStatus('current')
me1200IcfgMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2, 1, 1)).setObjects(("ME1200-ICFG-MIB", "me1200IcfgStatusFileStatisticsInfoGroup"), ("ME1200-ICFG-MIB", "me1200IcfgStatusFileTableInfoGroup"), ("ME1200-ICFG-MIB", "me1200IcfgStatusCopyConfigInfoGroup"), ("ME1200-ICFG-MIB", "me1200IcfgControlGlobalsInfoGroup"), ("ME1200-ICFG-MIB", "me1200IcfgControlCopyConfigInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200IcfgMIBCompliance = me1200IcfgMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("ME1200-ICFG-MIB", me1200IcfgControlGlobals=me1200IcfgControlGlobals, me1200IcfgControlGlobalsReloadDefault=me1200IcfgControlGlobalsReloadDefault, me1200IcfgStatusFileStatisticsNumberOfFiles=me1200IcfgStatusFileStatisticsNumberOfFiles, me1200IcfgControlCopyConfigDestinationConfigType=me1200IcfgControlCopyConfigDestinationConfigType, me1200IcfgMIB=me1200IcfgMIB, me1200IcfgControlCopyConfigSourceConfigFile=me1200IcfgControlCopyConfigSourceConfigFile, me1200IcfgStatusFileModifiedTime=me1200IcfgStatusFileModifiedTime, me1200IcfgControlGlobalsDeleteFile=me1200IcfgControlGlobalsDeleteFile, me1200IcfgStatusFileStatistics=me1200IcfgStatusFileStatistics, me1200IcfgStatusFileFileName=me1200IcfgStatusFileFileName, me1200IcfgControlCopyConfigMerge=me1200IcfgControlCopyConfigMerge, ME1200ConfigStatus=ME1200ConfigStatus, me1200IcfgControlCopyConfigDestinationConfigFile=me1200IcfgControlCopyConfigDestinationConfigFile, me1200IcfgStatusFileStatisticsInfoGroup=me1200IcfgStatusFileStatisticsInfoGroup, me1200IcfgStatusFileStatisticsTotalBytes=me1200IcfgStatusFileStatisticsTotalBytes, me1200IcfgStatusFileFileNo=me1200IcfgStatusFileFileNo, me1200IcfgControl=me1200IcfgControl, me1200IcfgControlCopyConfigCopy=me1200IcfgControlCopyConfigCopy, me1200IcfgStatus=me1200IcfgStatus, me1200IcfgStatusFileTableInfoGroup=me1200IcfgStatusFileTableInfoGroup, ME1200ConfigType=ME1200ConfigType, me1200IcfgStatusFileTable=me1200IcfgStatusFileTable, me1200IcfgMIBObjects=me1200IcfgMIBObjects, me1200IcfgControlCopyConfig=me1200IcfgControlCopyConfig, PYSNMP_MODULE_ID=me1200IcfgMIB, me1200IcfgStatusCopyConfigInfoGroup=me1200IcfgStatusCopyConfigInfoGroup, me1200IcfgMIBGroups=me1200IcfgMIBGroups, me1200IcfgMIBCompliances=me1200IcfgMIBCompliances, me1200IcfgStatusCopyConfig=me1200IcfgStatusCopyConfig, me1200IcfgMIBCompliance=me1200IcfgMIBCompliance, me1200IcfgMIBConformance=me1200IcfgMIBConformance, me1200IcfgStatusFileEntry=me1200IcfgStatusFileEntry, me1200IcfgControlGlobalsInfoGroup=me1200IcfgControlGlobalsInfoGroup, me1200IcfgStatusCopyConfigStatus=me1200IcfgStatusCopyConfigStatus, me1200IcfgStatusFileAttribute=me1200IcfgStatusFileAttribute, me1200IcfgControlCopyConfigInfoGroup=me1200IcfgControlCopyConfigInfoGroup, me1200IcfgStatusFileBytes=me1200IcfgStatusFileBytes, me1200IcfgControlCopyConfigSourceConfigType=me1200IcfgControlCopyConfigSourceConfigType, ME1200ReloadDefault=ME1200ReloadDefault)
