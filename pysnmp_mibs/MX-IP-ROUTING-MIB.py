_f='ipRoutingBandwidthControlGroupVer1'
_e='ipRoutingMacSpoofGroupVer1'
_d='ipRoutingLanInterfaceGroupVer1'
_c='ipRoutingQosGroupVer1'
_b='ipRoutingDhcpGroupVer1'
_a='ipRoutingGroupVer1'
_Z='ipRoutingWanUpstreamBandwidth'
_Y='ipRoutingBandwidthControlEnable'
_X='ipRoutingMacSpoofAddress'
_W='ipRoutingMacSpoofEnable'
_V='lanStaticNetworkMask'
_U='lanStaticAddress'
_T='ipRoutingQosDiffServSubstitution'
_S='ipRoutingQosDiffServSubstitutionEnable'
_R='ipRoutingDhcpServerNoWanLeaseTime'
_Q='ipRoutingDhcpServerNoWanLeaseEnable'
_P='ipRoutingDhcpServerDnsFallbackEnable'
_O='ipRoutingDhcpIpLeaseRangeEnd'
_N='ipRoutingDhcpIpLeaseRangeStart'
_M='ipRoutingDhcpServerLeaseTime'
_L='ipRoutingDhcpServerEnable'
_K='ipRoutingMode'
_J='ipRoutingEnable'
_I='MxIpSubnetMask'
_H='Integer32'
_G='OctetString'
_F='MxIpAddress'
_E='Unsigned32'
_D='MxEnableState'
_C='read-write'
_B='MX-IP-ROUTING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipAddressConfig,mediatrixConfig,mediatrixMgmt=mibBuilder.importSymbols('MX-SMI','ipAddressConfig','mediatrixConfig','mediatrixMgmt')
MxEnableState,MxIpAddress,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC',_D,_F,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ipRoutingMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,110))
if mibBuilder.loadTexts:ipRoutingMIB.setRevisions(('2011-05-09 00:00','2008-07-03 00:00','2006-03-06 00:00','2005-09-16 00:00','2005-08-12 00:00','2005-05-20 00:00','2005-04-22 00:00','2004-09-28 00:00','2004-07-14 00:00','2004-02-13 00:00','2003-10-24 00:00','2003-10-01 00:00','2003-09-15 00:00'))
_IpRoutingStatus_ObjectIdentity=ObjectIdentity
ipRoutingStatus=_IpRoutingStatus_ObjectIdentity((1,3,6,1,4,1,4935,10,70))
class _IpRoutingMacAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(12,12))
_IpRoutingMacAddress_Type.__name__=_G
_IpRoutingMacAddress_Object=MibScalar
ipRoutingMacAddress=_IpRoutingMacAddress_Object((1,3,6,1,4,1,4935,10,70,25),_IpRoutingMacAddress_Type())
ipRoutingMacAddress.setMaxAccess('read-only')
if mibBuilder.loadTexts:ipRoutingMacAddress.setStatus(_A)
_IpAddressConfigLanInterface_ObjectIdentity=ObjectIdentity
ipAddressConfigLanInterface=_IpAddressConfigLanInterface_ObjectIdentity((1,3,6,1,4,1,4935,15,1,100))
class _LanStaticAddressActivation_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ipRouting',0),('vlanSubstitution',1),('always',2)))
_LanStaticAddressActivation_Type.__name__=_H
_LanStaticAddressActivation_Object=MibScalar
lanStaticAddressActivation=_LanStaticAddressActivation_Object((1,3,6,1,4,1,4935,15,1,100,3),_LanStaticAddressActivation_Type())
lanStaticAddressActivation.setMaxAccess(_C)
if mibBuilder.loadTexts:lanStaticAddressActivation.setStatus(_A)
class _LanStaticAddress_Type(MxIpAddress):defaultValue=OctetString('192.168.10.1')
_LanStaticAddress_Type.__name__=_F
_LanStaticAddress_Object=MibScalar
lanStaticAddress=_LanStaticAddress_Object((1,3,6,1,4,1,4935,15,1,100,5),_LanStaticAddress_Type())
lanStaticAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:lanStaticAddress.setStatus(_A)
class _LanStaticNetworkMask_Type(MxIpSubnetMask):defaultValue=OctetString('255.255.255.0')
_LanStaticNetworkMask_Type.__name__=_I
_LanStaticNetworkMask_Object=MibScalar
lanStaticNetworkMask=_LanStaticNetworkMask_Object((1,3,6,1,4,1,4935,15,1,100,10),_LanStaticNetworkMask_Type())
lanStaticNetworkMask.setMaxAccess(_C)
if mibBuilder.loadTexts:lanStaticNetworkMask.setStatus(_A)
_IpRoutingMIBObjects_ObjectIdentity=ObjectIdentity
ipRoutingMIBObjects=_IpRoutingMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,110,1))
class _IpRoutingEnable_Type(MxEnableState):defaultValue=0
_IpRoutingEnable_Type.__name__=_D
_IpRoutingEnable_Object=MibScalar
ipRoutingEnable=_IpRoutingEnable_Object((1,3,6,1,4,1,4935,15,110,1,5),_IpRoutingEnable_Type())
ipRoutingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRoutingEnable.setStatus(_A)
class _IpRoutingMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('tas',0),('nat',1),('normal',2)))
_IpRoutingMode_Type.__name__=_H
_IpRoutingMode_Object=MibScalar
ipRoutingMode=_IpRoutingMode_Object((1,3,6,1,4,1,4935,15,110,1,7),_IpRoutingMode_Type())
ipRoutingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRoutingMode.setStatus(_A)
_IpRoutingDhcp_ObjectIdentity=ObjectIdentity
ipRoutingDhcp=_IpRoutingDhcp_ObjectIdentity((1,3,6,1,4,1,4935,15,110,1,10))
class _IpRoutingDhcpServerEnable_Type(MxEnableState):defaultValue=1
_IpRoutingDhcpServerEnable_Type.__name__=_D
_IpRoutingDhcpServerEnable_Object=MibScalar
ipRoutingDhcpServerEnable=_IpRoutingDhcpServerEnable_Object((1,3,6,1,4,1,4935,15,110,1,10,3),_IpRoutingDhcpServerEnable_Type())
ipRoutingDhcpServerEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRoutingDhcpServerEnable.setStatus(_A)
class _IpRoutingDhcpServerLeaseTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,172800))
_IpRoutingDhcpServerLeaseTime_Type.__name__=_E
_IpRoutingDhcpServerLeaseTime_Object=MibScalar
ipRoutingDhcpServerLeaseTime=_IpRoutingDhcpServerLeaseTime_Object((1,3,6,1,4,1,4935,15,110,1,10,5),_IpRoutingDhcpServerLeaseTime_Type())
ipRoutingDhcpServerLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRoutingDhcpServerLeaseTime.setStatus(_A)
class _IpRoutingDhcpIpLeaseRangeStart_Type(MxIpAddress):defaultValue=OctetString('192.168.10.2')
_IpRoutingDhcpIpLeaseRangeStart_Type.__name__=_F
_IpRoutingDhcpIpLeaseRangeStart_Object=MibScalar
ipRoutingDhcpIpLeaseRangeStart=_IpRoutingDhcpIpLeaseRangeStart_Object((1,3,6,1,4,1,4935,15,110,1,10,50),_IpRoutingDhcpIpLeaseRangeStart_Type())
ipRoutingDhcpIpLeaseRangeStart.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRoutingDhcpIpLeaseRangeStart.setStatus(_A)
class _IpRoutingDhcpIpLeaseRangeEnd_Type(MxIpAddress):defaultValue=OctetString('192.168.10.254')
_IpRoutingDhcpIpLeaseRangeEnd_Type.__name__=_F
_IpRoutingDhcpIpLeaseRangeEnd_Object=MibScalar
ipRoutingDhcpIpLeaseRangeEnd=_IpRoutingDhcpIpLeaseRangeEnd_Object((1,3,6,1,4,1,4935,15,110,1,10,100),_IpRoutingDhcpIpLeaseRangeEnd_Type())
ipRoutingDhcpIpLeaseRangeEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRoutingDhcpIpLeaseRangeEnd.setStatus(_A)
class _IpRoutingDhcpServerDnsFallbackEnable_Type(MxEnableState):defaultValue=0
_IpRoutingDhcpServerDnsFallbackEnable_Type.__name__=_D
_IpRoutingDhcpServerDnsFallbackEnable_Object=MibScalar
ipRoutingDhcpServerDnsFallbackEnable=_IpRoutingDhcpServerDnsFallbackEnable_Object((1,3,6,1,4,1,4935,15,110,1,10,150),_IpRoutingDhcpServerDnsFallbackEnable_Type())
ipRoutingDhcpServerDnsFallbackEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRoutingDhcpServerDnsFallbackEnable.setStatus(_A)
class _IpRoutingDhcpServerNoWanLeaseEnable_Type(MxEnableState):defaultValue=0
_IpRoutingDhcpServerNoWanLeaseEnable_Type.__name__=_D
_IpRoutingDhcpServerNoWanLeaseEnable_Object=MibScalar
ipRoutingDhcpServerNoWanLeaseEnable=_IpRoutingDhcpServerNoWanLeaseEnable_Object((1,3,6,1,4,1,4935,15,110,1,10,200),_IpRoutingDhcpServerNoWanLeaseEnable_Type())
ipRoutingDhcpServerNoWanLeaseEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRoutingDhcpServerNoWanLeaseEnable.setStatus(_A)
class _IpRoutingDhcpServerNoWanLeaseTime_Type(Unsigned32):defaultValue=180;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,172800))
_IpRoutingDhcpServerNoWanLeaseTime_Type.__name__=_E
_IpRoutingDhcpServerNoWanLeaseTime_Object=MibScalar
ipRoutingDhcpServerNoWanLeaseTime=_IpRoutingDhcpServerNoWanLeaseTime_Object((1,3,6,1,4,1,4935,15,110,1,10,250),_IpRoutingDhcpServerNoWanLeaseTime_Type())
ipRoutingDhcpServerNoWanLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRoutingDhcpServerNoWanLeaseTime.setStatus(_A)
_IpRoutingQos_ObjectIdentity=ObjectIdentity
ipRoutingQos=_IpRoutingQos_ObjectIdentity((1,3,6,1,4,1,4935,15,110,1,15))
class _IpRoutingQosDiffServSubstitutionEnable_Type(MxEnableState):defaultValue=0
_IpRoutingQosDiffServSubstitutionEnable_Type.__name__=_D
_IpRoutingQosDiffServSubstitutionEnable_Object=MibScalar
ipRoutingQosDiffServSubstitutionEnable=_IpRoutingQosDiffServSubstitutionEnable_Object((1,3,6,1,4,1,4935,15,110,1,15,5),_IpRoutingQosDiffServSubstitutionEnable_Type())
ipRoutingQosDiffServSubstitutionEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRoutingQosDiffServSubstitutionEnable.setStatus(_A)
class _IpRoutingQosDiffServSubstitution_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IpRoutingQosDiffServSubstitution_Type.__name__=_E
_IpRoutingQosDiffServSubstitution_Object=MibScalar
ipRoutingQosDiffServSubstitution=_IpRoutingQosDiffServSubstitution_Object((1,3,6,1,4,1,4935,15,110,1,15,10),_IpRoutingQosDiffServSubstitution_Type())
ipRoutingQosDiffServSubstitution.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRoutingQosDiffServSubstitution.setStatus(_A)
_IpRoutingMacSpoof_ObjectIdentity=ObjectIdentity
ipRoutingMacSpoof=_IpRoutingMacSpoof_ObjectIdentity((1,3,6,1,4,1,4935,15,110,1,20))
class _IpRoutingMacSpoofEnable_Type(MxEnableState):defaultValue=0
_IpRoutingMacSpoofEnable_Type.__name__=_D
_IpRoutingMacSpoofEnable_Object=MibScalar
ipRoutingMacSpoofEnable=_IpRoutingMacSpoofEnable_Object((1,3,6,1,4,1,4935,15,110,1,20,10),_IpRoutingMacSpoofEnable_Type())
ipRoutingMacSpoofEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRoutingMacSpoofEnable.setStatus(_A)
class _IpRoutingMacSpoofAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(12,12))
_IpRoutingMacSpoofAddress_Type.__name__=_G
_IpRoutingMacSpoofAddress_Object=MibScalar
ipRoutingMacSpoofAddress=_IpRoutingMacSpoofAddress_Object((1,3,6,1,4,1,4935,15,110,1,20,20),_IpRoutingMacSpoofAddress_Type())
ipRoutingMacSpoofAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRoutingMacSpoofAddress.setStatus(_A)
_IpRoutingBandwidthControl_ObjectIdentity=ObjectIdentity
ipRoutingBandwidthControl=_IpRoutingBandwidthControl_ObjectIdentity((1,3,6,1,4,1,4935,15,110,1,30))
class _IpRoutingBandwidthControlEnable_Type(MxEnableState):defaultValue=0
_IpRoutingBandwidthControlEnable_Type.__name__=_D
_IpRoutingBandwidthControlEnable_Object=MibScalar
ipRoutingBandwidthControlEnable=_IpRoutingBandwidthControlEnable_Object((1,3,6,1,4,1,4935,15,110,1,30,5),_IpRoutingBandwidthControlEnable_Type())
ipRoutingBandwidthControlEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRoutingBandwidthControlEnable.setStatus(_A)
class _IpRoutingWanUpstreamBandwidth_Type(Unsigned32):defaultValue=512;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,4096))
_IpRoutingWanUpstreamBandwidth_Type.__name__=_E
_IpRoutingWanUpstreamBandwidth_Object=MibScalar
ipRoutingWanUpstreamBandwidth=_IpRoutingWanUpstreamBandwidth_Object((1,3,6,1,4,1,4935,15,110,1,30,10),_IpRoutingWanUpstreamBandwidth_Type())
ipRoutingWanUpstreamBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRoutingWanUpstreamBandwidth.setStatus(_A)
_IpRoutingConformance_ObjectIdentity=ObjectIdentity
ipRoutingConformance=_IpRoutingConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,110,2))
_IpRoutingCompliances_ObjectIdentity=ObjectIdentity
ipRoutingCompliances=_IpRoutingCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,110,2,1))
_IpRoutingGroups_ObjectIdentity=ObjectIdentity
ipRoutingGroups=_IpRoutingGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,110,2,5))
ipRoutingGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,110,2,5,5))
ipRoutingGroupVer1.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ipRoutingGroupVer1.setStatus(_A)
ipRoutingDhcpGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,110,2,5,10))
ipRoutingDhcpGroupVer1.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ipRoutingDhcpGroupVer1.setStatus(_A)
ipRoutingQosGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,110,2,5,15))
ipRoutingQosGroupVer1.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ipRoutingQosGroupVer1.setStatus(_A)
ipRoutingLanInterfaceGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,110,2,5,20))
ipRoutingLanInterfaceGroupVer1.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:ipRoutingLanInterfaceGroupVer1.setStatus(_A)
ipRoutingMacSpoofGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,110,2,5,25))
ipRoutingMacSpoofGroupVer1.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ipRoutingMacSpoofGroupVer1.setStatus(_A)
ipRoutingBandwidthControlGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,110,2,5,30))
ipRoutingBandwidthControlGroupVer1.setObjects(*((_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:ipRoutingBandwidthControlGroupVer1.setStatus(_A)
ipRoutingComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,110,2,1,1))
ipRoutingComplVer1.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:ipRoutingComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ipRoutingStatus':ipRoutingStatus,'ipRoutingMacAddress':ipRoutingMacAddress,'ipAddressConfigLanInterface':ipAddressConfigLanInterface,'lanStaticAddressActivation':lanStaticAddressActivation,_U:lanStaticAddress,_V:lanStaticNetworkMask,'ipRoutingMIB':ipRoutingMIB,'ipRoutingMIBObjects':ipRoutingMIBObjects,_J:ipRoutingEnable,_K:ipRoutingMode,'ipRoutingDhcp':ipRoutingDhcp,_L:ipRoutingDhcpServerEnable,_M:ipRoutingDhcpServerLeaseTime,_N:ipRoutingDhcpIpLeaseRangeStart,_O:ipRoutingDhcpIpLeaseRangeEnd,_P:ipRoutingDhcpServerDnsFallbackEnable,_Q:ipRoutingDhcpServerNoWanLeaseEnable,_R:ipRoutingDhcpServerNoWanLeaseTime,'ipRoutingQos':ipRoutingQos,_S:ipRoutingQosDiffServSubstitutionEnable,_T:ipRoutingQosDiffServSubstitution,'ipRoutingMacSpoof':ipRoutingMacSpoof,_W:ipRoutingMacSpoofEnable,_X:ipRoutingMacSpoofAddress,'ipRoutingBandwidthControl':ipRoutingBandwidthControl,_Y:ipRoutingBandwidthControlEnable,_Z:ipRoutingWanUpstreamBandwidth,'ipRoutingConformance':ipRoutingConformance,'ipRoutingCompliances':ipRoutingCompliances,'ipRoutingComplVer1':ipRoutingComplVer1,'ipRoutingGroups':ipRoutingGroups,_a:ipRoutingGroupVer1,_b:ipRoutingDhcpGroupVer1,_c:ipRoutingQosGroupVer1,_d:ipRoutingLanInterfaceGroupVer1,_e:ipRoutingMacSpoofGroupVer1,_f:ipRoutingBandwidthControlGroupVer1})