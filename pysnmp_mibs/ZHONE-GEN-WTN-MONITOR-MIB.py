#
# PySNMP MIB module ZHONE-GEN-WTN-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zhone/ZHONE-GEN-WTN-MONITOR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:19:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
zhoneGenWtn, zhoneModules = mibBuilder.importSymbols("Zhone", "zhoneGenWtn", "zhoneModules")
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
mibBuilder.exportSymbols("ZHONE-GEN-WTN-MONITOR-MIB", zhoneGenWtnMonitorModule=zhoneGenWtnMonitorModule, wtnLedStatus=wtnLedStatus, wtnMonitor=wtnMonitor, wtnAlarmStatus=wtnAlarmStatus, radioLinkConfiguration=radioLinkConfiguration, wtnLinkName=wtnLinkName, PYSNMP_MODULE_ID=zhoneGenWtnMonitorModule)
