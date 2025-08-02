_Y='ntcTsOIpOutConfGrpV1Standard'
_X='ntcTsOIpOutAlOutputOverflow'
_W='ntcTsOIpOutAlNoOutput'
_V='ntcTsOIpOutOverflowCount'
_U='ntcTsOIpOutDropCount'
_T='ntcTsOIpOutBitrate'
_S='ntcTsOIpOutCounterReset'
_R='ntcTsOIpOutFlushScheduleTime'
_Q='ntcTsOIpOutRtpFecRows'
_P='ntcTsOIpOutRtpFecColumns'
_O='ntcTsOIpOutTsPacketsInFrame'
_N='ntcTsOIpOutTtl'
_M='ntcTsOIpOutDestIpAddress'
_L='ntcTsOIpOutDestUdpPort'
_K='ntcTsOIpOutTsEncapProtocol'
_J='ntcTsOIpOutEnable'
_I='NtcNetworkAddress'
_H='NtcEnable'
_G='packets'
_F='Integer32'
_E='read-only'
_D='Unsigned32'
_C='read-write'
_B='NEWTEC-TSOVERIPOUT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable,NtcNetworkAddress=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcTsOverIpOut=ModuleIdentity((1,3,6,1,4,1,5835,5,2,8400))
if mibBuilder.loadTexts:ntcTsOverIpOut.setRevisions(('2017-07-10 12:00','2016-12-05 12:00','2016-02-02 07:00','2014-09-09 09:00'))
_NtcTsOIpOutObjects_ObjectIdentity=ObjectIdentity
ntcTsOIpOutObjects=_NtcTsOIpOutObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8400,1))
if mibBuilder.loadTexts:ntcTsOIpOutObjects.setStatus(_A)
_NtcTsOIpOutConfiguration_ObjectIdentity=ObjectIdentity
ntcTsOIpOutConfiguration=_NtcTsOIpOutConfiguration_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8400,1,1))
if mibBuilder.loadTexts:ntcTsOIpOutConfiguration.setStatus(_A)
class _NtcTsOIpOutEnable_Type(NtcEnable):defaultValue=0
_NtcTsOIpOutEnable_Type.__name__=_H
_NtcTsOIpOutEnable_Object=MibScalar
ntcTsOIpOutEnable=_NtcTsOIpOutEnable_Object((1,3,6,1,4,1,5835,5,2,8400,1,1,1),_NtcTsOIpOutEnable_Type())
ntcTsOIpOutEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpOutEnable.setStatus(_A)
class _NtcTsOIpOutTsEncapProtocol_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('udp',0),('rtp',1),('rtpfeccolsonly',2),('rtpfeccolsandrows',3)))
_NtcTsOIpOutTsEncapProtocol_Type.__name__=_F
_NtcTsOIpOutTsEncapProtocol_Object=MibScalar
ntcTsOIpOutTsEncapProtocol=_NtcTsOIpOutTsEncapProtocol_Object((1,3,6,1,4,1,5835,5,2,8400,1,1,2),_NtcTsOIpOutTsEncapProtocol_Type())
ntcTsOIpOutTsEncapProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpOutTsEncapProtocol.setStatus(_A)
class _NtcTsOIpOutDestUdpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NtcTsOIpOutDestUdpPort_Type.__name__=_D
_NtcTsOIpOutDestUdpPort_Object=MibScalar
ntcTsOIpOutDestUdpPort=_NtcTsOIpOutDestUdpPort_Object((1,3,6,1,4,1,5835,5,2,8400,1,1,3),_NtcTsOIpOutDestUdpPort_Type())
ntcTsOIpOutDestUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpOutDestUdpPort.setStatus(_A)
class _NtcTsOIpOutDestIpAddress_Type(NtcNetworkAddress):defaultValue=OctetString('10.0.0.1')
_NtcTsOIpOutDestIpAddress_Type.__name__=_I
_NtcTsOIpOutDestIpAddress_Object=MibScalar
ntcTsOIpOutDestIpAddress=_NtcTsOIpOutDestIpAddress_Object((1,3,6,1,4,1,5835,5,2,8400,1,1,4),_NtcTsOIpOutDestIpAddress_Type())
ntcTsOIpOutDestIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpOutDestIpAddress.setStatus(_A)
class _NtcTsOIpOutTtl_Type(Unsigned32):defaultValue=8;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_NtcTsOIpOutTtl_Type.__name__=_D
_NtcTsOIpOutTtl_Object=MibScalar
ntcTsOIpOutTtl=_NtcTsOIpOutTtl_Object((1,3,6,1,4,1,5835,5,2,8400,1,1,5),_NtcTsOIpOutTtl_Type())
ntcTsOIpOutTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpOutTtl.setStatus(_A)
class _NtcTsOIpOutTsPacketsInFrame_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_NtcTsOIpOutTsPacketsInFrame_Type.__name__=_D
_NtcTsOIpOutTsPacketsInFrame_Object=MibScalar
ntcTsOIpOutTsPacketsInFrame=_NtcTsOIpOutTsPacketsInFrame_Object((1,3,6,1,4,1,5835,5,2,8400,1,1,6),_NtcTsOIpOutTsPacketsInFrame_Type())
ntcTsOIpOutTsPacketsInFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpOutTsPacketsInFrame.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpOutTsPacketsInFrame.setUnits(_G)
class _NtcTsOIpOutRtpFecColumns_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_NtcTsOIpOutRtpFecColumns_Type.__name__=_D
_NtcTsOIpOutRtpFecColumns_Object=MibScalar
ntcTsOIpOutRtpFecColumns=_NtcTsOIpOutRtpFecColumns_Object((1,3,6,1,4,1,5835,5,2,8400,1,1,7),_NtcTsOIpOutRtpFecColumns_Type())
ntcTsOIpOutRtpFecColumns.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpOutRtpFecColumns.setStatus(_A)
class _NtcTsOIpOutRtpFecRows_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,20))
_NtcTsOIpOutRtpFecRows_Type.__name__=_D
_NtcTsOIpOutRtpFecRows_Object=MibScalar
ntcTsOIpOutRtpFecRows=_NtcTsOIpOutRtpFecRows_Object((1,3,6,1,4,1,5835,5,2,8400,1,1,8),_NtcTsOIpOutRtpFecRows_Type())
ntcTsOIpOutRtpFecRows.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpOutRtpFecRows.setStatus(_A)
class _NtcTsOIpOutFlushScheduleTime_Type(Unsigned32):defaultValue=4000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,5000))
_NtcTsOIpOutFlushScheduleTime_Type.__name__=_D
_NtcTsOIpOutFlushScheduleTime_Object=MibScalar
ntcTsOIpOutFlushScheduleTime=_NtcTsOIpOutFlushScheduleTime_Object((1,3,6,1,4,1,5835,5,2,8400,1,1,9),_NtcTsOIpOutFlushScheduleTime_Type())
ntcTsOIpOutFlushScheduleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpOutFlushScheduleTime.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpOutFlushScheduleTime.setUnits('us')
_NtcTsOIpOutMonitoring_ObjectIdentity=ObjectIdentity
ntcTsOIpOutMonitoring=_NtcTsOIpOutMonitoring_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8400,1,2))
if mibBuilder.loadTexts:ntcTsOIpOutMonitoring.setStatus(_A)
class _NtcTsOIpOutCounterReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('counting',0),('reset',1)))
_NtcTsOIpOutCounterReset_Type.__name__=_F
_NtcTsOIpOutCounterReset_Object=MibScalar
ntcTsOIpOutCounterReset=_NtcTsOIpOutCounterReset_Object((1,3,6,1,4,1,5835,5,2,8400,1,2,1),_NtcTsOIpOutCounterReset_Type())
ntcTsOIpOutCounterReset.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsOIpOutCounterReset.setStatus(_A)
_NtcTsOIpOutBitrate_Type=Unsigned32
_NtcTsOIpOutBitrate_Object=MibScalar
ntcTsOIpOutBitrate=_NtcTsOIpOutBitrate_Object((1,3,6,1,4,1,5835,5,2,8400,1,2,2),_NtcTsOIpOutBitrate_Type())
ntcTsOIpOutBitrate.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcTsOIpOutBitrate.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpOutBitrate.setUnits('bps')
_NtcTsOIpOutDropCount_Type=Counter32
_NtcTsOIpOutDropCount_Object=MibScalar
ntcTsOIpOutDropCount=_NtcTsOIpOutDropCount_Object((1,3,6,1,4,1,5835,5,2,8400,1,2,3),_NtcTsOIpOutDropCount_Type())
ntcTsOIpOutDropCount.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcTsOIpOutDropCount.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpOutDropCount.setUnits(_G)
_NtcTsOIpOutOverflowCount_Type=Counter32
_NtcTsOIpOutOverflowCount_Object=MibScalar
ntcTsOIpOutOverflowCount=_NtcTsOIpOutOverflowCount_Object((1,3,6,1,4,1,5835,5,2,8400,1,2,4),_NtcTsOIpOutOverflowCount_Type())
ntcTsOIpOutOverflowCount.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcTsOIpOutOverflowCount.setStatus(_A)
if mibBuilder.loadTexts:ntcTsOIpOutOverflowCount.setUnits(_G)
_NtcTsOIpOutAlarms_ObjectIdentity=ObjectIdentity
ntcTsOIpOutAlarms=_NtcTsOIpOutAlarms_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8400,1,3))
if mibBuilder.loadTexts:ntcTsOIpOutAlarms.setStatus(_A)
_NtcTsOIpOutAlNoOutput_Type=NtcAlarmState
_NtcTsOIpOutAlNoOutput_Object=MibScalar
ntcTsOIpOutAlNoOutput=_NtcTsOIpOutAlNoOutput_Object((1,3,6,1,4,1,5835,5,2,8400,1,3,1),_NtcTsOIpOutAlNoOutput_Type())
ntcTsOIpOutAlNoOutput.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcTsOIpOutAlNoOutput.setStatus(_A)
_NtcTsOIpOutAlOutputOverflow_Type=NtcAlarmState
_NtcTsOIpOutAlOutputOverflow_Object=MibScalar
ntcTsOIpOutAlOutputOverflow=_NtcTsOIpOutAlOutputOverflow_Object((1,3,6,1,4,1,5835,5,2,8400,1,3,2),_NtcTsOIpOutAlOutputOverflow_Type())
ntcTsOIpOutAlOutputOverflow.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcTsOIpOutAlOutputOverflow.setStatus(_A)
_NtcTsOIpOutConformance_ObjectIdentity=ObjectIdentity
ntcTsOIpOutConformance=_NtcTsOIpOutConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8400,2))
if mibBuilder.loadTexts:ntcTsOIpOutConformance.setStatus(_A)
_NtcTsOIpOutConfCompliance_ObjectIdentity=ObjectIdentity
ntcTsOIpOutConfCompliance=_NtcTsOIpOutConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8400,2,1))
if mibBuilder.loadTexts:ntcTsOIpOutConfCompliance.setStatus(_A)
_NtcTsOIpOutConfGroup_ObjectIdentity=ObjectIdentity
ntcTsOIpOutConfGroup=_NtcTsOIpOutConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8400,2,2))
if mibBuilder.loadTexts:ntcTsOIpOutConfGroup.setStatus(_A)
ntcTsOIpOutConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,8400,2,2,1))
ntcTsOIpOutConfGrpV1Standard.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ntcTsOIpOutConfGrpV1Standard.setStatus(_A)
ntcTsOIpOutConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,8400,2,1,1))
ntcTsOIpOutConfCompV1Standard.setObjects((_B,_Y))
if mibBuilder.loadTexts:ntcTsOIpOutConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcTsOverIpOut':ntcTsOverIpOut,'ntcTsOIpOutObjects':ntcTsOIpOutObjects,'ntcTsOIpOutConfiguration':ntcTsOIpOutConfiguration,_J:ntcTsOIpOutEnable,_K:ntcTsOIpOutTsEncapProtocol,_L:ntcTsOIpOutDestUdpPort,_M:ntcTsOIpOutDestIpAddress,_N:ntcTsOIpOutTtl,_O:ntcTsOIpOutTsPacketsInFrame,_P:ntcTsOIpOutRtpFecColumns,_Q:ntcTsOIpOutRtpFecRows,_R:ntcTsOIpOutFlushScheduleTime,'ntcTsOIpOutMonitoring':ntcTsOIpOutMonitoring,_S:ntcTsOIpOutCounterReset,_T:ntcTsOIpOutBitrate,_U:ntcTsOIpOutDropCount,_V:ntcTsOIpOutOverflowCount,'ntcTsOIpOutAlarms':ntcTsOIpOutAlarms,_W:ntcTsOIpOutAlNoOutput,_X:ntcTsOIpOutAlOutputOverflow,'ntcTsOIpOutConformance':ntcTsOIpOutConformance,'ntcTsOIpOutConfCompliance':ntcTsOIpOutConfCompliance,'ntcTsOIpOutConfCompV1Standard':ntcTsOIpOutConfCompV1Standard,'ntcTsOIpOutConfGroup':ntcTsOIpOutConfGroup,_Y:ntcTsOIpOutConfGrpV1Standard})