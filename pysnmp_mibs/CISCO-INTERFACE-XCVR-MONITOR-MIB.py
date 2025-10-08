#
# PySNMP MIB module CISCO-INTERFACE-XCVR-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-INTERFACE-XCVR-MONITOR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:23:44 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifName, = mibBuilder.importSymbols("IF-MIB", "ifName")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoInterfaceXcvrMonitorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 706))
ciscoInterfaceXcvrMonitorMIB.setRevisions(('2009-10-09 00:00',))
if mibBuilder.loadTexts: ciscoInterfaceXcvrMonitorMIB.setLastUpdated('200910090000Z')
if mibBuilder.loadTexts: ciscoInterfaceXcvrMonitorMIB.setOrganization('Cisco Systems, Inc.')
class CiscoInterfaceXcvrMonitorStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("highSet", 1), ("lowSet", 2), ("highClear", 3), ("lowClear", 4), ("normal", 5))

ciscoInterfaceXcvrMonMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 706, 0))
ciscoInterfaceXcvrMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 706, 1))
ciscoInterfaceXcvrMonMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 706, 2))
cIfXcvrMonDigitalDiagTempAlarm = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 1), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagTempAlarm.setStatus('current')
cIfXcvrMonDigitalDiagTempWarning = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 2), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagTempWarning.setStatus('current')
cIfXcvrMonDigitalDiagVoltAlarm = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 3), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagVoltAlarm.setStatus('current')
cIfXcvrMonDigitalDiagVoltWarning = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 4), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagVoltWarning.setStatus('current')
cIfXcvrMonDigitalDiagCurrAlarm = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 5), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagCurrAlarm.setStatus('current')
cIfXcvrMonDigitalDiagCurrWarning = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 6), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagCurrWarning.setStatus('current')
cIfXcvrMonDigitalDiagRxPwrAlarm = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 7), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagRxPwrAlarm.setStatus('current')
cIfXcvrMonDigitalDiagRxPwrWarning = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 8), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagRxPwrWarning.setStatus('current')
cIfXcvrMonDigitalDiagTxPwrAlarm = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 9), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagTxPwrAlarm.setStatus('current')
cIfXcvrMonDigitalDiagTxPwrWarning = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 10), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagTxPwrWarning.setStatus('current')
cIfXcvrMonDigitalDiagTxFaultAlarm = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 11), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagTxFaultAlarm.setStatus('current')
cIfXcvrMonStatusChangeNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cIfXcvrMonStatusChangeNotifEnable.setStatus('current')
cIfXcvrMonStatusChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 706, 0, 1)).setObjects(("IF-MIB", "ifName"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTempAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTempWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagVoltAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagVoltWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagCurrAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagCurrWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagRxPwrAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagRxPwrWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxPwrAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxPwrWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxFaultAlarm"))
if mibBuilder.loadTexts: cIfXcvrMonStatusChangeNotif.setStatus('current')
ciscoInterfaceXcvrMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 706, 2, 1))
ciscoInterfaceXcvrMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 706, 2, 2))
cIfXcvrMonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 706, 2, 1, 1)).setObjects(("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrDigitalDiagMonStatusGroup"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonStatusChangeNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIfXcvrMonMIBCompliance = cIfXcvrMonMIBCompliance.setStatus('current')
cIfXcvrDigitalDiagMonStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 706, 2, 2, 1)).setObjects(("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTempAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTempWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagVoltAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagVoltWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagCurrAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagCurrWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagRxPwrAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagRxPwrWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxPwrAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxPwrWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxFaultAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonStatusChangeNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIfXcvrDigitalDiagMonStatusGroup = cIfXcvrDigitalDiagMonStatusGroup.setStatus('current')
cIfXcvrMonStatusChangeNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 706, 2, 2, 2)).setObjects(("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonStatusChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIfXcvrMonStatusChangeNotifGroup = cIfXcvrMonStatusChangeNotifGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-INTERFACE-XCVR-MONITOR-MIB", cIfXcvrMonStatusChangeNotif=cIfXcvrMonStatusChangeNotif, CiscoInterfaceXcvrMonitorStatus=CiscoInterfaceXcvrMonitorStatus, cIfXcvrMonDigitalDiagTempAlarm=cIfXcvrMonDigitalDiagTempAlarm, cIfXcvrMonDigitalDiagTxFaultAlarm=cIfXcvrMonDigitalDiagTxFaultAlarm, ciscoInterfaceXcvrMonitorMIB=ciscoInterfaceXcvrMonitorMIB, cIfXcvrMonDigitalDiagVoltAlarm=cIfXcvrMonDigitalDiagVoltAlarm, ciscoInterfaceXcvrMonMIBNotifs=ciscoInterfaceXcvrMonMIBNotifs, cIfXcvrMonDigitalDiagRxPwrWarning=cIfXcvrMonDigitalDiagRxPwrWarning, ciscoInterfaceXcvrMonMIBConform=ciscoInterfaceXcvrMonMIBConform, cIfXcvrMonDigitalDiagTempWarning=cIfXcvrMonDigitalDiagTempWarning, ciscoInterfaceXcvrMonMIBGroups=ciscoInterfaceXcvrMonMIBGroups, cIfXcvrMonDigitalDiagRxPwrAlarm=cIfXcvrMonDigitalDiagRxPwrAlarm, cIfXcvrMonStatusChangeNotifGroup=cIfXcvrMonStatusChangeNotifGroup, cIfXcvrMonStatusChangeNotifEnable=cIfXcvrMonStatusChangeNotifEnable, ciscoInterfaceXcvrMonMIBObjects=ciscoInterfaceXcvrMonMIBObjects, cIfXcvrMonDigitalDiagTxPwrAlarm=cIfXcvrMonDigitalDiagTxPwrAlarm, cIfXcvrMonDigitalDiagCurrWarning=cIfXcvrMonDigitalDiagCurrWarning, cIfXcvrMonDigitalDiagCurrAlarm=cIfXcvrMonDigitalDiagCurrAlarm, cIfXcvrMonMIBCompliance=cIfXcvrMonMIBCompliance, cIfXcvrMonDigitalDiagVoltWarning=cIfXcvrMonDigitalDiagVoltWarning, cIfXcvrDigitalDiagMonStatusGroup=cIfXcvrDigitalDiagMonStatusGroup, ciscoInterfaceXcvrMonMIBCompliances=ciscoInterfaceXcvrMonMIBCompliances, cIfXcvrMonDigitalDiagTxPwrWarning=cIfXcvrMonDigitalDiagTxPwrWarning, PYSNMP_MODULE_ID=ciscoInterfaceXcvrMonitorMIB)
