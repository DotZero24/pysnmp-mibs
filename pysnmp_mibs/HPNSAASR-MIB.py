_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpnsaASR_ObjectIdentity=ObjectIdentity
hpnsaASR=_HpnsaASR_ObjectIdentity((1,3,6,1,4,1,11,2,23,25))
_HpnsaASRMibRev_ObjectIdentity=ObjectIdentity
hpnsaASRMibRev=_HpnsaASRMibRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,25,1))
class _HpnsaASRMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnsaASRMibRevMajor_Type.__name__=_C
_HpnsaASRMibRevMajor_Object=MibScalar
hpnsaASRMibRevMajor=_HpnsaASRMibRevMajor_Object((1,3,6,1,4,1,11,2,23,25,1,1),_HpnsaASRMibRevMajor_Type())
hpnsaASRMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaASRMibRevMajor.setStatus(_A)
class _HpnsaASRMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaASRMibRevMinor_Type.__name__=_C
_HpnsaASRMibRevMinor_Object=MibScalar
hpnsaASRMibRevMinor=_HpnsaASRMibRevMinor_Object((1,3,6,1,4,1,11,2,23,25,1,2),_HpnsaASRMibRevMinor_Type())
hpnsaASRMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaASRMibRevMinor.setStatus(_A)
_HpnsaASRParms_ObjectIdentity=ObjectIdentity
hpnsaASRParms=_HpnsaASRParms_ObjectIdentity((1,3,6,1,4,1,11,2,23,25,2))
class _HpnsaASRMaxConsecutiveASR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_HpnsaASRMaxConsecutiveASR_Type.__name__=_C
_HpnsaASRMaxConsecutiveASR_Object=MibScalar
hpnsaASRMaxConsecutiveASR=_HpnsaASRMaxConsecutiveASR_Object((1,3,6,1,4,1,11,2,23,25,2,1),_HpnsaASRMaxConsecutiveASR_Type())
hpnsaASRMaxConsecutiveASR.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaASRMaxConsecutiveASR.setStatus(_A)
_HpnsaASRCurrentConsecutiveASR_Type=Integer32
_HpnsaASRCurrentConsecutiveASR_Object=MibScalar
hpnsaASRCurrentConsecutiveASR=_HpnsaASRCurrentConsecutiveASR_Object((1,3,6,1,4,1,11,2,23,25,2,2),_HpnsaASRCurrentConsecutiveASR_Type())
hpnsaASRCurrentConsecutiveASR.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaASRCurrentConsecutiveASR.setStatus(_A)
_HpnsaASRTimeOutInterval_Type=Integer32
_HpnsaASRTimeOutInterval_Object=MibScalar
hpnsaASRTimeOutInterval=_HpnsaASRTimeOutInterval_Object((1,3,6,1,4,1,11,2,23,25,2,3),_HpnsaASRTimeOutInterval_Type())
hpnsaASRTimeOutInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaASRTimeOutInterval.setStatus(_A)
_HpnsaASRKickInterval_Type=Integer32
_HpnsaASRKickInterval_Object=MibScalar
hpnsaASRKickInterval=_HpnsaASRKickInterval_Object((1,3,6,1,4,1,11,2,23,25,2,4),_HpnsaASRKickInterval_Type())
hpnsaASRKickInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaASRKickInterval.setStatus(_A)
_HpnsaASRTimeoutAction_Type=DisplayString
_HpnsaASRTimeoutAction_Object=MibScalar
hpnsaASRTimeoutAction=_HpnsaASRTimeoutAction_Object((1,3,6,1,4,1,11,2,23,25,2,5),_HpnsaASRTimeoutAction_Type())
hpnsaASRTimeoutAction.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaASRTimeoutAction.setStatus(_A)
mibBuilder.exportSymbols('HPNSAASR-MIB',**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaASR':hpnsaASR,'hpnsaASRMibRev':hpnsaASRMibRev,'hpnsaASRMibRevMajor':hpnsaASRMibRevMajor,'hpnsaASRMibRevMinor':hpnsaASRMibRevMinor,'hpnsaASRParms':hpnsaASRParms,'hpnsaASRMaxConsecutiveASR':hpnsaASRMaxConsecutiveASR,'hpnsaASRCurrentConsecutiveASR':hpnsaASRCurrentConsecutiveASR,'hpnsaASRTimeOutInterval':hpnsaASRTimeOutInterval,'hpnsaASRKickInterval':hpnsaASRKickInterval,'hpnsaASRTimeoutAction':hpnsaASRTimeoutAction})