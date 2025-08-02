_Z='myClusterCandidateGroup'
_Y='myClusterMemberGroup'
_X='myClusterMemberStatusGroup'
_W='myClusterStatusGroup'
_V='scMemberRowStatus'
_U='scMemberDeviceID'
_T='scMemberNumber'
_S='scStatusCommanderMacAddress'
_R='scStatusLastFailureAddMember'
_Q='scStatusMaxNumberOfMembers'
_P='scStatusTimeOfLastChange'
_O='read-create'
_N='scMemberMacAddress'
_M='read-write'
_L='TimeStamp'
_K='DisplayString'
_J='EnabledStatus'
_I='scMemberOperStatus'
_H='scStatusClusterStatus'
_G='scStatusClusterMode'
_F='scStatusClusterName'
_E='scCandidateMacAddress'
_D='Integer32'
_C='read-only'
_B='MY-CLUSTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('MY-SMI','myMgmt')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_K,'MacAddress','PhysAddress','RowStatus','TextualConvention',_L)
myClusterMIB=ModuleIdentity((1,3,6,1,4,1,4881,1,1,10,2,31))
if mibBuilder.loadTexts:myClusterMIB.setRevisions(('2003-04-01 00:00',))
_MyClusterMIBObjects_ObjectIdentity=ObjectIdentity
myClusterMIBObjects=_MyClusterMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,31,1))
_ScStatus_ObjectIdentity=ObjectIdentity
scStatus=_ScStatus_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,31,1,1))
class _ScStatusClusterName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ScStatusClusterName_Type.__name__=_K
_ScStatusClusterName_Object=MibScalar
scStatusClusterName=_ScStatusClusterName_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,1,1),_ScStatusClusterName_Type())
scStatusClusterName.setMaxAccess(_M)
if mibBuilder.loadTexts:scStatusClusterName.setStatus(_A)
class _ScStatusClusterMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('commandDevice',1),('memberDevice',2),('none',3)))
_ScStatusClusterMode_Type.__name__=_D
_ScStatusClusterMode_Object=MibScalar
scStatusClusterMode=_ScStatusClusterMode_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,1,2),_ScStatusClusterMode_Type())
scStatusClusterMode.setMaxAccess(_C)
if mibBuilder.loadTexts:scStatusClusterMode.setStatus(_A)
class _ScStatusClusterStatus_Type(EnabledStatus):defaultValue=1
_ScStatusClusterStatus_Type.__name__=_J
_ScStatusClusterStatus_Object=MibScalar
scStatusClusterStatus=_ScStatusClusterStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,1,3),_ScStatusClusterStatus_Type())
scStatusClusterStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:scStatusClusterStatus.setStatus(_A)
_ScStatusCommanderMacAddress_Type=MacAddress
_ScStatusCommanderMacAddress_Object=MibScalar
scStatusCommanderMacAddress=_ScStatusCommanderMacAddress_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,1,4),_ScStatusCommanderMacAddress_Type())
scStatusCommanderMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:scStatusCommanderMacAddress.setStatus(_A)
class _ScStatusTimeOfLastChange_Type(TimeStamp):defaultValue=0
_ScStatusTimeOfLastChange_Type.__name__=_L
_ScStatusTimeOfLastChange_Object=MibScalar
scStatusTimeOfLastChange=_ScStatusTimeOfLastChange_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,1,5),_ScStatusTimeOfLastChange_Type())
scStatusTimeOfLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:scStatusTimeOfLastChange.setStatus(_A)
_ScStatusMaxNumberOfMembers_Type=Unsigned32
_ScStatusMaxNumberOfMembers_Object=MibScalar
scStatusMaxNumberOfMembers=_ScStatusMaxNumberOfMembers_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,1,6),_ScStatusMaxNumberOfMembers_Type())
scStatusMaxNumberOfMembers.setMaxAccess(_C)
if mibBuilder.loadTexts:scStatusMaxNumberOfMembers.setStatus(_A)
class _ScStatusLastFailureAddMember_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('password',2),('overmax',3),('noncandidate',4),('memberNumberInUse',5),('unreachable',6),('communityStringFull',7)))
_ScStatusLastFailureAddMember_Type.__name__=_D
_ScStatusLastFailureAddMember_Object=MibScalar
scStatusLastFailureAddMember=_ScStatusLastFailureAddMember_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,1,7),_ScStatusLastFailureAddMember_Type())
scStatusLastFailureAddMember.setMaxAccess(_C)
if mibBuilder.loadTexts:scStatusLastFailureAddMember.setStatus(_A)
_ScMember_ObjectIdentity=ObjectIdentity
scMember=_ScMember_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,31,1,2))
_ScMemberTable_Object=MibTable
scMemberTable=_ScMemberTable_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,2,1))
if mibBuilder.loadTexts:scMemberTable.setStatus(_A)
_ScMemberEntry_Object=MibTableRow
scMemberEntry=_ScMemberEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,2,1,1))
scMemberEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:scMemberEntry.setStatus(_A)
_ScMemberMacAddress_Type=MacAddress
_ScMemberMacAddress_Object=MibTableColumn
scMemberMacAddress=_ScMemberMacAddress_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,2,1,1,1),_ScMemberMacAddress_Type())
scMemberMacAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:scMemberMacAddress.setStatus(_A)
_ScMemberNumber_Type=Unsigned32
_ScMemberNumber_Object=MibTableColumn
scMemberNumber=_ScMemberNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,2,1,1,2),_ScMemberNumber_Type())
scMemberNumber.setMaxAccess(_O)
if mibBuilder.loadTexts:scMemberNumber.setStatus(_A)
class _ScMemberOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_ScMemberOperStatus_Type.__name__=_D
_ScMemberOperStatus_Object=MibTableColumn
scMemberOperStatus=_ScMemberOperStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,2,1,1,3),_ScMemberOperStatus_Type())
scMemberOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:scMemberOperStatus.setStatus(_A)
_ScMemberDeviceID_Type=MacAddress
_ScMemberDeviceID_Object=MibTableColumn
scMemberDeviceID=_ScMemberDeviceID_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,2,1,1,4),_ScMemberDeviceID_Type())
scMemberDeviceID.setMaxAccess(_C)
if mibBuilder.loadTexts:scMemberDeviceID.setStatus(_A)
_ScMemberRowStatus_Type=RowStatus
_ScMemberRowStatus_Object=MibTableColumn
scMemberRowStatus=_ScMemberRowStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,2,1,1,5),_ScMemberRowStatus_Type())
scMemberRowStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:scMemberRowStatus.setStatus(_A)
_ScCandidate_ObjectIdentity=ObjectIdentity
scCandidate=_ScCandidate_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,31,1,3))
_ScCandidateTable_Object=MibTable
scCandidateTable=_ScCandidateTable_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,3,1))
if mibBuilder.loadTexts:scCandidateTable.setStatus(_A)
_ScCandidateEntry_Object=MibTableRow
scCandidateEntry=_ScCandidateEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,3,1,1))
scCandidateEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:scCandidateEntry.setStatus(_A)
_ScCandidateMacAddress_Type=MacAddress
_ScCandidateMacAddress_Object=MibTableColumn
scCandidateMacAddress=_ScCandidateMacAddress_Object((1,3,6,1,4,1,4881,1,1,10,2,31,1,3,1,1,1),_ScCandidateMacAddress_Type())
scCandidateMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:scCandidateMacAddress.setStatus(_A)
_MyClusterTraps_ObjectIdentity=ObjectIdentity
myClusterTraps=_MyClusterTraps_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,31,2))
_MyClusterMIBConformance_ObjectIdentity=ObjectIdentity
myClusterMIBConformance=_MyClusterMIBConformance_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,31,3))
_MyClusterMIBCompliances_ObjectIdentity=ObjectIdentity
myClusterMIBCompliances=_MyClusterMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,31,3,1))
_MyClusterMIBGroups_ObjectIdentity=ObjectIdentity
myClusterMIBGroups=_MyClusterMIBGroups_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,31,3,2))
myClusterStatusGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,31,3,2,1))
myClusterStatusGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:myClusterStatusGroup.setStatus(_A)
myClusterMemberStatusGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,31,3,2,2))
myClusterMemberStatusGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_S)))
if mibBuilder.loadTexts:myClusterMemberStatusGroup.setStatus(_A)
myClusterCandidateStatusGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,31,3,2,3))
myClusterCandidateStatusGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:myClusterCandidateStatusGroup.setStatus(_A)
myClusterMemberGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,31,3,2,4))
myClusterMemberGroup.setObjects(*((_B,_I),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:myClusterMemberGroup.setStatus(_A)
myClusterCandidateGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,31,3,2,5))
myClusterCandidateGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:myClusterCandidateGroup.setStatus(_A)
memberStateChangeTrap=NotificationType((1,3,6,1,4,1,4881,1,1,10,2,31,2,1))
memberStateChangeTrap.setObjects((_B,_I))
if mibBuilder.loadTexts:memberStateChangeTrap.setStatus(_A)
myClusterCompliance=ModuleCompliance((1,3,6,1,4,1,4881,1,1,10,2,31,3,1,1))
myClusterCompliance.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:myClusterCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myClusterMIB':myClusterMIB,'myClusterMIBObjects':myClusterMIBObjects,'scStatus':scStatus,_F:scStatusClusterName,_G:scStatusClusterMode,_H:scStatusClusterStatus,_S:scStatusCommanderMacAddress,_P:scStatusTimeOfLastChange,_Q:scStatusMaxNumberOfMembers,_R:scStatusLastFailureAddMember,'scMember':scMember,'scMemberTable':scMemberTable,'scMemberEntry':scMemberEntry,_N:scMemberMacAddress,_T:scMemberNumber,_I:scMemberOperStatus,_U:scMemberDeviceID,_V:scMemberRowStatus,'scCandidate':scCandidate,'scCandidateTable':scCandidateTable,'scCandidateEntry':scCandidateEntry,_E:scCandidateMacAddress,'myClusterTraps':myClusterTraps,'memberStateChangeTrap':memberStateChangeTrap,'myClusterMIBConformance':myClusterMIBConformance,'myClusterMIBCompliances':myClusterMIBCompliances,'myClusterCompliance':myClusterCompliance,'myClusterMIBGroups':myClusterMIBGroups,_W:myClusterStatusGroup,_X:myClusterMemberStatusGroup,'myClusterCandidateStatusGroup':myClusterCandidateStatusGroup,_Y:myClusterMemberGroup,_Z:myClusterCandidateGroup})