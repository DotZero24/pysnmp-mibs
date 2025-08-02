if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adIdentityShared,adShared=mibBuilder.importSymbols('ADTRAN-MIB','adIdentityShared','adShared')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adVdsl2Identity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,65))
if mibBuilder.loadTexts:adVdsl2Identity.setRevisions(('2008-07-08 00:00',))
_AdVdsl2_ObjectIdentity=ObjectIdentity
adVdsl2=_AdVdsl2_ObjectIdentity((1,3,6,1,4,1,664,5,65))
_AdGenVdsl2_ObjectIdentity=ObjectIdentity
adGenVdsl2=_AdGenVdsl2_ObjectIdentity((1,3,6,1,4,1,664,5,65,1))
_AdGenVdsl2ID_ObjectIdentity=ObjectIdentity
adGenVdsl2ID=_AdGenVdsl2ID_ObjectIdentity((1,3,6,1,4,1,664,6,10000,65,1))
mibBuilder.exportSymbols('ADTRAN-SHARED-VDSL2-MIB',**{'adVdsl2':adVdsl2,'adGenVdsl2':adGenVdsl2,'adVdsl2Identity':adVdsl2Identity,'adGenVdsl2ID':adGenVdsl2ID})