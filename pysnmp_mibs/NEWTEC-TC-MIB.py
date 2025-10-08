#
# PySNMP MIB module NEWTEC-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/newtec/NEWTEC-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ntcGeneric, = mibBuilder.importSymbols("NEWTEC-MAIN-MIB", "ntcGeneric")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntcGenTextualConvention = ModuleIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 1, 1))
ntcGenTextualConvention.setRevisions(('2012-06-28 12:00',))
if mibBuilder.loadTexts: ntcGenTextualConvention.setLastUpdated('201206281200Z')
if mibBuilder.loadTexts: ntcGenTextualConvention.setOrganization('Newtec Cy')
class NtcAlarmState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class NtcEnable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class NtcNetworkAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '7a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(7, 18)

class NtcPid(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class NtcSystemTime(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

mibBuilder.exportSymbols("NEWTEC-TC-MIB", PYSNMP_MODULE_ID=ntcGenTextualConvention, NtcPid=NtcPid, NtcNetworkAddress=NtcNetworkAddress, NtcAlarmState=NtcAlarmState, ntcGenTextualConvention=ntcGenTextualConvention, NtcSystemTime=NtcSystemTime, NtcEnable=NtcEnable)
