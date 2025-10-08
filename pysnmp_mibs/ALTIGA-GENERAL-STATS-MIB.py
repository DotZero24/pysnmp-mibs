#
# PySNMP MIB module ALTIGA-GENERAL-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/ALTIGA-GENERAL-STATS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:03 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
alGeneralMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alGeneralMibModule")
alGeneralGroup, alStatsGeneral = mibBuilder.importSymbols("ALTIGA-MIB", "alGeneralGroup", "alStatsGeneral")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
altigaGeneralStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2))
altigaGeneralStatsMibModule.setRevisions(('2002-09-11 13:00', '2002-07-10 00:00',))
if mibBuilder.loadTexts: altigaGeneralStatsMibModule.setLastUpdated('200209111300Z')
if mibBuilder.loadTexts: altigaGeneralStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsGeneralGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1))
alGeneralTime = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralTime.setStatus('current')
alGeneralGaugeCpuUtil = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralGaugeCpuUtil.setStatus('current')
alGeneralGaugeActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralGaugeActiveSessions.setStatus('current')
alGeneralGaugeThroughput = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralGaugeThroughput.setStatus('current')
alGeneralTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralTimeZone.setStatus('current')
altigaGeneralStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2, 1))
altigaGeneralStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2, 1, 1))
altigaGeneralStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2, 1, 1, 1)).setObjects(("ALTIGA-GENERAL-STATS-MIB", "altigaGeneralStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaGeneralStatsMibCompliance = altigaGeneralStatsMibCompliance.setStatus('current')
altigaGeneralStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 25, 2)).setObjects(("ALTIGA-GENERAL-STATS-MIB", "alGeneralTime"), ("ALTIGA-GENERAL-STATS-MIB", "alGeneralGaugeCpuUtil"), ("ALTIGA-GENERAL-STATS-MIB", "alGeneralGaugeActiveSessions"), ("ALTIGA-GENERAL-STATS-MIB", "alGeneralGaugeThroughput"), ("ALTIGA-GENERAL-STATS-MIB", "alGeneralTimeZone"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaGeneralStatsGroup = altigaGeneralStatsGroup.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-GENERAL-STATS-MIB", alGeneralTimeZone=alGeneralTimeZone, alGeneralGaugeActiveSessions=alGeneralGaugeActiveSessions, alStatsGeneralGlobal=alStatsGeneralGlobal, altigaGeneralStatsMibCompliance=altigaGeneralStatsMibCompliance, altigaGeneralStatsGroup=altigaGeneralStatsGroup, PYSNMP_MODULE_ID=altigaGeneralStatsMibModule, altigaGeneralStatsMibConformance=altigaGeneralStatsMibConformance, alGeneralTime=alGeneralTime, alGeneralGaugeThroughput=alGeneralGaugeThroughput, alGeneralGaugeCpuUtil=alGeneralGaugeCpuUtil, altigaGeneralStatsMibModule=altigaGeneralStatsMibModule, altigaGeneralStatsMibCompliances=altigaGeneralStatsMibCompliances)
