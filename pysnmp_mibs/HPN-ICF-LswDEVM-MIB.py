_U='hpnicfdevMSlotEnvironmentType'
_T='hpnicfDevMPowerNum'
_S='unsupport'
_R='not-install'
_Q='deactive'
_P='active'
_O='hpnicfDevMFanNum'
_N='hpnicfBufSize'
_M='hpnicfBufModuleIndex'
_L='hpnicfMemModuleIndex'
_K='hpnicfCpuIndex'
_J='TimeTicks'
_I='hpnicfLswSlotIndex'
_H='hpnicfLswFrameIndex'
_G='HPN-ICF-LSW-DEV-ADM-MIB'
_F='not-accessible'
_E='read-write'
_D='HPN-ICF-LswDEVM-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfLswFrameIndex,hpnicfLswSlotIndex=mibBuilder.importSymbols(_G,_H,_I)
hpnicfRhw,hpnicflswCommon=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfRhw','hpnicflswCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_J,'Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfLswdevMMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,9))
if mibBuilder.loadTexts:hpnicfLswdevMMib.setRevisions(('2001-06-29 00:00',))
_HpnicfDevice_ObjectIdentity=ObjectIdentity
hpnicfDevice=_HpnicfDevice_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,8))
_HpnicfCpuTable_Object=MibTable
hpnicfCpuTable=_HpnicfCpuTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,1))
if mibBuilder.loadTexts:hpnicfCpuTable.setStatus(_A)
_HpnicfCpuEntry_Object=MibTableRow
hpnicfCpuEntry=_HpnicfCpuEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,1,1))
hpnicfCpuEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:hpnicfCpuEntry.setStatus(_A)
_HpnicfCpuIndex_Type=Integer32
_HpnicfCpuIndex_Object=MibTableColumn
hpnicfCpuIndex=_HpnicfCpuIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,1,1,1),_HpnicfCpuIndex_Type())
hpnicfCpuIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCpuIndex.setStatus(_A)
_HpnicfCpuCostRate_Type=Gauge32
_HpnicfCpuCostRate_Object=MibTableColumn
hpnicfCpuCostRate=_HpnicfCpuCostRate_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,1,1,2),_HpnicfCpuCostRate_Type())
hpnicfCpuCostRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCpuCostRate.setStatus(_A)
_HpnicfCpuCostRatePer1Min_Type=Gauge32
_HpnicfCpuCostRatePer1Min_Object=MibTableColumn
hpnicfCpuCostRatePer1Min=_HpnicfCpuCostRatePer1Min_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,1,1,3),_HpnicfCpuCostRatePer1Min_Type())
hpnicfCpuCostRatePer1Min.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCpuCostRatePer1Min.setStatus(_A)
_HpnicfCpuCostRatePer5Min_Type=Gauge32
_HpnicfCpuCostRatePer5Min_Object=MibTableColumn
hpnicfCpuCostRatePer5Min=_HpnicfCpuCostRatePer5Min_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,1,1,4),_HpnicfCpuCostRatePer5Min_Type())
hpnicfCpuCostRatePer5Min.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCpuCostRatePer5Min.setStatus(_A)
_HpnicfMem_ObjectIdentity=ObjectIdentity
hpnicfMem=_HpnicfMem_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,8,2))
_HpnicfMemTable_Object=MibTable
hpnicfMemTable=_HpnicfMemTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,2,1))
if mibBuilder.loadTexts:hpnicfMemTable.setStatus(_A)
_HpnicfMemEntry_Object=MibTableRow
hpnicfMemEntry=_HpnicfMemEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,2,1,1))
hpnicfMemEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:hpnicfMemEntry.setStatus(_A)
_HpnicfMemModuleIndex_Type=Integer32
_HpnicfMemModuleIndex_Object=MibTableColumn
hpnicfMemModuleIndex=_HpnicfMemModuleIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,2,1,1,1),_HpnicfMemModuleIndex_Type())
hpnicfMemModuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMemModuleIndex.setStatus(_A)
_HpnicfMemSize_Type=Gauge32
_HpnicfMemSize_Object=MibTableColumn
hpnicfMemSize=_HpnicfMemSize_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,2,1,1,2),_HpnicfMemSize_Type())
hpnicfMemSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMemSize.setStatus(_A)
_HpnicfMemFree_Type=Gauge32
_HpnicfMemFree_Object=MibTableColumn
hpnicfMemFree=_HpnicfMemFree_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,2,1,1,3),_HpnicfMemFree_Type())
hpnicfMemFree.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMemFree.setStatus(_A)
_HpnicfMemRawSliceUsed_Type=Gauge32
_HpnicfMemRawSliceUsed_Object=MibTableColumn
hpnicfMemRawSliceUsed=_HpnicfMemRawSliceUsed_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,2,1,1,4),_HpnicfMemRawSliceUsed_Type())
hpnicfMemRawSliceUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMemRawSliceUsed.setStatus(_A)
_HpnicfMemLgFree_Type=Gauge32
_HpnicfMemLgFree_Object=MibTableColumn
hpnicfMemLgFree=_HpnicfMemLgFree_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,2,1,1,5),_HpnicfMemLgFree_Type())
hpnicfMemLgFree.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMemLgFree.setStatus(_A)
_HpnicfMemFail_Type=Gauge32
_HpnicfMemFail_Object=MibTableColumn
hpnicfMemFail=_HpnicfMemFail_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,2,1,1,6),_HpnicfMemFail_Type())
hpnicfMemFail.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMemFail.setStatus(_A)
_HpnicfMemFailNoMem_Type=Gauge32
_HpnicfMemFailNoMem_Object=MibTableColumn
hpnicfMemFailNoMem=_HpnicfMemFailNoMem_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,2,1,1,7),_HpnicfMemFailNoMem_Type())
hpnicfMemFailNoMem.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMemFailNoMem.setStatus(_A)
_HpnicfBufTable_Object=MibTable
hpnicfBufTable=_HpnicfBufTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,2,2))
if mibBuilder.loadTexts:hpnicfBufTable.setStatus(_A)
_HpnicfBufEntry_Object=MibTableRow
hpnicfBufEntry=_HpnicfBufEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,2,2,1))
hpnicfBufEntry.setIndexNames((0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:hpnicfBufEntry.setStatus(_A)
_HpnicfBufModuleIndex_Type=Integer32
_HpnicfBufModuleIndex_Object=MibTableColumn
hpnicfBufModuleIndex=_HpnicfBufModuleIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,2,2,1,1),_HpnicfBufModuleIndex_Type())
hpnicfBufModuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfBufModuleIndex.setStatus(_A)
_HpnicfBufSize_Type=Integer32
_HpnicfBufSize_Object=MibTableColumn
hpnicfBufSize=_HpnicfBufSize_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,2,2,1,2),_HpnicfBufSize_Type())
hpnicfBufSize.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfBufSize.setStatus(_A)
_HpnicfBufCurrentTotal_Type=Gauge32
_HpnicfBufCurrentTotal_Object=MibTableColumn
hpnicfBufCurrentTotal=_HpnicfBufCurrentTotal_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,2,2,1,3),_HpnicfBufCurrentTotal_Type())
hpnicfBufCurrentTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBufCurrentTotal.setStatus(_A)
_HpnicfBufCurrentUsed_Type=Gauge32
_HpnicfBufCurrentUsed_Object=MibTableColumn
hpnicfBufCurrentUsed=_HpnicfBufCurrentUsed_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,2,2,1,4),_HpnicfBufCurrentUsed_Type())
hpnicfBufCurrentUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBufCurrentUsed.setStatus(_A)
_HpnicfFlh_ObjectIdentity=ObjectIdentity
hpnicfFlh=_HpnicfFlh_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,8,3))
_HpnicfFlhTotalSize_Type=Integer32
_HpnicfFlhTotalSize_Object=MibScalar
hpnicfFlhTotalSize=_HpnicfFlhTotalSize_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,3,1),_HpnicfFlhTotalSize_Type())
hpnicfFlhTotalSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFlhTotalSize.setStatus(_A)
_HpnicfFlhTotalFree_Type=Integer32
_HpnicfFlhTotalFree_Object=MibScalar
hpnicfFlhTotalFree=_HpnicfFlhTotalFree_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,3,2),_HpnicfFlhTotalFree_Type())
hpnicfFlhTotalFree.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFlhTotalFree.setStatus(_A)
class _HpnicfFlhLastDelTime_Type(TimeTicks):defaultValue=0
_HpnicfFlhLastDelTime_Type.__name__=_J
_HpnicfFlhLastDelTime_Object=MibScalar
hpnicfFlhLastDelTime=_HpnicfFlhLastDelTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,3,3),_HpnicfFlhLastDelTime_Type())
hpnicfFlhLastDelTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFlhLastDelTime.setStatus(_A)
class _HpnicfFlhDelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('executing',1),('ok',2),('error',3),('readOnly',4),('failtoopen',5),('blockMallocFail',6),('noneDelOperationSinceStart',7)))
_HpnicfFlhDelState_Type.__name__=_C
_HpnicfFlhDelState_Object=MibScalar
hpnicfFlhDelState=_HpnicfFlhDelState_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,3,4),_HpnicfFlhDelState_Type())
hpnicfFlhDelState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFlhDelState.setStatus(_A)
class _HpnicfFlhState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('busy',1),('free',2)))
_HpnicfFlhState_Type.__name__=_C
_HpnicfFlhState_Object=MibScalar
hpnicfFlhState=_HpnicfFlhState_Object((1,3,6,1,4,1,11,2,14,11,15,8,8,3,5),_HpnicfFlhState_Type())
hpnicfFlhState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFlhState.setStatus(_A)
_HpnicfLswdevMMibObject_ObjectIdentity=ObjectIdentity
hpnicfLswdevMMibObject=_HpnicfLswdevMMibObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1))
if mibBuilder.loadTexts:hpnicfLswdevMMibObject.setStatus(_A)
_HpnicfdevMFanStatusTable_Object=MibTable
hpnicfdevMFanStatusTable=_HpnicfdevMFanStatusTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,1))
if mibBuilder.loadTexts:hpnicfdevMFanStatusTable.setStatus(_A)
_HpnicfdevMFanStatusEntry_Object=MibTableRow
hpnicfdevMFanStatusEntry=_HpnicfdevMFanStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,1,1))
hpnicfdevMFanStatusEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:hpnicfdevMFanStatusEntry.setStatus(_A)
_HpnicfDevMFanNum_Type=Integer32
_HpnicfDevMFanNum_Object=MibTableColumn
hpnicfDevMFanNum=_HpnicfDevMFanNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,1,1,1),_HpnicfDevMFanNum_Type())
hpnicfDevMFanNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDevMFanNum.setStatus(_A)
class _HpnicfDevMFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4)))
_HpnicfDevMFanStatus_Type.__name__=_C
_HpnicfDevMFanStatus_Object=MibTableColumn
hpnicfDevMFanStatus=_HpnicfDevMFanStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,1,1,2),_HpnicfDevMFanStatus_Type())
hpnicfDevMFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDevMFanStatus.setStatus(_A)
_HpnicfdevMPowerStatusTable_Object=MibTable
hpnicfdevMPowerStatusTable=_HpnicfdevMPowerStatusTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,2))
if mibBuilder.loadTexts:hpnicfdevMPowerStatusTable.setStatus(_A)
_HpnicfdevMPowerStatusEntry_Object=MibTableRow
hpnicfdevMPowerStatusEntry=_HpnicfdevMPowerStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,2,1))
hpnicfdevMPowerStatusEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:hpnicfdevMPowerStatusEntry.setStatus(_A)
_HpnicfDevMPowerNum_Type=Integer32
_HpnicfDevMPowerNum_Object=MibTableColumn
hpnicfDevMPowerNum=_HpnicfDevMPowerNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,2,1,1),_HpnicfDevMPowerNum_Type())
hpnicfDevMPowerNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDevMPowerNum.setStatus(_A)
class _HpnicfDevMPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4)))
_HpnicfDevMPowerStatus_Type.__name__=_C
_HpnicfDevMPowerStatus_Object=MibTableColumn
hpnicfDevMPowerStatus=_HpnicfDevMPowerStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,2,1,2),_HpnicfDevMPowerStatus_Type())
hpnicfDevMPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDevMPowerStatus.setStatus(_A)
_HpnicfdevMSlotEnvironmentTable_Object=MibTable
hpnicfdevMSlotEnvironmentTable=_HpnicfdevMSlotEnvironmentTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,3))
if mibBuilder.loadTexts:hpnicfdevMSlotEnvironmentTable.setStatus(_A)
_HpnicfdevMSlotEnvironmentEntry_Object=MibTableRow
hpnicfdevMSlotEnvironmentEntry=_HpnicfdevMSlotEnvironmentEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,3,1))
hpnicfdevMSlotEnvironmentEntry.setIndexNames((0,_G,_H),(0,_G,_I),(0,_D,_U))
if mibBuilder.loadTexts:hpnicfdevMSlotEnvironmentEntry.setStatus(_A)
class _HpnicfdevMSlotEnvironmentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('temperature',1),('humidity',2),('fog',3)))
_HpnicfdevMSlotEnvironmentType_Type.__name__=_C
_HpnicfdevMSlotEnvironmentType_Object=MibTableColumn
hpnicfdevMSlotEnvironmentType=_HpnicfdevMSlotEnvironmentType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,3,1,1),_HpnicfdevMSlotEnvironmentType_Type())
hpnicfdevMSlotEnvironmentType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfdevMSlotEnvironmentType.setStatus(_A)
class _HpnicfDevMSlotEnvironmentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('upper',2),('lower',3)))
_HpnicfDevMSlotEnvironmentStatus_Type.__name__=_C
_HpnicfDevMSlotEnvironmentStatus_Object=MibTableColumn
hpnicfDevMSlotEnvironmentStatus=_HpnicfDevMSlotEnvironmentStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,3,1,2),_HpnicfDevMSlotEnvironmentStatus_Type())
hpnicfDevMSlotEnvironmentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDevMSlotEnvironmentStatus.setStatus(_A)
_HpnicfDevMSlotEnvironmentValue_Type=Integer32
_HpnicfDevMSlotEnvironmentValue_Object=MibTableColumn
hpnicfDevMSlotEnvironmentValue=_HpnicfDevMSlotEnvironmentValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,3,1,3),_HpnicfDevMSlotEnvironmentValue_Type())
hpnicfDevMSlotEnvironmentValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDevMSlotEnvironmentValue.setStatus(_A)
_HpnicfDevMSlotEnvironmentUpperLimit_Type=Integer32
_HpnicfDevMSlotEnvironmentUpperLimit_Object=MibTableColumn
hpnicfDevMSlotEnvironmentUpperLimit=_HpnicfDevMSlotEnvironmentUpperLimit_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,3,1,4),_HpnicfDevMSlotEnvironmentUpperLimit_Type())
hpnicfDevMSlotEnvironmentUpperLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDevMSlotEnvironmentUpperLimit.setStatus(_A)
_HpnicfDevMSlotEnvironmentLowerLimit_Type=Integer32
_HpnicfDevMSlotEnvironmentLowerLimit_Object=MibTableColumn
hpnicfDevMSlotEnvironmentLowerLimit=_HpnicfDevMSlotEnvironmentLowerLimit_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,3,1,5),_HpnicfDevMSlotEnvironmentLowerLimit_Type())
hpnicfDevMSlotEnvironmentLowerLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDevMSlotEnvironmentLowerLimit.setStatus(_A)
class _HpnicfLinkUpDownTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('enableBoth',1),('disableBoth',2),('enableLinkUpTrapOnly',3),('enableLinkDownTrapOnly',4)))
_HpnicfLinkUpDownTrapEnable_Type.__name__=_C
_HpnicfLinkUpDownTrapEnable_Object=MibScalar
hpnicfLinkUpDownTrapEnable=_HpnicfLinkUpDownTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,9),_HpnicfLinkUpDownTrapEnable_Type())
hpnicfLinkUpDownTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfLinkUpDownTrapEnable.setStatus(_A)
class _Hpnicfdot1qTpFdbLearnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_Hpnicfdot1qTpFdbLearnStatus_Type.__name__=_C
_Hpnicfdot1qTpFdbLearnStatus_Object=MibScalar
hpnicfdot1qTpFdbLearnStatus=_Hpnicfdot1qTpFdbLearnStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,10),_Hpnicfdot1qTpFdbLearnStatus_Type())
hpnicfdot1qTpFdbLearnStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdot1qTpFdbLearnStatus.setStatus(_A)
class _HpnicfCfmWriteFlash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('write',1))
_HpnicfCfmWriteFlash_Type.__name__=_C
_HpnicfCfmWriteFlash_Object=MibScalar
hpnicfCfmWriteFlash=_HpnicfCfmWriteFlash_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,11),_HpnicfCfmWriteFlash_Type())
hpnicfCfmWriteFlash.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCfmWriteFlash.setStatus(_A)
class _HpnicfCfmEraseFlash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('erase',1))
_HpnicfCfmEraseFlash_Type.__name__=_C
_HpnicfCfmEraseFlash_Object=MibScalar
hpnicfCfmEraseFlash=_HpnicfCfmEraseFlash_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,12),_HpnicfCfmEraseFlash_Type())
hpnicfCfmEraseFlash.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCfmEraseFlash.setStatus(_A)
_HpnicfDevMFirstTrapTime_Type=TimeTicks
_HpnicfDevMFirstTrapTime_Object=MibScalar
hpnicfDevMFirstTrapTime=_HpnicfDevMFirstTrapTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,13),_HpnicfDevMFirstTrapTime_Type())
hpnicfDevMFirstTrapTime.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hpnicfDevMFirstTrapTime.setStatus(_A)
_HpnicfdevMExternalAlarmStatus_ObjectIdentity=ObjectIdentity
hpnicfdevMExternalAlarmStatus=_HpnicfdevMExternalAlarmStatus_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,9,1,14))
mibBuilder.exportSymbols(_D,**{'hpnicfDevice':hpnicfDevice,'hpnicfCpuTable':hpnicfCpuTable,'hpnicfCpuEntry':hpnicfCpuEntry,_K:hpnicfCpuIndex,'hpnicfCpuCostRate':hpnicfCpuCostRate,'hpnicfCpuCostRatePer1Min':hpnicfCpuCostRatePer1Min,'hpnicfCpuCostRatePer5Min':hpnicfCpuCostRatePer5Min,'hpnicfMem':hpnicfMem,'hpnicfMemTable':hpnicfMemTable,'hpnicfMemEntry':hpnicfMemEntry,_L:hpnicfMemModuleIndex,'hpnicfMemSize':hpnicfMemSize,'hpnicfMemFree':hpnicfMemFree,'hpnicfMemRawSliceUsed':hpnicfMemRawSliceUsed,'hpnicfMemLgFree':hpnicfMemLgFree,'hpnicfMemFail':hpnicfMemFail,'hpnicfMemFailNoMem':hpnicfMemFailNoMem,'hpnicfBufTable':hpnicfBufTable,'hpnicfBufEntry':hpnicfBufEntry,_M:hpnicfBufModuleIndex,_N:hpnicfBufSize,'hpnicfBufCurrentTotal':hpnicfBufCurrentTotal,'hpnicfBufCurrentUsed':hpnicfBufCurrentUsed,'hpnicfFlh':hpnicfFlh,'hpnicfFlhTotalSize':hpnicfFlhTotalSize,'hpnicfFlhTotalFree':hpnicfFlhTotalFree,'hpnicfFlhLastDelTime':hpnicfFlhLastDelTime,'hpnicfFlhDelState':hpnicfFlhDelState,'hpnicfFlhState':hpnicfFlhState,'hpnicfLswdevMMib':hpnicfLswdevMMib,'hpnicfLswdevMMibObject':hpnicfLswdevMMibObject,'hpnicfdevMFanStatusTable':hpnicfdevMFanStatusTable,'hpnicfdevMFanStatusEntry':hpnicfdevMFanStatusEntry,_O:hpnicfDevMFanNum,'hpnicfDevMFanStatus':hpnicfDevMFanStatus,'hpnicfdevMPowerStatusTable':hpnicfdevMPowerStatusTable,'hpnicfdevMPowerStatusEntry':hpnicfdevMPowerStatusEntry,_T:hpnicfDevMPowerNum,'hpnicfDevMPowerStatus':hpnicfDevMPowerStatus,'hpnicfdevMSlotEnvironmentTable':hpnicfdevMSlotEnvironmentTable,'hpnicfdevMSlotEnvironmentEntry':hpnicfdevMSlotEnvironmentEntry,_U:hpnicfdevMSlotEnvironmentType,'hpnicfDevMSlotEnvironmentStatus':hpnicfDevMSlotEnvironmentStatus,'hpnicfDevMSlotEnvironmentValue':hpnicfDevMSlotEnvironmentValue,'hpnicfDevMSlotEnvironmentUpperLimit':hpnicfDevMSlotEnvironmentUpperLimit,'hpnicfDevMSlotEnvironmentLowerLimit':hpnicfDevMSlotEnvironmentLowerLimit,'hpnicfLinkUpDownTrapEnable':hpnicfLinkUpDownTrapEnable,'hpnicfdot1qTpFdbLearnStatus':hpnicfdot1qTpFdbLearnStatus,'hpnicfCfmWriteFlash':hpnicfCfmWriteFlash,'hpnicfCfmEraseFlash':hpnicfCfmEraseFlash,'hpnicfDevMFirstTrapTime':hpnicfDevMFirstTrapTime,'hpnicfdevMExternalAlarmStatus':hpnicfdevMExternalAlarmStatus})