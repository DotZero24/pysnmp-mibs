_X='tnFanUnitGroup'
_W='tnFanUnitSpeedControl'
_V='tnFanUnitStatusLEDState'
_U='tnFanUnitStatusLEDColor'
_T='tnFanUnitSpeed'
_S='tnFanUnitPower'
_R='tnFanUnitSWGenericLoadName'
_Q='tnFanUnitMarketingPartNumber'
_P='tnFanUnitManufacturingPartNumber'
_O='tnFanUnitSerialNumber'
_N='tnFanUnitHFD'
_M='tnFanUnitCLEI'
_L='tnFanUnitDescr'
_K='tnFanUnitName'
_J='tnSlotIndex'
_I='TROPIC-SLOT-MIB'
_H='tnShelfIndex'
_G='TROPIC-SHELF-MIB'
_F='Integer32'
_E='read-create'
_D='SnmpAdminString'
_C='read-only'
_B='TROPIC-FAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tnFanMIB,tnMiscModules=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnFanMIB','tnMiscModules')
tnShelfIndex,=mibBuilder.importSymbols(_G,_H)
tnSlotIndex,=mibBuilder.importSymbols(_I,_J)
TropicCardCLEI,TropicCardHFD,TropicCardManufacturingPartNumber,TropicCardMarketingPartNumber,TropicCardSWGenericLoadName,TropicCardSerialNumber,TropicLEDColorType,TropicLEDStateType=mibBuilder.importSymbols('TROPIC-TC','TropicCardCLEI','TropicCardHFD','TropicCardManufacturingPartNumber','TropicCardMarketingPartNumber','TropicCardSWGenericLoadName','TropicCardSerialNumber','TropicLEDColorType','TropicLEDStateType')
tnFanMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,2,5,1))
if mibBuilder.loadTexts:tnFanMibModule.setRevisions(('2018-02-23 12:00','2016-11-16 12:00','2013-05-21 12:00','2010-02-16 12:00','2008-03-20 12:00'))
_TnFanConf_ObjectIdentity=ObjectIdentity
tnFanConf=_TnFanConf_ObjectIdentity((1,3,6,1,4,1,7483,2,2,5,1,1))
_TnFanGroups_ObjectIdentity=ObjectIdentity
tnFanGroups=_TnFanGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,2,5,1,1,1))
_TnFanCompliances_ObjectIdentity=ObjectIdentity
tnFanCompliances=_TnFanCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,2,5,1,1,2))
_TnFanObjs_ObjectIdentity=ObjectIdentity
tnFanObjs=_TnFanObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,2,5,1,2))
_TnFanBasics_ObjectIdentity=ObjectIdentity
tnFanBasics=_TnFanBasics_ObjectIdentity((1,3,6,1,4,1,7483,2,2,5,1,2,1))
_TnFanUnitTable_Object=MibTable
tnFanUnitTable=_TnFanUnitTable_Object((1,3,6,1,4,1,7483,2,2,5,1,2,1,2))
if mibBuilder.loadTexts:tnFanUnitTable.setStatus(_A)
_TnFanUnitEntry_Object=MibTableRow
tnFanUnitEntry=_TnFanUnitEntry_Object((1,3,6,1,4,1,7483,2,2,5,1,2,1,2,1))
tnFanUnitEntry.setIndexNames((0,_G,_H),(0,_I,_J))
if mibBuilder.loadTexts:tnFanUnitEntry.setStatus(_A)
class _TnFanUnitName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TnFanUnitName_Type.__name__=_D
_TnFanUnitName_Object=MibTableColumn
tnFanUnitName=_TnFanUnitName_Object((1,3,6,1,4,1,7483,2,2,5,1,2,1,2,1,1),_TnFanUnitName_Type())
tnFanUnitName.setMaxAccess(_E)
if mibBuilder.loadTexts:tnFanUnitName.setStatus(_A)
class _TnFanUnitDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnFanUnitDescr_Type.__name__=_D
_TnFanUnitDescr_Object=MibTableColumn
tnFanUnitDescr=_TnFanUnitDescr_Object((1,3,6,1,4,1,7483,2,2,5,1,2,1,2,1,2),_TnFanUnitDescr_Type())
tnFanUnitDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:tnFanUnitDescr.setStatus(_A)
_TnFanUnitCLEI_Type=TropicCardCLEI
_TnFanUnitCLEI_Object=MibTableColumn
tnFanUnitCLEI=_TnFanUnitCLEI_Object((1,3,6,1,4,1,7483,2,2,5,1,2,1,2,1,3),_TnFanUnitCLEI_Type())
tnFanUnitCLEI.setMaxAccess(_C)
if mibBuilder.loadTexts:tnFanUnitCLEI.setStatus(_A)
_TnFanUnitHFD_Type=TropicCardHFD
_TnFanUnitHFD_Object=MibTableColumn
tnFanUnitHFD=_TnFanUnitHFD_Object((1,3,6,1,4,1,7483,2,2,5,1,2,1,2,1,4),_TnFanUnitHFD_Type())
tnFanUnitHFD.setMaxAccess(_C)
if mibBuilder.loadTexts:tnFanUnitHFD.setStatus(_A)
_TnFanUnitSerialNumber_Type=TropicCardSerialNumber
_TnFanUnitSerialNumber_Object=MibTableColumn
tnFanUnitSerialNumber=_TnFanUnitSerialNumber_Object((1,3,6,1,4,1,7483,2,2,5,1,2,1,2,1,5),_TnFanUnitSerialNumber_Type())
tnFanUnitSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tnFanUnitSerialNumber.setStatus(_A)
_TnFanUnitManufacturingPartNumber_Type=TropicCardManufacturingPartNumber
_TnFanUnitManufacturingPartNumber_Object=MibTableColumn
tnFanUnitManufacturingPartNumber=_TnFanUnitManufacturingPartNumber_Object((1,3,6,1,4,1,7483,2,2,5,1,2,1,2,1,6),_TnFanUnitManufacturingPartNumber_Type())
tnFanUnitManufacturingPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tnFanUnitManufacturingPartNumber.setStatus(_A)
_TnFanUnitMarketingPartNumber_Type=TropicCardMarketingPartNumber
_TnFanUnitMarketingPartNumber_Object=MibTableColumn
tnFanUnitMarketingPartNumber=_TnFanUnitMarketingPartNumber_Object((1,3,6,1,4,1,7483,2,2,5,1,2,1,2,1,7),_TnFanUnitMarketingPartNumber_Type())
tnFanUnitMarketingPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tnFanUnitMarketingPartNumber.setStatus(_A)
_TnFanUnitSWGenericLoadName_Type=TropicCardSWGenericLoadName
_TnFanUnitSWGenericLoadName_Object=MibTableColumn
tnFanUnitSWGenericLoadName=_TnFanUnitSWGenericLoadName_Object((1,3,6,1,4,1,7483,2,2,5,1,2,1,2,1,8),_TnFanUnitSWGenericLoadName_Type())
tnFanUnitSWGenericLoadName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnFanUnitSWGenericLoadName.setStatus(_A)
_TnFanUnitPower_Type=Integer32
_TnFanUnitPower_Object=MibTableColumn
tnFanUnitPower=_TnFanUnitPower_Object((1,3,6,1,4,1,7483,2,2,5,1,2,1,2,1,9),_TnFanUnitPower_Type())
tnFanUnitPower.setMaxAccess(_C)
if mibBuilder.loadTexts:tnFanUnitPower.setStatus(_A)
_TnFanUnitSpeed_Type=Integer32
_TnFanUnitSpeed_Object=MibTableColumn
tnFanUnitSpeed=_TnFanUnitSpeed_Object((1,3,6,1,4,1,7483,2,2,5,1,2,1,2,1,10),_TnFanUnitSpeed_Type())
tnFanUnitSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:tnFanUnitSpeed.setStatus(_A)
if mibBuilder.loadTexts:tnFanUnitSpeed.setUnits('RPM')
_TnFanUnitStatusLEDColor_Type=TropicLEDColorType
_TnFanUnitStatusLEDColor_Object=MibTableColumn
tnFanUnitStatusLEDColor=_TnFanUnitStatusLEDColor_Object((1,3,6,1,4,1,7483,2,2,5,1,2,1,2,1,11),_TnFanUnitStatusLEDColor_Type())
tnFanUnitStatusLEDColor.setMaxAccess(_C)
if mibBuilder.loadTexts:tnFanUnitStatusLEDColor.setStatus(_A)
_TnFanUnitStatusLEDState_Type=TropicLEDStateType
_TnFanUnitStatusLEDState_Object=MibTableColumn
tnFanUnitStatusLEDState=_TnFanUnitStatusLEDState_Object((1,3,6,1,4,1,7483,2,2,5,1,2,1,2,1,12),_TnFanUnitStatusLEDState_Type())
tnFanUnitStatusLEDState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnFanUnitStatusLEDState.setStatus(_A)
class _TnFanUnitSpeedControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('maximum',2)))
_TnFanUnitSpeedControl_Type.__name__=_F
_TnFanUnitSpeedControl_Object=MibTableColumn
tnFanUnitSpeedControl=_TnFanUnitSpeedControl_Object((1,3,6,1,4,1,7483,2,2,5,1,2,1,2,1,13),_TnFanUnitSpeedControl_Type())
tnFanUnitSpeedControl.setMaxAccess(_E)
if mibBuilder.loadTexts:tnFanUnitSpeedControl.setStatus(_A)
tnFanUnitGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,5,1,1,1,2))
tnFanUnitGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:tnFanUnitGroup.setStatus(_A)
tnFanCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,2,5,1,1,2,1))
tnFanCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:tnFanCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tnFanMibModule':tnFanMibModule,'tnFanConf':tnFanConf,'tnFanGroups':tnFanGroups,_X:tnFanUnitGroup,'tnFanCompliances':tnFanCompliances,'tnFanCompliance':tnFanCompliance,'tnFanObjs':tnFanObjs,'tnFanBasics':tnFanBasics,'tnFanUnitTable':tnFanUnitTable,'tnFanUnitEntry':tnFanUnitEntry,_K:tnFanUnitName,_L:tnFanUnitDescr,_M:tnFanUnitCLEI,_N:tnFanUnitHFD,_O:tnFanUnitSerialNumber,_P:tnFanUnitManufacturingPartNumber,_Q:tnFanUnitMarketingPartNumber,_R:tnFanUnitSWGenericLoadName,_S:tnFanUnitPower,_T:tnFanUnitSpeed,_U:tnFanUnitStatusLEDColor,_V:tnFanUnitStatusLEDState,_W:tnFanUnitSpeedControl})