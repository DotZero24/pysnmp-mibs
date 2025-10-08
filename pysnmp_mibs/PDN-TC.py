#
# PySNMP MIB module PDN-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/paradyne/PDN-TC
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:29 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdyn = MibIdentifier((1, 3, 6, 1, 4, 1, 1795))
class VnidMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("implicit", 1), ("explicit", 2), ("notagging", 3))

class ClientState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

class VnidTaggingState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class VnidRange(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(2, 4000)

class SwitchState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class ResetStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noOp", 1), ("reset", 2), ("resetToFactoryDefaults", 3), ("resetToNewActiveConfig", 4))

class ResultTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("success", 2), ("failure", 3), ("inProgress", 4))

class InitiatorTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noop", 1), ("telnet", 2), ("console", 3), ("snmp", 4))

class NTPMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unicast", 1), ("broadcast", 2), ("multicast", 3))

class DNSServerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("primary", 1), ("secondary", 2))

class MibOidType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("scalar", 1), ("table", 2), ("mib", 3), ("section", 4))

class SocketType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("stream", 2), ("datagram", 3), ("rawProtocol", 4), ("reliableMessageDelivery", 5), ("sequencedPacket", 6))

class SocketFamily(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("unknown", 1), ("unix", 2), ("darpaInternet", 3), ("darpaIMP", 4), ("pUP", 5), ("cHAOSFamily", 6), ("xeroxNovell", 7), ("nBS", 8), ("eCMA", 9), ("dATAKIT", 10), ("cCITT", 11), ("sNA", 12), ("dECnet", 13), ("directDataLinkInterface", 14), ("dECLAT", 15), ("nSCHyperChannel", 16), ("appleTalk", 17), ("netqorkInterfaceTap", 18), ("iEEE8020ISO8802", 19), ("oSI", 20), ("x25", 21), ("oSIAFI47IDI4", 22), ("uSGovermentOSI", 23))

class SocketState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("closed", 1), ("listen", 2), ("sYNSent", 3), ("sYNRCVD", 4), ("established", 5), ("closeWait", 6), ("fINWait", 7), ("closing", 8), ("lastAck", 9), ("fINWait2", 10), ("timeWait", 11))

class DomainName(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class SnmpAdminString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class InetAddressType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("primary", 1), ("secondary", 2))

class ManagementType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inband", 1), ("outband", 2))

class ContactState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("open", 1), ("close", 2))

class IdslClockMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("triState", 1), ("portCardSinkClock", 2), ("portCardDriveClock", 3), ("portCardDriveClockOnboard", 4))

class TimeOfDay(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class DayOfWeek(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("sunday", 1), ("monday", 2), ("tuesday", 3), ("wednesday", 4), ("thursday", 5), ("friday", 6), ("saturday", 7), ("daily", 8))

mibBuilder.exportSymbols("PDN-TC", TimeOfDay=TimeOfDay, IdslClockMode=IdslClockMode, ClientState=ClientState, SocketState=SocketState, ResetStates=ResetStates, VnidMode=VnidMode, NTPMode=NTPMode, ResultTypes=ResultTypes, pdyn=pdyn, MibOidType=MibOidType, DayOfWeek=DayOfWeek, SocketFamily=SocketFamily, VnidRange=VnidRange, ManagementType=ManagementType, VnidTaggingState=VnidTaggingState, InitiatorTypes=InitiatorTypes, DNSServerType=DNSServerType, DomainName=DomainName, ContactState=ContactState, SocketType=SocketType, InetAddressType=InetAddressType, SnmpAdminString=SnmpAdminString, SwitchState=SwitchState)
