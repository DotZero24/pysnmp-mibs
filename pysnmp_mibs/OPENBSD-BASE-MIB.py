if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
openBSD=ModuleIdentity((1,3,6,1,4,1,30155))
if mibBuilder.loadTexts:openBSD.setRevisions(('2012-01-31 00:00','2008-12-23 00:00'))
_PfMIBObjects_ObjectIdentity=ObjectIdentity
pfMIBObjects=_PfMIBObjects_ObjectIdentity((1,3,6,1,4,1,30155,1))
_SensorsMIBObjects_ObjectIdentity=ObjectIdentity
sensorsMIBObjects=_SensorsMIBObjects_ObjectIdentity((1,3,6,1,4,1,30155,2))
_RelaydMIBObjects_ObjectIdentity=ObjectIdentity
relaydMIBObjects=_RelaydMIBObjects_ObjectIdentity((1,3,6,1,4,1,30155,3))
_MemMIBObjects_ObjectIdentity=ObjectIdentity
memMIBObjects=_MemMIBObjects_ObjectIdentity((1,3,6,1,4,1,30155,5))
_CarpMIBObjects_ObjectIdentity=ObjectIdentity
carpMIBObjects=_CarpMIBObjects_ObjectIdentity((1,3,6,1,4,1,30155,6))
_LocalSystem_ObjectIdentity=ObjectIdentity
localSystem=_LocalSystem_ObjectIdentity((1,3,6,1,4,1,30155,23))
_OpenBSDDefaultObjectID_ObjectIdentity=ObjectIdentity
openBSDDefaultObjectID=_OpenBSDDefaultObjectID_ObjectIdentity((1,3,6,1,4,1,30155,23,1))
_LocalTest_ObjectIdentity=ObjectIdentity
localTest=_LocalTest_ObjectIdentity((1,3,6,1,4,1,30155,42))
mibBuilder.exportSymbols('OPENBSD-BASE-MIB',**{'openBSD':openBSD,'pfMIBObjects':pfMIBObjects,'sensorsMIBObjects':sensorsMIBObjects,'relaydMIBObjects':relaydMIBObjects,'memMIBObjects':memMIBObjects,'carpMIBObjects':carpMIBObjects,'localSystem':localSystem,'openBSDDefaultObjectID':openBSDDefaultObjectID,'localTest':localTest})