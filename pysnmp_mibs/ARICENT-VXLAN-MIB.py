_i='fsVxlanEcmpNveRemoteVtepAddress'
_h='fsVxlanEcmpNveRemoteVtepAddressType'
_g='fsVxlanEcmpNveDestVmMac'
_f='fsVxlanEcmpNveVniNumber'
_e='fsVxlanEcmpNveIfIndex'
_d='fsEvpnVxlanMHEviVniESI'
_c='fsEvpnVxlanPeerIpAddress'
_b='fsEvpnVxlanPeerIpAddressType'
_a='fsEvpnVxlanVrfRTType'
_Z='fsEvpnVxlanVrfRTIndex'
_Y='fsEvpnVxlanBgpRTType'
_X='fsEvpnVxlanBgpRTIndex'
_W='fsVxlanInReplicaVniNumber'
_V='fsVxlanInReplicaNveIfIndex'
_U='fsVxlanVniVlanMapVlanId'
_T='fsVxlanMCastVniNumber'
_S='fsVxlanMCastNveIfIndex'
_R='fsVxlanNveDestVmMac'
_Q='fsVxlanNveVniNumber'
_P='fsVxlanNveIfIndex'
_O='fsVxlanVtepNveIfIndex'
_N='fsEvpnVxlanVrfName'
_M='fsEvpnVxlanEviVniMapVniNumber'
_L='fsEvpnVxlanEviVniMapEviIndex'
_K='disabled'
_J='enabled'
_I='TruthValue'
_H='Integer32'
_G='Unsigned32'
_F='read-create'
_E='read-only'
_D='not-accessible'
_C='ARICENT-VXLAN-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','StorageType','TextualConvention',_I)
fsvxlan=ModuleIdentity((1,3,6,1,4,1,29601,2,89))
if mibBuilder.loadTexts:fsvxlan.setRevisions(('2014-05-21 00:00',))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class VniId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4096,16777215))
class EviId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
class EvpnVxlanBgpRD(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class EvpnVxlanESI(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
class EvpnVxlanBgpRTType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('import',1),('export',2),('both',3)))
class EvpnVxlanVrfName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FsVxlanObjects_ObjectIdentity=ObjectIdentity
fsVxlanObjects=_FsVxlanObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,89,1))
_FsVxlanSystem_ObjectIdentity=ObjectIdentity
fsVxlanSystem=_FsVxlanSystem_ObjectIdentity((1,3,6,1,4,1,29601,2,89,1,1))
class _FsVxlanEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsVxlanEnable_Type.__name__=_H
_FsVxlanEnable_Object=MibScalar
fsVxlanEnable=_FsVxlanEnable_Object((1,3,6,1,4,1,29601,2,89,1,1,1),_FsVxlanEnable_Type())
fsVxlanEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanEnable.setStatus(_A)
class _FsVxlanUdpPort_Type(Unsigned32):defaultValue=4789;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,65535))
_FsVxlanUdpPort_Type.__name__=_G
_FsVxlanUdpPort_Object=MibScalar
fsVxlanUdpPort=_FsVxlanUdpPort_Object((1,3,6,1,4,1,29601,2,89,1,1,2),_FsVxlanUdpPort_Type())
fsVxlanUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanUdpPort.setStatus(_A)
class _FsVxlanTraceOption_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsVxlanTraceOption_Type.__name__=_G
_FsVxlanTraceOption_Object=MibScalar
fsVxlanTraceOption=_FsVxlanTraceOption_Object((1,3,6,1,4,1,29601,2,89,1,1,3),_FsVxlanTraceOption_Type())
fsVxlanTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanTraceOption.setStatus(_A)
class _FsVxlanNotificationCntl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsVxlanNotificationCntl_Type.__name__=_H
_FsVxlanNotificationCntl_Object=MibScalar
fsVxlanNotificationCntl=_FsVxlanNotificationCntl_Object((1,3,6,1,4,1,29601,2,89,1,1,4),_FsVxlanNotificationCntl_Type())
fsVxlanNotificationCntl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanNotificationCntl.setStatus(_A)
class _FsEvpnVxlanEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsEvpnVxlanEnable_Type.__name__=_H
_FsEvpnVxlanEnable_Object=MibScalar
fsEvpnVxlanEnable=_FsEvpnVxlanEnable_Object((1,3,6,1,4,1,29601,2,89,1,1,5),_FsEvpnVxlanEnable_Type())
fsEvpnVxlanEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEvpnVxlanEnable.setStatus(_A)
_FsVxlanConfigObjects_ObjectIdentity=ObjectIdentity
fsVxlanConfigObjects=_FsVxlanConfigObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,89,1,2))
_FsVxlanVtepTable_Object=MibTable
fsVxlanVtepTable=_FsVxlanVtepTable_Object((1,3,6,1,4,1,29601,2,89,1,2,1))
if mibBuilder.loadTexts:fsVxlanVtepTable.setStatus(_A)
_FsVxlanVtepEntry_Object=MibTableRow
fsVxlanVtepEntry=_FsVxlanVtepEntry_Object((1,3,6,1,4,1,29601,2,89,1,2,1,1))
fsVxlanVtepEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:fsVxlanVtepEntry.setStatus(_A)
_FsVxlanVtepNveIfIndex_Type=InterfaceIndexOrZero
_FsVxlanVtepNveIfIndex_Object=MibTableColumn
fsVxlanVtepNveIfIndex=_FsVxlanVtepNveIfIndex_Object((1,3,6,1,4,1,29601,2,89,1,2,1,1,1),_FsVxlanVtepNveIfIndex_Type())
fsVxlanVtepNveIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVxlanVtepNveIfIndex.setStatus(_A)
_FsVxlanVtepAddressType_Type=InetAddressType
_FsVxlanVtepAddressType_Object=MibTableColumn
fsVxlanVtepAddressType=_FsVxlanVtepAddressType_Object((1,3,6,1,4,1,29601,2,89,1,2,1,1,2),_FsVxlanVtepAddressType_Type())
fsVxlanVtepAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanVtepAddressType.setStatus(_A)
_FsVxlanVtepAddress_Type=InetAddress
_FsVxlanVtepAddress_Object=MibTableColumn
fsVxlanVtepAddress=_FsVxlanVtepAddress_Object((1,3,6,1,4,1,29601,2,89,1,2,1,1,3),_FsVxlanVtepAddress_Type())
fsVxlanVtepAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanVtepAddress.setStatus(_A)
_FsVxlanVtepRowStatus_Type=RowStatus
_FsVxlanVtepRowStatus_Object=MibTableColumn
fsVxlanVtepRowStatus=_FsVxlanVtepRowStatus_Object((1,3,6,1,4,1,29601,2,89,1,2,1,1,4),_FsVxlanVtepRowStatus_Type())
fsVxlanVtepRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsVxlanVtepRowStatus.setStatus(_A)
_FsVxlanNveTable_Object=MibTable
fsVxlanNveTable=_FsVxlanNveTable_Object((1,3,6,1,4,1,29601,2,89,1,2,2))
if mibBuilder.loadTexts:fsVxlanNveTable.setStatus(_A)
_FsVxlanNveEntry_Object=MibTableRow
fsVxlanNveEntry=_FsVxlanNveEntry_Object((1,3,6,1,4,1,29601,2,89,1,2,2,1))
fsVxlanNveEntry.setIndexNames((0,_C,_P),(0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:fsVxlanNveEntry.setStatus(_A)
_FsVxlanNveIfIndex_Type=InterfaceIndexOrZero
_FsVxlanNveIfIndex_Object=MibTableColumn
fsVxlanNveIfIndex=_FsVxlanNveIfIndex_Object((1,3,6,1,4,1,29601,2,89,1,2,2,1,1),_FsVxlanNveIfIndex_Type())
fsVxlanNveIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVxlanNveIfIndex.setStatus(_A)
_FsVxlanNveVniNumber_Type=VniId
_FsVxlanNveVniNumber_Object=MibTableColumn
fsVxlanNveVniNumber=_FsVxlanNveVniNumber_Object((1,3,6,1,4,1,29601,2,89,1,2,2,1,2),_FsVxlanNveVniNumber_Type())
fsVxlanNveVniNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVxlanNveVniNumber.setStatus(_A)
_FsVxlanNveDestVmMac_Type=MacAddress
_FsVxlanNveDestVmMac_Object=MibTableColumn
fsVxlanNveDestVmMac=_FsVxlanNveDestVmMac_Object((1,3,6,1,4,1,29601,2,89,1,2,2,1,3),_FsVxlanNveDestVmMac_Type())
fsVxlanNveDestVmMac.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVxlanNveDestVmMac.setStatus(_A)
_FsVxlanNveVtepAddressType_Type=InetAddressType
_FsVxlanNveVtepAddressType_Object=MibTableColumn
fsVxlanNveVtepAddressType=_FsVxlanNveVtepAddressType_Object((1,3,6,1,4,1,29601,2,89,1,2,2,1,4),_FsVxlanNveVtepAddressType_Type())
fsVxlanNveVtepAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVxlanNveVtepAddressType.setStatus(_A)
_FsVxlanNveVtepAddress_Type=InetAddress
_FsVxlanNveVtepAddress_Object=MibTableColumn
fsVxlanNveVtepAddress=_FsVxlanNveVtepAddress_Object((1,3,6,1,4,1,29601,2,89,1,2,2,1,5),_FsVxlanNveVtepAddress_Type())
fsVxlanNveVtepAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVxlanNveVtepAddress.setStatus(_A)
_FsVxlanNveRemoteVtepAddressType_Type=InetAddressType
_FsVxlanNveRemoteVtepAddressType_Object=MibTableColumn
fsVxlanNveRemoteVtepAddressType=_FsVxlanNveRemoteVtepAddressType_Object((1,3,6,1,4,1,29601,2,89,1,2,2,1,6),_FsVxlanNveRemoteVtepAddressType_Type())
fsVxlanNveRemoteVtepAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanNveRemoteVtepAddressType.setStatus(_A)
_FsVxlanNveRemoteVtepAddress_Type=InetAddress
_FsVxlanNveRemoteVtepAddress_Object=MibTableColumn
fsVxlanNveRemoteVtepAddress=_FsVxlanNveRemoteVtepAddress_Object((1,3,6,1,4,1,29601,2,89,1,2,2,1,7),_FsVxlanNveRemoteVtepAddress_Type())
fsVxlanNveRemoteVtepAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanNveRemoteVtepAddress.setStatus(_A)
_FsVxlanNveStorageType_Type=StorageType
_FsVxlanNveStorageType_Object=MibTableColumn
fsVxlanNveStorageType=_FsVxlanNveStorageType_Object((1,3,6,1,4,1,29601,2,89,1,2,2,1,8),_FsVxlanNveStorageType_Type())
fsVxlanNveStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVxlanNveStorageType.setStatus(_A)
_FsVxlanNveRowStatus_Type=RowStatus
_FsVxlanNveRowStatus_Object=MibTableColumn
fsVxlanNveRowStatus=_FsVxlanNveRowStatus_Object((1,3,6,1,4,1,29601,2,89,1,2,2,1,9),_FsVxlanNveRowStatus_Type())
fsVxlanNveRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsVxlanNveRowStatus.setStatus(_A)
class _FsVxlanSuppressArp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsVxlanSuppressArp_Type.__name__=_H
_FsVxlanSuppressArp_Object=MibTableColumn
fsVxlanSuppressArp=_FsVxlanSuppressArp_Object((1,3,6,1,4,1,29601,2,89,1,2,2,1,10),_FsVxlanSuppressArp_Type())
fsVxlanSuppressArp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanSuppressArp.setStatus(_A)
_FsVxlanMCastTable_Object=MibTable
fsVxlanMCastTable=_FsVxlanMCastTable_Object((1,3,6,1,4,1,29601,2,89,1,2,3))
if mibBuilder.loadTexts:fsVxlanMCastTable.setStatus(_A)
_FsVxlanMCastEntry_Object=MibTableRow
fsVxlanMCastEntry=_FsVxlanMCastEntry_Object((1,3,6,1,4,1,29601,2,89,1,2,3,1))
fsVxlanMCastEntry.setIndexNames((0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:fsVxlanMCastEntry.setStatus(_A)
_FsVxlanMCastNveIfIndex_Type=InterfaceIndexOrZero
_FsVxlanMCastNveIfIndex_Object=MibTableColumn
fsVxlanMCastNveIfIndex=_FsVxlanMCastNveIfIndex_Object((1,3,6,1,4,1,29601,2,89,1,2,3,1,1),_FsVxlanMCastNveIfIndex_Type())
fsVxlanMCastNveIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVxlanMCastNveIfIndex.setStatus(_A)
_FsVxlanMCastVniNumber_Type=VniId
_FsVxlanMCastVniNumber_Object=MibTableColumn
fsVxlanMCastVniNumber=_FsVxlanMCastVniNumber_Object((1,3,6,1,4,1,29601,2,89,1,2,3,1,2),_FsVxlanMCastVniNumber_Type())
fsVxlanMCastVniNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVxlanMCastVniNumber.setStatus(_A)
_FsVxlanMCastGroupAddressType_Type=InetAddressType
_FsVxlanMCastGroupAddressType_Object=MibTableColumn
fsVxlanMCastGroupAddressType=_FsVxlanMCastGroupAddressType_Object((1,3,6,1,4,1,29601,2,89,1,2,3,1,3),_FsVxlanMCastGroupAddressType_Type())
fsVxlanMCastGroupAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanMCastGroupAddressType.setStatus(_A)
_FsVxlanMCastGroupAddress_Type=InetAddress
_FsVxlanMCastGroupAddress_Object=MibTableColumn
fsVxlanMCastGroupAddress=_FsVxlanMCastGroupAddress_Object((1,3,6,1,4,1,29601,2,89,1,2,3,1,4),_FsVxlanMCastGroupAddress_Type())
fsVxlanMCastGroupAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanMCastGroupAddress.setStatus(_A)
_FsVxlanMCastVtepAddressType_Type=InetAddressType
_FsVxlanMCastVtepAddressType_Object=MibTableColumn
fsVxlanMCastVtepAddressType=_FsVxlanMCastVtepAddressType_Object((1,3,6,1,4,1,29601,2,89,1,2,3,1,5),_FsVxlanMCastVtepAddressType_Type())
fsVxlanMCastVtepAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVxlanMCastVtepAddressType.setStatus(_A)
_FsVxlanMCastVtepAddress_Type=InetAddress
_FsVxlanMCastVtepAddress_Object=MibTableColumn
fsVxlanMCastVtepAddress=_FsVxlanMCastVtepAddress_Object((1,3,6,1,4,1,29601,2,89,1,2,3,1,6),_FsVxlanMCastVtepAddress_Type())
fsVxlanMCastVtepAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVxlanMCastVtepAddress.setStatus(_A)
_FsVxlanMCastRowStatus_Type=RowStatus
_FsVxlanMCastRowStatus_Object=MibTableColumn
fsVxlanMCastRowStatus=_FsVxlanMCastRowStatus_Object((1,3,6,1,4,1,29601,2,89,1,2,3,1,7),_FsVxlanMCastRowStatus_Type())
fsVxlanMCastRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsVxlanMCastRowStatus.setStatus(_A)
_FsVxlanVniVlanMapTable_Object=MibTable
fsVxlanVniVlanMapTable=_FsVxlanVniVlanMapTable_Object((1,3,6,1,4,1,29601,2,89,1,2,4))
if mibBuilder.loadTexts:fsVxlanVniVlanMapTable.setStatus(_A)
_FsVxlanVniVlanMapEntry_Object=MibTableRow
fsVxlanVniVlanMapEntry=_FsVxlanVniVlanMapEntry_Object((1,3,6,1,4,1,29601,2,89,1,2,4,1))
fsVxlanVniVlanMapEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:fsVxlanVniVlanMapEntry.setStatus(_A)
_FsVxlanVniVlanMapVlanId_Type=VlanId
_FsVxlanVniVlanMapVlanId_Object=MibTableColumn
fsVxlanVniVlanMapVlanId=_FsVxlanVniVlanMapVlanId_Object((1,3,6,1,4,1,29601,2,89,1,2,4,1,1),_FsVxlanVniVlanMapVlanId_Type())
fsVxlanVniVlanMapVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVxlanVniVlanMapVlanId.setStatus(_A)
_FsVxlanVniVlanMapVniNumber_Type=VniId
_FsVxlanVniVlanMapVniNumber_Object=MibTableColumn
fsVxlanVniVlanMapVniNumber=_FsVxlanVniVlanMapVniNumber_Object((1,3,6,1,4,1,29601,2,89,1,2,4,1,2),_FsVxlanVniVlanMapVniNumber_Type())
fsVxlanVniVlanMapVniNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanVniVlanMapVniNumber.setStatus(_A)
class _FsVxlanVniVlanMapPktSent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsVxlanVniVlanMapPktSent_Type.__name__=_G
_FsVxlanVniVlanMapPktSent_Object=MibTableColumn
fsVxlanVniVlanMapPktSent=_FsVxlanVniVlanMapPktSent_Object((1,3,6,1,4,1,29601,2,89,1,2,4,1,3),_FsVxlanVniVlanMapPktSent_Type())
fsVxlanVniVlanMapPktSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanVniVlanMapPktSent.setStatus(_A)
class _FsVxlanVniVlanMapPktRcvd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsVxlanVniVlanMapPktRcvd_Type.__name__=_G
_FsVxlanVniVlanMapPktRcvd_Object=MibTableColumn
fsVxlanVniVlanMapPktRcvd=_FsVxlanVniVlanMapPktRcvd_Object((1,3,6,1,4,1,29601,2,89,1,2,4,1,4),_FsVxlanVniVlanMapPktRcvd_Type())
fsVxlanVniVlanMapPktRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanVniVlanMapPktRcvd.setStatus(_A)
class _FsVxlanVniVlanMapPktDrpd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsVxlanVniVlanMapPktDrpd_Type.__name__=_G
_FsVxlanVniVlanMapPktDrpd_Object=MibTableColumn
fsVxlanVniVlanMapPktDrpd=_FsVxlanVniVlanMapPktDrpd_Object((1,3,6,1,4,1,29601,2,89,1,2,4,1,5),_FsVxlanVniVlanMapPktDrpd_Type())
fsVxlanVniVlanMapPktDrpd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanVniVlanMapPktDrpd.setStatus(_A)
_FsVxlanVniVlanMapRowStatus_Type=RowStatus
_FsVxlanVniVlanMapRowStatus_Object=MibTableColumn
fsVxlanVniVlanMapRowStatus=_FsVxlanVniVlanMapRowStatus_Object((1,3,6,1,4,1,29601,2,89,1,2,4,1,6),_FsVxlanVniVlanMapRowStatus_Type())
fsVxlanVniVlanMapRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsVxlanVniVlanMapRowStatus.setStatus(_A)
class _FsVxlanVniVlanDfElection_Type(TruthValue):defaultValue=2
_FsVxlanVniVlanDfElection_Type.__name__=_I
_FsVxlanVniVlanDfElection_Object=MibTableColumn
fsVxlanVniVlanDfElection=_FsVxlanVniVlanDfElection_Object((1,3,6,1,4,1,29601,2,89,1,2,4,1,7),_FsVxlanVniVlanDfElection_Type())
fsVxlanVniVlanDfElection.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVxlanVniVlanDfElection.setStatus(_A)
_FsVxlanInReplicaTable_Object=MibTable
fsVxlanInReplicaTable=_FsVxlanInReplicaTable_Object((1,3,6,1,4,1,29601,2,89,1,2,5))
if mibBuilder.loadTexts:fsVxlanInReplicaTable.setStatus(_A)
_FsVxlanInReplicaEntry_Object=MibTableRow
fsVxlanInReplicaEntry=_FsVxlanInReplicaEntry_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1))
fsVxlanInReplicaEntry.setIndexNames((0,_C,_V),(0,_C,_W))
if mibBuilder.loadTexts:fsVxlanInReplicaEntry.setStatus(_A)
_FsVxlanInReplicaNveIfIndex_Type=InterfaceIndexOrZero
_FsVxlanInReplicaNveIfIndex_Object=MibTableColumn
fsVxlanInReplicaNveIfIndex=_FsVxlanInReplicaNveIfIndex_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1,1),_FsVxlanInReplicaNveIfIndex_Type())
fsVxlanInReplicaNveIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVxlanInReplicaNveIfIndex.setStatus(_A)
_FsVxlanInReplicaVniNumber_Type=VniId
_FsVxlanInReplicaVniNumber_Object=MibTableColumn
fsVxlanInReplicaVniNumber=_FsVxlanInReplicaVniNumber_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1,2),_FsVxlanInReplicaVniNumber_Type())
fsVxlanInReplicaVniNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVxlanInReplicaVniNumber.setStatus(_A)
_FsVxlanInReplicaVtepAddressType_Type=InetAddressType
_FsVxlanInReplicaVtepAddressType_Object=MibTableColumn
fsVxlanInReplicaVtepAddressType=_FsVxlanInReplicaVtepAddressType_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1,3),_FsVxlanInReplicaVtepAddressType_Type())
fsVxlanInReplicaVtepAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVxlanInReplicaVtepAddressType.setStatus(_A)
_FsVxlanInReplicaVtepAddress_Type=InetAddress
_FsVxlanInReplicaVtepAddress_Object=MibTableColumn
fsVxlanInReplicaVtepAddress=_FsVxlanInReplicaVtepAddress_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1,4),_FsVxlanInReplicaVtepAddress_Type())
fsVxlanInReplicaVtepAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVxlanInReplicaVtepAddress.setStatus(_A)
_FsVxlanInReplicaRemoteVtepAddressType_Type=InetAddressType
_FsVxlanInReplicaRemoteVtepAddressType_Object=MibTableColumn
fsVxlanInReplicaRemoteVtepAddressType=_FsVxlanInReplicaRemoteVtepAddressType_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1,5),_FsVxlanInReplicaRemoteVtepAddressType_Type())
fsVxlanInReplicaRemoteVtepAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanInReplicaRemoteVtepAddressType.setStatus(_A)
_FsVxlanInReplicaRemoteVtepAddress1_Type=InetAddress
_FsVxlanInReplicaRemoteVtepAddress1_Object=MibTableColumn
fsVxlanInReplicaRemoteVtepAddress1=_FsVxlanInReplicaRemoteVtepAddress1_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1,6),_FsVxlanInReplicaRemoteVtepAddress1_Type())
fsVxlanInReplicaRemoteVtepAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanInReplicaRemoteVtepAddress1.setStatus(_A)
_FsVxlanInReplicaRemoteVtepAddress2_Type=InetAddress
_FsVxlanInReplicaRemoteVtepAddress2_Object=MibTableColumn
fsVxlanInReplicaRemoteVtepAddress2=_FsVxlanInReplicaRemoteVtepAddress2_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1,7),_FsVxlanInReplicaRemoteVtepAddress2_Type())
fsVxlanInReplicaRemoteVtepAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanInReplicaRemoteVtepAddress2.setStatus(_A)
_FsVxlanInReplicaRemoteVtepAddress3_Type=InetAddress
_FsVxlanInReplicaRemoteVtepAddress3_Object=MibTableColumn
fsVxlanInReplicaRemoteVtepAddress3=_FsVxlanInReplicaRemoteVtepAddress3_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1,8),_FsVxlanInReplicaRemoteVtepAddress3_Type())
fsVxlanInReplicaRemoteVtepAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanInReplicaRemoteVtepAddress3.setStatus(_A)
_FsVxlanInReplicaRemoteVtepAddress4_Type=InetAddress
_FsVxlanInReplicaRemoteVtepAddress4_Object=MibTableColumn
fsVxlanInReplicaRemoteVtepAddress4=_FsVxlanInReplicaRemoteVtepAddress4_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1,9),_FsVxlanInReplicaRemoteVtepAddress4_Type())
fsVxlanInReplicaRemoteVtepAddress4.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanInReplicaRemoteVtepAddress4.setStatus(_A)
_FsVxlanInReplicaRemoteVtepAddress5_Type=InetAddress
_FsVxlanInReplicaRemoteVtepAddress5_Object=MibTableColumn
fsVxlanInReplicaRemoteVtepAddress5=_FsVxlanInReplicaRemoteVtepAddress5_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1,10),_FsVxlanInReplicaRemoteVtepAddress5_Type())
fsVxlanInReplicaRemoteVtepAddress5.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanInReplicaRemoteVtepAddress5.setStatus(_A)
_FsVxlanInReplicaRemoteVtepAddress6_Type=InetAddress
_FsVxlanInReplicaRemoteVtepAddress6_Object=MibTableColumn
fsVxlanInReplicaRemoteVtepAddress6=_FsVxlanInReplicaRemoteVtepAddress6_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1,11),_FsVxlanInReplicaRemoteVtepAddress6_Type())
fsVxlanInReplicaRemoteVtepAddress6.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanInReplicaRemoteVtepAddress6.setStatus(_A)
_FsVxlanInReplicaRemoteVtepAddress7_Type=InetAddress
_FsVxlanInReplicaRemoteVtepAddress7_Object=MibTableColumn
fsVxlanInReplicaRemoteVtepAddress7=_FsVxlanInReplicaRemoteVtepAddress7_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1,12),_FsVxlanInReplicaRemoteVtepAddress7_Type())
fsVxlanInReplicaRemoteVtepAddress7.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanInReplicaRemoteVtepAddress7.setStatus(_A)
_FsVxlanInReplicaRemoteVtepAddress8_Type=InetAddress
_FsVxlanInReplicaRemoteVtepAddress8_Object=MibTableColumn
fsVxlanInReplicaRemoteVtepAddress8=_FsVxlanInReplicaRemoteVtepAddress8_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1,13),_FsVxlanInReplicaRemoteVtepAddress8_Type())
fsVxlanInReplicaRemoteVtepAddress8.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanInReplicaRemoteVtepAddress8.setStatus(_A)
_FsVxlanInReplicaRemoteVtepAddress9_Type=InetAddress
_FsVxlanInReplicaRemoteVtepAddress9_Object=MibTableColumn
fsVxlanInReplicaRemoteVtepAddress9=_FsVxlanInReplicaRemoteVtepAddress9_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1,14),_FsVxlanInReplicaRemoteVtepAddress9_Type())
fsVxlanInReplicaRemoteVtepAddress9.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanInReplicaRemoteVtepAddress9.setStatus(_A)
_FsVxlanInReplicaRemoteVtepAddress10_Type=InetAddress
_FsVxlanInReplicaRemoteVtepAddress10_Object=MibTableColumn
fsVxlanInReplicaRemoteVtepAddress10=_FsVxlanInReplicaRemoteVtepAddress10_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1,15),_FsVxlanInReplicaRemoteVtepAddress10_Type())
fsVxlanInReplicaRemoteVtepAddress10.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxlanInReplicaRemoteVtepAddress10.setStatus(_A)
_FsVxlanInReplicaRowStatus_Type=RowStatus
_FsVxlanInReplicaRowStatus_Object=MibTableColumn
fsVxlanInReplicaRowStatus=_FsVxlanInReplicaRowStatus_Object((1,3,6,1,4,1,29601,2,89,1,2,5,1,16),_FsVxlanInReplicaRowStatus_Type())
fsVxlanInReplicaRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsVxlanInReplicaRowStatus.setStatus(_A)
_FsEvpnVxlanEviVniMapTable_Object=MibTable
fsEvpnVxlanEviVniMapTable=_FsEvpnVxlanEviVniMapTable_Object((1,3,6,1,4,1,29601,2,89,1,2,6))
if mibBuilder.loadTexts:fsEvpnVxlanEviVniMapTable.setStatus(_A)
_FsEvpnVxlanEviVniMapEntry_Object=MibTableRow
fsEvpnVxlanEviVniMapEntry=_FsEvpnVxlanEviVniMapEntry_Object((1,3,6,1,4,1,29601,2,89,1,2,6,1))
fsEvpnVxlanEviVniMapEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:fsEvpnVxlanEviVniMapEntry.setStatus(_A)
_FsEvpnVxlanEviVniMapEviIndex_Type=EviId
_FsEvpnVxlanEviVniMapEviIndex_Object=MibTableColumn
fsEvpnVxlanEviVniMapEviIndex=_FsEvpnVxlanEviVniMapEviIndex_Object((1,3,6,1,4,1,29601,2,89,1,2,6,1,1),_FsEvpnVxlanEviVniMapEviIndex_Type())
fsEvpnVxlanEviVniMapEviIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsEvpnVxlanEviVniMapEviIndex.setStatus(_A)
_FsEvpnVxlanEviVniMapVniNumber_Type=VniId
_FsEvpnVxlanEviVniMapVniNumber_Object=MibTableColumn
fsEvpnVxlanEviVniMapVniNumber=_FsEvpnVxlanEviVniMapVniNumber_Object((1,3,6,1,4,1,29601,2,89,1,2,6,1,2),_FsEvpnVxlanEviVniMapVniNumber_Type())
fsEvpnVxlanEviVniMapVniNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fsEvpnVxlanEviVniMapVniNumber.setStatus(_A)
_FsEvpnVxlanEviVniMapBgpRD_Type=EvpnVxlanBgpRD
_FsEvpnVxlanEviVniMapBgpRD_Object=MibTableColumn
fsEvpnVxlanEviVniMapBgpRD=_FsEvpnVxlanEviVniMapBgpRD_Object((1,3,6,1,4,1,29601,2,89,1,2,6,1,3),_FsEvpnVxlanEviVniMapBgpRD_Type())
fsEvpnVxlanEviVniMapBgpRD.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEvpnVxlanEviVniMapBgpRD.setStatus(_A)
_FsEvpnVxlanEviVniESI_Type=EvpnVxlanESI
_FsEvpnVxlanEviVniESI_Object=MibTableColumn
fsEvpnVxlanEviVniESI=_FsEvpnVxlanEviVniESI_Object((1,3,6,1,4,1,29601,2,89,1,2,6,1,4),_FsEvpnVxlanEviVniESI_Type())
fsEvpnVxlanEviVniESI.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEvpnVxlanEviVniESI.setStatus(_A)
class _FsEvpnVxlanEviVniLoadBalance_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_FsEvpnVxlanEviVniLoadBalance_Type.__name__=_H
_FsEvpnVxlanEviVniLoadBalance_Object=MibTableColumn
fsEvpnVxlanEviVniLoadBalance=_FsEvpnVxlanEviVniLoadBalance_Object((1,3,6,1,4,1,29601,2,89,1,2,6,1,5),_FsEvpnVxlanEviVniLoadBalance_Type())
fsEvpnVxlanEviVniLoadBalance.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEvpnVxlanEviVniLoadBalance.setStatus(_A)
class _FsEvpnVxlanEviVniMapSentPkts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsEvpnVxlanEviVniMapSentPkts_Type.__name__=_G
_FsEvpnVxlanEviVniMapSentPkts_Object=MibTableColumn
fsEvpnVxlanEviVniMapSentPkts=_FsEvpnVxlanEviVniMapSentPkts_Object((1,3,6,1,4,1,29601,2,89,1,2,6,1,6),_FsEvpnVxlanEviVniMapSentPkts_Type())
fsEvpnVxlanEviVniMapSentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEvpnVxlanEviVniMapSentPkts.setStatus(_A)
class _FsEvpnVxlanEviVniMapRcvdPkts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsEvpnVxlanEviVniMapRcvdPkts_Type.__name__=_G
_FsEvpnVxlanEviVniMapRcvdPkts_Object=MibTableColumn
fsEvpnVxlanEviVniMapRcvdPkts=_FsEvpnVxlanEviVniMapRcvdPkts_Object((1,3,6,1,4,1,29601,2,89,1,2,6,1,7),_FsEvpnVxlanEviVniMapRcvdPkts_Type())
fsEvpnVxlanEviVniMapRcvdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEvpnVxlanEviVniMapRcvdPkts.setStatus(_A)
class _FsEvpnVxlanEviVniMapDroppedPkts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsEvpnVxlanEviVniMapDroppedPkts_Type.__name__=_G
_FsEvpnVxlanEviVniMapDroppedPkts_Object=MibTableColumn
fsEvpnVxlanEviVniMapDroppedPkts=_FsEvpnVxlanEviVniMapDroppedPkts_Object((1,3,6,1,4,1,29601,2,89,1,2,6,1,8),_FsEvpnVxlanEviVniMapDroppedPkts_Type())
fsEvpnVxlanEviVniMapDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEvpnVxlanEviVniMapDroppedPkts.setStatus(_A)
_FsEvpnVxlanEviVniMapRowStatus_Type=RowStatus
_FsEvpnVxlanEviVniMapRowStatus_Object=MibTableColumn
fsEvpnVxlanEviVniMapRowStatus=_FsEvpnVxlanEviVniMapRowStatus_Object((1,3,6,1,4,1,29601,2,89,1,2,6,1,9),_FsEvpnVxlanEviVniMapRowStatus_Type())
fsEvpnVxlanEviVniMapRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEvpnVxlanEviVniMapRowStatus.setStatus(_A)
class _FsEvpnVxlanEviVniMapBgpRDAuto_Type(TruthValue):defaultValue=2
_FsEvpnVxlanEviVniMapBgpRDAuto_Type.__name__=_I
_FsEvpnVxlanEviVniMapBgpRDAuto_Object=MibTableColumn
fsEvpnVxlanEviVniMapBgpRDAuto=_FsEvpnVxlanEviVniMapBgpRDAuto_Object((1,3,6,1,4,1,29601,2,89,1,2,6,1,10),_FsEvpnVxlanEviVniMapBgpRDAuto_Type())
fsEvpnVxlanEviVniMapBgpRDAuto.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEvpnVxlanEviVniMapBgpRDAuto.setStatus(_A)
_FsEvpnVxlanBgpRTTable_Object=MibTable
fsEvpnVxlanBgpRTTable=_FsEvpnVxlanBgpRTTable_Object((1,3,6,1,4,1,29601,2,89,1,2,7))
if mibBuilder.loadTexts:fsEvpnVxlanBgpRTTable.setStatus(_A)
_FsEvpnVxlanBgpRTEntry_Object=MibTableRow
fsEvpnVxlanBgpRTEntry=_FsEvpnVxlanBgpRTEntry_Object((1,3,6,1,4,1,29601,2,89,1,2,7,1))
fsEvpnVxlanBgpRTEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_X),(0,_C,_Y))
if mibBuilder.loadTexts:fsEvpnVxlanBgpRTEntry.setStatus(_A)
_FsEvpnVxlanBgpRTIndex_Type=Unsigned32
_FsEvpnVxlanBgpRTIndex_Object=MibTableColumn
fsEvpnVxlanBgpRTIndex=_FsEvpnVxlanBgpRTIndex_Object((1,3,6,1,4,1,29601,2,89,1,2,7,1,1),_FsEvpnVxlanBgpRTIndex_Type())
fsEvpnVxlanBgpRTIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsEvpnVxlanBgpRTIndex.setStatus(_A)
_FsEvpnVxlanBgpRTType_Type=EvpnVxlanBgpRTType
_FsEvpnVxlanBgpRTType_Object=MibTableColumn
fsEvpnVxlanBgpRTType=_FsEvpnVxlanBgpRTType_Object((1,3,6,1,4,1,29601,2,89,1,2,7,1,2),_FsEvpnVxlanBgpRTType_Type())
fsEvpnVxlanBgpRTType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsEvpnVxlanBgpRTType.setStatus(_A)
_FsEvpnVxlanBgpRT_Type=EvpnVxlanBgpRD
_FsEvpnVxlanBgpRT_Object=MibTableColumn
fsEvpnVxlanBgpRT=_FsEvpnVxlanBgpRT_Object((1,3,6,1,4,1,29601,2,89,1,2,7,1,3),_FsEvpnVxlanBgpRT_Type())
fsEvpnVxlanBgpRT.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEvpnVxlanBgpRT.setStatus(_A)
_FsEvpnVxlanBgpRTRowStatus_Type=RowStatus
_FsEvpnVxlanBgpRTRowStatus_Object=MibTableColumn
fsEvpnVxlanBgpRTRowStatus=_FsEvpnVxlanBgpRTRowStatus_Object((1,3,6,1,4,1,29601,2,89,1,2,7,1,4),_FsEvpnVxlanBgpRTRowStatus_Type())
fsEvpnVxlanBgpRTRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEvpnVxlanBgpRTRowStatus.setStatus(_A)
class _FsEvpnVxlanBgpRTAuto_Type(TruthValue):defaultValue=2
_FsEvpnVxlanBgpRTAuto_Type.__name__=_I
_FsEvpnVxlanBgpRTAuto_Object=MibTableColumn
fsEvpnVxlanBgpRTAuto=_FsEvpnVxlanBgpRTAuto_Object((1,3,6,1,4,1,29601,2,89,1,2,7,1,5),_FsEvpnVxlanBgpRTAuto_Type())
fsEvpnVxlanBgpRTAuto.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEvpnVxlanBgpRTAuto.setStatus(_A)
_FsEvpnVxlanVrfTable_Object=MibTable
fsEvpnVxlanVrfTable=_FsEvpnVxlanVrfTable_Object((1,3,6,1,4,1,29601,2,89,1,2,8))
if mibBuilder.loadTexts:fsEvpnVxlanVrfTable.setStatus(_A)
_FsEvpnVxlanVrfEntry_Object=MibTableRow
fsEvpnVxlanVrfEntry=_FsEvpnVxlanVrfEntry_Object((1,3,6,1,4,1,29601,2,89,1,2,8,1))
fsEvpnVxlanVrfEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:fsEvpnVxlanVrfEntry.setStatus(_A)
_FsEvpnVxlanVrfName_Type=EvpnVxlanVrfName
_FsEvpnVxlanVrfName_Object=MibTableColumn
fsEvpnVxlanVrfName=_FsEvpnVxlanVrfName_Object((1,3,6,1,4,1,29601,2,89,1,2,8,1,1),_FsEvpnVxlanVrfName_Type())
fsEvpnVxlanVrfName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsEvpnVxlanVrfName.setStatus(_A)
_FsEvpnVxlanVrfRD_Type=EvpnVxlanBgpRD
_FsEvpnVxlanVrfRD_Object=MibTableColumn
fsEvpnVxlanVrfRD=_FsEvpnVxlanVrfRD_Object((1,3,6,1,4,1,29601,2,89,1,2,8,1,2),_FsEvpnVxlanVrfRD_Type())
fsEvpnVxlanVrfRD.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEvpnVxlanVrfRD.setStatus(_A)
_FsEvpnVxlanVrfRowStatus_Type=RowStatus
_FsEvpnVxlanVrfRowStatus_Object=MibTableColumn
fsEvpnVxlanVrfRowStatus=_FsEvpnVxlanVrfRowStatus_Object((1,3,6,1,4,1,29601,2,89,1,2,8,1,3),_FsEvpnVxlanVrfRowStatus_Type())
fsEvpnVxlanVrfRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEvpnVxlanVrfRowStatus.setStatus(_A)
_FsEvpnVxlanVrfRTTable_Object=MibTable
fsEvpnVxlanVrfRTTable=_FsEvpnVxlanVrfRTTable_Object((1,3,6,1,4,1,29601,2,89,1,2,9))
if mibBuilder.loadTexts:fsEvpnVxlanVrfRTTable.setStatus(_A)
_FsEvpnVxlanVrfRTEntry_Object=MibTableRow
fsEvpnVxlanVrfRTEntry=_FsEvpnVxlanVrfRTEntry_Object((1,3,6,1,4,1,29601,2,89,1,2,9,1))
fsEvpnVxlanVrfRTEntry.setIndexNames((0,_C,_N),(0,_C,_Z),(0,_C,_a))
if mibBuilder.loadTexts:fsEvpnVxlanVrfRTEntry.setStatus(_A)
_FsEvpnVxlanVrfRTIndex_Type=Unsigned32
_FsEvpnVxlanVrfRTIndex_Object=MibTableColumn
fsEvpnVxlanVrfRTIndex=_FsEvpnVxlanVrfRTIndex_Object((1,3,6,1,4,1,29601,2,89,1,2,9,1,1),_FsEvpnVxlanVrfRTIndex_Type())
fsEvpnVxlanVrfRTIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsEvpnVxlanVrfRTIndex.setStatus(_A)
_FsEvpnVxlanVrfRTType_Type=EvpnVxlanBgpRTType
_FsEvpnVxlanVrfRTType_Object=MibTableColumn
fsEvpnVxlanVrfRTType=_FsEvpnVxlanVrfRTType_Object((1,3,6,1,4,1,29601,2,89,1,2,9,1,2),_FsEvpnVxlanVrfRTType_Type())
fsEvpnVxlanVrfRTType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsEvpnVxlanVrfRTType.setStatus(_A)
_FsEvpnVxlanVrfRT_Type=EvpnVxlanBgpRD
_FsEvpnVxlanVrfRT_Object=MibTableColumn
fsEvpnVxlanVrfRT=_FsEvpnVxlanVrfRT_Object((1,3,6,1,4,1,29601,2,89,1,2,9,1,3),_FsEvpnVxlanVrfRT_Type())
fsEvpnVxlanVrfRT.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEvpnVxlanVrfRT.setStatus(_A)
_FsEvpnVxlanVrfRTRowStatus_Type=RowStatus
_FsEvpnVxlanVrfRTRowStatus_Object=MibTableColumn
fsEvpnVxlanVrfRTRowStatus=_FsEvpnVxlanVrfRTRowStatus_Object((1,3,6,1,4,1,29601,2,89,1,2,9,1,4),_FsEvpnVxlanVrfRTRowStatus_Type())
fsEvpnVxlanVrfRTRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEvpnVxlanVrfRTRowStatus.setStatus(_A)
_FsEvpnVxlanMultihomedPeerTable_Object=MibTable
fsEvpnVxlanMultihomedPeerTable=_FsEvpnVxlanMultihomedPeerTable_Object((1,3,6,1,4,1,29601,2,89,1,2,10))
if mibBuilder.loadTexts:fsEvpnVxlanMultihomedPeerTable.setStatus(_A)
_FsEvpnVxlanMultihomedPeerEntry_Object=MibTableRow
fsEvpnVxlanMultihomedPeerEntry=_FsEvpnVxlanMultihomedPeerEntry_Object((1,3,6,1,4,1,29601,2,89,1,2,10,1))
fsEvpnVxlanMultihomedPeerEntry.setIndexNames((0,_C,_b),(0,_C,_c),(0,_C,_d))
if mibBuilder.loadTexts:fsEvpnVxlanMultihomedPeerEntry.setStatus(_A)
_FsEvpnVxlanPeerIpAddressType_Type=InetAddressType
_FsEvpnVxlanPeerIpAddressType_Object=MibTableColumn
fsEvpnVxlanPeerIpAddressType=_FsEvpnVxlanPeerIpAddressType_Object((1,3,6,1,4,1,29601,2,89,1,2,10,1,1),_FsEvpnVxlanPeerIpAddressType_Type())
fsEvpnVxlanPeerIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsEvpnVxlanPeerIpAddressType.setStatus(_A)
_FsEvpnVxlanPeerIpAddress_Type=InetAddress
_FsEvpnVxlanPeerIpAddress_Object=MibTableColumn
fsEvpnVxlanPeerIpAddress=_FsEvpnVxlanPeerIpAddress_Object((1,3,6,1,4,1,29601,2,89,1,2,10,1,2),_FsEvpnVxlanPeerIpAddress_Type())
fsEvpnVxlanPeerIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsEvpnVxlanPeerIpAddress.setStatus(_A)
_FsEvpnVxlanMHEviVniESI_Type=EvpnVxlanESI
_FsEvpnVxlanMHEviVniESI_Object=MibTableColumn
fsEvpnVxlanMHEviVniESI=_FsEvpnVxlanMHEviVniESI_Object((1,3,6,1,4,1,29601,2,89,1,2,10,1,3),_FsEvpnVxlanMHEviVniESI_Type())
fsEvpnVxlanMHEviVniESI.setMaxAccess(_D)
if mibBuilder.loadTexts:fsEvpnVxlanMHEviVniESI.setStatus(_A)
class _FsEvpnVxlanOrdinalNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_FsEvpnVxlanOrdinalNum_Type.__name__=_G
_FsEvpnVxlanOrdinalNum_Object=MibTableColumn
fsEvpnVxlanOrdinalNum=_FsEvpnVxlanOrdinalNum_Object((1,3,6,1,4,1,29601,2,89,1,2,10,1,4),_FsEvpnVxlanOrdinalNum_Type())
fsEvpnVxlanOrdinalNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEvpnVxlanOrdinalNum.setStatus(_A)
_FsEvpnVxlanMultihomedPeerRowStatus_Type=RowStatus
_FsEvpnVxlanMultihomedPeerRowStatus_Object=MibTableColumn
fsEvpnVxlanMultihomedPeerRowStatus=_FsEvpnVxlanMultihomedPeerRowStatus_Object((1,3,6,1,4,1,29601,2,89,1,2,10,1,5),_FsEvpnVxlanMultihomedPeerRowStatus_Type())
fsEvpnVxlanMultihomedPeerRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEvpnVxlanMultihomedPeerRowStatus.setStatus(_A)
_FsVxlanEcmpNveTable_Object=MibTable
fsVxlanEcmpNveTable=_FsVxlanEcmpNveTable_Object((1,3,6,1,4,1,29601,2,89,1,2,11))
if mibBuilder.loadTexts:fsVxlanEcmpNveTable.setStatus(_A)
_FsVxlanEcmpNveEntry_Object=MibTableRow
fsVxlanEcmpNveEntry=_FsVxlanEcmpNveEntry_Object((1,3,6,1,4,1,29601,2,89,1,2,11,1))
fsVxlanEcmpNveEntry.setIndexNames((0,_C,_e),(0,_C,_f),(0,_C,_g),(0,_C,_h),(0,_C,_i))
if mibBuilder.loadTexts:fsVxlanEcmpNveEntry.setStatus(_A)
_FsVxlanEcmpNveIfIndex_Type=InterfaceIndexOrZero
_FsVxlanEcmpNveIfIndex_Object=MibTableColumn
fsVxlanEcmpNveIfIndex=_FsVxlanEcmpNveIfIndex_Object((1,3,6,1,4,1,29601,2,89,1,2,11,1,1),_FsVxlanEcmpNveIfIndex_Type())
fsVxlanEcmpNveIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVxlanEcmpNveIfIndex.setStatus(_A)
_FsVxlanEcmpNveVniNumber_Type=VniId
_FsVxlanEcmpNveVniNumber_Object=MibTableColumn
fsVxlanEcmpNveVniNumber=_FsVxlanEcmpNveVniNumber_Object((1,3,6,1,4,1,29601,2,89,1,2,11,1,2),_FsVxlanEcmpNveVniNumber_Type())
fsVxlanEcmpNveVniNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVxlanEcmpNveVniNumber.setStatus(_A)
_FsVxlanEcmpNveDestVmMac_Type=MacAddress
_FsVxlanEcmpNveDestVmMac_Object=MibTableColumn
fsVxlanEcmpNveDestVmMac=_FsVxlanEcmpNveDestVmMac_Object((1,3,6,1,4,1,29601,2,89,1,2,11,1,3),_FsVxlanEcmpNveDestVmMac_Type())
fsVxlanEcmpNveDestVmMac.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVxlanEcmpNveDestVmMac.setStatus(_A)
_FsVxlanEcmpNveVtepAddressType_Type=InetAddressType
_FsVxlanEcmpNveVtepAddressType_Object=MibTableColumn
fsVxlanEcmpNveVtepAddressType=_FsVxlanEcmpNveVtepAddressType_Object((1,3,6,1,4,1,29601,2,89,1,2,11,1,4),_FsVxlanEcmpNveVtepAddressType_Type())
fsVxlanEcmpNveVtepAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVxlanEcmpNveVtepAddressType.setStatus(_A)
_FsVxlanEcmpNveVtepAddress_Type=InetAddress
_FsVxlanEcmpNveVtepAddress_Object=MibTableColumn
fsVxlanEcmpNveVtepAddress=_FsVxlanEcmpNveVtepAddress_Object((1,3,6,1,4,1,29601,2,89,1,2,11,1,5),_FsVxlanEcmpNveVtepAddress_Type())
fsVxlanEcmpNveVtepAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVxlanEcmpNveVtepAddress.setStatus(_A)
_FsVxlanEcmpNveRemoteVtepAddressType_Type=InetAddressType
_FsVxlanEcmpNveRemoteVtepAddressType_Object=MibTableColumn
fsVxlanEcmpNveRemoteVtepAddressType=_FsVxlanEcmpNveRemoteVtepAddressType_Object((1,3,6,1,4,1,29601,2,89,1,2,11,1,6),_FsVxlanEcmpNveRemoteVtepAddressType_Type())
fsVxlanEcmpNveRemoteVtepAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVxlanEcmpNveRemoteVtepAddressType.setStatus(_A)
_FsVxlanEcmpNveRemoteVtepAddress_Type=InetAddress
_FsVxlanEcmpNveRemoteVtepAddress_Object=MibTableColumn
fsVxlanEcmpNveRemoteVtepAddress=_FsVxlanEcmpNveRemoteVtepAddress_Object((1,3,6,1,4,1,29601,2,89,1,2,11,1,7),_FsVxlanEcmpNveRemoteVtepAddress_Type())
fsVxlanEcmpNveRemoteVtepAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVxlanEcmpNveRemoteVtepAddress.setStatus(_A)
_FsVxlanEcmpNveStorageType_Type=StorageType
_FsVxlanEcmpNveStorageType_Object=MibTableColumn
fsVxlanEcmpNveStorageType=_FsVxlanEcmpNveStorageType_Object((1,3,6,1,4,1,29601,2,89,1,2,11,1,8),_FsVxlanEcmpNveStorageType_Type())
fsVxlanEcmpNveStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVxlanEcmpNveStorageType.setStatus(_A)
class _FsVxlanEcmpSuppressArp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsVxlanEcmpSuppressArp_Type.__name__=_H
_FsVxlanEcmpSuppressArp_Object=MibTableColumn
fsVxlanEcmpSuppressArp=_FsVxlanEcmpSuppressArp_Object((1,3,6,1,4,1,29601,2,89,1,2,11,1,9),_FsVxlanEcmpSuppressArp_Type())
fsVxlanEcmpSuppressArp.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVxlanEcmpSuppressArp.setStatus(_A)
_FsVxlanEcmpMHEviVniESI_Type=EvpnVxlanESI
_FsVxlanEcmpMHEviVniESI_Object=MibTableColumn
fsVxlanEcmpMHEviVniESI=_FsVxlanEcmpMHEviVniESI_Object((1,3,6,1,4,1,29601,2,89,1,2,11,1,10),_FsVxlanEcmpMHEviVniESI_Type())
fsVxlanEcmpMHEviVniESI.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVxlanEcmpMHEviVniESI.setStatus(_A)
class _FsVxlanEcmpActive_Type(TruthValue):defaultValue=2
_FsVxlanEcmpActive_Type.__name__=_I
_FsVxlanEcmpActive_Object=MibTableColumn
fsVxlanEcmpActive=_FsVxlanEcmpActive_Object((1,3,6,1,4,1,29601,2,89,1,2,11,1,11),_FsVxlanEcmpActive_Type())
fsVxlanEcmpActive.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVxlanEcmpActive.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'VlanId':VlanId,'VniId':VniId,'EviId':EviId,'EvpnVxlanBgpRD':EvpnVxlanBgpRD,'EvpnVxlanESI':EvpnVxlanESI,'EvpnVxlanBgpRTType':EvpnVxlanBgpRTType,'EvpnVxlanVrfName':EvpnVxlanVrfName,'fsvxlan':fsvxlan,'fsVxlanObjects':fsVxlanObjects,'fsVxlanSystem':fsVxlanSystem,'fsVxlanEnable':fsVxlanEnable,'fsVxlanUdpPort':fsVxlanUdpPort,'fsVxlanTraceOption':fsVxlanTraceOption,'fsVxlanNotificationCntl':fsVxlanNotificationCntl,'fsEvpnVxlanEnable':fsEvpnVxlanEnable,'fsVxlanConfigObjects':fsVxlanConfigObjects,'fsVxlanVtepTable':fsVxlanVtepTable,'fsVxlanVtepEntry':fsVxlanVtepEntry,_O:fsVxlanVtepNveIfIndex,'fsVxlanVtepAddressType':fsVxlanVtepAddressType,'fsVxlanVtepAddress':fsVxlanVtepAddress,'fsVxlanVtepRowStatus':fsVxlanVtepRowStatus,'fsVxlanNveTable':fsVxlanNveTable,'fsVxlanNveEntry':fsVxlanNveEntry,_P:fsVxlanNveIfIndex,_Q:fsVxlanNveVniNumber,_R:fsVxlanNveDestVmMac,'fsVxlanNveVtepAddressType':fsVxlanNveVtepAddressType,'fsVxlanNveVtepAddress':fsVxlanNveVtepAddress,'fsVxlanNveRemoteVtepAddressType':fsVxlanNveRemoteVtepAddressType,'fsVxlanNveRemoteVtepAddress':fsVxlanNveRemoteVtepAddress,'fsVxlanNveStorageType':fsVxlanNveStorageType,'fsVxlanNveRowStatus':fsVxlanNveRowStatus,'fsVxlanSuppressArp':fsVxlanSuppressArp,'fsVxlanMCastTable':fsVxlanMCastTable,'fsVxlanMCastEntry':fsVxlanMCastEntry,_S:fsVxlanMCastNveIfIndex,_T:fsVxlanMCastVniNumber,'fsVxlanMCastGroupAddressType':fsVxlanMCastGroupAddressType,'fsVxlanMCastGroupAddress':fsVxlanMCastGroupAddress,'fsVxlanMCastVtepAddressType':fsVxlanMCastVtepAddressType,'fsVxlanMCastVtepAddress':fsVxlanMCastVtepAddress,'fsVxlanMCastRowStatus':fsVxlanMCastRowStatus,'fsVxlanVniVlanMapTable':fsVxlanVniVlanMapTable,'fsVxlanVniVlanMapEntry':fsVxlanVniVlanMapEntry,_U:fsVxlanVniVlanMapVlanId,'fsVxlanVniVlanMapVniNumber':fsVxlanVniVlanMapVniNumber,'fsVxlanVniVlanMapPktSent':fsVxlanVniVlanMapPktSent,'fsVxlanVniVlanMapPktRcvd':fsVxlanVniVlanMapPktRcvd,'fsVxlanVniVlanMapPktDrpd':fsVxlanVniVlanMapPktDrpd,'fsVxlanVniVlanMapRowStatus':fsVxlanVniVlanMapRowStatus,'fsVxlanVniVlanDfElection':fsVxlanVniVlanDfElection,'fsVxlanInReplicaTable':fsVxlanInReplicaTable,'fsVxlanInReplicaEntry':fsVxlanInReplicaEntry,_V:fsVxlanInReplicaNveIfIndex,_W:fsVxlanInReplicaVniNumber,'fsVxlanInReplicaVtepAddressType':fsVxlanInReplicaVtepAddressType,'fsVxlanInReplicaVtepAddress':fsVxlanInReplicaVtepAddress,'fsVxlanInReplicaRemoteVtepAddressType':fsVxlanInReplicaRemoteVtepAddressType,'fsVxlanInReplicaRemoteVtepAddress1':fsVxlanInReplicaRemoteVtepAddress1,'fsVxlanInReplicaRemoteVtepAddress2':fsVxlanInReplicaRemoteVtepAddress2,'fsVxlanInReplicaRemoteVtepAddress3':fsVxlanInReplicaRemoteVtepAddress3,'fsVxlanInReplicaRemoteVtepAddress4':fsVxlanInReplicaRemoteVtepAddress4,'fsVxlanInReplicaRemoteVtepAddress5':fsVxlanInReplicaRemoteVtepAddress5,'fsVxlanInReplicaRemoteVtepAddress6':fsVxlanInReplicaRemoteVtepAddress6,'fsVxlanInReplicaRemoteVtepAddress7':fsVxlanInReplicaRemoteVtepAddress7,'fsVxlanInReplicaRemoteVtepAddress8':fsVxlanInReplicaRemoteVtepAddress8,'fsVxlanInReplicaRemoteVtepAddress9':fsVxlanInReplicaRemoteVtepAddress9,'fsVxlanInReplicaRemoteVtepAddress10':fsVxlanInReplicaRemoteVtepAddress10,'fsVxlanInReplicaRowStatus':fsVxlanInReplicaRowStatus,'fsEvpnVxlanEviVniMapTable':fsEvpnVxlanEviVniMapTable,'fsEvpnVxlanEviVniMapEntry':fsEvpnVxlanEviVniMapEntry,_L:fsEvpnVxlanEviVniMapEviIndex,_M:fsEvpnVxlanEviVniMapVniNumber,'fsEvpnVxlanEviVniMapBgpRD':fsEvpnVxlanEviVniMapBgpRD,'fsEvpnVxlanEviVniESI':fsEvpnVxlanEviVniESI,'fsEvpnVxlanEviVniLoadBalance':fsEvpnVxlanEviVniLoadBalance,'fsEvpnVxlanEviVniMapSentPkts':fsEvpnVxlanEviVniMapSentPkts,'fsEvpnVxlanEviVniMapRcvdPkts':fsEvpnVxlanEviVniMapRcvdPkts,'fsEvpnVxlanEviVniMapDroppedPkts':fsEvpnVxlanEviVniMapDroppedPkts,'fsEvpnVxlanEviVniMapRowStatus':fsEvpnVxlanEviVniMapRowStatus,'fsEvpnVxlanEviVniMapBgpRDAuto':fsEvpnVxlanEviVniMapBgpRDAuto,'fsEvpnVxlanBgpRTTable':fsEvpnVxlanBgpRTTable,'fsEvpnVxlanBgpRTEntry':fsEvpnVxlanBgpRTEntry,_X:fsEvpnVxlanBgpRTIndex,_Y:fsEvpnVxlanBgpRTType,'fsEvpnVxlanBgpRT':fsEvpnVxlanBgpRT,'fsEvpnVxlanBgpRTRowStatus':fsEvpnVxlanBgpRTRowStatus,'fsEvpnVxlanBgpRTAuto':fsEvpnVxlanBgpRTAuto,'fsEvpnVxlanVrfTable':fsEvpnVxlanVrfTable,'fsEvpnVxlanVrfEntry':fsEvpnVxlanVrfEntry,_N:fsEvpnVxlanVrfName,'fsEvpnVxlanVrfRD':fsEvpnVxlanVrfRD,'fsEvpnVxlanVrfRowStatus':fsEvpnVxlanVrfRowStatus,'fsEvpnVxlanVrfRTTable':fsEvpnVxlanVrfRTTable,'fsEvpnVxlanVrfRTEntry':fsEvpnVxlanVrfRTEntry,_Z:fsEvpnVxlanVrfRTIndex,_a:fsEvpnVxlanVrfRTType,'fsEvpnVxlanVrfRT':fsEvpnVxlanVrfRT,'fsEvpnVxlanVrfRTRowStatus':fsEvpnVxlanVrfRTRowStatus,'fsEvpnVxlanMultihomedPeerTable':fsEvpnVxlanMultihomedPeerTable,'fsEvpnVxlanMultihomedPeerEntry':fsEvpnVxlanMultihomedPeerEntry,_b:fsEvpnVxlanPeerIpAddressType,_c:fsEvpnVxlanPeerIpAddress,_d:fsEvpnVxlanMHEviVniESI,'fsEvpnVxlanOrdinalNum':fsEvpnVxlanOrdinalNum,'fsEvpnVxlanMultihomedPeerRowStatus':fsEvpnVxlanMultihomedPeerRowStatus,'fsVxlanEcmpNveTable':fsVxlanEcmpNveTable,'fsVxlanEcmpNveEntry':fsVxlanEcmpNveEntry,_e:fsVxlanEcmpNveIfIndex,_f:fsVxlanEcmpNveVniNumber,_g:fsVxlanEcmpNveDestVmMac,'fsVxlanEcmpNveVtepAddressType':fsVxlanEcmpNveVtepAddressType,'fsVxlanEcmpNveVtepAddress':fsVxlanEcmpNveVtepAddress,_h:fsVxlanEcmpNveRemoteVtepAddressType,_i:fsVxlanEcmpNveRemoteVtepAddress,'fsVxlanEcmpNveStorageType':fsVxlanEcmpNveStorageType,'fsVxlanEcmpSuppressArp':fsVxlanEcmpSuppressArp,'fsVxlanEcmpMHEviVniESI':fsVxlanEcmpMHEviVniESI,'fsVxlanEcmpActive':fsVxlanEcmpActive})