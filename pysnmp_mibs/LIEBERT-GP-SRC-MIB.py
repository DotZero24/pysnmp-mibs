_I='degrees Celsius'
_H='degrees Fahrenheit'
_G='lgpSrcDevId'
_F='LIEBERT-GP-SRC-MIB'
_E='read-only'
_D='read-write'
_C='unknown'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lgpSrc,liebertSrcModuleReg=mibBuilder.importSymbols('LIEBERT-GP-REGISTRATION-MIB','lgpSrc','liebertSrcModuleReg')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysUpTime,=mibBuilder.importSymbols('SNMPv2-MIB','sysUpTime')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
liebertGlobalProductsSrcModule=ModuleIdentity((1,3,6,1,4,1,476,1,42,1,12,1))
if mibBuilder.loadTexts:liebertGlobalProductsSrcModule.setRevisions(('2017-11-10 00:00','2017-10-16 00:00','2017-08-18 00:00'))
_LgpSrcTable_Object=MibTable
lgpSrcTable=_LgpSrcTable_Object((1,3,6,1,4,1,476,1,42,3,10,1))
if mibBuilder.loadTexts:lgpSrcTable.setStatus(_A)
_LgpSrcEntry_Object=MibTableRow
lgpSrcEntry=_LgpSrcEntry_Object((1,3,6,1,4,1,476,1,42,3,10,1,1))
lgpSrcEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:lgpSrcEntry.setStatus(_A)
_LgpSrcDevId_Type=Unsigned32
_LgpSrcDevId_Object=MibTableColumn
lgpSrcDevId=_LgpSrcDevId_Object((1,3,6,1,4,1,476,1,42,3,10,1,1,1),_LgpSrcDevId_Type())
lgpSrcDevId.setMaxAccess(_E)
if mibBuilder.loadTexts:lgpSrcDevId.setStatus(_A)
_LgpSrcDevAddress_Type=Unsigned32
_LgpSrcDevAddress_Object=MibTableColumn
lgpSrcDevAddress=_LgpSrcDevAddress_Object((1,3,6,1,4,1,476,1,42,3,10,1,1,2),_LgpSrcDevAddress_Type())
lgpSrcDevAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:lgpSrcDevAddress.setStatus(_A)
class _LgpSrcDevState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('enabled',1),('standbyOffline',2),('unavailableOffline',3),('absent',4)))
_LgpSrcDevState_Type.__name__=_B
_LgpSrcDevState_Object=MibTableColumn
lgpSrcDevState=_LgpSrcDevState_Object((1,3,6,1,4,1,476,1,42,3,10,1,1,3),_LgpSrcDevState_Type())
lgpSrcDevState.setMaxAccess(_E)
if mibBuilder.loadTexts:lgpSrcDevState.setStatus(_A)
class _LgpSrcDevTemperatureDegF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2147483647));namedValues=NamedValues((_C,2147483647))
_LgpSrcDevTemperatureDegF_Type.__name__=_B
_LgpSrcDevTemperatureDegF_Object=MibTableColumn
lgpSrcDevTemperatureDegF=_LgpSrcDevTemperatureDegF_Object((1,3,6,1,4,1,476,1,42,3,10,1,1,4),_LgpSrcDevTemperatureDegF_Type())
lgpSrcDevTemperatureDegF.setMaxAccess(_E)
if mibBuilder.loadTexts:lgpSrcDevTemperatureDegF.setStatus(_A)
class _LgpSrcDevTemperatureSetpointDegF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2147483647));namedValues=NamedValues((_C,2147483647))
_LgpSrcDevTemperatureSetpointDegF_Type.__name__=_B
_LgpSrcDevTemperatureSetpointDegF_Object=MibTableColumn
lgpSrcDevTemperatureSetpointDegF=_LgpSrcDevTemperatureSetpointDegF_Object((1,3,6,1,4,1,476,1,42,3,10,1,1,5),_LgpSrcDevTemperatureSetpointDegF_Type())
lgpSrcDevTemperatureSetpointDegF.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpSrcDevTemperatureSetpointDegF.setStatus(_A)
class _LgpSrcDevTemperatureDegC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2147483647));namedValues=NamedValues((_C,2147483647))
_LgpSrcDevTemperatureDegC_Type.__name__=_B
_LgpSrcDevTemperatureDegC_Object=MibTableColumn
lgpSrcDevTemperatureDegC=_LgpSrcDevTemperatureDegC_Object((1,3,6,1,4,1,476,1,42,3,10,1,1,6),_LgpSrcDevTemperatureDegC_Type())
lgpSrcDevTemperatureDegC.setMaxAccess(_E)
if mibBuilder.loadTexts:lgpSrcDevTemperatureDegC.setStatus(_A)
class _LgpSrcDevTemperatureSetpointDegC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2147483647));namedValues=NamedValues((_C,2147483647))
_LgpSrcDevTemperatureSetpointDegC_Type.__name__=_B
_LgpSrcDevTemperatureSetpointDegC_Object=MibTableColumn
lgpSrcDevTemperatureSetpointDegC=_LgpSrcDevTemperatureSetpointDegC_Object((1,3,6,1,4,1,476,1,42,3,10,1,1,7),_LgpSrcDevTemperatureSetpointDegC_Type())
lgpSrcDevTemperatureSetpointDegC.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpSrcDevTemperatureSetpointDegC.setStatus(_A)
class _LgpSrcDevFanSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,2147483647)));namedValues=NamedValues(*(('low',1),('middle',2),('high',3),('auto',4),(_C,2147483647)))
_LgpSrcDevFanSpeed_Type.__name__=_B
_LgpSrcDevFanSpeed_Object=MibTableColumn
lgpSrcDevFanSpeed=_LgpSrcDevFanSpeed_Object((1,3,6,1,4,1,476,1,42,3,10,1,1,8),_LgpSrcDevFanSpeed_Type())
lgpSrcDevFanSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpSrcDevFanSpeed.setStatus(_A)
class _LgpSrcDevPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2147483647)));namedValues=NamedValues(*(('off',0),('on',1),(_C,2147483647)))
_LgpSrcDevPowerStatus_Type.__name__=_B
_LgpSrcDevPowerStatus_Object=MibTableColumn
lgpSrcDevPowerStatus=_LgpSrcDevPowerStatus_Object((1,3,6,1,4,1,476,1,42,3,10,1,1,9),_LgpSrcDevPowerStatus_Type())
lgpSrcDevPowerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpSrcDevPowerStatus.setStatus(_A)
class _LgpSrcDevOperatingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,2147483647)));namedValues=NamedValues(*(('cooling',0),('dehumidify',1),('fan',2),('ai',3),('heating',4),(_C,2147483647)))
_LgpSrcDevOperatingMode_Type.__name__=_B
_LgpSrcDevOperatingMode_Object=MibTableColumn
lgpSrcDevOperatingMode=_LgpSrcDevOperatingMode_Object((1,3,6,1,4,1,476,1,42,3,10,1,1,10),_LgpSrcDevOperatingMode_Type())
lgpSrcDevOperatingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpSrcDevOperatingMode.setStatus(_A)
class _LgpSrcDevTemperatureHighThresholdDegF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2147483647));namedValues=NamedValues((_C,2147483647))
_LgpSrcDevTemperatureHighThresholdDegF_Type.__name__=_B
_LgpSrcDevTemperatureHighThresholdDegF_Object=MibTableColumn
lgpSrcDevTemperatureHighThresholdDegF=_LgpSrcDevTemperatureHighThresholdDegF_Object((1,3,6,1,4,1,476,1,42,3,10,1,1,11),_LgpSrcDevTemperatureHighThresholdDegF_Type())
lgpSrcDevTemperatureHighThresholdDegF.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpSrcDevTemperatureHighThresholdDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpSrcDevTemperatureHighThresholdDegF.setUnits(_H)
class _LgpSrcDevTemperatureLowThresholdDegF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2147483647));namedValues=NamedValues((_C,2147483647))
_LgpSrcDevTemperatureLowThresholdDegF_Type.__name__=_B
_LgpSrcDevTemperatureLowThresholdDegF_Object=MibTableColumn
lgpSrcDevTemperatureLowThresholdDegF=_LgpSrcDevTemperatureLowThresholdDegF_Object((1,3,6,1,4,1,476,1,42,3,10,1,1,12),_LgpSrcDevTemperatureLowThresholdDegF_Type())
lgpSrcDevTemperatureLowThresholdDegF.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpSrcDevTemperatureLowThresholdDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpSrcDevTemperatureLowThresholdDegF.setUnits(_H)
class _LgpSrcDevTemperatureHighThresholdDegC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2147483647));namedValues=NamedValues((_C,2147483647))
_LgpSrcDevTemperatureHighThresholdDegC_Type.__name__=_B
_LgpSrcDevTemperatureHighThresholdDegC_Object=MibTableColumn
lgpSrcDevTemperatureHighThresholdDegC=_LgpSrcDevTemperatureHighThresholdDegC_Object((1,3,6,1,4,1,476,1,42,3,10,1,1,13),_LgpSrcDevTemperatureHighThresholdDegC_Type())
lgpSrcDevTemperatureHighThresholdDegC.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpSrcDevTemperatureHighThresholdDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpSrcDevTemperatureHighThresholdDegC.setUnits(_I)
class _LgpSrcDevTemperatureLowThresholdDegC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2147483647));namedValues=NamedValues((_C,2147483647))
_LgpSrcDevTemperatureLowThresholdDegC_Type.__name__=_B
_LgpSrcDevTemperatureLowThresholdDegC_Object=MibTableColumn
lgpSrcDevTemperatureLowThresholdDegC=_LgpSrcDevTemperatureLowThresholdDegC_Object((1,3,6,1,4,1,476,1,42,3,10,1,1,14),_LgpSrcDevTemperatureLowThresholdDegC_Type())
lgpSrcDevTemperatureLowThresholdDegC.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpSrcDevTemperatureLowThresholdDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpSrcDevTemperatureLowThresholdDegC.setUnits(_I)
mibBuilder.exportSymbols(_F,**{'liebertGlobalProductsSrcModule':liebertGlobalProductsSrcModule,'lgpSrcTable':lgpSrcTable,'lgpSrcEntry':lgpSrcEntry,_G:lgpSrcDevId,'lgpSrcDevAddress':lgpSrcDevAddress,'lgpSrcDevState':lgpSrcDevState,'lgpSrcDevTemperatureDegF':lgpSrcDevTemperatureDegF,'lgpSrcDevTemperatureSetpointDegF':lgpSrcDevTemperatureSetpointDegF,'lgpSrcDevTemperatureDegC':lgpSrcDevTemperatureDegC,'lgpSrcDevTemperatureSetpointDegC':lgpSrcDevTemperatureSetpointDegC,'lgpSrcDevFanSpeed':lgpSrcDevFanSpeed,'lgpSrcDevPowerStatus':lgpSrcDevPowerStatus,'lgpSrcDevOperatingMode':lgpSrcDevOperatingMode,'lgpSrcDevTemperatureHighThresholdDegF':lgpSrcDevTemperatureHighThresholdDegF,'lgpSrcDevTemperatureLowThresholdDegF':lgpSrcDevTemperatureLowThresholdDegF,'lgpSrcDevTemperatureHighThresholdDegC':lgpSrcDevTemperatureHighThresholdDegC,'lgpSrcDevTemperatureLowThresholdDegC':lgpSrcDevTemperatureLowThresholdDegC})