_T='ciscoQinqVlanTranslationGroup'
_S='ciscoQinqVlanTerminationGroup'
_R='cqvTranslationRowStatus'
_Q='cqvTranslationCosPBits'
_P='cqvTranslationType'
_O='cqvTranslationTrunkCeVlanId'
_N='cqvTranslationTrunkPeVlanId'
_M='cqvTerminationRowStatus'
_L='cqvTerminationPeEncap'
_K='cqvTranslationInternalCeVlanId'
_J='cqvTranslationInternalPeVlanId'
_I='cqvTerminationCeVlanId'
_H='cqvTerminationPeVlanId'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='not-accessible'
_C='read-create'
_B='CISCO-QINQ-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoQinqVlanMIB=ModuleIdentity((1,3,6,1,4,1,9,9,445))
if mibBuilder.loadTexts:ciscoQinqVlanMIB.setRevisions(('2004-11-29 00:00',))
class CqvVlanIdOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
class CqvEncapsulationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('isl',1),('dot1Q',2)))
_CiscoQinqVlanMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoQinqVlanMIBNotifs=_CiscoQinqVlanMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,445,0))
_CiscoQinqVlanMIBObjects_ObjectIdentity=ObjectIdentity
ciscoQinqVlanMIBObjects=_CiscoQinqVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,445,1))
_CqvTermination_ObjectIdentity=ObjectIdentity
cqvTermination=_CqvTermination_ObjectIdentity((1,3,6,1,4,1,9,9,445,1,1))
_CqvTerminationTable_Object=MibTable
cqvTerminationTable=_CqvTerminationTable_Object((1,3,6,1,4,1,9,9,445,1,1,1))
if mibBuilder.loadTexts:cqvTerminationTable.setStatus(_A)
_CqvTerminationEntry_Object=MibTableRow
cqvTerminationEntry=_CqvTerminationEntry_Object((1,3,6,1,4,1,9,9,445,1,1,1,1))
cqvTerminationEntry.setIndexNames((0,_E,_F),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:cqvTerminationEntry.setStatus(_A)
_CqvTerminationPeVlanId_Type=VlanId
_CqvTerminationPeVlanId_Object=MibTableColumn
cqvTerminationPeVlanId=_CqvTerminationPeVlanId_Object((1,3,6,1,4,1,9,9,445,1,1,1,1,1),_CqvTerminationPeVlanId_Type())
cqvTerminationPeVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:cqvTerminationPeVlanId.setStatus(_A)
_CqvTerminationCeVlanId_Type=VlanId
_CqvTerminationCeVlanId_Object=MibTableColumn
cqvTerminationCeVlanId=_CqvTerminationCeVlanId_Object((1,3,6,1,4,1,9,9,445,1,1,1,1,2),_CqvTerminationCeVlanId_Type())
cqvTerminationCeVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:cqvTerminationCeVlanId.setStatus(_A)
_CqvTerminationPeEncap_Type=CqvEncapsulationType
_CqvTerminationPeEncap_Object=MibTableColumn
cqvTerminationPeEncap=_CqvTerminationPeEncap_Object((1,3,6,1,4,1,9,9,445,1,1,1,1,3),_CqvTerminationPeEncap_Type())
cqvTerminationPeEncap.setMaxAccess(_C)
if mibBuilder.loadTexts:cqvTerminationPeEncap.setStatus(_A)
_CqvTerminationRowStatus_Type=RowStatus
_CqvTerminationRowStatus_Object=MibTableColumn
cqvTerminationRowStatus=_CqvTerminationRowStatus_Object((1,3,6,1,4,1,9,9,445,1,1,1,1,4),_CqvTerminationRowStatus_Type())
cqvTerminationRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cqvTerminationRowStatus.setStatus(_A)
_CqvTranslation_ObjectIdentity=ObjectIdentity
cqvTranslation=_CqvTranslation_ObjectIdentity((1,3,6,1,4,1,9,9,445,1,2))
_CqvTranslationTable_Object=MibTable
cqvTranslationTable=_CqvTranslationTable_Object((1,3,6,1,4,1,9,9,445,1,2,1))
if mibBuilder.loadTexts:cqvTranslationTable.setStatus(_A)
_CqvTranslationEntry_Object=MibTableRow
cqvTranslationEntry=_CqvTranslationEntry_Object((1,3,6,1,4,1,9,9,445,1,2,1,1))
cqvTranslationEntry.setIndexNames((0,_E,_F),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:cqvTranslationEntry.setStatus(_A)
_CqvTranslationInternalPeVlanId_Type=CqvVlanIdOrZero
_CqvTranslationInternalPeVlanId_Object=MibTableColumn
cqvTranslationInternalPeVlanId=_CqvTranslationInternalPeVlanId_Object((1,3,6,1,4,1,9,9,445,1,2,1,1,1),_CqvTranslationInternalPeVlanId_Type())
cqvTranslationInternalPeVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:cqvTranslationInternalPeVlanId.setStatus(_A)
_CqvTranslationInternalCeVlanId_Type=CqvVlanIdOrZero
_CqvTranslationInternalCeVlanId_Object=MibTableColumn
cqvTranslationInternalCeVlanId=_CqvTranslationInternalCeVlanId_Object((1,3,6,1,4,1,9,9,445,1,2,1,1,2),_CqvTranslationInternalCeVlanId_Type())
cqvTranslationInternalCeVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:cqvTranslationInternalCeVlanId.setStatus(_A)
_CqvTranslationTrunkPeVlanId_Type=CqvVlanIdOrZero
_CqvTranslationTrunkPeVlanId_Object=MibTableColumn
cqvTranslationTrunkPeVlanId=_CqvTranslationTrunkPeVlanId_Object((1,3,6,1,4,1,9,9,445,1,2,1,1,3),_CqvTranslationTrunkPeVlanId_Type())
cqvTranslationTrunkPeVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:cqvTranslationTrunkPeVlanId.setStatus(_A)
_CqvTranslationTrunkCeVlanId_Type=CqvVlanIdOrZero
_CqvTranslationTrunkCeVlanId_Object=MibTableColumn
cqvTranslationTrunkCeVlanId=_CqvTranslationTrunkCeVlanId_Object((1,3,6,1,4,1,9,9,445,1,2,1,1,4),_CqvTranslationTrunkCeVlanId_Type())
cqvTranslationTrunkCeVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:cqvTranslationTrunkCeVlanId.setStatus(_A)
class _CqvTranslationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('doubleToSingle',1),('doubleToDouble',2),('doubleToDoubleOutOfRange',3)))
_CqvTranslationType_Type.__name__=_G
_CqvTranslationType_Object=MibTableColumn
cqvTranslationType=_CqvTranslationType_Object((1,3,6,1,4,1,9,9,445,1,2,1,1,5),_CqvTranslationType_Type())
cqvTranslationType.setMaxAccess(_C)
if mibBuilder.loadTexts:cqvTranslationType.setStatus(_A)
class _CqvTranslationCosPBits_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('copyFromOuterTag',1),('copyFromInnerTag',2)))
_CqvTranslationCosPBits_Type.__name__=_G
_CqvTranslationCosPBits_Object=MibTableColumn
cqvTranslationCosPBits=_CqvTranslationCosPBits_Object((1,3,6,1,4,1,9,9,445,1,2,1,1,6),_CqvTranslationCosPBits_Type())
cqvTranslationCosPBits.setMaxAccess(_C)
if mibBuilder.loadTexts:cqvTranslationCosPBits.setStatus(_A)
_CqvTranslationRowStatus_Type=RowStatus
_CqvTranslationRowStatus_Object=MibTableColumn
cqvTranslationRowStatus=_CqvTranslationRowStatus_Object((1,3,6,1,4,1,9,9,445,1,2,1,1,7),_CqvTranslationRowStatus_Type())
cqvTranslationRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cqvTranslationRowStatus.setStatus(_A)
_CiscoQinqVlanMIBConform_ObjectIdentity=ObjectIdentity
ciscoQinqVlanMIBConform=_CiscoQinqVlanMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,445,2))
_CiscoQinqVlanMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoQinqVlanMIBCompliances=_CiscoQinqVlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,445,2,1))
_CiscoQinqVlanMIBGroups_ObjectIdentity=ObjectIdentity
ciscoQinqVlanMIBGroups=_CiscoQinqVlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,445,2,2))
ciscoQinqVlanTerminationGroup=ObjectGroup((1,3,6,1,4,1,9,9,445,2,2,1))
ciscoQinqVlanTerminationGroup.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ciscoQinqVlanTerminationGroup.setStatus(_A)
ciscoQinqVlanTranslationGroup=ObjectGroup((1,3,6,1,4,1,9,9,445,2,2,2))
ciscoQinqVlanTranslationGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ciscoQinqVlanTranslationGroup.setStatus(_A)
ciscoQinQVlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,445,2,1,1))
ciscoQinQVlanMIBCompliance.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciscoQinQVlanMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CqvVlanIdOrZero':CqvVlanIdOrZero,'CqvEncapsulationType':CqvEncapsulationType,'ciscoQinqVlanMIB':ciscoQinqVlanMIB,'ciscoQinqVlanMIBNotifs':ciscoQinqVlanMIBNotifs,'ciscoQinqVlanMIBObjects':ciscoQinqVlanMIBObjects,'cqvTermination':cqvTermination,'cqvTerminationTable':cqvTerminationTable,'cqvTerminationEntry':cqvTerminationEntry,_H:cqvTerminationPeVlanId,_I:cqvTerminationCeVlanId,_L:cqvTerminationPeEncap,_M:cqvTerminationRowStatus,'cqvTranslation':cqvTranslation,'cqvTranslationTable':cqvTranslationTable,'cqvTranslationEntry':cqvTranslationEntry,_J:cqvTranslationInternalPeVlanId,_K:cqvTranslationInternalCeVlanId,_N:cqvTranslationTrunkPeVlanId,_O:cqvTranslationTrunkCeVlanId,_P:cqvTranslationType,_Q:cqvTranslationCosPBits,_R:cqvTranslationRowStatus,'ciscoQinqVlanMIBConform':ciscoQinqVlanMIBConform,'ciscoQinqVlanMIBCompliances':ciscoQinqVlanMIBCompliances,'ciscoQinQVlanMIBCompliance':ciscoQinQVlanMIBCompliance,'ciscoQinqVlanMIBGroups':ciscoQinqVlanMIBGroups,_S:ciscoQinqVlanTerminationGroup,_T:ciscoQinqVlanTranslationGroup})