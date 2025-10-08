#
# PySNMP MIB module QTECH-IP-SET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-IP-SET-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:13:59 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
qtechIPSetMgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111))
qtechIPSetMgmt.setRevisions(('2012-02-15 00:00',))
if mibBuilder.loadTexts: qtechIPSetMgmt.setLastUpdated('201202150000Z')
if mibBuilder.loadTexts: qtechIPSetMgmt.setOrganization('Qtech Networks Co.,Ltd.')
qtechIPSetMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 1))
qtechIPSetipAddressTable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 1, 1), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechIPSetipAddressTable.setStatus('current')
qtechIPSetIpAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 1, 1, 1), ).setMaxAccess("readonly").setIndexNames((0, "QTECH-IP-SET-MIB", "qtechIPSetipAddressIfIndex"))
if mibBuilder.loadTexts: qtechIPSetIpAddressEntry.setStatus('current')
qtechIPSetipAddressIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechIPSetipAddressIfIndex.setStatus('current')
qtechIPSetipAddressAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechIPSetipAddressAddr.setStatus('current')
qtechIPSetipAddressMask = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechIPSetipAddressMask.setStatus('current')
qtechIPSetipAddressStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("delete", 0), ("add", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechIPSetipAddressStatus.setStatus('current')
qtechIPSetipAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unicast", 1), ("anycast", 2), ("broadcast", 3))).clone('unicast')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechIPSetipAddressType.setStatus('current')
qtechIpSetMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 2))
qtechIpSetMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 2, 1))
qtechIpSetMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 2, 2))
qtechIcmpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 2, 1, 1)).setObjects(("QTECH-IP-SET-MIB", "qtechIpSetMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechIcmpMIBCompliance = qtechIcmpMIBCompliance.setStatus('current')
qtechIpSetMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 2, 2, 1)).setObjects(("QTECH-IP-SET-MIB", "qtechIPSetipAddressIfIndex"), ("QTECH-IP-SET-MIB", "qtechIPSetipAddressAddr"), ("QTECH-IP-SET-MIB", "qtechIPSetipAddressMask"), ("QTECH-IP-SET-MIB", "qtechIPSetipAddressStatus"), ("QTECH-IP-SET-MIB", "qtechIPSetipAddressType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechIpSetMIBGroup = qtechIpSetMIBGroup.setStatus('current')
mibBuilder.exportSymbols("QTECH-IP-SET-MIB", PYSNMP_MODULE_ID=qtechIPSetMgmt, qtechIPSetMgmt=qtechIPSetMgmt, qtechIPSetIpAddressEntry=qtechIPSetIpAddressEntry, qtechIPSetipAddressStatus=qtechIPSetipAddressStatus, qtechIpSetMIBConformance=qtechIpSetMIBConformance, qtechIpSetMIBGroups=qtechIpSetMIBGroups, qtechIPSetipAddressTable=qtechIPSetipAddressTable, qtechIPSetipAddressIfIndex=qtechIPSetipAddressIfIndex, qtechIcmpMIBCompliance=qtechIcmpMIBCompliance, qtechIPSetMIBObjects=qtechIPSetMIBObjects, qtechIPSetipAddressType=qtechIPSetipAddressType, qtechIPSetipAddressMask=qtechIPSetipAddressMask, qtechIpSetMIBGroup=qtechIpSetMIBGroup, qtechIPSetipAddressAddr=qtechIPSetipAddressAddr, qtechIpSetMIBCompliances=qtechIpSetMIBCompliances)
