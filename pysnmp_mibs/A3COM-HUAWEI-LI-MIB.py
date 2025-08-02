_T='h3cLIBoardInformation'
_S='h3cLIMediationRowStatus'
_R='00000000'
_Q='not-accessible'
_P='SnmpAdminString'
_O='InetAddressType'
_N='OctetString'
_M='h3cLIStreamtype'
_L='TruthValue'
_K='InetAddressPrefixLength'
_J='InetAddress'
_I='h3cLIStreamIndex'
_H='read-create'
_G='read-only'
_F='InetPortNumber'
_E='h3cLIMediationIndex'
_D='Integer32'
_C='A3COM-HUAWEI-LI-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_J,_K,_O,_F)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_P)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_L)
h3cLI=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,111))
if mibBuilder.loadTexts:h3cLI.setRevisions(('2009-08-25 10:00',))
_H3cLICommon_ObjectIdentity=ObjectIdentity
h3cLICommon=_H3cLICommon_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,111,1))
_H3cLITrapBindObjects_ObjectIdentity=ObjectIdentity
h3cLITrapBindObjects=_H3cLITrapBindObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,111,1,1))
_H3cLIBoardInformation_Type=Unsigned32
_H3cLIBoardInformation_Object=MibScalar
h3cLIBoardInformation=_H3cLIBoardInformation_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,1,1),_H3cLIBoardInformation_Type())
h3cLIBoardInformation.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cLIBoardInformation.setStatus(_A)
_H3cLINotifications_ObjectIdentity=ObjectIdentity
h3cLINotifications=_H3cLINotifications_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,111,1,2))
_H3cLINotificationsPrefix_ObjectIdentity=ObjectIdentity
h3cLINotificationsPrefix=_H3cLINotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,111,1,2,0))
_H3cLIObjects_ObjectIdentity=ObjectIdentity
h3cLIObjects=_H3cLIObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,111,1,3))
class _H3cLINewIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cLINewIndex_Type.__name__=_D
_H3cLINewIndex_Object=MibScalar
h3cLINewIndex=_H3cLINewIndex_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,1),_H3cLINewIndex_Type())
h3cLINewIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cLINewIndex.setStatus(_A)
_H3cLIMediationTable_Object=MibTable
h3cLIMediationTable=_H3cLIMediationTable_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,2))
if mibBuilder.loadTexts:h3cLIMediationTable.setStatus(_A)
_H3cLIMediationEntry_Object=MibTableRow
h3cLIMediationEntry=_H3cLIMediationEntry_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,2,1))
h3cLIMediationEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:h3cLIMediationEntry.setStatus(_A)
class _H3cLIMediationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cLIMediationIndex_Type.__name__=_D
_H3cLIMediationIndex_Object=MibTableColumn
h3cLIMediationIndex=_H3cLIMediationIndex_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,2,1,1),_H3cLIMediationIndex_Type())
h3cLIMediationIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:h3cLIMediationIndex.setStatus(_A)
_H3cLIMediationDestAddrType_Type=InetAddressType
_H3cLIMediationDestAddrType_Object=MibTableColumn
h3cLIMediationDestAddrType=_H3cLIMediationDestAddrType_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,2,1,2),_H3cLIMediationDestAddrType_Type())
h3cLIMediationDestAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIMediationDestAddrType.setStatus(_A)
_H3cLIMediationDestAddr_Type=InetAddress
_H3cLIMediationDestAddr_Object=MibTableColumn
h3cLIMediationDestAddr=_H3cLIMediationDestAddr_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,2,1,3),_H3cLIMediationDestAddr_Type())
h3cLIMediationDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIMediationDestAddr.setStatus(_A)
_H3cLIMediationDestPort_Type=InetPortNumber
_H3cLIMediationDestPort_Object=MibTableColumn
h3cLIMediationDestPort=_H3cLIMediationDestPort_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,2,1,4),_H3cLIMediationDestPort_Type())
h3cLIMediationDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIMediationDestPort.setStatus(_A)
_H3cLIMediationSrcInterface_Type=InterfaceIndexOrZero
_H3cLIMediationSrcInterface_Object=MibTableColumn
h3cLIMediationSrcInterface=_H3cLIMediationSrcInterface_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,2,1,5),_H3cLIMediationSrcInterface_Type())
h3cLIMediationSrcInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIMediationSrcInterface.setStatus(_A)
class _H3cLIMediationDscp_Type(Integer32):defaultValue=34
_H3cLIMediationDscp_Type.__name__=_D
_H3cLIMediationDscp_Object=MibTableColumn
h3cLIMediationDscp=_H3cLIMediationDscp_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,2,1,6),_H3cLIMediationDscp_Type())
h3cLIMediationDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIMediationDscp.setStatus(_A)
_H3cLIMediationTimeOut_Type=DateAndTime
_H3cLIMediationTimeOut_Object=MibTableColumn
h3cLIMediationTimeOut=_H3cLIMediationTimeOut_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,2,1,7),_H3cLIMediationTimeOut_Type())
h3cLIMediationTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIMediationTimeOut.setStatus(_A)
class _H3cLIMediationTransport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('udp',1))
_H3cLIMediationTransport_Type.__name__=_D
_H3cLIMediationTransport_Object=MibTableColumn
h3cLIMediationTransport=_H3cLIMediationTransport_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,2,1,8),_H3cLIMediationTransport_Type())
h3cLIMediationTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIMediationTransport.setStatus(_A)
class _H3cLIMediationNotificationEnable_Type(TruthValue):defaultValue=1
_H3cLIMediationNotificationEnable_Type.__name__=_L
_H3cLIMediationNotificationEnable_Object=MibTableColumn
h3cLIMediationNotificationEnable=_H3cLIMediationNotificationEnable_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,2,1,9),_H3cLIMediationNotificationEnable_Type())
h3cLIMediationNotificationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIMediationNotificationEnable.setStatus(_A)
_H3cLIMediationRowStatus_Type=RowStatus
_H3cLIMediationRowStatus_Object=MibTableColumn
h3cLIMediationRowStatus=_H3cLIMediationRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,2,1,10),_H3cLIMediationRowStatus_Type())
h3cLIMediationRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cLIMediationRowStatus.setStatus(_A)
_H3cLIStreamTable_Object=MibTable
h3cLIStreamTable=_H3cLIStreamTable_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,3))
if mibBuilder.loadTexts:h3cLIStreamTable.setStatus(_A)
_H3cLIStreamEntry_Object=MibTableRow
h3cLIStreamEntry=_H3cLIStreamEntry_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,3,1))
h3cLIStreamEntry.setIndexNames((0,_C,_E),(0,_C,_I))
if mibBuilder.loadTexts:h3cLIStreamEntry.setStatus(_A)
class _H3cLIStreamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cLIStreamIndex_Type.__name__=_D
_H3cLIStreamIndex_Object=MibTableColumn
h3cLIStreamIndex=_H3cLIStreamIndex_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,3,1,1),_H3cLIStreamIndex_Type())
h3cLIStreamIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:h3cLIStreamIndex.setStatus(_A)
class _H3cLIStreamtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ip',1),('mac',2),('userConnection',3)))
_H3cLIStreamtype_Type.__name__=_D
_H3cLIStreamtype_Object=MibTableColumn
h3cLIStreamtype=_H3cLIStreamtype_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,3,1,2),_H3cLIStreamtype_Type())
h3cLIStreamtype.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIStreamtype.setStatus(_A)
class _H3cLIStreamEnable_Type(TruthValue):defaultValue=2
_H3cLIStreamEnable_Type.__name__=_L
_H3cLIStreamEnable_Object=MibTableColumn
h3cLIStreamEnable=_H3cLIStreamEnable_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,3,1,3),_H3cLIStreamEnable_Type())
h3cLIStreamEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIStreamEnable.setStatus(_A)
_H3cLIStreamPackets_Type=Counter32
_H3cLIStreamPackets_Object=MibTableColumn
h3cLIStreamPackets=_H3cLIStreamPackets_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,3,1,4),_H3cLIStreamPackets_Type())
h3cLIStreamPackets.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cLIStreamPackets.setStatus(_A)
_H3cLIStreamDrops_Type=Counter32
_H3cLIStreamDrops_Object=MibTableColumn
h3cLIStreamDrops=_H3cLIStreamDrops_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,3,1,5),_H3cLIStreamDrops_Type())
h3cLIStreamDrops.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cLIStreamDrops.setStatus(_A)
_H3cLIStreamHPackets_Type=Counter64
_H3cLIStreamHPackets_Object=MibTableColumn
h3cLIStreamHPackets=_H3cLIStreamHPackets_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,3,1,6),_H3cLIStreamHPackets_Type())
h3cLIStreamHPackets.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cLIStreamHPackets.setStatus(_A)
_H3cLIStreamHDrops_Type=Counter64
_H3cLIStreamHDrops_Object=MibTableColumn
h3cLIStreamHDrops=_H3cLIStreamHDrops_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,3,1,7),_H3cLIStreamHDrops_Type())
h3cLIStreamHDrops.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cLIStreamHDrops.setStatus(_A)
_H3cLIStreamRowStatus_Type=RowStatus
_H3cLIStreamRowStatus_Object=MibTableColumn
h3cLIStreamRowStatus=_H3cLIStreamRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,111,1,3,3,1,8),_H3cLIStreamRowStatus_Type())
h3cLIStreamRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cLIStreamRowStatus.setStatus(_A)
_H3cLIIPStream_ObjectIdentity=ObjectIdentity
h3cLIIPStream=_H3cLIIPStream_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,111,2))
_H3cLIIPStreamObjects_ObjectIdentity=ObjectIdentity
h3cLIIPStreamObjects=_H3cLIIPStreamObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,111,2,1))
_H3cLIIPStreamTable_Object=MibTable
h3cLIIPStreamTable=_H3cLIIPStreamTable_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1))
if mibBuilder.loadTexts:h3cLIIPStreamTable.setStatus(_A)
_H3cLIIPStreamEntry_Object=MibTableRow
h3cLIIPStreamEntry=_H3cLIIPStreamEntry_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1))
h3cLIIPStreamEntry.setIndexNames((0,_C,_E),(0,_C,_I))
if mibBuilder.loadTexts:h3cLIIPStreamEntry.setStatus(_A)
_H3cLIIPStreamInterface_Type=InterfaceIndexOrZero
_H3cLIIPStreamInterface_Object=MibTableColumn
h3cLIIPStreamInterface=_H3cLIIPStreamInterface_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1,1),_H3cLIIPStreamInterface_Type())
h3cLIIPStreamInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIIPStreamInterface.setStatus(_A)
class _H3cLIIPStreamAddrType_Type(InetAddressType):defaultValue=1
_H3cLIIPStreamAddrType_Type.__name__=_O
_H3cLIIPStreamAddrType_Object=MibTableColumn
h3cLIIPStreamAddrType=_H3cLIIPStreamAddrType_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1,2),_H3cLIIPStreamAddrType_Type())
h3cLIIPStreamAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIIPStreamAddrType.setStatus(_A)
class _H3cLIIPStreamDestAddr_Type(InetAddress):defaultHexValue=_R
_H3cLIIPStreamDestAddr_Type.__name__=_J
_H3cLIIPStreamDestAddr_Object=MibTableColumn
h3cLIIPStreamDestAddr=_H3cLIIPStreamDestAddr_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1,3),_H3cLIIPStreamDestAddr_Type())
h3cLIIPStreamDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIIPStreamDestAddr.setStatus(_A)
class _H3cLIIPStreamDestAddrLength_Type(InetAddressPrefixLength):defaultValue=0
_H3cLIIPStreamDestAddrLength_Type.__name__=_K
_H3cLIIPStreamDestAddrLength_Object=MibTableColumn
h3cLIIPStreamDestAddrLength=_H3cLIIPStreamDestAddrLength_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1,4),_H3cLIIPStreamDestAddrLength_Type())
h3cLIIPStreamDestAddrLength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIIPStreamDestAddrLength.setStatus(_A)
class _H3cLIIPStreamSrcAddr_Type(InetAddress):defaultHexValue=_R
_H3cLIIPStreamSrcAddr_Type.__name__=_J
_H3cLIIPStreamSrcAddr_Object=MibTableColumn
h3cLIIPStreamSrcAddr=_H3cLIIPStreamSrcAddr_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1,5),_H3cLIIPStreamSrcAddr_Type())
h3cLIIPStreamSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIIPStreamSrcAddr.setStatus(_A)
class _H3cLIIPStreamSrcAddrLength_Type(InetAddressPrefixLength):defaultValue=0
_H3cLIIPStreamSrcAddrLength_Type.__name__=_K
_H3cLIIPStreamSrcAddrLength_Object=MibTableColumn
h3cLIIPStreamSrcAddrLength=_H3cLIIPStreamSrcAddrLength_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1,6),_H3cLIIPStreamSrcAddrLength_Type())
h3cLIIPStreamSrcAddrLength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIIPStreamSrcAddrLength.setStatus(_A)
class _H3cLIIPStreamTosByte_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cLIIPStreamTosByte_Type.__name__=_D
_H3cLIIPStreamTosByte_Object=MibTableColumn
h3cLIIPStreamTosByte=_H3cLIIPStreamTosByte_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1,7),_H3cLIIPStreamTosByte_Type())
h3cLIIPStreamTosByte.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIIPStreamTosByte.setStatus(_A)
class _H3cLIIPStreamTosByteMask_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cLIIPStreamTosByteMask_Type.__name__=_D
_H3cLIIPStreamTosByteMask_Object=MibTableColumn
h3cLIIPStreamTosByteMask=_H3cLIIPStreamTosByteMask_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1,8),_H3cLIIPStreamTosByteMask_Type())
h3cLIIPStreamTosByteMask.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIIPStreamTosByteMask.setStatus(_A)
class _H3cLIIPStreamFlowId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,1048575))
_H3cLIIPStreamFlowId_Type.__name__=_D
_H3cLIIPStreamFlowId_Object=MibTableColumn
h3cLIIPStreamFlowId=_H3cLIIPStreamFlowId_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1,9),_H3cLIIPStreamFlowId_Type())
h3cLIIPStreamFlowId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIIPStreamFlowId.setStatus(_A)
class _H3cLIIPStreamProtocol_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_H3cLIIPStreamProtocol_Type.__name__=_D
_H3cLIIPStreamProtocol_Object=MibTableColumn
h3cLIIPStreamProtocol=_H3cLIIPStreamProtocol_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1,10),_H3cLIIPStreamProtocol_Type())
h3cLIIPStreamProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIIPStreamProtocol.setStatus(_A)
class _H3cLIIPStreamDestL4PortMin_Type(InetPortNumber):defaultValue=0
_H3cLIIPStreamDestL4PortMin_Type.__name__=_F
_H3cLIIPStreamDestL4PortMin_Object=MibTableColumn
h3cLIIPStreamDestL4PortMin=_H3cLIIPStreamDestL4PortMin_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1,11),_H3cLIIPStreamDestL4PortMin_Type())
h3cLIIPStreamDestL4PortMin.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIIPStreamDestL4PortMin.setStatus(_A)
class _H3cLIIPStreamDestL4PortMax_Type(InetPortNumber):defaultValue=65535
_H3cLIIPStreamDestL4PortMax_Type.__name__=_F
_H3cLIIPStreamDestL4PortMax_Object=MibTableColumn
h3cLIIPStreamDestL4PortMax=_H3cLIIPStreamDestL4PortMax_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1,12),_H3cLIIPStreamDestL4PortMax_Type())
h3cLIIPStreamDestL4PortMax.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIIPStreamDestL4PortMax.setStatus(_A)
class _H3cLIIPStreamSrcL4PortMin_Type(InetPortNumber):defaultValue=0
_H3cLIIPStreamSrcL4PortMin_Type.__name__=_F
_H3cLIIPStreamSrcL4PortMin_Object=MibTableColumn
h3cLIIPStreamSrcL4PortMin=_H3cLIIPStreamSrcL4PortMin_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1,13),_H3cLIIPStreamSrcL4PortMin_Type())
h3cLIIPStreamSrcL4PortMin.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIIPStreamSrcL4PortMin.setStatus(_A)
class _H3cLIIPStreamSrcL4PortMax_Type(InetPortNumber):defaultValue=65535
_H3cLIIPStreamSrcL4PortMax_Type.__name__=_F
_H3cLIIPStreamSrcL4PortMax_Object=MibTableColumn
h3cLIIPStreamSrcL4PortMax=_H3cLIIPStreamSrcL4PortMax_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1,14),_H3cLIIPStreamSrcL4PortMax_Type())
h3cLIIPStreamSrcL4PortMax.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIIPStreamSrcL4PortMax.setStatus(_A)
class _H3cLIIPStreamVRF_Type(SnmpAdminString):defaultValue=OctetString('')
_H3cLIIPStreamVRF_Type.__name__=_P
_H3cLIIPStreamVRF_Object=MibTableColumn
h3cLIIPStreamVRF=_H3cLIIPStreamVRF_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1,15),_H3cLIIPStreamVRF_Type())
h3cLIIPStreamVRF.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIIPStreamVRF.setStatus(_A)
_H3cLIIPStreamRowStatus_Type=RowStatus
_H3cLIIPStreamRowStatus_Object=MibTableColumn
h3cLIIPStreamRowStatus=_H3cLIIPStreamRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,111,2,1,1,1,18),_H3cLIIPStreamRowStatus_Type())
h3cLIIPStreamRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cLIIPStreamRowStatus.setStatus(_A)
_H3cLIMACStream_ObjectIdentity=ObjectIdentity
h3cLIMACStream=_H3cLIMACStream_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,111,3))
_H3cLIMACStreamObjects_ObjectIdentity=ObjectIdentity
h3cLIMACStreamObjects=_H3cLIMACStreamObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,111,3,1))
_H3cLIMACStreamTable_Object=MibTable
h3cLIMACStreamTable=_H3cLIMACStreamTable_Object((1,3,6,1,4,1,43,45,1,10,2,111,3,1,1))
if mibBuilder.loadTexts:h3cLIMACStreamTable.setStatus(_A)
_H3cLIMACStreamEntry_Object=MibTableRow
h3cLIMACStreamEntry=_H3cLIMACStreamEntry_Object((1,3,6,1,4,1,43,45,1,10,2,111,3,1,1,1))
h3cLIMACStreamEntry.setIndexNames((0,_C,_E),(0,_C,_I))
if mibBuilder.loadTexts:h3cLIMACStreamEntry.setStatus(_A)
class _H3cLIMACStreamFields_Type(Bits):namedValues=NamedValues(*(('interface',0),('dstMacAddress',1),('srcMacAddress',2),('ethernetPid',3),('dSap',4),('sSap',5)))
_H3cLIMACStreamFields_Type.__name__='Bits'
_H3cLIMACStreamFields_Object=MibTableColumn
h3cLIMACStreamFields=_H3cLIMACStreamFields_Object((1,3,6,1,4,1,43,45,1,10,2,111,3,1,1,1,1),_H3cLIMACStreamFields_Type())
h3cLIMACStreamFields.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIMACStreamFields.setStatus(_A)
_H3cLIMACStreamInterface_Type=InterfaceIndexOrZero
_H3cLIMACStreamInterface_Object=MibTableColumn
h3cLIMACStreamInterface=_H3cLIMACStreamInterface_Object((1,3,6,1,4,1,43,45,1,10,2,111,3,1,1,1,2),_H3cLIMACStreamInterface_Type())
h3cLIMACStreamInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIMACStreamInterface.setStatus(_A)
_H3cLIMACStreamDestAddr_Type=MacAddress
_H3cLIMACStreamDestAddr_Object=MibTableColumn
h3cLIMACStreamDestAddr=_H3cLIMACStreamDestAddr_Object((1,3,6,1,4,1,43,45,1,10,2,111,3,1,1,1,3),_H3cLIMACStreamDestAddr_Type())
h3cLIMACStreamDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIMACStreamDestAddr.setStatus(_A)
_H3cLIMACStreamSrcAddr_Type=MacAddress
_H3cLIMACStreamSrcAddr_Object=MibTableColumn
h3cLIMACStreamSrcAddr=_H3cLIMACStreamSrcAddr_Object((1,3,6,1,4,1,43,45,1,10,2,111,3,1,1,1,4),_H3cLIMACStreamSrcAddr_Type())
h3cLIMACStreamSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIMACStreamSrcAddr.setStatus(_A)
_H3cLIMACStreamEthPid_Type=Unsigned32
_H3cLIMACStreamEthPid_Object=MibTableColumn
h3cLIMACStreamEthPid=_H3cLIMACStreamEthPid_Object((1,3,6,1,4,1,43,45,1,10,2,111,3,1,1,1,5),_H3cLIMACStreamEthPid_Type())
h3cLIMACStreamEthPid.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIMACStreamEthPid.setStatus(_A)
_H3cLIMACStreamDSap_Type=Unsigned32
_H3cLIMACStreamDSap_Object=MibTableColumn
h3cLIMACStreamDSap=_H3cLIMACStreamDSap_Object((1,3,6,1,4,1,43,45,1,10,2,111,3,1,1,1,6),_H3cLIMACStreamDSap_Type())
h3cLIMACStreamDSap.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIMACStreamDSap.setStatus(_A)
_H3cLIMACStreamSSap_Type=Unsigned32
_H3cLIMACStreamSSap_Object=MibTableColumn
h3cLIMACStreamSSap=_H3cLIMACStreamSSap_Object((1,3,6,1,4,1,43,45,1,10,2,111,3,1,1,1,7),_H3cLIMACStreamSSap_Type())
h3cLIMACStreamSSap.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIMACStreamSSap.setStatus(_A)
_H3cLIMACStreamRowStatus_Type=RowStatus
_H3cLIMACStreamRowStatus_Object=MibTableColumn
h3cLIMACStreamRowStatus=_H3cLIMACStreamRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,111,3,1,1,1,8),_H3cLIMACStreamRowStatus_Type())
h3cLIMACStreamRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cLIMACStreamRowStatus.setStatus(_A)
_H3cLIUserStream_ObjectIdentity=ObjectIdentity
h3cLIUserStream=_H3cLIUserStream_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,111,4))
_H3cLIUserStreamObjects_ObjectIdentity=ObjectIdentity
h3cLIUserStreamObjects=_H3cLIUserStreamObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,111,4,1))
_H3cLIUserStreamTable_Object=MibTable
h3cLIUserStreamTable=_H3cLIUserStreamTable_Object((1,3,6,1,4,1,43,45,1,10,2,111,4,1,1))
if mibBuilder.loadTexts:h3cLIUserStreamTable.setStatus(_A)
_H3cLIUserStreamEntry_Object=MibTableRow
h3cLIUserStreamEntry=_H3cLIUserStreamEntry_Object((1,3,6,1,4,1,43,45,1,10,2,111,4,1,1,1))
h3cLIUserStreamEntry.setIndexNames((0,_C,_E),(0,_C,_I))
if mibBuilder.loadTexts:h3cLIUserStreamEntry.setStatus(_A)
class _H3cLIUserStreamAcctSessID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,253))
_H3cLIUserStreamAcctSessID_Type.__name__=_N
_H3cLIUserStreamAcctSessID_Object=MibTableColumn
h3cLIUserStreamAcctSessID=_H3cLIUserStreamAcctSessID_Object((1,3,6,1,4,1,43,45,1,10,2,111,4,1,1,1,1),_H3cLIUserStreamAcctSessID_Type())
h3cLIUserStreamAcctSessID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLIUserStreamAcctSessID.setStatus(_A)
_H3cLIUserStreamRowStatus_Type=RowStatus
_H3cLIUserStreamRowStatus_Object=MibTableColumn
h3cLIUserStreamRowStatus=_H3cLIUserStreamRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,111,4,1,1,1,2),_H3cLIUserStreamRowStatus_Type())
h3cLIUserStreamRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cLIUserStreamRowStatus.setStatus(_A)
h3cLIActive=NotificationType((1,3,6,1,4,1,43,45,1,10,2,111,1,2,0,1))
h3cLIActive.setObjects((_C,_M))
if mibBuilder.loadTexts:h3cLIActive.setStatus(_A)
h3cLITimeOut=NotificationType((1,3,6,1,4,1,43,45,1,10,2,111,1,2,0,2))
h3cLITimeOut.setObjects((_C,_S))
if mibBuilder.loadTexts:h3cLITimeOut.setStatus(_A)
h3cLIFailureInformation=NotificationType((1,3,6,1,4,1,43,45,1,10,2,111,1,2,0,3))
h3cLIFailureInformation.setObjects(*((_C,_M),(_C,_T)))
if mibBuilder.loadTexts:h3cLIFailureInformation.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3cLI':h3cLI,'h3cLICommon':h3cLICommon,'h3cLITrapBindObjects':h3cLITrapBindObjects,_T:h3cLIBoardInformation,'h3cLINotifications':h3cLINotifications,'h3cLINotificationsPrefix':h3cLINotificationsPrefix,'h3cLIActive':h3cLIActive,'h3cLITimeOut':h3cLITimeOut,'h3cLIFailureInformation':h3cLIFailureInformation,'h3cLIObjects':h3cLIObjects,'h3cLINewIndex':h3cLINewIndex,'h3cLIMediationTable':h3cLIMediationTable,'h3cLIMediationEntry':h3cLIMediationEntry,_E:h3cLIMediationIndex,'h3cLIMediationDestAddrType':h3cLIMediationDestAddrType,'h3cLIMediationDestAddr':h3cLIMediationDestAddr,'h3cLIMediationDestPort':h3cLIMediationDestPort,'h3cLIMediationSrcInterface':h3cLIMediationSrcInterface,'h3cLIMediationDscp':h3cLIMediationDscp,'h3cLIMediationTimeOut':h3cLIMediationTimeOut,'h3cLIMediationTransport':h3cLIMediationTransport,'h3cLIMediationNotificationEnable':h3cLIMediationNotificationEnable,_S:h3cLIMediationRowStatus,'h3cLIStreamTable':h3cLIStreamTable,'h3cLIStreamEntry':h3cLIStreamEntry,_I:h3cLIStreamIndex,_M:h3cLIStreamtype,'h3cLIStreamEnable':h3cLIStreamEnable,'h3cLIStreamPackets':h3cLIStreamPackets,'h3cLIStreamDrops':h3cLIStreamDrops,'h3cLIStreamHPackets':h3cLIStreamHPackets,'h3cLIStreamHDrops':h3cLIStreamHDrops,'h3cLIStreamRowStatus':h3cLIStreamRowStatus,'h3cLIIPStream':h3cLIIPStream,'h3cLIIPStreamObjects':h3cLIIPStreamObjects,'h3cLIIPStreamTable':h3cLIIPStreamTable,'h3cLIIPStreamEntry':h3cLIIPStreamEntry,'h3cLIIPStreamInterface':h3cLIIPStreamInterface,'h3cLIIPStreamAddrType':h3cLIIPStreamAddrType,'h3cLIIPStreamDestAddr':h3cLIIPStreamDestAddr,'h3cLIIPStreamDestAddrLength':h3cLIIPStreamDestAddrLength,'h3cLIIPStreamSrcAddr':h3cLIIPStreamSrcAddr,'h3cLIIPStreamSrcAddrLength':h3cLIIPStreamSrcAddrLength,'h3cLIIPStreamTosByte':h3cLIIPStreamTosByte,'h3cLIIPStreamTosByteMask':h3cLIIPStreamTosByteMask,'h3cLIIPStreamFlowId':h3cLIIPStreamFlowId,'h3cLIIPStreamProtocol':h3cLIIPStreamProtocol,'h3cLIIPStreamDestL4PortMin':h3cLIIPStreamDestL4PortMin,'h3cLIIPStreamDestL4PortMax':h3cLIIPStreamDestL4PortMax,'h3cLIIPStreamSrcL4PortMin':h3cLIIPStreamSrcL4PortMin,'h3cLIIPStreamSrcL4PortMax':h3cLIIPStreamSrcL4PortMax,'h3cLIIPStreamVRF':h3cLIIPStreamVRF,'h3cLIIPStreamRowStatus':h3cLIIPStreamRowStatus,'h3cLIMACStream':h3cLIMACStream,'h3cLIMACStreamObjects':h3cLIMACStreamObjects,'h3cLIMACStreamTable':h3cLIMACStreamTable,'h3cLIMACStreamEntry':h3cLIMACStreamEntry,'h3cLIMACStreamFields':h3cLIMACStreamFields,'h3cLIMACStreamInterface':h3cLIMACStreamInterface,'h3cLIMACStreamDestAddr':h3cLIMACStreamDestAddr,'h3cLIMACStreamSrcAddr':h3cLIMACStreamSrcAddr,'h3cLIMACStreamEthPid':h3cLIMACStreamEthPid,'h3cLIMACStreamDSap':h3cLIMACStreamDSap,'h3cLIMACStreamSSap':h3cLIMACStreamSSap,'h3cLIMACStreamRowStatus':h3cLIMACStreamRowStatus,'h3cLIUserStream':h3cLIUserStream,'h3cLIUserStreamObjects':h3cLIUserStreamObjects,'h3cLIUserStreamTable':h3cLIUserStreamTable,'h3cLIUserStreamEntry':h3cLIUserStreamEntry,'h3cLIUserStreamAcctSessID':h3cLIUserStreamAcctSessID,'h3cLIUserStreamRowStatus':h3cLIUserStreamRowStatus})