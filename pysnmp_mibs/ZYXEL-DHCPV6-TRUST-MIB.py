#
# PySNMP MIB module ZYXEL-DHCPV6-TRUST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-DHCPV6-TRUST-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:03:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ZYXEL-DHCPV6-TRUST-MIB", zyxelDhcpv6TrustPortEntry=zyxelDhcpv6TrustPortEntry, zyDhcpv6TrustPortState=zyDhcpv6TrustPortState, zyxelDhcpv6TrustPortTable=zyxelDhcpv6TrustPortTable, zyDhcpv6TrustState=zyDhcpv6TrustState, PYSNMP_MODULE_ID=zyxelDhcpv6Trust, zyxelDhcpv6Trust=zyxelDhcpv6Trust, zyxelDhcpv6TrustSetup=zyxelDhcpv6TrustSetup)
