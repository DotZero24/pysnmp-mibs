#
# PySNMP MIB module CISCO-INTERFACE-XCVR-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-INTERFACE-XCVR-MONITOR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:11:35 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifName, = mibBuilder.importSymbols("IF-MIB", "ifName")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("CISCO-INTERFACE-XCVR-MONITOR-MIB", cIfXcvrMonStatusChangeNotif=cIfXcvrMonStatusChangeNotif, cIfXcvrMonDigitalDiagTxPwrAlarm=cIfXcvrMonDigitalDiagTxPwrAlarm, cIfXcvrMonDigitalDiagVoltAlarm=cIfXcvrMonDigitalDiagVoltAlarm, cIfXcvrMonStatusChangeNotifGroup=cIfXcvrMonStatusChangeNotifGroup, ciscoInterfaceXcvrMonMIBNotifs=ciscoInterfaceXcvrMonMIBNotifs, ciscoInterfaceXcvrMonMIBObjects=ciscoInterfaceXcvrMonMIBObjects, ciscoInterfaceXcvrMonMIBConform=ciscoInterfaceXcvrMonMIBConform, cIfXcvrMonDigitalDiagTxFaultAlarm=cIfXcvrMonDigitalDiagTxFaultAlarm, cIfXcvrMonDigitalDiagCurrAlarm=cIfXcvrMonDigitalDiagCurrAlarm, cIfXcvrMonDigitalDiagVoltWarning=cIfXcvrMonDigitalDiagVoltWarning, cIfXcvrMonDigitalDiagTempAlarm=cIfXcvrMonDigitalDiagTempAlarm, ciscoInterfaceXcvrMonMIBGroups=ciscoInterfaceXcvrMonMIBGroups, cIfXcvrMonMIBCompliance=cIfXcvrMonMIBCompliance, cIfXcvrMonDigitalDiagRxPwrAlarm=cIfXcvrMonDigitalDiagRxPwrAlarm, PYSNMP_MODULE_ID=ciscoInterfaceXcvrMonitorMIB, ciscoInterfaceXcvrMonitorMIB=ciscoInterfaceXcvrMonitorMIB, cIfXcvrMonDigitalDiagTxPwrWarning=cIfXcvrMonDigitalDiagTxPwrWarning, cIfXcvrMonStatusChangeNotifEnable=cIfXcvrMonStatusChangeNotifEnable, cIfXcvrMonDigitalDiagCurrWarning=cIfXcvrMonDigitalDiagCurrWarning, CiscoInterfaceXcvrMonitorStatus=CiscoInterfaceXcvrMonitorStatus, cIfXcvrMonDigitalDiagTempWarning=cIfXcvrMonDigitalDiagTempWarning, cIfXcvrDigitalDiagMonStatusGroup=cIfXcvrDigitalDiagMonStatusGroup, cIfXcvrMonDigitalDiagRxPwrWarning=cIfXcvrMonDigitalDiagRxPwrWarning, ciscoInterfaceXcvrMonMIBCompliances=ciscoInterfaceXcvrMonMIBCompliances)
