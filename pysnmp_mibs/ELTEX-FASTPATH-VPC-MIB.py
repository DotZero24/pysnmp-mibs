_A='TruthValue'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesFastpath,=mibBuilder.importSymbols('ELTEX-MES-FASTPATH-MIB','eltMesFastpath')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_A)
eltFastpathVpcMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,103,6))
if mibBuilder.loadTexts:eltFastpathVpcMIB.setRevisions(('2018-08-31 00:00',))
_EfpVpcObjects_ObjectIdentity=ObjectIdentity
efpVpcObjects=_EfpVpcObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,103,6,1))
_EfpVpcGlobals_ObjectIdentity=ObjectIdentity
efpVpcGlobals=_EfpVpcGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,103,6,1,1))
class _EfpVpcOrphanIsolationMode_Type(TruthValue):defaultValue=1
_EfpVpcOrphanIsolationMode_Type.__name__=_A
_EfpVpcOrphanIsolationMode_Object=MibScalar
efpVpcOrphanIsolationMode=_EfpVpcOrphanIsolationMode_Object((1,3,6,1,4,1,35265,1,103,6,1,1,1),_EfpVpcOrphanIsolationMode_Type())
efpVpcOrphanIsolationMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:efpVpcOrphanIsolationMode.setStatus('current')
_EfpVpcNotifications_ObjectIdentity=ObjectIdentity
efpVpcNotifications=_EfpVpcNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,103,6,2))
_EfpVpcNotificationsPrefix_ObjectIdentity=ObjectIdentity
efpVpcNotificationsPrefix=_EfpVpcNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,35265,1,103,6,2,0))
_EfpVpcConformance_ObjectIdentity=ObjectIdentity
efpVpcConformance=_EfpVpcConformance_ObjectIdentity((1,3,6,1,4,1,35265,1,103,6,3))
mibBuilder.exportSymbols('ELTEX-FASTPATH-VPC-MIB',**{'eltFastpathVpcMIB':eltFastpathVpcMIB,'efpVpcObjects':efpVpcObjects,'efpVpcGlobals':efpVpcGlobals,'efpVpcOrphanIsolationMode':efpVpcOrphanIsolationMode,'efpVpcNotifications':efpVpcNotifications,'efpVpcNotificationsPrefix':efpVpcNotificationsPrefix,'efpVpcConformance':efpVpcConformance})