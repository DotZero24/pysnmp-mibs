_i='etsysSecureShellServerHostKeyGroup'
_h='etsysSecureShellServerConfigGroup'
_g='etsysSecureShellServerHostKeyRowStatus'
_f='etsysSecureShellServerHostKeyStorageType'
_e='etsysSecureShellServerHostKeyErrorStatus'
_d='etsysSecureShellServerHostKeyFingerprint'
_c='etsysSecureShellServerHostKeyAdminStatus'
_b='etsysSecureShellServerHostKeyOperStatus'
_a='etsysSecureShellServerHostKeyDate'
_Z='etsysSecureShellServerOperCiphers'
_Y='etsysSecureShellServerAdminCiphers'
_X='etsysSecureShellServerSupportedCiphers'
_W='etsysSecureShellServerOperMacs'
_V='etsysSecureShellServerAdminMacs'
_U='etsysSecureShellServerSupportedMacs'
_T='etsysSecureShellServerOperPort'
_S='etsysSecureShellServerAdminPort'
_R='etsysSecureShellServerOperStatus'
_Q='etsysSecureShellServerAdminStatus'
_P='HexString'
_O='read-create'
_N='not-accessible'
_M='etsysSecureShellServerHostKeySize'
_L='etsysSecureShellServerHostKeyType'
_K='initializing'
_J='operational'
_I='reinitialize'
_H='StorageType'
_G='Unsigned32'
_F='SnmpAdminString'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='ENTERASYS-SECURE-SHELL-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus',_H,'TextualConvention')
etsysSecureShellServerMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,36))
if mibBuilder.loadTexts:etsysSecureShellServerMIB.setRevisions(('2003-02-12 17:14',))
class SshCipherList(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('triple-des-cbc',0),('twofish128-cbc',1),('blowfish-cbc',2),('cast128-cbc',3),('aes128-cbc',4)))
class SshMacList(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('hmac-md5',0),('hmac-md5-96',1),('hmac-sha1',2),('hmac-sha1-96',3),('hmac-ripemd160',4)))
class HexString(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_EtsysSecureShellServer_ObjectIdentity=ObjectIdentity
etsysSecureShellServer=_EtsysSecureShellServer_ObjectIdentity((1,3,6,1,4,1,5624,1,2,36,1))
_EtsysSecureShellServerConfig_ObjectIdentity=ObjectIdentity
etsysSecureShellServerConfig=_EtsysSecureShellServerConfig_ObjectIdentity((1,3,6,1,4,1,5624,1,2,36,1,1))
class _EtsysSecureShellServerAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('disabled',2),(_I,3)))
_EtsysSecureShellServerAdminStatus_Type.__name__=_D
_EtsysSecureShellServerAdminStatus_Object=MibScalar
etsysSecureShellServerAdminStatus=_EtsysSecureShellServerAdminStatus_Object((1,3,6,1,4,1,5624,1,2,36,1,1,1),_EtsysSecureShellServerAdminStatus_Type())
etsysSecureShellServerAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSecureShellServerAdminStatus.setStatus(_A)
class _EtsysSecureShellServerOperStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),('nonOperational',3)))
_EtsysSecureShellServerOperStatus_Type.__name__=_D
_EtsysSecureShellServerOperStatus_Object=MibScalar
etsysSecureShellServerOperStatus=_EtsysSecureShellServerOperStatus_Object((1,3,6,1,4,1,5624,1,2,36,1,1,2),_EtsysSecureShellServerOperStatus_Type())
etsysSecureShellServerOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSecureShellServerOperStatus.setStatus(_A)
class _EtsysSecureShellServerErrorStatus_Type(SnmpAdminString):defaultHexValue=''
_EtsysSecureShellServerErrorStatus_Type.__name__=_F
_EtsysSecureShellServerErrorStatus_Object=MibScalar
etsysSecureShellServerErrorStatus=_EtsysSecureShellServerErrorStatus_Object((1,3,6,1,4,1,5624,1,2,36,1,1,3),_EtsysSecureShellServerErrorStatus_Type())
etsysSecureShellServerErrorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSecureShellServerErrorStatus.setStatus(_A)
class _EtsysSecureShellServerAdminPort_Type(Unsigned32):defaultValue=22;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EtsysSecureShellServerAdminPort_Type.__name__=_G
_EtsysSecureShellServerAdminPort_Object=MibScalar
etsysSecureShellServerAdminPort=_EtsysSecureShellServerAdminPort_Object((1,3,6,1,4,1,5624,1,2,36,1,1,4),_EtsysSecureShellServerAdminPort_Type())
etsysSecureShellServerAdminPort.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSecureShellServerAdminPort.setStatus(_A)
_EtsysSecureShellServerOperPort_Type=Unsigned32
_EtsysSecureShellServerOperPort_Object=MibScalar
etsysSecureShellServerOperPort=_EtsysSecureShellServerOperPort_Object((1,3,6,1,4,1,5624,1,2,36,1,1,5),_EtsysSecureShellServerOperPort_Type())
etsysSecureShellServerOperPort.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSecureShellServerOperPort.setStatus(_A)
_EtsysSecureShellServerMac_ObjectIdentity=ObjectIdentity
etsysSecureShellServerMac=_EtsysSecureShellServerMac_ObjectIdentity((1,3,6,1,4,1,5624,1,2,36,1,2))
_EtsysSecureShellServerSupportedMacs_Type=SshMacList
_EtsysSecureShellServerSupportedMacs_Object=MibScalar
etsysSecureShellServerSupportedMacs=_EtsysSecureShellServerSupportedMacs_Object((1,3,6,1,4,1,5624,1,2,36,1,2,1),_EtsysSecureShellServerSupportedMacs_Type())
etsysSecureShellServerSupportedMacs.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSecureShellServerSupportedMacs.setStatus(_A)
_EtsysSecureShellServerAdminMacs_Type=SshMacList
_EtsysSecureShellServerAdminMacs_Object=MibScalar
etsysSecureShellServerAdminMacs=_EtsysSecureShellServerAdminMacs_Object((1,3,6,1,4,1,5624,1,2,36,1,2,2),_EtsysSecureShellServerAdminMacs_Type())
etsysSecureShellServerAdminMacs.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSecureShellServerAdminMacs.setStatus(_A)
_EtsysSecureShellServerOperMacs_Type=SshMacList
_EtsysSecureShellServerOperMacs_Object=MibScalar
etsysSecureShellServerOperMacs=_EtsysSecureShellServerOperMacs_Object((1,3,6,1,4,1,5624,1,2,36,1,2,3),_EtsysSecureShellServerOperMacs_Type())
etsysSecureShellServerOperMacs.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSecureShellServerOperMacs.setStatus(_A)
_EtsysSecureShellServerCipher_ObjectIdentity=ObjectIdentity
etsysSecureShellServerCipher=_EtsysSecureShellServerCipher_ObjectIdentity((1,3,6,1,4,1,5624,1,2,36,1,3))
_EtsysSecureShellServerSupportedCiphers_Type=SshCipherList
_EtsysSecureShellServerSupportedCiphers_Object=MibScalar
etsysSecureShellServerSupportedCiphers=_EtsysSecureShellServerSupportedCiphers_Object((1,3,6,1,4,1,5624,1,2,36,1,3,1),_EtsysSecureShellServerSupportedCiphers_Type())
etsysSecureShellServerSupportedCiphers.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSecureShellServerSupportedCiphers.setStatus(_A)
_EtsysSecureShellServerAdminCiphers_Type=SshCipherList
_EtsysSecureShellServerAdminCiphers_Object=MibScalar
etsysSecureShellServerAdminCiphers=_EtsysSecureShellServerAdminCiphers_Object((1,3,6,1,4,1,5624,1,2,36,1,3,2),_EtsysSecureShellServerAdminCiphers_Type())
etsysSecureShellServerAdminCiphers.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSecureShellServerAdminCiphers.setStatus(_A)
_EtsysSecureShellServerOperCiphers_Type=SshCipherList
_EtsysSecureShellServerOperCiphers_Object=MibScalar
etsysSecureShellServerOperCiphers=_EtsysSecureShellServerOperCiphers_Object((1,3,6,1,4,1,5624,1,2,36,1,3,3),_EtsysSecureShellServerOperCiphers_Type())
etsysSecureShellServerOperCiphers.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSecureShellServerOperCiphers.setStatus(_A)
_EtsysSecureShellServerHostKey_ObjectIdentity=ObjectIdentity
etsysSecureShellServerHostKey=_EtsysSecureShellServerHostKey_ObjectIdentity((1,3,6,1,4,1,5624,1,2,36,1,4))
_EtsysSecureShellServerHostKeyTable_Object=MibTable
etsysSecureShellServerHostKeyTable=_EtsysSecureShellServerHostKeyTable_Object((1,3,6,1,4,1,5624,1,2,36,1,4,1))
if mibBuilder.loadTexts:etsysSecureShellServerHostKeyTable.setStatus(_A)
_EtsysSecureShellServerHostKeyEntry_Object=MibTableRow
etsysSecureShellServerHostKeyEntry=_EtsysSecureShellServerHostKeyEntry_Object((1,3,6,1,4,1,5624,1,2,36,1,4,1,1))
etsysSecureShellServerHostKeyEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:etsysSecureShellServerHostKeyEntry.setStatus(_A)
class _EtsysSecureShellServerHostKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sshDss',1),('sshRsa',2)))
_EtsysSecureShellServerHostKeyType_Type.__name__=_D
_EtsysSecureShellServerHostKeyType_Object=MibTableColumn
etsysSecureShellServerHostKeyType=_EtsysSecureShellServerHostKeyType_Object((1,3,6,1,4,1,5624,1,2,36,1,4,1,1,1),_EtsysSecureShellServerHostKeyType_Type())
etsysSecureShellServerHostKeyType.setMaxAccess(_N)
if mibBuilder.loadTexts:etsysSecureShellServerHostKeyType.setStatus(_A)
class _EtsysSecureShellServerHostKeySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bits512',1),('bits768',2),('bits1024',3),('bits2048',4)))
_EtsysSecureShellServerHostKeySize_Type.__name__=_D
_EtsysSecureShellServerHostKeySize_Object=MibTableColumn
etsysSecureShellServerHostKeySize=_EtsysSecureShellServerHostKeySize_Object((1,3,6,1,4,1,5624,1,2,36,1,4,1,1,2),_EtsysSecureShellServerHostKeySize_Type())
etsysSecureShellServerHostKeySize.setMaxAccess(_N)
if mibBuilder.loadTexts:etsysSecureShellServerHostKeySize.setStatus(_A)
_EtsysSecureShellServerHostKeyDate_Type=DateAndTime
_EtsysSecureShellServerHostKeyDate_Object=MibTableColumn
etsysSecureShellServerHostKeyDate=_EtsysSecureShellServerHostKeyDate_Object((1,3,6,1,4,1,5624,1,2,36,1,4,1,1,3),_EtsysSecureShellServerHostKeyDate_Type())
etsysSecureShellServerHostKeyDate.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSecureShellServerHostKeyDate.setStatus(_A)
class _EtsysSecureShellServerHostKeyOperStatus_Type(Bits):namedValues=NamedValues(*((_K,0),(_J,1),('completed',2),('pending',3),('failed',4)))
_EtsysSecureShellServerHostKeyOperStatus_Type.__name__='Bits'
_EtsysSecureShellServerHostKeyOperStatus_Object=MibTableColumn
etsysSecureShellServerHostKeyOperStatus=_EtsysSecureShellServerHostKeyOperStatus_Object((1,3,6,1,4,1,5624,1,2,36,1,4,1,1,4),_EtsysSecureShellServerHostKeyOperStatus_Type())
etsysSecureShellServerHostKeyOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSecureShellServerHostKeyOperStatus.setStatus(_A)
class _EtsysSecureShellServerHostKeyAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),(_I,2)))
_EtsysSecureShellServerHostKeyAdminStatus_Type.__name__=_D
_EtsysSecureShellServerHostKeyAdminStatus_Object=MibTableColumn
etsysSecureShellServerHostKeyAdminStatus=_EtsysSecureShellServerHostKeyAdminStatus_Object((1,3,6,1,4,1,5624,1,2,36,1,4,1,1,5),_EtsysSecureShellServerHostKeyAdminStatus_Type())
etsysSecureShellServerHostKeyAdminStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:etsysSecureShellServerHostKeyAdminStatus.setStatus(_A)
class _EtsysSecureShellServerHostKeyFingerprint_Type(HexString):subtypeSpec=HexString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_EtsysSecureShellServerHostKeyFingerprint_Type.__name__=_P
_EtsysSecureShellServerHostKeyFingerprint_Object=MibTableColumn
etsysSecureShellServerHostKeyFingerprint=_EtsysSecureShellServerHostKeyFingerprint_Object((1,3,6,1,4,1,5624,1,2,36,1,4,1,1,6),_EtsysSecureShellServerHostKeyFingerprint_Type())
etsysSecureShellServerHostKeyFingerprint.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSecureShellServerHostKeyFingerprint.setStatus(_A)
class _EtsysSecureShellServerHostKeyErrorStatus_Type(SnmpAdminString):defaultHexValue=''
_EtsysSecureShellServerHostKeyErrorStatus_Type.__name__=_F
_EtsysSecureShellServerHostKeyErrorStatus_Object=MibTableColumn
etsysSecureShellServerHostKeyErrorStatus=_EtsysSecureShellServerHostKeyErrorStatus_Object((1,3,6,1,4,1,5624,1,2,36,1,4,1,1,7),_EtsysSecureShellServerHostKeyErrorStatus_Type())
etsysSecureShellServerHostKeyErrorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSecureShellServerHostKeyErrorStatus.setStatus(_A)
class _EtsysSecureShellServerHostKeyStorageType_Type(StorageType):defaultValue=3
_EtsysSecureShellServerHostKeyStorageType_Type.__name__=_H
_EtsysSecureShellServerHostKeyStorageType_Object=MibTableColumn
etsysSecureShellServerHostKeyStorageType=_EtsysSecureShellServerHostKeyStorageType_Object((1,3,6,1,4,1,5624,1,2,36,1,4,1,1,8),_EtsysSecureShellServerHostKeyStorageType_Type())
etsysSecureShellServerHostKeyStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSecureShellServerHostKeyStorageType.setStatus(_A)
_EtsysSecureShellServerHostKeyRowStatus_Type=RowStatus
_EtsysSecureShellServerHostKeyRowStatus_Object=MibTableColumn
etsysSecureShellServerHostKeyRowStatus=_EtsysSecureShellServerHostKeyRowStatus_Object((1,3,6,1,4,1,5624,1,2,36,1,4,1,1,9),_EtsysSecureShellServerHostKeyRowStatus_Type())
etsysSecureShellServerHostKeyRowStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:etsysSecureShellServerHostKeyRowStatus.setStatus(_A)
_EtsysSecureShellServerConformance_ObjectIdentity=ObjectIdentity
etsysSecureShellServerConformance=_EtsysSecureShellServerConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,36,2))
_EtsysSecureShellServerGroups_ObjectIdentity=ObjectIdentity
etsysSecureShellServerGroups=_EtsysSecureShellServerGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,36,2,1))
_EtsysSecureShellServerCompliances_ObjectIdentity=ObjectIdentity
etsysSecureShellServerCompliances=_EtsysSecureShellServerCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,36,2,2))
etsysSecureShellServerConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,36,2,1,1))
etsysSecureShellServerConfigGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:etsysSecureShellServerConfigGroup.setStatus(_A)
etsysSecureShellServerHostKeyGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,36,2,1,2))
etsysSecureShellServerHostKeyGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:etsysSecureShellServerHostKeyGroup.setStatus(_A)
etsysSecureShellServerCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,36,2,2,1))
etsysSecureShellServerCompliance.setObjects(*((_B,_h),(_B,_i)))
if mibBuilder.loadTexts:etsysSecureShellServerCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SshCipherList':SshCipherList,'SshMacList':SshMacList,_P:HexString,'etsysSecureShellServerMIB':etsysSecureShellServerMIB,'etsysSecureShellServer':etsysSecureShellServer,'etsysSecureShellServerConfig':etsysSecureShellServerConfig,_Q:etsysSecureShellServerAdminStatus,_R:etsysSecureShellServerOperStatus,'etsysSecureShellServerErrorStatus':etsysSecureShellServerErrorStatus,_S:etsysSecureShellServerAdminPort,_T:etsysSecureShellServerOperPort,'etsysSecureShellServerMac':etsysSecureShellServerMac,_U:etsysSecureShellServerSupportedMacs,_V:etsysSecureShellServerAdminMacs,_W:etsysSecureShellServerOperMacs,'etsysSecureShellServerCipher':etsysSecureShellServerCipher,_X:etsysSecureShellServerSupportedCiphers,_Y:etsysSecureShellServerAdminCiphers,_Z:etsysSecureShellServerOperCiphers,'etsysSecureShellServerHostKey':etsysSecureShellServerHostKey,'etsysSecureShellServerHostKeyTable':etsysSecureShellServerHostKeyTable,'etsysSecureShellServerHostKeyEntry':etsysSecureShellServerHostKeyEntry,_L:etsysSecureShellServerHostKeyType,_M:etsysSecureShellServerHostKeySize,_a:etsysSecureShellServerHostKeyDate,_b:etsysSecureShellServerHostKeyOperStatus,_c:etsysSecureShellServerHostKeyAdminStatus,_d:etsysSecureShellServerHostKeyFingerprint,_e:etsysSecureShellServerHostKeyErrorStatus,_f:etsysSecureShellServerHostKeyStorageType,_g:etsysSecureShellServerHostKeyRowStatus,'etsysSecureShellServerConformance':etsysSecureShellServerConformance,'etsysSecureShellServerGroups':etsysSecureShellServerGroups,_h:etsysSecureShellServerConfigGroup,_i:etsysSecureShellServerHostKeyGroup,'etsysSecureShellServerCompliances':etsysSecureShellServerCompliances,'etsysSecureShellServerCompliance':etsysSecureShellServerCompliance})