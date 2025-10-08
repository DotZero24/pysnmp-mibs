#
# PySNMP MIB module CISCO-SUBSCRIBER-SESSION-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-SUBSCRIBER-SESSION-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:29:04 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSubscriberSessionTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 785))
ciscoSubscriberSessionTcMIB.setRevisions(('2007-09-26 00:00',))
if mibBuilder.loadTexts: ciscoSubscriberSessionTcMIB.setLastUpdated('201201270000Z')
if mibBuilder.loadTexts: ciscoSubscriberSessionTcMIB.setOrganization('Cisco Systems, Inc.')
class SubSessionType(TextualConvention, Integer32):
    reference = "W. Simpson, 'The Point-to-Point Protocol (PPP)', RFC-1661, July 1994. R. Droms, 'Dynamic Host Configuration Protocol', RFC-2131, March 1997. A. Valencia, M. Littlewood, T. Kolar, 'Cisco Layer Two Forwarding Protocol (L2F)', RFC-2341, May 1998. L. Mamakos, K. Lidl, J. Evarts, D. Carrel, D. Simone, and R. Wheeler, 'A Method for Transmitting PPP Over Ethernet (PPPoE)', RFC-2516, February 1999. W. Townsley, A. Valencia, A. Rubens, G. Pall, G. Zorn, and B. Palter, 'Layer Two Tunneling Protocol (L2TP)', RFC-2661, August 1999. C. Rigney, S. Willens, A. Rubens, and W. Simpson, 'Remote Authentication Dial-In User Service (RADIUS)', RFC-2865, June 2000."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("all", 1), ("other", 2), ("pppSubscriber", 3), ("pppoeSubscriber", 4), ("l2tpSubscriber", 5), ("l2fSubscriber", 6), ("ipInterfaceSubscriber", 7), ("ipPktSubscriber", 8), ("ipDhcpv4Subscriber", 9), ("ipRadiusSubscriber", 10), ("l2MacSubscriber", 11), ("l2Dhcpv4Subscriber", 12), ("l2RadiusSubscriber", 13))

class SubSessionTypes(TextualConvention, Bits):
    reference = "W. Simpson, 'The Point-to-Point Protocol (PPP)', RFC-1661, July 1994. R. Droms, 'Dynamic Host Configuration Protocol', RFC-2131, March 1997. A. Valencia, M. Littlewood, T. Kolar, 'Cisco Layer Two Forwarding Protocol (L2F)', RFC-2341, May 1998. L. Mamakos, K. Lidl, J. Evarts, D. Carrel, D. Simone, and R. Wheeler, 'A Method for Transmitting PPP Over Ethernet (PPPoE)', RFC-2516, February 1999. W. Townsley, A. Valencia, A. Rubens, G. Pall, G. Zorn, and B. Palter, 'Layer Two Tunneling Protocol (L2TP)', RFC-2661, August 1999. C. Rigney, S. Willens, A. Rubens, and W. Simpson, 'Remote Authentication Dial-In User Service (RADIUS)', RFC-2865, June 2000."
    status = 'current'
    namedValues = NamedValues(("pppSubscriber", 0), ("pppoeSubscriber", 1), ("l2tpSubscriber", 2), ("l2fSubscriber", 3), ("ipInterfaceSubscriber", 4), ("ipPktSubscriber", 5), ("ipDhcpv4Subscriber", 6), ("ipRadiusSubscriber", 7), ("l2MacSubscriber", 8), ("l2Dhcpv4Subscriber", 9), ("l2RadiusSubscriber", 10))

class SubSessionState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("pending", 2), ("up", 3))

class SubSessionRedundancyMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("other", 2), ("active", 3), ("standby", 4))

mibBuilder.exportSymbols("CISCO-SUBSCRIBER-SESSION-TC-MIB", SubSessionRedundancyMode=SubSessionRedundancyMode, SubSessionType=SubSessionType, SubSessionState=SubSessionState, SubSessionTypes=SubSessionTypes, PYSNMP_MODULE_ID=ciscoSubscriberSessionTcMIB, ciscoSubscriberSessionTcMIB=ciscoSubscriberSessionTcMIB)
