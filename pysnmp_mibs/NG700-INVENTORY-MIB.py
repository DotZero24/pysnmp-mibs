_J='agentInventoryComponentIndex'
_I='not-accessible'
_H='agentInventoryCardIndex'
_G='disable'
_F='enable'
_E='NG700-INVENTORY-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ng700smartswitch,=mibBuilder.importSymbols('NG700-REF-MIB','ng700smartswitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fastPathInventory=ModuleIdentity((1,3,6,1,4,1,4526,11,13))
if mibBuilder.loadTexts:fastPathInventory.setRevisions(('2011-01-26 00:00','2007-05-23 00:00','2004-10-28 20:37','2003-05-26 19:30'))
class AgentInventoryUnitPreference(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disabled',0),('unsassigned',1),('assigned',2)))
class AgentInventoryUnitType(TextualConvention,Unsigned32):status=_A;displayHint='x'
class AgentInventoryCardType(TextualConvention,Unsigned32):status=_A;displayHint='x'
_AgentInventoryStackGroup_ObjectIdentity=ObjectIdentity
agentInventoryStackGroup=_AgentInventoryStackGroup_ObjectIdentity((1,3,6,1,4,1,4526,11,13,1))
class _AgentInventoryStackSTKname_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unconfigured',1),('image1',2),('image2',3)))
_AgentInventoryStackSTKname_Type.__name__=_C
_AgentInventoryStackSTKname_Object=MibScalar
agentInventoryStackSTKname=_AgentInventoryStackSTKname_Object((1,3,6,1,4,1,4526,11,13,1,5),_AgentInventoryStackSTKname_Type())
agentInventoryStackSTKname.setMaxAccess(_D)
if mibBuilder.loadTexts:agentInventoryStackSTKname.setStatus(_A)
class _AgentInventoryStackActivateSTK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentInventoryStackActivateSTK_Type.__name__=_C
_AgentInventoryStackActivateSTK_Object=MibScalar
agentInventoryStackActivateSTK=_AgentInventoryStackActivateSTK_Object((1,3,6,1,4,1,4526,11,13,1,6),_AgentInventoryStackActivateSTK_Type())
agentInventoryStackActivateSTK.setMaxAccess(_D)
if mibBuilder.loadTexts:agentInventoryStackActivateSTK.setStatus(_A)
class _AgentInventoryStackDeleteSTK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentInventoryStackDeleteSTK_Type.__name__=_C
_AgentInventoryStackDeleteSTK_Object=MibScalar
agentInventoryStackDeleteSTK=_AgentInventoryStackDeleteSTK_Object((1,3,6,1,4,1,4526,11,13,1,7),_AgentInventoryStackDeleteSTK_Type())
agentInventoryStackDeleteSTK.setMaxAccess(_D)
if mibBuilder.loadTexts:agentInventoryStackDeleteSTK.setStatus(_A)
_AgentInventoryCardGroup_ObjectIdentity=ObjectIdentity
agentInventoryCardGroup=_AgentInventoryCardGroup_ObjectIdentity((1,3,6,1,4,1,4526,11,13,4))
_AgentInventoryCardTypeTable_Object=MibTable
agentInventoryCardTypeTable=_AgentInventoryCardTypeTable_Object((1,3,6,1,4,1,4526,11,13,4,1))
if mibBuilder.loadTexts:agentInventoryCardTypeTable.setStatus(_A)
_AgentInventoryCardTypeEntry_Object=MibTableRow
agentInventoryCardTypeEntry=_AgentInventoryCardTypeEntry_Object((1,3,6,1,4,1,4526,11,13,4,1,1))
agentInventoryCardTypeEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:agentInventoryCardTypeEntry.setStatus(_A)
_AgentInventoryCardIndex_Type=Unsigned32
_AgentInventoryCardIndex_Object=MibTableColumn
agentInventoryCardIndex=_AgentInventoryCardIndex_Object((1,3,6,1,4,1,4526,11,13,4,1,1,1),_AgentInventoryCardIndex_Type())
agentInventoryCardIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:agentInventoryCardIndex.setStatus(_A)
_AgentInventoryCardType_Type=AgentInventoryCardType
_AgentInventoryCardType_Object=MibTableColumn
agentInventoryCardType=_AgentInventoryCardType_Object((1,3,6,1,4,1,4526,11,13,4,1,1,2),_AgentInventoryCardType_Type())
agentInventoryCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentInventoryCardType.setStatus(_A)
_AgentInventoryCardModelIdentifier_Type=DisplayString
_AgentInventoryCardModelIdentifier_Object=MibTableColumn
agentInventoryCardModelIdentifier=_AgentInventoryCardModelIdentifier_Object((1,3,6,1,4,1,4526,11,13,4,1,1,3),_AgentInventoryCardModelIdentifier_Type())
agentInventoryCardModelIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:agentInventoryCardModelIdentifier.setStatus(_A)
_AgentInventoryCardDescription_Type=DisplayString
_AgentInventoryCardDescription_Object=MibTableColumn
agentInventoryCardDescription=_AgentInventoryCardDescription_Object((1,3,6,1,4,1,4526,11,13,4,1,1,4),_AgentInventoryCardDescription_Type())
agentInventoryCardDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:agentInventoryCardDescription.setStatus(_A)
_AgentInventoryComponentGroup_ObjectIdentity=ObjectIdentity
agentInventoryComponentGroup=_AgentInventoryComponentGroup_ObjectIdentity((1,3,6,1,4,1,4526,11,13,5))
_AgentInventoryComponentTable_Object=MibTable
agentInventoryComponentTable=_AgentInventoryComponentTable_Object((1,3,6,1,4,1,4526,11,13,5,1))
if mibBuilder.loadTexts:agentInventoryComponentTable.setStatus(_A)
_AgentInventoryComponentEntry_Object=MibTableRow
agentInventoryComponentEntry=_AgentInventoryComponentEntry_Object((1,3,6,1,4,1,4526,11,13,5,1,1))
agentInventoryComponentEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:agentInventoryComponentEntry.setStatus(_A)
_AgentInventoryComponentIndex_Type=Unsigned32
_AgentInventoryComponentIndex_Object=MibTableColumn
agentInventoryComponentIndex=_AgentInventoryComponentIndex_Object((1,3,6,1,4,1,4526,11,13,5,1,1,1),_AgentInventoryComponentIndex_Type())
agentInventoryComponentIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:agentInventoryComponentIndex.setStatus(_A)
_AgentInventoryComponentMnemonic_Type=DisplayString
_AgentInventoryComponentMnemonic_Object=MibTableColumn
agentInventoryComponentMnemonic=_AgentInventoryComponentMnemonic_Object((1,3,6,1,4,1,4526,11,13,5,1,1,2),_AgentInventoryComponentMnemonic_Type())
agentInventoryComponentMnemonic.setMaxAccess(_B)
if mibBuilder.loadTexts:agentInventoryComponentMnemonic.setStatus(_A)
_AgentInventoryComponentName_Type=DisplayString
_AgentInventoryComponentName_Object=MibTableColumn
agentInventoryComponentName=_AgentInventoryComponentName_Object((1,3,6,1,4,1,4526,11,13,5,1,1,3),_AgentInventoryComponentName_Type())
agentInventoryComponentName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentInventoryComponentName.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'AgentInventoryUnitPreference':AgentInventoryUnitPreference,'AgentInventoryUnitType':AgentInventoryUnitType,'AgentInventoryCardType':AgentInventoryCardType,'fastPathInventory':fastPathInventory,'agentInventoryStackGroup':agentInventoryStackGroup,'agentInventoryStackSTKname':agentInventoryStackSTKname,'agentInventoryStackActivateSTK':agentInventoryStackActivateSTK,'agentInventoryStackDeleteSTK':agentInventoryStackDeleteSTK,'agentInventoryCardGroup':agentInventoryCardGroup,'agentInventoryCardTypeTable':agentInventoryCardTypeTable,'agentInventoryCardTypeEntry':agentInventoryCardTypeEntry,_H:agentInventoryCardIndex,'agentInventoryCardType':agentInventoryCardType,'agentInventoryCardModelIdentifier':agentInventoryCardModelIdentifier,'agentInventoryCardDescription':agentInventoryCardDescription,'agentInventoryComponentGroup':agentInventoryComponentGroup,'agentInventoryComponentTable':agentInventoryComponentTable,'agentInventoryComponentEntry':agentInventoryComponentEntry,_J:agentInventoryComponentIndex,'agentInventoryComponentMnemonic':agentInventoryComponentMnemonic,'agentInventoryComponentName':agentInventoryComponentName})