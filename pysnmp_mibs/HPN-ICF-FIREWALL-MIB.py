_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfFireWall=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,88))
_HpnicfFirewallobject_ObjectIdentity=ObjectIdentity
hpnicfFirewallobject=_HpnicfFirewallobject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,88,1))
_HpnicfFirewallSpecs_ObjectIdentity=ObjectIdentity
hpnicfFirewallSpecs=_HpnicfFirewallSpecs_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,88,1,1))
_HpnicfFWMaxConnNum_Type=Unsigned32
_HpnicfFWMaxConnNum_Object=MibScalar
hpnicfFWMaxConnNum=_HpnicfFWMaxConnNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,88,1,1,1),_HpnicfFWMaxConnNum_Type())
hpnicfFWMaxConnNum.setMaxAccess(_A)
if mibBuilder.loadTexts:hpnicfFWMaxConnNum.setStatus(_B)
_HpnicfFirewallGlobalStats_ObjectIdentity=ObjectIdentity
hpnicfFirewallGlobalStats=_HpnicfFirewallGlobalStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,88,1,2))
_HpnicfFWConnNumCurr_Type=Gauge32
_HpnicfFWConnNumCurr_Object=MibScalar
hpnicfFWConnNumCurr=_HpnicfFWConnNumCurr_Object((1,3,6,1,4,1,11,2,14,11,15,2,88,1,2,1),_HpnicfFWConnNumCurr_Type())
hpnicfFWConnNumCurr.setMaxAccess(_A)
if mibBuilder.loadTexts:hpnicfFWConnNumCurr.setStatus(_B)
_HpnicfFWConnRate_Type=Gauge32
_HpnicfFWConnRate_Object=MibScalar
hpnicfFWConnRate=_HpnicfFWConnRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,88,1,2,2),_HpnicfFWConnRate_Type())
hpnicfFWConnRate.setMaxAccess(_A)
if mibBuilder.loadTexts:hpnicfFWConnRate.setStatus(_B)
mibBuilder.exportSymbols('HPN-ICF-FIREWALL-MIB',**{'hpnicfFireWall':hpnicfFireWall,'hpnicfFirewallobject':hpnicfFirewallobject,'hpnicfFirewallSpecs':hpnicfFirewallSpecs,'hpnicfFWMaxConnNum':hpnicfFWMaxConnNum,'hpnicfFirewallGlobalStats':hpnicfFirewallGlobalStats,'hpnicfFWConnNumCurr':hpnicfFWConnNumCurr,'hpnicfFWConnRate':hpnicfFWConnRate})