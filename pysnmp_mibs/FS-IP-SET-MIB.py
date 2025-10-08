#
# PySNMP MIB module FS-IP-SET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-IP-SET-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fsIPSetMgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111))
fsIPSetMgmt.setRevisions(('2012-02-15 00:00',))
if mibBuilder.loadTexts: fsIPSetMgmt.setLastUpdated('201202150000Z')
if mibBuilder.loadTexts: fsIPSetMgmt.setOrganization('FS.COM Inc..')
fsIPSetMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 1))
fsIPSetipAddressTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 1, 1), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsIPSetipAddressTable.setStatus('current')
fsIPSetIpAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 1, 1, 1), ).setMaxAccess("readonly").setIndexNames((0, "FS-IP-SET-MIB", "fsIPSetipAddressIfIndex"))
if mibBuilder.loadTexts: fsIPSetIpAddressEntry.setStatus('current')
fsIPSetipAddressIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsIPSetipAddressIfIndex.setStatus('current')
fsIPSetipAddressAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsIPSetipAddressAddr.setStatus('current')
fsIPSetipAddressMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsIPSetipAddressMask.setStatus('current')
fsIPSetipAddressStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("delete", 0), ("add", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsIPSetipAddressStatus.setStatus('current')
fsIPSetipAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unicast", 1), ("anycast", 2), ("broadcast", 3))).clone('unicast')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsIPSetipAddressType.setStatus('current')
fsIpSetMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 2))
fsIpSetMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 2, 1))
fsIpSetMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 2, 2))
fsIcmpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 2, 1, 1)).setObjects(("FS-IP-SET-MIB", "fsIpSetMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsIcmpMIBCompliance = fsIcmpMIBCompliance.setStatus('current')
fsIpSetMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 2, 2, 1)).setObjects(("FS-IP-SET-MIB", "fsIPSetipAddressIfIndex"), ("FS-IP-SET-MIB", "fsIPSetipAddressAddr"), ("FS-IP-SET-MIB", "fsIPSetipAddressMask"), ("FS-IP-SET-MIB", "fsIPSetipAddressStatus"), ("FS-IP-SET-MIB", "fsIPSetipAddressType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsIpSetMIBGroup = fsIpSetMIBGroup.setStatus('current')
mibBuilder.exportSymbols("FS-IP-SET-MIB", fsIpSetMIBConformance=fsIpSetMIBConformance, fsIPSetMIBObjects=fsIPSetMIBObjects, fsIPSetipAddressMask=fsIPSetipAddressMask, fsIPSetipAddressAddr=fsIPSetipAddressAddr, fsIcmpMIBCompliance=fsIcmpMIBCompliance, fsIPSetipAddressType=fsIPSetipAddressType, fsIPSetIpAddressEntry=fsIPSetIpAddressEntry, fsIpSetMIBGroups=fsIpSetMIBGroups, PYSNMP_MODULE_ID=fsIPSetMgmt, fsIPSetipAddressIfIndex=fsIPSetipAddressIfIndex, fsIpSetMIBCompliances=fsIpSetMIBCompliances, fsIPSetMgmt=fsIPSetMgmt, fsIpSetMIBGroup=fsIpSetMIBGroup, fsIPSetipAddressStatus=fsIPSetipAddressStatus, fsIPSetipAddressTable=fsIPSetipAddressTable)
