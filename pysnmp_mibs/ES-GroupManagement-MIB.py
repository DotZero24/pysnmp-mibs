_Z='memStatus'
_Y='memIpAddr'
_X='deviceMac'
_W='tpTrunkId'
_V='tpPortId'
_U='dpTrunkPeerMac'
_T='dpLocalTrunkId'
_S='dpPortPeerMac'
_R='dpLocalPortId'
_Q='dpTrunkId'
_P='dpPortId'
_O='independentSwitch'
_N='commandSwitch'
_M='OctetString'
_L='yes'
_K='memMac'
_J='candidateSwitch'
_I='memberSwitch'
_H='not-accessible'
_G='disable'
_F='enable'
_E='ES-GroupManagement-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
class MacAddress(TextualConvention,OctetString):status=_A
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_EthernetSwitch_ObjectIdentity=ObjectIdentity
ethernetSwitch=_EthernetSwitch_ObjectIdentity((1,3,6,1,4,1,3902,15))
_GroupManagement_ObjectIdentity=ObjectIdentity
groupManagement=_GroupManagement_ObjectIdentity((1,3,6,1,4,1,3902,15,4))
_GroupParam_ObjectIdentity=ObjectIdentity
groupParam=_GroupParam_ObjectIdentity((1,3,6,1,4,1,3902,15,4,1))
class _GmHandtime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_GmHandtime_Type.__name__=_B
_GmHandtime_Object=MibScalar
gmHandtime=_GmHandtime_Object((1,3,6,1,4,1,3902,15,4,1,1),_GmHandtime_Type())
gmHandtime.setMaxAccess(_D)
if mibBuilder.loadTexts:gmHandtime.setStatus(_A)
class _GmHoldtime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_GmHoldtime_Type.__name__=_B
_GmHoldtime_Object=MibScalar
gmHoldtime=_GmHoldtime_Object((1,3,6,1,4,1,3902,15,4,1,2),_GmHoldtime_Type())
gmHoldtime.setMaxAccess(_D)
if mibBuilder.loadTexts:gmHoldtime.setStatus(_A)
class _GmName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_GmName_Type.__name__=_M
_GmName_Object=MibScalar
gmName=_GmName_Object((1,3,6,1,4,1,3902,15,4,1,3),_GmName_Type())
gmName.setMaxAccess(_D)
if mibBuilder.loadTexts:gmName.setStatus(_A)
class _GmSwitchRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_I,2),(_J,3),(_O,4)))
_GmSwitchRole_Type.__name__=_B
_GmSwitchRole_Object=MibScalar
gmSwitchRole=_GmSwitchRole_Object((1,3,6,1,4,1,3902,15,4,1,4),_GmSwitchRole_Type())
gmSwitchRole.setMaxAccess(_D)
if mibBuilder.loadTexts:gmSwitchRole.setStatus(_A)
_GmIpPool_Type=OctetString
_GmIpPool_Object=MibScalar
gmIpPool=_GmIpPool_Object((1,3,6,1,4,1,3902,15,4,1,5),_GmIpPool_Type())
gmIpPool.setMaxAccess(_D)
if mibBuilder.loadTexts:gmIpPool.setStatus(_A)
_TftpServerIpAddr_Type=IpAddress
_TftpServerIpAddr_Object=MibScalar
tftpServerIpAddr=_TftpServerIpAddr_Object((1,3,6,1,4,1,3902,15,4,1,6),_TftpServerIpAddr_Type())
tftpServerIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:tftpServerIpAddr.setStatus(_A)
_BelongedCmdMac_Type=MacAddress
_BelongedCmdMac_Object=MibScalar
belongedCmdMac=_BelongedCmdMac_Object((1,3,6,1,4,1,3902,15,4,1,7),_BelongedCmdMac_Type())
belongedCmdMac.setMaxAccess(_C)
if mibBuilder.loadTexts:belongedCmdMac.setStatus(_A)
_NeighborDiscovery_ObjectIdentity=ObjectIdentity
neighborDiscovery=_NeighborDiscovery_ObjectIdentity((1,3,6,1,4,1,3902,15,4,2))
class _DpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DpAdminStatus_Type.__name__=_B
_DpAdminStatus_Object=MibScalar
dpAdminStatus=_DpAdminStatus_Object((1,3,6,1,4,1,3902,15,4,2,1),_DpAdminStatus_Type())
dpAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dpAdminStatus.setStatus(_A)
class _DpTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,255))
_DpTimer_Type.__name__=_B
_DpTimer_Object=MibScalar
dpTimer=_DpTimer_Object((1,3,6,1,4,1,3902,15,4,2,2),_DpTimer_Type())
dpTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:dpTimer.setStatus(_A)
class _DpHoldtime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,255))
_DpHoldtime_Type.__name__=_B
_DpHoldtime_Object=MibScalar
dpHoldtime=_DpHoldtime_Object((1,3,6,1,4,1,3902,15,4,2,3),_DpHoldtime_Type())
dpHoldtime.setMaxAccess(_D)
if mibBuilder.loadTexts:dpHoldtime.setStatus(_A)
_DpPortTable_Object=MibTable
dpPortTable=_DpPortTable_Object((1,3,6,1,4,1,3902,15,4,2,4))
if mibBuilder.loadTexts:dpPortTable.setStatus(_A)
_DpPortEntry_Object=MibTableRow
dpPortEntry=_DpPortEntry_Object((1,3,6,1,4,1,3902,15,4,2,4,1))
dpPortEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:dpPortEntry.setStatus(_A)
_DpPortId_Type=Integer32
_DpPortId_Object=MibTableColumn
dpPortId=_DpPortId_Object((1,3,6,1,4,1,3902,15,4,2,4,1,1),_DpPortId_Type())
dpPortId.setMaxAccess(_H)
if mibBuilder.loadTexts:dpPortId.setStatus(_A)
class _DpPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DpPortAdminStatus_Type.__name__=_B
_DpPortAdminStatus_Object=MibTableColumn
dpPortAdminStatus=_DpPortAdminStatus_Object((1,3,6,1,4,1,3902,15,4,2,4,1,2),_DpPortAdminStatus_Type())
dpPortAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dpPortAdminStatus.setStatus(_A)
_DpTrunkTable_Object=MibTable
dpTrunkTable=_DpTrunkTable_Object((1,3,6,1,4,1,3902,15,4,2,5))
if mibBuilder.loadTexts:dpTrunkTable.setStatus(_A)
_DpTrunkEntry_Object=MibTableRow
dpTrunkEntry=_DpTrunkEntry_Object((1,3,6,1,4,1,3902,15,4,2,5,1))
dpTrunkEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:dpTrunkEntry.setStatus(_A)
_DpTrunkId_Type=Integer32
_DpTrunkId_Object=MibTableColumn
dpTrunkId=_DpTrunkId_Object((1,3,6,1,4,1,3902,15,4,2,5,1,1),_DpTrunkId_Type())
dpTrunkId.setMaxAccess(_H)
if mibBuilder.loadTexts:dpTrunkId.setStatus(_A)
class _DpTrunkAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DpTrunkAdminStatus_Type.__name__=_B
_DpTrunkAdminStatus_Object=MibTableColumn
dpTrunkAdminStatus=_DpTrunkAdminStatus_Object((1,3,6,1,4,1,3902,15,4,2,5,1,2),_DpTrunkAdminStatus_Type())
dpTrunkAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dpTrunkAdminStatus.setStatus(_A)
_DpDevPortTable_Object=MibTable
dpDevPortTable=_DpDevPortTable_Object((1,3,6,1,4,1,3902,15,4,2,6))
if mibBuilder.loadTexts:dpDevPortTable.setStatus(_A)
_DpDevPortEntry_Object=MibTableRow
dpDevPortEntry=_DpDevPortEntry_Object((1,3,6,1,4,1,3902,15,4,2,6,1))
dpDevPortEntry.setIndexNames((0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:dpDevPortEntry.setStatus(_A)
_DpLocalPortId_Type=Integer32
_DpLocalPortId_Object=MibTableColumn
dpLocalPortId=_DpLocalPortId_Object((1,3,6,1,4,1,3902,15,4,2,6,1,1),_DpLocalPortId_Type())
dpLocalPortId.setMaxAccess(_H)
if mibBuilder.loadTexts:dpLocalPortId.setStatus(_A)
_DpPortPeerMac_Type=MacAddress
_DpPortPeerMac_Object=MibTableColumn
dpPortPeerMac=_DpPortPeerMac_Object((1,3,6,1,4,1,3902,15,4,2,6,1,2),_DpPortPeerMac_Type())
dpPortPeerMac.setMaxAccess(_C)
if mibBuilder.loadTexts:dpPortPeerMac.setStatus(_A)
_DpPortHoldTime_Type=Integer32
_DpPortHoldTime_Object=MibTableColumn
dpPortHoldTime=_DpPortHoldTime_Object((1,3,6,1,4,1,3902,15,4,2,6,1,3),_DpPortHoldTime_Type())
dpPortHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dpPortHoldTime.setStatus(_A)
_DpPortPeerPlatform_Type=OctetString
_DpPortPeerPlatform_Object=MibTableColumn
dpPortPeerPlatform=_DpPortPeerPlatform_Object((1,3,6,1,4,1,3902,15,4,2,6,1,4),_DpPortPeerPlatform_Type())
dpPortPeerPlatform.setMaxAccess(_C)
if mibBuilder.loadTexts:dpPortPeerPlatform.setStatus(_A)
_DpPortPeerPort_Type=OctetString
_DpPortPeerPort_Object=MibTableColumn
dpPortPeerPort=_DpPortPeerPort_Object((1,3,6,1,4,1,3902,15,4,2,6,1,5),_DpPortPeerPort_Type())
dpPortPeerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dpPortPeerPort.setStatus(_A)
_DpDevTrunkTable_Object=MibTable
dpDevTrunkTable=_DpDevTrunkTable_Object((1,3,6,1,4,1,3902,15,4,2,7))
if mibBuilder.loadTexts:dpDevTrunkTable.setStatus(_A)
_DpDevTrunkEntry_Object=MibTableRow
dpDevTrunkEntry=_DpDevTrunkEntry_Object((1,3,6,1,4,1,3902,15,4,2,7,1))
dpDevTrunkEntry.setIndexNames((0,_E,_T),(0,_E,_U))
if mibBuilder.loadTexts:dpDevTrunkEntry.setStatus(_A)
_DpLocalTrunkId_Type=Integer32
_DpLocalTrunkId_Object=MibTableColumn
dpLocalTrunkId=_DpLocalTrunkId_Object((1,3,6,1,4,1,3902,15,4,2,7,1,1),_DpLocalTrunkId_Type())
dpLocalTrunkId.setMaxAccess(_H)
if mibBuilder.loadTexts:dpLocalTrunkId.setStatus(_A)
_DpTrunkPeerMac_Type=MacAddress
_DpTrunkPeerMac_Object=MibTableColumn
dpTrunkPeerMac=_DpTrunkPeerMac_Object((1,3,6,1,4,1,3902,15,4,2,7,1,2),_DpTrunkPeerMac_Type())
dpTrunkPeerMac.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTrunkPeerMac.setStatus(_A)
_DpTrunkHoldTime_Type=Integer32
_DpTrunkHoldTime_Object=MibTableColumn
dpTrunkHoldTime=_DpTrunkHoldTime_Object((1,3,6,1,4,1,3902,15,4,2,7,1,3),_DpTrunkHoldTime_Type())
dpTrunkHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTrunkHoldTime.setStatus(_A)
_DpTrunkPeerPlatform_Type=OctetString
_DpTrunkPeerPlatform_Object=MibTableColumn
dpTrunkPeerPlatform=_DpTrunkPeerPlatform_Object((1,3,6,1,4,1,3902,15,4,2,7,1,4),_DpTrunkPeerPlatform_Type())
dpTrunkPeerPlatform.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTrunkPeerPlatform.setStatus(_A)
_DpTrunkPeerTrunk_Type=OctetString
_DpTrunkPeerTrunk_Object=MibTableColumn
dpTrunkPeerTrunk=_DpTrunkPeerTrunk_Object((1,3,6,1,4,1,3902,15,4,2,7,1,5),_DpTrunkPeerTrunk_Type())
dpTrunkPeerTrunk.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTrunkPeerTrunk.setStatus(_A)
_TopologyCollect_ObjectIdentity=ObjectIdentity
topologyCollect=_TopologyCollect_ObjectIdentity((1,3,6,1,4,1,3902,15,4,3))
class _TpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TpAdminStatus_Type.__name__=_B
_TpAdminStatus_Object=MibScalar
tpAdminStatus=_TpAdminStatus_Object((1,3,6,1,4,1,3902,15,4,3,1),_TpAdminStatus_Type())
tpAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tpAdminStatus.setStatus(_A)
class _TpVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_TpVlan_Type.__name__=_B
_TpVlan_Object=MibScalar
tpVlan=_TpVlan_Object((1,3,6,1,4,1,3902,15,4,3,2),_TpVlan_Type())
tpVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:tpVlan.setStatus(_A)
class _TpHop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_TpHop_Type.__name__=_B
_TpHop_Object=MibScalar
tpHop=_TpHop_Object((1,3,6,1,4,1,3902,15,4,3,3),_TpHop_Type())
tpHop.setMaxAccess(_D)
if mibBuilder.loadTexts:tpHop.setStatus(_A)
class _TpTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_TpTimer_Type.__name__=_B
_TpTimer_Object=MibScalar
tpTimer=_TpTimer_Object((1,3,6,1,4,1,3902,15,4,3,4),_TpTimer_Type())
tpTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:tpTimer.setStatus(_A)
class _TpHopDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_TpHopDelay_Type.__name__=_B
_TpHopDelay_Object=MibScalar
tpHopDelay=_TpHopDelay_Object((1,3,6,1,4,1,3902,15,4,3,5),_TpHopDelay_Type())
tpHopDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:tpHopDelay.setStatus(_A)
class _TpPortDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_TpPortDelay_Type.__name__=_B
_TpPortDelay_Object=MibScalar
tpPortDelay=_TpPortDelay_Object((1,3,6,1,4,1,3902,15,4,3,6),_TpPortDelay_Type())
tpPortDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPortDelay.setStatus(_A)
class _TpStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('start',1))
_TpStart_Type.__name__=_B
_TpStart_Object=MibScalar
tpStart=_TpStart_Object((1,3,6,1,4,1,3902,15,4,3,7),_TpStart_Type())
tpStart.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStart.setStatus(_A)
_TpPortTable_Object=MibTable
tpPortTable=_TpPortTable_Object((1,3,6,1,4,1,3902,15,4,3,8))
if mibBuilder.loadTexts:tpPortTable.setStatus(_A)
_TpPortEntry_Object=MibTableRow
tpPortEntry=_TpPortEntry_Object((1,3,6,1,4,1,3902,15,4,3,8,1))
tpPortEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:tpPortEntry.setStatus(_A)
_TpPortId_Type=Integer32
_TpPortId_Object=MibTableColumn
tpPortId=_TpPortId_Object((1,3,6,1,4,1,3902,15,4,3,8,1,1),_TpPortId_Type())
tpPortId.setMaxAccess(_H)
if mibBuilder.loadTexts:tpPortId.setStatus(_A)
class _TpPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TpPortAdminStatus_Type.__name__=_B
_TpPortAdminStatus_Object=MibTableColumn
tpPortAdminStatus=_TpPortAdminStatus_Object((1,3,6,1,4,1,3902,15,4,3,8,1,2),_TpPortAdminStatus_Type())
tpPortAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPortAdminStatus.setStatus(_A)
_TpTrunkTable_Object=MibTable
tpTrunkTable=_TpTrunkTable_Object((1,3,6,1,4,1,3902,15,4,3,9))
if mibBuilder.loadTexts:tpTrunkTable.setStatus(_A)
_TpTrunkEntry_Object=MibTableRow
tpTrunkEntry=_TpTrunkEntry_Object((1,3,6,1,4,1,3902,15,4,3,9,1))
tpTrunkEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:tpTrunkEntry.setStatus(_A)
_TpTrunkId_Type=Integer32
_TpTrunkId_Object=MibTableColumn
tpTrunkId=_TpTrunkId_Object((1,3,6,1,4,1,3902,15,4,3,9,1,1),_TpTrunkId_Type())
tpTrunkId.setMaxAccess(_H)
if mibBuilder.loadTexts:tpTrunkId.setStatus(_A)
class _TpTrunkAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TpTrunkAdminStatus_Type.__name__=_B
_TpTrunkAdminStatus_Object=MibTableColumn
tpTrunkAdminStatus=_TpTrunkAdminStatus_Object((1,3,6,1,4,1,3902,15,4,3,9,1,2),_TpTrunkAdminStatus_Type())
tpTrunkAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tpTrunkAdminStatus.setStatus(_A)
_TpDeviceTable_Object=MibTable
tpDeviceTable=_TpDeviceTable_Object((1,3,6,1,4,1,3902,15,4,3,10))
if mibBuilder.loadTexts:tpDeviceTable.setStatus(_A)
_TpDeviceEntry_Object=MibTableRow
tpDeviceEntry=_TpDeviceEntry_Object((1,3,6,1,4,1,3902,15,4,3,10,1))
tpDeviceEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:tpDeviceEntry.setStatus(_A)
_DeviceMac_Type=MacAddress
_DeviceMac_Object=MibTableColumn
deviceMac=_DeviceMac_Object((1,3,6,1,4,1,3902,15,4,3,10,1,1),_DeviceMac_Type())
deviceMac.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceMac.setStatus(_A)
class _DeviceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_DeviceId_Type.__name__=_B
_DeviceId_Object=MibTableColumn
deviceId=_DeviceId_Object((1,3,6,1,4,1,3902,15,4,3,10,1,2),_DeviceId_Type())
deviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceId.setStatus(_A)
_DeviceIpAddr_Type=IpAddress
_DeviceIpAddr_Object=MibTableColumn
deviceIpAddr=_DeviceIpAddr_Object((1,3,6,1,4,1,3902,15,4,3,10,1,3),_DeviceIpAddr_Type())
deviceIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceIpAddr.setStatus(_A)
_DeviceHop_Type=Integer32
_DeviceHop_Object=MibTableColumn
deviceHop=_DeviceHop_Object((1,3,6,1,4,1,3902,15,4,3,10,1,4),_DeviceHop_Type())
deviceHop.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceHop.setStatus(_A)
_DevicePlatform_Type=OctetString
_DevicePlatform_Object=MibTableColumn
devicePlatform=_DevicePlatform_Object((1,3,6,1,4,1,3902,15,4,3,10,1,5),_DevicePlatform_Type())
devicePlatform.setMaxAccess(_C)
if mibBuilder.loadTexts:devicePlatform.setStatus(_A)
class _DeviceRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_I,2),(_J,3),(_O,4)))
_DeviceRole_Type.__name__=_B
_DeviceRole_Object=MibTableColumn
deviceRole=_DeviceRole_Object((1,3,6,1,4,1,3902,15,4,3,10,1,6),_DeviceRole_Type())
deviceRole.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceRole.setStatus(_A)
_DevicePeerPort_Type=OctetString
_DevicePeerPort_Object=MibTableColumn
devicePeerPort=_DevicePeerPort_Object((1,3,6,1,4,1,3902,15,4,3,10,1,7),_DevicePeerPort_Type())
devicePeerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:devicePeerPort.setStatus(_A)
_DeviceBelongedMac_Type=MacAddress
_DeviceBelongedMac_Object=MibTableColumn
deviceBelongedMac=_DeviceBelongedMac_Object((1,3,6,1,4,1,3902,15,4,3,10,1,8),_DeviceBelongedMac_Type())
deviceBelongedMac.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceBelongedMac.setStatus(_A)
_DeviceBelongedIpAddr_Type=IpAddress
_DeviceBelongedIpAddr_Object=MibTableColumn
deviceBelongedIpAddr=_DeviceBelongedIpAddr_Object((1,3,6,1,4,1,3902,15,4,3,10,1,9),_DeviceBelongedIpAddr_Type())
deviceBelongedIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceBelongedIpAddr.setStatus(_A)
_MemberManage_ObjectIdentity=ObjectIdentity
memberManage=_MemberManage_ObjectIdentity((1,3,6,1,4,1,3902,15,4,4))
_MemberTable_Object=MibTable
memberTable=_MemberTable_Object((1,3,6,1,4,1,3902,15,4,4,1))
if mibBuilder.loadTexts:memberTable.setStatus(_A)
_MemberEntry_Object=MibTableRow
memberEntry=_MemberEntry_Object((1,3,6,1,4,1,3902,15,4,4,1,1))
memberEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:memberEntry.setStatus(_A)
_MemMac_Type=MacAddress
_MemMac_Object=MibTableColumn
memMac=_MemMac_Object((1,3,6,1,4,1,3902,15,4,4,1,1,1),_MemMac_Type())
memMac.setMaxAccess(_C)
if mibBuilder.loadTexts:memMac.setStatus(_A)
_MemId_Type=Integer32
_MemId_Object=MibTableColumn
memId=_MemId_Object((1,3,6,1,4,1,3902,15,4,4,1,1,2),_MemId_Type())
memId.setMaxAccess(_C)
if mibBuilder.loadTexts:memId.setStatus(_A)
_MemIpAddr_Type=IpAddress
_MemIpAddr_Object=MibTableColumn
memIpAddr=_MemIpAddr_Object((1,3,6,1,4,1,3902,15,4,4,1,1,3),_MemIpAddr_Type())
memIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:memIpAddr.setStatus(_A)
_MemMask_Type=IpAddress
_MemMask_Object=MibTableColumn
memMask=_MemMask_Object((1,3,6,1,4,1,3902,15,4,4,1,1,4),_MemMask_Type())
memMask.setMaxAccess(_C)
if mibBuilder.loadTexts:memMask.setStatus(_A)
class _MemStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_MemStatus_Type.__name__=_B
_MemStatus_Object=MibTableColumn
memStatus=_MemStatus_Object((1,3,6,1,4,1,3902,15,4,4,1,1,5),_MemStatus_Type())
memStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:memStatus.setStatus(_A)
class _MemRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_MemRole_Type.__name__=_B
_MemRole_Object=MibTableColumn
memRole=_MemRole_Object((1,3,6,1,4,1,3902,15,4,4,1,1,6),_MemRole_Type())
memRole.setMaxAccess(_D)
if mibBuilder.loadTexts:memRole.setStatus(_A)
_SnmpPortMap_Type=Unsigned32
_SnmpPortMap_Object=MibTableColumn
snmpPortMap=_SnmpPortMap_Object((1,3,6,1,4,1,3902,15,4,4,1,1,7),_SnmpPortMap_Type())
snmpPortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpPortMap.setStatus(_A)
class _HttpPortMap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_HttpPortMap_Type.__name__=_B
_HttpPortMap_Object=MibTableColumn
httpPortMap=_HttpPortMap_Object((1,3,6,1,4,1,3902,15,4,4,1,1,8),_HttpPortMap_Type())
httpPortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:httpPortMap.setStatus(_A)
class _FtpPortMap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_FtpPortMap_Type.__name__=_B
_FtpPortMap_Object=MibTableColumn
ftpPortMap=_FtpPortMap_Object((1,3,6,1,4,1,3902,15,4,4,1,1,9),_FtpPortMap_Type())
ftpPortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:ftpPortMap.setStatus(_A)
class _TftpPortMap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_TftpPortMap_Type.__name__=_B
_TftpPortMap_Object=MibTableColumn
tftpPortMap=_TftpPortMap_Object((1,3,6,1,4,1,3902,15,4,4,1,1,10),_TftpPortMap_Type())
tftpPortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:tftpPortMap.setStatus(_A)
_TelnetPortMap_Type=Integer32
_TelnetPortMap_Object=MibTableColumn
telnetPortMap=_TelnetPortMap_Object((1,3,6,1,4,1,3902,15,4,4,1,1,11),_TelnetPortMap_Type())
telnetPortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:telnetPortMap.setStatus(_A)
_SshPortMap_Type=Integer32
_SshPortMap_Object=MibTableColumn
sshPortMap=_SshPortMap_Object((1,3,6,1,4,1,3902,15,4,4,1,1,12),_SshPortMap_Type())
sshPortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:sshPortMap.setStatus(_A)
class _MemSaveConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('no',2)))
_MemSaveConfig_Type.__name__=_B
_MemSaveConfig_Object=MibTableColumn
memSaveConfig=_MemSaveConfig_Object((1,3,6,1,4,1,3902,15,4,4,1,1,13),_MemSaveConfig_Type())
memSaveConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:memSaveConfig.setStatus(_A)
class _MemEraseConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('no',2)))
_MemEraseConfig_Type.__name__=_B
_MemEraseConfig_Object=MibTableColumn
memEraseConfig=_MemEraseConfig_Object((1,3,6,1,4,1,3902,15,4,4,1,1,14),_MemEraseConfig_Type())
memEraseConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:memEraseConfig.setStatus(_A)
class _MemReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('no',2)))
_MemReboot_Type.__name__=_B
_MemReboot_Object=MibTableColumn
memReboot=_MemReboot_Object((1,3,6,1,4,1,3902,15,4,4,1,1,15),_MemReboot_Type())
memReboot.setMaxAccess(_D)
if mibBuilder.loadTexts:memReboot.setStatus(_A)
_GmEnterpriseTrap_ObjectIdentity=ObjectIdentity
gmEnterpriseTrap=_GmEnterpriseTrap_ObjectIdentity((1,3,6,1,4,1,3902,15,4,5))
gmTopologyChange=NotificationType((1,3,6,1,4,1,3902,15,4,5,1))
if mibBuilder.loadTexts:gmTopologyChange.setStatus(_A)
gmMemberUpDown=NotificationType((1,3,6,1,4,1,3902,15,4,5,2))
gmMemberUpDown.setObjects(*((_E,_K),(_E,'memId'),(_E,_Y),(_E,_Z)))
if mibBuilder.loadTexts:gmMemberUpDown.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'MacAddress':MacAddress,'zte':zte,'ethernetSwitch':ethernetSwitch,'groupManagement':groupManagement,'groupParam':groupParam,'gmHandtime':gmHandtime,'gmHoldtime':gmHoldtime,'gmName':gmName,'gmSwitchRole':gmSwitchRole,'gmIpPool':gmIpPool,'tftpServerIpAddr':tftpServerIpAddr,'belongedCmdMac':belongedCmdMac,'neighborDiscovery':neighborDiscovery,'dpAdminStatus':dpAdminStatus,'dpTimer':dpTimer,'dpHoldtime':dpHoldtime,'dpPortTable':dpPortTable,'dpPortEntry':dpPortEntry,_P:dpPortId,'dpPortAdminStatus':dpPortAdminStatus,'dpTrunkTable':dpTrunkTable,'dpTrunkEntry':dpTrunkEntry,_Q:dpTrunkId,'dpTrunkAdminStatus':dpTrunkAdminStatus,'dpDevPortTable':dpDevPortTable,'dpDevPortEntry':dpDevPortEntry,_R:dpLocalPortId,_S:dpPortPeerMac,'dpPortHoldTime':dpPortHoldTime,'dpPortPeerPlatform':dpPortPeerPlatform,'dpPortPeerPort':dpPortPeerPort,'dpDevTrunkTable':dpDevTrunkTable,'dpDevTrunkEntry':dpDevTrunkEntry,_T:dpLocalTrunkId,_U:dpTrunkPeerMac,'dpTrunkHoldTime':dpTrunkHoldTime,'dpTrunkPeerPlatform':dpTrunkPeerPlatform,'dpTrunkPeerTrunk':dpTrunkPeerTrunk,'topologyCollect':topologyCollect,'tpAdminStatus':tpAdminStatus,'tpVlan':tpVlan,'tpHop':tpHop,'tpTimer':tpTimer,'tpHopDelay':tpHopDelay,'tpPortDelay':tpPortDelay,'tpStart':tpStart,'tpPortTable':tpPortTable,'tpPortEntry':tpPortEntry,_V:tpPortId,'tpPortAdminStatus':tpPortAdminStatus,'tpTrunkTable':tpTrunkTable,'tpTrunkEntry':tpTrunkEntry,_W:tpTrunkId,'tpTrunkAdminStatus':tpTrunkAdminStatus,'tpDeviceTable':tpDeviceTable,'tpDeviceEntry':tpDeviceEntry,_X:deviceMac,'deviceId':deviceId,'deviceIpAddr':deviceIpAddr,'deviceHop':deviceHop,'devicePlatform':devicePlatform,'deviceRole':deviceRole,'devicePeerPort':devicePeerPort,'deviceBelongedMac':deviceBelongedMac,'deviceBelongedIpAddr':deviceBelongedIpAddr,'memberManage':memberManage,'memberTable':memberTable,'memberEntry':memberEntry,_K:memMac,'memId':memId,_Y:memIpAddr,'memMask':memMask,_Z:memStatus,'memRole':memRole,'snmpPortMap':snmpPortMap,'httpPortMap':httpPortMap,'ftpPortMap':ftpPortMap,'tftpPortMap':tftpPortMap,'telnetPortMap':telnetPortMap,'sshPortMap':sshPortMap,'memSaveConfig':memSaveConfig,'memEraseConfig':memEraseConfig,'memReboot':memReboot,'gmEnterpriseTrap':gmEnterpriseTrap,'gmTopologyChange':gmTopologyChange,'gmMemberUpDown':gmMemberUpDown})