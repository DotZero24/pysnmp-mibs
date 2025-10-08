#
# PySNMP MIB module ENTERASYS-UPN-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-UPN-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysUpnTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 44))
etsysUpnTcMIB.setRevisions(('2004-02-03 22:00', '2004-02-03 15:33',))
if mibBuilder.loadTexts: etsysUpnTcMIB.setLastUpdated('200402032200Z')
if mibBuilder.loadTexts: etsysUpnTcMIB.setOrganization('Enterasys Networks, Inc.')
class StationAddressType(TextualConvention, Integer32):
    reference = 'STD0058 (RFC2579), Textual Conventions for SMIv2. RFC3291, Textual Conventions for Internet Network Addresses.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 16))
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2), ("mac", 3), ("dns", 16))

class StationAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class StationAddressIPv6(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:2x:2x:2x:2x:2x:2x:2x%4d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )
mibBuilder.exportSymbols("ENTERASYS-UPN-TC-MIB", StationAddress=StationAddress, StationAddressType=StationAddressType, StationAddressIPv6=StationAddressIPv6, PYSNMP_MODULE_ID=etsysUpnTcMIB, etsysUpnTcMIB=etsysUpnTcMIB)
