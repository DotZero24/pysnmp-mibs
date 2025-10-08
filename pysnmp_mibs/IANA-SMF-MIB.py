#
# PySNMP MIB module IANA-SMF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/IANA-SMF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaSmfMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 225))
ianaSmfMIB.setRevisions(('2014-10-10 00:00',))
if mibBuilder.loadTexts: ianaSmfMIB.setLastUpdated('201410100000Z')
if mibBuilder.loadTexts: ianaSmfMIB.setOrganization('IANA')
class IANAsmfOpModeIdTC(TextualConvention, Integer32):
    reference = "See Section 7.2 'Reduced Relay Set Forwarding', and the Appendices A, B, and C in RFC 6621 - 'Simplified Multicast Forwarding', Macker, J., Ed., May 2012."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("independent", 1), ("routing", 2), ("crossLayer", 3))

class IANAsmfRssaIdTC(TextualConvention, Integer32):
    reference = "For example, see: Section 8.1.1. 'SMF Message TLV Type' and the Appendices A, B, and C in RFC 6621 - 'Simplified Multicast Forwarding', Macker, J., Ed., May 2012. RFC 3626 - Clausen, T., Ed., and P. Jacquet, Ed., 'Optimized Link State Routing Protocol (OLSR)', October 2003. RFC 5614 - Ogier, R. and P. Spagnolo, 'Mobile Ad Hoc Network (MANET) Extension of OSPF Using Connected Dominating Set (CDS) Flooding', August 2009. RFC 7181 - Clausen, T., Dearlove, C., Jacquet, P., and U. Herberg, 'The Optimized Link State Routing Protocol Version 2', April 2014."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("cF", 1), ("sMPR", 2), ("eCDS", 3), ("mprCDS", 4))

mibBuilder.exportSymbols("IANA-SMF-MIB", PYSNMP_MODULE_ID=ianaSmfMIB, IANAsmfRssaIdTC=IANAsmfRssaIdTC, IANAsmfOpModeIdTC=IANAsmfOpModeIdTC, ianaSmfMIB=ianaSmfMIB)
