_S='coDot1xPaeAuthenticatorGroup'
_R='coDot1xPaeSystemGroup'
_Q='coDot1xAuthReAuthMax'
_P='coDot1xAuthKeyTxEnabled'
_O='coDot1xAuthReAuthEnabled'
_N='coDot1xAuthReAuthPeriod'
_M='coDot1xAuthMaxReq'
_L='coDot1xAuthServerTimeout'
_K='coDot1xAuthSuppTimeout'
_J='coDot1xAuthTxPeriod'
_I='coDot1xAuthQuietPeriod'
_H='coDot1xPaeSystemModifyKeyInterval'
_G='coDot1xPaeSystemModifyKey'
_F='TruthValue'
_E='seconds'
_D='Unsigned32'
_C='read-write'
_B='ALVARION-802DOT1X-ACCESS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
alvarion802Dot1xMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,8))
_CoPaeMIBObjects_ObjectIdentity=ObjectIdentity
coPaeMIBObjects=_CoPaeMIBObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,8,1))
_CoDot1xPaeSystem_ObjectIdentity=ObjectIdentity
coDot1xPaeSystem=_CoDot1xPaeSystem_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,8,1,1))
class _CoDot1xPaeSystemModifyKey_Type(TruthValue):defaultValue=2
_CoDot1xPaeSystemModifyKey_Type.__name__=_F
_CoDot1xPaeSystemModifyKey_Object=MibScalar
coDot1xPaeSystemModifyKey=_CoDot1xPaeSystemModifyKey_Object((1,3,6,1,4,1,12394,1,10,5,8,1,1,1),_CoDot1xPaeSystemModifyKey_Type())
coDot1xPaeSystemModifyKey.setMaxAccess('read-only')
if mibBuilder.loadTexts:coDot1xPaeSystemModifyKey.setStatus(_A)
class _CoDot1xPaeSystemModifyKeyInterval_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,65535))
_CoDot1xPaeSystemModifyKeyInterval_Type.__name__=_D
_CoDot1xPaeSystemModifyKeyInterval_Object=MibScalar
coDot1xPaeSystemModifyKeyInterval=_CoDot1xPaeSystemModifyKeyInterval_Object((1,3,6,1,4,1,12394,1,10,5,8,1,1,2),_CoDot1xPaeSystemModifyKeyInterval_Type())
coDot1xPaeSystemModifyKeyInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:coDot1xPaeSystemModifyKeyInterval.setStatus(_A)
if mibBuilder.loadTexts:coDot1xPaeSystemModifyKeyInterval.setUnits(_E)
_CoDot1xPaeAuthenticator_ObjectIdentity=ObjectIdentity
coDot1xPaeAuthenticator=_CoDot1xPaeAuthenticator_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,8,1,2))
class _CoDot1xAuthQuietPeriod_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CoDot1xAuthQuietPeriod_Type.__name__=_D
_CoDot1xAuthQuietPeriod_Object=MibScalar
coDot1xAuthQuietPeriod=_CoDot1xAuthQuietPeriod_Object((1,3,6,1,4,1,12394,1,10,5,8,1,2,1),_CoDot1xAuthQuietPeriod_Type())
coDot1xAuthQuietPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:coDot1xAuthQuietPeriod.setStatus(_A)
if mibBuilder.loadTexts:coDot1xAuthQuietPeriod.setUnits(_E)
class _CoDot1xAuthTxPeriod_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CoDot1xAuthTxPeriod_Type.__name__=_D
_CoDot1xAuthTxPeriod_Object=MibScalar
coDot1xAuthTxPeriod=_CoDot1xAuthTxPeriod_Object((1,3,6,1,4,1,12394,1,10,5,8,1,2,2),_CoDot1xAuthTxPeriod_Type())
coDot1xAuthTxPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:coDot1xAuthTxPeriod.setStatus(_A)
if mibBuilder.loadTexts:coDot1xAuthTxPeriod.setUnits(_E)
class _CoDot1xAuthSuppTimeout_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CoDot1xAuthSuppTimeout_Type.__name__=_D
_CoDot1xAuthSuppTimeout_Object=MibScalar
coDot1xAuthSuppTimeout=_CoDot1xAuthSuppTimeout_Object((1,3,6,1,4,1,12394,1,10,5,8,1,2,3),_CoDot1xAuthSuppTimeout_Type())
coDot1xAuthSuppTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:coDot1xAuthSuppTimeout.setStatus(_A)
if mibBuilder.loadTexts:coDot1xAuthSuppTimeout.setUnits(_E)
class _CoDot1xAuthServerTimeout_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CoDot1xAuthServerTimeout_Type.__name__=_D
_CoDot1xAuthServerTimeout_Object=MibScalar
coDot1xAuthServerTimeout=_CoDot1xAuthServerTimeout_Object((1,3,6,1,4,1,12394,1,10,5,8,1,2,4),_CoDot1xAuthServerTimeout_Type())
coDot1xAuthServerTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:coDot1xAuthServerTimeout.setStatus(_A)
if mibBuilder.loadTexts:coDot1xAuthServerTimeout.setUnits(_E)
class _CoDot1xAuthMaxReq_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CoDot1xAuthMaxReq_Type.__name__=_D
_CoDot1xAuthMaxReq_Object=MibScalar
coDot1xAuthMaxReq=_CoDot1xAuthMaxReq_Object((1,3,6,1,4,1,12394,1,10,5,8,1,2,5),_CoDot1xAuthMaxReq_Type())
coDot1xAuthMaxReq.setMaxAccess(_C)
if mibBuilder.loadTexts:coDot1xAuthMaxReq.setStatus(_A)
class _CoDot1xAuthReAuthPeriod_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CoDot1xAuthReAuthPeriod_Type.__name__=_D
_CoDot1xAuthReAuthPeriod_Object=MibScalar
coDot1xAuthReAuthPeriod=_CoDot1xAuthReAuthPeriod_Object((1,3,6,1,4,1,12394,1,10,5,8,1,2,6),_CoDot1xAuthReAuthPeriod_Type())
coDot1xAuthReAuthPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:coDot1xAuthReAuthPeriod.setStatus(_A)
if mibBuilder.loadTexts:coDot1xAuthReAuthPeriod.setUnits(_E)
class _CoDot1xAuthReAuthEnabled_Type(TruthValue):defaultValue=2
_CoDot1xAuthReAuthEnabled_Type.__name__=_F
_CoDot1xAuthReAuthEnabled_Object=MibScalar
coDot1xAuthReAuthEnabled=_CoDot1xAuthReAuthEnabled_Object((1,3,6,1,4,1,12394,1,10,5,8,1,2,7),_CoDot1xAuthReAuthEnabled_Type())
coDot1xAuthReAuthEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:coDot1xAuthReAuthEnabled.setStatus(_A)
class _CoDot1xAuthKeyTxEnabled_Type(TruthValue):defaultValue=1
_CoDot1xAuthKeyTxEnabled_Type.__name__=_F
_CoDot1xAuthKeyTxEnabled_Object=MibScalar
coDot1xAuthKeyTxEnabled=_CoDot1xAuthKeyTxEnabled_Object((1,3,6,1,4,1,12394,1,10,5,8,1,2,8),_CoDot1xAuthKeyTxEnabled_Type())
coDot1xAuthKeyTxEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:coDot1xAuthKeyTxEnabled.setStatus(_A)
class _CoDot1xAuthReAuthMax_Type(Unsigned32):defaultValue=8;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CoDot1xAuthReAuthMax_Type.__name__=_D
_CoDot1xAuthReAuthMax_Object=MibScalar
coDot1xAuthReAuthMax=_CoDot1xAuthReAuthMax_Object((1,3,6,1,4,1,12394,1,10,5,8,1,2,9),_CoDot1xAuthReAuthMax_Type())
coDot1xAuthReAuthMax.setMaxAccess(_C)
if mibBuilder.loadTexts:coDot1xAuthReAuthMax.setStatus(_A)
_CoDot1xPaeConformance_ObjectIdentity=ObjectIdentity
coDot1xPaeConformance=_CoDot1xPaeConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,8,2))
_CoDot1xPaeGroups_ObjectIdentity=ObjectIdentity
coDot1xPaeGroups=_CoDot1xPaeGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,8,2,1))
_CoDot1xPaeCompliances_ObjectIdentity=ObjectIdentity
coDot1xPaeCompliances=_CoDot1xPaeCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,8,2,2))
coDot1xPaeSystemGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,8,2,1,1))
coDot1xPaeSystemGroup.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:coDot1xPaeSystemGroup.setStatus(_A)
coDot1xPaeAuthenticatorGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,8,2,1,2))
coDot1xPaeAuthenticatorGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:coDot1xPaeAuthenticatorGroup.setStatus(_A)
coDot1xPaeCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,8,2,2,1))
coDot1xPaeCompliance.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:coDot1xPaeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alvarion802Dot1xMIB':alvarion802Dot1xMIB,'coPaeMIBObjects':coPaeMIBObjects,'coDot1xPaeSystem':coDot1xPaeSystem,_G:coDot1xPaeSystemModifyKey,_H:coDot1xPaeSystemModifyKeyInterval,'coDot1xPaeAuthenticator':coDot1xPaeAuthenticator,_I:coDot1xAuthQuietPeriod,_J:coDot1xAuthTxPeriod,_K:coDot1xAuthSuppTimeout,_L:coDot1xAuthServerTimeout,_M:coDot1xAuthMaxReq,_N:coDot1xAuthReAuthPeriod,_O:coDot1xAuthReAuthEnabled,_P:coDot1xAuthKeyTxEnabled,_Q:coDot1xAuthReAuthMax,'coDot1xPaeConformance':coDot1xPaeConformance,'coDot1xPaeGroups':coDot1xPaeGroups,_R:coDot1xPaeSystemGroup,_S:coDot1xPaeAuthenticatorGroup,'coDot1xPaeCompliances':coDot1xPaeCompliances,'coDot1xPaeCompliance':coDot1xPaeCompliance})