#
# PySNMP MIB module GNOME-PRODUCT-ZEBRA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/gnome/GNOME-PRODUCT-ZEBRA-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:19:59 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
gnomeProducts, = mibBuilder.importSymbols("GNOME-SMI", "gnomeProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
zebra = ModuleIdentity((1, 3, 6, 1, 4, 1, 3319, 1, 2))
if mibBuilder.loadTexts: zebra.setLastUpdated('200004250000Z')
if mibBuilder.loadTexts: zebra.setOrganization('GNOME project')
zserv = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 1, 2, 1))
if mibBuilder.loadTexts: zserv.setStatus('current')
bgpd = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 1, 2, 2))
if mibBuilder.loadTexts: bgpd.setStatus('current')
ripd = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 1, 2, 3))
if mibBuilder.loadTexts: ripd.setStatus('current')
ripngd = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 1, 2, 4))
if mibBuilder.loadTexts: ripngd.setStatus('current')
ospfd = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 1, 2, 5))
if mibBuilder.loadTexts: ospfd.setStatus('current')
ospf6d = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 1, 2, 6))
if mibBuilder.loadTexts: ospf6d.setStatus('current')
mibBuilder.exportSymbols("GNOME-PRODUCT-ZEBRA-MIB", ospf6d=ospf6d, zebra=zebra, PYSNMP_MODULE_ID=zebra, zserv=zserv, ripd=ripd, ripngd=ripngd, bgpd=bgpd, ospfd=ospfd)
