_Av='ciscoWanFrConnQueueGroup'
_Au='ciscoWanFrConnForesightGroup'
_At='ciscoWanFrConnABRGroup'
_As='ciscoWanFrConnEndptGroup'
_Ar='ciscoWanFrConnStateGroup'
_Aq='ciscoWanFrConnTestGroup'
_Ap='ciscoWanFrConnGroup'
_Ao='frstdABRPCR'
_An='frstdABRMCR'
_Am='frstdABRICR'
_Al='frstdABRADTF'
_Ak='frstdABRCDF'
_Aj='frstdABRTrm'
_Ai='frstdABRNrm'
_Ah='frstdABRRIF'
_Ag='frstdABRRDF'
_Af='frstdABRFRTT'
_Ae='frstdABRTBE'
_Ad='endLineNum'
_Ac='endChanNum'
_Ab='chanStatusBitMap'
_Aa='rcvATMState'
_AZ='xmtATMState'
_AY='rcvAbitState'
_AX='xmtAbitState'
_AW='chanState'
_AV='chanRTDResult'
_AU='chanTestState'
_AT='chanTestType'
_AS='egressQECNThresh'
_AR='egressQDEThresh'
_AQ='egressQDepth'
_AP='ingressQECNThresh'
_AO='ingressQDEThresh'
_AN='ingressQDepth'
_AM='foreSightEnable'
_AL='frChanDirectRoute'
_AK='frChanPrefRouteId'
_AJ='chanNumNextAvailable'
_AI='frConnRemoteMBS'
_AH='frChanSlaveType'
_AG='frChanUpcEnable'
_AF='frChanLocalLpbkEnable'
_AE='frChanStatsEnable'
_AD='frChanOamCCEnable'
_AC='frChanCnfIgnoreIncomingDE'
_AB='frChanCnfChangeCount'
_AA='frConnAdminStatus'
_A9='frConnTemplateId'
_A8='frConnRemoteSCR'
_A7='frConnSCR'
_A6='chanReroute'
_A5='zeroCirConEir'
_A4='chanServiceRate'
_A3='chanServiceRateOverride'
_A2='chanServType'
_A1='frConnFGCRAEnable'
_A0='frConnForeSightEnable'
_z='frConnRemotePercentUtil'
_y='frConnPercentUtil'
_x='frConnRemoteMCR'
_w='frConnMCR'
_v='frConnRemotePCR'
_u='frConnPCR'
_t='frRestrictTrunkType'
_s='frMaxCost'
_r='frRoutingPriority'
_q='frConnServiceType'
_p='frVpcFlag'
_o='frMastership'
_n='frRemoteNSAP'
_m='frRemoteVci'
_l='frRemoteVpi'
_k='frLocalNSAP'
_j='frLocalVci'
_i='frLocalVpi'
_h='frCDRNumber'
_g='chanFrConnType'
_f='chanOvrSubOvrRide'
_e='chanEgrSrvRate'
_d='chanEgrPercentUtil'
_c='chanIngrPercentUtil'
_b='chanCLPtoDEmap'
_a='chanDEtoCLPmap'
_Z='chanFECNconfig'
_Y='chanType'
_X='chanLocRmtLpbkState'
_W='deTaggingEnable'
_V='egressQSelect'
_U='chanPortNum'
_T='chanRowStatus'
_S='percentage'
_R='failed'
_Q='TruthValue'
_P='endDLCI'
_O='endPortNum'
_N='stateChanNum'
_M='cells-per-second'
_L='milli-seconds'
_K='frstdABRcnfChanNum'
_J='fastpackets-per-second'
_I='chanNum'
_H='OctetString'
_G='disable'
_F='enable'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='CISCO-WAN-FR-CONN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
frChan,frameRelay=mibBuilder.importSymbols('BASIS-MIB','frChan','frameRelay')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_Q)
ciscoWanFrConnMIB=ModuleIdentity((1,3,6,1,4,1,351,150,47))
if mibBuilder.loadTexts:ciscoWanFrConnMIB.setRevisions(('2002-09-18 00:00',))
_FrChanCnfGrp_ObjectIdentity=ObjectIdentity
frChanCnfGrp=_FrChanCnfGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,1,2,1))
_FrChanCnfGrpTable_Object=MibTable
frChanCnfGrpTable=_FrChanCnfGrpTable_Object((1,3,6,1,4,1,351,110,5,1,2,1,1))
if mibBuilder.loadTexts:frChanCnfGrpTable.setStatus(_A)
_FrChanCnfGrpEntry_Object=MibTableRow
frChanCnfGrpEntry=_FrChanCnfGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1))
frChanCnfGrpEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:frChanCnfGrpEntry.setStatus(_A)
class _ChanNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ChanNum_Type.__name__=_C
_ChanNum_Object=MibTableColumn
chanNum=_ChanNum_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,1),_ChanNum_Type())
chanNum.setMaxAccess(_E)
if mibBuilder.loadTexts:chanNum.setStatus(_A)
class _ChanRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('add',1),('del',2),('mod',3),('outOfService',4)))
_ChanRowStatus_Type.__name__=_C
_ChanRowStatus_Object=MibTableColumn
chanRowStatus=_ChanRowStatus_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,2),_ChanRowStatus_Type())
chanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:chanRowStatus.setStatus(_A)
_ChanPortNum_Type=Integer32
_ChanPortNum_Object=MibTableColumn
chanPortNum=_ChanPortNum_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,3),_ChanPortNum_Type())
chanPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:chanPortNum.setStatus(_A)
class _DLCI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8388607))
_DLCI_Type.__name__=_C
_DLCI_Object=MibTableColumn
dLCI=_DLCI_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,4),_DLCI_Type())
dLCI.setMaxAccess(_D)
if mibBuilder.loadTexts:dLCI.setStatus(_A)
class _EgressQSelect_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('highPriority',1),('lowPriority',2),('notSupported',3)))
_EgressQSelect_Type.__name__=_C
_EgressQSelect_Object=MibTableColumn
egressQSelect=_EgressQSelect_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,5),_EgressQSelect_Type())
egressQSelect.setMaxAccess(_D)
if mibBuilder.loadTexts:egressQSelect.setStatus(_A)
class _IngressQDepth_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4510,2097151))
_IngressQDepth_Type.__name__=_C
_IngressQDepth_Object=MibTableColumn
ingressQDepth=_IngressQDepth_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,6),_IngressQDepth_Type())
ingressQDepth.setMaxAccess(_D)
if mibBuilder.loadTexts:ingressQDepth.setStatus(_A)
class _IngressQECNThresh_Type(Integer32):defaultValue=6553;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2097151))
_IngressQECNThresh_Type.__name__=_C
_IngressQECNThresh_Object=MibTableColumn
ingressQECNThresh=_IngressQECNThresh_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,7),_IngressQECNThresh_Type())
ingressQECNThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:ingressQECNThresh.setStatus(_A)
class _IngressQDEThresh_Type(Integer32):defaultValue=32767;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2097151))
_IngressQDEThresh_Type.__name__=_C
_IngressQDEThresh_Object=MibTableColumn
ingressQDEThresh=_IngressQDEThresh_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,8),_IngressQDEThresh_Type())
ingressQDEThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:ingressQDEThresh.setStatus(_A)
class _EgressQDepth_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2097151))
_EgressQDepth_Type.__name__=_C
_EgressQDepth_Object=MibTableColumn
egressQDepth=_EgressQDepth_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,9),_EgressQDepth_Type())
egressQDepth.setMaxAccess(_D)
if mibBuilder.loadTexts:egressQDepth.setStatus(_A)
class _EgressQDEThresh_Type(Integer32):defaultValue=32767;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2097151))
_EgressQDEThresh_Type.__name__=_C
_EgressQDEThresh_Object=MibTableColumn
egressQDEThresh=_EgressQDEThresh_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,10),_EgressQDEThresh_Type())
egressQDEThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:egressQDEThresh.setStatus(_A)
class _EgressQECNThresh_Type(Integer32):defaultValue=6553;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2097151))
_EgressQECNThresh_Type.__name__=_C
_EgressQECNThresh_Object=MibTableColumn
egressQECNThresh=_EgressQECNThresh_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,11),_EgressQECNThresh_Type())
egressQECNThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:egressQECNThresh.setStatus(_A)
class _DeTaggingEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DeTaggingEnable_Type.__name__=_C
_DeTaggingEnable_Object=MibTableColumn
deTaggingEnable=_DeTaggingEnable_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,12),_DeTaggingEnable_Type())
deTaggingEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:deTaggingEnable.setStatus(_A)
class _Cir_Type(Integer32):defaultValue=2400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,52000000))
_Cir_Type.__name__=_C
_Cir_Object=MibTableColumn
cir=_Cir_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,13),_Cir_Type())
cir.setMaxAccess(_D)
if mibBuilder.loadTexts:cir.setStatus(_A)
if mibBuilder.loadTexts:cir.setUnits('bps')
class _Bc_Type(Integer32):defaultValue=5100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2097151))
_Bc_Type.__name__=_C
_Bc_Object=MibTableColumn
bc=_Bc_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,14),_Bc_Type())
bc.setMaxAccess(_D)
if mibBuilder.loadTexts:bc.setStatus(_A)
if mibBuilder.loadTexts:bc.setUnits('bytes')
class _Be_Type(Integer32):defaultValue=5100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2097151))
_Be_Type.__name__=_C
_Be_Object=MibTableColumn
be=_Be_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,15),_Be_Type())
be.setMaxAccess(_D)
if mibBuilder.loadTexts:be.setStatus(_A)
if mibBuilder.loadTexts:be.setUnits('bytes')
class _Ibs_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2097151))
_Ibs_Type.__name__=_C
_Ibs_Object=MibTableColumn
ibs=_Ibs_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,16),_Ibs_Type())
ibs.setMaxAccess(_D)
if mibBuilder.loadTexts:ibs.setStatus(_A)
class _ForeSightEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ForeSightEnable_Type.__name__=_C
_ForeSightEnable_Object=MibTableColumn
foreSightEnable=_ForeSightEnable_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,17),_ForeSightEnable_Type())
foreSightEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:foreSightEnable.setStatus(_A)
class _Qir_Type(Integer32):defaultValue=160;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(160,6400000))
_Qir_Type.__name__=_C
_Qir_Object=MibTableColumn
qir=_Qir_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,18),_Qir_Type())
qir.setMaxAccess(_D)
if mibBuilder.loadTexts:qir.setStatus(_A)
if mibBuilder.loadTexts:qir.setUnits(_J)
class _Mir_Type(Integer32):defaultValue=160;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(160,6400000))
_Mir_Type.__name__=_C
_Mir_Object=MibTableColumn
mir=_Mir_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,19),_Mir_Type())
mir.setMaxAccess(_D)
if mibBuilder.loadTexts:mir.setStatus(_A)
if mibBuilder.loadTexts:mir.setUnits(_J)
class _Pir_Type(Integer32):defaultValue=160;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(160,6400000))
_Pir_Type.__name__=_C
_Pir_Object=MibTableColumn
pir=_Pir_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,20),_Pir_Type())
pir.setMaxAccess(_D)
if mibBuilder.loadTexts:pir.setStatus(_A)
if mibBuilder.loadTexts:pir.setUnits(_J)
class _ChanLocRmtLpbkState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ChanLocRmtLpbkState_Type.__name__=_C
_ChanLocRmtLpbkState_Object=MibTableColumn
chanLocRmtLpbkState=_ChanLocRmtLpbkState_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,21),_ChanLocRmtLpbkState_Type())
chanLocRmtLpbkState.setMaxAccess(_D)
if mibBuilder.loadTexts:chanLocRmtLpbkState.setStatus(_A)
class _ChanTestType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('testcon',1),('testdelay',2),('notest',3)))
_ChanTestType_Type.__name__=_C
_ChanTestType_Object=MibTableColumn
chanTestType=_ChanTestType_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,22),_ChanTestType_Type())
chanTestType.setMaxAccess(_D)
if mibBuilder.loadTexts:chanTestType.setStatus(_A)
class _ChanTestState_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('passed',1),(_R,2),('inprogress',3),('notinprogress',4)))
_ChanTestState_Type.__name__=_C
_ChanTestState_Object=MibTableColumn
chanTestState=_ChanTestState_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,23),_ChanTestState_Type())
chanTestState.setMaxAccess(_E)
if mibBuilder.loadTexts:chanTestState.setStatus(_A)
class _ChanRTDResult_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ChanRTDResult_Type.__name__=_C
_ChanRTDResult_Object=MibTableColumn
chanRTDResult=_ChanRTDResult_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,24),_ChanRTDResult_Type())
chanRTDResult.setMaxAccess(_E)
if mibBuilder.loadTexts:chanRTDResult.setStatus(_A)
class _ChanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('frNIW',1),('frSIW-transparent',2),('frSIW-translate',3),('frFUNI',4),('frForward',5),('frNIWReplace',6)))
_ChanType_Type.__name__=_C
_ChanType_Object=MibTableColumn
chanType=_ChanType_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,25),_ChanType_Type())
chanType.setMaxAccess(_D)
if mibBuilder.loadTexts:chanType.setStatus(_A)
class _ChanFECNconfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mapEFCI',1),('setEFCIzero',2)))
_ChanFECNconfig_Type.__name__=_C
_ChanFECNconfig_Object=MibTableColumn
chanFECNconfig=_ChanFECNconfig_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,26),_ChanFECNconfig_Type())
chanFECNconfig.setMaxAccess(_D)
if mibBuilder.loadTexts:chanFECNconfig.setStatus(_A)
class _ChanDEtoCLPmap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mapCLP',1),('setCLPzero',2),('setCLPone',3)))
_ChanDEtoCLPmap_Type.__name__=_C
_ChanDEtoCLPmap_Object=MibTableColumn
chanDEtoCLPmap=_ChanDEtoCLPmap_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,27),_ChanDEtoCLPmap_Type())
chanDEtoCLPmap.setMaxAccess(_D)
if mibBuilder.loadTexts:chanDEtoCLPmap.setStatus(_A)
class _ChanCLPtoDEmap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('mapDE',1),('setDEzero',2),('setDEone',3),('ignoreCLP',4)))
_ChanCLPtoDEmap_Type.__name__=_C
_ChanCLPtoDEmap_Object=MibTableColumn
chanCLPtoDEmap=_ChanCLPtoDEmap_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,28),_ChanCLPtoDEmap_Type())
chanCLPtoDEmap.setMaxAccess(_D)
if mibBuilder.loadTexts:chanCLPtoDEmap.setStatus(_A)
class _ChanIngrPercentUtil_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ChanIngrPercentUtil_Type.__name__=_C
_ChanIngrPercentUtil_Object=MibTableColumn
chanIngrPercentUtil=_ChanIngrPercentUtil_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,29),_ChanIngrPercentUtil_Type())
chanIngrPercentUtil.setMaxAccess(_D)
if mibBuilder.loadTexts:chanIngrPercentUtil.setStatus(_A)
if mibBuilder.loadTexts:chanIngrPercentUtil.setUnits(_S)
class _ChanEgrPercentUtil_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ChanEgrPercentUtil_Type.__name__=_C
_ChanEgrPercentUtil_Object=MibTableColumn
chanEgrPercentUtil=_ChanEgrPercentUtil_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,30),_ChanEgrPercentUtil_Type())
chanEgrPercentUtil.setMaxAccess(_D)
if mibBuilder.loadTexts:chanEgrPercentUtil.setStatus(_A)
if mibBuilder.loadTexts:chanEgrPercentUtil.setUnits(_S)
class _ChanEgrSrvRate_Type(Integer32):defaultValue=2400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2400,52000000))
_ChanEgrSrvRate_Type.__name__=_C
_ChanEgrSrvRate_Object=MibTableColumn
chanEgrSrvRate=_ChanEgrSrvRate_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,31),_ChanEgrSrvRate_Type())
chanEgrSrvRate.setMaxAccess(_D)
if mibBuilder.loadTexts:chanEgrSrvRate.setStatus(_A)
class _ChanOvrSubOvrRide_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_ChanOvrSubOvrRide_Type.__name__=_C
_ChanOvrSubOvrRide_Object=MibTableColumn
chanOvrSubOvrRide=_ChanOvrSubOvrRide_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,32),_ChanOvrSubOvrRide_Type())
chanOvrSubOvrRide.setMaxAccess(_D)
if mibBuilder.loadTexts:chanOvrSubOvrRide.setStatus(_A)
class _ChanFrConnType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('pvc',1),('svc',2),('spvc',3),('par',4),('pnni',5),('tag',6)))
_ChanFrConnType_Type.__name__=_C
_ChanFrConnType_Object=MibTableColumn
chanFrConnType=_ChanFrConnType_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,33),_ChanFrConnType_Type())
chanFrConnType.setMaxAccess(_D)
if mibBuilder.loadTexts:chanFrConnType.setStatus(_A)
_FrCDRNumber_Type=Integer32
_FrCDRNumber_Object=MibTableColumn
frCDRNumber=_FrCDRNumber_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,34),_FrCDRNumber_Type())
frCDRNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:frCDRNumber.setStatus(_A)
class _FrLocalVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrLocalVpi_Type.__name__=_C
_FrLocalVpi_Object=MibTableColumn
frLocalVpi=_FrLocalVpi_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,35),_FrLocalVpi_Type())
frLocalVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:frLocalVpi.setStatus(_A)
class _FrLocalVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrLocalVci_Type.__name__=_C
_FrLocalVci_Object=MibTableColumn
frLocalVci=_FrLocalVci_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,36),_FrLocalVci_Type())
frLocalVci.setMaxAccess(_E)
if mibBuilder.loadTexts:frLocalVci.setStatus(_A)
class _FrLocalNSAP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_FrLocalNSAP_Type.__name__=_H
_FrLocalNSAP_Object=MibTableColumn
frLocalNSAP=_FrLocalNSAP_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,37),_FrLocalNSAP_Type())
frLocalNSAP.setMaxAccess(_D)
if mibBuilder.loadTexts:frLocalNSAP.setStatus(_A)
class _FrRemoteVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrRemoteVpi_Type.__name__=_C
_FrRemoteVpi_Object=MibTableColumn
frRemoteVpi=_FrRemoteVpi_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,38),_FrRemoteVpi_Type())
frRemoteVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:frRemoteVpi.setStatus(_A)
class _FrRemoteVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrRemoteVci_Type.__name__=_C
_FrRemoteVci_Object=MibTableColumn
frRemoteVci=_FrRemoteVci_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,39),_FrRemoteVci_Type())
frRemoteVci.setMaxAccess(_D)
if mibBuilder.loadTexts:frRemoteVci.setStatus(_A)
class _FrRemoteNSAP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_FrRemoteNSAP_Type.__name__=_H
_FrRemoteNSAP_Object=MibTableColumn
frRemoteNSAP=_FrRemoteNSAP_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,40),_FrRemoteNSAP_Type())
frRemoteNSAP.setMaxAccess(_D)
if mibBuilder.loadTexts:frRemoteNSAP.setStatus(_A)
class _FrMastership_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),('unknown',3)))
_FrMastership_Type.__name__=_C
_FrMastership_Object=MibTableColumn
frMastership=_FrMastership_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,41),_FrMastership_Type())
frMastership.setMaxAccess(_D)
if mibBuilder.loadTexts:frMastership.setStatus(_A)
class _FrVpcFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vpc',1),('vcc',2)))
_FrVpcFlag_Type.__name__=_C
_FrVpcFlag_Object=MibTableColumn
frVpcFlag=_FrVpcFlag_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,42),_FrVpcFlag_Type())
frVpcFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:frVpcFlag.setStatus(_A)
class _FrConnServiceType_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,28,29,30,31,32)));namedValues=NamedValues(*(('cbr',1),('vbr',2),('notUsed',3),('ubr',4),('atfr',5),('abrstd',6),('abrfst',7),('vbrrt',8),('cbr1',21),('vbr1rt',22),('vbr2rt',23),('vbr3rt',24),('vbr1nrt',25),('vbr2nrt',26),('vbr3nrt',27),('ubr1',28),('ubr2',29),('stdabr',30),('cbr2',31),('cbr3',32)))
_FrConnServiceType_Type.__name__=_C
_FrConnServiceType_Object=MibTableColumn
frConnServiceType=_FrConnServiceType_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,43),_FrConnServiceType_Type())
frConnServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:frConnServiceType.setStatus(_A)
class _FrRoutingPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_FrRoutingPriority_Type.__name__=_C
_FrRoutingPriority_Object=MibTableColumn
frRoutingPriority=_FrRoutingPriority_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,44),_FrRoutingPriority_Type())
frRoutingPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:frRoutingPriority.setStatus(_A)
class _FrMaxCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FrMaxCost_Type.__name__=_C
_FrMaxCost_Object=MibTableColumn
frMaxCost=_FrMaxCost_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,45),_FrMaxCost_Type())
frMaxCost.setMaxAccess(_D)
if mibBuilder.loadTexts:frMaxCost.setStatus(_A)
class _FrRestrictTrunkType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('norestriction',1),('terrestrialTrunk',2),('sateliteTrunk',3)))
_FrRestrictTrunkType_Type.__name__=_C
_FrRestrictTrunkType_Object=MibTableColumn
frRestrictTrunkType=_FrRestrictTrunkType_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,46),_FrRestrictTrunkType_Type())
frRestrictTrunkType.setMaxAccess(_D)
if mibBuilder.loadTexts:frRestrictTrunkType.setStatus(_A)
_FrConnPCR_Type=Integer32
_FrConnPCR_Object=MibTableColumn
frConnPCR=_FrConnPCR_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,47),_FrConnPCR_Type())
frConnPCR.setMaxAccess(_D)
if mibBuilder.loadTexts:frConnPCR.setStatus(_A)
_FrConnRemotePCR_Type=Integer32
_FrConnRemotePCR_Object=MibTableColumn
frConnRemotePCR=_FrConnRemotePCR_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,48),_FrConnRemotePCR_Type())
frConnRemotePCR.setMaxAccess(_D)
if mibBuilder.loadTexts:frConnRemotePCR.setStatus(_A)
_FrConnMCR_Type=Integer32
_FrConnMCR_Object=MibTableColumn
frConnMCR=_FrConnMCR_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,49),_FrConnMCR_Type())
frConnMCR.setMaxAccess(_D)
if mibBuilder.loadTexts:frConnMCR.setStatus(_A)
_FrConnRemoteMCR_Type=Integer32
_FrConnRemoteMCR_Object=MibTableColumn
frConnRemoteMCR=_FrConnRemoteMCR_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,50),_FrConnRemoteMCR_Type())
frConnRemoteMCR.setMaxAccess(_D)
if mibBuilder.loadTexts:frConnRemoteMCR.setStatus(_A)
class _FrConnPercentUtil_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FrConnPercentUtil_Type.__name__=_C
_FrConnPercentUtil_Object=MibTableColumn
frConnPercentUtil=_FrConnPercentUtil_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,51),_FrConnPercentUtil_Type())
frConnPercentUtil.setMaxAccess(_D)
if mibBuilder.loadTexts:frConnPercentUtil.setStatus(_A)
class _FrConnRemotePercentUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FrConnRemotePercentUtil_Type.__name__=_C
_FrConnRemotePercentUtil_Object=MibTableColumn
frConnRemotePercentUtil=_FrConnRemotePercentUtil_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,52),_FrConnRemotePercentUtil_Type())
frConnRemotePercentUtil.setMaxAccess(_D)
if mibBuilder.loadTexts:frConnRemotePercentUtil.setStatus(_A)
class _FrConnForeSightEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FrConnForeSightEnable_Type.__name__=_C
_FrConnForeSightEnable_Object=MibTableColumn
frConnForeSightEnable=_FrConnForeSightEnable_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,53),_FrConnForeSightEnable_Type())
frConnForeSightEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:frConnForeSightEnable.setStatus(_A)
class _FrConnFGCRAEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FrConnFGCRAEnable_Type.__name__=_C
_FrConnFGCRAEnable_Object=MibTableColumn
frConnFGCRAEnable=_FrConnFGCRAEnable_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,54),_FrConnFGCRAEnable_Type())
frConnFGCRAEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:frConnFGCRAEnable.setStatus(_A)
class _ChanServType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('highpriority',1),('rtVBR',2),('nrtVBR',3),('aBR',4),('uBR',5),('queue6',6),('queue7',7),('queue8',8),('stdABR',9)))
_ChanServType_Type.__name__=_C
_ChanServType_Object=MibTableColumn
chanServType=_ChanServType_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,55),_ChanServType_Type())
chanServType.setMaxAccess(_D)
if mibBuilder.loadTexts:chanServType.setStatus(_A)
class _ChanServiceRateOverride_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ChanServiceRateOverride_Type.__name__=_C
_ChanServiceRateOverride_Object=MibTableColumn
chanServiceRateOverride=_ChanServiceRateOverride_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,56),_ChanServiceRateOverride_Type())
chanServiceRateOverride.setMaxAccess(_D)
if mibBuilder.loadTexts:chanServiceRateOverride.setStatus(_A)
class _ChanServiceRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(160,6400000))
_ChanServiceRate_Type.__name__=_C
_ChanServiceRate_Object=MibTableColumn
chanServiceRate=_ChanServiceRate_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,57),_ChanServiceRate_Type())
chanServiceRate.setMaxAccess(_D)
if mibBuilder.loadTexts:chanServiceRate.setStatus(_A)
class _ZeroCirConEir_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,52000000))
_ZeroCirConEir_Type.__name__=_C
_ZeroCirConEir_Object=MibTableColumn
zeroCirConEir=_ZeroCirConEir_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,58),_ZeroCirConEir_Type())
zeroCirConEir.setMaxAccess(_D)
if mibBuilder.loadTexts:zeroCirConEir.setStatus(_A)
class _ChanReroute_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_ChanReroute_Type.__name__=_C
_ChanReroute_Object=MibTableColumn
chanReroute=_ChanReroute_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,59),_ChanReroute_Type())
chanReroute.setMaxAccess(_D)
if mibBuilder.loadTexts:chanReroute.setStatus(_A)
_FrConnSCR_Type=Integer32
_FrConnSCR_Object=MibTableColumn
frConnSCR=_FrConnSCR_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,60),_FrConnSCR_Type())
frConnSCR.setMaxAccess(_D)
if mibBuilder.loadTexts:frConnSCR.setStatus(_A)
_FrConnRemoteSCR_Type=Integer32
_FrConnRemoteSCR_Object=MibTableColumn
frConnRemoteSCR=_FrConnRemoteSCR_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,61),_FrConnRemoteSCR_Type())
frConnRemoteSCR.setMaxAccess(_D)
if mibBuilder.loadTexts:frConnRemoteSCR.setStatus(_A)
class _FrConnTemplateId_Type(Integer32):defaultValue=17;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,17))
_FrConnTemplateId_Type.__name__=_C
_FrConnTemplateId_Object=MibTableColumn
frConnTemplateId=_FrConnTemplateId_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,62),_FrConnTemplateId_Type())
frConnTemplateId.setMaxAccess(_D)
if mibBuilder.loadTexts:frConnTemplateId.setStatus(_A)
class _FrConnAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_FrConnAdminStatus_Type.__name__=_C
_FrConnAdminStatus_Object=MibTableColumn
frConnAdminStatus=_FrConnAdminStatus_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,63),_FrConnAdminStatus_Type())
frConnAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:frConnAdminStatus.setStatus(_A)
_FrChanCnfChangeCount_Type=Counter32
_FrChanCnfChangeCount_Object=MibTableColumn
frChanCnfChangeCount=_FrChanCnfChangeCount_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,64),_FrChanCnfChangeCount_Type())
frChanCnfChangeCount.setMaxAccess(_E)
if mibBuilder.loadTexts:frChanCnfChangeCount.setStatus(_A)
class _FrChanCnfIgnoreIncomingDE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FrChanCnfIgnoreIncomingDE_Type.__name__=_C
_FrChanCnfIgnoreIncomingDE_Object=MibTableColumn
frChanCnfIgnoreIncomingDE=_FrChanCnfIgnoreIncomingDE_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,65),_FrChanCnfIgnoreIncomingDE_Type())
frChanCnfIgnoreIncomingDE.setMaxAccess(_D)
if mibBuilder.loadTexts:frChanCnfIgnoreIncomingDE.setStatus(_A)
class _FrChanOamCCEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FrChanOamCCEnable_Type.__name__=_C
_FrChanOamCCEnable_Object=MibTableColumn
frChanOamCCEnable=_FrChanOamCCEnable_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,66),_FrChanOamCCEnable_Type())
frChanOamCCEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:frChanOamCCEnable.setStatus(_A)
class _FrChanStatsEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FrChanStatsEnable_Type.__name__=_C
_FrChanStatsEnable_Object=MibTableColumn
frChanStatsEnable=_FrChanStatsEnable_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,67),_FrChanStatsEnable_Type())
frChanStatsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:frChanStatsEnable.setStatus(_A)
class _FrChanLocalLpbkEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FrChanLocalLpbkEnable_Type.__name__=_C
_FrChanLocalLpbkEnable_Object=MibTableColumn
frChanLocalLpbkEnable=_FrChanLocalLpbkEnable_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,68),_FrChanLocalLpbkEnable_Type())
frChanLocalLpbkEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:frChanLocalLpbkEnable.setStatus(_A)
class _FrChanUpcEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FrChanUpcEnable_Type.__name__=_C
_FrChanUpcEnable_Object=MibTableColumn
frChanUpcEnable=_FrChanUpcEnable_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,69),_FrChanUpcEnable_Type())
frChanUpcEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:frChanUpcEnable.setStatus(_A)
class _FrChanSlaveType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('persistentSlave',1),('nonPersistentSlave',2)))
_FrChanSlaveType_Type.__name__=_C
_FrChanSlaveType_Object=MibTableColumn
frChanSlaveType=_FrChanSlaveType_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,70),_FrChanSlaveType_Type())
frChanSlaveType.setMaxAccess(_D)
if mibBuilder.loadTexts:frChanSlaveType.setStatus(_A)
class _FrConnRemoteMBS_Type(Integer32):defaultValue=1024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5000000))
_FrConnRemoteMBS_Type.__name__=_C
_FrConnRemoteMBS_Object=MibTableColumn
frConnRemoteMBS=_FrConnRemoteMBS_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,71),_FrConnRemoteMBS_Type())
frConnRemoteMBS.setMaxAccess(_D)
if mibBuilder.loadTexts:frConnRemoteMBS.setStatus(_A)
class _FrChanPrefRouteId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrChanPrefRouteId_Type.__name__=_C
_FrChanPrefRouteId_Object=MibTableColumn
frChanPrefRouteId=_FrChanPrefRouteId_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,72),_FrChanPrefRouteId_Type())
frChanPrefRouteId.setMaxAccess(_D)
if mibBuilder.loadTexts:frChanPrefRouteId.setStatus(_A)
class _FrChanDirectRoute_Type(TruthValue):defaultValue=2
_FrChanDirectRoute_Type.__name__=_Q
_FrChanDirectRoute_Object=MibTableColumn
frChanDirectRoute=_FrChanDirectRoute_Object((1,3,6,1,4,1,351,110,5,1,2,1,1,1,73),_FrChanDirectRoute_Type())
frChanDirectRoute.setMaxAccess(_D)
if mibBuilder.loadTexts:frChanDirectRoute.setStatus(_A)
class _ChanNumNextAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,2147483647))
_ChanNumNextAvailable_Type.__name__=_C
_ChanNumNextAvailable_Object=MibScalar
chanNumNextAvailable=_ChanNumNextAvailable_Object((1,3,6,1,4,1,351,110,5,1,2,1,2),_ChanNumNextAvailable_Type())
chanNumNextAvailable.setMaxAccess(_E)
if mibBuilder.loadTexts:chanNumNextAvailable.setStatus(_A)
_FrstdABRCnfGrpTable_Object=MibTable
frstdABRCnfGrpTable=_FrstdABRCnfGrpTable_Object((1,3,6,1,4,1,351,110,5,1,2,1,3))
if mibBuilder.loadTexts:frstdABRCnfGrpTable.setStatus(_A)
_FrstdABRCnfGrpEntry_Object=MibTableRow
frstdABRCnfGrpEntry=_FrstdABRCnfGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,2,1,3,1))
frstdABRCnfGrpEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:frstdABRCnfGrpEntry.setStatus(_A)
class _FrstdABRcnfChanNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FrstdABRcnfChanNum_Type.__name__=_C
_FrstdABRcnfChanNum_Object=MibTableColumn
frstdABRcnfChanNum=_FrstdABRcnfChanNum_Object((1,3,6,1,4,1,351,110,5,1,2,1,3,1,1),_FrstdABRcnfChanNum_Type())
frstdABRcnfChanNum.setMaxAccess(_E)
if mibBuilder.loadTexts:frstdABRcnfChanNum.setStatus(_A)
class _FrstdABRTBE_Type(Integer32):defaultValue=16777215;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_FrstdABRTBE_Type.__name__=_C
_FrstdABRTBE_Object=MibTableColumn
frstdABRTBE=_FrstdABRTBE_Object((1,3,6,1,4,1,351,110,5,1,2,1,3,1,2),_FrstdABRTBE_Type())
frstdABRTBE.setMaxAccess(_D)
if mibBuilder.loadTexts:frstdABRTBE.setStatus(_A)
if mibBuilder.loadTexts:frstdABRTBE.setUnits('cells')
class _FrstdABRFRTT_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16700))
_FrstdABRFRTT_Type.__name__=_C
_FrstdABRFRTT_Object=MibTableColumn
frstdABRFRTT=_FrstdABRFRTT_Object((1,3,6,1,4,1,351,110,5,1,2,1,3,1,3),_FrstdABRFRTT_Type())
frstdABRFRTT.setMaxAccess(_D)
if mibBuilder.loadTexts:frstdABRFRTT.setStatus(_A)
if mibBuilder.loadTexts:frstdABRFRTT.setUnits(_L)
class _FrstdABRRDF_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32768))
_FrstdABRRDF_Type.__name__=_C
_FrstdABRRDF_Object=MibTableColumn
frstdABRRDF=_FrstdABRRDF_Object((1,3,6,1,4,1,351,110,5,1,2,1,3,1,4),_FrstdABRRDF_Type())
frstdABRRDF.setMaxAccess(_D)
if mibBuilder.loadTexts:frstdABRRDF.setStatus(_A)
class _FrstdABRRIF_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32768))
_FrstdABRRIF_Type.__name__=_C
_FrstdABRRIF_Object=MibTableColumn
frstdABRRIF=_FrstdABRRIF_Object((1,3,6,1,4,1,351,110,5,1,2,1,3,1,5),_FrstdABRRIF_Type())
frstdABRRIF.setMaxAccess(_D)
if mibBuilder.loadTexts:frstdABRRIF.setStatus(_A)
class _FrstdABRNrm_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,256))
_FrstdABRNrm_Type.__name__=_C
_FrstdABRNrm_Object=MibTableColumn
frstdABRNrm=_FrstdABRNrm_Object((1,3,6,1,4,1,351,110,5,1,2,1,3,1,6),_FrstdABRNrm_Type())
frstdABRNrm.setMaxAccess(_D)
if mibBuilder.loadTexts:frstdABRNrm.setStatus(_A)
class _FrstdABRTrm_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,255))
_FrstdABRTrm_Type.__name__=_C
_FrstdABRTrm_Object=MibTableColumn
frstdABRTrm=_FrstdABRTrm_Object((1,3,6,1,4,1,351,110,5,1,2,1,3,1,7),_FrstdABRTrm_Type())
frstdABRTrm.setMaxAccess(_D)
if mibBuilder.loadTexts:frstdABRTrm.setStatus(_A)
if mibBuilder.loadTexts:frstdABRTrm.setUnits(_L)
class _FrstdABRCDF_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_FrstdABRCDF_Type.__name__=_C
_FrstdABRCDF_Object=MibTableColumn
frstdABRCDF=_FrstdABRCDF_Object((1,3,6,1,4,1,351,110,5,1,2,1,3,1,8),_FrstdABRCDF_Type())
frstdABRCDF.setMaxAccess(_D)
if mibBuilder.loadTexts:frstdABRCDF.setStatus(_A)
class _FrstdABRADTF_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10230))
_FrstdABRADTF_Type.__name__=_C
_FrstdABRADTF_Object=MibTableColumn
frstdABRADTF=_FrstdABRADTF_Object((1,3,6,1,4,1,351,110,5,1,2,1,3,1,9),_FrstdABRADTF_Type())
frstdABRADTF.setMaxAccess(_D)
if mibBuilder.loadTexts:frstdABRADTF.setStatus(_A)
if mibBuilder.loadTexts:frstdABRADTF.setUnits(_L)
class _FrstdABRICR_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,400000))
_FrstdABRICR_Type.__name__=_C
_FrstdABRICR_Object=MibTableColumn
frstdABRICR=_FrstdABRICR_Object((1,3,6,1,4,1,351,110,5,1,2,1,3,1,10),_FrstdABRICR_Type())
frstdABRICR.setMaxAccess(_D)
if mibBuilder.loadTexts:frstdABRICR.setStatus(_A)
if mibBuilder.loadTexts:frstdABRICR.setUnits(_M)
class _FrstdABRMCR_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,400000))
_FrstdABRMCR_Type.__name__=_C
_FrstdABRMCR_Object=MibTableColumn
frstdABRMCR=_FrstdABRMCR_Object((1,3,6,1,4,1,351,110,5,1,2,1,3,1,11),_FrstdABRMCR_Type())
frstdABRMCR.setMaxAccess(_D)
if mibBuilder.loadTexts:frstdABRMCR.setStatus(_A)
if mibBuilder.loadTexts:frstdABRMCR.setUnits(_M)
class _FrstdABRPCR_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,400000))
_FrstdABRPCR_Type.__name__=_C
_FrstdABRPCR_Object=MibTableColumn
frstdABRPCR=_FrstdABRPCR_Object((1,3,6,1,4,1,351,110,5,1,2,1,3,1,12),_FrstdABRPCR_Type())
frstdABRPCR.setMaxAccess(_D)
if mibBuilder.loadTexts:frstdABRPCR.setStatus(_A)
if mibBuilder.loadTexts:frstdABRPCR.setUnits(_M)
_FrChanStateGrp_ObjectIdentity=ObjectIdentity
frChanStateGrp=_FrChanStateGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,1,2,2))
_FrChanStateGrpTable_Object=MibTable
frChanStateGrpTable=_FrChanStateGrpTable_Object((1,3,6,1,4,1,351,110,5,1,2,2,1))
if mibBuilder.loadTexts:frChanStateGrpTable.setStatus(_A)
_FrChanStateGrpEntry_Object=MibTableRow
frChanStateGrpEntry=_FrChanStateGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,2,2,1,1))
frChanStateGrpEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:frChanStateGrpEntry.setStatus(_A)
class _StateChanNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_StateChanNum_Type.__name__=_C
_StateChanNum_Object=MibTableColumn
stateChanNum=_StateChanNum_Object((1,3,6,1,4,1,351,110,5,1,2,2,1,1,1),_StateChanNum_Type())
stateChanNum.setMaxAccess(_E)
if mibBuilder.loadTexts:stateChanNum.setStatus(_A)
class _ChanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notConfigured',1),('okay',2),('alarm',3),(_R,4)))
_ChanState_Type.__name__=_C
_ChanState_Object=MibTableColumn
chanState=_ChanState_Object((1,3,6,1,4,1,351,110,5,1,2,2,1,1,2),_ChanState_Type())
chanState.setMaxAccess(_E)
if mibBuilder.loadTexts:chanState.setStatus(_A)
class _XmtAbitState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('sendingAequal1',2),('sendingAequal0',3)))
_XmtAbitState_Type.__name__=_C
_XmtAbitState_Object=MibTableColumn
xmtAbitState=_XmtAbitState_Object((1,3,6,1,4,1,351,110,5,1,2,2,1,1,3),_XmtAbitState_Type())
xmtAbitState.setMaxAccess(_E)
if mibBuilder.loadTexts:xmtAbitState.setStatus(_A)
class _RcvAbitState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('rcvingAequal1',2),('rcvingAequal0',3)))
_RcvAbitState_Type.__name__=_C
_RcvAbitState_Object=MibTableColumn
rcvAbitState=_RcvAbitState_Object((1,3,6,1,4,1,351,110,5,1,2,2,1,1,4),_RcvAbitState_Type())
rcvAbitState.setMaxAccess(_E)
if mibBuilder.loadTexts:rcvAbitState.setStatus(_A)
class _XmtATMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notSending',1),('sendingAIS',2),('sendingFERF',3)))
_XmtATMState_Type.__name__=_C
_XmtATMState_Object=MibTableColumn
xmtATMState=_XmtATMState_Object((1,3,6,1,4,1,351,110,5,1,2,2,1,1,5),_XmtATMState_Type())
xmtATMState.setMaxAccess(_E)
if mibBuilder.loadTexts:xmtATMState.setStatus(_A)
class _RcvATMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notRcving',1),('rcvingAIS',2),('rcvingFERF',3)))
_RcvATMState_Type.__name__=_C
_RcvATMState_Object=MibTableColumn
rcvATMState=_RcvATMState_Object((1,3,6,1,4,1,351,110,5,1,2,2,1,1,6),_RcvATMState_Type())
rcvATMState.setMaxAccess(_E)
if mibBuilder.loadTexts:rcvATMState.setStatus(_A)
class _ChanStatusBitMap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ChanStatusBitMap_Type.__name__=_C
_ChanStatusBitMap_Object=MibTableColumn
chanStatusBitMap=_ChanStatusBitMap_Object((1,3,6,1,4,1,351,110,5,1,2,2,1,1,7),_ChanStatusBitMap_Type())
chanStatusBitMap.setMaxAccess(_E)
if mibBuilder.loadTexts:chanStatusBitMap.setStatus(_A)
_FrEndPtMapGrp_ObjectIdentity=ObjectIdentity
frEndPtMapGrp=_FrEndPtMapGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,1,3))
_FrEndPtMapGrpTable_Object=MibTable
frEndPtMapGrpTable=_FrEndPtMapGrpTable_Object((1,3,6,1,4,1,351,110,5,1,3,1))
if mibBuilder.loadTexts:frEndPtMapGrpTable.setStatus(_A)
_FrEndPtMapGrpEntry_Object=MibTableRow
frEndPtMapGrpEntry=_FrEndPtMapGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,3,1,1))
frEndPtMapGrpEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:frEndPtMapGrpEntry.setStatus(_A)
class _EndPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EndPortNum_Type.__name__=_C
_EndPortNum_Object=MibTableColumn
endPortNum=_EndPortNum_Object((1,3,6,1,4,1,351,110,5,1,3,1,1,1),_EndPortNum_Type())
endPortNum.setMaxAccess(_E)
if mibBuilder.loadTexts:endPortNum.setStatus(_A)
class _EndDLCI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8388607))
_EndDLCI_Type.__name__=_C
_EndDLCI_Object=MibTableColumn
endDLCI=_EndDLCI_Object((1,3,6,1,4,1,351,110,5,1,3,1,1,2),_EndDLCI_Type())
endDLCI.setMaxAccess(_E)
if mibBuilder.loadTexts:endDLCI.setStatus(_A)
class _EndChanNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EndChanNum_Type.__name__=_C
_EndChanNum_Object=MibTableColumn
endChanNum=_EndChanNum_Object((1,3,6,1,4,1,351,110,5,1,3,1,1,3),_EndChanNum_Type())
endChanNum.setMaxAccess(_E)
if mibBuilder.loadTexts:endChanNum.setStatus(_A)
class _EndLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EndLineNum_Type.__name__=_C
_EndLineNum_Object=MibTableColumn
endLineNum=_EndLineNum_Object((1,3,6,1,4,1,351,110,5,1,3,1,1,4),_EndLineNum_Type())
endLineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:endLineNum.setStatus(_A)
_CiscoWanFrConnMIBConformance_ObjectIdentity=ObjectIdentity
ciscoWanFrConnMIBConformance=_CiscoWanFrConnMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,47,2))
_CiscoWanFrConnMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWanFrConnMIBGroups=_CiscoWanFrConnMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,47,2,1))
_CiscoWanFrConnMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWanFrConnMIBCompliances=_CiscoWanFrConnMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,47,2,2))
ciscoWanFrConnGroup=ObjectGroup((1,3,6,1,4,1,351,150,47,2,1,1))
ciscoWanFrConnGroup.setObjects(*((_B,_I),(_B,_T),(_B,_U),(_B,'dLCI'),(_B,_V),(_B,_W),(_B,'cir'),(_B,'bc'),(_B,'be'),(_B,'ibs'),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:ciscoWanFrConnGroup.setStatus(_A)
ciscoWanFrConnForesightGroup=ObjectGroup((1,3,6,1,4,1,351,150,47,2,1,2))
ciscoWanFrConnForesightGroup.setObjects(*((_B,_AM),(_B,'qir'),(_B,'mir'),(_B,'pir')))
if mibBuilder.loadTexts:ciscoWanFrConnForesightGroup.setStatus(_A)
ciscoWanFrConnQueueGroup=ObjectGroup((1,3,6,1,4,1,351,150,47,2,1,3))
ciscoWanFrConnQueueGroup.setObjects(*((_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:ciscoWanFrConnQueueGroup.setStatus(_A)
ciscoWanFrConnTestGroup=ObjectGroup((1,3,6,1,4,1,351,150,47,2,1,4))
ciscoWanFrConnTestGroup.setObjects(*((_B,_AT),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:ciscoWanFrConnTestGroup.setStatus(_A)
ciscoWanFrConnStateGroup=ObjectGroup((1,3,6,1,4,1,351,150,47,2,1,5))
ciscoWanFrConnStateGroup.setObjects(*((_B,_N),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab)))
if mibBuilder.loadTexts:ciscoWanFrConnStateGroup.setStatus(_A)
ciscoWanFrConnEndptGroup=ObjectGroup((1,3,6,1,4,1,351,150,47,2,1,6))
ciscoWanFrConnEndptGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:ciscoWanFrConnEndptGroup.setStatus(_A)
ciscoWanFrConnABRGroup=ObjectGroup((1,3,6,1,4,1,351,150,47,2,1,7))
ciscoWanFrConnABRGroup.setObjects(*((_B,_K),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao)))
if mibBuilder.loadTexts:ciscoWanFrConnABRGroup.setStatus(_A)
ciscoWanFrConnCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,47,2,2,1))
ciscoWanFrConnCompliance.setObjects(*((_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av)))
if mibBuilder.loadTexts:ciscoWanFrConnCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'frChanCnfGrp':frChanCnfGrp,'frChanCnfGrpTable':frChanCnfGrpTable,'frChanCnfGrpEntry':frChanCnfGrpEntry,_I:chanNum,_T:chanRowStatus,_U:chanPortNum,'dLCI':dLCI,_V:egressQSelect,_AN:ingressQDepth,_AP:ingressQECNThresh,_AO:ingressQDEThresh,_AQ:egressQDepth,_AR:egressQDEThresh,_AS:egressQECNThresh,_W:deTaggingEnable,'cir':cir,'bc':bc,'be':be,'ibs':ibs,_AM:foreSightEnable,'qir':qir,'mir':mir,'pir':pir,_X:chanLocRmtLpbkState,_AT:chanTestType,_AU:chanTestState,_AV:chanRTDResult,_Y:chanType,_Z:chanFECNconfig,_a:chanDEtoCLPmap,_b:chanCLPtoDEmap,_c:chanIngrPercentUtil,_d:chanEgrPercentUtil,_e:chanEgrSrvRate,_f:chanOvrSubOvrRide,_g:chanFrConnType,_h:frCDRNumber,_i:frLocalVpi,_j:frLocalVci,_k:frLocalNSAP,_l:frRemoteVpi,_m:frRemoteVci,_n:frRemoteNSAP,_o:frMastership,_p:frVpcFlag,_q:frConnServiceType,_r:frRoutingPriority,_s:frMaxCost,_t:frRestrictTrunkType,_u:frConnPCR,_v:frConnRemotePCR,_w:frConnMCR,_x:frConnRemoteMCR,_y:frConnPercentUtil,_z:frConnRemotePercentUtil,_A0:frConnForeSightEnable,_A1:frConnFGCRAEnable,_A2:chanServType,_A3:chanServiceRateOverride,_A4:chanServiceRate,_A5:zeroCirConEir,_A6:chanReroute,_A7:frConnSCR,_A8:frConnRemoteSCR,_A9:frConnTemplateId,_AA:frConnAdminStatus,_AB:frChanCnfChangeCount,_AC:frChanCnfIgnoreIncomingDE,_AD:frChanOamCCEnable,_AE:frChanStatsEnable,_AF:frChanLocalLpbkEnable,_AG:frChanUpcEnable,_AH:frChanSlaveType,_AI:frConnRemoteMBS,_AK:frChanPrefRouteId,_AL:frChanDirectRoute,_AJ:chanNumNextAvailable,'frstdABRCnfGrpTable':frstdABRCnfGrpTable,'frstdABRCnfGrpEntry':frstdABRCnfGrpEntry,_K:frstdABRcnfChanNum,_Ae:frstdABRTBE,_Af:frstdABRFRTT,_Ag:frstdABRRDF,_Ah:frstdABRRIF,_Ai:frstdABRNrm,_Aj:frstdABRTrm,_Ak:frstdABRCDF,_Al:frstdABRADTF,_Am:frstdABRICR,_An:frstdABRMCR,_Ao:frstdABRPCR,'frChanStateGrp':frChanStateGrp,'frChanStateGrpTable':frChanStateGrpTable,'frChanStateGrpEntry':frChanStateGrpEntry,_N:stateChanNum,_AW:chanState,_AX:xmtAbitState,_AY:rcvAbitState,_AZ:xmtATMState,_Aa:rcvATMState,_Ab:chanStatusBitMap,'frEndPtMapGrp':frEndPtMapGrp,'frEndPtMapGrpTable':frEndPtMapGrpTable,'frEndPtMapGrpEntry':frEndPtMapGrpEntry,_O:endPortNum,_P:endDLCI,_Ac:endChanNum,_Ad:endLineNum,'ciscoWanFrConnMIB':ciscoWanFrConnMIB,'ciscoWanFrConnMIBConformance':ciscoWanFrConnMIBConformance,'ciscoWanFrConnMIBGroups':ciscoWanFrConnMIBGroups,_Ap:ciscoWanFrConnGroup,_Au:ciscoWanFrConnForesightGroup,_Av:ciscoWanFrConnQueueGroup,_Aq:ciscoWanFrConnTestGroup,_Ar:ciscoWanFrConnStateGroup,_As:ciscoWanFrConnEndptGroup,_At:ciscoWanFrConnABRGroup,'ciscoWanFrConnMIBCompliances':ciscoWanFrConnMIBCompliances,'ciscoWanFrConnCompliance':ciscoWanFrConnCompliance})