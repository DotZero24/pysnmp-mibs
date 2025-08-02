if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adIdentityShared,adShared=mibBuilder.importSymbols('ADTRAN-MIB','adIdentityShared','adShared')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adDS3Identity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,74))
if mibBuilder.loadTexts:adDS3Identity.setRevisions(('2008-04-24 00:00',))
_AdDS3_ObjectIdentity=ObjectIdentity
adDS3=_AdDS3_ObjectIdentity((1,3,6,1,4,1,664,5,74))
_AdGenDS3Test_ObjectIdentity=ObjectIdentity
adGenDS3Test=_AdGenDS3Test_ObjectIdentity((1,3,6,1,4,1,664,5,74,1))
_AdGenDS3TestID_ObjectIdentity=ObjectIdentity
adGenDS3TestID=_AdGenDS3TestID_ObjectIdentity((1,3,6,1,4,1,664,6,10000,74,1))
mibBuilder.exportSymbols('ADTRAN-SHARED-DS3-MIB',**{'adDS3':adDS3,'adGenDS3Test':adGenDS3Test,'adDS3Identity':adDS3Identity,'adGenDS3TestID':adGenDS3TestID})