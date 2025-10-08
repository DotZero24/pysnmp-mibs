#
# PySNMP MIB module DEVNM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aperto/DEVNM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DEVNM-MIB", PYSNMP_MODULE_ID=aniDevNetworkManager, aniDevNMWriteAccessCommunity=aniDevNMWriteAccessCommunity, aniDevNMAccessIp=aniDevNMAccessIp, aniDevNMAccessIndex=aniDevNMAccessIndex, aniDevNMReadAccessCommunity=aniDevNMReadAccessCommunity, aniDevNumManagingHosts=aniDevNumManagingHosts, aniDevNetworkManager=aniDevNetworkManager, aniDevNMAccessControl=aniDevNMAccessControl, aniDevNetworkMgrAccessEntry=aniDevNetworkMgrAccessEntry, aniDevNetworkMgrAccessTable=aniDevNetworkMgrAccessTable)
