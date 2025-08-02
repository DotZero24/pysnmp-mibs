_AG='hotlinksInfoTriggerId'
_AF='trunkGroupInfoIndex'
_AE='vlanInfoId'
_AD='dot1pInfoPortIndex'
_AC='dot1pInfoPriorityIndex'
_AB='initialize'
_AA='dot1xInfoPortIndex'
_A9='lacpInfoPortIndex'
_A8='stpInfoPortIndex'
_A7='stpInfoPortStpIndex'
_A6='stpInfoIndex'
_A5='fdbMacAddr'
_A4='forwarding'
_A3='cistInfoPortIndex'
_A2='hotlinksStatsTriggerId'
_A1='lacpStatsIndex'
_A0='stgStatsPortIndex'
_z='stgStatsStpIndex'
_y='hotlinksNewCfgTriggerId'
_x='hotlinksCurCfgTriggerId'
_w='fdbNewCfgEntryIndex'
_v='dot1xNewCfgPortIndex'
_u='dot1xCurCfgPortIndex'
_t='lacpNewPortCfgTableId'
_s='passive'
_r='active'
_q='lacpCurPortCfgTableId'
_p='mstCistNewCfgPortIndex'
_o='mstCistCurCfgPortIndex'
_n='pmNewCfgPmirrMirrPortIndex'
_m='pmNewCfgPmirrMoniPortIndex'
_l='pmCurCfgPmirrMirrPortIndex'
_k='pmCurCfgPmirrMoniPortIndex'
_j='stgNewCfgPortIndex'
_i='stgNewCfgStgIndex'
_h='stgCurCfgPortIndex'
_g='stgCurCfgStgIndex'
_f='stgNewCfgIndex'
_e='stgCurCfgIndex'
_d='trunkGroupNewCfgIndex'
_c='trunkGroupCurCfgIndex'
_b='vlanNewCfgVlanId'
_a='vlanCurCfgVlanId'
_Z='false'
_Y='true'
_X='both'
_W='unknown'
_V='obsolete'
_U='forceAuth'
_T='forceUnauth'
_S='shared'
_R='p2p'
_Q='delete'
_P='other'
_O='DisplayString'
_N='auto'
_M='OctetString'
_L='on'
_K='disable'
_J='enable'
_I='off'
_H='enabled'
_G='disabled'
_F='BLADETYPE2-PHYSICAL-MIB'
_E='read-write'
_D='read-create'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId')
hpSwitchBladeType2_Mgmt,=mibBuilder.importSymbols('HP-SWITCH-PL-MIB','hpSwitchBladeType2-Mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_O,'PhysAddress','TextualConvention')
layer2=ModuleIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2))
_Layer2Configs_ObjectIdentity=ObjectIdentity
layer2Configs=_Layer2Configs_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1))
_Vlan_ObjectIdentity=ObjectIdentity
vlan=_Vlan_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1))
_VlanMaxEnt_Type=Integer32
_VlanMaxEnt_Object=MibScalar
vlanMaxEnt=_VlanMaxEnt_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,1),_VlanMaxEnt_Type())
vlanMaxEnt.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanMaxEnt.setStatus(_A)
_VlanCurCfgTable_Object=MibTable
vlanCurCfgTable=_VlanCurCfgTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,2))
if mibBuilder.loadTexts:vlanCurCfgTable.setStatus(_A)
_VlanCurCfgTableEntry_Object=MibTableRow
vlanCurCfgTableEntry=_VlanCurCfgTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,2,1))
vlanCurCfgTableEntry.setIndexNames((0,_F,_a))
if mibBuilder.loadTexts:vlanCurCfgTableEntry.setStatus(_A)
_VlanCurCfgVlanId_Type=Integer32
_VlanCurCfgVlanId_Object=MibTableColumn
vlanCurCfgVlanId=_VlanCurCfgVlanId_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,2,1,1),_VlanCurCfgVlanId_Type())
vlanCurCfgVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgVlanId.setStatus(_A)
class _VlanCurCfgVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VlanCurCfgVlanName_Type.__name__=_O
_VlanCurCfgVlanName_Object=MibTableColumn
vlanCurCfgVlanName=_VlanCurCfgVlanName_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,2,1,2),_VlanCurCfgVlanName_Type())
vlanCurCfgVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgVlanName.setStatus(_A)
_VlanCurCfgPorts_Type=OctetString
_VlanCurCfgPorts_Object=MibTableColumn
vlanCurCfgPorts=_VlanCurCfgPorts_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,2,1,3),_VlanCurCfgPorts_Type())
vlanCurCfgPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgPorts.setStatus(_A)
class _VlanCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_G,3)))
_VlanCurCfgState_Type.__name__=_C
_VlanCurCfgState_Object=MibTableColumn
vlanCurCfgState=_VlanCurCfgState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,2,1,4),_VlanCurCfgState_Type())
vlanCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgState.setStatus(_A)
_VlanCurCfgStg_Type=Integer32
_VlanCurCfgStg_Object=MibTableColumn
vlanCurCfgStg=_VlanCurCfgStg_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,2,1,6),_VlanCurCfgStg_Type())
vlanCurCfgStg.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgStg.setStatus(_A)
_VlanNewCfgTable_Object=MibTable
vlanNewCfgTable=_VlanNewCfgTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,3))
if mibBuilder.loadTexts:vlanNewCfgTable.setStatus(_A)
_VlanNewCfgTableEntry_Object=MibTableRow
vlanNewCfgTableEntry=_VlanNewCfgTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,3,1))
vlanNewCfgTableEntry.setIndexNames((0,_F,_b))
if mibBuilder.loadTexts:vlanNewCfgTableEntry.setStatus(_A)
_VlanNewCfgVlanId_Type=Integer32
_VlanNewCfgVlanId_Object=MibTableColumn
vlanNewCfgVlanId=_VlanNewCfgVlanId_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,3,1,1),_VlanNewCfgVlanId_Type())
vlanNewCfgVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNewCfgVlanId.setStatus(_A)
class _VlanNewCfgVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VlanNewCfgVlanName_Type.__name__=_O
_VlanNewCfgVlanName_Object=MibTableColumn
vlanNewCfgVlanName=_VlanNewCfgVlanName_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,3,1,2),_VlanNewCfgVlanName_Type())
vlanNewCfgVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgVlanName.setStatus(_A)
_VlanNewCfgPorts_Type=OctetString
_VlanNewCfgPorts_Object=MibTableColumn
vlanNewCfgPorts=_VlanNewCfgPorts_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,3,1,3),_VlanNewCfgPorts_Type())
vlanNewCfgPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNewCfgPorts.setStatus(_A)
class _VlanNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_G,3)))
_VlanNewCfgState_Type.__name__=_C
_VlanNewCfgState_Object=MibTableColumn
vlanNewCfgState=_VlanNewCfgState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,3,1,4),_VlanNewCfgState_Type())
vlanNewCfgState.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgState.setStatus(_A)
_VlanNewCfgAddPort_Type=Integer32
_VlanNewCfgAddPort_Object=MibTableColumn
vlanNewCfgAddPort=_VlanNewCfgAddPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,3,1,5),_VlanNewCfgAddPort_Type())
vlanNewCfgAddPort.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgAddPort.setStatus(_A)
_VlanNewCfgRemovePort_Type=Integer32
_VlanNewCfgRemovePort_Object=MibTableColumn
vlanNewCfgRemovePort=_VlanNewCfgRemovePort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,3,1,6),_VlanNewCfgRemovePort_Type())
vlanNewCfgRemovePort.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgRemovePort.setStatus(_A)
class _VlanNewCfgDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_VlanNewCfgDelete_Type.__name__=_C
_VlanNewCfgDelete_Object=MibTableColumn
vlanNewCfgDelete=_VlanNewCfgDelete_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,3,1,7),_VlanNewCfgDelete_Type())
vlanNewCfgDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgDelete.setStatus(_A)
_VlanNewCfgStg_Type=Integer32
_VlanNewCfgStg_Object=MibTableColumn
vlanNewCfgStg=_VlanNewCfgStg_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,1,3,1,9),_VlanNewCfgStg_Type())
vlanNewCfgStg.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgStg.setStatus(_A)
_Trunkgroup_ObjectIdentity=ObjectIdentity
trunkgroup=_Trunkgroup_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,2))
_TrunkGroupTableMaxSize_Type=Integer32
_TrunkGroupTableMaxSize_Object=MibScalar
trunkGroupTableMaxSize=_TrunkGroupTableMaxSize_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,2,1),_TrunkGroupTableMaxSize_Type())
trunkGroupTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupTableMaxSize.setStatus(_A)
_TrunkGroupCurCfgTable_Object=MibTable
trunkGroupCurCfgTable=_TrunkGroupCurCfgTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,2,2))
if mibBuilder.loadTexts:trunkGroupCurCfgTable.setStatus(_A)
_TrunkGroupCurCfgTableEntry_Object=MibTableRow
trunkGroupCurCfgTableEntry=_TrunkGroupCurCfgTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,2,2,1))
trunkGroupCurCfgTableEntry.setIndexNames((0,_F,_c))
if mibBuilder.loadTexts:trunkGroupCurCfgTableEntry.setStatus(_A)
_TrunkGroupCurCfgIndex_Type=Integer32
_TrunkGroupCurCfgIndex_Object=MibTableColumn
trunkGroupCurCfgIndex=_TrunkGroupCurCfgIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,2,2,1,1),_TrunkGroupCurCfgIndex_Type())
trunkGroupCurCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupCurCfgIndex.setStatus(_A)
_TrunkGroupCurCfgPorts_Type=OctetString
_TrunkGroupCurCfgPorts_Object=MibTableColumn
trunkGroupCurCfgPorts=_TrunkGroupCurCfgPorts_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,2,2,1,2),_TrunkGroupCurCfgPorts_Type())
trunkGroupCurCfgPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupCurCfgPorts.setStatus(_A)
class _TrunkGroupCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_TrunkGroupCurCfgState_Type.__name__=_C
_TrunkGroupCurCfgState_Object=MibTableColumn
trunkGroupCurCfgState=_TrunkGroupCurCfgState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,2,2,1,3),_TrunkGroupCurCfgState_Type())
trunkGroupCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupCurCfgState.setStatus(_A)
_TrunkGroupNewCfgTable_Object=MibTable
trunkGroupNewCfgTable=_TrunkGroupNewCfgTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,2,3))
if mibBuilder.loadTexts:trunkGroupNewCfgTable.setStatus(_A)
_TrunkGroupNewCfgTableEntry_Object=MibTableRow
trunkGroupNewCfgTableEntry=_TrunkGroupNewCfgTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,2,3,1))
trunkGroupNewCfgTableEntry.setIndexNames((0,_F,_d))
if mibBuilder.loadTexts:trunkGroupNewCfgTableEntry.setStatus(_A)
_TrunkGroupNewCfgIndex_Type=Integer32
_TrunkGroupNewCfgIndex_Object=MibTableColumn
trunkGroupNewCfgIndex=_TrunkGroupNewCfgIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,2,3,1,1),_TrunkGroupNewCfgIndex_Type())
trunkGroupNewCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupNewCfgIndex.setStatus(_A)
_TrunkGroupNewCfgPorts_Type=OctetString
_TrunkGroupNewCfgPorts_Object=MibTableColumn
trunkGroupNewCfgPorts=_TrunkGroupNewCfgPorts_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,2,3,1,2),_TrunkGroupNewCfgPorts_Type())
trunkGroupNewCfgPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupNewCfgPorts.setStatus(_A)
_TrunkGroupNewCfgAddPort_Type=Integer32
_TrunkGroupNewCfgAddPort_Object=MibTableColumn
trunkGroupNewCfgAddPort=_TrunkGroupNewCfgAddPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,2,3,1,3),_TrunkGroupNewCfgAddPort_Type())
trunkGroupNewCfgAddPort.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkGroupNewCfgAddPort.setStatus(_A)
_TrunkGroupNewCfgRemovePort_Type=Integer32
_TrunkGroupNewCfgRemovePort_Object=MibTableColumn
trunkGroupNewCfgRemovePort=_TrunkGroupNewCfgRemovePort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,2,3,1,4),_TrunkGroupNewCfgRemovePort_Type())
trunkGroupNewCfgRemovePort.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkGroupNewCfgRemovePort.setStatus(_A)
class _TrunkGroupNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_TrunkGroupNewCfgState_Type.__name__=_C
_TrunkGroupNewCfgState_Object=MibTableColumn
trunkGroupNewCfgState=_TrunkGroupNewCfgState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,2,3,1,5),_TrunkGroupNewCfgState_Type())
trunkGroupNewCfgState.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkGroupNewCfgState.setStatus(_A)
class _TrunkGroupNewCfgDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_TrunkGroupNewCfgDelete_Type.__name__=_C
_TrunkGroupNewCfgDelete_Object=MibTableColumn
trunkGroupNewCfgDelete=_TrunkGroupNewCfgDelete_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,2,3,1,6),_TrunkGroupNewCfgDelete_Type())
trunkGroupNewCfgDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkGroupNewCfgDelete.setStatus(_A)
_StgCfg_ObjectIdentity=ObjectIdentity
stgCfg=_StgCfg_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3))
_StgCurCfgTable_Object=MibTable
stgCurCfgTable=_StgCurCfgTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,1))
if mibBuilder.loadTexts:stgCurCfgTable.setStatus(_A)
_StgCurCfgTableEntry_Object=MibTableRow
stgCurCfgTableEntry=_StgCurCfgTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,1,1))
stgCurCfgTableEntry.setIndexNames((0,_F,_e))
if mibBuilder.loadTexts:stgCurCfgTableEntry.setStatus(_A)
_StgCurCfgIndex_Type=Integer32
_StgCurCfgIndex_Object=MibTableColumn
stgCurCfgIndex=_StgCurCfgIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,1,1,1),_StgCurCfgIndex_Type())
stgCurCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgIndex.setStatus(_A)
class _StgCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_I,2)))
_StgCurCfgState_Type.__name__=_C
_StgCurCfgState_Object=MibTableColumn
stgCurCfgState=_StgCurCfgState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,1,1,2),_StgCurCfgState_Type())
stgCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgState.setStatus(_A)
class _StgCurCfgVlanBmap1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_StgCurCfgVlanBmap1_Type.__name__=_M
_StgCurCfgVlanBmap1_Object=MibTableColumn
stgCurCfgVlanBmap1=_StgCurCfgVlanBmap1_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,1,1,3),_StgCurCfgVlanBmap1_Type())
stgCurCfgVlanBmap1.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgVlanBmap1.setStatus(_V)
class _StgCurCfgVlanBmap2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_StgCurCfgVlanBmap2_Type.__name__=_M
_StgCurCfgVlanBmap2_Object=MibTableColumn
stgCurCfgVlanBmap2=_StgCurCfgVlanBmap2_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,1,1,4),_StgCurCfgVlanBmap2_Type())
stgCurCfgVlanBmap2.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgVlanBmap2.setStatus(_V)
class _StgCurCfgPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StgCurCfgPriority_Type.__name__=_C
_StgCurCfgPriority_Object=MibTableColumn
stgCurCfgPriority=_StgCurCfgPriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,1,1,5),_StgCurCfgPriority_Type())
stgCurCfgPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPriority.setStatus(_A)
class _StgCurCfgBrgHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_StgCurCfgBrgHelloTime_Type.__name__=_C
_StgCurCfgBrgHelloTime_Object=MibTableColumn
stgCurCfgBrgHelloTime=_StgCurCfgBrgHelloTime_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,1,1,6),_StgCurCfgBrgHelloTime_Type())
stgCurCfgBrgHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgBrgHelloTime.setStatus(_A)
class _StgCurCfgBrgForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_StgCurCfgBrgForwardDelay_Type.__name__=_C
_StgCurCfgBrgForwardDelay_Object=MibTableColumn
stgCurCfgBrgForwardDelay=_StgCurCfgBrgForwardDelay_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,1,1,7),_StgCurCfgBrgForwardDelay_Type())
stgCurCfgBrgForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgBrgForwardDelay.setStatus(_A)
class _StgCurCfgBrgMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_StgCurCfgBrgMaxAge_Type.__name__=_C
_StgCurCfgBrgMaxAge_Object=MibTableColumn
stgCurCfgBrgMaxAge=_StgCurCfgBrgMaxAge_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,1,1,8),_StgCurCfgBrgMaxAge_Type())
stgCurCfgBrgMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgBrgMaxAge.setStatus(_A)
class _StgCurCfgAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StgCurCfgAgingTime_Type.__name__=_C
_StgCurCfgAgingTime_Object=MibTableColumn
stgCurCfgAgingTime=_StgCurCfgAgingTime_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,1,1,9),_StgCurCfgAgingTime_Type())
stgCurCfgAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgAgingTime.setStatus(_A)
class _StgCurCfgVlanBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_StgCurCfgVlanBmap_Type.__name__=_M
_StgCurCfgVlanBmap_Object=MibTableColumn
stgCurCfgVlanBmap=_StgCurCfgVlanBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,1,1,10),_StgCurCfgVlanBmap_Type())
stgCurCfgVlanBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgVlanBmap.setStatus(_A)
_StgNewCfgTable_Object=MibTable
stgNewCfgTable=_StgNewCfgTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,2))
if mibBuilder.loadTexts:stgNewCfgTable.setStatus(_A)
_StgNewCfgTableEntry_Object=MibTableRow
stgNewCfgTableEntry=_StgNewCfgTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,2,1))
stgNewCfgTableEntry.setIndexNames((0,_F,_f))
if mibBuilder.loadTexts:stgNewCfgTableEntry.setStatus(_A)
_StgNewCfgIndex_Type=Integer32
_StgNewCfgIndex_Object=MibTableColumn
stgNewCfgIndex=_StgNewCfgIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,2,1,1),_StgNewCfgIndex_Type())
stgNewCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgNewCfgIndex.setStatus(_A)
class _StgNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_I,2)))
_StgNewCfgState_Type.__name__=_C
_StgNewCfgState_Object=MibTableColumn
stgNewCfgState=_StgNewCfgState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,2,1,2),_StgNewCfgState_Type())
stgNewCfgState.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgState.setStatus(_A)
class _StgNewCfgDefaultCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('default-config',1))
_StgNewCfgDefaultCfg_Type.__name__=_C
_StgNewCfgDefaultCfg_Object=MibTableColumn
stgNewCfgDefaultCfg=_StgNewCfgDefaultCfg_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,2,1,3),_StgNewCfgDefaultCfg_Type())
stgNewCfgDefaultCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgDefaultCfg.setStatus(_A)
_StgNewCfgAddVlan_Type=Integer32
_StgNewCfgAddVlan_Object=MibTableColumn
stgNewCfgAddVlan=_StgNewCfgAddVlan_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,2,1,4),_StgNewCfgAddVlan_Type())
stgNewCfgAddVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgAddVlan.setStatus(_A)
_StgNewCfgRemoveVlan_Type=Integer32
_StgNewCfgRemoveVlan_Object=MibTableColumn
stgNewCfgRemoveVlan=_StgNewCfgRemoveVlan_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,2,1,5),_StgNewCfgRemoveVlan_Type())
stgNewCfgRemoveVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgRemoveVlan.setStatus(_A)
class _StgNewCfgVlanBmap1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_StgNewCfgVlanBmap1_Type.__name__=_M
_StgNewCfgVlanBmap1_Object=MibTableColumn
stgNewCfgVlanBmap1=_StgNewCfgVlanBmap1_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,2,1,6),_StgNewCfgVlanBmap1_Type())
stgNewCfgVlanBmap1.setMaxAccess(_B)
if mibBuilder.loadTexts:stgNewCfgVlanBmap1.setStatus(_V)
class _StgNewCfgVlanBmap2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_StgNewCfgVlanBmap2_Type.__name__=_M
_StgNewCfgVlanBmap2_Object=MibTableColumn
stgNewCfgVlanBmap2=_StgNewCfgVlanBmap2_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,2,1,7),_StgNewCfgVlanBmap2_Type())
stgNewCfgVlanBmap2.setMaxAccess(_B)
if mibBuilder.loadTexts:stgNewCfgVlanBmap2.setStatus(_V)
class _StgNewCfgPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StgNewCfgPriority_Type.__name__=_C
_StgNewCfgPriority_Object=MibTableColumn
stgNewCfgPriority=_StgNewCfgPriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,2,1,8),_StgNewCfgPriority_Type())
stgNewCfgPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgPriority.setStatus(_A)
class _StgNewCfgBrgHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_StgNewCfgBrgHelloTime_Type.__name__=_C
_StgNewCfgBrgHelloTime_Object=MibTableColumn
stgNewCfgBrgHelloTime=_StgNewCfgBrgHelloTime_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,2,1,9),_StgNewCfgBrgHelloTime_Type())
stgNewCfgBrgHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgBrgHelloTime.setStatus(_A)
class _StgNewCfgBrgForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_StgNewCfgBrgForwardDelay_Type.__name__=_C
_StgNewCfgBrgForwardDelay_Object=MibTableColumn
stgNewCfgBrgForwardDelay=_StgNewCfgBrgForwardDelay_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,2,1,10),_StgNewCfgBrgForwardDelay_Type())
stgNewCfgBrgForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgBrgForwardDelay.setStatus(_A)
class _StgNewCfgBrgMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_StgNewCfgBrgMaxAge_Type.__name__=_C
_StgNewCfgBrgMaxAge_Object=MibTableColumn
stgNewCfgBrgMaxAge=_StgNewCfgBrgMaxAge_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,2,1,11),_StgNewCfgBrgMaxAge_Type())
stgNewCfgBrgMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgBrgMaxAge.setStatus(_A)
class _StgNewCfgAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StgNewCfgAgingTime_Type.__name__=_C
_StgNewCfgAgingTime_Object=MibTableColumn
stgNewCfgAgingTime=_StgNewCfgAgingTime_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,2,1,12),_StgNewCfgAgingTime_Type())
stgNewCfgAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgAgingTime.setStatus(_A)
class _StgNewCfgVlanBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_StgNewCfgVlanBmap_Type.__name__=_M
_StgNewCfgVlanBmap_Object=MibTableColumn
stgNewCfgVlanBmap=_StgNewCfgVlanBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,2,1,13),_StgNewCfgVlanBmap_Type())
stgNewCfgVlanBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:stgNewCfgVlanBmap.setStatus(_A)
_StgCurCfgPortTable_Object=MibTable
stgCurCfgPortTable=_StgCurCfgPortTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,3))
if mibBuilder.loadTexts:stgCurCfgPortTable.setStatus(_A)
_StgCurCfgPortTableEntry_Object=MibTableRow
stgCurCfgPortTableEntry=_StgCurCfgPortTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,3,1))
stgCurCfgPortTableEntry.setIndexNames((0,_F,_g),(0,_F,_h))
if mibBuilder.loadTexts:stgCurCfgPortTableEntry.setStatus(_A)
_StgCurCfgStgIndex_Type=Integer32
_StgCurCfgStgIndex_Object=MibTableColumn
stgCurCfgStgIndex=_StgCurCfgStgIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,3,1,1),_StgCurCfgStgIndex_Type())
stgCurCfgStgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgStgIndex.setStatus(_A)
_StgCurCfgPortIndex_Type=Integer32
_StgCurCfgPortIndex_Object=MibTableColumn
stgCurCfgPortIndex=_StgCurCfgPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,3,1,2),_StgCurCfgPortIndex_Type())
stgCurCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPortIndex.setStatus(_A)
class _StgCurCfgPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_I,2)))
_StgCurCfgPortState_Type.__name__=_C
_StgCurCfgPortState_Object=MibTableColumn
stgCurCfgPortState=_StgCurCfgPortState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,3,1,3),_StgCurCfgPortState_Type())
stgCurCfgPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPortState.setStatus(_A)
class _StgCurCfgPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_StgCurCfgPortPriority_Type.__name__=_C
_StgCurCfgPortPriority_Object=MibTableColumn
stgCurCfgPortPriority=_StgCurCfgPortPriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,3,1,4),_StgCurCfgPortPriority_Type())
stgCurCfgPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPortPriority.setStatus(_A)
class _StgCurCfgPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StgCurCfgPortPathCost_Type.__name__=_C
_StgCurCfgPortPathCost_Object=MibTableColumn
stgCurCfgPortPathCost=_StgCurCfgPortPathCost_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,3,1,5),_StgCurCfgPortPathCost_Type())
stgCurCfgPortPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPortPathCost.setStatus(_A)
class _StgCurCfgPortLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_R,2),(_S,3)))
_StgCurCfgPortLink_Type.__name__=_C
_StgCurCfgPortLink_Object=MibTableColumn
stgCurCfgPortLink=_StgCurCfgPortLink_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,3,1,6),_StgCurCfgPortLink_Type())
stgCurCfgPortLink.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPortLink.setStatus(_A)
class _StgCurCfgPortEdge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_StgCurCfgPortEdge_Type.__name__=_C
_StgCurCfgPortEdge_Object=MibTableColumn
stgCurCfgPortEdge=_StgCurCfgPortEdge_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,3,1,7),_StgCurCfgPortEdge_Type())
stgCurCfgPortEdge.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPortEdge.setStatus(_A)
class _StgCurCfgPortFastFwd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_StgCurCfgPortFastFwd_Type.__name__=_C
_StgCurCfgPortFastFwd_Object=MibTableColumn
stgCurCfgPortFastFwd=_StgCurCfgPortFastFwd_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,3,1,8),_StgCurCfgPortFastFwd_Type())
stgCurCfgPortFastFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPortFastFwd.setStatus(_A)
_StgNewCfgPortTable_Object=MibTable
stgNewCfgPortTable=_StgNewCfgPortTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,4))
if mibBuilder.loadTexts:stgNewCfgPortTable.setStatus(_A)
_StgNewCfgPortTableEntry_Object=MibTableRow
stgNewCfgPortTableEntry=_StgNewCfgPortTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,4,1))
stgNewCfgPortTableEntry.setIndexNames((0,_F,_i),(0,_F,_j))
if mibBuilder.loadTexts:stgNewCfgPortTableEntry.setStatus(_A)
_StgNewCfgStgIndex_Type=Integer32
_StgNewCfgStgIndex_Object=MibTableColumn
stgNewCfgStgIndex=_StgNewCfgStgIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,4,1,1),_StgNewCfgStgIndex_Type())
stgNewCfgStgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgNewCfgStgIndex.setStatus(_A)
_StgNewCfgPortIndex_Type=Integer32
_StgNewCfgPortIndex_Object=MibTableColumn
stgNewCfgPortIndex=_StgNewCfgPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,4,1,2),_StgNewCfgPortIndex_Type())
stgNewCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgNewCfgPortIndex.setStatus(_A)
class _StgNewCfgPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_I,2)))
_StgNewCfgPortState_Type.__name__=_C
_StgNewCfgPortState_Object=MibTableColumn
stgNewCfgPortState=_StgNewCfgPortState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,4,1,3),_StgNewCfgPortState_Type())
stgNewCfgPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgPortState.setStatus(_A)
class _StgNewCfgPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_StgNewCfgPortPriority_Type.__name__=_C
_StgNewCfgPortPriority_Object=MibTableColumn
stgNewCfgPortPriority=_StgNewCfgPortPriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,4,1,4),_StgNewCfgPortPriority_Type())
stgNewCfgPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgPortPriority.setStatus(_A)
class _StgNewCfgPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StgNewCfgPortPathCost_Type.__name__=_C
_StgNewCfgPortPathCost_Object=MibTableColumn
stgNewCfgPortPathCost=_StgNewCfgPortPathCost_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,4,1,5),_StgNewCfgPortPathCost_Type())
stgNewCfgPortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgPortPathCost.setStatus(_A)
class _StgNewCfgPortLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_R,2),(_S,3)))
_StgNewCfgPortLink_Type.__name__=_C
_StgNewCfgPortLink_Object=MibTableColumn
stgNewCfgPortLink=_StgNewCfgPortLink_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,4,1,6),_StgNewCfgPortLink_Type())
stgNewCfgPortLink.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgPortLink.setStatus(_A)
class _StgNewCfgPortEdge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_StgNewCfgPortEdge_Type.__name__=_C
_StgNewCfgPortEdge_Object=MibTableColumn
stgNewCfgPortEdge=_StgNewCfgPortEdge_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,4,1,7),_StgNewCfgPortEdge_Type())
stgNewCfgPortEdge.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgPortEdge.setStatus(_A)
class _StgNewCfgPortFastFwd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_StgNewCfgPortFastFwd_Type.__name__=_C
_StgNewCfgPortFastFwd_Object=MibTableColumn
stgNewCfgPortFastFwd=_StgNewCfgPortFastFwd_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,3,4,1,8),_StgNewCfgPortFastFwd_Type())
stgNewCfgPortFastFwd.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgPortFastFwd.setStatus(_A)
_Mirroring_ObjectIdentity=ObjectIdentity
mirroring=_Mirroring_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,4))
_MirrPortMirr_ObjectIdentity=ObjectIdentity
mirrPortMirr=_MirrPortMirr_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,4,1))
class _PmCurCfgPortMirrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_PmCurCfgPortMirrState_Type.__name__=_C
_PmCurCfgPortMirrState_Object=MibScalar
pmCurCfgPortMirrState=_PmCurCfgPortMirrState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,4,1,1),_PmCurCfgPortMirrState_Type())
pmCurCfgPortMirrState.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgPortMirrState.setStatus(_A)
class _PmNewCfgPortMirrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_PmNewCfgPortMirrState_Type.__name__=_C
_PmNewCfgPortMirrState_Object=MibScalar
pmNewCfgPortMirrState=_PmNewCfgPortMirrState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,4,1,2),_PmNewCfgPortMirrState_Type())
pmNewCfgPortMirrState.setMaxAccess(_E)
if mibBuilder.loadTexts:pmNewCfgPortMirrState.setStatus(_A)
_PmCurCfgPortMonitorTable_Object=MibTable
pmCurCfgPortMonitorTable=_PmCurCfgPortMonitorTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,4,1,3))
if mibBuilder.loadTexts:pmCurCfgPortMonitorTable.setStatus(_A)
_PmCurCfgPortMonitorEntry_Object=MibTableRow
pmCurCfgPortMonitorEntry=_PmCurCfgPortMonitorEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,4,1,3,1))
pmCurCfgPortMonitorEntry.setIndexNames((0,_F,_k),(0,_F,_l))
if mibBuilder.loadTexts:pmCurCfgPortMonitorEntry.setStatus(_A)
_PmCurCfgPmirrMoniPortIndex_Type=Integer32
_PmCurCfgPmirrMoniPortIndex_Object=MibTableColumn
pmCurCfgPmirrMoniPortIndex=_PmCurCfgPmirrMoniPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,4,1,3,1,1),_PmCurCfgPmirrMoniPortIndex_Type())
pmCurCfgPmirrMoniPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgPmirrMoniPortIndex.setStatus(_A)
_PmCurCfgPmirrMirrPortIndex_Type=Integer32
_PmCurCfgPmirrMirrPortIndex_Object=MibTableColumn
pmCurCfgPmirrMirrPortIndex=_PmCurCfgPmirrMirrPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,4,1,3,1,2),_PmCurCfgPmirrMirrPortIndex_Type())
pmCurCfgPmirrMirrPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgPmirrMirrPortIndex.setStatus(_A)
class _PmCurCfgPmirrDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('in',1),('out',2),(_X,3)))
_PmCurCfgPmirrDirection_Type.__name__=_C
_PmCurCfgPmirrDirection_Object=MibTableColumn
pmCurCfgPmirrDirection=_PmCurCfgPmirrDirection_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,4,1,3,1,3),_PmCurCfgPmirrDirection_Type())
pmCurCfgPmirrDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgPmirrDirection.setStatus(_A)
_PmNewCfgPortMonitorTable_Object=MibTable
pmNewCfgPortMonitorTable=_PmNewCfgPortMonitorTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,4,1,4))
if mibBuilder.loadTexts:pmNewCfgPortMonitorTable.setStatus(_A)
_PmNewCfgPortMonitorEntry_Object=MibTableRow
pmNewCfgPortMonitorEntry=_PmNewCfgPortMonitorEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,4,1,4,1))
pmNewCfgPortMonitorEntry.setIndexNames((0,_F,_m),(0,_F,_n))
if mibBuilder.loadTexts:pmNewCfgPortMonitorEntry.setStatus(_A)
_PmNewCfgPmirrMoniPortIndex_Type=Integer32
_PmNewCfgPmirrMoniPortIndex_Object=MibTableColumn
pmNewCfgPmirrMoniPortIndex=_PmNewCfgPmirrMoniPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,4,1,4,1,1),_PmNewCfgPmirrMoniPortIndex_Type())
pmNewCfgPmirrMoniPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmNewCfgPmirrMoniPortIndex.setStatus(_A)
_PmNewCfgPmirrMirrPortIndex_Type=Integer32
_PmNewCfgPmirrMirrPortIndex_Object=MibTableColumn
pmNewCfgPmirrMirrPortIndex=_PmNewCfgPmirrMirrPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,4,1,4,1,2),_PmNewCfgPmirrMirrPortIndex_Type())
pmNewCfgPmirrMirrPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmNewCfgPmirrMirrPortIndex.setStatus(_A)
class _PmNewCfgPmirrDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('in',1),('out',2),(_X,3)))
_PmNewCfgPmirrDirection_Type.__name__=_C
_PmNewCfgPmirrDirection_Object=MibTableColumn
pmNewCfgPmirrDirection=_PmNewCfgPmirrDirection_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,4,1,4,1,3),_PmNewCfgPmirrDirection_Type())
pmNewCfgPmirrDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgPmirrDirection.setStatus(_A)
class _PmNewCfgPmirrDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_PmNewCfgPmirrDelete_Type.__name__=_C
_PmNewCfgPmirrDelete_Object=MibTableColumn
pmNewCfgPmirrDelete=_PmNewCfgPmirrDelete_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,4,1,4,1,4),_PmNewCfgPmirrDelete_Type())
pmNewCfgPmirrDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgPmirrDelete.setStatus(_A)
class _PmNewCfgPmonDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_PmNewCfgPmonDelete_Type.__name__=_C
_PmNewCfgPmonDelete_Object=MibTableColumn
pmNewCfgPmonDelete=_PmNewCfgPmonDelete_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,4,1,4,1,10),_PmNewCfgPmonDelete_Type())
pmNewCfgPmonDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgPmonDelete.setStatus(_A)
_MstCfg_ObjectIdentity=ObjectIdentity
mstCfg=_MstCfg_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5))
_MstGeneralCfg_ObjectIdentity=ObjectIdentity
mstGeneralCfg=_MstGeneralCfg_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,1))
class _MstCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_G,3)))
_MstCurCfgState_Type.__name__=_C
_MstCurCfgState_Object=MibScalar
mstCurCfgState=_MstCurCfgState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,1,1),_MstCurCfgState_Type())
mstCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCurCfgState.setStatus(_A)
class _MstNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_G,3)))
_MstNewCfgState_Type.__name__=_C
_MstNewCfgState_Object=MibScalar
mstNewCfgState=_MstNewCfgState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,1,2),_MstNewCfgState_Type())
mstNewCfgState.setMaxAccess(_E)
if mibBuilder.loadTexts:mstNewCfgState.setStatus(_A)
class _MstCurCfgRegionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MstCurCfgRegionName_Type.__name__=_O
_MstCurCfgRegionName_Object=MibScalar
mstCurCfgRegionName=_MstCurCfgRegionName_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,1,3),_MstCurCfgRegionName_Type())
mstCurCfgRegionName.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCurCfgRegionName.setStatus(_A)
class _MstNewCfgRegionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MstNewCfgRegionName_Type.__name__=_O
_MstNewCfgRegionName_Object=MibScalar
mstNewCfgRegionName=_MstNewCfgRegionName_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,1,4),_MstNewCfgRegionName_Type())
mstNewCfgRegionName.setMaxAccess(_E)
if mibBuilder.loadTexts:mstNewCfgRegionName.setStatus(_A)
class _MstCurCfgRegionVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MstCurCfgRegionVersion_Type.__name__=_C
_MstCurCfgRegionVersion_Object=MibScalar
mstCurCfgRegionVersion=_MstCurCfgRegionVersion_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,1,5),_MstCurCfgRegionVersion_Type())
mstCurCfgRegionVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCurCfgRegionVersion.setStatus(_A)
class _MstNewCfgRegionVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MstNewCfgRegionVersion_Type.__name__=_C
_MstNewCfgRegionVersion_Object=MibScalar
mstNewCfgRegionVersion=_MstNewCfgRegionVersion_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,1,6),_MstNewCfgRegionVersion_Type())
mstNewCfgRegionVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:mstNewCfgRegionVersion.setStatus(_A)
class _MstCurCfgMaxHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,60))
_MstCurCfgMaxHopCount_Type.__name__=_C
_MstCurCfgMaxHopCount_Object=MibScalar
mstCurCfgMaxHopCount=_MstCurCfgMaxHopCount_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,1,7),_MstCurCfgMaxHopCount_Type())
mstCurCfgMaxHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCurCfgMaxHopCount.setStatus(_A)
class _MstNewCfgMaxHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,60))
_MstNewCfgMaxHopCount_Type.__name__=_C
_MstNewCfgMaxHopCount_Object=MibScalar
mstNewCfgMaxHopCount=_MstNewCfgMaxHopCount_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,1,8),_MstNewCfgMaxHopCount_Type())
mstNewCfgMaxHopCount.setMaxAccess(_E)
if mibBuilder.loadTexts:mstNewCfgMaxHopCount.setStatus(_A)
class _MstCurCfgStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mstp',1),('rstp',2)))
_MstCurCfgStpMode_Type.__name__=_C
_MstCurCfgStpMode_Object=MibScalar
mstCurCfgStpMode=_MstCurCfgStpMode_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,1,9),_MstCurCfgStpMode_Type())
mstCurCfgStpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCurCfgStpMode.setStatus(_A)
class _MstNewCfgStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mstp',1),('rstp',2)))
_MstNewCfgStpMode_Type.__name__=_C
_MstNewCfgStpMode_Object=MibScalar
mstNewCfgStpMode=_MstNewCfgStpMode_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,1,10),_MstNewCfgStpMode_Type())
mstNewCfgStpMode.setMaxAccess(_E)
if mibBuilder.loadTexts:mstNewCfgStpMode.setStatus(_A)
_MstCistCfg_ObjectIdentity=ObjectIdentity
mstCistCfg=_MstCistCfg_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2))
class _MstCistDefaultCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('default',1))
_MstCistDefaultCfg_Type.__name__=_C
_MstCistDefaultCfg_Object=MibScalar
mstCistDefaultCfg=_MstCistDefaultCfg_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,1),_MstCistDefaultCfg_Type())
mstCistDefaultCfg.setMaxAccess(_E)
if mibBuilder.loadTexts:mstCistDefaultCfg.setStatus(_A)
_MstCistBridgeCfg_ObjectIdentity=ObjectIdentity
mstCistBridgeCfg=_MstCistBridgeCfg_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,2))
class _MstCistCurCfgBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MstCistCurCfgBridgePriority_Type.__name__=_C
_MstCistCurCfgBridgePriority_Object=MibScalar
mstCistCurCfgBridgePriority=_MstCistCurCfgBridgePriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,2,1),_MstCistCurCfgBridgePriority_Type())
mstCistCurCfgBridgePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgBridgePriority.setStatus(_A)
class _MstCistNewCfgBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MstCistNewCfgBridgePriority_Type.__name__=_C
_MstCistNewCfgBridgePriority_Object=MibScalar
mstCistNewCfgBridgePriority=_MstCistNewCfgBridgePriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,2,2),_MstCistNewCfgBridgePriority_Type())
mstCistNewCfgBridgePriority.setMaxAccess(_E)
if mibBuilder.loadTexts:mstCistNewCfgBridgePriority.setStatus(_A)
class _MstCistCurCfgBridgeMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_MstCistCurCfgBridgeMaxAge_Type.__name__=_C
_MstCistCurCfgBridgeMaxAge_Object=MibScalar
mstCistCurCfgBridgeMaxAge=_MstCistCurCfgBridgeMaxAge_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,2,5),_MstCistCurCfgBridgeMaxAge_Type())
mstCistCurCfgBridgeMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgBridgeMaxAge.setStatus(_A)
class _MstCistNewCfgBridgeMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_MstCistNewCfgBridgeMaxAge_Type.__name__=_C
_MstCistNewCfgBridgeMaxAge_Object=MibScalar
mstCistNewCfgBridgeMaxAge=_MstCistNewCfgBridgeMaxAge_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,2,6),_MstCistNewCfgBridgeMaxAge_Type())
mstCistNewCfgBridgeMaxAge.setMaxAccess(_E)
if mibBuilder.loadTexts:mstCistNewCfgBridgeMaxAge.setStatus(_A)
class _MstCistCurCfgBridgeForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_MstCistCurCfgBridgeForwardDelay_Type.__name__=_C
_MstCistCurCfgBridgeForwardDelay_Object=MibScalar
mstCistCurCfgBridgeForwardDelay=_MstCistCurCfgBridgeForwardDelay_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,2,7),_MstCistCurCfgBridgeForwardDelay_Type())
mstCistCurCfgBridgeForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgBridgeForwardDelay.setStatus(_A)
class _MstCistNewCfgBridgeForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_MstCistNewCfgBridgeForwardDelay_Type.__name__=_C
_MstCistNewCfgBridgeForwardDelay_Object=MibScalar
mstCistNewCfgBridgeForwardDelay=_MstCistNewCfgBridgeForwardDelay_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,2,8),_MstCistNewCfgBridgeForwardDelay_Type())
mstCistNewCfgBridgeForwardDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:mstCistNewCfgBridgeForwardDelay.setStatus(_A)
class _MstCistCurCfgVlanBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_MstCistCurCfgVlanBmap_Type.__name__=_M
_MstCistCurCfgVlanBmap_Object=MibScalar
mstCistCurCfgVlanBmap=_MstCistCurCfgVlanBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,2,9),_MstCistCurCfgVlanBmap_Type())
mstCistCurCfgVlanBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgVlanBmap.setStatus(_A)
class _MstCistNewCfgVlanBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_MstCistNewCfgVlanBmap_Type.__name__=_M
_MstCistNewCfgVlanBmap_Object=MibScalar
mstCistNewCfgVlanBmap=_MstCistNewCfgVlanBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,2,10),_MstCistNewCfgVlanBmap_Type())
mstCistNewCfgVlanBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistNewCfgVlanBmap.setStatus(_A)
_MstCistNewCfgAddVlan_Type=Integer32
_MstCistNewCfgAddVlan_Object=MibScalar
mstCistNewCfgAddVlan=_MstCistNewCfgAddVlan_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,2,11),_MstCistNewCfgAddVlan_Type())
mstCistNewCfgAddVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:mstCistNewCfgAddVlan.setStatus(_A)
_MstCistCurCfgPortTable_Object=MibTable
mstCistCurCfgPortTable=_MstCistCurCfgPortTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,3))
if mibBuilder.loadTexts:mstCistCurCfgPortTable.setStatus(_A)
_MstCistCurCfgPortTableEntry_Object=MibTableRow
mstCistCurCfgPortTableEntry=_MstCistCurCfgPortTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,3,1))
mstCistCurCfgPortTableEntry.setIndexNames((0,_F,_o))
if mibBuilder.loadTexts:mstCistCurCfgPortTableEntry.setStatus(_A)
_MstCistCurCfgPortIndex_Type=Integer32
_MstCistCurCfgPortIndex_Object=MibTableColumn
mstCistCurCfgPortIndex=_MstCistCurCfgPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,3,1,1),_MstCistCurCfgPortIndex_Type())
mstCistCurCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgPortIndex.setStatus(_A)
class _MstCistCurCfgPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_MstCistCurCfgPortPriority_Type.__name__=_C
_MstCistCurCfgPortPriority_Object=MibTableColumn
mstCistCurCfgPortPriority=_MstCistCurCfgPortPriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,3,1,2),_MstCistCurCfgPortPriority_Type())
mstCistCurCfgPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgPortPriority.setStatus(_A)
class _MstCistCurCfgPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_MstCistCurCfgPortPathCost_Type.__name__=_C
_MstCistCurCfgPortPathCost_Object=MibTableColumn
mstCistCurCfgPortPathCost=_MstCistCurCfgPortPathCost_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,3,1,3),_MstCistCurCfgPortPathCost_Type())
mstCistCurCfgPortPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgPortPathCost.setStatus(_A)
class _MstCistCurCfgPortLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_R,2),(_S,3)))
_MstCistCurCfgPortLinkType_Type.__name__=_C
_MstCistCurCfgPortLinkType_Object=MibTableColumn
mstCistCurCfgPortLinkType=_MstCistCurCfgPortLinkType_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,3,1,4),_MstCistCurCfgPortLinkType_Type())
mstCistCurCfgPortLinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgPortLinkType.setStatus(_A)
class _MstCistCurCfgPortEdge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_MstCistCurCfgPortEdge_Type.__name__=_C
_MstCistCurCfgPortEdge_Object=MibTableColumn
mstCistCurCfgPortEdge=_MstCistCurCfgPortEdge_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,3,1,5),_MstCistCurCfgPortEdge_Type())
mstCistCurCfgPortEdge.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgPortEdge.setStatus(_A)
class _MstCistCurCfgPortStpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_I,2)))
_MstCistCurCfgPortStpState_Type.__name__=_C
_MstCistCurCfgPortStpState_Object=MibTableColumn
mstCistCurCfgPortStpState=_MstCistCurCfgPortStpState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,3,1,6),_MstCistCurCfgPortStpState_Type())
mstCistCurCfgPortStpState.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgPortStpState.setStatus(_A)
class _MstCistCurCfgPortHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_MstCistCurCfgPortHelloTime_Type.__name__=_C
_MstCistCurCfgPortHelloTime_Object=MibTableColumn
mstCistCurCfgPortHelloTime=_MstCistCurCfgPortHelloTime_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,3,1,7),_MstCistCurCfgPortHelloTime_Type())
mstCistCurCfgPortHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgPortHelloTime.setStatus(_A)
_MstCistNewCfgPortTable_Object=MibTable
mstCistNewCfgPortTable=_MstCistNewCfgPortTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,4))
if mibBuilder.loadTexts:mstCistNewCfgPortTable.setStatus(_A)
_MstCistNewCfgPortTableEntry_Object=MibTableRow
mstCistNewCfgPortTableEntry=_MstCistNewCfgPortTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,4,1))
mstCistNewCfgPortTableEntry.setIndexNames((0,_F,_p))
if mibBuilder.loadTexts:mstCistNewCfgPortTableEntry.setStatus(_A)
_MstCistNewCfgPortIndex_Type=Integer32
_MstCistNewCfgPortIndex_Object=MibTableColumn
mstCistNewCfgPortIndex=_MstCistNewCfgPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,4,1,1),_MstCistNewCfgPortIndex_Type())
mstCistNewCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistNewCfgPortIndex.setStatus(_A)
class _MstCistNewCfgPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_MstCistNewCfgPortPriority_Type.__name__=_C
_MstCistNewCfgPortPriority_Object=MibTableColumn
mstCistNewCfgPortPriority=_MstCistNewCfgPortPriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,4,1,2),_MstCistNewCfgPortPriority_Type())
mstCistNewCfgPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:mstCistNewCfgPortPriority.setStatus(_A)
class _MstCistNewCfgPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_MstCistNewCfgPortPathCost_Type.__name__=_C
_MstCistNewCfgPortPathCost_Object=MibTableColumn
mstCistNewCfgPortPathCost=_MstCistNewCfgPortPathCost_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,4,1,3),_MstCistNewCfgPortPathCost_Type())
mstCistNewCfgPortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:mstCistNewCfgPortPathCost.setStatus(_A)
class _MstCistNewCfgPortLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_R,2),(_S,3)))
_MstCistNewCfgPortLinkType_Type.__name__=_C
_MstCistNewCfgPortLinkType_Object=MibTableColumn
mstCistNewCfgPortLinkType=_MstCistNewCfgPortLinkType_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,4,1,4),_MstCistNewCfgPortLinkType_Type())
mstCistNewCfgPortLinkType.setMaxAccess(_D)
if mibBuilder.loadTexts:mstCistNewCfgPortLinkType.setStatus(_A)
class _MstCistNewCfgPortEdge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_MstCistNewCfgPortEdge_Type.__name__=_C
_MstCistNewCfgPortEdge_Object=MibTableColumn
mstCistNewCfgPortEdge=_MstCistNewCfgPortEdge_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,4,1,5),_MstCistNewCfgPortEdge_Type())
mstCistNewCfgPortEdge.setMaxAccess(_D)
if mibBuilder.loadTexts:mstCistNewCfgPortEdge.setStatus(_A)
class _MstCistNewCfgPortStpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_I,2)))
_MstCistNewCfgPortStpState_Type.__name__=_C
_MstCistNewCfgPortStpState_Object=MibTableColumn
mstCistNewCfgPortStpState=_MstCistNewCfgPortStpState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,4,1,6),_MstCistNewCfgPortStpState_Type())
mstCistNewCfgPortStpState.setMaxAccess(_D)
if mibBuilder.loadTexts:mstCistNewCfgPortStpState.setStatus(_A)
class _MstCistNewCfgPortHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_MstCistNewCfgPortHelloTime_Type.__name__=_C
_MstCistNewCfgPortHelloTime_Object=MibTableColumn
mstCistNewCfgPortHelloTime=_MstCistNewCfgPortHelloTime_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,5,2,4,1,7),_MstCistNewCfgPortHelloTime_Type())
mstCistNewCfgPortHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mstCistNewCfgPortHelloTime.setStatus(_A)
_Lacp_ObjectIdentity=ObjectIdentity
lacp=_Lacp_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6))
class _LacpCurSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LacpCurSystemPriority_Type.__name__=_C
_LacpCurSystemPriority_Object=MibScalar
lacpCurSystemPriority=_LacpCurSystemPriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6,1),_LacpCurSystemPriority_Type())
lacpCurSystemPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpCurSystemPriority.setStatus(_A)
class _LacpNewSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LacpNewSystemPriority_Type.__name__=_C
_LacpNewSystemPriority_Object=MibScalar
lacpNewSystemPriority=_LacpNewSystemPriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6,2),_LacpNewSystemPriority_Type())
lacpNewSystemPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:lacpNewSystemPriority.setStatus(_A)
class _LacpCurSystemTimeoutTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,90)));namedValues=NamedValues(*(('short',3),('long',90)))
_LacpCurSystemTimeoutTime_Type.__name__=_C
_LacpCurSystemTimeoutTime_Object=MibScalar
lacpCurSystemTimeoutTime=_LacpCurSystemTimeoutTime_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6,5),_LacpCurSystemTimeoutTime_Type())
lacpCurSystemTimeoutTime.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpCurSystemTimeoutTime.setStatus(_A)
class _LacpNewSystemTimeoutTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,90)));namedValues=NamedValues(*(('short',3),('long',90)))
_LacpNewSystemTimeoutTime_Type.__name__=_C
_LacpNewSystemTimeoutTime_Object=MibScalar
lacpNewSystemTimeoutTime=_LacpNewSystemTimeoutTime_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6,6),_LacpNewSystemTimeoutTime_Type())
lacpNewSystemTimeoutTime.setMaxAccess(_E)
if mibBuilder.loadTexts:lacpNewSystemTimeoutTime.setStatus(_A)
_LacpCurPortCfgTable_Object=MibTable
lacpCurPortCfgTable=_LacpCurPortCfgTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6,7))
if mibBuilder.loadTexts:lacpCurPortCfgTable.setStatus(_A)
_LacpCurPortCfgTableEntry_Object=MibTableRow
lacpCurPortCfgTableEntry=_LacpCurPortCfgTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6,7,1))
lacpCurPortCfgTableEntry.setIndexNames((0,_F,_q))
if mibBuilder.loadTexts:lacpCurPortCfgTableEntry.setStatus(_A)
_LacpCurPortCfgTableId_Type=Integer32
_LacpCurPortCfgTableId_Object=MibTableColumn
lacpCurPortCfgTableId=_LacpCurPortCfgTableId_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6,7,1,1),_LacpCurPortCfgTableId_Type())
lacpCurPortCfgTableId.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpCurPortCfgTableId.setStatus(_A)
class _LacpCurPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_r,2),(_s,3)))
_LacpCurPortState_Type.__name__=_C
_LacpCurPortState_Object=MibTableColumn
lacpCurPortState=_LacpCurPortState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6,7,1,2),_LacpCurPortState_Type())
lacpCurPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpCurPortState.setStatus(_A)
class _LacpCurPortActorPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LacpCurPortActorPortPriority_Type.__name__=_C
_LacpCurPortActorPortPriority_Object=MibTableColumn
lacpCurPortActorPortPriority=_LacpCurPortActorPortPriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6,7,1,3),_LacpCurPortActorPortPriority_Type())
lacpCurPortActorPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpCurPortActorPortPriority.setStatus(_A)
class _LacpCurPortActorAdminKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LacpCurPortActorAdminKey_Type.__name__=_C
_LacpCurPortActorAdminKey_Object=MibTableColumn
lacpCurPortActorAdminKey=_LacpCurPortActorAdminKey_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6,7,1,4),_LacpCurPortActorAdminKey_Type())
lacpCurPortActorAdminKey.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpCurPortActorAdminKey.setStatus(_A)
_LacpNewPortCfgTable_Object=MibTable
lacpNewPortCfgTable=_LacpNewPortCfgTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6,8))
if mibBuilder.loadTexts:lacpNewPortCfgTable.setStatus(_A)
_LacpNewPortCfgTableEntry_Object=MibTableRow
lacpNewPortCfgTableEntry=_LacpNewPortCfgTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6,8,1))
lacpNewPortCfgTableEntry.setIndexNames((0,_F,_t))
if mibBuilder.loadTexts:lacpNewPortCfgTableEntry.setStatus(_A)
_LacpNewPortCfgTableId_Type=Integer32
_LacpNewPortCfgTableId_Object=MibTableColumn
lacpNewPortCfgTableId=_LacpNewPortCfgTableId_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6,8,1,1),_LacpNewPortCfgTableId_Type())
lacpNewPortCfgTableId.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpNewPortCfgTableId.setStatus(_A)
class _LacpNewPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_r,2),(_s,3)))
_LacpNewPortState_Type.__name__=_C
_LacpNewPortState_Object=MibTableColumn
lacpNewPortState=_LacpNewPortState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6,8,1,2),_LacpNewPortState_Type())
lacpNewPortState.setMaxAccess(_E)
if mibBuilder.loadTexts:lacpNewPortState.setStatus(_A)
class _LacpNewPortActorPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LacpNewPortActorPortPriority_Type.__name__=_C
_LacpNewPortActorPortPriority_Object=MibTableColumn
lacpNewPortActorPortPriority=_LacpNewPortActorPortPriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6,8,1,3),_LacpNewPortActorPortPriority_Type())
lacpNewPortActorPortPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:lacpNewPortActorPortPriority.setStatus(_A)
class _LacpNewPortActorAdminKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LacpNewPortActorAdminKey_Type.__name__=_C
_LacpNewPortActorAdminKey_Object=MibTableColumn
lacpNewPortActorAdminKey=_LacpNewPortActorAdminKey_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,6,8,1,4),_LacpNewPortActorAdminKey_Type())
lacpNewPortActorAdminKey.setMaxAccess(_E)
if mibBuilder.loadTexts:lacpNewPortActorAdminKey.setStatus(_A)
_Thash_ObjectIdentity=ObjectIdentity
thash=_Thash_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,7))
_ThashL2_ObjectIdentity=ObjectIdentity
thashL2=_ThashL2_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,7,1))
class _L2ThashCurCfgSmacState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_L2ThashCurCfgSmacState_Type.__name__=_C
_L2ThashCurCfgSmacState_Object=MibScalar
l2ThashCurCfgSmacState=_L2ThashCurCfgSmacState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,7,1,1),_L2ThashCurCfgSmacState_Type())
l2ThashCurCfgSmacState.setMaxAccess(_B)
if mibBuilder.loadTexts:l2ThashCurCfgSmacState.setStatus(_A)
class _L2ThashNewCfgSmacState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_L2ThashNewCfgSmacState_Type.__name__=_C
_L2ThashNewCfgSmacState_Object=MibScalar
l2ThashNewCfgSmacState=_L2ThashNewCfgSmacState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,7,1,2),_L2ThashNewCfgSmacState_Type())
l2ThashNewCfgSmacState.setMaxAccess(_E)
if mibBuilder.loadTexts:l2ThashNewCfgSmacState.setStatus(_A)
class _L2ThashCurCfgDmacState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_L2ThashCurCfgDmacState_Type.__name__=_C
_L2ThashCurCfgDmacState_Object=MibScalar
l2ThashCurCfgDmacState=_L2ThashCurCfgDmacState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,7,1,3),_L2ThashCurCfgDmacState_Type())
l2ThashCurCfgDmacState.setMaxAccess(_B)
if mibBuilder.loadTexts:l2ThashCurCfgDmacState.setStatus(_A)
class _L2ThashNewCfgDmacState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_L2ThashNewCfgDmacState_Type.__name__=_C
_L2ThashNewCfgDmacState_Object=MibScalar
l2ThashNewCfgDmacState=_L2ThashNewCfgDmacState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,7,1,4),_L2ThashNewCfgDmacState_Type())
l2ThashNewCfgDmacState.setMaxAccess(_E)
if mibBuilder.loadTexts:l2ThashNewCfgDmacState.setStatus(_A)
class _L2ThashCurCfgSipState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_L2ThashCurCfgSipState_Type.__name__=_C
_L2ThashCurCfgSipState_Object=MibScalar
l2ThashCurCfgSipState=_L2ThashCurCfgSipState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,7,1,5),_L2ThashCurCfgSipState_Type())
l2ThashCurCfgSipState.setMaxAccess(_B)
if mibBuilder.loadTexts:l2ThashCurCfgSipState.setStatus(_A)
class _L2ThashNewCfgSipState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_L2ThashNewCfgSipState_Type.__name__=_C
_L2ThashNewCfgSipState_Object=MibScalar
l2ThashNewCfgSipState=_L2ThashNewCfgSipState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,7,1,6),_L2ThashNewCfgSipState_Type())
l2ThashNewCfgSipState.setMaxAccess(_E)
if mibBuilder.loadTexts:l2ThashNewCfgSipState.setStatus(_A)
class _L2ThashCurCfgDipState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_L2ThashCurCfgDipState_Type.__name__=_C
_L2ThashCurCfgDipState_Object=MibScalar
l2ThashCurCfgDipState=_L2ThashCurCfgDipState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,7,1,7),_L2ThashCurCfgDipState_Type())
l2ThashCurCfgDipState.setMaxAccess(_B)
if mibBuilder.loadTexts:l2ThashCurCfgDipState.setStatus(_A)
class _L2ThashNewCfgDipState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_L2ThashNewCfgDipState_Type.__name__=_C
_L2ThashNewCfgDipState_Object=MibScalar
l2ThashNewCfgDipState=_L2ThashNewCfgDipState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,7,1,8),_L2ThashNewCfgDipState_Type())
l2ThashNewCfgDipState.setMaxAccess(_E)
if mibBuilder.loadTexts:l2ThashNewCfgDipState.setStatus(_A)
_L2GeneralCfg_ObjectIdentity=ObjectIdentity
l2GeneralCfg=_L2GeneralCfg_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,8))
class _UpfastCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_UpfastCurCfgState_Type.__name__=_C
_UpfastCurCfgState_Object=MibScalar
upfastCurCfgState=_UpfastCurCfgState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,8,1),_UpfastCurCfgState_Type())
upfastCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:upfastCurCfgState.setStatus(_A)
class _UpfastNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_UpfastNewCfgState_Type.__name__=_C
_UpfastNewCfgState_Object=MibScalar
upfastNewCfgState=_UpfastNewCfgState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,8,2),_UpfastNewCfgState_Type())
upfastNewCfgState.setMaxAccess(_E)
if mibBuilder.loadTexts:upfastNewCfgState.setStatus(_A)
class _UpdateCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,200))
_UpdateCurCfgState_Type.__name__=_C
_UpdateCurCfgState_Object=MibScalar
updateCurCfgState=_UpdateCurCfgState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,8,3),_UpdateCurCfgState_Type())
updateCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:updateCurCfgState.setStatus(_A)
class _UpdateNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,200))
_UpdateNewCfgState_Type.__name__=_C
_UpdateNewCfgState_Object=MibScalar
updateNewCfgState=_UpdateNewCfgState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,8,4),_UpdateNewCfgState_Type())
updateNewCfgState.setMaxAccess(_E)
if mibBuilder.loadTexts:updateNewCfgState.setStatus(_A)
_Ufd_ObjectIdentity=ObjectIdentity
ufd=_Ufd_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9))
_UfdGeneralCfg_ObjectIdentity=ObjectIdentity
ufdGeneralCfg=_UfdGeneralCfg_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1))
class _UfdCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_UfdCurCfgState_Type.__name__=_C
_UfdCurCfgState_Object=MibScalar
ufdCurCfgState=_UfdCurCfgState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,1),_UfdCurCfgState_Type())
ufdCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:ufdCurCfgState.setStatus(_A)
class _UfdNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_UfdNewCfgState_Type.__name__=_C
_UfdNewCfgState_Object=MibScalar
ufdNewCfgState=_UfdNewCfgState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,2),_UfdNewCfgState_Type())
ufdNewCfgState.setMaxAccess(_E)
if mibBuilder.loadTexts:ufdNewCfgState.setStatus(_A)
_UfdCurCfgLtMPorts_Type=OctetString
_UfdCurCfgLtMPorts_Object=MibScalar
ufdCurCfgLtMPorts=_UfdCurCfgLtMPorts_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,3),_UfdCurCfgLtMPorts_Type())
ufdCurCfgLtMPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:ufdCurCfgLtMPorts.setStatus(_A)
_UfdNewCfgLtMPorts_Type=OctetString
_UfdNewCfgLtMPorts_Object=MibScalar
ufdNewCfgLtMPorts=_UfdNewCfgLtMPorts_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,4),_UfdNewCfgLtMPorts_Type())
ufdNewCfgLtMPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:ufdNewCfgLtMPorts.setStatus(_A)
_UfdCurCfgLtMTrunks_Type=OctetString
_UfdCurCfgLtMTrunks_Object=MibScalar
ufdCurCfgLtMTrunks=_UfdCurCfgLtMTrunks_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,5),_UfdCurCfgLtMTrunks_Type())
ufdCurCfgLtMTrunks.setMaxAccess(_B)
if mibBuilder.loadTexts:ufdCurCfgLtMTrunks.setStatus(_A)
_UfdNewCfgLtMTrunks_Type=OctetString
_UfdNewCfgLtMTrunks_Object=MibScalar
ufdNewCfgLtMTrunks=_UfdNewCfgLtMTrunks_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,6),_UfdNewCfgLtMTrunks_Type())
ufdNewCfgLtMTrunks.setMaxAccess(_E)
if mibBuilder.loadTexts:ufdNewCfgLtMTrunks.setStatus(_A)
_UfdCurCfgLtDPorts_Type=OctetString
_UfdCurCfgLtDPorts_Object=MibScalar
ufdCurCfgLtDPorts=_UfdCurCfgLtDPorts_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,7),_UfdCurCfgLtDPorts_Type())
ufdCurCfgLtDPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:ufdCurCfgLtDPorts.setStatus(_A)
_UfdNewCfgLtDPorts_Type=OctetString
_UfdNewCfgLtDPorts_Object=MibScalar
ufdNewCfgLtDPorts=_UfdNewCfgLtDPorts_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,8),_UfdNewCfgLtDPorts_Type())
ufdNewCfgLtDPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:ufdNewCfgLtDPorts.setStatus(_A)
_UfdCurCfgLtDTrunks_Type=OctetString
_UfdCurCfgLtDTrunks_Object=MibScalar
ufdCurCfgLtDTrunks=_UfdCurCfgLtDTrunks_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,9),_UfdCurCfgLtDTrunks_Type())
ufdCurCfgLtDTrunks.setMaxAccess(_B)
if mibBuilder.loadTexts:ufdCurCfgLtDTrunks.setStatus(_A)
_UfdNewCfgLtDTrunks_Type=OctetString
_UfdNewCfgLtDTrunks_Object=MibScalar
ufdNewCfgLtDTrunks=_UfdNewCfgLtDTrunks_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,10),_UfdNewCfgLtDTrunks_Type())
ufdNewCfgLtDTrunks.setMaxAccess(_E)
if mibBuilder.loadTexts:ufdNewCfgLtDTrunks.setStatus(_A)
_UfdNewCfgAddLtMPort_Type=Integer32
_UfdNewCfgAddLtMPort_Object=MibScalar
ufdNewCfgAddLtMPort=_UfdNewCfgAddLtMPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,11),_UfdNewCfgAddLtMPort_Type())
ufdNewCfgAddLtMPort.setMaxAccess(_E)
if mibBuilder.loadTexts:ufdNewCfgAddLtMPort.setStatus(_A)
_UfdNewCfgRemoveLtMPort_Type=Integer32
_UfdNewCfgRemoveLtMPort_Object=MibScalar
ufdNewCfgRemoveLtMPort=_UfdNewCfgRemoveLtMPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,12),_UfdNewCfgRemoveLtMPort_Type())
ufdNewCfgRemoveLtMPort.setMaxAccess(_E)
if mibBuilder.loadTexts:ufdNewCfgRemoveLtMPort.setStatus(_A)
_UfdNewCfgAddLtMTrunk_Type=Integer32
_UfdNewCfgAddLtMTrunk_Object=MibScalar
ufdNewCfgAddLtMTrunk=_UfdNewCfgAddLtMTrunk_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,13),_UfdNewCfgAddLtMTrunk_Type())
ufdNewCfgAddLtMTrunk.setMaxAccess(_E)
if mibBuilder.loadTexts:ufdNewCfgAddLtMTrunk.setStatus(_A)
_UfdNewCfgRemoveLtMTrunk_Type=Integer32
_UfdNewCfgRemoveLtMTrunk_Object=MibScalar
ufdNewCfgRemoveLtMTrunk=_UfdNewCfgRemoveLtMTrunk_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,14),_UfdNewCfgRemoveLtMTrunk_Type())
ufdNewCfgRemoveLtMTrunk.setMaxAccess(_E)
if mibBuilder.loadTexts:ufdNewCfgRemoveLtMTrunk.setStatus(_A)
_UfdNewCfgAddLtDPort_Type=Integer32
_UfdNewCfgAddLtDPort_Object=MibScalar
ufdNewCfgAddLtDPort=_UfdNewCfgAddLtDPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,15),_UfdNewCfgAddLtDPort_Type())
ufdNewCfgAddLtDPort.setMaxAccess(_E)
if mibBuilder.loadTexts:ufdNewCfgAddLtDPort.setStatus(_A)
_UfdNewCfgRemoveLtDPort_Type=Integer32
_UfdNewCfgRemoveLtDPort_Object=MibScalar
ufdNewCfgRemoveLtDPort=_UfdNewCfgRemoveLtDPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,16),_UfdNewCfgRemoveLtDPort_Type())
ufdNewCfgRemoveLtDPort.setMaxAccess(_E)
if mibBuilder.loadTexts:ufdNewCfgRemoveLtDPort.setStatus(_A)
_UfdNewCfgAddLtDTrunk_Type=Integer32
_UfdNewCfgAddLtDTrunk_Object=MibScalar
ufdNewCfgAddLtDTrunk=_UfdNewCfgAddLtDTrunk_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,17),_UfdNewCfgAddLtDTrunk_Type())
ufdNewCfgAddLtDTrunk.setMaxAccess(_E)
if mibBuilder.loadTexts:ufdNewCfgAddLtDTrunk.setStatus(_A)
_UfdNewCfgRemoveLtDTrunk_Type=Integer32
_UfdNewCfgRemoveLtDTrunk_Object=MibScalar
ufdNewCfgRemoveLtDTrunk=_UfdNewCfgRemoveLtDTrunk_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,18),_UfdNewCfgRemoveLtDTrunk_Type())
ufdNewCfgRemoveLtDTrunk.setMaxAccess(_E)
if mibBuilder.loadTexts:ufdNewCfgRemoveLtDTrunk.setStatus(_A)
class _UfdCurCfgGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_UfdCurCfgGlobalState_Type.__name__=_C
_UfdCurCfgGlobalState_Object=MibScalar
ufdCurCfgGlobalState=_UfdCurCfgGlobalState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,19),_UfdCurCfgGlobalState_Type())
ufdCurCfgGlobalState.setMaxAccess(_B)
if mibBuilder.loadTexts:ufdCurCfgGlobalState.setStatus(_A)
class _UfdNewCfgGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_UfdNewCfgGlobalState_Type.__name__=_C
_UfdNewCfgGlobalState_Object=MibScalar
ufdNewCfgGlobalState=_UfdNewCfgGlobalState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,9,1,20),_UfdNewCfgGlobalState_Type())
ufdNewCfgGlobalState.setMaxAccess(_E)
if mibBuilder.loadTexts:ufdNewCfgGlobalState.setStatus(_A)
_Dot1x_ObjectIdentity=ObjectIdentity
dot1x=_Dot1x_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11))
class _Dot1xCurStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_Dot1xCurStatus_Type.__name__=_C
_Dot1xCurStatus_Object=MibScalar
dot1xCurStatus=_Dot1xCurStatus_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,1),_Dot1xCurStatus_Type())
dot1xCurStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurStatus.setStatus(_A)
class _Dot1xNewStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_Dot1xNewStatus_Type.__name__=_C
_Dot1xNewStatus_Object=MibScalar
dot1xNewStatus=_Dot1xNewStatus_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,2),_Dot1xNewStatus_Type())
dot1xNewStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xNewStatus.setStatus(_A)
_Dot1xCurCfgPortTable_Object=MibTable
dot1xCurCfgPortTable=_Dot1xCurCfgPortTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,3))
if mibBuilder.loadTexts:dot1xCurCfgPortTable.setStatus(_A)
_Dot1xCurCfgPortEntry_Object=MibTableRow
dot1xCurCfgPortEntry=_Dot1xCurCfgPortEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,3,1))
dot1xCurCfgPortEntry.setIndexNames((0,_F,_u))
if mibBuilder.loadTexts:dot1xCurCfgPortEntry.setStatus(_A)
_Dot1xCurCfgPortIndex_Type=Integer32
_Dot1xCurCfgPortIndex_Object=MibTableColumn
dot1xCurCfgPortIndex=_Dot1xCurCfgPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,3,1,1),_Dot1xCurCfgPortIndex_Type())
dot1xCurCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgPortIndex.setStatus(_A)
class _Dot1xCurCfgPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_T,0),(_N,1),(_U,2)))
_Dot1xCurCfgPortMode_Type.__name__=_C
_Dot1xCurCfgPortMode_Object=MibTableColumn
dot1xCurCfgPortMode=_Dot1xCurCfgPortMode_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,3,1,2),_Dot1xCurCfgPortMode_Type())
dot1xCurCfgPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgPortMode.setStatus(_A)
class _Dot1xCurCfgPortQtPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1xCurCfgPortQtPeriod_Type.__name__=_C
_Dot1xCurCfgPortQtPeriod_Object=MibTableColumn
dot1xCurCfgPortQtPeriod=_Dot1xCurCfgPortQtPeriod_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,3,1,3),_Dot1xCurCfgPortQtPeriod_Type())
dot1xCurCfgPortQtPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgPortQtPeriod.setStatus(_A)
class _Dot1xCurCfgPortTxPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1xCurCfgPortTxPeriod_Type.__name__=_C
_Dot1xCurCfgPortTxPeriod_Object=MibTableColumn
dot1xCurCfgPortTxPeriod=_Dot1xCurCfgPortTxPeriod_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,3,1,4),_Dot1xCurCfgPortTxPeriod_Type())
dot1xCurCfgPortTxPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgPortTxPeriod.setStatus(_A)
class _Dot1xCurCfgPortSupTmout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1xCurCfgPortSupTmout_Type.__name__=_C
_Dot1xCurCfgPortSupTmout_Object=MibTableColumn
dot1xCurCfgPortSupTmout=_Dot1xCurCfgPortSupTmout_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,3,1,5),_Dot1xCurCfgPortSupTmout_Type())
dot1xCurCfgPortSupTmout.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgPortSupTmout.setStatus(_A)
class _Dot1xCurCfgPortSrvTmout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1xCurCfgPortSrvTmout_Type.__name__=_C
_Dot1xCurCfgPortSrvTmout_Object=MibTableColumn
dot1xCurCfgPortSrvTmout=_Dot1xCurCfgPortSrvTmout_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,3,1,6),_Dot1xCurCfgPortSrvTmout_Type())
dot1xCurCfgPortSrvTmout.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgPortSrvTmout.setStatus(_A)
class _Dot1xCurCfgPortMaxRq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Dot1xCurCfgPortMaxRq_Type.__name__=_C
_Dot1xCurCfgPortMaxRq_Object=MibTableColumn
dot1xCurCfgPortMaxRq=_Dot1xCurCfgPortMaxRq_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,3,1,7),_Dot1xCurCfgPortMaxRq_Type())
dot1xCurCfgPortMaxRq.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgPortMaxRq.setStatus(_A)
class _Dot1xCurCfgPortRaPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_Dot1xCurCfgPortRaPeriod_Type.__name__=_C
_Dot1xCurCfgPortRaPeriod_Object=MibTableColumn
dot1xCurCfgPortRaPeriod=_Dot1xCurCfgPortRaPeriod_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,3,1,8),_Dot1xCurCfgPortRaPeriod_Type())
dot1xCurCfgPortRaPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgPortRaPeriod.setStatus(_A)
class _Dot1xCurCfgPortReAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_L,1)))
_Dot1xCurCfgPortReAuth_Type.__name__=_C
_Dot1xCurCfgPortReAuth_Object=MibTableColumn
dot1xCurCfgPortReAuth=_Dot1xCurCfgPortReAuth_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,3,1,9),_Dot1xCurCfgPortReAuth_Type())
dot1xCurCfgPortReAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgPortReAuth.setStatus(_A)
_Dot1xNewCfgPortTable_Object=MibTable
dot1xNewCfgPortTable=_Dot1xNewCfgPortTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,4))
if mibBuilder.loadTexts:dot1xNewCfgPortTable.setStatus(_A)
_Dot1xNewCfgPortEntry_Object=MibTableRow
dot1xNewCfgPortEntry=_Dot1xNewCfgPortEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,4,1))
dot1xNewCfgPortEntry.setIndexNames((0,_F,_v))
if mibBuilder.loadTexts:dot1xNewCfgPortEntry.setStatus(_A)
_Dot1xNewCfgPortIndex_Type=Integer32
_Dot1xNewCfgPortIndex_Object=MibTableColumn
dot1xNewCfgPortIndex=_Dot1xNewCfgPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,4,1,1),_Dot1xNewCfgPortIndex_Type())
dot1xNewCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xNewCfgPortIndex.setStatus(_A)
class _Dot1xNewCfgPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_T,0),(_N,1),(_U,2)))
_Dot1xNewCfgPortMode_Type.__name__=_C
_Dot1xNewCfgPortMode_Object=MibTableColumn
dot1xNewCfgPortMode=_Dot1xNewCfgPortMode_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,4,1,2),_Dot1xNewCfgPortMode_Type())
dot1xNewCfgPortMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgPortMode.setStatus(_A)
class _Dot1xNewCfgPortQtPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1xNewCfgPortQtPeriod_Type.__name__=_C
_Dot1xNewCfgPortQtPeriod_Object=MibTableColumn
dot1xNewCfgPortQtPeriod=_Dot1xNewCfgPortQtPeriod_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,4,1,3),_Dot1xNewCfgPortQtPeriod_Type())
dot1xNewCfgPortQtPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgPortQtPeriod.setStatus(_A)
class _Dot1xNewCfgPortTxPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1xNewCfgPortTxPeriod_Type.__name__=_C
_Dot1xNewCfgPortTxPeriod_Object=MibTableColumn
dot1xNewCfgPortTxPeriod=_Dot1xNewCfgPortTxPeriod_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,4,1,4),_Dot1xNewCfgPortTxPeriod_Type())
dot1xNewCfgPortTxPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgPortTxPeriod.setStatus(_A)
class _Dot1xNewCfgPortSupTmout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1xNewCfgPortSupTmout_Type.__name__=_C
_Dot1xNewCfgPortSupTmout_Object=MibTableColumn
dot1xNewCfgPortSupTmout=_Dot1xNewCfgPortSupTmout_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,4,1,5),_Dot1xNewCfgPortSupTmout_Type())
dot1xNewCfgPortSupTmout.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgPortSupTmout.setStatus(_A)
class _Dot1xNewCfgPortSrvTmout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1xNewCfgPortSrvTmout_Type.__name__=_C
_Dot1xNewCfgPortSrvTmout_Object=MibTableColumn
dot1xNewCfgPortSrvTmout=_Dot1xNewCfgPortSrvTmout_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,4,1,6),_Dot1xNewCfgPortSrvTmout_Type())
dot1xNewCfgPortSrvTmout.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgPortSrvTmout.setStatus(_A)
class _Dot1xNewCfgPortMaxRq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Dot1xNewCfgPortMaxRq_Type.__name__=_C
_Dot1xNewCfgPortMaxRq_Object=MibTableColumn
dot1xNewCfgPortMaxRq=_Dot1xNewCfgPortMaxRq_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,4,1,7),_Dot1xNewCfgPortMaxRq_Type())
dot1xNewCfgPortMaxRq.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgPortMaxRq.setStatus(_A)
class _Dot1xNewCfgPortRaPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,604800))
_Dot1xNewCfgPortRaPeriod_Type.__name__=_C
_Dot1xNewCfgPortRaPeriod_Object=MibTableColumn
dot1xNewCfgPortRaPeriod=_Dot1xNewCfgPortRaPeriod_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,4,1,8),_Dot1xNewCfgPortRaPeriod_Type())
dot1xNewCfgPortRaPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgPortRaPeriod.setStatus(_A)
class _Dot1xNewCfgPortReAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_L,1)))
_Dot1xNewCfgPortReAuth_Type.__name__=_C
_Dot1xNewCfgPortReAuth_Object=MibTableColumn
dot1xNewCfgPortReAuth=_Dot1xNewCfgPortReAuth_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,4,1,9),_Dot1xNewCfgPortReAuth_Type())
dot1xNewCfgPortReAuth.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgPortReAuth.setStatus(_A)
class _Dot1xNewCfgPortDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),('apply',1)))
_Dot1xNewCfgPortDefault_Type.__name__=_C
_Dot1xNewCfgPortDefault_Object=MibTableColumn
dot1xNewCfgPortDefault=_Dot1xNewCfgPortDefault_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,4,1,10),_Dot1xNewCfgPortDefault_Type())
dot1xNewCfgPortDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgPortDefault.setStatus(_A)
class _Dot1xNewCfgPortApplyGlobal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),('apply',1)))
_Dot1xNewCfgPortApplyGlobal_Type.__name__=_C
_Dot1xNewCfgPortApplyGlobal_Object=MibTableColumn
dot1xNewCfgPortApplyGlobal=_Dot1xNewCfgPortApplyGlobal_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,4,1,11),_Dot1xNewCfgPortApplyGlobal_Type())
dot1xNewCfgPortApplyGlobal.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgPortApplyGlobal.setStatus(_A)
_Dot1xCurCfgGlobalTable_ObjectIdentity=ObjectIdentity
dot1xCurCfgGlobalTable=_Dot1xCurCfgGlobalTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,5))
class _Dot1xCurCfgGlobalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_T,0),(_N,1),(_U,2)))
_Dot1xCurCfgGlobalMode_Type.__name__=_C
_Dot1xCurCfgGlobalMode_Object=MibScalar
dot1xCurCfgGlobalMode=_Dot1xCurCfgGlobalMode_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,5,1),_Dot1xCurCfgGlobalMode_Type())
dot1xCurCfgGlobalMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgGlobalMode.setStatus(_A)
class _Dot1xCurCfgGlobalQtPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1xCurCfgGlobalQtPeriod_Type.__name__=_C
_Dot1xCurCfgGlobalQtPeriod_Object=MibScalar
dot1xCurCfgGlobalQtPeriod=_Dot1xCurCfgGlobalQtPeriod_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,5,2),_Dot1xCurCfgGlobalQtPeriod_Type())
dot1xCurCfgGlobalQtPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgGlobalQtPeriod.setStatus(_A)
class _Dot1xCurCfgGlobalTxPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1xCurCfgGlobalTxPeriod_Type.__name__=_C
_Dot1xCurCfgGlobalTxPeriod_Object=MibScalar
dot1xCurCfgGlobalTxPeriod=_Dot1xCurCfgGlobalTxPeriod_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,5,3),_Dot1xCurCfgGlobalTxPeriod_Type())
dot1xCurCfgGlobalTxPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgGlobalTxPeriod.setStatus(_A)
class _Dot1xCurCfgGlobalSupTmout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1xCurCfgGlobalSupTmout_Type.__name__=_C
_Dot1xCurCfgGlobalSupTmout_Object=MibScalar
dot1xCurCfgGlobalSupTmout=_Dot1xCurCfgGlobalSupTmout_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,5,4),_Dot1xCurCfgGlobalSupTmout_Type())
dot1xCurCfgGlobalSupTmout.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgGlobalSupTmout.setStatus(_A)
class _Dot1xCurCfgGlobalSrvTmout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1xCurCfgGlobalSrvTmout_Type.__name__=_C
_Dot1xCurCfgGlobalSrvTmout_Object=MibScalar
dot1xCurCfgGlobalSrvTmout=_Dot1xCurCfgGlobalSrvTmout_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,5,5),_Dot1xCurCfgGlobalSrvTmout_Type())
dot1xCurCfgGlobalSrvTmout.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgGlobalSrvTmout.setStatus(_A)
class _Dot1xCurCfgGlobalMaxRq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Dot1xCurCfgGlobalMaxRq_Type.__name__=_C
_Dot1xCurCfgGlobalMaxRq_Object=MibScalar
dot1xCurCfgGlobalMaxRq=_Dot1xCurCfgGlobalMaxRq_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,5,6),_Dot1xCurCfgGlobalMaxRq_Type())
dot1xCurCfgGlobalMaxRq.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgGlobalMaxRq.setStatus(_A)
class _Dot1xCurCfgGlobalRaPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_Dot1xCurCfgGlobalRaPeriod_Type.__name__=_C
_Dot1xCurCfgGlobalRaPeriod_Object=MibScalar
dot1xCurCfgGlobalRaPeriod=_Dot1xCurCfgGlobalRaPeriod_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,5,7),_Dot1xCurCfgGlobalRaPeriod_Type())
dot1xCurCfgGlobalRaPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgGlobalRaPeriod.setStatus(_A)
class _Dot1xCurCfgGlobalReAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_L,1)))
_Dot1xCurCfgGlobalReAuth_Type.__name__=_C
_Dot1xCurCfgGlobalReAuth_Object=MibScalar
dot1xCurCfgGlobalReAuth=_Dot1xCurCfgGlobalReAuth_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,5,8),_Dot1xCurCfgGlobalReAuth_Type())
dot1xCurCfgGlobalReAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xCurCfgGlobalReAuth.setStatus(_A)
_Dot1xNewCfgGlobalTable_ObjectIdentity=ObjectIdentity
dot1xNewCfgGlobalTable=_Dot1xNewCfgGlobalTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,6))
class _Dot1xNewCfgGlobalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_T,0),(_N,1),(_U,2)))
_Dot1xNewCfgGlobalMode_Type.__name__=_C
_Dot1xNewCfgGlobalMode_Object=MibScalar
dot1xNewCfgGlobalMode=_Dot1xNewCfgGlobalMode_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,6,1),_Dot1xNewCfgGlobalMode_Type())
dot1xNewCfgGlobalMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgGlobalMode.setStatus(_A)
class _Dot1xNewCfgGlobalQtPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1xNewCfgGlobalQtPeriod_Type.__name__=_C
_Dot1xNewCfgGlobalQtPeriod_Object=MibScalar
dot1xNewCfgGlobalQtPeriod=_Dot1xNewCfgGlobalQtPeriod_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,6,2),_Dot1xNewCfgGlobalQtPeriod_Type())
dot1xNewCfgGlobalQtPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgGlobalQtPeriod.setStatus(_A)
class _Dot1xNewCfgGlobalTxPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1xNewCfgGlobalTxPeriod_Type.__name__=_C
_Dot1xNewCfgGlobalTxPeriod_Object=MibScalar
dot1xNewCfgGlobalTxPeriod=_Dot1xNewCfgGlobalTxPeriod_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,6,3),_Dot1xNewCfgGlobalTxPeriod_Type())
dot1xNewCfgGlobalTxPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgGlobalTxPeriod.setStatus(_A)
class _Dot1xNewCfgGlobalSupTmout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1xNewCfgGlobalSupTmout_Type.__name__=_C
_Dot1xNewCfgGlobalSupTmout_Object=MibScalar
dot1xNewCfgGlobalSupTmout=_Dot1xNewCfgGlobalSupTmout_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,6,4),_Dot1xNewCfgGlobalSupTmout_Type())
dot1xNewCfgGlobalSupTmout.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgGlobalSupTmout.setStatus(_A)
class _Dot1xNewCfgGlobalSrvTmout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1xNewCfgGlobalSrvTmout_Type.__name__=_C
_Dot1xNewCfgGlobalSrvTmout_Object=MibScalar
dot1xNewCfgGlobalSrvTmout=_Dot1xNewCfgGlobalSrvTmout_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,6,5),_Dot1xNewCfgGlobalSrvTmout_Type())
dot1xNewCfgGlobalSrvTmout.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgGlobalSrvTmout.setStatus(_A)
class _Dot1xNewCfgGlobalMaxRq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Dot1xNewCfgGlobalMaxRq_Type.__name__=_C
_Dot1xNewCfgGlobalMaxRq_Object=MibScalar
dot1xNewCfgGlobalMaxRq=_Dot1xNewCfgGlobalMaxRq_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,6,6),_Dot1xNewCfgGlobalMaxRq_Type())
dot1xNewCfgGlobalMaxRq.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgGlobalMaxRq.setStatus(_A)
class _Dot1xNewCfgGlobalRaPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,604800))
_Dot1xNewCfgGlobalRaPeriod_Type.__name__=_C
_Dot1xNewCfgGlobalRaPeriod_Object=MibScalar
dot1xNewCfgGlobalRaPeriod=_Dot1xNewCfgGlobalRaPeriod_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,6,7),_Dot1xNewCfgGlobalRaPeriod_Type())
dot1xNewCfgGlobalRaPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgGlobalRaPeriod.setStatus(_A)
class _Dot1xNewCfgGlobalReAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_L,1)))
_Dot1xNewCfgGlobalReAuth_Type.__name__=_C
_Dot1xNewCfgGlobalReAuth_Object=MibScalar
dot1xNewCfgGlobalReAuth=_Dot1xNewCfgGlobalReAuth_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,11,6,8),_Dot1xNewCfgGlobalReAuth_Type())
dot1xNewCfgGlobalReAuth.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1xNewCfgGlobalReAuth.setStatus(_A)
_Fdb_ObjectIdentity=ObjectIdentity
fdb=_Fdb_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,12))
_FdbGeneralCfg_ObjectIdentity=ObjectIdentity
fdbGeneralCfg=_FdbGeneralCfg_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,12,1))
_FdbCurCfgAgingTime_Type=Integer32
_FdbCurCfgAgingTime_Object=MibScalar
fdbCurCfgAgingTime=_FdbCurCfgAgingTime_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,12,1,1),_FdbCurCfgAgingTime_Type())
fdbCurCfgAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbCurCfgAgingTime.setStatus(_A)
_FdbNewCfgAgingTime_Type=Integer32
_FdbNewCfgAgingTime_Object=MibScalar
fdbNewCfgAgingTime=_FdbNewCfgAgingTime_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,12,1,2),_FdbNewCfgAgingTime_Type())
fdbNewCfgAgingTime.setMaxAccess(_E)
if mibBuilder.loadTexts:fdbNewCfgAgingTime.setStatus(_A)
_FdbNewCfgStaticTable_Object=MibTable
fdbNewCfgStaticTable=_FdbNewCfgStaticTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,12,2))
if mibBuilder.loadTexts:fdbNewCfgStaticTable.setStatus(_A)
_FdbNewCfgStaticEntry_Object=MibTableRow
fdbNewCfgStaticEntry=_FdbNewCfgStaticEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,12,2,1))
fdbNewCfgStaticEntry.setIndexNames((0,_F,_w))
if mibBuilder.loadTexts:fdbNewCfgStaticEntry.setStatus(_A)
_FdbNewCfgEntryIndex_Type=Integer32
_FdbNewCfgEntryIndex_Object=MibTableColumn
fdbNewCfgEntryIndex=_FdbNewCfgEntryIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,12,2,1,1),_FdbNewCfgEntryIndex_Type())
fdbNewCfgEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbNewCfgEntryIndex.setStatus(_A)
_FdbNewCfgAddVlan_Type=Integer32
_FdbNewCfgAddVlan_Object=MibTableColumn
fdbNewCfgAddVlan=_FdbNewCfgAddVlan_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,12,2,1,2),_FdbNewCfgAddVlan_Type())
fdbNewCfgAddVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:fdbNewCfgAddVlan.setStatus(_A)
_FdbNewCfgAddPort_Type=Integer32
_FdbNewCfgAddPort_Object=MibTableColumn
fdbNewCfgAddPort=_FdbNewCfgAddPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,12,2,1,3),_FdbNewCfgAddPort_Type())
fdbNewCfgAddPort.setMaxAccess(_D)
if mibBuilder.loadTexts:fdbNewCfgAddPort.setStatus(_A)
_FdbNewCfgAddMac_Type=PhysAddress
_FdbNewCfgAddMac_Object=MibTableColumn
fdbNewCfgAddMac=_FdbNewCfgAddMac_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,12,2,1,4),_FdbNewCfgAddMac_Type())
fdbNewCfgAddMac.setMaxAccess(_D)
if mibBuilder.loadTexts:fdbNewCfgAddMac.setStatus(_A)
class _FdbNewCfgDelStaticEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_FdbNewCfgDelStaticEntry_Type.__name__=_C
_FdbNewCfgDelStaticEntry_Object=MibTableColumn
fdbNewCfgDelStaticEntry=_FdbNewCfgDelStaticEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,12,2,1,5),_FdbNewCfgDelStaticEntry_Type())
fdbNewCfgDelStaticEntry.setMaxAccess(_D)
if mibBuilder.loadTexts:fdbNewCfgDelStaticEntry.setStatus(_A)
_HotlinksCfg_ObjectIdentity=ObjectIdentity
hotlinksCfg=_HotlinksCfg_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14))
class _HotlinksCurCfgOnState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_I,2)))
_HotlinksCurCfgOnState_Type.__name__=_C
_HotlinksCurCfgOnState_Object=MibScalar
hotlinksCurCfgOnState=_HotlinksCurCfgOnState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,1),_HotlinksCurCfgOnState_Type())
hotlinksCurCfgOnState.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksCurCfgOnState.setStatus(_A)
class _HotlinksNewCfgOnState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_I,2)))
_HotlinksNewCfgOnState_Type.__name__=_C
_HotlinksNewCfgOnState_Object=MibScalar
hotlinksNewCfgOnState=_HotlinksNewCfgOnState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,2),_HotlinksNewCfgOnState_Type())
hotlinksNewCfgOnState.setMaxAccess(_E)
if mibBuilder.loadTexts:hotlinksNewCfgOnState.setStatus(_A)
class _HotlinksCurCfgFdbUpdateState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_HotlinksCurCfgFdbUpdateState_Type.__name__=_C
_HotlinksCurCfgFdbUpdateState_Object=MibScalar
hotlinksCurCfgFdbUpdateState=_HotlinksCurCfgFdbUpdateState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,3),_HotlinksCurCfgFdbUpdateState_Type())
hotlinksCurCfgFdbUpdateState.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksCurCfgFdbUpdateState.setStatus(_A)
class _HotlinksNewCfgFdbUpdateState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_HotlinksNewCfgFdbUpdateState_Type.__name__=_C
_HotlinksNewCfgFdbUpdateState_Object=MibScalar
hotlinksNewCfgFdbUpdateState=_HotlinksNewCfgFdbUpdateState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,4),_HotlinksNewCfgFdbUpdateState_Type())
hotlinksNewCfgFdbUpdateState.setMaxAccess(_E)
if mibBuilder.loadTexts:hotlinksNewCfgFdbUpdateState.setStatus(_A)
_HotlinksMaxTriggerEntries_Type=Integer32
_HotlinksMaxTriggerEntries_Object=MibScalar
hotlinksMaxTriggerEntries=_HotlinksMaxTriggerEntries_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,5),_HotlinksMaxTriggerEntries_Type())
hotlinksMaxTriggerEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksMaxTriggerEntries.setStatus(_A)
_HotlinksCurCfgTriggerTable_Object=MibTable
hotlinksCurCfgTriggerTable=_HotlinksCurCfgTriggerTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,6))
if mibBuilder.loadTexts:hotlinksCurCfgTriggerTable.setStatus(_A)
_HotlinksCurCfgTriggerTableEntry_Object=MibTableRow
hotlinksCurCfgTriggerTableEntry=_HotlinksCurCfgTriggerTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,6,1))
hotlinksCurCfgTriggerTableEntry.setIndexNames((0,_F,_x))
if mibBuilder.loadTexts:hotlinksCurCfgTriggerTableEntry.setStatus(_A)
_HotlinksCurCfgTriggerId_Type=Integer32
_HotlinksCurCfgTriggerId_Object=MibTableColumn
hotlinksCurCfgTriggerId=_HotlinksCurCfgTriggerId_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,6,1,1),_HotlinksCurCfgTriggerId_Type())
hotlinksCurCfgTriggerId.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksCurCfgTriggerId.setStatus(_A)
class _HotlinksCurCfgTriggerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_HotlinksCurCfgTriggerState_Type.__name__=_C
_HotlinksCurCfgTriggerState_Object=MibTableColumn
hotlinksCurCfgTriggerState=_HotlinksCurCfgTriggerState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,6,1,2),_HotlinksCurCfgTriggerState_Type())
hotlinksCurCfgTriggerState.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksCurCfgTriggerState.setStatus(_A)
class _HotlinksCurCfgTriggerPreemptState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_HotlinksCurCfgTriggerPreemptState_Type.__name__=_C
_HotlinksCurCfgTriggerPreemptState_Object=MibTableColumn
hotlinksCurCfgTriggerPreemptState=_HotlinksCurCfgTriggerPreemptState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,6,1,3),_HotlinksCurCfgTriggerPreemptState_Type())
hotlinksCurCfgTriggerPreemptState.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksCurCfgTriggerPreemptState.setStatus(_A)
_HotlinksCurCfgTriggerFdelay_Type=Integer32
_HotlinksCurCfgTriggerFdelay_Object=MibTableColumn
hotlinksCurCfgTriggerFdelay=_HotlinksCurCfgTriggerFdelay_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,6,1,4),_HotlinksCurCfgTriggerFdelay_Type())
hotlinksCurCfgTriggerFdelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksCurCfgTriggerFdelay.setStatus(_A)
_HotlinksCurCfgTriggerMasterPort_Type=Integer32
_HotlinksCurCfgTriggerMasterPort_Object=MibTableColumn
hotlinksCurCfgTriggerMasterPort=_HotlinksCurCfgTriggerMasterPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,6,1,5),_HotlinksCurCfgTriggerMasterPort_Type())
hotlinksCurCfgTriggerMasterPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksCurCfgTriggerMasterPort.setStatus(_A)
_HotlinksCurCfgTriggerMasterTrunk_Type=Integer32
_HotlinksCurCfgTriggerMasterTrunk_Object=MibTableColumn
hotlinksCurCfgTriggerMasterTrunk=_HotlinksCurCfgTriggerMasterTrunk_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,6,1,6),_HotlinksCurCfgTriggerMasterTrunk_Type())
hotlinksCurCfgTriggerMasterTrunk.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksCurCfgTriggerMasterTrunk.setStatus(_A)
_HotlinksCurCfgTriggerBackupPort_Type=Integer32
_HotlinksCurCfgTriggerBackupPort_Object=MibTableColumn
hotlinksCurCfgTriggerBackupPort=_HotlinksCurCfgTriggerBackupPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,6,1,7),_HotlinksCurCfgTriggerBackupPort_Type())
hotlinksCurCfgTriggerBackupPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksCurCfgTriggerBackupPort.setStatus(_A)
_HotlinksCurCfgTriggerBackupTrunk_Type=Integer32
_HotlinksCurCfgTriggerBackupTrunk_Object=MibTableColumn
hotlinksCurCfgTriggerBackupTrunk=_HotlinksCurCfgTriggerBackupTrunk_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,6,1,8),_HotlinksCurCfgTriggerBackupTrunk_Type())
hotlinksCurCfgTriggerBackupTrunk.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksCurCfgTriggerBackupTrunk.setStatus(_A)
_HotlinksNewCfgTriggerTable_Object=MibTable
hotlinksNewCfgTriggerTable=_HotlinksNewCfgTriggerTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,7))
if mibBuilder.loadTexts:hotlinksNewCfgTriggerTable.setStatus(_A)
_HotlinksNewCfgTriggerTableEntry_Object=MibTableRow
hotlinksNewCfgTriggerTableEntry=_HotlinksNewCfgTriggerTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,7,1))
hotlinksNewCfgTriggerTableEntry.setIndexNames((0,_F,_y))
if mibBuilder.loadTexts:hotlinksNewCfgTriggerTableEntry.setStatus(_A)
_HotlinksNewCfgTriggerId_Type=Integer32
_HotlinksNewCfgTriggerId_Object=MibTableColumn
hotlinksNewCfgTriggerId=_HotlinksNewCfgTriggerId_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,7,1,1),_HotlinksNewCfgTriggerId_Type())
hotlinksNewCfgTriggerId.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksNewCfgTriggerId.setStatus(_A)
class _HotlinksNewCfgTriggerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_HotlinksNewCfgTriggerState_Type.__name__=_C
_HotlinksNewCfgTriggerState_Object=MibTableColumn
hotlinksNewCfgTriggerState=_HotlinksNewCfgTriggerState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,7,1,2),_HotlinksNewCfgTriggerState_Type())
hotlinksNewCfgTriggerState.setMaxAccess(_E)
if mibBuilder.loadTexts:hotlinksNewCfgTriggerState.setStatus(_A)
class _HotlinksNewCfgTriggerPreemptState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_HotlinksNewCfgTriggerPreemptState_Type.__name__=_C
_HotlinksNewCfgTriggerPreemptState_Object=MibTableColumn
hotlinksNewCfgTriggerPreemptState=_HotlinksNewCfgTriggerPreemptState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,7,1,3),_HotlinksNewCfgTriggerPreemptState_Type())
hotlinksNewCfgTriggerPreemptState.setMaxAccess(_E)
if mibBuilder.loadTexts:hotlinksNewCfgTriggerPreemptState.setStatus(_A)
_HotlinksNewCfgTriggerFdelay_Type=Integer32
_HotlinksNewCfgTriggerFdelay_Object=MibTableColumn
hotlinksNewCfgTriggerFdelay=_HotlinksNewCfgTriggerFdelay_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,7,1,4),_HotlinksNewCfgTriggerFdelay_Type())
hotlinksNewCfgTriggerFdelay.setMaxAccess(_E)
if mibBuilder.loadTexts:hotlinksNewCfgTriggerFdelay.setStatus(_A)
_HotlinksNewCfgTriggerMasterPort_Type=Integer32
_HotlinksNewCfgTriggerMasterPort_Object=MibTableColumn
hotlinksNewCfgTriggerMasterPort=_HotlinksNewCfgTriggerMasterPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,7,1,5),_HotlinksNewCfgTriggerMasterPort_Type())
hotlinksNewCfgTriggerMasterPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hotlinksNewCfgTriggerMasterPort.setStatus(_A)
_HotlinksNewCfgTriggerMasterTrunk_Type=Integer32
_HotlinksNewCfgTriggerMasterTrunk_Object=MibTableColumn
hotlinksNewCfgTriggerMasterTrunk=_HotlinksNewCfgTriggerMasterTrunk_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,7,1,6),_HotlinksNewCfgTriggerMasterTrunk_Type())
hotlinksNewCfgTriggerMasterTrunk.setMaxAccess(_E)
if mibBuilder.loadTexts:hotlinksNewCfgTriggerMasterTrunk.setStatus(_A)
_HotlinksNewCfgTriggerBackupPort_Type=Integer32
_HotlinksNewCfgTriggerBackupPort_Object=MibTableColumn
hotlinksNewCfgTriggerBackupPort=_HotlinksNewCfgTriggerBackupPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,7,1,7),_HotlinksNewCfgTriggerBackupPort_Type())
hotlinksNewCfgTriggerBackupPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hotlinksNewCfgTriggerBackupPort.setStatus(_A)
_HotlinksNewCfgTriggerBackupTrunk_Type=Integer32
_HotlinksNewCfgTriggerBackupTrunk_Object=MibTableColumn
hotlinksNewCfgTriggerBackupTrunk=_HotlinksNewCfgTriggerBackupTrunk_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,1,14,7,1,8),_HotlinksNewCfgTriggerBackupTrunk_Type())
hotlinksNewCfgTriggerBackupTrunk.setMaxAccess(_E)
if mibBuilder.loadTexts:hotlinksNewCfgTriggerBackupTrunk.setStatus(_A)
_Layer2Stats_ObjectIdentity=ObjectIdentity
layer2Stats=_Layer2Stats_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2))
_FdbStats_ObjectIdentity=ObjectIdentity
fdbStats=_FdbStats_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,1))
_FdbStatsCreates_Type=Counter32
_FdbStatsCreates_Object=MibScalar
fdbStatsCreates=_FdbStatsCreates_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,1,1),_FdbStatsCreates_Type())
fdbStatsCreates.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsCreates.setStatus(_A)
_FdbStatsDeletes_Type=Counter32
_FdbStatsDeletes_Object=MibScalar
fdbStatsDeletes=_FdbStatsDeletes_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,1,2),_FdbStatsDeletes_Type())
fdbStatsDeletes.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsDeletes.setStatus(_A)
_FdbStatsCurrent_Type=Gauge32
_FdbStatsCurrent_Object=MibScalar
fdbStatsCurrent=_FdbStatsCurrent_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,1,3),_FdbStatsCurrent_Type())
fdbStatsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsCurrent.setStatus(_A)
_FdbStatsHiwat_Type=Integer32
_FdbStatsHiwat_Object=MibScalar
fdbStatsHiwat=_FdbStatsHiwat_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,1,4),_FdbStatsHiwat_Type())
fdbStatsHiwat.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsHiwat.setStatus(_A)
_FdbStatsLookups_Type=Counter32
_FdbStatsLookups_Object=MibScalar
fdbStatsLookups=_FdbStatsLookups_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,1,5),_FdbStatsLookups_Type())
fdbStatsLookups.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsLookups.setStatus(_A)
_FdbStatsLookupFails_Type=Counter32
_FdbStatsLookupFails_Object=MibScalar
fdbStatsLookupFails=_FdbStatsLookupFails_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,1,6),_FdbStatsLookupFails_Type())
fdbStatsLookupFails.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsLookupFails.setStatus(_A)
_FdbStatsFinds_Type=Counter32
_FdbStatsFinds_Object=MibScalar
fdbStatsFinds=_FdbStatsFinds_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,1,7),_FdbStatsFinds_Type())
fdbStatsFinds.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsFinds.setStatus(_A)
_FdbStatsFindFails_Type=Counter32
_FdbStatsFindFails_Object=MibScalar
fdbStatsFindFails=_FdbStatsFindFails_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,1,8),_FdbStatsFindFails_Type())
fdbStatsFindFails.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsFindFails.setStatus(_A)
_FdbStatsFindOrCreates_Type=Counter32
_FdbStatsFindOrCreates_Object=MibScalar
fdbStatsFindOrCreates=_FdbStatsFindOrCreates_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,1,9),_FdbStatsFindOrCreates_Type())
fdbStatsFindOrCreates.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsFindOrCreates.setStatus(_A)
_FdbStatsOverflows_Type=Counter32
_FdbStatsOverflows_Object=MibScalar
fdbStatsOverflows=_FdbStatsOverflows_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,1,10),_FdbStatsOverflows_Type())
fdbStatsOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsOverflows.setStatus(_A)
_StpStats_ObjectIdentity=ObjectIdentity
stpStats=_StpStats_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,2))
_StgStatsPortTable_Object=MibTable
stgStatsPortTable=_StgStatsPortTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,2,1))
if mibBuilder.loadTexts:stgStatsPortTable.setStatus(_A)
_StgStatsPortTableEntry_Object=MibTableRow
stgStatsPortTableEntry=_StgStatsPortTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,2,1,1))
stgStatsPortTableEntry.setIndexNames((0,_F,_z),(0,_F,_A0))
if mibBuilder.loadTexts:stgStatsPortTableEntry.setStatus(_A)
_StgStatsStpIndex_Type=Integer32
_StgStatsStpIndex_Object=MibTableColumn
stgStatsStpIndex=_StgStatsStpIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,2,1,1,1),_StgStatsStpIndex_Type())
stgStatsStpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgStatsStpIndex.setStatus(_A)
_StgStatsPortIndex_Type=Integer32
_StgStatsPortIndex_Object=MibTableColumn
stgStatsPortIndex=_StgStatsPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,2,1,1,2),_StgStatsPortIndex_Type())
stgStatsPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgStatsPortIndex.setStatus(_A)
_StgStatsPortRcvCfgBpdus_Type=Counter32
_StgStatsPortRcvCfgBpdus_Object=MibTableColumn
stgStatsPortRcvCfgBpdus=_StgStatsPortRcvCfgBpdus_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,2,1,1,3),_StgStatsPortRcvCfgBpdus_Type())
stgStatsPortRcvCfgBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:stgStatsPortRcvCfgBpdus.setStatus(_A)
_StgStatsPortRcvTcnBpdus_Type=Counter32
_StgStatsPortRcvTcnBpdus_Object=MibTableColumn
stgStatsPortRcvTcnBpdus=_StgStatsPortRcvTcnBpdus_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,2,1,1,4),_StgStatsPortRcvTcnBpdus_Type())
stgStatsPortRcvTcnBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:stgStatsPortRcvTcnBpdus.setStatus(_A)
_StgStatsPortXmtCfgBpdus_Type=Counter32
_StgStatsPortXmtCfgBpdus_Object=MibTableColumn
stgStatsPortXmtCfgBpdus=_StgStatsPortXmtCfgBpdus_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,2,1,1,5),_StgStatsPortXmtCfgBpdus_Type())
stgStatsPortXmtCfgBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:stgStatsPortXmtCfgBpdus.setStatus(_A)
_StgStatsPortXmtTcnBpdus_Type=Counter32
_StgStatsPortXmtTcnBpdus_Object=MibTableColumn
stgStatsPortXmtTcnBpdus=_StgStatsPortXmtTcnBpdus_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,2,1,1,6),_StgStatsPortXmtTcnBpdus_Type())
stgStatsPortXmtTcnBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:stgStatsPortXmtTcnBpdus.setStatus(_A)
_LacpStats_ObjectIdentity=ObjectIdentity
lacpStats=_LacpStats_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,3))
_LacpStatsTable_Object=MibTable
lacpStatsTable=_LacpStatsTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,3,1))
if mibBuilder.loadTexts:lacpStatsTable.setStatus(_A)
_LacpStatsTableEntry_Object=MibTableRow
lacpStatsTableEntry=_LacpStatsTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,3,1,1))
lacpStatsTableEntry.setIndexNames((0,_F,_A1))
if mibBuilder.loadTexts:lacpStatsTableEntry.setStatus(_A)
_LacpStatsIndex_Type=Integer32
_LacpStatsIndex_Object=MibTableColumn
lacpStatsIndex=_LacpStatsIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,3,1,1,1),_LacpStatsIndex_Type())
lacpStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpStatsIndex.setStatus(_A)
_LacpdusRx_Type=Integer32
_LacpdusRx_Object=MibTableColumn
lacpdusRx=_LacpdusRx_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,3,1,1,2),_LacpdusRx_Type())
lacpdusRx.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpdusRx.setStatus(_A)
_MarkerpdusRx_Type=Integer32
_MarkerpdusRx_Object=MibTableColumn
markerpdusRx=_MarkerpdusRx_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,3,1,1,3),_MarkerpdusRx_Type())
markerpdusRx.setMaxAccess(_B)
if mibBuilder.loadTexts:markerpdusRx.setStatus(_A)
_MarkerresponsepdusRx_Type=Integer32
_MarkerresponsepdusRx_Object=MibTableColumn
markerresponsepdusRx=_MarkerresponsepdusRx_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,3,1,1,4),_MarkerresponsepdusRx_Type())
markerresponsepdusRx.setMaxAccess(_B)
if mibBuilder.loadTexts:markerresponsepdusRx.setStatus(_A)
_UnknownRx_Type=Integer32
_UnknownRx_Object=MibTableColumn
unknownRx=_UnknownRx_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,3,1,1,5),_UnknownRx_Type())
unknownRx.setMaxAccess(_B)
if mibBuilder.loadTexts:unknownRx.setStatus(_A)
_IllegalRx_Type=Integer32
_IllegalRx_Object=MibTableColumn
illegalRx=_IllegalRx_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,3,1,1,6),_IllegalRx_Type())
illegalRx.setMaxAccess(_B)
if mibBuilder.loadTexts:illegalRx.setStatus(_A)
_LacpdusTx_Type=Integer32
_LacpdusTx_Object=MibTableColumn
lacpdusTx=_LacpdusTx_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,3,1,1,7),_LacpdusTx_Type())
lacpdusTx.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpdusTx.setStatus(_A)
_MarkerpdusTx_Type=Integer32
_MarkerpdusTx_Object=MibTableColumn
markerpdusTx=_MarkerpdusTx_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,3,1,1,8),_MarkerpdusTx_Type())
markerpdusTx.setMaxAccess(_B)
if mibBuilder.loadTexts:markerpdusTx.setStatus(_A)
_MarkerresponsepdusTx_Type=Integer32
_MarkerresponsepdusTx_Object=MibTableColumn
markerresponsepdusTx=_MarkerresponsepdusTx_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,3,1,1,9),_MarkerresponsepdusTx_Type())
markerresponsepdusTx.setMaxAccess(_B)
if mibBuilder.loadTexts:markerresponsepdusTx.setStatus(_A)
_UfdStats_ObjectIdentity=ObjectIdentity
ufdStats=_UfdStats_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,4))
_UfdNoLtMLinkFailure_Type=Integer32
_UfdNoLtMLinkFailure_Object=MibScalar
ufdNoLtMLinkFailure=_UfdNoLtMLinkFailure_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,4,1),_UfdNoLtMLinkFailure_Type())
ufdNoLtMLinkFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:ufdNoLtMLinkFailure.setStatus(_A)
_UfdNoLtMLinkBlockingState_Type=Integer32
_UfdNoLtMLinkBlockingState_Object=MibScalar
ufdNoLtMLinkBlockingState=_UfdNoLtMLinkBlockingState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,4,2),_UfdNoLtMLinkBlockingState_Type())
ufdNoLtMLinkBlockingState.setMaxAccess(_B)
if mibBuilder.loadTexts:ufdNoLtMLinkBlockingState.setStatus(_A)
_UfdNoLtDAutoDisabled_Type=Integer32
_UfdNoLtDAutoDisabled_Object=MibScalar
ufdNoLtDAutoDisabled=_UfdNoLtDAutoDisabled_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,4,3),_UfdNoLtDAutoDisabled_Type())
ufdNoLtDAutoDisabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ufdNoLtDAutoDisabled.setStatus(_A)
_HotlinksStats_ObjectIdentity=ObjectIdentity
hotlinksStats=_HotlinksStats_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,6))
_HotlinksStatsTriggerTable_Object=MibTable
hotlinksStatsTriggerTable=_HotlinksStatsTriggerTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,6,1))
if mibBuilder.loadTexts:hotlinksStatsTriggerTable.setStatus(_A)
_HotlinksStatsTriggerTableEntry_Object=MibTableRow
hotlinksStatsTriggerTableEntry=_HotlinksStatsTriggerTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,6,1,1))
hotlinksStatsTriggerTableEntry.setIndexNames((0,_F,_A2))
if mibBuilder.loadTexts:hotlinksStatsTriggerTableEntry.setStatus(_A)
_HotlinksStatsTriggerId_Type=Integer32
_HotlinksStatsTriggerId_Object=MibTableColumn
hotlinksStatsTriggerId=_HotlinksStatsTriggerId_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,6,1,1,1),_HotlinksStatsTriggerId_Type())
hotlinksStatsTriggerId.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksStatsTriggerId.setStatus(_A)
_HotlinksStatsTriggerMasterActive_Type=Integer32
_HotlinksStatsTriggerMasterActive_Object=MibTableColumn
hotlinksStatsTriggerMasterActive=_HotlinksStatsTriggerMasterActive_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,6,1,1,2),_HotlinksStatsTriggerMasterActive_Type())
hotlinksStatsTriggerMasterActive.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksStatsTriggerMasterActive.setStatus(_A)
_HotlinksStatsTriggerBackupActive_Type=Integer32
_HotlinksStatsTriggerBackupActive_Object=MibTableColumn
hotlinksStatsTriggerBackupActive=_HotlinksStatsTriggerBackupActive_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,6,1,1,3),_HotlinksStatsTriggerBackupActive_Type())
hotlinksStatsTriggerBackupActive.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksStatsTriggerBackupActive.setStatus(_A)
_HotlinksStatsTriggerFdbUpdate_Type=Integer32
_HotlinksStatsTriggerFdbUpdate_Object=MibTableColumn
hotlinksStatsTriggerFdbUpdate=_HotlinksStatsTriggerFdbUpdate_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,6,1,1,4),_HotlinksStatsTriggerFdbUpdate_Type())
hotlinksStatsTriggerFdbUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksStatsTriggerFdbUpdate.setStatus(_A)
_HotlinksStatsTriggerFdbFailed_Type=Integer32
_HotlinksStatsTriggerFdbFailed_Object=MibTableColumn
hotlinksStatsTriggerFdbFailed=_HotlinksStatsTriggerFdbFailed_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,2,6,1,1,5),_HotlinksStatsTriggerFdbFailed_Type())
hotlinksStatsTriggerFdbFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksStatsTriggerFdbFailed.setStatus(_A)
_Layer2Info_ObjectIdentity=ObjectIdentity
layer2Info=_Layer2Info_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3))
_CistInfo_ObjectIdentity=ObjectIdentity
cistInfo=_CistInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1))
_CistGeneralInfo_ObjectIdentity=ObjectIdentity
cistGeneralInfo=_CistGeneralInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,1))
_CistRoot_Type=BridgeId
_CistRoot_Object=MibScalar
cistRoot=_CistRoot_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,1,1),_CistRoot_Type())
cistRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:cistRoot.setStatus(_A)
_CistRootPathCost_Type=Integer32
_CistRootPathCost_Object=MibScalar
cistRootPathCost=_CistRootPathCost_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,1,2),_CistRootPathCost_Type())
cistRootPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:cistRootPathCost.setStatus(_A)
_CistRootPort_Type=Integer32
_CistRootPort_Object=MibScalar
cistRootPort=_CistRootPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,1,3),_CistRootPort_Type())
cistRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cistRootPort.setStatus(_A)
_CistRootHelloTime_Type=Integer32
_CistRootHelloTime_Object=MibScalar
cistRootHelloTime=_CistRootHelloTime_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,1,4),_CistRootHelloTime_Type())
cistRootHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cistRootHelloTime.setStatus(_A)
_CistRootMaxAge_Type=Integer32
_CistRootMaxAge_Object=MibScalar
cistRootMaxAge=_CistRootMaxAge_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,1,5),_CistRootMaxAge_Type())
cistRootMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:cistRootMaxAge.setStatus(_A)
_CistRootForwardDelay_Type=Integer32
_CistRootForwardDelay_Object=MibScalar
cistRootForwardDelay=_CistRootForwardDelay_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,1,6),_CistRootForwardDelay_Type())
cistRootForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:cistRootForwardDelay.setStatus(_A)
_CistRegionalRoot_Type=BridgeId
_CistRegionalRoot_Object=MibScalar
cistRegionalRoot=_CistRegionalRoot_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,1,7),_CistRegionalRoot_Type())
cistRegionalRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:cistRegionalRoot.setStatus(_A)
_CistRegionalPathCost_Type=Integer32
_CistRegionalPathCost_Object=MibScalar
cistRegionalPathCost=_CistRegionalPathCost_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,1,8),_CistRegionalPathCost_Type())
cistRegionalPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:cistRegionalPathCost.setStatus(_A)
class _CistBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CistBridgePriority_Type.__name__=_C
_CistBridgePriority_Object=MibScalar
cistBridgePriority=_CistBridgePriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,1,9),_CistBridgePriority_Type())
cistBridgePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cistBridgePriority.setStatus(_A)
class _CistBridgeMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_CistBridgeMaxAge_Type.__name__=_C
_CistBridgeMaxAge_Object=MibScalar
cistBridgeMaxAge=_CistBridgeMaxAge_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,1,10),_CistBridgeMaxAge_Type())
cistBridgeMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:cistBridgeMaxAge.setStatus(_A)
class _CistBridgeForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_CistBridgeForwardDelay_Type.__name__=_C
_CistBridgeForwardDelay_Object=MibScalar
cistBridgeForwardDelay=_CistBridgeForwardDelay_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,1,11),_CistBridgeForwardDelay_Type())
cistBridgeForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:cistBridgeForwardDelay.setStatus(_A)
class _CistMaxHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,60))
_CistMaxHopCount_Type.__name__=_C
_CistMaxHopCount_Object=MibScalar
cistMaxHopCount=_CistMaxHopCount_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,1,12),_CistMaxHopCount_Type())
cistMaxHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cistMaxHopCount.setStatus(_A)
class _MstpDigest_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_MstpDigest_Type.__name__=_O
_MstpDigest_Object=MibScalar
mstpDigest=_MstpDigest_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,1,13),_MstpDigest_Type())
mstpDigest.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpDigest.setStatus(_A)
_CistInfoPortTable_Object=MibTable
cistInfoPortTable=_CistInfoPortTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,2))
if mibBuilder.loadTexts:cistInfoPortTable.setStatus(_A)
_CistInfoPortTableEntry_Object=MibTableRow
cistInfoPortTableEntry=_CistInfoPortTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,2,1))
cistInfoPortTableEntry.setIndexNames((0,_F,_A3))
if mibBuilder.loadTexts:cistInfoPortTableEntry.setStatus(_A)
_CistInfoPortIndex_Type=Integer32
_CistInfoPortIndex_Object=MibTableColumn
cistInfoPortIndex=_CistInfoPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,2,1,1),_CistInfoPortIndex_Type())
cistInfoPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortIndex.setStatus(_A)
_CistInfoPortPriority_Type=Integer32
_CistInfoPortPriority_Object=MibTableColumn
cistInfoPortPriority=_CistInfoPortPriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,2,1,2),_CistInfoPortPriority_Type())
cistInfoPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortPriority.setStatus(_A)
_CistInfoPortPathCost_Type=Integer32
_CistInfoPortPathCost_Object=MibTableColumn
cistInfoPortPathCost=_CistInfoPortPathCost_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,2,1,3),_CistInfoPortPathCost_Type())
cistInfoPortPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortPathCost.setStatus(_A)
class _CistInfoPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_G,1),('discarding',2),('learning',4),(_A4,5)))
_CistInfoPortState_Type.__name__=_C
_CistInfoPortState_Object=MibTableColumn
cistInfoPortState=_CistInfoPortState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,2,1,4),_CistInfoPortState_Type())
cistInfoPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortState.setStatus(_A)
class _CistInfoPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),('alternate',2),('backup',3),('root',4),('designated',5),('master',6),(_W,7)))
_CistInfoPortRole_Type.__name__=_C
_CistInfoPortRole_Object=MibTableColumn
cistInfoPortRole=_CistInfoPortRole_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,2,1,5),_CistInfoPortRole_Type())
cistInfoPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortRole.setStatus(_A)
_CistInfoPortDesignatedBridge_Type=BridgeId
_CistInfoPortDesignatedBridge_Object=MibTableColumn
cistInfoPortDesignatedBridge=_CistInfoPortDesignatedBridge_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,2,1,6),_CistInfoPortDesignatedBridge_Type())
cistInfoPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortDesignatedBridge.setStatus(_A)
class _CistInfoPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_CistInfoPortDesignatedPort_Type.__name__=_M
_CistInfoPortDesignatedPort_Object=MibTableColumn
cistInfoPortDesignatedPort=_CistInfoPortDesignatedPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,2,1,7),_CistInfoPortDesignatedPort_Type())
cistInfoPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortDesignatedPort.setStatus(_A)
class _CistInfoPortLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_W,3)))
_CistInfoPortLinkType_Type.__name__=_C
_CistInfoPortLinkType_Object=MibTableColumn
cistInfoPortLinkType=_CistInfoPortLinkType_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,2,1,8),_CistInfoPortLinkType_Type())
cistInfoPortLinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortLinkType.setStatus(_A)
class _CistInfoPortHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CistInfoPortHelloTime_Type.__name__=_C
_CistInfoPortHelloTime_Object=MibTableColumn
cistInfoPortHelloTime=_CistInfoPortHelloTime_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,1,2,1,9),_CistInfoPortHelloTime_Type())
cistInfoPortHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortHelloTime.setStatus(_A)
_FdbInfo_ObjectIdentity=ObjectIdentity
fdbInfo=_FdbInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,2))
class _FdbClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('clear',2)))
_FdbClear_Type.__name__=_C
_FdbClear_Object=MibScalar
fdbClear=_FdbClear_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,2,1),_FdbClear_Type())
fdbClear.setMaxAccess(_E)
if mibBuilder.loadTexts:fdbClear.setStatus(_A)
_FdbTable_Object=MibTable
fdbTable=_FdbTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,2,2))
if mibBuilder.loadTexts:fdbTable.setStatus(_A)
_FdbEntry_Object=MibTableRow
fdbEntry=_FdbEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,2,2,1))
fdbEntry.setIndexNames((0,_F,_A5))
if mibBuilder.loadTexts:fdbEntry.setStatus(_A)
_FdbMacAddr_Type=PhysAddress
_FdbMacAddr_Object=MibTableColumn
fdbMacAddr=_FdbMacAddr_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,2,2,1,1),_FdbMacAddr_Type())
fdbMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbMacAddr.setStatus(_A)
_FdbVlan_Type=Integer32
_FdbVlan_Object=MibTableColumn
fdbVlan=_FdbVlan_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,2,2,1,2),_FdbVlan_Type())
fdbVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbVlan.setStatus(_A)
_FdbSrcPort_Type=Integer32
_FdbSrcPort_Object=MibTableColumn
fdbSrcPort=_FdbSrcPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,2,2,1,3),_FdbSrcPort_Type())
fdbSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbSrcPort.setStatus(_A)
class _FdbState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_W,1),('ignore',2),('forward',3),('flood',4),('ffd',5),('trunk',6),('vir',7),('vsr',8),('vpr',9),(_P,10)))
_FdbState_Type.__name__=_C
_FdbState_Object=MibTableColumn
fdbState=_FdbState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,2,2,1,4),_FdbState_Type())
fdbState.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbState.setStatus(_A)
class _FdbRefSps_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FdbRefSps_Type.__name__=_O
_FdbRefSps_Object=MibTableColumn
fdbRefSps=_FdbRefSps_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,2,2,1,5),_FdbRefSps_Type())
fdbRefSps.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbRefSps.setStatus(_A)
_FdbLearnedPort_Type=Integer32
_FdbLearnedPort_Object=MibTableColumn
fdbLearnedPort=_FdbLearnedPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,2,2,1,6),_FdbLearnedPort_Type())
fdbLearnedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbLearnedPort.setStatus(_A)
_FdbSrcTrunk_Type=Integer32
_FdbSrcTrunk_Object=MibTableColumn
fdbSrcTrunk=_FdbSrcTrunk_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,2,2,1,7),_FdbSrcTrunk_Type())
fdbSrcTrunk.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbSrcTrunk.setStatus(_A)
_StpInfo_ObjectIdentity=ObjectIdentity
stpInfo=_StpInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3))
_StpInfoTable_Object=MibTable
stpInfoTable=_StpInfoTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1))
if mibBuilder.loadTexts:stpInfoTable.setStatus(_A)
_StpInfoTableEntry_Object=MibTableRow
stpInfoTableEntry=_StpInfoTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1))
stpInfoTableEntry.setIndexNames((0,_F,_A6))
if mibBuilder.loadTexts:stpInfoTableEntry.setStatus(_A)
_StpInfoIndex_Type=Integer32
_StpInfoIndex_Object=MibTableColumn
stpInfoIndex=_StpInfoIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,1),_StpInfoIndex_Type())
stpInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoIndex.setStatus(_A)
class _StpInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_I,2)))
_StpInfoState_Type.__name__=_C
_StpInfoState_Object=MibTableColumn
stpInfoState=_StpInfoState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,2),_StpInfoState_Type())
stpInfoState.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoState.setStatus(_A)
class _StgInfoVlanBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_StgInfoVlanBmap_Type.__name__=_M
_StgInfoVlanBmap_Object=MibTableColumn
stgInfoVlanBmap=_StgInfoVlanBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,3),_StgInfoVlanBmap_Type())
stgInfoVlanBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:stgInfoVlanBmap.setStatus(_A)
_StpInfoTimeSinceTopChange_Type=TimeTicks
_StpInfoTimeSinceTopChange_Object=MibTableColumn
stpInfoTimeSinceTopChange=_StpInfoTimeSinceTopChange_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,4),_StpInfoTimeSinceTopChange_Type())
stpInfoTimeSinceTopChange.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoTimeSinceTopChange.setStatus(_A)
_StpInfoTopChanges_Type=Counter32
_StpInfoTopChanges_Object=MibTableColumn
stpInfoTopChanges=_StpInfoTopChanges_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,5),_StpInfoTopChanges_Type())
stpInfoTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoTopChanges.setStatus(_A)
_StpInfoDesignatedRoot_Type=BridgeId
_StpInfoDesignatedRoot_Object=MibTableColumn
stpInfoDesignatedRoot=_StpInfoDesignatedRoot_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,6),_StpInfoDesignatedRoot_Type())
stpInfoDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoDesignatedRoot.setStatus(_A)
_StpInfoRootCost_Type=Integer32
_StpInfoRootCost_Object=MibTableColumn
stpInfoRootCost=_StpInfoRootCost_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,7),_StpInfoRootCost_Type())
stpInfoRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoRootCost.setStatus(_A)
_StpInfoRootPort_Type=Integer32
_StpInfoRootPort_Object=MibTableColumn
stpInfoRootPort=_StpInfoRootPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,8),_StpInfoRootPort_Type())
stpInfoRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoRootPort.setStatus(_A)
_StpInfoMaxAge_Type=Integer32
_StpInfoMaxAge_Object=MibTableColumn
stpInfoMaxAge=_StpInfoMaxAge_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,9),_StpInfoMaxAge_Type())
stpInfoMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoMaxAge.setStatus(_A)
_StpInfoHelloTime_Type=Integer32
_StpInfoHelloTime_Object=MibTableColumn
stpInfoHelloTime=_StpInfoHelloTime_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,10),_StpInfoHelloTime_Type())
stpInfoHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoHelloTime.setStatus(_A)
_StpInfoForwardDelay_Type=Integer32
_StpInfoForwardDelay_Object=MibTableColumn
stpInfoForwardDelay=_StpInfoForwardDelay_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,11),_StpInfoForwardDelay_Type())
stpInfoForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoForwardDelay.setStatus(_A)
_StpInfoHoldTime_Type=Integer32
_StpInfoHoldTime_Object=MibTableColumn
stpInfoHoldTime=_StpInfoHoldTime_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,12),_StpInfoHoldTime_Type())
stpInfoHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoHoldTime.setStatus(_A)
class _StpInfoBrgPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StpInfoBrgPriority_Type.__name__=_C
_StpInfoBrgPriority_Object=MibTableColumn
stpInfoBrgPriority=_StpInfoBrgPriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,13),_StpInfoBrgPriority_Type())
stpInfoBrgPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoBrgPriority.setStatus(_A)
class _StpInfoBrgHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_StpInfoBrgHelloTime_Type.__name__=_C
_StpInfoBrgHelloTime_Object=MibTableColumn
stpInfoBrgHelloTime=_StpInfoBrgHelloTime_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,14),_StpInfoBrgHelloTime_Type())
stpInfoBrgHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoBrgHelloTime.setStatus(_A)
class _StpInfoBrgForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_StpInfoBrgForwardDelay_Type.__name__=_C
_StpInfoBrgForwardDelay_Object=MibTableColumn
stpInfoBrgForwardDelay=_StpInfoBrgForwardDelay_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,15),_StpInfoBrgForwardDelay_Type())
stpInfoBrgForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoBrgForwardDelay.setStatus(_A)
class _StpInfoBrgMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_StpInfoBrgMaxAge_Type.__name__=_C
_StpInfoBrgMaxAge_Object=MibTableColumn
stpInfoBrgMaxAge=_StpInfoBrgMaxAge_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,16),_StpInfoBrgMaxAge_Type())
stpInfoBrgMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoBrgMaxAge.setStatus(_A)
class _StpInfoAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StpInfoAgingTime_Type.__name__=_C
_StpInfoAgingTime_Object=MibTableColumn
stpInfoAgingTime=_StpInfoAgingTime_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,1,1,17),_StpInfoAgingTime_Type())
stpInfoAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoAgingTime.setStatus(_A)
_StpInfoPortTable_Object=MibTable
stpInfoPortTable=_StpInfoPortTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,2))
if mibBuilder.loadTexts:stpInfoPortTable.setStatus(_A)
_StpInfoPortTableEntry_Object=MibTableRow
stpInfoPortTableEntry=_StpInfoPortTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,2,1))
stpInfoPortTableEntry.setIndexNames((0,_F,_A7),(0,_F,_A8))
if mibBuilder.loadTexts:stpInfoPortTableEntry.setStatus(_A)
_StpInfoPortStpIndex_Type=Integer32
_StpInfoPortStpIndex_Object=MibTableColumn
stpInfoPortStpIndex=_StpInfoPortStpIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,2,1,1),_StpInfoPortStpIndex_Type())
stpInfoPortStpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortStpIndex.setStatus(_A)
_StpInfoPortIndex_Type=Integer32
_StpInfoPortIndex_Object=MibTableColumn
stpInfoPortIndex=_StpInfoPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,2,1,2),_StpInfoPortIndex_Type())
stpInfoPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortIndex.setStatus(_A)
class _StpInfoPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('blocking',2),('listening',3),('learning',4),(_A4,5),('broken',6)))
_StpInfoPortState_Type.__name__=_C
_StpInfoPortState_Object=MibTableColumn
stpInfoPortState=_StpInfoPortState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,2,1,3),_StpInfoPortState_Type())
stpInfoPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortState.setStatus(_A)
_StpInfoPortDesignatedRoot_Type=BridgeId
_StpInfoPortDesignatedRoot_Object=MibTableColumn
stpInfoPortDesignatedRoot=_StpInfoPortDesignatedRoot_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,2,1,4),_StpInfoPortDesignatedRoot_Type())
stpInfoPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortDesignatedRoot.setStatus(_A)
_StpInfoPortDesignatedCost_Type=Integer32
_StpInfoPortDesignatedCost_Object=MibTableColumn
stpInfoPortDesignatedCost=_StpInfoPortDesignatedCost_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,2,1,5),_StpInfoPortDesignatedCost_Type())
stpInfoPortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortDesignatedCost.setStatus(_A)
_StpInfoPortDesignatedBridge_Type=BridgeId
_StpInfoPortDesignatedBridge_Object=MibTableColumn
stpInfoPortDesignatedBridge=_StpInfoPortDesignatedBridge_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,2,1,6),_StpInfoPortDesignatedBridge_Type())
stpInfoPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortDesignatedBridge.setStatus(_A)
class _StpInfoPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_StpInfoPortDesignatedPort_Type.__name__=_M
_StpInfoPortDesignatedPort_Object=MibTableColumn
stpInfoPortDesignatedPort=_StpInfoPortDesignatedPort_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,2,1,7),_StpInfoPortDesignatedPort_Type())
stpInfoPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortDesignatedPort.setStatus(_A)
_StpInfoPortForwardTransitions_Type=Counter32
_StpInfoPortForwardTransitions_Object=MibTableColumn
stpInfoPortForwardTransitions=_StpInfoPortForwardTransitions_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,2,1,8),_StpInfoPortForwardTransitions_Type())
stpInfoPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortForwardTransitions.setStatus(_A)
_StpInfoPortPathCost_Type=Integer32
_StpInfoPortPathCost_Object=MibTableColumn
stpInfoPortPathCost=_StpInfoPortPathCost_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,3,2,1,9),_StpInfoPortPathCost_Type())
stpInfoPortPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortPathCost.setStatus(_A)
_LacpInfo_ObjectIdentity=ObjectIdentity
lacpInfo=_LacpInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,4))
_LacpInfoPortTable_Object=MibTable
lacpInfoPortTable=_LacpInfoPortTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,4,1))
if mibBuilder.loadTexts:lacpInfoPortTable.setStatus(_A)
_LacpInfoPortTableEntry_Object=MibTableRow
lacpInfoPortTableEntry=_LacpInfoPortTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,4,1,1))
lacpInfoPortTableEntry.setIndexNames((0,_F,_A9))
if mibBuilder.loadTexts:lacpInfoPortTableEntry.setStatus(_A)
_LacpInfoPortIndex_Type=Integer32
_LacpInfoPortIndex_Object=MibTableColumn
lacpInfoPortIndex=_LacpInfoPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,4,1,1,1),_LacpInfoPortIndex_Type())
lacpInfoPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpInfoPortIndex.setStatus(_A)
class _LacpInfoPortSelected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('selected',1),('unselected',2),('standby',3)))
_LacpInfoPortSelected_Type.__name__=_C
_LacpInfoPortSelected_Object=MibTableColumn
lacpInfoPortSelected=_LacpInfoPortSelected_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,4,1,1,2),_LacpInfoPortSelected_Type())
lacpInfoPortSelected.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpInfoPortSelected.setStatus(_A)
class _LacpInfoPortNtt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_LacpInfoPortNtt_Type.__name__=_C
_LacpInfoPortNtt_Object=MibTableColumn
lacpInfoPortNtt=_LacpInfoPortNtt_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,4,1,1,3),_LacpInfoPortNtt_Type())
lacpInfoPortNtt.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpInfoPortNtt.setStatus(_A)
class _LacpInfoPortReadyN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_LacpInfoPortReadyN_Type.__name__=_C
_LacpInfoPortReadyN_Object=MibTableColumn
lacpInfoPortReadyN=_LacpInfoPortReadyN_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,4,1,1,4),_LacpInfoPortReadyN_Type())
lacpInfoPortReadyN.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpInfoPortReadyN.setStatus(_A)
class _LacpInfoPortMoved_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_LacpInfoPortMoved_Type.__name__=_C
_LacpInfoPortMoved_Object=MibTableColumn
lacpInfoPortMoved=_LacpInfoPortMoved_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,4,1,1,5),_LacpInfoPortMoved_Type())
lacpInfoPortMoved.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpInfoPortMoved.setStatus(_A)
_Dot1xInfo_ObjectIdentity=ObjectIdentity
dot1xInfo=_Dot1xInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,5))
_Dot1xInfoPortTable_Object=MibTable
dot1xInfoPortTable=_Dot1xInfoPortTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,5,1))
if mibBuilder.loadTexts:dot1xInfoPortTable.setStatus(_A)
_Dot1xInfoPortEntry_Object=MibTableRow
dot1xInfoPortEntry=_Dot1xInfoPortEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,5,1,1))
dot1xInfoPortEntry.setIndexNames((0,_F,_AA))
if mibBuilder.loadTexts:dot1xInfoPortEntry.setStatus(_A)
_Dot1xInfoPortIndex_Type=Integer32
_Dot1xInfoPortIndex_Object=MibTableColumn
dot1xInfoPortIndex=_Dot1xInfoPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,5,1,1,1),_Dot1xInfoPortIndex_Type())
dot1xInfoPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xInfoPortIndex.setStatus(_A)
class _Dot1xInfoPortAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_T,0),(_N,1),(_U,2)))
_Dot1xInfoPortAuthMode_Type.__name__=_C
_Dot1xInfoPortAuthMode_Object=MibTableColumn
dot1xInfoPortAuthMode=_Dot1xInfoPortAuthMode_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,5,1,1,2),_Dot1xInfoPortAuthMode_Type())
dot1xInfoPortAuthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xInfoPortAuthMode.setStatus(_A)
class _Dot1xInfoPortAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('authorized',0),('unauthorized',1)))
_Dot1xInfoPortAuthStatus_Type.__name__=_C
_Dot1xInfoPortAuthStatus_Object=MibTableColumn
dot1xInfoPortAuthStatus=_Dot1xInfoPortAuthStatus_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,5,1,1,3),_Dot1xInfoPortAuthStatus_Type())
dot1xInfoPortAuthStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xInfoPortAuthStatus.setStatus(_A)
class _Dot1xInfoPortCtrlDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_X,0),('in',1)))
_Dot1xInfoPortCtrlDir_Type.__name__=_C
_Dot1xInfoPortCtrlDir_Object=MibTableColumn
dot1xInfoPortCtrlDir=_Dot1xInfoPortCtrlDir_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,5,1,1,4),_Dot1xInfoPortCtrlDir_Type())
dot1xInfoPortCtrlDir.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xInfoPortCtrlDir.setStatus(_A)
class _Dot1xInfoPortAuthPAEState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_AB,0),('disconnected',1),('connecting',2),('authenticating',3),('authenticated',4),('aborting',5),('held',6),('forceauth',7),('forceunauth',8)))
_Dot1xInfoPortAuthPAEState_Type.__name__=_C
_Dot1xInfoPortAuthPAEState_Object=MibTableColumn
dot1xInfoPortAuthPAEState=_Dot1xInfoPortAuthPAEState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,5,1,1,5),_Dot1xInfoPortAuthPAEState_Type())
dot1xInfoPortAuthPAEState.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xInfoPortAuthPAEState.setStatus(_A)
class _Dot1xInfoPortBackAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('request',0),('response',1),('success',2),('fail',3),('timeout',4),('idle',5),(_AB,6)))
_Dot1xInfoPortBackAuthState_Type.__name__=_C
_Dot1xInfoPortBackAuthState_Object=MibTableColumn
dot1xInfoPortBackAuthState=_Dot1xInfoPortBackAuthState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,5,1,1,6),_Dot1xInfoPortBackAuthState_Type())
dot1xInfoPortBackAuthState.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xInfoPortBackAuthState.setStatus(_A)
_Dot1xSystemInfo_ObjectIdentity=ObjectIdentity
dot1xSystemInfo=_Dot1xSystemInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,5,2))
class _Dot1xSystemCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('authenticator',0),('supplicant',1),('authenticatorAndSupplicant',2),(_W,3)))
_Dot1xSystemCapability_Type.__name__=_C
_Dot1xSystemCapability_Object=MibScalar
dot1xSystemCapability=_Dot1xSystemCapability_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,5,2,1),_Dot1xSystemCapability_Type())
dot1xSystemCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xSystemCapability.setStatus(_A)
class _Dot1xSystemStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_G,1)))
_Dot1xSystemStatus_Type.__name__=_C
_Dot1xSystemStatus_Object=MibScalar
dot1xSystemStatus=_Dot1xSystemStatus_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,5,2,2),_Dot1xSystemStatus_Type())
dot1xSystemStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xSystemStatus.setStatus(_A)
_Dot1xSystemProtoVersion_Type=Integer32
_Dot1xSystemProtoVersion_Object=MibScalar
dot1xSystemProtoVersion=_Dot1xSystemProtoVersion_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,5,2,3),_Dot1xSystemProtoVersion_Type())
dot1xSystemProtoVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xSystemProtoVersion.setStatus(_A)
_Dot1pInfo_ObjectIdentity=ObjectIdentity
dot1pInfo=_Dot1pInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,6))
_Dot1pInfoPriorityCOSTable_Object=MibTable
dot1pInfoPriorityCOSTable=_Dot1pInfoPriorityCOSTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,6,1))
if mibBuilder.loadTexts:dot1pInfoPriorityCOSTable.setStatus(_A)
_Dot1pInfoPriorityCOSEntry_Object=MibTableRow
dot1pInfoPriorityCOSEntry=_Dot1pInfoPriorityCOSEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,6,1,1))
dot1pInfoPriorityCOSEntry.setIndexNames((0,_F,_AC))
if mibBuilder.loadTexts:dot1pInfoPriorityCOSEntry.setStatus(_A)
class _Dot1pInfoPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1pInfoPriorityIndex_Type.__name__=_C
_Dot1pInfoPriorityIndex_Object=MibTableColumn
dot1pInfoPriorityIndex=_Dot1pInfoPriorityIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,6,1,1,1),_Dot1pInfoPriorityIndex_Type())
dot1pInfoPriorityIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1pInfoPriorityIndex.setStatus(_A)
_Dot1pInfoPriorityCOSQueue_Type=Integer32
_Dot1pInfoPriorityCOSQueue_Object=MibTableColumn
dot1pInfoPriorityCOSQueue=_Dot1pInfoPriorityCOSQueue_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,6,1,1,2),_Dot1pInfoPriorityCOSQueue_Type())
dot1pInfoPriorityCOSQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1pInfoPriorityCOSQueue.setStatus(_A)
_Dot1pInfoPriorityCOSWeight_Type=Integer32
_Dot1pInfoPriorityCOSWeight_Object=MibTableColumn
dot1pInfoPriorityCOSWeight=_Dot1pInfoPriorityCOSWeight_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,6,1,1,3),_Dot1pInfoPriorityCOSWeight_Type())
dot1pInfoPriorityCOSWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1pInfoPriorityCOSWeight.setStatus(_A)
_Dot1pInfoPortTable_Object=MibTable
dot1pInfoPortTable=_Dot1pInfoPortTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,6,2))
if mibBuilder.loadTexts:dot1pInfoPortTable.setStatus(_A)
_Dot1pInfoPortEntry_Object=MibTableRow
dot1pInfoPortEntry=_Dot1pInfoPortEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,6,2,1))
dot1pInfoPortEntry.setIndexNames((0,_F,_AD))
if mibBuilder.loadTexts:dot1pInfoPortEntry.setStatus(_A)
_Dot1pInfoPortIndex_Type=Integer32
_Dot1pInfoPortIndex_Object=MibTableColumn
dot1pInfoPortIndex=_Dot1pInfoPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,6,2,1,1),_Dot1pInfoPortIndex_Type())
dot1pInfoPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1pInfoPortIndex.setStatus(_A)
_Dot1pInfoPortPriority_Type=Integer32
_Dot1pInfoPortPriority_Object=MibTableColumn
dot1pInfoPortPriority=_Dot1pInfoPortPriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,6,2,1,2),_Dot1pInfoPortPriority_Type())
dot1pInfoPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1pInfoPortPriority.setStatus(_A)
_Dot1pInfoPortCOSq_Type=Integer32
_Dot1pInfoPortCOSq_Object=MibTableColumn
dot1pInfoPortCOSq=_Dot1pInfoPortCOSq_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,6,2,1,3),_Dot1pInfoPortCOSq_Type())
dot1pInfoPortCOSq.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1pInfoPortCOSq.setStatus(_A)
_Dot1pInfoPortWeight_Type=Integer32
_Dot1pInfoPortWeight_Object=MibTableColumn
dot1pInfoPortWeight=_Dot1pInfoPortWeight_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,6,2,1,4),_Dot1pInfoPortWeight_Type())
dot1pInfoPortWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1pInfoPortWeight.setStatus(_A)
_GenInfo_ObjectIdentity=ObjectIdentity
genInfo=_GenInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,7))
class _GeneralInfoStpUplinkFast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_GeneralInfoStpUplinkFast_Type.__name__=_C
_GeneralInfoStpUplinkFast_Object=MibScalar
generalInfoStpUplinkFast=_GeneralInfoStpUplinkFast_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,7,1),_GeneralInfoStpUplinkFast_Type())
generalInfoStpUplinkFast.setMaxAccess(_B)
if mibBuilder.loadTexts:generalInfoStpUplinkFast.setStatus(_A)
_GeneralInfoUplinkFastRate_Type=Integer32
_GeneralInfoUplinkFastRate_Object=MibScalar
generalInfoUplinkFastRate=_GeneralInfoUplinkFastRate_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,7,2),_GeneralInfoUplinkFastRate_Type())
generalInfoUplinkFastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:generalInfoUplinkFastRate.setStatus(_A)
_VlanInfo_ObjectIdentity=ObjectIdentity
vlanInfo=_VlanInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,8))
_VlanInfoTable_Object=MibTable
vlanInfoTable=_VlanInfoTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,8,1))
if mibBuilder.loadTexts:vlanInfoTable.setStatus(_A)
_VlanInfoTableEntry_Object=MibTableRow
vlanInfoTableEntry=_VlanInfoTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,8,1,1))
vlanInfoTableEntry.setIndexNames((0,_F,_AE))
if mibBuilder.loadTexts:vlanInfoTableEntry.setStatus(_A)
class _VlanInfoId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_VlanInfoId_Type.__name__=_C
_VlanInfoId_Object=MibTableColumn
vlanInfoId=_VlanInfoId_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,8,1,1,1),_VlanInfoId_Type())
vlanInfoId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanInfoId.setStatus(_A)
class _VlanInfoName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VlanInfoName_Type.__name__=_O
_VlanInfoName_Object=MibTableColumn
vlanInfoName=_VlanInfoName_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,8,1,1,2),_VlanInfoName_Type())
vlanInfoName.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanInfoName.setStatus(_A)
class _VlanInfoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_G,3)))
_VlanInfoStatus_Type.__name__=_C
_VlanInfoStatus_Object=MibTableColumn
vlanInfoStatus=_VlanInfoStatus_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,8,1,1,3),_VlanInfoStatus_Type())
vlanInfoStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanInfoStatus.setStatus(_A)
_VlanInfoPorts_Type=OctetString
_VlanInfoPorts_Object=MibTableColumn
vlanInfoPorts=_VlanInfoPorts_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,8,1,1,4),_VlanInfoPorts_Type())
vlanInfoPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanInfoPorts.setStatus(_A)
_TrunkGroupInfo_ObjectIdentity=ObjectIdentity
trunkGroupInfo=_TrunkGroupInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,9))
_TrunkGroupInfoTable_Object=MibTable
trunkGroupInfoTable=_TrunkGroupInfoTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,9,1))
if mibBuilder.loadTexts:trunkGroupInfoTable.setStatus(_A)
_TrunkGroupInfoTableEntry_Object=MibTableRow
trunkGroupInfoTableEntry=_TrunkGroupInfoTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,9,1,1))
trunkGroupInfoTableEntry.setIndexNames((0,_F,_AF))
if mibBuilder.loadTexts:trunkGroupInfoTableEntry.setStatus(_A)
_TrunkGroupInfoIndex_Type=Integer32
_TrunkGroupInfoIndex_Object=MibTableColumn
trunkGroupInfoIndex=_TrunkGroupInfoIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,9,1,1,1),_TrunkGroupInfoIndex_Type())
trunkGroupInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupInfoIndex.setStatus(_A)
class _TrunkGroupInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_TrunkGroupInfoState_Type.__name__=_C
_TrunkGroupInfoState_Object=MibTableColumn
trunkGroupInfoState=_TrunkGroupInfoState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,9,1,1,2),_TrunkGroupInfoState_Type())
trunkGroupInfoState.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupInfoState.setStatus(_A)
_TrunkGroupInfoPorts_Type=OctetString
_TrunkGroupInfoPorts_Object=MibTableColumn
trunkGroupInfoPorts=_TrunkGroupInfoPorts_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,9,1,1,3),_TrunkGroupInfoPorts_Type())
trunkGroupInfoPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupInfoPorts.setStatus(_A)
_HotlinksInfo_ObjectIdentity=ObjectIdentity
hotlinksInfo=_HotlinksInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,10))
class _HotlinksInfoOnState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_I,2)))
_HotlinksInfoOnState_Type.__name__=_C
_HotlinksInfoOnState_Object=MibScalar
hotlinksInfoOnState=_HotlinksInfoOnState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,10,1),_HotlinksInfoOnState_Type())
hotlinksInfoOnState.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksInfoOnState.setStatus(_A)
class _HotlinksInfoFdbUpdateState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_HotlinksInfoFdbUpdateState_Type.__name__=_C
_HotlinksInfoFdbUpdateState_Object=MibScalar
hotlinksInfoFdbUpdateState=_HotlinksInfoFdbUpdateState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,10,2),_HotlinksInfoFdbUpdateState_Type())
hotlinksInfoFdbUpdateState.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksInfoFdbUpdateState.setStatus(_A)
_HotlinksInfoTriggerTable_Object=MibTable
hotlinksInfoTriggerTable=_HotlinksInfoTriggerTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,10,3))
if mibBuilder.loadTexts:hotlinksInfoTriggerTable.setStatus(_A)
_HotlinksInfoTriggerTableEntry_Object=MibTableRow
hotlinksInfoTriggerTableEntry=_HotlinksInfoTriggerTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,10,3,1))
hotlinksInfoTriggerTableEntry.setIndexNames((0,_F,_AG))
if mibBuilder.loadTexts:hotlinksInfoTriggerTableEntry.setStatus(_A)
_HotlinksInfoTriggerId_Type=Integer32
_HotlinksInfoTriggerId_Object=MibTableColumn
hotlinksInfoTriggerId=_HotlinksInfoTriggerId_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,10,3,1,1),_HotlinksInfoTriggerId_Type())
hotlinksInfoTriggerId.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksInfoTriggerId.setStatus(_A)
class _HotlinksInfoTriggerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_HotlinksInfoTriggerState_Type.__name__=_C
_HotlinksInfoTriggerState_Object=MibTableColumn
hotlinksInfoTriggerState=_HotlinksInfoTriggerState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,10,3,1,2),_HotlinksInfoTriggerState_Type())
hotlinksInfoTriggerState.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksInfoTriggerState.setStatus(_A)
class _HotlinksInfoTriggerPreemptState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_HotlinksInfoTriggerPreemptState_Type.__name__=_C
_HotlinksInfoTriggerPreemptState_Object=MibTableColumn
hotlinksInfoTriggerPreemptState=_HotlinksInfoTriggerPreemptState_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,10,3,1,3),_HotlinksInfoTriggerPreemptState_Type())
hotlinksInfoTriggerPreemptState.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksInfoTriggerPreemptState.setStatus(_A)
_HotlinksInfoTriggerFdelay_Type=Integer32
_HotlinksInfoTriggerFdelay_Object=MibTableColumn
hotlinksInfoTriggerFdelay=_HotlinksInfoTriggerFdelay_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,10,3,1,4),_HotlinksInfoTriggerFdelay_Type())
hotlinksInfoTriggerFdelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksInfoTriggerFdelay.setStatus(_A)
_HotlinksInfoTriggerActive_Type=DisplayString
_HotlinksInfoTriggerActive_Object=MibTableColumn
hotlinksInfoTriggerActive=_HotlinksInfoTriggerActive_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,3,10,3,1,5),_HotlinksInfoTriggerActive_Type())
hotlinksInfoTriggerActive.setMaxAccess(_B)
if mibBuilder.loadTexts:hotlinksInfoTriggerActive.setStatus(_A)
_Layer2Oper_ObjectIdentity=ObjectIdentity
layer2Oper=_Layer2Oper_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,2,4))
mibBuilder.exportSymbols(_F,**{'layer2':layer2,'layer2Configs':layer2Configs,'vlan':vlan,'vlanMaxEnt':vlanMaxEnt,'vlanCurCfgTable':vlanCurCfgTable,'vlanCurCfgTableEntry':vlanCurCfgTableEntry,_a:vlanCurCfgVlanId,'vlanCurCfgVlanName':vlanCurCfgVlanName,'vlanCurCfgPorts':vlanCurCfgPorts,'vlanCurCfgState':vlanCurCfgState,'vlanCurCfgStg':vlanCurCfgStg,'vlanNewCfgTable':vlanNewCfgTable,'vlanNewCfgTableEntry':vlanNewCfgTableEntry,_b:vlanNewCfgVlanId,'vlanNewCfgVlanName':vlanNewCfgVlanName,'vlanNewCfgPorts':vlanNewCfgPorts,'vlanNewCfgState':vlanNewCfgState,'vlanNewCfgAddPort':vlanNewCfgAddPort,'vlanNewCfgRemovePort':vlanNewCfgRemovePort,'vlanNewCfgDelete':vlanNewCfgDelete,'vlanNewCfgStg':vlanNewCfgStg,'trunkgroup':trunkgroup,'trunkGroupTableMaxSize':trunkGroupTableMaxSize,'trunkGroupCurCfgTable':trunkGroupCurCfgTable,'trunkGroupCurCfgTableEntry':trunkGroupCurCfgTableEntry,_c:trunkGroupCurCfgIndex,'trunkGroupCurCfgPorts':trunkGroupCurCfgPorts,'trunkGroupCurCfgState':trunkGroupCurCfgState,'trunkGroupNewCfgTable':trunkGroupNewCfgTable,'trunkGroupNewCfgTableEntry':trunkGroupNewCfgTableEntry,_d:trunkGroupNewCfgIndex,'trunkGroupNewCfgPorts':trunkGroupNewCfgPorts,'trunkGroupNewCfgAddPort':trunkGroupNewCfgAddPort,'trunkGroupNewCfgRemovePort':trunkGroupNewCfgRemovePort,'trunkGroupNewCfgState':trunkGroupNewCfgState,'trunkGroupNewCfgDelete':trunkGroupNewCfgDelete,'stgCfg':stgCfg,'stgCurCfgTable':stgCurCfgTable,'stgCurCfgTableEntry':stgCurCfgTableEntry,_e:stgCurCfgIndex,'stgCurCfgState':stgCurCfgState,'stgCurCfgVlanBmap1':stgCurCfgVlanBmap1,'stgCurCfgVlanBmap2':stgCurCfgVlanBmap2,'stgCurCfgPriority':stgCurCfgPriority,'stgCurCfgBrgHelloTime':stgCurCfgBrgHelloTime,'stgCurCfgBrgForwardDelay':stgCurCfgBrgForwardDelay,'stgCurCfgBrgMaxAge':stgCurCfgBrgMaxAge,'stgCurCfgAgingTime':stgCurCfgAgingTime,'stgCurCfgVlanBmap':stgCurCfgVlanBmap,'stgNewCfgTable':stgNewCfgTable,'stgNewCfgTableEntry':stgNewCfgTableEntry,_f:stgNewCfgIndex,'stgNewCfgState':stgNewCfgState,'stgNewCfgDefaultCfg':stgNewCfgDefaultCfg,'stgNewCfgAddVlan':stgNewCfgAddVlan,'stgNewCfgRemoveVlan':stgNewCfgRemoveVlan,'stgNewCfgVlanBmap1':stgNewCfgVlanBmap1,'stgNewCfgVlanBmap2':stgNewCfgVlanBmap2,'stgNewCfgPriority':stgNewCfgPriority,'stgNewCfgBrgHelloTime':stgNewCfgBrgHelloTime,'stgNewCfgBrgForwardDelay':stgNewCfgBrgForwardDelay,'stgNewCfgBrgMaxAge':stgNewCfgBrgMaxAge,'stgNewCfgAgingTime':stgNewCfgAgingTime,'stgNewCfgVlanBmap':stgNewCfgVlanBmap,'stgCurCfgPortTable':stgCurCfgPortTable,'stgCurCfgPortTableEntry':stgCurCfgPortTableEntry,_g:stgCurCfgStgIndex,_h:stgCurCfgPortIndex,'stgCurCfgPortState':stgCurCfgPortState,'stgCurCfgPortPriority':stgCurCfgPortPriority,'stgCurCfgPortPathCost':stgCurCfgPortPathCost,'stgCurCfgPortLink':stgCurCfgPortLink,'stgCurCfgPortEdge':stgCurCfgPortEdge,'stgCurCfgPortFastFwd':stgCurCfgPortFastFwd,'stgNewCfgPortTable':stgNewCfgPortTable,'stgNewCfgPortTableEntry':stgNewCfgPortTableEntry,_i:stgNewCfgStgIndex,_j:stgNewCfgPortIndex,'stgNewCfgPortState':stgNewCfgPortState,'stgNewCfgPortPriority':stgNewCfgPortPriority,'stgNewCfgPortPathCost':stgNewCfgPortPathCost,'stgNewCfgPortLink':stgNewCfgPortLink,'stgNewCfgPortEdge':stgNewCfgPortEdge,'stgNewCfgPortFastFwd':stgNewCfgPortFastFwd,'mirroring':mirroring,'mirrPortMirr':mirrPortMirr,'pmCurCfgPortMirrState':pmCurCfgPortMirrState,'pmNewCfgPortMirrState':pmNewCfgPortMirrState,'pmCurCfgPortMonitorTable':pmCurCfgPortMonitorTable,'pmCurCfgPortMonitorEntry':pmCurCfgPortMonitorEntry,_k:pmCurCfgPmirrMoniPortIndex,_l:pmCurCfgPmirrMirrPortIndex,'pmCurCfgPmirrDirection':pmCurCfgPmirrDirection,'pmNewCfgPortMonitorTable':pmNewCfgPortMonitorTable,'pmNewCfgPortMonitorEntry':pmNewCfgPortMonitorEntry,_m:pmNewCfgPmirrMoniPortIndex,_n:pmNewCfgPmirrMirrPortIndex,'pmNewCfgPmirrDirection':pmNewCfgPmirrDirection,'pmNewCfgPmirrDelete':pmNewCfgPmirrDelete,'pmNewCfgPmonDelete':pmNewCfgPmonDelete,'mstCfg':mstCfg,'mstGeneralCfg':mstGeneralCfg,'mstCurCfgState':mstCurCfgState,'mstNewCfgState':mstNewCfgState,'mstCurCfgRegionName':mstCurCfgRegionName,'mstNewCfgRegionName':mstNewCfgRegionName,'mstCurCfgRegionVersion':mstCurCfgRegionVersion,'mstNewCfgRegionVersion':mstNewCfgRegionVersion,'mstCurCfgMaxHopCount':mstCurCfgMaxHopCount,'mstNewCfgMaxHopCount':mstNewCfgMaxHopCount,'mstCurCfgStpMode':mstCurCfgStpMode,'mstNewCfgStpMode':mstNewCfgStpMode,'mstCistCfg':mstCistCfg,'mstCistDefaultCfg':mstCistDefaultCfg,'mstCistBridgeCfg':mstCistBridgeCfg,'mstCistCurCfgBridgePriority':mstCistCurCfgBridgePriority,'mstCistNewCfgBridgePriority':mstCistNewCfgBridgePriority,'mstCistCurCfgBridgeMaxAge':mstCistCurCfgBridgeMaxAge,'mstCistNewCfgBridgeMaxAge':mstCistNewCfgBridgeMaxAge,'mstCistCurCfgBridgeForwardDelay':mstCistCurCfgBridgeForwardDelay,'mstCistNewCfgBridgeForwardDelay':mstCistNewCfgBridgeForwardDelay,'mstCistCurCfgVlanBmap':mstCistCurCfgVlanBmap,'mstCistNewCfgVlanBmap':mstCistNewCfgVlanBmap,'mstCistNewCfgAddVlan':mstCistNewCfgAddVlan,'mstCistCurCfgPortTable':mstCistCurCfgPortTable,'mstCistCurCfgPortTableEntry':mstCistCurCfgPortTableEntry,_o:mstCistCurCfgPortIndex,'mstCistCurCfgPortPriority':mstCistCurCfgPortPriority,'mstCistCurCfgPortPathCost':mstCistCurCfgPortPathCost,'mstCistCurCfgPortLinkType':mstCistCurCfgPortLinkType,'mstCistCurCfgPortEdge':mstCistCurCfgPortEdge,'mstCistCurCfgPortStpState':mstCistCurCfgPortStpState,'mstCistCurCfgPortHelloTime':mstCistCurCfgPortHelloTime,'mstCistNewCfgPortTable':mstCistNewCfgPortTable,'mstCistNewCfgPortTableEntry':mstCistNewCfgPortTableEntry,_p:mstCistNewCfgPortIndex,'mstCistNewCfgPortPriority':mstCistNewCfgPortPriority,'mstCistNewCfgPortPathCost':mstCistNewCfgPortPathCost,'mstCistNewCfgPortLinkType':mstCistNewCfgPortLinkType,'mstCistNewCfgPortEdge':mstCistNewCfgPortEdge,'mstCistNewCfgPortStpState':mstCistNewCfgPortStpState,'mstCistNewCfgPortHelloTime':mstCistNewCfgPortHelloTime,'lacp':lacp,'lacpCurSystemPriority':lacpCurSystemPriority,'lacpNewSystemPriority':lacpNewSystemPriority,'lacpCurSystemTimeoutTime':lacpCurSystemTimeoutTime,'lacpNewSystemTimeoutTime':lacpNewSystemTimeoutTime,'lacpCurPortCfgTable':lacpCurPortCfgTable,'lacpCurPortCfgTableEntry':lacpCurPortCfgTableEntry,_q:lacpCurPortCfgTableId,'lacpCurPortState':lacpCurPortState,'lacpCurPortActorPortPriority':lacpCurPortActorPortPriority,'lacpCurPortActorAdminKey':lacpCurPortActorAdminKey,'lacpNewPortCfgTable':lacpNewPortCfgTable,'lacpNewPortCfgTableEntry':lacpNewPortCfgTableEntry,_t:lacpNewPortCfgTableId,'lacpNewPortState':lacpNewPortState,'lacpNewPortActorPortPriority':lacpNewPortActorPortPriority,'lacpNewPortActorAdminKey':lacpNewPortActorAdminKey,'thash':thash,'thashL2':thashL2,'l2ThashCurCfgSmacState':l2ThashCurCfgSmacState,'l2ThashNewCfgSmacState':l2ThashNewCfgSmacState,'l2ThashCurCfgDmacState':l2ThashCurCfgDmacState,'l2ThashNewCfgDmacState':l2ThashNewCfgDmacState,'l2ThashCurCfgSipState':l2ThashCurCfgSipState,'l2ThashNewCfgSipState':l2ThashNewCfgSipState,'l2ThashCurCfgDipState':l2ThashCurCfgDipState,'l2ThashNewCfgDipState':l2ThashNewCfgDipState,'l2GeneralCfg':l2GeneralCfg,'upfastCurCfgState':upfastCurCfgState,'upfastNewCfgState':upfastNewCfgState,'updateCurCfgState':updateCurCfgState,'updateNewCfgState':updateNewCfgState,'ufd':ufd,'ufdGeneralCfg':ufdGeneralCfg,'ufdCurCfgState':ufdCurCfgState,'ufdNewCfgState':ufdNewCfgState,'ufdCurCfgLtMPorts':ufdCurCfgLtMPorts,'ufdNewCfgLtMPorts':ufdNewCfgLtMPorts,'ufdCurCfgLtMTrunks':ufdCurCfgLtMTrunks,'ufdNewCfgLtMTrunks':ufdNewCfgLtMTrunks,'ufdCurCfgLtDPorts':ufdCurCfgLtDPorts,'ufdNewCfgLtDPorts':ufdNewCfgLtDPorts,'ufdCurCfgLtDTrunks':ufdCurCfgLtDTrunks,'ufdNewCfgLtDTrunks':ufdNewCfgLtDTrunks,'ufdNewCfgAddLtMPort':ufdNewCfgAddLtMPort,'ufdNewCfgRemoveLtMPort':ufdNewCfgRemoveLtMPort,'ufdNewCfgAddLtMTrunk':ufdNewCfgAddLtMTrunk,'ufdNewCfgRemoveLtMTrunk':ufdNewCfgRemoveLtMTrunk,'ufdNewCfgAddLtDPort':ufdNewCfgAddLtDPort,'ufdNewCfgRemoveLtDPort':ufdNewCfgRemoveLtDPort,'ufdNewCfgAddLtDTrunk':ufdNewCfgAddLtDTrunk,'ufdNewCfgRemoveLtDTrunk':ufdNewCfgRemoveLtDTrunk,'ufdCurCfgGlobalState':ufdCurCfgGlobalState,'ufdNewCfgGlobalState':ufdNewCfgGlobalState,'dot1x':dot1x,'dot1xCurStatus':dot1xCurStatus,'dot1xNewStatus':dot1xNewStatus,'dot1xCurCfgPortTable':dot1xCurCfgPortTable,'dot1xCurCfgPortEntry':dot1xCurCfgPortEntry,_u:dot1xCurCfgPortIndex,'dot1xCurCfgPortMode':dot1xCurCfgPortMode,'dot1xCurCfgPortQtPeriod':dot1xCurCfgPortQtPeriod,'dot1xCurCfgPortTxPeriod':dot1xCurCfgPortTxPeriod,'dot1xCurCfgPortSupTmout':dot1xCurCfgPortSupTmout,'dot1xCurCfgPortSrvTmout':dot1xCurCfgPortSrvTmout,'dot1xCurCfgPortMaxRq':dot1xCurCfgPortMaxRq,'dot1xCurCfgPortRaPeriod':dot1xCurCfgPortRaPeriod,'dot1xCurCfgPortReAuth':dot1xCurCfgPortReAuth,'dot1xNewCfgPortTable':dot1xNewCfgPortTable,'dot1xNewCfgPortEntry':dot1xNewCfgPortEntry,_v:dot1xNewCfgPortIndex,'dot1xNewCfgPortMode':dot1xNewCfgPortMode,'dot1xNewCfgPortQtPeriod':dot1xNewCfgPortQtPeriod,'dot1xNewCfgPortTxPeriod':dot1xNewCfgPortTxPeriod,'dot1xNewCfgPortSupTmout':dot1xNewCfgPortSupTmout,'dot1xNewCfgPortSrvTmout':dot1xNewCfgPortSrvTmout,'dot1xNewCfgPortMaxRq':dot1xNewCfgPortMaxRq,'dot1xNewCfgPortRaPeriod':dot1xNewCfgPortRaPeriod,'dot1xNewCfgPortReAuth':dot1xNewCfgPortReAuth,'dot1xNewCfgPortDefault':dot1xNewCfgPortDefault,'dot1xNewCfgPortApplyGlobal':dot1xNewCfgPortApplyGlobal,'dot1xCurCfgGlobalTable':dot1xCurCfgGlobalTable,'dot1xCurCfgGlobalMode':dot1xCurCfgGlobalMode,'dot1xCurCfgGlobalQtPeriod':dot1xCurCfgGlobalQtPeriod,'dot1xCurCfgGlobalTxPeriod':dot1xCurCfgGlobalTxPeriod,'dot1xCurCfgGlobalSupTmout':dot1xCurCfgGlobalSupTmout,'dot1xCurCfgGlobalSrvTmout':dot1xCurCfgGlobalSrvTmout,'dot1xCurCfgGlobalMaxRq':dot1xCurCfgGlobalMaxRq,'dot1xCurCfgGlobalRaPeriod':dot1xCurCfgGlobalRaPeriod,'dot1xCurCfgGlobalReAuth':dot1xCurCfgGlobalReAuth,'dot1xNewCfgGlobalTable':dot1xNewCfgGlobalTable,'dot1xNewCfgGlobalMode':dot1xNewCfgGlobalMode,'dot1xNewCfgGlobalQtPeriod':dot1xNewCfgGlobalQtPeriod,'dot1xNewCfgGlobalTxPeriod':dot1xNewCfgGlobalTxPeriod,'dot1xNewCfgGlobalSupTmout':dot1xNewCfgGlobalSupTmout,'dot1xNewCfgGlobalSrvTmout':dot1xNewCfgGlobalSrvTmout,'dot1xNewCfgGlobalMaxRq':dot1xNewCfgGlobalMaxRq,'dot1xNewCfgGlobalRaPeriod':dot1xNewCfgGlobalRaPeriod,'dot1xNewCfgGlobalReAuth':dot1xNewCfgGlobalReAuth,'fdb':fdb,'fdbGeneralCfg':fdbGeneralCfg,'fdbCurCfgAgingTime':fdbCurCfgAgingTime,'fdbNewCfgAgingTime':fdbNewCfgAgingTime,'fdbNewCfgStaticTable':fdbNewCfgStaticTable,'fdbNewCfgStaticEntry':fdbNewCfgStaticEntry,_w:fdbNewCfgEntryIndex,'fdbNewCfgAddVlan':fdbNewCfgAddVlan,'fdbNewCfgAddPort':fdbNewCfgAddPort,'fdbNewCfgAddMac':fdbNewCfgAddMac,'fdbNewCfgDelStaticEntry':fdbNewCfgDelStaticEntry,'hotlinksCfg':hotlinksCfg,'hotlinksCurCfgOnState':hotlinksCurCfgOnState,'hotlinksNewCfgOnState':hotlinksNewCfgOnState,'hotlinksCurCfgFdbUpdateState':hotlinksCurCfgFdbUpdateState,'hotlinksNewCfgFdbUpdateState':hotlinksNewCfgFdbUpdateState,'hotlinksMaxTriggerEntries':hotlinksMaxTriggerEntries,'hotlinksCurCfgTriggerTable':hotlinksCurCfgTriggerTable,'hotlinksCurCfgTriggerTableEntry':hotlinksCurCfgTriggerTableEntry,_x:hotlinksCurCfgTriggerId,'hotlinksCurCfgTriggerState':hotlinksCurCfgTriggerState,'hotlinksCurCfgTriggerPreemptState':hotlinksCurCfgTriggerPreemptState,'hotlinksCurCfgTriggerFdelay':hotlinksCurCfgTriggerFdelay,'hotlinksCurCfgTriggerMasterPort':hotlinksCurCfgTriggerMasterPort,'hotlinksCurCfgTriggerMasterTrunk':hotlinksCurCfgTriggerMasterTrunk,'hotlinksCurCfgTriggerBackupPort':hotlinksCurCfgTriggerBackupPort,'hotlinksCurCfgTriggerBackupTrunk':hotlinksCurCfgTriggerBackupTrunk,'hotlinksNewCfgTriggerTable':hotlinksNewCfgTriggerTable,'hotlinksNewCfgTriggerTableEntry':hotlinksNewCfgTriggerTableEntry,_y:hotlinksNewCfgTriggerId,'hotlinksNewCfgTriggerState':hotlinksNewCfgTriggerState,'hotlinksNewCfgTriggerPreemptState':hotlinksNewCfgTriggerPreemptState,'hotlinksNewCfgTriggerFdelay':hotlinksNewCfgTriggerFdelay,'hotlinksNewCfgTriggerMasterPort':hotlinksNewCfgTriggerMasterPort,'hotlinksNewCfgTriggerMasterTrunk':hotlinksNewCfgTriggerMasterTrunk,'hotlinksNewCfgTriggerBackupPort':hotlinksNewCfgTriggerBackupPort,'hotlinksNewCfgTriggerBackupTrunk':hotlinksNewCfgTriggerBackupTrunk,'layer2Stats':layer2Stats,'fdbStats':fdbStats,'fdbStatsCreates':fdbStatsCreates,'fdbStatsDeletes':fdbStatsDeletes,'fdbStatsCurrent':fdbStatsCurrent,'fdbStatsHiwat':fdbStatsHiwat,'fdbStatsLookups':fdbStatsLookups,'fdbStatsLookupFails':fdbStatsLookupFails,'fdbStatsFinds':fdbStatsFinds,'fdbStatsFindFails':fdbStatsFindFails,'fdbStatsFindOrCreates':fdbStatsFindOrCreates,'fdbStatsOverflows':fdbStatsOverflows,'stpStats':stpStats,'stgStatsPortTable':stgStatsPortTable,'stgStatsPortTableEntry':stgStatsPortTableEntry,_z:stgStatsStpIndex,_A0:stgStatsPortIndex,'stgStatsPortRcvCfgBpdus':stgStatsPortRcvCfgBpdus,'stgStatsPortRcvTcnBpdus':stgStatsPortRcvTcnBpdus,'stgStatsPortXmtCfgBpdus':stgStatsPortXmtCfgBpdus,'stgStatsPortXmtTcnBpdus':stgStatsPortXmtTcnBpdus,'lacpStats':lacpStats,'lacpStatsTable':lacpStatsTable,'lacpStatsTableEntry':lacpStatsTableEntry,_A1:lacpStatsIndex,'lacpdusRx':lacpdusRx,'markerpdusRx':markerpdusRx,'markerresponsepdusRx':markerresponsepdusRx,'unknownRx':unknownRx,'illegalRx':illegalRx,'lacpdusTx':lacpdusTx,'markerpdusTx':markerpdusTx,'markerresponsepdusTx':markerresponsepdusTx,'ufdStats':ufdStats,'ufdNoLtMLinkFailure':ufdNoLtMLinkFailure,'ufdNoLtMLinkBlockingState':ufdNoLtMLinkBlockingState,'ufdNoLtDAutoDisabled':ufdNoLtDAutoDisabled,'hotlinksStats':hotlinksStats,'hotlinksStatsTriggerTable':hotlinksStatsTriggerTable,'hotlinksStatsTriggerTableEntry':hotlinksStatsTriggerTableEntry,_A2:hotlinksStatsTriggerId,'hotlinksStatsTriggerMasterActive':hotlinksStatsTriggerMasterActive,'hotlinksStatsTriggerBackupActive':hotlinksStatsTriggerBackupActive,'hotlinksStatsTriggerFdbUpdate':hotlinksStatsTriggerFdbUpdate,'hotlinksStatsTriggerFdbFailed':hotlinksStatsTriggerFdbFailed,'layer2Info':layer2Info,'cistInfo':cistInfo,'cistGeneralInfo':cistGeneralInfo,'cistRoot':cistRoot,'cistRootPathCost':cistRootPathCost,'cistRootPort':cistRootPort,'cistRootHelloTime':cistRootHelloTime,'cistRootMaxAge':cistRootMaxAge,'cistRootForwardDelay':cistRootForwardDelay,'cistRegionalRoot':cistRegionalRoot,'cistRegionalPathCost':cistRegionalPathCost,'cistBridgePriority':cistBridgePriority,'cistBridgeMaxAge':cistBridgeMaxAge,'cistBridgeForwardDelay':cistBridgeForwardDelay,'cistMaxHopCount':cistMaxHopCount,'mstpDigest':mstpDigest,'cistInfoPortTable':cistInfoPortTable,'cistInfoPortTableEntry':cistInfoPortTableEntry,_A3:cistInfoPortIndex,'cistInfoPortPriority':cistInfoPortPriority,'cistInfoPortPathCost':cistInfoPortPathCost,'cistInfoPortState':cistInfoPortState,'cistInfoPortRole':cistInfoPortRole,'cistInfoPortDesignatedBridge':cistInfoPortDesignatedBridge,'cistInfoPortDesignatedPort':cistInfoPortDesignatedPort,'cistInfoPortLinkType':cistInfoPortLinkType,'cistInfoPortHelloTime':cistInfoPortHelloTime,'fdbInfo':fdbInfo,'fdbClear':fdbClear,'fdbTable':fdbTable,'fdbEntry':fdbEntry,_A5:fdbMacAddr,'fdbVlan':fdbVlan,'fdbSrcPort':fdbSrcPort,'fdbState':fdbState,'fdbRefSps':fdbRefSps,'fdbLearnedPort':fdbLearnedPort,'fdbSrcTrunk':fdbSrcTrunk,'stpInfo':stpInfo,'stpInfoTable':stpInfoTable,'stpInfoTableEntry':stpInfoTableEntry,_A6:stpInfoIndex,'stpInfoState':stpInfoState,'stgInfoVlanBmap':stgInfoVlanBmap,'stpInfoTimeSinceTopChange':stpInfoTimeSinceTopChange,'stpInfoTopChanges':stpInfoTopChanges,'stpInfoDesignatedRoot':stpInfoDesignatedRoot,'stpInfoRootCost':stpInfoRootCost,'stpInfoRootPort':stpInfoRootPort,'stpInfoMaxAge':stpInfoMaxAge,'stpInfoHelloTime':stpInfoHelloTime,'stpInfoForwardDelay':stpInfoForwardDelay,'stpInfoHoldTime':stpInfoHoldTime,'stpInfoBrgPriority':stpInfoBrgPriority,'stpInfoBrgHelloTime':stpInfoBrgHelloTime,'stpInfoBrgForwardDelay':stpInfoBrgForwardDelay,'stpInfoBrgMaxAge':stpInfoBrgMaxAge,'stpInfoAgingTime':stpInfoAgingTime,'stpInfoPortTable':stpInfoPortTable,'stpInfoPortTableEntry':stpInfoPortTableEntry,_A7:stpInfoPortStpIndex,_A8:stpInfoPortIndex,'stpInfoPortState':stpInfoPortState,'stpInfoPortDesignatedRoot':stpInfoPortDesignatedRoot,'stpInfoPortDesignatedCost':stpInfoPortDesignatedCost,'stpInfoPortDesignatedBridge':stpInfoPortDesignatedBridge,'stpInfoPortDesignatedPort':stpInfoPortDesignatedPort,'stpInfoPortForwardTransitions':stpInfoPortForwardTransitions,'stpInfoPortPathCost':stpInfoPortPathCost,'lacpInfo':lacpInfo,'lacpInfoPortTable':lacpInfoPortTable,'lacpInfoPortTableEntry':lacpInfoPortTableEntry,_A9:lacpInfoPortIndex,'lacpInfoPortSelected':lacpInfoPortSelected,'lacpInfoPortNtt':lacpInfoPortNtt,'lacpInfoPortReadyN':lacpInfoPortReadyN,'lacpInfoPortMoved':lacpInfoPortMoved,'dot1xInfo':dot1xInfo,'dot1xInfoPortTable':dot1xInfoPortTable,'dot1xInfoPortEntry':dot1xInfoPortEntry,_AA:dot1xInfoPortIndex,'dot1xInfoPortAuthMode':dot1xInfoPortAuthMode,'dot1xInfoPortAuthStatus':dot1xInfoPortAuthStatus,'dot1xInfoPortCtrlDir':dot1xInfoPortCtrlDir,'dot1xInfoPortAuthPAEState':dot1xInfoPortAuthPAEState,'dot1xInfoPortBackAuthState':dot1xInfoPortBackAuthState,'dot1xSystemInfo':dot1xSystemInfo,'dot1xSystemCapability':dot1xSystemCapability,'dot1xSystemStatus':dot1xSystemStatus,'dot1xSystemProtoVersion':dot1xSystemProtoVersion,'dot1pInfo':dot1pInfo,'dot1pInfoPriorityCOSTable':dot1pInfoPriorityCOSTable,'dot1pInfoPriorityCOSEntry':dot1pInfoPriorityCOSEntry,_AC:dot1pInfoPriorityIndex,'dot1pInfoPriorityCOSQueue':dot1pInfoPriorityCOSQueue,'dot1pInfoPriorityCOSWeight':dot1pInfoPriorityCOSWeight,'dot1pInfoPortTable':dot1pInfoPortTable,'dot1pInfoPortEntry':dot1pInfoPortEntry,_AD:dot1pInfoPortIndex,'dot1pInfoPortPriority':dot1pInfoPortPriority,'dot1pInfoPortCOSq':dot1pInfoPortCOSq,'dot1pInfoPortWeight':dot1pInfoPortWeight,'genInfo':genInfo,'generalInfoStpUplinkFast':generalInfoStpUplinkFast,'generalInfoUplinkFastRate':generalInfoUplinkFastRate,'vlanInfo':vlanInfo,'vlanInfoTable':vlanInfoTable,'vlanInfoTableEntry':vlanInfoTableEntry,_AE:vlanInfoId,'vlanInfoName':vlanInfoName,'vlanInfoStatus':vlanInfoStatus,'vlanInfoPorts':vlanInfoPorts,'trunkGroupInfo':trunkGroupInfo,'trunkGroupInfoTable':trunkGroupInfoTable,'trunkGroupInfoTableEntry':trunkGroupInfoTableEntry,_AF:trunkGroupInfoIndex,'trunkGroupInfoState':trunkGroupInfoState,'trunkGroupInfoPorts':trunkGroupInfoPorts,'hotlinksInfo':hotlinksInfo,'hotlinksInfoOnState':hotlinksInfoOnState,'hotlinksInfoFdbUpdateState':hotlinksInfoFdbUpdateState,'hotlinksInfoTriggerTable':hotlinksInfoTriggerTable,'hotlinksInfoTriggerTableEntry':hotlinksInfoTriggerTableEntry,_AG:hotlinksInfoTriggerId,'hotlinksInfoTriggerState':hotlinksInfoTriggerState,'hotlinksInfoTriggerPreemptState':hotlinksInfoTriggerPreemptState,'hotlinksInfoTriggerFdelay':hotlinksInfoTriggerFdelay,'hotlinksInfoTriggerActive':hotlinksInfoTriggerActive,'layer2Oper':layer2Oper})