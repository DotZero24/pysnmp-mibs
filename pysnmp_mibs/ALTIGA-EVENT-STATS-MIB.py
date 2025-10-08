#
# PySNMP MIB module ALTIGA-EVENT-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/ALTIGA-EVENT-STATS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:02 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
alEventMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alEventMibModule")
alEventGroup, alStatsEvent = mibBuilder.importSymbols("ALTIGA-MIB", "alEventGroup", "alStatsEvent")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
altigaEventStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2))
altigaEventStatsMibModule.setRevisions(('2003-01-13 00:00', '2002-07-10 00:00',))
if mibBuilder.loadTexts: altigaEventStatsMibModule.setLastUpdated('200301130000Z')
if mibBuilder.loadTexts: altigaEventStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsEventGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 1))
alStatsEventNotificationId = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alStatsEventNotificationId.setStatus('current')
alEventStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2), )
if mibBuilder.loadTexts: alEventStatsTable.setStatus('current')
alEventStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1), ).setIndexNames((0, "ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"), (0, "ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"))
if mibBuilder.loadTexts: alEventStatsEntry.setStatus('current')
alEventStatsClass = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alEventStatsClass.setStatus('current')
alEventStatsEventNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alEventStatsEventNumber.setStatus('current')
alEventStatsCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alEventStatsCount.setStatus('current')
altigaEventStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1))
altigaEventStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1))
altigaEventStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1, 1)).setObjects(("ALTIGA-EVENT-STATS-MIB", "altigaEventStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsMibCompliance = altigaEventStatsMibCompliance.setStatus('deprecated')
altigaEventStatsMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1, 2)).setObjects(("ALTIGA-EVENT-STATS-MIB", "altigaEventStatsGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsMibComplianceRev1 = altigaEventStatsMibComplianceRev1.setStatus('current')
altigaEventStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 4, 2)).setObjects(("ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsGroup = altigaEventStatsGroup.setStatus('deprecated')
altigaEventStatsGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 4, 3)).setObjects(("ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsCount"), ("ALTIGA-EVENT-STATS-MIB", "alStatsEventNotificationId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsGroupRev1 = altigaEventStatsGroupRev1.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-EVENT-STATS-MIB", altigaEventStatsMibConformance=altigaEventStatsMibConformance, altigaEventStatsGroupRev1=altigaEventStatsGroupRev1, alStatsEventGlobal=alStatsEventGlobal, altigaEventStatsMibCompliance=altigaEventStatsMibCompliance, alEventStatsEventNumber=alEventStatsEventNumber, PYSNMP_MODULE_ID=altigaEventStatsMibModule, alEventStatsEntry=alEventStatsEntry, alEventStatsCount=alEventStatsCount, altigaEventStatsGroup=altigaEventStatsGroup, alStatsEventNotificationId=alStatsEventNotificationId, altigaEventStatsMibCompliances=altigaEventStatsMibCompliances, altigaEventStatsMibComplianceRev1=altigaEventStatsMibComplianceRev1, alEventStatsClass=alEventStatsClass, alEventStatsTable=alEventStatsTable, altigaEventStatsMibModule=altigaEventStatsMibModule)
