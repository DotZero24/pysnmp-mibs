_H='lmMiscSensorsIndex'
_G='lmVoltSensorsIndex'
_F='lmFanSensorsIndex'
_E='lmTempSensorsIndex'
_D='LM-SENSORS-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ucdExperimental,=mibBuilder.importSymbols('UCD-SNMP-MIB','ucdExperimental')
lmSensorsMIB=ModuleIdentity((1,3,6,1,4,1,2021,13,16,1))
if mibBuilder.loadTexts:lmSensorsMIB.setRevisions(('2000-11-05 00:00',))
_LmSensors_ObjectIdentity=ObjectIdentity
lmSensors=_LmSensors_ObjectIdentity((1,3,6,1,4,1,2021,13,16))
_LmTempSensorsTable_Object=MibTable
lmTempSensorsTable=_LmTempSensorsTable_Object((1,3,6,1,4,1,2021,13,16,2))
if mibBuilder.loadTexts:lmTempSensorsTable.setStatus(_A)
_LmTempSensorsEntry_Object=MibTableRow
lmTempSensorsEntry=_LmTempSensorsEntry_Object((1,3,6,1,4,1,2021,13,16,2,1))
lmTempSensorsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:lmTempSensorsEntry.setStatus(_A)
class _LmTempSensorsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LmTempSensorsIndex_Type.__name__=_C
_LmTempSensorsIndex_Object=MibTableColumn
lmTempSensorsIndex=_LmTempSensorsIndex_Object((1,3,6,1,4,1,2021,13,16,2,1,1),_LmTempSensorsIndex_Type())
lmTempSensorsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lmTempSensorsIndex.setStatus(_A)
_LmTempSensorsDevice_Type=DisplayString
_LmTempSensorsDevice_Object=MibTableColumn
lmTempSensorsDevice=_LmTempSensorsDevice_Object((1,3,6,1,4,1,2021,13,16,2,1,2),_LmTempSensorsDevice_Type())
lmTempSensorsDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:lmTempSensorsDevice.setStatus(_A)
_LmTempSensorsValue_Type=Gauge32
_LmTempSensorsValue_Object=MibTableColumn
lmTempSensorsValue=_LmTempSensorsValue_Object((1,3,6,1,4,1,2021,13,16,2,1,3),_LmTempSensorsValue_Type())
lmTempSensorsValue.setMaxAccess(_B)
if mibBuilder.loadTexts:lmTempSensorsValue.setStatus(_A)
_LmFanSensorsTable_Object=MibTable
lmFanSensorsTable=_LmFanSensorsTable_Object((1,3,6,1,4,1,2021,13,16,3))
if mibBuilder.loadTexts:lmFanSensorsTable.setStatus(_A)
_LmFanSensorsEntry_Object=MibTableRow
lmFanSensorsEntry=_LmFanSensorsEntry_Object((1,3,6,1,4,1,2021,13,16,3,1))
lmFanSensorsEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:lmFanSensorsEntry.setStatus(_A)
class _LmFanSensorsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LmFanSensorsIndex_Type.__name__=_C
_LmFanSensorsIndex_Object=MibTableColumn
lmFanSensorsIndex=_LmFanSensorsIndex_Object((1,3,6,1,4,1,2021,13,16,3,1,1),_LmFanSensorsIndex_Type())
lmFanSensorsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lmFanSensorsIndex.setStatus(_A)
_LmFanSensorsDevice_Type=DisplayString
_LmFanSensorsDevice_Object=MibTableColumn
lmFanSensorsDevice=_LmFanSensorsDevice_Object((1,3,6,1,4,1,2021,13,16,3,1,2),_LmFanSensorsDevice_Type())
lmFanSensorsDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:lmFanSensorsDevice.setStatus(_A)
_LmFanSensorsValue_Type=Gauge32
_LmFanSensorsValue_Object=MibTableColumn
lmFanSensorsValue=_LmFanSensorsValue_Object((1,3,6,1,4,1,2021,13,16,3,1,3),_LmFanSensorsValue_Type())
lmFanSensorsValue.setMaxAccess(_B)
if mibBuilder.loadTexts:lmFanSensorsValue.setStatus(_A)
_LmVoltSensorsTable_Object=MibTable
lmVoltSensorsTable=_LmVoltSensorsTable_Object((1,3,6,1,4,1,2021,13,16,4))
if mibBuilder.loadTexts:lmVoltSensorsTable.setStatus(_A)
_LmVoltSensorsEntry_Object=MibTableRow
lmVoltSensorsEntry=_LmVoltSensorsEntry_Object((1,3,6,1,4,1,2021,13,16,4,1))
lmVoltSensorsEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:lmVoltSensorsEntry.setStatus(_A)
class _LmVoltSensorsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LmVoltSensorsIndex_Type.__name__=_C
_LmVoltSensorsIndex_Object=MibTableColumn
lmVoltSensorsIndex=_LmVoltSensorsIndex_Object((1,3,6,1,4,1,2021,13,16,4,1,1),_LmVoltSensorsIndex_Type())
lmVoltSensorsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lmVoltSensorsIndex.setStatus(_A)
_LmVoltSensorsDevice_Type=DisplayString
_LmVoltSensorsDevice_Object=MibTableColumn
lmVoltSensorsDevice=_LmVoltSensorsDevice_Object((1,3,6,1,4,1,2021,13,16,4,1,2),_LmVoltSensorsDevice_Type())
lmVoltSensorsDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:lmVoltSensorsDevice.setStatus(_A)
_LmVoltSensorsValue_Type=Gauge32
_LmVoltSensorsValue_Object=MibTableColumn
lmVoltSensorsValue=_LmVoltSensorsValue_Object((1,3,6,1,4,1,2021,13,16,4,1,3),_LmVoltSensorsValue_Type())
lmVoltSensorsValue.setMaxAccess(_B)
if mibBuilder.loadTexts:lmVoltSensorsValue.setStatus(_A)
_LmMiscSensorsTable_Object=MibTable
lmMiscSensorsTable=_LmMiscSensorsTable_Object((1,3,6,1,4,1,2021,13,16,5))
if mibBuilder.loadTexts:lmMiscSensorsTable.setStatus(_A)
_LmMiscSensorsEntry_Object=MibTableRow
lmMiscSensorsEntry=_LmMiscSensorsEntry_Object((1,3,6,1,4,1,2021,13,16,5,1))
lmMiscSensorsEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:lmMiscSensorsEntry.setStatus(_A)
class _LmMiscSensorsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LmMiscSensorsIndex_Type.__name__=_C
_LmMiscSensorsIndex_Object=MibTableColumn
lmMiscSensorsIndex=_LmMiscSensorsIndex_Object((1,3,6,1,4,1,2021,13,16,5,1,1),_LmMiscSensorsIndex_Type())
lmMiscSensorsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lmMiscSensorsIndex.setStatus(_A)
_LmMiscSensorsDevice_Type=DisplayString
_LmMiscSensorsDevice_Object=MibTableColumn
lmMiscSensorsDevice=_LmMiscSensorsDevice_Object((1,3,6,1,4,1,2021,13,16,5,1,2),_LmMiscSensorsDevice_Type())
lmMiscSensorsDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:lmMiscSensorsDevice.setStatus(_A)
_LmMiscSensorsValue_Type=Gauge32
_LmMiscSensorsValue_Object=MibTableColumn
lmMiscSensorsValue=_LmMiscSensorsValue_Object((1,3,6,1,4,1,2021,13,16,5,1,3),_LmMiscSensorsValue_Type())
lmMiscSensorsValue.setMaxAccess(_B)
if mibBuilder.loadTexts:lmMiscSensorsValue.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'lmSensors':lmSensors,'lmSensorsMIB':lmSensorsMIB,'lmTempSensorsTable':lmTempSensorsTable,'lmTempSensorsEntry':lmTempSensorsEntry,_E:lmTempSensorsIndex,'lmTempSensorsDevice':lmTempSensorsDevice,'lmTempSensorsValue':lmTempSensorsValue,'lmFanSensorsTable':lmFanSensorsTable,'lmFanSensorsEntry':lmFanSensorsEntry,_F:lmFanSensorsIndex,'lmFanSensorsDevice':lmFanSensorsDevice,'lmFanSensorsValue':lmFanSensorsValue,'lmVoltSensorsTable':lmVoltSensorsTable,'lmVoltSensorsEntry':lmVoltSensorsEntry,_G:lmVoltSensorsIndex,'lmVoltSensorsDevice':lmVoltSensorsDevice,'lmVoltSensorsValue':lmVoltSensorsValue,'lmMiscSensorsTable':lmMiscSensorsTable,'lmMiscSensorsEntry':lmMiscSensorsEntry,_H:lmMiscSensorsIndex,'lmMiscSensorsDevice':lmMiscSensorsDevice,'lmMiscSensorsValue':lmMiscSensorsValue})