_E='disable'
_D='enable'
_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zxDslSshMib=ModuleIdentity((1,3,6,1,4,1,3902,1004,35))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxDsl_ObjectIdentity=ObjectIdentity
zxDsl=_ZxDsl_ObjectIdentity((1,3,6,1,4,1,3902,1004))
_ZxDslSshglobal_ObjectIdentity=ObjectIdentity
zxDslSshglobal=_ZxDslSshglobal_ObjectIdentity((1,3,6,1,4,1,3902,1004,35,1))
class _ZxDslSshGlobalState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxDslSshGlobalState_Type.__name__=_A
_ZxDslSshGlobalState_Object=MibScalar
zxDslSshGlobalState=_ZxDslSshGlobalState_Object((1,3,6,1,4,1,3902,1004,35,1,1),_ZxDslSshGlobalState_Type())
zxDslSshGlobalState.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslSshGlobalState.setStatus(_C)
class _ZxDslSshAuthMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('radius',2)))
_ZxDslSshAuthMode_Type.__name__=_A
_ZxDslSshAuthMode_Object=MibScalar
zxDslSshAuthMode=_ZxDslSshAuthMode_Object((1,3,6,1,4,1,3902,1004,35,1,2),_ZxDslSshAuthMode_Type())
zxDslSshAuthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslSshAuthMode.setStatus(_C)
class _ZxDslSshAuthType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pap',1),('chap',2)))
_ZxDslSshAuthType_Type.__name__=_A
_ZxDslSshAuthType_Object=MibScalar
zxDslSshAuthType=_ZxDslSshAuthType_Object((1,3,6,1,4,1,3902,1004,35,1,3),_ZxDslSshAuthType_Type())
zxDslSshAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslSshAuthType.setStatus(_C)
class _ZxDslSshGenKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('value',1))
_ZxDslSshGenKey_Type.__name__=_A
_ZxDslSshGenKey_Object=MibScalar
zxDslSshGenKey=_ZxDslSshGenKey_Object((1,3,6,1,4,1,3902,1004,35,1,4),_ZxDslSshGenKey_Type())
zxDslSshGenKey.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslSshGenKey.setStatus(_C)
class _ZxDslSshServOnly_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxDslSshServOnly_Type.__name__=_A
_ZxDslSshServOnly_Object=MibScalar
zxDslSshServOnly=_ZxDslSshServOnly_Object((1,3,6,1,4,1,3902,1004,35,1,5),_ZxDslSshServOnly_Type())
zxDslSshServOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslSshServOnly.setStatus(_C)
class _ZxDslSshVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sshv1',1),('sshv2',2)))
_ZxDslSshVersion_Type.__name__=_A
_ZxDslSshVersion_Object=MibScalar
zxDslSshVersion=_ZxDslSshVersion_Object((1,3,6,1,4,1,3902,1004,35,1,6),_ZxDslSshVersion_Type())
zxDslSshVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslSshVersion.setStatus(_C)
mibBuilder.exportSymbols('ZTE-DSL-SSH-MIB',**{'zte':zte,'zxDsl':zxDsl,'zxDslSshMib':zxDslSshMib,'zxDslSshglobal':zxDslSshglobal,'zxDslSshGlobalState':zxDslSshGlobalState,'zxDslSshAuthMode':zxDslSshAuthMode,'zxDslSshAuthType':zxDslSshAuthType,'zxDslSshGenKey':zxDslSshGenKey,'zxDslSshServOnly':zxDslSshServOnly,'zxDslSshVersion':zxDslSshVersion})