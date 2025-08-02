_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechApMgmtMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,124))
if mibBuilder.loadTexts:qtechApMgmtMIB.setRevisions(('2013-07-23 00:00',))
_QtechApMgmtMIBObjects_ObjectIdentity=ObjectIdentity
qtechApMgmtMIBObjects=_QtechApMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,124,1))
_QtechApMgmt_ObjectIdentity=ObjectIdentity
qtechApMgmt=_QtechApMgmt_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,124,1,1))
class _QtechApMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechApMode_Type.__name__=_A
_QtechApMode_Object=MibScalar
qtechApMode=_QtechApMode_Object((1,3,6,1,4,1,27514,1,1,10,2,124,1,1,1),_QtechApMode_Type())
qtechApMode.setMaxAccess('read-only')
if mibBuilder.loadTexts:qtechApMode.setStatus('current')
mibBuilder.exportSymbols('QTECH-AP-MGMT-MIB',**{'qtechApMgmtMIB':qtechApMgmtMIB,'qtechApMgmtMIBObjects':qtechApMgmtMIBObjects,'qtechApMgmt':qtechApMgmt,'qtechApMode':qtechApMode})