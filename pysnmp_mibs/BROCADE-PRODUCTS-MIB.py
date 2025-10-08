#
# PySNMP MIB module BROCADE-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/BROCADE-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:08 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
bcsiReg, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiReg")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BROCADE-PRODUCTS-MIB", vdx6940Q36=vdx6940Q36, vdx8770S8=vdx8770S8, slx9850S4=slx9850S4, vdx6740=vdx6740, brocadeProducts=brocadeProducts, slx9540=slx9540, PYSNMP_MODULE_ID=brocadeProductsMIB, vdx2740=vdx2740, brocadeProductsMIB=brocadeProductsMIB, vdx8770S16=vdx8770S16, slx9240=slx9240, slx9140=slx9140, vdx6740T1G=vdx6740T1G, vdx6740T=vdx6740T, vdx6940S144=vdx6940S144, slx9850S8=slx9850S8, vdx8770S4=vdx8770S4)
