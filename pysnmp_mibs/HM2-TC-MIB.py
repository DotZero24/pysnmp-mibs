#
# PySNMP MIB module HM2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hirschmann/HM2-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:23 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hm2TcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 1))
hm2TcMib.setRevisions(('2011-03-16 00:00',))
if mibBuilder.loadTexts: hm2TcMib.setLastUpdated('201103160000Z')
if mibBuilder.loadTexts: hm2TcMib.setOrganization('Hirschmann Automation and Control GmbH')
hirschmann = MibIdentifier((1, 3, 6, 1, 4, 1, 248))
hm2ConfigurationMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11))
hm2PlatformMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12))
class HmEnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class HmActionValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("noop", 1), ("action", 2))

class HmTimeHHMM24(TextualConvention, OctetString):
    status = 'current'
    displayHint = '5a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 5)

class HmTimeSeconds1970(TextualConvention, Unsigned32):
    status = 'current'

class HmLargeDisplayString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class HmExtraLargeDisplayString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1400a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1400)

class HmAccessLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("readWrite", 1), ("readOnly", 2))

mibBuilder.exportSymbols("HM2-TC-MIB", hm2PlatformMibs=hm2PlatformMibs, HmTimeHHMM24=HmTimeHHMM24, HmExtraLargeDisplayString=HmExtraLargeDisplayString, hirschmann=hirschmann, hm2ConfigurationMibs=hm2ConfigurationMibs, HmEnabledStatus=HmEnabledStatus, HmAccessLevel=HmAccessLevel, hm2TcMib=hm2TcMib, HmActionValue=HmActionValue, HmLargeDisplayString=HmLargeDisplayString, PYSNMP_MODULE_ID=hm2TcMib, HmTimeSeconds1970=HmTimeSeconds1970)
