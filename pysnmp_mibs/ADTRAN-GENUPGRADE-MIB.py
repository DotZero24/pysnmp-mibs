_M='NotificationType'
_L='optional'
_K='adGenUpgradeFailureStatus'
_J='ADTRAN-GENUPGRADE-MIB'
_I='sysName'
_H='SNMPv2-MIB'
_G='adTrapInformSeqNum'
_F='ADTRAN-GENTRAPINFORM-MIB'
_E='Integer32'
_D='adGenSlotInfoIndex'
_C='ADTRAN-GENSLOT-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenericShelves,=mibBuilder.importSymbols('ADTRAN-GENCHASSIS-MIB','adGenericShelves')
adGenSlotAlarmStatus,adGenSlotInfoIndex=mibBuilder.importSymbols(_C,'adGenSlotAlarmStatus',_D)
adTrapInformSeqNum,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_H,_I)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_M,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_M,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_AdGenUpgrade_ObjectIdentity=ObjectIdentity
adGenUpgrade=_AdGenUpgrade_ObjectIdentity((1,3,6,1,4,1,664,5,13,4))
_AdGenUpgradeStatus_ObjectIdentity=ObjectIdentity
adGenUpgradeStatus=_AdGenUpgradeStatus_ObjectIdentity((1,3,6,1,4,1,664,5,13,4,1))
_AdGenUpgradeStatusTable_Object=MibTable
adGenUpgradeStatusTable=_AdGenUpgradeStatusTable_Object((1,3,6,1,4,1,664,5,13,4,1,1))
if mibBuilder.loadTexts:adGenUpgradeStatusTable.setStatus(_A)
_AdGenUpgradeStatusEntry_Object=MibTableRow
adGenUpgradeStatusEntry=_AdGenUpgradeStatusEntry_Object((1,3,6,1,4,1,664,5,13,4,1,1,1))
adGenUpgradeStatusEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenUpgradeStatusEntry.setStatus(_A)
class _AdGenUpgradeFailureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noFailure',1),('genericFailure',2),('ymodemProtocolFailure',3),('wrongSoftwareSentFailure',4),('softwareValidationFailure',5)))
_AdGenUpgradeFailureStatus_Type.__name__=_E
_AdGenUpgradeFailureStatus_Object=MibTableColumn
adGenUpgradeFailureStatus=_AdGenUpgradeFailureStatus_Object((1,3,6,1,4,1,664,5,13,4,1,1,1,1),_AdGenUpgradeFailureStatus_Type())
adGenUpgradeFailureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenUpgradeFailureStatus.setStatus(_A)
class _AdGenUpgradeSoftwareStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('upgradeNotInProgress',1),('ymodemNegotiation',2),('ymodemInProgress',3),('tftpNegotiation',4),('tftpInProgress',5),('validatingSoftware',6),('erasingEntireSoftware',7),('erasingNonBootblockSoftware',8),('writingSoftware',9),('rebooting',10)))
_AdGenUpgradeSoftwareStatus_Type.__name__=_E
_AdGenUpgradeSoftwareStatus_Object=MibTableColumn
adGenUpgradeSoftwareStatus=_AdGenUpgradeSoftwareStatus_Object((1,3,6,1,4,1,664,5,13,4,1,1,1,2),_AdGenUpgradeSoftwareStatus_Type())
adGenUpgradeSoftwareStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenUpgradeSoftwareStatus.setStatus(_L)
class _AdGenUpgradeSoftwarePercentageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,101))
_AdGenUpgradeSoftwarePercentageStatus_Type.__name__=_E
_AdGenUpgradeSoftwarePercentageStatus_Object=MibTableColumn
adGenUpgradeSoftwarePercentageStatus=_AdGenUpgradeSoftwarePercentageStatus_Object((1,3,6,1,4,1,664,5,13,4,1,1,1,3),_AdGenUpgradeSoftwarePercentageStatus_Type())
adGenUpgradeSoftwarePercentageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenUpgradeSoftwarePercentageStatus.setStatus(_L)
class _AdGenUpgradeSwUpgradeability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upgradeable',1),('notUpgradeable',2)))
_AdGenUpgradeSwUpgradeability_Type.__name__=_E
_AdGenUpgradeSwUpgradeability_Object=MibTableColumn
adGenUpgradeSwUpgradeability=_AdGenUpgradeSwUpgradeability_Object((1,3,6,1,4,1,664,5,13,4,1,1,1,4),_AdGenUpgradeSwUpgradeability_Type())
adGenUpgradeSwUpgradeability.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenUpgradeSwUpgradeability.setStatus(_A)
_AdGenUpgradeConfig_ObjectIdentity=ObjectIdentity
adGenUpgradeConfig=_AdGenUpgradeConfig_ObjectIdentity((1,3,6,1,4,1,664,5,13,4,2))
_AdGenUpgradeConfigTable_Object=MibTable
adGenUpgradeConfigTable=_AdGenUpgradeConfigTable_Object((1,3,6,1,4,1,664,5,13,4,2,1))
if mibBuilder.loadTexts:adGenUpgradeConfigTable.setStatus(_A)
_AdGenUpgradeConfigEntry_Object=MibTableRow
adGenUpgradeConfigEntry=_AdGenUpgradeConfigEntry_Object((1,3,6,1,4,1,664,5,13,4,2,1,1))
adGenUpgradeConfigEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenUpgradeConfigEntry.setStatus(_A)
class _AdGenUpgradeSwConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('mainCodeOnly',1),('mainAndStandbyCode',2),('mainCodeWithBootSector',3),('mainAndStandbyWithBootSector',4),('noneOfTheAbove',5)))
_AdGenUpgradeSwConfiguration_Type.__name__=_E
_AdGenUpgradeSwConfiguration_Object=MibTableColumn
adGenUpgradeSwConfiguration=_AdGenUpgradeSwConfiguration_Object((1,3,6,1,4,1,664,5,13,4,2,1,1,1),_AdGenUpgradeSwConfiguration_Type())
adGenUpgradeSwConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenUpgradeSwConfiguration.setStatus(_L)
_AdGenUpgradeSwConfigDescription_Type=DisplayString
_AdGenUpgradeSwConfigDescription_Object=MibTableColumn
adGenUpgradeSwConfigDescription=_AdGenUpgradeSwConfigDescription_Object((1,3,6,1,4,1,664,5,13,4,2,1,1,2),_AdGenUpgradeSwConfigDescription_Type())
adGenUpgradeSwConfigDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenUpgradeSwConfigDescription.setStatus(_L)
_AdGenUpgradeProdMainSwVersion_Type=DisplayString
_AdGenUpgradeProdMainSwVersion_Object=MibTableColumn
adGenUpgradeProdMainSwVersion=_AdGenUpgradeProdMainSwVersion_Object((1,3,6,1,4,1,664,5,13,4,2,1,1,3),_AdGenUpgradeProdMainSwVersion_Type())
adGenUpgradeProdMainSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenUpgradeProdMainSwVersion.setStatus(_A)
_AdGenUpgradeProdStandbySwVersion_Type=DisplayString
_AdGenUpgradeProdStandbySwVersion_Object=MibTableColumn
adGenUpgradeProdStandbySwVersion=_AdGenUpgradeProdStandbySwVersion_Object((1,3,6,1,4,1,664,5,13,4,2,1,1,4),_AdGenUpgradeProdStandbySwVersion_Type())
adGenUpgradeProdStandbySwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenUpgradeProdStandbySwVersion.setStatus(_A)
_AdGenUpgradeProdMainBootSwVersion_Type=DisplayString
_AdGenUpgradeProdMainBootSwVersion_Object=MibTableColumn
adGenUpgradeProdMainBootSwVersion=_AdGenUpgradeProdMainBootSwVersion_Object((1,3,6,1,4,1,664,5,13,4,2,1,1,5),_AdGenUpgradeProdMainBootSwVersion_Type())
adGenUpgradeProdMainBootSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenUpgradeProdMainBootSwVersion.setStatus(_A)
_AdGenUpgradeProdStandbyBootSwVersion_Type=DisplayString
_AdGenUpgradeProdStandbyBootSwVersion_Object=MibTableColumn
adGenUpgradeProdStandbyBootSwVersion=_AdGenUpgradeProdStandbyBootSwVersion_Object((1,3,6,1,4,1,664,5,13,4,2,1,1,6),_AdGenUpgradeProdStandbyBootSwVersion_Type())
adGenUpgradeProdStandbyBootSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenUpgradeProdStandbyBootSwVersion.setStatus(_A)
adClrSWFailAlarm=NotificationType((1,3,6,1,4,1,664,5,13,4,0,1001340))
adClrSWFailAlarm.setObjects(*((_F,_G),(_H,_I),(_C,_D),(_J,_K)))
if mibBuilder.loadTexts:adClrSWFailAlarm.setStatus('')
adSWFailAlarm=NotificationType((1,3,6,1,4,1,664,5,13,4,0,1001341))
adSWFailAlarm.setObjects(*((_F,_G),(_H,_I),(_C,_D),(_J,_K)))
if mibBuilder.loadTexts:adSWFailAlarm.setStatus('')
adClrIncompatibleSWAlarm=NotificationType((1,3,6,1,4,1,664,5,13,4,0,1001342))
adClrIncompatibleSWAlarm.setObjects(*((_F,_G),(_H,_I),(_C,_D),(_J,_K)))
if mibBuilder.loadTexts:adClrIncompatibleSWAlarm.setStatus('')
adIncompatibleSWAlarm=NotificationType((1,3,6,1,4,1,664,5,13,4,0,1001343))
adIncompatibleSWAlarm.setObjects(*((_F,_G),(_H,_I),(_C,_D),(_J,_K)))
if mibBuilder.loadTexts:adIncompatibleSWAlarm.setStatus('')
mibBuilder.exportSymbols(_J,**{'adGenUpgrade':adGenUpgrade,'adClrSWFailAlarm':adClrSWFailAlarm,'adSWFailAlarm':adSWFailAlarm,'adClrIncompatibleSWAlarm':adClrIncompatibleSWAlarm,'adIncompatibleSWAlarm':adIncompatibleSWAlarm,'adGenUpgradeStatus':adGenUpgradeStatus,'adGenUpgradeStatusTable':adGenUpgradeStatusTable,'adGenUpgradeStatusEntry':adGenUpgradeStatusEntry,_K:adGenUpgradeFailureStatus,'adGenUpgradeSoftwareStatus':adGenUpgradeSoftwareStatus,'adGenUpgradeSoftwarePercentageStatus':adGenUpgradeSoftwarePercentageStatus,'adGenUpgradeSwUpgradeability':adGenUpgradeSwUpgradeability,'adGenUpgradeConfig':adGenUpgradeConfig,'adGenUpgradeConfigTable':adGenUpgradeConfigTable,'adGenUpgradeConfigEntry':adGenUpgradeConfigEntry,'adGenUpgradeSwConfiguration':adGenUpgradeSwConfiguration,'adGenUpgradeSwConfigDescription':adGenUpgradeSwConfigDescription,'adGenUpgradeProdMainSwVersion':adGenUpgradeProdMainSwVersion,'adGenUpgradeProdStandbySwVersion':adGenUpgradeProdStandbySwVersion,'adGenUpgradeProdMainBootSwVersion':adGenUpgradeProdMainBootSwVersion,'adGenUpgradeProdStandbyBootSwVersion':adGenUpgradeProdStandbyBootSwVersion})