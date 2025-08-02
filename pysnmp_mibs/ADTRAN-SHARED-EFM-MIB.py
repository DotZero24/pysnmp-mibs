if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adIdentityShared,adShared=mibBuilder.importSymbols('ADTRAN-MIB','adIdentityShared','adShared')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adEfmIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,66))
if mibBuilder.loadTexts:adEfmIdentity.setRevisions(('2007-04-05 00:00',))
_AdEfm_ObjectIdentity=ObjectIdentity
adEfm=_AdEfm_ObjectIdentity((1,3,6,1,4,1,664,5,66))
_AdGenEfm_ObjectIdentity=ObjectIdentity
adGenEfm=_AdGenEfm_ObjectIdentity((1,3,6,1,4,1,664,5,66,1))
_AdGenEfmNtu_ObjectIdentity=ObjectIdentity
adGenEfmNtu=_AdGenEfmNtu_ObjectIdentity((1,3,6,1,4,1,664,5,66,2))
_AdGenEfmExt_ObjectIdentity=ObjectIdentity
adGenEfmExt=_AdGenEfmExt_ObjectIdentity((1,3,6,1,4,1,664,5,66,3))
_AdGenEfmID_ObjectIdentity=ObjectIdentity
adGenEfmID=_AdGenEfmID_ObjectIdentity((1,3,6,1,4,1,664,6,10000,66,1))
_AdGenEfmNtuID_ObjectIdentity=ObjectIdentity
adGenEfmNtuID=_AdGenEfmNtuID_ObjectIdentity((1,3,6,1,4,1,664,6,10000,66,2))
_AdGenEfmExtID_ObjectIdentity=ObjectIdentity
adGenEfmExtID=_AdGenEfmExtID_ObjectIdentity((1,3,6,1,4,1,664,6,10000,66,3))
mibBuilder.exportSymbols('ADTRAN-SHARED-EFM-MIB',**{'adEfm':adEfm,'adGenEfm':adGenEfm,'adGenEfmNtu':adGenEfmNtu,'adGenEfmExt':adGenEfmExt,'adEfmIdentity':adEfmIdentity,'adGenEfmID':adGenEfmID,'adGenEfmNtuID':adGenEfmNtuID,'adGenEfmExtID':adGenEfmExtID})