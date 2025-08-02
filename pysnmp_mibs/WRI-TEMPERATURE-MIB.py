_M='temperatureHThreshold'
_L='temperatureLThreshold'
_K='temperatureIndex'
_J='temperatureValue'
_I='temperatureDescr'
_H='disable'
_G='enable'
_F='DisplayString'
_E='read-only'
_D='Integer32'
_C='WRI-TEMPERATURE-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
wri,wriProducts=mibBuilder.importSymbols('WRI-SMI','wri','wriProducts')
msppTemperature=ModuleIdentity((1,3,6,1,4,1,3807,1,8012,1,6))
if mibBuilder.loadTexts:msppTemperature.setRevisions(('2010-01-11 00:00','2009-01-11 00:00'))
class DisplayString(TextualConvention,OctetString):status=_A
_Mspp_ObjectIdentity=ObjectIdentity
mspp=_Mspp_ObjectIdentity((1,3,6,1,4,1,3807,1,8012))
_MsppChassis_ObjectIdentity=ObjectIdentity
msppChassis=_MsppChassis_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,1))
_TemperatureGeneral_ObjectIdentity=ObjectIdentity
temperatureGeneral=_TemperatureGeneral_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,1,6,1))
class _TemperatureTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_TemperatureTrapEnable_Type.__name__=_D
_TemperatureTrapEnable_Object=MibScalar
temperatureTrapEnable=_TemperatureTrapEnable_Object((1,3,6,1,4,1,3807,1,8012,1,6,1,1),_TemperatureTrapEnable_Type())
temperatureTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureTrapEnable.setStatus(_A)
class _TemperatureMonitorEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_TemperatureMonitorEnable_Type.__name__=_D
_TemperatureMonitorEnable_Object=MibScalar
temperatureMonitorEnable=_TemperatureMonitorEnable_Object((1,3,6,1,4,1,3807,1,8012,1,6,1,2),_TemperatureMonitorEnable_Type())
temperatureMonitorEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureMonitorEnable.setStatus(_A)
_TemperatureNumber_Type=Integer32
_TemperatureNumber_Object=MibScalar
temperatureNumber=_TemperatureNumber_Object((1,3,6,1,4,1,3807,1,8012,1,6,1,3),_TemperatureNumber_Type())
temperatureNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:temperatureNumber.setStatus(_A)
_TemperatureTable_Object=MibTable
temperatureTable=_TemperatureTable_Object((1,3,6,1,4,1,3807,1,8012,1,6,2))
if mibBuilder.loadTexts:temperatureTable.setStatus(_A)
_TemperatureEntry_Object=MibTableRow
temperatureEntry=_TemperatureEntry_Object((1,3,6,1,4,1,3807,1,8012,1,6,2,1))
temperatureEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:temperatureEntry.setStatus(_A)
_TemperatureIndex_Type=Unsigned32
_TemperatureIndex_Object=MibTableColumn
temperatureIndex=_TemperatureIndex_Object((1,3,6,1,4,1,3807,1,8012,1,6,2,1,1),_TemperatureIndex_Type())
temperatureIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:temperatureIndex.setStatus(_A)
class _TemperatureDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TemperatureDescr_Type.__name__=_F
_TemperatureDescr_Object=MibTableColumn
temperatureDescr=_TemperatureDescr_Object((1,3,6,1,4,1,3807,1,8012,1,6,2,1,2),_TemperatureDescr_Type())
temperatureDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureDescr.setStatus(_A)
_TemperatureLThreshold_Type=Integer32
_TemperatureLThreshold_Object=MibTableColumn
temperatureLThreshold=_TemperatureLThreshold_Object((1,3,6,1,4,1,3807,1,8012,1,6,2,1,3),_TemperatureLThreshold_Type())
temperatureLThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureLThreshold.setStatus(_A)
_TemperatureHThreshold_Type=Integer32
_TemperatureHThreshold_Object=MibTableColumn
temperatureHThreshold=_TemperatureHThreshold_Object((1,3,6,1,4,1,3807,1,8012,1,6,2,1,4),_TemperatureHThreshold_Type())
temperatureHThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureHThreshold.setStatus(_A)
_TemperatureValue_Type=Integer32
_TemperatureValue_Object=MibTableColumn
temperatureValue=_TemperatureValue_Object((1,3,6,1,4,1,3807,1,8012,1,6,2,1,5),_TemperatureValue_Type())
temperatureValue.setMaxAccess(_E)
if mibBuilder.loadTexts:temperatureValue.setStatus(_A)
class _TemperatureState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('normal',0),('lowtrap',1),('hightrap',2)))
_TemperatureState_Type.__name__=_D
_TemperatureState_Object=MibTableColumn
temperatureState=_TemperatureState_Object((1,3,6,1,4,1,3807,1,8012,1,6,2,1,6),_TemperatureState_Type())
temperatureState.setMaxAccess(_E)
if mibBuilder.loadTexts:temperatureState.setStatus(_A)
class _TemperatureTrapEna_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_TemperatureTrapEna_Type.__name__=_D
_TemperatureTrapEna_Object=MibTableColumn
temperatureTrapEna=_TemperatureTrapEna_Object((1,3,6,1,4,1,3807,1,8012,1,6,2,1,7),_TemperatureTrapEna_Type())
temperatureTrapEna.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureTrapEna.setStatus(_A)
_TemperatureAllSetting_Type=OctetString
_TemperatureAllSetting_Object=MibTableColumn
temperatureAllSetting=_TemperatureAllSetting_Object((1,3,6,1,4,1,3807,1,8012,1,6,2,1,8),_TemperatureAllSetting_Type())
temperatureAllSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureAllSetting.setStatus(_A)
_TemperatureIndexDescr_Type=OctetString
_TemperatureIndexDescr_Object=MibTableColumn
temperatureIndexDescr=_TemperatureIndexDescr_Object((1,3,6,1,4,1,3807,1,8012,1,6,2,1,9),_TemperatureIndexDescr_Type())
temperatureIndexDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:temperatureIndexDescr.setStatus(_A)
_TemperatureRebootHThreshold_Type=Integer32
_TemperatureRebootHThreshold_Object=MibTableColumn
temperatureRebootHThreshold=_TemperatureRebootHThreshold_Object((1,3,6,1,4,1,3807,1,8012,1,6,2,1,10),_TemperatureRebootHThreshold_Type())
temperatureRebootHThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureRebootHThreshold.setStatus(_A)
_TemperatureTrap_ObjectIdentity=ObjectIdentity
temperatureTrap=_TemperatureTrap_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,1,6,3))
temperatureOk=NotificationType((1,3,6,1,4,1,3807,1,8012,1,6,3,1))
temperatureOk.setObjects(*((_C,_I),(_C,_J)))
if mibBuilder.loadTexts:temperatureOk.setStatus(_A)
temperatureFault=NotificationType((1,3,6,1,4,1,3807,1,8012,1,6,3,2))
temperatureFault.setObjects(*((_C,_I),(_C,_J),(_C,_L),(_C,_M)))
if mibBuilder.loadTexts:temperatureFault.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_F:DisplayString,'mspp':mspp,'msppChassis':msppChassis,'msppTemperature':msppTemperature,'temperatureGeneral':temperatureGeneral,'temperatureTrapEnable':temperatureTrapEnable,'temperatureMonitorEnable':temperatureMonitorEnable,'temperatureNumber':temperatureNumber,'temperatureTable':temperatureTable,'temperatureEntry':temperatureEntry,_K:temperatureIndex,_I:temperatureDescr,_L:temperatureLThreshold,_M:temperatureHThreshold,_J:temperatureValue,'temperatureState':temperatureState,'temperatureTrapEna':temperatureTrapEna,'temperatureAllSetting':temperatureAllSetting,'temperatureIndexDescr':temperatureIndexDescr,'temperatureRebootHThreshold':temperatureRebootHThreshold,'temperatureTrap':temperatureTrap,'temperatureOk':temperatureOk,'temperatureFault':temperatureFault})