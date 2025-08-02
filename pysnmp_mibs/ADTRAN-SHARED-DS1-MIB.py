if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adIdentityShared,adShared=mibBuilder.importSymbols('ADTRAN-MIB','adIdentityShared','adShared')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adDS1Identity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,78))
if mibBuilder.loadTexts:adDS1Identity.setRevisions(('2008-09-18 00:00',))
_AdDS1_ObjectIdentity=ObjectIdentity
adDS1=_AdDS1_ObjectIdentity((1,3,6,1,4,1,664,5,78))
_AdGenDS1Test_ObjectIdentity=ObjectIdentity
adGenDS1Test=_AdGenDS1Test_ObjectIdentity((1,3,6,1,4,1,664,5,78,1))
_AdGenDS1TestID_ObjectIdentity=ObjectIdentity
adGenDS1TestID=_AdGenDS1TestID_ObjectIdentity((1,3,6,1,4,1,664,6,10000,78,1))
mibBuilder.exportSymbols('ADTRAN-SHARED-DS1-MIB',**{'adDS1':adDS1,'adGenDS1Test':adGenDS1Test,'adDS1Identity':adDS1Identity,'adGenDS1TestID':adGenDS1TestID})