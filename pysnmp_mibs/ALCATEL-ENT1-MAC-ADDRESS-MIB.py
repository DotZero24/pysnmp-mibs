_l='slMacVlanLearningGroup'
_k='slMacLearningGroup'
_j='slMacGeneralGroup'
_i='slMacAgingGroup'
_h='slMacAddressGroup'
_g='slMacLearningVlanControlStatus'
_f='slMacLearningControlStatus'
_e='slDistributedMacMode'
_d='slMacAgingRowStatus'
_c='slMacAgingValue'
_b='slVxLanVnID'
_a='slSvcISID'
_Z='slMacAddressGblGroupField'
_Y='slMacAddressGblProtocol'
_X='slMacAddressGblRowStatus'
_W='slMacAddressGblDisposition'
_V='slMacAddressGblManagement'
_U='slMacAddressGbl'
_T='slSubId'
_S='slServiceId'
_R='slOriginId'
_Q='slLocaleType'
_P='slMacDomain'
_O='disabled'
_N='enabled'
_M='Unsigned32'
_L='dot1qVlanIndex'
_K='Q-BRIDGE-MIB'
_J='ifIndex'
_I='IF-MIB'
_H='vlanNumber'
_G='ALCATEL-ENT1-VLAN-MGR-MIB'
_F='read-write'
_E='not-accessible'
_D='read-create'
_C='Integer32'
_B='ALCATEL-ENT1-MAC-ADDRESS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1MacAddress,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1MacAddress')
vlanNumber,=mibBuilder.importSymbols(_G,_H)
ifIndex,=mibBuilder.importSymbols(_I,_J)
dot1qVlanIndex,=mibBuilder.importSymbols(_K,_L)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
alcatelIND1MacAddressMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,8,1))
if mibBuilder.loadTexts:alcatelIND1MacAddressMIB.setRevisions(('2010-05-13 00:00','2007-04-03 00:00'))
class MacAddressProtocolType(TextualConvention,Integer32):status=_A;displayHint='x';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlcatelIND1MacAddressMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1MacAddressMIBNotifications=_AlcatelIND1MacAddressMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,8,1,0))
if mibBuilder.loadTexts:alcatelIND1MacAddressMIBNotifications.setStatus(_A)
_AlcatelIND1MacAddressMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1MacAddressMIBObjects=_AlcatelIND1MacAddressMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,8,1,1))
if mibBuilder.loadTexts:alcatelIND1MacAddressMIBObjects.setStatus(_A)
_SlMacAddressAgingTable_Object=MibTable
slMacAddressAgingTable=_SlMacAddressAgingTable_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,2))
if mibBuilder.loadTexts:slMacAddressAgingTable.setStatus(_A)
_SlMacAddressAgingEntry_Object=MibTableRow
slMacAddressAgingEntry=_SlMacAddressAgingEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,2,1))
slMacAddressAgingEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:slMacAddressAgingEntry.setStatus(_A)
class _SlMacAgingValue_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_SlMacAgingValue_Type.__name__=_C
_SlMacAgingValue_Object=MibTableColumn
slMacAgingValue=_SlMacAgingValue_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,2,1,1),_SlMacAgingValue_Type())
slMacAgingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:slMacAgingValue.setStatus(_A)
_SlMacAgingRowStatus_Type=RowStatus
_SlMacAgingRowStatus_Object=MibTableColumn
slMacAgingRowStatus=_SlMacAgingRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,2,1,2),_SlMacAgingRowStatus_Type())
slMacAgingRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:slMacAgingRowStatus.setStatus(_A)
class _SlDistributedMacMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_SlDistributedMacMode_Type.__name__=_C
_SlDistributedMacMode_Object=MibScalar
slDistributedMacMode=_SlDistributedMacMode_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,5),_SlDistributedMacMode_Type())
slDistributedMacMode.setMaxAccess(_F)
if mibBuilder.loadTexts:slDistributedMacMode.setStatus(_A)
_SlMacLearningControlTable_Object=MibTable
slMacLearningControlTable=_SlMacLearningControlTable_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,7))
if mibBuilder.loadTexts:slMacLearningControlTable.setStatus(_A)
_SlMacLearningControlEntry_Object=MibTableRow
slMacLearningControlEntry=_SlMacLearningControlEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,7,1))
slMacLearningControlEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:slMacLearningControlEntry.setStatus(_A)
class _SlMacLearningControlStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_SlMacLearningControlStatus_Type.__name__=_C
_SlMacLearningControlStatus_Object=MibTableColumn
slMacLearningControlStatus=_SlMacLearningControlStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,7,1,1),_SlMacLearningControlStatus_Type())
slMacLearningControlStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:slMacLearningControlStatus.setStatus(_A)
_AlaSlMacAddressGlobalTable_Object=MibTable
alaSlMacAddressGlobalTable=_AlaSlMacAddressGlobalTable_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,8))
if mibBuilder.loadTexts:alaSlMacAddressGlobalTable.setStatus(_A)
_AlaSlMacAddressGlobalEntry_Object=MibTableRow
alaSlMacAddressGlobalEntry=_AlaSlMacAddressGlobalEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,8,1))
alaSlMacAddressGlobalEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_R),(0,_B,_S),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:alaSlMacAddressGlobalEntry.setStatus(_A)
class _SlMacDomain_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('all',0),('vlan',1),('vpls',2),('spbm',3),('evb',4),('local',5),('vxlan',6)))
_SlMacDomain_Type.__name__=_C
_SlMacDomain_Object=MibTableColumn
slMacDomain=_SlMacDomain_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,8,1,1),_SlMacDomain_Type())
slMacDomain.setMaxAccess(_E)
if mibBuilder.loadTexts:slMacDomain.setStatus(_A)
class _SlLocaleType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('default',0),('sap',1),('sBind',2)))
_SlLocaleType_Type.__name__=_C
_SlLocaleType_Object=MibTableColumn
slLocaleType=_SlLocaleType_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,8,1,2),_SlLocaleType_Type())
slLocaleType.setMaxAccess(_E)
if mibBuilder.loadTexts:slLocaleType.setStatus(_A)
class _SlOriginId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_SlOriginId_Type.__name__=_C
_SlOriginId_Object=MibTableColumn
slOriginId=_SlOriginId_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,8,1,3),_SlOriginId_Type())
slOriginId.setMaxAccess(_E)
if mibBuilder.loadTexts:slOriginId.setStatus(_A)
class _SlServiceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,32767))
_SlServiceId_Type.__name__=_C
_SlServiceId_Object=MibTableColumn
slServiceId=_SlServiceId_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,8,1,4),_SlServiceId_Type())
slServiceId.setMaxAccess(_E)
if mibBuilder.loadTexts:slServiceId.setStatus(_A)
class _SlSubId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SlSubId_Type.__name__=_C
_SlSubId_Object=MibTableColumn
slSubId=_SlSubId_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,8,1,5),_SlSubId_Type())
slSubId.setMaxAccess(_E)
if mibBuilder.loadTexts:slSubId.setStatus(_A)
_SlMacAddressGbl_Type=MacAddress
_SlMacAddressGbl_Object=MibTableColumn
slMacAddressGbl=_SlMacAddressGbl_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,8,1,6),_SlMacAddressGbl_Type())
slMacAddressGbl.setMaxAccess(_E)
if mibBuilder.loadTexts:slMacAddressGbl.setStatus(_A)
class _SlMacAddressGblManagement_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('permanent',1),('deleteOnReset',2),('deleteOnTimeout',3),('learned',4),('staticMulticast',5)))
_SlMacAddressGblManagement_Type.__name__=_C
_SlMacAddressGblManagement_Object=MibTableColumn
slMacAddressGblManagement=_SlMacAddressGblManagement_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,8,1,7),_SlMacAddressGblManagement_Type())
slMacAddressGblManagement.setMaxAccess(_D)
if mibBuilder.loadTexts:slMacAddressGblManagement.setStatus(_A)
class _SlMacAddressGblDisposition_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('bridging',1),('filtering',2),('quarantined',3),('hostIntegrity',4),('userNetworkProf',5),('servicing',6)))
_SlMacAddressGblDisposition_Type.__name__=_C
_SlMacAddressGblDisposition_Object=MibTableColumn
slMacAddressGblDisposition=_SlMacAddressGblDisposition_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,8,1,8),_SlMacAddressGblDisposition_Type())
slMacAddressGblDisposition.setMaxAccess(_D)
if mibBuilder.loadTexts:slMacAddressGblDisposition.setStatus(_A)
_SlMacAddressGblRowStatus_Type=RowStatus
_SlMacAddressGblRowStatus_Object=MibTableColumn
slMacAddressGblRowStatus=_SlMacAddressGblRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,8,1,9),_SlMacAddressGblRowStatus_Type())
slMacAddressGblRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:slMacAddressGblRowStatus.setStatus(_A)
_SlMacAddressGblProtocol_Type=MacAddressProtocolType
_SlMacAddressGblProtocol_Object=MibTableColumn
slMacAddressGblProtocol=_SlMacAddressGblProtocol_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,8,1,10),_SlMacAddressGblProtocol_Type())
slMacAddressGblProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:slMacAddressGblProtocol.setStatus(_A)
_SlMacAddressGblGroupField_Type=Unsigned32
_SlMacAddressGblGroupField_Object=MibTableColumn
slMacAddressGblGroupField=_SlMacAddressGblGroupField_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,8,1,11),_SlMacAddressGblGroupField_Type())
slMacAddressGblGroupField.setMaxAccess(_D)
if mibBuilder.loadTexts:slMacAddressGblGroupField.setStatus(_A)
class _SlSvcISID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(256,16777214))
_SlSvcISID_Type.__name__=_C
_SlSvcISID_Object=MibTableColumn
slSvcISID=_SlSvcISID_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,8,1,12),_SlSvcISID_Type())
slSvcISID.setMaxAccess(_D)
if mibBuilder.loadTexts:slSvcISID.setStatus(_A)
class _SlVxLanVnID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,16777215))
_SlVxLanVnID_Type.__name__=_M
_SlVxLanVnID_Object=MibTableColumn
slVxLanVnID=_SlVxLanVnID_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,8,1,13),_SlVxLanVnID_Type())
slVxLanVnID.setMaxAccess(_D)
if mibBuilder.loadTexts:slVxLanVnID.setStatus(_A)
_SlMacLearningVlanControlTable_Object=MibTable
slMacLearningVlanControlTable=_SlMacLearningVlanControlTable_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,10))
if mibBuilder.loadTexts:slMacLearningVlanControlTable.setStatus(_A)
_SlMacLearningVlanControlEntry_Object=MibTableRow
slMacLearningVlanControlEntry=_SlMacLearningVlanControlEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,10,1))
slMacLearningVlanControlEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:slMacLearningVlanControlEntry.setStatus(_A)
class _SlMacLearningVlanControlStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_SlMacLearningVlanControlStatus_Type.__name__=_C
_SlMacLearningVlanControlStatus_Object=MibTableColumn
slMacLearningVlanControlStatus=_SlMacLearningVlanControlStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,8,1,1,10,1,1),_SlMacLearningVlanControlStatus_Type())
slMacLearningVlanControlStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:slMacLearningVlanControlStatus.setStatus(_A)
_AlcatelIND1MacAddressMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1MacAddressMIBConformance=_AlcatelIND1MacAddressMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,8,1,2))
if mibBuilder.loadTexts:alcatelIND1MacAddressMIBConformance.setStatus(_A)
_AlcatelIND1MacAddressMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1MacAddressMIBGroups=_AlcatelIND1MacAddressMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,8,1,2,1))
if mibBuilder.loadTexts:alcatelIND1MacAddressMIBGroups.setStatus(_A)
_AlcatelIND1MacAddressMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1MacAddressMIBCompliances=_AlcatelIND1MacAddressMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,8,1,2,2))
if mibBuilder.loadTexts:alcatelIND1MacAddressMIBCompliances.setStatus(_A)
slMacAddressGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,8,1,2,1,1))
slMacAddressGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:slMacAddressGroup.setStatus(_A)
slMacAgingGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,8,1,2,1,2))
slMacAgingGroup.setObjects(*((_B,_c),(_B,_d)))
if mibBuilder.loadTexts:slMacAgingGroup.setStatus(_A)
slMacGeneralGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,8,1,2,1,3))
slMacGeneralGroup.setObjects((_B,_e))
if mibBuilder.loadTexts:slMacGeneralGroup.setStatus(_A)
slMacLearningGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,8,1,2,1,4))
slMacLearningGroup.setObjects((_B,_f))
if mibBuilder.loadTexts:slMacLearningGroup.setStatus(_A)
slMacVlanLearningGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,8,1,2,1,5))
slMacVlanLearningGroup.setObjects((_B,_g))
if mibBuilder.loadTexts:slMacVlanLearningGroup.setStatus(_A)
alcatelIND1MacAddressMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,8,1,2,2,1))
alcatelIND1MacAddressMIBCompliance.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:alcatelIND1MacAddressMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MacAddressProtocolType':MacAddressProtocolType,'alcatelIND1MacAddressMIB':alcatelIND1MacAddressMIB,'alcatelIND1MacAddressMIBNotifications':alcatelIND1MacAddressMIBNotifications,'alcatelIND1MacAddressMIBObjects':alcatelIND1MacAddressMIBObjects,'slMacAddressAgingTable':slMacAddressAgingTable,'slMacAddressAgingEntry':slMacAddressAgingEntry,_c:slMacAgingValue,_d:slMacAgingRowStatus,_e:slDistributedMacMode,'slMacLearningControlTable':slMacLearningControlTable,'slMacLearningControlEntry':slMacLearningControlEntry,_f:slMacLearningControlStatus,'alaSlMacAddressGlobalTable':alaSlMacAddressGlobalTable,'alaSlMacAddressGlobalEntry':alaSlMacAddressGlobalEntry,_P:slMacDomain,_Q:slLocaleType,_R:slOriginId,_S:slServiceId,_T:slSubId,_U:slMacAddressGbl,_V:slMacAddressGblManagement,_W:slMacAddressGblDisposition,_X:slMacAddressGblRowStatus,_Y:slMacAddressGblProtocol,_Z:slMacAddressGblGroupField,_a:slSvcISID,_b:slVxLanVnID,'slMacLearningVlanControlTable':slMacLearningVlanControlTable,'slMacLearningVlanControlEntry':slMacLearningVlanControlEntry,_g:slMacLearningVlanControlStatus,'alcatelIND1MacAddressMIBConformance':alcatelIND1MacAddressMIBConformance,'alcatelIND1MacAddressMIBGroups':alcatelIND1MacAddressMIBGroups,_h:slMacAddressGroup,_i:slMacAgingGroup,_j:slMacGeneralGroup,_k:slMacLearningGroup,_l:slMacVlanLearningGroup,'alcatelIND1MacAddressMIBCompliances':alcatelIND1MacAddressMIBCompliances,'alcatelIND1MacAddressMIBCompliance':alcatelIND1MacAddressMIBCompliance})