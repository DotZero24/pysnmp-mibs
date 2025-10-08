#
# PySNMP MIB module NET-SNMP-PERIODIC-NOTIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/net-snmp/NET-SNMP-PERIODIC-NOTIFY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:44 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
netSnmpObjects, netSnmpNotifications, netSnmpModuleIDs = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpObjects", "netSnmpNotifications", "netSnmpModuleIDs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netSnmpPeriodicNotifyMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5))
netSnmpPeriodicNotifyMib.setRevisions(('2011-04-20 00:00',))
if mibBuilder.loadTexts: netSnmpPeriodicNotifyMib.setLastUpdated('201104200000Z')
if mibBuilder.loadTexts: netSnmpPeriodicNotifyMib.setOrganization('www.net-snmp.org')
nsPNScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 1))
nsPNTables = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 2))
nsPNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 3))
nsPNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 4))
nsPNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 4, 0))
nsPNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 4, 1))
nsNotifyPeriodicNotification = NotificationType((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 4, 0, 1))
if mibBuilder.loadTexts: nsNotifyPeriodicNotification.setStatus('current')
nsPNPeriodicTime = MibScalar((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 3, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nsPNPeriodicTime.setStatus('current')
nsPNotifyMessageNumber = MibScalar((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 3, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nsPNotifyMessageNumber.setStatus('current')
nsPNotifyMaxMessageNumber = MibScalar((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 3, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nsPNotifyMaxMessageNumber.setStatus('current')
mibBuilder.exportSymbols("NET-SNMP-PERIODIC-NOTIFY-MIB", nsPNScalars=nsPNScalars, netSnmpPeriodicNotifyMib=netSnmpPeriodicNotifyMib, nsPNotifyMessageNumber=nsPNotifyMessageNumber, PYSNMP_MODULE_ID=netSnmpPeriodicNotifyMib, nsPNotifications=nsPNotifications, nsNotifyPeriodicNotification=nsNotifyPeriodicNotification, nsPNTables=nsPNTables, nsPNotifyObjects=nsPNotifyObjects, nsPNotificationObjects=nsPNotificationObjects, nsPNotificationPrefix=nsPNotificationPrefix, nsPNPeriodicTime=nsPNPeriodicTime, nsPNotifyMaxMessageNumber=nsPNotifyMaxMessageNumber)
