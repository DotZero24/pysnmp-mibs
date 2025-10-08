#
# PySNMP MIB module CIENA-WS-PLATFORM-TYPEDEFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciena/CIENA-WS-PLATFORM-TYPEDEFS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cienaWsPlatformConfig, = mibBuilder.importSymbols("CIENA-WS-MIB", "cienaWsPlatformConfig")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cienaWsPlatformTypedefsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 5, 13))
cienaWsPlatformTypedefsMIB.setRevisions(('2018-08-01 00:00', '2018-04-27 00:00',))
if mibBuilder.loadTexts: cienaWsPlatformTypedefsMIB.setLastUpdated('201808010000Z')
if mibBuilder.loadTexts: cienaWsPlatformTypedefsMIB.setOrganization('Ciena Corporation')
class EnabledDisabledEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class StringMaxl16(TextualConvention, OctetString):
    status = 'current'
    displayHint = '16a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class StringMaxl32(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class StringMaxl44(TextualConvention, OctetString):
    status = 'current'
    displayHint = '44a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 44)

mibBuilder.exportSymbols("CIENA-WS-PLATFORM-TYPEDEFS-MIB", StringMaxl32=StringMaxl32, StringMaxl16=StringMaxl16, EnabledDisabledEnum=EnabledDisabledEnum, StringMaxl44=StringMaxl44, PYSNMP_MODULE_ID=cienaWsPlatformTypedefsMIB, cienaWsPlatformTypedefsMIB=cienaWsPlatformTypedefsMIB)
