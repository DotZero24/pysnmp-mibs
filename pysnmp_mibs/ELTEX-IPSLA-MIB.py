_M='eltexIpSlaStatsUdpJitterIndex'
_L='eltexIpSlaStatsIcmpEchoIndex'
_K='eltexIpSlaAdminUdpJitterIndex'
_J='eltexIpSlaAdminIcmpEchoIndex'
_I='eltexIpSlaAdminCtrlIndex'
_H='InterfaceIndexOrZero'
_G='DisplayString'
_F='ELTEX-IPSLA-MIB'
_E='Integer32'
_D='read-write'
_C='milliseconds'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
eltexIpSlaMIB=ModuleIdentity((1,3,6,1,4,1,35265,32))
class EltexIpSlaOperationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('icmp-echo',1),('udp-jitter',2)))
class EltexIpSlaOperationStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
class EltexIpSlaStatsOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknown',0),('ok',1),('failed',2)))
_EltexIpSlaObjects_ObjectIdentity=ObjectIdentity
eltexIpSlaObjects=_EltexIpSlaObjects_ObjectIdentity((1,3,6,1,4,1,35265,32,1))
_EltexIpSlaAppl_ObjectIdentity=ObjectIdentity
eltexIpSlaAppl=_EltexIpSlaAppl_ObjectIdentity((1,3,6,1,4,1,35265,32,1,1))
_EltexIpSlaApplResponder_ObjectIdentity=ObjectIdentity
eltexIpSlaApplResponder=_EltexIpSlaApplResponder_ObjectIdentity((1,3,6,1,4,1,35265,32,1,1,13))
class _EltexIpSlaApplResponderUdpJitterPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexIpSlaApplResponderUdpJitterPort_Type.__name__=_E
_EltexIpSlaApplResponderUdpJitterPort_Object=MibScalar
eltexIpSlaApplResponderUdpJitterPort=_EltexIpSlaApplResponderUdpJitterPort_Object((1,3,6,1,4,1,35265,32,1,1,13,1),_EltexIpSlaApplResponderUdpJitterPort_Type())
eltexIpSlaApplResponderUdpJitterPort.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaApplResponderUdpJitterPort.setStatus(_A)
_EltexIpSlaAdmin_ObjectIdentity=ObjectIdentity
eltexIpSlaAdmin=_EltexIpSlaAdmin_ObjectIdentity((1,3,6,1,4,1,35265,32,1,2))
_EltexIpSlaAdminCtrlTable_Object=MibTable
eltexIpSlaAdminCtrlTable=_EltexIpSlaAdminCtrlTable_Object((1,3,6,1,4,1,35265,32,1,2,1))
if mibBuilder.loadTexts:eltexIpSlaAdminCtrlTable.setStatus(_A)
_EltexIpSlaAdminCtrlEntry_Object=MibTableRow
eltexIpSlaAdminCtrlEntry=_EltexIpSlaAdminCtrlEntry_Object((1,3,6,1,4,1,35265,32,1,2,1,1))
eltexIpSlaAdminCtrlEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:eltexIpSlaAdminCtrlEntry.setStatus(_A)
_EltexIpSlaAdminCtrlIndex_Type=Integer32
_EltexIpSlaAdminCtrlIndex_Object=MibTableColumn
eltexIpSlaAdminCtrlIndex=_EltexIpSlaAdminCtrlIndex_Object((1,3,6,1,4,1,35265,32,1,2,1,1,1),_EltexIpSlaAdminCtrlIndex_Type())
eltexIpSlaAdminCtrlIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminCtrlIndex.setStatus(_A)
_EltexIpSlaAdminCtrlType_Type=EltexIpSlaOperationType
_EltexIpSlaAdminCtrlType_Object=MibTableColumn
eltexIpSlaAdminCtrlType=_EltexIpSlaAdminCtrlType_Object((1,3,6,1,4,1,35265,32,1,2,1,1,2),_EltexIpSlaAdminCtrlType_Type())
eltexIpSlaAdminCtrlType.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminCtrlType.setStatus(_A)
_EltexIpSlaAdminCtrlStatus_Type=EltexIpSlaOperationStatus
_EltexIpSlaAdminCtrlStatus_Object=MibTableColumn
eltexIpSlaAdminCtrlStatus=_EltexIpSlaAdminCtrlStatus_Object((1,3,6,1,4,1,35265,32,1,2,1,1,3),_EltexIpSlaAdminCtrlStatus_Type())
eltexIpSlaAdminCtrlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaAdminCtrlStatus.setStatus(_A)
class _EltexIpSlaAdminCtrlFrequency_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_EltexIpSlaAdminCtrlFrequency_Type.__name__=_E
_EltexIpSlaAdminCtrlFrequency_Object=MibTableColumn
eltexIpSlaAdminCtrlFrequency=_EltexIpSlaAdminCtrlFrequency_Object((1,3,6,1,4,1,35265,32,1,2,1,1,4),_EltexIpSlaAdminCtrlFrequency_Type())
eltexIpSlaAdminCtrlFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminCtrlFrequency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaAdminCtrlFrequency.setUnits('seconds')
class _EltexIpSlaAdminCtrlTag_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltexIpSlaAdminCtrlTag_Type.__name__=_G
_EltexIpSlaAdminCtrlTag_Object=MibTableColumn
eltexIpSlaAdminCtrlTag=_EltexIpSlaAdminCtrlTag_Object((1,3,6,1,4,1,35265,32,1,2,1,1,5),_EltexIpSlaAdminCtrlTag_Type())
eltexIpSlaAdminCtrlTag.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminCtrlTag.setStatus(_A)
class _EltexIpSlaAdminCtrlOwner_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EltexIpSlaAdminCtrlOwner_Type.__name__=_G
_EltexIpSlaAdminCtrlOwner_Object=MibTableColumn
eltexIpSlaAdminCtrlOwner=_EltexIpSlaAdminCtrlOwner_Object((1,3,6,1,4,1,35265,32,1,2,1,1,6),_EltexIpSlaAdminCtrlOwner_Type())
eltexIpSlaAdminCtrlOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminCtrlOwner.setStatus(_A)
_EltexIpSlaAdminCtrlRowStatus_Type=RowStatus
_EltexIpSlaAdminCtrlRowStatus_Object=MibTableColumn
eltexIpSlaAdminCtrlRowStatus=_EltexIpSlaAdminCtrlRowStatus_Object((1,3,6,1,4,1,35265,32,1,2,1,1,7),_EltexIpSlaAdminCtrlRowStatus_Type())
eltexIpSlaAdminCtrlRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminCtrlRowStatus.setStatus(_A)
_EltexIpSlaAdminIcmpEchoTable_Object=MibTable
eltexIpSlaAdminIcmpEchoTable=_EltexIpSlaAdminIcmpEchoTable_Object((1,3,6,1,4,1,35265,32,1,2,2))
if mibBuilder.loadTexts:eltexIpSlaAdminIcmpEchoTable.setStatus(_A)
_EltexIpSlaAdminIcmpEchoEntry_Object=MibTableRow
eltexIpSlaAdminIcmpEchoEntry=_EltexIpSlaAdminIcmpEchoEntry_Object((1,3,6,1,4,1,35265,32,1,2,2,1))
eltexIpSlaAdminIcmpEchoEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:eltexIpSlaAdminIcmpEchoEntry.setStatus(_A)
_EltexIpSlaAdminIcmpEchoIndex_Type=Integer32
_EltexIpSlaAdminIcmpEchoIndex_Object=MibTableColumn
eltexIpSlaAdminIcmpEchoIndex=_EltexIpSlaAdminIcmpEchoIndex_Object((1,3,6,1,4,1,35265,32,1,2,2,1,1),_EltexIpSlaAdminIcmpEchoIndex_Type())
eltexIpSlaAdminIcmpEchoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminIcmpEchoIndex.setStatus(_A)
_EltexIpSlaAdminIcmpEchoTargetAddress_Type=IpAddress
_EltexIpSlaAdminIcmpEchoTargetAddress_Object=MibTableColumn
eltexIpSlaAdminIcmpEchoTargetAddress=_EltexIpSlaAdminIcmpEchoTargetAddress_Object((1,3,6,1,4,1,35265,32,1,2,2,1,2),_EltexIpSlaAdminIcmpEchoTargetAddress_Type())
eltexIpSlaAdminIcmpEchoTargetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminIcmpEchoTargetAddress.setStatus(_A)
_EltexIpSlaAdminIcmpEchoSourceAddress_Type=IpAddress
_EltexIpSlaAdminIcmpEchoSourceAddress_Object=MibTableColumn
eltexIpSlaAdminIcmpEchoSourceAddress=_EltexIpSlaAdminIcmpEchoSourceAddress_Object((1,3,6,1,4,1,35265,32,1,2,2,1,3),_EltexIpSlaAdminIcmpEchoSourceAddress_Type())
eltexIpSlaAdminIcmpEchoSourceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminIcmpEchoSourceAddress.setStatus(_A)
_EltexIpSlaAdminIcmpEchoSourceInterface_Type=InterfaceIndexOrZero
_EltexIpSlaAdminIcmpEchoSourceInterface_Object=MibTableColumn
eltexIpSlaAdminIcmpEchoSourceInterface=_EltexIpSlaAdminIcmpEchoSourceInterface_Object((1,3,6,1,4,1,35265,32,1,2,2,1,4),_EltexIpSlaAdminIcmpEchoSourceInterface_Type())
eltexIpSlaAdminIcmpEchoSourceInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminIcmpEchoSourceInterface.setStatus(_A)
class _EltexIpSlaAdminIcmpEchoTimeOut_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_EltexIpSlaAdminIcmpEchoTimeOut_Type.__name__=_E
_EltexIpSlaAdminIcmpEchoTimeOut_Object=MibTableColumn
eltexIpSlaAdminIcmpEchoTimeOut=_EltexIpSlaAdminIcmpEchoTimeOut_Object((1,3,6,1,4,1,35265,32,1,2,2,1,5),_EltexIpSlaAdminIcmpEchoTimeOut_Type())
eltexIpSlaAdminIcmpEchoTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminIcmpEchoTimeOut.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaAdminIcmpEchoTimeOut.setUnits(_C)
class _EltexIpSlaAdminIcmpEchoReqDataSize_Type(Integer32):defaultValue=56;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1432))
_EltexIpSlaAdminIcmpEchoReqDataSize_Type.__name__=_E
_EltexIpSlaAdminIcmpEchoReqDataSize_Object=MibTableColumn
eltexIpSlaAdminIcmpEchoReqDataSize=_EltexIpSlaAdminIcmpEchoReqDataSize_Object((1,3,6,1,4,1,35265,32,1,2,2,1,6),_EltexIpSlaAdminIcmpEchoReqDataSize_Type())
eltexIpSlaAdminIcmpEchoReqDataSize.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminIcmpEchoReqDataSize.setStatus(_A)
class _EltexIpSlaAdminIcmpEchoTOS_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EltexIpSlaAdminIcmpEchoTOS_Type.__name__=_E
_EltexIpSlaAdminIcmpEchoTOS_Object=MibTableColumn
eltexIpSlaAdminIcmpEchoTOS=_EltexIpSlaAdminIcmpEchoTOS_Object((1,3,6,1,4,1,35265,32,1,2,2,1,7),_EltexIpSlaAdminIcmpEchoTOS_Type())
eltexIpSlaAdminIcmpEchoTOS.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminIcmpEchoTOS.setStatus(_A)
_EltexIpSlaAdminIcmpEchoRowStatus_Type=RowStatus
_EltexIpSlaAdminIcmpEchoRowStatus_Object=MibTableColumn
eltexIpSlaAdminIcmpEchoRowStatus=_EltexIpSlaAdminIcmpEchoRowStatus_Object((1,3,6,1,4,1,35265,32,1,2,2,1,8),_EltexIpSlaAdminIcmpEchoRowStatus_Type())
eltexIpSlaAdminIcmpEchoRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminIcmpEchoRowStatus.setStatus(_A)
_EltexIpSlaAdminUdpJitterTable_Object=MibTable
eltexIpSlaAdminUdpJitterTable=_EltexIpSlaAdminUdpJitterTable_Object((1,3,6,1,4,1,35265,32,1,2,3))
if mibBuilder.loadTexts:eltexIpSlaAdminUdpJitterTable.setStatus(_A)
_EltexIpSlaAdminUdpJitterEntry_Object=MibTableRow
eltexIpSlaAdminUdpJitterEntry=_EltexIpSlaAdminUdpJitterEntry_Object((1,3,6,1,4,1,35265,32,1,2,3,1))
eltexIpSlaAdminUdpJitterEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:eltexIpSlaAdminUdpJitterEntry.setStatus(_A)
_EltexIpSlaAdminUdpJitterIndex_Type=Integer32
_EltexIpSlaAdminUdpJitterIndex_Object=MibTableColumn
eltexIpSlaAdminUdpJitterIndex=_EltexIpSlaAdminUdpJitterIndex_Object((1,3,6,1,4,1,35265,32,1,2,3,1,1),_EltexIpSlaAdminUdpJitterIndex_Type())
eltexIpSlaAdminUdpJitterIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminUdpJitterIndex.setStatus(_A)
_EltexIpSlaAdminUdpJitterTargetAddress_Type=IpAddress
_EltexIpSlaAdminUdpJitterTargetAddress_Object=MibTableColumn
eltexIpSlaAdminUdpJitterTargetAddress=_EltexIpSlaAdminUdpJitterTargetAddress_Object((1,3,6,1,4,1,35265,32,1,2,3,1,2),_EltexIpSlaAdminUdpJitterTargetAddress_Type())
eltexIpSlaAdminUdpJitterTargetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminUdpJitterTargetAddress.setStatus(_A)
class _EltexIpSlaAdminUdpJitterTargetPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexIpSlaAdminUdpJitterTargetPort_Type.__name__=_E
_EltexIpSlaAdminUdpJitterTargetPort_Object=MibTableColumn
eltexIpSlaAdminUdpJitterTargetPort=_EltexIpSlaAdminUdpJitterTargetPort_Object((1,3,6,1,4,1,35265,32,1,2,3,1,3),_EltexIpSlaAdminUdpJitterTargetPort_Type())
eltexIpSlaAdminUdpJitterTargetPort.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminUdpJitterTargetPort.setStatus(_A)
_EltexIpSlaAdminUdpJitterSourceAddress_Type=IpAddress
_EltexIpSlaAdminUdpJitterSourceAddress_Object=MibTableColumn
eltexIpSlaAdminUdpJitterSourceAddress=_EltexIpSlaAdminUdpJitterSourceAddress_Object((1,3,6,1,4,1,35265,32,1,2,3,1,4),_EltexIpSlaAdminUdpJitterSourceAddress_Type())
eltexIpSlaAdminUdpJitterSourceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminUdpJitterSourceAddress.setStatus(_A)
class _EltexIpSlaAdminUdpJitterSourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexIpSlaAdminUdpJitterSourcePort_Type.__name__=_E
_EltexIpSlaAdminUdpJitterSourcePort_Object=MibTableColumn
eltexIpSlaAdminUdpJitterSourcePort=_EltexIpSlaAdminUdpJitterSourcePort_Object((1,3,6,1,4,1,35265,32,1,2,3,1,5),_EltexIpSlaAdminUdpJitterSourcePort_Type())
eltexIpSlaAdminUdpJitterSourcePort.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminUdpJitterSourcePort.setStatus(_A)
class _EltexIpSlaAdminUdpJitterSourceInterface_Type(InterfaceIndexOrZero):defaultValue=0
_EltexIpSlaAdminUdpJitterSourceInterface_Type.__name__=_H
_EltexIpSlaAdminUdpJitterSourceInterface_Object=MibTableColumn
eltexIpSlaAdminUdpJitterSourceInterface=_EltexIpSlaAdminUdpJitterSourceInterface_Object((1,3,6,1,4,1,35265,32,1,2,3,1,6),_EltexIpSlaAdminUdpJitterSourceInterface_Type())
eltexIpSlaAdminUdpJitterSourceInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminUdpJitterSourceInterface.setStatus(_A)
class _EltexIpSlaAdminUdpJitterInterval_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000))
_EltexIpSlaAdminUdpJitterInterval_Type.__name__=_E
_EltexIpSlaAdminUdpJitterInterval_Object=MibTableColumn
eltexIpSlaAdminUdpJitterInterval=_EltexIpSlaAdminUdpJitterInterval_Object((1,3,6,1,4,1,35265,32,1,2,3,1,7),_EltexIpSlaAdminUdpJitterInterval_Type())
eltexIpSlaAdminUdpJitterInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminUdpJitterInterval.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaAdminUdpJitterInterval.setUnits(_C)
class _EltexIpSlaAdminUdpJitterNumPackets_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_EltexIpSlaAdminUdpJitterNumPackets_Type.__name__=_E
_EltexIpSlaAdminUdpJitterNumPackets_Object=MibTableColumn
eltexIpSlaAdminUdpJitterNumPackets=_EltexIpSlaAdminUdpJitterNumPackets_Object((1,3,6,1,4,1,35265,32,1,2,3,1,8),_EltexIpSlaAdminUdpJitterNumPackets_Type())
eltexIpSlaAdminUdpJitterNumPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminUdpJitterNumPackets.setStatus(_A)
class _EltexIpSlaAdminUdpJitterTimeOut_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_EltexIpSlaAdminUdpJitterTimeOut_Type.__name__=_E
_EltexIpSlaAdminUdpJitterTimeOut_Object=MibTableColumn
eltexIpSlaAdminUdpJitterTimeOut=_EltexIpSlaAdminUdpJitterTimeOut_Object((1,3,6,1,4,1,35265,32,1,2,3,1,9),_EltexIpSlaAdminUdpJitterTimeOut_Type())
eltexIpSlaAdminUdpJitterTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminUdpJitterTimeOut.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaAdminUdpJitterTimeOut.setUnits(_C)
class _EltexIpSlaAdminUdpJitterReqDataSize_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1432))
_EltexIpSlaAdminUdpJitterReqDataSize_Type.__name__=_E
_EltexIpSlaAdminUdpJitterReqDataSize_Object=MibTableColumn
eltexIpSlaAdminUdpJitterReqDataSize=_EltexIpSlaAdminUdpJitterReqDataSize_Object((1,3,6,1,4,1,35265,32,1,2,3,1,10),_EltexIpSlaAdminUdpJitterReqDataSize_Type())
eltexIpSlaAdminUdpJitterReqDataSize.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminUdpJitterReqDataSize.setStatus(_A)
class _EltexIpSlaAdminUdpJitterTOS_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EltexIpSlaAdminUdpJitterTOS_Type.__name__=_E
_EltexIpSlaAdminUdpJitterTOS_Object=MibTableColumn
eltexIpSlaAdminUdpJitterTOS=_EltexIpSlaAdminUdpJitterTOS_Object((1,3,6,1,4,1,35265,32,1,2,3,1,11),_EltexIpSlaAdminUdpJitterTOS_Type())
eltexIpSlaAdminUdpJitterTOS.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminUdpJitterTOS.setStatus(_A)
_EltexIpSlaAdminUdpJitterRowStatus_Type=RowStatus
_EltexIpSlaAdminUdpJitterRowStatus_Object=MibTableColumn
eltexIpSlaAdminUdpJitterRowStatus=_EltexIpSlaAdminUdpJitterRowStatus_Object((1,3,6,1,4,1,35265,32,1,2,3,1,12),_EltexIpSlaAdminUdpJitterRowStatus_Type())
eltexIpSlaAdminUdpJitterRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaAdminUdpJitterRowStatus.setStatus(_A)
_EltexIpSlaStats_ObjectIdentity=ObjectIdentity
eltexIpSlaStats=_EltexIpSlaStats_ObjectIdentity((1,3,6,1,4,1,35265,32,1,3))
_EltexIpSlaStatsIcmpEchoTable_Object=MibTable
eltexIpSlaStatsIcmpEchoTable=_EltexIpSlaStatsIcmpEchoTable_Object((1,3,6,1,4,1,35265,32,1,3,2))
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoTable.setStatus(_A)
_EltexIpSlaStatsIcmpEchoEntry_Object=MibTableRow
eltexIpSlaStatsIcmpEchoEntry=_EltexIpSlaStatsIcmpEchoEntry_Object((1,3,6,1,4,1,35265,32,1,3,2,1))
eltexIpSlaStatsIcmpEchoEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoEntry.setStatus(_A)
_EltexIpSlaStatsIcmpEchoIndex_Type=Integer32
_EltexIpSlaStatsIcmpEchoIndex_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoIndex=_EltexIpSlaStatsIcmpEchoIndex_Object((1,3,6,1,4,1,35265,32,1,3,2,1,1),_EltexIpSlaStatsIcmpEchoIndex_Type())
eltexIpSlaStatsIcmpEchoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoIndex.setStatus(_A)
_EltexIpSlaStatsIcmpEchoLastStatus_Type=EltexIpSlaStatsOperStatus
_EltexIpSlaStatsIcmpEchoLastStatus_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoLastStatus=_EltexIpSlaStatsIcmpEchoLastStatus_Object((1,3,6,1,4,1,35265,32,1,3,2,1,2),_EltexIpSlaStatsIcmpEchoLastStatus_Type())
eltexIpSlaStatsIcmpEchoLastStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoLastStatus.setStatus(_A)
_EltexIpSlaStatsIcmpEchoLastLatency_Type=Integer32
_EltexIpSlaStatsIcmpEchoLastLatency_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoLastLatency=_EltexIpSlaStatsIcmpEchoLastLatency_Object((1,3,6,1,4,1,35265,32,1,3,2,1,3),_EltexIpSlaStatsIcmpEchoLastLatency_Type())
eltexIpSlaStatsIcmpEchoLastLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoLastLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoLastLatency.setUnits(_C)
_EltexIpSlaStatsIcmpEchoMinLatency_Type=Integer32
_EltexIpSlaStatsIcmpEchoMinLatency_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoMinLatency=_EltexIpSlaStatsIcmpEchoMinLatency_Object((1,3,6,1,4,1,35265,32,1,3,2,1,4),_EltexIpSlaStatsIcmpEchoMinLatency_Type())
eltexIpSlaStatsIcmpEchoMinLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoMinLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoMinLatency.setUnits(_C)
_EltexIpSlaStatsIcmpEchoAvgLatency_Type=Integer32
_EltexIpSlaStatsIcmpEchoAvgLatency_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoAvgLatency=_EltexIpSlaStatsIcmpEchoAvgLatency_Object((1,3,6,1,4,1,35265,32,1,3,2,1,5),_EltexIpSlaStatsIcmpEchoAvgLatency_Type())
eltexIpSlaStatsIcmpEchoAvgLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoAvgLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoAvgLatency.setUnits(_C)
_EltexIpSlaStatsIcmpEchoMaxLatency_Type=Integer32
_EltexIpSlaStatsIcmpEchoMaxLatency_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoMaxLatency=_EltexIpSlaStatsIcmpEchoMaxLatency_Object((1,3,6,1,4,1,35265,32,1,3,2,1,6),_EltexIpSlaStatsIcmpEchoMaxLatency_Type())
eltexIpSlaStatsIcmpEchoMaxLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoMaxLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoMaxLatency.setUnits(_C)
_EltexIpSlaStatsIcmpEchoOperationsCtr_Type=Counter32
_EltexIpSlaStatsIcmpEchoOperationsCtr_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoOperationsCtr=_EltexIpSlaStatsIcmpEchoOperationsCtr_Object((1,3,6,1,4,1,35265,32,1,3,2,1,7),_EltexIpSlaStatsIcmpEchoOperationsCtr_Type())
eltexIpSlaStatsIcmpEchoOperationsCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoOperationsCtr.setStatus(_A)
_EltexIpSlaStatsIcmpEchoSuccessesCtr_Type=Counter32
_EltexIpSlaStatsIcmpEchoSuccessesCtr_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoSuccessesCtr=_EltexIpSlaStatsIcmpEchoSuccessesCtr_Object((1,3,6,1,4,1,35265,32,1,3,2,1,8),_EltexIpSlaStatsIcmpEchoSuccessesCtr_Type())
eltexIpSlaStatsIcmpEchoSuccessesCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoSuccessesCtr.setStatus(_A)
_EltexIpSlaStatsIcmpEchoFailuresCtr_Type=Counter32
_EltexIpSlaStatsIcmpEchoFailuresCtr_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoFailuresCtr=_EltexIpSlaStatsIcmpEchoFailuresCtr_Object((1,3,6,1,4,1,35265,32,1,3,2,1,9),_EltexIpSlaStatsIcmpEchoFailuresCtr_Type())
eltexIpSlaStatsIcmpEchoFailuresCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoFailuresCtr.setStatus(_A)
_EltexIpSlaStatsIcmpEchoTimeoutCtr_Type=Counter32
_EltexIpSlaStatsIcmpEchoTimeoutCtr_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoTimeoutCtr=_EltexIpSlaStatsIcmpEchoTimeoutCtr_Object((1,3,6,1,4,1,35265,32,1,3,2,1,10),_EltexIpSlaStatsIcmpEchoTimeoutCtr_Type())
eltexIpSlaStatsIcmpEchoTimeoutCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoTimeoutCtr.setStatus(_A)
_EltexIpSlaStatsIcmpEchoUnreachNetCtr_Type=Counter32
_EltexIpSlaStatsIcmpEchoUnreachNetCtr_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoUnreachNetCtr=_EltexIpSlaStatsIcmpEchoUnreachNetCtr_Object((1,3,6,1,4,1,35265,32,1,3,2,1,11),_EltexIpSlaStatsIcmpEchoUnreachNetCtr_Type())
eltexIpSlaStatsIcmpEchoUnreachNetCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoUnreachNetCtr.setStatus(_A)
_EltexIpSlaStatsIcmpEchoUnreachHostCtr_Type=Counter32
_EltexIpSlaStatsIcmpEchoUnreachHostCtr_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoUnreachHostCtr=_EltexIpSlaStatsIcmpEchoUnreachHostCtr_Object((1,3,6,1,4,1,35265,32,1,3,2,1,12),_EltexIpSlaStatsIcmpEchoUnreachHostCtr_Type())
eltexIpSlaStatsIcmpEchoUnreachHostCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoUnreachHostCtr.setStatus(_A)
_EltexIpSlaStatsIcmpEchoUnreachProtCtr_Type=Counter32
_EltexIpSlaStatsIcmpEchoUnreachProtCtr_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoUnreachProtCtr=_EltexIpSlaStatsIcmpEchoUnreachProtCtr_Object((1,3,6,1,4,1,35265,32,1,3,2,1,13),_EltexIpSlaStatsIcmpEchoUnreachProtCtr_Type())
eltexIpSlaStatsIcmpEchoUnreachProtCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoUnreachProtCtr.setStatus(_A)
_EltexIpSlaStatsIcmpEchoExTimeTransCtr_Type=Counter32
_EltexIpSlaStatsIcmpEchoExTimeTransCtr_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoExTimeTransCtr=_EltexIpSlaStatsIcmpEchoExTimeTransCtr_Object((1,3,6,1,4,1,35265,32,1,3,2,1,14),_EltexIpSlaStatsIcmpEchoExTimeTransCtr_Type())
eltexIpSlaStatsIcmpEchoExTimeTransCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoExTimeTransCtr.setStatus(_A)
_EltexIpSlaStatsIcmpEchoExTimeReassCtr_Type=Counter32
_EltexIpSlaStatsIcmpEchoExTimeReassCtr_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoExTimeReassCtr=_EltexIpSlaStatsIcmpEchoExTimeReassCtr_Object((1,3,6,1,4,1,35265,32,1,3,2,1,15),_EltexIpSlaStatsIcmpEchoExTimeReassCtr_Type())
eltexIpSlaStatsIcmpEchoExTimeReassCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoExTimeReassCtr.setStatus(_A)
_EltexIpSlaStatsIcmpEchoUnableSendCtr_Type=Counter32
_EltexIpSlaStatsIcmpEchoUnableSendCtr_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoUnableSendCtr=_EltexIpSlaStatsIcmpEchoUnableSendCtr_Object((1,3,6,1,4,1,35265,32,1,3,2,1,16),_EltexIpSlaStatsIcmpEchoUnableSendCtr_Type())
eltexIpSlaStatsIcmpEchoUnableSendCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoUnableSendCtr.setStatus(_A)
_EltexIpSlaStatsIcmpEchoBadReplyCtr_Type=Counter32
_EltexIpSlaStatsIcmpEchoBadReplyCtr_Object=MibTableColumn
eltexIpSlaStatsIcmpEchoBadReplyCtr=_EltexIpSlaStatsIcmpEchoBadReplyCtr_Object((1,3,6,1,4,1,35265,32,1,3,2,1,17),_EltexIpSlaStatsIcmpEchoBadReplyCtr_Type())
eltexIpSlaStatsIcmpEchoBadReplyCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsIcmpEchoBadReplyCtr.setStatus(_A)
_EltexIpSlaStatsUdpJitterTable_Object=MibTable
eltexIpSlaStatsUdpJitterTable=_EltexIpSlaStatsUdpJitterTable_Object((1,3,6,1,4,1,35265,32,1,3,3))
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterTable.setStatus(_A)
_EltexIpSlaStatsUdpJitterEntry_Object=MibTableRow
eltexIpSlaStatsUdpJitterEntry=_EltexIpSlaStatsUdpJitterEntry_Object((1,3,6,1,4,1,35265,32,1,3,3,1))
eltexIpSlaStatsUdpJitterEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterEntry.setStatus(_A)
_EltexIpSlaStatsUdpJitterIndex_Type=Integer32
_EltexIpSlaStatsUdpJitterIndex_Object=MibTableColumn
eltexIpSlaStatsUdpJitterIndex=_EltexIpSlaStatsUdpJitterIndex_Object((1,3,6,1,4,1,35265,32,1,3,3,1,1),_EltexIpSlaStatsUdpJitterIndex_Type())
eltexIpSlaStatsUdpJitterIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterIndex.setStatus(_A)
_EltexIpSlaStatsUdpJitterLastStatus_Type=EltexIpSlaStatsOperStatus
_EltexIpSlaStatsUdpJitterLastStatus_Object=MibTableColumn
eltexIpSlaStatsUdpJitterLastStatus=_EltexIpSlaStatsUdpJitterLastStatus_Object((1,3,6,1,4,1,35265,32,1,3,3,1,2),_EltexIpSlaStatsUdpJitterLastStatus_Type())
eltexIpSlaStatsUdpJitterLastStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterLastStatus.setStatus(_A)
_EltexIpSlaStatsUdpJitterLastLatency_Type=Integer32
_EltexIpSlaStatsUdpJitterLastLatency_Object=MibTableColumn
eltexIpSlaStatsUdpJitterLastLatency=_EltexIpSlaStatsUdpJitterLastLatency_Object((1,3,6,1,4,1,35265,32,1,3,3,1,3),_EltexIpSlaStatsUdpJitterLastLatency_Type())
eltexIpSlaStatsUdpJitterLastLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterLastLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterLastLatency.setUnits(_C)
_EltexIpSlaStatsUdpJitterNumLatency_Type=Integer32
_EltexIpSlaStatsUdpJitterNumLatency_Object=MibTableColumn
eltexIpSlaStatsUdpJitterNumLatency=_EltexIpSlaStatsUdpJitterNumLatency_Object((1,3,6,1,4,1,35265,32,1,3,3,1,4),_EltexIpSlaStatsUdpJitterNumLatency_Type())
eltexIpSlaStatsUdpJitterNumLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterNumLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterNumLatency.setUnits(_C)
_EltexIpSlaStatsUdpJitterSumLatency_Type=Integer32
_EltexIpSlaStatsUdpJitterSumLatency_Object=MibTableColumn
eltexIpSlaStatsUdpJitterSumLatency=_EltexIpSlaStatsUdpJitterSumLatency_Object((1,3,6,1,4,1,35265,32,1,3,3,1,5),_EltexIpSlaStatsUdpJitterSumLatency_Type())
eltexIpSlaStatsUdpJitterSumLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterSumLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterSumLatency.setUnits(_C)
_EltexIpSlaStatsUdpJitterMinLatency_Type=Integer32
_EltexIpSlaStatsUdpJitterMinLatency_Object=MibTableColumn
eltexIpSlaStatsUdpJitterMinLatency=_EltexIpSlaStatsUdpJitterMinLatency_Object((1,3,6,1,4,1,35265,32,1,3,3,1,6),_EltexIpSlaStatsUdpJitterMinLatency_Type())
eltexIpSlaStatsUdpJitterMinLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMinLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMinLatency.setUnits(_C)
_EltexIpSlaStatsUdpJitterAvgLatency_Type=Integer32
_EltexIpSlaStatsUdpJitterAvgLatency_Object=MibTableColumn
eltexIpSlaStatsUdpJitterAvgLatency=_EltexIpSlaStatsUdpJitterAvgLatency_Object((1,3,6,1,4,1,35265,32,1,3,3,1,7),_EltexIpSlaStatsUdpJitterAvgLatency_Type())
eltexIpSlaStatsUdpJitterAvgLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterAvgLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterAvgLatency.setUnits(_C)
_EltexIpSlaStatsUdpJitterMaxLatency_Type=Integer32
_EltexIpSlaStatsUdpJitterMaxLatency_Object=MibTableColumn
eltexIpSlaStatsUdpJitterMaxLatency=_EltexIpSlaStatsUdpJitterMaxLatency_Object((1,3,6,1,4,1,35265,32,1,3,3,1,8),_EltexIpSlaStatsUdpJitterMaxLatency_Type())
eltexIpSlaStatsUdpJitterMaxLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMaxLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMaxLatency.setUnits(_C)
_EltexIpSlaStatsUdpJitterNumSDLatency_Type=Integer32
_EltexIpSlaStatsUdpJitterNumSDLatency_Object=MibTableColumn
eltexIpSlaStatsUdpJitterNumSDLatency=_EltexIpSlaStatsUdpJitterNumSDLatency_Object((1,3,6,1,4,1,35265,32,1,3,3,1,9),_EltexIpSlaStatsUdpJitterNumSDLatency_Type())
eltexIpSlaStatsUdpJitterNumSDLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterNumSDLatency.setStatus(_A)
_EltexIpSlaStatsUdpJitterSumSDLatency_Type=Integer32
_EltexIpSlaStatsUdpJitterSumSDLatency_Object=MibTableColumn
eltexIpSlaStatsUdpJitterSumSDLatency=_EltexIpSlaStatsUdpJitterSumSDLatency_Object((1,3,6,1,4,1,35265,32,1,3,3,1,10),_EltexIpSlaStatsUdpJitterSumSDLatency_Type())
eltexIpSlaStatsUdpJitterSumSDLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterSumSDLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterSumSDLatency.setUnits(_C)
_EltexIpSlaStatsUdpJitterMinSDLatency_Type=Integer32
_EltexIpSlaStatsUdpJitterMinSDLatency_Object=MibTableColumn
eltexIpSlaStatsUdpJitterMinSDLatency=_EltexIpSlaStatsUdpJitterMinSDLatency_Object((1,3,6,1,4,1,35265,32,1,3,3,1,11),_EltexIpSlaStatsUdpJitterMinSDLatency_Type())
eltexIpSlaStatsUdpJitterMinSDLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMinSDLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMinSDLatency.setUnits(_C)
_EltexIpSlaStatsUdpJitterAvgSDLatency_Type=Integer32
_EltexIpSlaStatsUdpJitterAvgSDLatency_Object=MibTableColumn
eltexIpSlaStatsUdpJitterAvgSDLatency=_EltexIpSlaStatsUdpJitterAvgSDLatency_Object((1,3,6,1,4,1,35265,32,1,3,3,1,12),_EltexIpSlaStatsUdpJitterAvgSDLatency_Type())
eltexIpSlaStatsUdpJitterAvgSDLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterAvgSDLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterAvgSDLatency.setUnits(_C)
_EltexIpSlaStatsUdpJitterMaxSDLatency_Type=Integer32
_EltexIpSlaStatsUdpJitterMaxSDLatency_Object=MibTableColumn
eltexIpSlaStatsUdpJitterMaxSDLatency=_EltexIpSlaStatsUdpJitterMaxSDLatency_Object((1,3,6,1,4,1,35265,32,1,3,3,1,13),_EltexIpSlaStatsUdpJitterMaxSDLatency_Type())
eltexIpSlaStatsUdpJitterMaxSDLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMaxSDLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMaxSDLatency.setUnits(_C)
_EltexIpSlaStatsUdpJitterNumDSLatency_Type=Integer32
_EltexIpSlaStatsUdpJitterNumDSLatency_Object=MibTableColumn
eltexIpSlaStatsUdpJitterNumDSLatency=_EltexIpSlaStatsUdpJitterNumDSLatency_Object((1,3,6,1,4,1,35265,32,1,3,3,1,14),_EltexIpSlaStatsUdpJitterNumDSLatency_Type())
eltexIpSlaStatsUdpJitterNumDSLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterNumDSLatency.setStatus(_A)
_EltexIpSlaStatsUdpJitterSumDSLatency_Type=Integer32
_EltexIpSlaStatsUdpJitterSumDSLatency_Object=MibTableColumn
eltexIpSlaStatsUdpJitterSumDSLatency=_EltexIpSlaStatsUdpJitterSumDSLatency_Object((1,3,6,1,4,1,35265,32,1,3,3,1,15),_EltexIpSlaStatsUdpJitterSumDSLatency_Type())
eltexIpSlaStatsUdpJitterSumDSLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterSumDSLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterSumDSLatency.setUnits(_C)
_EltexIpSlaStatsUdpJitterMinDSLatency_Type=Integer32
_EltexIpSlaStatsUdpJitterMinDSLatency_Object=MibTableColumn
eltexIpSlaStatsUdpJitterMinDSLatency=_EltexIpSlaStatsUdpJitterMinDSLatency_Object((1,3,6,1,4,1,35265,32,1,3,3,1,16),_EltexIpSlaStatsUdpJitterMinDSLatency_Type())
eltexIpSlaStatsUdpJitterMinDSLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMinDSLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMinDSLatency.setUnits(_C)
_EltexIpSlaStatsUdpJitterAvgDSLatency_Type=Integer32
_EltexIpSlaStatsUdpJitterAvgDSLatency_Object=MibTableColumn
eltexIpSlaStatsUdpJitterAvgDSLatency=_EltexIpSlaStatsUdpJitterAvgDSLatency_Object((1,3,6,1,4,1,35265,32,1,3,3,1,17),_EltexIpSlaStatsUdpJitterAvgDSLatency_Type())
eltexIpSlaStatsUdpJitterAvgDSLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterAvgDSLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterAvgDSLatency.setUnits(_C)
_EltexIpSlaStatsUdpJitterMaxDSLatency_Type=Integer32
_EltexIpSlaStatsUdpJitterMaxDSLatency_Object=MibTableColumn
eltexIpSlaStatsUdpJitterMaxDSLatency=_EltexIpSlaStatsUdpJitterMaxDSLatency_Object((1,3,6,1,4,1,35265,32,1,3,3,1,18),_EltexIpSlaStatsUdpJitterMaxDSLatency_Type())
eltexIpSlaStatsUdpJitterMaxDSLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMaxDSLatency.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMaxDSLatency.setUnits(_C)
_EltexIpSlaStatsUdpJitterNumSDPosJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterNumSDPosJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterNumSDPosJitter=_EltexIpSlaStatsUdpJitterNumSDPosJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,19),_EltexIpSlaStatsUdpJitterNumSDPosJitter_Type())
eltexIpSlaStatsUdpJitterNumSDPosJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterNumSDPosJitter.setStatus(_A)
_EltexIpSlaStatsUdpJitterSumSDPosJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterSumSDPosJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterSumSDPosJitter=_EltexIpSlaStatsUdpJitterSumSDPosJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,20),_EltexIpSlaStatsUdpJitterSumSDPosJitter_Type())
eltexIpSlaStatsUdpJitterSumSDPosJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterSumSDPosJitter.setStatus(_A)
_EltexIpSlaStatsUdpJitterMinSDPosJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterMinSDPosJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterMinSDPosJitter=_EltexIpSlaStatsUdpJitterMinSDPosJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,21),_EltexIpSlaStatsUdpJitterMinSDPosJitter_Type())
eltexIpSlaStatsUdpJitterMinSDPosJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMinSDPosJitter.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMinSDPosJitter.setUnits(_C)
_EltexIpSlaStatsUdpJitterAvgSDPosJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterAvgSDPosJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterAvgSDPosJitter=_EltexIpSlaStatsUdpJitterAvgSDPosJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,22),_EltexIpSlaStatsUdpJitterAvgSDPosJitter_Type())
eltexIpSlaStatsUdpJitterAvgSDPosJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterAvgSDPosJitter.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterAvgSDPosJitter.setUnits(_C)
_EltexIpSlaStatsUdpJitterMaxSDPosJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterMaxSDPosJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterMaxSDPosJitter=_EltexIpSlaStatsUdpJitterMaxSDPosJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,23),_EltexIpSlaStatsUdpJitterMaxSDPosJitter_Type())
eltexIpSlaStatsUdpJitterMaxSDPosJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMaxSDPosJitter.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMaxSDPosJitter.setUnits(_C)
_EltexIpSlaStatsUdpJitterNumDSPosJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterNumDSPosJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterNumDSPosJitter=_EltexIpSlaStatsUdpJitterNumDSPosJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,24),_EltexIpSlaStatsUdpJitterNumDSPosJitter_Type())
eltexIpSlaStatsUdpJitterNumDSPosJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterNumDSPosJitter.setStatus(_A)
_EltexIpSlaStatsUdpJitterSumDSPosJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterSumDSPosJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterSumDSPosJitter=_EltexIpSlaStatsUdpJitterSumDSPosJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,25),_EltexIpSlaStatsUdpJitterSumDSPosJitter_Type())
eltexIpSlaStatsUdpJitterSumDSPosJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterSumDSPosJitter.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterSumDSPosJitter.setUnits(_C)
_EltexIpSlaStatsUdpJitterMinDSPosJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterMinDSPosJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterMinDSPosJitter=_EltexIpSlaStatsUdpJitterMinDSPosJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,26),_EltexIpSlaStatsUdpJitterMinDSPosJitter_Type())
eltexIpSlaStatsUdpJitterMinDSPosJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMinDSPosJitter.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMinDSPosJitter.setUnits(_C)
_EltexIpSlaStatsUdpJitterAvgDSPosJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterAvgDSPosJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterAvgDSPosJitter=_EltexIpSlaStatsUdpJitterAvgDSPosJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,27),_EltexIpSlaStatsUdpJitterAvgDSPosJitter_Type())
eltexIpSlaStatsUdpJitterAvgDSPosJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterAvgDSPosJitter.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterAvgDSPosJitter.setUnits(_C)
_EltexIpSlaStatsUdpJitterMaxDSPosJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterMaxDSPosJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterMaxDSPosJitter=_EltexIpSlaStatsUdpJitterMaxDSPosJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,28),_EltexIpSlaStatsUdpJitterMaxDSPosJitter_Type())
eltexIpSlaStatsUdpJitterMaxDSPosJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMaxDSPosJitter.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMaxDSPosJitter.setUnits(_C)
_EltexIpSlaStatsUdpJitterNumSDNegJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterNumSDNegJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterNumSDNegJitter=_EltexIpSlaStatsUdpJitterNumSDNegJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,29),_EltexIpSlaStatsUdpJitterNumSDNegJitter_Type())
eltexIpSlaStatsUdpJitterNumSDNegJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterNumSDNegJitter.setStatus(_A)
_EltexIpSlaStatsUdpJitterSumSDNegJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterSumSDNegJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterSumSDNegJitter=_EltexIpSlaStatsUdpJitterSumSDNegJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,30),_EltexIpSlaStatsUdpJitterSumSDNegJitter_Type())
eltexIpSlaStatsUdpJitterSumSDNegJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterSumSDNegJitter.setStatus(_A)
_EltexIpSlaStatsUdpJitterMinSDNegJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterMinSDNegJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterMinSDNegJitter=_EltexIpSlaStatsUdpJitterMinSDNegJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,31),_EltexIpSlaStatsUdpJitterMinSDNegJitter_Type())
eltexIpSlaStatsUdpJitterMinSDNegJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMinSDNegJitter.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMinSDNegJitter.setUnits(_C)
_EltexIpSlaStatsUdpJitterAvgSDNegJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterAvgSDNegJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterAvgSDNegJitter=_EltexIpSlaStatsUdpJitterAvgSDNegJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,32),_EltexIpSlaStatsUdpJitterAvgSDNegJitter_Type())
eltexIpSlaStatsUdpJitterAvgSDNegJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterAvgSDNegJitter.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterAvgSDNegJitter.setUnits(_C)
_EltexIpSlaStatsUdpJitterMaxSDNegJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterMaxSDNegJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterMaxSDNegJitter=_EltexIpSlaStatsUdpJitterMaxSDNegJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,33),_EltexIpSlaStatsUdpJitterMaxSDNegJitter_Type())
eltexIpSlaStatsUdpJitterMaxSDNegJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMaxSDNegJitter.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMaxSDNegJitter.setUnits(_C)
_EltexIpSlaStatsUdpJitterNumDSNegJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterNumDSNegJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterNumDSNegJitter=_EltexIpSlaStatsUdpJitterNumDSNegJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,34),_EltexIpSlaStatsUdpJitterNumDSNegJitter_Type())
eltexIpSlaStatsUdpJitterNumDSNegJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterNumDSNegJitter.setStatus(_A)
_EltexIpSlaStatsUdpJitterSumDSNegJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterSumDSNegJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterSumDSNegJitter=_EltexIpSlaStatsUdpJitterSumDSNegJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,35),_EltexIpSlaStatsUdpJitterSumDSNegJitter_Type())
eltexIpSlaStatsUdpJitterSumDSNegJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterSumDSNegJitter.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterSumDSNegJitter.setUnits(_C)
_EltexIpSlaStatsUdpJitterMinDSNegJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterMinDSNegJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterMinDSNegJitter=_EltexIpSlaStatsUdpJitterMinDSNegJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,36),_EltexIpSlaStatsUdpJitterMinDSNegJitter_Type())
eltexIpSlaStatsUdpJitterMinDSNegJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMinDSNegJitter.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMinDSNegJitter.setUnits(_C)
_EltexIpSlaStatsUdpJitterAvgDSNegJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterAvgDSNegJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterAvgDSNegJitter=_EltexIpSlaStatsUdpJitterAvgDSNegJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,37),_EltexIpSlaStatsUdpJitterAvgDSNegJitter_Type())
eltexIpSlaStatsUdpJitterAvgDSNegJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterAvgDSNegJitter.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterAvgDSNegJitter.setUnits(_C)
_EltexIpSlaStatsUdpJitterMaxDSNegJitter_Type=Integer32
_EltexIpSlaStatsUdpJitterMaxDSNegJitter_Object=MibTableColumn
eltexIpSlaStatsUdpJitterMaxDSNegJitter=_EltexIpSlaStatsUdpJitterMaxDSNegJitter_Object((1,3,6,1,4,1,35265,32,1,3,3,1,38),_EltexIpSlaStatsUdpJitterMaxDSNegJitter_Type())
eltexIpSlaStatsUdpJitterMaxDSNegJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMaxDSNegJitter.setStatus(_A)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterMaxDSNegJitter.setUnits(_C)
_EltexIpSlaStatsUdpJitterOperationsCtr_Type=Counter32
_EltexIpSlaStatsUdpJitterOperationsCtr_Object=MibTableColumn
eltexIpSlaStatsUdpJitterOperationsCtr=_EltexIpSlaStatsUdpJitterOperationsCtr_Object((1,3,6,1,4,1,35265,32,1,3,3,1,39),_EltexIpSlaStatsUdpJitterOperationsCtr_Type())
eltexIpSlaStatsUdpJitterOperationsCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterOperationsCtr.setStatus(_A)
_EltexIpSlaStatsUdpJitterSuccessesCtr_Type=Counter32
_EltexIpSlaStatsUdpJitterSuccessesCtr_Object=MibTableColumn
eltexIpSlaStatsUdpJitterSuccessesCtr=_EltexIpSlaStatsUdpJitterSuccessesCtr_Object((1,3,6,1,4,1,35265,32,1,3,3,1,40),_EltexIpSlaStatsUdpJitterSuccessesCtr_Type())
eltexIpSlaStatsUdpJitterSuccessesCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterSuccessesCtr.setStatus(_A)
_EltexIpSlaStatsUdpJitterFailuresCtr_Type=Counter32
_EltexIpSlaStatsUdpJitterFailuresCtr_Object=MibTableColumn
eltexIpSlaStatsUdpJitterFailuresCtr=_EltexIpSlaStatsUdpJitterFailuresCtr_Object((1,3,6,1,4,1,35265,32,1,3,3,1,41),_EltexIpSlaStatsUdpJitterFailuresCtr_Type())
eltexIpSlaStatsUdpJitterFailuresCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterFailuresCtr.setStatus(_A)
_EltexIpSlaStatsUdpJitterTimeoutCtr_Type=Counter32
_EltexIpSlaStatsUdpJitterTimeoutCtr_Object=MibTableColumn
eltexIpSlaStatsUdpJitterTimeoutCtr=_EltexIpSlaStatsUdpJitterTimeoutCtr_Object((1,3,6,1,4,1,35265,32,1,3,3,1,42),_EltexIpSlaStatsUdpJitterTimeoutCtr_Type())
eltexIpSlaStatsUdpJitterTimeoutCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterTimeoutCtr.setStatus(_A)
_EltexIpSlaStatsUdpJitterUnreachNetCtr_Type=Counter32
_EltexIpSlaStatsUdpJitterUnreachNetCtr_Object=MibTableColumn
eltexIpSlaStatsUdpJitterUnreachNetCtr=_EltexIpSlaStatsUdpJitterUnreachNetCtr_Object((1,3,6,1,4,1,35265,32,1,3,3,1,43),_EltexIpSlaStatsUdpJitterUnreachNetCtr_Type())
eltexIpSlaStatsUdpJitterUnreachNetCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterUnreachNetCtr.setStatus(_A)
_EltexIpSlaStatsUdpJitterUnreachHostCtr_Type=Counter32
_EltexIpSlaStatsUdpJitterUnreachHostCtr_Object=MibTableColumn
eltexIpSlaStatsUdpJitterUnreachHostCtr=_EltexIpSlaStatsUdpJitterUnreachHostCtr_Object((1,3,6,1,4,1,35265,32,1,3,3,1,44),_EltexIpSlaStatsUdpJitterUnreachHostCtr_Type())
eltexIpSlaStatsUdpJitterUnreachHostCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterUnreachHostCtr.setStatus(_A)
_EltexIpSlaStatsUdpJitterUnreachPortCtr_Type=Counter32
_EltexIpSlaStatsUdpJitterUnreachPortCtr_Object=MibTableColumn
eltexIpSlaStatsUdpJitterUnreachPortCtr=_EltexIpSlaStatsUdpJitterUnreachPortCtr_Object((1,3,6,1,4,1,35265,32,1,3,3,1,45),_EltexIpSlaStatsUdpJitterUnreachPortCtr_Type())
eltexIpSlaStatsUdpJitterUnreachPortCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterUnreachPortCtr.setStatus(_A)
_EltexIpSlaStatsUdpJitterUnreachProtCtr_Type=Counter32
_EltexIpSlaStatsUdpJitterUnreachProtCtr_Object=MibTableColumn
eltexIpSlaStatsUdpJitterUnreachProtCtr=_EltexIpSlaStatsUdpJitterUnreachProtCtr_Object((1,3,6,1,4,1,35265,32,1,3,3,1,46),_EltexIpSlaStatsUdpJitterUnreachProtCtr_Type())
eltexIpSlaStatsUdpJitterUnreachProtCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterUnreachProtCtr.setStatus(_A)
_EltexIpSlaStatsUdpJitterExTimeTransCtr_Type=Counter32
_EltexIpSlaStatsUdpJitterExTimeTransCtr_Object=MibTableColumn
eltexIpSlaStatsUdpJitterExTimeTransCtr=_EltexIpSlaStatsUdpJitterExTimeTransCtr_Object((1,3,6,1,4,1,35265,32,1,3,3,1,47),_EltexIpSlaStatsUdpJitterExTimeTransCtr_Type())
eltexIpSlaStatsUdpJitterExTimeTransCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterExTimeTransCtr.setStatus(_A)
_EltexIpSlaStatsUdpJitterExTimeReassCtr_Type=Counter32
_EltexIpSlaStatsUdpJitterExTimeReassCtr_Object=MibTableColumn
eltexIpSlaStatsUdpJitterExTimeReassCtr=_EltexIpSlaStatsUdpJitterExTimeReassCtr_Object((1,3,6,1,4,1,35265,32,1,3,3,1,48),_EltexIpSlaStatsUdpJitterExTimeReassCtr_Type())
eltexIpSlaStatsUdpJitterExTimeReassCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterExTimeReassCtr.setStatus(_A)
_EltexIpSlaStatsUdpJitterUnableSendCtr_Type=Counter32
_EltexIpSlaStatsUdpJitterUnableSendCtr_Object=MibTableColumn
eltexIpSlaStatsUdpJitterUnableSendCtr=_EltexIpSlaStatsUdpJitterUnableSendCtr_Object((1,3,6,1,4,1,35265,32,1,3,3,1,49),_EltexIpSlaStatsUdpJitterUnableSendCtr_Type())
eltexIpSlaStatsUdpJitterUnableSendCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterUnableSendCtr.setStatus(_A)
_EltexIpSlaStatsUdpJitterBadReplyCtr_Type=Counter32
_EltexIpSlaStatsUdpJitterBadReplyCtr_Object=MibTableColumn
eltexIpSlaStatsUdpJitterBadReplyCtr=_EltexIpSlaStatsUdpJitterBadReplyCtr_Object((1,3,6,1,4,1,35265,32,1,3,3,1,50),_EltexIpSlaStatsUdpJitterBadReplyCtr_Type())
eltexIpSlaStatsUdpJitterBadReplyCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterBadReplyCtr.setStatus(_A)
_EltexIpSlaStatsUdpJitterPacketsOOSCtr_Type=Counter32
_EltexIpSlaStatsUdpJitterPacketsOOSCtr_Object=MibTableColumn
eltexIpSlaStatsUdpJitterPacketsOOSCtr=_EltexIpSlaStatsUdpJitterPacketsOOSCtr_Object((1,3,6,1,4,1,35265,32,1,3,3,1,51),_EltexIpSlaStatsUdpJitterPacketsOOSCtr_Type())
eltexIpSlaStatsUdpJitterPacketsOOSCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexIpSlaStatsUdpJitterPacketsOOSCtr.setStatus(_A)
_EltexIpSlaSchedule_ObjectIdentity=ObjectIdentity
eltexIpSlaSchedule=_EltexIpSlaSchedule_ObjectIdentity((1,3,6,1,4,1,35265,32,1,4))
_EltexIpSlaScheduleStartTrigger_Type=Integer32
_EltexIpSlaScheduleStartTrigger_Object=MibScalar
eltexIpSlaScheduleStartTrigger=_EltexIpSlaScheduleStartTrigger_Object((1,3,6,1,4,1,35265,32,1,4,1),_EltexIpSlaScheduleStartTrigger_Type())
eltexIpSlaScheduleStartTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaScheduleStartTrigger.setStatus(_A)
_EltexIpSlaScheduleStopTrigger_Type=Integer32
_EltexIpSlaScheduleStopTrigger_Object=MibScalar
eltexIpSlaScheduleStopTrigger=_EltexIpSlaScheduleStopTrigger_Object((1,3,6,1,4,1,35265,32,1,4,2),_EltexIpSlaScheduleStopTrigger_Type())
eltexIpSlaScheduleStopTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpSlaScheduleStopTrigger.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'EltexIpSlaOperationType':EltexIpSlaOperationType,'EltexIpSlaOperationStatus':EltexIpSlaOperationStatus,'EltexIpSlaStatsOperStatus':EltexIpSlaStatsOperStatus,'eltexIpSlaMIB':eltexIpSlaMIB,'eltexIpSlaObjects':eltexIpSlaObjects,'eltexIpSlaAppl':eltexIpSlaAppl,'eltexIpSlaApplResponder':eltexIpSlaApplResponder,'eltexIpSlaApplResponderUdpJitterPort':eltexIpSlaApplResponderUdpJitterPort,'eltexIpSlaAdmin':eltexIpSlaAdmin,'eltexIpSlaAdminCtrlTable':eltexIpSlaAdminCtrlTable,'eltexIpSlaAdminCtrlEntry':eltexIpSlaAdminCtrlEntry,_I:eltexIpSlaAdminCtrlIndex,'eltexIpSlaAdminCtrlType':eltexIpSlaAdminCtrlType,'eltexIpSlaAdminCtrlStatus':eltexIpSlaAdminCtrlStatus,'eltexIpSlaAdminCtrlFrequency':eltexIpSlaAdminCtrlFrequency,'eltexIpSlaAdminCtrlTag':eltexIpSlaAdminCtrlTag,'eltexIpSlaAdminCtrlOwner':eltexIpSlaAdminCtrlOwner,'eltexIpSlaAdminCtrlRowStatus':eltexIpSlaAdminCtrlRowStatus,'eltexIpSlaAdminIcmpEchoTable':eltexIpSlaAdminIcmpEchoTable,'eltexIpSlaAdminIcmpEchoEntry':eltexIpSlaAdminIcmpEchoEntry,_J:eltexIpSlaAdminIcmpEchoIndex,'eltexIpSlaAdminIcmpEchoTargetAddress':eltexIpSlaAdminIcmpEchoTargetAddress,'eltexIpSlaAdminIcmpEchoSourceAddress':eltexIpSlaAdminIcmpEchoSourceAddress,'eltexIpSlaAdminIcmpEchoSourceInterface':eltexIpSlaAdminIcmpEchoSourceInterface,'eltexIpSlaAdminIcmpEchoTimeOut':eltexIpSlaAdminIcmpEchoTimeOut,'eltexIpSlaAdminIcmpEchoReqDataSize':eltexIpSlaAdminIcmpEchoReqDataSize,'eltexIpSlaAdminIcmpEchoTOS':eltexIpSlaAdminIcmpEchoTOS,'eltexIpSlaAdminIcmpEchoRowStatus':eltexIpSlaAdminIcmpEchoRowStatus,'eltexIpSlaAdminUdpJitterTable':eltexIpSlaAdminUdpJitterTable,'eltexIpSlaAdminUdpJitterEntry':eltexIpSlaAdminUdpJitterEntry,_K:eltexIpSlaAdminUdpJitterIndex,'eltexIpSlaAdminUdpJitterTargetAddress':eltexIpSlaAdminUdpJitterTargetAddress,'eltexIpSlaAdminUdpJitterTargetPort':eltexIpSlaAdminUdpJitterTargetPort,'eltexIpSlaAdminUdpJitterSourceAddress':eltexIpSlaAdminUdpJitterSourceAddress,'eltexIpSlaAdminUdpJitterSourcePort':eltexIpSlaAdminUdpJitterSourcePort,'eltexIpSlaAdminUdpJitterSourceInterface':eltexIpSlaAdminUdpJitterSourceInterface,'eltexIpSlaAdminUdpJitterInterval':eltexIpSlaAdminUdpJitterInterval,'eltexIpSlaAdminUdpJitterNumPackets':eltexIpSlaAdminUdpJitterNumPackets,'eltexIpSlaAdminUdpJitterTimeOut':eltexIpSlaAdminUdpJitterTimeOut,'eltexIpSlaAdminUdpJitterReqDataSize':eltexIpSlaAdminUdpJitterReqDataSize,'eltexIpSlaAdminUdpJitterTOS':eltexIpSlaAdminUdpJitterTOS,'eltexIpSlaAdminUdpJitterRowStatus':eltexIpSlaAdminUdpJitterRowStatus,'eltexIpSlaStats':eltexIpSlaStats,'eltexIpSlaStatsIcmpEchoTable':eltexIpSlaStatsIcmpEchoTable,'eltexIpSlaStatsIcmpEchoEntry':eltexIpSlaStatsIcmpEchoEntry,_L:eltexIpSlaStatsIcmpEchoIndex,'eltexIpSlaStatsIcmpEchoLastStatus':eltexIpSlaStatsIcmpEchoLastStatus,'eltexIpSlaStatsIcmpEchoLastLatency':eltexIpSlaStatsIcmpEchoLastLatency,'eltexIpSlaStatsIcmpEchoMinLatency':eltexIpSlaStatsIcmpEchoMinLatency,'eltexIpSlaStatsIcmpEchoAvgLatency':eltexIpSlaStatsIcmpEchoAvgLatency,'eltexIpSlaStatsIcmpEchoMaxLatency':eltexIpSlaStatsIcmpEchoMaxLatency,'eltexIpSlaStatsIcmpEchoOperationsCtr':eltexIpSlaStatsIcmpEchoOperationsCtr,'eltexIpSlaStatsIcmpEchoSuccessesCtr':eltexIpSlaStatsIcmpEchoSuccessesCtr,'eltexIpSlaStatsIcmpEchoFailuresCtr':eltexIpSlaStatsIcmpEchoFailuresCtr,'eltexIpSlaStatsIcmpEchoTimeoutCtr':eltexIpSlaStatsIcmpEchoTimeoutCtr,'eltexIpSlaStatsIcmpEchoUnreachNetCtr':eltexIpSlaStatsIcmpEchoUnreachNetCtr,'eltexIpSlaStatsIcmpEchoUnreachHostCtr':eltexIpSlaStatsIcmpEchoUnreachHostCtr,'eltexIpSlaStatsIcmpEchoUnreachProtCtr':eltexIpSlaStatsIcmpEchoUnreachProtCtr,'eltexIpSlaStatsIcmpEchoExTimeTransCtr':eltexIpSlaStatsIcmpEchoExTimeTransCtr,'eltexIpSlaStatsIcmpEchoExTimeReassCtr':eltexIpSlaStatsIcmpEchoExTimeReassCtr,'eltexIpSlaStatsIcmpEchoUnableSendCtr':eltexIpSlaStatsIcmpEchoUnableSendCtr,'eltexIpSlaStatsIcmpEchoBadReplyCtr':eltexIpSlaStatsIcmpEchoBadReplyCtr,'eltexIpSlaStatsUdpJitterTable':eltexIpSlaStatsUdpJitterTable,'eltexIpSlaStatsUdpJitterEntry':eltexIpSlaStatsUdpJitterEntry,_M:eltexIpSlaStatsUdpJitterIndex,'eltexIpSlaStatsUdpJitterLastStatus':eltexIpSlaStatsUdpJitterLastStatus,'eltexIpSlaStatsUdpJitterLastLatency':eltexIpSlaStatsUdpJitterLastLatency,'eltexIpSlaStatsUdpJitterNumLatency':eltexIpSlaStatsUdpJitterNumLatency,'eltexIpSlaStatsUdpJitterSumLatency':eltexIpSlaStatsUdpJitterSumLatency,'eltexIpSlaStatsUdpJitterMinLatency':eltexIpSlaStatsUdpJitterMinLatency,'eltexIpSlaStatsUdpJitterAvgLatency':eltexIpSlaStatsUdpJitterAvgLatency,'eltexIpSlaStatsUdpJitterMaxLatency':eltexIpSlaStatsUdpJitterMaxLatency,'eltexIpSlaStatsUdpJitterNumSDLatency':eltexIpSlaStatsUdpJitterNumSDLatency,'eltexIpSlaStatsUdpJitterSumSDLatency':eltexIpSlaStatsUdpJitterSumSDLatency,'eltexIpSlaStatsUdpJitterMinSDLatency':eltexIpSlaStatsUdpJitterMinSDLatency,'eltexIpSlaStatsUdpJitterAvgSDLatency':eltexIpSlaStatsUdpJitterAvgSDLatency,'eltexIpSlaStatsUdpJitterMaxSDLatency':eltexIpSlaStatsUdpJitterMaxSDLatency,'eltexIpSlaStatsUdpJitterNumDSLatency':eltexIpSlaStatsUdpJitterNumDSLatency,'eltexIpSlaStatsUdpJitterSumDSLatency':eltexIpSlaStatsUdpJitterSumDSLatency,'eltexIpSlaStatsUdpJitterMinDSLatency':eltexIpSlaStatsUdpJitterMinDSLatency,'eltexIpSlaStatsUdpJitterAvgDSLatency':eltexIpSlaStatsUdpJitterAvgDSLatency,'eltexIpSlaStatsUdpJitterMaxDSLatency':eltexIpSlaStatsUdpJitterMaxDSLatency,'eltexIpSlaStatsUdpJitterNumSDPosJitter':eltexIpSlaStatsUdpJitterNumSDPosJitter,'eltexIpSlaStatsUdpJitterSumSDPosJitter':eltexIpSlaStatsUdpJitterSumSDPosJitter,'eltexIpSlaStatsUdpJitterMinSDPosJitter':eltexIpSlaStatsUdpJitterMinSDPosJitter,'eltexIpSlaStatsUdpJitterAvgSDPosJitter':eltexIpSlaStatsUdpJitterAvgSDPosJitter,'eltexIpSlaStatsUdpJitterMaxSDPosJitter':eltexIpSlaStatsUdpJitterMaxSDPosJitter,'eltexIpSlaStatsUdpJitterNumDSPosJitter':eltexIpSlaStatsUdpJitterNumDSPosJitter,'eltexIpSlaStatsUdpJitterSumDSPosJitter':eltexIpSlaStatsUdpJitterSumDSPosJitter,'eltexIpSlaStatsUdpJitterMinDSPosJitter':eltexIpSlaStatsUdpJitterMinDSPosJitter,'eltexIpSlaStatsUdpJitterAvgDSPosJitter':eltexIpSlaStatsUdpJitterAvgDSPosJitter,'eltexIpSlaStatsUdpJitterMaxDSPosJitter':eltexIpSlaStatsUdpJitterMaxDSPosJitter,'eltexIpSlaStatsUdpJitterNumSDNegJitter':eltexIpSlaStatsUdpJitterNumSDNegJitter,'eltexIpSlaStatsUdpJitterSumSDNegJitter':eltexIpSlaStatsUdpJitterSumSDNegJitter,'eltexIpSlaStatsUdpJitterMinSDNegJitter':eltexIpSlaStatsUdpJitterMinSDNegJitter,'eltexIpSlaStatsUdpJitterAvgSDNegJitter':eltexIpSlaStatsUdpJitterAvgSDNegJitter,'eltexIpSlaStatsUdpJitterMaxSDNegJitter':eltexIpSlaStatsUdpJitterMaxSDNegJitter,'eltexIpSlaStatsUdpJitterNumDSNegJitter':eltexIpSlaStatsUdpJitterNumDSNegJitter,'eltexIpSlaStatsUdpJitterSumDSNegJitter':eltexIpSlaStatsUdpJitterSumDSNegJitter,'eltexIpSlaStatsUdpJitterMinDSNegJitter':eltexIpSlaStatsUdpJitterMinDSNegJitter,'eltexIpSlaStatsUdpJitterAvgDSNegJitter':eltexIpSlaStatsUdpJitterAvgDSNegJitter,'eltexIpSlaStatsUdpJitterMaxDSNegJitter':eltexIpSlaStatsUdpJitterMaxDSNegJitter,'eltexIpSlaStatsUdpJitterOperationsCtr':eltexIpSlaStatsUdpJitterOperationsCtr,'eltexIpSlaStatsUdpJitterSuccessesCtr':eltexIpSlaStatsUdpJitterSuccessesCtr,'eltexIpSlaStatsUdpJitterFailuresCtr':eltexIpSlaStatsUdpJitterFailuresCtr,'eltexIpSlaStatsUdpJitterTimeoutCtr':eltexIpSlaStatsUdpJitterTimeoutCtr,'eltexIpSlaStatsUdpJitterUnreachNetCtr':eltexIpSlaStatsUdpJitterUnreachNetCtr,'eltexIpSlaStatsUdpJitterUnreachHostCtr':eltexIpSlaStatsUdpJitterUnreachHostCtr,'eltexIpSlaStatsUdpJitterUnreachPortCtr':eltexIpSlaStatsUdpJitterUnreachPortCtr,'eltexIpSlaStatsUdpJitterUnreachProtCtr':eltexIpSlaStatsUdpJitterUnreachProtCtr,'eltexIpSlaStatsUdpJitterExTimeTransCtr':eltexIpSlaStatsUdpJitterExTimeTransCtr,'eltexIpSlaStatsUdpJitterExTimeReassCtr':eltexIpSlaStatsUdpJitterExTimeReassCtr,'eltexIpSlaStatsUdpJitterUnableSendCtr':eltexIpSlaStatsUdpJitterUnableSendCtr,'eltexIpSlaStatsUdpJitterBadReplyCtr':eltexIpSlaStatsUdpJitterBadReplyCtr,'eltexIpSlaStatsUdpJitterPacketsOOSCtr':eltexIpSlaStatsUdpJitterPacketsOOSCtr,'eltexIpSlaSchedule':eltexIpSlaSchedule,'eltexIpSlaScheduleStartTrigger':eltexIpSlaScheduleStartTrigger,'eltexIpSlaScheduleStopTrigger':eltexIpSlaScheduleStopTrigger})