_N='swSDCardMgmtExecFilename'
_M='disabled'
_L='enabled'
_K='swSDCardMgmtBackupFilename'
_J='swSDCardMgmtBackupType'
_I='read-write'
_H='not-accessible'
_G='swTimeRangeMgmtRangeName'
_F='TIMERANGE-MIB'
_E='SDCARDMGMT-MIB'
_D='DisplayString'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention','TruthValue')
swTimeRangeMgmtRangeName,=mibBuilder.importSymbols(_F,_G)
swSDCardMgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,12,95))
_SwSDCardMgmtNotifications_ObjectIdentity=ObjectIdentity
swSDCardMgmtNotifications=_SwSDCardMgmtNotifications_ObjectIdentity((1,3,6,1,4,1,171,12,95,0))
_SwSDCardMgmtMIBObjects_ObjectIdentity=ObjectIdentity
swSDCardMgmtMIBObjects=_SwSDCardMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,12,95,1))
_SwSDCardMgmtGeneralGroup_ObjectIdentity=ObjectIdentity
swSDCardMgmtGeneralGroup=_SwSDCardMgmtGeneralGroup_ObjectIdentity((1,3,6,1,4,1,171,12,95,1,1))
_SwSDCardMgmtBackupCtrl_ObjectIdentity=ObjectIdentity
swSDCardMgmtBackupCtrl=_SwSDCardMgmtBackupCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,95,1,2))
_SwSDCardMgmtBackupCtrlTable_Object=MibTable
swSDCardMgmtBackupCtrlTable=_SwSDCardMgmtBackupCtrlTable_Object((1,3,6,1,4,1,171,12,95,1,2,1))
if mibBuilder.loadTexts:swSDCardMgmtBackupCtrlTable.setStatus(_A)
_SwSDCardMgmtBackupCtrlEntry_Object=MibTableRow
swSDCardMgmtBackupCtrlEntry=_SwSDCardMgmtBackupCtrlEntry_Object((1,3,6,1,4,1,171,12,95,1,2,1,1))
swSDCardMgmtBackupCtrlEntry.setIndexNames((0,_E,_J),(0,_F,_G),(0,_E,_K))
if mibBuilder.loadTexts:swSDCardMgmtBackupCtrlEntry.setStatus(_A)
class _SwSDCardMgmtBackupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('configuration',1),('log',2)))
_SwSDCardMgmtBackupType_Type.__name__=_B
_SwSDCardMgmtBackupType_Object=MibTableColumn
swSDCardMgmtBackupType=_SwSDCardMgmtBackupType_Object((1,3,6,1,4,1,171,12,95,1,2,1,1,1),_SwSDCardMgmtBackupType_Type())
swSDCardMgmtBackupType.setMaxAccess(_H)
if mibBuilder.loadTexts:swSDCardMgmtBackupType.setStatus(_A)
class _SwSDCardMgmtBackupFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwSDCardMgmtBackupFilename_Type.__name__=_D
_SwSDCardMgmtBackupFilename_Object=MibTableColumn
swSDCardMgmtBackupFilename=_SwSDCardMgmtBackupFilename_Object((1,3,6,1,4,1,171,12,95,1,2,1,1,2),_SwSDCardMgmtBackupFilename_Type())
swSDCardMgmtBackupFilename.setMaxAccess(_H)
if mibBuilder.loadTexts:swSDCardMgmtBackupFilename.setStatus(_A)
class _SwSDCardMgmtBackupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SwSDCardMgmtBackupState_Type.__name__=_B
_SwSDCardMgmtBackupState_Object=MibTableColumn
swSDCardMgmtBackupState=_SwSDCardMgmtBackupState_Object((1,3,6,1,4,1,171,12,95,1,2,1,1,3),_SwSDCardMgmtBackupState_Type())
swSDCardMgmtBackupState.setMaxAccess(_C)
if mibBuilder.loadTexts:swSDCardMgmtBackupState.setStatus(_A)
_SwSDCardMgmtBackupRowStatus_Type=RowStatus
_SwSDCardMgmtBackupRowStatus_Object=MibTableColumn
swSDCardMgmtBackupRowStatus=_SwSDCardMgmtBackupRowStatus_Object((1,3,6,1,4,1,171,12,95,1,2,1,1,100),_SwSDCardMgmtBackupRowStatus_Type())
swSDCardMgmtBackupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swSDCardMgmtBackupRowStatus.setStatus(_A)
_SwSDCardMgmtExecCtrl_ObjectIdentity=ObjectIdentity
swSDCardMgmtExecCtrl=_SwSDCardMgmtExecCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,95,1,3))
_SwSDCardMgmtExecCtrlTable_Object=MibTable
swSDCardMgmtExecCtrlTable=_SwSDCardMgmtExecCtrlTable_Object((1,3,6,1,4,1,171,12,95,1,3,1))
if mibBuilder.loadTexts:swSDCardMgmtExecCtrlTable.setStatus(_A)
_SwSDCardMgmtExecCtrlEntry_Object=MibTableRow
swSDCardMgmtExecCtrlEntry=_SwSDCardMgmtExecCtrlEntry_Object((1,3,6,1,4,1,171,12,95,1,3,1,1))
swSDCardMgmtExecCtrlEntry.setIndexNames((0,_F,_G),(0,_E,_N))
if mibBuilder.loadTexts:swSDCardMgmtExecCtrlEntry.setStatus(_A)
class _SwSDCardMgmtExecFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwSDCardMgmtExecFilename_Type.__name__=_D
_SwSDCardMgmtExecFilename_Object=MibTableColumn
swSDCardMgmtExecFilename=_SwSDCardMgmtExecFilename_Object((1,3,6,1,4,1,171,12,95,1,3,1,1,1),_SwSDCardMgmtExecFilename_Type())
swSDCardMgmtExecFilename.setMaxAccess(_H)
if mibBuilder.loadTexts:swSDCardMgmtExecFilename.setStatus(_A)
class _SwSDCardMgmtExecState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SwSDCardMgmtExecState_Type.__name__=_B
_SwSDCardMgmtExecState_Object=MibTableColumn
swSDCardMgmtExecState=_SwSDCardMgmtExecState_Object((1,3,6,1,4,1,171,12,95,1,3,1,1,2),_SwSDCardMgmtExecState_Type())
swSDCardMgmtExecState.setMaxAccess(_C)
if mibBuilder.loadTexts:swSDCardMgmtExecState.setStatus(_A)
_SwSDCardMgmtExecIncrement_Type=TruthValue
_SwSDCardMgmtExecIncrement_Object=MibTableColumn
swSDCardMgmtExecIncrement=_SwSDCardMgmtExecIncrement_Object((1,3,6,1,4,1,171,12,95,1,3,1,1,3),_SwSDCardMgmtExecIncrement_Type())
swSDCardMgmtExecIncrement.setMaxAccess(_C)
if mibBuilder.loadTexts:swSDCardMgmtExecIncrement.setStatus(_A)
_SwSDCardMgmtExecRowStatus_Type=RowStatus
_SwSDCardMgmtExecRowStatus_Object=MibTableColumn
swSDCardMgmtExecRowStatus=_SwSDCardMgmtExecRowStatus_Object((1,3,6,1,4,1,171,12,95,1,3,1,1,100),_SwSDCardMgmtExecRowStatus_Type())
swSDCardMgmtExecRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swSDCardMgmtExecRowStatus.setStatus(_A)
_SwSDCardMgmtExecConfigCtrl_ObjectIdentity=ObjectIdentity
swSDCardMgmtExecConfigCtrl=_SwSDCardMgmtExecConfigCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,95,1,4))
class _SwSDCardMgmtExecConfigFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwSDCardMgmtExecConfigFilename_Type.__name__=_D
_SwSDCardMgmtExecConfigFilename_Object=MibScalar
swSDCardMgmtExecConfigFilename=_SwSDCardMgmtExecConfigFilename_Object((1,3,6,1,4,1,171,12,95,1,4,1),_SwSDCardMgmtExecConfigFilename_Type())
swSDCardMgmtExecConfigFilename.setMaxAccess(_I)
if mibBuilder.loadTexts:swSDCardMgmtExecConfigFilename.setStatus(_A)
_SwSDCardMgmtExecConfigIncrement_Type=TruthValue
_SwSDCardMgmtExecConfigIncrement_Object=MibScalar
swSDCardMgmtExecConfigIncrement=_SwSDCardMgmtExecConfigIncrement_Object((1,3,6,1,4,1,171,12,95,1,4,2),_SwSDCardMgmtExecConfigIncrement_Type())
swSDCardMgmtExecConfigIncrement.setMaxAccess(_I)
if mibBuilder.loadTexts:swSDCardMgmtExecConfigIncrement.setStatus(_A)
class _SwSDCardMgmtExecConfigAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('start',2)))
_SwSDCardMgmtExecConfigAction_Type.__name__=_B
_SwSDCardMgmtExecConfigAction_Object=MibScalar
swSDCardMgmtExecConfigAction=_SwSDCardMgmtExecConfigAction_Object((1,3,6,1,4,1,171,12,95,1,4,3),_SwSDCardMgmtExecConfigAction_Type())
swSDCardMgmtExecConfigAction.setMaxAccess(_I)
if mibBuilder.loadTexts:swSDCardMgmtExecConfigAction.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'swSDCardMgmtMIB':swSDCardMgmtMIB,'swSDCardMgmtNotifications':swSDCardMgmtNotifications,'swSDCardMgmtMIBObjects':swSDCardMgmtMIBObjects,'swSDCardMgmtGeneralGroup':swSDCardMgmtGeneralGroup,'swSDCardMgmtBackupCtrl':swSDCardMgmtBackupCtrl,'swSDCardMgmtBackupCtrlTable':swSDCardMgmtBackupCtrlTable,'swSDCardMgmtBackupCtrlEntry':swSDCardMgmtBackupCtrlEntry,_J:swSDCardMgmtBackupType,_K:swSDCardMgmtBackupFilename,'swSDCardMgmtBackupState':swSDCardMgmtBackupState,'swSDCardMgmtBackupRowStatus':swSDCardMgmtBackupRowStatus,'swSDCardMgmtExecCtrl':swSDCardMgmtExecCtrl,'swSDCardMgmtExecCtrlTable':swSDCardMgmtExecCtrlTable,'swSDCardMgmtExecCtrlEntry':swSDCardMgmtExecCtrlEntry,_N:swSDCardMgmtExecFilename,'swSDCardMgmtExecState':swSDCardMgmtExecState,'swSDCardMgmtExecIncrement':swSDCardMgmtExecIncrement,'swSDCardMgmtExecRowStatus':swSDCardMgmtExecRowStatus,'swSDCardMgmtExecConfigCtrl':swSDCardMgmtExecConfigCtrl,'swSDCardMgmtExecConfigFilename':swSDCardMgmtExecConfigFilename,'swSDCardMgmtExecConfigIncrement':swSDCardMgmtExecConfigIncrement,'swSDCardMgmtExecConfigAction':swSDCardMgmtExecConfigAction})