#
# PySNMP MIB module ALVARION-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/alvarion/ALVARION-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
alvarionModules, alvarionProducts = mibBuilder.importSymbols("ALVARION-SMI", "alvarionModules", "alvarionProducts")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alvarionProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 4, 2))
if mibBuilder.loadTexts: alvarionProductsMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionProductsMIB.setOrganization('Alvarion Ltd.')
alvarionWI2CTRL40 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 25))
alvarionWI2CTRL200 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 27))
alvarionWI2CTRL10 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 35))
alvarionWI2SR1 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 36))
alvarionWI2DR1 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 37))
mibBuilder.exportSymbols("ALVARION-PRODUCTS-MIB", alvarionWI2CTRL200=alvarionWI2CTRL200, alvarionWI2CTRL40=alvarionWI2CTRL40, alvarionWI2SR1=alvarionWI2SR1, alvarionProductsMIB=alvarionProductsMIB, alvarionWI2DR1=alvarionWI2DR1, PYSNMP_MODULE_ID=alvarionProductsMIB, alvarionWI2CTRL10=alvarionWI2CTRL10)
