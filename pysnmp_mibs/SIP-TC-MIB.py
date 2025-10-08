#
# PySNMP MIB module SIP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/SIP-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:34 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sipTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 148))
sipTC.setRevisions(('2007-04-20 00:00',))
if mibBuilder.loadTexts: sipTC.setLastUpdated('200704200000Z')
if mibBuilder.loadTexts: sipTC.setOrganization('IETF Session Initiation Protocol Working Group')
class SipTCTransportProtocol(TextualConvention, Bits):
    reference = 'RFC 3261, Section 18 and RFC 4168'
    status = 'current'
    namedValues = NamedValues(("other", 0), ("udp", 1), ("tcp", 2), ("sctp", 3), ("tlsTcp", 4), ("tlsSctp", 5))

class SipTCEntityRole(TextualConvention, Bits):
    reference = 'RFC 3261, Section 6'
    status = 'current'
    namedValues = NamedValues(("other", 0), ("userAgent", 1), ("proxyServer", 2), ("redirectServer", 3), ("registrarServer", 4))

class SipTCOptionTagHeaders(TextualConvention, Bits):
    reference = 'RFC 3261, Sections 19.2, 20.32, 20.29, 20.37, and 20.40'
    status = 'current'
    namedValues = NamedValues(("require", 0), ("proxyRequire", 1), ("supported", 2), ("unsupported", 3))

class SipTCMethodName(TextualConvention, OctetString):
    reference = 'RFC 3261, Section 27.4'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 100)

mibBuilder.exportSymbols("SIP-TC-MIB", sipTC=sipTC, SipTCMethodName=SipTCMethodName, SipTCTransportProtocol=SipTCTransportProtocol, SipTCEntityRole=SipTCEntityRole, SipTCOptionTagHeaders=SipTCOptionTagHeaders, PYSNMP_MODULE_ID=sipTC)
