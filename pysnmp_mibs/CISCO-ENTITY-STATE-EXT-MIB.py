_X='ciscoEntStateExtStatusNotifGroup'
_W='ciscoEntStateExtSwitchoverNotifGroup'
_V='ciscoEntStateExtNotifControlGroup'
_U='ciscoEntStateExtNotifObjectsGroup'
_T='ceStateExtStandbyStatusChange'
_S='ceStateExtStandbySwitchover'
_R='ceStateExtGlobalOperNotifEnable'
_Q='ceStateExtGlobalStandbyStatusNotifEnable'
_P='ceStateExtGlobalSwitchoverNotifEnable'
_O='ceStateExtOperNotifEnable'
_N='ceStateExtStandbyStatusNotifEnable'
_M='ceStateExtSwitchoverNotifEnable'
_L='ceStateExtEntry'
_K='ceStateExtPrevStandbyState'
_J='enabled'
_I='followsGlobal'
_H='entStateStandby'
_G='entStateAlarm'
_F='ENTITY-STATE-MIB'
_E='read-write'
_D='disabled'
_C='Integer32'
_B='CISCO-ENTITY-STATE-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entStateAlarm,entStateEntry,entStateStandby=mibBuilder.importSymbols(_F,_G,'entStateEntry',_H)
EntityStandbyStatus,=mibBuilder.importSymbols('ENTITY-STATE-TC-MIB','EntityStandbyStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoEntityStateExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,747))
if mibBuilder.loadTexts:ciscoEntityStateExtMIB.setRevisions(('2010-06-16 00:00',))
_CiscoEntityStateExtMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoEntityStateExtMIBNotifs=_CiscoEntityStateExtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,747,0))
_CiscoEntityStateExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEntityStateExtMIBObjects=_CiscoEntityStateExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,747,1))
_CeStateExtTable_Object=MibTable
ceStateExtTable=_CeStateExtTable_Object((1,3,6,1,4,1,9,9,747,1,1))
if mibBuilder.loadTexts:ceStateExtTable.setStatus(_A)
_CeStateExtEntry_Object=MibTableRow
ceStateExtEntry=_CeStateExtEntry_Object((1,3,6,1,4,1,9,9,747,1,1,1))
if mibBuilder.loadTexts:ceStateExtEntry.setStatus(_A)
_CeStateExtPrevStandbyState_Type=EntityStandbyStatus
_CeStateExtPrevStandbyState_Object=MibTableColumn
ceStateExtPrevStandbyState=_CeStateExtPrevStandbyState_Object((1,3,6,1,4,1,9,9,747,1,1,1,1),_CeStateExtPrevStandbyState_Type())
ceStateExtPrevStandbyState.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:ceStateExtPrevStandbyState.setStatus(_A)
class _CeStateExtSwitchoverNotifEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_D,2)))
_CeStateExtSwitchoverNotifEnable_Type.__name__=_C
_CeStateExtSwitchoverNotifEnable_Object=MibTableColumn
ceStateExtSwitchoverNotifEnable=_CeStateExtSwitchoverNotifEnable_Object((1,3,6,1,4,1,9,9,747,1,1,1,2),_CeStateExtSwitchoverNotifEnable_Type())
ceStateExtSwitchoverNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ceStateExtSwitchoverNotifEnable.setStatus(_A)
class _CeStateExtStandbyStatusNotifEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_D,2)))
_CeStateExtStandbyStatusNotifEnable_Type.__name__=_C
_CeStateExtStandbyStatusNotifEnable_Object=MibTableColumn
ceStateExtStandbyStatusNotifEnable=_CeStateExtStandbyStatusNotifEnable_Object((1,3,6,1,4,1,9,9,747,1,1,1,3),_CeStateExtStandbyStatusNotifEnable_Type())
ceStateExtStandbyStatusNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ceStateExtStandbyStatusNotifEnable.setStatus(_A)
class _CeStateExtOperNotifEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_D,2)))
_CeStateExtOperNotifEnable_Type.__name__=_C
_CeStateExtOperNotifEnable_Object=MibTableColumn
ceStateExtOperNotifEnable=_CeStateExtOperNotifEnable_Object((1,3,6,1,4,1,9,9,747,1,1,1,4),_CeStateExtOperNotifEnable_Type())
ceStateExtOperNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ceStateExtOperNotifEnable.setStatus(_A)
_CiscoEntityStateExtNotifControl_ObjectIdentity=ObjectIdentity
ciscoEntityStateExtNotifControl=_CiscoEntityStateExtNotifControl_ObjectIdentity((1,3,6,1,4,1,9,9,747,1,2))
class _CeStateExtGlobalSwitchoverNotifEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_D,2)))
_CeStateExtGlobalSwitchoverNotifEnable_Type.__name__=_C
_CeStateExtGlobalSwitchoverNotifEnable_Object=MibScalar
ceStateExtGlobalSwitchoverNotifEnable=_CeStateExtGlobalSwitchoverNotifEnable_Object((1,3,6,1,4,1,9,9,747,1,2,1),_CeStateExtGlobalSwitchoverNotifEnable_Type())
ceStateExtGlobalSwitchoverNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ceStateExtGlobalSwitchoverNotifEnable.setStatus(_A)
class _CeStateExtGlobalStandbyStatusNotifEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_D,2)))
_CeStateExtGlobalStandbyStatusNotifEnable_Type.__name__=_C
_CeStateExtGlobalStandbyStatusNotifEnable_Object=MibScalar
ceStateExtGlobalStandbyStatusNotifEnable=_CeStateExtGlobalStandbyStatusNotifEnable_Object((1,3,6,1,4,1,9,9,747,1,2,2),_CeStateExtGlobalStandbyStatusNotifEnable_Type())
ceStateExtGlobalStandbyStatusNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ceStateExtGlobalStandbyStatusNotifEnable.setStatus(_A)
class _CeStateExtGlobalOperNotifEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_D,2)))
_CeStateExtGlobalOperNotifEnable_Type.__name__=_C
_CeStateExtGlobalOperNotifEnable_Object=MibScalar
ceStateExtGlobalOperNotifEnable=_CeStateExtGlobalOperNotifEnable_Object((1,3,6,1,4,1,9,9,747,1,2,3),_CeStateExtGlobalOperNotifEnable_Type())
ceStateExtGlobalOperNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ceStateExtGlobalOperNotifEnable.setStatus(_A)
_CiscoEntityStateExtMIBConform_ObjectIdentity=ObjectIdentity
ciscoEntityStateExtMIBConform=_CiscoEntityStateExtMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,747,2))
_CiscoEntStateExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoEntStateExtMIBCompliances=_CiscoEntStateExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,747,2,1))
_CiscoEntStateExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoEntStateExtMIBGroups=_CiscoEntStateExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,747,2,2))
entStateEntry.registerAugmentions((_B,_L))
ceStateExtEntry.setIndexNames(*entStateEntry.getIndexNames())
ciscoEntStateExtNotifObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,747,2,2,1))
ciscoEntStateExtNotifObjectsGroup.setObjects((_B,_K))
if mibBuilder.loadTexts:ciscoEntStateExtNotifObjectsGroup.setStatus(_A)
ciscoEntStateExtNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,747,2,2,2))
ciscoEntStateExtNotifControlGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ciscoEntStateExtNotifControlGroup.setStatus(_A)
ceStateExtStandbySwitchover=NotificationType((1,3,6,1,4,1,9,9,747,0,1))
ceStateExtStandbySwitchover.setObjects(*((_F,_G),(_F,_H)))
if mibBuilder.loadTexts:ceStateExtStandbySwitchover.setStatus(_A)
ceStateExtStandbyStatusChange=NotificationType((1,3,6,1,4,1,9,9,747,0,2))
ceStateExtStandbyStatusChange.setObjects(*((_F,_G),(_F,_H),(_B,_K)))
if mibBuilder.loadTexts:ceStateExtStandbyStatusChange.setStatus(_A)
ciscoEntStateExtSwitchoverNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,747,2,2,3))
ciscoEntStateExtSwitchoverNotifGroup.setObjects((_B,_S))
if mibBuilder.loadTexts:ciscoEntStateExtSwitchoverNotifGroup.setStatus(_A)
ciscoEntStateExtStatusNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,747,2,2,4))
ciscoEntStateExtStatusNotifGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:ciscoEntStateExtStatusNotifGroup.setStatus(_A)
ciscoEntStateExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,747,2,1,1))
ciscoEntStateExtMIBCompliance.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciscoEntStateExtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoEntityStateExtMIB':ciscoEntityStateExtMIB,'ciscoEntityStateExtMIBNotifs':ciscoEntityStateExtMIBNotifs,_S:ceStateExtStandbySwitchover,_T:ceStateExtStandbyStatusChange,'ciscoEntityStateExtMIBObjects':ciscoEntityStateExtMIBObjects,'ceStateExtTable':ceStateExtTable,_L:ceStateExtEntry,_K:ceStateExtPrevStandbyState,_M:ceStateExtSwitchoverNotifEnable,_N:ceStateExtStandbyStatusNotifEnable,_O:ceStateExtOperNotifEnable,'ciscoEntityStateExtNotifControl':ciscoEntityStateExtNotifControl,_P:ceStateExtGlobalSwitchoverNotifEnable,_Q:ceStateExtGlobalStandbyStatusNotifEnable,_R:ceStateExtGlobalOperNotifEnable,'ciscoEntityStateExtMIBConform':ciscoEntityStateExtMIBConform,'ciscoEntStateExtMIBCompliances':ciscoEntStateExtMIBCompliances,'ciscoEntStateExtMIBCompliance':ciscoEntStateExtMIBCompliance,'ciscoEntStateExtMIBGroups':ciscoEntStateExtMIBGroups,_U:ciscoEntStateExtNotifObjectsGroup,_V:ciscoEntStateExtNotifControlGroup,_W:ciscoEntStateExtSwitchoverNotifGroup,_X:ciscoEntStateExtStatusNotifGroup})