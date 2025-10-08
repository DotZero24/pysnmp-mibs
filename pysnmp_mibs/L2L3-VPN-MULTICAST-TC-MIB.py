#
# PySNMP MIB module L2L3-VPN-MULTICAST-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/L2L3-VPN-MULTICAST-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:53 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
l2L3VpnMcastTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 244))
l2L3VpnMcastTCMIB.setRevisions(('2018-12-14 00:00',))
if mibBuilder.loadTexts: l2L3VpnMcastTCMIB.setLastUpdated('201812140000Z')
if mibBuilder.loadTexts: l2L3VpnMcastTCMIB.setOrganization('IETF BESS Working Group')
class L2L3VpnMcastProviderTunnelType(TextualConvention, Integer32):
    reference = 'RFC 4875 RFC 5015 RFC 6388 RFC 6513 RFC 6514, Section 5 RFC 7524, Section 14.1 RFC 7761 '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("noTunnelInfo", 0), ("rsvpP2mp", 1), ("ldpP2mp", 2), ("pimSsm", 3), ("pimAsm", 4), ("pimBidir", 5), ("ingressReplication", 6), ("ldpMp2mp", 7), ("transportTunnel", 8))

class L2L3VpnMcastProviderTunnelId(TextualConvention, OctetString):
    reference = 'RFC 6514, Section 5 RFC 4875, Section 19.1 RFC 6388, Sections 2.2 and 3.2 RFC 7524, Section 14.1 '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(12, 12), ValueSizeConstraint(16, 16), ValueSizeConstraint(17, 17), ValueSizeConstraint(24, 24), ValueSizeConstraint(29, 29), ValueSizeConstraint(32, 32), )
mibBuilder.exportSymbols("L2L3-VPN-MULTICAST-TC-MIB", l2L3VpnMcastTCMIB=l2L3VpnMcastTCMIB, PYSNMP_MODULE_ID=l2L3VpnMcastTCMIB, L2L3VpnMcastProviderTunnelId=L2L3VpnMcastProviderTunnelId, L2L3VpnMcastProviderTunnelType=L2L3VpnMcastProviderTunnelType)
