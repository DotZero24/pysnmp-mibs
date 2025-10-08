#
# PySNMP MIB module MX-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-TC
# Produced by pysmi-1.1.12 at Wed Oct  8 11:06:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mediatrixModules, = mibBuilder.importSymbols("MX-SMI", "mediatrixModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mxTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 90, 1))
mxTextualConventions.setRevisions(('1903-03-11 00:00',))
if mibBuilder.loadTexts: mxTextualConventions.setLastUpdated('0303110000Z')
if mibBuilder.loadTexts: mxTextualConventions.setOrganization('Mediatrix Telecom, Inc.')
class MxIpHostName(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class MxIpAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class MxIpPort(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class MxAdvancedIpPort(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class MxIpSubnetMask(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class MxIpSelectConfigSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("static", 0), ("dhcp", 1))

class MxIpConfigSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 99))
    namedValues = NamedValues(("static", 0), ("dhcp", 1), ("default", 99))

class MxIpDhcpSiteSpecificCode(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(128, 254), )
class MxFloatingPoint(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class MxEnableState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

class MxActivationState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("inactive", 0), ("active", 1))

class MxSignalingAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class MxDigitMap(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

mibBuilder.exportSymbols("MX-TC", MxDigitMap=MxDigitMap, mxTextualConventions=mxTextualConventions, MxIpSelectConfigSource=MxIpSelectConfigSource, MxIpDhcpSiteSpecificCode=MxIpDhcpSiteSpecificCode, MxSignalingAddress=MxSignalingAddress, PYSNMP_MODULE_ID=mxTextualConventions, MxAdvancedIpPort=MxAdvancedIpPort, MxEnableState=MxEnableState, MxIpAddress=MxIpAddress, MxIpConfigSource=MxIpConfigSource, MxIpHostName=MxIpHostName, MxActivationState=MxActivationState, MxIpPort=MxIpPort, MxIpSubnetMask=MxIpSubnetMask, MxFloatingPoint=MxFloatingPoint)
