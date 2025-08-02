_Ak='iwBrBlackListTime'
_Aj='iwBrBlackListSrcMac'
_Ai='iwBrListValues'
_Ah='iwBrListName'
_Ag='iwBrListType'
_Af='iwBrRuleProtoList'
_Ae='iwBrRuleDstList'
_Ad='iwBrRuleSrcList'
_Ac='iwBrRuleIfaceList'
_Ab='iwBrRuleVlanList'
_Aa='iwBrRuleMatchList'
_AZ='iwBrRuleAction'
_AY='iwBrGrpPermittedVLAN'
_AX='iwBrGrpXVlan'
_AW='iwBrGrpDefaultAction'
_AV='iwBrPortStpPVer'
_AU='iwBrGrpStpRootPort'
_AT='iwBrGrpStpRoot'
_AS='iwBrGrpDropSDPS'
_AR='iwBrGrpDropJOIN'
_AQ='iwBrGrpDropLCNA'
_AP='iwBrGrpDropNOBG'
_AO='iwBrGrpDropLOOP'
_AN='iwBrGrpDropFWRL'
_AM='iwBrGrpDropUNRD'
_AL='iwBrGrpDropSTPL'
_AK='iwBrGrpFlooded'
_AJ='iwBrGrpForwarded'
_AI='iwBrGrpInfo'
_AH='iwBrGrpFlgOper'
_AG='iwBrGrpFlgAct'
_AF='iwBrGrpFlgAdmin'
_AE='iwBrGrpFlgRptr'
_AD='iwBrGrpFlgIGMP'
_AC='iwBrGrpFlgSTP'
_AB='iwBrGrpUncoupled'
_AA='iwBrGrpInTrunk'
_A9='iwBrGrpDsChan'
_A8='iwBrGrpUsChan'
_A7='iwBrGrpType'
_A6='iwBrDbGroupOrder'
_A5='iwBrDbTrunkVLANId'
_A4='iwBrDbDead'
_A3='iwBrDbUseCnt'
_A2='iwBrDbCost'
_A1='iwBrDbGwType'
_A0='iwBrDbGwMac'
_z='iwBrDbStatus'
_y='iwBrDbPort'
_x='iwBrDbAgingTime'
_w='iwBrDbEntryDiscards'
_v='iwBrPortVlanAlteration'
_u='iwBrPortStpPathCost32'
_t='iwBrPortStpFwdTransitions'
_s='iwBrPortStpDesPort'
_r='iwBrPortStpDesBridge'
_q='iwBrPortStpDesCost'
_p='iwBrPortStpRole'
_o='iwBrPortStpState'
_n='iwBrPortStpPrio'
_m='iwBrStpBridgeForwardDelay'
_l='iwBrStpBridgeHelloTime'
_k='iwBrStpBridgeMaxAge'
_j='iwBrStpForwardDelay'
_i='iwBrStpHoldTime'
_h='iwBrStpHelloTime'
_g='iwBrStpMaxAge'
_f='iwBrStpTopChanges'
_e='iwBrStpTimeSinceTopoChange'
_d='iwBrStpPriority'
_c='iwBrStpProtoSpec'
_b='iwBrLocalTag'
_a='iwBrBaseType'
_Z='iwBrBasePorts'
_Y='iwBrBaseAddress'
_X='permit'
_W='normal'
_V='disabled'
_U='Unsigned32'
_T='iwBrBlackListDstMac'
_S='iwBrBlackListGrpId'
_R='iwBrListId'
_Q='iwBrRulePriority'
_P='iwBrRuleGrpId'
_O='iwBrGrpId'
_N='iwBrDbAddress'
_M='iwBrDbGroupId'
_L='iwBrPortId'
_K='iwBrPortGrpId'
_J='unknown'
_I='DisplayString'
_H='Timeout'
_G='unset'
_F='centi-seconds'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='INFINET-BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
wanflex,=mibBuilder.importSymbols('INFINET-MIB','wanflex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_U,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','TextualConvention')
iwBrMIB=ModuleIdentity((1,3,6,1,4,1,3942,1,1,8))
if mibBuilder.loadTexts:iwBrMIB.setRevisions(('2014-03-13 07:18',))
class BridgeId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class Timeout(TextualConvention,Integer32):status=_A;displayHint='d'
class BridgeGroupIdOrZero(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_IwBrMIBObjects_ObjectIdentity=ObjectIdentity
iwBrMIBObjects=_IwBrMIBObjects_ObjectIdentity((1,3,6,1,4,1,3942,1,1,8,1))
_IwBrBase_ObjectIdentity=ObjectIdentity
iwBrBase=_IwBrBase_ObjectIdentity((1,3,6,1,4,1,3942,1,1,8,1,1))
_IwBrBaseAddress_Type=MacAddress
_IwBrBaseAddress_Object=MibScalar
iwBrBaseAddress=_IwBrBaseAddress_Object((1,3,6,1,4,1,3942,1,1,8,1,1,1),_IwBrBaseAddress_Type())
iwBrBaseAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrBaseAddress.setStatus(_A)
_IwBrBasePorts_Type=Integer32
_IwBrBasePorts_Object=MibScalar
iwBrBasePorts=_IwBrBasePorts_Object((1,3,6,1,4,1,3942,1,1,8,1,1,2),_IwBrBasePorts_Type())
iwBrBasePorts.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrBasePorts.setStatus(_A)
class _IwBrBaseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('transparent-only',2),('sourceroute-only',3),('srt',4)))
_IwBrBaseType_Type.__name__=_D
_IwBrBaseType_Object=MibScalar
iwBrBaseType=_IwBrBaseType_Object((1,3,6,1,4,1,3942,1,1,8,1,1,3),_IwBrBaseType_Type())
iwBrBaseType.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrBaseType.setStatus(_A)
_IwBrLocalTag_Type=Integer32
_IwBrLocalTag_Object=MibScalar
iwBrLocalTag=_IwBrLocalTag_Object((1,3,6,1,4,1,3942,1,1,8,1,1,4),_IwBrLocalTag_Type())
iwBrLocalTag.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrLocalTag.setStatus(_A)
_IwBrStp_ObjectIdentity=ObjectIdentity
iwBrStp=_IwBrStp_ObjectIdentity((1,3,6,1,4,1,3942,1,1,8,1,2))
class _IwBrStpProtoSpec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('decLb100',2),('ieee8021d',3)))
_IwBrStpProtoSpec_Type.__name__=_D
_IwBrStpProtoSpec_Object=MibScalar
iwBrStpProtoSpec=_IwBrStpProtoSpec_Object((1,3,6,1,4,1,3942,1,1,8,1,2,1),_IwBrStpProtoSpec_Type())
iwBrStpProtoSpec.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrStpProtoSpec.setStatus(_A)
class _IwBrStpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IwBrStpPriority_Type.__name__=_D
_IwBrStpPriority_Object=MibScalar
iwBrStpPriority=_IwBrStpPriority_Object((1,3,6,1,4,1,3942,1,1,8,1,2,2),_IwBrStpPriority_Type())
iwBrStpPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:iwBrStpPriority.setStatus(_A)
_IwBrStpTimeSinceTopoChange_Type=TimeTicks
_IwBrStpTimeSinceTopoChange_Object=MibScalar
iwBrStpTimeSinceTopoChange=_IwBrStpTimeSinceTopoChange_Object((1,3,6,1,4,1,3942,1,1,8,1,2,3),_IwBrStpTimeSinceTopoChange_Type())
iwBrStpTimeSinceTopoChange.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrStpTimeSinceTopoChange.setStatus(_A)
if mibBuilder.loadTexts:iwBrStpTimeSinceTopoChange.setUnits(_F)
_IwBrStpTopChanges_Type=Counter32
_IwBrStpTopChanges_Object=MibScalar
iwBrStpTopChanges=_IwBrStpTopChanges_Object((1,3,6,1,4,1,3942,1,1,8,1,2,4),_IwBrStpTopChanges_Type())
iwBrStpTopChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrStpTopChanges.setStatus(_A)
_IwBrStpMaxAge_Type=Timeout
_IwBrStpMaxAge_Object=MibScalar
iwBrStpMaxAge=_IwBrStpMaxAge_Object((1,3,6,1,4,1,3942,1,1,8,1,2,5),_IwBrStpMaxAge_Type())
iwBrStpMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrStpMaxAge.setStatus(_A)
if mibBuilder.loadTexts:iwBrStpMaxAge.setUnits(_F)
_IwBrStpHelloTime_Type=Timeout
_IwBrStpHelloTime_Object=MibScalar
iwBrStpHelloTime=_IwBrStpHelloTime_Object((1,3,6,1,4,1,3942,1,1,8,1,2,6),_IwBrStpHelloTime_Type())
iwBrStpHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrStpHelloTime.setStatus(_A)
if mibBuilder.loadTexts:iwBrStpHelloTime.setUnits(_F)
_IwBrStpHoldTime_Type=Integer32
_IwBrStpHoldTime_Object=MibScalar
iwBrStpHoldTime=_IwBrStpHoldTime_Object((1,3,6,1,4,1,3942,1,1,8,1,2,7),_IwBrStpHoldTime_Type())
iwBrStpHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrStpHoldTime.setStatus(_A)
if mibBuilder.loadTexts:iwBrStpHoldTime.setUnits(_F)
_IwBrStpForwardDelay_Type=Timeout
_IwBrStpForwardDelay_Object=MibScalar
iwBrStpForwardDelay=_IwBrStpForwardDelay_Object((1,3,6,1,4,1,3942,1,1,8,1,2,8),_IwBrStpForwardDelay_Type())
iwBrStpForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrStpForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:iwBrStpForwardDelay.setUnits(_F)
class _IwBrStpBridgeMaxAge_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_IwBrStpBridgeMaxAge_Type.__name__=_H
_IwBrStpBridgeMaxAge_Object=MibScalar
iwBrStpBridgeMaxAge=_IwBrStpBridgeMaxAge_Object((1,3,6,1,4,1,3942,1,1,8,1,2,9),_IwBrStpBridgeMaxAge_Type())
iwBrStpBridgeMaxAge.setMaxAccess(_E)
if mibBuilder.loadTexts:iwBrStpBridgeMaxAge.setStatus(_A)
if mibBuilder.loadTexts:iwBrStpBridgeMaxAge.setUnits(_F)
class _IwBrStpBridgeHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_IwBrStpBridgeHelloTime_Type.__name__=_H
_IwBrStpBridgeHelloTime_Object=MibScalar
iwBrStpBridgeHelloTime=_IwBrStpBridgeHelloTime_Object((1,3,6,1,4,1,3942,1,1,8,1,2,10),_IwBrStpBridgeHelloTime_Type())
iwBrStpBridgeHelloTime.setMaxAccess(_E)
if mibBuilder.loadTexts:iwBrStpBridgeHelloTime.setStatus(_A)
if mibBuilder.loadTexts:iwBrStpBridgeHelloTime.setUnits(_F)
class _IwBrStpBridgeForwardDelay_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_IwBrStpBridgeForwardDelay_Type.__name__=_H
_IwBrStpBridgeForwardDelay_Object=MibScalar
iwBrStpBridgeForwardDelay=_IwBrStpBridgeForwardDelay_Object((1,3,6,1,4,1,3942,1,1,8,1,2,11),_IwBrStpBridgeForwardDelay_Type())
iwBrStpBridgeForwardDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:iwBrStpBridgeForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:iwBrStpBridgeForwardDelay.setUnits(_F)
_IwBrPorts_ObjectIdentity=ObjectIdentity
iwBrPorts=_IwBrPorts_ObjectIdentity((1,3,6,1,4,1,3942,1,1,8,1,3))
_IwBrPortTable_Object=MibTable
iwBrPortTable=_IwBrPortTable_Object((1,3,6,1,4,1,3942,1,1,8,1,3,1))
if mibBuilder.loadTexts:iwBrPortTable.setStatus(_A)
_IwBrPortEntry_Object=MibTableRow
iwBrPortEntry=_IwBrPortEntry_Object((1,3,6,1,4,1,3942,1,1,8,1,3,1,1))
iwBrPortEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:iwBrPortEntry.setStatus(_A)
_IwBrPortGrpId_Type=BridgeGroupIdOrZero
_IwBrPortGrpId_Object=MibTableColumn
iwBrPortGrpId=_IwBrPortGrpId_Object((1,3,6,1,4,1,3942,1,1,8,1,3,1,1,1),_IwBrPortGrpId_Type())
iwBrPortGrpId.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrPortGrpId.setStatus(_A)
_IwBrPortId_Type=InterfaceIndex
_IwBrPortId_Object=MibTableColumn
iwBrPortId=_IwBrPortId_Object((1,3,6,1,4,1,3942,1,1,8,1,3,1,1,2),_IwBrPortId_Type())
iwBrPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrPortId.setStatus(_A)
class _IwBrPortStpPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IwBrPortStpPrio_Type.__name__=_D
_IwBrPortStpPrio_Object=MibTableColumn
iwBrPortStpPrio=_IwBrPortStpPrio_Object((1,3,6,1,4,1,3942,1,1,8,1,3,1,1,3),_IwBrPortStpPrio_Type())
iwBrPortStpPrio.setMaxAccess(_E)
if mibBuilder.loadTexts:iwBrPortStpPrio.setStatus(_A)
class _IwBrPortStpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_V,1),('blocking',2),('listening',3),('learning',4),('forwarding',5),('broken',6)))
_IwBrPortStpState_Type.__name__=_D
_IwBrPortStpState_Object=MibTableColumn
iwBrPortStpState=_IwBrPortStpState_Object((1,3,6,1,4,1,3942,1,1,8,1,3,1,1,4),_IwBrPortStpState_Type())
iwBrPortStpState.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrPortStpState.setStatus(_A)
class _IwBrPortStpRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_V,1),('root',2),('designated',3),('alternate',4),('backup',5)))
_IwBrPortStpRole_Type.__name__=_D
_IwBrPortStpRole_Object=MibTableColumn
iwBrPortStpRole=_IwBrPortStpRole_Object((1,3,6,1,4,1,3942,1,1,8,1,3,1,1,5),_IwBrPortStpRole_Type())
iwBrPortStpRole.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrPortStpRole.setStatus(_A)
_IwBrPortStpDesCost_Type=Integer32
_IwBrPortStpDesCost_Object=MibTableColumn
iwBrPortStpDesCost=_IwBrPortStpDesCost_Object((1,3,6,1,4,1,3942,1,1,8,1,3,1,1,6),_IwBrPortStpDesCost_Type())
iwBrPortStpDesCost.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrPortStpDesCost.setStatus(_A)
_IwBrPortStpDesBridge_Type=BridgeId
_IwBrPortStpDesBridge_Object=MibTableColumn
iwBrPortStpDesBridge=_IwBrPortStpDesBridge_Object((1,3,6,1,4,1,3942,1,1,8,1,3,1,1,7),_IwBrPortStpDesBridge_Type())
iwBrPortStpDesBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrPortStpDesBridge.setStatus(_A)
class _IwBrPortStpDesPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IwBrPortStpDesPort_Type.__name__=_D
_IwBrPortStpDesPort_Object=MibTableColumn
iwBrPortStpDesPort=_IwBrPortStpDesPort_Object((1,3,6,1,4,1,3942,1,1,8,1,3,1,1,8),_IwBrPortStpDesPort_Type())
iwBrPortStpDesPort.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrPortStpDesPort.setStatus(_A)
_IwBrPortStpFwdTransitions_Type=Counter32
_IwBrPortStpFwdTransitions_Object=MibTableColumn
iwBrPortStpFwdTransitions=_IwBrPortStpFwdTransitions_Object((1,3,6,1,4,1,3942,1,1,8,1,3,1,1,9),_IwBrPortStpFwdTransitions_Type())
iwBrPortStpFwdTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrPortStpFwdTransitions.setStatus(_A)
class _IwBrPortStpPathCost32_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_IwBrPortStpPathCost32_Type.__name__=_D
_IwBrPortStpPathCost32_Object=MibTableColumn
iwBrPortStpPathCost32=_IwBrPortStpPathCost32_Object((1,3,6,1,4,1,3942,1,1,8,1,3,1,1,10),_IwBrPortStpPathCost32_Type())
iwBrPortStpPathCost32.setMaxAccess(_E)
if mibBuilder.loadTexts:iwBrPortStpPathCost32.setStatus(_A)
class _IwBrPortVlanAlteration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,4095))
_IwBrPortVlanAlteration_Type.__name__=_D
_IwBrPortVlanAlteration_Object=MibTableColumn
iwBrPortVlanAlteration=_IwBrPortVlanAlteration_Object((1,3,6,1,4,1,3942,1,1,8,1,3,1,1,11),_IwBrPortVlanAlteration_Type())
iwBrPortVlanAlteration.setMaxAccess(_E)
if mibBuilder.loadTexts:iwBrPortVlanAlteration.setStatus(_A)
_IwBrDb_ObjectIdentity=ObjectIdentity
iwBrDb=_IwBrDb_ObjectIdentity((1,3,6,1,4,1,3942,1,1,8,1,4))
_IwBrDbEntryDiscards_Type=Counter32
_IwBrDbEntryDiscards_Object=MibScalar
iwBrDbEntryDiscards=_IwBrDbEntryDiscards_Object((1,3,6,1,4,1,3942,1,1,8,1,4,1),_IwBrDbEntryDiscards_Type())
iwBrDbEntryDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrDbEntryDiscards.setStatus(_A)
class _IwBrDbAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_IwBrDbAgingTime_Type.__name__=_D
_IwBrDbAgingTime_Object=MibScalar
iwBrDbAgingTime=_IwBrDbAgingTime_Object((1,3,6,1,4,1,3942,1,1,8,1,4,2),_IwBrDbAgingTime_Type())
iwBrDbAgingTime.setMaxAccess(_E)
if mibBuilder.loadTexts:iwBrDbAgingTime.setStatus(_A)
_IwBrDbTable_Object=MibTable
iwBrDbTable=_IwBrDbTable_Object((1,3,6,1,4,1,3942,1,1,8,1,4,3))
if mibBuilder.loadTexts:iwBrDbTable.setStatus(_A)
_IwBrDbEntry_Object=MibTableRow
iwBrDbEntry=_IwBrDbEntry_Object((1,3,6,1,4,1,3942,1,1,8,1,4,3,1))
iwBrDbEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:iwBrDbEntry.setStatus(_A)
_IwBrDbGroupId_Type=BridgeGroupIdOrZero
_IwBrDbGroupId_Object=MibTableColumn
iwBrDbGroupId=_IwBrDbGroupId_Object((1,3,6,1,4,1,3942,1,1,8,1,4,3,1,1),_IwBrDbGroupId_Type())
iwBrDbGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrDbGroupId.setStatus(_A)
_IwBrDbAddress_Type=MacAddress
_IwBrDbAddress_Object=MibTableColumn
iwBrDbAddress=_IwBrDbAddress_Object((1,3,6,1,4,1,3942,1,1,8,1,4,3,1,2),_IwBrDbAddress_Type())
iwBrDbAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrDbAddress.setStatus(_A)
_IwBrDbPort_Type=InterfaceIndex
_IwBrDbPort_Object=MibTableColumn
iwBrDbPort=_IwBrDbPort_Object((1,3,6,1,4,1,3942,1,1,8,1,4,3,1,3),_IwBrDbPort_Type())
iwBrDbPort.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrDbPort.setStatus(_A)
class _IwBrDbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('learned',3),('self',4)))
_IwBrDbStatus_Type.__name__=_D
_IwBrDbStatus_Object=MibTableColumn
iwBrDbStatus=_IwBrDbStatus_Object((1,3,6,1,4,1,3942,1,1,8,1,4,3,1,4),_IwBrDbStatus_Type())
iwBrDbStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrDbStatus.setStatus(_A)
_IwBrDbGwMac_Type=MacAddress
_IwBrDbGwMac_Object=MibTableColumn
iwBrDbGwMac=_IwBrDbGwMac_Object((1,3,6,1,4,1,3942,1,1,8,1,4,3,1,5),_IwBrDbGwMac_Type())
iwBrDbGwMac.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrDbGwMac.setStatus(_A)
class _IwBrDbGwType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('broadcast',1),('gateway',2)))
_IwBrDbGwType_Type.__name__=_D
_IwBrDbGwType_Object=MibTableColumn
iwBrDbGwType=_IwBrDbGwType_Object((1,3,6,1,4,1,3942,1,1,8,1,4,3,1,6),_IwBrDbGwType_Type())
iwBrDbGwType.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrDbGwType.setStatus(_A)
class _IwBrDbCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IwBrDbCost_Type.__name__=_D
_IwBrDbCost_Object=MibTableColumn
iwBrDbCost=_IwBrDbCost_Object((1,3,6,1,4,1,3942,1,1,8,1,4,3,1,7),_IwBrDbCost_Type())
iwBrDbCost.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrDbCost.setStatus(_A)
_IwBrDbUseCnt_Type=Counter32
_IwBrDbUseCnt_Object=MibTableColumn
iwBrDbUseCnt=_IwBrDbUseCnt_Object((1,3,6,1,4,1,3942,1,1,8,1,4,3,1,8),_IwBrDbUseCnt_Type())
iwBrDbUseCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrDbUseCnt.setStatus(_A)
_IwBrDbDead_Type=Gauge32
_IwBrDbDead_Object=MibTableColumn
iwBrDbDead=_IwBrDbDead_Object((1,3,6,1,4,1,3942,1,1,8,1,4,3,1,9),_IwBrDbDead_Type())
iwBrDbDead.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrDbDead.setStatus(_A)
_IwBrDbTrunkVLANId_Type=BridgeGroupIdOrZero
_IwBrDbTrunkVLANId_Object=MibTableColumn
iwBrDbTrunkVLANId=_IwBrDbTrunkVLANId_Object((1,3,6,1,4,1,3942,1,1,8,1,4,3,1,10),_IwBrDbTrunkVLANId_Type())
iwBrDbTrunkVLANId.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrDbTrunkVLANId.setStatus(_A)
class _IwBrDbGroupOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_IwBrDbGroupOrder_Type.__name__=_D
_IwBrDbGroupOrder_Object=MibTableColumn
iwBrDbGroupOrder=_IwBrDbGroupOrder_Object((1,3,6,1,4,1,3942,1,1,8,1,4,3,1,11),_IwBrDbGroupOrder_Type())
iwBrDbGroupOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrDbGroupOrder.setStatus(_A)
_IwBrGrp_ObjectIdentity=ObjectIdentity
iwBrGrp=_IwBrGrp_ObjectIdentity((1,3,6,1,4,1,3942,1,1,8,1,5))
_IwBrGrpTable_Object=MibTable
iwBrGrpTable=_IwBrGrpTable_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1))
if mibBuilder.loadTexts:iwBrGrpTable.setStatus(_A)
_IwBrGrpEntry_Object=MibTableRow
iwBrGrpEntry=_IwBrGrpEntry_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1))
iwBrGrpEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:iwBrGrpEntry.setStatus(_A)
_IwBrGrpId_Type=BridgeGroupIdOrZero
_IwBrGrpId_Object=MibTableColumn
iwBrGrpId=_IwBrGrpId_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,1),_IwBrGrpId_Type())
iwBrGrpId.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpId.setStatus(_A)
class _IwBrGrpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),('trunk',1)))
_IwBrGrpType_Type.__name__=_D
_IwBrGrpType_Object=MibTableColumn
iwBrGrpType=_IwBrGrpType_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,2),_IwBrGrpType_Type())
iwBrGrpType.setMaxAccess(_E)
if mibBuilder.loadTexts:iwBrGrpType.setStatus(_A)
class _IwBrGrpUsChan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('chan1',1),('chan2',2)))
_IwBrGrpUsChan_Type.__name__=_D
_IwBrGrpUsChan_Object=MibTableColumn
iwBrGrpUsChan=_IwBrGrpUsChan_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,3),_IwBrGrpUsChan_Type())
iwBrGrpUsChan.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpUsChan.setStatus(_A)
class _IwBrGrpDsChan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('chan1',1),('chan2',2)))
_IwBrGrpDsChan_Type.__name__=_D
_IwBrGrpDsChan_Object=MibTableColumn
iwBrGrpDsChan=_IwBrGrpDsChan_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,4),_IwBrGrpDsChan_Type())
iwBrGrpDsChan.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpDsChan.setStatus(_A)
_IwBrGrpInTrunk_Type=BridgeGroupIdOrZero
_IwBrGrpInTrunk_Object=MibTableColumn
iwBrGrpInTrunk=_IwBrGrpInTrunk_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,5),_IwBrGrpInTrunk_Type())
iwBrGrpInTrunk.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpInTrunk.setStatus(_A)
class _IwBrGrpUncoupled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),('uncoupled',1)))
_IwBrGrpUncoupled_Type.__name__=_D
_IwBrGrpUncoupled_Object=MibTableColumn
iwBrGrpUncoupled=_IwBrGrpUncoupled_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,6),_IwBrGrpUncoupled_Type())
iwBrGrpUncoupled.setMaxAccess(_E)
if mibBuilder.loadTexts:iwBrGrpUncoupled.setStatus(_A)
class _IwBrGrpFlgSTP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('stp',1)))
_IwBrGrpFlgSTP_Type.__name__=_D
_IwBrGrpFlgSTP_Object=MibTableColumn
iwBrGrpFlgSTP=_IwBrGrpFlgSTP_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,7),_IwBrGrpFlgSTP_Type())
iwBrGrpFlgSTP.setMaxAccess(_E)
if mibBuilder.loadTexts:iwBrGrpFlgSTP.setStatus(_A)
class _IwBrGrpFlgIGMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('igmp',1)))
_IwBrGrpFlgIGMP_Type.__name__=_D
_IwBrGrpFlgIGMP_Object=MibTableColumn
iwBrGrpFlgIGMP=_IwBrGrpFlgIGMP_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,8),_IwBrGrpFlgIGMP_Type())
iwBrGrpFlgIGMP.setMaxAccess(_E)
if mibBuilder.loadTexts:iwBrGrpFlgIGMP.setStatus(_A)
class _IwBrGrpFlgRptr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('repeater',1)))
_IwBrGrpFlgRptr_Type.__name__=_D
_IwBrGrpFlgRptr_Object=MibTableColumn
iwBrGrpFlgRptr=_IwBrGrpFlgRptr_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,9),_IwBrGrpFlgRptr_Type())
iwBrGrpFlgRptr.setMaxAccess(_E)
if mibBuilder.loadTexts:iwBrGrpFlgRptr.setStatus(_A)
class _IwBrGrpFlgAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('admin',1)))
_IwBrGrpFlgAdmin_Type.__name__=_D
_IwBrGrpFlgAdmin_Object=MibTableColumn
iwBrGrpFlgAdmin=_IwBrGrpFlgAdmin_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,10),_IwBrGrpFlgAdmin_Type())
iwBrGrpFlgAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:iwBrGrpFlgAdmin.setStatus(_A)
class _IwBrGrpFlgAct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inactive',0),('active',1)))
_IwBrGrpFlgAct_Type.__name__=_D
_IwBrGrpFlgAct_Object=MibTableColumn
iwBrGrpFlgAct=_IwBrGrpFlgAct_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,11),_IwBrGrpFlgAct_Type())
iwBrGrpFlgAct.setMaxAccess(_E)
if mibBuilder.loadTexts:iwBrGrpFlgAct.setStatus(_A)
class _IwBrGrpFlgOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('not-operative',0),('operative',1)))
_IwBrGrpFlgOper_Type.__name__=_D
_IwBrGrpFlgOper_Object=MibTableColumn
iwBrGrpFlgOper=_IwBrGrpFlgOper_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,12),_IwBrGrpFlgOper_Type())
iwBrGrpFlgOper.setMaxAccess(_E)
if mibBuilder.loadTexts:iwBrGrpFlgOper.setStatus(_A)
class _IwBrGrpInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_IwBrGrpInfo_Type.__name__=_I
_IwBrGrpInfo_Object=MibTableColumn
iwBrGrpInfo=_IwBrGrpInfo_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,13),_IwBrGrpInfo_Type())
iwBrGrpInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpInfo.setStatus(_A)
_IwBrGrpForwarded_Type=Counter32
_IwBrGrpForwarded_Object=MibTableColumn
iwBrGrpForwarded=_IwBrGrpForwarded_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,14),_IwBrGrpForwarded_Type())
iwBrGrpForwarded.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpForwarded.setStatus(_A)
_IwBrGrpFlooded_Type=Counter32
_IwBrGrpFlooded_Object=MibTableColumn
iwBrGrpFlooded=_IwBrGrpFlooded_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,15),_IwBrGrpFlooded_Type())
iwBrGrpFlooded.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpFlooded.setStatus(_A)
_IwBrGrpDropSTPL_Type=Counter32
_IwBrGrpDropSTPL_Object=MibTableColumn
iwBrGrpDropSTPL=_IwBrGrpDropSTPL_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,16),_IwBrGrpDropSTPL_Type())
iwBrGrpDropSTPL.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpDropSTPL.setStatus(_A)
_IwBrGrpDropUNRD_Type=Counter32
_IwBrGrpDropUNRD_Object=MibTableColumn
iwBrGrpDropUNRD=_IwBrGrpDropUNRD_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,17),_IwBrGrpDropUNRD_Type())
iwBrGrpDropUNRD.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpDropUNRD.setStatus(_A)
_IwBrGrpDropFWRL_Type=Counter32
_IwBrGrpDropFWRL_Object=MibTableColumn
iwBrGrpDropFWRL=_IwBrGrpDropFWRL_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,18),_IwBrGrpDropFWRL_Type())
iwBrGrpDropFWRL.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpDropFWRL.setStatus(_A)
_IwBrGrpDropLOOP_Type=Counter32
_IwBrGrpDropLOOP_Object=MibTableColumn
iwBrGrpDropLOOP=_IwBrGrpDropLOOP_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,19),_IwBrGrpDropLOOP_Type())
iwBrGrpDropLOOP.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpDropLOOP.setStatus(_A)
_IwBrGrpDropNOBG_Type=Counter32
_IwBrGrpDropNOBG_Object=MibTableColumn
iwBrGrpDropNOBG=_IwBrGrpDropNOBG_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,20),_IwBrGrpDropNOBG_Type())
iwBrGrpDropNOBG.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpDropNOBG.setStatus(_A)
_IwBrGrpDropLCNA_Type=Counter32
_IwBrGrpDropLCNA_Object=MibTableColumn
iwBrGrpDropLCNA=_IwBrGrpDropLCNA_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,21),_IwBrGrpDropLCNA_Type())
iwBrGrpDropLCNA.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpDropLCNA.setStatus(_A)
_IwBrGrpDropJOIN_Type=Counter32
_IwBrGrpDropJOIN_Object=MibTableColumn
iwBrGrpDropJOIN=_IwBrGrpDropJOIN_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,22),_IwBrGrpDropJOIN_Type())
iwBrGrpDropJOIN.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpDropJOIN.setStatus(_A)
_IwBrGrpDropSDPS_Type=Counter32
_IwBrGrpDropSDPS_Object=MibTableColumn
iwBrGrpDropSDPS=_IwBrGrpDropSDPS_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,23),_IwBrGrpDropSDPS_Type())
iwBrGrpDropSDPS.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpDropSDPS.setStatus(_A)
_IwBrGrpStpRoot_Type=BridgeId
_IwBrGrpStpRoot_Object=MibTableColumn
iwBrGrpStpRoot=_IwBrGrpStpRoot_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,24),_IwBrGrpStpRoot_Type())
iwBrGrpStpRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpStpRoot.setStatus(_A)
class _IwBrGrpStpRootPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IwBrGrpStpRootPort_Type.__name__=_D
_IwBrGrpStpRootPort_Object=MibTableColumn
iwBrGrpStpRootPort=_IwBrGrpStpRootPort_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,25),_IwBrGrpStpRootPort_Type())
iwBrGrpStpRootPort.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpStpRootPort.setStatus(_A)
class _IwBrPortStpPVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stp',1),('rstp',2)))
_IwBrPortStpPVer_Type.__name__=_D
_IwBrPortStpPVer_Object=MibTableColumn
iwBrPortStpPVer=_IwBrPortStpPVer_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,26),_IwBrPortStpPVer_Type())
iwBrPortStpPVer.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrPortStpPVer.setStatus(_A)
class _IwBrGrpDefaultAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),('deny',2)))
_IwBrGrpDefaultAction_Type.__name__=_D
_IwBrGrpDefaultAction_Object=MibTableColumn
iwBrGrpDefaultAction=_IwBrGrpDefaultAction_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,27),_IwBrGrpDefaultAction_Type())
iwBrGrpDefaultAction.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpDefaultAction.setStatus(_A)
class _IwBrGrpXVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('xvlan',1),(_G,2)))
_IwBrGrpXVlan_Type.__name__=_D
_IwBrGrpXVlan_Object=MibTableColumn
iwBrGrpXVlan=_IwBrGrpXVlan_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,28),_IwBrGrpXVlan_Type())
iwBrGrpXVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpXVlan.setStatus(_A)
class _IwBrGrpPermittedVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-4095,2147483647))
_IwBrGrpPermittedVLAN_Type.__name__=_D
_IwBrGrpPermittedVLAN_Object=MibTableColumn
iwBrGrpPermittedVLAN=_IwBrGrpPermittedVLAN_Object((1,3,6,1,4,1,3942,1,1,8,1,5,1,1,29),_IwBrGrpPermittedVLAN_Type())
iwBrGrpPermittedVLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrGrpPermittedVLAN.setStatus(_A)
_IwBrRules_ObjectIdentity=ObjectIdentity
iwBrRules=_IwBrRules_ObjectIdentity((1,3,6,1,4,1,3942,1,1,8,1,6))
_IwBrRuleTable_Object=MibTable
iwBrRuleTable=_IwBrRuleTable_Object((1,3,6,1,4,1,3942,1,1,8,1,6,1))
if mibBuilder.loadTexts:iwBrRuleTable.setStatus(_A)
_IwBrRuleEntry_Object=MibTableRow
iwBrRuleEntry=_IwBrRuleEntry_Object((1,3,6,1,4,1,3942,1,1,8,1,6,1,1))
iwBrRuleEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:iwBrRuleEntry.setStatus(_A)
class _IwBrRuleGrpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_IwBrRuleGrpId_Type.__name__=_D
_IwBrRuleGrpId_Object=MibTableColumn
iwBrRuleGrpId=_IwBrRuleGrpId_Object((1,3,6,1,4,1,3942,1,1,8,1,6,1,1,1),_IwBrRuleGrpId_Type())
iwBrRuleGrpId.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrRuleGrpId.setStatus(_A)
class _IwBrRulePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IwBrRulePriority_Type.__name__=_D
_IwBrRulePriority_Object=MibTableColumn
iwBrRulePriority=_IwBrRulePriority_Object((1,3,6,1,4,1,3942,1,1,8,1,6,1,1,2),_IwBrRulePriority_Type())
iwBrRulePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrRulePriority.setStatus(_A)
class _IwBrRuleAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),('deny',2)))
_IwBrRuleAction_Type.__name__=_D
_IwBrRuleAction_Object=MibTableColumn
iwBrRuleAction=_IwBrRuleAction_Object((1,3,6,1,4,1,3942,1,1,8,1,6,1,1,3),_IwBrRuleAction_Type())
iwBrRuleAction.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrRuleAction.setStatus(_A)
class _IwBrRuleMatchList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IwBrRuleMatchList_Type.__name__=_D
_IwBrRuleMatchList_Object=MibTableColumn
iwBrRuleMatchList=_IwBrRuleMatchList_Object((1,3,6,1,4,1,3942,1,1,8,1,6,1,1,4),_IwBrRuleMatchList_Type())
iwBrRuleMatchList.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrRuleMatchList.setStatus(_A)
class _IwBrRuleVlanList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IwBrRuleVlanList_Type.__name__=_D
_IwBrRuleVlanList_Object=MibTableColumn
iwBrRuleVlanList=_IwBrRuleVlanList_Object((1,3,6,1,4,1,3942,1,1,8,1,6,1,1,5),_IwBrRuleVlanList_Type())
iwBrRuleVlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrRuleVlanList.setStatus(_A)
class _IwBrRuleIfaceList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IwBrRuleIfaceList_Type.__name__=_D
_IwBrRuleIfaceList_Object=MibTableColumn
iwBrRuleIfaceList=_IwBrRuleIfaceList_Object((1,3,6,1,4,1,3942,1,1,8,1,6,1,1,6),_IwBrRuleIfaceList_Type())
iwBrRuleIfaceList.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrRuleIfaceList.setStatus(_A)
class _IwBrRuleSrcList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IwBrRuleSrcList_Type.__name__=_D
_IwBrRuleSrcList_Object=MibTableColumn
iwBrRuleSrcList=_IwBrRuleSrcList_Object((1,3,6,1,4,1,3942,1,1,8,1,6,1,1,7),_IwBrRuleSrcList_Type())
iwBrRuleSrcList.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrRuleSrcList.setStatus(_A)
class _IwBrRuleDstList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IwBrRuleDstList_Type.__name__=_D
_IwBrRuleDstList_Object=MibTableColumn
iwBrRuleDstList=_IwBrRuleDstList_Object((1,3,6,1,4,1,3942,1,1,8,1,6,1,1,8),_IwBrRuleDstList_Type())
iwBrRuleDstList.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrRuleDstList.setStatus(_A)
class _IwBrRuleProtoList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IwBrRuleProtoList_Type.__name__=_D
_IwBrRuleProtoList_Object=MibTableColumn
iwBrRuleProtoList=_IwBrRuleProtoList_Object((1,3,6,1,4,1,3942,1,1,8,1,6,1,1,9),_IwBrRuleProtoList_Type())
iwBrRuleProtoList.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrRuleProtoList.setStatus(_A)
_IwBrListTable_Object=MibTable
iwBrListTable=_IwBrListTable_Object((1,3,6,1,4,1,3942,1,1,8,1,6,2))
if mibBuilder.loadTexts:iwBrListTable.setStatus(_A)
_IwBrListEntry_Object=MibTableRow
iwBrListEntry=_IwBrListEntry_Object((1,3,6,1,4,1,3942,1,1,8,1,6,2,1))
iwBrListEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:iwBrListEntry.setStatus(_A)
class _IwBrListId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IwBrListId_Type.__name__=_D
_IwBrListId_Object=MibTableColumn
iwBrListId=_IwBrListId_Object((1,3,6,1,4,1,3942,1,1,8,1,6,2,1,1),_IwBrListId_Type())
iwBrListId.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrListId.setStatus(_A)
class _IwBrListType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('iface',1),('mac',2),('numrange',3),('match',4)))
_IwBrListType_Type.__name__=_D
_IwBrListType_Object=MibTableColumn
iwBrListType=_IwBrListType_Object((1,3,6,1,4,1,3942,1,1,8,1,6,2,1,2),_IwBrListType_Type())
iwBrListType.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrListType.setStatus(_A)
class _IwBrListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_IwBrListName_Type.__name__=_I
_IwBrListName_Object=MibTableColumn
iwBrListName=_IwBrListName_Object((1,3,6,1,4,1,3942,1,1,8,1,6,2,1,3),_IwBrListName_Type())
iwBrListName.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrListName.setStatus(_A)
_IwBrListValues_Type=DisplayString
_IwBrListValues_Object=MibTableColumn
iwBrListValues=_IwBrListValues_Object((1,3,6,1,4,1,3942,1,1,8,1,6,2,1,4),_IwBrListValues_Type())
iwBrListValues.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrListValues.setStatus(_A)
_IwBrBlackList_ObjectIdentity=ObjectIdentity
iwBrBlackList=_IwBrBlackList_ObjectIdentity((1,3,6,1,4,1,3942,1,1,8,1,7))
_IwBrBlackListTable_Object=MibTable
iwBrBlackListTable=_IwBrBlackListTable_Object((1,3,6,1,4,1,3942,1,1,8,1,7,1))
if mibBuilder.loadTexts:iwBrBlackListTable.setStatus(_A)
_IwBrBlackListEntry_Object=MibTableRow
iwBrBlackListEntry=_IwBrBlackListEntry_Object((1,3,6,1,4,1,3942,1,1,8,1,7,1,1))
iwBrBlackListEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:iwBrBlackListEntry.setStatus(_A)
class _IwBrBlackListGrpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_IwBrBlackListGrpId_Type.__name__=_D
_IwBrBlackListGrpId_Object=MibTableColumn
iwBrBlackListGrpId=_IwBrBlackListGrpId_Object((1,3,6,1,4,1,3942,1,1,8,1,7,1,1,1),_IwBrBlackListGrpId_Type())
iwBrBlackListGrpId.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrBlackListGrpId.setStatus(_A)
_IwBrBlackListDstMac_Type=MacAddress
_IwBrBlackListDstMac_Object=MibTableColumn
iwBrBlackListDstMac=_IwBrBlackListDstMac_Object((1,3,6,1,4,1,3942,1,1,8,1,7,1,1,2),_IwBrBlackListDstMac_Type())
iwBrBlackListDstMac.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrBlackListDstMac.setStatus(_A)
_IwBrBlackListSrcMac_Type=MacAddress
_IwBrBlackListSrcMac_Object=MibTableColumn
iwBrBlackListSrcMac=_IwBrBlackListSrcMac_Object((1,3,6,1,4,1,3942,1,1,8,1,7,1,1,3),_IwBrBlackListSrcMac_Type())
iwBrBlackListSrcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrBlackListSrcMac.setStatus(_A)
class _IwBrBlackListTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_IwBrBlackListTime_Type.__name__=_U
_IwBrBlackListTime_Object=MibTableColumn
iwBrBlackListTime=_IwBrBlackListTime_Object((1,3,6,1,4,1,3942,1,1,8,1,7,1,1,4),_IwBrBlackListTime_Type())
iwBrBlackListTime.setMaxAccess(_C)
if mibBuilder.loadTexts:iwBrBlackListTime.setStatus(_A)
_IwBrMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
iwBrMIBNotificationsPrefix=_IwBrMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,3942,1,1,8,2))
_IwBrMIBNotifications_ObjectIdentity=ObjectIdentity
iwBrMIBNotifications=_IwBrMIBNotifications_ObjectIdentity((1,3,6,1,4,1,3942,1,1,8,2,0))
_IwBrMIBConformance_ObjectIdentity=ObjectIdentity
iwBrMIBConformance=_IwBrMIBConformance_ObjectIdentity((1,3,6,1,4,1,3942,1,1,8,3))
iwBrMIBGroup=ObjectGroup((1,3,6,1,4,1,3942,1,1,8,3,2))
iwBrMIBGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_K),(_B,_L),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_M),(_B,_N),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_O),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_P),(_B,_Q),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_R),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_S),(_B,_T),(_B,_Aj),(_B,_Ak)))
if mibBuilder.loadTexts:iwBrMIBGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'BridgeId':BridgeId,_H:Timeout,'BridgeGroupIdOrZero':BridgeGroupIdOrZero,'iwBrMIB':iwBrMIB,'iwBrMIBObjects':iwBrMIBObjects,'iwBrBase':iwBrBase,_Y:iwBrBaseAddress,_Z:iwBrBasePorts,_a:iwBrBaseType,_b:iwBrLocalTag,'iwBrStp':iwBrStp,_c:iwBrStpProtoSpec,_d:iwBrStpPriority,_e:iwBrStpTimeSinceTopoChange,_f:iwBrStpTopChanges,_g:iwBrStpMaxAge,_h:iwBrStpHelloTime,_i:iwBrStpHoldTime,_j:iwBrStpForwardDelay,_k:iwBrStpBridgeMaxAge,_l:iwBrStpBridgeHelloTime,_m:iwBrStpBridgeForwardDelay,'iwBrPorts':iwBrPorts,'iwBrPortTable':iwBrPortTable,'iwBrPortEntry':iwBrPortEntry,_K:iwBrPortGrpId,_L:iwBrPortId,_n:iwBrPortStpPrio,_o:iwBrPortStpState,_p:iwBrPortStpRole,_q:iwBrPortStpDesCost,_r:iwBrPortStpDesBridge,_s:iwBrPortStpDesPort,_t:iwBrPortStpFwdTransitions,_u:iwBrPortStpPathCost32,_v:iwBrPortVlanAlteration,'iwBrDb':iwBrDb,_w:iwBrDbEntryDiscards,_x:iwBrDbAgingTime,'iwBrDbTable':iwBrDbTable,'iwBrDbEntry':iwBrDbEntry,_M:iwBrDbGroupId,_N:iwBrDbAddress,_y:iwBrDbPort,_z:iwBrDbStatus,_A0:iwBrDbGwMac,_A1:iwBrDbGwType,_A2:iwBrDbCost,_A3:iwBrDbUseCnt,_A4:iwBrDbDead,_A5:iwBrDbTrunkVLANId,_A6:iwBrDbGroupOrder,'iwBrGrp':iwBrGrp,'iwBrGrpTable':iwBrGrpTable,'iwBrGrpEntry':iwBrGrpEntry,_O:iwBrGrpId,_A7:iwBrGrpType,_A8:iwBrGrpUsChan,_A9:iwBrGrpDsChan,_AA:iwBrGrpInTrunk,_AB:iwBrGrpUncoupled,_AC:iwBrGrpFlgSTP,_AD:iwBrGrpFlgIGMP,_AE:iwBrGrpFlgRptr,_AF:iwBrGrpFlgAdmin,_AG:iwBrGrpFlgAct,_AH:iwBrGrpFlgOper,_AI:iwBrGrpInfo,_AJ:iwBrGrpForwarded,_AK:iwBrGrpFlooded,_AL:iwBrGrpDropSTPL,_AM:iwBrGrpDropUNRD,_AN:iwBrGrpDropFWRL,_AO:iwBrGrpDropLOOP,_AP:iwBrGrpDropNOBG,_AQ:iwBrGrpDropLCNA,_AR:iwBrGrpDropJOIN,_AS:iwBrGrpDropSDPS,_AT:iwBrGrpStpRoot,_AU:iwBrGrpStpRootPort,_AV:iwBrPortStpPVer,_AW:iwBrGrpDefaultAction,_AX:iwBrGrpXVlan,_AY:iwBrGrpPermittedVLAN,'iwBrRules':iwBrRules,'iwBrRuleTable':iwBrRuleTable,'iwBrRuleEntry':iwBrRuleEntry,_P:iwBrRuleGrpId,_Q:iwBrRulePriority,_AZ:iwBrRuleAction,_Aa:iwBrRuleMatchList,_Ab:iwBrRuleVlanList,_Ac:iwBrRuleIfaceList,_Ad:iwBrRuleSrcList,_Ae:iwBrRuleDstList,_Af:iwBrRuleProtoList,'iwBrListTable':iwBrListTable,'iwBrListEntry':iwBrListEntry,_R:iwBrListId,_Ag:iwBrListType,_Ah:iwBrListName,_Ai:iwBrListValues,'iwBrBlackList':iwBrBlackList,'iwBrBlackListTable':iwBrBlackListTable,'iwBrBlackListEntry':iwBrBlackListEntry,_S:iwBrBlackListGrpId,_T:iwBrBlackListDstMac,_Aj:iwBrBlackListSrcMac,_Ak:iwBrBlackListTime,'iwBrMIBNotificationsPrefix':iwBrMIBNotificationsPrefix,'iwBrMIBNotifications':iwBrMIBNotifications,'iwBrMIBConformance':iwBrMIBConformance,'iwBrMIBGroup':iwBrMIBGroup})