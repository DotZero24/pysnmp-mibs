#
# PySNMP MIB module CIENA-WS-PLATFORM-TYPEDEFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/CIENA-WS-PLATFORM-TYPEDEFS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cienaWsPlatformConfig, = mibBuilder.importSymbols("CIENA-WS-MIB", "cienaWsPlatformConfig")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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

mibBuilder.exportSymbols("CIENA-WS-PLATFORM-TYPEDEFS-MIB", EnabledDisabledEnum=EnabledDisabledEnum, StringMaxl44=StringMaxl44, StringMaxl32=StringMaxl32, StringMaxl16=StringMaxl16, PYSNMP_MODULE_ID=cienaWsPlatformTypedefsMIB, cienaWsPlatformTypedefsMIB=cienaWsPlatformTypedefsMIB)
