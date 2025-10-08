#
# PySNMP MIB module ALTIGA-VERSION-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/ALTIGA-VERSION-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:39 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
alVersionMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alVersionMibModule")
alVersionGroup, alStatsVersion = mibBuilder.importSymbols("ALTIGA-MIB", "alVersionGroup", "alStatsVersion")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaVersionStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2))
altigaVersionStatsMibModule.setRevisions(('2002-09-05 13:00',))
if mibBuilder.loadTexts: altigaVersionStatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaVersionStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsVersionGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1))
alVersionMajor = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionMajor.setStatus('current')
alVersionMinor = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionMinor.setStatus('current')
alVersionInt = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionInt.setStatus('current')
alVersionString = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionString.setStatus('current')
alVersionLong = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionLong.setStatus('current')
alVersionShort = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionShort.setStatus('current')
alVersionBoot = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionBoot.setStatus('current')
altigaVersionStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2, 1))
altigaVersionStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2, 1, 1))
altigaVersionStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2, 1, 1, 1)).setObjects(("ALTIGA-VERSION-STATS-MIB", "altigaVersionStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaVersionStatsMibCompliance = altigaVersionStatsMibCompliance.setStatus('current')
altigaVersionStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 1, 2)).setObjects(("ALTIGA-VERSION-STATS-MIB", "alVersionMajor"), ("ALTIGA-VERSION-STATS-MIB", "alVersionMinor"), ("ALTIGA-VERSION-STATS-MIB", "alVersionInt"), ("ALTIGA-VERSION-STATS-MIB", "alVersionString"), ("ALTIGA-VERSION-STATS-MIB", "alVersionLong"), ("ALTIGA-VERSION-STATS-MIB", "alVersionShort"), ("ALTIGA-VERSION-STATS-MIB", "alVersionBoot"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaVersionStatsGroup = altigaVersionStatsGroup.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-VERSION-STATS-MIB", alVersionLong=alVersionLong, alVersionShort=alVersionShort, alVersionMajor=alVersionMajor, PYSNMP_MODULE_ID=altigaVersionStatsMibModule, altigaVersionStatsMibCompliances=altigaVersionStatsMibCompliances, altigaVersionStatsMibConformance=altigaVersionStatsMibConformance, altigaVersionStatsGroup=altigaVersionStatsGroup, alVersionString=alVersionString, alStatsVersionGlobal=alStatsVersionGlobal, alVersionMinor=alVersionMinor, altigaVersionStatsMibModule=altigaVersionStatsMibModule, alVersionBoot=alVersionBoot, altigaVersionStatsMibCompliance=altigaVersionStatsMibCompliance, alVersionInt=alVersionInt)
