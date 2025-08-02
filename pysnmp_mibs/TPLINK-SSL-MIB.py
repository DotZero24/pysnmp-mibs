_E='enable'
_D='disable'
_C='Integer32'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkSslMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,42))
if mibBuilder.loadTexts:tplinkSslMIB.setRevisions(('2012-12-13 09:30',))
_TplinkSslMIBObjects_ObjectIdentity=ObjectIdentity
tplinkSslMIBObjects=_TplinkSslMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,42,1))
class _TpHttpsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpHttpsEnable_Type.__name__=_C
_TpHttpsEnable_Object=MibScalar
tpHttpsEnable=_TpHttpsEnable_Object((1,3,6,1,4,1,11863,6,42,1,1),_TpHttpsEnable_Type())
tpHttpsEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:tpHttpsEnable.setStatus(_B)
class _TpSslProtocolVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('sslv3',1),('tlsv1',2),('tlsv11',3),('tlsv12',4),('all',5)))
_TpSslProtocolVersion_Type.__name__=_C
_TpSslProtocolVersion_Object=MibScalar
tpSslProtocolVersion=_TpSslProtocolVersion_Object((1,3,6,1,4,1,11863,6,42,1,2),_TpSslProtocolVersion_Type())
tpSslProtocolVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:tpSslProtocolVersion.setStatus(_B)
class _TpRc4Md5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpRc4Md5_Type.__name__=_C
_TpRc4Md5_Object=MibScalar
tpRc4Md5=_TpRc4Md5_Object((1,3,6,1,4,1,11863,6,42,1,3),_TpRc4Md5_Type())
tpRc4Md5.setMaxAccess(_A)
if mibBuilder.loadTexts:tpRc4Md5.setStatus(_B)
class _TpRc4Sha_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpRc4Sha_Type.__name__=_C
_TpRc4Sha_Object=MibScalar
tpRc4Sha=_TpRc4Sha_Object((1,3,6,1,4,1,11863,6,42,1,4),_TpRc4Sha_Type())
tpRc4Sha.setMaxAccess(_A)
if mibBuilder.loadTexts:tpRc4Sha.setStatus(_B)
class _TpDesCbcSha_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpDesCbcSha_Type.__name__=_C
_TpDesCbcSha_Object=MibScalar
tpDesCbcSha=_TpDesCbcSha_Object((1,3,6,1,4,1,11863,6,42,1,5),_TpDesCbcSha_Type())
tpDesCbcSha.setMaxAccess(_A)
if mibBuilder.loadTexts:tpDesCbcSha.setStatus(_B)
class _Tp3DesEdeCbcSha_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_Tp3DesEdeCbcSha_Type.__name__=_C
_Tp3DesEdeCbcSha_Object=MibScalar
tp3DesEdeCbcSha=_Tp3DesEdeCbcSha_Object((1,3,6,1,4,1,11863,6,42,1,6),_Tp3DesEdeCbcSha_Type())
tp3DesEdeCbcSha.setMaxAccess(_A)
if mibBuilder.loadTexts:tp3DesEdeCbcSha.setStatus(_B)
class _TpEcdheAes128GcmSha256_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpEcdheAes128GcmSha256_Type.__name__=_C
_TpEcdheAes128GcmSha256_Object=MibScalar
tpEcdheAes128GcmSha256=_TpEcdheAes128GcmSha256_Object((1,3,6,1,4,1,11863,6,42,1,7),_TpEcdheAes128GcmSha256_Type())
tpEcdheAes128GcmSha256.setMaxAccess(_A)
if mibBuilder.loadTexts:tpEcdheAes128GcmSha256.setStatus(_B)
class _TpEcdheAes256GcmSha384_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpEcdheAes256GcmSha384_Type.__name__=_C
_TpEcdheAes256GcmSha384_Object=MibScalar
tpEcdheAes256GcmSha384=_TpEcdheAes256GcmSha384_Object((1,3,6,1,4,1,11863,6,42,1,8),_TpEcdheAes256GcmSha384_Type())
tpEcdheAes256GcmSha384.setMaxAccess(_A)
if mibBuilder.loadTexts:tpEcdheAes256GcmSha384.setStatus(_B)
class _TpHttpsSessionTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_TpHttpsSessionTimeOut_Type.__name__=_C
_TpHttpsSessionTimeOut_Object=MibScalar
tpHttpsSessionTimeOut=_TpHttpsSessionTimeOut_Object((1,3,6,1,4,1,11863,6,42,1,9),_TpHttpsSessionTimeOut_Type())
tpHttpsSessionTimeOut.setMaxAccess(_A)
if mibBuilder.loadTexts:tpHttpsSessionTimeOut.setStatus(_B)
class _TpHttpsUserLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpHttpsUserLimitEnable_Type.__name__=_C
_TpHttpsUserLimitEnable_Object=MibScalar
tpHttpsUserLimitEnable=_TpHttpsUserLimitEnable_Object((1,3,6,1,4,1,11863,6,42,1,10),_TpHttpsUserLimitEnable_Type())
tpHttpsUserLimitEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:tpHttpsUserLimitEnable.setStatus(_B)
_TpHttpsUserLimitMaxAdminNum_Type=Integer32
_TpHttpsUserLimitMaxAdminNum_Object=MibScalar
tpHttpsUserLimitMaxAdminNum=_TpHttpsUserLimitMaxAdminNum_Object((1,3,6,1,4,1,11863,6,42,1,11),_TpHttpsUserLimitMaxAdminNum_Type())
tpHttpsUserLimitMaxAdminNum.setMaxAccess(_A)
if mibBuilder.loadTexts:tpHttpsUserLimitMaxAdminNum.setStatus(_B)
_TpHttpsUserLimitMaxOperatorNum_Type=Integer32
_TpHttpsUserLimitMaxOperatorNum_Object=MibScalar
tpHttpsUserLimitMaxOperatorNum=_TpHttpsUserLimitMaxOperatorNum_Object((1,3,6,1,4,1,11863,6,42,1,12),_TpHttpsUserLimitMaxOperatorNum_Type())
tpHttpsUserLimitMaxOperatorNum.setMaxAccess(_A)
if mibBuilder.loadTexts:tpHttpsUserLimitMaxOperatorNum.setStatus(_B)
_TpHttpsUserLimitMaxPowerUserNum_Type=Integer32
_TpHttpsUserLimitMaxPowerUserNum_Object=MibScalar
tpHttpsUserLimitMaxPowerUserNum=_TpHttpsUserLimitMaxPowerUserNum_Object((1,3,6,1,4,1,11863,6,42,1,13),_TpHttpsUserLimitMaxPowerUserNum_Type())
tpHttpsUserLimitMaxPowerUserNum.setMaxAccess(_A)
if mibBuilder.loadTexts:tpHttpsUserLimitMaxPowerUserNum.setStatus(_B)
_TpHttpsUserLimitMaxUserNum_Type=Integer32
_TpHttpsUserLimitMaxUserNum_Object=MibScalar
tpHttpsUserLimitMaxUserNum=_TpHttpsUserLimitMaxUserNum_Object((1,3,6,1,4,1,11863,6,42,1,14),_TpHttpsUserLimitMaxUserNum_Type())
tpHttpsUserLimitMaxUserNum.setMaxAccess(_A)
if mibBuilder.loadTexts:tpHttpsUserLimitMaxUserNum.setStatus(_B)
class _TpHttpsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TpHttpsPort_Type.__name__=_C
_TpHttpsPort_Object=MibScalar
tpHttpsPort=_TpHttpsPort_Object((1,3,6,1,4,1,11863,6,42,1,15),_TpHttpsPort_Type())
tpHttpsPort.setMaxAccess(_A)
if mibBuilder.loadTexts:tpHttpsPort.setStatus(_B)
_TplinkSslNotifications_ObjectIdentity=ObjectIdentity
tplinkSslNotifications=_TplinkSslNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,42,2))
mibBuilder.exportSymbols('TPLINK-SSL-MIB',**{'tplinkSslMIB':tplinkSslMIB,'tplinkSslMIBObjects':tplinkSslMIBObjects,'tpHttpsEnable':tpHttpsEnable,'tpSslProtocolVersion':tpSslProtocolVersion,'tpRc4Md5':tpRc4Md5,'tpRc4Sha':tpRc4Sha,'tpDesCbcSha':tpDesCbcSha,'tp3DesEdeCbcSha':tp3DesEdeCbcSha,'tpEcdheAes128GcmSha256':tpEcdheAes128GcmSha256,'tpEcdheAes256GcmSha384':tpEcdheAes256GcmSha384,'tpHttpsSessionTimeOut':tpHttpsSessionTimeOut,'tpHttpsUserLimitEnable':tpHttpsUserLimitEnable,'tpHttpsUserLimitMaxAdminNum':tpHttpsUserLimitMaxAdminNum,'tpHttpsUserLimitMaxOperatorNum':tpHttpsUserLimitMaxOperatorNum,'tpHttpsUserLimitMaxPowerUserNum':tpHttpsUserLimitMaxPowerUserNum,'tpHttpsUserLimitMaxUserNum':tpHttpsUserLimitMaxUserNum,'tpHttpsPort':tpHttpsPort,'tplinkSslNotifications':tplinkSslNotifications})