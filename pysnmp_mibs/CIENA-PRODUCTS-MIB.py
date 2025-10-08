#
# PySNMP MIB module CIENA-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciena/CIENA-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:04 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cienaCommon, cienaProducts = mibBuilder.importSymbols("CIENA-SMI", "cienaCommon", "cienaProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cienaProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 1, 1))
cienaProductsMIB.setRevisions(('2017-06-07 00:00', '2014-01-21 00:00', '2013-03-05 00:00', '2010-03-28 00:00',))
if mibBuilder.loadTexts: cienaProductsMIB.setLastUpdated('201706070000Z')
if mibBuilder.loadTexts: cienaProductsMIB.setOrganization('Ciena Corp.')
cn5410 = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 1, 2, 1))
cn5430 = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 1, 2, 2))
ome6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 1, 2, 3))
pn8500_10 = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 1, 2, 4)).setLabel("pn8500-10")
pn8500_30 = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 1, 2, 5)).setLabel("pn8500-30")
pn8700_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 1, 2, 6)).setLabel("pn8700-2")
pn8700_4 = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 1, 2, 7)).setLabel("pn8700-4")
pn8700_10 = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 1, 2, 8)).setLabel("pn8700-10")
pn8700_20 = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 1, 2, 9)).setLabel("pn8700-20")
mibBuilder.exportSymbols("CIENA-PRODUCTS-MIB", pn8500_30=pn8500_30, cn5410=cn5410, pn8700_4=pn8700_4, cienaProductsMIB=cienaProductsMIB, ome6500=ome6500, pn8500_10=pn8500_10, pn8700_10=pn8700_10, PYSNMP_MODULE_ID=cienaProductsMIB, pn8700_2=pn8700_2, pn8700_20=pn8700_20, cn5430=cn5430)
