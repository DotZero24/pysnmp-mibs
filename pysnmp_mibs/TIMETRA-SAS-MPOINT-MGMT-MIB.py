_Z='tSASMpGlobalGroup'
_Y='tSASMpBwPlcyQueMgmtPlcy'
_X='tSASMpBwPlcyPirAdaptation'
_W='tSASMpBwPlcyCirAdaptation'
_V='tSASMpBwPlcyPir'
_U='tSASMpBwPlcyCir'
_T='tSASMpBwPlcyMbs'
_S='tSASMpBwPlcyCbs'
_R='tSASMpBwPlcyIngrAggrRate'
_Q='tSASMpBwPlcyDescription'
_P='tSASMpBwPlcyLastChanged'
_O='tSASMpBwPlcyRowStatus'
_N='percent'
_M='tSASMpBwPlcyQueueId'
_L='not-accessible'
_K='TNamedItem'
_J='TItemDescription'
_I='TBurstSize'
_H='tSASMpBwPlcyName'
_G='TAdaptationRule'
_F='Unsigned32'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='TIMETRA-SAS-MPOINT-MGMT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
timetraSASConfs,timetraSASModules,timetraSASNotifyPrefix,timetraSASObjs=mibBuilder.importSymbols('TIMETRA-SAS-GLOBAL-MIB','timetraSASConfs','timetraSASModules','timetraSASNotifyPrefix','timetraSASObjs')
TAdaptationRule,TBurstSize=mibBuilder.importSymbols('TIMETRA-SAS-QOS-MIB',_G,_I)
TItemDescription,TNamedItem=mibBuilder.importSymbols('TIMETRA-TC-MIB',_J,_K)
timetraSASMpointMgmtMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,2,1,1,54))
if mibBuilder.loadTexts:timetraSASMpointMgmtMIBModule.setRevisions(('1910-05-10 00:00',))
class TSASMpQueueIdTc(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('none',0),('queue1',1),('queue2',2),('queue3',3),('queue4',4),('queue5',5),('queue6',6),('queue7',7),('queue8',8)))
_TSASMpConformance_ObjectIdentity=ObjectIdentity
tSASMpConformance=_TSASMpConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,54))
_TSASMpCompliances_ObjectIdentity=ObjectIdentity
tSASMpCompliances=_TSASMpCompliances_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,54,1))
_TSASMpGroups_ObjectIdentity=ObjectIdentity
tSASMpGroups=_TSASMpGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,54,2))
_TSASMpObjects_ObjectIdentity=ObjectIdentity
tSASMpObjects=_TSASMpObjects_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,54))
_TSASMpGlobalObjs_ObjectIdentity=ObjectIdentity
tSASMpGlobalObjs=_TSASMpGlobalObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,54,1))
_TSASMpBwPlcyTable_Object=MibTable
tSASMpBwPlcyTable=_TSASMpBwPlcyTable_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,1))
if mibBuilder.loadTexts:tSASMpBwPlcyTable.setStatus(_A)
_TSASMpBwPlcyEntry_Object=MibTableRow
tSASMpBwPlcyEntry=_TSASMpBwPlcyEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,1,1))
tSASMpBwPlcyEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:tSASMpBwPlcyEntry.setStatus(_A)
_TSASMpBwPlcyName_Type=TNamedItem
_TSASMpBwPlcyName_Object=MibTableColumn
tSASMpBwPlcyName=_TSASMpBwPlcyName_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,1,1,1),_TSASMpBwPlcyName_Type())
tSASMpBwPlcyName.setMaxAccess(_L)
if mibBuilder.loadTexts:tSASMpBwPlcyName.setStatus(_A)
_TSASMpBwPlcyRowStatus_Type=RowStatus
_TSASMpBwPlcyRowStatus_Object=MibTableColumn
tSASMpBwPlcyRowStatus=_TSASMpBwPlcyRowStatus_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,1,1,2),_TSASMpBwPlcyRowStatus_Type())
tSASMpBwPlcyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tSASMpBwPlcyRowStatus.setStatus(_A)
_TSASMpBwPlcyLastChanged_Type=TimeStamp
_TSASMpBwPlcyLastChanged_Object=MibTableColumn
tSASMpBwPlcyLastChanged=_TSASMpBwPlcyLastChanged_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,1,1,3),_TSASMpBwPlcyLastChanged_Type())
tSASMpBwPlcyLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:tSASMpBwPlcyLastChanged.setStatus(_A)
class _TSASMpBwPlcyDescription_Type(TItemDescription):defaultValue=OctetString('')
_TSASMpBwPlcyDescription_Type.__name__=_J
_TSASMpBwPlcyDescription_Object=MibTableColumn
tSASMpBwPlcyDescription=_TSASMpBwPlcyDescription_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,1,1,4),_TSASMpBwPlcyDescription_Type())
tSASMpBwPlcyDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tSASMpBwPlcyDescription.setStatus(_A)
class _TSASMpBwPlcyIngrAggrRate_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,10000))
_TSASMpBwPlcyIngrAggrRate_Type.__name__=_E
_TSASMpBwPlcyIngrAggrRate_Object=MibTableColumn
tSASMpBwPlcyIngrAggrRate=_TSASMpBwPlcyIngrAggrRate_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,1,1,5),_TSASMpBwPlcyIngrAggrRate_Type())
tSASMpBwPlcyIngrAggrRate.setMaxAccess(_C)
if mibBuilder.loadTexts:tSASMpBwPlcyIngrAggrRate.setStatus(_A)
if mibBuilder.loadTexts:tSASMpBwPlcyIngrAggrRate.setUnits('mega-bits-per-second')
_TSASMpBwPlcyQueueTable_Object=MibTable
tSASMpBwPlcyQueueTable=_TSASMpBwPlcyQueueTable_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,2))
if mibBuilder.loadTexts:tSASMpBwPlcyQueueTable.setStatus(_A)
_TSASMpBwPlcyQueueEntry_Object=MibTableRow
tSASMpBwPlcyQueueEntry=_TSASMpBwPlcyQueueEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,2,1))
tSASMpBwPlcyQueueEntry.setIndexNames((0,_B,_H),(0,_B,_M))
if mibBuilder.loadTexts:tSASMpBwPlcyQueueEntry.setStatus(_A)
_TSASMpBwPlcyQueueId_Type=TSASMpQueueIdTc
_TSASMpBwPlcyQueueId_Object=MibTableColumn
tSASMpBwPlcyQueueId=_TSASMpBwPlcyQueueId_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,2,1,1),_TSASMpBwPlcyQueueId_Type())
tSASMpBwPlcyQueueId.setMaxAccess(_L)
if mibBuilder.loadTexts:tSASMpBwPlcyQueueId.setStatus(_A)
class _TSASMpBwPlcyCbs_Type(TBurstSize):defaultValue=-1
_TSASMpBwPlcyCbs_Type.__name__=_I
_TSASMpBwPlcyCbs_Object=MibTableColumn
tSASMpBwPlcyCbs=_TSASMpBwPlcyCbs_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,2,1,2),_TSASMpBwPlcyCbs_Type())
tSASMpBwPlcyCbs.setMaxAccess(_C)
if mibBuilder.loadTexts:tSASMpBwPlcyCbs.setStatus(_A)
class _TSASMpBwPlcyMbs_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,131072))
_TSASMpBwPlcyMbs_Type.__name__=_E
_TSASMpBwPlcyMbs_Object=MibTableColumn
tSASMpBwPlcyMbs=_TSASMpBwPlcyMbs_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,2,1,3),_TSASMpBwPlcyMbs_Type())
tSASMpBwPlcyMbs.setMaxAccess(_C)
if mibBuilder.loadTexts:tSASMpBwPlcyMbs.setStatus(_A)
class _TSASMpBwPlcyCir_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TSASMpBwPlcyCir_Type.__name__=_F
_TSASMpBwPlcyCir_Object=MibTableColumn
tSASMpBwPlcyCir=_TSASMpBwPlcyCir_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,2,1,4),_TSASMpBwPlcyCir_Type())
tSASMpBwPlcyCir.setMaxAccess(_C)
if mibBuilder.loadTexts:tSASMpBwPlcyCir.setStatus(_A)
if mibBuilder.loadTexts:tSASMpBwPlcyCir.setUnits(_N)
class _TSASMpBwPlcyPir_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_TSASMpBwPlcyPir_Type.__name__=_F
_TSASMpBwPlcyPir_Object=MibTableColumn
tSASMpBwPlcyPir=_TSASMpBwPlcyPir_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,2,1,5),_TSASMpBwPlcyPir_Type())
tSASMpBwPlcyPir.setMaxAccess(_C)
if mibBuilder.loadTexts:tSASMpBwPlcyPir.setStatus(_A)
if mibBuilder.loadTexts:tSASMpBwPlcyPir.setUnits(_N)
class _TSASMpBwPlcyCirAdaptation_Type(TAdaptationRule):defaultValue=3
_TSASMpBwPlcyCirAdaptation_Type.__name__=_G
_TSASMpBwPlcyCirAdaptation_Object=MibTableColumn
tSASMpBwPlcyCirAdaptation=_TSASMpBwPlcyCirAdaptation_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,2,1,6),_TSASMpBwPlcyCirAdaptation_Type())
tSASMpBwPlcyCirAdaptation.setMaxAccess(_C)
if mibBuilder.loadTexts:tSASMpBwPlcyCirAdaptation.setStatus(_A)
class _TSASMpBwPlcyPirAdaptation_Type(TAdaptationRule):defaultValue=3
_TSASMpBwPlcyPirAdaptation_Type.__name__=_G
_TSASMpBwPlcyPirAdaptation_Object=MibTableColumn
tSASMpBwPlcyPirAdaptation=_TSASMpBwPlcyPirAdaptation_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,2,1,7),_TSASMpBwPlcyPirAdaptation_Type())
tSASMpBwPlcyPirAdaptation.setMaxAccess(_C)
if mibBuilder.loadTexts:tSASMpBwPlcyPirAdaptation.setStatus(_A)
class _TSASMpBwPlcyQueMgmtPlcy_Type(TNamedItem):defaultValue=OctetString('default')
_TSASMpBwPlcyQueMgmtPlcy_Type.__name__=_K
_TSASMpBwPlcyQueMgmtPlcy_Object=MibTableColumn
tSASMpBwPlcyQueMgmtPlcy=_TSASMpBwPlcyQueMgmtPlcy_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,2,1,8),_TSASMpBwPlcyQueMgmtPlcy_Type())
tSASMpBwPlcyQueMgmtPlcy.setMaxAccess(_C)
if mibBuilder.loadTexts:tSASMpBwPlcyQueMgmtPlcy.setStatus(_A)
_TSASMpBwPlcyQueStatsFwdPkts_Type=Counter64
_TSASMpBwPlcyQueStatsFwdPkts_Object=MibTableColumn
tSASMpBwPlcyQueStatsFwdPkts=_TSASMpBwPlcyQueStatsFwdPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,2,1,9),_TSASMpBwPlcyQueStatsFwdPkts_Type())
tSASMpBwPlcyQueStatsFwdPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:tSASMpBwPlcyQueStatsFwdPkts.setStatus(_A)
_TSASMpBwPlcyQueStatsFwdOcts_Type=Counter64
_TSASMpBwPlcyQueStatsFwdOcts_Object=MibTableColumn
tSASMpBwPlcyQueStatsFwdOcts=_TSASMpBwPlcyQueStatsFwdOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,2,1,10),_TSASMpBwPlcyQueStatsFwdOcts_Type())
tSASMpBwPlcyQueStatsFwdOcts.setMaxAccess(_D)
if mibBuilder.loadTexts:tSASMpBwPlcyQueStatsFwdOcts.setStatus(_A)
_TSASMpBwPlcyQueStatsDroPkts_Type=Counter64
_TSASMpBwPlcyQueStatsDroPkts_Object=MibTableColumn
tSASMpBwPlcyQueStatsDroPkts=_TSASMpBwPlcyQueStatsDroPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,2,1,11),_TSASMpBwPlcyQueStatsDroPkts_Type())
tSASMpBwPlcyQueStatsDroPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:tSASMpBwPlcyQueStatsDroPkts.setStatus(_A)
_TSASMpBwPlcyQueStatsDroOcts_Type=Counter64
_TSASMpBwPlcyQueStatsDroOcts_Object=MibTableColumn
tSASMpBwPlcyQueStatsDroOcts=_TSASMpBwPlcyQueStatsDroOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,54,1,2,1,12),_TSASMpBwPlcyQueStatsDroOcts_Type())
tSASMpBwPlcyQueStatsDroOcts.setMaxAccess(_D)
if mibBuilder.loadTexts:tSASMpBwPlcyQueStatsDroOcts.setStatus(_A)
_TSASMpNotifyObjs_ObjectIdentity=ObjectIdentity
tSASMpNotifyObjs=_TSASMpNotifyObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,54,2))
_TSASMpNotifyPrefix_ObjectIdentity=ObjectIdentity
tSASMpNotifyPrefix=_TSASMpNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,3,54))
_TSASMpNotifications_ObjectIdentity=ObjectIdentity
tSASMpNotifications=_TSASMpNotifications_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,3,54,0))
tSASMpGlobalGroup=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,54,2,1))
tSASMpGlobalGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:tSASMpGlobalGroup.setStatus(_A)
tSASMp7210V1v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,6,2,2,1,54,1,1))
tSASMp7210V1v0Compliance.setObjects((_B,_Z))
if mibBuilder.loadTexts:tSASMp7210V1v0Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TSASMpQueueIdTc':TSASMpQueueIdTc,'timetraSASMpointMgmtMIBModule':timetraSASMpointMgmtMIBModule,'tSASMpConformance':tSASMpConformance,'tSASMpCompliances':tSASMpCompliances,'tSASMp7210V1v0Compliance':tSASMp7210V1v0Compliance,'tSASMpGroups':tSASMpGroups,_Z:tSASMpGlobalGroup,'tSASMpObjects':tSASMpObjects,'tSASMpGlobalObjs':tSASMpGlobalObjs,'tSASMpBwPlcyTable':tSASMpBwPlcyTable,'tSASMpBwPlcyEntry':tSASMpBwPlcyEntry,_H:tSASMpBwPlcyName,_O:tSASMpBwPlcyRowStatus,_P:tSASMpBwPlcyLastChanged,_Q:tSASMpBwPlcyDescription,_R:tSASMpBwPlcyIngrAggrRate,'tSASMpBwPlcyQueueTable':tSASMpBwPlcyQueueTable,'tSASMpBwPlcyQueueEntry':tSASMpBwPlcyQueueEntry,_M:tSASMpBwPlcyQueueId,_S:tSASMpBwPlcyCbs,_T:tSASMpBwPlcyMbs,_U:tSASMpBwPlcyCir,_V:tSASMpBwPlcyPir,_W:tSASMpBwPlcyCirAdaptation,_X:tSASMpBwPlcyPirAdaptation,_Y:tSASMpBwPlcyQueMgmtPlcy,'tSASMpBwPlcyQueStatsFwdPkts':tSASMpBwPlcyQueStatsFwdPkts,'tSASMpBwPlcyQueStatsFwdOcts':tSASMpBwPlcyQueStatsFwdOcts,'tSASMpBwPlcyQueStatsDroPkts':tSASMpBwPlcyQueStatsDroPkts,'tSASMpBwPlcyQueStatsDroOcts':tSASMpBwPlcyQueStatsDroOcts,'tSASMpNotifyObjs':tSASMpNotifyObjs,'tSASMpNotifyPrefix':tSASMpNotifyPrefix,'tSASMpNotifications':tSASMpNotifications})