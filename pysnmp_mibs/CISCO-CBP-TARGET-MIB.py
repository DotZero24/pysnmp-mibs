_R='ccbptTargetProvisioningGroup'
_Q='ccbptPolicyAttachTime'
_P='ccbptTargetTableLastChange'
_O='ccbptPolicyInstance'
_N='ccbptPolicyMap'
_M='ccbptTargetStorageType'
_L='ccbptTargetStatus'
_K='ccbptPolicyIdNext'
_J='ccbptPolicyId'
_I='ccbptPolicySourceType'
_H='ccbptTargetDir'
_G='ccbptTargetId'
_F='ccbptTargetType'
_E='read-create'
_D='read-only'
_C='not-accessible'
_B='CISCO-CBP-TARGET-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CcbptPolicyIdentifier,CcbptPolicyIdentifierOrZero,CcbptPolicySourceType,CcbptTargetDirection,CcbptTargetId,CcbptTargetType=mibBuilder.importSymbols('CISCO-CBP-TARGET-TC-MIB','CcbptPolicyIdentifier','CcbptPolicyIdentifierOrZero','CcbptPolicySourceType','CcbptTargetDirection','CcbptTargetId','CcbptTargetType')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','StorageType','TextualConvention','TimeStamp')
ciscoCbpTargetMIB=ModuleIdentity((1,3,6,1,4,1,9,9,533))
if mibBuilder.loadTexts:ciscoCbpTargetMIB.setRevisions(('2006-05-24 00:00',))
_CiscoCbpTargetMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCbpTargetMIBNotifs=_CiscoCbpTargetMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,533,0))
_CiscoCbpTargetMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCbpTargetMIBObjects=_CiscoCbpTargetMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,533,1))
_CcbptTargetAttachCfg_ObjectIdentity=ObjectIdentity
ccbptTargetAttachCfg=_CcbptTargetAttachCfg_ObjectIdentity((1,3,6,1,4,1,9,9,533,1,1))
_CcbptPolicyIdNext_Type=CcbptPolicyIdentifierOrZero
_CcbptPolicyIdNext_Object=MibScalar
ccbptPolicyIdNext=_CcbptPolicyIdNext_Object((1,3,6,1,4,1,9,9,533,1,1,1),_CcbptPolicyIdNext_Type())
ccbptPolicyIdNext.setMaxAccess(_D)
if mibBuilder.loadTexts:ccbptPolicyIdNext.setStatus(_A)
_CcbptTargetTable_Object=MibTable
ccbptTargetTable=_CcbptTargetTable_Object((1,3,6,1,4,1,9,9,533,1,1,2))
if mibBuilder.loadTexts:ccbptTargetTable.setStatus(_A)
_CcbptTargetEntry_Object=MibTableRow
ccbptTargetEntry=_CcbptTargetEntry_Object((1,3,6,1,4,1,9,9,533,1,1,2,1))
ccbptTargetEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:ccbptTargetEntry.setStatus(_A)
_CcbptTargetType_Type=CcbptTargetType
_CcbptTargetType_Object=MibTableColumn
ccbptTargetType=_CcbptTargetType_Object((1,3,6,1,4,1,9,9,533,1,1,2,1,1),_CcbptTargetType_Type())
ccbptTargetType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccbptTargetType.setStatus(_A)
_CcbptTargetId_Type=CcbptTargetId
_CcbptTargetId_Object=MibTableColumn
ccbptTargetId=_CcbptTargetId_Object((1,3,6,1,4,1,9,9,533,1,1,2,1,2),_CcbptTargetId_Type())
ccbptTargetId.setMaxAccess(_C)
if mibBuilder.loadTexts:ccbptTargetId.setStatus(_A)
_CcbptTargetDir_Type=CcbptTargetDirection
_CcbptTargetDir_Object=MibTableColumn
ccbptTargetDir=_CcbptTargetDir_Object((1,3,6,1,4,1,9,9,533,1,1,2,1,3),_CcbptTargetDir_Type())
ccbptTargetDir.setMaxAccess(_C)
if mibBuilder.loadTexts:ccbptTargetDir.setStatus(_A)
_CcbptPolicySourceType_Type=CcbptPolicySourceType
_CcbptPolicySourceType_Object=MibTableColumn
ccbptPolicySourceType=_CcbptPolicySourceType_Object((1,3,6,1,4,1,9,9,533,1,1,2,1,4),_CcbptPolicySourceType_Type())
ccbptPolicySourceType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccbptPolicySourceType.setStatus(_A)
_CcbptPolicyId_Type=CcbptPolicyIdentifier
_CcbptPolicyId_Object=MibTableColumn
ccbptPolicyId=_CcbptPolicyId_Object((1,3,6,1,4,1,9,9,533,1,1,2,1,5),_CcbptPolicyId_Type())
ccbptPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:ccbptPolicyId.setStatus(_A)
_CcbptTargetStatus_Type=RowStatus
_CcbptTargetStatus_Object=MibTableColumn
ccbptTargetStatus=_CcbptTargetStatus_Object((1,3,6,1,4,1,9,9,533,1,1,2,1,6),_CcbptTargetStatus_Type())
ccbptTargetStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ccbptTargetStatus.setStatus(_A)
_CcbptTargetStorageType_Type=StorageType
_CcbptTargetStorageType_Object=MibTableColumn
ccbptTargetStorageType=_CcbptTargetStorageType_Object((1,3,6,1,4,1,9,9,533,1,1,2,1,7),_CcbptTargetStorageType_Type())
ccbptTargetStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:ccbptTargetStorageType.setStatus(_A)
_CcbptPolicyMap_Type=RowPointer
_CcbptPolicyMap_Object=MibTableColumn
ccbptPolicyMap=_CcbptPolicyMap_Object((1,3,6,1,4,1,9,9,533,1,1,2,1,8),_CcbptPolicyMap_Type())
ccbptPolicyMap.setMaxAccess(_E)
if mibBuilder.loadTexts:ccbptPolicyMap.setStatus(_A)
_CcbptPolicyInstance_Type=RowPointer
_CcbptPolicyInstance_Object=MibTableColumn
ccbptPolicyInstance=_CcbptPolicyInstance_Object((1,3,6,1,4,1,9,9,533,1,1,2,1,9),_CcbptPolicyInstance_Type())
ccbptPolicyInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:ccbptPolicyInstance.setStatus(_A)
_CcbptPolicyAttachTime_Type=TimeStamp
_CcbptPolicyAttachTime_Object=MibTableColumn
ccbptPolicyAttachTime=_CcbptPolicyAttachTime_Object((1,3,6,1,4,1,9,9,533,1,1,2,1,10),_CcbptPolicyAttachTime_Type())
ccbptPolicyAttachTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ccbptPolicyAttachTime.setStatus(_A)
_CcbptTargetTableLastChange_Type=TimeStamp
_CcbptTargetTableLastChange_Object=MibScalar
ccbptTargetTableLastChange=_CcbptTargetTableLastChange_Object((1,3,6,1,4,1,9,9,533,1,1,3),_CcbptTargetTableLastChange_Type())
ccbptTargetTableLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:ccbptTargetTableLastChange.setStatus(_A)
_CiscoCbpTargetMIBConform_ObjectIdentity=ObjectIdentity
ciscoCbpTargetMIBConform=_CiscoCbpTargetMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,533,2))
_CiscoCbpTargetMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCbpTargetMIBCompliances=_CiscoCbpTargetMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,533,2,1))
_CiscoCbpTargetMIBMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCbpTargetMIBMIBGroups=_CiscoCbpTargetMIBMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,533,2,2))
ccbptTargetProvisioningGroup=ObjectGroup((1,3,6,1,4,1,9,9,533,2,2,1))
ccbptTargetProvisioningGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ccbptTargetProvisioningGroup.setStatus(_A)
ccbptTargetTimeGroup=ObjectGroup((1,3,6,1,4,1,9,9,533,2,2,2))
ccbptTargetTimeGroup.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ccbptTargetTimeGroup.setStatus(_A)
ciscoCbpTargetMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,533,2,1,1))
ciscoCbpTargetMIBCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:ciscoCbpTargetMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCbpTargetMIB':ciscoCbpTargetMIB,'ciscoCbpTargetMIBNotifs':ciscoCbpTargetMIBNotifs,'ciscoCbpTargetMIBObjects':ciscoCbpTargetMIBObjects,'ccbptTargetAttachCfg':ccbptTargetAttachCfg,_K:ccbptPolicyIdNext,'ccbptTargetTable':ccbptTargetTable,'ccbptTargetEntry':ccbptTargetEntry,_F:ccbptTargetType,_G:ccbptTargetId,_H:ccbptTargetDir,_I:ccbptPolicySourceType,_J:ccbptPolicyId,_L:ccbptTargetStatus,_M:ccbptTargetStorageType,_N:ccbptPolicyMap,_O:ccbptPolicyInstance,_Q:ccbptPolicyAttachTime,_P:ccbptTargetTableLastChange,'ciscoCbpTargetMIBConform':ciscoCbpTargetMIBConform,'ciscoCbpTargetMIBCompliances':ciscoCbpTargetMIBCompliances,'ciscoCbpTargetMIBCompliance':ciscoCbpTargetMIBCompliance,'ciscoCbpTargetMIBMIBGroups':ciscoCbpTargetMIBMIBGroups,_R:ccbptTargetProvisioningGroup,'ccbptTargetTimeGroup':ccbptTargetTimeGroup})