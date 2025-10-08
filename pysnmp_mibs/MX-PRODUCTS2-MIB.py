#
# PySNMP MIB module MX-PRODUCTS2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-PRODUCTS2-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mediatrixProducts, = mibBuilder.importSymbols("MX-SMI2", "mediatrixProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mediatrix3000Series = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 100))
mediatrix4400Series = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 200))
mediatrix4100Series = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 300))
mediatrixLPSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 400))
mediatrixiPBXSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 500))
mediatrixC7Series = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 600))
mediatrixSentinelSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 700))
mediatrixG7Series = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 800))
mediatrixS7Series = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 900))
mibBuilder.exportSymbols("MX-PRODUCTS2-MIB", mediatrix4400Series=mediatrix4400Series, mediatrixG7Series=mediatrixG7Series, mediatrix3000Series=mediatrix3000Series, mediatrixS7Series=mediatrixS7Series, mediatrixiPBXSeries=mediatrixiPBXSeries, mediatrixSentinelSeries=mediatrixSentinelSeries, mediatrix4100Series=mediatrix4100Series, mediatrixC7Series=mediatrixC7Series, mediatrixLPSeries=mediatrixLPSeries)
