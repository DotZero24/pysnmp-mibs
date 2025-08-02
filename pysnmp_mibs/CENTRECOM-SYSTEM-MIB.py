_I='atiFanNumber'
_H='CENTRECOM-SYSTEM-MIB'
_G='read-write'
_F='secondary'
_E='primary'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extSwitchMIB,=mibBuilder.importSymbols('CENTRECOM-MIB','extSwitchMIB')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
atiSwitchSystem=ModuleIdentity((1,3,6,1,4,1,207,8,12,2,3))
class _AtiSaveConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('saveToPrimary',1),('saveToSecondary',2)))
_AtiSaveConfiguration_Type.__name__=_C
_AtiSaveConfiguration_Object=MibScalar
atiSaveConfiguration=_AtiSaveConfiguration_Object((1,3,6,1,4,1,207,8,12,2,3,3),_AtiSaveConfiguration_Type())
atiSaveConfiguration.setMaxAccess('write-only')
if mibBuilder.loadTexts:atiSaveConfiguration.setStatus(_A)
class _AtiSaveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('saveInProgress',1),('saveNotInProgress',2)))
_AtiSaveStatus_Type.__name__=_C
_AtiSaveStatus_Object=MibScalar
atiSaveStatus=_AtiSaveStatus_Object((1,3,6,1,4,1,207,8,12,2,3,4),_AtiSaveStatus_Type())
atiSaveStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiSaveStatus.setStatus(_A)
class _AtiCurrentConfigInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtiCurrentConfigInUse_Type.__name__=_C
_AtiCurrentConfigInUse_Object=MibScalar
atiCurrentConfigInUse=_AtiCurrentConfigInUse_Object((1,3,6,1,4,1,207,8,12,2,3,5),_AtiCurrentConfigInUse_Type())
atiCurrentConfigInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:atiCurrentConfigInUse.setStatus(_A)
class _AtiConfigToUseOnReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtiConfigToUseOnReboot_Type.__name__=_C
_AtiConfigToUseOnReboot_Object=MibScalar
atiConfigToUseOnReboot=_AtiConfigToUseOnReboot_Object((1,3,6,1,4,1,207,8,12,2,3,6),_AtiConfigToUseOnReboot_Type())
atiConfigToUseOnReboot.setMaxAccess(_G)
if mibBuilder.loadTexts:atiConfigToUseOnReboot.setStatus(_A)
_AtiOverTemperatureAlarm_Type=TruthValue
_AtiOverTemperatureAlarm_Object=MibScalar
atiOverTemperatureAlarm=_AtiOverTemperatureAlarm_Object((1,3,6,1,4,1,207,8,12,2,3,7),_AtiOverTemperatureAlarm_Type())
atiOverTemperatureAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:atiOverTemperatureAlarm.setStatus(_A)
class _AtiCurrentTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AtiCurrentTemperature_Type.__name__=_C
_AtiCurrentTemperature_Object=MibScalar
atiCurrentTemperature=_AtiCurrentTemperature_Object((1,3,6,1,4,1,207,8,12,2,3,8),_AtiCurrentTemperature_Type())
atiCurrentTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:atiCurrentTemperature.setStatus(_A)
_AtiFanStatusTable_Object=MibTable
atiFanStatusTable=_AtiFanStatusTable_Object((1,3,6,1,4,1,207,8,12,2,3,9))
if mibBuilder.loadTexts:atiFanStatusTable.setStatus(_A)
_AtiFanStatusEntry_Object=MibTableRow
atiFanStatusEntry=_AtiFanStatusEntry_Object((1,3,6,1,4,1,207,8,12,2,3,9,1))
atiFanStatusEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:atiFanStatusEntry.setStatus(_A)
_AtiFanNumber_Type=Integer32
_AtiFanNumber_Object=MibTableColumn
atiFanNumber=_AtiFanNumber_Object((1,3,6,1,4,1,207,8,12,2,3,9,1,1),_AtiFanNumber_Type())
atiFanNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:atiFanNumber.setStatus(_A)
_AtiFanOperational_Type=TruthValue
_AtiFanOperational_Object=MibTableColumn
atiFanOperational=_AtiFanOperational_Object((1,3,6,1,4,1,207,8,12,2,3,9,1,2),_AtiFanOperational_Type())
atiFanOperational.setMaxAccess(_B)
if mibBuilder.loadTexts:atiFanOperational.setStatus(_A)
_AtiPrimaryPowerOperational_Type=TruthValue
_AtiPrimaryPowerOperational_Object=MibScalar
atiPrimaryPowerOperational=_AtiPrimaryPowerOperational_Object((1,3,6,1,4,1,207,8,12,2,3,10),_AtiPrimaryPowerOperational_Type())
atiPrimaryPowerOperational.setMaxAccess(_B)
if mibBuilder.loadTexts:atiPrimaryPowerOperational.setStatus(_A)
class _AtiRedundantPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notPresent',1),('presentOK',2),('presentNotOK',3)))
_AtiRedundantPowerStatus_Type.__name__=_C
_AtiRedundantPowerStatus_Object=MibScalar
atiRedundantPowerStatus=_AtiRedundantPowerStatus_Object((1,3,6,1,4,1,207,8,12,2,3,11),_AtiRedundantPowerStatus_Type())
atiRedundantPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiRedundantPowerStatus.setStatus(_A)
_AtiRedundantPowerAlarm_Type=TruthValue
_AtiRedundantPowerAlarm_Object=MibScalar
atiRedundantPowerAlarm=_AtiRedundantPowerAlarm_Object((1,3,6,1,4,1,207,8,12,2,3,12),_AtiRedundantPowerAlarm_Type())
atiRedundantPowerAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:atiRedundantPowerAlarm.setStatus(_A)
class _AtiPrimarySoftwareRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AtiPrimarySoftwareRev_Type.__name__=_D
_AtiPrimarySoftwareRev_Object=MibScalar
atiPrimarySoftwareRev=_AtiPrimarySoftwareRev_Object((1,3,6,1,4,1,207,8,12,2,3,13),_AtiPrimarySoftwareRev_Type())
atiPrimarySoftwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:atiPrimarySoftwareRev.setStatus(_A)
class _AtiSecondarySoftwareRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AtiSecondarySoftwareRev_Type.__name__=_D
_AtiSecondarySoftwareRev_Object=MibScalar
atiSecondarySoftwareRev=_AtiSecondarySoftwareRev_Object((1,3,6,1,4,1,207,8,12,2,3,14),_AtiSecondarySoftwareRev_Type())
atiSecondarySoftwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:atiSecondarySoftwareRev.setStatus(_A)
class _AtiImageToUseOnReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AtiImageToUseOnReboot_Type.__name__=_C
_AtiImageToUseOnReboot_Object=MibScalar
atiImageToUseOnReboot=_AtiImageToUseOnReboot_Object((1,3,6,1,4,1,207,8,12,2,3,15),_AtiImageToUseOnReboot_Type())
atiImageToUseOnReboot.setMaxAccess(_G)
if mibBuilder.loadTexts:atiImageToUseOnReboot.setStatus(_A)
class _AtiSystemID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,126))
_AtiSystemID_Type.__name__=_D
_AtiSystemID_Object=MibScalar
atiSystemID=_AtiSystemID_Object((1,3,6,1,4,1,207,8,12,2,3,16),_AtiSystemID_Type())
atiSystemID.setMaxAccess(_B)
if mibBuilder.loadTexts:atiSystemID.setStatus(_A)
class _AtiSystemBoardID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,126))
_AtiSystemBoardID_Type.__name__=_D
_AtiSystemBoardID_Object=MibScalar
atiSystemBoardID=_AtiSystemBoardID_Object((1,3,6,1,4,1,207,8,12,2,3,17),_AtiSystemBoardID_Type())
atiSystemBoardID.setMaxAccess(_B)
if mibBuilder.loadTexts:atiSystemBoardID.setStatus(_A)
class _AtiSystemLeftBoardID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,126))
_AtiSystemLeftBoardID_Type.__name__=_D
_AtiSystemLeftBoardID_Object=MibScalar
atiSystemLeftBoardID=_AtiSystemLeftBoardID_Object((1,3,6,1,4,1,207,8,12,2,3,18),_AtiSystemLeftBoardID_Type())
atiSystemLeftBoardID.setMaxAccess(_B)
if mibBuilder.loadTexts:atiSystemLeftBoardID.setStatus(_A)
class _AtiSystemRightBoardID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,126))
_AtiSystemRightBoardID_Type.__name__=_D
_AtiSystemRightBoardID_Object=MibScalar
atiSystemRightBoardID=_AtiSystemRightBoardID_Object((1,3,6,1,4,1,207,8,12,2,3,19),_AtiSystemRightBoardID_Type())
atiSystemRightBoardID.setMaxAccess(_B)
if mibBuilder.loadTexts:atiSystemRightBoardID.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'atiSwitchSystem':atiSwitchSystem,'atiSaveConfiguration':atiSaveConfiguration,'atiSaveStatus':atiSaveStatus,'atiCurrentConfigInUse':atiCurrentConfigInUse,'atiConfigToUseOnReboot':atiConfigToUseOnReboot,'atiOverTemperatureAlarm':atiOverTemperatureAlarm,'atiCurrentTemperature':atiCurrentTemperature,'atiFanStatusTable':atiFanStatusTable,'atiFanStatusEntry':atiFanStatusEntry,_I:atiFanNumber,'atiFanOperational':atiFanOperational,'atiPrimaryPowerOperational':atiPrimaryPowerOperational,'atiRedundantPowerStatus':atiRedundantPowerStatus,'atiRedundantPowerAlarm':atiRedundantPowerAlarm,'atiPrimarySoftwareRev':atiPrimarySoftwareRev,'atiSecondarySoftwareRev':atiSecondarySoftwareRev,'atiImageToUseOnReboot':atiImageToUseOnReboot,'atiSystemID':atiSystemID,'atiSystemBoardID':atiSystemBoardID,'atiSystemLeftBoardID':atiSystemLeftBoardID,'atiSystemRightBoardID':atiSystemRightBoardID})