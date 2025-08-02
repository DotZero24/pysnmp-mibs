_Af='hpicfVsfVCConfigScalarGroup2'
_Ae='hpicfVsfVCConfigScalarGroup'
_Ad='hpicfVsfVCStackTopoChange'
_Ac='hpicfVsfVCActiveMemberCount'
_Ab='hpicfVsfVCMemberCount'
_Aa='hpicfVsfVCPortOperStatusErrorStr'
_AZ='hpicfVsfVCPortOperStatus'
_AY='hpicfVsfVCLldpMADActiveFragment'
_AX='hpicfVsfVCLldpMADProbeResponseRcvd'
_AW='hpicfVsfVCLldpMADProbeRequestsSent'
_AV='hpicfVsfVCLldpMADProbeOriginator'
_AU='hpicfVsfVCLldpMADSplitStatus'
_AT='hpicfVsfVCLldpMADConnectivity'
_AS='hpicfVsfVCLldpMADProbePortSet'
_AR='hpicfVsfVCLldpMADTrunkIfIndex'
_AQ='hpicfVsfVCLldpMADVlanId'
_AP='hpicfVsfVCLldpMADDeviceMAC'
_AO='hpicfVsfVCLldpMADReadinessStatus'
_AN='hpicfVsfVCLinkPortStartState'
_AM='hpicfVsfVCLinkIdForTrap'
_AL='hpicfVsfVCLinkEntryStatus'
_AK='hpicfVsfVCLinkPortList'
_AJ='hpicfVsfVCPeerLinkId'
_AI='hpicfVsfVCPeerMemberId'
_AH='hpicfVsfVCLinkOperStatus'
_AG='hpicfVsfVCLinkName'
_AF='hpicfVsfVCMemberFreeMemory'
_AE='hpicfVsfVCMemberTotalMemory'
_AD='hpicfVsfVCMemberCpuUtil'
_AC='hpicfVsfVCMemberRenumber'
_AB='hpicfVsfVCMemberBootImage'
_AA='hpicfVsfVCMemberOsVersion'
_A9='hpicfVsfVCMemberBootRomVersion'
_A8='hpicfVsfVCMemberSerialNum'
_A7='hpicfVsfVCMemberSysOid'
_A6='hpicfVsfVCMemberUpTime'
_A5='hpicfVsfVCMemberProductName'
_A4='hpicfVsfVCMemberEntPhysicalIndex'
_A3='hpicfVsfVCMemberEntryStatus'
_A2='hpicfVsfVCMemberAdminPriority'
_A1='hpicfVsfVCMemberReboot'
_A0='hpicfVsfVCMemberShutdown'
_z='hpicfVsfVCMemberMacAddr'
_y='hpicfVsfVCMemberProductId'
_x='hpicfVsfVCLinkId'
_w='hpicfVsfVCLinkMemberId'
_v='accessible-for-notify'
_u='hpicfVsfVCMemberId'
_t='partial'
_s='DisplayString'
_r='hpSwitchBaseMACAddress'
_q='NETSWITCH-MIB'
_p='ifIndex'
_o='IF-MIB'
_n='hpicfVsfVCNotificationsGroup1'
_m='hpicfVsfVCConfigScalarGroup1'
_l='hpicfVsfVCNotificationsGroup'
_k='hpicfVsfVCMemberStatusChange'
_j='hpicfVsfVCMemberChange'
_i='hpicfVsfVCCommanderChange'
_h='hpicfVsfVCPortSpeed'
_g='hpicfVsfMADVlanConnectivity'
_f='hpicfVsfMADVlan'
_e='not-accessible'
_d='yes'
_c='disabled'
_b='hpicfVsfVCLldpMADSnmpCommunity'
_a='hpicfVsfVCLldpMADSnmpVersion'
_Z='hpicfVsfVCLldpMADDeviceIpAddr'
_Y='hpicfVsfVCLldpMADDeviceIpType'
_X='hpicfVsfVCOobmMADEnable'
_W='hpicfVsfLldpMADEnable'
_V='hpicfVsfVCTrapEnable'
_U='hpicfVsfVCAdminStatus'
_T='hpicfVsfVCOperStatus'
_S='hpicfVsfVCDomainId'
_R='none'
_Q='OctetString'
_P='hpicfVsfVCPortTableGroup'
_O='hpicfVsfVCStatusScalarGroup'
_N='hpicfVsfVCLinkTableGroup'
_M='hpicfVsfVCMemberTableGroup'
_L='hpicfVsfVCMemberState'
_K='hpicfVsfVCTopology'
_J='disable'
_I='enable'
_H='hpicfVsfVCMemberIdForTrap'
_G='deprecated'
_F='read-create'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='HP-VSF-VC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Q,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_o,'InterfaceIndexOrZero',_p)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
hpSwitchBaseMACAddress,=mibBuilder.importSymbols(_q,_r)
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_s,'PhysAddress','RowStatus','TextualConvention','TruthValue')
hpicfVsfVCMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,116))
if mibBuilder.loadTexts:hpicfVsfVCMIB.setRevisions(('2021-01-22 00:00','2020-09-29 00:00','2020-09-21 00:00','2016-06-22 00:00','2016-05-09 00:00','2015-03-04 00:00'))
_HpicfVsfVCNotifications_ObjectIdentity=ObjectIdentity
hpicfVsfVCNotifications=_HpicfVsfVCNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,116,0))
_HpicfVsfVCObjects_ObjectIdentity=ObjectIdentity
hpicfVsfVCObjects=_HpicfVsfVCObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,116,1))
_HpicfVsfVCConfig_ObjectIdentity=ObjectIdentity
hpicfVsfVCConfig=_HpicfVsfVCConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1))
_HpicfVsfVCDomainId_Type=Unsigned32
_HpicfVsfVCDomainId_Object=MibScalar
hpicfVsfVCDomainId=_HpicfVsfVCDomainId_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1,1),_HpicfVsfVCDomainId_Type())
hpicfVsfVCDomainId.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVsfVCDomainId.setStatus(_B)
class _HpicfVsfVCOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('unAvailable',0),(_c,1),('active',2),('fragmentInactive',3),('fragmentActive',4)))
_HpicfVsfVCOperStatus_Type.__name__=_D
_HpicfVsfVCOperStatus_Object=MibScalar
hpicfVsfVCOperStatus=_HpicfVsfVCOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1,2),_HpicfVsfVCOperStatus_Type())
hpicfVsfVCOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCOperStatus.setStatus(_B)
class _HpicfVsfVCAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HpicfVsfVCAdminStatus_Type.__name__=_D
_HpicfVsfVCAdminStatus_Object=MibScalar
hpicfVsfVCAdminStatus=_HpicfVsfVCAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1,3),_HpicfVsfVCAdminStatus_Type())
hpicfVsfVCAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVsfVCAdminStatus.setStatus(_B)
class _HpicfVsfVCTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('unknown',0),('chain',1),('ring',2),('mesh',3),('partialMesh',4)))
_HpicfVsfVCTopology_Type.__name__=_D
_HpicfVsfVCTopology_Object=MibScalar
hpicfVsfVCTopology=_HpicfVsfVCTopology_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1,4),_HpicfVsfVCTopology_Type())
hpicfVsfVCTopology.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCTopology.setStatus(_B)
class _HpicfVsfVCTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HpicfVsfVCTrapEnable_Type.__name__=_D
_HpicfVsfVCTrapEnable_Object=MibScalar
hpicfVsfVCTrapEnable=_HpicfVsfVCTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1,5),_HpicfVsfVCTrapEnable_Type())
hpicfVsfVCTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVsfVCTrapEnable.setStatus(_B)
class _HpicfVsfVCOobmMADEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HpicfVsfVCOobmMADEnable_Type.__name__=_D
_HpicfVsfVCOobmMADEnable_Object=MibScalar
hpicfVsfVCOobmMADEnable=_HpicfVsfVCOobmMADEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1,6),_HpicfVsfVCOobmMADEnable_Type())
hpicfVsfVCOobmMADEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVsfVCOobmMADEnable.setStatus(_B)
class _HpicfVsfLldpMADEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HpicfVsfLldpMADEnable_Type.__name__=_D
_HpicfVsfLldpMADEnable_Object=MibScalar
hpicfVsfLldpMADEnable=_HpicfVsfLldpMADEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1,7),_HpicfVsfLldpMADEnable_Type())
hpicfVsfLldpMADEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVsfLldpMADEnable.setStatus(_B)
_HpicfVsfVCLldpMADDeviceIpType_Type=InetAddressType
_HpicfVsfVCLldpMADDeviceIpType_Object=MibScalar
hpicfVsfVCLldpMADDeviceIpType=_HpicfVsfVCLldpMADDeviceIpType_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1,8),_HpicfVsfVCLldpMADDeviceIpType_Type())
hpicfVsfVCLldpMADDeviceIpType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVsfVCLldpMADDeviceIpType.setStatus(_B)
_HpicfVsfVCLldpMADDeviceIpAddr_Type=InetAddress
_HpicfVsfVCLldpMADDeviceIpAddr_Object=MibScalar
hpicfVsfVCLldpMADDeviceIpAddr=_HpicfVsfVCLldpMADDeviceIpAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1,9),_HpicfVsfVCLldpMADDeviceIpAddr_Type())
hpicfVsfVCLldpMADDeviceIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVsfVCLldpMADDeviceIpAddr.setStatus(_B)
class _HpicfVsfVCLldpMADSnmpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('v2c',2))
_HpicfVsfVCLldpMADSnmpVersion_Type.__name__=_D
_HpicfVsfVCLldpMADSnmpVersion_Object=MibScalar
hpicfVsfVCLldpMADSnmpVersion=_HpicfVsfVCLldpMADSnmpVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1,10),_HpicfVsfVCLldpMADSnmpVersion_Type())
hpicfVsfVCLldpMADSnmpVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVsfVCLldpMADSnmpVersion.setStatus(_B)
class _HpicfVsfVCLldpMADSnmpCommunity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpicfVsfVCLldpMADSnmpCommunity_Type.__name__=_Q
_HpicfVsfVCLldpMADSnmpCommunity_Object=MibScalar
hpicfVsfVCLldpMADSnmpCommunity=_HpicfVsfVCLldpMADSnmpCommunity_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1,11),_HpicfVsfVCLldpMADSnmpCommunity_Type())
hpicfVsfVCLldpMADSnmpCommunity.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVsfVCLldpMADSnmpCommunity.setStatus(_B)
class _HpicfVsfMADVlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpicfVsfMADVlan_Type.__name__=_D
_HpicfVsfMADVlan_Object=MibScalar
hpicfVsfMADVlan=_HpicfVsfMADVlan_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1,12),_HpicfVsfMADVlan_Type())
hpicfVsfMADVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVsfMADVlan.setStatus(_B)
class _HpicfVsfMADVlanConnectivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('full',2),(_t,3)))
_HpicfVsfMADVlanConnectivity_Type.__name__=_D
_HpicfVsfMADVlanConnectivity_Object=MibScalar
hpicfVsfMADVlanConnectivity=_HpicfVsfMADVlanConnectivity_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1,13),_HpicfVsfMADVlanConnectivity_Type())
hpicfVsfMADVlanConnectivity.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfMADVlanConnectivity.setStatus(_B)
class _HpicfVsfVCPortSpeed_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_R,0),('oneGbps',1),('tenGbps',2),('fortyGbps',3)))
_HpicfVsfVCPortSpeed_Type.__name__=_D
_HpicfVsfVCPortSpeed_Object=MibScalar
hpicfVsfVCPortSpeed=_HpicfVsfVCPortSpeed_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1,14),_HpicfVsfVCPortSpeed_Type())
hpicfVsfVCPortSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVsfVCPortSpeed.setStatus(_B)
class _HpicfVsfVCMemberCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_HpicfVsfVCMemberCount_Type.__name__=_D
_HpicfVsfVCMemberCount_Object=MibScalar
hpicfVsfVCMemberCount=_HpicfVsfVCMemberCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1,15),_HpicfVsfVCMemberCount_Type())
hpicfVsfVCMemberCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCMemberCount.setStatus(_B)
class _HpicfVsfVCActiveMemberCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_HpicfVsfVCActiveMemberCount_Type.__name__=_D
_HpicfVsfVCActiveMemberCount_Object=MibScalar
hpicfVsfVCActiveMemberCount=_HpicfVsfVCActiveMemberCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,1,16),_HpicfVsfVCActiveMemberCount_Type())
hpicfVsfVCActiveMemberCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCActiveMemberCount.setStatus(_B)
_HpicfVsfVCStatus_ObjectIdentity=ObjectIdentity
hpicfVsfVCStatus=_HpicfVsfVCStatus_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,116,1,2))
class _HpicfVsfVCLldpMADReadinessStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_R,0),('success',1),('failure',2)))
_HpicfVsfVCLldpMADReadinessStatus_Type.__name__=_D
_HpicfVsfVCLldpMADReadinessStatus_Object=MibScalar
hpicfVsfVCLldpMADReadinessStatus=_HpicfVsfVCLldpMADReadinessStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,2,1),_HpicfVsfVCLldpMADReadinessStatus_Type())
hpicfVsfVCLldpMADReadinessStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCLldpMADReadinessStatus.setStatus(_B)
class _HpicfVsfVCLldpMADDeviceMAC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(6,6))
_HpicfVsfVCLldpMADDeviceMAC_Type.__name__=_Q
_HpicfVsfVCLldpMADDeviceMAC_Object=MibScalar
hpicfVsfVCLldpMADDeviceMAC=_HpicfVsfVCLldpMADDeviceMAC_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,2,2),_HpicfVsfVCLldpMADDeviceMAC_Type())
hpicfVsfVCLldpMADDeviceMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCLldpMADDeviceMAC.setStatus(_B)
class _HpicfVsfVCLldpMADVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_HpicfVsfVCLldpMADVlanId_Type.__name__=_D
_HpicfVsfVCLldpMADVlanId_Object=MibScalar
hpicfVsfVCLldpMADVlanId=_HpicfVsfVCLldpMADVlanId_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,2,3),_HpicfVsfVCLldpMADVlanId_Type())
hpicfVsfVCLldpMADVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCLldpMADVlanId.setStatus(_B)
_HpicfVsfVCLldpMADTrunkIfIndex_Type=InterfaceIndexOrZero
_HpicfVsfVCLldpMADTrunkIfIndex_Object=MibScalar
hpicfVsfVCLldpMADTrunkIfIndex=_HpicfVsfVCLldpMADTrunkIfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,2,4),_HpicfVsfVCLldpMADTrunkIfIndex_Type())
hpicfVsfVCLldpMADTrunkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCLldpMADTrunkIfIndex.setStatus(_B)
_HpicfVsfVCLldpMADProbePortSet_Type=PortList
_HpicfVsfVCLldpMADProbePortSet_Object=MibScalar
hpicfVsfVCLldpMADProbePortSet=_HpicfVsfVCLldpMADProbePortSet_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,2,5),_HpicfVsfVCLldpMADProbePortSet_Type())
hpicfVsfVCLldpMADProbePortSet.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCLldpMADProbePortSet.setStatus(_B)
class _HpicfVsfVCLldpMADConnectivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('full',2),(_t,3)))
_HpicfVsfVCLldpMADConnectivity_Type.__name__=_D
_HpicfVsfVCLldpMADConnectivity_Object=MibScalar
hpicfVsfVCLldpMADConnectivity=_HpicfVsfVCLldpMADConnectivity_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,2,6),_HpicfVsfVCLldpMADConnectivity_Type())
hpicfVsfVCLldpMADConnectivity.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCLldpMADConnectivity.setStatus(_B)
class _HpicfVsfVCLldpMADSplitStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),('no',2)))
_HpicfVsfVCLldpMADSplitStatus_Type.__name__=_D
_HpicfVsfVCLldpMADSplitStatus_Object=MibScalar
hpicfVsfVCLldpMADSplitStatus=_HpicfVsfVCLldpMADSplitStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,2,7),_HpicfVsfVCLldpMADSplitStatus_Type())
hpicfVsfVCLldpMADSplitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCLldpMADSplitStatus.setStatus(_B)
class _HpicfVsfVCLldpMADProbeOriginator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),('no',2)))
_HpicfVsfVCLldpMADProbeOriginator_Type.__name__=_D
_HpicfVsfVCLldpMADProbeOriginator_Object=MibScalar
hpicfVsfVCLldpMADProbeOriginator=_HpicfVsfVCLldpMADProbeOriginator_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,2,8),_HpicfVsfVCLldpMADProbeOriginator_Type())
hpicfVsfVCLldpMADProbeOriginator.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCLldpMADProbeOriginator.setStatus(_B)
_HpicfVsfVCLldpMADProbeRequestsSent_Type=Counter32
_HpicfVsfVCLldpMADProbeRequestsSent_Object=MibScalar
hpicfVsfVCLldpMADProbeRequestsSent=_HpicfVsfVCLldpMADProbeRequestsSent_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,2,9),_HpicfVsfVCLldpMADProbeRequestsSent_Type())
hpicfVsfVCLldpMADProbeRequestsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCLldpMADProbeRequestsSent.setStatus(_B)
_HpicfVsfVCLldpMADProbeResponseRcvd_Type=Counter32
_HpicfVsfVCLldpMADProbeResponseRcvd_Object=MibScalar
hpicfVsfVCLldpMADProbeResponseRcvd=_HpicfVsfVCLldpMADProbeResponseRcvd_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,2,10),_HpicfVsfVCLldpMADProbeResponseRcvd_Type())
hpicfVsfVCLldpMADProbeResponseRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCLldpMADProbeResponseRcvd.setStatus(_B)
class _HpicfVsfVCLldpMADActiveFragment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),('no',2)))
_HpicfVsfVCLldpMADActiveFragment_Type.__name__=_D
_HpicfVsfVCLldpMADActiveFragment_Object=MibScalar
hpicfVsfVCLldpMADActiveFragment=_HpicfVsfVCLldpMADActiveFragment_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,2,11),_HpicfVsfVCLldpMADActiveFragment_Type())
hpicfVsfVCLldpMADActiveFragment.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCLldpMADActiveFragment.setStatus(_B)
_HpicfVsfVCMemberTable_Object=MibTable
hpicfVsfVCMemberTable=_HpicfVsfVCMemberTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3))
if mibBuilder.loadTexts:hpicfVsfVCMemberTable.setStatus(_B)
_HpicfVsfVCMemberEntry_Object=MibTableRow
hpicfVsfVCMemberEntry=_HpicfVsfVCMemberEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1))
hpicfVsfVCMemberEntry.setIndexNames((0,_A,_u))
if mibBuilder.loadTexts:hpicfVsfVCMemberEntry.setStatus(_B)
class _HpicfVsfVCMemberId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfVsfVCMemberId_Type.__name__=_D
_HpicfVsfVCMemberId_Object=MibTableColumn
hpicfVsfVCMemberId=_HpicfVsfVCMemberId_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,1),_HpicfVsfVCMemberId_Type())
hpicfVsfVCMemberId.setMaxAccess(_e)
if mibBuilder.loadTexts:hpicfVsfVCMemberId.setStatus(_B)
_HpicfVsfVCMemberProductId_Type=DisplayString
_HpicfVsfVCMemberProductId_Object=MibTableColumn
hpicfVsfVCMemberProductId=_HpicfVsfVCMemberProductId_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,2),_HpicfVsfVCMemberProductId_Type())
hpicfVsfVCMemberProductId.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfVsfVCMemberProductId.setStatus(_B)
class _HpicfVsfVCMemberMacAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(6,6))
_HpicfVsfVCMemberMacAddr_Type.__name__=_Q
_HpicfVsfVCMemberMacAddr_Object=MibTableColumn
hpicfVsfVCMemberMacAddr=_HpicfVsfVCMemberMacAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,3),_HpicfVsfVCMemberMacAddr_Type())
hpicfVsfVCMemberMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfVsfVCMemberMacAddr.setStatus(_B)
_HpicfVsfVCMemberShutdown_Type=TruthValue
_HpicfVsfVCMemberShutdown_Object=MibTableColumn
hpicfVsfVCMemberShutdown=_HpicfVsfVCMemberShutdown_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,4),_HpicfVsfVCMemberShutdown_Type())
hpicfVsfVCMemberShutdown.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfVsfVCMemberShutdown.setStatus(_B)
_HpicfVsfVCMemberReboot_Type=TruthValue
_HpicfVsfVCMemberReboot_Object=MibTableColumn
hpicfVsfVCMemberReboot=_HpicfVsfVCMemberReboot_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,5),_HpicfVsfVCMemberReboot_Type())
hpicfVsfVCMemberReboot.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfVsfVCMemberReboot.setStatus(_B)
class _HpicfVsfVCMemberAdminPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpicfVsfVCMemberAdminPriority_Type.__name__=_D
_HpicfVsfVCMemberAdminPriority_Object=MibTableColumn
hpicfVsfVCMemberAdminPriority=_HpicfVsfVCMemberAdminPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,6),_HpicfVsfVCMemberAdminPriority_Type())
hpicfVsfVCMemberAdminPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfVsfVCMemberAdminPriority.setStatus(_B)
_HpicfVsfVCMemberEntryStatus_Type=RowStatus
_HpicfVsfVCMemberEntryStatus_Object=MibTableColumn
hpicfVsfVCMemberEntryStatus=_HpicfVsfVCMemberEntryStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,7),_HpicfVsfVCMemberEntryStatus_Type())
hpicfVsfVCMemberEntryStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfVsfVCMemberEntryStatus.setStatus(_B)
_HpicfVsfVCMemberEntPhysicalIndex_Type=PhysicalIndex
_HpicfVsfVCMemberEntPhysicalIndex_Object=MibTableColumn
hpicfVsfVCMemberEntPhysicalIndex=_HpicfVsfVCMemberEntPhysicalIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,8),_HpicfVsfVCMemberEntPhysicalIndex_Type())
hpicfVsfVCMemberEntPhysicalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCMemberEntPhysicalIndex.setStatus(_B)
class _HpicfVsfVCMemberState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('unusedId',0),('missing',1),('provision',2),('commander',3),('standby',4),('member',5),('shutdown',6),('booting',7),('communicationFailure',8),('incompatibleOS',9),('unknownState',10),('standbyBooting',11)))
_HpicfVsfVCMemberState_Type.__name__=_D
_HpicfVsfVCMemberState_Object=MibTableColumn
hpicfVsfVCMemberState=_HpicfVsfVCMemberState_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,9),_HpicfVsfVCMemberState_Type())
hpicfVsfVCMemberState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCMemberState.setStatus(_B)
_HpicfVsfVCMemberProductName_Type=SnmpAdminString
_HpicfVsfVCMemberProductName_Object=MibTableColumn
hpicfVsfVCMemberProductName=_HpicfVsfVCMemberProductName_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,10),_HpicfVsfVCMemberProductName_Type())
hpicfVsfVCMemberProductName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCMemberProductName.setStatus(_B)
_HpicfVsfVCMemberUpTime_Type=TimeTicks
_HpicfVsfVCMemberUpTime_Object=MibTableColumn
hpicfVsfVCMemberUpTime=_HpicfVsfVCMemberUpTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,11),_HpicfVsfVCMemberUpTime_Type())
hpicfVsfVCMemberUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCMemberUpTime.setStatus(_B)
_HpicfVsfVCMemberSysOid_Type=ObjectIdentifier
_HpicfVsfVCMemberSysOid_Object=MibTableColumn
hpicfVsfVCMemberSysOid=_HpicfVsfVCMemberSysOid_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,12),_HpicfVsfVCMemberSysOid_Type())
hpicfVsfVCMemberSysOid.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCMemberSysOid.setStatus(_B)
_HpicfVsfVCMemberIdForTrap_Type=Integer32
_HpicfVsfVCMemberIdForTrap_Object=MibTableColumn
hpicfVsfVCMemberIdForTrap=_HpicfVsfVCMemberIdForTrap_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,13),_HpicfVsfVCMemberIdForTrap_Type())
hpicfVsfVCMemberIdForTrap.setMaxAccess(_v)
if mibBuilder.loadTexts:hpicfVsfVCMemberIdForTrap.setStatus(_B)
_HpicfVsfVCMemberSerialNum_Type=DisplayString
_HpicfVsfVCMemberSerialNum_Object=MibTableColumn
hpicfVsfVCMemberSerialNum=_HpicfVsfVCMemberSerialNum_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,14),_HpicfVsfVCMemberSerialNum_Type())
hpicfVsfVCMemberSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCMemberSerialNum.setStatus(_B)
_HpicfVsfVCMemberBootRomVersion_Type=DisplayString
_HpicfVsfVCMemberBootRomVersion_Object=MibTableColumn
hpicfVsfVCMemberBootRomVersion=_HpicfVsfVCMemberBootRomVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,15),_HpicfVsfVCMemberBootRomVersion_Type())
hpicfVsfVCMemberBootRomVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCMemberBootRomVersion.setStatus(_B)
_HpicfVsfVCMemberOsVersion_Type=DisplayString
_HpicfVsfVCMemberOsVersion_Object=MibTableColumn
hpicfVsfVCMemberOsVersion=_HpicfVsfVCMemberOsVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,16),_HpicfVsfVCMemberOsVersion_Type())
hpicfVsfVCMemberOsVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCMemberOsVersion.setStatus(_B)
class _HpicfVsfVCMemberBootImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_HpicfVsfVCMemberBootImage_Type.__name__=_D
_HpicfVsfVCMemberBootImage_Object=MibTableColumn
hpicfVsfVCMemberBootImage=_HpicfVsfVCMemberBootImage_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,17),_HpicfVsfVCMemberBootImage_Type())
hpicfVsfVCMemberBootImage.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCMemberBootImage.setStatus(_B)
_HpicfVsfVCMemberRenumber_Type=Integer32
_HpicfVsfVCMemberRenumber_Object=MibTableColumn
hpicfVsfVCMemberRenumber=_HpicfVsfVCMemberRenumber_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,18),_HpicfVsfVCMemberRenumber_Type())
hpicfVsfVCMemberRenumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVsfVCMemberRenumber.setStatus(_B)
_HpicfVsfVCMemberCpuUtil_Type=Integer32
_HpicfVsfVCMemberCpuUtil_Object=MibTableColumn
hpicfVsfVCMemberCpuUtil=_HpicfVsfVCMemberCpuUtil_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,19),_HpicfVsfVCMemberCpuUtil_Type())
hpicfVsfVCMemberCpuUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCMemberCpuUtil.setStatus(_B)
_HpicfVsfVCMemberTotalMemory_Type=Integer32
_HpicfVsfVCMemberTotalMemory_Object=MibTableColumn
hpicfVsfVCMemberTotalMemory=_HpicfVsfVCMemberTotalMemory_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,20),_HpicfVsfVCMemberTotalMemory_Type())
hpicfVsfVCMemberTotalMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCMemberTotalMemory.setStatus(_B)
_HpicfVsfVCMemberFreeMemory_Type=Integer32
_HpicfVsfVCMemberFreeMemory_Object=MibTableColumn
hpicfVsfVCMemberFreeMemory=_HpicfVsfVCMemberFreeMemory_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,3,1,21),_HpicfVsfVCMemberFreeMemory_Type())
hpicfVsfVCMemberFreeMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCMemberFreeMemory.setStatus(_B)
_HpicfVsfVCLinkTable_Object=MibTable
hpicfVsfVCLinkTable=_HpicfVsfVCLinkTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,4))
if mibBuilder.loadTexts:hpicfVsfVCLinkTable.setStatus(_B)
_HpicfVsfVCLinkEntry_Object=MibTableRow
hpicfVsfVCLinkEntry=_HpicfVsfVCLinkEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,4,1))
hpicfVsfVCLinkEntry.setIndexNames((0,_A,_w),(0,_A,_x))
if mibBuilder.loadTexts:hpicfVsfVCLinkEntry.setStatus(_B)
class _HpicfVsfVCLinkMemberId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfVsfVCLinkMemberId_Type.__name__=_D
_HpicfVsfVCLinkMemberId_Object=MibTableColumn
hpicfVsfVCLinkMemberId=_HpicfVsfVCLinkMemberId_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,4,1,1),_HpicfVsfVCLinkMemberId_Type())
hpicfVsfVCLinkMemberId.setMaxAccess(_e)
if mibBuilder.loadTexts:hpicfVsfVCLinkMemberId.setStatus(_B)
class _HpicfVsfVCLinkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_HpicfVsfVCLinkId_Type.__name__=_D
_HpicfVsfVCLinkId_Object=MibTableColumn
hpicfVsfVCLinkId=_HpicfVsfVCLinkId_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,4,1,2),_HpicfVsfVCLinkId_Type())
hpicfVsfVCLinkId.setMaxAccess(_e)
if mibBuilder.loadTexts:hpicfVsfVCLinkId.setStatus(_B)
class _HpicfVsfVCLinkName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_HpicfVsfVCLinkName_Type.__name__=_s
_HpicfVsfVCLinkName_Object=MibTableColumn
hpicfVsfVCLinkName=_HpicfVsfVCLinkName_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,4,1,3),_HpicfVsfVCLinkName_Type())
hpicfVsfVCLinkName.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVsfVCLinkName.setStatus(_B)
class _HpicfVsfVCLinkOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_c,3)))
_HpicfVsfVCLinkOperStatus_Type.__name__=_D
_HpicfVsfVCLinkOperStatus_Object=MibTableColumn
hpicfVsfVCLinkOperStatus=_HpicfVsfVCLinkOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,4,1,4),_HpicfVsfVCLinkOperStatus_Type())
hpicfVsfVCLinkOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCLinkOperStatus.setStatus(_B)
_HpicfVsfVCPeerMemberId_Type=Integer32
_HpicfVsfVCPeerMemberId_Object=MibTableColumn
hpicfVsfVCPeerMemberId=_HpicfVsfVCPeerMemberId_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,4,1,5),_HpicfVsfVCPeerMemberId_Type())
hpicfVsfVCPeerMemberId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCPeerMemberId.setStatus(_B)
_HpicfVsfVCPeerLinkId_Type=Integer32
_HpicfVsfVCPeerLinkId_Object=MibTableColumn
hpicfVsfVCPeerLinkId=_HpicfVsfVCPeerLinkId_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,4,1,6),_HpicfVsfVCPeerLinkId_Type())
hpicfVsfVCPeerLinkId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCPeerLinkId.setStatus(_B)
_HpicfVsfVCLinkPortList_Type=PortList
_HpicfVsfVCLinkPortList_Object=MibTableColumn
hpicfVsfVCLinkPortList=_HpicfVsfVCLinkPortList_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,4,1,7),_HpicfVsfVCLinkPortList_Type())
hpicfVsfVCLinkPortList.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVsfVCLinkPortList.setStatus(_B)
_HpicfVsfVCLinkEntryStatus_Type=RowStatus
_HpicfVsfVCLinkEntryStatus_Object=MibTableColumn
hpicfVsfVCLinkEntryStatus=_HpicfVsfVCLinkEntryStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,4,1,8),_HpicfVsfVCLinkEntryStatus_Type())
hpicfVsfVCLinkEntryStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfVsfVCLinkEntryStatus.setStatus(_B)
_HpicfVsfVCLinkIdForTrap_Type=Integer32
_HpicfVsfVCLinkIdForTrap_Object=MibTableColumn
hpicfVsfVCLinkIdForTrap=_HpicfVsfVCLinkIdForTrap_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,4,1,9),_HpicfVsfVCLinkIdForTrap_Type())
hpicfVsfVCLinkIdForTrap.setMaxAccess(_v)
if mibBuilder.loadTexts:hpicfVsfVCLinkIdForTrap.setStatus(_B)
class _HpicfVsfVCLinkPortStartState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HpicfVsfVCLinkPortStartState_Type.__name__=_D
_HpicfVsfVCLinkPortStartState_Object=MibTableColumn
hpicfVsfVCLinkPortStartState=_HpicfVsfVCLinkPortStartState_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,4,1,10),_HpicfVsfVCLinkPortStartState_Type())
hpicfVsfVCLinkPortStartState.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfVsfVCLinkPortStartState.setStatus(_B)
_HpicfVsfVCPortTable_Object=MibTable
hpicfVsfVCPortTable=_HpicfVsfVCPortTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,5))
if mibBuilder.loadTexts:hpicfVsfVCPortTable.setStatus(_B)
_HpicfVsfVCPortEntry_Object=MibTableRow
hpicfVsfVCPortEntry=_HpicfVsfVCPortEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,5,1))
hpicfVsfVCPortEntry.setIndexNames((0,_o,_p))
if mibBuilder.loadTexts:hpicfVsfVCPortEntry.setStatus(_B)
class _HpicfVsfVCPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('up',1),('down',2),('error',3),(_c,4),('provisioned',5)))
_HpicfVsfVCPortOperStatus_Type.__name__=_D
_HpicfVsfVCPortOperStatus_Object=MibTableColumn
hpicfVsfVCPortOperStatus=_HpicfVsfVCPortOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,5,1,1),_HpicfVsfVCPortOperStatus_Type())
hpicfVsfVCPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCPortOperStatus.setStatus(_B)
_HpicfVsfVCPortOperStatusErrorStr_Type=DisplayString
_HpicfVsfVCPortOperStatusErrorStr_Object=MibTableColumn
hpicfVsfVCPortOperStatusErrorStr=_HpicfVsfVCPortOperStatusErrorStr_Object((1,3,6,1,4,1,11,2,14,11,5,1,116,1,5,1,2),_HpicfVsfVCPortOperStatusErrorStr_Type())
hpicfVsfVCPortOperStatusErrorStr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVsfVCPortOperStatusErrorStr.setStatus(_B)
_HpicfVsfVCConformance_ObjectIdentity=ObjectIdentity
hpicfVsfVCConformance=_HpicfVsfVCConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,116,2))
_HpicfVsfVCCompliances_ObjectIdentity=ObjectIdentity
hpicfVsfVCCompliances=_HpicfVsfVCCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,116,2,1))
_HpicfVsfVCGroups_ObjectIdentity=ObjectIdentity
hpicfVsfVCGroups=_HpicfVsfVCGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,116,2,2))
hpicfVsfVCConfigScalarGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,116,2,2,1))
hpicfVsfVCConfigScalarGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_K),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:hpicfVsfVCConfigScalarGroup.setStatus(_G)
hpicfVsfVCMemberTableGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,116,2,2,2))
hpicfVsfVCMemberTableGroup.setObjects(*((_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_L),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_H),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:hpicfVsfVCMemberTableGroup.setStatus(_B)
hpicfVsfVCLinkTableGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,116,2,2,3))
hpicfVsfVCLinkTableGroup.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:hpicfVsfVCLinkTableGroup.setStatus(_B)
hpicfVsfVCStatusScalarGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,116,2,2,5))
hpicfVsfVCStatusScalarGroup.setObjects(*((_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:hpicfVsfVCStatusScalarGroup.setStatus(_B)
hpicfVsfVCPortTableGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,116,2,2,6))
hpicfVsfVCPortTableGroup.setObjects(*((_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:hpicfVsfVCPortTableGroup.setStatus(_B)
hpicfVsfVCConfigScalarGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,116,2,2,7))
hpicfVsfVCConfigScalarGroup1.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_K),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:hpicfVsfVCConfigScalarGroup1.setStatus(_G)
hpicfVsfVCConfigScalarGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,116,2,2,9))
hpicfVsfVCConfigScalarGroup2.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_K),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_f),(_A,_g),(_A,_h),(_A,_Ab),(_A,_Ac)))
if mibBuilder.loadTexts:hpicfVsfVCConfigScalarGroup2.setStatus(_B)
hpicfVsfVCCommanderChange=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,116,0,2))
hpicfVsfVCCommanderChange.setObjects(*((_A,_H),(_A,_L)))
if mibBuilder.loadTexts:hpicfVsfVCCommanderChange.setStatus(_B)
hpicfVsfVCMemberChange=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,116,0,3))
hpicfVsfVCMemberChange.setObjects(*((_A,_H),(_A,_L)))
if mibBuilder.loadTexts:hpicfVsfVCMemberChange.setStatus(_B)
hpicfVsfVCMemberStatusChange=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,116,0,4))
hpicfVsfVCMemberStatusChange.setObjects(*((_A,_H),(_q,_r),(_A,_L)))
if mibBuilder.loadTexts:hpicfVsfVCMemberStatusChange.setStatus(_B)
hpicfVsfVCStackTopoChange=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,116,0,7))
hpicfVsfVCStackTopoChange.setObjects(*((_A,_H),(_A,_K)))
if mibBuilder.loadTexts:hpicfVsfVCStackTopoChange.setStatus(_B)
hpicfVsfVCNotificationsGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,116,2,2,4))
hpicfVsfVCNotificationsGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:hpicfVsfVCNotificationsGroup.setStatus(_G)
hpicfVsfVCNotificationsGroup1=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,116,2,2,8))
hpicfVsfVCNotificationsGroup1.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_Ad)))
if mibBuilder.loadTexts:hpicfVsfVCNotificationsGroup1.setStatus(_B)
hpicfVsfVCMibCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,116,2,1,1))
hpicfVsfVCMibCompliance.setObjects(*((_A,_Ae),(_A,_M),(_A,_N),(_A,_l),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:hpicfVsfVCMibCompliance.setStatus(_G)
hpicfVsfVCMibCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,116,2,1,2))
hpicfVsfVCMibCompliance1.setObjects(*((_A,_m),(_A,_M),(_A,_N),(_A,_l),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:hpicfVsfVCMibCompliance1.setStatus(_G)
hpicfVsfVCMibCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,116,2,1,3))
hpicfVsfVCMibCompliance2.setObjects(*((_A,_m),(_A,_M),(_A,_N),(_A,_n),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:hpicfVsfVCMibCompliance2.setStatus(_G)
hpicfVsfVCMibCompliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,116,2,1,4))
hpicfVsfVCMibCompliance3.setObjects(*((_A,_Af),(_A,_M),(_A,_N),(_A,_n),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:hpicfVsfVCMibCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfVsfVCMIB':hpicfVsfVCMIB,'hpicfVsfVCNotifications':hpicfVsfVCNotifications,_i:hpicfVsfVCCommanderChange,_j:hpicfVsfVCMemberChange,_k:hpicfVsfVCMemberStatusChange,_Ad:hpicfVsfVCStackTopoChange,'hpicfVsfVCObjects':hpicfVsfVCObjects,'hpicfVsfVCConfig':hpicfVsfVCConfig,_S:hpicfVsfVCDomainId,_T:hpicfVsfVCOperStatus,_U:hpicfVsfVCAdminStatus,_K:hpicfVsfVCTopology,_V:hpicfVsfVCTrapEnable,_X:hpicfVsfVCOobmMADEnable,_W:hpicfVsfLldpMADEnable,_Y:hpicfVsfVCLldpMADDeviceIpType,_Z:hpicfVsfVCLldpMADDeviceIpAddr,_a:hpicfVsfVCLldpMADSnmpVersion,_b:hpicfVsfVCLldpMADSnmpCommunity,_f:hpicfVsfMADVlan,_g:hpicfVsfMADVlanConnectivity,_h:hpicfVsfVCPortSpeed,_Ab:hpicfVsfVCMemberCount,_Ac:hpicfVsfVCActiveMemberCount,'hpicfVsfVCStatus':hpicfVsfVCStatus,_AO:hpicfVsfVCLldpMADReadinessStatus,_AP:hpicfVsfVCLldpMADDeviceMAC,_AQ:hpicfVsfVCLldpMADVlanId,_AR:hpicfVsfVCLldpMADTrunkIfIndex,_AS:hpicfVsfVCLldpMADProbePortSet,_AT:hpicfVsfVCLldpMADConnectivity,_AU:hpicfVsfVCLldpMADSplitStatus,_AV:hpicfVsfVCLldpMADProbeOriginator,_AW:hpicfVsfVCLldpMADProbeRequestsSent,_AX:hpicfVsfVCLldpMADProbeResponseRcvd,_AY:hpicfVsfVCLldpMADActiveFragment,'hpicfVsfVCMemberTable':hpicfVsfVCMemberTable,'hpicfVsfVCMemberEntry':hpicfVsfVCMemberEntry,_u:hpicfVsfVCMemberId,_y:hpicfVsfVCMemberProductId,_z:hpicfVsfVCMemberMacAddr,_A0:hpicfVsfVCMemberShutdown,_A1:hpicfVsfVCMemberReboot,_A2:hpicfVsfVCMemberAdminPriority,_A3:hpicfVsfVCMemberEntryStatus,_A4:hpicfVsfVCMemberEntPhysicalIndex,_L:hpicfVsfVCMemberState,_A5:hpicfVsfVCMemberProductName,_A6:hpicfVsfVCMemberUpTime,_A7:hpicfVsfVCMemberSysOid,_H:hpicfVsfVCMemberIdForTrap,_A8:hpicfVsfVCMemberSerialNum,_A9:hpicfVsfVCMemberBootRomVersion,_AA:hpicfVsfVCMemberOsVersion,_AB:hpicfVsfVCMemberBootImage,_AC:hpicfVsfVCMemberRenumber,_AD:hpicfVsfVCMemberCpuUtil,_AE:hpicfVsfVCMemberTotalMemory,_AF:hpicfVsfVCMemberFreeMemory,'hpicfVsfVCLinkTable':hpicfVsfVCLinkTable,'hpicfVsfVCLinkEntry':hpicfVsfVCLinkEntry,_w:hpicfVsfVCLinkMemberId,_x:hpicfVsfVCLinkId,_AG:hpicfVsfVCLinkName,_AH:hpicfVsfVCLinkOperStatus,_AI:hpicfVsfVCPeerMemberId,_AJ:hpicfVsfVCPeerLinkId,_AK:hpicfVsfVCLinkPortList,_AL:hpicfVsfVCLinkEntryStatus,_AM:hpicfVsfVCLinkIdForTrap,_AN:hpicfVsfVCLinkPortStartState,'hpicfVsfVCPortTable':hpicfVsfVCPortTable,'hpicfVsfVCPortEntry':hpicfVsfVCPortEntry,_AZ:hpicfVsfVCPortOperStatus,_Aa:hpicfVsfVCPortOperStatusErrorStr,'hpicfVsfVCConformance':hpicfVsfVCConformance,'hpicfVsfVCCompliances':hpicfVsfVCCompliances,'hpicfVsfVCMibCompliance':hpicfVsfVCMibCompliance,'hpicfVsfVCMibCompliance1':hpicfVsfVCMibCompliance1,'hpicfVsfVCMibCompliance2':hpicfVsfVCMibCompliance2,'hpicfVsfVCMibCompliance3':hpicfVsfVCMibCompliance3,'hpicfVsfVCGroups':hpicfVsfVCGroups,_Ae:hpicfVsfVCConfigScalarGroup,_M:hpicfVsfVCMemberTableGroup,_N:hpicfVsfVCLinkTableGroup,_l:hpicfVsfVCNotificationsGroup,_O:hpicfVsfVCStatusScalarGroup,_P:hpicfVsfVCPortTableGroup,_m:hpicfVsfVCConfigScalarGroup1,_n:hpicfVsfVCNotificationsGroup1,_Af:hpicfVsfVCConfigScalarGroup2})