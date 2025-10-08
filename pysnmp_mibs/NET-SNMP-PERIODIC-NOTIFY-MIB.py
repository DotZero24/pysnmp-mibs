#
# PySNMP MIB module NET-SNMP-PERIODIC-NOTIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/net-snmp/NET-SNMP-PERIODIC-NOTIFY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
netSnmpNotifications, netSnmpObjects, netSnmpModuleIDs = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpNotifications", "netSnmpObjects", "netSnmpModuleIDs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NET-SNMP-PERIODIC-NOTIFY-MIB", nsPNotifications=nsPNotifications, nsPNotifyMaxMessageNumber=nsPNotifyMaxMessageNumber, nsPNotificationPrefix=nsPNotificationPrefix, PYSNMP_MODULE_ID=netSnmpPeriodicNotifyMib, nsPNotificationObjects=nsPNotificationObjects, nsPNotifyMessageNumber=nsPNotifyMessageNumber, nsPNPeriodicTime=nsPNPeriodicTime, nsPNTables=nsPNTables, nsPNScalars=nsPNScalars, nsPNotifyObjects=nsPNotifyObjects, nsNotifyPeriodicNotification=nsNotifyPeriodicNotification, netSnmpPeriodicNotifyMib=netSnmpPeriodicNotifyMib)
