_I='zxDslUapsSwapReason'
_H='zxDslUapsPortOperStatus'
_G='zxDslUapsPortWorkingStatus'
_F='Bits'
_E='ZTE-DSL-UAPS-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_F,'Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
zxDslUapsMib=ModuleIdentity((1,3,6,1,4,1,3902,1004,33))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxDsl_ObjectIdentity=ObjectIdentity
zxDsl=_ZxDsl_ObjectIdentity((1,3,6,1,4,1,3902,1004))
_ZxDslUapsObjects_ObjectIdentity=ObjectIdentity
zxDslUapsObjects=_ZxDslUapsObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,33,1))
class _ZxDslUapsPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('uaps',1),('trunk',2),('uplink',3)))
_ZxDslUapsPortMode_Type.__name__=_B
_ZxDslUapsPortMode_Object=MibScalar
zxDslUapsPortMode=_ZxDslUapsPortMode_Object((1,3,6,1,4,1,3902,1004,33,1,1),_ZxDslUapsPortMode_Type())
zxDslUapsPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslUapsPortMode.setStatus(_A)
_ZxDslUapsPrimaryPort_Type=Integer32
_ZxDslUapsPrimaryPort_Object=MibScalar
zxDslUapsPrimaryPort=_ZxDslUapsPrimaryPort_Object((1,3,6,1,4,1,3902,1004,33,1,2),_ZxDslUapsPrimaryPort_Type())
zxDslUapsPrimaryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslUapsPrimaryPort.setStatus(_A)
_ZxDslUapsAutoFailbackEnable_Type=Integer32
_ZxDslUapsAutoFailbackEnable_Object=MibScalar
zxDslUapsAutoFailbackEnable=_ZxDslUapsAutoFailbackEnable_Object((1,3,6,1,4,1,3902,1004,33,1,3),_ZxDslUapsAutoFailbackEnable_Type())
zxDslUapsAutoFailbackEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslUapsAutoFailbackEnable.setStatus(_A)
class _ZxDslUapsProtectionTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,900))
_ZxDslUapsProtectionTime_Type.__name__=_B
_ZxDslUapsProtectionTime_Object=MibScalar
zxDslUapsProtectionTime=_ZxDslUapsProtectionTime_Object((1,3,6,1,4,1,3902,1004,33,1,4),_ZxDslUapsProtectionTime_Type())
zxDslUapsProtectionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslUapsProtectionTime.setStatus(_A)
if mibBuilder.loadTexts:zxDslUapsProtectionTime.setUnits('second')
_ZxDslUapsForceSwap_Type=Integer32
_ZxDslUapsForceSwap_Object=MibScalar
zxDslUapsForceSwap=_ZxDslUapsForceSwap_Object((1,3,6,1,4,1,3902,1004,33,1,5),_ZxDslUapsForceSwap_Type())
zxDslUapsForceSwap.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslUapsForceSwap.setStatus(_A)
class _ZxDslUapsPortWorkingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primaryPortInWorking',1),('secondaryPortInWorking',2)))
_ZxDslUapsPortWorkingStatus_Type.__name__=_B
_ZxDslUapsPortWorkingStatus_Object=MibScalar
zxDslUapsPortWorkingStatus=_ZxDslUapsPortWorkingStatus_Object((1,3,6,1,4,1,3902,1004,33,1,6),_ZxDslUapsPortWorkingStatus_Type())
zxDslUapsPortWorkingStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslUapsPortWorkingStatus.setStatus(_A)
class _ZxDslUapsPortOperStatus_Type(Bits):namedValues=NamedValues(*(('primaryPort',0),('secondaryPort',1)))
_ZxDslUapsPortOperStatus_Type.__name__=_F
_ZxDslUapsPortOperStatus_Object=MibScalar
zxDslUapsPortOperStatus=_ZxDslUapsPortOperStatus_Object((1,3,6,1,4,1,3902,1004,33,1,7),_ZxDslUapsPortOperStatus_Type())
zxDslUapsPortOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslUapsPortOperStatus.setStatus(_A)
_ZxDslUapsIsInPrtctTime_Type=TruthValue
_ZxDslUapsIsInPrtctTime_Object=MibScalar
zxDslUapsIsInPrtctTime=_ZxDslUapsIsInPrtctTime_Object((1,3,6,1,4,1,3902,1004,33,1,8),_ZxDslUapsIsInPrtctTime_Type())
zxDslUapsIsInPrtctTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslUapsIsInPrtctTime.setStatus(_A)
class _ZxDslUapsSwapRequestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('existRequest',1),('noRequest',2)))
_ZxDslUapsSwapRequestStatus_Type.__name__=_B
_ZxDslUapsSwapRequestStatus_Object=MibScalar
zxDslUapsSwapRequestStatus=_ZxDslUapsSwapRequestStatus_Object((1,3,6,1,4,1,3902,1004,33,1,9),_ZxDslUapsSwapRequestStatus_Type())
zxDslUapsSwapRequestStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslUapsSwapRequestStatus.setStatus(_A)
class _ZxDslUapsSwapReason_Type(Bits):namedValues=NamedValues(*(('failback',0),('failover',1),('forceSwap',2)))
_ZxDslUapsSwapReason_Type.__name__=_F
_ZxDslUapsSwapReason_Object=MibScalar
zxDslUapsSwapReason=_ZxDslUapsSwapReason_Object((1,3,6,1,4,1,3902,1004,33,1,10),_ZxDslUapsSwapReason_Type())
zxDslUapsSwapReason.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslUapsSwapReason.setStatus(_A)
_ZxDslUapsTraps_ObjectIdentity=ObjectIdentity
zxDslUapsTraps=_ZxDslUapsTraps_ObjectIdentity((1,3,6,1,4,1,3902,1004,33,2))
zxDslUapsSwappedTrap=NotificationType((1,3,6,1,4,1,3902,1004,33,2,1))
zxDslUapsSwappedTrap.setObjects(*((_E,_G),(_E,_H),(_E,_I)))
if mibBuilder.loadTexts:zxDslUapsSwappedTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zte':zte,'zxDsl':zxDsl,'zxDslUapsMib':zxDslUapsMib,'zxDslUapsObjects':zxDslUapsObjects,'zxDslUapsPortMode':zxDslUapsPortMode,'zxDslUapsPrimaryPort':zxDslUapsPrimaryPort,'zxDslUapsAutoFailbackEnable':zxDslUapsAutoFailbackEnable,'zxDslUapsProtectionTime':zxDslUapsProtectionTime,'zxDslUapsForceSwap':zxDslUapsForceSwap,_G:zxDslUapsPortWorkingStatus,_H:zxDslUapsPortOperStatus,'zxDslUapsIsInPrtctTime':zxDslUapsIsInPrtctTime,'zxDslUapsSwapRequestStatus':zxDslUapsSwapRequestStatus,_I:zxDslUapsSwapReason,'zxDslUapsTraps':zxDslUapsTraps,'zxDslUapsSwappedTrap':zxDslUapsSwappedTrap})