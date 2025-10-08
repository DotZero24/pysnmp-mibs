#
# PySNMP MIB module DELL-NETWORKING-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dell/DELL-NETWORKING-SYSLOG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dellNetMgmt, = mibBuilder.importSymbols("DELL-NETWORKING-SMI", "dellNetMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("DELL-NETWORKING-SYSLOG-MIB", dellNetSyslogNotifications=dellNetSyslogNotifications, PYSNMP_MODULE_ID=dellNetSyslogMib, dellNetSyslogServerReachableTrap=dellNetSyslogServerReachableTrap, dellNetSyslogServerNotReachableTrap=dellNetSyslogServerNotReachableTrap, dellNetSyslogTraps=dellNetSyslogTraps, dellNetSyslogMib=dellNetSyslogMib)
