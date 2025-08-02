_k='hm2VpnCertificateIndex'
_j='read-write'
_i='hm2VpnTrafficSelIndex'
_h='packets'
_g='hm2VpnConnInfoTunnelIndex'
_f='re-keying'
_e='aes256'
_d='aes192'
_c='aes128'
_b='hmacsha512'
_a='hmacsha384'
_Z='hmacsha256'
_Y='hmacsha1'
_X='hmacmd5'
_W='ecp521'
_V='ecp384'
_U='ecp256'
_T='modp4096'
_S='modp3072'
_R='modp2048'
_Q='modp1536'
_P='modp1024'
_O='address'
_N='pkcs12'
_M='TruthValue'
_L='HmLargeDisplayString'
_K='hm2VpnConnOperStatus'
_J='seconds'
_I='not-accessible'
_H='hm2VpnConnIndex'
_G='any'
_F='HM2-VPN-MIB'
_E='Integer32'
_D='DisplayString'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmLargeDisplayString,HmTimeSeconds1970,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_L,'HmTimeSeconds1970','hm2ConfigurationMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention',_M)
hm2VpnMib=ModuleIdentity((1,3,6,1,4,1,248,11,120))
if mibBuilder.loadTexts:hm2VpnMib.setRevisions(('2014-03-14 12:00',))
_Hm2VpnMibNotifications_ObjectIdentity=ObjectIdentity
hm2VpnMibNotifications=_Hm2VpnMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,120,0))
_Hm2VpnMibObjects_ObjectIdentity=ObjectIdentity
hm2VpnMibObjects=_Hm2VpnMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,120,1))
_Hm2VpnGeneralGroup_ObjectIdentity=ObjectIdentity
hm2VpnGeneralGroup=_Hm2VpnGeneralGroup_ObjectIdentity((1,3,6,1,4,1,248,11,120,1,1))
_Hm2VpnConnectionGroup_ObjectIdentity=ObjectIdentity
hm2VpnConnectionGroup=_Hm2VpnConnectionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,120,1,2))
class _Hm2VpnConnMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Hm2VpnConnMax_Type.__name__=_E
_Hm2VpnConnMax_Object=MibScalar
hm2VpnConnMax=_Hm2VpnConnMax_Object((1,3,6,1,4,1,248,11,120,1,2,1),_Hm2VpnConnMax_Type())
hm2VpnConnMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnMax.setStatus(_A)
class _Hm2VpnConnActiveMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Hm2VpnConnActiveMax_Type.__name__=_E
_Hm2VpnConnActiveMax_Object=MibScalar
hm2VpnConnActiveMax=_Hm2VpnConnActiveMax_Object((1,3,6,1,4,1,248,11,120,1,2,2),_Hm2VpnConnActiveMax_Type())
hm2VpnConnActiveMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnActiveMax.setStatus(_A)
class _Hm2VpnConnNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Hm2VpnConnNext_Type.__name__=_E
_Hm2VpnConnNext_Object=MibScalar
hm2VpnConnNext=_Hm2VpnConnNext_Object((1,3,6,1,4,1,248,11,120,1,2,3),_Hm2VpnConnNext_Type())
hm2VpnConnNext.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnNext.setStatus(_A)
_Hm2VpnConnTable_Object=MibTable
hm2VpnConnTable=_Hm2VpnConnTable_Object((1,3,6,1,4,1,248,11,120,1,2,10))
if mibBuilder.loadTexts:hm2VpnConnTable.setStatus(_A)
_Hm2VpnConnEntry_Object=MibTableRow
hm2VpnConnEntry=_Hm2VpnConnEntry_Object((1,3,6,1,4,1,248,11,120,1,2,10,1))
hm2VpnConnEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:hm2VpnConnEntry.setStatus(_A)
class _Hm2VpnConnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Hm2VpnConnIndex_Type.__name__=_E
_Hm2VpnConnIndex_Object=MibTableColumn
hm2VpnConnIndex=_Hm2VpnConnIndex_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,1),_Hm2VpnConnIndex_Type())
hm2VpnConnIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hm2VpnConnIndex.setStatus(_A)
class _Hm2VpnConnIkeVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ike',1),('ikev1',2),('ikev2',3)))
_Hm2VpnConnIkeVersion_Type.__name__=_E
_Hm2VpnConnIkeVersion_Object=MibTableColumn
hm2VpnConnIkeVersion=_Hm2VpnConnIkeVersion_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,2),_Hm2VpnConnIkeVersion_Type())
hm2VpnConnIkeVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeVersion.setStatus(_A)
class _Hm2VpnConnIkeStartup_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('initiator',1),('responder',2)))
_Hm2VpnConnIkeStartup_Type.__name__=_E
_Hm2VpnConnIkeStartup_Object=MibTableColumn
hm2VpnConnIkeStartup=_Hm2VpnConnIkeStartup_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,3),_Hm2VpnConnIkeStartup_Type())
hm2VpnConnIkeStartup.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeStartup.setStatus(_A)
class _Hm2VpnConnIkeLifetime_Type(Integer32):defaultValue=28800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,86400))
_Hm2VpnConnIkeLifetime_Type.__name__=_E
_Hm2VpnConnIkeLifetime_Object=MibTableColumn
hm2VpnConnIkeLifetime=_Hm2VpnConnIkeLifetime_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,4),_Hm2VpnConnIkeLifetime_Type())
hm2VpnConnIkeLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeLifetime.setStatus(_A)
class _Hm2VpnConnIkeDpdTimeout_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_Hm2VpnConnIkeDpdTimeout_Type.__name__=_E
_Hm2VpnConnIkeDpdTimeout_Object=MibTableColumn
hm2VpnConnIkeDpdTimeout=_Hm2VpnConnIkeDpdTimeout_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,5),_Hm2VpnConnIkeDpdTimeout_Type())
hm2VpnConnIkeDpdTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeDpdTimeout.setStatus(_A)
class _Hm2VpnConnIkeLocalAddr_Type(DisplayString):defaultValue=OctetString(_G);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnConnIkeLocalAddr_Type.__name__=_D
_Hm2VpnConnIkeLocalAddr_Object=MibTableColumn
hm2VpnConnIkeLocalAddr=_Hm2VpnConnIkeLocalAddr_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,6),_Hm2VpnConnIkeLocalAddr_Type())
hm2VpnConnIkeLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeLocalAddr.setStatus(_A)
class _Hm2VpnConnIkeRemoteAddr_Type(DisplayString):defaultValue=OctetString(_G);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnConnIkeRemoteAddr_Type.__name__=_D
_Hm2VpnConnIkeRemoteAddr_Object=MibTableColumn
hm2VpnConnIkeRemoteAddr=_Hm2VpnConnIkeRemoteAddr_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,7),_Hm2VpnConnIkeRemoteAddr_Type())
hm2VpnConnIkeRemoteAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeRemoteAddr.setStatus(_A)
class _Hm2VpnConnIkeAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('psk',1),('individualx509',2),(_N,3)))
_Hm2VpnConnIkeAuthType_Type.__name__=_E
_Hm2VpnConnIkeAuthType_Object=MibTableColumn
hm2VpnConnIkeAuthType=_Hm2VpnConnIkeAuthType_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,8),_Hm2VpnConnIkeAuthType_Type())
hm2VpnConnIkeAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeAuthType.setStatus(_A)
class _Hm2VpnConnIkeAuthMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('main',1),('aggressive',2)))
_Hm2VpnConnIkeAuthMode_Type.__name__=_E
_Hm2VpnConnIkeAuthMode_Object=MibTableColumn
hm2VpnConnIkeAuthMode=_Hm2VpnConnIkeAuthMode_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,9),_Hm2VpnConnIkeAuthMode_Type())
hm2VpnConnIkeAuthMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeAuthMode.setStatus(_A)
class _Hm2VpnConnIkeAuthCertCA_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnConnIkeAuthCertCA_Type.__name__=_D
_Hm2VpnConnIkeAuthCertCA_Object=MibTableColumn
hm2VpnConnIkeAuthCertCA=_Hm2VpnConnIkeAuthCertCA_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,10),_Hm2VpnConnIkeAuthCertCA_Type())
hm2VpnConnIkeAuthCertCA.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeAuthCertCA.setStatus(_A)
class _Hm2VpnConnIkeAuthCertRemote_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnConnIkeAuthCertRemote_Type.__name__=_D
_Hm2VpnConnIkeAuthCertRemote_Object=MibTableColumn
hm2VpnConnIkeAuthCertRemote=_Hm2VpnConnIkeAuthCertRemote_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,11),_Hm2VpnConnIkeAuthCertRemote_Type())
hm2VpnConnIkeAuthCertRemote.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeAuthCertRemote.setStatus(_A)
class _Hm2VpnConnIkeAuthCertLocal_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnConnIkeAuthCertLocal_Type.__name__=_D
_Hm2VpnConnIkeAuthCertLocal_Object=MibTableColumn
hm2VpnConnIkeAuthCertLocal=_Hm2VpnConnIkeAuthCertLocal_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,12),_Hm2VpnConnIkeAuthCertLocal_Type())
hm2VpnConnIkeAuthCertLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeAuthCertLocal.setStatus(_A)
class _Hm2VpnConnIkeAuthPrivKey_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnConnIkeAuthPrivKey_Type.__name__=_D
_Hm2VpnConnIkeAuthPrivKey_Object=MibTableColumn
hm2VpnConnIkeAuthPrivKey=_Hm2VpnConnIkeAuthPrivKey_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,13),_Hm2VpnConnIkeAuthPrivKey_Type())
hm2VpnConnIkeAuthPrivKey.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeAuthPrivKey.setStatus(_A)
class _Hm2VpnConnIkeAuthPasswd_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnConnIkeAuthPasswd_Type.__name__=_D
_Hm2VpnConnIkeAuthPasswd_Object=MibTableColumn
hm2VpnConnIkeAuthPasswd=_Hm2VpnConnIkeAuthPasswd_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,14),_Hm2VpnConnIkeAuthPasswd_Type())
hm2VpnConnIkeAuthPasswd.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeAuthPasswd.setStatus(_A)
class _Hm2VpnConnIkeAuthPsk_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnConnIkeAuthPsk_Type.__name__=_D
_Hm2VpnConnIkeAuthPsk_Object=MibTableColumn
hm2VpnConnIkeAuthPsk=_Hm2VpnConnIkeAuthPsk_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,15),_Hm2VpnConnIkeAuthPsk_Type())
hm2VpnConnIkeAuthPsk.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeAuthPsk.setStatus(_A)
class _Hm2VpnConnIkeAuthLocId_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnConnIkeAuthLocId_Type.__name__=_D
_Hm2VpnConnIkeAuthLocId_Object=MibTableColumn
hm2VpnConnIkeAuthLocId=_Hm2VpnConnIkeAuthLocId_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,16),_Hm2VpnConnIkeAuthLocId_Type())
hm2VpnConnIkeAuthLocId.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeAuthLocId.setStatus(_A)
class _Hm2VpnConnIkeAuthLocType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('default',1),(_O,2),('id',3)))
_Hm2VpnConnIkeAuthLocType_Type.__name__=_E
_Hm2VpnConnIkeAuthLocType_Object=MibTableColumn
hm2VpnConnIkeAuthLocType=_Hm2VpnConnIkeAuthLocType_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,17),_Hm2VpnConnIkeAuthLocType_Type())
hm2VpnConnIkeAuthLocType.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeAuthLocType.setStatus(_A)
class _Hm2VpnConnIkeAuthRemId_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnConnIkeAuthRemId_Type.__name__=_D
_Hm2VpnConnIkeAuthRemId_Object=MibTableColumn
hm2VpnConnIkeAuthRemId=_Hm2VpnConnIkeAuthRemId_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,18),_Hm2VpnConnIkeAuthRemId_Type())
hm2VpnConnIkeAuthRemId.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeAuthRemId.setStatus(_A)
class _Hm2VpnConnIkeAuthRemType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_O,2),('id',3)))
_Hm2VpnConnIkeAuthRemType_Type.__name__=_E
_Hm2VpnConnIkeAuthRemType_Object=MibTableColumn
hm2VpnConnIkeAuthRemType=_Hm2VpnConnIkeAuthRemType_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,19),_Hm2VpnConnIkeAuthRemType_Type())
hm2VpnConnIkeAuthRemType.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeAuthRemType.setStatus(_A)
class _Hm2VpnConnIkeAlgDh_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9)))
_Hm2VpnConnIkeAlgDh_Type.__name__=_E
_Hm2VpnConnIkeAlgDh_Object=MibTableColumn
hm2VpnConnIkeAlgDh=_Hm2VpnConnIkeAlgDh_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,20),_Hm2VpnConnIkeAlgDh_Type())
hm2VpnConnIkeAlgDh.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeAlgDh.setStatus(_A)
class _Hm2VpnConnIkeAlgMac_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6)))
_Hm2VpnConnIkeAlgMac_Type.__name__=_E
_Hm2VpnConnIkeAlgMac_Object=MibTableColumn
hm2VpnConnIkeAlgMac=_Hm2VpnConnIkeAlgMac_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,21),_Hm2VpnConnIkeAlgMac_Type())
hm2VpnConnIkeAlgMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeAlgMac.setStatus(_A)
class _Hm2VpnConnIkeAlgEncr_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('des',2),('des3',3),(_c,4),(_d,5),(_e,6)))
_Hm2VpnConnIkeAlgEncr_Type.__name__=_E
_Hm2VpnConnIkeAlgEncr_Object=MibTableColumn
hm2VpnConnIkeAlgEncr=_Hm2VpnConnIkeAlgEncr_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,22),_Hm2VpnConnIkeAlgEncr_Type())
hm2VpnConnIkeAlgEncr.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeAlgEncr.setStatus(_A)
class _Hm2VpnConnIkeReAuth_Type(TruthValue):defaultValue=2
_Hm2VpnConnIkeReAuth_Type.__name__=_M
_Hm2VpnConnIkeReAuth_Object=MibTableColumn
hm2VpnConnIkeReAuth=_Hm2VpnConnIkeReAuth_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,23),_Hm2VpnConnIkeReAuth_Type())
hm2VpnConnIkeReAuth.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIkeReAuth.setStatus(_A)
class _Hm2VpnConnIpsecMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('tunnel',1))
_Hm2VpnConnIpsecMode_Type.__name__=_E
_Hm2VpnConnIpsecMode_Object=MibTableColumn
hm2VpnConnIpsecMode=_Hm2VpnConnIpsecMode_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,24),_Hm2VpnConnIpsecMode_Type())
hm2VpnConnIpsecMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIpsecMode.setStatus(_A)
class _Hm2VpnConnIpsecLifetime_Type(Integer32):defaultValue=3600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,28800))
_Hm2VpnConnIpsecLifetime_Type.__name__=_E
_Hm2VpnConnIpsecLifetime_Object=MibTableColumn
hm2VpnConnIpsecLifetime=_Hm2VpnConnIpsecLifetime_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,25),_Hm2VpnConnIpsecLifetime_Type())
hm2VpnConnIpsecLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIpsecLifetime.setStatus(_A)
class _Hm2VpnConnMargintime_Type(Integer32):defaultValue=150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
_Hm2VpnConnMargintime_Type.__name__=_E
_Hm2VpnConnMargintime_Object=MibTableColumn
hm2VpnConnMargintime=_Hm2VpnConnMargintime_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,26),_Hm2VpnConnMargintime_Type())
hm2VpnConnMargintime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnMargintime.setStatus(_A)
class _Hm2VpnConnIpsecAlgDh_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),('none',7),(_U,8),(_V,9),(_W,10)))
_Hm2VpnConnIpsecAlgDh_Type.__name__=_E
_Hm2VpnConnIpsecAlgDh_Object=MibTableColumn
hm2VpnConnIpsecAlgDh=_Hm2VpnConnIpsecAlgDh_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,27),_Hm2VpnConnIpsecAlgDh_Type())
hm2VpnConnIpsecAlgDh.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIpsecAlgDh.setStatus(_A)
class _Hm2VpnConnIpsecAlgMac_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6)))
_Hm2VpnConnIpsecAlgMac_Type.__name__=_E
_Hm2VpnConnIpsecAlgMac_Object=MibTableColumn
hm2VpnConnIpsecAlgMac=_Hm2VpnConnIpsecAlgMac_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,28),_Hm2VpnConnIpsecAlgMac_Type())
hm2VpnConnIpsecAlgMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIpsecAlgMac.setStatus(_A)
class _Hm2VpnConnIpsecAlgEncr_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*((_G,1),('des',2),('des3',3),(_c,4),(_d,5),(_e,6),('aes128ctr',7),('aes192ctr',8),('aes256ctr',9),('aes128gcm64',10),('aes128gcm96',11),('aes128gcm128',12),('aes192gcm64',13),('aes192gcm96',14),('aes192gcm128',15),('aes256gcm64',16),('aes256gcm96',17),('aes256gcm128',18)))
_Hm2VpnConnIpsecAlgEncr_Type.__name__=_E
_Hm2VpnConnIpsecAlgEncr_Object=MibTableColumn
hm2VpnConnIpsecAlgEncr=_Hm2VpnConnIpsecAlgEncr_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,29),_Hm2VpnConnIpsecAlgEncr_Type())
hm2VpnConnIpsecAlgEncr.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnIpsecAlgEncr.setStatus(_A)
class _Hm2VpnConnOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('up',1),('down',2),('negotiation',3),('constructing',4),('dormant',5),(_f,6)))
_Hm2VpnConnOperStatus_Type.__name__=_E
_Hm2VpnConnOperStatus_Object=MibTableColumn
hm2VpnConnOperStatus=_Hm2VpnConnOperStatus_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,30),_Hm2VpnConnOperStatus_Type())
hm2VpnConnOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnOperStatus.setStatus(_A)
class _Hm2VpnConnDesc_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnConnDesc_Type.__name__=_D
_Hm2VpnConnDesc_Object=MibTableColumn
hm2VpnConnDesc=_Hm2VpnConnDesc_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,31),_Hm2VpnConnDesc_Type())
hm2VpnConnDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnDesc.setStatus(_A)
class _Hm2VpnConnLastError_Type(HmLargeDisplayString):defaultValue=OctetString('');subtypeSpec=HmLargeDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_Hm2VpnConnLastError_Type.__name__=_L
_Hm2VpnConnLastError_Object=MibTableColumn
hm2VpnConnLastError=_Hm2VpnConnLastError_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,32),_Hm2VpnConnLastError_Type())
hm2VpnConnLastError.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnLastError.setStatus(_A)
class _Hm2VpnConnDebug_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('informational',0),('unhandled',1)))
_Hm2VpnConnDebug_Type.__name__='Bits'
_Hm2VpnConnDebug_Object=MibTableColumn
hm2VpnConnDebug=_Hm2VpnConnDebug_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,33),_Hm2VpnConnDebug_Type())
hm2VpnConnDebug.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnDebug.setStatus(_A)
_Hm2VpnConnRowStatus_Type=RowStatus
_Hm2VpnConnRowStatus_Object=MibTableColumn
hm2VpnConnRowStatus=_Hm2VpnConnRowStatus_Object((1,3,6,1,4,1,248,11,120,1,2,10,1,34),_Hm2VpnConnRowStatus_Type())
hm2VpnConnRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnConnRowStatus.setStatus(_A)
_Hm2VpnConnInfoTable_Object=MibTable
hm2VpnConnInfoTable=_Hm2VpnConnInfoTable_Object((1,3,6,1,4,1,248,11,120,1,2,15))
if mibBuilder.loadTexts:hm2VpnConnInfoTable.setStatus(_A)
_Hm2VpnConnInfoEntry_Object=MibTableRow
hm2VpnConnInfoEntry=_Hm2VpnConnInfoEntry_Object((1,3,6,1,4,1,248,11,120,1,2,15,1))
hm2VpnConnInfoEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:hm2VpnConnInfoEntry.setStatus(_A)
class _Hm2VpnConnInfoIkeVersionUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ikev1',1),('ikev2',2)))
_Hm2VpnConnInfoIkeVersionUsed_Type.__name__=_E
_Hm2VpnConnInfoIkeVersionUsed_Object=MibTableColumn
hm2VpnConnInfoIkeVersionUsed=_Hm2VpnConnInfoIkeVersionUsed_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,1),_Hm2VpnConnInfoIkeVersionUsed_Type())
hm2VpnConnInfoIkeVersionUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIkeVersionUsed.setStatus(_A)
class _Hm2VpnConnInfoIkeProposal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnConnInfoIkeProposal_Type.__name__=_D
_Hm2VpnConnInfoIkeProposal_Object=MibTableColumn
hm2VpnConnInfoIkeProposal=_Hm2VpnConnInfoIkeProposal_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,2),_Hm2VpnConnInfoIkeProposal_Type())
hm2VpnConnInfoIkeProposal.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIkeProposal.setStatus(_A)
class _Hm2VpnConnInfoIpsecProposal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnConnInfoIpsecProposal_Type.__name__=_D
_Hm2VpnConnInfoIpsecProposal_Object=MibTableColumn
hm2VpnConnInfoIpsecProposal=_Hm2VpnConnInfoIpsecProposal_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,3),_Hm2VpnConnInfoIpsecProposal_Type())
hm2VpnConnInfoIpsecProposal.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIpsecProposal.setStatus(_A)
class _Hm2VpnConnInfoLocalHost_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnConnInfoLocalHost_Type.__name__=_D
_Hm2VpnConnInfoLocalHost_Object=MibTableColumn
hm2VpnConnInfoLocalHost=_Hm2VpnConnInfoLocalHost_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,4),_Hm2VpnConnInfoLocalHost_Type())
hm2VpnConnInfoLocalHost.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoLocalHost.setStatus(_A)
class _Hm2VpnConnInfoRemoteHost_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnConnInfoRemoteHost_Type.__name__=_D
_Hm2VpnConnInfoRemoteHost_Object=MibTableColumn
hm2VpnConnInfoRemoteHost=_Hm2VpnConnInfoRemoteHost_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,5),_Hm2VpnConnInfoRemoteHost_Type())
hm2VpnConnInfoRemoteHost.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoRemoteHost.setStatus(_A)
_Hm2VpnConnInfoEstablished_Type=Unsigned32
_Hm2VpnConnInfoEstablished_Object=MibTableColumn
hm2VpnConnInfoEstablished=_Hm2VpnConnInfoEstablished_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,6),_Hm2VpnConnInfoEstablished_Type())
hm2VpnConnInfoEstablished.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoEstablished.setStatus(_A)
_Hm2VpnConnInfoIKEReauth_Type=Unsigned32
_Hm2VpnConnInfoIKEReauth_Object=MibTableColumn
hm2VpnConnInfoIKEReauth=_Hm2VpnConnInfoIKEReauth_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,7),_Hm2VpnConnInfoIKEReauth_Type())
hm2VpnConnInfoIKEReauth.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIKEReauth.setStatus(_A)
_Hm2VpnConnInfoIKERekeying_Type=Unsigned32
_Hm2VpnConnInfoIKERekeying_Object=MibTableColumn
hm2VpnConnInfoIKERekeying=_Hm2VpnConnInfoIKERekeying_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,8),_Hm2VpnConnInfoIKERekeying_Type())
hm2VpnConnInfoIKERekeying.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIKERekeying.setStatus(_A)
_Hm2VpnConnInfoIpsecRekeying_Type=Unsigned32
_Hm2VpnConnInfoIpsecRekeying_Object=MibTableColumn
hm2VpnConnInfoIpsecRekeying=_Hm2VpnConnInfoIpsecRekeying_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,9),_Hm2VpnConnInfoIpsecRekeying_Type())
hm2VpnConnInfoIpsecRekeying.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIpsecRekeying.setStatus(_A)
_Hm2VpnConnInfoIpsecInBytes_Type=Counter64
_Hm2VpnConnInfoIpsecInBytes_Object=MibTableColumn
hm2VpnConnInfoIpsecInBytes=_Hm2VpnConnInfoIpsecInBytes_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,10),_Hm2VpnConnInfoIpsecInBytes_Type())
hm2VpnConnInfoIpsecInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIpsecInBytes.setStatus(_A)
_Hm2VpnConnInfoIpsecInPackets_Type=Counter64
_Hm2VpnConnInfoIpsecInPackets_Object=MibTableColumn
hm2VpnConnInfoIpsecInPackets=_Hm2VpnConnInfoIpsecInPackets_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,11),_Hm2VpnConnInfoIpsecInPackets_Type())
hm2VpnConnInfoIpsecInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIpsecInPackets.setStatus(_A)
_Hm2VpnConnInfoIpsecInUse_Type=Unsigned32
_Hm2VpnConnInfoIpsecInUse_Object=MibTableColumn
hm2VpnConnInfoIpsecInUse=_Hm2VpnConnInfoIpsecInUse_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,12),_Hm2VpnConnInfoIpsecInUse_Type())
hm2VpnConnInfoIpsecInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIpsecInUse.setStatus(_A)
_Hm2VpnConnInfoIpsecOutBytes_Type=Counter64
_Hm2VpnConnInfoIpsecOutBytes_Object=MibTableColumn
hm2VpnConnInfoIpsecOutBytes=_Hm2VpnConnInfoIpsecOutBytes_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,13),_Hm2VpnConnInfoIpsecOutBytes_Type())
hm2VpnConnInfoIpsecOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIpsecOutBytes.setStatus(_A)
_Hm2VpnConnInfoIpsecOutPackets_Type=Counter64
_Hm2VpnConnInfoIpsecOutPackets_Object=MibTableColumn
hm2VpnConnInfoIpsecOutPackets=_Hm2VpnConnInfoIpsecOutPackets_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,14),_Hm2VpnConnInfoIpsecOutPackets_Type())
hm2VpnConnInfoIpsecOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIpsecOutPackets.setStatus(_A)
_Hm2VpnConnInfoIpsecOutUse_Type=Unsigned32
_Hm2VpnConnInfoIpsecOutUse_Object=MibTableColumn
hm2VpnConnInfoIpsecOutUse=_Hm2VpnConnInfoIpsecOutUse_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,15),_Hm2VpnConnInfoIpsecOutUse_Type())
hm2VpnConnInfoIpsecOutUse.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIpsecOutUse.setStatus(_A)
class _Hm2VpnConnInfoIKEInitiatorSPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Hm2VpnConnInfoIKEInitiatorSPI_Type.__name__=_D
_Hm2VpnConnInfoIKEInitiatorSPI_Object=MibTableColumn
hm2VpnConnInfoIKEInitiatorSPI=_Hm2VpnConnInfoIKEInitiatorSPI_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,16),_Hm2VpnConnInfoIKEInitiatorSPI_Type())
hm2VpnConnInfoIKEInitiatorSPI.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIKEInitiatorSPI.setStatus(_A)
class _Hm2VpnConnInfoIKEResponderSPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Hm2VpnConnInfoIKEResponderSPI_Type.__name__=_D
_Hm2VpnConnInfoIKEResponderSPI_Object=MibTableColumn
hm2VpnConnInfoIKEResponderSPI=_Hm2VpnConnInfoIKEResponderSPI_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,17),_Hm2VpnConnInfoIKEResponderSPI_Type())
hm2VpnConnInfoIKEResponderSPI.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIKEResponderSPI.setStatus(_A)
class _Hm2VpnConnInfoIpsecInSPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Hm2VpnConnInfoIpsecInSPI_Type.__name__=_D
_Hm2VpnConnInfoIpsecInSPI_Object=MibTableColumn
hm2VpnConnInfoIpsecInSPI=_Hm2VpnConnInfoIpsecInSPI_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,18),_Hm2VpnConnInfoIpsecInSPI_Type())
hm2VpnConnInfoIpsecInSPI.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIpsecInSPI.setStatus(_A)
class _Hm2VpnConnInfoIpsecOutSPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Hm2VpnConnInfoIpsecOutSPI_Type.__name__=_D
_Hm2VpnConnInfoIpsecOutSPI_Object=MibTableColumn
hm2VpnConnInfoIpsecOutSPI=_Hm2VpnConnInfoIpsecOutSPI_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,19),_Hm2VpnConnInfoIpsecOutSPI_Type())
hm2VpnConnInfoIpsecOutSPI.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIpsecOutSPI.setStatus(_A)
_Hm2VpnConnInfoIpsecNumTunnel_Type=Unsigned32
_Hm2VpnConnInfoIpsecNumTunnel_Object=MibTableColumn
hm2VpnConnInfoIpsecNumTunnel=_Hm2VpnConnInfoIpsecNumTunnel_Object((1,3,6,1,4,1,248,11,120,1,2,15,1,20),_Hm2VpnConnInfoIpsecNumTunnel_Type())
hm2VpnConnInfoIpsecNumTunnel.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoIpsecNumTunnel.setStatus(_A)
_Hm2VpnConnInfoTunnelTable_Object=MibTable
hm2VpnConnInfoTunnelTable=_Hm2VpnConnInfoTunnelTable_Object((1,3,6,1,4,1,248,11,120,1,2,16))
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelTable.setStatus(_A)
_Hm2VpnConnInfoTunnelEntry_Object=MibTableRow
hm2VpnConnInfoTunnelEntry=_Hm2VpnConnInfoTunnelEntry_Object((1,3,6,1,4,1,248,11,120,1,2,16,1))
hm2VpnConnInfoTunnelEntry.setIndexNames((0,_F,_H),(0,_F,_g))
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelEntry.setStatus(_A)
class _Hm2VpnConnInfoTunnelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Hm2VpnConnInfoTunnelIndex_Type.__name__=_E
_Hm2VpnConnInfoTunnelIndex_Object=MibTableColumn
hm2VpnConnInfoTunnelIndex=_Hm2VpnConnInfoTunnelIndex_Object((1,3,6,1,4,1,248,11,120,1,2,16,1,1),_Hm2VpnConnInfoTunnelIndex_Type())
hm2VpnConnInfoTunnelIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelIndex.setStatus(_A)
class _Hm2VpnConnInfoTSelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_Hm2VpnConnInfoTSelIndex_Type.__name__=_E
_Hm2VpnConnInfoTSelIndex_Object=MibTableColumn
hm2VpnConnInfoTSelIndex=_Hm2VpnConnInfoTSelIndex_Object((1,3,6,1,4,1,248,11,120,1,2,16,1,2),_Hm2VpnConnInfoTSelIndex_Type())
hm2VpnConnInfoTSelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoTSelIndex.setStatus(_A)
class _Hm2VpnConnInfoTunnelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('unknown',0),('created',1),('routed',2),('installing',3),('installed',4),('updating',5),(_f,6),('re-keyed',7),('re-trying',8),('deleting',9),('destroying',10)))
_Hm2VpnConnInfoTunnelStatus_Type.__name__=_E
_Hm2VpnConnInfoTunnelStatus_Object=MibTableColumn
hm2VpnConnInfoTunnelStatus=_Hm2VpnConnInfoTunnelStatus_Object((1,3,6,1,4,1,248,11,120,1,2,16,1,3),_Hm2VpnConnInfoTunnelStatus_Type())
hm2VpnConnInfoTunnelStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelStatus.setStatus(_A)
_Hm2VpnConnInfoTunnelRekeying_Type=Unsigned32
_Hm2VpnConnInfoTunnelRekeying_Object=MibTableColumn
hm2VpnConnInfoTunnelRekeying=_Hm2VpnConnInfoTunnelRekeying_Object((1,3,6,1,4,1,248,11,120,1,2,16,1,4),_Hm2VpnConnInfoTunnelRekeying_Type())
hm2VpnConnInfoTunnelRekeying.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelRekeying.setStatus(_A)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelRekeying.setUnits(_J)
_Hm2VpnConnInfoTunnelInBytes_Type=Counter64
_Hm2VpnConnInfoTunnelInBytes_Object=MibTableColumn
hm2VpnConnInfoTunnelInBytes=_Hm2VpnConnInfoTunnelInBytes_Object((1,3,6,1,4,1,248,11,120,1,2,16,1,5),_Hm2VpnConnInfoTunnelInBytes_Type())
hm2VpnConnInfoTunnelInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelInBytes.setStatus(_A)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelInBytes.setUnits('bytes')
_Hm2VpnConnInfoTunnelInPackets_Type=Counter64
_Hm2VpnConnInfoTunnelInPackets_Object=MibTableColumn
hm2VpnConnInfoTunnelInPackets=_Hm2VpnConnInfoTunnelInPackets_Object((1,3,6,1,4,1,248,11,120,1,2,16,1,6),_Hm2VpnConnInfoTunnelInPackets_Type())
hm2VpnConnInfoTunnelInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelInPackets.setStatus(_A)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelInPackets.setUnits(_h)
_Hm2VpnConnInfoTunnelInUse_Type=Unsigned32
_Hm2VpnConnInfoTunnelInUse_Object=MibTableColumn
hm2VpnConnInfoTunnelInUse=_Hm2VpnConnInfoTunnelInUse_Object((1,3,6,1,4,1,248,11,120,1,2,16,1,7),_Hm2VpnConnInfoTunnelInUse_Type())
hm2VpnConnInfoTunnelInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelInUse.setStatus(_A)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelInUse.setUnits(_J)
_Hm2VpnConnInfoTunnelOutBytes_Type=Counter64
_Hm2VpnConnInfoTunnelOutBytes_Object=MibTableColumn
hm2VpnConnInfoTunnelOutBytes=_Hm2VpnConnInfoTunnelOutBytes_Object((1,3,6,1,4,1,248,11,120,1,2,16,1,8),_Hm2VpnConnInfoTunnelOutBytes_Type())
hm2VpnConnInfoTunnelOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelOutBytes.setStatus(_A)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelOutBytes.setUnits('bytes')
_Hm2VpnConnInfoTunnelOutPackets_Type=Counter64
_Hm2VpnConnInfoTunnelOutPackets_Object=MibTableColumn
hm2VpnConnInfoTunnelOutPackets=_Hm2VpnConnInfoTunnelOutPackets_Object((1,3,6,1,4,1,248,11,120,1,2,16,1,9),_Hm2VpnConnInfoTunnelOutPackets_Type())
hm2VpnConnInfoTunnelOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelOutPackets.setStatus(_A)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelOutPackets.setUnits(_h)
_Hm2VpnConnInfoTunnelOutUse_Type=Unsigned32
_Hm2VpnConnInfoTunnelOutUse_Object=MibTableColumn
hm2VpnConnInfoTunnelOutUse=_Hm2VpnConnInfoTunnelOutUse_Object((1,3,6,1,4,1,248,11,120,1,2,16,1,10),_Hm2VpnConnInfoTunnelOutUse_Type())
hm2VpnConnInfoTunnelOutUse.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelOutUse.setStatus(_A)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelOutUse.setUnits(_J)
class _Hm2VpnConnInfoTunnelInSPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Hm2VpnConnInfoTunnelInSPI_Type.__name__=_D
_Hm2VpnConnInfoTunnelInSPI_Object=MibTableColumn
hm2VpnConnInfoTunnelInSPI=_Hm2VpnConnInfoTunnelInSPI_Object((1,3,6,1,4,1,248,11,120,1,2,16,1,11),_Hm2VpnConnInfoTunnelInSPI_Type())
hm2VpnConnInfoTunnelInSPI.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelInSPI.setStatus(_A)
class _Hm2VpnConnInfoTunnelOutSPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Hm2VpnConnInfoTunnelOutSPI_Type.__name__=_D
_Hm2VpnConnInfoTunnelOutSPI_Object=MibTableColumn
hm2VpnConnInfoTunnelOutSPI=_Hm2VpnConnInfoTunnelOutSPI_Object((1,3,6,1,4,1,248,11,120,1,2,16,1,12),_Hm2VpnConnInfoTunnelOutSPI_Type())
hm2VpnConnInfoTunnelOutSPI.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelOutSPI.setStatus(_A)
class _Hm2VpnConnInfoTunnelLocalSel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Hm2VpnConnInfoTunnelLocalSel_Type.__name__=_D
_Hm2VpnConnInfoTunnelLocalSel_Object=MibTableColumn
hm2VpnConnInfoTunnelLocalSel=_Hm2VpnConnInfoTunnelLocalSel_Object((1,3,6,1,4,1,248,11,120,1,2,16,1,13),_Hm2VpnConnInfoTunnelLocalSel_Type())
hm2VpnConnInfoTunnelLocalSel.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelLocalSel.setStatus(_A)
class _Hm2VpnConnInfoTunnelRemoteSel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Hm2VpnConnInfoTunnelRemoteSel_Type.__name__=_D
_Hm2VpnConnInfoTunnelRemoteSel_Object=MibTableColumn
hm2VpnConnInfoTunnelRemoteSel=_Hm2VpnConnInfoTunnelRemoteSel_Object((1,3,6,1,4,1,248,11,120,1,2,16,1,14),_Hm2VpnConnInfoTunnelRemoteSel_Type())
hm2VpnConnInfoTunnelRemoteSel.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnConnInfoTunnelRemoteSel.setStatus(_A)
_Hm2VpnTrafficSelGroup_ObjectIdentity=ObjectIdentity
hm2VpnTrafficSelGroup=_Hm2VpnTrafficSelGroup_ObjectIdentity((1,3,6,1,4,1,248,11,120,1,3))
_Hm2VpnTrafficSelTable_Object=MibTable
hm2VpnTrafficSelTable=_Hm2VpnTrafficSelTable_Object((1,3,6,1,4,1,248,11,120,1,3,1))
if mibBuilder.loadTexts:hm2VpnTrafficSelTable.setStatus(_A)
_Hm2VpnTrafficSelEntry_Object=MibTableRow
hm2VpnTrafficSelEntry=_Hm2VpnTrafficSelEntry_Object((1,3,6,1,4,1,248,11,120,1,3,1,1))
hm2VpnTrafficSelEntry.setIndexNames((0,_F,_H),(0,_F,_i))
if mibBuilder.loadTexts:hm2VpnTrafficSelEntry.setStatus(_A)
class _Hm2VpnTrafficSelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Hm2VpnTrafficSelIndex_Type.__name__=_E
_Hm2VpnTrafficSelIndex_Object=MibTableColumn
hm2VpnTrafficSelIndex=_Hm2VpnTrafficSelIndex_Object((1,3,6,1,4,1,248,11,120,1,3,1,1,1),_Hm2VpnTrafficSelIndex_Type())
hm2VpnTrafficSelIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hm2VpnTrafficSelIndex.setStatus(_A)
class _Hm2VpnTrafficSelSrcAddr_Type(DisplayString):defaultValue=OctetString(_G);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Hm2VpnTrafficSelSrcAddr_Type.__name__=_D
_Hm2VpnTrafficSelSrcAddr_Object=MibTableColumn
hm2VpnTrafficSelSrcAddr=_Hm2VpnTrafficSelSrcAddr_Object((1,3,6,1,4,1,248,11,120,1,3,1,1,2),_Hm2VpnTrafficSelSrcAddr_Type())
hm2VpnTrafficSelSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnTrafficSelSrcAddr.setStatus(_A)
class _Hm2VpnTrafficSelDstAddr_Type(DisplayString):defaultValue=OctetString(_G);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Hm2VpnTrafficSelDstAddr_Type.__name__=_D
_Hm2VpnTrafficSelDstAddr_Object=MibTableColumn
hm2VpnTrafficSelDstAddr=_Hm2VpnTrafficSelDstAddr_Object((1,3,6,1,4,1,248,11,120,1,3,1,1,3),_Hm2VpnTrafficSelDstAddr_Type())
hm2VpnTrafficSelDstAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnTrafficSelDstAddr.setStatus(_A)
class _Hm2VpnTrafficSelSrcRest_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Hm2VpnTrafficSelSrcRest_Type.__name__=_D
_Hm2VpnTrafficSelSrcRest_Object=MibTableColumn
hm2VpnTrafficSelSrcRest=_Hm2VpnTrafficSelSrcRest_Object((1,3,6,1,4,1,248,11,120,1,3,1,1,4),_Hm2VpnTrafficSelSrcRest_Type())
hm2VpnTrafficSelSrcRest.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnTrafficSelSrcRest.setStatus(_A)
class _Hm2VpnTrafficSelDstRest_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Hm2VpnTrafficSelDstRest_Type.__name__=_D
_Hm2VpnTrafficSelDstRest_Object=MibTableColumn
hm2VpnTrafficSelDstRest=_Hm2VpnTrafficSelDstRest_Object((1,3,6,1,4,1,248,11,120,1,3,1,1,5),_Hm2VpnTrafficSelDstRest_Type())
hm2VpnTrafficSelDstRest.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnTrafficSelDstRest.setStatus(_A)
class _Hm2VpnTrafficSelDesc_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnTrafficSelDesc_Type.__name__=_D
_Hm2VpnTrafficSelDesc_Object=MibTableColumn
hm2VpnTrafficSelDesc=_Hm2VpnTrafficSelDesc_Object((1,3,6,1,4,1,248,11,120,1,3,1,1,6),_Hm2VpnTrafficSelDesc_Type())
hm2VpnTrafficSelDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnTrafficSelDesc.setStatus(_A)
_Hm2VpnTrafficSelRowStatus_Type=RowStatus
_Hm2VpnTrafficSelRowStatus_Object=MibTableColumn
hm2VpnTrafficSelRowStatus=_Hm2VpnTrafficSelRowStatus_Object((1,3,6,1,4,1,248,11,120,1,3,1,1,7),_Hm2VpnTrafficSelRowStatus_Type())
hm2VpnTrafficSelRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2VpnTrafficSelRowStatus.setStatus(_A)
_Hm2VpnCertificateGroup_ObjectIdentity=ObjectIdentity
hm2VpnCertificateGroup=_Hm2VpnCertificateGroup_ObjectIdentity((1,3,6,1,4,1,248,11,120,1,4))
class _Hm2VpnCertificateUploadPassphrase_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnCertificateUploadPassphrase_Type.__name__=_D
_Hm2VpnCertificateUploadPassphrase_Object=MibScalar
hm2VpnCertificateUploadPassphrase=_Hm2VpnCertificateUploadPassphrase_Object((1,3,6,1,4,1,248,11,120,1,4,1),_Hm2VpnCertificateUploadPassphrase_Type())
hm2VpnCertificateUploadPassphrase.setMaxAccess(_j)
if mibBuilder.loadTexts:hm2VpnCertificateUploadPassphrase.setStatus(_A)
_Hm2VpnCertificateTable_Object=MibTable
hm2VpnCertificateTable=_Hm2VpnCertificateTable_Object((1,3,6,1,4,1,248,11,120,1,4,10))
if mibBuilder.loadTexts:hm2VpnCertificateTable.setStatus(_A)
_Hm2VpnCertificateEntry_Object=MibTableRow
hm2VpnCertificateEntry=_Hm2VpnCertificateEntry_Object((1,3,6,1,4,1,248,11,120,1,4,10,1))
hm2VpnCertificateEntry.setIndexNames((0,_F,_k))
if mibBuilder.loadTexts:hm2VpnCertificateEntry.setStatus(_A)
class _Hm2VpnCertificateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_Hm2VpnCertificateIndex_Type.__name__=_E
_Hm2VpnCertificateIndex_Object=MibTableColumn
hm2VpnCertificateIndex=_Hm2VpnCertificateIndex_Object((1,3,6,1,4,1,248,11,120,1,4,10,1,1),_Hm2VpnCertificateIndex_Type())
hm2VpnCertificateIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hm2VpnCertificateIndex.setStatus(_A)
class _Hm2VpnCertificateSubject_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnCertificateSubject_Type.__name__=_D
_Hm2VpnCertificateSubject_Object=MibTableColumn
hm2VpnCertificateSubject=_Hm2VpnCertificateSubject_Object((1,3,6,1,4,1,248,11,120,1,4,10,1,2),_Hm2VpnCertificateSubject_Type())
hm2VpnCertificateSubject.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnCertificateSubject.setStatus(_A)
class _Hm2VpnCertificateIssuer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2VpnCertificateIssuer_Type.__name__=_D
_Hm2VpnCertificateIssuer_Object=MibTableColumn
hm2VpnCertificateIssuer=_Hm2VpnCertificateIssuer_Object((1,3,6,1,4,1,248,11,120,1,4,10,1,3),_Hm2VpnCertificateIssuer_Type())
hm2VpnCertificateIssuer.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnCertificateIssuer.setStatus(_A)
_Hm2VpnCertificateStartDate_Type=HmTimeSeconds1970
_Hm2VpnCertificateStartDate_Object=MibTableColumn
hm2VpnCertificateStartDate=_Hm2VpnCertificateStartDate_Object((1,3,6,1,4,1,248,11,120,1,4,10,1,4),_Hm2VpnCertificateStartDate_Type())
hm2VpnCertificateStartDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnCertificateStartDate.setStatus(_A)
_Hm2VpnCertificateEndDate_Type=HmTimeSeconds1970
_Hm2VpnCertificateEndDate_Object=MibTableColumn
hm2VpnCertificateEndDate=_Hm2VpnCertificateEndDate_Object((1,3,6,1,4,1,248,11,120,1,4,10,1,5),_Hm2VpnCertificateEndDate_Type())
hm2VpnCertificateEndDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnCertificateEndDate.setStatus(_A)
class _Hm2VpnCertificateFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Hm2VpnCertificateFileName_Type.__name__=_D
_Hm2VpnCertificateFileName_Object=MibTableColumn
hm2VpnCertificateFileName=_Hm2VpnCertificateFileName_Object((1,3,6,1,4,1,248,11,120,1,4,10,1,6),_Hm2VpnCertificateFileName_Type())
hm2VpnCertificateFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnCertificateFileName.setStatus(_A)
class _Hm2VpnCertificateType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ca',1),('peer',2),('encryptedkey',3),(_N,4),('encryptedpkcs12',5)))
_Hm2VpnCertificateType_Type.__name__=_E
_Hm2VpnCertificateType_Object=MibTableColumn
hm2VpnCertificateType=_Hm2VpnCertificateType_Object((1,3,6,1,4,1,248,11,120,1,4,10,1,7),_Hm2VpnCertificateType_Type())
hm2VpnCertificateType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnCertificateType.setStatus(_A)
_Hm2VpnCertificateCertUploadDate_Type=HmTimeSeconds1970
_Hm2VpnCertificateCertUploadDate_Object=MibTableColumn
hm2VpnCertificateCertUploadDate=_Hm2VpnCertificateCertUploadDate_Object((1,3,6,1,4,1,248,11,120,1,4,10,1,8),_Hm2VpnCertificateCertUploadDate_Type())
hm2VpnCertificateCertUploadDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnCertificateCertUploadDate.setStatus(_A)
class _Hm2VpnCertificatePrivateKeyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('present',2),('notFound',3)))
_Hm2VpnCertificatePrivateKeyStatus_Type.__name__=_E
_Hm2VpnCertificatePrivateKeyStatus_Object=MibTableColumn
hm2VpnCertificatePrivateKeyStatus=_Hm2VpnCertificatePrivateKeyStatus_Object((1,3,6,1,4,1,248,11,120,1,4,10,1,9),_Hm2VpnCertificatePrivateKeyStatus_Type())
hm2VpnCertificatePrivateKeyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnCertificatePrivateKeyStatus.setStatus(_A)
class _Hm2VpnCertificatePrivateKeyFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Hm2VpnCertificatePrivateKeyFile_Type.__name__=_D
_Hm2VpnCertificatePrivateKeyFile_Object=MibTableColumn
hm2VpnCertificatePrivateKeyFile=_Hm2VpnCertificatePrivateKeyFile_Object((1,3,6,1,4,1,248,11,120,1,4,10,1,10),_Hm2VpnCertificatePrivateKeyFile_Type())
hm2VpnCertificatePrivateKeyFile.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnCertificatePrivateKeyFile.setStatus(_A)
class _Hm2VpnCertificateNoConnections_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Hm2VpnCertificateNoConnections_Type.__name__=_E
_Hm2VpnCertificateNoConnections_Object=MibTableColumn
hm2VpnCertificateNoConnections=_Hm2VpnCertificateNoConnections_Object((1,3,6,1,4,1,248,11,120,1,4,10,1,11),_Hm2VpnCertificateNoConnections_Type())
hm2VpnCertificateNoConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2VpnCertificateNoConnections.setStatus(_A)
class _Hm2VpnCertificateUserActions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('delete',2)))
_Hm2VpnCertificateUserActions_Type.__name__=_E
_Hm2VpnCertificateUserActions_Object=MibTableColumn
hm2VpnCertificateUserActions=_Hm2VpnCertificateUserActions_Object((1,3,6,1,4,1,248,11,120,1,4,10,1,12),_Hm2VpnCertificateUserActions_Type())
hm2VpnCertificateUserActions.setMaxAccess(_j)
if mibBuilder.loadTexts:hm2VpnCertificateUserActions.setStatus(_A)
_Hm2VpnMibSNMPExtensionGroup_ObjectIdentity=ObjectIdentity
hm2VpnMibSNMPExtensionGroup=_Hm2VpnMibSNMPExtensionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,120,3))
_Hm2VpnMibSNMPExtensionNoTrafficSelector_ObjectIdentity=ObjectIdentity
hm2VpnMibSNMPExtensionNoTrafficSelector=_Hm2VpnMibSNMPExtensionNoTrafficSelector_ObjectIdentity((1,3,6,1,4,1,248,11,120,3,1))
if mibBuilder.loadTexts:hm2VpnMibSNMPExtensionNoTrafficSelector.setStatus(_A)
_Hm2VpnMibSNMPExtensionTooManyActive_ObjectIdentity=ObjectIdentity
hm2VpnMibSNMPExtensionTooManyActive=_Hm2VpnMibSNMPExtensionTooManyActive_ObjectIdentity((1,3,6,1,4,1,248,11,120,3,2))
if mibBuilder.loadTexts:hm2VpnMibSNMPExtensionTooManyActive.setStatus(_A)
_Hm2VpnMibSNMPExtensionTooManyConns_ObjectIdentity=ObjectIdentity
hm2VpnMibSNMPExtensionTooManyConns=_Hm2VpnMibSNMPExtensionTooManyConns_ObjectIdentity((1,3,6,1,4,1,248,11,120,3,3))
if mibBuilder.loadTexts:hm2VpnMibSNMPExtensionTooManyConns.setStatus(_A)
_Hm2VpnMibSNMPExtensionActiveRow_ObjectIdentity=ObjectIdentity
hm2VpnMibSNMPExtensionActiveRow=_Hm2VpnMibSNMPExtensionActiveRow_ObjectIdentity((1,3,6,1,4,1,248,11,120,3,4))
if mibBuilder.loadTexts:hm2VpnMibSNMPExtensionActiveRow.setStatus(_A)
_Hm2VpnMibSNMPExtensionInitiatorAny_ObjectIdentity=ObjectIdentity
hm2VpnMibSNMPExtensionInitiatorAny=_Hm2VpnMibSNMPExtensionInitiatorAny_ObjectIdentity((1,3,6,1,4,1,248,11,120,3,5))
if mibBuilder.loadTexts:hm2VpnMibSNMPExtensionInitiatorAny.setStatus(_A)
hm2VpnUpTrap=NotificationType((1,3,6,1,4,1,248,11,120,0,1))
hm2VpnUpTrap.setObjects(*((_F,_H),(_F,_K)))
if mibBuilder.loadTexts:hm2VpnUpTrap.setStatus(_A)
hm2VpnDownTrap=NotificationType((1,3,6,1,4,1,248,11,120,0,2))
hm2VpnDownTrap.setObjects(*((_F,_H),(_F,_K)))
if mibBuilder.loadTexts:hm2VpnDownTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'hm2VpnMib':hm2VpnMib,'hm2VpnMibNotifications':hm2VpnMibNotifications,'hm2VpnUpTrap':hm2VpnUpTrap,'hm2VpnDownTrap':hm2VpnDownTrap,'hm2VpnMibObjects':hm2VpnMibObjects,'hm2VpnGeneralGroup':hm2VpnGeneralGroup,'hm2VpnConnectionGroup':hm2VpnConnectionGroup,'hm2VpnConnMax':hm2VpnConnMax,'hm2VpnConnActiveMax':hm2VpnConnActiveMax,'hm2VpnConnNext':hm2VpnConnNext,'hm2VpnConnTable':hm2VpnConnTable,'hm2VpnConnEntry':hm2VpnConnEntry,_H:hm2VpnConnIndex,'hm2VpnConnIkeVersion':hm2VpnConnIkeVersion,'hm2VpnConnIkeStartup':hm2VpnConnIkeStartup,'hm2VpnConnIkeLifetime':hm2VpnConnIkeLifetime,'hm2VpnConnIkeDpdTimeout':hm2VpnConnIkeDpdTimeout,'hm2VpnConnIkeLocalAddr':hm2VpnConnIkeLocalAddr,'hm2VpnConnIkeRemoteAddr':hm2VpnConnIkeRemoteAddr,'hm2VpnConnIkeAuthType':hm2VpnConnIkeAuthType,'hm2VpnConnIkeAuthMode':hm2VpnConnIkeAuthMode,'hm2VpnConnIkeAuthCertCA':hm2VpnConnIkeAuthCertCA,'hm2VpnConnIkeAuthCertRemote':hm2VpnConnIkeAuthCertRemote,'hm2VpnConnIkeAuthCertLocal':hm2VpnConnIkeAuthCertLocal,'hm2VpnConnIkeAuthPrivKey':hm2VpnConnIkeAuthPrivKey,'hm2VpnConnIkeAuthPasswd':hm2VpnConnIkeAuthPasswd,'hm2VpnConnIkeAuthPsk':hm2VpnConnIkeAuthPsk,'hm2VpnConnIkeAuthLocId':hm2VpnConnIkeAuthLocId,'hm2VpnConnIkeAuthLocType':hm2VpnConnIkeAuthLocType,'hm2VpnConnIkeAuthRemId':hm2VpnConnIkeAuthRemId,'hm2VpnConnIkeAuthRemType':hm2VpnConnIkeAuthRemType,'hm2VpnConnIkeAlgDh':hm2VpnConnIkeAlgDh,'hm2VpnConnIkeAlgMac':hm2VpnConnIkeAlgMac,'hm2VpnConnIkeAlgEncr':hm2VpnConnIkeAlgEncr,'hm2VpnConnIkeReAuth':hm2VpnConnIkeReAuth,'hm2VpnConnIpsecMode':hm2VpnConnIpsecMode,'hm2VpnConnIpsecLifetime':hm2VpnConnIpsecLifetime,'hm2VpnConnMargintime':hm2VpnConnMargintime,'hm2VpnConnIpsecAlgDh':hm2VpnConnIpsecAlgDh,'hm2VpnConnIpsecAlgMac':hm2VpnConnIpsecAlgMac,'hm2VpnConnIpsecAlgEncr':hm2VpnConnIpsecAlgEncr,_K:hm2VpnConnOperStatus,'hm2VpnConnDesc':hm2VpnConnDesc,'hm2VpnConnLastError':hm2VpnConnLastError,'hm2VpnConnDebug':hm2VpnConnDebug,'hm2VpnConnRowStatus':hm2VpnConnRowStatus,'hm2VpnConnInfoTable':hm2VpnConnInfoTable,'hm2VpnConnInfoEntry':hm2VpnConnInfoEntry,'hm2VpnConnInfoIkeVersionUsed':hm2VpnConnInfoIkeVersionUsed,'hm2VpnConnInfoIkeProposal':hm2VpnConnInfoIkeProposal,'hm2VpnConnInfoIpsecProposal':hm2VpnConnInfoIpsecProposal,'hm2VpnConnInfoLocalHost':hm2VpnConnInfoLocalHost,'hm2VpnConnInfoRemoteHost':hm2VpnConnInfoRemoteHost,'hm2VpnConnInfoEstablished':hm2VpnConnInfoEstablished,'hm2VpnConnInfoIKEReauth':hm2VpnConnInfoIKEReauth,'hm2VpnConnInfoIKERekeying':hm2VpnConnInfoIKERekeying,'hm2VpnConnInfoIpsecRekeying':hm2VpnConnInfoIpsecRekeying,'hm2VpnConnInfoIpsecInBytes':hm2VpnConnInfoIpsecInBytes,'hm2VpnConnInfoIpsecInPackets':hm2VpnConnInfoIpsecInPackets,'hm2VpnConnInfoIpsecInUse':hm2VpnConnInfoIpsecInUse,'hm2VpnConnInfoIpsecOutBytes':hm2VpnConnInfoIpsecOutBytes,'hm2VpnConnInfoIpsecOutPackets':hm2VpnConnInfoIpsecOutPackets,'hm2VpnConnInfoIpsecOutUse':hm2VpnConnInfoIpsecOutUse,'hm2VpnConnInfoIKEInitiatorSPI':hm2VpnConnInfoIKEInitiatorSPI,'hm2VpnConnInfoIKEResponderSPI':hm2VpnConnInfoIKEResponderSPI,'hm2VpnConnInfoIpsecInSPI':hm2VpnConnInfoIpsecInSPI,'hm2VpnConnInfoIpsecOutSPI':hm2VpnConnInfoIpsecOutSPI,'hm2VpnConnInfoIpsecNumTunnel':hm2VpnConnInfoIpsecNumTunnel,'hm2VpnConnInfoTunnelTable':hm2VpnConnInfoTunnelTable,'hm2VpnConnInfoTunnelEntry':hm2VpnConnInfoTunnelEntry,_g:hm2VpnConnInfoTunnelIndex,'hm2VpnConnInfoTSelIndex':hm2VpnConnInfoTSelIndex,'hm2VpnConnInfoTunnelStatus':hm2VpnConnInfoTunnelStatus,'hm2VpnConnInfoTunnelRekeying':hm2VpnConnInfoTunnelRekeying,'hm2VpnConnInfoTunnelInBytes':hm2VpnConnInfoTunnelInBytes,'hm2VpnConnInfoTunnelInPackets':hm2VpnConnInfoTunnelInPackets,'hm2VpnConnInfoTunnelInUse':hm2VpnConnInfoTunnelInUse,'hm2VpnConnInfoTunnelOutBytes':hm2VpnConnInfoTunnelOutBytes,'hm2VpnConnInfoTunnelOutPackets':hm2VpnConnInfoTunnelOutPackets,'hm2VpnConnInfoTunnelOutUse':hm2VpnConnInfoTunnelOutUse,'hm2VpnConnInfoTunnelInSPI':hm2VpnConnInfoTunnelInSPI,'hm2VpnConnInfoTunnelOutSPI':hm2VpnConnInfoTunnelOutSPI,'hm2VpnConnInfoTunnelLocalSel':hm2VpnConnInfoTunnelLocalSel,'hm2VpnConnInfoTunnelRemoteSel':hm2VpnConnInfoTunnelRemoteSel,'hm2VpnTrafficSelGroup':hm2VpnTrafficSelGroup,'hm2VpnTrafficSelTable':hm2VpnTrafficSelTable,'hm2VpnTrafficSelEntry':hm2VpnTrafficSelEntry,_i:hm2VpnTrafficSelIndex,'hm2VpnTrafficSelSrcAddr':hm2VpnTrafficSelSrcAddr,'hm2VpnTrafficSelDstAddr':hm2VpnTrafficSelDstAddr,'hm2VpnTrafficSelSrcRest':hm2VpnTrafficSelSrcRest,'hm2VpnTrafficSelDstRest':hm2VpnTrafficSelDstRest,'hm2VpnTrafficSelDesc':hm2VpnTrafficSelDesc,'hm2VpnTrafficSelRowStatus':hm2VpnTrafficSelRowStatus,'hm2VpnCertificateGroup':hm2VpnCertificateGroup,'hm2VpnCertificateUploadPassphrase':hm2VpnCertificateUploadPassphrase,'hm2VpnCertificateTable':hm2VpnCertificateTable,'hm2VpnCertificateEntry':hm2VpnCertificateEntry,_k:hm2VpnCertificateIndex,'hm2VpnCertificateSubject':hm2VpnCertificateSubject,'hm2VpnCertificateIssuer':hm2VpnCertificateIssuer,'hm2VpnCertificateStartDate':hm2VpnCertificateStartDate,'hm2VpnCertificateEndDate':hm2VpnCertificateEndDate,'hm2VpnCertificateFileName':hm2VpnCertificateFileName,'hm2VpnCertificateType':hm2VpnCertificateType,'hm2VpnCertificateCertUploadDate':hm2VpnCertificateCertUploadDate,'hm2VpnCertificatePrivateKeyStatus':hm2VpnCertificatePrivateKeyStatus,'hm2VpnCertificatePrivateKeyFile':hm2VpnCertificatePrivateKeyFile,'hm2VpnCertificateNoConnections':hm2VpnCertificateNoConnections,'hm2VpnCertificateUserActions':hm2VpnCertificateUserActions,'hm2VpnMibSNMPExtensionGroup':hm2VpnMibSNMPExtensionGroup,'hm2VpnMibSNMPExtensionNoTrafficSelector':hm2VpnMibSNMPExtensionNoTrafficSelector,'hm2VpnMibSNMPExtensionTooManyActive':hm2VpnMibSNMPExtensionTooManyActive,'hm2VpnMibSNMPExtensionTooManyConns':hm2VpnMibSNMPExtensionTooManyConns,'hm2VpnMibSNMPExtensionActiveRow':hm2VpnMibSNMPExtensionActiveRow,'hm2VpnMibSNMPExtensionInitiatorAny':hm2VpnMibSNMPExtensionInitiatorAny})