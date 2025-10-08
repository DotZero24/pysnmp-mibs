#
# PySNMP MIB module A3COM-HUAWEI-LswMAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-LswMAM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
hwdot1qVlanIndex, = mibBuilder.importSymbols("A3COM-HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex")
lswCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "lswCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
hwLswMacPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3))
hwLswMacPort.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hwLswMacPort.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hwLswMacPort.setOrganization(' ')
class InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class PortList(TextualConvention, OctetString):
    status = 'current'

hwdot1qMacSearchTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1), )
if mibBuilder.loadTexts: hwdot1qMacSearchTable.setStatus('current')
hwdot1qMacSearchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswMAM-MIB", "hwdot1qMacSearchAddress"), (0, "A3COM-HUAWEI-LswMAM-MIB", "hwdot1qMacSearchVlanID"))
if mibBuilder.loadTexts: hwdot1qMacSearchEntry.setStatus('current')
hwdot1qMacSearchAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qMacSearchAddress.setStatus('current')
hwdot1qMacSearchVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 4096), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qMacSearchVlanID.setStatus('current')
hwdot1qMacSearchPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qMacSearchPort.setStatus('current')
hwdot1qMacSearchAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qMacSearchAgeTime.setStatus('current')
hwdot1qTpFdbSetTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2), )
if mibBuilder.loadTexts: hwdot1qTpFdbSetTable.setStatus('current')
hwdot1qTpFdbSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex"), (0, "A3COM-HUAWEI-LswMAM-MIB", "hwdot1qTpFdbSetAddress"))
if mibBuilder.loadTexts: hwdot1qTpFdbSetEntry.setStatus('current')
hwdot1qTpFdbSetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: hwdot1qTpFdbSetAddress.setStatus('current')
hwdot1qTpFdbSetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2, 1, 2), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbSetPort.setStatus('current')
hwdot1qTpFdbSetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 6, 7, 9, 11))).clone(namedValues=NamedValues(("other", 1), ("learned", 3), ("static", 6), ("dynamic", 7), ("blackhole", 9), ("security", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbSetStatus.setStatus('current')
hwdot1qTpFdbSetOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbSetOperate.setStatus('current')
hwdot1qTpFdbGroupSetTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 3), )
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetTable.setStatus('current')
hwdot1qTpFdbGroupSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex"), (0, "A3COM-HUAWEI-LswMAM-MIB", "hwdot1qTpFdbGroupSetAddress"))
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetEntry.setStatus('current')
hwdot1qTpFdbGroupSetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 3, 1, 1), MacAddress())
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetAddress.setStatus('current')
hwdot1qTpFdbGroupSetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 3, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetPort.setStatus('current')
hwdot1qTpFdbGroupSetOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetOperate.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-LswMAM-MIB", PYSNMP_MODULE_ID=hwLswMacPort, hwdot1qMacSearchAddress=hwdot1qMacSearchAddress, hwLswMacPort=hwLswMacPort, hwdot1qTpFdbGroupSetPort=hwdot1qTpFdbGroupSetPort, hwdot1qTpFdbGroupSetAddress=hwdot1qTpFdbGroupSetAddress, InterfaceIndex=InterfaceIndex, hwdot1qTpFdbSetAddress=hwdot1qTpFdbSetAddress, hwdot1qMacSearchAgeTime=hwdot1qMacSearchAgeTime, hwdot1qTpFdbGroupSetEntry=hwdot1qTpFdbGroupSetEntry, hwdot1qMacSearchTable=hwdot1qMacSearchTable, hwdot1qTpFdbGroupSetOperate=hwdot1qTpFdbGroupSetOperate, hwdot1qMacSearchPort=hwdot1qMacSearchPort, hwdot1qTpFdbSetTable=hwdot1qTpFdbSetTable, hwdot1qTpFdbSetEntry=hwdot1qTpFdbSetEntry, hwdot1qTpFdbSetStatus=hwdot1qTpFdbSetStatus, hwdot1qTpFdbSetOperate=hwdot1qTpFdbSetOperate, hwdot1qTpFdbGroupSetTable=hwdot1qTpFdbGroupSetTable, hwdot1qTpFdbSetPort=hwdot1qTpFdbSetPort, PortList=PortList, hwdot1qMacSearchEntry=hwdot1qMacSearchEntry, hwdot1qMacSearchVlanID=hwdot1qMacSearchVlanID)
