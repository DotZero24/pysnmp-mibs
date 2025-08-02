_L='hpnsaHS2SlotIndex'
_K='hpnsaHS2SlotCageIndex'
_J='present'
_I='hpnsaHS2CageIndex'
_H='OctetString'
_G='read-write'
_F='attached'
_E='not-attached'
_D='HPHOTSWAP2SUBSYSTEM-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpnsaHotswap2_ObjectIdentity=ObjectIdentity
hpnsaHotswap2=_HpnsaHotswap2_ObjectIdentity((1,3,6,1,4,1,11,2,23,27))
_HpnsaHS2MibRev_ObjectIdentity=ObjectIdentity
hpnsaHS2MibRev=_HpnsaHS2MibRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,27,1))
_HpnsaHS2MibRevMajor_Type=Integer32
_HpnsaHS2MibRevMajor_Object=MibScalar
hpnsaHS2MibRevMajor=_HpnsaHS2MibRevMajor_Object((1,3,6,1,4,1,11,2,23,27,1,1),_HpnsaHS2MibRevMajor_Type())
hpnsaHS2MibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2MibRevMajor.setStatus(_A)
_HpnsaHS2MibRevMinor_Type=Integer32
_HpnsaHS2MibRevMinor_Object=MibScalar
hpnsaHS2MibRevMinor=_HpnsaHS2MibRevMinor_Object((1,3,6,1,4,1,11,2,23,27,1,2),_HpnsaHS2MibRevMinor_Type())
hpnsaHS2MibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2MibRevMinor.setStatus(_A)
_HpnsaHS2Cage_ObjectIdentity=ObjectIdentity
hpnsaHS2Cage=_HpnsaHS2Cage_ObjectIdentity((1,3,6,1,4,1,11,2,23,27,2))
_HpnsaHS2CageTable_Object=MibTable
hpnsaHS2CageTable=_HpnsaHS2CageTable_Object((1,3,6,1,4,1,11,2,23,27,2,1))
if mibBuilder.loadTexts:hpnsaHS2CageTable.setStatus(_A)
_HpnsaHS2CageEntry_Object=MibTableRow
hpnsaHS2CageEntry=_HpnsaHS2CageEntry_Object((1,3,6,1,4,1,11,2,23,27,2,1,1))
hpnsaHS2CageEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:hpnsaHS2CageEntry.setStatus(_A)
_HpnsaHS2CageIndex_Type=Integer32
_HpnsaHS2CageIndex_Object=MibTableColumn
hpnsaHS2CageIndex=_HpnsaHS2CageIndex_Object((1,3,6,1,4,1,11,2,23,27,2,1,1,1),_HpnsaHS2CageIndex_Type())
hpnsaHS2CageIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2CageIndex.setStatus(_A)
class _HpnsaHS2Cage12VPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absent',1),(_J,2)))
_HpnsaHS2Cage12VPower_Type.__name__=_C
_HpnsaHS2Cage12VPower_Object=MibTableColumn
hpnsaHS2Cage12VPower=_HpnsaHS2Cage12VPower_Object((1,3,6,1,4,1,11,2,23,27,2,1,1,2),_HpnsaHS2Cage12VPower_Type())
hpnsaHS2Cage12VPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2Cage12VPower.setStatus(_A)
class _HpnsaHS2CageTerminator1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HpnsaHS2CageTerminator1_Type.__name__=_C
_HpnsaHS2CageTerminator1_Object=MibTableColumn
hpnsaHS2CageTerminator1=_HpnsaHS2CageTerminator1_Object((1,3,6,1,4,1,11,2,23,27,2,1,1,3),_HpnsaHS2CageTerminator1_Type())
hpnsaHS2CageTerminator1.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2CageTerminator1.setStatus(_A)
class _HpnsaHS2CageTerminator2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HpnsaHS2CageTerminator2_Type.__name__=_C
_HpnsaHS2CageTerminator2_Object=MibTableColumn
hpnsaHS2CageTerminator2=_HpnsaHS2CageTerminator2_Object((1,3,6,1,4,1,11,2,23,27,2,1,1,4),_HpnsaHS2CageTerminator2_Type())
hpnsaHS2CageTerminator2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2CageTerminator2.setStatus(_A)
class _HpnsaHS2CageSCSICable1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HpnsaHS2CageSCSICable1_Type.__name__=_C
_HpnsaHS2CageSCSICable1_Object=MibTableColumn
hpnsaHS2CageSCSICable1=_HpnsaHS2CageSCSICable1_Object((1,3,6,1,4,1,11,2,23,27,2,1,1,5),_HpnsaHS2CageSCSICable1_Type())
hpnsaHS2CageSCSICable1.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2CageSCSICable1.setStatus(_A)
class _HpnsaHS2CageSCSICable2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HpnsaHS2CageSCSICable2_Type.__name__=_C
_HpnsaHS2CageSCSICable2_Object=MibTableColumn
hpnsaHS2CageSCSICable2=_HpnsaHS2CageSCSICable2_Object((1,3,6,1,4,1,11,2,23,27,2,1,1,6),_HpnsaHS2CageSCSICable2_Type())
hpnsaHS2CageSCSICable2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2CageSCSICable2.setStatus(_A)
_HpnsaHS2CageBaseSCSIAddress_Type=Integer32
_HpnsaHS2CageBaseSCSIAddress_Object=MibTableColumn
hpnsaHS2CageBaseSCSIAddress=_HpnsaHS2CageBaseSCSIAddress_Object((1,3,6,1,4,1,11,2,23,27,2,1,1,7),_HpnsaHS2CageBaseSCSIAddress_Type())
hpnsaHS2CageBaseSCSIAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnsaHS2CageBaseSCSIAddress.setStatus(_A)
_HpnsaHS2CageTemperature_Type=Integer32
_HpnsaHS2CageTemperature_Object=MibTableColumn
hpnsaHS2CageTemperature=_HpnsaHS2CageTemperature_Object((1,3,6,1,4,1,11,2,23,27,2,1,1,8),_HpnsaHS2CageTemperature_Type())
hpnsaHS2CageTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2CageTemperature.setStatus(_A)
_HpnsaHS2CageTemperatureWarningThreshold_Type=Integer32
_HpnsaHS2CageTemperatureWarningThreshold_Object=MibTableColumn
hpnsaHS2CageTemperatureWarningThreshold=_HpnsaHS2CageTemperatureWarningThreshold_Object((1,3,6,1,4,1,11,2,23,27,2,1,1,9),_HpnsaHS2CageTemperatureWarningThreshold_Type())
hpnsaHS2CageTemperatureWarningThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnsaHS2CageTemperatureWarningThreshold.setStatus(_A)
_HpnsaHS2CageTemperatureAlertThreshold_Type=Integer32
_HpnsaHS2CageTemperatureAlertThreshold_Object=MibTableColumn
hpnsaHS2CageTemperatureAlertThreshold=_HpnsaHS2CageTemperatureAlertThreshold_Object((1,3,6,1,4,1,11,2,23,27,2,1,1,10),_HpnsaHS2CageTemperatureAlertThreshold_Type())
hpnsaHS2CageTemperatureAlertThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnsaHS2CageTemperatureAlertThreshold.setStatus(_A)
class _HpnsaHS2CageManagementBoardFRU_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaHS2CageManagementBoardFRU_Type.__name__=_H
_HpnsaHS2CageManagementBoardFRU_Object=MibTableColumn
hpnsaHS2CageManagementBoardFRU=_HpnsaHS2CageManagementBoardFRU_Object((1,3,6,1,4,1,11,2,23,27,2,1,1,11),_HpnsaHS2CageManagementBoardFRU_Type())
hpnsaHS2CageManagementBoardFRU.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2CageManagementBoardFRU.setStatus(_A)
class _HpnsaHS2CageInterconnectFRU_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaHS2CageInterconnectFRU_Type.__name__=_H
_HpnsaHS2CageInterconnectFRU_Object=MibTableColumn
hpnsaHS2CageInterconnectFRU=_HpnsaHS2CageInterconnectFRU_Object((1,3,6,1,4,1,11,2,23,27,2,1,1,12),_HpnsaHS2CageInterconnectFRU_Type())
hpnsaHS2CageInterconnectFRU.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2CageInterconnectFRU.setStatus(_A)
_HpnsaHS2CageFirmwareMajorRev_Type=Integer32
_HpnsaHS2CageFirmwareMajorRev_Object=MibTableColumn
hpnsaHS2CageFirmwareMajorRev=_HpnsaHS2CageFirmwareMajorRev_Object((1,3,6,1,4,1,11,2,23,27,2,1,1,13),_HpnsaHS2CageFirmwareMajorRev_Type())
hpnsaHS2CageFirmwareMajorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2CageFirmwareMajorRev.setStatus(_A)
_HpnsaHS2CageFirmwareMinorRev_Type=Integer32
_HpnsaHS2CageFirmwareMinorRev_Object=MibTableColumn
hpnsaHS2CageFirmwareMinorRev=_HpnsaHS2CageFirmwareMinorRev_Object((1,3,6,1,4,1,11,2,23,27,2,1,1,14),_HpnsaHS2CageFirmwareMinorRev_Type())
hpnsaHS2CageFirmwareMinorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2CageFirmwareMinorRev.setStatus(_A)
_HpnsaHS2Slot_ObjectIdentity=ObjectIdentity
hpnsaHS2Slot=_HpnsaHS2Slot_ObjectIdentity((1,3,6,1,4,1,11,2,23,27,3))
_HpnsaHS2SlotTable_Object=MibTable
hpnsaHS2SlotTable=_HpnsaHS2SlotTable_Object((1,3,6,1,4,1,11,2,23,27,3,1))
if mibBuilder.loadTexts:hpnsaHS2SlotTable.setStatus(_A)
_HpnsaHS2SlotEntry_Object=MibTableRow
hpnsaHS2SlotEntry=_HpnsaHS2SlotEntry_Object((1,3,6,1,4,1,11,2,23,27,3,1,1))
hpnsaHS2SlotEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:hpnsaHS2SlotEntry.setStatus(_A)
_HpnsaHS2SlotCageIndex_Type=Integer32
_HpnsaHS2SlotCageIndex_Object=MibTableColumn
hpnsaHS2SlotCageIndex=_HpnsaHS2SlotCageIndex_Object((1,3,6,1,4,1,11,2,23,27,3,1,1,1),_HpnsaHS2SlotCageIndex_Type())
hpnsaHS2SlotCageIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2SlotCageIndex.setStatus(_A)
_HpnsaHS2SlotIndex_Type=Integer32
_HpnsaHS2SlotIndex_Object=MibTableColumn
hpnsaHS2SlotIndex=_HpnsaHS2SlotIndex_Object((1,3,6,1,4,1,11,2,23,27,3,1,1,2),_HpnsaHS2SlotIndex_Type())
hpnsaHS2SlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2SlotIndex.setStatus(_A)
class _HpnsaHS2DrivePresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('not-present',1),(_J,2)))
_HpnsaHS2DrivePresent_Type.__name__=_C
_HpnsaHS2DrivePresent_Object=MibTableColumn
hpnsaHS2DrivePresent=_HpnsaHS2DrivePresent_Object((1,3,6,1,4,1,11,2,23,27,3,1,1,3),_HpnsaHS2DrivePresent_Type())
hpnsaHS2DrivePresent.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2DrivePresent.setStatus(_A)
class _HpnsaHS2DriveSCSIBusType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('se',1),('lvd',2),('hvd',3),('none',4)))
_HpnsaHS2DriveSCSIBusType_Type.__name__=_C
_HpnsaHS2DriveSCSIBusType_Object=MibTableColumn
hpnsaHS2DriveSCSIBusType=_HpnsaHS2DriveSCSIBusType_Object((1,3,6,1,4,1,11,2,23,27,3,1,1,4),_HpnsaHS2DriveSCSIBusType_Type())
hpnsaHS2DriveSCSIBusType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHS2DriveSCSIBusType.setStatus(_A)
_HpnsaHS2DriveIdentify_Type=Integer32
_HpnsaHS2DriveIdentify_Object=MibTableColumn
hpnsaHS2DriveIdentify=_HpnsaHS2DriveIdentify_Object((1,3,6,1,4,1,11,2,23,27,3,1,1,5),_HpnsaHS2DriveIdentify_Type())
hpnsaHS2DriveIdentify.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnsaHS2DriveIdentify.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaHotswap2':hpnsaHotswap2,'hpnsaHS2MibRev':hpnsaHS2MibRev,'hpnsaHS2MibRevMajor':hpnsaHS2MibRevMajor,'hpnsaHS2MibRevMinor':hpnsaHS2MibRevMinor,'hpnsaHS2Cage':hpnsaHS2Cage,'hpnsaHS2CageTable':hpnsaHS2CageTable,'hpnsaHS2CageEntry':hpnsaHS2CageEntry,_I:hpnsaHS2CageIndex,'hpnsaHS2Cage12VPower':hpnsaHS2Cage12VPower,'hpnsaHS2CageTerminator1':hpnsaHS2CageTerminator1,'hpnsaHS2CageTerminator2':hpnsaHS2CageTerminator2,'hpnsaHS2CageSCSICable1':hpnsaHS2CageSCSICable1,'hpnsaHS2CageSCSICable2':hpnsaHS2CageSCSICable2,'hpnsaHS2CageBaseSCSIAddress':hpnsaHS2CageBaseSCSIAddress,'hpnsaHS2CageTemperature':hpnsaHS2CageTemperature,'hpnsaHS2CageTemperatureWarningThreshold':hpnsaHS2CageTemperatureWarningThreshold,'hpnsaHS2CageTemperatureAlertThreshold':hpnsaHS2CageTemperatureAlertThreshold,'hpnsaHS2CageManagementBoardFRU':hpnsaHS2CageManagementBoardFRU,'hpnsaHS2CageInterconnectFRU':hpnsaHS2CageInterconnectFRU,'hpnsaHS2CageFirmwareMajorRev':hpnsaHS2CageFirmwareMajorRev,'hpnsaHS2CageFirmwareMinorRev':hpnsaHS2CageFirmwareMinorRev,'hpnsaHS2Slot':hpnsaHS2Slot,'hpnsaHS2SlotTable':hpnsaHS2SlotTable,'hpnsaHS2SlotEntry':hpnsaHS2SlotEntry,_K:hpnsaHS2SlotCageIndex,_L:hpnsaHS2SlotIndex,'hpnsaHS2DrivePresent':hpnsaHS2DrivePresent,'hpnsaHS2DriveSCSIBusType':hpnsaHS2DriveSCSIBusType,'hpnsaHS2DriveIdentify':hpnsaHS2DriveIdentify})