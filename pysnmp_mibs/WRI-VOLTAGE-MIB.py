_M='voltageHThreshold'
_L='voltageLThreshold'
_K='voltageIndex'
_J='voltageValue'
_I='voltageDescr'
_H='disable'
_G='enable'
_F='DisplayString'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='WRI-VOLTAGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
wri,wriProducts=mibBuilder.importSymbols('WRI-SMI','wri','wriProducts')
msppVoltage=ModuleIdentity((1,3,6,1,4,1,3807,1,8012,1,7))
if mibBuilder.loadTexts:msppVoltage.setRevisions(('2010-01-11 00:00','2009-01-11 00:00'))
class DisplayString(TextualConvention,OctetString):status=_A
_Mspp_ObjectIdentity=ObjectIdentity
mspp=_Mspp_ObjectIdentity((1,3,6,1,4,1,3807,1,8012))
_MsppChassis_ObjectIdentity=ObjectIdentity
msppChassis=_MsppChassis_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,1))
_VoltageGeneral_ObjectIdentity=ObjectIdentity
voltageGeneral=_VoltageGeneral_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,1,7,1))
class _VoltageTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_VoltageTrapEnable_Type.__name__=_D
_VoltageTrapEnable_Object=MibScalar
voltageTrapEnable=_VoltageTrapEnable_Object((1,3,6,1,4,1,3807,1,8012,1,7,1,1),_VoltageTrapEnable_Type())
voltageTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:voltageTrapEnable.setStatus(_A)
class _VoltageMonitorEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_VoltageMonitorEnable_Type.__name__=_D
_VoltageMonitorEnable_Object=MibScalar
voltageMonitorEnable=_VoltageMonitorEnable_Object((1,3,6,1,4,1,3807,1,8012,1,7,1,2),_VoltageMonitorEnable_Type())
voltageMonitorEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:voltageMonitorEnable.setStatus(_A)
_VoltageNumber_Type=Integer32
_VoltageNumber_Object=MibScalar
voltageNumber=_VoltageNumber_Object((1,3,6,1,4,1,3807,1,8012,1,7,1,3),_VoltageNumber_Type())
voltageNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:voltageNumber.setStatus(_A)
_VoltageTable_Object=MibTable
voltageTable=_VoltageTable_Object((1,3,6,1,4,1,3807,1,8012,1,7,2))
if mibBuilder.loadTexts:voltageTable.setStatus(_A)
_VoltageEntry_Object=MibTableRow
voltageEntry=_VoltageEntry_Object((1,3,6,1,4,1,3807,1,8012,1,7,2,1))
voltageEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:voltageEntry.setStatus(_A)
_VoltageIndex_Type=Unsigned32
_VoltageIndex_Object=MibTableColumn
voltageIndex=_VoltageIndex_Object((1,3,6,1,4,1,3807,1,8012,1,7,2,1,1),_VoltageIndex_Type())
voltageIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:voltageIndex.setStatus(_A)
class _VoltageDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_VoltageDescr_Type.__name__=_F
_VoltageDescr_Object=MibTableColumn
voltageDescr=_VoltageDescr_Object((1,3,6,1,4,1,3807,1,8012,1,7,2,1,2),_VoltageDescr_Type())
voltageDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:voltageDescr.setStatus(_A)
_VoltageLThreshold_Type=Integer32
_VoltageLThreshold_Object=MibTableColumn
voltageLThreshold=_VoltageLThreshold_Object((1,3,6,1,4,1,3807,1,8012,1,7,2,1,3),_VoltageLThreshold_Type())
voltageLThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:voltageLThreshold.setStatus(_A)
_VoltageHThreshold_Type=Integer32
_VoltageHThreshold_Object=MibTableColumn
voltageHThreshold=_VoltageHThreshold_Object((1,3,6,1,4,1,3807,1,8012,1,7,2,1,4),_VoltageHThreshold_Type())
voltageHThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:voltageHThreshold.setStatus(_A)
_VoltageValue_Type=Integer32
_VoltageValue_Object=MibTableColumn
voltageValue=_VoltageValue_Object((1,3,6,1,4,1,3807,1,8012,1,7,2,1,5),_VoltageValue_Type())
voltageValue.setMaxAccess(_E)
if mibBuilder.loadTexts:voltageValue.setStatus(_A)
class _VoltageState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('normal',0),('lowtrap',1),('hightrap',2)))
_VoltageState_Type.__name__=_D
_VoltageState_Object=MibTableColumn
voltageState=_VoltageState_Object((1,3,6,1,4,1,3807,1,8012,1,7,2,1,6),_VoltageState_Type())
voltageState.setMaxAccess(_E)
if mibBuilder.loadTexts:voltageState.setStatus(_A)
class _VoltageTrapEna_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_VoltageTrapEna_Type.__name__=_D
_VoltageTrapEna_Object=MibTableColumn
voltageTrapEna=_VoltageTrapEna_Object((1,3,6,1,4,1,3807,1,8012,1,7,2,1,7),_VoltageTrapEna_Type())
voltageTrapEna.setMaxAccess(_C)
if mibBuilder.loadTexts:voltageTrapEna.setStatus(_A)
_VoltageAllSetting_Type=OctetString
_VoltageAllSetting_Object=MibTableColumn
voltageAllSetting=_VoltageAllSetting_Object((1,3,6,1,4,1,3807,1,8012,1,7,2,1,8),_VoltageAllSetting_Type())
voltageAllSetting.setMaxAccess(_C)
if mibBuilder.loadTexts:voltageAllSetting.setStatus(_A)
_VoltageIndexDescr_Type=OctetString
_VoltageIndexDescr_Object=MibTableColumn
voltageIndexDescr=_VoltageIndexDescr_Object((1,3,6,1,4,1,3807,1,8012,1,7,2,1,9),_VoltageIndexDescr_Type())
voltageIndexDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:voltageIndexDescr.setStatus(_A)
_VoltageTrap_ObjectIdentity=ObjectIdentity
voltageTrap=_VoltageTrap_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,1,7,3))
voltageOk=NotificationType((1,3,6,1,4,1,3807,1,8012,1,7,3,1))
voltageOk.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:voltageOk.setStatus(_A)
voltageFault=NotificationType((1,3,6,1,4,1,3807,1,8012,1,7,3,2))
voltageFault.setObjects(*((_B,_I),(_B,_J),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:voltageFault.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_F:DisplayString,'mspp':mspp,'msppChassis':msppChassis,'msppVoltage':msppVoltage,'voltageGeneral':voltageGeneral,'voltageTrapEnable':voltageTrapEnable,'voltageMonitorEnable':voltageMonitorEnable,'voltageNumber':voltageNumber,'voltageTable':voltageTable,'voltageEntry':voltageEntry,_K:voltageIndex,_I:voltageDescr,_L:voltageLThreshold,_M:voltageHThreshold,_J:voltageValue,'voltageState':voltageState,'voltageTrapEna':voltageTrapEna,'voltageAllSetting':voltageAllSetting,'voltageIndexDescr':voltageIndexDescr,'voltageTrap':voltageTrap,'voltageOk':voltageOk,'voltageFault':voltageFault})