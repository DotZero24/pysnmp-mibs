#
# PySNMP MIB module RUGGEDCOM-TIMECONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/RUGGEDCOM-TIMECONFIG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ruggedcomMgmt, = mibBuilder.importSymbols("RUGGEDCOM-MIB", "ruggedcomMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "DisplayString", "TextualConvention")
rcTimeConfig = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 4, 11))
rcTimeConfig.setRevisions(('2015-09-28 13:00',))
if mibBuilder.loadTexts: rcTimeConfig.setLastUpdated('201509281300Z')
if mibBuilder.loadTexts: rcTimeConfig.setOrganization('Siemens Canada Ltd.')
class RcTimeSyncStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("notPresent", 1), ("disabled", 2), ("locked", 3), ("searching", 4), ("aquiring", 5), ("holdover", 6), ("parity", 7), ("decoder", 8), ("shortckt", 9), ("cfgfailure", 10))

rcTimeConfigBase = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 4, 11, 1))
rcTimeConfigConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 4, 11, 3))
rcTimeConfigGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 4, 11, 3, 2))
rcTimeSource = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(6, 2, 4, 5, 3))).clone(namedValues=NamedValues(("localclk", 6), ("irigb", 2), ("ieee1588", 4), ("ntp", 5), ("gps", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcTimeSource.setStatus('current')
rcTimeAndDate = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 11, 1, 2), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcTimeAndDate.setStatus('current')
rcDSTOfst = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 86399))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcDSTOfst.setStatus('current')
rcCurrentUTCOfst = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 11, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcCurrentUTCOfst.setStatus('current')
rcLeapSecPending = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 11, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcLeapSecPending.setStatus('current')
rcDSTRule = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 11, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcDSTRule.setStatus('current')
rcTimeConfigBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 11, 3, 2, 1)).setObjects(("RUGGEDCOM-TIMECONFIG-MIB", "rcTimeSource"), ("RUGGEDCOM-TIMECONFIG-MIB", "rcTimeAndDate"), ("RUGGEDCOM-TIMECONFIG-MIB", "rcDSTOfst"), ("RUGGEDCOM-TIMECONFIG-MIB", "rcCurrentUTCOfst"), ("RUGGEDCOM-TIMECONFIG-MIB", "rcLeapSecPending"), ("RUGGEDCOM-TIMECONFIG-MIB", "rcDSTRule"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcTimeConfigBaseGroup = rcTimeConfigBaseGroup.setStatus('current')
mibBuilder.exportSymbols("RUGGEDCOM-TIMECONFIG-MIB", rcLeapSecPending=rcLeapSecPending, PYSNMP_MODULE_ID=rcTimeConfig, rcTimeConfigGroups=rcTimeConfigGroups, rcTimeAndDate=rcTimeAndDate, rcDSTOfst=rcDSTOfst, rcTimeConfigConformance=rcTimeConfigConformance, rcTimeConfigBase=rcTimeConfigBase, rcDSTRule=rcDSTRule, rcCurrentUTCOfst=rcCurrentUTCOfst, rcTimeSource=rcTimeSource, RcTimeSyncStatus=RcTimeSyncStatus, rcTimeConfig=rcTimeConfig, rcTimeConfigBaseGroup=rcTimeConfigBaseGroup)
