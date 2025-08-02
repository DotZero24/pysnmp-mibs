_C='mandatory'
_B='read-only'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpnsaRPS_ObjectIdentity=ObjectIdentity
hpnsaRPS=_HpnsaRPS_ObjectIdentity((1,3,6,1,4,1,11,2,23,22))
_HpnsaRPSMibRev_ObjectIdentity=ObjectIdentity
hpnsaRPSMibRev=_HpnsaRPSMibRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,22,1))
class _HpnsaRPSMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnsaRPSMibRevMajor_Type.__name__=_A
_HpnsaRPSMibRevMajor_Object=MibScalar
hpnsaRPSMibRevMajor=_HpnsaRPSMibRevMajor_Object((1,3,6,1,4,1,11,2,23,22,1,1),_HpnsaRPSMibRevMajor_Type())
hpnsaRPSMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRPSMibRevMajor.setStatus(_C)
class _HpnsaRPSMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaRPSMibRevMinor_Type.__name__=_A
_HpnsaRPSMibRevMinor_Object=MibScalar
hpnsaRPSMibRevMinor=_HpnsaRPSMibRevMinor_Object((1,3,6,1,4,1,11,2,23,22,1,2),_HpnsaRPSMibRevMinor_Type())
hpnsaRPSMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRPSMibRevMinor.setStatus(_C)
mibBuilder.exportSymbols('HPNSARPS-MIB',**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaRPS':hpnsaRPS,'hpnsaRPSMibRev':hpnsaRPSMibRev,'hpnsaRPSMibRevMajor':hpnsaRPSMibRevMajor,'hpnsaRPSMibRevMinor':hpnsaRPSMibRevMinor})