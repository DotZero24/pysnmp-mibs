#
# PySNMP MIB module NEWTEC-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/newtec/NEWTEC-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ntcGeneric, = mibBuilder.importSymbols("NEWTEC-MAIN-MIB", "ntcGeneric")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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

mibBuilder.exportSymbols("NEWTEC-TC-MIB", NtcPid=NtcPid, NtcEnable=NtcEnable, ntcGenTextualConvention=ntcGenTextualConvention, NtcSystemTime=NtcSystemTime, PYSNMP_MODULE_ID=ntcGenTextualConvention, NtcNetworkAddress=NtcNetworkAddress, NtcAlarmState=NtcAlarmState)
