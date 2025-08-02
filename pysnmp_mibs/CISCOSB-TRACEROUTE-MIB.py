_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rlTraceRoute=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,81))
if mibBuilder.loadTexts:rlTraceRoute.setRevisions(('2007-01-02 00:00',))
_RlTraceRouteMibVersion_Type=Integer32
_RlTraceRouteMibVersion_Object=MibScalar
rlTraceRouteMibVersion=_RlTraceRouteMibVersion_Object((1,3,6,1,4,1,9,6,1,101,81,1),_RlTraceRouteMibVersion_Type())
rlTraceRouteMibVersion.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlTraceRouteMibVersion.setStatus(_A)
_RlTraceRouteWebLastTestName_Type=Integer32
_RlTraceRouteWebLastTestName_Object=MibScalar
rlTraceRouteWebLastTestName=_RlTraceRouteWebLastTestName_Object((1,3,6,1,4,1,9,6,1,101,81,2),_RlTraceRouteWebLastTestName_Type())
rlTraceRouteWebLastTestName.setMaxAccess('read-write')
if mibBuilder.loadTexts:rlTraceRouteWebLastTestName.setStatus(_A)
mibBuilder.exportSymbols('CISCOSB-TRACEROUTE-MIB',**{'rlTraceRoute':rlTraceRoute,'rlTraceRouteMibVersion':rlTraceRouteMibVersion,'rlTraceRouteWebLastTestName':rlTraceRouteWebLastTestName})