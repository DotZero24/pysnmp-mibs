_F='arubaWiredVsxAggregatorIndex'
_E='ARUBAWIRED-VSX-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
arubaWiredVsxMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,7))
if mibBuilder.loadTexts:arubaWiredVsxMIB.setRevisions(('2018-09-05 00:00','2018-06-08 00:00'))
class VidList(TextualConvention,OctetString):status=_A;displayHint='512x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_ArubaWiredVsxConfig_ObjectIdentity=ObjectIdentity
arubaWiredVsxConfig=_ArubaWiredVsxConfig_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,7,1))
_ArubaWiredVsxIslConfig_ObjectIdentity=ObjectIdentity
arubaWiredVsxIslConfig=_ArubaWiredVsxIslConfig_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,7,1,1))
_ArubaWiredVsxIslPort_Type=DisplayString
_ArubaWiredVsxIslPort_Object=MibScalar
arubaWiredVsxIslPort=_ArubaWiredVsxIslPort_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,1,1),_ArubaWiredVsxIslPort_Type())
arubaWiredVsxIslPort.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredVsxIslPort.setStatus(_A)
class _ArubaWiredVsxIslHelloInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_ArubaWiredVsxIslHelloInterval_Type.__name__=_C
_ArubaWiredVsxIslHelloInterval_Object=MibScalar
arubaWiredVsxIslHelloInterval=_ArubaWiredVsxIslHelloInterval_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,1,2),_ArubaWiredVsxIslHelloInterval_Type())
arubaWiredVsxIslHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredVsxIslHelloInterval.setStatus(_A)
class _ArubaWiredVsxIslHoldTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_ArubaWiredVsxIslHoldTime_Type.__name__=_C
_ArubaWiredVsxIslHoldTime_Object=MibScalar
arubaWiredVsxIslHoldTime=_ArubaWiredVsxIslHoldTime_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,1,3),_ArubaWiredVsxIslHoldTime_Type())
arubaWiredVsxIslHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredVsxIslHoldTime.setStatus(_A)
class _ArubaWiredVsxIslHelloTimeout_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,20))
_ArubaWiredVsxIslHelloTimeout_Type.__name__=_C
_ArubaWiredVsxIslHelloTimeout_Object=MibScalar
arubaWiredVsxIslHelloTimeout=_ArubaWiredVsxIslHelloTimeout_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,1,4),_ArubaWiredVsxIslHelloTimeout_Type())
arubaWiredVsxIslHelloTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredVsxIslHelloTimeout.setStatus(_A)
_ArubaWiredVsxIslSystemID_Type=DisplayString
_ArubaWiredVsxIslSystemID_Object=MibScalar
arubaWiredVsxIslSystemID=_ArubaWiredVsxIslSystemID_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,1,5),_ArubaWiredVsxIslSystemID_Type())
arubaWiredVsxIslSystemID.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxIslSystemID.setStatus(_A)
_ArubaWiredVsxIslPlatformName_Type=DisplayString
_ArubaWiredVsxIslPlatformName_Object=MibScalar
arubaWiredVsxIslPlatformName=_ArubaWiredVsxIslPlatformName_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,1,6),_ArubaWiredVsxIslPlatformName_Type())
arubaWiredVsxIslPlatformName.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxIslPlatformName.setStatus(_A)
_ArubaWiredVsxIslSwVersion_Type=DisplayString
_ArubaWiredVsxIslSwVersion_Object=MibScalar
arubaWiredVsxIslSwVersion=_ArubaWiredVsxIslSwVersion_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,1,7),_ArubaWiredVsxIslSwVersion_Type())
arubaWiredVsxIslSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxIslSwVersion.setStatus(_A)
_ArubaWiredVsxIslVIDList_Type=VidList
_ArubaWiredVsxIslVIDList_Object=MibScalar
arubaWiredVsxIslVIDList=_ArubaWiredVsxIslVIDList_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,1,8),_ArubaWiredVsxIslVIDList_Type())
arubaWiredVsxIslVIDList.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxIslVIDList.setStatus(_A)
_ArubaWiredVsxKeepAliveConfig_ObjectIdentity=ObjectIdentity
arubaWiredVsxKeepAliveConfig=_ArubaWiredVsxKeepAliveConfig_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,7,1,2))
_ArubaWiredVsxKeepAliveSrcIPAddrType_Type=InetAddressType
_ArubaWiredVsxKeepAliveSrcIPAddrType_Object=MibScalar
arubaWiredVsxKeepAliveSrcIPAddrType=_ArubaWiredVsxKeepAliveSrcIPAddrType_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,2,1),_ArubaWiredVsxKeepAliveSrcIPAddrType_Type())
arubaWiredVsxKeepAliveSrcIPAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredVsxKeepAliveSrcIPAddrType.setStatus(_A)
_ArubaWiredVsxKeepAliveSrcIPAddr_Type=InetAddress
_ArubaWiredVsxKeepAliveSrcIPAddr_Object=MibScalar
arubaWiredVsxKeepAliveSrcIPAddr=_ArubaWiredVsxKeepAliveSrcIPAddr_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,2,2),_ArubaWiredVsxKeepAliveSrcIPAddr_Type())
arubaWiredVsxKeepAliveSrcIPAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredVsxKeepAliveSrcIPAddr.setStatus(_A)
_ArubaWiredVsxKeepAliveVrf_Type=DisplayString
_ArubaWiredVsxKeepAliveVrf_Object=MibScalar
arubaWiredVsxKeepAliveVrf=_ArubaWiredVsxKeepAliveVrf_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,2,3),_ArubaWiredVsxKeepAliveVrf_Type())
arubaWiredVsxKeepAliveVrf.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredVsxKeepAliveVrf.setStatus(_A)
class _ArubaWiredVsxKeepAliveUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_ArubaWiredVsxKeepAliveUdpPort_Type.__name__=_C
_ArubaWiredVsxKeepAliveUdpPort_Object=MibScalar
arubaWiredVsxKeepAliveUdpPort=_ArubaWiredVsxKeepAliveUdpPort_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,2,4),_ArubaWiredVsxKeepAliveUdpPort_Type())
arubaWiredVsxKeepAliveUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredVsxKeepAliveUdpPort.setStatus(_A)
_ArubaWiredVsxKeepAlivePeerIPAddrType_Type=InetAddressType
_ArubaWiredVsxKeepAlivePeerIPAddrType_Object=MibScalar
arubaWiredVsxKeepAlivePeerIPAddrType=_ArubaWiredVsxKeepAlivePeerIPAddrType_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,2,5),_ArubaWiredVsxKeepAlivePeerIPAddrType_Type())
arubaWiredVsxKeepAlivePeerIPAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredVsxKeepAlivePeerIPAddrType.setStatus(_A)
_ArubaWiredVsxKeepAlivePeerIPAddr_Type=InetAddress
_ArubaWiredVsxKeepAlivePeerIPAddr_Object=MibScalar
arubaWiredVsxKeepAlivePeerIPAddr=_ArubaWiredVsxKeepAlivePeerIPAddr_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,2,6),_ArubaWiredVsxKeepAlivePeerIPAddr_Type())
arubaWiredVsxKeepAlivePeerIPAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredVsxKeepAlivePeerIPAddr.setStatus(_A)
class _ArubaWiredVsxKeepAliveHelloInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_ArubaWiredVsxKeepAliveHelloInterval_Type.__name__=_C
_ArubaWiredVsxKeepAliveHelloInterval_Object=MibScalar
arubaWiredVsxKeepAliveHelloInterval=_ArubaWiredVsxKeepAliveHelloInterval_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,2,7),_ArubaWiredVsxKeepAliveHelloInterval_Type())
arubaWiredVsxKeepAliveHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredVsxKeepAliveHelloInterval.setStatus(_A)
class _ArubaWiredVsxKeepAliveHelloTimeout_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,20))
_ArubaWiredVsxKeepAliveHelloTimeout_Type.__name__=_C
_ArubaWiredVsxKeepAliveHelloTimeout_Object=MibScalar
arubaWiredVsxKeepAliveHelloTimeout=_ArubaWiredVsxKeepAliveHelloTimeout_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,2,8),_ArubaWiredVsxKeepAliveHelloTimeout_Type())
arubaWiredVsxKeepAliveHelloTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredVsxKeepAliveHelloTimeout.setStatus(_A)
_ArubaWiredVsxKeepAliveSystemID_Type=DisplayString
_ArubaWiredVsxKeepAliveSystemID_Object=MibScalar
arubaWiredVsxKeepAliveSystemID=_ArubaWiredVsxKeepAliveSystemID_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,2,9),_ArubaWiredVsxKeepAliveSystemID_Type())
arubaWiredVsxKeepAliveSystemID.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxKeepAliveSystemID.setStatus(_A)
_ArubaWiredVsxKeepAlivePlatformName_Type=DisplayString
_ArubaWiredVsxKeepAlivePlatformName_Object=MibScalar
arubaWiredVsxKeepAlivePlatformName=_ArubaWiredVsxKeepAlivePlatformName_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,2,10),_ArubaWiredVsxKeepAlivePlatformName_Type())
arubaWiredVsxKeepAlivePlatformName.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxKeepAlivePlatformName.setStatus(_A)
_ArubaWiredVsxKeepAliveSwVersion_Type=DisplayString
_ArubaWiredVsxKeepAliveSwVersion_Object=MibScalar
arubaWiredVsxKeepAliveSwVersion=_ArubaWiredVsxKeepAliveSwVersion_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,2,11),_ArubaWiredVsxKeepAliveSwVersion_Type())
arubaWiredVsxKeepAliveSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxKeepAliveSwVersion.setStatus(_A)
_ArubaWiredVsxAggregatorConfig_ObjectIdentity=ObjectIdentity
arubaWiredVsxAggregatorConfig=_ArubaWiredVsxAggregatorConfig_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,7,1,3))
_ArubaWiredVsxAggregatorTable_Object=MibTable
arubaWiredVsxAggregatorTable=_ArubaWiredVsxAggregatorTable_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,3,1))
if mibBuilder.loadTexts:arubaWiredVsxAggregatorTable.setStatus(_A)
_ArubaWiredVsxAggregatorEntry_Object=MibTableRow
arubaWiredVsxAggregatorEntry=_ArubaWiredVsxAggregatorEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,3,1,1))
arubaWiredVsxAggregatorEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:arubaWiredVsxAggregatorEntry.setStatus(_A)
_ArubaWiredVsxAggregatorIndex_Type=InterfaceIndex
_ArubaWiredVsxAggregatorIndex_Object=MibTableColumn
arubaWiredVsxAggregatorIndex=_ArubaWiredVsxAggregatorIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,3,1,1,1),_ArubaWiredVsxAggregatorIndex_Type())
arubaWiredVsxAggregatorIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:arubaWiredVsxAggregatorIndex.setStatus(_A)
class _ArubaWiredVsxAggregatorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('point2Point',1),('multiChassis',2)))
_ArubaWiredVsxAggregatorType_Type.__name__=_C
_ArubaWiredVsxAggregatorType_Object=MibTableColumn
arubaWiredVsxAggregatorType=_ArubaWiredVsxAggregatorType_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,3,1,1,2),_ArubaWiredVsxAggregatorType_Type())
arubaWiredVsxAggregatorType.setMaxAccess('read-create')
if mibBuilder.loadTexts:arubaWiredVsxAggregatorType.setStatus(_A)
_ArubaWiredVsxVlanList_Type=VidList
_ArubaWiredVsxVlanList_Object=MibTableColumn
arubaWiredVsxVlanList=_ArubaWiredVsxVlanList_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,3,1,1,3),_ArubaWiredVsxVlanList_Type())
arubaWiredVsxVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxVlanList.setStatus(_A)
_ArubaWiredVsxLoopProtectEnabled_Type=TruthValue
_ArubaWiredVsxLoopProtectEnabled_Object=MibTableColumn
arubaWiredVsxLoopProtectEnabled=_ArubaWiredVsxLoopProtectEnabled_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,3,1,1,4),_ArubaWiredVsxLoopProtectEnabled_Type())
arubaWiredVsxLoopProtectEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxLoopProtectEnabled.setStatus(_A)
class _ArubaWiredVsxLoadBalanceScheme_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('l2-Src-Dst',1),('l3-Src-Dst',2),('l4-Src-Dst',3)))
_ArubaWiredVsxLoadBalanceScheme_Type.__name__=_C
_ArubaWiredVsxLoadBalanceScheme_Object=MibTableColumn
arubaWiredVsxLoadBalanceScheme=_ArubaWiredVsxLoadBalanceScheme_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,3,1,1,5),_ArubaWiredVsxLoadBalanceScheme_Type())
arubaWiredVsxLoadBalanceScheme.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxLoadBalanceScheme.setStatus(_A)
class _ArubaWiredVsxCosOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ArubaWiredVsxCosOverride_Type.__name__=_C
_ArubaWiredVsxCosOverride_Object=MibTableColumn
arubaWiredVsxCosOverride=_ArubaWiredVsxCosOverride_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,3,1,1,6),_ArubaWiredVsxCosOverride_Type())
arubaWiredVsxCosOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxCosOverride.setStatus(_A)
class _ArubaWiredVsxDscpOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ArubaWiredVsxDscpOverride_Type.__name__=_C
_ArubaWiredVsxDscpOverride_Object=MibTableColumn
arubaWiredVsxDscpOverride=_ArubaWiredVsxDscpOverride_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,3,1,1,7),_ArubaWiredVsxDscpOverride_Type())
arubaWiredVsxDscpOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxDscpOverride.setStatus(_A)
class _ArubaWiredVsxQoSTrust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cos',1),('dscp',2)))
_ArubaWiredVsxQoSTrust_Type.__name__=_C
_ArubaWiredVsxQoSTrust_Object=MibTableColumn
arubaWiredVsxQoSTrust=_ArubaWiredVsxQoSTrust_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,3,1,1,8),_ArubaWiredVsxQoSTrust_Type())
arubaWiredVsxQoSTrust.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxQoSTrust.setStatus(_A)
_ArubaWiredVsxGlobalConfiguration_ObjectIdentity=ObjectIdentity
arubaWiredVsxGlobalConfiguration=_ArubaWiredVsxGlobalConfiguration_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,7,1,4))
class _ArubaWiredVsxDeviceRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('secondary',2),('notConfigured',3)))
_ArubaWiredVsxDeviceRole_Type.__name__=_C
_ArubaWiredVsxDeviceRole_Object=MibScalar
arubaWiredVsxDeviceRole=_ArubaWiredVsxDeviceRole_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,4,1),_ArubaWiredVsxDeviceRole_Type())
arubaWiredVsxDeviceRole.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxDeviceRole.setStatus(_A)
class _ArubaWiredVsxConfigSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ArubaWiredVsxConfigSync_Type.__name__=_C
_ArubaWiredVsxConfigSync_Object=MibScalar
arubaWiredVsxConfigSync=_ArubaWiredVsxConfigSync_Object((1,3,6,1,4,1,47196,4,1,1,3,7,1,4,2),_ArubaWiredVsxConfigSync_Type())
arubaWiredVsxConfigSync.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxConfigSync.setStatus(_A)
_ArubaWiredVsxStatus_ObjectIdentity=ObjectIdentity
arubaWiredVsxStatus=_ArubaWiredVsxStatus_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,7,2))
_ArubaWiredVsxIslStatus_ObjectIdentity=ObjectIdentity
arubaWiredVsxIslStatus=_ArubaWiredVsxIslStatus_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,7,2,1))
class _ArubaWiredVsxIslOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('init',1),('outSync',2),('inSync',3)))
_ArubaWiredVsxIslOperState_Type.__name__=_C
_ArubaWiredVsxIslOperState_Object=MibScalar
arubaWiredVsxIslOperState=_ArubaWiredVsxIslOperState_Object((1,3,6,1,4,1,47196,4,1,1,3,7,2,1,1),_ArubaWiredVsxIslOperState_Type())
arubaWiredVsxIslOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxIslOperState.setStatus(_A)
_ArubaWiredVsxIslPduTx_Type=Integer32
_ArubaWiredVsxIslPduTx_Object=MibScalar
arubaWiredVsxIslPduTx=_ArubaWiredVsxIslPduTx_Object((1,3,6,1,4,1,47196,4,1,1,3,7,2,1,2),_ArubaWiredVsxIslPduTx_Type())
arubaWiredVsxIslPduTx.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxIslPduTx.setStatus(_A)
_ArubaWiredVsxIslPduRx_Type=Integer32
_ArubaWiredVsxIslPduRx_Object=MibScalar
arubaWiredVsxIslPduRx=_ArubaWiredVsxIslPduRx_Object((1,3,6,1,4,1,47196,4,1,1,3,7,2,1,3),_ArubaWiredVsxIslPduRx_Type())
arubaWiredVsxIslPduRx.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxIslPduRx.setStatus(_A)
_ArubaWiredVsxIslHelloTx_Type=Integer32
_ArubaWiredVsxIslHelloTx_Object=MibScalar
arubaWiredVsxIslHelloTx=_ArubaWiredVsxIslHelloTx_Object((1,3,6,1,4,1,47196,4,1,1,3,7,2,1,4),_ArubaWiredVsxIslHelloTx_Type())
arubaWiredVsxIslHelloTx.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxIslHelloTx.setStatus(_A)
_ArubaWiredVsxIslHelloRx_Type=Integer32
_ArubaWiredVsxIslHelloRx_Object=MibScalar
arubaWiredVsxIslHelloRx=_ArubaWiredVsxIslHelloRx_Object((1,3,6,1,4,1,47196,4,1,1,3,7,2,1,5),_ArubaWiredVsxIslHelloRx_Type())
arubaWiredVsxIslHelloRx.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxIslHelloRx.setStatus(_A)
_ArubaWiredVsxDeviceOperSystemID_Type=DisplayString
_ArubaWiredVsxDeviceOperSystemID_Object=MibScalar
arubaWiredVsxDeviceOperSystemID=_ArubaWiredVsxDeviceOperSystemID_Object((1,3,6,1,4,1,47196,4,1,1,3,7,2,1,6),_ArubaWiredVsxDeviceOperSystemID_Type())
arubaWiredVsxDeviceOperSystemID.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxDeviceOperSystemID.setStatus(_A)
_ArubaWiredVsxKeepAliveStatus_ObjectIdentity=ObjectIdentity
arubaWiredVsxKeepAliveStatus=_ArubaWiredVsxKeepAliveStatus_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,7,2,2))
class _ArubaWiredVsxKeepAliveOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('init',1),('configured',2),('inSyncEstablished',3),('outofSyncEstablished',4),('initEstablished',5),('failed',6),('stopped',7)))
_ArubaWiredVsxKeepAliveOperState_Type.__name__=_C
_ArubaWiredVsxKeepAliveOperState_Object=MibScalar
arubaWiredVsxKeepAliveOperState=_ArubaWiredVsxKeepAliveOperState_Object((1,3,6,1,4,1,47196,4,1,1,3,7,2,2,1),_ArubaWiredVsxKeepAliveOperState_Type())
arubaWiredVsxKeepAliveOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxKeepAliveOperState.setStatus(_A)
_ArubaWiredVsxKeepAlivePacketsTx_Type=Integer32
_ArubaWiredVsxKeepAlivePacketsTx_Object=MibScalar
arubaWiredVsxKeepAlivePacketsTx=_ArubaWiredVsxKeepAlivePacketsTx_Object((1,3,6,1,4,1,47196,4,1,1,3,7,2,2,2),_ArubaWiredVsxKeepAlivePacketsTx_Type())
arubaWiredVsxKeepAlivePacketsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxKeepAlivePacketsTx.setStatus(_A)
_ArubaWiredVsxKeepAlivePacketsRx_Type=Integer32
_ArubaWiredVsxKeepAlivePacketsRx_Object=MibScalar
arubaWiredVsxKeepAlivePacketsRx=_ArubaWiredVsxKeepAlivePacketsRx_Object((1,3,6,1,4,1,47196,4,1,1,3,7,2,2,3),_ArubaWiredVsxKeepAlivePacketsRx_Type())
arubaWiredVsxKeepAlivePacketsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxKeepAlivePacketsRx.setStatus(_A)
_ArubaWiredVsxKeepAlivePacketsDrop_Type=Integer32
_ArubaWiredVsxKeepAlivePacketsDrop_Object=MibScalar
arubaWiredVsxKeepAlivePacketsDrop=_ArubaWiredVsxKeepAlivePacketsDrop_Object((1,3,6,1,4,1,47196,4,1,1,3,7,2,2,4),_ArubaWiredVsxKeepAlivePacketsDrop_Type())
arubaWiredVsxKeepAlivePacketsDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxKeepAlivePacketsDrop.setStatus(_A)
_ArubaWiredVsxKeepAliveTimeoutCount_Type=Integer32
_ArubaWiredVsxKeepAliveTimeoutCount_Object=MibScalar
arubaWiredVsxKeepAliveTimeoutCount=_ArubaWiredVsxKeepAliveTimeoutCount_Object((1,3,6,1,4,1,47196,4,1,1,3,7,2,2,5),_ArubaWiredVsxKeepAliveTimeoutCount_Type())
arubaWiredVsxKeepAliveTimeoutCount.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxKeepAliveTimeoutCount.setStatus(_A)
_ArubaWiredVsxKeepAliveLastEstablishedTime_Type=TimeTicks
_ArubaWiredVsxKeepAliveLastEstablishedTime_Object=MibScalar
arubaWiredVsxKeepAliveLastEstablishedTime=_ArubaWiredVsxKeepAliveLastEstablishedTime_Object((1,3,6,1,4,1,47196,4,1,1,3,7,2,2,6),_ArubaWiredVsxKeepAliveLastEstablishedTime_Type())
arubaWiredVsxKeepAliveLastEstablishedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxKeepAliveLastEstablishedTime.setStatus(_A)
_ArubaWiredVsxKeepAliveLastFailedTime_Type=TimeTicks
_ArubaWiredVsxKeepAliveLastFailedTime_Object=MibScalar
arubaWiredVsxKeepAliveLastFailedTime=_ArubaWiredVsxKeepAliveLastFailedTime_Object((1,3,6,1,4,1,47196,4,1,1,3,7,2,2,7),_ArubaWiredVsxKeepAliveLastFailedTime_Type())
arubaWiredVsxKeepAliveLastFailedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaWiredVsxKeepAliveLastFailedTime.setStatus(_A)
_ArubaWiredVsxNotifications_ObjectIdentity=ObjectIdentity
arubaWiredVsxNotifications=_ArubaWiredVsxNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,7,3))
_ArubaWiredVsxTraps_ObjectIdentity=ObjectIdentity
arubaWiredVsxTraps=_ArubaWiredVsxTraps_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,7,3,1))
islUp=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,7,3,1,1))
if mibBuilder.loadTexts:islUp.setStatus(_A)
islDown=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,7,3,1,2))
if mibBuilder.loadTexts:islDown.setStatus(_A)
keepAliveUp=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,7,3,1,3))
if mibBuilder.loadTexts:keepAliveUp.setStatus(_A)
keepAliveDown=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,7,3,1,4))
if mibBuilder.loadTexts:keepAliveDown.setStatus(_A)
mclagLocalUpPeerUp=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,7,3,1,5))
mclagLocalUpPeerUp.setObjects((_E,_F))
if mibBuilder.loadTexts:mclagLocalUpPeerUp.setStatus(_A)
mclagLocalUpPeerDown=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,7,3,1,6))
mclagLocalUpPeerDown.setObjects((_E,_F))
if mibBuilder.loadTexts:mclagLocalUpPeerDown.setStatus(_A)
mclagLocalDownPeerUp=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,7,3,1,7))
mclagLocalDownPeerUp.setObjects((_E,_F))
if mibBuilder.loadTexts:mclagLocalDownPeerUp.setStatus(_A)
mclagLocalDownPeerDown=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,7,3,1,8))
mclagLocalDownPeerDown.setObjects((_E,_F))
if mibBuilder.loadTexts:mclagLocalDownPeerDown.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'VidList':VidList,'arubaWiredVsxMIB':arubaWiredVsxMIB,'arubaWiredVsxConfig':arubaWiredVsxConfig,'arubaWiredVsxIslConfig':arubaWiredVsxIslConfig,'arubaWiredVsxIslPort':arubaWiredVsxIslPort,'arubaWiredVsxIslHelloInterval':arubaWiredVsxIslHelloInterval,'arubaWiredVsxIslHoldTime':arubaWiredVsxIslHoldTime,'arubaWiredVsxIslHelloTimeout':arubaWiredVsxIslHelloTimeout,'arubaWiredVsxIslSystemID':arubaWiredVsxIslSystemID,'arubaWiredVsxIslPlatformName':arubaWiredVsxIslPlatformName,'arubaWiredVsxIslSwVersion':arubaWiredVsxIslSwVersion,'arubaWiredVsxIslVIDList':arubaWiredVsxIslVIDList,'arubaWiredVsxKeepAliveConfig':arubaWiredVsxKeepAliveConfig,'arubaWiredVsxKeepAliveSrcIPAddrType':arubaWiredVsxKeepAliveSrcIPAddrType,'arubaWiredVsxKeepAliveSrcIPAddr':arubaWiredVsxKeepAliveSrcIPAddr,'arubaWiredVsxKeepAliveVrf':arubaWiredVsxKeepAliveVrf,'arubaWiredVsxKeepAliveUdpPort':arubaWiredVsxKeepAliveUdpPort,'arubaWiredVsxKeepAlivePeerIPAddrType':arubaWiredVsxKeepAlivePeerIPAddrType,'arubaWiredVsxKeepAlivePeerIPAddr':arubaWiredVsxKeepAlivePeerIPAddr,'arubaWiredVsxKeepAliveHelloInterval':arubaWiredVsxKeepAliveHelloInterval,'arubaWiredVsxKeepAliveHelloTimeout':arubaWiredVsxKeepAliveHelloTimeout,'arubaWiredVsxKeepAliveSystemID':arubaWiredVsxKeepAliveSystemID,'arubaWiredVsxKeepAlivePlatformName':arubaWiredVsxKeepAlivePlatformName,'arubaWiredVsxKeepAliveSwVersion':arubaWiredVsxKeepAliveSwVersion,'arubaWiredVsxAggregatorConfig':arubaWiredVsxAggregatorConfig,'arubaWiredVsxAggregatorTable':arubaWiredVsxAggregatorTable,'arubaWiredVsxAggregatorEntry':arubaWiredVsxAggregatorEntry,_F:arubaWiredVsxAggregatorIndex,'arubaWiredVsxAggregatorType':arubaWiredVsxAggregatorType,'arubaWiredVsxVlanList':arubaWiredVsxVlanList,'arubaWiredVsxLoopProtectEnabled':arubaWiredVsxLoopProtectEnabled,'arubaWiredVsxLoadBalanceScheme':arubaWiredVsxLoadBalanceScheme,'arubaWiredVsxCosOverride':arubaWiredVsxCosOverride,'arubaWiredVsxDscpOverride':arubaWiredVsxDscpOverride,'arubaWiredVsxQoSTrust':arubaWiredVsxQoSTrust,'arubaWiredVsxGlobalConfiguration':arubaWiredVsxGlobalConfiguration,'arubaWiredVsxDeviceRole':arubaWiredVsxDeviceRole,'arubaWiredVsxConfigSync':arubaWiredVsxConfigSync,'arubaWiredVsxStatus':arubaWiredVsxStatus,'arubaWiredVsxIslStatus':arubaWiredVsxIslStatus,'arubaWiredVsxIslOperState':arubaWiredVsxIslOperState,'arubaWiredVsxIslPduTx':arubaWiredVsxIslPduTx,'arubaWiredVsxIslPduRx':arubaWiredVsxIslPduRx,'arubaWiredVsxIslHelloTx':arubaWiredVsxIslHelloTx,'arubaWiredVsxIslHelloRx':arubaWiredVsxIslHelloRx,'arubaWiredVsxDeviceOperSystemID':arubaWiredVsxDeviceOperSystemID,'arubaWiredVsxKeepAliveStatus':arubaWiredVsxKeepAliveStatus,'arubaWiredVsxKeepAliveOperState':arubaWiredVsxKeepAliveOperState,'arubaWiredVsxKeepAlivePacketsTx':arubaWiredVsxKeepAlivePacketsTx,'arubaWiredVsxKeepAlivePacketsRx':arubaWiredVsxKeepAlivePacketsRx,'arubaWiredVsxKeepAlivePacketsDrop':arubaWiredVsxKeepAlivePacketsDrop,'arubaWiredVsxKeepAliveTimeoutCount':arubaWiredVsxKeepAliveTimeoutCount,'arubaWiredVsxKeepAliveLastEstablishedTime':arubaWiredVsxKeepAliveLastEstablishedTime,'arubaWiredVsxKeepAliveLastFailedTime':arubaWiredVsxKeepAliveLastFailedTime,'arubaWiredVsxNotifications':arubaWiredVsxNotifications,'arubaWiredVsxTraps':arubaWiredVsxTraps,'islUp':islUp,'islDown':islDown,'keepAliveUp':keepAliveUp,'keepAliveDown':keepAliveDown,'mclagLocalUpPeerUp':mclagLocalUpPeerUp,'mclagLocalUpPeerDown':mclagLocalUpPeerDown,'mclagLocalDownPeerUp':mclagLocalDownPeerUp,'mclagLocalDownPeerDown':mclagLocalDownPeerDown})