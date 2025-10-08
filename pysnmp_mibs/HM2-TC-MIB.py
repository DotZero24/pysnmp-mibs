#
# PySNMP MIB module HM2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HM2-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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

mibBuilder.exportSymbols("HM2-TC-MIB", hm2TcMib=hm2TcMib, HmLargeDisplayString=HmLargeDisplayString, hm2PlatformMibs=hm2PlatformMibs, hirschmann=hirschmann, PYSNMP_MODULE_ID=hm2TcMib, HmActionValue=HmActionValue, HmExtraLargeDisplayString=HmExtraLargeDisplayString, hm2ConfigurationMibs=hm2ConfigurationMibs, HmAccessLevel=HmAccessLevel, HmTimeHHMM24=HmTimeHHMM24, HmEnabledStatus=HmEnabledStatus, HmTimeSeconds1970=HmTimeSeconds1970)
