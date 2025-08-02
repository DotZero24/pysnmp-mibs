_L='voltageoverload'
_K='voltagelack'
_J='normal'
_I='powerIndex'
_H='disable'
_G='enable'
_F='powerState'
_E='read-write'
_D='WRI-POWER-MIB'
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
wri,wriProducts=mibBuilder.importSymbols('WRI-SMI','wri','wriProducts')
msppPower=ModuleIdentity((1,3,6,1,4,1,3807,1,8012,1,2))
if mibBuilder.loadTexts:msppPower.setRevisions(('2010-01-11 00:00','2009-01-11 00:00'))
_Mspp_ObjectIdentity=ObjectIdentity
mspp=_Mspp_ObjectIdentity((1,3,6,1,4,1,3807,1,8012))
_MsppChassis_ObjectIdentity=ObjectIdentity
msppChassis=_MsppChassis_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,1))
_PowerTable_Object=MibTable
powerTable=_PowerTable_Object((1,3,6,1,4,1,3807,1,8012,1,2,1))
if mibBuilder.loadTexts:powerTable.setStatus(_A)
_PowerEntry_Object=MibTableRow
powerEntry=_PowerEntry_Object((1,3,6,1,4,1,3807,1,8012,1,2,1,1))
powerEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:powerEntry.setStatus(_A)
_PowerIndex_Type=Unsigned32
_PowerIndex_Object=MibTableColumn
powerIndex=_PowerIndex_Object((1,3,6,1,4,1,3807,1,8012,1,2,1,1,1),_PowerIndex_Type())
powerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:powerIndex.setStatus(_A)
class _PowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dcdc',0),('acdc',1)))
_PowerType_Type.__name__=_C
_PowerType_Object=MibTableColumn
powerType=_PowerType_Object((1,3,6,1,4,1,3807,1,8012,1,2,1,1,2),_PowerType_Type())
powerType.setMaxAccess(_B)
if mibBuilder.loadTexts:powerType.setStatus(_A)
class _PowerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_PowerState_Type.__name__=_C
_PowerState_Object=MibTableColumn
powerState=_PowerState_Object((1,3,6,1,4,1,3807,1,8012,1,2,1,1,3),_PowerState_Type())
powerState.setMaxAccess(_B)
if mibBuilder.loadTexts:powerState.setStatus(_A)
_PowerValue_Type=Integer32
_PowerValue_Object=MibTableColumn
powerValue=_PowerValue_Object((1,3,6,1,4,1,3807,1,8012,1,2,1,1,4),_PowerValue_Type())
powerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:powerValue.setStatus(_A)
_PowerRole_Type=Integer32
_PowerRole_Object=MibTableColumn
powerRole=_PowerRole_Object((1,3,6,1,4,1,3807,1,8012,1,2,1,1,5),_PowerRole_Type())
powerRole.setMaxAccess(_E)
if mibBuilder.loadTexts:powerRole.setStatus(_A)
_PowerDescr_Type=OctetString
_PowerDescr_Object=MibTableColumn
powerDescr=_PowerDescr_Object((1,3,6,1,4,1,3807,1,8012,1,2,1,1,6),_PowerDescr_Type())
powerDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:powerDescr.setStatus(_A)
_PowerSerial_Type=OctetString
_PowerSerial_Object=MibTableColumn
powerSerial=_PowerSerial_Object((1,3,6,1,4,1,3807,1,8012,1,2,1,1,7),_PowerSerial_Type())
powerSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:powerSerial.setStatus(_A)
_PowerTemperature_Type=Integer32
_PowerTemperature_Object=MibTableColumn
powerTemperature=_PowerTemperature_Object((1,3,6,1,4,1,3807,1,8012,1,2,1,1,8),_PowerTemperature_Type())
powerTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:powerTemperature.setStatus(_A)
_PowerFuseStatus_Type=Integer32
_PowerFuseStatus_Object=MibTableColumn
powerFuseStatus=_PowerFuseStatus_Object((1,3,6,1,4,1,3807,1,8012,1,2,1,1,9),_PowerFuseStatus_Type())
powerFuseStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:powerFuseStatus.setStatus(_A)
class _PowerStateBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_PowerStateBits_Type.__name__=_C
_PowerStateBits_Object=MibTableColumn
powerStateBits=_PowerStateBits_Object((1,3,6,1,4,1,3807,1,8012,1,2,1,1,10),_PowerStateBits_Type())
powerStateBits.setMaxAccess(_B)
if mibBuilder.loadTexts:powerStateBits.setStatus(_A)
class _PowerTrapEna_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_PowerTrapEna_Type.__name__=_C
_PowerTrapEna_Object=MibTableColumn
powerTrapEna=_PowerTrapEna_Object((1,3,6,1,4,1,3807,1,8012,1,2,1,1,11),_PowerTrapEna_Type())
powerTrapEna.setMaxAccess(_E)
if mibBuilder.loadTexts:powerTrapEna.setStatus(_A)
_PowerAllSetting_Type=OctetString
_PowerAllSetting_Object=MibTableColumn
powerAllSetting=_PowerAllSetting_Object((1,3,6,1,4,1,3807,1,8012,1,2,1,1,12),_PowerAllSetting_Type())
powerAllSetting.setMaxAccess(_E)
if mibBuilder.loadTexts:powerAllSetting.setStatus(_A)
_PowerIndexDescr_Type=OctetString
_PowerIndexDescr_Object=MibTableColumn
powerIndexDescr=_PowerIndexDescr_Object((1,3,6,1,4,1,3807,1,8012,1,2,1,1,13),_PowerIndexDescr_Type())
powerIndexDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:powerIndexDescr.setStatus(_A)
_PowerTrap_ObjectIdentity=ObjectIdentity
powerTrap=_PowerTrap_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,1,2,2))
_PowerGeneral_ObjectIdentity=ObjectIdentity
powerGeneral=_PowerGeneral_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,1,2,3))
_PowerBits_Type=Counter32
_PowerBits_Object=MibScalar
powerBits=_PowerBits_Object((1,3,6,1,4,1,3807,1,8012,1,2,3,1),_PowerBits_Type())
powerBits.setMaxAccess(_B)
if mibBuilder.loadTexts:powerBits.setStatus(_A)
_PowerNum_Type=Integer32
_PowerNum_Object=MibScalar
powerNum=_PowerNum_Object((1,3,6,1,4,1,3807,1,8012,1,2,3,2),_PowerNum_Type())
powerNum.setMaxAccess(_B)
if mibBuilder.loadTexts:powerNum.setStatus(_A)
class _PowerTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_PowerTrapEnable_Type.__name__=_C
_PowerTrapEnable_Object=MibScalar
powerTrapEnable=_PowerTrapEnable_Object((1,3,6,1,4,1,3807,1,8012,1,2,3,3),_PowerTrapEnable_Type())
powerTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:powerTrapEnable.setStatus(_A)
class _PowerMonitorEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_PowerMonitorEnable_Type.__name__=_C
_PowerMonitorEnable_Object=MibScalar
powerMonitorEnable=_PowerMonitorEnable_Object((1,3,6,1,4,1,3807,1,8012,1,2,3,4),_PowerMonitorEnable_Type())
powerMonitorEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:powerMonitorEnable.setStatus(_A)
powerUp=NotificationType((1,3,6,1,4,1,3807,1,8012,1,2,2,1))
powerUp.setObjects((_D,_F))
if mibBuilder.loadTexts:powerUp.setStatus(_A)
powerDown=NotificationType((1,3,6,1,4,1,3807,1,8012,1,2,2,2))
powerDown.setObjects((_D,_F))
if mibBuilder.loadTexts:powerDown.setStatus(_A)
powerFault=NotificationType((1,3,6,1,4,1,3807,1,8012,1,2,2,3))
powerFault.setObjects((_D,_F))
if mibBuilder.loadTexts:powerFault.setStatus(_A)
powerOk=NotificationType((1,3,6,1,4,1,3807,1,8012,1,2,2,4))
powerOk.setObjects((_D,_F))
if mibBuilder.loadTexts:powerOk.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'mspp':mspp,'msppChassis':msppChassis,'msppPower':msppPower,'powerTable':powerTable,'powerEntry':powerEntry,_I:powerIndex,'powerType':powerType,_F:powerState,'powerValue':powerValue,'powerRole':powerRole,'powerDescr':powerDescr,'powerSerial':powerSerial,'powerTemperature':powerTemperature,'powerFuseStatus':powerFuseStatus,'powerStateBits':powerStateBits,'powerTrapEna':powerTrapEna,'powerAllSetting':powerAllSetting,'powerIndexDescr':powerIndexDescr,'powerTrap':powerTrap,'powerUp':powerUp,'powerDown':powerDown,'powerFault':powerFault,'powerOk':powerOk,'powerGeneral':powerGeneral,'powerBits':powerBits,'powerNum':powerNum,'powerTrapEnable':powerTrapEnable,'powerMonitorEnable':powerMonitorEnable})