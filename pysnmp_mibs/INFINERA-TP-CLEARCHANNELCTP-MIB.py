#
# PySNMP MIB module INFINERA-TP-CLEARCHANNELCTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-CLEARCHANNELCTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:36 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
InfnServiceType, InfnServiceMode, InfnSMQ, FloatTenths = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnServiceType", "InfnServiceMode", "InfnSMQ", "FloatTenths")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
clearChannelCtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9))
clearChannelCtpMIB.setRevisions(('2008-02-18 00:00',))
if mibBuilder.loadTexts: clearChannelCtpMIB.setLastUpdated('200802180000Z')
if mibBuilder.loadTexts: clearChannelCtpMIB.setOrganization('Infinera')
clearChannelCtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 3))
clearChannelCtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 3, 1))
clearChannelCtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 3, 2))
clearChannelCtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 1), )
if mibBuilder.loadTexts: clearChannelCtpTable.setStatus('current')
clearChannelCtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: clearChannelCtpEntry.setStatus('current')
clearChannelCtpSupportingCircuitIdList = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clearChannelCtpSupportingCircuitIdList.setStatus('current')
clearChannelCtpLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("terminal", 2), ("facility", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clearChannelCtpLoopback.setStatus('current')
clearChannelCtpPmHistStatsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clearChannelCtpPmHistStatsEnable.setStatus('obsolete')
clearChannelCtpConfiguredServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 1, 1, 4), InfnServiceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clearChannelCtpConfiguredServiceType.setStatus('current')
clearChannelCtpServiceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 1, 1, 5), InfnServiceMode().clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: clearChannelCtpServiceMode.setStatus('current')
clearChannelCtpServiceModeQualifier = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 1, 1, 6), InfnSMQ().clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: clearChannelCtpServiceModeQualifier.setStatus('current')
clearChannelCtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 3, 1, 1)).setObjects(("INFINERA-TP-CLEARCHANNELCTP-MIB", "clearChannelCtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clearChannelCtpCompliance = clearChannelCtpCompliance.setStatus('current')
clearChannelCtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 3, 2, 1)).setObjects(("INFINERA-TP-CLEARCHANNELCTP-MIB", "clearChannelCtpSupportingCircuitIdList"), ("INFINERA-TP-CLEARCHANNELCTP-MIB", "clearChannelCtpLoopback"), ("INFINERA-TP-CLEARCHANNELCTP-MIB", "clearChannelCtpPmHistStatsEnable"), ("INFINERA-TP-CLEARCHANNELCTP-MIB", "clearChannelCtpConfiguredServiceType"), ("INFINERA-TP-CLEARCHANNELCTP-MIB", "clearChannelCtpServiceMode"), ("INFINERA-TP-CLEARCHANNELCTP-MIB", "clearChannelCtpServiceModeQualifier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clearChannelCtpGroup = clearChannelCtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-CLEARCHANNELCTP-MIB", clearChannelCtpEntry=clearChannelCtpEntry, clearChannelCtpConformance=clearChannelCtpConformance, clearChannelCtpCompliance=clearChannelCtpCompliance, clearChannelCtpMIB=clearChannelCtpMIB, clearChannelCtpConfiguredServiceType=clearChannelCtpConfiguredServiceType, PYSNMP_MODULE_ID=clearChannelCtpMIB, clearChannelCtpServiceMode=clearChannelCtpServiceMode, clearChannelCtpGroups=clearChannelCtpGroups, clearChannelCtpSupportingCircuitIdList=clearChannelCtpSupportingCircuitIdList, clearChannelCtpServiceModeQualifier=clearChannelCtpServiceModeQualifier, clearChannelCtpTable=clearChannelCtpTable, clearChannelCtpLoopback=clearChannelCtpLoopback, clearChannelCtpPmHistStatsEnable=clearChannelCtpPmHistStatsEnable, clearChannelCtpCompliances=clearChannelCtpCompliances, clearChannelCtpGroup=clearChannelCtpGroup)
