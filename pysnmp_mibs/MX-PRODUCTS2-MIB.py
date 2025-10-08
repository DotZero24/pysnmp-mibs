#
# PySNMP MIB module MX-PRODUCTS2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-PRODUCTS2-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:06:04 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mediatrixProducts, = mibBuilder.importSymbols("MX-SMI2", "mediatrixProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mediatrix3000Series = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 100))
mediatrix4400Series = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 200))
mediatrix4100Series = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 300))
mediatrixLPSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 400))
mediatrixiPBXSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 500))
mediatrixC7Series = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 600))
mediatrixSentinelSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 700))
mediatrixG7Series = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 800))
mediatrixS7Series = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100, 900))
mibBuilder.exportSymbols("MX-PRODUCTS2-MIB", mediatrix3000Series=mediatrix3000Series, mediatrixS7Series=mediatrixS7Series, mediatrix4100Series=mediatrix4100Series, mediatrix4400Series=mediatrix4400Series, mediatrixLPSeries=mediatrixLPSeries, mediatrixSentinelSeries=mediatrixSentinelSeries, mediatrixG7Series=mediatrixG7Series, mediatrixC7Series=mediatrixC7Series, mediatrixiPBXSeries=mediatrixiPBXSeries)
