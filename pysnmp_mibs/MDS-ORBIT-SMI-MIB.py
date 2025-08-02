_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mdsRoot,=mibBuilder.importSymbols('MDS-REG-MIB','mdsRoot')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mdsOrbit=ModuleIdentity((1,3,6,1,4,1,4130,10))
if mibBuilder.loadTexts:mdsOrbit.setRevisions(('2013-04-22 00:00',))
_MdsSystem_ObjectIdentity=ObjectIdentity
mdsSystem=_MdsSystem_ObjectIdentity((1,3,6,1,4,1,4130,10,1))
if mibBuilder.loadTexts:mdsSystem.setStatus(_A)
_MdsInterfaces_ObjectIdentity=ObjectIdentity
mdsInterfaces=_MdsInterfaces_ObjectIdentity((1,3,6,1,4,1,4130,10,2))
if mibBuilder.loadTexts:mdsInterfaces.setStatus(_A)
_MdsServices_ObjectIdentity=ObjectIdentity
mdsServices=_MdsServices_ObjectIdentity((1,3,6,1,4,1,4130,10,3))
if mibBuilder.loadTexts:mdsServices.setStatus(_A)
_MdsLogging_ObjectIdentity=ObjectIdentity
mdsLogging=_MdsLogging_ObjectIdentity((1,3,6,1,4,1,4130,10,4))
if mibBuilder.loadTexts:mdsLogging.setStatus(_A)
mibBuilder.exportSymbols('MDS-ORBIT-SMI-MIB',**{'mdsOrbit':mdsOrbit,'mdsSystem':mdsSystem,'mdsInterfaces':mdsInterfaces,'mdsServices':mdsServices,'mdsLogging':mdsLogging})