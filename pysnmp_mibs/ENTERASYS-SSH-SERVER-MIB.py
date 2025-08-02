_p='etsysSshEventLogGroup'
_o='etsysSshAdvancedGroup'
_n='etsysSshBaseGroup'
_m='etsysSshEventLogFilter'
_l='etsysSshPasswordGuesses'
_k='etsysSshIdleTimeout'
_j='etsysSshLoginGraceTime'
_i='etsysSshBannerMessage'
_h='etsysSshRequiredAuthentications'
_g='etsysSshAllowedAuthentications'
_f='etsysSshOperKeyType'
_e='etsysSshAdminKeyType'
_d='etsysSshPublicHostKey'
_c='etsysSshGenerateHostKeys'
_b='etsysSshRandomSeed'
_a='etsysSshRekeyIntervalSeconds'
_Z='etsysSshMACs'
_Y='etsysSshCiphers'
_X='etsysSshNumConnections'
_W='etsysSshMaxConnections'
_V='etsysSshEnabled'
_U='publickey'
_T='password'
_S='rsa512'
_R='dsa512'
_Q='rsa3072'
_P='dsa3072'
_O='rsa2048'
_N='dsa2048'
_M='rsa1024'
_L='dsa1024'
_K='rsa768'
_J='dsa768'
_I='seconds'
_H='TruthValue'
_G='DisplayString'
_F='read-only'
_E='OctetString'
_D='read-write'
_C='Integer32'
_B='ENTERASYS-SSH-SERVER-MIB'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention',_H)
etsysSshServerMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,26))
if mibBuilder.loadTexts:etsysSshServerMIB.setRevisions(('2003-02-19 19:03','2002-11-14 15:41','2002-09-27 17:48','2002-09-18 20:41'))
_EtsysSshObjects_ObjectIdentity=ObjectIdentity
etsysSshObjects=_EtsysSshObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,26,1))
_EtsysSshGeneralBranch_ObjectIdentity=ObjectIdentity
etsysSshGeneralBranch=_EtsysSshGeneralBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,26,1,1))
class _EtsysSshEnabled_Type(TruthValue):defaultValue=2
_EtsysSshEnabled_Type.__name__=_H
_EtsysSshEnabled_Object=MibScalar
etsysSshEnabled=_EtsysSshEnabled_Object((1,3,6,1,4,1,5624,1,2,26,1,1,1),_EtsysSshEnabled_Type())
etsysSshEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSshEnabled.setStatus(_A)
class _EtsysSshEventLogFilter_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('information',2),('warning',3),('error',4)))
_EtsysSshEventLogFilter_Type.__name__=_C
_EtsysSshEventLogFilter_Object=MibScalar
etsysSshEventLogFilter=_EtsysSshEventLogFilter_Object((1,3,6,1,4,1,5624,1,2,26,1,1,2),_EtsysSshEventLogFilter_Type())
etsysSshEventLogFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSshEventLogFilter.setStatus(_A)
class _EtsysSshMaxConnections_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_EtsysSshMaxConnections_Type.__name__=_C
_EtsysSshMaxConnections_Object=MibScalar
etsysSshMaxConnections=_EtsysSshMaxConnections_Object((1,3,6,1,4,1,5624,1,2,26,1,1,3),_EtsysSshMaxConnections_Type())
etsysSshMaxConnections.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysSshMaxConnections.setStatus(_A)
class _EtsysSshNumConnections_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EtsysSshNumConnections_Type.__name__=_C
_EtsysSshNumConnections_Object=MibScalar
etsysSshNumConnections=_EtsysSshNumConnections_Object((1,3,6,1,4,1,5624,1,2,26,1,1,4),_EtsysSshNumConnections_Type())
etsysSshNumConnections.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSshNumConnections.setStatus(_A)
_EtsysSshNetworkBranch_ObjectIdentity=ObjectIdentity
etsysSshNetworkBranch=_EtsysSshNetworkBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,26,1,2))
_EtsysSshCryptoBranch_ObjectIdentity=ObjectIdentity
etsysSshCryptoBranch=_EtsysSshCryptoBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,26,1,3))
class _EtsysSshCiphers_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('anyStdCipher',1),('anyCipher',2),('des',3),('tripleDes',4),('blowfish',5),('arcFour',6),('twofish',7),('cast128',8),('aes',9)))
_EtsysSshCiphers_Type.__name__=_C
_EtsysSshCiphers_Object=MibScalar
etsysSshCiphers=_EtsysSshCiphers_Object((1,3,6,1,4,1,5624,1,2,26,1,3,1),_EtsysSshCiphers_Type())
etsysSshCiphers.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSshCiphers.setStatus(_A)
class _EtsysSshMACs_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('anyStdMac',1),('anyMac',2),('hmacSha1',3),('hmacSha1Dash96',4),('hmacMd5',5),('hmacMd5Dash96',6),('hmacRipemd160',7),('hmacRipemd160Dash96',8)))
_EtsysSshMACs_Type.__name__=_C
_EtsysSshMACs_Object=MibScalar
etsysSshMACs=_EtsysSshMACs_Object((1,3,6,1,4,1,5624,1,2,26,1,3,2),_EtsysSshMACs_Type())
etsysSshMACs.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSshMACs.setStatus(_A)
class _EtsysSshRekeyIntervalSeconds_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EtsysSshRekeyIntervalSeconds_Type.__name__=_C
_EtsysSshRekeyIntervalSeconds_Object=MibScalar
etsysSshRekeyIntervalSeconds=_EtsysSshRekeyIntervalSeconds_Object((1,3,6,1,4,1,5624,1,2,26,1,3,3),_EtsysSshRekeyIntervalSeconds_Type())
etsysSshRekeyIntervalSeconds.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSshRekeyIntervalSeconds.setStatus(_A)
if mibBuilder.loadTexts:etsysSshRekeyIntervalSeconds.setUnits(_I)
class _EtsysSshRandomSeed_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_EtsysSshRandomSeed_Type.__name__=_E
_EtsysSshRandomSeed_Object=MibScalar
etsysSshRandomSeed=_EtsysSshRandomSeed_Object((1,3,6,1,4,1,5624,1,2,26,1,3,4),_EtsysSshRandomSeed_Type())
etsysSshRandomSeed.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSshRandomSeed.setStatus(_A)
_EtsysSshLoginBranch_ObjectIdentity=ObjectIdentity
etsysSshLoginBranch=_EtsysSshLoginBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,26,1,4))
class _EtsysSshLoginGraceTime_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_EtsysSshLoginGraceTime_Type.__name__=_C
_EtsysSshLoginGraceTime_Object=MibScalar
etsysSshLoginGraceTime=_EtsysSshLoginGraceTime_Object((1,3,6,1,4,1,5624,1,2,26,1,4,1),_EtsysSshLoginGraceTime_Type())
etsysSshLoginGraceTime.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSshLoginGraceTime.setStatus(_A)
if mibBuilder.loadTexts:etsysSshLoginGraceTime.setUnits(_I)
class _EtsysSshIdleTimeout_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EtsysSshIdleTimeout_Type.__name__=_C
_EtsysSshIdleTimeout_Object=MibScalar
etsysSshIdleTimeout=_EtsysSshIdleTimeout_Object((1,3,6,1,4,1,5624,1,2,26,1,4,2),_EtsysSshIdleTimeout_Type())
etsysSshIdleTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSshIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:etsysSshIdleTimeout.setUnits('minutes')
class _EtsysSshBannerMessage_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysSshBannerMessage_Type.__name__=_G
_EtsysSshBannerMessage_Object=MibScalar
etsysSshBannerMessage=_EtsysSshBannerMessage_Object((1,3,6,1,4,1,5624,1,2,26,1,4,3),_EtsysSshBannerMessage_Type())
etsysSshBannerMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSshBannerMessage.setStatus(_A)
_EtsysSshServerKeyBranch_ObjectIdentity=ObjectIdentity
etsysSshServerKeyBranch=_EtsysSshServerKeyBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,26,1,5))
class _EtsysSshGenerateHostKeys_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notInitiated',1),('completed',2),('failed',3),('generate',4),('completedPending',5)))
_EtsysSshGenerateHostKeys_Type.__name__=_C
_EtsysSshGenerateHostKeys_Object=MibScalar
etsysSshGenerateHostKeys=_EtsysSshGenerateHostKeys_Object((1,3,6,1,4,1,5624,1,2,26,1,5,1),_EtsysSshGenerateHostKeys_Type())
etsysSshGenerateHostKeys.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSshGenerateHostKeys.setStatus(_A)
class _EtsysSshPublicHostKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_EtsysSshPublicHostKey_Type.__name__=_E
_EtsysSshPublicHostKey_Object=MibScalar
etsysSshPublicHostKey=_EtsysSshPublicHostKey_Object((1,3,6,1,4,1,5624,1,2,26,1,5,2),_EtsysSshPublicHostKey_Type())
etsysSshPublicHostKey.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysSshPublicHostKey.setStatus(_A)
class _EtsysSshAdminKeyType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8),(_R,9),(_S,10)))
_EtsysSshAdminKeyType_Type.__name__=_C
_EtsysSshAdminKeyType_Object=MibScalar
etsysSshAdminKeyType=_EtsysSshAdminKeyType_Object((1,3,6,1,4,1,5624,1,2,26,1,5,3),_EtsysSshAdminKeyType_Type())
etsysSshAdminKeyType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSshAdminKeyType.setStatus(_A)
class _EtsysSshOperKeyType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,99)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8),(_R,9),(_S,10),('none',99)))
_EtsysSshOperKeyType_Type.__name__=_C
_EtsysSshOperKeyType_Object=MibScalar
etsysSshOperKeyType=_EtsysSshOperKeyType_Object((1,3,6,1,4,1,5624,1,2,26,1,5,4),_EtsysSshOperKeyType_Type())
etsysSshOperKeyType.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysSshOperKeyType.setStatus(_A)
_EtsysSshAuthBranch_ObjectIdentity=ObjectIdentity
etsysSshAuthBranch=_EtsysSshAuthBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,26,1,6))
class _EtsysSshPasswordGuesses_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_EtsysSshPasswordGuesses_Type.__name__=_C
_EtsysSshPasswordGuesses_Object=MibScalar
etsysSshPasswordGuesses=_EtsysSshPasswordGuesses_Object((1,3,6,1,4,1,5624,1,2,26,1,6,1),_EtsysSshPasswordGuesses_Type())
etsysSshPasswordGuesses.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSshPasswordGuesses.setStatus(_A)
class _EtsysSshAllowedAuthentications_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('allAuth',1),(_T,2),(_U,3)))
_EtsysSshAllowedAuthentications_Type.__name__=_C
_EtsysSshAllowedAuthentications_Object=MibScalar
etsysSshAllowedAuthentications=_EtsysSshAllowedAuthentications_Object((1,3,6,1,4,1,5624,1,2,26,1,6,2),_EtsysSshAllowedAuthentications_Type())
etsysSshAllowedAuthentications.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSshAllowedAuthentications.setStatus(_A)
class _EtsysSshRequiredAuthentications_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAuth',1),(_T,2),(_U,3)))
_EtsysSshRequiredAuthentications_Type.__name__=_C
_EtsysSshRequiredAuthentications_Object=MibScalar
etsysSshRequiredAuthentications=_EtsysSshRequiredAuthentications_Object((1,3,6,1,4,1,5624,1,2,26,1,6,3),_EtsysSshRequiredAuthentications_Type())
etsysSshRequiredAuthentications.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSshRequiredAuthentications.setStatus(_A)
_EtsysSshConformance_ObjectIdentity=ObjectIdentity
etsysSshConformance=_EtsysSshConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,26,2))
_EtsysSshGroups_ObjectIdentity=ObjectIdentity
etsysSshGroups=_EtsysSshGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,26,2,1))
_EtsysSshCompliances_ObjectIdentity=ObjectIdentity
etsysSshCompliances=_EtsysSshCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,26,2,2))
etsysSshBaseGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,26,2,1,1))
etsysSshBaseGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:etsysSshBaseGroup.setStatus(_A)
etsysSshAdvancedGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,26,2,1,2))
etsysSshAdvancedGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:etsysSshAdvancedGroup.setStatus(_A)
etsysSshEventLogGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,26,2,1,3))
etsysSshEventLogGroup.setObjects((_B,_m))
if mibBuilder.loadTexts:etsysSshEventLogGroup.setStatus(_A)
etsysSshCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,26,2,2,1))
etsysSshCompliance.setObjects(*((_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:etsysSshCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysSshServerMIB':etsysSshServerMIB,'etsysSshObjects':etsysSshObjects,'etsysSshGeneralBranch':etsysSshGeneralBranch,_V:etsysSshEnabled,_m:etsysSshEventLogFilter,_W:etsysSshMaxConnections,_X:etsysSshNumConnections,'etsysSshNetworkBranch':etsysSshNetworkBranch,'etsysSshCryptoBranch':etsysSshCryptoBranch,_Y:etsysSshCiphers,_Z:etsysSshMACs,_a:etsysSshRekeyIntervalSeconds,_b:etsysSshRandomSeed,'etsysSshLoginBranch':etsysSshLoginBranch,_j:etsysSshLoginGraceTime,_k:etsysSshIdleTimeout,_i:etsysSshBannerMessage,'etsysSshServerKeyBranch':etsysSshServerKeyBranch,_c:etsysSshGenerateHostKeys,_d:etsysSshPublicHostKey,_e:etsysSshAdminKeyType,_f:etsysSshOperKeyType,'etsysSshAuthBranch':etsysSshAuthBranch,_l:etsysSshPasswordGuesses,_g:etsysSshAllowedAuthentications,_h:etsysSshRequiredAuthentications,'etsysSshConformance':etsysSshConformance,'etsysSshGroups':etsysSshGroups,_n:etsysSshBaseGroup,_o:etsysSshAdvancedGroup,_p:etsysSshEventLogGroup,'etsysSshCompliances':etsysSshCompliances,'etsysSshCompliance':etsysSshCompliance})