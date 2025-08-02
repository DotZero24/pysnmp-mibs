_E='ntcExObjectIndex'
_D='ntcExGroupIndex'
_C='SVRNTCLU-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mgmt')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class ObjectType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('objectUnknown',1),('objectOther',2),('share',3),('disk',4),('application',5),('ipAddress',6),('fileShare',7)))
class PolicyType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('policyUnknown',1),('policyOther',2),('inOrder',3),('random',4),('leastLoad',5),('roundRobin',6)))
class Boolean(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
class DateAndTime(DisplayString):0
class FailoverReason(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('reasonUnknown',1),('reasonOther',2),('reconfiguration',3),('failure',4),('failback',5)))
_Dec_ObjectIdentity=ObjectIdentity
dec=_Dec_ObjectIdentity((1,3,6,1,4,1,36))
_Ema_ObjectIdentity=ObjectIdentity
ema=_Ema_ObjectIdentity((1,3,6,1,4,1,36,2))
_Mib_extensions_1_ObjectIdentity=ObjectIdentity
mib_extensions_1=_Mib_extensions_1_ObjectIdentity((1,3,6,1,4,1,36,2,18))
_SvrSystem_ObjectIdentity=ObjectIdentity
svrSystem=_SvrSystem_ObjectIdentity((1,3,6,1,4,1,36,2,18,22))
_SvrCluster_ObjectIdentity=ObjectIdentity
svrCluster=_SvrCluster_ObjectIdentity((1,3,6,1,4,1,36,2,18,22,4))
_SvrNTClu_ObjectIdentity=ObjectIdentity
svrNTClu=_SvrNTClu_ObjectIdentity((1,3,6,1,4,1,36,2,18,22,4,2))
_SvrNTCluObjects_ObjectIdentity=ObjectIdentity
svrNTCluObjects=_SvrNTCluObjects_ObjectIdentity((1,3,6,1,4,1,36,2,18,22,4,2,1))
_SvrNTCluMibInfo_ObjectIdentity=ObjectIdentity
svrNTCluMibInfo=_SvrNTCluMibInfo_ObjectIdentity((1,3,6,1,4,1,36,2,18,22,4,2,1,1))
_NtcExMgtMibMajorRev_Type=Integer32
_NtcExMgtMibMajorRev_Object=MibScalar
ntcExMgtMibMajorRev=_NtcExMgtMibMajorRev_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,1,1),_NtcExMgtMibMajorRev_Type())
ntcExMgtMibMajorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExMgtMibMajorRev.setStatus(_A)
_NtcExMgtMibMinorRev_Type=Integer32
_NtcExMgtMibMinorRev_Object=MibScalar
ntcExMgtMibMinorRev=_NtcExMgtMibMinorRev_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,1,2),_NtcExMgtMibMinorRev_Type())
ntcExMgtMibMinorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExMgtMibMinorRev.setStatus(_A)
_SvrNTCluClusterInfo_ObjectIdentity=ObjectIdentity
svrNTCluClusterInfo=_SvrNTCluClusterInfo_ObjectIdentity((1,3,6,1,4,1,36,2,18,22,4,2,1,2))
_NtcExAlias_Type=DisplayString
_NtcExAlias_Object=MibScalar
ntcExAlias=_NtcExAlias_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,1),_NtcExAlias_Type())
ntcExAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExAlias.setStatus(_A)
_NtcExGroupTable_Object=MibTable
ntcExGroupTable=_NtcExGroupTable_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,7))
if mibBuilder.loadTexts:ntcExGroupTable.setStatus(_A)
_NtcExGroupEntry_Object=MibTableRow
ntcExGroupEntry=_NtcExGroupEntry_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,7,1))
ntcExGroupEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ntcExGroupEntry.setStatus(_A)
_NtcExGroupIndex_Type=Integer32
_NtcExGroupIndex_Object=MibTableColumn
ntcExGroupIndex=_NtcExGroupIndex_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,7,1,1),_NtcExGroupIndex_Type())
ntcExGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExGroupIndex.setStatus(_A)
_NtcExGroupName_Type=DisplayString
_NtcExGroupName_Object=MibTableColumn
ntcExGroupName=_NtcExGroupName_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,7,1,2),_NtcExGroupName_Type())
ntcExGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExGroupName.setStatus(_A)
_NtcExGroupComment_Type=DisplayString
_NtcExGroupComment_Object=MibTableColumn
ntcExGroupComment=_NtcExGroupComment_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,7,1,3),_NtcExGroupComment_Type())
ntcExGroupComment.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExGroupComment.setStatus(_A)
_NtcExGroupOnLine_Type=Integer32
_NtcExGroupOnLine_Object=MibTableColumn
ntcExGroupOnLine=_NtcExGroupOnLine_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,7,1,4),_NtcExGroupOnLine_Type())
ntcExGroupOnLine.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExGroupOnLine.setStatus(_A)
_NtcExGroupFailedOver_Type=Boolean
_NtcExGroupFailedOver_Object=MibTableColumn
ntcExGroupFailedOver=_NtcExGroupFailedOver_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,7,1,5),_NtcExGroupFailedOver_Type())
ntcExGroupFailedOver.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExGroupFailedOver.setStatus(_A)
_NtcExGroupPolicy_Type=PolicyType
_NtcExGroupPolicy_Object=MibTableColumn
ntcExGroupPolicy=_NtcExGroupPolicy_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,7,1,6),_NtcExGroupPolicy_Type())
ntcExGroupPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExGroupPolicy.setStatus(_A)
_NtcExGroupReevaluate_Type=Boolean
_NtcExGroupReevaluate_Object=MibTableColumn
ntcExGroupReevaluate=_NtcExGroupReevaluate_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,7,1,7),_NtcExGroupReevaluate_Type())
ntcExGroupReevaluate.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExGroupReevaluate.setStatus(_A)
_NtcExGroupMembers_Type=DisplayString
_NtcExGroupMembers_Object=MibTableColumn
ntcExGroupMembers=_NtcExGroupMembers_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,7,1,8),_NtcExGroupMembers_Type())
ntcExGroupMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExGroupMembers.setStatus(_A)
_NtcExGroupObjects_Type=DisplayString
_NtcExGroupObjects_Object=MibTableColumn
ntcExGroupObjects=_NtcExGroupObjects_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,7,1,9),_NtcExGroupObjects_Type())
ntcExGroupObjects.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExGroupObjects.setStatus(_A)
_NtcExObjectTable_Object=MibTable
ntcExObjectTable=_NtcExObjectTable_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,8))
if mibBuilder.loadTexts:ntcExObjectTable.setStatus(_A)
_NtcExObjectEntry_Object=MibTableRow
ntcExObjectEntry=_NtcExObjectEntry_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,8,1))
ntcExObjectEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:ntcExObjectEntry.setStatus(_A)
_NtcExObjectIndex_Type=Integer32
_NtcExObjectIndex_Object=MibTableColumn
ntcExObjectIndex=_NtcExObjectIndex_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,8,1,1),_NtcExObjectIndex_Type())
ntcExObjectIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExObjectIndex.setStatus(_A)
_NtcExObjectName_Type=DisplayString
_NtcExObjectName_Object=MibTableColumn
ntcExObjectName=_NtcExObjectName_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,8,1,2),_NtcExObjectName_Type())
ntcExObjectName.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExObjectName.setStatus(_A)
_NtcExObjectComment_Type=DisplayString
_NtcExObjectComment_Object=MibTableColumn
ntcExObjectComment=_NtcExObjectComment_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,8,1,3),_NtcExObjectComment_Type())
ntcExObjectComment.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExObjectComment.setStatus(_A)
_NtcExObjectType_Type=ObjectType
_NtcExObjectType_Object=MibTableColumn
ntcExObjectType=_NtcExObjectType_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,8,1,4),_NtcExObjectType_Type())
ntcExObjectType.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExObjectType.setStatus(_A)
_NtcExObjectDrives_Type=DisplayString
_NtcExObjectDrives_Object=MibTableColumn
ntcExObjectDrives=_NtcExObjectDrives_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,8,1,5),_NtcExObjectDrives_Type())
ntcExObjectDrives.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExObjectDrives.setStatus(_A)
_NtcExObjectIpAddress_Type=IpAddress
_NtcExObjectIpAddress_Object=MibTableColumn
ntcExObjectIpAddress=_NtcExObjectIpAddress_Object((1,3,6,1,4,1,36,2,18,22,4,2,1,2,8,1,6),_NtcExObjectIpAddress_Type())
ntcExObjectIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ntcExObjectIpAddress.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ObjectType':ObjectType,'PolicyType':PolicyType,'Boolean':Boolean,'DateAndTime':DateAndTime,'FailoverReason':FailoverReason,'dec':dec,'ema':ema,'mib-extensions-1':mib_extensions_1,'svrSystem':svrSystem,'svrCluster':svrCluster,'svrNTClu':svrNTClu,'svrNTCluObjects':svrNTCluObjects,'svrNTCluMibInfo':svrNTCluMibInfo,'ntcExMgtMibMajorRev':ntcExMgtMibMajorRev,'ntcExMgtMibMinorRev':ntcExMgtMibMinorRev,'svrNTCluClusterInfo':svrNTCluClusterInfo,'ntcExAlias':ntcExAlias,'ntcExGroupTable':ntcExGroupTable,'ntcExGroupEntry':ntcExGroupEntry,_D:ntcExGroupIndex,'ntcExGroupName':ntcExGroupName,'ntcExGroupComment':ntcExGroupComment,'ntcExGroupOnLine':ntcExGroupOnLine,'ntcExGroupFailedOver':ntcExGroupFailedOver,'ntcExGroupPolicy':ntcExGroupPolicy,'ntcExGroupReevaluate':ntcExGroupReevaluate,'ntcExGroupMembers':ntcExGroupMembers,'ntcExGroupObjects':ntcExGroupObjects,'ntcExObjectTable':ntcExObjectTable,'ntcExObjectEntry':ntcExObjectEntry,_E:ntcExObjectIndex,'ntcExObjectName':ntcExObjectName,'ntcExObjectComment':ntcExObjectComment,'ntcExObjectType':ntcExObjectType,'ntcExObjectDrives':ntcExObjectDrives,'ntcExObjectIpAddress':ntcExObjectIpAddress})