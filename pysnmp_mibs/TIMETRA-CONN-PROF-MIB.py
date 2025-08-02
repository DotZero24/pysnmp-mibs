_c='tmnxConnProfVlanGroup'
_b='tmnxConnProfAtmMemberGroup'
_a='tmnxConnProfGroup'
_Z='tmnxConnProfTimeStampGroup'
_Y='tmnxConnProfVlanTblLastChanged'
_X='tmnxConnProfVlanEthTblLastChgd'
_W='tmnxConnProfVlanEthLastChanged'
_V='tmnxConnProfVlanEthRowStatus'
_U='tmnxConnProfVlanEthRangeEnd'
_T='tmnxConnProfVlanDescription'
_S='tmnxConnProfVlanLastChanged'
_R='tmnxConnProfVlanRowStatus'
_Q='tmnxConnProfAtmMemberRowStatus'
_P='tmnxConnProfDescription'
_O='tmnxConnProfLastChanged'
_N='tmnxConnProfRowStatus'
_M='tmnxConnProfAtmMemberTblLastChgd'
_L='tmnxConnProfTblLastChanged'
_K='tmnxConnProfVlanEthRangeStart'
_J='tmnxConnProfAtmMemberEncapValue'
_I='tmnxConnProfVlanId'
_H='tmnxConnProfId'
_G='TItemDescription'
_F='Integer32'
_E='not-accessible'
_D='read-create'
_C='read-only'
_B='TIMETRA-CONN-PROF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TItemDescription,TmnxEncapVal=mibBuilder.importSymbols('TIMETRA-TC-MIB',_G,'TmnxEncapVal')
timetraConnProfMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,75))
if mibBuilder.loadTexts:timetraConnProfMIBModule.setRevisions(('2016-01-01 00:00','2011-02-01 00:00'))
class TmnxConnProfId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8000))
_TmnxConnProfConformance_ObjectIdentity=ObjectIdentity
tmnxConnProfConformance=_TmnxConnProfConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,75))
_TmnxConnProfCompliances_ObjectIdentity=ObjectIdentity
tmnxConnProfCompliances=_TmnxConnProfCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,75,1))
_TmnxConnProfGroups_ObjectIdentity=ObjectIdentity
tmnxConnProfGroups=_TmnxConnProfGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,75,2))
_TmnxConnV9v0Groups_ObjectIdentity=ObjectIdentity
tmnxConnV9v0Groups=_TmnxConnV9v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,75,2,1))
_TmnxConnV14v0Groups_ObjectIdentity=ObjectIdentity
tmnxConnV14v0Groups=_TmnxConnV14v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,75,2,2))
_TmnxConnProfObjs_ObjectIdentity=ObjectIdentity
tmnxConnProfObjs=_TmnxConnProfObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,75))
_TmnxConnProfConfigTimeStamps_ObjectIdentity=ObjectIdentity
tmnxConnProfConfigTimeStamps=_TmnxConnProfConfigTimeStamps_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,75,1))
_TmnxConnProfTblLastChanged_Type=TimeStamp
_TmnxConnProfTblLastChanged_Object=MibScalar
tmnxConnProfTblLastChanged=_TmnxConnProfTblLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,75,1,1),_TmnxConnProfTblLastChanged_Type())
tmnxConnProfTblLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxConnProfTblLastChanged.setStatus(_A)
_TmnxConnProfAtmMemberTblLastChgd_Type=TimeStamp
_TmnxConnProfAtmMemberTblLastChgd_Object=MibScalar
tmnxConnProfAtmMemberTblLastChgd=_TmnxConnProfAtmMemberTblLastChgd_Object((1,3,6,1,4,1,6527,3,1,2,75,1,2),_TmnxConnProfAtmMemberTblLastChgd_Type())
tmnxConnProfAtmMemberTblLastChgd.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxConnProfAtmMemberTblLastChgd.setStatus(_A)
_TmnxConnProfVlanTblLastChanged_Type=TimeStamp
_TmnxConnProfVlanTblLastChanged_Object=MibScalar
tmnxConnProfVlanTblLastChanged=_TmnxConnProfVlanTblLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,75,1,3),_TmnxConnProfVlanTblLastChanged_Type())
tmnxConnProfVlanTblLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxConnProfVlanTblLastChanged.setStatus(_A)
_TmnxConnProfVlanEthTblLastChgd_Type=TimeStamp
_TmnxConnProfVlanEthTblLastChgd_Object=MibScalar
tmnxConnProfVlanEthTblLastChgd=_TmnxConnProfVlanEthTblLastChgd_Object((1,3,6,1,4,1,6527,3,1,2,75,1,4),_TmnxConnProfVlanEthTblLastChgd_Type())
tmnxConnProfVlanEthTblLastChgd.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxConnProfVlanEthTblLastChgd.setStatus(_A)
_TmnxConnProfConfigObjs_ObjectIdentity=ObjectIdentity
tmnxConnProfConfigObjs=_TmnxConnProfConfigObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,75,2))
_TmnxConnProfTable_Object=MibTable
tmnxConnProfTable=_TmnxConnProfTable_Object((1,3,6,1,4,1,6527,3,1,2,75,2,1))
if mibBuilder.loadTexts:tmnxConnProfTable.setStatus(_A)
_TmnxConnProfEntry_Object=MibTableRow
tmnxConnProfEntry=_TmnxConnProfEntry_Object((1,3,6,1,4,1,6527,3,1,2,75,2,1,1))
tmnxConnProfEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:tmnxConnProfEntry.setStatus(_A)
_TmnxConnProfId_Type=TmnxConnProfId
_TmnxConnProfId_Object=MibTableColumn
tmnxConnProfId=_TmnxConnProfId_Object((1,3,6,1,4,1,6527,3,1,2,75,2,1,1,1),_TmnxConnProfId_Type())
tmnxConnProfId.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxConnProfId.setStatus(_A)
_TmnxConnProfRowStatus_Type=RowStatus
_TmnxConnProfRowStatus_Object=MibTableColumn
tmnxConnProfRowStatus=_TmnxConnProfRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,75,2,1,1,2),_TmnxConnProfRowStatus_Type())
tmnxConnProfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxConnProfRowStatus.setStatus(_A)
_TmnxConnProfLastChanged_Type=TimeStamp
_TmnxConnProfLastChanged_Object=MibTableColumn
tmnxConnProfLastChanged=_TmnxConnProfLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,75,2,1,1,3),_TmnxConnProfLastChanged_Type())
tmnxConnProfLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxConnProfLastChanged.setStatus(_A)
class _TmnxConnProfDescription_Type(TItemDescription):defaultValue=OctetString('')
_TmnxConnProfDescription_Type.__name__=_G
_TmnxConnProfDescription_Object=MibTableColumn
tmnxConnProfDescription=_TmnxConnProfDescription_Object((1,3,6,1,4,1,6527,3,1,2,75,2,1,1,4),_TmnxConnProfDescription_Type())
tmnxConnProfDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxConnProfDescription.setStatus(_A)
_TmnxConnProfAtmMemberTable_Object=MibTable
tmnxConnProfAtmMemberTable=_TmnxConnProfAtmMemberTable_Object((1,3,6,1,4,1,6527,3,1,2,75,2,2))
if mibBuilder.loadTexts:tmnxConnProfAtmMemberTable.setStatus(_A)
_TmnxConnProfAtmMemberEntry_Object=MibTableRow
tmnxConnProfAtmMemberEntry=_TmnxConnProfAtmMemberEntry_Object((1,3,6,1,4,1,6527,3,1,2,75,2,2,1))
tmnxConnProfAtmMemberEntry.setIndexNames((0,_B,_H),(0,_B,_J))
if mibBuilder.loadTexts:tmnxConnProfAtmMemberEntry.setStatus(_A)
_TmnxConnProfAtmMemberEncapValue_Type=TmnxEncapVal
_TmnxConnProfAtmMemberEncapValue_Object=MibTableColumn
tmnxConnProfAtmMemberEncapValue=_TmnxConnProfAtmMemberEncapValue_Object((1,3,6,1,4,1,6527,3,1,2,75,2,2,1,1),_TmnxConnProfAtmMemberEncapValue_Type())
tmnxConnProfAtmMemberEncapValue.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxConnProfAtmMemberEncapValue.setStatus(_A)
_TmnxConnProfAtmMemberRowStatus_Type=RowStatus
_TmnxConnProfAtmMemberRowStatus_Object=MibTableColumn
tmnxConnProfAtmMemberRowStatus=_TmnxConnProfAtmMemberRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,75,2,2,1,2),_TmnxConnProfAtmMemberRowStatus_Type())
tmnxConnProfAtmMemberRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxConnProfAtmMemberRowStatus.setStatus(_A)
_TmnxConnProfVlanTable_Object=MibTable
tmnxConnProfVlanTable=_TmnxConnProfVlanTable_Object((1,3,6,1,4,1,6527,3,1,2,75,2,3))
if mibBuilder.loadTexts:tmnxConnProfVlanTable.setStatus(_A)
_TmnxConnProfVlanEntry_Object=MibTableRow
tmnxConnProfVlanEntry=_TmnxConnProfVlanEntry_Object((1,3,6,1,4,1,6527,3,1,2,75,2,3,1))
tmnxConnProfVlanEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:tmnxConnProfVlanEntry.setStatus(_A)
_TmnxConnProfVlanId_Type=TmnxConnProfId
_TmnxConnProfVlanId_Object=MibTableColumn
tmnxConnProfVlanId=_TmnxConnProfVlanId_Object((1,3,6,1,4,1,6527,3,1,2,75,2,3,1,1),_TmnxConnProfVlanId_Type())
tmnxConnProfVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxConnProfVlanId.setStatus(_A)
_TmnxConnProfVlanRowStatus_Type=RowStatus
_TmnxConnProfVlanRowStatus_Object=MibTableColumn
tmnxConnProfVlanRowStatus=_TmnxConnProfVlanRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,75,2,3,1,2),_TmnxConnProfVlanRowStatus_Type())
tmnxConnProfVlanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxConnProfVlanRowStatus.setStatus(_A)
_TmnxConnProfVlanLastChanged_Type=TimeStamp
_TmnxConnProfVlanLastChanged_Object=MibTableColumn
tmnxConnProfVlanLastChanged=_TmnxConnProfVlanLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,75,2,3,1,3),_TmnxConnProfVlanLastChanged_Type())
tmnxConnProfVlanLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxConnProfVlanLastChanged.setStatus(_A)
class _TmnxConnProfVlanDescription_Type(TItemDescription):defaultValue=OctetString('')
_TmnxConnProfVlanDescription_Type.__name__=_G
_TmnxConnProfVlanDescription_Object=MibTableColumn
tmnxConnProfVlanDescription=_TmnxConnProfVlanDescription_Object((1,3,6,1,4,1,6527,3,1,2,75,2,3,1,4),_TmnxConnProfVlanDescription_Type())
tmnxConnProfVlanDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxConnProfVlanDescription.setStatus(_A)
_TmnxConnProfVlanEthTable_Object=MibTable
tmnxConnProfVlanEthTable=_TmnxConnProfVlanEthTable_Object((1,3,6,1,4,1,6527,3,1,2,75,2,4))
if mibBuilder.loadTexts:tmnxConnProfVlanEthTable.setStatus(_A)
_TmnxConnProfVlanEthEntry_Object=MibTableRow
tmnxConnProfVlanEthEntry=_TmnxConnProfVlanEthEntry_Object((1,3,6,1,4,1,6527,3,1,2,75,2,4,1))
tmnxConnProfVlanEthEntry.setIndexNames((0,_B,_I),(0,_B,_K))
if mibBuilder.loadTexts:tmnxConnProfVlanEthEntry.setStatus(_A)
class _TmnxConnProfVlanEthRangeStart_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094))
_TmnxConnProfVlanEthRangeStart_Type.__name__=_F
_TmnxConnProfVlanEthRangeStart_Object=MibTableColumn
tmnxConnProfVlanEthRangeStart=_TmnxConnProfVlanEthRangeStart_Object((1,3,6,1,4,1,6527,3,1,2,75,2,4,1,1),_TmnxConnProfVlanEthRangeStart_Type())
tmnxConnProfVlanEthRangeStart.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxConnProfVlanEthRangeStart.setStatus(_A)
_TmnxConnProfVlanEthRowStatus_Type=RowStatus
_TmnxConnProfVlanEthRowStatus_Object=MibTableColumn
tmnxConnProfVlanEthRowStatus=_TmnxConnProfVlanEthRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,75,2,4,1,2),_TmnxConnProfVlanEthRowStatus_Type())
tmnxConnProfVlanEthRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxConnProfVlanEthRowStatus.setStatus(_A)
class _TmnxConnProfVlanEthRangeEnd_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094))
_TmnxConnProfVlanEthRangeEnd_Type.__name__=_F
_TmnxConnProfVlanEthRangeEnd_Object=MibTableColumn
tmnxConnProfVlanEthRangeEnd=_TmnxConnProfVlanEthRangeEnd_Object((1,3,6,1,4,1,6527,3,1,2,75,2,4,1,3),_TmnxConnProfVlanEthRangeEnd_Type())
tmnxConnProfVlanEthRangeEnd.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxConnProfVlanEthRangeEnd.setStatus(_A)
_TmnxConnProfVlanEthLastChanged_Type=TimeStamp
_TmnxConnProfVlanEthLastChanged_Object=MibTableColumn
tmnxConnProfVlanEthLastChanged=_TmnxConnProfVlanEthLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,75,2,4,1,4),_TmnxConnProfVlanEthLastChanged_Type())
tmnxConnProfVlanEthLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxConnProfVlanEthLastChanged.setStatus(_A)
_TmnxConnProfNtfyPrefix_ObjectIdentity=ObjectIdentity
tmnxConnProfNtfyPrefix=_TmnxConnProfNtfyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,75))
_TmnxConnProfNotifications_ObjectIdentity=ObjectIdentity
tmnxConnProfNotifications=_TmnxConnProfNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,75,0))
tmnxConnProfTimeStampGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,75,2,1,1))
tmnxConnProfTimeStampGroup.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:tmnxConnProfTimeStampGroup.setStatus(_A)
tmnxConnProfGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,75,2,1,2))
tmnxConnProfGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:tmnxConnProfGroup.setStatus(_A)
tmnxConnProfAtmMemberGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,75,2,1,3))
tmnxConnProfAtmMemberGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:tmnxConnProfAtmMemberGroup.setStatus(_A)
tmnxConnProfVlanGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,75,2,2,1))
tmnxConnProfVlanGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:tmnxConnProfVlanGroup.setStatus(_A)
tmnxConnProfV9v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,75,1,1))
tmnxConnProfV9v0Compliance.setObjects(*((_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:tmnxConnProfV9v0Compliance.setStatus(_A)
tmnxConnProfV14v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,75,1,2))
tmnxConnProfV14v0Compliance.setObjects((_B,_c))
if mibBuilder.loadTexts:tmnxConnProfV14v0Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TmnxConnProfId':TmnxConnProfId,'timetraConnProfMIBModule':timetraConnProfMIBModule,'tmnxConnProfConformance':tmnxConnProfConformance,'tmnxConnProfCompliances':tmnxConnProfCompliances,'tmnxConnProfV9v0Compliance':tmnxConnProfV9v0Compliance,'tmnxConnProfV14v0Compliance':tmnxConnProfV14v0Compliance,'tmnxConnProfGroups':tmnxConnProfGroups,'tmnxConnV9v0Groups':tmnxConnV9v0Groups,_Z:tmnxConnProfTimeStampGroup,_a:tmnxConnProfGroup,_b:tmnxConnProfAtmMemberGroup,'tmnxConnV14v0Groups':tmnxConnV14v0Groups,_c:tmnxConnProfVlanGroup,'tmnxConnProfObjs':tmnxConnProfObjs,'tmnxConnProfConfigTimeStamps':tmnxConnProfConfigTimeStamps,_L:tmnxConnProfTblLastChanged,_M:tmnxConnProfAtmMemberTblLastChgd,_Y:tmnxConnProfVlanTblLastChanged,_X:tmnxConnProfVlanEthTblLastChgd,'tmnxConnProfConfigObjs':tmnxConnProfConfigObjs,'tmnxConnProfTable':tmnxConnProfTable,'tmnxConnProfEntry':tmnxConnProfEntry,_H:tmnxConnProfId,_N:tmnxConnProfRowStatus,_O:tmnxConnProfLastChanged,_P:tmnxConnProfDescription,'tmnxConnProfAtmMemberTable':tmnxConnProfAtmMemberTable,'tmnxConnProfAtmMemberEntry':tmnxConnProfAtmMemberEntry,_J:tmnxConnProfAtmMemberEncapValue,_Q:tmnxConnProfAtmMemberRowStatus,'tmnxConnProfVlanTable':tmnxConnProfVlanTable,'tmnxConnProfVlanEntry':tmnxConnProfVlanEntry,_I:tmnxConnProfVlanId,_R:tmnxConnProfVlanRowStatus,_S:tmnxConnProfVlanLastChanged,_T:tmnxConnProfVlanDescription,'tmnxConnProfVlanEthTable':tmnxConnProfVlanEthTable,'tmnxConnProfVlanEthEntry':tmnxConnProfVlanEthEntry,_K:tmnxConnProfVlanEthRangeStart,_V:tmnxConnProfVlanEthRowStatus,_U:tmnxConnProfVlanEthRangeEnd,_W:tmnxConnProfVlanEthLastChanged,'tmnxConnProfNtfyPrefix':tmnxConnProfNtfyPrefix,'tmnxConnProfNotifications':tmnxConnProfNotifications})