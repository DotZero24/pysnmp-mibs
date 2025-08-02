_X='wfCSMACDAutoNegConnector'
_W='wfCSMACDAutoNegSlot'
_V='gigabitduplexflowctrl'
_U='gigabitduplex'
_T='hundredbasetxduplexcongctrl'
_S='tenbasetduplexcongctrl'
_R='hundredbaset4'
_Q='hundredbasetxduplex'
_P='hundredbasetx'
_O='tenbasetduplex'
_N='tenbaset'
_M='delete'
_L='create'
_K='wfCSMACDConnector'
_J='wfCSMACDSlot'
_I='enabled'
_H='disable'
_G='enable'
_F='disabled'
_E='Wellfleet-CSMACD-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
wfCSMACDAutoNegGroup,wfLine=mibBuilder.importSymbols('Wellfleet-COMMON-MIB','wfCSMACDAutoNegGroup','wfLine')
_WfCSMACDTable_Object=MibTable
wfCSMACDTable=_WfCSMACDTable_Object((1,3,6,1,4,1,18,3,4,1))
if mibBuilder.loadTexts:wfCSMACDTable.setStatus(_A)
_WfCSMACDEntry_Object=MibTableRow
wfCSMACDEntry=_WfCSMACDEntry_Object((1,3,6,1,4,1,18,3,4,1,1))
wfCSMACDEntry.setIndexNames((0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:wfCSMACDEntry.setStatus(_A)
class _WfCSMACDDelete_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WfCSMACDDelete_Type.__name__=_C
_WfCSMACDDelete_Object=MibTableColumn
wfCSMACDDelete=_WfCSMACDDelete_Object((1,3,6,1,4,1,18,3,4,1,1,1),_WfCSMACDDelete_Type())
wfCSMACDDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDDelete.setStatus(_A)
class _WfCSMACDEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WfCSMACDEnable_Type.__name__=_C
_WfCSMACDEnable_Object=MibTableColumn
wfCSMACDEnable=_WfCSMACDEnable_Object((1,3,6,1,4,1,18,3,4,1,1,2),_WfCSMACDEnable_Type())
wfCSMACDEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDEnable.setStatus(_A)
class _WfCSMACDState_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('init',3),('notpresent',4)))
_WfCSMACDState_Type.__name__=_C
_WfCSMACDState_Object=MibTableColumn
wfCSMACDState=_WfCSMACDState_Object((1,3,6,1,4,1,18,3,4,1,1,3),_WfCSMACDState_Type())
wfCSMACDState.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDState.setStatus(_A)
class _WfCSMACDSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_WfCSMACDSlot_Type.__name__=_C
_WfCSMACDSlot_Object=MibTableColumn
wfCSMACDSlot=_WfCSMACDSlot_Object((1,3,6,1,4,1,18,3,4,1,1,4),_WfCSMACDSlot_Type())
wfCSMACDSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDSlot.setStatus(_A)
class _WfCSMACDConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,44))
_WfCSMACDConnector_Type.__name__=_C
_WfCSMACDConnector_Object=MibTableColumn
wfCSMACDConnector=_WfCSMACDConnector_Object((1,3,6,1,4,1,18,3,4,1,1,5),_WfCSMACDConnector_Type())
wfCSMACDConnector.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDConnector.setStatus(_A)
class _WfCSMACDCct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_WfCSMACDCct_Type.__name__=_C
_WfCSMACDCct_Object=MibTableColumn
wfCSMACDCct=_WfCSMACDCct_Object((1,3,6,1,4,1,18,3,4,1,1,6),_WfCSMACDCct_Type())
wfCSMACDCct.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDCct.setStatus(_A)
class _WfCSMACDBofl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WfCSMACDBofl_Type.__name__=_C
_WfCSMACDBofl_Object=MibTableColumn
wfCSMACDBofl=_WfCSMACDBofl_Object((1,3,6,1,4,1,18,3,4,1,1,7),_WfCSMACDBofl_Type())
wfCSMACDBofl.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDBofl.setStatus(_A)
class _WfCSMACDBoflTmo_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_WfCSMACDBoflTmo_Type.__name__=_C
_WfCSMACDBoflTmo_Object=MibTableColumn
wfCSMACDBoflTmo=_WfCSMACDBoflTmo_Object((1,3,6,1,4,1,18,3,4,1,1,8),_WfCSMACDBoflTmo_Type())
wfCSMACDBoflTmo.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDBoflTmo.setStatus(_A)
class _WfCSMACDMtu_Type(Integer32):defaultValue=1518;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1518));namedValues=NamedValues(('default',1518))
_WfCSMACDMtu_Type.__name__=_C
_WfCSMACDMtu_Object=MibTableColumn
wfCSMACDMtu=_WfCSMACDMtu_Object((1,3,6,1,4,1,18,3,4,1,1,9),_WfCSMACDMtu_Type())
wfCSMACDMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDMtu.setStatus(_A)
_WfCSMACDMadr_Type=OctetString
_WfCSMACDMadr_Object=MibTableColumn
wfCSMACDMadr=_WfCSMACDMadr_Object((1,3,6,1,4,1,18,3,4,1,1,10),_WfCSMACDMadr_Type())
wfCSMACDMadr.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDMadr.setStatus(_A)
_WfCSMACDOctetsRxOk_Type=Counter32
_WfCSMACDOctetsRxOk_Object=MibTableColumn
wfCSMACDOctetsRxOk=_WfCSMACDOctetsRxOk_Object((1,3,6,1,4,1,18,3,4,1,1,11),_WfCSMACDOctetsRxOk_Type())
wfCSMACDOctetsRxOk.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDOctetsRxOk.setStatus(_A)
_WfCSMACDFramesRxOk_Type=Counter32
_WfCSMACDFramesRxOk_Object=MibTableColumn
wfCSMACDFramesRxOk=_WfCSMACDFramesRxOk_Object((1,3,6,1,4,1,18,3,4,1,1,12),_WfCSMACDFramesRxOk_Type())
wfCSMACDFramesRxOk.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDFramesRxOk.setStatus(_A)
_WfCSMACDOctetsTxOk_Type=Counter32
_WfCSMACDOctetsTxOk_Object=MibTableColumn
wfCSMACDOctetsTxOk=_WfCSMACDOctetsTxOk_Object((1,3,6,1,4,1,18,3,4,1,1,13),_WfCSMACDOctetsTxOk_Type())
wfCSMACDOctetsTxOk.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDOctetsTxOk.setStatus(_A)
_WfCSMACDFramesTxOk_Type=Counter32
_WfCSMACDFramesTxOk_Object=MibTableColumn
wfCSMACDFramesTxOk=_WfCSMACDFramesTxOk_Object((1,3,6,1,4,1,18,3,4,1,1,14),_WfCSMACDFramesTxOk_Type())
wfCSMACDFramesTxOk.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDFramesTxOk.setStatus(_A)
_WfCSMACDDeferredTx_Type=Counter32
_WfCSMACDDeferredTx_Object=MibTableColumn
wfCSMACDDeferredTx=_WfCSMACDDeferredTx_Object((1,3,6,1,4,1,18,3,4,1,1,15),_WfCSMACDDeferredTx_Type())
wfCSMACDDeferredTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDDeferredTx.setStatus(_A)
_WfCSMACDLateCollnTx_Type=Counter32
_WfCSMACDLateCollnTx_Object=MibTableColumn
wfCSMACDLateCollnTx=_WfCSMACDLateCollnTx_Object((1,3,6,1,4,1,18,3,4,1,1,16),_WfCSMACDLateCollnTx_Type())
wfCSMACDLateCollnTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDLateCollnTx.setStatus(_A)
_WfCSMACDExcessvCollnTx_Type=Counter32
_WfCSMACDExcessvCollnTx_Object=MibTableColumn
wfCSMACDExcessvCollnTx=_WfCSMACDExcessvCollnTx_Object((1,3,6,1,4,1,18,3,4,1,1,17),_WfCSMACDExcessvCollnTx_Type())
wfCSMACDExcessvCollnTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDExcessvCollnTx.setStatus(_A)
_WfCSMACDBablErrorTx_Type=Counter32
_WfCSMACDBablErrorTx_Object=MibTableColumn
wfCSMACDBablErrorTx=_WfCSMACDBablErrorTx_Object((1,3,6,1,4,1,18,3,4,1,1,18),_WfCSMACDBablErrorTx_Type())
wfCSMACDBablErrorTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDBablErrorTx.setStatus(_A)
_WfCSMACDBufErrorTx_Type=Counter32
_WfCSMACDBufErrorTx_Object=MibTableColumn
wfCSMACDBufErrorTx=_WfCSMACDBufErrorTx_Object((1,3,6,1,4,1,18,3,4,1,1,19),_WfCSMACDBufErrorTx_Type())
wfCSMACDBufErrorTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDBufErrorTx.setStatus(_A)
_WfCSMACDLcarTx_Type=Counter32
_WfCSMACDLcarTx_Object=MibTableColumn
wfCSMACDLcarTx=_WfCSMACDLcarTx_Object((1,3,6,1,4,1,18,3,4,1,1,20),_WfCSMACDLcarTx_Type())
wfCSMACDLcarTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDLcarTx.setStatus(_A)
_WfCSMACDUfloTx_Type=Counter32
_WfCSMACDUfloTx_Object=MibTableColumn
wfCSMACDUfloTx=_WfCSMACDUfloTx_Object((1,3,6,1,4,1,18,3,4,1,1,21),_WfCSMACDUfloTx_Type())
wfCSMACDUfloTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDUfloTx.setStatus(_A)
_WfCSMACDFcsErrorRx_Type=Counter32
_WfCSMACDFcsErrorRx_Object=MibTableColumn
wfCSMACDFcsErrorRx=_WfCSMACDFcsErrorRx_Object((1,3,6,1,4,1,18,3,4,1,1,22),_WfCSMACDFcsErrorRx_Type())
wfCSMACDFcsErrorRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDFcsErrorRx.setStatus(_A)
_WfCSMACDAlignErrorRx_Type=Counter32
_WfCSMACDAlignErrorRx_Object=MibTableColumn
wfCSMACDAlignErrorRx=_WfCSMACDAlignErrorRx_Object((1,3,6,1,4,1,18,3,4,1,1,23),_WfCSMACDAlignErrorRx_Type())
wfCSMACDAlignErrorRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDAlignErrorRx.setStatus(_A)
_WfCSMACDLackRescErrorRx_Type=Counter32
_WfCSMACDLackRescErrorRx_Object=MibTableColumn
wfCSMACDLackRescErrorRx=_WfCSMACDLackRescErrorRx_Object((1,3,6,1,4,1,18,3,4,1,1,24),_WfCSMACDLackRescErrorRx_Type())
wfCSMACDLackRescErrorRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDLackRescErrorRx.setStatus(_A)
_WfCSMACDTooLongErrorRx_Type=Counter32
_WfCSMACDTooLongErrorRx_Object=MibTableColumn
wfCSMACDTooLongErrorRx=_WfCSMACDTooLongErrorRx_Object((1,3,6,1,4,1,18,3,4,1,1,25),_WfCSMACDTooLongErrorRx_Type())
wfCSMACDTooLongErrorRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDTooLongErrorRx.setStatus(_A)
_WfCSMACDOfloRx_Type=Counter32
_WfCSMACDOfloRx_Object=MibTableColumn
wfCSMACDOfloRx=_WfCSMACDOfloRx_Object((1,3,6,1,4,1,18,3,4,1,1,26),_WfCSMACDOfloRx_Type())
wfCSMACDOfloRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDOfloRx.setStatus(_A)
_WfCSMACDMerr_Type=Counter32
_WfCSMACDMerr_Object=MibTableColumn
wfCSMACDMerr=_WfCSMACDMerr_Object((1,3,6,1,4,1,18,3,4,1,1,27),_WfCSMACDMerr_Type())
wfCSMACDMerr.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDMerr.setStatus(_A)
_WfCSMACDCerr_Type=Counter32
_WfCSMACDCerr_Object=MibTableColumn
wfCSMACDCerr=_WfCSMACDCerr_Object((1,3,6,1,4,1,18,3,4,1,1,28),_WfCSMACDCerr_Type())
wfCSMACDCerr.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDCerr.setStatus(_A)
class _WfCSMACDHardwareFilter_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WfCSMACDHardwareFilter_Type.__name__=_C
_WfCSMACDHardwareFilter_Object=MibTableColumn
wfCSMACDHardwareFilter=_WfCSMACDHardwareFilter_Object((1,3,6,1,4,1,18,3,4,1,1,29),_WfCSMACDHardwareFilter_Type())
wfCSMACDHardwareFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDHardwareFilter.setStatus(_A)
_WfCSMACDTxQueueLength_Type=Integer32
_WfCSMACDTxQueueLength_Object=MibTableColumn
wfCSMACDTxQueueLength=_WfCSMACDTxQueueLength_Object((1,3,6,1,4,1,18,3,4,1,1,30),_WfCSMACDTxQueueLength_Type())
wfCSMACDTxQueueLength.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDTxQueueLength.setStatus(_A)
_WfCSMACDRxQueueLength_Type=Integer32
_WfCSMACDRxQueueLength_Object=MibTableColumn
wfCSMACDRxQueueLength=_WfCSMACDRxQueueLength_Object((1,3,6,1,4,1,18,3,4,1,1,31),_WfCSMACDRxQueueLength_Type())
wfCSMACDRxQueueLength.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDRxQueueLength.setStatus(_A)
_WfCSMACDTxClipFrames_Type=Counter32
_WfCSMACDTxClipFrames_Object=MibTableColumn
wfCSMACDTxClipFrames=_WfCSMACDTxClipFrames_Object((1,3,6,1,4,1,18,3,4,1,1,32),_WfCSMACDTxClipFrames_Type())
wfCSMACDTxClipFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDTxClipFrames.setStatus(_A)
_WfCSMACDRxReplenMisses_Type=Counter32
_WfCSMACDRxReplenMisses_Object=MibTableColumn
wfCSMACDRxReplenMisses=_WfCSMACDRxReplenMisses_Object((1,3,6,1,4,1,18,3,4,1,1,33),_WfCSMACDRxReplenMisses_Type())
wfCSMACDRxReplenMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDRxReplenMisses.setStatus(_A)
class _WfCSMACDCfgTxQueueLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WfCSMACDCfgTxQueueLength_Type.__name__=_C
_WfCSMACDCfgTxQueueLength_Object=MibTableColumn
wfCSMACDCfgTxQueueLength=_WfCSMACDCfgTxQueueLength_Object((1,3,6,1,4,1,18,3,4,1,1,34),_WfCSMACDCfgTxQueueLength_Type())
wfCSMACDCfgTxQueueLength.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDCfgTxQueueLength.setStatus(_A)
class _WfCSMACDCfgRxQueueLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WfCSMACDCfgRxQueueLength_Type.__name__=_C
_WfCSMACDCfgRxQueueLength_Object=MibTableColumn
wfCSMACDCfgRxQueueLength=_WfCSMACDCfgRxQueueLength_Object((1,3,6,1,4,1,18,3,4,1,1,35),_WfCSMACDCfgRxQueueLength_Type())
wfCSMACDCfgRxQueueLength.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDCfgRxQueueLength.setStatus(_A)
class _WfCSMACDAlignmentMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('bytes',2),(_F,3)))
_WfCSMACDAlignmentMode_Type.__name__=_C
_WfCSMACDAlignmentMode_Object=MibTableColumn
wfCSMACDAlignmentMode=_WfCSMACDAlignmentMode_Object((1,3,6,1,4,1,18,3,4,1,1,36),_WfCSMACDAlignmentMode_Type())
wfCSMACDAlignmentMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDAlignmentMode.setStatus(_A)
_WfCSMACDUnAlignedFrames_Type=Counter32
_WfCSMACDUnAlignedFrames_Object=MibTableColumn
wfCSMACDUnAlignedFrames=_WfCSMACDUnAlignedFrames_Object((1,3,6,1,4,1,18,3,4,1,1,37),_WfCSMACDUnAlignedFrames_Type())
wfCSMACDUnAlignedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDUnAlignedFrames.setStatus(_A)
_WfCSMACDLineNumber_Type=Integer32
_WfCSMACDLineNumber_Object=MibTableColumn
wfCSMACDLineNumber=_WfCSMACDLineNumber_Object((1,3,6,1,4,1,18,3,4,1,1,38),_WfCSMACDLineNumber_Type())
wfCSMACDLineNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDLineNumber.setStatus(_A)
_WfCSMACDLateCollnRx_Type=Counter32
_WfCSMACDLateCollnRx_Object=MibTableColumn
wfCSMACDLateCollnRx=_WfCSMACDLateCollnRx_Object((1,3,6,1,4,1,18,3,4,1,1,39),_WfCSMACDLateCollnRx_Type())
wfCSMACDLateCollnRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDLateCollnRx.setStatus(_A)
class _WfCSMACDModule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('one',1),('two',2),('three',3),('four',4)))
_WfCSMACDModule_Type.__name__=_C
_WfCSMACDModule_Object=MibTableColumn
wfCSMACDModule=_WfCSMACDModule_Object((1,3,6,1,4,1,18,3,4,1,1,40),_WfCSMACDModule_Type())
wfCSMACDModule.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDModule.setStatus(_A)
class _WfCSMACDActualConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('one',1),('two',2),('three',3),('four',4)))
_WfCSMACDActualConnector_Type.__name__=_C
_WfCSMACDActualConnector_Object=MibTableColumn
wfCSMACDActualConnector=_WfCSMACDActualConnector_Object((1,3,6,1,4,1,18,3,4,1,1,41),_WfCSMACDActualConnector_Type())
wfCSMACDActualConnector.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDActualConnector.setStatus(_A)
_WfCSMACDLastChange_Type=TimeTicks
_WfCSMACDLastChange_Object=MibTableColumn
wfCSMACDLastChange=_WfCSMACDLastChange_Object((1,3,6,1,4,1,18,3,4,1,1,42),_WfCSMACDLastChange_Type())
wfCSMACDLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDLastChange.setStatus(_A)
_WfCSMACDOutQLen_Type=Gauge32
_WfCSMACDOutQLen_Object=MibTableColumn
wfCSMACDOutQLen=_WfCSMACDOutQLen_Object((1,3,6,1,4,1,18,3,4,1,1,43),_WfCSMACDOutQLen_Type())
wfCSMACDOutQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDOutQLen.setStatus(_A)
_WfCSMACDIntProcessings_Type=Counter32
_WfCSMACDIntProcessings_Object=MibTableColumn
wfCSMACDIntProcessings=_WfCSMACDIntProcessings_Object((1,3,6,1,4,1,18,3,4,1,1,44),_WfCSMACDIntProcessings_Type())
wfCSMACDIntProcessings.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDIntProcessings.setStatus(_A)
_WfCSMACDTxProcessings_Type=Counter32
_WfCSMACDTxProcessings_Object=MibTableColumn
wfCSMACDTxProcessings=_WfCSMACDTxProcessings_Object((1,3,6,1,4,1,18,3,4,1,1,45),_WfCSMACDTxProcessings_Type())
wfCSMACDTxProcessings.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDTxProcessings.setStatus(_A)
_WfCSMACDRxProcessings_Type=Counter32
_WfCSMACDRxProcessings_Object=MibTableColumn
wfCSMACDRxProcessings=_WfCSMACDRxProcessings_Object((1,3,6,1,4,1,18,3,4,1,1,46),_WfCSMACDRxProcessings_Type())
wfCSMACDRxProcessings.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDRxProcessings.setStatus(_A)
_WfCSMACDTxCmplProcessings_Type=Counter32
_WfCSMACDTxCmplProcessings_Object=MibTableColumn
wfCSMACDTxCmplProcessings=_WfCSMACDTxCmplProcessings_Object((1,3,6,1,4,1,18,3,4,1,1,47),_WfCSMACDTxCmplProcessings_Type())
wfCSMACDTxCmplProcessings.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDTxCmplProcessings.setStatus(_A)
_WfCSMACDTxQueueReductions_Type=Counter32
_WfCSMACDTxQueueReductions_Object=MibTableColumn
wfCSMACDTxQueueReductions=_WfCSMACDTxQueueReductions_Object((1,3,6,1,4,1,18,3,4,1,1,48),_WfCSMACDTxQueueReductions_Type())
wfCSMACDTxQueueReductions.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDTxQueueReductions.setStatus(_A)
_WfCSMACDSingleCollisionFrames_Type=Counter32
_WfCSMACDSingleCollisionFrames_Object=MibTableColumn
wfCSMACDSingleCollisionFrames=_WfCSMACDSingleCollisionFrames_Object((1,3,6,1,4,1,18,3,4,1,1,49),_WfCSMACDSingleCollisionFrames_Type())
wfCSMACDSingleCollisionFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDSingleCollisionFrames.setStatus(_A)
_WfCSMACDMultipleCollisionFrames_Type=Counter32
_WfCSMACDMultipleCollisionFrames_Object=MibTableColumn
wfCSMACDMultipleCollisionFrames=_WfCSMACDMultipleCollisionFrames_Object((1,3,6,1,4,1,18,3,4,1,1,50),_WfCSMACDMultipleCollisionFrames_Type())
wfCSMACDMultipleCollisionFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDMultipleCollisionFrames.setStatus(_A)
_WfCSMACDInternalMacTxErrors_Type=Counter32
_WfCSMACDInternalMacTxErrors_Object=MibTableColumn
wfCSMACDInternalMacTxErrors=_WfCSMACDInternalMacTxErrors_Object((1,3,6,1,4,1,18,3,4,1,1,51),_WfCSMACDInternalMacTxErrors_Type())
wfCSMACDInternalMacTxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDInternalMacTxErrors.setStatus(_A)
class _WfCSMACDLineCapability_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),(_T,7),(_U,8),(_V,9)))
_WfCSMACDLineCapability_Type.__name__=_C
_WfCSMACDLineCapability_Object=MibTableColumn
wfCSMACDLineCapability=_WfCSMACDLineCapability_Object((1,3,6,1,4,1,18,3,4,1,1,52),_WfCSMACDLineCapability_Type())
wfCSMACDLineCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDLineCapability.setStatus(_A)
_WfCSMACDEtherChipSet_Type=ObjectIdentifier
_WfCSMACDEtherChipSet_Object=MibTableColumn
wfCSMACDEtherChipSet=_WfCSMACDEtherChipSet_Object((1,3,6,1,4,1,18,3,4,1,1,53),_WfCSMACDEtherChipSet_Type())
wfCSMACDEtherChipSet.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDEtherChipSet.setStatus(_A)
_WfCSMACDRxSymbolErrors_Type=Counter32
_WfCSMACDRxSymbolErrors_Object=MibTableColumn
wfCSMACDRxSymbolErrors=_WfCSMACDRxSymbolErrors_Object((1,3,6,1,4,1,18,3,4,1,1,54),_WfCSMACDRxSymbolErrors_Type())
wfCSMACDRxSymbolErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDRxSymbolErrors.setStatus(_A)
_WfCSMACDInternalMacRxErrors_Type=Counter32
_WfCSMACDInternalMacRxErrors_Object=MibTableColumn
wfCSMACDInternalMacRxErrors=_WfCSMACDInternalMacRxErrors_Object((1,3,6,1,4,1,18,3,4,1,1,55),_WfCSMACDInternalMacRxErrors_Type())
wfCSMACDInternalMacRxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDInternalMacRxErrors.setStatus(_A)
class _WfCSMACDConfigurableSpeed_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_F,2)))
_WfCSMACDConfigurableSpeed_Type.__name__=_C
_WfCSMACDConfigurableSpeed_Object=MibTableColumn
wfCSMACDConfigurableSpeed=_WfCSMACDConfigurableSpeed_Object((1,3,6,1,4,1,18,3,4,1,1,56),_WfCSMACDConfigurableSpeed_Type())
wfCSMACDConfigurableSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDConfigurableSpeed.setStatus(_A)
_WfCSMACDRxFlushes_Type=Counter32
_WfCSMACDRxFlushes_Object=MibTableColumn
wfCSMACDRxFlushes=_WfCSMACDRxFlushes_Object((1,3,6,1,4,1,18,3,4,1,1,57),_WfCSMACDRxFlushes_Type())
wfCSMACDRxFlushes.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDRxFlushes.setStatus(_A)
_WfCSMACDTxDeadlocks_Type=Counter32
_WfCSMACDTxDeadlocks_Object=MibTableColumn
wfCSMACDTxDeadlocks=_WfCSMACDTxDeadlocks_Object((1,3,6,1,4,1,18,3,4,1,1,58),_WfCSMACDTxDeadlocks_Type())
wfCSMACDTxDeadlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDTxDeadlocks.setStatus(_A)
class _WfCSMACDBoflRetries_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_WfCSMACDBoflRetries_Type.__name__=_C
_WfCSMACDBoflRetries_Object=MibTableColumn
wfCSMACDBoflRetries=_WfCSMACDBoflRetries_Object((1,3,6,1,4,1,18,3,4,1,1,59),_WfCSMACDBoflRetries_Type())
wfCSMACDBoflRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDBoflRetries.setStatus(_A)
class _WfCSMACDBoflTmoDivisor_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WfCSMACDBoflTmoDivisor_Type.__name__=_C
_WfCSMACDBoflTmoDivisor_Object=MibTableColumn
wfCSMACDBoflTmoDivisor=_WfCSMACDBoflTmoDivisor_Object((1,3,6,1,4,1,18,3,4,1,1,60),_WfCSMACDBoflTmoDivisor_Type())
wfCSMACDBoflTmoDivisor.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDBoflTmoDivisor.setStatus(_A)
class _WfCSMACDTurboBoflDebug_Type(Integer32):defaultValue=0
_WfCSMACDTurboBoflDebug_Type.__name__=_C
_WfCSMACDTurboBoflDebug_Object=MibTableColumn
wfCSMACDTurboBoflDebug=_WfCSMACDTurboBoflDebug_Object((1,3,6,1,4,1,18,3,4,1,1,61),_WfCSMACDTurboBoflDebug_Type())
wfCSMACDTurboBoflDebug.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDTurboBoflDebug.setStatus(_A)
_WfCSMACDIfIndex_Type=Integer32
_WfCSMACDIfIndex_Object=MibTableColumn
wfCSMACDIfIndex=_WfCSMACDIfIndex_Object((1,3,6,1,4,1,18,3,4,1,1,62),_WfCSMACDIfIndex_Type())
wfCSMACDIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDIfIndex.setStatus(_A)
_WfCSMACDTxFlowControlPauseFrames_Type=Counter32
_WfCSMACDTxFlowControlPauseFrames_Object=MibTableColumn
wfCSMACDTxFlowControlPauseFrames=_WfCSMACDTxFlowControlPauseFrames_Object((1,3,6,1,4,1,18,3,4,1,1,63),_WfCSMACDTxFlowControlPauseFrames_Type())
wfCSMACDTxFlowControlPauseFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDTxFlowControlPauseFrames.setStatus(_A)
_WfCSMACDRxFlowControlPauseFrames_Type=Counter32
_WfCSMACDRxFlowControlPauseFrames_Object=MibTableColumn
wfCSMACDRxFlowControlPauseFrames=_WfCSMACDRxFlowControlPauseFrames_Object((1,3,6,1,4,1,18,3,4,1,1,64),_WfCSMACDRxFlowControlPauseFrames_Type())
wfCSMACDRxFlowControlPauseFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDRxFlowControlPauseFrames.setStatus(_A)
_WfCSMACDRxUnsupportedOpcodes_Type=Counter32
_WfCSMACDRxUnsupportedOpcodes_Object=MibTableColumn
wfCSMACDRxUnsupportedOpcodes=_WfCSMACDRxUnsupportedOpcodes_Object((1,3,6,1,4,1,18,3,4,1,1,65),_WfCSMACDRxUnsupportedOpcodes_Type())
wfCSMACDRxUnsupportedOpcodes.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDRxUnsupportedOpcodes.setStatus(_A)
class _WfCSMACDFlowControlEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_F,2)))
_WfCSMACDFlowControlEnable_Type.__name__=_C
_WfCSMACDFlowControlEnable_Object=MibTableColumn
wfCSMACDFlowControlEnable=_WfCSMACDFlowControlEnable_Object((1,3,6,1,4,1,18,3,4,1,1,66),_WfCSMACDFlowControlEnable_Type())
wfCSMACDFlowControlEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDFlowControlEnable.setStatus(_A)
class _WfCSMACDTxFlowControlPauseTime_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,65535))
_WfCSMACDTxFlowControlPauseTime_Type.__name__=_C
_WfCSMACDTxFlowControlPauseTime_Object=MibTableColumn
wfCSMACDTxFlowControlPauseTime=_WfCSMACDTxFlowControlPauseTime_Object((1,3,6,1,4,1,18,3,4,1,1,67),_WfCSMACDTxFlowControlPauseTime_Type())
wfCSMACDTxFlowControlPauseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDTxFlowControlPauseTime.setStatus(_A)
class _WfCSMACDTxFlowControlPauseZeroEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_F,2)))
_WfCSMACDTxFlowControlPauseZeroEnable_Type.__name__=_C
_WfCSMACDTxFlowControlPauseZeroEnable_Object=MibTableColumn
wfCSMACDTxFlowControlPauseZeroEnable=_WfCSMACDTxFlowControlPauseZeroEnable_Object((1,3,6,1,4,1,18,3,4,1,1,68),_WfCSMACDTxFlowControlPauseZeroEnable_Type())
wfCSMACDTxFlowControlPauseZeroEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDTxFlowControlPauseZeroEnable.setStatus(_A)
class _WfCSMACDDsqmsLineSpeed_Type(Integer32):defaultValue=1250000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000000))
_WfCSMACDDsqmsLineSpeed_Type.__name__=_C
_WfCSMACDDsqmsLineSpeed_Object=MibTableColumn
wfCSMACDDsqmsLineSpeed=_WfCSMACDDsqmsLineSpeed_Object((1,3,6,1,4,1,18,3,4,1,1,69),_WfCSMACDDsqmsLineSpeed_Type())
wfCSMACDDsqmsLineSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDDsqmsLineSpeed.setStatus(_A)
_WfCSMACDAutoNegTable_Object=MibTable
wfCSMACDAutoNegTable=_WfCSMACDAutoNegTable_Object((1,3,6,1,4,1,18,3,4,16,1))
if mibBuilder.loadTexts:wfCSMACDAutoNegTable.setStatus(_A)
_WfCSMACDAutoNegEntry_Object=MibTableRow
wfCSMACDAutoNegEntry=_WfCSMACDAutoNegEntry_Object((1,3,6,1,4,1,18,3,4,16,1,1))
wfCSMACDAutoNegEntry.setIndexNames((0,_E,_W),(0,_E,_X))
if mibBuilder.loadTexts:wfCSMACDAutoNegEntry.setStatus(_A)
class _WfCSMACDAutoNegDelete_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WfCSMACDAutoNegDelete_Type.__name__=_C
_WfCSMACDAutoNegDelete_Object=MibTableColumn
wfCSMACDAutoNegDelete=_WfCSMACDAutoNegDelete_Object((1,3,6,1,4,1,18,3,4,16,1,1,1),_WfCSMACDAutoNegDelete_Type())
wfCSMACDAutoNegDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDAutoNegDelete.setStatus(_A)
class _WfCSMACDAutoNegSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_WfCSMACDAutoNegSlot_Type.__name__=_C
_WfCSMACDAutoNegSlot_Object=MibTableColumn
wfCSMACDAutoNegSlot=_WfCSMACDAutoNegSlot_Object((1,3,6,1,4,1,18,3,4,16,1,1,2),_WfCSMACDAutoNegSlot_Type())
wfCSMACDAutoNegSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDAutoNegSlot.setStatus(_A)
class _WfCSMACDAutoNegConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,44))
_WfCSMACDAutoNegConnector_Type.__name__=_C
_WfCSMACDAutoNegConnector_Object=MibTableColumn
wfCSMACDAutoNegConnector=_WfCSMACDAutoNegConnector_Object((1,3,6,1,4,1,18,3,4,16,1,1,3),_WfCSMACDAutoNegConnector_Type())
wfCSMACDAutoNegConnector.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDAutoNegConnector.setStatus(_A)
class _WfCSMACDAutoNegSpeedSelect_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('nway',1),(_N,2),(_O,3),(_P,4),(_Q,5),(_R,6),('macloopback',7),('phyloopback',8),('twisterloopback',9),(_S,10),(_T,11),(_U,12),(_V,13)))
_WfCSMACDAutoNegSpeedSelect_Type.__name__=_C
_WfCSMACDAutoNegSpeedSelect_Object=MibTableColumn
wfCSMACDAutoNegSpeedSelect=_WfCSMACDAutoNegSpeedSelect_Object((1,3,6,1,4,1,18,3,4,16,1,1,4),_WfCSMACDAutoNegSpeedSelect_Type())
wfCSMACDAutoNegSpeedSelect.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDAutoNegSpeedSelect.setStatus(_A)
class _WfCSMACDAutoNegRemoteSignaling_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('detected',1),('notdetected',2)))
_WfCSMACDAutoNegRemoteSignaling_Type.__name__=_C
_WfCSMACDAutoNegRemoteSignaling_Object=MibTableColumn
wfCSMACDAutoNegRemoteSignaling=_WfCSMACDAutoNegRemoteSignaling_Object((1,3,6,1,4,1,18,3,4,16,1,1,5),_WfCSMACDAutoNegRemoteSignaling_Type())
wfCSMACDAutoNegRemoteSignaling.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDAutoNegRemoteSignaling.setStatus(_A)
class _WfCSMACDAutoNegState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('configuring',2),('complete',3),('paralleldetectfail',4)))
_WfCSMACDAutoNegState_Type.__name__=_C
_WfCSMACDAutoNegState_Object=MibTableColumn
wfCSMACDAutoNegState=_WfCSMACDAutoNegState_Object((1,3,6,1,4,1,18,3,4,16,1,1,6),_WfCSMACDAutoNegState_Type())
wfCSMACDAutoNegState.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDAutoNegState.setStatus(_A)
_WfCSMACDAutoNegRestartAutoConfig_Type=Integer32
_WfCSMACDAutoNegRestartAutoConfig_Object=MibTableColumn
wfCSMACDAutoNegRestartAutoConfig=_WfCSMACDAutoNegRestartAutoConfig_Object((1,3,6,1,4,1,18,3,4,16,1,1,7),_WfCSMACDAutoNegRestartAutoConfig_Type())
wfCSMACDAutoNegRestartAutoConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDAutoNegRestartAutoConfig.setStatus(_A)
_WfCSMACDAutoNegLocalCapability_Type=Gauge32
_WfCSMACDAutoNegLocalCapability_Object=MibTableColumn
wfCSMACDAutoNegLocalCapability=_WfCSMACDAutoNegLocalCapability_Object((1,3,6,1,4,1,18,3,4,16,1,1,8),_WfCSMACDAutoNegLocalCapability_Type())
wfCSMACDAutoNegLocalCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDAutoNegLocalCapability.setStatus(_A)
_WfCSMACDAutoNegAdvertisedCapability_Type=Gauge32
_WfCSMACDAutoNegAdvertisedCapability_Object=MibTableColumn
wfCSMACDAutoNegAdvertisedCapability=_WfCSMACDAutoNegAdvertisedCapability_Object((1,3,6,1,4,1,18,3,4,16,1,1,9),_WfCSMACDAutoNegAdvertisedCapability_Type())
wfCSMACDAutoNegAdvertisedCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:wfCSMACDAutoNegAdvertisedCapability.setStatus(_A)
_WfCSMACDAutoNegReceivedCapability_Type=Gauge32
_WfCSMACDAutoNegReceivedCapability_Object=MibTableColumn
wfCSMACDAutoNegReceivedCapability=_WfCSMACDAutoNegReceivedCapability_Object((1,3,6,1,4,1,18,3,4,16,1,1,10),_WfCSMACDAutoNegReceivedCapability_Type())
wfCSMACDAutoNegReceivedCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:wfCSMACDAutoNegReceivedCapability.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'wfCSMACDTable':wfCSMACDTable,'wfCSMACDEntry':wfCSMACDEntry,'wfCSMACDDelete':wfCSMACDDelete,'wfCSMACDEnable':wfCSMACDEnable,'wfCSMACDState':wfCSMACDState,_J:wfCSMACDSlot,_K:wfCSMACDConnector,'wfCSMACDCct':wfCSMACDCct,'wfCSMACDBofl':wfCSMACDBofl,'wfCSMACDBoflTmo':wfCSMACDBoflTmo,'wfCSMACDMtu':wfCSMACDMtu,'wfCSMACDMadr':wfCSMACDMadr,'wfCSMACDOctetsRxOk':wfCSMACDOctetsRxOk,'wfCSMACDFramesRxOk':wfCSMACDFramesRxOk,'wfCSMACDOctetsTxOk':wfCSMACDOctetsTxOk,'wfCSMACDFramesTxOk':wfCSMACDFramesTxOk,'wfCSMACDDeferredTx':wfCSMACDDeferredTx,'wfCSMACDLateCollnTx':wfCSMACDLateCollnTx,'wfCSMACDExcessvCollnTx':wfCSMACDExcessvCollnTx,'wfCSMACDBablErrorTx':wfCSMACDBablErrorTx,'wfCSMACDBufErrorTx':wfCSMACDBufErrorTx,'wfCSMACDLcarTx':wfCSMACDLcarTx,'wfCSMACDUfloTx':wfCSMACDUfloTx,'wfCSMACDFcsErrorRx':wfCSMACDFcsErrorRx,'wfCSMACDAlignErrorRx':wfCSMACDAlignErrorRx,'wfCSMACDLackRescErrorRx':wfCSMACDLackRescErrorRx,'wfCSMACDTooLongErrorRx':wfCSMACDTooLongErrorRx,'wfCSMACDOfloRx':wfCSMACDOfloRx,'wfCSMACDMerr':wfCSMACDMerr,'wfCSMACDCerr':wfCSMACDCerr,'wfCSMACDHardwareFilter':wfCSMACDHardwareFilter,'wfCSMACDTxQueueLength':wfCSMACDTxQueueLength,'wfCSMACDRxQueueLength':wfCSMACDRxQueueLength,'wfCSMACDTxClipFrames':wfCSMACDTxClipFrames,'wfCSMACDRxReplenMisses':wfCSMACDRxReplenMisses,'wfCSMACDCfgTxQueueLength':wfCSMACDCfgTxQueueLength,'wfCSMACDCfgRxQueueLength':wfCSMACDCfgRxQueueLength,'wfCSMACDAlignmentMode':wfCSMACDAlignmentMode,'wfCSMACDUnAlignedFrames':wfCSMACDUnAlignedFrames,'wfCSMACDLineNumber':wfCSMACDLineNumber,'wfCSMACDLateCollnRx':wfCSMACDLateCollnRx,'wfCSMACDModule':wfCSMACDModule,'wfCSMACDActualConnector':wfCSMACDActualConnector,'wfCSMACDLastChange':wfCSMACDLastChange,'wfCSMACDOutQLen':wfCSMACDOutQLen,'wfCSMACDIntProcessings':wfCSMACDIntProcessings,'wfCSMACDTxProcessings':wfCSMACDTxProcessings,'wfCSMACDRxProcessings':wfCSMACDRxProcessings,'wfCSMACDTxCmplProcessings':wfCSMACDTxCmplProcessings,'wfCSMACDTxQueueReductions':wfCSMACDTxQueueReductions,'wfCSMACDSingleCollisionFrames':wfCSMACDSingleCollisionFrames,'wfCSMACDMultipleCollisionFrames':wfCSMACDMultipleCollisionFrames,'wfCSMACDInternalMacTxErrors':wfCSMACDInternalMacTxErrors,'wfCSMACDLineCapability':wfCSMACDLineCapability,'wfCSMACDEtherChipSet':wfCSMACDEtherChipSet,'wfCSMACDRxSymbolErrors':wfCSMACDRxSymbolErrors,'wfCSMACDInternalMacRxErrors':wfCSMACDInternalMacRxErrors,'wfCSMACDConfigurableSpeed':wfCSMACDConfigurableSpeed,'wfCSMACDRxFlushes':wfCSMACDRxFlushes,'wfCSMACDTxDeadlocks':wfCSMACDTxDeadlocks,'wfCSMACDBoflRetries':wfCSMACDBoflRetries,'wfCSMACDBoflTmoDivisor':wfCSMACDBoflTmoDivisor,'wfCSMACDTurboBoflDebug':wfCSMACDTurboBoflDebug,'wfCSMACDIfIndex':wfCSMACDIfIndex,'wfCSMACDTxFlowControlPauseFrames':wfCSMACDTxFlowControlPauseFrames,'wfCSMACDRxFlowControlPauseFrames':wfCSMACDRxFlowControlPauseFrames,'wfCSMACDRxUnsupportedOpcodes':wfCSMACDRxUnsupportedOpcodes,'wfCSMACDFlowControlEnable':wfCSMACDFlowControlEnable,'wfCSMACDTxFlowControlPauseTime':wfCSMACDTxFlowControlPauseTime,'wfCSMACDTxFlowControlPauseZeroEnable':wfCSMACDTxFlowControlPauseZeroEnable,'wfCSMACDDsqmsLineSpeed':wfCSMACDDsqmsLineSpeed,'wfCSMACDAutoNegTable':wfCSMACDAutoNegTable,'wfCSMACDAutoNegEntry':wfCSMACDAutoNegEntry,'wfCSMACDAutoNegDelete':wfCSMACDAutoNegDelete,_W:wfCSMACDAutoNegSlot,_X:wfCSMACDAutoNegConnector,'wfCSMACDAutoNegSpeedSelect':wfCSMACDAutoNegSpeedSelect,'wfCSMACDAutoNegRemoteSignaling':wfCSMACDAutoNegRemoteSignaling,'wfCSMACDAutoNegState':wfCSMACDAutoNegState,'wfCSMACDAutoNegRestartAutoConfig':wfCSMACDAutoNegRestartAutoConfig,'wfCSMACDAutoNegLocalCapability':wfCSMACDAutoNegLocalCapability,'wfCSMACDAutoNegAdvertisedCapability':wfCSMACDAutoNegAdvertisedCapability,'wfCSMACDAutoNegReceivedCapability':wfCSMACDAutoNegReceivedCapability})