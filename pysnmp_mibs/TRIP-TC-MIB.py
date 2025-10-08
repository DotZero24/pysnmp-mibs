#
# PySNMP MIB module TRIP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/TRIP-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:48:35 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tripTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 115))
tripTC.setRevisions(('2004-09-02 00:00',))
if mibBuilder.loadTexts: tripTC.setLastUpdated('200409020000Z')
if mibBuilder.loadTexts: tripTC.setOrganization('IETF IPTel Working Group. Mailing list: iptel@lists.bell-labs.com')
class TripItad(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class TripId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class TripAddressFamily(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 255))
    namedValues = NamedValues(("decimal", 1), ("pentadecimal", 2), ("e164", 3), ("other", 255))

class TripAppProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 255))
    namedValues = NamedValues(("sip", 1), ("q931", 2), ("ras", 3), ("annexG", 4), ("other", 255))

class TripCommunityId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class TripProtocolVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class TripSendReceiveMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("sendReceive", 1), ("sendOnly", 2), ("receiveOnly", 3))

mibBuilder.exportSymbols("TRIP-TC-MIB", TripProtocolVersion=TripProtocolVersion, TripItad=TripItad, TripAddressFamily=TripAddressFamily, TripAppProtocol=TripAppProtocol, tripTC=tripTC, TripCommunityId=TripCommunityId, PYSNMP_MODULE_ID=tripTC, TripId=TripId, TripSendReceiveMode=TripSendReceiveMode)
