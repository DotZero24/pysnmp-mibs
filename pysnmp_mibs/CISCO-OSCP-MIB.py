#
# PySNMP MIB module CISCO-OSCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-OSCP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:11:39 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
ciscoOscpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 202))
ciscoOscpMIB.setRevisions(('2001-05-18 00:00',))
if mibBuilder.loadTexts: ciscoOscpMIB.setLastUpdated('200105180000Z')
if mibBuilder.loadTexts: ciscoOscpMIB.setOrganization('Cisco Systems, Inc.')
ciscoOscpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 1))
class CoscpSwitchId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class CoscpPortId(TextualConvention, Unsigned32):
    status = 'current'

class CoscpBundleId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class CoscpVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unknown", 1), ("version1", 2))

ciscoOscpBaseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1))
coscpHighestVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 1), CoscpVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpHighestVersion.setStatus('current')
coscpLowestVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 2), CoscpVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLowestVersion.setStatus('current')
coscpSwitchId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 3), CoscpSwitchId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpSwitchId.setStatus('current')
coscpPriorityChangeMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("immediate", 1), ("delayed", 2))).clone('immediate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpPriorityChangeMode.setStatus('current')
coscpHelloHoldDown = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 10000)).clone(100)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpHelloHoldDown.setStatus('current')
coscpHelloInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(150, 30000)).clone(3000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpHelloInterval.setStatus('current')
coscpHelloInactivityFactor = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 50)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpHelloInactivityFactor.setStatus('current')
coscpNotifiesEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpNotifiesEnabled.setStatus('current')
coscpLinkTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2), )
if mibBuilder.loadTexts: coscpLinkTable.setStatus('current')
coscpLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1), ).setIndexNames((0, "CISCO-OSCP-MIB", "coscpLinkPortId"))
if mibBuilder.loadTexts: coscpLinkEntry.setStatus('current')
coscpLinkPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 1), CoscpPortId())
if mibBuilder.loadTexts: coscpLinkPortId.setStatus('current')
coscpLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("dedicatedWavelength", 2), ("inBand", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkType.setStatus('current')
coscpLinkVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 3), CoscpVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkVersion.setStatus('current')
coscpLinkHelloState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("down", 1), ("attempt", 2), ("oneWay", 3), ("twoWay", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkHelloState.setStatus('current')
coscpLinkRemoteSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 5), CoscpSwitchId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkRemoteSwitchId.setStatus('current')
coscpLinkRemotePortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 6), CoscpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkRemotePortId.setStatus('current')
coscpLinkDerivedBundleId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 7), CoscpBundleId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkDerivedBundleId.setStatus('current')
coscpLinkConfigBundleId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 8), CoscpBundleId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpLinkConfigBundleId.setStatus('current')
coscpLinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 9), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkIfIndex.setStatus('current')
coscpLinkSelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpLinkSelPriority.setStatus('current')
coscpLinkInHellos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkInHellos.setStatus('current')
coscpLinkInDiscardedHellos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkInDiscardedHellos.setStatus('current')
coscpLinkOutHellos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkOutHellos.setStatus('current')
coscpLinkTransDown = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkTransDown.setStatus('current')
coscpBundleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3), )
if mibBuilder.loadTexts: coscpBundleTable.setStatus('current')
coscpBundleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1), ).setIndexNames((0, "CISCO-OSCP-MIB", "coscpBundleRemoteSwitchId"), (0, "CISCO-OSCP-MIB", "coscpBundleId"))
if mibBuilder.loadTexts: coscpBundleEntry.setStatus('current')
coscpBundleRemoteSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 1), CoscpSwitchId())
if mibBuilder.loadTexts: coscpBundleRemoteSwitchId.setStatus('current')
coscpBundleId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 2), CoscpBundleId())
if mibBuilder.loadTexts: coscpBundleId.setStatus('current')
coscpBundleActivePortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 3), CoscpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpBundleActivePortId.setStatus('current')
coscpBundleIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpBundleIfIndex.setStatus('current')
coscpBundlePortCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpBundlePortCount.setStatus('current')
coscpBundleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: coscpBundleRowStatus.setStatus('current')
ciscoOscpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 2))
ciscoOscpNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 2, 0))
coscpNotifyTransDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 202, 2, 0, 1)).setObjects(("CISCO-OSCP-MIB", "coscpLinkTransDown"))
if mibBuilder.loadTexts: coscpNotifyTransDown.setStatus('current')
ciscoOscpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 3))
ciscoOscpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 1))
ciscoOscpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 2))
ciscoOscpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 1, 1)).setObjects(("CISCO-OSCP-MIB", "ciscoOscpBasicGroup"), ("CISCO-OSCP-MIB", "ciscoOscpNotificationsGroup"), ("CISCO-OSCP-MIB", "ciscoOscpBundleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOscpMIBCompliance = ciscoOscpMIBCompliance.setStatus('current')
ciscoOscpBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 2, 1)).setObjects(("CISCO-OSCP-MIB", "coscpHighestVersion"), ("CISCO-OSCP-MIB", "coscpLowestVersion"), ("CISCO-OSCP-MIB", "coscpSwitchId"), ("CISCO-OSCP-MIB", "coscpHelloHoldDown"), ("CISCO-OSCP-MIB", "coscpHelloInterval"), ("CISCO-OSCP-MIB", "coscpHelloInactivityFactor"), ("CISCO-OSCP-MIB", "coscpNotifiesEnabled"), ("CISCO-OSCP-MIB", "coscpLinkType"), ("CISCO-OSCP-MIB", "coscpLinkVersion"), ("CISCO-OSCP-MIB", "coscpLinkHelloState"), ("CISCO-OSCP-MIB", "coscpLinkRemoteSwitchId"), ("CISCO-OSCP-MIB", "coscpLinkRemotePortId"), ("CISCO-OSCP-MIB", "coscpLinkIfIndex"), ("CISCO-OSCP-MIB", "coscpLinkInHellos"), ("CISCO-OSCP-MIB", "coscpLinkInDiscardedHellos"), ("CISCO-OSCP-MIB", "coscpLinkOutHellos"), ("CISCO-OSCP-MIB", "coscpLinkTransDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOscpBasicGroup = ciscoOscpBasicGroup.setStatus('current')
ciscoOscpBundleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 2, 2)).setObjects(("CISCO-OSCP-MIB", "coscpPriorityChangeMode"), ("CISCO-OSCP-MIB", "coscpLinkDerivedBundleId"), ("CISCO-OSCP-MIB", "coscpLinkConfigBundleId"), ("CISCO-OSCP-MIB", "coscpLinkSelPriority"), ("CISCO-OSCP-MIB", "coscpBundleActivePortId"), ("CISCO-OSCP-MIB", "coscpBundleIfIndex"), ("CISCO-OSCP-MIB", "coscpBundlePortCount"), ("CISCO-OSCP-MIB", "coscpBundleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOscpBundleGroup = ciscoOscpBundleGroup.setStatus('current')
ciscoOscpNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 2, 3)).setObjects(("CISCO-OSCP-MIB", "coscpNotifyTransDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOscpNotificationsGroup = ciscoOscpNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-OSCP-MIB", coscpBundlePortCount=coscpBundlePortCount, CoscpBundleId=CoscpBundleId, coscpLinkVersion=coscpLinkVersion, coscpBundleIfIndex=coscpBundleIfIndex, coscpHelloHoldDown=coscpHelloHoldDown, coscpLinkInDiscardedHellos=coscpLinkInDiscardedHellos, coscpBundleRowStatus=coscpBundleRowStatus, PYSNMP_MODULE_ID=ciscoOscpMIB, ciscoOscpMIBConformance=ciscoOscpMIBConformance, coscpBundleId=coscpBundleId, ciscoOscpBasicGroup=ciscoOscpBasicGroup, coscpLinkRemotePortId=coscpLinkRemotePortId, ciscoOscpNotificationsPrefix=ciscoOscpNotificationsPrefix, ciscoOscpNotificationsGroup=ciscoOscpNotificationsGroup, coscpNotifiesEnabled=coscpNotifiesEnabled, ciscoOscpBundleGroup=ciscoOscpBundleGroup, coscpHelloInactivityFactor=coscpHelloInactivityFactor, ciscoOscpMIB=ciscoOscpMIB, coscpLinkPortId=coscpLinkPortId, coscpLinkSelPriority=coscpLinkSelPriority, coscpLinkRemoteSwitchId=coscpLinkRemoteSwitchId, ciscoOscpMIBObjects=ciscoOscpMIBObjects, ciscoOscpMIBCompliances=ciscoOscpMIBCompliances, coscpLinkOutHellos=coscpLinkOutHellos, coscpLinkHelloState=coscpLinkHelloState, CoscpSwitchId=CoscpSwitchId, ciscoOscpMIBCompliance=ciscoOscpMIBCompliance, ciscoOscpBaseGroup=ciscoOscpBaseGroup, coscpLinkEntry=coscpLinkEntry, coscpBundleEntry=coscpBundleEntry, coscpLinkTable=coscpLinkTable, coscpLinkIfIndex=coscpLinkIfIndex, coscpBundleTable=coscpBundleTable, coscpLinkConfigBundleId=coscpLinkConfigBundleId, coscpPriorityChangeMode=coscpPriorityChangeMode, coscpLinkInHellos=coscpLinkInHellos, coscpSwitchId=coscpSwitchId, coscpLinkType=coscpLinkType, coscpNotifyTransDown=coscpNotifyTransDown, coscpHighestVersion=coscpHighestVersion, coscpLowestVersion=coscpLowestVersion, coscpLinkDerivedBundleId=coscpLinkDerivedBundleId, ciscoOscpMIBNotifications=ciscoOscpMIBNotifications, CoscpVersion=CoscpVersion, CoscpPortId=CoscpPortId, coscpBundleRemoteSwitchId=coscpBundleRemoteSwitchId, coscpLinkTransDown=coscpLinkTransDown, coscpBundleActivePortId=coscpBundleActivePortId, coscpHelloInterval=coscpHelloInterval, ciscoOscpMIBGroups=ciscoOscpMIBGroups)
