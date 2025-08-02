_T='cienaWsEncryptionGroup'
_S='entityCertificate'
_R='signingCACertificate'
_Q='warmRestartType'
_P='authenticationMaterialType'
_O='encryptionPreSharedKeyDescription'
_N='encryptionPreSharedKeyStatus'
_M='encryptionPreSharedKeyFingerprint'
_L='encryptionPreSharedChannelDescr'
_K='peerAuthenticationStatusUpdateTime'
_J='peerAuthenticationStatus'
_I='channelDescr'
_H='systemEncryptionTableSnmpKey'
_G='unknown'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='CIENA-WS-PLATFORM-ENCRYPTION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaWsPlatformConfig,=mibBuilder.importSymbols('CIENA-WS-MIB','cienaWsPlatformConfig')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cienaWsPlatformEncryptionMIB=ModuleIdentity((1,3,6,1,4,1,1271,3,5,23))
if mibBuilder.loadTexts:cienaWsPlatformEncryptionMIB.setRevisions(('2018-08-22 00:00','2018-07-16 00:00'))
class AuthenticationMaterialType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('preSharedKey',1),('certificateECC',2)))
class WarmRestartType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('fips',1),('nonFIPS',2)))
_CienaWsEncryptionObjects_ObjectIdentity=ObjectIdentity
cienaWsEncryptionObjects=_CienaWsEncryptionObjects_ObjectIdentity((1,3,6,1,4,1,1271,3,5,23,1))
_CienaWsEncryptionConformance_ObjectIdentity=ObjectIdentity
cienaWsEncryptionConformance=_CienaWsEncryptionConformance_ObjectIdentity((1,3,6,1,4,1,1271,3,5,23,2))
_CienaWsEncryptionGroups_ObjectIdentity=ObjectIdentity
cienaWsEncryptionGroups=_CienaWsEncryptionGroups_ObjectIdentity((1,3,6,1,4,1,1271,3,5,23,2,1))
_CienaWsEncryptionCompliances_ObjectIdentity=ObjectIdentity
cienaWsEncryptionCompliances=_CienaWsEncryptionCompliances_ObjectIdentity((1,3,6,1,4,1,1271,3,5,23,2,2))
_ChannelEncryptionTable_Object=MibTable
channelEncryptionTable=_ChannelEncryptionTable_Object((1,3,6,1,4,1,1271,3,5,23,3))
if mibBuilder.loadTexts:channelEncryptionTable.setStatus(_A)
_ChannelEncryptionEntry_Object=MibTableRow
channelEncryptionEntry=_ChannelEncryptionEntry_Object((1,3,6,1,4,1,1271,3,5,23,3,1))
channelEncryptionEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:channelEncryptionEntry.setStatus(_A)
_ChannelDescr_Type=DisplayString
_ChannelDescr_Object=MibTableColumn
channelDescr=_ChannelDescr_Object((1,3,6,1,4,1,1271,3,5,23,3,1,1),_ChannelDescr_Type())
channelDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:channelDescr.setStatus(_A)
class _PeerAuthenticationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('pass',1),('fail',2)))
_PeerAuthenticationStatus_Type.__name__=_F
_PeerAuthenticationStatus_Object=MibTableColumn
peerAuthenticationStatus=_PeerAuthenticationStatus_Object((1,3,6,1,4,1,1271,3,5,23,3,1,2),_PeerAuthenticationStatus_Type())
peerAuthenticationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:peerAuthenticationStatus.setStatus(_A)
_PeerAuthenticationStatusUpdateTime_Type=DisplayString
_PeerAuthenticationStatusUpdateTime_Object=MibTableColumn
peerAuthenticationStatusUpdateTime=_PeerAuthenticationStatusUpdateTime_Object((1,3,6,1,4,1,1271,3,5,23,3,1,3),_PeerAuthenticationStatusUpdateTime_Type())
peerAuthenticationStatusUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:peerAuthenticationStatusUpdateTime.setStatus(_A)
_EncryptionPreSharedKeyTable_Object=MibTable
encryptionPreSharedKeyTable=_EncryptionPreSharedKeyTable_Object((1,3,6,1,4,1,1271,3,5,23,4))
if mibBuilder.loadTexts:encryptionPreSharedKeyTable.setStatus(_A)
_EncryptionPreSharedKeyEntry_Object=MibTableRow
encryptionPreSharedKeyEntry=_EncryptionPreSharedKeyEntry_Object((1,3,6,1,4,1,1271,3,5,23,4,1))
encryptionPreSharedKeyEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:encryptionPreSharedKeyEntry.setStatus(_A)
_EncryptionPreSharedChannelDescr_Type=DisplayString
_EncryptionPreSharedChannelDescr_Object=MibTableColumn
encryptionPreSharedChannelDescr=_EncryptionPreSharedChannelDescr_Object((1,3,6,1,4,1,1271,3,5,23,4,1,1),_EncryptionPreSharedChannelDescr_Type())
encryptionPreSharedChannelDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:encryptionPreSharedChannelDescr.setStatus(_A)
_EncryptionPreSharedKeyFingerprint_Type=DisplayString
_EncryptionPreSharedKeyFingerprint_Object=MibTableColumn
encryptionPreSharedKeyFingerprint=_EncryptionPreSharedKeyFingerprint_Object((1,3,6,1,4,1,1271,3,5,23,4,1,2),_EncryptionPreSharedKeyFingerprint_Type())
encryptionPreSharedKeyFingerprint.setMaxAccess(_C)
if mibBuilder.loadTexts:encryptionPreSharedKeyFingerprint.setStatus(_A)
_EncryptionPreSharedKeyStatus_Type=TruthValue
_EncryptionPreSharedKeyStatus_Object=MibTableColumn
encryptionPreSharedKeyStatus=_EncryptionPreSharedKeyStatus_Object((1,3,6,1,4,1,1271,3,5,23,4,1,3),_EncryptionPreSharedKeyStatus_Type())
encryptionPreSharedKeyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:encryptionPreSharedKeyStatus.setStatus(_A)
_EncryptionPreSharedKeyDescription_Type=DisplayString
_EncryptionPreSharedKeyDescription_Object=MibTableColumn
encryptionPreSharedKeyDescription=_EncryptionPreSharedKeyDescription_Object((1,3,6,1,4,1,1271,3,5,23,4,1,4),_EncryptionPreSharedKeyDescription_Type())
encryptionPreSharedKeyDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:encryptionPreSharedKeyDescription.setStatus(_A)
_SystemEncryptionTable_Object=MibTable
systemEncryptionTable=_SystemEncryptionTable_Object((1,3,6,1,4,1,1271,3,5,23,5))
if mibBuilder.loadTexts:systemEncryptionTable.setStatus(_A)
_SystemEncryptionEntry_Object=MibTableRow
systemEncryptionEntry=_SystemEncryptionEntry_Object((1,3,6,1,4,1,1271,3,5,23,5,1))
systemEncryptionEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:systemEncryptionEntry.setStatus(_A)
class _SystemEncryptionTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SystemEncryptionTableSnmpKey_Type.__name__=_F
_SystemEncryptionTableSnmpKey_Object=MibTableColumn
systemEncryptionTableSnmpKey=_SystemEncryptionTableSnmpKey_Object((1,3,6,1,4,1,1271,3,5,23,5,1,1),_SystemEncryptionTableSnmpKey_Type())
systemEncryptionTableSnmpKey.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:systemEncryptionTableSnmpKey.setStatus(_A)
_AuthenticationMaterialType_Type=AuthenticationMaterialType
_AuthenticationMaterialType_Object=MibTableColumn
authenticationMaterialType=_AuthenticationMaterialType_Object((1,3,6,1,4,1,1271,3,5,23,5,1,2),_AuthenticationMaterialType_Type())
authenticationMaterialType.setMaxAccess(_C)
if mibBuilder.loadTexts:authenticationMaterialType.setStatus(_A)
_WarmRestartType_Type=WarmRestartType
_WarmRestartType_Object=MibTableColumn
warmRestartType=_WarmRestartType_Object((1,3,6,1,4,1,1271,3,5,23,5,1,3),_WarmRestartType_Type())
warmRestartType.setMaxAccess(_C)
if mibBuilder.loadTexts:warmRestartType.setStatus(_A)
_SigningCACertificate_Type=DisplayString
_SigningCACertificate_Object=MibTableColumn
signingCACertificate=_SigningCACertificate_Object((1,3,6,1,4,1,1271,3,5,23,5,1,4),_SigningCACertificate_Type())
signingCACertificate.setMaxAccess(_C)
if mibBuilder.loadTexts:signingCACertificate.setStatus(_A)
_EntityCertificate_Type=DisplayString
_EntityCertificate_Object=MibTableColumn
entityCertificate=_EntityCertificate_Object((1,3,6,1,4,1,1271,3,5,23,5,1,5),_EntityCertificate_Type())
entityCertificate.setMaxAccess(_C)
if mibBuilder.loadTexts:entityCertificate.setStatus(_A)
cienaWsEncryptionGroup=ObjectGroup((1,3,6,1,4,1,1271,3,5,23,2,1,1))
cienaWsEncryptionGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:cienaWsEncryptionGroup.setStatus(_A)
cienaWsEncryptionCompliance=ModuleCompliance((1,3,6,1,4,1,1271,3,5,23,2,2,1))
cienaWsEncryptionCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:cienaWsEncryptionCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AuthenticationMaterialType':AuthenticationMaterialType,'WarmRestartType':WarmRestartType,'cienaWsPlatformEncryptionMIB':cienaWsPlatformEncryptionMIB,'cienaWsEncryptionObjects':cienaWsEncryptionObjects,'cienaWsEncryptionConformance':cienaWsEncryptionConformance,'cienaWsEncryptionGroups':cienaWsEncryptionGroups,_T:cienaWsEncryptionGroup,'cienaWsEncryptionCompliances':cienaWsEncryptionCompliances,'cienaWsEncryptionCompliance':cienaWsEncryptionCompliance,'channelEncryptionTable':channelEncryptionTable,'channelEncryptionEntry':channelEncryptionEntry,_I:channelDescr,_J:peerAuthenticationStatus,_K:peerAuthenticationStatusUpdateTime,'encryptionPreSharedKeyTable':encryptionPreSharedKeyTable,'encryptionPreSharedKeyEntry':encryptionPreSharedKeyEntry,_L:encryptionPreSharedChannelDescr,_M:encryptionPreSharedKeyFingerprint,_N:encryptionPreSharedKeyStatus,_O:encryptionPreSharedKeyDescription,'systemEncryptionTable':systemEncryptionTable,'systemEncryptionEntry':systemEncryptionEntry,_H:systemEncryptionTableSnmpKey,_P:authenticationMaterialType,_Q:warmRestartType,_R:signingCACertificate,_S:entityCertificate})