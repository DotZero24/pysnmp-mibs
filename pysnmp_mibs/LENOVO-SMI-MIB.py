#
# PySNMP MIB module LENOVO-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ibm/LENOVO-SMI-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:45:35 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lenovo = ModuleIdentity((1, 3, 6, 1, 4, 1, 19046))
lenovo.setRevisions(('2016-10-27 18:30',))
if mibBuilder.loadTexts: lenovo.setLastUpdated('201608150000Z')
if mibBuilder.loadTexts: lenovo.setOrganization('Lenovo Group Ltd.')
lenovoProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 1))
if mibBuilder.loadTexts: lenovoProducts.setStatus('current')
lenovoNetworkMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 2))
if mibBuilder.loadTexts: lenovoNetworkMibs.setStatus('current')
tor_mibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 2, 7)).setLabel("tor-mibs")
if mibBuilder.loadTexts: tor_mibs.setStatus('current')
flex_mibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 2, 18)).setLabel("flex-mibs")
if mibBuilder.loadTexts: flex_mibs.setStatus('current')
network_mibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 2, 3)).setLabel("network-mibs")
if mibBuilder.loadTexts: network_mibs.setStatus('current')
lenovoServerMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 11))
if mibBuilder.loadTexts: lenovoServerMibs.setStatus('current')
lenovoModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 4))
if mibBuilder.loadTexts: lenovoModules.setStatus('current')
mibBuilder.exportSymbols("LENOVO-SMI-MIB", lenovoModules=lenovoModules, lenovo=lenovo, lenovoProducts=lenovoProducts, flex_mibs=flex_mibs, lenovoNetworkMibs=lenovoNetworkMibs, network_mibs=network_mibs, lenovoServerMibs=lenovoServerMibs, PYSNMP_MODULE_ID=lenovo, tor_mibs=tor_mibs)
