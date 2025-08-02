_P='cie1000UsersConfigTableRowEditorInfoGroup'
_O='cie1000UsersConfigTableInfoGroup'
_N='cie1000UsersConfigTableRowEditorAction'
_M='cie1000UsersConfigTableRowEditorPassword'
_L='cie1000UsersConfigTableRowEditorEncrypted'
_K='cie1000UsersConfigTableRowEditorPrivilege'
_J='cie1000UsersConfigTableRowEditorUsername'
_I='cie1000UsersConfigAction'
_H='cie1000UsersConfigPassword'
_G='cie1000UsersConfigEncrypted'
_F='cie1000UsersConfigPrivilege'
_E='cie1000UsersConfigUsername'
_D='CIE1000DisplayString'
_C='read-write'
_B='CIE1000-USERS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CIE1000DisplayString,CIE1000RowEditorState=mibBuilder.importSymbols('CIE1000-TC',_D,'CIE1000RowEditorState')
cie1000SwitchMgmt,=mibBuilder.importSymbols('CISCO-IE1000-MIB','cie1000SwitchMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cie1000UsersMib=ModuleIdentity((1,3,6,1,4,1,9,9,832,1,58))
if mibBuilder.loadTexts:cie1000UsersMib.setRevisions(('2016-01-19 00:00','2014-07-01 00:00'))
_Cie1000UsersMibObjects_ObjectIdentity=ObjectIdentity
cie1000UsersMibObjects=_Cie1000UsersMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,58,1))
_Cie1000UsersConfig_ObjectIdentity=ObjectIdentity
cie1000UsersConfig=_Cie1000UsersConfig_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,58,1,2))
_Cie1000UsersConfigTable_Object=MibTable
cie1000UsersConfigTable=_Cie1000UsersConfigTable_Object((1,3,6,1,4,1,9,9,832,1,58,1,2,1))
if mibBuilder.loadTexts:cie1000UsersConfigTable.setStatus(_A)
_Cie1000UsersConfigEntry_Object=MibTableRow
cie1000UsersConfigEntry=_Cie1000UsersConfigEntry_Object((1,3,6,1,4,1,9,9,832,1,58,1,2,1,1))
cie1000UsersConfigEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cie1000UsersConfigEntry.setStatus(_A)
class _Cie1000UsersConfigUsername_Type(CIE1000DisplayString):subtypeSpec=CIE1000DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_Cie1000UsersConfigUsername_Type.__name__=_D
_Cie1000UsersConfigUsername_Object=MibTableColumn
cie1000UsersConfigUsername=_Cie1000UsersConfigUsername_Object((1,3,6,1,4,1,9,9,832,1,58,1,2,1,1,1),_Cie1000UsersConfigUsername_Type())
cie1000UsersConfigUsername.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:cie1000UsersConfigUsername.setStatus(_A)
_Cie1000UsersConfigPrivilege_Type=Unsigned32
_Cie1000UsersConfigPrivilege_Object=MibTableColumn
cie1000UsersConfigPrivilege=_Cie1000UsersConfigPrivilege_Object((1,3,6,1,4,1,9,9,832,1,58,1,2,1,1,2),_Cie1000UsersConfigPrivilege_Type())
cie1000UsersConfigPrivilege.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000UsersConfigPrivilege.setStatus(_A)
_Cie1000UsersConfigEncrypted_Type=TruthValue
_Cie1000UsersConfigEncrypted_Object=MibTableColumn
cie1000UsersConfigEncrypted=_Cie1000UsersConfigEncrypted_Object((1,3,6,1,4,1,9,9,832,1,58,1,2,1,1,3),_Cie1000UsersConfigEncrypted_Type())
cie1000UsersConfigEncrypted.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000UsersConfigEncrypted.setStatus(_A)
class _Cie1000UsersConfigPassword_Type(CIE1000DisplayString):subtypeSpec=CIE1000DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Cie1000UsersConfigPassword_Type.__name__=_D
_Cie1000UsersConfigPassword_Object=MibTableColumn
cie1000UsersConfigPassword=_Cie1000UsersConfigPassword_Object((1,3,6,1,4,1,9,9,832,1,58,1,2,1,1,4),_Cie1000UsersConfigPassword_Type())
cie1000UsersConfigPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000UsersConfigPassword.setStatus(_A)
_Cie1000UsersConfigAction_Type=CIE1000RowEditorState
_Cie1000UsersConfigAction_Object=MibTableColumn
cie1000UsersConfigAction=_Cie1000UsersConfigAction_Object((1,3,6,1,4,1,9,9,832,1,58,1,2,1,1,100),_Cie1000UsersConfigAction_Type())
cie1000UsersConfigAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000UsersConfigAction.setStatus(_A)
_Cie1000UsersConfigTableRowEditor_ObjectIdentity=ObjectIdentity
cie1000UsersConfigTableRowEditor=_Cie1000UsersConfigTableRowEditor_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,58,1,2,2))
class _Cie1000UsersConfigTableRowEditorUsername_Type(CIE1000DisplayString):subtypeSpec=CIE1000DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_Cie1000UsersConfigTableRowEditorUsername_Type.__name__=_D
_Cie1000UsersConfigTableRowEditorUsername_Object=MibScalar
cie1000UsersConfigTableRowEditorUsername=_Cie1000UsersConfigTableRowEditorUsername_Object((1,3,6,1,4,1,9,9,832,1,58,1,2,2,1),_Cie1000UsersConfigTableRowEditorUsername_Type())
cie1000UsersConfigTableRowEditorUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000UsersConfigTableRowEditorUsername.setStatus(_A)
_Cie1000UsersConfigTableRowEditorPrivilege_Type=Unsigned32
_Cie1000UsersConfigTableRowEditorPrivilege_Object=MibScalar
cie1000UsersConfigTableRowEditorPrivilege=_Cie1000UsersConfigTableRowEditorPrivilege_Object((1,3,6,1,4,1,9,9,832,1,58,1,2,2,2),_Cie1000UsersConfigTableRowEditorPrivilege_Type())
cie1000UsersConfigTableRowEditorPrivilege.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000UsersConfigTableRowEditorPrivilege.setStatus(_A)
_Cie1000UsersConfigTableRowEditorEncrypted_Type=TruthValue
_Cie1000UsersConfigTableRowEditorEncrypted_Object=MibScalar
cie1000UsersConfigTableRowEditorEncrypted=_Cie1000UsersConfigTableRowEditorEncrypted_Object((1,3,6,1,4,1,9,9,832,1,58,1,2,2,3),_Cie1000UsersConfigTableRowEditorEncrypted_Type())
cie1000UsersConfigTableRowEditorEncrypted.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000UsersConfigTableRowEditorEncrypted.setStatus(_A)
class _Cie1000UsersConfigTableRowEditorPassword_Type(CIE1000DisplayString):subtypeSpec=CIE1000DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Cie1000UsersConfigTableRowEditorPassword_Type.__name__=_D
_Cie1000UsersConfigTableRowEditorPassword_Object=MibScalar
cie1000UsersConfigTableRowEditorPassword=_Cie1000UsersConfigTableRowEditorPassword_Object((1,3,6,1,4,1,9,9,832,1,58,1,2,2,4),_Cie1000UsersConfigTableRowEditorPassword_Type())
cie1000UsersConfigTableRowEditorPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000UsersConfigTableRowEditorPassword.setStatus(_A)
_Cie1000UsersConfigTableRowEditorAction_Type=CIE1000RowEditorState
_Cie1000UsersConfigTableRowEditorAction_Object=MibScalar
cie1000UsersConfigTableRowEditorAction=_Cie1000UsersConfigTableRowEditorAction_Object((1,3,6,1,4,1,9,9,832,1,58,1,2,2,100),_Cie1000UsersConfigTableRowEditorAction_Type())
cie1000UsersConfigTableRowEditorAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000UsersConfigTableRowEditorAction.setStatus(_A)
_Cie1000UsersMibConformance_ObjectIdentity=ObjectIdentity
cie1000UsersMibConformance=_Cie1000UsersMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,58,2))
_Cie1000UsersMibCompliances_ObjectIdentity=ObjectIdentity
cie1000UsersMibCompliances=_Cie1000UsersMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,58,2,1))
_Cie1000UsersMibGroups_ObjectIdentity=ObjectIdentity
cie1000UsersMibGroups=_Cie1000UsersMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,58,2,2))
cie1000UsersConfigTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,58,2,2,1))
cie1000UsersConfigTableInfoGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:cie1000UsersConfigTableInfoGroup.setStatus(_A)
cie1000UsersConfigTableRowEditorInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,58,2,2,2))
cie1000UsersConfigTableRowEditorInfoGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cie1000UsersConfigTableRowEditorInfoGroup.setStatus(_A)
cie1000UsersMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,832,1,58,2,1,1))
cie1000UsersMibCompliance.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:cie1000UsersMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cie1000UsersMib':cie1000UsersMib,'cie1000UsersMibObjects':cie1000UsersMibObjects,'cie1000UsersConfig':cie1000UsersConfig,'cie1000UsersConfigTable':cie1000UsersConfigTable,'cie1000UsersConfigEntry':cie1000UsersConfigEntry,_E:cie1000UsersConfigUsername,_F:cie1000UsersConfigPrivilege,_G:cie1000UsersConfigEncrypted,_H:cie1000UsersConfigPassword,_I:cie1000UsersConfigAction,'cie1000UsersConfigTableRowEditor':cie1000UsersConfigTableRowEditor,_J:cie1000UsersConfigTableRowEditorUsername,_K:cie1000UsersConfigTableRowEditorPrivilege,_L:cie1000UsersConfigTableRowEditorEncrypted,_M:cie1000UsersConfigTableRowEditorPassword,_N:cie1000UsersConfigTableRowEditorAction,'cie1000UsersMibConformance':cie1000UsersMibConformance,'cie1000UsersMibCompliances':cie1000UsersMibCompliances,'cie1000UsersMibCompliance':cie1000UsersMibCompliance,'cie1000UsersMibGroups':cie1000UsersMibGroups,_O:cie1000UsersConfigTableInfoGroup,_P:cie1000UsersConfigTableRowEditorInfoGroup})