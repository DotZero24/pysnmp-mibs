_AH='alaVrrpTrackGroup'
_AG='alaVrrpGroupGroup'
_AF='alaVrrp3AssoTrackGroup'
_AE='alaVRRPConfigGroup'
_AD='alaVrrpTrackBfdStatus'
_AC='alaVrrpTrackEntityIpAddr'
_AB='alaVrrpTrackEntityIpAddrType'
_AA='alaVrrpTrackEntityIpv6Interface'
_A9='alaVrrpTrackEntityInterface'
_A8='alaVrrpTrackRowStatus'
_A7='alaVrrpTrackPriority'
_A6='alaVrrpTrackEntityIpAddress'
_A5='alaVrrpTrackEntityPort'
_A4='alaVrrpTrackEntityVlan'
_A3='alaVrrpTrackEntityType'
_A2='alaVrrpTrackAdminState'
_A1='alaVrrpTrackState'
_A0='alaVrrpGroupRowStatus'
_z='alaVrrpGroupOverride'
_y='alaVrrpGroupSetParam'
_x='alaVrrpGroupAdminState'
_w='alaVrrpGroupPreemptMode'
_v='alaVrrpGroupPriority'
_u='alaVrrpGroupInterval'
_t='alaVrrp3TrackCount'
_s='alaVrrp3GroupIdent'
_r='alaVrrp3CurrentPriority'
_q='alaVrrp3AssoTrackRowStatus'
_p='alaVrrpGroupIdent'
_o='alaVrrpTrackCount'
_n='alaVrrpCurrentPriority'
_m='alaVrrpAssoTrackRowStatus'
_l='alaVrrpAssoGroupRowStatus'
_k='alaVRRPSetParam'
_j='alaVRRPOverride'
_i='alaVRRPDefaultPriority'
_h='alaVRRPDefaultPreemptMode'
_g='alaVRRPDefaultInterval'
_f='alaVRRPAdminState'
_e='alaVrrpBfdStatus'
_d='alaVRRPStartDelay'
_c='alaVrrp3OperExEntry'
_b='alaVrrpOperEntry'
_a='preempt'
_Z='priority'
_Y='interval'
_X='allEnable'
_W='alaVrrp3AssoTrackId'
_V='alaVrrpAssoTrackId'
_U='deprecated'
_T='alaVrrpTrackId'
_S='alaVrrp3OperVrId'
_R='alaVrrp3OperIpVersion'
_Q='alaVrrpGroupId'
_P='seconds'
_O='vrrpOperVrId'
_N='VRRP-MIB'
_M='TruthValue'
_L='ALCATEL-IND1-VRRP3-MIB'
_K='not-accessible'
_J='disable'
_I='enable'
_H='ifIndex'
_G='IF-MIB'
_F='read-only'
_E='read-write'
_D='read-create'
_C='Integer32'
_B='ALCATEL-IND1-VRRP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Vrrp,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1Vrrp')
alaVrrp3OperEntry,alaVrrp3OperIpVersion,alaVrrp3OperVrId=mibBuilder.importSymbols(_L,'alaVrrp3OperEntry',_R,_S)
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_G,'InterfaceIndexOrZero',_H)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_M)
vrrpOperEntry,vrrpOperVrId=mibBuilder.importSymbols(_N,'vrrpOperEntry',_O)
alcatelIND1VRRPMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,1))
if mibBuilder.loadTexts:alcatelIND1VRRPMIB.setRevisions(('2007-04-03 00:00',))
class AlaVrTrackId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
class AlaVrGroupId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlcatelIND1VRRPMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1VRRPMIBObjects=_AlcatelIND1VRRPMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,1,1))
_AlaVRRPConfig_ObjectIdentity=ObjectIdentity
alaVRRPConfig=_AlaVRRPConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,1))
class _AlaVRRPStartDelay_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_AlaVRRPStartDelay_Type.__name__=_C
_AlaVRRPStartDelay_Object=MibScalar
alaVRRPStartDelay=_AlaVRRPStartDelay_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,1,1),_AlaVRRPStartDelay_Type())
alaVRRPStartDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVRRPStartDelay.setStatus(_A)
if mibBuilder.loadTexts:alaVRRPStartDelay.setUnits(_P)
class _AlaVrrpBfdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_AlaVrrpBfdStatus_Type.__name__=_C
_AlaVrrpBfdStatus_Object=MibScalar
alaVrrpBfdStatus=_AlaVrrpBfdStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,1,2),_AlaVrrpBfdStatus_Type())
alaVrrpBfdStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVrrpBfdStatus.setStatus(_A)
_AlaVrrpTracking_ObjectIdentity=ObjectIdentity
alaVrrpTracking=_AlaVrrpTracking_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2))
_AlaVrrpTrackTable_Object=MibTable
alaVrrpTrackTable=_AlaVrrpTrackTable_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,1))
if mibBuilder.loadTexts:alaVrrpTrackTable.setStatus(_A)
_AlaVrrpTrackEntry_Object=MibTableRow
alaVrrpTrackEntry=_AlaVrrpTrackEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,1,1))
alaVrrpTrackEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:alaVrrpTrackEntry.setStatus(_A)
_AlaVrrpTrackId_Type=AlaVrTrackId
_AlaVrrpTrackId_Object=MibTableColumn
alaVrrpTrackId=_AlaVrrpTrackId_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,1,1,1),_AlaVrrpTrackId_Type())
alaVrrpTrackId.setMaxAccess(_K)
if mibBuilder.loadTexts:alaVrrpTrackId.setStatus(_A)
class _AlaVrrpTrackState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AlaVrrpTrackState_Type.__name__=_C
_AlaVrrpTrackState_Object=MibTableColumn
alaVrrpTrackState=_AlaVrrpTrackState_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,1,1,2),_AlaVrrpTrackState_Type())
alaVrrpTrackState.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVrrpTrackState.setStatus(_A)
class _AlaVrrpTrackAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_AlaVrrpTrackAdminState_Type.__name__=_C
_AlaVrrpTrackAdminState_Object=MibTableColumn
alaVrrpTrackAdminState=_AlaVrrpTrackAdminState_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,1,1,3),_AlaVrrpTrackAdminState_Type())
alaVrrpTrackAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpTrackAdminState.setStatus(_A)
class _AlaVrrpTrackEntityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('vlan',1),('port',2),('ipaddress',3),('interface',4),('ipv6Interface',5)))
_AlaVrrpTrackEntityType_Type.__name__=_C
_AlaVrrpTrackEntityType_Object=MibTableColumn
alaVrrpTrackEntityType=_AlaVrrpTrackEntityType_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,1,1,4),_AlaVrrpTrackEntityType_Type())
alaVrrpTrackEntityType.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVrrpTrackEntityType.setStatus(_A)
class _AlaVrrpTrackEntityVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_AlaVrrpTrackEntityVlan_Type.__name__=_C
_AlaVrrpTrackEntityVlan_Object=MibTableColumn
alaVrrpTrackEntityVlan=_AlaVrrpTrackEntityVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,1,1,5),_AlaVrrpTrackEntityVlan_Type())
alaVrrpTrackEntityVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpTrackEntityVlan.setStatus(_U)
_AlaVrrpTrackEntityPort_Type=InterfaceIndexOrZero
_AlaVrrpTrackEntityPort_Object=MibTableColumn
alaVrrpTrackEntityPort=_AlaVrrpTrackEntityPort_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,1,1,6),_AlaVrrpTrackEntityPort_Type())
alaVrrpTrackEntityPort.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpTrackEntityPort.setStatus(_A)
_AlaVrrpTrackEntityIpAddress_Type=IpAddress
_AlaVrrpTrackEntityIpAddress_Object=MibTableColumn
alaVrrpTrackEntityIpAddress=_AlaVrrpTrackEntityIpAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,1,1,7),_AlaVrrpTrackEntityIpAddress_Type())
alaVrrpTrackEntityIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpTrackEntityIpAddress.setStatus(_U)
class _AlaVrrpTrackPriority_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaVrrpTrackPriority_Type.__name__=_C
_AlaVrrpTrackPriority_Object=MibTableColumn
alaVrrpTrackPriority=_AlaVrrpTrackPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,1,1,8),_AlaVrrpTrackPriority_Type())
alaVrrpTrackPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpTrackPriority.setStatus(_A)
_AlaVrrpTrackRowStatus_Type=RowStatus
_AlaVrrpTrackRowStatus_Object=MibTableColumn
alaVrrpTrackRowStatus=_AlaVrrpTrackRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,1,1,9),_AlaVrrpTrackRowStatus_Type())
alaVrrpTrackRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpTrackRowStatus.setStatus(_A)
_AlaVrrpTrackEntityInterface_Type=InterfaceIndexOrZero
_AlaVrrpTrackEntityInterface_Object=MibTableColumn
alaVrrpTrackEntityInterface=_AlaVrrpTrackEntityInterface_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,1,1,10),_AlaVrrpTrackEntityInterface_Type())
alaVrrpTrackEntityInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpTrackEntityInterface.setStatus(_A)
_AlaVrrpTrackEntityIpv6Interface_Type=InterfaceIndexOrZero
_AlaVrrpTrackEntityIpv6Interface_Object=MibTableColumn
alaVrrpTrackEntityIpv6Interface=_AlaVrrpTrackEntityIpv6Interface_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,1,1,11),_AlaVrrpTrackEntityIpv6Interface_Type())
alaVrrpTrackEntityIpv6Interface.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpTrackEntityIpv6Interface.setStatus(_A)
_AlaVrrpTrackEntityIpAddrType_Type=InetAddressType
_AlaVrrpTrackEntityIpAddrType_Object=MibTableColumn
alaVrrpTrackEntityIpAddrType=_AlaVrrpTrackEntityIpAddrType_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,1,1,12),_AlaVrrpTrackEntityIpAddrType_Type())
alaVrrpTrackEntityIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpTrackEntityIpAddrType.setStatus(_A)
_AlaVrrpTrackEntityIpAddr_Type=InetAddress
_AlaVrrpTrackEntityIpAddr_Object=MibTableColumn
alaVrrpTrackEntityIpAddr=_AlaVrrpTrackEntityIpAddr_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,1,1,13),_AlaVrrpTrackEntityIpAddr_Type())
alaVrrpTrackEntityIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpTrackEntityIpAddr.setStatus(_A)
_AlaVrrpTrackBfdStatus_Type=Integer32
_AlaVrrpTrackBfdStatus_Object=MibTableColumn
alaVrrpTrackBfdStatus=_AlaVrrpTrackBfdStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,1,1,14),_AlaVrrpTrackBfdStatus_Type())
alaVrrpTrackBfdStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpTrackBfdStatus.setStatus(_A)
_AlaVrrpAssoTrackTable_Object=MibTable
alaVrrpAssoTrackTable=_AlaVrrpAssoTrackTable_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,2))
if mibBuilder.loadTexts:alaVrrpAssoTrackTable.setStatus(_A)
_AlaVrrpAssoTrackEntry_Object=MibTableRow
alaVrrpAssoTrackEntry=_AlaVrrpAssoTrackEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,2,1))
alaVrrpAssoTrackEntry.setIndexNames((0,_G,_H),(0,_N,_O),(0,_B,_V))
if mibBuilder.loadTexts:alaVrrpAssoTrackEntry.setStatus(_A)
_AlaVrrpAssoTrackId_Type=AlaVrTrackId
_AlaVrrpAssoTrackId_Object=MibTableColumn
alaVrrpAssoTrackId=_AlaVrrpAssoTrackId_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,2,1,1),_AlaVrrpAssoTrackId_Type())
alaVrrpAssoTrackId.setMaxAccess(_K)
if mibBuilder.loadTexts:alaVrrpAssoTrackId.setStatus(_A)
_AlaVrrpAssoTrackRowStatus_Type=RowStatus
_AlaVrrpAssoTrackRowStatus_Object=MibTableColumn
alaVrrpAssoTrackRowStatus=_AlaVrrpAssoTrackRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,2,1,2),_AlaVrrpAssoTrackRowStatus_Type())
alaVrrpAssoTrackRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpAssoTrackRowStatus.setStatus(_A)
_AlaVrrp3AssoTrackTable_Object=MibTable
alaVrrp3AssoTrackTable=_AlaVrrp3AssoTrackTable_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,3))
if mibBuilder.loadTexts:alaVrrp3AssoTrackTable.setStatus(_A)
_AlaVrrp3AssoTrackEntry_Object=MibTableRow
alaVrrp3AssoTrackEntry=_AlaVrrp3AssoTrackEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,3,1))
alaVrrp3AssoTrackEntry.setIndexNames((0,_L,_R),(0,_L,_S),(0,_G,_H),(0,_B,_W))
if mibBuilder.loadTexts:alaVrrp3AssoTrackEntry.setStatus(_A)
_AlaVrrp3AssoTrackId_Type=AlaVrTrackId
_AlaVrrp3AssoTrackId_Object=MibTableColumn
alaVrrp3AssoTrackId=_AlaVrrp3AssoTrackId_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,3,1,1),_AlaVrrp3AssoTrackId_Type())
alaVrrp3AssoTrackId.setMaxAccess(_K)
if mibBuilder.loadTexts:alaVrrp3AssoTrackId.setStatus(_A)
_AlaVrrp3AssoTrackRowStatus_Type=RowStatus
_AlaVrrp3AssoTrackRowStatus_Object=MibTableColumn
alaVrrp3AssoTrackRowStatus=_AlaVrrp3AssoTrackRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,2,3,1,2),_AlaVrrp3AssoTrackRowStatus_Type())
alaVrrp3AssoTrackRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVrrp3AssoTrackRowStatus.setStatus(_A)
_AlaVrrpOperations_ObjectIdentity=ObjectIdentity
alaVrrpOperations=_AlaVrrpOperations_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,3))
_AlaVrrpOperTable_Object=MibTable
alaVrrpOperTable=_AlaVrrpOperTable_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,3,1))
if mibBuilder.loadTexts:alaVrrpOperTable.setStatus(_A)
_AlaVrrpOperEntry_Object=MibTableRow
alaVrrpOperEntry=_AlaVrrpOperEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,3,1,1))
if mibBuilder.loadTexts:alaVrrpOperEntry.setStatus(_A)
class _AlaVrrpCurrentPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaVrrpCurrentPriority_Type.__name__=_C
_AlaVrrpCurrentPriority_Object=MibTableColumn
alaVrrpCurrentPriority=_AlaVrrpCurrentPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,3,1,1,1),_AlaVrrpCurrentPriority_Type())
alaVrrpCurrentPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVrrpCurrentPriority.setStatus(_A)
_AlaVrrpTrackCount_Type=Integer32
_AlaVrrpTrackCount_Object=MibTableColumn
alaVrrpTrackCount=_AlaVrrpTrackCount_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,3,1,1,2),_AlaVrrpTrackCount_Type())
alaVrrpTrackCount.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVrrpTrackCount.setStatus(_A)
class _AlaVrrpGroupIdent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaVrrpGroupIdent_Type.__name__=_C
_AlaVrrpGroupIdent_Object=MibTableColumn
alaVrrpGroupIdent=_AlaVrrpGroupIdent_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,3,1,1,3),_AlaVrrpGroupIdent_Type())
alaVrrpGroupIdent.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVrrpGroupIdent.setStatus(_A)
_AlaVrrp3OperExTable_Object=MibTable
alaVrrp3OperExTable=_AlaVrrp3OperExTable_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,3,2))
if mibBuilder.loadTexts:alaVrrp3OperExTable.setStatus(_A)
_AlaVrrp3OperExEntry_Object=MibTableRow
alaVrrp3OperExEntry=_AlaVrrp3OperExEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,3,2,1))
if mibBuilder.loadTexts:alaVrrp3OperExEntry.setStatus(_A)
class _AlaVrrp3CurrentPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaVrrp3CurrentPriority_Type.__name__=_C
_AlaVrrp3CurrentPriority_Object=MibTableColumn
alaVrrp3CurrentPriority=_AlaVrrp3CurrentPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,3,2,1,1),_AlaVrrp3CurrentPriority_Type())
alaVrrp3CurrentPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVrrp3CurrentPriority.setStatus(_A)
_AlaVrrp3TrackCount_Type=Integer32
_AlaVrrp3TrackCount_Object=MibTableColumn
alaVrrp3TrackCount=_AlaVrrp3TrackCount_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,3,2,1,2),_AlaVrrp3TrackCount_Type())
alaVrrp3TrackCount.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVrrp3TrackCount.setStatus(_A)
class _AlaVrrp3GroupIdent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaVrrp3GroupIdent_Type.__name__=_C
_AlaVrrp3GroupIdent_Object=MibTableColumn
alaVrrp3GroupIdent=_AlaVrrp3GroupIdent_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,3,2,1,3),_AlaVrrp3GroupIdent_Type())
alaVrrp3GroupIdent.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVrrp3GroupIdent.setStatus(_A)
_AlaVRRPv2Config_ObjectIdentity=ObjectIdentity
alaVRRPv2Config=_AlaVRRPv2Config_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,4))
class _AlaVRRPDefaultInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaVRRPDefaultInterval_Type.__name__=_C
_AlaVRRPDefaultInterval_Object=MibScalar
alaVRRPDefaultInterval=_AlaVRRPDefaultInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,4,1),_AlaVRRPDefaultInterval_Type())
alaVRRPDefaultInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVRRPDefaultInterval.setStatus(_A)
if mibBuilder.loadTexts:alaVRRPDefaultInterval.setUnits(_P)
class _AlaVRRPDefaultPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_AlaVRRPDefaultPriority_Type.__name__=_C
_AlaVRRPDefaultPriority_Object=MibScalar
alaVRRPDefaultPriority=_AlaVRRPDefaultPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,4,2),_AlaVRRPDefaultPriority_Type())
alaVRRPDefaultPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVRRPDefaultPriority.setStatus(_A)
class _AlaVRRPDefaultPreemptMode_Type(TruthValue):defaultValue=1
_AlaVRRPDefaultPreemptMode_Type.__name__=_M
_AlaVRRPDefaultPreemptMode_Object=MibScalar
alaVRRPDefaultPreemptMode=_AlaVRRPDefaultPreemptMode_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,4,3),_AlaVRRPDefaultPreemptMode_Type())
alaVRRPDefaultPreemptMode.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVRRPDefaultPreemptMode.setStatus(_A)
class _AlaVRRPAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_I,2),(_J,3)))
_AlaVRRPAdminState_Type.__name__=_C
_AlaVRRPAdminState_Object=MibScalar
alaVRRPAdminState=_AlaVRRPAdminState_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,4,4),_AlaVRRPAdminState_Type())
alaVRRPAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVRRPAdminState.setStatus(_A)
class _AlaVRRPSetParam_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('all',2),(_Y,3),(_Z,4),(_a,5)))
_AlaVRRPSetParam_Type.__name__=_C
_AlaVRRPSetParam_Object=MibScalar
alaVRRPSetParam=_AlaVRRPSetParam_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,4,5),_AlaVRRPSetParam_Type())
alaVRRPSetParam.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVRRPSetParam.setStatus(_A)
_AlaVRRPOverride_Type=TruthValue
_AlaVRRPOverride_Object=MibScalar
alaVRRPOverride=_AlaVRRPOverride_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,4,6),_AlaVRRPOverride_Type())
alaVRRPOverride.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVRRPOverride.setStatus(_A)
_AlaVrrpGroup_ObjectIdentity=ObjectIdentity
alaVrrpGroup=_AlaVrrpGroup_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,5))
_AlaVrrpGroupTable_Object=MibTable
alaVrrpGroupTable=_AlaVrrpGroupTable_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,5,1))
if mibBuilder.loadTexts:alaVrrpGroupTable.setStatus(_A)
_AlaVrrpGroupEntry_Object=MibTableRow
alaVrrpGroupEntry=_AlaVrrpGroupEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,5,1,1))
alaVrrpGroupEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:alaVrrpGroupEntry.setStatus(_A)
_AlaVrrpGroupId_Type=AlaVrGroupId
_AlaVrrpGroupId_Object=MibTableColumn
alaVrrpGroupId=_AlaVrrpGroupId_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,5,1,1,1),_AlaVrrpGroupId_Type())
alaVrrpGroupId.setMaxAccess(_K)
if mibBuilder.loadTexts:alaVrrpGroupId.setStatus(_A)
class _AlaVrrpGroupInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaVrrpGroupInterval_Type.__name__=_C
_AlaVrrpGroupInterval_Object=MibTableColumn
alaVrrpGroupInterval=_AlaVrrpGroupInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,5,1,1,2),_AlaVrrpGroupInterval_Type())
alaVrrpGroupInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpGroupInterval.setStatus(_A)
if mibBuilder.loadTexts:alaVrrpGroupInterval.setUnits(_P)
class _AlaVrrpGroupPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_AlaVrrpGroupPriority_Type.__name__=_C
_AlaVrrpGroupPriority_Object=MibTableColumn
alaVrrpGroupPriority=_AlaVrrpGroupPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,5,1,1,3),_AlaVrrpGroupPriority_Type())
alaVrrpGroupPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpGroupPriority.setStatus(_A)
class _AlaVrrpGroupPreemptMode_Type(TruthValue):defaultValue=1
_AlaVrrpGroupPreemptMode_Type.__name__=_M
_AlaVrrpGroupPreemptMode_Object=MibTableColumn
alaVrrpGroupPreemptMode=_AlaVrrpGroupPreemptMode_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,5,1,1,4),_AlaVrrpGroupPreemptMode_Type())
alaVrrpGroupPreemptMode.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpGroupPreemptMode.setStatus(_A)
class _AlaVrrpGroupAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_I,2),(_J,3)))
_AlaVrrpGroupAdminState_Type.__name__=_C
_AlaVrrpGroupAdminState_Object=MibTableColumn
alaVrrpGroupAdminState=_AlaVrrpGroupAdminState_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,5,1,1,5),_AlaVrrpGroupAdminState_Type())
alaVrrpGroupAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpGroupAdminState.setStatus(_A)
class _AlaVrrpGroupSetParam_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('all',2),(_Y,3),(_Z,4),(_a,5)))
_AlaVrrpGroupSetParam_Type.__name__=_C
_AlaVrrpGroupSetParam_Object=MibTableColumn
alaVrrpGroupSetParam=_AlaVrrpGroupSetParam_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,5,1,1,6),_AlaVrrpGroupSetParam_Type())
alaVrrpGroupSetParam.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpGroupSetParam.setStatus(_A)
_AlaVrrpGroupOverride_Type=TruthValue
_AlaVrrpGroupOverride_Object=MibTableColumn
alaVrrpGroupOverride=_AlaVrrpGroupOverride_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,5,1,1,7),_AlaVrrpGroupOverride_Type())
alaVrrpGroupOverride.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpGroupOverride.setStatus(_A)
_AlaVrrpGroupRowStatus_Type=RowStatus
_AlaVrrpGroupRowStatus_Object=MibTableColumn
alaVrrpGroupRowStatus=_AlaVrrpGroupRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,5,1,1,8),_AlaVrrpGroupRowStatus_Type())
alaVrrpGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpGroupRowStatus.setStatus(_A)
_AlaVrrpAssoGroupTable_Object=MibTable
alaVrrpAssoGroupTable=_AlaVrrpAssoGroupTable_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,5,2))
if mibBuilder.loadTexts:alaVrrpAssoGroupTable.setStatus(_A)
_AlaVrrpAssoGroupEntry_Object=MibTableRow
alaVrrpAssoGroupEntry=_AlaVrrpAssoGroupEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,5,2,1))
alaVrrpAssoGroupEntry.setIndexNames((0,_B,_Q),(0,_G,_H),(0,_N,_O))
if mibBuilder.loadTexts:alaVrrpAssoGroupEntry.setStatus(_A)
_AlaVrrpAssoGroupRowStatus_Type=RowStatus
_AlaVrrpAssoGroupRowStatus_Object=MibTableColumn
alaVrrpAssoGroupRowStatus=_AlaVrrpAssoGroupRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,28,1,1,5,2,1,1),_AlaVrrpAssoGroupRowStatus_Type())
alaVrrpAssoGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVrrpAssoGroupRowStatus.setStatus(_A)
_AlcatelIND1VRRPMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1VRRPMIBConformance=_AlcatelIND1VRRPMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,1,2))
_AlcatelIND1VRRPMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1VRRPMIBCompliances=_AlcatelIND1VRRPMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,1,2,1))
_AlcatelIND1VRRPMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1VRRPMIBGroups=_AlcatelIND1VRRPMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,1,2,2))
vrrpOperEntry.registerAugmentions((_B,_b))
alaVrrpOperEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
alaVrrp3OperEntry.registerAugmentions((_B,_c))
alaVrrp3OperExEntry.setIndexNames(*alaVrrp3OperEntry.getIndexNames())
alaVRRPConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,28,1,2,2,1))
alaVRRPConfigGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:alaVRRPConfigGroup.setStatus(_A)
alaVrrp3AssoTrackGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,28,1,2,2,2))
alaVrrp3AssoTrackGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:alaVrrp3AssoTrackGroup.setStatus(_A)
alaVrrpGroupGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,28,1,2,2,3))
alaVrrpGroupGroup.setObjects(*((_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:alaVrrpGroupGroup.setStatus(_A)
alaVrrpTrackGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,28,1,2,2,4))
alaVrrpTrackGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:alaVrrpTrackGroup.setStatus(_A)
alaVRRPCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,28,1,2,1,1))
alaVRRPCompliance.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:alaVRRPCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AlaVrTrackId':AlaVrTrackId,'AlaVrGroupId':AlaVrGroupId,'alcatelIND1VRRPMIB':alcatelIND1VRRPMIB,'alcatelIND1VRRPMIBObjects':alcatelIND1VRRPMIBObjects,'alaVRRPConfig':alaVRRPConfig,_d:alaVRRPStartDelay,_e:alaVrrpBfdStatus,'alaVrrpTracking':alaVrrpTracking,'alaVrrpTrackTable':alaVrrpTrackTable,'alaVrrpTrackEntry':alaVrrpTrackEntry,_T:alaVrrpTrackId,_A1:alaVrrpTrackState,_A2:alaVrrpTrackAdminState,_A3:alaVrrpTrackEntityType,_A4:alaVrrpTrackEntityVlan,_A5:alaVrrpTrackEntityPort,_A6:alaVrrpTrackEntityIpAddress,_A7:alaVrrpTrackPriority,_A8:alaVrrpTrackRowStatus,_A9:alaVrrpTrackEntityInterface,_AA:alaVrrpTrackEntityIpv6Interface,_AB:alaVrrpTrackEntityIpAddrType,_AC:alaVrrpTrackEntityIpAddr,_AD:alaVrrpTrackBfdStatus,'alaVrrpAssoTrackTable':alaVrrpAssoTrackTable,'alaVrrpAssoTrackEntry':alaVrrpAssoTrackEntry,_V:alaVrrpAssoTrackId,_m:alaVrrpAssoTrackRowStatus,'alaVrrp3AssoTrackTable':alaVrrp3AssoTrackTable,'alaVrrp3AssoTrackEntry':alaVrrp3AssoTrackEntry,_W:alaVrrp3AssoTrackId,_q:alaVrrp3AssoTrackRowStatus,'alaVrrpOperations':alaVrrpOperations,'alaVrrpOperTable':alaVrrpOperTable,_b:alaVrrpOperEntry,_n:alaVrrpCurrentPriority,_o:alaVrrpTrackCount,_p:alaVrrpGroupIdent,'alaVrrp3OperExTable':alaVrrp3OperExTable,_c:alaVrrp3OperExEntry,_r:alaVrrp3CurrentPriority,_t:alaVrrp3TrackCount,_s:alaVrrp3GroupIdent,'alaVRRPv2Config':alaVRRPv2Config,_g:alaVRRPDefaultInterval,_i:alaVRRPDefaultPriority,_h:alaVRRPDefaultPreemptMode,_f:alaVRRPAdminState,_k:alaVRRPSetParam,_j:alaVRRPOverride,'alaVrrpGroup':alaVrrpGroup,'alaVrrpGroupTable':alaVrrpGroupTable,'alaVrrpGroupEntry':alaVrrpGroupEntry,_Q:alaVrrpGroupId,_u:alaVrrpGroupInterval,_v:alaVrrpGroupPriority,_w:alaVrrpGroupPreemptMode,_x:alaVrrpGroupAdminState,_y:alaVrrpGroupSetParam,_z:alaVrrpGroupOverride,_A0:alaVrrpGroupRowStatus,'alaVrrpAssoGroupTable':alaVrrpAssoGroupTable,'alaVrrpAssoGroupEntry':alaVrrpAssoGroupEntry,_l:alaVrrpAssoGroupRowStatus,'alcatelIND1VRRPMIBConformance':alcatelIND1VRRPMIBConformance,'alcatelIND1VRRPMIBCompliances':alcatelIND1VRRPMIBCompliances,'alaVRRPCompliance':alaVRRPCompliance,'alcatelIND1VRRPMIBGroups':alcatelIND1VRRPMIBGroups,_AE:alaVRRPConfigGroup,_AF:alaVrrp3AssoTrackGroup,_AG:alaVrrpGroupGroup,_AH:alaVrrpTrackGroup})