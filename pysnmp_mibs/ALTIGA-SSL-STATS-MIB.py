#
# PySNMP MIB module ALTIGA-SSL-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/ALTIGA-SSL-STATS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:02 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
alSslMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alSslMibModule")
alSslGroup, alStatsSsl = mibBuilder.importSymbols("ALTIGA-MIB", "alSslGroup", "alStatsSsl")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ALTIGA-SSL-STATS-MIB", PYSNMP_MODULE_ID=altigaSslStatsMibModule, alSslStatsActiveSessions=alSslStatsActiveSessions, alSslStatsPostEncryptOctets=alSslStatsPostEncryptOctets, alSslStatsPreDecryptOctets=alSslStatsPreDecryptOctets, altigaSslStatsMibModule=altigaSslStatsMibModule, alSslStatsPostDecryptOctets=alSslStatsPostDecryptOctets, altigaSslStatsMibCompliance=altigaSslStatsMibCompliance, alSslStatsPreEncryptOctets=alSslStatsPreEncryptOctets, altigaSslStatsMibConformance=altigaSslStatsMibConformance, altigaSslStatsGroup=altigaSslStatsGroup, altigaSslStatsMibCompliances=altigaSslStatsMibCompliances, alSslStatsMaxSessions=alSslStatsMaxSessions, alStatsSslGlobal=alStatsSslGlobal, alSslStatsTotalSessions=alSslStatsTotalSessions)
