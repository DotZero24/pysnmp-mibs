_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfPPPoEServer=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,102))
if mibBuilder.loadTexts:hpnicfPPPoEServer.setRevisions(('2009-05-06 00:00',))
_HpnicfPPPoEServerObject_ObjectIdentity=ObjectIdentity
hpnicfPPPoEServerObject=_HpnicfPPPoEServerObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,102,1))
_HpnicfPPPoEServerMaxSessions_Type=Integer32
_HpnicfPPPoEServerMaxSessions_Object=MibScalar
hpnicfPPPoEServerMaxSessions=_HpnicfPPPoEServerMaxSessions_Object((1,3,6,1,4,1,11,2,14,11,15,2,102,1,1),_HpnicfPPPoEServerMaxSessions_Type())
hpnicfPPPoEServerMaxSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPPPoEServerMaxSessions.setStatus(_A)
_HpnicfPPPoEServerCurrSessions_Type=Integer32
_HpnicfPPPoEServerCurrSessions_Object=MibScalar
hpnicfPPPoEServerCurrSessions=_HpnicfPPPoEServerCurrSessions_Object((1,3,6,1,4,1,11,2,14,11,15,2,102,1,2),_HpnicfPPPoEServerCurrSessions_Type())
hpnicfPPPoEServerCurrSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPPPoEServerCurrSessions.setStatus(_A)
_HpnicfPPPoEServerAuthRequests_Type=Counter32
_HpnicfPPPoEServerAuthRequests_Object=MibScalar
hpnicfPPPoEServerAuthRequests=_HpnicfPPPoEServerAuthRequests_Object((1,3,6,1,4,1,11,2,14,11,15,2,102,1,3),_HpnicfPPPoEServerAuthRequests_Type())
hpnicfPPPoEServerAuthRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPPPoEServerAuthRequests.setStatus(_A)
_HpnicfPPPoEServerAuthSuccesses_Type=Counter32
_HpnicfPPPoEServerAuthSuccesses_Object=MibScalar
hpnicfPPPoEServerAuthSuccesses=_HpnicfPPPoEServerAuthSuccesses_Object((1,3,6,1,4,1,11,2,14,11,15,2,102,1,4),_HpnicfPPPoEServerAuthSuccesses_Type())
hpnicfPPPoEServerAuthSuccesses.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPPPoEServerAuthSuccesses.setStatus(_A)
_HpnicfPPPoEServerAuthFailures_Type=Counter32
_HpnicfPPPoEServerAuthFailures_Object=MibScalar
hpnicfPPPoEServerAuthFailures=_HpnicfPPPoEServerAuthFailures_Object((1,3,6,1,4,1,11,2,14,11,15,2,102,1,5),_HpnicfPPPoEServerAuthFailures_Type())
hpnicfPPPoEServerAuthFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPPPoEServerAuthFailures.setStatus(_A)
class _HpnicfPPPoESAbnormOffsThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfPPPoESAbnormOffsThreshold_Type.__name__=_C
_HpnicfPPPoESAbnormOffsThreshold_Object=MibScalar
hpnicfPPPoESAbnormOffsThreshold=_HpnicfPPPoESAbnormOffsThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,102,1,6),_HpnicfPPPoESAbnormOffsThreshold_Type())
hpnicfPPPoESAbnormOffsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPPPoESAbnormOffsThreshold.setStatus(_A)
class _HpnicfPPPoESAbnormOffPerThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfPPPoESAbnormOffPerThreshold_Type.__name__=_C
_HpnicfPPPoESAbnormOffPerThreshold_Object=MibScalar
hpnicfPPPoESAbnormOffPerThreshold=_HpnicfPPPoESAbnormOffPerThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,102,1,7),_HpnicfPPPoESAbnormOffPerThreshold_Type())
hpnicfPPPoESAbnormOffPerThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPPPoESAbnormOffPerThreshold.setStatus(_A)
class _HpnicfPPPoESNormOffPerThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfPPPoESNormOffPerThreshold_Type.__name__=_C
_HpnicfPPPoESNormOffPerThreshold_Object=MibScalar
hpnicfPPPoESNormOffPerThreshold=_HpnicfPPPoESNormOffPerThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,102,1,8),_HpnicfPPPoESNormOffPerThreshold_Type())
hpnicfPPPoESNormOffPerThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPPPoESNormOffPerThreshold.setStatus(_A)
_HpnicfPPPoEServerTraps_ObjectIdentity=ObjectIdentity
hpnicfPPPoEServerTraps=_HpnicfPPPoEServerTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,102,2))
_HpnicfPPPoeServerTrapPrefix_ObjectIdentity=ObjectIdentity
hpnicfPPPoeServerTrapPrefix=_HpnicfPPPoeServerTrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,102,2,0))
hpnicfPPPoESAbnormOffsAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,102,2,0,1))
if mibBuilder.loadTexts:hpnicfPPPoESAbnormOffsAlarm.setStatus(_A)
hpnicfPPPoESAbnormOffPerAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,102,2,0,2))
if mibBuilder.loadTexts:hpnicfPPPoESAbnormOffPerAlarm.setStatus(_A)
hpnicfPPPoESNormOffPerAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,102,2,0,3))
if mibBuilder.loadTexts:hpnicfPPPoESNormOffPerAlarm.setStatus(_A)
mibBuilder.exportSymbols('HPN-ICF-PPPOE-SERVER-MIB',**{'hpnicfPPPoEServer':hpnicfPPPoEServer,'hpnicfPPPoEServerObject':hpnicfPPPoEServerObject,'hpnicfPPPoEServerMaxSessions':hpnicfPPPoEServerMaxSessions,'hpnicfPPPoEServerCurrSessions':hpnicfPPPoEServerCurrSessions,'hpnicfPPPoEServerAuthRequests':hpnicfPPPoEServerAuthRequests,'hpnicfPPPoEServerAuthSuccesses':hpnicfPPPoEServerAuthSuccesses,'hpnicfPPPoEServerAuthFailures':hpnicfPPPoEServerAuthFailures,'hpnicfPPPoESAbnormOffsThreshold':hpnicfPPPoESAbnormOffsThreshold,'hpnicfPPPoESAbnormOffPerThreshold':hpnicfPPPoESAbnormOffPerThreshold,'hpnicfPPPoESNormOffPerThreshold':hpnicfPPPoESNormOffPerThreshold,'hpnicfPPPoEServerTraps':hpnicfPPPoEServerTraps,'hpnicfPPPoeServerTrapPrefix':hpnicfPPPoeServerTrapPrefix,'hpnicfPPPoESAbnormOffsAlarm':hpnicfPPPoESAbnormOffsAlarm,'hpnicfPPPoESAbnormOffPerAlarm':hpnicfPPPoESAbnormOffPerAlarm,'hpnicfPPPoESNormOffPerAlarm':hpnicfPPPoESNormOffPerAlarm})