_U='hwBufSize'
_T='hwBufModuleIndex'
_S='hwMemModuleIndex'
_R='hwCpuIndex'
_Q='hwdevMSlotEnvironmentType'
_P='hwDevMPowerNum'
_O='unsupport'
_N='not-install'
_M='deactive'
_L='active'
_K='hwDevMFanNum'
_J='TimeTicks'
_I='hwLswSlotIndex'
_H='hwLswFrameIndex'
_G='A3COM-HUAWEI-DEVICE-MIB'
_F='not-accessible'
_E='read-write'
_D='A3COM-HUAWEI-LswDEVM-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hwLswFrameIndex,hwLswSlotIndex=mibBuilder.importSymbols(_G,_H,_I)
huaweiUtility,lswCommon=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','huaweiUtility','lswCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_J,'Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwLswdevMMib=ModuleIdentity((1,3,6,1,4,1,43,45,1,2,23,1,9))
if mibBuilder.loadTexts:hwLswdevMMib.setRevisions(('2001-06-29 00:00',))
_HwLswdevMMibObject_ObjectIdentity=ObjectIdentity
hwLswdevMMibObject=_HwLswdevMMibObject_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,23,1,9,1))
if mibBuilder.loadTexts:hwLswdevMMibObject.setStatus(_A)
_HwdevMFanStatusTable_Object=MibTable
hwdevMFanStatusTable=_HwdevMFanStatusTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,1))
if mibBuilder.loadTexts:hwdevMFanStatusTable.setStatus(_A)
_HwdevMFanStatusEntry_Object=MibTableRow
hwdevMFanStatusEntry=_HwdevMFanStatusEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,1,1))
hwdevMFanStatusEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:hwdevMFanStatusEntry.setStatus(_A)
_HwDevMFanNum_Type=Integer32
_HwDevMFanNum_Object=MibTableColumn
hwDevMFanNum=_HwDevMFanNum_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,1,1,1),_HwDevMFanNum_Type())
hwDevMFanNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwDevMFanNum.setStatus(_A)
class _HwDevMFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4)))
_HwDevMFanStatus_Type.__name__=_C
_HwDevMFanStatus_Object=MibTableColumn
hwDevMFanStatus=_HwDevMFanStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,1,1,2),_HwDevMFanStatus_Type())
hwDevMFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwDevMFanStatus.setStatus(_A)
_HwdevMPowerStatusTable_Object=MibTable
hwdevMPowerStatusTable=_HwdevMPowerStatusTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,2))
if mibBuilder.loadTexts:hwdevMPowerStatusTable.setStatus(_A)
_HwdevMPowerStatusEntry_Object=MibTableRow
hwdevMPowerStatusEntry=_HwdevMPowerStatusEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,2,1))
hwdevMPowerStatusEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:hwdevMPowerStatusEntry.setStatus(_A)
_HwDevMPowerNum_Type=Integer32
_HwDevMPowerNum_Object=MibTableColumn
hwDevMPowerNum=_HwDevMPowerNum_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,2,1,1),_HwDevMPowerNum_Type())
hwDevMPowerNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwDevMPowerNum.setStatus(_A)
class _HwDevMPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4)))
_HwDevMPowerStatus_Type.__name__=_C
_HwDevMPowerStatus_Object=MibTableColumn
hwDevMPowerStatus=_HwDevMPowerStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,2,1,2),_HwDevMPowerStatus_Type())
hwDevMPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwDevMPowerStatus.setStatus(_A)
_HwdevMSlotEnvironmentTable_Object=MibTable
hwdevMSlotEnvironmentTable=_HwdevMSlotEnvironmentTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,3))
if mibBuilder.loadTexts:hwdevMSlotEnvironmentTable.setStatus(_A)
_HwdevMSlotEnvironmentEntry_Object=MibTableRow
hwdevMSlotEnvironmentEntry=_HwdevMSlotEnvironmentEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,3,1))
hwdevMSlotEnvironmentEntry.setIndexNames((0,_G,_H),(0,_G,_I),(0,_D,_Q))
if mibBuilder.loadTexts:hwdevMSlotEnvironmentEntry.setStatus(_A)
class _HwdevMSlotEnvironmentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('temperature',1),('humidity',2),('fog',3)))
_HwdevMSlotEnvironmentType_Type.__name__=_C
_HwdevMSlotEnvironmentType_Object=MibTableColumn
hwdevMSlotEnvironmentType=_HwdevMSlotEnvironmentType_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,3,1,1),_HwdevMSlotEnvironmentType_Type())
hwdevMSlotEnvironmentType.setMaxAccess(_F)
if mibBuilder.loadTexts:hwdevMSlotEnvironmentType.setStatus(_A)
class _HwDevMSlotEnvironmentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('upper',2),('lower',3)))
_HwDevMSlotEnvironmentStatus_Type.__name__=_C
_HwDevMSlotEnvironmentStatus_Object=MibTableColumn
hwDevMSlotEnvironmentStatus=_HwDevMSlotEnvironmentStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,3,1,2),_HwDevMSlotEnvironmentStatus_Type())
hwDevMSlotEnvironmentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwDevMSlotEnvironmentStatus.setStatus(_A)
_HwDevMSlotEnvironmentValue_Type=Integer32
_HwDevMSlotEnvironmentValue_Object=MibTableColumn
hwDevMSlotEnvironmentValue=_HwDevMSlotEnvironmentValue_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,3,1,3),_HwDevMSlotEnvironmentValue_Type())
hwDevMSlotEnvironmentValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hwDevMSlotEnvironmentValue.setStatus(_A)
_HwDevMSlotEnvironmentUpperLimit_Type=Integer32
_HwDevMSlotEnvironmentUpperLimit_Object=MibTableColumn
hwDevMSlotEnvironmentUpperLimit=_HwDevMSlotEnvironmentUpperLimit_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,3,1,4),_HwDevMSlotEnvironmentUpperLimit_Type())
hwDevMSlotEnvironmentUpperLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDevMSlotEnvironmentUpperLimit.setStatus(_A)
_HwDevMSlotEnvironmentLowerLimit_Type=Integer32
_HwDevMSlotEnvironmentLowerLimit_Object=MibTableColumn
hwDevMSlotEnvironmentLowerLimit=_HwDevMSlotEnvironmentLowerLimit_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,3,1,5),_HwDevMSlotEnvironmentLowerLimit_Type())
hwDevMSlotEnvironmentLowerLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDevMSlotEnvironmentLowerLimit.setStatus(_A)
class _HwLinkUpDownTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('enableBoth',1),('disableBoth',2),('enableLinkUpTrapOnly',3),('enableLinkDownTrapOnly',4)))
_HwLinkUpDownTrapEnable_Type.__name__=_C
_HwLinkUpDownTrapEnable_Object=MibScalar
hwLinkUpDownTrapEnable=_HwLinkUpDownTrapEnable_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,9),_HwLinkUpDownTrapEnable_Type())
hwLinkUpDownTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hwLinkUpDownTrapEnable.setStatus(_A)
class _Hwdot1qTpFdbLearnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_Hwdot1qTpFdbLearnStatus_Type.__name__=_C
_Hwdot1qTpFdbLearnStatus_Object=MibScalar
hwdot1qTpFdbLearnStatus=_Hwdot1qTpFdbLearnStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,10),_Hwdot1qTpFdbLearnStatus_Type())
hwdot1qTpFdbLearnStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hwdot1qTpFdbLearnStatus.setStatus(_A)
class _HwCfmWriteFlash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('write',1))
_HwCfmWriteFlash_Type.__name__=_C
_HwCfmWriteFlash_Object=MibScalar
hwCfmWriteFlash=_HwCfmWriteFlash_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,11),_HwCfmWriteFlash_Type())
hwCfmWriteFlash.setMaxAccess(_E)
if mibBuilder.loadTexts:hwCfmWriteFlash.setStatus(_A)
class _HwCfmEraseFlash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('erase',1))
_HwCfmEraseFlash_Type.__name__=_C
_HwCfmEraseFlash_Object=MibScalar
hwCfmEraseFlash=_HwCfmEraseFlash_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,12),_HwCfmEraseFlash_Type())
hwCfmEraseFlash.setMaxAccess(_E)
if mibBuilder.loadTexts:hwCfmEraseFlash.setStatus(_A)
_HwDevMFirstTrapTime_Type=TimeTicks
_HwDevMFirstTrapTime_Object=MibScalar
hwDevMFirstTrapTime=_HwDevMFirstTrapTime_Object((1,3,6,1,4,1,43,45,1,2,23,1,9,1,13),_HwDevMFirstTrapTime_Type())
hwDevMFirstTrapTime.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hwDevMFirstTrapTime.setStatus(_A)
_HwDevice_ObjectIdentity=ObjectIdentity
hwDevice=_HwDevice_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,1))
_HwCpuTable_Object=MibTable
hwCpuTable=_HwCpuTable_Object((1,3,6,1,4,1,43,45,1,6,1,1))
if mibBuilder.loadTexts:hwCpuTable.setStatus(_A)
_HwCpuEntry_Object=MibTableRow
hwCpuEntry=_HwCpuEntry_Object((1,3,6,1,4,1,43,45,1,6,1,1,1))
hwCpuEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:hwCpuEntry.setStatus(_A)
_HwCpuIndex_Type=Integer32
_HwCpuIndex_Object=MibTableColumn
hwCpuIndex=_HwCpuIndex_Object((1,3,6,1,4,1,43,45,1,6,1,1,1,1),_HwCpuIndex_Type())
hwCpuIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwCpuIndex.setStatus(_A)
_HwCpuCostRate_Type=Gauge32
_HwCpuCostRate_Object=MibTableColumn
hwCpuCostRate=_HwCpuCostRate_Object((1,3,6,1,4,1,43,45,1,6,1,1,1,2),_HwCpuCostRate_Type())
hwCpuCostRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hwCpuCostRate.setStatus(_A)
_HwCpuCostRatePer1Min_Type=Gauge32
_HwCpuCostRatePer1Min_Object=MibTableColumn
hwCpuCostRatePer1Min=_HwCpuCostRatePer1Min_Object((1,3,6,1,4,1,43,45,1,6,1,1,1,3),_HwCpuCostRatePer1Min_Type())
hwCpuCostRatePer1Min.setMaxAccess(_B)
if mibBuilder.loadTexts:hwCpuCostRatePer1Min.setStatus(_A)
_HwCpuCostRatePer5Min_Type=Gauge32
_HwCpuCostRatePer5Min_Object=MibTableColumn
hwCpuCostRatePer5Min=_HwCpuCostRatePer5Min_Object((1,3,6,1,4,1,43,45,1,6,1,1,1,4),_HwCpuCostRatePer5Min_Type())
hwCpuCostRatePer5Min.setMaxAccess(_B)
if mibBuilder.loadTexts:hwCpuCostRatePer5Min.setStatus(_A)
_HwMem_ObjectIdentity=ObjectIdentity
hwMem=_HwMem_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,1,2))
_HwMemTable_Object=MibTable
hwMemTable=_HwMemTable_Object((1,3,6,1,4,1,43,45,1,6,1,2,1))
if mibBuilder.loadTexts:hwMemTable.setStatus(_A)
_HwMemEntry_Object=MibTableRow
hwMemEntry=_HwMemEntry_Object((1,3,6,1,4,1,43,45,1,6,1,2,1,1))
hwMemEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:hwMemEntry.setStatus(_A)
_HwMemModuleIndex_Type=Integer32
_HwMemModuleIndex_Object=MibTableColumn
hwMemModuleIndex=_HwMemModuleIndex_Object((1,3,6,1,4,1,43,45,1,6,1,2,1,1,1),_HwMemModuleIndex_Type())
hwMemModuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMemModuleIndex.setStatus(_A)
_HwMemSize_Type=Gauge32
_HwMemSize_Object=MibTableColumn
hwMemSize=_HwMemSize_Object((1,3,6,1,4,1,43,45,1,6,1,2,1,1,2),_HwMemSize_Type())
hwMemSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hwMemSize.setStatus(_A)
_HwMemFree_Type=Gauge32
_HwMemFree_Object=MibTableColumn
hwMemFree=_HwMemFree_Object((1,3,6,1,4,1,43,45,1,6,1,2,1,1,3),_HwMemFree_Type())
hwMemFree.setMaxAccess(_B)
if mibBuilder.loadTexts:hwMemFree.setStatus(_A)
_HwMemRawSliceUsed_Type=Gauge32
_HwMemRawSliceUsed_Object=MibTableColumn
hwMemRawSliceUsed=_HwMemRawSliceUsed_Object((1,3,6,1,4,1,43,45,1,6,1,2,1,1,4),_HwMemRawSliceUsed_Type())
hwMemRawSliceUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:hwMemRawSliceUsed.setStatus(_A)
_HwMemLgFree_Type=Gauge32
_HwMemLgFree_Object=MibTableColumn
hwMemLgFree=_HwMemLgFree_Object((1,3,6,1,4,1,43,45,1,6,1,2,1,1,5),_HwMemLgFree_Type())
hwMemLgFree.setMaxAccess(_B)
if mibBuilder.loadTexts:hwMemLgFree.setStatus(_A)
_HwMemFail_Type=Gauge32
_HwMemFail_Object=MibTableColumn
hwMemFail=_HwMemFail_Object((1,3,6,1,4,1,43,45,1,6,1,2,1,1,6),_HwMemFail_Type())
hwMemFail.setMaxAccess(_B)
if mibBuilder.loadTexts:hwMemFail.setStatus(_A)
_HwMemFailNoMem_Type=Gauge32
_HwMemFailNoMem_Object=MibTableColumn
hwMemFailNoMem=_HwMemFailNoMem_Object((1,3,6,1,4,1,43,45,1,6,1,2,1,1,7),_HwMemFailNoMem_Type())
hwMemFailNoMem.setMaxAccess(_B)
if mibBuilder.loadTexts:hwMemFailNoMem.setStatus(_A)
_HwBufTable_Object=MibTable
hwBufTable=_HwBufTable_Object((1,3,6,1,4,1,43,45,1,6,1,2,2))
if mibBuilder.loadTexts:hwBufTable.setStatus(_A)
_HwBufEntry_Object=MibTableRow
hwBufEntry=_HwBufEntry_Object((1,3,6,1,4,1,43,45,1,6,1,2,2,1))
hwBufEntry.setIndexNames((0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:hwBufEntry.setStatus(_A)
_HwBufModuleIndex_Type=Integer32
_HwBufModuleIndex_Object=MibTableColumn
hwBufModuleIndex=_HwBufModuleIndex_Object((1,3,6,1,4,1,43,45,1,6,1,2,2,1,1),_HwBufModuleIndex_Type())
hwBufModuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwBufModuleIndex.setStatus(_A)
_HwBufSize_Type=Integer32
_HwBufSize_Object=MibTableColumn
hwBufSize=_HwBufSize_Object((1,3,6,1,4,1,43,45,1,6,1,2,2,1,2),_HwBufSize_Type())
hwBufSize.setMaxAccess(_F)
if mibBuilder.loadTexts:hwBufSize.setStatus(_A)
_HwBufCurrentTotal_Type=Gauge32
_HwBufCurrentTotal_Object=MibTableColumn
hwBufCurrentTotal=_HwBufCurrentTotal_Object((1,3,6,1,4,1,43,45,1,6,1,2,2,1,3),_HwBufCurrentTotal_Type())
hwBufCurrentTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:hwBufCurrentTotal.setStatus(_A)
_HwBufCurrentUsed_Type=Gauge32
_HwBufCurrentUsed_Object=MibTableColumn
hwBufCurrentUsed=_HwBufCurrentUsed_Object((1,3,6,1,4,1,43,45,1,6,1,2,2,1,4),_HwBufCurrentUsed_Type())
hwBufCurrentUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:hwBufCurrentUsed.setStatus(_A)
_HwFlh_ObjectIdentity=ObjectIdentity
hwFlh=_HwFlh_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,1,3))
_HwFlhTotalSize_Type=Integer32
_HwFlhTotalSize_Object=MibScalar
hwFlhTotalSize=_HwFlhTotalSize_Object((1,3,6,1,4,1,43,45,1,6,1,3,1),_HwFlhTotalSize_Type())
hwFlhTotalSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hwFlhTotalSize.setStatus(_A)
_HwFlhTotalFree_Type=Integer32
_HwFlhTotalFree_Object=MibScalar
hwFlhTotalFree=_HwFlhTotalFree_Object((1,3,6,1,4,1,43,45,1,6,1,3,2),_HwFlhTotalFree_Type())
hwFlhTotalFree.setMaxAccess(_B)
if mibBuilder.loadTexts:hwFlhTotalFree.setStatus(_A)
class _HwFlhLastDelTime_Type(TimeTicks):defaultValue=0
_HwFlhLastDelTime_Type.__name__=_J
_HwFlhLastDelTime_Object=MibScalar
hwFlhLastDelTime=_HwFlhLastDelTime_Object((1,3,6,1,4,1,43,45,1,6,1,3,3),_HwFlhLastDelTime_Type())
hwFlhLastDelTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwFlhLastDelTime.setStatus(_A)
class _HwFlhDelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('executing',1),('ok',2),('error',3),('readOnly',4),('failtoopen',5),('blockMallocFail',6),('noneDelOperationSinceStart',7)))
_HwFlhDelState_Type.__name__=_C
_HwFlhDelState_Object=MibScalar
hwFlhDelState=_HwFlhDelState_Object((1,3,6,1,4,1,43,45,1,6,1,3,4),_HwFlhDelState_Type())
hwFlhDelState.setMaxAccess(_B)
if mibBuilder.loadTexts:hwFlhDelState.setStatus(_A)
class _HwFlhState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('busy',1),('free',2)))
_HwFlhState_Type.__name__=_C
_HwFlhState_Object=MibScalar
hwFlhState=_HwFlhState_Object((1,3,6,1,4,1,43,45,1,6,1,3,5),_HwFlhState_Type())
hwFlhState.setMaxAccess(_B)
if mibBuilder.loadTexts:hwFlhState.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hwLswdevMMib':hwLswdevMMib,'hwLswdevMMibObject':hwLswdevMMibObject,'hwdevMFanStatusTable':hwdevMFanStatusTable,'hwdevMFanStatusEntry':hwdevMFanStatusEntry,_K:hwDevMFanNum,'hwDevMFanStatus':hwDevMFanStatus,'hwdevMPowerStatusTable':hwdevMPowerStatusTable,'hwdevMPowerStatusEntry':hwdevMPowerStatusEntry,_P:hwDevMPowerNum,'hwDevMPowerStatus':hwDevMPowerStatus,'hwdevMSlotEnvironmentTable':hwdevMSlotEnvironmentTable,'hwdevMSlotEnvironmentEntry':hwdevMSlotEnvironmentEntry,_Q:hwdevMSlotEnvironmentType,'hwDevMSlotEnvironmentStatus':hwDevMSlotEnvironmentStatus,'hwDevMSlotEnvironmentValue':hwDevMSlotEnvironmentValue,'hwDevMSlotEnvironmentUpperLimit':hwDevMSlotEnvironmentUpperLimit,'hwDevMSlotEnvironmentLowerLimit':hwDevMSlotEnvironmentLowerLimit,'hwLinkUpDownTrapEnable':hwLinkUpDownTrapEnable,'hwdot1qTpFdbLearnStatus':hwdot1qTpFdbLearnStatus,'hwCfmWriteFlash':hwCfmWriteFlash,'hwCfmEraseFlash':hwCfmEraseFlash,'hwDevMFirstTrapTime':hwDevMFirstTrapTime,'hwDevice':hwDevice,'hwCpuTable':hwCpuTable,'hwCpuEntry':hwCpuEntry,_R:hwCpuIndex,'hwCpuCostRate':hwCpuCostRate,'hwCpuCostRatePer1Min':hwCpuCostRatePer1Min,'hwCpuCostRatePer5Min':hwCpuCostRatePer5Min,'hwMem':hwMem,'hwMemTable':hwMemTable,'hwMemEntry':hwMemEntry,_S:hwMemModuleIndex,'hwMemSize':hwMemSize,'hwMemFree':hwMemFree,'hwMemRawSliceUsed':hwMemRawSliceUsed,'hwMemLgFree':hwMemLgFree,'hwMemFail':hwMemFail,'hwMemFailNoMem':hwMemFailNoMem,'hwBufTable':hwBufTable,'hwBufEntry':hwBufEntry,_T:hwBufModuleIndex,_U:hwBufSize,'hwBufCurrentTotal':hwBufCurrentTotal,'hwBufCurrentUsed':hwBufCurrentUsed,'hwFlh':hwFlh,'hwFlhTotalSize':hwFlhTotalSize,'hwFlhTotalFree':hwFlhTotalFree,'hwFlhLastDelTime':hwFlhLastDelTime,'hwFlhDelState':hwFlhDelState,'hwFlhState':hwFlhState})