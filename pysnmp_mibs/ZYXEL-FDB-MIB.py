#
# PySNMP MIB module ZYXEL-FDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-FDB-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:03:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ZYXEL-FDB-MIB", zyxelMacStatusNotifications=zyxelMacStatusNotifications, zyMacFlushVlan=zyMacFlushVlan, zyxelFdb=zyxelFdb, zyxelMacStatus=zyxelMacStatus, zyMacFlushPort=zyMacFlushPort, zyMacForwardingTableFullRecovered=zyMacForwardingTableFullRecovered, zyMacForwardingTableFull=zyMacForwardingTableFull, zyMacFlush=zyMacFlush, PYSNMP_MODULE_ID=zyxelFdb)
