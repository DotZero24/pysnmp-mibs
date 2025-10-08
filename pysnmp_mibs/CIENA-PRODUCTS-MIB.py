#
# PySNMP MIB module CIENA-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/CIENA-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cienaCommon, cienaProducts = mibBuilder.importSymbols("CIENA-SMI", "cienaCommon", "cienaProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CIENA-PRODUCTS-MIB", pn8700_2=pn8700_2, pn8500_30=pn8500_30, cn5410=cn5410, pn8500_10=pn8500_10, ome6500=ome6500, pn8700_10=pn8700_10, pn8700_20=pn8700_20, cienaProductsMIB=cienaProductsMIB, cn5430=cn5430, pn8700_4=pn8700_4, PYSNMP_MODULE_ID=cienaProductsMIB)
