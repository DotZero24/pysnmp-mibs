#
# PySNMP MIB module TRIP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/TRIP-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:26:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
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

mibBuilder.exportSymbols("TRIP-TC-MIB", TripAppProtocol=TripAppProtocol, PYSNMP_MODULE_ID=tripTC, TripCommunityId=TripCommunityId, tripTC=tripTC, TripAddressFamily=TripAddressFamily, TripItad=TripItad, TripProtocolVersion=TripProtocolVersion, TripSendReceiveMode=TripSendReceiveMode, TripId=TripId)
