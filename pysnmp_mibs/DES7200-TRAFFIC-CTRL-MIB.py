#
# PySNMP MIB module DES7200-TRAFFIC-CTRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DES7200-TRAFFIC-CTRL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:34:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
myMgmt, = mibBuilder.importSymbols("DES7200-SMI", "myMgmt")
MemberMap, IfIndex, ConfigStatus = mibBuilder.importSymbols("DES7200-TC", "MemberMap", "IfIndex", "ConfigStatus")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
myTrafficCtrlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14))
myTrafficCtrlMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: myTrafficCtrlMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: myTrafficCtrlMIB.setOrganization('$Company$')
class Percent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 100)

myTrafficCtrlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 1))
myPtTrafficCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 1, 1), )
if mibBuilder.loadTexts: myPtTrafficCtrlTable.setStatus('current')
myPtTrafficCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 1, 1, 1), ).setIndexNames((0, "DES7200-TRAFFIC-CTRL-MIB", "myPtTrafficCtrlIfIndex"))
if mibBuilder.loadTexts: myPtTrafficCtrlEntry.setStatus('current')
myPtTrafficCtrlIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 1, 1, 1, 1), IfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myPtTrafficCtrlIfIndex.setStatus('current')
myPtProtectedPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 1, 1, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myPtProtectedPortStatus.setStatus('current')
myPtBroadcastStormControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 1, 1, 1, 3), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myPtBroadcastStormControlStatus.setStatus('current')
myPtMulticastStormControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 1, 1, 1, 4), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myPtMulticastStormControlStatus.setStatus('current')
myPtUnicastStormControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 1, 1, 1, 5), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myPtUnicastStormControlStatus.setStatus('current')
myPtBroadcastStormControlLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 1, 1, 1, 6), Percent().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myPtBroadcastStormControlLevel.setStatus('current')
myPtMulticastStormControlLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 1, 1, 1, 7), Percent().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myPtMulticastStormControlLevel.setStatus('current')
myPtUnicastStormControlLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 1, 1, 1, 8), Percent().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myPtUnicastStormControlLevel.setStatus('current')
myPtTrafficCtrlTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 2))
stormViolationAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("broadcast", 2), ("mutlicast", 3), ("unicast", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: stormViolationAlarmType.setStatus('current')
stormViolationAlarm = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 2, 2)).setObjects(("IF-MIB", "ifIndex"), ("DES7200-TRAFFIC-CTRL-MIB", "stormViolationAlarmType"))
if mibBuilder.loadTexts: stormViolationAlarm.setStatus('current')
myPtTrafficCtrlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 3))
myPtTrafficCtrlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 3, 1))
myPtTrafficCtrlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 3, 2))
myPtTrafficCtrlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 3, 1, 1)).setObjects(("DES7200-TRAFFIC-CTRL-MIB", "myPtTrafficCtrlMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myPtTrafficCtrlMIBCompliance = myPtTrafficCtrlMIBCompliance.setStatus('current')
myPtTrafficCtrlMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 14, 3, 2, 1)).setObjects(("DES7200-TRAFFIC-CTRL-MIB", "myPtTrafficCtrlIfIndex"), ("DES7200-TRAFFIC-CTRL-MIB", "myPtProtectedPortStatus"), ("DES7200-TRAFFIC-CTRL-MIB", "myPtBroadcastStormControlStatus"), ("DES7200-TRAFFIC-CTRL-MIB", "myPtMulticastStormControlStatus"), ("DES7200-TRAFFIC-CTRL-MIB", "myPtUnicastStormControlStatus"), ("DES7200-TRAFFIC-CTRL-MIB", "myPtBroadcastStormControlLevel"), ("DES7200-TRAFFIC-CTRL-MIB", "myPtMulticastStormControlLevel"), ("DES7200-TRAFFIC-CTRL-MIB", "myPtUnicastStormControlLevel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myPtTrafficCtrlMIBGroup = myPtTrafficCtrlMIBGroup.setStatus('current')
mibBuilder.exportSymbols("DES7200-TRAFFIC-CTRL-MIB", myPtTrafficCtrlMIBCompliance=myPtTrafficCtrlMIBCompliance, myPtTrafficCtrlMIBGroup=myPtTrafficCtrlMIBGroup, myPtBroadcastStormControlLevel=myPtBroadcastStormControlLevel, myPtUnicastStormControlLevel=myPtUnicastStormControlLevel, stormViolationAlarmType=stormViolationAlarmType, myPtTrafficCtrlEntry=myPtTrafficCtrlEntry, myPtMulticastStormControlLevel=myPtMulticastStormControlLevel, Percent=Percent, stormViolationAlarm=stormViolationAlarm, PYSNMP_MODULE_ID=myTrafficCtrlMIB, myPtTrafficCtrlMIBGroups=myPtTrafficCtrlMIBGroups, myPtTrafficCtrlIfIndex=myPtTrafficCtrlIfIndex, myPtMulticastStormControlStatus=myPtMulticastStormControlStatus, myPtTrafficCtrlMIBConformance=myPtTrafficCtrlMIBConformance, myPtBroadcastStormControlStatus=myPtBroadcastStormControlStatus, myPtTrafficCtrlMIBCompliances=myPtTrafficCtrlMIBCompliances, myTrafficCtrlMIBObjects=myTrafficCtrlMIBObjects, myTrafficCtrlMIB=myTrafficCtrlMIB, myPtUnicastStormControlStatus=myPtUnicastStormControlStatus, myPtTrafficCtrlTable=myPtTrafficCtrlTable, myPtProtectedPortStatus=myPtProtectedPortStatus, myPtTrafficCtrlTraps=myPtTrafficCtrlTraps)
