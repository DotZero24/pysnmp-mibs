_O='zyHwMonitorPowerSourcePreviousStatus'
_N='zyHwMonitorTrapPowerSourceErrorType'
_M='zyHwMonitorVoltageDescription'
_L='zyHwMonitorTemperatureDescription'
_K='zyHwMonitorFanRpmDescription'
_J='zyHwMonitorPowerSourceDescription'
_I='zyHwMonitorPowerSourceStatus'
_H='zyHwMonitorVoltageIndex'
_G='zyHwMonitorTemperatureIndex'
_F='zyHwMonitorFanRpmIndex'
_E='zyHwMonitorPowerSourceIndex'
_D='not-accessible'
_C='read-only'
_B='ZYXEL-HW-MONITOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelHwMonitor=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,26))
_ZyxelHwMonitorStatus_ObjectIdentity=ObjectIdentity
zyxelHwMonitorStatus=_ZyxelHwMonitorStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,26,1))
_ZyxelHwMonitorFanRpmTable_Object=MibTable
zyxelHwMonitorFanRpmTable=_ZyxelHwMonitorFanRpmTable_Object((1,3,6,1,4,1,890,1,15,3,26,1,1))
if mibBuilder.loadTexts:zyxelHwMonitorFanRpmTable.setStatus(_A)
_ZyxelHwMonitorFanRpmEntry_Object=MibTableRow
zyxelHwMonitorFanRpmEntry=_ZyxelHwMonitorFanRpmEntry_Object((1,3,6,1,4,1,890,1,15,3,26,1,1,1))
zyxelHwMonitorFanRpmEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zyxelHwMonitorFanRpmEntry.setStatus(_A)
_ZyHwMonitorFanRpmIndex_Type=Integer32
_ZyHwMonitorFanRpmIndex_Object=MibTableColumn
zyHwMonitorFanRpmIndex=_ZyHwMonitorFanRpmIndex_Object((1,3,6,1,4,1,890,1,15,3,26,1,1,1,1),_ZyHwMonitorFanRpmIndex_Type())
zyHwMonitorFanRpmIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zyHwMonitorFanRpmIndex.setStatus(_A)
_ZyHwMonitorFanRpmDescription_Type=DisplayString
_ZyHwMonitorFanRpmDescription_Object=MibTableColumn
zyHwMonitorFanRpmDescription=_ZyHwMonitorFanRpmDescription_Object((1,3,6,1,4,1,890,1,15,3,26,1,1,1,2),_ZyHwMonitorFanRpmDescription_Type())
zyHwMonitorFanRpmDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorFanRpmDescription.setStatus(_A)
_ZyHwMonitorFanRpmCurrentValue_Type=Integer32
_ZyHwMonitorFanRpmCurrentValue_Object=MibTableColumn
zyHwMonitorFanRpmCurrentValue=_ZyHwMonitorFanRpmCurrentValue_Object((1,3,6,1,4,1,890,1,15,3,26,1,1,1,3),_ZyHwMonitorFanRpmCurrentValue_Type())
zyHwMonitorFanRpmCurrentValue.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorFanRpmCurrentValue.setStatus(_A)
_ZyHwMonitorFanRpmMaxValue_Type=Integer32
_ZyHwMonitorFanRpmMaxValue_Object=MibTableColumn
zyHwMonitorFanRpmMaxValue=_ZyHwMonitorFanRpmMaxValue_Object((1,3,6,1,4,1,890,1,15,3,26,1,1,1,4),_ZyHwMonitorFanRpmMaxValue_Type())
zyHwMonitorFanRpmMaxValue.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorFanRpmMaxValue.setStatus(_A)
_ZyHwMonitorFanRpmMinValue_Type=Integer32
_ZyHwMonitorFanRpmMinValue_Object=MibTableColumn
zyHwMonitorFanRpmMinValue=_ZyHwMonitorFanRpmMinValue_Object((1,3,6,1,4,1,890,1,15,3,26,1,1,1,5),_ZyHwMonitorFanRpmMinValue_Type())
zyHwMonitorFanRpmMinValue.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorFanRpmMinValue.setStatus(_A)
_ZyHwMonitorFanRpmLowThreshold_Type=Integer32
_ZyHwMonitorFanRpmLowThreshold_Object=MibTableColumn
zyHwMonitorFanRpmLowThreshold=_ZyHwMonitorFanRpmLowThreshold_Object((1,3,6,1,4,1,890,1,15,3,26,1,1,1,6),_ZyHwMonitorFanRpmLowThreshold_Type())
zyHwMonitorFanRpmLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorFanRpmLowThreshold.setStatus(_A)
_ZyHwMonitorFanRpmStatus_Type=DisplayString
_ZyHwMonitorFanRpmStatus_Object=MibTableColumn
zyHwMonitorFanRpmStatus=_ZyHwMonitorFanRpmStatus_Object((1,3,6,1,4,1,890,1,15,3,26,1,1,1,7),_ZyHwMonitorFanRpmStatus_Type())
zyHwMonitorFanRpmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorFanRpmStatus.setStatus(_A)
_ZyxelHwMonitorTemperatureTable_Object=MibTable
zyxelHwMonitorTemperatureTable=_ZyxelHwMonitorTemperatureTable_Object((1,3,6,1,4,1,890,1,15,3,26,1,2))
if mibBuilder.loadTexts:zyxelHwMonitorTemperatureTable.setStatus(_A)
_ZyxelHwMonitorTemperatureEntry_Object=MibTableRow
zyxelHwMonitorTemperatureEntry=_ZyxelHwMonitorTemperatureEntry_Object((1,3,6,1,4,1,890,1,15,3,26,1,2,1))
zyxelHwMonitorTemperatureEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:zyxelHwMonitorTemperatureEntry.setStatus(_A)
_ZyHwMonitorTemperatureIndex_Type=Integer32
_ZyHwMonitorTemperatureIndex_Object=MibTableColumn
zyHwMonitorTemperatureIndex=_ZyHwMonitorTemperatureIndex_Object((1,3,6,1,4,1,890,1,15,3,26,1,2,1,1),_ZyHwMonitorTemperatureIndex_Type())
zyHwMonitorTemperatureIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zyHwMonitorTemperatureIndex.setStatus(_A)
_ZyHwMonitorTemperatureDescription_Type=DisplayString
_ZyHwMonitorTemperatureDescription_Object=MibTableColumn
zyHwMonitorTemperatureDescription=_ZyHwMonitorTemperatureDescription_Object((1,3,6,1,4,1,890,1,15,3,26,1,2,1,2),_ZyHwMonitorTemperatureDescription_Type())
zyHwMonitorTemperatureDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorTemperatureDescription.setStatus(_A)
_ZyHwMonitorTemperatureCurrentValue_Type=Integer32
_ZyHwMonitorTemperatureCurrentValue_Object=MibTableColumn
zyHwMonitorTemperatureCurrentValue=_ZyHwMonitorTemperatureCurrentValue_Object((1,3,6,1,4,1,890,1,15,3,26,1,2,1,3),_ZyHwMonitorTemperatureCurrentValue_Type())
zyHwMonitorTemperatureCurrentValue.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorTemperatureCurrentValue.setStatus(_A)
_ZyHwMonitorTemperatureMaxValue_Type=Integer32
_ZyHwMonitorTemperatureMaxValue_Object=MibTableColumn
zyHwMonitorTemperatureMaxValue=_ZyHwMonitorTemperatureMaxValue_Object((1,3,6,1,4,1,890,1,15,3,26,1,2,1,4),_ZyHwMonitorTemperatureMaxValue_Type())
zyHwMonitorTemperatureMaxValue.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorTemperatureMaxValue.setStatus(_A)
_ZyHwMonitorTemperatureMinValue_Type=Integer32
_ZyHwMonitorTemperatureMinValue_Object=MibTableColumn
zyHwMonitorTemperatureMinValue=_ZyHwMonitorTemperatureMinValue_Object((1,3,6,1,4,1,890,1,15,3,26,1,2,1,5),_ZyHwMonitorTemperatureMinValue_Type())
zyHwMonitorTemperatureMinValue.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorTemperatureMinValue.setStatus(_A)
_ZyHwMonitorTemperatureHighThreshold_Type=Integer32
_ZyHwMonitorTemperatureHighThreshold_Object=MibTableColumn
zyHwMonitorTemperatureHighThreshold=_ZyHwMonitorTemperatureHighThreshold_Object((1,3,6,1,4,1,890,1,15,3,26,1,2,1,6),_ZyHwMonitorTemperatureHighThreshold_Type())
zyHwMonitorTemperatureHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorTemperatureHighThreshold.setStatus(_A)
_ZyHwMonitorTemperatureStatus_Type=DisplayString
_ZyHwMonitorTemperatureStatus_Object=MibTableColumn
zyHwMonitorTemperatureStatus=_ZyHwMonitorTemperatureStatus_Object((1,3,6,1,4,1,890,1,15,3,26,1,2,1,7),_ZyHwMonitorTemperatureStatus_Type())
zyHwMonitorTemperatureStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorTemperatureStatus.setStatus(_A)
_ZyxelHwMonitorVoltageTable_Object=MibTable
zyxelHwMonitorVoltageTable=_ZyxelHwMonitorVoltageTable_Object((1,3,6,1,4,1,890,1,15,3,26,1,3))
if mibBuilder.loadTexts:zyxelHwMonitorVoltageTable.setStatus(_A)
_ZyxelHwMonitorVoltageEntry_Object=MibTableRow
zyxelHwMonitorVoltageEntry=_ZyxelHwMonitorVoltageEntry_Object((1,3,6,1,4,1,890,1,15,3,26,1,3,1))
zyxelHwMonitorVoltageEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:zyxelHwMonitorVoltageEntry.setStatus(_A)
_ZyHwMonitorVoltageIndex_Type=Integer32
_ZyHwMonitorVoltageIndex_Object=MibTableColumn
zyHwMonitorVoltageIndex=_ZyHwMonitorVoltageIndex_Object((1,3,6,1,4,1,890,1,15,3,26,1,3,1,1),_ZyHwMonitorVoltageIndex_Type())
zyHwMonitorVoltageIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zyHwMonitorVoltageIndex.setStatus(_A)
_ZyHwMonitorVoltageDescription_Type=DisplayString
_ZyHwMonitorVoltageDescription_Object=MibTableColumn
zyHwMonitorVoltageDescription=_ZyHwMonitorVoltageDescription_Object((1,3,6,1,4,1,890,1,15,3,26,1,3,1,2),_ZyHwMonitorVoltageDescription_Type())
zyHwMonitorVoltageDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorVoltageDescription.setStatus(_A)
_ZyHwMonitorVoltageCurrentValue_Type=Integer32
_ZyHwMonitorVoltageCurrentValue_Object=MibTableColumn
zyHwMonitorVoltageCurrentValue=_ZyHwMonitorVoltageCurrentValue_Object((1,3,6,1,4,1,890,1,15,3,26,1,3,1,3),_ZyHwMonitorVoltageCurrentValue_Type())
zyHwMonitorVoltageCurrentValue.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorVoltageCurrentValue.setStatus(_A)
_ZyHwMonitorVoltageMaxValue_Type=Integer32
_ZyHwMonitorVoltageMaxValue_Object=MibTableColumn
zyHwMonitorVoltageMaxValue=_ZyHwMonitorVoltageMaxValue_Object((1,3,6,1,4,1,890,1,15,3,26,1,3,1,4),_ZyHwMonitorVoltageMaxValue_Type())
zyHwMonitorVoltageMaxValue.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorVoltageMaxValue.setStatus(_A)
_ZyHwMonitorVoltageMinValue_Type=Integer32
_ZyHwMonitorVoltageMinValue_Object=MibTableColumn
zyHwMonitorVoltageMinValue=_ZyHwMonitorVoltageMinValue_Object((1,3,6,1,4,1,890,1,15,3,26,1,3,1,5),_ZyHwMonitorVoltageMinValue_Type())
zyHwMonitorVoltageMinValue.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorVoltageMinValue.setStatus(_A)
_ZyHwMonitorVoltageNominalValue_Type=Integer32
_ZyHwMonitorVoltageNominalValue_Object=MibTableColumn
zyHwMonitorVoltageNominalValue=_ZyHwMonitorVoltageNominalValue_Object((1,3,6,1,4,1,890,1,15,3,26,1,3,1,6),_ZyHwMonitorVoltageNominalValue_Type())
zyHwMonitorVoltageNominalValue.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorVoltageNominalValue.setStatus(_A)
_ZyHwMonitorVoltageLowThreshold_Type=Integer32
_ZyHwMonitorVoltageLowThreshold_Object=MibTableColumn
zyHwMonitorVoltageLowThreshold=_ZyHwMonitorVoltageLowThreshold_Object((1,3,6,1,4,1,890,1,15,3,26,1,3,1,7),_ZyHwMonitorVoltageLowThreshold_Type())
zyHwMonitorVoltageLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorVoltageLowThreshold.setStatus(_A)
_ZyHwMonitorVoltageStatus_Type=DisplayString
_ZyHwMonitorVoltageStatus_Object=MibTableColumn
zyHwMonitorVoltageStatus=_ZyHwMonitorVoltageStatus_Object((1,3,6,1,4,1,890,1,15,3,26,1,3,1,8),_ZyHwMonitorVoltageStatus_Type())
zyHwMonitorVoltageStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorVoltageStatus.setStatus(_A)
_ZyxelHwMonitorPowerSource_ObjectIdentity=ObjectIdentity
zyxelHwMonitorPowerSource=_ZyxelHwMonitorPowerSource_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,26,1,4))
_ZyHwMonitorPowerSourceMode_Type=DisplayString
_ZyHwMonitorPowerSourceMode_Object=MibScalar
zyHwMonitorPowerSourceMode=_ZyHwMonitorPowerSourceMode_Object((1,3,6,1,4,1,890,1,15,3,26,1,4,1),_ZyHwMonitorPowerSourceMode_Type())
zyHwMonitorPowerSourceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorPowerSourceMode.setStatus(_A)
_ZyxelHwMonitorPowerSourceTable_Object=MibTable
zyxelHwMonitorPowerSourceTable=_ZyxelHwMonitorPowerSourceTable_Object((1,3,6,1,4,1,890,1,15,3,26,1,4,2))
if mibBuilder.loadTexts:zyxelHwMonitorPowerSourceTable.setStatus(_A)
_ZyxelHwMonitorPowerSourceEntry_Object=MibTableRow
zyxelHwMonitorPowerSourceEntry=_ZyxelHwMonitorPowerSourceEntry_Object((1,3,6,1,4,1,890,1,15,3,26,1,4,2,1))
zyxelHwMonitorPowerSourceEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:zyxelHwMonitorPowerSourceEntry.setStatus(_A)
_ZyHwMonitorPowerSourceIndex_Type=Integer32
_ZyHwMonitorPowerSourceIndex_Object=MibTableColumn
zyHwMonitorPowerSourceIndex=_ZyHwMonitorPowerSourceIndex_Object((1,3,6,1,4,1,890,1,15,3,26,1,4,2,1,1),_ZyHwMonitorPowerSourceIndex_Type())
zyHwMonitorPowerSourceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zyHwMonitorPowerSourceIndex.setStatus(_A)
_ZyHwMonitorPowerSourceType_Type=DisplayString
_ZyHwMonitorPowerSourceType_Object=MibTableColumn
zyHwMonitorPowerSourceType=_ZyHwMonitorPowerSourceType_Object((1,3,6,1,4,1,890,1,15,3,26,1,4,2,1,2),_ZyHwMonitorPowerSourceType_Type())
zyHwMonitorPowerSourceType.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorPowerSourceType.setStatus(_A)
_ZyHwMonitorPowerSourceStatus_Type=DisplayString
_ZyHwMonitorPowerSourceStatus_Object=MibTableColumn
zyHwMonitorPowerSourceStatus=_ZyHwMonitorPowerSourceStatus_Object((1,3,6,1,4,1,890,1,15,3,26,1,4,2,1,3),_ZyHwMonitorPowerSourceStatus_Type())
zyHwMonitorPowerSourceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorPowerSourceStatus.setStatus(_A)
_ZyHwMonitorPowerSourceDescription_Type=DisplayString
_ZyHwMonitorPowerSourceDescription_Object=MibTableColumn
zyHwMonitorPowerSourceDescription=_ZyHwMonitorPowerSourceDescription_Object((1,3,6,1,4,1,890,1,15,3,26,1,4,2,1,4),_ZyHwMonitorPowerSourceDescription_Type())
zyHwMonitorPowerSourceDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorPowerSourceDescription.setStatus(_A)
_ZyHwMonitorPowerSourcePreviousStatus_Type=DisplayString
_ZyHwMonitorPowerSourcePreviousStatus_Object=MibTableColumn
zyHwMonitorPowerSourcePreviousStatus=_ZyHwMonitorPowerSourcePreviousStatus_Object((1,3,6,1,4,1,890,1,15,3,26,1,4,2,1,5),_ZyHwMonitorPowerSourcePreviousStatus_Type())
zyHwMonitorPowerSourcePreviousStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHwMonitorPowerSourcePreviousStatus.setStatus(_A)
_ZyxelHwMonitorNotifications_ObjectIdentity=ObjectIdentity
zyxelHwMonitorNotifications=_ZyxelHwMonitorNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,26,2))
_ZyxelHwMonitorTrapInfoObject_ObjectIdentity=ObjectIdentity
zyxelHwMonitorTrapInfoObject=_ZyxelHwMonitorTrapInfoObject_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,26,3))
_ZyHwMonitorTrapPowerSourceErrorType_Type=DisplayString
_ZyHwMonitorTrapPowerSourceErrorType_Object=MibScalar
zyHwMonitorTrapPowerSourceErrorType=_ZyHwMonitorTrapPowerSourceErrorType_Object((1,3,6,1,4,1,890,1,15,3,26,3,1),_ZyHwMonitorTrapPowerSourceErrorType_Type())
zyHwMonitorTrapPowerSourceErrorType.setMaxAccess(_D)
if mibBuilder.loadTexts:zyHwMonitorTrapPowerSourceErrorType.setStatus(_A)
zyHwMonitorFanSpeedOutOfRange=NotificationType((1,3,6,1,4,1,890,1,15,3,26,2,1))
zyHwMonitorFanSpeedOutOfRange.setObjects(*((_B,_F),(_B,_K)))
if mibBuilder.loadTexts:zyHwMonitorFanSpeedOutOfRange.setStatus(_A)
zyHwMonitorTemperatureOutOfRange=NotificationType((1,3,6,1,4,1,890,1,15,3,26,2,2))
zyHwMonitorTemperatureOutOfRange.setObjects(*((_B,_G),(_B,_L)))
if mibBuilder.loadTexts:zyHwMonitorTemperatureOutOfRange.setStatus(_A)
zyHwMonitorPowerSupplyVoltageOutOfRange=NotificationType((1,3,6,1,4,1,890,1,15,3,26,2,3))
zyHwMonitorPowerSupplyVoltageOutOfRange.setObjects(*((_B,_H),(_B,_M)))
if mibBuilder.loadTexts:zyHwMonitorPowerSupplyVoltageOutOfRange.setStatus(_A)
zyHwMonitorBackupPowerSupplyInUse=NotificationType((1,3,6,1,4,1,890,1,15,3,26,2,4))
if mibBuilder.loadTexts:zyHwMonitorBackupPowerSupplyInUse.setStatus(_A)
zyHwMonitorDyingGasp=NotificationType((1,3,6,1,4,1,890,1,15,3,26,2,5))
if mibBuilder.loadTexts:zyHwMonitorDyingGasp.setStatus(_A)
zyHwMonitorFanAirFlowInconsistency=NotificationType((1,3,6,1,4,1,890,1,15,3,26,2,6))
if mibBuilder.loadTexts:zyHwMonitorFanAirFlowInconsistency.setStatus(_A)
zyHwMonitorFanSpeedOutOfRangeRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,26,2,7))
zyHwMonitorFanSpeedOutOfRangeRecovered.setObjects(*((_B,_F),(_B,_K)))
if mibBuilder.loadTexts:zyHwMonitorFanSpeedOutOfRangeRecovered.setStatus(_A)
zyHwMonitorTemperatureOutOfRangeRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,26,2,8))
zyHwMonitorTemperatureOutOfRangeRecovered.setObjects(*((_B,_G),(_B,_L)))
if mibBuilder.loadTexts:zyHwMonitorTemperatureOutOfRangeRecovered.setStatus(_A)
zyHwMonitorPowerSupplyVoltageOutOfRangeRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,26,2,9))
zyHwMonitorPowerSupplyVoltageOutOfRangeRecovered.setObjects(*((_B,_H),(_B,_M)))
if mibBuilder.loadTexts:zyHwMonitorPowerSupplyVoltageOutOfRangeRecovered.setStatus(_A)
zyHwMonitorPowerSourceAbnormal=NotificationType((1,3,6,1,4,1,890,1,15,3,26,2,10))
zyHwMonitorPowerSourceAbnormal.setObjects(*((_B,_E),(_B,_I),(_B,_J),(_B,_N)))
if mibBuilder.loadTexts:zyHwMonitorPowerSourceAbnormal.setStatus(_A)
zyHwMonitorPowerSourceAbnormalRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,26,2,11))
zyHwMonitorPowerSourceAbnormalRecovered.setObjects(*((_B,_E),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:zyHwMonitorPowerSourceAbnormalRecovered.setStatus(_A)
zyHwMonitorPowerSourceStatusChange=NotificationType((1,3,6,1,4,1,890,1,15,3,26,2,12))
zyHwMonitorPowerSourceStatusChange.setObjects(*((_B,_E),(_B,_O),(_B,_I),(_B,_J),(_B,_N)))
if mibBuilder.loadTexts:zyHwMonitorPowerSourceStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zyxelHwMonitor':zyxelHwMonitor,'zyxelHwMonitorStatus':zyxelHwMonitorStatus,'zyxelHwMonitorFanRpmTable':zyxelHwMonitorFanRpmTable,'zyxelHwMonitorFanRpmEntry':zyxelHwMonitorFanRpmEntry,_F:zyHwMonitorFanRpmIndex,_K:zyHwMonitorFanRpmDescription,'zyHwMonitorFanRpmCurrentValue':zyHwMonitorFanRpmCurrentValue,'zyHwMonitorFanRpmMaxValue':zyHwMonitorFanRpmMaxValue,'zyHwMonitorFanRpmMinValue':zyHwMonitorFanRpmMinValue,'zyHwMonitorFanRpmLowThreshold':zyHwMonitorFanRpmLowThreshold,'zyHwMonitorFanRpmStatus':zyHwMonitorFanRpmStatus,'zyxelHwMonitorTemperatureTable':zyxelHwMonitorTemperatureTable,'zyxelHwMonitorTemperatureEntry':zyxelHwMonitorTemperatureEntry,_G:zyHwMonitorTemperatureIndex,_L:zyHwMonitorTemperatureDescription,'zyHwMonitorTemperatureCurrentValue':zyHwMonitorTemperatureCurrentValue,'zyHwMonitorTemperatureMaxValue':zyHwMonitorTemperatureMaxValue,'zyHwMonitorTemperatureMinValue':zyHwMonitorTemperatureMinValue,'zyHwMonitorTemperatureHighThreshold':zyHwMonitorTemperatureHighThreshold,'zyHwMonitorTemperatureStatus':zyHwMonitorTemperatureStatus,'zyxelHwMonitorVoltageTable':zyxelHwMonitorVoltageTable,'zyxelHwMonitorVoltageEntry':zyxelHwMonitorVoltageEntry,_H:zyHwMonitorVoltageIndex,_M:zyHwMonitorVoltageDescription,'zyHwMonitorVoltageCurrentValue':zyHwMonitorVoltageCurrentValue,'zyHwMonitorVoltageMaxValue':zyHwMonitorVoltageMaxValue,'zyHwMonitorVoltageMinValue':zyHwMonitorVoltageMinValue,'zyHwMonitorVoltageNominalValue':zyHwMonitorVoltageNominalValue,'zyHwMonitorVoltageLowThreshold':zyHwMonitorVoltageLowThreshold,'zyHwMonitorVoltageStatus':zyHwMonitorVoltageStatus,'zyxelHwMonitorPowerSource':zyxelHwMonitorPowerSource,'zyHwMonitorPowerSourceMode':zyHwMonitorPowerSourceMode,'zyxelHwMonitorPowerSourceTable':zyxelHwMonitorPowerSourceTable,'zyxelHwMonitorPowerSourceEntry':zyxelHwMonitorPowerSourceEntry,_E:zyHwMonitorPowerSourceIndex,'zyHwMonitorPowerSourceType':zyHwMonitorPowerSourceType,_I:zyHwMonitorPowerSourceStatus,_J:zyHwMonitorPowerSourceDescription,_O:zyHwMonitorPowerSourcePreviousStatus,'zyxelHwMonitorNotifications':zyxelHwMonitorNotifications,'zyHwMonitorFanSpeedOutOfRange':zyHwMonitorFanSpeedOutOfRange,'zyHwMonitorTemperatureOutOfRange':zyHwMonitorTemperatureOutOfRange,'zyHwMonitorPowerSupplyVoltageOutOfRange':zyHwMonitorPowerSupplyVoltageOutOfRange,'zyHwMonitorBackupPowerSupplyInUse':zyHwMonitorBackupPowerSupplyInUse,'zyHwMonitorDyingGasp':zyHwMonitorDyingGasp,'zyHwMonitorFanAirFlowInconsistency':zyHwMonitorFanAirFlowInconsistency,'zyHwMonitorFanSpeedOutOfRangeRecovered':zyHwMonitorFanSpeedOutOfRangeRecovered,'zyHwMonitorTemperatureOutOfRangeRecovered':zyHwMonitorTemperatureOutOfRangeRecovered,'zyHwMonitorPowerSupplyVoltageOutOfRangeRecovered':zyHwMonitorPowerSupplyVoltageOutOfRangeRecovered,'zyHwMonitorPowerSourceAbnormal':zyHwMonitorPowerSourceAbnormal,'zyHwMonitorPowerSourceAbnormalRecovered':zyHwMonitorPowerSourceAbnormalRecovered,'zyHwMonitorPowerSourceStatusChange':zyHwMonitorPowerSourceStatusChange,'zyxelHwMonitorTrapInfoObject':zyxelHwMonitorTrapInfoObject,_N:zyHwMonitorTrapPowerSourceErrorType})