_A='TruthValue'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_A)
eltMesIssPppoeMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,2))
if mibBuilder.loadTexts:eltMesIssPppoeMIB.setRevisions(('2018-11-22 00:00',))
_EltMesIssPppoeObjects_ObjectIdentity=ObjectIdentity
eltMesIssPppoeObjects=_EltMesIssPppoeObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,2,1))
_EltMesIssPppoeGlobals_ObjectIdentity=ObjectIdentity
eltMesIssPppoeGlobals=_EltMesIssPppoeGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,2,1,1))
class _EltMesIssPppoePassthroughEnabled_Type(TruthValue):defaultValue=2
_EltMesIssPppoePassthroughEnabled_Type.__name__=_A
_EltMesIssPppoePassthroughEnabled_Object=MibScalar
eltMesIssPppoePassthroughEnabled=_EltMesIssPppoePassthroughEnabled_Object((1,3,6,1,4,1,35265,1,139,2,1,1,1),_EltMesIssPppoePassthroughEnabled_Type())
eltMesIssPppoePassthroughEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:eltMesIssPppoePassthroughEnabled.setStatus('current')
mibBuilder.exportSymbols('ELTEX-MES-ISS-PPPOE-MIB',**{'eltMesIssPppoeMIB':eltMesIssPppoeMIB,'eltMesIssPppoeObjects':eltMesIssPppoeObjects,'eltMesIssPppoeGlobals':eltMesIssPppoeGlobals,'eltMesIssPppoePassthroughEnabled':eltMesIssPppoePassthroughEnabled})