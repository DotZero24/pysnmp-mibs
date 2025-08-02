_P='oaFrPanelGroup'
_O='oaFrPanelSltPrtsSubConnector'
_N='oaFrPanelSltPrtsConnector'
_M='oaFrPanelSltLedStatuses'
_L='oaFrPanelSltLedsVersion'
_K='oaFrPanelSltLedsNumber'
_J='oaFrPanelSltPortsNumber'
_I='oaFrPanelGenSupport'
_H='not-accessible'
_G='oaFrPanelSltSlotId'
_F='oaFrPanelSltShelfId'
_E='OctetString'
_D='read-only'
_C='Integer32'
_B='OA-FRONT-PANEL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nbSwitchG1Il,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','nbSwitchG1Il')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
oaFrPanel=ModuleIdentity((1,3,6,1,4,1,629,1,50,16,20))
if mibBuilder.loadTexts:oaFrPanel.setRevisions(('2008-06-05 00:00',))
_NbDevId_ObjectIdentity=ObjectIdentity
nbDevId=_NbDevId_ObjectIdentity((1,3,6,1,4,1,629,1,50,16))
_OaFrPanelGen_ObjectIdentity=ObjectIdentity
oaFrPanelGen=_OaFrPanelGen_ObjectIdentity((1,3,6,1,4,1,629,1,50,16,20,1))
class _OaFrPanelGenSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_OaFrPanelGenSupport_Type.__name__=_C
_OaFrPanelGenSupport_Object=MibScalar
oaFrPanelGenSupport=_OaFrPanelGenSupport_Object((1,3,6,1,4,1,629,1,50,16,20,1,1),_OaFrPanelGenSupport_Type())
oaFrPanelGenSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFrPanelGenSupport.setStatus(_A)
_OaFrPanelSlot_ObjectIdentity=ObjectIdentity
oaFrPanelSlot=_OaFrPanelSlot_ObjectIdentity((1,3,6,1,4,1,629,1,50,16,20,5))
_OaFrPanelSlotTable_Object=MibTable
oaFrPanelSlotTable=_OaFrPanelSlotTable_Object((1,3,6,1,4,1,629,1,50,16,20,5,5))
if mibBuilder.loadTexts:oaFrPanelSlotTable.setStatus(_A)
_OaFrPanelSlotEntry_Object=MibTableRow
oaFrPanelSlotEntry=_OaFrPanelSlotEntry_Object((1,3,6,1,4,1,629,1,50,16,20,5,5,1))
oaFrPanelSlotEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:oaFrPanelSlotEntry.setStatus(_A)
class _OaFrPanelSltShelfId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_OaFrPanelSltShelfId_Type.__name__=_C
_OaFrPanelSltShelfId_Object=MibTableColumn
oaFrPanelSltShelfId=_OaFrPanelSltShelfId_Object((1,3,6,1,4,1,629,1,50,16,20,5,5,1,1),_OaFrPanelSltShelfId_Type())
oaFrPanelSltShelfId.setMaxAccess(_H)
if mibBuilder.loadTexts:oaFrPanelSltShelfId.setStatus(_A)
class _OaFrPanelSltSlotId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_OaFrPanelSltSlotId_Type.__name__=_C
_OaFrPanelSltSlotId_Object=MibTableColumn
oaFrPanelSltSlotId=_OaFrPanelSltSlotId_Object((1,3,6,1,4,1,629,1,50,16,20,5,5,1,2),_OaFrPanelSltSlotId_Type())
oaFrPanelSltSlotId.setMaxAccess(_H)
if mibBuilder.loadTexts:oaFrPanelSltSlotId.setStatus(_A)
class _OaFrPanelSltPortsNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OaFrPanelSltPortsNumber_Type.__name__=_C
_OaFrPanelSltPortsNumber_Object=MibTableColumn
oaFrPanelSltPortsNumber=_OaFrPanelSltPortsNumber_Object((1,3,6,1,4,1,629,1,50,16,20,5,5,1,3),_OaFrPanelSltPortsNumber_Type())
oaFrPanelSltPortsNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFrPanelSltPortsNumber.setStatus(_A)
class _OaFrPanelSltLedsNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OaFrPanelSltLedsNumber_Type.__name__=_C
_OaFrPanelSltLedsNumber_Object=MibTableColumn
oaFrPanelSltLedsNumber=_OaFrPanelSltLedsNumber_Object((1,3,6,1,4,1,629,1,50,16,20,5,5,1,4),_OaFrPanelSltLedsNumber_Type())
oaFrPanelSltLedsNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFrPanelSltLedsNumber.setStatus(_A)
class _OaFrPanelSltLedsVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_OaFrPanelSltLedsVersion_Type.__name__=_C
_OaFrPanelSltLedsVersion_Object=MibTableColumn
oaFrPanelSltLedsVersion=_OaFrPanelSltLedsVersion_Object((1,3,6,1,4,1,629,1,50,16,20,5,5,1,5),_OaFrPanelSltLedsVersion_Type())
oaFrPanelSltLedsVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFrPanelSltLedsVersion.setStatus(_A)
class _OaFrPanelSltLedStatuses_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OaFrPanelSltLedStatuses_Type.__name__=_E
_OaFrPanelSltLedStatuses_Object=MibTableColumn
oaFrPanelSltLedStatuses=_OaFrPanelSltLedStatuses_Object((1,3,6,1,4,1,629,1,50,16,20,5,5,1,6),_OaFrPanelSltLedStatuses_Type())
oaFrPanelSltLedStatuses.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFrPanelSltLedStatuses.setStatus(_A)
class _OaFrPanelSltPrtsConnector_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OaFrPanelSltPrtsConnector_Type.__name__=_E
_OaFrPanelSltPrtsConnector_Object=MibTableColumn
oaFrPanelSltPrtsConnector=_OaFrPanelSltPrtsConnector_Object((1,3,6,1,4,1,629,1,50,16,20,5,5,1,7),_OaFrPanelSltPrtsConnector_Type())
oaFrPanelSltPrtsConnector.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFrPanelSltPrtsConnector.setStatus(_A)
class _OaFrPanelSltPrtsSubConnector_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OaFrPanelSltPrtsSubConnector_Type.__name__=_E
_OaFrPanelSltPrtsSubConnector_Object=MibTableColumn
oaFrPanelSltPrtsSubConnector=_OaFrPanelSltPrtsSubConnector_Object((1,3,6,1,4,1,629,1,50,16,20,5,5,1,8),_OaFrPanelSltPrtsSubConnector_Type())
oaFrPanelSltPrtsSubConnector.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFrPanelSltPrtsSubConnector.setStatus(_A)
_OaFrPanelConformance_ObjectIdentity=ObjectIdentity
oaFrPanelConformance=_OaFrPanelConformance_ObjectIdentity((1,3,6,1,4,1,629,1,50,16,20,101))
_OaFrPanelCompliances_ObjectIdentity=ObjectIdentity
oaFrPanelCompliances=_OaFrPanelCompliances_ObjectIdentity((1,3,6,1,4,1,629,1,50,16,20,101,1))
_OaFrPanelGroups_ObjectIdentity=ObjectIdentity
oaFrPanelGroups=_OaFrPanelGroups_ObjectIdentity((1,3,6,1,4,1,629,1,50,16,20,101,2))
oaFrPanelGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,16,20,101,2,1))
oaFrPanelGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:oaFrPanelGroup.setStatus(_A)
oaFrPanelCompliance=ModuleCompliance((1,3,6,1,4,1,629,1,50,16,20,101,1,1))
oaFrPanelCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:oaFrPanelCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nbDevId':nbDevId,'oaFrPanel':oaFrPanel,'oaFrPanelGen':oaFrPanelGen,_I:oaFrPanelGenSupport,'oaFrPanelSlot':oaFrPanelSlot,'oaFrPanelSlotTable':oaFrPanelSlotTable,'oaFrPanelSlotEntry':oaFrPanelSlotEntry,_F:oaFrPanelSltShelfId,_G:oaFrPanelSltSlotId,_J:oaFrPanelSltPortsNumber,_K:oaFrPanelSltLedsNumber,_L:oaFrPanelSltLedsVersion,_M:oaFrPanelSltLedStatuses,_N:oaFrPanelSltPrtsConnector,_O:oaFrPanelSltPrtsSubConnector,'oaFrPanelConformance':oaFrPanelConformance,'oaFrPanelCompliances':oaFrPanelCompliances,'oaFrPanelCompliance':oaFrPanelCompliance,'oaFrPanelGroups':oaFrPanelGroups,_P:oaFrPanelGroup})