_O='msagVoipQRIndex'
_N='msagVoipQRSlotno'
_M='msagVoipQRShelfno'
_L='msagVoipQRRackno'
_K='msagVoipQovsCmdIndex'
_J='msagVoipQovsCmdSlotno'
_I='msagVoipQovsCmdShelfno'
_H='msagVoipQovsCmdRackno'
_G='msagVoipQovsParaIndex'
_F='read-write'
_E='not-accessible'
_D='ZTE-AN-VOIP-QOS-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
zxAnVoipQosMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,5200))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxAn_ObjectIdentity=ObjectIdentity
zxAn=_ZxAn_ObjectIdentity((1,3,6,1,4,1,3902,1015))
_MsagmajorVersion_ObjectIdentity=ObjectIdentity
msagmajorVersion=_MsagmajorVersion_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3))
_MsagVoipQovs_ObjectIdentity=ObjectIdentity
msagVoipQovs=_MsagVoipQovs_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,7))
_MsagVoipQovsParaSetTable_Object=MibTable
msagVoipQovsParaSetTable=_MsagVoipQovsParaSetTable_Object((1,3,6,1,4,1,3902,1015,5200,3,7,1))
if mibBuilder.loadTexts:msagVoipQovsParaSetTable.setStatus(_A)
_MsagVoipQovsParaSetEntry_Object=MibTableRow
msagVoipQovsParaSetEntry=_MsagVoipQovsParaSetEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,7,1,1))
msagVoipQovsParaSetEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:msagVoipQovsParaSetEntry.setStatus(_A)
class _MsagVoipQovsParaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_MsagVoipQovsParaIndex_Type.__name__=_B
_MsagVoipQovsParaIndex_Object=MibTableColumn
msagVoipQovsParaIndex=_MsagVoipQovsParaIndex_Object((1,3,6,1,4,1,3902,1015,5200,3,7,1,1,1),_MsagVoipQovsParaIndex_Type())
msagVoipQovsParaIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:msagVoipQovsParaIndex.setStatus(_A)
class _MsagVoipQovsParaTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_MsagVoipQovsParaTimer_Type.__name__=_B
_MsagVoipQovsParaTimer_Object=MibTableColumn
msagVoipQovsParaTimer=_MsagVoipQovsParaTimer_Object((1,3,6,1,4,1,3902,1015,5200,3,7,1,1,2),_MsagVoipQovsParaTimer_Type())
msagVoipQovsParaTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:msagVoipQovsParaTimer.setStatus(_A)
class _MsagVoipQovsParaDelayThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_MsagVoipQovsParaDelayThresh_Type.__name__=_B
_MsagVoipQovsParaDelayThresh_Object=MibTableColumn
msagVoipQovsParaDelayThresh=_MsagVoipQovsParaDelayThresh_Object((1,3,6,1,4,1,3902,1015,5200,3,7,1,1,3),_MsagVoipQovsParaDelayThresh_Type())
msagVoipQovsParaDelayThresh.setMaxAccess(_F)
if mibBuilder.loadTexts:msagVoipQovsParaDelayThresh.setStatus(_A)
class _MsagVoipQovsParaLossThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_MsagVoipQovsParaLossThresh_Type.__name__=_B
_MsagVoipQovsParaLossThresh_Object=MibTableColumn
msagVoipQovsParaLossThresh=_MsagVoipQovsParaLossThresh_Object((1,3,6,1,4,1,3902,1015,5200,3,7,1,1,4),_MsagVoipQovsParaLossThresh_Type())
msagVoipQovsParaLossThresh.setMaxAccess(_F)
if mibBuilder.loadTexts:msagVoipQovsParaLossThresh.setStatus(_A)
class _MsagVoipQovsParaJitterThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_MsagVoipQovsParaJitterThresh_Type.__name__=_B
_MsagVoipQovsParaJitterThresh_Object=MibTableColumn
msagVoipQovsParaJitterThresh=_MsagVoipQovsParaJitterThresh_Object((1,3,6,1,4,1,3902,1015,5200,3,7,1,1,5),_MsagVoipQovsParaJitterThresh_Type())
msagVoipQovsParaJitterThresh.setMaxAccess(_F)
if mibBuilder.loadTexts:msagVoipQovsParaJitterThresh.setStatus(_A)
_MsagVoipQovsCommandTable_Object=MibTable
msagVoipQovsCommandTable=_MsagVoipQovsCommandTable_Object((1,3,6,1,4,1,3902,1015,5200,3,7,2))
if mibBuilder.loadTexts:msagVoipQovsCommandTable.setStatus(_A)
_MsagVoipQovsCommandEntry_Object=MibTableRow
msagVoipQovsCommandEntry=_MsagVoipQovsCommandEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,7,2,1))
msagVoipQovsCommandEntry.setIndexNames((0,_D,_H),(0,_D,_I),(0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:msagVoipQovsCommandEntry.setStatus(_A)
class _MsagVoipQovsCmdRackno_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_MsagVoipQovsCmdRackno_Type.__name__=_B
_MsagVoipQovsCmdRackno_Object=MibTableColumn
msagVoipQovsCmdRackno=_MsagVoipQovsCmdRackno_Object((1,3,6,1,4,1,3902,1015,5200,3,7,2,1,1),_MsagVoipQovsCmdRackno_Type())
msagVoipQovsCmdRackno.setMaxAccess(_E)
if mibBuilder.loadTexts:msagVoipQovsCmdRackno.setStatus(_A)
class _MsagVoipQovsCmdShelfno_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_MsagVoipQovsCmdShelfno_Type.__name__=_B
_MsagVoipQovsCmdShelfno_Object=MibTableColumn
msagVoipQovsCmdShelfno=_MsagVoipQovsCmdShelfno_Object((1,3,6,1,4,1,3902,1015,5200,3,7,2,1,2),_MsagVoipQovsCmdShelfno_Type())
msagVoipQovsCmdShelfno.setMaxAccess(_E)
if mibBuilder.loadTexts:msagVoipQovsCmdShelfno.setStatus(_A)
class _MsagVoipQovsCmdSlotno_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,23))
_MsagVoipQovsCmdSlotno_Type.__name__=_B
_MsagVoipQovsCmdSlotno_Object=MibTableColumn
msagVoipQovsCmdSlotno=_MsagVoipQovsCmdSlotno_Object((1,3,6,1,4,1,3902,1015,5200,3,7,2,1,3),_MsagVoipQovsCmdSlotno_Type())
msagVoipQovsCmdSlotno.setMaxAccess(_E)
if mibBuilder.loadTexts:msagVoipQovsCmdSlotno.setStatus(_A)
class _MsagVoipQovsCmdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,23))
_MsagVoipQovsCmdIndex_Type.__name__=_B
_MsagVoipQovsCmdIndex_Object=MibTableColumn
msagVoipQovsCmdIndex=_MsagVoipQovsCmdIndex_Object((1,3,6,1,4,1,3902,1015,5200,3,7,2,1,4),_MsagVoipQovsCmdIndex_Type())
msagVoipQovsCmdIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:msagVoipQovsCmdIndex.setStatus(_A)
class _MsagVoipQovsCmdno_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cmdStart',1),('cmdEnd',2)))
_MsagVoipQovsCmdno_Type.__name__=_B
_MsagVoipQovsCmdno_Object=MibTableColumn
msagVoipQovsCmdno=_MsagVoipQovsCmdno_Object((1,3,6,1,4,1,3902,1015,5200,3,7,2,1,5),_MsagVoipQovsCmdno_Type())
msagVoipQovsCmdno.setMaxAccess(_F)
if mibBuilder.loadTexts:msagVoipQovsCmdno.setStatus(_A)
_MsagVoipQovsResultTable_Object=MibTable
msagVoipQovsResultTable=_MsagVoipQovsResultTable_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3))
if mibBuilder.loadTexts:msagVoipQovsResultTable.setStatus(_A)
_MsagVoipQovsResultEntry_Object=MibTableRow
msagVoipQovsResultEntry=_MsagVoipQovsResultEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1))
msagVoipQovsResultEntry.setIndexNames((0,_D,_L),(0,_D,_M),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:msagVoipQovsResultEntry.setStatus(_A)
class _MsagVoipQRRackno_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_MsagVoipQRRackno_Type.__name__=_B
_MsagVoipQRRackno_Object=MibTableColumn
msagVoipQRRackno=_MsagVoipQRRackno_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,1),_MsagVoipQRRackno_Type())
msagVoipQRRackno.setMaxAccess(_E)
if mibBuilder.loadTexts:msagVoipQRRackno.setStatus(_A)
class _MsagVoipQRShelfno_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_MsagVoipQRShelfno_Type.__name__=_B
_MsagVoipQRShelfno_Object=MibTableColumn
msagVoipQRShelfno=_MsagVoipQRShelfno_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,2),_MsagVoipQRShelfno_Type())
msagVoipQRShelfno.setMaxAccess(_E)
if mibBuilder.loadTexts:msagVoipQRShelfno.setStatus(_A)
class _MsagVoipQRSlotno_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,23))
_MsagVoipQRSlotno_Type.__name__=_B
_MsagVoipQRSlotno_Object=MibTableColumn
msagVoipQRSlotno=_MsagVoipQRSlotno_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,3),_MsagVoipQRSlotno_Type())
msagVoipQRSlotno.setMaxAccess(_E)
if mibBuilder.loadTexts:msagVoipQRSlotno.setStatus(_A)
class _MsagVoipQRIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,23))
_MsagVoipQRIndex_Type.__name__=_B
_MsagVoipQRIndex_Object=MibTableColumn
msagVoipQRIndex=_MsagVoipQRIndex_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,4),_MsagVoipQRIndex_Type())
msagVoipQRIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:msagVoipQRIndex.setStatus(_A)
class _MsagVoipQRDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_MsagVoipQRDelay_Type.__name__=_B
_MsagVoipQRDelay_Object=MibTableColumn
msagVoipQRDelay=_MsagVoipQRDelay_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,5),_MsagVoipQRDelay_Type())
msagVoipQRDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:msagVoipQRDelay.setStatus(_A)
class _MsagVoipQRLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_MsagVoipQRLoss_Type.__name__=_B
_MsagVoipQRLoss_Object=MibTableColumn
msagVoipQRLoss=_MsagVoipQRLoss_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,6),_MsagVoipQRLoss_Type())
msagVoipQRLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:msagVoipQRLoss.setStatus(_A)
class _MsagVoipQRJitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_MsagVoipQRJitter_Type.__name__=_B
_MsagVoipQRJitter_Object=MibTableColumn
msagVoipQRJitter=_MsagVoipQRJitter_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,7),_MsagVoipQRJitter_Type())
msagVoipQRJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:msagVoipQRJitter.setStatus(_A)
_MsagVoipQRSrcPort_Type=Integer32
_MsagVoipQRSrcPort_Object=MibTableColumn
msagVoipQRSrcPort=_MsagVoipQRSrcPort_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,8),_MsagVoipQRSrcPort_Type())
msagVoipQRSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:msagVoipQRSrcPort.setStatus(_A)
_MsagVoipQRDestPort_Type=Integer32
_MsagVoipQRDestPort_Object=MibTableColumn
msagVoipQRDestPort=_MsagVoipQRDestPort_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,9),_MsagVoipQRDestPort_Type())
msagVoipQRDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:msagVoipQRDestPort.setStatus(_A)
_MsagVoipQRSrcIPAddr_Type=IpAddress
_MsagVoipQRSrcIPAddr_Object=MibTableColumn
msagVoipQRSrcIPAddr=_MsagVoipQRSrcIPAddr_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,10),_MsagVoipQRSrcIPAddr_Type())
msagVoipQRSrcIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:msagVoipQRSrcIPAddr.setStatus(_A)
_MsagVoipQRTime_Type=Integer32
_MsagVoipQRTime_Object=MibTableColumn
msagVoipQRTime=_MsagVoipQRTime_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,11),_MsagVoipQRTime_Type())
msagVoipQRTime.setMaxAccess(_C)
if mibBuilder.loadTexts:msagVoipQRTime.setStatus(_A)
_MsagVoipQRMos_Type=Integer32
_MsagVoipQRMos_Object=MibTableColumn
msagVoipQRMos=_MsagVoipQRMos_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,12),_MsagVoipQRMos_Type())
msagVoipQRMos.setMaxAccess(_C)
if mibBuilder.loadTexts:msagVoipQRMos.setStatus(_A)
_MsagVoipQRLossRate_Type=Integer32
_MsagVoipQRLossRate_Object=MibTableColumn
msagVoipQRLossRate=_MsagVoipQRLossRate_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,13),_MsagVoipQRLossRate_Type())
msagVoipQRLossRate.setMaxAccess(_C)
if mibBuilder.loadTexts:msagVoipQRLossRate.setStatus(_A)
_MsagVoipQRsignalLev_Type=Integer32
_MsagVoipQRsignalLev_Object=MibTableColumn
msagVoipQRsignalLev=_MsagVoipQRsignalLev_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,14),_MsagVoipQRsignalLev_Type())
msagVoipQRsignalLev.setMaxAccess(_C)
if mibBuilder.loadTexts:msagVoipQRsignalLev.setStatus(_A)
_MsagVoipQRnoiseLev_Type=Integer32
_MsagVoipQRnoiseLev_Object=MibTableColumn
msagVoipQRnoiseLev=_MsagVoipQRnoiseLev_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,15),_MsagVoipQRnoiseLev_Type())
msagVoipQRnoiseLev.setMaxAccess(_C)
if mibBuilder.loadTexts:msagVoipQRnoiseLev.setStatus(_A)
_MsagVoipQRRERL_Type=Integer32
_MsagVoipQRRERL_Object=MibTableColumn
msagVoipQRRERL=_MsagVoipQRRERL_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,16),_MsagVoipQRRERL_Type())
msagVoipQRRERL.setMaxAccess(_C)
if mibBuilder.loadTexts:msagVoipQRRERL.setStatus(_A)
_MsagVoipQRBurstDuration_Type=Integer32
_MsagVoipQRBurstDuration_Object=MibTableColumn
msagVoipQRBurstDuration=_MsagVoipQRBurstDuration_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,17),_MsagVoipQRBurstDuration_Type())
msagVoipQRBurstDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:msagVoipQRBurstDuration.setStatus(_A)
_MsagVoipQRgapDuration_Type=Integer32
_MsagVoipQRgapDuration_Object=MibTableColumn
msagVoipQRgapDuration=_MsagVoipQRgapDuration_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,18),_MsagVoipQRgapDuration_Type())
msagVoipQRgapDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:msagVoipQRgapDuration.setStatus(_A)
_MsagVoipQRBurstDensity_Type=Integer32
_MsagVoipQRBurstDensity_Object=MibTableColumn
msagVoipQRBurstDensity=_MsagVoipQRBurstDensity_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,19),_MsagVoipQRBurstDensity_Type())
msagVoipQRBurstDensity.setMaxAccess(_C)
if mibBuilder.loadTexts:msagVoipQRBurstDensity.setStatus(_A)
_MsagVoipQRGapDensity_Type=Integer32
_MsagVoipQRGapDensity_Object=MibTableColumn
msagVoipQRGapDensity=_MsagVoipQRGapDensity_Object((1,3,6,1,4,1,3902,1015,5200,3,7,3,1,20),_MsagVoipQRGapDensity_Type())
msagVoipQRGapDensity.setMaxAccess(_C)
if mibBuilder.loadTexts:msagVoipQRGapDensity.setStatus(_A)
_MsagNarrowGetNext_Type=Integer32
_MsagNarrowGetNext_Object=MibScalar
msagNarrowGetNext=_MsagNarrowGetNext_Object((1,3,6,1,4,1,3902,1015,5200,3,7,10),_MsagNarrowGetNext_Type())
msagNarrowGetNext.setMaxAccess(_C)
if mibBuilder.loadTexts:msagNarrowGetNext.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zte':zte,'zxAn':zxAn,'zxAnVoipQosMib':zxAnVoipQosMib,'msagmajorVersion':msagmajorVersion,'msagVoipQovs':msagVoipQovs,'msagVoipQovsParaSetTable':msagVoipQovsParaSetTable,'msagVoipQovsParaSetEntry':msagVoipQovsParaSetEntry,_G:msagVoipQovsParaIndex,'msagVoipQovsParaTimer':msagVoipQovsParaTimer,'msagVoipQovsParaDelayThresh':msagVoipQovsParaDelayThresh,'msagVoipQovsParaLossThresh':msagVoipQovsParaLossThresh,'msagVoipQovsParaJitterThresh':msagVoipQovsParaJitterThresh,'msagVoipQovsCommandTable':msagVoipQovsCommandTable,'msagVoipQovsCommandEntry':msagVoipQovsCommandEntry,_H:msagVoipQovsCmdRackno,_I:msagVoipQovsCmdShelfno,_J:msagVoipQovsCmdSlotno,_K:msagVoipQovsCmdIndex,'msagVoipQovsCmdno':msagVoipQovsCmdno,'msagVoipQovsResultTable':msagVoipQovsResultTable,'msagVoipQovsResultEntry':msagVoipQovsResultEntry,_L:msagVoipQRRackno,_M:msagVoipQRShelfno,_N:msagVoipQRSlotno,_O:msagVoipQRIndex,'msagVoipQRDelay':msagVoipQRDelay,'msagVoipQRLoss':msagVoipQRLoss,'msagVoipQRJitter':msagVoipQRJitter,'msagVoipQRSrcPort':msagVoipQRSrcPort,'msagVoipQRDestPort':msagVoipQRDestPort,'msagVoipQRSrcIPAddr':msagVoipQRSrcIPAddr,'msagVoipQRTime':msagVoipQRTime,'msagVoipQRMos':msagVoipQRMos,'msagVoipQRLossRate':msagVoipQRLossRate,'msagVoipQRsignalLev':msagVoipQRsignalLev,'msagVoipQRnoiseLev':msagVoipQRnoiseLev,'msagVoipQRRERL':msagVoipQRRERL,'msagVoipQRBurstDuration':msagVoipQRBurstDuration,'msagVoipQRgapDuration':msagVoipQRgapDuration,'msagVoipQRBurstDensity':msagVoipQRBurstDensity,'msagVoipQRGapDensity':msagVoipQRGapDensity,'msagNarrowGetNext':msagNarrowGetNext})