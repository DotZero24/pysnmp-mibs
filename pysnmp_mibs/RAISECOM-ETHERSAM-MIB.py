_Q='rcEtherSamServiceList'
_P='rcEtherSamServiceTestResult'
_O='rcEtherSam2544FrameSize'
_N='rcEtherSamCfgStepNum'
_M='EnableVar'
_L='rcEtherSamFlowIndex'
_K='fail'
_J='pass'
_I='OctetString'
_H='not-accessible'
_G='rcEtherSamServiceIndex'
_F='RAISECOM-ETHERSAM-MIB'
_E='Unsigned32'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_M)
rcEtherSam=ModuleIdentity((1,3,6,1,4,1,8886,6,1,74))
if mibBuilder.loadTexts:rcEtherSam.setRevisions(('2012-09-10 00:00',))
_RcEtherSamGlobalGroup_ObjectIdentity=ObjectIdentity
rcEtherSamGlobalGroup=_RcEtherSamGlobalGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,74,1))
_RcEtherSamServiceList_Type=Integer32
_RcEtherSamServiceList_Object=MibScalar
rcEtherSamServiceList=_RcEtherSamServiceList_Object((1,3,6,1,4,1,8886,6,1,74,1,1),_RcEtherSamServiceList_Type())
rcEtherSamServiceList.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceList.setStatus(_A)
class _RcEtherSamServiceTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('configuration',1),('performance',2),('both',3),('rfc2544',4),('performance-inservice',5)))
_RcEtherSamServiceTestType_Type.__name__=_D
_RcEtherSamServiceTestType_Object=MibScalar
rcEtherSamServiceTestType=_RcEtherSamServiceTestType_Object((1,3,6,1,4,1,8886,6,1,74,1,2),_RcEtherSamServiceTestType_Type())
rcEtherSamServiceTestType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceTestType.setStatus(_A)
class _RcEtherSamServiceTestOperate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('start',1),('stop',2),('testing',3),('idle',4)))
_RcEtherSamServiceTestOperate_Type.__name__=_D
_RcEtherSamServiceTestOperate_Object=MibScalar
rcEtherSamServiceTestOperate=_RcEtherSamServiceTestOperate_Object((1,3,6,1,4,1,8886,6,1,74,1,3),_RcEtherSamServiceTestOperate_Type())
rcEtherSamServiceTestOperate.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceTestOperate.setStatus(_A)
class _RcEtherSamPerformanceDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,1440))
_RcEtherSamPerformanceDuration_Type.__name__=_D
_RcEtherSamPerformanceDuration_Object=MibScalar
rcEtherSamPerformanceDuration=_RcEtherSamPerformanceDuration_Object((1,3,6,1,4,1,8886,6,1,74,1,4),_RcEtherSamPerformanceDuration_Type())
rcEtherSamPerformanceDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamPerformanceDuration.setStatus(_A)
class _RcEtherSamTestElapsedTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,172800))
_RcEtherSamTestElapsedTime_Type.__name__=_D
_RcEtherSamTestElapsedTime_Object=MibScalar
rcEtherSamTestElapsedTime=_RcEtherSamTestElapsedTime_Object((1,3,6,1,4,1,8886,6,1,74,1,5),_RcEtherSamTestElapsedTime_Type())
rcEtherSamTestElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamTestElapsedTime.setStatus(_A)
class _RcEtherSamServiceTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_RcEtherSamServiceTestResult_Type.__name__=_D
_RcEtherSamServiceTestResult_Object=MibScalar
rcEtherSamServiceTestResult=_RcEtherSamServiceTestResult_Object((1,3,6,1,4,1,8886,6,1,74,1,6),_RcEtherSamServiceTestResult_Type())
rcEtherSamServiceTestResult.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamServiceTestResult.setStatus(_A)
_RcEtherSamTestGroup_ObjectIdentity=ObjectIdentity
rcEtherSamTestGroup=_RcEtherSamTestGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,74,2))
_RcEtherSamFlowTable_Object=MibTable
rcEtherSamFlowTable=_RcEtherSamFlowTable_Object((1,3,6,1,4,1,8886,6,1,74,2,1))
if mibBuilder.loadTexts:rcEtherSamFlowTable.setStatus(_A)
_RcEtherSamFlowEntry_Object=MibTableRow
rcEtherSamFlowEntry=_RcEtherSamFlowEntry_Object((1,3,6,1,4,1,8886,6,1,74,2,1,1))
rcEtherSamFlowEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:rcEtherSamFlowEntry.setStatus(_A)
class _RcEtherSamFlowIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_RcEtherSamFlowIndex_Type.__name__=_D
_RcEtherSamFlowIndex_Object=MibTableColumn
rcEtherSamFlowIndex=_RcEtherSamFlowIndex_Object((1,3,6,1,4,1,8886,6,1,74,2,1,1,1),_RcEtherSamFlowIndex_Type())
rcEtherSamFlowIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:rcEtherSamFlowIndex.setStatus(_A)
class _RcEtherSamFlowFrameType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('loopback',1),('ethernet',2),('ip',3),('tcp',4),('udp',5),('video',6),('voice-G711',7),('voice-G7231',8),('voice-G729',9)))
_RcEtherSamFlowFrameType_Type.__name__=_D
_RcEtherSamFlowFrameType_Object=MibTableColumn
rcEtherSamFlowFrameType=_RcEtherSamFlowFrameType_Object((1,3,6,1,4,1,8886,6,1,74,2,1,1,2),_RcEtherSamFlowFrameType_Type())
rcEtherSamFlowFrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowFrameType.setStatus(_A)
class _RcEtherSamFlowFrameEtherType_Type(Integer32):defaultValue=2208
_RcEtherSamFlowFrameEtherType_Type.__name__=_D
_RcEtherSamFlowFrameEtherType_Object=MibTableColumn
rcEtherSamFlowFrameEtherType=_RcEtherSamFlowFrameEtherType_Object((1,3,6,1,4,1,8886,6,1,74,2,1,1,3),_RcEtherSamFlowFrameEtherType_Type())
rcEtherSamFlowFrameEtherType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowFrameEtherType.setStatus(_A)
class _RcEtherSamFlowFrameLengthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('single',1),('mix',2)))
_RcEtherSamFlowFrameLengthType_Type.__name__=_D
_RcEtherSamFlowFrameLengthType_Object=MibTableColumn
rcEtherSamFlowFrameLengthType=_RcEtherSamFlowFrameLengthType_Object((1,3,6,1,4,1,8886,6,1,74,2,1,1,4),_RcEtherSamFlowFrameLengthType_Type())
rcEtherSamFlowFrameLengthType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowFrameLengthType.setStatus(_A)
class _RcEtherSamFlowFrameSize_Type(Integer32):defaultValue=512;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,12288))
_RcEtherSamFlowFrameSize_Type.__name__=_D
_RcEtherSamFlowFrameSize_Object=MibTableColumn
rcEtherSamFlowFrameSize=_RcEtherSamFlowFrameSize_Object((1,3,6,1,4,1,8886,6,1,74,2,1,1,5),_RcEtherSamFlowFrameSize_Type())
rcEtherSamFlowFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowFrameSize.setStatus(_A)
class _RcEtherSamFlowFrameCvlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_RcEtherSamFlowFrameCvlan_Type.__name__=_D
_RcEtherSamFlowFrameCvlan_Object=MibTableColumn
rcEtherSamFlowFrameCvlan=_RcEtherSamFlowFrameCvlan_Object((1,3,6,1,4,1,8886,6,1,74,2,1,1,6),_RcEtherSamFlowFrameCvlan_Type())
rcEtherSamFlowFrameCvlan.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowFrameCvlan.setStatus(_A)
class _RcEtherSamFlowFrameCos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcEtherSamFlowFrameCos_Type.__name__=_D
_RcEtherSamFlowFrameCos_Object=MibTableColumn
rcEtherSamFlowFrameCos=_RcEtherSamFlowFrameCos_Object((1,3,6,1,4,1,8886,6,1,74,2,1,1,7),_RcEtherSamFlowFrameCos_Type())
rcEtherSamFlowFrameCos.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowFrameCos.setStatus(_A)
_RcEtherSamFlowRowStatus_Type=RowStatus
_RcEtherSamFlowRowStatus_Object=MibTableColumn
rcEtherSamFlowRowStatus=_RcEtherSamFlowRowStatus_Object((1,3,6,1,4,1,8886,6,1,74,2,1,1,8),_RcEtherSamFlowRowStatus_Type())
rcEtherSamFlowRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowRowStatus.setStatus(_A)
class _RcEtherSamFlowDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RcEtherSamFlowDescription_Type.__name__=_I
_RcEtherSamFlowDescription_Object=MibTableColumn
rcEtherSamFlowDescription=_RcEtherSamFlowDescription_Object((1,3,6,1,4,1,8886,6,1,74,2,1,1,9),_RcEtherSamFlowDescription_Type())
rcEtherSamFlowDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowDescription.setStatus(_A)
_RcEtherSamFlowDestAddr_Type=IpAddress
_RcEtherSamFlowDestAddr_Object=MibTableColumn
rcEtherSamFlowDestAddr=_RcEtherSamFlowDestAddr_Object((1,3,6,1,4,1,8886,6,1,74,2,1,1,10),_RcEtherSamFlowDestAddr_Type())
rcEtherSamFlowDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowDestAddr.setStatus(_A)
class _RcEtherSamFlowDscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RcEtherSamFlowDscp_Type.__name__=_D
_RcEtherSamFlowDscp_Object=MibTableColumn
rcEtherSamFlowDscp=_RcEtherSamFlowDscp_Object((1,3,6,1,4,1,8886,6,1,74,2,1,1,11),_RcEtherSamFlowDscp_Type())
rcEtherSamFlowDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowDscp.setStatus(_A)
class _RcEtherSamFlowDatePattern_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('null',1),('Crc32',2)))
_RcEtherSamFlowDatePattern_Type.__name__=_D
_RcEtherSamFlowDatePattern_Object=MibTableColumn
rcEtherSamFlowDatePattern=_RcEtherSamFlowDatePattern_Object((1,3,6,1,4,1,8886,6,1,74,2,1,1,12),_RcEtherSamFlowDatePattern_Type())
rcEtherSamFlowDatePattern.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowDatePattern.setStatus(_A)
class _RcEtherSamFlowSourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcEtherSamFlowSourcePort_Type.__name__=_D
_RcEtherSamFlowSourcePort_Object=MibTableColumn
rcEtherSamFlowSourcePort=_RcEtherSamFlowSourcePort_Object((1,3,6,1,4,1,8886,6,1,74,2,1,1,13),_RcEtherSamFlowSourcePort_Type())
rcEtherSamFlowSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowSourcePort.setStatus(_A)
class _RcEtherSamFlowDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcEtherSamFlowDestPort_Type.__name__=_D
_RcEtherSamFlowDestPort_Object=MibTableColumn
rcEtherSamFlowDestPort=_RcEtherSamFlowDestPort_Object((1,3,6,1,4,1,8886,6,1,74,2,1,1,14),_RcEtherSamFlowDestPort_Type())
rcEtherSamFlowDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowDestPort.setStatus(_A)
_RcEtherSamFlowNextHopMac_Type=MacAddress
_RcEtherSamFlowNextHopMac_Object=MibTableColumn
rcEtherSamFlowNextHopMac=_RcEtherSamFlowNextHopMac_Object((1,3,6,1,4,1,8886,6,1,74,2,1,1,15),_RcEtherSamFlowNextHopMac_Type())
rcEtherSamFlowNextHopMac.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowNextHopMac.setStatus(_A)
_RcEtherSamServiceTable_Object=MibTable
rcEtherSamServiceTable=_RcEtherSamServiceTable_Object((1,3,6,1,4,1,8886,6,1,74,2,2))
if mibBuilder.loadTexts:rcEtherSamServiceTable.setStatus(_A)
_RcEtherSamServiceEntry_Object=MibTableRow
rcEtherSamServiceEntry=_RcEtherSamServiceEntry_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1))
rcEtherSamServiceEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:rcEtherSamServiceEntry.setStatus(_A)
class _RcEtherSamServiceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_RcEtherSamServiceIndex_Type.__name__=_D
_RcEtherSamServiceIndex_Object=MibTableColumn
rcEtherSamServiceIndex=_RcEtherSamServiceIndex_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,1),_RcEtherSamServiceIndex_Type())
rcEtherSamServiceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:rcEtherSamServiceIndex.setStatus(_A)
class _RcEtherSamServiceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RcEtherSamServiceName_Type.__name__=_I
_RcEtherSamServiceName_Object=MibTableColumn
rcEtherSamServiceName=_RcEtherSamServiceName_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,2),_RcEtherSamServiceName_Type())
rcEtherSamServiceName.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceName.setStatus(_A)
class _RcEtherSamServiceProfileNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_RcEtherSamServiceProfileNum_Type.__name__=_D
_RcEtherSamServiceProfileNum_Object=MibTableColumn
rcEtherSamServiceProfileNum=_RcEtherSamServiceProfileNum_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,3),_RcEtherSamServiceProfileNum_Type())
rcEtherSamServiceProfileNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceProfileNum.setStatus(_A)
class _RcEtherSamServiceSvlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcEtherSamServiceSvlan_Type.__name__=_D
_RcEtherSamServiceSvlan_Object=MibTableColumn
rcEtherSamServiceSvlan=_RcEtherSamServiceSvlan_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,4),_RcEtherSamServiceSvlan_Type())
rcEtherSamServiceSvlan.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceSvlan.setStatus(_A)
class _RcEtherSamServiceCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcEtherSamServiceCos_Type.__name__=_D
_RcEtherSamServiceCos_Object=MibTableColumn
rcEtherSamServiceCos=_RcEtherSamServiceCos_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,5),_RcEtherSamServiceCos_Type())
rcEtherSamServiceCos.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceCos.setStatus(_A)
_RcEtherSamServiceUNI_Type=Integer32
_RcEtherSamServiceUNI_Object=MibTableColumn
rcEtherSamServiceUNI=_RcEtherSamServiceUNI_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,6),_RcEtherSamServiceUNI_Type())
rcEtherSamServiceUNI.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceUNI.setStatus(_A)
_RcEtherSamServiceNNI_Type=Integer32
_RcEtherSamServiceNNI_Object=MibTableColumn
rcEtherSamServiceNNI=_RcEtherSamServiceNNI_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,7),_RcEtherSamServiceNNI_Type())
rcEtherSamServiceNNI.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceNNI.setStatus(_A)
class _RcEtherSamServiceCir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048576))
_RcEtherSamServiceCir_Type.__name__=_D
_RcEtherSamServiceCir_Object=MibTableColumn
rcEtherSamServiceCir=_RcEtherSamServiceCir_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,8),_RcEtherSamServiceCir_Type())
rcEtherSamServiceCir.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceCir.setStatus(_A)
class _RcEtherSamServiceEir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048576))
_RcEtherSamServiceEir_Type.__name__=_D
_RcEtherSamServiceEir_Object=MibTableColumn
rcEtherSamServiceEir=_RcEtherSamServiceEir_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,9),_RcEtherSamServiceEir_Type())
rcEtherSamServiceEir.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceEir.setStatus(_A)
class _RcEtherSamServiceMDL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcEtherSamServiceMDL_Type.__name__=_D
_RcEtherSamServiceMDL_Object=MibTableColumn
rcEtherSamServiceMDL=_RcEtherSamServiceMDL_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,10),_RcEtherSamServiceMDL_Type())
rcEtherSamServiceMDL.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceMDL.setStatus(_A)
_RcEtherSamServiceDMAC_Type=MacAddress
_RcEtherSamServiceDMAC_Object=MibTableColumn
rcEtherSamServiceDMAC=_RcEtherSamServiceDMAC_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,11),_RcEtherSamServiceDMAC_Type())
rcEtherSamServiceDMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceDMAC.setStatus(_A)
class _RcEtherSamServiceThresholdAvail_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_RcEtherSamServiceThresholdAvail_Type.__name__=_E
_RcEtherSamServiceThresholdAvail_Object=MibTableColumn
rcEtherSamServiceThresholdAvail=_RcEtherSamServiceThresholdAvail_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,12),_RcEtherSamServiceThresholdAvail_Type())
rcEtherSamServiceThresholdAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceThresholdAvail.setStatus(_A)
class _RcEtherSamServiceThresholdFD_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_RcEtherSamServiceThresholdFD_Type.__name__=_E
_RcEtherSamServiceThresholdFD_Object=MibTableColumn
rcEtherSamServiceThresholdFD=_RcEtherSamServiceThresholdFD_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,13),_RcEtherSamServiceThresholdFD_Type())
rcEtherSamServiceThresholdFD.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceThresholdFD.setStatus(_A)
class _RcEtherSamServiceThresholdFDV_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_RcEtherSamServiceThresholdFDV_Type.__name__=_E
_RcEtherSamServiceThresholdFDV_Object=MibTableColumn
rcEtherSamServiceThresholdFDV=_RcEtherSamServiceThresholdFDV_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,14),_RcEtherSamServiceThresholdFDV_Type())
rcEtherSamServiceThresholdFDV.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceThresholdFDV.setStatus(_A)
class _RcEtherSamServiceThresholdFLR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_RcEtherSamServiceThresholdFLR_Type.__name__=_E
_RcEtherSamServiceThresholdFLR_Object=MibTableColumn
rcEtherSamServiceThresholdFLR=_RcEtherSamServiceThresholdFLR_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,15),_RcEtherSamServiceThresholdFLR_Type())
rcEtherSamServiceThresholdFLR.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceThresholdFLR.setStatus(_A)
class _RcEtherSamServiceBandWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048576))
_RcEtherSamServiceBandWidth_Type.__name__=_D
_RcEtherSamServiceBandWidth_Object=MibTableColumn
rcEtherSamServiceBandWidth=_RcEtherSamServiceBandWidth_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,16),_RcEtherSamServiceBandWidth_Type())
rcEtherSamServiceBandWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceBandWidth.setStatus(_A)
_RcEtherSamServiceRowStatus_Type=RowStatus
_RcEtherSamServiceRowStatus_Object=MibTableColumn
rcEtherSamServiceRowStatus=_RcEtherSamServiceRowStatus_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,17),_RcEtherSamServiceRowStatus_Type())
rcEtherSamServiceRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceRowStatus.setStatus(_A)
_RcEtherSamServiceSecondNNI_Type=Integer32
_RcEtherSamServiceSecondNNI_Object=MibTableColumn
rcEtherSamServiceSecondNNI=_RcEtherSamServiceSecondNNI_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,18),_RcEtherSamServiceSecondNNI_Type())
rcEtherSamServiceSecondNNI.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceSecondNNI.setStatus(_A)
class _RcEtherSamServiceCfgBypassUniEnable_Type(EnableVar):defaultValue=2
_RcEtherSamServiceCfgBypassUniEnable_Type.__name__=_M
_RcEtherSamServiceCfgBypassUniEnable_Object=MibTableColumn
rcEtherSamServiceCfgBypassUniEnable=_RcEtherSamServiceCfgBypassUniEnable_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,19),_RcEtherSamServiceCfgBypassUniEnable_Type())
rcEtherSamServiceCfgBypassUniEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceCfgBypassUniEnable.setStatus(_A)
_RcEtherSamServiceDIPAddressType_Type=InetAddressType
_RcEtherSamServiceDIPAddressType_Object=MibTableColumn
rcEtherSamServiceDIPAddressType=_RcEtherSamServiceDIPAddressType_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,20),_RcEtherSamServiceDIPAddressType_Type())
rcEtherSamServiceDIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceDIPAddressType.setStatus(_A)
_RcEtherSamServiceDIPAddress_Type=InetAddress
_RcEtherSamServiceDIPAddress_Object=MibTableColumn
rcEtherSamServiceDIPAddress=_RcEtherSamServiceDIPAddress_Object((1,3,6,1,4,1,8886,6,1,74,2,2,1,21),_RcEtherSamServiceDIPAddress_Type())
rcEtherSamServiceDIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamServiceDIPAddress.setStatus(_A)
_RcEtherSamCfgResultTable_Object=MibTable
rcEtherSamCfgResultTable=_RcEtherSamCfgResultTable_Object((1,3,6,1,4,1,8886,6,1,74,2,3))
if mibBuilder.loadTexts:rcEtherSamCfgResultTable.setStatus(_A)
_RcEtherSamCfgResultEntry_Object=MibTableRow
rcEtherSamCfgResultEntry=_RcEtherSamCfgResultEntry_Object((1,3,6,1,4,1,8886,6,1,74,2,3,1))
rcEtherSamCfgResultEntry.setIndexNames((0,_F,_G),(0,_F,_N))
if mibBuilder.loadTexts:rcEtherSamCfgResultEntry.setStatus(_A)
class _RcEtherSamCfgStepNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_RcEtherSamCfgStepNum_Type.__name__=_D
_RcEtherSamCfgStepNum_Object=MibTableColumn
rcEtherSamCfgStepNum=_RcEtherSamCfgStepNum_Object((1,3,6,1,4,1,8886,6,1,74,2,3,1,1),_RcEtherSamCfgStepNum_Type())
rcEtherSamCfgStepNum.setMaxAccess(_H)
if mibBuilder.loadTexts:rcEtherSamCfgStepNum.setStatus(_A)
class _RcEtherSamCfgResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_RcEtherSamCfgResult_Type.__name__=_D
_RcEtherSamCfgResult_Object=MibTableColumn
rcEtherSamCfgResult=_RcEtherSamCfgResult_Object((1,3,6,1,4,1,8886,6,1,74,2,3,1,2),_RcEtherSamCfgResult_Type())
rcEtherSamCfgResult.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamCfgResult.setStatus(_A)
_RcEtherSamCfgReceiveIR_Type=Integer32
_RcEtherSamCfgReceiveIR_Object=MibTableColumn
rcEtherSamCfgReceiveIR=_RcEtherSamCfgReceiveIR_Object((1,3,6,1,4,1,8886,6,1,74,2,3,1,3),_RcEtherSamCfgReceiveIR_Type())
rcEtherSamCfgReceiveIR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamCfgReceiveIR.setStatus(_A)
class _RcEtherSamCfgFD_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_RcEtherSamCfgFD_Type.__name__=_E
_RcEtherSamCfgFD_Object=MibTableColumn
rcEtherSamCfgFD=_RcEtherSamCfgFD_Object((1,3,6,1,4,1,8886,6,1,74,2,3,1,4),_RcEtherSamCfgFD_Type())
rcEtherSamCfgFD.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamCfgFD.setStatus(_A)
class _RcEtherSamCfgFDV_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_RcEtherSamCfgFDV_Type.__name__=_E
_RcEtherSamCfgFDV_Object=MibTableColumn
rcEtherSamCfgFDV=_RcEtherSamCfgFDV_Object((1,3,6,1,4,1,8886,6,1,74,2,3,1,5),_RcEtherSamCfgFDV_Type())
rcEtherSamCfgFDV.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamCfgFDV.setStatus(_A)
class _RcEtherSamCfgFLRf_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_RcEtherSamCfgFLRf_Type.__name__=_E
_RcEtherSamCfgFLRf_Object=MibTableColumn
rcEtherSamCfgFLRf=_RcEtherSamCfgFLRf_Object((1,3,6,1,4,1,8886,6,1,74,2,3,1,6),_RcEtherSamCfgFLRf_Type())
rcEtherSamCfgFLRf.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamCfgFLRf.setStatus(_A)
class _RcEtherSamCfgFLRb_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_RcEtherSamCfgFLRb_Type.__name__=_E
_RcEtherSamCfgFLRb_Object=MibTableColumn
rcEtherSamCfgFLRb=_RcEtherSamCfgFLRb_Object((1,3,6,1,4,1,8886,6,1,74,2,3,1,7),_RcEtherSamCfgFLRb_Type())
rcEtherSamCfgFLRb.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamCfgFLRb.setStatus(_A)
_RcEtherSamPerformanceResultTable_Object=MibTable
rcEtherSamPerformanceResultTable=_RcEtherSamPerformanceResultTable_Object((1,3,6,1,4,1,8886,6,1,74,2,4))
if mibBuilder.loadTexts:rcEtherSamPerformanceResultTable.setStatus(_A)
_RcEtherSamPerformanceResultEntry_Object=MibTableRow
rcEtherSamPerformanceResultEntry=_RcEtherSamPerformanceResultEntry_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1))
rcEtherSamPerformanceResultEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:rcEtherSamPerformanceResultEntry.setStatus(_A)
class _RcEtherSamPerformanceResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_RcEtherSamPerformanceResult_Type.__name__=_D
_RcEtherSamPerformanceResult_Object=MibTableColumn
rcEtherSamPerformanceResult=_RcEtherSamPerformanceResult_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,1),_RcEtherSamPerformanceResult_Type())
rcEtherSamPerformanceResult.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceResult.setStatus(_A)
_RcEtherSamPerformanceCurrentReceiveIR_Type=Integer32
_RcEtherSamPerformanceCurrentReceiveIR_Object=MibTableColumn
rcEtherSamPerformanceCurrentReceiveIR=_RcEtherSamPerformanceCurrentReceiveIR_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,2),_RcEtherSamPerformanceCurrentReceiveIR_Type())
rcEtherSamPerformanceCurrentReceiveIR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceCurrentReceiveIR.setStatus(_A)
_RcEtherSamPerformanceMaxReceiveIR_Type=Integer32
_RcEtherSamPerformanceMaxReceiveIR_Object=MibTableColumn
rcEtherSamPerformanceMaxReceiveIR=_RcEtherSamPerformanceMaxReceiveIR_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,3),_RcEtherSamPerformanceMaxReceiveIR_Type())
rcEtherSamPerformanceMaxReceiveIR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceMaxReceiveIR.setStatus(_A)
_RcEtherSamPerformanceMinReceiveIR_Type=Integer32
_RcEtherSamPerformanceMinReceiveIR_Object=MibTableColumn
rcEtherSamPerformanceMinReceiveIR=_RcEtherSamPerformanceMinReceiveIR_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,4),_RcEtherSamPerformanceMinReceiveIR_Type())
rcEtherSamPerformanceMinReceiveIR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceMinReceiveIR.setStatus(_A)
_RcEtherSamPerformanceAverageReceiveIR_Type=Integer32
_RcEtherSamPerformanceAverageReceiveIR_Object=MibTableColumn
rcEtherSamPerformanceAverageReceiveIR=_RcEtherSamPerformanceAverageReceiveIR_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,5),_RcEtherSamPerformanceAverageReceiveIR_Type())
rcEtherSamPerformanceAverageReceiveIR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceAverageReceiveIR.setStatus(_A)
class _RcEtherSamPerformanceCurrentFD_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_RcEtherSamPerformanceCurrentFD_Type.__name__=_E
_RcEtherSamPerformanceCurrentFD_Object=MibTableColumn
rcEtherSamPerformanceCurrentFD=_RcEtherSamPerformanceCurrentFD_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,6),_RcEtherSamPerformanceCurrentFD_Type())
rcEtherSamPerformanceCurrentFD.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceCurrentFD.setStatus(_A)
class _RcEtherSamPerformanceMaxFD_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_RcEtherSamPerformanceMaxFD_Type.__name__=_E
_RcEtherSamPerformanceMaxFD_Object=MibTableColumn
rcEtherSamPerformanceMaxFD=_RcEtherSamPerformanceMaxFD_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,7),_RcEtherSamPerformanceMaxFD_Type())
rcEtherSamPerformanceMaxFD.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceMaxFD.setStatus(_A)
class _RcEtherSamPerformanceMinFD_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_RcEtherSamPerformanceMinFD_Type.__name__=_E
_RcEtherSamPerformanceMinFD_Object=MibTableColumn
rcEtherSamPerformanceMinFD=_RcEtherSamPerformanceMinFD_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,8),_RcEtherSamPerformanceMinFD_Type())
rcEtherSamPerformanceMinFD.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceMinFD.setStatus(_A)
class _RcEtherSamPerformanceAverageFD_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_RcEtherSamPerformanceAverageFD_Type.__name__=_E
_RcEtherSamPerformanceAverageFD_Object=MibTableColumn
rcEtherSamPerformanceAverageFD=_RcEtherSamPerformanceAverageFD_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,9),_RcEtherSamPerformanceAverageFD_Type())
rcEtherSamPerformanceAverageFD.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceAverageFD.setStatus(_A)
class _RcEtherSamPerformanceCurrentFDV_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_RcEtherSamPerformanceCurrentFDV_Type.__name__=_E
_RcEtherSamPerformanceCurrentFDV_Object=MibTableColumn
rcEtherSamPerformanceCurrentFDV=_RcEtherSamPerformanceCurrentFDV_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,10),_RcEtherSamPerformanceCurrentFDV_Type())
rcEtherSamPerformanceCurrentFDV.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceCurrentFDV.setStatus(_A)
class _RcEtherSamPerformanceMaxFDV_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_RcEtherSamPerformanceMaxFDV_Type.__name__=_E
_RcEtherSamPerformanceMaxFDV_Object=MibTableColumn
rcEtherSamPerformanceMaxFDV=_RcEtherSamPerformanceMaxFDV_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,11),_RcEtherSamPerformanceMaxFDV_Type())
rcEtherSamPerformanceMaxFDV.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceMaxFDV.setStatus(_A)
class _RcEtherSamPerformanceMinFDV_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_RcEtherSamPerformanceMinFDV_Type.__name__=_E
_RcEtherSamPerformanceMinFDV_Object=MibTableColumn
rcEtherSamPerformanceMinFDV=_RcEtherSamPerformanceMinFDV_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,12),_RcEtherSamPerformanceMinFDV_Type())
rcEtherSamPerformanceMinFDV.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceMinFDV.setStatus(_A)
class _RcEtherSamPerformanceAverageFDV_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_RcEtherSamPerformanceAverageFDV_Type.__name__=_E
_RcEtherSamPerformanceAverageFDV_Object=MibTableColumn
rcEtherSamPerformanceAverageFDV=_RcEtherSamPerformanceAverageFDV_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,13),_RcEtherSamPerformanceAverageFDV_Type())
rcEtherSamPerformanceAverageFDV.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceAverageFDV.setStatus(_A)
class _RcEtherSamPerformanceCurrentFLRf_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_RcEtherSamPerformanceCurrentFLRf_Type.__name__=_E
_RcEtherSamPerformanceCurrentFLRf_Object=MibTableColumn
rcEtherSamPerformanceCurrentFLRf=_RcEtherSamPerformanceCurrentFLRf_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,14),_RcEtherSamPerformanceCurrentFLRf_Type())
rcEtherSamPerformanceCurrentFLRf.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceCurrentFLRf.setStatus(_A)
class _RcEtherSamPerformanceMaxFLRf_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_RcEtherSamPerformanceMaxFLRf_Type.__name__=_E
_RcEtherSamPerformanceMaxFLRf_Object=MibTableColumn
rcEtherSamPerformanceMaxFLRf=_RcEtherSamPerformanceMaxFLRf_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,15),_RcEtherSamPerformanceMaxFLRf_Type())
rcEtherSamPerformanceMaxFLRf.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceMaxFLRf.setStatus(_A)
class _RcEtherSamPerformanceMinFLRf_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_RcEtherSamPerformanceMinFLRf_Type.__name__=_E
_RcEtherSamPerformanceMinFLRf_Object=MibTableColumn
rcEtherSamPerformanceMinFLRf=_RcEtherSamPerformanceMinFLRf_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,16),_RcEtherSamPerformanceMinFLRf_Type())
rcEtherSamPerformanceMinFLRf.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceMinFLRf.setStatus(_A)
class _RcEtherSamPerformanceAverageFLRf_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_RcEtherSamPerformanceAverageFLRf_Type.__name__=_E
_RcEtherSamPerformanceAverageFLRf_Object=MibTableColumn
rcEtherSamPerformanceAverageFLRf=_RcEtherSamPerformanceAverageFLRf_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,17),_RcEtherSamPerformanceAverageFLRf_Type())
rcEtherSamPerformanceAverageFLRf.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceAverageFLRf.setStatus(_A)
class _RcEtherSamPerformanceCurrentFLRb_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_RcEtherSamPerformanceCurrentFLRb_Type.__name__=_E
_RcEtherSamPerformanceCurrentFLRb_Object=MibTableColumn
rcEtherSamPerformanceCurrentFLRb=_RcEtherSamPerformanceCurrentFLRb_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,18),_RcEtherSamPerformanceCurrentFLRb_Type())
rcEtherSamPerformanceCurrentFLRb.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceCurrentFLRb.setStatus(_A)
class _RcEtherSamPerformanceMaxFLRb_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_RcEtherSamPerformanceMaxFLRb_Type.__name__=_E
_RcEtherSamPerformanceMaxFLRb_Object=MibTableColumn
rcEtherSamPerformanceMaxFLRb=_RcEtherSamPerformanceMaxFLRb_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,19),_RcEtherSamPerformanceMaxFLRb_Type())
rcEtherSamPerformanceMaxFLRb.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceMaxFLRb.setStatus(_A)
class _RcEtherSamPerformanceMinFLRb_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_RcEtherSamPerformanceMinFLRb_Type.__name__=_E
_RcEtherSamPerformanceMinFLRb_Object=MibTableColumn
rcEtherSamPerformanceMinFLRb=_RcEtherSamPerformanceMinFLRb_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,20),_RcEtherSamPerformanceMinFLRb_Type())
rcEtherSamPerformanceMinFLRb.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceMinFLRb.setStatus(_A)
class _RcEtherSamPerformanceAverageFLRb_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_RcEtherSamPerformanceAverageFLRb_Type.__name__=_E
_RcEtherSamPerformanceAverageFLRb_Object=MibTableColumn
rcEtherSamPerformanceAverageFLRb=_RcEtherSamPerformanceAverageFLRb_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,21),_RcEtherSamPerformanceAverageFLRb_Type())
rcEtherSamPerformanceAverageFLRb.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceAverageFLRb.setStatus(_A)
class _RcEtherSamPerformanceAvail_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_RcEtherSamPerformanceAvail_Type.__name__=_E
_RcEtherSamPerformanceAvail_Object=MibTableColumn
rcEtherSamPerformanceAvail=_RcEtherSamPerformanceAvail_Object((1,3,6,1,4,1,8886,6,1,74,2,4,1,22),_RcEtherSamPerformanceAvail_Type())
rcEtherSamPerformanceAvail.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamPerformanceAvail.setStatus(_A)
_RcEtherSamStatisticTable_Object=MibTable
rcEtherSamStatisticTable=_RcEtherSamStatisticTable_Object((1,3,6,1,4,1,8886,6,1,74,2,5))
if mibBuilder.loadTexts:rcEtherSamStatisticTable.setStatus(_A)
_RcEtherSamStatisticEntry_Object=MibTableRow
rcEtherSamStatisticEntry=_RcEtherSamStatisticEntry_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1))
rcEtherSamStatisticEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:rcEtherSamStatisticEntry.setStatus(_A)
_RcEtherSamStatisticDropEvents_Type=Counter32
_RcEtherSamStatisticDropEvents_Object=MibTableColumn
rcEtherSamStatisticDropEvents=_RcEtherSamStatisticDropEvents_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,1),_RcEtherSamStatisticDropEvents_Type())
rcEtherSamStatisticDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatisticDropEvents.setStatus(_A)
_RcEtherSamStatisticCRCAlignErrors_Type=Counter32
_RcEtherSamStatisticCRCAlignErrors_Object=MibTableColumn
rcEtherSamStatisticCRCAlignErrors=_RcEtherSamStatisticCRCAlignErrors_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,2),_RcEtherSamStatisticCRCAlignErrors_Type())
rcEtherSamStatisticCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatisticCRCAlignErrors.setStatus(_A)
_RcEtherSamStatisticUndersizePkts_Type=Counter32
_RcEtherSamStatisticUndersizePkts_Object=MibTableColumn
rcEtherSamStatisticUndersizePkts=_RcEtherSamStatisticUndersizePkts_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,3),_RcEtherSamStatisticUndersizePkts_Type())
rcEtherSamStatisticUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatisticUndersizePkts.setStatus(_A)
_RcEtherSamStatisticFragments_Type=Counter32
_RcEtherSamStatisticFragments_Object=MibTableColumn
rcEtherSamStatisticFragments=_RcEtherSamStatisticFragments_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,4),_RcEtherSamStatisticFragments_Type())
rcEtherSamStatisticFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatisticFragments.setStatus(_A)
_RcEtherSamStatisticJabbers_Type=Counter32
_RcEtherSamStatisticJabbers_Object=MibTableColumn
rcEtherSamStatisticJabbers=_RcEtherSamStatisticJabbers_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,5),_RcEtherSamStatisticJabbers_Type())
rcEtherSamStatisticJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatisticJabbers.setStatus(_A)
_RcEtherSamStatisticCollisions_Type=Counter32
_RcEtherSamStatisticCollisions_Object=MibTableColumn
rcEtherSamStatisticCollisions=_RcEtherSamStatisticCollisions_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,6),_RcEtherSamStatisticCollisions_Type())
rcEtherSamStatisticCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatisticCollisions.setStatus(_A)
_RcEtherSamStatisticInUnicast_Type=Counter64
_RcEtherSamStatisticInUnicast_Object=MibTableColumn
rcEtherSamStatisticInUnicast=_RcEtherSamStatisticInUnicast_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,7),_RcEtherSamStatisticInUnicast_Type())
rcEtherSamStatisticInUnicast.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatisticInUnicast.setStatus(_A)
_RcEtherSamStatisticInMulticast_Type=Counter64
_RcEtherSamStatisticInMulticast_Object=MibTableColumn
rcEtherSamStatisticInMulticast=_RcEtherSamStatisticInMulticast_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,8),_RcEtherSamStatisticInMulticast_Type())
rcEtherSamStatisticInMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatisticInMulticast.setStatus(_A)
_RcEtherSamStatisticInBroadcast_Type=Counter64
_RcEtherSamStatisticInBroadcast_Object=MibTableColumn
rcEtherSamStatisticInBroadcast=_RcEtherSamStatisticInBroadcast_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,9),_RcEtherSamStatisticInBroadcast_Type())
rcEtherSamStatisticInBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatisticInBroadcast.setStatus(_A)
_RcEtherSamStatisticOutUnicast_Type=Counter64
_RcEtherSamStatisticOutUnicast_Object=MibTableColumn
rcEtherSamStatisticOutUnicast=_RcEtherSamStatisticOutUnicast_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,10),_RcEtherSamStatisticOutUnicast_Type())
rcEtherSamStatisticOutUnicast.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatisticOutUnicast.setStatus(_A)
_RcEtherSamStatisticOutMulticast_Type=Counter64
_RcEtherSamStatisticOutMulticast_Object=MibTableColumn
rcEtherSamStatisticOutMulticast=_RcEtherSamStatisticOutMulticast_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,11),_RcEtherSamStatisticOutMulticast_Type())
rcEtherSamStatisticOutMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatisticOutMulticast.setStatus(_A)
_RcEtherSamStatisticOutBroadcast_Type=Counter64
_RcEtherSamStatisticOutBroadcast_Object=MibTableColumn
rcEtherSamStatisticOutBroadcast=_RcEtherSamStatisticOutBroadcast_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,12),_RcEtherSamStatisticOutBroadcast_Type())
rcEtherSamStatisticOutBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatisticOutBroadcast.setStatus(_A)
_RcEtherSamStatistic64to127octets_Type=Counter64
_RcEtherSamStatistic64to127octets_Object=MibTableColumn
rcEtherSamStatistic64to127octets=_RcEtherSamStatistic64to127octets_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,13),_RcEtherSamStatistic64to127octets_Type())
rcEtherSamStatistic64to127octets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatistic64to127octets.setStatus(_A)
_RcEtherSamStatistic128to255octets_Type=Counter64
_RcEtherSamStatistic128to255octets_Object=MibTableColumn
rcEtherSamStatistic128to255octets=_RcEtherSamStatistic128to255octets_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,14),_RcEtherSamStatistic128to255octets_Type())
rcEtherSamStatistic128to255octets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatistic128to255octets.setStatus(_A)
_RcEtherSamStatistic256to511octets_Type=Counter64
_RcEtherSamStatistic256to511octets_Object=MibTableColumn
rcEtherSamStatistic256to511octets=_RcEtherSamStatistic256to511octets_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,15),_RcEtherSamStatistic256to511octets_Type())
rcEtherSamStatistic256to511octets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatistic256to511octets.setStatus(_A)
_RcEtherSamStatistic512to1023octets_Type=Counter64
_RcEtherSamStatistic512to1023octets_Object=MibTableColumn
rcEtherSamStatistic512to1023octets=_RcEtherSamStatistic512to1023octets_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,16),_RcEtherSamStatistic512to1023octets_Type())
rcEtherSamStatistic512to1023octets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatistic512to1023octets.setStatus(_A)
_RcEtherSamStatistic1024to1518Octet_Type=Counter64
_RcEtherSamStatistic1024to1518Octet_Object=MibTableColumn
rcEtherSamStatistic1024to1518Octet=_RcEtherSamStatistic1024to1518Octet_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,17),_RcEtherSamStatistic1024to1518Octet_Type())
rcEtherSamStatistic1024to1518Octet.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatistic1024to1518Octet.setStatus(_A)
_RcEtherSamStatistic1519Octet_Type=Counter64
_RcEtherSamStatistic1519Octet_Object=MibTableColumn
rcEtherSamStatistic1519Octet=_RcEtherSamStatistic1519Octet_Object((1,3,6,1,4,1,8886,6,1,74,2,5,1,18),_RcEtherSamStatistic1519Octet_Type())
rcEtherSamStatistic1519Octet.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSamStatistic1519Octet.setStatus(_A)
_RcEtherSam2544ResultTable_Object=MibTable
rcEtherSam2544ResultTable=_RcEtherSam2544ResultTable_Object((1,3,6,1,4,1,8886,6,1,74,2,6))
if mibBuilder.loadTexts:rcEtherSam2544ResultTable.setStatus(_A)
_RcEtherSam2544ResultEntry_Object=MibTableRow
rcEtherSam2544ResultEntry=_RcEtherSam2544ResultEntry_Object((1,3,6,1,4,1,8886,6,1,74,2,6,1))
rcEtherSam2544ResultEntry.setIndexNames((0,_F,_G),(0,_F,_O))
if mibBuilder.loadTexts:rcEtherSam2544ResultEntry.setStatus(_A)
_RcEtherSam2544FrameSize_Type=Integer32
_RcEtherSam2544FrameSize_Object=MibTableColumn
rcEtherSam2544FrameSize=_RcEtherSam2544FrameSize_Object((1,3,6,1,4,1,8886,6,1,74,2,6,1,1),_RcEtherSam2544FrameSize_Type())
rcEtherSam2544FrameSize.setMaxAccess(_H)
if mibBuilder.loadTexts:rcEtherSam2544FrameSize.setStatus(_A)
_RcEtherSam2544Rate_Type=Integer32
_RcEtherSam2544Rate_Object=MibTableColumn
rcEtherSam2544Rate=_RcEtherSam2544Rate_Object((1,3,6,1,4,1,8886,6,1,74,2,6,1,2),_RcEtherSam2544Rate_Type())
rcEtherSam2544Rate.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSam2544Rate.setStatus(_A)
_RcEtherSam2544BER_Type=Integer32
_RcEtherSam2544BER_Object=MibTableColumn
rcEtherSam2544BER=_RcEtherSam2544BER_Object((1,3,6,1,4,1,8886,6,1,74,2,6,1,3),_RcEtherSam2544BER_Type())
rcEtherSam2544BER.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSam2544BER.setStatus(_A)
_RcEtherSam2544FD_Type=Integer32
_RcEtherSam2544FD_Object=MibTableColumn
rcEtherSam2544FD=_RcEtherSam2544FD_Object((1,3,6,1,4,1,8886,6,1,74,2,6,1,4),_RcEtherSam2544FD_Type())
rcEtherSam2544FD.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSam2544FD.setStatus(_A)
_RcEtherSam2544FDV_Type=Integer32
_RcEtherSam2544FDV_Object=MibTableColumn
rcEtherSam2544FDV=_RcEtherSam2544FDV_Object((1,3,6,1,4,1,8886,6,1,74,2,6,1,5),_RcEtherSam2544FDV_Type())
rcEtherSam2544FDV.setMaxAccess(_B)
if mibBuilder.loadTexts:rcEtherSam2544FDV.setStatus(_A)
_RcEtherSamFlowFrameLengthTable_Object=MibTable
rcEtherSamFlowFrameLengthTable=_RcEtherSamFlowFrameLengthTable_Object((1,3,6,1,4,1,8886,6,1,74,2,7))
if mibBuilder.loadTexts:rcEtherSamFlowFrameLengthTable.setStatus(_A)
_RcEtherSamFlowFrameLengthEntry_Object=MibTableRow
rcEtherSamFlowFrameLengthEntry=_RcEtherSamFlowFrameLengthEntry_Object((1,3,6,1,4,1,8886,6,1,74,2,7,1))
rcEtherSamFlowFrameLengthEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:rcEtherSamFlowFrameLengthEntry.setStatus(_A)
class _RcEtherSamFlowFrameNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_RcEtherSamFlowFrameNum_Type.__name__=_D
_RcEtherSamFlowFrameNum_Object=MibTableColumn
rcEtherSamFlowFrameNum=_RcEtherSamFlowFrameNum_Object((1,3,6,1,4,1,8886,6,1,74,2,7,1,1),_RcEtherSamFlowFrameNum_Type())
rcEtherSamFlowFrameNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowFrameNum.setStatus(_A)
class _RcEtherSamFlowFrame1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,12288))
_RcEtherSamFlowFrame1_Type.__name__=_D
_RcEtherSamFlowFrame1_Object=MibTableColumn
rcEtherSamFlowFrame1=_RcEtherSamFlowFrame1_Object((1,3,6,1,4,1,8886,6,1,74,2,7,1,2),_RcEtherSamFlowFrame1_Type())
rcEtherSamFlowFrame1.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowFrame1.setStatus(_A)
class _RcEtherSamFlowFrame2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,12288))
_RcEtherSamFlowFrame2_Type.__name__=_D
_RcEtherSamFlowFrame2_Object=MibTableColumn
rcEtherSamFlowFrame2=_RcEtherSamFlowFrame2_Object((1,3,6,1,4,1,8886,6,1,74,2,7,1,3),_RcEtherSamFlowFrame2_Type())
rcEtherSamFlowFrame2.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowFrame2.setStatus(_A)
class _RcEtherSamFlowFrame3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,12288))
_RcEtherSamFlowFrame3_Type.__name__=_D
_RcEtherSamFlowFrame3_Object=MibTableColumn
rcEtherSamFlowFrame3=_RcEtherSamFlowFrame3_Object((1,3,6,1,4,1,8886,6,1,74,2,7,1,4),_RcEtherSamFlowFrame3_Type())
rcEtherSamFlowFrame3.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowFrame3.setStatus(_A)
class _RcEtherSamFlowFrame4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,12288))
_RcEtherSamFlowFrame4_Type.__name__=_D
_RcEtherSamFlowFrame4_Object=MibTableColumn
rcEtherSamFlowFrame4=_RcEtherSamFlowFrame4_Object((1,3,6,1,4,1,8886,6,1,74,2,7,1,5),_RcEtherSamFlowFrame4_Type())
rcEtherSamFlowFrame4.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowFrame4.setStatus(_A)
class _RcEtherSamFlowFrame5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,12288))
_RcEtherSamFlowFrame5_Type.__name__=_D
_RcEtherSamFlowFrame5_Object=MibTableColumn
rcEtherSamFlowFrame5=_RcEtherSamFlowFrame5_Object((1,3,6,1,4,1,8886,6,1,74,2,7,1,6),_RcEtherSamFlowFrame5_Type())
rcEtherSamFlowFrame5.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowFrame5.setStatus(_A)
class _RcEtherSamFlowFrame6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,12288))
_RcEtherSamFlowFrame6_Type.__name__=_D
_RcEtherSamFlowFrame6_Object=MibTableColumn
rcEtherSamFlowFrame6=_RcEtherSamFlowFrame6_Object((1,3,6,1,4,1,8886,6,1,74,2,7,1,7),_RcEtherSamFlowFrame6_Type())
rcEtherSamFlowFrame6.setMaxAccess(_C)
if mibBuilder.loadTexts:rcEtherSamFlowFrame6.setStatus(_A)
_RcEtherSamTestTrapGroup_ObjectIdentity=ObjectIdentity
rcEtherSamTestTrapGroup=_RcEtherSamTestTrapGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,74,3))
rcEtherSamServiceTestFailTrap=NotificationType((1,3,6,1,4,1,8886,6,1,74,3,1))
rcEtherSamServiceTestFailTrap.setObjects((_F,_G))
if mibBuilder.loadTexts:rcEtherSamServiceTestFailTrap.setStatus(_A)
rcEtherSamServiceFinishTrap=NotificationType((1,3,6,1,4,1,8886,6,1,74,3,2))
rcEtherSamServiceFinishTrap.setObjects((_F,_P))
if mibBuilder.loadTexts:rcEtherSamServiceFinishTrap.setStatus(_A)
rcEtherSam2544FinishTrap=NotificationType((1,3,6,1,4,1,8886,6,1,74,3,3))
rcEtherSam2544FinishTrap.setObjects((_F,_Q))
if mibBuilder.loadTexts:rcEtherSam2544FinishTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'rcEtherSam':rcEtherSam,'rcEtherSamGlobalGroup':rcEtherSamGlobalGroup,_Q:rcEtherSamServiceList,'rcEtherSamServiceTestType':rcEtherSamServiceTestType,'rcEtherSamServiceTestOperate':rcEtherSamServiceTestOperate,'rcEtherSamPerformanceDuration':rcEtherSamPerformanceDuration,'rcEtherSamTestElapsedTime':rcEtherSamTestElapsedTime,_P:rcEtherSamServiceTestResult,'rcEtherSamTestGroup':rcEtherSamTestGroup,'rcEtherSamFlowTable':rcEtherSamFlowTable,'rcEtherSamFlowEntry':rcEtherSamFlowEntry,_L:rcEtherSamFlowIndex,'rcEtherSamFlowFrameType':rcEtherSamFlowFrameType,'rcEtherSamFlowFrameEtherType':rcEtherSamFlowFrameEtherType,'rcEtherSamFlowFrameLengthType':rcEtherSamFlowFrameLengthType,'rcEtherSamFlowFrameSize':rcEtherSamFlowFrameSize,'rcEtherSamFlowFrameCvlan':rcEtherSamFlowFrameCvlan,'rcEtherSamFlowFrameCos':rcEtherSamFlowFrameCos,'rcEtherSamFlowRowStatus':rcEtherSamFlowRowStatus,'rcEtherSamFlowDescription':rcEtherSamFlowDescription,'rcEtherSamFlowDestAddr':rcEtherSamFlowDestAddr,'rcEtherSamFlowDscp':rcEtherSamFlowDscp,'rcEtherSamFlowDatePattern':rcEtherSamFlowDatePattern,'rcEtherSamFlowSourcePort':rcEtherSamFlowSourcePort,'rcEtherSamFlowDestPort':rcEtherSamFlowDestPort,'rcEtherSamFlowNextHopMac':rcEtherSamFlowNextHopMac,'rcEtherSamServiceTable':rcEtherSamServiceTable,'rcEtherSamServiceEntry':rcEtherSamServiceEntry,_G:rcEtherSamServiceIndex,'rcEtherSamServiceName':rcEtherSamServiceName,'rcEtherSamServiceProfileNum':rcEtherSamServiceProfileNum,'rcEtherSamServiceSvlan':rcEtherSamServiceSvlan,'rcEtherSamServiceCos':rcEtherSamServiceCos,'rcEtherSamServiceUNI':rcEtherSamServiceUNI,'rcEtherSamServiceNNI':rcEtherSamServiceNNI,'rcEtherSamServiceCir':rcEtherSamServiceCir,'rcEtherSamServiceEir':rcEtherSamServiceEir,'rcEtherSamServiceMDL':rcEtherSamServiceMDL,'rcEtherSamServiceDMAC':rcEtherSamServiceDMAC,'rcEtherSamServiceThresholdAvail':rcEtherSamServiceThresholdAvail,'rcEtherSamServiceThresholdFD':rcEtherSamServiceThresholdFD,'rcEtherSamServiceThresholdFDV':rcEtherSamServiceThresholdFDV,'rcEtherSamServiceThresholdFLR':rcEtherSamServiceThresholdFLR,'rcEtherSamServiceBandWidth':rcEtherSamServiceBandWidth,'rcEtherSamServiceRowStatus':rcEtherSamServiceRowStatus,'rcEtherSamServiceSecondNNI':rcEtherSamServiceSecondNNI,'rcEtherSamServiceCfgBypassUniEnable':rcEtherSamServiceCfgBypassUniEnable,'rcEtherSamServiceDIPAddressType':rcEtherSamServiceDIPAddressType,'rcEtherSamServiceDIPAddress':rcEtherSamServiceDIPAddress,'rcEtherSamCfgResultTable':rcEtherSamCfgResultTable,'rcEtherSamCfgResultEntry':rcEtherSamCfgResultEntry,_N:rcEtherSamCfgStepNum,'rcEtherSamCfgResult':rcEtherSamCfgResult,'rcEtherSamCfgReceiveIR':rcEtherSamCfgReceiveIR,'rcEtherSamCfgFD':rcEtherSamCfgFD,'rcEtherSamCfgFDV':rcEtherSamCfgFDV,'rcEtherSamCfgFLRf':rcEtherSamCfgFLRf,'rcEtherSamCfgFLRb':rcEtherSamCfgFLRb,'rcEtherSamPerformanceResultTable':rcEtherSamPerformanceResultTable,'rcEtherSamPerformanceResultEntry':rcEtherSamPerformanceResultEntry,'rcEtherSamPerformanceResult':rcEtherSamPerformanceResult,'rcEtherSamPerformanceCurrentReceiveIR':rcEtherSamPerformanceCurrentReceiveIR,'rcEtherSamPerformanceMaxReceiveIR':rcEtherSamPerformanceMaxReceiveIR,'rcEtherSamPerformanceMinReceiveIR':rcEtherSamPerformanceMinReceiveIR,'rcEtherSamPerformanceAverageReceiveIR':rcEtherSamPerformanceAverageReceiveIR,'rcEtherSamPerformanceCurrentFD':rcEtherSamPerformanceCurrentFD,'rcEtherSamPerformanceMaxFD':rcEtherSamPerformanceMaxFD,'rcEtherSamPerformanceMinFD':rcEtherSamPerformanceMinFD,'rcEtherSamPerformanceAverageFD':rcEtherSamPerformanceAverageFD,'rcEtherSamPerformanceCurrentFDV':rcEtherSamPerformanceCurrentFDV,'rcEtherSamPerformanceMaxFDV':rcEtherSamPerformanceMaxFDV,'rcEtherSamPerformanceMinFDV':rcEtherSamPerformanceMinFDV,'rcEtherSamPerformanceAverageFDV':rcEtherSamPerformanceAverageFDV,'rcEtherSamPerformanceCurrentFLRf':rcEtherSamPerformanceCurrentFLRf,'rcEtherSamPerformanceMaxFLRf':rcEtherSamPerformanceMaxFLRf,'rcEtherSamPerformanceMinFLRf':rcEtherSamPerformanceMinFLRf,'rcEtherSamPerformanceAverageFLRf':rcEtherSamPerformanceAverageFLRf,'rcEtherSamPerformanceCurrentFLRb':rcEtherSamPerformanceCurrentFLRb,'rcEtherSamPerformanceMaxFLRb':rcEtherSamPerformanceMaxFLRb,'rcEtherSamPerformanceMinFLRb':rcEtherSamPerformanceMinFLRb,'rcEtherSamPerformanceAverageFLRb':rcEtherSamPerformanceAverageFLRb,'rcEtherSamPerformanceAvail':rcEtherSamPerformanceAvail,'rcEtherSamStatisticTable':rcEtherSamStatisticTable,'rcEtherSamStatisticEntry':rcEtherSamStatisticEntry,'rcEtherSamStatisticDropEvents':rcEtherSamStatisticDropEvents,'rcEtherSamStatisticCRCAlignErrors':rcEtherSamStatisticCRCAlignErrors,'rcEtherSamStatisticUndersizePkts':rcEtherSamStatisticUndersizePkts,'rcEtherSamStatisticFragments':rcEtherSamStatisticFragments,'rcEtherSamStatisticJabbers':rcEtherSamStatisticJabbers,'rcEtherSamStatisticCollisions':rcEtherSamStatisticCollisions,'rcEtherSamStatisticInUnicast':rcEtherSamStatisticInUnicast,'rcEtherSamStatisticInMulticast':rcEtherSamStatisticInMulticast,'rcEtherSamStatisticInBroadcast':rcEtherSamStatisticInBroadcast,'rcEtherSamStatisticOutUnicast':rcEtherSamStatisticOutUnicast,'rcEtherSamStatisticOutMulticast':rcEtherSamStatisticOutMulticast,'rcEtherSamStatisticOutBroadcast':rcEtherSamStatisticOutBroadcast,'rcEtherSamStatistic64to127octets':rcEtherSamStatistic64to127octets,'rcEtherSamStatistic128to255octets':rcEtherSamStatistic128to255octets,'rcEtherSamStatistic256to511octets':rcEtherSamStatistic256to511octets,'rcEtherSamStatistic512to1023octets':rcEtherSamStatistic512to1023octets,'rcEtherSamStatistic1024to1518Octet':rcEtherSamStatistic1024to1518Octet,'rcEtherSamStatistic1519Octet':rcEtherSamStatistic1519Octet,'rcEtherSam2544ResultTable':rcEtherSam2544ResultTable,'rcEtherSam2544ResultEntry':rcEtherSam2544ResultEntry,_O:rcEtherSam2544FrameSize,'rcEtherSam2544Rate':rcEtherSam2544Rate,'rcEtherSam2544BER':rcEtherSam2544BER,'rcEtherSam2544FD':rcEtherSam2544FD,'rcEtherSam2544FDV':rcEtherSam2544FDV,'rcEtherSamFlowFrameLengthTable':rcEtherSamFlowFrameLengthTable,'rcEtherSamFlowFrameLengthEntry':rcEtherSamFlowFrameLengthEntry,'rcEtherSamFlowFrameNum':rcEtherSamFlowFrameNum,'rcEtherSamFlowFrame1':rcEtherSamFlowFrame1,'rcEtherSamFlowFrame2':rcEtherSamFlowFrame2,'rcEtherSamFlowFrame3':rcEtherSamFlowFrame3,'rcEtherSamFlowFrame4':rcEtherSamFlowFrame4,'rcEtherSamFlowFrame5':rcEtherSamFlowFrame5,'rcEtherSamFlowFrame6':rcEtherSamFlowFrame6,'rcEtherSamTestTrapGroup':rcEtherSamTestTrapGroup,'rcEtherSamServiceTestFailTrap':rcEtherSamServiceTestFailTrap,'rcEtherSamServiceFinishTrap':rcEtherSamServiceFinishTrap,'rcEtherSam2544FinishTrap':rcEtherSam2544FinishTrap})