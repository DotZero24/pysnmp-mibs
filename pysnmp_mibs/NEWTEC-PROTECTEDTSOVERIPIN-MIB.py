_AH='ntcProtTsOIpInConfGrpV1Standard'
_AG='ntcProtTsOIpInNpRangeTimeWindow'
_AF='ntcProtTsOIpInNpRangeThrMaxRate'
_AE='ntcProtTsOIpInNpRangeThrEnable'
_AD='ntcProtTsOIpInAlRtpNoSync'
_AC='ntcProtTsOIpInAlBufferOverflow'
_AB='ntcProtTsOIpInAlBufferUnderflow'
_AA='ntcProtTsOIpInAlNoInputData'
_A9='ntcProtTsOIpInAlRedDegraded'
_A8='ntcProtTsOIpInAlRedFailure'
_A7='ntcProtTsOIpInRtpNoSync'
_A6='ntcProtTsOIpInBufferOverflow'
_A5='ntcProtTsOIpInBufferUnderflow'
_A4='ntcProtTsOIpInNoInputData'
_A3='ntcProtTsOIpInActivePcrPid'
_A2='ntcProtTsOIpInMonRtpRepairCount'
_A1='ntcProtTsOIpInMonRtpFecDropCount'
_A0='ntcProtTsOIpInMonRtpDropCount'
_z='ntcProtTsOIpInMonTsOverflowCount'
_y='ntcProtTsOIpInMonTsDropCount'
_x='ntcProtTsOIpInMonTsOutCount'
_w='ntcProtTsOIpInMonRtpRowFecInCnt'
_v='ntcProtTsOIpInMonRtpColFecInCnt'
_u='ntcProtTsOIpInMonRtpInCount'
_t='ntcProtTsOIpInMonTsInCount'
_s='ntcProtTsOIpInMonRtpFecScheme'
_r='ntcProtTsOIpInMonSourceInfo'
_q='ntcProtTsOIpInMonMaxBufferFill'
_p='ntcProtTsOIpInMonMinBufferFill'
_o='ntcProtTsOIpInMonBufferDelay'
_n='ntcProtTsOIpInMonMeasInTsBitRate'
_m='ntcProtTsOIpInActiveInput'
_l='ntcProtTsOIpInSwitchCount'
_k='ntcProtTsOIpInMInpSelTsBRate'
_j='ntcProtTsOIpInCounterReset'
_i='ntcProtTsOIpInInputTsBitRate'
_h='ntcProtTsOIpInMaxBufferDelay'
_g='ntcProtTsOIpInPcrPid'
_f='ntcProtTsOIpInAutoPcrDetection'
_e='ntcProtTsOIpInInputRateType'
_d='ntcProtTsOIpInTrafficProfile'
_c='ntcProtTsOIpInUdpPort'
_b='ntcProtTsOIpInMulticastSourceB'
_a='ntcProtTsOIpInMulticastSourceA'
_Z='ntcProtTsOIpInMulticastAddress'
_Y='ntcProtTsOIpInIpAddressType'
_X='ntcProtTsOIpInTsEncapProtocol'
_W='ntcProtTsOIpInInpSelection'
_V='ntcProtTsOIpInProtInpSelection'
_U='ntcProtTsOIpInEnable'
_T='ntcProtTsOIpInAlarmStatusName'
_S='ntcProtTsOIpInMonName'
_R='0.0.0.0'
_Q='ntcProtTsOIpInConfName'
_P='tsoip2'
_O='tsoip1'
_N='IpAddress'
_M='not-accessible'
_L='NtcNetworkAddress'
_K='bps'
_J='ms'
_I='NtcEnable'
_H='DisplayString'
_G='Unsigned32'
_F='packets'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='NEWTEC-PROTECTEDTSOVERIPIN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable,NtcNetworkAddress=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_I,_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,_N,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
ntcProtectedTsOverIpIn=ModuleIdentity((1,3,6,1,4,1,5835,5,2,9400))
if mibBuilder.loadTexts:ntcProtectedTsOverIpIn.setRevisions(('2018-04-04 10:00','2017-07-10 12:00','2016-02-02 07:00'))
_NtcProtTsOIpInObjects_ObjectIdentity=ObjectIdentity
ntcProtTsOIpInObjects=_NtcProtTsOIpInObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9400,1))
if mibBuilder.loadTexts:ntcProtTsOIpInObjects.setStatus(_A)
class _NtcProtTsOIpInEnable_Type(NtcEnable):defaultValue=0
_NtcProtTsOIpInEnable_Type.__name__=_I
_NtcProtTsOIpInEnable_Object=MibScalar
ntcProtTsOIpInEnable=_NtcProtTsOIpInEnable_Object((1,3,6,1,4,1,5835,5,2,9400,1,1),_NtcProtTsOIpInEnable_Type())
ntcProtTsOIpInEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInEnable.setStatus(_A)
class _NtcProtTsOIpInProtInpSelection_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),(_P,2),('tsoip1or2',3),('tsoip1before2',4),('tsoip2before1',5)))
_NtcProtTsOIpInProtInpSelection_Type.__name__=_E
_NtcProtTsOIpInProtInpSelection_Object=MibScalar
ntcProtTsOIpInProtInpSelection=_NtcProtTsOIpInProtInpSelection_Object((1,3,6,1,4,1,5835,5,2,9400,1,2),_NtcProtTsOIpInProtInpSelection_Type())
ntcProtTsOIpInProtInpSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInProtInpSelection.setStatus(_A)
_NtcProtTsOIpInConfTable_Object=MibTable
ntcProtTsOIpInConfTable=_NtcProtTsOIpInConfTable_Object((1,3,6,1,4,1,5835,5,2,9400,1,3))
if mibBuilder.loadTexts:ntcProtTsOIpInConfTable.setStatus(_A)
_NtcProtTsOIpInConfEntry_Object=MibTableRow
ntcProtTsOIpInConfEntry=_NtcProtTsOIpInConfEntry_Object((1,3,6,1,4,1,5835,5,2,9400,1,3,1))
ntcProtTsOIpInConfEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:ntcProtTsOIpInConfEntry.setStatus(_A)
class _NtcProtTsOIpInConfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NtcProtTsOIpInConfName_Type.__name__=_H
_NtcProtTsOIpInConfName_Object=MibTableColumn
ntcProtTsOIpInConfName=_NtcProtTsOIpInConfName_Object((1,3,6,1,4,1,5835,5,2,9400,1,3,1,1),_NtcProtTsOIpInConfName_Type())
ntcProtTsOIpInConfName.setMaxAccess(_M)
if mibBuilder.loadTexts:ntcProtTsOIpInConfName.setStatus(_A)
class _NtcProtTsOIpInInpSelection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('data1',2),('data2',3),('data',4),('any',5)))
_NtcProtTsOIpInInpSelection_Type.__name__=_E
_NtcProtTsOIpInInpSelection_Object=MibTableColumn
ntcProtTsOIpInInpSelection=_NtcProtTsOIpInInpSelection_Object((1,3,6,1,4,1,5835,5,2,9400,1,3,1,2),_NtcProtTsOIpInInpSelection_Type())
ntcProtTsOIpInInpSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInInpSelection.setStatus(_A)
class _NtcProtTsOIpInTsEncapProtocol_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('udp',0),('rtp',1),('rtpfec',2)))
_NtcProtTsOIpInTsEncapProtocol_Type.__name__=_E
_NtcProtTsOIpInTsEncapProtocol_Object=MibTableColumn
ntcProtTsOIpInTsEncapProtocol=_NtcProtTsOIpInTsEncapProtocol_Object((1,3,6,1,4,1,5835,5,2,9400,1,3,1,3),_NtcProtTsOIpInTsEncapProtocol_Type())
ntcProtTsOIpInTsEncapProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInTsEncapProtocol.setStatus(_A)
class _NtcProtTsOIpInIpAddressType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unicast',0),('multicast',1)))
_NtcProtTsOIpInIpAddressType_Type.__name__=_E
_NtcProtTsOIpInIpAddressType_Object=MibTableColumn
ntcProtTsOIpInIpAddressType=_NtcProtTsOIpInIpAddressType_Object((1,3,6,1,4,1,5835,5,2,9400,1,3,1,4),_NtcProtTsOIpInIpAddressType_Type())
ntcProtTsOIpInIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInIpAddressType.setStatus(_A)
class _NtcProtTsOIpInMulticastAddress_Type(IpAddress):defaultHexValue='e0010001'
_NtcProtTsOIpInMulticastAddress_Type.__name__=_N
_NtcProtTsOIpInMulticastAddress_Object=MibTableColumn
ntcProtTsOIpInMulticastAddress=_NtcProtTsOIpInMulticastAddress_Object((1,3,6,1,4,1,5835,5,2,9400,1,3,1,5),_NtcProtTsOIpInMulticastAddress_Type())
ntcProtTsOIpInMulticastAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInMulticastAddress.setStatus(_A)
class _NtcProtTsOIpInMulticastSourceA_Type(NtcNetworkAddress):defaultValue=OctetString(_R)
_NtcProtTsOIpInMulticastSourceA_Type.__name__=_L
_NtcProtTsOIpInMulticastSourceA_Object=MibTableColumn
ntcProtTsOIpInMulticastSourceA=_NtcProtTsOIpInMulticastSourceA_Object((1,3,6,1,4,1,5835,5,2,9400,1,3,1,6),_NtcProtTsOIpInMulticastSourceA_Type())
ntcProtTsOIpInMulticastSourceA.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInMulticastSourceA.setStatus(_A)
class _NtcProtTsOIpInMulticastSourceB_Type(NtcNetworkAddress):defaultValue=OctetString(_R)
_NtcProtTsOIpInMulticastSourceB_Type.__name__=_L
_NtcProtTsOIpInMulticastSourceB_Object=MibTableColumn
ntcProtTsOIpInMulticastSourceB=_NtcProtTsOIpInMulticastSourceB_Object((1,3,6,1,4,1,5835,5,2,9400,1,3,1,7),_NtcProtTsOIpInMulticastSourceB_Type())
ntcProtTsOIpInMulticastSourceB.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInMulticastSourceB.setStatus(_A)
class _NtcProtTsOIpInUdpPort_Type(Unsigned32):defaultValue=56789;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NtcProtTsOIpInUdpPort_Type.__name__=_G
_NtcProtTsOIpInUdpPort_Object=MibTableColumn
ntcProtTsOIpInUdpPort=_NtcProtTsOIpInUdpPort_Object((1,3,6,1,4,1,5835,5,2,9400,1,3,1,8),_NtcProtTsOIpInUdpPort_Type())
ntcProtTsOIpInUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInUdpPort.setStatus(_A)
class _NtcProtTsOIpInTrafficProfile_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('vbr',0),('cbr',1)))
_NtcProtTsOIpInTrafficProfile_Type.__name__=_E
_NtcProtTsOIpInTrafficProfile_Object=MibTableColumn
ntcProtTsOIpInTrafficProfile=_NtcProtTsOIpInTrafficProfile_Object((1,3,6,1,4,1,5835,5,2,9400,1,3,1,9),_NtcProtTsOIpInTrafficProfile_Type())
ntcProtTsOIpInTrafficProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInTrafficProfile.setStatus(_A)
class _NtcProtTsOIpInInputRateType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('userdefined',0),('pcr',1)))
_NtcProtTsOIpInInputRateType_Type.__name__=_E
_NtcProtTsOIpInInputRateType_Object=MibTableColumn
ntcProtTsOIpInInputRateType=_NtcProtTsOIpInInputRateType_Object((1,3,6,1,4,1,5835,5,2,9400,1,3,1,10),_NtcProtTsOIpInInputRateType_Type())
ntcProtTsOIpInInputRateType.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInInputRateType.setStatus(_A)
class _NtcProtTsOIpInAutoPcrDetection_Type(NtcEnable):defaultValue=1
_NtcProtTsOIpInAutoPcrDetection_Type.__name__=_I
_NtcProtTsOIpInAutoPcrDetection_Object=MibTableColumn
ntcProtTsOIpInAutoPcrDetection=_NtcProtTsOIpInAutoPcrDetection_Object((1,3,6,1,4,1,5835,5,2,9400,1,3,1,11),_NtcProtTsOIpInAutoPcrDetection_Type())
ntcProtTsOIpInAutoPcrDetection.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInAutoPcrDetection.setStatus(_A)
class _NtcProtTsOIpInPcrPid_Type(Unsigned32):defaultValue=8191;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_NtcProtTsOIpInPcrPid_Type.__name__=_G
_NtcProtTsOIpInPcrPid_Object=MibTableColumn
ntcProtTsOIpInPcrPid=_NtcProtTsOIpInPcrPid_Object((1,3,6,1,4,1,5835,5,2,9400,1,3,1,12),_NtcProtTsOIpInPcrPid_Type())
ntcProtTsOIpInPcrPid.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInPcrPid.setStatus(_A)
class _NtcProtTsOIpInMaxBufferDelay_Type(Unsigned32):defaultValue=250
_NtcProtTsOIpInMaxBufferDelay_Type.__name__=_G
_NtcProtTsOIpInMaxBufferDelay_Object=MibTableColumn
ntcProtTsOIpInMaxBufferDelay=_NtcProtTsOIpInMaxBufferDelay_Object((1,3,6,1,4,1,5835,5,2,9400,1,3,1,13),_NtcProtTsOIpInMaxBufferDelay_Type())
ntcProtTsOIpInMaxBufferDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInMaxBufferDelay.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInMaxBufferDelay.setUnits(_J)
class _NtcProtTsOIpInInputTsBitRate_Type(Unsigned32):defaultValue=1000000
_NtcProtTsOIpInInputTsBitRate_Type.__name__=_G
_NtcProtTsOIpInInputTsBitRate_Object=MibTableColumn
ntcProtTsOIpInInputTsBitRate=_NtcProtTsOIpInInputTsBitRate_Object((1,3,6,1,4,1,5835,5,2,9400,1,3,1,14),_NtcProtTsOIpInInputTsBitRate_Type())
ntcProtTsOIpInInputTsBitRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInInputTsBitRate.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInInputTsBitRate.setUnits(_K)
_NtcProtTsOIpInMon_ObjectIdentity=ObjectIdentity
ntcProtTsOIpInMon=_NtcProtTsOIpInMon_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9400,1,4))
if mibBuilder.loadTexts:ntcProtTsOIpInMon.setStatus(_A)
class _NtcProtTsOIpInCounterReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('counting',0),('reset',1)))
_NtcProtTsOIpInCounterReset_Type.__name__=_E
_NtcProtTsOIpInCounterReset_Object=MibScalar
ntcProtTsOIpInCounterReset=_NtcProtTsOIpInCounterReset_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,1),_NtcProtTsOIpInCounterReset_Type())
ntcProtTsOIpInCounterReset.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInCounterReset.setStatus(_A)
_NtcProtTsOIpInMInpSelTsBRate_Type=Unsigned32
_NtcProtTsOIpInMInpSelTsBRate_Object=MibScalar
ntcProtTsOIpInMInpSelTsBRate=_NtcProtTsOIpInMInpSelTsBRate_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,2),_NtcProtTsOIpInMInpSelTsBRate_Type())
ntcProtTsOIpInMInpSelTsBRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMInpSelTsBRate.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInMInpSelTsBRate.setUnits(_K)
_NtcProtTsOIpInSwitchCount_Type=Counter32
_NtcProtTsOIpInSwitchCount_Object=MibScalar
ntcProtTsOIpInSwitchCount=_NtcProtTsOIpInSwitchCount_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,3),_NtcProtTsOIpInSwitchCount_Type())
ntcProtTsOIpInSwitchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInSwitchCount.setStatus(_A)
class _NtcProtTsOIpInActiveInput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),(_O,1),(_P,2)))
_NtcProtTsOIpInActiveInput_Type.__name__=_E
_NtcProtTsOIpInActiveInput_Object=MibScalar
ntcProtTsOIpInActiveInput=_NtcProtTsOIpInActiveInput_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,4),_NtcProtTsOIpInActiveInput_Type())
ntcProtTsOIpInActiveInput.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInActiveInput.setStatus(_A)
_NtcProtTsOIpInMonTable_Object=MibTable
ntcProtTsOIpInMonTable=_NtcProtTsOIpInMonTable_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5))
if mibBuilder.loadTexts:ntcProtTsOIpInMonTable.setStatus(_A)
_NtcProtTsOIpInMonEntry_Object=MibTableRow
ntcProtTsOIpInMonEntry=_NtcProtTsOIpInMonEntry_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1))
ntcProtTsOIpInMonEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:ntcProtTsOIpInMonEntry.setStatus(_A)
class _NtcProtTsOIpInMonName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcProtTsOIpInMonName_Type.__name__=_H
_NtcProtTsOIpInMonName_Object=MibTableColumn
ntcProtTsOIpInMonName=_NtcProtTsOIpInMonName_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,1),_NtcProtTsOIpInMonName_Type())
ntcProtTsOIpInMonName.setMaxAccess(_M)
if mibBuilder.loadTexts:ntcProtTsOIpInMonName.setStatus(_A)
_NtcProtTsOIpInMonMeasInTsBitRate_Type=Unsigned32
_NtcProtTsOIpInMonMeasInTsBitRate_Object=MibTableColumn
ntcProtTsOIpInMonMeasInTsBitRate=_NtcProtTsOIpInMonMeasInTsBitRate_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,2),_NtcProtTsOIpInMonMeasInTsBitRate_Type())
ntcProtTsOIpInMonMeasInTsBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMonMeasInTsBitRate.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInMonMeasInTsBitRate.setUnits(_K)
_NtcProtTsOIpInMonBufferDelay_Type=Unsigned32
_NtcProtTsOIpInMonBufferDelay_Object=MibTableColumn
ntcProtTsOIpInMonBufferDelay=_NtcProtTsOIpInMonBufferDelay_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,3),_NtcProtTsOIpInMonBufferDelay_Type())
ntcProtTsOIpInMonBufferDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMonBufferDelay.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInMonBufferDelay.setUnits(_J)
_NtcProtTsOIpInMonMinBufferFill_Type=Unsigned32
_NtcProtTsOIpInMonMinBufferFill_Object=MibTableColumn
ntcProtTsOIpInMonMinBufferFill=_NtcProtTsOIpInMonMinBufferFill_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,4),_NtcProtTsOIpInMonMinBufferFill_Type())
ntcProtTsOIpInMonMinBufferFill.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMonMinBufferFill.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInMonMinBufferFill.setUnits(_J)
_NtcProtTsOIpInMonMaxBufferFill_Type=Unsigned32
_NtcProtTsOIpInMonMaxBufferFill_Object=MibTableColumn
ntcProtTsOIpInMonMaxBufferFill=_NtcProtTsOIpInMonMaxBufferFill_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,5),_NtcProtTsOIpInMonMaxBufferFill_Type())
ntcProtTsOIpInMonMaxBufferFill.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMonMaxBufferFill.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInMonMaxBufferFill.setUnits(_J)
class _NtcProtTsOIpInMonSourceInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcProtTsOIpInMonSourceInfo_Type.__name__=_H
_NtcProtTsOIpInMonSourceInfo_Object=MibTableColumn
ntcProtTsOIpInMonSourceInfo=_NtcProtTsOIpInMonSourceInfo_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,6),_NtcProtTsOIpInMonSourceInfo_Type())
ntcProtTsOIpInMonSourceInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMonSourceInfo.setStatus(_A)
class _NtcProtTsOIpInMonRtpFecScheme_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcProtTsOIpInMonRtpFecScheme_Type.__name__=_H
_NtcProtTsOIpInMonRtpFecScheme_Object=MibTableColumn
ntcProtTsOIpInMonRtpFecScheme=_NtcProtTsOIpInMonRtpFecScheme_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,7),_NtcProtTsOIpInMonRtpFecScheme_Type())
ntcProtTsOIpInMonRtpFecScheme.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMonRtpFecScheme.setStatus(_A)
_NtcProtTsOIpInMonTsInCount_Type=Counter32
_NtcProtTsOIpInMonTsInCount_Object=MibTableColumn
ntcProtTsOIpInMonTsInCount=_NtcProtTsOIpInMonTsInCount_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,8),_NtcProtTsOIpInMonTsInCount_Type())
ntcProtTsOIpInMonTsInCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMonTsInCount.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInMonTsInCount.setUnits(_F)
_NtcProtTsOIpInMonRtpInCount_Type=Counter32
_NtcProtTsOIpInMonRtpInCount_Object=MibTableColumn
ntcProtTsOIpInMonRtpInCount=_NtcProtTsOIpInMonRtpInCount_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,9),_NtcProtTsOIpInMonRtpInCount_Type())
ntcProtTsOIpInMonRtpInCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMonRtpInCount.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInMonRtpInCount.setUnits(_F)
_NtcProtTsOIpInMonRtpColFecInCnt_Type=Counter32
_NtcProtTsOIpInMonRtpColFecInCnt_Object=MibTableColumn
ntcProtTsOIpInMonRtpColFecInCnt=_NtcProtTsOIpInMonRtpColFecInCnt_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,10),_NtcProtTsOIpInMonRtpColFecInCnt_Type())
ntcProtTsOIpInMonRtpColFecInCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMonRtpColFecInCnt.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInMonRtpColFecInCnt.setUnits(_F)
_NtcProtTsOIpInMonRtpRowFecInCnt_Type=Counter32
_NtcProtTsOIpInMonRtpRowFecInCnt_Object=MibTableColumn
ntcProtTsOIpInMonRtpRowFecInCnt=_NtcProtTsOIpInMonRtpRowFecInCnt_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,11),_NtcProtTsOIpInMonRtpRowFecInCnt_Type())
ntcProtTsOIpInMonRtpRowFecInCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMonRtpRowFecInCnt.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInMonRtpRowFecInCnt.setUnits(_F)
_NtcProtTsOIpInMonTsOutCount_Type=Counter32
_NtcProtTsOIpInMonTsOutCount_Object=MibTableColumn
ntcProtTsOIpInMonTsOutCount=_NtcProtTsOIpInMonTsOutCount_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,12),_NtcProtTsOIpInMonTsOutCount_Type())
ntcProtTsOIpInMonTsOutCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMonTsOutCount.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInMonTsOutCount.setUnits(_F)
_NtcProtTsOIpInMonTsDropCount_Type=Counter32
_NtcProtTsOIpInMonTsDropCount_Object=MibTableColumn
ntcProtTsOIpInMonTsDropCount=_NtcProtTsOIpInMonTsDropCount_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,13),_NtcProtTsOIpInMonTsDropCount_Type())
ntcProtTsOIpInMonTsDropCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMonTsDropCount.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInMonTsDropCount.setUnits(_F)
_NtcProtTsOIpInMonTsOverflowCount_Type=Counter32
_NtcProtTsOIpInMonTsOverflowCount_Object=MibTableColumn
ntcProtTsOIpInMonTsOverflowCount=_NtcProtTsOIpInMonTsOverflowCount_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,14),_NtcProtTsOIpInMonTsOverflowCount_Type())
ntcProtTsOIpInMonTsOverflowCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMonTsOverflowCount.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInMonTsOverflowCount.setUnits(_F)
_NtcProtTsOIpInMonRtpDropCount_Type=Counter32
_NtcProtTsOIpInMonRtpDropCount_Object=MibTableColumn
ntcProtTsOIpInMonRtpDropCount=_NtcProtTsOIpInMonRtpDropCount_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,15),_NtcProtTsOIpInMonRtpDropCount_Type())
ntcProtTsOIpInMonRtpDropCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMonRtpDropCount.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInMonRtpDropCount.setUnits(_F)
_NtcProtTsOIpInMonRtpFecDropCount_Type=Counter32
_NtcProtTsOIpInMonRtpFecDropCount_Object=MibTableColumn
ntcProtTsOIpInMonRtpFecDropCount=_NtcProtTsOIpInMonRtpFecDropCount_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,16),_NtcProtTsOIpInMonRtpFecDropCount_Type())
ntcProtTsOIpInMonRtpFecDropCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMonRtpFecDropCount.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInMonRtpFecDropCount.setUnits(_F)
_NtcProtTsOIpInMonRtpRepairCount_Type=Counter32
_NtcProtTsOIpInMonRtpRepairCount_Object=MibTableColumn
ntcProtTsOIpInMonRtpRepairCount=_NtcProtTsOIpInMonRtpRepairCount_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,17),_NtcProtTsOIpInMonRtpRepairCount_Type())
ntcProtTsOIpInMonRtpRepairCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInMonRtpRepairCount.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInMonRtpRepairCount.setUnits(_F)
class _NtcProtTsOIpInActivePcrPid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8190))
_NtcProtTsOIpInActivePcrPid_Type.__name__=_G
_NtcProtTsOIpInActivePcrPid_Object=MibTableColumn
ntcProtTsOIpInActivePcrPid=_NtcProtTsOIpInActivePcrPid_Object((1,3,6,1,4,1,5835,5,2,9400,1,4,5,1,18),_NtcProtTsOIpInActivePcrPid_Type())
ntcProtTsOIpInActivePcrPid.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInActivePcrPid.setStatus(_A)
_NtcProtTsOIpInAlarms_ObjectIdentity=ObjectIdentity
ntcProtTsOIpInAlarms=_NtcProtTsOIpInAlarms_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9400,1,5))
if mibBuilder.loadTexts:ntcProtTsOIpInAlarms.setStatus(_A)
_NtcProtTsOIpInAlarmStatusTable_Object=MibTable
ntcProtTsOIpInAlarmStatusTable=_NtcProtTsOIpInAlarmStatusTable_Object((1,3,6,1,4,1,5835,5,2,9400,1,5,1))
if mibBuilder.loadTexts:ntcProtTsOIpInAlarmStatusTable.setStatus(_A)
_NtcProtTsOIpInAlarmStatusEntry_Object=MibTableRow
ntcProtTsOIpInAlarmStatusEntry=_NtcProtTsOIpInAlarmStatusEntry_Object((1,3,6,1,4,1,5835,5,2,9400,1,5,1,1))
ntcProtTsOIpInAlarmStatusEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:ntcProtTsOIpInAlarmStatusEntry.setStatus(_A)
class _NtcProtTsOIpInAlarmStatusName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcProtTsOIpInAlarmStatusName_Type.__name__=_H
_NtcProtTsOIpInAlarmStatusName_Object=MibTableColumn
ntcProtTsOIpInAlarmStatusName=_NtcProtTsOIpInAlarmStatusName_Object((1,3,6,1,4,1,5835,5,2,9400,1,5,1,1,1),_NtcProtTsOIpInAlarmStatusName_Type())
ntcProtTsOIpInAlarmStatusName.setMaxAccess(_M)
if mibBuilder.loadTexts:ntcProtTsOIpInAlarmStatusName.setStatus(_A)
_NtcProtTsOIpInNoInputData_Type=NtcAlarmState
_NtcProtTsOIpInNoInputData_Object=MibTableColumn
ntcProtTsOIpInNoInputData=_NtcProtTsOIpInNoInputData_Object((1,3,6,1,4,1,5835,5,2,9400,1,5,1,1,2),_NtcProtTsOIpInNoInputData_Type())
ntcProtTsOIpInNoInputData.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInNoInputData.setStatus(_A)
_NtcProtTsOIpInBufferUnderflow_Type=NtcAlarmState
_NtcProtTsOIpInBufferUnderflow_Object=MibTableColumn
ntcProtTsOIpInBufferUnderflow=_NtcProtTsOIpInBufferUnderflow_Object((1,3,6,1,4,1,5835,5,2,9400,1,5,1,1,3),_NtcProtTsOIpInBufferUnderflow_Type())
ntcProtTsOIpInBufferUnderflow.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInBufferUnderflow.setStatus(_A)
_NtcProtTsOIpInBufferOverflow_Type=NtcAlarmState
_NtcProtTsOIpInBufferOverflow_Object=MibTableColumn
ntcProtTsOIpInBufferOverflow=_NtcProtTsOIpInBufferOverflow_Object((1,3,6,1,4,1,5835,5,2,9400,1,5,1,1,4),_NtcProtTsOIpInBufferOverflow_Type())
ntcProtTsOIpInBufferOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInBufferOverflow.setStatus(_A)
_NtcProtTsOIpInRtpNoSync_Type=NtcAlarmState
_NtcProtTsOIpInRtpNoSync_Object=MibTableColumn
ntcProtTsOIpInRtpNoSync=_NtcProtTsOIpInRtpNoSync_Object((1,3,6,1,4,1,5835,5,2,9400,1,5,1,1,5),_NtcProtTsOIpInRtpNoSync_Type())
ntcProtTsOIpInRtpNoSync.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInRtpNoSync.setStatus(_A)
_NtcProtTsOIpInAlarm_ObjectIdentity=ObjectIdentity
ntcProtTsOIpInAlarm=_NtcProtTsOIpInAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9400,1,6))
if mibBuilder.loadTexts:ntcProtTsOIpInAlarm.setStatus(_A)
_NtcProtTsOIpInAlRedFailure_Type=NtcAlarmState
_NtcProtTsOIpInAlRedFailure_Object=MibScalar
ntcProtTsOIpInAlRedFailure=_NtcProtTsOIpInAlRedFailure_Object((1,3,6,1,4,1,5835,5,2,9400,1,6,1),_NtcProtTsOIpInAlRedFailure_Type())
ntcProtTsOIpInAlRedFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInAlRedFailure.setStatus(_A)
_NtcProtTsOIpInAlRedDegraded_Type=NtcAlarmState
_NtcProtTsOIpInAlRedDegraded_Object=MibScalar
ntcProtTsOIpInAlRedDegraded=_NtcProtTsOIpInAlRedDegraded_Object((1,3,6,1,4,1,5835,5,2,9400,1,6,2),_NtcProtTsOIpInAlRedDegraded_Type())
ntcProtTsOIpInAlRedDegraded.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInAlRedDegraded.setStatus(_A)
_NtcProtTsOIpInAlNoInputData_Type=NtcAlarmState
_NtcProtTsOIpInAlNoInputData_Object=MibScalar
ntcProtTsOIpInAlNoInputData=_NtcProtTsOIpInAlNoInputData_Object((1,3,6,1,4,1,5835,5,2,9400,1,6,3),_NtcProtTsOIpInAlNoInputData_Type())
ntcProtTsOIpInAlNoInputData.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInAlNoInputData.setStatus(_A)
_NtcProtTsOIpInAlBufferUnderflow_Type=NtcAlarmState
_NtcProtTsOIpInAlBufferUnderflow_Object=MibScalar
ntcProtTsOIpInAlBufferUnderflow=_NtcProtTsOIpInAlBufferUnderflow_Object((1,3,6,1,4,1,5835,5,2,9400,1,6,4),_NtcProtTsOIpInAlBufferUnderflow_Type())
ntcProtTsOIpInAlBufferUnderflow.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInAlBufferUnderflow.setStatus(_A)
_NtcProtTsOIpInAlBufferOverflow_Type=NtcAlarmState
_NtcProtTsOIpInAlBufferOverflow_Object=MibScalar
ntcProtTsOIpInAlBufferOverflow=_NtcProtTsOIpInAlBufferOverflow_Object((1,3,6,1,4,1,5835,5,2,9400,1,6,5),_NtcProtTsOIpInAlBufferOverflow_Type())
ntcProtTsOIpInAlBufferOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInAlBufferOverflow.setStatus(_A)
_NtcProtTsOIpInAlRtpNoSync_Type=NtcAlarmState
_NtcProtTsOIpInAlRtpNoSync_Object=MibScalar
ntcProtTsOIpInAlRtpNoSync=_NtcProtTsOIpInAlRtpNoSync_Object((1,3,6,1,4,1,5835,5,2,9400,1,6,6),_NtcProtTsOIpInAlRtpNoSync_Type())
ntcProtTsOIpInAlRtpNoSync.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcProtTsOIpInAlRtpNoSync.setStatus(_A)
_NtcProtTsOIpInNpRangeThr_ObjectIdentity=ObjectIdentity
ntcProtTsOIpInNpRangeThr=_NtcProtTsOIpInNpRangeThr_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9400,1,7))
if mibBuilder.loadTexts:ntcProtTsOIpInNpRangeThr.setStatus(_A)
class _NtcProtTsOIpInNpRangeThrEnable_Type(NtcEnable):defaultValue=0
_NtcProtTsOIpInNpRangeThrEnable_Type.__name__=_I
_NtcProtTsOIpInNpRangeThrEnable_Object=MibScalar
ntcProtTsOIpInNpRangeThrEnable=_NtcProtTsOIpInNpRangeThrEnable_Object((1,3,6,1,4,1,5835,5,2,9400,1,7,1),_NtcProtTsOIpInNpRangeThrEnable_Type())
ntcProtTsOIpInNpRangeThrEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInNpRangeThrEnable.setStatus(_A)
class _NtcProtTsOIpInNpRangeThrMaxRate_Type(Unsigned32):defaultValue=0
_NtcProtTsOIpInNpRangeThrMaxRate_Type.__name__=_G
_NtcProtTsOIpInNpRangeThrMaxRate_Object=MibScalar
ntcProtTsOIpInNpRangeThrMaxRate=_NtcProtTsOIpInNpRangeThrMaxRate_Object((1,3,6,1,4,1,5835,5,2,9400,1,7,2),_NtcProtTsOIpInNpRangeThrMaxRate_Type())
ntcProtTsOIpInNpRangeThrMaxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInNpRangeThrMaxRate.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInNpRangeThrMaxRate.setUnits(_K)
class _NtcProtTsOIpInNpRangeTimeWindow_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_NtcProtTsOIpInNpRangeTimeWindow_Type.__name__=_E
_NtcProtTsOIpInNpRangeTimeWindow_Object=MibScalar
ntcProtTsOIpInNpRangeTimeWindow=_NtcProtTsOIpInNpRangeTimeWindow_Object((1,3,6,1,4,1,5835,5,2,9400,1,7,3),_NtcProtTsOIpInNpRangeTimeWindow_Type())
ntcProtTsOIpInNpRangeTimeWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcProtTsOIpInNpRangeTimeWindow.setStatus(_A)
if mibBuilder.loadTexts:ntcProtTsOIpInNpRangeTimeWindow.setUnits('s')
_NtcProtTsOIpInConformance_ObjectIdentity=ObjectIdentity
ntcProtTsOIpInConformance=_NtcProtTsOIpInConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9400,2))
if mibBuilder.loadTexts:ntcProtTsOIpInConformance.setStatus(_A)
_NtcProtTsOIpInConfCompliance_ObjectIdentity=ObjectIdentity
ntcProtTsOIpInConfCompliance=_NtcProtTsOIpInConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9400,2,1))
if mibBuilder.loadTexts:ntcProtTsOIpInConfCompliance.setStatus(_A)
_NtcProtTsOIpInConfGroup_ObjectIdentity=ObjectIdentity
ntcProtTsOIpInConfGroup=_NtcProtTsOIpInConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9400,2,2))
if mibBuilder.loadTexts:ntcProtTsOIpInConfGroup.setStatus(_A)
ntcProtTsOIpInConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,9400,2,2,1))
ntcProtTsOIpInConfGrpV1Standard.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:ntcProtTsOIpInConfGrpV1Standard.setStatus(_A)
ntcProtTsOIpInConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,9400,2,1,1))
ntcProtTsOIpInConfCompV1Standard.setObjects((_B,_AH))
if mibBuilder.loadTexts:ntcProtTsOIpInConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcProtectedTsOverIpIn':ntcProtectedTsOverIpIn,'ntcProtTsOIpInObjects':ntcProtTsOIpInObjects,_U:ntcProtTsOIpInEnable,_V:ntcProtTsOIpInProtInpSelection,'ntcProtTsOIpInConfTable':ntcProtTsOIpInConfTable,'ntcProtTsOIpInConfEntry':ntcProtTsOIpInConfEntry,_Q:ntcProtTsOIpInConfName,_W:ntcProtTsOIpInInpSelection,_X:ntcProtTsOIpInTsEncapProtocol,_Y:ntcProtTsOIpInIpAddressType,_Z:ntcProtTsOIpInMulticastAddress,_a:ntcProtTsOIpInMulticastSourceA,_b:ntcProtTsOIpInMulticastSourceB,_c:ntcProtTsOIpInUdpPort,_d:ntcProtTsOIpInTrafficProfile,_e:ntcProtTsOIpInInputRateType,_f:ntcProtTsOIpInAutoPcrDetection,_g:ntcProtTsOIpInPcrPid,_h:ntcProtTsOIpInMaxBufferDelay,_i:ntcProtTsOIpInInputTsBitRate,'ntcProtTsOIpInMon':ntcProtTsOIpInMon,_j:ntcProtTsOIpInCounterReset,_k:ntcProtTsOIpInMInpSelTsBRate,_l:ntcProtTsOIpInSwitchCount,_m:ntcProtTsOIpInActiveInput,'ntcProtTsOIpInMonTable':ntcProtTsOIpInMonTable,'ntcProtTsOIpInMonEntry':ntcProtTsOIpInMonEntry,_S:ntcProtTsOIpInMonName,_n:ntcProtTsOIpInMonMeasInTsBitRate,_o:ntcProtTsOIpInMonBufferDelay,_p:ntcProtTsOIpInMonMinBufferFill,_q:ntcProtTsOIpInMonMaxBufferFill,_r:ntcProtTsOIpInMonSourceInfo,_s:ntcProtTsOIpInMonRtpFecScheme,_t:ntcProtTsOIpInMonTsInCount,_u:ntcProtTsOIpInMonRtpInCount,_v:ntcProtTsOIpInMonRtpColFecInCnt,_w:ntcProtTsOIpInMonRtpRowFecInCnt,_x:ntcProtTsOIpInMonTsOutCount,_y:ntcProtTsOIpInMonTsDropCount,_z:ntcProtTsOIpInMonTsOverflowCount,_A0:ntcProtTsOIpInMonRtpDropCount,_A1:ntcProtTsOIpInMonRtpFecDropCount,_A2:ntcProtTsOIpInMonRtpRepairCount,_A3:ntcProtTsOIpInActivePcrPid,'ntcProtTsOIpInAlarms':ntcProtTsOIpInAlarms,'ntcProtTsOIpInAlarmStatusTable':ntcProtTsOIpInAlarmStatusTable,'ntcProtTsOIpInAlarmStatusEntry':ntcProtTsOIpInAlarmStatusEntry,_T:ntcProtTsOIpInAlarmStatusName,_A4:ntcProtTsOIpInNoInputData,_A5:ntcProtTsOIpInBufferUnderflow,_A6:ntcProtTsOIpInBufferOverflow,_A7:ntcProtTsOIpInRtpNoSync,'ntcProtTsOIpInAlarm':ntcProtTsOIpInAlarm,_A8:ntcProtTsOIpInAlRedFailure,_A9:ntcProtTsOIpInAlRedDegraded,_AA:ntcProtTsOIpInAlNoInputData,_AB:ntcProtTsOIpInAlBufferUnderflow,_AC:ntcProtTsOIpInAlBufferOverflow,_AD:ntcProtTsOIpInAlRtpNoSync,'ntcProtTsOIpInNpRangeThr':ntcProtTsOIpInNpRangeThr,_AE:ntcProtTsOIpInNpRangeThrEnable,_AF:ntcProtTsOIpInNpRangeThrMaxRate,_AG:ntcProtTsOIpInNpRangeTimeWindow,'ntcProtTsOIpInConformance':ntcProtTsOIpInConformance,'ntcProtTsOIpInConfCompliance':ntcProtTsOIpInConfCompliance,'ntcProtTsOIpInConfCompV1Standard':ntcProtTsOIpInConfCompV1Standard,'ntcProtTsOIpInConfGroup':ntcProtTsOIpInConfGroup,_AH:ntcProtTsOIpInConfGrpV1Standard})