_AX='pktcMtaDevProvisioningEnrollment'
_AW='pktcMtaDevProvisioningStatus'
_AV='pktcMtaDevTelephonyRootCertificate'
_AU='pktcMtaDevProvisioningTimer'
_AT='pktcMtaDevProvState'
_AS='pktcMtaDevProvConfigKey'
_AR='pktcMtaDevProvConfigHash'
_AQ='pktcMtaDevProvSolicitedKeyTimeout'
_AP='pktcMtaDevProvKerbRealmName'
_AO='pktcMtaDevProvUnsolicitedKeyMaxRetries'
_AN='pktcMtaDevProvUnsolicitedKeyNomTimeout'
_AM='pktcMtaDevProvUnsolicitedKeyMaxTimeout'
_AL='pktcMtaDevResetKrbTickets'
_AK='pktcMtaDevCmsStatus'
_AJ='pktcMtaDevCmsIpsecCtrl'
_AI='pktcMtaDevCmsMaxClockSkew'
_AH='pktcMtaDevCmsSolicitedKeyTimeout'
_AG='pktcMtaDevCmsUnsolicitedKeyMaxRetries'
_AF='pktcMtaDevCmsUnsolicitedKeyNomTimeout'
_AE='pktcMtaDevCmsUnsolicitedKeyMaxTimeout'
_AD='pktcMtaDevCmsKerbRealmName'
_AC='pktcMtaDevCmsFqdn'
_AB='pktcMtaDevCmsAvailSlot'
_AA='pktcMtaDevRealmStatus'
_A9='pktcMtaDevRealmUnsolicitedKeyMaxRetries'
_A8='pktcMtaDevRealmUnsolicitedKeyNomTimeout'
_A7='pktcMtaDevRealmUnsolicitedKeyMaxTimeout'
_A6='pktcMtaDevRealmOrgName'
_A5='pktcMtaDevRealmName'
_A4='pktcMtaDevRealmAvailSlot'
_A3='pktcMtaDevRealmTgsGracePeriod'
_A2='pktcMtaDevRealmPkinitGracePeriod'
_A1='pktcMtaDevSnmpEntity'
_A0='pktcMtaDevConfigFile'
_z='pktcMtaDevTimeServer'
_y='pktcMtaDevServerDns2'
_x='pktcMtaDevServerDns1'
_w='pktcMtaDevServerDhcp2'
_v='pktcMtaDevServerDhcp1'
_u='pktcMtaDevProvConfigEncryptAlg'
_t='pktcMtaDevTimeServerAddressType'
_s='pktcMtaDevDnsServerAddressType'
_r='pktcMtaDevDhcpServerAddressType'
_q='pktcMtaDevManufacturerCertificate'
_p='pktcMtaDevCertificate'
_o='pktcMtaDevHttpAccess'
_n='pktcMtaDevErrorReason'
_m='pktcMtaDevErrorValue'
_l='pktcMtaDevErrorOid'
_k='pktcMtaDevProvisioningCounter'
_j='pktcMtaDevEnabled'
_i='pktcMtaDevEndPntCount'
_h='pktcMtaDevFQDN'
_g='pktcMtaDevSerialNumber'
_f='pktcMtaDevResetNow'
_e='pktcMtaDevCmsIndex'
_d='pktcMtaDevRealmIndex'
_c='PktcMtaDevProvEncryptAlg'
_b='pktcMtaDevErrorOidIndex'
_a='TruthValue'
_Z='sysDescr'
_Y='SNMPv2-MIB'
_X='docsBpi2CodeDownloadGroup'
_W='DOCS-IETF-BPI2-MIB'
_V='pktcMtaNotificationGroup'
_U='pktcMtaGroup'
_T='pktcMtaDevProvisioningState'
_S='pktcMtaDevTypeIdentifier'
_R='pktcMtaDevSwCurrentVers'
_Q='milliseconds'
_P='not-accessible'
_O='minutes'
_N='Integer32'
_M='ifPhysAddress'
_L='IF-MIB'
_K='OctetString'
_J='pktcMtaDevCorrelationId'
_I='InetAddressType'
_H='SnmpAdminString'
_G='seconds'
_F='read-write'
_E='read-create'
_D='Unsigned32'
_C='read-only'
_B='PKTC-IETF-MTA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DocsX509ASN1DEREncodedCertificate,docsBpi2CodeDownloadGroup=mibBuilder.importSymbols(_W,'DocsX509ASN1DEREncodedCertificate',_X)
ifPhysAddress,=mibBuilder.importSymbols(_L,_M)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysDescr,=mibBuilder.importSymbols(_Y,_Z)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_N,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_a)
pktcIetfMtaMib=ModuleIdentity((1,3,6,1,2,1,140))
if mibBuilder.loadTexts:pktcIetfMtaMib.setRevisions(('2006-09-18 00:00',))
class PktcMtaDevProvEncryptAlg(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('none',0),('des64CbcMode',1),('t3Des192CbcMode',2),('aes128CbcMode',3),('aes256CbcMode',4)))
_PktcMtaNotification_ObjectIdentity=ObjectIdentity
pktcMtaNotification=_PktcMtaNotification_ObjectIdentity((1,3,6,1,2,1,140,0))
_PktcMtaMibObjects_ObjectIdentity=ObjectIdentity
pktcMtaMibObjects=_PktcMtaMibObjects_ObjectIdentity((1,3,6,1,2,1,140,1))
_PktcMtaDevBase_ObjectIdentity=ObjectIdentity
pktcMtaDevBase=_PktcMtaDevBase_ObjectIdentity((1,3,6,1,2,1,140,1,1))
_PktcMtaDevResetNow_Type=TruthValue
_PktcMtaDevResetNow_Object=MibScalar
pktcMtaDevResetNow=_PktcMtaDevResetNow_Object((1,3,6,1,2,1,140,1,1,1),_PktcMtaDevResetNow_Type())
pktcMtaDevResetNow.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcMtaDevResetNow.setStatus(_A)
_PktcMtaDevSerialNumber_Type=SnmpAdminString
_PktcMtaDevSerialNumber_Object=MibScalar
pktcMtaDevSerialNumber=_PktcMtaDevSerialNumber_Object((1,3,6,1,2,1,140,1,1,2),_PktcMtaDevSerialNumber_Type())
pktcMtaDevSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevSerialNumber.setStatus(_A)
_PktcMtaDevSwCurrentVers_Type=SnmpAdminString
_PktcMtaDevSwCurrentVers_Object=MibScalar
pktcMtaDevSwCurrentVers=_PktcMtaDevSwCurrentVers_Object((1,3,6,1,2,1,140,1,1,3),_PktcMtaDevSwCurrentVers_Type())
pktcMtaDevSwCurrentVers.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevSwCurrentVers.setStatus(_A)
_PktcMtaDevFQDN_Type=SnmpAdminString
_PktcMtaDevFQDN_Object=MibScalar
pktcMtaDevFQDN=_PktcMtaDevFQDN_Object((1,3,6,1,2,1,140,1,1,4),_PktcMtaDevFQDN_Type())
pktcMtaDevFQDN.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevFQDN.setStatus(_A)
class _PktcMtaDevEndPntCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PktcMtaDevEndPntCount_Type.__name__=_D
_PktcMtaDevEndPntCount_Object=MibScalar
pktcMtaDevEndPntCount=_PktcMtaDevEndPntCount_Object((1,3,6,1,2,1,140,1,1,5),_PktcMtaDevEndPntCount_Type())
pktcMtaDevEndPntCount.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevEndPntCount.setStatus(_A)
_PktcMtaDevEnabled_Type=TruthValue
_PktcMtaDevEnabled_Object=MibScalar
pktcMtaDevEnabled=_PktcMtaDevEnabled_Object((1,3,6,1,2,1,140,1,1,6),_PktcMtaDevEnabled_Type())
pktcMtaDevEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcMtaDevEnabled.setStatus(_A)
_PktcMtaDevTypeIdentifier_Type=SnmpAdminString
_PktcMtaDevTypeIdentifier_Object=MibScalar
pktcMtaDevTypeIdentifier=_PktcMtaDevTypeIdentifier_Object((1,3,6,1,2,1,140,1,1,7),_PktcMtaDevTypeIdentifier_Type())
pktcMtaDevTypeIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevTypeIdentifier.setStatus(_A)
class _PktcMtaDevProvisioningState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('pass',1),('inProgress',2),('failConfigFileError',3),('passWithWarnings',4),('passWithIncompleteParsing',5),('failureInternalError',6),('failureOtherReason',7)))
_PktcMtaDevProvisioningState_Type.__name__=_N
_PktcMtaDevProvisioningState_Object=MibScalar
pktcMtaDevProvisioningState=_PktcMtaDevProvisioningState_Object((1,3,6,1,2,1,140,1,1,8),_PktcMtaDevProvisioningState_Type())
pktcMtaDevProvisioningState.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevProvisioningState.setStatus(_A)
_PktcMtaDevHttpAccess_Type=TruthValue
_PktcMtaDevHttpAccess_Object=MibScalar
pktcMtaDevHttpAccess=_PktcMtaDevHttpAccess_Object((1,3,6,1,2,1,140,1,1,9),_PktcMtaDevHttpAccess_Type())
pktcMtaDevHttpAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevHttpAccess.setStatus(_A)
class _PktcMtaDevProvisioningTimer_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_PktcMtaDevProvisioningTimer_Type.__name__=_D
_PktcMtaDevProvisioningTimer_Object=MibScalar
pktcMtaDevProvisioningTimer=_PktcMtaDevProvisioningTimer_Object((1,3,6,1,2,1,140,1,1,10),_PktcMtaDevProvisioningTimer_Type())
pktcMtaDevProvisioningTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcMtaDevProvisioningTimer.setStatus(_A)
if mibBuilder.loadTexts:pktcMtaDevProvisioningTimer.setUnits(_O)
_PktcMtaDevProvisioningCounter_Type=Counter32
_PktcMtaDevProvisioningCounter_Object=MibScalar
pktcMtaDevProvisioningCounter=_PktcMtaDevProvisioningCounter_Object((1,3,6,1,2,1,140,1,1,11),_PktcMtaDevProvisioningCounter_Type())
pktcMtaDevProvisioningCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevProvisioningCounter.setStatus(_A)
_PktcMtaDevErrorOidsTable_Object=MibTable
pktcMtaDevErrorOidsTable=_PktcMtaDevErrorOidsTable_Object((1,3,6,1,2,1,140,1,1,12))
if mibBuilder.loadTexts:pktcMtaDevErrorOidsTable.setStatus(_A)
_PktcMtaDevErrorOidsEntry_Object=MibTableRow
pktcMtaDevErrorOidsEntry=_PktcMtaDevErrorOidsEntry_Object((1,3,6,1,2,1,140,1,1,12,1))
pktcMtaDevErrorOidsEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:pktcMtaDevErrorOidsEntry.setStatus(_A)
class _PktcMtaDevErrorOidIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_PktcMtaDevErrorOidIndex_Type.__name__=_D
_PktcMtaDevErrorOidIndex_Object=MibTableColumn
pktcMtaDevErrorOidIndex=_PktcMtaDevErrorOidIndex_Object((1,3,6,1,2,1,140,1,1,12,1,1),_PktcMtaDevErrorOidIndex_Type())
pktcMtaDevErrorOidIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:pktcMtaDevErrorOidIndex.setStatus(_A)
_PktcMtaDevErrorOid_Type=SnmpAdminString
_PktcMtaDevErrorOid_Object=MibTableColumn
pktcMtaDevErrorOid=_PktcMtaDevErrorOid_Object((1,3,6,1,2,1,140,1,1,12,1,2),_PktcMtaDevErrorOid_Type())
pktcMtaDevErrorOid.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevErrorOid.setStatus(_A)
_PktcMtaDevErrorValue_Type=SnmpAdminString
_PktcMtaDevErrorValue_Object=MibTableColumn
pktcMtaDevErrorValue=_PktcMtaDevErrorValue_Object((1,3,6,1,2,1,140,1,1,12,1,3),_PktcMtaDevErrorValue_Type())
pktcMtaDevErrorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevErrorValue.setStatus(_A)
_PktcMtaDevErrorReason_Type=SnmpAdminString
_PktcMtaDevErrorReason_Object=MibTableColumn
pktcMtaDevErrorReason=_PktcMtaDevErrorReason_Object((1,3,6,1,2,1,140,1,1,12,1,4),_PktcMtaDevErrorReason_Type())
pktcMtaDevErrorReason.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevErrorReason.setStatus(_A)
_PktcMtaDevServer_ObjectIdentity=ObjectIdentity
pktcMtaDevServer=_PktcMtaDevServer_ObjectIdentity((1,3,6,1,2,1,140,1,2))
class _PktcMtaDevDhcpServerAddressType_Type(InetAddressType):defaultValue=1
_PktcMtaDevDhcpServerAddressType_Type.__name__=_I
_PktcMtaDevDhcpServerAddressType_Object=MibScalar
pktcMtaDevDhcpServerAddressType=_PktcMtaDevDhcpServerAddressType_Object((1,3,6,1,2,1,140,1,2,1),_PktcMtaDevDhcpServerAddressType_Type())
pktcMtaDevDhcpServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevDhcpServerAddressType.setStatus(_A)
_PktcMtaDevServerDhcp1_Type=InetAddress
_PktcMtaDevServerDhcp1_Object=MibScalar
pktcMtaDevServerDhcp1=_PktcMtaDevServerDhcp1_Object((1,3,6,1,2,1,140,1,2,2),_PktcMtaDevServerDhcp1_Type())
pktcMtaDevServerDhcp1.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevServerDhcp1.setStatus(_A)
_PktcMtaDevServerDhcp2_Type=InetAddress
_PktcMtaDevServerDhcp2_Object=MibScalar
pktcMtaDevServerDhcp2=_PktcMtaDevServerDhcp2_Object((1,3,6,1,2,1,140,1,2,3),_PktcMtaDevServerDhcp2_Type())
pktcMtaDevServerDhcp2.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevServerDhcp2.setStatus(_A)
class _PktcMtaDevDnsServerAddressType_Type(InetAddressType):defaultValue=1
_PktcMtaDevDnsServerAddressType_Type.__name__=_I
_PktcMtaDevDnsServerAddressType_Object=MibScalar
pktcMtaDevDnsServerAddressType=_PktcMtaDevDnsServerAddressType_Object((1,3,6,1,2,1,140,1,2,4),_PktcMtaDevDnsServerAddressType_Type())
pktcMtaDevDnsServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevDnsServerAddressType.setStatus(_A)
_PktcMtaDevServerDns1_Type=InetAddress
_PktcMtaDevServerDns1_Object=MibScalar
pktcMtaDevServerDns1=_PktcMtaDevServerDns1_Object((1,3,6,1,2,1,140,1,2,5),_PktcMtaDevServerDns1_Type())
pktcMtaDevServerDns1.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcMtaDevServerDns1.setStatus(_A)
_PktcMtaDevServerDns2_Type=InetAddress
_PktcMtaDevServerDns2_Object=MibScalar
pktcMtaDevServerDns2=_PktcMtaDevServerDns2_Object((1,3,6,1,2,1,140,1,2,6),_PktcMtaDevServerDns2_Type())
pktcMtaDevServerDns2.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcMtaDevServerDns2.setStatus(_A)
class _PktcMtaDevTimeServerAddressType_Type(InetAddressType):defaultValue=1
_PktcMtaDevTimeServerAddressType_Type.__name__=_I
_PktcMtaDevTimeServerAddressType_Object=MibScalar
pktcMtaDevTimeServerAddressType=_PktcMtaDevTimeServerAddressType_Object((1,3,6,1,2,1,140,1,2,7),_PktcMtaDevTimeServerAddressType_Type())
pktcMtaDevTimeServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevTimeServerAddressType.setStatus(_A)
_PktcMtaDevTimeServer_Type=InetAddress
_PktcMtaDevTimeServer_Object=MibScalar
pktcMtaDevTimeServer=_PktcMtaDevTimeServer_Object((1,3,6,1,2,1,140,1,2,8),_PktcMtaDevTimeServer_Type())
pktcMtaDevTimeServer.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcMtaDevTimeServer.setStatus(_A)
_PktcMtaDevConfigFile_Type=SnmpAdminString
_PktcMtaDevConfigFile_Object=MibScalar
pktcMtaDevConfigFile=_PktcMtaDevConfigFile_Object((1,3,6,1,2,1,140,1,2,9),_PktcMtaDevConfigFile_Type())
pktcMtaDevConfigFile.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcMtaDevConfigFile.setStatus(_A)
_PktcMtaDevSnmpEntity_Type=SnmpAdminString
_PktcMtaDevSnmpEntity_Object=MibScalar
pktcMtaDevSnmpEntity=_PktcMtaDevSnmpEntity_Object((1,3,6,1,2,1,140,1,2,10),_PktcMtaDevSnmpEntity_Type())
pktcMtaDevSnmpEntity.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevSnmpEntity.setStatus(_A)
class _PktcMtaDevProvConfigHash_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_PktcMtaDevProvConfigHash_Type.__name__=_K
_PktcMtaDevProvConfigHash_Object=MibScalar
pktcMtaDevProvConfigHash=_PktcMtaDevProvConfigHash_Object((1,3,6,1,2,1,140,1,2,11),_PktcMtaDevProvConfigHash_Type())
pktcMtaDevProvConfigHash.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcMtaDevProvConfigHash.setStatus(_A)
class _PktcMtaDevProvConfigKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_PktcMtaDevProvConfigKey_Type.__name__=_K
_PktcMtaDevProvConfigKey_Object=MibScalar
pktcMtaDevProvConfigKey=_PktcMtaDevProvConfigKey_Object((1,3,6,1,2,1,140,1,2,12),_PktcMtaDevProvConfigKey_Type())
pktcMtaDevProvConfigKey.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcMtaDevProvConfigKey.setStatus(_A)
class _PktcMtaDevProvConfigEncryptAlg_Type(PktcMtaDevProvEncryptAlg):defaultValue=1
_PktcMtaDevProvConfigEncryptAlg_Type.__name__=_c
_PktcMtaDevProvConfigEncryptAlg_Object=MibScalar
pktcMtaDevProvConfigEncryptAlg=_PktcMtaDevProvConfigEncryptAlg_Object((1,3,6,1,2,1,140,1,2,13),_PktcMtaDevProvConfigEncryptAlg_Type())
pktcMtaDevProvConfigEncryptAlg.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcMtaDevProvConfigEncryptAlg.setStatus(_A)
class _PktcMtaDevProvSolicitedKeyTimeout_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_PktcMtaDevProvSolicitedKeyTimeout_Type.__name__=_D
_PktcMtaDevProvSolicitedKeyTimeout_Object=MibScalar
pktcMtaDevProvSolicitedKeyTimeout=_PktcMtaDevProvSolicitedKeyTimeout_Object((1,3,6,1,2,1,140,1,2,14),_PktcMtaDevProvSolicitedKeyTimeout_Type())
pktcMtaDevProvSolicitedKeyTimeout.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcMtaDevProvSolicitedKeyTimeout.setStatus(_A)
if mibBuilder.loadTexts:pktcMtaDevProvSolicitedKeyTimeout.setUnits(_G)
class _PktcMtaDevProvUnsolicitedKeyMaxTimeout_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_PktcMtaDevProvUnsolicitedKeyMaxTimeout_Type.__name__=_D
_PktcMtaDevProvUnsolicitedKeyMaxTimeout_Object=MibScalar
pktcMtaDevProvUnsolicitedKeyMaxTimeout=_PktcMtaDevProvUnsolicitedKeyMaxTimeout_Object((1,3,6,1,2,1,140,1,2,15),_PktcMtaDevProvUnsolicitedKeyMaxTimeout_Type())
pktcMtaDevProvUnsolicitedKeyMaxTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevProvUnsolicitedKeyMaxTimeout.setStatus(_A)
if mibBuilder.loadTexts:pktcMtaDevProvUnsolicitedKeyMaxTimeout.setUnits(_G)
class _PktcMtaDevProvUnsolicitedKeyNomTimeout_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_PktcMtaDevProvUnsolicitedKeyNomTimeout_Type.__name__=_D
_PktcMtaDevProvUnsolicitedKeyNomTimeout_Object=MibScalar
pktcMtaDevProvUnsolicitedKeyNomTimeout=_PktcMtaDevProvUnsolicitedKeyNomTimeout_Object((1,3,6,1,2,1,140,1,2,16),_PktcMtaDevProvUnsolicitedKeyNomTimeout_Type())
pktcMtaDevProvUnsolicitedKeyNomTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevProvUnsolicitedKeyNomTimeout.setStatus(_A)
if mibBuilder.loadTexts:pktcMtaDevProvUnsolicitedKeyNomTimeout.setUnits(_G)
class _PktcMtaDevProvUnsolicitedKeyMaxRetries_Type(Unsigned32):defaultValue=8;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_PktcMtaDevProvUnsolicitedKeyMaxRetries_Type.__name__=_D
_PktcMtaDevProvUnsolicitedKeyMaxRetries_Object=MibScalar
pktcMtaDevProvUnsolicitedKeyMaxRetries=_PktcMtaDevProvUnsolicitedKeyMaxRetries_Object((1,3,6,1,2,1,140,1,2,17),_PktcMtaDevProvUnsolicitedKeyMaxRetries_Type())
pktcMtaDevProvUnsolicitedKeyMaxRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevProvUnsolicitedKeyMaxRetries.setStatus(_A)
class _PktcMtaDevProvKerbRealmName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_PktcMtaDevProvKerbRealmName_Type.__name__=_H
_PktcMtaDevProvKerbRealmName_Object=MibScalar
pktcMtaDevProvKerbRealmName=_PktcMtaDevProvKerbRealmName_Object((1,3,6,1,2,1,140,1,2,18),_PktcMtaDevProvKerbRealmName_Type())
pktcMtaDevProvKerbRealmName.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevProvKerbRealmName.setStatus(_A)
class _PktcMtaDevProvState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('operational',1),('waitingForSnmpSetInfo',2),('waitingForTftpAddrResponse',3),('waitingForConfigFile',4)))
_PktcMtaDevProvState_Type.__name__=_N
_PktcMtaDevProvState_Object=MibScalar
pktcMtaDevProvState=_PktcMtaDevProvState_Object((1,3,6,1,2,1,140,1,2,19),_PktcMtaDevProvState_Type())
pktcMtaDevProvState.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevProvState.setStatus(_A)
_PktcMtaDevSecurity_ObjectIdentity=ObjectIdentity
pktcMtaDevSecurity=_PktcMtaDevSecurity_ObjectIdentity((1,3,6,1,2,1,140,1,3))
_PktcMtaDevManufacturerCertificate_Type=DocsX509ASN1DEREncodedCertificate
_PktcMtaDevManufacturerCertificate_Object=MibScalar
pktcMtaDevManufacturerCertificate=_PktcMtaDevManufacturerCertificate_Object((1,3,6,1,2,1,140,1,3,1),_PktcMtaDevManufacturerCertificate_Type())
pktcMtaDevManufacturerCertificate.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevManufacturerCertificate.setStatus(_A)
_PktcMtaDevCertificate_Type=DocsX509ASN1DEREncodedCertificate
_PktcMtaDevCertificate_Object=MibScalar
pktcMtaDevCertificate=_PktcMtaDevCertificate_Object((1,3,6,1,2,1,140,1,3,2),_PktcMtaDevCertificate_Type())
pktcMtaDevCertificate.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevCertificate.setStatus(_A)
_PktcMtaDevCorrelationId_Type=Unsigned32
_PktcMtaDevCorrelationId_Object=MibScalar
pktcMtaDevCorrelationId=_PktcMtaDevCorrelationId_Object((1,3,6,1,2,1,140,1,3,3),_PktcMtaDevCorrelationId_Type())
pktcMtaDevCorrelationId.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevCorrelationId.setStatus(_A)
_PktcMtaDevTelephonyRootCertificate_Type=DocsX509ASN1DEREncodedCertificate
_PktcMtaDevTelephonyRootCertificate_Object=MibScalar
pktcMtaDevTelephonyRootCertificate=_PktcMtaDevTelephonyRootCertificate_Object((1,3,6,1,2,1,140,1,3,4),_PktcMtaDevTelephonyRootCertificate_Type())
pktcMtaDevTelephonyRootCertificate.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevTelephonyRootCertificate.setStatus(_A)
class _PktcMtaDevRealmAvailSlot_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_PktcMtaDevRealmAvailSlot_Type.__name__=_D
_PktcMtaDevRealmAvailSlot_Object=MibScalar
pktcMtaDevRealmAvailSlot=_PktcMtaDevRealmAvailSlot_Object((1,3,6,1,2,1,140,1,3,5),_PktcMtaDevRealmAvailSlot_Type())
pktcMtaDevRealmAvailSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevRealmAvailSlot.setStatus(_A)
_PktcMtaDevRealmTable_Object=MibTable
pktcMtaDevRealmTable=_PktcMtaDevRealmTable_Object((1,3,6,1,2,1,140,1,3,6))
if mibBuilder.loadTexts:pktcMtaDevRealmTable.setStatus(_A)
_PktcMtaDevRealmEntry_Object=MibTableRow
pktcMtaDevRealmEntry=_PktcMtaDevRealmEntry_Object((1,3,6,1,2,1,140,1,3,6,1))
pktcMtaDevRealmEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:pktcMtaDevRealmEntry.setStatus(_A)
class _PktcMtaDevRealmIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PktcMtaDevRealmIndex_Type.__name__=_D
_PktcMtaDevRealmIndex_Object=MibTableColumn
pktcMtaDevRealmIndex=_PktcMtaDevRealmIndex_Object((1,3,6,1,2,1,140,1,3,6,1,1),_PktcMtaDevRealmIndex_Type())
pktcMtaDevRealmIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:pktcMtaDevRealmIndex.setStatus(_A)
class _PktcMtaDevRealmName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_PktcMtaDevRealmName_Type.__name__=_H
_PktcMtaDevRealmName_Object=MibTableColumn
pktcMtaDevRealmName=_PktcMtaDevRealmName_Object((1,3,6,1,2,1,140,1,3,6,1,2),_PktcMtaDevRealmName_Type())
pktcMtaDevRealmName.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcMtaDevRealmName.setStatus(_A)
class _PktcMtaDevRealmPkinitGracePeriod_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,600))
_PktcMtaDevRealmPkinitGracePeriod_Type.__name__=_D
_PktcMtaDevRealmPkinitGracePeriod_Object=MibTableColumn
pktcMtaDevRealmPkinitGracePeriod=_PktcMtaDevRealmPkinitGracePeriod_Object((1,3,6,1,2,1,140,1,3,6,1,3),_PktcMtaDevRealmPkinitGracePeriod_Type())
pktcMtaDevRealmPkinitGracePeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcMtaDevRealmPkinitGracePeriod.setStatus(_A)
if mibBuilder.loadTexts:pktcMtaDevRealmPkinitGracePeriod.setUnits(_O)
class _PktcMtaDevRealmTgsGracePeriod_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_PktcMtaDevRealmTgsGracePeriod_Type.__name__=_D
_PktcMtaDevRealmTgsGracePeriod_Object=MibTableColumn
pktcMtaDevRealmTgsGracePeriod=_PktcMtaDevRealmTgsGracePeriod_Object((1,3,6,1,2,1,140,1,3,6,1,4),_PktcMtaDevRealmTgsGracePeriod_Type())
pktcMtaDevRealmTgsGracePeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcMtaDevRealmTgsGracePeriod.setStatus(_A)
if mibBuilder.loadTexts:pktcMtaDevRealmTgsGracePeriod.setUnits(_O)
_PktcMtaDevRealmOrgName_Type=SnmpAdminString
_PktcMtaDevRealmOrgName_Object=MibTableColumn
pktcMtaDevRealmOrgName=_PktcMtaDevRealmOrgName_Object((1,3,6,1,2,1,140,1,3,6,1,5),_PktcMtaDevRealmOrgName_Type())
pktcMtaDevRealmOrgName.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcMtaDevRealmOrgName.setStatus(_A)
class _PktcMtaDevRealmUnsolicitedKeyMaxTimeout_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_PktcMtaDevRealmUnsolicitedKeyMaxTimeout_Type.__name__=_D
_PktcMtaDevRealmUnsolicitedKeyMaxTimeout_Object=MibTableColumn
pktcMtaDevRealmUnsolicitedKeyMaxTimeout=_PktcMtaDevRealmUnsolicitedKeyMaxTimeout_Object((1,3,6,1,2,1,140,1,3,6,1,6),_PktcMtaDevRealmUnsolicitedKeyMaxTimeout_Type())
pktcMtaDevRealmUnsolicitedKeyMaxTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcMtaDevRealmUnsolicitedKeyMaxTimeout.setStatus(_A)
if mibBuilder.loadTexts:pktcMtaDevRealmUnsolicitedKeyMaxTimeout.setUnits(_G)
class _PktcMtaDevRealmUnsolicitedKeyNomTimeout_Type(Unsigned32):defaultValue=3000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,600000))
_PktcMtaDevRealmUnsolicitedKeyNomTimeout_Type.__name__=_D
_PktcMtaDevRealmUnsolicitedKeyNomTimeout_Object=MibTableColumn
pktcMtaDevRealmUnsolicitedKeyNomTimeout=_PktcMtaDevRealmUnsolicitedKeyNomTimeout_Object((1,3,6,1,2,1,140,1,3,6,1,7),_PktcMtaDevRealmUnsolicitedKeyNomTimeout_Type())
pktcMtaDevRealmUnsolicitedKeyNomTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcMtaDevRealmUnsolicitedKeyNomTimeout.setStatus(_A)
if mibBuilder.loadTexts:pktcMtaDevRealmUnsolicitedKeyNomTimeout.setUnits(_Q)
class _PktcMtaDevRealmUnsolicitedKeyMaxRetries_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_PktcMtaDevRealmUnsolicitedKeyMaxRetries_Type.__name__=_D
_PktcMtaDevRealmUnsolicitedKeyMaxRetries_Object=MibTableColumn
pktcMtaDevRealmUnsolicitedKeyMaxRetries=_PktcMtaDevRealmUnsolicitedKeyMaxRetries_Object((1,3,6,1,2,1,140,1,3,6,1,8),_PktcMtaDevRealmUnsolicitedKeyMaxRetries_Type())
pktcMtaDevRealmUnsolicitedKeyMaxRetries.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcMtaDevRealmUnsolicitedKeyMaxRetries.setStatus(_A)
_PktcMtaDevRealmStatus_Type=RowStatus
_PktcMtaDevRealmStatus_Object=MibTableColumn
pktcMtaDevRealmStatus=_PktcMtaDevRealmStatus_Object((1,3,6,1,2,1,140,1,3,6,1,9),_PktcMtaDevRealmStatus_Type())
pktcMtaDevRealmStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcMtaDevRealmStatus.setStatus(_A)
class _PktcMtaDevCmsAvailSlot_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PktcMtaDevCmsAvailSlot_Type.__name__=_D
_PktcMtaDevCmsAvailSlot_Object=MibScalar
pktcMtaDevCmsAvailSlot=_PktcMtaDevCmsAvailSlot_Object((1,3,6,1,2,1,140,1,3,7),_PktcMtaDevCmsAvailSlot_Type())
pktcMtaDevCmsAvailSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevCmsAvailSlot.setStatus(_A)
_PktcMtaDevCmsTable_Object=MibTable
pktcMtaDevCmsTable=_PktcMtaDevCmsTable_Object((1,3,6,1,2,1,140,1,3,8))
if mibBuilder.loadTexts:pktcMtaDevCmsTable.setStatus(_A)
_PktcMtaDevCmsEntry_Object=MibTableRow
pktcMtaDevCmsEntry=_PktcMtaDevCmsEntry_Object((1,3,6,1,2,1,140,1,3,8,1))
pktcMtaDevCmsEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:pktcMtaDevCmsEntry.setStatus(_A)
class _PktcMtaDevCmsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_PktcMtaDevCmsIndex_Type.__name__=_D
_PktcMtaDevCmsIndex_Object=MibTableColumn
pktcMtaDevCmsIndex=_PktcMtaDevCmsIndex_Object((1,3,6,1,2,1,140,1,3,8,1,1),_PktcMtaDevCmsIndex_Type())
pktcMtaDevCmsIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:pktcMtaDevCmsIndex.setStatus(_A)
class _PktcMtaDevCmsFqdn_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_PktcMtaDevCmsFqdn_Type.__name__=_H
_PktcMtaDevCmsFqdn_Object=MibTableColumn
pktcMtaDevCmsFqdn=_PktcMtaDevCmsFqdn_Object((1,3,6,1,2,1,140,1,3,8,1,2),_PktcMtaDevCmsFqdn_Type())
pktcMtaDevCmsFqdn.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcMtaDevCmsFqdn.setStatus(_A)
class _PktcMtaDevCmsKerbRealmName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_PktcMtaDevCmsKerbRealmName_Type.__name__=_H
_PktcMtaDevCmsKerbRealmName_Object=MibTableColumn
pktcMtaDevCmsKerbRealmName=_PktcMtaDevCmsKerbRealmName_Object((1,3,6,1,2,1,140,1,3,8,1,3),_PktcMtaDevCmsKerbRealmName_Type())
pktcMtaDevCmsKerbRealmName.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcMtaDevCmsKerbRealmName.setStatus(_A)
class _PktcMtaDevCmsMaxClockSkew_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
_PktcMtaDevCmsMaxClockSkew_Type.__name__=_D
_PktcMtaDevCmsMaxClockSkew_Object=MibTableColumn
pktcMtaDevCmsMaxClockSkew=_PktcMtaDevCmsMaxClockSkew_Object((1,3,6,1,2,1,140,1,3,8,1,4),_PktcMtaDevCmsMaxClockSkew_Type())
pktcMtaDevCmsMaxClockSkew.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcMtaDevCmsMaxClockSkew.setStatus(_A)
if mibBuilder.loadTexts:pktcMtaDevCmsMaxClockSkew.setUnits(_G)
class _PktcMtaDevCmsSolicitedKeyTimeout_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,30000))
_PktcMtaDevCmsSolicitedKeyTimeout_Type.__name__=_D
_PktcMtaDevCmsSolicitedKeyTimeout_Object=MibTableColumn
pktcMtaDevCmsSolicitedKeyTimeout=_PktcMtaDevCmsSolicitedKeyTimeout_Object((1,3,6,1,2,1,140,1,3,8,1,5),_PktcMtaDevCmsSolicitedKeyTimeout_Type())
pktcMtaDevCmsSolicitedKeyTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcMtaDevCmsSolicitedKeyTimeout.setStatus(_A)
if mibBuilder.loadTexts:pktcMtaDevCmsSolicitedKeyTimeout.setUnits(_Q)
class _PktcMtaDevCmsUnsolicitedKeyMaxTimeout_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_PktcMtaDevCmsUnsolicitedKeyMaxTimeout_Type.__name__=_D
_PktcMtaDevCmsUnsolicitedKeyMaxTimeout_Object=MibTableColumn
pktcMtaDevCmsUnsolicitedKeyMaxTimeout=_PktcMtaDevCmsUnsolicitedKeyMaxTimeout_Object((1,3,6,1,2,1,140,1,3,8,1,6),_PktcMtaDevCmsUnsolicitedKeyMaxTimeout_Type())
pktcMtaDevCmsUnsolicitedKeyMaxTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcMtaDevCmsUnsolicitedKeyMaxTimeout.setStatus(_A)
if mibBuilder.loadTexts:pktcMtaDevCmsUnsolicitedKeyMaxTimeout.setUnits(_G)
class _PktcMtaDevCmsUnsolicitedKeyNomTimeout_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,30000))
_PktcMtaDevCmsUnsolicitedKeyNomTimeout_Type.__name__=_D
_PktcMtaDevCmsUnsolicitedKeyNomTimeout_Object=MibTableColumn
pktcMtaDevCmsUnsolicitedKeyNomTimeout=_PktcMtaDevCmsUnsolicitedKeyNomTimeout_Object((1,3,6,1,2,1,140,1,3,8,1,7),_PktcMtaDevCmsUnsolicitedKeyNomTimeout_Type())
pktcMtaDevCmsUnsolicitedKeyNomTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcMtaDevCmsUnsolicitedKeyNomTimeout.setStatus(_A)
if mibBuilder.loadTexts:pktcMtaDevCmsUnsolicitedKeyNomTimeout.setUnits(_Q)
class _PktcMtaDevCmsUnsolicitedKeyMaxRetries_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_PktcMtaDevCmsUnsolicitedKeyMaxRetries_Type.__name__=_D
_PktcMtaDevCmsUnsolicitedKeyMaxRetries_Object=MibTableColumn
pktcMtaDevCmsUnsolicitedKeyMaxRetries=_PktcMtaDevCmsUnsolicitedKeyMaxRetries_Object((1,3,6,1,2,1,140,1,3,8,1,8),_PktcMtaDevCmsUnsolicitedKeyMaxRetries_Type())
pktcMtaDevCmsUnsolicitedKeyMaxRetries.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcMtaDevCmsUnsolicitedKeyMaxRetries.setStatus(_A)
class _PktcMtaDevCmsIpsecCtrl_Type(TruthValue):defaultValue=1
_PktcMtaDevCmsIpsecCtrl_Type.__name__=_a
_PktcMtaDevCmsIpsecCtrl_Object=MibTableColumn
pktcMtaDevCmsIpsecCtrl=_PktcMtaDevCmsIpsecCtrl_Object((1,3,6,1,2,1,140,1,3,8,1,9),_PktcMtaDevCmsIpsecCtrl_Type())
pktcMtaDevCmsIpsecCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMtaDevCmsIpsecCtrl.setStatus(_A)
_PktcMtaDevCmsStatus_Type=RowStatus
_PktcMtaDevCmsStatus_Object=MibTableColumn
pktcMtaDevCmsStatus=_PktcMtaDevCmsStatus_Object((1,3,6,1,2,1,140,1,3,8,1,10),_PktcMtaDevCmsStatus_Type())
pktcMtaDevCmsStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcMtaDevCmsStatus.setStatus(_A)
class _PktcMtaDevResetKrbTickets_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('invalidateProvOnReboot',0),('invalidateAllCmsOnReboot',1)))
_PktcMtaDevResetKrbTickets_Type.__name__='Bits'
_PktcMtaDevResetKrbTickets_Object=MibScalar
pktcMtaDevResetKrbTickets=_PktcMtaDevResetKrbTickets_Object((1,3,6,1,2,1,140,1,3,9),_PktcMtaDevResetKrbTickets_Type())
pktcMtaDevResetKrbTickets.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcMtaDevResetKrbTickets.setStatus(_A)
_PktcMtaDevErrors_ObjectIdentity=ObjectIdentity
pktcMtaDevErrors=_PktcMtaDevErrors_ObjectIdentity((1,3,6,1,2,1,140,1,4))
_PktcMtaDevErrorsTooManyErrors_ObjectIdentity=ObjectIdentity
pktcMtaDevErrorsTooManyErrors=_PktcMtaDevErrorsTooManyErrors_ObjectIdentity((1,3,6,1,2,1,140,1,4,1))
if mibBuilder.loadTexts:pktcMtaDevErrorsTooManyErrors.setStatus(_A)
_PktcMtaConformance_ObjectIdentity=ObjectIdentity
pktcMtaConformance=_PktcMtaConformance_ObjectIdentity((1,3,6,1,2,1,140,2))
_PktcMtaCompliances_ObjectIdentity=ObjectIdentity
pktcMtaCompliances=_PktcMtaCompliances_ObjectIdentity((1,3,6,1,2,1,140,2,1))
_PktcMtaGroups_ObjectIdentity=ObjectIdentity
pktcMtaGroups=_PktcMtaGroups_ObjectIdentity((1,3,6,1,2,1,140,2,2))
pktcMtaGroup=ObjectGroup((1,3,6,1,2,1,140,2,2,1))
pktcMtaGroup.setObjects(*((_B,_f),(_B,_g),(_B,_R),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_S),(_B,_T),(_B,_o),(_B,_p),(_B,_J),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:pktcMtaGroup.setStatus(_A)
pktcMtaDevProvisioningEnrollment=NotificationType((1,3,6,1,2,1,140,0,1))
pktcMtaDevProvisioningEnrollment.setObjects(*((_Y,_Z),(_B,_R),(_B,_S),(_L,_M),(_B,_J)))
if mibBuilder.loadTexts:pktcMtaDevProvisioningEnrollment.setStatus(_A)
pktcMtaDevProvisioningStatus=NotificationType((1,3,6,1,2,1,140,0,2))
pktcMtaDevProvisioningStatus.setObjects(*((_L,_M),(_B,_J),(_B,_T)))
if mibBuilder.loadTexts:pktcMtaDevProvisioningStatus.setStatus(_A)
pktcMtaNotificationGroup=NotificationGroup((1,3,6,1,2,1,140,2,2,2))
pktcMtaNotificationGroup.setObjects(*((_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:pktcMtaNotificationGroup.setStatus(_A)
pktcMtaBasicCompliance=ModuleCompliance((1,3,6,1,2,1,140,2,1,1))
pktcMtaBasicCompliance.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:pktcMtaBasicCompliance.setStatus(_A)
pktcMtaBasicSmtaCompliance=ModuleCompliance((1,3,6,1,2,1,140,2,1,2))
pktcMtaBasicSmtaCompliance.setObjects(*((_B,_U),(_B,_V),(_W,_X)))
if mibBuilder.loadTexts:pktcMtaBasicSmtaCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_c:PktcMtaDevProvEncryptAlg,'pktcIetfMtaMib':pktcIetfMtaMib,'pktcMtaNotification':pktcMtaNotification,_AX:pktcMtaDevProvisioningEnrollment,_AW:pktcMtaDevProvisioningStatus,'pktcMtaMibObjects':pktcMtaMibObjects,'pktcMtaDevBase':pktcMtaDevBase,_f:pktcMtaDevResetNow,_g:pktcMtaDevSerialNumber,_R:pktcMtaDevSwCurrentVers,_h:pktcMtaDevFQDN,_i:pktcMtaDevEndPntCount,_j:pktcMtaDevEnabled,_S:pktcMtaDevTypeIdentifier,_T:pktcMtaDevProvisioningState,_o:pktcMtaDevHttpAccess,_AU:pktcMtaDevProvisioningTimer,_k:pktcMtaDevProvisioningCounter,'pktcMtaDevErrorOidsTable':pktcMtaDevErrorOidsTable,'pktcMtaDevErrorOidsEntry':pktcMtaDevErrorOidsEntry,_b:pktcMtaDevErrorOidIndex,_l:pktcMtaDevErrorOid,_m:pktcMtaDevErrorValue,_n:pktcMtaDevErrorReason,'pktcMtaDevServer':pktcMtaDevServer,_r:pktcMtaDevDhcpServerAddressType,_v:pktcMtaDevServerDhcp1,_w:pktcMtaDevServerDhcp2,_s:pktcMtaDevDnsServerAddressType,_x:pktcMtaDevServerDns1,_y:pktcMtaDevServerDns2,_t:pktcMtaDevTimeServerAddressType,_z:pktcMtaDevTimeServer,_A0:pktcMtaDevConfigFile,_A1:pktcMtaDevSnmpEntity,_AR:pktcMtaDevProvConfigHash,_AS:pktcMtaDevProvConfigKey,_u:pktcMtaDevProvConfigEncryptAlg,_AQ:pktcMtaDevProvSolicitedKeyTimeout,_AM:pktcMtaDevProvUnsolicitedKeyMaxTimeout,_AN:pktcMtaDevProvUnsolicitedKeyNomTimeout,_AO:pktcMtaDevProvUnsolicitedKeyMaxRetries,_AP:pktcMtaDevProvKerbRealmName,_AT:pktcMtaDevProvState,'pktcMtaDevSecurity':pktcMtaDevSecurity,_q:pktcMtaDevManufacturerCertificate,_p:pktcMtaDevCertificate,_J:pktcMtaDevCorrelationId,_AV:pktcMtaDevTelephonyRootCertificate,_A4:pktcMtaDevRealmAvailSlot,'pktcMtaDevRealmTable':pktcMtaDevRealmTable,'pktcMtaDevRealmEntry':pktcMtaDevRealmEntry,_d:pktcMtaDevRealmIndex,_A5:pktcMtaDevRealmName,_A2:pktcMtaDevRealmPkinitGracePeriod,_A3:pktcMtaDevRealmTgsGracePeriod,_A6:pktcMtaDevRealmOrgName,_A7:pktcMtaDevRealmUnsolicitedKeyMaxTimeout,_A8:pktcMtaDevRealmUnsolicitedKeyNomTimeout,_A9:pktcMtaDevRealmUnsolicitedKeyMaxRetries,_AA:pktcMtaDevRealmStatus,_AB:pktcMtaDevCmsAvailSlot,'pktcMtaDevCmsTable':pktcMtaDevCmsTable,'pktcMtaDevCmsEntry':pktcMtaDevCmsEntry,_e:pktcMtaDevCmsIndex,_AC:pktcMtaDevCmsFqdn,_AD:pktcMtaDevCmsKerbRealmName,_AI:pktcMtaDevCmsMaxClockSkew,_AH:pktcMtaDevCmsSolicitedKeyTimeout,_AE:pktcMtaDevCmsUnsolicitedKeyMaxTimeout,_AF:pktcMtaDevCmsUnsolicitedKeyNomTimeout,_AG:pktcMtaDevCmsUnsolicitedKeyMaxRetries,_AJ:pktcMtaDevCmsIpsecCtrl,_AK:pktcMtaDevCmsStatus,_AL:pktcMtaDevResetKrbTickets,'pktcMtaDevErrors':pktcMtaDevErrors,'pktcMtaDevErrorsTooManyErrors':pktcMtaDevErrorsTooManyErrors,'pktcMtaConformance':pktcMtaConformance,'pktcMtaCompliances':pktcMtaCompliances,'pktcMtaBasicCompliance':pktcMtaBasicCompliance,'pktcMtaBasicSmtaCompliance':pktcMtaBasicSmtaCompliance,'pktcMtaGroups':pktcMtaGroups,_U:pktcMtaGroup,_V:pktcMtaNotificationGroup})