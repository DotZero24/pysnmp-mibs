if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adIdentityShared,adShared=mibBuilder.importSymbols('ADTRAN-MIB','adIdentityShared','adShared')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adAdsl2Identity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,82))
if mibBuilder.loadTexts:adAdsl2Identity.setRevisions(('2011-10-25 00:00',))
_AdAdsl2_ObjectIdentity=ObjectIdentity
adAdsl2=_AdAdsl2_ObjectIdentity((1,3,6,1,4,1,664,5,82))
_AdGenAdsl2_ObjectIdentity=ObjectIdentity
adGenAdsl2=_AdGenAdsl2_ObjectIdentity((1,3,6,1,4,1,664,5,82,1))
_AdGenAdsl2ID_ObjectIdentity=ObjectIdentity
adGenAdsl2ID=_AdGenAdsl2ID_ObjectIdentity((1,3,6,1,4,1,664,6,10000,82,1))
mibBuilder.exportSymbols('ADTRAN-SHARED-ADSL2-MIB',**{'adAdsl2':adAdsl2,'adGenAdsl2':adGenAdsl2,'adAdsl2Identity':adAdsl2Identity,'adGenAdsl2ID':adGenAdsl2ID})