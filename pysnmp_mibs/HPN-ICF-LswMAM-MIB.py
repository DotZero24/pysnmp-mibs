#
# PySNMP MIB module HPN-ICF-LswMAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-LswMAM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfdot1qVlanIndex, = mibBuilder.importSymbols("HPN-ICF-LswVLAN-MIB", "hpnicfdot1qVlanIndex")
hpnicflswCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicflswCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
hpnicfLswMacPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3))
hpnicfLswMacPort.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hpnicfLswMacPort.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hpnicfLswMacPort.setOrganization('')
class InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class PortList(TextualConvention, OctetString):
    status = 'current'

hpnicfdot1qMacSearchTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1), )
if mibBuilder.loadTexts: hpnicfdot1qMacSearchTable.setStatus('current')
hpnicfdot1qMacSearchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1, 1), ).setIndexNames((0, "HPN-ICF-LswMAM-MIB", "hpnicfdot1qMacSearchAddress"), (0, "HPN-ICF-LswMAM-MIB", "hpnicfdot1qMacSearchVlanID"))
if mibBuilder.loadTexts: hpnicfdot1qMacSearchEntry.setStatus('current')
hpnicfdot1qMacSearchAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1qMacSearchAddress.setStatus('current')
hpnicfdot1qMacSearchVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 4096), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1qMacSearchVlanID.setStatus('current')
hpnicfdot1qMacSearchPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1qMacSearchPort.setStatus('current')
hpnicfdot1qMacSearchAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1qMacSearchAgeTime.setStatus('current')
hpnicfdot1qTpFdbSetTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2), )
if mibBuilder.loadTexts: hpnicfdot1qTpFdbSetTable.setStatus('current')
hpnicfdot1qTpFdbSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2, 1), ).setIndexNames((0, "HPN-ICF-LswVLAN-MIB", "hpnicfdot1qVlanIndex"), (0, "HPN-ICF-LswMAM-MIB", "hpnicfdot1qTpFdbSetAddress"))
if mibBuilder.loadTexts: hpnicfdot1qTpFdbSetEntry.setStatus('current')
hpnicfdot1qTpFdbSetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: hpnicfdot1qTpFdbSetAddress.setStatus('current')
hpnicfdot1qTpFdbSetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2, 1, 2), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1qTpFdbSetPort.setStatus('current')
hpnicfdot1qTpFdbSetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 6, 7, 9, 11))).clone(namedValues=NamedValues(("other", 1), ("learned", 3), ("static", 6), ("dynamic", 7), ("blackhole", 9), ("security", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1qTpFdbSetStatus.setStatus('current')
hpnicfdot1qTpFdbSetOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1qTpFdbSetOperate.setStatus('current')
hpnicfdot1qTpFdbGroupSetTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 3), )
if mibBuilder.loadTexts: hpnicfdot1qTpFdbGroupSetTable.setStatus('current')
hpnicfdot1qTpFdbGroupSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 3, 1), ).setIndexNames((0, "HPN-ICF-LswVLAN-MIB", "hpnicfdot1qVlanIndex"), (0, "HPN-ICF-LswMAM-MIB", "hpnicfdot1qTpFdbGroupSetAddress"))
if mibBuilder.loadTexts: hpnicfdot1qTpFdbGroupSetEntry.setStatus('current')
hpnicfdot1qTpFdbGroupSetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 3, 1, 1), MacAddress())
if mibBuilder.loadTexts: hpnicfdot1qTpFdbGroupSetAddress.setStatus('current')
hpnicfdot1qTpFdbGroupSetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 3, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1qTpFdbGroupSetPort.setStatus('current')
hpnicfdot1qTpFdbGroupSetOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1qTpFdbGroupSetOperate.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-LswMAM-MIB", InterfaceIndex=InterfaceIndex, hpnicfdot1qTpFdbSetOperate=hpnicfdot1qTpFdbSetOperate, hpnicfdot1qTpFdbSetStatus=hpnicfdot1qTpFdbSetStatus, hpnicfdot1qTpFdbSetEntry=hpnicfdot1qTpFdbSetEntry, hpnicfdot1qTpFdbGroupSetEntry=hpnicfdot1qTpFdbGroupSetEntry, hpnicfdot1qMacSearchTable=hpnicfdot1qMacSearchTable, hpnicfdot1qMacSearchPort=hpnicfdot1qMacSearchPort, hpnicfdot1qTpFdbSetTable=hpnicfdot1qTpFdbSetTable, hpnicfdot1qTpFdbSetPort=hpnicfdot1qTpFdbSetPort, hpnicfLswMacPort=hpnicfLswMacPort, hpnicfdot1qTpFdbGroupSetOperate=hpnicfdot1qTpFdbGroupSetOperate, hpnicfdot1qMacSearchAddress=hpnicfdot1qMacSearchAddress, hpnicfdot1qMacSearchAgeTime=hpnicfdot1qMacSearchAgeTime, hpnicfdot1qTpFdbGroupSetAddress=hpnicfdot1qTpFdbGroupSetAddress, hpnicfdot1qTpFdbGroupSetTable=hpnicfdot1qTpFdbGroupSetTable, PYSNMP_MODULE_ID=hpnicfLswMacPort, hpnicfdot1qMacSearchVlanID=hpnicfdot1qMacSearchVlanID, PortList=PortList, hpnicfdot1qTpFdbGroupSetPort=hpnicfdot1qTpFdbGroupSetPort, hpnicfdot1qMacSearchEntry=hpnicfdot1qMacSearchEntry, hpnicfdot1qTpFdbSetAddress=hpnicfdot1qTpFdbSetAddress)
