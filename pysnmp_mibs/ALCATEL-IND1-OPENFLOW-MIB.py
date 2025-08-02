_A8='alaOpenflowModuleGroupStatsGroup'
_A7='alaOpenflowModulePortStatsGroup'
_A6='alaOpenflowModuleFlowEntryStatsGroup'
_A5='alaOpenflowModuleFlowStatsGroup'
_A4='alaOpenflowModuleInterfaceGroup'
_A3='alaOpenflowModuleControllerGroup'
_A2='alaOpenflowModuleLogicalSwitchGroup'
_A1='alaOpenflowModuleConfigGroup'
_A0='alaOpenflowGroupStatsDuration'
_z='alaOpenflowGroupStatsId'
_y='alaOpenflowPortStatsDuration'
_x='alaOpenflowPortStatsRcvdPcks'
_w='alaOpenflowPortStatsTransPcks'
_v='alaOpenflowPortStatsPortNumber'
_u='alaOpenflowPortStatsSlotNumber'
_t='alaOpenflowFlowEntryStatsDuration'
_s='alaOpenflowFlowEntryStatsRcvdbytes'
_r='alaOpenflowFlowEntryStatsRcvdPcks'
_q='alaOpenflowFlowEntryStatsFlowId'
_p='alaOpenflowFlowStatsWildCount'
_o='alaOpenflowFlowStatsExactCount'
_n='alaOpenflowInterfaceRowStatus'
_m='alaOpenflowInterfaceMode'
_l='alaOpenflowControllerRowStatus'
_k='alaOpenflowControllerOperState'
_j='alaOpenflowControllerAdminState'
_i='alaOpenflowControllerRole'
_h='alaOpenflowLogicalSwitchRowStatus'
_g='alaOpenflowLogicalSwitchFlowCount'
_f='alaOpenflowLogicalSwitchInterfaceCount'
_e='alaOpenflowLogicalSwitchControllerCount'
_d='alaOpenflowLogicalSwitchVlan'
_c='alaOpenflowLogicalSwitchVersions'
_b='alaOpenflowLogicalSwitchMode'
_a='alaOpenflowLogicalSwitchAdminState'
_Z='alaOpenflowGlobalIdleProbeTimeout'
_Y='alaOpenflowGlobalBackoffMax'
_X='alaOpenflowGroupStatsLogicalSwitch'
_W='alaOpenflowPortStatsLogicalSwitch'
_V='alaOpenflowFlowEntryStatsLogicalSwitch'
_U='alaOpenflowFlowStatsLogicalSwitch'
_T='alaOpenflowInterface'
_S='alaOpenflowInterfaceLogicalSwitch'
_R='alaOpenflowControllerPort'
_Q='alaOpenflowControllerIp'
_P='alaOpenflowControllerIpType'
_O='alaOpenflowControllerLogicalSwitch'
_N='normal'
_M='enabled'
_L='alaOpenflowLogicalSwitch'
_K='read-write'
_J='InetAddressType'
_I='InetAddress'
_H='disabled'
_G='not-accessible'
_F='read-create'
_E='SnmpAdminString'
_D='Integer32'
_C='read-only'
_B='ALCATEL-IND1-OPENFLOW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1OpenflowMIB,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1OpenflowMIB')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_I,_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
alcatelIND1OpenflowMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,70,1))
if mibBuilder.loadTexts:alcatelIND1OpenflowMIB.setRevisions(('2013-11-08 00:00',))
_AlcatelIND1OpenflowMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1OpenflowMIBNotifications=_AlcatelIND1OpenflowMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,70,1,0))
_AlcatelIND1OpenflowMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1OpenflowMIBObjects=_AlcatelIND1OpenflowMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,70,1,1))
if mibBuilder.loadTexts:alcatelIND1OpenflowMIBObjects.setStatus(_A)
_AlaOpenflowGlobalConfigObjects_ObjectIdentity=ObjectIdentity
alaOpenflowGlobalConfigObjects=_AlaOpenflowGlobalConfigObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,1))
class _AlaOpenflowGlobalBackoffMax_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_AlaOpenflowGlobalBackoffMax_Type.__name__=_D
_AlaOpenflowGlobalBackoffMax_Object=MibScalar
alaOpenflowGlobalBackoffMax=_AlaOpenflowGlobalBackoffMax_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,1,1),_AlaOpenflowGlobalBackoffMax_Type())
alaOpenflowGlobalBackoffMax.setMaxAccess(_K)
if mibBuilder.loadTexts:alaOpenflowGlobalBackoffMax.setStatus(_A)
class _AlaOpenflowGlobalIdleProbeTimeout_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_AlaOpenflowGlobalIdleProbeTimeout_Type.__name__=_D
_AlaOpenflowGlobalIdleProbeTimeout_Object=MibScalar
alaOpenflowGlobalIdleProbeTimeout=_AlaOpenflowGlobalIdleProbeTimeout_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,1,2),_AlaOpenflowGlobalIdleProbeTimeout_Type())
alaOpenflowGlobalIdleProbeTimeout.setMaxAccess(_K)
if mibBuilder.loadTexts:alaOpenflowGlobalIdleProbeTimeout.setStatus(_A)
_AlaOpenflowLogicalSwitchTable_Object=MibTable
alaOpenflowLogicalSwitchTable=_AlaOpenflowLogicalSwitchTable_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,2))
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchTable.setStatus(_A)
_AlaOpenflowLogicalSwitchEntry_Object=MibTableRow
alaOpenflowLogicalSwitchEntry=_AlaOpenflowLogicalSwitchEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,2,1))
alaOpenflowLogicalSwitchEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchEntry.setStatus(_A)
class _AlaOpenflowLogicalSwitch_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AlaOpenflowLogicalSwitch_Type.__name__=_E
_AlaOpenflowLogicalSwitch_Object=MibTableColumn
alaOpenflowLogicalSwitch=_AlaOpenflowLogicalSwitch_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,2,1,1),_AlaOpenflowLogicalSwitch_Type())
alaOpenflowLogicalSwitch.setMaxAccess(_G)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitch.setStatus(_A)
class _AlaOpenflowLogicalSwitchAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_H,2)))
_AlaOpenflowLogicalSwitchAdminState_Type.__name__=_D
_AlaOpenflowLogicalSwitchAdminState_Object=MibTableColumn
alaOpenflowLogicalSwitchAdminState=_AlaOpenflowLogicalSwitchAdminState_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,2,1,2),_AlaOpenflowLogicalSwitchAdminState_Type())
alaOpenflowLogicalSwitchAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchAdminState.setStatus(_A)
class _AlaOpenflowLogicalSwitchMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('api',2)))
_AlaOpenflowLogicalSwitchMode_Type.__name__=_D
_AlaOpenflowLogicalSwitchMode_Object=MibTableColumn
alaOpenflowLogicalSwitchMode=_AlaOpenflowLogicalSwitchMode_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,2,1,3),_AlaOpenflowLogicalSwitchMode_Type())
alaOpenflowLogicalSwitchMode.setMaxAccess(_F)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchMode.setStatus(_A)
class _AlaOpenflowLogicalSwitchVersions_Type(Bits):defaultBinValue='11';namedValues=NamedValues(*(('v1dot0',0),('v1dot3dot1',1)))
_AlaOpenflowLogicalSwitchVersions_Type.__name__='Bits'
_AlaOpenflowLogicalSwitchVersions_Object=MibTableColumn
alaOpenflowLogicalSwitchVersions=_AlaOpenflowLogicalSwitchVersions_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,2,1,4),_AlaOpenflowLogicalSwitchVersions_Type())
alaOpenflowLogicalSwitchVersions.setMaxAccess(_F)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchVersions.setStatus(_A)
class _AlaOpenflowLogicalSwitchVlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,4093))
_AlaOpenflowLogicalSwitchVlan_Type.__name__=_D
_AlaOpenflowLogicalSwitchVlan_Object=MibTableColumn
alaOpenflowLogicalSwitchVlan=_AlaOpenflowLogicalSwitchVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,2,1,5),_AlaOpenflowLogicalSwitchVlan_Type())
alaOpenflowLogicalSwitchVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchVlan.setStatus(_A)
class _AlaOpenflowLogicalSwitchControllerCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AlaOpenflowLogicalSwitchControllerCount_Type.__name__=_D
_AlaOpenflowLogicalSwitchControllerCount_Object=MibTableColumn
alaOpenflowLogicalSwitchControllerCount=_AlaOpenflowLogicalSwitchControllerCount_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,2,1,6),_AlaOpenflowLogicalSwitchControllerCount_Type())
alaOpenflowLogicalSwitchControllerCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchControllerCount.setStatus(_A)
class _AlaOpenflowLogicalSwitchInterfaceCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_AlaOpenflowLogicalSwitchInterfaceCount_Type.__name__=_D
_AlaOpenflowLogicalSwitchInterfaceCount_Object=MibTableColumn
alaOpenflowLogicalSwitchInterfaceCount=_AlaOpenflowLogicalSwitchInterfaceCount_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,2,1,7),_AlaOpenflowLogicalSwitchInterfaceCount_Type())
alaOpenflowLogicalSwitchInterfaceCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchInterfaceCount.setStatus(_A)
class _AlaOpenflowLogicalSwitchFlowCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,511))
_AlaOpenflowLogicalSwitchFlowCount_Type.__name__=_D
_AlaOpenflowLogicalSwitchFlowCount_Object=MibTableColumn
alaOpenflowLogicalSwitchFlowCount=_AlaOpenflowLogicalSwitchFlowCount_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,2,1,8),_AlaOpenflowLogicalSwitchFlowCount_Type())
alaOpenflowLogicalSwitchFlowCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchFlowCount.setStatus(_A)
_AlaOpenflowLogicalSwitchRowStatus_Type=RowStatus
_AlaOpenflowLogicalSwitchRowStatus_Object=MibTableColumn
alaOpenflowLogicalSwitchRowStatus=_AlaOpenflowLogicalSwitchRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,2,1,9),_AlaOpenflowLogicalSwitchRowStatus_Type())
alaOpenflowLogicalSwitchRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaOpenflowLogicalSwitchRowStatus.setStatus(_A)
_AlaOpenflowControllerTable_Object=MibTable
alaOpenflowControllerTable=_AlaOpenflowControllerTable_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,3))
if mibBuilder.loadTexts:alaOpenflowControllerTable.setStatus(_A)
_AlaOpenflowControllerEntry_Object=MibTableRow
alaOpenflowControllerEntry=_AlaOpenflowControllerEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,3,1))
alaOpenflowControllerEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:alaOpenflowControllerEntry.setStatus(_A)
class _AlaOpenflowControllerLogicalSwitch_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AlaOpenflowControllerLogicalSwitch_Type.__name__=_E
_AlaOpenflowControllerLogicalSwitch_Object=MibTableColumn
alaOpenflowControllerLogicalSwitch=_AlaOpenflowControllerLogicalSwitch_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,3,1,1),_AlaOpenflowControllerLogicalSwitch_Type())
alaOpenflowControllerLogicalSwitch.setMaxAccess(_G)
if mibBuilder.loadTexts:alaOpenflowControllerLogicalSwitch.setStatus(_A)
class _AlaOpenflowControllerIpType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AlaOpenflowControllerIpType_Type.__name__=_J
_AlaOpenflowControllerIpType_Object=MibTableColumn
alaOpenflowControllerIpType=_AlaOpenflowControllerIpType_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,3,1,2),_AlaOpenflowControllerIpType_Type())
alaOpenflowControllerIpType.setMaxAccess(_G)
if mibBuilder.loadTexts:alaOpenflowControllerIpType.setStatus(_A)
class _AlaOpenflowControllerIp_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AlaOpenflowControllerIp_Type.__name__=_I
_AlaOpenflowControllerIp_Object=MibTableColumn
alaOpenflowControllerIp=_AlaOpenflowControllerIp_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,3,1,3),_AlaOpenflowControllerIp_Type())
alaOpenflowControllerIp.setMaxAccess(_G)
if mibBuilder.loadTexts:alaOpenflowControllerIp.setStatus(_A)
class _AlaOpenflowControllerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AlaOpenflowControllerPort_Type.__name__=_D
_AlaOpenflowControllerPort_Object=MibTableColumn
alaOpenflowControllerPort=_AlaOpenflowControllerPort_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,3,1,4),_AlaOpenflowControllerPort_Type())
alaOpenflowControllerPort.setMaxAccess(_G)
if mibBuilder.loadTexts:alaOpenflowControllerPort.setStatus(_A)
class _AlaOpenflowControllerRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('equal',1),('master',2),('slave',3)))
_AlaOpenflowControllerRole_Type.__name__=_D
_AlaOpenflowControllerRole_Object=MibTableColumn
alaOpenflowControllerRole=_AlaOpenflowControllerRole_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,3,1,5),_AlaOpenflowControllerRole_Type())
alaOpenflowControllerRole.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowControllerRole.setStatus(_A)
class _AlaOpenflowControllerAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_H,2)))
_AlaOpenflowControllerAdminState_Type.__name__=_D
_AlaOpenflowControllerAdminState_Object=MibTableColumn
alaOpenflowControllerAdminState=_AlaOpenflowControllerAdminState_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,3,1,6),_AlaOpenflowControllerAdminState_Type())
alaOpenflowControllerAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:alaOpenflowControllerAdminState.setStatus(_A)
class _AlaOpenflowControllerOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('invalid',1),(_H,2),('sendError',3),('init',4),('connecting',5),('backoff',6),('exchangingHello',7),('active',8),('idle',9),('disconnected',10)))
_AlaOpenflowControllerOperState_Type.__name__=_D
_AlaOpenflowControllerOperState_Object=MibTableColumn
alaOpenflowControllerOperState=_AlaOpenflowControllerOperState_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,3,1,7),_AlaOpenflowControllerOperState_Type())
alaOpenflowControllerOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowControllerOperState.setStatus(_A)
_AlaOpenflowControllerRowStatus_Type=RowStatus
_AlaOpenflowControllerRowStatus_Object=MibTableColumn
alaOpenflowControllerRowStatus=_AlaOpenflowControllerRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,3,1,8),_AlaOpenflowControllerRowStatus_Type())
alaOpenflowControllerRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaOpenflowControllerRowStatus.setStatus(_A)
_AlaOpenflowInterfaceTable_Object=MibTable
alaOpenflowInterfaceTable=_AlaOpenflowInterfaceTable_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,4))
if mibBuilder.loadTexts:alaOpenflowInterfaceTable.setStatus(_A)
_AlaOpenflowInterfaceEntry_Object=MibTableRow
alaOpenflowInterfaceEntry=_AlaOpenflowInterfaceEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,4,1))
alaOpenflowInterfaceEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:alaOpenflowInterfaceEntry.setStatus(_A)
class _AlaOpenflowInterfaceLogicalSwitch_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AlaOpenflowInterfaceLogicalSwitch_Type.__name__=_E
_AlaOpenflowInterfaceLogicalSwitch_Object=MibTableColumn
alaOpenflowInterfaceLogicalSwitch=_AlaOpenflowInterfaceLogicalSwitch_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,4,1,1),_AlaOpenflowInterfaceLogicalSwitch_Type())
alaOpenflowInterfaceLogicalSwitch.setMaxAccess(_G)
if mibBuilder.loadTexts:alaOpenflowInterfaceLogicalSwitch.setStatus(_A)
class _AlaOpenflowInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AlaOpenflowInterface_Type.__name__=_D
_AlaOpenflowInterface_Object=MibTableColumn
alaOpenflowInterface=_AlaOpenflowInterface_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,4,1,2),_AlaOpenflowInterface_Type())
alaOpenflowInterface.setMaxAccess(_G)
if mibBuilder.loadTexts:alaOpenflowInterface.setStatus(_A)
class _AlaOpenflowInterfaceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('api',2)))
_AlaOpenflowInterfaceMode_Type.__name__=_D
_AlaOpenflowInterfaceMode_Object=MibTableColumn
alaOpenflowInterfaceMode=_AlaOpenflowInterfaceMode_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,4,1,3),_AlaOpenflowInterfaceMode_Type())
alaOpenflowInterfaceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowInterfaceMode.setStatus(_A)
_AlaOpenflowInterfaceRowStatus_Type=RowStatus
_AlaOpenflowInterfaceRowStatus_Object=MibTableColumn
alaOpenflowInterfaceRowStatus=_AlaOpenflowInterfaceRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,4,1,4),_AlaOpenflowInterfaceRowStatus_Type())
alaOpenflowInterfaceRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaOpenflowInterfaceRowStatus.setStatus(_A)
_AlaOpenflowFlowStatsTable_Object=MibTable
alaOpenflowFlowStatsTable=_AlaOpenflowFlowStatsTable_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,5))
if mibBuilder.loadTexts:alaOpenflowFlowStatsTable.setStatus(_A)
_AlaOpenflowFlowStatsEntry_Object=MibTableRow
alaOpenflowFlowStatsEntry=_AlaOpenflowFlowStatsEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,5,1))
alaOpenflowFlowStatsEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:alaOpenflowFlowStatsEntry.setStatus(_A)
class _AlaOpenflowFlowStatsLogicalSwitch_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AlaOpenflowFlowStatsLogicalSwitch_Type.__name__=_E
_AlaOpenflowFlowStatsLogicalSwitch_Object=MibTableColumn
alaOpenflowFlowStatsLogicalSwitch=_AlaOpenflowFlowStatsLogicalSwitch_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,5,1,1),_AlaOpenflowFlowStatsLogicalSwitch_Type())
alaOpenflowFlowStatsLogicalSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowFlowStatsLogicalSwitch.setStatus(_A)
class _AlaOpenflowFlowStatsExactCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_AlaOpenflowFlowStatsExactCount_Type.__name__=_D
_AlaOpenflowFlowStatsExactCount_Object=MibTableColumn
alaOpenflowFlowStatsExactCount=_AlaOpenflowFlowStatsExactCount_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,5,1,2),_AlaOpenflowFlowStatsExactCount_Type())
alaOpenflowFlowStatsExactCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowFlowStatsExactCount.setStatus(_A)
class _AlaOpenflowFlowStatsWildCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_AlaOpenflowFlowStatsWildCount_Type.__name__=_D
_AlaOpenflowFlowStatsWildCount_Object=MibTableColumn
alaOpenflowFlowStatsWildCount=_AlaOpenflowFlowStatsWildCount_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,5,1,3),_AlaOpenflowFlowStatsWildCount_Type())
alaOpenflowFlowStatsWildCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowFlowStatsWildCount.setStatus(_A)
_AlaOpenflowFlowEntryStatsTable_Object=MibTable
alaOpenflowFlowEntryStatsTable=_AlaOpenflowFlowEntryStatsTable_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,6))
if mibBuilder.loadTexts:alaOpenflowFlowEntryStatsTable.setStatus(_A)
_AlaOpenflowFlowEntryStatsEntry_Object=MibTableRow
alaOpenflowFlowEntryStatsEntry=_AlaOpenflowFlowEntryStatsEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,6,1))
alaOpenflowFlowEntryStatsEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:alaOpenflowFlowEntryStatsEntry.setStatus(_A)
class _AlaOpenflowFlowEntryStatsLogicalSwitch_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AlaOpenflowFlowEntryStatsLogicalSwitch_Type.__name__=_E
_AlaOpenflowFlowEntryStatsLogicalSwitch_Object=MibTableColumn
alaOpenflowFlowEntryStatsLogicalSwitch=_AlaOpenflowFlowEntryStatsLogicalSwitch_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,6,1,1),_AlaOpenflowFlowEntryStatsLogicalSwitch_Type())
alaOpenflowFlowEntryStatsLogicalSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowFlowEntryStatsLogicalSwitch.setStatus(_A)
class _AlaOpenflowFlowEntryStatsFlowId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_AlaOpenflowFlowEntryStatsFlowId_Type.__name__=_D
_AlaOpenflowFlowEntryStatsFlowId_Object=MibTableColumn
alaOpenflowFlowEntryStatsFlowId=_AlaOpenflowFlowEntryStatsFlowId_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,6,1,2),_AlaOpenflowFlowEntryStatsFlowId_Type())
alaOpenflowFlowEntryStatsFlowId.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowFlowEntryStatsFlowId.setStatus(_A)
_AlaOpenflowFlowEntryStatsRcvdPcks_Type=Counter32
_AlaOpenflowFlowEntryStatsRcvdPcks_Object=MibTableColumn
alaOpenflowFlowEntryStatsRcvdPcks=_AlaOpenflowFlowEntryStatsRcvdPcks_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,6,1,3),_AlaOpenflowFlowEntryStatsRcvdPcks_Type())
alaOpenflowFlowEntryStatsRcvdPcks.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowFlowEntryStatsRcvdPcks.setStatus(_A)
_AlaOpenflowFlowEntryStatsRcvdbytes_Type=Counter32
_AlaOpenflowFlowEntryStatsRcvdbytes_Object=MibTableColumn
alaOpenflowFlowEntryStatsRcvdbytes=_AlaOpenflowFlowEntryStatsRcvdbytes_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,6,1,4),_AlaOpenflowFlowEntryStatsRcvdbytes_Type())
alaOpenflowFlowEntryStatsRcvdbytes.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowFlowEntryStatsRcvdbytes.setStatus(_A)
_AlaOpenflowFlowEntryStatsDuration_Type=TimeStamp
_AlaOpenflowFlowEntryStatsDuration_Object=MibTableColumn
alaOpenflowFlowEntryStatsDuration=_AlaOpenflowFlowEntryStatsDuration_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,6,1,5),_AlaOpenflowFlowEntryStatsDuration_Type())
alaOpenflowFlowEntryStatsDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowFlowEntryStatsDuration.setStatus(_A)
_AlaOpenflowPortStatsTable_Object=MibTable
alaOpenflowPortStatsTable=_AlaOpenflowPortStatsTable_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,7))
if mibBuilder.loadTexts:alaOpenflowPortStatsTable.setStatus(_A)
_AlaOpenflowPortStatsEntry_Object=MibTableRow
alaOpenflowPortStatsEntry=_AlaOpenflowPortStatsEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,7,1))
alaOpenflowPortStatsEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:alaOpenflowPortStatsEntry.setStatus(_A)
class _AlaOpenflowPortStatsLogicalSwitch_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AlaOpenflowPortStatsLogicalSwitch_Type.__name__=_E
_AlaOpenflowPortStatsLogicalSwitch_Object=MibTableColumn
alaOpenflowPortStatsLogicalSwitch=_AlaOpenflowPortStatsLogicalSwitch_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,7,1,1),_AlaOpenflowPortStatsLogicalSwitch_Type())
alaOpenflowPortStatsLogicalSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowPortStatsLogicalSwitch.setStatus(_A)
class _AlaOpenflowPortStatsSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AlaOpenflowPortStatsSlotNumber_Type.__name__=_D
_AlaOpenflowPortStatsSlotNumber_Object=MibTableColumn
alaOpenflowPortStatsSlotNumber=_AlaOpenflowPortStatsSlotNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,7,1,2),_AlaOpenflowPortStatsSlotNumber_Type())
alaOpenflowPortStatsSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowPortStatsSlotNumber.setStatus(_A)
class _AlaOpenflowPortStatsPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_AlaOpenflowPortStatsPortNumber_Type.__name__=_D
_AlaOpenflowPortStatsPortNumber_Object=MibTableColumn
alaOpenflowPortStatsPortNumber=_AlaOpenflowPortStatsPortNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,7,1,3),_AlaOpenflowPortStatsPortNumber_Type())
alaOpenflowPortStatsPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowPortStatsPortNumber.setStatus(_A)
_AlaOpenflowPortStatsTransPcks_Type=Counter32
_AlaOpenflowPortStatsTransPcks_Object=MibTableColumn
alaOpenflowPortStatsTransPcks=_AlaOpenflowPortStatsTransPcks_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,7,1,4),_AlaOpenflowPortStatsTransPcks_Type())
alaOpenflowPortStatsTransPcks.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowPortStatsTransPcks.setStatus(_A)
_AlaOpenflowPortStatsRcvdPcks_Type=Counter32
_AlaOpenflowPortStatsRcvdPcks_Object=MibTableColumn
alaOpenflowPortStatsRcvdPcks=_AlaOpenflowPortStatsRcvdPcks_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,7,1,5),_AlaOpenflowPortStatsRcvdPcks_Type())
alaOpenflowPortStatsRcvdPcks.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowPortStatsRcvdPcks.setStatus(_A)
_AlaOpenflowPortStatsDuration_Type=TimeStamp
_AlaOpenflowPortStatsDuration_Object=MibTableColumn
alaOpenflowPortStatsDuration=_AlaOpenflowPortStatsDuration_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,7,1,6),_AlaOpenflowPortStatsDuration_Type())
alaOpenflowPortStatsDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowPortStatsDuration.setStatus(_A)
_AlaOpenflowGroupStatsTable_Object=MibTable
alaOpenflowGroupStatsTable=_AlaOpenflowGroupStatsTable_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,8))
if mibBuilder.loadTexts:alaOpenflowGroupStatsTable.setStatus(_A)
_AlaOpenflowGroupStatsEntry_Object=MibTableRow
alaOpenflowGroupStatsEntry=_AlaOpenflowGroupStatsEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,8,1))
alaOpenflowGroupStatsEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:alaOpenflowGroupStatsEntry.setStatus(_A)
class _AlaOpenflowGroupStatsLogicalSwitch_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AlaOpenflowGroupStatsLogicalSwitch_Type.__name__=_E
_AlaOpenflowGroupStatsLogicalSwitch_Object=MibTableColumn
alaOpenflowGroupStatsLogicalSwitch=_AlaOpenflowGroupStatsLogicalSwitch_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,8,1,1),_AlaOpenflowGroupStatsLogicalSwitch_Type())
alaOpenflowGroupStatsLogicalSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowGroupStatsLogicalSwitch.setStatus(_A)
class _AlaOpenflowGroupStatsId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_AlaOpenflowGroupStatsId_Type.__name__=_D
_AlaOpenflowGroupStatsId_Object=MibTableColumn
alaOpenflowGroupStatsId=_AlaOpenflowGroupStatsId_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,8,1,2),_AlaOpenflowGroupStatsId_Type())
alaOpenflowGroupStatsId.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowGroupStatsId.setStatus(_A)
_AlaOpenflowGroupStatsDuration_Type=TimeStamp
_AlaOpenflowGroupStatsDuration_Object=MibTableColumn
alaOpenflowGroupStatsDuration=_AlaOpenflowGroupStatsDuration_Object((1,3,6,1,4,1,6486,800,1,2,1,70,1,1,8,1,3),_AlaOpenflowGroupStatsDuration_Type())
alaOpenflowGroupStatsDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:alaOpenflowGroupStatsDuration.setStatus(_A)
_AlcatelIND1OpenflowMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1OpenflowMIBConformance=_AlcatelIND1OpenflowMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,70,1,2))
if mibBuilder.loadTexts:alcatelIND1OpenflowMIBConformance.setStatus(_A)
_AlcatelIND1OpenflowMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1OpenflowMIBGroups=_AlcatelIND1OpenflowMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,70,1,2,1))
if mibBuilder.loadTexts:alcatelIND1OpenflowMIBGroups.setStatus(_A)
_AlcatelIND1OpenflowMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1OpenflowMIBCompliances=_AlcatelIND1OpenflowMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,70,1,2,2))
if mibBuilder.loadTexts:alcatelIND1OpenflowMIBCompliances.setStatus(_A)
alaOpenflowModuleConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,70,1,2,1,1))
alaOpenflowModuleConfigGroup.setObjects(*((_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:alaOpenflowModuleConfigGroup.setStatus(_A)
alaOpenflowModuleLogicalSwitchGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,70,1,2,1,2))
alaOpenflowModuleLogicalSwitchGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:alaOpenflowModuleLogicalSwitchGroup.setStatus(_A)
alaOpenflowModuleControllerGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,70,1,2,1,3))
alaOpenflowModuleControllerGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:alaOpenflowModuleControllerGroup.setStatus(_A)
alaOpenflowModuleInterfaceGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,70,1,2,1,4))
alaOpenflowModuleInterfaceGroup.setObjects(*((_B,_m),(_B,_n)))
if mibBuilder.loadTexts:alaOpenflowModuleInterfaceGroup.setStatus(_A)
alaOpenflowModuleFlowStatsGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,70,1,2,1,5))
alaOpenflowModuleFlowStatsGroup.setObjects(*((_B,_o),(_B,_p)))
if mibBuilder.loadTexts:alaOpenflowModuleFlowStatsGroup.setStatus(_A)
alaOpenflowModuleFlowEntryStatsGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,70,1,2,1,6))
alaOpenflowModuleFlowEntryStatsGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:alaOpenflowModuleFlowEntryStatsGroup.setStatus(_A)
alaOpenflowModulePortStatsGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,70,1,2,1,7))
alaOpenflowModulePortStatsGroup.setObjects(*((_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:alaOpenflowModulePortStatsGroup.setStatus(_A)
alaOpenflowModuleGroupStatsGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,70,1,2,1,8))
alaOpenflowModuleGroupStatsGroup.setObjects(*((_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:alaOpenflowModuleGroupStatsGroup.setStatus(_A)
alaOpenflowMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,70,1,2,2,1))
alaOpenflowMIBCompliance.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:alaOpenflowMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1OpenflowMIB':alcatelIND1OpenflowMIB,'alcatelIND1OpenflowMIBNotifications':alcatelIND1OpenflowMIBNotifications,'alcatelIND1OpenflowMIBObjects':alcatelIND1OpenflowMIBObjects,'alaOpenflowGlobalConfigObjects':alaOpenflowGlobalConfigObjects,_Y:alaOpenflowGlobalBackoffMax,_Z:alaOpenflowGlobalIdleProbeTimeout,'alaOpenflowLogicalSwitchTable':alaOpenflowLogicalSwitchTable,'alaOpenflowLogicalSwitchEntry':alaOpenflowLogicalSwitchEntry,_L:alaOpenflowLogicalSwitch,_a:alaOpenflowLogicalSwitchAdminState,_b:alaOpenflowLogicalSwitchMode,_c:alaOpenflowLogicalSwitchVersions,_d:alaOpenflowLogicalSwitchVlan,_e:alaOpenflowLogicalSwitchControllerCount,_f:alaOpenflowLogicalSwitchInterfaceCount,_g:alaOpenflowLogicalSwitchFlowCount,_h:alaOpenflowLogicalSwitchRowStatus,'alaOpenflowControllerTable':alaOpenflowControllerTable,'alaOpenflowControllerEntry':alaOpenflowControllerEntry,_O:alaOpenflowControllerLogicalSwitch,_P:alaOpenflowControllerIpType,_Q:alaOpenflowControllerIp,_R:alaOpenflowControllerPort,_i:alaOpenflowControllerRole,_j:alaOpenflowControllerAdminState,_k:alaOpenflowControllerOperState,_l:alaOpenflowControllerRowStatus,'alaOpenflowInterfaceTable':alaOpenflowInterfaceTable,'alaOpenflowInterfaceEntry':alaOpenflowInterfaceEntry,_S:alaOpenflowInterfaceLogicalSwitch,_T:alaOpenflowInterface,_m:alaOpenflowInterfaceMode,_n:alaOpenflowInterfaceRowStatus,'alaOpenflowFlowStatsTable':alaOpenflowFlowStatsTable,'alaOpenflowFlowStatsEntry':alaOpenflowFlowStatsEntry,_U:alaOpenflowFlowStatsLogicalSwitch,_o:alaOpenflowFlowStatsExactCount,_p:alaOpenflowFlowStatsWildCount,'alaOpenflowFlowEntryStatsTable':alaOpenflowFlowEntryStatsTable,'alaOpenflowFlowEntryStatsEntry':alaOpenflowFlowEntryStatsEntry,_V:alaOpenflowFlowEntryStatsLogicalSwitch,_q:alaOpenflowFlowEntryStatsFlowId,_r:alaOpenflowFlowEntryStatsRcvdPcks,_s:alaOpenflowFlowEntryStatsRcvdbytes,_t:alaOpenflowFlowEntryStatsDuration,'alaOpenflowPortStatsTable':alaOpenflowPortStatsTable,'alaOpenflowPortStatsEntry':alaOpenflowPortStatsEntry,_W:alaOpenflowPortStatsLogicalSwitch,_u:alaOpenflowPortStatsSlotNumber,_v:alaOpenflowPortStatsPortNumber,_w:alaOpenflowPortStatsTransPcks,_x:alaOpenflowPortStatsRcvdPcks,_y:alaOpenflowPortStatsDuration,'alaOpenflowGroupStatsTable':alaOpenflowGroupStatsTable,'alaOpenflowGroupStatsEntry':alaOpenflowGroupStatsEntry,_X:alaOpenflowGroupStatsLogicalSwitch,_z:alaOpenflowGroupStatsId,_A0:alaOpenflowGroupStatsDuration,'alcatelIND1OpenflowMIBConformance':alcatelIND1OpenflowMIBConformance,'alcatelIND1OpenflowMIBGroups':alcatelIND1OpenflowMIBGroups,_A1:alaOpenflowModuleConfigGroup,_A2:alaOpenflowModuleLogicalSwitchGroup,_A3:alaOpenflowModuleControllerGroup,_A4:alaOpenflowModuleInterfaceGroup,_A5:alaOpenflowModuleFlowStatsGroup,_A6:alaOpenflowModuleFlowEntryStatsGroup,_A7:alaOpenflowModulePortStatsGroup,_A8:alaOpenflowModuleGroupStatsGroup,'alcatelIND1OpenflowMIBCompliances':alcatelIND1OpenflowMIBCompliances,'alaOpenflowMIBCompliance':alaOpenflowMIBCompliance})