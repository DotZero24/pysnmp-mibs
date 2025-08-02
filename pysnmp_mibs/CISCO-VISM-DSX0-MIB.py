_AR='ciscoVismDsx0ConfGroup2'
_AQ='ciscoVismDsx0ConfGroup'
_AP='ds0TxRxCasConfig'
_AO='ds0TxCasTransTblName'
_AN='ds0RxCasTransTblName'
_AM='ds0Companding'
_AL='ds0TransmitCodesEnable'
_AK='ds0ChanMapIfIndex'
_AJ='ds0StatusClrButton'
_AI='ds0Status'
_AH='lineStatsClrButton'
_AG='lineActiveHighWaterMark'
_AF='lineBlockDs0Count'
_AE='lineActiveDs0Count'
_AD='lineFreeDs0Count'
_AC='lineTotalDs0Count'
_AB='vismDs0CardStatsClrButton'
_AA='vismActiveHighWaterMark'
_A9='vismBlockDs0Count'
_A8='vismActiveDs0Count'
_A7='vismFreeDs0Count'
_A6='vismTotalDs0Count'
_A5='dB - decibel'
_A4='bidirectional'
_A3='ciscoVismCardStatsGroup'
_A2='ciscoVismDsx0ChanMapGroup'
_A1='ciscoVismDsx0StatusGroup'
_A0='ciscoVismDsx0LineStatsGroup'
_z='ds0ExecDiag'
_y='ds0SidPacket'
_x='ds0MusicThreshold'
_w='ds0OutputAttenuation'
_v='ds0InputGain'
_u='ds0CasOutgoingMgcpPackage'
_t='ds0CasIncomingMgcpPackage'
_s='ds0CasGlarePolicy'
_r='ds0CasDirectionality'
_q='ds0CasFlashMaxMakeTime'
_p='ds0CasFlashMinMakeTime'
_o='ds0CasMinStartDialTime'
_n='ds0CasMinDelayDialTime'
_m='ds0SignalingType'
_l='ds0CasDelayImmedStart'
_k='ds0CasGaurdTime'
_j='ds0CasGlareTime'
_i='ds0CasWinkBreakTime'
_h='ds0CasWinkMaxMakeTime'
_g='ds0CasWinkMinMakeTime'
_f='ds0CasOffHookMinMakeTime'
_e='ds0CasOnHookMinMakeTime'
_d='ds0CasParameterSource'
_c='ds0LoopbackCommand'
_b='ds0LocalCasPattern'
_a='ds0InsertLocalCas'
_Z='ds0CasCadenceOffTime'
_Y='ds0CasCadenceOnTime'
_X='ds0CasVariantName'
_W='ds0IfType'
_V='ds0BundleMapped'
_U='ds0ReceivedCode'
_T='ds0SeizedCode'
_S='ds0IdleCode'
_R='ds0RobbedBitSignalling'
_Q='ds0Number'
_P='ds0LineNumber'
_O='ds0LineNum'
_N='ds0ChanNum'
_M='dsx1LineNum'
_L='clear'
_K='noaction'
_J='deprecated'
_I='ds0IfIndex'
_H='DisplayString'
_G='TruthValue'
_F='milliseconds'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='current'
_A='CISCO-VISM-DSX0-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cardSpecific,dsx0Vism=mibBuilder.importSymbols('BASIS-MIB','cardSpecific','dsx0Vism')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention',_G)
ciscoVismDsx0MIB=ModuleIdentity((1,3,6,1,4,1,351,150,81))
if mibBuilder.loadTexts:ciscoVismDsx0MIB.setRevisions(('2004-03-11 00:00','2003-08-03 00:00','2003-06-17 00:00'))
_VismDs0CardStats_ObjectIdentity=ObjectIdentity
vismDs0CardStats=_VismDs0CardStats_ObjectIdentity((1,3,6,1,4,1,351,110,3,24))
class _VismTotalDs0Count_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismTotalDs0Count_Type.__name__=_C
_VismTotalDs0Count_Object=MibScalar
vismTotalDs0Count=_VismTotalDs0Count_Object((1,3,6,1,4,1,351,110,3,24,1),_VismTotalDs0Count_Type())
vismTotalDs0Count.setMaxAccess(_E)
if mibBuilder.loadTexts:vismTotalDs0Count.setStatus(_B)
class _VismFreeDs0Count_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismFreeDs0Count_Type.__name__=_C
_VismFreeDs0Count_Object=MibScalar
vismFreeDs0Count=_VismFreeDs0Count_Object((1,3,6,1,4,1,351,110,3,24,2),_VismFreeDs0Count_Type())
vismFreeDs0Count.setMaxAccess(_E)
if mibBuilder.loadTexts:vismFreeDs0Count.setStatus(_B)
class _VismActiveDs0Count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismActiveDs0Count_Type.__name__=_C
_VismActiveDs0Count_Object=MibScalar
vismActiveDs0Count=_VismActiveDs0Count_Object((1,3,6,1,4,1,351,110,3,24,3),_VismActiveDs0Count_Type())
vismActiveDs0Count.setMaxAccess(_E)
if mibBuilder.loadTexts:vismActiveDs0Count.setStatus(_B)
class _VismBlockDs0Count_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismBlockDs0Count_Type.__name__=_C
_VismBlockDs0Count_Object=MibScalar
vismBlockDs0Count=_VismBlockDs0Count_Object((1,3,6,1,4,1,351,110,3,24,4),_VismBlockDs0Count_Type())
vismBlockDs0Count.setMaxAccess(_E)
if mibBuilder.loadTexts:vismBlockDs0Count.setStatus(_B)
class _VismActiveHighWaterMark_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismActiveHighWaterMark_Type.__name__=_C
_VismActiveHighWaterMark_Object=MibScalar
vismActiveHighWaterMark=_VismActiveHighWaterMark_Object((1,3,6,1,4,1,351,110,3,24,5),_VismActiveHighWaterMark_Type())
vismActiveHighWaterMark.setMaxAccess(_E)
if mibBuilder.loadTexts:vismActiveHighWaterMark.setStatus(_B)
class _VismDs0CardStatsClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_VismDs0CardStatsClrButton_Type.__name__=_C
_VismDs0CardStatsClrButton_Object=MibScalar
vismDs0CardStatsClrButton=_VismDs0CardStatsClrButton_Object((1,3,6,1,4,1,351,110,3,24,6),_VismDs0CardStatsClrButton_Type())
vismDs0CardStatsClrButton.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDs0CardStatsClrButton.setStatus(_B)
_Dsx0VismCnfTable_Object=MibTable
dsx0VismCnfTable=_Dsx0VismCnfTable_Object((1,3,6,1,4,1,351,110,4,7,1))
if mibBuilder.loadTexts:dsx0VismCnfTable.setStatus(_B)
_Dsx0VismCnfEntry_Object=MibTableRow
dsx0VismCnfEntry=_Dsx0VismCnfEntry_Object((1,3,6,1,4,1,351,110,4,7,1,1))
dsx0VismCnfEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:dsx0VismCnfEntry.setStatus(_B)
class _Ds0IfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,248))
_Ds0IfIndex_Type.__name__=_C
_Ds0IfIndex_Object=MibTableColumn
ds0IfIndex=_Ds0IfIndex_Object((1,3,6,1,4,1,351,110,4,7,1,1,1),_Ds0IfIndex_Type())
ds0IfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ds0IfIndex.setStatus(_B)
_Ds0RobbedBitSignalling_Type=TruthValue
_Ds0RobbedBitSignalling_Object=MibTableColumn
ds0RobbedBitSignalling=_Ds0RobbedBitSignalling_Object((1,3,6,1,4,1,351,110,4,7,1,1,2),_Ds0RobbedBitSignalling_Type())
ds0RobbedBitSignalling.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0RobbedBitSignalling.setStatus(_B)
class _Ds0IdleCode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Ds0IdleCode_Type.__name__=_C
_Ds0IdleCode_Object=MibTableColumn
ds0IdleCode=_Ds0IdleCode_Object((1,3,6,1,4,1,351,110,4,7,1,1,3),_Ds0IdleCode_Type())
ds0IdleCode.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0IdleCode.setStatus(_B)
class _Ds0SeizedCode_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Ds0SeizedCode_Type.__name__=_C
_Ds0SeizedCode_Object=MibTableColumn
ds0SeizedCode=_Ds0SeizedCode_Object((1,3,6,1,4,1,351,110,4,7,1,1,4),_Ds0SeizedCode_Type())
ds0SeizedCode.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0SeizedCode.setStatus(_B)
class _Ds0ReceivedCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Ds0ReceivedCode_Type.__name__=_C
_Ds0ReceivedCode_Object=MibTableColumn
ds0ReceivedCode=_Ds0ReceivedCode_Object((1,3,6,1,4,1,351,110,4,7,1,1,5),_Ds0ReceivedCode_Type())
ds0ReceivedCode.setMaxAccess(_E)
if mibBuilder.loadTexts:ds0ReceivedCode.setStatus(_B)
class _Ds0TransmitCodesEnable_Type(TruthValue):defaultValue=1
_Ds0TransmitCodesEnable_Type.__name__=_G
_Ds0TransmitCodesEnable_Object=MibTableColumn
ds0TransmitCodesEnable=_Ds0TransmitCodesEnable_Object((1,3,6,1,4,1,351,110,4,7,1,1,6),_Ds0TransmitCodesEnable_Type())
ds0TransmitCodesEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ds0TransmitCodesEnable.setStatus(_J)
class _Ds0BundleMapped_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_Ds0BundleMapped_Type.__name__=_C
_Ds0BundleMapped_Object=MibTableColumn
ds0BundleMapped=_Ds0BundleMapped_Object((1,3,6,1,4,1,351,110,4,7,1,1,7),_Ds0BundleMapped_Type())
ds0BundleMapped.setMaxAccess(_E)
if mibBuilder.loadTexts:ds0BundleMapped.setStatus(_B)
class _Ds0IfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,63,81)));namedValues=NamedValues(*(('unknown',1),('ccs-signaling',63),('bearer',81)))
_Ds0IfType_Type.__name__=_C
_Ds0IfType_Object=MibTableColumn
ds0IfType=_Ds0IfType_Object((1,3,6,1,4,1,351,110,4,7,1,1,8),_Ds0IfType_Type())
ds0IfType.setMaxAccess(_E)
if mibBuilder.loadTexts:ds0IfType.setStatus(_B)
class _Ds0CasVariantName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Ds0CasVariantName_Type.__name__=_H
_Ds0CasVariantName_Object=MibTableColumn
ds0CasVariantName=_Ds0CasVariantName_Object((1,3,6,1,4,1,351,110,4,7,1,1,9),_Ds0CasVariantName_Type())
ds0CasVariantName.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasVariantName.setStatus(_B)
class _Ds0CasCadenceOnTime_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,9999))
_Ds0CasCadenceOnTime_Type.__name__=_C
_Ds0CasCadenceOnTime_Object=MibTableColumn
ds0CasCadenceOnTime=_Ds0CasCadenceOnTime_Object((1,3,6,1,4,1,351,110,4,7,1,1,10),_Ds0CasCadenceOnTime_Type())
ds0CasCadenceOnTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasCadenceOnTime.setStatus(_B)
class _Ds0CasCadenceOffTime_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_Ds0CasCadenceOffTime_Type.__name__=_C
_Ds0CasCadenceOffTime_Object=MibTableColumn
ds0CasCadenceOffTime=_Ds0CasCadenceOffTime_Object((1,3,6,1,4,1,351,110,4,7,1,1,11),_Ds0CasCadenceOffTime_Type())
ds0CasCadenceOffTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasCadenceOffTime.setStatus(_B)
class _Ds0InsertLocalCas_Type(TruthValue):defaultValue=2
_Ds0InsertLocalCas_Type.__name__=_G
_Ds0InsertLocalCas_Object=MibTableColumn
ds0InsertLocalCas=_Ds0InsertLocalCas_Object((1,3,6,1,4,1,351,110,4,7,1,1,12),_Ds0InsertLocalCas_Type())
ds0InsertLocalCas.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0InsertLocalCas.setStatus(_B)
class _Ds0LocalCasPattern_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Ds0LocalCasPattern_Type.__name__=_C
_Ds0LocalCasPattern_Object=MibTableColumn
ds0LocalCasPattern=_Ds0LocalCasPattern_Object((1,3,6,1,4,1,351,110,4,7,1,1,13),_Ds0LocalCasPattern_Type())
ds0LocalCasPattern.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0LocalCasPattern.setStatus(_B)
class _Ds0LoopbackCommand_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noLoop',1),('remoteLoop',2),('localLoop',3)))
_Ds0LoopbackCommand_Type.__name__=_C
_Ds0LoopbackCommand_Object=MibTableColumn
ds0LoopbackCommand=_Ds0LoopbackCommand_Object((1,3,6,1,4,1,351,110,4,7,1,1,14),_Ds0LoopbackCommand_Type())
ds0LoopbackCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0LoopbackCommand.setStatus(_B)
class _Ds0CasParameterSource_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('casAppl',1),('mibValue',2)))
_Ds0CasParameterSource_Type.__name__=_C
_Ds0CasParameterSource_Object=MibTableColumn
ds0CasParameterSource=_Ds0CasParameterSource_Object((1,3,6,1,4,1,351,110,4,7,1,1,15),_Ds0CasParameterSource_Type())
ds0CasParameterSource.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasParameterSource.setStatus(_B)
class _Ds0CasOnHookMinMakeTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Ds0CasOnHookMinMakeTime_Type.__name__=_C
_Ds0CasOnHookMinMakeTime_Object=MibTableColumn
ds0CasOnHookMinMakeTime=_Ds0CasOnHookMinMakeTime_Object((1,3,6,1,4,1,351,110,4,7,1,1,16),_Ds0CasOnHookMinMakeTime_Type())
ds0CasOnHookMinMakeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasOnHookMinMakeTime.setStatus(_B)
if mibBuilder.loadTexts:ds0CasOnHookMinMakeTime.setUnits(_F)
class _Ds0CasOffHookMinMakeTime_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Ds0CasOffHookMinMakeTime_Type.__name__=_C
_Ds0CasOffHookMinMakeTime_Object=MibTableColumn
ds0CasOffHookMinMakeTime=_Ds0CasOffHookMinMakeTime_Object((1,3,6,1,4,1,351,110,4,7,1,1,17),_Ds0CasOffHookMinMakeTime_Type())
ds0CasOffHookMinMakeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasOffHookMinMakeTime.setStatus(_B)
if mibBuilder.loadTexts:ds0CasOffHookMinMakeTime.setUnits(_F)
class _Ds0CasWinkMinMakeTime_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Ds0CasWinkMinMakeTime_Type.__name__=_C
_Ds0CasWinkMinMakeTime_Object=MibTableColumn
ds0CasWinkMinMakeTime=_Ds0CasWinkMinMakeTime_Object((1,3,6,1,4,1,351,110,4,7,1,1,18),_Ds0CasWinkMinMakeTime_Type())
ds0CasWinkMinMakeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasWinkMinMakeTime.setStatus(_B)
if mibBuilder.loadTexts:ds0CasWinkMinMakeTime.setUnits(_F)
class _Ds0CasWinkMaxMakeTime_Type(Integer32):defaultValue=350;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Ds0CasWinkMaxMakeTime_Type.__name__=_C
_Ds0CasWinkMaxMakeTime_Object=MibTableColumn
ds0CasWinkMaxMakeTime=_Ds0CasWinkMaxMakeTime_Object((1,3,6,1,4,1,351,110,4,7,1,1,19),_Ds0CasWinkMaxMakeTime_Type())
ds0CasWinkMaxMakeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasWinkMaxMakeTime.setStatus(_B)
if mibBuilder.loadTexts:ds0CasWinkMaxMakeTime.setUnits('millisesconds')
class _Ds0CasWinkBreakTime_Type(Integer32):defaultValue=70;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Ds0CasWinkBreakTime_Type.__name__=_C
_Ds0CasWinkBreakTime_Object=MibTableColumn
ds0CasWinkBreakTime=_Ds0CasWinkBreakTime_Object((1,3,6,1,4,1,351,110,4,7,1,1,20),_Ds0CasWinkBreakTime_Type())
ds0CasWinkBreakTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasWinkBreakTime.setStatus(_B)
if mibBuilder.loadTexts:ds0CasWinkBreakTime.setUnits(_F)
class _Ds0CasGlareTime_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Ds0CasGlareTime_Type.__name__=_C
_Ds0CasGlareTime_Object=MibTableColumn
ds0CasGlareTime=_Ds0CasGlareTime_Object((1,3,6,1,4,1,351,110,4,7,1,1,21),_Ds0CasGlareTime_Type())
ds0CasGlareTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasGlareTime.setStatus(_B)
if mibBuilder.loadTexts:ds0CasGlareTime.setUnits(_F)
class _Ds0CasGaurdTime_Type(Integer32):defaultValue=800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Ds0CasGaurdTime_Type.__name__=_C
_Ds0CasGaurdTime_Object=MibTableColumn
ds0CasGaurdTime=_Ds0CasGaurdTime_Object((1,3,6,1,4,1,351,110,4,7,1,1,22),_Ds0CasGaurdTime_Type())
ds0CasGaurdTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasGaurdTime.setStatus(_B)
if mibBuilder.loadTexts:ds0CasGaurdTime.setUnits(_F)
class _Ds0CasDelayImmedStart_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Ds0CasDelayImmedStart_Type.__name__=_C
_Ds0CasDelayImmedStart_Object=MibTableColumn
ds0CasDelayImmedStart=_Ds0CasDelayImmedStart_Object((1,3,6,1,4,1,351,110,4,7,1,1,23),_Ds0CasDelayImmedStart_Type())
ds0CasDelayImmedStart.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasDelayImmedStart.setStatus(_B)
if mibBuilder.loadTexts:ds0CasDelayImmedStart.setUnits(_F)
class _Ds0SignalingType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cas',1),('ccs',2),('none',3)))
_Ds0SignalingType_Type.__name__=_C
_Ds0SignalingType_Object=MibTableColumn
ds0SignalingType=_Ds0SignalingType_Object((1,3,6,1,4,1,351,110,4,7,1,1,24),_Ds0SignalingType_Type())
ds0SignalingType.setMaxAccess(_E)
if mibBuilder.loadTexts:ds0SignalingType.setStatus(_B)
class _Ds0CasMinDelayDialTime_Type(Integer32):defaultValue=100
_Ds0CasMinDelayDialTime_Type.__name__=_C
_Ds0CasMinDelayDialTime_Object=MibTableColumn
ds0CasMinDelayDialTime=_Ds0CasMinDelayDialTime_Object((1,3,6,1,4,1,351,110,4,7,1,1,25),_Ds0CasMinDelayDialTime_Type())
ds0CasMinDelayDialTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasMinDelayDialTime.setStatus(_B)
if mibBuilder.loadTexts:ds0CasMinDelayDialTime.setUnits(_F)
class _Ds0CasMinStartDialTime_Type(Integer32):defaultValue=70
_Ds0CasMinStartDialTime_Type.__name__=_C
_Ds0CasMinStartDialTime_Object=MibTableColumn
ds0CasMinStartDialTime=_Ds0CasMinStartDialTime_Object((1,3,6,1,4,1,351,110,4,7,1,1,26),_Ds0CasMinStartDialTime_Type())
ds0CasMinStartDialTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasMinStartDialTime.setStatus(_B)
if mibBuilder.loadTexts:ds0CasMinStartDialTime.setUnits(_F)
class _Ds0CasFlashMinMakeTime_Type(Integer32):defaultValue=300
_Ds0CasFlashMinMakeTime_Type.__name__=_C
_Ds0CasFlashMinMakeTime_Object=MibTableColumn
ds0CasFlashMinMakeTime=_Ds0CasFlashMinMakeTime_Object((1,3,6,1,4,1,351,110,4,7,1,1,27),_Ds0CasFlashMinMakeTime_Type())
ds0CasFlashMinMakeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasFlashMinMakeTime.setStatus(_B)
if mibBuilder.loadTexts:ds0CasFlashMinMakeTime.setUnits(_F)
class _Ds0CasFlashMaxMakeTime_Type(Integer32):defaultValue=1400
_Ds0CasFlashMaxMakeTime_Type.__name__=_C
_Ds0CasFlashMaxMakeTime_Object=MibTableColumn
ds0CasFlashMaxMakeTime=_Ds0CasFlashMaxMakeTime_Object((1,3,6,1,4,1,351,110,4,7,1,1,28),_Ds0CasFlashMaxMakeTime_Type())
ds0CasFlashMaxMakeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasFlashMaxMakeTime.setStatus(_B)
if mibBuilder.loadTexts:ds0CasFlashMaxMakeTime.setUnits(_F)
class _Ds0CasDirectionality_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_A4,1),('incoming',2),('outgoing',3)))
_Ds0CasDirectionality_Type.__name__=_C
_Ds0CasDirectionality_Object=MibTableColumn
ds0CasDirectionality=_Ds0CasDirectionality_Object((1,3,6,1,4,1,351,110,4,7,1,1,29),_Ds0CasDirectionality_Type())
ds0CasDirectionality.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasDirectionality.setStatus(_B)
class _Ds0CasGlarePolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('controlling',1),('releasing',2)))
_Ds0CasGlarePolicy_Type.__name__=_C
_Ds0CasGlarePolicy_Object=MibTableColumn
ds0CasGlarePolicy=_Ds0CasGlarePolicy_Object((1,3,6,1,4,1,351,110,4,7,1,1,30),_Ds0CasGlarePolicy_Type())
ds0CasGlarePolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasGlarePolicy.setStatus(_B)
class _Ds0CasIncomingMgcpPackage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Ds0CasIncomingMgcpPackage_Type.__name__=_H
_Ds0CasIncomingMgcpPackage_Object=MibTableColumn
ds0CasIncomingMgcpPackage=_Ds0CasIncomingMgcpPackage_Object((1,3,6,1,4,1,351,110,4,7,1,1,31),_Ds0CasIncomingMgcpPackage_Type())
ds0CasIncomingMgcpPackage.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasIncomingMgcpPackage.setStatus(_B)
class _Ds0CasOutgoingMgcpPackage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Ds0CasOutgoingMgcpPackage_Type.__name__=_H
_Ds0CasOutgoingMgcpPackage_Object=MibTableColumn
ds0CasOutgoingMgcpPackage=_Ds0CasOutgoingMgcpPackage_Object((1,3,6,1,4,1,351,110,4,7,1,1,32),_Ds0CasOutgoingMgcpPackage_Type())
ds0CasOutgoingMgcpPackage.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0CasOutgoingMgcpPackage.setStatus(_B)
class _Ds0InputGain_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-6,14))
_Ds0InputGain_Type.__name__=_C
_Ds0InputGain_Object=MibTableColumn
ds0InputGain=_Ds0InputGain_Object((1,3,6,1,4,1,351,110,4,7,1,1,33),_Ds0InputGain_Type())
ds0InputGain.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0InputGain.setStatus(_B)
if mibBuilder.loadTexts:ds0InputGain.setUnits(_A5)
class _Ds0OutputAttenuation_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_Ds0OutputAttenuation_Type.__name__=_C
_Ds0OutputAttenuation_Object=MibTableColumn
ds0OutputAttenuation=_Ds0OutputAttenuation_Object((1,3,6,1,4,1,351,110,4,7,1,1,34),_Ds0OutputAttenuation_Type())
ds0OutputAttenuation.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0OutputAttenuation.setStatus(_B)
if mibBuilder.loadTexts:ds0OutputAttenuation.setUnits(_A5)
class _Ds0MusicThreshold_Type(Integer32):defaultValue=-38;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-70,-30))
_Ds0MusicThreshold_Type.__name__=_C
_Ds0MusicThreshold_Object=MibTableColumn
ds0MusicThreshold=_Ds0MusicThreshold_Object((1,3,6,1,4,1,351,110,4,7,1,1,35),_Ds0MusicThreshold_Type())
ds0MusicThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0MusicThreshold.setStatus(_B)
class _Ds0SidPacket_Type(TruthValue):defaultValue=1
_Ds0SidPacket_Type.__name__=_G
_Ds0SidPacket_Object=MibTableColumn
ds0SidPacket=_Ds0SidPacket_Object((1,3,6,1,4,1,351,110,4,7,1,1,36),_Ds0SidPacket_Type())
ds0SidPacket.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0SidPacket.setStatus(_B)
class _Ds0ExecDiag_Type(TruthValue):defaultValue=1
_Ds0ExecDiag_Type.__name__=_G
_Ds0ExecDiag_Object=MibTableColumn
ds0ExecDiag=_Ds0ExecDiag_Object((1,3,6,1,4,1,351,110,4,7,1,1,37),_Ds0ExecDiag_Type())
ds0ExecDiag.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0ExecDiag.setStatus(_B)
class _Ds0Companding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uLaw',1),('aLaw',2)))
_Ds0Companding_Type.__name__=_C
_Ds0Companding_Object=MibTableColumn
ds0Companding=_Ds0Companding_Object((1,3,6,1,4,1,351,110,4,7,1,1,38),_Ds0Companding_Type())
ds0Companding.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0Companding.setStatus(_B)
_Ds0RxCasTransTblName_Type=DisplayString
_Ds0RxCasTransTblName_Object=MibTableColumn
ds0RxCasTransTblName=_Ds0RxCasTransTblName_Object((1,3,6,1,4,1,351,110,4,7,1,1,39),_Ds0RxCasTransTblName_Type())
ds0RxCasTransTblName.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0RxCasTransTblName.setStatus(_B)
_Ds0TxCasTransTblName_Type=DisplayString
_Ds0TxCasTransTblName_Object=MibTableColumn
ds0TxCasTransTblName=_Ds0TxCasTransTblName_Object((1,3,6,1,4,1,351,110,4,7,1,1,40),_Ds0TxCasTransTblName_Type())
ds0TxCasTransTblName.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0TxCasTransTblName.setStatus(_B)
class _Ds0TxRxCasConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('transmit',1),('receive',2),(_A4,3),('none',4)))
_Ds0TxRxCasConfig_Type.__name__=_C
_Ds0TxRxCasConfig_Object=MibTableColumn
ds0TxRxCasConfig=_Ds0TxRxCasConfig_Object((1,3,6,1,4,1,351,110,4,7,1,1,41),_Ds0TxRxCasConfig_Type())
ds0TxRxCasConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0TxRxCasConfig.setStatus(_B)
_Dsx0VismChanMapTable_Object=MibTable
dsx0VismChanMapTable=_Dsx0VismChanMapTable_Object((1,3,6,1,4,1,351,110,4,7,2))
if mibBuilder.loadTexts:dsx0VismChanMapTable.setStatus(_B)
_Dsx0VismChanMapEntry_Object=MibTableRow
dsx0VismChanMapEntry=_Dsx0VismChanMapEntry_Object((1,3,6,1,4,1,351,110,4,7,2,1))
dsx0VismChanMapEntry.setIndexNames((0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:dsx0VismChanMapEntry.setStatus(_B)
class _Dsx1LineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Dsx1LineNum_Type.__name__=_C
_Dsx1LineNum_Object=MibTableColumn
dsx1LineNum=_Dsx1LineNum_Object((1,3,6,1,4,1,351,110,4,7,2,1,1),_Dsx1LineNum_Type())
dsx1LineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx1LineNum.setStatus(_B)
class _Ds0ChanNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_Ds0ChanNum_Type.__name__=_C
_Ds0ChanNum_Object=MibTableColumn
ds0ChanNum=_Ds0ChanNum_Object((1,3,6,1,4,1,351,110,4,7,2,1,2),_Ds0ChanNum_Type())
ds0ChanNum.setMaxAccess(_E)
if mibBuilder.loadTexts:ds0ChanNum.setStatus(_B)
class _Ds0ChanMapIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Ds0ChanMapIfIndex_Type.__name__=_C
_Ds0ChanMapIfIndex_Object=MibTableColumn
ds0ChanMapIfIndex=_Ds0ChanMapIfIndex_Object((1,3,6,1,4,1,351,110,4,7,2,1,3),_Ds0ChanMapIfIndex_Type())
ds0ChanMapIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ds0ChanMapIfIndex.setStatus(_B)
_VismDs0LineStatsTable_Object=MibTable
vismDs0LineStatsTable=_VismDs0LineStatsTable_Object((1,3,6,1,4,1,351,110,4,7,3))
if mibBuilder.loadTexts:vismDs0LineStatsTable.setStatus(_B)
_VismDs0LineStatsEntry_Object=MibTableRow
vismDs0LineStatsEntry=_VismDs0LineStatsEntry_Object((1,3,6,1,4,1,351,110,4,7,3,1))
vismDs0LineStatsEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:vismDs0LineStatsEntry.setStatus(_B)
class _Ds0LineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Ds0LineNum_Type.__name__=_C
_Ds0LineNum_Object=MibTableColumn
ds0LineNum=_Ds0LineNum_Object((1,3,6,1,4,1,351,110,4,7,3,1,1),_Ds0LineNum_Type())
ds0LineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:ds0LineNum.setStatus(_B)
class _LineTotalDs0Count_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_LineTotalDs0Count_Type.__name__=_C
_LineTotalDs0Count_Object=MibTableColumn
lineTotalDs0Count=_LineTotalDs0Count_Object((1,3,6,1,4,1,351,110,4,7,3,1,2),_LineTotalDs0Count_Type())
lineTotalDs0Count.setMaxAccess(_E)
if mibBuilder.loadTexts:lineTotalDs0Count.setStatus(_B)
class _LineFreeDs0Count_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_LineFreeDs0Count_Type.__name__=_C
_LineFreeDs0Count_Object=MibTableColumn
lineFreeDs0Count=_LineFreeDs0Count_Object((1,3,6,1,4,1,351,110,4,7,3,1,3),_LineFreeDs0Count_Type())
lineFreeDs0Count.setMaxAccess(_E)
if mibBuilder.loadTexts:lineFreeDs0Count.setStatus(_B)
class _LineActiveDs0Count_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_LineActiveDs0Count_Type.__name__=_C
_LineActiveDs0Count_Object=MibTableColumn
lineActiveDs0Count=_LineActiveDs0Count_Object((1,3,6,1,4,1,351,110,4,7,3,1,4),_LineActiveDs0Count_Type())
lineActiveDs0Count.setMaxAccess(_E)
if mibBuilder.loadTexts:lineActiveDs0Count.setStatus(_B)
class _LineBlockDs0Count_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_LineBlockDs0Count_Type.__name__=_C
_LineBlockDs0Count_Object=MibTableColumn
lineBlockDs0Count=_LineBlockDs0Count_Object((1,3,6,1,4,1,351,110,4,7,3,1,5),_LineBlockDs0Count_Type())
lineBlockDs0Count.setMaxAccess(_E)
if mibBuilder.loadTexts:lineBlockDs0Count.setStatus(_B)
class _LineActiveHighWaterMark_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_LineActiveHighWaterMark_Type.__name__=_C
_LineActiveHighWaterMark_Object=MibTableColumn
lineActiveHighWaterMark=_LineActiveHighWaterMark_Object((1,3,6,1,4,1,351,110,4,7,3,1,6),_LineActiveHighWaterMark_Type())
lineActiveHighWaterMark.setMaxAccess(_E)
if mibBuilder.loadTexts:lineActiveHighWaterMark.setStatus(_B)
class _LineStatsClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LineStatsClrButton_Type.__name__=_C
_LineStatsClrButton_Object=MibTableColumn
lineStatsClrButton=_LineStatsClrButton_Object((1,3,6,1,4,1,351,110,4,7,3,1,7),_LineStatsClrButton_Type())
lineStatsClrButton.setMaxAccess(_D)
if mibBuilder.loadTexts:lineStatsClrButton.setStatus(_B)
_VismDs0StatusTable_Object=MibTable
vismDs0StatusTable=_VismDs0StatusTable_Object((1,3,6,1,4,1,351,110,4,7,4))
if mibBuilder.loadTexts:vismDs0StatusTable.setStatus(_B)
_VismDs0StatusEntry_Object=MibTableRow
vismDs0StatusEntry=_VismDs0StatusEntry_Object((1,3,6,1,4,1,351,110,4,7,4,1))
vismDs0StatusEntry.setIndexNames((0,_A,_P),(0,_A,_Q))
if mibBuilder.loadTexts:vismDs0StatusEntry.setStatus(_B)
class _Ds0LineNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Ds0LineNumber_Type.__name__=_C
_Ds0LineNumber_Object=MibTableColumn
ds0LineNumber=_Ds0LineNumber_Object((1,3,6,1,4,1,351,110,4,7,4,1,1),_Ds0LineNumber_Type())
ds0LineNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:ds0LineNumber.setStatus(_B)
class _Ds0Number_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_Ds0Number_Type.__name__=_C
_Ds0Number_Object=MibTableColumn
ds0Number=_Ds0Number_Object((1,3,6,1,4,1,351,110,4,7,4,1,2),_Ds0Number_Type())
ds0Number.setMaxAccess(_E)
if mibBuilder.loadTexts:ds0Number.setStatus(_B)
class _Ds0Status_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('idle',1),('busy',2),('fault',3),('block',4),('unknown',5)))
_Ds0Status_Type.__name__=_C
_Ds0Status_Object=MibTableColumn
ds0Status=_Ds0Status_Object((1,3,6,1,4,1,351,110,4,7,4,1,3),_Ds0Status_Type())
ds0Status.setMaxAccess(_E)
if mibBuilder.loadTexts:ds0Status.setStatus(_B)
class _Ds0StatusClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Ds0StatusClrButton_Type.__name__=_C
_Ds0StatusClrButton_Object=MibTableColumn
ds0StatusClrButton=_Ds0StatusClrButton_Object((1,3,6,1,4,1,351,110,4,7,4,1,4),_Ds0StatusClrButton_Type())
ds0StatusClrButton.setMaxAccess(_D)
if mibBuilder.loadTexts:ds0StatusClrButton.setStatus(_B)
_CiscoVismDsx0MIBConformance_ObjectIdentity=ObjectIdentity
ciscoVismDsx0MIBConformance=_CiscoVismDsx0MIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,81,2))
_CiscoVismDsx0MIBGroups_ObjectIdentity=ObjectIdentity
ciscoVismDsx0MIBGroups=_CiscoVismDsx0MIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,81,2,1))
_CiscoVismDsx0MIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVismDsx0MIBCompliances=_CiscoVismDsx0MIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,81,2,2))
ciscoVismCardStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,81,2,1,1))
ciscoVismCardStatsGroup.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:ciscoVismCardStatsGroup.setStatus(_B)
ciscoVismDsx0LineStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,81,2,1,2))
ciscoVismDsx0LineStatsGroup.setObjects(*((_A,_O),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:ciscoVismDsx0LineStatsGroup.setStatus(_B)
ciscoVismDsx0StatusGroup=ObjectGroup((1,3,6,1,4,1,351,150,81,2,1,3))
ciscoVismDsx0StatusGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:ciscoVismDsx0StatusGroup.setStatus(_B)
ciscoVismDsx0ConfGroup=ObjectGroup((1,3,6,1,4,1,351,150,81,2,1,4))
ciscoVismDsx0ConfGroup.setObjects(*((_A,_I),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:ciscoVismDsx0ConfGroup.setStatus(_J)
ciscoVismDsx0ChanMapGroup=ObjectGroup((1,3,6,1,4,1,351,150,81,2,1,5))
ciscoVismDsx0ChanMapGroup.setObjects(*((_A,_M),(_A,_N),(_A,_AK)))
if mibBuilder.loadTexts:ciscoVismDsx0ChanMapGroup.setStatus(_B)
ciscoVismDsx0ConfDeprecatedGroup=ObjectGroup((1,3,6,1,4,1,351,150,81,2,1,6))
ciscoVismDsx0ConfDeprecatedGroup.setObjects((_A,_AL))
if mibBuilder.loadTexts:ciscoVismDsx0ConfDeprecatedGroup.setStatus(_J)
ciscoVismDsx0ConfGroup2=ObjectGroup((1,3,6,1,4,1,351,150,81,2,1,7))
ciscoVismDsx0ConfGroup2.setObjects(*((_A,_I),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:ciscoVismDsx0ConfGroup2.setStatus(_B)
ciscoVismDsx0Compliance=ModuleCompliance((1,3,6,1,4,1,351,150,81,2,2,1))
ciscoVismDsx0Compliance.setObjects(*((_A,_A0),(_A,_A1),(_A,_AQ),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:ciscoVismDsx0Compliance.setStatus(_J)
ciscoVismDsx0Compliance2=ModuleCompliance((1,3,6,1,4,1,351,150,81,2,2,2))
ciscoVismDsx0Compliance2.setObjects(*((_A,_A0),(_A,_A1),(_A,_AR),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:ciscoVismDsx0Compliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'vismDs0CardStats':vismDs0CardStats,_A6:vismTotalDs0Count,_A7:vismFreeDs0Count,_A8:vismActiveDs0Count,_A9:vismBlockDs0Count,_AA:vismActiveHighWaterMark,_AB:vismDs0CardStatsClrButton,'dsx0VismCnfTable':dsx0VismCnfTable,'dsx0VismCnfEntry':dsx0VismCnfEntry,_I:ds0IfIndex,_R:ds0RobbedBitSignalling,_S:ds0IdleCode,_T:ds0SeizedCode,_U:ds0ReceivedCode,_AL:ds0TransmitCodesEnable,_V:ds0BundleMapped,_W:ds0IfType,_X:ds0CasVariantName,_Y:ds0CasCadenceOnTime,_Z:ds0CasCadenceOffTime,_a:ds0InsertLocalCas,_b:ds0LocalCasPattern,_c:ds0LoopbackCommand,_d:ds0CasParameterSource,_e:ds0CasOnHookMinMakeTime,_f:ds0CasOffHookMinMakeTime,_g:ds0CasWinkMinMakeTime,_h:ds0CasWinkMaxMakeTime,_i:ds0CasWinkBreakTime,_j:ds0CasGlareTime,_k:ds0CasGaurdTime,_l:ds0CasDelayImmedStart,_m:ds0SignalingType,_n:ds0CasMinDelayDialTime,_o:ds0CasMinStartDialTime,_p:ds0CasFlashMinMakeTime,_q:ds0CasFlashMaxMakeTime,_r:ds0CasDirectionality,_s:ds0CasGlarePolicy,_t:ds0CasIncomingMgcpPackage,_u:ds0CasOutgoingMgcpPackage,_v:ds0InputGain,_w:ds0OutputAttenuation,_x:ds0MusicThreshold,_y:ds0SidPacket,_z:ds0ExecDiag,_AM:ds0Companding,_AN:ds0RxCasTransTblName,_AO:ds0TxCasTransTblName,_AP:ds0TxRxCasConfig,'dsx0VismChanMapTable':dsx0VismChanMapTable,'dsx0VismChanMapEntry':dsx0VismChanMapEntry,_M:dsx1LineNum,_N:ds0ChanNum,_AK:ds0ChanMapIfIndex,'vismDs0LineStatsTable':vismDs0LineStatsTable,'vismDs0LineStatsEntry':vismDs0LineStatsEntry,_O:ds0LineNum,_AC:lineTotalDs0Count,_AD:lineFreeDs0Count,_AE:lineActiveDs0Count,_AF:lineBlockDs0Count,_AG:lineActiveHighWaterMark,_AH:lineStatsClrButton,'vismDs0StatusTable':vismDs0StatusTable,'vismDs0StatusEntry':vismDs0StatusEntry,_P:ds0LineNumber,_Q:ds0Number,_AI:ds0Status,_AJ:ds0StatusClrButton,'ciscoVismDsx0MIB':ciscoVismDsx0MIB,'ciscoVismDsx0MIBConformance':ciscoVismDsx0MIBConformance,'ciscoVismDsx0MIBGroups':ciscoVismDsx0MIBGroups,_A3:ciscoVismCardStatsGroup,_A0:ciscoVismDsx0LineStatsGroup,_A1:ciscoVismDsx0StatusGroup,_AQ:ciscoVismDsx0ConfGroup,_A2:ciscoVismDsx0ChanMapGroup,'ciscoVismDsx0ConfDeprecatedGroup':ciscoVismDsx0ConfDeprecatedGroup,_AR:ciscoVismDsx0ConfGroup2,'ciscoVismDsx0MIBCompliances':ciscoVismDsx0MIBCompliances,'ciscoVismDsx0Compliance':ciscoVismDsx0Compliance,'ciscoVismDsx0Compliance2':ciscoVismDsx0Compliance2})