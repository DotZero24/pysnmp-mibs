_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class OVTDAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_OpenView_ObjectIdentity=ObjectIdentity
openView=_OpenView_ObjectIdentity((1,3,6,1,4,1,11,2,17))
_HpOVSNMPSecurity_ObjectIdentity=ObjectIdentity
hpOVSNMPSecurity=_HpOVSNMPSecurity_ObjectIdentity((1,3,6,1,4,1,11,2,17,5))
_HpOVSecureTarget_Type=OVTDAddress
_HpOVSecureTarget_Object=MibScalar
hpOVSecureTarget=_HpOVSecureTarget_Object((1,3,6,1,4,1,11,2,17,5,1),_HpOVSecureTarget_Type())
hpOVSecureTarget.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpOVSecureTarget.setStatus(_A)
mibBuilder.exportSymbols('HPOV-SNMPSEC-MIB',**{'OVTDAddress':OVTDAddress,'hp':hp,'nm':nm,'openView':openView,'hpOVSNMPSecurity':hpOVSNMPSecurity,'hpOVSecureTarget':hpOVSecureTarget})