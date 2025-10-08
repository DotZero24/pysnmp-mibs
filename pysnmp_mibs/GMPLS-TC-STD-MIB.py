#
# PySNMP MIB module GMPLS-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/GMPLS-TC-STD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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

mibBuilder.exportSymbols("GMPLS-TC-STD-MIB", GmplsLabelTypeTC=GmplsLabelTypeTC, gmplsTCStdMIB=gmplsTCStdMIB, GmplsFreeformLabelTC=GmplsFreeformLabelTC, GmplsSegmentDirectionTC=GmplsSegmentDirectionTC, PYSNMP_MODULE_ID=gmplsTCStdMIB)
