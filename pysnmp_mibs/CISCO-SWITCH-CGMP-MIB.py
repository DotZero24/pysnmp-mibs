#
# PySNMP MIB module CISCO-SWITCH-CGMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-SWITCH-CGMP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:39 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention")
ciscoSwitchCgmpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 101))
ciscoSwitchCgmpMIB.setRevisions(('1998-05-07 00:00',))
if mibBuilder.loadTexts: ciscoSwitchCgmpMIB.setLastUpdated('9805070000Z')
if mibBuilder.loadTexts: ciscoSwitchCgmpMIB.setOrganization('Cisco Systems, Inc')
ciscoSwitchCgmpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 1))
sCgmpInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1))
class SCgmpVlanIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1023)

sCgmpEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sCgmpEnable.setStatus('current')
sCgmpFastLeaveEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sCgmpFastLeaveEnable.setStatus('current')
sCgmpRouterHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 6000))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sCgmpRouterHoldTime.setStatus('current')
sCgmpRouterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4), )
if mibBuilder.loadTexts: sCgmpRouterTable.setStatus('current')
sCgmpRouterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-SWITCH-CGMP-MIB", "sCgmpRouterVlanIndex"), (0, "BRIDGE-MIB", "dot1dBasePort"), (0, "CISCO-SWITCH-CGMP-MIB", "sCgmpRouterMacAddress"))
if mibBuilder.loadTexts: sCgmpRouterEntry.setStatus('current')
sCgmpRouterVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1, 1), SCgmpVlanIndex())
if mibBuilder.loadTexts: sCgmpRouterVlanIndex.setStatus('current')
sCgmpRouterMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1, 3), MacAddress())
if mibBuilder.loadTexts: sCgmpRouterMacAddress.setStatus('current')
sCgmpRouterEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sCgmpRouterEntryStatus.setStatus('current')
ciscoSwitchCgmpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 3))
ciscoSwitchCgmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 1))
ciscoSwitchCgmpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 2))
ciscoSwitchCgmpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 1, 1)).setObjects(("CISCO-SWITCH-CGMP-MIB", "sCgmpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchCgmpMIBCompliance = ciscoSwitchCgmpMIBCompliance.setStatus('current')
sCgmpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 2, 1)).setObjects(("CISCO-SWITCH-CGMP-MIB", "sCgmpEnable"), ("CISCO-SWITCH-CGMP-MIB", "sCgmpFastLeaveEnable"), ("CISCO-SWITCH-CGMP-MIB", "sCgmpRouterHoldTime"), ("CISCO-SWITCH-CGMP-MIB", "sCgmpRouterEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sCgmpGroup = sCgmpGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-CGMP-MIB", sCgmpRouterMacAddress=sCgmpRouterMacAddress, ciscoSwitchCgmpMIB=ciscoSwitchCgmpMIB, sCgmpFastLeaveEnable=sCgmpFastLeaveEnable, sCgmpRouterHoldTime=sCgmpRouterHoldTime, SCgmpVlanIndex=SCgmpVlanIndex, ciscoSwitchCgmpMIBCompliance=ciscoSwitchCgmpMIBCompliance, ciscoSwitchCgmpMIBGroups=ciscoSwitchCgmpMIBGroups, sCgmpRouterVlanIndex=sCgmpRouterVlanIndex, PYSNMP_MODULE_ID=ciscoSwitchCgmpMIB, ciscoSwitchCgmpMIBConformance=ciscoSwitchCgmpMIBConformance, sCgmpEnable=sCgmpEnable, sCgmpInfo=sCgmpInfo, sCgmpRouterEntry=sCgmpRouterEntry, ciscoSwitchCgmpMIBCompliances=ciscoSwitchCgmpMIBCompliances, sCgmpGroup=sCgmpGroup, sCgmpRouterEntryStatus=sCgmpRouterEntryStatus, sCgmpRouterTable=sCgmpRouterTable, ciscoSwitchCgmpMIBObjects=ciscoSwitchCgmpMIBObjects)
