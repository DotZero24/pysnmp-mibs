_U='vlanStackingSvlanPortGroup'
_T='vlanStackingPortGroup'
_S='alaVstkSvlanPortRowStatus'
_R='alaVstkSvlanPortMode'
_Q='alaVstkPortLegacyStpBpdu'
_P='alaVstkPortRowStatus'
_O='alaVstkPortDefaultSvlan'
_N='alaVstkPortLookupMiss'
_M='alaVstkPortAcceptFrameType'
_L='alaVstkPortBpduTreatment'
_K='alaVstkPortVendorTpid'
_J='alaVstkPortType'
_I='alaVstkSvlanPortCvlanNumber'
_H='alaVstkSvlanPortPortNumber'
_G='alaVstkSvlanPortSvlanNumber'
_F='alaVstkPortNumber'
_E='read-only'
_D='read-create'
_C='Integer32'
_B='ALCATEL-IND1-VLAN-STACKING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1VlanStackingMgt,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1VlanStackingMgt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1VLANStackingMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,37,1))
_AlcatelIND1VLANStackingMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1VLANStackingMIBObjects=_AlcatelIND1VLANStackingMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,37,1,1))
if mibBuilder.loadTexts:alcatelIND1VLANStackingMIBObjects.setStatus(_A)
_AlaVlanStackingPort_ObjectIdentity=ObjectIdentity
alaVlanStackingPort=_AlaVlanStackingPort_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,1))
_AlaVstkPortTable_Object=MibTable
alaVstkPortTable=_AlaVstkPortTable_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,1,1))
if mibBuilder.loadTexts:alaVstkPortTable.setStatus(_A)
_AlaVstkPortEntry_Object=MibTableRow
alaVstkPortEntry=_AlaVstkPortEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,1,1,1))
alaVstkPortEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:alaVstkPortEntry.setStatus(_A)
_AlaVstkPortNumber_Type=InterfaceIndex
_AlaVstkPortNumber_Object=MibTableColumn
alaVstkPortNumber=_AlaVstkPortNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,1,1,1,1),_AlaVstkPortNumber_Type())
alaVstkPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVstkPortNumber.setStatus(_A)
class _AlaVstkPortType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('userCustomer',1),('userProvider',2),('network',3)))
_AlaVstkPortType_Type.__name__=_C
_AlaVstkPortType_Object=MibTableColumn
alaVstkPortType=_AlaVstkPortType_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,1,1,1,2),_AlaVstkPortType_Type())
alaVstkPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVstkPortType.setStatus(_A)
class _AlaVstkPortVendorTpid_Type(Integer32):defaultValue=34984
_AlaVstkPortVendorTpid_Type.__name__=_C
_AlaVstkPortVendorTpid_Object=MibTableColumn
alaVstkPortVendorTpid=_AlaVstkPortVendorTpid_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,1,1,1,3),_AlaVstkPortVendorTpid_Type())
alaVstkPortVendorTpid.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVstkPortVendorTpid.setStatus(_A)
class _AlaVstkPortBpduTreatment_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('flooded',1),('dropped',2)))
_AlaVstkPortBpduTreatment_Type.__name__=_C
_AlaVstkPortBpduTreatment_Object=MibTableColumn
alaVstkPortBpduTreatment=_AlaVstkPortBpduTreatment_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,1,1,1,4),_AlaVstkPortBpduTreatment_Type())
alaVstkPortBpduTreatment.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVstkPortBpduTreatment.setStatus(_A)
class _AlaVstkPortAcceptFrameType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tagged',1),('untagged',2),('all',3)))
_AlaVstkPortAcceptFrameType_Type.__name__=_C
_AlaVstkPortAcceptFrameType_Object=MibTableColumn
alaVstkPortAcceptFrameType=_AlaVstkPortAcceptFrameType_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,1,1,1,5),_AlaVstkPortAcceptFrameType_Type())
alaVstkPortAcceptFrameType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVstkPortAcceptFrameType.setStatus(_A)
class _AlaVstkPortLookupMiss_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('drop',1),('default',2)))
_AlaVstkPortLookupMiss_Type.__name__=_C
_AlaVstkPortLookupMiss_Object=MibTableColumn
alaVstkPortLookupMiss=_AlaVstkPortLookupMiss_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,1,1,1,6),_AlaVstkPortLookupMiss_Type())
alaVstkPortLookupMiss.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVstkPortLookupMiss.setStatus(_A)
class _AlaVstkPortDefaultSvlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AlaVstkPortDefaultSvlan_Type.__name__=_C
_AlaVstkPortDefaultSvlan_Object=MibTableColumn
alaVstkPortDefaultSvlan=_AlaVstkPortDefaultSvlan_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,1,1,1,7),_AlaVstkPortDefaultSvlan_Type())
alaVstkPortDefaultSvlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVstkPortDefaultSvlan.setStatus(_A)
_AlaVstkPortRowStatus_Type=RowStatus
_AlaVstkPortRowStatus_Object=MibTableColumn
alaVstkPortRowStatus=_AlaVstkPortRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,1,1,1,8),_AlaVstkPortRowStatus_Type())
alaVstkPortRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVstkPortRowStatus.setStatus(_A)
class _AlaVstkPortLegacyStpBpdu_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AlaVstkPortLegacyStpBpdu_Type.__name__=_C
_AlaVstkPortLegacyStpBpdu_Object=MibTableColumn
alaVstkPortLegacyStpBpdu=_AlaVstkPortLegacyStpBpdu_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,1,1,1,9),_AlaVstkPortLegacyStpBpdu_Type())
alaVstkPortLegacyStpBpdu.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVstkPortLegacyStpBpdu.setStatus(_A)
_AlaVlanStackingSvlanPort_ObjectIdentity=ObjectIdentity
alaVlanStackingSvlanPort=_AlaVlanStackingSvlanPort_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,2))
_AlaVstkSvlanPortTable_Object=MibTable
alaVstkSvlanPortTable=_AlaVstkSvlanPortTable_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,2,1))
if mibBuilder.loadTexts:alaVstkSvlanPortTable.setStatus(_A)
_AlaVstkSvlanPortEntry_Object=MibTableRow
alaVstkSvlanPortEntry=_AlaVstkSvlanPortEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,2,1,1))
alaVstkSvlanPortEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:alaVstkSvlanPortEntry.setStatus(_A)
class _AlaVstkSvlanPortSvlanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AlaVstkSvlanPortSvlanNumber_Type.__name__=_C
_AlaVstkSvlanPortSvlanNumber_Object=MibTableColumn
alaVstkSvlanPortSvlanNumber=_AlaVstkSvlanPortSvlanNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,2,1,1,1),_AlaVstkSvlanPortSvlanNumber_Type())
alaVstkSvlanPortSvlanNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVstkSvlanPortSvlanNumber.setStatus(_A)
_AlaVstkSvlanPortPortNumber_Type=InterfaceIndex
_AlaVstkSvlanPortPortNumber_Object=MibTableColumn
alaVstkSvlanPortPortNumber=_AlaVstkSvlanPortPortNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,2,1,1,2),_AlaVstkSvlanPortPortNumber_Type())
alaVstkSvlanPortPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVstkSvlanPortPortNumber.setStatus(_A)
class _AlaVstkSvlanPortCvlanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AlaVstkSvlanPortCvlanNumber_Type.__name__=_C
_AlaVstkSvlanPortCvlanNumber_Object=MibTableColumn
alaVstkSvlanPortCvlanNumber=_AlaVstkSvlanPortCvlanNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,2,1,1,3),_AlaVstkSvlanPortCvlanNumber_Type())
alaVstkSvlanPortCvlanNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVstkSvlanPortCvlanNumber.setStatus(_A)
class _AlaVstkSvlanPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('doubleTag',1),('translate',2)))
_AlaVstkSvlanPortMode_Type.__name__=_C
_AlaVstkSvlanPortMode_Object=MibTableColumn
alaVstkSvlanPortMode=_AlaVstkSvlanPortMode_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,2,1,1,4),_AlaVstkSvlanPortMode_Type())
alaVstkSvlanPortMode.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVstkSvlanPortMode.setStatus(_A)
_AlaVstkSvlanPortRowStatus_Type=RowStatus
_AlaVstkSvlanPortRowStatus_Object=MibTableColumn
alaVstkSvlanPortRowStatus=_AlaVstkSvlanPortRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,37,1,1,2,1,1,5),_AlaVstkSvlanPortRowStatus_Type())
alaVstkSvlanPortRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVstkSvlanPortRowStatus.setStatus(_A)
_AlcatelIND1VLANStackingMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1VLANStackingMIBConformance=_AlcatelIND1VLANStackingMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,37,1,2))
if mibBuilder.loadTexts:alcatelIND1VLANStackingMIBConformance.setStatus(_A)
_AlcatelIND1VLANStackingMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1VLANStackingMIBGroups=_AlcatelIND1VLANStackingMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,37,1,2,1))
if mibBuilder.loadTexts:alcatelIND1VLANStackingMIBGroups.setStatus(_A)
_AlcatelIND1VLANStackingMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1VLANStackingMIBCompliances=_AlcatelIND1VLANStackingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,37,1,2,2))
if mibBuilder.loadTexts:alcatelIND1VLANStackingMIBCompliances.setStatus(_A)
vlanStackingPortGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,37,1,2,1,1))
vlanStackingPortGroup.setObjects(*((_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:vlanStackingPortGroup.setStatus(_A)
vlanStackingSvlanPortGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,37,1,2,1,2))
vlanStackingSvlanPortGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:vlanStackingSvlanPortGroup.setStatus(_A)
alcatelIND1VLANStackingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,37,1,2,2,1))
alcatelIND1VLANStackingMIBCompliance.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:alcatelIND1VLANStackingMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1VLANStackingMIB':alcatelIND1VLANStackingMIB,'alcatelIND1VLANStackingMIBObjects':alcatelIND1VLANStackingMIBObjects,'alaVlanStackingPort':alaVlanStackingPort,'alaVstkPortTable':alaVstkPortTable,'alaVstkPortEntry':alaVstkPortEntry,_F:alaVstkPortNumber,_J:alaVstkPortType,_K:alaVstkPortVendorTpid,_L:alaVstkPortBpduTreatment,_M:alaVstkPortAcceptFrameType,_N:alaVstkPortLookupMiss,_O:alaVstkPortDefaultSvlan,_P:alaVstkPortRowStatus,_Q:alaVstkPortLegacyStpBpdu,'alaVlanStackingSvlanPort':alaVlanStackingSvlanPort,'alaVstkSvlanPortTable':alaVstkSvlanPortTable,'alaVstkSvlanPortEntry':alaVstkSvlanPortEntry,_G:alaVstkSvlanPortSvlanNumber,_H:alaVstkSvlanPortPortNumber,_I:alaVstkSvlanPortCvlanNumber,_R:alaVstkSvlanPortMode,_S:alaVstkSvlanPortRowStatus,'alcatelIND1VLANStackingMIBConformance':alcatelIND1VLANStackingMIBConformance,'alcatelIND1VLANStackingMIBGroups':alcatelIND1VLANStackingMIBGroups,_T:vlanStackingPortGroup,_U:vlanStackingSvlanPortGroup,'alcatelIND1VLANStackingMIBCompliances':alcatelIND1VLANStackingMIBCompliances,'alcatelIND1VLANStackingMIBCompliance':alcatelIND1VLANStackingMIBCompliance})