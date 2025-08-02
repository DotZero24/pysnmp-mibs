_D='deprecated'
_C='current'
_B='Integer32'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
futuremld=ModuleIdentity((1,3,6,1,4,1,10876,101,1,70))
if mibBuilder.loadTexts:futuremld.setRevisions(('2012-09-05 00:00',))
_FsmldScalars_ObjectIdentity=ObjectIdentity
fsmldScalars=_FsmldScalars_ObjectIdentity((1,3,6,1,4,1,10876,101,1,70,1))
_FsmldNoOfCacheEntries_Type=Unsigned32
_FsmldNoOfCacheEntries_Object=MibScalar
fsmldNoOfCacheEntries=_FsmldNoOfCacheEntries_Object((1,3,6,1,4,1,10876,101,1,70,1,1),_FsmldNoOfCacheEntries_Type())
fsmldNoOfCacheEntries.setMaxAccess(_A)
if mibBuilder.loadTexts:fsmldNoOfCacheEntries.setStatus(_D)
_FsmldNoOfRoutingProtocols_Type=Unsigned32
_FsmldNoOfRoutingProtocols_Object=MibScalar
fsmldNoOfRoutingProtocols=_FsmldNoOfRoutingProtocols_Object((1,3,6,1,4,1,10876,101,1,70,1,2),_FsmldNoOfRoutingProtocols_Type())
fsmldNoOfRoutingProtocols.setMaxAccess(_A)
if mibBuilder.loadTexts:fsmldNoOfRoutingProtocols.setStatus(_D)
_FsmldTraceDebug_Type=Unsigned32
_FsmldTraceDebug_Object=MibScalar
fsmldTraceDebug=_FsmldTraceDebug_Object((1,3,6,1,4,1,10876,101,1,70,1,3),_FsmldTraceDebug_Type())
fsmldTraceDebug.setMaxAccess(_A)
if mibBuilder.loadTexts:fsmldTraceDebug.setStatus(_C)
class _FsmldMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mldrouter',1),('mldhost',2),('mldrouterhost',3)))
_FsmldMode_Type.__name__=_B
_FsmldMode_Object=MibScalar
fsmldMode=_FsmldMode_Object((1,3,6,1,4,1,10876,101,1,70,1,4),_FsmldMode_Type())
fsmldMode.setMaxAccess(_A)
if mibBuilder.loadTexts:fsmldMode.setStatus(_C)
class _FsmldProtocolUpDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mldinit',1),('mldshutdown',2)))
_FsmldProtocolUpDown_Type.__name__=_B
_FsmldProtocolUpDown_Object=MibScalar
fsmldProtocolUpDown=_FsmldProtocolUpDown_Object((1,3,6,1,4,1,10876,101,1,70,1,5),_FsmldProtocolUpDown_Type())
fsmldProtocolUpDown.setMaxAccess(_A)
if mibBuilder.loadTexts:fsmldProtocolUpDown.setStatus(_C)
mibBuilder.exportSymbols('SUPERMICRO-IPV6-MLD-MIB',**{'futuremld':futuremld,'fsmldScalars':fsmldScalars,'fsmldNoOfCacheEntries':fsmldNoOfCacheEntries,'fsmldNoOfRoutingProtocols':fsmldNoOfRoutingProtocols,'fsmldTraceDebug':fsmldTraceDebug,'fsmldMode':fsmldMode,'fsmldProtocolUpDown':fsmldProtocolUpDown})