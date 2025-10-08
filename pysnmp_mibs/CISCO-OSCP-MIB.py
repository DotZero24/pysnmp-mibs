#
# PySNMP MIB module CISCO-OSCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-OSCP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:23:49 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-OSCP-MIB", coscpLinkPortId=coscpLinkPortId, coscpBundleEntry=coscpBundleEntry, ciscoOscpMIBConformance=ciscoOscpMIBConformance, coscpSwitchId=coscpSwitchId, CoscpVersion=CoscpVersion, ciscoOscpMIBObjects=ciscoOscpMIBObjects, coscpBundleActivePortId=coscpBundleActivePortId, CoscpPortId=CoscpPortId, coscpLinkConfigBundleId=coscpLinkConfigBundleId, coscpHighestVersion=coscpHighestVersion, coscpPriorityChangeMode=coscpPriorityChangeMode, coscpBundleIfIndex=coscpBundleIfIndex, ciscoOscpMIBCompliances=ciscoOscpMIBCompliances, CoscpBundleId=CoscpBundleId, coscpNotifiesEnabled=coscpNotifiesEnabled, coscpHelloHoldDown=coscpHelloHoldDown, coscpLinkInHellos=coscpLinkInHellos, coscpLinkHelloState=coscpLinkHelloState, coscpLinkDerivedBundleId=coscpLinkDerivedBundleId, coscpBundleTable=coscpBundleTable, coscpBundleRemoteSwitchId=coscpBundleRemoteSwitchId, coscpNotifyTransDown=coscpNotifyTransDown, ciscoOscpNotificationsGroup=ciscoOscpNotificationsGroup, ciscoOscpMIB=ciscoOscpMIB, coscpBundleRowStatus=coscpBundleRowStatus, ciscoOscpBundleGroup=ciscoOscpBundleGroup, ciscoOscpMIBGroups=ciscoOscpMIBGroups, CoscpSwitchId=CoscpSwitchId, coscpLinkEntry=coscpLinkEntry, coscpHelloInactivityFactor=coscpHelloInactivityFactor, ciscoOscpNotificationsPrefix=ciscoOscpNotificationsPrefix, ciscoOscpMIBNotifications=ciscoOscpMIBNotifications, coscpLinkRemoteSwitchId=coscpLinkRemoteSwitchId, ciscoOscpBasicGroup=ciscoOscpBasicGroup, coscpLinkInDiscardedHellos=coscpLinkInDiscardedHellos, PYSNMP_MODULE_ID=ciscoOscpMIB, coscpLinkTable=coscpLinkTable, coscpLinkRemotePortId=coscpLinkRemotePortId, coscpLinkTransDown=coscpLinkTransDown, coscpLinkType=coscpLinkType, coscpLinkVersion=coscpLinkVersion, coscpHelloInterval=coscpHelloInterval, coscpBundlePortCount=coscpBundlePortCount, coscpLinkIfIndex=coscpLinkIfIndex, ciscoOscpMIBCompliance=ciscoOscpMIBCompliance, coscpBundleId=coscpBundleId, coscpLinkOutHellos=coscpLinkOutHellos, coscpLowestVersion=coscpLowestVersion, coscpLinkSelPriority=coscpLinkSelPriority, ciscoOscpBaseGroup=ciscoOscpBaseGroup)
