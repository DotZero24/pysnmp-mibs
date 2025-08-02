_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cFireWall=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,88))
_H3cFirewallobject_ObjectIdentity=ObjectIdentity
h3cFirewallobject=_H3cFirewallobject_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,88,1))
_H3cFirewallSpecs_ObjectIdentity=ObjectIdentity
h3cFirewallSpecs=_H3cFirewallSpecs_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,88,1,1))
_H3cFWMaxConnNum_Type=Unsigned32
_H3cFWMaxConnNum_Object=MibScalar
h3cFWMaxConnNum=_H3cFWMaxConnNum_Object((1,3,6,1,4,1,43,45,1,10,2,88,1,1,1),_H3cFWMaxConnNum_Type())
h3cFWMaxConnNum.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cFWMaxConnNum.setStatus(_B)
_H3cFirewallGlobalStats_ObjectIdentity=ObjectIdentity
h3cFirewallGlobalStats=_H3cFirewallGlobalStats_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,88,1,2))
_H3cFWConnNumCurr_Type=Gauge32
_H3cFWConnNumCurr_Object=MibScalar
h3cFWConnNumCurr=_H3cFWConnNumCurr_Object((1,3,6,1,4,1,43,45,1,10,2,88,1,2,1),_H3cFWConnNumCurr_Type())
h3cFWConnNumCurr.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cFWConnNumCurr.setStatus(_B)
mibBuilder.exportSymbols('A3COM-HUAWEI-FIREWALL-MIB',**{'h3cFireWall':h3cFireWall,'h3cFirewallobject':h3cFirewallobject,'h3cFirewallSpecs':h3cFirewallSpecs,'h3cFWMaxConnNum':h3cFWMaxConnNum,'h3cFirewallGlobalStats':h3cFirewallGlobalStats,'h3cFWConnNumCurr':h3cFWConnNumCurr})