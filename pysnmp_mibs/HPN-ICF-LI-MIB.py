_T='hpnicfLIBoardInformation'
_S='hpnicfLIMediationRowStatus'
_R='00000000'
_Q='not-accessible'
_P='SnmpAdminString'
_O='InetAddressType'
_N='OctetString'
_M='hpnicfLIStreamtype'
_L='TruthValue'
_K='InetAddressPrefixLength'
_J='InetAddress'
_I='hpnicfLIStreamIndex'
_H='read-create'
_G='read-only'
_F='InetPortNumber'
_E='hpnicfLIMediationIndex'
_D='Integer32'
_C='HPN-ICF-LI-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_J,_K,_O,_F)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_P)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_L)
hpnicfLI=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,111))
if mibBuilder.loadTexts:hpnicfLI.setRevisions(('2009-08-25 10:00',))
_HpnicfLICommon_ObjectIdentity=ObjectIdentity
hpnicfLICommon=_HpnicfLICommon_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,111,1))
_HpnicfLITrapBindObjects_ObjectIdentity=ObjectIdentity
hpnicfLITrapBindObjects=_HpnicfLITrapBindObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,111,1,1))
_HpnicfLIBoardInformation_Type=Unsigned32
_HpnicfLIBoardInformation_Object=MibScalar
hpnicfLIBoardInformation=_HpnicfLIBoardInformation_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,1,1),_HpnicfLIBoardInformation_Type())
hpnicfLIBoardInformation.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hpnicfLIBoardInformation.setStatus(_A)
_HpnicfLINotifications_ObjectIdentity=ObjectIdentity
hpnicfLINotifications=_HpnicfLINotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,111,1,2))
_HpnicfLINotificationsPrefix_ObjectIdentity=ObjectIdentity
hpnicfLINotificationsPrefix=_HpnicfLINotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,111,1,2,0))
_HpnicfLIObjects_ObjectIdentity=ObjectIdentity
hpnicfLIObjects=_HpnicfLIObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3))
class _HpnicfLINewIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfLINewIndex_Type.__name__=_D
_HpnicfLINewIndex_Object=MibScalar
hpnicfLINewIndex=_HpnicfLINewIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,1),_HpnicfLINewIndex_Type())
hpnicfLINewIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfLINewIndex.setStatus(_A)
_HpnicfLIMediationTable_Object=MibTable
hpnicfLIMediationTable=_HpnicfLIMediationTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,2))
if mibBuilder.loadTexts:hpnicfLIMediationTable.setStatus(_A)
_HpnicfLIMediationEntry_Object=MibTableRow
hpnicfLIMediationEntry=_HpnicfLIMediationEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,2,1))
hpnicfLIMediationEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:hpnicfLIMediationEntry.setStatus(_A)
class _HpnicfLIMediationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfLIMediationIndex_Type.__name__=_D
_HpnicfLIMediationIndex_Object=MibTableColumn
hpnicfLIMediationIndex=_HpnicfLIMediationIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,2,1,1),_HpnicfLIMediationIndex_Type())
hpnicfLIMediationIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:hpnicfLIMediationIndex.setStatus(_A)
_HpnicfLIMediationDestAddrType_Type=InetAddressType
_HpnicfLIMediationDestAddrType_Object=MibTableColumn
hpnicfLIMediationDestAddrType=_HpnicfLIMediationDestAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,2,1,2),_HpnicfLIMediationDestAddrType_Type())
hpnicfLIMediationDestAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIMediationDestAddrType.setStatus(_A)
_HpnicfLIMediationDestAddr_Type=InetAddress
_HpnicfLIMediationDestAddr_Object=MibTableColumn
hpnicfLIMediationDestAddr=_HpnicfLIMediationDestAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,2,1,3),_HpnicfLIMediationDestAddr_Type())
hpnicfLIMediationDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIMediationDestAddr.setStatus(_A)
_HpnicfLIMediationDestPort_Type=InetPortNumber
_HpnicfLIMediationDestPort_Object=MibTableColumn
hpnicfLIMediationDestPort=_HpnicfLIMediationDestPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,2,1,4),_HpnicfLIMediationDestPort_Type())
hpnicfLIMediationDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIMediationDestPort.setStatus(_A)
_HpnicfLIMediationSrcInterface_Type=InterfaceIndexOrZero
_HpnicfLIMediationSrcInterface_Object=MibTableColumn
hpnicfLIMediationSrcInterface=_HpnicfLIMediationSrcInterface_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,2,1,5),_HpnicfLIMediationSrcInterface_Type())
hpnicfLIMediationSrcInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIMediationSrcInterface.setStatus(_A)
class _HpnicfLIMediationDscp_Type(Integer32):defaultValue=34
_HpnicfLIMediationDscp_Type.__name__=_D
_HpnicfLIMediationDscp_Object=MibTableColumn
hpnicfLIMediationDscp=_HpnicfLIMediationDscp_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,2,1,6),_HpnicfLIMediationDscp_Type())
hpnicfLIMediationDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIMediationDscp.setStatus(_A)
_HpnicfLIMediationTimeOut_Type=DateAndTime
_HpnicfLIMediationTimeOut_Object=MibTableColumn
hpnicfLIMediationTimeOut=_HpnicfLIMediationTimeOut_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,2,1,7),_HpnicfLIMediationTimeOut_Type())
hpnicfLIMediationTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIMediationTimeOut.setStatus(_A)
class _HpnicfLIMediationTransport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('udp',1))
_HpnicfLIMediationTransport_Type.__name__=_D
_HpnicfLIMediationTransport_Object=MibTableColumn
hpnicfLIMediationTransport=_HpnicfLIMediationTransport_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,2,1,8),_HpnicfLIMediationTransport_Type())
hpnicfLIMediationTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIMediationTransport.setStatus(_A)
class _HpnicfLIMediationNotificationEnable_Type(TruthValue):defaultValue=1
_HpnicfLIMediationNotificationEnable_Type.__name__=_L
_HpnicfLIMediationNotificationEnable_Object=MibTableColumn
hpnicfLIMediationNotificationEnable=_HpnicfLIMediationNotificationEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,2,1,9),_HpnicfLIMediationNotificationEnable_Type())
hpnicfLIMediationNotificationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIMediationNotificationEnable.setStatus(_A)
_HpnicfLIMediationRowStatus_Type=RowStatus
_HpnicfLIMediationRowStatus_Object=MibTableColumn
hpnicfLIMediationRowStatus=_HpnicfLIMediationRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,2,1,10),_HpnicfLIMediationRowStatus_Type())
hpnicfLIMediationRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfLIMediationRowStatus.setStatus(_A)
_HpnicfLIStreamTable_Object=MibTable
hpnicfLIStreamTable=_HpnicfLIStreamTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,3))
if mibBuilder.loadTexts:hpnicfLIStreamTable.setStatus(_A)
_HpnicfLIStreamEntry_Object=MibTableRow
hpnicfLIStreamEntry=_HpnicfLIStreamEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,3,1))
hpnicfLIStreamEntry.setIndexNames((0,_C,_E),(0,_C,_I))
if mibBuilder.loadTexts:hpnicfLIStreamEntry.setStatus(_A)
class _HpnicfLIStreamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfLIStreamIndex_Type.__name__=_D
_HpnicfLIStreamIndex_Object=MibTableColumn
hpnicfLIStreamIndex=_HpnicfLIStreamIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,3,1,1),_HpnicfLIStreamIndex_Type())
hpnicfLIStreamIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:hpnicfLIStreamIndex.setStatus(_A)
class _HpnicfLIStreamtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ip',1),('mac',2),('userConnection',3)))
_HpnicfLIStreamtype_Type.__name__=_D
_HpnicfLIStreamtype_Object=MibTableColumn
hpnicfLIStreamtype=_HpnicfLIStreamtype_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,3,1,2),_HpnicfLIStreamtype_Type())
hpnicfLIStreamtype.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIStreamtype.setStatus(_A)
class _HpnicfLIStreamEnable_Type(TruthValue):defaultValue=2
_HpnicfLIStreamEnable_Type.__name__=_L
_HpnicfLIStreamEnable_Object=MibTableColumn
hpnicfLIStreamEnable=_HpnicfLIStreamEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,3,1,3),_HpnicfLIStreamEnable_Type())
hpnicfLIStreamEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIStreamEnable.setStatus(_A)
_HpnicfLIStreamPackets_Type=Counter32
_HpnicfLIStreamPackets_Object=MibTableColumn
hpnicfLIStreamPackets=_HpnicfLIStreamPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,3,1,4),_HpnicfLIStreamPackets_Type())
hpnicfLIStreamPackets.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfLIStreamPackets.setStatus(_A)
_HpnicfLIStreamDrops_Type=Counter32
_HpnicfLIStreamDrops_Object=MibTableColumn
hpnicfLIStreamDrops=_HpnicfLIStreamDrops_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,3,1,5),_HpnicfLIStreamDrops_Type())
hpnicfLIStreamDrops.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfLIStreamDrops.setStatus(_A)
_HpnicfLIStreamHPackets_Type=Counter64
_HpnicfLIStreamHPackets_Object=MibTableColumn
hpnicfLIStreamHPackets=_HpnicfLIStreamHPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,3,1,6),_HpnicfLIStreamHPackets_Type())
hpnicfLIStreamHPackets.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfLIStreamHPackets.setStatus(_A)
_HpnicfLIStreamHDrops_Type=Counter64
_HpnicfLIStreamHDrops_Object=MibTableColumn
hpnicfLIStreamHDrops=_HpnicfLIStreamHDrops_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,3,1,7),_HpnicfLIStreamHDrops_Type())
hpnicfLIStreamHDrops.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfLIStreamHDrops.setStatus(_A)
_HpnicfLIStreamRowStatus_Type=RowStatus
_HpnicfLIStreamRowStatus_Object=MibTableColumn
hpnicfLIStreamRowStatus=_HpnicfLIStreamRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,1,3,3,1,8),_HpnicfLIStreamRowStatus_Type())
hpnicfLIStreamRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfLIStreamRowStatus.setStatus(_A)
_HpnicfLIIPStream_ObjectIdentity=ObjectIdentity
hpnicfLIIPStream=_HpnicfLIIPStream_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,111,2))
_HpnicfLIIPStreamObjects_ObjectIdentity=ObjectIdentity
hpnicfLIIPStreamObjects=_HpnicfLIIPStreamObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1))
_HpnicfLIIPStreamTable_Object=MibTable
hpnicfLIIPStreamTable=_HpnicfLIIPStreamTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1))
if mibBuilder.loadTexts:hpnicfLIIPStreamTable.setStatus(_A)
_HpnicfLIIPStreamEntry_Object=MibTableRow
hpnicfLIIPStreamEntry=_HpnicfLIIPStreamEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1))
hpnicfLIIPStreamEntry.setIndexNames((0,_C,_E),(0,_C,_I))
if mibBuilder.loadTexts:hpnicfLIIPStreamEntry.setStatus(_A)
_HpnicfLIIPStreamInterface_Type=InterfaceIndexOrZero
_HpnicfLIIPStreamInterface_Object=MibTableColumn
hpnicfLIIPStreamInterface=_HpnicfLIIPStreamInterface_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1,1),_HpnicfLIIPStreamInterface_Type())
hpnicfLIIPStreamInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIIPStreamInterface.setStatus(_A)
class _HpnicfLIIPStreamAddrType_Type(InetAddressType):defaultValue=1
_HpnicfLIIPStreamAddrType_Type.__name__=_O
_HpnicfLIIPStreamAddrType_Object=MibTableColumn
hpnicfLIIPStreamAddrType=_HpnicfLIIPStreamAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1,2),_HpnicfLIIPStreamAddrType_Type())
hpnicfLIIPStreamAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIIPStreamAddrType.setStatus(_A)
class _HpnicfLIIPStreamDestAddr_Type(InetAddress):defaultHexValue=_R
_HpnicfLIIPStreamDestAddr_Type.__name__=_J
_HpnicfLIIPStreamDestAddr_Object=MibTableColumn
hpnicfLIIPStreamDestAddr=_HpnicfLIIPStreamDestAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1,3),_HpnicfLIIPStreamDestAddr_Type())
hpnicfLIIPStreamDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIIPStreamDestAddr.setStatus(_A)
class _HpnicfLIIPStreamDestAddrLength_Type(InetAddressPrefixLength):defaultValue=0
_HpnicfLIIPStreamDestAddrLength_Type.__name__=_K
_HpnicfLIIPStreamDestAddrLength_Object=MibTableColumn
hpnicfLIIPStreamDestAddrLength=_HpnicfLIIPStreamDestAddrLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1,4),_HpnicfLIIPStreamDestAddrLength_Type())
hpnicfLIIPStreamDestAddrLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIIPStreamDestAddrLength.setStatus(_A)
class _HpnicfLIIPStreamSrcAddr_Type(InetAddress):defaultHexValue=_R
_HpnicfLIIPStreamSrcAddr_Type.__name__=_J
_HpnicfLIIPStreamSrcAddr_Object=MibTableColumn
hpnicfLIIPStreamSrcAddr=_HpnicfLIIPStreamSrcAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1,5),_HpnicfLIIPStreamSrcAddr_Type())
hpnicfLIIPStreamSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIIPStreamSrcAddr.setStatus(_A)
class _HpnicfLIIPStreamSrcAddrLength_Type(InetAddressPrefixLength):defaultValue=0
_HpnicfLIIPStreamSrcAddrLength_Type.__name__=_K
_HpnicfLIIPStreamSrcAddrLength_Object=MibTableColumn
hpnicfLIIPStreamSrcAddrLength=_HpnicfLIIPStreamSrcAddrLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1,6),_HpnicfLIIPStreamSrcAddrLength_Type())
hpnicfLIIPStreamSrcAddrLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIIPStreamSrcAddrLength.setStatus(_A)
class _HpnicfLIIPStreamTosByte_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfLIIPStreamTosByte_Type.__name__=_D
_HpnicfLIIPStreamTosByte_Object=MibTableColumn
hpnicfLIIPStreamTosByte=_HpnicfLIIPStreamTosByte_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1,7),_HpnicfLIIPStreamTosByte_Type())
hpnicfLIIPStreamTosByte.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIIPStreamTosByte.setStatus(_A)
class _HpnicfLIIPStreamTosByteMask_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfLIIPStreamTosByteMask_Type.__name__=_D
_HpnicfLIIPStreamTosByteMask_Object=MibTableColumn
hpnicfLIIPStreamTosByteMask=_HpnicfLIIPStreamTosByteMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1,8),_HpnicfLIIPStreamTosByteMask_Type())
hpnicfLIIPStreamTosByteMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIIPStreamTosByteMask.setStatus(_A)
class _HpnicfLIIPStreamFlowId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,1048575))
_HpnicfLIIPStreamFlowId_Type.__name__=_D
_HpnicfLIIPStreamFlowId_Object=MibTableColumn
hpnicfLIIPStreamFlowId=_HpnicfLIIPStreamFlowId_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1,9),_HpnicfLIIPStreamFlowId_Type())
hpnicfLIIPStreamFlowId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIIPStreamFlowId.setStatus(_A)
class _HpnicfLIIPStreamProtocol_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_HpnicfLIIPStreamProtocol_Type.__name__=_D
_HpnicfLIIPStreamProtocol_Object=MibTableColumn
hpnicfLIIPStreamProtocol=_HpnicfLIIPStreamProtocol_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1,10),_HpnicfLIIPStreamProtocol_Type())
hpnicfLIIPStreamProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIIPStreamProtocol.setStatus(_A)
class _HpnicfLIIPStreamDestL4PortMin_Type(InetPortNumber):defaultValue=0
_HpnicfLIIPStreamDestL4PortMin_Type.__name__=_F
_HpnicfLIIPStreamDestL4PortMin_Object=MibTableColumn
hpnicfLIIPStreamDestL4PortMin=_HpnicfLIIPStreamDestL4PortMin_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1,11),_HpnicfLIIPStreamDestL4PortMin_Type())
hpnicfLIIPStreamDestL4PortMin.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIIPStreamDestL4PortMin.setStatus(_A)
class _HpnicfLIIPStreamDestL4PortMax_Type(InetPortNumber):defaultValue=65535
_HpnicfLIIPStreamDestL4PortMax_Type.__name__=_F
_HpnicfLIIPStreamDestL4PortMax_Object=MibTableColumn
hpnicfLIIPStreamDestL4PortMax=_HpnicfLIIPStreamDestL4PortMax_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1,12),_HpnicfLIIPStreamDestL4PortMax_Type())
hpnicfLIIPStreamDestL4PortMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIIPStreamDestL4PortMax.setStatus(_A)
class _HpnicfLIIPStreamSrcL4PortMin_Type(InetPortNumber):defaultValue=0
_HpnicfLIIPStreamSrcL4PortMin_Type.__name__=_F
_HpnicfLIIPStreamSrcL4PortMin_Object=MibTableColumn
hpnicfLIIPStreamSrcL4PortMin=_HpnicfLIIPStreamSrcL4PortMin_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1,13),_HpnicfLIIPStreamSrcL4PortMin_Type())
hpnicfLIIPStreamSrcL4PortMin.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIIPStreamSrcL4PortMin.setStatus(_A)
class _HpnicfLIIPStreamSrcL4PortMax_Type(InetPortNumber):defaultValue=65535
_HpnicfLIIPStreamSrcL4PortMax_Type.__name__=_F
_HpnicfLIIPStreamSrcL4PortMax_Object=MibTableColumn
hpnicfLIIPStreamSrcL4PortMax=_HpnicfLIIPStreamSrcL4PortMax_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1,14),_HpnicfLIIPStreamSrcL4PortMax_Type())
hpnicfLIIPStreamSrcL4PortMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIIPStreamSrcL4PortMax.setStatus(_A)
class _HpnicfLIIPStreamVRF_Type(SnmpAdminString):defaultValue=OctetString('')
_HpnicfLIIPStreamVRF_Type.__name__=_P
_HpnicfLIIPStreamVRF_Object=MibTableColumn
hpnicfLIIPStreamVRF=_HpnicfLIIPStreamVRF_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1,15),_HpnicfLIIPStreamVRF_Type())
hpnicfLIIPStreamVRF.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIIPStreamVRF.setStatus(_A)
_HpnicfLIIPStreamRowStatus_Type=RowStatus
_HpnicfLIIPStreamRowStatus_Object=MibTableColumn
hpnicfLIIPStreamRowStatus=_HpnicfLIIPStreamRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,2,1,1,1,18),_HpnicfLIIPStreamRowStatus_Type())
hpnicfLIIPStreamRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfLIIPStreamRowStatus.setStatus(_A)
_HpnicfLIMACStream_ObjectIdentity=ObjectIdentity
hpnicfLIMACStream=_HpnicfLIMACStream_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,111,3))
_HpnicfLIMACStreamObjects_ObjectIdentity=ObjectIdentity
hpnicfLIMACStreamObjects=_HpnicfLIMACStreamObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,111,3,1))
_HpnicfLIMACStreamTable_Object=MibTable
hpnicfLIMACStreamTable=_HpnicfLIMACStreamTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,3,1,1))
if mibBuilder.loadTexts:hpnicfLIMACStreamTable.setStatus(_A)
_HpnicfLIMACStreamEntry_Object=MibTableRow
hpnicfLIMACStreamEntry=_HpnicfLIMACStreamEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,3,1,1,1))
hpnicfLIMACStreamEntry.setIndexNames((0,_C,_E),(0,_C,_I))
if mibBuilder.loadTexts:hpnicfLIMACStreamEntry.setStatus(_A)
class _HpnicfLIMACStreamFields_Type(Bits):namedValues=NamedValues(*(('interface',0),('dstMacAddress',1),('srcMacAddress',2),('ethernetPid',3),('dSap',4),('sSap',5)))
_HpnicfLIMACStreamFields_Type.__name__='Bits'
_HpnicfLIMACStreamFields_Object=MibTableColumn
hpnicfLIMACStreamFields=_HpnicfLIMACStreamFields_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,3,1,1,1,1),_HpnicfLIMACStreamFields_Type())
hpnicfLIMACStreamFields.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIMACStreamFields.setStatus(_A)
_HpnicfLIMACStreamInterface_Type=InterfaceIndexOrZero
_HpnicfLIMACStreamInterface_Object=MibTableColumn
hpnicfLIMACStreamInterface=_HpnicfLIMACStreamInterface_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,3,1,1,1,2),_HpnicfLIMACStreamInterface_Type())
hpnicfLIMACStreamInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIMACStreamInterface.setStatus(_A)
_HpnicfLIMACStreamDestAddr_Type=MacAddress
_HpnicfLIMACStreamDestAddr_Object=MibTableColumn
hpnicfLIMACStreamDestAddr=_HpnicfLIMACStreamDestAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,3,1,1,1,3),_HpnicfLIMACStreamDestAddr_Type())
hpnicfLIMACStreamDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIMACStreamDestAddr.setStatus(_A)
_HpnicfLIMACStreamSrcAddr_Type=MacAddress
_HpnicfLIMACStreamSrcAddr_Object=MibTableColumn
hpnicfLIMACStreamSrcAddr=_HpnicfLIMACStreamSrcAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,3,1,1,1,4),_HpnicfLIMACStreamSrcAddr_Type())
hpnicfLIMACStreamSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIMACStreamSrcAddr.setStatus(_A)
_HpnicfLIMACStreamEthPid_Type=Unsigned32
_HpnicfLIMACStreamEthPid_Object=MibTableColumn
hpnicfLIMACStreamEthPid=_HpnicfLIMACStreamEthPid_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,3,1,1,1,5),_HpnicfLIMACStreamEthPid_Type())
hpnicfLIMACStreamEthPid.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIMACStreamEthPid.setStatus(_A)
_HpnicfLIMACStreamDSap_Type=Unsigned32
_HpnicfLIMACStreamDSap_Object=MibTableColumn
hpnicfLIMACStreamDSap=_HpnicfLIMACStreamDSap_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,3,1,1,1,6),_HpnicfLIMACStreamDSap_Type())
hpnicfLIMACStreamDSap.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIMACStreamDSap.setStatus(_A)
_HpnicfLIMACStreamSSap_Type=Unsigned32
_HpnicfLIMACStreamSSap_Object=MibTableColumn
hpnicfLIMACStreamSSap=_HpnicfLIMACStreamSSap_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,3,1,1,1,7),_HpnicfLIMACStreamSSap_Type())
hpnicfLIMACStreamSSap.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIMACStreamSSap.setStatus(_A)
_HpnicfLIMACStreamRowStatus_Type=RowStatus
_HpnicfLIMACStreamRowStatus_Object=MibTableColumn
hpnicfLIMACStreamRowStatus=_HpnicfLIMACStreamRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,3,1,1,1,8),_HpnicfLIMACStreamRowStatus_Type())
hpnicfLIMACStreamRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfLIMACStreamRowStatus.setStatus(_A)
_HpnicfLIUserStream_ObjectIdentity=ObjectIdentity
hpnicfLIUserStream=_HpnicfLIUserStream_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,111,4))
_HpnicfLIUserStreamObjects_ObjectIdentity=ObjectIdentity
hpnicfLIUserStreamObjects=_HpnicfLIUserStreamObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,111,4,1))
_HpnicfLIUserStreamTable_Object=MibTable
hpnicfLIUserStreamTable=_HpnicfLIUserStreamTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,4,1,1))
if mibBuilder.loadTexts:hpnicfLIUserStreamTable.setStatus(_A)
_HpnicfLIUserStreamEntry_Object=MibTableRow
hpnicfLIUserStreamEntry=_HpnicfLIUserStreamEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,4,1,1,1))
hpnicfLIUserStreamEntry.setIndexNames((0,_C,_E),(0,_C,_I))
if mibBuilder.loadTexts:hpnicfLIUserStreamEntry.setStatus(_A)
class _HpnicfLIUserStreamAcctSessID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,253))
_HpnicfLIUserStreamAcctSessID_Type.__name__=_N
_HpnicfLIUserStreamAcctSessID_Object=MibTableColumn
hpnicfLIUserStreamAcctSessID=_HpnicfLIUserStreamAcctSessID_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,4,1,1,1,1),_HpnicfLIUserStreamAcctSessID_Type())
hpnicfLIUserStreamAcctSessID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLIUserStreamAcctSessID.setStatus(_A)
_HpnicfLIUserStreamRowStatus_Type=RowStatus
_HpnicfLIUserStreamRowStatus_Object=MibTableColumn
hpnicfLIUserStreamRowStatus=_HpnicfLIUserStreamRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,111,4,1,1,1,2),_HpnicfLIUserStreamRowStatus_Type())
hpnicfLIUserStreamRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfLIUserStreamRowStatus.setStatus(_A)
hpnicfLIActive=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,111,1,2,0,1))
hpnicfLIActive.setObjects((_C,_M))
if mibBuilder.loadTexts:hpnicfLIActive.setStatus(_A)
hpnicfLITimeOut=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,111,1,2,0,2))
hpnicfLITimeOut.setObjects((_C,_S))
if mibBuilder.loadTexts:hpnicfLITimeOut.setStatus(_A)
hpnicfLIFailureInformation=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,111,1,2,0,3))
hpnicfLIFailureInformation.setObjects(*((_C,_M),(_C,_T)))
if mibBuilder.loadTexts:hpnicfLIFailureInformation.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfLI':hpnicfLI,'hpnicfLICommon':hpnicfLICommon,'hpnicfLITrapBindObjects':hpnicfLITrapBindObjects,_T:hpnicfLIBoardInformation,'hpnicfLINotifications':hpnicfLINotifications,'hpnicfLINotificationsPrefix':hpnicfLINotificationsPrefix,'hpnicfLIActive':hpnicfLIActive,'hpnicfLITimeOut':hpnicfLITimeOut,'hpnicfLIFailureInformation':hpnicfLIFailureInformation,'hpnicfLIObjects':hpnicfLIObjects,'hpnicfLINewIndex':hpnicfLINewIndex,'hpnicfLIMediationTable':hpnicfLIMediationTable,'hpnicfLIMediationEntry':hpnicfLIMediationEntry,_E:hpnicfLIMediationIndex,'hpnicfLIMediationDestAddrType':hpnicfLIMediationDestAddrType,'hpnicfLIMediationDestAddr':hpnicfLIMediationDestAddr,'hpnicfLIMediationDestPort':hpnicfLIMediationDestPort,'hpnicfLIMediationSrcInterface':hpnicfLIMediationSrcInterface,'hpnicfLIMediationDscp':hpnicfLIMediationDscp,'hpnicfLIMediationTimeOut':hpnicfLIMediationTimeOut,'hpnicfLIMediationTransport':hpnicfLIMediationTransport,'hpnicfLIMediationNotificationEnable':hpnicfLIMediationNotificationEnable,_S:hpnicfLIMediationRowStatus,'hpnicfLIStreamTable':hpnicfLIStreamTable,'hpnicfLIStreamEntry':hpnicfLIStreamEntry,_I:hpnicfLIStreamIndex,_M:hpnicfLIStreamtype,'hpnicfLIStreamEnable':hpnicfLIStreamEnable,'hpnicfLIStreamPackets':hpnicfLIStreamPackets,'hpnicfLIStreamDrops':hpnicfLIStreamDrops,'hpnicfLIStreamHPackets':hpnicfLIStreamHPackets,'hpnicfLIStreamHDrops':hpnicfLIStreamHDrops,'hpnicfLIStreamRowStatus':hpnicfLIStreamRowStatus,'hpnicfLIIPStream':hpnicfLIIPStream,'hpnicfLIIPStreamObjects':hpnicfLIIPStreamObjects,'hpnicfLIIPStreamTable':hpnicfLIIPStreamTable,'hpnicfLIIPStreamEntry':hpnicfLIIPStreamEntry,'hpnicfLIIPStreamInterface':hpnicfLIIPStreamInterface,'hpnicfLIIPStreamAddrType':hpnicfLIIPStreamAddrType,'hpnicfLIIPStreamDestAddr':hpnicfLIIPStreamDestAddr,'hpnicfLIIPStreamDestAddrLength':hpnicfLIIPStreamDestAddrLength,'hpnicfLIIPStreamSrcAddr':hpnicfLIIPStreamSrcAddr,'hpnicfLIIPStreamSrcAddrLength':hpnicfLIIPStreamSrcAddrLength,'hpnicfLIIPStreamTosByte':hpnicfLIIPStreamTosByte,'hpnicfLIIPStreamTosByteMask':hpnicfLIIPStreamTosByteMask,'hpnicfLIIPStreamFlowId':hpnicfLIIPStreamFlowId,'hpnicfLIIPStreamProtocol':hpnicfLIIPStreamProtocol,'hpnicfLIIPStreamDestL4PortMin':hpnicfLIIPStreamDestL4PortMin,'hpnicfLIIPStreamDestL4PortMax':hpnicfLIIPStreamDestL4PortMax,'hpnicfLIIPStreamSrcL4PortMin':hpnicfLIIPStreamSrcL4PortMin,'hpnicfLIIPStreamSrcL4PortMax':hpnicfLIIPStreamSrcL4PortMax,'hpnicfLIIPStreamVRF':hpnicfLIIPStreamVRF,'hpnicfLIIPStreamRowStatus':hpnicfLIIPStreamRowStatus,'hpnicfLIMACStream':hpnicfLIMACStream,'hpnicfLIMACStreamObjects':hpnicfLIMACStreamObjects,'hpnicfLIMACStreamTable':hpnicfLIMACStreamTable,'hpnicfLIMACStreamEntry':hpnicfLIMACStreamEntry,'hpnicfLIMACStreamFields':hpnicfLIMACStreamFields,'hpnicfLIMACStreamInterface':hpnicfLIMACStreamInterface,'hpnicfLIMACStreamDestAddr':hpnicfLIMACStreamDestAddr,'hpnicfLIMACStreamSrcAddr':hpnicfLIMACStreamSrcAddr,'hpnicfLIMACStreamEthPid':hpnicfLIMACStreamEthPid,'hpnicfLIMACStreamDSap':hpnicfLIMACStreamDSap,'hpnicfLIMACStreamSSap':hpnicfLIMACStreamSSap,'hpnicfLIMACStreamRowStatus':hpnicfLIMACStreamRowStatus,'hpnicfLIUserStream':hpnicfLIUserStream,'hpnicfLIUserStreamObjects':hpnicfLIUserStreamObjects,'hpnicfLIUserStreamTable':hpnicfLIUserStreamTable,'hpnicfLIUserStreamEntry':hpnicfLIUserStreamEntry,'hpnicfLIUserStreamAcctSessID':hpnicfLIUserStreamAcctSessID,'hpnicfLIUserStreamRowStatus':hpnicfLIUserStreamRowStatus})