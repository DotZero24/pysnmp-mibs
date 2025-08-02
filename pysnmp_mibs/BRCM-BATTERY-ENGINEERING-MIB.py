_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataEngineering,=mibBuilder.importSymbols('BRCM-CABLEDATA-ENGINEERING-MIB','cableDataEngineering')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
PositiveInteger,=mibBuilder.importSymbols('UPS-MIB','PositiveInteger')
batteryEngineering=ModuleIdentity((1,3,6,1,4,1,4413,2,99,1,1,3,10))
if mibBuilder.loadTexts:batteryEngineering.setRevisions(('2009-06-10 00:00',))
_BatteryEngrBase_ObjectIdentity=ObjectIdentity
batteryEngrBase=_BatteryEngrBase_ObjectIdentity((1,3,6,1,4,1,4413,2,99,1,1,3,10,1))
class _BattSimulatePowerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('utility',1),('battery',2)))
_BattSimulatePowerSource_Type.__name__=_A
_BattSimulatePowerSource_Object=MibScalar
battSimulatePowerSource=_BattSimulatePowerSource_Object((1,3,6,1,4,1,4413,2,99,1,1,3,10,1,1),_BattSimulatePowerSource_Type())
battSimulatePowerSource.setMaxAccess('read-write')
if mibBuilder.loadTexts:battSimulatePowerSource.setStatus('current')
mibBuilder.exportSymbols('BRCM-BATTERY-ENGINEERING-MIB',**{'batteryEngineering':batteryEngineering,'batteryEngrBase':batteryEngrBase,'battSimulatePowerSource':battSimulatePowerSource})