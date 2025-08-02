_Q='rate24330Mbps'
_P='rate12165Mbps'
_O='rate10137Mbps'
_N='rate8110Mbps'
_M='rate9830Mbps'
_L='rate6144Mbps'
_K='rate4915Mbps'
_J='rate3072Mbps'
_I='rate2457Mbps'
_H='rate1228Mbps'
_G='rate614Mbps'
_F='ifIndex'
_E='IF-MIB'
_D='Bits'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,ifName=mibBuilder.importSymbols(_E,_F,'ifName')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_D,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp','TruthValue')
ciscoCpriMIB=ModuleIdentity((1,3,6,1,4,1,9,9,9999))
if mibBuilder.loadTexts:ciscoCpriMIB.setRevisions(('2020-09-10 00:00',))
_CiscoCpriMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCpriMIBNotifs=_CiscoCpriMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,9999,0))
_CiscoCpriMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCpriMIBObjects=_CiscoCpriMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1))
_CoiCpriController_ObjectIdentity=ObjectIdentity
coiCpriController=_CoiCpriController_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1,1))
_CoiCpriControllerTable_Object=MibTable
coiCpriControllerTable=_CoiCpriControllerTable_Object((1,3,6,1,4,1,9,9,9999,1,1,1))
if mibBuilder.loadTexts:coiCpriControllerTable.setStatus(_A)
_CoiCpriControllerEntry_Object=MibTableRow
coiCpriControllerEntry=_CoiCpriControllerEntry_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1))
coiCpriControllerEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:coiCpriControllerEntry.setStatus(_A)
class _CoiCpriControllerSupportedRateList_Type(Bits):namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9),(_Q,10)))
_CoiCpriControllerSupportedRateList_Type.__name__=_D
_CoiCpriControllerSupportedRateList_Object=MibTableColumn
coiCpriControllerSupportedRateList=_CoiCpriControllerSupportedRateList_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,1),_CoiCpriControllerSupportedRateList_Type())
coiCpriControllerSupportedRateList.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriControllerSupportedRateList.setStatus(_A)
class _CoiCpriControllerConfiguredRateList_Type(Bits):namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9),(_Q,10)))
_CoiCpriControllerConfiguredRateList_Type.__name__=_D
_CoiCpriControllerConfiguredRateList_Object=MibTableColumn
coiCpriControllerConfiguredRateList=_CoiCpriControllerConfiguredRateList_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,2),_CoiCpriControllerConfiguredRateList_Type())
coiCpriControllerConfiguredRateList.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriControllerConfiguredRateList.setStatus(_A)
class _CoiCpriControllerNegotiatedRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('rateNone',0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10),(_Q,11)))
_CoiCpriControllerNegotiatedRate_Type.__name__=_C
_CoiCpriControllerNegotiatedRate_Object=MibTableColumn
coiCpriControllerNegotiatedRate=_CoiCpriControllerNegotiatedRate_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,3),_CoiCpriControllerNegotiatedRate_Type())
coiCpriControllerNegotiatedRate.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriControllerNegotiatedRate.setStatus(_A)
class _CoiCpriControllerPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('slave',0),('master',1)))
_CoiCpriControllerPortRole_Type.__name__=_C
_CoiCpriControllerPortRole_Object=MibTableColumn
coiCpriControllerPortRole=_CoiCpriControllerPortRole_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,4),_CoiCpriControllerPortRole_Type())
coiCpriControllerPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriControllerPortRole.setStatus(_A)
_CoiCpriControllerL1StartupTimer_Type=Unsigned32
_CoiCpriControllerL1StartupTimer_Object=MibTableColumn
coiCpriControllerL1StartupTimer=_CoiCpriControllerL1StartupTimer_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,5),_CoiCpriControllerL1StartupTimer_Type())
coiCpriControllerL1StartupTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriControllerL1StartupTimer.setStatus(_A)
class _CoiCpriControllerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_CoiCpriControllerAdminStatus_Type.__name__=_C
_CoiCpriControllerAdminStatus_Object=MibTableColumn
coiCpriControllerAdminStatus=_CoiCpriControllerAdminStatus_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,6),_CoiCpriControllerAdminStatus_Type())
coiCpriControllerAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriControllerAdminStatus.setStatus(_A)
class _CoiCpriControllerOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_CoiCpriControllerOperStatus_Type.__name__=_C
_CoiCpriControllerOperStatus_Object=MibTableColumn
coiCpriControllerOperStatus=_CoiCpriControllerOperStatus_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,7),_CoiCpriControllerOperStatus_Type())
coiCpriControllerOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriControllerOperStatus.setStatus(_A)
class _CoiCpriControllerLoopbackInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('loopbackNone',0),('loopbackLine',1),('loopbackInternal',2)))
_CoiCpriControllerLoopbackInfo_Type.__name__=_C
_CoiCpriControllerLoopbackInfo_Object=MibTableColumn
coiCpriControllerLoopbackInfo=_CoiCpriControllerLoopbackInfo_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,8),_CoiCpriControllerLoopbackInfo_Type())
coiCpriControllerLoopbackInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriControllerLoopbackInfo.setStatus(_A)
class _CoiCpriControllerAlarmStatus_Type(Bits):namedValues=NamedValues(*(('noAlarm',0),('los',1),('lof',2),('rai',3),('sdi',4)))
_CoiCpriControllerAlarmStatus_Type.__name__=_D
_CoiCpriControllerAlarmStatus_Object=MibTableColumn
coiCpriControllerAlarmStatus=_CoiCpriControllerAlarmStatus_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,9),_CoiCpriControllerAlarmStatus_Type())
coiCpriControllerAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriControllerAlarmStatus.setStatus(_A)
_CoiCpriRoeStats_ObjectIdentity=ObjectIdentity
coiCpriRoeStats=_CoiCpriRoeStats_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1,2))
_CoiCpriRoeStatsTable_ObjectIdentity=ObjectIdentity
coiCpriRoeStatsTable=_CoiCpriRoeStatsTable_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1,2,1))
_CoiCpriRoeStatsEntry_Object=MibTableRow
coiCpriRoeStatsEntry=_CoiCpriRoeStatsEntry_Object((1,3,6,1,4,1,9,9,9999,1,2,1,1))
coiCpriRoeStatsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:coiCpriRoeStatsEntry.setStatus(_A)
_CoiCpriRoeRxFrames_Type=Counter64
_CoiCpriRoeRxFrames_Object=MibTableColumn
coiCpriRoeRxFrames=_CoiCpriRoeRxFrames_Object((1,3,6,1,4,1,9,9,9999,1,2,1,1,1),_CoiCpriRoeRxFrames_Type())
coiCpriRoeRxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriRoeRxFrames.setStatus(_A)
_CoiCpriRoeDroppedFramesDetected_Type=Counter64
_CoiCpriRoeDroppedFramesDetected_Object=MibTableColumn
coiCpriRoeDroppedFramesDetected=_CoiCpriRoeDroppedFramesDetected_Object((1,3,6,1,4,1,9,9,9999,1,2,1,1,2),_CoiCpriRoeDroppedFramesDetected_Type())
coiCpriRoeDroppedFramesDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriRoeDroppedFramesDetected.setStatus(_A)
_CoiCpriRoeStrayFramesDetected_Type=Counter64
_CoiCpriRoeStrayFramesDetected_Object=MibTableColumn
coiCpriRoeStrayFramesDetected=_CoiCpriRoeStrayFramesDetected_Object((1,3,6,1,4,1,9,9,9999,1,2,1,1,3),_CoiCpriRoeStrayFramesDetected_Type())
coiCpriRoeStrayFramesDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriRoeStrayFramesDetected.setStatus(_A)
_CoiCpriRoeDuplicateFramesDetected_Type=Counter64
_CoiCpriRoeDuplicateFramesDetected_Object=MibTableColumn
coiCpriRoeDuplicateFramesDetected=_CoiCpriRoeDuplicateFramesDetected_Object((1,3,6,1,4,1,9,9,9999,1,2,1,1,4),_CoiCpriRoeDuplicateFramesDetected_Type())
coiCpriRoeDuplicateFramesDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriRoeDuplicateFramesDetected.setStatus(_A)
_CoiCpriRoeOutOfSeqFramesDetected_Type=Counter64
_CoiCpriRoeOutOfSeqFramesDetected_Object=MibTableColumn
coiCpriRoeOutOfSeqFramesDetected=_CoiCpriRoeOutOfSeqFramesDetected_Object((1,3,6,1,4,1,9,9,9999,1,2,1,1,5),_CoiCpriRoeOutOfSeqFramesDetected_Type())
coiCpriRoeOutOfSeqFramesDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriRoeOutOfSeqFramesDetected.setStatus(_A)
_CoiCpriRoeOutOfSeqFramesDropped_Type=Counter64
_CoiCpriRoeOutOfSeqFramesDropped_Object=MibTableColumn
coiCpriRoeOutOfSeqFramesDropped=_CoiCpriRoeOutOfSeqFramesDropped_Object((1,3,6,1,4,1,9,9,9999,1,2,1,1,6),_CoiCpriRoeOutOfSeqFramesDropped_Type())
coiCpriRoeOutOfSeqFramesDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriRoeOutOfSeqFramesDropped.setStatus(_A)
_CoiCpriRoeTxFrames_Type=Counter64
_CoiCpriRoeTxFrames_Object=MibTableColumn
coiCpriRoeTxFrames=_CoiCpriRoeTxFrames_Object((1,3,6,1,4,1,9,9,9999,1,2,1,1,7),_CoiCpriRoeTxFrames_Type())
coiCpriRoeTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriRoeTxFrames.setStatus(_A)
_CoiCpriRoeIdleFramesSent_Type=Counter64
_CoiCpriRoeIdleFramesSent_Object=MibTableColumn
coiCpriRoeIdleFramesSent=_CoiCpriRoeIdleFramesSent_Object((1,3,6,1,4,1,9,9,9999,1,2,1,1,8),_CoiCpriRoeIdleFramesSent_Type())
coiCpriRoeIdleFramesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriRoeIdleFramesSent.setStatus(_A)
_CoiCpriRoePktDelayVarMinVal_Type=Counter64
_CoiCpriRoePktDelayVarMinVal_Object=MibTableColumn
coiCpriRoePktDelayVarMinVal=_CoiCpriRoePktDelayVarMinVal_Object((1,3,6,1,4,1,9,9,9999,1,2,1,1,9),_CoiCpriRoePktDelayVarMinVal_Type())
coiCpriRoePktDelayVarMinVal.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriRoePktDelayVarMinVal.setStatus(_A)
_CoiCpriRoePktDelayVarMaxVal_Type=Counter64
_CoiCpriRoePktDelayVarMaxVal_Object=MibTableColumn
coiCpriRoePktDelayVarMaxVal=_CoiCpriRoePktDelayVarMaxVal_Object((1,3,6,1,4,1,9,9,9999,1,2,1,1,10),_CoiCpriRoePktDelayVarMaxVal_Type())
coiCpriRoePktDelayVarMaxVal.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriRoePktDelayVarMaxVal.setStatus(_A)
_CoiCpriRoePktDelayVarAvgVal_Type=Counter64
_CoiCpriRoePktDelayVarAvgVal_Object=MibTableColumn
coiCpriRoePktDelayVarAvgVal=_CoiCpriRoePktDelayVarAvgVal_Object((1,3,6,1,4,1,9,9,9999,1,2,1,1,11),_CoiCpriRoePktDelayVarAvgVal_Type())
coiCpriRoePktDelayVarAvgVal.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriRoePktDelayVarAvgVal.setStatus(_A)
_CoiCpriRoeLineCodeViolationDetected_Type=Counter64
_CoiCpriRoeLineCodeViolationDetected_Object=MibTableColumn
coiCpriRoeLineCodeViolationDetected=_CoiCpriRoeLineCodeViolationDetected_Object((1,3,6,1,4,1,9,9,9999,1,2,1,1,12),_CoiCpriRoeLineCodeViolationDetected_Type())
coiCpriRoeLineCodeViolationDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriRoeLineCodeViolationDetected.setStatus(_A)
_CoiCpriRoeLineCodeViolationPropagated_Type=Counter64
_CoiCpriRoeLineCodeViolationPropagated_Object=MibTableColumn
coiCpriRoeLineCodeViolationPropagated=_CoiCpriRoeLineCodeViolationPropagated_Object((1,3,6,1,4,1,9,9,9999,1,2,1,1,13),_CoiCpriRoeLineCodeViolationPropagated_Type())
coiCpriRoeLineCodeViolationPropagated.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriRoeLineCodeViolationPropagated.setStatus(_A)
_CoiCpriRoeErroredLengthFrames_Type=Counter64
_CoiCpriRoeErroredLengthFrames_Object=MibTableColumn
coiCpriRoeErroredLengthFrames=_CoiCpriRoeErroredLengthFrames_Object((1,3,6,1,4,1,9,9,9999,1,2,1,1,14),_CoiCpriRoeErroredLengthFrames_Type())
coiCpriRoeErroredLengthFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:coiCpriRoeErroredLengthFrames.setStatus(_A)
_CiscoCpriMIBConformance_ObjectIdentity=ObjectIdentity
ciscoCpriMIBConformance=_CiscoCpriMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,9999,2))
_CiscoCpriMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCpriMIBCompliances=_CiscoCpriMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,9999,2,1))
_CiscoCpriMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCpriMIBGroups=_CiscoCpriMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,9999,2,2))
mibBuilder.exportSymbols('CISCO-CPRI-MIB',**{'ciscoCpriMIB':ciscoCpriMIB,'ciscoCpriMIBNotifs':ciscoCpriMIBNotifs,'ciscoCpriMIBObjects':ciscoCpriMIBObjects,'coiCpriController':coiCpriController,'coiCpriControllerTable':coiCpriControllerTable,'coiCpriControllerEntry':coiCpriControllerEntry,'coiCpriControllerSupportedRateList':coiCpriControllerSupportedRateList,'coiCpriControllerConfiguredRateList':coiCpriControllerConfiguredRateList,'coiCpriControllerNegotiatedRate':coiCpriControllerNegotiatedRate,'coiCpriControllerPortRole':coiCpriControllerPortRole,'coiCpriControllerL1StartupTimer':coiCpriControllerL1StartupTimer,'coiCpriControllerAdminStatus':coiCpriControllerAdminStatus,'coiCpriControllerOperStatus':coiCpriControllerOperStatus,'coiCpriControllerLoopbackInfo':coiCpriControllerLoopbackInfo,'coiCpriControllerAlarmStatus':coiCpriControllerAlarmStatus,'coiCpriRoeStats':coiCpriRoeStats,'coiCpriRoeStatsTable':coiCpriRoeStatsTable,'coiCpriRoeStatsEntry':coiCpriRoeStatsEntry,'coiCpriRoeRxFrames':coiCpriRoeRxFrames,'coiCpriRoeDroppedFramesDetected':coiCpriRoeDroppedFramesDetected,'coiCpriRoeStrayFramesDetected':coiCpriRoeStrayFramesDetected,'coiCpriRoeDuplicateFramesDetected':coiCpriRoeDuplicateFramesDetected,'coiCpriRoeOutOfSeqFramesDetected':coiCpriRoeOutOfSeqFramesDetected,'coiCpriRoeOutOfSeqFramesDropped':coiCpriRoeOutOfSeqFramesDropped,'coiCpriRoeTxFrames':coiCpriRoeTxFrames,'coiCpriRoeIdleFramesSent':coiCpriRoeIdleFramesSent,'coiCpriRoePktDelayVarMinVal':coiCpriRoePktDelayVarMinVal,'coiCpriRoePktDelayVarMaxVal':coiCpriRoePktDelayVarMaxVal,'coiCpriRoePktDelayVarAvgVal':coiCpriRoePktDelayVarAvgVal,'coiCpriRoeLineCodeViolationDetected':coiCpriRoeLineCodeViolationDetected,'coiCpriRoeLineCodeViolationPropagated':coiCpriRoeLineCodeViolationPropagated,'coiCpriRoeErroredLengthFrames':coiCpriRoeErroredLengthFrames,'ciscoCpriMIBConformance':ciscoCpriMIBConformance,'ciscoCpriMIBCompliances':ciscoCpriMIBCompliances,'ciscoCpriMIBGroups':ciscoCpriMIBGroups})