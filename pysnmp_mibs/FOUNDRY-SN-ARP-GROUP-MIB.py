#
# PySNMP MIB module FOUNDRY-SN-ARP-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/FOUNDRY-SN-ARP-GROUP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
snSwitch, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "snSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("FOUNDRY-SN-ARP-GROUP-MIB", snArpStatsRequestSent=snArpStatsRequestSent, snArpStatsPendingDrop=snArpStatsPendingDrop, snArpStatsInvalidSource=snArpStatsInvalidSource, snArpStatsInvalidDestination=snArpStatsInvalidDestination, snArpInfo=snArpInfo, snArpStatsRequestReceived=snArpStatsRequestReceived, PYSNMP_MODULE_ID=snArpInfo, snArpStatsRepliesSent=snArpStatsRepliesSent, snArpStatsTotalReceived=snArpStatsTotalReceived, snArpStats=snArpStats)
