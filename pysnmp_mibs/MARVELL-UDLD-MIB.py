_M='rlUdldNeighborPortID'
_L='rlUdldNeighborDeviceID'
_K='rlUdldNeighborPortIfIndex'
_J='rlUdldPortIfIndex'
_I='aggressive'
_H='normal'
_G='bidirectional'
_F='read-write'
_E='disabled'
_D='not-accessible'
_C='MARVELL-UDLD-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
rnd,rndNotifications=mibBuilder.importSymbols('RADLAN-MIB','rnd','rndNotifications')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
rlUdld=ModuleIdentity((1,3,6,1,4,1,89,218))
if mibBuilder.loadTexts:rlUdld.setRevisions(('2012-08-01 00:00',))
class UdldString(SnmpAdminString):status=_A
class UdldPortBidirectionalState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('shutdown',1),('idle',2),('detection',3),('undetermined',4),(_G,5)))
class UdldNeighborCurrentState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('enabled',2),('undefined',3),(_G,4)))
class UdldGlobalMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_E,3)))
class UdldPortMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_I,2),(_E,3),('default',4)))
_RlUdldPortTable_Object=MibTable
rlUdldPortTable=_RlUdldPortTable_Object((1,3,6,1,4,1,89,218,1))
if mibBuilder.loadTexts:rlUdldPortTable.setStatus(_A)
_RlUdldPortEntry_Object=MibTableRow
rlUdldPortEntry=_RlUdldPortEntry_Object((1,3,6,1,4,1,89,218,1,1))
rlUdldPortEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:rlUdldPortEntry.setStatus(_A)
_RlUdldPortIfIndex_Type=InterfaceIndex
_RlUdldPortIfIndex_Object=MibTableColumn
rlUdldPortIfIndex=_RlUdldPortIfIndex_Object((1,3,6,1,4,1,89,218,1,1,1),_RlUdldPortIfIndex_Type())
rlUdldPortIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rlUdldPortIfIndex.setStatus(_A)
_RlUdldPortAdminMode_Type=UdldPortMode
_RlUdldPortAdminMode_Object=MibTableColumn
rlUdldPortAdminMode=_RlUdldPortAdminMode_Object((1,3,6,1,4,1,89,218,1,1,2),_RlUdldPortAdminMode_Type())
rlUdldPortAdminMode.setMaxAccess(_F)
if mibBuilder.loadTexts:rlUdldPortAdminMode.setStatus(_A)
_RlUdldPortOperMode_Type=UdldPortMode
_RlUdldPortOperMode_Object=MibTableColumn
rlUdldPortOperMode=_RlUdldPortOperMode_Object((1,3,6,1,4,1,89,218,1,1,3),_RlUdldPortOperMode_Type())
rlUdldPortOperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rlUdldPortOperMode.setStatus(_A)
_RlUdldPortDefaultConfiguration_Type=TruthValue
_RlUdldPortDefaultConfiguration_Object=MibTableColumn
rlUdldPortDefaultConfiguration=_RlUdldPortDefaultConfiguration_Object((1,3,6,1,4,1,89,218,1,1,4),_RlUdldPortDefaultConfiguration_Type())
rlUdldPortDefaultConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:rlUdldPortDefaultConfiguration.setStatus(_A)
_RlUdldBidirectionalState_Type=UdldPortBidirectionalState
_RlUdldBidirectionalState_Object=MibTableColumn
rlUdldBidirectionalState=_RlUdldBidirectionalState_Object((1,3,6,1,4,1,89,218,1,1,5),_RlUdldBidirectionalState_Type())
rlUdldBidirectionalState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlUdldBidirectionalState.setStatus(_A)
_RlUdldNumberOfDetectedNeighbors_Type=Integer32
_RlUdldNumberOfDetectedNeighbors_Object=MibTableColumn
rlUdldNumberOfDetectedNeighbors=_RlUdldNumberOfDetectedNeighbors_Object((1,3,6,1,4,1,89,218,1,1,6),_RlUdldNumberOfDetectedNeighbors_Type())
rlUdldNumberOfDetectedNeighbors.setMaxAccess(_B)
if mibBuilder.loadTexts:rlUdldNumberOfDetectedNeighbors.setStatus(_A)
_RlUdldNeighborTable_Object=MibTable
rlUdldNeighborTable=_RlUdldNeighborTable_Object((1,3,6,1,4,1,89,218,2))
if mibBuilder.loadTexts:rlUdldNeighborTable.setStatus(_A)
_RlUdldNeighborEntry_Object=MibTableRow
rlUdldNeighborEntry=_RlUdldNeighborEntry_Object((1,3,6,1,4,1,89,218,2,1))
rlUdldNeighborEntry.setIndexNames((0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:rlUdldNeighborEntry.setStatus(_A)
_RlUdldNeighborPortIfIndex_Type=InterfaceIndex
_RlUdldNeighborPortIfIndex_Object=MibTableColumn
rlUdldNeighborPortIfIndex=_RlUdldNeighborPortIfIndex_Object((1,3,6,1,4,1,89,218,2,1,1),_RlUdldNeighborPortIfIndex_Type())
rlUdldNeighborPortIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rlUdldNeighborPortIfIndex.setStatus(_A)
_RlUdldNeighborDeviceID_Type=UdldString
_RlUdldNeighborDeviceID_Object=MibTableColumn
rlUdldNeighborDeviceID=_RlUdldNeighborDeviceID_Object((1,3,6,1,4,1,89,218,2,1,2),_RlUdldNeighborDeviceID_Type())
rlUdldNeighborDeviceID.setMaxAccess(_D)
if mibBuilder.loadTexts:rlUdldNeighborDeviceID.setStatus(_A)
_RlUdldNeighborPortID_Type=UdldString
_RlUdldNeighborPortID_Object=MibTableColumn
rlUdldNeighborPortID=_RlUdldNeighborPortID_Object((1,3,6,1,4,1,89,218,2,1,3),_RlUdldNeighborPortID_Type())
rlUdldNeighborPortID.setMaxAccess(_D)
if mibBuilder.loadTexts:rlUdldNeighborPortID.setStatus(_A)
_RlUdldNeighborDeviceMACAddress_Type=MacAddress
_RlUdldNeighborDeviceMACAddress_Object=MibTableColumn
rlUdldNeighborDeviceMACAddress=_RlUdldNeighborDeviceMACAddress_Object((1,3,6,1,4,1,89,218,2,1,4),_RlUdldNeighborDeviceMACAddress_Type())
rlUdldNeighborDeviceMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:rlUdldNeighborDeviceMACAddress.setStatus(_A)
_RlUdldNeighborDeviceName_Type=UdldString
_RlUdldNeighborDeviceName_Object=MibTableColumn
rlUdldNeighborDeviceName=_RlUdldNeighborDeviceName_Object((1,3,6,1,4,1,89,218,2,1,5),_RlUdldNeighborDeviceName_Type())
rlUdldNeighborDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlUdldNeighborDeviceName.setStatus(_A)
_RlUdldNeighborMessageTime_Type=Integer32
_RlUdldNeighborMessageTime_Object=MibTableColumn
rlUdldNeighborMessageTime=_RlUdldNeighborMessageTime_Object((1,3,6,1,4,1,89,218,2,1,6),_RlUdldNeighborMessageTime_Type())
rlUdldNeighborMessageTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlUdldNeighborMessageTime.setStatus(_A)
_RlUdldNeighborLeftLifeTime_Type=Integer32
_RlUdldNeighborLeftLifeTime_Object=MibTableColumn
rlUdldNeighborLeftLifeTime=_RlUdldNeighborLeftLifeTime_Object((1,3,6,1,4,1,89,218,2,1,7),_RlUdldNeighborLeftLifeTime_Type())
rlUdldNeighborLeftLifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlUdldNeighborLeftLifeTime.setStatus(_A)
_RlUdldNeighborCurrentState_Type=UdldNeighborCurrentState
_RlUdldNeighborCurrentState_Object=MibTableColumn
rlUdldNeighborCurrentState=_RlUdldNeighborCurrentState_Object((1,3,6,1,4,1,89,218,2,1,8),_RlUdldNeighborCurrentState_Type())
rlUdldNeighborCurrentState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlUdldNeighborCurrentState.setStatus(_A)
_RlUdldGlobalUDLDMode_Type=UdldGlobalMode
_RlUdldGlobalUDLDMode_Object=MibScalar
rlUdldGlobalUDLDMode=_RlUdldGlobalUDLDMode_Object((1,3,6,1,4,1,89,218,3),_RlUdldGlobalUDLDMode_Type())
rlUdldGlobalUDLDMode.setMaxAccess(_F)
if mibBuilder.loadTexts:rlUdldGlobalUDLDMode.setStatus(_A)
_RlUdldGlobalMessageTime_Type=Integer32
_RlUdldGlobalMessageTime_Object=MibScalar
rlUdldGlobalMessageTime=_RlUdldGlobalMessageTime_Object((1,3,6,1,4,1,89,218,4),_RlUdldGlobalMessageTime_Type())
rlUdldGlobalMessageTime.setMaxAccess(_F)
if mibBuilder.loadTexts:rlUdldGlobalMessageTime.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'UdldString':UdldString,'UdldPortBidirectionalState':UdldPortBidirectionalState,'UdldNeighborCurrentState':UdldNeighborCurrentState,'UdldGlobalMode':UdldGlobalMode,'UdldPortMode':UdldPortMode,'rlUdld':rlUdld,'rlUdldPortTable':rlUdldPortTable,'rlUdldPortEntry':rlUdldPortEntry,_J:rlUdldPortIfIndex,'rlUdldPortAdminMode':rlUdldPortAdminMode,'rlUdldPortOperMode':rlUdldPortOperMode,'rlUdldPortDefaultConfiguration':rlUdldPortDefaultConfiguration,'rlUdldBidirectionalState':rlUdldBidirectionalState,'rlUdldNumberOfDetectedNeighbors':rlUdldNumberOfDetectedNeighbors,'rlUdldNeighborTable':rlUdldNeighborTable,'rlUdldNeighborEntry':rlUdldNeighborEntry,_K:rlUdldNeighborPortIfIndex,_L:rlUdldNeighborDeviceID,_M:rlUdldNeighborPortID,'rlUdldNeighborDeviceMACAddress':rlUdldNeighborDeviceMACAddress,'rlUdldNeighborDeviceName':rlUdldNeighborDeviceName,'rlUdldNeighborMessageTime':rlUdldNeighborMessageTime,'rlUdldNeighborLeftLifeTime':rlUdldNeighborLeftLifeTime,'rlUdldNeighborCurrentState':rlUdldNeighborCurrentState,'rlUdldGlobalUDLDMode':rlUdldGlobalUDLDMode,'rlUdldGlobalMessageTime':rlUdldGlobalMessageTime})