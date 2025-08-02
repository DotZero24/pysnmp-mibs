_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
gbnL3,=mibBuilder.importSymbols('QTECH-MASTER-MIB','gbnL3')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
gbnL3RouteCommon=ModuleIdentity((1,3,6,1,4,1,27514,1,2,5,2))
if mibBuilder.loadTexts:gbnL3RouteCommon.setRevisions(('1901-05-10 20:04',))
_RouterId_ObjectIdentity=ObjectIdentity
routerId=_RouterId_ObjectIdentity((1,3,6,1,4,1,27514,1,2,5,2,1))
_RouterIdConfig_Type=TruthValue
_RouterIdConfig_Object=MibScalar
routerIdConfig=_RouterIdConfig_Object((1,3,6,1,4,1,27514,1,2,5,2,1,1),_RouterIdConfig_Type())
routerIdConfig.setMaxAccess('read-only')
if mibBuilder.loadTexts:routerIdConfig.setStatus(_A)
_RouterIdValue_Type=IpAddress
_RouterIdValue_Object=MibScalar
routerIdValue=_RouterIdValue_Object((1,3,6,1,4,1,27514,1,2,5,2,1,2),_RouterIdValue_Type())
routerIdValue.setMaxAccess('read-write')
if mibBuilder.loadTexts:routerIdValue.setStatus(_A)
mibBuilder.exportSymbols('QTECH-GBNL3RouteCommon-MIB',**{'gbnL3RouteCommon':gbnL3RouteCommon,'routerId':routerId,'routerIdConfig':routerIdConfig,'routerIdValue':routerIdValue})