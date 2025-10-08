#
# PySNMP MIB module QTECH-TRAFFIC-CTRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-TRAFFIC-CTRL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:13:54 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
IfIndex, = mibBuilder.importSymbols("QTECH-TC", "IfIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
qtechTrafficCtrlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14))
qtechTrafficCtrlMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: qtechTrafficCtrlMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: qtechTrafficCtrlMIB.setOrganization('Qtech Networks Co.,Ltd.')
class Percent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 100)

qtechTrafficCtrlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1))
qtechPtTrafficCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1), )
if mibBuilder.loadTexts: qtechPtTrafficCtrlTable.setStatus('current')
qtechPtTrafficCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1), ).setIndexNames((0, "QTECH-TRAFFIC-CTRL-MIB", "qtechPtTrafficCtrlIfIndex"))
if mibBuilder.loadTexts: qtechPtTrafficCtrlEntry.setStatus('current')
qtechPtTrafficCtrlIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1, 1), IfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechPtTrafficCtrlIfIndex.setStatus('current')
qtechPtProtectedPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechPtProtectedPortStatus.setStatus('current')
qtechPtBroadcastStormControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1, 3), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechPtBroadcastStormControlStatus.setStatus('current')
qtechPtMulticastStormControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1, 4), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechPtMulticastStormControlStatus.setStatus('current')
qtechPtUnicastStormControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1, 5), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechPtUnicastStormControlStatus.setStatus('current')
qtechPtBroadcastStormControlLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1, 6), Percent().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechPtBroadcastStormControlLevel.setStatus('current')
qtechPtMulticastStormControlLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1, 7), Percent().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechPtMulticastStormControlLevel.setStatus('current')
qtechPtUnicastStormControlLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 1, 1, 1, 8), Percent().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechPtUnicastStormControlLevel.setStatus('current')
qtechPtTrafficCtrlTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 2))
stormViolationAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("broadcast", 2), ("mutlicast", 3), ("unicast", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: stormViolationAlarmType.setStatus('current')
stormViolationAlarm = NotificationType((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 2, 2)).setObjects(("IF-MIB", "ifIndex"), ("QTECH-TRAFFIC-CTRL-MIB", "stormViolationAlarmType"))
if mibBuilder.loadTexts: stormViolationAlarm.setStatus('current')
qtechPtTrafficCtrlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 3))
qtechPtTrafficCtrlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 3, 1))
qtechPtTrafficCtrlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 3, 2))
qtechPtTrafficCtrlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 3, 1, 1)).setObjects(("QTECH-TRAFFIC-CTRL-MIB", "qtechPtTrafficCtrlMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechPtTrafficCtrlMIBCompliance = qtechPtTrafficCtrlMIBCompliance.setStatus('current')
qtechPtTrafficCtrlMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 14, 3, 2, 1)).setObjects(("QTECH-TRAFFIC-CTRL-MIB", "qtechPtTrafficCtrlIfIndex"), ("QTECH-TRAFFIC-CTRL-MIB", "qtechPtProtectedPortStatus"), ("QTECH-TRAFFIC-CTRL-MIB", "qtechPtBroadcastStormControlStatus"), ("QTECH-TRAFFIC-CTRL-MIB", "qtechPtMulticastStormControlStatus"), ("QTECH-TRAFFIC-CTRL-MIB", "qtechPtUnicastStormControlStatus"), ("QTECH-TRAFFIC-CTRL-MIB", "qtechPtBroadcastStormControlLevel"), ("QTECH-TRAFFIC-CTRL-MIB", "qtechPtMulticastStormControlLevel"), ("QTECH-TRAFFIC-CTRL-MIB", "qtechPtUnicastStormControlLevel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechPtTrafficCtrlMIBGroup = qtechPtTrafficCtrlMIBGroup.setStatus('current')
mibBuilder.exportSymbols("QTECH-TRAFFIC-CTRL-MIB", stormViolationAlarmType=stormViolationAlarmType, qtechPtTrafficCtrlMIBConformance=qtechPtTrafficCtrlMIBConformance, qtechPtBroadcastStormControlLevel=qtechPtBroadcastStormControlLevel, PYSNMP_MODULE_ID=qtechTrafficCtrlMIB, qtechPtTrafficCtrlMIBGroups=qtechPtTrafficCtrlMIBGroups, qtechTrafficCtrlMIB=qtechTrafficCtrlMIB, qtechPtTrafficCtrlIfIndex=qtechPtTrafficCtrlIfIndex, qtechPtBroadcastStormControlStatus=qtechPtBroadcastStormControlStatus, stormViolationAlarm=stormViolationAlarm, qtechPtMulticastStormControlStatus=qtechPtMulticastStormControlStatus, qtechPtUnicastStormControlStatus=qtechPtUnicastStormControlStatus, Percent=Percent, qtechPtTrafficCtrlMIBCompliance=qtechPtTrafficCtrlMIBCompliance, qtechPtTrafficCtrlMIBGroup=qtechPtTrafficCtrlMIBGroup, qtechPtTrafficCtrlTraps=qtechPtTrafficCtrlTraps, qtechPtTrafficCtrlMIBCompliances=qtechPtTrafficCtrlMIBCompliances, qtechPtProtectedPortStatus=qtechPtProtectedPortStatus, qtechPtTrafficCtrlTable=qtechPtTrafficCtrlTable, qtechPtTrafficCtrlEntry=qtechPtTrafficCtrlEntry, qtechPtUnicastStormControlLevel=qtechPtUnicastStormControlLevel, qtechTrafficCtrlMIBObjects=qtechTrafficCtrlMIBObjects, qtechPtMulticastStormControlLevel=qtechPtMulticastStormControlLevel)
