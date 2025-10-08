#
# PySNMP MIB module EXTREME-IETF-BFD-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/extreme/EXTREME-IETF-BFD-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:59 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
extremeBfd, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeBfd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
extremeIetfBfdTCMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 43, 1))
extremeIetfBfdTCMib.setRevisions(('2012-06-14 12:00',))
if mibBuilder.loadTexts: extremeIetfBfdTCMib.setLastUpdated('201206141200Z')
if mibBuilder.loadTexts: extremeIetfBfdTCMib.setOrganization('IETF Bidirectional Forwarding Detection Working Group')
class ExtremeBfdSessIndexTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class ExtremeBfdIntervalTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class ExtremeBfdMultiplierTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class ExtremeBfdDiagTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("noDiagnostic", 0), ("controlDetectionTimeExpired", 1), ("echoFunctionFailed", 2), ("neighborSignaledSessionDown", 3), ("forwardingPlaneReset", 4), ("pathDown", 5), ("concatenatedPathDown", 6), ("administrativelyDown", 7), ("reverseConcatenatedPathDown", 8))

class ExtremeBfdSessTypeTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010. Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for IPv4 and IPv6 (Single Hop), Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for Multihop Paths, RFC 5883, June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("singleHop", 1), ("multiHopTotallyArbitraryPaths", 2), ("multiHopOutOfBandSignaling", 3), ("multiHopUnidirectionalLinks", 4), ("multiPointHead", 5), ("multiPointTail", 6))

class ExtremeBfdSessOperModeTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("asyncModeWEchoFunction", 1), ("asynchModeWOEchoFunction", 2), ("demandModeWEchoFunction", 3), ("demandModeWOEchoFunction", 4))

class ExtremeBfdCtrlDestPortNumberTC(TextualConvention, Unsigned32):
    reference = 'Use of port 3784 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for IPv4 and IPv6 (Single Hop), Use of port 4784 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for IPv4 and IPv6 (Single Hop), RFC 5881, June 2010.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class ExtremeBfdCtrlSourcePortNumberTC(TextualConvention, Unsigned32):
    reference = 'Port 49152..65535 (RFC5881)'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class ExtremeBfdSessStateTC(TextualConvention, Integer32):
    reference = 'RFC 5880 - Bidirectional Forwarding Detection (BFD), Katz, D., Ward, D., June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("adminDown", 1), ("down", 2), ("init", 3), ("up", 4), ("failing", 5))

class ExtremeBfdSessAuthenticationTypeTC(TextualConvention, Integer32):
    reference = 'Sections 4.2 - 4.4 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD),'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("noAuthentication", -1), ("reserved", 0), ("simplePassword", 1), ("keyedMD5", 2), ("meticulousKeyedMD5", 3), ("keyedSHA1", 4), ("meticulousKeyedSHA1", 5))

class ExtremeBfdSessionAuthenticationKeyTC(TextualConvention, OctetString):
    reference = 'RFC5880, Sections 4.2 - 4.4'
    status = 'current'
    displayHint = '1x '
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 252)

mibBuilder.exportSymbols("EXTREME-IETF-BFD-TC-MIB", ExtremeBfdSessOperModeTC=ExtremeBfdSessOperModeTC, ExtremeBfdSessTypeTC=ExtremeBfdSessTypeTC, ExtremeBfdSessionAuthenticationKeyTC=ExtremeBfdSessionAuthenticationKeyTC, ExtremeBfdDiagTC=ExtremeBfdDiagTC, ExtremeBfdSessStateTC=ExtremeBfdSessStateTC, ExtremeBfdIntervalTC=ExtremeBfdIntervalTC, PYSNMP_MODULE_ID=extremeIetfBfdTCMib, ExtremeBfdMultiplierTC=ExtremeBfdMultiplierTC, ExtremeBfdCtrlDestPortNumberTC=ExtremeBfdCtrlDestPortNumberTC, ExtremeBfdSessAuthenticationTypeTC=ExtremeBfdSessAuthenticationTypeTC, ExtremeBfdCtrlSourcePortNumberTC=ExtremeBfdCtrlSourcePortNumberTC, ExtremeBfdSessIndexTC=ExtremeBfdSessIndexTC, extremeIetfBfdTCMib=extremeIetfBfdTCMib)
