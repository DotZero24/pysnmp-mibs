#
# PySNMP MIB module BROCADE-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/BROCADE-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
bcsiReg, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiReg")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
brocadeProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 3))
brocadeProductsMIB.setRevisions(('2018-05-29 12:00', '2017-12-07 00:00', '2017-01-05 00:00', '2016-12-26 00:00', '2016-06-28 00:00', '2014-10-07 14:05', '2013-11-21 00:00', '2013-09-25 13:00', '2012-02-03 00:00',))
if mibBuilder.loadTexts: brocadeProductsMIB.setLastUpdated('201805291200Z')
if mibBuilder.loadTexts: brocadeProductsMIB.setOrganization('Extreme Networks, Inc.')
brocadeProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1))
vdx6740 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 131))
vdx6740T = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 137))
vdx2740 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 138))
vdx6740T1G = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 151))
vdx6940Q36 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 153))
vdx6940S144 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 164))
vdx8770S4 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 1000))
vdx8770S8 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 1001))
vdx8770S16 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 1002))
slx9850S4 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 2000))
slx9850S8 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 2001))
slx9240 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 3000))
slx9140 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 3001))
slx9540 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 4000))
mibBuilder.exportSymbols("BROCADE-PRODUCTS-MIB", slx9850S4=slx9850S4, vdx6740T1G=vdx6740T1G, vdx6740T=vdx6740T, brocadeProducts=brocadeProducts, vdx6940Q36=vdx6940Q36, vdx8770S16=vdx8770S16, brocadeProductsMIB=brocadeProductsMIB, PYSNMP_MODULE_ID=brocadeProductsMIB, vdx6740=vdx6740, vdx8770S4=vdx8770S4, slx9240=slx9240, vdx8770S8=vdx8770S8, slx9540=slx9540, vdx6940S144=vdx6940S144, slx9140=slx9140, vdx2740=vdx2740, slx9850S8=slx9850S8)
