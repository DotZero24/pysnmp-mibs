_A8='a3ComFddiPORTEBErrorCt'
_A7='a3ComFddiSMTHoldState'
_A6='receive-noise'
_A5='receive-unknown'
_A4='receive-active'
_A3='a3ComFddiPORTLSPORTIndex'
_A2='a3ComFddiPORTLSSMTIndex'
_A1='a3ComFddiPORTIndex'
_A0='a3ComFddiPORTSMTIndex'
_z='a3ComFddiPATHSbaPATHIndex'
_y='a3ComFddiPATHSbaSMTIndex'
_x='a3ComFddiPATHRingPATHIndex'
_w='a3ComFddiPATHRingSMTIndex'
_v='a3ComFddiMACTPriMACIndex'
_u='a3ComFddiMACTPriSMTIndex'
_t='a3ComFddiMACBridgeFunctionMACIndex'
_s='a3ComFddiMACBridgeFunctionSMTIndex'
_r='a3ComFddiSMTIndex'
_q='NotificationType'
_p='fddimibSMTPeerWrapFlag'
_o='fddimibSMTCFState'
_n='fddimibPORTRequestedPaths'
_m='fddimibPORTPCWithhold'
_l='fddimibPORTLerFlag'
_k='fddimibPORTLerEstimate'
_j='fddimibPORTLerCutoff'
_i='fddimibPORTLerAlarm'
_h='fddimibPORTLemRejectCts'
_g='fddimibPORTLemCts'
_f='fddimibPORTCurrentPath'
_e='fddimibPORTConnectState'
_d='fddimibPORTAvailablePaths'
_c='fddimibMACUnaDaFlag'
_b='fddimibMACRequestedPaths'
_a='fddimibMACOldUpstreamNbr'
_Z='fddimibMACOldDownstreamNbr'
_Y='fddimibMACNotCopiedRatio'
_X='fddimibMACNotCopiedFlag'
_W='fddimibMACNotCopiedCts'
_V='fddimibMACLostCts'
_U='fddimibMACFrameErrorRatio'
_T='fddimibMACFrameErrorFlag'
_S='fddimibMACFrameCts'
_R='fddimibMACErrorCts'
_Q='fddimibMACDownstreamNbr'
_P='fddimibMACDaFlag'
_O='fddimibMACCopiedCts'
_N='fddimibMACAvailablePaths'
_M='fddimibPORTNeighborType'
_L='fddimibPORTMyType'
_K='fddimibMACUpstreamNbr'
_J='fddimibMACSMTAddress'
_I='fddimibMACCurrentPath'
_H='OctetString'
_G='read-write'
_F='fddimibSMTStationId'
_E='A3COM-SWITCHING-SYSTEMS-FDDI-MIB'
_D='Integer32'
_C='read-only'
_B='mandatory'
_A='FDDI-SMT73-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
FddiSMTStationIdType,FddiTimeNano,fddimibMACAvailablePaths,fddimibMACCopiedCts,fddimibMACCurrentPath,fddimibMACDaFlag,fddimibMACDownstreamNbr,fddimibMACErrorCts,fddimibMACFrameCts,fddimibMACFrameErrorFlag,fddimibMACFrameErrorRatio,fddimibMACLostCts,fddimibMACNotCopiedCts,fddimibMACNotCopiedFlag,fddimibMACNotCopiedRatio,fddimibMACOldDownstreamNbr,fddimibMACOldUpstreamNbr,fddimibMACRequestedPaths,fddimibMACSMTAddress,fddimibMACUnaDaFlag,fddimibMACUpstreamNbr,fddimibPORTAvailablePaths,fddimibPORTConnectState,fddimibPORTCurrentPath,fddimibPORTLemCts,fddimibPORTLemRejectCts,fddimibPORTLerAlarm,fddimibPORTLerCutoff,fddimibPORTLerEstimate,fddimibPORTLerFlag,fddimibPORTMyType,fddimibPORTNeighborType,fddimibPORTPCWithhold,fddimibPORTRequestedPaths,fddimibSMTCFState,fddimibSMTPeerWrapFlag,fddimibSMTStationId=mibBuilder.importSymbols(_A,'FddiSMTStationIdType','FddiTimeNano',_N,_O,_I,_P,_Q,_R,_S,_T,_U,_V,_W,_X,_Y,_Z,_a,_b,_J,_c,_K,_d,_e,_f,_g,_h,_i,_j,_k,_l,_L,_M,_m,_n,_o,_p,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_q,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_q,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_SwitchingSystemsMibs_ObjectIdentity=ObjectIdentity
switchingSystemsMibs=_SwitchingSystemsMibs_ObjectIdentity((1,3,6,1,4,1,43,29))
_A3ComSwitchingSystemsFddiMib_ObjectIdentity=ObjectIdentity
a3ComSwitchingSystemsFddiMib=_A3ComSwitchingSystemsFddiMib_ObjectIdentity((1,3,6,1,4,1,43,29,10))
_A3ComFddiSMT_ObjectIdentity=ObjectIdentity
a3ComFddiSMT=_A3ComFddiSMT_ObjectIdentity((1,3,6,1,4,1,43,29,10,1))
_A3ComFddiSMTTable_Object=MibTable
a3ComFddiSMTTable=_A3ComFddiSMTTable_Object((1,3,6,1,4,1,43,29,10,1,1))
if mibBuilder.loadTexts:a3ComFddiSMTTable.setStatus(_B)
_A3ComFddiSMTEntry_Object=MibTableRow
a3ComFddiSMTEntry=_A3ComFddiSMTEntry_Object((1,3,6,1,4,1,43,29,10,1,1,1))
a3ComFddiSMTEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:a3ComFddiSMTEntry.setStatus(_B)
class _A3ComFddiSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComFddiSMTIndex_Type.__name__=_D
_A3ComFddiSMTIndex_Object=MibTableColumn
a3ComFddiSMTIndex=_A3ComFddiSMTIndex_Object((1,3,6,1,4,1,43,29,10,1,1,1,1),_A3ComFddiSMTIndex_Type())
a3ComFddiSMTIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiSMTIndex.setStatus(_B)
class _A3ComFddiSMTManufacturerOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_A3ComFddiSMTManufacturerOUI_Type.__name__=_H
_A3ComFddiSMTManufacturerOUI_Object=MibTableColumn
a3ComFddiSMTManufacturerOUI=_A3ComFddiSMTManufacturerOUI_Object((1,3,6,1,4,1,43,29,10,1,1,1,2),_A3ComFddiSMTManufacturerOUI_Type())
a3ComFddiSMTManufacturerOUI.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiSMTManufacturerOUI.setStatus(_B)
class _A3ComFddiSMTManufacturerData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(29,29));fixedLength=29
_A3ComFddiSMTManufacturerData_Type.__name__=_H
_A3ComFddiSMTManufacturerData_Object=MibTableColumn
a3ComFddiSMTManufacturerData=_A3ComFddiSMTManufacturerData_Object((1,3,6,1,4,1,43,29,10,1,1,1,3),_A3ComFddiSMTManufacturerData_Type())
a3ComFddiSMTManufacturerData.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiSMTManufacturerData.setStatus(_B)
class _A3ComFddiSMTHoldState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('not-implemented',1),('not-holding',2),('holding-prm',3),('holding-sec',4)))
_A3ComFddiSMTHoldState_Type.__name__=_D
_A3ComFddiSMTHoldState_Object=MibTableColumn
a3ComFddiSMTHoldState=_A3ComFddiSMTHoldState_Object((1,3,6,1,4,1,43,29,10,1,1,1,4),_A3ComFddiSMTHoldState_Type())
a3ComFddiSMTHoldState.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiSMTHoldState.setStatus(_B)
_A3ComFddiSMTSetCount_Type=Integer32
_A3ComFddiSMTSetCount_Object=MibTableColumn
a3ComFddiSMTSetCount=_A3ComFddiSMTSetCount_Object((1,3,6,1,4,1,43,29,10,1,1,1,5),_A3ComFddiSMTSetCount_Type())
a3ComFddiSMTSetCount.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiSMTSetCount.setStatus(_B)
_A3ComFddiSMTLastSetStationId_Type=FddiSMTStationIdType
_A3ComFddiSMTLastSetStationId_Object=MibTableColumn
a3ComFddiSMTLastSetStationId=_A3ComFddiSMTLastSetStationId_Object((1,3,6,1,4,1,43,29,10,1,1,1,6),_A3ComFddiSMTLastSetStationId_Type())
a3ComFddiSMTLastSetStationId.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiSMTLastSetStationId.setStatus(_B)
_A3ComFddiMAC_ObjectIdentity=ObjectIdentity
a3ComFddiMAC=_A3ComFddiMAC_ObjectIdentity((1,3,6,1,4,1,43,29,10,2))
_A3ComFddiMACBridgeFunctionTable_Object=MibTable
a3ComFddiMACBridgeFunctionTable=_A3ComFddiMACBridgeFunctionTable_Object((1,3,6,1,4,1,43,29,10,2,1))
if mibBuilder.loadTexts:a3ComFddiMACBridgeFunctionTable.setStatus(_B)
_A3ComFddiMACBridgeFunctionEntry_Object=MibTableRow
a3ComFddiMACBridgeFunctionEntry=_A3ComFddiMACBridgeFunctionEntry_Object((1,3,6,1,4,1,43,29,10,2,1,1))
a3ComFddiMACBridgeFunctionEntry.setIndexNames((0,_E,_s),(0,_E,_t))
if mibBuilder.loadTexts:a3ComFddiMACBridgeFunctionEntry.setStatus(_B)
class _A3ComFddiMACBridgeFunctionSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComFddiMACBridgeFunctionSMTIndex_Type.__name__=_D
_A3ComFddiMACBridgeFunctionSMTIndex_Object=MibTableColumn
a3ComFddiMACBridgeFunctionSMTIndex=_A3ComFddiMACBridgeFunctionSMTIndex_Object((1,3,6,1,4,1,43,29,10,2,1,1,1),_A3ComFddiMACBridgeFunctionSMTIndex_Type())
a3ComFddiMACBridgeFunctionSMTIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiMACBridgeFunctionSMTIndex.setStatus(_B)
class _A3ComFddiMACBridgeFunctionMACIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComFddiMACBridgeFunctionMACIndex_Type.__name__=_D
_A3ComFddiMACBridgeFunctionMACIndex_Object=MibTableColumn
a3ComFddiMACBridgeFunctionMACIndex=_A3ComFddiMACBridgeFunctionMACIndex_Object((1,3,6,1,4,1,43,29,10,2,1,1,2),_A3ComFddiMACBridgeFunctionMACIndex_Type())
a3ComFddiMACBridgeFunctionMACIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiMACBridgeFunctionMACIndex.setStatus(_B)
class _A3ComFddiMACBridgeFunctions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_A3ComFddiMACBridgeFunctions_Type.__name__=_D
_A3ComFddiMACBridgeFunctions_Object=MibTableColumn
a3ComFddiMACBridgeFunctions=_A3ComFddiMACBridgeFunctions_Object((1,3,6,1,4,1,43,29,10,2,1,1,3),_A3ComFddiMACBridgeFunctions_Type())
a3ComFddiMACBridgeFunctions.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiMACBridgeFunctions.setStatus(_B)
_A3ComFddiMACTPriTable_Object=MibTable
a3ComFddiMACTPriTable=_A3ComFddiMACTPriTable_Object((1,3,6,1,4,1,43,29,10,2,2))
if mibBuilder.loadTexts:a3ComFddiMACTPriTable.setStatus(_B)
_A3ComFddiMACTPriEntry_Object=MibTableRow
a3ComFddiMACTPriEntry=_A3ComFddiMACTPriEntry_Object((1,3,6,1,4,1,43,29,10,2,2,1))
a3ComFddiMACTPriEntry.setIndexNames((0,_E,_u),(0,_E,_v))
if mibBuilder.loadTexts:a3ComFddiMACTPriEntry.setStatus(_B)
class _A3ComFddiMACTPriSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComFddiMACTPriSMTIndex_Type.__name__=_D
_A3ComFddiMACTPriSMTIndex_Object=MibTableColumn
a3ComFddiMACTPriSMTIndex=_A3ComFddiMACTPriSMTIndex_Object((1,3,6,1,4,1,43,29,10,2,2,1,1),_A3ComFddiMACTPriSMTIndex_Type())
a3ComFddiMACTPriSMTIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiMACTPriSMTIndex.setStatus(_B)
class _A3ComFddiMACTPriMACIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComFddiMACTPriMACIndex_Type.__name__=_D
_A3ComFddiMACTPriMACIndex_Object=MibTableColumn
a3ComFddiMACTPriMACIndex=_A3ComFddiMACTPriMACIndex_Object((1,3,6,1,4,1,43,29,10,2,2,1,2),_A3ComFddiMACTPriMACIndex_Type())
a3ComFddiMACTPriMACIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiMACTPriMACIndex.setStatus(_B)
_A3ComFddiMACTPri0_Type=FddiTimeNano
_A3ComFddiMACTPri0_Object=MibTableColumn
a3ComFddiMACTPri0=_A3ComFddiMACTPri0_Object((1,3,6,1,4,1,43,29,10,2,2,1,3),_A3ComFddiMACTPri0_Type())
a3ComFddiMACTPri0.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiMACTPri0.setStatus(_B)
_A3ComFddiMACTPri1_Type=FddiTimeNano
_A3ComFddiMACTPri1_Object=MibTableColumn
a3ComFddiMACTPri1=_A3ComFddiMACTPri1_Object((1,3,6,1,4,1,43,29,10,2,2,1,4),_A3ComFddiMACTPri1_Type())
a3ComFddiMACTPri1.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiMACTPri1.setStatus(_B)
_A3ComFddiMACTPri2_Type=FddiTimeNano
_A3ComFddiMACTPri2_Object=MibTableColumn
a3ComFddiMACTPri2=_A3ComFddiMACTPri2_Object((1,3,6,1,4,1,43,29,10,2,2,1,5),_A3ComFddiMACTPri2_Type())
a3ComFddiMACTPri2.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiMACTPri2.setStatus(_B)
_A3ComFddiMACTPri3_Type=FddiTimeNano
_A3ComFddiMACTPri3_Object=MibTableColumn
a3ComFddiMACTPri3=_A3ComFddiMACTPri3_Object((1,3,6,1,4,1,43,29,10,2,2,1,6),_A3ComFddiMACTPri3_Type())
a3ComFddiMACTPri3.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiMACTPri3.setStatus(_B)
_A3ComFddiMACTPri4_Type=FddiTimeNano
_A3ComFddiMACTPri4_Object=MibTableColumn
a3ComFddiMACTPri4=_A3ComFddiMACTPri4_Object((1,3,6,1,4,1,43,29,10,2,2,1,7),_A3ComFddiMACTPri4_Type())
a3ComFddiMACTPri4.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiMACTPri4.setStatus(_B)
_A3ComFddiMACTPri5_Type=FddiTimeNano
_A3ComFddiMACTPri5_Object=MibTableColumn
a3ComFddiMACTPri5=_A3ComFddiMACTPri5_Object((1,3,6,1,4,1,43,29,10,2,2,1,8),_A3ComFddiMACTPri5_Type())
a3ComFddiMACTPri5.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiMACTPri5.setStatus(_B)
_A3ComFddiMACTPri6_Type=FddiTimeNano
_A3ComFddiMACTPri6_Object=MibTableColumn
a3ComFddiMACTPri6=_A3ComFddiMACTPri6_Object((1,3,6,1,4,1,43,29,10,2,2,1,9),_A3ComFddiMACTPri6_Type())
a3ComFddiMACTPri6.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiMACTPri6.setStatus(_B)
_A3ComFddiPATH_ObjectIdentity=ObjectIdentity
a3ComFddiPATH=_A3ComFddiPATH_ObjectIdentity((1,3,6,1,4,1,43,29,10,3))
_A3ComFddiPATHRingTable_Object=MibTable
a3ComFddiPATHRingTable=_A3ComFddiPATHRingTable_Object((1,3,6,1,4,1,43,29,10,3,1))
if mibBuilder.loadTexts:a3ComFddiPATHRingTable.setStatus(_B)
_A3ComFddiPATHRingEntry_Object=MibTableRow
a3ComFddiPATHRingEntry=_A3ComFddiPATHRingEntry_Object((1,3,6,1,4,1,43,29,10,3,1,1))
a3ComFddiPATHRingEntry.setIndexNames((0,_E,_w),(0,_E,_x))
if mibBuilder.loadTexts:a3ComFddiPATHRingEntry.setStatus(_B)
class _A3ComFddiPATHRingSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComFddiPATHRingSMTIndex_Type.__name__=_D
_A3ComFddiPATHRingSMTIndex_Object=MibTableColumn
a3ComFddiPATHRingSMTIndex=_A3ComFddiPATHRingSMTIndex_Object((1,3,6,1,4,1,43,29,10,3,1,1,1),_A3ComFddiPATHRingSMTIndex_Type())
a3ComFddiPATHRingSMTIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiPATHRingSMTIndex.setStatus(_B)
class _A3ComFddiPATHRingPATHIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_A3ComFddiPATHRingPATHIndex_Type.__name__=_D
_A3ComFddiPATHRingPATHIndex_Object=MibTableColumn
a3ComFddiPATHRingPATHIndex=_A3ComFddiPATHRingPATHIndex_Object((1,3,6,1,4,1,43,29,10,3,1,1,2),_A3ComFddiPATHRingPATHIndex_Type())
a3ComFddiPATHRingPATHIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiPATHRingPATHIndex.setStatus(_B)
_A3ComFddiPATHRingLatency_Type=FddiTimeNano
_A3ComFddiPATHRingLatency_Object=MibTableColumn
a3ComFddiPATHRingLatency=_A3ComFddiPATHRingLatency_Object((1,3,6,1,4,1,43,29,10,3,1,1,3),_A3ComFddiPATHRingLatency_Type())
a3ComFddiPATHRingLatency.setMaxAccess(_G)
if mibBuilder.loadTexts:a3ComFddiPATHRingLatency.setStatus(_B)
class _A3ComFddiPATHTraceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_A3ComFddiPATHTraceStatus_Type.__name__=_D
_A3ComFddiPATHTraceStatus_Object=MibTableColumn
a3ComFddiPATHTraceStatus=_A3ComFddiPATHTraceStatus_Object((1,3,6,1,4,1,43,29,10,3,1,1,4),_A3ComFddiPATHTraceStatus_Type())
a3ComFddiPATHTraceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiPATHTraceStatus.setStatus(_B)
_A3ComFddiPATHT_Rmode_Type=FddiTimeNano
_A3ComFddiPATHT_Rmode_Object=MibTableColumn
a3ComFddiPATHT_Rmode=_A3ComFddiPATHT_Rmode_Object((1,3,6,1,4,1,43,29,10,3,1,1,5),_A3ComFddiPATHT_Rmode_Type())
a3ComFddiPATHT_Rmode.setMaxAccess(_G)
if mibBuilder.loadTexts:a3ComFddiPATHT_Rmode.setStatus(_B)
_A3ComFddiPATHSbaTable_Object=MibTable
a3ComFddiPATHSbaTable=_A3ComFddiPATHSbaTable_Object((1,3,6,1,4,1,43,29,10,3,2))
if mibBuilder.loadTexts:a3ComFddiPATHSbaTable.setStatus(_B)
_A3ComFddiPATHSbaEntry_Object=MibTableRow
a3ComFddiPATHSbaEntry=_A3ComFddiPATHSbaEntry_Object((1,3,6,1,4,1,43,29,10,3,2,1))
a3ComFddiPATHSbaEntry.setIndexNames((0,_E,_y),(0,_E,_z))
if mibBuilder.loadTexts:a3ComFddiPATHSbaEntry.setStatus(_B)
class _A3ComFddiPATHSbaSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComFddiPATHSbaSMTIndex_Type.__name__=_D
_A3ComFddiPATHSbaSMTIndex_Object=MibTableColumn
a3ComFddiPATHSbaSMTIndex=_A3ComFddiPATHSbaSMTIndex_Object((1,3,6,1,4,1,43,29,10,3,2,1,1),_A3ComFddiPATHSbaSMTIndex_Type())
a3ComFddiPATHSbaSMTIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiPATHSbaSMTIndex.setStatus(_B)
class _A3ComFddiPATHSbaPATHIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_A3ComFddiPATHSbaPATHIndex_Type.__name__=_D
_A3ComFddiPATHSbaPATHIndex_Object=MibTableColumn
a3ComFddiPATHSbaPATHIndex=_A3ComFddiPATHSbaPATHIndex_Object((1,3,6,1,4,1,43,29,10,3,2,1,2),_A3ComFddiPATHSbaPATHIndex_Type())
a3ComFddiPATHSbaPATHIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiPATHSbaPATHIndex.setStatus(_B)
class _A3ComFddiPATHSbaPayload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1562))
_A3ComFddiPATHSbaPayload_Type.__name__=_D
_A3ComFddiPATHSbaPayload_Object=MibTableColumn
a3ComFddiPATHSbaPayload=_A3ComFddiPATHSbaPayload_Object((1,3,6,1,4,1,43,29,10,3,2,1,3),_A3ComFddiPATHSbaPayload_Type())
a3ComFddiPATHSbaPayload.setMaxAccess(_G)
if mibBuilder.loadTexts:a3ComFddiPATHSbaPayload.setStatus(_B)
_A3ComFddiPATHSbaOverhead_Type=Integer32
_A3ComFddiPATHSbaOverhead_Object=MibTableColumn
a3ComFddiPATHSbaOverhead=_A3ComFddiPATHSbaOverhead_Object((1,3,6,1,4,1,43,29,10,3,2,1,4),_A3ComFddiPATHSbaOverhead_Type())
a3ComFddiPATHSbaOverhead.setMaxAccess(_G)
if mibBuilder.loadTexts:a3ComFddiPATHSbaOverhead.setStatus(_B)
class _A3ComFddiPATHSbaAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12500000))
_A3ComFddiPATHSbaAvailable_Type.__name__=_D
_A3ComFddiPATHSbaAvailable_Object=MibTableColumn
a3ComFddiPATHSbaAvailable=_A3ComFddiPATHSbaAvailable_Object((1,3,6,1,4,1,43,29,10,3,2,1,5),_A3ComFddiPATHSbaAvailable_Type())
a3ComFddiPATHSbaAvailable.setMaxAccess(_G)
if mibBuilder.loadTexts:a3ComFddiPATHSbaAvailable.setStatus(_B)
_A3ComFddiPORT_ObjectIdentity=ObjectIdentity
a3ComFddiPORT=_A3ComFddiPORT_ObjectIdentity((1,3,6,1,4,1,43,29,10,4))
_A3ComFddiPORTTable_Object=MibTable
a3ComFddiPORTTable=_A3ComFddiPORTTable_Object((1,3,6,1,4,1,43,29,10,4,1))
if mibBuilder.loadTexts:a3ComFddiPORTTable.setStatus(_B)
_A3ComFddiPORTEntry_Object=MibTableRow
a3ComFddiPORTEntry=_A3ComFddiPORTEntry_Object((1,3,6,1,4,1,43,29,10,4,1,1))
a3ComFddiPORTEntry.setIndexNames((0,_E,_A0),(0,_E,_A1))
if mibBuilder.loadTexts:a3ComFddiPORTEntry.setStatus(_B)
class _A3ComFddiPORTSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComFddiPORTSMTIndex_Type.__name__=_D
_A3ComFddiPORTSMTIndex_Object=MibTableColumn
a3ComFddiPORTSMTIndex=_A3ComFddiPORTSMTIndex_Object((1,3,6,1,4,1,43,29,10,4,1,1,1),_A3ComFddiPORTSMTIndex_Type())
a3ComFddiPORTSMTIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiPORTSMTIndex.setStatus(_B)
class _A3ComFddiPORTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComFddiPORTIndex_Type.__name__=_D
_A3ComFddiPORTIndex_Object=MibTableColumn
a3ComFddiPORTIndex=_A3ComFddiPORTIndex_Object((1,3,6,1,4,1,43,29,10,4,1,1,2),_A3ComFddiPORTIndex_Type())
a3ComFddiPORTIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiPORTIndex.setStatus(_B)
_A3ComFddiPORTMACLoopTime_Type=FddiTimeNano
_A3ComFddiPORTMACLoopTime_Object=MibTableColumn
a3ComFddiPORTMACLoopTime=_A3ComFddiPORTMACLoopTime_Object((1,3,6,1,4,1,43,29,10,4,1,1,3),_A3ComFddiPORTMACLoopTime_Type())
a3ComFddiPORTMACLoopTime.setMaxAccess(_G)
if mibBuilder.loadTexts:a3ComFddiPORTMACLoopTime.setStatus(_B)
_A3ComFddiPORTEBErrorCt_Type=Counter32
_A3ComFddiPORTEBErrorCt_Object=MibTableColumn
a3ComFddiPORTEBErrorCt=_A3ComFddiPORTEBErrorCt_Object((1,3,6,1,4,1,43,29,10,4,1,1,4),_A3ComFddiPORTEBErrorCt_Type())
a3ComFddiPORTEBErrorCt.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiPORTEBErrorCt.setStatus(_B)
_A3ComFddiPORTLSTable_Object=MibTable
a3ComFddiPORTLSTable=_A3ComFddiPORTLSTable_Object((1,3,6,1,4,1,43,29,10,4,2))
if mibBuilder.loadTexts:a3ComFddiPORTLSTable.setStatus(_B)
_A3ComFddiPORTLSEntry_Object=MibTableRow
a3ComFddiPORTLSEntry=_A3ComFddiPORTLSEntry_Object((1,3,6,1,4,1,43,29,10,4,2,1))
a3ComFddiPORTLSEntry.setIndexNames((0,_E,_A2),(0,_E,_A3))
if mibBuilder.loadTexts:a3ComFddiPORTLSEntry.setStatus(_B)
class _A3ComFddiPORTLSSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComFddiPORTLSSMTIndex_Type.__name__=_D
_A3ComFddiPORTLSSMTIndex_Object=MibTableColumn
a3ComFddiPORTLSSMTIndex=_A3ComFddiPORTLSSMTIndex_Object((1,3,6,1,4,1,43,29,10,4,2,1,1),_A3ComFddiPORTLSSMTIndex_Type())
a3ComFddiPORTLSSMTIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiPORTLSSMTIndex.setStatus(_B)
class _A3ComFddiPORTLSPORTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComFddiPORTLSPORTIndex_Type.__name__=_D
_A3ComFddiPORTLSPORTIndex_Object=MibTableColumn
a3ComFddiPORTLSPORTIndex=_A3ComFddiPORTLSPORTIndex_Object((1,3,6,1,4,1,43,29,10,4,2,1,2),_A3ComFddiPORTLSPORTIndex_Type())
a3ComFddiPORTLSPORTIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiPORTLSPORTIndex.setStatus(_B)
class _A3ComFddiPORTMaintLS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('quiet',1),('idle',2),('master',3),('halt',4),(_A4,5),(_A5,6),(_A6,7)))
_A3ComFddiPORTMaintLS_Type.__name__=_D
_A3ComFddiPORTMaintLS_Object=MibTableColumn
a3ComFddiPORTMaintLS=_A3ComFddiPORTMaintLS_Object((1,3,6,1,4,1,43,29,10,4,2,1,3),_A3ComFddiPORTMaintLS_Type())
a3ComFddiPORTMaintLS.setMaxAccess(_G)
if mibBuilder.loadTexts:a3ComFddiPORTMaintLS.setStatus(_B)
class _A3ComFddiPORTPCLS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('quiet',1),('idle',2),('master',3),('halt',4),(_A4,5),(_A5,6),(_A6,7)))
_A3ComFddiPORTPCLS_Type.__name__=_D
_A3ComFddiPORTPCLS_Object=MibTableColumn
a3ComFddiPORTPCLS=_A3ComFddiPORTPCLS_Object((1,3,6,1,4,1,43,29,10,4,2,1,4),_A3ComFddiPORTPCLS_Type())
a3ComFddiPORTPCLS.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComFddiPORTPCLS.setStatus(_B)
a3ComFddiSMTHoldCondition=NotificationType((1,3,6,1,4,1,43,29,10,0,1))
a3ComFddiSMTHoldCondition.setObjects(*((_A,_F),(_E,_A7)))
if mibBuilder.loadTexts:a3ComFddiSMTHoldCondition.setStatus('')
a3ComFddiSMTPeerWrapCondition=NotificationType((1,3,6,1,4,1,43,29,10,0,2))
a3ComFddiSMTPeerWrapCondition.setObjects(*((_A,_F),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:a3ComFddiSMTPeerWrapCondition.setStatus('')
a3ComFddiMACDuplicateAddressCondition=NotificationType((1,3,6,1,4,1,43,29,10,0,3))
a3ComFddiMACDuplicateAddressCondition.setObjects(*((_A,_F),(_A,_J),(_A,_K),(_A,_P),(_A,_c)))
if mibBuilder.loadTexts:a3ComFddiMACDuplicateAddressCondition.setStatus('')
a3ComFddiMACFrameErrorCondition=NotificationType((1,3,6,1,4,1,43,29,10,0,4))
a3ComFddiMACFrameErrorCondition.setObjects(*((_A,_F),(_A,_T),(_A,_S),(_A,_R),(_A,_V),(_A,_U)))
if mibBuilder.loadTexts:a3ComFddiMACFrameErrorCondition.setStatus('')
a3ComFddiMACNotCopiedCondition=NotificationType((1,3,6,1,4,1,43,29,10,0,5))
a3ComFddiMACNotCopiedCondition.setObjects(*((_A,_F),(_A,_W),(_A,_O),(_A,_Y),(_A,_X)))
if mibBuilder.loadTexts:a3ComFddiMACNotCopiedCondition.setStatus('')
a3ComFddiMACNeighborChangeEvent=NotificationType((1,3,6,1,4,1,43,29,10,0,6))
a3ComFddiMACNeighborChangeEvent.setObjects(*((_A,_F),(_A,_K),(_A,_a),(_A,_Q),(_A,_Z),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:a3ComFddiMACNeighborChangeEvent.setStatus('')
a3ComFddiMACPathChangeEvent=NotificationType((1,3,6,1,4,1,43,29,10,0,7))
a3ComFddiMACPathChangeEvent.setObjects(*((_A,_F),(_A,_N),(_A,_I),(_A,_b)))
if mibBuilder.loadTexts:a3ComFddiMACPathChangeEvent.setStatus('')
a3ComFddiPORTLerCondition=NotificationType((1,3,6,1,4,1,43,29,10,0,8))
a3ComFddiPORTLerCondition.setObjects(*((_A,_F),(_A,_j),(_A,_i),(_A,_k),(_A,_h),(_A,_g),(_A,_l)))
if mibBuilder.loadTexts:a3ComFddiPORTLerCondition.setStatus('')
a3ComFddiPORTUndesiredConnAttemptEvent=NotificationType((1,3,6,1,4,1,43,29,10,0,9))
a3ComFddiPORTUndesiredConnAttemptEvent.setObjects(*((_A,_F),(_A,_L),(_A,_e),(_A,_M),(_A,_m)))
if mibBuilder.loadTexts:a3ComFddiPORTUndesiredConnAttemptEvent.setStatus('')
a3ComFddiPORTEBErrorCondition=NotificationType((1,3,6,1,4,1,43,29,10,0,10))
a3ComFddiPORTEBErrorCondition.setObjects(*((_A,_F),(_E,_A8)))
if mibBuilder.loadTexts:a3ComFddiPORTEBErrorCondition.setStatus('')
a3ComFddiPORTPathChangeEvent=NotificationType((1,3,6,1,4,1,43,29,10,0,11))
a3ComFddiPORTPathChangeEvent.setObjects(*((_A,_F),(_A,_d),(_A,_f),(_A,_n),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:a3ComFddiPORTPathChangeEvent.setStatus('')
mibBuilder.exportSymbols(_E,**{'a3Com':a3Com,'switchingSystemsMibs':switchingSystemsMibs,'a3ComSwitchingSystemsFddiMib':a3ComSwitchingSystemsFddiMib,'a3ComFddiSMTHoldCondition':a3ComFddiSMTHoldCondition,'a3ComFddiSMTPeerWrapCondition':a3ComFddiSMTPeerWrapCondition,'a3ComFddiMACDuplicateAddressCondition':a3ComFddiMACDuplicateAddressCondition,'a3ComFddiMACFrameErrorCondition':a3ComFddiMACFrameErrorCondition,'a3ComFddiMACNotCopiedCondition':a3ComFddiMACNotCopiedCondition,'a3ComFddiMACNeighborChangeEvent':a3ComFddiMACNeighborChangeEvent,'a3ComFddiMACPathChangeEvent':a3ComFddiMACPathChangeEvent,'a3ComFddiPORTLerCondition':a3ComFddiPORTLerCondition,'a3ComFddiPORTUndesiredConnAttemptEvent':a3ComFddiPORTUndesiredConnAttemptEvent,'a3ComFddiPORTEBErrorCondition':a3ComFddiPORTEBErrorCondition,'a3ComFddiPORTPathChangeEvent':a3ComFddiPORTPathChangeEvent,'a3ComFddiSMT':a3ComFddiSMT,'a3ComFddiSMTTable':a3ComFddiSMTTable,'a3ComFddiSMTEntry':a3ComFddiSMTEntry,_r:a3ComFddiSMTIndex,'a3ComFddiSMTManufacturerOUI':a3ComFddiSMTManufacturerOUI,'a3ComFddiSMTManufacturerData':a3ComFddiSMTManufacturerData,_A7:a3ComFddiSMTHoldState,'a3ComFddiSMTSetCount':a3ComFddiSMTSetCount,'a3ComFddiSMTLastSetStationId':a3ComFddiSMTLastSetStationId,'a3ComFddiMAC':a3ComFddiMAC,'a3ComFddiMACBridgeFunctionTable':a3ComFddiMACBridgeFunctionTable,'a3ComFddiMACBridgeFunctionEntry':a3ComFddiMACBridgeFunctionEntry,_s:a3ComFddiMACBridgeFunctionSMTIndex,_t:a3ComFddiMACBridgeFunctionMACIndex,'a3ComFddiMACBridgeFunctions':a3ComFddiMACBridgeFunctions,'a3ComFddiMACTPriTable':a3ComFddiMACTPriTable,'a3ComFddiMACTPriEntry':a3ComFddiMACTPriEntry,_u:a3ComFddiMACTPriSMTIndex,_v:a3ComFddiMACTPriMACIndex,'a3ComFddiMACTPri0':a3ComFddiMACTPri0,'a3ComFddiMACTPri1':a3ComFddiMACTPri1,'a3ComFddiMACTPri2':a3ComFddiMACTPri2,'a3ComFddiMACTPri3':a3ComFddiMACTPri3,'a3ComFddiMACTPri4':a3ComFddiMACTPri4,'a3ComFddiMACTPri5':a3ComFddiMACTPri5,'a3ComFddiMACTPri6':a3ComFddiMACTPri6,'a3ComFddiPATH':a3ComFddiPATH,'a3ComFddiPATHRingTable':a3ComFddiPATHRingTable,'a3ComFddiPATHRingEntry':a3ComFddiPATHRingEntry,_w:a3ComFddiPATHRingSMTIndex,_x:a3ComFddiPATHRingPATHIndex,'a3ComFddiPATHRingLatency':a3ComFddiPATHRingLatency,'a3ComFddiPATHTraceStatus':a3ComFddiPATHTraceStatus,'a3ComFddiPATHT-Rmode':a3ComFddiPATHT_Rmode,'a3ComFddiPATHSbaTable':a3ComFddiPATHSbaTable,'a3ComFddiPATHSbaEntry':a3ComFddiPATHSbaEntry,_y:a3ComFddiPATHSbaSMTIndex,_z:a3ComFddiPATHSbaPATHIndex,'a3ComFddiPATHSbaPayload':a3ComFddiPATHSbaPayload,'a3ComFddiPATHSbaOverhead':a3ComFddiPATHSbaOverhead,'a3ComFddiPATHSbaAvailable':a3ComFddiPATHSbaAvailable,'a3ComFddiPORT':a3ComFddiPORT,'a3ComFddiPORTTable':a3ComFddiPORTTable,'a3ComFddiPORTEntry':a3ComFddiPORTEntry,_A0:a3ComFddiPORTSMTIndex,_A1:a3ComFddiPORTIndex,'a3ComFddiPORTMACLoopTime':a3ComFddiPORTMACLoopTime,_A8:a3ComFddiPORTEBErrorCt,'a3ComFddiPORTLSTable':a3ComFddiPORTLSTable,'a3ComFddiPORTLSEntry':a3ComFddiPORTLSEntry,_A2:a3ComFddiPORTLSSMTIndex,_A3:a3ComFddiPORTLSPORTIndex,'a3ComFddiPORTMaintLS':a3ComFddiPORTMaintLS,'a3ComFddiPORTPCLS':a3ComFddiPORTPCLS})