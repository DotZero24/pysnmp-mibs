_I='testing'
_H='slEntPhysicalIndex'
_G='SL-ENTITY-MIB'
_F='unknown'
_E='read-write'
_D='SnmpAdminString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
slMain,=mibBuilder.importSymbols('SL-MAIN-MIB','slMain')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
AutonomousType,DisplayString,PhysAddress,RowStatus,TAddress,TDomain,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','RowStatus','TAddress','TDomain','TextualConvention','TimeStamp','TruthValue')
slmEntity=ModuleIdentity((1,3,6,1,4,1,4515,1,3,6))
class PhysicalIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class PhysicalClass(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('other',1),(_F,2),('chassis',3),('backplane',4),('container',5),('powerSupply',6),('fan',7),('sensor',8),('module',9),('port',10),('stack',11)))
class PhysicalType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,90,91,92,93,94,95,96,97,98,99,100,800)));namedValues=NamedValues(*(('powerModule',1),('fanModule',2),('switchModule',3),('trunkModule',4),('oc12Module',5),('gbeModule',6),('fcModule',7),('passiveModule',8),('trunkModuleTransponding',9),('oc3Module',10),('ds3Module',11),('oc48tdmModule',12),('transpondingModule',13),('edfaModule',14),('transponding10GModule',15),('trunk10GModule',16),('esconModule',17),('gbeAggModule',18),('esconTrunkModule',19),('fc2gModule',20),('pl16000',90),('pl10',91),('pl20',92),('pl100',93),('pl400PmPiggy',94),('pl400MuxPiggy',95),('pl400',96),('pl1000',97),('pl200',98),('pl400E',99),(_F,100),('pl800',800)))
class CleiCode(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_SlEntityPhysical_ObjectIdentity=ObjectIdentity
slEntityPhysical=_SlEntityPhysical_ObjectIdentity((1,3,6,1,4,1,4515,1,3,6,1))
_SlEntPhysicalTable_Object=MibTable
slEntPhysicalTable=_SlEntPhysicalTable_Object((1,3,6,1,4,1,4515,1,3,6,1,1))
if mibBuilder.loadTexts:slEntPhysicalTable.setStatus(_A)
_SlEntPhysicalEntry_Object=MibTableRow
slEntPhysicalEntry=_SlEntPhysicalEntry_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1))
slEntPhysicalEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:slEntPhysicalEntry.setStatus(_A)
_SlEntPhysicalIndex_Type=InterfaceIndexOrZero
_SlEntPhysicalIndex_Object=MibTableColumn
slEntPhysicalIndex=_SlEntPhysicalIndex_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,1),_SlEntPhysicalIndex_Type())
slEntPhysicalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalIndex.setStatus(_A)
_SlEntPhysicalDescr_Type=SnmpAdminString
_SlEntPhysicalDescr_Object=MibTableColumn
slEntPhysicalDescr=_SlEntPhysicalDescr_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,2),_SlEntPhysicalDescr_Type())
slEntPhysicalDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalDescr.setStatus(_A)
_SlEntPhysicalClass_Type=PhysicalClass
_SlEntPhysicalClass_Object=MibTableColumn
slEntPhysicalClass=_SlEntPhysicalClass_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,3),_SlEntPhysicalClass_Type())
slEntPhysicalClass.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalClass.setStatus(_A)
_SlEntPhysicalHardwareRev_Type=SnmpAdminString
_SlEntPhysicalHardwareRev_Object=MibTableColumn
slEntPhysicalHardwareRev=_SlEntPhysicalHardwareRev_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,4),_SlEntPhysicalHardwareRev_Type())
slEntPhysicalHardwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalHardwareRev.setStatus(_A)
_SlEntPhysicalFirmwareRev_Type=SnmpAdminString
_SlEntPhysicalFirmwareRev_Object=MibTableColumn
slEntPhysicalFirmwareRev=_SlEntPhysicalFirmwareRev_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,5),_SlEntPhysicalFirmwareRev_Type())
slEntPhysicalFirmwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalFirmwareRev.setStatus(_A)
_SlEntPhysicalSoftwareRev_Type=SnmpAdminString
_SlEntPhysicalSoftwareRev_Object=MibTableColumn
slEntPhysicalSoftwareRev=_SlEntPhysicalSoftwareRev_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,6),_SlEntPhysicalSoftwareRev_Type())
slEntPhysicalSoftwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalSoftwareRev.setStatus(_A)
class _SlEntPhysicalSerialNum_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SlEntPhysicalSerialNum_Type.__name__=_D
_SlEntPhysicalSerialNum_Object=MibTableColumn
slEntPhysicalSerialNum=_SlEntPhysicalSerialNum_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,7),_SlEntPhysicalSerialNum_Type())
slEntPhysicalSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalSerialNum.setStatus(_A)
_SlEntPhysicalProtectionEntity_Type=PhysicalIndex
_SlEntPhysicalProtectionEntity_Object=MibTableColumn
slEntPhysicalProtectionEntity=_SlEntPhysicalProtectionEntity_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,8),_SlEntPhysicalProtectionEntity_Type())
slEntPhysicalProtectionEntity.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalProtectionEntity.setStatus(_A)
class _SlEntPhysicalProtectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('working',1),('protecting',2),('noProtection',3)))
_SlEntPhysicalProtectState_Type.__name__=_C
_SlEntPhysicalProtectState_Object=MibTableColumn
slEntPhysicalProtectState=_SlEntPhysicalProtectState_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,9),_SlEntPhysicalProtectState_Type())
slEntPhysicalProtectState.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalProtectState.setStatus(_A)
class _SlEntPhysicalProtectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('lock',1),('force',2),('automatic',3)))
_SlEntPhysicalProtectMode_Type.__name__=_C
_SlEntPhysicalProtectMode_Object=MibTableColumn
slEntPhysicalProtectMode=_SlEntPhysicalProtectMode_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,14),_SlEntPhysicalProtectMode_Type())
slEntPhysicalProtectMode.setMaxAccess(_E)
if mibBuilder.loadTexts:slEntPhysicalProtectMode.setStatus(_A)
class _SlEntPhysicalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_SlEntPhysicalStatus_Type.__name__=_C
_SlEntPhysicalStatus_Object=MibTableColumn
slEntPhysicalStatus=_SlEntPhysicalStatus_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,15),_SlEntPhysicalStatus_Type())
slEntPhysicalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalStatus.setStatus(_A)
_SlEntPhysicalFailureDescription_Type=SnmpAdminString
_SlEntPhysicalFailureDescription_Object=MibTableColumn
slEntPhysicalFailureDescription=_SlEntPhysicalFailureDescription_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,16),_SlEntPhysicalFailureDescription_Type())
slEntPhysicalFailureDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalFailureDescription.setStatus(_A)
class _SlEntPhysicalAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7)));namedValues=NamedValues(*(('up',1),('down',2),(_I,3),('warmBoot',4),('coldBoot',5),('hotBoot',7)))
_SlEntPhysicalAdminStatus_Type.__name__=_C
_SlEntPhysicalAdminStatus_Object=MibTableColumn
slEntPhysicalAdminStatus=_SlEntPhysicalAdminStatus_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,17),_SlEntPhysicalAdminStatus_Type())
slEntPhysicalAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:slEntPhysicalAdminStatus.setStatus(_A)
class _SlEntPhysicalOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,6)));namedValues=NamedValues(*(('up',1),('down',2),(_I,3),('notPresent',6)))
_SlEntPhysicalOperStatus_Type.__name__=_C
_SlEntPhysicalOperStatus_Object=MibTableColumn
slEntPhysicalOperStatus=_SlEntPhysicalOperStatus_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,18),_SlEntPhysicalOperStatus_Type())
slEntPhysicalOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalOperStatus.setStatus(_A)
_SlEntPhysicalSysUptime_Type=TimeTicks
_SlEntPhysicalSysUptime_Object=MibTableColumn
slEntPhysicalSysUptime=_SlEntPhysicalSysUptime_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,19),_SlEntPhysicalSysUptime_Type())
slEntPhysicalSysUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalSysUptime.setStatus(_A)
_SlEntPhysicalType_Type=PhysicalType
_SlEntPhysicalType_Object=MibTableColumn
slEntPhysicalType=_SlEntPhysicalType_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,20),_SlEntPhysicalType_Type())
slEntPhysicalType.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalType.setStatus(_A)
_SlEntPhysicalCleiCode_Type=CleiCode
_SlEntPhysicalCleiCode_Object=MibTableColumn
slEntPhysicalCleiCode=_SlEntPhysicalCleiCode_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,21),_SlEntPhysicalCleiCode_Type())
slEntPhysicalCleiCode.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalCleiCode.setStatus(_A)
class _SlEntPhysicalPartNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SlEntPhysicalPartNumber_Type.__name__=_D
_SlEntPhysicalPartNumber_Object=MibTableColumn
slEntPhysicalPartNumber=_SlEntPhysicalPartNumber_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,22),_SlEntPhysicalPartNumber_Type())
slEntPhysicalPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalPartNumber.setStatus(_A)
class _SlEntPhysicalOemSerialNum_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SlEntPhysicalOemSerialNum_Type.__name__=_D
_SlEntPhysicalOemSerialNum_Object=MibTableColumn
slEntPhysicalOemSerialNum=_SlEntPhysicalOemSerialNum_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,23),_SlEntPhysicalOemSerialNum_Type())
slEntPhysicalOemSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalOemSerialNum.setStatus(_A)
_SlEntPhysicalProductionDate_Type=SnmpAdminString
_SlEntPhysicalProductionDate_Object=MibTableColumn
slEntPhysicalProductionDate=_SlEntPhysicalProductionDate_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,24),_SlEntPhysicalProductionDate_Type())
slEntPhysicalProductionDate.setMaxAccess(_E)
if mibBuilder.loadTexts:slEntPhysicalProductionDate.setStatus(_A)
_SlEntPhysicalSysTemp_Type=Integer32
_SlEntPhysicalSysTemp_Object=MibTableColumn
slEntPhysicalSysTemp=_SlEntPhysicalSysTemp_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,25),_SlEntPhysicalSysTemp_Type())
slEntPhysicalSysTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalSysTemp.setStatus(_A)
_SlEntPhysicalSysAlias_Type=SnmpAdminString
_SlEntPhysicalSysAlias_Object=MibTableColumn
slEntPhysicalSysAlias=_SlEntPhysicalSysAlias_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,26),_SlEntPhysicalSysAlias_Type())
slEntPhysicalSysAlias.setMaxAccess(_E)
if mibBuilder.loadTexts:slEntPhysicalSysAlias.setStatus(_A)
_SlEntPhysicalSysSubType_Type=Integer32
_SlEntPhysicalSysSubType_Object=MibTableColumn
slEntPhysicalSysSubType=_SlEntPhysicalSysSubType_Object((1,3,6,1,4,1,4515,1,3,6,1,1,1,27),_SlEntPhysicalSysSubType_Type())
slEntPhysicalSysSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:slEntPhysicalSysSubType.setStatus(_A)
_SlEntityNotification_ObjectIdentity=ObjectIdentity
slEntityNotification=_SlEntityNotification_ObjectIdentity((1,3,6,1,4,1,4515,1,3,6,2))
mibBuilder.exportSymbols(_G,**{'PhysicalIndex':PhysicalIndex,'PhysicalClass':PhysicalClass,'PhysicalType':PhysicalType,'CleiCode':CleiCode,'slmEntity':slmEntity,'slEntityPhysical':slEntityPhysical,'slEntPhysicalTable':slEntPhysicalTable,'slEntPhysicalEntry':slEntPhysicalEntry,_H:slEntPhysicalIndex,'slEntPhysicalDescr':slEntPhysicalDescr,'slEntPhysicalClass':slEntPhysicalClass,'slEntPhysicalHardwareRev':slEntPhysicalHardwareRev,'slEntPhysicalFirmwareRev':slEntPhysicalFirmwareRev,'slEntPhysicalSoftwareRev':slEntPhysicalSoftwareRev,'slEntPhysicalSerialNum':slEntPhysicalSerialNum,'slEntPhysicalProtectionEntity':slEntPhysicalProtectionEntity,'slEntPhysicalProtectState':slEntPhysicalProtectState,'slEntPhysicalProtectMode':slEntPhysicalProtectMode,'slEntPhysicalStatus':slEntPhysicalStatus,'slEntPhysicalFailureDescription':slEntPhysicalFailureDescription,'slEntPhysicalAdminStatus':slEntPhysicalAdminStatus,'slEntPhysicalOperStatus':slEntPhysicalOperStatus,'slEntPhysicalSysUptime':slEntPhysicalSysUptime,'slEntPhysicalType':slEntPhysicalType,'slEntPhysicalCleiCode':slEntPhysicalCleiCode,'slEntPhysicalPartNumber':slEntPhysicalPartNumber,'slEntPhysicalOemSerialNum':slEntPhysicalOemSerialNum,'slEntPhysicalProductionDate':slEntPhysicalProductionDate,'slEntPhysicalSysTemp':slEntPhysicalSysTemp,'slEntPhysicalSysAlias':slEntPhysicalSysAlias,'slEntPhysicalSysSubType':slEntPhysicalSysSubType,'slEntityNotification':slEntityNotification})