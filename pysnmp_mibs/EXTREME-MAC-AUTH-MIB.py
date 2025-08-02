_D='read-write'
_C='extremeMacAuthClientAddress'
_B='EXTREME-MAC-AUTH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
extremeMacAuthMIB=ModuleIdentity((1,3,6,1,4,1,1916,1,44))
_ExtremeMacAuthObjects_ObjectIdentity=ObjectIdentity
extremeMacAuthObjects=_ExtremeMacAuthObjects_ObjectIdentity((1,3,6,1,4,1,1916,1,44,1))
_ExtremeMacAuthClientTable_Object=MibTable
extremeMacAuthClientTable=_ExtremeMacAuthClientTable_Object((1,3,6,1,4,1,1916,1,44,1,1))
if mibBuilder.loadTexts:extremeMacAuthClientTable.setStatus(_A)
_ExtremeMacAuthClientEntry_Object=MibTableRow
extremeMacAuthClientEntry=_ExtremeMacAuthClientEntry_Object((1,3,6,1,4,1,1916,1,44,1,1,1))
extremeMacAuthClientEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:extremeMacAuthClientEntry.setStatus(_A)
_ExtremeMacAuthClientAddress_Type=MacAddress
_ExtremeMacAuthClientAddress_Object=MibTableColumn
extremeMacAuthClientAddress=_ExtremeMacAuthClientAddress_Object((1,3,6,1,4,1,1916,1,44,1,1,1,1),_ExtremeMacAuthClientAddress_Type())
extremeMacAuthClientAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:extremeMacAuthClientAddress.setStatus(_A)
_ExtremeMacAuthClientInitialize_Type=TruthValue
_ExtremeMacAuthClientInitialize_Object=MibTableColumn
extremeMacAuthClientInitialize=_ExtremeMacAuthClientInitialize_Object((1,3,6,1,4,1,1916,1,44,1,1,1,2),_ExtremeMacAuthClientInitialize_Type())
extremeMacAuthClientInitialize.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMacAuthClientInitialize.setStatus(_A)
_ExtremeMacAuthClientReauthenticate_Type=TruthValue
_ExtremeMacAuthClientReauthenticate_Object=MibTableColumn
extremeMacAuthClientReauthenticate=_ExtremeMacAuthClientReauthenticate_Object((1,3,6,1,4,1,1916,1,44,1,1,1,3),_ExtremeMacAuthClientReauthenticate_Type())
extremeMacAuthClientReauthenticate.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMacAuthClientReauthenticate.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'extremeMacAuthMIB':extremeMacAuthMIB,'extremeMacAuthObjects':extremeMacAuthObjects,'extremeMacAuthClientTable':extremeMacAuthClientTable,'extremeMacAuthClientEntry':extremeMacAuthClientEntry,_C:extremeMacAuthClientAddress,'extremeMacAuthClientInitialize':extremeMacAuthClientInitialize,'extremeMacAuthClientReauthenticate':extremeMacAuthClientReauthenticate})