_R='alaLldpXMedLocMediaPolicyGroup'
_Q='alaLldpXMedLocMediaPolicyPortRowStatus'
_P='alaLldpXMedLocMediaPolicyRowStatus'
_O='alaLldpXMedLocMediaPolicyTagged'
_N='alaLldpXMedLocMediaPolicyUnknown'
_M='alaLldpXMedLocMediaPolicyDscp'
_L='alaLldpXMedLocMediaPolicyPriority'
_K='alaLldpXMedLocMediaPolicyVlanID'
_J='alaLldpXMedLocMediaPolicyVlanType'
_I='alaLldpXMedLocMediaPolicyAppType'
_H='alaLldpXMedLocMediaPolicyPortNumber'
_G='read-only'
_F='not-accessible'
_E='alaLldpXMedLocMediaPolicyId'
_D='Integer32'
_C='read-create'
_B='ALCATEL-IND1-LLDP-MED-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1LldpMed,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1LldpMed')
Dscp,PolicyAppType=mibBuilder.importSymbols('LLDP-EXT-MED-MIB','Dscp','PolicyAppType')
LldpPortNumber,=mibBuilder.importSymbols('LLDP-MIB','LldpPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
alcatelIND1LLDPMEDMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,58,1))
if mibBuilder.loadTexts:alcatelIND1LLDPMEDMIB.setRevisions(('2009-08-11 00:00',))
_AlcatelIND1LLDPMEDMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1LLDPMEDMIBObjects=_AlcatelIND1LLDPMEDMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,58,1,1))
if mibBuilder.loadTexts:alcatelIND1LLDPMEDMIBObjects.setStatus(_A)
_AlaLldpMedLocMediaPolicyAttributes_ObjectIdentity=ObjectIdentity
alaLldpMedLocMediaPolicyAttributes=_AlaLldpMedLocMediaPolicyAttributes_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,58,1,1,1))
_AlaLldpXMedLocMediaPolicyTable_Object=MibTable
alaLldpXMedLocMediaPolicyTable=_AlaLldpXMedLocMediaPolicyTable_Object((1,3,6,1,4,1,6486,800,1,2,1,58,1,1,1,1))
if mibBuilder.loadTexts:alaLldpXMedLocMediaPolicyTable.setStatus(_A)
_AlaLldpXMedLocMediaPolicyEntry_Object=MibTableRow
alaLldpXMedLocMediaPolicyEntry=_AlaLldpXMedLocMediaPolicyEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,58,1,1,1,1,1))
alaLldpXMedLocMediaPolicyEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:alaLldpXMedLocMediaPolicyEntry.setStatus(_A)
class _AlaLldpXMedLocMediaPolicyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlaLldpXMedLocMediaPolicyId_Type.__name__=_D
_AlaLldpXMedLocMediaPolicyId_Object=MibTableColumn
alaLldpXMedLocMediaPolicyId=_AlaLldpXMedLocMediaPolicyId_Object((1,3,6,1,4,1,6486,800,1,2,1,58,1,1,1,1,1,1),_AlaLldpXMedLocMediaPolicyId_Type())
alaLldpXMedLocMediaPolicyId.setMaxAccess(_F)
if mibBuilder.loadTexts:alaLldpXMedLocMediaPolicyId.setStatus(_A)
_AlaLldpXMedLocMediaPolicyAppType_Type=PolicyAppType
_AlaLldpXMedLocMediaPolicyAppType_Object=MibTableColumn
alaLldpXMedLocMediaPolicyAppType=_AlaLldpXMedLocMediaPolicyAppType_Object((1,3,6,1,4,1,6486,800,1,2,1,58,1,1,1,1,1,2),_AlaLldpXMedLocMediaPolicyAppType_Type())
alaLldpXMedLocMediaPolicyAppType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaLldpXMedLocMediaPolicyAppType.setStatus(_A)
class _AlaLldpXMedLocMediaPolicyVlanType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tagged',1),('priorityTagged',2),('untagged',3)))
_AlaLldpXMedLocMediaPolicyVlanType_Type.__name__=_D
_AlaLldpXMedLocMediaPolicyVlanType_Object=MibTableColumn
alaLldpXMedLocMediaPolicyVlanType=_AlaLldpXMedLocMediaPolicyVlanType_Object((1,3,6,1,4,1,6486,800,1,2,1,58,1,1,1,1,1,3),_AlaLldpXMedLocMediaPolicyVlanType_Type())
alaLldpXMedLocMediaPolicyVlanType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaLldpXMedLocMediaPolicyVlanType.setStatus(_A)
class _AlaLldpXMedLocMediaPolicyVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094),ValueRangeConstraint(4095,4095))
_AlaLldpXMedLocMediaPolicyVlanID_Type.__name__=_D
_AlaLldpXMedLocMediaPolicyVlanID_Object=MibTableColumn
alaLldpXMedLocMediaPolicyVlanID=_AlaLldpXMedLocMediaPolicyVlanID_Object((1,3,6,1,4,1,6486,800,1,2,1,58,1,1,1,1,1,4),_AlaLldpXMedLocMediaPolicyVlanID_Type())
alaLldpXMedLocMediaPolicyVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:alaLldpXMedLocMediaPolicyVlanID.setStatus(_A)
class _AlaLldpXMedLocMediaPolicyPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AlaLldpXMedLocMediaPolicyPriority_Type.__name__=_D
_AlaLldpXMedLocMediaPolicyPriority_Object=MibTableColumn
alaLldpXMedLocMediaPolicyPriority=_AlaLldpXMedLocMediaPolicyPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,58,1,1,1,1,1,5),_AlaLldpXMedLocMediaPolicyPriority_Type())
alaLldpXMedLocMediaPolicyPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:alaLldpXMedLocMediaPolicyPriority.setStatus(_A)
_AlaLldpXMedLocMediaPolicyDscp_Type=Dscp
_AlaLldpXMedLocMediaPolicyDscp_Object=MibTableColumn
alaLldpXMedLocMediaPolicyDscp=_AlaLldpXMedLocMediaPolicyDscp_Object((1,3,6,1,4,1,6486,800,1,2,1,58,1,1,1,1,1,6),_AlaLldpXMedLocMediaPolicyDscp_Type())
alaLldpXMedLocMediaPolicyDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:alaLldpXMedLocMediaPolicyDscp.setStatus(_A)
_AlaLldpXMedLocMediaPolicyUnknown_Type=TruthValue
_AlaLldpXMedLocMediaPolicyUnknown_Object=MibTableColumn
alaLldpXMedLocMediaPolicyUnknown=_AlaLldpXMedLocMediaPolicyUnknown_Object((1,3,6,1,4,1,6486,800,1,2,1,58,1,1,1,1,1,7),_AlaLldpXMedLocMediaPolicyUnknown_Type())
alaLldpXMedLocMediaPolicyUnknown.setMaxAccess(_G)
if mibBuilder.loadTexts:alaLldpXMedLocMediaPolicyUnknown.setStatus(_A)
_AlaLldpXMedLocMediaPolicyTagged_Type=TruthValue
_AlaLldpXMedLocMediaPolicyTagged_Object=MibTableColumn
alaLldpXMedLocMediaPolicyTagged=_AlaLldpXMedLocMediaPolicyTagged_Object((1,3,6,1,4,1,6486,800,1,2,1,58,1,1,1,1,1,8),_AlaLldpXMedLocMediaPolicyTagged_Type())
alaLldpXMedLocMediaPolicyTagged.setMaxAccess(_G)
if mibBuilder.loadTexts:alaLldpXMedLocMediaPolicyTagged.setStatus(_A)
_AlaLldpXMedLocMediaPolicyRowStatus_Type=RowStatus
_AlaLldpXMedLocMediaPolicyRowStatus_Object=MibTableColumn
alaLldpXMedLocMediaPolicyRowStatus=_AlaLldpXMedLocMediaPolicyRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,58,1,1,1,1,1,9),_AlaLldpXMedLocMediaPolicyRowStatus_Type())
alaLldpXMedLocMediaPolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaLldpXMedLocMediaPolicyRowStatus.setStatus(_A)
_AlaLldpXMedLocMediaPolicyPortTable_Object=MibTable
alaLldpXMedLocMediaPolicyPortTable=_AlaLldpXMedLocMediaPolicyPortTable_Object((1,3,6,1,4,1,6486,800,1,2,1,58,1,1,1,2))
if mibBuilder.loadTexts:alaLldpXMedLocMediaPolicyPortTable.setStatus(_A)
_AlaLldpXMedLocMediaPolicyPortEntry_Object=MibTableRow
alaLldpXMedLocMediaPolicyPortEntry=_AlaLldpXMedLocMediaPolicyPortEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,58,1,1,1,2,1))
alaLldpXMedLocMediaPolicyPortEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:alaLldpXMedLocMediaPolicyPortEntry.setStatus(_A)
_AlaLldpXMedLocMediaPolicyPortNumber_Type=LldpPortNumber
_AlaLldpXMedLocMediaPolicyPortNumber_Object=MibTableColumn
alaLldpXMedLocMediaPolicyPortNumber=_AlaLldpXMedLocMediaPolicyPortNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,58,1,1,1,2,1,1),_AlaLldpXMedLocMediaPolicyPortNumber_Type())
alaLldpXMedLocMediaPolicyPortNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:alaLldpXMedLocMediaPolicyPortNumber.setStatus(_A)
_AlaLldpXMedLocMediaPolicyPortRowStatus_Type=RowStatus
_AlaLldpXMedLocMediaPolicyPortRowStatus_Object=MibTableColumn
alaLldpXMedLocMediaPolicyPortRowStatus=_AlaLldpXMedLocMediaPolicyPortRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,58,1,1,1,2,1,2),_AlaLldpXMedLocMediaPolicyPortRowStatus_Type())
alaLldpXMedLocMediaPolicyPortRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaLldpXMedLocMediaPolicyPortRowStatus.setStatus(_A)
_AlcatelIND1LLDPMEDMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1LLDPMEDMIBConformance=_AlcatelIND1LLDPMEDMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,58,1,2))
_AlcatelIND1LLDPMEDMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1LLDPMEDMIBCompliances=_AlcatelIND1LLDPMEDMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,58,1,2,1))
_AlcatelIND1LLDPMEDMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1LLDPMEDMIBGroups=_AlcatelIND1LLDPMEDMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,58,1,2,2))
alaLldpXMedLocMediaPolicyGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,58,1,2,2,1))
alaLldpXMedLocMediaPolicyGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:alaLldpXMedLocMediaPolicyGroup.setStatus(_A)
alcatelIND1LLDPMEDMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,58,1,2,1,1))
alcatelIND1LLDPMEDMIBCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:alcatelIND1LLDPMEDMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1LLDPMEDMIB':alcatelIND1LLDPMEDMIB,'alcatelIND1LLDPMEDMIBObjects':alcatelIND1LLDPMEDMIBObjects,'alaLldpMedLocMediaPolicyAttributes':alaLldpMedLocMediaPolicyAttributes,'alaLldpXMedLocMediaPolicyTable':alaLldpXMedLocMediaPolicyTable,'alaLldpXMedLocMediaPolicyEntry':alaLldpXMedLocMediaPolicyEntry,_E:alaLldpXMedLocMediaPolicyId,_I:alaLldpXMedLocMediaPolicyAppType,_J:alaLldpXMedLocMediaPolicyVlanType,_K:alaLldpXMedLocMediaPolicyVlanID,_L:alaLldpXMedLocMediaPolicyPriority,_M:alaLldpXMedLocMediaPolicyDscp,_N:alaLldpXMedLocMediaPolicyUnknown,_O:alaLldpXMedLocMediaPolicyTagged,_P:alaLldpXMedLocMediaPolicyRowStatus,'alaLldpXMedLocMediaPolicyPortTable':alaLldpXMedLocMediaPolicyPortTable,'alaLldpXMedLocMediaPolicyPortEntry':alaLldpXMedLocMediaPolicyPortEntry,_H:alaLldpXMedLocMediaPolicyPortNumber,_Q:alaLldpXMedLocMediaPolicyPortRowStatus,'alcatelIND1LLDPMEDMIBConformance':alcatelIND1LLDPMEDMIBConformance,'alcatelIND1LLDPMEDMIBCompliances':alcatelIND1LLDPMEDMIBCompliances,'alcatelIND1LLDPMEDMIBCompliance':alcatelIND1LLDPMEDMIBCompliance,'alcatelIND1LLDPMEDMIBGroups':alcatelIND1LLDPMEDMIBGroups,_R:alaLldpXMedLocMediaPolicyGroup})