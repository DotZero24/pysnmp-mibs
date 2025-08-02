_Y='singleManagementEntityNotificationGroup'
_X='singleManagementEntityGroup'
_W='wanInterfaceGroup'
_V='pdnStackUnitComRestored'
_U='pdnStackUnitComFailure'
_T='pdnStackUnitAdded'
_S='pdnStackUnitComRestoredTrapEnable'
_R='pdnStackUnitComFailureTrapEnable'
_Q='pdnStackUnitAddedTrapEnable'
_P='pdnMoveUnitCmd'
_O='pdnUnitPresent'
_N='pdnUnitAssigned'
_M='pdnUnitEntPhysicalIndex'
_L='pdnStackMethod'
_K='wanInterface'
_J='pdnMoveUnitDestNumber'
_I='pdnMoveUnitSrcNumber'
_H='pdnUnitExternalID'
_G='not-accessible'
_F='read-only'
_E='Integer32'
_D='pdnUnitGUID'
_C='read-write'
_B='PDN-STACKABLE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pdn_common,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-common')
SwitchState,=mibBuilder.importSymbols('PDN-TC','SwitchState')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
pdnStackable=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,36))
if mibBuilder.loadTexts:pdnStackable.setRevisions(('2004-09-14 00:00','2003-03-12 00:00','2002-07-31 00:00','2002-05-15 00:00'))
_PdnStackableNotifications_ObjectIdentity=ObjectIdentity
pdnStackableNotifications=_PdnStackableNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,36,0))
_PdnStackableObjects_ObjectIdentity=ObjectIdentity
pdnStackableObjects=_PdnStackableObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,36,1))
class _WanInterface_Type(Bits):namedValues=NamedValues(*(('stackLink1',0),('stackLink2',1),('plugInModule',2),('stackLink3',3),('stackLink4',4),('stackLink5',5),('stackLink6',6),('stackLink7',7),('stackLink8',8),('stackLink9',9),('stackLink10',10),('stackLink11',11),('stackLink12',12),('stackLink13',13),('stackLink14',14),('stackLink15',15),('stackLink16',16),('stackLink17',17),('stackLink18',18)))
_WanInterface_Type.__name__='Bits'
_WanInterface_Object=MibScalar
wanInterface=_WanInterface_Object((1,3,6,1,4,1,1795,2,24,2,36,1,1),_WanInterface_Type())
wanInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:wanInterface.setStatus(_A)
class _PdnStackMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('daisyChain',1),('star',2)))
_PdnStackMethod_Type.__name__=_E
_PdnStackMethod_Object=MibScalar
pdnStackMethod=_PdnStackMethod_Object((1,3,6,1,4,1,1795,2,24,2,36,1,2),_PdnStackMethod_Type())
pdnStackMethod.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnStackMethod.setStatus(_A)
_PdnStackConfigurationTable_Object=MibTable
pdnStackConfigurationTable=_PdnStackConfigurationTable_Object((1,3,6,1,4,1,1795,2,24,2,36,1,3))
if mibBuilder.loadTexts:pdnStackConfigurationTable.setStatus(_A)
_PdnStackConfigurationEntry_Object=MibTableRow
pdnStackConfigurationEntry=_PdnStackConfigurationEntry_Object((1,3,6,1,4,1,1795,2,24,2,36,1,3,1))
pdnStackConfigurationEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:pdnStackConfigurationEntry.setStatus(_A)
_PdnUnitExternalID_Type=Unsigned32
_PdnUnitExternalID_Object=MibTableColumn
pdnUnitExternalID=_PdnUnitExternalID_Object((1,3,6,1,4,1,1795,2,24,2,36,1,3,1,1),_PdnUnitExternalID_Type())
pdnUnitExternalID.setMaxAccess(_G)
if mibBuilder.loadTexts:pdnUnitExternalID.setStatus(_A)
class _PdnUnitEntPhysicalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PdnUnitEntPhysicalIndex_Type.__name__=_E
_PdnUnitEntPhysicalIndex_Object=MibTableColumn
pdnUnitEntPhysicalIndex=_PdnUnitEntPhysicalIndex_Object((1,3,6,1,4,1,1795,2,24,2,36,1,3,1,2),_PdnUnitEntPhysicalIndex_Type())
pdnUnitEntPhysicalIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnUnitEntPhysicalIndex.setStatus(_A)
_PdnUnitAssigned_Type=TruthValue
_PdnUnitAssigned_Object=MibTableColumn
pdnUnitAssigned=_PdnUnitAssigned_Object((1,3,6,1,4,1,1795,2,24,2,36,1,3,1,3),_PdnUnitAssigned_Type())
pdnUnitAssigned.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnUnitAssigned.setStatus(_A)
_PdnUnitGUID_Type=DisplayString
_PdnUnitGUID_Object=MibTableColumn
pdnUnitGUID=_PdnUnitGUID_Object((1,3,6,1,4,1,1795,2,24,2,36,1,3,1,4),_PdnUnitGUID_Type())
pdnUnitGUID.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnUnitGUID.setStatus(_A)
_PdnUnitPresent_Type=TruthValue
_PdnUnitPresent_Object=MibTableColumn
pdnUnitPresent=_PdnUnitPresent_Object((1,3,6,1,4,1,1795,2,24,2,36,1,3,1,5),_PdnUnitPresent_Type())
pdnUnitPresent.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnUnitPresent.setStatus(_A)
_PdnMoveUnitCmdTable_Object=MibTable
pdnMoveUnitCmdTable=_PdnMoveUnitCmdTable_Object((1,3,6,1,4,1,1795,2,24,2,36,1,4))
if mibBuilder.loadTexts:pdnMoveUnitCmdTable.setStatus(_A)
_PdnMoveUnitCmdEntry_Object=MibTableRow
pdnMoveUnitCmdEntry=_PdnMoveUnitCmdEntry_Object((1,3,6,1,4,1,1795,2,24,2,36,1,4,1))
pdnMoveUnitCmdEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:pdnMoveUnitCmdEntry.setStatus(_A)
_PdnMoveUnitSrcNumber_Type=Unsigned32
_PdnMoveUnitSrcNumber_Object=MibTableColumn
pdnMoveUnitSrcNumber=_PdnMoveUnitSrcNumber_Object((1,3,6,1,4,1,1795,2,24,2,36,1,4,1,1),_PdnMoveUnitSrcNumber_Type())
pdnMoveUnitSrcNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:pdnMoveUnitSrcNumber.setStatus(_A)
_PdnMoveUnitDestNumber_Type=Unsigned32
_PdnMoveUnitDestNumber_Object=MibTableColumn
pdnMoveUnitDestNumber=_PdnMoveUnitDestNumber_Object((1,3,6,1,4,1,1795,2,24,2,36,1,4,1,2),_PdnMoveUnitDestNumber_Type())
pdnMoveUnitDestNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:pdnMoveUnitDestNumber.setStatus(_A)
class _PdnMoveUnitCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),('move',2)))
_PdnMoveUnitCmd_Type.__name__=_E
_PdnMoveUnitCmd_Object=MibTableColumn
pdnMoveUnitCmd=_PdnMoveUnitCmd_Object((1,3,6,1,4,1,1795,2,24,2,36,1,4,1,3),_PdnMoveUnitCmd_Type())
pdnMoveUnitCmd.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnMoveUnitCmd.setStatus(_A)
_PdnStackUnitAddedTrapEnable_Type=SwitchState
_PdnStackUnitAddedTrapEnable_Object=MibScalar
pdnStackUnitAddedTrapEnable=_PdnStackUnitAddedTrapEnable_Object((1,3,6,1,4,1,1795,2,24,2,36,1,5),_PdnStackUnitAddedTrapEnable_Type())
pdnStackUnitAddedTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnStackUnitAddedTrapEnable.setStatus(_A)
_PdnStackUnitComFailureTrapEnable_Type=SwitchState
_PdnStackUnitComFailureTrapEnable_Object=MibScalar
pdnStackUnitComFailureTrapEnable=_PdnStackUnitComFailureTrapEnable_Object((1,3,6,1,4,1,1795,2,24,2,36,1,6),_PdnStackUnitComFailureTrapEnable_Type())
pdnStackUnitComFailureTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnStackUnitComFailureTrapEnable.setStatus(_A)
_PdnStackUnitComRestoredTrapEnable_Type=SwitchState
_PdnStackUnitComRestoredTrapEnable_Object=MibScalar
pdnStackUnitComRestoredTrapEnable=_PdnStackUnitComRestoredTrapEnable_Object((1,3,6,1,4,1,1795,2,24,2,36,1,7),_PdnStackUnitComRestoredTrapEnable_Type())
pdnStackUnitComRestoredTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnStackUnitComRestoredTrapEnable.setStatus(_A)
_PdnStackableAFNs_ObjectIdentity=ObjectIdentity
pdnStackableAFNs=_PdnStackableAFNs_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,36,2))
_PdnStackableConformance_ObjectIdentity=ObjectIdentity
pdnStackableConformance=_PdnStackableConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,36,3))
_PdnStackableCompliances_ObjectIdentity=ObjectIdentity
pdnStackableCompliances=_PdnStackableCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,36,3,1))
_PdnStackableGroups_ObjectIdentity=ObjectIdentity
pdnStackableGroups=_PdnStackableGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,36,3,2))
_PdnStackableObjGroups_ObjectIdentity=ObjectIdentity
pdnStackableObjGroups=_PdnStackableObjGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,36,3,2,1))
_PdnStackableAfnGroups_ObjectIdentity=ObjectIdentity
pdnStackableAfnGroups=_PdnStackableAfnGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,36,3,2,2))
_PdnStackableNtfyGroups_ObjectIdentity=ObjectIdentity
pdnStackableNtfyGroups=_PdnStackableNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,36,3,2,3))
wanInterfaceGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,36,3,2,1,1))
wanInterfaceGroup.setObjects((_B,_K))
if mibBuilder.loadTexts:wanInterfaceGroup.setStatus(_A)
singleManagementEntityGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,36,3,2,1,2))
singleManagementEntityGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_D),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:singleManagementEntityGroup.setStatus(_A)
pdnStackUnitAdded=NotificationType((1,3,6,1,4,1,1795,2,24,2,36,0,1))
pdnStackUnitAdded.setObjects((_B,_D))
if mibBuilder.loadTexts:pdnStackUnitAdded.setStatus(_A)
pdnStackUnitComFailure=NotificationType((1,3,6,1,4,1,1795,2,24,2,36,0,2))
pdnStackUnitComFailure.setObjects((_B,_D))
if mibBuilder.loadTexts:pdnStackUnitComFailure.setStatus(_A)
pdnStackUnitComRestored=NotificationType((1,3,6,1,4,1,1795,2,24,2,36,0,3))
pdnStackUnitComRestored.setObjects((_B,_D))
if mibBuilder.loadTexts:pdnStackUnitComRestored.setStatus(_A)
singleManagementEntityNotificationGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,2,36,3,2,3,1))
singleManagementEntityNotificationGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:singleManagementEntityNotificationGroup.setStatus(_A)
pdnStackableConmpliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,36,3,1,1))
pdnStackableConmpliance.setObjects(*((_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:pdnStackableConmpliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnStackable':pdnStackable,'pdnStackableNotifications':pdnStackableNotifications,_T:pdnStackUnitAdded,_U:pdnStackUnitComFailure,_V:pdnStackUnitComRestored,'pdnStackableObjects':pdnStackableObjects,_K:wanInterface,_L:pdnStackMethod,'pdnStackConfigurationTable':pdnStackConfigurationTable,'pdnStackConfigurationEntry':pdnStackConfigurationEntry,_H:pdnUnitExternalID,_M:pdnUnitEntPhysicalIndex,_N:pdnUnitAssigned,_D:pdnUnitGUID,_O:pdnUnitPresent,'pdnMoveUnitCmdTable':pdnMoveUnitCmdTable,'pdnMoveUnitCmdEntry':pdnMoveUnitCmdEntry,_I:pdnMoveUnitSrcNumber,_J:pdnMoveUnitDestNumber,_P:pdnMoveUnitCmd,_Q:pdnStackUnitAddedTrapEnable,_R:pdnStackUnitComFailureTrapEnable,_S:pdnStackUnitComRestoredTrapEnable,'pdnStackableAFNs':pdnStackableAFNs,'pdnStackableConformance':pdnStackableConformance,'pdnStackableCompliances':pdnStackableCompliances,'pdnStackableConmpliance':pdnStackableConmpliance,'pdnStackableGroups':pdnStackableGroups,'pdnStackableObjGroups':pdnStackableObjGroups,_W:wanInterfaceGroup,_X:singleManagementEntityGroup,'pdnStackableAfnGroups':pdnStackableAfnGroups,'pdnStackableNtfyGroups':pdnStackableNtfyGroups,_Y:singleManagementEntityNotificationGroup})