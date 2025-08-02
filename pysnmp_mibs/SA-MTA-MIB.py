_G='read-only'
_F='milliseconds'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
saMta=ModuleIdentity((1,3,6,1,4,1,1429,78,3))
if mibBuilder.loadTexts:saMta.setRevisions(('2016-11-10 00:00',))
_Sa_ObjectIdentity=ObjectIdentity
sa=_Sa_ObjectIdentity((1,3,6,1,4,1,1429))
_SaVoip_ObjectIdentity=ObjectIdentity
saVoip=_SaVoip_ObjectIdentity((1,3,6,1,4,1,1429,78))
_SaMtaDevice_ObjectIdentity=ObjectIdentity
saMtaDevice=_SaMtaDevice_ObjectIdentity((1,3,6,1,4,1,1429,78,3,1))
class _SaMtaDevOffHookWarnTOBusy_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_SaMtaDevOffHookWarnTOBusy_Type.__name__=_B
_SaMtaDevOffHookWarnTOBusy_Object=MibScalar
saMtaDevOffHookWarnTOBusy=_SaMtaDevOffHookWarnTOBusy_Object((1,3,6,1,4,1,1429,78,3,1,61),_SaMtaDevOffHookWarnTOBusy_Type())
saMtaDevOffHookWarnTOBusy.setMaxAccess(_C)
if mibBuilder.loadTexts:saMtaDevOffHookWarnTOBusy.setStatus(_A)
_SaMtaEndPointTable_Object=MibTable
saMtaEndPointTable=_SaMtaEndPointTable_Object((1,3,6,1,4,1,1429,78,3,2))
if mibBuilder.loadTexts:saMtaEndPointTable.setStatus(_A)
_SaMtaEndPointEntry_Object=MibTableRow
saMtaEndPointEntry=_SaMtaEndPointEntry_Object((1,3,6,1,4,1,1429,78,3,2,1))
saMtaEndPointEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:saMtaEndPointEntry.setStatus(_A)
class _SaMtaEndPntHookFlashMinTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(40,2000))
_SaMtaEndPntHookFlashMinTime_Type.__name__=_B
_SaMtaEndPntHookFlashMinTime_Object=MibTableColumn
saMtaEndPntHookFlashMinTime=_SaMtaEndPntHookFlashMinTime_Object((1,3,6,1,4,1,1429,78,3,2,1,1),_SaMtaEndPntHookFlashMinTime_Type())
saMtaEndPntHookFlashMinTime.setMaxAccess(_C)
if mibBuilder.loadTexts:saMtaEndPntHookFlashMinTime.setStatus(_A)
if mibBuilder.loadTexts:saMtaEndPntHookFlashMinTime.setUnits(_F)
class _SaMtaEndPntHookFlashMaxTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,2000))
_SaMtaEndPntHookFlashMaxTime_Type.__name__=_B
_SaMtaEndPntHookFlashMaxTime_Object=MibTableColumn
saMtaEndPntHookFlashMaxTime=_SaMtaEndPntHookFlashMaxTime_Object((1,3,6,1,4,1,1429,78,3,2,1,2),_SaMtaEndPntHookFlashMaxTime_Type())
saMtaEndPntHookFlashMaxTime.setMaxAccess(_C)
if mibBuilder.loadTexts:saMtaEndPntHookFlashMaxTime.setStatus(_A)
if mibBuilder.loadTexts:saMtaEndPntHookFlashMaxTime.setUnits(_F)
class _SaMtaEndPntStatePhysical_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('onHook',1),('offHook',2)))
_SaMtaEndPntStatePhysical_Type.__name__=_B
_SaMtaEndPntStatePhysical_Object=MibTableColumn
saMtaEndPntStatePhysical=_SaMtaEndPntStatePhysical_Object((1,3,6,1,4,1,1429,78,3,2,1,6),_SaMtaEndPntStatePhysical_Type())
saMtaEndPntStatePhysical.setMaxAccess(_G)
if mibBuilder.loadTexts:saMtaEndPntStatePhysical.setStatus(_A)
class _SaMtaEndPntStateLogical_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('connectedIdle',1),('disconnected',2),('inCallVoice',3),('inCallData',4)))
_SaMtaEndPntStateLogical_Type.__name__=_B
_SaMtaEndPntStateLogical_Object=MibTableColumn
saMtaEndPntStateLogical=_SaMtaEndPntStateLogical_Object((1,3,6,1,4,1,1429,78,3,2,1,7),_SaMtaEndPntStateLogical_Type())
saMtaEndPntStateLogical.setMaxAccess(_G)
if mibBuilder.loadTexts:saMtaEndPntStateLogical.setStatus(_A)
mibBuilder.exportSymbols('SA-MTA-MIB',**{'sa':sa,'saVoip':saVoip,'saMta':saMta,'saMtaDevice':saMtaDevice,'saMtaDevOffHookWarnTOBusy':saMtaDevOffHookWarnTOBusy,'saMtaEndPointTable':saMtaEndPointTable,'saMtaEndPointEntry':saMtaEndPointEntry,'saMtaEndPntHookFlashMinTime':saMtaEndPntHookFlashMinTime,'saMtaEndPntHookFlashMaxTime':saMtaEndPntHookFlashMaxTime,'saMtaEndPntStatePhysical':saMtaEndPntStatePhysical,'saMtaEndPntStateLogical':saMtaEndPntStateLogical})