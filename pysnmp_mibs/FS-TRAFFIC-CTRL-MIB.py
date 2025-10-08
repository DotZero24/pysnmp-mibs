#
# PySNMP MIB module FS-TRAFFIC-CTRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-TRAFFIC-CTRL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
IfIndex, = mibBuilder.importSymbols("FS-TC", "IfIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fsTrafficCtrlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14))
fsTrafficCtrlMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: fsTrafficCtrlMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: fsTrafficCtrlMIB.setOrganization('FS.COM Inc..')
class Percent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 100)

fsTrafficCtrlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1))
fsPtTrafficCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1), )
if mibBuilder.loadTexts: fsPtTrafficCtrlTable.setStatus('current')
fsPtTrafficCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1), ).setIndexNames((0, "FS-TRAFFIC-CTRL-MIB", "fsPtTrafficCtrlIfIndex"))
if mibBuilder.loadTexts: fsPtTrafficCtrlEntry.setStatus('current')
fsPtTrafficCtrlIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1, 1), IfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsPtTrafficCtrlIfIndex.setStatus('current')
fsPtProtectedPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsPtProtectedPortStatus.setStatus('current')
fsPtBroadcastStormControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1, 3), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsPtBroadcastStormControlStatus.setStatus('current')
fsPtMulticastStormControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1, 4), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsPtMulticastStormControlStatus.setStatus('current')
fsPtUnicastStormControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1, 5), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsPtUnicastStormControlStatus.setStatus('current')
fsPtBroadcastStormControlLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1, 6), Percent().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsPtBroadcastStormControlLevel.setStatus('current')
fsPtMulticastStormControlLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1, 7), Percent().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsPtMulticastStormControlLevel.setStatus('current')
fsPtUnicastStormControlLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 1, 1, 1, 8), Percent().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsPtUnicastStormControlLevel.setStatus('current')
fsPtTrafficCtrlTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 2))
stormViolationAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("broadcast", 2), ("mutlicast", 3), ("unicast", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: stormViolationAlarmType.setStatus('current')
stormViolationAlarm = NotificationType((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 2, 2)).setObjects(("IF-MIB", "ifIndex"), ("FS-TRAFFIC-CTRL-MIB", "stormViolationAlarmType"))
if mibBuilder.loadTexts: stormViolationAlarm.setStatus('current')
fsPtTrafficCtrlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 3))
fsPtTrafficCtrlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 3, 1))
fsPtTrafficCtrlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 3, 2))
fsPtTrafficCtrlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 3, 1, 1)).setObjects(("FS-TRAFFIC-CTRL-MIB", "fsPtTrafficCtrlMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsPtTrafficCtrlMIBCompliance = fsPtTrafficCtrlMIBCompliance.setStatus('current')
fsPtTrafficCtrlMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 14, 3, 2, 1)).setObjects(("FS-TRAFFIC-CTRL-MIB", "fsPtTrafficCtrlIfIndex"), ("FS-TRAFFIC-CTRL-MIB", "fsPtProtectedPortStatus"), ("FS-TRAFFIC-CTRL-MIB", "fsPtBroadcastStormControlStatus"), ("FS-TRAFFIC-CTRL-MIB", "fsPtMulticastStormControlStatus"), ("FS-TRAFFIC-CTRL-MIB", "fsPtUnicastStormControlStatus"), ("FS-TRAFFIC-CTRL-MIB", "fsPtBroadcastStormControlLevel"), ("FS-TRAFFIC-CTRL-MIB", "fsPtMulticastStormControlLevel"), ("FS-TRAFFIC-CTRL-MIB", "fsPtUnicastStormControlLevel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsPtTrafficCtrlMIBGroup = fsPtTrafficCtrlMIBGroup.setStatus('current')
mibBuilder.exportSymbols("FS-TRAFFIC-CTRL-MIB", PYSNMP_MODULE_ID=fsTrafficCtrlMIB, fsPtBroadcastStormControlStatus=fsPtBroadcastStormControlStatus, stormViolationAlarmType=stormViolationAlarmType, fsTrafficCtrlMIBObjects=fsTrafficCtrlMIBObjects, fsPtTrafficCtrlMIBConformance=fsPtTrafficCtrlMIBConformance, fsPtTrafficCtrlTable=fsPtTrafficCtrlTable, fsPtMulticastStormControlStatus=fsPtMulticastStormControlStatus, stormViolationAlarm=stormViolationAlarm, fsPtTrafficCtrlMIBGroup=fsPtTrafficCtrlMIBGroup, fsPtUnicastStormControlLevel=fsPtUnicastStormControlLevel, Percent=Percent, fsPtBroadcastStormControlLevel=fsPtBroadcastStormControlLevel, fsPtTrafficCtrlTraps=fsPtTrafficCtrlTraps, fsPtTrafficCtrlIfIndex=fsPtTrafficCtrlIfIndex, fsPtMulticastStormControlLevel=fsPtMulticastStormControlLevel, fsPtTrafficCtrlMIBGroups=fsPtTrafficCtrlMIBGroups, fsPtTrafficCtrlMIBCompliance=fsPtTrafficCtrlMIBCompliance, fsPtTrafficCtrlEntry=fsPtTrafficCtrlEntry, fsPtProtectedPortStatus=fsPtProtectedPortStatus, fsPtTrafficCtrlMIBCompliances=fsPtTrafficCtrlMIBCompliances, fsTrafficCtrlMIB=fsTrafficCtrlMIB, fsPtUnicastStormControlStatus=fsPtUnicastStormControlStatus)
