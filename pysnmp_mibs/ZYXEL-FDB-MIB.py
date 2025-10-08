#
# PySNMP MIB module ZYXEL-FDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-FDB-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelFdb = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48))
if mibBuilder.loadTexts: zyxelFdb.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelFdb.setOrganization('Enterprise Solution ZyXEL')
zyxelMacStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 1))
zyxelMacStatusNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 2))
zyMacFlush = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacFlush.setStatus('current')
zyMacFlushPort = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacFlushPort.setStatus('current')
zyMacFlushVlan = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacFlushVlan.setStatus('current')
zyMacForwardingTableFull = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 2, 1))
if mibBuilder.loadTexts: zyMacForwardingTableFull.setStatus('current')
zyMacForwardingTableFullRecovered = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 2, 2))
if mibBuilder.loadTexts: zyMacForwardingTableFullRecovered.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-FDB-MIB", zyMacFlushVlan=zyMacFlushVlan, zyxelFdb=zyxelFdb, zyMacForwardingTableFull=zyMacForwardingTableFull, zyMacFlush=zyMacFlush, zyxelMacStatus=zyxelMacStatus, zyxelMacStatusNotifications=zyxelMacStatusNotifications, zyMacForwardingTableFullRecovered=zyMacForwardingTableFullRecovered, zyMacFlushPort=zyMacFlushPort, PYSNMP_MODULE_ID=zyxelFdb)
