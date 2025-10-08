#
# PySNMP MIB module MARVELL-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/radlan/MARVELL-UDLD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:40:58 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
rndNotifications, rnd = mibBuilder.importSymbols("RADLAN-MIB", "rndNotifications", "rnd")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
class UdldString(SnmpAdminString):
    status = 'current'

class UdldPortBidirectionalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("shutdown", 1), ("idle", 2), ("detection", 3), ("undetermined", 4), ("bidirectional", 5))

class UdldNeighborCurrentState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2), ("undefined", 3), ("bidirectional", 4))

class UdldGlobalMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("aggressive", 2), ("disabled", 3))

class UdldPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("normal", 1), ("aggressive", 2), ("disabled", 3), ("default", 4))

rlUdld = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 218))
rlUdld.setRevisions(('2012-08-01 00:00',))
if mibBuilder.loadTexts: rlUdld.setLastUpdated('201208010000Z')
if mibBuilder.loadTexts: rlUdld.setOrganization('Marvell Computer Communications Ltd.')
rlUdldPortTable = MibTable((1, 3, 6, 1, 4, 1, 89, 218, 1), )
if mibBuilder.loadTexts: rlUdldPortTable.setStatus('current')
rlUdldPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 218, 1, 1), ).setIndexNames((0, "MARVELL-UDLD-MIB", "rlUdldPortIfIndex"))
if mibBuilder.loadTexts: rlUdldPortEntry.setStatus('current')
rlUdldPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 218, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlUdldPortIfIndex.setStatus('current')
rlUdldPortAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 218, 1, 1, 2), UdldPortMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUdldPortAdminMode.setStatus('current')
rlUdldPortOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 218, 1, 1, 3), UdldPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldPortOperMode.setStatus('current')
rlUdldPortDefaultConfiguration = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 218, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldPortDefaultConfiguration.setStatus('current')
rlUdldBidirectionalState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 218, 1, 1, 5), UdldPortBidirectionalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldBidirectionalState.setStatus('current')
rlUdldNumberOfDetectedNeighbors = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 218, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNumberOfDetectedNeighbors.setStatus('current')
rlUdldNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 89, 218, 2), )
if mibBuilder.loadTexts: rlUdldNeighborTable.setStatus('current')
rlUdldNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 218, 2, 1), ).setIndexNames((0, "MARVELL-UDLD-MIB", "rlUdldNeighborPortIfIndex"), (0, "MARVELL-UDLD-MIB", "rlUdldNeighborDeviceID"), (0, "MARVELL-UDLD-MIB", "rlUdldNeighborPortID"))
if mibBuilder.loadTexts: rlUdldNeighborEntry.setStatus('current')
rlUdldNeighborPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 218, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlUdldNeighborPortIfIndex.setStatus('current')
rlUdldNeighborDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 218, 2, 1, 2), UdldString())
if mibBuilder.loadTexts: rlUdldNeighborDeviceID.setStatus('current')
rlUdldNeighborPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 218, 2, 1, 3), UdldString())
if mibBuilder.loadTexts: rlUdldNeighborPortID.setStatus('current')
rlUdldNeighborDeviceMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 218, 2, 1, 4), MacAddress())
if mibBuilder.loadTexts: rlUdldNeighborDeviceMACAddress.setStatus('current')
rlUdldNeighborDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 218, 2, 1, 5), UdldString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborDeviceName.setStatus('current')
rlUdldNeighborMessageTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 218, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborMessageTime.setStatus('current')
rlUdldNeighborLeftLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 218, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborLeftLifeTime.setStatus('current')
rlUdldNeighborCurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 218, 2, 1, 8), UdldNeighborCurrentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborCurrentState.setStatus('current')
rlUdldGlobalUDLDMode = MibScalar((1, 3, 6, 1, 4, 1, 89, 218, 3), UdldGlobalMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUdldGlobalUDLDMode.setStatus('current')
rlUdldGlobalMessageTime = MibScalar((1, 3, 6, 1, 4, 1, 89, 218, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUdldGlobalMessageTime.setStatus('current')
mibBuilder.exportSymbols("MARVELL-UDLD-MIB", rlUdldPortDefaultConfiguration=rlUdldPortDefaultConfiguration, rlUdldPortIfIndex=rlUdldPortIfIndex, UdldPortMode=UdldPortMode, UdldGlobalMode=UdldGlobalMode, rlUdldGlobalUDLDMode=rlUdldGlobalUDLDMode, PYSNMP_MODULE_ID=rlUdld, rlUdldBidirectionalState=rlUdldBidirectionalState, rlUdldNeighborMessageTime=rlUdldNeighborMessageTime, rlUdldNeighborPortIfIndex=rlUdldNeighborPortIfIndex, rlUdldNeighborDeviceName=rlUdldNeighborDeviceName, rlUdldNeighborLeftLifeTime=rlUdldNeighborLeftLifeTime, rlUdldNeighborPortID=rlUdldNeighborPortID, UdldPortBidirectionalState=UdldPortBidirectionalState, rlUdldGlobalMessageTime=rlUdldGlobalMessageTime, rlUdldPortEntry=rlUdldPortEntry, rlUdldNumberOfDetectedNeighbors=rlUdldNumberOfDetectedNeighbors, rlUdldNeighborDeviceMACAddress=rlUdldNeighborDeviceMACAddress, rlUdldNeighborDeviceID=rlUdldNeighborDeviceID, rlUdldNeighborCurrentState=rlUdldNeighborCurrentState, rlUdldPortTable=rlUdldPortTable, rlUdldNeighborEntry=rlUdldNeighborEntry, rlUdld=rlUdld, rlUdldPortAdminMode=rlUdldPortAdminMode, rlUdldPortOperMode=rlUdldPortOperMode, rlUdldNeighborTable=rlUdldNeighborTable, UdldNeighborCurrentState=UdldNeighborCurrentState, UdldString=UdldString)
