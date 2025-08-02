_u='alaHAVlanNotificationGroup'
_t='alaHAVlanClusterPortGroup'
_s='alaHAVlanClusterGroup'
_r='alaHAVlanDynamicMAC'
_q='alaHAVlanMCPeerMismatch'
_p='alaHAVlanClusterPeerMismatch'
_o='alaHAVlanClusterPortValid'
_n='alaHAVlanClusterPortType'
_m='alaHAVlanClusterPortRowStatus'
_l='alaHAVlanClusterLoopback'
_k='alaHAVlanClusterVflStatus'
_j='alaHAVlanClusterMcmStatusFlag'
_i='alaHAVlanClusterMcmStatus'
_h='alaHAVlanClusterRowStatus'
_g='alaHAVlanClusterMulticastInetAddress'
_f='alaHAVlanClusterMulticastInetAddressType'
_e='alaHAVlanClusterMulticastStatus'
_d='alaHAVlanClusterInetAddressType'
_c='alaHAVlanClusterMacAddressType'
_b='alaHAVlanClusterVlan'
_a='alaHAVlanClusterMode'
_Z='alaHAVlanClusterOperStatusFlag'
_Y='alaHAVlanClusterOperStatus'
_X='alaHAVlanClusterAdminStatus'
_W='alaHAVlanClusterName'
_V='00000000'
_U='dynamic'
_T='static'
_S='MacAddress'
_R='SnmpAdminString'
_Q='alaHAVlanMultiChassisId'
_P='alaHAVlanClusterInetAddress'
_O='alaHAVlanClusterMacAddress'
_N='deprecated'
_M='invalid'
_L='accessible-for-notify'
_K='InetAddressType'
_J='InetAddress'
_I='alaHAVlanClusterPortIfIndex'
_H='disable'
_G='enable'
_F='read-only'
_E='alaHAVlanClusterId'
_D='read-create'
_C='Integer32'
_B='current'
_A='ALCATEL-ENT1-HA-VLAN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1HAVlan,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1HAVlan')
MultiChassisId,=mibBuilder.importSymbols('ALCATEL-ENT1-MULTI-CHASSIS-MIB','MultiChassisId')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_J,_K)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_R)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_S,'PhysAddress','RowStatus','TextualConvention')
alcatelIND1HAVlanMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,64,1))
if mibBuilder.loadTexts:alcatelIND1HAVlanMIB.setRevisions(('2010-05-13 00:00','2007-04-03 00:00'))
_AlcatelIND1HAVlanMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1HAVlanMIBNotifications=_AlcatelIND1HAVlanMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,64,1,0))
if mibBuilder.loadTexts:alcatelIND1HAVlanMIBNotifications.setStatus(_B)
_AlcatelIND1HAVlanMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1HAVlanMIBObjects=_AlcatelIND1HAVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,64,1,1))
if mibBuilder.loadTexts:alcatelIND1HAVlanMIBObjects.setStatus(_B)
_AlaHAVlanCluster_ObjectIdentity=ObjectIdentity
alaHAVlanCluster=_AlaHAVlanCluster_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1))
_AlaHAVlanClusterTable_Object=MibTable
alaHAVlanClusterTable=_AlaHAVlanClusterTable_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1))
if mibBuilder.loadTexts:alaHAVlanClusterTable.setStatus(_B)
_AlaHAVlanClusterEntry_Object=MibTableRow
alaHAVlanClusterEntry=_AlaHAVlanClusterEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1))
alaHAVlanClusterEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:alaHAVlanClusterEntry.setStatus(_B)
class _AlaHAVlanClusterId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_AlaHAVlanClusterId_Type.__name__=_C
_AlaHAVlanClusterId_Object=MibTableColumn
alaHAVlanClusterId=_AlaHAVlanClusterId_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,1),_AlaHAVlanClusterId_Type())
alaHAVlanClusterId.setMaxAccess(_L)
if mibBuilder.loadTexts:alaHAVlanClusterId.setStatus(_B)
class _AlaHAVlanClusterName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AlaHAVlanClusterName_Type.__name__=_R
_AlaHAVlanClusterName_Object=MibTableColumn
alaHAVlanClusterName=_AlaHAVlanClusterName_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,2),_AlaHAVlanClusterName_Type())
alaHAVlanClusterName.setMaxAccess(_D)
if mibBuilder.loadTexts:alaHAVlanClusterName.setStatus(_B)
class _AlaHAVlanClusterAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaHAVlanClusterAdminStatus_Type.__name__=_C
_AlaHAVlanClusterAdminStatus_Object=MibTableColumn
alaHAVlanClusterAdminStatus=_AlaHAVlanClusterAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,3),_AlaHAVlanClusterAdminStatus_Type())
alaHAVlanClusterAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaHAVlanClusterAdminStatus.setStatus(_B)
class _AlaHAVlanClusterOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaHAVlanClusterOperStatus_Type.__name__=_C
_AlaHAVlanClusterOperStatus_Object=MibTableColumn
alaHAVlanClusterOperStatus=_AlaHAVlanClusterOperStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,4),_AlaHAVlanClusterOperStatus_Type())
alaHAVlanClusterOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaHAVlanClusterOperStatus.setStatus(_B)
class _AlaHAVlanClusterOperStatusFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,0),('novlan',1),('vlandown',2),('vpanotforwarding',3),('ipinterfacedown',4),('noigmpmembers',5),('nomacaddress',6),('nomulticastip',7)))
_AlaHAVlanClusterOperStatusFlag_Type.__name__=_C
_AlaHAVlanClusterOperStatusFlag_Object=MibTableColumn
alaHAVlanClusterOperStatusFlag=_AlaHAVlanClusterOperStatusFlag_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,5),_AlaHAVlanClusterOperStatusFlag_Type())
alaHAVlanClusterOperStatusFlag.setMaxAccess(_F)
if mibBuilder.loadTexts:alaHAVlanClusterOperStatusFlag.setStatus(_B)
class _AlaHAVlanClusterMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('l2mode',1),('l3mode',2)))
_AlaHAVlanClusterMode_Type.__name__=_C
_AlaHAVlanClusterMode_Object=MibTableColumn
alaHAVlanClusterMode=_AlaHAVlanClusterMode_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,6),_AlaHAVlanClusterMode_Type())
alaHAVlanClusterMode.setMaxAccess(_D)
if mibBuilder.loadTexts:alaHAVlanClusterMode.setStatus(_B)
class _AlaHAVlanClusterVlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_AlaHAVlanClusterVlan_Type.__name__=_C
_AlaHAVlanClusterVlan_Object=MibTableColumn
alaHAVlanClusterVlan=_AlaHAVlanClusterVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,7),_AlaHAVlanClusterVlan_Type())
alaHAVlanClusterVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaHAVlanClusterVlan.setStatus(_B)
class _AlaHAVlanClusterMacAddressType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_T,2),(_U,3)))
_AlaHAVlanClusterMacAddressType_Type.__name__=_C
_AlaHAVlanClusterMacAddressType_Object=MibTableColumn
alaHAVlanClusterMacAddressType=_AlaHAVlanClusterMacAddressType_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,8),_AlaHAVlanClusterMacAddressType_Type())
alaHAVlanClusterMacAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaHAVlanClusterMacAddressType.setStatus(_B)
class _AlaHAVlanClusterMacAddress_Type(MacAddress):defaultHexValue='000000000000'
_AlaHAVlanClusterMacAddress_Type.__name__=_S
_AlaHAVlanClusterMacAddress_Object=MibTableColumn
alaHAVlanClusterMacAddress=_AlaHAVlanClusterMacAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,9),_AlaHAVlanClusterMacAddress_Type())
alaHAVlanClusterMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaHAVlanClusterMacAddress.setStatus(_B)
class _AlaHAVlanClusterInetAddressType_Type(InetAddressType):defaultValue=1;subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('ipv4',1))
_AlaHAVlanClusterInetAddressType_Type.__name__=_K
_AlaHAVlanClusterInetAddressType_Object=MibTableColumn
alaHAVlanClusterInetAddressType=_AlaHAVlanClusterInetAddressType_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,10),_AlaHAVlanClusterInetAddressType_Type())
alaHAVlanClusterInetAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaHAVlanClusterInetAddressType.setStatus(_B)
class _AlaHAVlanClusterInetAddress_Type(InetAddress):defaultHexValue=_V;subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_AlaHAVlanClusterInetAddress_Type.__name__=_J
_AlaHAVlanClusterInetAddress_Object=MibTableColumn
alaHAVlanClusterInetAddress=_AlaHAVlanClusterInetAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,11),_AlaHAVlanClusterInetAddress_Type())
alaHAVlanClusterInetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaHAVlanClusterInetAddress.setStatus(_B)
class _AlaHAVlanClusterMulticastStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaHAVlanClusterMulticastStatus_Type.__name__=_C
_AlaHAVlanClusterMulticastStatus_Object=MibTableColumn
alaHAVlanClusterMulticastStatus=_AlaHAVlanClusterMulticastStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,12),_AlaHAVlanClusterMulticastStatus_Type())
alaHAVlanClusterMulticastStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaHAVlanClusterMulticastStatus.setStatus(_B)
class _AlaHAVlanClusterMulticastInetAddressType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AlaHAVlanClusterMulticastInetAddressType_Type.__name__=_K
_AlaHAVlanClusterMulticastInetAddressType_Object=MibTableColumn
alaHAVlanClusterMulticastInetAddressType=_AlaHAVlanClusterMulticastInetAddressType_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,13),_AlaHAVlanClusterMulticastInetAddressType_Type())
alaHAVlanClusterMulticastInetAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaHAVlanClusterMulticastInetAddressType.setStatus(_B)
class _AlaHAVlanClusterMulticastInetAddress_Type(InetAddress):defaultHexValue=_V;subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_AlaHAVlanClusterMulticastInetAddress_Type.__name__=_J
_AlaHAVlanClusterMulticastInetAddress_Object=MibTableColumn
alaHAVlanClusterMulticastInetAddress=_AlaHAVlanClusterMulticastInetAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,14),_AlaHAVlanClusterMulticastInetAddress_Type())
alaHAVlanClusterMulticastInetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaHAVlanClusterMulticastInetAddress.setStatus(_B)
_AlaHAVlanClusterRowStatus_Type=RowStatus
_AlaHAVlanClusterRowStatus_Object=MibTableColumn
alaHAVlanClusterRowStatus=_AlaHAVlanClusterRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,15),_AlaHAVlanClusterRowStatus_Type())
alaHAVlanClusterRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaHAVlanClusterRowStatus.setStatus(_B)
class _AlaHAVlanClusterMcmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inSync',1),('outofSync',2)))
_AlaHAVlanClusterMcmStatus_Type.__name__=_C
_AlaHAVlanClusterMcmStatus_Object=MibTableColumn
alaHAVlanClusterMcmStatus=_AlaHAVlanClusterMcmStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,16),_AlaHAVlanClusterMcmStatus_Type())
alaHAVlanClusterMcmStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaHAVlanClusterMcmStatus.setStatus(_N)
class _AlaHAVlanClusterMcmStatusFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('mcdown',1),('operationaldown',2),('allportmodenotsupported',3),('modemismatch',4),('vlanmismatch',5),('macmismatch',6),('ipmismatch',7),('arptypemismatch',8),('igmpstatusmismatch',9),('mcastipmismatch',10),('syncinprogress',11),('invalidmac',12),('nonvipvlannotsupportedinl3mode',13),('noflag',14)))
_AlaHAVlanClusterMcmStatusFlag_Type.__name__=_C
_AlaHAVlanClusterMcmStatusFlag_Object=MibTableColumn
alaHAVlanClusterMcmStatusFlag=_AlaHAVlanClusterMcmStatusFlag_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,17),_AlaHAVlanClusterMcmStatusFlag_Type())
alaHAVlanClusterMcmStatusFlag.setMaxAccess(_F)
if mibBuilder.loadTexts:alaHAVlanClusterMcmStatusFlag.setStatus(_N)
class _AlaHAVlanClusterVflStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaHAVlanClusterVflStatus_Type.__name__=_C
_AlaHAVlanClusterVflStatus_Object=MibTableColumn
alaHAVlanClusterVflStatus=_AlaHAVlanClusterVflStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,18),_AlaHAVlanClusterVflStatus_Type())
alaHAVlanClusterVflStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaHAVlanClusterVflStatus.setStatus(_N)
class _AlaHAVlanClusterLoopback_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaHAVlanClusterLoopback_Type.__name__=_C
_AlaHAVlanClusterLoopback_Object=MibTableColumn
alaHAVlanClusterLoopback=_AlaHAVlanClusterLoopback_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,1,1,1,19),_AlaHAVlanClusterLoopback_Type())
alaHAVlanClusterLoopback.setMaxAccess(_D)
if mibBuilder.loadTexts:alaHAVlanClusterLoopback.setStatus(_B)
_AlaHAVlanClusterPort_ObjectIdentity=ObjectIdentity
alaHAVlanClusterPort=_AlaHAVlanClusterPort_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,2))
_AlaHAVlanClusterPortTable_Object=MibTable
alaHAVlanClusterPortTable=_AlaHAVlanClusterPortTable_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,2,1))
if mibBuilder.loadTexts:alaHAVlanClusterPortTable.setStatus(_B)
_AlaHAVlanClusterPortEntry_Object=MibTableRow
alaHAVlanClusterPortEntry=_AlaHAVlanClusterPortEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,2,1,1))
alaHAVlanClusterPortEntry.setIndexNames((0,_A,_E),(0,_A,_I))
if mibBuilder.loadTexts:alaHAVlanClusterPortEntry.setStatus(_B)
_AlaHAVlanClusterPortIfIndex_Type=InterfaceIndex
_AlaHAVlanClusterPortIfIndex_Object=MibTableColumn
alaHAVlanClusterPortIfIndex=_AlaHAVlanClusterPortIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,2,1,1,1),_AlaHAVlanClusterPortIfIndex_Type())
alaHAVlanClusterPortIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:alaHAVlanClusterPortIfIndex.setStatus(_B)
_AlaHAVlanClusterPortRowStatus_Type=RowStatus
_AlaHAVlanClusterPortRowStatus_Object=MibTableColumn
alaHAVlanClusterPortRowStatus=_AlaHAVlanClusterPortRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,2,1,1,2),_AlaHAVlanClusterPortRowStatus_Type())
alaHAVlanClusterPortRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaHAVlanClusterPortRowStatus.setStatus(_B)
class _AlaHAVlanClusterPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_AlaHAVlanClusterPortType_Type.__name__=_C
_AlaHAVlanClusterPortType_Object=MibTableColumn
alaHAVlanClusterPortType=_AlaHAVlanClusterPortType_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,2,1,1,3),_AlaHAVlanClusterPortType_Type())
alaHAVlanClusterPortType.setMaxAccess(_F)
if mibBuilder.loadTexts:alaHAVlanClusterPortType.setStatus(_B)
class _AlaHAVlanClusterPortValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_M,2)))
_AlaHAVlanClusterPortValid_Type.__name__=_C
_AlaHAVlanClusterPortValid_Object=MibTableColumn
alaHAVlanClusterPortValid=_AlaHAVlanClusterPortValid_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,2,1,1,4),_AlaHAVlanClusterPortValid_Type())
alaHAVlanClusterPortValid.setMaxAccess(_F)
if mibBuilder.loadTexts:alaHAVlanClusterPortValid.setStatus(_B)
_AlaHAVlanNotificationObj_ObjectIdentity=ObjectIdentity
alaHAVlanNotificationObj=_AlaHAVlanNotificationObj_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,3))
_AlaHAVlanMultiChassisId_Type=MultiChassisId
_AlaHAVlanMultiChassisId_Object=MibScalar
alaHAVlanMultiChassisId=_AlaHAVlanMultiChassisId_Object((1,3,6,1,4,1,6486,801,1,2,1,64,1,1,3,1),_AlaHAVlanMultiChassisId_Type())
alaHAVlanMultiChassisId.setMaxAccess(_L)
if mibBuilder.loadTexts:alaHAVlanMultiChassisId.setStatus(_B)
_AlcatelIND1HAVlanMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1HAVlanMIBConformance=_AlcatelIND1HAVlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,64,1,2))
if mibBuilder.loadTexts:alcatelIND1HAVlanMIBConformance.setStatus(_B)
_AlcatelIND1HAVlanMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1HAVlanMIBGroups=_AlcatelIND1HAVlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,64,1,2,1))
if mibBuilder.loadTexts:alcatelIND1HAVlanMIBGroups.setStatus(_B)
_AlcatelIND1HAVlanMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1HAVlanMIBCompliances=_AlcatelIND1HAVlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,64,1,2,2))
if mibBuilder.loadTexts:alcatelIND1HAVlanMIBCompliances.setStatus(_B)
alaHAVlanClusterGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,64,1,2,1,1))
alaHAVlanClusterGroup.setObjects(*((_A,_E),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_O),(_A,_d),(_A,_P),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:alaHAVlanClusterGroup.setStatus(_B)
alaHAVlanClusterPortGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,64,1,2,1,2))
alaHAVlanClusterPortGroup.setObjects(*((_A,_I),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:alaHAVlanClusterPortGroup.setStatus(_B)
alaHAVlanNotificationObjectGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,64,1,2,1,3))
alaHAVlanNotificationObjectGroup.setObjects((_A,_Q))
if mibBuilder.loadTexts:alaHAVlanNotificationObjectGroup.setStatus(_B)
alaHAVlanClusterPeerMismatch=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,64,1,0,1))
alaHAVlanClusterPeerMismatch.setObjects((_A,_E))
if mibBuilder.loadTexts:alaHAVlanClusterPeerMismatch.setStatus(_B)
alaHAVlanMCPeerMismatch=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,64,1,0,2))
alaHAVlanMCPeerMismatch.setObjects(*((_A,_E),(_A,_Q),(_A,_I)))
if mibBuilder.loadTexts:alaHAVlanMCPeerMismatch.setStatus(_B)
alaHAVlanDynamicMAC=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,64,1,0,3))
alaHAVlanDynamicMAC.setObjects(*((_A,_E),(_A,_P),(_A,_O),(_A,_I)))
if mibBuilder.loadTexts:alaHAVlanDynamicMAC.setStatus(_B)
alaHAVlanNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,64,1,2,1,4))
alaHAVlanNotificationGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:alaHAVlanNotificationGroup.setStatus(_B)
alcatelIND1HAVlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,64,1,2,2,1))
alcatelIND1HAVlanMIBCompliance.setObjects(*((_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:alcatelIND1HAVlanMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alcatelIND1HAVlanMIB':alcatelIND1HAVlanMIB,'alcatelIND1HAVlanMIBNotifications':alcatelIND1HAVlanMIBNotifications,_p:alaHAVlanClusterPeerMismatch,_q:alaHAVlanMCPeerMismatch,_r:alaHAVlanDynamicMAC,'alcatelIND1HAVlanMIBObjects':alcatelIND1HAVlanMIBObjects,'alaHAVlanCluster':alaHAVlanCluster,'alaHAVlanClusterTable':alaHAVlanClusterTable,'alaHAVlanClusterEntry':alaHAVlanClusterEntry,_E:alaHAVlanClusterId,_W:alaHAVlanClusterName,_X:alaHAVlanClusterAdminStatus,_Y:alaHAVlanClusterOperStatus,_Z:alaHAVlanClusterOperStatusFlag,_a:alaHAVlanClusterMode,_b:alaHAVlanClusterVlan,_c:alaHAVlanClusterMacAddressType,_O:alaHAVlanClusterMacAddress,_d:alaHAVlanClusterInetAddressType,_P:alaHAVlanClusterInetAddress,_e:alaHAVlanClusterMulticastStatus,_f:alaHAVlanClusterMulticastInetAddressType,_g:alaHAVlanClusterMulticastInetAddress,_h:alaHAVlanClusterRowStatus,_i:alaHAVlanClusterMcmStatus,_j:alaHAVlanClusterMcmStatusFlag,_k:alaHAVlanClusterVflStatus,_l:alaHAVlanClusterLoopback,'alaHAVlanClusterPort':alaHAVlanClusterPort,'alaHAVlanClusterPortTable':alaHAVlanClusterPortTable,'alaHAVlanClusterPortEntry':alaHAVlanClusterPortEntry,_I:alaHAVlanClusterPortIfIndex,_m:alaHAVlanClusterPortRowStatus,_n:alaHAVlanClusterPortType,_o:alaHAVlanClusterPortValid,'alaHAVlanNotificationObj':alaHAVlanNotificationObj,_Q:alaHAVlanMultiChassisId,'alcatelIND1HAVlanMIBConformance':alcatelIND1HAVlanMIBConformance,'alcatelIND1HAVlanMIBGroups':alcatelIND1HAVlanMIBGroups,_s:alaHAVlanClusterGroup,_t:alaHAVlanClusterPortGroup,'alaHAVlanNotificationObjectGroup':alaHAVlanNotificationObjectGroup,_u:alaHAVlanNotificationGroup,'alcatelIND1HAVlanMIBCompliances':alcatelIND1HAVlanMIBCompliances,'alcatelIND1HAVlanMIBCompliance':alcatelIND1HAVlanMIBCompliance})