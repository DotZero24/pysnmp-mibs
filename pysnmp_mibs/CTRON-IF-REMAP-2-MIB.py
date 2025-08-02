_U='ctIFRemap2VlanDestPort'
_T='ctIFRemap2VlanDestSlot'
_S='ctIFRemap2VlanSourceVlan'
_R='ctIFRemap2VlanSourceSlot'
_Q='ctIFRemap2SlotIndex'
_P='ctIFRemap2PortIndex'
_O='ctIFRemap2PortSlot'
_N='alwaysUntagged'
_M='alwaysTagged'
_L='unsupported'
_K='ctIFRemap2DestPort'
_J='ctIFRemap2DestSlot'
_I='ctIFRemap2SourcePort'
_H='ctIFRemap2SourceSlot'
_G='disable'
_F='enable'
_E='read-write'
_D='Integer32'
_C='CTRON-IF-REMAP-2-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctIFRemap2,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctIFRemap2')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtIFRemap2Config_ObjectIdentity=ObjectIdentity
ctIFRemap2Config=_CtIFRemap2Config_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,14,1))
_CtIFRemap2Table_Object=MibTable
ctIFRemap2Table=_CtIFRemap2Table_Object((1,3,6,1,4,1,52,4,1,1,14,1,1))
if mibBuilder.loadTexts:ctIFRemap2Table.setStatus(_A)
_CtIFRemap2Entry_Object=MibTableRow
ctIFRemap2Entry=_CtIFRemap2Entry_Object((1,3,6,1,4,1,52,4,1,1,14,1,1,1))
ctIFRemap2Entry.setIndexNames((0,_C,_H),(0,_C,_I),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:ctIFRemap2Entry.setStatus(_A)
_CtIFRemap2SourceSlot_Type=Integer32
_CtIFRemap2SourceSlot_Object=MibTableColumn
ctIFRemap2SourceSlot=_CtIFRemap2SourceSlot_Object((1,3,6,1,4,1,52,4,1,1,14,1,1,1,1),_CtIFRemap2SourceSlot_Type())
ctIFRemap2SourceSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIFRemap2SourceSlot.setStatus(_A)
_CtIFRemap2SourcePort_Type=Integer32
_CtIFRemap2SourcePort_Object=MibTableColumn
ctIFRemap2SourcePort=_CtIFRemap2SourcePort_Object((1,3,6,1,4,1,52,4,1,1,14,1,1,1,2),_CtIFRemap2SourcePort_Type())
ctIFRemap2SourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIFRemap2SourcePort.setStatus(_A)
_CtIFRemap2DestSlot_Type=Integer32
_CtIFRemap2DestSlot_Object=MibTableColumn
ctIFRemap2DestSlot=_CtIFRemap2DestSlot_Object((1,3,6,1,4,1,52,4,1,1,14,1,1,1,3),_CtIFRemap2DestSlot_Type())
ctIFRemap2DestSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIFRemap2DestSlot.setStatus(_A)
_CtIFRemap2DestPort_Type=Integer32
_CtIFRemap2DestPort_Object=MibTableColumn
ctIFRemap2DestPort=_CtIFRemap2DestPort_Object((1,3,6,1,4,1,52,4,1,1,14,1,1,1,4),_CtIFRemap2DestPort_Type())
ctIFRemap2DestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIFRemap2DestPort.setStatus(_A)
class _CtIFRemap2Status_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CtIFRemap2Status_Type.__name__=_D
_CtIFRemap2Status_Object=MibTableColumn
ctIFRemap2Status=_CtIFRemap2Status_Object((1,3,6,1,4,1,52,4,1,1,14,1,1,1,5),_CtIFRemap2Status_Type())
ctIFRemap2Status.setMaxAccess(_E)
if mibBuilder.loadTexts:ctIFRemap2Status.setStatus(_A)
class _CtIFRemap2PhysicalErrors_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3)))
_CtIFRemap2PhysicalErrors_Type.__name__=_D
_CtIFRemap2PhysicalErrors_Object=MibTableColumn
ctIFRemap2PhysicalErrors=_CtIFRemap2PhysicalErrors_Object((1,3,6,1,4,1,52,4,1,1,14,1,1,1,6),_CtIFRemap2PhysicalErrors_Type())
ctIFRemap2PhysicalErrors.setMaxAccess(_E)
if mibBuilder.loadTexts:ctIFRemap2PhysicalErrors.setStatus(_A)
class _CtIFRemap2EgressType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),(_M,2),(_N,3)))
_CtIFRemap2EgressType_Type.__name__=_D
_CtIFRemap2EgressType_Object=MibTableColumn
ctIFRemap2EgressType=_CtIFRemap2EgressType_Object((1,3,6,1,4,1,52,4,1,1,14,1,1,1,7),_CtIFRemap2EgressType_Type())
ctIFRemap2EgressType.setMaxAccess(_E)
if mibBuilder.loadTexts:ctIFRemap2EgressType.setStatus(_A)
_CtIFRemap2PortTable_Object=MibTable
ctIFRemap2PortTable=_CtIFRemap2PortTable_Object((1,3,6,1,4,1,52,4,1,1,14,1,2))
if mibBuilder.loadTexts:ctIFRemap2PortTable.setStatus(_A)
_CtIFRemap2PortEntry_Object=MibTableRow
ctIFRemap2PortEntry=_CtIFRemap2PortEntry_Object((1,3,6,1,4,1,52,4,1,1,14,1,2,1))
ctIFRemap2PortEntry.setIndexNames((0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:ctIFRemap2PortEntry.setStatus(_A)
_CtIFRemap2PortSlot_Type=Integer32
_CtIFRemap2PortSlot_Object=MibTableColumn
ctIFRemap2PortSlot=_CtIFRemap2PortSlot_Object((1,3,6,1,4,1,52,4,1,1,14,1,2,1,1),_CtIFRemap2PortSlot_Type())
ctIFRemap2PortSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIFRemap2PortSlot.setStatus(_A)
_CtIFRemap2PortIndex_Type=Integer32
_CtIFRemap2PortIndex_Object=MibTableColumn
ctIFRemap2PortIndex=_CtIFRemap2PortIndex_Object((1,3,6,1,4,1,52,4,1,1,14,1,2,1,2),_CtIFRemap2PortIndex_Type())
ctIFRemap2PortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIFRemap2PortIndex.setStatus(_A)
_CtIFRemap2PortReference_Type=ObjectIdentifier
_CtIFRemap2PortReference_Object=MibTableColumn
ctIFRemap2PortReference=_CtIFRemap2PortReference_Object((1,3,6,1,4,1,52,4,1,1,14,1,2,1,3),_CtIFRemap2PortReference_Type())
ctIFRemap2PortReference.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIFRemap2PortReference.setStatus(_A)
class _CtIFRemap2PhysErrsCapable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('supported',1),(_L,2)))
_CtIFRemap2PhysErrsCapable_Type.__name__=_D
_CtIFRemap2PhysErrsCapable_Object=MibTableColumn
ctIFRemap2PhysErrsCapable=_CtIFRemap2PhysErrsCapable_Object((1,3,6,1,4,1,52,4,1,1,14,1,2,1,4),_CtIFRemap2PhysErrsCapable_Type())
ctIFRemap2PhysErrsCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIFRemap2PhysErrsCapable.setStatus(_A)
_CtIFRemap2SlotTable_Object=MibTable
ctIFRemap2SlotTable=_CtIFRemap2SlotTable_Object((1,3,6,1,4,1,52,4,1,1,14,1,3))
if mibBuilder.loadTexts:ctIFRemap2SlotTable.setStatus(_A)
_CtIFRemap2SlotEntry_Object=MibTableRow
ctIFRemap2SlotEntry=_CtIFRemap2SlotEntry_Object((1,3,6,1,4,1,52,4,1,1,14,1,3,1))
ctIFRemap2SlotEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:ctIFRemap2SlotEntry.setStatus(_A)
_CtIFRemap2SlotIndex_Type=Integer32
_CtIFRemap2SlotIndex_Object=MibTableColumn
ctIFRemap2SlotIndex=_CtIFRemap2SlotIndex_Object((1,3,6,1,4,1,52,4,1,1,14,1,3,1,1),_CtIFRemap2SlotIndex_Type())
ctIFRemap2SlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIFRemap2SlotIndex.setStatus(_A)
_CtIFRemap2SlotMaxRemaps_Type=Integer32
_CtIFRemap2SlotMaxRemaps_Object=MibTableColumn
ctIFRemap2SlotMaxRemaps=_CtIFRemap2SlotMaxRemaps_Object((1,3,6,1,4,1,52,4,1,1,14,1,3,1,2),_CtIFRemap2SlotMaxRemaps_Type())
ctIFRemap2SlotMaxRemaps.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIFRemap2SlotMaxRemaps.setStatus(_A)
_CtIFRemap2SlotMaxRemoteDests_Type=Integer32
_CtIFRemap2SlotMaxRemoteDests_Object=MibTableColumn
ctIFRemap2SlotMaxRemoteDests=_CtIFRemap2SlotMaxRemoteDests_Object((1,3,6,1,4,1,52,4,1,1,14,1,3,1,3),_CtIFRemap2SlotMaxRemoteDests_Type())
ctIFRemap2SlotMaxRemoteDests.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIFRemap2SlotMaxRemoteDests.setStatus(_A)
_CtIFRemap2VlanTable_Object=MibTable
ctIFRemap2VlanTable=_CtIFRemap2VlanTable_Object((1,3,6,1,4,1,52,4,1,1,14,1,4))
if mibBuilder.loadTexts:ctIFRemap2VlanTable.setStatus(_A)
_CtIFRemap2VlanEntry_Object=MibTableRow
ctIFRemap2VlanEntry=_CtIFRemap2VlanEntry_Object((1,3,6,1,4,1,52,4,1,1,14,1,4,1))
ctIFRemap2VlanEntry.setIndexNames((0,_C,_R),(0,_C,_S),(0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:ctIFRemap2VlanEntry.setStatus(_A)
_CtIFRemap2VlanSourceSlot_Type=Integer32
_CtIFRemap2VlanSourceSlot_Object=MibTableColumn
ctIFRemap2VlanSourceSlot=_CtIFRemap2VlanSourceSlot_Object((1,3,6,1,4,1,52,4,1,1,14,1,4,1,1),_CtIFRemap2VlanSourceSlot_Type())
ctIFRemap2VlanSourceSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIFRemap2VlanSourceSlot.setStatus(_A)
_CtIFRemap2VlanSourceVlan_Type=Integer32
_CtIFRemap2VlanSourceVlan_Object=MibTableColumn
ctIFRemap2VlanSourceVlan=_CtIFRemap2VlanSourceVlan_Object((1,3,6,1,4,1,52,4,1,1,14,1,4,1,2),_CtIFRemap2VlanSourceVlan_Type())
ctIFRemap2VlanSourceVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIFRemap2VlanSourceVlan.setStatus(_A)
_CtIFRemap2VlanDestSlot_Type=Integer32
_CtIFRemap2VlanDestSlot_Object=MibTableColumn
ctIFRemap2VlanDestSlot=_CtIFRemap2VlanDestSlot_Object((1,3,6,1,4,1,52,4,1,1,14,1,4,1,3),_CtIFRemap2VlanDestSlot_Type())
ctIFRemap2VlanDestSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIFRemap2VlanDestSlot.setStatus(_A)
_CtIFRemap2VlanDestPort_Type=Integer32
_CtIFRemap2VlanDestPort_Object=MibTableColumn
ctIFRemap2VlanDestPort=_CtIFRemap2VlanDestPort_Object((1,3,6,1,4,1,52,4,1,1,14,1,4,1,4),_CtIFRemap2VlanDestPort_Type())
ctIFRemap2VlanDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ctIFRemap2VlanDestPort.setStatus(_A)
class _CtIFRemap2VlanStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CtIFRemap2VlanStatus_Type.__name__=_D
_CtIFRemap2VlanStatus_Object=MibTableColumn
ctIFRemap2VlanStatus=_CtIFRemap2VlanStatus_Object((1,3,6,1,4,1,52,4,1,1,14,1,4,1,5),_CtIFRemap2VlanStatus_Type())
ctIFRemap2VlanStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ctIFRemap2VlanStatus.setStatus(_A)
class _CtIFRemap2VlanEgressType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('received',1),(_M,2),(_N,3)))
_CtIFRemap2VlanEgressType_Type.__name__=_D
_CtIFRemap2VlanEgressType_Object=MibTableColumn
ctIFRemap2VlanEgressType=_CtIFRemap2VlanEgressType_Object((1,3,6,1,4,1,52,4,1,1,14,1,4,1,6),_CtIFRemap2VlanEgressType_Type())
ctIFRemap2VlanEgressType.setMaxAccess(_E)
if mibBuilder.loadTexts:ctIFRemap2VlanEgressType.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ctIFRemap2Config':ctIFRemap2Config,'ctIFRemap2Table':ctIFRemap2Table,'ctIFRemap2Entry':ctIFRemap2Entry,_H:ctIFRemap2SourceSlot,_I:ctIFRemap2SourcePort,_J:ctIFRemap2DestSlot,_K:ctIFRemap2DestPort,'ctIFRemap2Status':ctIFRemap2Status,'ctIFRemap2PhysicalErrors':ctIFRemap2PhysicalErrors,'ctIFRemap2EgressType':ctIFRemap2EgressType,'ctIFRemap2PortTable':ctIFRemap2PortTable,'ctIFRemap2PortEntry':ctIFRemap2PortEntry,_O:ctIFRemap2PortSlot,_P:ctIFRemap2PortIndex,'ctIFRemap2PortReference':ctIFRemap2PortReference,'ctIFRemap2PhysErrsCapable':ctIFRemap2PhysErrsCapable,'ctIFRemap2SlotTable':ctIFRemap2SlotTable,'ctIFRemap2SlotEntry':ctIFRemap2SlotEntry,_Q:ctIFRemap2SlotIndex,'ctIFRemap2SlotMaxRemaps':ctIFRemap2SlotMaxRemaps,'ctIFRemap2SlotMaxRemoteDests':ctIFRemap2SlotMaxRemoteDests,'ctIFRemap2VlanTable':ctIFRemap2VlanTable,'ctIFRemap2VlanEntry':ctIFRemap2VlanEntry,_R:ctIFRemap2VlanSourceSlot,_S:ctIFRemap2VlanSourceVlan,_T:ctIFRemap2VlanDestSlot,_U:ctIFRemap2VlanDestPort,'ctIFRemap2VlanStatus':ctIFRemap2VlanStatus,'ctIFRemap2VlanEgressType':ctIFRemap2VlanEgressType})