_A0='ntcTsOIpInConfGrpV1Standard'
_z='ntcTsOIpInMaxTrafficJitter'
_y='ntcTsOIpInPcrPid'
_x='ntcTsOIpInAutoPcrDetection'
_w='ntcTsOIpInInputRateType'
_v='ntcTsOIpInMulticastSourceB'
_u='ntcTsOIpInMulticastSourceA'
_t='ntcTsOIpInAlmInvalidTsBitRate'
_s='ntcTsOIpInAlmRtpNoSync'
_r='ntcTsOIpInAlmBufferUnflow'
_q='ntcTsOIpInAlmBufferOverflow'
_p='ntcTsOIpInAlmNoInputData'
_o='ntcTsOIpInAlmGeneralTsOverIpIn'
_n='ntcTsOIpInMonActivePCRPID'
_m='ntcTsOIpInMonRtpFecDropCount'
_l='ntcTsOIpInMonRtpRepairCount'
_k='ntcTsOIpInMonRtpDropCount'
_j='ntcTsOIpInMonTsOverflowCount'
_i='ntcTsOIpInMonTsDropCount'
_h='ntcTsOIpInMonTsOutCount'
_g='ntcTsOIpInMonRtpRowFecInCount'
_f='ntcTsOIpInMonRtpColumnFecInCount'
_e='ntcTsOIpInMonRtpInCount'
_d='ntcTsOIpInMonTsInCount'
_c='ntcTsOIpInMonRtpFecScheme'
_b='ntcTsOIpInMonSourceInfo'
_a='ntcTsOIpInMonMaxBufferFilling'
_Z='ntcTsOIpInMonMinBufferFilling'
_Y='ntcTsOIpInMonBufferDelay'
_X='ntcTsOIpInMonInputTsBitRate'
_W='ntcTsOIpInMonResetCounters'
_V='ntcTsOIpInInputTsBitRate'
_U='ntcTsOIpInMaxBufferDelay'
_T='ntcTsOIpInTrafficProfile'
_S='ntcTsOIpInUdpPort'
_R='ntcTsOIpInMulticastAddress'
_Q='ntcTsOIpInIpAddressType'
_P='ntcTsOIpInTsEncapProtocol'
_O='ntcTsOIpInInputSelection'
_N='ntcTsOIpInEnable'
_M='0.0.0.0'
_L='IpAddress'
_K='DisplayString'
_J='NtcNetworkAddress'
_I='NtcEnable'
_H='ms'
_G='Unsigned32'
_F='Integer32'
_E='packets'
_D='read-write'
_C='read-only'
_B='NEWTEC-TSOVERIPIN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable,NtcNetworkAddress=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_I,_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,_L,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','TextualConvention')
ntcTsOverIpIn=ModuleIdentity((1,3,6,1,4,1,5835,5,2,600))
if mibBuilder.loadTexts:ntcTsOverIpIn.setRevisions(('2017-07-10 12:00','2016-02-02 07:00','2015-02-19 09:00','2014-09-09 09:00','2013-03-27 10:00','2012-06-28 12:00'))
_NtcTsOIpInObjects_ObjectIdentity=ObjectIdentity
ntcTsOIpInObjects=_NtcTsOIpInObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,600,1))
if mibBuilder.loadTexts:ntcTsOIpInObjects.setStatus(_A)
class _NtcTsOIpInEnable_Type(NtcEnable):defaultValue=0
_NtcTsOIpInEnable_Type.__name__=_I
_NtcTsOIpInEnable_Object=MibScalar
ntcTsOIpInEnable=_NtcTsOIpInEnable_Object((1,3,6,1,4,1,5835,5,2,600,1,1),_NtcTsOIpInEnable_Type())
ntcTsOIpInEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsOIpInEnable.setStatus(_A)
class _NtcTsOIpInInputSelection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('data1',2),('data2',3),('data',4),('any',5)))
_NtcTsOIpInInputSelection_Type.__name__=_F
_NtcTsOIpInInputSelection_Object=MibScalar
ntcTsOIpInInputSelection=_NtcTsOIpInInputSelection_Object((1,3,6,1,4,1,5835,5,2,600,1,2),_NtcTsOIpInInputSelection_Type())
ntcTsOIpInInputSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsOIpInInputSelection.setStatus(_A)
class _NtcTsOIpInTsEncapProtocol_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('udp',0),('rtp',1),('rtpfec',2)))
_NtcTsOIpInTsEncapProtocol_Type.__name__=_F
_NtcTsOIpInTsEncapProtocol_Object=MibScalar
ntcTsOIpInTsEncapProtocol=_NtcTsOIpInTsEncapProtocol_Object((1,3,6,1,4,1,5835,5,2,600,1,3),_NtcTsOIpInTsEncapProtocol_Type())
ntcTsOIpInTsEncapProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsOIpInTsEncapProtocol.setStatus(_A)
class _NtcTsOIpInIpAddressType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unicast',0),('multicast',1)))
_NtcTsOIpInIpAddressType_Type.__name__=_F
_NtcTsOIpInIpAddressType_Object=MibScalar
ntcTsOIpInIpAddressType=_NtcTsOIpInIpAddressType_Object((1,3,6,1,4,1,5835,5,2,600,1,4),_NtcTsOIpInIpAddressType_Type())
ntcTsOIpInIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsOIpInIpAddressType.setStatus(_A)
class _NtcTsOIpInMulticastAddress_Type(IpAddress):defaultHexValue='e0010001'
_NtcTsOIpInMulticastAddress_Type.__name__=_L
_NtcTsOIpInMulticastAddress_Object=MibScalar
ntcTsOIpInMulticastAddress=_NtcTsOIpInMulticastAddress_Object((1,3,6,1,4,1,5835,5,2,600,1,5),_NtcTsOIpInMulticastAddress_Type())
ntcTsOIpInMulticastAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsOIpInMulticastAddress.setStatus(_A)
class _NtcTsOIpInUdpPort_Type(Unsigned32):defaultValue=56789;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NtcTsOIpInUdpPort_Type.__name__=_G
_NtcTsOIpInUdpPort_Object=MibScalar
ntcTsOIpInUdpPort=_NtcTsOIpInUdpPort_Object((1,3,6,1,4,1,5835,5,2,600,1,6),_NtcTsOIpInUdpPort_Type())
ntcTsOIpInUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsOIpInUdpPort.setStatus(_A)
class _NtcTsOIpInTrafficProfile_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('vbr',0),('cbr',1)))
_NtcTsOIpInTrafficProfile_Type.__name__=_F
_NtcTsOIpInTrafficProfile_Object=MibScalar
ntcTsOIpInTrafficProfile=_NtcTsOIpInTrafficProfile_Object((1,3,6,1,4,1,5835,5,2,600,1,7),_NtcTsOIpInTrafficProfile_Type())
ntcTsOIpInTrafficProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsOIpInTrafficProfile.setStatus(_A)
class _NtcTsOIpInMaxTrafficJitter_Type(Unsigned32):defaultValue=50
_NtcTsOIpInMaxTrafficJitter_Type.__name__=_G
_NtcTsOIpInMaxTrafficJitter_Object=MibScalar
ntcTsOIpInMaxTrafficJitter=_NtcTsOIpInMaxTrafficJitter_Object((1,3,6,1,4,1,5835,5,2,600,1,8),_NtcTsOIpInMaxTrafficJitter_Type())
ntcTsOIpInMaxTrafficJitter.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsOIpInMaxTrafficJitter.setStatus('deprecated')
if mibBuilder.loadTexts:ntcTsOIpInMaxTrafficJitter.setUnits(_H)
class _NtcTsOIpInMaxBufferDelay_Type(Unsigned32):defaultValue=250
_NtcTsOIpInMaxBufferDelay_Type.__name__=_G
_NtcTsOIpInMaxBufferDelay_Object=MibScalar
ntcTsOIpInMaxBufferDelay=_NtcTsOIpInMaxBufferDelay_Object((1,3,6,1,4,1,5835,5,2,600,1,9),_NtcTsOIpInMaxBufferDelay_Type())
ntcTsOIpInMaxBufferDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsOIpInMaxBufferDelay.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpInMaxBufferDelay.setUnits(_H)
class _NtcTsOIpInInputTsBitRate_Type(Unsigned32):defaultValue=1000000
_NtcTsOIpInInputTsBitRate_Type.__name__=_G
_NtcTsOIpInInputTsBitRate_Object=MibScalar
ntcTsOIpInInputTsBitRate=_NtcTsOIpInInputTsBitRate_Object((1,3,6,1,4,1,5835,5,2,600,1,10),_NtcTsOIpInInputTsBitRate_Type())
ntcTsOIpInInputTsBitRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsOIpInInputTsBitRate.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpInInputTsBitRate.setUnits('bps')
_NtcTsOIpInMonitor_ObjectIdentity=ObjectIdentity
ntcTsOIpInMonitor=_NtcTsOIpInMonitor_ObjectIdentity((1,3,6,1,4,1,5835,5,2,600,1,11))
if mibBuilder.loadTexts:ntcTsOIpInMonitor.setStatus(_A)
class _NtcTsOIpInMonResetCounters_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('counting',0),('reset',1)))
_NtcTsOIpInMonResetCounters_Type.__name__=_F
_NtcTsOIpInMonResetCounters_Object=MibScalar
ntcTsOIpInMonResetCounters=_NtcTsOIpInMonResetCounters_Object((1,3,6,1,4,1,5835,5,2,600,1,11,1),_NtcTsOIpInMonResetCounters_Type())
ntcTsOIpInMonResetCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsOIpInMonResetCounters.setStatus(_A)
_NtcTsOIpInMonInputTsBitRate_Type=Unsigned32
_NtcTsOIpInMonInputTsBitRate_Object=MibScalar
ntcTsOIpInMonInputTsBitRate=_NtcTsOIpInMonInputTsBitRate_Object((1,3,6,1,4,1,5835,5,2,600,1,11,2),_NtcTsOIpInMonInputTsBitRate_Type())
ntcTsOIpInMonInputTsBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonInputTsBitRate.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpInMonInputTsBitRate.setUnits('bps')
_NtcTsOIpInMonBufferDelay_Type=Unsigned32
_NtcTsOIpInMonBufferDelay_Object=MibScalar
ntcTsOIpInMonBufferDelay=_NtcTsOIpInMonBufferDelay_Object((1,3,6,1,4,1,5835,5,2,600,1,11,3),_NtcTsOIpInMonBufferDelay_Type())
ntcTsOIpInMonBufferDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonBufferDelay.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpInMonBufferDelay.setUnits(_H)
_NtcTsOIpInMonMinBufferFilling_Type=Unsigned32
_NtcTsOIpInMonMinBufferFilling_Object=MibScalar
ntcTsOIpInMonMinBufferFilling=_NtcTsOIpInMonMinBufferFilling_Object((1,3,6,1,4,1,5835,5,2,600,1,11,4),_NtcTsOIpInMonMinBufferFilling_Type())
ntcTsOIpInMonMinBufferFilling.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonMinBufferFilling.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpInMonMinBufferFilling.setUnits(_H)
_NtcTsOIpInMonMaxBufferFilling_Type=Unsigned32
_NtcTsOIpInMonMaxBufferFilling_Object=MibScalar
ntcTsOIpInMonMaxBufferFilling=_NtcTsOIpInMonMaxBufferFilling_Object((1,3,6,1,4,1,5835,5,2,600,1,11,5),_NtcTsOIpInMonMaxBufferFilling_Type())
ntcTsOIpInMonMaxBufferFilling.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonMaxBufferFilling.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpInMonMaxBufferFilling.setUnits(_H)
class _NtcTsOIpInMonSourceInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcTsOIpInMonSourceInfo_Type.__name__=_K
_NtcTsOIpInMonSourceInfo_Object=MibScalar
ntcTsOIpInMonSourceInfo=_NtcTsOIpInMonSourceInfo_Object((1,3,6,1,4,1,5835,5,2,600,1,11,6),_NtcTsOIpInMonSourceInfo_Type())
ntcTsOIpInMonSourceInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonSourceInfo.setStatus(_A)
class _NtcTsOIpInMonRtpFecScheme_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcTsOIpInMonRtpFecScheme_Type.__name__=_K
_NtcTsOIpInMonRtpFecScheme_Object=MibScalar
ntcTsOIpInMonRtpFecScheme=_NtcTsOIpInMonRtpFecScheme_Object((1,3,6,1,4,1,5835,5,2,600,1,11,7),_NtcTsOIpInMonRtpFecScheme_Type())
ntcTsOIpInMonRtpFecScheme.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonRtpFecScheme.setStatus(_A)
_NtcTsOIpInMonTsInCount_Type=Counter32
_NtcTsOIpInMonTsInCount_Object=MibScalar
ntcTsOIpInMonTsInCount=_NtcTsOIpInMonTsInCount_Object((1,3,6,1,4,1,5835,5,2,600,1,11,8),_NtcTsOIpInMonTsInCount_Type())
ntcTsOIpInMonTsInCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonTsInCount.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpInMonTsInCount.setUnits(_E)
_NtcTsOIpInMonRtpInCount_Type=Counter32
_NtcTsOIpInMonRtpInCount_Object=MibScalar
ntcTsOIpInMonRtpInCount=_NtcTsOIpInMonRtpInCount_Object((1,3,6,1,4,1,5835,5,2,600,1,11,9),_NtcTsOIpInMonRtpInCount_Type())
ntcTsOIpInMonRtpInCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonRtpInCount.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpInMonRtpInCount.setUnits(_E)
_NtcTsOIpInMonRtpColumnFecInCount_Type=Counter32
_NtcTsOIpInMonRtpColumnFecInCount_Object=MibScalar
ntcTsOIpInMonRtpColumnFecInCount=_NtcTsOIpInMonRtpColumnFecInCount_Object((1,3,6,1,4,1,5835,5,2,600,1,11,10),_NtcTsOIpInMonRtpColumnFecInCount_Type())
ntcTsOIpInMonRtpColumnFecInCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonRtpColumnFecInCount.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpInMonRtpColumnFecInCount.setUnits(_E)
_NtcTsOIpInMonRtpRowFecInCount_Type=Counter32
_NtcTsOIpInMonRtpRowFecInCount_Object=MibScalar
ntcTsOIpInMonRtpRowFecInCount=_NtcTsOIpInMonRtpRowFecInCount_Object((1,3,6,1,4,1,5835,5,2,600,1,11,11),_NtcTsOIpInMonRtpRowFecInCount_Type())
ntcTsOIpInMonRtpRowFecInCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonRtpRowFecInCount.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpInMonRtpRowFecInCount.setUnits(_E)
_NtcTsOIpInMonTsOutCount_Type=Counter32
_NtcTsOIpInMonTsOutCount_Object=MibScalar
ntcTsOIpInMonTsOutCount=_NtcTsOIpInMonTsOutCount_Object((1,3,6,1,4,1,5835,5,2,600,1,11,12),_NtcTsOIpInMonTsOutCount_Type())
ntcTsOIpInMonTsOutCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonTsOutCount.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpInMonTsOutCount.setUnits(_E)
_NtcTsOIpInMonTsDropCount_Type=Counter32
_NtcTsOIpInMonTsDropCount_Object=MibScalar
ntcTsOIpInMonTsDropCount=_NtcTsOIpInMonTsDropCount_Object((1,3,6,1,4,1,5835,5,2,600,1,11,13),_NtcTsOIpInMonTsDropCount_Type())
ntcTsOIpInMonTsDropCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonTsDropCount.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpInMonTsDropCount.setUnits(_E)
_NtcTsOIpInMonTsOverflowCount_Type=Counter32
_NtcTsOIpInMonTsOverflowCount_Object=MibScalar
ntcTsOIpInMonTsOverflowCount=_NtcTsOIpInMonTsOverflowCount_Object((1,3,6,1,4,1,5835,5,2,600,1,11,14),_NtcTsOIpInMonTsOverflowCount_Type())
ntcTsOIpInMonTsOverflowCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonTsOverflowCount.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpInMonTsOverflowCount.setUnits(_E)
_NtcTsOIpInMonRtpDropCount_Type=Counter32
_NtcTsOIpInMonRtpDropCount_Object=MibScalar
ntcTsOIpInMonRtpDropCount=_NtcTsOIpInMonRtpDropCount_Object((1,3,6,1,4,1,5835,5,2,600,1,11,15),_NtcTsOIpInMonRtpDropCount_Type())
ntcTsOIpInMonRtpDropCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonRtpDropCount.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpInMonRtpDropCount.setUnits(_E)
_NtcTsOIpInMonRtpRepairCount_Type=Counter32
_NtcTsOIpInMonRtpRepairCount_Object=MibScalar
ntcTsOIpInMonRtpRepairCount=_NtcTsOIpInMonRtpRepairCount_Object((1,3,6,1,4,1,5835,5,2,600,1,11,16),_NtcTsOIpInMonRtpRepairCount_Type())
ntcTsOIpInMonRtpRepairCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonRtpRepairCount.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpInMonRtpRepairCount.setUnits(_E)
_NtcTsOIpInMonRtpFecDropCount_Type=Counter32
_NtcTsOIpInMonRtpFecDropCount_Object=MibScalar
ntcTsOIpInMonRtpFecDropCount=_NtcTsOIpInMonRtpFecDropCount_Object((1,3,6,1,4,1,5835,5,2,600,1,11,17),_NtcTsOIpInMonRtpFecDropCount_Type())
ntcTsOIpInMonRtpFecDropCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonRtpFecDropCount.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpInMonRtpFecDropCount.setUnits(_E)
class _NtcTsOIpInMonActivePCRPID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8190))
_NtcTsOIpInMonActivePCRPID_Type.__name__=_G
_NtcTsOIpInMonActivePCRPID_Object=MibScalar
ntcTsOIpInMonActivePCRPID=_NtcTsOIpInMonActivePCRPID_Object((1,3,6,1,4,1,5835,5,2,600,1,11,18),_NtcTsOIpInMonActivePCRPID_Type())
ntcTsOIpInMonActivePCRPID.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInMonActivePCRPID.setStatus(_A)
_NtcTsOIpInAlarm_ObjectIdentity=ObjectIdentity
ntcTsOIpInAlarm=_NtcTsOIpInAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,600,1,12))
if mibBuilder.loadTexts:ntcTsOIpInAlarm.setStatus(_A)
_NtcTsOIpInAlmGeneralTsOverIpIn_Type=NtcAlarmState
_NtcTsOIpInAlmGeneralTsOverIpIn_Object=MibScalar
ntcTsOIpInAlmGeneralTsOverIpIn=_NtcTsOIpInAlmGeneralTsOverIpIn_Object((1,3,6,1,4,1,5835,5,2,600,1,12,1),_NtcTsOIpInAlmGeneralTsOverIpIn_Type())
ntcTsOIpInAlmGeneralTsOverIpIn.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInAlmGeneralTsOverIpIn.setStatus(_A)
_NtcTsOIpInAlmNoInputData_Type=NtcAlarmState
_NtcTsOIpInAlmNoInputData_Object=MibScalar
ntcTsOIpInAlmNoInputData=_NtcTsOIpInAlmNoInputData_Object((1,3,6,1,4,1,5835,5,2,600,1,12,2),_NtcTsOIpInAlmNoInputData_Type())
ntcTsOIpInAlmNoInputData.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInAlmNoInputData.setStatus(_A)
_NtcTsOIpInAlmBufferOverflow_Type=NtcAlarmState
_NtcTsOIpInAlmBufferOverflow_Object=MibScalar
ntcTsOIpInAlmBufferOverflow=_NtcTsOIpInAlmBufferOverflow_Object((1,3,6,1,4,1,5835,5,2,600,1,12,3),_NtcTsOIpInAlmBufferOverflow_Type())
ntcTsOIpInAlmBufferOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInAlmBufferOverflow.setStatus(_A)
_NtcTsOIpInAlmBufferUnflow_Type=NtcAlarmState
_NtcTsOIpInAlmBufferUnflow_Object=MibScalar
ntcTsOIpInAlmBufferUnflow=_NtcTsOIpInAlmBufferUnflow_Object((1,3,6,1,4,1,5835,5,2,600,1,12,4),_NtcTsOIpInAlmBufferUnflow_Type())
ntcTsOIpInAlmBufferUnflow.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInAlmBufferUnflow.setStatus(_A)
_NtcTsOIpInAlmRtpNoSync_Type=NtcAlarmState
_NtcTsOIpInAlmRtpNoSync_Object=MibScalar
ntcTsOIpInAlmRtpNoSync=_NtcTsOIpInAlmRtpNoSync_Object((1,3,6,1,4,1,5835,5,2,600,1,12,5),_NtcTsOIpInAlmRtpNoSync_Type())
ntcTsOIpInAlmRtpNoSync.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInAlmRtpNoSync.setStatus(_A)
_NtcTsOIpInAlmInvalidTsBitRate_Type=NtcAlarmState
_NtcTsOIpInAlmInvalidTsBitRate_Object=MibScalar
ntcTsOIpInAlmInvalidTsBitRate=_NtcTsOIpInAlmInvalidTsBitRate_Object((1,3,6,1,4,1,5835,5,2,600,1,12,6),_NtcTsOIpInAlmInvalidTsBitRate_Type())
ntcTsOIpInAlmInvalidTsBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpInAlmInvalidTsBitRate.setStatus(_A)
class _NtcTsOIpInMulticastSourceA_Type(NtcNetworkAddress):defaultValue=OctetString(_M)
_NtcTsOIpInMulticastSourceA_Type.__name__=_J
_NtcTsOIpInMulticastSourceA_Object=MibScalar
ntcTsOIpInMulticastSourceA=_NtcTsOIpInMulticastSourceA_Object((1,3,6,1,4,1,5835,5,2,600,1,13),_NtcTsOIpInMulticastSourceA_Type())
ntcTsOIpInMulticastSourceA.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsOIpInMulticastSourceA.setStatus(_A)
class _NtcTsOIpInMulticastSourceB_Type(NtcNetworkAddress):defaultValue=OctetString(_M)
_NtcTsOIpInMulticastSourceB_Type.__name__=_J
_NtcTsOIpInMulticastSourceB_Object=MibScalar
ntcTsOIpInMulticastSourceB=_NtcTsOIpInMulticastSourceB_Object((1,3,6,1,4,1,5835,5,2,600,1,14),_NtcTsOIpInMulticastSourceB_Type())
ntcTsOIpInMulticastSourceB.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsOIpInMulticastSourceB.setStatus(_A)
class _NtcTsOIpInInputRateType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('userdefined',0),('pcr',1)))
_NtcTsOIpInInputRateType_Type.__name__=_F
_NtcTsOIpInInputRateType_Object=MibScalar
ntcTsOIpInInputRateType=_NtcTsOIpInInputRateType_Object((1,3,6,1,4,1,5835,5,2,600,1,15),_NtcTsOIpInInputRateType_Type())
ntcTsOIpInInputRateType.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsOIpInInputRateType.setStatus(_A)
class _NtcTsOIpInAutoPcrDetection_Type(NtcEnable):defaultValue=1
_NtcTsOIpInAutoPcrDetection_Type.__name__=_I
_NtcTsOIpInAutoPcrDetection_Object=MibScalar
ntcTsOIpInAutoPcrDetection=_NtcTsOIpInAutoPcrDetection_Object((1,3,6,1,4,1,5835,5,2,600,1,16),_NtcTsOIpInAutoPcrDetection_Type())
ntcTsOIpInAutoPcrDetection.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsOIpInAutoPcrDetection.setStatus(_A)
class _NtcTsOIpInPcrPid_Type(Unsigned32):defaultValue=8191;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_NtcTsOIpInPcrPid_Type.__name__=_G
_NtcTsOIpInPcrPid_Object=MibScalar
ntcTsOIpInPcrPid=_NtcTsOIpInPcrPid_Object((1,3,6,1,4,1,5835,5,2,600,1,17),_NtcTsOIpInPcrPid_Type())
ntcTsOIpInPcrPid.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsOIpInPcrPid.setStatus(_A)
_NtcTsOIpInConformance_ObjectIdentity=ObjectIdentity
ntcTsOIpInConformance=_NtcTsOIpInConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,600,2))
if mibBuilder.loadTexts:ntcTsOIpInConformance.setStatus(_A)
_NtcTsOIpInConfCompliance_ObjectIdentity=ObjectIdentity
ntcTsOIpInConfCompliance=_NtcTsOIpInConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,600,2,1))
if mibBuilder.loadTexts:ntcTsOIpInConfCompliance.setStatus(_A)
_NtcTsOIpInConfGroup_ObjectIdentity=ObjectIdentity
ntcTsOIpInConfGroup=_NtcTsOIpInConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,600,2,2))
if mibBuilder.loadTexts:ntcTsOIpInConfGroup.setStatus(_A)
ntcTsOIpInConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,600,2,2,1))
ntcTsOIpInConfGrpV1Standard.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:ntcTsOIpInConfGrpV1Standard.setStatus(_A)
ntcTsOIpInConfGrpObsolete=ObjectGroup((1,3,6,1,4,1,5835,5,2,600,2,2,2))
ntcTsOIpInConfGrpObsolete.setObjects((_B,_z))
if mibBuilder.loadTexts:ntcTsOIpInConfGrpObsolete.setStatus('obsolete')
ntcTsOIpInConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,600,2,1,1))
ntcTsOIpInConfCompV1Standard.setObjects((_B,_A0))
if mibBuilder.loadTexts:ntcTsOIpInConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcTsOverIpIn':ntcTsOverIpIn,'ntcTsOIpInObjects':ntcTsOIpInObjects,_N:ntcTsOIpInEnable,_O:ntcTsOIpInInputSelection,_P:ntcTsOIpInTsEncapProtocol,_Q:ntcTsOIpInIpAddressType,_R:ntcTsOIpInMulticastAddress,_S:ntcTsOIpInUdpPort,_T:ntcTsOIpInTrafficProfile,_z:ntcTsOIpInMaxTrafficJitter,_U:ntcTsOIpInMaxBufferDelay,_V:ntcTsOIpInInputTsBitRate,'ntcTsOIpInMonitor':ntcTsOIpInMonitor,_W:ntcTsOIpInMonResetCounters,_X:ntcTsOIpInMonInputTsBitRate,_Y:ntcTsOIpInMonBufferDelay,_Z:ntcTsOIpInMonMinBufferFilling,_a:ntcTsOIpInMonMaxBufferFilling,_b:ntcTsOIpInMonSourceInfo,_c:ntcTsOIpInMonRtpFecScheme,_d:ntcTsOIpInMonTsInCount,_e:ntcTsOIpInMonRtpInCount,_f:ntcTsOIpInMonRtpColumnFecInCount,_g:ntcTsOIpInMonRtpRowFecInCount,_h:ntcTsOIpInMonTsOutCount,_i:ntcTsOIpInMonTsDropCount,_j:ntcTsOIpInMonTsOverflowCount,_k:ntcTsOIpInMonRtpDropCount,_l:ntcTsOIpInMonRtpRepairCount,_m:ntcTsOIpInMonRtpFecDropCount,_n:ntcTsOIpInMonActivePCRPID,'ntcTsOIpInAlarm':ntcTsOIpInAlarm,_o:ntcTsOIpInAlmGeneralTsOverIpIn,_p:ntcTsOIpInAlmNoInputData,_q:ntcTsOIpInAlmBufferOverflow,_r:ntcTsOIpInAlmBufferUnflow,_s:ntcTsOIpInAlmRtpNoSync,_t:ntcTsOIpInAlmInvalidTsBitRate,_u:ntcTsOIpInMulticastSourceA,_v:ntcTsOIpInMulticastSourceB,_w:ntcTsOIpInInputRateType,_x:ntcTsOIpInAutoPcrDetection,_y:ntcTsOIpInPcrPid,'ntcTsOIpInConformance':ntcTsOIpInConformance,'ntcTsOIpInConfCompliance':ntcTsOIpInConfCompliance,'ntcTsOIpInConfCompV1Standard':ntcTsOIpInConfCompV1Standard,'ntcTsOIpInConfGroup':ntcTsOIpInConfGroup,_A0:ntcTsOIpInConfGrpV1Standard,'ntcTsOIpInConfGrpObsolete':ntcTsOIpInConfGrpObsolete})