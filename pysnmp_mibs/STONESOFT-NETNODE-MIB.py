_k='nodeHwmonNotificationsGroup'
_j='nodeHwmonGroup'
_i='nodeTesterNotificationsGroup'
_h='nodeTesterGroup'
_g='nodeLoginNotificationsGroup'
_f='nodeLoginGroup'
_e='nodeIdentificationGroup'
_d='nodeStatusNotificationsGroup'
_c='nodeStatusGroup'
_b='nodeHwmon'
_a='nodeTestFailure'
_Z='nodeUserLogout'
_Y='nodeFailedUserLogin'
_X='nodeUserLogin'
_W='nodeShutdown'
_V='nodeBoot'
_U='nodeOffline'
_T='nodeOnline'
_S='nodeTestResultTime'
_R='nodeTestResult'
_Q='nodeLastLoginTime'
_P='nodeCPULoad'
_O='nodePosCode'
_N='nodeSerialNumber'
_M='nodeApplianceModel'
_L='nodeMemberId'
_K='nodeClusterId'
_J='nodeTestIndex'
_I='Unsigned32'
_H='nodeHwmonEvent'
_G='nodeTestIdentity'
_F='nodeLastLogin'
_E='nodeOperState'
_D='Integer32'
_C='read-only'
_B='current'
_A='STONESOFT-NETNODE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
stonesoftModules,stonesoftNetworkNode=mibBuilder.importSymbols('STONESOFT-SMI-MIB','stonesoftModules','stonesoftNetworkNode')
stonesoftNetworkNodeMibModule=ModuleIdentity((1,3,6,1,4,1,1369,3,4))
if mibBuilder.loadTexts:stonesoftNetworkNodeMibModule.setRevisions(('2014-03-10 00:00','2008-02-04 00:00','2004-06-16 00:00'))
_NetNodeObjects_ObjectIdentity=ObjectIdentity
netNodeObjects=_NetNodeObjects_ObjectIdentity((1,3,6,1,4,1,1369,6,1,1))
class _NodeClusterId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NodeClusterId_Type.__name__=_D
_NodeClusterId_Object=MibScalar
nodeClusterId=_NodeClusterId_Object((1,3,6,1,4,1,1369,6,1,1,1),_NodeClusterId_Type())
nodeClusterId.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeClusterId.setStatus(_B)
class _NodeMemberId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_NodeMemberId_Type.__name__=_D
_NodeMemberId_Object=MibScalar
nodeMemberId=_NodeMemberId_Object((1,3,6,1,4,1,1369,6,1,1,2),_NodeMemberId_Type())
nodeMemberId.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeMemberId.setStatus(_B)
class _NodeOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('unknown',0),('online',1),('goingOnline',2),('lockedOnline',3),('goingLockedOnline',4),('offline',5),('goingOffline',6),('lockedOffline',7),('goingLockedOffline',8),('standby',9),('goingStandby',10)))
_NodeOperState_Type.__name__=_D
_NodeOperState_Object=MibScalar
nodeOperState=_NodeOperState_Object((1,3,6,1,4,1,1369,6,1,1,3),_NodeOperState_Type())
nodeOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeOperState.setStatus(_B)
class _NodeCPULoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NodeCPULoad_Type.__name__=_D
_NodeCPULoad_Object=MibScalar
nodeCPULoad=_NodeCPULoad_Object((1,3,6,1,4,1,1369,6,1,1,4),_NodeCPULoad_Type())
nodeCPULoad.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeCPULoad.setStatus(_B)
_NodeLastLogin_Type=DisplayString
_NodeLastLogin_Object=MibScalar
nodeLastLogin=_NodeLastLogin_Object((1,3,6,1,4,1,1369,6,1,1,5),_NodeLastLogin_Type())
nodeLastLogin.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeLastLogin.setStatus(_B)
_NodeLastLoginTime_Type=TimeStamp
_NodeLastLoginTime_Object=MibScalar
nodeLastLoginTime=_NodeLastLoginTime_Object((1,3,6,1,4,1,1369,6,1,1,6),_NodeLastLoginTime_Type())
nodeLastLoginTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeLastLoginTime.setStatus(_B)
_NodeTestTable_Object=MibTable
nodeTestTable=_NodeTestTable_Object((1,3,6,1,4,1,1369,6,1,1,7))
if mibBuilder.loadTexts:nodeTestTable.setStatus(_B)
_NodeTestEntry_Object=MibTableRow
nodeTestEntry=_NodeTestEntry_Object((1,3,6,1,4,1,1369,6,1,1,7,1))
nodeTestEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:nodeTestEntry.setStatus(_B)
class _NodeTestIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NodeTestIndex_Type.__name__=_I
_NodeTestIndex_Object=MibTableColumn
nodeTestIndex=_NodeTestIndex_Object((1,3,6,1,4,1,1369,6,1,1,7,1,1),_NodeTestIndex_Type())
nodeTestIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:nodeTestIndex.setStatus(_B)
_NodeTestIdentity_Type=DisplayString
_NodeTestIdentity_Object=MibTableColumn
nodeTestIdentity=_NodeTestIdentity_Object((1,3,6,1,4,1,1369,6,1,1,7,1,2),_NodeTestIdentity_Type())
nodeTestIdentity.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeTestIdentity.setStatus(_B)
class _NodeTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('success',1),('failure',2)))
_NodeTestResult_Type.__name__=_D
_NodeTestResult_Object=MibTableColumn
nodeTestResult=_NodeTestResult_Object((1,3,6,1,4,1,1369,6,1,1,7,1,3),_NodeTestResult_Type())
nodeTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeTestResult.setStatus(_B)
_NodeTestResultTime_Type=TimeStamp
_NodeTestResultTime_Object=MibTableColumn
nodeTestResultTime=_NodeTestResultTime_Object((1,3,6,1,4,1,1369,6,1,1,7,1,4),_NodeTestResultTime_Type())
nodeTestResultTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeTestResultTime.setStatus(_B)
_NodeHwmonEvent_Type=DisplayString
_NodeHwmonEvent_Object=MibScalar
nodeHwmonEvent=_NodeHwmonEvent_Object((1,3,6,1,4,1,1369,6,1,1,8),_NodeHwmonEvent_Type())
nodeHwmonEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeHwmonEvent.setStatus(_B)
_NodeApplianceModel_Type=DisplayString
_NodeApplianceModel_Object=MibScalar
nodeApplianceModel=_NodeApplianceModel_Object((1,3,6,1,4,1,1369,6,1,1,9),_NodeApplianceModel_Type())
nodeApplianceModel.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeApplianceModel.setStatus(_B)
_NodeSerialNumber_Type=DisplayString
_NodeSerialNumber_Object=MibScalar
nodeSerialNumber=_NodeSerialNumber_Object((1,3,6,1,4,1,1369,6,1,1,10),_NodeSerialNumber_Type())
nodeSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeSerialNumber.setStatus(_B)
_NodePosCode_Type=DisplayString
_NodePosCode_Object=MibScalar
nodePosCode=_NodePosCode_Object((1,3,6,1,4,1,1369,6,1,1,11),_NodePosCode_Type())
nodePosCode.setMaxAccess(_C)
if mibBuilder.loadTexts:nodePosCode.setStatus(_B)
_NetNodeEvents_ObjectIdentity=ObjectIdentity
netNodeEvents=_NetNodeEvents_ObjectIdentity((1,3,6,1,4,1,1369,6,1,2))
_NetNodeEventsV2_ObjectIdentity=ObjectIdentity
netNodeEventsV2=_NetNodeEventsV2_ObjectIdentity((1,3,6,1,4,1,1369,6,1,2,0))
_NetNodeConformance_ObjectIdentity=ObjectIdentity
netNodeConformance=_NetNodeConformance_ObjectIdentity((1,3,6,1,4,1,1369,6,1,3))
_NetNodeGroups_ObjectIdentity=ObjectIdentity
netNodeGroups=_NetNodeGroups_ObjectIdentity((1,3,6,1,4,1,1369,6,1,3,1))
_NetNodeCompliances_ObjectIdentity=ObjectIdentity
netNodeCompliances=_NetNodeCompliances_ObjectIdentity((1,3,6,1,4,1,1369,6,1,3,2))
nodeIdentificationGroup=ObjectGroup((1,3,6,1,4,1,1369,6,1,3,1,1))
nodeIdentificationGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:nodeIdentificationGroup.setStatus(_B)
nodeStatusGroup=ObjectGroup((1,3,6,1,4,1,1369,6,1,3,1,2))
nodeStatusGroup.setObjects(*((_A,_E),(_A,_P)))
if mibBuilder.loadTexts:nodeStatusGroup.setStatus(_B)
nodeLoginGroup=ObjectGroup((1,3,6,1,4,1,1369,6,1,3,1,3))
nodeLoginGroup.setObjects(*((_A,_F),(_A,_Q)))
if mibBuilder.loadTexts:nodeLoginGroup.setStatus(_B)
nodeTesterGroup=ObjectGroup((1,3,6,1,4,1,1369,6,1,3,1,4))
nodeTesterGroup.setObjects(*((_A,_G),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:nodeTesterGroup.setStatus(_B)
nodeHwmonGroup=ObjectGroup((1,3,6,1,4,1,1369,6,1,3,1,8))
nodeHwmonGroup.setObjects((_A,_H))
if mibBuilder.loadTexts:nodeHwmonGroup.setStatus(_B)
nodeOnline=NotificationType((1,3,6,1,4,1,1369,6,1,2,0,1))
nodeOnline.setObjects((_A,_E))
if mibBuilder.loadTexts:nodeOnline.setStatus(_B)
nodeOffline=NotificationType((1,3,6,1,4,1,1369,6,1,2,0,2))
nodeOffline.setObjects((_A,_E))
if mibBuilder.loadTexts:nodeOffline.setStatus(_B)
nodeBoot=NotificationType((1,3,6,1,4,1,1369,6,1,2,0,3))
if mibBuilder.loadTexts:nodeBoot.setStatus(_B)
nodeShutdown=NotificationType((1,3,6,1,4,1,1369,6,1,2,0,4))
if mibBuilder.loadTexts:nodeShutdown.setStatus(_B)
nodeUserLogin=NotificationType((1,3,6,1,4,1,1369,6,1,2,0,5))
nodeUserLogin.setObjects((_A,_F))
if mibBuilder.loadTexts:nodeUserLogin.setStatus(_B)
nodeTestFailure=NotificationType((1,3,6,1,4,1,1369,6,1,2,0,6))
nodeTestFailure.setObjects((_A,_G))
if mibBuilder.loadTexts:nodeTestFailure.setStatus(_B)
nodeHwmon=NotificationType((1,3,6,1,4,1,1369,6,1,2,0,7))
nodeHwmon.setObjects((_A,_H))
if mibBuilder.loadTexts:nodeHwmon.setStatus(_B)
nodeFailedUserLogin=NotificationType((1,3,6,1,4,1,1369,6,1,2,0,8))
if mibBuilder.loadTexts:nodeFailedUserLogin.setStatus(_B)
nodeUserLogout=NotificationType((1,3,6,1,4,1,1369,6,1,2,0,9))
if mibBuilder.loadTexts:nodeUserLogout.setStatus(_B)
nodeStatusNotificationsGroup=NotificationGroup((1,3,6,1,4,1,1369,6,1,3,1,5))
nodeStatusNotificationsGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:nodeStatusNotificationsGroup.setStatus(_B)
nodeLoginNotificationsGroup=NotificationGroup((1,3,6,1,4,1,1369,6,1,3,1,6))
nodeLoginNotificationsGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:nodeLoginNotificationsGroup.setStatus(_B)
nodeTesterNotificationsGroup=NotificationGroup((1,3,6,1,4,1,1369,6,1,3,1,7))
nodeTesterNotificationsGroup.setObjects((_A,_a))
if mibBuilder.loadTexts:nodeTesterNotificationsGroup.setStatus(_B)
nodeHwmonNotificationsGroup=NotificationGroup((1,3,6,1,4,1,1369,6,1,3,1,9))
nodeHwmonNotificationsGroup.setObjects((_A,_b))
if mibBuilder.loadTexts:nodeHwmonNotificationsGroup.setStatus(_B)
nodeCompliance1=ModuleCompliance((1,3,6,1,4,1,1369,6,1,3,2,1))
nodeCompliance1.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:nodeCompliance1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'stonesoftNetworkNodeMibModule':stonesoftNetworkNodeMibModule,'netNodeObjects':netNodeObjects,_K:nodeClusterId,_L:nodeMemberId,_E:nodeOperState,_P:nodeCPULoad,_F:nodeLastLogin,_Q:nodeLastLoginTime,'nodeTestTable':nodeTestTable,'nodeTestEntry':nodeTestEntry,_J:nodeTestIndex,_G:nodeTestIdentity,_R:nodeTestResult,_S:nodeTestResultTime,_H:nodeHwmonEvent,_M:nodeApplianceModel,_N:nodeSerialNumber,_O:nodePosCode,'netNodeEvents':netNodeEvents,'netNodeEventsV2':netNodeEventsV2,_T:nodeOnline,_U:nodeOffline,_V:nodeBoot,_W:nodeShutdown,_X:nodeUserLogin,_a:nodeTestFailure,_b:nodeHwmon,_Y:nodeFailedUserLogin,_Z:nodeUserLogout,'netNodeConformance':netNodeConformance,'netNodeGroups':netNodeGroups,_e:nodeIdentificationGroup,_c:nodeStatusGroup,_f:nodeLoginGroup,_h:nodeTesterGroup,_d:nodeStatusNotificationsGroup,_g:nodeLoginNotificationsGroup,_i:nodeTesterNotificationsGroup,_j:nodeHwmonGroup,_k:nodeHwmonNotificationsGroup,'netNodeCompliances':netNodeCompliances,'nodeCompliance1':nodeCompliance1})