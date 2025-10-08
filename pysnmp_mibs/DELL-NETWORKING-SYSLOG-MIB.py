#
# PySNMP MIB module DELL-NETWORKING-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/dell/DELL-NETWORKING-SYSLOG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:44:22 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dellNetMgmt, = mibBuilder.importSymbols("DELL-NETWORKING-SMI", "dellNetMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dellNetSyslogMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027, 3, 30))
dellNetSyslogMib.setRevisions(('2014-10-23 00:00',))
if mibBuilder.loadTexts: dellNetSyslogMib.setLastUpdated('201410230000Z')
if mibBuilder.loadTexts: dellNetSyslogMib.setOrganization('Dell Inc.')
dellNetSyslogNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 30, 1))
dellNetSyslogTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 30, 1, 1))
dellNetSyslogServerNotReachableTrap = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 30, 1, 1, 1))
if mibBuilder.loadTexts: dellNetSyslogServerNotReachableTrap.setStatus('current')
dellNetSyslogServerReachableTrap = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 30, 1, 1, 2))
if mibBuilder.loadTexts: dellNetSyslogServerReachableTrap.setStatus('current')
mibBuilder.exportSymbols("DELL-NETWORKING-SYSLOG-MIB", dellNetSyslogServerReachableTrap=dellNetSyslogServerReachableTrap, dellNetSyslogServerNotReachableTrap=dellNetSyslogServerNotReachableTrap, dellNetSyslogNotifications=dellNetSyslogNotifications, PYSNMP_MODULE_ID=dellNetSyslogMib, dellNetSyslogTraps=dellNetSyslogTraps, dellNetSyslogMib=dellNetSyslogMib)
