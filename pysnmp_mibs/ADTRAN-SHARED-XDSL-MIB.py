if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adIdentityShared,adShared=mibBuilder.importSymbols('ADTRAN-MIB','adIdentityShared','adShared')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adXdslIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,73))
if mibBuilder.loadTexts:adXdslIdentity.setRevisions(('2010-06-10 00:00','2008-07-17 00:00'))
_AdXdsl_ObjectIdentity=ObjectIdentity
adXdsl=_AdXdsl_ObjectIdentity((1,3,6,1,4,1,664,5,73))
_AdGenXdsl_ObjectIdentity=ObjectIdentity
adGenXdsl=_AdGenXdsl_ObjectIdentity((1,3,6,1,4,1,664,5,73,1))
_AdGenGeminax_ObjectIdentity=ObjectIdentity
adGenGeminax=_AdGenGeminax_ObjectIdentity((1,3,6,1,4,1,664,5,73,2))
_AdGenXdslID_ObjectIdentity=ObjectIdentity
adGenXdslID=_AdGenXdslID_ObjectIdentity((1,3,6,1,4,1,664,6,10000,73,1))
_AdGenGeminaxID_ObjectIdentity=ObjectIdentity
adGenGeminaxID=_AdGenGeminaxID_ObjectIdentity((1,3,6,1,4,1,664,6,10000,73,2))
mibBuilder.exportSymbols('ADTRAN-SHARED-XDSL-MIB',**{'adXdsl':adXdsl,'adGenXdsl':adGenXdsl,'adGenGeminax':adGenGeminax,'adXdslIdentity':adXdslIdentity,'adGenXdslID':adGenXdslID,'adGenGeminaxID':adGenGeminaxID})