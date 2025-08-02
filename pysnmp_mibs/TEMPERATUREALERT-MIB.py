_G='NotificationType'
_F='taLastCheck'
_E='taTemperature'
_D='taDeviceIndex'
_C='read-only'
_B='current'
_A='TEMPERATUREALERT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_G,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_G,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
taMIB=ModuleIdentity((1,3,6,1,4,1,27297))
if mibBuilder.loadTexts:taMIB.setRevisions(('1918-10-23 12:00','1906-10-31 12:00'))
_TaTraps_ObjectIdentity=ObjectIdentity
taTraps=_TaTraps_ObjectIdentity((1,3,6,1,4,1,27297,0))
_TaService_ObjectIdentity=ObjectIdentity
taService=_TaService_ObjectIdentity((1,3,6,1,4,1,27297,1))
_TaDeviceIndex_Type=DisplayString
_TaDeviceIndex_Object=MibScalar
taDeviceIndex=_TaDeviceIndex_Object((1,3,6,1,4,1,27297,1,1),_TaDeviceIndex_Type())
taDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:taDeviceIndex.setStatus(_B)
_TaTemperature_Type=DisplayString
_TaTemperature_Object=MibScalar
taTemperature=_TaTemperature_Object((1,3,6,1,4,1,27297,1,2),_TaTemperature_Type())
taTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:taTemperature.setStatus(_B)
_TaLastCheck_Type=DisplayString
_TaLastCheck_Object=MibScalar
taLastCheck=_TaLastCheck_Object((1,3,6,1,4,1,27297,1,3),_TaLastCheck_Type())
taLastCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:taLastCheck.setStatus(_B)
_TaWifi_ObjectIdentity=ObjectIdentity
taWifi=_TaWifi_ObjectIdentity((1,3,6,1,4,1,27297,2))
_TaTemperatureTable_ObjectIdentity=ObjectIdentity
taTemperatureTable=_TaTemperatureTable_ObjectIdentity((1,3,6,1,4,1,27297,2,7))
_TaTemperatureEntry_ObjectIdentity=ObjectIdentity
taTemperatureEntry=_TaTemperatureEntry_ObjectIdentity((1,3,6,1,4,1,27297,2,7,1))
_TaTemperaturePort_Type=DisplayString
_TaTemperaturePort_Object=MibScalar
taTemperaturePort=_TaTemperaturePort_Object((1,3,6,1,4,1,27297,2,7,1,7),_TaTemperaturePort_Type())
taTemperaturePort.setMaxAccess(_C)
if mibBuilder.loadTexts:taTemperaturePort.setStatus(_B)
taNormal=NotificationType((1,3,6,1,4,1,27297,0,1))
taNormal.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:taNormal.setStatus(_B)
taHighAlarm=NotificationType((1,3,6,1,4,1,27297,0,2))
taHighAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:taHighAlarm.setStatus(_B)
taLowAlarm=NotificationType((1,3,6,1,4,1,27297,0,3))
taLowAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:taLowAlarm.setStatus(_B)
taShutdown=NotificationType((1,3,6,1,4,1,27297,0,4))
if mibBuilder.loadTexts:taShutdown.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'taMIB':taMIB,'taTraps':taTraps,'taNormal':taNormal,'taHighAlarm':taHighAlarm,'taLowAlarm':taLowAlarm,'taShutdown':taShutdown,'taService':taService,_D:taDeviceIndex,_E:taTemperature,_F:taLastCheck,'taWifi':taWifi,'taTemperatureTable':taTemperatureTable,'taTemperatureEntry':taTemperatureEntry,'taTemperaturePort':taTemperaturePort})