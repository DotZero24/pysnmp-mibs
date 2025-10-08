#
# PySNMP MIB module ZYXEL-DHCPV6-TRUST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-DHCPV6-TRUST-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:01 2025
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
zyxelDhcpv6Trust = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 107))
if mibBuilder.loadTexts: zyxelDhcpv6Trust.setLastUpdated('201502160000Z')
if mibBuilder.loadTexts: zyxelDhcpv6Trust.setOrganization('Enterprise Solution ZyXEL')
zyxelDhcpv6TrustSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 107, 1))
zyDhcpv6TrustState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 107, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpv6TrustState.setStatus('current')
zyxelDhcpv6TrustPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 107, 1, 2), )
if mibBuilder.loadTexts: zyxelDhcpv6TrustPortTable.setStatus('current')
zyxelDhcpv6TrustPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 107, 1, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelDhcpv6TrustPortEntry.setStatus('current')
zyDhcpv6TrustPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 107, 1, 2, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpv6TrustPortState.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-DHCPV6-TRUST-MIB", zyxelDhcpv6TrustSetup=zyxelDhcpv6TrustSetup, PYSNMP_MODULE_ID=zyxelDhcpv6Trust, zyxelDhcpv6Trust=zyxelDhcpv6Trust, zyDhcpv6TrustState=zyDhcpv6TrustState, zyDhcpv6TrustPortState=zyDhcpv6TrustPortState, zyxelDhcpv6TrustPortTable=zyxelDhcpv6TrustPortTable, zyxelDhcpv6TrustPortEntry=zyxelDhcpv6TrustPortEntry)
