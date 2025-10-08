#
# PySNMP MIB module ALTIGA-SSL-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/ALTIGA-SSL-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:40 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
alSslMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alSslMibModule")
alStatsSsl, alSslGroup = mibBuilder.importSymbols("ALTIGA-MIB", "alStatsSsl", "alSslGroup")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaSslStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2))
altigaSslStatsMibModule.setRevisions(('2002-09-05 13:00', '2002-07-10 00:00',))
if mibBuilder.loadTexts: altigaSslStatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaSslStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsSslGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1))
alSslStatsTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsTotalSessions.setStatus('current')
alSslStatsActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsActiveSessions.setStatus('current')
alSslStatsMaxSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsMaxSessions.setStatus('current')
alSslStatsPreDecryptOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsPreDecryptOctets.setStatus('current')
alSslStatsPostDecryptOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsPostDecryptOctets.setStatus('current')
alSslStatsPreEncryptOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsPreEncryptOctets.setStatus('current')
alSslStatsPostEncryptOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsPostEncryptOctets.setStatus('current')
altigaSslStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2, 1))
altigaSslStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2, 1, 1))
altigaSslStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2, 1, 1, 1)).setObjects(("ALTIGA-SSL-STATS-MIB", "altigaSslStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaSslStatsMibCompliance = altigaSslStatsMibCompliance.setStatus('current')
altigaSslStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 26, 2)).setObjects(("ALTIGA-SSL-STATS-MIB", "alSslStatsTotalSessions"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsActiveSessions"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsMaxSessions"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsPreDecryptOctets"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsPostDecryptOctets"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsPreEncryptOctets"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsPostEncryptOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaSslStatsGroup = altigaSslStatsGroup.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-SSL-STATS-MIB", alSslStatsActiveSessions=alSslStatsActiveSessions, PYSNMP_MODULE_ID=altigaSslStatsMibModule, altigaSslStatsMibCompliances=altigaSslStatsMibCompliances, alSslStatsPostEncryptOctets=alSslStatsPostEncryptOctets, altigaSslStatsMibConformance=altigaSslStatsMibConformance, alSslStatsMaxSessions=alSslStatsMaxSessions, alSslStatsPreDecryptOctets=alSslStatsPreDecryptOctets, altigaSslStatsGroup=altigaSslStatsGroup, altigaSslStatsMibCompliance=altigaSslStatsMibCompliance, alSslStatsPostDecryptOctets=alSslStatsPostDecryptOctets, alSslStatsTotalSessions=alSslStatsTotalSessions, alStatsSslGlobal=alStatsSslGlobal, altigaSslStatsMibModule=altigaSslStatsMibModule, alSslStatsPreEncryptOctets=alSslStatsPreEncryptOctets)
