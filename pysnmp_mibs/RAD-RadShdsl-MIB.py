_j='hdsl2ShdslIfConfLinkDownReason'
_i='shdslSpanConfProfileEntry'
_h='shdslEndpointCurrEntry'
_g='hdsl2ShdslSideIdx'
_f='hdsl2ShdslIfConfIdx'
_e='disabled'
_d='enhanced'
_c='hdsl2ShdslInvIndex'
_b='hdsl2ShdslEndpointThreshSNRMargin'
_a='hdsl2ShdslEndpointThreshLoopAttenuation'
_Z='hdsl2ShdslEndpointThreshLOSWS'
_Y='hdsl2ShdslEndpointThreshCRCanomalies'
_X='hdsl2ShdslEndpointSide'
_W='hdsl2ShdslEndpointCurrSnrMgn'
_V='hdsl2ShdslEndpointCurrAtn'
_U='hdsl2ShdslEndpointCurr15MinLOSWS'
_T='hdsl2ShdslEndpointCurr15MinCRCanomalies'
_S='Bits'
_R='ifIndex'
_Q='dB'
_P='alarmEventReason'
_O='alarmEventLogSourceName'
_N='alarmEventLogSeverity'
_M='alarmEventLogDescription'
_L='alarmEventLogDateAndTime'
_K='alarmEventLogAlarmOrEventId'
_J='ifAlias'
_I='RAD-RadShdsl-MIB'
_H='notApplicable'
_G='IF-MIB'
_F='HDSL2-SHDSL-LINE-MIB'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='RAD-GEN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hdsl2ShdslEndpointCurr15MinCRCanomalies,hdsl2ShdslEndpointCurr15MinLOSWS,hdsl2ShdslEndpointCurrAtn,hdsl2ShdslEndpointCurrEntry,hdsl2ShdslEndpointCurrSnrMgn,hdsl2ShdslEndpointSide,hdsl2ShdslEndpointThreshCRCanomalies,hdsl2ShdslEndpointThreshLOSWS,hdsl2ShdslEndpointThreshLoopAttenuation,hdsl2ShdslEndpointThreshSNRMargin,hdsl2ShdslInvIndex,hdsl2ShdslSpanConfProfileEntry=mibBuilder.importSymbols(_F,_T,_U,_V,'hdsl2ShdslEndpointCurrEntry',_W,_X,_Y,_Z,_a,_b,_c,'hdsl2ShdslSpanConfProfileEntry')
ifAlias,ifIndex=mibBuilder.importSymbols(_G,_J,_R)
alarmEventLogAlarmOrEventId,alarmEventLogDateAndTime,alarmEventLogDescription,alarmEventLogSeverity,alarmEventLogSourceName,alarmEventReason=mibBuilder.importSymbols(_B,_K,_L,_M,_N,_O,_P)
diverseIfWanGen,=mibBuilder.importSymbols('RAD-SMI-MIB','diverseIfWanGen')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_S,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
shdslIf=ModuleIdentity((1,3,6,1,4,1,164,3,1,6,12))
_RadHdsl2ShdslEvents_ObjectIdentity=ObjectIdentity
radHdsl2ShdslEvents=_RadHdsl2ShdslEvents_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,12,0))
_ShdslEndpointCurrTable_Object=MibTable
shdslEndpointCurrTable=_ShdslEndpointCurrTable_Object((1,3,6,1,4,1,164,3,1,6,12,1))
if mibBuilder.loadTexts:shdslEndpointCurrTable.setStatus(_A)
_ShdslEndpointCurrEntry_Object=MibTableRow
shdslEndpointCurrEntry=_ShdslEndpointCurrEntry_Object((1,3,6,1,4,1,164,3,1,6,12,1,1))
if mibBuilder.loadTexts:shdslEndpointCurrEntry.setStatus(_A)
_Hdsl2ShdslEndpointCurrRcvGain_Type=Integer32
_Hdsl2ShdslEndpointCurrRcvGain_Object=MibTableColumn
hdsl2ShdslEndpointCurrRcvGain=_Hdsl2ShdslEndpointCurrRcvGain_Object((1,3,6,1,4,1,164,3,1,6,12,1,1,1),_Hdsl2ShdslEndpointCurrRcvGain_Type())
hdsl2ShdslEndpointCurrRcvGain.setMaxAccess(_E)
if mibBuilder.loadTexts:hdsl2ShdslEndpointCurrRcvGain.setStatus(_A)
if mibBuilder.loadTexts:hdsl2ShdslEndpointCurrRcvGain.setUnits(_Q)
_Hdsl2ShdslEndpointCurrTransPower_Type=Integer32
_Hdsl2ShdslEndpointCurrTransPower_Object=MibTableColumn
hdsl2ShdslEndpointCurrTransPower=_Hdsl2ShdslEndpointCurrTransPower_Object((1,3,6,1,4,1,164,3,1,6,12,1,1,2),_Hdsl2ShdslEndpointCurrTransPower_Type())
hdsl2ShdslEndpointCurrTransPower.setMaxAccess(_E)
if mibBuilder.loadTexts:hdsl2ShdslEndpointCurrTransPower.setStatus(_A)
_Hdsl2ShdslEndpointCurrPowerBO_Type=Integer32
_Hdsl2ShdslEndpointCurrPowerBO_Object=MibTableColumn
hdsl2ShdslEndpointCurrPowerBO=_Hdsl2ShdslEndpointCurrPowerBO_Object((1,3,6,1,4,1,164,3,1,6,12,1,1,3),_Hdsl2ShdslEndpointCurrPowerBO_Type())
hdsl2ShdslEndpointCurrPowerBO.setMaxAccess(_E)
if mibBuilder.loadTexts:hdsl2ShdslEndpointCurrPowerBO.setStatus(_A)
if mibBuilder.loadTexts:hdsl2ShdslEndpointCurrPowerBO.setUnits(_Q)
class _Hdsl2ShdslEndpointCurrLineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('noSync',2),('sync',3)))
_Hdsl2ShdslEndpointCurrLineStatus_Type.__name__=_C
_Hdsl2ShdslEndpointCurrLineStatus_Object=MibTableColumn
hdsl2ShdslEndpointCurrLineStatus=_Hdsl2ShdslEndpointCurrLineStatus_Object((1,3,6,1,4,1,164,3,1,6,12,1,1,4),_Hdsl2ShdslEndpointCurrLineStatus_Type())
hdsl2ShdslEndpointCurrLineStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hdsl2ShdslEndpointCurrLineStatus.setStatus(_A)
class _Hdsl2ShdslEndpointCurrOpState_Type(Bits):namedValues=NamedValues(*(('idleMode',0),('dataMode',1),('bootUpload',2),('bootUploadDone',3),('startupHandshakeInProgress',4),('startupTrainingInProgress',5),('framerSyncInProgress',6),('localAnalogLoopbackInProgress',7),('remoteCoreLoopbackInProgress',8),('localDigitalLoopbackInProgress',9),('spectrumTestInProgress',10)))
_Hdsl2ShdslEndpointCurrOpState_Type.__name__=_S
_Hdsl2ShdslEndpointCurrOpState_Object=MibTableColumn
hdsl2ShdslEndpointCurrOpState=_Hdsl2ShdslEndpointCurrOpState_Object((1,3,6,1,4,1,164,3,1,6,12,1,1,5),_Hdsl2ShdslEndpointCurrOpState_Type())
hdsl2ShdslEndpointCurrOpState.setMaxAccess(_E)
if mibBuilder.loadTexts:hdsl2ShdslEndpointCurrOpState.setStatus(_A)
_Hdsl2ShdslEndpointAccumulatedTimeElapsed_Type=TimeTicks
_Hdsl2ShdslEndpointAccumulatedTimeElapsed_Object=MibTableColumn
hdsl2ShdslEndpointAccumulatedTimeElapsed=_Hdsl2ShdslEndpointAccumulatedTimeElapsed_Object((1,3,6,1,4,1,164,3,1,6,12,1,1,6),_Hdsl2ShdslEndpointAccumulatedTimeElapsed_Type())
hdsl2ShdslEndpointAccumulatedTimeElapsed.setMaxAccess(_E)
if mibBuilder.loadTexts:hdsl2ShdslEndpointAccumulatedTimeElapsed.setStatus(_A)
class _Hdsl2ShdslEndpointCurrPsd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('asymmetric',2),('symmetric',3)))
_Hdsl2ShdslEndpointCurrPsd_Type.__name__=_C
_Hdsl2ShdslEndpointCurrPsd_Object=MibTableColumn
hdsl2ShdslEndpointCurrPsd=_Hdsl2ShdslEndpointCurrPsd_Object((1,3,6,1,4,1,164,3,1,6,12,1,1,7),_Hdsl2ShdslEndpointCurrPsd_Type())
hdsl2ShdslEndpointCurrPsd.setMaxAccess(_E)
if mibBuilder.loadTexts:hdsl2ShdslEndpointCurrPsd.setStatus(_A)
_Hdsl2ShdslEndpointValidIntervals_Type=Unsigned32
_Hdsl2ShdslEndpointValidIntervals_Object=MibTableColumn
hdsl2ShdslEndpointValidIntervals=_Hdsl2ShdslEndpointValidIntervals_Object((1,3,6,1,4,1,164,3,1,6,12,1,1,8),_Hdsl2ShdslEndpointValidIntervals_Type())
hdsl2ShdslEndpointValidIntervals.setMaxAccess(_E)
if mibBuilder.loadTexts:hdsl2ShdslEndpointValidIntervals.setStatus(_A)
_Hdsl2ShdslEndpointValidDaysIntervals_Type=Unsigned32
_Hdsl2ShdslEndpointValidDaysIntervals_Object=MibTableColumn
hdsl2ShdslEndpointValidDaysIntervals=_Hdsl2ShdslEndpointValidDaysIntervals_Object((1,3,6,1,4,1,164,3,1,6,12,1,1,9),_Hdsl2ShdslEndpointValidDaysIntervals_Type())
hdsl2ShdslEndpointValidDaysIntervals.setMaxAccess(_E)
if mibBuilder.loadTexts:hdsl2ShdslEndpointValidDaysIntervals.setStatus(_A)
_ShdslEndpointMaintTable_Object=MibTable
shdslEndpointMaintTable=_ShdslEndpointMaintTable_Object((1,3,6,1,4,1,164,3,1,6,12,2))
if mibBuilder.loadTexts:shdslEndpointMaintTable.setStatus(_A)
_ShdslEndpointMaintEntry_Object=MibTableRow
shdslEndpointMaintEntry=_ShdslEndpointMaintEntry_Object((1,3,6,1,4,1,164,3,1,6,12,2,1))
shdslEndpointMaintEntry.setIndexNames((0,_G,_R),(0,_F,_c),(0,_F,_X))
if mibBuilder.loadTexts:shdslEndpointMaintEntry.setStatus(_A)
class _ShdslMaintPowerBackOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('default',1),(_d,2),(_e,3)))
_ShdslMaintPowerBackOff_Type.__name__=_C
_ShdslMaintPowerBackOff_Object=MibTableColumn
shdslMaintPowerBackOff=_ShdslMaintPowerBackOff_Object((1,3,6,1,4,1,164,3,1,6,12,2,1,1),_ShdslMaintPowerBackOff_Type())
shdslMaintPowerBackOff.setMaxAccess(_D)
if mibBuilder.loadTexts:shdslMaintPowerBackOff.setStatus(_A)
_ShdslSpanConfProfileTable_Object=MibTable
shdslSpanConfProfileTable=_ShdslSpanConfProfileTable_Object((1,3,6,1,4,1,164,3,1,6,12,3))
if mibBuilder.loadTexts:shdslSpanConfProfileTable.setStatus(_A)
_ShdslSpanConfProfileEntry_Object=MibTableRow
shdslSpanConfProfileEntry=_ShdslSpanConfProfileEntry_Object((1,3,6,1,4,1,164,3,1,6,12,3,1))
if mibBuilder.loadTexts:shdslSpanConfProfileEntry.setStatus(_A)
class _Hdsl2ShdslSpanConfEocCompatible_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('proprietary',2),('standard',3)))
_Hdsl2ShdslSpanConfEocCompatible_Type.__name__=_C
_Hdsl2ShdslSpanConfEocCompatible_Object=MibTableColumn
hdsl2ShdslSpanConfEocCompatible=_Hdsl2ShdslSpanConfEocCompatible_Object((1,3,6,1,4,1,164,3,1,6,12,3,1,1),_Hdsl2ShdslSpanConfEocCompatible_Type())
hdsl2ShdslSpanConfEocCompatible.setMaxAccess(_E)
if mibBuilder.loadTexts:hdsl2ShdslSpanConfEocCompatible.setStatus(_A)
class _Hdsl2ShdslSpanConfAsymmetricPSDRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('asymmetricR1',2),('asymmetricR2',3)))
_Hdsl2ShdslSpanConfAsymmetricPSDRate_Type.__name__=_C
_Hdsl2ShdslSpanConfAsymmetricPSDRate_Object=MibTableColumn
hdsl2ShdslSpanConfAsymmetricPSDRate=_Hdsl2ShdslSpanConfAsymmetricPSDRate_Object((1,3,6,1,4,1,164,3,1,6,12,3,1,2),_Hdsl2ShdslSpanConfAsymmetricPSDRate_Type())
hdsl2ShdslSpanConfAsymmetricPSDRate.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslSpanConfAsymmetricPSDRate.setStatus(_A)
class _Hdsl2ShdslSpanConfWireInterfaceUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('twoWires',2),('fourWires',3),('autoDetection',4)))
_Hdsl2ShdslSpanConfWireInterfaceUsed_Type.__name__=_C
_Hdsl2ShdslSpanConfWireInterfaceUsed_Object=MibTableColumn
hdsl2ShdslSpanConfWireInterfaceUsed=_Hdsl2ShdslSpanConfWireInterfaceUsed_Object((1,3,6,1,4,1,164,3,1,6,12,3,1,3),_Hdsl2ShdslSpanConfWireInterfaceUsed_Type())
hdsl2ShdslSpanConfWireInterfaceUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslSpanConfWireInterfaceUsed.setStatus(_A)
class _Hdsl2ShdslSpanConfHandshake_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('automatic',1),('g994dot1rev2001',2)))
_Hdsl2ShdslSpanConfHandshake_Type.__name__=_C
_Hdsl2ShdslSpanConfHandshake_Object=MibTableColumn
hdsl2ShdslSpanConfHandshake=_Hdsl2ShdslSpanConfHandshake_Object((1,3,6,1,4,1,164,3,1,6,12,3,1,4),_Hdsl2ShdslSpanConfHandshake_Type())
hdsl2ShdslSpanConfHandshake.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslSpanConfHandshake.setStatus(_A)
_Hdsl2ShdslIfConf_ObjectIdentity=ObjectIdentity
hdsl2ShdslIfConf=_Hdsl2ShdslIfConf_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,12,4))
_Hdsl2ShdslIfConfTable_Object=MibTable
hdsl2ShdslIfConfTable=_Hdsl2ShdslIfConfTable_Object((1,3,6,1,4,1,164,3,1,6,12,4,1))
if mibBuilder.loadTexts:hdsl2ShdslIfConfTable.setStatus(_A)
_Hdsl2ShdslIfConfEntry_Object=MibTableRow
hdsl2ShdslIfConfEntry=_Hdsl2ShdslIfConfEntry_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1))
hdsl2ShdslIfConfEntry.setIndexNames((0,_I,_f),(0,_G,_R),(0,_I,_g))
if mibBuilder.loadTexts:hdsl2ShdslIfConfEntry.setStatus(_A)
class _Hdsl2ShdslIfConfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Hdsl2ShdslIfConfIdx_Type.__name__=_C
_Hdsl2ShdslIfConfIdx_Object=MibTableColumn
hdsl2ShdslIfConfIdx=_Hdsl2ShdslIfConfIdx_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,1),_Hdsl2ShdslIfConfIdx_Type())
hdsl2ShdslIfConfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:hdsl2ShdslIfConfIdx.setStatus(_A)
class _Hdsl2ShdslSideIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('nearEnd',2),('farEnd',3),('rptr1',4),('rptr2',5),('rptr3',6),('rptr4',7),('rptr5',8),('rptr6',9),('rptr7',10),('rptr8',11)))
_Hdsl2ShdslSideIdx_Type.__name__=_C
_Hdsl2ShdslSideIdx_Object=MibTableColumn
hdsl2ShdslSideIdx=_Hdsl2ShdslSideIdx_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,2),_Hdsl2ShdslSideIdx_Type())
hdsl2ShdslSideIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:hdsl2ShdslSideIdx.setStatus(_A)
class _Hdsl2ShdslMaxBw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)));namedValues=NamedValues(*((_H,1),('r192',2),('r256',3),('r320',4),('r384',5),('r448',6),('r512',7),('r576',8),('r640',9),('r704',10),('r768',11),('r832',12),('r896',13),('r960',14),('r1024',15),('r1088',16),('r1152',17),('r1216',18),('r1280',19),('r1344',20),('r1408',21),('r1472',22),('r1536',23),('r1600',24),('r1664',25),('r1728',26),('r1792',27),('r1856',28),('r1920',29),('r1984',30),('r2048',31)))
_Hdsl2ShdslMaxBw_Type.__name__=_C
_Hdsl2ShdslMaxBw_Object=MibTableColumn
hdsl2ShdslMaxBw=_Hdsl2ShdslMaxBw_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,3),_Hdsl2ShdslMaxBw_Type())
hdsl2ShdslMaxBw.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslMaxBw.setStatus(_A)
class _Hdsl2ShdslPwrBackoff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_d,2),(_e,3)))
_Hdsl2ShdslPwrBackoff_Type.__name__=_C
_Hdsl2ShdslPwrBackoff_Object=MibTableColumn
hdsl2ShdslPwrBackoff=_Hdsl2ShdslPwrBackoff_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,4),_Hdsl2ShdslPwrBackoff_Type())
hdsl2ShdslPwrBackoff.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslPwrBackoff.setStatus(_A)
class _Hdsl2ShdslTxMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('annexA',2),('annexB',3),('annexG',4),('annexF',5)))
_Hdsl2ShdslTxMode_Type.__name__=_C
_Hdsl2ShdslTxMode_Object=MibTableColumn
hdsl2ShdslTxMode=_Hdsl2ShdslTxMode_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,5),_Hdsl2ShdslTxMode_Type())
hdsl2ShdslTxMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslTxMode.setStatus(_A)
_Hdsl2ShdslAttenuationThreshold_Type=Integer32
_Hdsl2ShdslAttenuationThreshold_Object=MibTableColumn
hdsl2ShdslAttenuationThreshold=_Hdsl2ShdslAttenuationThreshold_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,6),_Hdsl2ShdslAttenuationThreshold_Type())
hdsl2ShdslAttenuationThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslAttenuationThreshold.setStatus(_A)
if mibBuilder.loadTexts:hdsl2ShdslAttenuationThreshold.setUnits(_Q)
_Hdsl2ShdslSnrMarginThreshold_Type=Integer32
_Hdsl2ShdslSnrMarginThreshold_Object=MibTableColumn
hdsl2ShdslSnrMarginThreshold=_Hdsl2ShdslSnrMarginThreshold_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,7),_Hdsl2ShdslSnrMarginThreshold_Type())
hdsl2ShdslSnrMarginThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslSnrMarginThreshold.setStatus(_A)
if mibBuilder.loadTexts:hdsl2ShdslSnrMarginThreshold.setUnits(_Q)
class _Hdsl2ShdslTs0OverDsl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('looped',2),('transparent',3)))
_Hdsl2ShdslTs0OverDsl_Type.__name__=_C
_Hdsl2ShdslTs0OverDsl_Object=MibTableColumn
hdsl2ShdslTs0OverDsl=_Hdsl2ShdslTs0OverDsl_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,8),_Hdsl2ShdslTs0OverDsl_Type())
hdsl2ShdslTs0OverDsl.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslTs0OverDsl.setStatus(_A)
class _Hdsl2ShdslMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('stuC',2),('stuR',3)))
_Hdsl2ShdslMode_Type.__name__=_C
_Hdsl2ShdslMode_Object=MibTableColumn
hdsl2ShdslMode=_Hdsl2ShdslMode_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,9),_Hdsl2ShdslMode_Type())
hdsl2ShdslMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslMode.setStatus(_A)
class _Hdsl2ShdslTsCompactionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noCompaction',1),('noMapping',2),('withMapping',3),('lowTsMapping',4),('spareMapping',5)))
_Hdsl2ShdslTsCompactionMode_Type.__name__=_C
_Hdsl2ShdslTsCompactionMode_Object=MibTableColumn
hdsl2ShdslTsCompactionMode=_Hdsl2ShdslTsCompactionMode_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,10),_Hdsl2ShdslTsCompactionMode_Type())
hdsl2ShdslTsCompactionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslTsCompactionMode.setStatus(_A)
class _Hdsl2ShdslEocEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('no',2),('yes',3)))
_Hdsl2ShdslEocEnable_Type.__name__=_C
_Hdsl2ShdslEocEnable_Object=MibTableColumn
hdsl2ShdslEocEnable=_Hdsl2ShdslEocEnable_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,11),_Hdsl2ShdslEocEnable_Type())
hdsl2ShdslEocEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslEocEnable.setStatus(_A)
_Hdsl2ShdslFar1stIfNumOfTSs_Type=Unsigned32
_Hdsl2ShdslFar1stIfNumOfTSs_Object=MibTableColumn
hdsl2ShdslFar1stIfNumOfTSs=_Hdsl2ShdslFar1stIfNumOfTSs_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,12),_Hdsl2ShdslFar1stIfNumOfTSs_Type())
hdsl2ShdslFar1stIfNumOfTSs.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslFar1stIfNumOfTSs.setStatus(_A)
class _Hdsl2ShdslFarEndDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('other',2),('mpComponent',3),('asmi52SingleIf',4),('asmi52E1AndData',5),('asmi52E1AndEth',6),('asmi52EthAndData',7),('fcdip',8),('dxc',9)))
_Hdsl2ShdslFarEndDevice_Type.__name__=_C
_Hdsl2ShdslFarEndDevice_Object=MibTableColumn
hdsl2ShdslFarEndDevice=_Hdsl2ShdslFarEndDevice_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,13),_Hdsl2ShdslFarEndDevice_Type())
hdsl2ShdslFarEndDevice.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslFarEndDevice.setStatus(_A)
_Hdsl2ShdslPwrBackoffDb_Type=Integer32
_Hdsl2ShdslPwrBackoffDb_Object=MibTableColumn
hdsl2ShdslPwrBackoffDb=_Hdsl2ShdslPwrBackoffDb_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,14),_Hdsl2ShdslPwrBackoffDb_Type())
hdsl2ShdslPwrBackoffDb.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslPwrBackoffDb.setStatus(_A)
if mibBuilder.loadTexts:hdsl2ShdslPwrBackoffDb.setUnits(_Q)
_Hdsl2ShdslFarEndMuxTsa_Type=OctetString
_Hdsl2ShdslFarEndMuxTsa_Object=MibTableColumn
hdsl2ShdslFarEndMuxTsa=_Hdsl2ShdslFarEndMuxTsa_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,15),_Hdsl2ShdslFarEndMuxTsa_Type())
hdsl2ShdslFarEndMuxTsa.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslFarEndMuxTsa.setStatus(_A)
class _Hdsl2ShdslLineProbeEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_Hdsl2ShdslLineProbeEnable_Type.__name__=_C
_Hdsl2ShdslLineProbeEnable_Object=MibTableColumn
hdsl2ShdslLineProbeEnable=_Hdsl2ShdslLineProbeEnable_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,16),_Hdsl2ShdslLineProbeEnable_Type())
hdsl2ShdslLineProbeEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslLineProbeEnable.setStatus(_A)
class _Hdsl2ShdslClockMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('plesiochronous1',1),('plesiochronousWithTimeReference2',2),('synchronous3a',3),('hybrid',4)))
_Hdsl2ShdslClockMode_Type.__name__=_C
_Hdsl2ShdslClockMode_Object=MibTableColumn
hdsl2ShdslClockMode=_Hdsl2ShdslClockMode_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,17),_Hdsl2ShdslClockMode_Type())
hdsl2ShdslClockMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hdsl2ShdslClockMode.setStatus(_A)
class _Hdsl2ShdslIfConfLinkDownReason_Type(Bits):namedValues=NamedValues(*(('unknown',0),('es',1),('ses',2),('crcAnomaly',3),('losw',4),('uas',5),('snrMarginAlarm',6)))
_Hdsl2ShdslIfConfLinkDownReason_Type.__name__=_S
_Hdsl2ShdslIfConfLinkDownReason_Object=MibTableColumn
hdsl2ShdslIfConfLinkDownReason=_Hdsl2ShdslIfConfLinkDownReason_Object((1,3,6,1,4,1,164,3,1,6,12,4,1,1,19),_Hdsl2ShdslIfConfLinkDownReason_Type())
hdsl2ShdslIfConfLinkDownReason.setMaxAccess(_E)
if mibBuilder.loadTexts:hdsl2ShdslIfConfLinkDownReason.setStatus(_A)
hdsl2ShdslEndpointCurrEntry.registerAugmentions((_I,_h))
shdslEndpointCurrEntry.setIndexNames(*hdsl2ShdslEndpointCurrEntry.getIndexNames())
hdsl2ShdslSpanConfProfileEntry.registerAugmentions((_I,_i))
shdslSpanConfProfileEntry.setIndexNames(*hdsl2ShdslSpanConfProfileEntry.getIndexNames())
radHdsl2ShdslLoopBackTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,12,0,1))
radHdsl2ShdslLoopBackTrap.setObjects(*((_I,'alarmSeverity'),(_I,'alarmState'),(_G,_J)))
if mibBuilder.loadTexts:radHdsl2ShdslLoopBackTrap.setStatus(_A)
shdslLosw=NotificationType((1,3,6,1,4,1,164,3,1,6,12,0,13))
shdslLosw.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_G,_J),(_F,_U),(_F,_Z)))
if mibBuilder.loadTexts:shdslLosw.setStatus(_A)
shdslExcessiveCrcError=NotificationType((1,3,6,1,4,1,164,3,1,6,12,0,15))
shdslExcessiveCrcError.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_G,_J),(_F,_T),(_F,_Y)))
if mibBuilder.loadTexts:shdslExcessiveCrcError.setStatus(_A)
shdslLoopAttenuationOra=NotificationType((1,3,6,1,4,1,164,3,1,6,12,0,19))
shdslLoopAttenuationOra.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_G,_J),(_F,_V),(_F,_a)))
if mibBuilder.loadTexts:shdslLoopAttenuationOra.setStatus(_A)
shdslSnrMarginOra=NotificationType((1,3,6,1,4,1,164,3,1,6,12,0,20))
shdslSnrMarginOra.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_G,_J),(_F,_W),(_F,_b)))
if mibBuilder.loadTexts:shdslSnrMarginOra.setStatus(_A)
shdslLinkDown=NotificationType((1,3,6,1,4,1,164,3,1,6,12,0,23))
shdslLinkDown.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_G,_J),(_I,_j)))
if mibBuilder.loadTexts:shdslLinkDown.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'shdslIf':shdslIf,'radHdsl2ShdslEvents':radHdsl2ShdslEvents,'radHdsl2ShdslLoopBackTrap':radHdsl2ShdslLoopBackTrap,'shdslLosw':shdslLosw,'shdslExcessiveCrcError':shdslExcessiveCrcError,'shdslLoopAttenuationOra':shdslLoopAttenuationOra,'shdslSnrMarginOra':shdslSnrMarginOra,'shdslLinkDown':shdslLinkDown,'shdslEndpointCurrTable':shdslEndpointCurrTable,_h:shdslEndpointCurrEntry,'hdsl2ShdslEndpointCurrRcvGain':hdsl2ShdslEndpointCurrRcvGain,'hdsl2ShdslEndpointCurrTransPower':hdsl2ShdslEndpointCurrTransPower,'hdsl2ShdslEndpointCurrPowerBO':hdsl2ShdslEndpointCurrPowerBO,'hdsl2ShdslEndpointCurrLineStatus':hdsl2ShdslEndpointCurrLineStatus,'hdsl2ShdslEndpointCurrOpState':hdsl2ShdslEndpointCurrOpState,'hdsl2ShdslEndpointAccumulatedTimeElapsed':hdsl2ShdslEndpointAccumulatedTimeElapsed,'hdsl2ShdslEndpointCurrPsd':hdsl2ShdslEndpointCurrPsd,'hdsl2ShdslEndpointValidIntervals':hdsl2ShdslEndpointValidIntervals,'hdsl2ShdslEndpointValidDaysIntervals':hdsl2ShdslEndpointValidDaysIntervals,'shdslEndpointMaintTable':shdslEndpointMaintTable,'shdslEndpointMaintEntry':shdslEndpointMaintEntry,'shdslMaintPowerBackOff':shdslMaintPowerBackOff,'shdslSpanConfProfileTable':shdslSpanConfProfileTable,_i:shdslSpanConfProfileEntry,'hdsl2ShdslSpanConfEocCompatible':hdsl2ShdslSpanConfEocCompatible,'hdsl2ShdslSpanConfAsymmetricPSDRate':hdsl2ShdslSpanConfAsymmetricPSDRate,'hdsl2ShdslSpanConfWireInterfaceUsed':hdsl2ShdslSpanConfWireInterfaceUsed,'hdsl2ShdslSpanConfHandshake':hdsl2ShdslSpanConfHandshake,'hdsl2ShdslIfConf':hdsl2ShdslIfConf,'hdsl2ShdslIfConfTable':hdsl2ShdslIfConfTable,'hdsl2ShdslIfConfEntry':hdsl2ShdslIfConfEntry,_f:hdsl2ShdslIfConfIdx,_g:hdsl2ShdslSideIdx,'hdsl2ShdslMaxBw':hdsl2ShdslMaxBw,'hdsl2ShdslPwrBackoff':hdsl2ShdslPwrBackoff,'hdsl2ShdslTxMode':hdsl2ShdslTxMode,'hdsl2ShdslAttenuationThreshold':hdsl2ShdslAttenuationThreshold,'hdsl2ShdslSnrMarginThreshold':hdsl2ShdslSnrMarginThreshold,'hdsl2ShdslTs0OverDsl':hdsl2ShdslTs0OverDsl,'hdsl2ShdslMode':hdsl2ShdslMode,'hdsl2ShdslTsCompactionMode':hdsl2ShdslTsCompactionMode,'hdsl2ShdslEocEnable':hdsl2ShdslEocEnable,'hdsl2ShdslFar1stIfNumOfTSs':hdsl2ShdslFar1stIfNumOfTSs,'hdsl2ShdslFarEndDevice':hdsl2ShdslFarEndDevice,'hdsl2ShdslPwrBackoffDb':hdsl2ShdslPwrBackoffDb,'hdsl2ShdslFarEndMuxTsa':hdsl2ShdslFarEndMuxTsa,'hdsl2ShdslLineProbeEnable':hdsl2ShdslLineProbeEnable,'hdsl2ShdslClockMode':hdsl2ShdslClockMode,_j:hdsl2ShdslIfConfLinkDownReason})