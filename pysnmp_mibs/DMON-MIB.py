#
# PySNMP MIB module DMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/electroline/DMON-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:43:08 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
electrolineCoRoot, = mibBuilder.importSymbols("ELECTROLINE-GLOBAL-REG", "electrolineCoRoot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class ModulationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", -1), ("qam16", 0), ("qam64", 1), ("qam256", 2), ("qam1024", 3), ("qam32", 4), ("qam128", 5), ("qpsk", 6))

dmonMib = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 999999))
dmonPhyGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 999999, 1))
dmonCommonGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 999999, 2))
dmonDsgMcastRedirectGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 999999, 3))
mibBuilder.exportSymbols("DMON-MIB", dmonMib=dmonMib, dmonCommonGroup=dmonCommonGroup, dmonDsgMcastRedirectGroup=dmonDsgMcastRedirectGroup, ModulationType=ModulationType, dmonPhyGroup=dmonPhyGroup)
