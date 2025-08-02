if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pbi=ModuleIdentity((1,3,6,1,4,1,1070))
if mibBuilder.loadTexts:pbi.setRevisions(('2006-09-13 10:23',))
_Org_ObjectIdentity=ObjectIdentity
org=_Org_ObjectIdentity((1,3))
_Dod_ObjectIdentity=ObjectIdentity
dod=_Dod_ObjectIdentity((1,3,6))
_Internet_ObjectIdentity=ObjectIdentity
internet=_Internet_ObjectIdentity((1,3,6,1))
_Private_ObjectIdentity=ObjectIdentity
private=_Private_ObjectIdentity((1,3,6,1,4))
_Enterprises_ObjectIdentity=ObjectIdentity
enterprises=_Enterprises_ObjectIdentity((1,3,6,1,4,1))
_Mg_ObjectIdentity=ObjectIdentity
mg=_Mg_ObjectIdentity((1,3,6,1,4,1,1070,3))
mibBuilder.exportSymbols('PBI-MAIN-MIB',**{'org':org,'dod':dod,'internet':internet,'private':private,'enterprises':enterprises,'pbi':pbi,'mg':mg})