_S='cvtPortTranslationGroup'
_R='cvtGlobalTranslationGroup'
_Q='cvtPortTranslationStatus'
_P='cvtPortTranslatedVlan'
_O='cvtPortTranslationMax'
_N='cvtPortTranslationEnabled'
_M='cvtGlobalTranslationStatus'
_L='cvtGlobalTranslationEffective'
_K='cvtGlobalTranslatedVlan'
_J='cvtGlobalTranslationMax'
_I='cvtPortOriginalVlan'
_H='not-accessible'
_G='cvtGlobalOriginalVlan'
_F='read-only'
_E='ifIndex'
_D='IF-MIB'
_C='read-create'
_B='CISCO-VLAN-TRANSLATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_D,_E)
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
ciscoVlanTranslationMIB=ModuleIdentity((1,3,6,1,4,1,9,9,411))
if mibBuilder.loadTexts:ciscoVlanTranslationMIB.setRevisions(('2004-06-01 00:00',))
_CiscoVlanTranslationMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoVlanTranslationMIBNotifs=_CiscoVlanTranslationMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,411,0))
_CiscoVlanTranslationMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVlanTranslationMIBObjects=_CiscoVlanTranslationMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,411,1))
_CvtGlobalTranslation_ObjectIdentity=ObjectIdentity
cvtGlobalTranslation=_CvtGlobalTranslation_ObjectIdentity((1,3,6,1,4,1,9,9,411,1,1))
_CvtGlobalTranslationMax_Type=Unsigned32
_CvtGlobalTranslationMax_Object=MibScalar
cvtGlobalTranslationMax=_CvtGlobalTranslationMax_Object((1,3,6,1,4,1,9,9,411,1,1,1),_CvtGlobalTranslationMax_Type())
cvtGlobalTranslationMax.setMaxAccess(_F)
if mibBuilder.loadTexts:cvtGlobalTranslationMax.setStatus(_A)
_CvtGlobalTranslationTable_Object=MibTable
cvtGlobalTranslationTable=_CvtGlobalTranslationTable_Object((1,3,6,1,4,1,9,9,411,1,1,2))
if mibBuilder.loadTexts:cvtGlobalTranslationTable.setStatus(_A)
_CvtGlobalTranslationEntry_Object=MibTableRow
cvtGlobalTranslationEntry=_CvtGlobalTranslationEntry_Object((1,3,6,1,4,1,9,9,411,1,1,2,1))
cvtGlobalTranslationEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:cvtGlobalTranslationEntry.setStatus(_A)
_CvtGlobalOriginalVlan_Type=VlanIndex
_CvtGlobalOriginalVlan_Object=MibTableColumn
cvtGlobalOriginalVlan=_CvtGlobalOriginalVlan_Object((1,3,6,1,4,1,9,9,411,1,1,2,1,1),_CvtGlobalOriginalVlan_Type())
cvtGlobalOriginalVlan.setMaxAccess(_H)
if mibBuilder.loadTexts:cvtGlobalOriginalVlan.setStatus(_A)
_CvtGlobalTranslatedVlan_Type=VlanIndex
_CvtGlobalTranslatedVlan_Object=MibTableColumn
cvtGlobalTranslatedVlan=_CvtGlobalTranslatedVlan_Object((1,3,6,1,4,1,9,9,411,1,1,2,1,2),_CvtGlobalTranslatedVlan_Type())
cvtGlobalTranslatedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cvtGlobalTranslatedVlan.setStatus(_A)
_CvtGlobalTranslationEffective_Type=TruthValue
_CvtGlobalTranslationEffective_Object=MibTableColumn
cvtGlobalTranslationEffective=_CvtGlobalTranslationEffective_Object((1,3,6,1,4,1,9,9,411,1,1,2,1,3),_CvtGlobalTranslationEffective_Type())
cvtGlobalTranslationEffective.setMaxAccess(_F)
if mibBuilder.loadTexts:cvtGlobalTranslationEffective.setStatus(_A)
_CvtGlobalTranslationStatus_Type=RowStatus
_CvtGlobalTranslationStatus_Object=MibTableColumn
cvtGlobalTranslationStatus=_CvtGlobalTranslationStatus_Object((1,3,6,1,4,1,9,9,411,1,1,2,1,4),_CvtGlobalTranslationStatus_Type())
cvtGlobalTranslationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvtGlobalTranslationStatus.setStatus(_A)
_CvtPortBasedTranslation_ObjectIdentity=ObjectIdentity
cvtPortBasedTranslation=_CvtPortBasedTranslation_ObjectIdentity((1,3,6,1,4,1,9,9,411,1,2))
_CvtPortConfigTable_Object=MibTable
cvtPortConfigTable=_CvtPortConfigTable_Object((1,3,6,1,4,1,9,9,411,1,2,1))
if mibBuilder.loadTexts:cvtPortConfigTable.setStatus(_A)
_CvtPortConfigEntry_Object=MibTableRow
cvtPortConfigEntry=_CvtPortConfigEntry_Object((1,3,6,1,4,1,9,9,411,1,2,1,1))
cvtPortConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cvtPortConfigEntry.setStatus(_A)
_CvtPortTranslationEnabled_Type=TruthValue
_CvtPortTranslationEnabled_Object=MibTableColumn
cvtPortTranslationEnabled=_CvtPortTranslationEnabled_Object((1,3,6,1,4,1,9,9,411,1,2,1,1,1),_CvtPortTranslationEnabled_Type())
cvtPortTranslationEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:cvtPortTranslationEnabled.setStatus(_A)
_CvtPortTranslationMax_Type=Unsigned32
_CvtPortTranslationMax_Object=MibTableColumn
cvtPortTranslationMax=_CvtPortTranslationMax_Object((1,3,6,1,4,1,9,9,411,1,2,1,1,2),_CvtPortTranslationMax_Type())
cvtPortTranslationMax.setMaxAccess(_F)
if mibBuilder.loadTexts:cvtPortTranslationMax.setStatus(_A)
_CvtPortTranslationTable_Object=MibTable
cvtPortTranslationTable=_CvtPortTranslationTable_Object((1,3,6,1,4,1,9,9,411,1,2,2))
if mibBuilder.loadTexts:cvtPortTranslationTable.setStatus(_A)
_CvtPortTranslationEntry_Object=MibTableRow
cvtPortTranslationEntry=_CvtPortTranslationEntry_Object((1,3,6,1,4,1,9,9,411,1,2,2,1))
cvtPortTranslationEntry.setIndexNames((0,_D,_E),(0,_B,_I))
if mibBuilder.loadTexts:cvtPortTranslationEntry.setStatus(_A)
_CvtPortOriginalVlan_Type=VlanIndex
_CvtPortOriginalVlan_Object=MibTableColumn
cvtPortOriginalVlan=_CvtPortOriginalVlan_Object((1,3,6,1,4,1,9,9,411,1,2,2,1,1),_CvtPortOriginalVlan_Type())
cvtPortOriginalVlan.setMaxAccess(_H)
if mibBuilder.loadTexts:cvtPortOriginalVlan.setStatus(_A)
_CvtPortTranslatedVlan_Type=VlanIndex
_CvtPortTranslatedVlan_Object=MibTableColumn
cvtPortTranslatedVlan=_CvtPortTranslatedVlan_Object((1,3,6,1,4,1,9,9,411,1,2,2,1,2),_CvtPortTranslatedVlan_Type())
cvtPortTranslatedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cvtPortTranslatedVlan.setStatus(_A)
_CvtPortTranslationStatus_Type=RowStatus
_CvtPortTranslationStatus_Object=MibTableColumn
cvtPortTranslationStatus=_CvtPortTranslationStatus_Object((1,3,6,1,4,1,9,9,411,1,2,2,1,3),_CvtPortTranslationStatus_Type())
cvtPortTranslationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvtPortTranslationStatus.setStatus(_A)
_CiscoVlanTranslationMIBConform_ObjectIdentity=ObjectIdentity
ciscoVlanTranslationMIBConform=_CiscoVlanTranslationMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,411,2))
_CvtMIBCompliances_ObjectIdentity=ObjectIdentity
cvtMIBCompliances=_CvtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,411,2,1))
_CvtMIBGroups_ObjectIdentity=ObjectIdentity
cvtMIBGroups=_CvtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,411,2,2))
cvtGlobalTranslationGroup=ObjectGroup((1,3,6,1,4,1,9,9,411,2,2,1))
cvtGlobalTranslationGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:cvtGlobalTranslationGroup.setStatus(_A)
cvtPortTranslationGroup=ObjectGroup((1,3,6,1,4,1,9,9,411,2,2,2))
cvtPortTranslationGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:cvtPortTranslationGroup.setStatus(_A)
cvtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,411,2,1,1))
cvtMIBCompliance.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:cvtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoVlanTranslationMIB':ciscoVlanTranslationMIB,'ciscoVlanTranslationMIBNotifs':ciscoVlanTranslationMIBNotifs,'ciscoVlanTranslationMIBObjects':ciscoVlanTranslationMIBObjects,'cvtGlobalTranslation':cvtGlobalTranslation,_J:cvtGlobalTranslationMax,'cvtGlobalTranslationTable':cvtGlobalTranslationTable,'cvtGlobalTranslationEntry':cvtGlobalTranslationEntry,_G:cvtGlobalOriginalVlan,_K:cvtGlobalTranslatedVlan,_L:cvtGlobalTranslationEffective,_M:cvtGlobalTranslationStatus,'cvtPortBasedTranslation':cvtPortBasedTranslation,'cvtPortConfigTable':cvtPortConfigTable,'cvtPortConfigEntry':cvtPortConfigEntry,_N:cvtPortTranslationEnabled,_O:cvtPortTranslationMax,'cvtPortTranslationTable':cvtPortTranslationTable,'cvtPortTranslationEntry':cvtPortTranslationEntry,_I:cvtPortOriginalVlan,_P:cvtPortTranslatedVlan,_Q:cvtPortTranslationStatus,'ciscoVlanTranslationMIBConform':ciscoVlanTranslationMIBConform,'cvtMIBCompliances':cvtMIBCompliances,'cvtMIBCompliance':cvtMIBCompliance,'cvtMIBGroups':cvtMIBGroups,_R:cvtGlobalTranslationGroup,_S:cvtPortTranslationGroup})