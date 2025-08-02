_Aq='juniNtpSysClockGroup2'
_Ap='juniNtpClockOffSetLimitCrossed'
_Ao='juniNtpFirstSystemClockSet'
_An='juniNtpTimeServerSynDown'
_Am='juniNtpTimeServerSynUp'
_Al='juniNtpTimeSynDown'
_Ak='juniNtpTimeSynUp'
_Aj='juniNtpFrequencyCalibrationEnd'
_Ai='juniNtpFrequencyCalibrationStart'
_Ah='juniNtpPeerLastUpdateTime'
_Ag='juniNtpSysClockFrequencyErrorNew'
_Af='juniNtpSysClockOffsetErrorNew'
_Ae='juniNtpRouterAccessGroupQueryOnly'
_Ad='juniNtpRouterAccessGroupServeOnly'
_Ac='juniNtpRouterAccessGroupServe'
_Ab='juniNtpRouterAccessGroupPeer'
_Aa='juniNtpServerStratumNumber'
_AZ='juniNtpServerAdminStatus'
_AY='juniNtpClientIfIsBroadcastClient'
_AX='juniNtpClientIfDisable'
_AW='juniNtpClientBroadcastDelay'
_AV='juniNtpClientPacketSourceIfIndex'
_AU='juniNtpClientSystemRouterIndex'
_AT='juniNtpClientAdminStatus'
_AS='juniSysClockDstRecurStopMinute'
_AR='juniSysClockDstRecurStopHour'
_AQ='juniSysClockDstRecurStopDay'
_AP='juniSysClockDstRecurStopWeek'
_AO='juniSysClockDstRecurStopMonth'
_AN='juniSysClockDstRecurStartMinute'
_AM='juniSysClockDstRecurStartHour'
_AL='juniSysClockDstRecurStartDay'
_AK='juniSysClockDstRecurStartWeek'
_AJ='juniSysClockDstRecurStartMonth'
_AI='juniSysClockDstAbsoluteStopTime'
_AH='juniSysClockDstAbsoluteStartTime'
_AG='juniSysClockDstStatus'
_AF='juniSysClockDstOffset'
_AE='juniSysClockDstName'
_AD='juniSysClockTimeZoneName'
_AC='juniSysClockDateAndTime'
_AB='juniNtpPeerFilterIndex'
_AA='juniNtpClientIfIfIndex'
_A9='JuniEnable'
_A8='juniNtpNotificationGroup'
_A7='juniNtpSysClockGroup'
_A6='juniNtpPeerCfgRowStatus'
_A5='juniNtpPeerCfgPacketSourceIfIndex'
_A4='juniNtpPeerCfgNtpVersion'
_A3='juniNtpPeerFilterDispersion'
_A2='juniNtpPeerFilterDelay'
_A1='juniNtpPeerFilterOffset'
_A0='juniNtpPeerRequestTime'
_z='juniNtpPeerTransmitTime'
_y='juniNtpPeerReceiveTime'
_x='juniNtpPeerRootTimeUpdateServer'
_w='juniNtpPeerRootTime'
_v='juniNtpPeerRootSyncDistance'
_u='juniNtpPeerRootDispersion'
_t='juniNtpPeerRootDelay'
_s='juniNtpPeerPrecision'
_r='juniNtpPeerReachability'
_q='juniNtpPeerOffsetError'
_p='juniNtpPeerDispersion'
_o='juniNtpPeerDelay'
_n='juniNtpPeerPollingInterval'
_m='juniNtpPeerPolledInterval'
_l='juniNtpPeerBroadcastInterval'
_k='juniNtpPeerAssociationMode'
_j='juniNtpPeerStratumNumber'
_i='juniNtpPeerState'
_h='juniNtpSysClockLastUpdateServer'
_g='juniNtpSysClockLastUpdateTime'
_f='juniNtpSysClockStratumNumber'
_e='juniNtpSysClockRootDispersion'
_d='juniNtpSysClockRootDelay'
_c='deprecated'
_b='JuniSysClockMinute'
_a='JuniSysClockHour'
_Z='JuniSysClockDayOfTheWeek'
_Y='JuniSysClockWeekOfTheMonth'
_X='JuniSysClockMonth'
_W='OctetString'
_V='juniNtpAccessGroupGroup'
_U='juniNtpPeersGroup'
_T='juniNtpServerGroup'
_S='juniNtpClientGroup'
_R='juniSysClockDstGroup'
_Q='juniSysClockTimeGroup'
_P='obsolete'
_O='juniNtpPeerCfgIpAddress'
_N='not-accessible'
_M='juniNtpClientIfRouterIndex'
_L='juniNtpPeerCfgIsPreferred'
_K='juniNtpSysClockFrequencyError'
_J='juniNtpSysClockOffsetError'
_I='juniNtpSysClockState'
_H='DisplayString'
_G='read-create'
_F='Integer32'
_E='seconds'
_D='read-write'
_C='read-only'
_B='current'
_A='Juniper-System-Clock-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_W,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniEnable,=mibBuilder.importSymbols('Juniper-TC',_A9)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_H,'PhysAddress','RowStatus','TextualConvention','TruthValue')
juniSysClockMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,56))
if mibBuilder.loadTexts:juniSysClockMIB.setRevisions(('2014-09-15 14:00','2007-03-22 14:00','2005-12-14 14:01','2003-09-15 14:01','2003-09-12 13:37','2002-04-04 14:56'))
class JuniSysClockMonth(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('january',1),('february',2),('march',3),('april',4),('may',5),('june',6),('july',7),('august',8),('september',9),('october',10),('november',11),('december',12)))
class JuniSysClockWeekOfTheMonth(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('weekFirst',0),('weekOne',1),('weekTwo',2),('weekThree',3),('weekFour',4),('weekFive',5),('weekLast',6)))
class JuniSysClockDayOfTheWeek(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('sunday',0),('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6)))
class JuniSysClockHour(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
class JuniSysClockMinute(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
class JuniNtpTimeStamp(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,21))
class JuniNtpClockSignedTime(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
class JuniNtpClockUnsignedTime(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_JuniSysClockObjects_ObjectIdentity=ObjectIdentity
juniSysClockObjects=_JuniSysClockObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,56,1))
_JuniSysClockTime_ObjectIdentity=ObjectIdentity
juniSysClockTime=_JuniSysClockTime_ObjectIdentity((1,3,6,1,4,1,4874,2,2,56,1,1))
_JuniSysClockDateAndTime_Type=DateAndTime
_JuniSysClockDateAndTime_Object=MibScalar
juniSysClockDateAndTime=_JuniSysClockDateAndTime_Object((1,3,6,1,4,1,4874,2,2,56,1,1,1),_JuniSysClockDateAndTime_Type())
juniSysClockDateAndTime.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockDateAndTime.setStatus(_B)
class _JuniSysClockTimeZoneName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_JuniSysClockTimeZoneName_Type.__name__=_H
_JuniSysClockTimeZoneName_Object=MibScalar
juniSysClockTimeZoneName=_JuniSysClockTimeZoneName_Object((1,3,6,1,4,1,4874,2,2,56,1,1,2),_JuniSysClockTimeZoneName_Type())
juniSysClockTimeZoneName.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockTimeZoneName.setStatus(_B)
_JuniSysClockDst_ObjectIdentity=ObjectIdentity
juniSysClockDst=_JuniSysClockDst_ObjectIdentity((1,3,6,1,4,1,4874,2,2,56,1,2))
class _JuniSysClockDstName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_JuniSysClockDstName_Type.__name__=_H
_JuniSysClockDstName_Object=MibScalar
juniSysClockDstName=_JuniSysClockDstName_Object((1,3,6,1,4,1,4874,2,2,56,1,2,1),_JuniSysClockDstName_Type())
juniSysClockDstName.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockDstName.setStatus(_B)
class _JuniSysClockDstOffset_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_JuniSysClockDstOffset_Type.__name__=_F
_JuniSysClockDstOffset_Object=MibScalar
juniSysClockDstOffset=_JuniSysClockDstOffset_Object((1,3,6,1,4,1,4874,2,2,56,1,2,2),_JuniSysClockDstOffset_Type())
juniSysClockDstOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockDstOffset.setStatus(_B)
if mibBuilder.loadTexts:juniSysClockDstOffset.setUnits('minutes')
class _JuniSysClockDstStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('off',0),('recurrent',1),('absolute',2),('recognizedUS',3)))
_JuniSysClockDstStatus_Type.__name__=_F
_JuniSysClockDstStatus_Object=MibScalar
juniSysClockDstStatus=_JuniSysClockDstStatus_Object((1,3,6,1,4,1,4874,2,2,56,1,2,3),_JuniSysClockDstStatus_Type())
juniSysClockDstStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockDstStatus.setStatus(_B)
_JuniSysClockDstAbsoluteStartTime_Type=DateAndTime
_JuniSysClockDstAbsoluteStartTime_Object=MibScalar
juniSysClockDstAbsoluteStartTime=_JuniSysClockDstAbsoluteStartTime_Object((1,3,6,1,4,1,4874,2,2,56,1,2,4),_JuniSysClockDstAbsoluteStartTime_Type())
juniSysClockDstAbsoluteStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockDstAbsoluteStartTime.setStatus(_B)
_JuniSysClockDstAbsoluteStopTime_Type=DateAndTime
_JuniSysClockDstAbsoluteStopTime_Object=MibScalar
juniSysClockDstAbsoluteStopTime=_JuniSysClockDstAbsoluteStopTime_Object((1,3,6,1,4,1,4874,2,2,56,1,2,5),_JuniSysClockDstAbsoluteStopTime_Type())
juniSysClockDstAbsoluteStopTime.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockDstAbsoluteStopTime.setStatus(_B)
class _JuniSysClockDstRecurStartMonth_Type(JuniSysClockMonth):defaultValue=3
_JuniSysClockDstRecurStartMonth_Type.__name__=_X
_JuniSysClockDstRecurStartMonth_Object=MibScalar
juniSysClockDstRecurStartMonth=_JuniSysClockDstRecurStartMonth_Object((1,3,6,1,4,1,4874,2,2,56,1,2,6),_JuniSysClockDstRecurStartMonth_Type())
juniSysClockDstRecurStartMonth.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockDstRecurStartMonth.setStatus(_B)
class _JuniSysClockDstRecurStartWeek_Type(JuniSysClockWeekOfTheMonth):defaultValue=2
_JuniSysClockDstRecurStartWeek_Type.__name__=_Y
_JuniSysClockDstRecurStartWeek_Object=MibScalar
juniSysClockDstRecurStartWeek=_JuniSysClockDstRecurStartWeek_Object((1,3,6,1,4,1,4874,2,2,56,1,2,7),_JuniSysClockDstRecurStartWeek_Type())
juniSysClockDstRecurStartWeek.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockDstRecurStartWeek.setStatus(_B)
class _JuniSysClockDstRecurStartDay_Type(JuniSysClockDayOfTheWeek):defaultValue=0
_JuniSysClockDstRecurStartDay_Type.__name__=_Z
_JuniSysClockDstRecurStartDay_Object=MibScalar
juniSysClockDstRecurStartDay=_JuniSysClockDstRecurStartDay_Object((1,3,6,1,4,1,4874,2,2,56,1,2,8),_JuniSysClockDstRecurStartDay_Type())
juniSysClockDstRecurStartDay.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockDstRecurStartDay.setStatus(_B)
class _JuniSysClockDstRecurStartHour_Type(JuniSysClockHour):defaultValue=1
_JuniSysClockDstRecurStartHour_Type.__name__=_a
_JuniSysClockDstRecurStartHour_Object=MibScalar
juniSysClockDstRecurStartHour=_JuniSysClockDstRecurStartHour_Object((1,3,6,1,4,1,4874,2,2,56,1,2,9),_JuniSysClockDstRecurStartHour_Type())
juniSysClockDstRecurStartHour.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockDstRecurStartHour.setStatus(_B)
class _JuniSysClockDstRecurStartMinute_Type(JuniSysClockMinute):defaultValue=0
_JuniSysClockDstRecurStartMinute_Type.__name__=_b
_JuniSysClockDstRecurStartMinute_Object=MibScalar
juniSysClockDstRecurStartMinute=_JuniSysClockDstRecurStartMinute_Object((1,3,6,1,4,1,4874,2,2,56,1,2,10),_JuniSysClockDstRecurStartMinute_Type())
juniSysClockDstRecurStartMinute.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockDstRecurStartMinute.setStatus(_B)
class _JuniSysClockDstRecurStopMonth_Type(JuniSysClockMonth):defaultValue=11
_JuniSysClockDstRecurStopMonth_Type.__name__=_X
_JuniSysClockDstRecurStopMonth_Object=MibScalar
juniSysClockDstRecurStopMonth=_JuniSysClockDstRecurStopMonth_Object((1,3,6,1,4,1,4874,2,2,56,1,2,11),_JuniSysClockDstRecurStopMonth_Type())
juniSysClockDstRecurStopMonth.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockDstRecurStopMonth.setStatus(_B)
class _JuniSysClockDstRecurStopWeek_Type(JuniSysClockWeekOfTheMonth):defaultValue=0
_JuniSysClockDstRecurStopWeek_Type.__name__=_Y
_JuniSysClockDstRecurStopWeek_Object=MibScalar
juniSysClockDstRecurStopWeek=_JuniSysClockDstRecurStopWeek_Object((1,3,6,1,4,1,4874,2,2,56,1,2,12),_JuniSysClockDstRecurStopWeek_Type())
juniSysClockDstRecurStopWeek.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockDstRecurStopWeek.setStatus(_B)
class _JuniSysClockDstRecurStopDay_Type(JuniSysClockDayOfTheWeek):defaultValue=0
_JuniSysClockDstRecurStopDay_Type.__name__=_Z
_JuniSysClockDstRecurStopDay_Object=MibScalar
juniSysClockDstRecurStopDay=_JuniSysClockDstRecurStopDay_Object((1,3,6,1,4,1,4874,2,2,56,1,2,13),_JuniSysClockDstRecurStopDay_Type())
juniSysClockDstRecurStopDay.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockDstRecurStopDay.setStatus(_B)
class _JuniSysClockDstRecurStopHour_Type(JuniSysClockHour):defaultValue=2
_JuniSysClockDstRecurStopHour_Type.__name__=_a
_JuniSysClockDstRecurStopHour_Object=MibScalar
juniSysClockDstRecurStopHour=_JuniSysClockDstRecurStopHour_Object((1,3,6,1,4,1,4874,2,2,56,1,2,14),_JuniSysClockDstRecurStopHour_Type())
juniSysClockDstRecurStopHour.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockDstRecurStopHour.setStatus(_B)
class _JuniSysClockDstRecurStopMinute_Type(JuniSysClockMinute):defaultValue=0
_JuniSysClockDstRecurStopMinute_Type.__name__=_b
_JuniSysClockDstRecurStopMinute_Object=MibScalar
juniSysClockDstRecurStopMinute=_JuniSysClockDstRecurStopMinute_Object((1,3,6,1,4,1,4874,2,2,56,1,2,15),_JuniSysClockDstRecurStopMinute_Type())
juniSysClockDstRecurStopMinute.setMaxAccess(_D)
if mibBuilder.loadTexts:juniSysClockDstRecurStopMinute.setStatus(_B)
_JuniNtpObjects_ObjectIdentity=ObjectIdentity
juniNtpObjects=_JuniNtpObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,56,2))
_JuniNtpTraps_ObjectIdentity=ObjectIdentity
juniNtpTraps=_JuniNtpTraps_ObjectIdentity((1,3,6,1,4,1,4874,2,2,56,2,0))
_JuniNtpSysClock_ObjectIdentity=ObjectIdentity
juniNtpSysClock=_JuniNtpSysClock_ObjectIdentity((1,3,6,1,4,1,4874,2,2,56,2,1))
class _JuniNtpSysClockState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('neverFrequencyCalibrated',0),('frequencyCalibrated',1),('setToServerTime',2),('frequencyCalibrationIsGoingOn',3),('synchronized',4),('spikeDetected',5)))
_JuniNtpSysClockState_Type.__name__=_F
_JuniNtpSysClockState_Object=MibScalar
juniNtpSysClockState=_JuniNtpSysClockState_Object((1,3,6,1,4,1,4874,2,2,56,2,1,1),_JuniNtpSysClockState_Type())
juniNtpSysClockState.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpSysClockState.setStatus(_B)
_JuniNtpSysClockOffsetError_Type=JuniNtpClockSignedTime
_JuniNtpSysClockOffsetError_Object=MibScalar
juniNtpSysClockOffsetError=_JuniNtpSysClockOffsetError_Object((1,3,6,1,4,1,4874,2,2,56,2,1,2),_JuniNtpSysClockOffsetError_Type())
juniNtpSysClockOffsetError.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpSysClockOffsetError.setStatus(_c)
if mibBuilder.loadTexts:juniNtpSysClockOffsetError.setUnits(_E)
_JuniNtpSysClockFrequencyError_Type=Integer32
_JuniNtpSysClockFrequencyError_Object=MibScalar
juniNtpSysClockFrequencyError=_JuniNtpSysClockFrequencyError_Object((1,3,6,1,4,1,4874,2,2,56,2,1,3),_JuniNtpSysClockFrequencyError_Type())
juniNtpSysClockFrequencyError.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpSysClockFrequencyError.setStatus(_c)
if mibBuilder.loadTexts:juniNtpSysClockFrequencyError.setUnits('ppm')
_JuniNtpSysClockRootDelay_Type=JuniNtpClockSignedTime
_JuniNtpSysClockRootDelay_Object=MibScalar
juniNtpSysClockRootDelay=_JuniNtpSysClockRootDelay_Object((1,3,6,1,4,1,4874,2,2,56,2,1,4),_JuniNtpSysClockRootDelay_Type())
juniNtpSysClockRootDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpSysClockRootDelay.setStatus(_B)
if mibBuilder.loadTexts:juniNtpSysClockRootDelay.setUnits(_E)
_JuniNtpSysClockRootDispersion_Type=JuniNtpClockUnsignedTime
_JuniNtpSysClockRootDispersion_Object=MibScalar
juniNtpSysClockRootDispersion=_JuniNtpSysClockRootDispersion_Object((1,3,6,1,4,1,4874,2,2,56,2,1,5),_JuniNtpSysClockRootDispersion_Type())
juniNtpSysClockRootDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpSysClockRootDispersion.setStatus(_B)
if mibBuilder.loadTexts:juniNtpSysClockRootDispersion.setUnits(_E)
class _JuniNtpSysClockStratumNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_JuniNtpSysClockStratumNumber_Type.__name__=_F
_JuniNtpSysClockStratumNumber_Object=MibScalar
juniNtpSysClockStratumNumber=_JuniNtpSysClockStratumNumber_Object((1,3,6,1,4,1,4874,2,2,56,2,1,6),_JuniNtpSysClockStratumNumber_Type())
juniNtpSysClockStratumNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpSysClockStratumNumber.setStatus(_B)
_JuniNtpSysClockLastUpdateTime_Type=JuniNtpTimeStamp
_JuniNtpSysClockLastUpdateTime_Object=MibScalar
juniNtpSysClockLastUpdateTime=_JuniNtpSysClockLastUpdateTime_Object((1,3,6,1,4,1,4874,2,2,56,2,1,7),_JuniNtpSysClockLastUpdateTime_Type())
juniNtpSysClockLastUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpSysClockLastUpdateTime.setStatus(_B)
if mibBuilder.loadTexts:juniNtpSysClockLastUpdateTime.setUnits(_E)
_JuniNtpSysClockLastUpdateServer_Type=IpAddress
_JuniNtpSysClockLastUpdateServer_Object=MibScalar
juniNtpSysClockLastUpdateServer=_JuniNtpSysClockLastUpdateServer_Object((1,3,6,1,4,1,4874,2,2,56,2,1,8),_JuniNtpSysClockLastUpdateServer_Type())
juniNtpSysClockLastUpdateServer.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpSysClockLastUpdateServer.setStatus(_B)
class _JuniNtpSysClockOffsetErrorNew_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_JuniNtpSysClockOffsetErrorNew_Type.__name__=_H
_JuniNtpSysClockOffsetErrorNew_Object=MibScalar
juniNtpSysClockOffsetErrorNew=_JuniNtpSysClockOffsetErrorNew_Object((1,3,6,1,4,1,4874,2,2,56,2,1,9),_JuniNtpSysClockOffsetErrorNew_Type())
juniNtpSysClockOffsetErrorNew.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpSysClockOffsetErrorNew.setStatus(_B)
if mibBuilder.loadTexts:juniNtpSysClockOffsetErrorNew.setUnits(_E)
class _JuniNtpSysClockFrequencyErrorNew_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_JuniNtpSysClockFrequencyErrorNew_Type.__name__=_H
_JuniNtpSysClockFrequencyErrorNew_Object=MibScalar
juniNtpSysClockFrequencyErrorNew=_JuniNtpSysClockFrequencyErrorNew_Object((1,3,6,1,4,1,4874,2,2,56,2,1,10),_JuniNtpSysClockFrequencyErrorNew_Type())
juniNtpSysClockFrequencyErrorNew.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpSysClockFrequencyErrorNew.setStatus(_B)
if mibBuilder.loadTexts:juniNtpSysClockFrequencyErrorNew.setUnits('ppm')
_JuniNtpClient_ObjectIdentity=ObjectIdentity
juniNtpClient=_JuniNtpClient_ObjectIdentity((1,3,6,1,4,1,4874,2,2,56,2,2))
class _JuniNtpClientAdminStatus_Type(JuniEnable):defaultValue=0
_JuniNtpClientAdminStatus_Type.__name__=_A9
_JuniNtpClientAdminStatus_Object=MibScalar
juniNtpClientAdminStatus=_JuniNtpClientAdminStatus_Object((1,3,6,1,4,1,4874,2,2,56,2,2,1),_JuniNtpClientAdminStatus_Type())
juniNtpClientAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniNtpClientAdminStatus.setStatus(_B)
_JuniNtpClientSystemRouterIndex_Type=Unsigned32
_JuniNtpClientSystemRouterIndex_Object=MibScalar
juniNtpClientSystemRouterIndex=_JuniNtpClientSystemRouterIndex_Object((1,3,6,1,4,1,4874,2,2,56,2,2,2),_JuniNtpClientSystemRouterIndex_Type())
juniNtpClientSystemRouterIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpClientSystemRouterIndex.setStatus(_B)
class _JuniNtpClientPacketSourceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniNtpClientPacketSourceIfIndex_Type.__name__=_F
_JuniNtpClientPacketSourceIfIndex_Object=MibScalar
juniNtpClientPacketSourceIfIndex=_JuniNtpClientPacketSourceIfIndex_Object((1,3,6,1,4,1,4874,2,2,56,2,2,3),_JuniNtpClientPacketSourceIfIndex_Type())
juniNtpClientPacketSourceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:juniNtpClientPacketSourceIfIndex.setStatus(_B)
class _JuniNtpClientBroadcastDelay_Type(Integer32):defaultValue=3000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_JuniNtpClientBroadcastDelay_Type.__name__=_F
_JuniNtpClientBroadcastDelay_Object=MibScalar
juniNtpClientBroadcastDelay=_JuniNtpClientBroadcastDelay_Object((1,3,6,1,4,1,4874,2,2,56,2,2,4),_JuniNtpClientBroadcastDelay_Type())
juniNtpClientBroadcastDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:juniNtpClientBroadcastDelay.setStatus(_B)
if mibBuilder.loadTexts:juniNtpClientBroadcastDelay.setUnits('microseconds')
_JuniNtpClientIfTable_Object=MibTable
juniNtpClientIfTable=_JuniNtpClientIfTable_Object((1,3,6,1,4,1,4874,2,2,56,2,2,5))
if mibBuilder.loadTexts:juniNtpClientIfTable.setStatus(_B)
_JuniNtpClientIfEntry_Object=MibTableRow
juniNtpClientIfEntry=_JuniNtpClientIfEntry_Object((1,3,6,1,4,1,4874,2,2,56,2,2,5,1))
juniNtpClientIfEntry.setIndexNames((0,_A,_M),(0,_A,_AA))
if mibBuilder.loadTexts:juniNtpClientIfEntry.setStatus(_B)
_JuniNtpClientIfRouterIndex_Type=Unsigned32
_JuniNtpClientIfRouterIndex_Object=MibTableColumn
juniNtpClientIfRouterIndex=_JuniNtpClientIfRouterIndex_Object((1,3,6,1,4,1,4874,2,2,56,2,2,5,1,1),_JuniNtpClientIfRouterIndex_Type())
juniNtpClientIfRouterIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:juniNtpClientIfRouterIndex.setStatus(_B)
class _JuniNtpClientIfIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniNtpClientIfIfIndex_Type.__name__=_F
_JuniNtpClientIfIfIndex_Object=MibTableColumn
juniNtpClientIfIfIndex=_JuniNtpClientIfIfIndex_Object((1,3,6,1,4,1,4874,2,2,56,2,2,5,1,2),_JuniNtpClientIfIfIndex_Type())
juniNtpClientIfIfIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:juniNtpClientIfIfIndex.setStatus(_B)
_JuniNtpClientIfDisable_Type=TruthValue
_JuniNtpClientIfDisable_Object=MibTableColumn
juniNtpClientIfDisable=_JuniNtpClientIfDisable_Object((1,3,6,1,4,1,4874,2,2,56,2,2,5,1,3),_JuniNtpClientIfDisable_Type())
juniNtpClientIfDisable.setMaxAccess(_G)
if mibBuilder.loadTexts:juniNtpClientIfDisable.setStatus(_B)
_JuniNtpClientIfIsBroadcastClient_Type=TruthValue
_JuniNtpClientIfIsBroadcastClient_Object=MibTableColumn
juniNtpClientIfIsBroadcastClient=_JuniNtpClientIfIsBroadcastClient_Object((1,3,6,1,4,1,4874,2,2,56,2,2,5,1,4),_JuniNtpClientIfIsBroadcastClient_Type())
juniNtpClientIfIsBroadcastClient.setMaxAccess(_G)
if mibBuilder.loadTexts:juniNtpClientIfIsBroadcastClient.setStatus(_B)
_JuniNtpClientIfIsBroadcastServer_Type=TruthValue
_JuniNtpClientIfIsBroadcastServer_Object=MibTableColumn
juniNtpClientIfIsBroadcastServer=_JuniNtpClientIfIsBroadcastServer_Object((1,3,6,1,4,1,4874,2,2,56,2,2,5,1,5),_JuniNtpClientIfIsBroadcastServer_Type())
juniNtpClientIfIsBroadcastServer.setMaxAccess(_G)
if mibBuilder.loadTexts:juniNtpClientIfIsBroadcastServer.setStatus(_B)
class _JuniNtpClientIfIsBroadcastServerVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_JuniNtpClientIfIsBroadcastServerVersion_Type.__name__=_F
_JuniNtpClientIfIsBroadcastServerVersion_Object=MibTableColumn
juniNtpClientIfIsBroadcastServerVersion=_JuniNtpClientIfIsBroadcastServerVersion_Object((1,3,6,1,4,1,4874,2,2,56,2,2,5,1,6),_JuniNtpClientIfIsBroadcastServerVersion_Type())
juniNtpClientIfIsBroadcastServerVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:juniNtpClientIfIsBroadcastServerVersion.setStatus(_B)
class _JuniNtpClientIfIsBroadcastServerDelay_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,17))
_JuniNtpClientIfIsBroadcastServerDelay_Type.__name__=_F
_JuniNtpClientIfIsBroadcastServerDelay_Object=MibTableColumn
juniNtpClientIfIsBroadcastServerDelay=_JuniNtpClientIfIsBroadcastServerDelay_Object((1,3,6,1,4,1,4874,2,2,56,2,2,5,1,7),_JuniNtpClientIfIsBroadcastServerDelay_Type())
juniNtpClientIfIsBroadcastServerDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:juniNtpClientIfIsBroadcastServerDelay.setStatus(_B)
_JuniNtpServer_ObjectIdentity=ObjectIdentity
juniNtpServer=_JuniNtpServer_ObjectIdentity((1,3,6,1,4,1,4874,2,2,56,2,3))
class _JuniNtpServerStratumNumber_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_JuniNtpServerStratumNumber_Type.__name__=_F
_JuniNtpServerStratumNumber_Object=MibScalar
juniNtpServerStratumNumber=_JuniNtpServerStratumNumber_Object((1,3,6,1,4,1,4874,2,2,56,2,3,1),_JuniNtpServerStratumNumber_Type())
juniNtpServerStratumNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:juniNtpServerStratumNumber.setStatus(_B)
_JuniNtpServerAdminStatus_Type=JuniEnable
_JuniNtpServerAdminStatus_Object=MibScalar
juniNtpServerAdminStatus=_JuniNtpServerAdminStatus_Object((1,3,6,1,4,1,4874,2,2,56,2,3,2),_JuniNtpServerAdminStatus_Type())
juniNtpServerAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniNtpServerAdminStatus.setStatus(_B)
_JuniNtpPeers_ObjectIdentity=ObjectIdentity
juniNtpPeers=_JuniNtpPeers_ObjectIdentity((1,3,6,1,4,1,4874,2,2,56,2,4))
_JuniNtpPeerCfgTable_Object=MibTable
juniNtpPeerCfgTable=_JuniNtpPeerCfgTable_Object((1,3,6,1,4,1,4874,2,2,56,2,4,1))
if mibBuilder.loadTexts:juniNtpPeerCfgTable.setStatus(_B)
_JuniNtpPeerCfgEntry_Object=MibTableRow
juniNtpPeerCfgEntry=_JuniNtpPeerCfgEntry_Object((1,3,6,1,4,1,4874,2,2,56,2,4,1,1))
juniNtpPeerCfgEntry.setIndexNames((0,_A,_M),(0,_A,_O))
if mibBuilder.loadTexts:juniNtpPeerCfgEntry.setStatus(_B)
_JuniNtpPeerCfgIpAddress_Type=IpAddress
_JuniNtpPeerCfgIpAddress_Object=MibTableColumn
juniNtpPeerCfgIpAddress=_JuniNtpPeerCfgIpAddress_Object((1,3,6,1,4,1,4874,2,2,56,2,4,1,1,1),_JuniNtpPeerCfgIpAddress_Type())
juniNtpPeerCfgIpAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:juniNtpPeerCfgIpAddress.setStatus(_B)
class _JuniNtpPeerCfgNtpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_JuniNtpPeerCfgNtpVersion_Type.__name__=_F
_JuniNtpPeerCfgNtpVersion_Object=MibTableColumn
juniNtpPeerCfgNtpVersion=_JuniNtpPeerCfgNtpVersion_Object((1,3,6,1,4,1,4874,2,2,56,2,4,1,1,2),_JuniNtpPeerCfgNtpVersion_Type())
juniNtpPeerCfgNtpVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:juniNtpPeerCfgNtpVersion.setStatus(_B)
class _JuniNtpPeerCfgPacketSourceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniNtpPeerCfgPacketSourceIfIndex_Type.__name__=_F
_JuniNtpPeerCfgPacketSourceIfIndex_Object=MibTableColumn
juniNtpPeerCfgPacketSourceIfIndex=_JuniNtpPeerCfgPacketSourceIfIndex_Object((1,3,6,1,4,1,4874,2,2,56,2,4,1,1,3),_JuniNtpPeerCfgPacketSourceIfIndex_Type())
juniNtpPeerCfgPacketSourceIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:juniNtpPeerCfgPacketSourceIfIndex.setStatus(_B)
_JuniNtpPeerCfgIsPreferred_Type=TruthValue
_JuniNtpPeerCfgIsPreferred_Object=MibTableColumn
juniNtpPeerCfgIsPreferred=_JuniNtpPeerCfgIsPreferred_Object((1,3,6,1,4,1,4874,2,2,56,2,4,1,1,4),_JuniNtpPeerCfgIsPreferred_Type())
juniNtpPeerCfgIsPreferred.setMaxAccess(_G)
if mibBuilder.loadTexts:juniNtpPeerCfgIsPreferred.setStatus(_B)
_JuniNtpPeerCfgRowStatus_Type=RowStatus
_JuniNtpPeerCfgRowStatus_Object=MibTableColumn
juniNtpPeerCfgRowStatus=_JuniNtpPeerCfgRowStatus_Object((1,3,6,1,4,1,4874,2,2,56,2,4,1,1,5),_JuniNtpPeerCfgRowStatus_Type())
juniNtpPeerCfgRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:juniNtpPeerCfgRowStatus.setStatus(_B)
_JuniNtpPeerTable_Object=MibTable
juniNtpPeerTable=_JuniNtpPeerTable_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2))
if mibBuilder.loadTexts:juniNtpPeerTable.setStatus(_B)
_JuniNtpPeerEntry_Object=MibTableRow
juniNtpPeerEntry=_JuniNtpPeerEntry_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1))
juniNtpPeerEntry.setIndexNames((0,_A,_M),(0,_A,_O))
if mibBuilder.loadTexts:juniNtpPeerEntry.setStatus(_B)
class _JuniNtpPeerState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_JuniNtpPeerState_Type.__name__=_W
_JuniNtpPeerState_Object=MibTableColumn
juniNtpPeerState=_JuniNtpPeerState_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,1),_JuniNtpPeerState_Type())
juniNtpPeerState.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerState.setStatus(_B)
class _JuniNtpPeerStratumNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_JuniNtpPeerStratumNumber_Type.__name__=_F
_JuniNtpPeerStratumNumber_Object=MibTableColumn
juniNtpPeerStratumNumber=_JuniNtpPeerStratumNumber_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,2),_JuniNtpPeerStratumNumber_Type())
juniNtpPeerStratumNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerStratumNumber.setStatus(_B)
class _JuniNtpPeerAssociationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('broacastServer',0),('multicastServer',1),('unicastServer',2)))
_JuniNtpPeerAssociationMode_Type.__name__=_F
_JuniNtpPeerAssociationMode_Object=MibTableColumn
juniNtpPeerAssociationMode=_JuniNtpPeerAssociationMode_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,3),_JuniNtpPeerAssociationMode_Type())
juniNtpPeerAssociationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerAssociationMode.setStatus(_B)
_JuniNtpPeerBroadcastInterval_Type=Integer32
_JuniNtpPeerBroadcastInterval_Object=MibTableColumn
juniNtpPeerBroadcastInterval=_JuniNtpPeerBroadcastInterval_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,4),_JuniNtpPeerBroadcastInterval_Type())
juniNtpPeerBroadcastInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerBroadcastInterval.setStatus(_B)
if mibBuilder.loadTexts:juniNtpPeerBroadcastInterval.setUnits(_E)
_JuniNtpPeerPolledInterval_Type=Integer32
_JuniNtpPeerPolledInterval_Object=MibTableColumn
juniNtpPeerPolledInterval=_JuniNtpPeerPolledInterval_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,5),_JuniNtpPeerPolledInterval_Type())
juniNtpPeerPolledInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerPolledInterval.setStatus(_B)
if mibBuilder.loadTexts:juniNtpPeerPolledInterval.setUnits(_E)
_JuniNtpPeerPollingInterval_Type=Integer32
_JuniNtpPeerPollingInterval_Object=MibTableColumn
juniNtpPeerPollingInterval=_JuniNtpPeerPollingInterval_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,6),_JuniNtpPeerPollingInterval_Type())
juniNtpPeerPollingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerPollingInterval.setStatus(_B)
if mibBuilder.loadTexts:juniNtpPeerPollingInterval.setUnits(_E)
_JuniNtpPeerDelay_Type=JuniNtpClockSignedTime
_JuniNtpPeerDelay_Object=MibTableColumn
juniNtpPeerDelay=_JuniNtpPeerDelay_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,7),_JuniNtpPeerDelay_Type())
juniNtpPeerDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerDelay.setStatus(_B)
if mibBuilder.loadTexts:juniNtpPeerDelay.setUnits(_E)
_JuniNtpPeerDispersion_Type=JuniNtpClockUnsignedTime
_JuniNtpPeerDispersion_Object=MibTableColumn
juniNtpPeerDispersion=_JuniNtpPeerDispersion_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,8),_JuniNtpPeerDispersion_Type())
juniNtpPeerDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerDispersion.setStatus(_B)
if mibBuilder.loadTexts:juniNtpPeerDispersion.setUnits(_E)
_JuniNtpPeerOffsetError_Type=JuniNtpClockSignedTime
_JuniNtpPeerOffsetError_Object=MibTableColumn
juniNtpPeerOffsetError=_JuniNtpPeerOffsetError_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,9),_JuniNtpPeerOffsetError_Type())
juniNtpPeerOffsetError.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerOffsetError.setStatus(_B)
if mibBuilder.loadTexts:juniNtpPeerOffsetError.setUnits(_E)
class _JuniNtpPeerReachability_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_JuniNtpPeerReachability_Type.__name__=_W
_JuniNtpPeerReachability_Object=MibTableColumn
juniNtpPeerReachability=_JuniNtpPeerReachability_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,10),_JuniNtpPeerReachability_Type())
juniNtpPeerReachability.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerReachability.setStatus(_B)
_JuniNtpPeerRootDelay_Type=JuniNtpClockSignedTime
_JuniNtpPeerRootDelay_Object=MibTableColumn
juniNtpPeerRootDelay=_JuniNtpPeerRootDelay_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,11),_JuniNtpPeerRootDelay_Type())
juniNtpPeerRootDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerRootDelay.setStatus(_B)
if mibBuilder.loadTexts:juniNtpPeerRootDelay.setUnits(_E)
_JuniNtpPeerRootDispersion_Type=JuniNtpClockUnsignedTime
_JuniNtpPeerRootDispersion_Object=MibTableColumn
juniNtpPeerRootDispersion=_JuniNtpPeerRootDispersion_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,12),_JuniNtpPeerRootDispersion_Type())
juniNtpPeerRootDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerRootDispersion.setStatus(_B)
if mibBuilder.loadTexts:juniNtpPeerRootDispersion.setUnits(_E)
_JuniNtpPeerRootSyncDistance_Type=JuniNtpClockSignedTime
_JuniNtpPeerRootSyncDistance_Object=MibTableColumn
juniNtpPeerRootSyncDistance=_JuniNtpPeerRootSyncDistance_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,13),_JuniNtpPeerRootSyncDistance_Type())
juniNtpPeerRootSyncDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerRootSyncDistance.setStatus(_B)
if mibBuilder.loadTexts:juniNtpPeerRootSyncDistance.setUnits(_E)
_JuniNtpPeerRootTime_Type=JuniNtpTimeStamp
_JuniNtpPeerRootTime_Object=MibTableColumn
juniNtpPeerRootTime=_JuniNtpPeerRootTime_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,14),_JuniNtpPeerRootTime_Type())
juniNtpPeerRootTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerRootTime.setStatus(_B)
if mibBuilder.loadTexts:juniNtpPeerRootTime.setUnits(_E)
_JuniNtpPeerRootTimeUpdateServer_Type=IpAddress
_JuniNtpPeerRootTimeUpdateServer_Object=MibTableColumn
juniNtpPeerRootTimeUpdateServer=_JuniNtpPeerRootTimeUpdateServer_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,15),_JuniNtpPeerRootTimeUpdateServer_Type())
juniNtpPeerRootTimeUpdateServer.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerRootTimeUpdateServer.setStatus(_B)
_JuniNtpPeerReceiveTime_Type=JuniNtpTimeStamp
_JuniNtpPeerReceiveTime_Object=MibTableColumn
juniNtpPeerReceiveTime=_JuniNtpPeerReceiveTime_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,16),_JuniNtpPeerReceiveTime_Type())
juniNtpPeerReceiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerReceiveTime.setStatus(_B)
_JuniNtpPeerTransmitTime_Type=JuniNtpTimeStamp
_JuniNtpPeerTransmitTime_Object=MibTableColumn
juniNtpPeerTransmitTime=_JuniNtpPeerTransmitTime_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,17),_JuniNtpPeerTransmitTime_Type())
juniNtpPeerTransmitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerTransmitTime.setStatus(_B)
_JuniNtpPeerRequestTime_Type=JuniNtpTimeStamp
_JuniNtpPeerRequestTime_Object=MibTableColumn
juniNtpPeerRequestTime=_JuniNtpPeerRequestTime_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,18),_JuniNtpPeerRequestTime_Type())
juniNtpPeerRequestTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerRequestTime.setStatus(_B)
_JuniNtpPeerPrecision_Type=JuniNtpClockSignedTime
_JuniNtpPeerPrecision_Object=MibTableColumn
juniNtpPeerPrecision=_JuniNtpPeerPrecision_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,19),_JuniNtpPeerPrecision_Type())
juniNtpPeerPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerPrecision.setStatus(_B)
if mibBuilder.loadTexts:juniNtpPeerPrecision.setUnits(_E)
_JuniNtpPeerLastUpdateTime_Type=Unsigned32
_JuniNtpPeerLastUpdateTime_Object=MibTableColumn
juniNtpPeerLastUpdateTime=_JuniNtpPeerLastUpdateTime_Object((1,3,6,1,4,1,4874,2,2,56,2,4,2,1,20),_JuniNtpPeerLastUpdateTime_Type())
juniNtpPeerLastUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerLastUpdateTime.setStatus(_B)
if mibBuilder.loadTexts:juniNtpPeerLastUpdateTime.setUnits(_E)
_JuniNtpPeerFilterRegisterTable_Object=MibTable
juniNtpPeerFilterRegisterTable=_JuniNtpPeerFilterRegisterTable_Object((1,3,6,1,4,1,4874,2,2,56,2,4,3))
if mibBuilder.loadTexts:juniNtpPeerFilterRegisterTable.setStatus(_B)
_JuniNtpPeerFilterRegisterEntry_Object=MibTableRow
juniNtpPeerFilterRegisterEntry=_JuniNtpPeerFilterRegisterEntry_Object((1,3,6,1,4,1,4874,2,2,56,2,4,3,1))
juniNtpPeerFilterRegisterEntry.setIndexNames((0,_A,_O),(0,_A,_AB))
if mibBuilder.loadTexts:juniNtpPeerFilterRegisterEntry.setStatus(_B)
_JuniNtpPeerFilterIndex_Type=Unsigned32
_JuniNtpPeerFilterIndex_Object=MibTableColumn
juniNtpPeerFilterIndex=_JuniNtpPeerFilterIndex_Object((1,3,6,1,4,1,4874,2,2,56,2,4,3,1,1),_JuniNtpPeerFilterIndex_Type())
juniNtpPeerFilterIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:juniNtpPeerFilterIndex.setStatus(_B)
_JuniNtpPeerFilterOffset_Type=JuniNtpClockSignedTime
_JuniNtpPeerFilterOffset_Object=MibTableColumn
juniNtpPeerFilterOffset=_JuniNtpPeerFilterOffset_Object((1,3,6,1,4,1,4874,2,2,56,2,4,3,1,2),_JuniNtpPeerFilterOffset_Type())
juniNtpPeerFilterOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerFilterOffset.setStatus(_B)
if mibBuilder.loadTexts:juniNtpPeerFilterOffset.setUnits(_E)
_JuniNtpPeerFilterDelay_Type=JuniNtpClockSignedTime
_JuniNtpPeerFilterDelay_Object=MibTableColumn
juniNtpPeerFilterDelay=_JuniNtpPeerFilterDelay_Object((1,3,6,1,4,1,4874,2,2,56,2,4,3,1,3),_JuniNtpPeerFilterDelay_Type())
juniNtpPeerFilterDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerFilterDelay.setStatus(_B)
if mibBuilder.loadTexts:juniNtpPeerFilterDelay.setUnits(_E)
_JuniNtpPeerFilterDispersion_Type=JuniNtpClockUnsignedTime
_JuniNtpPeerFilterDispersion_Object=MibTableColumn
juniNtpPeerFilterDispersion=_JuniNtpPeerFilterDispersion_Object((1,3,6,1,4,1,4874,2,2,56,2,4,3,1,4),_JuniNtpPeerFilterDispersion_Type())
juniNtpPeerFilterDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:juniNtpPeerFilterDispersion.setStatus(_B)
if mibBuilder.loadTexts:juniNtpPeerFilterDispersion.setUnits(_E)
_JuniNtpAccessGroup_ObjectIdentity=ObjectIdentity
juniNtpAccessGroup=_JuniNtpAccessGroup_ObjectIdentity((1,3,6,1,4,1,4874,2,2,56,2,5))
_JuniNtpRouterAccessGroupPeer_Type=DisplayString
_JuniNtpRouterAccessGroupPeer_Object=MibScalar
juniNtpRouterAccessGroupPeer=_JuniNtpRouterAccessGroupPeer_Object((1,3,6,1,4,1,4874,2,2,56,2,5,1),_JuniNtpRouterAccessGroupPeer_Type())
juniNtpRouterAccessGroupPeer.setMaxAccess(_D)
if mibBuilder.loadTexts:juniNtpRouterAccessGroupPeer.setStatus(_B)
_JuniNtpRouterAccessGroupServe_Type=DisplayString
_JuniNtpRouterAccessGroupServe_Object=MibScalar
juniNtpRouterAccessGroupServe=_JuniNtpRouterAccessGroupServe_Object((1,3,6,1,4,1,4874,2,2,56,2,5,2),_JuniNtpRouterAccessGroupServe_Type())
juniNtpRouterAccessGroupServe.setMaxAccess(_D)
if mibBuilder.loadTexts:juniNtpRouterAccessGroupServe.setStatus(_B)
_JuniNtpRouterAccessGroupServeOnly_Type=DisplayString
_JuniNtpRouterAccessGroupServeOnly_Object=MibScalar
juniNtpRouterAccessGroupServeOnly=_JuniNtpRouterAccessGroupServeOnly_Object((1,3,6,1,4,1,4874,2,2,56,2,5,3),_JuniNtpRouterAccessGroupServeOnly_Type())
juniNtpRouterAccessGroupServeOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:juniNtpRouterAccessGroupServeOnly.setStatus(_B)
_JuniNtpRouterAccessGroupQueryOnly_Type=DisplayString
_JuniNtpRouterAccessGroupQueryOnly_Object=MibScalar
juniNtpRouterAccessGroupQueryOnly=_JuniNtpRouterAccessGroupQueryOnly_Object((1,3,6,1,4,1,4874,2,2,56,2,5,4),_JuniNtpRouterAccessGroupQueryOnly_Type())
juniNtpRouterAccessGroupQueryOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:juniNtpRouterAccessGroupQueryOnly.setStatus(_B)
_JuniSysClockConformance_ObjectIdentity=ObjectIdentity
juniSysClockConformance=_JuniSysClockConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,56,3))
_JuniSysClockCompliances_ObjectIdentity=ObjectIdentity
juniSysClockCompliances=_JuniSysClockCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,56,3,1))
_JuniSysClockGroups_ObjectIdentity=ObjectIdentity
juniSysClockGroups=_JuniSysClockGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,56,3,2))
juniSysClockTimeGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,56,3,2,1))
juniSysClockTimeGroup.setObjects(*((_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:juniSysClockTimeGroup.setStatus(_B)
juniSysClockDstGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,56,3,2,2))
juniSysClockDstGroup.setObjects(*((_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:juniSysClockDstGroup.setStatus(_B)
juniNtpSysClockGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,56,3,2,3))
juniNtpSysClockGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:juniNtpSysClockGroup.setStatus(_P)
juniNtpClientGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,56,3,2,4))
juniNtpClientGroup.setObjects(*((_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:juniNtpClientGroup.setStatus(_B)
juniNtpServerGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,56,3,2,5))
juniNtpServerGroup.setObjects(*((_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:juniNtpServerGroup.setStatus(_B)
juniNtpPeersGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,56,3,2,6))
juniNtpPeersGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_L),(_A,_A6)))
if mibBuilder.loadTexts:juniNtpPeersGroup.setStatus(_P)
juniNtpAccessGroupGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,56,3,2,7))
juniNtpAccessGroupGroup.setObjects(*((_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae)))
if mibBuilder.loadTexts:juniNtpAccessGroupGroup.setStatus(_B)
juniNtpSysClockGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,56,3,2,9))
juniNtpSysClockGroup2.setObjects(*((_A,_I),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_Af),(_A,_Ag)))
if mibBuilder.loadTexts:juniNtpSysClockGroup2.setStatus(_B)
juniNtpSysClockDeprecatedGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,56,3,2,10))
juniNtpSysClockDeprecatedGroup.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:juniNtpSysClockDeprecatedGroup.setStatus(_c)
juniNtpPeersGroup1=ObjectGroup((1,3,6,1,4,1,4874,2,2,56,3,2,11))
juniNtpPeersGroup1.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_L),(_A,_A6),(_A,_Ah)))
if mibBuilder.loadTexts:juniNtpPeersGroup1.setStatus(_B)
juniNtpFrequencyCalibrationStart=NotificationType((1,3,6,1,4,1,4874,2,2,56,2,0,1))
juniNtpFrequencyCalibrationStart.setObjects((_A,_K))
if mibBuilder.loadTexts:juniNtpFrequencyCalibrationStart.setStatus(_B)
juniNtpFrequencyCalibrationEnd=NotificationType((1,3,6,1,4,1,4874,2,2,56,2,0,2))
juniNtpFrequencyCalibrationEnd.setObjects((_A,_K))
if mibBuilder.loadTexts:juniNtpFrequencyCalibrationEnd.setStatus(_B)
juniNtpTimeSynUp=NotificationType((1,3,6,1,4,1,4874,2,2,56,2,0,3))
if mibBuilder.loadTexts:juniNtpTimeSynUp.setStatus(_B)
juniNtpTimeSynDown=NotificationType((1,3,6,1,4,1,4874,2,2,56,2,0,4))
if mibBuilder.loadTexts:juniNtpTimeSynDown.setStatus(_B)
juniNtpTimeServerSynUp=NotificationType((1,3,6,1,4,1,4874,2,2,56,2,0,5))
juniNtpTimeServerSynUp.setObjects((_A,_L))
if mibBuilder.loadTexts:juniNtpTimeServerSynUp.setStatus(_B)
juniNtpTimeServerSynDown=NotificationType((1,3,6,1,4,1,4874,2,2,56,2,0,6))
juniNtpTimeServerSynDown.setObjects((_A,_L))
if mibBuilder.loadTexts:juniNtpTimeServerSynDown.setStatus(_B)
juniNtpFirstSystemClockSet=NotificationType((1,3,6,1,4,1,4874,2,2,56,2,0,7))
juniNtpFirstSystemClockSet.setObjects(*((_A,_J),(_A,_I)))
if mibBuilder.loadTexts:juniNtpFirstSystemClockSet.setStatus(_B)
juniNtpClockOffSetLimitCrossed=NotificationType((1,3,6,1,4,1,4874,2,2,56,2,0,8))
juniNtpClockOffSetLimitCrossed.setObjects(*((_A,_J),(_A,_I)))
if mibBuilder.loadTexts:juniNtpClockOffSetLimitCrossed.setStatus(_B)
juniNtpNotificationGroup=NotificationGroup((1,3,6,1,4,1,4874,2,2,56,3,2,8))
juniNtpNotificationGroup.setObjects(*((_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap)))
if mibBuilder.loadTexts:juniNtpNotificationGroup.setStatus(_B)
juniSysClockCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,56,3,1,1))
juniSysClockCompliance.setObjects(*((_A,_Q),(_A,_R),(_A,_A7),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:juniSysClockCompliance.setStatus(_P)
juniSysClockCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,56,3,1,2))
juniSysClockCompliance2.setObjects(*((_A,_Q),(_A,_R),(_A,_A7),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_A8)))
if mibBuilder.loadTexts:juniSysClockCompliance2.setStatus(_P)
juniSysClockCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,56,3,1,3))
juniSysClockCompliance3.setObjects(*((_A,_Q),(_A,_R),(_A,_Aq),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_A8)))
if mibBuilder.loadTexts:juniSysClockCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_X:JuniSysClockMonth,_Y:JuniSysClockWeekOfTheMonth,_Z:JuniSysClockDayOfTheWeek,_a:JuniSysClockHour,_b:JuniSysClockMinute,'JuniNtpTimeStamp':JuniNtpTimeStamp,'JuniNtpClockSignedTime':JuniNtpClockSignedTime,'JuniNtpClockUnsignedTime':JuniNtpClockUnsignedTime,'juniSysClockMIB':juniSysClockMIB,'juniSysClockObjects':juniSysClockObjects,'juniSysClockTime':juniSysClockTime,_AC:juniSysClockDateAndTime,_AD:juniSysClockTimeZoneName,'juniSysClockDst':juniSysClockDst,_AE:juniSysClockDstName,_AF:juniSysClockDstOffset,_AG:juniSysClockDstStatus,_AH:juniSysClockDstAbsoluteStartTime,_AI:juniSysClockDstAbsoluteStopTime,_AJ:juniSysClockDstRecurStartMonth,_AK:juniSysClockDstRecurStartWeek,_AL:juniSysClockDstRecurStartDay,_AM:juniSysClockDstRecurStartHour,_AN:juniSysClockDstRecurStartMinute,_AO:juniSysClockDstRecurStopMonth,_AP:juniSysClockDstRecurStopWeek,_AQ:juniSysClockDstRecurStopDay,_AR:juniSysClockDstRecurStopHour,_AS:juniSysClockDstRecurStopMinute,'juniNtpObjects':juniNtpObjects,'juniNtpTraps':juniNtpTraps,_Ai:juniNtpFrequencyCalibrationStart,_Aj:juniNtpFrequencyCalibrationEnd,_Ak:juniNtpTimeSynUp,_Al:juniNtpTimeSynDown,_Am:juniNtpTimeServerSynUp,_An:juniNtpTimeServerSynDown,_Ao:juniNtpFirstSystemClockSet,_Ap:juniNtpClockOffSetLimitCrossed,'juniNtpSysClock':juniNtpSysClock,_I:juniNtpSysClockState,_J:juniNtpSysClockOffsetError,_K:juniNtpSysClockFrequencyError,_d:juniNtpSysClockRootDelay,_e:juniNtpSysClockRootDispersion,_f:juniNtpSysClockStratumNumber,_g:juniNtpSysClockLastUpdateTime,_h:juniNtpSysClockLastUpdateServer,_Af:juniNtpSysClockOffsetErrorNew,_Ag:juniNtpSysClockFrequencyErrorNew,'juniNtpClient':juniNtpClient,_AT:juniNtpClientAdminStatus,_AU:juniNtpClientSystemRouterIndex,_AV:juniNtpClientPacketSourceIfIndex,_AW:juniNtpClientBroadcastDelay,'juniNtpClientIfTable':juniNtpClientIfTable,'juniNtpClientIfEntry':juniNtpClientIfEntry,_M:juniNtpClientIfRouterIndex,_AA:juniNtpClientIfIfIndex,_AX:juniNtpClientIfDisable,_AY:juniNtpClientIfIsBroadcastClient,'juniNtpClientIfIsBroadcastServer':juniNtpClientIfIsBroadcastServer,'juniNtpClientIfIsBroadcastServerVersion':juniNtpClientIfIsBroadcastServerVersion,'juniNtpClientIfIsBroadcastServerDelay':juniNtpClientIfIsBroadcastServerDelay,'juniNtpServer':juniNtpServer,_Aa:juniNtpServerStratumNumber,_AZ:juniNtpServerAdminStatus,'juniNtpPeers':juniNtpPeers,'juniNtpPeerCfgTable':juniNtpPeerCfgTable,'juniNtpPeerCfgEntry':juniNtpPeerCfgEntry,_O:juniNtpPeerCfgIpAddress,_A4:juniNtpPeerCfgNtpVersion,_A5:juniNtpPeerCfgPacketSourceIfIndex,_L:juniNtpPeerCfgIsPreferred,_A6:juniNtpPeerCfgRowStatus,'juniNtpPeerTable':juniNtpPeerTable,'juniNtpPeerEntry':juniNtpPeerEntry,_i:juniNtpPeerState,_j:juniNtpPeerStratumNumber,_k:juniNtpPeerAssociationMode,_l:juniNtpPeerBroadcastInterval,_m:juniNtpPeerPolledInterval,_n:juniNtpPeerPollingInterval,_o:juniNtpPeerDelay,_p:juniNtpPeerDispersion,_q:juniNtpPeerOffsetError,_r:juniNtpPeerReachability,_t:juniNtpPeerRootDelay,_u:juniNtpPeerRootDispersion,_v:juniNtpPeerRootSyncDistance,_w:juniNtpPeerRootTime,_x:juniNtpPeerRootTimeUpdateServer,_y:juniNtpPeerReceiveTime,_z:juniNtpPeerTransmitTime,_A0:juniNtpPeerRequestTime,_s:juniNtpPeerPrecision,_Ah:juniNtpPeerLastUpdateTime,'juniNtpPeerFilterRegisterTable':juniNtpPeerFilterRegisterTable,'juniNtpPeerFilterRegisterEntry':juniNtpPeerFilterRegisterEntry,_AB:juniNtpPeerFilterIndex,_A1:juniNtpPeerFilterOffset,_A2:juniNtpPeerFilterDelay,_A3:juniNtpPeerFilterDispersion,'juniNtpAccessGroup':juniNtpAccessGroup,_Ab:juniNtpRouterAccessGroupPeer,_Ac:juniNtpRouterAccessGroupServe,_Ad:juniNtpRouterAccessGroupServeOnly,_Ae:juniNtpRouterAccessGroupQueryOnly,'juniSysClockConformance':juniSysClockConformance,'juniSysClockCompliances':juniSysClockCompliances,'juniSysClockCompliance':juniSysClockCompliance,'juniSysClockCompliance2':juniSysClockCompliance2,'juniSysClockCompliance3':juniSysClockCompliance3,'juniSysClockGroups':juniSysClockGroups,_Q:juniSysClockTimeGroup,_R:juniSysClockDstGroup,_A7:juniNtpSysClockGroup,_S:juniNtpClientGroup,_T:juniNtpServerGroup,_U:juniNtpPeersGroup,_V:juniNtpAccessGroupGroup,_A8:juniNtpNotificationGroup,_Aq:juniNtpSysClockGroup2,'juniNtpSysClockDeprecatedGroup':juniNtpSysClockDeprecatedGroup,'juniNtpPeersGroup1':juniNtpPeersGroup1})