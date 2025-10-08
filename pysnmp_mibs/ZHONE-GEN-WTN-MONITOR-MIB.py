#
# PySNMP MIB module ZHONE-GEN-WTN-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zhone/ZHONE-GEN-WTN-MONITOR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zhoneModules, zhoneGenWtn = mibBuilder.importSymbols("Zhone", "zhoneModules", "zhoneGenWtn")
zhoneGenWtnMonitorModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 102))
zhoneGenWtnMonitorModule.setRevisions(('1901-05-25 21:36',))
if mibBuilder.loadTexts: zhoneGenWtnMonitorModule.setLastUpdated('0009281216Z')
if mibBuilder.loadTexts: zhoneGenWtnMonitorModule.setOrganization('Zhone Technologies, Inc.')
wtnMonitor = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 3, 9, 1))
if mibBuilder.loadTexts: wtnMonitor.setStatus('current')
wtnLedStatus = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 9, 1, 1), Bits().clone(namedValues=NamedValues(("diag", 0), ("operational", 1), ("lineInterface", 2), ("radio", 3), ("local", 4), ("remote", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wtnLedStatus.setStatus('current')
wtnAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 9, 1, 2), Bits().clone(namedValues=NamedValues(("minorAlarm", 0), ("criticalAlarm", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wtnAlarmStatus.setStatus('current')
radioLinkConfiguration = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 3, 9, 2))
if mibBuilder.loadTexts: radioLinkConfiguration.setStatus('current')
wtnLinkName = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 9, 2, 1), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wtnLinkName.setStatus('current')
mibBuilder.exportSymbols("ZHONE-GEN-WTN-MONITOR-MIB", PYSNMP_MODULE_ID=zhoneGenWtnMonitorModule, wtnMonitor=wtnMonitor, wtnAlarmStatus=wtnAlarmStatus, radioLinkConfiguration=radioLinkConfiguration, zhoneGenWtnMonitorModule=zhoneGenWtnMonitorModule, wtnLinkName=wtnLinkName, wtnLedStatus=wtnLedStatus)
