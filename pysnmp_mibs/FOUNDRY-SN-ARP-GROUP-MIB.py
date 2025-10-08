#
# PySNMP MIB module FOUNDRY-SN-ARP-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/FOUNDRY-SN-ARP-GROUP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:56 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
snSwitch, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "snSwitch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snArpInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22))
if mibBuilder.loadTexts: snArpInfo.setLastUpdated('200402090000Z')
if mibBuilder.loadTexts: snArpInfo.setOrganization('Ruckus Wireless Network')
snArpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1))
snArpStatsTotalReceived = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snArpStatsTotalReceived.setStatus('current')
snArpStatsRequestReceived = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snArpStatsRequestReceived.setStatus('current')
snArpStatsRequestSent = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snArpStatsRequestSent.setStatus('current')
snArpStatsRepliesSent = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snArpStatsRepliesSent.setStatus('current')
snArpStatsPendingDrop = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snArpStatsPendingDrop.setStatus('current')
snArpStatsInvalidSource = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snArpStatsInvalidSource.setStatus('current')
snArpStatsInvalidDestination = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snArpStatsInvalidDestination.setStatus('current')
mibBuilder.exportSymbols("FOUNDRY-SN-ARP-GROUP-MIB", snArpInfo=snArpInfo, snArpStatsRequestReceived=snArpStatsRequestReceived, snArpStatsTotalReceived=snArpStatsTotalReceived, PYSNMP_MODULE_ID=snArpInfo, snArpStatsRequestSent=snArpStatsRequestSent, snArpStatsPendingDrop=snArpStatsPendingDrop, snArpStats=snArpStats, snArpStatsInvalidDestination=snArpStatsInvalidDestination, snArpStatsInvalidSource=snArpStatsInvalidSource, snArpStatsRepliesSent=snArpStatsRepliesSent)
