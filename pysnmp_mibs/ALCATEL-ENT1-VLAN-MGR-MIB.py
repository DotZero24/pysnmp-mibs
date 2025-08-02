_i='vlanMgrVlanSetGroup'
_h='vlanMgrVpaGroup'
_g='vlanMgrVlanGroup'
_f='vlanSetVstkVlanCount'
_e='vlanSetIpRouterCount'
_d='vlanSetDynamicVlanCount'
_c='vlanSetVlanCount'
_b='vpaStatus'
_a='vpaState'
_Z='vpaType'
_Y='vlanAfdCfg'
_X='vlanMtu'
_W='vlanType'
_V='vlanSrcLearningStatus'
_U='vlanRouterStatus'
_T='vlanStatus'
_S='vlanOperStatus'
_R='vlanAdmStatus'
_Q='vlanDescription'
_P='vpaIfIndex'
_O='vpaVlanNumber'
_N='dynamic'
_M='inactive'
_L='disabled'
_K='enabled'
_J='vlanNumber'
_I='Unsigned32'
_H='SnmpAdminString'
_G='invalid'
_F='not-accessible'
_E='read-only'
_D='read-create'
_C='Integer32'
_B='ALCATEL-ENT1-VLAN-MGR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1VlanMgt,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1VlanMgt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1VLANMgrMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,3,1))
if mibBuilder.loadTexts:alcatelIND1VLANMgrMIB.setRevisions(('2007-04-03 00:00',))
_AlcatelIND1VLANMgrMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1VLANMgrMIBObjects=_AlcatelIND1VLANMgrMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,3,1,1))
if mibBuilder.loadTexts:alcatelIND1VLANMgrMIBObjects.setStatus(_A)
_VlanMgrVlan_ObjectIdentity=ObjectIdentity
vlanMgrVlan=_VlanMgrVlan_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,1))
_VlanTable_Object=MibTable
vlanTable=_VlanTable_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,1,1))
if mibBuilder.loadTexts:vlanTable.setStatus(_A)
_VlanEntry_Object=MibTableRow
vlanEntry=_VlanEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,1,1,1))
vlanEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:vlanEntry.setStatus(_A)
class _VlanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanNumber_Type.__name__=_C
_VlanNumber_Object=MibTableColumn
vlanNumber=_VlanNumber_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,1,1,1,1),_VlanNumber_Type())
vlanNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanNumber.setStatus(_A)
class _VlanDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VlanDescription_Type.__name__=_H
_VlanDescription_Object=MibTableColumn
vlanDescription=_VlanDescription_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,1,1,1,2),_VlanDescription_Type())
vlanDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanDescription.setStatus(_A)
class _VlanAdmStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_VlanAdmStatus_Type.__name__=_C
_VlanAdmStatus_Object=MibTableColumn
vlanAdmStatus=_VlanAdmStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,1,1,1,3),_VlanAdmStatus_Type())
vlanAdmStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanAdmStatus.setStatus(_A)
class _VlanOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),(_M,2)))
_VlanOperStatus_Type.__name__=_C
_VlanOperStatus_Object=MibTableColumn
vlanOperStatus=_VlanOperStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,1,1,1,4),_VlanOperStatus_Type())
vlanOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanOperStatus.setStatus(_A)
_VlanStatus_Type=RowStatus
_VlanStatus_Object=MibTableColumn
vlanStatus=_VlanStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,1,1,1,5),_VlanStatus_Type())
vlanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanStatus.setStatus(_A)
class _VlanRouterStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('ipv4router',1),('ipv6router',2),('both',3)))
_VlanRouterStatus_Type.__name__=_C
_VlanRouterStatus_Object=MibTableColumn
vlanRouterStatus=_VlanRouterStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,1,1,1,6),_VlanRouterStatus_Type())
vlanRouterStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanRouterStatus.setStatus(_A)
class _VlanSrcLearningStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_VlanSrcLearningStatus_Type.__name__=_C
_VlanSrcLearningStatus_Object=MibTableColumn
vlanSrcLearningStatus=_VlanSrcLearningStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,1,1,1,7),_VlanSrcLearningStatus_Type())
vlanSrcLearningStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanSrcLearningStatus.setStatus(_A)
class _VlanType_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*((_G,0),('service',1),('multicastEnt',2),('multicastService',3),(_N,4),('standard',5),('ipc',6),('vipVlan',7),('erpVlan',8),('mtpVlan',9),('unpDynamic',10),('dynamicRemote',11),('bvlan',12),('controlBvlan',13),('evbVlan',14),('vcmipc',15),('fcoeVlan',16),('openflowVlan',17),('routerVlan',18),('primaryVlan',19),('isolatedVlan',20),('communityVlan',21),('allVlan',22),('invalidVlan',23)))
_VlanType_Type.__name__=_C
_VlanType_Object=MibTableColumn
vlanType=_VlanType_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,1,1,1,8),_VlanType_Type())
vlanType.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanType.setStatus(_A)
class _VlanMtu_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,10222))
_VlanMtu_Type.__name__=_C
_VlanMtu_Object=MibTableColumn
vlanMtu=_VlanMtu_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,1,1,1,9),_VlanMtu_Type())
vlanMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanMtu.setStatus(_A)
class _VlanAfdCfg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_VlanAfdCfg_Type.__name__=_C
_VlanAfdCfg_Object=MibTableColumn
vlanAfdCfg=_VlanAfdCfg_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,1,1,1,10),_VlanAfdCfg_Type())
vlanAfdCfg.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanAfdCfg.setStatus(_A)
_VlanMgrVpa_ObjectIdentity=ObjectIdentity
vlanMgrVpa=_VlanMgrVpa_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,2))
_VpaTable_Object=MibTable
vpaTable=_VpaTable_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,2,1))
if mibBuilder.loadTexts:vpaTable.setStatus(_A)
_VpaEntry_Object=MibTableRow
vpaEntry=_VpaEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,2,1,1))
vpaEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:vpaEntry.setStatus(_A)
class _VpaVlanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VpaVlanNumber_Type.__name__=_C
_VpaVlanNumber_Object=MibTableColumn
vpaVlanNumber=_VpaVlanNumber_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,2,1,1,1),_VpaVlanNumber_Type())
vpaVlanNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:vpaVlanNumber.setStatus(_A)
class _VpaIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,4294967295))
_VpaIfIndex_Type.__name__=_I
_VpaIfIndex_Object=MibTableColumn
vpaIfIndex=_VpaIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,2,1,1,2),_VpaIfIndex_Type())
vpaIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:vpaIfIndex.setStatus(_A)
class _VpaType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_G,0),('cfgDefault',1),('qTagged',2),(_N,3),('vstkDoubleTag',4),('vstkTranslate',5),('forbidden',6),('mirrored',7),('bvpa',8),('unpUntagged',9),('unpTagged',10),('evbTagged',11)))
_VpaType_Type.__name__=_C
_VpaType_Object=MibTableColumn
vpaType=_VpaType_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,2,1,1,3),_VpaType_Type())
vpaType.setMaxAccess(_D)
if mibBuilder.loadTexts:vpaType.setStatus(_A)
class _VpaState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('forwarding',0),('blocking',1),(_M,2),(_G,3),('dhlBlocking',4)))
_VpaState_Type.__name__=_C
_VpaState_Object=MibTableColumn
vpaState=_VpaState_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,2,1,1,4),_VpaState_Type())
vpaState.setMaxAccess(_E)
if mibBuilder.loadTexts:vpaState.setStatus(_A)
_VpaStatus_Type=RowStatus
_VpaStatus_Object=MibTableColumn
vpaStatus=_VpaStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,2,1,1,5),_VpaStatus_Type())
vpaStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vpaStatus.setStatus(_A)
_VlanMgrVlanSet_ObjectIdentity=ObjectIdentity
vlanMgrVlanSet=_VlanMgrVlanSet_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,3))
class _VlanSetVlanCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanSetVlanCount_Type.__name__=_C
_VlanSetVlanCount_Object=MibScalar
vlanSetVlanCount=_VlanSetVlanCount_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,3,1),_VlanSetVlanCount_Type())
vlanSetVlanCount.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanSetVlanCount.setStatus(_A)
class _VlanSetDynamicVlanCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_VlanSetDynamicVlanCount_Type.__name__=_C
_VlanSetDynamicVlanCount_Object=MibScalar
vlanSetDynamicVlanCount=_VlanSetDynamicVlanCount_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,3,2),_VlanSetDynamicVlanCount_Type())
vlanSetDynamicVlanCount.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanSetDynamicVlanCount.setStatus(_A)
class _VlanSetIpRouterCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_VlanSetIpRouterCount_Type.__name__=_C
_VlanSetIpRouterCount_Object=MibScalar
vlanSetIpRouterCount=_VlanSetIpRouterCount_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,3,3),_VlanSetIpRouterCount_Type())
vlanSetIpRouterCount.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanSetIpRouterCount.setStatus(_A)
class _VlanSetVstkVlanCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_VlanSetVstkVlanCount_Type.__name__=_C
_VlanSetVstkVlanCount_Object=MibScalar
vlanSetVstkVlanCount=_VlanSetVstkVlanCount_Object((1,3,6,1,4,1,6486,801,1,2,1,3,1,1,3,4),_VlanSetVstkVlanCount_Type())
vlanSetVstkVlanCount.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanSetVstkVlanCount.setStatus(_A)
_AlcatelIND1VLANMgrMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1VLANMgrMIBConformance=_AlcatelIND1VLANMgrMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,3,1,2))
if mibBuilder.loadTexts:alcatelIND1VLANMgrMIBConformance.setStatus(_A)
_AlcatelIND1VLANMgrMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1VLANMgrMIBGroups=_AlcatelIND1VLANMgrMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,3,1,2,1))
if mibBuilder.loadTexts:alcatelIND1VLANMgrMIBGroups.setStatus(_A)
_AlcatelIND1VLANMgrMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1VLANMgrMIBCompliances=_AlcatelIND1VLANMgrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,3,1,2,2))
if mibBuilder.loadTexts:alcatelIND1VLANMgrMIBCompliances.setStatus(_A)
vlanMgrVlanGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,3,1,2,1,1))
vlanMgrVlanGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:vlanMgrVlanGroup.setStatus(_A)
vlanMgrVpaGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,3,1,2,1,2))
vlanMgrVpaGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:vlanMgrVpaGroup.setStatus(_A)
vlanMgrVlanSetGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,3,1,2,1,3))
vlanMgrVlanSetGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:vlanMgrVlanSetGroup.setStatus(_A)
alcatelIND1VLANMgrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,3,1,2,2,1))
alcatelIND1VLANMgrMIBCompliance.setObjects(*((_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:alcatelIND1VLANMgrMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1VLANMgrMIB':alcatelIND1VLANMgrMIB,'alcatelIND1VLANMgrMIBObjects':alcatelIND1VLANMgrMIBObjects,'vlanMgrVlan':vlanMgrVlan,'vlanTable':vlanTable,'vlanEntry':vlanEntry,_J:vlanNumber,_Q:vlanDescription,_R:vlanAdmStatus,_S:vlanOperStatus,_T:vlanStatus,_U:vlanRouterStatus,_V:vlanSrcLearningStatus,_W:vlanType,_X:vlanMtu,_Y:vlanAfdCfg,'vlanMgrVpa':vlanMgrVpa,'vpaTable':vpaTable,'vpaEntry':vpaEntry,_O:vpaVlanNumber,_P:vpaIfIndex,_Z:vpaType,_a:vpaState,_b:vpaStatus,'vlanMgrVlanSet':vlanMgrVlanSet,_c:vlanSetVlanCount,_d:vlanSetDynamicVlanCount,_e:vlanSetIpRouterCount,_f:vlanSetVstkVlanCount,'alcatelIND1VLANMgrMIBConformance':alcatelIND1VLANMgrMIBConformance,'alcatelIND1VLANMgrMIBGroups':alcatelIND1VLANMgrMIBGroups,_g:vlanMgrVlanGroup,_h:vlanMgrVpaGroup,_i:vlanMgrVlanSetGroup,'alcatelIND1VLANMgrMIBCompliances':alcatelIND1VLANMgrMIBCompliances,'alcatelIND1VLANMgrMIBCompliance':alcatelIND1VLANMgrMIBCompliance})