_H='raisecomPowerStatus'
_G='raisecomPowerVoltValue'
_F='raisecomPowerVoltReference'
_E='Integer32'
_D='read-only'
_C='raisecomPowerIndex'
_B='RAISECOM-POWERMONITOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
raisecomPowerMonitor=ModuleIdentity((1,3,6,1,4,1,8886,1,24))
_RaisecomPowerMonitorNotification_ObjectIdentity=ObjectIdentity
raisecomPowerMonitorNotification=_RaisecomPowerMonitorNotification_ObjectIdentity((1,3,6,1,4,1,8886,1,24,1))
_RaisecomPowerMonitorMibObjects_ObjectIdentity=ObjectIdentity
raisecomPowerMonitorMibObjects=_RaisecomPowerMonitorMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,24,2))
_RaisecomPowerMonitorStateTable_Object=MibTable
raisecomPowerMonitorStateTable=_RaisecomPowerMonitorStateTable_Object((1,3,6,1,4,1,8886,1,24,2,1))
if mibBuilder.loadTexts:raisecomPowerMonitorStateTable.setStatus(_A)
_RaisecomPowerMonitorStateEntry_Object=MibTableRow
raisecomPowerMonitorStateEntry=_RaisecomPowerMonitorStateEntry_Object((1,3,6,1,4,1,8886,1,24,2,1,1))
raisecomPowerMonitorStateEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:raisecomPowerMonitorStateEntry.setStatus(_A)
_RaisecomPowerIndex_Type=Unsigned32
_RaisecomPowerIndex_Object=MibTableColumn
raisecomPowerIndex=_RaisecomPowerIndex_Object((1,3,6,1,4,1,8886,1,24,2,1,1,1),_RaisecomPowerIndex_Type())
raisecomPowerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:raisecomPowerIndex.setStatus(_A)
_RaisecomPowerSerialNumber_Type=OctetString
_RaisecomPowerSerialNumber_Object=MibTableColumn
raisecomPowerSerialNumber=_RaisecomPowerSerialNumber_Object((1,3,6,1,4,1,8886,1,24,2,1,1,2),_RaisecomPowerSerialNumber_Type())
raisecomPowerSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPowerSerialNumber.setStatus(_A)
class _RaisecomPowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ac',1),('dc',2)))
_RaisecomPowerType_Type.__name__=_E
_RaisecomPowerType_Object=MibTableColumn
raisecomPowerType=_RaisecomPowerType_Object((1,3,6,1,4,1,8886,1,24,2,1,1,3),_RaisecomPowerType_Type())
raisecomPowerType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPowerType.setStatus(_A)
_RaisecomPowerVoltReference_Type=Integer32
_RaisecomPowerVoltReference_Object=MibTableColumn
raisecomPowerVoltReference=_RaisecomPowerVoltReference_Object((1,3,6,1,4,1,8886,1,24,2,1,1,4),_RaisecomPowerVoltReference_Type())
raisecomPowerVoltReference.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPowerVoltReference.setStatus(_A)
_RaisecomPowerVoltValue_Type=Integer32
_RaisecomPowerVoltValue_Object=MibTableColumn
raisecomPowerVoltValue=_RaisecomPowerVoltValue_Object((1,3,6,1,4,1,8886,1,24,2,1,1,5),_RaisecomPowerVoltValue_Type())
raisecomPowerVoltValue.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPowerVoltValue.setStatus(_A)
class _RaisecomPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('power-on',1),('power-off',2)))
_RaisecomPowerStatus_Type.__name__=_E
_RaisecomPowerStatus_Object=MibTableColumn
raisecomPowerStatus=_RaisecomPowerStatus_Object((1,3,6,1,4,1,8886,1,24,2,1,1,6),_RaisecomPowerStatus_Type())
raisecomPowerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPowerStatus.setStatus(_A)
raisecomPowerVoltNormal=NotificationType((1,3,6,1,4,1,8886,1,24,1,1))
raisecomPowerVoltNormal.setObjects(*((_B,_C),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:raisecomPowerVoltNormal.setStatus(_A)
raisecomPowerVoltAbnormal=NotificationType((1,3,6,1,4,1,8886,1,24,1,2))
raisecomPowerVoltAbnormal.setObjects(*((_B,_C),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:raisecomPowerVoltAbnormal.setStatus(_A)
raisecomPowerStatusTrap=NotificationType((1,3,6,1,4,1,8886,1,24,1,3))
raisecomPowerStatusTrap.setObjects(*((_B,_C),(_B,_H)))
if mibBuilder.loadTexts:raisecomPowerStatusTrap.setStatus(_A)
raisecomDyingGaspTrap=NotificationType((1,3,6,1,4,1,8886,1,24,1,4))
if mibBuilder.loadTexts:raisecomDyingGaspTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'raisecomPowerMonitor':raisecomPowerMonitor,'raisecomPowerMonitorNotification':raisecomPowerMonitorNotification,'raisecomPowerVoltNormal':raisecomPowerVoltNormal,'raisecomPowerVoltAbnormal':raisecomPowerVoltAbnormal,'raisecomPowerStatusTrap':raisecomPowerStatusTrap,'raisecomDyingGaspTrap':raisecomDyingGaspTrap,'raisecomPowerMonitorMibObjects':raisecomPowerMonitorMibObjects,'raisecomPowerMonitorStateTable':raisecomPowerMonitorStateTable,'raisecomPowerMonitorStateEntry':raisecomPowerMonitorStateEntry,_C:raisecomPowerIndex,'raisecomPowerSerialNumber':raisecomPowerSerialNumber,'raisecomPowerType':raisecomPowerType,_F:raisecomPowerVoltReference,_G:raisecomPowerVoltValue,_H:raisecomPowerStatus})