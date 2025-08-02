_Z='copper'
_Y='eqlSFPIndex'
_X='eqlChannelCardIndex'
_W='eqlDaughterCardIndex'
_V='eqlEMMIndex'
_U='eqlBackplaneIndex'
_T='seconds'
_S='unknown sw rev'
_R='eqlControllerIndex'
_Q='good'
_P='failed'
_O='unknown model'
_N='not-present'
_M='OctetString'
_L='not-accessible'
_K='EQLCONTROLLER-MIB'
_J='eqlMemberIndex'
_I='EQLMEMBER-MIB'
_H='eqlGroupId'
_G='EQLGROUP-MIB'
_F='Unsigned32'
_E='Integer32'
_D='unknown'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eqlGroupId,=mibBuilder.importSymbols(_G,_H)
eqlMemberIndex,=mibBuilder.importSymbols(_I,_J)
equalLogic,=mibBuilder.importSymbols('EQUALLOGIC-SMI','equalLogic')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
eqlcontrollerModule=ModuleIdentity((1,3,6,1,4,1,12740,4))
if mibBuilder.loadTexts:eqlcontrollerModule.setRevisions(('2002-09-06 00:00',))
_EqlcontrollerObjects_ObjectIdentity=ObjectIdentity
eqlcontrollerObjects=_EqlcontrollerObjects_ObjectIdentity((1,3,6,1,4,1,12740,4,1))
_EqlControllerTable_Object=MibTable
eqlControllerTable=_EqlControllerTable_Object((1,3,6,1,4,1,12740,4,1,1))
if mibBuilder.loadTexts:eqlControllerTable.setStatus(_A)
_EqlControllerEntry_Object=MibTableRow
eqlControllerEntry=_EqlControllerEntry_Object((1,3,6,1,4,1,12740,4,1,1,1))
eqlControllerEntry.setIndexNames((0,_G,_H),(0,_I,_J),(0,_K,_R))
if mibBuilder.loadTexts:eqlControllerEntry.setStatus(_A)
class _EqlControllerIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_EqlControllerIndex_Type.__name__=_E
_EqlControllerIndex_Object=MibTableColumn
eqlControllerIndex=_EqlControllerIndex_Object((1,3,6,1,4,1,12740,4,1,1,1,1),_EqlControllerIndex_Type())
eqlControllerIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:eqlControllerIndex.setStatus(_A)
class _EqlControllerModel_Type(DisplayString):defaultValue=OctetString(_O);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EqlControllerModel_Type.__name__=_C
_EqlControllerModel_Object=MibTableColumn
eqlControllerModel=_EqlControllerModel_Object((1,3,6,1,4,1,12740,4,1,1,1,2),_EqlControllerModel_Type())
eqlControllerModel.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerModel.setStatus(_A)
class _EqlControllerCMRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_EqlControllerCMRevision_Type.__name__=_C
_EqlControllerCMRevision_Object=MibTableColumn
eqlControllerCMRevision=_EqlControllerCMRevision_Object((1,3,6,1,4,1,12740,4,1,1,1,3),_EqlControllerCMRevision_Type())
eqlControllerCMRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerCMRevision.setStatus(_A)
class _EqlControllerSwRevision_Type(DisplayString):defaultValue=OctetString(_S);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,96))
_EqlControllerSwRevision_Type.__name__=_C
_EqlControllerSwRevision_Object=MibTableColumn
eqlControllerSwRevision=_EqlControllerSwRevision_Object((1,3,6,1,4,1,12740,4,1,1,1,4),_EqlControllerSwRevision_Type())
eqlControllerSwRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerSwRevision.setStatus(_A)
class _EqlControllerBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ok',1),(_P,2),('good-battery-is-charging',3),('low-voltage-status',4),('low-voltage-is-charging',5),('missing-battery',6)))
_EqlControllerBatteryStatus_Type.__name__=_E
_EqlControllerBatteryStatus_Object=MibTableColumn
eqlControllerBatteryStatus=_EqlControllerBatteryStatus_Object((1,3,6,1,4,1,12740,4,1,1,1,5),_EqlControllerBatteryStatus_Type())
eqlControllerBatteryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerBatteryStatus.setStatus(_A)
_EqlControllerUpTime_Type=Counter32
_EqlControllerUpTime_Object=MibTableColumn
eqlControllerUpTime=_EqlControllerUpTime_Object((1,3,6,1,4,1,12740,4,1,1,1,6),_EqlControllerUpTime_Type())
eqlControllerUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerUpTime.setStatus(_A)
if mibBuilder.loadTexts:eqlControllerUpTime.setUnits(_T)
_EqlControllerProcessorTemp_Type=Integer32
_EqlControllerProcessorTemp_Object=MibTableColumn
eqlControllerProcessorTemp=_EqlControllerProcessorTemp_Object((1,3,6,1,4,1,12740,4,1,1,1,7),_EqlControllerProcessorTemp_Type())
eqlControllerProcessorTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerProcessorTemp.setStatus(_A)
_EqlControllerChipsetTemp_Type=Integer32
_EqlControllerChipsetTemp_Object=MibTableColumn
eqlControllerChipsetTemp=_EqlControllerChipsetTemp_Object((1,3,6,1,4,1,12740,4,1,1,1,8),_EqlControllerChipsetTemp_Type())
eqlControllerChipsetTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerChipsetTemp.setStatus(_A)
class _EqlControllerPrimaryOrSecondary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_EqlControllerPrimaryOrSecondary_Type.__name__=_E
_EqlControllerPrimaryOrSecondary_Object=MibTableColumn
eqlControllerPrimaryOrSecondary=_EqlControllerPrimaryOrSecondary_Object((1,3,6,1,4,1,12740,4,1,1,1,9),_EqlControllerPrimaryOrSecondary_Type())
eqlControllerPrimaryOrSecondary.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerPrimaryOrSecondary.setStatus(_A)
class _EqlControllerPrimaryFlashImageRev_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_EqlControllerPrimaryFlashImageRev_Type.__name__=_C
_EqlControllerPrimaryFlashImageRev_Object=MibTableColumn
eqlControllerPrimaryFlashImageRev=_EqlControllerPrimaryFlashImageRev_Object((1,3,6,1,4,1,12740,4,1,1,1,10),_EqlControllerPrimaryFlashImageRev_Type())
eqlControllerPrimaryFlashImageRev.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerPrimaryFlashImageRev.setStatus(_A)
class _EqlControllerSecondaryFlashImageRev_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_EqlControllerSecondaryFlashImageRev_Type.__name__=_C
_EqlControllerSecondaryFlashImageRev_Object=MibTableColumn
eqlControllerSecondaryFlashImageRev=_EqlControllerSecondaryFlashImageRev_Object((1,3,6,1,4,1,12740,4,1,1,1,11),_EqlControllerSecondaryFlashImageRev_Type())
eqlControllerSecondaryFlashImageRev.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerSecondaryFlashImageRev.setStatus(_A)
class _EqlControllerSerialNumber_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlControllerSerialNumber_Type.__name__=_C
_EqlControllerSerialNumber_Object=MibTableColumn
eqlControllerSerialNumber=_EqlControllerSerialNumber_Object((1,3,6,1,4,1,12740,4,1,1,1,12),_EqlControllerSerialNumber_Type())
eqlControllerSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerSerialNumber.setStatus(_A)
class _EqlControllerDate_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlControllerDate_Type.__name__=_C
_EqlControllerDate_Object=MibTableColumn
eqlControllerDate=_EqlControllerDate_Object((1,3,6,1,4,1,12740,4,1,1,1,13),_EqlControllerDate_Type())
eqlControllerDate.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerDate.setStatus(_A)
class _EqlControllerECO_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlControllerECO_Type.__name__=_C
_EqlControllerECO_Object=MibTableColumn
eqlControllerECO=_EqlControllerECO_Object((1,3,6,1,4,1,12740,4,1,1,1,14),_EqlControllerECO_Type())
eqlControllerECO.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerECO.setStatus(_A)
class _EqlControllerEEprom_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_EqlControllerEEprom_Type.__name__=_M
_EqlControllerEEprom_Object=MibTableColumn
eqlControllerEEprom=_EqlControllerEEprom_Object((1,3,6,1,4,1,12740,4,1,1,1,15),_EqlControllerEEprom_Type())
eqlControllerEEprom.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerEEprom.setStatus(_A)
class _EqlControllerPLDrev_Type(Unsigned32):defaultValue=0
_EqlControllerPLDrev_Type.__name__=_F
_EqlControllerPLDrev_Object=MibTableColumn
eqlControllerPLDrev=_EqlControllerPLDrev_Object((1,3,6,1,4,1,12740,4,1,1,1,16),_EqlControllerPLDrev_Type())
eqlControllerPLDrev.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerPLDrev.setStatus(_A)
class _EqlControllerPlatformType_Type(Unsigned32):defaultValue=0
_EqlControllerPlatformType_Type.__name__=_F
_EqlControllerPlatformType_Object=MibTableColumn
eqlControllerPlatformType=_EqlControllerPlatformType_Object((1,3,6,1,4,1,12740,4,1,1,1,17),_EqlControllerPlatformType_Type())
eqlControllerPlatformType.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerPlatformType.setStatus(_A)
class _EqlControllerPlatformVersion_Type(Unsigned32):defaultValue=0
_EqlControllerPlatformVersion_Type.__name__=_F
_EqlControllerPlatformVersion_Object=MibTableColumn
eqlControllerPlatformVersion=_EqlControllerPlatformVersion_Object((1,3,6,1,4,1,12740,4,1,1,1,18),_EqlControllerPlatformVersion_Type())
eqlControllerPlatformVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerPlatformVersion.setStatus(_A)
class _EqlControllerCPUPass_Type(Unsigned32):defaultValue=0
_EqlControllerCPUPass_Type.__name__=_F
_EqlControllerCPUPass_Object=MibTableColumn
eqlControllerCPUPass=_EqlControllerCPUPass_Object((1,3,6,1,4,1,12740,4,1,1,1,19),_EqlControllerCPUPass_Type())
eqlControllerCPUPass.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerCPUPass.setStatus(_A)
class _EqlControllerCPUrev_Type(Unsigned32):defaultValue=0
_EqlControllerCPUrev_Type.__name__=_F
_EqlControllerCPUrev_Object=MibTableColumn
eqlControllerCPUrev=_EqlControllerCPUrev_Object((1,3,6,1,4,1,12740,4,1,1,1,20),_EqlControllerCPUrev_Type())
eqlControllerCPUrev.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerCPUrev.setStatus(_A)
class _EqlControllerCPUfreq_Type(Unsigned32):defaultValue=0
_EqlControllerCPUfreq_Type.__name__=_F
_EqlControllerCPUfreq_Object=MibTableColumn
eqlControllerCPUfreq=_EqlControllerCPUfreq_Object((1,3,6,1,4,1,12740,4,1,1,1,21),_EqlControllerCPUfreq_Type())
eqlControllerCPUfreq.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerCPUfreq.setStatus(_A)
class _EqlControllerPhysRam_Type(Unsigned32):defaultValue=0
_EqlControllerPhysRam_Type.__name__=_F
_EqlControllerPhysRam_Object=MibTableColumn
eqlControllerPhysRam=_EqlControllerPhysRam_Object((1,3,6,1,4,1,12740,4,1,1,1,22),_EqlControllerPhysRam_Type())
eqlControllerPhysRam.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerPhysRam.setStatus(_A)
class _EqlControllerBootRomVersion_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_EqlControllerBootRomVersion_Type.__name__=_C
_EqlControllerBootRomVersion_Object=MibTableColumn
eqlControllerBootRomVersion=_EqlControllerBootRomVersion_Object((1,3,6,1,4,1,12740,4,1,1,1,23),_EqlControllerBootRomVersion_Type())
eqlControllerBootRomVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerBootRomVersion.setStatus(_A)
class _EqlControllerBootRomBuildDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_EqlControllerBootRomBuildDate_Type.__name__=_C
_EqlControllerBootRomBuildDate_Object=MibTableColumn
eqlControllerBootRomBuildDate=_EqlControllerBootRomBuildDate_Object((1,3,6,1,4,1,12740,4,1,1,1,24),_EqlControllerBootRomBuildDate_Type())
eqlControllerBootRomBuildDate.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerBootRomBuildDate.setStatus(_A)
class _EqlControllerInfoMsg_Type(DisplayString):defaultValue=OctetString(_D)
_EqlControllerInfoMsg_Type.__name__=_C
_EqlControllerInfoMsg_Object=MibTableColumn
eqlControllerInfoMsg=_EqlControllerInfoMsg_Object((1,3,6,1,4,1,12740,4,1,1,1,25),_EqlControllerInfoMsg_Type())
eqlControllerInfoMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerInfoMsg.setStatus(_A)
class _EqlControllerAthenaSataVersion_Type(DisplayString):defaultValue=OctetString(_D)
_EqlControllerAthenaSataVersion_Type.__name__=_C
_EqlControllerAthenaSataVersion_Object=MibTableColumn
eqlControllerAthenaSataVersion=_EqlControllerAthenaSataVersion_Object((1,3,6,1,4,1,12740,4,1,1,1,26),_EqlControllerAthenaSataVersion_Type())
eqlControllerAthenaSataVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerAthenaSataVersion.setStatus(_A)
class _EqlControllerMajorVersion_Type(Unsigned32):defaultValue=1
_EqlControllerMajorVersion_Type.__name__=_F
_EqlControllerMajorVersion_Object=MibTableColumn
eqlControllerMajorVersion=_EqlControllerMajorVersion_Object((1,3,6,1,4,1,12740,4,1,1,1,27),_EqlControllerMajorVersion_Type())
eqlControllerMajorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerMajorVersion.setStatus(_A)
class _EqlControllerMinorVersion_Type(Unsigned32):defaultValue=1
_EqlControllerMinorVersion_Type.__name__=_F
_EqlControllerMinorVersion_Object=MibTableColumn
eqlControllerMinorVersion=_EqlControllerMinorVersion_Object((1,3,6,1,4,1,12740,4,1,1,1,28),_EqlControllerMinorVersion_Type())
eqlControllerMinorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerMinorVersion.setStatus(_A)
class _EqlControllerMaintenanceVersion_Type(Unsigned32):defaultValue=0
_EqlControllerMaintenanceVersion_Type.__name__=_F
_EqlControllerMaintenanceVersion_Object=MibTableColumn
eqlControllerMaintenanceVersion=_EqlControllerMaintenanceVersion_Object((1,3,6,1,4,1,12740,4,1,1,1,29),_EqlControllerMaintenanceVersion_Type())
eqlControllerMaintenanceVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerMaintenanceVersion.setStatus(_A)
_EqlControllerSWCompatibilityLevel_Type=Unsigned32
_EqlControllerSWCompatibilityLevel_Object=MibTableColumn
eqlControllerSWCompatibilityLevel=_EqlControllerSWCompatibilityLevel_Object((1,3,6,1,4,1,12740,4,1,1,1,30),_EqlControllerSWCompatibilityLevel_Type())
eqlControllerSWCompatibilityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerSWCompatibilityLevel.setStatus(_A)
class _EqlControllerFullSwRevision_Type(DisplayString):defaultValue=OctetString(_S);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,96))
_EqlControllerFullSwRevision_Type.__name__=_C
_EqlControllerFullSwRevision_Object=MibTableColumn
eqlControllerFullSwRevision=_EqlControllerFullSwRevision_Object((1,3,6,1,4,1,12740,4,1,1,1,31),_EqlControllerFullSwRevision_Type())
eqlControllerFullSwRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerFullSwRevision.setStatus(_A)
class _EqlControllerNVRAMBattery_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_N,0),(_Q,1),('bad',2),(_D,3)))
_EqlControllerNVRAMBattery_Type.__name__=_E
_EqlControllerNVRAMBattery_Object=MibTableColumn
eqlControllerNVRAMBattery=_EqlControllerNVRAMBattery_Object((1,3,6,1,4,1,12740,4,1,1,1,32),_EqlControllerNVRAMBattery_Type())
eqlControllerNVRAMBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerNVRAMBattery.setStatus(_A)
class _EqlControllerSerialNumber2_Type(DisplayString):defaultValue=OctetString(_D)
_EqlControllerSerialNumber2_Type.__name__=_C
_EqlControllerSerialNumber2_Object=MibTableColumn
eqlControllerSerialNumber2=_EqlControllerSerialNumber2_Object((1,3,6,1,4,1,12740,4,1,1,1,33),_EqlControllerSerialNumber2_Type())
eqlControllerSerialNumber2.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerSerialNumber2.setStatus(_A)
class _EqlControllerType_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EqlControllerType_Type.__name__=_C
_EqlControllerType_Object=MibTableColumn
eqlControllerType=_EqlControllerType_Object((1,3,6,1,4,1,12740,4,1,1,1,34),_EqlControllerType_Type())
eqlControllerType.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerType.setStatus(_A)
_EqlControllerBootTime_Type=Counter32
_EqlControllerBootTime_Object=MibTableColumn
eqlControllerBootTime=_EqlControllerBootTime_Object((1,3,6,1,4,1,12740,4,1,1,1,35),_EqlControllerBootTime_Type())
eqlControllerBootTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlControllerBootTime.setStatus(_A)
if mibBuilder.loadTexts:eqlControllerBootTime.setUnits(_T)
_EqlcontrollerNotifications_ObjectIdentity=ObjectIdentity
eqlcontrollerNotifications=_EqlcontrollerNotifications_ObjectIdentity((1,3,6,1,4,1,12740,4,2))
_EqlcontrollerConformance_ObjectIdentity=ObjectIdentity
eqlcontrollerConformance=_EqlcontrollerConformance_ObjectIdentity((1,3,6,1,4,1,12740,4,3))
_EqlbackplaneObjects_ObjectIdentity=ObjectIdentity
eqlbackplaneObjects=_EqlbackplaneObjects_ObjectIdentity((1,3,6,1,4,1,12740,4,4))
_EqlBackplaneTable_Object=MibTable
eqlBackplaneTable=_EqlBackplaneTable_Object((1,3,6,1,4,1,12740,4,4,1))
if mibBuilder.loadTexts:eqlBackplaneTable.setStatus(_A)
_EqlBackplaneEntry_Object=MibTableRow
eqlBackplaneEntry=_EqlBackplaneEntry_Object((1,3,6,1,4,1,12740,4,4,1,1))
eqlBackplaneEntry.setIndexNames((0,_G,_H),(0,_I,_J),(0,_K,_U))
if mibBuilder.loadTexts:eqlBackplaneEntry.setStatus(_A)
class _EqlBackplaneIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_EqlBackplaneIndex_Type.__name__=_E
_EqlBackplaneIndex_Object=MibTableColumn
eqlBackplaneIndex=_EqlBackplaneIndex_Object((1,3,6,1,4,1,12740,4,4,1,1,1),_EqlBackplaneIndex_Type())
eqlBackplaneIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:eqlBackplaneIndex.setStatus(_A)
class _EqlBackplanePartNum_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlBackplanePartNum_Type.__name__=_C
_EqlBackplanePartNum_Object=MibTableColumn
eqlBackplanePartNum=_EqlBackplanePartNum_Object((1,3,6,1,4,1,12740,4,4,1,1,2),_EqlBackplanePartNum_Type())
eqlBackplanePartNum.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlBackplanePartNum.setStatus(_A)
class _EqlBackplaneRev_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlBackplaneRev_Type.__name__=_C
_EqlBackplaneRev_Object=MibTableColumn
eqlBackplaneRev=_EqlBackplaneRev_Object((1,3,6,1,4,1,12740,4,4,1,1,3),_EqlBackplaneRev_Type())
eqlBackplaneRev.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlBackplaneRev.setStatus(_A)
class _EqlBackplaneDate_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlBackplaneDate_Type.__name__=_C
_EqlBackplaneDate_Object=MibTableColumn
eqlBackplaneDate=_EqlBackplaneDate_Object((1,3,6,1,4,1,12740,4,4,1,1,4),_EqlBackplaneDate_Type())
eqlBackplaneDate.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlBackplaneDate.setStatus(_A)
class _EqlBackplaneSN_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlBackplaneSN_Type.__name__=_C
_EqlBackplaneSN_Object=MibTableColumn
eqlBackplaneSN=_EqlBackplaneSN_Object((1,3,6,1,4,1,12740,4,4,1,1,5),_EqlBackplaneSN_Type())
eqlBackplaneSN.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlBackplaneSN.setStatus(_A)
class _EqlBackplaneECO_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlBackplaneECO_Type.__name__=_C
_EqlBackplaneECO_Object=MibTableColumn
eqlBackplaneECO=_EqlBackplaneECO_Object((1,3,6,1,4,1,12740,4,4,1,1,6),_EqlBackplaneECO_Type())
eqlBackplaneECO.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlBackplaneECO.setStatus(_A)
class _EqlBackplaneEEprom_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_EqlBackplaneEEprom_Type.__name__=_M
_EqlBackplaneEEprom_Object=MibTableColumn
eqlBackplaneEEprom=_EqlBackplaneEEprom_Object((1,3,6,1,4,1,12740,4,4,1,1,7),_EqlBackplaneEEprom_Type())
eqlBackplaneEEprom.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlBackplaneEEprom.setStatus(_A)
class _EqlBackplaneSN2_Type(DisplayString):defaultValue=OctetString(_D)
_EqlBackplaneSN2_Type.__name__=_C
_EqlBackplaneSN2_Object=MibTableColumn
eqlBackplaneSN2=_EqlBackplaneSN2_Object((1,3,6,1,4,1,12740,4,4,1,1,8),_EqlBackplaneSN2_Type())
eqlBackplaneSN2.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlBackplaneSN2.setStatus(_A)
class _EqlBackplaneType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EqlBackplaneType_Type.__name__=_C
_EqlBackplaneType_Object=MibTableColumn
eqlBackplaneType=_EqlBackplaneType_Object((1,3,6,1,4,1,12740,4,4,1,1,9),_EqlBackplaneType_Type())
eqlBackplaneType.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlBackplaneType.setStatus(_A)
_EqlBackplaneTypeId_Type=Integer32
_EqlBackplaneTypeId_Object=MibTableColumn
eqlBackplaneTypeId=_EqlBackplaneTypeId_Object((1,3,6,1,4,1,12740,4,4,1,1,10),_EqlBackplaneTypeId_Type())
eqlBackplaneTypeId.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlBackplaneTypeId.setStatus(_A)
_EqlbackplaneNotifications_ObjectIdentity=ObjectIdentity
eqlbackplaneNotifications=_EqlbackplaneNotifications_ObjectIdentity((1,3,6,1,4,1,12740,4,5))
_EqlbackplaneConformance_ObjectIdentity=ObjectIdentity
eqlbackplaneConformance=_EqlbackplaneConformance_ObjectIdentity((1,3,6,1,4,1,12740,4,6))
_EqlemmObjects_ObjectIdentity=ObjectIdentity
eqlemmObjects=_EqlemmObjects_ObjectIdentity((1,3,6,1,4,1,12740,4,7))
_EqlEMMTable_Object=MibTable
eqlEMMTable=_EqlEMMTable_Object((1,3,6,1,4,1,12740,4,7,1))
if mibBuilder.loadTexts:eqlEMMTable.setStatus(_A)
_EqlEMMEntry_Object=MibTableRow
eqlEMMEntry=_EqlEMMEntry_Object((1,3,6,1,4,1,12740,4,7,1,1))
eqlEMMEntry.setIndexNames((0,_G,_H),(0,_I,_J),(0,_K,_V))
if mibBuilder.loadTexts:eqlEMMEntry.setStatus(_A)
class _EqlEMMIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_EqlEMMIndex_Type.__name__=_E
_EqlEMMIndex_Object=MibTableColumn
eqlEMMIndex=_EqlEMMIndex_Object((1,3,6,1,4,1,12740,4,7,1,1,1),_EqlEMMIndex_Type())
eqlEMMIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:eqlEMMIndex.setStatus(_A)
class _EqlEMMModel_Type(DisplayString):defaultValue=OctetString(_O);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EqlEMMModel_Type.__name__=_C
_EqlEMMModel_Object=MibTableColumn
eqlEMMModel=_EqlEMMModel_Object((1,3,6,1,4,1,12740,4,7,1,1,2),_EqlEMMModel_Type())
eqlEMMModel.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlEMMModel.setStatus(_A)
class _EqlEMMPartNum_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlEMMPartNum_Type.__name__=_C
_EqlEMMPartNum_Object=MibTableColumn
eqlEMMPartNum=_EqlEMMPartNum_Object((1,3,6,1,4,1,12740,4,7,1,1,3),_EqlEMMPartNum_Type())
eqlEMMPartNum.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlEMMPartNum.setStatus(_A)
class _EqlEMMRev_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlEMMRev_Type.__name__=_C
_EqlEMMRev_Object=MibTableColumn
eqlEMMRev=_EqlEMMRev_Object((1,3,6,1,4,1,12740,4,7,1,1,4),_EqlEMMRev_Type())
eqlEMMRev.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlEMMRev.setStatus(_A)
class _EqlEMMDate_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlEMMDate_Type.__name__=_C
_EqlEMMDate_Object=MibTableColumn
eqlEMMDate=_EqlEMMDate_Object((1,3,6,1,4,1,12740,4,7,1,1,5),_EqlEMMDate_Type())
eqlEMMDate.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlEMMDate.setStatus(_A)
class _EqlEMMSN_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlEMMSN_Type.__name__=_C
_EqlEMMSN_Object=MibTableColumn
eqlEMMSN=_EqlEMMSN_Object((1,3,6,1,4,1,12740,4,7,1,1,6),_EqlEMMSN_Type())
eqlEMMSN.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlEMMSN.setStatus(_A)
class _EqlEMMECO_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlEMMECO_Type.__name__=_C
_EqlEMMECO_Object=MibTableColumn
eqlEMMECO=_EqlEMMECO_Object((1,3,6,1,4,1,12740,4,7,1,1,7),_EqlEMMECO_Type())
eqlEMMECO.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlEMMECO.setStatus(_A)
class _EqlEMMEEprom_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_EqlEMMEEprom_Type.__name__=_M
_EqlEMMEEprom_Object=MibTableColumn
eqlEMMEEprom=_EqlEMMEEprom_Object((1,3,6,1,4,1,12740,4,7,1,1,8),_EqlEMMEEprom_Type())
eqlEMMEEprom.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlEMMEEprom.setStatus(_A)
class _EqlEMMSN2_Type(DisplayString):defaultValue=OctetString(_D)
_EqlEMMSN2_Type.__name__=_C
_EqlEMMSN2_Object=MibTableColumn
eqlEMMSN2=_EqlEMMSN2_Object((1,3,6,1,4,1,12740,4,7,1,1,9),_EqlEMMSN2_Type())
eqlEMMSN2.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlEMMSN2.setStatus(_A)
_EqlemmNotifications_ObjectIdentity=ObjectIdentity
eqlemmNotifications=_EqlemmNotifications_ObjectIdentity((1,3,6,1,4,1,12740,4,8))
_EqlemmConformance_ObjectIdentity=ObjectIdentity
eqlemmConformance=_EqlemmConformance_ObjectIdentity((1,3,6,1,4,1,12740,4,9))
_EqldaughtercardObjects_ObjectIdentity=ObjectIdentity
eqldaughtercardObjects=_EqldaughtercardObjects_ObjectIdentity((1,3,6,1,4,1,12740,4,10))
_EqlDaughterCardTable_Object=MibTable
eqlDaughterCardTable=_EqlDaughterCardTable_Object((1,3,6,1,4,1,12740,4,10,1))
if mibBuilder.loadTexts:eqlDaughterCardTable.setStatus(_A)
_EqlDaughterCardEntry_Object=MibTableRow
eqlDaughterCardEntry=_EqlDaughterCardEntry_Object((1,3,6,1,4,1,12740,4,10,1,1))
eqlDaughterCardEntry.setIndexNames((0,_G,_H),(0,_I,_J),(0,_K,_W))
if mibBuilder.loadTexts:eqlDaughterCardEntry.setStatus(_A)
class _EqlDaughterCardIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_EqlDaughterCardIndex_Type.__name__=_E
_EqlDaughterCardIndex_Object=MibTableColumn
eqlDaughterCardIndex=_EqlDaughterCardIndex_Object((1,3,6,1,4,1,12740,4,10,1,1,1),_EqlDaughterCardIndex_Type())
eqlDaughterCardIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:eqlDaughterCardIndex.setStatus(_A)
class _EqlDaughterCardModel_Type(DisplayString):defaultValue=OctetString(_O);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EqlDaughterCardModel_Type.__name__=_C
_EqlDaughterCardModel_Object=MibTableColumn
eqlDaughterCardModel=_EqlDaughterCardModel_Object((1,3,6,1,4,1,12740,4,10,1,1,2),_EqlDaughterCardModel_Type())
eqlDaughterCardModel.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDaughterCardModel.setStatus(_A)
class _EqlDaughterCardPartNum_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlDaughterCardPartNum_Type.__name__=_C
_EqlDaughterCardPartNum_Object=MibTableColumn
eqlDaughterCardPartNum=_EqlDaughterCardPartNum_Object((1,3,6,1,4,1,12740,4,10,1,1,3),_EqlDaughterCardPartNum_Type())
eqlDaughterCardPartNum.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDaughterCardPartNum.setStatus(_A)
class _EqlDaughterCardRev_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlDaughterCardRev_Type.__name__=_C
_EqlDaughterCardRev_Object=MibTableColumn
eqlDaughterCardRev=_EqlDaughterCardRev_Object((1,3,6,1,4,1,12740,4,10,1,1,4),_EqlDaughterCardRev_Type())
eqlDaughterCardRev.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDaughterCardRev.setStatus(_A)
class _EqlDaughterCardDate_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlDaughterCardDate_Type.__name__=_C
_EqlDaughterCardDate_Object=MibTableColumn
eqlDaughterCardDate=_EqlDaughterCardDate_Object((1,3,6,1,4,1,12740,4,10,1,1,5),_EqlDaughterCardDate_Type())
eqlDaughterCardDate.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDaughterCardDate.setStatus(_A)
class _EqlDaughterCardSN_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlDaughterCardSN_Type.__name__=_C
_EqlDaughterCardSN_Object=MibTableColumn
eqlDaughterCardSN=_EqlDaughterCardSN_Object((1,3,6,1,4,1,12740,4,10,1,1,6),_EqlDaughterCardSN_Type())
eqlDaughterCardSN.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDaughterCardSN.setStatus(_A)
class _EqlDaughterCardECO_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EqlDaughterCardECO_Type.__name__=_C
_EqlDaughterCardECO_Object=MibTableColumn
eqlDaughterCardECO=_EqlDaughterCardECO_Object((1,3,6,1,4,1,12740,4,10,1,1,7),_EqlDaughterCardECO_Type())
eqlDaughterCardECO.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDaughterCardECO.setStatus(_A)
class _EqlDaughterCardEEprom_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_EqlDaughterCardEEprom_Type.__name__=_M
_EqlDaughterCardEEprom_Object=MibTableColumn
eqlDaughterCardEEprom=_EqlDaughterCardEEprom_Object((1,3,6,1,4,1,12740,4,10,1,1,8),_EqlDaughterCardEEprom_Type())
eqlDaughterCardEEprom.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDaughterCardEEprom.setStatus(_A)
_EqldaughtercardNotifications_ObjectIdentity=ObjectIdentity
eqldaughtercardNotifications=_EqldaughtercardNotifications_ObjectIdentity((1,3,6,1,4,1,12740,4,11))
_EqldaughtercardConformance_ObjectIdentity=ObjectIdentity
eqldaughtercardConformance=_EqldaughtercardConformance_ObjectIdentity((1,3,6,1,4,1,12740,4,12))
_EqlchannelcardObjects_ObjectIdentity=ObjectIdentity
eqlchannelcardObjects=_EqlchannelcardObjects_ObjectIdentity((1,3,6,1,4,1,12740,4,13))
_EqlChannelCardTable_Object=MibTable
eqlChannelCardTable=_EqlChannelCardTable_Object((1,3,6,1,4,1,12740,4,13,1))
if mibBuilder.loadTexts:eqlChannelCardTable.setStatus(_A)
_EqlChannelCardEntry_Object=MibTableRow
eqlChannelCardEntry=_EqlChannelCardEntry_Object((1,3,6,1,4,1,12740,4,13,1,1))
eqlChannelCardEntry.setIndexNames((0,_G,_H),(0,_I,_J),(0,_K,_X))
if mibBuilder.loadTexts:eqlChannelCardEntry.setStatus(_A)
class _EqlChannelCardIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_EqlChannelCardIndex_Type.__name__=_F
_EqlChannelCardIndex_Object=MibTableColumn
eqlChannelCardIndex=_EqlChannelCardIndex_Object((1,3,6,1,4,1,12740,4,13,1,1,1),_EqlChannelCardIndex_Type())
eqlChannelCardIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:eqlChannelCardIndex.setStatus(_A)
class _EqlChannelCardSerialNumber_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EqlChannelCardSerialNumber_Type.__name__=_C
_EqlChannelCardSerialNumber_Object=MibTableColumn
eqlChannelCardSerialNumber=_EqlChannelCardSerialNumber_Object((1,3,6,1,4,1,12740,4,13,1,1,2),_EqlChannelCardSerialNumber_Type())
eqlChannelCardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlChannelCardSerialNumber.setStatus(_A)
class _EqlChannelCardFirmwareRev_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EqlChannelCardFirmwareRev_Type.__name__=_C
_EqlChannelCardFirmwareRev_Object=MibTableColumn
eqlChannelCardFirmwareRev=_EqlChannelCardFirmwareRev_Object((1,3,6,1,4,1,12740,4,13,1,1,3),_EqlChannelCardFirmwareRev_Type())
eqlChannelCardFirmwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlChannelCardFirmwareRev.setStatus(_A)
class _EqlChannelCardInitRev_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EqlChannelCardInitRev_Type.__name__=_C
_EqlChannelCardInitRev_Object=MibTableColumn
eqlChannelCardInitRev=_EqlChannelCardInitRev_Object((1,3,6,1,4,1,12740,4,13,1,1,4),_EqlChannelCardInitRev_Type())
eqlChannelCardInitRev.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlChannelCardInitRev.setStatus(_A)
class _EqlChannelCardStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_N,1),(_P,2),(_Q,3)))
_EqlChannelCardStatus_Type.__name__=_E
_EqlChannelCardStatus_Object=MibTableColumn
eqlChannelCardStatus=_EqlChannelCardStatus_Object((1,3,6,1,4,1,12740,4,13,1,1,5),_EqlChannelCardStatus_Type())
eqlChannelCardStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlChannelCardStatus.setStatus(_A)
_EqlsfpObjects_ObjectIdentity=ObjectIdentity
eqlsfpObjects=_EqlsfpObjects_ObjectIdentity((1,3,6,1,4,1,12740,4,14))
_EqlSFPTable_Object=MibTable
eqlSFPTable=_EqlSFPTable_Object((1,3,6,1,4,1,12740,4,14,1))
if mibBuilder.loadTexts:eqlSFPTable.setStatus(_A)
_EqlSFPEntry_Object=MibTableRow
eqlSFPEntry=_EqlSFPEntry_Object((1,3,6,1,4,1,12740,4,14,1,1))
eqlSFPEntry.setIndexNames((0,_G,_H),(0,_I,_J),(0,_K,_Y))
if mibBuilder.loadTexts:eqlSFPEntry.setStatus(_A)
class _EqlSFPIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_EqlSFPIndex_Type.__name__=_F
_EqlSFPIndex_Object=MibTableColumn
eqlSFPIndex=_EqlSFPIndex_Object((1,3,6,1,4,1,12740,4,14,1,1,1),_EqlSFPIndex_Type())
eqlSFPIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:eqlSFPIndex.setStatus(_A)
class _EqlSFPMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),('single-mode',1),('multi-mode',2),(_Z,3),(_N,4)))
_EqlSFPMode_Type.__name__=_E
_EqlSFPMode_Object=MibTableColumn
eqlSFPMode=_EqlSFPMode_Object((1,3,6,1,4,1,12740,4,14,1,1,2),_EqlSFPMode_Type())
eqlSFPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlSFPMode.setStatus(_A)
_EqlSFPIfIndex_Type=Integer32
_EqlSFPIfIndex_Object=MibTableColumn
eqlSFPIfIndex=_EqlSFPIfIndex_Object((1,3,6,1,4,1,12740,4,14,1,1,3),_EqlSFPIfIndex_Type())
eqlSFPIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlSFPIfIndex.setStatus(_A)
class _EqlSFPIdentifier_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,3)));namedValues=NamedValues(*((_D,0),('sfp-transceiver',3)))
_EqlSFPIdentifier_Type.__name__=_E
_EqlSFPIdentifier_Object=MibTableColumn
eqlSFPIdentifier=_EqlSFPIdentifier_Object((1,3,6,1,4,1,12740,4,14,1,1,4),_EqlSFPIdentifier_Type())
eqlSFPIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlSFPIdentifier.setStatus(_A)
class _EqlSFPConnector_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,7,33)));namedValues=NamedValues(*((_D,0),('lc',7),(_Z,33)))
_EqlSFPConnector_Type.__name__=_E
_EqlSFPConnector_Object=MibTableColumn
eqlSFPConnector=_EqlSFPConnector_Object((1,3,6,1,4,1,12740,4,14,1,1,5),_EqlSFPConnector_Type())
eqlSFPConnector.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlSFPConnector.setStatus(_A)
_EqlSFPBitrate_Type=Integer32
_EqlSFPBitrate_Object=MibTableColumn
eqlSFPBitrate=_EqlSFPBitrate_Object((1,3,6,1,4,1,12740,4,14,1,1,6),_EqlSFPBitrate_Type())
eqlSFPBitrate.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlSFPBitrate.setStatus(_A)
_EqlSFPLength1_Type=Integer32
_EqlSFPLength1_Object=MibTableColumn
eqlSFPLength1=_EqlSFPLength1_Object((1,3,6,1,4,1,12740,4,14,1,1,7),_EqlSFPLength1_Type())
eqlSFPLength1.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlSFPLength1.setStatus(_A)
_EqlSFPLength2_Type=Integer32
_EqlSFPLength2_Object=MibTableColumn
eqlSFPLength2=_EqlSFPLength2_Object((1,3,6,1,4,1,12740,4,14,1,1,8),_EqlSFPLength2_Type())
eqlSFPLength2.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlSFPLength2.setStatus(_A)
class _EqlSFPVendorName_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_EqlSFPVendorName_Type.__name__=_C
_EqlSFPVendorName_Object=MibTableColumn
eqlSFPVendorName=_EqlSFPVendorName_Object((1,3,6,1,4,1,12740,4,14,1,1,9),_EqlSFPVendorName_Type())
eqlSFPVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlSFPVendorName.setStatus(_A)
class _EqlSFPPartNumber_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_EqlSFPPartNumber_Type.__name__=_C
_EqlSFPPartNumber_Object=MibTableColumn
eqlSFPPartNumber=_EqlSFPPartNumber_Object((1,3,6,1,4,1,12740,4,14,1,1,10),_EqlSFPPartNumber_Type())
eqlSFPPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlSFPPartNumber.setStatus(_A)
class _EqlSFPFirmwareRev_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_EqlSFPFirmwareRev_Type.__name__=_C
_EqlSFPFirmwareRev_Object=MibTableColumn
eqlSFPFirmwareRev=_EqlSFPFirmwareRev_Object((1,3,6,1,4,1,12740,4,14,1,1,11),_EqlSFPFirmwareRev_Type())
eqlSFPFirmwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlSFPFirmwareRev.setStatus(_A)
class _EqlSFPSerialNumber_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_EqlSFPSerialNumber_Type.__name__=_C
_EqlSFPSerialNumber_Object=MibTableColumn
eqlSFPSerialNumber=_EqlSFPSerialNumber_Object((1,3,6,1,4,1,12740,4,14,1,1,12),_EqlSFPSerialNumber_Type())
eqlSFPSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlSFPSerialNumber.setStatus(_A)
class _EqlSFPDateCode_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_EqlSFPDateCode_Type.__name__=_C
_EqlSFPDateCode_Object=MibTableColumn
eqlSFPDateCode=_EqlSFPDateCode_Object((1,3,6,1,4,1,12740,4,14,1,1,13),_EqlSFPDateCode_Type())
eqlSFPDateCode.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlSFPDateCode.setStatus(_A)
class _EqlSFPStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_N,1),(_P,2),(_Q,3)))
_EqlSFPStatus_Type.__name__=_E
_EqlSFPStatus_Object=MibTableColumn
eqlSFPStatus=_EqlSFPStatus_Object((1,3,6,1,4,1,12740,4,14,1,1,14),_EqlSFPStatus_Type())
eqlSFPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlSFPStatus.setStatus(_A)
mibBuilder.exportSymbols(_K,**{'eqlcontrollerModule':eqlcontrollerModule,'eqlcontrollerObjects':eqlcontrollerObjects,'eqlControllerTable':eqlControllerTable,'eqlControllerEntry':eqlControllerEntry,_R:eqlControllerIndex,'eqlControllerModel':eqlControllerModel,'eqlControllerCMRevision':eqlControllerCMRevision,'eqlControllerSwRevision':eqlControllerSwRevision,'eqlControllerBatteryStatus':eqlControllerBatteryStatus,'eqlControllerUpTime':eqlControllerUpTime,'eqlControllerProcessorTemp':eqlControllerProcessorTemp,'eqlControllerChipsetTemp':eqlControllerChipsetTemp,'eqlControllerPrimaryOrSecondary':eqlControllerPrimaryOrSecondary,'eqlControllerPrimaryFlashImageRev':eqlControllerPrimaryFlashImageRev,'eqlControllerSecondaryFlashImageRev':eqlControllerSecondaryFlashImageRev,'eqlControllerSerialNumber':eqlControllerSerialNumber,'eqlControllerDate':eqlControllerDate,'eqlControllerECO':eqlControllerECO,'eqlControllerEEprom':eqlControllerEEprom,'eqlControllerPLDrev':eqlControllerPLDrev,'eqlControllerPlatformType':eqlControllerPlatformType,'eqlControllerPlatformVersion':eqlControllerPlatformVersion,'eqlControllerCPUPass':eqlControllerCPUPass,'eqlControllerCPUrev':eqlControllerCPUrev,'eqlControllerCPUfreq':eqlControllerCPUfreq,'eqlControllerPhysRam':eqlControllerPhysRam,'eqlControllerBootRomVersion':eqlControllerBootRomVersion,'eqlControllerBootRomBuildDate':eqlControllerBootRomBuildDate,'eqlControllerInfoMsg':eqlControllerInfoMsg,'eqlControllerAthenaSataVersion':eqlControllerAthenaSataVersion,'eqlControllerMajorVersion':eqlControllerMajorVersion,'eqlControllerMinorVersion':eqlControllerMinorVersion,'eqlControllerMaintenanceVersion':eqlControllerMaintenanceVersion,'eqlControllerSWCompatibilityLevel':eqlControllerSWCompatibilityLevel,'eqlControllerFullSwRevision':eqlControllerFullSwRevision,'eqlControllerNVRAMBattery':eqlControllerNVRAMBattery,'eqlControllerSerialNumber2':eqlControllerSerialNumber2,'eqlControllerType':eqlControllerType,'eqlControllerBootTime':eqlControllerBootTime,'eqlcontrollerNotifications':eqlcontrollerNotifications,'eqlcontrollerConformance':eqlcontrollerConformance,'eqlbackplaneObjects':eqlbackplaneObjects,'eqlBackplaneTable':eqlBackplaneTable,'eqlBackplaneEntry':eqlBackplaneEntry,_U:eqlBackplaneIndex,'eqlBackplanePartNum':eqlBackplanePartNum,'eqlBackplaneRev':eqlBackplaneRev,'eqlBackplaneDate':eqlBackplaneDate,'eqlBackplaneSN':eqlBackplaneSN,'eqlBackplaneECO':eqlBackplaneECO,'eqlBackplaneEEprom':eqlBackplaneEEprom,'eqlBackplaneSN2':eqlBackplaneSN2,'eqlBackplaneType':eqlBackplaneType,'eqlBackplaneTypeId':eqlBackplaneTypeId,'eqlbackplaneNotifications':eqlbackplaneNotifications,'eqlbackplaneConformance':eqlbackplaneConformance,'eqlemmObjects':eqlemmObjects,'eqlEMMTable':eqlEMMTable,'eqlEMMEntry':eqlEMMEntry,_V:eqlEMMIndex,'eqlEMMModel':eqlEMMModel,'eqlEMMPartNum':eqlEMMPartNum,'eqlEMMRev':eqlEMMRev,'eqlEMMDate':eqlEMMDate,'eqlEMMSN':eqlEMMSN,'eqlEMMECO':eqlEMMECO,'eqlEMMEEprom':eqlEMMEEprom,'eqlEMMSN2':eqlEMMSN2,'eqlemmNotifications':eqlemmNotifications,'eqlemmConformance':eqlemmConformance,'eqldaughtercardObjects':eqldaughtercardObjects,'eqlDaughterCardTable':eqlDaughterCardTable,'eqlDaughterCardEntry':eqlDaughterCardEntry,_W:eqlDaughterCardIndex,'eqlDaughterCardModel':eqlDaughterCardModel,'eqlDaughterCardPartNum':eqlDaughterCardPartNum,'eqlDaughterCardRev':eqlDaughterCardRev,'eqlDaughterCardDate':eqlDaughterCardDate,'eqlDaughterCardSN':eqlDaughterCardSN,'eqlDaughterCardECO':eqlDaughterCardECO,'eqlDaughterCardEEprom':eqlDaughterCardEEprom,'eqldaughtercardNotifications':eqldaughtercardNotifications,'eqldaughtercardConformance':eqldaughtercardConformance,'eqlchannelcardObjects':eqlchannelcardObjects,'eqlChannelCardTable':eqlChannelCardTable,'eqlChannelCardEntry':eqlChannelCardEntry,_X:eqlChannelCardIndex,'eqlChannelCardSerialNumber':eqlChannelCardSerialNumber,'eqlChannelCardFirmwareRev':eqlChannelCardFirmwareRev,'eqlChannelCardInitRev':eqlChannelCardInitRev,'eqlChannelCardStatus':eqlChannelCardStatus,'eqlsfpObjects':eqlsfpObjects,'eqlSFPTable':eqlSFPTable,'eqlSFPEntry':eqlSFPEntry,_Y:eqlSFPIndex,'eqlSFPMode':eqlSFPMode,'eqlSFPIfIndex':eqlSFPIfIndex,'eqlSFPIdentifier':eqlSFPIdentifier,'eqlSFPConnector':eqlSFPConnector,'eqlSFPBitrate':eqlSFPBitrate,'eqlSFPLength1':eqlSFPLength1,'eqlSFPLength2':eqlSFPLength2,'eqlSFPVendorName':eqlSFPVendorName,'eqlSFPPartNumber':eqlSFPPartNumber,'eqlSFPFirmwareRev':eqlSFPFirmwareRev,'eqlSFPSerialNumber':eqlSFPSerialNumber,'eqlSFPDateCode':eqlSFPDateCode,'eqlSFPStatus':eqlSFPStatus})