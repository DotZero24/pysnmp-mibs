#
# PySNMP MIB module ALVARION-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/alvarion/ALVARION-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
alvarionModules, alvarionProducts = mibBuilder.importSymbols("ALVARION-SMI", "alvarionModules", "alvarionProducts")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alvarionProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 4, 2))
if mibBuilder.loadTexts: alvarionProductsMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionProductsMIB.setOrganization('Alvarion Ltd.')
alvarionWI2CTRL40 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 25))
alvarionWI2CTRL200 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 27))
alvarionWI2CTRL10 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 35))
alvarionWI2SR1 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 36))
alvarionWI2DR1 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 37))
mibBuilder.exportSymbols("ALVARION-PRODUCTS-MIB", alvarionWI2CTRL40=alvarionWI2CTRL40, alvarionWI2CTRL200=alvarionWI2CTRL200, alvarionWI2DR1=alvarionWI2DR1, PYSNMP_MODULE_ID=alvarionProductsMIB, alvarionProductsMIB=alvarionProductsMIB, alvarionWI2CTRL10=alvarionWI2CTRL10, alvarionWI2SR1=alvarionWI2SR1)
