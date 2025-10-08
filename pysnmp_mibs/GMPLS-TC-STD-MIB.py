#
# PySNMP MIB module GMPLS-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/GMPLS-TC-STD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:38 2025
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
gmplsTCStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 12))
gmplsTCStdMIB.setRevisions(('2007-02-28 00:00',))
if mibBuilder.loadTexts: gmplsTCStdMIB.setLastUpdated('200702280000Z')
if mibBuilder.loadTexts: gmplsTCStdMIB.setOrganization('IETF Common Control and Measurement Plane (CCAMP) Working Group')
class GmplsFreeformLabelTC(TextualConvention, OctetString):
    reference = '1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3.2.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class GmplsLabelTypeTC(TextualConvention, Integer32):
    reference = '1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3. 2. Definition of Textual Conventions and for Multiprotocol Label Switching (MPLS) Management, RFC 3811, section 3. 3. Generalized Multi-Protocol Label Switching (GMPLS) Extensions for Synchronous Optical Network (SONET) and Synchronous Digital Hierarchy (SDH) Control, RFC 4606.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("gmplsMplsLabel", 1), ("gmplsPortWavelengthLabel", 2), ("gmplsFreeformGeneralizedLabel", 3), ("gmplsSonetLabel", 4), ("gmplsSdhLabel", 5), ("gmplsWavebandLabel", 6))

class GmplsSegmentDirectionTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("forward", 1), ("reverse", 2))

mibBuilder.exportSymbols("GMPLS-TC-STD-MIB", gmplsTCStdMIB=gmplsTCStdMIB, PYSNMP_MODULE_ID=gmplsTCStdMIB, GmplsSegmentDirectionTC=GmplsSegmentDirectionTC, GmplsFreeformLabelTC=GmplsFreeformLabelTC, GmplsLabelTypeTC=GmplsLabelTypeTC)
