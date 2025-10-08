#
# PySNMP MIB module SIP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/SIP-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
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

mibBuilder.exportSymbols("SIP-TC-MIB", PYSNMP_MODULE_ID=sipTC, SipTCTransportProtocol=SipTCTransportProtocol, SipTCEntityRole=SipTCEntityRole, sipTC=sipTC, SipTCMethodName=SipTCMethodName, SipTCOptionTagHeaders=SipTCOptionTagHeaders)
