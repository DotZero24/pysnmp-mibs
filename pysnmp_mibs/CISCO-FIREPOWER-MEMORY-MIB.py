_Q='cfprMemoryUnitEnvStatsHistInstanceId'
_P='cfprMemoryUnitEnvStatsInstanceId'
_O='cfprMemoryUnitInstanceId'
_N='cfprMemoryRuntimeHistInstanceId'
_M='cfprMemoryRuntimeInstanceId'
_L='cfprMemoryQualInstanceId'
_K='cfprMemoryErrorStatsInstanceId'
_J='cfprMemoryBufferUnitEnvStatsHistInstanceId'
_I='cfprMemoryBufferUnitEnvStatsInstanceId'
_H='cfprMemoryBufferUnitInstanceId'
_G='cfprMemoryArrayEnvStatsHistInstanceId'
_F='cfprMemoryArrayEnvStatsInstanceId'
_E='cfprMemoryArrayInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-MEMORY-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprEquipmentOperability,CfprEquipmentPowerState,CfprEquipmentPresence,CfprEquipmentSensorThresholdStatus,CfprMemoryAdminState,CfprMemoryArrayEnvStatsHistThresholded,CfprMemoryArrayEnvStatsThresholded,CfprMemoryArrayId,CfprMemoryBufferUnitEnvStatsHistThresholded,CfprMemoryBufferUnitEnvStatsThresholded,CfprMemoryBufferUnitId,CfprMemoryErrorCorrection,CfprMemoryErrorStatsThresholded,CfprMemoryFormFactor,CfprMemoryIssues,CfprMemoryRuntimeHistThresholded,CfprMemoryRuntimeThresholded,CfprMemoryRuntimeType,CfprMemoryType,CfprMemoryUnitEnvStatsHistThresholded,CfprMemoryUnitEnvStatsThresholded,CfprMemoryUnitId,CfprMemoryUnitOperability,CfprMemoryVisibility=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprEquipmentOperability','CfprEquipmentPowerState','CfprEquipmentPresence','CfprEquipmentSensorThresholdStatus','CfprMemoryAdminState','CfprMemoryArrayEnvStatsHistThresholded','CfprMemoryArrayEnvStatsThresholded','CfprMemoryArrayId','CfprMemoryBufferUnitEnvStatsHistThresholded','CfprMemoryBufferUnitEnvStatsThresholded','CfprMemoryBufferUnitId','CfprMemoryErrorCorrection','CfprMemoryErrorStatsThresholded','CfprMemoryFormFactor','CfprMemoryIssues','CfprMemoryRuntimeHistThresholded','CfprMemoryRuntimeThresholded','CfprMemoryRuntimeType','CfprMemoryType','CfprMemoryUnitEnvStatsHistThresholded','CfprMemoryUnitEnvStatsThresholded','CfprMemoryUnitId','CfprMemoryUnitOperability','CfprMemoryVisibility')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprMemoryObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,50))
_CfprMemoryArrayTable_Object=MibTable
cfprMemoryArrayTable=_CfprMemoryArrayTable_Object((1,3,6,1,4,1,9,9,826,1,50,1))
if mibBuilder.loadTexts:cfprMemoryArrayTable.setStatus(_A)
_CfprMemoryArrayEntry_Object=MibTableRow
cfprMemoryArrayEntry=_CfprMemoryArrayEntry_Object((1,3,6,1,4,1,9,9,826,1,50,1,1))
cfprMemoryArrayEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprMemoryArrayEntry.setStatus(_A)
_CfprMemoryArrayInstanceId_Type=CfprManagedObjectId
_CfprMemoryArrayInstanceId_Object=MibTableColumn
cfprMemoryArrayInstanceId=_CfprMemoryArrayInstanceId_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,1),_CfprMemoryArrayInstanceId_Type())
cfprMemoryArrayInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMemoryArrayInstanceId.setStatus(_A)
_CfprMemoryArrayDn_Type=CfprManagedObjectDn
_CfprMemoryArrayDn_Object=MibTableColumn
cfprMemoryArrayDn=_CfprMemoryArrayDn_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,2),_CfprMemoryArrayDn_Type())
cfprMemoryArrayDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayDn.setStatus(_A)
_CfprMemoryArrayRn_Type=SnmpAdminString
_CfprMemoryArrayRn_Object=MibTableColumn
cfprMemoryArrayRn=_CfprMemoryArrayRn_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,3),_CfprMemoryArrayRn_Type())
cfprMemoryArrayRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayRn.setStatus(_A)
_CfprMemoryArrayCpuId_Type=Gauge32
_CfprMemoryArrayCpuId_Object=MibTableColumn
cfprMemoryArrayCpuId=_CfprMemoryArrayCpuId_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,4),_CfprMemoryArrayCpuId_Type())
cfprMemoryArrayCpuId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayCpuId.setStatus(_A)
_CfprMemoryArrayCurrCapacity_Type=Gauge32
_CfprMemoryArrayCurrCapacity_Object=MibTableColumn
cfprMemoryArrayCurrCapacity=_CfprMemoryArrayCurrCapacity_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,5),_CfprMemoryArrayCurrCapacity_Type())
cfprMemoryArrayCurrCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayCurrCapacity.setStatus(_A)
_CfprMemoryArrayErrorCorrection_Type=CfprMemoryErrorCorrection
_CfprMemoryArrayErrorCorrection_Object=MibTableColumn
cfprMemoryArrayErrorCorrection=_CfprMemoryArrayErrorCorrection_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,6),_CfprMemoryArrayErrorCorrection_Type())
cfprMemoryArrayErrorCorrection.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayErrorCorrection.setStatus(_A)
_CfprMemoryArrayId_Type=CfprMemoryArrayId
_CfprMemoryArrayId_Object=MibTableColumn
cfprMemoryArrayId=_CfprMemoryArrayId_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,7),_CfprMemoryArrayId_Type())
cfprMemoryArrayId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayId.setStatus(_A)
_CfprMemoryArrayLocationDn_Type=SnmpAdminString
_CfprMemoryArrayLocationDn_Object=MibTableColumn
cfprMemoryArrayLocationDn=_CfprMemoryArrayLocationDn_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,8),_CfprMemoryArrayLocationDn_Type())
cfprMemoryArrayLocationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayLocationDn.setStatus(_A)
_CfprMemoryArrayMaxCapacity_Type=Gauge32
_CfprMemoryArrayMaxCapacity_Object=MibTableColumn
cfprMemoryArrayMaxCapacity=_CfprMemoryArrayMaxCapacity_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,9),_CfprMemoryArrayMaxCapacity_Type())
cfprMemoryArrayMaxCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayMaxCapacity.setStatus(_A)
_CfprMemoryArrayMaxDevices_Type=Gauge32
_CfprMemoryArrayMaxDevices_Object=MibTableColumn
cfprMemoryArrayMaxDevices=_CfprMemoryArrayMaxDevices_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,10),_CfprMemoryArrayMaxDevices_Type())
cfprMemoryArrayMaxDevices.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayMaxDevices.setStatus(_A)
_CfprMemoryArrayModel_Type=SnmpAdminString
_CfprMemoryArrayModel_Object=MibTableColumn
cfprMemoryArrayModel=_CfprMemoryArrayModel_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,11),_CfprMemoryArrayModel_Type())
cfprMemoryArrayModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayModel.setStatus(_A)
_CfprMemoryArrayOperQualifierReason_Type=SnmpAdminString
_CfprMemoryArrayOperQualifierReason_Object=MibTableColumn
cfprMemoryArrayOperQualifierReason=_CfprMemoryArrayOperQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,12),_CfprMemoryArrayOperQualifierReason_Type())
cfprMemoryArrayOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayOperQualifierReason.setStatus(_A)
_CfprMemoryArrayOperState_Type=CfprEquipmentOperability
_CfprMemoryArrayOperState_Object=MibTableColumn
cfprMemoryArrayOperState=_CfprMemoryArrayOperState_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,13),_CfprMemoryArrayOperState_Type())
cfprMemoryArrayOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayOperState.setStatus(_A)
_CfprMemoryArrayOperability_Type=CfprEquipmentOperability
_CfprMemoryArrayOperability_Object=MibTableColumn
cfprMemoryArrayOperability=_CfprMemoryArrayOperability_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,14),_CfprMemoryArrayOperability_Type())
cfprMemoryArrayOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayOperability.setStatus(_A)
_CfprMemoryArrayPerf_Type=CfprEquipmentSensorThresholdStatus
_CfprMemoryArrayPerf_Object=MibTableColumn
cfprMemoryArrayPerf=_CfprMemoryArrayPerf_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,15),_CfprMemoryArrayPerf_Type())
cfprMemoryArrayPerf.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayPerf.setStatus(_A)
_CfprMemoryArrayPopulated_Type=Gauge32
_CfprMemoryArrayPopulated_Object=MibTableColumn
cfprMemoryArrayPopulated=_CfprMemoryArrayPopulated_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,16),_CfprMemoryArrayPopulated_Type())
cfprMemoryArrayPopulated.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayPopulated.setStatus(_A)
_CfprMemoryArrayPower_Type=CfprEquipmentPowerState
_CfprMemoryArrayPower_Object=MibTableColumn
cfprMemoryArrayPower=_CfprMemoryArrayPower_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,17),_CfprMemoryArrayPower_Type())
cfprMemoryArrayPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayPower.setStatus(_A)
_CfprMemoryArrayPresence_Type=CfprEquipmentPresence
_CfprMemoryArrayPresence_Object=MibTableColumn
cfprMemoryArrayPresence=_CfprMemoryArrayPresence_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,18),_CfprMemoryArrayPresence_Type())
cfprMemoryArrayPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayPresence.setStatus(_A)
_CfprMemoryArrayRevision_Type=SnmpAdminString
_CfprMemoryArrayRevision_Object=MibTableColumn
cfprMemoryArrayRevision=_CfprMemoryArrayRevision_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,19),_CfprMemoryArrayRevision_Type())
cfprMemoryArrayRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayRevision.setStatus(_A)
_CfprMemoryArraySerial_Type=SnmpAdminString
_CfprMemoryArraySerial_Object=MibTableColumn
cfprMemoryArraySerial=_CfprMemoryArraySerial_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,20),_CfprMemoryArraySerial_Type())
cfprMemoryArraySerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArraySerial.setStatus(_A)
_CfprMemoryArrayThermal_Type=CfprEquipmentSensorThresholdStatus
_CfprMemoryArrayThermal_Object=MibTableColumn
cfprMemoryArrayThermal=_CfprMemoryArrayThermal_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,21),_CfprMemoryArrayThermal_Type())
cfprMemoryArrayThermal.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayThermal.setStatus(_A)
_CfprMemoryArrayVendor_Type=SnmpAdminString
_CfprMemoryArrayVendor_Object=MibTableColumn
cfprMemoryArrayVendor=_CfprMemoryArrayVendor_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,22),_CfprMemoryArrayVendor_Type())
cfprMemoryArrayVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayVendor.setStatus(_A)
_CfprMemoryArrayVoltage_Type=CfprEquipmentSensorThresholdStatus
_CfprMemoryArrayVoltage_Object=MibTableColumn
cfprMemoryArrayVoltage=_CfprMemoryArrayVoltage_Object((1,3,6,1,4,1,9,9,826,1,50,1,1,23),_CfprMemoryArrayVoltage_Type())
cfprMemoryArrayVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayVoltage.setStatus(_A)
_CfprMemoryArrayEnvStatsTable_Object=MibTable
cfprMemoryArrayEnvStatsTable=_CfprMemoryArrayEnvStatsTable_Object((1,3,6,1,4,1,9,9,826,1,50,2))
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsTable.setStatus(_A)
_CfprMemoryArrayEnvStatsEntry_Object=MibTableRow
cfprMemoryArrayEnvStatsEntry=_CfprMemoryArrayEnvStatsEntry_Object((1,3,6,1,4,1,9,9,826,1,50,2,1))
cfprMemoryArrayEnvStatsEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsEntry.setStatus(_A)
_CfprMemoryArrayEnvStatsInstanceId_Type=CfprManagedObjectId
_CfprMemoryArrayEnvStatsInstanceId_Object=MibTableColumn
cfprMemoryArrayEnvStatsInstanceId=_CfprMemoryArrayEnvStatsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,50,2,1,1),_CfprMemoryArrayEnvStatsInstanceId_Type())
cfprMemoryArrayEnvStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsInstanceId.setStatus(_A)
_CfprMemoryArrayEnvStatsDn_Type=CfprManagedObjectDn
_CfprMemoryArrayEnvStatsDn_Object=MibTableColumn
cfprMemoryArrayEnvStatsDn=_CfprMemoryArrayEnvStatsDn_Object((1,3,6,1,4,1,9,9,826,1,50,2,1,2),_CfprMemoryArrayEnvStatsDn_Type())
cfprMemoryArrayEnvStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsDn.setStatus(_A)
_CfprMemoryArrayEnvStatsRn_Type=SnmpAdminString
_CfprMemoryArrayEnvStatsRn_Object=MibTableColumn
cfprMemoryArrayEnvStatsRn=_CfprMemoryArrayEnvStatsRn_Object((1,3,6,1,4,1,9,9,826,1,50,2,1,3),_CfprMemoryArrayEnvStatsRn_Type())
cfprMemoryArrayEnvStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsRn.setStatus(_A)
_CfprMemoryArrayEnvStatsInputCurrent_Type=Integer32
_CfprMemoryArrayEnvStatsInputCurrent_Object=MibTableColumn
cfprMemoryArrayEnvStatsInputCurrent=_CfprMemoryArrayEnvStatsInputCurrent_Object((1,3,6,1,4,1,9,9,826,1,50,2,1,4),_CfprMemoryArrayEnvStatsInputCurrent_Type())
cfprMemoryArrayEnvStatsInputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsInputCurrent.setStatus(_A)
_CfprMemoryArrayEnvStatsInputCurrentAvg_Type=Integer32
_CfprMemoryArrayEnvStatsInputCurrentAvg_Object=MibTableColumn
cfprMemoryArrayEnvStatsInputCurrentAvg=_CfprMemoryArrayEnvStatsInputCurrentAvg_Object((1,3,6,1,4,1,9,9,826,1,50,2,1,5),_CfprMemoryArrayEnvStatsInputCurrentAvg_Type())
cfprMemoryArrayEnvStatsInputCurrentAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsInputCurrentAvg.setStatus(_A)
_CfprMemoryArrayEnvStatsInputCurrentMax_Type=Integer32
_CfprMemoryArrayEnvStatsInputCurrentMax_Object=MibTableColumn
cfprMemoryArrayEnvStatsInputCurrentMax=_CfprMemoryArrayEnvStatsInputCurrentMax_Object((1,3,6,1,4,1,9,9,826,1,50,2,1,6),_CfprMemoryArrayEnvStatsInputCurrentMax_Type())
cfprMemoryArrayEnvStatsInputCurrentMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsInputCurrentMax.setStatus(_A)
_CfprMemoryArrayEnvStatsInputCurrentMin_Type=Integer32
_CfprMemoryArrayEnvStatsInputCurrentMin_Object=MibTableColumn
cfprMemoryArrayEnvStatsInputCurrentMin=_CfprMemoryArrayEnvStatsInputCurrentMin_Object((1,3,6,1,4,1,9,9,826,1,50,2,1,7),_CfprMemoryArrayEnvStatsInputCurrentMin_Type())
cfprMemoryArrayEnvStatsInputCurrentMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsInputCurrentMin.setStatus(_A)
_CfprMemoryArrayEnvStatsIntervals_Type=Gauge32
_CfprMemoryArrayEnvStatsIntervals_Object=MibTableColumn
cfprMemoryArrayEnvStatsIntervals=_CfprMemoryArrayEnvStatsIntervals_Object((1,3,6,1,4,1,9,9,826,1,50,2,1,8),_CfprMemoryArrayEnvStatsIntervals_Type())
cfprMemoryArrayEnvStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsIntervals.setStatus(_A)
_CfprMemoryArrayEnvStatsSuspect_Type=TruthValue
_CfprMemoryArrayEnvStatsSuspect_Object=MibTableColumn
cfprMemoryArrayEnvStatsSuspect=_CfprMemoryArrayEnvStatsSuspect_Object((1,3,6,1,4,1,9,9,826,1,50,2,1,9),_CfprMemoryArrayEnvStatsSuspect_Type())
cfprMemoryArrayEnvStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsSuspect.setStatus(_A)
_CfprMemoryArrayEnvStatsThresholded_Type=CfprMemoryArrayEnvStatsThresholded
_CfprMemoryArrayEnvStatsThresholded_Object=MibTableColumn
cfprMemoryArrayEnvStatsThresholded=_CfprMemoryArrayEnvStatsThresholded_Object((1,3,6,1,4,1,9,9,826,1,50,2,1,10),_CfprMemoryArrayEnvStatsThresholded_Type())
cfprMemoryArrayEnvStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsThresholded.setStatus(_A)
_CfprMemoryArrayEnvStatsTimeCollected_Type=DateAndTime
_CfprMemoryArrayEnvStatsTimeCollected_Object=MibTableColumn
cfprMemoryArrayEnvStatsTimeCollected=_CfprMemoryArrayEnvStatsTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,50,2,1,11),_CfprMemoryArrayEnvStatsTimeCollected_Type())
cfprMemoryArrayEnvStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsTimeCollected.setStatus(_A)
_CfprMemoryArrayEnvStatsUpdate_Type=Gauge32
_CfprMemoryArrayEnvStatsUpdate_Object=MibTableColumn
cfprMemoryArrayEnvStatsUpdate=_CfprMemoryArrayEnvStatsUpdate_Object((1,3,6,1,4,1,9,9,826,1,50,2,1,12),_CfprMemoryArrayEnvStatsUpdate_Type())
cfprMemoryArrayEnvStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsUpdate.setStatus(_A)
_CfprMemoryArrayEnvStatsHistTable_Object=MibTable
cfprMemoryArrayEnvStatsHistTable=_CfprMemoryArrayEnvStatsHistTable_Object((1,3,6,1,4,1,9,9,826,1,50,3))
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsHistTable.setStatus(_A)
_CfprMemoryArrayEnvStatsHistEntry_Object=MibTableRow
cfprMemoryArrayEnvStatsHistEntry=_CfprMemoryArrayEnvStatsHistEntry_Object((1,3,6,1,4,1,9,9,826,1,50,3,1))
cfprMemoryArrayEnvStatsHistEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsHistEntry.setStatus(_A)
_CfprMemoryArrayEnvStatsHistInstanceId_Type=CfprManagedObjectId
_CfprMemoryArrayEnvStatsHistInstanceId_Object=MibTableColumn
cfprMemoryArrayEnvStatsHistInstanceId=_CfprMemoryArrayEnvStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,826,1,50,3,1,1),_CfprMemoryArrayEnvStatsHistInstanceId_Type())
cfprMemoryArrayEnvStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsHistInstanceId.setStatus(_A)
_CfprMemoryArrayEnvStatsHistDn_Type=CfprManagedObjectDn
_CfprMemoryArrayEnvStatsHistDn_Object=MibTableColumn
cfprMemoryArrayEnvStatsHistDn=_CfprMemoryArrayEnvStatsHistDn_Object((1,3,6,1,4,1,9,9,826,1,50,3,1,2),_CfprMemoryArrayEnvStatsHistDn_Type())
cfprMemoryArrayEnvStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsHistDn.setStatus(_A)
_CfprMemoryArrayEnvStatsHistRn_Type=SnmpAdminString
_CfprMemoryArrayEnvStatsHistRn_Object=MibTableColumn
cfprMemoryArrayEnvStatsHistRn=_CfprMemoryArrayEnvStatsHistRn_Object((1,3,6,1,4,1,9,9,826,1,50,3,1,3),_CfprMemoryArrayEnvStatsHistRn_Type())
cfprMemoryArrayEnvStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsHistRn.setStatus(_A)
_CfprMemoryArrayEnvStatsHistId_Type=Unsigned64
_CfprMemoryArrayEnvStatsHistId_Object=MibTableColumn
cfprMemoryArrayEnvStatsHistId=_CfprMemoryArrayEnvStatsHistId_Object((1,3,6,1,4,1,9,9,826,1,50,3,1,4),_CfprMemoryArrayEnvStatsHistId_Type())
cfprMemoryArrayEnvStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsHistId.setStatus(_A)
_CfprMemoryArrayEnvStatsHistInputCurrent_Type=Integer32
_CfprMemoryArrayEnvStatsHistInputCurrent_Object=MibTableColumn
cfprMemoryArrayEnvStatsHistInputCurrent=_CfprMemoryArrayEnvStatsHistInputCurrent_Object((1,3,6,1,4,1,9,9,826,1,50,3,1,5),_CfprMemoryArrayEnvStatsHistInputCurrent_Type())
cfprMemoryArrayEnvStatsHistInputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsHistInputCurrent.setStatus(_A)
_CfprMemoryArrayEnvStatsHistInputCurrentAvg_Type=Integer32
_CfprMemoryArrayEnvStatsHistInputCurrentAvg_Object=MibTableColumn
cfprMemoryArrayEnvStatsHistInputCurrentAvg=_CfprMemoryArrayEnvStatsHistInputCurrentAvg_Object((1,3,6,1,4,1,9,9,826,1,50,3,1,6),_CfprMemoryArrayEnvStatsHistInputCurrentAvg_Type())
cfprMemoryArrayEnvStatsHistInputCurrentAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsHistInputCurrentAvg.setStatus(_A)
_CfprMemoryArrayEnvStatsHistInputCurrentMax_Type=Integer32
_CfprMemoryArrayEnvStatsHistInputCurrentMax_Object=MibTableColumn
cfprMemoryArrayEnvStatsHistInputCurrentMax=_CfprMemoryArrayEnvStatsHistInputCurrentMax_Object((1,3,6,1,4,1,9,9,826,1,50,3,1,7),_CfprMemoryArrayEnvStatsHistInputCurrentMax_Type())
cfprMemoryArrayEnvStatsHistInputCurrentMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsHistInputCurrentMax.setStatus(_A)
_CfprMemoryArrayEnvStatsHistInputCurrentMin_Type=Integer32
_CfprMemoryArrayEnvStatsHistInputCurrentMin_Object=MibTableColumn
cfprMemoryArrayEnvStatsHistInputCurrentMin=_CfprMemoryArrayEnvStatsHistInputCurrentMin_Object((1,3,6,1,4,1,9,9,826,1,50,3,1,8),_CfprMemoryArrayEnvStatsHistInputCurrentMin_Type())
cfprMemoryArrayEnvStatsHistInputCurrentMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsHistInputCurrentMin.setStatus(_A)
_CfprMemoryArrayEnvStatsHistMostRecent_Type=TruthValue
_CfprMemoryArrayEnvStatsHistMostRecent_Object=MibTableColumn
cfprMemoryArrayEnvStatsHistMostRecent=_CfprMemoryArrayEnvStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,826,1,50,3,1,9),_CfprMemoryArrayEnvStatsHistMostRecent_Type())
cfprMemoryArrayEnvStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsHistMostRecent.setStatus(_A)
_CfprMemoryArrayEnvStatsHistSuspect_Type=TruthValue
_CfprMemoryArrayEnvStatsHistSuspect_Object=MibTableColumn
cfprMemoryArrayEnvStatsHistSuspect=_CfprMemoryArrayEnvStatsHistSuspect_Object((1,3,6,1,4,1,9,9,826,1,50,3,1,10),_CfprMemoryArrayEnvStatsHistSuspect_Type())
cfprMemoryArrayEnvStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsHistSuspect.setStatus(_A)
_CfprMemoryArrayEnvStatsHistThresholded_Type=CfprMemoryArrayEnvStatsHistThresholded
_CfprMemoryArrayEnvStatsHistThresholded_Object=MibTableColumn
cfprMemoryArrayEnvStatsHistThresholded=_CfprMemoryArrayEnvStatsHistThresholded_Object((1,3,6,1,4,1,9,9,826,1,50,3,1,11),_CfprMemoryArrayEnvStatsHistThresholded_Type())
cfprMemoryArrayEnvStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsHistThresholded.setStatus(_A)
_CfprMemoryArrayEnvStatsHistTimeCollected_Type=DateAndTime
_CfprMemoryArrayEnvStatsHistTimeCollected_Object=MibTableColumn
cfprMemoryArrayEnvStatsHistTimeCollected=_CfprMemoryArrayEnvStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,50,3,1,12),_CfprMemoryArrayEnvStatsHistTimeCollected_Type())
cfprMemoryArrayEnvStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryArrayEnvStatsHistTimeCollected.setStatus(_A)
_CfprMemoryBufferUnitTable_Object=MibTable
cfprMemoryBufferUnitTable=_CfprMemoryBufferUnitTable_Object((1,3,6,1,4,1,9,9,826,1,50,4))
if mibBuilder.loadTexts:cfprMemoryBufferUnitTable.setStatus(_A)
_CfprMemoryBufferUnitEntry_Object=MibTableRow
cfprMemoryBufferUnitEntry=_CfprMemoryBufferUnitEntry_Object((1,3,6,1,4,1,9,9,826,1,50,4,1))
cfprMemoryBufferUnitEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprMemoryBufferUnitEntry.setStatus(_A)
_CfprMemoryBufferUnitInstanceId_Type=CfprManagedObjectId
_CfprMemoryBufferUnitInstanceId_Object=MibTableColumn
cfprMemoryBufferUnitInstanceId=_CfprMemoryBufferUnitInstanceId_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,1),_CfprMemoryBufferUnitInstanceId_Type())
cfprMemoryBufferUnitInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMemoryBufferUnitInstanceId.setStatus(_A)
_CfprMemoryBufferUnitDn_Type=CfprManagedObjectDn
_CfprMemoryBufferUnitDn_Object=MibTableColumn
cfprMemoryBufferUnitDn=_CfprMemoryBufferUnitDn_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,2),_CfprMemoryBufferUnitDn_Type())
cfprMemoryBufferUnitDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitDn.setStatus(_A)
_CfprMemoryBufferUnitRn_Type=SnmpAdminString
_CfprMemoryBufferUnitRn_Object=MibTableColumn
cfprMemoryBufferUnitRn=_CfprMemoryBufferUnitRn_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,3),_CfprMemoryBufferUnitRn_Type())
cfprMemoryBufferUnitRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitRn.setStatus(_A)
_CfprMemoryBufferUnitId_Type=CfprMemoryBufferUnitId
_CfprMemoryBufferUnitId_Object=MibTableColumn
cfprMemoryBufferUnitId=_CfprMemoryBufferUnitId_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,4),_CfprMemoryBufferUnitId_Type())
cfprMemoryBufferUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitId.setStatus(_A)
_CfprMemoryBufferUnitLocationDn_Type=SnmpAdminString
_CfprMemoryBufferUnitLocationDn_Object=MibTableColumn
cfprMemoryBufferUnitLocationDn=_CfprMemoryBufferUnitLocationDn_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,5),_CfprMemoryBufferUnitLocationDn_Type())
cfprMemoryBufferUnitLocationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitLocationDn.setStatus(_A)
_CfprMemoryBufferUnitModel_Type=SnmpAdminString
_CfprMemoryBufferUnitModel_Object=MibTableColumn
cfprMemoryBufferUnitModel=_CfprMemoryBufferUnitModel_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,6),_CfprMemoryBufferUnitModel_Type())
cfprMemoryBufferUnitModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitModel.setStatus(_A)
_CfprMemoryBufferUnitOperQualifierReason_Type=SnmpAdminString
_CfprMemoryBufferUnitOperQualifierReason_Object=MibTableColumn
cfprMemoryBufferUnitOperQualifierReason=_CfprMemoryBufferUnitOperQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,7),_CfprMemoryBufferUnitOperQualifierReason_Type())
cfprMemoryBufferUnitOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitOperQualifierReason.setStatus(_A)
_CfprMemoryBufferUnitOperState_Type=CfprEquipmentOperability
_CfprMemoryBufferUnitOperState_Object=MibTableColumn
cfprMemoryBufferUnitOperState=_CfprMemoryBufferUnitOperState_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,8),_CfprMemoryBufferUnitOperState_Type())
cfprMemoryBufferUnitOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitOperState.setStatus(_A)
_CfprMemoryBufferUnitOperability_Type=CfprEquipmentOperability
_CfprMemoryBufferUnitOperability_Object=MibTableColumn
cfprMemoryBufferUnitOperability=_CfprMemoryBufferUnitOperability_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,9),_CfprMemoryBufferUnitOperability_Type())
cfprMemoryBufferUnitOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitOperability.setStatus(_A)
_CfprMemoryBufferUnitPerf_Type=CfprEquipmentSensorThresholdStatus
_CfprMemoryBufferUnitPerf_Object=MibTableColumn
cfprMemoryBufferUnitPerf=_CfprMemoryBufferUnitPerf_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,10),_CfprMemoryBufferUnitPerf_Type())
cfprMemoryBufferUnitPerf.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitPerf.setStatus(_A)
_CfprMemoryBufferUnitPower_Type=CfprEquipmentPowerState
_CfprMemoryBufferUnitPower_Object=MibTableColumn
cfprMemoryBufferUnitPower=_CfprMemoryBufferUnitPower_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,11),_CfprMemoryBufferUnitPower_Type())
cfprMemoryBufferUnitPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitPower.setStatus(_A)
_CfprMemoryBufferUnitPresence_Type=CfprEquipmentPresence
_CfprMemoryBufferUnitPresence_Object=MibTableColumn
cfprMemoryBufferUnitPresence=_CfprMemoryBufferUnitPresence_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,12),_CfprMemoryBufferUnitPresence_Type())
cfprMemoryBufferUnitPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitPresence.setStatus(_A)
_CfprMemoryBufferUnitRevision_Type=SnmpAdminString
_CfprMemoryBufferUnitRevision_Object=MibTableColumn
cfprMemoryBufferUnitRevision=_CfprMemoryBufferUnitRevision_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,13),_CfprMemoryBufferUnitRevision_Type())
cfprMemoryBufferUnitRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitRevision.setStatus(_A)
_CfprMemoryBufferUnitSerial_Type=SnmpAdminString
_CfprMemoryBufferUnitSerial_Object=MibTableColumn
cfprMemoryBufferUnitSerial=_CfprMemoryBufferUnitSerial_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,14),_CfprMemoryBufferUnitSerial_Type())
cfprMemoryBufferUnitSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitSerial.setStatus(_A)
_CfprMemoryBufferUnitThermal_Type=CfprEquipmentSensorThresholdStatus
_CfprMemoryBufferUnitThermal_Object=MibTableColumn
cfprMemoryBufferUnitThermal=_CfprMemoryBufferUnitThermal_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,15),_CfprMemoryBufferUnitThermal_Type())
cfprMemoryBufferUnitThermal.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitThermal.setStatus(_A)
_CfprMemoryBufferUnitVendor_Type=SnmpAdminString
_CfprMemoryBufferUnitVendor_Object=MibTableColumn
cfprMemoryBufferUnitVendor=_CfprMemoryBufferUnitVendor_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,16),_CfprMemoryBufferUnitVendor_Type())
cfprMemoryBufferUnitVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitVendor.setStatus(_A)
_CfprMemoryBufferUnitVoltage_Type=CfprEquipmentSensorThresholdStatus
_CfprMemoryBufferUnitVoltage_Object=MibTableColumn
cfprMemoryBufferUnitVoltage=_CfprMemoryBufferUnitVoltage_Object((1,3,6,1,4,1,9,9,826,1,50,4,1,17),_CfprMemoryBufferUnitVoltage_Type())
cfprMemoryBufferUnitVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitVoltage.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsTable_Object=MibTable
cfprMemoryBufferUnitEnvStatsTable=_CfprMemoryBufferUnitEnvStatsTable_Object((1,3,6,1,4,1,9,9,826,1,50,5))
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsTable.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsEntry_Object=MibTableRow
cfprMemoryBufferUnitEnvStatsEntry=_CfprMemoryBufferUnitEnvStatsEntry_Object((1,3,6,1,4,1,9,9,826,1,50,5,1))
cfprMemoryBufferUnitEnvStatsEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsEntry.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsInstanceId_Type=CfprManagedObjectId
_CfprMemoryBufferUnitEnvStatsInstanceId_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsInstanceId=_CfprMemoryBufferUnitEnvStatsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,50,5,1,1),_CfprMemoryBufferUnitEnvStatsInstanceId_Type())
cfprMemoryBufferUnitEnvStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsInstanceId.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsDn_Type=CfprManagedObjectDn
_CfprMemoryBufferUnitEnvStatsDn_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsDn=_CfprMemoryBufferUnitEnvStatsDn_Object((1,3,6,1,4,1,9,9,826,1,50,5,1,2),_CfprMemoryBufferUnitEnvStatsDn_Type())
cfprMemoryBufferUnitEnvStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsDn.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsRn_Type=SnmpAdminString
_CfprMemoryBufferUnitEnvStatsRn_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsRn=_CfprMemoryBufferUnitEnvStatsRn_Object((1,3,6,1,4,1,9,9,826,1,50,5,1,3),_CfprMemoryBufferUnitEnvStatsRn_Type())
cfprMemoryBufferUnitEnvStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsRn.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsIntervals_Type=Gauge32
_CfprMemoryBufferUnitEnvStatsIntervals_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsIntervals=_CfprMemoryBufferUnitEnvStatsIntervals_Object((1,3,6,1,4,1,9,9,826,1,50,5,1,4),_CfprMemoryBufferUnitEnvStatsIntervals_Type())
cfprMemoryBufferUnitEnvStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsIntervals.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsSuspect_Type=TruthValue
_CfprMemoryBufferUnitEnvStatsSuspect_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsSuspect=_CfprMemoryBufferUnitEnvStatsSuspect_Object((1,3,6,1,4,1,9,9,826,1,50,5,1,5),_CfprMemoryBufferUnitEnvStatsSuspect_Type())
cfprMemoryBufferUnitEnvStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsSuspect.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsTemperature_Type=Integer32
_CfprMemoryBufferUnitEnvStatsTemperature_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsTemperature=_CfprMemoryBufferUnitEnvStatsTemperature_Object((1,3,6,1,4,1,9,9,826,1,50,5,1,6),_CfprMemoryBufferUnitEnvStatsTemperature_Type())
cfprMemoryBufferUnitEnvStatsTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsTemperature.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsTemperatureAvg_Type=Integer32
_CfprMemoryBufferUnitEnvStatsTemperatureAvg_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsTemperatureAvg=_CfprMemoryBufferUnitEnvStatsTemperatureAvg_Object((1,3,6,1,4,1,9,9,826,1,50,5,1,7),_CfprMemoryBufferUnitEnvStatsTemperatureAvg_Type())
cfprMemoryBufferUnitEnvStatsTemperatureAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsTemperatureAvg.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsTemperatureMax_Type=Integer32
_CfprMemoryBufferUnitEnvStatsTemperatureMax_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsTemperatureMax=_CfprMemoryBufferUnitEnvStatsTemperatureMax_Object((1,3,6,1,4,1,9,9,826,1,50,5,1,8),_CfprMemoryBufferUnitEnvStatsTemperatureMax_Type())
cfprMemoryBufferUnitEnvStatsTemperatureMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsTemperatureMax.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsTemperatureMin_Type=Integer32
_CfprMemoryBufferUnitEnvStatsTemperatureMin_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsTemperatureMin=_CfprMemoryBufferUnitEnvStatsTemperatureMin_Object((1,3,6,1,4,1,9,9,826,1,50,5,1,9),_CfprMemoryBufferUnitEnvStatsTemperatureMin_Type())
cfprMemoryBufferUnitEnvStatsTemperatureMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsTemperatureMin.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsThresholded_Type=CfprMemoryBufferUnitEnvStatsThresholded
_CfprMemoryBufferUnitEnvStatsThresholded_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsThresholded=_CfprMemoryBufferUnitEnvStatsThresholded_Object((1,3,6,1,4,1,9,9,826,1,50,5,1,10),_CfprMemoryBufferUnitEnvStatsThresholded_Type())
cfprMemoryBufferUnitEnvStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsThresholded.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsTimeCollected_Type=DateAndTime
_CfprMemoryBufferUnitEnvStatsTimeCollected_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsTimeCollected=_CfprMemoryBufferUnitEnvStatsTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,50,5,1,11),_CfprMemoryBufferUnitEnvStatsTimeCollected_Type())
cfprMemoryBufferUnitEnvStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsTimeCollected.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsUpdate_Type=Gauge32
_CfprMemoryBufferUnitEnvStatsUpdate_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsUpdate=_CfprMemoryBufferUnitEnvStatsUpdate_Object((1,3,6,1,4,1,9,9,826,1,50,5,1,12),_CfprMemoryBufferUnitEnvStatsUpdate_Type())
cfprMemoryBufferUnitEnvStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsUpdate.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsHistTable_Object=MibTable
cfprMemoryBufferUnitEnvStatsHistTable=_CfprMemoryBufferUnitEnvStatsHistTable_Object((1,3,6,1,4,1,9,9,826,1,50,6))
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsHistTable.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsHistEntry_Object=MibTableRow
cfprMemoryBufferUnitEnvStatsHistEntry=_CfprMemoryBufferUnitEnvStatsHistEntry_Object((1,3,6,1,4,1,9,9,826,1,50,6,1))
cfprMemoryBufferUnitEnvStatsHistEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsHistEntry.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsHistInstanceId_Type=CfprManagedObjectId
_CfprMemoryBufferUnitEnvStatsHistInstanceId_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsHistInstanceId=_CfprMemoryBufferUnitEnvStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,826,1,50,6,1,1),_CfprMemoryBufferUnitEnvStatsHistInstanceId_Type())
cfprMemoryBufferUnitEnvStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsHistInstanceId.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsHistDn_Type=CfprManagedObjectDn
_CfprMemoryBufferUnitEnvStatsHistDn_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsHistDn=_CfprMemoryBufferUnitEnvStatsHistDn_Object((1,3,6,1,4,1,9,9,826,1,50,6,1,2),_CfprMemoryBufferUnitEnvStatsHistDn_Type())
cfprMemoryBufferUnitEnvStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsHistDn.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsHistRn_Type=SnmpAdminString
_CfprMemoryBufferUnitEnvStatsHistRn_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsHistRn=_CfprMemoryBufferUnitEnvStatsHistRn_Object((1,3,6,1,4,1,9,9,826,1,50,6,1,3),_CfprMemoryBufferUnitEnvStatsHistRn_Type())
cfprMemoryBufferUnitEnvStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsHistRn.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsHistId_Type=Unsigned64
_CfprMemoryBufferUnitEnvStatsHistId_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsHistId=_CfprMemoryBufferUnitEnvStatsHistId_Object((1,3,6,1,4,1,9,9,826,1,50,6,1,4),_CfprMemoryBufferUnitEnvStatsHistId_Type())
cfprMemoryBufferUnitEnvStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsHistId.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsHistMostRecent_Type=TruthValue
_CfprMemoryBufferUnitEnvStatsHistMostRecent_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsHistMostRecent=_CfprMemoryBufferUnitEnvStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,826,1,50,6,1,5),_CfprMemoryBufferUnitEnvStatsHistMostRecent_Type())
cfprMemoryBufferUnitEnvStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsHistMostRecent.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsHistSuspect_Type=TruthValue
_CfprMemoryBufferUnitEnvStatsHistSuspect_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsHistSuspect=_CfprMemoryBufferUnitEnvStatsHistSuspect_Object((1,3,6,1,4,1,9,9,826,1,50,6,1,6),_CfprMemoryBufferUnitEnvStatsHistSuspect_Type())
cfprMemoryBufferUnitEnvStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsHistSuspect.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsHistTemperature_Type=Integer32
_CfprMemoryBufferUnitEnvStatsHistTemperature_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsHistTemperature=_CfprMemoryBufferUnitEnvStatsHistTemperature_Object((1,3,6,1,4,1,9,9,826,1,50,6,1,7),_CfprMemoryBufferUnitEnvStatsHistTemperature_Type())
cfprMemoryBufferUnitEnvStatsHistTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsHistTemperature.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsHistTemperatureAvg_Type=Integer32
_CfprMemoryBufferUnitEnvStatsHistTemperatureAvg_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsHistTemperatureAvg=_CfprMemoryBufferUnitEnvStatsHistTemperatureAvg_Object((1,3,6,1,4,1,9,9,826,1,50,6,1,8),_CfprMemoryBufferUnitEnvStatsHistTemperatureAvg_Type())
cfprMemoryBufferUnitEnvStatsHistTemperatureAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsHistTemperatureAvg.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsHistTemperatureMax_Type=Integer32
_CfprMemoryBufferUnitEnvStatsHistTemperatureMax_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsHistTemperatureMax=_CfprMemoryBufferUnitEnvStatsHistTemperatureMax_Object((1,3,6,1,4,1,9,9,826,1,50,6,1,9),_CfprMemoryBufferUnitEnvStatsHistTemperatureMax_Type())
cfprMemoryBufferUnitEnvStatsHistTemperatureMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsHistTemperatureMax.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsHistTemperatureMin_Type=Integer32
_CfprMemoryBufferUnitEnvStatsHistTemperatureMin_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsHistTemperatureMin=_CfprMemoryBufferUnitEnvStatsHistTemperatureMin_Object((1,3,6,1,4,1,9,9,826,1,50,6,1,10),_CfprMemoryBufferUnitEnvStatsHistTemperatureMin_Type())
cfprMemoryBufferUnitEnvStatsHistTemperatureMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsHistTemperatureMin.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsHistThresholded_Type=CfprMemoryBufferUnitEnvStatsHistThresholded
_CfprMemoryBufferUnitEnvStatsHistThresholded_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsHistThresholded=_CfprMemoryBufferUnitEnvStatsHistThresholded_Object((1,3,6,1,4,1,9,9,826,1,50,6,1,11),_CfprMemoryBufferUnitEnvStatsHistThresholded_Type())
cfprMemoryBufferUnitEnvStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsHistThresholded.setStatus(_A)
_CfprMemoryBufferUnitEnvStatsHistTimeCollected_Type=DateAndTime
_CfprMemoryBufferUnitEnvStatsHistTimeCollected_Object=MibTableColumn
cfprMemoryBufferUnitEnvStatsHistTimeCollected=_CfprMemoryBufferUnitEnvStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,50,6,1,12),_CfprMemoryBufferUnitEnvStatsHistTimeCollected_Type())
cfprMemoryBufferUnitEnvStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryBufferUnitEnvStatsHistTimeCollected.setStatus(_A)
_CfprMemoryErrorStatsTable_Object=MibTable
cfprMemoryErrorStatsTable=_CfprMemoryErrorStatsTable_Object((1,3,6,1,4,1,9,9,826,1,50,7))
if mibBuilder.loadTexts:cfprMemoryErrorStatsTable.setStatus(_A)
_CfprMemoryErrorStatsEntry_Object=MibTableRow
cfprMemoryErrorStatsEntry=_CfprMemoryErrorStatsEntry_Object((1,3,6,1,4,1,9,9,826,1,50,7,1))
cfprMemoryErrorStatsEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprMemoryErrorStatsEntry.setStatus(_A)
_CfprMemoryErrorStatsInstanceId_Type=CfprManagedObjectId
_CfprMemoryErrorStatsInstanceId_Object=MibTableColumn
cfprMemoryErrorStatsInstanceId=_CfprMemoryErrorStatsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,1),_CfprMemoryErrorStatsInstanceId_Type())
cfprMemoryErrorStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMemoryErrorStatsInstanceId.setStatus(_A)
_CfprMemoryErrorStatsDn_Type=CfprManagedObjectDn
_CfprMemoryErrorStatsDn_Object=MibTableColumn
cfprMemoryErrorStatsDn=_CfprMemoryErrorStatsDn_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,2),_CfprMemoryErrorStatsDn_Type())
cfprMemoryErrorStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsDn.setStatus(_A)
_CfprMemoryErrorStatsRn_Type=SnmpAdminString
_CfprMemoryErrorStatsRn_Object=MibTableColumn
cfprMemoryErrorStatsRn=_CfprMemoryErrorStatsRn_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,3),_CfprMemoryErrorStatsRn_Type())
cfprMemoryErrorStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsRn.setStatus(_A)
_CfprMemoryErrorStatsAddressParityErrors_Type=Counter32
_CfprMemoryErrorStatsAddressParityErrors_Object=MibTableColumn
cfprMemoryErrorStatsAddressParityErrors=_CfprMemoryErrorStatsAddressParityErrors_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,4),_CfprMemoryErrorStatsAddressParityErrors_Type())
cfprMemoryErrorStatsAddressParityErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsAddressParityErrors.setStatus(_A)
_CfprMemoryErrorStatsAddressParityErrors15Min_Type=Gauge32
_CfprMemoryErrorStatsAddressParityErrors15Min_Object=MibTableColumn
cfprMemoryErrorStatsAddressParityErrors15Min=_CfprMemoryErrorStatsAddressParityErrors15Min_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,5),_CfprMemoryErrorStatsAddressParityErrors15Min_Type())
cfprMemoryErrorStatsAddressParityErrors15Min.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsAddressParityErrors15Min.setStatus(_A)
_CfprMemoryErrorStatsAddressParityErrors15MinH_Type=Gauge32
_CfprMemoryErrorStatsAddressParityErrors15MinH_Object=MibTableColumn
cfprMemoryErrorStatsAddressParityErrors15MinH=_CfprMemoryErrorStatsAddressParityErrors15MinH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,6),_CfprMemoryErrorStatsAddressParityErrors15MinH_Type())
cfprMemoryErrorStatsAddressParityErrors15MinH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsAddressParityErrors15MinH.setStatus(_A)
_CfprMemoryErrorStatsAddressParityErrors1Day_Type=Gauge32
_CfprMemoryErrorStatsAddressParityErrors1Day_Object=MibTableColumn
cfprMemoryErrorStatsAddressParityErrors1Day=_CfprMemoryErrorStatsAddressParityErrors1Day_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,7),_CfprMemoryErrorStatsAddressParityErrors1Day_Type())
cfprMemoryErrorStatsAddressParityErrors1Day.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsAddressParityErrors1Day.setStatus(_A)
_CfprMemoryErrorStatsAddressParityErrors1DayH_Type=Gauge32
_CfprMemoryErrorStatsAddressParityErrors1DayH_Object=MibTableColumn
cfprMemoryErrorStatsAddressParityErrors1DayH=_CfprMemoryErrorStatsAddressParityErrors1DayH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,8),_CfprMemoryErrorStatsAddressParityErrors1DayH_Type())
cfprMemoryErrorStatsAddressParityErrors1DayH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsAddressParityErrors1DayH.setStatus(_A)
_CfprMemoryErrorStatsAddressParityErrors1Hour_Type=Gauge32
_CfprMemoryErrorStatsAddressParityErrors1Hour_Object=MibTableColumn
cfprMemoryErrorStatsAddressParityErrors1Hour=_CfprMemoryErrorStatsAddressParityErrors1Hour_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,9),_CfprMemoryErrorStatsAddressParityErrors1Hour_Type())
cfprMemoryErrorStatsAddressParityErrors1Hour.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsAddressParityErrors1Hour.setStatus(_A)
_CfprMemoryErrorStatsAddressParityErrors1HourH_Type=Gauge32
_CfprMemoryErrorStatsAddressParityErrors1HourH_Object=MibTableColumn
cfprMemoryErrorStatsAddressParityErrors1HourH=_CfprMemoryErrorStatsAddressParityErrors1HourH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,10),_CfprMemoryErrorStatsAddressParityErrors1HourH_Type())
cfprMemoryErrorStatsAddressParityErrors1HourH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsAddressParityErrors1HourH.setStatus(_A)
_CfprMemoryErrorStatsAddressParityErrors1Week_Type=Gauge32
_CfprMemoryErrorStatsAddressParityErrors1Week_Object=MibTableColumn
cfprMemoryErrorStatsAddressParityErrors1Week=_CfprMemoryErrorStatsAddressParityErrors1Week_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,11),_CfprMemoryErrorStatsAddressParityErrors1Week_Type())
cfprMemoryErrorStatsAddressParityErrors1Week.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsAddressParityErrors1Week.setStatus(_A)
_CfprMemoryErrorStatsAddressParityErrors1WeekH_Type=Gauge32
_CfprMemoryErrorStatsAddressParityErrors1WeekH_Object=MibTableColumn
cfprMemoryErrorStatsAddressParityErrors1WeekH=_CfprMemoryErrorStatsAddressParityErrors1WeekH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,12),_CfprMemoryErrorStatsAddressParityErrors1WeekH_Type())
cfprMemoryErrorStatsAddressParityErrors1WeekH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsAddressParityErrors1WeekH.setStatus(_A)
_CfprMemoryErrorStatsAddressParityErrors2Weeks_Type=Gauge32
_CfprMemoryErrorStatsAddressParityErrors2Weeks_Object=MibTableColumn
cfprMemoryErrorStatsAddressParityErrors2Weeks=_CfprMemoryErrorStatsAddressParityErrors2Weeks_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,13),_CfprMemoryErrorStatsAddressParityErrors2Weeks_Type())
cfprMemoryErrorStatsAddressParityErrors2Weeks.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsAddressParityErrors2Weeks.setStatus(_A)
_CfprMemoryErrorStatsAddressParityErrors2WeeksH_Type=Gauge32
_CfprMemoryErrorStatsAddressParityErrors2WeeksH_Object=MibTableColumn
cfprMemoryErrorStatsAddressParityErrors2WeeksH=_CfprMemoryErrorStatsAddressParityErrors2WeeksH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,14),_CfprMemoryErrorStatsAddressParityErrors2WeeksH_Type())
cfprMemoryErrorStatsAddressParityErrors2WeeksH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsAddressParityErrors2WeeksH.setStatus(_A)
_CfprMemoryErrorStatsEccMultibitErrors_Type=Counter32
_CfprMemoryErrorStatsEccMultibitErrors_Object=MibTableColumn
cfprMemoryErrorStatsEccMultibitErrors=_CfprMemoryErrorStatsEccMultibitErrors_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,15),_CfprMemoryErrorStatsEccMultibitErrors_Type())
cfprMemoryErrorStatsEccMultibitErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccMultibitErrors.setStatus(_A)
_CfprMemoryErrorStatsEccMultibitErrors15Min_Type=Gauge32
_CfprMemoryErrorStatsEccMultibitErrors15Min_Object=MibTableColumn
cfprMemoryErrorStatsEccMultibitErrors15Min=_CfprMemoryErrorStatsEccMultibitErrors15Min_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,16),_CfprMemoryErrorStatsEccMultibitErrors15Min_Type())
cfprMemoryErrorStatsEccMultibitErrors15Min.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccMultibitErrors15Min.setStatus(_A)
_CfprMemoryErrorStatsEccMultibitErrors15MinH_Type=Gauge32
_CfprMemoryErrorStatsEccMultibitErrors15MinH_Object=MibTableColumn
cfprMemoryErrorStatsEccMultibitErrors15MinH=_CfprMemoryErrorStatsEccMultibitErrors15MinH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,17),_CfprMemoryErrorStatsEccMultibitErrors15MinH_Type())
cfprMemoryErrorStatsEccMultibitErrors15MinH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccMultibitErrors15MinH.setStatus(_A)
_CfprMemoryErrorStatsEccMultibitErrors1Day_Type=Gauge32
_CfprMemoryErrorStatsEccMultibitErrors1Day_Object=MibTableColumn
cfprMemoryErrorStatsEccMultibitErrors1Day=_CfprMemoryErrorStatsEccMultibitErrors1Day_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,18),_CfprMemoryErrorStatsEccMultibitErrors1Day_Type())
cfprMemoryErrorStatsEccMultibitErrors1Day.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccMultibitErrors1Day.setStatus(_A)
_CfprMemoryErrorStatsEccMultibitErrors1DayH_Type=Gauge32
_CfprMemoryErrorStatsEccMultibitErrors1DayH_Object=MibTableColumn
cfprMemoryErrorStatsEccMultibitErrors1DayH=_CfprMemoryErrorStatsEccMultibitErrors1DayH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,19),_CfprMemoryErrorStatsEccMultibitErrors1DayH_Type())
cfprMemoryErrorStatsEccMultibitErrors1DayH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccMultibitErrors1DayH.setStatus(_A)
_CfprMemoryErrorStatsEccMultibitErrors1Hour_Type=Gauge32
_CfprMemoryErrorStatsEccMultibitErrors1Hour_Object=MibTableColumn
cfprMemoryErrorStatsEccMultibitErrors1Hour=_CfprMemoryErrorStatsEccMultibitErrors1Hour_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,20),_CfprMemoryErrorStatsEccMultibitErrors1Hour_Type())
cfprMemoryErrorStatsEccMultibitErrors1Hour.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccMultibitErrors1Hour.setStatus(_A)
_CfprMemoryErrorStatsEccMultibitErrors1HourH_Type=Gauge32
_CfprMemoryErrorStatsEccMultibitErrors1HourH_Object=MibTableColumn
cfprMemoryErrorStatsEccMultibitErrors1HourH=_CfprMemoryErrorStatsEccMultibitErrors1HourH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,21),_CfprMemoryErrorStatsEccMultibitErrors1HourH_Type())
cfprMemoryErrorStatsEccMultibitErrors1HourH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccMultibitErrors1HourH.setStatus(_A)
_CfprMemoryErrorStatsEccMultibitErrors1Week_Type=Gauge32
_CfprMemoryErrorStatsEccMultibitErrors1Week_Object=MibTableColumn
cfprMemoryErrorStatsEccMultibitErrors1Week=_CfprMemoryErrorStatsEccMultibitErrors1Week_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,22),_CfprMemoryErrorStatsEccMultibitErrors1Week_Type())
cfprMemoryErrorStatsEccMultibitErrors1Week.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccMultibitErrors1Week.setStatus(_A)
_CfprMemoryErrorStatsEccMultibitErrors1WeekH_Type=Gauge32
_CfprMemoryErrorStatsEccMultibitErrors1WeekH_Object=MibTableColumn
cfprMemoryErrorStatsEccMultibitErrors1WeekH=_CfprMemoryErrorStatsEccMultibitErrors1WeekH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,23),_CfprMemoryErrorStatsEccMultibitErrors1WeekH_Type())
cfprMemoryErrorStatsEccMultibitErrors1WeekH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccMultibitErrors1WeekH.setStatus(_A)
_CfprMemoryErrorStatsEccMultibitErrors2Weeks_Type=Gauge32
_CfprMemoryErrorStatsEccMultibitErrors2Weeks_Object=MibTableColumn
cfprMemoryErrorStatsEccMultibitErrors2Weeks=_CfprMemoryErrorStatsEccMultibitErrors2Weeks_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,24),_CfprMemoryErrorStatsEccMultibitErrors2Weeks_Type())
cfprMemoryErrorStatsEccMultibitErrors2Weeks.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccMultibitErrors2Weeks.setStatus(_A)
_CfprMemoryErrorStatsEccMultibitErrors2WeeksH_Type=Gauge32
_CfprMemoryErrorStatsEccMultibitErrors2WeeksH_Object=MibTableColumn
cfprMemoryErrorStatsEccMultibitErrors2WeeksH=_CfprMemoryErrorStatsEccMultibitErrors2WeeksH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,25),_CfprMemoryErrorStatsEccMultibitErrors2WeeksH_Type())
cfprMemoryErrorStatsEccMultibitErrors2WeeksH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccMultibitErrors2WeeksH.setStatus(_A)
_CfprMemoryErrorStatsEccSinglebitErrors_Type=Counter32
_CfprMemoryErrorStatsEccSinglebitErrors_Object=MibTableColumn
cfprMemoryErrorStatsEccSinglebitErrors=_CfprMemoryErrorStatsEccSinglebitErrors_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,26),_CfprMemoryErrorStatsEccSinglebitErrors_Type())
cfprMemoryErrorStatsEccSinglebitErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccSinglebitErrors.setStatus(_A)
_CfprMemoryErrorStatsEccSinglebitErrors15Min_Type=Gauge32
_CfprMemoryErrorStatsEccSinglebitErrors15Min_Object=MibTableColumn
cfprMemoryErrorStatsEccSinglebitErrors15Min=_CfprMemoryErrorStatsEccSinglebitErrors15Min_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,27),_CfprMemoryErrorStatsEccSinglebitErrors15Min_Type())
cfprMemoryErrorStatsEccSinglebitErrors15Min.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccSinglebitErrors15Min.setStatus(_A)
_CfprMemoryErrorStatsEccSinglebitErrors15MinH_Type=Gauge32
_CfprMemoryErrorStatsEccSinglebitErrors15MinH_Object=MibTableColumn
cfprMemoryErrorStatsEccSinglebitErrors15MinH=_CfprMemoryErrorStatsEccSinglebitErrors15MinH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,28),_CfprMemoryErrorStatsEccSinglebitErrors15MinH_Type())
cfprMemoryErrorStatsEccSinglebitErrors15MinH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccSinglebitErrors15MinH.setStatus(_A)
_CfprMemoryErrorStatsEccSinglebitErrors1Day_Type=Gauge32
_CfprMemoryErrorStatsEccSinglebitErrors1Day_Object=MibTableColumn
cfprMemoryErrorStatsEccSinglebitErrors1Day=_CfprMemoryErrorStatsEccSinglebitErrors1Day_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,29),_CfprMemoryErrorStatsEccSinglebitErrors1Day_Type())
cfprMemoryErrorStatsEccSinglebitErrors1Day.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccSinglebitErrors1Day.setStatus(_A)
_CfprMemoryErrorStatsEccSinglebitErrors1DayH_Type=Gauge32
_CfprMemoryErrorStatsEccSinglebitErrors1DayH_Object=MibTableColumn
cfprMemoryErrorStatsEccSinglebitErrors1DayH=_CfprMemoryErrorStatsEccSinglebitErrors1DayH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,30),_CfprMemoryErrorStatsEccSinglebitErrors1DayH_Type())
cfprMemoryErrorStatsEccSinglebitErrors1DayH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccSinglebitErrors1DayH.setStatus(_A)
_CfprMemoryErrorStatsEccSinglebitErrors1Hour_Type=Gauge32
_CfprMemoryErrorStatsEccSinglebitErrors1Hour_Object=MibTableColumn
cfprMemoryErrorStatsEccSinglebitErrors1Hour=_CfprMemoryErrorStatsEccSinglebitErrors1Hour_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,31),_CfprMemoryErrorStatsEccSinglebitErrors1Hour_Type())
cfprMemoryErrorStatsEccSinglebitErrors1Hour.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccSinglebitErrors1Hour.setStatus(_A)
_CfprMemoryErrorStatsEccSinglebitErrors1HourH_Type=Gauge32
_CfprMemoryErrorStatsEccSinglebitErrors1HourH_Object=MibTableColumn
cfprMemoryErrorStatsEccSinglebitErrors1HourH=_CfprMemoryErrorStatsEccSinglebitErrors1HourH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,32),_CfprMemoryErrorStatsEccSinglebitErrors1HourH_Type())
cfprMemoryErrorStatsEccSinglebitErrors1HourH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccSinglebitErrors1HourH.setStatus(_A)
_CfprMemoryErrorStatsEccSinglebitErrors1Week_Type=Gauge32
_CfprMemoryErrorStatsEccSinglebitErrors1Week_Object=MibTableColumn
cfprMemoryErrorStatsEccSinglebitErrors1Week=_CfprMemoryErrorStatsEccSinglebitErrors1Week_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,33),_CfprMemoryErrorStatsEccSinglebitErrors1Week_Type())
cfprMemoryErrorStatsEccSinglebitErrors1Week.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccSinglebitErrors1Week.setStatus(_A)
_CfprMemoryErrorStatsEccSinglebitErrors1WeekH_Type=Gauge32
_CfprMemoryErrorStatsEccSinglebitErrors1WeekH_Object=MibTableColumn
cfprMemoryErrorStatsEccSinglebitErrors1WeekH=_CfprMemoryErrorStatsEccSinglebitErrors1WeekH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,34),_CfprMemoryErrorStatsEccSinglebitErrors1WeekH_Type())
cfprMemoryErrorStatsEccSinglebitErrors1WeekH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccSinglebitErrors1WeekH.setStatus(_A)
_CfprMemoryErrorStatsEccSinglebitErrors2Weeks_Type=Gauge32
_CfprMemoryErrorStatsEccSinglebitErrors2Weeks_Object=MibTableColumn
cfprMemoryErrorStatsEccSinglebitErrors2Weeks=_CfprMemoryErrorStatsEccSinglebitErrors2Weeks_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,35),_CfprMemoryErrorStatsEccSinglebitErrors2Weeks_Type())
cfprMemoryErrorStatsEccSinglebitErrors2Weeks.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccSinglebitErrors2Weeks.setStatus(_A)
_CfprMemoryErrorStatsEccSinglebitErrors2WeeksH_Type=Gauge32
_CfprMemoryErrorStatsEccSinglebitErrors2WeeksH_Object=MibTableColumn
cfprMemoryErrorStatsEccSinglebitErrors2WeeksH=_CfprMemoryErrorStatsEccSinglebitErrors2WeeksH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,36),_CfprMemoryErrorStatsEccSinglebitErrors2WeeksH_Type())
cfprMemoryErrorStatsEccSinglebitErrors2WeeksH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsEccSinglebitErrors2WeeksH.setStatus(_A)
_CfprMemoryErrorStatsIntervals_Type=Gauge32
_CfprMemoryErrorStatsIntervals_Object=MibTableColumn
cfprMemoryErrorStatsIntervals=_CfprMemoryErrorStatsIntervals_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,37),_CfprMemoryErrorStatsIntervals_Type())
cfprMemoryErrorStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsIntervals.setStatus(_A)
_CfprMemoryErrorStatsMismatchErrors_Type=Counter32
_CfprMemoryErrorStatsMismatchErrors_Object=MibTableColumn
cfprMemoryErrorStatsMismatchErrors=_CfprMemoryErrorStatsMismatchErrors_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,38),_CfprMemoryErrorStatsMismatchErrors_Type())
cfprMemoryErrorStatsMismatchErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsMismatchErrors.setStatus(_A)
_CfprMemoryErrorStatsMismatchErrors15Min_Type=Gauge32
_CfprMemoryErrorStatsMismatchErrors15Min_Object=MibTableColumn
cfprMemoryErrorStatsMismatchErrors15Min=_CfprMemoryErrorStatsMismatchErrors15Min_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,39),_CfprMemoryErrorStatsMismatchErrors15Min_Type())
cfprMemoryErrorStatsMismatchErrors15Min.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsMismatchErrors15Min.setStatus(_A)
_CfprMemoryErrorStatsMismatchErrors15MinH_Type=Gauge32
_CfprMemoryErrorStatsMismatchErrors15MinH_Object=MibTableColumn
cfprMemoryErrorStatsMismatchErrors15MinH=_CfprMemoryErrorStatsMismatchErrors15MinH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,40),_CfprMemoryErrorStatsMismatchErrors15MinH_Type())
cfprMemoryErrorStatsMismatchErrors15MinH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsMismatchErrors15MinH.setStatus(_A)
_CfprMemoryErrorStatsMismatchErrors1Day_Type=Gauge32
_CfprMemoryErrorStatsMismatchErrors1Day_Object=MibTableColumn
cfprMemoryErrorStatsMismatchErrors1Day=_CfprMemoryErrorStatsMismatchErrors1Day_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,41),_CfprMemoryErrorStatsMismatchErrors1Day_Type())
cfprMemoryErrorStatsMismatchErrors1Day.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsMismatchErrors1Day.setStatus(_A)
_CfprMemoryErrorStatsMismatchErrors1DayH_Type=Gauge32
_CfprMemoryErrorStatsMismatchErrors1DayH_Object=MibTableColumn
cfprMemoryErrorStatsMismatchErrors1DayH=_CfprMemoryErrorStatsMismatchErrors1DayH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,42),_CfprMemoryErrorStatsMismatchErrors1DayH_Type())
cfprMemoryErrorStatsMismatchErrors1DayH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsMismatchErrors1DayH.setStatus(_A)
_CfprMemoryErrorStatsMismatchErrors1Hour_Type=Gauge32
_CfprMemoryErrorStatsMismatchErrors1Hour_Object=MibTableColumn
cfprMemoryErrorStatsMismatchErrors1Hour=_CfprMemoryErrorStatsMismatchErrors1Hour_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,43),_CfprMemoryErrorStatsMismatchErrors1Hour_Type())
cfprMemoryErrorStatsMismatchErrors1Hour.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsMismatchErrors1Hour.setStatus(_A)
_CfprMemoryErrorStatsMismatchErrors1HourH_Type=Gauge32
_CfprMemoryErrorStatsMismatchErrors1HourH_Object=MibTableColumn
cfprMemoryErrorStatsMismatchErrors1HourH=_CfprMemoryErrorStatsMismatchErrors1HourH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,44),_CfprMemoryErrorStatsMismatchErrors1HourH_Type())
cfprMemoryErrorStatsMismatchErrors1HourH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsMismatchErrors1HourH.setStatus(_A)
_CfprMemoryErrorStatsMismatchErrors1Week_Type=Gauge32
_CfprMemoryErrorStatsMismatchErrors1Week_Object=MibTableColumn
cfprMemoryErrorStatsMismatchErrors1Week=_CfprMemoryErrorStatsMismatchErrors1Week_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,45),_CfprMemoryErrorStatsMismatchErrors1Week_Type())
cfprMemoryErrorStatsMismatchErrors1Week.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsMismatchErrors1Week.setStatus(_A)
_CfprMemoryErrorStatsMismatchErrors1WeekH_Type=Gauge32
_CfprMemoryErrorStatsMismatchErrors1WeekH_Object=MibTableColumn
cfprMemoryErrorStatsMismatchErrors1WeekH=_CfprMemoryErrorStatsMismatchErrors1WeekH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,46),_CfprMemoryErrorStatsMismatchErrors1WeekH_Type())
cfprMemoryErrorStatsMismatchErrors1WeekH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsMismatchErrors1WeekH.setStatus(_A)
_CfprMemoryErrorStatsMismatchErrors2Weeks_Type=Gauge32
_CfprMemoryErrorStatsMismatchErrors2Weeks_Object=MibTableColumn
cfprMemoryErrorStatsMismatchErrors2Weeks=_CfprMemoryErrorStatsMismatchErrors2Weeks_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,47),_CfprMemoryErrorStatsMismatchErrors2Weeks_Type())
cfprMemoryErrorStatsMismatchErrors2Weeks.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsMismatchErrors2Weeks.setStatus(_A)
_CfprMemoryErrorStatsMismatchErrors2WeeksH_Type=Gauge32
_CfprMemoryErrorStatsMismatchErrors2WeeksH_Object=MibTableColumn
cfprMemoryErrorStatsMismatchErrors2WeeksH=_CfprMemoryErrorStatsMismatchErrors2WeeksH_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,48),_CfprMemoryErrorStatsMismatchErrors2WeeksH_Type())
cfprMemoryErrorStatsMismatchErrors2WeeksH.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsMismatchErrors2WeeksH.setStatus(_A)
_CfprMemoryErrorStatsSuspect_Type=TruthValue
_CfprMemoryErrorStatsSuspect_Object=MibTableColumn
cfprMemoryErrorStatsSuspect=_CfprMemoryErrorStatsSuspect_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,49),_CfprMemoryErrorStatsSuspect_Type())
cfprMemoryErrorStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsSuspect.setStatus(_A)
_CfprMemoryErrorStatsThresholded_Type=CfprMemoryErrorStatsThresholded
_CfprMemoryErrorStatsThresholded_Object=MibTableColumn
cfprMemoryErrorStatsThresholded=_CfprMemoryErrorStatsThresholded_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,50),_CfprMemoryErrorStatsThresholded_Type())
cfprMemoryErrorStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsThresholded.setStatus(_A)
_CfprMemoryErrorStatsTimeCollected_Type=DateAndTime
_CfprMemoryErrorStatsTimeCollected_Object=MibTableColumn
cfprMemoryErrorStatsTimeCollected=_CfprMemoryErrorStatsTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,51),_CfprMemoryErrorStatsTimeCollected_Type())
cfprMemoryErrorStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsTimeCollected.setStatus(_A)
_CfprMemoryErrorStatsUpdate_Type=Gauge32
_CfprMemoryErrorStatsUpdate_Object=MibTableColumn
cfprMemoryErrorStatsUpdate=_CfprMemoryErrorStatsUpdate_Object((1,3,6,1,4,1,9,9,826,1,50,7,1,52),_CfprMemoryErrorStatsUpdate_Type())
cfprMemoryErrorStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryErrorStatsUpdate.setStatus(_A)
_CfprMemoryQualTable_Object=MibTable
cfprMemoryQualTable=_CfprMemoryQualTable_Object((1,3,6,1,4,1,9,9,826,1,50,8))
if mibBuilder.loadTexts:cfprMemoryQualTable.setStatus(_A)
_CfprMemoryQualEntry_Object=MibTableRow
cfprMemoryQualEntry=_CfprMemoryQualEntry_Object((1,3,6,1,4,1,9,9,826,1,50,8,1))
cfprMemoryQualEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cfprMemoryQualEntry.setStatus(_A)
_CfprMemoryQualInstanceId_Type=CfprManagedObjectId
_CfprMemoryQualInstanceId_Object=MibTableColumn
cfprMemoryQualInstanceId=_CfprMemoryQualInstanceId_Object((1,3,6,1,4,1,9,9,826,1,50,8,1,1),_CfprMemoryQualInstanceId_Type())
cfprMemoryQualInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMemoryQualInstanceId.setStatus(_A)
_CfprMemoryQualDn_Type=CfprManagedObjectDn
_CfprMemoryQualDn_Object=MibTableColumn
cfprMemoryQualDn=_CfprMemoryQualDn_Object((1,3,6,1,4,1,9,9,826,1,50,8,1,2),_CfprMemoryQualDn_Type())
cfprMemoryQualDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryQualDn.setStatus(_A)
_CfprMemoryQualRn_Type=SnmpAdminString
_CfprMemoryQualRn_Object=MibTableColumn
cfprMemoryQualRn=_CfprMemoryQualRn_Object((1,3,6,1,4,1,9,9,826,1,50,8,1,3),_CfprMemoryQualRn_Type())
cfprMemoryQualRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryQualRn.setStatus(_A)
_CfprMemoryQualClock_Type=Gauge32
_CfprMemoryQualClock_Object=MibTableColumn
cfprMemoryQualClock=_CfprMemoryQualClock_Object((1,3,6,1,4,1,9,9,826,1,50,8,1,4),_CfprMemoryQualClock_Type())
cfprMemoryQualClock.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryQualClock.setStatus(_A)
_CfprMemoryQualLatency_Type=Integer32
_CfprMemoryQualLatency_Object=MibTableColumn
cfprMemoryQualLatency=_CfprMemoryQualLatency_Object((1,3,6,1,4,1,9,9,826,1,50,8,1,5),_CfprMemoryQualLatency_Type())
cfprMemoryQualLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryQualLatency.setStatus(_A)
_CfprMemoryQualMaxCap_Type=Gauge32
_CfprMemoryQualMaxCap_Object=MibTableColumn
cfprMemoryQualMaxCap=_CfprMemoryQualMaxCap_Object((1,3,6,1,4,1,9,9,826,1,50,8,1,6),_CfprMemoryQualMaxCap_Type())
cfprMemoryQualMaxCap.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryQualMaxCap.setStatus(_A)
_CfprMemoryQualMinCap_Type=Gauge32
_CfprMemoryQualMinCap_Object=MibTableColumn
cfprMemoryQualMinCap=_CfprMemoryQualMinCap_Object((1,3,6,1,4,1,9,9,826,1,50,8,1,7),_CfprMemoryQualMinCap_Type())
cfprMemoryQualMinCap.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryQualMinCap.setStatus(_A)
_CfprMemoryQualSpeed_Type=Gauge32
_CfprMemoryQualSpeed_Object=MibTableColumn
cfprMemoryQualSpeed=_CfprMemoryQualSpeed_Object((1,3,6,1,4,1,9,9,826,1,50,8,1,8),_CfprMemoryQualSpeed_Type())
cfprMemoryQualSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryQualSpeed.setStatus(_A)
_CfprMemoryQualUnits_Type=Gauge32
_CfprMemoryQualUnits_Object=MibTableColumn
cfprMemoryQualUnits=_CfprMemoryQualUnits_Object((1,3,6,1,4,1,9,9,826,1,50,8,1,9),_CfprMemoryQualUnits_Type())
cfprMemoryQualUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryQualUnits.setStatus(_A)
_CfprMemoryQualWidth_Type=Gauge32
_CfprMemoryQualWidth_Object=MibTableColumn
cfprMemoryQualWidth=_CfprMemoryQualWidth_Object((1,3,6,1,4,1,9,9,826,1,50,8,1,10),_CfprMemoryQualWidth_Type())
cfprMemoryQualWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryQualWidth.setStatus(_A)
_CfprMemoryRuntimeTable_Object=MibTable
cfprMemoryRuntimeTable=_CfprMemoryRuntimeTable_Object((1,3,6,1,4,1,9,9,826,1,50,9))
if mibBuilder.loadTexts:cfprMemoryRuntimeTable.setStatus(_A)
_CfprMemoryRuntimeEntry_Object=MibTableRow
cfprMemoryRuntimeEntry=_CfprMemoryRuntimeEntry_Object((1,3,6,1,4,1,9,9,826,1,50,9,1))
cfprMemoryRuntimeEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cfprMemoryRuntimeEntry.setStatus(_A)
_CfprMemoryRuntimeInstanceId_Type=CfprManagedObjectId
_CfprMemoryRuntimeInstanceId_Object=MibTableColumn
cfprMemoryRuntimeInstanceId=_CfprMemoryRuntimeInstanceId_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,1),_CfprMemoryRuntimeInstanceId_Type())
cfprMemoryRuntimeInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMemoryRuntimeInstanceId.setStatus(_A)
_CfprMemoryRuntimeDn_Type=CfprManagedObjectDn
_CfprMemoryRuntimeDn_Object=MibTableColumn
cfprMemoryRuntimeDn=_CfprMemoryRuntimeDn_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,2),_CfprMemoryRuntimeDn_Type())
cfprMemoryRuntimeDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeDn.setStatus(_A)
_CfprMemoryRuntimeRn_Type=SnmpAdminString
_CfprMemoryRuntimeRn_Object=MibTableColumn
cfprMemoryRuntimeRn=_CfprMemoryRuntimeRn_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,3),_CfprMemoryRuntimeRn_Type())
cfprMemoryRuntimeRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeRn.setStatus(_A)
_CfprMemoryRuntimeAvailable_Type=Gauge32
_CfprMemoryRuntimeAvailable_Object=MibTableColumn
cfprMemoryRuntimeAvailable=_CfprMemoryRuntimeAvailable_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,4),_CfprMemoryRuntimeAvailable_Type())
cfprMemoryRuntimeAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeAvailable.setStatus(_A)
_CfprMemoryRuntimeAvailableAvg_Type=Gauge32
_CfprMemoryRuntimeAvailableAvg_Object=MibTableColumn
cfprMemoryRuntimeAvailableAvg=_CfprMemoryRuntimeAvailableAvg_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,5),_CfprMemoryRuntimeAvailableAvg_Type())
cfprMemoryRuntimeAvailableAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeAvailableAvg.setStatus(_A)
_CfprMemoryRuntimeAvailableMax_Type=Gauge32
_CfprMemoryRuntimeAvailableMax_Object=MibTableColumn
cfprMemoryRuntimeAvailableMax=_CfprMemoryRuntimeAvailableMax_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,6),_CfprMemoryRuntimeAvailableMax_Type())
cfprMemoryRuntimeAvailableMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeAvailableMax.setStatus(_A)
_CfprMemoryRuntimeAvailableMin_Type=Gauge32
_CfprMemoryRuntimeAvailableMin_Object=MibTableColumn
cfprMemoryRuntimeAvailableMin=_CfprMemoryRuntimeAvailableMin_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,7),_CfprMemoryRuntimeAvailableMin_Type())
cfprMemoryRuntimeAvailableMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeAvailableMin.setStatus(_A)
_CfprMemoryRuntimeCached_Type=Gauge32
_CfprMemoryRuntimeCached_Object=MibTableColumn
cfprMemoryRuntimeCached=_CfprMemoryRuntimeCached_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,8),_CfprMemoryRuntimeCached_Type())
cfprMemoryRuntimeCached.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeCached.setStatus(_A)
_CfprMemoryRuntimeCachedAvg_Type=Gauge32
_CfprMemoryRuntimeCachedAvg_Object=MibTableColumn
cfprMemoryRuntimeCachedAvg=_CfprMemoryRuntimeCachedAvg_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,9),_CfprMemoryRuntimeCachedAvg_Type())
cfprMemoryRuntimeCachedAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeCachedAvg.setStatus(_A)
_CfprMemoryRuntimeCachedMax_Type=Gauge32
_CfprMemoryRuntimeCachedMax_Object=MibTableColumn
cfprMemoryRuntimeCachedMax=_CfprMemoryRuntimeCachedMax_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,10),_CfprMemoryRuntimeCachedMax_Type())
cfprMemoryRuntimeCachedMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeCachedMax.setStatus(_A)
_CfprMemoryRuntimeCachedMin_Type=Gauge32
_CfprMemoryRuntimeCachedMin_Object=MibTableColumn
cfprMemoryRuntimeCachedMin=_CfprMemoryRuntimeCachedMin_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,11),_CfprMemoryRuntimeCachedMin_Type())
cfprMemoryRuntimeCachedMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeCachedMin.setStatus(_A)
_CfprMemoryRuntimeIntervals_Type=Gauge32
_CfprMemoryRuntimeIntervals_Object=MibTableColumn
cfprMemoryRuntimeIntervals=_CfprMemoryRuntimeIntervals_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,12),_CfprMemoryRuntimeIntervals_Type())
cfprMemoryRuntimeIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeIntervals.setStatus(_A)
_CfprMemoryRuntimeSuspect_Type=TruthValue
_CfprMemoryRuntimeSuspect_Object=MibTableColumn
cfprMemoryRuntimeSuspect=_CfprMemoryRuntimeSuspect_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,13),_CfprMemoryRuntimeSuspect_Type())
cfprMemoryRuntimeSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeSuspect.setStatus(_A)
_CfprMemoryRuntimeThresholded_Type=CfprMemoryRuntimeThresholded
_CfprMemoryRuntimeThresholded_Object=MibTableColumn
cfprMemoryRuntimeThresholded=_CfprMemoryRuntimeThresholded_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,14),_CfprMemoryRuntimeThresholded_Type())
cfprMemoryRuntimeThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeThresholded.setStatus(_A)
_CfprMemoryRuntimeTimeCollected_Type=DateAndTime
_CfprMemoryRuntimeTimeCollected_Object=MibTableColumn
cfprMemoryRuntimeTimeCollected=_CfprMemoryRuntimeTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,15),_CfprMemoryRuntimeTimeCollected_Type())
cfprMemoryRuntimeTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeTimeCollected.setStatus(_A)
_CfprMemoryRuntimeTotal_Type=Gauge32
_CfprMemoryRuntimeTotal_Object=MibTableColumn
cfprMemoryRuntimeTotal=_CfprMemoryRuntimeTotal_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,16),_CfprMemoryRuntimeTotal_Type())
cfprMemoryRuntimeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeTotal.setStatus(_A)
_CfprMemoryRuntimeTotalAvg_Type=Gauge32
_CfprMemoryRuntimeTotalAvg_Object=MibTableColumn
cfprMemoryRuntimeTotalAvg=_CfprMemoryRuntimeTotalAvg_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,17),_CfprMemoryRuntimeTotalAvg_Type())
cfprMemoryRuntimeTotalAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeTotalAvg.setStatus(_A)
_CfprMemoryRuntimeTotalMax_Type=Gauge32
_CfprMemoryRuntimeTotalMax_Object=MibTableColumn
cfprMemoryRuntimeTotalMax=_CfprMemoryRuntimeTotalMax_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,18),_CfprMemoryRuntimeTotalMax_Type())
cfprMemoryRuntimeTotalMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeTotalMax.setStatus(_A)
_CfprMemoryRuntimeTotalMin_Type=Gauge32
_CfprMemoryRuntimeTotalMin_Object=MibTableColumn
cfprMemoryRuntimeTotalMin=_CfprMemoryRuntimeTotalMin_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,19),_CfprMemoryRuntimeTotalMin_Type())
cfprMemoryRuntimeTotalMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeTotalMin.setStatus(_A)
_CfprMemoryRuntimeType_Type=CfprMemoryRuntimeType
_CfprMemoryRuntimeType_Object=MibTableColumn
cfprMemoryRuntimeType=_CfprMemoryRuntimeType_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,20),_CfprMemoryRuntimeType_Type())
cfprMemoryRuntimeType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeType.setStatus(_A)
_CfprMemoryRuntimeUpdate_Type=Gauge32
_CfprMemoryRuntimeUpdate_Object=MibTableColumn
cfprMemoryRuntimeUpdate=_CfprMemoryRuntimeUpdate_Object((1,3,6,1,4,1,9,9,826,1,50,9,1,21),_CfprMemoryRuntimeUpdate_Type())
cfprMemoryRuntimeUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeUpdate.setStatus(_A)
_CfprMemoryRuntimeHistTable_Object=MibTable
cfprMemoryRuntimeHistTable=_CfprMemoryRuntimeHistTable_Object((1,3,6,1,4,1,9,9,826,1,50,10))
if mibBuilder.loadTexts:cfprMemoryRuntimeHistTable.setStatus(_A)
_CfprMemoryRuntimeHistEntry_Object=MibTableRow
cfprMemoryRuntimeHistEntry=_CfprMemoryRuntimeHistEntry_Object((1,3,6,1,4,1,9,9,826,1,50,10,1))
cfprMemoryRuntimeHistEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cfprMemoryRuntimeHistEntry.setStatus(_A)
_CfprMemoryRuntimeHistInstanceId_Type=CfprManagedObjectId
_CfprMemoryRuntimeHistInstanceId_Object=MibTableColumn
cfprMemoryRuntimeHistInstanceId=_CfprMemoryRuntimeHistInstanceId_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,1),_CfprMemoryRuntimeHistInstanceId_Type())
cfprMemoryRuntimeHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistInstanceId.setStatus(_A)
_CfprMemoryRuntimeHistDn_Type=CfprManagedObjectDn
_CfprMemoryRuntimeHistDn_Object=MibTableColumn
cfprMemoryRuntimeHistDn=_CfprMemoryRuntimeHistDn_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,2),_CfprMemoryRuntimeHistDn_Type())
cfprMemoryRuntimeHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistDn.setStatus(_A)
_CfprMemoryRuntimeHistRn_Type=SnmpAdminString
_CfprMemoryRuntimeHistRn_Object=MibTableColumn
cfprMemoryRuntimeHistRn=_CfprMemoryRuntimeHistRn_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,3),_CfprMemoryRuntimeHistRn_Type())
cfprMemoryRuntimeHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistRn.setStatus(_A)
_CfprMemoryRuntimeHistAvailable_Type=Gauge32
_CfprMemoryRuntimeHistAvailable_Object=MibTableColumn
cfprMemoryRuntimeHistAvailable=_CfprMemoryRuntimeHistAvailable_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,4),_CfprMemoryRuntimeHistAvailable_Type())
cfprMemoryRuntimeHistAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistAvailable.setStatus(_A)
_CfprMemoryRuntimeHistAvailableAvg_Type=Gauge32
_CfprMemoryRuntimeHistAvailableAvg_Object=MibTableColumn
cfprMemoryRuntimeHistAvailableAvg=_CfprMemoryRuntimeHistAvailableAvg_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,5),_CfprMemoryRuntimeHistAvailableAvg_Type())
cfprMemoryRuntimeHistAvailableAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistAvailableAvg.setStatus(_A)
_CfprMemoryRuntimeHistAvailableMax_Type=Gauge32
_CfprMemoryRuntimeHistAvailableMax_Object=MibTableColumn
cfprMemoryRuntimeHistAvailableMax=_CfprMemoryRuntimeHistAvailableMax_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,6),_CfprMemoryRuntimeHistAvailableMax_Type())
cfprMemoryRuntimeHistAvailableMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistAvailableMax.setStatus(_A)
_CfprMemoryRuntimeHistAvailableMin_Type=Gauge32
_CfprMemoryRuntimeHistAvailableMin_Object=MibTableColumn
cfprMemoryRuntimeHistAvailableMin=_CfprMemoryRuntimeHistAvailableMin_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,7),_CfprMemoryRuntimeHistAvailableMin_Type())
cfprMemoryRuntimeHistAvailableMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistAvailableMin.setStatus(_A)
_CfprMemoryRuntimeHistCached_Type=Gauge32
_CfprMemoryRuntimeHistCached_Object=MibTableColumn
cfprMemoryRuntimeHistCached=_CfprMemoryRuntimeHistCached_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,8),_CfprMemoryRuntimeHistCached_Type())
cfprMemoryRuntimeHistCached.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistCached.setStatus(_A)
_CfprMemoryRuntimeHistCachedAvg_Type=Gauge32
_CfprMemoryRuntimeHistCachedAvg_Object=MibTableColumn
cfprMemoryRuntimeHistCachedAvg=_CfprMemoryRuntimeHistCachedAvg_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,9),_CfprMemoryRuntimeHistCachedAvg_Type())
cfprMemoryRuntimeHistCachedAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistCachedAvg.setStatus(_A)
_CfprMemoryRuntimeHistCachedMax_Type=Gauge32
_CfprMemoryRuntimeHistCachedMax_Object=MibTableColumn
cfprMemoryRuntimeHistCachedMax=_CfprMemoryRuntimeHistCachedMax_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,10),_CfprMemoryRuntimeHistCachedMax_Type())
cfprMemoryRuntimeHistCachedMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistCachedMax.setStatus(_A)
_CfprMemoryRuntimeHistCachedMin_Type=Gauge32
_CfprMemoryRuntimeHistCachedMin_Object=MibTableColumn
cfprMemoryRuntimeHistCachedMin=_CfprMemoryRuntimeHistCachedMin_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,11),_CfprMemoryRuntimeHistCachedMin_Type())
cfprMemoryRuntimeHistCachedMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistCachedMin.setStatus(_A)
_CfprMemoryRuntimeHistId_Type=Unsigned64
_CfprMemoryRuntimeHistId_Object=MibTableColumn
cfprMemoryRuntimeHistId=_CfprMemoryRuntimeHistId_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,12),_CfprMemoryRuntimeHistId_Type())
cfprMemoryRuntimeHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistId.setStatus(_A)
_CfprMemoryRuntimeHistMostRecent_Type=TruthValue
_CfprMemoryRuntimeHistMostRecent_Object=MibTableColumn
cfprMemoryRuntimeHistMostRecent=_CfprMemoryRuntimeHistMostRecent_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,13),_CfprMemoryRuntimeHistMostRecent_Type())
cfprMemoryRuntimeHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistMostRecent.setStatus(_A)
_CfprMemoryRuntimeHistSuspect_Type=TruthValue
_CfprMemoryRuntimeHistSuspect_Object=MibTableColumn
cfprMemoryRuntimeHistSuspect=_CfprMemoryRuntimeHistSuspect_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,14),_CfprMemoryRuntimeHistSuspect_Type())
cfprMemoryRuntimeHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistSuspect.setStatus(_A)
_CfprMemoryRuntimeHistThresholded_Type=CfprMemoryRuntimeHistThresholded
_CfprMemoryRuntimeHistThresholded_Object=MibTableColumn
cfprMemoryRuntimeHistThresholded=_CfprMemoryRuntimeHistThresholded_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,15),_CfprMemoryRuntimeHistThresholded_Type())
cfprMemoryRuntimeHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistThresholded.setStatus(_A)
_CfprMemoryRuntimeHistTimeCollected_Type=DateAndTime
_CfprMemoryRuntimeHistTimeCollected_Object=MibTableColumn
cfprMemoryRuntimeHistTimeCollected=_CfprMemoryRuntimeHistTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,16),_CfprMemoryRuntimeHistTimeCollected_Type())
cfprMemoryRuntimeHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistTimeCollected.setStatus(_A)
_CfprMemoryRuntimeHistTotal_Type=Gauge32
_CfprMemoryRuntimeHistTotal_Object=MibTableColumn
cfprMemoryRuntimeHistTotal=_CfprMemoryRuntimeHistTotal_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,17),_CfprMemoryRuntimeHistTotal_Type())
cfprMemoryRuntimeHistTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistTotal.setStatus(_A)
_CfprMemoryRuntimeHistTotalAvg_Type=Gauge32
_CfprMemoryRuntimeHistTotalAvg_Object=MibTableColumn
cfprMemoryRuntimeHistTotalAvg=_CfprMemoryRuntimeHistTotalAvg_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,18),_CfprMemoryRuntimeHistTotalAvg_Type())
cfprMemoryRuntimeHistTotalAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistTotalAvg.setStatus(_A)
_CfprMemoryRuntimeHistTotalMax_Type=Gauge32
_CfprMemoryRuntimeHistTotalMax_Object=MibTableColumn
cfprMemoryRuntimeHistTotalMax=_CfprMemoryRuntimeHistTotalMax_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,19),_CfprMemoryRuntimeHistTotalMax_Type())
cfprMemoryRuntimeHistTotalMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistTotalMax.setStatus(_A)
_CfprMemoryRuntimeHistTotalMin_Type=Gauge32
_CfprMemoryRuntimeHistTotalMin_Object=MibTableColumn
cfprMemoryRuntimeHistTotalMin=_CfprMemoryRuntimeHistTotalMin_Object((1,3,6,1,4,1,9,9,826,1,50,10,1,20),_CfprMemoryRuntimeHistTotalMin_Type())
cfprMemoryRuntimeHistTotalMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryRuntimeHistTotalMin.setStatus(_A)
_CfprMemoryUnitTable_Object=MibTable
cfprMemoryUnitTable=_CfprMemoryUnitTable_Object((1,3,6,1,4,1,9,9,826,1,50,11))
if mibBuilder.loadTexts:cfprMemoryUnitTable.setStatus(_A)
_CfprMemoryUnitEntry_Object=MibTableRow
cfprMemoryUnitEntry=_CfprMemoryUnitEntry_Object((1,3,6,1,4,1,9,9,826,1,50,11,1))
cfprMemoryUnitEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cfprMemoryUnitEntry.setStatus(_A)
_CfprMemoryUnitInstanceId_Type=CfprManagedObjectId
_CfprMemoryUnitInstanceId_Object=MibTableColumn
cfprMemoryUnitInstanceId=_CfprMemoryUnitInstanceId_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,1),_CfprMemoryUnitInstanceId_Type())
cfprMemoryUnitInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMemoryUnitInstanceId.setStatus(_A)
_CfprMemoryUnitDn_Type=CfprManagedObjectDn
_CfprMemoryUnitDn_Object=MibTableColumn
cfprMemoryUnitDn=_CfprMemoryUnitDn_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,2),_CfprMemoryUnitDn_Type())
cfprMemoryUnitDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitDn.setStatus(_A)
_CfprMemoryUnitRn_Type=SnmpAdminString
_CfprMemoryUnitRn_Object=MibTableColumn
cfprMemoryUnitRn=_CfprMemoryUnitRn_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,3),_CfprMemoryUnitRn_Type())
cfprMemoryUnitRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitRn.setStatus(_A)
_CfprMemoryUnitAdminState_Type=CfprMemoryAdminState
_CfprMemoryUnitAdminState_Object=MibTableColumn
cfprMemoryUnitAdminState=_CfprMemoryUnitAdminState_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,4),_CfprMemoryUnitAdminState_Type())
cfprMemoryUnitAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitAdminState.setStatus(_A)
_CfprMemoryUnitArray_Type=Gauge32
_CfprMemoryUnitArray_Object=MibTableColumn
cfprMemoryUnitArray=_CfprMemoryUnitArray_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,5),_CfprMemoryUnitArray_Type())
cfprMemoryUnitArray.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitArray.setStatus(_A)
_CfprMemoryUnitBank_Type=Gauge32
_CfprMemoryUnitBank_Object=MibTableColumn
cfprMemoryUnitBank=_CfprMemoryUnitBank_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,6),_CfprMemoryUnitBank_Type())
cfprMemoryUnitBank.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitBank.setStatus(_A)
_CfprMemoryUnitCapacity_Type=Gauge32
_CfprMemoryUnitCapacity_Object=MibTableColumn
cfprMemoryUnitCapacity=_CfprMemoryUnitCapacity_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,7),_CfprMemoryUnitCapacity_Type())
cfprMemoryUnitCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitCapacity.setStatus(_A)
_CfprMemoryUnitClock_Type=Gauge32
_CfprMemoryUnitClock_Object=MibTableColumn
cfprMemoryUnitClock=_CfprMemoryUnitClock_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,8),_CfprMemoryUnitClock_Type())
cfprMemoryUnitClock.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitClock.setStatus(_A)
_CfprMemoryUnitFormFactor_Type=CfprMemoryFormFactor
_CfprMemoryUnitFormFactor_Object=MibTableColumn
cfprMemoryUnitFormFactor=_CfprMemoryUnitFormFactor_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,9),_CfprMemoryUnitFormFactor_Type())
cfprMemoryUnitFormFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitFormFactor.setStatus(_A)
_CfprMemoryUnitId_Type=CfprMemoryUnitId
_CfprMemoryUnitId_Object=MibTableColumn
cfprMemoryUnitId=_CfprMemoryUnitId_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,10),_CfprMemoryUnitId_Type())
cfprMemoryUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitId.setStatus(_A)
_CfprMemoryUnitLatency_Type=Integer32
_CfprMemoryUnitLatency_Object=MibTableColumn
cfprMemoryUnitLatency=_CfprMemoryUnitLatency_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,11),_CfprMemoryUnitLatency_Type())
cfprMemoryUnitLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitLatency.setStatus(_A)
_CfprMemoryUnitLocation_Type=SnmpAdminString
_CfprMemoryUnitLocation_Object=MibTableColumn
cfprMemoryUnitLocation=_CfprMemoryUnitLocation_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,12),_CfprMemoryUnitLocation_Type())
cfprMemoryUnitLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitLocation.setStatus(_A)
_CfprMemoryUnitLocationDn_Type=SnmpAdminString
_CfprMemoryUnitLocationDn_Object=MibTableColumn
cfprMemoryUnitLocationDn=_CfprMemoryUnitLocationDn_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,13),_CfprMemoryUnitLocationDn_Type())
cfprMemoryUnitLocationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitLocationDn.setStatus(_A)
_CfprMemoryUnitModel_Type=SnmpAdminString
_CfprMemoryUnitModel_Object=MibTableColumn
cfprMemoryUnitModel=_CfprMemoryUnitModel_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,14),_CfprMemoryUnitModel_Type())
cfprMemoryUnitModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitModel.setStatus(_A)
_CfprMemoryUnitOperQualifier_Type=CfprMemoryIssues
_CfprMemoryUnitOperQualifier_Object=MibTableColumn
cfprMemoryUnitOperQualifier=_CfprMemoryUnitOperQualifier_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,15),_CfprMemoryUnitOperQualifier_Type())
cfprMemoryUnitOperQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitOperQualifier.setStatus(_A)
_CfprMemoryUnitOperQualifierReason_Type=SnmpAdminString
_CfprMemoryUnitOperQualifierReason_Object=MibTableColumn
cfprMemoryUnitOperQualifierReason=_CfprMemoryUnitOperQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,16),_CfprMemoryUnitOperQualifierReason_Type())
cfprMemoryUnitOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitOperQualifierReason.setStatus(_A)
_CfprMemoryUnitOperState_Type=CfprEquipmentOperability
_CfprMemoryUnitOperState_Object=MibTableColumn
cfprMemoryUnitOperState=_CfprMemoryUnitOperState_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,17),_CfprMemoryUnitOperState_Type())
cfprMemoryUnitOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitOperState.setStatus(_A)
_CfprMemoryUnitOperability_Type=CfprMemoryUnitOperability
_CfprMemoryUnitOperability_Object=MibTableColumn
cfprMemoryUnitOperability=_CfprMemoryUnitOperability_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,18),_CfprMemoryUnitOperability_Type())
cfprMemoryUnitOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitOperability.setStatus(_A)
_CfprMemoryUnitPerf_Type=CfprEquipmentSensorThresholdStatus
_CfprMemoryUnitPerf_Object=MibTableColumn
cfprMemoryUnitPerf=_CfprMemoryUnitPerf_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,19),_CfprMemoryUnitPerf_Type())
cfprMemoryUnitPerf.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitPerf.setStatus(_A)
_CfprMemoryUnitPower_Type=CfprEquipmentPowerState
_CfprMemoryUnitPower_Object=MibTableColumn
cfprMemoryUnitPower=_CfprMemoryUnitPower_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,20),_CfprMemoryUnitPower_Type())
cfprMemoryUnitPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitPower.setStatus(_A)
_CfprMemoryUnitPresence_Type=CfprEquipmentPresence
_CfprMemoryUnitPresence_Object=MibTableColumn
cfprMemoryUnitPresence=_CfprMemoryUnitPresence_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,21),_CfprMemoryUnitPresence_Type())
cfprMemoryUnitPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitPresence.setStatus(_A)
_CfprMemoryUnitRevision_Type=SnmpAdminString
_CfprMemoryUnitRevision_Object=MibTableColumn
cfprMemoryUnitRevision=_CfprMemoryUnitRevision_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,22),_CfprMemoryUnitRevision_Type())
cfprMemoryUnitRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitRevision.setStatus(_A)
_CfprMemoryUnitSerial_Type=SnmpAdminString
_CfprMemoryUnitSerial_Object=MibTableColumn
cfprMemoryUnitSerial=_CfprMemoryUnitSerial_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,23),_CfprMemoryUnitSerial_Type())
cfprMemoryUnitSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitSerial.setStatus(_A)
_CfprMemoryUnitSet_Type=Gauge32
_CfprMemoryUnitSet_Object=MibTableColumn
cfprMemoryUnitSet=_CfprMemoryUnitSet_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,24),_CfprMemoryUnitSet_Type())
cfprMemoryUnitSet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitSet.setStatus(_A)
_CfprMemoryUnitSpeed_Type=Gauge32
_CfprMemoryUnitSpeed_Object=MibTableColumn
cfprMemoryUnitSpeed=_CfprMemoryUnitSpeed_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,25),_CfprMemoryUnitSpeed_Type())
cfprMemoryUnitSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitSpeed.setStatus(_A)
_CfprMemoryUnitThermal_Type=CfprEquipmentSensorThresholdStatus
_CfprMemoryUnitThermal_Object=MibTableColumn
cfprMemoryUnitThermal=_CfprMemoryUnitThermal_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,26),_CfprMemoryUnitThermal_Type())
cfprMemoryUnitThermal.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitThermal.setStatus(_A)
_CfprMemoryUnitType_Type=CfprMemoryType
_CfprMemoryUnitType_Object=MibTableColumn
cfprMemoryUnitType=_CfprMemoryUnitType_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,27),_CfprMemoryUnitType_Type())
cfprMemoryUnitType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitType.setStatus(_A)
_CfprMemoryUnitVendor_Type=SnmpAdminString
_CfprMemoryUnitVendor_Object=MibTableColumn
cfprMemoryUnitVendor=_CfprMemoryUnitVendor_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,28),_CfprMemoryUnitVendor_Type())
cfprMemoryUnitVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitVendor.setStatus(_A)
_CfprMemoryUnitVisibility_Type=CfprMemoryVisibility
_CfprMemoryUnitVisibility_Object=MibTableColumn
cfprMemoryUnitVisibility=_CfprMemoryUnitVisibility_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,29),_CfprMemoryUnitVisibility_Type())
cfprMemoryUnitVisibility.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitVisibility.setStatus(_A)
_CfprMemoryUnitVoltage_Type=CfprEquipmentSensorThresholdStatus
_CfprMemoryUnitVoltage_Object=MibTableColumn
cfprMemoryUnitVoltage=_CfprMemoryUnitVoltage_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,30),_CfprMemoryUnitVoltage_Type())
cfprMemoryUnitVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitVoltage.setStatus(_A)
_CfprMemoryUnitWidth_Type=Gauge32
_CfprMemoryUnitWidth_Object=MibTableColumn
cfprMemoryUnitWidth=_CfprMemoryUnitWidth_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,31),_CfprMemoryUnitWidth_Type())
cfprMemoryUnitWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitWidth.setStatus(_A)
_CfprMemoryUnitVendorDescription_Type=SnmpAdminString
_CfprMemoryUnitVendorDescription_Object=MibTableColumn
cfprMemoryUnitVendorDescription=_CfprMemoryUnitVendorDescription_Object((1,3,6,1,4,1,9,9,826,1,50,11,1,32),_CfprMemoryUnitVendorDescription_Type())
cfprMemoryUnitVendorDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitVendorDescription.setStatus(_A)
_CfprMemoryUnitEnvStatsTable_Object=MibTable
cfprMemoryUnitEnvStatsTable=_CfprMemoryUnitEnvStatsTable_Object((1,3,6,1,4,1,9,9,826,1,50,12))
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsTable.setStatus(_A)
_CfprMemoryUnitEnvStatsEntry_Object=MibTableRow
cfprMemoryUnitEnvStatsEntry=_CfprMemoryUnitEnvStatsEntry_Object((1,3,6,1,4,1,9,9,826,1,50,12,1))
cfprMemoryUnitEnvStatsEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsEntry.setStatus(_A)
_CfprMemoryUnitEnvStatsInstanceId_Type=CfprManagedObjectId
_CfprMemoryUnitEnvStatsInstanceId_Object=MibTableColumn
cfprMemoryUnitEnvStatsInstanceId=_CfprMemoryUnitEnvStatsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,50,12,1,1),_CfprMemoryUnitEnvStatsInstanceId_Type())
cfprMemoryUnitEnvStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsInstanceId.setStatus(_A)
_CfprMemoryUnitEnvStatsDn_Type=CfprManagedObjectDn
_CfprMemoryUnitEnvStatsDn_Object=MibTableColumn
cfprMemoryUnitEnvStatsDn=_CfprMemoryUnitEnvStatsDn_Object((1,3,6,1,4,1,9,9,826,1,50,12,1,2),_CfprMemoryUnitEnvStatsDn_Type())
cfprMemoryUnitEnvStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsDn.setStatus(_A)
_CfprMemoryUnitEnvStatsRn_Type=SnmpAdminString
_CfprMemoryUnitEnvStatsRn_Object=MibTableColumn
cfprMemoryUnitEnvStatsRn=_CfprMemoryUnitEnvStatsRn_Object((1,3,6,1,4,1,9,9,826,1,50,12,1,3),_CfprMemoryUnitEnvStatsRn_Type())
cfprMemoryUnitEnvStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsRn.setStatus(_A)
_CfprMemoryUnitEnvStatsIntervals_Type=Gauge32
_CfprMemoryUnitEnvStatsIntervals_Object=MibTableColumn
cfprMemoryUnitEnvStatsIntervals=_CfprMemoryUnitEnvStatsIntervals_Object((1,3,6,1,4,1,9,9,826,1,50,12,1,4),_CfprMemoryUnitEnvStatsIntervals_Type())
cfprMemoryUnitEnvStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsIntervals.setStatus(_A)
_CfprMemoryUnitEnvStatsSuspect_Type=TruthValue
_CfprMemoryUnitEnvStatsSuspect_Object=MibTableColumn
cfprMemoryUnitEnvStatsSuspect=_CfprMemoryUnitEnvStatsSuspect_Object((1,3,6,1,4,1,9,9,826,1,50,12,1,5),_CfprMemoryUnitEnvStatsSuspect_Type())
cfprMemoryUnitEnvStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsSuspect.setStatus(_A)
_CfprMemoryUnitEnvStatsTemperature_Type=Integer32
_CfprMemoryUnitEnvStatsTemperature_Object=MibTableColumn
cfprMemoryUnitEnvStatsTemperature=_CfprMemoryUnitEnvStatsTemperature_Object((1,3,6,1,4,1,9,9,826,1,50,12,1,6),_CfprMemoryUnitEnvStatsTemperature_Type())
cfprMemoryUnitEnvStatsTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsTemperature.setStatus(_A)
_CfprMemoryUnitEnvStatsTemperatureAvg_Type=Integer32
_CfprMemoryUnitEnvStatsTemperatureAvg_Object=MibTableColumn
cfprMemoryUnitEnvStatsTemperatureAvg=_CfprMemoryUnitEnvStatsTemperatureAvg_Object((1,3,6,1,4,1,9,9,826,1,50,12,1,7),_CfprMemoryUnitEnvStatsTemperatureAvg_Type())
cfprMemoryUnitEnvStatsTemperatureAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsTemperatureAvg.setStatus(_A)
_CfprMemoryUnitEnvStatsTemperatureMax_Type=Integer32
_CfprMemoryUnitEnvStatsTemperatureMax_Object=MibTableColumn
cfprMemoryUnitEnvStatsTemperatureMax=_CfprMemoryUnitEnvStatsTemperatureMax_Object((1,3,6,1,4,1,9,9,826,1,50,12,1,8),_CfprMemoryUnitEnvStatsTemperatureMax_Type())
cfprMemoryUnitEnvStatsTemperatureMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsTemperatureMax.setStatus(_A)
_CfprMemoryUnitEnvStatsTemperatureMin_Type=Integer32
_CfprMemoryUnitEnvStatsTemperatureMin_Object=MibTableColumn
cfprMemoryUnitEnvStatsTemperatureMin=_CfprMemoryUnitEnvStatsTemperatureMin_Object((1,3,6,1,4,1,9,9,826,1,50,12,1,9),_CfprMemoryUnitEnvStatsTemperatureMin_Type())
cfprMemoryUnitEnvStatsTemperatureMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsTemperatureMin.setStatus(_A)
_CfprMemoryUnitEnvStatsThresholded_Type=CfprMemoryUnitEnvStatsThresholded
_CfprMemoryUnitEnvStatsThresholded_Object=MibTableColumn
cfprMemoryUnitEnvStatsThresholded=_CfprMemoryUnitEnvStatsThresholded_Object((1,3,6,1,4,1,9,9,826,1,50,12,1,10),_CfprMemoryUnitEnvStatsThresholded_Type())
cfprMemoryUnitEnvStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsThresholded.setStatus(_A)
_CfprMemoryUnitEnvStatsTimeCollected_Type=DateAndTime
_CfprMemoryUnitEnvStatsTimeCollected_Object=MibTableColumn
cfprMemoryUnitEnvStatsTimeCollected=_CfprMemoryUnitEnvStatsTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,50,12,1,11),_CfprMemoryUnitEnvStatsTimeCollected_Type())
cfprMemoryUnitEnvStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsTimeCollected.setStatus(_A)
_CfprMemoryUnitEnvStatsUpdate_Type=Gauge32
_CfprMemoryUnitEnvStatsUpdate_Object=MibTableColumn
cfprMemoryUnitEnvStatsUpdate=_CfprMemoryUnitEnvStatsUpdate_Object((1,3,6,1,4,1,9,9,826,1,50,12,1,12),_CfprMemoryUnitEnvStatsUpdate_Type())
cfprMemoryUnitEnvStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsUpdate.setStatus(_A)
_CfprMemoryUnitEnvStatsHistTable_Object=MibTable
cfprMemoryUnitEnvStatsHistTable=_CfprMemoryUnitEnvStatsHistTable_Object((1,3,6,1,4,1,9,9,826,1,50,13))
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsHistTable.setStatus(_A)
_CfprMemoryUnitEnvStatsHistEntry_Object=MibTableRow
cfprMemoryUnitEnvStatsHistEntry=_CfprMemoryUnitEnvStatsHistEntry_Object((1,3,6,1,4,1,9,9,826,1,50,13,1))
cfprMemoryUnitEnvStatsHistEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsHistEntry.setStatus(_A)
_CfprMemoryUnitEnvStatsHistInstanceId_Type=CfprManagedObjectId
_CfprMemoryUnitEnvStatsHistInstanceId_Object=MibTableColumn
cfprMemoryUnitEnvStatsHistInstanceId=_CfprMemoryUnitEnvStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,826,1,50,13,1,1),_CfprMemoryUnitEnvStatsHistInstanceId_Type())
cfprMemoryUnitEnvStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsHistInstanceId.setStatus(_A)
_CfprMemoryUnitEnvStatsHistDn_Type=CfprManagedObjectDn
_CfprMemoryUnitEnvStatsHistDn_Object=MibTableColumn
cfprMemoryUnitEnvStatsHistDn=_CfprMemoryUnitEnvStatsHistDn_Object((1,3,6,1,4,1,9,9,826,1,50,13,1,2),_CfprMemoryUnitEnvStatsHistDn_Type())
cfprMemoryUnitEnvStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsHistDn.setStatus(_A)
_CfprMemoryUnitEnvStatsHistRn_Type=SnmpAdminString
_CfprMemoryUnitEnvStatsHistRn_Object=MibTableColumn
cfprMemoryUnitEnvStatsHistRn=_CfprMemoryUnitEnvStatsHistRn_Object((1,3,6,1,4,1,9,9,826,1,50,13,1,3),_CfprMemoryUnitEnvStatsHistRn_Type())
cfprMemoryUnitEnvStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsHistRn.setStatus(_A)
_CfprMemoryUnitEnvStatsHistId_Type=Unsigned64
_CfprMemoryUnitEnvStatsHistId_Object=MibTableColumn
cfprMemoryUnitEnvStatsHistId=_CfprMemoryUnitEnvStatsHistId_Object((1,3,6,1,4,1,9,9,826,1,50,13,1,4),_CfprMemoryUnitEnvStatsHistId_Type())
cfprMemoryUnitEnvStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsHistId.setStatus(_A)
_CfprMemoryUnitEnvStatsHistMostRecent_Type=TruthValue
_CfprMemoryUnitEnvStatsHistMostRecent_Object=MibTableColumn
cfprMemoryUnitEnvStatsHistMostRecent=_CfprMemoryUnitEnvStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,826,1,50,13,1,5),_CfprMemoryUnitEnvStatsHistMostRecent_Type())
cfprMemoryUnitEnvStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsHistMostRecent.setStatus(_A)
_CfprMemoryUnitEnvStatsHistSuspect_Type=TruthValue
_CfprMemoryUnitEnvStatsHistSuspect_Object=MibTableColumn
cfprMemoryUnitEnvStatsHistSuspect=_CfprMemoryUnitEnvStatsHistSuspect_Object((1,3,6,1,4,1,9,9,826,1,50,13,1,6),_CfprMemoryUnitEnvStatsHistSuspect_Type())
cfprMemoryUnitEnvStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsHistSuspect.setStatus(_A)
_CfprMemoryUnitEnvStatsHistTemperature_Type=Integer32
_CfprMemoryUnitEnvStatsHistTemperature_Object=MibTableColumn
cfprMemoryUnitEnvStatsHistTemperature=_CfprMemoryUnitEnvStatsHistTemperature_Object((1,3,6,1,4,1,9,9,826,1,50,13,1,7),_CfprMemoryUnitEnvStatsHistTemperature_Type())
cfprMemoryUnitEnvStatsHistTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsHistTemperature.setStatus(_A)
_CfprMemoryUnitEnvStatsHistTemperatureAvg_Type=Integer32
_CfprMemoryUnitEnvStatsHistTemperatureAvg_Object=MibTableColumn
cfprMemoryUnitEnvStatsHistTemperatureAvg=_CfprMemoryUnitEnvStatsHistTemperatureAvg_Object((1,3,6,1,4,1,9,9,826,1,50,13,1,8),_CfprMemoryUnitEnvStatsHistTemperatureAvg_Type())
cfprMemoryUnitEnvStatsHistTemperatureAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsHistTemperatureAvg.setStatus(_A)
_CfprMemoryUnitEnvStatsHistTemperatureMax_Type=Integer32
_CfprMemoryUnitEnvStatsHistTemperatureMax_Object=MibTableColumn
cfprMemoryUnitEnvStatsHistTemperatureMax=_CfprMemoryUnitEnvStatsHistTemperatureMax_Object((1,3,6,1,4,1,9,9,826,1,50,13,1,9),_CfprMemoryUnitEnvStatsHistTemperatureMax_Type())
cfprMemoryUnitEnvStatsHistTemperatureMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsHistTemperatureMax.setStatus(_A)
_CfprMemoryUnitEnvStatsHistTemperatureMin_Type=Integer32
_CfprMemoryUnitEnvStatsHistTemperatureMin_Object=MibTableColumn
cfprMemoryUnitEnvStatsHistTemperatureMin=_CfprMemoryUnitEnvStatsHistTemperatureMin_Object((1,3,6,1,4,1,9,9,826,1,50,13,1,10),_CfprMemoryUnitEnvStatsHistTemperatureMin_Type())
cfprMemoryUnitEnvStatsHistTemperatureMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsHistTemperatureMin.setStatus(_A)
_CfprMemoryUnitEnvStatsHistThresholded_Type=CfprMemoryUnitEnvStatsHistThresholded
_CfprMemoryUnitEnvStatsHistThresholded_Object=MibTableColumn
cfprMemoryUnitEnvStatsHistThresholded=_CfprMemoryUnitEnvStatsHistThresholded_Object((1,3,6,1,4,1,9,9,826,1,50,13,1,11),_CfprMemoryUnitEnvStatsHistThresholded_Type())
cfprMemoryUnitEnvStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsHistThresholded.setStatus(_A)
_CfprMemoryUnitEnvStatsHistTimeCollected_Type=DateAndTime
_CfprMemoryUnitEnvStatsHistTimeCollected_Object=MibTableColumn
cfprMemoryUnitEnvStatsHistTimeCollected=_CfprMemoryUnitEnvStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,50,13,1,12),_CfprMemoryUnitEnvStatsHistTimeCollected_Type())
cfprMemoryUnitEnvStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMemoryUnitEnvStatsHistTimeCollected.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprMemoryObjects':cfprMemoryObjects,'cfprMemoryArrayTable':cfprMemoryArrayTable,'cfprMemoryArrayEntry':cfprMemoryArrayEntry,_E:cfprMemoryArrayInstanceId,'cfprMemoryArrayDn':cfprMemoryArrayDn,'cfprMemoryArrayRn':cfprMemoryArrayRn,'cfprMemoryArrayCpuId':cfprMemoryArrayCpuId,'cfprMemoryArrayCurrCapacity':cfprMemoryArrayCurrCapacity,'cfprMemoryArrayErrorCorrection':cfprMemoryArrayErrorCorrection,'cfprMemoryArrayId':cfprMemoryArrayId,'cfprMemoryArrayLocationDn':cfprMemoryArrayLocationDn,'cfprMemoryArrayMaxCapacity':cfprMemoryArrayMaxCapacity,'cfprMemoryArrayMaxDevices':cfprMemoryArrayMaxDevices,'cfprMemoryArrayModel':cfprMemoryArrayModel,'cfprMemoryArrayOperQualifierReason':cfprMemoryArrayOperQualifierReason,'cfprMemoryArrayOperState':cfprMemoryArrayOperState,'cfprMemoryArrayOperability':cfprMemoryArrayOperability,'cfprMemoryArrayPerf':cfprMemoryArrayPerf,'cfprMemoryArrayPopulated':cfprMemoryArrayPopulated,'cfprMemoryArrayPower':cfprMemoryArrayPower,'cfprMemoryArrayPresence':cfprMemoryArrayPresence,'cfprMemoryArrayRevision':cfprMemoryArrayRevision,'cfprMemoryArraySerial':cfprMemoryArraySerial,'cfprMemoryArrayThermal':cfprMemoryArrayThermal,'cfprMemoryArrayVendor':cfprMemoryArrayVendor,'cfprMemoryArrayVoltage':cfprMemoryArrayVoltage,'cfprMemoryArrayEnvStatsTable':cfprMemoryArrayEnvStatsTable,'cfprMemoryArrayEnvStatsEntry':cfprMemoryArrayEnvStatsEntry,_F:cfprMemoryArrayEnvStatsInstanceId,'cfprMemoryArrayEnvStatsDn':cfprMemoryArrayEnvStatsDn,'cfprMemoryArrayEnvStatsRn':cfprMemoryArrayEnvStatsRn,'cfprMemoryArrayEnvStatsInputCurrent':cfprMemoryArrayEnvStatsInputCurrent,'cfprMemoryArrayEnvStatsInputCurrentAvg':cfprMemoryArrayEnvStatsInputCurrentAvg,'cfprMemoryArrayEnvStatsInputCurrentMax':cfprMemoryArrayEnvStatsInputCurrentMax,'cfprMemoryArrayEnvStatsInputCurrentMin':cfprMemoryArrayEnvStatsInputCurrentMin,'cfprMemoryArrayEnvStatsIntervals':cfprMemoryArrayEnvStatsIntervals,'cfprMemoryArrayEnvStatsSuspect':cfprMemoryArrayEnvStatsSuspect,'cfprMemoryArrayEnvStatsThresholded':cfprMemoryArrayEnvStatsThresholded,'cfprMemoryArrayEnvStatsTimeCollected':cfprMemoryArrayEnvStatsTimeCollected,'cfprMemoryArrayEnvStatsUpdate':cfprMemoryArrayEnvStatsUpdate,'cfprMemoryArrayEnvStatsHistTable':cfprMemoryArrayEnvStatsHistTable,'cfprMemoryArrayEnvStatsHistEntry':cfprMemoryArrayEnvStatsHistEntry,_G:cfprMemoryArrayEnvStatsHistInstanceId,'cfprMemoryArrayEnvStatsHistDn':cfprMemoryArrayEnvStatsHistDn,'cfprMemoryArrayEnvStatsHistRn':cfprMemoryArrayEnvStatsHistRn,'cfprMemoryArrayEnvStatsHistId':cfprMemoryArrayEnvStatsHistId,'cfprMemoryArrayEnvStatsHistInputCurrent':cfprMemoryArrayEnvStatsHistInputCurrent,'cfprMemoryArrayEnvStatsHistInputCurrentAvg':cfprMemoryArrayEnvStatsHistInputCurrentAvg,'cfprMemoryArrayEnvStatsHistInputCurrentMax':cfprMemoryArrayEnvStatsHistInputCurrentMax,'cfprMemoryArrayEnvStatsHistInputCurrentMin':cfprMemoryArrayEnvStatsHistInputCurrentMin,'cfprMemoryArrayEnvStatsHistMostRecent':cfprMemoryArrayEnvStatsHistMostRecent,'cfprMemoryArrayEnvStatsHistSuspect':cfprMemoryArrayEnvStatsHistSuspect,'cfprMemoryArrayEnvStatsHistThresholded':cfprMemoryArrayEnvStatsHistThresholded,'cfprMemoryArrayEnvStatsHistTimeCollected':cfprMemoryArrayEnvStatsHistTimeCollected,'cfprMemoryBufferUnitTable':cfprMemoryBufferUnitTable,'cfprMemoryBufferUnitEntry':cfprMemoryBufferUnitEntry,_H:cfprMemoryBufferUnitInstanceId,'cfprMemoryBufferUnitDn':cfprMemoryBufferUnitDn,'cfprMemoryBufferUnitRn':cfprMemoryBufferUnitRn,'cfprMemoryBufferUnitId':cfprMemoryBufferUnitId,'cfprMemoryBufferUnitLocationDn':cfprMemoryBufferUnitLocationDn,'cfprMemoryBufferUnitModel':cfprMemoryBufferUnitModel,'cfprMemoryBufferUnitOperQualifierReason':cfprMemoryBufferUnitOperQualifierReason,'cfprMemoryBufferUnitOperState':cfprMemoryBufferUnitOperState,'cfprMemoryBufferUnitOperability':cfprMemoryBufferUnitOperability,'cfprMemoryBufferUnitPerf':cfprMemoryBufferUnitPerf,'cfprMemoryBufferUnitPower':cfprMemoryBufferUnitPower,'cfprMemoryBufferUnitPresence':cfprMemoryBufferUnitPresence,'cfprMemoryBufferUnitRevision':cfprMemoryBufferUnitRevision,'cfprMemoryBufferUnitSerial':cfprMemoryBufferUnitSerial,'cfprMemoryBufferUnitThermal':cfprMemoryBufferUnitThermal,'cfprMemoryBufferUnitVendor':cfprMemoryBufferUnitVendor,'cfprMemoryBufferUnitVoltage':cfprMemoryBufferUnitVoltage,'cfprMemoryBufferUnitEnvStatsTable':cfprMemoryBufferUnitEnvStatsTable,'cfprMemoryBufferUnitEnvStatsEntry':cfprMemoryBufferUnitEnvStatsEntry,_I:cfprMemoryBufferUnitEnvStatsInstanceId,'cfprMemoryBufferUnitEnvStatsDn':cfprMemoryBufferUnitEnvStatsDn,'cfprMemoryBufferUnitEnvStatsRn':cfprMemoryBufferUnitEnvStatsRn,'cfprMemoryBufferUnitEnvStatsIntervals':cfprMemoryBufferUnitEnvStatsIntervals,'cfprMemoryBufferUnitEnvStatsSuspect':cfprMemoryBufferUnitEnvStatsSuspect,'cfprMemoryBufferUnitEnvStatsTemperature':cfprMemoryBufferUnitEnvStatsTemperature,'cfprMemoryBufferUnitEnvStatsTemperatureAvg':cfprMemoryBufferUnitEnvStatsTemperatureAvg,'cfprMemoryBufferUnitEnvStatsTemperatureMax':cfprMemoryBufferUnitEnvStatsTemperatureMax,'cfprMemoryBufferUnitEnvStatsTemperatureMin':cfprMemoryBufferUnitEnvStatsTemperatureMin,'cfprMemoryBufferUnitEnvStatsThresholded':cfprMemoryBufferUnitEnvStatsThresholded,'cfprMemoryBufferUnitEnvStatsTimeCollected':cfprMemoryBufferUnitEnvStatsTimeCollected,'cfprMemoryBufferUnitEnvStatsUpdate':cfprMemoryBufferUnitEnvStatsUpdate,'cfprMemoryBufferUnitEnvStatsHistTable':cfprMemoryBufferUnitEnvStatsHistTable,'cfprMemoryBufferUnitEnvStatsHistEntry':cfprMemoryBufferUnitEnvStatsHistEntry,_J:cfprMemoryBufferUnitEnvStatsHistInstanceId,'cfprMemoryBufferUnitEnvStatsHistDn':cfprMemoryBufferUnitEnvStatsHistDn,'cfprMemoryBufferUnitEnvStatsHistRn':cfprMemoryBufferUnitEnvStatsHistRn,'cfprMemoryBufferUnitEnvStatsHistId':cfprMemoryBufferUnitEnvStatsHistId,'cfprMemoryBufferUnitEnvStatsHistMostRecent':cfprMemoryBufferUnitEnvStatsHistMostRecent,'cfprMemoryBufferUnitEnvStatsHistSuspect':cfprMemoryBufferUnitEnvStatsHistSuspect,'cfprMemoryBufferUnitEnvStatsHistTemperature':cfprMemoryBufferUnitEnvStatsHistTemperature,'cfprMemoryBufferUnitEnvStatsHistTemperatureAvg':cfprMemoryBufferUnitEnvStatsHistTemperatureAvg,'cfprMemoryBufferUnitEnvStatsHistTemperatureMax':cfprMemoryBufferUnitEnvStatsHistTemperatureMax,'cfprMemoryBufferUnitEnvStatsHistTemperatureMin':cfprMemoryBufferUnitEnvStatsHistTemperatureMin,'cfprMemoryBufferUnitEnvStatsHistThresholded':cfprMemoryBufferUnitEnvStatsHistThresholded,'cfprMemoryBufferUnitEnvStatsHistTimeCollected':cfprMemoryBufferUnitEnvStatsHistTimeCollected,'cfprMemoryErrorStatsTable':cfprMemoryErrorStatsTable,'cfprMemoryErrorStatsEntry':cfprMemoryErrorStatsEntry,_K:cfprMemoryErrorStatsInstanceId,'cfprMemoryErrorStatsDn':cfprMemoryErrorStatsDn,'cfprMemoryErrorStatsRn':cfprMemoryErrorStatsRn,'cfprMemoryErrorStatsAddressParityErrors':cfprMemoryErrorStatsAddressParityErrors,'cfprMemoryErrorStatsAddressParityErrors15Min':cfprMemoryErrorStatsAddressParityErrors15Min,'cfprMemoryErrorStatsAddressParityErrors15MinH':cfprMemoryErrorStatsAddressParityErrors15MinH,'cfprMemoryErrorStatsAddressParityErrors1Day':cfprMemoryErrorStatsAddressParityErrors1Day,'cfprMemoryErrorStatsAddressParityErrors1DayH':cfprMemoryErrorStatsAddressParityErrors1DayH,'cfprMemoryErrorStatsAddressParityErrors1Hour':cfprMemoryErrorStatsAddressParityErrors1Hour,'cfprMemoryErrorStatsAddressParityErrors1HourH':cfprMemoryErrorStatsAddressParityErrors1HourH,'cfprMemoryErrorStatsAddressParityErrors1Week':cfprMemoryErrorStatsAddressParityErrors1Week,'cfprMemoryErrorStatsAddressParityErrors1WeekH':cfprMemoryErrorStatsAddressParityErrors1WeekH,'cfprMemoryErrorStatsAddressParityErrors2Weeks':cfprMemoryErrorStatsAddressParityErrors2Weeks,'cfprMemoryErrorStatsAddressParityErrors2WeeksH':cfprMemoryErrorStatsAddressParityErrors2WeeksH,'cfprMemoryErrorStatsEccMultibitErrors':cfprMemoryErrorStatsEccMultibitErrors,'cfprMemoryErrorStatsEccMultibitErrors15Min':cfprMemoryErrorStatsEccMultibitErrors15Min,'cfprMemoryErrorStatsEccMultibitErrors15MinH':cfprMemoryErrorStatsEccMultibitErrors15MinH,'cfprMemoryErrorStatsEccMultibitErrors1Day':cfprMemoryErrorStatsEccMultibitErrors1Day,'cfprMemoryErrorStatsEccMultibitErrors1DayH':cfprMemoryErrorStatsEccMultibitErrors1DayH,'cfprMemoryErrorStatsEccMultibitErrors1Hour':cfprMemoryErrorStatsEccMultibitErrors1Hour,'cfprMemoryErrorStatsEccMultibitErrors1HourH':cfprMemoryErrorStatsEccMultibitErrors1HourH,'cfprMemoryErrorStatsEccMultibitErrors1Week':cfprMemoryErrorStatsEccMultibitErrors1Week,'cfprMemoryErrorStatsEccMultibitErrors1WeekH':cfprMemoryErrorStatsEccMultibitErrors1WeekH,'cfprMemoryErrorStatsEccMultibitErrors2Weeks':cfprMemoryErrorStatsEccMultibitErrors2Weeks,'cfprMemoryErrorStatsEccMultibitErrors2WeeksH':cfprMemoryErrorStatsEccMultibitErrors2WeeksH,'cfprMemoryErrorStatsEccSinglebitErrors':cfprMemoryErrorStatsEccSinglebitErrors,'cfprMemoryErrorStatsEccSinglebitErrors15Min':cfprMemoryErrorStatsEccSinglebitErrors15Min,'cfprMemoryErrorStatsEccSinglebitErrors15MinH':cfprMemoryErrorStatsEccSinglebitErrors15MinH,'cfprMemoryErrorStatsEccSinglebitErrors1Day':cfprMemoryErrorStatsEccSinglebitErrors1Day,'cfprMemoryErrorStatsEccSinglebitErrors1DayH':cfprMemoryErrorStatsEccSinglebitErrors1DayH,'cfprMemoryErrorStatsEccSinglebitErrors1Hour':cfprMemoryErrorStatsEccSinglebitErrors1Hour,'cfprMemoryErrorStatsEccSinglebitErrors1HourH':cfprMemoryErrorStatsEccSinglebitErrors1HourH,'cfprMemoryErrorStatsEccSinglebitErrors1Week':cfprMemoryErrorStatsEccSinglebitErrors1Week,'cfprMemoryErrorStatsEccSinglebitErrors1WeekH':cfprMemoryErrorStatsEccSinglebitErrors1WeekH,'cfprMemoryErrorStatsEccSinglebitErrors2Weeks':cfprMemoryErrorStatsEccSinglebitErrors2Weeks,'cfprMemoryErrorStatsEccSinglebitErrors2WeeksH':cfprMemoryErrorStatsEccSinglebitErrors2WeeksH,'cfprMemoryErrorStatsIntervals':cfprMemoryErrorStatsIntervals,'cfprMemoryErrorStatsMismatchErrors':cfprMemoryErrorStatsMismatchErrors,'cfprMemoryErrorStatsMismatchErrors15Min':cfprMemoryErrorStatsMismatchErrors15Min,'cfprMemoryErrorStatsMismatchErrors15MinH':cfprMemoryErrorStatsMismatchErrors15MinH,'cfprMemoryErrorStatsMismatchErrors1Day':cfprMemoryErrorStatsMismatchErrors1Day,'cfprMemoryErrorStatsMismatchErrors1DayH':cfprMemoryErrorStatsMismatchErrors1DayH,'cfprMemoryErrorStatsMismatchErrors1Hour':cfprMemoryErrorStatsMismatchErrors1Hour,'cfprMemoryErrorStatsMismatchErrors1HourH':cfprMemoryErrorStatsMismatchErrors1HourH,'cfprMemoryErrorStatsMismatchErrors1Week':cfprMemoryErrorStatsMismatchErrors1Week,'cfprMemoryErrorStatsMismatchErrors1WeekH':cfprMemoryErrorStatsMismatchErrors1WeekH,'cfprMemoryErrorStatsMismatchErrors2Weeks':cfprMemoryErrorStatsMismatchErrors2Weeks,'cfprMemoryErrorStatsMismatchErrors2WeeksH':cfprMemoryErrorStatsMismatchErrors2WeeksH,'cfprMemoryErrorStatsSuspect':cfprMemoryErrorStatsSuspect,'cfprMemoryErrorStatsThresholded':cfprMemoryErrorStatsThresholded,'cfprMemoryErrorStatsTimeCollected':cfprMemoryErrorStatsTimeCollected,'cfprMemoryErrorStatsUpdate':cfprMemoryErrorStatsUpdate,'cfprMemoryQualTable':cfprMemoryQualTable,'cfprMemoryQualEntry':cfprMemoryQualEntry,_L:cfprMemoryQualInstanceId,'cfprMemoryQualDn':cfprMemoryQualDn,'cfprMemoryQualRn':cfprMemoryQualRn,'cfprMemoryQualClock':cfprMemoryQualClock,'cfprMemoryQualLatency':cfprMemoryQualLatency,'cfprMemoryQualMaxCap':cfprMemoryQualMaxCap,'cfprMemoryQualMinCap':cfprMemoryQualMinCap,'cfprMemoryQualSpeed':cfprMemoryQualSpeed,'cfprMemoryQualUnits':cfprMemoryQualUnits,'cfprMemoryQualWidth':cfprMemoryQualWidth,'cfprMemoryRuntimeTable':cfprMemoryRuntimeTable,'cfprMemoryRuntimeEntry':cfprMemoryRuntimeEntry,_M:cfprMemoryRuntimeInstanceId,'cfprMemoryRuntimeDn':cfprMemoryRuntimeDn,'cfprMemoryRuntimeRn':cfprMemoryRuntimeRn,'cfprMemoryRuntimeAvailable':cfprMemoryRuntimeAvailable,'cfprMemoryRuntimeAvailableAvg':cfprMemoryRuntimeAvailableAvg,'cfprMemoryRuntimeAvailableMax':cfprMemoryRuntimeAvailableMax,'cfprMemoryRuntimeAvailableMin':cfprMemoryRuntimeAvailableMin,'cfprMemoryRuntimeCached':cfprMemoryRuntimeCached,'cfprMemoryRuntimeCachedAvg':cfprMemoryRuntimeCachedAvg,'cfprMemoryRuntimeCachedMax':cfprMemoryRuntimeCachedMax,'cfprMemoryRuntimeCachedMin':cfprMemoryRuntimeCachedMin,'cfprMemoryRuntimeIntervals':cfprMemoryRuntimeIntervals,'cfprMemoryRuntimeSuspect':cfprMemoryRuntimeSuspect,'cfprMemoryRuntimeThresholded':cfprMemoryRuntimeThresholded,'cfprMemoryRuntimeTimeCollected':cfprMemoryRuntimeTimeCollected,'cfprMemoryRuntimeTotal':cfprMemoryRuntimeTotal,'cfprMemoryRuntimeTotalAvg':cfprMemoryRuntimeTotalAvg,'cfprMemoryRuntimeTotalMax':cfprMemoryRuntimeTotalMax,'cfprMemoryRuntimeTotalMin':cfprMemoryRuntimeTotalMin,'cfprMemoryRuntimeType':cfprMemoryRuntimeType,'cfprMemoryRuntimeUpdate':cfprMemoryRuntimeUpdate,'cfprMemoryRuntimeHistTable':cfprMemoryRuntimeHistTable,'cfprMemoryRuntimeHistEntry':cfprMemoryRuntimeHistEntry,_N:cfprMemoryRuntimeHistInstanceId,'cfprMemoryRuntimeHistDn':cfprMemoryRuntimeHistDn,'cfprMemoryRuntimeHistRn':cfprMemoryRuntimeHistRn,'cfprMemoryRuntimeHistAvailable':cfprMemoryRuntimeHistAvailable,'cfprMemoryRuntimeHistAvailableAvg':cfprMemoryRuntimeHistAvailableAvg,'cfprMemoryRuntimeHistAvailableMax':cfprMemoryRuntimeHistAvailableMax,'cfprMemoryRuntimeHistAvailableMin':cfprMemoryRuntimeHistAvailableMin,'cfprMemoryRuntimeHistCached':cfprMemoryRuntimeHistCached,'cfprMemoryRuntimeHistCachedAvg':cfprMemoryRuntimeHistCachedAvg,'cfprMemoryRuntimeHistCachedMax':cfprMemoryRuntimeHistCachedMax,'cfprMemoryRuntimeHistCachedMin':cfprMemoryRuntimeHistCachedMin,'cfprMemoryRuntimeHistId':cfprMemoryRuntimeHistId,'cfprMemoryRuntimeHistMostRecent':cfprMemoryRuntimeHistMostRecent,'cfprMemoryRuntimeHistSuspect':cfprMemoryRuntimeHistSuspect,'cfprMemoryRuntimeHistThresholded':cfprMemoryRuntimeHistThresholded,'cfprMemoryRuntimeHistTimeCollected':cfprMemoryRuntimeHistTimeCollected,'cfprMemoryRuntimeHistTotal':cfprMemoryRuntimeHistTotal,'cfprMemoryRuntimeHistTotalAvg':cfprMemoryRuntimeHistTotalAvg,'cfprMemoryRuntimeHistTotalMax':cfprMemoryRuntimeHistTotalMax,'cfprMemoryRuntimeHistTotalMin':cfprMemoryRuntimeHistTotalMin,'cfprMemoryUnitTable':cfprMemoryUnitTable,'cfprMemoryUnitEntry':cfprMemoryUnitEntry,_O:cfprMemoryUnitInstanceId,'cfprMemoryUnitDn':cfprMemoryUnitDn,'cfprMemoryUnitRn':cfprMemoryUnitRn,'cfprMemoryUnitAdminState':cfprMemoryUnitAdminState,'cfprMemoryUnitArray':cfprMemoryUnitArray,'cfprMemoryUnitBank':cfprMemoryUnitBank,'cfprMemoryUnitCapacity':cfprMemoryUnitCapacity,'cfprMemoryUnitClock':cfprMemoryUnitClock,'cfprMemoryUnitFormFactor':cfprMemoryUnitFormFactor,'cfprMemoryUnitId':cfprMemoryUnitId,'cfprMemoryUnitLatency':cfprMemoryUnitLatency,'cfprMemoryUnitLocation':cfprMemoryUnitLocation,'cfprMemoryUnitLocationDn':cfprMemoryUnitLocationDn,'cfprMemoryUnitModel':cfprMemoryUnitModel,'cfprMemoryUnitOperQualifier':cfprMemoryUnitOperQualifier,'cfprMemoryUnitOperQualifierReason':cfprMemoryUnitOperQualifierReason,'cfprMemoryUnitOperState':cfprMemoryUnitOperState,'cfprMemoryUnitOperability':cfprMemoryUnitOperability,'cfprMemoryUnitPerf':cfprMemoryUnitPerf,'cfprMemoryUnitPower':cfprMemoryUnitPower,'cfprMemoryUnitPresence':cfprMemoryUnitPresence,'cfprMemoryUnitRevision':cfprMemoryUnitRevision,'cfprMemoryUnitSerial':cfprMemoryUnitSerial,'cfprMemoryUnitSet':cfprMemoryUnitSet,'cfprMemoryUnitSpeed':cfprMemoryUnitSpeed,'cfprMemoryUnitThermal':cfprMemoryUnitThermal,'cfprMemoryUnitType':cfprMemoryUnitType,'cfprMemoryUnitVendor':cfprMemoryUnitVendor,'cfprMemoryUnitVisibility':cfprMemoryUnitVisibility,'cfprMemoryUnitVoltage':cfprMemoryUnitVoltage,'cfprMemoryUnitWidth':cfprMemoryUnitWidth,'cfprMemoryUnitVendorDescription':cfprMemoryUnitVendorDescription,'cfprMemoryUnitEnvStatsTable':cfprMemoryUnitEnvStatsTable,'cfprMemoryUnitEnvStatsEntry':cfprMemoryUnitEnvStatsEntry,_P:cfprMemoryUnitEnvStatsInstanceId,'cfprMemoryUnitEnvStatsDn':cfprMemoryUnitEnvStatsDn,'cfprMemoryUnitEnvStatsRn':cfprMemoryUnitEnvStatsRn,'cfprMemoryUnitEnvStatsIntervals':cfprMemoryUnitEnvStatsIntervals,'cfprMemoryUnitEnvStatsSuspect':cfprMemoryUnitEnvStatsSuspect,'cfprMemoryUnitEnvStatsTemperature':cfprMemoryUnitEnvStatsTemperature,'cfprMemoryUnitEnvStatsTemperatureAvg':cfprMemoryUnitEnvStatsTemperatureAvg,'cfprMemoryUnitEnvStatsTemperatureMax':cfprMemoryUnitEnvStatsTemperatureMax,'cfprMemoryUnitEnvStatsTemperatureMin':cfprMemoryUnitEnvStatsTemperatureMin,'cfprMemoryUnitEnvStatsThresholded':cfprMemoryUnitEnvStatsThresholded,'cfprMemoryUnitEnvStatsTimeCollected':cfprMemoryUnitEnvStatsTimeCollected,'cfprMemoryUnitEnvStatsUpdate':cfprMemoryUnitEnvStatsUpdate,'cfprMemoryUnitEnvStatsHistTable':cfprMemoryUnitEnvStatsHistTable,'cfprMemoryUnitEnvStatsHistEntry':cfprMemoryUnitEnvStatsHistEntry,_Q:cfprMemoryUnitEnvStatsHistInstanceId,'cfprMemoryUnitEnvStatsHistDn':cfprMemoryUnitEnvStatsHistDn,'cfprMemoryUnitEnvStatsHistRn':cfprMemoryUnitEnvStatsHistRn,'cfprMemoryUnitEnvStatsHistId':cfprMemoryUnitEnvStatsHistId,'cfprMemoryUnitEnvStatsHistMostRecent':cfprMemoryUnitEnvStatsHistMostRecent,'cfprMemoryUnitEnvStatsHistSuspect':cfprMemoryUnitEnvStatsHistSuspect,'cfprMemoryUnitEnvStatsHistTemperature':cfprMemoryUnitEnvStatsHistTemperature,'cfprMemoryUnitEnvStatsHistTemperatureAvg':cfprMemoryUnitEnvStatsHistTemperatureAvg,'cfprMemoryUnitEnvStatsHistTemperatureMax':cfprMemoryUnitEnvStatsHistTemperatureMax,'cfprMemoryUnitEnvStatsHistTemperatureMin':cfprMemoryUnitEnvStatsHistTemperatureMin,'cfprMemoryUnitEnvStatsHistThresholded':cfprMemoryUnitEnvStatsHistThresholded,'cfprMemoryUnitEnvStatsHistTimeCollected':cfprMemoryUnitEnvStatsHistTimeCollected})