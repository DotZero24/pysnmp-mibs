#
# PySNMP MIB module CISCO-SUBSCRIBER-IDENTITY-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-SUBSCRIBER-IDENTITY-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSubscriberIdentityTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 782))
ciscoSubscriberIdentityTcMIB.setRevisions(('2011-12-23 00:00',))
if mibBuilder.loadTexts: ciscoSubscriberIdentityTcMIB.setLastUpdated('201112230000Z')
if mibBuilder.loadTexts: ciscoSubscriberIdentityTcMIB.setOrganization('Cisco Systems, Inc.')
class SubSessionIdentity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))
    namedValues = NamedValues(("other", 1), ("ifIndex", 2), ("subscriberLabel", 3), ("macAddress", 4), ("nativeVrf", 5), ("nativeIpAddress", 6), ("domainVrf", 7), ("domainIpAddress", 8), ("pbhk", 9), ("remoteId", 10), ("circuitId", 11), ("nasPort", 12), ("domain", 13), ("username", 14), ("acctSessionId", 15), ("dnis", 16), ("media", 17), ("mlpNegotiated", 18), ("protocol", 19), ("serviceName", 20), ("dhcpClass", 21), ("tunnelName", 22))

class SubSessionIdentities(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ifIndex", 0), ("subscriberLabel", 1), ("macAddress", 2), ("nativeVrf", 3), ("nativeIpAddress", 4), ("domainVrf", 5), ("domainIpAddress", 6), ("pbhk", 7), ("remoteId", 8), ("circuitId", 9), ("nasPort", 10), ("domain", 11), ("username", 12), ("acctSessionId", 13), ("dnis", 14), ("media", 15), ("mlpNegotiated", 16), ("protocol", 17), ("serviceName", 18), ("dhcpClass", 19), ("tunnelName", 20))

class SubscriberLabel(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class SubscriberVRF(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberPbhk(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class SubscriberRemoteId(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberCircuitId(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberNasPort(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class SubscriberDomain(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberUsername(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberAcctSessionId(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class SubscriberDnis(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberMediaType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("other", 1), ("async", 2), ("atm", 3), ("ethernet", 4), ("ip", 5), ("isdn", 6), ("mpls", 7), ("sync", 8))

class SubscriberProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("atom", 2), ("ip", 3), ("psdn", 4), ("ppp", 5), ("vpdn", 6))

class SubscriberDhcpClass(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberTunnelName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberLocationName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberServiceName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

mibBuilder.exportSymbols("CISCO-SUBSCRIBER-IDENTITY-TC-MIB", SubscriberVRF=SubscriberVRF, ciscoSubscriberIdentityTcMIB=ciscoSubscriberIdentityTcMIB, SubscriberCircuitId=SubscriberCircuitId, SubscriberDomain=SubscriberDomain, SubscriberDnis=SubscriberDnis, SubscriberPbhk=SubscriberPbhk, SubscriberDhcpClass=SubscriberDhcpClass, SubscriberUsername=SubscriberUsername, SubscriberMediaType=SubscriberMediaType, SubscriberRemoteId=SubscriberRemoteId, SubscriberLocationName=SubscriberLocationName, SubSessionIdentity=SubSessionIdentity, SubscriberTunnelName=SubscriberTunnelName, PYSNMP_MODULE_ID=ciscoSubscriberIdentityTcMIB, SubSessionIdentities=SubSessionIdentities, SubscriberLabel=SubscriberLabel, SubscriberNasPort=SubscriberNasPort, SubscriberProtocolType=SubscriberProtocolType, SubscriberAcctSessionId=SubscriberAcctSessionId, SubscriberServiceName=SubscriberServiceName)
