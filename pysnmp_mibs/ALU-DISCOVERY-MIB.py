_e='aluDiscoveryNotificationGroup'
_d='aluDiscoveryGroup'
_c='aluDiscoverySuccessful'
_b='aluDiscoveryTerminated'
_a='aluDiscoveryStarted'
_Z='aluSbiAutoDiscoverVlan'
_Y='aluSbiAutoDiscoverId'
_X='aluSbiAutoDiscover'
_W='aluDiscoveryServerIpAddr'
_V='aluDiscoveryGatewayRemId'
_U='aluDiscoveryLocalSubnet'
_T='aluDiscoverySystemSubnet'
_S='aluDiscoveryEndTime'
_R='aluDiscoveryStartTime'
_Q='aluDiscoveryStage'
_P='aluDiscoveryStatus'
_O='tmnxChassisIndex'
_N='TIMETRA-CHASSIS-MIB'
_M='TruthValue'
_L='DisplayString'
_K='Unsigned32'
_J='aluDiscoveryFailureFlags'
_I='aluDiscoveryGatewayIpAddr'
_H='aluDiscoveryGatewayCircId'
_G='aluDiscoveryLocalIpAddr'
_F='aluDiscoveryLocalCircId'
_E='aluDiscoverySystemIpAddr'
_D='read-write'
_C='read-only'
_B='ALU-DISCOVERY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_M)
tmnxChassisIndex,tmnxChassisNotifyHwIndex=mibBuilder.importSymbols(_N,_O,'tmnxChassisNotifyHwIndex')
alcatelCommonMIBModules,alcatelConformance,alcatelNotifyPrefix,alcatelObjects=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','alcatelCommonMIBModules','alcatelConformance','alcatelNotifyPrefix','alcatelObjects')
aluDiscoveryMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,5,4))
if mibBuilder.loadTexts:aluDiscoveryMIBModule.setRevisions(('1909-01-18 00:00',))
class AluDiscoveryStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,5)));namedValues=NamedValues(*(('noAutoDiscovery',0),('inProgress',1),('halted',2),('terminated',4),('successful',5)))
class AluDiscoveryStage(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('unknown',0),('selfDiscovery',1),('aquiringNetwork',2),('aquiringConfig',3),('testAndCommitConfig',4)))
class AluDiscoveryCircuitId(DisplayString):status=_A
class AluDiscoveryFailureFlags(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('configConflict',0),('eqNotReady',1),('noPortsReady',2),('noNetworkFound',3),('ipRequestFailed',4),('portSelectFailed',5),('configLoadingProblem',6),('configTestingFailed',7),('configCommitProblem',8)))
_AluDiscoveryMIBConformance_ObjectIdentity=ObjectIdentity
aluDiscoveryMIBConformance=_AluDiscoveryMIBConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,3,1,4))
_AluDiscoveryConformance_ObjectIdentity=ObjectIdentity
aluDiscoveryConformance=_AluDiscoveryConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,3,1,4,1))
_AluDiscoveryCompliances_ObjectIdentity=ObjectIdentity
aluDiscoveryCompliances=_AluDiscoveryCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,3,1,4,1,1))
_AluDiscoveryComp7705_ObjectIdentity=ObjectIdentity
aluDiscoveryComp7705=_AluDiscoveryComp7705_ObjectIdentity((1,3,6,1,4,1,6527,3,3,1,4,1,1,1))
_AluDiscoveryGroups_ObjectIdentity=ObjectIdentity
aluDiscoveryGroups=_AluDiscoveryGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,3,1,4,1,2))
_AluDiscoveryObjs_ObjectIdentity=ObjectIdentity
aluDiscoveryObjs=_AluDiscoveryObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,3,2,4))
_AluDiscoveryTable_Object=MibTable
aluDiscoveryTable=_AluDiscoveryTable_Object((1,3,6,1,4,1,6527,3,3,2,4,1))
if mibBuilder.loadTexts:aluDiscoveryTable.setStatus(_A)
_AluDiscoveryEntry_Object=MibTableRow
aluDiscoveryEntry=_AluDiscoveryEntry_Object((1,3,6,1,4,1,6527,3,3,2,4,1,1))
aluDiscoveryEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:aluDiscoveryEntry.setStatus(_A)
_AluDiscoveryStatus_Type=AluDiscoveryStatus
_AluDiscoveryStatus_Object=MibTableColumn
aluDiscoveryStatus=_AluDiscoveryStatus_Object((1,3,6,1,4,1,6527,3,3,2,4,1,1,1),_AluDiscoveryStatus_Type())
aluDiscoveryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aluDiscoveryStatus.setStatus(_A)
_AluDiscoveryStage_Type=AluDiscoveryStage
_AluDiscoveryStage_Object=MibTableColumn
aluDiscoveryStage=_AluDiscoveryStage_Object((1,3,6,1,4,1,6527,3,3,2,4,1,1,2),_AluDiscoveryStage_Type())
aluDiscoveryStage.setMaxAccess(_C)
if mibBuilder.loadTexts:aluDiscoveryStage.setStatus(_A)
_AluDiscoveryStartTime_Type=TimeStamp
_AluDiscoveryStartTime_Object=MibTableColumn
aluDiscoveryStartTime=_AluDiscoveryStartTime_Object((1,3,6,1,4,1,6527,3,3,2,4,1,1,3),_AluDiscoveryStartTime_Type())
aluDiscoveryStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aluDiscoveryStartTime.setStatus(_A)
_AluDiscoveryEndTime_Type=TimeStamp
_AluDiscoveryEndTime_Object=MibTableColumn
aluDiscoveryEndTime=_AluDiscoveryEndTime_Object((1,3,6,1,4,1,6527,3,3,2,4,1,1,4),_AluDiscoveryEndTime_Type())
aluDiscoveryEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aluDiscoveryEndTime.setStatus(_A)
_AluDiscoverySystemIpAddr_Type=IpAddress
_AluDiscoverySystemIpAddr_Object=MibTableColumn
aluDiscoverySystemIpAddr=_AluDiscoverySystemIpAddr_Object((1,3,6,1,4,1,6527,3,3,2,4,1,1,5),_AluDiscoverySystemIpAddr_Type())
aluDiscoverySystemIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:aluDiscoverySystemIpAddr.setStatus(_A)
_AluDiscoverySystemSubnet_Type=IpAddress
_AluDiscoverySystemSubnet_Object=MibTableColumn
aluDiscoverySystemSubnet=_AluDiscoverySystemSubnet_Object((1,3,6,1,4,1,6527,3,3,2,4,1,1,6),_AluDiscoverySystemSubnet_Type())
aluDiscoverySystemSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:aluDiscoverySystemSubnet.setStatus(_A)
_AluDiscoveryLocalCircId_Type=AluDiscoveryCircuitId
_AluDiscoveryLocalCircId_Object=MibTableColumn
aluDiscoveryLocalCircId=_AluDiscoveryLocalCircId_Object((1,3,6,1,4,1,6527,3,3,2,4,1,1,7),_AluDiscoveryLocalCircId_Type())
aluDiscoveryLocalCircId.setMaxAccess(_C)
if mibBuilder.loadTexts:aluDiscoveryLocalCircId.setStatus(_A)
_AluDiscoveryLocalIpAddr_Type=IpAddress
_AluDiscoveryLocalIpAddr_Object=MibTableColumn
aluDiscoveryLocalIpAddr=_AluDiscoveryLocalIpAddr_Object((1,3,6,1,4,1,6527,3,3,2,4,1,1,8),_AluDiscoveryLocalIpAddr_Type())
aluDiscoveryLocalIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:aluDiscoveryLocalIpAddr.setStatus(_A)
_AluDiscoveryLocalSubnet_Type=IpAddress
_AluDiscoveryLocalSubnet_Object=MibTableColumn
aluDiscoveryLocalSubnet=_AluDiscoveryLocalSubnet_Object((1,3,6,1,4,1,6527,3,3,2,4,1,1,9),_AluDiscoveryLocalSubnet_Type())
aluDiscoveryLocalSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:aluDiscoveryLocalSubnet.setStatus(_A)
_AluDiscoveryGatewayCircId_Type=AluDiscoveryCircuitId
_AluDiscoveryGatewayCircId_Object=MibTableColumn
aluDiscoveryGatewayCircId=_AluDiscoveryGatewayCircId_Object((1,3,6,1,4,1,6527,3,3,2,4,1,1,10),_AluDiscoveryGatewayCircId_Type())
aluDiscoveryGatewayCircId.setMaxAccess(_C)
if mibBuilder.loadTexts:aluDiscoveryGatewayCircId.setStatus(_A)
_AluDiscoveryGatewayRemId_Type=DisplayString
_AluDiscoveryGatewayRemId_Object=MibTableColumn
aluDiscoveryGatewayRemId=_AluDiscoveryGatewayRemId_Object((1,3,6,1,4,1,6527,3,3,2,4,1,1,11),_AluDiscoveryGatewayRemId_Type())
aluDiscoveryGatewayRemId.setMaxAccess(_C)
if mibBuilder.loadTexts:aluDiscoveryGatewayRemId.setStatus(_A)
_AluDiscoveryGatewayIpAddr_Type=IpAddress
_AluDiscoveryGatewayIpAddr_Object=MibTableColumn
aluDiscoveryGatewayIpAddr=_AluDiscoveryGatewayIpAddr_Object((1,3,6,1,4,1,6527,3,3,2,4,1,1,12),_AluDiscoveryGatewayIpAddr_Type())
aluDiscoveryGatewayIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:aluDiscoveryGatewayIpAddr.setStatus(_A)
_AluDiscoveryServerIpAddr_Type=IpAddress
_AluDiscoveryServerIpAddr_Object=MibTableColumn
aluDiscoveryServerIpAddr=_AluDiscoveryServerIpAddr_Object((1,3,6,1,4,1,6527,3,3,2,4,1,1,13),_AluDiscoveryServerIpAddr_Type())
aluDiscoveryServerIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:aluDiscoveryServerIpAddr.setStatus(_A)
_AluDiscoveryFailureFlags_Type=AluDiscoveryFailureFlags
_AluDiscoveryFailureFlags_Object=MibTableColumn
aluDiscoveryFailureFlags=_AluDiscoveryFailureFlags_Object((1,3,6,1,4,1,6527,3,3,2,4,1,1,14),_AluDiscoveryFailureFlags_Type())
aluDiscoveryFailureFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:aluDiscoveryFailureFlags.setStatus(_A)
_AluDiscoveryBofInfo_ObjectIdentity=ObjectIdentity
aluDiscoveryBofInfo=_AluDiscoveryBofInfo_ObjectIdentity((1,3,6,1,4,1,6527,3,3,2,4,2))
class _AluSbiAutoDiscover_Type(TruthValue):defaultValue=2
_AluSbiAutoDiscover_Type.__name__=_M
_AluSbiAutoDiscover_Object=MibScalar
aluSbiAutoDiscover=_AluSbiAutoDiscover_Object((1,3,6,1,4,1,6527,3,3,2,4,2,1),_AluSbiAutoDiscover_Type())
aluSbiAutoDiscover.setMaxAccess(_D)
if mibBuilder.loadTexts:aluSbiAutoDiscover.setStatus(_A)
class _AluSbiAutoDiscoverId_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_AluSbiAutoDiscoverId_Type.__name__=_L
_AluSbiAutoDiscoverId_Object=MibScalar
aluSbiAutoDiscoverId=_AluSbiAutoDiscoverId_Object((1,3,6,1,4,1,6527,3,3,2,4,2,2),_AluSbiAutoDiscoverId_Type())
aluSbiAutoDiscoverId.setMaxAccess(_D)
if mibBuilder.loadTexts:aluSbiAutoDiscoverId.setStatus(_A)
class _AluSbiAutoDiscoverVlan_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_AluSbiAutoDiscoverVlan_Type.__name__=_K
_AluSbiAutoDiscoverVlan_Object=MibScalar
aluSbiAutoDiscoverVlan=_AluSbiAutoDiscoverVlan_Object((1,3,6,1,4,1,6527,3,3,2,4,2,3),_AluSbiAutoDiscoverVlan_Type())
aluSbiAutoDiscoverVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:aluSbiAutoDiscoverVlan.setStatus(_A)
_AluDiscoveryNotificationsPrefix_ObjectIdentity=ObjectIdentity
aluDiscoveryNotificationsPrefix=_AluDiscoveryNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,3,3,4))
_AluDiscoveryNotifications_ObjectIdentity=ObjectIdentity
aluDiscoveryNotifications=_AluDiscoveryNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,3,3,4,0))
aluDiscoveryGroup=ObjectGroup((1,3,6,1,4,1,6527,3,3,1,4,1,2,1))
aluDiscoveryGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_E),(_B,_T),(_B,_F),(_B,_G),(_B,_U),(_B,_H),(_B,_V),(_B,_I),(_B,_W),(_B,_J),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:aluDiscoveryGroup.setStatus(_A)
aluDiscoveryStarted=NotificationType((1,3,6,1,4,1,6527,3,3,3,4,0,1))
if mibBuilder.loadTexts:aluDiscoveryStarted.setStatus(_A)
aluDiscoveryTerminated=NotificationType((1,3,6,1,4,1,6527,3,3,3,4,0,2))
aluDiscoveryTerminated.setObjects((_B,_J))
if mibBuilder.loadTexts:aluDiscoveryTerminated.setStatus(_A)
aluDiscoverySuccessful=NotificationType((1,3,6,1,4,1,6527,3,3,3,4,0,3))
aluDiscoverySuccessful.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:aluDiscoverySuccessful.setStatus(_A)
aluDiscoveryNotificationGroup=NotificationGroup((1,3,6,1,4,1,6527,3,3,1,4,1,2,2))
aluDiscoveryNotificationGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:aluDiscoveryNotificationGroup.setStatus(_A)
aluDiscoveryComp7705V1v0=ModuleCompliance((1,3,6,1,4,1,6527,3,3,1,4,1,1,1,1))
aluDiscoveryComp7705V1v0.setObjects(*((_B,_d),(_B,_e)))
if mibBuilder.loadTexts:aluDiscoveryComp7705V1v0.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AluDiscoveryStatus':AluDiscoveryStatus,'AluDiscoveryStage':AluDiscoveryStage,'AluDiscoveryCircuitId':AluDiscoveryCircuitId,'AluDiscoveryFailureFlags':AluDiscoveryFailureFlags,'aluDiscoveryMIBModule':aluDiscoveryMIBModule,'aluDiscoveryMIBConformance':aluDiscoveryMIBConformance,'aluDiscoveryConformance':aluDiscoveryConformance,'aluDiscoveryCompliances':aluDiscoveryCompliances,'aluDiscoveryComp7705':aluDiscoveryComp7705,'aluDiscoveryComp7705V1v0':aluDiscoveryComp7705V1v0,'aluDiscoveryGroups':aluDiscoveryGroups,_d:aluDiscoveryGroup,_e:aluDiscoveryNotificationGroup,'aluDiscoveryObjs':aluDiscoveryObjs,'aluDiscoveryTable':aluDiscoveryTable,'aluDiscoveryEntry':aluDiscoveryEntry,_P:aluDiscoveryStatus,_Q:aluDiscoveryStage,_R:aluDiscoveryStartTime,_S:aluDiscoveryEndTime,_E:aluDiscoverySystemIpAddr,_T:aluDiscoverySystemSubnet,_F:aluDiscoveryLocalCircId,_G:aluDiscoveryLocalIpAddr,_U:aluDiscoveryLocalSubnet,_H:aluDiscoveryGatewayCircId,_V:aluDiscoveryGatewayRemId,_I:aluDiscoveryGatewayIpAddr,_W:aluDiscoveryServerIpAddr,_J:aluDiscoveryFailureFlags,'aluDiscoveryBofInfo':aluDiscoveryBofInfo,_X:aluSbiAutoDiscover,_Y:aluSbiAutoDiscoverId,_Z:aluSbiAutoDiscoverVlan,'aluDiscoveryNotificationsPrefix':aluDiscoveryNotificationsPrefix,'aluDiscoveryNotifications':aluDiscoveryNotifications,_a:aluDiscoveryStarted,_b:aluDiscoveryTerminated,_c:aluDiscoverySuccessful})