_AA='ntcTsAnlyConfGrpV1Standard'
_A9='ntcTsAnlyEPidTransportError'
_A8='ntcTsAnlyEPidContinuityError'
_A7='ntcTsAnlyEPidCtuCntErrorCntr'
_A6='ntcTsAnlyEPidType'
_A5='ntcTsAnlyAlmPcrAccuracy'
_A4='ntcTsAnlyAlmPcrDiscontinuity'
_A3='ntcTsAnlyAlmPcrRepetition'
_A2='ntcTsAnlyAlmTransport'
_A1='ntcTsAnlyAlmContinuityCount'
_A0='ntcTsAnlyAlmPat'
_z='ntcTsAnlyAlmSyncByte'
_y='ntcTsAnlyAlmSyncLoss'
_x='ntcTsAnlyPcrPidPcrRate'
_w='ntcTsAnlyPcrPidRateOffset'
_v='ntcTsAnlyPcrPidMaxHoldJitter'
_u='ntcTsAnlyPcrPidMinHoldJitter'
_t='ntcTsAnlyPcrPidMaxJitter'
_s='ntcTsAnlyPcrPidMinJitter'
_r='ntcTsAnlyPcrPidPcrAccuracyError'
_q='ntcTsAnlyPcrPidPcrRepeatError'
_p='ntcTsAnlyPcrPidPcrIntervalTime'
_o='ntcTsAnlyPidCtuCntErrorCntr'
_n='ntcTsAnlyPidTransportError'
_m='ntcTsAnlyPidContinuityError'
_l='ntcTsAnlyPidPIDRate'
_k='ntcTsAnlyPidType'
_j='ntcTsAnlyEstimatedTsRate'
_i='ntcTsAnlyReset'
_h='ntcTsAnlyEble'
_g='ntcTsAnlyEPidPid'
_f='ntcTsAnlyPcrPidPid'
_e='packets'
_d='visual'
_c='othersOrGhost'
_b='measurement'
_a='inband'
_Z='netwSync'
_Y='tdtOrTotOrSt'
_X='rstOrSt'
_W='eitOrStCit'
_V='sdtOrBatOrSt'
_U='nitOrSt'
_T='userPrivate'
_S='metadata'
_R='slOrFlexMux'
_Q='auxiliary'
_P='pesPrivate'
_O='privateSection'
_N='others'
_M='ntcTsAnlyPidPid'
_L='read-write'
_K='NtcEnable'
_J='not-accessible'
_I='bps'
_H='ns'
_G='Unsigned32'
_F='on'
_E='off'
_D='Integer32'
_C='read-only'
_B='NEWTEC-TSANALYSER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcTsAnalyser=ModuleIdentity((1,3,6,1,4,1,5835,5,2,1400))
if mibBuilder.loadTexts:ntcTsAnalyser.setRevisions(('2018-04-04 10:00','2017-07-10 12:00','2016-12-05 12:00','2014-09-09 09:00','2013-03-27 10:00','2012-06-28 12:00'))
_NtcTsAnlyObjects_ObjectIdentity=ObjectIdentity
ntcTsAnlyObjects=_NtcTsAnlyObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1400,1))
if mibBuilder.loadTexts:ntcTsAnlyObjects.setStatus(_A)
class _NtcTsAnlyEble_Type(NtcEnable):defaultValue=0
_NtcTsAnlyEble_Type.__name__=_K
_NtcTsAnlyEble_Object=MibScalar
ntcTsAnlyEble=_NtcTsAnlyEble_Object((1,3,6,1,4,1,5835,5,2,1400,1,1),_NtcTsAnlyEble_Type())
ntcTsAnlyEble.setMaxAccess(_L)
if mibBuilder.loadTexts:ntcTsAnlyEble.setStatus(_A)
class _NtcTsAnlyReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('running',0),('reset',1)))
_NtcTsAnlyReset_Type.__name__=_D
_NtcTsAnlyReset_Object=MibScalar
ntcTsAnlyReset=_NtcTsAnlyReset_Object((1,3,6,1,4,1,5835,5,2,1400,1,2),_NtcTsAnlyReset_Type())
ntcTsAnlyReset.setMaxAccess(_L)
if mibBuilder.loadTexts:ntcTsAnlyReset.setStatus(_A)
_NtcTsAnlyEstimatedTsRate_Type=Unsigned32
_NtcTsAnlyEstimatedTsRate_Object=MibScalar
ntcTsAnlyEstimatedTsRate=_NtcTsAnlyEstimatedTsRate_Object((1,3,6,1,4,1,5835,5,2,1400,1,3),_NtcTsAnlyEstimatedTsRate_Type())
ntcTsAnlyEstimatedTsRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyEstimatedTsRate.setStatus(_A)
if mibBuilder.loadTexts:ntcTsAnlyEstimatedTsRate.setUnits(_I)
_NtcTsAnlyPidTable_Object=MibTable
ntcTsAnlyPidTable=_NtcTsAnlyPidTable_Object((1,3,6,1,4,1,5835,5,2,1400,1,4))
if mibBuilder.loadTexts:ntcTsAnlyPidTable.setStatus(_A)
_NtcTsAnlyPidEntry_Object=MibTableRow
ntcTsAnlyPidEntry=_NtcTsAnlyPidEntry_Object((1,3,6,1,4,1,5835,5,2,1400,1,4,1))
ntcTsAnlyPidEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:ntcTsAnlyPidEntry.setStatus(_A)
class _NtcTsAnlyPidPid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8190))
_NtcTsAnlyPidPid_Type.__name__=_G
_NtcTsAnlyPidPid_Object=MibTableColumn
ntcTsAnlyPidPid=_NtcTsAnlyPidPid_Object((1,3,6,1,4,1,5835,5,2,1400,1,4,1,1),_NtcTsAnlyPidPid_Type())
ntcTsAnlyPidPid.setMaxAccess(_J)
if mibBuilder.loadTexts:ntcTsAnlyPidPid.setStatus(_A)
class _NtcTsAnlyPidType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35)));namedValues=NamedValues(*((_N,0),('video',1),('audio',2),(_O,3),(_P,4),('mheg',5),('dsmCc',6),('h2221',7),('mpe',8),(_Q,9),(_R,10),('sdp',11),(_S,12),('ipmp',13),(_T,14),('pat',15),('cat',16),('tsdt',17),(_U,18),(_V,19),(_W,20),(_X,21),(_Y,22),(_Z,23),('rnt',24),(_a,25),(_b,26),('dit',27),('sit',28),('null',29),(_c,30),('pmt',31),(_d,32),('srm',33),('ecm',34),('emm',35)))
_NtcTsAnlyPidType_Type.__name__=_D
_NtcTsAnlyPidType_Object=MibTableColumn
ntcTsAnlyPidType=_NtcTsAnlyPidType_Object((1,3,6,1,4,1,5835,5,2,1400,1,4,1,2),_NtcTsAnlyPidType_Type())
ntcTsAnlyPidType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyPidType.setStatus(_A)
_NtcTsAnlyPidPIDRate_Type=Unsigned32
_NtcTsAnlyPidPIDRate_Object=MibTableColumn
ntcTsAnlyPidPIDRate=_NtcTsAnlyPidPIDRate_Object((1,3,6,1,4,1,5835,5,2,1400,1,4,1,3),_NtcTsAnlyPidPIDRate_Type())
ntcTsAnlyPidPIDRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyPidPIDRate.setStatus(_A)
if mibBuilder.loadTexts:ntcTsAnlyPidPIDRate.setUnits(_I)
class _NtcTsAnlyPidContinuityError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NtcTsAnlyPidContinuityError_Type.__name__=_D
_NtcTsAnlyPidContinuityError_Object=MibTableColumn
ntcTsAnlyPidContinuityError=_NtcTsAnlyPidContinuityError_Object((1,3,6,1,4,1,5835,5,2,1400,1,4,1,4),_NtcTsAnlyPidContinuityError_Type())
ntcTsAnlyPidContinuityError.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyPidContinuityError.setStatus(_A)
class _NtcTsAnlyPidTransportError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NtcTsAnlyPidTransportError_Type.__name__=_D
_NtcTsAnlyPidTransportError_Object=MibTableColumn
ntcTsAnlyPidTransportError=_NtcTsAnlyPidTransportError_Object((1,3,6,1,4,1,5835,5,2,1400,1,4,1,5),_NtcTsAnlyPidTransportError_Type())
ntcTsAnlyPidTransportError.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyPidTransportError.setStatus(_A)
_NtcTsAnlyPidCtuCntErrorCntr_Type=Counter64
_NtcTsAnlyPidCtuCntErrorCntr_Object=MibTableColumn
ntcTsAnlyPidCtuCntErrorCntr=_NtcTsAnlyPidCtuCntErrorCntr_Object((1,3,6,1,4,1,5835,5,2,1400,1,4,1,6),_NtcTsAnlyPidCtuCntErrorCntr_Type())
ntcTsAnlyPidCtuCntErrorCntr.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyPidCtuCntErrorCntr.setStatus(_A)
if mibBuilder.loadTexts:ntcTsAnlyPidCtuCntErrorCntr.setUnits(_e)
_NtcTsAnlyPcrPidTable_Object=MibTable
ntcTsAnlyPcrPidTable=_NtcTsAnlyPcrPidTable_Object((1,3,6,1,4,1,5835,5,2,1400,1,5))
if mibBuilder.loadTexts:ntcTsAnlyPcrPidTable.setStatus(_A)
_NtcTsAnlyPcrPidEntry_Object=MibTableRow
ntcTsAnlyPcrPidEntry=_NtcTsAnlyPcrPidEntry_Object((1,3,6,1,4,1,5835,5,2,1400,1,5,1))
ntcTsAnlyPcrPidEntry.setIndexNames((0,_B,_f))
if mibBuilder.loadTexts:ntcTsAnlyPcrPidEntry.setStatus(_A)
class _NtcTsAnlyPcrPidPid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8190))
_NtcTsAnlyPcrPidPid_Type.__name__=_G
_NtcTsAnlyPcrPidPid_Object=MibTableColumn
ntcTsAnlyPcrPidPid=_NtcTsAnlyPcrPidPid_Object((1,3,6,1,4,1,5835,5,2,1400,1,5,1,1),_NtcTsAnlyPcrPidPid_Type())
ntcTsAnlyPcrPidPid.setMaxAccess(_J)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidPid.setStatus(_A)
class _NtcTsAnlyPcrPidPcrIntervalTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999999))
_NtcTsAnlyPcrPidPcrIntervalTime_Type.__name__=_G
_NtcTsAnlyPcrPidPcrIntervalTime_Object=MibTableColumn
ntcTsAnlyPcrPidPcrIntervalTime=_NtcTsAnlyPcrPidPcrIntervalTime_Object((1,3,6,1,4,1,5835,5,2,1400,1,5,1,2),_NtcTsAnlyPcrPidPcrIntervalTime_Type())
ntcTsAnlyPcrPidPcrIntervalTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidPcrIntervalTime.setStatus(_A)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidPcrIntervalTime.setUnits('ms')
class _NtcTsAnlyPcrPidPcrRepeatError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NtcTsAnlyPcrPidPcrRepeatError_Type.__name__=_D
_NtcTsAnlyPcrPidPcrRepeatError_Object=MibTableColumn
ntcTsAnlyPcrPidPcrRepeatError=_NtcTsAnlyPcrPidPcrRepeatError_Object((1,3,6,1,4,1,5835,5,2,1400,1,5,1,3),_NtcTsAnlyPcrPidPcrRepeatError_Type())
ntcTsAnlyPcrPidPcrRepeatError.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidPcrRepeatError.setStatus(_A)
class _NtcTsAnlyPcrPidPcrAccuracyError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NtcTsAnlyPcrPidPcrAccuracyError_Type.__name__=_D
_NtcTsAnlyPcrPidPcrAccuracyError_Object=MibTableColumn
ntcTsAnlyPcrPidPcrAccuracyError=_NtcTsAnlyPcrPidPcrAccuracyError_Object((1,3,6,1,4,1,5835,5,2,1400,1,5,1,4),_NtcTsAnlyPcrPidPcrAccuracyError_Type())
ntcTsAnlyPcrPidPcrAccuracyError.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidPcrAccuracyError.setStatus(_A)
class _NtcTsAnlyPcrPidMinJitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9999999,9999999))
_NtcTsAnlyPcrPidMinJitter_Type.__name__=_D
_NtcTsAnlyPcrPidMinJitter_Object=MibTableColumn
ntcTsAnlyPcrPidMinJitter=_NtcTsAnlyPcrPidMinJitter_Object((1,3,6,1,4,1,5835,5,2,1400,1,5,1,5),_NtcTsAnlyPcrPidMinJitter_Type())
ntcTsAnlyPcrPidMinJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidMinJitter.setStatus(_A)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidMinJitter.setUnits(_H)
class _NtcTsAnlyPcrPidMaxJitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9999999,9999999))
_NtcTsAnlyPcrPidMaxJitter_Type.__name__=_D
_NtcTsAnlyPcrPidMaxJitter_Object=MibTableColumn
ntcTsAnlyPcrPidMaxJitter=_NtcTsAnlyPcrPidMaxJitter_Object((1,3,6,1,4,1,5835,5,2,1400,1,5,1,6),_NtcTsAnlyPcrPidMaxJitter_Type())
ntcTsAnlyPcrPidMaxJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidMaxJitter.setStatus(_A)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidMaxJitter.setUnits(_H)
class _NtcTsAnlyPcrPidMinHoldJitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9999999,9999999))
_NtcTsAnlyPcrPidMinHoldJitter_Type.__name__=_D
_NtcTsAnlyPcrPidMinHoldJitter_Object=MibTableColumn
ntcTsAnlyPcrPidMinHoldJitter=_NtcTsAnlyPcrPidMinHoldJitter_Object((1,3,6,1,4,1,5835,5,2,1400,1,5,1,7),_NtcTsAnlyPcrPidMinHoldJitter_Type())
ntcTsAnlyPcrPidMinHoldJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidMinHoldJitter.setStatus(_A)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidMinHoldJitter.setUnits(_H)
class _NtcTsAnlyPcrPidMaxHoldJitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9999999,9999999))
_NtcTsAnlyPcrPidMaxHoldJitter_Type.__name__=_D
_NtcTsAnlyPcrPidMaxHoldJitter_Object=MibTableColumn
ntcTsAnlyPcrPidMaxHoldJitter=_NtcTsAnlyPcrPidMaxHoldJitter_Object((1,3,6,1,4,1,5835,5,2,1400,1,5,1,8),_NtcTsAnlyPcrPidMaxHoldJitter_Type())
ntcTsAnlyPcrPidMaxHoldJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidMaxHoldJitter.setStatus(_A)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidMaxHoldJitter.setUnits(_H)
_NtcTsAnlyPcrPidRateOffset_Type=Unsigned32
_NtcTsAnlyPcrPidRateOffset_Object=MibTableColumn
ntcTsAnlyPcrPidRateOffset=_NtcTsAnlyPcrPidRateOffset_Object((1,3,6,1,4,1,5835,5,2,1400,1,5,1,9),_NtcTsAnlyPcrPidRateOffset_Type())
ntcTsAnlyPcrPidRateOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidRateOffset.setStatus(_A)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidRateOffset.setUnits('ppm')
_NtcTsAnlyPcrPidPcrRate_Type=Unsigned32
_NtcTsAnlyPcrPidPcrRate_Object=MibTableColumn
ntcTsAnlyPcrPidPcrRate=_NtcTsAnlyPcrPidPcrRate_Object((1,3,6,1,4,1,5835,5,2,1400,1,5,1,10),_NtcTsAnlyPcrPidPcrRate_Type())
ntcTsAnlyPcrPidPcrRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidPcrRate.setStatus(_A)
if mibBuilder.loadTexts:ntcTsAnlyPcrPidPcrRate.setUnits(_I)
_NtcTsAnlyAlarm_ObjectIdentity=ObjectIdentity
ntcTsAnlyAlarm=_NtcTsAnlyAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1400,1,6))
if mibBuilder.loadTexts:ntcTsAnlyAlarm.setStatus(_A)
_NtcTsAnlyAlmSyncLoss_Type=NtcAlarmState
_NtcTsAnlyAlmSyncLoss_Object=MibScalar
ntcTsAnlyAlmSyncLoss=_NtcTsAnlyAlmSyncLoss_Object((1,3,6,1,4,1,5835,5,2,1400,1,6,1),_NtcTsAnlyAlmSyncLoss_Type())
ntcTsAnlyAlmSyncLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyAlmSyncLoss.setStatus(_A)
_NtcTsAnlyAlmSyncByte_Type=NtcAlarmState
_NtcTsAnlyAlmSyncByte_Object=MibScalar
ntcTsAnlyAlmSyncByte=_NtcTsAnlyAlmSyncByte_Object((1,3,6,1,4,1,5835,5,2,1400,1,6,2),_NtcTsAnlyAlmSyncByte_Type())
ntcTsAnlyAlmSyncByte.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyAlmSyncByte.setStatus(_A)
_NtcTsAnlyAlmPat_Type=NtcAlarmState
_NtcTsAnlyAlmPat_Object=MibScalar
ntcTsAnlyAlmPat=_NtcTsAnlyAlmPat_Object((1,3,6,1,4,1,5835,5,2,1400,1,6,3),_NtcTsAnlyAlmPat_Type())
ntcTsAnlyAlmPat.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyAlmPat.setStatus(_A)
_NtcTsAnlyAlmContinuityCount_Type=NtcAlarmState
_NtcTsAnlyAlmContinuityCount_Object=MibScalar
ntcTsAnlyAlmContinuityCount=_NtcTsAnlyAlmContinuityCount_Object((1,3,6,1,4,1,5835,5,2,1400,1,6,4),_NtcTsAnlyAlmContinuityCount_Type())
ntcTsAnlyAlmContinuityCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyAlmContinuityCount.setStatus(_A)
_NtcTsAnlyAlmTransport_Type=NtcAlarmState
_NtcTsAnlyAlmTransport_Object=MibScalar
ntcTsAnlyAlmTransport=_NtcTsAnlyAlmTransport_Object((1,3,6,1,4,1,5835,5,2,1400,1,6,5),_NtcTsAnlyAlmTransport_Type())
ntcTsAnlyAlmTransport.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyAlmTransport.setStatus(_A)
_NtcTsAnlyAlmPcrRepetition_Type=NtcAlarmState
_NtcTsAnlyAlmPcrRepetition_Object=MibScalar
ntcTsAnlyAlmPcrRepetition=_NtcTsAnlyAlmPcrRepetition_Object((1,3,6,1,4,1,5835,5,2,1400,1,6,6),_NtcTsAnlyAlmPcrRepetition_Type())
ntcTsAnlyAlmPcrRepetition.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyAlmPcrRepetition.setStatus(_A)
_NtcTsAnlyAlmPcrDiscontinuity_Type=NtcAlarmState
_NtcTsAnlyAlmPcrDiscontinuity_Object=MibScalar
ntcTsAnlyAlmPcrDiscontinuity=_NtcTsAnlyAlmPcrDiscontinuity_Object((1,3,6,1,4,1,5835,5,2,1400,1,6,7),_NtcTsAnlyAlmPcrDiscontinuity_Type())
ntcTsAnlyAlmPcrDiscontinuity.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyAlmPcrDiscontinuity.setStatus(_A)
_NtcTsAnlyAlmPcrAccuracy_Type=NtcAlarmState
_NtcTsAnlyAlmPcrAccuracy_Object=MibScalar
ntcTsAnlyAlmPcrAccuracy=_NtcTsAnlyAlmPcrAccuracy_Object((1,3,6,1,4,1,5835,5,2,1400,1,6,8),_NtcTsAnlyAlmPcrAccuracy_Type())
ntcTsAnlyAlmPcrAccuracy.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyAlmPcrAccuracy.setStatus(_A)
_NtcTsAnlyEPidTable_Object=MibTable
ntcTsAnlyEPidTable=_NtcTsAnlyEPidTable_Object((1,3,6,1,4,1,5835,5,2,1400,1,7))
if mibBuilder.loadTexts:ntcTsAnlyEPidTable.setStatus(_A)
_NtcTsAnlyEPidEntry_Object=MibTableRow
ntcTsAnlyEPidEntry=_NtcTsAnlyEPidEntry_Object((1,3,6,1,4,1,5835,5,2,1400,1,7,1))
ntcTsAnlyEPidEntry.setIndexNames((0,_B,_g))
if mibBuilder.loadTexts:ntcTsAnlyEPidEntry.setStatus(_A)
class _NtcTsAnlyEPidPid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8190))
_NtcTsAnlyEPidPid_Type.__name__=_G
_NtcTsAnlyEPidPid_Object=MibTableColumn
ntcTsAnlyEPidPid=_NtcTsAnlyEPidPid_Object((1,3,6,1,4,1,5835,5,2,1400,1,7,1,1),_NtcTsAnlyEPidPid_Type())
ntcTsAnlyEPidPid.setMaxAccess(_J)
if mibBuilder.loadTexts:ntcTsAnlyEPidPid.setStatus(_A)
class _NtcTsAnlyEPidType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35)));namedValues=NamedValues(*((_N,0),('video',1),('audio',2),(_O,3),(_P,4),('mheg',5),('dsmCc',6),('h2221',7),('mpe',8),(_Q,9),(_R,10),('sdp',11),(_S,12),('ipmp',13),(_T,14),('pat',15),('cat',16),('tsdt',17),(_U,18),(_V,19),(_W,20),(_X,21),(_Y,22),(_Z,23),('rnt',24),(_a,25),(_b,26),('dit',27),('sit',28),('null',29),(_c,30),('pmt',31),(_d,32),('srm',33),('ecm',34),('emm',35)))
_NtcTsAnlyEPidType_Type.__name__=_D
_NtcTsAnlyEPidType_Object=MibTableColumn
ntcTsAnlyEPidType=_NtcTsAnlyEPidType_Object((1,3,6,1,4,1,5835,5,2,1400,1,7,1,2),_NtcTsAnlyEPidType_Type())
ntcTsAnlyEPidType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyEPidType.setStatus(_A)
_NtcTsAnlyEPidCtuCntErrorCntr_Type=Counter64
_NtcTsAnlyEPidCtuCntErrorCntr_Object=MibTableColumn
ntcTsAnlyEPidCtuCntErrorCntr=_NtcTsAnlyEPidCtuCntErrorCntr_Object((1,3,6,1,4,1,5835,5,2,1400,1,7,1,3),_NtcTsAnlyEPidCtuCntErrorCntr_Type())
ntcTsAnlyEPidCtuCntErrorCntr.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyEPidCtuCntErrorCntr.setStatus(_A)
if mibBuilder.loadTexts:ntcTsAnlyEPidCtuCntErrorCntr.setUnits(_e)
class _NtcTsAnlyEPidContinuityError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NtcTsAnlyEPidContinuityError_Type.__name__=_D
_NtcTsAnlyEPidContinuityError_Object=MibTableColumn
ntcTsAnlyEPidContinuityError=_NtcTsAnlyEPidContinuityError_Object((1,3,6,1,4,1,5835,5,2,1400,1,7,1,4),_NtcTsAnlyEPidContinuityError_Type())
ntcTsAnlyEPidContinuityError.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyEPidContinuityError.setStatus(_A)
class _NtcTsAnlyEPidTransportError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NtcTsAnlyEPidTransportError_Type.__name__=_D
_NtcTsAnlyEPidTransportError_Object=MibTableColumn
ntcTsAnlyEPidTransportError=_NtcTsAnlyEPidTransportError_Object((1,3,6,1,4,1,5835,5,2,1400,1,7,1,5),_NtcTsAnlyEPidTransportError_Type())
ntcTsAnlyEPidTransportError.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsAnlyEPidTransportError.setStatus(_A)
_NtcTsAnlyConformance_ObjectIdentity=ObjectIdentity
ntcTsAnlyConformance=_NtcTsAnlyConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1400,2))
if mibBuilder.loadTexts:ntcTsAnlyConformance.setStatus(_A)
_NtcTsAnlyConfCompliance_ObjectIdentity=ObjectIdentity
ntcTsAnlyConfCompliance=_NtcTsAnlyConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1400,2,1))
if mibBuilder.loadTexts:ntcTsAnlyConfCompliance.setStatus(_A)
_NtcTsAnlyConfGroup_ObjectIdentity=ObjectIdentity
ntcTsAnlyConfGroup=_NtcTsAnlyConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1400,2,2))
if mibBuilder.loadTexts:ntcTsAnlyConfGroup.setStatus(_A)
ntcTsAnlyConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,1400,2,2,1))
ntcTsAnlyConfGrpV1Standard.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:ntcTsAnlyConfGrpV1Standard.setStatus(_A)
ntcTsAnlyConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,1400,2,1,1))
ntcTsAnlyConfCompV1Standard.setObjects((_B,_AA))
if mibBuilder.loadTexts:ntcTsAnlyConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcTsAnalyser':ntcTsAnalyser,'ntcTsAnlyObjects':ntcTsAnlyObjects,_h:ntcTsAnlyEble,_i:ntcTsAnlyReset,_j:ntcTsAnlyEstimatedTsRate,'ntcTsAnlyPidTable':ntcTsAnlyPidTable,'ntcTsAnlyPidEntry':ntcTsAnlyPidEntry,_M:ntcTsAnlyPidPid,_k:ntcTsAnlyPidType,_l:ntcTsAnlyPidPIDRate,_m:ntcTsAnlyPidContinuityError,_n:ntcTsAnlyPidTransportError,_o:ntcTsAnlyPidCtuCntErrorCntr,'ntcTsAnlyPcrPidTable':ntcTsAnlyPcrPidTable,'ntcTsAnlyPcrPidEntry':ntcTsAnlyPcrPidEntry,_f:ntcTsAnlyPcrPidPid,_p:ntcTsAnlyPcrPidPcrIntervalTime,_q:ntcTsAnlyPcrPidPcrRepeatError,_r:ntcTsAnlyPcrPidPcrAccuracyError,_s:ntcTsAnlyPcrPidMinJitter,_t:ntcTsAnlyPcrPidMaxJitter,_u:ntcTsAnlyPcrPidMinHoldJitter,_v:ntcTsAnlyPcrPidMaxHoldJitter,_w:ntcTsAnlyPcrPidRateOffset,_x:ntcTsAnlyPcrPidPcrRate,'ntcTsAnlyAlarm':ntcTsAnlyAlarm,_y:ntcTsAnlyAlmSyncLoss,_z:ntcTsAnlyAlmSyncByte,_A0:ntcTsAnlyAlmPat,_A1:ntcTsAnlyAlmContinuityCount,_A2:ntcTsAnlyAlmTransport,_A3:ntcTsAnlyAlmPcrRepetition,_A4:ntcTsAnlyAlmPcrDiscontinuity,_A5:ntcTsAnlyAlmPcrAccuracy,'ntcTsAnlyEPidTable':ntcTsAnlyEPidTable,'ntcTsAnlyEPidEntry':ntcTsAnlyEPidEntry,_g:ntcTsAnlyEPidPid,_A6:ntcTsAnlyEPidType,_A7:ntcTsAnlyEPidCtuCntErrorCntr,_A8:ntcTsAnlyEPidContinuityError,_A9:ntcTsAnlyEPidTransportError,'ntcTsAnlyConformance':ntcTsAnlyConformance,'ntcTsAnlyConfCompliance':ntcTsAnlyConfCompliance,'ntcTsAnlyConfCompV1Standard':ntcTsAnlyConfCompV1Standard,'ntcTsAnlyConfGroup':ntcTsAnlyConfGroup,_AA:ntcTsAnlyConfGrpV1Standard})