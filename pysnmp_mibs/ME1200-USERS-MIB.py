_P='me1200UsersConfigTableRowEditorInfoGroup'
_O='me1200UsersConfigTableInfoGroup'
_N='me1200UsersConfigTableRowEditorAction'
_M='me1200UsersConfigTableRowEditorPassword'
_L='me1200UsersConfigTableRowEditorEncrypted'
_K='me1200UsersConfigTableRowEditorPrivilege'
_J='me1200UsersConfigTableRowEditorUsername'
_I='me1200UsersConfigAction'
_H='me1200UsersConfigPassword'
_G='me1200UsersConfigEncrypted'
_F='me1200UsersConfigPrivilege'
_E='me1200UsersConfigUsername'
_D='ME1200DisplayString'
_C='read-write'
_B='ME1200-USERS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
me1200SwitchMgmt,=mibBuilder.importSymbols('CISCOME1200-MIB','me1200SwitchMgmt')
ME1200DisplayString,ME1200RowEditorState=mibBuilder.importSymbols('ME1200-TC',_D,'ME1200RowEditorState')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
me1200UsersMIB=ModuleIdentity((1,3,6,1,4,1,9,9,815,1,58))
if mibBuilder.loadTexts:me1200UsersMIB.setRevisions(('2014-01-29 00:00','2014-01-22 00:00','2013-12-11 00:00'))
_Me1200UsersMIBObjects_ObjectIdentity=ObjectIdentity
me1200UsersMIBObjects=_Me1200UsersMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,58,1))
_Me1200UsersConfig_ObjectIdentity=ObjectIdentity
me1200UsersConfig=_Me1200UsersConfig_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,58,1,2))
_Me1200UsersConfigTable_Object=MibTable
me1200UsersConfigTable=_Me1200UsersConfigTable_Object((1,3,6,1,4,1,9,9,815,1,58,1,2,1))
if mibBuilder.loadTexts:me1200UsersConfigTable.setStatus(_A)
_Me1200UsersConfigEntry_Object=MibTableRow
me1200UsersConfigEntry=_Me1200UsersConfigEntry_Object((1,3,6,1,4,1,9,9,815,1,58,1,2,1,1))
me1200UsersConfigEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:me1200UsersConfigEntry.setStatus(_A)
class _Me1200UsersConfigUsername_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_Me1200UsersConfigUsername_Type.__name__=_D
_Me1200UsersConfigUsername_Object=MibTableColumn
me1200UsersConfigUsername=_Me1200UsersConfigUsername_Object((1,3,6,1,4,1,9,9,815,1,58,1,2,1,1,1),_Me1200UsersConfigUsername_Type())
me1200UsersConfigUsername.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:me1200UsersConfigUsername.setStatus(_A)
_Me1200UsersConfigPrivilege_Type=Unsigned32
_Me1200UsersConfigPrivilege_Object=MibTableColumn
me1200UsersConfigPrivilege=_Me1200UsersConfigPrivilege_Object((1,3,6,1,4,1,9,9,815,1,58,1,2,1,1,2),_Me1200UsersConfigPrivilege_Type())
me1200UsersConfigPrivilege.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UsersConfigPrivilege.setStatus(_A)
_Me1200UsersConfigEncrypted_Type=TruthValue
_Me1200UsersConfigEncrypted_Object=MibTableColumn
me1200UsersConfigEncrypted=_Me1200UsersConfigEncrypted_Object((1,3,6,1,4,1,9,9,815,1,58,1,2,1,1,3),_Me1200UsersConfigEncrypted_Type())
me1200UsersConfigEncrypted.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UsersConfigEncrypted.setStatus(_A)
class _Me1200UsersConfigPassword_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,44))
_Me1200UsersConfigPassword_Type.__name__=_D
_Me1200UsersConfigPassword_Object=MibTableColumn
me1200UsersConfigPassword=_Me1200UsersConfigPassword_Object((1,3,6,1,4,1,9,9,815,1,58,1,2,1,1,4),_Me1200UsersConfigPassword_Type())
me1200UsersConfigPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UsersConfigPassword.setStatus(_A)
_Me1200UsersConfigAction_Type=ME1200RowEditorState
_Me1200UsersConfigAction_Object=MibTableColumn
me1200UsersConfigAction=_Me1200UsersConfigAction_Object((1,3,6,1,4,1,9,9,815,1,58,1,2,1,1,100),_Me1200UsersConfigAction_Type())
me1200UsersConfigAction.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UsersConfigAction.setStatus(_A)
_Me1200UsersConfigTableRowEditor_ObjectIdentity=ObjectIdentity
me1200UsersConfigTableRowEditor=_Me1200UsersConfigTableRowEditor_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,58,1,2,2))
class _Me1200UsersConfigTableRowEditorUsername_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_Me1200UsersConfigTableRowEditorUsername_Type.__name__=_D
_Me1200UsersConfigTableRowEditorUsername_Object=MibScalar
me1200UsersConfigTableRowEditorUsername=_Me1200UsersConfigTableRowEditorUsername_Object((1,3,6,1,4,1,9,9,815,1,58,1,2,2,1),_Me1200UsersConfigTableRowEditorUsername_Type())
me1200UsersConfigTableRowEditorUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UsersConfigTableRowEditorUsername.setStatus(_A)
_Me1200UsersConfigTableRowEditorPrivilege_Type=Unsigned32
_Me1200UsersConfigTableRowEditorPrivilege_Object=MibScalar
me1200UsersConfigTableRowEditorPrivilege=_Me1200UsersConfigTableRowEditorPrivilege_Object((1,3,6,1,4,1,9,9,815,1,58,1,2,2,2),_Me1200UsersConfigTableRowEditorPrivilege_Type())
me1200UsersConfigTableRowEditorPrivilege.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UsersConfigTableRowEditorPrivilege.setStatus(_A)
_Me1200UsersConfigTableRowEditorEncrypted_Type=TruthValue
_Me1200UsersConfigTableRowEditorEncrypted_Object=MibScalar
me1200UsersConfigTableRowEditorEncrypted=_Me1200UsersConfigTableRowEditorEncrypted_Object((1,3,6,1,4,1,9,9,815,1,58,1,2,2,3),_Me1200UsersConfigTableRowEditorEncrypted_Type())
me1200UsersConfigTableRowEditorEncrypted.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UsersConfigTableRowEditorEncrypted.setStatus(_A)
class _Me1200UsersConfigTableRowEditorPassword_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,44))
_Me1200UsersConfigTableRowEditorPassword_Type.__name__=_D
_Me1200UsersConfigTableRowEditorPassword_Object=MibScalar
me1200UsersConfigTableRowEditorPassword=_Me1200UsersConfigTableRowEditorPassword_Object((1,3,6,1,4,1,9,9,815,1,58,1,2,2,4),_Me1200UsersConfigTableRowEditorPassword_Type())
me1200UsersConfigTableRowEditorPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UsersConfigTableRowEditorPassword.setStatus(_A)
_Me1200UsersConfigTableRowEditorAction_Type=ME1200RowEditorState
_Me1200UsersConfigTableRowEditorAction_Object=MibScalar
me1200UsersConfigTableRowEditorAction=_Me1200UsersConfigTableRowEditorAction_Object((1,3,6,1,4,1,9,9,815,1,58,1,2,2,100),_Me1200UsersConfigTableRowEditorAction_Type())
me1200UsersConfigTableRowEditorAction.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UsersConfigTableRowEditorAction.setStatus(_A)
_Me1200UsersMIBConformance_ObjectIdentity=ObjectIdentity
me1200UsersMIBConformance=_Me1200UsersMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,58,2))
_Me1200UsersMIBCompliances_ObjectIdentity=ObjectIdentity
me1200UsersMIBCompliances=_Me1200UsersMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,58,2,1))
_Me1200UsersMIBGroups_ObjectIdentity=ObjectIdentity
me1200UsersMIBGroups=_Me1200UsersMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,58,2,2))
me1200UsersConfigTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,58,2,2,1))
me1200UsersConfigTableInfoGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:me1200UsersConfigTableInfoGroup.setStatus(_A)
me1200UsersConfigTableRowEditorInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,58,2,2,2))
me1200UsersConfigTableRowEditorInfoGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:me1200UsersConfigTableRowEditorInfoGroup.setStatus(_A)
me1200UsersMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,815,1,58,2,1,1))
me1200UsersMIBCompliance.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:me1200UsersMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'me1200UsersMIB':me1200UsersMIB,'me1200UsersMIBObjects':me1200UsersMIBObjects,'me1200UsersConfig':me1200UsersConfig,'me1200UsersConfigTable':me1200UsersConfigTable,'me1200UsersConfigEntry':me1200UsersConfigEntry,_E:me1200UsersConfigUsername,_F:me1200UsersConfigPrivilege,_G:me1200UsersConfigEncrypted,_H:me1200UsersConfigPassword,_I:me1200UsersConfigAction,'me1200UsersConfigTableRowEditor':me1200UsersConfigTableRowEditor,_J:me1200UsersConfigTableRowEditorUsername,_K:me1200UsersConfigTableRowEditorPrivilege,_L:me1200UsersConfigTableRowEditorEncrypted,_M:me1200UsersConfigTableRowEditorPassword,_N:me1200UsersConfigTableRowEditorAction,'me1200UsersMIBConformance':me1200UsersMIBConformance,'me1200UsersMIBCompliances':me1200UsersMIBCompliances,'me1200UsersMIBCompliance':me1200UsersMIBCompliance,'me1200UsersMIBGroups':me1200UsersMIBGroups,_O:me1200UsersConfigTableInfoGroup,_P:me1200UsersConfigTableRowEditorInfoGroup})