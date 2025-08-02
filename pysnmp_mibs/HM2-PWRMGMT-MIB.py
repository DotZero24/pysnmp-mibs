_I='hm2PSState'
_H='hm2PSUUnitIndex'
_G='not-accessible'
_F='hm2PSUSlotIndex'
_E='hm2PSID'
_D='HM2-PWRMGMT-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2ConfigurationMibs,=mibBuilder.importSymbols('HM2-TC-MIB','hm2ConfigurationMibs')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hm2PowerMgmtMib=ModuleIdentity((1,3,6,1,4,1,248,11,11))
if mibBuilder.loadTexts:hm2PowerMgmtMib.setRevisions(('2011-03-16 00:00',))
_Hm2PowerMgmtMibNotifications_ObjectIdentity=ObjectIdentity
hm2PowerMgmtMibNotifications=_Hm2PowerMgmtMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,11,0))
_Hm2PowerMgmtMibObjects_ObjectIdentity=ObjectIdentity
hm2PowerMgmtMibObjects=_Hm2PowerMgmtMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,11,1))
_Hm2PowerSupplyGroup_ObjectIdentity=ObjectIdentity
hm2PowerSupplyGroup=_Hm2PowerSupplyGroup_ObjectIdentity((1,3,6,1,4,1,248,11,11,1,1))
_Hm2PSTable_Object=MibTable
hm2PSTable=_Hm2PSTable_Object((1,3,6,1,4,1,248,11,11,1,1,1))
if mibBuilder.loadTexts:hm2PSTable.setStatus(_A)
_Hm2PSEntry_Object=MibTableRow
hm2PSEntry=_Hm2PSEntry_Object((1,3,6,1,4,1,248,11,11,1,1,1,1))
hm2PSEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hm2PSEntry.setStatus(_A)
class _Hm2PSID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Hm2PSID_Type.__name__=_C
_Hm2PSID_Object=MibTableColumn
hm2PSID=_Hm2PSID_Object((1,3,6,1,4,1,248,11,11,1,1,1,1,1),_Hm2PSID_Type())
hm2PSID.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSID.setStatus(_A)
class _Hm2PSState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('present',1),('defective',2),('notInstalled',3),('unknown',4)))
_Hm2PSState_Type.__name__=_C
_Hm2PSState_Object=MibTableColumn
hm2PSState=_Hm2PSState_Object((1,3,6,1,4,1,248,11,11,1,1,1,1,2),_Hm2PSState_Type())
hm2PSState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSState.setStatus(_A)
_Hm2PSUSlotInfoTable_Object=MibTable
hm2PSUSlotInfoTable=_Hm2PSUSlotInfoTable_Object((1,3,6,1,4,1,248,11,11,1,1,10))
if mibBuilder.loadTexts:hm2PSUSlotInfoTable.setStatus(_A)
_Hm2PSUSlotInfoEntry_Object=MibTableRow
hm2PSUSlotInfoEntry=_Hm2PSUSlotInfoEntry_Object((1,3,6,1,4,1,248,11,11,1,1,10,1))
hm2PSUSlotInfoEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hm2PSUSlotInfoEntry.setStatus(_A)
class _Hm2PSUSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Hm2PSUSlotIndex_Type.__name__=_C
_Hm2PSUSlotIndex_Object=MibTableColumn
hm2PSUSlotIndex=_Hm2PSUSlotIndex_Object((1,3,6,1,4,1,248,11,11,1,1,10,1,1),_Hm2PSUSlotIndex_Type())
hm2PSUSlotIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2PSUSlotIndex.setStatus(_A)
class _Hm2PSUSlotChassisTypeId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('other',0),('mach1020',1),('mach4000',2),('railswitch',3),('grs',4)))
_Hm2PSUSlotChassisTypeId_Type.__name__=_C
_Hm2PSUSlotChassisTypeId_Object=MibTableColumn
hm2PSUSlotChassisTypeId=_Hm2PSUSlotChassisTypeId_Object((1,3,6,1,4,1,248,11,11,1,1,10,1,2),_Hm2PSUSlotChassisTypeId_Type())
hm2PSUSlotChassisTypeId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUSlotChassisTypeId.setStatus(_A)
class _Hm2PSUSlotManufacturerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('other',0),('hirschmann',1)))
_Hm2PSUSlotManufacturerId_Type.__name__=_C
_Hm2PSUSlotManufacturerId_Object=MibTableColumn
hm2PSUSlotManufacturerId=_Hm2PSUSlotManufacturerId_Object((1,3,6,1,4,1,248,11,11,1,1,10,1,3),_Hm2PSUSlotManufacturerId_Type())
hm2PSUSlotManufacturerId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUSlotManufacturerId.setStatus(_A)
_Hm2PSUSlotManufacturerDate_Type=SnmpAdminString
_Hm2PSUSlotManufacturerDate_Object=MibTableColumn
hm2PSUSlotManufacturerDate=_Hm2PSUSlotManufacturerDate_Object((1,3,6,1,4,1,248,11,11,1,1,10,1,4),_Hm2PSUSlotManufacturerDate_Type())
hm2PSUSlotManufacturerDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUSlotManufacturerDate.setStatus('obsolete')
_Hm2PSUSlotSerialNumber_Type=SnmpAdminString
_Hm2PSUSlotSerialNumber_Object=MibTableColumn
hm2PSUSlotSerialNumber=_Hm2PSUSlotSerialNumber_Object((1,3,6,1,4,1,248,11,11,1,1,10,1,5),_Hm2PSUSlotSerialNumber_Type())
hm2PSUSlotSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUSlotSerialNumber.setStatus(_A)
_Hm2PSUSlotProductCode_Type=SnmpAdminString
_Hm2PSUSlotProductCode_Object=MibTableColumn
hm2PSUSlotProductCode=_Hm2PSUSlotProductCode_Object((1,3,6,1,4,1,248,11,11,1,1,10,1,6),_Hm2PSUSlotProductCode_Type())
hm2PSUSlotProductCode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUSlotProductCode.setStatus(_A)
_Hm2PSUSlotDescription_Type=SnmpAdminString
_Hm2PSUSlotDescription_Object=MibTableColumn
hm2PSUSlotDescription=_Hm2PSUSlotDescription_Object((1,3,6,1,4,1,248,11,11,1,1,10,1,7),_Hm2PSUSlotDescription_Type())
hm2PSUSlotDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUSlotDescription.setStatus(_A)
class _Hm2PSUSlotCombinationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('only-on-psu1',0),('psu1-sys-psu2-poe',1),('psu1-poe-psu2-sys',2),('two-separate-psus',3)))
_Hm2PSUSlotCombinationType_Type.__name__=_C
_Hm2PSUSlotCombinationType_Object=MibTableColumn
hm2PSUSlotCombinationType=_Hm2PSUSlotCombinationType_Object((1,3,6,1,4,1,248,11,11,1,1,10,1,8),_Hm2PSUSlotCombinationType_Type())
hm2PSUSlotCombinationType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUSlotCombinationType.setStatus(_A)
class _Hm2PSUSlotTemperatureRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('tr-0-60',0),('tr-minus40-60',1),('tr-minus40-70',2),('tr-minus40-70cc',3),('tr-minus40-85',4),('tr-minus40-85cc',5)))
_Hm2PSUSlotTemperatureRange_Type.__name__=_C
_Hm2PSUSlotTemperatureRange_Object=MibTableColumn
hm2PSUSlotTemperatureRange=_Hm2PSUSlotTemperatureRange_Object((1,3,6,1,4,1,248,11,11,1,1,10,1,9),_Hm2PSUSlotTemperatureRange_Type())
hm2PSUSlotTemperatureRange.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUSlotTemperatureRange.setStatus(_A)
class _Hm2PSUSlotRevisionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2PSUSlotRevisionId_Type.__name__=_C
_Hm2PSUSlotRevisionId_Object=MibTableColumn
hm2PSUSlotRevisionId=_Hm2PSUSlotRevisionId_Object((1,3,6,1,4,1,248,11,11,1,1,10,1,10),_Hm2PSUSlotRevisionId_Type())
hm2PSUSlotRevisionId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUSlotRevisionId.setStatus(_A)
_Hm2PSUUnitInfoTable_Object=MibTable
hm2PSUUnitInfoTable=_Hm2PSUUnitInfoTable_Object((1,3,6,1,4,1,248,11,11,1,1,20))
if mibBuilder.loadTexts:hm2PSUUnitInfoTable.setStatus(_A)
_Hm2PSUUnitInfoEntry_Object=MibTableRow
hm2PSUUnitInfoEntry=_Hm2PSUUnitInfoEntry_Object((1,3,6,1,4,1,248,11,11,1,1,20,1))
hm2PSUUnitInfoEntry.setIndexNames((0,_D,_F),(0,_D,_H))
if mibBuilder.loadTexts:hm2PSUUnitInfoEntry.setStatus(_A)
class _Hm2PSUUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Hm2PSUUnitIndex_Type.__name__=_C
_Hm2PSUUnitIndex_Object=MibTableColumn
hm2PSUUnitIndex=_Hm2PSUUnitIndex_Object((1,3,6,1,4,1,248,11,11,1,1,20,1,1),_Hm2PSUUnitIndex_Type())
hm2PSUUnitIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2PSUUnitIndex.setStatus(_A)
class _Hm2PSUUnitConverterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ac',1),('dc',2)))
_Hm2PSUUnitConverterType_Type.__name__=_C
_Hm2PSUUnitConverterType_Object=MibTableColumn
hm2PSUUnitConverterType=_Hm2PSUUnitConverterType_Object((1,3,6,1,4,1,248,11,11,1,1,20,1,2),_Hm2PSUUnitConverterType_Type())
hm2PSUUnitConverterType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUUnitConverterType.setStatus(_A)
class _Hm2PSUUnitNumberOfInputs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Hm2PSUUnitNumberOfInputs_Type.__name__=_C
_Hm2PSUUnitNumberOfInputs_Object=MibTableColumn
hm2PSUUnitNumberOfInputs=_Hm2PSUUnitNumberOfInputs_Object((1,3,6,1,4,1,248,11,11,1,1,20,1,3),_Hm2PSUUnitNumberOfInputs_Type())
hm2PSUUnitNumberOfInputs.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUUnitNumberOfInputs.setStatus(_A)
class _Hm2PSUUnitOutputType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('system',1),('both',2),('poe',3)))
_Hm2PSUUnitOutputType_Type.__name__=_C
_Hm2PSUUnitOutputType_Object=MibTableColumn
hm2PSUUnitOutputType=_Hm2PSUUnitOutputType_Object((1,3,6,1,4,1,248,11,11,1,1,20,1,4),_Hm2PSUUnitOutputType_Type())
hm2PSUUnitOutputType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUUnitOutputType.setStatus(_A)
class _Hm2PSUUnitSystemBudget_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Hm2PSUUnitSystemBudget_Type.__name__=_C
_Hm2PSUUnitSystemBudget_Object=MibTableColumn
hm2PSUUnitSystemBudget=_Hm2PSUUnitSystemBudget_Object((1,3,6,1,4,1,248,11,11,1,1,20,1,5),_Hm2PSUUnitSystemBudget_Type())
hm2PSUUnitSystemBudget.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUUnitSystemBudget.setStatus(_A)
class _Hm2PSUUnitPoeBudget_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Hm2PSUUnitPoeBudget_Type.__name__=_C
_Hm2PSUUnitPoeBudget_Object=MibTableColumn
hm2PSUUnitPoeBudget=_Hm2PSUUnitPoeBudget_Object((1,3,6,1,4,1,248,11,11,1,1,20,1,6),_Hm2PSUUnitPoeBudget_Type())
hm2PSUUnitPoeBudget.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUUnitPoeBudget.setStatus(_A)
class _Hm2PSUUnitFanCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Hm2PSUUnitFanCount_Type.__name__=_C
_Hm2PSUUnitFanCount_Object=MibTableColumn
hm2PSUUnitFanCount=_Hm2PSUUnitFanCount_Object((1,3,6,1,4,1,248,11,11,1,1,20,1,7),_Hm2PSUUnitFanCount_Type())
hm2PSUUnitFanCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUUnitFanCount.setStatus(_A)
class _Hm2PSUUnitVoltageRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('vr-18-60vdc',0),('vr-24-60vdc',1),('vr-24-48vdc',2),('vr-60-250vdc-110-240vac',3),('vr-48-54vdc-poe',4)))
_Hm2PSUUnitVoltageRange_Type.__name__=_C
_Hm2PSUUnitVoltageRange_Object=MibTableColumn
hm2PSUUnitVoltageRange=_Hm2PSUUnitVoltageRange_Object((1,3,6,1,4,1,248,11,11,1,1,20,1,8),_Hm2PSUUnitVoltageRange_Type())
hm2PSUUnitVoltageRange.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUUnitVoltageRange.setStatus(_A)
class _Hm2PSUUnitPowerInterruption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_Hm2PSUUnitPowerInterruption_Type.__name__=_C
_Hm2PSUUnitPowerInterruption_Object=MibTableColumn
hm2PSUUnitPowerInterruption=_Hm2PSUUnitPowerInterruption_Object((1,3,6,1,4,1,248,11,11,1,1,20,1,9),_Hm2PSUUnitPowerInterruption_Type())
hm2PSUUnitPowerInterruption.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PSUUnitPowerInterruption.setStatus(_A)
hm2PowerSupplyTrap=NotificationType((1,3,6,1,4,1,248,11,11,0,1))
hm2PowerSupplyTrap.setObjects(*((_D,_E),(_D,_I)))
if mibBuilder.loadTexts:hm2PowerSupplyTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hm2PowerMgmtMib':hm2PowerMgmtMib,'hm2PowerMgmtMibNotifications':hm2PowerMgmtMibNotifications,'hm2PowerSupplyTrap':hm2PowerSupplyTrap,'hm2PowerMgmtMibObjects':hm2PowerMgmtMibObjects,'hm2PowerSupplyGroup':hm2PowerSupplyGroup,'hm2PSTable':hm2PSTable,'hm2PSEntry':hm2PSEntry,_E:hm2PSID,_I:hm2PSState,'hm2PSUSlotInfoTable':hm2PSUSlotInfoTable,'hm2PSUSlotInfoEntry':hm2PSUSlotInfoEntry,_F:hm2PSUSlotIndex,'hm2PSUSlotChassisTypeId':hm2PSUSlotChassisTypeId,'hm2PSUSlotManufacturerId':hm2PSUSlotManufacturerId,'hm2PSUSlotManufacturerDate':hm2PSUSlotManufacturerDate,'hm2PSUSlotSerialNumber':hm2PSUSlotSerialNumber,'hm2PSUSlotProductCode':hm2PSUSlotProductCode,'hm2PSUSlotDescription':hm2PSUSlotDescription,'hm2PSUSlotCombinationType':hm2PSUSlotCombinationType,'hm2PSUSlotTemperatureRange':hm2PSUSlotTemperatureRange,'hm2PSUSlotRevisionId':hm2PSUSlotRevisionId,'hm2PSUUnitInfoTable':hm2PSUUnitInfoTable,'hm2PSUUnitInfoEntry':hm2PSUUnitInfoEntry,_H:hm2PSUUnitIndex,'hm2PSUUnitConverterType':hm2PSUUnitConverterType,'hm2PSUUnitNumberOfInputs':hm2PSUUnitNumberOfInputs,'hm2PSUUnitOutputType':hm2PSUUnitOutputType,'hm2PSUUnitSystemBudget':hm2PSUUnitSystemBudget,'hm2PSUUnitPoeBudget':hm2PSUUnitPoeBudget,'hm2PSUUnitFanCount':hm2PSUUnitFanCount,'hm2PSUUnitVoltageRange':hm2PSUUnitVoltageRange,'hm2PSUUnitPowerInterruption':hm2PSUUnitPowerInterruption})