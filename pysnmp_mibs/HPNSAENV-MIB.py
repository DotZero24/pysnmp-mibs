_Z='hpnsaEnvFanSensorIndex'
_Y='hpnsaEnvTemperatureSensorIndex'
_X='hpnsaEnvVoltageSensorIndex'
_W='non-recoverable'
_V='critical'
_U='non-critical'
_T='add-in-card'
_S='power-unit'
_R='processor-module'
_Q='memory-module'
_P='motherboard'
_O='system-management-module'
_N='peripheral-bay'
_M='disk'
_L='processor'
_K='four-state-discrete'
_J='three-state-discrete'
_I='digital'
_H='analog'
_G='HPNSAENV-MIB'
_F='unknown'
_E='other'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
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
_HpnsaEnvironment_ObjectIdentity=ObjectIdentity
hpnsaEnvironment=_HpnsaEnvironment_ObjectIdentity((1,3,6,1,4,1,11,2,23,26))
_HpnsaEnvMibRev_ObjectIdentity=ObjectIdentity
hpnsaEnvMibRev=_HpnsaEnvMibRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,26,1))
class _HpnsaEnvMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvMibRevMajor_Type.__name__=_C
_HpnsaEnvMibRevMajor_Object=MibScalar
hpnsaEnvMibRevMajor=_HpnsaEnvMibRevMajor_Object((1,3,6,1,4,1,11,2,23,26,1,1),_HpnsaEnvMibRevMajor_Type())
hpnsaEnvMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvMibRevMajor.setStatus(_A)
class _HpnsaEnvMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvMibRevMinor_Type.__name__=_C
_HpnsaEnvMibRevMinor_Object=MibScalar
hpnsaEnvMibRevMinor=_HpnsaEnvMibRevMinor_Object((1,3,6,1,4,1,11,2,23,26,1,2),_HpnsaEnvMibRevMinor_Type())
hpnsaEnvMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvMibRevMinor.setStatus(_A)
_HpnsaEnvVoltageData_ObjectIdentity=ObjectIdentity
hpnsaEnvVoltageData=_HpnsaEnvVoltageData_ObjectIdentity((1,3,6,1,4,1,11,2,23,26,2))
_HpnsaEnvVoltageSensorTable_Object=MibTable
hpnsaEnvVoltageSensorTable=_HpnsaEnvVoltageSensorTable_Object((1,3,6,1,4,1,11,2,23,26,2,1))
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorTable.setStatus(_A)
_HpnsaEnvVoltageSensorEntry_Object=MibTableRow
hpnsaEnvVoltageSensorEntry=_HpnsaEnvVoltageSensorEntry_Object((1,3,6,1,4,1,11,2,23,26,2,1,1))
hpnsaEnvVoltageSensorEntry.setIndexNames((0,_G,_X))
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorEntry.setStatus(_A)
class _HpnsaEnvVoltageSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEnvVoltageSensorIndex_Type.__name__=_C
_HpnsaEnvVoltageSensorIndex_Object=MibTableColumn
hpnsaEnvVoltageSensorIndex=_HpnsaEnvVoltageSensorIndex_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,1),_HpnsaEnvVoltageSensorIndex_Type())
hpnsaEnvVoltageSensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorIndex.setStatus(_A)
class _HpnsaEnvVoltageSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3),(_I,4),(_J,5),(_K,6)))
_HpnsaEnvVoltageSensorType_Type.__name__=_C
_HpnsaEnvVoltageSensorType_Object=MibTableColumn
hpnsaEnvVoltageSensorType=_HpnsaEnvVoltageSensorType_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,2),_HpnsaEnvVoltageSensorType_Type())
hpnsaEnvVoltageSensorType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorType.setStatus(_A)
class _HpnsaEnvVoltageSensorLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_E,1),(_F,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8),(_R,9),(_S,10),(_T,11)))
_HpnsaEnvVoltageSensorLocation_Type.__name__=_C
_HpnsaEnvVoltageSensorLocation_Object=MibTableColumn
hpnsaEnvVoltageSensorLocation=_HpnsaEnvVoltageSensorLocation_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,3),_HpnsaEnvVoltageSensorLocation_Type())
hpnsaEnvVoltageSensorLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorLocation.setStatus(_A)
class _HpnsaEnvVoltageSensorDescription_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('voltsensor-other',1),('voltsensor-unknown',2),('voltsensor-plus-5-volt',3),('voltsensor-minus-5-volt',4),('voltsensor-plus-12-volt',5),('voltsensor-minus-12-volt',6),('voltsensor-plus-3-3-volt',7),('voltsensor-plus-2-5-volt',8),('voltsensor-scsi-terminator',9),('voltsensor-processor-1',10),('voltsensor-processor-2',11),('voltsensor-processor-3',12),('voltsensor-processor-4',13)))
_HpnsaEnvVoltageSensorDescription_Type.__name__=_C
_HpnsaEnvVoltageSensorDescription_Object=MibTableColumn
hpnsaEnvVoltageSensorDescription=_HpnsaEnvVoltageSensorDescription_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,4),_HpnsaEnvVoltageSensorDescription_Type())
hpnsaEnvVoltageSensorDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorDescription.setStatus(_A)
class _HpnsaEnvVoltageSensorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),('ok',3),(_U,4),(_V,5),(_W,6)))
_HpnsaEnvVoltageSensorStatus_Type.__name__=_C
_HpnsaEnvVoltageSensorStatus_Object=MibTableColumn
hpnsaEnvVoltageSensorStatus=_HpnsaEnvVoltageSensorStatus_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,5),_HpnsaEnvVoltageSensorStatus_Type())
hpnsaEnvVoltageSensorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorStatus.setStatus(_A)
_HpnsaEnvVoltageSensorLevel_Type=Integer32
_HpnsaEnvVoltageSensorLevel_Object=MibTableColumn
hpnsaEnvVoltageSensorLevel=_HpnsaEnvVoltageSensorLevel_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,6),_HpnsaEnvVoltageSensorLevel_Type())
hpnsaEnvVoltageSensorLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorLevel.setStatus(_A)
_HpnsaEnvVoltageSensorNominalLevel_Type=Integer32
_HpnsaEnvVoltageSensorNominalLevel_Object=MibTableColumn
hpnsaEnvVoltageSensorNominalLevel=_HpnsaEnvVoltageSensorNominalLevel_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,7),_HpnsaEnvVoltageSensorNominalLevel_Type())
hpnsaEnvVoltageSensorNominalLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorNominalLevel.setStatus(_A)
_HpnsaEnvVoltageSensorNormalMaximum_Type=Integer32
_HpnsaEnvVoltageSensorNormalMaximum_Object=MibTableColumn
hpnsaEnvVoltageSensorNormalMaximum=_HpnsaEnvVoltageSensorNormalMaximum_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,8),_HpnsaEnvVoltageSensorNormalMaximum_Type())
hpnsaEnvVoltageSensorNormalMaximum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorNormalMaximum.setStatus(_A)
_HpnsaEnvVoltageSensorNormalMinimum_Type=Integer32
_HpnsaEnvVoltageSensorNormalMinimum_Object=MibTableColumn
hpnsaEnvVoltageSensorNormalMinimum=_HpnsaEnvVoltageSensorNormalMinimum_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,9),_HpnsaEnvVoltageSensorNormalMinimum_Type())
hpnsaEnvVoltageSensorNormalMinimum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorNormalMinimum.setStatus(_A)
_HpnsaEnvVoltageSensorMaximum_Type=Integer32
_HpnsaEnvVoltageSensorMaximum_Object=MibTableColumn
hpnsaEnvVoltageSensorMaximum=_HpnsaEnvVoltageSensorMaximum_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,10),_HpnsaEnvVoltageSensorMaximum_Type())
hpnsaEnvVoltageSensorMaximum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorMaximum.setStatus(_A)
_HpnsaEnvVoltageSensorMinimum_Type=Integer32
_HpnsaEnvVoltageSensorMinimum_Object=MibTableColumn
hpnsaEnvVoltageSensorMinimum=_HpnsaEnvVoltageSensorMinimum_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,11),_HpnsaEnvVoltageSensorMinimum_Type())
hpnsaEnvVoltageSensorMinimum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorMinimum.setStatus(_A)
_HpnsaEnvVoltageSensorLowerNonCriticalThreshold_Type=Integer32
_HpnsaEnvVoltageSensorLowerNonCriticalThreshold_Object=MibTableColumn
hpnsaEnvVoltageSensorLowerNonCriticalThreshold=_HpnsaEnvVoltageSensorLowerNonCriticalThreshold_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,12),_HpnsaEnvVoltageSensorLowerNonCriticalThreshold_Type())
hpnsaEnvVoltageSensorLowerNonCriticalThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorLowerNonCriticalThreshold.setStatus(_A)
_HpnsaEnvVoltageSensorUpperNonCriticalThreshold_Type=Integer32
_HpnsaEnvVoltageSensorUpperNonCriticalThreshold_Object=MibTableColumn
hpnsaEnvVoltageSensorUpperNonCriticalThreshold=_HpnsaEnvVoltageSensorUpperNonCriticalThreshold_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,13),_HpnsaEnvVoltageSensorUpperNonCriticalThreshold_Type())
hpnsaEnvVoltageSensorUpperNonCriticalThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorUpperNonCriticalThreshold.setStatus(_A)
_HpnsaEnvVoltageSensorLowerCriticalThreshold_Type=Integer32
_HpnsaEnvVoltageSensorLowerCriticalThreshold_Object=MibTableColumn
hpnsaEnvVoltageSensorLowerCriticalThreshold=_HpnsaEnvVoltageSensorLowerCriticalThreshold_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,14),_HpnsaEnvVoltageSensorLowerCriticalThreshold_Type())
hpnsaEnvVoltageSensorLowerCriticalThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorLowerCriticalThreshold.setStatus(_A)
_HpnsaEnvVoltageSensorUpperCriticalThreshold_Type=Integer32
_HpnsaEnvVoltageSensorUpperCriticalThreshold_Object=MibTableColumn
hpnsaEnvVoltageSensorUpperCriticalThreshold=_HpnsaEnvVoltageSensorUpperCriticalThreshold_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,15),_HpnsaEnvVoltageSensorUpperCriticalThreshold_Type())
hpnsaEnvVoltageSensorUpperCriticalThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorUpperCriticalThreshold.setStatus(_A)
_HpnsaEnvVoltageSensorLowerNonRecoverableThreshold_Type=Integer32
_HpnsaEnvVoltageSensorLowerNonRecoverableThreshold_Object=MibTableColumn
hpnsaEnvVoltageSensorLowerNonRecoverableThreshold=_HpnsaEnvVoltageSensorLowerNonRecoverableThreshold_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,16),_HpnsaEnvVoltageSensorLowerNonRecoverableThreshold_Type())
hpnsaEnvVoltageSensorLowerNonRecoverableThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorLowerNonRecoverableThreshold.setStatus(_A)
_HpnsaEnvVoltageSensorUpperNonRecoverableThreshold_Type=Integer32
_HpnsaEnvVoltageSensorUpperNonRecoverableThreshold_Object=MibTableColumn
hpnsaEnvVoltageSensorUpperNonRecoverableThreshold=_HpnsaEnvVoltageSensorUpperNonRecoverableThreshold_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,17),_HpnsaEnvVoltageSensorUpperNonRecoverableThreshold_Type())
hpnsaEnvVoltageSensorUpperNonRecoverableThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorUpperNonRecoverableThreshold.setStatus(_A)
_HpnsaEnvVoltageSensorResolution_Type=Integer32
_HpnsaEnvVoltageSensorResolution_Object=MibTableColumn
hpnsaEnvVoltageSensorResolution=_HpnsaEnvVoltageSensorResolution_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,18),_HpnsaEnvVoltageSensorResolution_Type())
hpnsaEnvVoltageSensorResolution.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorResolution.setStatus(_A)
_HpnsaEnvVoltageSensorTolerance_Type=Integer32
_HpnsaEnvVoltageSensorTolerance_Object=MibTableColumn
hpnsaEnvVoltageSensorTolerance=_HpnsaEnvVoltageSensorTolerance_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,19),_HpnsaEnvVoltageSensorTolerance_Type())
hpnsaEnvVoltageSensorTolerance.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorTolerance.setStatus(_A)
_HpnsaEnvVoltageSensorAccuracy_Type=Integer32
_HpnsaEnvVoltageSensorAccuracy_Object=MibTableColumn
hpnsaEnvVoltageSensorAccuracy=_HpnsaEnvVoltageSensorAccuracy_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,20),_HpnsaEnvVoltageSensorAccuracy_Type())
hpnsaEnvVoltageSensorAccuracy.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorAccuracy.setStatus(_A)
_HpnsaEnvVoltageSensorPositiveHysterisis_Type=Integer32
_HpnsaEnvVoltageSensorPositiveHysterisis_Object=MibTableColumn
hpnsaEnvVoltageSensorPositiveHysterisis=_HpnsaEnvVoltageSensorPositiveHysterisis_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,21),_HpnsaEnvVoltageSensorPositiveHysterisis_Type())
hpnsaEnvVoltageSensorPositiveHysterisis.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorPositiveHysterisis.setStatus(_A)
_HpnsaEnvVoltageSensorNegativeHysterisis_Type=Integer32
_HpnsaEnvVoltageSensorNegativeHysterisis_Object=MibTableColumn
hpnsaEnvVoltageSensorNegativeHysterisis=_HpnsaEnvVoltageSensorNegativeHysterisis_Object((1,3,6,1,4,1,11,2,23,26,2,1,1,22),_HpnsaEnvVoltageSensorNegativeHysterisis_Type())
hpnsaEnvVoltageSensorNegativeHysterisis.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvVoltageSensorNegativeHysterisis.setStatus(_A)
_HpnsaEnvTemperatureData_ObjectIdentity=ObjectIdentity
hpnsaEnvTemperatureData=_HpnsaEnvTemperatureData_ObjectIdentity((1,3,6,1,4,1,11,2,23,26,3))
_HpnsaEnvTemperatureSensorTable_Object=MibTable
hpnsaEnvTemperatureSensorTable=_HpnsaEnvTemperatureSensorTable_Object((1,3,6,1,4,1,11,2,23,26,3,1))
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorTable.setStatus(_A)
_HpnsaEnvTemperatureSensorEntry_Object=MibTableRow
hpnsaEnvTemperatureSensorEntry=_HpnsaEnvTemperatureSensorEntry_Object((1,3,6,1,4,1,11,2,23,26,3,1,1))
hpnsaEnvTemperatureSensorEntry.setIndexNames((0,_G,_Y))
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorEntry.setStatus(_A)
class _HpnsaEnvTemperatureSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEnvTemperatureSensorIndex_Type.__name__=_C
_HpnsaEnvTemperatureSensorIndex_Object=MibTableColumn
hpnsaEnvTemperatureSensorIndex=_HpnsaEnvTemperatureSensorIndex_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,1),_HpnsaEnvTemperatureSensorIndex_Type())
hpnsaEnvTemperatureSensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorIndex.setStatus(_A)
class _HpnsaEnvTemperatureSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3),(_I,4),(_J,5),(_K,6)))
_HpnsaEnvTemperatureSensorType_Type.__name__=_C
_HpnsaEnvTemperatureSensorType_Object=MibTableColumn
hpnsaEnvTemperatureSensorType=_HpnsaEnvTemperatureSensorType_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,2),_HpnsaEnvTemperatureSensorType_Type())
hpnsaEnvTemperatureSensorType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorType.setStatus(_A)
class _HpnsaEnvTemperatureSensorLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_E,1),(_F,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8),(_R,9),(_S,10),(_T,11)))
_HpnsaEnvTemperatureSensorLocation_Type.__name__=_C
_HpnsaEnvTemperatureSensorLocation_Object=MibTableColumn
hpnsaEnvTemperatureSensorLocation=_HpnsaEnvTemperatureSensorLocation_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,3),_HpnsaEnvTemperatureSensorLocation_Type())
hpnsaEnvTemperatureSensorLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorLocation.setStatus(_A)
class _HpnsaEnvTemperatureSensorDescription_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('temperature-sensor-other',1),('temperature-sensor-unknown',2),('temperature-sensor-processor-1',3),('temperature-sensor-processor-2',4),('temperature-sensor-processor-3',5),('temperature-sensor-processor-4',6),('temperature-sensor-processor-5',7),('temperature-sensor-processor-6',8),('temperature-sensor-processor-7',9),('temperature-sensor-processor-8',10),('temperature-sensor-system-board',11),('temperature-sensor-disk-backplane',12)))
_HpnsaEnvTemperatureSensorDescription_Type.__name__=_C
_HpnsaEnvTemperatureSensorDescription_Object=MibTableColumn
hpnsaEnvTemperatureSensorDescription=_HpnsaEnvTemperatureSensorDescription_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,4),_HpnsaEnvTemperatureSensorDescription_Type())
hpnsaEnvTemperatureSensorDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorDescription.setStatus(_A)
class _HpnsaEnvTemperatureSensorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),('ok',3),(_U,4),(_V,5),(_W,6)))
_HpnsaEnvTemperatureSensorStatus_Type.__name__=_C
_HpnsaEnvTemperatureSensorStatus_Object=MibTableColumn
hpnsaEnvTemperatureSensorStatus=_HpnsaEnvTemperatureSensorStatus_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,5),_HpnsaEnvTemperatureSensorStatus_Type())
hpnsaEnvTemperatureSensorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorStatus.setStatus(_A)
_HpnsaEnvTemperatureSensorReading_Type=Integer32
_HpnsaEnvTemperatureSensorReading_Object=MibTableColumn
hpnsaEnvTemperatureSensorReading=_HpnsaEnvTemperatureSensorReading_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,6),_HpnsaEnvTemperatureSensorReading_Type())
hpnsaEnvTemperatureSensorReading.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorReading.setStatus(_A)
_HpnsaEnvTemperatureSensorNominalReading_Type=Integer32
_HpnsaEnvTemperatureSensorNominalReading_Object=MibTableColumn
hpnsaEnvTemperatureSensorNominalReading=_HpnsaEnvTemperatureSensorNominalReading_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,7),_HpnsaEnvTemperatureSensorNominalReading_Type())
hpnsaEnvTemperatureSensorNominalReading.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorNominalReading.setStatus(_A)
_HpnsaEnvTemperatureSensorNormalMaximum_Type=Integer32
_HpnsaEnvTemperatureSensorNormalMaximum_Object=MibTableColumn
hpnsaEnvTemperatureSensorNormalMaximum=_HpnsaEnvTemperatureSensorNormalMaximum_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,8),_HpnsaEnvTemperatureSensorNormalMaximum_Type())
hpnsaEnvTemperatureSensorNormalMaximum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorNormalMaximum.setStatus(_A)
_HpnsaEnvTemperatureSensorNormalMinimum_Type=Integer32
_HpnsaEnvTemperatureSensorNormalMinimum_Object=MibTableColumn
hpnsaEnvTemperatureSensorNormalMinimum=_HpnsaEnvTemperatureSensorNormalMinimum_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,9),_HpnsaEnvTemperatureSensorNormalMinimum_Type())
hpnsaEnvTemperatureSensorNormalMinimum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorNormalMinimum.setStatus(_A)
_HpnsaEnvTemperatureSensorMaximum_Type=Integer32
_HpnsaEnvTemperatureSensorMaximum_Object=MibTableColumn
hpnsaEnvTemperatureSensorMaximum=_HpnsaEnvTemperatureSensorMaximum_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,10),_HpnsaEnvTemperatureSensorMaximum_Type())
hpnsaEnvTemperatureSensorMaximum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorMaximum.setStatus(_A)
_HpnsaEnvTemperatureSensorMinimum_Type=Integer32
_HpnsaEnvTemperatureSensorMinimum_Object=MibTableColumn
hpnsaEnvTemperatureSensorMinimum=_HpnsaEnvTemperatureSensorMinimum_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,11),_HpnsaEnvTemperatureSensorMinimum_Type())
hpnsaEnvTemperatureSensorMinimum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorMinimum.setStatus(_A)
_HpnsaEnvTemperatureSensorLowerNonCriticalThreshold_Type=Integer32
_HpnsaEnvTemperatureSensorLowerNonCriticalThreshold_Object=MibTableColumn
hpnsaEnvTemperatureSensorLowerNonCriticalThreshold=_HpnsaEnvTemperatureSensorLowerNonCriticalThreshold_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,12),_HpnsaEnvTemperatureSensorLowerNonCriticalThreshold_Type())
hpnsaEnvTemperatureSensorLowerNonCriticalThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorLowerNonCriticalThreshold.setStatus(_A)
_HpnsaEnvTemperatureSensorUpperNonCriticalThreshold_Type=Integer32
_HpnsaEnvTemperatureSensorUpperNonCriticalThreshold_Object=MibTableColumn
hpnsaEnvTemperatureSensorUpperNonCriticalThreshold=_HpnsaEnvTemperatureSensorUpperNonCriticalThreshold_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,13),_HpnsaEnvTemperatureSensorUpperNonCriticalThreshold_Type())
hpnsaEnvTemperatureSensorUpperNonCriticalThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorUpperNonCriticalThreshold.setStatus(_A)
_HpnsaEnvTemperatureSensorLowerCriticalThreshold_Type=Integer32
_HpnsaEnvTemperatureSensorLowerCriticalThreshold_Object=MibTableColumn
hpnsaEnvTemperatureSensorLowerCriticalThreshold=_HpnsaEnvTemperatureSensorLowerCriticalThreshold_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,14),_HpnsaEnvTemperatureSensorLowerCriticalThreshold_Type())
hpnsaEnvTemperatureSensorLowerCriticalThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorLowerCriticalThreshold.setStatus(_A)
_HpnsaEnvTemperatureSensorUpperCriticalThreshold_Type=Integer32
_HpnsaEnvTemperatureSensorUpperCriticalThreshold_Object=MibTableColumn
hpnsaEnvTemperatureSensorUpperCriticalThreshold=_HpnsaEnvTemperatureSensorUpperCriticalThreshold_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,15),_HpnsaEnvTemperatureSensorUpperCriticalThreshold_Type())
hpnsaEnvTemperatureSensorUpperCriticalThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorUpperCriticalThreshold.setStatus(_A)
_HpnsaEnvTemperatureSensorLowerNonRecoverableThreshold_Type=Integer32
_HpnsaEnvTemperatureSensorLowerNonRecoverableThreshold_Object=MibTableColumn
hpnsaEnvTemperatureSensorLowerNonRecoverableThreshold=_HpnsaEnvTemperatureSensorLowerNonRecoverableThreshold_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,16),_HpnsaEnvTemperatureSensorLowerNonRecoverableThreshold_Type())
hpnsaEnvTemperatureSensorLowerNonRecoverableThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorLowerNonRecoverableThreshold.setStatus(_A)
_HpnsaEnvTemperatureSensorUpperNonRecoverableThreshold_Type=Integer32
_HpnsaEnvTemperatureSensorUpperNonRecoverableThreshold_Object=MibTableColumn
hpnsaEnvTemperatureSensorUpperNonRecoverableThreshold=_HpnsaEnvTemperatureSensorUpperNonRecoverableThreshold_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,17),_HpnsaEnvTemperatureSensorUpperNonRecoverableThreshold_Type())
hpnsaEnvTemperatureSensorUpperNonRecoverableThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorUpperNonRecoverableThreshold.setStatus(_A)
_HpnsaEnvTemperatureSensorResolution_Type=Integer32
_HpnsaEnvTemperatureSensorResolution_Object=MibTableColumn
hpnsaEnvTemperatureSensorResolution=_HpnsaEnvTemperatureSensorResolution_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,18),_HpnsaEnvTemperatureSensorResolution_Type())
hpnsaEnvTemperatureSensorResolution.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorResolution.setStatus(_A)
_HpnsaEnvTemperatureSensorTolerance_Type=Integer32
_HpnsaEnvTemperatureSensorTolerance_Object=MibTableColumn
hpnsaEnvTemperatureSensorTolerance=_HpnsaEnvTemperatureSensorTolerance_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,19),_HpnsaEnvTemperatureSensorTolerance_Type())
hpnsaEnvTemperatureSensorTolerance.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorTolerance.setStatus(_A)
_HpnsaEnvTemperatureSensorAccuracy_Type=Integer32
_HpnsaEnvTemperatureSensorAccuracy_Object=MibTableColumn
hpnsaEnvTemperatureSensorAccuracy=_HpnsaEnvTemperatureSensorAccuracy_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,20),_HpnsaEnvTemperatureSensorAccuracy_Type())
hpnsaEnvTemperatureSensorAccuracy.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorAccuracy.setStatus(_A)
_HpnsaEnvTemperatureSensorPositiveHysterisis_Type=Integer32
_HpnsaEnvTemperatureSensorPositiveHysterisis_Object=MibTableColumn
hpnsaEnvTemperatureSensorPositiveHysterisis=_HpnsaEnvTemperatureSensorPositiveHysterisis_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,21),_HpnsaEnvTemperatureSensorPositiveHysterisis_Type())
hpnsaEnvTemperatureSensorPositiveHysterisis.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorPositiveHysterisis.setStatus(_A)
_HpnsaEnvTemperatureSensorNegativeHysterisis_Type=Integer32
_HpnsaEnvTemperatureSensorNegativeHysterisis_Object=MibTableColumn
hpnsaEnvTemperatureSensorNegativeHysterisis=_HpnsaEnvTemperatureSensorNegativeHysterisis_Object((1,3,6,1,4,1,11,2,23,26,3,1,1,22),_HpnsaEnvTemperatureSensorNegativeHysterisis_Type())
hpnsaEnvTemperatureSensorNegativeHysterisis.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvTemperatureSensorNegativeHysterisis.setStatus(_A)
_HpnsaEnvFanSensorData_ObjectIdentity=ObjectIdentity
hpnsaEnvFanSensorData=_HpnsaEnvFanSensorData_ObjectIdentity((1,3,6,1,4,1,11,2,23,26,4))
_HpnsaEnvFanSensorTable_Object=MibTable
hpnsaEnvFanSensorTable=_HpnsaEnvFanSensorTable_Object((1,3,6,1,4,1,11,2,23,26,4,1))
if mibBuilder.loadTexts:hpnsaEnvFanSensorTable.setStatus(_A)
_HpnsaEnvFanSensorEntry_Object=MibTableRow
hpnsaEnvFanSensorEntry=_HpnsaEnvFanSensorEntry_Object((1,3,6,1,4,1,11,2,23,26,4,1,1))
hpnsaEnvFanSensorEntry.setIndexNames((0,_G,_Z))
if mibBuilder.loadTexts:hpnsaEnvFanSensorEntry.setStatus(_A)
class _HpnsaEnvFanSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEnvFanSensorIndex_Type.__name__=_C
_HpnsaEnvFanSensorIndex_Object=MibTableColumn
hpnsaEnvFanSensorIndex=_HpnsaEnvFanSensorIndex_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,1),_HpnsaEnvFanSensorIndex_Type())
hpnsaEnvFanSensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvFanSensorIndex.setStatus(_A)
class _HpnsaEnvFanSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3),(_I,4),(_J,5),(_K,6)))
_HpnsaEnvFanSensorType_Type.__name__=_C
_HpnsaEnvFanSensorType_Object=MibTableColumn
hpnsaEnvFanSensorType=_HpnsaEnvFanSensorType_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,2),_HpnsaEnvFanSensorType_Type())
hpnsaEnvFanSensorType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvFanSensorType.setStatus(_A)
class _HpnsaEnvFanSensorLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_E,1),(_F,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8),(_R,9),(_S,10),(_T,11)))
_HpnsaEnvFanSensorLocation_Type.__name__=_C
_HpnsaEnvFanSensorLocation_Object=MibTableColumn
hpnsaEnvFanSensorLocation=_HpnsaEnvFanSensorLocation_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,3),_HpnsaEnvFanSensorLocation_Type())
hpnsaEnvFanSensorLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvFanSensorLocation.setStatus(_A)
class _HpnsaEnvFanSensorDescription_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fan-sensor-other',1),('fan-sensor-unknown',2),('fan-sensor-cpu-board',3),('fan-sensor-chassis',4)))
_HpnsaEnvFanSensorDescription_Type.__name__=_C
_HpnsaEnvFanSensorDescription_Object=MibTableColumn
hpnsaEnvFanSensorDescription=_HpnsaEnvFanSensorDescription_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,4),_HpnsaEnvFanSensorDescription_Type())
hpnsaEnvFanSensorDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvFanSensorDescription.setStatus(_A)
class _HpnsaEnvFanSensorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),('ok',3),(_U,4),(_V,5),(_W,6)))
_HpnsaEnvFanSensorStatus_Type.__name__=_C
_HpnsaEnvFanSensorStatus_Object=MibTableColumn
hpnsaEnvFanSensorStatus=_HpnsaEnvFanSensorStatus_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,5),_HpnsaEnvFanSensorStatus_Type())
hpnsaEnvFanSensorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvFanSensorStatus.setStatus(_A)
class _HpnsaEnvFanSensorReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorReading_Type.__name__=_C
_HpnsaEnvFanSensorReading_Object=MibTableColumn
hpnsaEnvFanSensorReading=_HpnsaEnvFanSensorReading_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,6),_HpnsaEnvFanSensorReading_Type())
hpnsaEnvFanSensorReading.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvFanSensorReading.setStatus(_A)
class _HpnsaEnvFanSensorNominalReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorNominalReading_Type.__name__=_C
_HpnsaEnvFanSensorNominalReading_Object=MibTableColumn
hpnsaEnvFanSensorNominalReading=_HpnsaEnvFanSensorNominalReading_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,7),_HpnsaEnvFanSensorNominalReading_Type())
hpnsaEnvFanSensorNominalReading.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvFanSensorNominalReading.setStatus(_A)
class _HpnsaEnvFanSensorNormalMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorNormalMaximum_Type.__name__=_C
_HpnsaEnvFanSensorNormalMaximum_Object=MibTableColumn
hpnsaEnvFanSensorNormalMaximum=_HpnsaEnvFanSensorNormalMaximum_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,8),_HpnsaEnvFanSensorNormalMaximum_Type())
hpnsaEnvFanSensorNormalMaximum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvFanSensorNormalMaximum.setStatus(_A)
class _HpnsaEnvFanSensorNormalMinimum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorNormalMinimum_Type.__name__=_C
_HpnsaEnvFanSensorNormalMinimum_Object=MibTableColumn
hpnsaEnvFanSensorNormalMinimum=_HpnsaEnvFanSensorNormalMinimum_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,9),_HpnsaEnvFanSensorNormalMinimum_Type())
hpnsaEnvFanSensorNormalMinimum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvFanSensorNormalMinimum.setStatus(_A)
class _HpnsaEnvFanSensorMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorMaximum_Type.__name__=_C
_HpnsaEnvFanSensorMaximum_Object=MibTableColumn
hpnsaEnvFanSensorMaximum=_HpnsaEnvFanSensorMaximum_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,10),_HpnsaEnvFanSensorMaximum_Type())
hpnsaEnvFanSensorMaximum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvFanSensorMaximum.setStatus(_A)
class _HpnsaEnvFanSensorMinimum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorMinimum_Type.__name__=_C
_HpnsaEnvFanSensorMinimum_Object=MibTableColumn
hpnsaEnvFanSensorMinimum=_HpnsaEnvFanSensorMinimum_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,11),_HpnsaEnvFanSensorMinimum_Type())
hpnsaEnvFanSensorMinimum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvFanSensorMinimum.setStatus(_A)
class _HpnsaEnvFanSensorLowerNonCriticalThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorLowerNonCriticalThreshold_Type.__name__=_C
_HpnsaEnvFanSensorLowerNonCriticalThreshold_Object=MibTableColumn
hpnsaEnvFanSensorLowerNonCriticalThreshold=_HpnsaEnvFanSensorLowerNonCriticalThreshold_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,12),_HpnsaEnvFanSensorLowerNonCriticalThreshold_Type())
hpnsaEnvFanSensorLowerNonCriticalThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvFanSensorLowerNonCriticalThreshold.setStatus(_A)
class _HpnsaEnvFanSensorUpperNonCriticalThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorUpperNonCriticalThreshold_Type.__name__=_C
_HpnsaEnvFanSensorUpperNonCriticalThreshold_Object=MibTableColumn
hpnsaEnvFanSensorUpperNonCriticalThreshold=_HpnsaEnvFanSensorUpperNonCriticalThreshold_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,13),_HpnsaEnvFanSensorUpperNonCriticalThreshold_Type())
hpnsaEnvFanSensorUpperNonCriticalThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvFanSensorUpperNonCriticalThreshold.setStatus(_A)
class _HpnsaEnvFanSensorLowerCriticalThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorLowerCriticalThreshold_Type.__name__=_C
_HpnsaEnvFanSensorLowerCriticalThreshold_Object=MibTableColumn
hpnsaEnvFanSensorLowerCriticalThreshold=_HpnsaEnvFanSensorLowerCriticalThreshold_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,14),_HpnsaEnvFanSensorLowerCriticalThreshold_Type())
hpnsaEnvFanSensorLowerCriticalThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvFanSensorLowerCriticalThreshold.setStatus(_A)
class _HpnsaEnvFanSensorUpperCriticalThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorUpperCriticalThreshold_Type.__name__=_C
_HpnsaEnvFanSensorUpperCriticalThreshold_Object=MibTableColumn
hpnsaEnvFanSensorUpperCriticalThreshold=_HpnsaEnvFanSensorUpperCriticalThreshold_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,15),_HpnsaEnvFanSensorUpperCriticalThreshold_Type())
hpnsaEnvFanSensorUpperCriticalThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvFanSensorUpperCriticalThreshold.setStatus(_A)
class _HpnsaEnvFanSensorLowerNonRecoverableThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorLowerNonRecoverableThreshold_Type.__name__=_C
_HpnsaEnvFanSensorLowerNonRecoverableThreshold_Object=MibTableColumn
hpnsaEnvFanSensorLowerNonRecoverableThreshold=_HpnsaEnvFanSensorLowerNonRecoverableThreshold_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,16),_HpnsaEnvFanSensorLowerNonRecoverableThreshold_Type())
hpnsaEnvFanSensorLowerNonRecoverableThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvFanSensorLowerNonRecoverableThreshold.setStatus(_A)
class _HpnsaEnvFanSensorUpperNonRecoverableThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorUpperNonRecoverableThreshold_Type.__name__=_C
_HpnsaEnvFanSensorUpperNonRecoverableThreshold_Object=MibTableColumn
hpnsaEnvFanSensorUpperNonRecoverableThreshold=_HpnsaEnvFanSensorUpperNonRecoverableThreshold_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,17),_HpnsaEnvFanSensorUpperNonRecoverableThreshold_Type())
hpnsaEnvFanSensorUpperNonRecoverableThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvFanSensorUpperNonRecoverableThreshold.setStatus(_A)
class _HpnsaEnvFanSensorResolution_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorResolution_Type.__name__=_C
_HpnsaEnvFanSensorResolution_Object=MibTableColumn
hpnsaEnvFanSensorResolution=_HpnsaEnvFanSensorResolution_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,18),_HpnsaEnvFanSensorResolution_Type())
hpnsaEnvFanSensorResolution.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvFanSensorResolution.setStatus(_A)
class _HpnsaEnvFanSensorTolerance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorTolerance_Type.__name__=_C
_HpnsaEnvFanSensorTolerance_Object=MibTableColumn
hpnsaEnvFanSensorTolerance=_HpnsaEnvFanSensorTolerance_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,19),_HpnsaEnvFanSensorTolerance_Type())
hpnsaEnvFanSensorTolerance.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvFanSensorTolerance.setStatus(_A)
class _HpnsaEnvFanSensorAccuracy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorAccuracy_Type.__name__=_C
_HpnsaEnvFanSensorAccuracy_Object=MibTableColumn
hpnsaEnvFanSensorAccuracy=_HpnsaEnvFanSensorAccuracy_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,20),_HpnsaEnvFanSensorAccuracy_Type())
hpnsaEnvFanSensorAccuracy.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvFanSensorAccuracy.setStatus(_A)
class _HpnsaEnvFanSensorPositiveHysterisis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorPositiveHysterisis_Type.__name__=_C
_HpnsaEnvFanSensorPositiveHysterisis_Object=MibTableColumn
hpnsaEnvFanSensorPositiveHysterisis=_HpnsaEnvFanSensorPositiveHysterisis_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,21),_HpnsaEnvFanSensorPositiveHysterisis_Type())
hpnsaEnvFanSensorPositiveHysterisis.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvFanSensorPositiveHysterisis.setStatus(_A)
class _HpnsaEnvFanSensorNegativeHysterisis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEnvFanSensorNegativeHysterisis_Type.__name__=_C
_HpnsaEnvFanSensorNegativeHysterisis_Object=MibTableColumn
hpnsaEnvFanSensorNegativeHysterisis=_HpnsaEnvFanSensorNegativeHysterisis_Object((1,3,6,1,4,1,11,2,23,26,4,1,1,22),_HpnsaEnvFanSensorNegativeHysterisis_Type())
hpnsaEnvFanSensorNegativeHysterisis.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEnvFanSensorNegativeHysterisis.setStatus(_A)
_HpnsaEnvChassisData_ObjectIdentity=ObjectIdentity
hpnsaEnvChassisData=_HpnsaEnvChassisData_ObjectIdentity((1,3,6,1,4,1,11,2,23,26,5))
class _HpnsaEnvChassisStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chassis-open',1),('chassis-closed',2)))
_HpnsaEnvChassisStatus_Type.__name__=_C
_HpnsaEnvChassisStatus_Object=MibScalar
hpnsaEnvChassisStatus=_HpnsaEnvChassisStatus_Object((1,3,6,1,4,1,11,2,23,26,5,1),_HpnsaEnvChassisStatus_Type())
hpnsaEnvChassisStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEnvChassisStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaEnvironment':hpnsaEnvironment,'hpnsaEnvMibRev':hpnsaEnvMibRev,'hpnsaEnvMibRevMajor':hpnsaEnvMibRevMajor,'hpnsaEnvMibRevMinor':hpnsaEnvMibRevMinor,'hpnsaEnvVoltageData':hpnsaEnvVoltageData,'hpnsaEnvVoltageSensorTable':hpnsaEnvVoltageSensorTable,'hpnsaEnvVoltageSensorEntry':hpnsaEnvVoltageSensorEntry,_X:hpnsaEnvVoltageSensorIndex,'hpnsaEnvVoltageSensorType':hpnsaEnvVoltageSensorType,'hpnsaEnvVoltageSensorLocation':hpnsaEnvVoltageSensorLocation,'hpnsaEnvVoltageSensorDescription':hpnsaEnvVoltageSensorDescription,'hpnsaEnvVoltageSensorStatus':hpnsaEnvVoltageSensorStatus,'hpnsaEnvVoltageSensorLevel':hpnsaEnvVoltageSensorLevel,'hpnsaEnvVoltageSensorNominalLevel':hpnsaEnvVoltageSensorNominalLevel,'hpnsaEnvVoltageSensorNormalMaximum':hpnsaEnvVoltageSensorNormalMaximum,'hpnsaEnvVoltageSensorNormalMinimum':hpnsaEnvVoltageSensorNormalMinimum,'hpnsaEnvVoltageSensorMaximum':hpnsaEnvVoltageSensorMaximum,'hpnsaEnvVoltageSensorMinimum':hpnsaEnvVoltageSensorMinimum,'hpnsaEnvVoltageSensorLowerNonCriticalThreshold':hpnsaEnvVoltageSensorLowerNonCriticalThreshold,'hpnsaEnvVoltageSensorUpperNonCriticalThreshold':hpnsaEnvVoltageSensorUpperNonCriticalThreshold,'hpnsaEnvVoltageSensorLowerCriticalThreshold':hpnsaEnvVoltageSensorLowerCriticalThreshold,'hpnsaEnvVoltageSensorUpperCriticalThreshold':hpnsaEnvVoltageSensorUpperCriticalThreshold,'hpnsaEnvVoltageSensorLowerNonRecoverableThreshold':hpnsaEnvVoltageSensorLowerNonRecoverableThreshold,'hpnsaEnvVoltageSensorUpperNonRecoverableThreshold':hpnsaEnvVoltageSensorUpperNonRecoverableThreshold,'hpnsaEnvVoltageSensorResolution':hpnsaEnvVoltageSensorResolution,'hpnsaEnvVoltageSensorTolerance':hpnsaEnvVoltageSensorTolerance,'hpnsaEnvVoltageSensorAccuracy':hpnsaEnvVoltageSensorAccuracy,'hpnsaEnvVoltageSensorPositiveHysterisis':hpnsaEnvVoltageSensorPositiveHysterisis,'hpnsaEnvVoltageSensorNegativeHysterisis':hpnsaEnvVoltageSensorNegativeHysterisis,'hpnsaEnvTemperatureData':hpnsaEnvTemperatureData,'hpnsaEnvTemperatureSensorTable':hpnsaEnvTemperatureSensorTable,'hpnsaEnvTemperatureSensorEntry':hpnsaEnvTemperatureSensorEntry,_Y:hpnsaEnvTemperatureSensorIndex,'hpnsaEnvTemperatureSensorType':hpnsaEnvTemperatureSensorType,'hpnsaEnvTemperatureSensorLocation':hpnsaEnvTemperatureSensorLocation,'hpnsaEnvTemperatureSensorDescription':hpnsaEnvTemperatureSensorDescription,'hpnsaEnvTemperatureSensorStatus':hpnsaEnvTemperatureSensorStatus,'hpnsaEnvTemperatureSensorReading':hpnsaEnvTemperatureSensorReading,'hpnsaEnvTemperatureSensorNominalReading':hpnsaEnvTemperatureSensorNominalReading,'hpnsaEnvTemperatureSensorNormalMaximum':hpnsaEnvTemperatureSensorNormalMaximum,'hpnsaEnvTemperatureSensorNormalMinimum':hpnsaEnvTemperatureSensorNormalMinimum,'hpnsaEnvTemperatureSensorMaximum':hpnsaEnvTemperatureSensorMaximum,'hpnsaEnvTemperatureSensorMinimum':hpnsaEnvTemperatureSensorMinimum,'hpnsaEnvTemperatureSensorLowerNonCriticalThreshold':hpnsaEnvTemperatureSensorLowerNonCriticalThreshold,'hpnsaEnvTemperatureSensorUpperNonCriticalThreshold':hpnsaEnvTemperatureSensorUpperNonCriticalThreshold,'hpnsaEnvTemperatureSensorLowerCriticalThreshold':hpnsaEnvTemperatureSensorLowerCriticalThreshold,'hpnsaEnvTemperatureSensorUpperCriticalThreshold':hpnsaEnvTemperatureSensorUpperCriticalThreshold,'hpnsaEnvTemperatureSensorLowerNonRecoverableThreshold':hpnsaEnvTemperatureSensorLowerNonRecoverableThreshold,'hpnsaEnvTemperatureSensorUpperNonRecoverableThreshold':hpnsaEnvTemperatureSensorUpperNonRecoverableThreshold,'hpnsaEnvTemperatureSensorResolution':hpnsaEnvTemperatureSensorResolution,'hpnsaEnvTemperatureSensorTolerance':hpnsaEnvTemperatureSensorTolerance,'hpnsaEnvTemperatureSensorAccuracy':hpnsaEnvTemperatureSensorAccuracy,'hpnsaEnvTemperatureSensorPositiveHysterisis':hpnsaEnvTemperatureSensorPositiveHysterisis,'hpnsaEnvTemperatureSensorNegativeHysterisis':hpnsaEnvTemperatureSensorNegativeHysterisis,'hpnsaEnvFanSensorData':hpnsaEnvFanSensorData,'hpnsaEnvFanSensorTable':hpnsaEnvFanSensorTable,'hpnsaEnvFanSensorEntry':hpnsaEnvFanSensorEntry,_Z:hpnsaEnvFanSensorIndex,'hpnsaEnvFanSensorType':hpnsaEnvFanSensorType,'hpnsaEnvFanSensorLocation':hpnsaEnvFanSensorLocation,'hpnsaEnvFanSensorDescription':hpnsaEnvFanSensorDescription,'hpnsaEnvFanSensorStatus':hpnsaEnvFanSensorStatus,'hpnsaEnvFanSensorReading':hpnsaEnvFanSensorReading,'hpnsaEnvFanSensorNominalReading':hpnsaEnvFanSensorNominalReading,'hpnsaEnvFanSensorNormalMaximum':hpnsaEnvFanSensorNormalMaximum,'hpnsaEnvFanSensorNormalMinimum':hpnsaEnvFanSensorNormalMinimum,'hpnsaEnvFanSensorMaximum':hpnsaEnvFanSensorMaximum,'hpnsaEnvFanSensorMinimum':hpnsaEnvFanSensorMinimum,'hpnsaEnvFanSensorLowerNonCriticalThreshold':hpnsaEnvFanSensorLowerNonCriticalThreshold,'hpnsaEnvFanSensorUpperNonCriticalThreshold':hpnsaEnvFanSensorUpperNonCriticalThreshold,'hpnsaEnvFanSensorLowerCriticalThreshold':hpnsaEnvFanSensorLowerCriticalThreshold,'hpnsaEnvFanSensorUpperCriticalThreshold':hpnsaEnvFanSensorUpperCriticalThreshold,'hpnsaEnvFanSensorLowerNonRecoverableThreshold':hpnsaEnvFanSensorLowerNonRecoverableThreshold,'hpnsaEnvFanSensorUpperNonRecoverableThreshold':hpnsaEnvFanSensorUpperNonRecoverableThreshold,'hpnsaEnvFanSensorResolution':hpnsaEnvFanSensorResolution,'hpnsaEnvFanSensorTolerance':hpnsaEnvFanSensorTolerance,'hpnsaEnvFanSensorAccuracy':hpnsaEnvFanSensorAccuracy,'hpnsaEnvFanSensorPositiveHysterisis':hpnsaEnvFanSensorPositiveHysterisis,'hpnsaEnvFanSensorNegativeHysterisis':hpnsaEnvFanSensorNegativeHysterisis,'hpnsaEnvChassisData':hpnsaEnvChassisData,'hpnsaEnvChassisStatus':hpnsaEnvChassisStatus})