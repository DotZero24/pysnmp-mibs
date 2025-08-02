_A0='tptAuditLogCapacityNotifyPercent'
_z='tptAuditLogNotifyMessage'
_y='tptAuditLogNotifyUser'
_x='tptAuditLogNotifyResult'
_w='tptAuditLogNotifyCategory'
_v='tptAuditLogNotifyIpAddr'
_u='tptAuditLogNotifyIpAddrType'
_t='tptAuditLogNotifyType'
_s='tptAuditLogNotifyAccess'
_r='tptAuditLogNotifyTime'
_q='tptTier3CongestionThreshold'
_p='tptTier3CongestionPacketLoss'
_o='tptTier3CongestionNotifyPhase'
_n='tptCongestionThreshold'
_m='tptCongestionPacketLoss'
_l='tptCongestionNotifyPhase'
_k='tptQuarantineNotifySslInspected'
_j='tptQuarantineNotifyHostNetAddrV6'
_i='tptQuarantineNotifyAction'
_h='tptQuarantineNotifySegmentName'
_g='tptQuarantineNotifyReason'
_f='tptQuarantineNotifyHostNetAddr'
_e='tptSystemLogNotifyTimeNano'
_d='tptSystemLogNotifyTimeSec'
_c='tptSystemLogNotifySeverity'
_b='tptSystemLogNotifySequence'
_a='tptSystemLogNotifyText'
_Z='tptDiscoveryNotifyHostDeviceID'
_Y='tptDiscoveryNotifyHostNetAddr'
_X='tptDiscoveryNotifySchedID'
_W='tptDiscoveryNotifyErrorText'
_V='tptDiscoveryNotifyStopTime'
_U='tptDiscoveryNotifyStartTime'
_T='tptDiscoveryNotifyUnknown'
_S='tptDiscoveryNotifyNotFound'
_R='tptDiscoveryNotifyUnchanged'
_Q='tptDiscoveryNotifyChanged'
_P='tptDiscoveryNotifyNewHosts'
_O='tptDiscoveryNotifyDelta'
_N='tptDiscoveryNotifyScanRange'
_M='tptDiscoveryNotifySegmentName'
_L='tptDiscoveryNotifyScanID'
_K='tptRolloverNotifyFileType'
_J='deprecated'
_I='SnmpAdminString'
_H='tptRolloverNotifyTime'
_G='accessible-for-notify'
_F='OctetString'
_E='tptMiscNotifyDeviceID'
_D='obsolete'
_C='read-only'
_B='current'
_A='TPT-MISC-NOTIFY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
SslInspectedFlag,=mibBuilder.importSymbols('TPT-POLICY-MIB','SslInspectedFlag')
tpt_tpa_eventsV2,tpt_tpa_objs,tpt_tpa_unkparams=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-eventsV2','tpt-tpa-objs','tpt-tpa-unkparams')
tpt_misc_notify=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,2))
if mibBuilder.loadTexts:tpt_misc_notify.setRevisions(('2016-05-25 18:54','2016-05-03 17:26','2015-05-28 13:30','2014-11-11 18:43'))
class LogFileType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('system',1),('alert',2),('block',3),('peer',4),('audit',5),('quarantine',6)))
class DiscoveryDelta(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('changed',1),('unchanged',2)))
class SystemLogSeverity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('critical',1),('error',2),('emergency',3),('warning',4),('alert',5),('notice',6),('info',7),('debug',8)))
class AddOrRemove(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('add',1),('remove',2)))
class CongestionThresholdPhase(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('entering',1),('continuing',2),('exiting',3)))
class AuditLogResult(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('success',1),('failed',2)))
class AuditLogCategory(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('undefined',1),('general',2),('login',3),('logout',4),('user',5),('time',6),('policy',7),('update',8),('boot',9),('report',10),('host',11),('cfg',12),('device',13),('sms',14),('server',15),('segment',16),('license',17),('ha',18),('monitor',19),('ipFilter',20),('connTable',21),('hostComm',22),('tse',23),('cf',24)))
class _TptMiscNotifyDeviceID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptMiscNotifyDeviceID_Type.__name__=_F
_TptMiscNotifyDeviceID_Object=MibScalar
tptMiscNotifyDeviceID=_TptMiscNotifyDeviceID_Object((1,3,6,1,4,1,10734,3,3,3,1,31),_TptMiscNotifyDeviceID_Type())
tptMiscNotifyDeviceID.setMaxAccess(_C)
if mibBuilder.loadTexts:tptMiscNotifyDeviceID.setStatus(_B)
_TptRolloverNotifyFileType_Type=LogFileType
_TptRolloverNotifyFileType_Object=MibScalar
tptRolloverNotifyFileType=_TptRolloverNotifyFileType_Object((1,3,6,1,4,1,10734,3,3,3,1,32),_TptRolloverNotifyFileType_Type())
tptRolloverNotifyFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:tptRolloverNotifyFileType.setStatus(_B)
_TptRolloverNotifyMaxFiles_Type=Unsigned32
_TptRolloverNotifyMaxFiles_Object=MibScalar
tptRolloverNotifyMaxFiles=_TptRolloverNotifyMaxFiles_Object((1,3,6,1,4,1,10734,3,3,3,1,33),_TptRolloverNotifyMaxFiles_Type())
tptRolloverNotifyMaxFiles.setMaxAccess(_C)
if mibBuilder.loadTexts:tptRolloverNotifyMaxFiles.setStatus(_J)
_TptRolloverNotifyNumFiles_Type=Unsigned32
_TptRolloverNotifyNumFiles_Object=MibScalar
tptRolloverNotifyNumFiles=_TptRolloverNotifyNumFiles_Object((1,3,6,1,4,1,10734,3,3,3,1,34),_TptRolloverNotifyNumFiles_Type())
tptRolloverNotifyNumFiles.setMaxAccess(_C)
if mibBuilder.loadTexts:tptRolloverNotifyNumFiles.setStatus(_J)
_TptRolloverNotifyTime_Type=Unsigned32
_TptRolloverNotifyTime_Object=MibScalar
tptRolloverNotifyTime=_TptRolloverNotifyTime_Object((1,3,6,1,4,1,10734,3,3,3,1,35),_TptRolloverNotifyTime_Type())
tptRolloverNotifyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tptRolloverNotifyTime.setStatus(_B)
class _TptDiscoveryNotifyScanID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptDiscoveryNotifyScanID_Type.__name__=_F
_TptDiscoveryNotifyScanID_Object=MibScalar
tptDiscoveryNotifyScanID=_TptDiscoveryNotifyScanID_Object((1,3,6,1,4,1,10734,3,3,3,1,42),_TptDiscoveryNotifyScanID_Type())
tptDiscoveryNotifyScanID.setMaxAccess(_C)
if mibBuilder.loadTexts:tptDiscoveryNotifyScanID.setStatus(_D)
class _TptDiscoveryNotifySegmentName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_TptDiscoveryNotifySegmentName_Type.__name__=_F
_TptDiscoveryNotifySegmentName_Object=MibScalar
tptDiscoveryNotifySegmentName=_TptDiscoveryNotifySegmentName_Object((1,3,6,1,4,1,10734,3,3,3,1,43),_TptDiscoveryNotifySegmentName_Type())
tptDiscoveryNotifySegmentName.setMaxAccess(_C)
if mibBuilder.loadTexts:tptDiscoveryNotifySegmentName.setStatus(_D)
class _TptDiscoveryNotifyScanRange_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptDiscoveryNotifyScanRange_Type.__name__=_F
_TptDiscoveryNotifyScanRange_Object=MibScalar
tptDiscoveryNotifyScanRange=_TptDiscoveryNotifyScanRange_Object((1,3,6,1,4,1,10734,3,3,3,1,44),_TptDiscoveryNotifyScanRange_Type())
tptDiscoveryNotifyScanRange.setMaxAccess(_C)
if mibBuilder.loadTexts:tptDiscoveryNotifyScanRange.setStatus(_D)
_TptDiscoveryNotifyDelta_Type=DiscoveryDelta
_TptDiscoveryNotifyDelta_Object=MibScalar
tptDiscoveryNotifyDelta=_TptDiscoveryNotifyDelta_Object((1,3,6,1,4,1,10734,3,3,3,1,45),_TptDiscoveryNotifyDelta_Type())
tptDiscoveryNotifyDelta.setMaxAccess(_C)
if mibBuilder.loadTexts:tptDiscoveryNotifyDelta.setStatus(_D)
_TptDiscoveryNotifyNewHosts_Type=Integer32
_TptDiscoveryNotifyNewHosts_Object=MibScalar
tptDiscoveryNotifyNewHosts=_TptDiscoveryNotifyNewHosts_Object((1,3,6,1,4,1,10734,3,3,3,1,46),_TptDiscoveryNotifyNewHosts_Type())
tptDiscoveryNotifyNewHosts.setMaxAccess(_C)
if mibBuilder.loadTexts:tptDiscoveryNotifyNewHosts.setStatus(_D)
_TptDiscoveryNotifyChanged_Type=Integer32
_TptDiscoveryNotifyChanged_Object=MibScalar
tptDiscoveryNotifyChanged=_TptDiscoveryNotifyChanged_Object((1,3,6,1,4,1,10734,3,3,3,1,47),_TptDiscoveryNotifyChanged_Type())
tptDiscoveryNotifyChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tptDiscoveryNotifyChanged.setStatus(_D)
_TptDiscoveryNotifyUnchanged_Type=Integer32
_TptDiscoveryNotifyUnchanged_Object=MibScalar
tptDiscoveryNotifyUnchanged=_TptDiscoveryNotifyUnchanged_Object((1,3,6,1,4,1,10734,3,3,3,1,48),_TptDiscoveryNotifyUnchanged_Type())
tptDiscoveryNotifyUnchanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tptDiscoveryNotifyUnchanged.setStatus(_D)
_TptDiscoveryNotifyNotFound_Type=Integer32
_TptDiscoveryNotifyNotFound_Object=MibScalar
tptDiscoveryNotifyNotFound=_TptDiscoveryNotifyNotFound_Object((1,3,6,1,4,1,10734,3,3,3,1,49),_TptDiscoveryNotifyNotFound_Type())
tptDiscoveryNotifyNotFound.setMaxAccess(_C)
if mibBuilder.loadTexts:tptDiscoveryNotifyNotFound.setStatus(_D)
_TptDiscoveryNotifyUnknown_Type=Integer32
_TptDiscoveryNotifyUnknown_Object=MibScalar
tptDiscoveryNotifyUnknown=_TptDiscoveryNotifyUnknown_Object((1,3,6,1,4,1,10734,3,3,3,1,50),_TptDiscoveryNotifyUnknown_Type())
tptDiscoveryNotifyUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:tptDiscoveryNotifyUnknown.setStatus(_D)
_TptDiscoveryNotifyStartTime_Type=Unsigned32
_TptDiscoveryNotifyStartTime_Object=MibScalar
tptDiscoveryNotifyStartTime=_TptDiscoveryNotifyStartTime_Object((1,3,6,1,4,1,10734,3,3,3,1,51),_TptDiscoveryNotifyStartTime_Type())
tptDiscoveryNotifyStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tptDiscoveryNotifyStartTime.setStatus(_D)
_TptDiscoveryNotifyStopTime_Type=Unsigned32
_TptDiscoveryNotifyStopTime_Object=MibScalar
tptDiscoveryNotifyStopTime=_TptDiscoveryNotifyStopTime_Object((1,3,6,1,4,1,10734,3,3,3,1,52),_TptDiscoveryNotifyStopTime_Type())
tptDiscoveryNotifyStopTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tptDiscoveryNotifyStopTime.setStatus(_D)
class _TptDiscoveryNotifyErrorText_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TptDiscoveryNotifyErrorText_Type.__name__=_F
_TptDiscoveryNotifyErrorText_Object=MibScalar
tptDiscoveryNotifyErrorText=_TptDiscoveryNotifyErrorText_Object((1,3,6,1,4,1,10734,3,3,3,1,53),_TptDiscoveryNotifyErrorText_Type())
tptDiscoveryNotifyErrorText.setMaxAccess(_C)
if mibBuilder.loadTexts:tptDiscoveryNotifyErrorText.setStatus(_D)
_TptDiscoveryNotifyHostNetAddr_Type=IpAddress
_TptDiscoveryNotifyHostNetAddr_Object=MibScalar
tptDiscoveryNotifyHostNetAddr=_TptDiscoveryNotifyHostNetAddr_Object((1,3,6,1,4,1,10734,3,3,3,1,54),_TptDiscoveryNotifyHostNetAddr_Type())
tptDiscoveryNotifyHostNetAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tptDiscoveryNotifyHostNetAddr.setStatus(_D)
class _TptDiscoveryNotifyHostDeviceID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptDiscoveryNotifyHostDeviceID_Type.__name__=_F
_TptDiscoveryNotifyHostDeviceID_Object=MibScalar
tptDiscoveryNotifyHostDeviceID=_TptDiscoveryNotifyHostDeviceID_Object((1,3,6,1,4,1,10734,3,3,3,1,55),_TptDiscoveryNotifyHostDeviceID_Type())
tptDiscoveryNotifyHostDeviceID.setMaxAccess(_C)
if mibBuilder.loadTexts:tptDiscoveryNotifyHostDeviceID.setStatus(_D)
class _TptDiscoveryNotifySchedID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptDiscoveryNotifySchedID_Type.__name__=_F
_TptDiscoveryNotifySchedID_Object=MibScalar
tptDiscoveryNotifySchedID=_TptDiscoveryNotifySchedID_Object((1,3,6,1,4,1,10734,3,3,3,1,56),_TptDiscoveryNotifySchedID_Type())
tptDiscoveryNotifySchedID.setMaxAccess(_C)
if mibBuilder.loadTexts:tptDiscoveryNotifySchedID.setStatus(_D)
class _TptSystemLogNotifyText_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_TptSystemLogNotifyText_Type.__name__=_F
_TptSystemLogNotifyText_Object=MibScalar
tptSystemLogNotifyText=_TptSystemLogNotifyText_Object((1,3,6,1,4,1,10734,3,3,3,1,92),_TptSystemLogNotifyText_Type())
tptSystemLogNotifyText.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSystemLogNotifyText.setStatus(_B)
_TptSystemLogNotifySequence_Type=Counter64
_TptSystemLogNotifySequence_Object=MibScalar
tptSystemLogNotifySequence=_TptSystemLogNotifySequence_Object((1,3,6,1,4,1,10734,3,3,3,1,93),_TptSystemLogNotifySequence_Type())
tptSystemLogNotifySequence.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSystemLogNotifySequence.setStatus(_B)
_TptSystemLogNotifySeverity_Type=SystemLogSeverity
_TptSystemLogNotifySeverity_Object=MibScalar
tptSystemLogNotifySeverity=_TptSystemLogNotifySeverity_Object((1,3,6,1,4,1,10734,3,3,3,1,94),_TptSystemLogNotifySeverity_Type())
tptSystemLogNotifySeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSystemLogNotifySeverity.setStatus(_B)
_TptSystemLogNotifyTimeSec_Type=Unsigned32
_TptSystemLogNotifyTimeSec_Object=MibScalar
tptSystemLogNotifyTimeSec=_TptSystemLogNotifyTimeSec_Object((1,3,6,1,4,1,10734,3,3,3,1,95),_TptSystemLogNotifyTimeSec_Type())
tptSystemLogNotifyTimeSec.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSystemLogNotifyTimeSec.setStatus(_B)
_TptSystemLogNotifyTimeNano_Type=Unsigned32
_TptSystemLogNotifyTimeNano_Object=MibScalar
tptSystemLogNotifyTimeNano=_TptSystemLogNotifyTimeNano_Object((1,3,6,1,4,1,10734,3,3,3,1,96),_TptSystemLogNotifyTimeNano_Type())
tptSystemLogNotifyTimeNano.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSystemLogNotifyTimeNano.setStatus(_B)
_TptQuarantineNotifyHostNetAddr_Type=IpAddress
_TptQuarantineNotifyHostNetAddr_Object=MibScalar
tptQuarantineNotifyHostNetAddr=_TptQuarantineNotifyHostNetAddr_Object((1,3,6,1,4,1,10734,3,3,3,1,132),_TptQuarantineNotifyHostNetAddr_Type())
tptQuarantineNotifyHostNetAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tptQuarantineNotifyHostNetAddr.setStatus(_B)
class _TptQuarantineNotifyReason_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptQuarantineNotifyReason_Type.__name__=_F
_TptQuarantineNotifyReason_Object=MibScalar
tptQuarantineNotifyReason=_TptQuarantineNotifyReason_Object((1,3,6,1,4,1,10734,3,3,3,1,133),_TptQuarantineNotifyReason_Type())
tptQuarantineNotifyReason.setMaxAccess(_C)
if mibBuilder.loadTexts:tptQuarantineNotifyReason.setStatus(_B)
class _TptQuarantineNotifySegmentName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_TptQuarantineNotifySegmentName_Type.__name__=_F
_TptQuarantineNotifySegmentName_Object=MibScalar
tptQuarantineNotifySegmentName=_TptQuarantineNotifySegmentName_Object((1,3,6,1,4,1,10734,3,3,3,1,134),_TptQuarantineNotifySegmentName_Type())
tptQuarantineNotifySegmentName.setMaxAccess(_C)
if mibBuilder.loadTexts:tptQuarantineNotifySegmentName.setStatus(_B)
_TptQuarantineNotifyAction_Type=AddOrRemove
_TptQuarantineNotifyAction_Object=MibScalar
tptQuarantineNotifyAction=_TptQuarantineNotifyAction_Object((1,3,6,1,4,1,10734,3,3,3,1,135),_TptQuarantineNotifyAction_Type())
tptQuarantineNotifyAction.setMaxAccess(_C)
if mibBuilder.loadTexts:tptQuarantineNotifyAction.setStatus(_B)
_TptQuarantineNotifyHostNetAddrV6_Type=Ipv6Address
_TptQuarantineNotifyHostNetAddrV6_Object=MibScalar
tptQuarantineNotifyHostNetAddrV6=_TptQuarantineNotifyHostNetAddrV6_Object((1,3,6,1,4,1,10734,3,3,3,1,136),_TptQuarantineNotifyHostNetAddrV6_Type())
tptQuarantineNotifyHostNetAddrV6.setMaxAccess(_C)
if mibBuilder.loadTexts:tptQuarantineNotifyHostNetAddrV6.setStatus(_B)
_TptCongestionPacketLoss_Type=Unsigned32
_TptCongestionPacketLoss_Object=MibScalar
tptCongestionPacketLoss=_TptCongestionPacketLoss_Object((1,3,6,1,4,1,10734,3,3,3,1,153),_TptCongestionPacketLoss_Type())
tptCongestionPacketLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:tptCongestionPacketLoss.setStatus(_B)
_TptCongestionNotifyPhase_Type=CongestionThresholdPhase
_TptCongestionNotifyPhase_Object=MibScalar
tptCongestionNotifyPhase=_TptCongestionNotifyPhase_Object((1,3,6,1,4,1,10734,3,3,3,1,154),_TptCongestionNotifyPhase_Type())
tptCongestionNotifyPhase.setMaxAccess(_C)
if mibBuilder.loadTexts:tptCongestionNotifyPhase.setStatus(_B)
_TptCongestionThreshold_Type=Unsigned32
_TptCongestionThreshold_Object=MibScalar
tptCongestionThreshold=_TptCongestionThreshold_Object((1,3,6,1,4,1,10734,3,3,3,1,155),_TptCongestionThreshold_Type())
tptCongestionThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tptCongestionThreshold.setStatus(_B)
_TptTier3CongestionPacketLoss_Type=Unsigned32
_TptTier3CongestionPacketLoss_Object=MibScalar
tptTier3CongestionPacketLoss=_TptTier3CongestionPacketLoss_Object((1,3,6,1,4,1,10734,3,3,3,1,156),_TptTier3CongestionPacketLoss_Type())
tptTier3CongestionPacketLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:tptTier3CongestionPacketLoss.setStatus(_B)
_TptTier3CongestionNotifyPhase_Type=CongestionThresholdPhase
_TptTier3CongestionNotifyPhase_Object=MibScalar
tptTier3CongestionNotifyPhase=_TptTier3CongestionNotifyPhase_Object((1,3,6,1,4,1,10734,3,3,3,1,157),_TptTier3CongestionNotifyPhase_Type())
tptTier3CongestionNotifyPhase.setMaxAccess(_C)
if mibBuilder.loadTexts:tptTier3CongestionNotifyPhase.setStatus(_B)
_TptTier3CongestionThreshold_Type=Unsigned32
_TptTier3CongestionThreshold_Object=MibScalar
tptTier3CongestionThreshold=_TptTier3CongestionThreshold_Object((1,3,6,1,4,1,10734,3,3,3,1,158),_TptTier3CongestionThreshold_Type())
tptTier3CongestionThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tptTier3CongestionThreshold.setStatus(_B)
_TptAuditLogNotifyTime_Type=DateAndTime
_TptAuditLogNotifyTime_Object=MibScalar
tptAuditLogNotifyTime=_TptAuditLogNotifyTime_Object((1,3,6,1,4,1,10734,3,3,3,1,170),_TptAuditLogNotifyTime_Type())
tptAuditLogNotifyTime.setMaxAccess(_G)
if mibBuilder.loadTexts:tptAuditLogNotifyTime.setStatus(_B)
_TptAuditLogNotifyAccess_Type=Unsigned32
_TptAuditLogNotifyAccess_Object=MibScalar
tptAuditLogNotifyAccess=_TptAuditLogNotifyAccess_Object((1,3,6,1,4,1,10734,3,3,3,1,171),_TptAuditLogNotifyAccess_Type())
tptAuditLogNotifyAccess.setMaxAccess(_G)
if mibBuilder.loadTexts:tptAuditLogNotifyAccess.setStatus(_B)
class _TptAuditLogNotifyType_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptAuditLogNotifyType_Type.__name__=_I
_TptAuditLogNotifyType_Object=MibScalar
tptAuditLogNotifyType=_TptAuditLogNotifyType_Object((1,3,6,1,4,1,10734,3,3,3,1,172),_TptAuditLogNotifyType_Type())
tptAuditLogNotifyType.setMaxAccess(_G)
if mibBuilder.loadTexts:tptAuditLogNotifyType.setStatus(_B)
_TptAuditLogNotifyIpAddrType_Type=InetAddressType
_TptAuditLogNotifyIpAddrType_Object=MibScalar
tptAuditLogNotifyIpAddrType=_TptAuditLogNotifyIpAddrType_Object((1,3,6,1,4,1,10734,3,3,3,1,173),_TptAuditLogNotifyIpAddrType_Type())
tptAuditLogNotifyIpAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:tptAuditLogNotifyIpAddrType.setStatus(_B)
_TptAuditLogNotifyIpAddr_Type=InetAddress
_TptAuditLogNotifyIpAddr_Object=MibScalar
tptAuditLogNotifyIpAddr=_TptAuditLogNotifyIpAddr_Object((1,3,6,1,4,1,10734,3,3,3,1,174),_TptAuditLogNotifyIpAddr_Type())
tptAuditLogNotifyIpAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:tptAuditLogNotifyIpAddr.setStatus(_B)
_TptAuditLogNotifyCategory_Type=AuditLogCategory
_TptAuditLogNotifyCategory_Object=MibScalar
tptAuditLogNotifyCategory=_TptAuditLogNotifyCategory_Object((1,3,6,1,4,1,10734,3,3,3,1,175),_TptAuditLogNotifyCategory_Type())
tptAuditLogNotifyCategory.setMaxAccess(_G)
if mibBuilder.loadTexts:tptAuditLogNotifyCategory.setStatus(_B)
_TptAuditLogNotifyResult_Type=AuditLogResult
_TptAuditLogNotifyResult_Object=MibScalar
tptAuditLogNotifyResult=_TptAuditLogNotifyResult_Object((1,3,6,1,4,1,10734,3,3,3,1,176),_TptAuditLogNotifyResult_Type())
tptAuditLogNotifyResult.setMaxAccess(_G)
if mibBuilder.loadTexts:tptAuditLogNotifyResult.setStatus(_B)
class _TptAuditLogNotifyUser_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TptAuditLogNotifyUser_Type.__name__=_I
_TptAuditLogNotifyUser_Object=MibScalar
tptAuditLogNotifyUser=_TptAuditLogNotifyUser_Object((1,3,6,1,4,1,10734,3,3,3,1,177),_TptAuditLogNotifyUser_Type())
tptAuditLogNotifyUser.setMaxAccess(_G)
if mibBuilder.loadTexts:tptAuditLogNotifyUser.setStatus(_B)
class _TptAuditLogNotifyMessage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4096))
_TptAuditLogNotifyMessage_Type.__name__=_F
_TptAuditLogNotifyMessage_Object=MibScalar
tptAuditLogNotifyMessage=_TptAuditLogNotifyMessage_Object((1,3,6,1,4,1,10734,3,3,3,1,178),_TptAuditLogNotifyMessage_Type())
tptAuditLogNotifyMessage.setMaxAccess(_G)
if mibBuilder.loadTexts:tptAuditLogNotifyMessage.setStatus(_B)
_TptQuarantineNotifySslInspected_Type=SslInspectedFlag
_TptQuarantineNotifySslInspected_Object=MibScalar
tptQuarantineNotifySslInspected=_TptQuarantineNotifySslInspected_Object((1,3,6,1,4,1,10734,3,3,3,1,181),_TptQuarantineNotifySslInspected_Type())
tptQuarantineNotifySslInspected.setMaxAccess(_C)
if mibBuilder.loadTexts:tptQuarantineNotifySslInspected.setStatus(_B)
_TptAuditLogCapacityNotifyPercent_Type=Unsigned32
_TptAuditLogCapacityNotifyPercent_Object=MibScalar
tptAuditLogCapacityNotifyPercent=_TptAuditLogCapacityNotifyPercent_Object((1,3,6,1,4,1,10734,3,3,3,1,201),_TptAuditLogCapacityNotifyPercent_Type())
tptAuditLogCapacityNotifyPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:tptAuditLogCapacityNotifyPercent.setStatus(_B)
_TptAuditLogCapacityOrFailureNotifyTime_Type=Unsigned32
_TptAuditLogCapacityOrFailureNotifyTime_Object=MibScalar
tptAuditLogCapacityOrFailureNotifyTime=_TptAuditLogCapacityOrFailureNotifyTime_Object((1,3,6,1,4,1,10734,3,3,3,1,202),_TptAuditLogCapacityOrFailureNotifyTime_Type())
tptAuditLogCapacityOrFailureNotifyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tptAuditLogCapacityOrFailureNotifyTime.setStatus(_B)
tptManagedNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,9))
tptManagedNotify.setObjects((_A,_E))
if mibBuilder.loadTexts:tptManagedNotify.setStatus(_B)
tptUnmanagedNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,10))
tptUnmanagedNotify.setObjects((_A,_E))
if mibBuilder.loadTexts:tptUnmanagedNotify.setStatus(_B)
tptRolloverNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,11))
tptRolloverNotify.setObjects(*((_A,_E),(_A,_K),(_A,_H)))
if mibBuilder.loadTexts:tptRolloverNotify.setStatus(_B)
tptDiscoveryNotifyStartStop=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,12))
tptDiscoveryNotifyStartStop.setObjects(*((_A,_E),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:tptDiscoveryNotifyStartStop.setStatus(_D)
tptDiscoveryNotifyNewHost=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,13))
tptDiscoveryNotifyNewHost.setObjects(*((_A,_E),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:tptDiscoveryNotifyNewHost.setStatus(_D)
tptSystemLogNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,16))
tptSystemLogNotify.setObjects(*((_A,_E),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:tptSystemLogNotify.setStatus(_B)
tptQuarantineNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,20))
tptQuarantineNotify.setObjects(*((_A,_E),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:tptQuarantineNotify.setStatus(_B)
tptCongestionThresholdNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,25))
tptCongestionThresholdNotify.setObjects(*((_A,_E),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:tptCongestionThresholdNotify.setStatus(_B)
tptiTier3CongestionThresholdNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,26))
tptiTier3CongestionThresholdNotify.setObjects(*((_A,_E),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:tptiTier3CongestionThresholdNotify.setStatus(_B)
tptAuditLogNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,60))
tptAuditLogNotify.setObjects(*((_A,_E),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:tptAuditLogNotify.setStatus(_B)
tptAuditLogCapacityNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,61))
tptAuditLogCapacityNotify.setObjects(*((_A,_E),(_A,_A0),(_A,_H)))
if mibBuilder.loadTexts:tptAuditLogCapacityNotify.setStatus(_B)
tptLoggingFailureNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,62))
tptLoggingFailureNotify.setObjects(*((_A,_E),(_A,_H)))
if mibBuilder.loadTexts:tptLoggingFailureNotify.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'LogFileType':LogFileType,'DiscoveryDelta':DiscoveryDelta,'SystemLogSeverity':SystemLogSeverity,'AddOrRemove':AddOrRemove,'CongestionThresholdPhase':CongestionThresholdPhase,'AuditLogResult':AuditLogResult,'AuditLogCategory':AuditLogCategory,'tpt-misc-notify':tpt_misc_notify,'tptManagedNotify':tptManagedNotify,'tptUnmanagedNotify':tptUnmanagedNotify,'tptRolloverNotify':tptRolloverNotify,'tptDiscoveryNotifyStartStop':tptDiscoveryNotifyStartStop,'tptDiscoveryNotifyNewHost':tptDiscoveryNotifyNewHost,'tptSystemLogNotify':tptSystemLogNotify,'tptQuarantineNotify':tptQuarantineNotify,'tptCongestionThresholdNotify':tptCongestionThresholdNotify,'tptiTier3CongestionThresholdNotify':tptiTier3CongestionThresholdNotify,'tptAuditLogNotify':tptAuditLogNotify,'tptAuditLogCapacityNotify':tptAuditLogCapacityNotify,'tptLoggingFailureNotify':tptLoggingFailureNotify,_E:tptMiscNotifyDeviceID,_K:tptRolloverNotifyFileType,'tptRolloverNotifyMaxFiles':tptRolloverNotifyMaxFiles,'tptRolloverNotifyNumFiles':tptRolloverNotifyNumFiles,_H:tptRolloverNotifyTime,_L:tptDiscoveryNotifyScanID,_M:tptDiscoveryNotifySegmentName,_N:tptDiscoveryNotifyScanRange,_O:tptDiscoveryNotifyDelta,_P:tptDiscoveryNotifyNewHosts,_Q:tptDiscoveryNotifyChanged,_R:tptDiscoveryNotifyUnchanged,_S:tptDiscoveryNotifyNotFound,_T:tptDiscoveryNotifyUnknown,_U:tptDiscoveryNotifyStartTime,_V:tptDiscoveryNotifyStopTime,_W:tptDiscoveryNotifyErrorText,_Y:tptDiscoveryNotifyHostNetAddr,_Z:tptDiscoveryNotifyHostDeviceID,_X:tptDiscoveryNotifySchedID,_a:tptSystemLogNotifyText,_b:tptSystemLogNotifySequence,_c:tptSystemLogNotifySeverity,_d:tptSystemLogNotifyTimeSec,_e:tptSystemLogNotifyTimeNano,_f:tptQuarantineNotifyHostNetAddr,_g:tptQuarantineNotifyReason,_h:tptQuarantineNotifySegmentName,_i:tptQuarantineNotifyAction,_j:tptQuarantineNotifyHostNetAddrV6,_m:tptCongestionPacketLoss,_l:tptCongestionNotifyPhase,_n:tptCongestionThreshold,_p:tptTier3CongestionPacketLoss,_o:tptTier3CongestionNotifyPhase,_q:tptTier3CongestionThreshold,_r:tptAuditLogNotifyTime,_s:tptAuditLogNotifyAccess,_t:tptAuditLogNotifyType,_u:tptAuditLogNotifyIpAddrType,_v:tptAuditLogNotifyIpAddr,_w:tptAuditLogNotifyCategory,_x:tptAuditLogNotifyResult,_y:tptAuditLogNotifyUser,_z:tptAuditLogNotifyMessage,_k:tptQuarantineNotifySslInspected,_A0:tptAuditLogCapacityNotifyPercent,'tptAuditLogCapacityOrFailureNotifyTime':tptAuditLogCapacityOrFailureNotifyTime})