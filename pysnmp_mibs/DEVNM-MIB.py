#
# PySNMP MIB module DEVNM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aperto/DEVNM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aniDevNetworkManager = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 2, 7))
if mibBuilder.loadTexts: aniDevNetworkManager.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniDevNetworkManager.setOrganization('Aperto Networks')
aniDevNumManagingHosts = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 7, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevNumManagingHosts.setStatus('current')
aniDevNetworkMgrAccessTable = MibTable((1, 3, 6, 1, 4, 1, 4325, 2, 7, 2), )
if mibBuilder.loadTexts: aniDevNetworkMgrAccessTable.setStatus('current')
aniDevNetworkMgrAccessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4325, 2, 7, 2, 1), ).setIndexNames((0, "DEVNM-MIB", "aniDevNMAccessIndex"))
if mibBuilder.loadTexts: aniDevNetworkMgrAccessEntry.setStatus('current')
aniDevNMAccessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 2, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: aniDevNMAccessIndex.setStatus('current')
aniDevNMAccessIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 2, 7, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevNMAccessIp.setStatus('current')
aniDevNMReadAccessCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 2, 7, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31)).clone('public')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevNMReadAccessCommunity.setStatus('current')
aniDevNMWriteAccessCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 2, 7, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31)).clone('private')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevNMWriteAccessCommunity.setStatus('current')
aniDevNMAccessControl = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 2, 7, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("read", 1), ("readWrite", 2), ("roWithTraps", 3), ("rwWithTraps", 4), ("trapsOnly", 5))).clone('readWrite')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevNMAccessControl.setStatus('current')
mibBuilder.exportSymbols("DEVNM-MIB", PYSNMP_MODULE_ID=aniDevNetworkManager, aniDevNetworkMgrAccessEntry=aniDevNetworkMgrAccessEntry, aniDevNMAccessIp=aniDevNMAccessIp, aniDevNumManagingHosts=aniDevNumManagingHosts, aniDevNetworkMgrAccessTable=aniDevNetworkMgrAccessTable, aniDevNetworkManager=aniDevNetworkManager, aniDevNMAccessControl=aniDevNMAccessControl, aniDevNMAccessIndex=aniDevNMAccessIndex, aniDevNMReadAccessCommunity=aniDevNMReadAccessCommunity, aniDevNMWriteAccessCommunity=aniDevNMWriteAccessCommunity)
