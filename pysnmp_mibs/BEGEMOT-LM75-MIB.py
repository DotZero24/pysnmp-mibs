_D='lm75SensorIndex'
_C='BEGEMOT-LM75-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
begemot,=mibBuilder.importSymbols('BEGEMOT-MIB','begemot')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
begemotLm75=ModuleIdentity((1,3,6,1,4,1,12325,1,400))
if mibBuilder.loadTexts:begemotLm75.setRevisions(('2018-10-24 00:00','2014-02-24 00:00'))
_BegemotLm75Objects_ObjectIdentity=ObjectIdentity
begemotLm75Objects=_BegemotLm75Objects_ObjectIdentity((1,3,6,1,4,1,12325,1,400,1))
_Lm75Sensor_ObjectIdentity=ObjectIdentity
lm75Sensor=_Lm75Sensor_ObjectIdentity((1,3,6,1,4,1,12325,1,400,1,1))
_Lm75Sensors_Type=Integer32
_Lm75Sensors_Object=MibScalar
lm75Sensors=_Lm75Sensors_Object((1,3,6,1,4,1,12325,1,400,1,1,1),_Lm75Sensors_Type())
lm75Sensors.setMaxAccess(_B)
if mibBuilder.loadTexts:lm75Sensors.setStatus(_A)
_Lm75SensorTable_Object=MibTable
lm75SensorTable=_Lm75SensorTable_Object((1,3,6,1,4,1,12325,1,400,1,2))
if mibBuilder.loadTexts:lm75SensorTable.setStatus(_A)
_Lm75SensorEntry_Object=MibTableRow
lm75SensorEntry=_Lm75SensorEntry_Object((1,3,6,1,4,1,12325,1,400,1,2,1))
lm75SensorEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:lm75SensorEntry.setStatus(_A)
_Lm75SensorIndex_Type=Integer32
_Lm75SensorIndex_Object=MibTableColumn
lm75SensorIndex=_Lm75SensorIndex_Object((1,3,6,1,4,1,12325,1,400,1,2,1,1),_Lm75SensorIndex_Type())
lm75SensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lm75SensorIndex.setStatus(_A)
_Lm75SensorSysctlIndex_Type=Integer32
_Lm75SensorSysctlIndex_Object=MibTableColumn
lm75SensorSysctlIndex=_Lm75SensorSysctlIndex_Object((1,3,6,1,4,1,12325,1,400,1,2,1,2),_Lm75SensorSysctlIndex_Type())
lm75SensorSysctlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lm75SensorSysctlIndex.setStatus(_A)
_Lm75SensorDesc_Type=OctetString
_Lm75SensorDesc_Object=MibTableColumn
lm75SensorDesc=_Lm75SensorDesc_Object((1,3,6,1,4,1,12325,1,400,1,2,1,3),_Lm75SensorDesc_Type())
lm75SensorDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:lm75SensorDesc.setStatus(_A)
_Lm75SensorLocation_Type=OctetString
_Lm75SensorLocation_Object=MibTableColumn
lm75SensorLocation=_Lm75SensorLocation_Object((1,3,6,1,4,1,12325,1,400,1,2,1,4),_Lm75SensorLocation_Type())
lm75SensorLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:lm75SensorLocation.setStatus(_A)
_Lm75SensorPnpInfo_Type=OctetString
_Lm75SensorPnpInfo_Object=MibTableColumn
lm75SensorPnpInfo=_Lm75SensorPnpInfo_Object((1,3,6,1,4,1,12325,1,400,1,2,1,5),_Lm75SensorPnpInfo_Type())
lm75SensorPnpInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:lm75SensorPnpInfo.setStatus(_A)
_Lm75SensorParent_Type=OctetString
_Lm75SensorParent_Object=MibTableColumn
lm75SensorParent=_Lm75SensorParent_Object((1,3,6,1,4,1,12325,1,400,1,2,1,6),_Lm75SensorParent_Type())
lm75SensorParent.setMaxAccess(_B)
if mibBuilder.loadTexts:lm75SensorParent.setStatus(_A)
_Lm75SensorTemperature_Type=Integer32
_Lm75SensorTemperature_Object=MibTableColumn
lm75SensorTemperature=_Lm75SensorTemperature_Object((1,3,6,1,4,1,12325,1,400,1,2,1,7),_Lm75SensorTemperature_Type())
lm75SensorTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:lm75SensorTemperature.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'begemotLm75':begemotLm75,'begemotLm75Objects':begemotLm75Objects,'lm75Sensor':lm75Sensor,'lm75Sensors':lm75Sensors,'lm75SensorTable':lm75SensorTable,'lm75SensorEntry':lm75SensorEntry,_D:lm75SensorIndex,'lm75SensorSysctlIndex':lm75SensorSysctlIndex,'lm75SensorDesc':lm75SensorDesc,'lm75SensorLocation':lm75SensorLocation,'lm75SensorPnpInfo':lm75SensorPnpInfo,'lm75SensorParent':lm75SensorParent,'lm75SensorTemperature':lm75SensorTemperature})