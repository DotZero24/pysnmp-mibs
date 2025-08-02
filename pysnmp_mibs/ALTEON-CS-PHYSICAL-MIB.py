_A9='portTeamInfoIndex'
_A8='vlanInfoIdx'
_A7='vlanInfoId'
_A6='cistInfoPortIndex'
_A5='lacpInfoPortIndex'
_A4='designated'
_A3='alternate'
_A2='discarding'
_A1='forwarding'
_A0='stpInfoPortIndex'
_z='stpInfoPortStpIndex'
_y='stpInfoIndex'
_x='fdbMacAddr'
_w='stgStatsPortIndex'
_v='stgStatsStpIndex'
_u='vadcVlanNewCfgVlanId'
_t='vadcVlanCurCfgVlanId'
_s='portTeamNewCfgIndex'
_r='portTeamCurCfgIndex'
_q='mstCistNewCfgPortIndex'
_p='mstCistCurCfgPortIndex'
_o='lacpNewPortCfgTableId'
_n='lacpCurPortCfgTableId'
_m='pmNewCfgPmirrMirrPortIndex'
_l='pmNewCfgPmirrMoniPortIndex'
_k='pmCurCfgPmirrMirrPortIndex'
_j='pmCurCfgPmirrMoniPortIndex'
_i='stgNewCfgPortIndex'
_h='stgNewCfgStgIndex'
_g='stgCurCfgPortIndex'
_f='stgCurCfgStgIndex'
_e='stgNewCfgIndex'
_d='stgCurCfgIndex'
_c='trunkGroupNewCfgIndex'
_b='trunkGroupCurCfgIndex'
_a='vlanNewCfgVlanId'
_Z='vlanCurCfgVlanId'
_Y='false'
_X='true'
_W='passive'
_V='active'
_U='auto'
_T='disable'
_S='enable'
_R='delete'
_Q='unknown'
_P='other'
_O='OctetString'
_N='shared'
_M='p2p'
_L='on'
_K='off'
_J='Unsigned32'
_I='DisplayString'
_H='read-write'
_G='ALTEON-CS-PHYSICAL-MIB'
_F='enabled'
_E='disabled'
_D='read-create'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aws_switch,=mibBuilder.importSymbols('ALTEON-ROOT-MIB','aws-switch')
BridgeId,=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
layer2=ModuleIdentity((1,3,6,1,4,1,1872,2,5,2))
if mibBuilder.loadTexts:layer2.setRevisions(('2009-08-05 00:00',))
_Layer2Configs_ObjectIdentity=ObjectIdentity
layer2Configs=_Layer2Configs_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,1))
_Vlan_ObjectIdentity=ObjectIdentity
vlan=_Vlan_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,1,1))
_VlanMaxEnt_Type=Integer32
_VlanMaxEnt_Object=MibScalar
vlanMaxEnt=_VlanMaxEnt_Object((1,3,6,1,4,1,1872,2,5,2,1,1,1),_VlanMaxEnt_Type())
vlanMaxEnt.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanMaxEnt.setStatus(_A)
_VlanCurCfgTable_Object=MibTable
vlanCurCfgTable=_VlanCurCfgTable_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2))
if mibBuilder.loadTexts:vlanCurCfgTable.setStatus(_A)
_VlanCurCfgTableEntry_Object=MibTableRow
vlanCurCfgTableEntry=_VlanCurCfgTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1))
vlanCurCfgTableEntry.setIndexNames((0,_G,_Z))
if mibBuilder.loadTexts:vlanCurCfgTableEntry.setStatus(_A)
_VlanCurCfgVlanId_Type=Integer32
_VlanCurCfgVlanId_Object=MibTableColumn
vlanCurCfgVlanId=_VlanCurCfgVlanId_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,1),_VlanCurCfgVlanId_Type())
vlanCurCfgVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgVlanId.setStatus(_A)
class _VlanCurCfgVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VlanCurCfgVlanName_Type.__name__=_I
_VlanCurCfgVlanName_Object=MibTableColumn
vlanCurCfgVlanName=_VlanCurCfgVlanName_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,2),_VlanCurCfgVlanName_Type())
vlanCurCfgVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgVlanName.setStatus(_A)
_VlanCurCfgPorts_Type=OctetString
_VlanCurCfgPorts_Object=MibTableColumn
vlanCurCfgPorts=_VlanCurCfgPorts_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,3),_VlanCurCfgPorts_Type())
vlanCurCfgPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgPorts.setStatus(_A)
class _VlanCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanCurCfgState_Type.__name__=_C
_VlanCurCfgState_Object=MibTableColumn
vlanCurCfgState=_VlanCurCfgState_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,4),_VlanCurCfgState_Type())
vlanCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgState.setStatus(_A)
_VlanCurCfgBwmContract_Type=Integer32
_VlanCurCfgBwmContract_Object=MibTableColumn
vlanCurCfgBwmContract=_VlanCurCfgBwmContract_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,5),_VlanCurCfgBwmContract_Type())
vlanCurCfgBwmContract.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgBwmContract.setStatus(_A)
_VlanCurCfgStg_Type=Integer32
_VlanCurCfgStg_Object=MibTableColumn
vlanCurCfgStg=_VlanCurCfgStg_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,6),_VlanCurCfgStg_Type())
vlanCurCfgStg.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgStg.setStatus(_A)
class _VlanCurCfgJumbo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanCurCfgJumbo_Type.__name__=_C
_VlanCurCfgJumbo_Object=MibTableColumn
vlanCurCfgJumbo=_VlanCurCfgJumbo_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,7),_VlanCurCfgJumbo_Type())
vlanCurCfgJumbo.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgJumbo.setStatus(_A)
class _VlanCurCfgLearn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanCurCfgLearn_Type.__name__=_C
_VlanCurCfgLearn_Object=MibTableColumn
vlanCurCfgLearn=_VlanCurCfgLearn_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,8),_VlanCurCfgLearn_Type())
vlanCurCfgLearn.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgLearn.setStatus(_A)
class _VlanCurCfgShared_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanCurCfgShared_Type.__name__=_C
_VlanCurCfgShared_Object=MibTableColumn
vlanCurCfgShared=_VlanCurCfgShared_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,9),_VlanCurCfgShared_Type())
vlanCurCfgShared.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgShared.setStatus(_A)
class _VlanCurCfgIpv6LlaGen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanCurCfgIpv6LlaGen_Type.__name__=_C
_VlanCurCfgIpv6LlaGen_Object=MibTableColumn
vlanCurCfgIpv6LlaGen=_VlanCurCfgIpv6LlaGen_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,10),_VlanCurCfgIpv6LlaGen_Type())
vlanCurCfgIpv6LlaGen.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgIpv6LlaGen.setStatus(_A)
class _VlanCurCfgRouterAdv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanCurCfgRouterAdv_Type.__name__=_C
_VlanCurCfgRouterAdv_Object=MibTableColumn
vlanCurCfgRouterAdv=_VlanCurCfgRouterAdv_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,11),_VlanCurCfgRouterAdv_Type())
vlanCurCfgRouterAdv.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgRouterAdv.setStatus(_A)
class _VlanCurCfgReTransInt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_VlanCurCfgReTransInt_Type.__name__=_J
_VlanCurCfgReTransInt_Object=MibTableColumn
vlanCurCfgReTransInt=_VlanCurCfgReTransInt_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,12),_VlanCurCfgReTransInt_Type())
vlanCurCfgReTransInt.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgReTransInt.setStatus(_A)
class _VlanCurCfgMinIntBwAdv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1800))
_VlanCurCfgMinIntBwAdv_Type.__name__=_C
_VlanCurCfgMinIntBwAdv_Object=MibTableColumn
vlanCurCfgMinIntBwAdv=_VlanCurCfgMinIntBwAdv_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,13),_VlanCurCfgMinIntBwAdv_Type())
vlanCurCfgMinIntBwAdv.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgMinIntBwAdv.setStatus(_A)
class _VlanCurCfgMaxIntBwAdv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_VlanCurCfgMaxIntBwAdv_Type.__name__=_C
_VlanCurCfgMaxIntBwAdv_Object=MibTableColumn
vlanCurCfgMaxIntBwAdv=_VlanCurCfgMaxIntBwAdv_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,14),_VlanCurCfgMaxIntBwAdv_Type())
vlanCurCfgMaxIntBwAdv.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgMaxIntBwAdv.setStatus(_A)
class _VlanCurCfgMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1200,1500))
_VlanCurCfgMtu_Type.__name__=_C
_VlanCurCfgMtu_Object=MibTableColumn
vlanCurCfgMtu=_VlanCurCfgMtu_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,15),_VlanCurCfgMtu_Type())
vlanCurCfgMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgMtu.setStatus(_A)
class _VlanCurCfgCurHopLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VlanCurCfgCurHopLimit_Type.__name__=_C
_VlanCurCfgCurHopLimit_Object=MibTableColumn
vlanCurCfgCurHopLimit=_VlanCurCfgCurHopLimit_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,16),_VlanCurCfgCurHopLimit_Type())
vlanCurCfgCurHopLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgCurHopLimit.setStatus(_A)
class _VlanCurCfgMFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanCurCfgMFlag_Type.__name__=_C
_VlanCurCfgMFlag_Object=MibTableColumn
vlanCurCfgMFlag=_VlanCurCfgMFlag_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,17),_VlanCurCfgMFlag_Type())
vlanCurCfgMFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgMFlag.setStatus(_A)
class _VlanCurCfgOFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanCurCfgOFlag_Type.__name__=_C
_VlanCurCfgOFlag_Object=MibTableColumn
vlanCurCfgOFlag=_VlanCurCfgOFlag_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,18),_VlanCurCfgOFlag_Type())
vlanCurCfgOFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgOFlag.setStatus(_A)
class _VlanCurCfgRTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_VlanCurCfgRTime_Type.__name__=_C
_VlanCurCfgRTime_Object=MibTableColumn
vlanCurCfgRTime=_VlanCurCfgRTime_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,19),_VlanCurCfgRTime_Type())
vlanCurCfgRTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgRTime.setStatus(_A)
class _VlanCurCfgRlTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9000))
_VlanCurCfgRlTime_Type.__name__=_C
_VlanCurCfgRlTime_Object=MibTableColumn
vlanCurCfgRlTime=_VlanCurCfgRlTime_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,20),_VlanCurCfgRlTime_Type())
vlanCurCfgRlTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgRlTime.setStatus(_A)
class _VlanCurCfgPlTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_VlanCurCfgPlTime_Type.__name__=_J
_VlanCurCfgPlTime_Object=MibTableColumn
vlanCurCfgPlTime=_VlanCurCfgPlTime_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,21),_VlanCurCfgPlTime_Type())
vlanCurCfgPlTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgPlTime.setStatus(_A)
class _VlanCurCfgVlTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_VlanCurCfgVlTime_Type.__name__=_J
_VlanCurCfgVlTime_Object=MibTableColumn
vlanCurCfgVlTime=_VlanCurCfgVlTime_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,22),_VlanCurCfgVlTime_Type())
vlanCurCfgVlTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgVlTime.setStatus(_A)
class _VlanCurCfgOpInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanCurCfgOpInfo_Type.__name__=_C
_VlanCurCfgOpInfo_Object=MibTableColumn
vlanCurCfgOpInfo=_VlanCurCfgOpInfo_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,23),_VlanCurCfgOpInfo_Type())
vlanCurCfgOpInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgOpInfo.setStatus(_A)
class _VlanCurCfgApInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanCurCfgApInfo_Type.__name__=_C
_VlanCurCfgApInfo_Object=MibTableColumn
vlanCurCfgApInfo=_VlanCurCfgApInfo_Object((1,3,6,1,4,1,1872,2,5,2,1,1,2,1,24),_VlanCurCfgApInfo_Type())
vlanCurCfgApInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgApInfo.setStatus(_A)
_VlanNewCfgTable_Object=MibTable
vlanNewCfgTable=_VlanNewCfgTable_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3))
if mibBuilder.loadTexts:vlanNewCfgTable.setStatus(_A)
_VlanNewCfgTableEntry_Object=MibTableRow
vlanNewCfgTableEntry=_VlanNewCfgTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1))
vlanNewCfgTableEntry.setIndexNames((0,_G,_a))
if mibBuilder.loadTexts:vlanNewCfgTableEntry.setStatus(_A)
_VlanNewCfgVlanId_Type=Integer32
_VlanNewCfgVlanId_Object=MibTableColumn
vlanNewCfgVlanId=_VlanNewCfgVlanId_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,1),_VlanNewCfgVlanId_Type())
vlanNewCfgVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNewCfgVlanId.setStatus(_A)
class _VlanNewCfgVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VlanNewCfgVlanName_Type.__name__=_I
_VlanNewCfgVlanName_Object=MibTableColumn
vlanNewCfgVlanName=_VlanNewCfgVlanName_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,2),_VlanNewCfgVlanName_Type())
vlanNewCfgVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgVlanName.setStatus(_A)
_VlanNewCfgPorts_Type=OctetString
_VlanNewCfgPorts_Object=MibTableColumn
vlanNewCfgPorts=_VlanNewCfgPorts_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,3),_VlanNewCfgPorts_Type())
vlanNewCfgPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNewCfgPorts.setStatus(_A)
class _VlanNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanNewCfgState_Type.__name__=_C
_VlanNewCfgState_Object=MibTableColumn
vlanNewCfgState=_VlanNewCfgState_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,4),_VlanNewCfgState_Type())
vlanNewCfgState.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgState.setStatus(_A)
_VlanNewCfgAddPort_Type=Integer32
_VlanNewCfgAddPort_Object=MibTableColumn
vlanNewCfgAddPort=_VlanNewCfgAddPort_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,5),_VlanNewCfgAddPort_Type())
vlanNewCfgAddPort.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgAddPort.setStatus(_A)
_VlanNewCfgRemovePort_Type=Integer32
_VlanNewCfgRemovePort_Object=MibTableColumn
vlanNewCfgRemovePort=_VlanNewCfgRemovePort_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,6),_VlanNewCfgRemovePort_Type())
vlanNewCfgRemovePort.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgRemovePort.setStatus(_A)
class _VlanNewCfgDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_R,2)))
_VlanNewCfgDelete_Type.__name__=_C
_VlanNewCfgDelete_Object=MibTableColumn
vlanNewCfgDelete=_VlanNewCfgDelete_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,7),_VlanNewCfgDelete_Type())
vlanNewCfgDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgDelete.setStatus(_A)
_VlanNewCfgBwmContract_Type=Integer32
_VlanNewCfgBwmContract_Object=MibTableColumn
vlanNewCfgBwmContract=_VlanNewCfgBwmContract_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,8),_VlanNewCfgBwmContract_Type())
vlanNewCfgBwmContract.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgBwmContract.setStatus(_A)
_VlanNewCfgStg_Type=Integer32
_VlanNewCfgStg_Object=MibTableColumn
vlanNewCfgStg=_VlanNewCfgStg_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,9),_VlanNewCfgStg_Type())
vlanNewCfgStg.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgStg.setStatus(_A)
class _VlanNewCfgJumbo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanNewCfgJumbo_Type.__name__=_C
_VlanNewCfgJumbo_Object=MibTableColumn
vlanNewCfgJumbo=_VlanNewCfgJumbo_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,10),_VlanNewCfgJumbo_Type())
vlanNewCfgJumbo.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgJumbo.setStatus(_A)
class _VlanNewCfgLearn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanNewCfgLearn_Type.__name__=_C
_VlanNewCfgLearn_Object=MibTableColumn
vlanNewCfgLearn=_VlanNewCfgLearn_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,11),_VlanNewCfgLearn_Type())
vlanNewCfgLearn.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgLearn.setStatus(_A)
class _VlanNewCfgShared_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanNewCfgShared_Type.__name__=_C
_VlanNewCfgShared_Object=MibTableColumn
vlanNewCfgShared=_VlanNewCfgShared_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,12),_VlanNewCfgShared_Type())
vlanNewCfgShared.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgShared.setStatus(_A)
class _VlanNewCfgIpv6LlaGen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanNewCfgIpv6LlaGen_Type.__name__=_C
_VlanNewCfgIpv6LlaGen_Object=MibTableColumn
vlanNewCfgIpv6LlaGen=_VlanNewCfgIpv6LlaGen_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,13),_VlanNewCfgIpv6LlaGen_Type())
vlanNewCfgIpv6LlaGen.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgIpv6LlaGen.setStatus(_A)
class _VlanNewCfgRouterAdv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanNewCfgRouterAdv_Type.__name__=_C
_VlanNewCfgRouterAdv_Object=MibTableColumn
vlanNewCfgRouterAdv=_VlanNewCfgRouterAdv_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,14),_VlanNewCfgRouterAdv_Type())
vlanNewCfgRouterAdv.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgRouterAdv.setStatus(_A)
class _VlanNewCfgReTransInt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_VlanNewCfgReTransInt_Type.__name__=_J
_VlanNewCfgReTransInt_Object=MibTableColumn
vlanNewCfgReTransInt=_VlanNewCfgReTransInt_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,15),_VlanNewCfgReTransInt_Type())
vlanNewCfgReTransInt.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgReTransInt.setStatus(_A)
class _VlanNewCfgMinIntBwAdv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1800))
_VlanNewCfgMinIntBwAdv_Type.__name__=_C
_VlanNewCfgMinIntBwAdv_Object=MibTableColumn
vlanNewCfgMinIntBwAdv=_VlanNewCfgMinIntBwAdv_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,16),_VlanNewCfgMinIntBwAdv_Type())
vlanNewCfgMinIntBwAdv.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgMinIntBwAdv.setStatus(_A)
class _VlanNewCfgMaxIntBwAdv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_VlanNewCfgMaxIntBwAdv_Type.__name__=_C
_VlanNewCfgMaxIntBwAdv_Object=MibTableColumn
vlanNewCfgMaxIntBwAdv=_VlanNewCfgMaxIntBwAdv_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,17),_VlanNewCfgMaxIntBwAdv_Type())
vlanNewCfgMaxIntBwAdv.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgMaxIntBwAdv.setStatus(_A)
class _VlanNewCfgMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1200,1500))
_VlanNewCfgMtu_Type.__name__=_C
_VlanNewCfgMtu_Object=MibTableColumn
vlanNewCfgMtu=_VlanNewCfgMtu_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,18),_VlanNewCfgMtu_Type())
vlanNewCfgMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgMtu.setStatus(_A)
class _VlanNewCfgCurHopLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VlanNewCfgCurHopLimit_Type.__name__=_C
_VlanNewCfgCurHopLimit_Object=MibTableColumn
vlanNewCfgCurHopLimit=_VlanNewCfgCurHopLimit_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,19),_VlanNewCfgCurHopLimit_Type())
vlanNewCfgCurHopLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgCurHopLimit.setStatus(_A)
class _VlanNewCfgMFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanNewCfgMFlag_Type.__name__=_C
_VlanNewCfgMFlag_Object=MibTableColumn
vlanNewCfgMFlag=_VlanNewCfgMFlag_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,20),_VlanNewCfgMFlag_Type())
vlanNewCfgMFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgMFlag.setStatus(_A)
class _VlanNewCfgOFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanNewCfgOFlag_Type.__name__=_C
_VlanNewCfgOFlag_Object=MibTableColumn
vlanNewCfgOFlag=_VlanNewCfgOFlag_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,21),_VlanNewCfgOFlag_Type())
vlanNewCfgOFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgOFlag.setStatus(_A)
class _VlanNewCfgRTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_VlanNewCfgRTime_Type.__name__=_C
_VlanNewCfgRTime_Object=MibTableColumn
vlanNewCfgRTime=_VlanNewCfgRTime_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,22),_VlanNewCfgRTime_Type())
vlanNewCfgRTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgRTime.setStatus(_A)
class _VlanNewCfgRlTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9000))
_VlanNewCfgRlTime_Type.__name__=_C
_VlanNewCfgRlTime_Object=MibTableColumn
vlanNewCfgRlTime=_VlanNewCfgRlTime_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,23),_VlanNewCfgRlTime_Type())
vlanNewCfgRlTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgRlTime.setStatus(_A)
class _VlanNewCfgPlTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_VlanNewCfgPlTime_Type.__name__=_J
_VlanNewCfgPlTime_Object=MibTableColumn
vlanNewCfgPlTime=_VlanNewCfgPlTime_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,24),_VlanNewCfgPlTime_Type())
vlanNewCfgPlTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgPlTime.setStatus(_A)
class _VlanNewCfgVlTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_VlanNewCfgVlTime_Type.__name__=_J
_VlanNewCfgVlTime_Object=MibTableColumn
vlanNewCfgVlTime=_VlanNewCfgVlTime_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,25),_VlanNewCfgVlTime_Type())
vlanNewCfgVlTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgVlTime.setStatus(_A)
class _VlanNewCfgOpInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanNewCfgOpInfo_Type.__name__=_C
_VlanNewCfgOpInfo_Object=MibTableColumn
vlanNewCfgOpInfo=_VlanNewCfgOpInfo_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,26),_VlanNewCfgOpInfo_Type())
vlanNewCfgOpInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgOpInfo.setStatus(_A)
class _VlanNewCfgApInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanNewCfgApInfo_Type.__name__=_C
_VlanNewCfgApInfo_Object=MibTableColumn
vlanNewCfgApInfo=_VlanNewCfgApInfo_Object((1,3,6,1,4,1,1872,2,5,2,1,1,3,1,27),_VlanNewCfgApInfo_Type())
vlanNewCfgApInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgApInfo.setStatus(_A)
_VlanMaxVlanID_Type=Integer32
_VlanMaxVlanID_Object=MibScalar
vlanMaxVlanID=_VlanMaxVlanID_Object((1,3,6,1,4,1,1872,2,5,2,1,1,4),_VlanMaxVlanID_Type())
vlanMaxVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanMaxVlanID.setStatus(_A)
_Trunkgroup_ObjectIdentity=ObjectIdentity
trunkgroup=_Trunkgroup_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,1,2))
_TrunkGroupTableMaxSize_Type=Integer32
_TrunkGroupTableMaxSize_Object=MibScalar
trunkGroupTableMaxSize=_TrunkGroupTableMaxSize_Object((1,3,6,1,4,1,1872,2,5,2,1,2,1),_TrunkGroupTableMaxSize_Type())
trunkGroupTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupTableMaxSize.setStatus(_A)
_TrunkGroupCurCfgTable_Object=MibTable
trunkGroupCurCfgTable=_TrunkGroupCurCfgTable_Object((1,3,6,1,4,1,1872,2,5,2,1,2,2))
if mibBuilder.loadTexts:trunkGroupCurCfgTable.setStatus(_A)
_TrunkGroupCurCfgTableEntry_Object=MibTableRow
trunkGroupCurCfgTableEntry=_TrunkGroupCurCfgTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,2,2,1))
trunkGroupCurCfgTableEntry.setIndexNames((0,_G,_b))
if mibBuilder.loadTexts:trunkGroupCurCfgTableEntry.setStatus(_A)
_TrunkGroupCurCfgIndex_Type=Integer32
_TrunkGroupCurCfgIndex_Object=MibTableColumn
trunkGroupCurCfgIndex=_TrunkGroupCurCfgIndex_Object((1,3,6,1,4,1,1872,2,5,2,1,2,2,1,1),_TrunkGroupCurCfgIndex_Type())
trunkGroupCurCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupCurCfgIndex.setStatus(_A)
_TrunkGroupCurCfgPorts_Type=OctetString
_TrunkGroupCurCfgPorts_Object=MibTableColumn
trunkGroupCurCfgPorts=_TrunkGroupCurCfgPorts_Object((1,3,6,1,4,1,1872,2,5,2,1,2,2,1,2),_TrunkGroupCurCfgPorts_Type())
trunkGroupCurCfgPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupCurCfgPorts.setStatus(_A)
class _TrunkGroupCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_TrunkGroupCurCfgState_Type.__name__=_C
_TrunkGroupCurCfgState_Object=MibTableColumn
trunkGroupCurCfgState=_TrunkGroupCurCfgState_Object((1,3,6,1,4,1,1872,2,5,2,1,2,2,1,3),_TrunkGroupCurCfgState_Type())
trunkGroupCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupCurCfgState.setStatus(_A)
_TrunkGroupCurCfgBwmContract_Type=Integer32
_TrunkGroupCurCfgBwmContract_Object=MibTableColumn
trunkGroupCurCfgBwmContract=_TrunkGroupCurCfgBwmContract_Object((1,3,6,1,4,1,1872,2,5,2,1,2,2,1,4),_TrunkGroupCurCfgBwmContract_Type())
trunkGroupCurCfgBwmContract.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupCurCfgBwmContract.setStatus(_A)
class _TrunkGroupCurCfgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TrunkGroupCurCfgName_Type.__name__=_I
_TrunkGroupCurCfgName_Object=MibTableColumn
trunkGroupCurCfgName=_TrunkGroupCurCfgName_Object((1,3,6,1,4,1,1872,2,5,2,1,2,2,1,6),_TrunkGroupCurCfgName_Type())
trunkGroupCurCfgName.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupCurCfgName.setStatus(_A)
_TrunkGroupNewCfgTable_Object=MibTable
trunkGroupNewCfgTable=_TrunkGroupNewCfgTable_Object((1,3,6,1,4,1,1872,2,5,2,1,2,3))
if mibBuilder.loadTexts:trunkGroupNewCfgTable.setStatus(_A)
_TrunkGroupNewCfgTableEntry_Object=MibTableRow
trunkGroupNewCfgTableEntry=_TrunkGroupNewCfgTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,2,3,1))
trunkGroupNewCfgTableEntry.setIndexNames((0,_G,_c))
if mibBuilder.loadTexts:trunkGroupNewCfgTableEntry.setStatus(_A)
_TrunkGroupNewCfgIndex_Type=Integer32
_TrunkGroupNewCfgIndex_Object=MibTableColumn
trunkGroupNewCfgIndex=_TrunkGroupNewCfgIndex_Object((1,3,6,1,4,1,1872,2,5,2,1,2,3,1,1),_TrunkGroupNewCfgIndex_Type())
trunkGroupNewCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupNewCfgIndex.setStatus(_A)
_TrunkGroupNewCfgPorts_Type=OctetString
_TrunkGroupNewCfgPorts_Object=MibTableColumn
trunkGroupNewCfgPorts=_TrunkGroupNewCfgPorts_Object((1,3,6,1,4,1,1872,2,5,2,1,2,3,1,2),_TrunkGroupNewCfgPorts_Type())
trunkGroupNewCfgPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupNewCfgPorts.setStatus(_A)
_TrunkGroupNewCfgAddPort_Type=Integer32
_TrunkGroupNewCfgAddPort_Object=MibTableColumn
trunkGroupNewCfgAddPort=_TrunkGroupNewCfgAddPort_Object((1,3,6,1,4,1,1872,2,5,2,1,2,3,1,3),_TrunkGroupNewCfgAddPort_Type())
trunkGroupNewCfgAddPort.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkGroupNewCfgAddPort.setStatus(_A)
_TrunkGroupNewCfgRemovePort_Type=Integer32
_TrunkGroupNewCfgRemovePort_Object=MibTableColumn
trunkGroupNewCfgRemovePort=_TrunkGroupNewCfgRemovePort_Object((1,3,6,1,4,1,1872,2,5,2,1,2,3,1,4),_TrunkGroupNewCfgRemovePort_Type())
trunkGroupNewCfgRemovePort.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkGroupNewCfgRemovePort.setStatus(_A)
class _TrunkGroupNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_TrunkGroupNewCfgState_Type.__name__=_C
_TrunkGroupNewCfgState_Object=MibTableColumn
trunkGroupNewCfgState=_TrunkGroupNewCfgState_Object((1,3,6,1,4,1,1872,2,5,2,1,2,3,1,5),_TrunkGroupNewCfgState_Type())
trunkGroupNewCfgState.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkGroupNewCfgState.setStatus(_A)
class _TrunkGroupNewCfgDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_R,2)))
_TrunkGroupNewCfgDelete_Type.__name__=_C
_TrunkGroupNewCfgDelete_Object=MibTableColumn
trunkGroupNewCfgDelete=_TrunkGroupNewCfgDelete_Object((1,3,6,1,4,1,1872,2,5,2,1,2,3,1,6),_TrunkGroupNewCfgDelete_Type())
trunkGroupNewCfgDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkGroupNewCfgDelete.setStatus(_A)
_TrunkGroupNewCfgBwmContract_Type=Integer32
_TrunkGroupNewCfgBwmContract_Object=MibTableColumn
trunkGroupNewCfgBwmContract=_TrunkGroupNewCfgBwmContract_Object((1,3,6,1,4,1,1872,2,5,2,1,2,3,1,7),_TrunkGroupNewCfgBwmContract_Type())
trunkGroupNewCfgBwmContract.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkGroupNewCfgBwmContract.setStatus(_A)
class _TrunkGroupNewCfgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TrunkGroupNewCfgName_Type.__name__=_I
_TrunkGroupNewCfgName_Object=MibTableColumn
trunkGroupNewCfgName=_TrunkGroupNewCfgName_Object((1,3,6,1,4,1,1872,2,5,2,1,2,3,1,9),_TrunkGroupNewCfgName_Type())
trunkGroupNewCfgName.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkGroupNewCfgName.setStatus(_A)
_StgCfg_ObjectIdentity=ObjectIdentity
stgCfg=_StgCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,1,3))
_StgCurCfgTable_Object=MibTable
stgCurCfgTable=_StgCurCfgTable_Object((1,3,6,1,4,1,1872,2,5,2,1,3,1))
if mibBuilder.loadTexts:stgCurCfgTable.setStatus(_A)
_StgCurCfgTableEntry_Object=MibTableRow
stgCurCfgTableEntry=_StgCurCfgTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,3,1,1))
stgCurCfgTableEntry.setIndexNames((0,_G,_d))
if mibBuilder.loadTexts:stgCurCfgTableEntry.setStatus(_A)
_StgCurCfgIndex_Type=Integer32
_StgCurCfgIndex_Object=MibTableColumn
stgCurCfgIndex=_StgCurCfgIndex_Object((1,3,6,1,4,1,1872,2,5,2,1,3,1,1,1),_StgCurCfgIndex_Type())
stgCurCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgIndex.setStatus(_A)
class _StgCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_K,2)))
_StgCurCfgState_Type.__name__=_C
_StgCurCfgState_Object=MibTableColumn
stgCurCfgState=_StgCurCfgState_Object((1,3,6,1,4,1,1872,2,5,2,1,3,1,1,2),_StgCurCfgState_Type())
stgCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgState.setStatus(_A)
class _StgCurCfgPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StgCurCfgPriority_Type.__name__=_C
_StgCurCfgPriority_Object=MibTableColumn
stgCurCfgPriority=_StgCurCfgPriority_Object((1,3,6,1,4,1,1872,2,5,2,1,3,1,1,5),_StgCurCfgPriority_Type())
stgCurCfgPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPriority.setStatus(_A)
class _StgCurCfgBrgHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_StgCurCfgBrgHelloTime_Type.__name__=_C
_StgCurCfgBrgHelloTime_Object=MibTableColumn
stgCurCfgBrgHelloTime=_StgCurCfgBrgHelloTime_Object((1,3,6,1,4,1,1872,2,5,2,1,3,1,1,6),_StgCurCfgBrgHelloTime_Type())
stgCurCfgBrgHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgBrgHelloTime.setStatus(_A)
class _StgCurCfgBrgForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_StgCurCfgBrgForwardDelay_Type.__name__=_C
_StgCurCfgBrgForwardDelay_Object=MibTableColumn
stgCurCfgBrgForwardDelay=_StgCurCfgBrgForwardDelay_Object((1,3,6,1,4,1,1872,2,5,2,1,3,1,1,7),_StgCurCfgBrgForwardDelay_Type())
stgCurCfgBrgForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgBrgForwardDelay.setStatus(_A)
class _StgCurCfgBrgMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_StgCurCfgBrgMaxAge_Type.__name__=_C
_StgCurCfgBrgMaxAge_Object=MibTableColumn
stgCurCfgBrgMaxAge=_StgCurCfgBrgMaxAge_Object((1,3,6,1,4,1,1872,2,5,2,1,3,1,1,8),_StgCurCfgBrgMaxAge_Type())
stgCurCfgBrgMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgBrgMaxAge.setStatus(_A)
class _StgCurCfgAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StgCurCfgAgingTime_Type.__name__=_C
_StgCurCfgAgingTime_Object=MibTableColumn
stgCurCfgAgingTime=_StgCurCfgAgingTime_Object((1,3,6,1,4,1,1872,2,5,2,1,3,1,1,9),_StgCurCfgAgingTime_Type())
stgCurCfgAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgAgingTime.setStatus(_A)
class _StgCurCfgVlanBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_StgCurCfgVlanBmap_Type.__name__=_O
_StgCurCfgVlanBmap_Object=MibTableColumn
stgCurCfgVlanBmap=_StgCurCfgVlanBmap_Object((1,3,6,1,4,1,1872,2,5,2,1,3,1,1,10),_StgCurCfgVlanBmap_Type())
stgCurCfgVlanBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgVlanBmap.setStatus(_A)
_StgNewCfgTable_Object=MibTable
stgNewCfgTable=_StgNewCfgTable_Object((1,3,6,1,4,1,1872,2,5,2,1,3,2))
if mibBuilder.loadTexts:stgNewCfgTable.setStatus(_A)
_StgNewCfgTableEntry_Object=MibTableRow
stgNewCfgTableEntry=_StgNewCfgTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,3,2,1))
stgNewCfgTableEntry.setIndexNames((0,_G,_e))
if mibBuilder.loadTexts:stgNewCfgTableEntry.setStatus(_A)
_StgNewCfgIndex_Type=Integer32
_StgNewCfgIndex_Object=MibTableColumn
stgNewCfgIndex=_StgNewCfgIndex_Object((1,3,6,1,4,1,1872,2,5,2,1,3,2,1,1),_StgNewCfgIndex_Type())
stgNewCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgNewCfgIndex.setStatus(_A)
class _StgNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_K,2)))
_StgNewCfgState_Type.__name__=_C
_StgNewCfgState_Object=MibTableColumn
stgNewCfgState=_StgNewCfgState_Object((1,3,6,1,4,1,1872,2,5,2,1,3,2,1,2),_StgNewCfgState_Type())
stgNewCfgState.setMaxAccess(_H)
if mibBuilder.loadTexts:stgNewCfgState.setStatus(_A)
class _StgNewCfgDefaultCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('default-config',1))
_StgNewCfgDefaultCfg_Type.__name__=_C
_StgNewCfgDefaultCfg_Object=MibTableColumn
stgNewCfgDefaultCfg=_StgNewCfgDefaultCfg_Object((1,3,6,1,4,1,1872,2,5,2,1,3,2,1,3),_StgNewCfgDefaultCfg_Type())
stgNewCfgDefaultCfg.setMaxAccess(_H)
if mibBuilder.loadTexts:stgNewCfgDefaultCfg.setStatus(_A)
_StgNewCfgAddVlan_Type=Integer32
_StgNewCfgAddVlan_Object=MibTableColumn
stgNewCfgAddVlan=_StgNewCfgAddVlan_Object((1,3,6,1,4,1,1872,2,5,2,1,3,2,1,4),_StgNewCfgAddVlan_Type())
stgNewCfgAddVlan.setMaxAccess(_H)
if mibBuilder.loadTexts:stgNewCfgAddVlan.setStatus(_A)
_StgNewCfgRemoveVlan_Type=Integer32
_StgNewCfgRemoveVlan_Object=MibTableColumn
stgNewCfgRemoveVlan=_StgNewCfgRemoveVlan_Object((1,3,6,1,4,1,1872,2,5,2,1,3,2,1,5),_StgNewCfgRemoveVlan_Type())
stgNewCfgRemoveVlan.setMaxAccess(_H)
if mibBuilder.loadTexts:stgNewCfgRemoveVlan.setStatus(_A)
class _StgNewCfgPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StgNewCfgPriority_Type.__name__=_C
_StgNewCfgPriority_Object=MibTableColumn
stgNewCfgPriority=_StgNewCfgPriority_Object((1,3,6,1,4,1,1872,2,5,2,1,3,2,1,8),_StgNewCfgPriority_Type())
stgNewCfgPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:stgNewCfgPriority.setStatus(_A)
class _StgNewCfgBrgHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_StgNewCfgBrgHelloTime_Type.__name__=_C
_StgNewCfgBrgHelloTime_Object=MibTableColumn
stgNewCfgBrgHelloTime=_StgNewCfgBrgHelloTime_Object((1,3,6,1,4,1,1872,2,5,2,1,3,2,1,9),_StgNewCfgBrgHelloTime_Type())
stgNewCfgBrgHelloTime.setMaxAccess(_H)
if mibBuilder.loadTexts:stgNewCfgBrgHelloTime.setStatus(_A)
class _StgNewCfgBrgForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_StgNewCfgBrgForwardDelay_Type.__name__=_C
_StgNewCfgBrgForwardDelay_Object=MibTableColumn
stgNewCfgBrgForwardDelay=_StgNewCfgBrgForwardDelay_Object((1,3,6,1,4,1,1872,2,5,2,1,3,2,1,10),_StgNewCfgBrgForwardDelay_Type())
stgNewCfgBrgForwardDelay.setMaxAccess(_H)
if mibBuilder.loadTexts:stgNewCfgBrgForwardDelay.setStatus(_A)
class _StgNewCfgBrgMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_StgNewCfgBrgMaxAge_Type.__name__=_C
_StgNewCfgBrgMaxAge_Object=MibTableColumn
stgNewCfgBrgMaxAge=_StgNewCfgBrgMaxAge_Object((1,3,6,1,4,1,1872,2,5,2,1,3,2,1,11),_StgNewCfgBrgMaxAge_Type())
stgNewCfgBrgMaxAge.setMaxAccess(_H)
if mibBuilder.loadTexts:stgNewCfgBrgMaxAge.setStatus(_A)
class _StgNewCfgAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StgNewCfgAgingTime_Type.__name__=_C
_StgNewCfgAgingTime_Object=MibTableColumn
stgNewCfgAgingTime=_StgNewCfgAgingTime_Object((1,3,6,1,4,1,1872,2,5,2,1,3,2,1,12),_StgNewCfgAgingTime_Type())
stgNewCfgAgingTime.setMaxAccess(_H)
if mibBuilder.loadTexts:stgNewCfgAgingTime.setStatus(_A)
class _StgNewCfgVlanBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_StgNewCfgVlanBmap_Type.__name__=_O
_StgNewCfgVlanBmap_Object=MibTableColumn
stgNewCfgVlanBmap=_StgNewCfgVlanBmap_Object((1,3,6,1,4,1,1872,2,5,2,1,3,2,1,13),_StgNewCfgVlanBmap_Type())
stgNewCfgVlanBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:stgNewCfgVlanBmap.setStatus(_A)
_StgCurCfgPortTable_Object=MibTable
stgCurCfgPortTable=_StgCurCfgPortTable_Object((1,3,6,1,4,1,1872,2,5,2,1,3,3))
if mibBuilder.loadTexts:stgCurCfgPortTable.setStatus(_A)
_StgCurCfgPortTableEntry_Object=MibTableRow
stgCurCfgPortTableEntry=_StgCurCfgPortTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,3,3,1))
stgCurCfgPortTableEntry.setIndexNames((0,_G,_f),(0,_G,_g))
if mibBuilder.loadTexts:stgCurCfgPortTableEntry.setStatus(_A)
_StgCurCfgStgIndex_Type=Integer32
_StgCurCfgStgIndex_Object=MibTableColumn
stgCurCfgStgIndex=_StgCurCfgStgIndex_Object((1,3,6,1,4,1,1872,2,5,2,1,3,3,1,1),_StgCurCfgStgIndex_Type())
stgCurCfgStgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgStgIndex.setStatus(_A)
_StgCurCfgPortIndex_Type=Integer32
_StgCurCfgPortIndex_Object=MibTableColumn
stgCurCfgPortIndex=_StgCurCfgPortIndex_Object((1,3,6,1,4,1,1872,2,5,2,1,3,3,1,2),_StgCurCfgPortIndex_Type())
stgCurCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPortIndex.setStatus(_A)
class _StgCurCfgPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_K,2)))
_StgCurCfgPortState_Type.__name__=_C
_StgCurCfgPortState_Object=MibTableColumn
stgCurCfgPortState=_StgCurCfgPortState_Object((1,3,6,1,4,1,1872,2,5,2,1,3,3,1,3),_StgCurCfgPortState_Type())
stgCurCfgPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPortState.setStatus(_A)
class _StgCurCfgPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_StgCurCfgPortPriority_Type.__name__=_C
_StgCurCfgPortPriority_Object=MibTableColumn
stgCurCfgPortPriority=_StgCurCfgPortPriority_Object((1,3,6,1,4,1,1872,2,5,2,1,3,3,1,4),_StgCurCfgPortPriority_Type())
stgCurCfgPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPortPriority.setStatus(_A)
_StgCurCfgPortPathCost_Type=Integer32
_StgCurCfgPortPathCost_Object=MibTableColumn
stgCurCfgPortPathCost=_StgCurCfgPortPathCost_Object((1,3,6,1,4,1,1872,2,5,2,1,3,3,1,5),_StgCurCfgPortPathCost_Type())
stgCurCfgPortPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPortPathCost.setStatus(_A)
class _StgCurCfgPortLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_M,2),(_N,3)))
_StgCurCfgPortLink_Type.__name__=_C
_StgCurCfgPortLink_Object=MibTableColumn
stgCurCfgPortLink=_StgCurCfgPortLink_Object((1,3,6,1,4,1,1872,2,5,2,1,3,3,1,6),_StgCurCfgPortLink_Type())
stgCurCfgPortLink.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPortLink.setStatus(_A)
class _StgCurCfgPortEdge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_StgCurCfgPortEdge_Type.__name__=_C
_StgCurCfgPortEdge_Object=MibTableColumn
stgCurCfgPortEdge=_StgCurCfgPortEdge_Object((1,3,6,1,4,1,1872,2,5,2,1,3,3,1,7),_StgCurCfgPortEdge_Type())
stgCurCfgPortEdge.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPortEdge.setStatus(_A)
_StgNewCfgPortTable_Object=MibTable
stgNewCfgPortTable=_StgNewCfgPortTable_Object((1,3,6,1,4,1,1872,2,5,2,1,3,4))
if mibBuilder.loadTexts:stgNewCfgPortTable.setStatus(_A)
_StgNewCfgPortTableEntry_Object=MibTableRow
stgNewCfgPortTableEntry=_StgNewCfgPortTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,3,4,1))
stgNewCfgPortTableEntry.setIndexNames((0,_G,_h),(0,_G,_i))
if mibBuilder.loadTexts:stgNewCfgPortTableEntry.setStatus(_A)
_StgNewCfgStgIndex_Type=Integer32
_StgNewCfgStgIndex_Object=MibTableColumn
stgNewCfgStgIndex=_StgNewCfgStgIndex_Object((1,3,6,1,4,1,1872,2,5,2,1,3,4,1,1),_StgNewCfgStgIndex_Type())
stgNewCfgStgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgNewCfgStgIndex.setStatus(_A)
_StgNewCfgPortIndex_Type=Integer32
_StgNewCfgPortIndex_Object=MibTableColumn
stgNewCfgPortIndex=_StgNewCfgPortIndex_Object((1,3,6,1,4,1,1872,2,5,2,1,3,4,1,2),_StgNewCfgPortIndex_Type())
stgNewCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgNewCfgPortIndex.setStatus(_A)
class _StgNewCfgPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_K,2)))
_StgNewCfgPortState_Type.__name__=_C
_StgNewCfgPortState_Object=MibTableColumn
stgNewCfgPortState=_StgNewCfgPortState_Object((1,3,6,1,4,1,1872,2,5,2,1,3,4,1,3),_StgNewCfgPortState_Type())
stgNewCfgPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgPortState.setStatus(_A)
class _StgNewCfgPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_StgNewCfgPortPriority_Type.__name__=_C
_StgNewCfgPortPriority_Object=MibTableColumn
stgNewCfgPortPriority=_StgNewCfgPortPriority_Object((1,3,6,1,4,1,1872,2,5,2,1,3,4,1,4),_StgNewCfgPortPriority_Type())
stgNewCfgPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgPortPriority.setStatus(_A)
_StgNewCfgPortPathCost_Type=Integer32
_StgNewCfgPortPathCost_Object=MibTableColumn
stgNewCfgPortPathCost=_StgNewCfgPortPathCost_Object((1,3,6,1,4,1,1872,2,5,2,1,3,4,1,5),_StgNewCfgPortPathCost_Type())
stgNewCfgPortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgPortPathCost.setStatus(_A)
class _StgNewCfgPortLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_M,2),(_N,3)))
_StgNewCfgPortLink_Type.__name__=_C
_StgNewCfgPortLink_Object=MibTableColumn
stgNewCfgPortLink=_StgNewCfgPortLink_Object((1,3,6,1,4,1,1872,2,5,2,1,3,4,1,6),_StgNewCfgPortLink_Type())
stgNewCfgPortLink.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgPortLink.setStatus(_A)
class _StgNewCfgPortEdge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_StgNewCfgPortEdge_Type.__name__=_C
_StgNewCfgPortEdge_Object=MibTableColumn
stgNewCfgPortEdge=_StgNewCfgPortEdge_Object((1,3,6,1,4,1,1872,2,5,2,1,3,4,1,7),_StgNewCfgPortEdge_Type())
stgNewCfgPortEdge.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgPortEdge.setStatus(_A)
_Mirroring_ObjectIdentity=ObjectIdentity
mirroring=_Mirroring_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,1,4))
_MirrPortMirr_ObjectIdentity=ObjectIdentity
mirrPortMirr=_MirrPortMirr_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,1,4,1))
class _PmCurCfgPortMirrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_PmCurCfgPortMirrState_Type.__name__=_C
_PmCurCfgPortMirrState_Object=MibScalar
pmCurCfgPortMirrState=_PmCurCfgPortMirrState_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,1),_PmCurCfgPortMirrState_Type())
pmCurCfgPortMirrState.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgPortMirrState.setStatus(_A)
class _PmNewCfgPortMirrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_PmNewCfgPortMirrState_Type.__name__=_C
_PmNewCfgPortMirrState_Object=MibScalar
pmNewCfgPortMirrState=_PmNewCfgPortMirrState_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,2),_PmNewCfgPortMirrState_Type())
pmNewCfgPortMirrState.setMaxAccess(_H)
if mibBuilder.loadTexts:pmNewCfgPortMirrState.setStatus(_A)
_PmCurCfgPortMonitorTable_Object=MibTable
pmCurCfgPortMonitorTable=_PmCurCfgPortMonitorTable_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,3))
if mibBuilder.loadTexts:pmCurCfgPortMonitorTable.setStatus(_A)
_PmCurCfgPortMonitorEntry_Object=MibTableRow
pmCurCfgPortMonitorEntry=_PmCurCfgPortMonitorEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,3,1))
pmCurCfgPortMonitorEntry.setIndexNames((0,_G,_j),(0,_G,_k))
if mibBuilder.loadTexts:pmCurCfgPortMonitorEntry.setStatus(_A)
_PmCurCfgPmirrMoniPortIndex_Type=Integer32
_PmCurCfgPmirrMoniPortIndex_Object=MibTableColumn
pmCurCfgPmirrMoniPortIndex=_PmCurCfgPmirrMoniPortIndex_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,3,1,1),_PmCurCfgPmirrMoniPortIndex_Type())
pmCurCfgPmirrMoniPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgPmirrMoniPortIndex.setStatus(_A)
_PmCurCfgPmirrMirrPortIndex_Type=Integer32
_PmCurCfgPmirrMirrPortIndex_Object=MibTableColumn
pmCurCfgPmirrMirrPortIndex=_PmCurCfgPmirrMirrPortIndex_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,3,1,2),_PmCurCfgPmirrMirrPortIndex_Type())
pmCurCfgPmirrMirrPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgPmirrMirrPortIndex.setStatus(_A)
class _PmCurCfgPmirrDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('in',1),('out',2),('both',3)))
_PmCurCfgPmirrDirection_Type.__name__=_C
_PmCurCfgPmirrDirection_Object=MibTableColumn
pmCurCfgPmirrDirection=_PmCurCfgPmirrDirection_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,3,1,3),_PmCurCfgPmirrDirection_Type())
pmCurCfgPmirrDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgPmirrDirection.setStatus(_A)
_PmCurCfgPmirrPortVlansBmap_Type=OctetString
_PmCurCfgPmirrPortVlansBmap_Object=MibTableColumn
pmCurCfgPmirrPortVlansBmap=_PmCurCfgPmirrPortVlansBmap_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,3,1,6),_PmCurCfgPmirrPortVlansBmap_Type())
pmCurCfgPmirrPortVlansBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgPmirrPortVlansBmap.setStatus(_A)
_PmNewCfgPortMonitorTable_Object=MibTable
pmNewCfgPortMonitorTable=_PmNewCfgPortMonitorTable_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,4))
if mibBuilder.loadTexts:pmNewCfgPortMonitorTable.setStatus(_A)
_PmNewCfgPortMonitorEntry_Object=MibTableRow
pmNewCfgPortMonitorEntry=_PmNewCfgPortMonitorEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,4,1))
pmNewCfgPortMonitorEntry.setIndexNames((0,_G,_l),(0,_G,_m))
if mibBuilder.loadTexts:pmNewCfgPortMonitorEntry.setStatus(_A)
_PmNewCfgPmirrMoniPortIndex_Type=Integer32
_PmNewCfgPmirrMoniPortIndex_Object=MibTableColumn
pmNewCfgPmirrMoniPortIndex=_PmNewCfgPmirrMoniPortIndex_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,4,1,1),_PmNewCfgPmirrMoniPortIndex_Type())
pmNewCfgPmirrMoniPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmNewCfgPmirrMoniPortIndex.setStatus(_A)
_PmNewCfgPmirrMirrPortIndex_Type=Integer32
_PmNewCfgPmirrMirrPortIndex_Object=MibTableColumn
pmNewCfgPmirrMirrPortIndex=_PmNewCfgPmirrMirrPortIndex_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,4,1,2),_PmNewCfgPmirrMirrPortIndex_Type())
pmNewCfgPmirrMirrPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmNewCfgPmirrMirrPortIndex.setStatus(_A)
class _PmNewCfgPmirrDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('in',1),('out',2),('both',3)))
_PmNewCfgPmirrDirection_Type.__name__=_C
_PmNewCfgPmirrDirection_Object=MibTableColumn
pmNewCfgPmirrDirection=_PmNewCfgPmirrDirection_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,4,1,3),_PmNewCfgPmirrDirection_Type())
pmNewCfgPmirrDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgPmirrDirection.setStatus(_A)
class _PmNewCfgPmirrDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_R,2)))
_PmNewCfgPmirrDelete_Type.__name__=_C
_PmNewCfgPmirrDelete_Object=MibTableColumn
pmNewCfgPmirrDelete=_PmNewCfgPmirrDelete_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,4,1,4),_PmNewCfgPmirrDelete_Type())
pmNewCfgPmirrDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgPmirrDelete.setStatus(_A)
_PmNewCfgAddVlan_Type=Integer32
_PmNewCfgAddVlan_Object=MibTableColumn
pmNewCfgAddVlan=_PmNewCfgAddVlan_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,4,1,7),_PmNewCfgAddVlan_Type())
pmNewCfgAddVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgAddVlan.setStatus(_A)
_PmNewCfgRemoveVlan_Type=Integer32
_PmNewCfgRemoveVlan_Object=MibTableColumn
pmNewCfgRemoveVlan=_PmNewCfgRemoveVlan_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,4,1,8),_PmNewCfgRemoveVlan_Type())
pmNewCfgRemoveVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgRemoveVlan.setStatus(_A)
_PmNewCfgPmirrPortVlansBmap_Type=OctetString
_PmNewCfgPmirrPortVlansBmap_Object=MibTableColumn
pmNewCfgPmirrPortVlansBmap=_PmNewCfgPmirrPortVlansBmap_Object((1,3,6,1,4,1,1872,2,5,2,1,4,1,4,1,9),_PmNewCfgPmirrPortVlansBmap_Type())
pmNewCfgPmirrPortVlansBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:pmNewCfgPmirrPortVlansBmap.setStatus(_A)
_Lacp_ObjectIdentity=ObjectIdentity
lacp=_Lacp_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,1,5))
class _LacpCurSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LacpCurSystemPriority_Type.__name__=_C
_LacpCurSystemPriority_Object=MibScalar
lacpCurSystemPriority=_LacpCurSystemPriority_Object((1,3,6,1,4,1,1872,2,5,2,1,5,1),_LacpCurSystemPriority_Type())
lacpCurSystemPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpCurSystemPriority.setStatus(_A)
class _LacpNewSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LacpNewSystemPriority_Type.__name__=_C
_LacpNewSystemPriority_Object=MibScalar
lacpNewSystemPriority=_LacpNewSystemPriority_Object((1,3,6,1,4,1,1872,2,5,2,1,5,2),_LacpNewSystemPriority_Type())
lacpNewSystemPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:lacpNewSystemPriority.setStatus(_A)
class _LacpCurSystemTimeoutTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,90)));namedValues=NamedValues(*(('short',3),('long',90)))
_LacpCurSystemTimeoutTime_Type.__name__=_C
_LacpCurSystemTimeoutTime_Object=MibScalar
lacpCurSystemTimeoutTime=_LacpCurSystemTimeoutTime_Object((1,3,6,1,4,1,1872,2,5,2,1,5,5),_LacpCurSystemTimeoutTime_Type())
lacpCurSystemTimeoutTime.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpCurSystemTimeoutTime.setStatus(_A)
class _LacpNewSystemTimeoutTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,90)));namedValues=NamedValues(*(('short',3),('long',90)))
_LacpNewSystemTimeoutTime_Type.__name__=_C
_LacpNewSystemTimeoutTime_Object=MibScalar
lacpNewSystemTimeoutTime=_LacpNewSystemTimeoutTime_Object((1,3,6,1,4,1,1872,2,5,2,1,5,6),_LacpNewSystemTimeoutTime_Type())
lacpNewSystemTimeoutTime.setMaxAccess(_H)
if mibBuilder.loadTexts:lacpNewSystemTimeoutTime.setStatus(_A)
_LacpCurPortCfgTable_Object=MibTable
lacpCurPortCfgTable=_LacpCurPortCfgTable_Object((1,3,6,1,4,1,1872,2,5,2,1,5,7))
if mibBuilder.loadTexts:lacpCurPortCfgTable.setStatus(_A)
_LacpCurPortCfgTableEntry_Object=MibTableRow
lacpCurPortCfgTableEntry=_LacpCurPortCfgTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,5,7,1))
lacpCurPortCfgTableEntry.setIndexNames((0,_G,_n))
if mibBuilder.loadTexts:lacpCurPortCfgTableEntry.setStatus(_A)
_LacpCurPortCfgTableId_Type=Integer32
_LacpCurPortCfgTableId_Object=MibTableColumn
lacpCurPortCfgTableId=_LacpCurPortCfgTableId_Object((1,3,6,1,4,1,1872,2,5,2,1,5,7,1,1),_LacpCurPortCfgTableId_Type())
lacpCurPortCfgTableId.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpCurPortCfgTableId.setStatus(_A)
class _LacpCurPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_V,2),(_W,3)))
_LacpCurPortState_Type.__name__=_C
_LacpCurPortState_Object=MibTableColumn
lacpCurPortState=_LacpCurPortState_Object((1,3,6,1,4,1,1872,2,5,2,1,5,7,1,2),_LacpCurPortState_Type())
lacpCurPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpCurPortState.setStatus(_A)
class _LacpCurPortActorPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LacpCurPortActorPortPriority_Type.__name__=_C
_LacpCurPortActorPortPriority_Object=MibTableColumn
lacpCurPortActorPortPriority=_LacpCurPortActorPortPriority_Object((1,3,6,1,4,1,1872,2,5,2,1,5,7,1,3),_LacpCurPortActorPortPriority_Type())
lacpCurPortActorPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpCurPortActorPortPriority.setStatus(_A)
class _LacpCurPortActorAdminKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LacpCurPortActorAdminKey_Type.__name__=_C
_LacpCurPortActorAdminKey_Object=MibTableColumn
lacpCurPortActorAdminKey=_LacpCurPortActorAdminKey_Object((1,3,6,1,4,1,1872,2,5,2,1,5,7,1,4),_LacpCurPortActorAdminKey_Type())
lacpCurPortActorAdminKey.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpCurPortActorAdminKey.setStatus(_A)
_LacpNewPortCfgTable_Object=MibTable
lacpNewPortCfgTable=_LacpNewPortCfgTable_Object((1,3,6,1,4,1,1872,2,5,2,1,5,8))
if mibBuilder.loadTexts:lacpNewPortCfgTable.setStatus(_A)
_LacpNewPortCfgTableEntry_Object=MibTableRow
lacpNewPortCfgTableEntry=_LacpNewPortCfgTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,5,8,1))
lacpNewPortCfgTableEntry.setIndexNames((0,_G,_o))
if mibBuilder.loadTexts:lacpNewPortCfgTableEntry.setStatus(_A)
_LacpNewPortCfgTableId_Type=Integer32
_LacpNewPortCfgTableId_Object=MibTableColumn
lacpNewPortCfgTableId=_LacpNewPortCfgTableId_Object((1,3,6,1,4,1,1872,2,5,2,1,5,8,1,1),_LacpNewPortCfgTableId_Type())
lacpNewPortCfgTableId.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpNewPortCfgTableId.setStatus(_A)
class _LacpNewPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_V,2),(_W,3)))
_LacpNewPortState_Type.__name__=_C
_LacpNewPortState_Object=MibTableColumn
lacpNewPortState=_LacpNewPortState_Object((1,3,6,1,4,1,1872,2,5,2,1,5,8,1,2),_LacpNewPortState_Type())
lacpNewPortState.setMaxAccess(_H)
if mibBuilder.loadTexts:lacpNewPortState.setStatus(_A)
class _LacpNewPortActorPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LacpNewPortActorPortPriority_Type.__name__=_C
_LacpNewPortActorPortPriority_Object=MibTableColumn
lacpNewPortActorPortPriority=_LacpNewPortActorPortPriority_Object((1,3,6,1,4,1,1872,2,5,2,1,5,8,1,3),_LacpNewPortActorPortPriority_Type())
lacpNewPortActorPortPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:lacpNewPortActorPortPriority.setStatus(_A)
class _LacpNewPortActorAdminKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LacpNewPortActorAdminKey_Type.__name__=_C
_LacpNewPortActorAdminKey_Object=MibTableColumn
lacpNewPortActorAdminKey=_LacpNewPortActorAdminKey_Object((1,3,6,1,4,1,1872,2,5,2,1,5,8,1,4),_LacpNewPortActorAdminKey_Type())
lacpNewPortActorAdminKey.setMaxAccess(_H)
if mibBuilder.loadTexts:lacpNewPortActorAdminKey.setStatus(_A)
class _LacpCurSystemName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_LacpCurSystemName_Type.__name__=_I
_LacpCurSystemName_Object=MibScalar
lacpCurSystemName=_LacpCurSystemName_Object((1,3,6,1,4,1,1872,2,5,2,1,5,9),_LacpCurSystemName_Type())
lacpCurSystemName.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpCurSystemName.setStatus(_A)
class _LacpNewSystemName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_LacpNewSystemName_Type.__name__=_I
_LacpNewSystemName_Object=MibScalar
lacpNewSystemName=_LacpNewSystemName_Object((1,3,6,1,4,1,1872,2,5,2,1,5,10),_LacpNewSystemName_Type())
lacpNewSystemName.setMaxAccess(_H)
if mibBuilder.loadTexts:lacpNewSystemName.setStatus(_A)
_MstCfg_ObjectIdentity=ObjectIdentity
mstCfg=_MstCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,1,7))
_MstGeneralCfg_ObjectIdentity=ObjectIdentity
mstGeneralCfg=_MstGeneralCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,1,7,1))
class _MstCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_MstCurCfgState_Type.__name__=_C
_MstCurCfgState_Object=MibScalar
mstCurCfgState=_MstCurCfgState_Object((1,3,6,1,4,1,1872,2,5,2,1,7,1,1),_MstCurCfgState_Type())
mstCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCurCfgState.setStatus(_A)
class _MstNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_MstNewCfgState_Type.__name__=_C
_MstNewCfgState_Object=MibScalar
mstNewCfgState=_MstNewCfgState_Object((1,3,6,1,4,1,1872,2,5,2,1,7,1,2),_MstNewCfgState_Type())
mstNewCfgState.setMaxAccess(_H)
if mibBuilder.loadTexts:mstNewCfgState.setStatus(_A)
class _MstCurCfgRegionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MstCurCfgRegionName_Type.__name__=_I
_MstCurCfgRegionName_Object=MibScalar
mstCurCfgRegionName=_MstCurCfgRegionName_Object((1,3,6,1,4,1,1872,2,5,2,1,7,1,3),_MstCurCfgRegionName_Type())
mstCurCfgRegionName.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCurCfgRegionName.setStatus(_A)
class _MstNewCfgRegionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MstNewCfgRegionName_Type.__name__=_I
_MstNewCfgRegionName_Object=MibScalar
mstNewCfgRegionName=_MstNewCfgRegionName_Object((1,3,6,1,4,1,1872,2,5,2,1,7,1,4),_MstNewCfgRegionName_Type())
mstNewCfgRegionName.setMaxAccess(_H)
if mibBuilder.loadTexts:mstNewCfgRegionName.setStatus(_A)
class _MstCurCfgRegionVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MstCurCfgRegionVersion_Type.__name__=_C
_MstCurCfgRegionVersion_Object=MibScalar
mstCurCfgRegionVersion=_MstCurCfgRegionVersion_Object((1,3,6,1,4,1,1872,2,5,2,1,7,1,5),_MstCurCfgRegionVersion_Type())
mstCurCfgRegionVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCurCfgRegionVersion.setStatus(_A)
class _MstNewCfgRegionVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MstNewCfgRegionVersion_Type.__name__=_C
_MstNewCfgRegionVersion_Object=MibScalar
mstNewCfgRegionVersion=_MstNewCfgRegionVersion_Object((1,3,6,1,4,1,1872,2,5,2,1,7,1,6),_MstNewCfgRegionVersion_Type())
mstNewCfgRegionVersion.setMaxAccess(_H)
if mibBuilder.loadTexts:mstNewCfgRegionVersion.setStatus(_A)
class _MstCurCfgMaxHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,60))
_MstCurCfgMaxHopCount_Type.__name__=_C
_MstCurCfgMaxHopCount_Object=MibScalar
mstCurCfgMaxHopCount=_MstCurCfgMaxHopCount_Object((1,3,6,1,4,1,1872,2,5,2,1,7,1,7),_MstCurCfgMaxHopCount_Type())
mstCurCfgMaxHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCurCfgMaxHopCount.setStatus(_A)
class _MstNewCfgMaxHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,60))
_MstNewCfgMaxHopCount_Type.__name__=_C
_MstNewCfgMaxHopCount_Object=MibScalar
mstNewCfgMaxHopCount=_MstNewCfgMaxHopCount_Object((1,3,6,1,4,1,1872,2,5,2,1,7,1,8),_MstNewCfgMaxHopCount_Type())
mstNewCfgMaxHopCount.setMaxAccess(_H)
if mibBuilder.loadTexts:mstNewCfgMaxHopCount.setStatus(_A)
class _MstCurCfgStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mstp',1),('rstp',2)))
_MstCurCfgStpMode_Type.__name__=_C
_MstCurCfgStpMode_Object=MibScalar
mstCurCfgStpMode=_MstCurCfgStpMode_Object((1,3,6,1,4,1,1872,2,5,2,1,7,1,9),_MstCurCfgStpMode_Type())
mstCurCfgStpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCurCfgStpMode.setStatus(_A)
class _MstNewCfgStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mstp',1),('rstp',2)))
_MstNewCfgStpMode_Type.__name__=_C
_MstNewCfgStpMode_Object=MibScalar
mstNewCfgStpMode=_MstNewCfgStpMode_Object((1,3,6,1,4,1,1872,2,5,2,1,7,1,10),_MstNewCfgStpMode_Type())
mstNewCfgStpMode.setMaxAccess(_H)
if mibBuilder.loadTexts:mstNewCfgStpMode.setStatus(_A)
_MstCistCfg_ObjectIdentity=ObjectIdentity
mstCistCfg=_MstCistCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,1,7,2))
class _MstCistDefaultCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('default',1))
_MstCistDefaultCfg_Type.__name__=_C
_MstCistDefaultCfg_Object=MibScalar
mstCistDefaultCfg=_MstCistDefaultCfg_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,1),_MstCistDefaultCfg_Type())
mstCistDefaultCfg.setMaxAccess(_H)
if mibBuilder.loadTexts:mstCistDefaultCfg.setStatus(_A)
_MstCistBridgeCfg_ObjectIdentity=ObjectIdentity
mstCistBridgeCfg=_MstCistBridgeCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,1,7,2,2))
class _MstCistCurCfgBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MstCistCurCfgBridgePriority_Type.__name__=_C
_MstCistCurCfgBridgePriority_Object=MibScalar
mstCistCurCfgBridgePriority=_MstCistCurCfgBridgePriority_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,2,1),_MstCistCurCfgBridgePriority_Type())
mstCistCurCfgBridgePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgBridgePriority.setStatus(_A)
class _MstCistNewCfgBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MstCistNewCfgBridgePriority_Type.__name__=_C
_MstCistNewCfgBridgePriority_Object=MibScalar
mstCistNewCfgBridgePriority=_MstCistNewCfgBridgePriority_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,2,2),_MstCistNewCfgBridgePriority_Type())
mstCistNewCfgBridgePriority.setMaxAccess(_H)
if mibBuilder.loadTexts:mstCistNewCfgBridgePriority.setStatus(_A)
class _MstCistCurCfgBridgeMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_MstCistCurCfgBridgeMaxAge_Type.__name__=_C
_MstCistCurCfgBridgeMaxAge_Object=MibScalar
mstCistCurCfgBridgeMaxAge=_MstCistCurCfgBridgeMaxAge_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,2,5),_MstCistCurCfgBridgeMaxAge_Type())
mstCistCurCfgBridgeMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgBridgeMaxAge.setStatus(_A)
class _MstCistNewCfgBridgeMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_MstCistNewCfgBridgeMaxAge_Type.__name__=_C
_MstCistNewCfgBridgeMaxAge_Object=MibScalar
mstCistNewCfgBridgeMaxAge=_MstCistNewCfgBridgeMaxAge_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,2,6),_MstCistNewCfgBridgeMaxAge_Type())
mstCistNewCfgBridgeMaxAge.setMaxAccess(_H)
if mibBuilder.loadTexts:mstCistNewCfgBridgeMaxAge.setStatus(_A)
class _MstCistCurCfgBridgeForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_MstCistCurCfgBridgeForwardDelay_Type.__name__=_C
_MstCistCurCfgBridgeForwardDelay_Object=MibScalar
mstCistCurCfgBridgeForwardDelay=_MstCistCurCfgBridgeForwardDelay_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,2,7),_MstCistCurCfgBridgeForwardDelay_Type())
mstCistCurCfgBridgeForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgBridgeForwardDelay.setStatus(_A)
class _MstCistNewCfgBridgeForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_MstCistNewCfgBridgeForwardDelay_Type.__name__=_C
_MstCistNewCfgBridgeForwardDelay_Object=MibScalar
mstCistNewCfgBridgeForwardDelay=_MstCistNewCfgBridgeForwardDelay_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,2,8),_MstCistNewCfgBridgeForwardDelay_Type())
mstCistNewCfgBridgeForwardDelay.setMaxAccess(_H)
if mibBuilder.loadTexts:mstCistNewCfgBridgeForwardDelay.setStatus(_A)
_MstCistCurCfgPortTable_Object=MibTable
mstCistCurCfgPortTable=_MstCistCurCfgPortTable_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,3))
if mibBuilder.loadTexts:mstCistCurCfgPortTable.setStatus(_A)
_MstCistCurCfgPortTableEntry_Object=MibTableRow
mstCistCurCfgPortTableEntry=_MstCistCurCfgPortTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,3,1))
mstCistCurCfgPortTableEntry.setIndexNames((0,_G,_p))
if mibBuilder.loadTexts:mstCistCurCfgPortTableEntry.setStatus(_A)
_MstCistCurCfgPortIndex_Type=Integer32
_MstCistCurCfgPortIndex_Object=MibTableColumn
mstCistCurCfgPortIndex=_MstCistCurCfgPortIndex_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,3,1,1),_MstCistCurCfgPortIndex_Type())
mstCistCurCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgPortIndex.setStatus(_A)
class _MstCistCurCfgPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_MstCistCurCfgPortPriority_Type.__name__=_C
_MstCistCurCfgPortPriority_Object=MibTableColumn
mstCistCurCfgPortPriority=_MstCistCurCfgPortPriority_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,3,1,2),_MstCistCurCfgPortPriority_Type())
mstCistCurCfgPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgPortPriority.setStatus(_A)
class _MstCistCurCfgPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_MstCistCurCfgPortPathCost_Type.__name__=_C
_MstCistCurCfgPortPathCost_Object=MibTableColumn
mstCistCurCfgPortPathCost=_MstCistCurCfgPortPathCost_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,3,1,3),_MstCistCurCfgPortPathCost_Type())
mstCistCurCfgPortPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgPortPathCost.setStatus(_A)
class _MstCistCurCfgPortLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_M,2),(_N,3)))
_MstCistCurCfgPortLinkType_Type.__name__=_C
_MstCistCurCfgPortLinkType_Object=MibTableColumn
mstCistCurCfgPortLinkType=_MstCistCurCfgPortLinkType_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,3,1,4),_MstCistCurCfgPortLinkType_Type())
mstCistCurCfgPortLinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgPortLinkType.setStatus(_A)
class _MstCistCurCfgPortEdge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_MstCistCurCfgPortEdge_Type.__name__=_C
_MstCistCurCfgPortEdge_Object=MibTableColumn
mstCistCurCfgPortEdge=_MstCistCurCfgPortEdge_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,3,1,5),_MstCistCurCfgPortEdge_Type())
mstCistCurCfgPortEdge.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgPortEdge.setStatus(_A)
class _MstCistCurCfgPortStpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_K,2)))
_MstCistCurCfgPortStpState_Type.__name__=_C
_MstCistCurCfgPortStpState_Object=MibTableColumn
mstCistCurCfgPortStpState=_MstCistCurCfgPortStpState_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,3,1,6),_MstCistCurCfgPortStpState_Type())
mstCistCurCfgPortStpState.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgPortStpState.setStatus(_A)
class _MstCistCurCfgPortHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_MstCistCurCfgPortHelloTime_Type.__name__=_C
_MstCistCurCfgPortHelloTime_Object=MibTableColumn
mstCistCurCfgPortHelloTime=_MstCistCurCfgPortHelloTime_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,3,1,7),_MstCistCurCfgPortHelloTime_Type())
mstCistCurCfgPortHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistCurCfgPortHelloTime.setStatus(_A)
_MstCistNewCfgPortTable_Object=MibTable
mstCistNewCfgPortTable=_MstCistNewCfgPortTable_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,4))
if mibBuilder.loadTexts:mstCistNewCfgPortTable.setStatus(_A)
_MstCistNewCfgPortTableEntry_Object=MibTableRow
mstCistNewCfgPortTableEntry=_MstCistNewCfgPortTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,4,1))
mstCistNewCfgPortTableEntry.setIndexNames((0,_G,_q))
if mibBuilder.loadTexts:mstCistNewCfgPortTableEntry.setStatus(_A)
_MstCistNewCfgPortIndex_Type=Integer32
_MstCistNewCfgPortIndex_Object=MibTableColumn
mstCistNewCfgPortIndex=_MstCistNewCfgPortIndex_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,4,1,1),_MstCistNewCfgPortIndex_Type())
mstCistNewCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mstCistNewCfgPortIndex.setStatus(_A)
class _MstCistNewCfgPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_MstCistNewCfgPortPriority_Type.__name__=_C
_MstCistNewCfgPortPriority_Object=MibTableColumn
mstCistNewCfgPortPriority=_MstCistNewCfgPortPriority_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,4,1,2),_MstCistNewCfgPortPriority_Type())
mstCistNewCfgPortPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:mstCistNewCfgPortPriority.setStatus(_A)
class _MstCistNewCfgPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_MstCistNewCfgPortPathCost_Type.__name__=_C
_MstCistNewCfgPortPathCost_Object=MibTableColumn
mstCistNewCfgPortPathCost=_MstCistNewCfgPortPathCost_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,4,1,3),_MstCistNewCfgPortPathCost_Type())
mstCistNewCfgPortPathCost.setMaxAccess(_H)
if mibBuilder.loadTexts:mstCistNewCfgPortPathCost.setStatus(_A)
class _MstCistNewCfgPortLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_M,2),(_N,3)))
_MstCistNewCfgPortLinkType_Type.__name__=_C
_MstCistNewCfgPortLinkType_Object=MibTableColumn
mstCistNewCfgPortLinkType=_MstCistNewCfgPortLinkType_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,4,1,4),_MstCistNewCfgPortLinkType_Type())
mstCistNewCfgPortLinkType.setMaxAccess(_H)
if mibBuilder.loadTexts:mstCistNewCfgPortLinkType.setStatus(_A)
class _MstCistNewCfgPortEdge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_MstCistNewCfgPortEdge_Type.__name__=_C
_MstCistNewCfgPortEdge_Object=MibTableColumn
mstCistNewCfgPortEdge=_MstCistNewCfgPortEdge_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,4,1,5),_MstCistNewCfgPortEdge_Type())
mstCistNewCfgPortEdge.setMaxAccess(_H)
if mibBuilder.loadTexts:mstCistNewCfgPortEdge.setStatus(_A)
class _MstCistNewCfgPortStpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_K,2)))
_MstCistNewCfgPortStpState_Type.__name__=_C
_MstCistNewCfgPortStpState_Object=MibTableColumn
mstCistNewCfgPortStpState=_MstCistNewCfgPortStpState_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,4,1,6),_MstCistNewCfgPortStpState_Type())
mstCistNewCfgPortStpState.setMaxAccess(_H)
if mibBuilder.loadTexts:mstCistNewCfgPortStpState.setStatus(_A)
class _MstCistNewCfgPortHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_MstCistNewCfgPortHelloTime_Type.__name__=_C
_MstCistNewCfgPortHelloTime_Object=MibTableColumn
mstCistNewCfgPortHelloTime=_MstCistNewCfgPortHelloTime_Object((1,3,6,1,4,1,1872,2,5,2,1,7,2,4,1,7),_MstCistNewCfgPortHelloTime_Type())
mstCistNewCfgPortHelloTime.setMaxAccess(_H)
if mibBuilder.loadTexts:mstCistNewCfgPortHelloTime.setStatus(_A)
_PortTeamCfg_ObjectIdentity=ObjectIdentity
portTeamCfg=_PortTeamCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,1,9))
_PortTeamTableMaxSize_Type=Integer32
_PortTeamTableMaxSize_Object=MibScalar
portTeamTableMaxSize=_PortTeamTableMaxSize_Object((1,3,6,1,4,1,1872,2,5,2,1,9,1),_PortTeamTableMaxSize_Type())
portTeamTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:portTeamTableMaxSize.setStatus(_A)
_PortTeamCurCfgTable_Object=MibTable
portTeamCurCfgTable=_PortTeamCurCfgTable_Object((1,3,6,1,4,1,1872,2,5,2,1,9,2))
if mibBuilder.loadTexts:portTeamCurCfgTable.setStatus(_A)
_PortTeamCurCfgTableEntry_Object=MibTableRow
portTeamCurCfgTableEntry=_PortTeamCurCfgTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,9,2,1))
portTeamCurCfgTableEntry.setIndexNames((0,_G,_r))
if mibBuilder.loadTexts:portTeamCurCfgTableEntry.setStatus(_A)
_PortTeamCurCfgIndex_Type=Integer32
_PortTeamCurCfgIndex_Object=MibTableColumn
portTeamCurCfgIndex=_PortTeamCurCfgIndex_Object((1,3,6,1,4,1,1872,2,5,2,1,9,2,1,1),_PortTeamCurCfgIndex_Type())
portTeamCurCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portTeamCurCfgIndex.setStatus(_A)
class _PortTeamCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_PortTeamCurCfgState_Type.__name__=_C
_PortTeamCurCfgState_Object=MibTableColumn
portTeamCurCfgState=_PortTeamCurCfgState_Object((1,3,6,1,4,1,1872,2,5,2,1,9,2,1,2),_PortTeamCurCfgState_Type())
portTeamCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:portTeamCurCfgState.setStatus(_A)
_PortTeamCurCfgPorts_Type=OctetString
_PortTeamCurCfgPorts_Object=MibTableColumn
portTeamCurCfgPorts=_PortTeamCurCfgPorts_Object((1,3,6,1,4,1,1872,2,5,2,1,9,2,1,3),_PortTeamCurCfgPorts_Type())
portTeamCurCfgPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:portTeamCurCfgPorts.setStatus(_A)
_PortTeamCurCfgTrunks_Type=OctetString
_PortTeamCurCfgTrunks_Object=MibTableColumn
portTeamCurCfgTrunks=_PortTeamCurCfgTrunks_Object((1,3,6,1,4,1,1872,2,5,2,1,9,2,1,4),_PortTeamCurCfgTrunks_Type())
portTeamCurCfgTrunks.setMaxAccess(_B)
if mibBuilder.loadTexts:portTeamCurCfgTrunks.setStatus(_A)
class _PortTeamCurCfgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PortTeamCurCfgName_Type.__name__=_I
_PortTeamCurCfgName_Object=MibTableColumn
portTeamCurCfgName=_PortTeamCurCfgName_Object((1,3,6,1,4,1,1872,2,5,2,1,9,2,1,5),_PortTeamCurCfgName_Type())
portTeamCurCfgName.setMaxAccess(_B)
if mibBuilder.loadTexts:portTeamCurCfgName.setStatus(_A)
_PortTeamNewCfgTable_Object=MibTable
portTeamNewCfgTable=_PortTeamNewCfgTable_Object((1,3,6,1,4,1,1872,2,5,2,1,9,3))
if mibBuilder.loadTexts:portTeamNewCfgTable.setStatus(_A)
_PortTeamNewCfgTableEntry_Object=MibTableRow
portTeamNewCfgTableEntry=_PortTeamNewCfgTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,9,3,1))
portTeamNewCfgTableEntry.setIndexNames((0,_G,_s))
if mibBuilder.loadTexts:portTeamNewCfgTableEntry.setStatus(_A)
_PortTeamNewCfgIndex_Type=Integer32
_PortTeamNewCfgIndex_Object=MibTableColumn
portTeamNewCfgIndex=_PortTeamNewCfgIndex_Object((1,3,6,1,4,1,1872,2,5,2,1,9,3,1,1),_PortTeamNewCfgIndex_Type())
portTeamNewCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portTeamNewCfgIndex.setStatus(_A)
class _PortTeamNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_PortTeamNewCfgState_Type.__name__=_C
_PortTeamNewCfgState_Object=MibTableColumn
portTeamNewCfgState=_PortTeamNewCfgState_Object((1,3,6,1,4,1,1872,2,5,2,1,9,3,1,2),_PortTeamNewCfgState_Type())
portTeamNewCfgState.setMaxAccess(_D)
if mibBuilder.loadTexts:portTeamNewCfgState.setStatus(_A)
_PortTeamNewCfgPorts_Type=OctetString
_PortTeamNewCfgPorts_Object=MibTableColumn
portTeamNewCfgPorts=_PortTeamNewCfgPorts_Object((1,3,6,1,4,1,1872,2,5,2,1,9,3,1,3),_PortTeamNewCfgPorts_Type())
portTeamNewCfgPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:portTeamNewCfgPorts.setStatus(_A)
_PortTeamNewCfgAddPort_Type=Integer32
_PortTeamNewCfgAddPort_Object=MibTableColumn
portTeamNewCfgAddPort=_PortTeamNewCfgAddPort_Object((1,3,6,1,4,1,1872,2,5,2,1,9,3,1,4),_PortTeamNewCfgAddPort_Type())
portTeamNewCfgAddPort.setMaxAccess(_D)
if mibBuilder.loadTexts:portTeamNewCfgAddPort.setStatus(_A)
_PortTeamNewCfgRemovePort_Type=Integer32
_PortTeamNewCfgRemovePort_Object=MibTableColumn
portTeamNewCfgRemovePort=_PortTeamNewCfgRemovePort_Object((1,3,6,1,4,1,1872,2,5,2,1,9,3,1,5),_PortTeamNewCfgRemovePort_Type())
portTeamNewCfgRemovePort.setMaxAccess(_D)
if mibBuilder.loadTexts:portTeamNewCfgRemovePort.setStatus(_A)
_PortTeamNewCfgTrunks_Type=OctetString
_PortTeamNewCfgTrunks_Object=MibTableColumn
portTeamNewCfgTrunks=_PortTeamNewCfgTrunks_Object((1,3,6,1,4,1,1872,2,5,2,1,9,3,1,6),_PortTeamNewCfgTrunks_Type())
portTeamNewCfgTrunks.setMaxAccess(_B)
if mibBuilder.loadTexts:portTeamNewCfgTrunks.setStatus(_A)
_PortTeamNewCfgAddTrunk_Type=Integer32
_PortTeamNewCfgAddTrunk_Object=MibTableColumn
portTeamNewCfgAddTrunk=_PortTeamNewCfgAddTrunk_Object((1,3,6,1,4,1,1872,2,5,2,1,9,3,1,7),_PortTeamNewCfgAddTrunk_Type())
portTeamNewCfgAddTrunk.setMaxAccess(_D)
if mibBuilder.loadTexts:portTeamNewCfgAddTrunk.setStatus(_A)
_PortTeamNewCfgRemoveTrunk_Type=Integer32
_PortTeamNewCfgRemoveTrunk_Object=MibTableColumn
portTeamNewCfgRemoveTrunk=_PortTeamNewCfgRemoveTrunk_Object((1,3,6,1,4,1,1872,2,5,2,1,9,3,1,8),_PortTeamNewCfgRemoveTrunk_Type())
portTeamNewCfgRemoveTrunk.setMaxAccess(_D)
if mibBuilder.loadTexts:portTeamNewCfgRemoveTrunk.setStatus(_A)
class _PortTeamNewCfgDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_R,2)))
_PortTeamNewCfgDelete_Type.__name__=_C
_PortTeamNewCfgDelete_Object=MibTableColumn
portTeamNewCfgDelete=_PortTeamNewCfgDelete_Object((1,3,6,1,4,1,1872,2,5,2,1,9,3,1,9),_PortTeamNewCfgDelete_Type())
portTeamNewCfgDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:portTeamNewCfgDelete.setStatus(_A)
class _PortTeamNewCfgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PortTeamNewCfgName_Type.__name__=_I
_PortTeamNewCfgName_Object=MibTableColumn
portTeamNewCfgName=_PortTeamNewCfgName_Object((1,3,6,1,4,1,1872,2,5,2,1,9,3,1,10),_PortTeamNewCfgName_Type())
portTeamNewCfgName.setMaxAccess(_D)
if mibBuilder.loadTexts:portTeamNewCfgName.setStatus(_A)
_VadcVlan_ObjectIdentity=ObjectIdentity
vadcVlan=_VadcVlan_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,1,10))
_VadcVlanCurCfgTable_Object=MibTable
vadcVlanCurCfgTable=_VadcVlanCurCfgTable_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1))
if mibBuilder.loadTexts:vadcVlanCurCfgTable.setStatus(_A)
_VadcVlanCurCfgTableEntry_Object=MibTableRow
vadcVlanCurCfgTableEntry=_VadcVlanCurCfgTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1))
vadcVlanCurCfgTableEntry.setIndexNames((0,_G,_t))
if mibBuilder.loadTexts:vadcVlanCurCfgTableEntry.setStatus(_A)
_VadcVlanCurCfgVlanId_Type=Integer32
_VadcVlanCurCfgVlanId_Object=MibTableColumn
vadcVlanCurCfgVlanId=_VadcVlanCurCfgVlanId_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,1),_VadcVlanCurCfgVlanId_Type())
vadcVlanCurCfgVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgVlanId.setStatus(_A)
_VadcVlanCurCfgBwmCont_Type=Integer32
_VadcVlanCurCfgBwmCont_Object=MibTableColumn
vadcVlanCurCfgBwmCont=_VadcVlanCurCfgBwmCont_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,2),_VadcVlanCurCfgBwmCont_Type())
vadcVlanCurCfgBwmCont.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgBwmCont.setStatus(_A)
_VadcVlanCurCfgNonIp_Type=Integer32
_VadcVlanCurCfgNonIp_Object=MibTableColumn
vadcVlanCurCfgNonIp=_VadcVlanCurCfgNonIp_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,3),_VadcVlanCurCfgNonIp_Type())
vadcVlanCurCfgNonIp.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgNonIp.setStatus(_A)
class _VadcVlanCurCfgIpv6LlaGen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VadcVlanCurCfgIpv6LlaGen_Type.__name__=_C
_VadcVlanCurCfgIpv6LlaGen_Object=MibTableColumn
vadcVlanCurCfgIpv6LlaGen=_VadcVlanCurCfgIpv6LlaGen_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,4),_VadcVlanCurCfgIpv6LlaGen_Type())
vadcVlanCurCfgIpv6LlaGen.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgIpv6LlaGen.setStatus(_A)
class _VadcVlanCurCfgRouterAdv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VadcVlanCurCfgRouterAdv_Type.__name__=_C
_VadcVlanCurCfgRouterAdv_Object=MibTableColumn
vadcVlanCurCfgRouterAdv=_VadcVlanCurCfgRouterAdv_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,5),_VadcVlanCurCfgRouterAdv_Type())
vadcVlanCurCfgRouterAdv.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgRouterAdv.setStatus(_A)
class _VadcVlanCurCfgReTransInt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_VadcVlanCurCfgReTransInt_Type.__name__=_J
_VadcVlanCurCfgReTransInt_Object=MibTableColumn
vadcVlanCurCfgReTransInt=_VadcVlanCurCfgReTransInt_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,6),_VadcVlanCurCfgReTransInt_Type())
vadcVlanCurCfgReTransInt.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgReTransInt.setStatus(_A)
class _VadcVlanCurCfgMinIntBwAdv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1800))
_VadcVlanCurCfgMinIntBwAdv_Type.__name__=_C
_VadcVlanCurCfgMinIntBwAdv_Object=MibTableColumn
vadcVlanCurCfgMinIntBwAdv=_VadcVlanCurCfgMinIntBwAdv_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,7),_VadcVlanCurCfgMinIntBwAdv_Type())
vadcVlanCurCfgMinIntBwAdv.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgMinIntBwAdv.setStatus(_A)
class _VadcVlanCurCfgMaxIntBwAdv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_VadcVlanCurCfgMaxIntBwAdv_Type.__name__=_C
_VadcVlanCurCfgMaxIntBwAdv_Object=MibTableColumn
vadcVlanCurCfgMaxIntBwAdv=_VadcVlanCurCfgMaxIntBwAdv_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,8),_VadcVlanCurCfgMaxIntBwAdv_Type())
vadcVlanCurCfgMaxIntBwAdv.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgMaxIntBwAdv.setStatus(_A)
class _VadcVlanCurCfgMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1200,1500))
_VadcVlanCurCfgMtu_Type.__name__=_C
_VadcVlanCurCfgMtu_Object=MibTableColumn
vadcVlanCurCfgMtu=_VadcVlanCurCfgMtu_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,9),_VadcVlanCurCfgMtu_Type())
vadcVlanCurCfgMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgMtu.setStatus(_A)
class _VadcVlanCurCfgCurHopLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VadcVlanCurCfgCurHopLimit_Type.__name__=_C
_VadcVlanCurCfgCurHopLimit_Object=MibTableColumn
vadcVlanCurCfgCurHopLimit=_VadcVlanCurCfgCurHopLimit_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,10),_VadcVlanCurCfgCurHopLimit_Type())
vadcVlanCurCfgCurHopLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgCurHopLimit.setStatus(_A)
class _VadcVlanCurCfgMFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VadcVlanCurCfgMFlag_Type.__name__=_C
_VadcVlanCurCfgMFlag_Object=MibTableColumn
vadcVlanCurCfgMFlag=_VadcVlanCurCfgMFlag_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,11),_VadcVlanCurCfgMFlag_Type())
vadcVlanCurCfgMFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgMFlag.setStatus(_A)
class _VadcVlanCurCfgOFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VadcVlanCurCfgOFlag_Type.__name__=_C
_VadcVlanCurCfgOFlag_Object=MibTableColumn
vadcVlanCurCfgOFlag=_VadcVlanCurCfgOFlag_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,12),_VadcVlanCurCfgOFlag_Type())
vadcVlanCurCfgOFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgOFlag.setStatus(_A)
class _VadcVlanCurCfgRTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_VadcVlanCurCfgRTime_Type.__name__=_C
_VadcVlanCurCfgRTime_Object=MibTableColumn
vadcVlanCurCfgRTime=_VadcVlanCurCfgRTime_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,13),_VadcVlanCurCfgRTime_Type())
vadcVlanCurCfgRTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgRTime.setStatus(_A)
class _VadcVlanCurCfgRlTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9000))
_VadcVlanCurCfgRlTime_Type.__name__=_C
_VadcVlanCurCfgRlTime_Object=MibTableColumn
vadcVlanCurCfgRlTime=_VadcVlanCurCfgRlTime_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,14),_VadcVlanCurCfgRlTime_Type())
vadcVlanCurCfgRlTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgRlTime.setStatus(_A)
class _VadcVlanCurCfgPlTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_VadcVlanCurCfgPlTime_Type.__name__=_J
_VadcVlanCurCfgPlTime_Object=MibTableColumn
vadcVlanCurCfgPlTime=_VadcVlanCurCfgPlTime_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,15),_VadcVlanCurCfgPlTime_Type())
vadcVlanCurCfgPlTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgPlTime.setStatus(_A)
class _VadcVlanCurCfgVlTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_VadcVlanCurCfgVlTime_Type.__name__=_J
_VadcVlanCurCfgVlTime_Object=MibTableColumn
vadcVlanCurCfgVlTime=_VadcVlanCurCfgVlTime_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,16),_VadcVlanCurCfgVlTime_Type())
vadcVlanCurCfgVlTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgVlTime.setStatus(_A)
class _VadcVlanCurCfgOpInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VadcVlanCurCfgOpInfo_Type.__name__=_C
_VadcVlanCurCfgOpInfo_Object=MibTableColumn
vadcVlanCurCfgOpInfo=_VadcVlanCurCfgOpInfo_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,17),_VadcVlanCurCfgOpInfo_Type())
vadcVlanCurCfgOpInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgOpInfo.setStatus(_A)
class _VadcVlanCurCfgApInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VadcVlanCurCfgApInfo_Type.__name__=_C
_VadcVlanCurCfgApInfo_Object=MibTableColumn
vadcVlanCurCfgApInfo=_VadcVlanCurCfgApInfo_Object((1,3,6,1,4,1,1872,2,5,2,1,10,1,1,18),_VadcVlanCurCfgApInfo_Type())
vadcVlanCurCfgApInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanCurCfgApInfo.setStatus(_A)
_VadcVlanNewCfgTable_Object=MibTable
vadcVlanNewCfgTable=_VadcVlanNewCfgTable_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2))
if mibBuilder.loadTexts:vadcVlanNewCfgTable.setStatus(_A)
_VadcVlanNewCfgTableEntry_Object=MibTableRow
vadcVlanNewCfgTableEntry=_VadcVlanNewCfgTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1))
vadcVlanNewCfgTableEntry.setIndexNames((0,_G,_u))
if mibBuilder.loadTexts:vadcVlanNewCfgTableEntry.setStatus(_A)
_VadcVlanNewCfgVlanId_Type=Integer32
_VadcVlanNewCfgVlanId_Object=MibTableColumn
vadcVlanNewCfgVlanId=_VadcVlanNewCfgVlanId_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,1),_VadcVlanNewCfgVlanId_Type())
vadcVlanNewCfgVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vadcVlanNewCfgVlanId.setStatus(_A)
_VadcVlanNewCfgBwmCont_Type=Integer32
_VadcVlanNewCfgBwmCont_Object=MibTableColumn
vadcVlanNewCfgBwmCont=_VadcVlanNewCfgBwmCont_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,2),_VadcVlanNewCfgBwmCont_Type())
vadcVlanNewCfgBwmCont.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgBwmCont.setStatus(_A)
_VadcVlanNewCfgNonIp_Type=Integer32
_VadcVlanNewCfgNonIp_Object=MibTableColumn
vadcVlanNewCfgNonIp=_VadcVlanNewCfgNonIp_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,3),_VadcVlanNewCfgNonIp_Type())
vadcVlanNewCfgNonIp.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgNonIp.setStatus(_A)
class _VadcVlanNewCfgIpv6LlaGen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VadcVlanNewCfgIpv6LlaGen_Type.__name__=_C
_VadcVlanNewCfgIpv6LlaGen_Object=MibTableColumn
vadcVlanNewCfgIpv6LlaGen=_VadcVlanNewCfgIpv6LlaGen_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,4),_VadcVlanNewCfgIpv6LlaGen_Type())
vadcVlanNewCfgIpv6LlaGen.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgIpv6LlaGen.setStatus(_A)
class _VadcVlanNewCfgRouterAdv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VadcVlanNewCfgRouterAdv_Type.__name__=_C
_VadcVlanNewCfgRouterAdv_Object=MibTableColumn
vadcVlanNewCfgRouterAdv=_VadcVlanNewCfgRouterAdv_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,5),_VadcVlanNewCfgRouterAdv_Type())
vadcVlanNewCfgRouterAdv.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgRouterAdv.setStatus(_A)
class _VadcVlanNewCfgReTransInt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_VadcVlanNewCfgReTransInt_Type.__name__=_J
_VadcVlanNewCfgReTransInt_Object=MibTableColumn
vadcVlanNewCfgReTransInt=_VadcVlanNewCfgReTransInt_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,6),_VadcVlanNewCfgReTransInt_Type())
vadcVlanNewCfgReTransInt.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgReTransInt.setStatus(_A)
class _VadcVlanNewCfgMinIntBwAdv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1800))
_VadcVlanNewCfgMinIntBwAdv_Type.__name__=_C
_VadcVlanNewCfgMinIntBwAdv_Object=MibTableColumn
vadcVlanNewCfgMinIntBwAdv=_VadcVlanNewCfgMinIntBwAdv_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,7),_VadcVlanNewCfgMinIntBwAdv_Type())
vadcVlanNewCfgMinIntBwAdv.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgMinIntBwAdv.setStatus(_A)
class _VadcVlanNewCfgMaxIntBwAdv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_VadcVlanNewCfgMaxIntBwAdv_Type.__name__=_C
_VadcVlanNewCfgMaxIntBwAdv_Object=MibTableColumn
vadcVlanNewCfgMaxIntBwAdv=_VadcVlanNewCfgMaxIntBwAdv_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,8),_VadcVlanNewCfgMaxIntBwAdv_Type())
vadcVlanNewCfgMaxIntBwAdv.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgMaxIntBwAdv.setStatus(_A)
class _VadcVlanNewCfgMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1200,1500))
_VadcVlanNewCfgMtu_Type.__name__=_C
_VadcVlanNewCfgMtu_Object=MibTableColumn
vadcVlanNewCfgMtu=_VadcVlanNewCfgMtu_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,9),_VadcVlanNewCfgMtu_Type())
vadcVlanNewCfgMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgMtu.setStatus(_A)
class _VadcVlanNewCfgCurHopLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VadcVlanNewCfgCurHopLimit_Type.__name__=_C
_VadcVlanNewCfgCurHopLimit_Object=MibTableColumn
vadcVlanNewCfgCurHopLimit=_VadcVlanNewCfgCurHopLimit_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,10),_VadcVlanNewCfgCurHopLimit_Type())
vadcVlanNewCfgCurHopLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgCurHopLimit.setStatus(_A)
class _VadcVlanNewCfgMFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VadcVlanNewCfgMFlag_Type.__name__=_C
_VadcVlanNewCfgMFlag_Object=MibTableColumn
vadcVlanNewCfgMFlag=_VadcVlanNewCfgMFlag_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,11),_VadcVlanNewCfgMFlag_Type())
vadcVlanNewCfgMFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgMFlag.setStatus(_A)
class _VadcVlanNewCfgOFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VadcVlanNewCfgOFlag_Type.__name__=_C
_VadcVlanNewCfgOFlag_Object=MibTableColumn
vadcVlanNewCfgOFlag=_VadcVlanNewCfgOFlag_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,12),_VadcVlanNewCfgOFlag_Type())
vadcVlanNewCfgOFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgOFlag.setStatus(_A)
class _VadcVlanNewCfgRTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_VadcVlanNewCfgRTime_Type.__name__=_C
_VadcVlanNewCfgRTime_Object=MibTableColumn
vadcVlanNewCfgRTime=_VadcVlanNewCfgRTime_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,13),_VadcVlanNewCfgRTime_Type())
vadcVlanNewCfgRTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgRTime.setStatus(_A)
class _VadcVlanNewCfgRlTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9000))
_VadcVlanNewCfgRlTime_Type.__name__=_C
_VadcVlanNewCfgRlTime_Object=MibTableColumn
vadcVlanNewCfgRlTime=_VadcVlanNewCfgRlTime_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,14),_VadcVlanNewCfgRlTime_Type())
vadcVlanNewCfgRlTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgRlTime.setStatus(_A)
class _VadcVlanNewCfgPlTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_VadcVlanNewCfgPlTime_Type.__name__=_J
_VadcVlanNewCfgPlTime_Object=MibTableColumn
vadcVlanNewCfgPlTime=_VadcVlanNewCfgPlTime_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,15),_VadcVlanNewCfgPlTime_Type())
vadcVlanNewCfgPlTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgPlTime.setStatus(_A)
class _VadcVlanNewCfgVlTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_VadcVlanNewCfgVlTime_Type.__name__=_J
_VadcVlanNewCfgVlTime_Object=MibTableColumn
vadcVlanNewCfgVlTime=_VadcVlanNewCfgVlTime_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,16),_VadcVlanNewCfgVlTime_Type())
vadcVlanNewCfgVlTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgVlTime.setStatus(_A)
class _VadcVlanNewCfgOpInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VadcVlanNewCfgOpInfo_Type.__name__=_C
_VadcVlanNewCfgOpInfo_Object=MibTableColumn
vadcVlanNewCfgOpInfo=_VadcVlanNewCfgOpInfo_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,17),_VadcVlanNewCfgOpInfo_Type())
vadcVlanNewCfgOpInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgOpInfo.setStatus(_A)
class _VadcVlanNewCfgApInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VadcVlanNewCfgApInfo_Type.__name__=_C
_VadcVlanNewCfgApInfo_Object=MibTableColumn
vadcVlanNewCfgApInfo=_VadcVlanNewCfgApInfo_Object((1,3,6,1,4,1,1872,2,5,2,1,10,2,1,18),_VadcVlanNewCfgApInfo_Type())
vadcVlanNewCfgApInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:vadcVlanNewCfgApInfo.setStatus(_A)
_Layer2Stats_ObjectIdentity=ObjectIdentity
layer2Stats=_Layer2Stats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,2))
_FdbStats_ObjectIdentity=ObjectIdentity
fdbStats=_FdbStats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,2,1))
_FdbStatsCreates_Type=Counter32
_FdbStatsCreates_Object=MibScalar
fdbStatsCreates=_FdbStatsCreates_Object((1,3,6,1,4,1,1872,2,5,2,2,1,1),_FdbStatsCreates_Type())
fdbStatsCreates.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsCreates.setStatus(_A)
_FdbStatsDeletes_Type=Counter32
_FdbStatsDeletes_Object=MibScalar
fdbStatsDeletes=_FdbStatsDeletes_Object((1,3,6,1,4,1,1872,2,5,2,2,1,2),_FdbStatsDeletes_Type())
fdbStatsDeletes.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsDeletes.setStatus(_A)
_FdbStatsCurrent_Type=Gauge32
_FdbStatsCurrent_Object=MibScalar
fdbStatsCurrent=_FdbStatsCurrent_Object((1,3,6,1,4,1,1872,2,5,2,2,1,3),_FdbStatsCurrent_Type())
fdbStatsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsCurrent.setStatus(_A)
_FdbStatsHiwat_Type=Integer32
_FdbStatsHiwat_Object=MibScalar
fdbStatsHiwat=_FdbStatsHiwat_Object((1,3,6,1,4,1,1872,2,5,2,2,1,4),_FdbStatsHiwat_Type())
fdbStatsHiwat.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsHiwat.setStatus(_A)
_FdbStatsLookups_Type=Counter32
_FdbStatsLookups_Object=MibScalar
fdbStatsLookups=_FdbStatsLookups_Object((1,3,6,1,4,1,1872,2,5,2,2,1,5),_FdbStatsLookups_Type())
fdbStatsLookups.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsLookups.setStatus(_A)
_FdbStatsLookupFails_Type=Counter32
_FdbStatsLookupFails_Object=MibScalar
fdbStatsLookupFails=_FdbStatsLookupFails_Object((1,3,6,1,4,1,1872,2,5,2,2,1,6),_FdbStatsLookupFails_Type())
fdbStatsLookupFails.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsLookupFails.setStatus(_A)
_FdbStatsFinds_Type=Counter32
_FdbStatsFinds_Object=MibScalar
fdbStatsFinds=_FdbStatsFinds_Object((1,3,6,1,4,1,1872,2,5,2,2,1,7),_FdbStatsFinds_Type())
fdbStatsFinds.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsFinds.setStatus(_A)
_FdbStatsFindFails_Type=Counter32
_FdbStatsFindFails_Object=MibScalar
fdbStatsFindFails=_FdbStatsFindFails_Object((1,3,6,1,4,1,1872,2,5,2,2,1,8),_FdbStatsFindFails_Type())
fdbStatsFindFails.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsFindFails.setStatus(_A)
_FdbStatsFindOrCreates_Type=Counter32
_FdbStatsFindOrCreates_Object=MibScalar
fdbStatsFindOrCreates=_FdbStatsFindOrCreates_Object((1,3,6,1,4,1,1872,2,5,2,2,1,9),_FdbStatsFindOrCreates_Type())
fdbStatsFindOrCreates.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsFindOrCreates.setStatus(_A)
_FdbStatsOverflows_Type=Counter32
_FdbStatsOverflows_Object=MibScalar
fdbStatsOverflows=_FdbStatsOverflows_Object((1,3,6,1,4,1,1872,2,5,2,2,1,10),_FdbStatsOverflows_Type())
fdbStatsOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbStatsOverflows.setStatus(_A)
_StpStats_ObjectIdentity=ObjectIdentity
stpStats=_StpStats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,2,2))
_StgStatsPortTable_Object=MibTable
stgStatsPortTable=_StgStatsPortTable_Object((1,3,6,1,4,1,1872,2,5,2,2,2,1))
if mibBuilder.loadTexts:stgStatsPortTable.setStatus(_A)
_StgStatsPortTableEntry_Object=MibTableRow
stgStatsPortTableEntry=_StgStatsPortTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,2,2,1,1))
stgStatsPortTableEntry.setIndexNames((0,_G,_v),(0,_G,_w))
if mibBuilder.loadTexts:stgStatsPortTableEntry.setStatus(_A)
_StgStatsStpIndex_Type=Integer32
_StgStatsStpIndex_Object=MibTableColumn
stgStatsStpIndex=_StgStatsStpIndex_Object((1,3,6,1,4,1,1872,2,5,2,2,2,1,1,1),_StgStatsStpIndex_Type())
stgStatsStpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgStatsStpIndex.setStatus(_A)
_StgStatsPortIndex_Type=Integer32
_StgStatsPortIndex_Object=MibTableColumn
stgStatsPortIndex=_StgStatsPortIndex_Object((1,3,6,1,4,1,1872,2,5,2,2,2,1,1,2),_StgStatsPortIndex_Type())
stgStatsPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgStatsPortIndex.setStatus(_A)
_StgStatsPortRcvCfgBpdus_Type=Integer32
_StgStatsPortRcvCfgBpdus_Object=MibTableColumn
stgStatsPortRcvCfgBpdus=_StgStatsPortRcvCfgBpdus_Object((1,3,6,1,4,1,1872,2,5,2,2,2,1,1,3),_StgStatsPortRcvCfgBpdus_Type())
stgStatsPortRcvCfgBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:stgStatsPortRcvCfgBpdus.setStatus(_A)
_StgStatsPortRcvTcnBpdus_Type=Integer32
_StgStatsPortRcvTcnBpdus_Object=MibTableColumn
stgStatsPortRcvTcnBpdus=_StgStatsPortRcvTcnBpdus_Object((1,3,6,1,4,1,1872,2,5,2,2,2,1,1,4),_StgStatsPortRcvTcnBpdus_Type())
stgStatsPortRcvTcnBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:stgStatsPortRcvTcnBpdus.setStatus(_A)
_StgStatsPortXmtCfgBpdus_Type=Integer32
_StgStatsPortXmtCfgBpdus_Object=MibTableColumn
stgStatsPortXmtCfgBpdus=_StgStatsPortXmtCfgBpdus_Object((1,3,6,1,4,1,1872,2,5,2,2,2,1,1,5),_StgStatsPortXmtCfgBpdus_Type())
stgStatsPortXmtCfgBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:stgStatsPortXmtCfgBpdus.setStatus(_A)
_StgStatsPortXmtTcnBpdus_Type=Integer32
_StgStatsPortXmtTcnBpdus_Object=MibTableColumn
stgStatsPortXmtTcnBpdus=_StgStatsPortXmtTcnBpdus_Object((1,3,6,1,4,1,1872,2,5,2,2,2,1,1,6),_StgStatsPortXmtTcnBpdus_Type())
stgStatsPortXmtTcnBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:stgStatsPortXmtTcnBpdus.setStatus(_A)
_Layer2Info_ObjectIdentity=ObjectIdentity
layer2Info=_Layer2Info_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,3))
_FdbInfo_ObjectIdentity=ObjectIdentity
fdbInfo=_FdbInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,3,1))
class _FdbClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('clear',2)))
_FdbClear_Type.__name__=_C
_FdbClear_Object=MibScalar
fdbClear=_FdbClear_Object((1,3,6,1,4,1,1872,2,5,2,3,1,1),_FdbClear_Type())
fdbClear.setMaxAccess(_H)
if mibBuilder.loadTexts:fdbClear.setStatus(_A)
_FdbTable_Object=MibTable
fdbTable=_FdbTable_Object((1,3,6,1,4,1,1872,2,5,2,3,1,2))
if mibBuilder.loadTexts:fdbTable.setStatus(_A)
_FdbEntry_Object=MibTableRow
fdbEntry=_FdbEntry_Object((1,3,6,1,4,1,1872,2,5,2,3,1,2,1))
fdbEntry.setIndexNames((0,_G,_x))
if mibBuilder.loadTexts:fdbEntry.setStatus(_A)
_FdbMacAddr_Type=PhysAddress
_FdbMacAddr_Object=MibTableColumn
fdbMacAddr=_FdbMacAddr_Object((1,3,6,1,4,1,1872,2,5,2,3,1,2,1,1),_FdbMacAddr_Type())
fdbMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbMacAddr.setStatus(_A)
_FdbVlan_Type=Integer32
_FdbVlan_Object=MibTableColumn
fdbVlan=_FdbVlan_Object((1,3,6,1,4,1,1872,2,5,2,3,1,2,1,2),_FdbVlan_Type())
fdbVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbVlan.setStatus(_A)
_FdbSrcPort_Type=Integer32
_FdbSrcPort_Object=MibTableColumn
fdbSrcPort=_FdbSrcPort_Object((1,3,6,1,4,1,1872,2,5,2,3,1,2,1,3),_FdbSrcPort_Type())
fdbSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbSrcPort.setStatus(_A)
class _FdbState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_Q,1),('ignore',2),('forward',3),('flood',4),('ffd',5),('trunk',6),('vir',7),('vsr',8),('vpr',9),(_P,10)))
_FdbState_Type.__name__=_C
_FdbState_Object=MibTableColumn
fdbState=_FdbState_Object((1,3,6,1,4,1,1872,2,5,2,3,1,2,1,4),_FdbState_Type())
fdbState.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbState.setStatus(_A)
class _FdbRefSps_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FdbRefSps_Type.__name__=_I
_FdbRefSps_Object=MibTableColumn
fdbRefSps=_FdbRefSps_Object((1,3,6,1,4,1,1872,2,5,2,3,1,2,1,5),_FdbRefSps_Type())
fdbRefSps.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbRefSps.setStatus(_A)
_FdbLearnedPort_Type=Integer32
_FdbLearnedPort_Object=MibTableColumn
fdbLearnedPort=_FdbLearnedPort_Object((1,3,6,1,4,1,1872,2,5,2,3,1,2,1,6),_FdbLearnedPort_Type())
fdbLearnedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbLearnedPort.setStatus(_A)
_FdbSrcTrunk_Type=Integer32
_FdbSrcTrunk_Object=MibTableColumn
fdbSrcTrunk=_FdbSrcTrunk_Object((1,3,6,1,4,1,1872,2,5,2,3,1,2,1,7),_FdbSrcTrunk_Type())
fdbSrcTrunk.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbSrcTrunk.setStatus(_A)
_StpInfo_ObjectIdentity=ObjectIdentity
stpInfo=_StpInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,3,2))
_StpInfoTable_Object=MibTable
stpInfoTable=_StpInfoTable_Object((1,3,6,1,4,1,1872,2,5,2,3,2,1))
if mibBuilder.loadTexts:stpInfoTable.setStatus(_A)
_StpInfoTableEntry_Object=MibTableRow
stpInfoTableEntry=_StpInfoTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,3,2,1,1))
stpInfoTableEntry.setIndexNames((0,_G,_y))
if mibBuilder.loadTexts:stpInfoTableEntry.setStatus(_A)
_StpInfoIndex_Type=Integer32
_StpInfoIndex_Object=MibTableColumn
stpInfoIndex=_StpInfoIndex_Object((1,3,6,1,4,1,1872,2,5,2,3,2,1,1,1),_StpInfoIndex_Type())
stpInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoIndex.setStatus(_A)
_StpInfoTimeSinceTopChange_Type=TimeTicks
_StpInfoTimeSinceTopChange_Object=MibTableColumn
stpInfoTimeSinceTopChange=_StpInfoTimeSinceTopChange_Object((1,3,6,1,4,1,1872,2,5,2,3,2,1,1,2),_StpInfoTimeSinceTopChange_Type())
stpInfoTimeSinceTopChange.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoTimeSinceTopChange.setStatus(_A)
_StpInfoTopChanges_Type=Counter32
_StpInfoTopChanges_Object=MibTableColumn
stpInfoTopChanges=_StpInfoTopChanges_Object((1,3,6,1,4,1,1872,2,5,2,3,2,1,1,3),_StpInfoTopChanges_Type())
stpInfoTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoTopChanges.setStatus(_A)
_StpInfoDesignatedRoot_Type=BridgeId
_StpInfoDesignatedRoot_Object=MibTableColumn
stpInfoDesignatedRoot=_StpInfoDesignatedRoot_Object((1,3,6,1,4,1,1872,2,5,2,3,2,1,1,4),_StpInfoDesignatedRoot_Type())
stpInfoDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoDesignatedRoot.setStatus(_A)
_StpInfoRootCost_Type=Integer32
_StpInfoRootCost_Object=MibTableColumn
stpInfoRootCost=_StpInfoRootCost_Object((1,3,6,1,4,1,1872,2,5,2,3,2,1,1,5),_StpInfoRootCost_Type())
stpInfoRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoRootCost.setStatus(_A)
_StpInfoRootPort_Type=Integer32
_StpInfoRootPort_Object=MibTableColumn
stpInfoRootPort=_StpInfoRootPort_Object((1,3,6,1,4,1,1872,2,5,2,3,2,1,1,6),_StpInfoRootPort_Type())
stpInfoRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoRootPort.setStatus(_A)
_StpInfoMaxAge_Type=Integer32
_StpInfoMaxAge_Object=MibTableColumn
stpInfoMaxAge=_StpInfoMaxAge_Object((1,3,6,1,4,1,1872,2,5,2,3,2,1,1,7),_StpInfoMaxAge_Type())
stpInfoMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoMaxAge.setStatus(_A)
_StpInfoHelloTime_Type=Integer32
_StpInfoHelloTime_Object=MibTableColumn
stpInfoHelloTime=_StpInfoHelloTime_Object((1,3,6,1,4,1,1872,2,5,2,3,2,1,1,8),_StpInfoHelloTime_Type())
stpInfoHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoHelloTime.setStatus(_A)
_StpInfoForwardDelay_Type=Integer32
_StpInfoForwardDelay_Object=MibTableColumn
stpInfoForwardDelay=_StpInfoForwardDelay_Object((1,3,6,1,4,1,1872,2,5,2,3,2,1,1,9),_StpInfoForwardDelay_Type())
stpInfoForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoForwardDelay.setStatus(_A)
_StpInfoHoldTime_Type=Integer32
_StpInfoHoldTime_Object=MibTableColumn
stpInfoHoldTime=_StpInfoHoldTime_Object((1,3,6,1,4,1,1872,2,5,2,3,2,1,1,10),_StpInfoHoldTime_Type())
stpInfoHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoHoldTime.setStatus(_A)
_StpInfoPortTable_Object=MibTable
stpInfoPortTable=_StpInfoPortTable_Object((1,3,6,1,4,1,1872,2,5,2,3,2,2))
if mibBuilder.loadTexts:stpInfoPortTable.setStatus(_A)
_StpInfoPortTableEntry_Object=MibTableRow
stpInfoPortTableEntry=_StpInfoPortTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,3,2,2,1))
stpInfoPortTableEntry.setIndexNames((0,_G,_z),(0,_G,_A0))
if mibBuilder.loadTexts:stpInfoPortTableEntry.setStatus(_A)
_StpInfoPortStpIndex_Type=Integer32
_StpInfoPortStpIndex_Object=MibTableColumn
stpInfoPortStpIndex=_StpInfoPortStpIndex_Object((1,3,6,1,4,1,1872,2,5,2,3,2,2,1,1),_StpInfoPortStpIndex_Type())
stpInfoPortStpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortStpIndex.setStatus(_A)
_StpInfoPortIndex_Type=Integer32
_StpInfoPortIndex_Object=MibTableColumn
stpInfoPortIndex=_StpInfoPortIndex_Object((1,3,6,1,4,1,1872,2,5,2,3,2,2,1,2),_StpInfoPortIndex_Type())
stpInfoPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortIndex.setStatus(_A)
class _StpInfoPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),('blocking',2),('listening',3),('learning',4),(_A1,5),('broken',6),(_A2,7)))
_StpInfoPortState_Type.__name__=_C
_StpInfoPortState_Object=MibTableColumn
stpInfoPortState=_StpInfoPortState_Object((1,3,6,1,4,1,1872,2,5,2,3,2,2,1,3),_StpInfoPortState_Type())
stpInfoPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortState.setStatus(_A)
_StpInfoPortDesignatedRoot_Type=BridgeId
_StpInfoPortDesignatedRoot_Object=MibTableColumn
stpInfoPortDesignatedRoot=_StpInfoPortDesignatedRoot_Object((1,3,6,1,4,1,1872,2,5,2,3,2,2,1,4),_StpInfoPortDesignatedRoot_Type())
stpInfoPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortDesignatedRoot.setStatus(_A)
_StpInfoPortDesignatedCost_Type=Integer32
_StpInfoPortDesignatedCost_Object=MibTableColumn
stpInfoPortDesignatedCost=_StpInfoPortDesignatedCost_Object((1,3,6,1,4,1,1872,2,5,2,3,2,2,1,5),_StpInfoPortDesignatedCost_Type())
stpInfoPortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortDesignatedCost.setStatus(_A)
_StpInfoPortDesignatedBridge_Type=BridgeId
_StpInfoPortDesignatedBridge_Object=MibTableColumn
stpInfoPortDesignatedBridge=_StpInfoPortDesignatedBridge_Object((1,3,6,1,4,1,1872,2,5,2,3,2,2,1,6),_StpInfoPortDesignatedBridge_Type())
stpInfoPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortDesignatedBridge.setStatus(_A)
class _StpInfoPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_StpInfoPortDesignatedPort_Type.__name__=_O
_StpInfoPortDesignatedPort_Object=MibTableColumn
stpInfoPortDesignatedPort=_StpInfoPortDesignatedPort_Object((1,3,6,1,4,1,1872,2,5,2,3,2,2,1,7),_StpInfoPortDesignatedPort_Type())
stpInfoPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortDesignatedPort.setStatus(_A)
_StpInfoPortForwardTransitions_Type=Counter32
_StpInfoPortForwardTransitions_Object=MibTableColumn
stpInfoPortForwardTransitions=_StpInfoPortForwardTransitions_Object((1,3,6,1,4,1,1872,2,5,2,3,2,2,1,8),_StpInfoPortForwardTransitions_Type())
stpInfoPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortForwardTransitions.setStatus(_A)
_StpInfoPortPathCost_Type=Integer32
_StpInfoPortPathCost_Object=MibTableColumn
stpInfoPortPathCost=_StpInfoPortPathCost_Object((1,3,6,1,4,1,1872,2,5,2,3,2,2,1,9),_StpInfoPortPathCost_Type())
stpInfoPortPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortPathCost.setStatus(_A)
class _StpInfoPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_A3,2),('backup',3),('root',4),(_A4,5),('master',6),(_Q,7)))
_StpInfoPortRole_Type.__name__=_C
_StpInfoPortRole_Object=MibTableColumn
stpInfoPortRole=_StpInfoPortRole_Object((1,3,6,1,4,1,1872,2,5,2,3,2,2,1,10),_StpInfoPortRole_Type())
stpInfoPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortRole.setStatus(_A)
class _StpInfoPortLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_Q,3)))
_StpInfoPortLinkType_Type.__name__=_C
_StpInfoPortLinkType_Object=MibTableColumn
stpInfoPortLinkType=_StpInfoPortLinkType_Object((1,3,6,1,4,1,1872,2,5,2,3,2,2,1,11),_StpInfoPortLinkType_Type())
stpInfoPortLinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortLinkType.setStatus(_A)
class _StpInfoPortEdge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_StpInfoPortEdge_Type.__name__=_C
_StpInfoPortEdge_Object=MibTableColumn
stpInfoPortEdge=_StpInfoPortEdge_Object((1,3,6,1,4,1,1872,2,5,2,3,2,2,1,12),_StpInfoPortEdge_Type())
stpInfoPortEdge.setMaxAccess(_B)
if mibBuilder.loadTexts:stpInfoPortEdge.setStatus(_A)
_LacpInfo_ObjectIdentity=ObjectIdentity
lacpInfo=_LacpInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,3,3))
_LacpInfoPortTable_Object=MibTable
lacpInfoPortTable=_LacpInfoPortTable_Object((1,3,6,1,4,1,1872,2,5,2,3,3,1))
if mibBuilder.loadTexts:lacpInfoPortTable.setStatus(_A)
_LacpInfoPortTableEntry_Object=MibTableRow
lacpInfoPortTableEntry=_LacpInfoPortTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,3,3,1,1))
lacpInfoPortTableEntry.setIndexNames((0,_G,_A5))
if mibBuilder.loadTexts:lacpInfoPortTableEntry.setStatus(_A)
_LacpInfoPortIndex_Type=Integer32
_LacpInfoPortIndex_Object=MibTableColumn
lacpInfoPortIndex=_LacpInfoPortIndex_Object((1,3,6,1,4,1,1872,2,5,2,3,3,1,1,1),_LacpInfoPortIndex_Type())
lacpInfoPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpInfoPortIndex.setStatus(_A)
class _LacpInfoPortSelected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('selected',1),('unselected',2),('standby',3)))
_LacpInfoPortSelected_Type.__name__=_C
_LacpInfoPortSelected_Object=MibTableColumn
lacpInfoPortSelected=_LacpInfoPortSelected_Object((1,3,6,1,4,1,1872,2,5,2,3,3,1,1,2),_LacpInfoPortSelected_Type())
lacpInfoPortSelected.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpInfoPortSelected.setStatus(_A)
class _LacpInfoPortNtt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_LacpInfoPortNtt_Type.__name__=_C
_LacpInfoPortNtt_Object=MibTableColumn
lacpInfoPortNtt=_LacpInfoPortNtt_Object((1,3,6,1,4,1,1872,2,5,2,3,3,1,1,3),_LacpInfoPortNtt_Type())
lacpInfoPortNtt.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpInfoPortNtt.setStatus(_A)
class _LacpInfoPortReadyN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_LacpInfoPortReadyN_Type.__name__=_C
_LacpInfoPortReadyN_Object=MibTableColumn
lacpInfoPortReadyN=_LacpInfoPortReadyN_Object((1,3,6,1,4,1,1872,2,5,2,3,3,1,1,4),_LacpInfoPortReadyN_Type())
lacpInfoPortReadyN.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpInfoPortReadyN.setStatus(_A)
class _LacpInfoPortMoved_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_LacpInfoPortMoved_Type.__name__=_C
_LacpInfoPortMoved_Object=MibTableColumn
lacpInfoPortMoved=_LacpInfoPortMoved_Object((1,3,6,1,4,1,1872,2,5,2,3,3,1,1,5),_LacpInfoPortMoved_Type())
lacpInfoPortMoved.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpInfoPortMoved.setStatus(_A)
_CistInfo_ObjectIdentity=ObjectIdentity
cistInfo=_CistInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,3,4))
_CistGeneralInfo_ObjectIdentity=ObjectIdentity
cistGeneralInfo=_CistGeneralInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,3,4,1))
_CistRoot_Type=BridgeId
_CistRoot_Object=MibScalar
cistRoot=_CistRoot_Object((1,3,6,1,4,1,1872,2,5,2,3,4,1,1),_CistRoot_Type())
cistRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:cistRoot.setStatus(_A)
_CistRootPathCost_Type=Integer32
_CistRootPathCost_Object=MibScalar
cistRootPathCost=_CistRootPathCost_Object((1,3,6,1,4,1,1872,2,5,2,3,4,1,2),_CistRootPathCost_Type())
cistRootPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:cistRootPathCost.setStatus(_A)
_CistRootPort_Type=Integer32
_CistRootPort_Object=MibScalar
cistRootPort=_CistRootPort_Object((1,3,6,1,4,1,1872,2,5,2,3,4,1,3),_CistRootPort_Type())
cistRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cistRootPort.setStatus(_A)
_CistBridgeHelloTime_Type=Integer32
_CistBridgeHelloTime_Object=MibScalar
cistBridgeHelloTime=_CistBridgeHelloTime_Object((1,3,6,1,4,1,1872,2,5,2,3,4,1,4),_CistBridgeHelloTime_Type())
cistBridgeHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cistBridgeHelloTime.setStatus(_A)
_CistBridgeMaxAge_Type=Integer32
_CistBridgeMaxAge_Object=MibScalar
cistBridgeMaxAge=_CistBridgeMaxAge_Object((1,3,6,1,4,1,1872,2,5,2,3,4,1,5),_CistBridgeMaxAge_Type())
cistBridgeMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:cistBridgeMaxAge.setStatus(_A)
_CistBridgeForwardDelay_Type=Integer32
_CistBridgeForwardDelay_Object=MibScalar
cistBridgeForwardDelay=_CistBridgeForwardDelay_Object((1,3,6,1,4,1,1872,2,5,2,3,4,1,6),_CistBridgeForwardDelay_Type())
cistBridgeForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:cistBridgeForwardDelay.setStatus(_A)
_CistRegionalRoot_Type=BridgeId
_CistRegionalRoot_Object=MibScalar
cistRegionalRoot=_CistRegionalRoot_Object((1,3,6,1,4,1,1872,2,5,2,3,4,1,7),_CistRegionalRoot_Type())
cistRegionalRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:cistRegionalRoot.setStatus(_A)
_CistRegionalPathCost_Type=Integer32
_CistRegionalPathCost_Object=MibScalar
cistRegionalPathCost=_CistRegionalPathCost_Object((1,3,6,1,4,1,1872,2,5,2,3,4,1,8),_CistRegionalPathCost_Type())
cistRegionalPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:cistRegionalPathCost.setStatus(_A)
_CistInfoPortTable_Object=MibTable
cistInfoPortTable=_CistInfoPortTable_Object((1,3,6,1,4,1,1872,2,5,2,3,4,2))
if mibBuilder.loadTexts:cistInfoPortTable.setStatus(_A)
_CistInfoPortTableEntry_Object=MibTableRow
cistInfoPortTableEntry=_CistInfoPortTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,3,4,2,1))
cistInfoPortTableEntry.setIndexNames((0,_G,_A6))
if mibBuilder.loadTexts:cistInfoPortTableEntry.setStatus(_A)
_CistInfoPortIndex_Type=Integer32
_CistInfoPortIndex_Object=MibTableColumn
cistInfoPortIndex=_CistInfoPortIndex_Object((1,3,6,1,4,1,1872,2,5,2,3,4,2,1,1),_CistInfoPortIndex_Type())
cistInfoPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortIndex.setStatus(_A)
_CistInfoPortPriority_Type=Integer32
_CistInfoPortPriority_Object=MibTableColumn
cistInfoPortPriority=_CistInfoPortPriority_Object((1,3,6,1,4,1,1872,2,5,2,3,4,2,1,2),_CistInfoPortPriority_Type())
cistInfoPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortPriority.setStatus(_A)
_CistInfoPortPathCost_Type=Integer32
_CistInfoPortPathCost_Object=MibTableColumn
cistInfoPortPathCost=_CistInfoPortPathCost_Object((1,3,6,1,4,1,1872,2,5,2,3,4,2,1,3),_CistInfoPortPathCost_Type())
cistInfoPortPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortPathCost.setStatus(_A)
class _CistInfoPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_E,1),(_A2,2),('learning',4),(_A1,5)))
_CistInfoPortState_Type.__name__=_C
_CistInfoPortState_Object=MibTableColumn
cistInfoPortState=_CistInfoPortState_Object((1,3,6,1,4,1,1872,2,5,2,3,4,2,1,4),_CistInfoPortState_Type())
cistInfoPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortState.setStatus(_A)
class _CistInfoPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_A3,2),('backup',3),('root',4),(_A4,5),('master',6),(_Q,7)))
_CistInfoPortRole_Type.__name__=_C
_CistInfoPortRole_Object=MibTableColumn
cistInfoPortRole=_CistInfoPortRole_Object((1,3,6,1,4,1,1872,2,5,2,3,4,2,1,5),_CistInfoPortRole_Type())
cistInfoPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortRole.setStatus(_A)
_CistInfoPortDesignatedBridge_Type=BridgeId
_CistInfoPortDesignatedBridge_Object=MibTableColumn
cistInfoPortDesignatedBridge=_CistInfoPortDesignatedBridge_Object((1,3,6,1,4,1,1872,2,5,2,3,4,2,1,6),_CistInfoPortDesignatedBridge_Type())
cistInfoPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortDesignatedBridge.setStatus(_A)
class _CistInfoPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_CistInfoPortDesignatedPort_Type.__name__=_O
_CistInfoPortDesignatedPort_Object=MibTableColumn
cistInfoPortDesignatedPort=_CistInfoPortDesignatedPort_Object((1,3,6,1,4,1,1872,2,5,2,3,4,2,1,7),_CistInfoPortDesignatedPort_Type())
cistInfoPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortDesignatedPort.setStatus(_A)
class _CistInfoPortLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_Q,3)))
_CistInfoPortLinkType_Type.__name__=_C
_CistInfoPortLinkType_Object=MibTableColumn
cistInfoPortLinkType=_CistInfoPortLinkType_Object((1,3,6,1,4,1,1872,2,5,2,3,4,2,1,8),_CistInfoPortLinkType_Type())
cistInfoPortLinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:cistInfoPortLinkType.setStatus(_A)
_VlanInfo_ObjectIdentity=ObjectIdentity
vlanInfo=_VlanInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,3,5))
_VlanInfoTable_Object=MibTable
vlanInfoTable=_VlanInfoTable_Object((1,3,6,1,4,1,1872,2,5,2,3,5,1))
if mibBuilder.loadTexts:vlanInfoTable.setStatus(_A)
_VlanInfoTableEntry_Object=MibTableRow
vlanInfoTableEntry=_VlanInfoTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,3,5,1,1))
vlanInfoTableEntry.setIndexNames((0,_G,_A7))
if mibBuilder.loadTexts:vlanInfoTableEntry.setStatus(_A)
class _VlanInfoId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4090))
_VlanInfoId_Type.__name__=_C
_VlanInfoId_Object=MibTableColumn
vlanInfoId=_VlanInfoId_Object((1,3,6,1,4,1,1872,2,5,2,3,5,1,1,1),_VlanInfoId_Type())
vlanInfoId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanInfoId.setStatus(_A)
class _VlanInfoName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VlanInfoName_Type.__name__=_I
_VlanInfoName_Object=MibTableColumn
vlanInfoName=_VlanInfoName_Object((1,3,6,1,4,1,1872,2,5,2,3,5,1,1,2),_VlanInfoName_Type())
vlanInfoName.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanInfoName.setStatus(_A)
class _VlanInfoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanInfoStatus_Type.__name__=_C
_VlanInfoStatus_Object=MibTableColumn
vlanInfoStatus=_VlanInfoStatus_Object((1,3,6,1,4,1,1872,2,5,2,3,5,1,1,3),_VlanInfoStatus_Type())
vlanInfoStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanInfoStatus.setStatus(_A)
class _VlanInfoJumbo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanInfoJumbo_Type.__name__=_C
_VlanInfoJumbo_Object=MibTableColumn
vlanInfoJumbo=_VlanInfoJumbo_Object((1,3,6,1,4,1,1872,2,5,2,3,5,1,1,4),_VlanInfoJumbo_Type())
vlanInfoJumbo.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanInfoJumbo.setStatus(_A)
_VlanInfoBwmContract_Type=Integer32
_VlanInfoBwmContract_Object=MibTableColumn
vlanInfoBwmContract=_VlanInfoBwmContract_Object((1,3,6,1,4,1,1872,2,5,2,3,5,1,1,5),_VlanInfoBwmContract_Type())
vlanInfoBwmContract.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanInfoBwmContract.setStatus(_A)
class _VlanInfoLearn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_VlanInfoLearn_Type.__name__=_C
_VlanInfoLearn_Object=MibTableColumn
vlanInfoLearn=_VlanInfoLearn_Object((1,3,6,1,4,1,1872,2,5,2,3,5,1,1,6),_VlanInfoLearn_Type())
vlanInfoLearn.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanInfoLearn.setStatus(_A)
_VlanInfoPorts_Type=OctetString
_VlanInfoPorts_Object=MibTableColumn
vlanInfoPorts=_VlanInfoPorts_Object((1,3,6,1,4,1,1872,2,5,2,3,5,1,1,7),_VlanInfoPorts_Type())
vlanInfoPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanInfoPorts.setStatus(_A)
_VlanInfoTableVADC_Object=MibTable
vlanInfoTableVADC=_VlanInfoTableVADC_Object((1,3,6,1,4,1,1872,2,5,2,3,5,2))
if mibBuilder.loadTexts:vlanInfoTableVADC.setStatus(_A)
_VlanInfoTableVADCEntry_Object=MibTableRow
vlanInfoTableVADCEntry=_VlanInfoTableVADCEntry_Object((1,3,6,1,4,1,1872,2,5,2,3,5,2,1))
vlanInfoTableVADCEntry.setIndexNames((0,_G,_A8))
if mibBuilder.loadTexts:vlanInfoTableVADCEntry.setStatus(_A)
class _VlanInfoIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4090))
_VlanInfoIdx_Type.__name__=_C
_VlanInfoIdx_Object=MibTableColumn
vlanInfoIdx=_VlanInfoIdx_Object((1,3,6,1,4,1,1872,2,5,2,3,5,2,1,1),_VlanInfoIdx_Type())
vlanInfoIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanInfoIdx.setStatus(_A)
class _VlanInfoVADC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VlanInfoVADC_Type.__name__=_I
_VlanInfoVADC_Object=MibTableColumn
vlanInfoVADC=_VlanInfoVADC_Object((1,3,6,1,4,1,1872,2,5,2,3,5,2,1,2),_VlanInfoVADC_Type())
vlanInfoVADC.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanInfoVADC.setStatus(_A)
_PortTeamInfo_ObjectIdentity=ObjectIdentity
portTeamInfo=_PortTeamInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,3,6))
_PortTeamInfoTable_Object=MibTable
portTeamInfoTable=_PortTeamInfoTable_Object((1,3,6,1,4,1,1872,2,5,2,3,6,1))
if mibBuilder.loadTexts:portTeamInfoTable.setStatus(_A)
_PortTeamInfoTableEntry_Object=MibTableRow
portTeamInfoTableEntry=_PortTeamInfoTableEntry_Object((1,3,6,1,4,1,1872,2,5,2,3,6,1,1))
portTeamInfoTableEntry.setIndexNames((0,_G,_A9))
if mibBuilder.loadTexts:portTeamInfoTableEntry.setStatus(_A)
_PortTeamInfoIndex_Type=Integer32
_PortTeamInfoIndex_Object=MibTableColumn
portTeamInfoIndex=_PortTeamInfoIndex_Object((1,3,6,1,4,1,1872,2,5,2,3,6,1,1,1),_PortTeamInfoIndex_Type())
portTeamInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portTeamInfoIndex.setStatus(_A)
class _PortTeamInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_W,2),(_V,3)))
_PortTeamInfoState_Type.__name__=_C
_PortTeamInfoState_Object=MibTableColumn
portTeamInfoState=_PortTeamInfoState_Object((1,3,6,1,4,1,1872,2,5,2,3,6,1,1,2),_PortTeamInfoState_Type())
portTeamInfoState.setMaxAccess(_B)
if mibBuilder.loadTexts:portTeamInfoState.setStatus(_A)
_PortTeamInfoPorts_Type=OctetString
_PortTeamInfoPorts_Object=MibTableColumn
portTeamInfoPorts=_PortTeamInfoPorts_Object((1,3,6,1,4,1,1872,2,5,2,3,6,1,1,3),_PortTeamInfoPorts_Type())
portTeamInfoPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:portTeamInfoPorts.setStatus(_A)
_PortTeamInfoPortsState_Type=OctetString
_PortTeamInfoPortsState_Object=MibTableColumn
portTeamInfoPortsState=_PortTeamInfoPortsState_Object((1,3,6,1,4,1,1872,2,5,2,3,6,1,1,4),_PortTeamInfoPortsState_Type())
portTeamInfoPortsState.setMaxAccess(_B)
if mibBuilder.loadTexts:portTeamInfoPortsState.setStatus(_A)
_PortTeamInfoTrunks_Type=OctetString
_PortTeamInfoTrunks_Object=MibTableColumn
portTeamInfoTrunks=_PortTeamInfoTrunks_Object((1,3,6,1,4,1,1872,2,5,2,3,6,1,1,5),_PortTeamInfoTrunks_Type())
portTeamInfoTrunks.setMaxAccess(_B)
if mibBuilder.loadTexts:portTeamInfoTrunks.setStatus(_A)
_PortTeamInfoTrunksState_Type=OctetString
_PortTeamInfoTrunksState_Object=MibTableColumn
portTeamInfoTrunksState=_PortTeamInfoTrunksState_Object((1,3,6,1,4,1,1872,2,5,2,3,6,1,1,6),_PortTeamInfoTrunksState_Type())
portTeamInfoTrunksState.setMaxAccess(_B)
if mibBuilder.loadTexts:portTeamInfoTrunksState.setStatus(_A)
_PortTeamInfoMaster_Type=DisplayString
_PortTeamInfoMaster_Object=MibTableColumn
portTeamInfoMaster=_PortTeamInfoMaster_Object((1,3,6,1,4,1,1872,2,5,2,3,6,1,1,7),_PortTeamInfoMaster_Type())
portTeamInfoMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:portTeamInfoMaster.setStatus(_A)
_Layer2Oper_ObjectIdentity=ObjectIdentity
layer2Oper=_Layer2Oper_ObjectIdentity((1,3,6,1,4,1,1872,2,5,2,4))
mibBuilder.exportSymbols(_G,**{'layer2':layer2,'layer2Configs':layer2Configs,'vlan':vlan,'vlanMaxEnt':vlanMaxEnt,'vlanCurCfgTable':vlanCurCfgTable,'vlanCurCfgTableEntry':vlanCurCfgTableEntry,_Z:vlanCurCfgVlanId,'vlanCurCfgVlanName':vlanCurCfgVlanName,'vlanCurCfgPorts':vlanCurCfgPorts,'vlanCurCfgState':vlanCurCfgState,'vlanCurCfgBwmContract':vlanCurCfgBwmContract,'vlanCurCfgStg':vlanCurCfgStg,'vlanCurCfgJumbo':vlanCurCfgJumbo,'vlanCurCfgLearn':vlanCurCfgLearn,'vlanCurCfgShared':vlanCurCfgShared,'vlanCurCfgIpv6LlaGen':vlanCurCfgIpv6LlaGen,'vlanCurCfgRouterAdv':vlanCurCfgRouterAdv,'vlanCurCfgReTransInt':vlanCurCfgReTransInt,'vlanCurCfgMinIntBwAdv':vlanCurCfgMinIntBwAdv,'vlanCurCfgMaxIntBwAdv':vlanCurCfgMaxIntBwAdv,'vlanCurCfgMtu':vlanCurCfgMtu,'vlanCurCfgCurHopLimit':vlanCurCfgCurHopLimit,'vlanCurCfgMFlag':vlanCurCfgMFlag,'vlanCurCfgOFlag':vlanCurCfgOFlag,'vlanCurCfgRTime':vlanCurCfgRTime,'vlanCurCfgRlTime':vlanCurCfgRlTime,'vlanCurCfgPlTime':vlanCurCfgPlTime,'vlanCurCfgVlTime':vlanCurCfgVlTime,'vlanCurCfgOpInfo':vlanCurCfgOpInfo,'vlanCurCfgApInfo':vlanCurCfgApInfo,'vlanNewCfgTable':vlanNewCfgTable,'vlanNewCfgTableEntry':vlanNewCfgTableEntry,_a:vlanNewCfgVlanId,'vlanNewCfgVlanName':vlanNewCfgVlanName,'vlanNewCfgPorts':vlanNewCfgPorts,'vlanNewCfgState':vlanNewCfgState,'vlanNewCfgAddPort':vlanNewCfgAddPort,'vlanNewCfgRemovePort':vlanNewCfgRemovePort,'vlanNewCfgDelete':vlanNewCfgDelete,'vlanNewCfgBwmContract':vlanNewCfgBwmContract,'vlanNewCfgStg':vlanNewCfgStg,'vlanNewCfgJumbo':vlanNewCfgJumbo,'vlanNewCfgLearn':vlanNewCfgLearn,'vlanNewCfgShared':vlanNewCfgShared,'vlanNewCfgIpv6LlaGen':vlanNewCfgIpv6LlaGen,'vlanNewCfgRouterAdv':vlanNewCfgRouterAdv,'vlanNewCfgReTransInt':vlanNewCfgReTransInt,'vlanNewCfgMinIntBwAdv':vlanNewCfgMinIntBwAdv,'vlanNewCfgMaxIntBwAdv':vlanNewCfgMaxIntBwAdv,'vlanNewCfgMtu':vlanNewCfgMtu,'vlanNewCfgCurHopLimit':vlanNewCfgCurHopLimit,'vlanNewCfgMFlag':vlanNewCfgMFlag,'vlanNewCfgOFlag':vlanNewCfgOFlag,'vlanNewCfgRTime':vlanNewCfgRTime,'vlanNewCfgRlTime':vlanNewCfgRlTime,'vlanNewCfgPlTime':vlanNewCfgPlTime,'vlanNewCfgVlTime':vlanNewCfgVlTime,'vlanNewCfgOpInfo':vlanNewCfgOpInfo,'vlanNewCfgApInfo':vlanNewCfgApInfo,'vlanMaxVlanID':vlanMaxVlanID,'trunkgroup':trunkgroup,'trunkGroupTableMaxSize':trunkGroupTableMaxSize,'trunkGroupCurCfgTable':trunkGroupCurCfgTable,'trunkGroupCurCfgTableEntry':trunkGroupCurCfgTableEntry,_b:trunkGroupCurCfgIndex,'trunkGroupCurCfgPorts':trunkGroupCurCfgPorts,'trunkGroupCurCfgState':trunkGroupCurCfgState,'trunkGroupCurCfgBwmContract':trunkGroupCurCfgBwmContract,'trunkGroupCurCfgName':trunkGroupCurCfgName,'trunkGroupNewCfgTable':trunkGroupNewCfgTable,'trunkGroupNewCfgTableEntry':trunkGroupNewCfgTableEntry,_c:trunkGroupNewCfgIndex,'trunkGroupNewCfgPorts':trunkGroupNewCfgPorts,'trunkGroupNewCfgAddPort':trunkGroupNewCfgAddPort,'trunkGroupNewCfgRemovePort':trunkGroupNewCfgRemovePort,'trunkGroupNewCfgState':trunkGroupNewCfgState,'trunkGroupNewCfgDelete':trunkGroupNewCfgDelete,'trunkGroupNewCfgBwmContract':trunkGroupNewCfgBwmContract,'trunkGroupNewCfgName':trunkGroupNewCfgName,'stgCfg':stgCfg,'stgCurCfgTable':stgCurCfgTable,'stgCurCfgTableEntry':stgCurCfgTableEntry,_d:stgCurCfgIndex,'stgCurCfgState':stgCurCfgState,'stgCurCfgPriority':stgCurCfgPriority,'stgCurCfgBrgHelloTime':stgCurCfgBrgHelloTime,'stgCurCfgBrgForwardDelay':stgCurCfgBrgForwardDelay,'stgCurCfgBrgMaxAge':stgCurCfgBrgMaxAge,'stgCurCfgAgingTime':stgCurCfgAgingTime,'stgCurCfgVlanBmap':stgCurCfgVlanBmap,'stgNewCfgTable':stgNewCfgTable,'stgNewCfgTableEntry':stgNewCfgTableEntry,_e:stgNewCfgIndex,'stgNewCfgState':stgNewCfgState,'stgNewCfgDefaultCfg':stgNewCfgDefaultCfg,'stgNewCfgAddVlan':stgNewCfgAddVlan,'stgNewCfgRemoveVlan':stgNewCfgRemoveVlan,'stgNewCfgPriority':stgNewCfgPriority,'stgNewCfgBrgHelloTime':stgNewCfgBrgHelloTime,'stgNewCfgBrgForwardDelay':stgNewCfgBrgForwardDelay,'stgNewCfgBrgMaxAge':stgNewCfgBrgMaxAge,'stgNewCfgAgingTime':stgNewCfgAgingTime,'stgNewCfgVlanBmap':stgNewCfgVlanBmap,'stgCurCfgPortTable':stgCurCfgPortTable,'stgCurCfgPortTableEntry':stgCurCfgPortTableEntry,_f:stgCurCfgStgIndex,_g:stgCurCfgPortIndex,'stgCurCfgPortState':stgCurCfgPortState,'stgCurCfgPortPriority':stgCurCfgPortPriority,'stgCurCfgPortPathCost':stgCurCfgPortPathCost,'stgCurCfgPortLink':stgCurCfgPortLink,'stgCurCfgPortEdge':stgCurCfgPortEdge,'stgNewCfgPortTable':stgNewCfgPortTable,'stgNewCfgPortTableEntry':stgNewCfgPortTableEntry,_h:stgNewCfgStgIndex,_i:stgNewCfgPortIndex,'stgNewCfgPortState':stgNewCfgPortState,'stgNewCfgPortPriority':stgNewCfgPortPriority,'stgNewCfgPortPathCost':stgNewCfgPortPathCost,'stgNewCfgPortLink':stgNewCfgPortLink,'stgNewCfgPortEdge':stgNewCfgPortEdge,'mirroring':mirroring,'mirrPortMirr':mirrPortMirr,'pmCurCfgPortMirrState':pmCurCfgPortMirrState,'pmNewCfgPortMirrState':pmNewCfgPortMirrState,'pmCurCfgPortMonitorTable':pmCurCfgPortMonitorTable,'pmCurCfgPortMonitorEntry':pmCurCfgPortMonitorEntry,_j:pmCurCfgPmirrMoniPortIndex,_k:pmCurCfgPmirrMirrPortIndex,'pmCurCfgPmirrDirection':pmCurCfgPmirrDirection,'pmCurCfgPmirrPortVlansBmap':pmCurCfgPmirrPortVlansBmap,'pmNewCfgPortMonitorTable':pmNewCfgPortMonitorTable,'pmNewCfgPortMonitorEntry':pmNewCfgPortMonitorEntry,_l:pmNewCfgPmirrMoniPortIndex,_m:pmNewCfgPmirrMirrPortIndex,'pmNewCfgPmirrDirection':pmNewCfgPmirrDirection,'pmNewCfgPmirrDelete':pmNewCfgPmirrDelete,'pmNewCfgAddVlan':pmNewCfgAddVlan,'pmNewCfgRemoveVlan':pmNewCfgRemoveVlan,'pmNewCfgPmirrPortVlansBmap':pmNewCfgPmirrPortVlansBmap,'lacp':lacp,'lacpCurSystemPriority':lacpCurSystemPriority,'lacpNewSystemPriority':lacpNewSystemPriority,'lacpCurSystemTimeoutTime':lacpCurSystemTimeoutTime,'lacpNewSystemTimeoutTime':lacpNewSystemTimeoutTime,'lacpCurPortCfgTable':lacpCurPortCfgTable,'lacpCurPortCfgTableEntry':lacpCurPortCfgTableEntry,_n:lacpCurPortCfgTableId,'lacpCurPortState':lacpCurPortState,'lacpCurPortActorPortPriority':lacpCurPortActorPortPriority,'lacpCurPortActorAdminKey':lacpCurPortActorAdminKey,'lacpNewPortCfgTable':lacpNewPortCfgTable,'lacpNewPortCfgTableEntry':lacpNewPortCfgTableEntry,_o:lacpNewPortCfgTableId,'lacpNewPortState':lacpNewPortState,'lacpNewPortActorPortPriority':lacpNewPortActorPortPriority,'lacpNewPortActorAdminKey':lacpNewPortActorAdminKey,'lacpCurSystemName':lacpCurSystemName,'lacpNewSystemName':lacpNewSystemName,'mstCfg':mstCfg,'mstGeneralCfg':mstGeneralCfg,'mstCurCfgState':mstCurCfgState,'mstNewCfgState':mstNewCfgState,'mstCurCfgRegionName':mstCurCfgRegionName,'mstNewCfgRegionName':mstNewCfgRegionName,'mstCurCfgRegionVersion':mstCurCfgRegionVersion,'mstNewCfgRegionVersion':mstNewCfgRegionVersion,'mstCurCfgMaxHopCount':mstCurCfgMaxHopCount,'mstNewCfgMaxHopCount':mstNewCfgMaxHopCount,'mstCurCfgStpMode':mstCurCfgStpMode,'mstNewCfgStpMode':mstNewCfgStpMode,'mstCistCfg':mstCistCfg,'mstCistDefaultCfg':mstCistDefaultCfg,'mstCistBridgeCfg':mstCistBridgeCfg,'mstCistCurCfgBridgePriority':mstCistCurCfgBridgePriority,'mstCistNewCfgBridgePriority':mstCistNewCfgBridgePriority,'mstCistCurCfgBridgeMaxAge':mstCistCurCfgBridgeMaxAge,'mstCistNewCfgBridgeMaxAge':mstCistNewCfgBridgeMaxAge,'mstCistCurCfgBridgeForwardDelay':mstCistCurCfgBridgeForwardDelay,'mstCistNewCfgBridgeForwardDelay':mstCistNewCfgBridgeForwardDelay,'mstCistCurCfgPortTable':mstCistCurCfgPortTable,'mstCistCurCfgPortTableEntry':mstCistCurCfgPortTableEntry,_p:mstCistCurCfgPortIndex,'mstCistCurCfgPortPriority':mstCistCurCfgPortPriority,'mstCistCurCfgPortPathCost':mstCistCurCfgPortPathCost,'mstCistCurCfgPortLinkType':mstCistCurCfgPortLinkType,'mstCistCurCfgPortEdge':mstCistCurCfgPortEdge,'mstCistCurCfgPortStpState':mstCistCurCfgPortStpState,'mstCistCurCfgPortHelloTime':mstCistCurCfgPortHelloTime,'mstCistNewCfgPortTable':mstCistNewCfgPortTable,'mstCistNewCfgPortTableEntry':mstCistNewCfgPortTableEntry,_q:mstCistNewCfgPortIndex,'mstCistNewCfgPortPriority':mstCistNewCfgPortPriority,'mstCistNewCfgPortPathCost':mstCistNewCfgPortPathCost,'mstCistNewCfgPortLinkType':mstCistNewCfgPortLinkType,'mstCistNewCfgPortEdge':mstCistNewCfgPortEdge,'mstCistNewCfgPortStpState':mstCistNewCfgPortStpState,'mstCistNewCfgPortHelloTime':mstCistNewCfgPortHelloTime,'portTeamCfg':portTeamCfg,'portTeamTableMaxSize':portTeamTableMaxSize,'portTeamCurCfgTable':portTeamCurCfgTable,'portTeamCurCfgTableEntry':portTeamCurCfgTableEntry,_r:portTeamCurCfgIndex,'portTeamCurCfgState':portTeamCurCfgState,'portTeamCurCfgPorts':portTeamCurCfgPorts,'portTeamCurCfgTrunks':portTeamCurCfgTrunks,'portTeamCurCfgName':portTeamCurCfgName,'portTeamNewCfgTable':portTeamNewCfgTable,'portTeamNewCfgTableEntry':portTeamNewCfgTableEntry,_s:portTeamNewCfgIndex,'portTeamNewCfgState':portTeamNewCfgState,'portTeamNewCfgPorts':portTeamNewCfgPorts,'portTeamNewCfgAddPort':portTeamNewCfgAddPort,'portTeamNewCfgRemovePort':portTeamNewCfgRemovePort,'portTeamNewCfgTrunks':portTeamNewCfgTrunks,'portTeamNewCfgAddTrunk':portTeamNewCfgAddTrunk,'portTeamNewCfgRemoveTrunk':portTeamNewCfgRemoveTrunk,'portTeamNewCfgDelete':portTeamNewCfgDelete,'portTeamNewCfgName':portTeamNewCfgName,'vadcVlan':vadcVlan,'vadcVlanCurCfgTable':vadcVlanCurCfgTable,'vadcVlanCurCfgTableEntry':vadcVlanCurCfgTableEntry,_t:vadcVlanCurCfgVlanId,'vadcVlanCurCfgBwmCont':vadcVlanCurCfgBwmCont,'vadcVlanCurCfgNonIp':vadcVlanCurCfgNonIp,'vadcVlanCurCfgIpv6LlaGen':vadcVlanCurCfgIpv6LlaGen,'vadcVlanCurCfgRouterAdv':vadcVlanCurCfgRouterAdv,'vadcVlanCurCfgReTransInt':vadcVlanCurCfgReTransInt,'vadcVlanCurCfgMinIntBwAdv':vadcVlanCurCfgMinIntBwAdv,'vadcVlanCurCfgMaxIntBwAdv':vadcVlanCurCfgMaxIntBwAdv,'vadcVlanCurCfgMtu':vadcVlanCurCfgMtu,'vadcVlanCurCfgCurHopLimit':vadcVlanCurCfgCurHopLimit,'vadcVlanCurCfgMFlag':vadcVlanCurCfgMFlag,'vadcVlanCurCfgOFlag':vadcVlanCurCfgOFlag,'vadcVlanCurCfgRTime':vadcVlanCurCfgRTime,'vadcVlanCurCfgRlTime':vadcVlanCurCfgRlTime,'vadcVlanCurCfgPlTime':vadcVlanCurCfgPlTime,'vadcVlanCurCfgVlTime':vadcVlanCurCfgVlTime,'vadcVlanCurCfgOpInfo':vadcVlanCurCfgOpInfo,'vadcVlanCurCfgApInfo':vadcVlanCurCfgApInfo,'vadcVlanNewCfgTable':vadcVlanNewCfgTable,'vadcVlanNewCfgTableEntry':vadcVlanNewCfgTableEntry,_u:vadcVlanNewCfgVlanId,'vadcVlanNewCfgBwmCont':vadcVlanNewCfgBwmCont,'vadcVlanNewCfgNonIp':vadcVlanNewCfgNonIp,'vadcVlanNewCfgIpv6LlaGen':vadcVlanNewCfgIpv6LlaGen,'vadcVlanNewCfgRouterAdv':vadcVlanNewCfgRouterAdv,'vadcVlanNewCfgReTransInt':vadcVlanNewCfgReTransInt,'vadcVlanNewCfgMinIntBwAdv':vadcVlanNewCfgMinIntBwAdv,'vadcVlanNewCfgMaxIntBwAdv':vadcVlanNewCfgMaxIntBwAdv,'vadcVlanNewCfgMtu':vadcVlanNewCfgMtu,'vadcVlanNewCfgCurHopLimit':vadcVlanNewCfgCurHopLimit,'vadcVlanNewCfgMFlag':vadcVlanNewCfgMFlag,'vadcVlanNewCfgOFlag':vadcVlanNewCfgOFlag,'vadcVlanNewCfgRTime':vadcVlanNewCfgRTime,'vadcVlanNewCfgRlTime':vadcVlanNewCfgRlTime,'vadcVlanNewCfgPlTime':vadcVlanNewCfgPlTime,'vadcVlanNewCfgVlTime':vadcVlanNewCfgVlTime,'vadcVlanNewCfgOpInfo':vadcVlanNewCfgOpInfo,'vadcVlanNewCfgApInfo':vadcVlanNewCfgApInfo,'layer2Stats':layer2Stats,'fdbStats':fdbStats,'fdbStatsCreates':fdbStatsCreates,'fdbStatsDeletes':fdbStatsDeletes,'fdbStatsCurrent':fdbStatsCurrent,'fdbStatsHiwat':fdbStatsHiwat,'fdbStatsLookups':fdbStatsLookups,'fdbStatsLookupFails':fdbStatsLookupFails,'fdbStatsFinds':fdbStatsFinds,'fdbStatsFindFails':fdbStatsFindFails,'fdbStatsFindOrCreates':fdbStatsFindOrCreates,'fdbStatsOverflows':fdbStatsOverflows,'stpStats':stpStats,'stgStatsPortTable':stgStatsPortTable,'stgStatsPortTableEntry':stgStatsPortTableEntry,_v:stgStatsStpIndex,_w:stgStatsPortIndex,'stgStatsPortRcvCfgBpdus':stgStatsPortRcvCfgBpdus,'stgStatsPortRcvTcnBpdus':stgStatsPortRcvTcnBpdus,'stgStatsPortXmtCfgBpdus':stgStatsPortXmtCfgBpdus,'stgStatsPortXmtTcnBpdus':stgStatsPortXmtTcnBpdus,'layer2Info':layer2Info,'fdbInfo':fdbInfo,'fdbClear':fdbClear,'fdbTable':fdbTable,'fdbEntry':fdbEntry,_x:fdbMacAddr,'fdbVlan':fdbVlan,'fdbSrcPort':fdbSrcPort,'fdbState':fdbState,'fdbRefSps':fdbRefSps,'fdbLearnedPort':fdbLearnedPort,'fdbSrcTrunk':fdbSrcTrunk,'stpInfo':stpInfo,'stpInfoTable':stpInfoTable,'stpInfoTableEntry':stpInfoTableEntry,_y:stpInfoIndex,'stpInfoTimeSinceTopChange':stpInfoTimeSinceTopChange,'stpInfoTopChanges':stpInfoTopChanges,'stpInfoDesignatedRoot':stpInfoDesignatedRoot,'stpInfoRootCost':stpInfoRootCost,'stpInfoRootPort':stpInfoRootPort,'stpInfoMaxAge':stpInfoMaxAge,'stpInfoHelloTime':stpInfoHelloTime,'stpInfoForwardDelay':stpInfoForwardDelay,'stpInfoHoldTime':stpInfoHoldTime,'stpInfoPortTable':stpInfoPortTable,'stpInfoPortTableEntry':stpInfoPortTableEntry,_z:stpInfoPortStpIndex,_A0:stpInfoPortIndex,'stpInfoPortState':stpInfoPortState,'stpInfoPortDesignatedRoot':stpInfoPortDesignatedRoot,'stpInfoPortDesignatedCost':stpInfoPortDesignatedCost,'stpInfoPortDesignatedBridge':stpInfoPortDesignatedBridge,'stpInfoPortDesignatedPort':stpInfoPortDesignatedPort,'stpInfoPortForwardTransitions':stpInfoPortForwardTransitions,'stpInfoPortPathCost':stpInfoPortPathCost,'stpInfoPortRole':stpInfoPortRole,'stpInfoPortLinkType':stpInfoPortLinkType,'stpInfoPortEdge':stpInfoPortEdge,'lacpInfo':lacpInfo,'lacpInfoPortTable':lacpInfoPortTable,'lacpInfoPortTableEntry':lacpInfoPortTableEntry,_A5:lacpInfoPortIndex,'lacpInfoPortSelected':lacpInfoPortSelected,'lacpInfoPortNtt':lacpInfoPortNtt,'lacpInfoPortReadyN':lacpInfoPortReadyN,'lacpInfoPortMoved':lacpInfoPortMoved,'cistInfo':cistInfo,'cistGeneralInfo':cistGeneralInfo,'cistRoot':cistRoot,'cistRootPathCost':cistRootPathCost,'cistRootPort':cistRootPort,'cistBridgeHelloTime':cistBridgeHelloTime,'cistBridgeMaxAge':cistBridgeMaxAge,'cistBridgeForwardDelay':cistBridgeForwardDelay,'cistRegionalRoot':cistRegionalRoot,'cistRegionalPathCost':cistRegionalPathCost,'cistInfoPortTable':cistInfoPortTable,'cistInfoPortTableEntry':cistInfoPortTableEntry,_A6:cistInfoPortIndex,'cistInfoPortPriority':cistInfoPortPriority,'cistInfoPortPathCost':cistInfoPortPathCost,'cistInfoPortState':cistInfoPortState,'cistInfoPortRole':cistInfoPortRole,'cistInfoPortDesignatedBridge':cistInfoPortDesignatedBridge,'cistInfoPortDesignatedPort':cistInfoPortDesignatedPort,'cistInfoPortLinkType':cistInfoPortLinkType,'vlanInfo':vlanInfo,'vlanInfoTable':vlanInfoTable,'vlanInfoTableEntry':vlanInfoTableEntry,_A7:vlanInfoId,'vlanInfoName':vlanInfoName,'vlanInfoStatus':vlanInfoStatus,'vlanInfoJumbo':vlanInfoJumbo,'vlanInfoBwmContract':vlanInfoBwmContract,'vlanInfoLearn':vlanInfoLearn,'vlanInfoPorts':vlanInfoPorts,'vlanInfoTableVADC':vlanInfoTableVADC,'vlanInfoTableVADCEntry':vlanInfoTableVADCEntry,_A8:vlanInfoIdx,'vlanInfoVADC':vlanInfoVADC,'portTeamInfo':portTeamInfo,'portTeamInfoTable':portTeamInfoTable,'portTeamInfoTableEntry':portTeamInfoTableEntry,_A9:portTeamInfoIndex,'portTeamInfoState':portTeamInfoState,'portTeamInfoPorts':portTeamInfoPorts,'portTeamInfoPortsState':portTeamInfoPortsState,'portTeamInfoTrunks':portTeamInfoTrunks,'portTeamInfoTrunksState':portTeamInfoTrunksState,'portTeamInfoMaster':portTeamInfoMaster,'layer2Oper':layer2Oper})