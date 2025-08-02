_AH='sourceLearningTrapsGroup'
_AG='slMacToPortMacGroup'
_AF='hashCollisionNotificationGroup'
_AE='bcmHashCollisionTrapGroup'
_AD='halHashCollisionTrapGroup'
_AC='slMacLearningGroup'
_AB='slMacGeneralGroup'
_AA='slPCamNotificationGroup'
_A9='slMacAgingGroup'
_A8='slMacAddressGroup'
_A7='halHashCollisionTrap'
_A6='bcmHashCollisionTrap'
_A5='slPCAMStatusTrap'
_A4='slMacToPortMacRowStatus'
_A3='slMacLearningControlStatus'
_A2='slDistributedMacMode'
_A1='slMacAgingRowStatus'
_A0='slMacAgingValue'
_z='slMacAddressGblRowStatus'
_y='slMacAddressGblProtocol'
_x='slMacAddressGblManagement'
_w='slMacAddressGblDisposition'
_v='slMacAddressProtocol'
_u='slMacAddressRowStatus'
_t='slMacAddressDisposition'
_s='slMacAddressManagement'
_r='slMacAddressGbl'
_q='slSubId'
_p='slServiceId'
_o='slOriginId'
_n='slLocaleType'
_m='slMacDomain'
_l='userNetworkProf'
_k='hostIntegrity'
_j='quarantined'
_i='filtering'
_h='bridging'
_g='staticMulticast'
_f='learned'
_e='deleteOnTimeout'
_d='deleteOnReset'
_c='permanent'
_b='slPCAMStatus'
_a='slPCAMSliceNumber'
_Z='slPCAMSlotNumber'
_Y='halHashCollisionTable'
_X='halHashCollisionVlan'
_W='halHashCollisionPort'
_V='halHashCollisionSlot'
_U='halHashCollisionMac'
_T='bcmHashCollisionTable'
_S='bcmHashCollisionVlan'
_R='bcmHashCollisionPort'
_Q='bcmHashCollisionSlot'
_P='bcmHashCollisionMac'
_O='slMacToPortMacAddress'
_N='slMacToPortMacVlanId'
_M='slMacAddress'
_L='DisplayString'
_K='dot1qVlanIndex'
_J='Q-BRIDGE-MIB'
_I='ifIndex'
_H='IF-MIB'
_G='read-write'
_F='not-accessible'
_E='read-create'
_D='accessible-for-notify'
_C='Integer32'
_B='current'
_A='ALCATEL-IND1-MAC-ADDRESS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1MacAddress,sourceLearningTraps=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1MacAddress','sourceLearningTraps')
ifIndex,=mibBuilder.importSymbols(_H,_I)
dot1qVlanIndex,=mibBuilder.importSymbols(_J,_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'MacAddress','PhysAddress','RowStatus','TextualConvention')
alcatelIND1MacAddressMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,8,1))
if mibBuilder.loadTexts:alcatelIND1MacAddressMIB.setRevisions(('2007-04-03 00:00',))
class MacAddressProtocolType(TextualConvention,Integer32):status=_B;displayHint='x';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlcatelIND1MacAddressMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1MacAddressMIBObjects=_AlcatelIND1MacAddressMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,8,1,1))
if mibBuilder.loadTexts:alcatelIND1MacAddressMIBObjects.setStatus(_B)
_SlMacAddressTable_Object=MibTable
slMacAddressTable=_SlMacAddressTable_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,1))
if mibBuilder.loadTexts:slMacAddressTable.setStatus(_B)
_SlMacAddressEntry_Object=MibTableRow
slMacAddressEntry=_SlMacAddressEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,1,1))
slMacAddressEntry.setIndexNames((0,_H,_I),(0,_J,_K),(0,_A,_M))
if mibBuilder.loadTexts:slMacAddressEntry.setStatus(_B)
_SlMacAddress_Type=MacAddress
_SlMacAddress_Object=MibTableColumn
slMacAddress=_SlMacAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,1,1,1),_SlMacAddress_Type())
slMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:slMacAddress.setStatus(_B)
class _SlMacAddressManagement_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_f,4),(_g,5)))
_SlMacAddressManagement_Type.__name__=_C
_SlMacAddressManagement_Object=MibTableColumn
slMacAddressManagement=_SlMacAddressManagement_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,1,1,2),_SlMacAddressManagement_Type())
slMacAddressManagement.setMaxAccess(_E)
if mibBuilder.loadTexts:slMacAddressManagement.setStatus(_B)
class _SlMacAddressDisposition_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3),(_k,4),(_l,5)))
_SlMacAddressDisposition_Type.__name__=_C
_SlMacAddressDisposition_Object=MibTableColumn
slMacAddressDisposition=_SlMacAddressDisposition_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,1,1,3),_SlMacAddressDisposition_Type())
slMacAddressDisposition.setMaxAccess(_E)
if mibBuilder.loadTexts:slMacAddressDisposition.setStatus(_B)
_SlMacAddressRowStatus_Type=RowStatus
_SlMacAddressRowStatus_Object=MibTableColumn
slMacAddressRowStatus=_SlMacAddressRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,1,1,4),_SlMacAddressRowStatus_Type())
slMacAddressRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:slMacAddressRowStatus.setStatus(_B)
_SlMacAddressProtocol_Type=MacAddressProtocolType
_SlMacAddressProtocol_Object=MibTableColumn
slMacAddressProtocol=_SlMacAddressProtocol_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,1,1,5),_SlMacAddressProtocol_Type())
slMacAddressProtocol.setMaxAccess('read-only')
if mibBuilder.loadTexts:slMacAddressProtocol.setStatus(_B)
_SlMacAddressAgingTable_Object=MibTable
slMacAddressAgingTable=_SlMacAddressAgingTable_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,2))
if mibBuilder.loadTexts:slMacAddressAgingTable.setStatus(_B)
_SlMacAddressAgingEntry_Object=MibTableRow
slMacAddressAgingEntry=_SlMacAddressAgingEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,2,1))
slMacAddressAgingEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:slMacAddressAgingEntry.setStatus(_B)
class _SlMacAgingValue_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_SlMacAgingValue_Type.__name__=_C
_SlMacAgingValue_Object=MibTableColumn
slMacAgingValue=_SlMacAgingValue_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,2,1,1),_SlMacAgingValue_Type())
slMacAgingValue.setMaxAccess(_E)
if mibBuilder.loadTexts:slMacAgingValue.setStatus(_B)
_SlMacAgingRowStatus_Type=RowStatus
_SlMacAgingRowStatus_Object=MibTableColumn
slMacAgingRowStatus=_SlMacAgingRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,2,1,2),_SlMacAgingRowStatus_Type())
slMacAgingRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:slMacAgingRowStatus.setStatus(_B)
_SlPCamTrapObj_ObjectIdentity=ObjectIdentity
slPCamTrapObj=_SlPCamTrapObj_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,3))
class _SlPCAMSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_SlPCAMSlotNumber_Type.__name__=_C
_SlPCAMSlotNumber_Object=MibScalar
slPCAMSlotNumber=_SlPCAMSlotNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,3,1),_SlPCAMSlotNumber_Type())
slPCAMSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:slPCAMSlotNumber.setStatus(_B)
class _SlPCAMSliceNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_SlPCAMSliceNumber_Type.__name__=_C
_SlPCAMSliceNumber_Object=MibScalar
slPCAMSliceNumber=_SlPCAMSliceNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,3,2),_SlPCAMSliceNumber_Type())
slPCAMSliceNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:slPCAMSliceNumber.setStatus(_B)
class _SlPCAMStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('lowWaterMark',1),('highWaterMark',2),('floodWaterMark',3),('full',4)))
_SlPCAMStatus_Type.__name__=_C
_SlPCAMStatus_Object=MibScalar
slPCAMStatus=_SlPCAMStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,3,3),_SlPCAMStatus_Type())
slPCAMStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:slPCAMStatus.setStatus(_B)
_SlMacToPortMacTable_Object=MibTable
slMacToPortMacTable=_SlMacToPortMacTable_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,4))
if mibBuilder.loadTexts:slMacToPortMacTable.setStatus(_B)
_SlMacToPortMacEntry_Object=MibTableRow
slMacToPortMacEntry=_SlMacToPortMacEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,4,1))
slMacToPortMacEntry.setIndexNames((0,_A,_N),(0,_A,_O))
if mibBuilder.loadTexts:slMacToPortMacEntry.setStatus(_B)
class _SlMacToPortMacVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SlMacToPortMacVlanId_Type.__name__=_C
_SlMacToPortMacVlanId_Object=MibTableColumn
slMacToPortMacVlanId=_SlMacToPortMacVlanId_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,4,1,1),_SlMacToPortMacVlanId_Type())
slMacToPortMacVlanId.setMaxAccess(_G)
if mibBuilder.loadTexts:slMacToPortMacVlanId.setStatus(_B)
_SlMacToPortMacAddress_Type=MacAddress
_SlMacToPortMacAddress_Object=MibTableColumn
slMacToPortMacAddress=_SlMacToPortMacAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,4,1,2),_SlMacToPortMacAddress_Type())
slMacToPortMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:slMacToPortMacAddress.setStatus(_B)
_SlMacToPortMacRowStatus_Type=RowStatus
_SlMacToPortMacRowStatus_Object=MibTableColumn
slMacToPortMacRowStatus=_SlMacToPortMacRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,4,1,3),_SlMacToPortMacRowStatus_Type())
slMacToPortMacRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:slMacToPortMacRowStatus.setStatus(_B)
class _SlDistributedMacMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_SlDistributedMacMode_Type.__name__=_C
_SlDistributedMacMode_Object=MibScalar
slDistributedMacMode=_SlDistributedMacMode_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,5),_SlDistributedMacMode_Type())
slDistributedMacMode.setMaxAccess(_G)
if mibBuilder.loadTexts:slDistributedMacMode.setStatus(_B)
_BcmHashCollisionTrapObj_ObjectIdentity=ObjectIdentity
bcmHashCollisionTrapObj=_BcmHashCollisionTrapObj_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,6))
_BcmHashCollisionMac_Type=MacAddress
_BcmHashCollisionMac_Object=MibScalar
bcmHashCollisionMac=_BcmHashCollisionMac_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,6,1),_BcmHashCollisionMac_Type())
bcmHashCollisionMac.setMaxAccess(_D)
if mibBuilder.loadTexts:bcmHashCollisionMac.setStatus(_B)
_BcmHashCollisionSlot_Type=Unsigned32
_BcmHashCollisionSlot_Object=MibScalar
bcmHashCollisionSlot=_BcmHashCollisionSlot_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,6,2),_BcmHashCollisionSlot_Type())
bcmHashCollisionSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:bcmHashCollisionSlot.setStatus(_B)
_BcmHashCollisionPort_Type=Unsigned32
_BcmHashCollisionPort_Object=MibScalar
bcmHashCollisionPort=_BcmHashCollisionPort_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,6,3),_BcmHashCollisionPort_Type())
bcmHashCollisionPort.setMaxAccess(_D)
if mibBuilder.loadTexts:bcmHashCollisionPort.setStatus(_B)
_BcmHashCollisionVlan_Type=Unsigned32
_BcmHashCollisionVlan_Object=MibScalar
bcmHashCollisionVlan=_BcmHashCollisionVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,6,4),_BcmHashCollisionVlan_Type())
bcmHashCollisionVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:bcmHashCollisionVlan.setStatus(_B)
class _BcmHashCollisionTable_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_BcmHashCollisionTable_Type.__name__=_L
_BcmHashCollisionTable_Object=MibScalar
bcmHashCollisionTable=_BcmHashCollisionTable_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,6,5),_BcmHashCollisionTable_Type())
bcmHashCollisionTable.setMaxAccess(_D)
if mibBuilder.loadTexts:bcmHashCollisionTable.setStatus(_B)
_SlMacLearningControlTable_Object=MibTable
slMacLearningControlTable=_SlMacLearningControlTable_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,7))
if mibBuilder.loadTexts:slMacLearningControlTable.setStatus(_B)
_SlMacLearningControlEntry_Object=MibTableRow
slMacLearningControlEntry=_SlMacLearningControlEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,7,1))
slMacLearningControlEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:slMacLearningControlEntry.setStatus(_B)
class _SlMacLearningControlStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_SlMacLearningControlStatus_Type.__name__=_C
_SlMacLearningControlStatus_Object=MibTableColumn
slMacLearningControlStatus=_SlMacLearningControlStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,7,1,1),_SlMacLearningControlStatus_Type())
slMacLearningControlStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:slMacLearningControlStatus.setStatus(_B)
_AlaSlMacAddressGlobalTable_Object=MibTable
alaSlMacAddressGlobalTable=_AlaSlMacAddressGlobalTable_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,8))
if mibBuilder.loadTexts:alaSlMacAddressGlobalTable.setStatus(_B)
_AlaSlMacAddressGlobalEntry_Object=MibTableRow
alaSlMacAddressGlobalEntry=_AlaSlMacAddressGlobalEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,8,1))
alaSlMacAddressGlobalEntry.setIndexNames((0,_A,_m),(0,_A,_n),(0,_A,_o),(0,_A,_p),(0,_A,_q),(0,_A,_r))
if mibBuilder.loadTexts:alaSlMacAddressGlobalEntry.setStatus(_B)
class _SlMacDomain_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('all',0),('vlan',1),('vpls',2)))
_SlMacDomain_Type.__name__=_C
_SlMacDomain_Object=MibTableColumn
slMacDomain=_SlMacDomain_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,8,1,1),_SlMacDomain_Type())
slMacDomain.setMaxAccess(_F)
if mibBuilder.loadTexts:slMacDomain.setStatus(_B)
class _SlLocaleType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('default',0),('sap',1),('sBind',2)))
_SlLocaleType_Type.__name__=_C
_SlLocaleType_Object=MibTableColumn
slLocaleType=_SlLocaleType_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,8,1,2),_SlLocaleType_Type())
slLocaleType.setMaxAccess(_F)
if mibBuilder.loadTexts:slLocaleType.setStatus(_B)
class _SlOriginId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SlOriginId_Type.__name__=_C
_SlOriginId_Object=MibTableColumn
slOriginId=_SlOriginId_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,8,1,3),_SlOriginId_Type())
slOriginId.setMaxAccess(_F)
if mibBuilder.loadTexts:slOriginId.setStatus(_B)
class _SlServiceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SlServiceId_Type.__name__=_C
_SlServiceId_Object=MibTableColumn
slServiceId=_SlServiceId_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,8,1,4),_SlServiceId_Type())
slServiceId.setMaxAccess(_F)
if mibBuilder.loadTexts:slServiceId.setStatus(_B)
class _SlSubId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SlSubId_Type.__name__=_C
_SlSubId_Object=MibTableColumn
slSubId=_SlSubId_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,8,1,5),_SlSubId_Type())
slSubId.setMaxAccess(_F)
if mibBuilder.loadTexts:slSubId.setStatus(_B)
_SlMacAddressGbl_Type=MacAddress
_SlMacAddressGbl_Object=MibTableColumn
slMacAddressGbl=_SlMacAddressGbl_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,8,1,6),_SlMacAddressGbl_Type())
slMacAddressGbl.setMaxAccess(_F)
if mibBuilder.loadTexts:slMacAddressGbl.setStatus(_B)
class _SlMacAddressGblManagement_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_f,4),(_g,5)))
_SlMacAddressGblManagement_Type.__name__=_C
_SlMacAddressGblManagement_Object=MibTableColumn
slMacAddressGblManagement=_SlMacAddressGblManagement_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,8,1,7),_SlMacAddressGblManagement_Type())
slMacAddressGblManagement.setMaxAccess(_E)
if mibBuilder.loadTexts:slMacAddressGblManagement.setStatus(_B)
class _SlMacAddressGblDisposition_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3),(_k,4),(_l,5)))
_SlMacAddressGblDisposition_Type.__name__=_C
_SlMacAddressGblDisposition_Object=MibTableColumn
slMacAddressGblDisposition=_SlMacAddressGblDisposition_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,8,1,8),_SlMacAddressGblDisposition_Type())
slMacAddressGblDisposition.setMaxAccess(_E)
if mibBuilder.loadTexts:slMacAddressGblDisposition.setStatus(_B)
_SlMacAddressGblRowStatus_Type=RowStatus
_SlMacAddressGblRowStatus_Object=MibTableColumn
slMacAddressGblRowStatus=_SlMacAddressGblRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,8,1,9),_SlMacAddressGblRowStatus_Type())
slMacAddressGblRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:slMacAddressGblRowStatus.setStatus(_B)
_SlMacAddressGblProtocol_Type=MacAddressProtocolType
_SlMacAddressGblProtocol_Object=MibTableColumn
slMacAddressGblProtocol=_SlMacAddressGblProtocol_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,8,1,10),_SlMacAddressGblProtocol_Type())
slMacAddressGblProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:slMacAddressGblProtocol.setStatus(_B)
_HalHashCollisionTrapObj_ObjectIdentity=ObjectIdentity
halHashCollisionTrapObj=_HalHashCollisionTrapObj_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,10))
_HalHashCollisionMac_Type=MacAddress
_HalHashCollisionMac_Object=MibScalar
halHashCollisionMac=_HalHashCollisionMac_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,10,1),_HalHashCollisionMac_Type())
halHashCollisionMac.setMaxAccess(_D)
if mibBuilder.loadTexts:halHashCollisionMac.setStatus(_B)
_HalHashCollisionSlot_Type=Unsigned32
_HalHashCollisionSlot_Object=MibScalar
halHashCollisionSlot=_HalHashCollisionSlot_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,10,2),_HalHashCollisionSlot_Type())
halHashCollisionSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:halHashCollisionSlot.setStatus(_B)
_HalHashCollisionPort_Type=Unsigned32
_HalHashCollisionPort_Object=MibScalar
halHashCollisionPort=_HalHashCollisionPort_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,10,3),_HalHashCollisionPort_Type())
halHashCollisionPort.setMaxAccess(_D)
if mibBuilder.loadTexts:halHashCollisionPort.setStatus(_B)
_HalHashCollisionVlan_Type=Unsigned32
_HalHashCollisionVlan_Object=MibScalar
halHashCollisionVlan=_HalHashCollisionVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,10,4),_HalHashCollisionVlan_Type())
halHashCollisionVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:halHashCollisionVlan.setStatus(_B)
class _HalHashCollisionTable_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HalHashCollisionTable_Type.__name__=_L
_HalHashCollisionTable_Object=MibScalar
halHashCollisionTable=_HalHashCollisionTable_Object((1,3,6,1,4,1,6486,800,1,2,1,8,1,1,10,5),_HalHashCollisionTable_Type())
halHashCollisionTable.setMaxAccess(_D)
if mibBuilder.loadTexts:halHashCollisionTable.setStatus(_B)
_AlcatelIND1MacAddressMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1MacAddressMIBConformance=_AlcatelIND1MacAddressMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,8,1,2))
if mibBuilder.loadTexts:alcatelIND1MacAddressMIBConformance.setStatus(_B)
_AlcatelIND1MacAddressMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1MacAddressMIBGroups=_AlcatelIND1MacAddressMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,8,1,2,1))
if mibBuilder.loadTexts:alcatelIND1MacAddressMIBGroups.setStatus(_B)
_AlcatelIND1MacAddressMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1MacAddressMIBCompliances=_AlcatelIND1MacAddressMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,8,1,2,2))
if mibBuilder.loadTexts:alcatelIND1MacAddressMIBCompliances.setStatus(_B)
slMacAddressGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,8,1,2,1,1))
slMacAddressGroup.setObjects(*((_A,_M),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:slMacAddressGroup.setStatus(_B)
slMacAgingGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,8,1,2,1,2))
slMacAgingGroup.setObjects(*((_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:slMacAgingGroup.setStatus(_B)
slMacGeneralGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,8,1,2,1,4))
slMacGeneralGroup.setObjects((_A,_A2))
if mibBuilder.loadTexts:slMacGeneralGroup.setStatus(_B)
slMacLearningGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,8,1,2,1,5))
slMacLearningGroup.setObjects((_A,_A3))
if mibBuilder.loadTexts:slMacLearningGroup.setStatus(_B)
bcmHashCollisionTrapGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,8,1,2,1,6))
bcmHashCollisionTrapGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:bcmHashCollisionTrapGroup.setStatus(_B)
halHashCollisionTrapGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,8,1,2,1,7))
halHashCollisionTrapGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:halHashCollisionTrapGroup.setStatus(_B)
slMacToPortMacGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,8,1,2,1,9))
slMacToPortMacGroup.setObjects(*((_A,_N),(_A,_O),(_A,_A4)))
if mibBuilder.loadTexts:slMacToPortMacGroup.setStatus(_B)
sourceLearningTrapsGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,8,1,2,1,10))
sourceLearningTrapsGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:sourceLearningTrapsGroup.setStatus(_B)
slPCAMStatusTrap=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,9,0,1))
slPCAMStatusTrap.setObjects(*((_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:slPCAMStatusTrap.setStatus(_B)
bcmHashCollisionTrap=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,9,0,3))
bcmHashCollisionTrap.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:bcmHashCollisionTrap.setStatus(_B)
halHashCollisionTrap=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,9,0,4))
halHashCollisionTrap.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:halHashCollisionTrap.setStatus(_B)
slPCamNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,8,1,2,1,3))
slPCamNotificationGroup.setObjects((_A,_A5))
if mibBuilder.loadTexts:slPCamNotificationGroup.setStatus(_B)
hashCollisionNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,8,1,2,1,8))
hashCollisionNotificationGroup.setObjects(*((_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:hashCollisionNotificationGroup.setStatus(_B)
alcatelIND1MacAddressMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,8,1,2,2,1))
alcatelIND1MacAddressMIBCompliance.setObjects(*((_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:alcatelIND1MacAddressMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'MacAddressProtocolType':MacAddressProtocolType,'alcatelIND1MacAddressMIB':alcatelIND1MacAddressMIB,'alcatelIND1MacAddressMIBObjects':alcatelIND1MacAddressMIBObjects,'slMacAddressTable':slMacAddressTable,'slMacAddressEntry':slMacAddressEntry,_M:slMacAddress,_s:slMacAddressManagement,_t:slMacAddressDisposition,_u:slMacAddressRowStatus,_v:slMacAddressProtocol,'slMacAddressAgingTable':slMacAddressAgingTable,'slMacAddressAgingEntry':slMacAddressAgingEntry,_A0:slMacAgingValue,_A1:slMacAgingRowStatus,'slPCamTrapObj':slPCamTrapObj,_Z:slPCAMSlotNumber,_a:slPCAMSliceNumber,_b:slPCAMStatus,'slMacToPortMacTable':slMacToPortMacTable,'slMacToPortMacEntry':slMacToPortMacEntry,_N:slMacToPortMacVlanId,_O:slMacToPortMacAddress,_A4:slMacToPortMacRowStatus,_A2:slDistributedMacMode,'bcmHashCollisionTrapObj':bcmHashCollisionTrapObj,_P:bcmHashCollisionMac,_Q:bcmHashCollisionSlot,_R:bcmHashCollisionPort,_S:bcmHashCollisionVlan,_T:bcmHashCollisionTable,'slMacLearningControlTable':slMacLearningControlTable,'slMacLearningControlEntry':slMacLearningControlEntry,_A3:slMacLearningControlStatus,'alaSlMacAddressGlobalTable':alaSlMacAddressGlobalTable,'alaSlMacAddressGlobalEntry':alaSlMacAddressGlobalEntry,_m:slMacDomain,_n:slLocaleType,_o:slOriginId,_p:slServiceId,_q:slSubId,_r:slMacAddressGbl,_x:slMacAddressGblManagement,_w:slMacAddressGblDisposition,_z:slMacAddressGblRowStatus,_y:slMacAddressGblProtocol,'halHashCollisionTrapObj':halHashCollisionTrapObj,_U:halHashCollisionMac,_V:halHashCollisionSlot,_W:halHashCollisionPort,_X:halHashCollisionVlan,_Y:halHashCollisionTable,'alcatelIND1MacAddressMIBConformance':alcatelIND1MacAddressMIBConformance,'alcatelIND1MacAddressMIBGroups':alcatelIND1MacAddressMIBGroups,_A8:slMacAddressGroup,_A9:slMacAgingGroup,_AA:slPCamNotificationGroup,_AB:slMacGeneralGroup,_AC:slMacLearningGroup,_AE:bcmHashCollisionTrapGroup,_AD:halHashCollisionTrapGroup,_AF:hashCollisionNotificationGroup,_AG:slMacToPortMacGroup,_AH:sourceLearningTrapsGroup,'alcatelIND1MacAddressMIBCompliances':alcatelIND1MacAddressMIBCompliances,'alcatelIND1MacAddressMIBCompliance':alcatelIND1MacAddressMIBCompliance,_A5:slPCAMStatusTrap,_A6:bcmHashCollisionTrap,_A7:halHashCollisionTrap})