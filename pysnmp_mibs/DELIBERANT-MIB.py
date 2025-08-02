if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
deliberant=ModuleIdentity((1,3,6,1,4,1,32761))
if mibBuilder.loadTexts:deliberant.setRevisions(('2008-09-05 00:00',))
_DlbProducts_ObjectIdentity=ObjectIdentity
dlbProducts=_DlbProducts_ObjectIdentity((1,3,6,1,4,1,32761,1))
_DlbAdmin_ObjectIdentity=ObjectIdentity
dlbAdmin=_DlbAdmin_ObjectIdentity((1,3,6,1,4,1,32761,2))
_DlbMgmt_ObjectIdentity=ObjectIdentity
dlbMgmt=_DlbMgmt_ObjectIdentity((1,3,6,1,4,1,32761,3))
_DlbExperimental_ObjectIdentity=ObjectIdentity
dlbExperimental=_DlbExperimental_ObjectIdentity((1,3,6,1,4,1,32761,7))
mibBuilder.exportSymbols('DELIBERANT-MIB',**{'deliberant':deliberant,'dlbProducts':dlbProducts,'dlbAdmin':dlbAdmin,'dlbMgmt':dlbMgmt,'dlbExperimental':dlbExperimental})