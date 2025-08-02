_s='cabhCapGroup'
_r='cabhCapMappingEnable'
_q='cabhCapMappingRemoteHostAddr'
_p='cabhCapMappingRemoteHostAddrType'
_o='cabhCapUpnpTimeWait'
_n='cabhCapUpnpPortForwardingEnable'
_m='cabhCapMappingDuration'
_l='cabhCapMappingLastUpdateTime'
_k='cabhCapMappingCreateTime'
_j='cabhCapMappingRowDescr'
_i='cabhCapMappingNumPorts'
_h='cabhCapPassthroughRowStatus'
_g='cabhCapPassthroughMacAddr'
_f='cabhCapMappingRowStatus'
_e='cabhCapMappingProtocol'
_d='cabhCapMappingMethod'
_c='cabhCapMappingLanPort'
_b='cabhCapMappingLanAddr'
_a='cabhCapMappingLanAddrType'
_Z='cabhCapMappingWanPort'
_Y='cabhCapMappingWanAddr'
_X='cabhCapMappingWanAddrType'
_W='cabhCapLastSetToFactory'
_V='cabhCapSetToFactory'
_U='cabhCapPrimaryMode'
_T='cabhCapIcmpTimeWait'
_S='cabhCapUdpTimeWait'
_R='cabhCapTcpTimeWait'
_Q='cabhCapPassthroughIndex'
_P='not-accessible'
_O='cabhCapMappingIndex'
_N='PhysAddress'
_M='SnmpAdminString'
_L='InetAddress'
_K='TruthValue'
_J='InetPortNumber'
_I='InetAddressType'
_H='seconds'
_G='Unsigned32'
_F='read-only'
_E='read-write'
_D='Integer32'
_C='read-create'
_B='CABH-CAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clabProjCableHome,=mibBuilder.importSymbols('CLAB-DEF-MIB','clabProjCableHome')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_L,_I,_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString',_N,'RowStatus','TextualConvention','TimeStamp',_K)
cabhCapMib=ModuleIdentity((1,3,6,1,4,1,4491,2,4,3))
if mibBuilder.loadTexts:cabhCapMib.setRevisions(('2005-02-11 00:00',))
_CabhCapObjects_ObjectIdentity=ObjectIdentity
cabhCapObjects=_CabhCapObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,4,3,1))
_CabhCapBase_ObjectIdentity=ObjectIdentity
cabhCapBase=_CabhCapBase_ObjectIdentity((1,3,6,1,4,1,4491,2,4,3,1,1))
class _CabhCapTcpTimeWait_Type(Unsigned32):defaultValue=300
_CabhCapTcpTimeWait_Type.__name__=_G
_CabhCapTcpTimeWait_Object=MibScalar
cabhCapTcpTimeWait=_CabhCapTcpTimeWait_Object((1,3,6,1,4,1,4491,2,4,3,1,1,1),_CabhCapTcpTimeWait_Type())
cabhCapTcpTimeWait.setMaxAccess(_E)
if mibBuilder.loadTexts:cabhCapTcpTimeWait.setStatus(_A)
if mibBuilder.loadTexts:cabhCapTcpTimeWait.setUnits(_H)
class _CabhCapUdpTimeWait_Type(Unsigned32):defaultValue=300
_CabhCapUdpTimeWait_Type.__name__=_G
_CabhCapUdpTimeWait_Object=MibScalar
cabhCapUdpTimeWait=_CabhCapUdpTimeWait_Object((1,3,6,1,4,1,4491,2,4,3,1,1,2),_CabhCapUdpTimeWait_Type())
cabhCapUdpTimeWait.setMaxAccess(_E)
if mibBuilder.loadTexts:cabhCapUdpTimeWait.setStatus(_A)
if mibBuilder.loadTexts:cabhCapUdpTimeWait.setUnits(_H)
class _CabhCapIcmpTimeWait_Type(Unsigned32):defaultValue=300
_CabhCapIcmpTimeWait_Type.__name__=_G
_CabhCapIcmpTimeWait_Object=MibScalar
cabhCapIcmpTimeWait=_CabhCapIcmpTimeWait_Object((1,3,6,1,4,1,4491,2,4,3,1,1,3),_CabhCapIcmpTimeWait_Type())
cabhCapIcmpTimeWait.setMaxAccess(_E)
if mibBuilder.loadTexts:cabhCapIcmpTimeWait.setStatus(_A)
if mibBuilder.loadTexts:cabhCapIcmpTimeWait.setUnits(_H)
class _CabhCapPrimaryMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('napt',1),('nat',2),('passthrough',3)))
_CabhCapPrimaryMode_Type.__name__=_D
_CabhCapPrimaryMode_Object=MibScalar
cabhCapPrimaryMode=_CabhCapPrimaryMode_Object((1,3,6,1,4,1,4491,2,4,3,1,1,4),_CabhCapPrimaryMode_Type())
cabhCapPrimaryMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cabhCapPrimaryMode.setStatus(_A)
_CabhCapSetToFactory_Type=TruthValue
_CabhCapSetToFactory_Object=MibScalar
cabhCapSetToFactory=_CabhCapSetToFactory_Object((1,3,6,1,4,1,4491,2,4,3,1,1,5),_CabhCapSetToFactory_Type())
cabhCapSetToFactory.setMaxAccess(_E)
if mibBuilder.loadTexts:cabhCapSetToFactory.setStatus(_A)
_CabhCapLastSetToFactory_Type=TimeStamp
_CabhCapLastSetToFactory_Object=MibScalar
cabhCapLastSetToFactory=_CabhCapLastSetToFactory_Object((1,3,6,1,4,1,4491,2,4,3,1,1,6),_CabhCapLastSetToFactory_Type())
cabhCapLastSetToFactory.setMaxAccess(_F)
if mibBuilder.loadTexts:cabhCapLastSetToFactory.setStatus(_A)
class _CabhCapUpnpPortForwardingEnable_Type(TruthValue):defaultValue=1
_CabhCapUpnpPortForwardingEnable_Type.__name__=_K
_CabhCapUpnpPortForwardingEnable_Object=MibScalar
cabhCapUpnpPortForwardingEnable=_CabhCapUpnpPortForwardingEnable_Object((1,3,6,1,4,1,4491,2,4,3,1,1,7),_CabhCapUpnpPortForwardingEnable_Type())
cabhCapUpnpPortForwardingEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cabhCapUpnpPortForwardingEnable.setStatus(_A)
class _CabhCapUpnpTimeWait_Type(Unsigned32):defaultValue=0
_CabhCapUpnpTimeWait_Type.__name__=_G
_CabhCapUpnpTimeWait_Object=MibScalar
cabhCapUpnpTimeWait=_CabhCapUpnpTimeWait_Object((1,3,6,1,4,1,4491,2,4,3,1,1,8),_CabhCapUpnpTimeWait_Type())
cabhCapUpnpTimeWait.setMaxAccess(_E)
if mibBuilder.loadTexts:cabhCapUpnpTimeWait.setStatus(_A)
if mibBuilder.loadTexts:cabhCapUpnpTimeWait.setUnits(_H)
_CabhCapMap_ObjectIdentity=ObjectIdentity
cabhCapMap=_CabhCapMap_ObjectIdentity((1,3,6,1,4,1,4491,2,4,3,1,2))
_CabhCapMappingTable_Object=MibTable
cabhCapMappingTable=_CabhCapMappingTable_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1))
if mibBuilder.loadTexts:cabhCapMappingTable.setStatus(_A)
_CabhCapMappingEntry_Object=MibTableRow
cabhCapMappingEntry=_CabhCapMappingEntry_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1))
cabhCapMappingEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:cabhCapMappingEntry.setStatus(_A)
class _CabhCapMappingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CabhCapMappingIndex_Type.__name__=_D
_CabhCapMappingIndex_Object=MibTableColumn
cabhCapMappingIndex=_CabhCapMappingIndex_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,1),_CabhCapMappingIndex_Type())
cabhCapMappingIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:cabhCapMappingIndex.setStatus(_A)
class _CabhCapMappingWanAddrType_Type(InetAddressType):defaultValue=1
_CabhCapMappingWanAddrType_Type.__name__=_I
_CabhCapMappingWanAddrType_Object=MibTableColumn
cabhCapMappingWanAddrType=_CabhCapMappingWanAddrType_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,2),_CabhCapMappingWanAddrType_Type())
cabhCapMappingWanAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhCapMappingWanAddrType.setStatus(_A)
_CabhCapMappingWanAddr_Type=InetAddress
_CabhCapMappingWanAddr_Object=MibTableColumn
cabhCapMappingWanAddr=_CabhCapMappingWanAddr_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,3),_CabhCapMappingWanAddr_Type())
cabhCapMappingWanAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhCapMappingWanAddr.setStatus(_A)
class _CabhCapMappingWanPort_Type(InetPortNumber):defaultValue=0
_CabhCapMappingWanPort_Type.__name__=_J
_CabhCapMappingWanPort_Object=MibTableColumn
cabhCapMappingWanPort=_CabhCapMappingWanPort_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,4),_CabhCapMappingWanPort_Type())
cabhCapMappingWanPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhCapMappingWanPort.setStatus(_A)
class _CabhCapMappingLanAddrType_Type(InetAddressType):defaultValue=1
_CabhCapMappingLanAddrType_Type.__name__=_I
_CabhCapMappingLanAddrType_Object=MibTableColumn
cabhCapMappingLanAddrType=_CabhCapMappingLanAddrType_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,5),_CabhCapMappingLanAddrType_Type())
cabhCapMappingLanAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhCapMappingLanAddrType.setStatus(_A)
_CabhCapMappingLanAddr_Type=InetAddress
_CabhCapMappingLanAddr_Object=MibTableColumn
cabhCapMappingLanAddr=_CabhCapMappingLanAddr_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,6),_CabhCapMappingLanAddr_Type())
cabhCapMappingLanAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhCapMappingLanAddr.setStatus(_A)
class _CabhCapMappingLanPort_Type(InetPortNumber):defaultValue=0
_CabhCapMappingLanPort_Type.__name__=_J
_CabhCapMappingLanPort_Object=MibTableColumn
cabhCapMappingLanPort=_CabhCapMappingLanPort_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,7),_CabhCapMappingLanPort_Type())
cabhCapMappingLanPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhCapMappingLanPort.setStatus(_A)
class _CabhCapMappingMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),('dynamic',2),('upnp',3)))
_CabhCapMappingMethod_Type.__name__=_D
_CabhCapMappingMethod_Object=MibTableColumn
cabhCapMappingMethod=_CabhCapMappingMethod_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,8),_CabhCapMappingMethod_Type())
cabhCapMappingMethod.setMaxAccess(_F)
if mibBuilder.loadTexts:cabhCapMappingMethod.setStatus(_A)
class _CabhCapMappingProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*(('other',1),('icmp',2),('udp',3),('tcp',4),('all',255)))
_CabhCapMappingProtocol_Type.__name__=_D
_CabhCapMappingProtocol_Object=MibTableColumn
cabhCapMappingProtocol=_CabhCapMappingProtocol_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,9),_CabhCapMappingProtocol_Type())
cabhCapMappingProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhCapMappingProtocol.setStatus(_A)
_CabhCapMappingRowStatus_Type=RowStatus
_CabhCapMappingRowStatus_Object=MibTableColumn
cabhCapMappingRowStatus=_CabhCapMappingRowStatus_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,10),_CabhCapMappingRowStatus_Type())
cabhCapMappingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhCapMappingRowStatus.setStatus(_A)
class _CabhCapMappingNumPorts_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CabhCapMappingNumPorts_Type.__name__=_G
_CabhCapMappingNumPorts_Object=MibTableColumn
cabhCapMappingNumPorts=_CabhCapMappingNumPorts_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,11),_CabhCapMappingNumPorts_Type())
cabhCapMappingNumPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhCapMappingNumPorts.setStatus(_A)
class _CabhCapMappingRowDescr_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CabhCapMappingRowDescr_Type.__name__=_M
_CabhCapMappingRowDescr_Object=MibTableColumn
cabhCapMappingRowDescr=_CabhCapMappingRowDescr_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,12),_CabhCapMappingRowDescr_Type())
cabhCapMappingRowDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhCapMappingRowDescr.setStatus(_A)
_CabhCapMappingCreateTime_Type=DateAndTime
_CabhCapMappingCreateTime_Object=MibTableColumn
cabhCapMappingCreateTime=_CabhCapMappingCreateTime_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,13),_CabhCapMappingCreateTime_Type())
cabhCapMappingCreateTime.setMaxAccess(_F)
if mibBuilder.loadTexts:cabhCapMappingCreateTime.setStatus(_A)
_CabhCapMappingLastUpdateTime_Type=DateAndTime
_CabhCapMappingLastUpdateTime_Object=MibTableColumn
cabhCapMappingLastUpdateTime=_CabhCapMappingLastUpdateTime_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,14),_CabhCapMappingLastUpdateTime_Type())
cabhCapMappingLastUpdateTime.setMaxAccess(_F)
if mibBuilder.loadTexts:cabhCapMappingLastUpdateTime.setStatus(_A)
class _CabhCapMappingDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_CabhCapMappingDuration_Type.__name__=_D
_CabhCapMappingDuration_Object=MibTableColumn
cabhCapMappingDuration=_CabhCapMappingDuration_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,15),_CabhCapMappingDuration_Type())
cabhCapMappingDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhCapMappingDuration.setStatus(_A)
if mibBuilder.loadTexts:cabhCapMappingDuration.setUnits(_H)
class _CabhCapMappingRemoteHostAddrType_Type(InetAddressType):defaultValue=1
_CabhCapMappingRemoteHostAddrType_Type.__name__=_I
_CabhCapMappingRemoteHostAddrType_Object=MibTableColumn
cabhCapMappingRemoteHostAddrType=_CabhCapMappingRemoteHostAddrType_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,16),_CabhCapMappingRemoteHostAddrType_Type())
cabhCapMappingRemoteHostAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:cabhCapMappingRemoteHostAddrType.setStatus(_A)
class _CabhCapMappingRemoteHostAddr_Type(InetAddress):defaultHexValue='00000000'
_CabhCapMappingRemoteHostAddr_Type.__name__=_L
_CabhCapMappingRemoteHostAddr_Object=MibTableColumn
cabhCapMappingRemoteHostAddr=_CabhCapMappingRemoteHostAddr_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,17),_CabhCapMappingRemoteHostAddr_Type())
cabhCapMappingRemoteHostAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:cabhCapMappingRemoteHostAddr.setStatus(_A)
class _CabhCapMappingEnable_Type(TruthValue):defaultValue=1
_CabhCapMappingEnable_Type.__name__=_K
_CabhCapMappingEnable_Object=MibTableColumn
cabhCapMappingEnable=_CabhCapMappingEnable_Object((1,3,6,1,4,1,4491,2,4,3,1,2,1,1,18),_CabhCapMappingEnable_Type())
cabhCapMappingEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:cabhCapMappingEnable.setStatus(_A)
_CabhCapPassthroughTable_Object=MibTable
cabhCapPassthroughTable=_CabhCapPassthroughTable_Object((1,3,6,1,4,1,4491,2,4,3,1,2,2))
if mibBuilder.loadTexts:cabhCapPassthroughTable.setStatus(_A)
_CabhCapPassthroughEntry_Object=MibTableRow
cabhCapPassthroughEntry=_CabhCapPassthroughEntry_Object((1,3,6,1,4,1,4491,2,4,3,1,2,2,1))
cabhCapPassthroughEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:cabhCapPassthroughEntry.setStatus(_A)
class _CabhCapPassthroughIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CabhCapPassthroughIndex_Type.__name__=_D
_CabhCapPassthroughIndex_Object=MibTableColumn
cabhCapPassthroughIndex=_CabhCapPassthroughIndex_Object((1,3,6,1,4,1,4491,2,4,3,1,2,2,1,1),_CabhCapPassthroughIndex_Type())
cabhCapPassthroughIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:cabhCapPassthroughIndex.setStatus(_A)
class _CabhCapPassthroughMacAddr_Type(PhysAddress):subtypeSpec=PhysAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CabhCapPassthroughMacAddr_Type.__name__=_N
_CabhCapPassthroughMacAddr_Object=MibTableColumn
cabhCapPassthroughMacAddr=_CabhCapPassthroughMacAddr_Object((1,3,6,1,4,1,4491,2,4,3,1,2,2,1,2),_CabhCapPassthroughMacAddr_Type())
cabhCapPassthroughMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhCapPassthroughMacAddr.setStatus(_A)
_CabhCapPassthroughRowStatus_Type=RowStatus
_CabhCapPassthroughRowStatus_Object=MibTableColumn
cabhCapPassthroughRowStatus=_CabhCapPassthroughRowStatus_Object((1,3,6,1,4,1,4491,2,4,3,1,2,2,1,3),_CabhCapPassthroughRowStatus_Type())
cabhCapPassthroughRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhCapPassthroughRowStatus.setStatus(_A)
_CabhCapNotification_ObjectIdentity=ObjectIdentity
cabhCapNotification=_CabhCapNotification_ObjectIdentity((1,3,6,1,4,1,4491,2,4,3,2,0))
_CabhCapConformance_ObjectIdentity=ObjectIdentity
cabhCapConformance=_CabhCapConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,4,3,3))
_CabhCapCompliances_ObjectIdentity=ObjectIdentity
cabhCapCompliances=_CabhCapCompliances_ObjectIdentity((1,3,6,1,4,1,4491,2,4,3,3,1))
_CabhCapGroups_ObjectIdentity=ObjectIdentity
cabhCapGroups=_CabhCapGroups_ObjectIdentity((1,3,6,1,4,1,4491,2,4,3,3,2))
cabhCapGroup=ObjectGroup((1,3,6,1,4,1,4491,2,4,3,3,2,1))
cabhCapGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:cabhCapGroup.setStatus(_A)
cabhCapBasicCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,4,3,3,1,1))
cabhCapBasicCompliance.setObjects((_B,_s))
if mibBuilder.loadTexts:cabhCapBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cabhCapMib':cabhCapMib,'cabhCapObjects':cabhCapObjects,'cabhCapBase':cabhCapBase,_R:cabhCapTcpTimeWait,_S:cabhCapUdpTimeWait,_T:cabhCapIcmpTimeWait,_U:cabhCapPrimaryMode,_V:cabhCapSetToFactory,_W:cabhCapLastSetToFactory,_n:cabhCapUpnpPortForwardingEnable,_o:cabhCapUpnpTimeWait,'cabhCapMap':cabhCapMap,'cabhCapMappingTable':cabhCapMappingTable,'cabhCapMappingEntry':cabhCapMappingEntry,_O:cabhCapMappingIndex,_X:cabhCapMappingWanAddrType,_Y:cabhCapMappingWanAddr,_Z:cabhCapMappingWanPort,_a:cabhCapMappingLanAddrType,_b:cabhCapMappingLanAddr,_c:cabhCapMappingLanPort,_d:cabhCapMappingMethod,_e:cabhCapMappingProtocol,_f:cabhCapMappingRowStatus,_i:cabhCapMappingNumPorts,_j:cabhCapMappingRowDescr,_k:cabhCapMappingCreateTime,_l:cabhCapMappingLastUpdateTime,_m:cabhCapMappingDuration,_p:cabhCapMappingRemoteHostAddrType,_q:cabhCapMappingRemoteHostAddr,_r:cabhCapMappingEnable,'cabhCapPassthroughTable':cabhCapPassthroughTable,'cabhCapPassthroughEntry':cabhCapPassthroughEntry,_Q:cabhCapPassthroughIndex,_g:cabhCapPassthroughMacAddr,_h:cabhCapPassthroughRowStatus,'cabhCapNotification':cabhCapNotification,'cabhCapConformance':cabhCapConformance,'cabhCapCompliances':cabhCapCompliances,'cabhCapBasicCompliance':cabhCapBasicCompliance,'cabhCapGroups':cabhCapGroups,_s:cabhCapGroup})