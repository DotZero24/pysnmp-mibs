_Q='cucsMemoryUnitEnvStatsHistInstanceId'
_P='cucsMemoryUnitEnvStatsInstanceId'
_O='cucsMemoryUnitInstanceId'
_N='cucsMemoryRuntimeHistInstanceId'
_M='cucsMemoryRuntimeInstanceId'
_L='cucsMemoryQualInstanceId'
_K='cucsMemoryErrorStatsInstanceId'
_J='cucsMemoryBufferUnitEnvStatsHistInstanceId'
_I='cucsMemoryBufferUnitEnvStatsInstanceId'
_H='cucsMemoryBufferUnitInstanceId'
_G='cucsMemoryArrayEnvStatsHistInstanceId'
_F='cucsMemoryArrayEnvStatsInstanceId'
_E='cucsMemoryArrayInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-MEMORY-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsEquipmentOperability,CucsEquipmentPowerState,CucsEquipmentPresence,CucsEquipmentSensorThresholdStatus,CucsMemoryAdminState,CucsMemoryArrayEnvStatsHistThresholded,CucsMemoryArrayEnvStatsThresholded,CucsMemoryArrayId,CucsMemoryBufferUnitEnvStatsHistThresholded,CucsMemoryBufferUnitEnvStatsThresholded,CucsMemoryBufferUnitId,CucsMemoryErrorCorrection,CucsMemoryErrorStatsThresholded,CucsMemoryFormFactor,CucsMemoryIssues,CucsMemoryRuntimeHistThresholded,CucsMemoryRuntimeThresholded,CucsMemoryRuntimeType,CucsMemoryType,CucsMemoryUnitEnvStatsHistThresholded,CucsMemoryUnitEnvStatsThresholded,CucsMemoryUnitId,CucsMemoryUnitOperability,CucsMemoryVisibility=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsEquipmentOperability','CucsEquipmentPowerState','CucsEquipmentPresence','CucsEquipmentSensorThresholdStatus','CucsMemoryAdminState','CucsMemoryArrayEnvStatsHistThresholded','CucsMemoryArrayEnvStatsThresholded','CucsMemoryArrayId','CucsMemoryBufferUnitEnvStatsHistThresholded','CucsMemoryBufferUnitEnvStatsThresholded','CucsMemoryBufferUnitId','CucsMemoryErrorCorrection','CucsMemoryErrorStatsThresholded','CucsMemoryFormFactor','CucsMemoryIssues','CucsMemoryRuntimeHistThresholded','CucsMemoryRuntimeThresholded','CucsMemoryRuntimeType','CucsMemoryType','CucsMemoryUnitEnvStatsHistThresholded','CucsMemoryUnitEnvStatsThresholded','CucsMemoryUnitId','CucsMemoryUnitOperability','CucsMemoryVisibility')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsMemoryObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,30))
_CucsMemoryArrayTable_Object=MibTable
cucsMemoryArrayTable=_CucsMemoryArrayTable_Object((1,3,6,1,4,1,9,9,719,1,30,1))
if mibBuilder.loadTexts:cucsMemoryArrayTable.setStatus(_A)
_CucsMemoryArrayEntry_Object=MibTableRow
cucsMemoryArrayEntry=_CucsMemoryArrayEntry_Object((1,3,6,1,4,1,9,9,719,1,30,1,1))
cucsMemoryArrayEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsMemoryArrayEntry.setStatus(_A)
_CucsMemoryArrayInstanceId_Type=CucsManagedObjectId
_CucsMemoryArrayInstanceId_Object=MibTableColumn
cucsMemoryArrayInstanceId=_CucsMemoryArrayInstanceId_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,1),_CucsMemoryArrayInstanceId_Type())
cucsMemoryArrayInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMemoryArrayInstanceId.setStatus(_A)
_CucsMemoryArrayDn_Type=CucsManagedObjectDn
_CucsMemoryArrayDn_Object=MibTableColumn
cucsMemoryArrayDn=_CucsMemoryArrayDn_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,2),_CucsMemoryArrayDn_Type())
cucsMemoryArrayDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayDn.setStatus(_A)
_CucsMemoryArrayRn_Type=SnmpAdminString
_CucsMemoryArrayRn_Object=MibTableColumn
cucsMemoryArrayRn=_CucsMemoryArrayRn_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,3),_CucsMemoryArrayRn_Type())
cucsMemoryArrayRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayRn.setStatus(_A)
_CucsMemoryArrayCpuId_Type=Gauge32
_CucsMemoryArrayCpuId_Object=MibTableColumn
cucsMemoryArrayCpuId=_CucsMemoryArrayCpuId_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,4),_CucsMemoryArrayCpuId_Type())
cucsMemoryArrayCpuId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayCpuId.setStatus(_A)
_CucsMemoryArrayCurrCapacity_Type=Gauge32
_CucsMemoryArrayCurrCapacity_Object=MibTableColumn
cucsMemoryArrayCurrCapacity=_CucsMemoryArrayCurrCapacity_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,5),_CucsMemoryArrayCurrCapacity_Type())
cucsMemoryArrayCurrCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayCurrCapacity.setStatus(_A)
_CucsMemoryArrayErrorCorrection_Type=CucsMemoryErrorCorrection
_CucsMemoryArrayErrorCorrection_Object=MibTableColumn
cucsMemoryArrayErrorCorrection=_CucsMemoryArrayErrorCorrection_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,6),_CucsMemoryArrayErrorCorrection_Type())
cucsMemoryArrayErrorCorrection.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayErrorCorrection.setStatus(_A)
_CucsMemoryArrayId_Type=CucsMemoryArrayId
_CucsMemoryArrayId_Object=MibTableColumn
cucsMemoryArrayId=_CucsMemoryArrayId_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,7),_CucsMemoryArrayId_Type())
cucsMemoryArrayId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayId.setStatus(_A)
_CucsMemoryArrayMaxCapacity_Type=Gauge32
_CucsMemoryArrayMaxCapacity_Object=MibTableColumn
cucsMemoryArrayMaxCapacity=_CucsMemoryArrayMaxCapacity_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,8),_CucsMemoryArrayMaxCapacity_Type())
cucsMemoryArrayMaxCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayMaxCapacity.setStatus(_A)
_CucsMemoryArrayMaxDevices_Type=Gauge32
_CucsMemoryArrayMaxDevices_Object=MibTableColumn
cucsMemoryArrayMaxDevices=_CucsMemoryArrayMaxDevices_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,9),_CucsMemoryArrayMaxDevices_Type())
cucsMemoryArrayMaxDevices.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayMaxDevices.setStatus(_A)
_CucsMemoryArrayModel_Type=SnmpAdminString
_CucsMemoryArrayModel_Object=MibTableColumn
cucsMemoryArrayModel=_CucsMemoryArrayModel_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,10),_CucsMemoryArrayModel_Type())
cucsMemoryArrayModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayModel.setStatus(_A)
_CucsMemoryArrayOperState_Type=CucsEquipmentOperability
_CucsMemoryArrayOperState_Object=MibTableColumn
cucsMemoryArrayOperState=_CucsMemoryArrayOperState_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,11),_CucsMemoryArrayOperState_Type())
cucsMemoryArrayOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayOperState.setStatus(_A)
_CucsMemoryArrayOperability_Type=CucsEquipmentOperability
_CucsMemoryArrayOperability_Object=MibTableColumn
cucsMemoryArrayOperability=_CucsMemoryArrayOperability_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,12),_CucsMemoryArrayOperability_Type())
cucsMemoryArrayOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayOperability.setStatus(_A)
_CucsMemoryArrayPerf_Type=CucsEquipmentSensorThresholdStatus
_CucsMemoryArrayPerf_Object=MibTableColumn
cucsMemoryArrayPerf=_CucsMemoryArrayPerf_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,13),_CucsMemoryArrayPerf_Type())
cucsMemoryArrayPerf.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayPerf.setStatus(_A)
_CucsMemoryArrayPopulated_Type=Gauge32
_CucsMemoryArrayPopulated_Object=MibTableColumn
cucsMemoryArrayPopulated=_CucsMemoryArrayPopulated_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,14),_CucsMemoryArrayPopulated_Type())
cucsMemoryArrayPopulated.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayPopulated.setStatus(_A)
_CucsMemoryArrayPower_Type=CucsEquipmentPowerState
_CucsMemoryArrayPower_Object=MibTableColumn
cucsMemoryArrayPower=_CucsMemoryArrayPower_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,15),_CucsMemoryArrayPower_Type())
cucsMemoryArrayPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayPower.setStatus(_A)
_CucsMemoryArrayPresence_Type=CucsEquipmentPresence
_CucsMemoryArrayPresence_Object=MibTableColumn
cucsMemoryArrayPresence=_CucsMemoryArrayPresence_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,16),_CucsMemoryArrayPresence_Type())
cucsMemoryArrayPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayPresence.setStatus(_A)
_CucsMemoryArrayRevision_Type=SnmpAdminString
_CucsMemoryArrayRevision_Object=MibTableColumn
cucsMemoryArrayRevision=_CucsMemoryArrayRevision_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,17),_CucsMemoryArrayRevision_Type())
cucsMemoryArrayRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayRevision.setStatus(_A)
_CucsMemoryArraySerial_Type=SnmpAdminString
_CucsMemoryArraySerial_Object=MibTableColumn
cucsMemoryArraySerial=_CucsMemoryArraySerial_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,18),_CucsMemoryArraySerial_Type())
cucsMemoryArraySerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArraySerial.setStatus(_A)
_CucsMemoryArrayThermal_Type=CucsEquipmentSensorThresholdStatus
_CucsMemoryArrayThermal_Object=MibTableColumn
cucsMemoryArrayThermal=_CucsMemoryArrayThermal_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,19),_CucsMemoryArrayThermal_Type())
cucsMemoryArrayThermal.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayThermal.setStatus(_A)
_CucsMemoryArrayVendor_Type=SnmpAdminString
_CucsMemoryArrayVendor_Object=MibTableColumn
cucsMemoryArrayVendor=_CucsMemoryArrayVendor_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,20),_CucsMemoryArrayVendor_Type())
cucsMemoryArrayVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayVendor.setStatus(_A)
_CucsMemoryArrayVoltage_Type=CucsEquipmentSensorThresholdStatus
_CucsMemoryArrayVoltage_Object=MibTableColumn
cucsMemoryArrayVoltage=_CucsMemoryArrayVoltage_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,21),_CucsMemoryArrayVoltage_Type())
cucsMemoryArrayVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayVoltage.setStatus(_A)
_CucsMemoryArrayOperQualifierReason_Type=SnmpAdminString
_CucsMemoryArrayOperQualifierReason_Object=MibTableColumn
cucsMemoryArrayOperQualifierReason=_CucsMemoryArrayOperQualifierReason_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,22),_CucsMemoryArrayOperQualifierReason_Type())
cucsMemoryArrayOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayOperQualifierReason.setStatus(_A)
_CucsMemoryArrayLocationDn_Type=SnmpAdminString
_CucsMemoryArrayLocationDn_Object=MibTableColumn
cucsMemoryArrayLocationDn=_CucsMemoryArrayLocationDn_Object((1,3,6,1,4,1,9,9,719,1,30,1,1,23),_CucsMemoryArrayLocationDn_Type())
cucsMemoryArrayLocationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayLocationDn.setStatus(_A)
_CucsMemoryArrayEnvStatsTable_Object=MibTable
cucsMemoryArrayEnvStatsTable=_CucsMemoryArrayEnvStatsTable_Object((1,3,6,1,4,1,9,9,719,1,30,2))
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsTable.setStatus(_A)
_CucsMemoryArrayEnvStatsEntry_Object=MibTableRow
cucsMemoryArrayEnvStatsEntry=_CucsMemoryArrayEnvStatsEntry_Object((1,3,6,1,4,1,9,9,719,1,30,2,1))
cucsMemoryArrayEnvStatsEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsEntry.setStatus(_A)
_CucsMemoryArrayEnvStatsInstanceId_Type=CucsManagedObjectId
_CucsMemoryArrayEnvStatsInstanceId_Object=MibTableColumn
cucsMemoryArrayEnvStatsInstanceId=_CucsMemoryArrayEnvStatsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,30,2,1,1),_CucsMemoryArrayEnvStatsInstanceId_Type())
cucsMemoryArrayEnvStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsInstanceId.setStatus(_A)
_CucsMemoryArrayEnvStatsDn_Type=CucsManagedObjectDn
_CucsMemoryArrayEnvStatsDn_Object=MibTableColumn
cucsMemoryArrayEnvStatsDn=_CucsMemoryArrayEnvStatsDn_Object((1,3,6,1,4,1,9,9,719,1,30,2,1,2),_CucsMemoryArrayEnvStatsDn_Type())
cucsMemoryArrayEnvStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsDn.setStatus(_A)
_CucsMemoryArrayEnvStatsRn_Type=SnmpAdminString
_CucsMemoryArrayEnvStatsRn_Object=MibTableColumn
cucsMemoryArrayEnvStatsRn=_CucsMemoryArrayEnvStatsRn_Object((1,3,6,1,4,1,9,9,719,1,30,2,1,3),_CucsMemoryArrayEnvStatsRn_Type())
cucsMemoryArrayEnvStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsRn.setStatus(_A)
_CucsMemoryArrayEnvStatsInputCurrent_Type=Integer32
_CucsMemoryArrayEnvStatsInputCurrent_Object=MibTableColumn
cucsMemoryArrayEnvStatsInputCurrent=_CucsMemoryArrayEnvStatsInputCurrent_Object((1,3,6,1,4,1,9,9,719,1,30,2,1,4),_CucsMemoryArrayEnvStatsInputCurrent_Type())
cucsMemoryArrayEnvStatsInputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsInputCurrent.setStatus(_A)
_CucsMemoryArrayEnvStatsInputCurrentAvg_Type=Integer32
_CucsMemoryArrayEnvStatsInputCurrentAvg_Object=MibTableColumn
cucsMemoryArrayEnvStatsInputCurrentAvg=_CucsMemoryArrayEnvStatsInputCurrentAvg_Object((1,3,6,1,4,1,9,9,719,1,30,2,1,5),_CucsMemoryArrayEnvStatsInputCurrentAvg_Type())
cucsMemoryArrayEnvStatsInputCurrentAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsInputCurrentAvg.setStatus(_A)
_CucsMemoryArrayEnvStatsInputCurrentMax_Type=Integer32
_CucsMemoryArrayEnvStatsInputCurrentMax_Object=MibTableColumn
cucsMemoryArrayEnvStatsInputCurrentMax=_CucsMemoryArrayEnvStatsInputCurrentMax_Object((1,3,6,1,4,1,9,9,719,1,30,2,1,6),_CucsMemoryArrayEnvStatsInputCurrentMax_Type())
cucsMemoryArrayEnvStatsInputCurrentMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsInputCurrentMax.setStatus(_A)
_CucsMemoryArrayEnvStatsInputCurrentMin_Type=Integer32
_CucsMemoryArrayEnvStatsInputCurrentMin_Object=MibTableColumn
cucsMemoryArrayEnvStatsInputCurrentMin=_CucsMemoryArrayEnvStatsInputCurrentMin_Object((1,3,6,1,4,1,9,9,719,1,30,2,1,7),_CucsMemoryArrayEnvStatsInputCurrentMin_Type())
cucsMemoryArrayEnvStatsInputCurrentMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsInputCurrentMin.setStatus(_A)
_CucsMemoryArrayEnvStatsIntervals_Type=Gauge32
_CucsMemoryArrayEnvStatsIntervals_Object=MibTableColumn
cucsMemoryArrayEnvStatsIntervals=_CucsMemoryArrayEnvStatsIntervals_Object((1,3,6,1,4,1,9,9,719,1,30,2,1,8),_CucsMemoryArrayEnvStatsIntervals_Type())
cucsMemoryArrayEnvStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsIntervals.setStatus(_A)
_CucsMemoryArrayEnvStatsSuspect_Type=TruthValue
_CucsMemoryArrayEnvStatsSuspect_Object=MibTableColumn
cucsMemoryArrayEnvStatsSuspect=_CucsMemoryArrayEnvStatsSuspect_Object((1,3,6,1,4,1,9,9,719,1,30,2,1,9),_CucsMemoryArrayEnvStatsSuspect_Type())
cucsMemoryArrayEnvStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsSuspect.setStatus(_A)
_CucsMemoryArrayEnvStatsThresholded_Type=CucsMemoryArrayEnvStatsThresholded
_CucsMemoryArrayEnvStatsThresholded_Object=MibTableColumn
cucsMemoryArrayEnvStatsThresholded=_CucsMemoryArrayEnvStatsThresholded_Object((1,3,6,1,4,1,9,9,719,1,30,2,1,10),_CucsMemoryArrayEnvStatsThresholded_Type())
cucsMemoryArrayEnvStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsThresholded.setStatus(_A)
_CucsMemoryArrayEnvStatsTimeCollected_Type=DateAndTime
_CucsMemoryArrayEnvStatsTimeCollected_Object=MibTableColumn
cucsMemoryArrayEnvStatsTimeCollected=_CucsMemoryArrayEnvStatsTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,30,2,1,11),_CucsMemoryArrayEnvStatsTimeCollected_Type())
cucsMemoryArrayEnvStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsTimeCollected.setStatus(_A)
_CucsMemoryArrayEnvStatsUpdate_Type=Gauge32
_CucsMemoryArrayEnvStatsUpdate_Object=MibTableColumn
cucsMemoryArrayEnvStatsUpdate=_CucsMemoryArrayEnvStatsUpdate_Object((1,3,6,1,4,1,9,9,719,1,30,2,1,12),_CucsMemoryArrayEnvStatsUpdate_Type())
cucsMemoryArrayEnvStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsUpdate.setStatus(_A)
_CucsMemoryArrayEnvStatsHistTable_Object=MibTable
cucsMemoryArrayEnvStatsHistTable=_CucsMemoryArrayEnvStatsHistTable_Object((1,3,6,1,4,1,9,9,719,1,30,3))
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsHistTable.setStatus(_A)
_CucsMemoryArrayEnvStatsHistEntry_Object=MibTableRow
cucsMemoryArrayEnvStatsHistEntry=_CucsMemoryArrayEnvStatsHistEntry_Object((1,3,6,1,4,1,9,9,719,1,30,3,1))
cucsMemoryArrayEnvStatsHistEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsHistEntry.setStatus(_A)
_CucsMemoryArrayEnvStatsHistInstanceId_Type=CucsManagedObjectId
_CucsMemoryArrayEnvStatsHistInstanceId_Object=MibTableColumn
cucsMemoryArrayEnvStatsHistInstanceId=_CucsMemoryArrayEnvStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,719,1,30,3,1,1),_CucsMemoryArrayEnvStatsHistInstanceId_Type())
cucsMemoryArrayEnvStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsHistInstanceId.setStatus(_A)
_CucsMemoryArrayEnvStatsHistDn_Type=CucsManagedObjectDn
_CucsMemoryArrayEnvStatsHistDn_Object=MibTableColumn
cucsMemoryArrayEnvStatsHistDn=_CucsMemoryArrayEnvStatsHistDn_Object((1,3,6,1,4,1,9,9,719,1,30,3,1,2),_CucsMemoryArrayEnvStatsHistDn_Type())
cucsMemoryArrayEnvStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsHistDn.setStatus(_A)
_CucsMemoryArrayEnvStatsHistRn_Type=SnmpAdminString
_CucsMemoryArrayEnvStatsHistRn_Object=MibTableColumn
cucsMemoryArrayEnvStatsHistRn=_CucsMemoryArrayEnvStatsHistRn_Object((1,3,6,1,4,1,9,9,719,1,30,3,1,3),_CucsMemoryArrayEnvStatsHistRn_Type())
cucsMemoryArrayEnvStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsHistRn.setStatus(_A)
_CucsMemoryArrayEnvStatsHistId_Type=Unsigned64
_CucsMemoryArrayEnvStatsHistId_Object=MibTableColumn
cucsMemoryArrayEnvStatsHistId=_CucsMemoryArrayEnvStatsHistId_Object((1,3,6,1,4,1,9,9,719,1,30,3,1,4),_CucsMemoryArrayEnvStatsHistId_Type())
cucsMemoryArrayEnvStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsHistId.setStatus(_A)
_CucsMemoryArrayEnvStatsHistInputCurrent_Type=Integer32
_CucsMemoryArrayEnvStatsHistInputCurrent_Object=MibTableColumn
cucsMemoryArrayEnvStatsHistInputCurrent=_CucsMemoryArrayEnvStatsHistInputCurrent_Object((1,3,6,1,4,1,9,9,719,1,30,3,1,5),_CucsMemoryArrayEnvStatsHistInputCurrent_Type())
cucsMemoryArrayEnvStatsHistInputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsHistInputCurrent.setStatus(_A)
_CucsMemoryArrayEnvStatsHistInputCurrentAvg_Type=Integer32
_CucsMemoryArrayEnvStatsHistInputCurrentAvg_Object=MibTableColumn
cucsMemoryArrayEnvStatsHistInputCurrentAvg=_CucsMemoryArrayEnvStatsHistInputCurrentAvg_Object((1,3,6,1,4,1,9,9,719,1,30,3,1,6),_CucsMemoryArrayEnvStatsHistInputCurrentAvg_Type())
cucsMemoryArrayEnvStatsHistInputCurrentAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsHistInputCurrentAvg.setStatus(_A)
_CucsMemoryArrayEnvStatsHistInputCurrentMax_Type=Integer32
_CucsMemoryArrayEnvStatsHistInputCurrentMax_Object=MibTableColumn
cucsMemoryArrayEnvStatsHistInputCurrentMax=_CucsMemoryArrayEnvStatsHistInputCurrentMax_Object((1,3,6,1,4,1,9,9,719,1,30,3,1,7),_CucsMemoryArrayEnvStatsHistInputCurrentMax_Type())
cucsMemoryArrayEnvStatsHistInputCurrentMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsHistInputCurrentMax.setStatus(_A)
_CucsMemoryArrayEnvStatsHistInputCurrentMin_Type=Integer32
_CucsMemoryArrayEnvStatsHistInputCurrentMin_Object=MibTableColumn
cucsMemoryArrayEnvStatsHistInputCurrentMin=_CucsMemoryArrayEnvStatsHistInputCurrentMin_Object((1,3,6,1,4,1,9,9,719,1,30,3,1,8),_CucsMemoryArrayEnvStatsHistInputCurrentMin_Type())
cucsMemoryArrayEnvStatsHistInputCurrentMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsHistInputCurrentMin.setStatus(_A)
_CucsMemoryArrayEnvStatsHistMostRecent_Type=TruthValue
_CucsMemoryArrayEnvStatsHistMostRecent_Object=MibTableColumn
cucsMemoryArrayEnvStatsHistMostRecent=_CucsMemoryArrayEnvStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,719,1,30,3,1,9),_CucsMemoryArrayEnvStatsHistMostRecent_Type())
cucsMemoryArrayEnvStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsHistMostRecent.setStatus(_A)
_CucsMemoryArrayEnvStatsHistSuspect_Type=TruthValue
_CucsMemoryArrayEnvStatsHistSuspect_Object=MibTableColumn
cucsMemoryArrayEnvStatsHistSuspect=_CucsMemoryArrayEnvStatsHistSuspect_Object((1,3,6,1,4,1,9,9,719,1,30,3,1,10),_CucsMemoryArrayEnvStatsHistSuspect_Type())
cucsMemoryArrayEnvStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsHistSuspect.setStatus(_A)
_CucsMemoryArrayEnvStatsHistThresholded_Type=CucsMemoryArrayEnvStatsHistThresholded
_CucsMemoryArrayEnvStatsHistThresholded_Object=MibTableColumn
cucsMemoryArrayEnvStatsHistThresholded=_CucsMemoryArrayEnvStatsHistThresholded_Object((1,3,6,1,4,1,9,9,719,1,30,3,1,11),_CucsMemoryArrayEnvStatsHistThresholded_Type())
cucsMemoryArrayEnvStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsHistThresholded.setStatus(_A)
_CucsMemoryArrayEnvStatsHistTimeCollected_Type=DateAndTime
_CucsMemoryArrayEnvStatsHistTimeCollected_Object=MibTableColumn
cucsMemoryArrayEnvStatsHistTimeCollected=_CucsMemoryArrayEnvStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,30,3,1,12),_CucsMemoryArrayEnvStatsHistTimeCollected_Type())
cucsMemoryArrayEnvStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryArrayEnvStatsHistTimeCollected.setStatus(_A)
_CucsMemoryBufferUnitTable_Object=MibTable
cucsMemoryBufferUnitTable=_CucsMemoryBufferUnitTable_Object((1,3,6,1,4,1,9,9,719,1,30,4))
if mibBuilder.loadTexts:cucsMemoryBufferUnitTable.setStatus(_A)
_CucsMemoryBufferUnitEntry_Object=MibTableRow
cucsMemoryBufferUnitEntry=_CucsMemoryBufferUnitEntry_Object((1,3,6,1,4,1,9,9,719,1,30,4,1))
cucsMemoryBufferUnitEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsMemoryBufferUnitEntry.setStatus(_A)
_CucsMemoryBufferUnitInstanceId_Type=CucsManagedObjectId
_CucsMemoryBufferUnitInstanceId_Object=MibTableColumn
cucsMemoryBufferUnitInstanceId=_CucsMemoryBufferUnitInstanceId_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,1),_CucsMemoryBufferUnitInstanceId_Type())
cucsMemoryBufferUnitInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMemoryBufferUnitInstanceId.setStatus(_A)
_CucsMemoryBufferUnitDn_Type=CucsManagedObjectDn
_CucsMemoryBufferUnitDn_Object=MibTableColumn
cucsMemoryBufferUnitDn=_CucsMemoryBufferUnitDn_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,2),_CucsMemoryBufferUnitDn_Type())
cucsMemoryBufferUnitDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitDn.setStatus(_A)
_CucsMemoryBufferUnitRn_Type=SnmpAdminString
_CucsMemoryBufferUnitRn_Object=MibTableColumn
cucsMemoryBufferUnitRn=_CucsMemoryBufferUnitRn_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,3),_CucsMemoryBufferUnitRn_Type())
cucsMemoryBufferUnitRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitRn.setStatus(_A)
_CucsMemoryBufferUnitId_Type=CucsMemoryBufferUnitId
_CucsMemoryBufferUnitId_Object=MibTableColumn
cucsMemoryBufferUnitId=_CucsMemoryBufferUnitId_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,4),_CucsMemoryBufferUnitId_Type())
cucsMemoryBufferUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitId.setStatus(_A)
_CucsMemoryBufferUnitModel_Type=SnmpAdminString
_CucsMemoryBufferUnitModel_Object=MibTableColumn
cucsMemoryBufferUnitModel=_CucsMemoryBufferUnitModel_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,5),_CucsMemoryBufferUnitModel_Type())
cucsMemoryBufferUnitModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitModel.setStatus(_A)
_CucsMemoryBufferUnitOperState_Type=CucsEquipmentOperability
_CucsMemoryBufferUnitOperState_Object=MibTableColumn
cucsMemoryBufferUnitOperState=_CucsMemoryBufferUnitOperState_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,6),_CucsMemoryBufferUnitOperState_Type())
cucsMemoryBufferUnitOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitOperState.setStatus(_A)
_CucsMemoryBufferUnitOperability_Type=CucsEquipmentOperability
_CucsMemoryBufferUnitOperability_Object=MibTableColumn
cucsMemoryBufferUnitOperability=_CucsMemoryBufferUnitOperability_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,7),_CucsMemoryBufferUnitOperability_Type())
cucsMemoryBufferUnitOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitOperability.setStatus(_A)
_CucsMemoryBufferUnitPerf_Type=CucsEquipmentSensorThresholdStatus
_CucsMemoryBufferUnitPerf_Object=MibTableColumn
cucsMemoryBufferUnitPerf=_CucsMemoryBufferUnitPerf_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,8),_CucsMemoryBufferUnitPerf_Type())
cucsMemoryBufferUnitPerf.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitPerf.setStatus(_A)
_CucsMemoryBufferUnitPower_Type=CucsEquipmentPowerState
_CucsMemoryBufferUnitPower_Object=MibTableColumn
cucsMemoryBufferUnitPower=_CucsMemoryBufferUnitPower_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,9),_CucsMemoryBufferUnitPower_Type())
cucsMemoryBufferUnitPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitPower.setStatus(_A)
_CucsMemoryBufferUnitPresence_Type=CucsEquipmentPresence
_CucsMemoryBufferUnitPresence_Object=MibTableColumn
cucsMemoryBufferUnitPresence=_CucsMemoryBufferUnitPresence_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,10),_CucsMemoryBufferUnitPresence_Type())
cucsMemoryBufferUnitPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitPresence.setStatus(_A)
_CucsMemoryBufferUnitRevision_Type=SnmpAdminString
_CucsMemoryBufferUnitRevision_Object=MibTableColumn
cucsMemoryBufferUnitRevision=_CucsMemoryBufferUnitRevision_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,11),_CucsMemoryBufferUnitRevision_Type())
cucsMemoryBufferUnitRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitRevision.setStatus(_A)
_CucsMemoryBufferUnitSerial_Type=SnmpAdminString
_CucsMemoryBufferUnitSerial_Object=MibTableColumn
cucsMemoryBufferUnitSerial=_CucsMemoryBufferUnitSerial_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,12),_CucsMemoryBufferUnitSerial_Type())
cucsMemoryBufferUnitSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitSerial.setStatus(_A)
_CucsMemoryBufferUnitThermal_Type=CucsEquipmentSensorThresholdStatus
_CucsMemoryBufferUnitThermal_Object=MibTableColumn
cucsMemoryBufferUnitThermal=_CucsMemoryBufferUnitThermal_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,13),_CucsMemoryBufferUnitThermal_Type())
cucsMemoryBufferUnitThermal.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitThermal.setStatus(_A)
_CucsMemoryBufferUnitVendor_Type=SnmpAdminString
_CucsMemoryBufferUnitVendor_Object=MibTableColumn
cucsMemoryBufferUnitVendor=_CucsMemoryBufferUnitVendor_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,14),_CucsMemoryBufferUnitVendor_Type())
cucsMemoryBufferUnitVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitVendor.setStatus(_A)
_CucsMemoryBufferUnitVoltage_Type=CucsEquipmentSensorThresholdStatus
_CucsMemoryBufferUnitVoltage_Object=MibTableColumn
cucsMemoryBufferUnitVoltage=_CucsMemoryBufferUnitVoltage_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,15),_CucsMemoryBufferUnitVoltage_Type())
cucsMemoryBufferUnitVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitVoltage.setStatus(_A)
_CucsMemoryBufferUnitOperQualifierReason_Type=SnmpAdminString
_CucsMemoryBufferUnitOperQualifierReason_Object=MibTableColumn
cucsMemoryBufferUnitOperQualifierReason=_CucsMemoryBufferUnitOperQualifierReason_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,16),_CucsMemoryBufferUnitOperQualifierReason_Type())
cucsMemoryBufferUnitOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitOperQualifierReason.setStatus(_A)
_CucsMemoryBufferUnitLocationDn_Type=SnmpAdminString
_CucsMemoryBufferUnitLocationDn_Object=MibTableColumn
cucsMemoryBufferUnitLocationDn=_CucsMemoryBufferUnitLocationDn_Object((1,3,6,1,4,1,9,9,719,1,30,4,1,17),_CucsMemoryBufferUnitLocationDn_Type())
cucsMemoryBufferUnitLocationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitLocationDn.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsTable_Object=MibTable
cucsMemoryBufferUnitEnvStatsTable=_CucsMemoryBufferUnitEnvStatsTable_Object((1,3,6,1,4,1,9,9,719,1,30,5))
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsTable.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsEntry_Object=MibTableRow
cucsMemoryBufferUnitEnvStatsEntry=_CucsMemoryBufferUnitEnvStatsEntry_Object((1,3,6,1,4,1,9,9,719,1,30,5,1))
cucsMemoryBufferUnitEnvStatsEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsEntry.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsInstanceId_Type=CucsManagedObjectId
_CucsMemoryBufferUnitEnvStatsInstanceId_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsInstanceId=_CucsMemoryBufferUnitEnvStatsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,30,5,1,1),_CucsMemoryBufferUnitEnvStatsInstanceId_Type())
cucsMemoryBufferUnitEnvStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsInstanceId.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsDn_Type=CucsManagedObjectDn
_CucsMemoryBufferUnitEnvStatsDn_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsDn=_CucsMemoryBufferUnitEnvStatsDn_Object((1,3,6,1,4,1,9,9,719,1,30,5,1,2),_CucsMemoryBufferUnitEnvStatsDn_Type())
cucsMemoryBufferUnitEnvStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsDn.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsRn_Type=SnmpAdminString
_CucsMemoryBufferUnitEnvStatsRn_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsRn=_CucsMemoryBufferUnitEnvStatsRn_Object((1,3,6,1,4,1,9,9,719,1,30,5,1,3),_CucsMemoryBufferUnitEnvStatsRn_Type())
cucsMemoryBufferUnitEnvStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsRn.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsIntervals_Type=Gauge32
_CucsMemoryBufferUnitEnvStatsIntervals_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsIntervals=_CucsMemoryBufferUnitEnvStatsIntervals_Object((1,3,6,1,4,1,9,9,719,1,30,5,1,4),_CucsMemoryBufferUnitEnvStatsIntervals_Type())
cucsMemoryBufferUnitEnvStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsIntervals.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsSuspect_Type=TruthValue
_CucsMemoryBufferUnitEnvStatsSuspect_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsSuspect=_CucsMemoryBufferUnitEnvStatsSuspect_Object((1,3,6,1,4,1,9,9,719,1,30,5,1,5),_CucsMemoryBufferUnitEnvStatsSuspect_Type())
cucsMemoryBufferUnitEnvStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsSuspect.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsTemperature_Type=Integer32
_CucsMemoryBufferUnitEnvStatsTemperature_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsTemperature=_CucsMemoryBufferUnitEnvStatsTemperature_Object((1,3,6,1,4,1,9,9,719,1,30,5,1,6),_CucsMemoryBufferUnitEnvStatsTemperature_Type())
cucsMemoryBufferUnitEnvStatsTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsTemperature.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsTemperatureAvg_Type=Integer32
_CucsMemoryBufferUnitEnvStatsTemperatureAvg_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsTemperatureAvg=_CucsMemoryBufferUnitEnvStatsTemperatureAvg_Object((1,3,6,1,4,1,9,9,719,1,30,5,1,7),_CucsMemoryBufferUnitEnvStatsTemperatureAvg_Type())
cucsMemoryBufferUnitEnvStatsTemperatureAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsTemperatureAvg.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsTemperatureMax_Type=Integer32
_CucsMemoryBufferUnitEnvStatsTemperatureMax_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsTemperatureMax=_CucsMemoryBufferUnitEnvStatsTemperatureMax_Object((1,3,6,1,4,1,9,9,719,1,30,5,1,8),_CucsMemoryBufferUnitEnvStatsTemperatureMax_Type())
cucsMemoryBufferUnitEnvStatsTemperatureMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsTemperatureMax.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsTemperatureMin_Type=Integer32
_CucsMemoryBufferUnitEnvStatsTemperatureMin_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsTemperatureMin=_CucsMemoryBufferUnitEnvStatsTemperatureMin_Object((1,3,6,1,4,1,9,9,719,1,30,5,1,9),_CucsMemoryBufferUnitEnvStatsTemperatureMin_Type())
cucsMemoryBufferUnitEnvStatsTemperatureMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsTemperatureMin.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsThresholded_Type=CucsMemoryBufferUnitEnvStatsThresholded
_CucsMemoryBufferUnitEnvStatsThresholded_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsThresholded=_CucsMemoryBufferUnitEnvStatsThresholded_Object((1,3,6,1,4,1,9,9,719,1,30,5,1,10),_CucsMemoryBufferUnitEnvStatsThresholded_Type())
cucsMemoryBufferUnitEnvStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsThresholded.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsTimeCollected_Type=DateAndTime
_CucsMemoryBufferUnitEnvStatsTimeCollected_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsTimeCollected=_CucsMemoryBufferUnitEnvStatsTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,30,5,1,11),_CucsMemoryBufferUnitEnvStatsTimeCollected_Type())
cucsMemoryBufferUnitEnvStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsTimeCollected.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsUpdate_Type=Gauge32
_CucsMemoryBufferUnitEnvStatsUpdate_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsUpdate=_CucsMemoryBufferUnitEnvStatsUpdate_Object((1,3,6,1,4,1,9,9,719,1,30,5,1,12),_CucsMemoryBufferUnitEnvStatsUpdate_Type())
cucsMemoryBufferUnitEnvStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsUpdate.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsHistTable_Object=MibTable
cucsMemoryBufferUnitEnvStatsHistTable=_CucsMemoryBufferUnitEnvStatsHistTable_Object((1,3,6,1,4,1,9,9,719,1,30,6))
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsHistTable.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsHistEntry_Object=MibTableRow
cucsMemoryBufferUnitEnvStatsHistEntry=_CucsMemoryBufferUnitEnvStatsHistEntry_Object((1,3,6,1,4,1,9,9,719,1,30,6,1))
cucsMemoryBufferUnitEnvStatsHistEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsHistEntry.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsHistInstanceId_Type=CucsManagedObjectId
_CucsMemoryBufferUnitEnvStatsHistInstanceId_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsHistInstanceId=_CucsMemoryBufferUnitEnvStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,719,1,30,6,1,1),_CucsMemoryBufferUnitEnvStatsHistInstanceId_Type())
cucsMemoryBufferUnitEnvStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsHistInstanceId.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsHistDn_Type=CucsManagedObjectDn
_CucsMemoryBufferUnitEnvStatsHistDn_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsHistDn=_CucsMemoryBufferUnitEnvStatsHistDn_Object((1,3,6,1,4,1,9,9,719,1,30,6,1,2),_CucsMemoryBufferUnitEnvStatsHistDn_Type())
cucsMemoryBufferUnitEnvStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsHistDn.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsHistRn_Type=SnmpAdminString
_CucsMemoryBufferUnitEnvStatsHistRn_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsHistRn=_CucsMemoryBufferUnitEnvStatsHistRn_Object((1,3,6,1,4,1,9,9,719,1,30,6,1,3),_CucsMemoryBufferUnitEnvStatsHistRn_Type())
cucsMemoryBufferUnitEnvStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsHistRn.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsHistId_Type=Unsigned64
_CucsMemoryBufferUnitEnvStatsHistId_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsHistId=_CucsMemoryBufferUnitEnvStatsHistId_Object((1,3,6,1,4,1,9,9,719,1,30,6,1,4),_CucsMemoryBufferUnitEnvStatsHistId_Type())
cucsMemoryBufferUnitEnvStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsHistId.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsHistMostRecent_Type=TruthValue
_CucsMemoryBufferUnitEnvStatsHistMostRecent_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsHistMostRecent=_CucsMemoryBufferUnitEnvStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,719,1,30,6,1,5),_CucsMemoryBufferUnitEnvStatsHistMostRecent_Type())
cucsMemoryBufferUnitEnvStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsHistMostRecent.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsHistSuspect_Type=TruthValue
_CucsMemoryBufferUnitEnvStatsHistSuspect_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsHistSuspect=_CucsMemoryBufferUnitEnvStatsHistSuspect_Object((1,3,6,1,4,1,9,9,719,1,30,6,1,6),_CucsMemoryBufferUnitEnvStatsHistSuspect_Type())
cucsMemoryBufferUnitEnvStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsHistSuspect.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsHistTemperature_Type=Integer32
_CucsMemoryBufferUnitEnvStatsHistTemperature_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsHistTemperature=_CucsMemoryBufferUnitEnvStatsHistTemperature_Object((1,3,6,1,4,1,9,9,719,1,30,6,1,7),_CucsMemoryBufferUnitEnvStatsHistTemperature_Type())
cucsMemoryBufferUnitEnvStatsHistTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsHistTemperature.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsHistTemperatureAvg_Type=Integer32
_CucsMemoryBufferUnitEnvStatsHistTemperatureAvg_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsHistTemperatureAvg=_CucsMemoryBufferUnitEnvStatsHistTemperatureAvg_Object((1,3,6,1,4,1,9,9,719,1,30,6,1,8),_CucsMemoryBufferUnitEnvStatsHistTemperatureAvg_Type())
cucsMemoryBufferUnitEnvStatsHistTemperatureAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsHistTemperatureAvg.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsHistTemperatureMax_Type=Integer32
_CucsMemoryBufferUnitEnvStatsHistTemperatureMax_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsHistTemperatureMax=_CucsMemoryBufferUnitEnvStatsHistTemperatureMax_Object((1,3,6,1,4,1,9,9,719,1,30,6,1,9),_CucsMemoryBufferUnitEnvStatsHistTemperatureMax_Type())
cucsMemoryBufferUnitEnvStatsHistTemperatureMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsHistTemperatureMax.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsHistTemperatureMin_Type=Integer32
_CucsMemoryBufferUnitEnvStatsHistTemperatureMin_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsHistTemperatureMin=_CucsMemoryBufferUnitEnvStatsHistTemperatureMin_Object((1,3,6,1,4,1,9,9,719,1,30,6,1,10),_CucsMemoryBufferUnitEnvStatsHistTemperatureMin_Type())
cucsMemoryBufferUnitEnvStatsHistTemperatureMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsHistTemperatureMin.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsHistThresholded_Type=CucsMemoryBufferUnitEnvStatsHistThresholded
_CucsMemoryBufferUnitEnvStatsHistThresholded_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsHistThresholded=_CucsMemoryBufferUnitEnvStatsHistThresholded_Object((1,3,6,1,4,1,9,9,719,1,30,6,1,11),_CucsMemoryBufferUnitEnvStatsHistThresholded_Type())
cucsMemoryBufferUnitEnvStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsHistThresholded.setStatus(_A)
_CucsMemoryBufferUnitEnvStatsHistTimeCollected_Type=DateAndTime
_CucsMemoryBufferUnitEnvStatsHistTimeCollected_Object=MibTableColumn
cucsMemoryBufferUnitEnvStatsHistTimeCollected=_CucsMemoryBufferUnitEnvStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,30,6,1,12),_CucsMemoryBufferUnitEnvStatsHistTimeCollected_Type())
cucsMemoryBufferUnitEnvStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryBufferUnitEnvStatsHistTimeCollected.setStatus(_A)
_CucsMemoryErrorStatsTable_Object=MibTable
cucsMemoryErrorStatsTable=_CucsMemoryErrorStatsTable_Object((1,3,6,1,4,1,9,9,719,1,30,7))
if mibBuilder.loadTexts:cucsMemoryErrorStatsTable.setStatus(_A)
_CucsMemoryErrorStatsEntry_Object=MibTableRow
cucsMemoryErrorStatsEntry=_CucsMemoryErrorStatsEntry_Object((1,3,6,1,4,1,9,9,719,1,30,7,1))
cucsMemoryErrorStatsEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsMemoryErrorStatsEntry.setStatus(_A)
_CucsMemoryErrorStatsInstanceId_Type=CucsManagedObjectId
_CucsMemoryErrorStatsInstanceId_Object=MibTableColumn
cucsMemoryErrorStatsInstanceId=_CucsMemoryErrorStatsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,1),_CucsMemoryErrorStatsInstanceId_Type())
cucsMemoryErrorStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMemoryErrorStatsInstanceId.setStatus(_A)
_CucsMemoryErrorStatsDn_Type=CucsManagedObjectDn
_CucsMemoryErrorStatsDn_Object=MibTableColumn
cucsMemoryErrorStatsDn=_CucsMemoryErrorStatsDn_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,2),_CucsMemoryErrorStatsDn_Type())
cucsMemoryErrorStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsDn.setStatus(_A)
_CucsMemoryErrorStatsRn_Type=SnmpAdminString
_CucsMemoryErrorStatsRn_Object=MibTableColumn
cucsMemoryErrorStatsRn=_CucsMemoryErrorStatsRn_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,3),_CucsMemoryErrorStatsRn_Type())
cucsMemoryErrorStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsRn.setStatus(_A)
_CucsMemoryErrorStatsAddressParityErrors_Type=Counter32
_CucsMemoryErrorStatsAddressParityErrors_Object=MibTableColumn
cucsMemoryErrorStatsAddressParityErrors=_CucsMemoryErrorStatsAddressParityErrors_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,4),_CucsMemoryErrorStatsAddressParityErrors_Type())
cucsMemoryErrorStatsAddressParityErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsAddressParityErrors.setStatus(_A)
_CucsMemoryErrorStatsAddressParityErrors15Min_Type=Gauge32
_CucsMemoryErrorStatsAddressParityErrors15Min_Object=MibTableColumn
cucsMemoryErrorStatsAddressParityErrors15Min=_CucsMemoryErrorStatsAddressParityErrors15Min_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,5),_CucsMemoryErrorStatsAddressParityErrors15Min_Type())
cucsMemoryErrorStatsAddressParityErrors15Min.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsAddressParityErrors15Min.setStatus(_A)
_CucsMemoryErrorStatsAddressParityErrors15MinH_Type=Gauge32
_CucsMemoryErrorStatsAddressParityErrors15MinH_Object=MibTableColumn
cucsMemoryErrorStatsAddressParityErrors15MinH=_CucsMemoryErrorStatsAddressParityErrors15MinH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,6),_CucsMemoryErrorStatsAddressParityErrors15MinH_Type())
cucsMemoryErrorStatsAddressParityErrors15MinH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsAddressParityErrors15MinH.setStatus(_A)
_CucsMemoryErrorStatsAddressParityErrors1Day_Type=Gauge32
_CucsMemoryErrorStatsAddressParityErrors1Day_Object=MibTableColumn
cucsMemoryErrorStatsAddressParityErrors1Day=_CucsMemoryErrorStatsAddressParityErrors1Day_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,7),_CucsMemoryErrorStatsAddressParityErrors1Day_Type())
cucsMemoryErrorStatsAddressParityErrors1Day.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsAddressParityErrors1Day.setStatus(_A)
_CucsMemoryErrorStatsAddressParityErrors1DayH_Type=Gauge32
_CucsMemoryErrorStatsAddressParityErrors1DayH_Object=MibTableColumn
cucsMemoryErrorStatsAddressParityErrors1DayH=_CucsMemoryErrorStatsAddressParityErrors1DayH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,8),_CucsMemoryErrorStatsAddressParityErrors1DayH_Type())
cucsMemoryErrorStatsAddressParityErrors1DayH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsAddressParityErrors1DayH.setStatus(_A)
_CucsMemoryErrorStatsAddressParityErrors1Hour_Type=Gauge32
_CucsMemoryErrorStatsAddressParityErrors1Hour_Object=MibTableColumn
cucsMemoryErrorStatsAddressParityErrors1Hour=_CucsMemoryErrorStatsAddressParityErrors1Hour_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,9),_CucsMemoryErrorStatsAddressParityErrors1Hour_Type())
cucsMemoryErrorStatsAddressParityErrors1Hour.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsAddressParityErrors1Hour.setStatus(_A)
_CucsMemoryErrorStatsAddressParityErrors1HourH_Type=Gauge32
_CucsMemoryErrorStatsAddressParityErrors1HourH_Object=MibTableColumn
cucsMemoryErrorStatsAddressParityErrors1HourH=_CucsMemoryErrorStatsAddressParityErrors1HourH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,10),_CucsMemoryErrorStatsAddressParityErrors1HourH_Type())
cucsMemoryErrorStatsAddressParityErrors1HourH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsAddressParityErrors1HourH.setStatus(_A)
_CucsMemoryErrorStatsAddressParityErrors1Week_Type=Gauge32
_CucsMemoryErrorStatsAddressParityErrors1Week_Object=MibTableColumn
cucsMemoryErrorStatsAddressParityErrors1Week=_CucsMemoryErrorStatsAddressParityErrors1Week_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,11),_CucsMemoryErrorStatsAddressParityErrors1Week_Type())
cucsMemoryErrorStatsAddressParityErrors1Week.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsAddressParityErrors1Week.setStatus(_A)
_CucsMemoryErrorStatsAddressParityErrors1WeekH_Type=Gauge32
_CucsMemoryErrorStatsAddressParityErrors1WeekH_Object=MibTableColumn
cucsMemoryErrorStatsAddressParityErrors1WeekH=_CucsMemoryErrorStatsAddressParityErrors1WeekH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,12),_CucsMemoryErrorStatsAddressParityErrors1WeekH_Type())
cucsMemoryErrorStatsAddressParityErrors1WeekH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsAddressParityErrors1WeekH.setStatus(_A)
_CucsMemoryErrorStatsEccMultibitErrors_Type=Counter32
_CucsMemoryErrorStatsEccMultibitErrors_Object=MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors=_CucsMemoryErrorStatsEccMultibitErrors_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,13),_CucsMemoryErrorStatsEccMultibitErrors_Type())
cucsMemoryErrorStatsEccMultibitErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccMultibitErrors.setStatus(_A)
_CucsMemoryErrorStatsEccMultibitErrors15Min_Type=Gauge32
_CucsMemoryErrorStatsEccMultibitErrors15Min_Object=MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors15Min=_CucsMemoryErrorStatsEccMultibitErrors15Min_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,14),_CucsMemoryErrorStatsEccMultibitErrors15Min_Type())
cucsMemoryErrorStatsEccMultibitErrors15Min.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccMultibitErrors15Min.setStatus(_A)
_CucsMemoryErrorStatsEccMultibitErrors15MinH_Type=Gauge32
_CucsMemoryErrorStatsEccMultibitErrors15MinH_Object=MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors15MinH=_CucsMemoryErrorStatsEccMultibitErrors15MinH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,15),_CucsMemoryErrorStatsEccMultibitErrors15MinH_Type())
cucsMemoryErrorStatsEccMultibitErrors15MinH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccMultibitErrors15MinH.setStatus(_A)
_CucsMemoryErrorStatsEccMultibitErrors1Day_Type=Gauge32
_CucsMemoryErrorStatsEccMultibitErrors1Day_Object=MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors1Day=_CucsMemoryErrorStatsEccMultibitErrors1Day_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,16),_CucsMemoryErrorStatsEccMultibitErrors1Day_Type())
cucsMemoryErrorStatsEccMultibitErrors1Day.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccMultibitErrors1Day.setStatus(_A)
_CucsMemoryErrorStatsEccMultibitErrors1DayH_Type=Gauge32
_CucsMemoryErrorStatsEccMultibitErrors1DayH_Object=MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors1DayH=_CucsMemoryErrorStatsEccMultibitErrors1DayH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,17),_CucsMemoryErrorStatsEccMultibitErrors1DayH_Type())
cucsMemoryErrorStatsEccMultibitErrors1DayH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccMultibitErrors1DayH.setStatus(_A)
_CucsMemoryErrorStatsEccMultibitErrors1Hour_Type=Gauge32
_CucsMemoryErrorStatsEccMultibitErrors1Hour_Object=MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors1Hour=_CucsMemoryErrorStatsEccMultibitErrors1Hour_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,18),_CucsMemoryErrorStatsEccMultibitErrors1Hour_Type())
cucsMemoryErrorStatsEccMultibitErrors1Hour.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccMultibitErrors1Hour.setStatus(_A)
_CucsMemoryErrorStatsEccMultibitErrors1HourH_Type=Gauge32
_CucsMemoryErrorStatsEccMultibitErrors1HourH_Object=MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors1HourH=_CucsMemoryErrorStatsEccMultibitErrors1HourH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,19),_CucsMemoryErrorStatsEccMultibitErrors1HourH_Type())
cucsMemoryErrorStatsEccMultibitErrors1HourH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccMultibitErrors1HourH.setStatus(_A)
_CucsMemoryErrorStatsEccMultibitErrors1Week_Type=Gauge32
_CucsMemoryErrorStatsEccMultibitErrors1Week_Object=MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors1Week=_CucsMemoryErrorStatsEccMultibitErrors1Week_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,20),_CucsMemoryErrorStatsEccMultibitErrors1Week_Type())
cucsMemoryErrorStatsEccMultibitErrors1Week.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccMultibitErrors1Week.setStatus(_A)
_CucsMemoryErrorStatsEccMultibitErrors1WeekH_Type=Gauge32
_CucsMemoryErrorStatsEccMultibitErrors1WeekH_Object=MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors1WeekH=_CucsMemoryErrorStatsEccMultibitErrors1WeekH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,21),_CucsMemoryErrorStatsEccMultibitErrors1WeekH_Type())
cucsMemoryErrorStatsEccMultibitErrors1WeekH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccMultibitErrors1WeekH.setStatus(_A)
_CucsMemoryErrorStatsEccSinglebitErrors_Type=Counter32
_CucsMemoryErrorStatsEccSinglebitErrors_Object=MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors=_CucsMemoryErrorStatsEccSinglebitErrors_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,22),_CucsMemoryErrorStatsEccSinglebitErrors_Type())
cucsMemoryErrorStatsEccSinglebitErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccSinglebitErrors.setStatus(_A)
_CucsMemoryErrorStatsEccSinglebitErrors15Min_Type=Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors15Min_Object=MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors15Min=_CucsMemoryErrorStatsEccSinglebitErrors15Min_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,23),_CucsMemoryErrorStatsEccSinglebitErrors15Min_Type())
cucsMemoryErrorStatsEccSinglebitErrors15Min.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccSinglebitErrors15Min.setStatus(_A)
_CucsMemoryErrorStatsEccSinglebitErrors15MinH_Type=Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors15MinH_Object=MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors15MinH=_CucsMemoryErrorStatsEccSinglebitErrors15MinH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,24),_CucsMemoryErrorStatsEccSinglebitErrors15MinH_Type())
cucsMemoryErrorStatsEccSinglebitErrors15MinH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccSinglebitErrors15MinH.setStatus(_A)
_CucsMemoryErrorStatsEccSinglebitErrors1Day_Type=Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors1Day_Object=MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors1Day=_CucsMemoryErrorStatsEccSinglebitErrors1Day_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,25),_CucsMemoryErrorStatsEccSinglebitErrors1Day_Type())
cucsMemoryErrorStatsEccSinglebitErrors1Day.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccSinglebitErrors1Day.setStatus(_A)
_CucsMemoryErrorStatsEccSinglebitErrors1DayH_Type=Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors1DayH_Object=MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors1DayH=_CucsMemoryErrorStatsEccSinglebitErrors1DayH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,26),_CucsMemoryErrorStatsEccSinglebitErrors1DayH_Type())
cucsMemoryErrorStatsEccSinglebitErrors1DayH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccSinglebitErrors1DayH.setStatus(_A)
_CucsMemoryErrorStatsEccSinglebitErrors1Hour_Type=Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors1Hour_Object=MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors1Hour=_CucsMemoryErrorStatsEccSinglebitErrors1Hour_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,27),_CucsMemoryErrorStatsEccSinglebitErrors1Hour_Type())
cucsMemoryErrorStatsEccSinglebitErrors1Hour.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccSinglebitErrors1Hour.setStatus(_A)
_CucsMemoryErrorStatsEccSinglebitErrors1HourH_Type=Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors1HourH_Object=MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors1HourH=_CucsMemoryErrorStatsEccSinglebitErrors1HourH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,28),_CucsMemoryErrorStatsEccSinglebitErrors1HourH_Type())
cucsMemoryErrorStatsEccSinglebitErrors1HourH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccSinglebitErrors1HourH.setStatus(_A)
_CucsMemoryErrorStatsEccSinglebitErrors1Week_Type=Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors1Week_Object=MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors1Week=_CucsMemoryErrorStatsEccSinglebitErrors1Week_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,29),_CucsMemoryErrorStatsEccSinglebitErrors1Week_Type())
cucsMemoryErrorStatsEccSinglebitErrors1Week.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccSinglebitErrors1Week.setStatus(_A)
_CucsMemoryErrorStatsEccSinglebitErrors1WeekH_Type=Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors1WeekH_Object=MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors1WeekH=_CucsMemoryErrorStatsEccSinglebitErrors1WeekH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,30),_CucsMemoryErrorStatsEccSinglebitErrors1WeekH_Type())
cucsMemoryErrorStatsEccSinglebitErrors1WeekH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccSinglebitErrors1WeekH.setStatus(_A)
_CucsMemoryErrorStatsIntervals_Type=Gauge32
_CucsMemoryErrorStatsIntervals_Object=MibTableColumn
cucsMemoryErrorStatsIntervals=_CucsMemoryErrorStatsIntervals_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,31),_CucsMemoryErrorStatsIntervals_Type())
cucsMemoryErrorStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsIntervals.setStatus(_A)
_CucsMemoryErrorStatsMismatchErrors_Type=Counter32
_CucsMemoryErrorStatsMismatchErrors_Object=MibTableColumn
cucsMemoryErrorStatsMismatchErrors=_CucsMemoryErrorStatsMismatchErrors_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,32),_CucsMemoryErrorStatsMismatchErrors_Type())
cucsMemoryErrorStatsMismatchErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsMismatchErrors.setStatus(_A)
_CucsMemoryErrorStatsMismatchErrors15Min_Type=Gauge32
_CucsMemoryErrorStatsMismatchErrors15Min_Object=MibTableColumn
cucsMemoryErrorStatsMismatchErrors15Min=_CucsMemoryErrorStatsMismatchErrors15Min_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,33),_CucsMemoryErrorStatsMismatchErrors15Min_Type())
cucsMemoryErrorStatsMismatchErrors15Min.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsMismatchErrors15Min.setStatus(_A)
_CucsMemoryErrorStatsMismatchErrors15MinH_Type=Gauge32
_CucsMemoryErrorStatsMismatchErrors15MinH_Object=MibTableColumn
cucsMemoryErrorStatsMismatchErrors15MinH=_CucsMemoryErrorStatsMismatchErrors15MinH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,34),_CucsMemoryErrorStatsMismatchErrors15MinH_Type())
cucsMemoryErrorStatsMismatchErrors15MinH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsMismatchErrors15MinH.setStatus(_A)
_CucsMemoryErrorStatsMismatchErrors1Day_Type=Gauge32
_CucsMemoryErrorStatsMismatchErrors1Day_Object=MibTableColumn
cucsMemoryErrorStatsMismatchErrors1Day=_CucsMemoryErrorStatsMismatchErrors1Day_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,35),_CucsMemoryErrorStatsMismatchErrors1Day_Type())
cucsMemoryErrorStatsMismatchErrors1Day.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsMismatchErrors1Day.setStatus(_A)
_CucsMemoryErrorStatsMismatchErrors1DayH_Type=Gauge32
_CucsMemoryErrorStatsMismatchErrors1DayH_Object=MibTableColumn
cucsMemoryErrorStatsMismatchErrors1DayH=_CucsMemoryErrorStatsMismatchErrors1DayH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,36),_CucsMemoryErrorStatsMismatchErrors1DayH_Type())
cucsMemoryErrorStatsMismatchErrors1DayH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsMismatchErrors1DayH.setStatus(_A)
_CucsMemoryErrorStatsMismatchErrors1Hour_Type=Gauge32
_CucsMemoryErrorStatsMismatchErrors1Hour_Object=MibTableColumn
cucsMemoryErrorStatsMismatchErrors1Hour=_CucsMemoryErrorStatsMismatchErrors1Hour_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,37),_CucsMemoryErrorStatsMismatchErrors1Hour_Type())
cucsMemoryErrorStatsMismatchErrors1Hour.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsMismatchErrors1Hour.setStatus(_A)
_CucsMemoryErrorStatsMismatchErrors1HourH_Type=Gauge32
_CucsMemoryErrorStatsMismatchErrors1HourH_Object=MibTableColumn
cucsMemoryErrorStatsMismatchErrors1HourH=_CucsMemoryErrorStatsMismatchErrors1HourH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,38),_CucsMemoryErrorStatsMismatchErrors1HourH_Type())
cucsMemoryErrorStatsMismatchErrors1HourH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsMismatchErrors1HourH.setStatus(_A)
_CucsMemoryErrorStatsMismatchErrors1Week_Type=Gauge32
_CucsMemoryErrorStatsMismatchErrors1Week_Object=MibTableColumn
cucsMemoryErrorStatsMismatchErrors1Week=_CucsMemoryErrorStatsMismatchErrors1Week_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,39),_CucsMemoryErrorStatsMismatchErrors1Week_Type())
cucsMemoryErrorStatsMismatchErrors1Week.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsMismatchErrors1Week.setStatus(_A)
_CucsMemoryErrorStatsMismatchErrors1WeekH_Type=Gauge32
_CucsMemoryErrorStatsMismatchErrors1WeekH_Object=MibTableColumn
cucsMemoryErrorStatsMismatchErrors1WeekH=_CucsMemoryErrorStatsMismatchErrors1WeekH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,40),_CucsMemoryErrorStatsMismatchErrors1WeekH_Type())
cucsMemoryErrorStatsMismatchErrors1WeekH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsMismatchErrors1WeekH.setStatus(_A)
_CucsMemoryErrorStatsSuspect_Type=TruthValue
_CucsMemoryErrorStatsSuspect_Object=MibTableColumn
cucsMemoryErrorStatsSuspect=_CucsMemoryErrorStatsSuspect_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,41),_CucsMemoryErrorStatsSuspect_Type())
cucsMemoryErrorStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsSuspect.setStatus(_A)
_CucsMemoryErrorStatsThresholded_Type=CucsMemoryErrorStatsThresholded
_CucsMemoryErrorStatsThresholded_Object=MibTableColumn
cucsMemoryErrorStatsThresholded=_CucsMemoryErrorStatsThresholded_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,42),_CucsMemoryErrorStatsThresholded_Type())
cucsMemoryErrorStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsThresholded.setStatus(_A)
_CucsMemoryErrorStatsTimeCollected_Type=DateAndTime
_CucsMemoryErrorStatsTimeCollected_Object=MibTableColumn
cucsMemoryErrorStatsTimeCollected=_CucsMemoryErrorStatsTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,43),_CucsMemoryErrorStatsTimeCollected_Type())
cucsMemoryErrorStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsTimeCollected.setStatus(_A)
_CucsMemoryErrorStatsUpdate_Type=Gauge32
_CucsMemoryErrorStatsUpdate_Object=MibTableColumn
cucsMemoryErrorStatsUpdate=_CucsMemoryErrorStatsUpdate_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,44),_CucsMemoryErrorStatsUpdate_Type())
cucsMemoryErrorStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsUpdate.setStatus(_A)
_CucsMemoryErrorStatsAddressParityErrors2Weeks_Type=Gauge32
_CucsMemoryErrorStatsAddressParityErrors2Weeks_Object=MibTableColumn
cucsMemoryErrorStatsAddressParityErrors2Weeks=_CucsMemoryErrorStatsAddressParityErrors2Weeks_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,45),_CucsMemoryErrorStatsAddressParityErrors2Weeks_Type())
cucsMemoryErrorStatsAddressParityErrors2Weeks.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsAddressParityErrors2Weeks.setStatus(_A)
_CucsMemoryErrorStatsAddressParityErrors2WeeksH_Type=Gauge32
_CucsMemoryErrorStatsAddressParityErrors2WeeksH_Object=MibTableColumn
cucsMemoryErrorStatsAddressParityErrors2WeeksH=_CucsMemoryErrorStatsAddressParityErrors2WeeksH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,46),_CucsMemoryErrorStatsAddressParityErrors2WeeksH_Type())
cucsMemoryErrorStatsAddressParityErrors2WeeksH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsAddressParityErrors2WeeksH.setStatus(_A)
_CucsMemoryErrorStatsEccMultibitErrors2Weeks_Type=Gauge32
_CucsMemoryErrorStatsEccMultibitErrors2Weeks_Object=MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors2Weeks=_CucsMemoryErrorStatsEccMultibitErrors2Weeks_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,47),_CucsMemoryErrorStatsEccMultibitErrors2Weeks_Type())
cucsMemoryErrorStatsEccMultibitErrors2Weeks.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccMultibitErrors2Weeks.setStatus(_A)
_CucsMemoryErrorStatsEccMultibitErrors2WeeksH_Type=Gauge32
_CucsMemoryErrorStatsEccMultibitErrors2WeeksH_Object=MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors2WeeksH=_CucsMemoryErrorStatsEccMultibitErrors2WeeksH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,48),_CucsMemoryErrorStatsEccMultibitErrors2WeeksH_Type())
cucsMemoryErrorStatsEccMultibitErrors2WeeksH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccMultibitErrors2WeeksH.setStatus(_A)
_CucsMemoryErrorStatsEccSinglebitErrors2Weeks_Type=Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors2Weeks_Object=MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors2Weeks=_CucsMemoryErrorStatsEccSinglebitErrors2Weeks_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,49),_CucsMemoryErrorStatsEccSinglebitErrors2Weeks_Type())
cucsMemoryErrorStatsEccSinglebitErrors2Weeks.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccSinglebitErrors2Weeks.setStatus(_A)
_CucsMemoryErrorStatsEccSinglebitErrors2WeeksH_Type=Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors2WeeksH_Object=MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors2WeeksH=_CucsMemoryErrorStatsEccSinglebitErrors2WeeksH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,50),_CucsMemoryErrorStatsEccSinglebitErrors2WeeksH_Type())
cucsMemoryErrorStatsEccSinglebitErrors2WeeksH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsEccSinglebitErrors2WeeksH.setStatus(_A)
_CucsMemoryErrorStatsMismatchErrors2Weeks_Type=Gauge32
_CucsMemoryErrorStatsMismatchErrors2Weeks_Object=MibTableColumn
cucsMemoryErrorStatsMismatchErrors2Weeks=_CucsMemoryErrorStatsMismatchErrors2Weeks_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,51),_CucsMemoryErrorStatsMismatchErrors2Weeks_Type())
cucsMemoryErrorStatsMismatchErrors2Weeks.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsMismatchErrors2Weeks.setStatus(_A)
_CucsMemoryErrorStatsMismatchErrors2WeeksH_Type=Gauge32
_CucsMemoryErrorStatsMismatchErrors2WeeksH_Object=MibTableColumn
cucsMemoryErrorStatsMismatchErrors2WeeksH=_CucsMemoryErrorStatsMismatchErrors2WeeksH_Object((1,3,6,1,4,1,9,9,719,1,30,7,1,52),_CucsMemoryErrorStatsMismatchErrors2WeeksH_Type())
cucsMemoryErrorStatsMismatchErrors2WeeksH.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryErrorStatsMismatchErrors2WeeksH.setStatus(_A)
_CucsMemoryQualTable_Object=MibTable
cucsMemoryQualTable=_CucsMemoryQualTable_Object((1,3,6,1,4,1,9,9,719,1,30,8))
if mibBuilder.loadTexts:cucsMemoryQualTable.setStatus(_A)
_CucsMemoryQualEntry_Object=MibTableRow
cucsMemoryQualEntry=_CucsMemoryQualEntry_Object((1,3,6,1,4,1,9,9,719,1,30,8,1))
cucsMemoryQualEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cucsMemoryQualEntry.setStatus(_A)
_CucsMemoryQualInstanceId_Type=CucsManagedObjectId
_CucsMemoryQualInstanceId_Object=MibTableColumn
cucsMemoryQualInstanceId=_CucsMemoryQualInstanceId_Object((1,3,6,1,4,1,9,9,719,1,30,8,1,1),_CucsMemoryQualInstanceId_Type())
cucsMemoryQualInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMemoryQualInstanceId.setStatus(_A)
_CucsMemoryQualDn_Type=CucsManagedObjectDn
_CucsMemoryQualDn_Object=MibTableColumn
cucsMemoryQualDn=_CucsMemoryQualDn_Object((1,3,6,1,4,1,9,9,719,1,30,8,1,2),_CucsMemoryQualDn_Type())
cucsMemoryQualDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryQualDn.setStatus(_A)
_CucsMemoryQualRn_Type=SnmpAdminString
_CucsMemoryQualRn_Object=MibTableColumn
cucsMemoryQualRn=_CucsMemoryQualRn_Object((1,3,6,1,4,1,9,9,719,1,30,8,1,3),_CucsMemoryQualRn_Type())
cucsMemoryQualRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryQualRn.setStatus(_A)
_CucsMemoryQualClock_Type=Gauge32
_CucsMemoryQualClock_Object=MibTableColumn
cucsMemoryQualClock=_CucsMemoryQualClock_Object((1,3,6,1,4,1,9,9,719,1,30,8,1,4),_CucsMemoryQualClock_Type())
cucsMemoryQualClock.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryQualClock.setStatus(_A)
_CucsMemoryQualLatency_Type=Integer32
_CucsMemoryQualLatency_Object=MibTableColumn
cucsMemoryQualLatency=_CucsMemoryQualLatency_Object((1,3,6,1,4,1,9,9,719,1,30,8,1,5),_CucsMemoryQualLatency_Type())
cucsMemoryQualLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryQualLatency.setStatus(_A)
_CucsMemoryQualMaxCap_Type=Gauge32
_CucsMemoryQualMaxCap_Object=MibTableColumn
cucsMemoryQualMaxCap=_CucsMemoryQualMaxCap_Object((1,3,6,1,4,1,9,9,719,1,30,8,1,6),_CucsMemoryQualMaxCap_Type())
cucsMemoryQualMaxCap.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryQualMaxCap.setStatus(_A)
_CucsMemoryQualMinCap_Type=Gauge32
_CucsMemoryQualMinCap_Object=MibTableColumn
cucsMemoryQualMinCap=_CucsMemoryQualMinCap_Object((1,3,6,1,4,1,9,9,719,1,30,8,1,7),_CucsMemoryQualMinCap_Type())
cucsMemoryQualMinCap.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryQualMinCap.setStatus(_A)
_CucsMemoryQualSpeed_Type=Gauge32
_CucsMemoryQualSpeed_Object=MibTableColumn
cucsMemoryQualSpeed=_CucsMemoryQualSpeed_Object((1,3,6,1,4,1,9,9,719,1,30,8,1,8),_CucsMemoryQualSpeed_Type())
cucsMemoryQualSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryQualSpeed.setStatus(_A)
_CucsMemoryQualUnits_Type=Gauge32
_CucsMemoryQualUnits_Object=MibTableColumn
cucsMemoryQualUnits=_CucsMemoryQualUnits_Object((1,3,6,1,4,1,9,9,719,1,30,8,1,9),_CucsMemoryQualUnits_Type())
cucsMemoryQualUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryQualUnits.setStatus(_A)
_CucsMemoryQualWidth_Type=Gauge32
_CucsMemoryQualWidth_Object=MibTableColumn
cucsMemoryQualWidth=_CucsMemoryQualWidth_Object((1,3,6,1,4,1,9,9,719,1,30,8,1,10),_CucsMemoryQualWidth_Type())
cucsMemoryQualWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryQualWidth.setStatus(_A)
_CucsMemoryRuntimeTable_Object=MibTable
cucsMemoryRuntimeTable=_CucsMemoryRuntimeTable_Object((1,3,6,1,4,1,9,9,719,1,30,9))
if mibBuilder.loadTexts:cucsMemoryRuntimeTable.setStatus(_A)
_CucsMemoryRuntimeEntry_Object=MibTableRow
cucsMemoryRuntimeEntry=_CucsMemoryRuntimeEntry_Object((1,3,6,1,4,1,9,9,719,1,30,9,1))
cucsMemoryRuntimeEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cucsMemoryRuntimeEntry.setStatus(_A)
_CucsMemoryRuntimeInstanceId_Type=CucsManagedObjectId
_CucsMemoryRuntimeInstanceId_Object=MibTableColumn
cucsMemoryRuntimeInstanceId=_CucsMemoryRuntimeInstanceId_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,1),_CucsMemoryRuntimeInstanceId_Type())
cucsMemoryRuntimeInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMemoryRuntimeInstanceId.setStatus(_A)
_CucsMemoryRuntimeDn_Type=CucsManagedObjectDn
_CucsMemoryRuntimeDn_Object=MibTableColumn
cucsMemoryRuntimeDn=_CucsMemoryRuntimeDn_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,2),_CucsMemoryRuntimeDn_Type())
cucsMemoryRuntimeDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeDn.setStatus(_A)
_CucsMemoryRuntimeRn_Type=SnmpAdminString
_CucsMemoryRuntimeRn_Object=MibTableColumn
cucsMemoryRuntimeRn=_CucsMemoryRuntimeRn_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,3),_CucsMemoryRuntimeRn_Type())
cucsMemoryRuntimeRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeRn.setStatus(_A)
_CucsMemoryRuntimeAvailable_Type=Gauge32
_CucsMemoryRuntimeAvailable_Object=MibTableColumn
cucsMemoryRuntimeAvailable=_CucsMemoryRuntimeAvailable_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,4),_CucsMemoryRuntimeAvailable_Type())
cucsMemoryRuntimeAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeAvailable.setStatus(_A)
_CucsMemoryRuntimeAvailableAvg_Type=Gauge32
_CucsMemoryRuntimeAvailableAvg_Object=MibTableColumn
cucsMemoryRuntimeAvailableAvg=_CucsMemoryRuntimeAvailableAvg_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,5),_CucsMemoryRuntimeAvailableAvg_Type())
cucsMemoryRuntimeAvailableAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeAvailableAvg.setStatus(_A)
_CucsMemoryRuntimeAvailableMax_Type=Gauge32
_CucsMemoryRuntimeAvailableMax_Object=MibTableColumn
cucsMemoryRuntimeAvailableMax=_CucsMemoryRuntimeAvailableMax_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,6),_CucsMemoryRuntimeAvailableMax_Type())
cucsMemoryRuntimeAvailableMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeAvailableMax.setStatus(_A)
_CucsMemoryRuntimeAvailableMin_Type=Gauge32
_CucsMemoryRuntimeAvailableMin_Object=MibTableColumn
cucsMemoryRuntimeAvailableMin=_CucsMemoryRuntimeAvailableMin_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,7),_CucsMemoryRuntimeAvailableMin_Type())
cucsMemoryRuntimeAvailableMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeAvailableMin.setStatus(_A)
_CucsMemoryRuntimeCached_Type=Gauge32
_CucsMemoryRuntimeCached_Object=MibTableColumn
cucsMemoryRuntimeCached=_CucsMemoryRuntimeCached_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,8),_CucsMemoryRuntimeCached_Type())
cucsMemoryRuntimeCached.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeCached.setStatus(_A)
_CucsMemoryRuntimeCachedAvg_Type=Gauge32
_CucsMemoryRuntimeCachedAvg_Object=MibTableColumn
cucsMemoryRuntimeCachedAvg=_CucsMemoryRuntimeCachedAvg_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,9),_CucsMemoryRuntimeCachedAvg_Type())
cucsMemoryRuntimeCachedAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeCachedAvg.setStatus(_A)
_CucsMemoryRuntimeCachedMax_Type=Gauge32
_CucsMemoryRuntimeCachedMax_Object=MibTableColumn
cucsMemoryRuntimeCachedMax=_CucsMemoryRuntimeCachedMax_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,10),_CucsMemoryRuntimeCachedMax_Type())
cucsMemoryRuntimeCachedMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeCachedMax.setStatus(_A)
_CucsMemoryRuntimeCachedMin_Type=Gauge32
_CucsMemoryRuntimeCachedMin_Object=MibTableColumn
cucsMemoryRuntimeCachedMin=_CucsMemoryRuntimeCachedMin_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,11),_CucsMemoryRuntimeCachedMin_Type())
cucsMemoryRuntimeCachedMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeCachedMin.setStatus(_A)
_CucsMemoryRuntimeIntervals_Type=Gauge32
_CucsMemoryRuntimeIntervals_Object=MibTableColumn
cucsMemoryRuntimeIntervals=_CucsMemoryRuntimeIntervals_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,12),_CucsMemoryRuntimeIntervals_Type())
cucsMemoryRuntimeIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeIntervals.setStatus(_A)
_CucsMemoryRuntimeSuspect_Type=TruthValue
_CucsMemoryRuntimeSuspect_Object=MibTableColumn
cucsMemoryRuntimeSuspect=_CucsMemoryRuntimeSuspect_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,13),_CucsMemoryRuntimeSuspect_Type())
cucsMemoryRuntimeSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeSuspect.setStatus(_A)
_CucsMemoryRuntimeThresholded_Type=CucsMemoryRuntimeThresholded
_CucsMemoryRuntimeThresholded_Object=MibTableColumn
cucsMemoryRuntimeThresholded=_CucsMemoryRuntimeThresholded_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,14),_CucsMemoryRuntimeThresholded_Type())
cucsMemoryRuntimeThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeThresholded.setStatus(_A)
_CucsMemoryRuntimeTimeCollected_Type=DateAndTime
_CucsMemoryRuntimeTimeCollected_Object=MibTableColumn
cucsMemoryRuntimeTimeCollected=_CucsMemoryRuntimeTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,15),_CucsMemoryRuntimeTimeCollected_Type())
cucsMemoryRuntimeTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeTimeCollected.setStatus(_A)
_CucsMemoryRuntimeTotal_Type=Gauge32
_CucsMemoryRuntimeTotal_Object=MibTableColumn
cucsMemoryRuntimeTotal=_CucsMemoryRuntimeTotal_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,16),_CucsMemoryRuntimeTotal_Type())
cucsMemoryRuntimeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeTotal.setStatus(_A)
_CucsMemoryRuntimeTotalAvg_Type=Gauge32
_CucsMemoryRuntimeTotalAvg_Object=MibTableColumn
cucsMemoryRuntimeTotalAvg=_CucsMemoryRuntimeTotalAvg_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,17),_CucsMemoryRuntimeTotalAvg_Type())
cucsMemoryRuntimeTotalAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeTotalAvg.setStatus(_A)
_CucsMemoryRuntimeTotalMax_Type=Gauge32
_CucsMemoryRuntimeTotalMax_Object=MibTableColumn
cucsMemoryRuntimeTotalMax=_CucsMemoryRuntimeTotalMax_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,18),_CucsMemoryRuntimeTotalMax_Type())
cucsMemoryRuntimeTotalMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeTotalMax.setStatus(_A)
_CucsMemoryRuntimeTotalMin_Type=Gauge32
_CucsMemoryRuntimeTotalMin_Object=MibTableColumn
cucsMemoryRuntimeTotalMin=_CucsMemoryRuntimeTotalMin_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,19),_CucsMemoryRuntimeTotalMin_Type())
cucsMemoryRuntimeTotalMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeTotalMin.setStatus(_A)
_CucsMemoryRuntimeType_Type=CucsMemoryRuntimeType
_CucsMemoryRuntimeType_Object=MibTableColumn
cucsMemoryRuntimeType=_CucsMemoryRuntimeType_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,20),_CucsMemoryRuntimeType_Type())
cucsMemoryRuntimeType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeType.setStatus(_A)
_CucsMemoryRuntimeUpdate_Type=Gauge32
_CucsMemoryRuntimeUpdate_Object=MibTableColumn
cucsMemoryRuntimeUpdate=_CucsMemoryRuntimeUpdate_Object((1,3,6,1,4,1,9,9,719,1,30,9,1,21),_CucsMemoryRuntimeUpdate_Type())
cucsMemoryRuntimeUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeUpdate.setStatus(_A)
_CucsMemoryRuntimeHistTable_Object=MibTable
cucsMemoryRuntimeHistTable=_CucsMemoryRuntimeHistTable_Object((1,3,6,1,4,1,9,9,719,1,30,10))
if mibBuilder.loadTexts:cucsMemoryRuntimeHistTable.setStatus(_A)
_CucsMemoryRuntimeHistEntry_Object=MibTableRow
cucsMemoryRuntimeHistEntry=_CucsMemoryRuntimeHistEntry_Object((1,3,6,1,4,1,9,9,719,1,30,10,1))
cucsMemoryRuntimeHistEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cucsMemoryRuntimeHistEntry.setStatus(_A)
_CucsMemoryRuntimeHistInstanceId_Type=CucsManagedObjectId
_CucsMemoryRuntimeHistInstanceId_Object=MibTableColumn
cucsMemoryRuntimeHistInstanceId=_CucsMemoryRuntimeHistInstanceId_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,1),_CucsMemoryRuntimeHistInstanceId_Type())
cucsMemoryRuntimeHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistInstanceId.setStatus(_A)
_CucsMemoryRuntimeHistDn_Type=CucsManagedObjectDn
_CucsMemoryRuntimeHistDn_Object=MibTableColumn
cucsMemoryRuntimeHistDn=_CucsMemoryRuntimeHistDn_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,2),_CucsMemoryRuntimeHistDn_Type())
cucsMemoryRuntimeHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistDn.setStatus(_A)
_CucsMemoryRuntimeHistRn_Type=SnmpAdminString
_CucsMemoryRuntimeHistRn_Object=MibTableColumn
cucsMemoryRuntimeHistRn=_CucsMemoryRuntimeHistRn_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,3),_CucsMemoryRuntimeHistRn_Type())
cucsMemoryRuntimeHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistRn.setStatus(_A)
_CucsMemoryRuntimeHistAvailable_Type=Gauge32
_CucsMemoryRuntimeHistAvailable_Object=MibTableColumn
cucsMemoryRuntimeHistAvailable=_CucsMemoryRuntimeHistAvailable_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,4),_CucsMemoryRuntimeHistAvailable_Type())
cucsMemoryRuntimeHistAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistAvailable.setStatus(_A)
_CucsMemoryRuntimeHistAvailableAvg_Type=Gauge32
_CucsMemoryRuntimeHistAvailableAvg_Object=MibTableColumn
cucsMemoryRuntimeHistAvailableAvg=_CucsMemoryRuntimeHistAvailableAvg_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,5),_CucsMemoryRuntimeHistAvailableAvg_Type())
cucsMemoryRuntimeHistAvailableAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistAvailableAvg.setStatus(_A)
_CucsMemoryRuntimeHistAvailableMax_Type=Gauge32
_CucsMemoryRuntimeHistAvailableMax_Object=MibTableColumn
cucsMemoryRuntimeHistAvailableMax=_CucsMemoryRuntimeHistAvailableMax_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,6),_CucsMemoryRuntimeHistAvailableMax_Type())
cucsMemoryRuntimeHistAvailableMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistAvailableMax.setStatus(_A)
_CucsMemoryRuntimeHistAvailableMin_Type=Gauge32
_CucsMemoryRuntimeHistAvailableMin_Object=MibTableColumn
cucsMemoryRuntimeHistAvailableMin=_CucsMemoryRuntimeHistAvailableMin_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,7),_CucsMemoryRuntimeHistAvailableMin_Type())
cucsMemoryRuntimeHistAvailableMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistAvailableMin.setStatus(_A)
_CucsMemoryRuntimeHistCached_Type=Gauge32
_CucsMemoryRuntimeHistCached_Object=MibTableColumn
cucsMemoryRuntimeHistCached=_CucsMemoryRuntimeHistCached_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,8),_CucsMemoryRuntimeHistCached_Type())
cucsMemoryRuntimeHistCached.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistCached.setStatus(_A)
_CucsMemoryRuntimeHistCachedAvg_Type=Gauge32
_CucsMemoryRuntimeHistCachedAvg_Object=MibTableColumn
cucsMemoryRuntimeHistCachedAvg=_CucsMemoryRuntimeHistCachedAvg_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,9),_CucsMemoryRuntimeHistCachedAvg_Type())
cucsMemoryRuntimeHistCachedAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistCachedAvg.setStatus(_A)
_CucsMemoryRuntimeHistCachedMax_Type=Gauge32
_CucsMemoryRuntimeHistCachedMax_Object=MibTableColumn
cucsMemoryRuntimeHistCachedMax=_CucsMemoryRuntimeHistCachedMax_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,10),_CucsMemoryRuntimeHistCachedMax_Type())
cucsMemoryRuntimeHistCachedMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistCachedMax.setStatus(_A)
_CucsMemoryRuntimeHistCachedMin_Type=Gauge32
_CucsMemoryRuntimeHistCachedMin_Object=MibTableColumn
cucsMemoryRuntimeHistCachedMin=_CucsMemoryRuntimeHistCachedMin_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,11),_CucsMemoryRuntimeHistCachedMin_Type())
cucsMemoryRuntimeHistCachedMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistCachedMin.setStatus(_A)
_CucsMemoryRuntimeHistId_Type=Unsigned64
_CucsMemoryRuntimeHistId_Object=MibTableColumn
cucsMemoryRuntimeHistId=_CucsMemoryRuntimeHistId_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,12),_CucsMemoryRuntimeHistId_Type())
cucsMemoryRuntimeHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistId.setStatus(_A)
_CucsMemoryRuntimeHistMostRecent_Type=TruthValue
_CucsMemoryRuntimeHistMostRecent_Object=MibTableColumn
cucsMemoryRuntimeHistMostRecent=_CucsMemoryRuntimeHistMostRecent_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,13),_CucsMemoryRuntimeHistMostRecent_Type())
cucsMemoryRuntimeHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistMostRecent.setStatus(_A)
_CucsMemoryRuntimeHistSuspect_Type=TruthValue
_CucsMemoryRuntimeHistSuspect_Object=MibTableColumn
cucsMemoryRuntimeHistSuspect=_CucsMemoryRuntimeHistSuspect_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,14),_CucsMemoryRuntimeHistSuspect_Type())
cucsMemoryRuntimeHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistSuspect.setStatus(_A)
_CucsMemoryRuntimeHistThresholded_Type=CucsMemoryRuntimeHistThresholded
_CucsMemoryRuntimeHistThresholded_Object=MibTableColumn
cucsMemoryRuntimeHistThresholded=_CucsMemoryRuntimeHistThresholded_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,15),_CucsMemoryRuntimeHistThresholded_Type())
cucsMemoryRuntimeHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistThresholded.setStatus(_A)
_CucsMemoryRuntimeHistTimeCollected_Type=DateAndTime
_CucsMemoryRuntimeHistTimeCollected_Object=MibTableColumn
cucsMemoryRuntimeHistTimeCollected=_CucsMemoryRuntimeHistTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,16),_CucsMemoryRuntimeHistTimeCollected_Type())
cucsMemoryRuntimeHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistTimeCollected.setStatus(_A)
_CucsMemoryRuntimeHistTotal_Type=Gauge32
_CucsMemoryRuntimeHistTotal_Object=MibTableColumn
cucsMemoryRuntimeHistTotal=_CucsMemoryRuntimeHistTotal_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,17),_CucsMemoryRuntimeHistTotal_Type())
cucsMemoryRuntimeHistTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistTotal.setStatus(_A)
_CucsMemoryRuntimeHistTotalAvg_Type=Gauge32
_CucsMemoryRuntimeHistTotalAvg_Object=MibTableColumn
cucsMemoryRuntimeHistTotalAvg=_CucsMemoryRuntimeHistTotalAvg_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,18),_CucsMemoryRuntimeHistTotalAvg_Type())
cucsMemoryRuntimeHistTotalAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistTotalAvg.setStatus(_A)
_CucsMemoryRuntimeHistTotalMax_Type=Gauge32
_CucsMemoryRuntimeHistTotalMax_Object=MibTableColumn
cucsMemoryRuntimeHistTotalMax=_CucsMemoryRuntimeHistTotalMax_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,19),_CucsMemoryRuntimeHistTotalMax_Type())
cucsMemoryRuntimeHistTotalMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistTotalMax.setStatus(_A)
_CucsMemoryRuntimeHistTotalMin_Type=Gauge32
_CucsMemoryRuntimeHistTotalMin_Object=MibTableColumn
cucsMemoryRuntimeHistTotalMin=_CucsMemoryRuntimeHistTotalMin_Object((1,3,6,1,4,1,9,9,719,1,30,10,1,20),_CucsMemoryRuntimeHistTotalMin_Type())
cucsMemoryRuntimeHistTotalMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryRuntimeHistTotalMin.setStatus(_A)
_CucsMemoryUnitTable_Object=MibTable
cucsMemoryUnitTable=_CucsMemoryUnitTable_Object((1,3,6,1,4,1,9,9,719,1,30,11))
if mibBuilder.loadTexts:cucsMemoryUnitTable.setStatus(_A)
_CucsMemoryUnitEntry_Object=MibTableRow
cucsMemoryUnitEntry=_CucsMemoryUnitEntry_Object((1,3,6,1,4,1,9,9,719,1,30,11,1))
cucsMemoryUnitEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cucsMemoryUnitEntry.setStatus(_A)
_CucsMemoryUnitInstanceId_Type=CucsManagedObjectId
_CucsMemoryUnitInstanceId_Object=MibTableColumn
cucsMemoryUnitInstanceId=_CucsMemoryUnitInstanceId_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,1),_CucsMemoryUnitInstanceId_Type())
cucsMemoryUnitInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMemoryUnitInstanceId.setStatus(_A)
_CucsMemoryUnitDn_Type=CucsManagedObjectDn
_CucsMemoryUnitDn_Object=MibTableColumn
cucsMemoryUnitDn=_CucsMemoryUnitDn_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,2),_CucsMemoryUnitDn_Type())
cucsMemoryUnitDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitDn.setStatus(_A)
_CucsMemoryUnitRn_Type=SnmpAdminString
_CucsMemoryUnitRn_Object=MibTableColumn
cucsMemoryUnitRn=_CucsMemoryUnitRn_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,3),_CucsMemoryUnitRn_Type())
cucsMemoryUnitRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitRn.setStatus(_A)
_CucsMemoryUnitArray_Type=Gauge32
_CucsMemoryUnitArray_Object=MibTableColumn
cucsMemoryUnitArray=_CucsMemoryUnitArray_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,4),_CucsMemoryUnitArray_Type())
cucsMemoryUnitArray.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitArray.setStatus(_A)
_CucsMemoryUnitBank_Type=Gauge32
_CucsMemoryUnitBank_Object=MibTableColumn
cucsMemoryUnitBank=_CucsMemoryUnitBank_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,5),_CucsMemoryUnitBank_Type())
cucsMemoryUnitBank.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitBank.setStatus(_A)
_CucsMemoryUnitCapacity_Type=Gauge32
_CucsMemoryUnitCapacity_Object=MibTableColumn
cucsMemoryUnitCapacity=_CucsMemoryUnitCapacity_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,6),_CucsMemoryUnitCapacity_Type())
cucsMemoryUnitCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitCapacity.setStatus(_A)
_CucsMemoryUnitClock_Type=Gauge32
_CucsMemoryUnitClock_Object=MibTableColumn
cucsMemoryUnitClock=_CucsMemoryUnitClock_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,7),_CucsMemoryUnitClock_Type())
cucsMemoryUnitClock.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitClock.setStatus(_A)
_CucsMemoryUnitFormFactor_Type=CucsMemoryFormFactor
_CucsMemoryUnitFormFactor_Object=MibTableColumn
cucsMemoryUnitFormFactor=_CucsMemoryUnitFormFactor_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,8),_CucsMemoryUnitFormFactor_Type())
cucsMemoryUnitFormFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitFormFactor.setStatus(_A)
_CucsMemoryUnitId_Type=CucsMemoryUnitId
_CucsMemoryUnitId_Object=MibTableColumn
cucsMemoryUnitId=_CucsMemoryUnitId_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,9),_CucsMemoryUnitId_Type())
cucsMemoryUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitId.setStatus(_A)
_CucsMemoryUnitLatency_Type=Integer32
_CucsMemoryUnitLatency_Object=MibTableColumn
cucsMemoryUnitLatency=_CucsMemoryUnitLatency_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,10),_CucsMemoryUnitLatency_Type())
cucsMemoryUnitLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitLatency.setStatus(_A)
_CucsMemoryUnitLocation_Type=SnmpAdminString
_CucsMemoryUnitLocation_Object=MibTableColumn
cucsMemoryUnitLocation=_CucsMemoryUnitLocation_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,11),_CucsMemoryUnitLocation_Type())
cucsMemoryUnitLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitLocation.setStatus(_A)
_CucsMemoryUnitModel_Type=SnmpAdminString
_CucsMemoryUnitModel_Object=MibTableColumn
cucsMemoryUnitModel=_CucsMemoryUnitModel_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,12),_CucsMemoryUnitModel_Type())
cucsMemoryUnitModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitModel.setStatus(_A)
_CucsMemoryUnitOperState_Type=CucsEquipmentOperability
_CucsMemoryUnitOperState_Object=MibTableColumn
cucsMemoryUnitOperState=_CucsMemoryUnitOperState_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,13),_CucsMemoryUnitOperState_Type())
cucsMemoryUnitOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitOperState.setStatus(_A)
_CucsMemoryUnitOperability_Type=CucsMemoryUnitOperability
_CucsMemoryUnitOperability_Object=MibTableColumn
cucsMemoryUnitOperability=_CucsMemoryUnitOperability_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,14),_CucsMemoryUnitOperability_Type())
cucsMemoryUnitOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitOperability.setStatus(_A)
_CucsMemoryUnitPerf_Type=CucsEquipmentSensorThresholdStatus
_CucsMemoryUnitPerf_Object=MibTableColumn
cucsMemoryUnitPerf=_CucsMemoryUnitPerf_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,15),_CucsMemoryUnitPerf_Type())
cucsMemoryUnitPerf.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitPerf.setStatus(_A)
_CucsMemoryUnitPower_Type=CucsEquipmentPowerState
_CucsMemoryUnitPower_Object=MibTableColumn
cucsMemoryUnitPower=_CucsMemoryUnitPower_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,16),_CucsMemoryUnitPower_Type())
cucsMemoryUnitPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitPower.setStatus(_A)
_CucsMemoryUnitPresence_Type=CucsEquipmentPresence
_CucsMemoryUnitPresence_Object=MibTableColumn
cucsMemoryUnitPresence=_CucsMemoryUnitPresence_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,17),_CucsMemoryUnitPresence_Type())
cucsMemoryUnitPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitPresence.setStatus(_A)
_CucsMemoryUnitRevision_Type=SnmpAdminString
_CucsMemoryUnitRevision_Object=MibTableColumn
cucsMemoryUnitRevision=_CucsMemoryUnitRevision_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,18),_CucsMemoryUnitRevision_Type())
cucsMemoryUnitRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitRevision.setStatus(_A)
_CucsMemoryUnitSerial_Type=SnmpAdminString
_CucsMemoryUnitSerial_Object=MibTableColumn
cucsMemoryUnitSerial=_CucsMemoryUnitSerial_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,19),_CucsMemoryUnitSerial_Type())
cucsMemoryUnitSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitSerial.setStatus(_A)
_CucsMemoryUnitSet_Type=Gauge32
_CucsMemoryUnitSet_Object=MibTableColumn
cucsMemoryUnitSet=_CucsMemoryUnitSet_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,20),_CucsMemoryUnitSet_Type())
cucsMemoryUnitSet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitSet.setStatus(_A)
_CucsMemoryUnitSpeed_Type=Gauge32
_CucsMemoryUnitSpeed_Object=MibTableColumn
cucsMemoryUnitSpeed=_CucsMemoryUnitSpeed_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,21),_CucsMemoryUnitSpeed_Type())
cucsMemoryUnitSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitSpeed.setStatus(_A)
_CucsMemoryUnitThermal_Type=CucsEquipmentSensorThresholdStatus
_CucsMemoryUnitThermal_Object=MibTableColumn
cucsMemoryUnitThermal=_CucsMemoryUnitThermal_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,22),_CucsMemoryUnitThermal_Type())
cucsMemoryUnitThermal.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitThermal.setStatus(_A)
_CucsMemoryUnitType_Type=CucsMemoryType
_CucsMemoryUnitType_Object=MibTableColumn
cucsMemoryUnitType=_CucsMemoryUnitType_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,23),_CucsMemoryUnitType_Type())
cucsMemoryUnitType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitType.setStatus(_A)
_CucsMemoryUnitVendor_Type=SnmpAdminString
_CucsMemoryUnitVendor_Object=MibTableColumn
cucsMemoryUnitVendor=_CucsMemoryUnitVendor_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,24),_CucsMemoryUnitVendor_Type())
cucsMemoryUnitVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitVendor.setStatus(_A)
_CucsMemoryUnitVisibility_Type=CucsMemoryVisibility
_CucsMemoryUnitVisibility_Object=MibTableColumn
cucsMemoryUnitVisibility=_CucsMemoryUnitVisibility_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,25),_CucsMemoryUnitVisibility_Type())
cucsMemoryUnitVisibility.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitVisibility.setStatus(_A)
_CucsMemoryUnitVoltage_Type=CucsEquipmentSensorThresholdStatus
_CucsMemoryUnitVoltage_Object=MibTableColumn
cucsMemoryUnitVoltage=_CucsMemoryUnitVoltage_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,26),_CucsMemoryUnitVoltage_Type())
cucsMemoryUnitVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitVoltage.setStatus(_A)
_CucsMemoryUnitWidth_Type=Gauge32
_CucsMemoryUnitWidth_Object=MibTableColumn
cucsMemoryUnitWidth=_CucsMemoryUnitWidth_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,27),_CucsMemoryUnitWidth_Type())
cucsMemoryUnitWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitWidth.setStatus(_A)
_CucsMemoryUnitAdminState_Type=CucsMemoryAdminState
_CucsMemoryUnitAdminState_Object=MibTableColumn
cucsMemoryUnitAdminState=_CucsMemoryUnitAdminState_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,28),_CucsMemoryUnitAdminState_Type())
cucsMemoryUnitAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitAdminState.setStatus(_A)
_CucsMemoryUnitOperQualifier_Type=CucsMemoryIssues
_CucsMemoryUnitOperQualifier_Object=MibTableColumn
cucsMemoryUnitOperQualifier=_CucsMemoryUnitOperQualifier_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,29),_CucsMemoryUnitOperQualifier_Type())
cucsMemoryUnitOperQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitOperQualifier.setStatus(_A)
_CucsMemoryUnitOperQualifierReason_Type=SnmpAdminString
_CucsMemoryUnitOperQualifierReason_Object=MibTableColumn
cucsMemoryUnitOperQualifierReason=_CucsMemoryUnitOperQualifierReason_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,30),_CucsMemoryUnitOperQualifierReason_Type())
cucsMemoryUnitOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitOperQualifierReason.setStatus(_A)
_CucsMemoryUnitLocationDn_Type=SnmpAdminString
_CucsMemoryUnitLocationDn_Object=MibTableColumn
cucsMemoryUnitLocationDn=_CucsMemoryUnitLocationDn_Object((1,3,6,1,4,1,9,9,719,1,30,11,1,31),_CucsMemoryUnitLocationDn_Type())
cucsMemoryUnitLocationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitLocationDn.setStatus(_A)
_CucsMemoryUnitEnvStatsTable_Object=MibTable
cucsMemoryUnitEnvStatsTable=_CucsMemoryUnitEnvStatsTable_Object((1,3,6,1,4,1,9,9,719,1,30,12))
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsTable.setStatus(_A)
_CucsMemoryUnitEnvStatsEntry_Object=MibTableRow
cucsMemoryUnitEnvStatsEntry=_CucsMemoryUnitEnvStatsEntry_Object((1,3,6,1,4,1,9,9,719,1,30,12,1))
cucsMemoryUnitEnvStatsEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsEntry.setStatus(_A)
_CucsMemoryUnitEnvStatsInstanceId_Type=CucsManagedObjectId
_CucsMemoryUnitEnvStatsInstanceId_Object=MibTableColumn
cucsMemoryUnitEnvStatsInstanceId=_CucsMemoryUnitEnvStatsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,30,12,1,1),_CucsMemoryUnitEnvStatsInstanceId_Type())
cucsMemoryUnitEnvStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsInstanceId.setStatus(_A)
_CucsMemoryUnitEnvStatsDn_Type=CucsManagedObjectDn
_CucsMemoryUnitEnvStatsDn_Object=MibTableColumn
cucsMemoryUnitEnvStatsDn=_CucsMemoryUnitEnvStatsDn_Object((1,3,6,1,4,1,9,9,719,1,30,12,1,2),_CucsMemoryUnitEnvStatsDn_Type())
cucsMemoryUnitEnvStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsDn.setStatus(_A)
_CucsMemoryUnitEnvStatsRn_Type=SnmpAdminString
_CucsMemoryUnitEnvStatsRn_Object=MibTableColumn
cucsMemoryUnitEnvStatsRn=_CucsMemoryUnitEnvStatsRn_Object((1,3,6,1,4,1,9,9,719,1,30,12,1,3),_CucsMemoryUnitEnvStatsRn_Type())
cucsMemoryUnitEnvStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsRn.setStatus(_A)
_CucsMemoryUnitEnvStatsIntervals_Type=Gauge32
_CucsMemoryUnitEnvStatsIntervals_Object=MibTableColumn
cucsMemoryUnitEnvStatsIntervals=_CucsMemoryUnitEnvStatsIntervals_Object((1,3,6,1,4,1,9,9,719,1,30,12,1,4),_CucsMemoryUnitEnvStatsIntervals_Type())
cucsMemoryUnitEnvStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsIntervals.setStatus(_A)
_CucsMemoryUnitEnvStatsSuspect_Type=TruthValue
_CucsMemoryUnitEnvStatsSuspect_Object=MibTableColumn
cucsMemoryUnitEnvStatsSuspect=_CucsMemoryUnitEnvStatsSuspect_Object((1,3,6,1,4,1,9,9,719,1,30,12,1,5),_CucsMemoryUnitEnvStatsSuspect_Type())
cucsMemoryUnitEnvStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsSuspect.setStatus(_A)
_CucsMemoryUnitEnvStatsTemperature_Type=Integer32
_CucsMemoryUnitEnvStatsTemperature_Object=MibTableColumn
cucsMemoryUnitEnvStatsTemperature=_CucsMemoryUnitEnvStatsTemperature_Object((1,3,6,1,4,1,9,9,719,1,30,12,1,6),_CucsMemoryUnitEnvStatsTemperature_Type())
cucsMemoryUnitEnvStatsTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsTemperature.setStatus(_A)
_CucsMemoryUnitEnvStatsTemperatureAvg_Type=Integer32
_CucsMemoryUnitEnvStatsTemperatureAvg_Object=MibTableColumn
cucsMemoryUnitEnvStatsTemperatureAvg=_CucsMemoryUnitEnvStatsTemperatureAvg_Object((1,3,6,1,4,1,9,9,719,1,30,12,1,7),_CucsMemoryUnitEnvStatsTemperatureAvg_Type())
cucsMemoryUnitEnvStatsTemperatureAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsTemperatureAvg.setStatus(_A)
_CucsMemoryUnitEnvStatsTemperatureMax_Type=Integer32
_CucsMemoryUnitEnvStatsTemperatureMax_Object=MibTableColumn
cucsMemoryUnitEnvStatsTemperatureMax=_CucsMemoryUnitEnvStatsTemperatureMax_Object((1,3,6,1,4,1,9,9,719,1,30,12,1,8),_CucsMemoryUnitEnvStatsTemperatureMax_Type())
cucsMemoryUnitEnvStatsTemperatureMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsTemperatureMax.setStatus(_A)
_CucsMemoryUnitEnvStatsTemperatureMin_Type=Integer32
_CucsMemoryUnitEnvStatsTemperatureMin_Object=MibTableColumn
cucsMemoryUnitEnvStatsTemperatureMin=_CucsMemoryUnitEnvStatsTemperatureMin_Object((1,3,6,1,4,1,9,9,719,1,30,12,1,9),_CucsMemoryUnitEnvStatsTemperatureMin_Type())
cucsMemoryUnitEnvStatsTemperatureMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsTemperatureMin.setStatus(_A)
_CucsMemoryUnitEnvStatsThresholded_Type=CucsMemoryUnitEnvStatsThresholded
_CucsMemoryUnitEnvStatsThresholded_Object=MibTableColumn
cucsMemoryUnitEnvStatsThresholded=_CucsMemoryUnitEnvStatsThresholded_Object((1,3,6,1,4,1,9,9,719,1,30,12,1,10),_CucsMemoryUnitEnvStatsThresholded_Type())
cucsMemoryUnitEnvStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsThresholded.setStatus(_A)
_CucsMemoryUnitEnvStatsTimeCollected_Type=DateAndTime
_CucsMemoryUnitEnvStatsTimeCollected_Object=MibTableColumn
cucsMemoryUnitEnvStatsTimeCollected=_CucsMemoryUnitEnvStatsTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,30,12,1,11),_CucsMemoryUnitEnvStatsTimeCollected_Type())
cucsMemoryUnitEnvStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsTimeCollected.setStatus(_A)
_CucsMemoryUnitEnvStatsUpdate_Type=Gauge32
_CucsMemoryUnitEnvStatsUpdate_Object=MibTableColumn
cucsMemoryUnitEnvStatsUpdate=_CucsMemoryUnitEnvStatsUpdate_Object((1,3,6,1,4,1,9,9,719,1,30,12,1,12),_CucsMemoryUnitEnvStatsUpdate_Type())
cucsMemoryUnitEnvStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsUpdate.setStatus(_A)
_CucsMemoryUnitEnvStatsHistTable_Object=MibTable
cucsMemoryUnitEnvStatsHistTable=_CucsMemoryUnitEnvStatsHistTable_Object((1,3,6,1,4,1,9,9,719,1,30,13))
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsHistTable.setStatus(_A)
_CucsMemoryUnitEnvStatsHistEntry_Object=MibTableRow
cucsMemoryUnitEnvStatsHistEntry=_CucsMemoryUnitEnvStatsHistEntry_Object((1,3,6,1,4,1,9,9,719,1,30,13,1))
cucsMemoryUnitEnvStatsHistEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsHistEntry.setStatus(_A)
_CucsMemoryUnitEnvStatsHistInstanceId_Type=CucsManagedObjectId
_CucsMemoryUnitEnvStatsHistInstanceId_Object=MibTableColumn
cucsMemoryUnitEnvStatsHistInstanceId=_CucsMemoryUnitEnvStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,719,1,30,13,1,1),_CucsMemoryUnitEnvStatsHistInstanceId_Type())
cucsMemoryUnitEnvStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsHistInstanceId.setStatus(_A)
_CucsMemoryUnitEnvStatsHistDn_Type=CucsManagedObjectDn
_CucsMemoryUnitEnvStatsHistDn_Object=MibTableColumn
cucsMemoryUnitEnvStatsHistDn=_CucsMemoryUnitEnvStatsHistDn_Object((1,3,6,1,4,1,9,9,719,1,30,13,1,2),_CucsMemoryUnitEnvStatsHistDn_Type())
cucsMemoryUnitEnvStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsHistDn.setStatus(_A)
_CucsMemoryUnitEnvStatsHistRn_Type=SnmpAdminString
_CucsMemoryUnitEnvStatsHistRn_Object=MibTableColumn
cucsMemoryUnitEnvStatsHistRn=_CucsMemoryUnitEnvStatsHistRn_Object((1,3,6,1,4,1,9,9,719,1,30,13,1,3),_CucsMemoryUnitEnvStatsHistRn_Type())
cucsMemoryUnitEnvStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsHistRn.setStatus(_A)
_CucsMemoryUnitEnvStatsHistId_Type=Unsigned64
_CucsMemoryUnitEnvStatsHistId_Object=MibTableColumn
cucsMemoryUnitEnvStatsHistId=_CucsMemoryUnitEnvStatsHistId_Object((1,3,6,1,4,1,9,9,719,1,30,13,1,4),_CucsMemoryUnitEnvStatsHistId_Type())
cucsMemoryUnitEnvStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsHistId.setStatus(_A)
_CucsMemoryUnitEnvStatsHistMostRecent_Type=TruthValue
_CucsMemoryUnitEnvStatsHistMostRecent_Object=MibTableColumn
cucsMemoryUnitEnvStatsHistMostRecent=_CucsMemoryUnitEnvStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,719,1,30,13,1,5),_CucsMemoryUnitEnvStatsHistMostRecent_Type())
cucsMemoryUnitEnvStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsHistMostRecent.setStatus(_A)
_CucsMemoryUnitEnvStatsHistSuspect_Type=TruthValue
_CucsMemoryUnitEnvStatsHistSuspect_Object=MibTableColumn
cucsMemoryUnitEnvStatsHistSuspect=_CucsMemoryUnitEnvStatsHistSuspect_Object((1,3,6,1,4,1,9,9,719,1,30,13,1,6),_CucsMemoryUnitEnvStatsHistSuspect_Type())
cucsMemoryUnitEnvStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsHistSuspect.setStatus(_A)
_CucsMemoryUnitEnvStatsHistTemperature_Type=Integer32
_CucsMemoryUnitEnvStatsHistTemperature_Object=MibTableColumn
cucsMemoryUnitEnvStatsHistTemperature=_CucsMemoryUnitEnvStatsHistTemperature_Object((1,3,6,1,4,1,9,9,719,1,30,13,1,7),_CucsMemoryUnitEnvStatsHistTemperature_Type())
cucsMemoryUnitEnvStatsHistTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsHistTemperature.setStatus(_A)
_CucsMemoryUnitEnvStatsHistTemperatureAvg_Type=Integer32
_CucsMemoryUnitEnvStatsHistTemperatureAvg_Object=MibTableColumn
cucsMemoryUnitEnvStatsHistTemperatureAvg=_CucsMemoryUnitEnvStatsHistTemperatureAvg_Object((1,3,6,1,4,1,9,9,719,1,30,13,1,8),_CucsMemoryUnitEnvStatsHistTemperatureAvg_Type())
cucsMemoryUnitEnvStatsHistTemperatureAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsHistTemperatureAvg.setStatus(_A)
_CucsMemoryUnitEnvStatsHistTemperatureMax_Type=Integer32
_CucsMemoryUnitEnvStatsHistTemperatureMax_Object=MibTableColumn
cucsMemoryUnitEnvStatsHistTemperatureMax=_CucsMemoryUnitEnvStatsHistTemperatureMax_Object((1,3,6,1,4,1,9,9,719,1,30,13,1,9),_CucsMemoryUnitEnvStatsHistTemperatureMax_Type())
cucsMemoryUnitEnvStatsHistTemperatureMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsHistTemperatureMax.setStatus(_A)
_CucsMemoryUnitEnvStatsHistTemperatureMin_Type=Integer32
_CucsMemoryUnitEnvStatsHistTemperatureMin_Object=MibTableColumn
cucsMemoryUnitEnvStatsHistTemperatureMin=_CucsMemoryUnitEnvStatsHistTemperatureMin_Object((1,3,6,1,4,1,9,9,719,1,30,13,1,10),_CucsMemoryUnitEnvStatsHistTemperatureMin_Type())
cucsMemoryUnitEnvStatsHistTemperatureMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsHistTemperatureMin.setStatus(_A)
_CucsMemoryUnitEnvStatsHistThresholded_Type=CucsMemoryUnitEnvStatsHistThresholded
_CucsMemoryUnitEnvStatsHistThresholded_Object=MibTableColumn
cucsMemoryUnitEnvStatsHistThresholded=_CucsMemoryUnitEnvStatsHistThresholded_Object((1,3,6,1,4,1,9,9,719,1,30,13,1,11),_CucsMemoryUnitEnvStatsHistThresholded_Type())
cucsMemoryUnitEnvStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsHistThresholded.setStatus(_A)
_CucsMemoryUnitEnvStatsHistTimeCollected_Type=DateAndTime
_CucsMemoryUnitEnvStatsHistTimeCollected_Object=MibTableColumn
cucsMemoryUnitEnvStatsHistTimeCollected=_CucsMemoryUnitEnvStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,30,13,1,12),_CucsMemoryUnitEnvStatsHistTimeCollected_Type())
cucsMemoryUnitEnvStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMemoryUnitEnvStatsHistTimeCollected.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsMemoryObjects':cucsMemoryObjects,'cucsMemoryArrayTable':cucsMemoryArrayTable,'cucsMemoryArrayEntry':cucsMemoryArrayEntry,_E:cucsMemoryArrayInstanceId,'cucsMemoryArrayDn':cucsMemoryArrayDn,'cucsMemoryArrayRn':cucsMemoryArrayRn,'cucsMemoryArrayCpuId':cucsMemoryArrayCpuId,'cucsMemoryArrayCurrCapacity':cucsMemoryArrayCurrCapacity,'cucsMemoryArrayErrorCorrection':cucsMemoryArrayErrorCorrection,'cucsMemoryArrayId':cucsMemoryArrayId,'cucsMemoryArrayMaxCapacity':cucsMemoryArrayMaxCapacity,'cucsMemoryArrayMaxDevices':cucsMemoryArrayMaxDevices,'cucsMemoryArrayModel':cucsMemoryArrayModel,'cucsMemoryArrayOperState':cucsMemoryArrayOperState,'cucsMemoryArrayOperability':cucsMemoryArrayOperability,'cucsMemoryArrayPerf':cucsMemoryArrayPerf,'cucsMemoryArrayPopulated':cucsMemoryArrayPopulated,'cucsMemoryArrayPower':cucsMemoryArrayPower,'cucsMemoryArrayPresence':cucsMemoryArrayPresence,'cucsMemoryArrayRevision':cucsMemoryArrayRevision,'cucsMemoryArraySerial':cucsMemoryArraySerial,'cucsMemoryArrayThermal':cucsMemoryArrayThermal,'cucsMemoryArrayVendor':cucsMemoryArrayVendor,'cucsMemoryArrayVoltage':cucsMemoryArrayVoltage,'cucsMemoryArrayOperQualifierReason':cucsMemoryArrayOperQualifierReason,'cucsMemoryArrayLocationDn':cucsMemoryArrayLocationDn,'cucsMemoryArrayEnvStatsTable':cucsMemoryArrayEnvStatsTable,'cucsMemoryArrayEnvStatsEntry':cucsMemoryArrayEnvStatsEntry,_F:cucsMemoryArrayEnvStatsInstanceId,'cucsMemoryArrayEnvStatsDn':cucsMemoryArrayEnvStatsDn,'cucsMemoryArrayEnvStatsRn':cucsMemoryArrayEnvStatsRn,'cucsMemoryArrayEnvStatsInputCurrent':cucsMemoryArrayEnvStatsInputCurrent,'cucsMemoryArrayEnvStatsInputCurrentAvg':cucsMemoryArrayEnvStatsInputCurrentAvg,'cucsMemoryArrayEnvStatsInputCurrentMax':cucsMemoryArrayEnvStatsInputCurrentMax,'cucsMemoryArrayEnvStatsInputCurrentMin':cucsMemoryArrayEnvStatsInputCurrentMin,'cucsMemoryArrayEnvStatsIntervals':cucsMemoryArrayEnvStatsIntervals,'cucsMemoryArrayEnvStatsSuspect':cucsMemoryArrayEnvStatsSuspect,'cucsMemoryArrayEnvStatsThresholded':cucsMemoryArrayEnvStatsThresholded,'cucsMemoryArrayEnvStatsTimeCollected':cucsMemoryArrayEnvStatsTimeCollected,'cucsMemoryArrayEnvStatsUpdate':cucsMemoryArrayEnvStatsUpdate,'cucsMemoryArrayEnvStatsHistTable':cucsMemoryArrayEnvStatsHistTable,'cucsMemoryArrayEnvStatsHistEntry':cucsMemoryArrayEnvStatsHistEntry,_G:cucsMemoryArrayEnvStatsHistInstanceId,'cucsMemoryArrayEnvStatsHistDn':cucsMemoryArrayEnvStatsHistDn,'cucsMemoryArrayEnvStatsHistRn':cucsMemoryArrayEnvStatsHistRn,'cucsMemoryArrayEnvStatsHistId':cucsMemoryArrayEnvStatsHistId,'cucsMemoryArrayEnvStatsHistInputCurrent':cucsMemoryArrayEnvStatsHistInputCurrent,'cucsMemoryArrayEnvStatsHistInputCurrentAvg':cucsMemoryArrayEnvStatsHistInputCurrentAvg,'cucsMemoryArrayEnvStatsHistInputCurrentMax':cucsMemoryArrayEnvStatsHistInputCurrentMax,'cucsMemoryArrayEnvStatsHistInputCurrentMin':cucsMemoryArrayEnvStatsHistInputCurrentMin,'cucsMemoryArrayEnvStatsHistMostRecent':cucsMemoryArrayEnvStatsHistMostRecent,'cucsMemoryArrayEnvStatsHistSuspect':cucsMemoryArrayEnvStatsHistSuspect,'cucsMemoryArrayEnvStatsHistThresholded':cucsMemoryArrayEnvStatsHistThresholded,'cucsMemoryArrayEnvStatsHistTimeCollected':cucsMemoryArrayEnvStatsHistTimeCollected,'cucsMemoryBufferUnitTable':cucsMemoryBufferUnitTable,'cucsMemoryBufferUnitEntry':cucsMemoryBufferUnitEntry,_H:cucsMemoryBufferUnitInstanceId,'cucsMemoryBufferUnitDn':cucsMemoryBufferUnitDn,'cucsMemoryBufferUnitRn':cucsMemoryBufferUnitRn,'cucsMemoryBufferUnitId':cucsMemoryBufferUnitId,'cucsMemoryBufferUnitModel':cucsMemoryBufferUnitModel,'cucsMemoryBufferUnitOperState':cucsMemoryBufferUnitOperState,'cucsMemoryBufferUnitOperability':cucsMemoryBufferUnitOperability,'cucsMemoryBufferUnitPerf':cucsMemoryBufferUnitPerf,'cucsMemoryBufferUnitPower':cucsMemoryBufferUnitPower,'cucsMemoryBufferUnitPresence':cucsMemoryBufferUnitPresence,'cucsMemoryBufferUnitRevision':cucsMemoryBufferUnitRevision,'cucsMemoryBufferUnitSerial':cucsMemoryBufferUnitSerial,'cucsMemoryBufferUnitThermal':cucsMemoryBufferUnitThermal,'cucsMemoryBufferUnitVendor':cucsMemoryBufferUnitVendor,'cucsMemoryBufferUnitVoltage':cucsMemoryBufferUnitVoltage,'cucsMemoryBufferUnitOperQualifierReason':cucsMemoryBufferUnitOperQualifierReason,'cucsMemoryBufferUnitLocationDn':cucsMemoryBufferUnitLocationDn,'cucsMemoryBufferUnitEnvStatsTable':cucsMemoryBufferUnitEnvStatsTable,'cucsMemoryBufferUnitEnvStatsEntry':cucsMemoryBufferUnitEnvStatsEntry,_I:cucsMemoryBufferUnitEnvStatsInstanceId,'cucsMemoryBufferUnitEnvStatsDn':cucsMemoryBufferUnitEnvStatsDn,'cucsMemoryBufferUnitEnvStatsRn':cucsMemoryBufferUnitEnvStatsRn,'cucsMemoryBufferUnitEnvStatsIntervals':cucsMemoryBufferUnitEnvStatsIntervals,'cucsMemoryBufferUnitEnvStatsSuspect':cucsMemoryBufferUnitEnvStatsSuspect,'cucsMemoryBufferUnitEnvStatsTemperature':cucsMemoryBufferUnitEnvStatsTemperature,'cucsMemoryBufferUnitEnvStatsTemperatureAvg':cucsMemoryBufferUnitEnvStatsTemperatureAvg,'cucsMemoryBufferUnitEnvStatsTemperatureMax':cucsMemoryBufferUnitEnvStatsTemperatureMax,'cucsMemoryBufferUnitEnvStatsTemperatureMin':cucsMemoryBufferUnitEnvStatsTemperatureMin,'cucsMemoryBufferUnitEnvStatsThresholded':cucsMemoryBufferUnitEnvStatsThresholded,'cucsMemoryBufferUnitEnvStatsTimeCollected':cucsMemoryBufferUnitEnvStatsTimeCollected,'cucsMemoryBufferUnitEnvStatsUpdate':cucsMemoryBufferUnitEnvStatsUpdate,'cucsMemoryBufferUnitEnvStatsHistTable':cucsMemoryBufferUnitEnvStatsHistTable,'cucsMemoryBufferUnitEnvStatsHistEntry':cucsMemoryBufferUnitEnvStatsHistEntry,_J:cucsMemoryBufferUnitEnvStatsHistInstanceId,'cucsMemoryBufferUnitEnvStatsHistDn':cucsMemoryBufferUnitEnvStatsHistDn,'cucsMemoryBufferUnitEnvStatsHistRn':cucsMemoryBufferUnitEnvStatsHistRn,'cucsMemoryBufferUnitEnvStatsHistId':cucsMemoryBufferUnitEnvStatsHistId,'cucsMemoryBufferUnitEnvStatsHistMostRecent':cucsMemoryBufferUnitEnvStatsHistMostRecent,'cucsMemoryBufferUnitEnvStatsHistSuspect':cucsMemoryBufferUnitEnvStatsHistSuspect,'cucsMemoryBufferUnitEnvStatsHistTemperature':cucsMemoryBufferUnitEnvStatsHistTemperature,'cucsMemoryBufferUnitEnvStatsHistTemperatureAvg':cucsMemoryBufferUnitEnvStatsHistTemperatureAvg,'cucsMemoryBufferUnitEnvStatsHistTemperatureMax':cucsMemoryBufferUnitEnvStatsHistTemperatureMax,'cucsMemoryBufferUnitEnvStatsHistTemperatureMin':cucsMemoryBufferUnitEnvStatsHistTemperatureMin,'cucsMemoryBufferUnitEnvStatsHistThresholded':cucsMemoryBufferUnitEnvStatsHistThresholded,'cucsMemoryBufferUnitEnvStatsHistTimeCollected':cucsMemoryBufferUnitEnvStatsHistTimeCollected,'cucsMemoryErrorStatsTable':cucsMemoryErrorStatsTable,'cucsMemoryErrorStatsEntry':cucsMemoryErrorStatsEntry,_K:cucsMemoryErrorStatsInstanceId,'cucsMemoryErrorStatsDn':cucsMemoryErrorStatsDn,'cucsMemoryErrorStatsRn':cucsMemoryErrorStatsRn,'cucsMemoryErrorStatsAddressParityErrors':cucsMemoryErrorStatsAddressParityErrors,'cucsMemoryErrorStatsAddressParityErrors15Min':cucsMemoryErrorStatsAddressParityErrors15Min,'cucsMemoryErrorStatsAddressParityErrors15MinH':cucsMemoryErrorStatsAddressParityErrors15MinH,'cucsMemoryErrorStatsAddressParityErrors1Day':cucsMemoryErrorStatsAddressParityErrors1Day,'cucsMemoryErrorStatsAddressParityErrors1DayH':cucsMemoryErrorStatsAddressParityErrors1DayH,'cucsMemoryErrorStatsAddressParityErrors1Hour':cucsMemoryErrorStatsAddressParityErrors1Hour,'cucsMemoryErrorStatsAddressParityErrors1HourH':cucsMemoryErrorStatsAddressParityErrors1HourH,'cucsMemoryErrorStatsAddressParityErrors1Week':cucsMemoryErrorStatsAddressParityErrors1Week,'cucsMemoryErrorStatsAddressParityErrors1WeekH':cucsMemoryErrorStatsAddressParityErrors1WeekH,'cucsMemoryErrorStatsEccMultibitErrors':cucsMemoryErrorStatsEccMultibitErrors,'cucsMemoryErrorStatsEccMultibitErrors15Min':cucsMemoryErrorStatsEccMultibitErrors15Min,'cucsMemoryErrorStatsEccMultibitErrors15MinH':cucsMemoryErrorStatsEccMultibitErrors15MinH,'cucsMemoryErrorStatsEccMultibitErrors1Day':cucsMemoryErrorStatsEccMultibitErrors1Day,'cucsMemoryErrorStatsEccMultibitErrors1DayH':cucsMemoryErrorStatsEccMultibitErrors1DayH,'cucsMemoryErrorStatsEccMultibitErrors1Hour':cucsMemoryErrorStatsEccMultibitErrors1Hour,'cucsMemoryErrorStatsEccMultibitErrors1HourH':cucsMemoryErrorStatsEccMultibitErrors1HourH,'cucsMemoryErrorStatsEccMultibitErrors1Week':cucsMemoryErrorStatsEccMultibitErrors1Week,'cucsMemoryErrorStatsEccMultibitErrors1WeekH':cucsMemoryErrorStatsEccMultibitErrors1WeekH,'cucsMemoryErrorStatsEccSinglebitErrors':cucsMemoryErrorStatsEccSinglebitErrors,'cucsMemoryErrorStatsEccSinglebitErrors15Min':cucsMemoryErrorStatsEccSinglebitErrors15Min,'cucsMemoryErrorStatsEccSinglebitErrors15MinH':cucsMemoryErrorStatsEccSinglebitErrors15MinH,'cucsMemoryErrorStatsEccSinglebitErrors1Day':cucsMemoryErrorStatsEccSinglebitErrors1Day,'cucsMemoryErrorStatsEccSinglebitErrors1DayH':cucsMemoryErrorStatsEccSinglebitErrors1DayH,'cucsMemoryErrorStatsEccSinglebitErrors1Hour':cucsMemoryErrorStatsEccSinglebitErrors1Hour,'cucsMemoryErrorStatsEccSinglebitErrors1HourH':cucsMemoryErrorStatsEccSinglebitErrors1HourH,'cucsMemoryErrorStatsEccSinglebitErrors1Week':cucsMemoryErrorStatsEccSinglebitErrors1Week,'cucsMemoryErrorStatsEccSinglebitErrors1WeekH':cucsMemoryErrorStatsEccSinglebitErrors1WeekH,'cucsMemoryErrorStatsIntervals':cucsMemoryErrorStatsIntervals,'cucsMemoryErrorStatsMismatchErrors':cucsMemoryErrorStatsMismatchErrors,'cucsMemoryErrorStatsMismatchErrors15Min':cucsMemoryErrorStatsMismatchErrors15Min,'cucsMemoryErrorStatsMismatchErrors15MinH':cucsMemoryErrorStatsMismatchErrors15MinH,'cucsMemoryErrorStatsMismatchErrors1Day':cucsMemoryErrorStatsMismatchErrors1Day,'cucsMemoryErrorStatsMismatchErrors1DayH':cucsMemoryErrorStatsMismatchErrors1DayH,'cucsMemoryErrorStatsMismatchErrors1Hour':cucsMemoryErrorStatsMismatchErrors1Hour,'cucsMemoryErrorStatsMismatchErrors1HourH':cucsMemoryErrorStatsMismatchErrors1HourH,'cucsMemoryErrorStatsMismatchErrors1Week':cucsMemoryErrorStatsMismatchErrors1Week,'cucsMemoryErrorStatsMismatchErrors1WeekH':cucsMemoryErrorStatsMismatchErrors1WeekH,'cucsMemoryErrorStatsSuspect':cucsMemoryErrorStatsSuspect,'cucsMemoryErrorStatsThresholded':cucsMemoryErrorStatsThresholded,'cucsMemoryErrorStatsTimeCollected':cucsMemoryErrorStatsTimeCollected,'cucsMemoryErrorStatsUpdate':cucsMemoryErrorStatsUpdate,'cucsMemoryErrorStatsAddressParityErrors2Weeks':cucsMemoryErrorStatsAddressParityErrors2Weeks,'cucsMemoryErrorStatsAddressParityErrors2WeeksH':cucsMemoryErrorStatsAddressParityErrors2WeeksH,'cucsMemoryErrorStatsEccMultibitErrors2Weeks':cucsMemoryErrorStatsEccMultibitErrors2Weeks,'cucsMemoryErrorStatsEccMultibitErrors2WeeksH':cucsMemoryErrorStatsEccMultibitErrors2WeeksH,'cucsMemoryErrorStatsEccSinglebitErrors2Weeks':cucsMemoryErrorStatsEccSinglebitErrors2Weeks,'cucsMemoryErrorStatsEccSinglebitErrors2WeeksH':cucsMemoryErrorStatsEccSinglebitErrors2WeeksH,'cucsMemoryErrorStatsMismatchErrors2Weeks':cucsMemoryErrorStatsMismatchErrors2Weeks,'cucsMemoryErrorStatsMismatchErrors2WeeksH':cucsMemoryErrorStatsMismatchErrors2WeeksH,'cucsMemoryQualTable':cucsMemoryQualTable,'cucsMemoryQualEntry':cucsMemoryQualEntry,_L:cucsMemoryQualInstanceId,'cucsMemoryQualDn':cucsMemoryQualDn,'cucsMemoryQualRn':cucsMemoryQualRn,'cucsMemoryQualClock':cucsMemoryQualClock,'cucsMemoryQualLatency':cucsMemoryQualLatency,'cucsMemoryQualMaxCap':cucsMemoryQualMaxCap,'cucsMemoryQualMinCap':cucsMemoryQualMinCap,'cucsMemoryQualSpeed':cucsMemoryQualSpeed,'cucsMemoryQualUnits':cucsMemoryQualUnits,'cucsMemoryQualWidth':cucsMemoryQualWidth,'cucsMemoryRuntimeTable':cucsMemoryRuntimeTable,'cucsMemoryRuntimeEntry':cucsMemoryRuntimeEntry,_M:cucsMemoryRuntimeInstanceId,'cucsMemoryRuntimeDn':cucsMemoryRuntimeDn,'cucsMemoryRuntimeRn':cucsMemoryRuntimeRn,'cucsMemoryRuntimeAvailable':cucsMemoryRuntimeAvailable,'cucsMemoryRuntimeAvailableAvg':cucsMemoryRuntimeAvailableAvg,'cucsMemoryRuntimeAvailableMax':cucsMemoryRuntimeAvailableMax,'cucsMemoryRuntimeAvailableMin':cucsMemoryRuntimeAvailableMin,'cucsMemoryRuntimeCached':cucsMemoryRuntimeCached,'cucsMemoryRuntimeCachedAvg':cucsMemoryRuntimeCachedAvg,'cucsMemoryRuntimeCachedMax':cucsMemoryRuntimeCachedMax,'cucsMemoryRuntimeCachedMin':cucsMemoryRuntimeCachedMin,'cucsMemoryRuntimeIntervals':cucsMemoryRuntimeIntervals,'cucsMemoryRuntimeSuspect':cucsMemoryRuntimeSuspect,'cucsMemoryRuntimeThresholded':cucsMemoryRuntimeThresholded,'cucsMemoryRuntimeTimeCollected':cucsMemoryRuntimeTimeCollected,'cucsMemoryRuntimeTotal':cucsMemoryRuntimeTotal,'cucsMemoryRuntimeTotalAvg':cucsMemoryRuntimeTotalAvg,'cucsMemoryRuntimeTotalMax':cucsMemoryRuntimeTotalMax,'cucsMemoryRuntimeTotalMin':cucsMemoryRuntimeTotalMin,'cucsMemoryRuntimeType':cucsMemoryRuntimeType,'cucsMemoryRuntimeUpdate':cucsMemoryRuntimeUpdate,'cucsMemoryRuntimeHistTable':cucsMemoryRuntimeHistTable,'cucsMemoryRuntimeHistEntry':cucsMemoryRuntimeHistEntry,_N:cucsMemoryRuntimeHistInstanceId,'cucsMemoryRuntimeHistDn':cucsMemoryRuntimeHistDn,'cucsMemoryRuntimeHistRn':cucsMemoryRuntimeHistRn,'cucsMemoryRuntimeHistAvailable':cucsMemoryRuntimeHistAvailable,'cucsMemoryRuntimeHistAvailableAvg':cucsMemoryRuntimeHistAvailableAvg,'cucsMemoryRuntimeHistAvailableMax':cucsMemoryRuntimeHistAvailableMax,'cucsMemoryRuntimeHistAvailableMin':cucsMemoryRuntimeHistAvailableMin,'cucsMemoryRuntimeHistCached':cucsMemoryRuntimeHistCached,'cucsMemoryRuntimeHistCachedAvg':cucsMemoryRuntimeHistCachedAvg,'cucsMemoryRuntimeHistCachedMax':cucsMemoryRuntimeHistCachedMax,'cucsMemoryRuntimeHistCachedMin':cucsMemoryRuntimeHistCachedMin,'cucsMemoryRuntimeHistId':cucsMemoryRuntimeHistId,'cucsMemoryRuntimeHistMostRecent':cucsMemoryRuntimeHistMostRecent,'cucsMemoryRuntimeHistSuspect':cucsMemoryRuntimeHistSuspect,'cucsMemoryRuntimeHistThresholded':cucsMemoryRuntimeHistThresholded,'cucsMemoryRuntimeHistTimeCollected':cucsMemoryRuntimeHistTimeCollected,'cucsMemoryRuntimeHistTotal':cucsMemoryRuntimeHistTotal,'cucsMemoryRuntimeHistTotalAvg':cucsMemoryRuntimeHistTotalAvg,'cucsMemoryRuntimeHistTotalMax':cucsMemoryRuntimeHistTotalMax,'cucsMemoryRuntimeHistTotalMin':cucsMemoryRuntimeHistTotalMin,'cucsMemoryUnitTable':cucsMemoryUnitTable,'cucsMemoryUnitEntry':cucsMemoryUnitEntry,_O:cucsMemoryUnitInstanceId,'cucsMemoryUnitDn':cucsMemoryUnitDn,'cucsMemoryUnitRn':cucsMemoryUnitRn,'cucsMemoryUnitArray':cucsMemoryUnitArray,'cucsMemoryUnitBank':cucsMemoryUnitBank,'cucsMemoryUnitCapacity':cucsMemoryUnitCapacity,'cucsMemoryUnitClock':cucsMemoryUnitClock,'cucsMemoryUnitFormFactor':cucsMemoryUnitFormFactor,'cucsMemoryUnitId':cucsMemoryUnitId,'cucsMemoryUnitLatency':cucsMemoryUnitLatency,'cucsMemoryUnitLocation':cucsMemoryUnitLocation,'cucsMemoryUnitModel':cucsMemoryUnitModel,'cucsMemoryUnitOperState':cucsMemoryUnitOperState,'cucsMemoryUnitOperability':cucsMemoryUnitOperability,'cucsMemoryUnitPerf':cucsMemoryUnitPerf,'cucsMemoryUnitPower':cucsMemoryUnitPower,'cucsMemoryUnitPresence':cucsMemoryUnitPresence,'cucsMemoryUnitRevision':cucsMemoryUnitRevision,'cucsMemoryUnitSerial':cucsMemoryUnitSerial,'cucsMemoryUnitSet':cucsMemoryUnitSet,'cucsMemoryUnitSpeed':cucsMemoryUnitSpeed,'cucsMemoryUnitThermal':cucsMemoryUnitThermal,'cucsMemoryUnitType':cucsMemoryUnitType,'cucsMemoryUnitVendor':cucsMemoryUnitVendor,'cucsMemoryUnitVisibility':cucsMemoryUnitVisibility,'cucsMemoryUnitVoltage':cucsMemoryUnitVoltage,'cucsMemoryUnitWidth':cucsMemoryUnitWidth,'cucsMemoryUnitAdminState':cucsMemoryUnitAdminState,'cucsMemoryUnitOperQualifier':cucsMemoryUnitOperQualifier,'cucsMemoryUnitOperQualifierReason':cucsMemoryUnitOperQualifierReason,'cucsMemoryUnitLocationDn':cucsMemoryUnitLocationDn,'cucsMemoryUnitEnvStatsTable':cucsMemoryUnitEnvStatsTable,'cucsMemoryUnitEnvStatsEntry':cucsMemoryUnitEnvStatsEntry,_P:cucsMemoryUnitEnvStatsInstanceId,'cucsMemoryUnitEnvStatsDn':cucsMemoryUnitEnvStatsDn,'cucsMemoryUnitEnvStatsRn':cucsMemoryUnitEnvStatsRn,'cucsMemoryUnitEnvStatsIntervals':cucsMemoryUnitEnvStatsIntervals,'cucsMemoryUnitEnvStatsSuspect':cucsMemoryUnitEnvStatsSuspect,'cucsMemoryUnitEnvStatsTemperature':cucsMemoryUnitEnvStatsTemperature,'cucsMemoryUnitEnvStatsTemperatureAvg':cucsMemoryUnitEnvStatsTemperatureAvg,'cucsMemoryUnitEnvStatsTemperatureMax':cucsMemoryUnitEnvStatsTemperatureMax,'cucsMemoryUnitEnvStatsTemperatureMin':cucsMemoryUnitEnvStatsTemperatureMin,'cucsMemoryUnitEnvStatsThresholded':cucsMemoryUnitEnvStatsThresholded,'cucsMemoryUnitEnvStatsTimeCollected':cucsMemoryUnitEnvStatsTimeCollected,'cucsMemoryUnitEnvStatsUpdate':cucsMemoryUnitEnvStatsUpdate,'cucsMemoryUnitEnvStatsHistTable':cucsMemoryUnitEnvStatsHistTable,'cucsMemoryUnitEnvStatsHistEntry':cucsMemoryUnitEnvStatsHistEntry,_Q:cucsMemoryUnitEnvStatsHistInstanceId,'cucsMemoryUnitEnvStatsHistDn':cucsMemoryUnitEnvStatsHistDn,'cucsMemoryUnitEnvStatsHistRn':cucsMemoryUnitEnvStatsHistRn,'cucsMemoryUnitEnvStatsHistId':cucsMemoryUnitEnvStatsHistId,'cucsMemoryUnitEnvStatsHistMostRecent':cucsMemoryUnitEnvStatsHistMostRecent,'cucsMemoryUnitEnvStatsHistSuspect':cucsMemoryUnitEnvStatsHistSuspect,'cucsMemoryUnitEnvStatsHistTemperature':cucsMemoryUnitEnvStatsHistTemperature,'cucsMemoryUnitEnvStatsHistTemperatureAvg':cucsMemoryUnitEnvStatsHistTemperatureAvg,'cucsMemoryUnitEnvStatsHistTemperatureMax':cucsMemoryUnitEnvStatsHistTemperatureMax,'cucsMemoryUnitEnvStatsHistTemperatureMin':cucsMemoryUnitEnvStatsHistTemperatureMin,'cucsMemoryUnitEnvStatsHistThresholded':cucsMemoryUnitEnvStatsHistThresholded,'cucsMemoryUnitEnvStatsHistTimeCollected':cucsMemoryUnitEnvStatsHistTimeCollected})