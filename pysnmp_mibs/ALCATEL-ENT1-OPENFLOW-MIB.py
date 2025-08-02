_A4='alaOpenflowModuleInterfaceVlanGroup'
_A3='alaOpenflowModuleInterfaceGroup'
_A2='alaOpenflowModuleControllerGroup'
_A1='alaOpenflowModuleLogicalSwitchGroup'
_A0='alaOpenflowModuleConfigGroup'
_z='alaOpenflowInterfaceVlanRowStatus'
_y='alaOpenflowInterfaceNativeVlan'
_x='alaOpenflowInterfaceType'
_w='alaOpenflowInterfaceRowStatus'
_v='alaOpenflowInterfaceMode'
_u='alaOpenflowControllerPriority'
_t='alaOpenflowControllerRowStatus'
_s='alaOpenflowControllerOperState'
_r='alaOpenflowControllerAdminState'
_q='alaOpenflowControllerRole'
_p='alaOpenflowLogicalSwitchTCPBufferSizeRx'
_o='alaOpenflowLogicalSwitchTCPBufferSizeTx'
_n='alaOpenflowLogicalSwitchTableMissAction'
_m='alaOpenflowLogicalSwitchDPID'
_l='alaOpenflowLogicalSwitchFailureDetectTime'
_k='alaOpenflowLogicalSwitchProbeTime'
_j='alaOpenflowLogicalSwitchLearnedMacUpdate'
_i='alaOpenflowLogicalSwitchRowStatus'
_h='alaOpenflowLogicalSwitchFlowCount'
_g='alaOpenflowLogicalSwitchInterfaceCount'
_f='alaOpenflowLogicalSwitchControllerCount'
_e='alaOpenflowLogicalSwitchVlan'
_d='alaOpenflowLogicalSwitchVersions'
_c='alaOpenflowLogicalSwitchMode'
_b='alaOpenflowLogicalSwitchAdminState'
_a='alaOpenflowGlobalIdleProbeTimeout'
_Z='alaOpenflowGlobalBackoffMax'
_Y='alaOpenflowInterfaceVlanVlanID'
_X='alaOpenflowControllerPort'
_W='alaOpenflowControllerIp'
_V='alaOpenflowControllerIpType'
_U='alaOpenflowControllerLogicalSwitch'
_T='Kilo Bytes'
_S='pfcChannel'
_R='normal'
_Q='alaOpenflowLogicalSwitch'
_P='read-write'
_O='InetAddressType'
_N='InetAddress'
_M='OctetString'
_L='alaOpenflowInterface'
_K='alaOpenflowInterfaceLogicalSwitch'
_J='enabled'
_I='disabled'
_H='SnmpAdminString'
_G='Unsigned32'
_F='read-only'
_E='not-accessible'
_D='read-create'
_C='Integer32'
_B='ALCATEL-ENT1-OPENFLOW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1OpenflowMIB,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1OpenflowMIB')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_N,_O)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1OpenflowMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,77,1))
if mibBuilder.loadTexts:alcatelIND1OpenflowMIB.setRevisions(('2014-03-26 00:00','2014-10-08 00:00'))
_AlcatelIND1OpenflowMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1OpenflowMIBNotifications=_AlcatelIND1OpenflowMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,77,1,0))
_AlcatelIND1OpenflowMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1OpenflowMIBObjects=_AlcatelIND1OpenflowMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,77,1,1))
if mibBuilder.loadTexts:alcatelIND1OpenflowMIBObjects.setStatus(_A)
_AlaOpenflowGlobalConfigObjects_ObjectIdentity=ObjectIdentity
alaOpenflowGlobalConfigObjects=_AlaOpenflowGlobalConfigObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,1))
class _AlaOpenflowGlobalBackoffMax_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_AlaOpenflowGlobalBackoffMax_Type.__name__=_C
_AlaOpenflowGlobalBackoffMax_Object=MibScalar
alaOpenflowGlobalBackoffMax=_AlaOpenflowGlobalBackoffMax_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,1,1),_AlaOpenflowGlobalBackoffMax_Type())
alaOpenflowGlobalBackoffMax.setMaxAccess(_P)
if mibBuilder.loadTexts:alaOpenflowGlobalBackoffMax.setStatus(_A)
class _AlaOpenflowGlobalIdleProbeTimeout_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_AlaOpenflowGlobalIdleProbeTimeout_Type.__name__=_C
_AlaOpenflowGlobalIdleProbeTimeout_Object=MibScalar
alaOpenflowGlobalIdleProbeTimeout=_AlaOpenflowGlobalIdleProbeTimeout_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,1,2),_AlaOpenflowGlobalIdleProbeTimeout_Type())
alaOpenflowGlobalIdleProbeTimeout.setMaxAccess(_P)
if mibBuilder.loadTexts:alaOpenflowGlobalIdleProbeTimeout.setStatus(_A)
_AlaOpenflowLogicalSwitchTable_Object=MibTable
alaOpenflowLogicalSwitchTable=_AlaOpenflowLogicalSwitchTable_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2))
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchTable.setStatus(_A)
_AlaOpenflowLogicalSwitchEntry_Object=MibTableRow
alaOpenflowLogicalSwitchEntry=_AlaOpenflowLogicalSwitchEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1))
alaOpenflowLogicalSwitchEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchEntry.setStatus(_A)
class _AlaOpenflowLogicalSwitch_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AlaOpenflowLogicalSwitch_Type.__name__=_H
_AlaOpenflowLogicalSwitch_Object=MibTableColumn
alaOpenflowLogicalSwitch=_AlaOpenflowLogicalSwitch_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1,1),_AlaOpenflowLogicalSwitch_Type())
alaOpenflowLogicalSwitch.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitch.setStatus(_A)
class _AlaOpenflowLogicalSwitchAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_AlaOpenflowLogicalSwitchAdminState_Type.__name__=_C
_AlaOpenflowLogicalSwitchAdminState_Object=MibTableColumn
alaOpenflowLogicalSwitchAdminState=_AlaOpenflowLogicalSwitchAdminState_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1,2),_AlaOpenflowLogicalSwitchAdminState_Type())
alaOpenflowLogicalSwitchAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchAdminState.setStatus(_A)
class _AlaOpenflowLogicalSwitchMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('api',2),(_S,3)))
_AlaOpenflowLogicalSwitchMode_Type.__name__=_C
_AlaOpenflowLogicalSwitchMode_Object=MibTableColumn
alaOpenflowLogicalSwitchMode=_AlaOpenflowLogicalSwitchMode_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1,3),_AlaOpenflowLogicalSwitchMode_Type())
alaOpenflowLogicalSwitchMode.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchMode.setStatus(_A)
class _AlaOpenflowLogicalSwitchVersions_Type(Bits):defaultBinValue='11';namedValues=NamedValues(*(('v1dot0',0),('v1dot3dot1',1)))
_AlaOpenflowLogicalSwitchVersions_Type.__name__='Bits'
_AlaOpenflowLogicalSwitchVersions_Object=MibTableColumn
alaOpenflowLogicalSwitchVersions=_AlaOpenflowLogicalSwitchVersions_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1,4),_AlaOpenflowLogicalSwitchVersions_Type())
alaOpenflowLogicalSwitchVersions.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchVersions.setStatus(_A)
class _AlaOpenflowLogicalSwitchVlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,4093))
_AlaOpenflowLogicalSwitchVlan_Type.__name__=_C
_AlaOpenflowLogicalSwitchVlan_Object=MibTableColumn
alaOpenflowLogicalSwitchVlan=_AlaOpenflowLogicalSwitchVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1,5),_AlaOpenflowLogicalSwitchVlan_Type())
alaOpenflowLogicalSwitchVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchVlan.setStatus(_A)
class _AlaOpenflowLogicalSwitchControllerCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AlaOpenflowLogicalSwitchControllerCount_Type.__name__=_C
_AlaOpenflowLogicalSwitchControllerCount_Object=MibTableColumn
alaOpenflowLogicalSwitchControllerCount=_AlaOpenflowLogicalSwitchControllerCount_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1,6),_AlaOpenflowLogicalSwitchControllerCount_Type())
alaOpenflowLogicalSwitchControllerCount.setMaxAccess(_F)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchControllerCount.setStatus(_A)
class _AlaOpenflowLogicalSwitchInterfaceCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_AlaOpenflowLogicalSwitchInterfaceCount_Type.__name__=_C
_AlaOpenflowLogicalSwitchInterfaceCount_Object=MibTableColumn
alaOpenflowLogicalSwitchInterfaceCount=_AlaOpenflowLogicalSwitchInterfaceCount_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1,7),_AlaOpenflowLogicalSwitchInterfaceCount_Type())
alaOpenflowLogicalSwitchInterfaceCount.setMaxAccess(_F)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchInterfaceCount.setStatus(_A)
class _AlaOpenflowLogicalSwitchFlowCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,511))
_AlaOpenflowLogicalSwitchFlowCount_Type.__name__=_C
_AlaOpenflowLogicalSwitchFlowCount_Object=MibTableColumn
alaOpenflowLogicalSwitchFlowCount=_AlaOpenflowLogicalSwitchFlowCount_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1,8),_AlaOpenflowLogicalSwitchFlowCount_Type())
alaOpenflowLogicalSwitchFlowCount.setMaxAccess(_F)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchFlowCount.setStatus(_A)
_AlaOpenflowLogicalSwitchRowStatus_Type=RowStatus
_AlaOpenflowLogicalSwitchRowStatus_Object=MibTableColumn
alaOpenflowLogicalSwitchRowStatus=_AlaOpenflowLogicalSwitchRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1,9),_AlaOpenflowLogicalSwitchRowStatus_Type())
alaOpenflowLogicalSwitchRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchRowStatus.setStatus(_A)
class _AlaOpenflowLogicalSwitchLearnedMacUpdate_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_AlaOpenflowLogicalSwitchLearnedMacUpdate_Type.__name__=_C
_AlaOpenflowLogicalSwitchLearnedMacUpdate_Object=MibTableColumn
alaOpenflowLogicalSwitchLearnedMacUpdate=_AlaOpenflowLogicalSwitchLearnedMacUpdate_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1,10),_AlaOpenflowLogicalSwitchLearnedMacUpdate_Type())
alaOpenflowLogicalSwitchLearnedMacUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchLearnedMacUpdate.setStatus(_A)
class _AlaOpenflowLogicalSwitchProbeTime_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_AlaOpenflowLogicalSwitchProbeTime_Type.__name__=_C
_AlaOpenflowLogicalSwitchProbeTime_Object=MibTableColumn
alaOpenflowLogicalSwitchProbeTime=_AlaOpenflowLogicalSwitchProbeTime_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1,11),_AlaOpenflowLogicalSwitchProbeTime_Type())
alaOpenflowLogicalSwitchProbeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchProbeTime.setStatus(_A)
class _AlaOpenflowLogicalSwitchFailureDetectTime_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_AlaOpenflowLogicalSwitchFailureDetectTime_Type.__name__=_C
_AlaOpenflowLogicalSwitchFailureDetectTime_Object=MibTableColumn
alaOpenflowLogicalSwitchFailureDetectTime=_AlaOpenflowLogicalSwitchFailureDetectTime_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1,12),_AlaOpenflowLogicalSwitchFailureDetectTime_Type())
alaOpenflowLogicalSwitchFailureDetectTime.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchFailureDetectTime.setStatus(_A)
class _AlaOpenflowLogicalSwitchDPID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_AlaOpenflowLogicalSwitchDPID_Type.__name__=_M
_AlaOpenflowLogicalSwitchDPID_Object=MibTableColumn
alaOpenflowLogicalSwitchDPID=_AlaOpenflowLogicalSwitchDPID_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1,13),_AlaOpenflowLogicalSwitchDPID_Type())
alaOpenflowLogicalSwitchDPID.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchDPID.setStatus(_A)
class _AlaOpenflowLogicalSwitchTableMissAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('drop',1),('controller',2)))
_AlaOpenflowLogicalSwitchTableMissAction_Type.__name__=_C
_AlaOpenflowLogicalSwitchTableMissAction_Object=MibTableColumn
alaOpenflowLogicalSwitchTableMissAction=_AlaOpenflowLogicalSwitchTableMissAction_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1,14),_AlaOpenflowLogicalSwitchTableMissAction_Type())
alaOpenflowLogicalSwitchTableMissAction.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchTableMissAction.setStatus(_A)
class _AlaOpenflowLogicalSwitchTCPBufferSizeTx_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,32))
_AlaOpenflowLogicalSwitchTCPBufferSizeTx_Type.__name__=_G
_AlaOpenflowLogicalSwitchTCPBufferSizeTx_Object=MibTableColumn
alaOpenflowLogicalSwitchTCPBufferSizeTx=_AlaOpenflowLogicalSwitchTCPBufferSizeTx_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1,15),_AlaOpenflowLogicalSwitchTCPBufferSizeTx_Type())
alaOpenflowLogicalSwitchTCPBufferSizeTx.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchTCPBufferSizeTx.setStatus(_A)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchTCPBufferSizeTx.setUnits(_T)
class _AlaOpenflowLogicalSwitchTCPBufferSizeRx_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,32))
_AlaOpenflowLogicalSwitchTCPBufferSizeRx_Type.__name__=_G
_AlaOpenflowLogicalSwitchTCPBufferSizeRx_Object=MibTableColumn
alaOpenflowLogicalSwitchTCPBufferSizeRx=_AlaOpenflowLogicalSwitchTCPBufferSizeRx_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,2,1,16),_AlaOpenflowLogicalSwitchTCPBufferSizeRx_Type())
alaOpenflowLogicalSwitchTCPBufferSizeRx.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchTCPBufferSizeRx.setStatus(_A)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchTCPBufferSizeRx.setUnits(_T)
_AlaOpenflowControllerTable_Object=MibTable
alaOpenflowControllerTable=_AlaOpenflowControllerTable_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,3))
if mibBuilder.loadTexts:alaOpenflowControllerTable.setStatus(_A)
_AlaOpenflowControllerEntry_Object=MibTableRow
alaOpenflowControllerEntry=_AlaOpenflowControllerEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,3,1))
alaOpenflowControllerEntry.setIndexNames((0,_B,_U),(0,_B,_V),(0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:alaOpenflowControllerEntry.setStatus(_A)
class _AlaOpenflowControllerLogicalSwitch_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AlaOpenflowControllerLogicalSwitch_Type.__name__=_H
_AlaOpenflowControllerLogicalSwitch_Object=MibTableColumn
alaOpenflowControllerLogicalSwitch=_AlaOpenflowControllerLogicalSwitch_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,3,1,1),_AlaOpenflowControllerLogicalSwitch_Type())
alaOpenflowControllerLogicalSwitch.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOpenflowControllerLogicalSwitch.setStatus(_A)
class _AlaOpenflowControllerIpType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AlaOpenflowControllerIpType_Type.__name__=_O
_AlaOpenflowControllerIpType_Object=MibTableColumn
alaOpenflowControllerIpType=_AlaOpenflowControllerIpType_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,3,1,2),_AlaOpenflowControllerIpType_Type())
alaOpenflowControllerIpType.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOpenflowControllerIpType.setStatus(_A)
class _AlaOpenflowControllerIp_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AlaOpenflowControllerIp_Type.__name__=_N
_AlaOpenflowControllerIp_Object=MibTableColumn
alaOpenflowControllerIp=_AlaOpenflowControllerIp_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,3,1,3),_AlaOpenflowControllerIp_Type())
alaOpenflowControllerIp.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOpenflowControllerIp.setStatus(_A)
class _AlaOpenflowControllerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AlaOpenflowControllerPort_Type.__name__=_C
_AlaOpenflowControllerPort_Object=MibTableColumn
alaOpenflowControllerPort=_AlaOpenflowControllerPort_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,3,1,4),_AlaOpenflowControllerPort_Type())
alaOpenflowControllerPort.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOpenflowControllerPort.setStatus(_A)
class _AlaOpenflowControllerRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('equal',1),('master',2),('slave',3)))
_AlaOpenflowControllerRole_Type.__name__=_C
_AlaOpenflowControllerRole_Object=MibTableColumn
alaOpenflowControllerRole=_AlaOpenflowControllerRole_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,3,1,5),_AlaOpenflowControllerRole_Type())
alaOpenflowControllerRole.setMaxAccess(_F)
if mibBuilder.loadTexts:alaOpenflowControllerRole.setStatus(_A)
class _AlaOpenflowControllerAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_AlaOpenflowControllerAdminState_Type.__name__=_C
_AlaOpenflowControllerAdminState_Object=MibTableColumn
alaOpenflowControllerAdminState=_AlaOpenflowControllerAdminState_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,3,1,6),_AlaOpenflowControllerAdminState_Type())
alaOpenflowControllerAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowControllerAdminState.setStatus(_A)
class _AlaOpenflowControllerOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('invalid',1),(_I,2),('sendError',3),('init',4),('connecting',5),('backoff',6),('exchangingHello',7),('active',8),('idle',9),('disconnected',10)))
_AlaOpenflowControllerOperState_Type.__name__=_C
_AlaOpenflowControllerOperState_Object=MibTableColumn
alaOpenflowControllerOperState=_AlaOpenflowControllerOperState_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,3,1,7),_AlaOpenflowControllerOperState_Type())
alaOpenflowControllerOperState.setMaxAccess(_F)
if mibBuilder.loadTexts:alaOpenflowControllerOperState.setStatus(_A)
_AlaOpenflowControllerRowStatus_Type=RowStatus
_AlaOpenflowControllerRowStatus_Object=MibTableColumn
alaOpenflowControllerRowStatus=_AlaOpenflowControllerRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,3,1,8),_AlaOpenflowControllerRowStatus_Type())
alaOpenflowControllerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowControllerRowStatus.setStatus(_A)
class _AlaOpenflowControllerPriority_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AlaOpenflowControllerPriority_Type.__name__=_C
_AlaOpenflowControllerPriority_Object=MibTableColumn
alaOpenflowControllerPriority=_AlaOpenflowControllerPriority_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,3,1,9),_AlaOpenflowControllerPriority_Type())
alaOpenflowControllerPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowControllerPriority.setStatus(_A)
_AlaOpenflowInterfaceTable_Object=MibTable
alaOpenflowInterfaceTable=_AlaOpenflowInterfaceTable_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,4))
if mibBuilder.loadTexts:alaOpenflowInterfaceTable.setStatus(_A)
_AlaOpenflowInterfaceEntry_Object=MibTableRow
alaOpenflowInterfaceEntry=_AlaOpenflowInterfaceEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,4,1))
alaOpenflowInterfaceEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:alaOpenflowInterfaceEntry.setStatus(_A)
class _AlaOpenflowInterfaceLogicalSwitch_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AlaOpenflowInterfaceLogicalSwitch_Type.__name__=_H
_AlaOpenflowInterfaceLogicalSwitch_Object=MibTableColumn
alaOpenflowInterfaceLogicalSwitch=_AlaOpenflowInterfaceLogicalSwitch_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,4,1,1),_AlaOpenflowInterfaceLogicalSwitch_Type())
alaOpenflowInterfaceLogicalSwitch.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOpenflowInterfaceLogicalSwitch.setStatus(_A)
class _AlaOpenflowInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AlaOpenflowInterface_Type.__name__=_C
_AlaOpenflowInterface_Object=MibTableColumn
alaOpenflowInterface=_AlaOpenflowInterface_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,4,1,2),_AlaOpenflowInterface_Type())
alaOpenflowInterface.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOpenflowInterface.setStatus(_A)
class _AlaOpenflowInterfaceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('api',2),(_S,3)))
_AlaOpenflowInterfaceMode_Type.__name__=_C
_AlaOpenflowInterfaceMode_Object=MibTableColumn
alaOpenflowInterfaceMode=_AlaOpenflowInterfaceMode_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,4,1,3),_AlaOpenflowInterfaceMode_Type())
alaOpenflowInterfaceMode.setMaxAccess(_F)
if mibBuilder.loadTexts:alaOpenflowInterfaceMode.setStatus(_A)
_AlaOpenflowInterfaceRowStatus_Type=RowStatus
_AlaOpenflowInterfaceRowStatus_Object=MibTableColumn
alaOpenflowInterfaceRowStatus=_AlaOpenflowInterfaceRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,4,1,4),_AlaOpenflowInterfaceRowStatus_Type())
alaOpenflowInterfaceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowInterfaceRowStatus.setStatus(_A)
class _AlaOpenflowInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trunk',1),('access',2)))
_AlaOpenflowInterfaceType_Type.__name__=_C
_AlaOpenflowInterfaceType_Object=MibTableColumn
alaOpenflowInterfaceType=_AlaOpenflowInterfaceType_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,4,1,5),_AlaOpenflowInterfaceType_Type())
alaOpenflowInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowInterfaceType.setStatus(_A)
class _AlaOpenflowInterfaceNativeVlan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4093))
_AlaOpenflowInterfaceNativeVlan_Type.__name__=_G
_AlaOpenflowInterfaceNativeVlan_Object=MibTableColumn
alaOpenflowInterfaceNativeVlan=_AlaOpenflowInterfaceNativeVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,4,1,6),_AlaOpenflowInterfaceNativeVlan_Type())
alaOpenflowInterfaceNativeVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowInterfaceNativeVlan.setStatus(_A)
_AlaOpenflowInterfaceVlanTable_Object=MibTable
alaOpenflowInterfaceVlanTable=_AlaOpenflowInterfaceVlanTable_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,5))
if mibBuilder.loadTexts:alaOpenflowInterfaceVlanTable.setStatus(_A)
_AlaOpenflowInterfaceVlanEntry_Object=MibTableRow
alaOpenflowInterfaceVlanEntry=_AlaOpenflowInterfaceVlanEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,5,1))
alaOpenflowInterfaceVlanEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_Y))
if mibBuilder.loadTexts:alaOpenflowInterfaceVlanEntry.setStatus(_A)
class _AlaOpenflowInterfaceVlanVlanID_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,4093))
_AlaOpenflowInterfaceVlanVlanID_Type.__name__=_G
_AlaOpenflowInterfaceVlanVlanID_Object=MibTableColumn
alaOpenflowInterfaceVlanVlanID=_AlaOpenflowInterfaceVlanVlanID_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,5,1,1),_AlaOpenflowInterfaceVlanVlanID_Type())
alaOpenflowInterfaceVlanVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:alaOpenflowInterfaceVlanVlanID.setStatus(_A)
_AlaOpenflowInterfaceVlanRowStatus_Type=RowStatus
_AlaOpenflowInterfaceVlanRowStatus_Object=MibTableColumn
alaOpenflowInterfaceVlanRowStatus=_AlaOpenflowInterfaceVlanRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,77,1,1,5,1,2),_AlaOpenflowInterfaceVlanRowStatus_Type())
alaOpenflowInterfaceVlanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaOpenflowInterfaceVlanRowStatus.setStatus(_A)
_AlcatelIND1OpenflowMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1OpenflowMIBConformance=_AlcatelIND1OpenflowMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,77,1,2))
if mibBuilder.loadTexts:alcatelIND1OpenflowMIBConformance.setStatus(_A)
_AlcatelIND1OpenflowMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1OpenflowMIBGroups=_AlcatelIND1OpenflowMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,77,1,2,1))
if mibBuilder.loadTexts:alcatelIND1OpenflowMIBGroups.setStatus(_A)
_AlcatelIND1OpenflowMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1OpenflowMIBCompliances=_AlcatelIND1OpenflowMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,77,1,2,2))
if mibBuilder.loadTexts:alcatelIND1OpenflowMIBCompliances.setStatus(_A)
alaOpenflowModuleConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,77,1,2,1,1))
alaOpenflowModuleConfigGroup.setObjects(*((_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:alaOpenflowModuleConfigGroup.setStatus(_A)
alaOpenflowModuleLogicalSwitchGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,77,1,2,1,2))
alaOpenflowModuleLogicalSwitchGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:alaOpenflowModuleLogicalSwitchGroup.setStatus(_A)
alaOpenflowModuleControllerGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,77,1,2,1,3))
alaOpenflowModuleControllerGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:alaOpenflowModuleControllerGroup.setStatus(_A)
alaOpenflowModuleInterfaceGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,77,1,2,1,4))
alaOpenflowModuleInterfaceGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:alaOpenflowModuleInterfaceGroup.setStatus(_A)
alaOpenflowModuleInterfaceVlanGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,77,1,2,1,5))
alaOpenflowModuleInterfaceVlanGroup.setObjects((_B,_z))
if mibBuilder.loadTexts:alaOpenflowModuleInterfaceVlanGroup.setStatus(_A)
alaOpenflowMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,77,1,2,2,1))
alaOpenflowMIBCompliance.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:alaOpenflowMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1OpenflowMIB':alcatelIND1OpenflowMIB,'alcatelIND1OpenflowMIBNotifications':alcatelIND1OpenflowMIBNotifications,'alcatelIND1OpenflowMIBObjects':alcatelIND1OpenflowMIBObjects,'alaOpenflowGlobalConfigObjects':alaOpenflowGlobalConfigObjects,_Z:alaOpenflowGlobalBackoffMax,_a:alaOpenflowGlobalIdleProbeTimeout,'alaOpenflowLogicalSwitchTable':alaOpenflowLogicalSwitchTable,'alaOpenflowLogicalSwitchEntry':alaOpenflowLogicalSwitchEntry,_Q:alaOpenflowLogicalSwitch,_b:alaOpenflowLogicalSwitchAdminState,_c:alaOpenflowLogicalSwitchMode,_d:alaOpenflowLogicalSwitchVersions,_e:alaOpenflowLogicalSwitchVlan,_f:alaOpenflowLogicalSwitchControllerCount,_g:alaOpenflowLogicalSwitchInterfaceCount,_h:alaOpenflowLogicalSwitchFlowCount,_i:alaOpenflowLogicalSwitchRowStatus,_j:alaOpenflowLogicalSwitchLearnedMacUpdate,_k:alaOpenflowLogicalSwitchProbeTime,_l:alaOpenflowLogicalSwitchFailureDetectTime,_m:alaOpenflowLogicalSwitchDPID,_n:alaOpenflowLogicalSwitchTableMissAction,_o:alaOpenflowLogicalSwitchTCPBufferSizeTx,_p:alaOpenflowLogicalSwitchTCPBufferSizeRx,'alaOpenflowControllerTable':alaOpenflowControllerTable,'alaOpenflowControllerEntry':alaOpenflowControllerEntry,_U:alaOpenflowControllerLogicalSwitch,_V:alaOpenflowControllerIpType,_W:alaOpenflowControllerIp,_X:alaOpenflowControllerPort,_q:alaOpenflowControllerRole,_r:alaOpenflowControllerAdminState,_s:alaOpenflowControllerOperState,_t:alaOpenflowControllerRowStatus,_u:alaOpenflowControllerPriority,'alaOpenflowInterfaceTable':alaOpenflowInterfaceTable,'alaOpenflowInterfaceEntry':alaOpenflowInterfaceEntry,_K:alaOpenflowInterfaceLogicalSwitch,_L:alaOpenflowInterface,_v:alaOpenflowInterfaceMode,_w:alaOpenflowInterfaceRowStatus,_x:alaOpenflowInterfaceType,_y:alaOpenflowInterfaceNativeVlan,'alaOpenflowInterfaceVlanTable':alaOpenflowInterfaceVlanTable,'alaOpenflowInterfaceVlanEntry':alaOpenflowInterfaceVlanEntry,_Y:alaOpenflowInterfaceVlanVlanID,_z:alaOpenflowInterfaceVlanRowStatus,'alcatelIND1OpenflowMIBConformance':alcatelIND1OpenflowMIBConformance,'alcatelIND1OpenflowMIBGroups':alcatelIND1OpenflowMIBGroups,_A0:alaOpenflowModuleConfigGroup,_A1:alaOpenflowModuleLogicalSwitchGroup,_A2:alaOpenflowModuleControllerGroup,_A3:alaOpenflowModuleInterfaceGroup,_A4:alaOpenflowModuleInterfaceVlanGroup,'alcatelIND1OpenflowMIBCompliances':alcatelIND1OpenflowMIBCompliances,'alaOpenflowMIBCompliance':alaOpenflowMIBCompliance})