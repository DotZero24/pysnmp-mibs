#
# PySNMP MIB module GNOME-PRODUCT-ZEBRA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/gnome/GNOME-PRODUCT-ZEBRA-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
gnomeProducts, = mibBuilder.importSymbols("GNOME-SMI", "gnomeProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("GNOME-PRODUCT-ZEBRA-MIB", ripd=ripd, ospf6d=ospf6d, ripngd=ripngd, PYSNMP_MODULE_ID=zebra, bgpd=bgpd, zserv=zserv, zebra=zebra, ospfd=ospfd)
