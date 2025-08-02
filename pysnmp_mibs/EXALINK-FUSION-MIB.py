_X='fusionTimeSourceStatus'
_W='fusionPortUsageStatus'
_V='fusionPortLinkStatus'
_U='fusionPortName'
_T='fusionFanFaultStatus'
_S='fusionPsuFaultStatus'
_R='fusionHighTempStatus'
_Q='fusionTempSensorName'
_P='fusionLidOpenStatus'
_O='unused'
_N='read-write'
_M='fusionPortIndex'
_L='fusionPortLineCard'
_K='fusionPsuIndex'
_J='fusionFanSensorIndex'
_I='Celsius'
_H='fusionTempSensorIndex'
_G='fusionModuleIndex'
_F='fusionLineCardIndex'
_E='Integer32'
_D='EXALINK-FUSION-MIB'
_C='Packets'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
exaFusion=ModuleIdentity((1,3,6,1,4,1,43296,3))
if mibBuilder.loadTexts:exaFusion.setRevisions(('2019-12-04 00:00','2019-07-16 00:00','2019-07-02 00:00','2018-08-06 00:00','2017-03-16 00:01','2017-03-16 00:00','2015-10-20 00:00','2015-07-30 00:00','2015-04-13 00:00'))
_FusionInfo_ObjectIdentity=ObjectIdentity
fusionInfo=_FusionInfo_ObjectIdentity((1,3,6,1,4,1,43296,3,1))
_FusionInfoSerial_Type=SnmpAdminString
_FusionInfoSerial_Object=MibScalar
fusionInfoSerial=_FusionInfoSerial_Object((1,3,6,1,4,1,43296,3,1,1),_FusionInfoSerial_Type())
fusionInfoSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionInfoSerial.setStatus(_A)
_FusionInfoVersion_Type=SnmpAdminString
_FusionInfoVersion_Object=MibScalar
fusionInfoVersion=_FusionInfoVersion_Object((1,3,6,1,4,1,43296,3,1,2),_FusionInfoVersion_Type())
fusionInfoVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionInfoVersion.setStatus(_A)
_FusionInfoBoard_Type=SnmpAdminString
_FusionInfoBoard_Object=MibScalar
fusionInfoBoard=_FusionInfoBoard_Object((1,3,6,1,4,1,43296,3,1,3),_FusionInfoBoard_Type())
fusionInfoBoard.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionInfoBoard.setStatus(_A)
_FusionInfoSoftware_Type=SnmpAdminString
_FusionInfoSoftware_Object=MibScalar
fusionInfoSoftware=_FusionInfoSoftware_Object((1,3,6,1,4,1,43296,3,1,4),_FusionInfoSoftware_Type())
fusionInfoSoftware.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionInfoSoftware.setStatus(_A)
_FusionLineCardTable_Object=MibTable
fusionLineCardTable=_FusionLineCardTable_Object((1,3,6,1,4,1,43296,3,1,5))
if mibBuilder.loadTexts:fusionLineCardTable.setStatus(_A)
_FusionLineCard_Object=MibTableRow
fusionLineCard=_FusionLineCard_Object((1,3,6,1,4,1,43296,3,1,5,1))
fusionLineCard.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:fusionLineCard.setStatus(_A)
class _FusionLineCardIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FusionLineCardIndex_Type.__name__=_E
_FusionLineCardIndex_Object=MibTableColumn
fusionLineCardIndex=_FusionLineCardIndex_Object((1,3,6,1,4,1,43296,3,1,5,1,1),_FusionLineCardIndex_Type())
fusionLineCardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionLineCardIndex.setStatus(_A)
_FusionLineCardName_Type=SnmpAdminString
_FusionLineCardName_Object=MibTableColumn
fusionLineCardName=_FusionLineCardName_Object((1,3,6,1,4,1,43296,3,1,5,1,2),_FusionLineCardName_Type())
fusionLineCardName.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionLineCardName.setStatus(_A)
_FusionLineCardBoard_Type=SnmpAdminString
_FusionLineCardBoard_Object=MibTableColumn
fusionLineCardBoard=_FusionLineCardBoard_Object((1,3,6,1,4,1,43296,3,1,5,1,3),_FusionLineCardBoard_Type())
fusionLineCardBoard.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionLineCardBoard.setStatus(_A)
_FusionModuleTable_Object=MibTable
fusionModuleTable=_FusionModuleTable_Object((1,3,6,1,4,1,43296,3,1,6))
if mibBuilder.loadTexts:fusionModuleTable.setStatus(_A)
_FusionModule_Object=MibTableRow
fusionModule=_FusionModule_Object((1,3,6,1,4,1,43296,3,1,6,1))
fusionModule.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fusionModule.setStatus(_A)
class _FusionModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FusionModuleIndex_Type.__name__=_E
_FusionModuleIndex_Object=MibTableColumn
fusionModuleIndex=_FusionModuleIndex_Object((1,3,6,1,4,1,43296,3,1,6,1,1),_FusionModuleIndex_Type())
fusionModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionModuleIndex.setStatus(_A)
_FusionModuleName_Type=SnmpAdminString
_FusionModuleName_Object=MibTableColumn
fusionModuleName=_FusionModuleName_Object((1,3,6,1,4,1,43296,3,1,6,1,2),_FusionModuleName_Type())
fusionModuleName.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionModuleName.setStatus(_A)
_FusionModuleBoard_Type=SnmpAdminString
_FusionModuleBoard_Object=MibTableColumn
fusionModuleBoard=_FusionModuleBoard_Object((1,3,6,1,4,1,43296,3,1,6,1,3),_FusionModuleBoard_Type())
fusionModuleBoard.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionModuleBoard.setStatus(_A)
_FusionModuleFunction_Type=SnmpAdminString
_FusionModuleFunction_Object=MibTableColumn
fusionModuleFunction=_FusionModuleFunction_Object((1,3,6,1,4,1,43296,3,1,6,1,4),_FusionModuleFunction_Type())
fusionModuleFunction.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionModuleFunction.setStatus(_A)
_FusionSysInfo_ObjectIdentity=ObjectIdentity
fusionSysInfo=_FusionSysInfo_ObjectIdentity((1,3,6,1,4,1,43296,3,1,7))
_FusionSysInfoLoadAverage_Type=Integer32
_FusionSysInfoLoadAverage_Object=MibScalar
fusionSysInfoLoadAverage=_FusionSysInfoLoadAverage_Object((1,3,6,1,4,1,43296,3,1,7,1),_FusionSysInfoLoadAverage_Type())
fusionSysInfoLoadAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionSysInfoLoadAverage.setStatus(_A)
_FusionSysInfoAvailMem_Type=Integer32
_FusionSysInfoAvailMem_Object=MibScalar
fusionSysInfoAvailMem=_FusionSysInfoAvailMem_Object((1,3,6,1,4,1,43296,3,1,7,2),_FusionSysInfoAvailMem_Type())
fusionSysInfoAvailMem.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionSysInfoAvailMem.setStatus(_A)
_FusionSysInfoNumProcesses_Type=Integer32
_FusionSysInfoNumProcesses_Object=MibScalar
fusionSysInfoNumProcesses=_FusionSysInfoNumProcesses_Object((1,3,6,1,4,1,43296,3,1,7,3),_FusionSysInfoNumProcesses_Type())
fusionSysInfoNumProcesses.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionSysInfoNumProcesses.setStatus(_A)
_FusionSensor_ObjectIdentity=ObjectIdentity
fusionSensor=_FusionSensor_ObjectIdentity((1,3,6,1,4,1,43296,3,2))
_FusionTempSensorTable_Object=MibTable
fusionTempSensorTable=_FusionTempSensorTable_Object((1,3,6,1,4,1,43296,3,2,1))
if mibBuilder.loadTexts:fusionTempSensorTable.setStatus(_A)
_FusionTempSensor_Object=MibTableRow
fusionTempSensor=_FusionTempSensor_Object((1,3,6,1,4,1,43296,3,2,1,1))
fusionTempSensor.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:fusionTempSensor.setStatus(_A)
class _FusionTempSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FusionTempSensorIndex_Type.__name__=_E
_FusionTempSensorIndex_Object=MibTableColumn
fusionTempSensorIndex=_FusionTempSensorIndex_Object((1,3,6,1,4,1,43296,3,2,1,1,1),_FusionTempSensorIndex_Type())
fusionTempSensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionTempSensorIndex.setStatus(_A)
_FusionTempSensorName_Type=SnmpAdminString
_FusionTempSensorName_Object=MibTableColumn
fusionTempSensorName=_FusionTempSensorName_Object((1,3,6,1,4,1,43296,3,2,1,1,2),_FusionTempSensorName_Type())
fusionTempSensorName.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionTempSensorName.setStatus(_A)
_FusionTempSensorValue_Type=Integer32
_FusionTempSensorValue_Object=MibTableColumn
fusionTempSensorValue=_FusionTempSensorValue_Object((1,3,6,1,4,1,43296,3,2,1,1,3),_FusionTempSensorValue_Type())
fusionTempSensorValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionTempSensorValue.setStatus(_A)
if mibBuilder.loadTexts:fusionTempSensorValue.setUnits(_I)
_FusionFanSensorTable_Object=MibTable
fusionFanSensorTable=_FusionFanSensorTable_Object((1,3,6,1,4,1,43296,3,2,2))
if mibBuilder.loadTexts:fusionFanSensorTable.setStatus(_A)
_FusionFanSensor_Object=MibTableRow
fusionFanSensor=_FusionFanSensor_Object((1,3,6,1,4,1,43296,3,2,2,1))
fusionFanSensor.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:fusionFanSensor.setStatus(_A)
class _FusionFanSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FusionFanSensorIndex_Type.__name__=_E
_FusionFanSensorIndex_Object=MibTableColumn
fusionFanSensorIndex=_FusionFanSensorIndex_Object((1,3,6,1,4,1,43296,3,2,2,1,1),_FusionFanSensorIndex_Type())
fusionFanSensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionFanSensorIndex.setStatus(_A)
_FusionFanSensorName_Type=SnmpAdminString
_FusionFanSensorName_Object=MibTableColumn
fusionFanSensorName=_FusionFanSensorName_Object((1,3,6,1,4,1,43296,3,2,2,1,2),_FusionFanSensorName_Type())
fusionFanSensorName.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionFanSensorName.setStatus(_A)
_FusionFanSensorValue_Type=Integer32
_FusionFanSensorValue_Object=MibTableColumn
fusionFanSensorValue=_FusionFanSensorValue_Object((1,3,6,1,4,1,43296,3,2,2,1,3),_FusionFanSensorValue_Type())
fusionFanSensorValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionFanSensorValue.setStatus(_A)
if mibBuilder.loadTexts:fusionFanSensorValue.setUnits('RPM')
_FusionPsuTable_Object=MibTable
fusionPsuTable=_FusionPsuTable_Object((1,3,6,1,4,1,43296,3,3))
if mibBuilder.loadTexts:fusionPsuTable.setStatus(_A)
_FusionPsu_Object=MibTableRow
fusionPsu=_FusionPsu_Object((1,3,6,1,4,1,43296,3,3,1))
fusionPsu.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:fusionPsu.setStatus(_A)
class _FusionPsuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FusionPsuIndex_Type.__name__=_E
_FusionPsuIndex_Object=MibTableColumn
fusionPsuIndex=_FusionPsuIndex_Object((1,3,6,1,4,1,43296,3,3,1,1),_FusionPsuIndex_Type())
fusionPsuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPsuIndex.setStatus(_A)
_FusionPsuType_Type=SnmpAdminString
_FusionPsuType_Object=MibTableColumn
fusionPsuType=_FusionPsuType_Object((1,3,6,1,4,1,43296,3,3,1,2),_FusionPsuType_Type())
fusionPsuType.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPsuType.setStatus(_A)
_FusionPsuPresent_Type=TruthValue
_FusionPsuPresent_Object=MibTableColumn
fusionPsuPresent=_FusionPsuPresent_Object((1,3,6,1,4,1,43296,3,3,1,3),_FusionPsuPresent_Type())
fusionPsuPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPsuPresent.setStatus(_A)
_FusionPsuTemperature_Type=Integer32
_FusionPsuTemperature_Object=MibTableColumn
fusionPsuTemperature=_FusionPsuTemperature_Object((1,3,6,1,4,1,43296,3,3,1,4),_FusionPsuTemperature_Type())
fusionPsuTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPsuTemperature.setStatus(_A)
if mibBuilder.loadTexts:fusionPsuTemperature.setUnits(_I)
_FusionPsuPowerIn_Type=Integer32
_FusionPsuPowerIn_Object=MibTableColumn
fusionPsuPowerIn=_FusionPsuPowerIn_Object((1,3,6,1,4,1,43296,3,3,1,5),_FusionPsuPowerIn_Type())
fusionPsuPowerIn.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPsuPowerIn.setStatus(_A)
if mibBuilder.loadTexts:fusionPsuPowerIn.setUnits('Watts')
_FusionPsuPowerOut_Type=Integer32
_FusionPsuPowerOut_Object=MibTableColumn
fusionPsuPowerOut=_FusionPsuPowerOut_Object((1,3,6,1,4,1,43296,3,3,1,6),_FusionPsuPowerOut_Type())
fusionPsuPowerOut.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPsuPowerOut.setStatus(_A)
if mibBuilder.loadTexts:fusionPsuPowerOut.setUnits('Watts')
_FusionPortTable_Object=MibTable
fusionPortTable=_FusionPortTable_Object((1,3,6,1,4,1,43296,3,4))
if mibBuilder.loadTexts:fusionPortTable.setStatus(_A)
_FusionPort_Object=MibTableRow
fusionPort=_FusionPort_Object((1,3,6,1,4,1,43296,3,4,1))
fusionPort.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:fusionPort.setStatus(_A)
class _FusionPortLineCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FusionPortLineCard_Type.__name__=_E
_FusionPortLineCard_Object=MibTableColumn
fusionPortLineCard=_FusionPortLineCard_Object((1,3,6,1,4,1,43296,3,4,1,1),_FusionPortLineCard_Type())
fusionPortLineCard.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortLineCard.setStatus(_A)
class _FusionPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FusionPortIndex_Type.__name__=_E
_FusionPortIndex_Object=MibTableColumn
fusionPortIndex=_FusionPortIndex_Object((1,3,6,1,4,1,43296,3,4,1,2),_FusionPortIndex_Type())
fusionPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortIndex.setStatus(_A)
_FusionPortName_Type=SnmpAdminString
_FusionPortName_Object=MibTableColumn
fusionPortName=_FusionPortName_Object((1,3,6,1,4,1,43296,3,4,1,3),_FusionPortName_Type())
fusionPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortName.setStatus(_A)
_FusionPortPresent_Type=TruthValue
_FusionPortPresent_Object=MibTableColumn
fusionPortPresent=_FusionPortPresent_Object((1,3,6,1,4,1,43296,3,4,1,4),_FusionPortPresent_Type())
fusionPortPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortPresent.setStatus(_A)
_FusionPortHasSignal_Type=TruthValue
_FusionPortHasSignal_Object=MibTableColumn
fusionPortHasSignal=_FusionPortHasSignal_Object((1,3,6,1,4,1,43296,3,4,1,5),_FusionPortHasSignal_Type())
fusionPortHasSignal.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortHasSignal.setStatus(_A)
_FusionPortEnabled_Type=TruthValue
_FusionPortEnabled_Object=MibTableColumn
fusionPortEnabled=_FusionPortEnabled_Object((1,3,6,1,4,1,43296,3,4,1,6),_FusionPortEnabled_Type())
fusionPortEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortEnabled.setStatus(_A)
_FusionPortAlias_Type=SnmpAdminString
_FusionPortAlias_Object=MibTableColumn
fusionPortAlias=_FusionPortAlias_Object((1,3,6,1,4,1,43296,3,4,1,7),_FusionPortAlias_Type())
fusionPortAlias.setMaxAccess(_N)
if mibBuilder.loadTexts:fusionPortAlias.setStatus(_A)
_FusionPortSpeed_Type=Integer32
_FusionPortSpeed_Object=MibTableColumn
fusionPortSpeed=_FusionPortSpeed_Object((1,3,6,1,4,1,43296,3,4,1,8),_FusionPortSpeed_Type())
fusionPortSpeed.setMaxAccess(_N)
if mibBuilder.loadTexts:fusionPortSpeed.setStatus(_A)
if mibBuilder.loadTexts:fusionPortSpeed.setUnits('Mbps')
_FusionPortRXPackets_Type=Counter64
_FusionPortRXPackets_Object=MibTableColumn
fusionPortRXPackets=_FusionPortRXPackets_Object((1,3,6,1,4,1,43296,3,4,1,9),_FusionPortRXPackets_Type())
fusionPortRXPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRXPackets.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRXPackets.setUnits(_C)
_FusionPortRXBytes_Type=Counter64
_FusionPortRXBytes_Object=MibTableColumn
fusionPortRXBytes=_FusionPortRXBytes_Object((1,3,6,1,4,1,43296,3,4,1,10),_FusionPortRXBytes_Type())
fusionPortRXBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRXBytes.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRXBytes.setUnits('B')
_FusionPortRXErrors_Type=Counter64
_FusionPortRXErrors_Object=MibTableColumn
fusionPortRXErrors=_FusionPortRXErrors_Object((1,3,6,1,4,1,43296,3,4,1,11),_FusionPortRXErrors_Type())
fusionPortRXErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRXErrors.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRXErrors.setUnits(_C)
_FusionPortTXPackets_Type=Counter64
_FusionPortTXPackets_Object=MibTableColumn
fusionPortTXPackets=_FusionPortTXPackets_Object((1,3,6,1,4,1,43296,3,4,1,12),_FusionPortTXPackets_Type())
fusionPortTXPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortTXPackets.setStatus(_A)
if mibBuilder.loadTexts:fusionPortTXPackets.setUnits(_C)
_FusionPortTXBytes_Type=Counter64
_FusionPortTXBytes_Object=MibTableColumn
fusionPortTXBytes=_FusionPortTXBytes_Object((1,3,6,1,4,1,43296,3,4,1,13),_FusionPortTXBytes_Type())
fusionPortTXBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortTXBytes.setStatus(_A)
if mibBuilder.loadTexts:fusionPortTXBytes.setUnits('B')
_FusionPortRXLink_Type=TruthValue
_FusionPortRXLink_Object=MibTableColumn
fusionPortRXLink=_FusionPortRXLink_Object((1,3,6,1,4,1,43296,3,4,1,14),_FusionPortRXLink_Type())
fusionPortRXLink.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRXLink.setStatus(_A)
_FusionPortRXLinkChanges_Type=Counter64
_FusionPortRXLinkChanges_Object=MibTableColumn
fusionPortRXLinkChanges=_FusionPortRXLinkChanges_Object((1,3,6,1,4,1,43296,3,4,1,15),_FusionPortRXLinkChanges_Type())
fusionPortRXLinkChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRXLinkChanges.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRXLinkChanges.setUnits('State changes')
_FusionPortRXDropped_Type=Counter64
_FusionPortRXDropped_Object=MibTableColumn
fusionPortRXDropped=_FusionPortRXDropped_Object((1,3,6,1,4,1,43296,3,4,1,16),_FusionPortRXDropped_Type())
fusionPortRXDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRXDropped.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRXDropped.setUnits(_C)
_FusionPortRXUnicast_Type=Counter64
_FusionPortRXUnicast_Object=MibTableColumn
fusionPortRXUnicast=_FusionPortRXUnicast_Object((1,3,6,1,4,1,43296,3,4,1,17),_FusionPortRXUnicast_Type())
fusionPortRXUnicast.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRXUnicast.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRXUnicast.setUnits(_C)
_FusionPortRXMulticast_Type=Counter64
_FusionPortRXMulticast_Object=MibTableColumn
fusionPortRXMulticast=_FusionPortRXMulticast_Object((1,3,6,1,4,1,43296,3,4,1,18),_FusionPortRXMulticast_Type())
fusionPortRXMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRXMulticast.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRXMulticast.setUnits(_C)
_FusionPortRXBroadcast_Type=Counter64
_FusionPortRXBroadcast_Object=MibTableColumn
fusionPortRXBroadcast=_FusionPortRXBroadcast_Object((1,3,6,1,4,1,43296,3,4,1,19),_FusionPortRXBroadcast_Type())
fusionPortRXBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRXBroadcast.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRXBroadcast.setUnits(_C)
_FusionPortRXRunt_Type=Counter64
_FusionPortRXRunt_Object=MibTableColumn
fusionPortRXRunt=_FusionPortRXRunt_Object((1,3,6,1,4,1,43296,3,4,1,20),_FusionPortRXRunt_Type())
fusionPortRXRunt.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRXRunt.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRXRunt.setUnits(_C)
_FusionPortRXPause_Type=Counter64
_FusionPortRXPause_Object=MibTableColumn
fusionPortRXPause=_FusionPortRXPause_Object((1,3,6,1,4,1,43296,3,4,1,21),_FusionPortRXPause_Type())
fusionPortRXPause.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRXPause.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRXPause.setUnits(_C)
_FusionPortRX64b_Type=Counter64
_FusionPortRX64b_Object=MibTableColumn
fusionPortRX64b=_FusionPortRX64b_Object((1,3,6,1,4,1,43296,3,4,1,22),_FusionPortRX64b_Type())
fusionPortRX64b.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRX64b.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRX64b.setUnits(_C)
_FusionPortRX65to127b_Type=Counter64
_FusionPortRX65to127b_Object=MibTableColumn
fusionPortRX65to127b=_FusionPortRX65to127b_Object((1,3,6,1,4,1,43296,3,4,1,23),_FusionPortRX65to127b_Type())
fusionPortRX65to127b.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRX65to127b.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRX65to127b.setUnits(_C)
_FusionPortRX128to255b_Type=Counter64
_FusionPortRX128to255b_Object=MibTableColumn
fusionPortRX128to255b=_FusionPortRX128to255b_Object((1,3,6,1,4,1,43296,3,4,1,24),_FusionPortRX128to255b_Type())
fusionPortRX128to255b.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRX128to255b.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRX128to255b.setUnits(_C)
_FusionPortRX256to511b_Type=Counter64
_FusionPortRX256to511b_Object=MibTableColumn
fusionPortRX256to511b=_FusionPortRX256to511b_Object((1,3,6,1,4,1,43296,3,4,1,25),_FusionPortRX256to511b_Type())
fusionPortRX256to511b.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRX256to511b.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRX256to511b.setUnits(_C)
_FusionPortRX512to1023b_Type=Counter64
_FusionPortRX512to1023b_Object=MibTableColumn
fusionPortRX512to1023b=_FusionPortRX512to1023b_Object((1,3,6,1,4,1,43296,3,4,1,26),_FusionPortRX512to1023b_Type())
fusionPortRX512to1023b.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRX512to1023b.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRX512to1023b.setUnits(_C)
_FusionPortRX1024to1518b_Type=Counter64
_FusionPortRX1024to1518b_Object=MibTableColumn
fusionPortRX1024to1518b=_FusionPortRX1024to1518b_Object((1,3,6,1,4,1,43296,3,4,1,27),_FusionPortRX1024to1518b_Type())
fusionPortRX1024to1518b.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRX1024to1518b.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRX1024to1518b.setUnits(_C)
_FusionPortRX1519to1522b_Type=Counter64
_FusionPortRX1519to1522b_Object=MibTableColumn
fusionPortRX1519to1522b=_FusionPortRX1519to1522b_Object((1,3,6,1,4,1,43296,3,4,1,28),_FusionPortRX1519to1522b_Type())
fusionPortRX1519to1522b.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortRX1519to1522b.setStatus(_A)
if mibBuilder.loadTexts:fusionPortRX1519to1522b.setUnits(_C)
_FusionPortTXUnicast_Type=Counter64
_FusionPortTXUnicast_Object=MibTableColumn
fusionPortTXUnicast=_FusionPortTXUnicast_Object((1,3,6,1,4,1,43296,3,4,1,29),_FusionPortTXUnicast_Type())
fusionPortTXUnicast.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortTXUnicast.setStatus(_A)
if mibBuilder.loadTexts:fusionPortTXUnicast.setUnits(_C)
_FusionPortTXMulticast_Type=Counter64
_FusionPortTXMulticast_Object=MibTableColumn
fusionPortTXMulticast=_FusionPortTXMulticast_Object((1,3,6,1,4,1,43296,3,4,1,30),_FusionPortTXMulticast_Type())
fusionPortTXMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortTXMulticast.setStatus(_A)
if mibBuilder.loadTexts:fusionPortTXMulticast.setUnits(_C)
_FusionPortTXBroadcast_Type=Counter64
_FusionPortTXBroadcast_Object=MibTableColumn
fusionPortTXBroadcast=_FusionPortTXBroadcast_Object((1,3,6,1,4,1,43296,3,4,1,31),_FusionPortTXBroadcast_Type())
fusionPortTXBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortTXBroadcast.setStatus(_A)
if mibBuilder.loadTexts:fusionPortTXBroadcast.setUnits(_C)
_FusionPortTX64b_Type=Counter64
_FusionPortTX64b_Object=MibTableColumn
fusionPortTX64b=_FusionPortTX64b_Object((1,3,6,1,4,1,43296,3,4,1,32),_FusionPortTX64b_Type())
fusionPortTX64b.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortTX64b.setStatus(_A)
if mibBuilder.loadTexts:fusionPortTX64b.setUnits(_C)
_FusionPortTX65to127b_Type=Counter64
_FusionPortTX65to127b_Object=MibTableColumn
fusionPortTX65to127b=_FusionPortTX65to127b_Object((1,3,6,1,4,1,43296,3,4,1,33),_FusionPortTX65to127b_Type())
fusionPortTX65to127b.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortTX65to127b.setStatus(_A)
if mibBuilder.loadTexts:fusionPortTX65to127b.setUnits(_C)
_FusionPortTX128to255b_Type=Counter64
_FusionPortTX128to255b_Object=MibTableColumn
fusionPortTX128to255b=_FusionPortTX128to255b_Object((1,3,6,1,4,1,43296,3,4,1,34),_FusionPortTX128to255b_Type())
fusionPortTX128to255b.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortTX128to255b.setStatus(_A)
if mibBuilder.loadTexts:fusionPortTX128to255b.setUnits(_C)
_FusionPortTX256to511b_Type=Counter64
_FusionPortTX256to511b_Object=MibTableColumn
fusionPortTX256to511b=_FusionPortTX256to511b_Object((1,3,6,1,4,1,43296,3,4,1,35),_FusionPortTX256to511b_Type())
fusionPortTX256to511b.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortTX256to511b.setStatus(_A)
if mibBuilder.loadTexts:fusionPortTX256to511b.setUnits(_C)
_FusionPortTX512to1023b_Type=Counter64
_FusionPortTX512to1023b_Object=MibTableColumn
fusionPortTX512to1023b=_FusionPortTX512to1023b_Object((1,3,6,1,4,1,43296,3,4,1,36),_FusionPortTX512to1023b_Type())
fusionPortTX512to1023b.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortTX512to1023b.setStatus(_A)
if mibBuilder.loadTexts:fusionPortTX512to1023b.setUnits(_C)
_FusionPortTX1024to1518b_Type=Counter64
_FusionPortTX1024to1518b_Object=MibTableColumn
fusionPortTX1024to1518b=_FusionPortTX1024to1518b_Object((1,3,6,1,4,1,43296,3,4,1,37),_FusionPortTX1024to1518b_Type())
fusionPortTX1024to1518b.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortTX1024to1518b.setStatus(_A)
if mibBuilder.loadTexts:fusionPortTX1024to1518b.setUnits(_C)
_FusionPortTX1519to1522b_Type=Counter64
_FusionPortTX1519to1522b_Object=MibTableColumn
fusionPortTX1519to1522b=_FusionPortTX1519to1522b_Object((1,3,6,1,4,1,43296,3,4,1,38),_FusionPortTX1519to1522b_Type())
fusionPortTX1519to1522b.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortTX1519to1522b.setStatus(_A)
if mibBuilder.loadTexts:fusionPortTX1519to1522b.setUnits(_C)
_FusionPortL1Source_Type=SnmpAdminString
_FusionPortL1Source_Object=MibTableColumn
fusionPortL1Source=_FusionPortL1Source_Object((1,3,6,1,4,1,43296,3,4,1,39),_FusionPortL1Source_Type())
fusionPortL1Source.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortL1Source.setStatus(_A)
_FusionTrapValues_ObjectIdentity=ObjectIdentity
fusionTrapValues=_FusionTrapValues_ObjectIdentity((1,3,6,1,4,1,43296,3,5))
_FusionLidOpenStatus_Type=TruthValue
_FusionLidOpenStatus_Object=MibScalar
fusionLidOpenStatus=_FusionLidOpenStatus_Object((1,3,6,1,4,1,43296,3,5,1),_FusionLidOpenStatus_Type())
fusionLidOpenStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionLidOpenStatus.setStatus(_A)
_FusionFanFaultStatus_Type=TruthValue
_FusionFanFaultStatus_Object=MibScalar
fusionFanFaultStatus=_FusionFanFaultStatus_Object((1,3,6,1,4,1,43296,3,5,2),_FusionFanFaultStatus_Type())
fusionFanFaultStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionFanFaultStatus.setStatus(_A)
_FusionHighTempStatus_Type=TruthValue
_FusionHighTempStatus_Object=MibScalar
fusionHighTempStatus=_FusionHighTempStatus_Object((1,3,6,1,4,1,43296,3,5,3),_FusionHighTempStatus_Type())
fusionHighTempStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionHighTempStatus.setStatus(_A)
class _FusionPortUsageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('off',0),('error',1),(_O,2),('ok',3)))
_FusionPortUsageStatus_Type.__name__=_E
_FusionPortUsageStatus_Object=MibScalar
fusionPortUsageStatus=_FusionPortUsageStatus_Object((1,3,6,1,4,1,43296,3,5,4),_FusionPortUsageStatus_Type())
fusionPortUsageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortUsageStatus.setStatus(_A)
class _FusionPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('off',0),('error',1),(_O,2),('ok',3)))
_FusionPortLinkStatus_Type.__name__=_E
_FusionPortLinkStatus_Object=MibScalar
fusionPortLinkStatus=_FusionPortLinkStatus_Object((1,3,6,1,4,1,43296,3,5,5),_FusionPortLinkStatus_Type())
fusionPortLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPortLinkStatus.setStatus(_A)
_FusionPsuFaultStatus_Type=TruthValue
_FusionPsuFaultStatus_Object=MibScalar
fusionPsuFaultStatus=_FusionPsuFaultStatus_Object((1,3,6,1,4,1,43296,3,5,6),_FusionPsuFaultStatus_Type())
fusionPsuFaultStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionPsuFaultStatus.setStatus(_A)
_FusionTimeSourceStatus_Type=TruthValue
_FusionTimeSourceStatus_Object=MibScalar
fusionTimeSourceStatus=_FusionTimeSourceStatus_Object((1,3,6,1,4,1,43296,3,5,7),_FusionTimeSourceStatus_Type())
fusionTimeSourceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fusionTimeSourceStatus.setStatus(_A)
_FusionTraps_ObjectIdentity=ObjectIdentity
fusionTraps=_FusionTraps_ObjectIdentity((1,3,6,1,4,1,43296,3,6))
fusionPowerFail=NotificationType((1,3,6,1,4,1,43296,3,6,1))
if mibBuilder.loadTexts:fusionPowerFail.setStatus(_A)
fusionTamperAlert=NotificationType((1,3,6,1,4,1,43296,3,6,2))
fusionTamperAlert.setObjects((_D,_P))
if mibBuilder.loadTexts:fusionTamperAlert.setStatus(_A)
fusionTempAlert=NotificationType((1,3,6,1,4,1,43296,3,6,3))
fusionTempAlert.setObjects(*((_D,_Q),(_D,_R)))
if mibBuilder.loadTexts:fusionTempAlert.setStatus(_A)
fusionPsuAlert=NotificationType((1,3,6,1,4,1,43296,3,6,4))
fusionPsuAlert.setObjects((_D,_S))
if mibBuilder.loadTexts:fusionPsuAlert.setStatus(_A)
fusionSystemAlert=NotificationType((1,3,6,1,4,1,43296,3,6,5))
if mibBuilder.loadTexts:fusionSystemAlert.setStatus(_A)
fusionFanAlert=NotificationType((1,3,6,1,4,1,43296,3,6,6))
fusionFanAlert.setObjects((_D,_T))
if mibBuilder.loadTexts:fusionFanAlert.setStatus(_A)
fusionPortAlert=NotificationType((1,3,6,1,4,1,43296,3,6,7))
fusionPortAlert.setObjects(*((_D,_U),(_D,_V),(_D,_W)))
if mibBuilder.loadTexts:fusionPortAlert.setStatus(_A)
fusionConfigUpdateAlert=NotificationType((1,3,6,1,4,1,43296,3,6,8))
if mibBuilder.loadTexts:fusionConfigUpdateAlert.setStatus(_A)
fusionTimeAlert=NotificationType((1,3,6,1,4,1,43296,3,6,9))
fusionTimeAlert.setObjects((_D,_X))
if mibBuilder.loadTexts:fusionTimeAlert.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'exaFusion':exaFusion,'fusionInfo':fusionInfo,'fusionInfoSerial':fusionInfoSerial,'fusionInfoVersion':fusionInfoVersion,'fusionInfoBoard':fusionInfoBoard,'fusionInfoSoftware':fusionInfoSoftware,'fusionLineCardTable':fusionLineCardTable,'fusionLineCard':fusionLineCard,_F:fusionLineCardIndex,'fusionLineCardName':fusionLineCardName,'fusionLineCardBoard':fusionLineCardBoard,'fusionModuleTable':fusionModuleTable,'fusionModule':fusionModule,_G:fusionModuleIndex,'fusionModuleName':fusionModuleName,'fusionModuleBoard':fusionModuleBoard,'fusionModuleFunction':fusionModuleFunction,'fusionSysInfo':fusionSysInfo,'fusionSysInfoLoadAverage':fusionSysInfoLoadAverage,'fusionSysInfoAvailMem':fusionSysInfoAvailMem,'fusionSysInfoNumProcesses':fusionSysInfoNumProcesses,'fusionSensor':fusionSensor,'fusionTempSensorTable':fusionTempSensorTable,'fusionTempSensor':fusionTempSensor,_H:fusionTempSensorIndex,_Q:fusionTempSensorName,'fusionTempSensorValue':fusionTempSensorValue,'fusionFanSensorTable':fusionFanSensorTable,'fusionFanSensor':fusionFanSensor,_J:fusionFanSensorIndex,'fusionFanSensorName':fusionFanSensorName,'fusionFanSensorValue':fusionFanSensorValue,'fusionPsuTable':fusionPsuTable,'fusionPsu':fusionPsu,_K:fusionPsuIndex,'fusionPsuType':fusionPsuType,'fusionPsuPresent':fusionPsuPresent,'fusionPsuTemperature':fusionPsuTemperature,'fusionPsuPowerIn':fusionPsuPowerIn,'fusionPsuPowerOut':fusionPsuPowerOut,'fusionPortTable':fusionPortTable,'fusionPort':fusionPort,_L:fusionPortLineCard,_M:fusionPortIndex,_U:fusionPortName,'fusionPortPresent':fusionPortPresent,'fusionPortHasSignal':fusionPortHasSignal,'fusionPortEnabled':fusionPortEnabled,'fusionPortAlias':fusionPortAlias,'fusionPortSpeed':fusionPortSpeed,'fusionPortRXPackets':fusionPortRXPackets,'fusionPortRXBytes':fusionPortRXBytes,'fusionPortRXErrors':fusionPortRXErrors,'fusionPortTXPackets':fusionPortTXPackets,'fusionPortTXBytes':fusionPortTXBytes,'fusionPortRXLink':fusionPortRXLink,'fusionPortRXLinkChanges':fusionPortRXLinkChanges,'fusionPortRXDropped':fusionPortRXDropped,'fusionPortRXUnicast':fusionPortRXUnicast,'fusionPortRXMulticast':fusionPortRXMulticast,'fusionPortRXBroadcast':fusionPortRXBroadcast,'fusionPortRXRunt':fusionPortRXRunt,'fusionPortRXPause':fusionPortRXPause,'fusionPortRX64b':fusionPortRX64b,'fusionPortRX65to127b':fusionPortRX65to127b,'fusionPortRX128to255b':fusionPortRX128to255b,'fusionPortRX256to511b':fusionPortRX256to511b,'fusionPortRX512to1023b':fusionPortRX512to1023b,'fusionPortRX1024to1518b':fusionPortRX1024to1518b,'fusionPortRX1519to1522b':fusionPortRX1519to1522b,'fusionPortTXUnicast':fusionPortTXUnicast,'fusionPortTXMulticast':fusionPortTXMulticast,'fusionPortTXBroadcast':fusionPortTXBroadcast,'fusionPortTX64b':fusionPortTX64b,'fusionPortTX65to127b':fusionPortTX65to127b,'fusionPortTX128to255b':fusionPortTX128to255b,'fusionPortTX256to511b':fusionPortTX256to511b,'fusionPortTX512to1023b':fusionPortTX512to1023b,'fusionPortTX1024to1518b':fusionPortTX1024to1518b,'fusionPortTX1519to1522b':fusionPortTX1519to1522b,'fusionPortL1Source':fusionPortL1Source,'fusionTrapValues':fusionTrapValues,_P:fusionLidOpenStatus,_T:fusionFanFaultStatus,_R:fusionHighTempStatus,_W:fusionPortUsageStatus,_V:fusionPortLinkStatus,_S:fusionPsuFaultStatus,_X:fusionTimeSourceStatus,'fusionTraps':fusionTraps,'fusionPowerFail':fusionPowerFail,'fusionTamperAlert':fusionTamperAlert,'fusionTempAlert':fusionTempAlert,'fusionPsuAlert':fusionPsuAlert,'fusionSystemAlert':fusionSystemAlert,'fusionFanAlert':fusionFanAlert,'fusionPortAlert':fusionPortAlert,'fusionConfigUpdateAlert':fusionConfigUpdateAlert,'fusionTimeAlert':fusionTimeAlert})