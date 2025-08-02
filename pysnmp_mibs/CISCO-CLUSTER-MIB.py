_e='ciscoClusterNotificationGroup'
_d='ccStatusMemberStatusChange'
_c='ccMemberRowStatus'
_b='ccMemberEntityLogicalIndex'
_a='ccMemberNumber'
_Z='ccStatusCommanderMacAddress'
_Y='ccStatusCommanderTAddress'
_X='ccStatusCommanderTDomain'
_W='ccStatusClusterMode'
_V='ccStatusClusterName'
_U='ccStatusMemberOrder'
_T='ccStatusMaxNumberOfMembers'
_S='ccStatusLastFailureAddMember'
_R='ccStatusLastNMSAddMemberTDomain'
_Q='ccStatusLastNMSAddMemberTAddress'
_P='ccStatusTimeOfLastChange'
_O='read-create'
_N='ccMemberMacAddress'
_M='read-write'
_L='TimeStamp'
_K='ciscoClusterCandidateGroup'
_J='ciscoClusterMemberGroup'
_I='ciscoClusterMemberStatusGroup'
_H='ciscoClusterStatusGroup'
_G='ccMemberOperStatus'
_F='ccCandidateMacAddress'
_E='SnmpAdminString'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-CLUSTER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TAddress,TDomain,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TAddress','TDomain','TextualConvention',_L)
ciscoClusterMIB=ModuleIdentity((1,3,6,1,4,1,9,9,134))
if mibBuilder.loadTexts:ciscoClusterMIB.setRevisions(('2005-11-18 00:00','1999-07-28 00:00'))
_CiscoClusterMIBObjects_ObjectIdentity=ObjectIdentity
ciscoClusterMIBObjects=_CiscoClusterMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,134,1))
_CcStatus_ObjectIdentity=ObjectIdentity
ccStatus=_CcStatus_ObjectIdentity((1,3,6,1,4,1,9,9,134,1,1))
class _CcStatusClusterName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CcStatusClusterName_Type.__name__=_E
_CcStatusClusterName_Object=MibScalar
ccStatusClusterName=_CcStatusClusterName_Object((1,3,6,1,4,1,9,9,134,1,1,1),_CcStatusClusterName_Type())
ccStatusClusterName.setMaxAccess(_M)
if mibBuilder.loadTexts:ccStatusClusterName.setStatus(_B)
class _CcStatusClusterMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('commandDevice',1),('memberDevice',2),('none',3)))
_CcStatusClusterMode_Type.__name__=_D
_CcStatusClusterMode_Object=MibScalar
ccStatusClusterMode=_CcStatusClusterMode_Object((1,3,6,1,4,1,9,9,134,1,1,2),_CcStatusClusterMode_Type())
ccStatusClusterMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ccStatusClusterMode.setStatus(_B)
_CcStatusCommanderTDomain_Type=TDomain
_CcStatusCommanderTDomain_Object=MibScalar
ccStatusCommanderTDomain=_CcStatusCommanderTDomain_Object((1,3,6,1,4,1,9,9,134,1,1,3),_CcStatusCommanderTDomain_Type())
ccStatusCommanderTDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:ccStatusCommanderTDomain.setStatus(_B)
_CcStatusCommanderTAddress_Type=TAddress
_CcStatusCommanderTAddress_Object=MibScalar
ccStatusCommanderTAddress=_CcStatusCommanderTAddress_Object((1,3,6,1,4,1,9,9,134,1,1,4),_CcStatusCommanderTAddress_Type())
ccStatusCommanderTAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccStatusCommanderTAddress.setStatus(_B)
_CcStatusCommanderMacAddress_Type=MacAddress
_CcStatusCommanderMacAddress_Object=MibScalar
ccStatusCommanderMacAddress=_CcStatusCommanderMacAddress_Object((1,3,6,1,4,1,9,9,134,1,1,5),_CcStatusCommanderMacAddress_Type())
ccStatusCommanderMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccStatusCommanderMacAddress.setStatus(_B)
class _CcStatusTimeOfLastChange_Type(TimeStamp):defaultValue=0
_CcStatusTimeOfLastChange_Type.__name__=_L
_CcStatusTimeOfLastChange_Object=MibScalar
ccStatusTimeOfLastChange=_CcStatusTimeOfLastChange_Object((1,3,6,1,4,1,9,9,134,1,1,6),_CcStatusTimeOfLastChange_Type())
ccStatusTimeOfLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:ccStatusTimeOfLastChange.setStatus(_B)
_CcStatusLastNMSAddMemberTDomain_Type=TDomain
_CcStatusLastNMSAddMemberTDomain_Object=MibScalar
ccStatusLastNMSAddMemberTDomain=_CcStatusLastNMSAddMemberTDomain_Object((1,3,6,1,4,1,9,9,134,1,1,7),_CcStatusLastNMSAddMemberTDomain_Type())
ccStatusLastNMSAddMemberTDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:ccStatusLastNMSAddMemberTDomain.setStatus(_B)
_CcStatusLastNMSAddMemberTAddress_Type=TAddress
_CcStatusLastNMSAddMemberTAddress_Object=MibScalar
ccStatusLastNMSAddMemberTAddress=_CcStatusLastNMSAddMemberTAddress_Object((1,3,6,1,4,1,9,9,134,1,1,8),_CcStatusLastNMSAddMemberTAddress_Type())
ccStatusLastNMSAddMemberTAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccStatusLastNMSAddMemberTAddress.setStatus(_B)
class _CcStatusLastFailureAddMember_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('password',2),('overmax',3),('noncandidate',4),('memberNumberInUse',5),('unreachable',6)))
_CcStatusLastFailureAddMember_Type.__name__=_D
_CcStatusLastFailureAddMember_Object=MibScalar
ccStatusLastFailureAddMember=_CcStatusLastFailureAddMember_Object((1,3,6,1,4,1,9,9,134,1,1,9),_CcStatusLastFailureAddMember_Type())
ccStatusLastFailureAddMember.setMaxAccess(_C)
if mibBuilder.loadTexts:ccStatusLastFailureAddMember.setStatus(_B)
_CcStatusMaxNumberOfMembers_Type=Unsigned32
_CcStatusMaxNumberOfMembers_Object=MibScalar
ccStatusMaxNumberOfMembers=_CcStatusMaxNumberOfMembers_Object((1,3,6,1,4,1,9,9,134,1,1,10),_CcStatusMaxNumberOfMembers_Type())
ccStatusMaxNumberOfMembers.setMaxAccess(_C)
if mibBuilder.loadTexts:ccStatusMaxNumberOfMembers.setStatus(_B)
class _CcStatusMemberOrder_Type(SnmpAdminString):defaultValue=OctetString('')
_CcStatusMemberOrder_Type.__name__=_E
_CcStatusMemberOrder_Object=MibScalar
ccStatusMemberOrder=_CcStatusMemberOrder_Object((1,3,6,1,4,1,9,9,134,1,1,11),_CcStatusMemberOrder_Type())
ccStatusMemberOrder.setMaxAccess(_M)
if mibBuilder.loadTexts:ccStatusMemberOrder.setStatus(_B)
_CcMember_ObjectIdentity=ObjectIdentity
ccMember=_CcMember_ObjectIdentity((1,3,6,1,4,1,9,9,134,1,2))
_CcMemberTable_Object=MibTable
ccMemberTable=_CcMemberTable_Object((1,3,6,1,4,1,9,9,134,1,2,1))
if mibBuilder.loadTexts:ccMemberTable.setStatus(_B)
_CcMemberEntry_Object=MibTableRow
ccMemberEntry=_CcMemberEntry_Object((1,3,6,1,4,1,9,9,134,1,2,1,1))
ccMemberEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:ccMemberEntry.setStatus(_B)
_CcMemberMacAddress_Type=MacAddress
_CcMemberMacAddress_Object=MibTableColumn
ccMemberMacAddress=_CcMemberMacAddress_Object((1,3,6,1,4,1,9,9,134,1,2,1,1,1),_CcMemberMacAddress_Type())
ccMemberMacAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ccMemberMacAddress.setStatus(_B)
_CcMemberNumber_Type=Unsigned32
_CcMemberNumber_Object=MibTableColumn
ccMemberNumber=_CcMemberNumber_Object((1,3,6,1,4,1,9,9,134,1,2,1,1,2),_CcMemberNumber_Type())
ccMemberNumber.setMaxAccess(_O)
if mibBuilder.loadTexts:ccMemberNumber.setStatus(_B)
class _CcMemberOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_CcMemberOperStatus_Type.__name__=_D
_CcMemberOperStatus_Object=MibTableColumn
ccMemberOperStatus=_CcMemberOperStatus_Object((1,3,6,1,4,1,9,9,134,1,2,1,1,3),_CcMemberOperStatus_Type())
ccMemberOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccMemberOperStatus.setStatus(_B)
class _CcMemberEntityLogicalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CcMemberEntityLogicalIndex_Type.__name__=_D
_CcMemberEntityLogicalIndex_Object=MibTableColumn
ccMemberEntityLogicalIndex=_CcMemberEntityLogicalIndex_Object((1,3,6,1,4,1,9,9,134,1,2,1,1,4),_CcMemberEntityLogicalIndex_Type())
ccMemberEntityLogicalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ccMemberEntityLogicalIndex.setStatus(_B)
_CcMemberRowStatus_Type=RowStatus
_CcMemberRowStatus_Object=MibTableColumn
ccMemberRowStatus=_CcMemberRowStatus_Object((1,3,6,1,4,1,9,9,134,1,2,1,1,5),_CcMemberRowStatus_Type())
ccMemberRowStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:ccMemberRowStatus.setStatus(_B)
_CcCandidate_ObjectIdentity=ObjectIdentity
ccCandidate=_CcCandidate_ObjectIdentity((1,3,6,1,4,1,9,9,134,1,3))
_CcCandidateTable_Object=MibTable
ccCandidateTable=_CcCandidateTable_Object((1,3,6,1,4,1,9,9,134,1,3,1))
if mibBuilder.loadTexts:ccCandidateTable.setStatus(_B)
_CcCandidateEntry_Object=MibTableRow
ccCandidateEntry=_CcCandidateEntry_Object((1,3,6,1,4,1,9,9,134,1,3,1,1))
ccCandidateEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:ccCandidateEntry.setStatus(_B)
_CcCandidateMacAddress_Type=MacAddress
_CcCandidateMacAddress_Object=MibTableColumn
ccCandidateMacAddress=_CcCandidateMacAddress_Object((1,3,6,1,4,1,9,9,134,1,3,1,1,1),_CcCandidateMacAddress_Type())
ccCandidateMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccCandidateMacAddress.setStatus(_B)
_CiscoClusterMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
ciscoClusterMIBNotificationsPrefix=_CiscoClusterMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,134,2))
_CiscoClusterMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoClusterMIBNotifications=_CiscoClusterMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,134,2,0))
_CiscoClusterMIBConformance_ObjectIdentity=ObjectIdentity
ciscoClusterMIBConformance=_CiscoClusterMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,134,3))
_CiscoClusterMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoClusterMIBCompliances=_CiscoClusterMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,134,3,1))
_CiscoClusterMIBGroups_ObjectIdentity=ObjectIdentity
ciscoClusterMIBGroups=_CiscoClusterMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,134,3,2))
ciscoClusterStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,134,3,2,1))
ciscoClusterStatusGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:ciscoClusterStatusGroup.setStatus(_B)
ciscoClusterMemberStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,134,3,2,2))
ciscoClusterMemberStatusGroup.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:ciscoClusterMemberStatusGroup.setStatus(_B)
ciscoClusterMemberGroup=ObjectGroup((1,3,6,1,4,1,9,9,134,3,2,3))
ciscoClusterMemberGroup.setObjects(*((_A,_G),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:ciscoClusterMemberGroup.setStatus(_B)
ciscoClusterCandidateGroup=ObjectGroup((1,3,6,1,4,1,9,9,134,3,2,4))
ciscoClusterCandidateGroup.setObjects((_A,_F))
if mibBuilder.loadTexts:ciscoClusterCandidateGroup.setStatus(_B)
ccStatusMemberStatusChange=NotificationType((1,3,6,1,4,1,9,9,134,2,0,1))
ccStatusMemberStatusChange.setObjects((_A,_G))
if mibBuilder.loadTexts:ccStatusMemberStatusChange.setStatus(_B)
ciscoClusterNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,134,3,2,5))
ciscoClusterNotificationGroup.setObjects((_A,_d))
if mibBuilder.loadTexts:ciscoClusterNotificationGroup.setStatus(_B)
ciscoClusterCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,134,3,1,1))
ciscoClusterCompliance.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoClusterCompliance.setStatus('deprecated')
ciscoClusterComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,134,3,1,2))
ciscoClusterComplianceRev1.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_e)))
if mibBuilder.loadTexts:ciscoClusterComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoClusterMIB':ciscoClusterMIB,'ciscoClusterMIBObjects':ciscoClusterMIBObjects,'ccStatus':ccStatus,_V:ccStatusClusterName,_W:ccStatusClusterMode,_X:ccStatusCommanderTDomain,_Y:ccStatusCommanderTAddress,_Z:ccStatusCommanderMacAddress,_P:ccStatusTimeOfLastChange,_R:ccStatusLastNMSAddMemberTDomain,_Q:ccStatusLastNMSAddMemberTAddress,_S:ccStatusLastFailureAddMember,_T:ccStatusMaxNumberOfMembers,_U:ccStatusMemberOrder,'ccMember':ccMember,'ccMemberTable':ccMemberTable,'ccMemberEntry':ccMemberEntry,_N:ccMemberMacAddress,_a:ccMemberNumber,_G:ccMemberOperStatus,_b:ccMemberEntityLogicalIndex,_c:ccMemberRowStatus,'ccCandidate':ccCandidate,'ccCandidateTable':ccCandidateTable,'ccCandidateEntry':ccCandidateEntry,_F:ccCandidateMacAddress,'ciscoClusterMIBNotificationsPrefix':ciscoClusterMIBNotificationsPrefix,'ciscoClusterMIBNotifications':ciscoClusterMIBNotifications,_d:ccStatusMemberStatusChange,'ciscoClusterMIBConformance':ciscoClusterMIBConformance,'ciscoClusterMIBCompliances':ciscoClusterMIBCompliances,'ciscoClusterCompliance':ciscoClusterCompliance,'ciscoClusterComplianceRev1':ciscoClusterComplianceRev1,'ciscoClusterMIBGroups':ciscoClusterMIBGroups,_H:ciscoClusterStatusGroup,_I:ciscoClusterMemberStatusGroup,_J:ciscoClusterMemberGroup,_K:ciscoClusterCandidateGroup,_e:ciscoClusterNotificationGroup})