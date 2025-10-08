#
# PySNMP MIB module ELTEX-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-TC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltexLtd, = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltexTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 8))
eltexTC.setRevisions(('2017-04-19 00:00',))
if mibBuilder.loadTexts: eltexTC.setLastUpdated('201704190000Z')
if mibBuilder.loadTexts: eltexTC.setOrganization('Eltex Enterprise, Ltd.')
class EltexPercent(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class EltexThresholdRelation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("lessThan", 1), ("lessOrEqual", 2), ("greaterThan", 3), ("greaterOrEqual", 4), ("equalTo", 5), ("notEqualTo", 6))

mibBuilder.exportSymbols("ELTEX-TC", eltexTC=eltexTC, EltexThresholdRelation=EltexThresholdRelation, EltexPercent=EltexPercent, PYSNMP_MODULE_ID=eltexTC)
