#
# PySNMP MIB module DMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/electroline/DMON-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
electrolineCoRoot, = mibBuilder.importSymbols("ELECTROLINE-GLOBAL-REG", "electrolineCoRoot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class ModulationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", -1), ("qam16", 0), ("qam64", 1), ("qam256", 2), ("qam1024", 3), ("qam32", 4), ("qam128", 5), ("qpsk", 6))

dmonMib = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 999999))
dmonPhyGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 999999, 1))
dmonCommonGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 999999, 2))
dmonDsgMcastRedirectGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 999999, 3))
mibBuilder.exportSymbols("DMON-MIB", dmonMib=dmonMib, ModulationType=ModulationType, dmonCommonGroup=dmonCommonGroup, dmonPhyGroup=dmonPhyGroup, dmonDsgMcastRedirectGroup=dmonDsgMcastRedirectGroup)
