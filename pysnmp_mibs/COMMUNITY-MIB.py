#
# PySNMP MIB module COMMUNITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cabletron/COMMUNITY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("COMMUNITY-MIB", communityTable=communityTable, cabletron=cabletron, community=community, communityIndex=communityIndex, communityName=communityName, communityIPAddr=communityIPAddr, communityTrap=communityTrap, communityEntry=communityEntry, commsDevice=commsDevice)
