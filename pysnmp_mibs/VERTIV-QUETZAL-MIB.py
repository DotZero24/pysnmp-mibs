_V='current'
_U='pduGroupID'
_T='pduGroupIndex'
_S='pduChannelWyeID'
_R='pduChannelDeltaID'
_Q='thdIndex'
_P='normal'
_O='unplugged'
_N='t3hdIndex'
_M='rtIndex'
_L='rtafhd3Index'
_K='pduBaseWyeIndex'
_J='pduBaseDeltaIndex'
_I='pduOutletMainID'
_H='pduOutletMainIndex'
_G='Integer32'
_F='not-accessible'
_E='Unsigned32'
_D='VERTIV-QUETZAL-MIB'
_C='read-write'
_B='read-only'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vertiv=ModuleIdentity((1,3,6,1,4,1,21239))
if mibBuilder.loadTexts:vertiv.setRevisions(('2019-08-30 00:00','2019-06-06 00:00','2018-01-19 00:00','2016-06-29 00:00','2012-09-21 00:00'))
class DeviceSerial(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
class DeviceStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ok',1),('notFound',2),('ioError',3),('unknown',4),('deleted',5)))
class DeviceLabel(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class TemperatureUnits(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fahrenheit',1),('celsius',2)))
class TemperatureValue(TextualConvention,Integer32):status=_A;displayHint='d-1'
class DeciAmps(TextualConvention,Gauge32):status=_A;displayHint='d-1'
_Quetzal_ObjectIdentity=ObjectIdentity
quetzal=_Quetzal_ObjectIdentity((1,3,6,1,4,1,21239,6))
_Devices_ObjectIdentity=ObjectIdentity
devices=_Devices_ObjectIdentity((1,3,6,1,4,1,21239,6,1))
_Rtafhd3_ObjectIdentity=ObjectIdentity
rtafhd3=_Rtafhd3_ObjectIdentity((1,3,6,1,4,1,21239,6,1,3))
_Rtafhd3Table_Object=MibTable
rtafhd3Table=_Rtafhd3Table_Object((1,3,6,1,4,1,21239,6,1,3,1))
if mibBuilder.loadTexts:rtafhd3Table.setStatus(_A)
_Rtafhd3Entry_Object=MibTableRow
rtafhd3Entry=_Rtafhd3Entry_Object((1,3,6,1,4,1,21239,6,1,3,1,1))
rtafhd3Entry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:rtafhd3Entry.setStatus(_A)
class _Rtafhd3Index_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Rtafhd3Index_Type.__name__=_E
_Rtafhd3Index_Object=MibTableColumn
rtafhd3Index=_Rtafhd3Index_Object((1,3,6,1,4,1,21239,6,1,3,1,1,1),_Rtafhd3Index_Type())
rtafhd3Index.setMaxAccess(_F)
if mibBuilder.loadTexts:rtafhd3Index.setStatus(_A)
_Rtafhd3Serial_Type=DeviceSerial
_Rtafhd3Serial_Object=MibTableColumn
rtafhd3Serial=_Rtafhd3Serial_Object((1,3,6,1,4,1,21239,6,1,3,1,1,2),_Rtafhd3Serial_Type())
rtafhd3Serial.setMaxAccess(_B)
if mibBuilder.loadTexts:rtafhd3Serial.setStatus(_A)
_Rtafhd3Label_Type=DeviceLabel
_Rtafhd3Label_Object=MibTableColumn
rtafhd3Label=_Rtafhd3Label_Object((1,3,6,1,4,1,21239,6,1,3,1,1,3),_Rtafhd3Label_Type())
rtafhd3Label.setMaxAccess(_C)
if mibBuilder.loadTexts:rtafhd3Label.setStatus(_A)
_Rtafhd3Status_Type=DeviceStatus
_Rtafhd3Status_Object=MibTableColumn
rtafhd3Status=_Rtafhd3Status_Object((1,3,6,1,4,1,21239,6,1,3,1,1,4),_Rtafhd3Status_Type())
rtafhd3Status.setMaxAccess(_B)
if mibBuilder.loadTexts:rtafhd3Status.setStatus(_A)
_Rtafhd3Airflow_Type=Gauge32
_Rtafhd3Airflow_Object=MibTableColumn
rtafhd3Airflow=_Rtafhd3Airflow_Object((1,3,6,1,4,1,21239,6,1,3,1,1,5),_Rtafhd3Airflow_Type())
rtafhd3Airflow.setMaxAccess(_B)
if mibBuilder.loadTexts:rtafhd3Airflow.setStatus(_A)
_Rtafhd3Humidity_Type=Gauge32
_Rtafhd3Humidity_Object=MibTableColumn
rtafhd3Humidity=_Rtafhd3Humidity_Object((1,3,6,1,4,1,21239,6,1,3,1,1,6),_Rtafhd3Humidity_Type())
rtafhd3Humidity.setMaxAccess(_B)
if mibBuilder.loadTexts:rtafhd3Humidity.setStatus(_A)
_Rtafhd3Temp_Type=TemperatureValue
_Rtafhd3Temp_Object=MibTableColumn
rtafhd3Temp=_Rtafhd3Temp_Object((1,3,6,1,4,1,21239,6,1,3,1,1,7),_Rtafhd3Temp_Type())
rtafhd3Temp.setMaxAccess(_B)
if mibBuilder.loadTexts:rtafhd3Temp.setStatus(_A)
_Rtafhd3DewPoint_Type=TemperatureValue
_Rtafhd3DewPoint_Object=MibTableColumn
rtafhd3DewPoint=_Rtafhd3DewPoint_Object((1,3,6,1,4,1,21239,6,1,3,1,1,8),_Rtafhd3DewPoint_Type())
rtafhd3DewPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:rtafhd3DewPoint.setStatus(_A)
_Rtafhd3TDUnits_Type=TemperatureUnits
_Rtafhd3TDUnits_Object=MibTableColumn
rtafhd3TDUnits=_Rtafhd3TDUnits_Object((1,3,6,1,4,1,21239,6,1,3,1,1,9),_Rtafhd3TDUnits_Type())
rtafhd3TDUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:rtafhd3TDUnits.setStatus(_A)
_Rt_ObjectIdentity=ObjectIdentity
rt=_Rt_ObjectIdentity((1,3,6,1,4,1,21239,6,1,8))
_RtTable_Object=MibTable
rtTable=_RtTable_Object((1,3,6,1,4,1,21239,6,1,8,1))
if mibBuilder.loadTexts:rtTable.setStatus(_A)
_RtEntry_Object=MibTableRow
rtEntry=_RtEntry_Object((1,3,6,1,4,1,21239,6,1,8,1,1))
rtEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:rtEntry.setStatus(_A)
class _RtIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_RtIndex_Type.__name__=_E
_RtIndex_Object=MibTableColumn
rtIndex=_RtIndex_Object((1,3,6,1,4,1,21239,6,1,8,1,1,1),_RtIndex_Type())
rtIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rtIndex.setStatus(_A)
_RtSerial_Type=DeviceSerial
_RtSerial_Object=MibTableColumn
rtSerial=_RtSerial_Object((1,3,6,1,4,1,21239,6,1,8,1,1,2),_RtSerial_Type())
rtSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:rtSerial.setStatus(_A)
_RtLabel_Type=DeviceLabel
_RtLabel_Object=MibTableColumn
rtLabel=_RtLabel_Object((1,3,6,1,4,1,21239,6,1,8,1,1,3),_RtLabel_Type())
rtLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:rtLabel.setStatus(_A)
_RtStatus_Type=DeviceStatus
_RtStatus_Object=MibTableColumn
rtStatus=_RtStatus_Object((1,3,6,1,4,1,21239,6,1,8,1,1,4),_RtStatus_Type())
rtStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rtStatus.setStatus(_A)
_RtTemp_Type=TemperatureValue
_RtTemp_Object=MibTableColumn
rtTemp=_RtTemp_Object((1,3,6,1,4,1,21239,6,1,8,1,1,5),_RtTemp_Type())
rtTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:rtTemp.setStatus(_A)
_RtUnits_Type=TemperatureUnits
_RtUnits_Object=MibTableColumn
rtUnits=_RtUnits_Object((1,3,6,1,4,1,21239,6,1,8,1,1,6),_RtUnits_Type())
rtUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:rtUnits.setStatus(_A)
_T3hd_ObjectIdentity=ObjectIdentity
t3hd=_T3hd_ObjectIdentity((1,3,6,1,4,1,21239,6,1,9))
_T3hdTable_Object=MibTable
t3hdTable=_T3hdTable_Object((1,3,6,1,4,1,21239,6,1,9,1))
if mibBuilder.loadTexts:t3hdTable.setStatus(_A)
_T3hdEntry_Object=MibTableRow
t3hdEntry=_T3hdEntry_Object((1,3,6,1,4,1,21239,6,1,9,1,1))
t3hdEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:t3hdEntry.setStatus(_A)
class _T3hdIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_T3hdIndex_Type.__name__=_E
_T3hdIndex_Object=MibTableColumn
t3hdIndex=_T3hdIndex_Object((1,3,6,1,4,1,21239,6,1,9,1,1,1),_T3hdIndex_Type())
t3hdIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:t3hdIndex.setStatus(_A)
_T3hdSerial_Type=DeviceSerial
_T3hdSerial_Object=MibTableColumn
t3hdSerial=_T3hdSerial_Object((1,3,6,1,4,1,21239,6,1,9,1,1,2),_T3hdSerial_Type())
t3hdSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:t3hdSerial.setStatus(_A)
_T3hdLabel_Type=DeviceLabel
_T3hdLabel_Object=MibTableColumn
t3hdLabel=_T3hdLabel_Object((1,3,6,1,4,1,21239,6,1,9,1,1,3),_T3hdLabel_Type())
t3hdLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdLabel.setStatus(_A)
_T3hdStatus_Type=DeviceStatus
_T3hdStatus_Object=MibTableColumn
t3hdStatus=_T3hdStatus_Object((1,3,6,1,4,1,21239,6,1,9,1,1,4),_T3hdStatus_Type())
t3hdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:t3hdStatus.setStatus(_A)
_T3hdMainLabel_Type=DeviceLabel
_T3hdMainLabel_Object=MibTableColumn
t3hdMainLabel=_T3hdMainLabel_Object((1,3,6,1,4,1,21239,6,1,9,1,1,5),_T3hdMainLabel_Type())
t3hdMainLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdMainLabel.setStatus(_A)
_T3hdMainTemp_Type=TemperatureValue
_T3hdMainTemp_Object=MibTableColumn
t3hdMainTemp=_T3hdMainTemp_Object((1,3,6,1,4,1,21239,6,1,9,1,1,6),_T3hdMainTemp_Type())
t3hdMainTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:t3hdMainTemp.setStatus(_A)
_T3hdMainHumidity_Type=Gauge32
_T3hdMainHumidity_Object=MibTableColumn
t3hdMainHumidity=_T3hdMainHumidity_Object((1,3,6,1,4,1,21239,6,1,9,1,1,7),_T3hdMainHumidity_Type())
t3hdMainHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:t3hdMainHumidity.setStatus(_A)
_T3hdMainDewPoint_Type=TemperatureValue
_T3hdMainDewPoint_Object=MibTableColumn
t3hdMainDewPoint=_T3hdMainDewPoint_Object((1,3,6,1,4,1,21239,6,1,9,1,1,8),_T3hdMainDewPoint_Type())
t3hdMainDewPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:t3hdMainDewPoint.setStatus(_A)
class _T3hdExt1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),(_P,1),('error',2)))
_T3hdExt1Status_Type.__name__=_G
_T3hdExt1Status_Object=MibTableColumn
t3hdExt1Status=_T3hdExt1Status_Object((1,3,6,1,4,1,21239,6,1,9,1,1,9),_T3hdExt1Status_Type())
t3hdExt1Status.setMaxAccess(_B)
if mibBuilder.loadTexts:t3hdExt1Status.setStatus(_A)
_T3hdExt1Label_Type=DeviceLabel
_T3hdExt1Label_Object=MibTableColumn
t3hdExt1Label=_T3hdExt1Label_Object((1,3,6,1,4,1,21239,6,1,9,1,1,10),_T3hdExt1Label_Type())
t3hdExt1Label.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdExt1Label.setStatus(_A)
_T3hdExt1Temp_Type=TemperatureValue
_T3hdExt1Temp_Object=MibTableColumn
t3hdExt1Temp=_T3hdExt1Temp_Object((1,3,6,1,4,1,21239,6,1,9,1,1,11),_T3hdExt1Temp_Type())
t3hdExt1Temp.setMaxAccess(_B)
if mibBuilder.loadTexts:t3hdExt1Temp.setStatus(_A)
class _T3hdExt2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),(_P,1),('error',2)))
_T3hdExt2Status_Type.__name__=_G
_T3hdExt2Status_Object=MibTableColumn
t3hdExt2Status=_T3hdExt2Status_Object((1,3,6,1,4,1,21239,6,1,9,1,1,12),_T3hdExt2Status_Type())
t3hdExt2Status.setMaxAccess(_B)
if mibBuilder.loadTexts:t3hdExt2Status.setStatus(_A)
_T3hdExt2Label_Type=DeviceLabel
_T3hdExt2Label_Object=MibTableColumn
t3hdExt2Label=_T3hdExt2Label_Object((1,3,6,1,4,1,21239,6,1,9,1,1,13),_T3hdExt2Label_Type())
t3hdExt2Label.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdExt2Label.setStatus(_A)
_T3hdExt2Temp_Type=TemperatureValue
_T3hdExt2Temp_Object=MibTableColumn
t3hdExt2Temp=_T3hdExt2Temp_Object((1,3,6,1,4,1,21239,6,1,9,1,1,14),_T3hdExt2Temp_Type())
t3hdExt2Temp.setMaxAccess(_B)
if mibBuilder.loadTexts:t3hdExt2Temp.setStatus(_A)
_T3hdTDUnits_Type=TemperatureUnits
_T3hdTDUnits_Object=MibTableColumn
t3hdTDUnits=_T3hdTDUnits_Object((1,3,6,1,4,1,21239,6,1,9,1,1,15),_T3hdTDUnits_Type())
t3hdTDUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:t3hdTDUnits.setStatus(_A)
_Thd_ObjectIdentity=ObjectIdentity
thd=_Thd_ObjectIdentity((1,3,6,1,4,1,21239,6,1,10))
_ThdTable_Object=MibTable
thdTable=_ThdTable_Object((1,3,6,1,4,1,21239,6,1,10,1))
if mibBuilder.loadTexts:thdTable.setStatus(_A)
_ThdEntry_Object=MibTableRow
thdEntry=_ThdEntry_Object((1,3,6,1,4,1,21239,6,1,10,1,1))
thdEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:thdEntry.setStatus(_A)
class _ThdIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_ThdIndex_Type.__name__=_E
_ThdIndex_Object=MibTableColumn
thdIndex=_ThdIndex_Object((1,3,6,1,4,1,21239,6,1,10,1,1,1),_ThdIndex_Type())
thdIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:thdIndex.setStatus(_A)
_ThdSerial_Type=DeviceSerial
_ThdSerial_Object=MibTableColumn
thdSerial=_ThdSerial_Object((1,3,6,1,4,1,21239,6,1,10,1,1,2),_ThdSerial_Type())
thdSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:thdSerial.setStatus(_A)
_ThdLabel_Type=DeviceLabel
_ThdLabel_Object=MibTableColumn
thdLabel=_ThdLabel_Object((1,3,6,1,4,1,21239,6,1,10,1,1,3),_ThdLabel_Type())
thdLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:thdLabel.setStatus(_A)
_ThdStatus_Type=DeviceStatus
_ThdStatus_Object=MibTableColumn
thdStatus=_ThdStatus_Object((1,3,6,1,4,1,21239,6,1,10,1,1,4),_ThdStatus_Type())
thdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:thdStatus.setStatus(_A)
_ThdTemp_Type=TemperatureValue
_ThdTemp_Object=MibTableColumn
thdTemp=_ThdTemp_Object((1,3,6,1,4,1,21239,6,1,10,1,1,5),_ThdTemp_Type())
thdTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:thdTemp.setStatus(_A)
_ThdHumidity_Type=Gauge32
_ThdHumidity_Object=MibTableColumn
thdHumidity=_ThdHumidity_Object((1,3,6,1,4,1,21239,6,1,10,1,1,6),_ThdHumidity_Type())
thdHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:thdHumidity.setStatus(_A)
_ThdDewPoint_Type=TemperatureValue
_ThdDewPoint_Object=MibTableColumn
thdDewPoint=_ThdDewPoint_Object((1,3,6,1,4,1,21239,6,1,10,1,1,7),_ThdDewPoint_Type())
thdDewPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:thdDewPoint.setStatus(_A)
_ThdTDUnits_Type=TemperatureUnits
_ThdTDUnits_Object=MibTableColumn
thdTDUnits=_ThdTDUnits_Object((1,3,6,1,4,1,21239,6,1,10,1,1,8),_ThdTDUnits_Type())
thdTDUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:thdTDUnits.setStatus(_A)
_LegacyPDU_ObjectIdentity=ObjectIdentity
legacyPDU=_LegacyPDU_ObjectIdentity((1,3,6,1,4,1,21239,6,1,99))
_PduBaseDeltaTable_Object=MibTable
pduBaseDeltaTable=_PduBaseDeltaTable_Object((1,3,6,1,4,1,21239,6,1,99,1))
if mibBuilder.loadTexts:pduBaseDeltaTable.setStatus(_A)
_PduBaseDeltaEntry_Object=MibTableRow
pduBaseDeltaEntry=_PduBaseDeltaEntry_Object((1,3,6,1,4,1,21239,6,1,99,1,1))
pduBaseDeltaEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:pduBaseDeltaEntry.setStatus(_A)
class _PduBaseDeltaIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PduBaseDeltaIndex_Type.__name__=_E
_PduBaseDeltaIndex_Object=MibTableColumn
pduBaseDeltaIndex=_PduBaseDeltaIndex_Object((1,3,6,1,4,1,21239,6,1,99,1,1,1),_PduBaseDeltaIndex_Type())
pduBaseDeltaIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pduBaseDeltaIndex.setStatus(_A)
_PduBaseDeltaSerial_Type=DeviceSerial
_PduBaseDeltaSerial_Object=MibTableColumn
pduBaseDeltaSerial=_PduBaseDeltaSerial_Object((1,3,6,1,4,1,21239,6,1,99,1,1,2),_PduBaseDeltaSerial_Type())
pduBaseDeltaSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:pduBaseDeltaSerial.setStatus(_A)
_PduBaseDeltaLabel_Type=DeviceLabel
_PduBaseDeltaLabel_Object=MibTableColumn
pduBaseDeltaLabel=_PduBaseDeltaLabel_Object((1,3,6,1,4,1,21239,6,1,99,1,1,3),_PduBaseDeltaLabel_Type())
pduBaseDeltaLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:pduBaseDeltaLabel.setStatus(_A)
_PduBaseDeltaStatus_Type=DeviceStatus
_PduBaseDeltaStatus_Object=MibTableColumn
pduBaseDeltaStatus=_PduBaseDeltaStatus_Object((1,3,6,1,4,1,21239,6,1,99,1,1,4),_PduBaseDeltaStatus_Type())
pduBaseDeltaStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pduBaseDeltaStatus.setStatus(_A)
_PduBaseDeltaKWattHrsTotal_Type=Gauge32
_PduBaseDeltaKWattHrsTotal_Object=MibTableColumn
pduBaseDeltaKWattHrsTotal=_PduBaseDeltaKWattHrsTotal_Object((1,3,6,1,4,1,21239,6,1,99,1,1,5),_PduBaseDeltaKWattHrsTotal_Type())
pduBaseDeltaKWattHrsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:pduBaseDeltaKWattHrsTotal.setStatus(_A)
_PduBaseDeltaRealPowerTotal_Type=Gauge32
_PduBaseDeltaRealPowerTotal_Object=MibTableColumn
pduBaseDeltaRealPowerTotal=_PduBaseDeltaRealPowerTotal_Object((1,3,6,1,4,1,21239,6,1,99,1,1,6),_PduBaseDeltaRealPowerTotal_Type())
pduBaseDeltaRealPowerTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:pduBaseDeltaRealPowerTotal.setStatus(_A)
_PduBaseDeltaAmpsA_Type=DeciAmps
_PduBaseDeltaAmpsA_Object=MibTableColumn
pduBaseDeltaAmpsA=_PduBaseDeltaAmpsA_Object((1,3,6,1,4,1,21239,6,1,99,1,1,7),_PduBaseDeltaAmpsA_Type())
pduBaseDeltaAmpsA.setMaxAccess(_B)
if mibBuilder.loadTexts:pduBaseDeltaAmpsA.setStatus(_A)
_PduBaseDeltaAmpsB_Type=DeciAmps
_PduBaseDeltaAmpsB_Object=MibTableColumn
pduBaseDeltaAmpsB=_PduBaseDeltaAmpsB_Object((1,3,6,1,4,1,21239,6,1,99,1,1,8),_PduBaseDeltaAmpsB_Type())
pduBaseDeltaAmpsB.setMaxAccess(_B)
if mibBuilder.loadTexts:pduBaseDeltaAmpsB.setStatus(_A)
_PduBaseDeltaAmpsC_Type=DeciAmps
_PduBaseDeltaAmpsC_Object=MibTableColumn
pduBaseDeltaAmpsC=_PduBaseDeltaAmpsC_Object((1,3,6,1,4,1,21239,6,1,99,1,1,9),_PduBaseDeltaAmpsC_Type())
pduBaseDeltaAmpsC.setMaxAccess(_B)
if mibBuilder.loadTexts:pduBaseDeltaAmpsC.setStatus(_A)
_PduBaseWyeTable_Object=MibTable
pduBaseWyeTable=_PduBaseWyeTable_Object((1,3,6,1,4,1,21239,6,1,99,2))
if mibBuilder.loadTexts:pduBaseWyeTable.setStatus(_A)
_PduBaseWyeEntry_Object=MibTableRow
pduBaseWyeEntry=_PduBaseWyeEntry_Object((1,3,6,1,4,1,21239,6,1,99,2,1))
pduBaseWyeEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:pduBaseWyeEntry.setStatus(_A)
class _PduBaseWyeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PduBaseWyeIndex_Type.__name__=_E
_PduBaseWyeIndex_Object=MibTableColumn
pduBaseWyeIndex=_PduBaseWyeIndex_Object((1,3,6,1,4,1,21239,6,1,99,2,1,1),_PduBaseWyeIndex_Type())
pduBaseWyeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pduBaseWyeIndex.setStatus(_A)
_PduBaseWyeSerial_Type=DeviceSerial
_PduBaseWyeSerial_Object=MibTableColumn
pduBaseWyeSerial=_PduBaseWyeSerial_Object((1,3,6,1,4,1,21239,6,1,99,2,1,2),_PduBaseWyeSerial_Type())
pduBaseWyeSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:pduBaseWyeSerial.setStatus(_A)
_PduBaseWyeLabel_Type=DeviceLabel
_PduBaseWyeLabel_Object=MibTableColumn
pduBaseWyeLabel=_PduBaseWyeLabel_Object((1,3,6,1,4,1,21239,6,1,99,2,1,3),_PduBaseWyeLabel_Type())
pduBaseWyeLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:pduBaseWyeLabel.setStatus(_A)
_PduBaseWyeStatus_Type=DeviceStatus
_PduBaseWyeStatus_Object=MibTableColumn
pduBaseWyeStatus=_PduBaseWyeStatus_Object((1,3,6,1,4,1,21239,6,1,99,2,1,4),_PduBaseWyeStatus_Type())
pduBaseWyeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pduBaseWyeStatus.setStatus(_A)
_PduBaseWyeKWattHrsTotal_Type=Gauge32
_PduBaseWyeKWattHrsTotal_Object=MibTableColumn
pduBaseWyeKWattHrsTotal=_PduBaseWyeKWattHrsTotal_Object((1,3,6,1,4,1,21239,6,1,99,2,1,5),_PduBaseWyeKWattHrsTotal_Type())
pduBaseWyeKWattHrsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:pduBaseWyeKWattHrsTotal.setStatus(_A)
_PduBaseWyeRealPowerTotal_Type=Gauge32
_PduBaseWyeRealPowerTotal_Object=MibTableColumn
pduBaseWyeRealPowerTotal=_PduBaseWyeRealPowerTotal_Object((1,3,6,1,4,1,21239,6,1,99,2,1,6),_PduBaseWyeRealPowerTotal_Type())
pduBaseWyeRealPowerTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:pduBaseWyeRealPowerTotal.setStatus(_A)
class _PduBaseWyeChannelCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_PduBaseWyeChannelCount_Type.__name__=_E
_PduBaseWyeChannelCount_Object=MibTableColumn
pduBaseWyeChannelCount=_PduBaseWyeChannelCount_Object((1,3,6,1,4,1,21239,6,1,99,2,1,7),_PduBaseWyeChannelCount_Type())
pduBaseWyeChannelCount.setMaxAccess(_B)
if mibBuilder.loadTexts:pduBaseWyeChannelCount.setStatus(_A)
_PduChannelDeltaTable_Object=MibTable
pduChannelDeltaTable=_PduChannelDeltaTable_Object((1,3,6,1,4,1,21239,6,1,99,3))
if mibBuilder.loadTexts:pduChannelDeltaTable.setStatus(_A)
_PduChannelDeltaEntry_Object=MibTableRow
pduChannelDeltaEntry=_PduChannelDeltaEntry_Object((1,3,6,1,4,1,21239,6,1,99,3,1))
pduChannelDeltaEntry.setIndexNames((0,_D,_J),(0,_D,_R))
if mibBuilder.loadTexts:pduChannelDeltaEntry.setStatus(_A)
class _PduChannelDeltaID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_PduChannelDeltaID_Type.__name__=_E
_PduChannelDeltaID_Object=MibTableColumn
pduChannelDeltaID=_PduChannelDeltaID_Object((1,3,6,1,4,1,21239,6,1,99,3,1,1),_PduChannelDeltaID_Type())
pduChannelDeltaID.setMaxAccess(_B)
if mibBuilder.loadTexts:pduChannelDeltaID.setStatus(_A)
_PduChannelDeltaLabel_Type=DeviceLabel
_PduChannelDeltaLabel_Object=MibTableColumn
pduChannelDeltaLabel=_PduChannelDeltaLabel_Object((1,3,6,1,4,1,21239,6,1,99,3,1,2),_PduChannelDeltaLabel_Type())
pduChannelDeltaLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:pduChannelDeltaLabel.setStatus(_A)
_PduChannelDeltaName_Type=DisplayString
_PduChannelDeltaName_Object=MibTableColumn
pduChannelDeltaName=_PduChannelDeltaName_Object((1,3,6,1,4,1,21239,6,1,99,3,1,3),_PduChannelDeltaName_Type())
pduChannelDeltaName.setMaxAccess(_B)
if mibBuilder.loadTexts:pduChannelDeltaName.setStatus(_A)
_PduChannelDeltaKWattHrs_Type=Gauge32
_PduChannelDeltaKWattHrs_Object=MibTableColumn
pduChannelDeltaKWattHrs=_PduChannelDeltaKWattHrs_Object((1,3,6,1,4,1,21239,6,1,99,3,1,4),_PduChannelDeltaKWattHrs_Type())
pduChannelDeltaKWattHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:pduChannelDeltaKWattHrs.setStatus(_A)
_PduChannelDeltaVolts_Type=Gauge32
_PduChannelDeltaVolts_Object=MibTableColumn
pduChannelDeltaVolts=_PduChannelDeltaVolts_Object((1,3,6,1,4,1,21239,6,1,99,3,1,5),_PduChannelDeltaVolts_Type())
pduChannelDeltaVolts.setMaxAccess(_B)
if mibBuilder.loadTexts:pduChannelDeltaVolts.setStatus(_A)
_PduChannelDeltaRealPower_Type=Gauge32
_PduChannelDeltaRealPower_Object=MibTableColumn
pduChannelDeltaRealPower=_PduChannelDeltaRealPower_Object((1,3,6,1,4,1,21239,6,1,99,3,1,7),_PduChannelDeltaRealPower_Type())
pduChannelDeltaRealPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pduChannelDeltaRealPower.setStatus(_A)
_PduChannelDeltaApparentPower_Type=Gauge32
_PduChannelDeltaApparentPower_Object=MibTableColumn
pduChannelDeltaApparentPower=_PduChannelDeltaApparentPower_Object((1,3,6,1,4,1,21239,6,1,99,3,1,8),_PduChannelDeltaApparentPower_Type())
pduChannelDeltaApparentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pduChannelDeltaApparentPower.setStatus(_A)
_PduChannelDeltaPowerFactor_Type=Gauge32
_PduChannelDeltaPowerFactor_Object=MibTableColumn
pduChannelDeltaPowerFactor=_PduChannelDeltaPowerFactor_Object((1,3,6,1,4,1,21239,6,1,99,3,1,9),_PduChannelDeltaPowerFactor_Type())
pduChannelDeltaPowerFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:pduChannelDeltaPowerFactor.setStatus(_A)
_PduChannelDeltaAmps_Type=DeciAmps
_PduChannelDeltaAmps_Object=MibTableColumn
pduChannelDeltaAmps=_PduChannelDeltaAmps_Object((1,3,6,1,4,1,21239,6,1,99,3,1,10),_PduChannelDeltaAmps_Type())
pduChannelDeltaAmps.setMaxAccess(_B)
if mibBuilder.loadTexts:pduChannelDeltaAmps.setStatus(_A)
_PduChannelWyeTable_Object=MibTable
pduChannelWyeTable=_PduChannelWyeTable_Object((1,3,6,1,4,1,21239,6,1,99,4))
if mibBuilder.loadTexts:pduChannelWyeTable.setStatus(_A)
_PduChannelWyeEntry_Object=MibTableRow
pduChannelWyeEntry=_PduChannelWyeEntry_Object((1,3,6,1,4,1,21239,6,1,99,4,1))
pduChannelWyeEntry.setIndexNames((0,_D,_K),(0,_D,_S))
if mibBuilder.loadTexts:pduChannelWyeEntry.setStatus(_A)
class _PduChannelWyeID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_PduChannelWyeID_Type.__name__=_E
_PduChannelWyeID_Object=MibTableColumn
pduChannelWyeID=_PduChannelWyeID_Object((1,3,6,1,4,1,21239,6,1,99,4,1,1),_PduChannelWyeID_Type())
pduChannelWyeID.setMaxAccess(_B)
if mibBuilder.loadTexts:pduChannelWyeID.setStatus(_A)
_PduChannelWyeLabel_Type=DeviceLabel
_PduChannelWyeLabel_Object=MibTableColumn
pduChannelWyeLabel=_PduChannelWyeLabel_Object((1,3,6,1,4,1,21239,6,1,99,4,1,2),_PduChannelWyeLabel_Type())
pduChannelWyeLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:pduChannelWyeLabel.setStatus(_A)
_PduChannelWyeName_Type=DisplayString
_PduChannelWyeName_Object=MibTableColumn
pduChannelWyeName=_PduChannelWyeName_Object((1,3,6,1,4,1,21239,6,1,99,4,1,3),_PduChannelWyeName_Type())
pduChannelWyeName.setMaxAccess(_B)
if mibBuilder.loadTexts:pduChannelWyeName.setStatus(_A)
_PduChannelWyeKWattHrs_Type=Gauge32
_PduChannelWyeKWattHrs_Object=MibTableColumn
pduChannelWyeKWattHrs=_PduChannelWyeKWattHrs_Object((1,3,6,1,4,1,21239,6,1,99,4,1,4),_PduChannelWyeKWattHrs_Type())
pduChannelWyeKWattHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:pduChannelWyeKWattHrs.setStatus(_A)
_PduChannelWyeVolts_Type=Gauge32
_PduChannelWyeVolts_Object=MibTableColumn
pduChannelWyeVolts=_PduChannelWyeVolts_Object((1,3,6,1,4,1,21239,6,1,99,4,1,5),_PduChannelWyeVolts_Type())
pduChannelWyeVolts.setMaxAccess(_B)
if mibBuilder.loadTexts:pduChannelWyeVolts.setStatus(_A)
_PduChannelWyeAmps_Type=DeciAmps
_PduChannelWyeAmps_Object=MibTableColumn
pduChannelWyeAmps=_PduChannelWyeAmps_Object((1,3,6,1,4,1,21239,6,1,99,4,1,7),_PduChannelWyeAmps_Type())
pduChannelWyeAmps.setMaxAccess(_B)
if mibBuilder.loadTexts:pduChannelWyeAmps.setStatus(_A)
_PduChannelWyeRealPower_Type=Gauge32
_PduChannelWyeRealPower_Object=MibTableColumn
pduChannelWyeRealPower=_PduChannelWyeRealPower_Object((1,3,6,1,4,1,21239,6,1,99,4,1,9),_PduChannelWyeRealPower_Type())
pduChannelWyeRealPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pduChannelWyeRealPower.setStatus(_A)
_PduChannelWyeApparentPower_Type=Gauge32
_PduChannelWyeApparentPower_Object=MibTableColumn
pduChannelWyeApparentPower=_PduChannelWyeApparentPower_Object((1,3,6,1,4,1,21239,6,1,99,4,1,10),_PduChannelWyeApparentPower_Type())
pduChannelWyeApparentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pduChannelWyeApparentPower.setStatus(_A)
_PduChannelWyePowerFactor_Type=Gauge32
_PduChannelWyePowerFactor_Object=MibTableColumn
pduChannelWyePowerFactor=_PduChannelWyePowerFactor_Object((1,3,6,1,4,1,21239,6,1,99,4,1,11),_PduChannelWyePowerFactor_Type())
pduChannelWyePowerFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:pduChannelWyePowerFactor.setStatus(_A)
_PduGroupTable_Object=MibTable
pduGroupTable=_PduGroupTable_Object((1,3,6,1,4,1,21239,6,1,99,5))
if mibBuilder.loadTexts:pduGroupTable.setStatus(_A)
_PduGroupEntry_Object=MibTableRow
pduGroupEntry=_PduGroupEntry_Object((1,3,6,1,4,1,21239,6,1,99,5,1))
pduGroupEntry.setIndexNames((0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:pduGroupEntry.setStatus(_A)
class _PduGroupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PduGroupIndex_Type.__name__=_E
_PduGroupIndex_Object=MibTableColumn
pduGroupIndex=_PduGroupIndex_Object((1,3,6,1,4,1,21239,6,1,99,5,1,1),_PduGroupIndex_Type())
pduGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pduGroupIndex.setStatus(_A)
_PduGroupSerial_Type=DeviceSerial
_PduGroupSerial_Object=MibTableColumn
pduGroupSerial=_PduGroupSerial_Object((1,3,6,1,4,1,21239,6,1,99,5,1,2),_PduGroupSerial_Type())
pduGroupSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:pduGroupSerial.setStatus(_A)
class _PduGroupID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PduGroupID_Type.__name__=_E
_PduGroupID_Object=MibTableColumn
pduGroupID=_PduGroupID_Object((1,3,6,1,4,1,21239,6,1,99,5,1,3),_PduGroupID_Type())
pduGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:pduGroupID.setStatus(_A)
_PduGroupLabel_Type=DeviceLabel
_PduGroupLabel_Object=MibTableColumn
pduGroupLabel=_PduGroupLabel_Object((1,3,6,1,4,1,21239,6,1,99,5,1,4),_PduGroupLabel_Type())
pduGroupLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:pduGroupLabel.setStatus(_A)
_PduGroupName_Type=DisplayString
_PduGroupName_Object=MibTableColumn
pduGroupName=_PduGroupName_Object((1,3,6,1,4,1,21239,6,1,99,5,1,5),_PduGroupName_Type())
pduGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:pduGroupName.setStatus(_A)
_PduGroupAmps_Type=DeciAmps
_PduGroupAmps_Object=MibTableColumn
pduGroupAmps=_PduGroupAmps_Object((1,3,6,1,4,1,21239,6,1,99,5,1,6),_PduGroupAmps_Type())
pduGroupAmps.setMaxAccess(_B)
if mibBuilder.loadTexts:pduGroupAmps.setStatus(_A)
_PduGroupApparentPower_Type=Gauge32
_PduGroupApparentPower_Object=MibTableColumn
pduGroupApparentPower=_PduGroupApparentPower_Object((1,3,6,1,4,1,21239,6,1,99,5,1,8),_PduGroupApparentPower_Type())
pduGroupApparentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pduGroupApparentPower.setStatus(_A)
_PduGroupPowerFactor_Type=Gauge32
_PduGroupPowerFactor_Object=MibTableColumn
pduGroupPowerFactor=_PduGroupPowerFactor_Object((1,3,6,1,4,1,21239,6,1,99,5,1,9),_PduGroupPowerFactor_Type())
pduGroupPowerFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:pduGroupPowerFactor.setStatus(_A)
_PduGroupRealPower_Type=Gauge32
_PduGroupRealPower_Object=MibTableColumn
pduGroupRealPower=_PduGroupRealPower_Object((1,3,6,1,4,1,21239,6,1,99,5,1,10),_PduGroupRealPower_Type())
pduGroupRealPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pduGroupRealPower.setStatus(_A)
_PduGroupVolts_Type=Gauge32
_PduGroupVolts_Object=MibTableColumn
pduGroupVolts=_PduGroupVolts_Object((1,3,6,1,4,1,21239,6,1,99,5,1,11),_PduGroupVolts_Type())
pduGroupVolts.setMaxAccess(_B)
if mibBuilder.loadTexts:pduGroupVolts.setStatus(_A)
_PduGroupWattHours_Type=Gauge32
_PduGroupWattHours_Object=MibTableColumn
pduGroupWattHours=_PduGroupWattHours_Object((1,3,6,1,4,1,21239,6,1,99,5,1,13),_PduGroupWattHours_Type())
pduGroupWattHours.setMaxAccess(_B)
if mibBuilder.loadTexts:pduGroupWattHours.setStatus(_A)
_PduOutletMainTable_Object=MibTable
pduOutletMainTable=_PduOutletMainTable_Object((1,3,6,1,4,1,21239,6,1,99,6))
if mibBuilder.loadTexts:pduOutletMainTable.setStatus(_A)
_PduOutletMainEntry_Object=MibTableRow
pduOutletMainEntry=_PduOutletMainEntry_Object((1,3,6,1,4,1,21239,6,1,99,6,1))
pduOutletMainEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:pduOutletMainEntry.setStatus(_A)
class _PduOutletMainIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PduOutletMainIndex_Type.__name__=_E
_PduOutletMainIndex_Object=MibTableColumn
pduOutletMainIndex=_PduOutletMainIndex_Object((1,3,6,1,4,1,21239,6,1,99,6,1,1),_PduOutletMainIndex_Type())
pduOutletMainIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pduOutletMainIndex.setStatus(_A)
_PduOutletMainSerial_Type=DeviceSerial
_PduOutletMainSerial_Object=MibTableColumn
pduOutletMainSerial=_PduOutletMainSerial_Object((1,3,6,1,4,1,21239,6,1,99,6,1,2),_PduOutletMainSerial_Type())
pduOutletMainSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:pduOutletMainSerial.setStatus(_A)
class _PduOutletMainID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PduOutletMainID_Type.__name__=_E
_PduOutletMainID_Object=MibTableColumn
pduOutletMainID=_PduOutletMainID_Object((1,3,6,1,4,1,21239,6,1,99,6,1,3),_PduOutletMainID_Type())
pduOutletMainID.setMaxAccess(_B)
if mibBuilder.loadTexts:pduOutletMainID.setStatus(_A)
_PduOutletMainLabel_Type=DeviceLabel
_PduOutletMainLabel_Object=MibTableColumn
pduOutletMainLabel=_PduOutletMainLabel_Object((1,3,6,1,4,1,21239,6,1,99,6,1,4),_PduOutletMainLabel_Type())
pduOutletMainLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:pduOutletMainLabel.setStatus(_A)
_PduOutletMainName_Type=DisplayString
_PduOutletMainName_Object=MibTableColumn
pduOutletMainName=_PduOutletMainName_Object((1,3,6,1,4,1,21239,6,1,99,6,1,5),_PduOutletMainName_Type())
pduOutletMainName.setMaxAccess(_B)
if mibBuilder.loadTexts:pduOutletMainName.setStatus(_A)
_PduOutletMainGroup_Type=DisplayString
_PduOutletMainGroup_Object=MibTableColumn
pduOutletMainGroup=_PduOutletMainGroup_Object((1,3,6,1,4,1,21239,6,1,99,6,1,6),_PduOutletMainGroup_Type())
pduOutletMainGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:pduOutletMainGroup.setStatus(_A)
_PduOutletMainURL_Type=DisplayString
_PduOutletMainURL_Object=MibTableColumn
pduOutletMainURL=_PduOutletMainURL_Object((1,3,6,1,4,1,21239,6,1,99,6,1,7),_PduOutletMainURL_Type())
pduOutletMainURL.setMaxAccess(_B)
if mibBuilder.loadTexts:pduOutletMainURL.setStatus(_A)
_PduOutletSwitchTable_Object=MibTable
pduOutletSwitchTable=_PduOutletSwitchTable_Object((1,3,6,1,4,1,21239,6,1,99,7))
if mibBuilder.loadTexts:pduOutletSwitchTable.setStatus(_A)
_PduOutletSwitchEntry_Object=MibTableRow
pduOutletSwitchEntry=_PduOutletSwitchEntry_Object((1,3,6,1,4,1,21239,6,1,99,7,1))
pduOutletSwitchEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:pduOutletSwitchEntry.setStatus(_A)
class _PduOutletSwitchState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('outletOff',0),('outletOn',1),('outletError',2)))
_PduOutletSwitchState_Type.__name__=_G
_PduOutletSwitchState_Object=MibTableColumn
pduOutletSwitchState=_PduOutletSwitchState_Object((1,3,6,1,4,1,21239,6,1,99,7,1,1),_PduOutletSwitchState_Type())
pduOutletSwitchState.setMaxAccess(_B)
if mibBuilder.loadTexts:pduOutletSwitchState.setStatus(_A)
_PduOutletSwitchStateChangeTime_Type=Unsigned32
_PduOutletSwitchStateChangeTime_Object=MibTableColumn
pduOutletSwitchStateChangeTime=_PduOutletSwitchStateChangeTime_Object((1,3,6,1,4,1,21239,6,1,99,7,1,2),_PduOutletSwitchStateChangeTime_Type())
pduOutletSwitchStateChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:pduOutletSwitchStateChangeTime.setStatus(_A)
class _PduOutletSwitchCurrentAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('manual',1),('reboot',2),('startUp',3),('other',4)))
_PduOutletSwitchCurrentAction_Type.__name__=_G
_PduOutletSwitchCurrentAction_Object=MibTableColumn
pduOutletSwitchCurrentAction=_PduOutletSwitchCurrentAction_Object((1,3,6,1,4,1,21239,6,1,99,7,1,3),_PduOutletSwitchCurrentAction_Type())
pduOutletSwitchCurrentAction.setMaxAccess(_B)
if mibBuilder.loadTexts:pduOutletSwitchCurrentAction.setStatus(_A)
_PduOutletSwitchOnDelay_Type=Unsigned32
_PduOutletSwitchOnDelay_Object=MibTableColumn
pduOutletSwitchOnDelay=_PduOutletSwitchOnDelay_Object((1,3,6,1,4,1,21239,6,1,99,7,1,4),_PduOutletSwitchOnDelay_Type())
pduOutletSwitchOnDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pduOutletSwitchOnDelay.setStatus(_A)
_PduOutletSwitchOffDelay_Type=Unsigned32
_PduOutletSwitchOffDelay_Object=MibTableColumn
pduOutletSwitchOffDelay=_PduOutletSwitchOffDelay_Object((1,3,6,1,4,1,21239,6,1,99,7,1,5),_PduOutletSwitchOffDelay_Type())
pduOutletSwitchOffDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pduOutletSwitchOffDelay.setStatus(_A)
_PduOutletSwitchRebootDelay_Type=Unsigned32
_PduOutletSwitchRebootDelay_Object=MibTableColumn
pduOutletSwitchRebootDelay=_PduOutletSwitchRebootDelay_Object((1,3,6,1,4,1,21239,6,1,99,7,1,6),_PduOutletSwitchRebootDelay_Type())
pduOutletSwitchRebootDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pduOutletSwitchRebootDelay.setStatus(_A)
_PduOutletSwitchRebootHold_Type=Unsigned32
_PduOutletSwitchRebootHold_Object=MibTableColumn
pduOutletSwitchRebootHold=_PduOutletSwitchRebootHold_Object((1,3,6,1,4,1,21239,6,1,99,7,1,7),_PduOutletSwitchRebootHold_Type())
pduOutletSwitchRebootHold.setMaxAccess(_C)
if mibBuilder.loadTexts:pduOutletSwitchRebootHold.setStatus(_A)
class _PduOutletSwitchStartupAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('startOff',0),('startOn',1),('lastKnown',2)))
_PduOutletSwitchStartupAction_Type.__name__=_G
_PduOutletSwitchStartupAction_Object=MibTableColumn
pduOutletSwitchStartupAction=_PduOutletSwitchStartupAction_Object((1,3,6,1,4,1,21239,6,1,99,7,1,8),_PduOutletSwitchStartupAction_Type())
pduOutletSwitchStartupAction.setMaxAccess(_C)
if mibBuilder.loadTexts:pduOutletSwitchStartupAction.setStatus(_A)
_PduOutletSwitchStartupStateDelay_Type=Unsigned32
_PduOutletSwitchStartupStateDelay_Object=MibTableColumn
pduOutletSwitchStartupStateDelay=_PduOutletSwitchStartupStateDelay_Object((1,3,6,1,4,1,21239,6,1,99,7,1,9),_PduOutletSwitchStartupStateDelay_Type())
pduOutletSwitchStartupStateDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pduOutletSwitchStartupStateDelay.setStatus(_A)
class _PduOutletSwitchControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',0),('cancelActions',1),('onNoDelay',2),('onDelay',3),('offNoDelay',4),('offDelay',5),('rebootNoDelay',6),('rebootDelay',7)))
_PduOutletSwitchControl_Type.__name__=_G
_PduOutletSwitchControl_Object=MibTableColumn
pduOutletSwitchControl=_PduOutletSwitchControl_Object((1,3,6,1,4,1,21239,6,1,99,7,1,10),_PduOutletSwitchControl_Type())
pduOutletSwitchControl.setMaxAccess(_C)
if mibBuilder.loadTexts:pduOutletSwitchControl.setStatus(_A)
_PduOutletMeterTable_Object=MibTable
pduOutletMeterTable=_PduOutletMeterTable_Object((1,3,6,1,4,1,21239,6,1,99,8))
if mibBuilder.loadTexts:pduOutletMeterTable.setStatus(_A)
_PduOutletMeterEntry_Object=MibTableRow
pduOutletMeterEntry=_PduOutletMeterEntry_Object((1,3,6,1,4,1,21239,6,1,99,8,1))
pduOutletMeterEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:pduOutletMeterEntry.setStatus(_A)
_PduOutletMeterKWattHrs_Type=Gauge32
_PduOutletMeterKWattHrs_Object=MibTableColumn
pduOutletMeterKWattHrs=_PduOutletMeterKWattHrs_Object((1,3,6,1,4,1,21239,6,1,99,8,1,1),_PduOutletMeterKWattHrs_Type())
pduOutletMeterKWattHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:pduOutletMeterKWattHrs.setStatus(_A)
_PduOutletMeterAmps_Type=DeciAmps
_PduOutletMeterAmps_Object=MibTableColumn
pduOutletMeterAmps=_PduOutletMeterAmps_Object((1,3,6,1,4,1,21239,6,1,99,8,1,2),_PduOutletMeterAmps_Type())
pduOutletMeterAmps.setMaxAccess(_B)
if mibBuilder.loadTexts:pduOutletMeterAmps.setStatus(_A)
_PduOutletMeterPower_Type=Gauge32
_PduOutletMeterPower_Object=MibTableColumn
pduOutletMeterPower=_PduOutletMeterPower_Object((1,3,6,1,4,1,21239,6,1,99,8,1,3),_PduOutletMeterPower_Type())
pduOutletMeterPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pduOutletMeterPower.setStatus(_A)
_Common_ObjectIdentity=ObjectIdentity
common=_Common_ObjectIdentity((1,3,6,1,4,1,21239,42))
_Identity_ObjectIdentity=ObjectIdentity
identity=_Identity_ObjectIdentity((1,3,6,1,4,1,21239,42,1))
_R05_ObjectIdentity=ObjectIdentity
r05=_R05_ObjectIdentity((1,3,6,1,4,1,21239,42,1,15))
if mibBuilder.loadTexts:r05.setStatus(_V)
_I03_ObjectIdentity=ObjectIdentity
i03=_I03_ObjectIdentity((1,3,6,1,4,1,21239,42,1,53))
if mibBuilder.loadTexts:i03.setStatus(_V)
mibBuilder.exportSymbols(_D,**{'DeviceSerial':DeviceSerial,'DeviceStatus':DeviceStatus,'DeviceLabel':DeviceLabel,'TemperatureUnits':TemperatureUnits,'TemperatureValue':TemperatureValue,'DeciAmps':DeciAmps,'vertiv':vertiv,'quetzal':quetzal,'devices':devices,'rtafhd3':rtafhd3,'rtafhd3Table':rtafhd3Table,'rtafhd3Entry':rtafhd3Entry,_L:rtafhd3Index,'rtafhd3Serial':rtafhd3Serial,'rtafhd3Label':rtafhd3Label,'rtafhd3Status':rtafhd3Status,'rtafhd3Airflow':rtafhd3Airflow,'rtafhd3Humidity':rtafhd3Humidity,'rtafhd3Temp':rtafhd3Temp,'rtafhd3DewPoint':rtafhd3DewPoint,'rtafhd3TDUnits':rtafhd3TDUnits,'rt':rt,'rtTable':rtTable,'rtEntry':rtEntry,_M:rtIndex,'rtSerial':rtSerial,'rtLabel':rtLabel,'rtStatus':rtStatus,'rtTemp':rtTemp,'rtUnits':rtUnits,'t3hd':t3hd,'t3hdTable':t3hdTable,'t3hdEntry':t3hdEntry,_N:t3hdIndex,'t3hdSerial':t3hdSerial,'t3hdLabel':t3hdLabel,'t3hdStatus':t3hdStatus,'t3hdMainLabel':t3hdMainLabel,'t3hdMainTemp':t3hdMainTemp,'t3hdMainHumidity':t3hdMainHumidity,'t3hdMainDewPoint':t3hdMainDewPoint,'t3hdExt1Status':t3hdExt1Status,'t3hdExt1Label':t3hdExt1Label,'t3hdExt1Temp':t3hdExt1Temp,'t3hdExt2Status':t3hdExt2Status,'t3hdExt2Label':t3hdExt2Label,'t3hdExt2Temp':t3hdExt2Temp,'t3hdTDUnits':t3hdTDUnits,'thd':thd,'thdTable':thdTable,'thdEntry':thdEntry,_Q:thdIndex,'thdSerial':thdSerial,'thdLabel':thdLabel,'thdStatus':thdStatus,'thdTemp':thdTemp,'thdHumidity':thdHumidity,'thdDewPoint':thdDewPoint,'thdTDUnits':thdTDUnits,'legacyPDU':legacyPDU,'pduBaseDeltaTable':pduBaseDeltaTable,'pduBaseDeltaEntry':pduBaseDeltaEntry,_J:pduBaseDeltaIndex,'pduBaseDeltaSerial':pduBaseDeltaSerial,'pduBaseDeltaLabel':pduBaseDeltaLabel,'pduBaseDeltaStatus':pduBaseDeltaStatus,'pduBaseDeltaKWattHrsTotal':pduBaseDeltaKWattHrsTotal,'pduBaseDeltaRealPowerTotal':pduBaseDeltaRealPowerTotal,'pduBaseDeltaAmpsA':pduBaseDeltaAmpsA,'pduBaseDeltaAmpsB':pduBaseDeltaAmpsB,'pduBaseDeltaAmpsC':pduBaseDeltaAmpsC,'pduBaseWyeTable':pduBaseWyeTable,'pduBaseWyeEntry':pduBaseWyeEntry,_K:pduBaseWyeIndex,'pduBaseWyeSerial':pduBaseWyeSerial,'pduBaseWyeLabel':pduBaseWyeLabel,'pduBaseWyeStatus':pduBaseWyeStatus,'pduBaseWyeKWattHrsTotal':pduBaseWyeKWattHrsTotal,'pduBaseWyeRealPowerTotal':pduBaseWyeRealPowerTotal,'pduBaseWyeChannelCount':pduBaseWyeChannelCount,'pduChannelDeltaTable':pduChannelDeltaTable,'pduChannelDeltaEntry':pduChannelDeltaEntry,_R:pduChannelDeltaID,'pduChannelDeltaLabel':pduChannelDeltaLabel,'pduChannelDeltaName':pduChannelDeltaName,'pduChannelDeltaKWattHrs':pduChannelDeltaKWattHrs,'pduChannelDeltaVolts':pduChannelDeltaVolts,'pduChannelDeltaRealPower':pduChannelDeltaRealPower,'pduChannelDeltaApparentPower':pduChannelDeltaApparentPower,'pduChannelDeltaPowerFactor':pduChannelDeltaPowerFactor,'pduChannelDeltaAmps':pduChannelDeltaAmps,'pduChannelWyeTable':pduChannelWyeTable,'pduChannelWyeEntry':pduChannelWyeEntry,_S:pduChannelWyeID,'pduChannelWyeLabel':pduChannelWyeLabel,'pduChannelWyeName':pduChannelWyeName,'pduChannelWyeKWattHrs':pduChannelWyeKWattHrs,'pduChannelWyeVolts':pduChannelWyeVolts,'pduChannelWyeAmps':pduChannelWyeAmps,'pduChannelWyeRealPower':pduChannelWyeRealPower,'pduChannelWyeApparentPower':pduChannelWyeApparentPower,'pduChannelWyePowerFactor':pduChannelWyePowerFactor,'pduGroupTable':pduGroupTable,'pduGroupEntry':pduGroupEntry,_T:pduGroupIndex,'pduGroupSerial':pduGroupSerial,_U:pduGroupID,'pduGroupLabel':pduGroupLabel,'pduGroupName':pduGroupName,'pduGroupAmps':pduGroupAmps,'pduGroupApparentPower':pduGroupApparentPower,'pduGroupPowerFactor':pduGroupPowerFactor,'pduGroupRealPower':pduGroupRealPower,'pduGroupVolts':pduGroupVolts,'pduGroupWattHours':pduGroupWattHours,'pduOutletMainTable':pduOutletMainTable,'pduOutletMainEntry':pduOutletMainEntry,_H:pduOutletMainIndex,'pduOutletMainSerial':pduOutletMainSerial,_I:pduOutletMainID,'pduOutletMainLabel':pduOutletMainLabel,'pduOutletMainName':pduOutletMainName,'pduOutletMainGroup':pduOutletMainGroup,'pduOutletMainURL':pduOutletMainURL,'pduOutletSwitchTable':pduOutletSwitchTable,'pduOutletSwitchEntry':pduOutletSwitchEntry,'pduOutletSwitchState':pduOutletSwitchState,'pduOutletSwitchStateChangeTime':pduOutletSwitchStateChangeTime,'pduOutletSwitchCurrentAction':pduOutletSwitchCurrentAction,'pduOutletSwitchOnDelay':pduOutletSwitchOnDelay,'pduOutletSwitchOffDelay':pduOutletSwitchOffDelay,'pduOutletSwitchRebootDelay':pduOutletSwitchRebootDelay,'pduOutletSwitchRebootHold':pduOutletSwitchRebootHold,'pduOutletSwitchStartupAction':pduOutletSwitchStartupAction,'pduOutletSwitchStartupStateDelay':pduOutletSwitchStartupStateDelay,'pduOutletSwitchControl':pduOutletSwitchControl,'pduOutletMeterTable':pduOutletMeterTable,'pduOutletMeterEntry':pduOutletMeterEntry,'pduOutletMeterKWattHrs':pduOutletMeterKWattHrs,'pduOutletMeterAmps':pduOutletMeterAmps,'pduOutletMeterPower':pduOutletMeterPower,'common':common,'identity':identity,'r05':r05,'i03':i03})