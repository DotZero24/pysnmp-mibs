_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cPPPoEServer=ModuleIdentity((1,3,6,1,4,1,2011,10,2,102))
if mibBuilder.loadTexts:h3cPPPoEServer.setRevisions(('2009-05-06 00:00',))
_H3cPPPoEServerObject_ObjectIdentity=ObjectIdentity
h3cPPPoEServerObject=_H3cPPPoEServerObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,102,1))
_H3cPPPoEServerMaxSessions_Type=Integer32
_H3cPPPoEServerMaxSessions_Object=MibScalar
h3cPPPoEServerMaxSessions=_H3cPPPoEServerMaxSessions_Object((1,3,6,1,4,1,2011,10,2,102,1,1),_H3cPPPoEServerMaxSessions_Type())
h3cPPPoEServerMaxSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPPPoEServerMaxSessions.setStatus(_A)
_H3cPPPoEServerCurrSessions_Type=Integer32
_H3cPPPoEServerCurrSessions_Object=MibScalar
h3cPPPoEServerCurrSessions=_H3cPPPoEServerCurrSessions_Object((1,3,6,1,4,1,2011,10,2,102,1,2),_H3cPPPoEServerCurrSessions_Type())
h3cPPPoEServerCurrSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPPPoEServerCurrSessions.setStatus(_A)
_H3cPPPoEServerAuthRequests_Type=Counter32
_H3cPPPoEServerAuthRequests_Object=MibScalar
h3cPPPoEServerAuthRequests=_H3cPPPoEServerAuthRequests_Object((1,3,6,1,4,1,2011,10,2,102,1,3),_H3cPPPoEServerAuthRequests_Type())
h3cPPPoEServerAuthRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPPPoEServerAuthRequests.setStatus(_A)
_H3cPPPoEServerAuthSuccesses_Type=Counter32
_H3cPPPoEServerAuthSuccesses_Object=MibScalar
h3cPPPoEServerAuthSuccesses=_H3cPPPoEServerAuthSuccesses_Object((1,3,6,1,4,1,2011,10,2,102,1,4),_H3cPPPoEServerAuthSuccesses_Type())
h3cPPPoEServerAuthSuccesses.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPPPoEServerAuthSuccesses.setStatus(_A)
_H3cPPPoEServerAuthFailures_Type=Counter32
_H3cPPPoEServerAuthFailures_Object=MibScalar
h3cPPPoEServerAuthFailures=_H3cPPPoEServerAuthFailures_Object((1,3,6,1,4,1,2011,10,2,102,1,5),_H3cPPPoEServerAuthFailures_Type())
h3cPPPoEServerAuthFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPPPoEServerAuthFailures.setStatus(_A)
class _H3cPPPoESAbnormOffsThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cPPPoESAbnormOffsThreshold_Type.__name__=_C
_H3cPPPoESAbnormOffsThreshold_Object=MibScalar
h3cPPPoESAbnormOffsThreshold=_H3cPPPoESAbnormOffsThreshold_Object((1,3,6,1,4,1,2011,10,2,102,1,6),_H3cPPPoESAbnormOffsThreshold_Type())
h3cPPPoESAbnormOffsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPPPoESAbnormOffsThreshold.setStatus(_A)
class _H3cPPPoESAbnormOffPerThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cPPPoESAbnormOffPerThreshold_Type.__name__=_C
_H3cPPPoESAbnormOffPerThreshold_Object=MibScalar
h3cPPPoESAbnormOffPerThreshold=_H3cPPPoESAbnormOffPerThreshold_Object((1,3,6,1,4,1,2011,10,2,102,1,7),_H3cPPPoESAbnormOffPerThreshold_Type())
h3cPPPoESAbnormOffPerThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPPPoESAbnormOffPerThreshold.setStatus(_A)
class _H3cPPPoESNormOffPerThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cPPPoESNormOffPerThreshold_Type.__name__=_C
_H3cPPPoESNormOffPerThreshold_Object=MibScalar
h3cPPPoESNormOffPerThreshold=_H3cPPPoESNormOffPerThreshold_Object((1,3,6,1,4,1,2011,10,2,102,1,8),_H3cPPPoESNormOffPerThreshold_Type())
h3cPPPoESNormOffPerThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPPPoESNormOffPerThreshold.setStatus(_A)
_H3cPPPoEServerTraps_ObjectIdentity=ObjectIdentity
h3cPPPoEServerTraps=_H3cPPPoEServerTraps_ObjectIdentity((1,3,6,1,4,1,2011,10,2,102,2))
_H3cPPPoeServerTrapPrefix_ObjectIdentity=ObjectIdentity
h3cPPPoeServerTrapPrefix=_H3cPPPoeServerTrapPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,102,2,0))
h3cPPPoESAbnormOffsAlarm=NotificationType((1,3,6,1,4,1,2011,10,2,102,2,0,1))
if mibBuilder.loadTexts:h3cPPPoESAbnormOffsAlarm.setStatus(_A)
h3cPPPoESAbnormOffPerAlarm=NotificationType((1,3,6,1,4,1,2011,10,2,102,2,0,2))
if mibBuilder.loadTexts:h3cPPPoESAbnormOffPerAlarm.setStatus(_A)
h3cPPPoESNormOffPerAlarm=NotificationType((1,3,6,1,4,1,2011,10,2,102,2,0,3))
if mibBuilder.loadTexts:h3cPPPoESNormOffPerAlarm.setStatus(_A)
mibBuilder.exportSymbols('H3C-PPPOE-SERVER-MIB',**{'h3cPPPoEServer':h3cPPPoEServer,'h3cPPPoEServerObject':h3cPPPoEServerObject,'h3cPPPoEServerMaxSessions':h3cPPPoEServerMaxSessions,'h3cPPPoEServerCurrSessions':h3cPPPoEServerCurrSessions,'h3cPPPoEServerAuthRequests':h3cPPPoEServerAuthRequests,'h3cPPPoEServerAuthSuccesses':h3cPPPoEServerAuthSuccesses,'h3cPPPoEServerAuthFailures':h3cPPPoEServerAuthFailures,'h3cPPPoESAbnormOffsThreshold':h3cPPPoESAbnormOffsThreshold,'h3cPPPoESAbnormOffPerThreshold':h3cPPPoESAbnormOffPerThreshold,'h3cPPPoESNormOffPerThreshold':h3cPPPoESNormOffPerThreshold,'h3cPPPoEServerTraps':h3cPPPoEServerTraps,'h3cPPPoeServerTrapPrefix':h3cPPPoeServerTrapPrefix,'h3cPPPoESAbnormOffsAlarm':h3cPPPoESAbnormOffsAlarm,'h3cPPPoESAbnormOffPerAlarm':h3cPPPoESAbnormOffPerAlarm,'h3cPPPoESNormOffPerAlarm':h3cPPPoESNormOffPerAlarm})