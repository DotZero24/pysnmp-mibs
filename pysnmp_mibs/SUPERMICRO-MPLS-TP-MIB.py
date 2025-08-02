_J='fsMplsTpNodeMapLocalNum'
_I='not-accessible'
_H='TruthValue'
_G='DisplayString'
_F='fsMplsTpContextId'
_E='Integer32'
_D='SUPERMICRO-MPLS-TP-MIB'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention',_H)
fsMplsTpMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,13,8))
if mibBuilder.loadTexts:fsMplsTpMIB.setRevisions(('2012-09-05 00:00',))
_FsMplsTpNotifications_ObjectIdentity=ObjectIdentity
fsMplsTpNotifications=_FsMplsTpNotifications_ObjectIdentity((1,3,6,1,4,1,10876,101,1,13,8,0))
_FsMplsTpObjects_ObjectIdentity=ObjectIdentity
fsMplsTpObjects=_FsMplsTpObjects_ObjectIdentity((1,3,6,1,4,1,10876,101,1,13,8,1))
_FsMplsTpScalarObjects_ObjectIdentity=ObjectIdentity
fsMplsTpScalarObjects=_FsMplsTpScalarObjects_ObjectIdentity((1,3,6,1,4,1,10876,101,1,13,8,1,1))
_FsMplsTpGlobalConfigTable_Object=MibTable
fsMplsTpGlobalConfigTable=_FsMplsTpGlobalConfigTable_Object((1,3,6,1,4,1,10876,101,1,13,8,1,2))
if mibBuilder.loadTexts:fsMplsTpGlobalConfigTable.setStatus(_A)
_FsMplsTpGlobalConfigEntry_Object=MibTableRow
fsMplsTpGlobalConfigEntry=_FsMplsTpGlobalConfigEntry_Object((1,3,6,1,4,1,10876,101,1,13,8,1,2,1))
fsMplsTpGlobalConfigEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:fsMplsTpGlobalConfigEntry.setStatus(_A)
_FsMplsTpContextId_Type=Unsigned32
_FsMplsTpContextId_Object=MibTableColumn
fsMplsTpContextId=_FsMplsTpContextId_Object((1,3,6,1,4,1,10876,101,1,13,8,1,2,1,1),_FsMplsTpContextId_Type())
fsMplsTpContextId.setMaxAccess(_I)
if mibBuilder.loadTexts:fsMplsTpContextId.setStatus(_A)
class _FsMplsTpOamModuleStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsMplsTpOamModuleStatus_Type.__name__=_E
_FsMplsTpOamModuleStatus_Object=MibTableColumn
fsMplsTpOamModuleStatus=_FsMplsTpOamModuleStatus_Object((1,3,6,1,4,1,10876,101,1,13,8,1,2,1,2),_FsMplsTpOamModuleStatus_Type())
fsMplsTpOamModuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpOamModuleStatus.setStatus(_A)
class _FsMplsTpGlobalId_Type(Unsigned32):defaultValue=0
_FsMplsTpGlobalId_Type.__name__=_C
_FsMplsTpGlobalId_Object=MibTableColumn
fsMplsTpGlobalId=_FsMplsTpGlobalId_Object((1,3,6,1,4,1,10876,101,1,13,8,1,2,1,3),_FsMplsTpGlobalId_Type())
fsMplsTpGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpGlobalId.setStatus(_A)
class _FsMplsTpIcc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_FsMplsTpIcc_Type.__name__=_G
_FsMplsTpIcc_Object=MibTableColumn
fsMplsTpIcc=_FsMplsTpIcc_Object((1,3,6,1,4,1,10876,101,1,13,8,1,2,1,4),_FsMplsTpIcc_Type())
fsMplsTpIcc.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpIcc.setStatus(_A)
class _FsMplsTpNodeIdentifier_Type(Unsigned32):defaultValue=0
_FsMplsTpNodeIdentifier_Type.__name__=_C
_FsMplsTpNodeIdentifier_Object=MibTableColumn
fsMplsTpNodeIdentifier=_FsMplsTpNodeIdentifier_Object((1,3,6,1,4,1,10876,101,1,13,8,1,2,1,5),_FsMplsTpNodeIdentifier_Type())
fsMplsTpNodeIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpNodeIdentifier.setStatus(_A)
class _FsMplsTpErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('elpsAssociationExists',1),('megAssociationExists',2),('pseudowireAssociationExists',3),('proactiveSessionExists',4),('elpsProactiveSessionExists',5),('activeMeExists',6)))
_FsMplsTpErrorCode_Type.__name__=_E
_FsMplsTpErrorCode_Object=MibTableColumn
fsMplsTpErrorCode=_FsMplsTpErrorCode_Object((1,3,6,1,4,1,10876,101,1,13,8,1,2,1,6),_FsMplsTpErrorCode_Type())
fsMplsTpErrorCode.setMaxAccess('read-only')
if mibBuilder.loadTexts:fsMplsTpErrorCode.setStatus(_A)
class _FsMplsTpTraceLevel_Type(Unsigned32):defaultValue=0
_FsMplsTpTraceLevel_Type.__name__=_C
_FsMplsTpTraceLevel_Object=MibTableColumn
fsMplsTpTraceLevel=_FsMplsTpTraceLevel_Object((1,3,6,1,4,1,10876,101,1,13,8,1,2,1,7),_FsMplsTpTraceLevel_Type())
fsMplsTpTraceLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpTraceLevel.setStatus(_A)
class _FsMplsTpNotificationEnable_Type(TruthValue):defaultValue=2
_FsMplsTpNotificationEnable_Type.__name__=_H
_FsMplsTpNotificationEnable_Object=MibTableColumn
fsMplsTpNotificationEnable=_FsMplsTpNotificationEnable_Object((1,3,6,1,4,1,10876,101,1,13,8,1,2,1,8),_FsMplsTpNotificationEnable_Type())
fsMplsTpNotificationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpNotificationEnable.setStatus(_A)
_FsMplsTpNodeMapTable_Object=MibTable
fsMplsTpNodeMapTable=_FsMplsTpNodeMapTable_Object((1,3,6,1,4,1,10876,101,1,13,8,1,3))
if mibBuilder.loadTexts:fsMplsTpNodeMapTable.setStatus(_A)
_FsMplsTpNodeMapEntry_Object=MibTableRow
fsMplsTpNodeMapEntry=_FsMplsTpNodeMapEntry_Object((1,3,6,1,4,1,10876,101,1,13,8,1,3,1))
fsMplsTpNodeMapEntry.setIndexNames((0,_D,_F),(0,_D,_J))
if mibBuilder.loadTexts:fsMplsTpNodeMapEntry.setStatus(_A)
_FsMplsTpNodeMapLocalNum_Type=Unsigned32
_FsMplsTpNodeMapLocalNum_Object=MibTableColumn
fsMplsTpNodeMapLocalNum=_FsMplsTpNodeMapLocalNum_Object((1,3,6,1,4,1,10876,101,1,13,8,1,3,1,1),_FsMplsTpNodeMapLocalNum_Type())
fsMplsTpNodeMapLocalNum.setMaxAccess(_I)
if mibBuilder.loadTexts:fsMplsTpNodeMapLocalNum.setStatus(_A)
_FsMplsTpNodeMapGlobalId_Type=Unsigned32
_FsMplsTpNodeMapGlobalId_Object=MibTableColumn
fsMplsTpNodeMapGlobalId=_FsMplsTpNodeMapGlobalId_Object((1,3,6,1,4,1,10876,101,1,13,8,1,3,1,2),_FsMplsTpNodeMapGlobalId_Type())
fsMplsTpNodeMapGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpNodeMapGlobalId.setStatus(_A)
_FsMplsTpNodeMapNodeId_Type=Unsigned32
_FsMplsTpNodeMapNodeId_Object=MibTableColumn
fsMplsTpNodeMapNodeId=_FsMplsTpNodeMapNodeId_Object((1,3,6,1,4,1,10876,101,1,13,8,1,3,1,3),_FsMplsTpNodeMapNodeId_Type())
fsMplsTpNodeMapNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpNodeMapNodeId.setStatus(_A)
_FsMplsTpNodeMapRowStatus_Type=RowStatus
_FsMplsTpNodeMapRowStatus_Object=MibTableColumn
fsMplsTpNodeMapRowStatus=_FsMplsTpNodeMapRowStatus_Object((1,3,6,1,4,1,10876,101,1,13,8,1,3,1,4),_FsMplsTpNodeMapRowStatus_Type())
fsMplsTpNodeMapRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsMplsTpNodeMapRowStatus.setStatus(_A)
_FsMplsTpConformance_ObjectIdentity=ObjectIdentity
fsMplsTpConformance=_FsMplsTpConformance_ObjectIdentity((1,3,6,1,4,1,10876,101,1,13,8,2))
mibBuilder.exportSymbols(_D,**{'fsMplsTpMIB':fsMplsTpMIB,'fsMplsTpNotifications':fsMplsTpNotifications,'fsMplsTpObjects':fsMplsTpObjects,'fsMplsTpScalarObjects':fsMplsTpScalarObjects,'fsMplsTpGlobalConfigTable':fsMplsTpGlobalConfigTable,'fsMplsTpGlobalConfigEntry':fsMplsTpGlobalConfigEntry,_F:fsMplsTpContextId,'fsMplsTpOamModuleStatus':fsMplsTpOamModuleStatus,'fsMplsTpGlobalId':fsMplsTpGlobalId,'fsMplsTpIcc':fsMplsTpIcc,'fsMplsTpNodeIdentifier':fsMplsTpNodeIdentifier,'fsMplsTpErrorCode':fsMplsTpErrorCode,'fsMplsTpTraceLevel':fsMplsTpTraceLevel,'fsMplsTpNotificationEnable':fsMplsTpNotificationEnable,'fsMplsTpNodeMapTable':fsMplsTpNodeMapTable,'fsMplsTpNodeMapEntry':fsMplsTpNodeMapEntry,_J:fsMplsTpNodeMapLocalNum,'fsMplsTpNodeMapGlobalId':fsMplsTpNodeMapGlobalId,'fsMplsTpNodeMapNodeId':fsMplsTpNodeMapNodeId,'fsMplsTpNodeMapRowStatus':fsMplsTpNodeMapRowStatus,'fsMplsTpConformance':fsMplsTpConformance})