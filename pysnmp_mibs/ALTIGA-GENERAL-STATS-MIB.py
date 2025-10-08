#
# PySNMP MIB module ALTIGA-GENERAL-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/ALTIGA-GENERAL-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:41 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
alGeneralMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alGeneralMibModule")
alGeneralGroup, alStatsGeneral = mibBuilder.importSymbols("ALTIGA-MIB", "alGeneralGroup", "alStatsGeneral")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ALTIGA-GENERAL-STATS-MIB", alStatsGeneralGlobal=alStatsGeneralGlobal, alGeneralGaugeActiveSessions=alGeneralGaugeActiveSessions, alGeneralTime=alGeneralTime, altigaGeneralStatsMibModule=altigaGeneralStatsMibModule, alGeneralGaugeThroughput=alGeneralGaugeThroughput, PYSNMP_MODULE_ID=altigaGeneralStatsMibModule, altigaGeneralStatsMibConformance=altigaGeneralStatsMibConformance, altigaGeneralStatsMibCompliances=altigaGeneralStatsMibCompliances, altigaGeneralStatsMibCompliance=altigaGeneralStatsMibCompliance, alGeneralGaugeCpuUtil=alGeneralGaugeCpuUtil, altigaGeneralStatsGroup=altigaGeneralStatsGroup, alGeneralTimeZone=alGeneralTimeZone)
