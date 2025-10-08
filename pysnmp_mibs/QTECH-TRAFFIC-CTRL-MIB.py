#
# PySNMP MIB module QTECH-TRAFFIC-CTRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-TRAFFIC-CTRL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
IfIndex, = mibBuilder.importSymbols("QTECH-TC", "IfIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("QTECH-TRAFFIC-CTRL-MIB", qtechPtUnicastStormControlLevel=qtechPtUnicastStormControlLevel, qtechPtTrafficCtrlMIBConformance=qtechPtTrafficCtrlMIBConformance, stormViolationAlarmType=stormViolationAlarmType, qtechPtTrafficCtrlMIBGroup=qtechPtTrafficCtrlMIBGroup, Percent=Percent, stormViolationAlarm=stormViolationAlarm, qtechPtMulticastStormControlLevel=qtechPtMulticastStormControlLevel, qtechPtTrafficCtrlMIBCompliance=qtechPtTrafficCtrlMIBCompliance, qtechPtUnicastStormControlStatus=qtechPtUnicastStormControlStatus, qtechPtBroadcastStormControlLevel=qtechPtBroadcastStormControlLevel, qtechPtTrafficCtrlEntry=qtechPtTrafficCtrlEntry, qtechPtTrafficCtrlTable=qtechPtTrafficCtrlTable, PYSNMP_MODULE_ID=qtechTrafficCtrlMIB, qtechPtMulticastStormControlStatus=qtechPtMulticastStormControlStatus, qtechPtTrafficCtrlMIBCompliances=qtechPtTrafficCtrlMIBCompliances, qtechPtTrafficCtrlIfIndex=qtechPtTrafficCtrlIfIndex, qtechTrafficCtrlMIBObjects=qtechTrafficCtrlMIBObjects, qtechPtBroadcastStormControlStatus=qtechPtBroadcastStormControlStatus, qtechPtTrafficCtrlMIBGroups=qtechPtTrafficCtrlMIBGroups, qtechPtProtectedPortStatus=qtechPtProtectedPortStatus, qtechTrafficCtrlMIB=qtechTrafficCtrlMIB, qtechPtTrafficCtrlTraps=qtechPtTrafficCtrlTraps)
