#
# PySNMP MIB module ZYXEL-SERVER-GUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-SERVER-GUARD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:37:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelDhcpServerGuard = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 122))
if mibBuilder.loadTexts: zyxelDhcpServerGuard.setLastUpdated('201911180000Z')
if mibBuilder.loadTexts: zyxelDhcpServerGuard.setOrganization('Enterprise Solution ZyXEL')
zyxelDhcpServerGuardSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 122, 1))
zyDhcpServerGuardState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 122, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpServerGuardState.setStatus('current')
zyxelDhcpServerGuardPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 122, 1, 2), )
if mibBuilder.loadTexts: zyxelDhcpServerGuardPortTable.setStatus('current')
zyxelDhcpServerGuardPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 122, 1, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelDhcpServerGuardPortEntry.setStatus('current')
zyDhcpServerGuardPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 122, 1, 2, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpServerGuardPortState.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-SERVER-GUARD-MIB", zyxelDhcpServerGuardPortEntry=zyxelDhcpServerGuardPortEntry, zyxelDhcpServerGuardSetup=zyxelDhcpServerGuardSetup, PYSNMP_MODULE_ID=zyxelDhcpServerGuard, zyxelDhcpServerGuard=zyxelDhcpServerGuard, zyxelDhcpServerGuardPortTable=zyxelDhcpServerGuardPortTable, zyDhcpServerGuardPortState=zyDhcpServerGuardPortState, zyDhcpServerGuardState=zyDhcpServerGuardState)
