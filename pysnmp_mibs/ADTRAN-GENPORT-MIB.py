_Z='adGenPortBaseGroup'
_Y='adGenIfCustomerUse'
_X='adGenIfIfIndex'
_W='adGenPortIfType'
_V='adGenPortAddress'
_U='adGenSlotAddress'
_T='adGenPortFarEndID'
_S='adGenPortTrapSeverity'
_R='adGenPortTrapIdentifier'
_Q='adGenPortCustomerUse'
_P='adGenPortAlarmStatus'
_O='adGenPortFarEndIP'
_N='adGenPortDataRate'
_M='adGenPortIfIndex'
_L='adGenPortInfoState'
_K='ifIndex'
_J='IF-MIB'
_I='adGenIfTypeIndex'
_H='adGenPortInfoIndex'
_G='adGenSlotInfoIndex'
_F='ADTRAN-GENSLOT-MIB'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='ADTRAN-GENPORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenericShelves,=mibBuilder.importSymbols('ADTRAN-GENCHASSIS-MIB','adGenericShelves')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_F,_G)
AdAlarmSeverity,AdPresence,AdProductIdentifier=mibBuilder.importSymbols('ADTRAN-TC','AdAlarmSeverity','AdPresence','AdProductIdentifier')
ifIndex,=mibBuilder.importSymbols(_J,_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenPort=ModuleIdentity((1,3,6,1,4,1,664,5,13,3))
_AdGenPortInfoTable_Object=MibTable
adGenPortInfoTable=_AdGenPortInfoTable_Object((1,3,6,1,4,1,664,5,13,3,3))
if mibBuilder.loadTexts:adGenPortInfoTable.setStatus(_A)
_AdGenPortInfoEntry_Object=MibTableRow
adGenPortInfoEntry=_AdGenPortInfoEntry_Object((1,3,6,1,4,1,664,5,13,3,3,1))
adGenPortInfoEntry.setIndexNames((0,_F,_G),(0,_B,_H))
if mibBuilder.loadTexts:adGenPortInfoEntry.setStatus(_A)
class _AdGenPortInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenPortInfoIndex_Type.__name__=_E
_AdGenPortInfoIndex_Object=MibTableColumn
adGenPortInfoIndex=_AdGenPortInfoIndex_Object((1,3,6,1,4,1,664,5,13,3,3,1,1),_AdGenPortInfoIndex_Type())
adGenPortInfoIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPortInfoIndex.setStatus(_A)
_AdGenPortInfoState_Type=AdPresence
_AdGenPortInfoState_Object=MibTableColumn
adGenPortInfoState=_AdGenPortInfoState_Object((1,3,6,1,4,1,664,5,13,3,3,1,3),_AdGenPortInfoState_Type())
adGenPortInfoState.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPortInfoState.setStatus(_A)
_AdGenPortIfIndex_Type=Integer32
_AdGenPortIfIndex_Object=MibTableColumn
adGenPortIfIndex=_AdGenPortIfIndex_Object((1,3,6,1,4,1,664,5,13,3,3,1,4),_AdGenPortIfIndex_Type())
adGenPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPortIfIndex.setStatus(_A)
_AdGenPortDataRate_Type=Integer32
_AdGenPortDataRate_Object=MibTableColumn
adGenPortDataRate=_AdGenPortDataRate_Object((1,3,6,1,4,1,664,5,13,3,3,1,6),_AdGenPortDataRate_Type())
adGenPortDataRate.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPortDataRate.setStatus(_A)
_AdGenPortFarEndIP_Type=IpAddress
_AdGenPortFarEndIP_Object=MibTableColumn
adGenPortFarEndIP=_AdGenPortFarEndIP_Object((1,3,6,1,4,1,664,5,13,3,3,1,8),_AdGenPortFarEndIP_Type())
adGenPortFarEndIP.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPortFarEndIP.setStatus(_A)
_AdGenPortAlarmStatus_Type=OctetString
_AdGenPortAlarmStatus_Object=MibTableColumn
adGenPortAlarmStatus=_AdGenPortAlarmStatus_Object((1,3,6,1,4,1,664,5,13,3,3,1,9),_AdGenPortAlarmStatus_Type())
adGenPortAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPortAlarmStatus.setStatus(_A)
_AdGenPortCustomerUse_Type=DisplayString
_AdGenPortCustomerUse_Object=MibTableColumn
adGenPortCustomerUse=_AdGenPortCustomerUse_Object((1,3,6,1,4,1,664,5,13,3,3,1,10),_AdGenPortCustomerUse_Type())
adGenPortCustomerUse.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPortCustomerUse.setStatus(_A)
_AdGenPortTrapIdentifier_Type=DisplayString
_AdGenPortTrapIdentifier_Object=MibTableColumn
adGenPortTrapIdentifier=_AdGenPortTrapIdentifier_Object((1,3,6,1,4,1,664,5,13,3,3,1,11),_AdGenPortTrapIdentifier_Type())
adGenPortTrapIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPortTrapIdentifier.setStatus(_A)
_AdGenPortTrapSeverity_Type=AdAlarmSeverity
_AdGenPortTrapSeverity_Object=MibTableColumn
adGenPortTrapSeverity=_AdGenPortTrapSeverity_Object((1,3,6,1,4,1,664,5,13,3,3,1,12),_AdGenPortTrapSeverity_Type())
adGenPortTrapSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPortTrapSeverity.setStatus(_A)
_AdGenPortFarEndID_Type=AdProductIdentifier
_AdGenPortFarEndID_Object=MibTableColumn
adGenPortFarEndID=_AdGenPortFarEndID_Object((1,3,6,1,4,1,664,5,13,3,3,1,14),_AdGenPortFarEndID_Type())
adGenPortFarEndID.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPortFarEndID.setStatus(_A)
_AdGenPortSlotMapTable_Object=MibTable
adGenPortSlotMapTable=_AdGenPortSlotMapTable_Object((1,3,6,1,4,1,664,5,13,3,4))
if mibBuilder.loadTexts:adGenPortSlotMapTable.setStatus(_A)
_AdGenPortSlotMapEntry_Object=MibTableRow
adGenPortSlotMapEntry=_AdGenPortSlotMapEntry_Object((1,3,6,1,4,1,664,5,13,3,4,1))
adGenPortSlotMapEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:adGenPortSlotMapEntry.setStatus(_A)
class _AdGenSlotAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenSlotAddress_Type.__name__=_E
_AdGenSlotAddress_Object=MibTableColumn
adGenSlotAddress=_AdGenSlotAddress_Object((1,3,6,1,4,1,664,5,13,3,4,1,2),_AdGenSlotAddress_Type())
adGenSlotAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotAddress.setStatus(_A)
class _AdGenPortAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenPortAddress_Type.__name__=_E
_AdGenPortAddress_Object=MibTableColumn
adGenPortAddress=_AdGenPortAddress_Object((1,3,6,1,4,1,664,5,13,3,4,1,3),_AdGenPortAddress_Type())
adGenPortAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPortAddress.setStatus(_A)
_AdGenPortIfType_Type=Integer32
_AdGenPortIfType_Object=MibTableColumn
adGenPortIfType=_AdGenPortIfType_Object((1,3,6,1,4,1,664,5,13,3,4,1,4),_AdGenPortIfType_Type())
adGenPortIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPortIfType.setStatus(_A)
_AdGenPortIfInfoTable_Object=MibTable
adGenPortIfInfoTable=_AdGenPortIfInfoTable_Object((1,3,6,1,4,1,664,5,13,3,5))
if mibBuilder.loadTexts:adGenPortIfInfoTable.setStatus(_A)
_AdGenPortIfInfoEntry_Object=MibTableRow
adGenPortIfInfoEntry=_AdGenPortIfInfoEntry_Object((1,3,6,1,4,1,664,5,13,3,5,1))
adGenPortIfInfoEntry.setIndexNames((0,_F,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:adGenPortIfInfoEntry.setStatus(_A)
_AdGenIfTypeIndex_Type=Integer32
_AdGenIfTypeIndex_Object=MibTableColumn
adGenIfTypeIndex=_AdGenIfTypeIndex_Object((1,3,6,1,4,1,664,5,13,3,5,1,1),_AdGenIfTypeIndex_Type())
adGenIfTypeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIfTypeIndex.setStatus(_A)
_AdGenIfIfIndex_Type=Integer32
_AdGenIfIfIndex_Object=MibTableColumn
adGenIfIfIndex=_AdGenIfIfIndex_Object((1,3,6,1,4,1,664,5,13,3,5,1,4),_AdGenIfIfIndex_Type())
adGenIfIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIfIfIndex.setStatus(_A)
_AdGenIfCustomerUse_Type=DisplayString
_AdGenIfCustomerUse_Object=MibTableColumn
adGenIfCustomerUse=_AdGenIfCustomerUse_Object((1,3,6,1,4,1,664,5,13,3,5,1,10),_AdGenIfCustomerUse_Type())
adGenIfCustomerUse.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenIfCustomerUse.setStatus(_A)
_AdGenPortConformance_ObjectIdentity=ObjectIdentity
adGenPortConformance=_AdGenPortConformance_ObjectIdentity((1,3,6,1,4,1,664,5,13,3,99))
_AdGenPortCompliances_ObjectIdentity=ObjectIdentity
adGenPortCompliances=_AdGenPortCompliances_ObjectIdentity((1,3,6,1,4,1,664,5,13,3,99,1))
_AdGenPortMIBGroups_ObjectIdentity=ObjectIdentity
adGenPortMIBGroups=_AdGenPortMIBGroups_ObjectIdentity((1,3,6,1,4,1,664,5,13,3,99,2))
adGenPortBaseGroup=ObjectGroup((1,3,6,1,4,1,664,5,13,3,99,2,1))
adGenPortBaseGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_I),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:adGenPortBaseGroup.setStatus(_A)
adGenPortCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,13,3,99,1,1))
adGenPortCompliance.setObjects((_B,_Z))
if mibBuilder.loadTexts:adGenPortCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenPort':adGenPort,'adGenPortInfoTable':adGenPortInfoTable,'adGenPortInfoEntry':adGenPortInfoEntry,_H:adGenPortInfoIndex,_L:adGenPortInfoState,_M:adGenPortIfIndex,_N:adGenPortDataRate,_O:adGenPortFarEndIP,_P:adGenPortAlarmStatus,_Q:adGenPortCustomerUse,_R:adGenPortTrapIdentifier,_S:adGenPortTrapSeverity,_T:adGenPortFarEndID,'adGenPortSlotMapTable':adGenPortSlotMapTable,'adGenPortSlotMapEntry':adGenPortSlotMapEntry,_U:adGenSlotAddress,_V:adGenPortAddress,_W:adGenPortIfType,'adGenPortIfInfoTable':adGenPortIfInfoTable,'adGenPortIfInfoEntry':adGenPortIfInfoEntry,_I:adGenIfTypeIndex,_X:adGenIfIfIndex,_Y:adGenIfCustomerUse,'adGenPortConformance':adGenPortConformance,'adGenPortCompliances':adGenPortCompliances,'adGenPortCompliance':adGenPortCompliance,'adGenPortMIBGroups':adGenPortMIBGroups,_Z:adGenPortBaseGroup})