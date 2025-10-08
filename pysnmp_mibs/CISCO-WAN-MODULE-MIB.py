#
# PySNMP MIB module CISCO-WAN-MODULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-WAN-MODULE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:30:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanModuleMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 145))
ciscoWanModuleMIB.setRevisions(('2002-09-11 00:00', '2001-07-20 00:00', '1999-10-22 00:00',))
if mibBuilder.loadTexts: ciscoWanModuleMIB.setLastUpdated('200209110000Z')
if mibBuilder.loadTexts: ciscoWanModuleMIB.setOrganization('Cisco Systems, Inc.')
cwmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 1))
cwmConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1))
cwmStatsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2))
class StatisticsLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notApplicable", 0), ("levelOne", 1), ("levelTwo", 2), ("levelThree", 3))

cwmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1), )
if mibBuilder.loadTexts: cwmConfigTable.setStatus('current')
cwmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-MODULE-MIB", "cwmIndex"))
if mibBuilder.loadTexts: cwmConfigEntry.setStatus('current')
cwmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cwmIndex.setStatus('current')
cwmIngressSCTFileId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmIngressSCTFileId.setStatus('current')
cwmIngressSCTFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmIngressSCTFileName.setStatus('current')
cwmAutoLineDiagEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmAutoLineDiagEnable.setStatus('current')
cwmSCTFileVerCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmSCTFileVerCfg.setStatus('current')
cwmSCTFileVerOpr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwmSCTFileVerOpr.setStatus('current')
cwmUploadCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwmUploadCounter.setStatus('current')
cwmStatConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1), )
if mibBuilder.loadTexts: cwmStatConfigTable.setStatus('current')
cwmStatConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-WAN-MODULE-MIB", "cwmIndex"))
if mibBuilder.loadTexts: cwmStatConfigEntry.setStatus('current')
cwmStatBucketInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(5, 10, 15, 20, 30, 60))).clone(namedValues=NamedValues(("five", 5), ("ten", 10), ("fifteen", 15), ("twenty", 20), ("thirty", 30), ("sixty", 60))).clone('fifteen')).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmStatBucketInterval.setStatus('current')
cwmStatCollectionInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 5))).clone(namedValues=NamedValues(("default", 0), ("one", 1), ("five", 5))).clone('default')).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmStatCollectionInterval.setStatus('current')
cwmStatCollectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmStatCollectionStatus.setStatus('current')
cwmStatCurrentLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 4), StatisticsLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwmStatCurrentLevel.setStatus('current')
cwmStatLevelConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 5), StatisticsLevel().clone('levelOne')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmStatLevelConfigured.setStatus('current')
cwmStatMaximumConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwmStatMaximumConnections.setStatus('current')
ciscoWanModuleMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 2))
ciscoWanModuleMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 2, 0))
ciscoWanModuleMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 3))
ciscoWanModuleMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 1))
ciscoWanModuleMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2))
ciscoWanModuleMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 1, 1)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleMIBCompliance = ciscoWanModuleMIBCompliance.setStatus('deprecated')
ciscoWanModuleMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 1, 2)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmConfigGroup"), ("CISCO-WAN-MODULE-MIB", "cwmConfigGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleMIBComplianceRev1 = ciscoWanModuleMIBComplianceRev1.setStatus('deprecated')
ciscoWanModuleMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 1, 3)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmConfigGroup"), ("CISCO-WAN-MODULE-MIB", "cwmConfigGroup2"), ("CISCO-WAN-MODULE-MIB", "cwmUploadGroup"), ("CISCO-WAN-MODULE-MIB", "cwmStatConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleMIBComplianceRev2 = ciscoWanModuleMIBComplianceRev2.setStatus('current')
cwmConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2, 1)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmIngressSCTFileId"), ("CISCO-WAN-MODULE-MIB", "cwmIngressSCTFileName"), ("CISCO-WAN-MODULE-MIB", "cwmAutoLineDiagEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmConfigGroup = cwmConfigGroup.setStatus('current')
cwmStatConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2, 2)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmStatBucketInterval"), ("CISCO-WAN-MODULE-MIB", "cwmStatCurrentLevel"), ("CISCO-WAN-MODULE-MIB", "cwmStatLevelConfigured"), ("CISCO-WAN-MODULE-MIB", "cwmStatCollectionStatus"), ("CISCO-WAN-MODULE-MIB", "cwmStatCollectionInterval"), ("CISCO-WAN-MODULE-MIB", "cwmStatMaximumConnections"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmStatConfigGroup = cwmStatConfigGroup.setStatus('current')
cwmConfigGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2, 3)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmSCTFileVerCfg"), ("CISCO-WAN-MODULE-MIB", "cwmSCTFileVerOpr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmConfigGroup2 = cwmConfigGroup2.setStatus('current')
cwmUploadGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2, 4)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmUploadCounter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmUploadGroup = cwmUploadGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-MODULE-MIB", cwmStatBucketInterval=cwmStatBucketInterval, cwmConfigGroup=cwmConfigGroup, cwmStatCollectionInterval=cwmStatCollectionInterval, cwmStatConfigTable=cwmStatConfigTable, cwmStatConfigGroup=cwmStatConfigGroup, StatisticsLevel=StatisticsLevel, cwmSCTFileVerCfg=cwmSCTFileVerCfg, cwmIngressSCTFileId=cwmIngressSCTFileId, ciscoWanModuleMIBConformance=ciscoWanModuleMIBConformance, cwmConfigEntry=cwmConfigEntry, ciscoWanModuleMIB=ciscoWanModuleMIB, cwmStatMaximumConnections=cwmStatMaximumConnections, PYSNMP_MODULE_ID=ciscoWanModuleMIB, ciscoWanModuleMIBComplianceRev1=ciscoWanModuleMIBComplianceRev1, cwmUploadGroup=cwmUploadGroup, cwmConfigTable=cwmConfigTable, cwmStatLevelConfigured=cwmStatLevelConfigured, cwmStatsConfig=cwmStatsConfig, ciscoWanModuleMIBCompliances=ciscoWanModuleMIBCompliances, cwmMIBObjects=cwmMIBObjects, cwmSCTFileVerOpr=cwmSCTFileVerOpr, cwmIndex=cwmIndex, cwmUploadCounter=cwmUploadCounter, cwmConfig=cwmConfig, cwmStatCurrentLevel=cwmStatCurrentLevel, ciscoWanModuleMIBCompliance=ciscoWanModuleMIBCompliance, cwmConfigGroup2=cwmConfigGroup2, ciscoWanModuleMIBNotificationPrefix=ciscoWanModuleMIBNotificationPrefix, cwmAutoLineDiagEnable=cwmAutoLineDiagEnable, ciscoWanModuleMIBNotifications=ciscoWanModuleMIBNotifications, ciscoWanModuleMIBComplianceRev2=ciscoWanModuleMIBComplianceRev2, cwmStatConfigEntry=cwmStatConfigEntry, cwmStatCollectionStatus=cwmStatCollectionStatus, ciscoWanModuleMIBGroups=ciscoWanModuleMIBGroups, cwmIngressSCTFileName=cwmIngressSCTFileName)
