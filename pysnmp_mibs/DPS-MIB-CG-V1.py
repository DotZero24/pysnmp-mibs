_H='cgBatteryNumber'
_G='cgStringNumber'
_F='cgStrNumber'
_E='not-accessible'
_D='DPS-MIB-CG-V1'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dpsCellguard=ModuleIdentity((1,3,6,1,4,1,2682,2))
if mibBuilder.loadTexts:dpsCellguard.setRevisions(('2013-10-18 12:00',))
_DpsInc_ObjectIdentity=ObjectIdentity
dpsInc=_DpsInc_ObjectIdentity((1,3,6,1,4,1,2682))
_CgStringChannels_Object=MibTable
cgStringChannels=_CgStringChannels_Object((1,3,6,1,4,1,2682,2,1))
if mibBuilder.loadTexts:cgStringChannels.setStatus(_A)
_CgStringEntry_Object=MibTableRow
cgStringEntry=_CgStringEntry_Object((1,3,6,1,4,1,2682,2,1,1))
cgStringEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:cgStringEntry.setStatus(_A)
class _CgStrNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_CgStrNumber_Type.__name__=_C
_CgStrNumber_Object=MibTableColumn
cgStrNumber=_CgStrNumber_Object((1,3,6,1,4,1,2682,2,1,1,1),_CgStrNumber_Type())
cgStrNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cgStrNumber.setStatus(_A)
class _CgStrEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_CgStrEnabled_Type.__name__=_C
_CgStrEnabled_Object=MibTableColumn
cgStrEnabled=_CgStrEnabled_Object((1,3,6,1,4,1,2682,2,1,1,2),_CgStrEnabled_Type())
cgStrEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:cgStrEnabled.setStatus(_A)
_CgStrStatus_Type=DisplayString
_CgStrStatus_Object=MibTableColumn
cgStrStatus=_CgStrStatus_Object((1,3,6,1,4,1,2682,2,1,1,3),_CgStrStatus_Type())
cgStrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cgStrStatus.setStatus(_A)
_CgStrVoltage_Type=DisplayString
_CgStrVoltage_Object=MibTableColumn
cgStrVoltage=_CgStrVoltage_Object((1,3,6,1,4,1,2682,2,1,1,4),_CgStrVoltage_Type())
cgStrVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cgStrVoltage.setStatus(_A)
_CgStrCurrent_Type=DisplayString
_CgStrCurrent_Object=MibTableColumn
cgStrCurrent=_CgStrCurrent_Object((1,3,6,1,4,1,2682,2,1,1,5),_CgStrCurrent_Type())
cgStrCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:cgStrCurrent.setStatus(_A)
_CgStrTempA_Type=DisplayString
_CgStrTempA_Object=MibTableColumn
cgStrTempA=_CgStrTempA_Object((1,3,6,1,4,1,2682,2,1,1,6),_CgStrTempA_Type())
cgStrTempA.setMaxAccess(_B)
if mibBuilder.loadTexts:cgStrTempA.setStatus(_A)
_CgStrTempB_Type=DisplayString
_CgStrTempB_Object=MibTableColumn
cgStrTempB=_CgStrTempB_Object((1,3,6,1,4,1,2682,2,1,1,7),_CgStrTempB_Type())
cgStrTempB.setMaxAccess(_B)
if mibBuilder.loadTexts:cgStrTempB.setStatus(_A)
_CgStrConductance_Type=DisplayString
_CgStrConductance_Object=MibTableColumn
cgStrConductance=_CgStrConductance_Object((1,3,6,1,4,1,2682,2,1,1,8),_CgStrConductance_Type())
cgStrConductance.setMaxAccess(_B)
if mibBuilder.loadTexts:cgStrConductance.setStatus(_A)
_CgStrLife_Type=DisplayString
_CgStrLife_Object=MibTableColumn
cgStrLife=_CgStrLife_Object((1,3,6,1,4,1,2682,2,1,1,9),_CgStrLife_Type())
cgStrLife.setMaxAccess(_B)
if mibBuilder.loadTexts:cgStrLife.setStatus(_A)
_CgBatteryChannels_Object=MibTable
cgBatteryChannels=_CgBatteryChannels_Object((1,3,6,1,4,1,2682,2,2))
if mibBuilder.loadTexts:cgBatteryChannels.setStatus(_A)
_CgBatteryEntry_Object=MibTableRow
cgBatteryEntry=_CgBatteryEntry_Object((1,3,6,1,4,1,2682,2,2,1))
cgBatteryEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:cgBatteryEntry.setStatus(_A)
class _CgStringNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_CgStringNumber_Type.__name__=_C
_CgStringNumber_Object=MibTableColumn
cgStringNumber=_CgStringNumber_Object((1,3,6,1,4,1,2682,2,2,1,1),_CgStringNumber_Type())
cgStringNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cgStringNumber.setStatus(_A)
class _CgBatteryNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,240))
_CgBatteryNumber_Type.__name__=_C
_CgBatteryNumber_Object=MibTableColumn
cgBatteryNumber=_CgBatteryNumber_Object((1,3,6,1,4,1,2682,2,2,1,2),_CgBatteryNumber_Type())
cgBatteryNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cgBatteryNumber.setStatus(_A)
_CgStatus_Type=DisplayString
_CgStatus_Object=MibTableColumn
cgStatus=_CgStatus_Object((1,3,6,1,4,1,2682,2,2,1,3),_CgStatus_Type())
cgStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cgStatus.setStatus(_A)
_CgVoltage_Type=DisplayString
_CgVoltage_Object=MibTableColumn
cgVoltage=_CgVoltage_Object((1,3,6,1,4,1,2682,2,2,1,4),_CgVoltage_Type())
cgVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cgVoltage.setStatus(_A)
_CgTemperature_Type=DisplayString
_CgTemperature_Object=MibTableColumn
cgTemperature=_CgTemperature_Object((1,3,6,1,4,1,2682,2,2,1,5),_CgTemperature_Type())
cgTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cgTemperature.setStatus(_A)
_CgStrapResist_Type=DisplayString
_CgStrapResist_Object=MibTableColumn
cgStrapResist=_CgStrapResist_Object((1,3,6,1,4,1,2682,2,2,1,6),_CgStrapResist_Type())
cgStrapResist.setMaxAccess(_B)
if mibBuilder.loadTexts:cgStrapResist.setStatus(_A)
_CgConductance_Type=DisplayString
_CgConductance_Object=MibTableColumn
cgConductance=_CgConductance_Object((1,3,6,1,4,1,2682,2,2,1,7),_CgConductance_Type())
cgConductance.setMaxAccess(_B)
if mibBuilder.loadTexts:cgConductance.setStatus(_A)
_CgBatteryLife_Type=DisplayString
_CgBatteryLife_Object=MibTableColumn
cgBatteryLife=_CgBatteryLife_Object((1,3,6,1,4,1,2682,2,2,1,8),_CgBatteryLife_Type())
cgBatteryLife.setMaxAccess(_B)
if mibBuilder.loadTexts:cgBatteryLife.setStatus(_A)
_CellguardTrap_ObjectIdentity=ObjectIdentity
cellguardTrap=_CellguardTrap_ObjectIdentity((1,3,6,1,4,1,2682,2,8000))
class _CgTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',0),('voltage',1),(_A,2),('temperature',3),('strapResistance',4),('life',5),('conductance',6)))
_CgTrapType_Type.__name__=_C
_CgTrapType_Object=MibScalar
cgTrapType=_CgTrapType_Object((1,3,6,1,4,1,2682,2,8000,2),_CgTrapType_Type())
cgTrapType.setMaxAccess(_E)
if mibBuilder.loadTexts:cgTrapType.setStatus(_A)
class _CgTrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('noAlarm',0),('minorUnder',1),('minorOver',2),('majorUnder',3),('majorOver',4),('notDetected',5)))
_CgTrapStatus_Type.__name__=_C
_CgTrapStatus_Object=MibScalar
cgTrapStatus=_CgTrapStatus_Object((1,3,6,1,4,1,2682,2,8000,3),_CgTrapStatus_Type())
cgTrapStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cgTrapStatus.setStatus(_A)
_CgTrapValue_Type=DisplayString
_CgTrapValue_Object=MibScalar
cgTrapValue=_CgTrapValue_Object((1,3,6,1,4,1,2682,2,8000,4),_CgTrapValue_Type())
cgTrapValue.setMaxAccess(_E)
if mibBuilder.loadTexts:cgTrapValue.setStatus(_A)
cgAlarmTrap=NotificationType((1,3,6,1,4,1,2682,2,8000,1))
if mibBuilder.loadTexts:cgAlarmTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'dpsInc':dpsInc,'dpsCellguard':dpsCellguard,'cgStringChannels':cgStringChannels,'cgStringEntry':cgStringEntry,_F:cgStrNumber,'cgStrEnabled':cgStrEnabled,'cgStrStatus':cgStrStatus,'cgStrVoltage':cgStrVoltage,'cgStrCurrent':cgStrCurrent,'cgStrTempA':cgStrTempA,'cgStrTempB':cgStrTempB,'cgStrConductance':cgStrConductance,'cgStrLife':cgStrLife,'cgBatteryChannels':cgBatteryChannels,'cgBatteryEntry':cgBatteryEntry,_G:cgStringNumber,_H:cgBatteryNumber,'cgStatus':cgStatus,'cgVoltage':cgVoltage,'cgTemperature':cgTemperature,'cgStrapResist':cgStrapResist,'cgConductance':cgConductance,'cgBatteryLife':cgBatteryLife,'cellguardTrap':cellguardTrap,'cgAlarmTrap':cgAlarmTrap,'cgTrapType':cgTrapType,'cgTrapStatus':cgTrapStatus,'cgTrapValue':cgTrapValue})