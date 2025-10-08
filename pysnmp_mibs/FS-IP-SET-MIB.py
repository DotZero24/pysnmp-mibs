#
# PySNMP MIB module FS-IP-SET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-IP-SET-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("FS-IP-SET-MIB", fsIpSetMIBGroup=fsIpSetMIBGroup, fsIPSetMIBObjects=fsIPSetMIBObjects, fsIPSetipAddressAddr=fsIPSetipAddressAddr, fsIPSetIpAddressEntry=fsIPSetIpAddressEntry, fsIPSetipAddressStatus=fsIPSetipAddressStatus, fsIPSetMgmt=fsIPSetMgmt, fsIPSetipAddressTable=fsIPSetipAddressTable, fsIPSetipAddressIfIndex=fsIPSetipAddressIfIndex, PYSNMP_MODULE_ID=fsIPSetMgmt, fsIPSetipAddressMask=fsIPSetipAddressMask, fsIpSetMIBGroups=fsIpSetMIBGroups, fsIpSetMIBConformance=fsIpSetMIBConformance, fsIcmpMIBCompliance=fsIcmpMIBCompliance, fsIpSetMIBCompliances=fsIpSetMIBCompliances, fsIPSetipAddressType=fsIPSetipAddressType)
