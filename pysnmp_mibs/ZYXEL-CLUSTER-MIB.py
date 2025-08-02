_K='zyClusterInfoMemberMacAddress'
_J='zyClusterCandidateMacAddress'
_I='zyClusterMemberMacAddress'
_H='read-create'
_G='read-write'
_F='zyClusterManagerVid'
_E='Integer32'
_D='not-accessible'
_C='ZYXEL-CLUSTER-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelCluster=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,14))
_ZyxelClusterSetup_ObjectIdentity=ObjectIdentity
zyxelClusterSetup=_ZyxelClusterSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,14,1))
_ZyxelClusterManager_ObjectIdentity=ObjectIdentity
zyxelClusterManager=_ZyxelClusterManager_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,14,1,1))
_ZyClusterManagerMaxNumberOfManagers_Type=Integer32
_ZyClusterManagerMaxNumberOfManagers_Object=MibScalar
zyClusterManagerMaxNumberOfManagers=_ZyClusterManagerMaxNumberOfManagers_Object((1,3,6,1,4,1,890,1,15,3,14,1,1,1),_ZyClusterManagerMaxNumberOfManagers_Type())
zyClusterManagerMaxNumberOfManagers.setMaxAccess(_B)
if mibBuilder.loadTexts:zyClusterManagerMaxNumberOfManagers.setStatus(_A)
_ZyxelClusterManagerTable_Object=MibTable
zyxelClusterManagerTable=_ZyxelClusterManagerTable_Object((1,3,6,1,4,1,890,1,15,3,14,1,1,2))
if mibBuilder.loadTexts:zyxelClusterManagerTable.setStatus(_A)
_ZyxelClusterManagerEntry_Object=MibTableRow
zyxelClusterManagerEntry=_ZyxelClusterManagerEntry_Object((1,3,6,1,4,1,890,1,15,3,14,1,1,2,1))
zyxelClusterManagerEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:zyxelClusterManagerEntry.setStatus(_A)
_ZyClusterManagerVid_Type=Integer32
_ZyClusterManagerVid_Object=MibTableColumn
zyClusterManagerVid=_ZyClusterManagerVid_Object((1,3,6,1,4,1,890,1,15,3,14,1,1,2,1,1),_ZyClusterManagerVid_Type())
zyClusterManagerVid.setMaxAccess(_D)
if mibBuilder.loadTexts:zyClusterManagerVid.setStatus(_A)
_ZyClusterManagerName_Type=DisplayString
_ZyClusterManagerName_Object=MibTableColumn
zyClusterManagerName=_ZyClusterManagerName_Object((1,3,6,1,4,1,890,1,15,3,14,1,1,2,1,2),_ZyClusterManagerName_Type())
zyClusterManagerName.setMaxAccess(_G)
if mibBuilder.loadTexts:zyClusterManagerName.setStatus(_A)
_ZyClusterManagerRowStatus_Type=RowStatus
_ZyClusterManagerRowStatus_Object=MibTableColumn
zyClusterManagerRowStatus=_ZyClusterManagerRowStatus_Object((1,3,6,1,4,1,890,1,15,3,14,1,1,2,1,3),_ZyClusterManagerRowStatus_Type())
zyClusterManagerRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:zyClusterManagerRowStatus.setStatus(_A)
_ZyxelClusterMembers_ObjectIdentity=ObjectIdentity
zyxelClusterMembers=_ZyxelClusterMembers_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,14,1,2))
_ZyClusterMemberMaxNumberOfMembers_Type=Integer32
_ZyClusterMemberMaxNumberOfMembers_Object=MibScalar
zyClusterMemberMaxNumberOfMembers=_ZyClusterMemberMaxNumberOfMembers_Object((1,3,6,1,4,1,890,1,15,3,14,1,2,1),_ZyClusterMemberMaxNumberOfMembers_Type())
zyClusterMemberMaxNumberOfMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:zyClusterMemberMaxNumberOfMembers.setStatus(_A)
_ZyxelClusterMemberTable_Object=MibTable
zyxelClusterMemberTable=_ZyxelClusterMemberTable_Object((1,3,6,1,4,1,890,1,15,3,14,1,2,2))
if mibBuilder.loadTexts:zyxelClusterMemberTable.setStatus(_A)
_ZyxelClusterMemberEntry_Object=MibTableRow
zyxelClusterMemberEntry=_ZyxelClusterMemberEntry_Object((1,3,6,1,4,1,890,1,15,3,14,1,2,2,1))
zyxelClusterMemberEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:zyxelClusterMemberEntry.setStatus(_A)
_ZyClusterMemberMacAddress_Type=MacAddress
_ZyClusterMemberMacAddress_Object=MibTableColumn
zyClusterMemberMacAddress=_ZyClusterMemberMacAddress_Object((1,3,6,1,4,1,890,1,15,3,14,1,2,2,1,1),_ZyClusterMemberMacAddress_Type())
zyClusterMemberMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zyClusterMemberMacAddress.setStatus(_A)
_ZyClusterMemberName_Type=DisplayString
_ZyClusterMemberName_Object=MibTableColumn
zyClusterMemberName=_ZyClusterMemberName_Object((1,3,6,1,4,1,890,1,15,3,14,1,2,2,1,2),_ZyClusterMemberName_Type())
zyClusterMemberName.setMaxAccess(_B)
if mibBuilder.loadTexts:zyClusterMemberName.setStatus(_A)
_ZyClusterMemberModel_Type=DisplayString
_ZyClusterMemberModel_Object=MibTableColumn
zyClusterMemberModel=_ZyClusterMemberModel_Object((1,3,6,1,4,1,890,1,15,3,14,1,2,2,1,3),_ZyClusterMemberModel_Type())
zyClusterMemberModel.setMaxAccess(_B)
if mibBuilder.loadTexts:zyClusterMemberModel.setStatus(_A)
_ZyClusterMemberPassword_Type=DisplayString
_ZyClusterMemberPassword_Object=MibTableColumn
zyClusterMemberPassword=_ZyClusterMemberPassword_Object((1,3,6,1,4,1,890,1,15,3,14,1,2,2,1,4),_ZyClusterMemberPassword_Type())
zyClusterMemberPassword.setMaxAccess(_G)
if mibBuilder.loadTexts:zyClusterMemberPassword.setStatus(_A)
_ZyClusterMemberRowStatus_Type=RowStatus
_ZyClusterMemberRowStatus_Object=MibTableColumn
zyClusterMemberRowStatus=_ZyClusterMemberRowStatus_Object((1,3,6,1,4,1,890,1,15,3,14,1,2,2,1,5),_ZyClusterMemberRowStatus_Type())
zyClusterMemberRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:zyClusterMemberRowStatus.setStatus(_A)
_ZyxelClusterStatus_ObjectIdentity=ObjectIdentity
zyxelClusterStatus=_ZyxelClusterStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,14,2))
_ZyxelClusterCandidate_ObjectIdentity=ObjectIdentity
zyxelClusterCandidate=_ZyxelClusterCandidate_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,14,2,1))
_ZyxelClusterCandidateTable_Object=MibTable
zyxelClusterCandidateTable=_ZyxelClusterCandidateTable_Object((1,3,6,1,4,1,890,1,15,3,14,2,1,1))
if mibBuilder.loadTexts:zyxelClusterCandidateTable.setStatus(_A)
_ZyxelClusterCandidateEntry_Object=MibTableRow
zyxelClusterCandidateEntry=_ZyxelClusterCandidateEntry_Object((1,3,6,1,4,1,890,1,15,3,14,2,1,1,1))
zyxelClusterCandidateEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:zyxelClusterCandidateEntry.setStatus(_A)
_ZyClusterCandidateMacAddress_Type=MacAddress
_ZyClusterCandidateMacAddress_Object=MibTableColumn
zyClusterCandidateMacAddress=_ZyClusterCandidateMacAddress_Object((1,3,6,1,4,1,890,1,15,3,14,2,1,1,1,1),_ZyClusterCandidateMacAddress_Type())
zyClusterCandidateMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zyClusterCandidateMacAddress.setStatus(_A)
_ZyClusterCandidateName_Type=DisplayString
_ZyClusterCandidateName_Object=MibTableColumn
zyClusterCandidateName=_ZyClusterCandidateName_Object((1,3,6,1,4,1,890,1,15,3,14,2,1,1,1,2),_ZyClusterCandidateName_Type())
zyClusterCandidateName.setMaxAccess(_B)
if mibBuilder.loadTexts:zyClusterCandidateName.setStatus(_A)
_ZyClusterCandidateModel_Type=DisplayString
_ZyClusterCandidateModel_Object=MibTableColumn
zyClusterCandidateModel=_ZyClusterCandidateModel_Object((1,3,6,1,4,1,890,1,15,3,14,2,1,1,1,3),_ZyClusterCandidateModel_Type())
zyClusterCandidateModel.setMaxAccess(_B)
if mibBuilder.loadTexts:zyClusterCandidateModel.setStatus(_A)
class _ZyClusterRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('manager',1),('member',2)))
_ZyClusterRole_Type.__name__=_E
_ZyClusterRole_Object=MibScalar
zyClusterRole=_ZyClusterRole_Object((1,3,6,1,4,1,890,1,15,3,14,2,2),_ZyClusterRole_Type())
zyClusterRole.setMaxAccess(_B)
if mibBuilder.loadTexts:zyClusterRole.setStatus(_A)
_ZyClusterInfoManager_Type=DisplayString
_ZyClusterInfoManager_Object=MibScalar
zyClusterInfoManager=_ZyClusterInfoManager_Object((1,3,6,1,4,1,890,1,15,3,14,2,3),_ZyClusterInfoManager_Type())
zyClusterInfoManager.setMaxAccess(_B)
if mibBuilder.loadTexts:zyClusterInfoManager.setStatus(_A)
_ZyxelClusterInfoMemberTable_Object=MibTable
zyxelClusterInfoMemberTable=_ZyxelClusterInfoMemberTable_Object((1,3,6,1,4,1,890,1,15,3,14,2,4))
if mibBuilder.loadTexts:zyxelClusterInfoMemberTable.setStatus(_A)
_ZyxelClusterInfoMemberEntry_Object=MibTableRow
zyxelClusterInfoMemberEntry=_ZyxelClusterInfoMemberEntry_Object((1,3,6,1,4,1,890,1,15,3,14,2,4,1))
zyxelClusterInfoMemberEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:zyxelClusterInfoMemberEntry.setStatus(_A)
_ZyClusterInfoMemberMacAddress_Type=MacAddress
_ZyClusterInfoMemberMacAddress_Object=MibTableColumn
zyClusterInfoMemberMacAddress=_ZyClusterInfoMemberMacAddress_Object((1,3,6,1,4,1,890,1,15,3,14,2,4,1,1),_ZyClusterInfoMemberMacAddress_Type())
zyClusterInfoMemberMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zyClusterInfoMemberMacAddress.setStatus(_A)
_ZyClusterInfoMemberName_Type=DisplayString
_ZyClusterInfoMemberName_Object=MibTableColumn
zyClusterInfoMemberName=_ZyClusterInfoMemberName_Object((1,3,6,1,4,1,890,1,15,3,14,2,4,1,2),_ZyClusterInfoMemberName_Type())
zyClusterInfoMemberName.setMaxAccess(_B)
if mibBuilder.loadTexts:zyClusterInfoMemberName.setStatus(_A)
_ZyClusterInfoMemberModel_Type=DisplayString
_ZyClusterInfoMemberModel_Object=MibTableColumn
zyClusterInfoMemberModel=_ZyClusterInfoMemberModel_Object((1,3,6,1,4,1,890,1,15,3,14,2,4,1,3),_ZyClusterInfoMemberModel_Type())
zyClusterInfoMemberModel.setMaxAccess(_B)
if mibBuilder.loadTexts:zyClusterInfoMemberModel.setStatus(_A)
class _ZyClusterInfoMemberStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('error',0),('online',1),('offline',2)))
_ZyClusterInfoMemberStatus_Type.__name__=_E
_ZyClusterInfoMemberStatus_Object=MibTableColumn
zyClusterInfoMemberStatus=_ZyClusterInfoMemberStatus_Object((1,3,6,1,4,1,890,1,15,3,14,2,4,1,4),_ZyClusterInfoMemberStatus_Type())
zyClusterInfoMemberStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zyClusterInfoMemberStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelCluster':zyxelCluster,'zyxelClusterSetup':zyxelClusterSetup,'zyxelClusterManager':zyxelClusterManager,'zyClusterManagerMaxNumberOfManagers':zyClusterManagerMaxNumberOfManagers,'zyxelClusterManagerTable':zyxelClusterManagerTable,'zyxelClusterManagerEntry':zyxelClusterManagerEntry,_F:zyClusterManagerVid,'zyClusterManagerName':zyClusterManagerName,'zyClusterManagerRowStatus':zyClusterManagerRowStatus,'zyxelClusterMembers':zyxelClusterMembers,'zyClusterMemberMaxNumberOfMembers':zyClusterMemberMaxNumberOfMembers,'zyxelClusterMemberTable':zyxelClusterMemberTable,'zyxelClusterMemberEntry':zyxelClusterMemberEntry,_I:zyClusterMemberMacAddress,'zyClusterMemberName':zyClusterMemberName,'zyClusterMemberModel':zyClusterMemberModel,'zyClusterMemberPassword':zyClusterMemberPassword,'zyClusterMemberRowStatus':zyClusterMemberRowStatus,'zyxelClusterStatus':zyxelClusterStatus,'zyxelClusterCandidate':zyxelClusterCandidate,'zyxelClusterCandidateTable':zyxelClusterCandidateTable,'zyxelClusterCandidateEntry':zyxelClusterCandidateEntry,_J:zyClusterCandidateMacAddress,'zyClusterCandidateName':zyClusterCandidateName,'zyClusterCandidateModel':zyClusterCandidateModel,'zyClusterRole':zyClusterRole,'zyClusterInfoManager':zyClusterInfoManager,'zyxelClusterInfoMemberTable':zyxelClusterInfoMemberTable,'zyxelClusterInfoMemberEntry':zyxelClusterInfoMemberEntry,_K:zyClusterInfoMemberMacAddress,'zyClusterInfoMemberName':zyClusterInfoMemberName,'zyClusterInfoMemberModel':zyClusterInfoMemberModel,'zyClusterInfoMemberStatus':zyClusterInfoMemberStatus})