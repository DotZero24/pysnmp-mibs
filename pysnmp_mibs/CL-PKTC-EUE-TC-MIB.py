#
# PySNMP MIB module CL-PKTC-EUE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/CL-PKTC-EUE-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:52 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pktcEUEMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "pktcEUEMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pktcEUETCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2))
pktcEUETCMIB.setRevisions(('2008-07-10 00:00', '2007-11-06 00:00',))
if mibBuilder.loadTexts: pktcEUETCMIB.setLastUpdated('200807100000Z')
if mibBuilder.loadTexts: pktcEUETCMIB.setOrganization('Cable Television Laboratories, Inc.')
pktcEUETCNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 0))
pktcEUETCObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1))
pktcEUETCConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2))
pktcEUETCCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 1))
pktcEUETCGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2))
pktcEUETCUsageObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1))
class PktcEUETCID(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1023)

class PktcEUETCIDType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("other", 1), ("gruu", 2), ("publicIdentity", 3), ("privateIdentity", 4), ("publicPrivatePair", 5), ("username", 6), ("macaddress", 7), ("packetcableIdentity", 8))

class PktcEUETCAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("inactive", 2))

class PktcEUETCOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("inactive", 2), ("notPresent", 3), ("unknown", 4))

class PktcEUETCStatusInfo(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 31)

class PktcEUETCUsrElementIndexType(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 63)

class PktcEUETCAppOrgIdentifier(TextualConvention, Unsigned32):
    reference = 'http://www.iana.org/assignments/enterprise-numbers'
    status = 'current'

class PktcEUETCAppIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 127)

class PktcEUETCUsrAppIndexType(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 31)

class PktcEUETCCredsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("none", 2), ("password", 3), ("preSharedKey", 4), ("certificate", 5))

class PktcEUETCCreds(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8192)

mibBuilder.exportSymbols("CL-PKTC-EUE-TC-MIB", pktcEUETCConformance=pktcEUETCConformance, PktcEUETCIDType=PktcEUETCIDType, pktcEUETCObjects=pktcEUETCObjects, pktcEUETCGroups=pktcEUETCGroups, PYSNMP_MODULE_ID=pktcEUETCMIB, pktcEUETCCompliances=pktcEUETCCompliances, PktcEUETCCreds=PktcEUETCCreds, pktcEUETCNotifications=pktcEUETCNotifications, PktcEUETCAdminStatus=PktcEUETCAdminStatus, PktcEUETCUsrAppIndexType=PktcEUETCUsrAppIndexType, PktcEUETCCredsType=PktcEUETCCredsType, PktcEUETCAppOrgIdentifier=PktcEUETCAppOrgIdentifier, PktcEUETCAppIdentifier=PktcEUETCAppIdentifier, pktcEUETCMIB=pktcEUETCMIB, PktcEUETCUsrElementIndexType=PktcEUETCUsrElementIndexType, PktcEUETCID=PktcEUETCID, PktcEUETCOperStatus=PktcEUETCOperStatus, PktcEUETCStatusInfo=PktcEUETCStatusInfo, pktcEUETCUsageObjs=pktcEUETCUsageObjs)
