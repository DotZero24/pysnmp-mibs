_w='h323RegistrationStatusGroupVer1'
_v='h323RegistrationMultipleGroupRegistrationGroupVer1'
_u='h323RegistrationMultipleRegistrationGroupVer1'
_t='h323RegistrationSingleRegistrationGroupVer1'
_s='h323RegistrationTimeToLive'
_r='h323RegistrationGkPort'
_q='h323RegistrationGkHost'
_p='h323GroupMultipleRegStaticRasPort'
_o='h323GroupMultipleRegRasPortSource'
_n='h323GroupMultipleRegLightweightTimeToLive'
_m='h323GroupMultipleRegLightweightEnable'
_l='h323GroupMultipleRegRetryTime'
_k='h323GroupMultipleRegGkDiscoveryMode'
_j='h323GroupMultipleRegEnable'
_i='h323MultipleRegStaticRasPort'
_h='h323MultipleRegRasPortSource'
_g='h323MultipleRegLightweightTimeToLive'
_f='h323MultipleRegLightweightEnable'
_e='h323MultipleRegRetryTime'
_d='h323MultipleRegGkDiscoveryMode'
_c='h323MultipleRegEnable'
_b='h323SingleRegStaticRasPort'
_a='h323SingleRegRasPortSource'
_Z='h323SingleRegLightweightTimeToLive'
_Y='h323SingleRegLightweightEnable'
_X='h323SingleRegRetryTime'
_W='h323SingleRegGkDiscoveryMode'
_V='ipAddressConfigH323GkIndex'
_U='not-accessible'
_T='ipAddressStatusH323GkIndex'
_S='MxIpDhcpSiteSpecificCode'
_R='groupIndex'
_Q='MX-LINE-GROUPING-MIB'
_P='manual'
_O='automatic'
_N='MxIpPort'
_M='ifIndex'
_L='IF-MIB'
_K='OctetString'
_J='MxIpAddress'
_I='static'
_H='dynamic'
_G='MxEnableState'
_F='read-only'
_E='Integer32'
_D='Unsigned32'
_C='read-write'
_B='MX-H323-REGISTRATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_L,_M)
h323,ipAddressConfigH323Dhcp,ipAddressConfigH323Static,ipAddressStatusH323=mibBuilder.importSymbols('MX-H323-MIB','h323','ipAddressConfigH323Dhcp','ipAddressConfigH323Static','ipAddressStatusH323')
groupIndex,=mibBuilder.importSymbols(_Q,_R)
ipAddressConfig,ipAddressStatus=mibBuilder.importSymbols('MX-SMI','ipAddressConfig','ipAddressStatus')
MxEnableState,MxIpAddress,MxIpDhcpSiteSpecificCode,MxIpPort=mibBuilder.importSymbols('MX-TC',_G,_J,_S,_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h323RegistrationMIB=ModuleIdentity((1,3,6,1,4,1,4935,20,30,1))
if mibBuilder.loadTexts:h323RegistrationMIB.setRevisions(('1903-03-28 00:00',))
_IpAddressStatusH323GatekeeperTable_Object=MibTable
ipAddressStatusH323GatekeeperTable=_IpAddressStatusH323GatekeeperTable_Object((1,3,6,1,4,1,4935,10,1,90,20))
if mibBuilder.loadTexts:ipAddressStatusH323GatekeeperTable.setStatus(_A)
_IpAddressStatusH323GatekeeperEntry_Object=MibTableRow
ipAddressStatusH323GatekeeperEntry=_IpAddressStatusH323GatekeeperEntry_Object((1,3,6,1,4,1,4935,10,1,90,20,1))
ipAddressStatusH323GatekeeperEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:ipAddressStatusH323GatekeeperEntry.setStatus(_A)
_IpAddressStatusH323GkIndex_Type=Unsigned32
_IpAddressStatusH323GkIndex_Object=MibTableColumn
ipAddressStatusH323GkIndex=_IpAddressStatusH323GkIndex_Object((1,3,6,1,4,1,4935,10,1,90,20,1,5),_IpAddressStatusH323GkIndex_Type())
ipAddressStatusH323GkIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:ipAddressStatusH323GkIndex.setStatus(_A)
class _IpAddressStatusH323GkHost_Type(MxIpAddress):defaultValue=OctetString('')
_IpAddressStatusH323GkHost_Type.__name__=_J
_IpAddressStatusH323GkHost_Object=MibTableColumn
ipAddressStatusH323GkHost=_IpAddressStatusH323GkHost_Object((1,3,6,1,4,1,4935,10,1,90,20,1,10),_IpAddressStatusH323GkHost_Type())
ipAddressStatusH323GkHost.setMaxAccess(_F)
if mibBuilder.loadTexts:ipAddressStatusH323GkHost.setStatus(_A)
class _IpAddressStatusH323GkPort_Type(MxIpPort):defaultValue=1719
_IpAddressStatusH323GkPort_Type.__name__=_N
_IpAddressStatusH323GkPort_Object=MibTableColumn
ipAddressStatusH323GkPort=_IpAddressStatusH323GkPort_Object((1,3,6,1,4,1,4935,10,1,90,20,1,15),_IpAddressStatusH323GkPort_Type())
ipAddressStatusH323GkPort.setMaxAccess(_F)
if mibBuilder.loadTexts:ipAddressStatusH323GkPort.setStatus(_A)
_IpAddressConfigH323GatekeeperTable_Object=MibTable
ipAddressConfigH323GatekeeperTable=_IpAddressConfigH323GatekeeperTable_Object((1,3,6,1,4,1,4935,15,1,90,10,15))
if mibBuilder.loadTexts:ipAddressConfigH323GatekeeperTable.setStatus(_A)
_IpAddressConfigH323GatekeeperEntry_Object=MibTableRow
ipAddressConfigH323GatekeeperEntry=_IpAddressConfigH323GatekeeperEntry_Object((1,3,6,1,4,1,4935,15,1,90,10,15,1))
ipAddressConfigH323GatekeeperEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:ipAddressConfigH323GatekeeperEntry.setStatus(_A)
_IpAddressConfigH323GkIndex_Type=Unsigned32
_IpAddressConfigH323GkIndex_Object=MibTableColumn
ipAddressConfigH323GkIndex=_IpAddressConfigH323GkIndex_Object((1,3,6,1,4,1,4935,15,1,90,10,15,1,5),_IpAddressConfigH323GkIndex_Type())
ipAddressConfigH323GkIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:ipAddressConfigH323GkIndex.setStatus(_A)
class _IpAddressConfigH323GkStaticHost_Type(MxIpAddress):defaultValue=OctetString('')
_IpAddressConfigH323GkStaticHost_Type.__name__=_J
_IpAddressConfigH323GkStaticHost_Object=MibTableColumn
ipAddressConfigH323GkStaticHost=_IpAddressConfigH323GkStaticHost_Object((1,3,6,1,4,1,4935,15,1,90,10,15,1,10),_IpAddressConfigH323GkStaticHost_Type())
ipAddressConfigH323GkStaticHost.setMaxAccess(_C)
if mibBuilder.loadTexts:ipAddressConfigH323GkStaticHost.setStatus(_A)
class _IpAddressConfigH323GkStaticPort_Type(MxIpPort):defaultValue=1719
_IpAddressConfigH323GkStaticPort_Type.__name__=_N
_IpAddressConfigH323GkStaticPort_Object=MibTableColumn
ipAddressConfigH323GkStaticPort=_IpAddressConfigH323GkStaticPort_Object((1,3,6,1,4,1,4935,15,1,90,10,15,1,15),_IpAddressConfigH323GkStaticPort_Type())
ipAddressConfigH323GkStaticPort.setMaxAccess(_F)
if mibBuilder.loadTexts:ipAddressConfigH323GkStaticPort.setStatus(_A)
class _H323GkDhcpSiteSpecificCode_Type(MxIpDhcpSiteSpecificCode):defaultValue=0
_H323GkDhcpSiteSpecificCode_Type.__name__=_S
_H323GkDhcpSiteSpecificCode_Object=MibScalar
h323GkDhcpSiteSpecificCode=_H323GkDhcpSiteSpecificCode_Object((1,3,6,1,4,1,4935,15,1,90,15,10),_H323GkDhcpSiteSpecificCode_Type())
h323GkDhcpSiteSpecificCode.setMaxAccess(_C)
if mibBuilder.loadTexts:h323GkDhcpSiteSpecificCode.setStatus(_A)
_H323RegistrationMIBObjects_ObjectIdentity=ObjectIdentity
h323RegistrationMIBObjects=_H323RegistrationMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,20,30,1,1))
class _H323RegMethod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('single',1),('multiple',2)))
_H323RegMethod_Type.__name__=_E
_H323RegMethod_Object=MibScalar
h323RegMethod=_H323RegMethod_Object((1,3,6,1,4,1,4935,20,30,1,1,5),_H323RegMethod_Type())
h323RegMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:h323RegMethod.setStatus(_A)
_H323RegistrationSingleRegistration_ObjectIdentity=ObjectIdentity
h323RegistrationSingleRegistration=_H323RegistrationSingleRegistration_ObjectIdentity((1,3,6,1,4,1,4935,20,30,1,1,10))
class _H323SingleRegGkDiscoveryMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_H323SingleRegGkDiscoveryMode_Type.__name__=_E
_H323SingleRegGkDiscoveryMode_Object=MibScalar
h323SingleRegGkDiscoveryMode=_H323SingleRegGkDiscoveryMode_Object((1,3,6,1,4,1,4935,20,30,1,1,10,5),_H323SingleRegGkDiscoveryMode_Type())
h323SingleRegGkDiscoveryMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h323SingleRegGkDiscoveryMode.setStatus(_A)
class _H323SingleRegRetryTime_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_H323SingleRegRetryTime_Type.__name__=_D
_H323SingleRegRetryTime_Object=MibScalar
h323SingleRegRetryTime=_H323SingleRegRetryTime_Object((1,3,6,1,4,1,4935,20,30,1,1,10,10),_H323SingleRegRetryTime_Type())
h323SingleRegRetryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h323SingleRegRetryTime.setStatus(_A)
class _H323SingleRegLightweightEnable_Type(MxEnableState):defaultValue=1
_H323SingleRegLightweightEnable_Type.__name__=_G
_H323SingleRegLightweightEnable_Object=MibScalar
h323SingleRegLightweightEnable=_H323SingleRegLightweightEnable_Object((1,3,6,1,4,1,4935,20,30,1,1,10,15),_H323SingleRegLightweightEnable_Type())
h323SingleRegLightweightEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h323SingleRegLightweightEnable.setStatus(_A)
class _H323SingleRegLightweightTimeToLive_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_H323SingleRegLightweightTimeToLive_Type.__name__=_D
_H323SingleRegLightweightTimeToLive_Object=MibScalar
h323SingleRegLightweightTimeToLive=_H323SingleRegLightweightTimeToLive_Object((1,3,6,1,4,1,4935,20,30,1,1,10,20),_H323SingleRegLightweightTimeToLive_Type())
h323SingleRegLightweightTimeToLive.setMaxAccess(_C)
if mibBuilder.loadTexts:h323SingleRegLightweightTimeToLive.setStatus(_A)
class _H323SingleRegRasPortSource_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_H323SingleRegRasPortSource_Type.__name__=_E
_H323SingleRegRasPortSource_Object=MibScalar
h323SingleRegRasPortSource=_H323SingleRegRasPortSource_Object((1,3,6,1,4,1,4935,20,30,1,1,10,30),_H323SingleRegRasPortSource_Type())
h323SingleRegRasPortSource.setMaxAccess(_C)
if mibBuilder.loadTexts:h323SingleRegRasPortSource.setStatus(_A)
class _H323SingleRegStaticRasPort_Type(Unsigned32):defaultValue=7000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1719,1720),ValueRangeConstraint(7000,65535))
_H323SingleRegStaticRasPort_Type.__name__=_D
_H323SingleRegStaticRasPort_Object=MibScalar
h323SingleRegStaticRasPort=_H323SingleRegStaticRasPort_Object((1,3,6,1,4,1,4935,20,30,1,1,10,35),_H323SingleRegStaticRasPort_Type())
h323SingleRegStaticRasPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h323SingleRegStaticRasPort.setStatus(_A)
class _H323SingleRegCallSignalingPortSource_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_H323SingleRegCallSignalingPortSource_Type.__name__=_E
_H323SingleRegCallSignalingPortSource_Object=MibScalar
h323SingleRegCallSignalingPortSource=_H323SingleRegCallSignalingPortSource_Object((1,3,6,1,4,1,4935,20,30,1,1,10,40),_H323SingleRegCallSignalingPortSource_Type())
h323SingleRegCallSignalingPortSource.setMaxAccess(_C)
if mibBuilder.loadTexts:h323SingleRegCallSignalingPortSource.setStatus(_A)
class _H323SingleRegStaticCallSignalingPort_Type(Unsigned32):defaultValue=7000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1719,1720),ValueRangeConstraint(7000,65535))
_H323SingleRegStaticCallSignalingPort_Type.__name__=_D
_H323SingleRegStaticCallSignalingPort_Object=MibScalar
h323SingleRegStaticCallSignalingPort=_H323SingleRegStaticCallSignalingPort_Object((1,3,6,1,4,1,4935,20,30,1,1,10,45),_H323SingleRegStaticCallSignalingPort_Type())
h323SingleRegStaticCallSignalingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h323SingleRegStaticCallSignalingPort.setStatus(_A)
_H323RegistrationMultipleRegistrationIfTable_Object=MibTable
h323RegistrationMultipleRegistrationIfTable=_H323RegistrationMultipleRegistrationIfTable_Object((1,3,6,1,4,1,4935,20,30,1,1,15))
if mibBuilder.loadTexts:h323RegistrationMultipleRegistrationIfTable.setStatus(_A)
_H323RegistrationMultipleRegistrationIfEntry_Object=MibTableRow
h323RegistrationMultipleRegistrationIfEntry=_H323RegistrationMultipleRegistrationIfEntry_Object((1,3,6,1,4,1,4935,20,30,1,1,15,1))
h323RegistrationMultipleRegistrationIfEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:h323RegistrationMultipleRegistrationIfEntry.setStatus(_A)
class _H323MultipleRegGroupIndex_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_H323MultipleRegGroupIndex_Type.__name__=_D
_H323MultipleRegGroupIndex_Object=MibTableColumn
h323MultipleRegGroupIndex=_H323MultipleRegGroupIndex_Object((1,3,6,1,4,1,4935,20,30,1,1,15,1,5),_H323MultipleRegGroupIndex_Type())
h323MultipleRegGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h323MultipleRegGroupIndex.setStatus(_A)
class _H323MultipleRegEnable_Type(MxEnableState):defaultValue=1
_H323MultipleRegEnable_Type.__name__=_G
_H323MultipleRegEnable_Object=MibTableColumn
h323MultipleRegEnable=_H323MultipleRegEnable_Object((1,3,6,1,4,1,4935,20,30,1,1,15,1,10),_H323MultipleRegEnable_Type())
h323MultipleRegEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h323MultipleRegEnable.setStatus(_A)
class _H323MultipleRegGkDiscoveryMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_H323MultipleRegGkDiscoveryMode_Type.__name__=_E
_H323MultipleRegGkDiscoveryMode_Object=MibTableColumn
h323MultipleRegGkDiscoveryMode=_H323MultipleRegGkDiscoveryMode_Object((1,3,6,1,4,1,4935,20,30,1,1,15,1,15),_H323MultipleRegGkDiscoveryMode_Type())
h323MultipleRegGkDiscoveryMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h323MultipleRegGkDiscoveryMode.setStatus(_A)
class _H323MultipleRegRetryTime_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_H323MultipleRegRetryTime_Type.__name__=_D
_H323MultipleRegRetryTime_Object=MibTableColumn
h323MultipleRegRetryTime=_H323MultipleRegRetryTime_Object((1,3,6,1,4,1,4935,20,30,1,1,15,1,20),_H323MultipleRegRetryTime_Type())
h323MultipleRegRetryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h323MultipleRegRetryTime.setStatus(_A)
class _H323MultipleRegLightweightEnable_Type(MxEnableState):defaultValue=1
_H323MultipleRegLightweightEnable_Type.__name__=_G
_H323MultipleRegLightweightEnable_Object=MibTableColumn
h323MultipleRegLightweightEnable=_H323MultipleRegLightweightEnable_Object((1,3,6,1,4,1,4935,20,30,1,1,15,1,25),_H323MultipleRegLightweightEnable_Type())
h323MultipleRegLightweightEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h323MultipleRegLightweightEnable.setStatus(_A)
class _H323MultipleRegLightweightTimeToLive_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_H323MultipleRegLightweightTimeToLive_Type.__name__=_D
_H323MultipleRegLightweightTimeToLive_Object=MibTableColumn
h323MultipleRegLightweightTimeToLive=_H323MultipleRegLightweightTimeToLive_Object((1,3,6,1,4,1,4935,20,30,1,1,15,1,30),_H323MultipleRegLightweightTimeToLive_Type())
h323MultipleRegLightweightTimeToLive.setMaxAccess(_C)
if mibBuilder.loadTexts:h323MultipleRegLightweightTimeToLive.setStatus(_A)
class _H323MultipleRegRasPortSource_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_H323MultipleRegRasPortSource_Type.__name__=_E
_H323MultipleRegRasPortSource_Object=MibTableColumn
h323MultipleRegRasPortSource=_H323MultipleRegRasPortSource_Object((1,3,6,1,4,1,4935,20,30,1,1,15,1,35),_H323MultipleRegRasPortSource_Type())
h323MultipleRegRasPortSource.setMaxAccess(_C)
if mibBuilder.loadTexts:h323MultipleRegRasPortSource.setStatus(_A)
class _H323MultipleRegStaticRasPort_Type(Unsigned32):defaultValue=7000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1719,1720),ValueRangeConstraint(7000,65535))
_H323MultipleRegStaticRasPort_Type.__name__=_D
_H323MultipleRegStaticRasPort_Object=MibTableColumn
h323MultipleRegStaticRasPort=_H323MultipleRegStaticRasPort_Object((1,3,6,1,4,1,4935,20,30,1,1,15,1,40),_H323MultipleRegStaticRasPort_Type())
h323MultipleRegStaticRasPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h323MultipleRegStaticRasPort.setStatus(_A)
class _H323MultipleRegCallSignalingPortSource_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_H323MultipleRegCallSignalingPortSource_Type.__name__=_E
_H323MultipleRegCallSignalingPortSource_Object=MibTableColumn
h323MultipleRegCallSignalingPortSource=_H323MultipleRegCallSignalingPortSource_Object((1,3,6,1,4,1,4935,20,30,1,1,15,1,45),_H323MultipleRegCallSignalingPortSource_Type())
h323MultipleRegCallSignalingPortSource.setMaxAccess(_C)
if mibBuilder.loadTexts:h323MultipleRegCallSignalingPortSource.setStatus(_A)
class _H323MultipleRegStaticCallSignalingPort_Type(Unsigned32):defaultValue=7000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1719,1720),ValueRangeConstraint(7000,65535))
_H323MultipleRegStaticCallSignalingPort_Type.__name__=_D
_H323MultipleRegStaticCallSignalingPort_Object=MibTableColumn
h323MultipleRegStaticCallSignalingPort=_H323MultipleRegStaticCallSignalingPort_Object((1,3,6,1,4,1,4935,20,30,1,1,15,1,50),_H323MultipleRegStaticCallSignalingPort_Type())
h323MultipleRegStaticCallSignalingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h323MultipleRegStaticCallSignalingPort.setStatus(_A)
_H323RegistrationMultipleRegistrationGroupTable_Object=MibTable
h323RegistrationMultipleRegistrationGroupTable=_H323RegistrationMultipleRegistrationGroupTable_Object((1,3,6,1,4,1,4935,20,30,1,1,17))
if mibBuilder.loadTexts:h323RegistrationMultipleRegistrationGroupTable.setStatus(_A)
_H323RegistrationMultipleRegistrationGroupEntry_Object=MibTableRow
h323RegistrationMultipleRegistrationGroupEntry=_H323RegistrationMultipleRegistrationGroupEntry_Object((1,3,6,1,4,1,4935,20,30,1,1,17,1))
h323RegistrationMultipleRegistrationGroupEntry.setIndexNames((0,_Q,_R))
if mibBuilder.loadTexts:h323RegistrationMultipleRegistrationGroupEntry.setStatus(_A)
class _H323GroupMultipleRegEnable_Type(MxEnableState):defaultValue=1
_H323GroupMultipleRegEnable_Type.__name__=_G
_H323GroupMultipleRegEnable_Object=MibTableColumn
h323GroupMultipleRegEnable=_H323GroupMultipleRegEnable_Object((1,3,6,1,4,1,4935,20,30,1,1,17,1,5),_H323GroupMultipleRegEnable_Type())
h323GroupMultipleRegEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h323GroupMultipleRegEnable.setStatus(_A)
class _H323GroupMultipleRegGkDiscoveryMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_H323GroupMultipleRegGkDiscoveryMode_Type.__name__=_E
_H323GroupMultipleRegGkDiscoveryMode_Object=MibTableColumn
h323GroupMultipleRegGkDiscoveryMode=_H323GroupMultipleRegGkDiscoveryMode_Object((1,3,6,1,4,1,4935,20,30,1,1,17,1,10),_H323GroupMultipleRegGkDiscoveryMode_Type())
h323GroupMultipleRegGkDiscoveryMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h323GroupMultipleRegGkDiscoveryMode.setStatus(_A)
class _H323GroupMultipleRegRetryTime_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_H323GroupMultipleRegRetryTime_Type.__name__=_D
_H323GroupMultipleRegRetryTime_Object=MibTableColumn
h323GroupMultipleRegRetryTime=_H323GroupMultipleRegRetryTime_Object((1,3,6,1,4,1,4935,20,30,1,1,17,1,15),_H323GroupMultipleRegRetryTime_Type())
h323GroupMultipleRegRetryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h323GroupMultipleRegRetryTime.setStatus(_A)
class _H323GroupMultipleRegLightweightEnable_Type(MxEnableState):defaultValue=1
_H323GroupMultipleRegLightweightEnable_Type.__name__=_G
_H323GroupMultipleRegLightweightEnable_Object=MibTableColumn
h323GroupMultipleRegLightweightEnable=_H323GroupMultipleRegLightweightEnable_Object((1,3,6,1,4,1,4935,20,30,1,1,17,1,20),_H323GroupMultipleRegLightweightEnable_Type())
h323GroupMultipleRegLightweightEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h323GroupMultipleRegLightweightEnable.setStatus(_A)
class _H323GroupMultipleRegLightweightTimeToLive_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_H323GroupMultipleRegLightweightTimeToLive_Type.__name__=_D
_H323GroupMultipleRegLightweightTimeToLive_Object=MibTableColumn
h323GroupMultipleRegLightweightTimeToLive=_H323GroupMultipleRegLightweightTimeToLive_Object((1,3,6,1,4,1,4935,20,30,1,1,17,1,25),_H323GroupMultipleRegLightweightTimeToLive_Type())
h323GroupMultipleRegLightweightTimeToLive.setMaxAccess(_C)
if mibBuilder.loadTexts:h323GroupMultipleRegLightweightTimeToLive.setStatus(_A)
class _H323GroupMultipleRegRasPortSource_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_H323GroupMultipleRegRasPortSource_Type.__name__=_E
_H323GroupMultipleRegRasPortSource_Object=MibTableColumn
h323GroupMultipleRegRasPortSource=_H323GroupMultipleRegRasPortSource_Object((1,3,6,1,4,1,4935,20,30,1,1,17,1,30),_H323GroupMultipleRegRasPortSource_Type())
h323GroupMultipleRegRasPortSource.setMaxAccess(_C)
if mibBuilder.loadTexts:h323GroupMultipleRegRasPortSource.setStatus(_A)
class _H323GroupMultipleRegStaticRasPort_Type(Unsigned32):defaultValue=7000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1719,1720),ValueRangeConstraint(7000,65535))
_H323GroupMultipleRegStaticRasPort_Type.__name__=_D
_H323GroupMultipleRegStaticRasPort_Object=MibTableColumn
h323GroupMultipleRegStaticRasPort=_H323GroupMultipleRegStaticRasPort_Object((1,3,6,1,4,1,4935,20,30,1,1,17,1,35),_H323GroupMultipleRegStaticRasPort_Type())
h323GroupMultipleRegStaticRasPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h323GroupMultipleRegStaticRasPort.setStatus(_A)
class _H323GroupMultipleRegCallSignalingPortSource_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_H323GroupMultipleRegCallSignalingPortSource_Type.__name__=_E
_H323GroupMultipleRegCallSignalingPortSource_Object=MibTableColumn
h323GroupMultipleRegCallSignalingPortSource=_H323GroupMultipleRegCallSignalingPortSource_Object((1,3,6,1,4,1,4935,20,30,1,1,17,1,40),_H323GroupMultipleRegCallSignalingPortSource_Type())
h323GroupMultipleRegCallSignalingPortSource.setMaxAccess(_C)
if mibBuilder.loadTexts:h323GroupMultipleRegCallSignalingPortSource.setStatus(_A)
class _H323GroupMultipleRegStaticCallSignalingPort_Type(Unsigned32):defaultValue=7000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1719,1720),ValueRangeConstraint(7000,65535))
_H323GroupMultipleRegStaticCallSignalingPort_Type.__name__=_D
_H323GroupMultipleRegStaticCallSignalingPort_Object=MibTableColumn
h323GroupMultipleRegStaticCallSignalingPort=_H323GroupMultipleRegStaticCallSignalingPort_Object((1,3,6,1,4,1,4935,20,30,1,1,17,1,45),_H323GroupMultipleRegStaticCallSignalingPort_Type())
h323GroupMultipleRegStaticCallSignalingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h323GroupMultipleRegStaticCallSignalingPort.setStatus(_A)
_H323RegistrationStatusIfTable_Object=MibTable
h323RegistrationStatusIfTable=_H323RegistrationStatusIfTable_Object((1,3,6,1,4,1,4935,20,30,1,1,19))
if mibBuilder.loadTexts:h323RegistrationStatusIfTable.setStatus(_A)
_H323RegistrationStatusIfEntry_Object=MibTableRow
h323RegistrationStatusIfEntry=_H323RegistrationStatusIfEntry_Object((1,3,6,1,4,1,4935,20,30,1,1,19,1))
h323RegistrationStatusIfEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:h323RegistrationStatusIfEntry.setStatus(_A)
class _H323RegistrationGkHost_Type(MxIpAddress):defaultValue=OctetString('')
_H323RegistrationGkHost_Type.__name__=_J
_H323RegistrationGkHost_Object=MibTableColumn
h323RegistrationGkHost=_H323RegistrationGkHost_Object((1,3,6,1,4,1,4935,20,30,1,1,19,1,5),_H323RegistrationGkHost_Type())
h323RegistrationGkHost.setMaxAccess(_F)
if mibBuilder.loadTexts:h323RegistrationGkHost.setStatus(_A)
class _H323RegistrationGkPort_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_H323RegistrationGkPort_Type.__name__=_K
_H323RegistrationGkPort_Object=MibTableColumn
h323RegistrationGkPort=_H323RegistrationGkPort_Object((1,3,6,1,4,1,4935,20,30,1,1,19,1,10),_H323RegistrationGkPort_Type())
h323RegistrationGkPort.setMaxAccess(_F)
if mibBuilder.loadTexts:h323RegistrationGkPort.setStatus(_A)
class _H323RegistrationTimeToLive_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_H323RegistrationTimeToLive_Type.__name__=_K
_H323RegistrationTimeToLive_Object=MibTableColumn
h323RegistrationTimeToLive=_H323RegistrationTimeToLive_Object((1,3,6,1,4,1,4935,20,30,1,1,19,1,15),_H323RegistrationTimeToLive_Type())
h323RegistrationTimeToLive.setMaxAccess(_F)
if mibBuilder.loadTexts:h323RegistrationTimeToLive.setStatus(_A)
_H323RegistrationConformance_ObjectIdentity=ObjectIdentity
h323RegistrationConformance=_H323RegistrationConformance_ObjectIdentity((1,3,6,1,4,1,4935,20,30,1,2))
_H323RegistrationCompliances_ObjectIdentity=ObjectIdentity
h323RegistrationCompliances=_H323RegistrationCompliances_ObjectIdentity((1,3,6,1,4,1,4935,20,30,1,2,1))
_H323RegistrationGroups_ObjectIdentity=ObjectIdentity
h323RegistrationGroups=_H323RegistrationGroups_ObjectIdentity((1,3,6,1,4,1,4935,20,30,1,2,2))
h323RegistrationSingleRegistrationGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,30,1,2,2,5))
h323RegistrationSingleRegistrationGroupVer1.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:h323RegistrationSingleRegistrationGroupVer1.setStatus(_A)
h323RegistrationMultipleRegistrationGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,30,1,2,2,10))
h323RegistrationMultipleRegistrationGroupVer1.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:h323RegistrationMultipleRegistrationGroupVer1.setStatus(_A)
h323RegistrationMultipleGroupRegistrationGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,30,1,2,2,15))
h323RegistrationMultipleGroupRegistrationGroupVer1.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:h323RegistrationMultipleGroupRegistrationGroupVer1.setStatus(_A)
h323RegistrationStatusGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,30,1,2,2,20))
h323RegistrationStatusGroupVer1.setObjects(*((_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:h323RegistrationStatusGroupVer1.setStatus(_A)
h323RegistrationBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,20,30,1,2,1,5))
h323RegistrationBasicComplVer1.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:h323RegistrationBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ipAddressStatusH323GatekeeperTable':ipAddressStatusH323GatekeeperTable,'ipAddressStatusH323GatekeeperEntry':ipAddressStatusH323GatekeeperEntry,_T:ipAddressStatusH323GkIndex,'ipAddressStatusH323GkHost':ipAddressStatusH323GkHost,'ipAddressStatusH323GkPort':ipAddressStatusH323GkPort,'ipAddressConfigH323GatekeeperTable':ipAddressConfigH323GatekeeperTable,'ipAddressConfigH323GatekeeperEntry':ipAddressConfigH323GatekeeperEntry,_V:ipAddressConfigH323GkIndex,'ipAddressConfigH323GkStaticHost':ipAddressConfigH323GkStaticHost,'ipAddressConfigH323GkStaticPort':ipAddressConfigH323GkStaticPort,'h323GkDhcpSiteSpecificCode':h323GkDhcpSiteSpecificCode,'h323RegistrationMIB':h323RegistrationMIB,'h323RegistrationMIBObjects':h323RegistrationMIBObjects,'h323RegMethod':h323RegMethod,'h323RegistrationSingleRegistration':h323RegistrationSingleRegistration,_W:h323SingleRegGkDiscoveryMode,_X:h323SingleRegRetryTime,_Y:h323SingleRegLightweightEnable,_Z:h323SingleRegLightweightTimeToLive,_a:h323SingleRegRasPortSource,_b:h323SingleRegStaticRasPort,'h323SingleRegCallSignalingPortSource':h323SingleRegCallSignalingPortSource,'h323SingleRegStaticCallSignalingPort':h323SingleRegStaticCallSignalingPort,'h323RegistrationMultipleRegistrationIfTable':h323RegistrationMultipleRegistrationIfTable,'h323RegistrationMultipleRegistrationIfEntry':h323RegistrationMultipleRegistrationIfEntry,'h323MultipleRegGroupIndex':h323MultipleRegGroupIndex,_c:h323MultipleRegEnable,_d:h323MultipleRegGkDiscoveryMode,_e:h323MultipleRegRetryTime,_f:h323MultipleRegLightweightEnable,_g:h323MultipleRegLightweightTimeToLive,_h:h323MultipleRegRasPortSource,_i:h323MultipleRegStaticRasPort,'h323MultipleRegCallSignalingPortSource':h323MultipleRegCallSignalingPortSource,'h323MultipleRegStaticCallSignalingPort':h323MultipleRegStaticCallSignalingPort,'h323RegistrationMultipleRegistrationGroupTable':h323RegistrationMultipleRegistrationGroupTable,'h323RegistrationMultipleRegistrationGroupEntry':h323RegistrationMultipleRegistrationGroupEntry,_j:h323GroupMultipleRegEnable,_k:h323GroupMultipleRegGkDiscoveryMode,_l:h323GroupMultipleRegRetryTime,_m:h323GroupMultipleRegLightweightEnable,_n:h323GroupMultipleRegLightweightTimeToLive,_o:h323GroupMultipleRegRasPortSource,_p:h323GroupMultipleRegStaticRasPort,'h323GroupMultipleRegCallSignalingPortSource':h323GroupMultipleRegCallSignalingPortSource,'h323GroupMultipleRegStaticCallSignalingPort':h323GroupMultipleRegStaticCallSignalingPort,'h323RegistrationStatusIfTable':h323RegistrationStatusIfTable,'h323RegistrationStatusIfEntry':h323RegistrationStatusIfEntry,_q:h323RegistrationGkHost,_r:h323RegistrationGkPort,_s:h323RegistrationTimeToLive,'h323RegistrationConformance':h323RegistrationConformance,'h323RegistrationCompliances':h323RegistrationCompliances,'h323RegistrationBasicComplVer1':h323RegistrationBasicComplVer1,'h323RegistrationGroups':h323RegistrationGroups,_t:h323RegistrationSingleRegistrationGroupVer1,_u:h323RegistrationMultipleRegistrationGroupVer1,_v:h323RegistrationMultipleGroupRegistrationGroupVer1,_w:h323RegistrationStatusGroupVer1})