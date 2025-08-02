_n='hipsDropPacInUnitTime'
_m='hipsCardStatus'
_l='hipsCardCPLDVer'
_k='hipsCardSoftVer'
_j='hipsCardHardVer'
_i='hipsTransformName'
_h='hipsStaticCryptomapSN'
_g='hipsStaticCryptomapName'
_f='hipsIsakmpPolPriority'
_e='unkown'
_d='hikeConnId'
_c='manual'
_b='isakmp'
_a='ealgXQc5'
_Z='ealgXAes'
_Y='ealgXSkipjack'
_X='ealgXCast'
_W='ealgXBlf'
_V='ealg3desCbc'
_U='ealgDescbc'
_T='ealgNone'
_S='hipsSPI'
_R='hipsProtocol'
_Q='hipsPeerIpAddr'
_P='Gauge32'
_O='read-write'
_N='none'
_M='aalgXSha1'
_L='aalgXMd5'
_K='aalgXRipeMd160Hmac96'
_J='aalgSha1Hmac96'
_I='aalgMd5Hmac96'
_H='aalgSha1Hmac'
_G='aalgMd5Hmac'
_F='aalgNone'
_E='hipsCardSlot'
_D='A3COM-HUAWEI-NDEC-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mlsr,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','mlsr')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_P,_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
huaweiNDEC=ModuleIdentity((1,3,6,1,4,1,43,45,1,2,33,2))
if mibBuilder.loadTexts:huaweiNDEC.setRevisions(('2004-09-15 10:52',))
_HipsNDECSAListTable_Object=MibTable
hipsNDECSAListTable=_HipsNDECSAListTable_Object((1,3,6,1,4,1,43,45,1,2,33,2,1))
if mibBuilder.loadTexts:hipsNDECSAListTable.setStatus(_A)
_HipsNDECSAListEntry_Object=MibTableRow
hipsNDECSAListEntry=_HipsNDECSAListEntry_Object((1,3,6,1,4,1,43,45,1,2,33,2,1,1))
hipsNDECSAListEntry.setIndexNames((0,_D,_Q),(0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:hipsNDECSAListEntry.setStatus(_A)
_HipsPeerIpAddr_Type=IpAddress
_HipsPeerIpAddr_Object=MibTableColumn
hipsPeerIpAddr=_HipsPeerIpAddr_Object((1,3,6,1,4,1,43,45,1,2,33,2,1,1,1),_HipsPeerIpAddr_Type())
hipsPeerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsPeerIpAddr.setStatus(_A)
class _HipsProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(50,51)));namedValues=NamedValues(*(('ipsecEsp',50),('ipsecAh',51)))
_HipsProtocol_Type.__name__=_C
_HipsProtocol_Object=MibTableColumn
hipsProtocol=_HipsProtocol_Object((1,3,6,1,4,1,43,45,1,2,33,2,1,1,2),_HipsProtocol_Type())
hipsProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsProtocol.setStatus(_A)
class _HipsSPI_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,4294967295))
_HipsSPI_Type.__name__=_P
_HipsSPI_Object=MibTableColumn
hipsSPI=_HipsSPI_Object((1,3,6,1,4,1,43,45,1,2,33,2,1,1,3),_HipsSPI_Type())
hipsSPI.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsSPI.setStatus(_A)
class _HipsEncAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_T,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_Z,7),(_a,8),('ealgXNsa',9)))
_HipsEncAlgorithm_Type.__name__=_C
_HipsEncAlgorithm_Object=MibTableColumn
hipsEncAlgorithm=_HipsEncAlgorithm_Object((1,3,6,1,4,1,43,45,1,2,33,2,1,1,4),_HipsEncAlgorithm_Type())
hipsEncAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsEncAlgorithm.setStatus(_A)
class _HipsAuthAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_M,8)))
_HipsAuthAlgorithm_Type.__name__=_C
_HipsAuthAlgorithm_Object=MibTableColumn
hipsAuthAlgorithm=_HipsAuthAlgorithm_Object((1,3,6,1,4,1,43,45,1,2,33,2,1,1,5),_HipsAuthAlgorithm_Type())
hipsAuthAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsAuthAlgorithm.setStatus(_A)
_HipsLocalIpAddr_Type=IpAddress
_HipsLocalIpAddr_Object=MibTableColumn
hipsLocalIpAddr=_HipsLocalIpAddr_Object((1,3,6,1,4,1,43,45,1,2,33,2,1,1,6),_HipsLocalIpAddr_Type())
hipsLocalIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsLocalIpAddr.setStatus(_A)
_HipsSaLifeKBytes_Type=Gauge32
_HipsSaLifeKBytes_Object=MibTableColumn
hipsSaLifeKBytes=_HipsSaLifeKBytes_Object((1,3,6,1,4,1,43,45,1,2,33,2,1,1,7),_HipsSaLifeKBytes_Type())
hipsSaLifeKBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsSaLifeKBytes.setStatus(_A)
_HipsSaLifeSecond_Type=Gauge32
_HipsSaLifeSecond_Object=MibTableColumn
hipsSaLifeSecond=_HipsSaLifeSecond_Object((1,3,6,1,4,1,43,45,1,2,33,2,1,1,8),_HipsSaLifeSecond_Type())
hipsSaLifeSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsSaLifeSecond.setStatus(_A)
_HipsByCard_Type=TruthValue
_HipsByCard_Object=MibTableColumn
hipsByCard=_HipsByCard_Object((1,3,6,1,4,1,43,45,1,2,33,2,1,1,9),_HipsByCard_Type())
hipsByCard.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsByCard.setStatus(_A)
class _HipsNegotiateSaMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_b,2),(_c,3)))
_HipsNegotiateSaMode_Type.__name__=_C
_HipsNegotiateSaMode_Object=MibTableColumn
hipsNegotiateSaMode=_HipsNegotiateSaMode_Object((1,3,6,1,4,1,43,45,1,2,33,2,1,1,10),_HipsNegotiateSaMode_Type())
hipsNegotiateSaMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsNegotiateSaMode.setStatus(_A)
_HipsExpBytes_Type=Gauge32
_HipsExpBytes_Object=MibTableColumn
hipsExpBytes=_HipsExpBytes_Object((1,3,6,1,4,1,43,45,1,2,33,2,1,1,11),_HipsExpBytes_Type())
hipsExpBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsExpBytes.setStatus(_A)
_HipsSoftBytes_Type=Gauge32
_HipsSoftBytes_Object=MibTableColumn
hipsSoftBytes=_HipsSoftBytes_Object((1,3,6,1,4,1,43,45,1,2,33,2,1,1,12),_HipsSoftBytes_Type())
hipsSoftBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsSoftBytes.setStatus(_A)
_HipsExpTimeout_Type=Gauge32
_HipsExpTimeout_Object=MibTableColumn
hipsExpTimeout=_HipsExpTimeout_Object((1,3,6,1,4,1,43,45,1,2,33,2,1,1,13),_HipsExpTimeout_Type())
hipsExpTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsExpTimeout.setStatus(_A)
_HipsSoftTimeout_Type=Gauge32
_HipsSoftTimeout_Object=MibTableColumn
hipsSoftTimeout=_HipsSoftTimeout_Object((1,3,6,1,4,1,43,45,1,2,33,2,1,1,14),_HipsSoftTimeout_Type())
hipsSoftTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsSoftTimeout.setStatus(_A)
_HikeSATable_Object=MibTable
hikeSATable=_HikeSATable_Object((1,3,6,1,4,1,43,45,1,2,33,2,2))
if mibBuilder.loadTexts:hikeSATable.setStatus(_A)
_HikeSAEntry_Object=MibTableRow
hikeSAEntry=_HikeSAEntry_Object((1,3,6,1,4,1,43,45,1,2,33,2,2,1))
hikeSAEntry.setIndexNames((0,_D,_d))
if mibBuilder.loadTexts:hikeSAEntry.setStatus(_A)
class _HikeConnId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HikeConnId_Type.__name__=_C
_HikeConnId_Object=MibTableColumn
hikeConnId=_HikeConnId_Object((1,3,6,1,4,1,43,45,1,2,33,2,2,1,1),_HikeConnId_Type())
hikeConnId.setMaxAccess(_B)
if mibBuilder.loadTexts:hikeConnId.setStatus(_A)
_HikePeerIpAddr_Type=IpAddress
_HikePeerIpAddr_Object=MibTableColumn
hikePeerIpAddr=_HikePeerIpAddr_Object((1,3,6,1,4,1,43,45,1,2,33,2,2,1,2),_HikePeerIpAddr_Type())
hikePeerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hikePeerIpAddr.setStatus(_A)
_HikeFlag_Type=DisplayString
_HikeFlag_Object=MibTableColumn
hikeFlag=_HikeFlag_Object((1,3,6,1,4,1,43,45,1,2,33,2,2,1,3),_HikeFlag_Type())
hikeFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:hikeFlag.setStatus(_A)
class _HikePhase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),('phase1',2),('phase2',3)))
_HikePhase_Type.__name__=_C
_HikePhase_Object=MibTableColumn
hikePhase=_HikePhase_Object((1,3,6,1,4,1,43,45,1,2,33,2,2,1,4),_HikePhase_Type())
hikePhase.setMaxAccess(_B)
if mibBuilder.loadTexts:hikePhase.setStatus(_A)
class _HikeDoi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),('ipsec',2)))
_HikeDoi_Type.__name__=_C
_HikeDoi_Object=MibTableColumn
hikeDoi=_HikeDoi_Object((1,3,6,1,4,1,43,45,1,2,33,2,2,1,5),_HikeDoi_Type())
hikeDoi.setMaxAccess(_B)
if mibBuilder.loadTexts:hikeDoi.setStatus(_A)
_HikeClearSA_Type=TruthValue
_HikeClearSA_Object=MibTableColumn
hikeClearSA=_HikeClearSA_Object((1,3,6,1,4,1,43,45,1,2,33,2,2,1,6),_HikeClearSA_Type())
hikeClearSA.setMaxAccess(_O)
if mibBuilder.loadTexts:hikeClearSA.setStatus(_A)
_HipsIKEPolicyTable_Object=MibTable
hipsIKEPolicyTable=_HipsIKEPolicyTable_Object((1,3,6,1,4,1,43,45,1,2,33,2,3))
if mibBuilder.loadTexts:hipsIKEPolicyTable.setStatus(_A)
_HipsIKEPolicyEntry_Object=MibTableRow
hipsIKEPolicyEntry=_HipsIKEPolicyEntry_Object((1,3,6,1,4,1,43,45,1,2,33,2,3,1))
hipsIKEPolicyEntry.setIndexNames((0,_D,_f))
if mibBuilder.loadTexts:hipsIKEPolicyEntry.setStatus(_A)
class _HipsIsakmpPolPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HipsIsakmpPolPriority_Type.__name__=_C
_HipsIsakmpPolPriority_Object=MibTableColumn
hipsIsakmpPolPriority=_HipsIsakmpPolPriority_Object((1,3,6,1,4,1,43,45,1,2,33,2,3,1,1),_HipsIsakmpPolPriority_Type())
hipsIsakmpPolPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsIsakmpPolPriority.setStatus(_A)
class _HipsIsakmpPolEncr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ikeEncryptNone',1),('ikeEncryptDesCbc',2),('ikeEncryptIdeaCbc',3),('ikeEncryptBlowfishcbc',4),('ikeEncryptRc5R16B64cbc',5),('ikeEncrypt3DesCbc',6),('ikeEncryptCastCbc',7)))
_HipsIsakmpPolEncr_Type.__name__=_C
_HipsIsakmpPolEncr_Object=MibTableColumn
hipsIsakmpPolEncr=_HipsIsakmpPolEncr_Object((1,3,6,1,4,1,43,45,1,2,33,2,3,1,2),_HipsIsakmpPolEncr_Type())
hipsIsakmpPolEncr.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsIsakmpPolEncr.setStatus(_A)
class _HipsIsakmpPolHash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ikeHashNone',1),('ikeHashMd5',2),('ikeHashSha',3),('ikeHashTiger',4)))
_HipsIsakmpPolHash_Type.__name__=_C
_HipsIsakmpPolHash_Object=MibTableColumn
hipsIsakmpPolHash=_HipsIsakmpPolHash_Object((1,3,6,1,4,1,43,45,1,2,33,2,3,1,3),_HipsIsakmpPolHash_Type())
hipsIsakmpPolHash.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsIsakmpPolHash.setStatus(_A)
class _HipsIsakmpPolAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ikeAuthPreNone',1),('ikeAuthPreShared',2),('ikeAuthDss',3),('ikeAuthRsaSig',4),('ikeAuthRsaEnc',5),('ikeAuthRsaEncRev',6)))
_HipsIsakmpPolAuth_Type.__name__=_C
_HipsIsakmpPolAuth_Object=MibTableColumn
hipsIsakmpPolAuth=_HipsIsakmpPolAuth_Object((1,3,6,1,4,1,43,45,1,2,33,2,3,1,4),_HipsIsakmpPolAuth_Type())
hipsIsakmpPolAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsIsakmpPolAuth.setStatus(_A)
class _HipsIsakmpPolGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('dhGroup1',2),('dhGroup2',3)))
_HipsIsakmpPolGroup_Type.__name__=_C
_HipsIsakmpPolGroup_Object=MibTableColumn
hipsIsakmpPolGroup=_HipsIsakmpPolGroup_Object((1,3,6,1,4,1,43,45,1,2,33,2,3,1,5),_HipsIsakmpPolGroup_Type())
hipsIsakmpPolGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsIsakmpPolGroup.setStatus(_A)
_HipsIsakmpPolLifetime_Type=Gauge32
_HipsIsakmpPolLifetime_Object=MibTableColumn
hipsIsakmpPolLifetime=_HipsIsakmpPolLifetime_Object((1,3,6,1,4,1,43,45,1,2,33,2,3,1,6),_HipsIsakmpPolLifetime_Type())
hipsIsakmpPolLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsIsakmpPolLifetime.setStatus(_A)
_HipsStaticCryptomapTable_Object=MibTable
hipsStaticCryptomapTable=_HipsStaticCryptomapTable_Object((1,3,6,1,4,1,43,45,1,2,33,2,4))
if mibBuilder.loadTexts:hipsStaticCryptomapTable.setStatus(_A)
_HipsStaticCryptomapEntry_Object=MibTableRow
hipsStaticCryptomapEntry=_HipsStaticCryptomapEntry_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1))
hipsStaticCryptomapEntry.setIndexNames((0,_D,_g),(0,_D,_h))
if mibBuilder.loadTexts:hipsStaticCryptomapEntry.setStatus(_A)
_HipsStaticCryptomapName_Type=DisplayString
_HipsStaticCryptomapName_Object=MibTableColumn
hipsStaticCryptomapName=_HipsStaticCryptomapName_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,1),_HipsStaticCryptomapName_Type())
hipsStaticCryptomapName.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsStaticCryptomapName.setStatus(_A)
class _HipsStaticCryptomapSN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HipsStaticCryptomapSN_Type.__name__=_C
_HipsStaticCryptomapSN_Object=MibTableColumn
hipsStaticCryptomapSN=_HipsStaticCryptomapSN_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,2),_HipsStaticCryptomapSN_Type())
hipsStaticCryptomapSN.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsStaticCryptomapSN.setStatus(_A)
class _HipsStaticCryptomapNegMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_b,2),(_c,3)))
_HipsStaticCryptomapNegMode_Type.__name__=_C
_HipsStaticCryptomapNegMode_Object=MibTableColumn
hipsStaticCryptomapNegMode=_HipsStaticCryptomapNegMode_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,3),_HipsStaticCryptomapNegMode_Type())
hipsStaticCryptomapNegMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsStaticCryptomapNegMode.setStatus(_A)
class _HipsStaticCryptomapMatchAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_HipsStaticCryptomapMatchAddr_Type.__name__=_C
_HipsStaticCryptomapMatchAddr_Object=MibTableColumn
hipsStaticCryptomapMatchAddr=_HipsStaticCryptomapMatchAddr_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,4),_HipsStaticCryptomapMatchAddr_Type())
hipsStaticCryptomapMatchAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsStaticCryptomapMatchAddr.setStatus(_A)
_HipsStaticCryptomapPeerIpAddr_Type=IpAddress
_HipsStaticCryptomapPeerIpAddr_Object=MibTableColumn
hipsStaticCryptomapPeerIpAddr=_HipsStaticCryptomapPeerIpAddr_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,5),_HipsStaticCryptomapPeerIpAddr_Type())
hipsStaticCryptomapPeerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsStaticCryptomapPeerIpAddr.setStatus(_A)
_HipsStaticCryptomapTransforName_Type=DisplayString
_HipsStaticCryptomapTransforName_Object=MibTableColumn
hipsStaticCryptomapTransforName=_HipsStaticCryptomapTransforName_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,6),_HipsStaticCryptomapTransforName_Type())
hipsStaticCryptomapTransforName.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsStaticCryptomapTransforName.setStatus(_A)
_HipsStaticCryptomapLifetime_Type=Gauge32
_HipsStaticCryptomapLifetime_Object=MibTableColumn
hipsStaticCryptomapLifetime=_HipsStaticCryptomapLifetime_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,7),_HipsStaticCryptomapLifetime_Type())
hipsStaticCryptomapLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsStaticCryptomapLifetime.setStatus(_A)
_HipsStaticCryptomapLifesize_Type=Gauge32
_HipsStaticCryptomapLifesize_Object=MibTableColumn
hipsStaticCryptomapLifesize=_HipsStaticCryptomapLifesize_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,8),_HipsStaticCryptomapLifesize_Type())
hipsStaticCryptomapLifesize.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsStaticCryptomapLifesize.setStatus(_A)
_HipsStaticCryptomapLocalIpAddr_Type=IpAddress
_HipsStaticCryptomapLocalIpAddr_Object=MibTableColumn
hipsStaticCryptomapLocalIpAddr=_HipsStaticCryptomapLocalIpAddr_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,9),_HipsStaticCryptomapLocalIpAddr_Type())
hipsStaticCryptomapLocalIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsStaticCryptomapLocalIpAddr.setStatus(_A)
_HipsIfNameUsed_Type=DisplayString
_HipsIfNameUsed_Object=MibTableColumn
hipsIfNameUsed=_HipsIfNameUsed_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,10),_HipsIfNameUsed_Type())
hipsIfNameUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsIfNameUsed.setStatus(_A)
_HipsInAHSPI_Type=Gauge32
_HipsInAHSPI_Object=MibTableColumn
hipsInAHSPI=_HipsInAHSPI_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,11),_HipsInAHSPI_Type())
hipsInAHSPI.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsInAHSPI.setStatus(_A)
_HipsInESPSPI_Type=Gauge32
_HipsInESPSPI_Object=MibTableColumn
hipsInESPSPI=_HipsInESPSPI_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,12),_HipsInESPSPI_Type())
hipsInESPSPI.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsInESPSPI.setStatus(_A)
_HipsOutAHSPI_Type=Gauge32
_HipsOutAHSPI_Object=MibTableColumn
hipsOutAHSPI=_HipsOutAHSPI_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,13),_HipsOutAHSPI_Type())
hipsOutAHSPI.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsOutAHSPI.setStatus(_A)
_HipsOutESPSPI_Type=Gauge32
_HipsOutESPSPI_Object=MibTableColumn
hipsOutESPSPI=_HipsOutESPSPI_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,14),_HipsOutESPSPI_Type())
hipsOutESPSPI.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsOutESPSPI.setStatus(_A)
_HipsInAhHexKeyString_Type=DisplayString
_HipsInAhHexKeyString_Object=MibTableColumn
hipsInAhHexKeyString=_HipsInAhHexKeyString_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,15),_HipsInAhHexKeyString_Type())
hipsInAhHexKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsInAhHexKeyString.setStatus(_A)
_HipsInEspCipherHexKeyString_Type=DisplayString
_HipsInEspCipherHexKeyString_Object=MibTableColumn
hipsInEspCipherHexKeyString=_HipsInEspCipherHexKeyString_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,16),_HipsInEspCipherHexKeyString_Type())
hipsInEspCipherHexKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsInEspCipherHexKeyString.setStatus(_A)
_HipsInEspAuthenHexKeyString_Type=DisplayString
_HipsInEspAuthenHexKeyString_Object=MibTableColumn
hipsInEspAuthenHexKeyString=_HipsInEspAuthenHexKeyString_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,17),_HipsInEspAuthenHexKeyString_Type())
hipsInEspAuthenHexKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsInEspAuthenHexKeyString.setStatus(_A)
_HipsInAhStringKeyString_Type=DisplayString
_HipsInAhStringKeyString_Object=MibTableColumn
hipsInAhStringKeyString=_HipsInAhStringKeyString_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,18),_HipsInAhStringKeyString_Type())
hipsInAhStringKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsInAhStringKeyString.setStatus(_A)
_HipsInEspStringKeyString_Type=DisplayString
_HipsInEspStringKeyString_Object=MibTableColumn
hipsInEspStringKeyString=_HipsInEspStringKeyString_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,19),_HipsInEspStringKeyString_Type())
hipsInEspStringKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsInEspStringKeyString.setStatus(_A)
_HipsOutAhHexKeyString_Type=DisplayString
_HipsOutAhHexKeyString_Object=MibTableColumn
hipsOutAhHexKeyString=_HipsOutAhHexKeyString_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,20),_HipsOutAhHexKeyString_Type())
hipsOutAhHexKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsOutAhHexKeyString.setStatus(_A)
_HipsOutEspCipherHexKeyString_Type=DisplayString
_HipsOutEspCipherHexKeyString_Object=MibTableColumn
hipsOutEspCipherHexKeyString=_HipsOutEspCipherHexKeyString_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,21),_HipsOutEspCipherHexKeyString_Type())
hipsOutEspCipherHexKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsOutEspCipherHexKeyString.setStatus(_A)
_HipsOutEspAuthenHexKeyString_Type=DisplayString
_HipsOutEspAuthenHexKeyString_Object=MibTableColumn
hipsOutEspAuthenHexKeyString=_HipsOutEspAuthenHexKeyString_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,22),_HipsOutEspAuthenHexKeyString_Type())
hipsOutEspAuthenHexKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsOutEspAuthenHexKeyString.setStatus(_A)
_HipsOutAhStringKeyString_Type=DisplayString
_HipsOutAhStringKeyString_Object=MibTableColumn
hipsOutAhStringKeyString=_HipsOutAhStringKeyString_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,23),_HipsOutAhStringKeyString_Type())
hipsOutAhStringKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsOutAhStringKeyString.setStatus(_A)
_HipsOutEspStringKeyString_Type=DisplayString
_HipsOutEspStringKeyString_Object=MibTableColumn
hipsOutEspStringKeyString=_HipsOutEspStringKeyString_Object((1,3,6,1,4,1,43,45,1,2,33,2,4,1,24),_HipsOutEspStringKeyString_Type())
hipsOutEspStringKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsOutEspStringKeyString.setStatus(_A)
_HipsTransformNameSetTable_Object=MibTable
hipsTransformNameSetTable=_HipsTransformNameSetTable_Object((1,3,6,1,4,1,43,45,1,2,33,2,5))
if mibBuilder.loadTexts:hipsTransformNameSetTable.setStatus(_A)
_HipsTransformNameSetEntry_Object=MibTableRow
hipsTransformNameSetEntry=_HipsTransformNameSetEntry_Object((1,3,6,1,4,1,43,45,1,2,33,2,5,1))
hipsTransformNameSetEntry.setIndexNames((0,_D,_i))
if mibBuilder.loadTexts:hipsTransformNameSetEntry.setStatus(_A)
_HipsTransformName_Type=DisplayString
_HipsTransformName_Object=MibTableColumn
hipsTransformName=_HipsTransformName_Object((1,3,6,1,4,1,43,45,1,2,33,2,5,1,1),_HipsTransformName_Type())
hipsTransformName.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsTransformName.setStatus(_A)
class _HipsTransformMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tunnel',1),('transport',2)))
_HipsTransformMode_Type.__name__=_C
_HipsTransformMode_Object=MibTableColumn
hipsTransformMode=_HipsTransformMode_Object((1,3,6,1,4,1,43,45,1,2,33,2,5,1,2),_HipsTransformMode_Type())
hipsTransformMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsTransformMode.setStatus(_A)
class _HipsTransformProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('ipsecNone',1),('ipsecAhNew',2),('ipsecAhEspNew',3),('ipsecAhEspOld',4),('ipsecAhOld',5),('ipsecEspNew',6),('ipsecEspAhNew',7),('ipsecEspAhOld',8),('ipsecEspOld',9)))
_HipsTransformProtocol_Type.__name__=_C
_HipsTransformProtocol_Object=MibTableColumn
hipsTransformProtocol=_HipsTransformProtocol_Object((1,3,6,1,4,1,43,45,1,2,33,2,5,1,3),_HipsTransformProtocol_Type())
hipsTransformProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsTransformProtocol.setStatus(_A)
class _HipsAH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_M,8)))
_HipsAH_Type.__name__=_C
_HipsAH_Object=MibTableColumn
hipsAH=_HipsAH_Object((1,3,6,1,4,1,43,45,1,2,33,2,5,1,4),_HipsAH_Type())
hipsAH.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsAH.setStatus(_A)
class _HipsEespEn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_T,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_Z,7),(_a,8)))
_HipsEespEn_Type.__name__=_C
_HipsEespEn_Object=MibTableColumn
hipsEespEn=_HipsEespEn_Object((1,3,6,1,4,1,43,45,1,2,33,2,5,1,5),_HipsEespEn_Type())
hipsEespEn.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsEespEn.setStatus(_A)
class _HipsEspAu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_M,8)))
_HipsEspAu_Type.__name__=_C
_HipsEspAu_Object=MibTableColumn
hipsEspAu=_HipsEspAu_Object((1,3,6,1,4,1,43,45,1,2,33,2,5,1,6),_HipsEspAu_Type())
hipsEspAu.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsEspAu.setStatus(_A)
_HipsIsCardTransform_Type=TruthValue
_HipsIsCardTransform_Object=MibTableColumn
hipsIsCardTransform=_HipsIsCardTransform_Object((1,3,6,1,4,1,43,45,1,2,33,2,5,1,7),_HipsIsCardTransform_Type())
hipsIsCardTransform.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsIsCardTransform.setStatus(_A)
_HipsNDECInfoTable_Object=MibTable
hipsNDECInfoTable=_HipsNDECInfoTable_Object((1,3,6,1,4,1,43,45,1,2,33,2,6))
if mibBuilder.loadTexts:hipsNDECInfoTable.setStatus(_A)
_HipsNDECInfoEntry_Object=MibTableRow
hipsNDECInfoEntry=_HipsNDECInfoEntry_Object((1,3,6,1,4,1,43,45,1,2,33,2,6,1))
hipsNDECInfoEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hipsNDECInfoEntry.setStatus(_A)
class _HipsCardSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HipsCardSlot_Type.__name__=_C
_HipsCardSlot_Object=MibTableColumn
hipsCardSlot=_HipsCardSlot_Object((1,3,6,1,4,1,43,45,1,2,33,2,6,1,1),_HipsCardSlot_Type())
hipsCardSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsCardSlot.setStatus(_A)
_HipsInPac_Type=Counter32
_HipsInPac_Object=MibTableColumn
hipsInPac=_HipsInPac_Object((1,3,6,1,4,1,43,45,1,2,33,2,6,1,2),_HipsInPac_Type())
hipsInPac.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsInPac.setStatus(_A)
_HipsOutPac_Type=Counter32
_HipsOutPac_Object=MibTableColumn
hipsOutPac=_HipsOutPac_Object((1,3,6,1,4,1,43,45,1,2,33,2,6,1,3),_HipsOutPac_Type())
hipsOutPac.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsOutPac.setStatus(_A)
_HipsInByte_Type=Counter32
_HipsInByte_Object=MibTableColumn
hipsInByte=_HipsInByte_Object((1,3,6,1,4,1,43,45,1,2,33,2,6,1,4),_HipsInByte_Type())
hipsInByte.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsInByte.setStatus(_A)
_HipsOutByte_Type=Counter32
_HipsOutByte_Object=MibTableColumn
hipsOutByte=_HipsOutByte_Object((1,3,6,1,4,1,43,45,1,2,33,2,6,1,5),_HipsOutByte_Type())
hipsOutByte.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsOutByte.setStatus(_A)
_HipsDropPac_Type=Counter32
_HipsDropPac_Object=MibTableColumn
hipsDropPac=_HipsDropPac_Object((1,3,6,1,4,1,43,45,1,2,33,2,6,1,6),_HipsDropPac_Type())
hipsDropPac.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsDropPac.setStatus(_A)
class _HipsCardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ecStateInvalid',1),('ecStateReady',2),('ecStateResetting',3),('ecStateProgramUpdating',4),('ecStateDisable',5)))
_HipsCardStatus_Type.__name__=_C
_HipsCardStatus_Object=MibTableColumn
hipsCardStatus=_HipsCardStatus_Object((1,3,6,1,4,1,43,45,1,2,33,2,6,1,7),_HipsCardStatus_Type())
hipsCardStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsCardStatus.setStatus(_A)
_HipsCardHardVer_Type=DisplayString
_HipsCardHardVer_Object=MibTableColumn
hipsCardHardVer=_HipsCardHardVer_Object((1,3,6,1,4,1,43,45,1,2,33,2,6,1,8),_HipsCardHardVer_Type())
hipsCardHardVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsCardHardVer.setStatus(_A)
_HipsCardSoftVer_Type=DisplayString
_HipsCardSoftVer_Object=MibTableColumn
hipsCardSoftVer=_HipsCardSoftVer_Object((1,3,6,1,4,1,43,45,1,2,33,2,6,1,9),_HipsCardSoftVer_Type())
hipsCardSoftVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsCardSoftVer.setStatus(_A)
_HipsCardCPLDVer_Type=DisplayString
_HipsCardCPLDVer_Object=MibTableColumn
hipsCardCPLDVer=_HipsCardCPLDVer_Object((1,3,6,1,4,1,43,45,1,2,33,2,6,1,10),_HipsCardCPLDVer_Type())
hipsCardCPLDVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsCardCPLDVer.setStatus(_A)
class _HipsCardOperate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('cardClearStatic',1),('cardReset',2),('cardSynTime',3),('cardSysLogOn',4),('cardSysLogOff',5),('cardSysLogClear',6)))
_HipsCardOperate_Type.__name__=_C
_HipsCardOperate_Object=MibTableColumn
hipsCardOperate=_HipsCardOperate_Object((1,3,6,1,4,1,43,45,1,2,33,2,6,1,11),_HipsCardOperate_Type())
hipsCardOperate.setMaxAccess(_O)
if mibBuilder.loadTexts:hipsCardOperate.setStatus(_A)
_HipsDropPacInUnitTime_Type=Gauge32
_HipsDropPacInUnitTime_Object=MibTableColumn
hipsDropPacInUnitTime=_HipsDropPacInUnitTime_Object((1,3,6,1,4,1,43,45,1,2,33,2,6,1,12),_HipsDropPacInUnitTime_Type())
hipsDropPacInUnitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsDropPacInUnitTime.setStatus(_A)
_HipsNDECLeaf_ObjectIdentity=ObjectIdentity
hipsNDECLeaf=_HipsNDECLeaf_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,33,2,7))
_HipsNDECConnections_Type=Integer32
_HipsNDECConnections_Object=MibScalar
hipsNDECConnections=_HipsNDECConnections_Object((1,3,6,1,4,1,43,45,1,2,33,2,7,1),_HipsNDECConnections_Type())
hipsNDECConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:hipsNDECConnections.setStatus(_A)
_HipsNDECBackup_Type=Integer32
_HipsNDECBackup_Object=MibScalar
hipsNDECBackup=_HipsNDECBackup_Object((1,3,6,1,4,1,43,45,1,2,33,2,7,2),_HipsNDECBackup_Type())
hipsNDECBackup.setMaxAccess(_O)
if mibBuilder.loadTexts:hipsNDECBackup.setStatus(_A)
_HipsTraps_ObjectIdentity=ObjectIdentity
hipsTraps=_HipsTraps_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,33,2,8))
hipsNDECNormalResetTrap=NotificationType((1,3,6,1,4,1,43,45,1,2,33,2,8,1))
hipsNDECNormalResetTrap.setObjects(*((_D,_E),(_D,_j),(_D,_k),(_D,_l)))
if mibBuilder.loadTexts:hipsNDECNormalResetTrap.setStatus(_A)
hipsNDECStateChangeTrap=NotificationType((1,3,6,1,4,1,43,45,1,2,33,2,8,2))
hipsNDECStateChangeTrap.setObjects(*((_D,_E),(_D,_m)))
if mibBuilder.loadTexts:hipsNDECStateChangeTrap.setStatus(_A)
hipsNDECFlowTrap=NotificationType((1,3,6,1,4,1,43,45,1,2,33,2,8,3))
hipsNDECFlowTrap.setObjects(*((_D,_E),(_D,_n)))
if mibBuilder.loadTexts:hipsNDECFlowTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'huaweiNDEC':huaweiNDEC,'hipsNDECSAListTable':hipsNDECSAListTable,'hipsNDECSAListEntry':hipsNDECSAListEntry,_Q:hipsPeerIpAddr,_R:hipsProtocol,_S:hipsSPI,'hipsEncAlgorithm':hipsEncAlgorithm,'hipsAuthAlgorithm':hipsAuthAlgorithm,'hipsLocalIpAddr':hipsLocalIpAddr,'hipsSaLifeKBytes':hipsSaLifeKBytes,'hipsSaLifeSecond':hipsSaLifeSecond,'hipsByCard':hipsByCard,'hipsNegotiateSaMode':hipsNegotiateSaMode,'hipsExpBytes':hipsExpBytes,'hipsSoftBytes':hipsSoftBytes,'hipsExpTimeout':hipsExpTimeout,'hipsSoftTimeout':hipsSoftTimeout,'hikeSATable':hikeSATable,'hikeSAEntry':hikeSAEntry,_d:hikeConnId,'hikePeerIpAddr':hikePeerIpAddr,'hikeFlag':hikeFlag,'hikePhase':hikePhase,'hikeDoi':hikeDoi,'hikeClearSA':hikeClearSA,'hipsIKEPolicyTable':hipsIKEPolicyTable,'hipsIKEPolicyEntry':hipsIKEPolicyEntry,_f:hipsIsakmpPolPriority,'hipsIsakmpPolEncr':hipsIsakmpPolEncr,'hipsIsakmpPolHash':hipsIsakmpPolHash,'hipsIsakmpPolAuth':hipsIsakmpPolAuth,'hipsIsakmpPolGroup':hipsIsakmpPolGroup,'hipsIsakmpPolLifetime':hipsIsakmpPolLifetime,'hipsStaticCryptomapTable':hipsStaticCryptomapTable,'hipsStaticCryptomapEntry':hipsStaticCryptomapEntry,_g:hipsStaticCryptomapName,_h:hipsStaticCryptomapSN,'hipsStaticCryptomapNegMode':hipsStaticCryptomapNegMode,'hipsStaticCryptomapMatchAddr':hipsStaticCryptomapMatchAddr,'hipsStaticCryptomapPeerIpAddr':hipsStaticCryptomapPeerIpAddr,'hipsStaticCryptomapTransforName':hipsStaticCryptomapTransforName,'hipsStaticCryptomapLifetime':hipsStaticCryptomapLifetime,'hipsStaticCryptomapLifesize':hipsStaticCryptomapLifesize,'hipsStaticCryptomapLocalIpAddr':hipsStaticCryptomapLocalIpAddr,'hipsIfNameUsed':hipsIfNameUsed,'hipsInAHSPI':hipsInAHSPI,'hipsInESPSPI':hipsInESPSPI,'hipsOutAHSPI':hipsOutAHSPI,'hipsOutESPSPI':hipsOutESPSPI,'hipsInAhHexKeyString':hipsInAhHexKeyString,'hipsInEspCipherHexKeyString':hipsInEspCipherHexKeyString,'hipsInEspAuthenHexKeyString':hipsInEspAuthenHexKeyString,'hipsInAhStringKeyString':hipsInAhStringKeyString,'hipsInEspStringKeyString':hipsInEspStringKeyString,'hipsOutAhHexKeyString':hipsOutAhHexKeyString,'hipsOutEspCipherHexKeyString':hipsOutEspCipherHexKeyString,'hipsOutEspAuthenHexKeyString':hipsOutEspAuthenHexKeyString,'hipsOutAhStringKeyString':hipsOutAhStringKeyString,'hipsOutEspStringKeyString':hipsOutEspStringKeyString,'hipsTransformNameSetTable':hipsTransformNameSetTable,'hipsTransformNameSetEntry':hipsTransformNameSetEntry,_i:hipsTransformName,'hipsTransformMode':hipsTransformMode,'hipsTransformProtocol':hipsTransformProtocol,'hipsAH':hipsAH,'hipsEespEn':hipsEespEn,'hipsEspAu':hipsEspAu,'hipsIsCardTransform':hipsIsCardTransform,'hipsNDECInfoTable':hipsNDECInfoTable,'hipsNDECInfoEntry':hipsNDECInfoEntry,_E:hipsCardSlot,'hipsInPac':hipsInPac,'hipsOutPac':hipsOutPac,'hipsInByte':hipsInByte,'hipsOutByte':hipsOutByte,'hipsDropPac':hipsDropPac,_m:hipsCardStatus,_j:hipsCardHardVer,_k:hipsCardSoftVer,_l:hipsCardCPLDVer,'hipsCardOperate':hipsCardOperate,_n:hipsDropPacInUnitTime,'hipsNDECLeaf':hipsNDECLeaf,'hipsNDECConnections':hipsNDECConnections,'hipsNDECBackup':hipsNDECBackup,'hipsTraps':hipsTraps,'hipsNDECNormalResetTrap':hipsNDECNormalResetTrap,'hipsNDECStateChangeTrap':hipsNDECStateChangeTrap,'hipsNDECFlowTrap':hipsNDECFlowTrap})