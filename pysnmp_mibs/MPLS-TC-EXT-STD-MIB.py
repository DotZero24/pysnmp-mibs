#
# PySNMP MIB module MPLS-TC-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/MPLS-TC-EXT-STD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:50:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mplsTcExtStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 17))
mplsTcExtStdMIB.setRevisions(('2015-02-02 00:00',))
if mibBuilder.loadTexts: mplsTcExtStdMIB.setLastUpdated('201502020000Z')
if mibBuilder.loadTexts: mplsTcExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
class MplsGlobalId(TextualConvention, OctetString):
    reference = 'MPLS Transport Profile (MPLS-TP) Identifiers, RFC 6370, Section 3'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class MplsCcId(TextualConvention, OctetString):
    reference = 'MPLS-TP Identifiers Following ITU-T Conventions, RFC 6923, Section 3. International Reference Alphabet (IRA) (Formerly International Alphabet No. 5 or IA5) - Information technology - 7-bit coded character set for information exchange, ITU-T Recommendation T.50, September 1992.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), )
class MplsIccId(TextualConvention, OctetString):
    reference = 'MPLS-TP Identifiers Following ITU-T Conventions, RFC 6923, Section 3. International Reference Alphabet (IRA) (Formerly International Alphabet No. 5 or IA5) - Information technology - 7-bit coded character set for information exchange, ITU-T Recommendation T.50, September 1992.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 6), )
class MplsNodeId(TextualConvention, Unsigned32):
    reference = 'MPLS Transport Profile (MPLS-TP) Identifiers, RFC 6370, Section 4'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
mibBuilder.exportSymbols("MPLS-TC-EXT-STD-MIB", MplsCcId=MplsCcId, PYSNMP_MODULE_ID=mplsTcExtStdMIB, MplsIccId=MplsIccId, MplsGlobalId=MplsGlobalId, MplsNodeId=MplsNodeId, mplsTcExtStdMIB=mplsTcExtStdMIB)
