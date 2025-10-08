#
# PySNMP MIB module ENTERASYS-UPN-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-UPN-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("ENTERASYS-UPN-TC-MIB", StationAddressIPv6=StationAddressIPv6, etsysUpnTcMIB=etsysUpnTcMIB, PYSNMP_MODULE_ID=etsysUpnTcMIB, StationAddress=StationAddress, StationAddressType=StationAddressType)
