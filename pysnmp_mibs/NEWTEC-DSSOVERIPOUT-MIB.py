_U='ntcDssOIpOutConfGrpV1Standard'
_T='ntcDssOIpOutAlOutputOverflow'
_S='ntcDssOIpOutAlNoOutput'
_R='ntcDssOIpOutBitrate'
_Q='ntcDssOIpOutCounterReset'
_P='ntcDssOIpOutRtpFecRows'
_O='ntcDssOIpOutRtpFecColumns'
_N='ntcDssOIpOutDssPacketsInFrame'
_M='ntcDssOIpOutTtl'
_L='ntcDssOIpOutDestIpAddress'
_K='ntcDssOIpOutDestUdpPort'
_J='ntcDssOIpOutDssEncapProtocol'
_I='ntcDssOIpOutEnable'
_H='NtcNetworkAddress'
_G='NtcEnable'
_F='read-only'
_E='Integer32'
_D='Unsigned32'
_C='read-write'
_B='NEWTEC-DSSOVERIPOUT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable,NtcNetworkAddress=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcDssOverIpOut=ModuleIdentity((1,3,6,1,4,1,5835,5,2,9300))
if mibBuilder.loadTexts:ntcDssOverIpOut.setRevisions(('2017-07-10 12:00','2016-02-02 07:00'))
_NtcDssOIpOutObjects_ObjectIdentity=ObjectIdentity
ntcDssOIpOutObjects=_NtcDssOIpOutObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9300,1))
if mibBuilder.loadTexts:ntcDssOIpOutObjects.setStatus(_A)
_NtcDssOIpOutConfiguration_ObjectIdentity=ObjectIdentity
ntcDssOIpOutConfiguration=_NtcDssOIpOutConfiguration_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9300,1,1))
if mibBuilder.loadTexts:ntcDssOIpOutConfiguration.setStatus(_A)
class _NtcDssOIpOutEnable_Type(NtcEnable):defaultValue=0
_NtcDssOIpOutEnable_Type.__name__=_G
_NtcDssOIpOutEnable_Object=MibScalar
ntcDssOIpOutEnable=_NtcDssOIpOutEnable_Object((1,3,6,1,4,1,5835,5,2,9300,1,1,1),_NtcDssOIpOutEnable_Type())
ntcDssOIpOutEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpOutEnable.setStatus(_A)
class _NtcDssOIpOutDssEncapProtocol_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('udp',0),('rtp',1),('rtpfeccolsonly',2),('rtpfeccolsandrows',3)))
_NtcDssOIpOutDssEncapProtocol_Type.__name__=_E
_NtcDssOIpOutDssEncapProtocol_Object=MibScalar
ntcDssOIpOutDssEncapProtocol=_NtcDssOIpOutDssEncapProtocol_Object((1,3,6,1,4,1,5835,5,2,9300,1,1,2),_NtcDssOIpOutDssEncapProtocol_Type())
ntcDssOIpOutDssEncapProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpOutDssEncapProtocol.setStatus(_A)
class _NtcDssOIpOutDestUdpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NtcDssOIpOutDestUdpPort_Type.__name__=_D
_NtcDssOIpOutDestUdpPort_Object=MibScalar
ntcDssOIpOutDestUdpPort=_NtcDssOIpOutDestUdpPort_Object((1,3,6,1,4,1,5835,5,2,9300,1,1,3),_NtcDssOIpOutDestUdpPort_Type())
ntcDssOIpOutDestUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpOutDestUdpPort.setStatus(_A)
class _NtcDssOIpOutDestIpAddress_Type(NtcNetworkAddress):defaultValue=OctetString('10.0.0.1')
_NtcDssOIpOutDestIpAddress_Type.__name__=_H
_NtcDssOIpOutDestIpAddress_Object=MibScalar
ntcDssOIpOutDestIpAddress=_NtcDssOIpOutDestIpAddress_Object((1,3,6,1,4,1,5835,5,2,9300,1,1,4),_NtcDssOIpOutDestIpAddress_Type())
ntcDssOIpOutDestIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpOutDestIpAddress.setStatus(_A)
class _NtcDssOIpOutTtl_Type(Unsigned32):defaultValue=8;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_NtcDssOIpOutTtl_Type.__name__=_D
_NtcDssOIpOutTtl_Object=MibScalar
ntcDssOIpOutTtl=_NtcDssOIpOutTtl_Object((1,3,6,1,4,1,5835,5,2,9300,1,1,5),_NtcDssOIpOutTtl_Type())
ntcDssOIpOutTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpOutTtl.setStatus(_A)
class _NtcDssOIpOutDssPacketsInFrame_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_NtcDssOIpOutDssPacketsInFrame_Type.__name__=_D
_NtcDssOIpOutDssPacketsInFrame_Object=MibScalar
ntcDssOIpOutDssPacketsInFrame=_NtcDssOIpOutDssPacketsInFrame_Object((1,3,6,1,4,1,5835,5,2,9300,1,1,6),_NtcDssOIpOutDssPacketsInFrame_Type())
ntcDssOIpOutDssPacketsInFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpOutDssPacketsInFrame.setStatus(_A)
if mibBuilder.loadTexts:ntcDssOIpOutDssPacketsInFrame.setUnits('packets')
class _NtcDssOIpOutRtpFecColumns_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_NtcDssOIpOutRtpFecColumns_Type.__name__=_D
_NtcDssOIpOutRtpFecColumns_Object=MibScalar
ntcDssOIpOutRtpFecColumns=_NtcDssOIpOutRtpFecColumns_Object((1,3,6,1,4,1,5835,5,2,9300,1,1,7),_NtcDssOIpOutRtpFecColumns_Type())
ntcDssOIpOutRtpFecColumns.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpOutRtpFecColumns.setStatus(_A)
class _NtcDssOIpOutRtpFecRows_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,20))
_NtcDssOIpOutRtpFecRows_Type.__name__=_D
_NtcDssOIpOutRtpFecRows_Object=MibScalar
ntcDssOIpOutRtpFecRows=_NtcDssOIpOutRtpFecRows_Object((1,3,6,1,4,1,5835,5,2,9300,1,1,8),_NtcDssOIpOutRtpFecRows_Type())
ntcDssOIpOutRtpFecRows.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpOutRtpFecRows.setStatus(_A)
_NtcDssOIpOutMonitoring_ObjectIdentity=ObjectIdentity
ntcDssOIpOutMonitoring=_NtcDssOIpOutMonitoring_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9300,1,2))
if mibBuilder.loadTexts:ntcDssOIpOutMonitoring.setStatus(_A)
class _NtcDssOIpOutCounterReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('counting',0),('reset',1)))
_NtcDssOIpOutCounterReset_Type.__name__=_E
_NtcDssOIpOutCounterReset_Object=MibScalar
ntcDssOIpOutCounterReset=_NtcDssOIpOutCounterReset_Object((1,3,6,1,4,1,5835,5,2,9300,1,2,1),_NtcDssOIpOutCounterReset_Type())
ntcDssOIpOutCounterReset.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDssOIpOutCounterReset.setStatus(_A)
_NtcDssOIpOutBitrate_Type=Unsigned32
_NtcDssOIpOutBitrate_Object=MibScalar
ntcDssOIpOutBitrate=_NtcDssOIpOutBitrate_Object((1,3,6,1,4,1,5835,5,2,9300,1,2,2),_NtcDssOIpOutBitrate_Type())
ntcDssOIpOutBitrate.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcDssOIpOutBitrate.setStatus(_A)
if mibBuilder.loadTexts:ntcDssOIpOutBitrate.setUnits('bps')
_NtcDssOIpOutAlarms_ObjectIdentity=ObjectIdentity
ntcDssOIpOutAlarms=_NtcDssOIpOutAlarms_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9300,1,3))
if mibBuilder.loadTexts:ntcDssOIpOutAlarms.setStatus(_A)
_NtcDssOIpOutAlNoOutput_Type=NtcAlarmState
_NtcDssOIpOutAlNoOutput_Object=MibScalar
ntcDssOIpOutAlNoOutput=_NtcDssOIpOutAlNoOutput_Object((1,3,6,1,4,1,5835,5,2,9300,1,3,1),_NtcDssOIpOutAlNoOutput_Type())
ntcDssOIpOutAlNoOutput.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcDssOIpOutAlNoOutput.setStatus(_A)
_NtcDssOIpOutAlOutputOverflow_Type=NtcAlarmState
_NtcDssOIpOutAlOutputOverflow_Object=MibScalar
ntcDssOIpOutAlOutputOverflow=_NtcDssOIpOutAlOutputOverflow_Object((1,3,6,1,4,1,5835,5,2,9300,1,3,2),_NtcDssOIpOutAlOutputOverflow_Type())
ntcDssOIpOutAlOutputOverflow.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcDssOIpOutAlOutputOverflow.setStatus(_A)
_NtcDssOIpOutConformance_ObjectIdentity=ObjectIdentity
ntcDssOIpOutConformance=_NtcDssOIpOutConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9300,2))
if mibBuilder.loadTexts:ntcDssOIpOutConformance.setStatus(_A)
_NtcDssOIpOutConfCompliance_ObjectIdentity=ObjectIdentity
ntcDssOIpOutConfCompliance=_NtcDssOIpOutConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9300,2,1))
if mibBuilder.loadTexts:ntcDssOIpOutConfCompliance.setStatus(_A)
_NtcDssOIpOutConfGroup_ObjectIdentity=ObjectIdentity
ntcDssOIpOutConfGroup=_NtcDssOIpOutConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9300,2,2))
if mibBuilder.loadTexts:ntcDssOIpOutConfGroup.setStatus(_A)
ntcDssOIpOutConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,9300,2,2,1))
ntcDssOIpOutConfGrpV1Standard.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ntcDssOIpOutConfGrpV1Standard.setStatus(_A)
ntcDssOIpOutConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,9300,2,1,1))
ntcDssOIpOutConfCompV1Standard.setObjects((_B,_U))
if mibBuilder.loadTexts:ntcDssOIpOutConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcDssOverIpOut':ntcDssOverIpOut,'ntcDssOIpOutObjects':ntcDssOIpOutObjects,'ntcDssOIpOutConfiguration':ntcDssOIpOutConfiguration,_I:ntcDssOIpOutEnable,_J:ntcDssOIpOutDssEncapProtocol,_K:ntcDssOIpOutDestUdpPort,_L:ntcDssOIpOutDestIpAddress,_M:ntcDssOIpOutTtl,_N:ntcDssOIpOutDssPacketsInFrame,_O:ntcDssOIpOutRtpFecColumns,_P:ntcDssOIpOutRtpFecRows,'ntcDssOIpOutMonitoring':ntcDssOIpOutMonitoring,_Q:ntcDssOIpOutCounterReset,_R:ntcDssOIpOutBitrate,'ntcDssOIpOutAlarms':ntcDssOIpOutAlarms,_S:ntcDssOIpOutAlNoOutput,_T:ntcDssOIpOutAlOutputOverflow,'ntcDssOIpOutConformance':ntcDssOIpOutConformance,'ntcDssOIpOutConfCompliance':ntcDssOIpOutConfCompliance,'ntcDssOIpOutConfCompV1Standard':ntcDssOIpOutConfCompV1Standard,'ntcDssOIpOutConfGroup':ntcDssOIpOutConfGroup,_U:ntcDssOIpOutConfGrpV1Standard})