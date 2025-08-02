_k='ntcDssOIpInConfGrpV1Standard'
_j='ntcDssOIpInAlmRtpNoSync'
_i='ntcDssOIpInAlmBufferUnflow'
_h='ntcDssOIpInAlmBufferOverflow'
_g='ntcDssOIpInAlmNoInputData'
_f='ntcDssOIpInMonRtpFecDropCount'
_e='ntcDssOIpInMonRtpRepairCount'
_d='ntcDssOIpInMonRtpDropCount'
_c='ntcDssOIpInMonRtpFecScheme'
_b='ntcDssOIpInMonSourceInfo'
_a='ntcDssOIpInMonMaxBufferFilling'
_Z='ntcDssOIpInMonMinBufferFilling'
_Y='ntcDssOIpInMonBufferDelay'
_X='ntcDssOIpInMonInputDssBitRate'
_W='ntcDssOIpInMonResetCounters'
_V='ntcDssOIpInMulticastSourceB'
_U='ntcDssOIpInMulticastSourceA'
_T='ntcDssOIpInMaxBufferDelay'
_S='ntcDssOIpInUdpPort'
_R='ntcDssOIpInMulticastAddress'
_Q='ntcDssOIpInIpAddressType'
_P='ntcDssOIpInDssEncapProtocol'
_O='ntcDssOIpInInputSelection'
_N='ntcDssOIpInEnable'
_M='0.0.0.0'
_L='IpAddress'
_K='NtcEnable'
_J='packets'
_I='DisplayString'
_H='Unsigned32'
_G='NtcNetworkAddress'
_F='ms'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='NEWTEC-DSSOVERIPIN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable,NtcNetworkAddress=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_K,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,_L,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
ntcDssOverIpIn=ModuleIdentity((1,3,6,1,4,1,5835,5,2,8700))
if mibBuilder.loadTexts:ntcDssOverIpIn.setRevisions(('2017-07-10 12:00','2015-02-19 09:00'))
_NtcDssOIpInObjects_ObjectIdentity=ObjectIdentity
ntcDssOIpInObjects=_NtcDssOIpInObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8700,1))
if mibBuilder.loadTexts:ntcDssOIpInObjects.setStatus(_A)
class _NtcDssOIpInEnable_Type(NtcEnable):defaultValue=0
_NtcDssOIpInEnable_Type.__name__=_K
_NtcDssOIpInEnable_Object=MibScalar
ntcDssOIpInEnable=_NtcDssOIpInEnable_Object((1,3,6,1,4,1,5835,5,2,8700,1,1),_NtcDssOIpInEnable_Type())
ntcDssOIpInEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDssOIpInEnable.setStatus(_A)
class _NtcDssOIpInInputSelection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('data1',2),('data2',3),('data',4),('any',5)))
_NtcDssOIpInInputSelection_Type.__name__=_E
_NtcDssOIpInInputSelection_Object=MibScalar
ntcDssOIpInInputSelection=_NtcDssOIpInInputSelection_Object((1,3,6,1,4,1,5835,5,2,8700,1,2),_NtcDssOIpInInputSelection_Type())
ntcDssOIpInInputSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDssOIpInInputSelection.setStatus(_A)
class _NtcDssOIpInDssEncapProtocol_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('udp',0),('rtp',1),('rtpfec',2)))
_NtcDssOIpInDssEncapProtocol_Type.__name__=_E
_NtcDssOIpInDssEncapProtocol_Object=MibScalar
ntcDssOIpInDssEncapProtocol=_NtcDssOIpInDssEncapProtocol_Object((1,3,6,1,4,1,5835,5,2,8700,1,3),_NtcDssOIpInDssEncapProtocol_Type())
ntcDssOIpInDssEncapProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDssOIpInDssEncapProtocol.setStatus(_A)
class _NtcDssOIpInIpAddressType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unicast',0),('multicast',1)))
_NtcDssOIpInIpAddressType_Type.__name__=_E
_NtcDssOIpInIpAddressType_Object=MibScalar
ntcDssOIpInIpAddressType=_NtcDssOIpInIpAddressType_Object((1,3,6,1,4,1,5835,5,2,8700,1,4),_NtcDssOIpInIpAddressType_Type())
ntcDssOIpInIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDssOIpInIpAddressType.setStatus(_A)
class _NtcDssOIpInMulticastAddress_Type(IpAddress):defaultHexValue='e0010001'
_NtcDssOIpInMulticastAddress_Type.__name__=_L
_NtcDssOIpInMulticastAddress_Object=MibScalar
ntcDssOIpInMulticastAddress=_NtcDssOIpInMulticastAddress_Object((1,3,6,1,4,1,5835,5,2,8700,1,5),_NtcDssOIpInMulticastAddress_Type())
ntcDssOIpInMulticastAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDssOIpInMulticastAddress.setStatus(_A)
class _NtcDssOIpInUdpPort_Type(Unsigned32):defaultValue=56789;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NtcDssOIpInUdpPort_Type.__name__=_H
_NtcDssOIpInUdpPort_Object=MibScalar
ntcDssOIpInUdpPort=_NtcDssOIpInUdpPort_Object((1,3,6,1,4,1,5835,5,2,8700,1,6),_NtcDssOIpInUdpPort_Type())
ntcDssOIpInUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDssOIpInUdpPort.setStatus(_A)
class _NtcDssOIpInMaxBufferDelay_Type(Unsigned32):defaultValue=250
_NtcDssOIpInMaxBufferDelay_Type.__name__=_H
_NtcDssOIpInMaxBufferDelay_Object=MibScalar
ntcDssOIpInMaxBufferDelay=_NtcDssOIpInMaxBufferDelay_Object((1,3,6,1,4,1,5835,5,2,8700,1,7),_NtcDssOIpInMaxBufferDelay_Type())
ntcDssOIpInMaxBufferDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDssOIpInMaxBufferDelay.setStatus(_A)
if mibBuilder.loadTexts:ntcDssOIpInMaxBufferDelay.setUnits(_F)
class _NtcDssOIpInMulticastSourceA_Type(NtcNetworkAddress):defaultValue=OctetString(_M)
_NtcDssOIpInMulticastSourceA_Type.__name__=_G
_NtcDssOIpInMulticastSourceA_Object=MibScalar
ntcDssOIpInMulticastSourceA=_NtcDssOIpInMulticastSourceA_Object((1,3,6,1,4,1,5835,5,2,8700,1,8),_NtcDssOIpInMulticastSourceA_Type())
ntcDssOIpInMulticastSourceA.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDssOIpInMulticastSourceA.setStatus(_A)
class _NtcDssOIpInMulticastSourceB_Type(NtcNetworkAddress):defaultValue=OctetString(_M)
_NtcDssOIpInMulticastSourceB_Type.__name__=_G
_NtcDssOIpInMulticastSourceB_Object=MibScalar
ntcDssOIpInMulticastSourceB=_NtcDssOIpInMulticastSourceB_Object((1,3,6,1,4,1,5835,5,2,8700,1,9),_NtcDssOIpInMulticastSourceB_Type())
ntcDssOIpInMulticastSourceB.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDssOIpInMulticastSourceB.setStatus(_A)
_NtcDssOIpInMonitor_ObjectIdentity=ObjectIdentity
ntcDssOIpInMonitor=_NtcDssOIpInMonitor_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8700,1,10))
if mibBuilder.loadTexts:ntcDssOIpInMonitor.setStatus(_A)
class _NtcDssOIpInMonResetCounters_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('counting',0),('reset',1)))
_NtcDssOIpInMonResetCounters_Type.__name__=_E
_NtcDssOIpInMonResetCounters_Object=MibScalar
ntcDssOIpInMonResetCounters=_NtcDssOIpInMonResetCounters_Object((1,3,6,1,4,1,5835,5,2,8700,1,10,1),_NtcDssOIpInMonResetCounters_Type())
ntcDssOIpInMonResetCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDssOIpInMonResetCounters.setStatus(_A)
_NtcDssOIpInMonInputDssBitRate_Type=Unsigned32
_NtcDssOIpInMonInputDssBitRate_Object=MibScalar
ntcDssOIpInMonInputDssBitRate=_NtcDssOIpInMonInputDssBitRate_Object((1,3,6,1,4,1,5835,5,2,8700,1,10,2),_NtcDssOIpInMonInputDssBitRate_Type())
ntcDssOIpInMonInputDssBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpInMonInputDssBitRate.setStatus(_A)
if mibBuilder.loadTexts:ntcDssOIpInMonInputDssBitRate.setUnits('bps')
_NtcDssOIpInMonBufferDelay_Type=Unsigned32
_NtcDssOIpInMonBufferDelay_Object=MibScalar
ntcDssOIpInMonBufferDelay=_NtcDssOIpInMonBufferDelay_Object((1,3,6,1,4,1,5835,5,2,8700,1,10,3),_NtcDssOIpInMonBufferDelay_Type())
ntcDssOIpInMonBufferDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpInMonBufferDelay.setStatus(_A)
if mibBuilder.loadTexts:ntcDssOIpInMonBufferDelay.setUnits(_F)
_NtcDssOIpInMonMinBufferFilling_Type=Unsigned32
_NtcDssOIpInMonMinBufferFilling_Object=MibScalar
ntcDssOIpInMonMinBufferFilling=_NtcDssOIpInMonMinBufferFilling_Object((1,3,6,1,4,1,5835,5,2,8700,1,10,4),_NtcDssOIpInMonMinBufferFilling_Type())
ntcDssOIpInMonMinBufferFilling.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpInMonMinBufferFilling.setStatus(_A)
if mibBuilder.loadTexts:ntcDssOIpInMonMinBufferFilling.setUnits(_F)
_NtcDssOIpInMonMaxBufferFilling_Type=Unsigned32
_NtcDssOIpInMonMaxBufferFilling_Object=MibScalar
ntcDssOIpInMonMaxBufferFilling=_NtcDssOIpInMonMaxBufferFilling_Object((1,3,6,1,4,1,5835,5,2,8700,1,10,5),_NtcDssOIpInMonMaxBufferFilling_Type())
ntcDssOIpInMonMaxBufferFilling.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpInMonMaxBufferFilling.setStatus(_A)
if mibBuilder.loadTexts:ntcDssOIpInMonMaxBufferFilling.setUnits(_F)
class _NtcDssOIpInMonSourceInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcDssOIpInMonSourceInfo_Type.__name__=_I
_NtcDssOIpInMonSourceInfo_Object=MibScalar
ntcDssOIpInMonSourceInfo=_NtcDssOIpInMonSourceInfo_Object((1,3,6,1,4,1,5835,5,2,8700,1,10,6),_NtcDssOIpInMonSourceInfo_Type())
ntcDssOIpInMonSourceInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpInMonSourceInfo.setStatus(_A)
class _NtcDssOIpInMonRtpFecScheme_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcDssOIpInMonRtpFecScheme_Type.__name__=_I
_NtcDssOIpInMonRtpFecScheme_Object=MibScalar
ntcDssOIpInMonRtpFecScheme=_NtcDssOIpInMonRtpFecScheme_Object((1,3,6,1,4,1,5835,5,2,8700,1,10,7),_NtcDssOIpInMonRtpFecScheme_Type())
ntcDssOIpInMonRtpFecScheme.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpInMonRtpFecScheme.setStatus(_A)
_NtcDssOIpInMonRtpDropCount_Type=Counter32
_NtcDssOIpInMonRtpDropCount_Object=MibScalar
ntcDssOIpInMonRtpDropCount=_NtcDssOIpInMonRtpDropCount_Object((1,3,6,1,4,1,5835,5,2,8700,1,10,8),_NtcDssOIpInMonRtpDropCount_Type())
ntcDssOIpInMonRtpDropCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpInMonRtpDropCount.setStatus(_A)
if mibBuilder.loadTexts:ntcDssOIpInMonRtpDropCount.setUnits(_J)
_NtcDssOIpInMonRtpRepairCount_Type=Counter32
_NtcDssOIpInMonRtpRepairCount_Object=MibScalar
ntcDssOIpInMonRtpRepairCount=_NtcDssOIpInMonRtpRepairCount_Object((1,3,6,1,4,1,5835,5,2,8700,1,10,9),_NtcDssOIpInMonRtpRepairCount_Type())
ntcDssOIpInMonRtpRepairCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpInMonRtpRepairCount.setStatus(_A)
if mibBuilder.loadTexts:ntcDssOIpInMonRtpRepairCount.setUnits(_J)
_NtcDssOIpInMonRtpFecDropCount_Type=Counter32
_NtcDssOIpInMonRtpFecDropCount_Object=MibScalar
ntcDssOIpInMonRtpFecDropCount=_NtcDssOIpInMonRtpFecDropCount_Object((1,3,6,1,4,1,5835,5,2,8700,1,10,10),_NtcDssOIpInMonRtpFecDropCount_Type())
ntcDssOIpInMonRtpFecDropCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpInMonRtpFecDropCount.setStatus(_A)
if mibBuilder.loadTexts:ntcDssOIpInMonRtpFecDropCount.setUnits(_J)
_NtcDssOIpInAlarm_ObjectIdentity=ObjectIdentity
ntcDssOIpInAlarm=_NtcDssOIpInAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8700,1,11))
if mibBuilder.loadTexts:ntcDssOIpInAlarm.setStatus(_A)
_NtcDssOIpInAlmNoInputData_Type=NtcAlarmState
_NtcDssOIpInAlmNoInputData_Object=MibScalar
ntcDssOIpInAlmNoInputData=_NtcDssOIpInAlmNoInputData_Object((1,3,6,1,4,1,5835,5,2,8700,1,11,1),_NtcDssOIpInAlmNoInputData_Type())
ntcDssOIpInAlmNoInputData.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpInAlmNoInputData.setStatus(_A)
_NtcDssOIpInAlmBufferOverflow_Type=NtcAlarmState
_NtcDssOIpInAlmBufferOverflow_Object=MibScalar
ntcDssOIpInAlmBufferOverflow=_NtcDssOIpInAlmBufferOverflow_Object((1,3,6,1,4,1,5835,5,2,8700,1,11,2),_NtcDssOIpInAlmBufferOverflow_Type())
ntcDssOIpInAlmBufferOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpInAlmBufferOverflow.setStatus(_A)
_NtcDssOIpInAlmBufferUnflow_Type=NtcAlarmState
_NtcDssOIpInAlmBufferUnflow_Object=MibScalar
ntcDssOIpInAlmBufferUnflow=_NtcDssOIpInAlmBufferUnflow_Object((1,3,6,1,4,1,5835,5,2,8700,1,11,3),_NtcDssOIpInAlmBufferUnflow_Type())
ntcDssOIpInAlmBufferUnflow.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpInAlmBufferUnflow.setStatus(_A)
_NtcDssOIpInAlmRtpNoSync_Type=NtcAlarmState
_NtcDssOIpInAlmRtpNoSync_Object=MibScalar
ntcDssOIpInAlmRtpNoSync=_NtcDssOIpInAlmRtpNoSync_Object((1,3,6,1,4,1,5835,5,2,8700,1,11,4),_NtcDssOIpInAlmRtpNoSync_Type())
ntcDssOIpInAlmRtpNoSync.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpInAlmRtpNoSync.setStatus(_A)
_NtcDssOIpInConformance_ObjectIdentity=ObjectIdentity
ntcDssOIpInConformance=_NtcDssOIpInConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8700,2))
if mibBuilder.loadTexts:ntcDssOIpInConformance.setStatus(_A)
_NtcDssOIpInConfCompliance_ObjectIdentity=ObjectIdentity
ntcDssOIpInConfCompliance=_NtcDssOIpInConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8700,2,1))
if mibBuilder.loadTexts:ntcDssOIpInConfCompliance.setStatus(_A)
_NtcDssOIpInConfGroup_ObjectIdentity=ObjectIdentity
ntcDssOIpInConfGroup=_NtcDssOIpInConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8700,2,2))
if mibBuilder.loadTexts:ntcDssOIpInConfGroup.setStatus(_A)
ntcDssOIpInConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,8700,2,2,1))
ntcDssOIpInConfGrpV1Standard.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:ntcDssOIpInConfGrpV1Standard.setStatus(_A)
ntcDssOIpInConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,8700,2,1,1))
ntcDssOIpInConfCompV1Standard.setObjects((_B,_k))
if mibBuilder.loadTexts:ntcDssOIpInConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcDssOverIpIn':ntcDssOverIpIn,'ntcDssOIpInObjects':ntcDssOIpInObjects,_N:ntcDssOIpInEnable,_O:ntcDssOIpInInputSelection,_P:ntcDssOIpInDssEncapProtocol,_Q:ntcDssOIpInIpAddressType,_R:ntcDssOIpInMulticastAddress,_S:ntcDssOIpInUdpPort,_T:ntcDssOIpInMaxBufferDelay,_U:ntcDssOIpInMulticastSourceA,_V:ntcDssOIpInMulticastSourceB,'ntcDssOIpInMonitor':ntcDssOIpInMonitor,_W:ntcDssOIpInMonResetCounters,_X:ntcDssOIpInMonInputDssBitRate,_Y:ntcDssOIpInMonBufferDelay,_Z:ntcDssOIpInMonMinBufferFilling,_a:ntcDssOIpInMonMaxBufferFilling,_b:ntcDssOIpInMonSourceInfo,_c:ntcDssOIpInMonRtpFecScheme,_d:ntcDssOIpInMonRtpDropCount,_e:ntcDssOIpInMonRtpRepairCount,_f:ntcDssOIpInMonRtpFecDropCount,'ntcDssOIpInAlarm':ntcDssOIpInAlarm,_g:ntcDssOIpInAlmNoInputData,_h:ntcDssOIpInAlmBufferOverflow,_i:ntcDssOIpInAlmBufferUnflow,_j:ntcDssOIpInAlmRtpNoSync,'ntcDssOIpInConformance':ntcDssOIpInConformance,'ntcDssOIpInConfCompliance':ntcDssOIpInConfCompliance,'ntcDssOIpInConfCompV1Standard':ntcDssOIpInConfCompV1Standard,'ntcDssOIpInConfGroup':ntcDssOIpInConfGroup,_k:ntcDssOIpInConfGrpV1Standard})