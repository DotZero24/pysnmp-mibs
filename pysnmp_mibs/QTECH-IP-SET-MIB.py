#
# PySNMP MIB module QTECH-IP-SET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-IP-SET-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:05 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("QTECH-IP-SET-MIB", qtechIPSetipAddressAddr=qtechIPSetipAddressAddr, qtechIpSetMIBCompliances=qtechIpSetMIBCompliances, qtechIPSetipAddressStatus=qtechIPSetipAddressStatus, qtechIPSetMIBObjects=qtechIPSetMIBObjects, qtechIPSetipAddressTable=qtechIPSetipAddressTable, qtechIpSetMIBGroups=qtechIpSetMIBGroups, qtechIPSetMgmt=qtechIPSetMgmt, qtechIPSetipAddressType=qtechIPSetipAddressType, qtechIPSetipAddressMask=qtechIPSetipAddressMask, qtechIpSetMIBConformance=qtechIpSetMIBConformance, qtechIpSetMIBGroup=qtechIpSetMIBGroup, PYSNMP_MODULE_ID=qtechIPSetMgmt, qtechIPSetipAddressIfIndex=qtechIPSetipAddressIfIndex, qtechIPSetIpAddressEntry=qtechIPSetIpAddressEntry, qtechIcmpMIBCompliance=qtechIcmpMIBCompliance)
