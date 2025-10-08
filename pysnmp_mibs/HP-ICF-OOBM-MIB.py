#
# PySNMP MIB module HP-ICF-OOBM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ICF-OOBM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:24 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
snmpTargetAddrEntry, = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetAddrEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
hpicfOobmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58))
hpicfOobmMIB.setRevisions(('2010-03-26 00:00', '2009-02-13 00:00',))
if mibBuilder.loadTexts: hpicfOobmMIB.setLastUpdated('201003260000Z')
if mibBuilder.loadTexts: hpicfOobmMIB.setOrganization('HP Networking')
hpicfOobmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 0))
hpicfOobmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1))
hpicfOobmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3))
class HpicfOobmServerIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("telnet", 1), ("ssh", 2), ("tftp", 3), ("http", 4), ("snmp", 5))

class HpicfOobmServerState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("oobm", 1), ("data", 2), ("both", 3))

hpicfOobmScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 1))
hpicfOobmStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfOobmStatus.setStatus('current')
hpicfOobmServers = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 2))
hpicfOobmServerTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 2, 1), )
if mibBuilder.loadTexts: hpicfOobmServerTable.setStatus('current')
hpicfOobmServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 2, 1, 1), ).setIndexNames((0, "HP-ICF-OOBM-MIB", "hpicfOobmServerType"))
if mibBuilder.loadTexts: hpicfOobmServerEntry.setStatus('current')
hpicfOobmServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 2, 1, 1, 1), HpicfOobmServerIndex())
if mibBuilder.loadTexts: hpicfOobmServerType.setStatus('current')
hpicfOobmServerListenMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 2, 1, 1, 2), HpicfOobmServerState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfOobmServerListenMode.setStatus('current')
hpicfOobmSnmpTargetAddrIsOobm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 3))
hpicfSnmpTargetAddrIsOobmTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 3, 1), )
if mibBuilder.loadTexts: hpicfSnmpTargetAddrIsOobmTable.setStatus('current')
hpicfSnmpTargetAddrIsOobmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 3, 1, 1), )
snmpTargetAddrEntry.registerAugmentions(("HP-ICF-OOBM-MIB", "hpicfSnmpTargetAddrIsOobmEntry"))
hpicfSnmpTargetAddrIsOobmEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfSnmpTargetAddrIsOobmEntry.setStatus('current')
hpicfSnmpTargetAddrIsOobm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 3, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSnmpTargetAddrIsOobm.setStatus('current')
hpicfOobmDefGateway = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 4))
hpicfOobmDefGatewayTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 4, 1), )
if mibBuilder.loadTexts: hpicfOobmDefGatewayTable.setStatus('current')
hpicfOobmDefGatewayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 4, 1, 1), ).setIndexNames((0, "HP-ICF-OOBM-MIB", "hpicfOobmDefGatewayType"))
if mibBuilder.loadTexts: hpicfOobmDefGatewayEntry.setStatus('current')
hpicfOobmDefGatewayType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 4, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hpicfOobmDefGatewayType.setStatus('current')
hpicfOobmDefGatewayAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 4, 1, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfOobmDefGatewayAddr.setStatus('current')
hpicfOobmStackMembers = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 5))
hpicfOobmMemberDefGatewayTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 5, 3), )
if mibBuilder.loadTexts: hpicfOobmMemberDefGatewayTable.setStatus('current')
hpicfOobmMemberDefGatewayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 5, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HP-ICF-OOBM-MIB", "hpicfOobmMemberDefGatewayType"))
if mibBuilder.loadTexts: hpicfOobmMemberDefGatewayEntry.setStatus('current')
hpicfOobmMemberDefGatewayType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 5, 3, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hpicfOobmMemberDefGatewayType.setStatus('current')
hpicfOobmMemberDefGatewayAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 5, 3, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfOobmMemberDefGatewayAddr.setStatus('current')
hpicfOobmCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 1))
hpicfOobmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2))
hpicfOobmMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 1, 1)).setObjects(("HP-ICF-OOBM-MIB", "hpicfOobmScalarsGroup"), ("HP-ICF-OOBM-MIB", "hpicfOobmServersGroup"), ("HP-ICF-OOBM-MIB", "hpicfSnmpTargetAddrIsOobmGroup"), ("HP-ICF-OOBM-MIB", "hpicfOobmDefGatewayGroup"), ("HP-ICF-OOBM-MIB", "hpicfOobmMemberGroup"), ("HP-ICF-OOBM-MIB", "hpicfOobmGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfOobmMibCompliance = hpicfOobmMibCompliance.setStatus('current')
hpicfOobmScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2, 1)).setObjects(("HP-ICF-OOBM-MIB", "hpicfOobmStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfOobmScalarsGroup = hpicfOobmScalarsGroup.setStatus('current')
hpicfOobmServersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2, 2)).setObjects(("HP-ICF-OOBM-MIB", "hpicfOobmServerListenMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfOobmServersGroup = hpicfOobmServersGroup.setStatus('current')
hpicfSnmpTargetAddrIsOobmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2, 3)).setObjects(("HP-ICF-OOBM-MIB", "hpicfSnmpTargetAddrIsOobm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSnmpTargetAddrIsOobmGroup = hpicfSnmpTargetAddrIsOobmGroup.setStatus('current')
hpicfOobmDefGatewayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2, 4)).setObjects(("HP-ICF-OOBM-MIB", "hpicfOobmDefGatewayAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfOobmDefGatewayGroup = hpicfOobmDefGatewayGroup.setStatus('current')
hpicfOobmMemberGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2, 5)).setObjects(("HP-ICF-OOBM-MIB", "hpicfOobmMemberDefGatewayAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfOobmMemberGroup = hpicfOobmMemberGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-OOBM-MIB", hpicfOobmServerType=hpicfOobmServerType, hpicfOobmMIB=hpicfOobmMIB, hpicfOobmServersGroup=hpicfOobmServersGroup, hpicfOobmMemberDefGatewayTable=hpicfOobmMemberDefGatewayTable, hpicfSnmpTargetAddrIsOobmGroup=hpicfSnmpTargetAddrIsOobmGroup, hpicfOobmMemberDefGatewayAddr=hpicfOobmMemberDefGatewayAddr, hpicfOobmServerListenMode=hpicfOobmServerListenMode, hpicfOobmDefGatewayGroup=hpicfOobmDefGatewayGroup, hpicfOobmScalarsGroup=hpicfOobmScalarsGroup, hpicfSnmpTargetAddrIsOobmTable=hpicfSnmpTargetAddrIsOobmTable, hpicfOobmObjects=hpicfOobmObjects, hpicfOobmDefGatewayEntry=hpicfOobmDefGatewayEntry, hpicfOobmDefGatewayAddr=hpicfOobmDefGatewayAddr, hpicfOobmGroups=hpicfOobmGroups, hpicfOobmMemberDefGatewayEntry=hpicfOobmMemberDefGatewayEntry, hpicfSnmpTargetAddrIsOobmEntry=hpicfSnmpTargetAddrIsOobmEntry, hpicfOobmSnmpTargetAddrIsOobm=hpicfOobmSnmpTargetAddrIsOobm, HpicfOobmServerState=HpicfOobmServerState, hpicfOobmStatus=hpicfOobmStatus, hpicfOobmConformance=hpicfOobmConformance, hpicfOobmDefGateway=hpicfOobmDefGateway, hpicfOobmMemberDefGatewayType=hpicfOobmMemberDefGatewayType, hpicfOobmMemberGroup=hpicfOobmMemberGroup, hpicfSnmpTargetAddrIsOobm=hpicfSnmpTargetAddrIsOobm, PYSNMP_MODULE_ID=hpicfOobmMIB, hpicfOobmDefGatewayType=hpicfOobmDefGatewayType, hpicfOobmServers=hpicfOobmServers, hpicfOobmStackMembers=hpicfOobmStackMembers, hpicfOobmServerTable=hpicfOobmServerTable, hpicfOobmDefGatewayTable=hpicfOobmDefGatewayTable, hpicfOobmCompliance=hpicfOobmCompliance, hpicfOobmNotifications=hpicfOobmNotifications, hpicfOobmScalars=hpicfOobmScalars, hpicfOobmServerEntry=hpicfOobmServerEntry, hpicfOobmMibCompliance=hpicfOobmMibCompliance, HpicfOobmServerIndex=HpicfOobmServerIndex)
