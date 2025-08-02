_H='infoDriveCardIndex'
_G='infoSFDSIndex'
_F='infoPowerSupplyIndex'
_E='Celsius'
_D='Integer32'
_C='LEFTHAND-NETWORKS-NUS-COMMON-INFO-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lhnModules,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-GLOBAL-REG','lhnModules')
lhnNusCommonInfo,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-NUS-COMMON-MIB','lhnNusCommonInfo')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
lhnNusCommonInfoModule=ModuleIdentity((1,3,6,1,4,1,9804,1,1,4))
_InfoSerialNumber_Type=OctetString
_InfoSerialNumber_Object=MibScalar
infoSerialNumber=_InfoSerialNumber_Object((1,3,6,1,4,1,9804,3,1,1,2,1,1),_InfoSerialNumber_Type())
infoSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:infoSerialNumber.setStatus(_A)
_InfoModel_Type=OctetString
_InfoModel_Object=MibScalar
infoModel=_InfoModel_Object((1,3,6,1,4,1,9804,3,1,1,2,1,2),_InfoModel_Type())
infoModel.setMaxAccess(_B)
if mibBuilder.loadTexts:infoModel.setStatus(_A)
_InfoSoftwareVersion_Type=OctetString
_InfoSoftwareVersion_Object=MibScalar
infoSoftwareVersion=_InfoSoftwareVersion_Object((1,3,6,1,4,1,9804,3,1,1,2,1,3),_InfoSoftwareVersion_Type())
infoSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:infoSoftwareVersion.setStatus(_A)
_InfoDSPFirmwareVersion_Type=OctetString
_InfoDSPFirmwareVersion_Object=MibScalar
infoDSPFirmwareVersion=_InfoDSPFirmwareVersion_Object((1,3,6,1,4,1,9804,3,1,1,2,1,4),_InfoDSPFirmwareVersion_Type())
infoDSPFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:infoDSPFirmwareVersion.setStatus(_A)
_InfoMotherboardTemperature_Type=Integer32
_InfoMotherboardTemperature_Object=MibScalar
infoMotherboardTemperature=_InfoMotherboardTemperature_Object((1,3,6,1,4,1,9804,3,1,1,2,1,5),_InfoMotherboardTemperature_Type())
infoMotherboardTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:infoMotherboardTemperature.setStatus(_A)
if mibBuilder.loadTexts:infoMotherboardTemperature.setUnits(_E)
_InfoCPUTemperature_Type=Integer32
_InfoCPUTemperature_Object=MibScalar
infoCPUTemperature=_InfoCPUTemperature_Object((1,3,6,1,4,1,9804,3,1,1,2,1,6),_InfoCPUTemperature_Type())
infoCPUTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:infoCPUTemperature.setStatus(_A)
if mibBuilder.loadTexts:infoCPUTemperature.setUnits(_E)
_InfoCPUFanSpeed_Type=Integer32
_InfoCPUFanSpeed_Object=MibScalar
infoCPUFanSpeed=_InfoCPUFanSpeed_Object((1,3,6,1,4,1,9804,3,1,1,2,1,7),_InfoCPUFanSpeed_Type())
infoCPUFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:infoCPUFanSpeed.setStatus(_A)
if mibBuilder.loadTexts:infoCPUFanSpeed.setUnits('RPM')
_InfoPowerSupplyCount_Type=Integer32
_InfoPowerSupplyCount_Object=MibScalar
infoPowerSupplyCount=_InfoPowerSupplyCount_Object((1,3,6,1,4,1,9804,3,1,1,2,1,8),_InfoPowerSupplyCount_Type())
infoPowerSupplyCount.setMaxAccess(_B)
if mibBuilder.loadTexts:infoPowerSupplyCount.setStatus(_A)
_InfoPowerSupplyTable_Object=MibTable
infoPowerSupplyTable=_InfoPowerSupplyTable_Object((1,3,6,1,4,1,9804,3,1,1,2,1,9))
if mibBuilder.loadTexts:infoPowerSupplyTable.setStatus(_A)
_InfoPowerSupplyEntry_Object=MibTableRow
infoPowerSupplyEntry=_InfoPowerSupplyEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,1,9,1))
infoPowerSupplyEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:infoPowerSupplyEntry.setStatus(_A)
_InfoPowerSupplyIndex_Type=Integer32
_InfoPowerSupplyIndex_Object=MibTableColumn
infoPowerSupplyIndex=_InfoPowerSupplyIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,1,9,1,1),_InfoPowerSupplyIndex_Type())
infoPowerSupplyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:infoPowerSupplyIndex.setStatus(_A)
class _InfoPowerSupplyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('inactive',2),('marginal',3)))
_InfoPowerSupplyStatus_Type.__name__=_D
_InfoPowerSupplyStatus_Object=MibTableColumn
infoPowerSupplyStatus=_InfoPowerSupplyStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,1,9,1,2),_InfoPowerSupplyStatus_Type())
infoPowerSupplyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:infoPowerSupplyStatus.setStatus(_A)
_InfoSFDSCount_Type=Integer32
_InfoSFDSCount_Object=MibScalar
infoSFDSCount=_InfoSFDSCount_Object((1,3,6,1,4,1,9804,3,1,1,2,1,10),_InfoSFDSCount_Type())
infoSFDSCount.setMaxAccess(_B)
if mibBuilder.loadTexts:infoSFDSCount.setStatus(_A)
_InfoSFDSTable_Object=MibTable
infoSFDSTable=_InfoSFDSTable_Object((1,3,6,1,4,1,9804,3,1,1,2,1,11))
if mibBuilder.loadTexts:infoSFDSTable.setStatus(_A)
_InfoSFDSEntry_Object=MibTableRow
infoSFDSEntry=_InfoSFDSEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,1,11,1))
infoSFDSEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:infoSFDSEntry.setStatus(_A)
_InfoSFDSIndex_Type=Integer32
_InfoSFDSIndex_Object=MibTableColumn
infoSFDSIndex=_InfoSFDSIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,1,11,1,1),_InfoSFDSIndex_Type())
infoSFDSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:infoSFDSIndex.setStatus(_A)
_InfoSFDSHardwareVersion_Type=OctetString
_InfoSFDSHardwareVersion_Object=MibTableColumn
infoSFDSHardwareVersion=_InfoSFDSHardwareVersion_Object((1,3,6,1,4,1,9804,3,1,1,2,1,11,1,2),_InfoSFDSHardwareVersion_Type())
infoSFDSHardwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:infoSFDSHardwareVersion.setStatus(_A)
_InfoSFDSFirmwareVersion_Type=OctetString
_InfoSFDSFirmwareVersion_Object=MibTableColumn
infoSFDSFirmwareVersion=_InfoSFDSFirmwareVersion_Object((1,3,6,1,4,1,9804,3,1,1,2,1,11,1,3),_InfoSFDSFirmwareVersion_Type())
infoSFDSFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:infoSFDSFirmwareVersion.setStatus(_A)
_InfoSFDSDriverVersion_Type=OctetString
_InfoSFDSDriverVersion_Object=MibTableColumn
infoSFDSDriverVersion=_InfoSFDSDriverVersion_Object((1,3,6,1,4,1,9804,3,1,1,2,1,11,1,4),_InfoSFDSDriverVersion_Type())
infoSFDSDriverVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:infoSFDSDriverVersion.setStatus(_A)
_InfoSFDSMemorySize_Type=Counter32
_InfoSFDSMemorySize_Object=MibTableColumn
infoSFDSMemorySize=_InfoSFDSMemorySize_Object((1,3,6,1,4,1,9804,3,1,1,2,1,11,1,5),_InfoSFDSMemorySize_Type())
infoSFDSMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:infoSFDSMemorySize.setStatus(_A)
if mibBuilder.loadTexts:infoSFDSMemorySize.setUnits('KBytes')
_InfoSFDSStatus_Type=OctetString
_InfoSFDSStatus_Object=MibTableColumn
infoSFDSStatus=_InfoSFDSStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,1,11,1,6),_InfoSFDSStatus_Type())
infoSFDSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:infoSFDSStatus.setStatus(_A)
_InfoDriveCardCount_Type=Integer32
_InfoDriveCardCount_Object=MibScalar
infoDriveCardCount=_InfoDriveCardCount_Object((1,3,6,1,4,1,9804,3,1,1,2,1,12),_InfoDriveCardCount_Type())
infoDriveCardCount.setMaxAccess(_B)
if mibBuilder.loadTexts:infoDriveCardCount.setStatus(_A)
_InfoDriveCardTable_Object=MibTable
infoDriveCardTable=_InfoDriveCardTable_Object((1,3,6,1,4,1,9804,3,1,1,2,1,13))
if mibBuilder.loadTexts:infoDriveCardTable.setStatus(_A)
_InfoDriveCardEntry_Object=MibTableRow
infoDriveCardEntry=_InfoDriveCardEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,1,13,1))
infoDriveCardEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:infoDriveCardEntry.setStatus(_A)
_InfoDriveCardIndex_Type=Integer32
_InfoDriveCardIndex_Object=MibTableColumn
infoDriveCardIndex=_InfoDriveCardIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,1,13,1,1),_InfoDriveCardIndex_Type())
infoDriveCardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:infoDriveCardIndex.setStatus(_A)
_InfoDriveCardModel_Type=OctetString
_InfoDriveCardModel_Object=MibTableColumn
infoDriveCardModel=_InfoDriveCardModel_Object((1,3,6,1,4,1,9804,3,1,1,2,1,13,1,2),_InfoDriveCardModel_Type())
infoDriveCardModel.setMaxAccess(_B)
if mibBuilder.loadTexts:infoDriveCardModel.setStatus(_A)
_InfoDriveCardBiosVersion_Type=OctetString
_InfoDriveCardBiosVersion_Object=MibTableColumn
infoDriveCardBiosVersion=_InfoDriveCardBiosVersion_Object((1,3,6,1,4,1,9804,3,1,1,2,1,13,1,3),_InfoDriveCardBiosVersion_Type())
infoDriveCardBiosVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:infoDriveCardBiosVersion.setStatus(_A)
_InfoDriveCardFirmwareVersion_Type=OctetString
_InfoDriveCardFirmwareVersion_Object=MibTableColumn
infoDriveCardFirmwareVersion=_InfoDriveCardFirmwareVersion_Object((1,3,6,1,4,1,9804,3,1,1,2,1,13,1,4),_InfoDriveCardFirmwareVersion_Type())
infoDriveCardFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:infoDriveCardFirmwareVersion.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'lhnNusCommonInfoModule':lhnNusCommonInfoModule,'infoSerialNumber':infoSerialNumber,'infoModel':infoModel,'infoSoftwareVersion':infoSoftwareVersion,'infoDSPFirmwareVersion':infoDSPFirmwareVersion,'infoMotherboardTemperature':infoMotherboardTemperature,'infoCPUTemperature':infoCPUTemperature,'infoCPUFanSpeed':infoCPUFanSpeed,'infoPowerSupplyCount':infoPowerSupplyCount,'infoPowerSupplyTable':infoPowerSupplyTable,'infoPowerSupplyEntry':infoPowerSupplyEntry,_F:infoPowerSupplyIndex,'infoPowerSupplyStatus':infoPowerSupplyStatus,'infoSFDSCount':infoSFDSCount,'infoSFDSTable':infoSFDSTable,'infoSFDSEntry':infoSFDSEntry,_G:infoSFDSIndex,'infoSFDSHardwareVersion':infoSFDSHardwareVersion,'infoSFDSFirmwareVersion':infoSFDSFirmwareVersion,'infoSFDSDriverVersion':infoSFDSDriverVersion,'infoSFDSMemorySize':infoSFDSMemorySize,'infoSFDSStatus':infoSFDSStatus,'infoDriveCardCount':infoDriveCardCount,'infoDriveCardTable':infoDriveCardTable,'infoDriveCardEntry':infoDriveCardEntry,_H:infoDriveCardIndex,'infoDriveCardModel':infoDriveCardModel,'infoDriveCardBiosVersion':infoDriveCardBiosVersion,'infoDriveCardFirmwareVersion':infoDriveCardFirmwareVersion})