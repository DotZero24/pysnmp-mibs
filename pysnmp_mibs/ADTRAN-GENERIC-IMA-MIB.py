_b='adGenImaLinkDayIntervalNumber'
_a='adGenImaLinkIntervalNumber'
_Z='adGenImaGroupDayIntervalNumber'
_Y='adGenImaGroupIntervalNumber'
_X='DisplayString'
_W='MilliSeconds'
_V='ImaTestProcStatus'
_U='ImaGroupTxClkMode'
_T='ImaGroupSymmetry'
_S='ImaFrameLength'
_R='InterfaceIndexOrZero'
_Q='not-accessible'
_P='reset'
_O='ADTRAN-GENERIC-IMA-MIB'
_N='read-write'
_M='adGenPortTrapIdentifier'
_L='ADTRAN-GENPORT-MIB'
_K='Integer32'
_J='sysName'
_I='SNMPv2-MIB'
_H='adTrapInformSeqNum'
_G='ADTRAN-GENTRAPINFORM-MIB'
_F='adGenSlotInfoIndex'
_E='ADTRAN-GENSLOT-MIB'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPortTrapIdentifier,=mibBuilder.importSymbols(_L,_M)
adGenSlotInfoIndex,=mibBuilder.importSymbols(_E,_F)
adGenIma,adGenImaID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adGenIma','adGenImaID')
adTrapInformSeqNum,=mibBuilder.importSymbols(_G,_H)
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_C,_R,_D)
ImaFrameLength,ImaGroupFailureStatus,ImaGroupState,ImaGroupSymmetry,ImaGroupTxClkMode,ImaLinkFailureStatus,ImaLinkState,ImaTestProcStatus,MilliSeconds=mibBuilder.importSymbols('IMA-MIB',_S,'ImaGroupFailureStatus','ImaGroupState',_T,_U,'ImaLinkFailureStatus','ImaLinkState',_V,_W)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_I,_J)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_X,'PhysAddress','TextualConvention')
adGenImaMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,25,1))
if mibBuilder.loadTexts:adGenImaMIB.setRevisions(('2011-10-07 00:00','2008-04-24 00:00'))
_AdGenImaProvisioning_ObjectIdentity=ObjectIdentity
adGenImaProvisioning=_AdGenImaProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,25,1))
_AdGenImaGroupProvTable_Object=MibTable
adGenImaGroupProvTable=_AdGenImaGroupProvTable_Object((1,3,6,1,4,1,664,5,67,1,25,1,1))
if mibBuilder.loadTexts:adGenImaGroupProvTable.setStatus(_A)
_AdGenImaGroupProvEntry_Object=MibTableRow
adGenImaGroupProvEntry=_AdGenImaGroupProvEntry_Object((1,3,6,1,4,1,664,5,67,1,25,1,1,1))
adGenImaGroupProvEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenImaGroupProvEntry.setStatus(_A)
class _AdGenImaGroupVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('version1Point0Alt',1),('version1Point1',2),('version1Point0',3)))
_AdGenImaGroupVersion_Type.__name__=_K
_AdGenImaGroupVersion_Object=MibTableColumn
adGenImaGroupVersion=_AdGenImaGroupVersion_Object((1,3,6,1,4,1,664,5,67,1,25,1,1,1,1),_AdGenImaGroupVersion_Type())
adGenImaGroupVersion.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaGroupVersion.setStatus(_A)
class _AdGenImaGroupSymmetry_Type(ImaGroupSymmetry):defaultValue=1
_AdGenImaGroupSymmetry_Type.__name__=_T
_AdGenImaGroupSymmetry_Object=MibTableColumn
adGenImaGroupSymmetry=_AdGenImaGroupSymmetry_Object((1,3,6,1,4,1,664,5,67,1,25,1,1,1,2),_AdGenImaGroupSymmetry_Type())
adGenImaGroupSymmetry.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaGroupSymmetry.setStatus(_A)
class _AdGenImaGroupNeTxClkMode_Type(ImaGroupTxClkMode):defaultValue=1
_AdGenImaGroupNeTxClkMode_Type.__name__=_U
_AdGenImaGroupNeTxClkMode_Object=MibTableColumn
adGenImaGroupNeTxClkMode=_AdGenImaGroupNeTxClkMode_Object((1,3,6,1,4,1,664,5,67,1,25,1,1,1,3),_AdGenImaGroupNeTxClkMode_Type())
adGenImaGroupNeTxClkMode.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaGroupNeTxClkMode.setStatus(_A)
class _AdGenImaGroupTxImaId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenImaGroupTxImaId_Type.__name__=_K
_AdGenImaGroupTxImaId_Object=MibTableColumn
adGenImaGroupTxImaId=_AdGenImaGroupTxImaId_Object((1,3,6,1,4,1,664,5,67,1,25,1,1,1,4),_AdGenImaGroupTxImaId_Type())
adGenImaGroupTxImaId.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaGroupTxImaId.setStatus(_A)
class _AdGenImaGroupTxFrameLength_Type(ImaFrameLength):defaultValue=128
_AdGenImaGroupTxFrameLength_Type.__name__=_S
_AdGenImaGroupTxFrameLength_Object=MibTableColumn
adGenImaGroupTxFrameLength=_AdGenImaGroupTxFrameLength_Object((1,3,6,1,4,1,664,5,67,1,25,1,1,1,5),_AdGenImaGroupTxFrameLength_Type())
adGenImaGroupTxFrameLength.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaGroupTxFrameLength.setStatus(_A)
class _AdGenImaGroupDiffDelayMax_Type(MilliSeconds):defaultValue=25
_AdGenImaGroupDiffDelayMax_Type.__name__=_W
_AdGenImaGroupDiffDelayMax_Object=MibTableColumn
adGenImaGroupDiffDelayMax=_AdGenImaGroupDiffDelayMax_Object((1,3,6,1,4,1,664,5,67,1,25,1,1,1,6),_AdGenImaGroupDiffDelayMax_Type())
adGenImaGroupDiffDelayMax.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaGroupDiffDelayMax.setStatus(_A)
class _AdGenImaGroupAlphaValue_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AdGenImaGroupAlphaValue_Type.__name__=_K
_AdGenImaGroupAlphaValue_Object=MibTableColumn
adGenImaGroupAlphaValue=_AdGenImaGroupAlphaValue_Object((1,3,6,1,4,1,664,5,67,1,25,1,1,1,7),_AdGenImaGroupAlphaValue_Type())
adGenImaGroupAlphaValue.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaGroupAlphaValue.setStatus(_A)
class _AdGenImaGroupBetaValue_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_AdGenImaGroupBetaValue_Type.__name__=_K
_AdGenImaGroupBetaValue_Object=MibTableColumn
adGenImaGroupBetaValue=_AdGenImaGroupBetaValue_Object((1,3,6,1,4,1,664,5,67,1,25,1,1,1,8),_AdGenImaGroupBetaValue_Type())
adGenImaGroupBetaValue.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaGroupBetaValue.setStatus(_A)
class _AdGenImaGroupGammaValue_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_AdGenImaGroupGammaValue_Type.__name__=_K
_AdGenImaGroupGammaValue_Object=MibTableColumn
adGenImaGroupGammaValue=_AdGenImaGroupGammaValue_Object((1,3,6,1,4,1,664,5,67,1,25,1,1,1,9),_AdGenImaGroupGammaValue_Type())
adGenImaGroupGammaValue.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaGroupGammaValue.setStatus(_A)
class _AdGenImaGroupTxClkSource_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('system',1),('loop',2)))
_AdGenImaGroupTxClkSource_Type.__name__=_K
_AdGenImaGroupTxClkSource_Object=MibTableColumn
adGenImaGroupTxClkSource=_AdGenImaGroupTxClkSource_Object((1,3,6,1,4,1,664,5,67,1,25,1,1,1,10),_AdGenImaGroupTxClkSource_Type())
adGenImaGroupTxClkSource.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaGroupTxClkSource.setStatus(_A)
_AdGenImaAtmGroupCommonProvTable_Object=MibTable
adGenImaAtmGroupCommonProvTable=_AdGenImaAtmGroupCommonProvTable_Object((1,3,6,1,4,1,664,5,67,1,25,1,2))
if mibBuilder.loadTexts:adGenImaAtmGroupCommonProvTable.setStatus(_A)
_AdGenImaAtmGroupCommonProvEntry_Object=MibTableRow
adGenImaAtmGroupCommonProvEntry=_AdGenImaAtmGroupCommonProvEntry_Object((1,3,6,1,4,1,664,5,67,1,25,1,2,1))
adGenImaAtmGroupCommonProvEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenImaAtmGroupCommonProvEntry.setStatus(_A)
class _AdGenImaAtmGroupCommonProvDhcpCircuitIdFormat_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_AdGenImaAtmGroupCommonProvDhcpCircuitIdFormat_Type.__name__=_X
_AdGenImaAtmGroupCommonProvDhcpCircuitIdFormat_Object=MibTableColumn
adGenImaAtmGroupCommonProvDhcpCircuitIdFormat=_AdGenImaAtmGroupCommonProvDhcpCircuitIdFormat_Object((1,3,6,1,4,1,664,5,67,1,25,1,2,1,1),_AdGenImaAtmGroupCommonProvDhcpCircuitIdFormat_Type())
adGenImaAtmGroupCommonProvDhcpCircuitIdFormat.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaAtmGroupCommonProvDhcpCircuitIdFormat.setStatus(_A)
_AdGenImaStatus_ObjectIdentity=ObjectIdentity
adGenImaStatus=_AdGenImaStatus_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,25,2))
_AdGenImaGroupStatusTable_Object=MibTable
adGenImaGroupStatusTable=_AdGenImaGroupStatusTable_Object((1,3,6,1,4,1,664,5,67,1,25,2,1))
if mibBuilder.loadTexts:adGenImaGroupStatusTable.setStatus(_A)
_AdGenImaGroupStatusEntry_Object=MibTableRow
adGenImaGroupStatusEntry=_AdGenImaGroupStatusEntry_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1))
adGenImaGroupStatusEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenImaGroupStatusEntry.setStatus(_A)
_AdGenImaGroupNeState_Type=ImaGroupState
_AdGenImaGroupNeState_Object=MibTableColumn
adGenImaGroupNeState=_AdGenImaGroupNeState_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1,1),_AdGenImaGroupNeState_Type())
adGenImaGroupNeState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupNeState.setStatus(_A)
_AdGenImaGroupFeState_Type=ImaGroupState
_AdGenImaGroupFeState_Object=MibTableColumn
adGenImaGroupFeState=_AdGenImaGroupFeState_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1,2),_AdGenImaGroupFeState_Type())
adGenImaGroupFeState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupFeState.setStatus(_A)
_AdGenImaGroupFailureStatus_Type=ImaGroupFailureStatus
_AdGenImaGroupFailureStatus_Object=MibTableColumn
adGenImaGroupFailureStatus=_AdGenImaGroupFailureStatus_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1,3),_AdGenImaGroupFailureStatus_Type())
adGenImaGroupFailureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupFailureStatus.setStatus(_A)
_AdGenImaGroupLastChange_Type=DateAndTime
_AdGenImaGroupLastChange_Object=MibTableColumn
adGenImaGroupLastChange=_AdGenImaGroupLastChange_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1,4),_AdGenImaGroupLastChange_Type())
adGenImaGroupLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupLastChange.setStatus(_A)
_AdGenImaGroupRunningSecs_Type=Gauge32
_AdGenImaGroupRunningSecs_Object=MibTableColumn
adGenImaGroupRunningSecs=_AdGenImaGroupRunningSecs_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1,5),_AdGenImaGroupRunningSecs_Type())
adGenImaGroupRunningSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupRunningSecs.setStatus(_A)
_AdGenImaGroupFeTxClkMode_Type=ImaGroupTxClkMode
_AdGenImaGroupFeTxClkMode_Object=MibTableColumn
adGenImaGroupFeTxClkMode=_AdGenImaGroupFeTxClkMode_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1,6),_AdGenImaGroupFeTxClkMode_Type())
adGenImaGroupFeTxClkMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupFeTxClkMode.setStatus(_A)
_AdGenImaGroupTxTimingRefLink_Type=InterfaceIndexOrZero
_AdGenImaGroupTxTimingRefLink_Object=MibTableColumn
adGenImaGroupTxTimingRefLink=_AdGenImaGroupTxTimingRefLink_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1,7),_AdGenImaGroupTxTimingRefLink_Type())
adGenImaGroupTxTimingRefLink.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupTxTimingRefLink.setStatus(_A)
_AdGenImaGroupRxTimingRefLink_Type=InterfaceIndexOrZero
_AdGenImaGroupRxTimingRefLink_Object=MibTableColumn
adGenImaGroupRxTimingRefLink=_AdGenImaGroupRxTimingRefLink_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1,8),_AdGenImaGroupRxTimingRefLink_Type())
adGenImaGroupRxTimingRefLink.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupRxTimingRefLink.setStatus(_A)
class _AdGenImaGroupRxImaId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenImaGroupRxImaId_Type.__name__=_K
_AdGenImaGroupRxImaId_Object=MibTableColumn
adGenImaGroupRxImaId=_AdGenImaGroupRxImaId_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1,9),_AdGenImaGroupRxImaId_Type())
adGenImaGroupRxImaId.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupRxImaId.setStatus(_A)
_AdGenImaGroupRxFrameLength_Type=ImaFrameLength
_AdGenImaGroupRxFrameLength_Object=MibTableColumn
adGenImaGroupRxFrameLength=_AdGenImaGroupRxFrameLength_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1,10),_AdGenImaGroupRxFrameLength_Type())
adGenImaGroupRxFrameLength.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupRxFrameLength.setStatus(_A)
_AdGenImaGroupLeastDelayLink_Type=InterfaceIndexOrZero
_AdGenImaGroupLeastDelayLink_Object=MibTableColumn
adGenImaGroupLeastDelayLink=_AdGenImaGroupLeastDelayLink_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1,11),_AdGenImaGroupLeastDelayLink_Type())
adGenImaGroupLeastDelayLink.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupLeastDelayLink.setStatus(_A)
_AdGenImaGroupDiffDelayMaxObs_Type=MilliSeconds
_AdGenImaGroupDiffDelayMaxObs_Object=MibTableColumn
adGenImaGroupDiffDelayMaxObs=_AdGenImaGroupDiffDelayMaxObs_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1,12),_AdGenImaGroupDiffDelayMaxObs_Type())
adGenImaGroupDiffDelayMaxObs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupDiffDelayMaxObs.setStatus(_A)
_AdGenImaGroupTxAvailCellRate_Type=Gauge32
_AdGenImaGroupTxAvailCellRate_Object=MibTableColumn
adGenImaGroupTxAvailCellRate=_AdGenImaGroupTxAvailCellRate_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1,13),_AdGenImaGroupTxAvailCellRate_Type())
adGenImaGroupTxAvailCellRate.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupTxAvailCellRate.setStatus(_A)
_AdGenImaGroupRxAvailCellRate_Type=Gauge32
_AdGenImaGroupRxAvailCellRate_Object=MibTableColumn
adGenImaGroupRxAvailCellRate=_AdGenImaGroupRxAvailCellRate_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1,14),_AdGenImaGroupRxAvailCellRate_Type())
adGenImaGroupRxAvailCellRate.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupRxAvailCellRate.setStatus(_A)
class _AdGenImaGroupTxOamLabelValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenImaGroupTxOamLabelValue_Type.__name__=_K
_AdGenImaGroupTxOamLabelValue_Object=MibTableColumn
adGenImaGroupTxOamLabelValue=_AdGenImaGroupTxOamLabelValue_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1,15),_AdGenImaGroupTxOamLabelValue_Type())
adGenImaGroupTxOamLabelValue.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupTxOamLabelValue.setStatus(_A)
class _AdGenImaGroupRxOamLabelValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenImaGroupRxOamLabelValue_Type.__name__=_K
_AdGenImaGroupRxOamLabelValue_Object=MibTableColumn
adGenImaGroupRxOamLabelValue=_AdGenImaGroupRxOamLabelValue_Object((1,3,6,1,4,1,664,5,67,1,25,2,1,1,16),_AdGenImaGroupRxOamLabelValue_Type())
adGenImaGroupRxOamLabelValue.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupRxOamLabelValue.setStatus(_A)
_AdGenImaLinkStatusTable_Object=MibTable
adGenImaLinkStatusTable=_AdGenImaLinkStatusTable_Object((1,3,6,1,4,1,664,5,67,1,25,2,2))
if mibBuilder.loadTexts:adGenImaLinkStatusTable.setStatus(_A)
_AdGenImaLinkStatusEntry_Object=MibTableRow
adGenImaLinkStatusEntry=_AdGenImaLinkStatusEntry_Object((1,3,6,1,4,1,664,5,67,1,25,2,2,1))
adGenImaLinkStatusEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenImaLinkStatusEntry.setStatus(_A)
_AdGenImaLinkNeTxState_Type=ImaLinkState
_AdGenImaLinkNeTxState_Object=MibTableColumn
adGenImaLinkNeTxState=_AdGenImaLinkNeTxState_Object((1,3,6,1,4,1,664,5,67,1,25,2,2,1,1),_AdGenImaLinkNeTxState_Type())
adGenImaLinkNeTxState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkNeTxState.setStatus(_A)
_AdGenImaLinkNeRxState_Type=ImaLinkState
_AdGenImaLinkNeRxState_Object=MibTableColumn
adGenImaLinkNeRxState=_AdGenImaLinkNeRxState_Object((1,3,6,1,4,1,664,5,67,1,25,2,2,1,2),_AdGenImaLinkNeRxState_Type())
adGenImaLinkNeRxState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkNeRxState.setStatus(_A)
_AdGenImaLinkFeTxState_Type=ImaLinkState
_AdGenImaLinkFeTxState_Object=MibTableColumn
adGenImaLinkFeTxState=_AdGenImaLinkFeTxState_Object((1,3,6,1,4,1,664,5,67,1,25,2,2,1,3),_AdGenImaLinkFeTxState_Type())
adGenImaLinkFeTxState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkFeTxState.setStatus(_A)
_AdGenImaLinkFeRxState_Type=ImaLinkState
_AdGenImaLinkFeRxState_Object=MibTableColumn
adGenImaLinkFeRxState=_AdGenImaLinkFeRxState_Object((1,3,6,1,4,1,664,5,67,1,25,2,2,1,4),_AdGenImaLinkFeRxState_Type())
adGenImaLinkFeRxState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkFeRxState.setStatus(_A)
_AdGenImaLinkNeRxFailureStatus_Type=ImaLinkFailureStatus
_AdGenImaLinkNeRxFailureStatus_Object=MibTableColumn
adGenImaLinkNeRxFailureStatus=_AdGenImaLinkNeRxFailureStatus_Object((1,3,6,1,4,1,664,5,67,1,25,2,2,1,5),_AdGenImaLinkNeRxFailureStatus_Type())
adGenImaLinkNeRxFailureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkNeRxFailureStatus.setStatus(_A)
_AdGenImaLinkFeRxFailureStatus_Type=ImaLinkFailureStatus
_AdGenImaLinkFeRxFailureStatus_Object=MibTableColumn
adGenImaLinkFeRxFailureStatus=_AdGenImaLinkFeRxFailureStatus_Object((1,3,6,1,4,1,664,5,67,1,25,2,2,1,6),_AdGenImaLinkFeRxFailureStatus_Type())
adGenImaLinkFeRxFailureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkFeRxFailureStatus.setStatus(_A)
class _AdGenImaLinkTxLid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_AdGenImaLinkTxLid_Type.__name__=_K
_AdGenImaLinkTxLid_Object=MibTableColumn
adGenImaLinkTxLid=_AdGenImaLinkTxLid_Object((1,3,6,1,4,1,664,5,67,1,25,2,2,1,7),_AdGenImaLinkTxLid_Type())
adGenImaLinkTxLid.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTxLid.setStatus(_A)
class _AdGenImaLinkRxLid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_AdGenImaLinkRxLid_Type.__name__=_K
_AdGenImaLinkRxLid_Object=MibTableColumn
adGenImaLinkRxLid=_AdGenImaLinkRxLid_Object((1,3,6,1,4,1,664,5,67,1,25,2,2,1,8),_AdGenImaLinkRxLid_Type())
adGenImaLinkRxLid.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkRxLid.setStatus(_A)
_AdGenImaLinkRelDelay_Type=MilliSeconds
_AdGenImaLinkRelDelay_Object=MibTableColumn
adGenImaLinkRelDelay=_AdGenImaLinkRelDelay_Object((1,3,6,1,4,1,664,5,67,1,25,2,2,1,9),_AdGenImaLinkRelDelay_Type())
adGenImaLinkRelDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkRelDelay.setStatus(_A)
_AdGenImaTest_ObjectIdentity=ObjectIdentity
adGenImaTest=_AdGenImaTest_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,25,3))
_AdGenImaGroupTestTable_Object=MibTable
adGenImaGroupTestTable=_AdGenImaGroupTestTable_Object((1,3,6,1,4,1,664,5,67,1,25,3,1))
if mibBuilder.loadTexts:adGenImaGroupTestTable.setStatus(_A)
_AdGenImaGroupTestEntry_Object=MibTableRow
adGenImaGroupTestEntry=_AdGenImaGroupTestEntry_Object((1,3,6,1,4,1,664,5,67,1,25,3,1,1))
adGenImaGroupTestEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenImaGroupTestEntry.setStatus(_A)
class _AdGenImaGroupTestLinkIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_AdGenImaGroupTestLinkIfIndex_Type.__name__=_R
_AdGenImaGroupTestLinkIfIndex_Object=MibTableColumn
adGenImaGroupTestLinkIfIndex=_AdGenImaGroupTestLinkIfIndex_Object((1,3,6,1,4,1,664,5,67,1,25,3,1,1,1),_AdGenImaGroupTestLinkIfIndex_Type())
adGenImaGroupTestLinkIfIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaGroupTestLinkIfIndex.setStatus(_A)
class _AdGenImaGroupTestPattern_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_AdGenImaGroupTestPattern_Type.__name__=_K
_AdGenImaGroupTestPattern_Object=MibTableColumn
adGenImaGroupTestPattern=_AdGenImaGroupTestPattern_Object((1,3,6,1,4,1,664,5,67,1,25,3,1,1,2),_AdGenImaGroupTestPattern_Type())
adGenImaGroupTestPattern.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaGroupTestPattern.setStatus(_A)
class _AdGenImaGroupTestProcStatus_Type(ImaTestProcStatus):defaultValue=1
_AdGenImaGroupTestProcStatus_Type.__name__=_V
_AdGenImaGroupTestProcStatus_Object=MibTableColumn
adGenImaGroupTestProcStatus=_AdGenImaGroupTestProcStatus_Object((1,3,6,1,4,1,664,5,67,1,25,3,1,1,3),_AdGenImaGroupTestProcStatus_Type())
adGenImaGroupTestProcStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaGroupTestProcStatus.setStatus(_A)
_AdGenImaLinkTestTable_Object=MibTable
adGenImaLinkTestTable=_AdGenImaLinkTestTable_Object((1,3,6,1,4,1,664,5,67,1,25,3,2))
if mibBuilder.loadTexts:adGenImaLinkTestTable.setStatus(_A)
_AdGenImaLinkTestEntry_Object=MibTableRow
adGenImaLinkTestEntry=_AdGenImaLinkTestEntry_Object((1,3,6,1,4,1,664,5,67,1,25,3,2,1))
adGenImaLinkTestEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenImaLinkTestEntry.setStatus(_A)
class _AdGenImaLinkRxTestPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenImaLinkRxTestPattern_Type.__name__=_K
_AdGenImaLinkRxTestPattern_Object=MibTableColumn
adGenImaLinkRxTestPattern=_AdGenImaLinkRxTestPattern_Object((1,3,6,1,4,1,664,5,67,1,25,3,2,1,1),_AdGenImaLinkRxTestPattern_Type())
adGenImaLinkRxTestPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkRxTestPattern.setStatus(_A)
_AdGenImaLinkTestProcStatus_Type=ImaTestProcStatus
_AdGenImaLinkTestProcStatus_Object=MibTableColumn
adGenImaLinkTestProcStatus=_AdGenImaLinkTestProcStatus_Object((1,3,6,1,4,1,664,5,67,1,25,3,2,1,2),_AdGenImaLinkTestProcStatus_Type())
adGenImaLinkTestProcStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTestProcStatus.setStatus(_A)
_AdGenImaPerformance_ObjectIdentity=ObjectIdentity
adGenImaPerformance=_AdGenImaPerformance_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,25,4))
_AdGenImaGroupPerfTable_Object=MibTable
adGenImaGroupPerfTable=_AdGenImaGroupPerfTable_Object((1,3,6,1,4,1,664,5,67,1,25,4,1))
if mibBuilder.loadTexts:adGenImaGroupPerfTable.setStatus(_A)
_AdGenImaGroupPerfEntry_Object=MibTableRow
adGenImaGroupPerfEntry=_AdGenImaGroupPerfEntry_Object((1,3,6,1,4,1,664,5,67,1,25,4,1,1))
adGenImaGroupPerfEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenImaGroupPerfEntry.setStatus(_A)
_AdGenImaGroupUnavailSecs_Type=Counter32
_AdGenImaGroupUnavailSecs_Object=MibTableColumn
adGenImaGroupUnavailSecs=_AdGenImaGroupUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,1,1,1),_AdGenImaGroupUnavailSecs_Type())
adGenImaGroupUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupUnavailSecs.setStatus(_A)
_AdGenImaGroupNeNumFailures_Type=Counter32
_AdGenImaGroupNeNumFailures_Object=MibTableColumn
adGenImaGroupNeNumFailures=_AdGenImaGroupNeNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,1,1,2),_AdGenImaGroupNeNumFailures_Type())
adGenImaGroupNeNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupNeNumFailures.setStatus(_A)
_AdGenImaGroupFeNumFailures_Type=Counter32
_AdGenImaGroupFeNumFailures_Object=MibTableColumn
adGenImaGroupFeNumFailures=_AdGenImaGroupFeNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,1,1,3),_AdGenImaGroupFeNumFailures_Type())
adGenImaGroupFeNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupFeNumFailures.setStatus(_A)
class _AdGenImaGroupValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_AdGenImaGroupValidIntervals_Type.__name__=_K
_AdGenImaGroupValidIntervals_Object=MibTableColumn
adGenImaGroupValidIntervals=_AdGenImaGroupValidIntervals_Object((1,3,6,1,4,1,664,5,67,1,25,4,1,1,4),_AdGenImaGroupValidIntervals_Type())
adGenImaGroupValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupValidIntervals.setStatus(_A)
class _AdGenImaGroupInvalidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_AdGenImaGroupInvalidIntervals_Type.__name__=_K
_AdGenImaGroupInvalidIntervals_Object=MibTableColumn
adGenImaGroupInvalidIntervals=_AdGenImaGroupInvalidIntervals_Object((1,3,6,1,4,1,664,5,67,1,25,4,1,1,5),_AdGenImaGroupInvalidIntervals_Type())
adGenImaGroupInvalidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupInvalidIntervals.setStatus(_A)
class _AdGenImaGroupTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_AdGenImaGroupTimeElapsed_Type.__name__=_K
_AdGenImaGroupTimeElapsed_Object=MibTableColumn
adGenImaGroupTimeElapsed=_AdGenImaGroupTimeElapsed_Object((1,3,6,1,4,1,664,5,67,1,25,4,1,1,6),_AdGenImaGroupTimeElapsed_Type())
adGenImaGroupTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupTimeElapsed.setStatus(_A)
class _AdGenImaGroupResetStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_P,1))
_AdGenImaGroupResetStats_Type.__name__=_K
_AdGenImaGroupResetStats_Object=MibTableColumn
adGenImaGroupResetStats=_AdGenImaGroupResetStats_Object((1,3,6,1,4,1,664,5,67,1,25,4,1,1,7),_AdGenImaGroupResetStats_Type())
adGenImaGroupResetStats.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaGroupResetStats.setStatus(_A)
class _AdGenImaGroupResetPerfHistory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_P,1))
_AdGenImaGroupResetPerfHistory_Type.__name__=_K
_AdGenImaGroupResetPerfHistory_Object=MibTableColumn
adGenImaGroupResetPerfHistory=_AdGenImaGroupResetPerfHistory_Object((1,3,6,1,4,1,664,5,67,1,25,4,1,1,8),_AdGenImaGroupResetPerfHistory_Type())
adGenImaGroupResetPerfHistory.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaGroupResetPerfHistory.setStatus(_A)
_AdGenImaLinkPerfTable_Object=MibTable
adGenImaLinkPerfTable=_AdGenImaLinkPerfTable_Object((1,3,6,1,4,1,664,5,67,1,25,4,2))
if mibBuilder.loadTexts:adGenImaLinkPerfTable.setStatus(_A)
_AdGenImaLinkPerfEntry_Object=MibTableRow
adGenImaLinkPerfEntry=_AdGenImaLinkPerfEntry_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1))
adGenImaLinkPerfEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenImaLinkPerfEntry.setStatus(_A)
_AdGenImaLinkImaViolations_Type=Counter32
_AdGenImaLinkImaViolations_Object=MibTableColumn
adGenImaLinkImaViolations=_AdGenImaLinkImaViolations_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,1),_AdGenImaLinkImaViolations_Type())
adGenImaLinkImaViolations.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkImaViolations.setStatus(_A)
_AdGenImaLinkOifAnomalies_Type=Counter32
_AdGenImaLinkOifAnomalies_Object=MibTableColumn
adGenImaLinkOifAnomalies=_AdGenImaLinkOifAnomalies_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,2),_AdGenImaLinkOifAnomalies_Type())
adGenImaLinkOifAnomalies.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkOifAnomalies.setStatus(_A)
_AdGenImaLinkNeSevErroredSecs_Type=Counter32
_AdGenImaLinkNeSevErroredSecs_Object=MibTableColumn
adGenImaLinkNeSevErroredSecs=_AdGenImaLinkNeSevErroredSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,3),_AdGenImaLinkNeSevErroredSecs_Type())
adGenImaLinkNeSevErroredSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkNeSevErroredSecs.setStatus(_A)
_AdGenImaLinkFeSevErroredSecs_Type=Counter32
_AdGenImaLinkFeSevErroredSecs_Object=MibTableColumn
adGenImaLinkFeSevErroredSecs=_AdGenImaLinkFeSevErroredSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,4),_AdGenImaLinkFeSevErroredSecs_Type())
adGenImaLinkFeSevErroredSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkFeSevErroredSecs.setStatus(_A)
_AdGenImaLinkNeUnavailSecs_Type=Counter32
_AdGenImaLinkNeUnavailSecs_Object=MibTableColumn
adGenImaLinkNeUnavailSecs=_AdGenImaLinkNeUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,5),_AdGenImaLinkNeUnavailSecs_Type())
adGenImaLinkNeUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkNeUnavailSecs.setStatus(_A)
_AdGenImaLinkFeUnavailSecs_Type=Counter32
_AdGenImaLinkFeUnavailSecs_Object=MibTableColumn
adGenImaLinkFeUnavailSecs=_AdGenImaLinkFeUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,6),_AdGenImaLinkFeUnavailSecs_Type())
adGenImaLinkFeUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkFeUnavailSecs.setStatus(_A)
_AdGenImaLinkNeTxUnusableSecs_Type=Counter32
_AdGenImaLinkNeTxUnusableSecs_Object=MibTableColumn
adGenImaLinkNeTxUnusableSecs=_AdGenImaLinkNeTxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,7),_AdGenImaLinkNeTxUnusableSecs_Type())
adGenImaLinkNeTxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkNeTxUnusableSecs.setStatus(_A)
_AdGenImaLinkNeRxUnusableSecs_Type=Counter32
_AdGenImaLinkNeRxUnusableSecs_Object=MibTableColumn
adGenImaLinkNeRxUnusableSecs=_AdGenImaLinkNeRxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,8),_AdGenImaLinkNeRxUnusableSecs_Type())
adGenImaLinkNeRxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkNeRxUnusableSecs.setStatus(_A)
_AdGenImaLinkFeTxUnusableSecs_Type=Counter32
_AdGenImaLinkFeTxUnusableSecs_Object=MibTableColumn
adGenImaLinkFeTxUnusableSecs=_AdGenImaLinkFeTxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,9),_AdGenImaLinkFeTxUnusableSecs_Type())
adGenImaLinkFeTxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkFeTxUnusableSecs.setStatus(_A)
_AdGenImaLinkFeRxUnusableSecs_Type=Counter32
_AdGenImaLinkFeRxUnusableSecs_Object=MibTableColumn
adGenImaLinkFeRxUnusableSecs=_AdGenImaLinkFeRxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,10),_AdGenImaLinkFeRxUnusableSecs_Type())
adGenImaLinkFeRxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkFeRxUnusableSecs.setStatus(_A)
_AdGenImaLinkNeTxNumFailures_Type=Counter32
_AdGenImaLinkNeTxNumFailures_Object=MibTableColumn
adGenImaLinkNeTxNumFailures=_AdGenImaLinkNeTxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,11),_AdGenImaLinkNeTxNumFailures_Type())
adGenImaLinkNeTxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkNeTxNumFailures.setStatus(_A)
_AdGenImaLinkNeRxNumFailures_Type=Counter32
_AdGenImaLinkNeRxNumFailures_Object=MibTableColumn
adGenImaLinkNeRxNumFailures=_AdGenImaLinkNeRxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,12),_AdGenImaLinkNeRxNumFailures_Type())
adGenImaLinkNeRxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkNeRxNumFailures.setStatus(_A)
_AdGenImaLinkFeTxNumFailures_Type=Counter32
_AdGenImaLinkFeTxNumFailures_Object=MibTableColumn
adGenImaLinkFeTxNumFailures=_AdGenImaLinkFeTxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,13),_AdGenImaLinkFeTxNumFailures_Type())
adGenImaLinkFeTxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkFeTxNumFailures.setStatus(_A)
_AdGenImaLinkFeRxNumFailures_Type=Counter32
_AdGenImaLinkFeRxNumFailures_Object=MibTableColumn
adGenImaLinkFeRxNumFailures=_AdGenImaLinkFeRxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,14),_AdGenImaLinkFeRxNumFailures_Type())
adGenImaLinkFeRxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkFeRxNumFailures.setStatus(_A)
_AdGenImaLinkTxStuffs_Type=Counter32
_AdGenImaLinkTxStuffs_Object=MibTableColumn
adGenImaLinkTxStuffs=_AdGenImaLinkTxStuffs_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,15),_AdGenImaLinkTxStuffs_Type())
adGenImaLinkTxStuffs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTxStuffs.setStatus(_A)
_AdGenImaLinkRxStuffs_Type=Counter32
_AdGenImaLinkRxStuffs_Object=MibTableColumn
adGenImaLinkRxStuffs=_AdGenImaLinkRxStuffs_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,16),_AdGenImaLinkRxStuffs_Type())
adGenImaLinkRxStuffs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkRxStuffs.setStatus(_A)
class _AdGenImaLinkValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_AdGenImaLinkValidIntervals_Type.__name__=_K
_AdGenImaLinkValidIntervals_Object=MibTableColumn
adGenImaLinkValidIntervals=_AdGenImaLinkValidIntervals_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,17),_AdGenImaLinkValidIntervals_Type())
adGenImaLinkValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkValidIntervals.setStatus(_A)
class _AdGenImaLinkInvalidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_AdGenImaLinkInvalidIntervals_Type.__name__=_K
_AdGenImaLinkInvalidIntervals_Object=MibTableColumn
adGenImaLinkInvalidIntervals=_AdGenImaLinkInvalidIntervals_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,18),_AdGenImaLinkInvalidIntervals_Type())
adGenImaLinkInvalidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkInvalidIntervals.setStatus(_A)
class _AdGenImaLinkTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_AdGenImaLinkTimeElapsed_Type.__name__=_K
_AdGenImaLinkTimeElapsed_Object=MibTableColumn
adGenImaLinkTimeElapsed=_AdGenImaLinkTimeElapsed_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,19),_AdGenImaLinkTimeElapsed_Type())
adGenImaLinkTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTimeElapsed.setStatus(_A)
class _AdGenImaLinkResetStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_P,1))
_AdGenImaLinkResetStats_Type.__name__=_K
_AdGenImaLinkResetStats_Object=MibTableColumn
adGenImaLinkResetStats=_AdGenImaLinkResetStats_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,20),_AdGenImaLinkResetStats_Type())
adGenImaLinkResetStats.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaLinkResetStats.setStatus(_A)
class _AdGenImaLinkResetPerfHistory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_P,1))
_AdGenImaLinkResetPerfHistory_Type.__name__=_K
_AdGenImaLinkResetPerfHistory_Object=MibTableColumn
adGenImaLinkResetPerfHistory=_AdGenImaLinkResetPerfHistory_Object((1,3,6,1,4,1,664,5,67,1,25,4,2,1,21),_AdGenImaLinkResetPerfHistory_Type())
adGenImaLinkResetPerfHistory.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenImaLinkResetPerfHistory.setStatus(_A)
_AdGenImaGroupCurrentTable_Object=MibTable
adGenImaGroupCurrentTable=_AdGenImaGroupCurrentTable_Object((1,3,6,1,4,1,664,5,67,1,25,4,3))
if mibBuilder.loadTexts:adGenImaGroupCurrentTable.setStatus(_A)
_AdGenImaGroupCurrentEntry_Object=MibTableRow
adGenImaGroupCurrentEntry=_AdGenImaGroupCurrentEntry_Object((1,3,6,1,4,1,664,5,67,1,25,4,3,1))
adGenImaGroupCurrentEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenImaGroupCurrentEntry.setStatus(_A)
_AdGenImaGroupCurrentUnavailSecs_Type=Gauge32
_AdGenImaGroupCurrentUnavailSecs_Object=MibTableColumn
adGenImaGroupCurrentUnavailSecs=_AdGenImaGroupCurrentUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,3,1,1),_AdGenImaGroupCurrentUnavailSecs_Type())
adGenImaGroupCurrentUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupCurrentUnavailSecs.setStatus(_A)
_AdGenImaGroupCurrentNeNumFailures_Type=Gauge32
_AdGenImaGroupCurrentNeNumFailures_Object=MibTableColumn
adGenImaGroupCurrentNeNumFailures=_AdGenImaGroupCurrentNeNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,3,1,2),_AdGenImaGroupCurrentNeNumFailures_Type())
adGenImaGroupCurrentNeNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupCurrentNeNumFailures.setStatus(_A)
_AdGenImaGroupCurrentFeNumFailures_Type=Gauge32
_AdGenImaGroupCurrentFeNumFailures_Object=MibTableColumn
adGenImaGroupCurrentFeNumFailures=_AdGenImaGroupCurrentFeNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,3,1,3),_AdGenImaGroupCurrentFeNumFailures_Type())
adGenImaGroupCurrentFeNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupCurrentFeNumFailures.setStatus(_A)
_AdGenImaGroupIntervalTable_Object=MibTable
adGenImaGroupIntervalTable=_AdGenImaGroupIntervalTable_Object((1,3,6,1,4,1,664,5,67,1,25,4,4))
if mibBuilder.loadTexts:adGenImaGroupIntervalTable.setStatus(_A)
_AdGenImaGroupIntervalEntry_Object=MibTableRow
adGenImaGroupIntervalEntry=_AdGenImaGroupIntervalEntry_Object((1,3,6,1,4,1,664,5,67,1,25,4,4,1))
adGenImaGroupIntervalEntry.setIndexNames((0,_C,_D),(0,_O,_Y))
if mibBuilder.loadTexts:adGenImaGroupIntervalEntry.setStatus(_A)
class _AdGenImaGroupIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AdGenImaGroupIntervalNumber_Type.__name__=_K
_AdGenImaGroupIntervalNumber_Object=MibTableColumn
adGenImaGroupIntervalNumber=_AdGenImaGroupIntervalNumber_Object((1,3,6,1,4,1,664,5,67,1,25,4,4,1,1),_AdGenImaGroupIntervalNumber_Type())
adGenImaGroupIntervalNumber.setMaxAccess(_Q)
if mibBuilder.loadTexts:adGenImaGroupIntervalNumber.setStatus(_A)
_AdGenImaGroupIntervalUnavailSecs_Type=Gauge32
_AdGenImaGroupIntervalUnavailSecs_Object=MibTableColumn
adGenImaGroupIntervalUnavailSecs=_AdGenImaGroupIntervalUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,4,1,2),_AdGenImaGroupIntervalUnavailSecs_Type())
adGenImaGroupIntervalUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupIntervalUnavailSecs.setStatus(_A)
_AdGenImaGroupIntervalNeNumFailures_Type=Gauge32
_AdGenImaGroupIntervalNeNumFailures_Object=MibTableColumn
adGenImaGroupIntervalNeNumFailures=_AdGenImaGroupIntervalNeNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,4,1,3),_AdGenImaGroupIntervalNeNumFailures_Type())
adGenImaGroupIntervalNeNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupIntervalNeNumFailures.setStatus(_A)
_AdGenImaGroupIntervalFeNumFailures_Type=Gauge32
_AdGenImaGroupIntervalFeNumFailures_Object=MibTableColumn
adGenImaGroupIntervalFeNumFailures=_AdGenImaGroupIntervalFeNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,4,1,4),_AdGenImaGroupIntervalFeNumFailures_Type())
adGenImaGroupIntervalFeNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupIntervalFeNumFailures.setStatus(_A)
_AdGenImaGroupIntervalTimeStamp_Type=DisplayString
_AdGenImaGroupIntervalTimeStamp_Object=MibTableColumn
adGenImaGroupIntervalTimeStamp=_AdGenImaGroupIntervalTimeStamp_Object((1,3,6,1,4,1,664,5,67,1,25,4,4,1,5),_AdGenImaGroupIntervalTimeStamp_Type())
adGenImaGroupIntervalTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupIntervalTimeStamp.setStatus(_A)
_AdGenImaGroupTotalTable_Object=MibTable
adGenImaGroupTotalTable=_AdGenImaGroupTotalTable_Object((1,3,6,1,4,1,664,5,67,1,25,4,5))
if mibBuilder.loadTexts:adGenImaGroupTotalTable.setStatus(_A)
_AdGenImaGroupTotalEntry_Object=MibTableRow
adGenImaGroupTotalEntry=_AdGenImaGroupTotalEntry_Object((1,3,6,1,4,1,664,5,67,1,25,4,5,1))
adGenImaGroupTotalEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenImaGroupTotalEntry.setStatus(_A)
_AdGenImaGroupTotalUnavailSecs_Type=Gauge32
_AdGenImaGroupTotalUnavailSecs_Object=MibTableColumn
adGenImaGroupTotalUnavailSecs=_AdGenImaGroupTotalUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,5,1,1),_AdGenImaGroupTotalUnavailSecs_Type())
adGenImaGroupTotalUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupTotalUnavailSecs.setStatus(_A)
_AdGenImaGroupTotalNeNumFailures_Type=Gauge32
_AdGenImaGroupTotalNeNumFailures_Object=MibTableColumn
adGenImaGroupTotalNeNumFailures=_AdGenImaGroupTotalNeNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,5,1,2),_AdGenImaGroupTotalNeNumFailures_Type())
adGenImaGroupTotalNeNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupTotalNeNumFailures.setStatus(_A)
_AdGenImaGroupTotalFeNumFailures_Type=Gauge32
_AdGenImaGroupTotalFeNumFailures_Object=MibTableColumn
adGenImaGroupTotalFeNumFailures=_AdGenImaGroupTotalFeNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,5,1,3),_AdGenImaGroupTotalFeNumFailures_Type())
adGenImaGroupTotalFeNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupTotalFeNumFailures.setStatus(_A)
_AdGenImaGroupDayCurrentTable_Object=MibTable
adGenImaGroupDayCurrentTable=_AdGenImaGroupDayCurrentTable_Object((1,3,6,1,4,1,664,5,67,1,25,4,6))
if mibBuilder.loadTexts:adGenImaGroupDayCurrentTable.setStatus(_A)
_AdGenImaGroupDayCurrentEntry_Object=MibTableRow
adGenImaGroupDayCurrentEntry=_AdGenImaGroupDayCurrentEntry_Object((1,3,6,1,4,1,664,5,67,1,25,4,6,1))
adGenImaGroupDayCurrentEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenImaGroupDayCurrentEntry.setStatus(_A)
_AdGenImaGroupDayCurrentUnavailSecs_Type=Gauge32
_AdGenImaGroupDayCurrentUnavailSecs_Object=MibTableColumn
adGenImaGroupDayCurrentUnavailSecs=_AdGenImaGroupDayCurrentUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,6,1,1),_AdGenImaGroupDayCurrentUnavailSecs_Type())
adGenImaGroupDayCurrentUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupDayCurrentUnavailSecs.setStatus(_A)
_AdGenImaGroupDayCurrentNeNumFailures_Type=Gauge32
_AdGenImaGroupDayCurrentNeNumFailures_Object=MibTableColumn
adGenImaGroupDayCurrentNeNumFailures=_AdGenImaGroupDayCurrentNeNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,6,1,2),_AdGenImaGroupDayCurrentNeNumFailures_Type())
adGenImaGroupDayCurrentNeNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupDayCurrentNeNumFailures.setStatus(_A)
_AdGenImaGroupDayCurrentFeNumFailures_Type=Gauge32
_AdGenImaGroupDayCurrentFeNumFailures_Object=MibTableColumn
adGenImaGroupDayCurrentFeNumFailures=_AdGenImaGroupDayCurrentFeNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,6,1,3),_AdGenImaGroupDayCurrentFeNumFailures_Type())
adGenImaGroupDayCurrentFeNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupDayCurrentFeNumFailures.setStatus(_A)
_AdGenImaGroupDayIntervalTable_Object=MibTable
adGenImaGroupDayIntervalTable=_AdGenImaGroupDayIntervalTable_Object((1,3,6,1,4,1,664,5,67,1,25,4,7))
if mibBuilder.loadTexts:adGenImaGroupDayIntervalTable.setStatus(_A)
_AdGenImaGroupDayIntervalEntry_Object=MibTableRow
adGenImaGroupDayIntervalEntry=_AdGenImaGroupDayIntervalEntry_Object((1,3,6,1,4,1,664,5,67,1,25,4,7,1))
adGenImaGroupDayIntervalEntry.setIndexNames((0,_C,_D),(0,_O,_Z))
if mibBuilder.loadTexts:adGenImaGroupDayIntervalEntry.setStatus(_A)
class _AdGenImaGroupDayIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_AdGenImaGroupDayIntervalNumber_Type.__name__=_K
_AdGenImaGroupDayIntervalNumber_Object=MibTableColumn
adGenImaGroupDayIntervalNumber=_AdGenImaGroupDayIntervalNumber_Object((1,3,6,1,4,1,664,5,67,1,25,4,7,1,1),_AdGenImaGroupDayIntervalNumber_Type())
adGenImaGroupDayIntervalNumber.setMaxAccess(_Q)
if mibBuilder.loadTexts:adGenImaGroupDayIntervalNumber.setStatus(_A)
_AdGenImaGroupDayIntervalUnavailSecs_Type=Gauge32
_AdGenImaGroupDayIntervalUnavailSecs_Object=MibTableColumn
adGenImaGroupDayIntervalUnavailSecs=_AdGenImaGroupDayIntervalUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,7,1,2),_AdGenImaGroupDayIntervalUnavailSecs_Type())
adGenImaGroupDayIntervalUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupDayIntervalUnavailSecs.setStatus(_A)
_AdGenImaGroupDayIntervalNeNumFailures_Type=Gauge32
_AdGenImaGroupDayIntervalNeNumFailures_Object=MibTableColumn
adGenImaGroupDayIntervalNeNumFailures=_AdGenImaGroupDayIntervalNeNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,7,1,3),_AdGenImaGroupDayIntervalNeNumFailures_Type())
adGenImaGroupDayIntervalNeNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupDayIntervalNeNumFailures.setStatus(_A)
_AdGenImaGroupDayIntervalFeNumFailures_Type=Gauge32
_AdGenImaGroupDayIntervalFeNumFailures_Object=MibTableColumn
adGenImaGroupDayIntervalFeNumFailures=_AdGenImaGroupDayIntervalFeNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,7,1,4),_AdGenImaGroupDayIntervalFeNumFailures_Type())
adGenImaGroupDayIntervalFeNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupDayIntervalFeNumFailures.setStatus(_A)
_AdGenImaGroupDayIntervalTimeStamp_Type=DisplayString
_AdGenImaGroupDayIntervalTimeStamp_Object=MibTableColumn
adGenImaGroupDayIntervalTimeStamp=_AdGenImaGroupDayIntervalTimeStamp_Object((1,3,6,1,4,1,664,5,67,1,25,4,7,1,5),_AdGenImaGroupDayIntervalTimeStamp_Type())
adGenImaGroupDayIntervalTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaGroupDayIntervalTimeStamp.setStatus(_A)
_AdGenImaLinkCurrentTable_Object=MibTable
adGenImaLinkCurrentTable=_AdGenImaLinkCurrentTable_Object((1,3,6,1,4,1,664,5,67,1,25,4,8))
if mibBuilder.loadTexts:adGenImaLinkCurrentTable.setStatus(_A)
_AdGenImaLinkCurrentEntry_Object=MibTableRow
adGenImaLinkCurrentEntry=_AdGenImaLinkCurrentEntry_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1))
adGenImaLinkCurrentEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenImaLinkCurrentEntry.setStatus(_A)
_AdGenImaLinkCurrentImaViolations_Type=Gauge32
_AdGenImaLinkCurrentImaViolations_Object=MibTableColumn
adGenImaLinkCurrentImaViolations=_AdGenImaLinkCurrentImaViolations_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1,1),_AdGenImaLinkCurrentImaViolations_Type())
adGenImaLinkCurrentImaViolations.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkCurrentImaViolations.setStatus(_A)
_AdGenImaLinkCurrentOifAnomalies_Type=Gauge32
_AdGenImaLinkCurrentOifAnomalies_Object=MibTableColumn
adGenImaLinkCurrentOifAnomalies=_AdGenImaLinkCurrentOifAnomalies_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1,2),_AdGenImaLinkCurrentOifAnomalies_Type())
adGenImaLinkCurrentOifAnomalies.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkCurrentOifAnomalies.setStatus(_A)
_AdGenImaLinkCurrentNeSevErroredSecs_Type=Gauge32
_AdGenImaLinkCurrentNeSevErroredSecs_Object=MibTableColumn
adGenImaLinkCurrentNeSevErroredSecs=_AdGenImaLinkCurrentNeSevErroredSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1,3),_AdGenImaLinkCurrentNeSevErroredSecs_Type())
adGenImaLinkCurrentNeSevErroredSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkCurrentNeSevErroredSecs.setStatus(_A)
_AdGenImaLinkCurrentFeSevErroredSecs_Type=Gauge32
_AdGenImaLinkCurrentFeSevErroredSecs_Object=MibTableColumn
adGenImaLinkCurrentFeSevErroredSecs=_AdGenImaLinkCurrentFeSevErroredSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1,4),_AdGenImaLinkCurrentFeSevErroredSecs_Type())
adGenImaLinkCurrentFeSevErroredSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkCurrentFeSevErroredSecs.setStatus(_A)
_AdGenImaLinkCurrentNeUnavailSecs_Type=Gauge32
_AdGenImaLinkCurrentNeUnavailSecs_Object=MibTableColumn
adGenImaLinkCurrentNeUnavailSecs=_AdGenImaLinkCurrentNeUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1,5),_AdGenImaLinkCurrentNeUnavailSecs_Type())
adGenImaLinkCurrentNeUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkCurrentNeUnavailSecs.setStatus(_A)
_AdGenImaLinkCurrentFeUnavailSecs_Type=Gauge32
_AdGenImaLinkCurrentFeUnavailSecs_Object=MibTableColumn
adGenImaLinkCurrentFeUnavailSecs=_AdGenImaLinkCurrentFeUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1,6),_AdGenImaLinkCurrentFeUnavailSecs_Type())
adGenImaLinkCurrentFeUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkCurrentFeUnavailSecs.setStatus(_A)
_AdGenImaLinkCurrentNeTxUnusableSecs_Type=Gauge32
_AdGenImaLinkCurrentNeTxUnusableSecs_Object=MibTableColumn
adGenImaLinkCurrentNeTxUnusableSecs=_AdGenImaLinkCurrentNeTxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1,7),_AdGenImaLinkCurrentNeTxUnusableSecs_Type())
adGenImaLinkCurrentNeTxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkCurrentNeTxUnusableSecs.setStatus(_A)
_AdGenImaLinkCurrentNeRxUnusableSecs_Type=Gauge32
_AdGenImaLinkCurrentNeRxUnusableSecs_Object=MibTableColumn
adGenImaLinkCurrentNeRxUnusableSecs=_AdGenImaLinkCurrentNeRxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1,8),_AdGenImaLinkCurrentNeRxUnusableSecs_Type())
adGenImaLinkCurrentNeRxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkCurrentNeRxUnusableSecs.setStatus(_A)
_AdGenImaLinkCurrentFeTxUnusableSecs_Type=Gauge32
_AdGenImaLinkCurrentFeTxUnusableSecs_Object=MibTableColumn
adGenImaLinkCurrentFeTxUnusableSecs=_AdGenImaLinkCurrentFeTxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1,9),_AdGenImaLinkCurrentFeTxUnusableSecs_Type())
adGenImaLinkCurrentFeTxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkCurrentFeTxUnusableSecs.setStatus(_A)
_AdGenImaLinkCurrentFeRxUnusableSecs_Type=Gauge32
_AdGenImaLinkCurrentFeRxUnusableSecs_Object=MibTableColumn
adGenImaLinkCurrentFeRxUnusableSecs=_AdGenImaLinkCurrentFeRxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1,10),_AdGenImaLinkCurrentFeRxUnusableSecs_Type())
adGenImaLinkCurrentFeRxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkCurrentFeRxUnusableSecs.setStatus(_A)
_AdGenImaLinkCurrentNeTxNumFailures_Type=Gauge32
_AdGenImaLinkCurrentNeTxNumFailures_Object=MibTableColumn
adGenImaLinkCurrentNeTxNumFailures=_AdGenImaLinkCurrentNeTxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1,11),_AdGenImaLinkCurrentNeTxNumFailures_Type())
adGenImaLinkCurrentNeTxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkCurrentNeTxNumFailures.setStatus(_A)
_AdGenImaLinkCurrentNeRxNumFailures_Type=Gauge32
_AdGenImaLinkCurrentNeRxNumFailures_Object=MibTableColumn
adGenImaLinkCurrentNeRxNumFailures=_AdGenImaLinkCurrentNeRxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1,12),_AdGenImaLinkCurrentNeRxNumFailures_Type())
adGenImaLinkCurrentNeRxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkCurrentNeRxNumFailures.setStatus(_A)
_AdGenImaLinkCurrentFeTxNumFailures_Type=Gauge32
_AdGenImaLinkCurrentFeTxNumFailures_Object=MibTableColumn
adGenImaLinkCurrentFeTxNumFailures=_AdGenImaLinkCurrentFeTxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1,13),_AdGenImaLinkCurrentFeTxNumFailures_Type())
adGenImaLinkCurrentFeTxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkCurrentFeTxNumFailures.setStatus(_A)
_AdGenImaLinkCurrentFeRxNumFailures_Type=Gauge32
_AdGenImaLinkCurrentFeRxNumFailures_Object=MibTableColumn
adGenImaLinkCurrentFeRxNumFailures=_AdGenImaLinkCurrentFeRxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1,14),_AdGenImaLinkCurrentFeRxNumFailures_Type())
adGenImaLinkCurrentFeRxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkCurrentFeRxNumFailures.setStatus(_A)
_AdGenImaLinkCurrentTxStuffs_Type=Gauge32
_AdGenImaLinkCurrentTxStuffs_Object=MibTableColumn
adGenImaLinkCurrentTxStuffs=_AdGenImaLinkCurrentTxStuffs_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1,15),_AdGenImaLinkCurrentTxStuffs_Type())
adGenImaLinkCurrentTxStuffs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkCurrentTxStuffs.setStatus(_A)
_AdGenImaLinkCurrentRxStuffs_Type=Gauge32
_AdGenImaLinkCurrentRxStuffs_Object=MibTableColumn
adGenImaLinkCurrentRxStuffs=_AdGenImaLinkCurrentRxStuffs_Object((1,3,6,1,4,1,664,5,67,1,25,4,8,1,16),_AdGenImaLinkCurrentRxStuffs_Type())
adGenImaLinkCurrentRxStuffs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkCurrentRxStuffs.setStatus(_A)
_AdGenImaLinkIntervalTable_Object=MibTable
adGenImaLinkIntervalTable=_AdGenImaLinkIntervalTable_Object((1,3,6,1,4,1,664,5,67,1,25,4,9))
if mibBuilder.loadTexts:adGenImaLinkIntervalTable.setStatus(_A)
_AdGenImaLinkIntervalEntry_Object=MibTableRow
adGenImaLinkIntervalEntry=_AdGenImaLinkIntervalEntry_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1))
adGenImaLinkIntervalEntry.setIndexNames((0,_C,_D),(0,_O,_a))
if mibBuilder.loadTexts:adGenImaLinkIntervalEntry.setStatus(_A)
class _AdGenImaLinkIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AdGenImaLinkIntervalNumber_Type.__name__=_K
_AdGenImaLinkIntervalNumber_Object=MibTableColumn
adGenImaLinkIntervalNumber=_AdGenImaLinkIntervalNumber_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,1),_AdGenImaLinkIntervalNumber_Type())
adGenImaLinkIntervalNumber.setMaxAccess(_Q)
if mibBuilder.loadTexts:adGenImaLinkIntervalNumber.setStatus(_A)
_AdGenImaLinkIntervalImaViolations_Type=Gauge32
_AdGenImaLinkIntervalImaViolations_Object=MibTableColumn
adGenImaLinkIntervalImaViolations=_AdGenImaLinkIntervalImaViolations_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,2),_AdGenImaLinkIntervalImaViolations_Type())
adGenImaLinkIntervalImaViolations.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalImaViolations.setStatus(_A)
_AdGenImaLinkIntervalOifAnomalies_Type=Gauge32
_AdGenImaLinkIntervalOifAnomalies_Object=MibTableColumn
adGenImaLinkIntervalOifAnomalies=_AdGenImaLinkIntervalOifAnomalies_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,3),_AdGenImaLinkIntervalOifAnomalies_Type())
adGenImaLinkIntervalOifAnomalies.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalOifAnomalies.setStatus(_A)
_AdGenImaLinkIntervalNeSevErroredSecs_Type=Gauge32
_AdGenImaLinkIntervalNeSevErroredSecs_Object=MibTableColumn
adGenImaLinkIntervalNeSevErroredSecs=_AdGenImaLinkIntervalNeSevErroredSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,4),_AdGenImaLinkIntervalNeSevErroredSecs_Type())
adGenImaLinkIntervalNeSevErroredSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalNeSevErroredSecs.setStatus(_A)
_AdGenImaLinkIntervalFeSevErroredSecs_Type=Gauge32
_AdGenImaLinkIntervalFeSevErroredSecs_Object=MibTableColumn
adGenImaLinkIntervalFeSevErroredSecs=_AdGenImaLinkIntervalFeSevErroredSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,5),_AdGenImaLinkIntervalFeSevErroredSecs_Type())
adGenImaLinkIntervalFeSevErroredSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalFeSevErroredSecs.setStatus(_A)
_AdGenImaLinkIntervalNeUnavailSecs_Type=Gauge32
_AdGenImaLinkIntervalNeUnavailSecs_Object=MibTableColumn
adGenImaLinkIntervalNeUnavailSecs=_AdGenImaLinkIntervalNeUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,6),_AdGenImaLinkIntervalNeUnavailSecs_Type())
adGenImaLinkIntervalNeUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalNeUnavailSecs.setStatus(_A)
_AdGenImaLinkIntervalFeUnavailSecs_Type=Gauge32
_AdGenImaLinkIntervalFeUnavailSecs_Object=MibTableColumn
adGenImaLinkIntervalFeUnavailSecs=_AdGenImaLinkIntervalFeUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,7),_AdGenImaLinkIntervalFeUnavailSecs_Type())
adGenImaLinkIntervalFeUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalFeUnavailSecs.setStatus(_A)
_AdGenImaLinkIntervalNeTxUnusableSecs_Type=Gauge32
_AdGenImaLinkIntervalNeTxUnusableSecs_Object=MibTableColumn
adGenImaLinkIntervalNeTxUnusableSecs=_AdGenImaLinkIntervalNeTxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,8),_AdGenImaLinkIntervalNeTxUnusableSecs_Type())
adGenImaLinkIntervalNeTxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalNeTxUnusableSecs.setStatus(_A)
_AdGenImaLinkIntervalNeRxUnusableSecs_Type=Gauge32
_AdGenImaLinkIntervalNeRxUnusableSecs_Object=MibTableColumn
adGenImaLinkIntervalNeRxUnusableSecs=_AdGenImaLinkIntervalNeRxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,9),_AdGenImaLinkIntervalNeRxUnusableSecs_Type())
adGenImaLinkIntervalNeRxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalNeRxUnusableSecs.setStatus(_A)
_AdGenImaLinkIntervalFeTxUnusableSecs_Type=Gauge32
_AdGenImaLinkIntervalFeTxUnusableSecs_Object=MibTableColumn
adGenImaLinkIntervalFeTxUnusableSecs=_AdGenImaLinkIntervalFeTxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,10),_AdGenImaLinkIntervalFeTxUnusableSecs_Type())
adGenImaLinkIntervalFeTxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalFeTxUnusableSecs.setStatus(_A)
_AdGenImaLinkIntervalFeRxUnusableSecs_Type=Gauge32
_AdGenImaLinkIntervalFeRxUnusableSecs_Object=MibTableColumn
adGenImaLinkIntervalFeRxUnusableSecs=_AdGenImaLinkIntervalFeRxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,11),_AdGenImaLinkIntervalFeRxUnusableSecs_Type())
adGenImaLinkIntervalFeRxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalFeRxUnusableSecs.setStatus(_A)
_AdGenImaLinkIntervalNeTxNumFailures_Type=Gauge32
_AdGenImaLinkIntervalNeTxNumFailures_Object=MibTableColumn
adGenImaLinkIntervalNeTxNumFailures=_AdGenImaLinkIntervalNeTxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,12),_AdGenImaLinkIntervalNeTxNumFailures_Type())
adGenImaLinkIntervalNeTxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalNeTxNumFailures.setStatus(_A)
_AdGenImaLinkIntervalNeRxNumFailures_Type=Gauge32
_AdGenImaLinkIntervalNeRxNumFailures_Object=MibTableColumn
adGenImaLinkIntervalNeRxNumFailures=_AdGenImaLinkIntervalNeRxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,13),_AdGenImaLinkIntervalNeRxNumFailures_Type())
adGenImaLinkIntervalNeRxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalNeRxNumFailures.setStatus(_A)
_AdGenImaLinkIntervalFeTxNumFailures_Type=Gauge32
_AdGenImaLinkIntervalFeTxNumFailures_Object=MibTableColumn
adGenImaLinkIntervalFeTxNumFailures=_AdGenImaLinkIntervalFeTxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,14),_AdGenImaLinkIntervalFeTxNumFailures_Type())
adGenImaLinkIntervalFeTxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalFeTxNumFailures.setStatus(_A)
_AdGenImaLinkIntervalFeRxNumFailures_Type=Gauge32
_AdGenImaLinkIntervalFeRxNumFailures_Object=MibTableColumn
adGenImaLinkIntervalFeRxNumFailures=_AdGenImaLinkIntervalFeRxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,15),_AdGenImaLinkIntervalFeRxNumFailures_Type())
adGenImaLinkIntervalFeRxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalFeRxNumFailures.setStatus(_A)
_AdGenImaLinkIntervalTxStuffs_Type=Gauge32
_AdGenImaLinkIntervalTxStuffs_Object=MibTableColumn
adGenImaLinkIntervalTxStuffs=_AdGenImaLinkIntervalTxStuffs_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,16),_AdGenImaLinkIntervalTxStuffs_Type())
adGenImaLinkIntervalTxStuffs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalTxStuffs.setStatus(_A)
_AdGenImaLinkIntervalRxStuffs_Type=Gauge32
_AdGenImaLinkIntervalRxStuffs_Object=MibTableColumn
adGenImaLinkIntervalRxStuffs=_AdGenImaLinkIntervalRxStuffs_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,17),_AdGenImaLinkIntervalRxStuffs_Type())
adGenImaLinkIntervalRxStuffs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalRxStuffs.setStatus(_A)
_AdGenImaLinkIntervalTimeStamp_Type=DisplayString
_AdGenImaLinkIntervalTimeStamp_Object=MibTableColumn
adGenImaLinkIntervalTimeStamp=_AdGenImaLinkIntervalTimeStamp_Object((1,3,6,1,4,1,664,5,67,1,25,4,9,1,18),_AdGenImaLinkIntervalTimeStamp_Type())
adGenImaLinkIntervalTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkIntervalTimeStamp.setStatus(_A)
_AdGenImaLinkTotalTable_Object=MibTable
adGenImaLinkTotalTable=_AdGenImaLinkTotalTable_Object((1,3,6,1,4,1,664,5,67,1,25,4,10))
if mibBuilder.loadTexts:adGenImaLinkTotalTable.setStatus(_A)
_AdGenImaLinkTotalEntry_Object=MibTableRow
adGenImaLinkTotalEntry=_AdGenImaLinkTotalEntry_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1))
adGenImaLinkTotalEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenImaLinkTotalEntry.setStatus(_A)
_AdGenImaLinkTotalImaViolations_Type=Gauge32
_AdGenImaLinkTotalImaViolations_Object=MibTableColumn
adGenImaLinkTotalImaViolations=_AdGenImaLinkTotalImaViolations_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1,1),_AdGenImaLinkTotalImaViolations_Type())
adGenImaLinkTotalImaViolations.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTotalImaViolations.setStatus(_A)
_AdGenImaLinkTotalOifAnomalies_Type=Gauge32
_AdGenImaLinkTotalOifAnomalies_Object=MibTableColumn
adGenImaLinkTotalOifAnomalies=_AdGenImaLinkTotalOifAnomalies_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1,2),_AdGenImaLinkTotalOifAnomalies_Type())
adGenImaLinkTotalOifAnomalies.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTotalOifAnomalies.setStatus(_A)
_AdGenImaLinkTotalNeSevErroredSecs_Type=Gauge32
_AdGenImaLinkTotalNeSevErroredSecs_Object=MibTableColumn
adGenImaLinkTotalNeSevErroredSecs=_AdGenImaLinkTotalNeSevErroredSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1,3),_AdGenImaLinkTotalNeSevErroredSecs_Type())
adGenImaLinkTotalNeSevErroredSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTotalNeSevErroredSecs.setStatus(_A)
_AdGenImaLinkTotalFeSevErroredSecs_Type=Gauge32
_AdGenImaLinkTotalFeSevErroredSecs_Object=MibTableColumn
adGenImaLinkTotalFeSevErroredSecs=_AdGenImaLinkTotalFeSevErroredSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1,4),_AdGenImaLinkTotalFeSevErroredSecs_Type())
adGenImaLinkTotalFeSevErroredSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTotalFeSevErroredSecs.setStatus(_A)
_AdGenImaLinkTotalNeUnavailSecs_Type=Gauge32
_AdGenImaLinkTotalNeUnavailSecs_Object=MibTableColumn
adGenImaLinkTotalNeUnavailSecs=_AdGenImaLinkTotalNeUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1,5),_AdGenImaLinkTotalNeUnavailSecs_Type())
adGenImaLinkTotalNeUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTotalNeUnavailSecs.setStatus(_A)
_AdGenImaLinkTotalFeUnavailSecs_Type=Gauge32
_AdGenImaLinkTotalFeUnavailSecs_Object=MibTableColumn
adGenImaLinkTotalFeUnavailSecs=_AdGenImaLinkTotalFeUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1,6),_AdGenImaLinkTotalFeUnavailSecs_Type())
adGenImaLinkTotalFeUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTotalFeUnavailSecs.setStatus(_A)
_AdGenImaLinkTotalNeTxUnusableSecs_Type=Gauge32
_AdGenImaLinkTotalNeTxUnusableSecs_Object=MibTableColumn
adGenImaLinkTotalNeTxUnusableSecs=_AdGenImaLinkTotalNeTxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1,7),_AdGenImaLinkTotalNeTxUnusableSecs_Type())
adGenImaLinkTotalNeTxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTotalNeTxUnusableSecs.setStatus(_A)
_AdGenImaLinkTotalNeRxUnusableSecs_Type=Gauge32
_AdGenImaLinkTotalNeRxUnusableSecs_Object=MibTableColumn
adGenImaLinkTotalNeRxUnusableSecs=_AdGenImaLinkTotalNeRxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1,8),_AdGenImaLinkTotalNeRxUnusableSecs_Type())
adGenImaLinkTotalNeRxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTotalNeRxUnusableSecs.setStatus(_A)
_AdGenImaLinkTotalFeTxUnusableSecs_Type=Gauge32
_AdGenImaLinkTotalFeTxUnusableSecs_Object=MibTableColumn
adGenImaLinkTotalFeTxUnusableSecs=_AdGenImaLinkTotalFeTxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1,9),_AdGenImaLinkTotalFeTxUnusableSecs_Type())
adGenImaLinkTotalFeTxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTotalFeTxUnusableSecs.setStatus(_A)
_AdGenImaLinkTotalFeRxUnusableSecs_Type=Gauge32
_AdGenImaLinkTotalFeRxUnusableSecs_Object=MibTableColumn
adGenImaLinkTotalFeRxUnusableSecs=_AdGenImaLinkTotalFeRxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1,10),_AdGenImaLinkTotalFeRxUnusableSecs_Type())
adGenImaLinkTotalFeRxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTotalFeRxUnusableSecs.setStatus(_A)
_AdGenImaLinkTotalNeTxNumFailures_Type=Gauge32
_AdGenImaLinkTotalNeTxNumFailures_Object=MibTableColumn
adGenImaLinkTotalNeTxNumFailures=_AdGenImaLinkTotalNeTxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1,11),_AdGenImaLinkTotalNeTxNumFailures_Type())
adGenImaLinkTotalNeTxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTotalNeTxNumFailures.setStatus(_A)
_AdGenImaLinkTotalNeRxNumFailures_Type=Gauge32
_AdGenImaLinkTotalNeRxNumFailures_Object=MibTableColumn
adGenImaLinkTotalNeRxNumFailures=_AdGenImaLinkTotalNeRxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1,12),_AdGenImaLinkTotalNeRxNumFailures_Type())
adGenImaLinkTotalNeRxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTotalNeRxNumFailures.setStatus(_A)
_AdGenImaLinkTotalFeTxNumFailures_Type=Gauge32
_AdGenImaLinkTotalFeTxNumFailures_Object=MibTableColumn
adGenImaLinkTotalFeTxNumFailures=_AdGenImaLinkTotalFeTxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1,13),_AdGenImaLinkTotalFeTxNumFailures_Type())
adGenImaLinkTotalFeTxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTotalFeTxNumFailures.setStatus(_A)
_AdGenImaLinkTotalFeRxNumFailures_Type=Gauge32
_AdGenImaLinkTotalFeRxNumFailures_Object=MibTableColumn
adGenImaLinkTotalFeRxNumFailures=_AdGenImaLinkTotalFeRxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1,14),_AdGenImaLinkTotalFeRxNumFailures_Type())
adGenImaLinkTotalFeRxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTotalFeRxNumFailures.setStatus(_A)
_AdGenImaLinkTotalTxStuffs_Type=Gauge32
_AdGenImaLinkTotalTxStuffs_Object=MibTableColumn
adGenImaLinkTotalTxStuffs=_AdGenImaLinkTotalTxStuffs_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1,15),_AdGenImaLinkTotalTxStuffs_Type())
adGenImaLinkTotalTxStuffs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTotalTxStuffs.setStatus(_A)
_AdGenImaLinkTotalRxStuffs_Type=Gauge32
_AdGenImaLinkTotalRxStuffs_Object=MibTableColumn
adGenImaLinkTotalRxStuffs=_AdGenImaLinkTotalRxStuffs_Object((1,3,6,1,4,1,664,5,67,1,25,4,10,1,16),_AdGenImaLinkTotalRxStuffs_Type())
adGenImaLinkTotalRxStuffs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkTotalRxStuffs.setStatus(_A)
_AdGenImaLinkDayCurrentTable_Object=MibTable
adGenImaLinkDayCurrentTable=_AdGenImaLinkDayCurrentTable_Object((1,3,6,1,4,1,664,5,67,1,25,4,11))
if mibBuilder.loadTexts:adGenImaLinkDayCurrentTable.setStatus(_A)
_AdGenImaLinkDayCurrentEntry_Object=MibTableRow
adGenImaLinkDayCurrentEntry=_AdGenImaLinkDayCurrentEntry_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1))
adGenImaLinkDayCurrentEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenImaLinkDayCurrentEntry.setStatus(_A)
_AdGenImaLinkDayCurrentImaViolations_Type=Gauge32
_AdGenImaLinkDayCurrentImaViolations_Object=MibTableColumn
adGenImaLinkDayCurrentImaViolations=_AdGenImaLinkDayCurrentImaViolations_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1,1),_AdGenImaLinkDayCurrentImaViolations_Type())
adGenImaLinkDayCurrentImaViolations.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayCurrentImaViolations.setStatus(_A)
_AdGenImaLinkDayCurrentOifAnomalies_Type=Gauge32
_AdGenImaLinkDayCurrentOifAnomalies_Object=MibTableColumn
adGenImaLinkDayCurrentOifAnomalies=_AdGenImaLinkDayCurrentOifAnomalies_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1,2),_AdGenImaLinkDayCurrentOifAnomalies_Type())
adGenImaLinkDayCurrentOifAnomalies.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayCurrentOifAnomalies.setStatus(_A)
_AdGenImaLinkDayCurrentNeSevErroredSecs_Type=Gauge32
_AdGenImaLinkDayCurrentNeSevErroredSecs_Object=MibTableColumn
adGenImaLinkDayCurrentNeSevErroredSecs=_AdGenImaLinkDayCurrentNeSevErroredSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1,3),_AdGenImaLinkDayCurrentNeSevErroredSecs_Type())
adGenImaLinkDayCurrentNeSevErroredSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayCurrentNeSevErroredSecs.setStatus(_A)
_AdGenImaLinkDayCurrentFeSevErroredSecs_Type=Gauge32
_AdGenImaLinkDayCurrentFeSevErroredSecs_Object=MibTableColumn
adGenImaLinkDayCurrentFeSevErroredSecs=_AdGenImaLinkDayCurrentFeSevErroredSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1,4),_AdGenImaLinkDayCurrentFeSevErroredSecs_Type())
adGenImaLinkDayCurrentFeSevErroredSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayCurrentFeSevErroredSecs.setStatus(_A)
_AdGenImaLinkDayCurrentNeUnavailSecs_Type=Gauge32
_AdGenImaLinkDayCurrentNeUnavailSecs_Object=MibTableColumn
adGenImaLinkDayCurrentNeUnavailSecs=_AdGenImaLinkDayCurrentNeUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1,5),_AdGenImaLinkDayCurrentNeUnavailSecs_Type())
adGenImaLinkDayCurrentNeUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayCurrentNeUnavailSecs.setStatus(_A)
_AdGenImaLinkDayCurrentFeUnavailSecs_Type=Gauge32
_AdGenImaLinkDayCurrentFeUnavailSecs_Object=MibTableColumn
adGenImaLinkDayCurrentFeUnavailSecs=_AdGenImaLinkDayCurrentFeUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1,6),_AdGenImaLinkDayCurrentFeUnavailSecs_Type())
adGenImaLinkDayCurrentFeUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayCurrentFeUnavailSecs.setStatus(_A)
_AdGenImaLinkDayCurrentNeTxUnusableSecs_Type=Gauge32
_AdGenImaLinkDayCurrentNeTxUnusableSecs_Object=MibTableColumn
adGenImaLinkDayCurrentNeTxUnusableSecs=_AdGenImaLinkDayCurrentNeTxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1,7),_AdGenImaLinkDayCurrentNeTxUnusableSecs_Type())
adGenImaLinkDayCurrentNeTxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayCurrentNeTxUnusableSecs.setStatus(_A)
_AdGenImaLinkDayCurrentNeRxUnusableSecs_Type=Gauge32
_AdGenImaLinkDayCurrentNeRxUnusableSecs_Object=MibTableColumn
adGenImaLinkDayCurrentNeRxUnusableSecs=_AdGenImaLinkDayCurrentNeRxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1,8),_AdGenImaLinkDayCurrentNeRxUnusableSecs_Type())
adGenImaLinkDayCurrentNeRxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayCurrentNeRxUnusableSecs.setStatus(_A)
_AdGenImaLinkDayCurrentFeTxUnusableSecs_Type=Gauge32
_AdGenImaLinkDayCurrentFeTxUnusableSecs_Object=MibTableColumn
adGenImaLinkDayCurrentFeTxUnusableSecs=_AdGenImaLinkDayCurrentFeTxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1,9),_AdGenImaLinkDayCurrentFeTxUnusableSecs_Type())
adGenImaLinkDayCurrentFeTxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayCurrentFeTxUnusableSecs.setStatus(_A)
_AdGenImaLinkDayCurrentFeRxUnusableSecs_Type=Gauge32
_AdGenImaLinkDayCurrentFeRxUnusableSecs_Object=MibTableColumn
adGenImaLinkDayCurrentFeRxUnusableSecs=_AdGenImaLinkDayCurrentFeRxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1,10),_AdGenImaLinkDayCurrentFeRxUnusableSecs_Type())
adGenImaLinkDayCurrentFeRxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayCurrentFeRxUnusableSecs.setStatus(_A)
_AdGenImaLinkDayCurrentNeTxNumFailures_Type=Gauge32
_AdGenImaLinkDayCurrentNeTxNumFailures_Object=MibTableColumn
adGenImaLinkDayCurrentNeTxNumFailures=_AdGenImaLinkDayCurrentNeTxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1,11),_AdGenImaLinkDayCurrentNeTxNumFailures_Type())
adGenImaLinkDayCurrentNeTxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayCurrentNeTxNumFailures.setStatus(_A)
_AdGenImaLinkDayCurrentNeRxNumFailures_Type=Gauge32
_AdGenImaLinkDayCurrentNeRxNumFailures_Object=MibTableColumn
adGenImaLinkDayCurrentNeRxNumFailures=_AdGenImaLinkDayCurrentNeRxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1,12),_AdGenImaLinkDayCurrentNeRxNumFailures_Type())
adGenImaLinkDayCurrentNeRxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayCurrentNeRxNumFailures.setStatus(_A)
_AdGenImaLinkDayCurrentFeTxNumFailures_Type=Gauge32
_AdGenImaLinkDayCurrentFeTxNumFailures_Object=MibTableColumn
adGenImaLinkDayCurrentFeTxNumFailures=_AdGenImaLinkDayCurrentFeTxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1,13),_AdGenImaLinkDayCurrentFeTxNumFailures_Type())
adGenImaLinkDayCurrentFeTxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayCurrentFeTxNumFailures.setStatus(_A)
_AdGenImaLinkDayCurrentFeRxNumFailures_Type=Gauge32
_AdGenImaLinkDayCurrentFeRxNumFailures_Object=MibTableColumn
adGenImaLinkDayCurrentFeRxNumFailures=_AdGenImaLinkDayCurrentFeRxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1,14),_AdGenImaLinkDayCurrentFeRxNumFailures_Type())
adGenImaLinkDayCurrentFeRxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayCurrentFeRxNumFailures.setStatus(_A)
_AdGenImaLinkDayCurrentTxStuffs_Type=Gauge32
_AdGenImaLinkDayCurrentTxStuffs_Object=MibTableColumn
adGenImaLinkDayCurrentTxStuffs=_AdGenImaLinkDayCurrentTxStuffs_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1,15),_AdGenImaLinkDayCurrentTxStuffs_Type())
adGenImaLinkDayCurrentTxStuffs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayCurrentTxStuffs.setStatus(_A)
_AdGenImaLinkDayCurrentRxStuffs_Type=Gauge32
_AdGenImaLinkDayCurrentRxStuffs_Object=MibTableColumn
adGenImaLinkDayCurrentRxStuffs=_AdGenImaLinkDayCurrentRxStuffs_Object((1,3,6,1,4,1,664,5,67,1,25,4,11,1,16),_AdGenImaLinkDayCurrentRxStuffs_Type())
adGenImaLinkDayCurrentRxStuffs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayCurrentRxStuffs.setStatus(_A)
_AdGenImaLinkDayIntervalTable_Object=MibTable
adGenImaLinkDayIntervalTable=_AdGenImaLinkDayIntervalTable_Object((1,3,6,1,4,1,664,5,67,1,25,4,12))
if mibBuilder.loadTexts:adGenImaLinkDayIntervalTable.setStatus(_A)
_AdGenImaLinkDayIntervalEntry_Object=MibTableRow
adGenImaLinkDayIntervalEntry=_AdGenImaLinkDayIntervalEntry_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1))
adGenImaLinkDayIntervalEntry.setIndexNames((0,_C,_D),(0,_O,_b))
if mibBuilder.loadTexts:adGenImaLinkDayIntervalEntry.setStatus(_A)
class _AdGenImaLinkDayIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_AdGenImaLinkDayIntervalNumber_Type.__name__=_K
_AdGenImaLinkDayIntervalNumber_Object=MibTableColumn
adGenImaLinkDayIntervalNumber=_AdGenImaLinkDayIntervalNumber_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,1),_AdGenImaLinkDayIntervalNumber_Type())
adGenImaLinkDayIntervalNumber.setMaxAccess(_Q)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalNumber.setStatus(_A)
_AdGenImaLinkDayIntervalImaViolations_Type=Gauge32
_AdGenImaLinkDayIntervalImaViolations_Object=MibTableColumn
adGenImaLinkDayIntervalImaViolations=_AdGenImaLinkDayIntervalImaViolations_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,2),_AdGenImaLinkDayIntervalImaViolations_Type())
adGenImaLinkDayIntervalImaViolations.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalImaViolations.setStatus(_A)
_AdGenImaLinkDayIntervalOifAnomalies_Type=Gauge32
_AdGenImaLinkDayIntervalOifAnomalies_Object=MibTableColumn
adGenImaLinkDayIntervalOifAnomalies=_AdGenImaLinkDayIntervalOifAnomalies_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,3),_AdGenImaLinkDayIntervalOifAnomalies_Type())
adGenImaLinkDayIntervalOifAnomalies.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalOifAnomalies.setStatus(_A)
_AdGenImaLinkDayIntervalNeSevErroredSecs_Type=Gauge32
_AdGenImaLinkDayIntervalNeSevErroredSecs_Object=MibTableColumn
adGenImaLinkDayIntervalNeSevErroredSecs=_AdGenImaLinkDayIntervalNeSevErroredSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,4),_AdGenImaLinkDayIntervalNeSevErroredSecs_Type())
adGenImaLinkDayIntervalNeSevErroredSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalNeSevErroredSecs.setStatus(_A)
_AdGenImaLinkDayIntervalFeSevErroredSecs_Type=Gauge32
_AdGenImaLinkDayIntervalFeSevErroredSecs_Object=MibTableColumn
adGenImaLinkDayIntervalFeSevErroredSecs=_AdGenImaLinkDayIntervalFeSevErroredSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,5),_AdGenImaLinkDayIntervalFeSevErroredSecs_Type())
adGenImaLinkDayIntervalFeSevErroredSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalFeSevErroredSecs.setStatus(_A)
_AdGenImaLinkDayIntervalNeUnavailSecs_Type=Gauge32
_AdGenImaLinkDayIntervalNeUnavailSecs_Object=MibTableColumn
adGenImaLinkDayIntervalNeUnavailSecs=_AdGenImaLinkDayIntervalNeUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,6),_AdGenImaLinkDayIntervalNeUnavailSecs_Type())
adGenImaLinkDayIntervalNeUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalNeUnavailSecs.setStatus(_A)
_AdGenImaLinkDayIntervalFeUnavailSecs_Type=Gauge32
_AdGenImaLinkDayIntervalFeUnavailSecs_Object=MibTableColumn
adGenImaLinkDayIntervalFeUnavailSecs=_AdGenImaLinkDayIntervalFeUnavailSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,7),_AdGenImaLinkDayIntervalFeUnavailSecs_Type())
adGenImaLinkDayIntervalFeUnavailSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalFeUnavailSecs.setStatus(_A)
_AdGenImaLinkDayIntervalNeTxUnusableSecs_Type=Gauge32
_AdGenImaLinkDayIntervalNeTxUnusableSecs_Object=MibTableColumn
adGenImaLinkDayIntervalNeTxUnusableSecs=_AdGenImaLinkDayIntervalNeTxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,8),_AdGenImaLinkDayIntervalNeTxUnusableSecs_Type())
adGenImaLinkDayIntervalNeTxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalNeTxUnusableSecs.setStatus(_A)
_AdGenImaLinkDayIntervalNeRxUnusableSecs_Type=Gauge32
_AdGenImaLinkDayIntervalNeRxUnusableSecs_Object=MibTableColumn
adGenImaLinkDayIntervalNeRxUnusableSecs=_AdGenImaLinkDayIntervalNeRxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,9),_AdGenImaLinkDayIntervalNeRxUnusableSecs_Type())
adGenImaLinkDayIntervalNeRxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalNeRxUnusableSecs.setStatus(_A)
_AdGenImaLinkDayIntervalFeTxUnusableSecs_Type=Gauge32
_AdGenImaLinkDayIntervalFeTxUnusableSecs_Object=MibTableColumn
adGenImaLinkDayIntervalFeTxUnusableSecs=_AdGenImaLinkDayIntervalFeTxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,10),_AdGenImaLinkDayIntervalFeTxUnusableSecs_Type())
adGenImaLinkDayIntervalFeTxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalFeTxUnusableSecs.setStatus(_A)
_AdGenImaLinkDayIntervalFeRxUnusableSecs_Type=Gauge32
_AdGenImaLinkDayIntervalFeRxUnusableSecs_Object=MibTableColumn
adGenImaLinkDayIntervalFeRxUnusableSecs=_AdGenImaLinkDayIntervalFeRxUnusableSecs_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,11),_AdGenImaLinkDayIntervalFeRxUnusableSecs_Type())
adGenImaLinkDayIntervalFeRxUnusableSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalFeRxUnusableSecs.setStatus(_A)
_AdGenImaLinkDayIntervalNeTxNumFailures_Type=Gauge32
_AdGenImaLinkDayIntervalNeTxNumFailures_Object=MibTableColumn
adGenImaLinkDayIntervalNeTxNumFailures=_AdGenImaLinkDayIntervalNeTxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,12),_AdGenImaLinkDayIntervalNeTxNumFailures_Type())
adGenImaLinkDayIntervalNeTxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalNeTxNumFailures.setStatus(_A)
_AdGenImaLinkDayIntervalNeRxNumFailures_Type=Gauge32
_AdGenImaLinkDayIntervalNeRxNumFailures_Object=MibTableColumn
adGenImaLinkDayIntervalNeRxNumFailures=_AdGenImaLinkDayIntervalNeRxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,13),_AdGenImaLinkDayIntervalNeRxNumFailures_Type())
adGenImaLinkDayIntervalNeRxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalNeRxNumFailures.setStatus(_A)
_AdGenImaLinkDayIntervalFeTxNumFailures_Type=Gauge32
_AdGenImaLinkDayIntervalFeTxNumFailures_Object=MibTableColumn
adGenImaLinkDayIntervalFeTxNumFailures=_AdGenImaLinkDayIntervalFeTxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,14),_AdGenImaLinkDayIntervalFeTxNumFailures_Type())
adGenImaLinkDayIntervalFeTxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalFeTxNumFailures.setStatus(_A)
_AdGenImaLinkDayIntervalFeRxNumFailures_Type=Gauge32
_AdGenImaLinkDayIntervalFeRxNumFailures_Object=MibTableColumn
adGenImaLinkDayIntervalFeRxNumFailures=_AdGenImaLinkDayIntervalFeRxNumFailures_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,15),_AdGenImaLinkDayIntervalFeRxNumFailures_Type())
adGenImaLinkDayIntervalFeRxNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalFeRxNumFailures.setStatus(_A)
_AdGenImaLinkDayIntervalTxStuffs_Type=Gauge32
_AdGenImaLinkDayIntervalTxStuffs_Object=MibTableColumn
adGenImaLinkDayIntervalTxStuffs=_AdGenImaLinkDayIntervalTxStuffs_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,16),_AdGenImaLinkDayIntervalTxStuffs_Type())
adGenImaLinkDayIntervalTxStuffs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalTxStuffs.setStatus(_A)
_AdGenImaLinkDayIntervalRxStuffs_Type=Gauge32
_AdGenImaLinkDayIntervalRxStuffs_Object=MibTableColumn
adGenImaLinkDayIntervalRxStuffs=_AdGenImaLinkDayIntervalRxStuffs_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,17),_AdGenImaLinkDayIntervalRxStuffs_Type())
adGenImaLinkDayIntervalRxStuffs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalRxStuffs.setStatus(_A)
_AdGenImaLinkDayIntervalTimeStamp_Type=DisplayString
_AdGenImaLinkDayIntervalTimeStamp_Object=MibTableColumn
adGenImaLinkDayIntervalTimeStamp=_AdGenImaLinkDayIntervalTimeStamp_Object((1,3,6,1,4,1,664,5,67,1,25,4,12,1,18),_AdGenImaLinkDayIntervalTimeStamp_Type())
adGenImaLinkDayIntervalTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenImaLinkDayIntervalTimeStamp.setStatus(_A)
_AdGenImaAlarmsPrefix_ObjectIdentity=ObjectIdentity
adGenImaAlarmsPrefix=_AdGenImaAlarmsPrefix_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,25,10))
_AdGenImaAlarms_ObjectIdentity=ObjectIdentity
adGenImaAlarms=_AdGenImaAlarms_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,25,10,0))
adGenImaGroupCfgAbortClr=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,2))
adGenImaGroupCfgAbortClr.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_C,_D)))
if mibBuilder.loadTexts:adGenImaGroupCfgAbortClr.setStatus(_A)
adGenImaGroupCfgAbortAct=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,3))
adGenImaGroupCfgAbortAct.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_C,_D)))
if mibBuilder.loadTexts:adGenImaGroupCfgAbortAct.setStatus(_A)
adGenImaGroupCfgInsufficentLinksClr=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,4))
adGenImaGroupCfgInsufficentLinksClr.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_C,_D)))
if mibBuilder.loadTexts:adGenImaGroupCfgInsufficentLinksClr.setStatus(_A)
adGenImaGroupCfgInsufficentLinksAct=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,5))
adGenImaGroupCfgInsufficentLinksAct.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_C,_D)))
if mibBuilder.loadTexts:adGenImaGroupCfgInsufficentLinksAct.setStatus(_A)
adGenImaGroupFeStartupClr=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,6))
adGenImaGroupFeStartupClr.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_C,_D)))
if mibBuilder.loadTexts:adGenImaGroupFeStartupClr.setStatus(_A)
adGenImaGroupFeStartupAct=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,7))
adGenImaGroupFeStartupAct.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_C,_D)))
if mibBuilder.loadTexts:adGenImaGroupFeStartupAct.setStatus(_A)
adGenImaGroupFeCfgAbortClr=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,8))
adGenImaGroupFeCfgAbortClr.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_C,_D)))
if mibBuilder.loadTexts:adGenImaGroupFeCfgAbortClr.setStatus(_A)
adGenImaGroupFeCfgAbortAct=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,9))
adGenImaGroupFeCfgAbortAct.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_C,_D)))
if mibBuilder.loadTexts:adGenImaGroupFeCfgAbortAct.setStatus(_A)
adGenImaGroupFeCfgInsufficentLinksClr=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,10))
adGenImaGroupFeCfgInsufficentLinksClr.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_C,_D)))
if mibBuilder.loadTexts:adGenImaGroupFeCfgInsufficentLinksClr.setStatus(_A)
adGenImaGroupFeCfgInsufficentLinksAct=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,11))
adGenImaGroupFeCfgInsufficentLinksAct.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_C,_D)))
if mibBuilder.loadTexts:adGenImaGroupFeCfgInsufficentLinksAct.setStatus(_A)
adGenImaGroupFeBlockedClr=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,12))
adGenImaGroupFeBlockedClr.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_C,_D)))
if mibBuilder.loadTexts:adGenImaGroupFeBlockedClr.setStatus(_A)
adGenImaGroupFeBlockedAct=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,13))
adGenImaGroupFeBlockedAct.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_C,_D)))
if mibBuilder.loadTexts:adGenImaGroupFeBlockedAct.setStatus(_A)
adGenImaGroupTimingMismatchClr=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,14))
adGenImaGroupTimingMismatchClr.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_C,_D)))
if mibBuilder.loadTexts:adGenImaGroupTimingMismatchClr.setStatus(_A)
adGenImaGroupTimingMismatchAct=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,15))
adGenImaGroupTimingMismatchAct.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_C,_D)))
if mibBuilder.loadTexts:adGenImaGroupTimingMismatchAct.setStatus(_A)
adGenImaLinkLifClr=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,16))
adGenImaLinkLifClr.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkLifClr.setStatus(_A)
adGenImaLinkLifAct=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,17))
adGenImaLinkLifAct.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkLifAct.setStatus(_A)
adGenImaLinkLodsClr=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,18))
adGenImaLinkLodsClr.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkLodsClr.setStatus(_A)
adGenImaLinkLodsAct=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,19))
adGenImaLinkLodsAct.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkLodsAct.setStatus(_A)
adGenImaLinkRfiClr=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,20))
adGenImaLinkRfiClr.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkRfiClr.setStatus(_A)
adGenImaLinkRfiAct=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,21))
adGenImaLinkRfiAct.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkRfiAct.setStatus(_A)
adGenImaLinkTxMisconnectedClr=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,22))
adGenImaLinkTxMisconnectedClr.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkTxMisconnectedClr.setStatus(_A)
adGenImaLinkTxMisconnectedAct=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,23))
adGenImaLinkTxMisconnectedAct.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkTxMisconnectedAct.setStatus(_A)
adGenImaLinkRxMisconnectedClr=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,24))
adGenImaLinkRxMisconnectedClr.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkRxMisconnectedClr.setStatus(_A)
adGenImaLinkRxMisconnectedAct=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,25))
adGenImaLinkRxMisconnectedAct.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkRxMisconnectedAct.setStatus(_A)
adGenImaLinkTxFaultClr=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,26))
adGenImaLinkTxFaultClr.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkTxFaultClr.setStatus(_A)
adGenImaLinkTxFaultAct=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,27))
adGenImaLinkTxFaultAct.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkTxFaultAct.setStatus(_A)
adGenImaLinkRxFaultClr=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,28))
adGenImaLinkRxFaultClr.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkRxFaultClr.setStatus(_A)
adGenImaLinkRxFaultAct=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,29))
adGenImaLinkRxFaultAct.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkRxFaultAct.setStatus(_A)
adGenImaLinkFeTxUnusableClr=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,30))
adGenImaLinkFeTxUnusableClr.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkFeTxUnusableClr.setStatus(_A)
adGenImaLinkFeTxUnusableAct=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,31))
adGenImaLinkFeTxUnusableAct.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkFeTxUnusableAct.setStatus(_A)
adGenImaLinkFeRxUnusableClr=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,32))
adGenImaLinkFeRxUnusableClr.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkFeRxUnusableClr.setStatus(_A)
adGenImaLinkFeRxUnusableAct=NotificationType((1,3,6,1,4,1,664,5,67,1,25,10,0,33))
adGenImaLinkFeRxUnusableAct.setObjects(*((_G,_H),(_I,_J),(_E,_F),(_L,_M),(_C,_D)))
if mibBuilder.loadTexts:adGenImaLinkFeRxUnusableAct.setStatus(_A)
mibBuilder.exportSymbols(_O,**{'adGenImaProvisioning':adGenImaProvisioning,'adGenImaGroupProvTable':adGenImaGroupProvTable,'adGenImaGroupProvEntry':adGenImaGroupProvEntry,'adGenImaGroupVersion':adGenImaGroupVersion,'adGenImaGroupSymmetry':adGenImaGroupSymmetry,'adGenImaGroupNeTxClkMode':adGenImaGroupNeTxClkMode,'adGenImaGroupTxImaId':adGenImaGroupTxImaId,'adGenImaGroupTxFrameLength':adGenImaGroupTxFrameLength,'adGenImaGroupDiffDelayMax':adGenImaGroupDiffDelayMax,'adGenImaGroupAlphaValue':adGenImaGroupAlphaValue,'adGenImaGroupBetaValue':adGenImaGroupBetaValue,'adGenImaGroupGammaValue':adGenImaGroupGammaValue,'adGenImaGroupTxClkSource':adGenImaGroupTxClkSource,'adGenImaAtmGroupCommonProvTable':adGenImaAtmGroupCommonProvTable,'adGenImaAtmGroupCommonProvEntry':adGenImaAtmGroupCommonProvEntry,'adGenImaAtmGroupCommonProvDhcpCircuitIdFormat':adGenImaAtmGroupCommonProvDhcpCircuitIdFormat,'adGenImaStatus':adGenImaStatus,'adGenImaGroupStatusTable':adGenImaGroupStatusTable,'adGenImaGroupStatusEntry':adGenImaGroupStatusEntry,'adGenImaGroupNeState':adGenImaGroupNeState,'adGenImaGroupFeState':adGenImaGroupFeState,'adGenImaGroupFailureStatus':adGenImaGroupFailureStatus,'adGenImaGroupLastChange':adGenImaGroupLastChange,'adGenImaGroupRunningSecs':adGenImaGroupRunningSecs,'adGenImaGroupFeTxClkMode':adGenImaGroupFeTxClkMode,'adGenImaGroupTxTimingRefLink':adGenImaGroupTxTimingRefLink,'adGenImaGroupRxTimingRefLink':adGenImaGroupRxTimingRefLink,'adGenImaGroupRxImaId':adGenImaGroupRxImaId,'adGenImaGroupRxFrameLength':adGenImaGroupRxFrameLength,'adGenImaGroupLeastDelayLink':adGenImaGroupLeastDelayLink,'adGenImaGroupDiffDelayMaxObs':adGenImaGroupDiffDelayMaxObs,'adGenImaGroupTxAvailCellRate':adGenImaGroupTxAvailCellRate,'adGenImaGroupRxAvailCellRate':adGenImaGroupRxAvailCellRate,'adGenImaGroupTxOamLabelValue':adGenImaGroupTxOamLabelValue,'adGenImaGroupRxOamLabelValue':adGenImaGroupRxOamLabelValue,'adGenImaLinkStatusTable':adGenImaLinkStatusTable,'adGenImaLinkStatusEntry':adGenImaLinkStatusEntry,'adGenImaLinkNeTxState':adGenImaLinkNeTxState,'adGenImaLinkNeRxState':adGenImaLinkNeRxState,'adGenImaLinkFeTxState':adGenImaLinkFeTxState,'adGenImaLinkFeRxState':adGenImaLinkFeRxState,'adGenImaLinkNeRxFailureStatus':adGenImaLinkNeRxFailureStatus,'adGenImaLinkFeRxFailureStatus':adGenImaLinkFeRxFailureStatus,'adGenImaLinkTxLid':adGenImaLinkTxLid,'adGenImaLinkRxLid':adGenImaLinkRxLid,'adGenImaLinkRelDelay':adGenImaLinkRelDelay,'adGenImaTest':adGenImaTest,'adGenImaGroupTestTable':adGenImaGroupTestTable,'adGenImaGroupTestEntry':adGenImaGroupTestEntry,'adGenImaGroupTestLinkIfIndex':adGenImaGroupTestLinkIfIndex,'adGenImaGroupTestPattern':adGenImaGroupTestPattern,'adGenImaGroupTestProcStatus':adGenImaGroupTestProcStatus,'adGenImaLinkTestTable':adGenImaLinkTestTable,'adGenImaLinkTestEntry':adGenImaLinkTestEntry,'adGenImaLinkRxTestPattern':adGenImaLinkRxTestPattern,'adGenImaLinkTestProcStatus':adGenImaLinkTestProcStatus,'adGenImaPerformance':adGenImaPerformance,'adGenImaGroupPerfTable':adGenImaGroupPerfTable,'adGenImaGroupPerfEntry':adGenImaGroupPerfEntry,'adGenImaGroupUnavailSecs':adGenImaGroupUnavailSecs,'adGenImaGroupNeNumFailures':adGenImaGroupNeNumFailures,'adGenImaGroupFeNumFailures':adGenImaGroupFeNumFailures,'adGenImaGroupValidIntervals':adGenImaGroupValidIntervals,'adGenImaGroupInvalidIntervals':adGenImaGroupInvalidIntervals,'adGenImaGroupTimeElapsed':adGenImaGroupTimeElapsed,'adGenImaGroupResetStats':adGenImaGroupResetStats,'adGenImaGroupResetPerfHistory':adGenImaGroupResetPerfHistory,'adGenImaLinkPerfTable':adGenImaLinkPerfTable,'adGenImaLinkPerfEntry':adGenImaLinkPerfEntry,'adGenImaLinkImaViolations':adGenImaLinkImaViolations,'adGenImaLinkOifAnomalies':adGenImaLinkOifAnomalies,'adGenImaLinkNeSevErroredSecs':adGenImaLinkNeSevErroredSecs,'adGenImaLinkFeSevErroredSecs':adGenImaLinkFeSevErroredSecs,'adGenImaLinkNeUnavailSecs':adGenImaLinkNeUnavailSecs,'adGenImaLinkFeUnavailSecs':adGenImaLinkFeUnavailSecs,'adGenImaLinkNeTxUnusableSecs':adGenImaLinkNeTxUnusableSecs,'adGenImaLinkNeRxUnusableSecs':adGenImaLinkNeRxUnusableSecs,'adGenImaLinkFeTxUnusableSecs':adGenImaLinkFeTxUnusableSecs,'adGenImaLinkFeRxUnusableSecs':adGenImaLinkFeRxUnusableSecs,'adGenImaLinkNeTxNumFailures':adGenImaLinkNeTxNumFailures,'adGenImaLinkNeRxNumFailures':adGenImaLinkNeRxNumFailures,'adGenImaLinkFeTxNumFailures':adGenImaLinkFeTxNumFailures,'adGenImaLinkFeRxNumFailures':adGenImaLinkFeRxNumFailures,'adGenImaLinkTxStuffs':adGenImaLinkTxStuffs,'adGenImaLinkRxStuffs':adGenImaLinkRxStuffs,'adGenImaLinkValidIntervals':adGenImaLinkValidIntervals,'adGenImaLinkInvalidIntervals':adGenImaLinkInvalidIntervals,'adGenImaLinkTimeElapsed':adGenImaLinkTimeElapsed,'adGenImaLinkResetStats':adGenImaLinkResetStats,'adGenImaLinkResetPerfHistory':adGenImaLinkResetPerfHistory,'adGenImaGroupCurrentTable':adGenImaGroupCurrentTable,'adGenImaGroupCurrentEntry':adGenImaGroupCurrentEntry,'adGenImaGroupCurrentUnavailSecs':adGenImaGroupCurrentUnavailSecs,'adGenImaGroupCurrentNeNumFailures':adGenImaGroupCurrentNeNumFailures,'adGenImaGroupCurrentFeNumFailures':adGenImaGroupCurrentFeNumFailures,'adGenImaGroupIntervalTable':adGenImaGroupIntervalTable,'adGenImaGroupIntervalEntry':adGenImaGroupIntervalEntry,_Y:adGenImaGroupIntervalNumber,'adGenImaGroupIntervalUnavailSecs':adGenImaGroupIntervalUnavailSecs,'adGenImaGroupIntervalNeNumFailures':adGenImaGroupIntervalNeNumFailures,'adGenImaGroupIntervalFeNumFailures':adGenImaGroupIntervalFeNumFailures,'adGenImaGroupIntervalTimeStamp':adGenImaGroupIntervalTimeStamp,'adGenImaGroupTotalTable':adGenImaGroupTotalTable,'adGenImaGroupTotalEntry':adGenImaGroupTotalEntry,'adGenImaGroupTotalUnavailSecs':adGenImaGroupTotalUnavailSecs,'adGenImaGroupTotalNeNumFailures':adGenImaGroupTotalNeNumFailures,'adGenImaGroupTotalFeNumFailures':adGenImaGroupTotalFeNumFailures,'adGenImaGroupDayCurrentTable':adGenImaGroupDayCurrentTable,'adGenImaGroupDayCurrentEntry':adGenImaGroupDayCurrentEntry,'adGenImaGroupDayCurrentUnavailSecs':adGenImaGroupDayCurrentUnavailSecs,'adGenImaGroupDayCurrentNeNumFailures':adGenImaGroupDayCurrentNeNumFailures,'adGenImaGroupDayCurrentFeNumFailures':adGenImaGroupDayCurrentFeNumFailures,'adGenImaGroupDayIntervalTable':adGenImaGroupDayIntervalTable,'adGenImaGroupDayIntervalEntry':adGenImaGroupDayIntervalEntry,_Z:adGenImaGroupDayIntervalNumber,'adGenImaGroupDayIntervalUnavailSecs':adGenImaGroupDayIntervalUnavailSecs,'adGenImaGroupDayIntervalNeNumFailures':adGenImaGroupDayIntervalNeNumFailures,'adGenImaGroupDayIntervalFeNumFailures':adGenImaGroupDayIntervalFeNumFailures,'adGenImaGroupDayIntervalTimeStamp':adGenImaGroupDayIntervalTimeStamp,'adGenImaLinkCurrentTable':adGenImaLinkCurrentTable,'adGenImaLinkCurrentEntry':adGenImaLinkCurrentEntry,'adGenImaLinkCurrentImaViolations':adGenImaLinkCurrentImaViolations,'adGenImaLinkCurrentOifAnomalies':adGenImaLinkCurrentOifAnomalies,'adGenImaLinkCurrentNeSevErroredSecs':adGenImaLinkCurrentNeSevErroredSecs,'adGenImaLinkCurrentFeSevErroredSecs':adGenImaLinkCurrentFeSevErroredSecs,'adGenImaLinkCurrentNeUnavailSecs':adGenImaLinkCurrentNeUnavailSecs,'adGenImaLinkCurrentFeUnavailSecs':adGenImaLinkCurrentFeUnavailSecs,'adGenImaLinkCurrentNeTxUnusableSecs':adGenImaLinkCurrentNeTxUnusableSecs,'adGenImaLinkCurrentNeRxUnusableSecs':adGenImaLinkCurrentNeRxUnusableSecs,'adGenImaLinkCurrentFeTxUnusableSecs':adGenImaLinkCurrentFeTxUnusableSecs,'adGenImaLinkCurrentFeRxUnusableSecs':adGenImaLinkCurrentFeRxUnusableSecs,'adGenImaLinkCurrentNeTxNumFailures':adGenImaLinkCurrentNeTxNumFailures,'adGenImaLinkCurrentNeRxNumFailures':adGenImaLinkCurrentNeRxNumFailures,'adGenImaLinkCurrentFeTxNumFailures':adGenImaLinkCurrentFeTxNumFailures,'adGenImaLinkCurrentFeRxNumFailures':adGenImaLinkCurrentFeRxNumFailures,'adGenImaLinkCurrentTxStuffs':adGenImaLinkCurrentTxStuffs,'adGenImaLinkCurrentRxStuffs':adGenImaLinkCurrentRxStuffs,'adGenImaLinkIntervalTable':adGenImaLinkIntervalTable,'adGenImaLinkIntervalEntry':adGenImaLinkIntervalEntry,_a:adGenImaLinkIntervalNumber,'adGenImaLinkIntervalImaViolations':adGenImaLinkIntervalImaViolations,'adGenImaLinkIntervalOifAnomalies':adGenImaLinkIntervalOifAnomalies,'adGenImaLinkIntervalNeSevErroredSecs':adGenImaLinkIntervalNeSevErroredSecs,'adGenImaLinkIntervalFeSevErroredSecs':adGenImaLinkIntervalFeSevErroredSecs,'adGenImaLinkIntervalNeUnavailSecs':adGenImaLinkIntervalNeUnavailSecs,'adGenImaLinkIntervalFeUnavailSecs':adGenImaLinkIntervalFeUnavailSecs,'adGenImaLinkIntervalNeTxUnusableSecs':adGenImaLinkIntervalNeTxUnusableSecs,'adGenImaLinkIntervalNeRxUnusableSecs':adGenImaLinkIntervalNeRxUnusableSecs,'adGenImaLinkIntervalFeTxUnusableSecs':adGenImaLinkIntervalFeTxUnusableSecs,'adGenImaLinkIntervalFeRxUnusableSecs':adGenImaLinkIntervalFeRxUnusableSecs,'adGenImaLinkIntervalNeTxNumFailures':adGenImaLinkIntervalNeTxNumFailures,'adGenImaLinkIntervalNeRxNumFailures':adGenImaLinkIntervalNeRxNumFailures,'adGenImaLinkIntervalFeTxNumFailures':adGenImaLinkIntervalFeTxNumFailures,'adGenImaLinkIntervalFeRxNumFailures':adGenImaLinkIntervalFeRxNumFailures,'adGenImaLinkIntervalTxStuffs':adGenImaLinkIntervalTxStuffs,'adGenImaLinkIntervalRxStuffs':adGenImaLinkIntervalRxStuffs,'adGenImaLinkIntervalTimeStamp':adGenImaLinkIntervalTimeStamp,'adGenImaLinkTotalTable':adGenImaLinkTotalTable,'adGenImaLinkTotalEntry':adGenImaLinkTotalEntry,'adGenImaLinkTotalImaViolations':adGenImaLinkTotalImaViolations,'adGenImaLinkTotalOifAnomalies':adGenImaLinkTotalOifAnomalies,'adGenImaLinkTotalNeSevErroredSecs':adGenImaLinkTotalNeSevErroredSecs,'adGenImaLinkTotalFeSevErroredSecs':adGenImaLinkTotalFeSevErroredSecs,'adGenImaLinkTotalNeUnavailSecs':adGenImaLinkTotalNeUnavailSecs,'adGenImaLinkTotalFeUnavailSecs':adGenImaLinkTotalFeUnavailSecs,'adGenImaLinkTotalNeTxUnusableSecs':adGenImaLinkTotalNeTxUnusableSecs,'adGenImaLinkTotalNeRxUnusableSecs':adGenImaLinkTotalNeRxUnusableSecs,'adGenImaLinkTotalFeTxUnusableSecs':adGenImaLinkTotalFeTxUnusableSecs,'adGenImaLinkTotalFeRxUnusableSecs':adGenImaLinkTotalFeRxUnusableSecs,'adGenImaLinkTotalNeTxNumFailures':adGenImaLinkTotalNeTxNumFailures,'adGenImaLinkTotalNeRxNumFailures':adGenImaLinkTotalNeRxNumFailures,'adGenImaLinkTotalFeTxNumFailures':adGenImaLinkTotalFeTxNumFailures,'adGenImaLinkTotalFeRxNumFailures':adGenImaLinkTotalFeRxNumFailures,'adGenImaLinkTotalTxStuffs':adGenImaLinkTotalTxStuffs,'adGenImaLinkTotalRxStuffs':adGenImaLinkTotalRxStuffs,'adGenImaLinkDayCurrentTable':adGenImaLinkDayCurrentTable,'adGenImaLinkDayCurrentEntry':adGenImaLinkDayCurrentEntry,'adGenImaLinkDayCurrentImaViolations':adGenImaLinkDayCurrentImaViolations,'adGenImaLinkDayCurrentOifAnomalies':adGenImaLinkDayCurrentOifAnomalies,'adGenImaLinkDayCurrentNeSevErroredSecs':adGenImaLinkDayCurrentNeSevErroredSecs,'adGenImaLinkDayCurrentFeSevErroredSecs':adGenImaLinkDayCurrentFeSevErroredSecs,'adGenImaLinkDayCurrentNeUnavailSecs':adGenImaLinkDayCurrentNeUnavailSecs,'adGenImaLinkDayCurrentFeUnavailSecs':adGenImaLinkDayCurrentFeUnavailSecs,'adGenImaLinkDayCurrentNeTxUnusableSecs':adGenImaLinkDayCurrentNeTxUnusableSecs,'adGenImaLinkDayCurrentNeRxUnusableSecs':adGenImaLinkDayCurrentNeRxUnusableSecs,'adGenImaLinkDayCurrentFeTxUnusableSecs':adGenImaLinkDayCurrentFeTxUnusableSecs,'adGenImaLinkDayCurrentFeRxUnusableSecs':adGenImaLinkDayCurrentFeRxUnusableSecs,'adGenImaLinkDayCurrentNeTxNumFailures':adGenImaLinkDayCurrentNeTxNumFailures,'adGenImaLinkDayCurrentNeRxNumFailures':adGenImaLinkDayCurrentNeRxNumFailures,'adGenImaLinkDayCurrentFeTxNumFailures':adGenImaLinkDayCurrentFeTxNumFailures,'adGenImaLinkDayCurrentFeRxNumFailures':adGenImaLinkDayCurrentFeRxNumFailures,'adGenImaLinkDayCurrentTxStuffs':adGenImaLinkDayCurrentTxStuffs,'adGenImaLinkDayCurrentRxStuffs':adGenImaLinkDayCurrentRxStuffs,'adGenImaLinkDayIntervalTable':adGenImaLinkDayIntervalTable,'adGenImaLinkDayIntervalEntry':adGenImaLinkDayIntervalEntry,_b:adGenImaLinkDayIntervalNumber,'adGenImaLinkDayIntervalImaViolations':adGenImaLinkDayIntervalImaViolations,'adGenImaLinkDayIntervalOifAnomalies':adGenImaLinkDayIntervalOifAnomalies,'adGenImaLinkDayIntervalNeSevErroredSecs':adGenImaLinkDayIntervalNeSevErroredSecs,'adGenImaLinkDayIntervalFeSevErroredSecs':adGenImaLinkDayIntervalFeSevErroredSecs,'adGenImaLinkDayIntervalNeUnavailSecs':adGenImaLinkDayIntervalNeUnavailSecs,'adGenImaLinkDayIntervalFeUnavailSecs':adGenImaLinkDayIntervalFeUnavailSecs,'adGenImaLinkDayIntervalNeTxUnusableSecs':adGenImaLinkDayIntervalNeTxUnusableSecs,'adGenImaLinkDayIntervalNeRxUnusableSecs':adGenImaLinkDayIntervalNeRxUnusableSecs,'adGenImaLinkDayIntervalFeTxUnusableSecs':adGenImaLinkDayIntervalFeTxUnusableSecs,'adGenImaLinkDayIntervalFeRxUnusableSecs':adGenImaLinkDayIntervalFeRxUnusableSecs,'adGenImaLinkDayIntervalNeTxNumFailures':adGenImaLinkDayIntervalNeTxNumFailures,'adGenImaLinkDayIntervalNeRxNumFailures':adGenImaLinkDayIntervalNeRxNumFailures,'adGenImaLinkDayIntervalFeTxNumFailures':adGenImaLinkDayIntervalFeTxNumFailures,'adGenImaLinkDayIntervalFeRxNumFailures':adGenImaLinkDayIntervalFeRxNumFailures,'adGenImaLinkDayIntervalTxStuffs':adGenImaLinkDayIntervalTxStuffs,'adGenImaLinkDayIntervalRxStuffs':adGenImaLinkDayIntervalRxStuffs,'adGenImaLinkDayIntervalTimeStamp':adGenImaLinkDayIntervalTimeStamp,'adGenImaAlarmsPrefix':adGenImaAlarmsPrefix,'adGenImaAlarms':adGenImaAlarms,'adGenImaGroupCfgAbortClr':adGenImaGroupCfgAbortClr,'adGenImaGroupCfgAbortAct':adGenImaGroupCfgAbortAct,'adGenImaGroupCfgInsufficentLinksClr':adGenImaGroupCfgInsufficentLinksClr,'adGenImaGroupCfgInsufficentLinksAct':adGenImaGroupCfgInsufficentLinksAct,'adGenImaGroupFeStartupClr':adGenImaGroupFeStartupClr,'adGenImaGroupFeStartupAct':adGenImaGroupFeStartupAct,'adGenImaGroupFeCfgAbortClr':adGenImaGroupFeCfgAbortClr,'adGenImaGroupFeCfgAbortAct':adGenImaGroupFeCfgAbortAct,'adGenImaGroupFeCfgInsufficentLinksClr':adGenImaGroupFeCfgInsufficentLinksClr,'adGenImaGroupFeCfgInsufficentLinksAct':adGenImaGroupFeCfgInsufficentLinksAct,'adGenImaGroupFeBlockedClr':adGenImaGroupFeBlockedClr,'adGenImaGroupFeBlockedAct':adGenImaGroupFeBlockedAct,'adGenImaGroupTimingMismatchClr':adGenImaGroupTimingMismatchClr,'adGenImaGroupTimingMismatchAct':adGenImaGroupTimingMismatchAct,'adGenImaLinkLifClr':adGenImaLinkLifClr,'adGenImaLinkLifAct':adGenImaLinkLifAct,'adGenImaLinkLodsClr':adGenImaLinkLodsClr,'adGenImaLinkLodsAct':adGenImaLinkLodsAct,'adGenImaLinkRfiClr':adGenImaLinkRfiClr,'adGenImaLinkRfiAct':adGenImaLinkRfiAct,'adGenImaLinkTxMisconnectedClr':adGenImaLinkTxMisconnectedClr,'adGenImaLinkTxMisconnectedAct':adGenImaLinkTxMisconnectedAct,'adGenImaLinkRxMisconnectedClr':adGenImaLinkRxMisconnectedClr,'adGenImaLinkRxMisconnectedAct':adGenImaLinkRxMisconnectedAct,'adGenImaLinkTxFaultClr':adGenImaLinkTxFaultClr,'adGenImaLinkTxFaultAct':adGenImaLinkTxFaultAct,'adGenImaLinkRxFaultClr':adGenImaLinkRxFaultClr,'adGenImaLinkRxFaultAct':adGenImaLinkRxFaultAct,'adGenImaLinkFeTxUnusableClr':adGenImaLinkFeTxUnusableClr,'adGenImaLinkFeTxUnusableAct':adGenImaLinkFeTxUnusableAct,'adGenImaLinkFeRxUnusableClr':adGenImaLinkFeRxUnusableClr,'adGenImaLinkFeRxUnusableAct':adGenImaLinkFeRxUnusableAct,'adGenImaMIB':adGenImaMIB})