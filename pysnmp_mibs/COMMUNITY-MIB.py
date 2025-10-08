#
# PySNMP MIB module COMMUNITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cabletron/COMMUNITY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:13:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
commsDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1))
community = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 52))
communityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1, 52, 2), )
if mibBuilder.loadTexts: communityTable.setStatus('mandatory')
communityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1, 52, 2, 1), ).setIndexNames((0, "COMMUNITY-MIB", "communityIndex"))
if mibBuilder.loadTexts: communityEntry.setStatus('mandatory')
communityName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 52, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: communityName.setStatus('mandatory')
communityTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 52, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: communityTrap.setStatus('mandatory')
communityIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 52, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: communityIPAddr.setStatus('mandatory')
communityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 52, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: communityIndex.setStatus('mandatory')
mibBuilder.exportSymbols("COMMUNITY-MIB", commsDevice=commsDevice, communityEntry=communityEntry, communityIndex=communityIndex, cabletron=cabletron, communityName=communityName, communityIPAddr=communityIPAddr, community=community, communityTrap=communityTrap, communityTable=communityTable)
