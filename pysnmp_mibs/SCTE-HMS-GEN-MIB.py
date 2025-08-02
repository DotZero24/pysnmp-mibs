_K='genDeviceAddress'
_J='SCTE-HMS-GEN-MIB'
_I='OctetString'
_H='optional'
_G='alarm'
_F='noAlarm'
_E='installed'
_D='notInstalled'
_C='mandatory'
_B='Integer32'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
genIdent,=mibBuilder.importSymbols('SCTE-HMS-ROOTS','genIdent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class _GenNumberOfGenerators_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_GenNumberOfGenerators_Type.__name__=_B
_GenNumberOfGenerators_Object=MibScalar
genNumberOfGenerators=_GenNumberOfGenerators_Object((1,3,6,1,4,1,5591,1,6,1),_GenNumberOfGenerators_Type())
genNumberOfGenerators.setMaxAccess(_A)
if mibBuilder.loadTexts:genNumberOfGenerators.setStatus(_C)
_GenDeviceTable_Object=MibTable
genDeviceTable=_GenDeviceTable_Object((1,3,6,1,4,1,5591,1,6,2))
if mibBuilder.loadTexts:genDeviceTable.setStatus(_C)
_GenDeviceEntry_Object=MibTableRow
genDeviceEntry=_GenDeviceEntry_Object((1,3,6,1,4,1,5591,1,6,2,1))
genDeviceEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:genDeviceEntry.setStatus(_C)
class _GenDeviceAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_GenDeviceAddress_Type.__name__=_B
_GenDeviceAddress_Object=MibTableColumn
genDeviceAddress=_GenDeviceAddress_Object((1,3,6,1,4,1,5591,1,6,2,1,1),_GenDeviceAddress_Type())
genDeviceAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:genDeviceAddress.setStatus(_C)
class _GenProtocolVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_GenProtocolVersion_Type.__name__=_B
_GenProtocolVersion_Object=MibTableColumn
genProtocolVersion=_GenProtocolVersion_Object((1,3,6,1,4,1,5591,1,6,2,1,2),_GenProtocolVersion_Type())
genProtocolVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:genProtocolVersion.setStatus(_C)
class _GenSoftwareVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_GenSoftwareVersion_Type.__name__=_I
_GenSoftwareVersion_Object=MibTableColumn
genSoftwareVersion=_GenSoftwareVersion_Object((1,3,6,1,4,1,5591,1,6,2,1,3),_GenSoftwareVersion_Type())
genSoftwareVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:genSoftwareVersion.setStatus(_C)
class _GenDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_GenDeviceId_Type.__name__=_I
_GenDeviceId_Object=MibTableColumn
genDeviceId=_GenDeviceId_Object((1,3,6,1,4,1,5591,1,6,2,1,4),_GenDeviceId_Type())
genDeviceId.setMaxAccess(_A)
if mibBuilder.loadTexts:genDeviceId.setStatus(_C)
class _GenGasHazardOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_GenGasHazardOption_Type.__name__=_B
_GenGasHazardOption_Object=MibTableColumn
genGasHazardOption=_GenGasHazardOption_Object((1,3,6,1,4,1,5591,1,6,2,1,5),_GenGasHazardOption_Type())
genGasHazardOption.setMaxAccess(_A)
if mibBuilder.loadTexts:genGasHazardOption.setStatus(_C)
class _GenWaterIntrusionOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_GenWaterIntrusionOption_Type.__name__=_B
_GenWaterIntrusionOption_Object=MibTableColumn
genWaterIntrusionOption=_GenWaterIntrusionOption_Object((1,3,6,1,4,1,5591,1,6,2,1,6),_GenWaterIntrusionOption_Type())
genWaterIntrusionOption.setMaxAccess(_A)
if mibBuilder.loadTexts:genWaterIntrusionOption.setStatus(_C)
class _GenPadShearOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_GenPadShearOption_Type.__name__=_B
_GenPadShearOption_Object=MibTableColumn
genPadShearOption=_GenPadShearOption_Object((1,3,6,1,4,1,5591,1,6,2,1,7),_GenPadShearOption_Type())
genPadShearOption.setMaxAccess(_A)
if mibBuilder.loadTexts:genPadShearOption.setStatus(_C)
class _GenDoorOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_GenDoorOption_Type.__name__=_B
_GenDoorOption_Object=MibTableColumn
genDoorOption=_GenDoorOption_Object((1,3,6,1,4,1,5591,1,6,2,1,8),_GenDoorOption_Type())
genDoorOption.setMaxAccess(_A)
if mibBuilder.loadTexts:genDoorOption.setStatus(_C)
class _GenChargerOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_GenChargerOption_Type.__name__=_B
_GenChargerOption_Object=MibTableColumn
genChargerOption=_GenChargerOption_Object((1,3,6,1,4,1,5591,1,6,2,1,9),_GenChargerOption_Type())
genChargerOption.setMaxAccess(_A)
if mibBuilder.loadTexts:genChargerOption.setStatus(_C)
class _GenFuelOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_GenFuelOption_Type.__name__=_B
_GenFuelOption_Object=MibTableColumn
genFuelOption=_GenFuelOption_Object((1,3,6,1,4,1,5591,1,6,2,1,10),_GenFuelOption_Type())
genFuelOption.setMaxAccess(_A)
if mibBuilder.loadTexts:genFuelOption.setStatus(_C)
class _GenVBatIgnitionOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_GenVBatIgnitionOption_Type.__name__=_B
_GenVBatIgnitionOption_Object=MibTableColumn
genVBatIgnitionOption=_GenVBatIgnitionOption_Object((1,3,6,1,4,1,5591,1,6,2,1,11),_GenVBatIgnitionOption_Type())
genVBatIgnitionOption.setMaxAccess(_A)
if mibBuilder.loadTexts:genVBatIgnitionOption.setStatus(_C)
class _GenTempOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_GenTempOption_Type.__name__=_B
_GenTempOption_Object=MibTableColumn
genTempOption=_GenTempOption_Object((1,3,6,1,4,1,5591,1,6,2,1,12),_GenTempOption_Type())
genTempOption.setMaxAccess(_A)
if mibBuilder.loadTexts:genTempOption.setStatus(_C)
class _GenGeneratorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('runningTest',2),('running',3),('fail',4)))
_GenGeneratorStatus_Type.__name__=_B
_GenGeneratorStatus_Object=MibTableColumn
genGeneratorStatus=_GenGeneratorStatus_Object((1,3,6,1,4,1,5591,1,6,2,1,13),_GenGeneratorStatus_Type())
genGeneratorStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:genGeneratorStatus.setStatus(_C)
class _GenGasHazard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_GenGasHazard_Type.__name__=_B
_GenGasHazard_Object=MibTableColumn
genGasHazard=_GenGasHazard_Object((1,3,6,1,4,1,5591,1,6,2,1,14),_GenGasHazard_Type())
genGasHazard.setMaxAccess(_A)
if mibBuilder.loadTexts:genGasHazard.setStatus(_C)
class _GenWaterIntrusion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_GenWaterIntrusion_Type.__name__=_B
_GenWaterIntrusion_Object=MibTableColumn
genWaterIntrusion=_GenWaterIntrusion_Object((1,3,6,1,4,1,5591,1,6,2,1,15),_GenWaterIntrusion_Type())
genWaterIntrusion.setMaxAccess(_A)
if mibBuilder.loadTexts:genWaterIntrusion.setStatus(_C)
class _GenPadShear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_GenPadShear_Type.__name__=_B
_GenPadShear_Object=MibTableColumn
genPadShear=_GenPadShear_Object((1,3,6,1,4,1,5591,1,6,2,1,16),_GenPadShear_Type())
genPadShear.setMaxAccess(_A)
if mibBuilder.loadTexts:genPadShear.setStatus(_C)
class _GenEnclosureDoor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_GenEnclosureDoor_Type.__name__=_B
_GenEnclosureDoor_Object=MibTableColumn
genEnclosureDoor=_GenEnclosureDoor_Object((1,3,6,1,4,1,5591,1,6,2,1,17),_GenEnclosureDoor_Type())
genEnclosureDoor.setMaxAccess(_A)
if mibBuilder.loadTexts:genEnclosureDoor.setStatus(_C)
class _GenCharger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_GenCharger_Type.__name__=_B
_GenCharger_Object=MibTableColumn
genCharger=_GenCharger_Object((1,3,6,1,4,1,5591,1,6,2,1,18),_GenCharger_Type())
genCharger.setMaxAccess(_A)
if mibBuilder.loadTexts:genCharger.setStatus(_C)
class _GenFuel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_GenFuel_Type.__name__=_B
_GenFuel_Object=MibTableColumn
genFuel=_GenFuel_Object((1,3,6,1,4,1,5591,1,6,2,1,19),_GenFuel_Type())
genFuel.setMaxAccess(_A)
if mibBuilder.loadTexts:genFuel.setStatus(_C)
class _GenVBatIgnition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_GenVBatIgnition_Type.__name__=_B
_GenVBatIgnition_Object=MibTableColumn
genVBatIgnition=_GenVBatIgnition_Object((1,3,6,1,4,1,5591,1,6,2,1,20),_GenVBatIgnition_Type())
genVBatIgnition.setMaxAccess(_A)
if mibBuilder.loadTexts:genVBatIgnition.setStatus(_C)
class _GenEnclosureTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,80))
_GenEnclosureTemperature_Type.__name__=_B
_GenEnclosureTemperature_Object=MibTableColumn
genEnclosureTemperature=_GenEnclosureTemperature_Object((1,3,6,1,4,1,5591,1,6,2,1,21),_GenEnclosureTemperature_Type())
genEnclosureTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:genEnclosureTemperature.setStatus(_C)
class _GenEquipmentControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stopGenerator',1),('startGenerator',2),('resetLatchedAlarms',3)))
_GenEquipmentControl_Type.__name__=_B
_GenEquipmentControl_Object=MibTableColumn
genEquipmentControl=_GenEquipmentControl_Object((1,3,6,1,4,1,5591,1,6,2,1,22),_GenEquipmentControl_Type())
genEquipmentControl.setMaxAccess('read-write')
if mibBuilder.loadTexts:genEquipmentControl.setStatus(_H)
class _GenOilOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_GenOilOption_Type.__name__=_B
_GenOilOption_Object=MibTableColumn
genOilOption=_GenOilOption_Object((1,3,6,1,4,1,5591,1,6,2,1,23),_GenOilOption_Type())
genOilOption.setMaxAccess(_A)
if mibBuilder.loadTexts:genOilOption.setStatus(_C)
class _GenMinorAlarmSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_GenMinorAlarmSupport_Type.__name__=_B
_GenMinorAlarmSupport_Object=MibTableColumn
genMinorAlarmSupport=_GenMinorAlarmSupport_Object((1,3,6,1,4,1,5591,1,6,2,1,24),_GenMinorAlarmSupport_Type())
genMinorAlarmSupport.setMaxAccess(_A)
if mibBuilder.loadTexts:genMinorAlarmSupport.setStatus(_C)
class _GenMajorAlarmSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_GenMajorAlarmSupport_Type.__name__=_B
_GenMajorAlarmSupport_Object=MibTableColumn
genMajorAlarmSupport=_GenMajorAlarmSupport_Object((1,3,6,1,4,1,5591,1,6,2,1,25),_GenMajorAlarmSupport_Type())
genMajorAlarmSupport.setMaxAccess(_A)
if mibBuilder.loadTexts:genMajorAlarmSupport.setStatus(_C)
class _GenOil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_GenOil_Type.__name__=_B
_GenOil_Object=MibTableColumn
genOil=_GenOil_Object((1,3,6,1,4,1,5591,1,6,2,1,26),_GenOil_Type())
genOil.setMaxAccess(_A)
if mibBuilder.loadTexts:genOil.setStatus(_H)
class _GenMinorAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_GenMinorAlarm_Type.__name__=_B
_GenMinorAlarm_Object=MibTableColumn
genMinorAlarm=_GenMinorAlarm_Object((1,3,6,1,4,1,5591,1,6,2,1,27),_GenMinorAlarm_Type())
genMinorAlarm.setMaxAccess(_A)
if mibBuilder.loadTexts:genMinorAlarm.setStatus(_H)
class _GenMajorAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_GenMajorAlarm_Type.__name__=_B
_GenMajorAlarm_Object=MibTableColumn
genMajorAlarm=_GenMajorAlarm_Object((1,3,6,1,4,1,5591,1,6,2,1,28),_GenMajorAlarm_Type())
genMajorAlarm.setMaxAccess(_A)
if mibBuilder.loadTexts:genMajorAlarm.setStatus(_H)
_GenVendorOID_Type=ObjectIdentifier
_GenVendorOID_Object=MibTableColumn
genVendorOID=_GenVendorOID_Object((1,3,6,1,4,1,5591,1,6,2,1,29),_GenVendorOID_Type())
genVendorOID.setMaxAccess(_A)
if mibBuilder.loadTexts:genVendorOID.setStatus(_H)
mibBuilder.exportSymbols(_J,**{'genNumberOfGenerators':genNumberOfGenerators,'genDeviceTable':genDeviceTable,'genDeviceEntry':genDeviceEntry,_K:genDeviceAddress,'genProtocolVersion':genProtocolVersion,'genSoftwareVersion':genSoftwareVersion,'genDeviceId':genDeviceId,'genGasHazardOption':genGasHazardOption,'genWaterIntrusionOption':genWaterIntrusionOption,'genPadShearOption':genPadShearOption,'genDoorOption':genDoorOption,'genChargerOption':genChargerOption,'genFuelOption':genFuelOption,'genVBatIgnitionOption':genVBatIgnitionOption,'genTempOption':genTempOption,'genGeneratorStatus':genGeneratorStatus,'genGasHazard':genGasHazard,'genWaterIntrusion':genWaterIntrusion,'genPadShear':genPadShear,'genEnclosureDoor':genEnclosureDoor,'genCharger':genCharger,'genFuel':genFuel,'genVBatIgnition':genVBatIgnition,'genEnclosureTemperature':genEnclosureTemperature,'genEquipmentControl':genEquipmentControl,'genOilOption':genOilOption,'genMinorAlarmSupport':genMinorAlarmSupport,'genMajorAlarmSupport':genMajorAlarmSupport,'genOil':genOil,'genMinorAlarm':genMinorAlarm,'genMajorAlarm':genMajorAlarm,'genVendorOID':genVendorOID})