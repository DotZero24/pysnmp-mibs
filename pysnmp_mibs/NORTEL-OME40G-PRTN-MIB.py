_K='lockout'
_J='read-create'
_I='protectionIfIndex'
_H='workingIfIndex'
_G='ifIndex'
_F='IF-MIB'
_E='read-only'
_D='NORTEL-OME40G-PRTN-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','entPhysicalIndex')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndex',_G)
nnOme40G,=mibBuilder.importSymbols('NORTEL-OME40G-MIB','nnOme40G')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
nnOme40GProtection=ModuleIdentity((1,3,6,1,4,1,562,68,11,3,3))
if mibBuilder.loadTexts:nnOme40GProtection.setRevisions(('2007-02-02 00:00','2008-02-07 00:00'))
_NnOme40Gotm3Protection_ObjectIdentity=ObjectIdentity
nnOme40Gotm3Protection=_NnOme40Gotm3Protection_ObjectIdentity((1,3,6,1,4,1,562,68,11,3,3,1))
_NnOTM3protectionGroupTable_Object=MibTable
nnOTM3protectionGroupTable=_NnOTM3protectionGroupTable_Object((1,3,6,1,4,1,562,68,11,3,3,1,1))
if mibBuilder.loadTexts:nnOTM3protectionGroupTable.setStatus(_A)
_NnOTM3protectionGroupEntry_Object=MibTableRow
nnOTM3protectionGroupEntry=_NnOTM3protectionGroupEntry_Object((1,3,6,1,4,1,562,68,11,3,3,1,1,1))
nnOTM3protectionGroupEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:nnOTM3protectionGroupEntry.setStatus(_A)
_WorkingIfIndex_Type=InterfaceIndex
_WorkingIfIndex_Object=MibTableColumn
workingIfIndex=_WorkingIfIndex_Object((1,3,6,1,4,1,562,68,11,3,3,1,1,1,1),_WorkingIfIndex_Type())
workingIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:workingIfIndex.setStatus(_A)
_ProtectionIfIndex_Type=InterfaceIndex
_ProtectionIfIndex_Object=MibTableColumn
protectionIfIndex=_ProtectionIfIndex_Object((1,3,6,1,4,1,562,68,11,3,3,1,1,1,2),_ProtectionIfIndex_Type())
protectionIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:protectionIfIndex.setStatus(_A)
_PtRowStatus_Type=RowStatus
_PtRowStatus_Object=MibTableColumn
ptRowStatus=_PtRowStatus_Object((1,3,6,1,4,1,562,68,11,3,3,1,1,1,3),_PtRowStatus_Type())
ptRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ptRowStatus.setStatus(_A)
class _ProtectionSwitchDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bidirectional',1),('unidirectional',2)))
_ProtectionSwitchDir_Type.__name__=_B
_ProtectionSwitchDir_Object=MibTableColumn
protectionSwitchDir=_ProtectionSwitchDir_Object((1,3,6,1,4,1,562,68,11,3,3,1,1,1,4),_ProtectionSwitchDir_Type())
protectionSwitchDir.setMaxAccess(_C)
if mibBuilder.loadTexts:protectionSwitchDir.setStatus(_A)
class _ProtectionScheme_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('one-plus-one',1))
_ProtectionScheme_Type.__name__=_B
_ProtectionScheme_Object=MibTableColumn
protectionScheme=_ProtectionScheme_Object((1,3,6,1,4,1,562,68,11,3,3,1,1,1,5),_ProtectionScheme_Type())
protectionScheme.setMaxAccess(_C)
if mibBuilder.loadTexts:protectionScheme.setStatus(_A)
class _WaitToRestore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('one-minute',1),('two-minutes',2),('three-minutes',3),('four-minutes',4),('five-minutes',5),('six-minutes',6),('seven-minutes',7),('eight-minutes',8),('nine-minutes',9),('ten-minutes',10),('eleven-minutes',11),('twelve-minutes',12)))
_WaitToRestore_Type.__name__=_B
_WaitToRestore_Object=MibTableColumn
waitToRestore=_WaitToRestore_Object((1,3,6,1,4,1,562,68,11,3,3,1,1,1,6),_WaitToRestore_Type())
waitToRestore.setMaxAccess(_C)
if mibBuilder.loadTexts:waitToRestore.setStatus(_A)
class _Revertive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_Revertive_Type.__name__=_B
_Revertive_Object=MibTableColumn
revertive=_Revertive_Object((1,3,6,1,4,1,562,68,11,3,3,1,1,1,7),_Revertive_Type())
revertive.setMaxAccess(_C)
if mibBuilder.loadTexts:revertive.setStatus(_A)
class _RemoteStandardMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('otn-g-873-1',1))
_RemoteStandardMode_Type.__name__=_B
_RemoteStandardMode_Object=MibTableColumn
remoteStandardMode=_RemoteStandardMode_Object((1,3,6,1,4,1,562,68,11,3,3,1,1,1,8),_RemoteStandardMode_Type())
remoteStandardMode.setMaxAccess(_C)
if mibBuilder.loadTexts:remoteStandardMode.setStatus(_A)
class _RouteDiversity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('off',0))
_RouteDiversity_Type.__name__=_B
_RouteDiversity_Object=MibTableColumn
routeDiversity=_RouteDiversity_Object((1,3,6,1,4,1,562,68,11,3,3,1,1,1,9),_RouteDiversity_Type())
routeDiversity.setMaxAccess(_C)
if mibBuilder.loadTexts:routeDiversity.setStatus(_A)
_NnOTM3protectionSwitchTable_Object=MibTable
nnOTM3protectionSwitchTable=_NnOTM3protectionSwitchTable_Object((1,3,6,1,4,1,562,68,11,3,3,1,2))
if mibBuilder.loadTexts:nnOTM3protectionSwitchTable.setStatus(_A)
_NnOTM3protectionSwitchEntry_Object=MibTableRow
nnOTM3protectionSwitchEntry=_NnOTM3protectionSwitchEntry_Object((1,3,6,1,4,1,562,68,11,3,3,1,2,1))
nnOTM3protectionSwitchEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:nnOTM3protectionSwitchEntry.setStatus(_A)
class _SwitchCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('man',1),('frcd',2),(_K,3),('release',4)))
_SwitchCommand_Type.__name__=_B
_SwitchCommand_Object=MibTableColumn
switchCommand=_SwitchCommand_Object((1,3,6,1,4,1,562,68,11,3,3,1,2,1,1),_SwitchCommand_Type())
switchCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:switchCommand.setStatus(_A)
class _SwitchStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('idle',1),('auto',2),('man',3),('frcd',4),(_K,5)))
_SwitchStatus_Type.__name__=_B
_SwitchStatus_Object=MibTableColumn
switchStatus=_SwitchStatus_Object((1,3,6,1,4,1,562,68,11,3,3,1,2,1,2),_SwitchStatus_Type())
switchStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:switchStatus.setStatus(_A)
class _EndInitiatingSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('remote',1),('local',2)))
_EndInitiatingSwitch_Type.__name__=_B
_EndInitiatingSwitch_Object=MibTableColumn
endInitiatingSwitch=_EndInitiatingSwitch_Object((1,3,6,1,4,1,562,68,11,3,3,1,2,1,3),_EndInitiatingSwitch_Type())
endInitiatingSwitch.setMaxAccess(_E)
if mibBuilder.loadTexts:endInitiatingSwitch.setStatus(_A)
class _ReasonForAutoSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('sigok',1),('sf',2),('sd',3),('eber',4),('eqpfl',5),('facoos',6),('eqpoos',7),('osc',8),('wr',9)))
_ReasonForAutoSwitch_Type.__name__=_B
_ReasonForAutoSwitch_Object=MibTableColumn
reasonForAutoSwitch=_ReasonForAutoSwitch_Object((1,3,6,1,4,1,562,68,11,3,3,1,2,1,4),_ReasonForAutoSwitch_Type())
reasonForAutoSwitch.setMaxAccess(_E)
if mibBuilder.loadTexts:reasonForAutoSwitch.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nnOme40GProtection':nnOme40GProtection,'nnOme40Gotm3Protection':nnOme40Gotm3Protection,'nnOTM3protectionGroupTable':nnOTM3protectionGroupTable,'nnOTM3protectionGroupEntry':nnOTM3protectionGroupEntry,_H:workingIfIndex,_I:protectionIfIndex,'ptRowStatus':ptRowStatus,'protectionSwitchDir':protectionSwitchDir,'protectionScheme':protectionScheme,'waitToRestore':waitToRestore,'revertive':revertive,'remoteStandardMode':remoteStandardMode,'routeDiversity':routeDiversity,'nnOTM3protectionSwitchTable':nnOTM3protectionSwitchTable,'nnOTM3protectionSwitchEntry':nnOTM3protectionSwitchEntry,'switchCommand':switchCommand,'switchStatus':switchStatus,'endInitiatingSwitch':endInitiatingSwitch,'reasonForAutoSwitch':reasonForAutoSwitch})