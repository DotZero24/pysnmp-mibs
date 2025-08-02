_y='devIDMIBAuditGroup'
_x='devIDMIBCertificateGroup'
_w='devIDMIBModuleGroup'
_v='devIDMIBObjectGroup'
_u='devIDStatisticCertDeletionCount'
_t='devIDStatisticCertInsertionCount'
_s='devIDChainCert'
_r='devIDChainCertFingerprint'
_q='devIDCert'
_p='devIDCertEnabled'
_o='devIDCertKeyEnabled'
_n='devIDCertIDevID'
_m='devIDCertPublicKeyInfoFprint'
_l='devIDModuleInsertsLDevIDKeys'
_k='devIDModuleGeneratesLDevIDKeys'
_j='devIDModuleSupportsLDevIDs'
_i='devIDStatisticCredentialDeletionCount'
_h='devIDStatisticCredentialInsertionCount'
_g='devIDStatisticCSRGenerationCount'
_f='devIDCredentialErrStatus'
_e='devIDCredentialPubkeyIndex'
_d='devIDCredentialEntityIndex'
_c='devIDCredentialSubjectAltName'
_b='devIDCredentialSubject'
_a='devIDCredentialIssuer'
_Z='devIDCredentialSerialNumber'
_Y='devIDCredentialSHA1Hash'
_X='devIDCredentialEnabled'
_W='devIDCredentialCount'
_V='devIDPublicKeyErrStatus'
_U='devIDPublicKeyPubkeySHA1Hash'
_T='devIDPublicKeyAlgorithm'
_S='devIDPublicKeyEnabled'
_R='devIDPublicKeyCount'
_Q='devIDChainCertIndex'
_P='devIDCredentialIndex'
_O='read-write'
_N='SnmpAdminString'
_M='devIDStatisticKeyDeletionCount'
_L='devIDStatisticKeyInsertionCount'
_K='devIDStatisticKeyGenerationCount'
_J='devIDCertFingerprint'
_I='DevIDErrorStatus'
_H='Unsigned32'
_G='not-accessible'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='obsolete'
_C='current'
_B='read-only'
_A='IEEE8021-DEVID-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndex,entPhysicalIndex=mibBuilder.importSymbols(_E,'PhysicalIndex',_F)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ieee8021DevIDMIB=ModuleIdentity((1,3,111,2,802,1,1,17))
if mibBuilder.loadTexts:ieee8021DevIDMIB.setRevisions(('2018-07-15 19:04','2009-06-25 00:00'))
class DevIDFingerprint(TextualConvention,OctetString):status=_C;displayHint='1x:1x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,49))
class DevIDErrorStatus(TextualConvention,Integer32):status=_D;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('internalError',2)))
class DevIDAlgorithmIdentifier(TextualConvention,Integer32):status=_D;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rsaEncryption',1),('idecPublicKey',2)))
_DevIDMIBNotifications_ObjectIdentity=ObjectIdentity
devIDMIBNotifications=_DevIDMIBNotifications_ObjectIdentity((1,3,111,2,802,1,1,17,0))
_DevIDMIBObjects_ObjectIdentity=ObjectIdentity
devIDMIBObjects=_DevIDMIBObjects_ObjectIdentity((1,3,111,2,802,1,1,17,1))
_DevIDGlobalMIBObjects_ObjectIdentity=ObjectIdentity
devIDGlobalMIBObjects=_DevIDGlobalMIBObjects_ObjectIdentity((1,3,111,2,802,1,1,17,1,1))
_DevIDMgmtMIBObjects_ObjectIdentity=ObjectIdentity
devIDMgmtMIBObjects=_DevIDMgmtMIBObjects_ObjectIdentity((1,3,111,2,802,1,1,17,1,2))
_DevIDPublicKeyCount_Type=Unsigned32
_DevIDPublicKeyCount_Object=MibScalar
devIDPublicKeyCount=_DevIDPublicKeyCount_Object((1,3,111,2,802,1,1,17,1,2,1),_DevIDPublicKeyCount_Type())
devIDPublicKeyCount.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDPublicKeyCount.setStatus(_D)
_DevIDPublicKeyTable_Object=MibTable
devIDPublicKeyTable=_DevIDPublicKeyTable_Object((1,3,111,2,802,1,1,17,1,2,2))
if mibBuilder.loadTexts:devIDPublicKeyTable.setStatus(_D)
_DevIDPublicKeyEntry_Object=MibTableRow
devIDPublicKeyEntry=_DevIDPublicKeyEntry_Object((1,3,111,2,802,1,1,17,1,2,2,1))
devIDPublicKeyEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:devIDPublicKeyEntry.setStatus(_D)
class _DevIDPublicKeyIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_DevIDPublicKeyIndex_Type.__name__=_H
_DevIDPublicKeyIndex_Object=MibTableColumn
devIDPublicKeyIndex=_DevIDPublicKeyIndex_Object((1,3,111,2,802,1,1,17,1,2,2,1,1),_DevIDPublicKeyIndex_Type())
devIDPublicKeyIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:devIDPublicKeyIndex.setStatus(_D)
_DevIDPublicKeyEnabled_Type=TruthValue
_DevIDPublicKeyEnabled_Object=MibTableColumn
devIDPublicKeyEnabled=_DevIDPublicKeyEnabled_Object((1,3,111,2,802,1,1,17,1,2,2,1,2),_DevIDPublicKeyEnabled_Type())
devIDPublicKeyEnabled.setMaxAccess(_O)
if mibBuilder.loadTexts:devIDPublicKeyEnabled.setStatus(_D)
_DevIDPublicKeyAlgorithm_Type=DevIDAlgorithmIdentifier
_DevIDPublicKeyAlgorithm_Object=MibTableColumn
devIDPublicKeyAlgorithm=_DevIDPublicKeyAlgorithm_Object((1,3,111,2,802,1,1,17,1,2,2,1,3),_DevIDPublicKeyAlgorithm_Type())
devIDPublicKeyAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDPublicKeyAlgorithm.setStatus(_D)
_DevIDPublicKeyPubkeySHA1Hash_Type=SnmpAdminString
_DevIDPublicKeyPubkeySHA1Hash_Object=MibTableColumn
devIDPublicKeyPubkeySHA1Hash=_DevIDPublicKeyPubkeySHA1Hash_Object((1,3,111,2,802,1,1,17,1,2,2,1,4),_DevIDPublicKeyPubkeySHA1Hash_Type())
devIDPublicKeyPubkeySHA1Hash.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDPublicKeyPubkeySHA1Hash.setStatus(_D)
class _DevIDPublicKeyErrStatus_Type(DevIDErrorStatus):defaultValue=1
_DevIDPublicKeyErrStatus_Type.__name__=_I
_DevIDPublicKeyErrStatus_Object=MibTableColumn
devIDPublicKeyErrStatus=_DevIDPublicKeyErrStatus_Object((1,3,111,2,802,1,1,17,1,2,2,1,5),_DevIDPublicKeyErrStatus_Type())
devIDPublicKeyErrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDPublicKeyErrStatus.setStatus(_D)
_DevIDCredentialCount_Type=Unsigned32
_DevIDCredentialCount_Object=MibScalar
devIDCredentialCount=_DevIDCredentialCount_Object((1,3,111,2,802,1,1,17,1,2,3),_DevIDCredentialCount_Type())
devIDCredentialCount.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDCredentialCount.setStatus(_D)
_DevIDCredentialTable_Object=MibTable
devIDCredentialTable=_DevIDCredentialTable_Object((1,3,111,2,802,1,1,17,1,2,4))
if mibBuilder.loadTexts:devIDCredentialTable.setStatus(_D)
_DevIDCredentialEntry_Object=MibTableRow
devIDCredentialEntry=_DevIDCredentialEntry_Object((1,3,111,2,802,1,1,17,1,2,4,1))
devIDCredentialEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:devIDCredentialEntry.setStatus(_D)
class _DevIDCredentialIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_DevIDCredentialIndex_Type.__name__=_H
_DevIDCredentialIndex_Object=MibTableColumn
devIDCredentialIndex=_DevIDCredentialIndex_Object((1,3,111,2,802,1,1,17,1,2,4,1,1),_DevIDCredentialIndex_Type())
devIDCredentialIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:devIDCredentialIndex.setStatus(_D)
_DevIDCredentialEnabled_Type=TruthValue
_DevIDCredentialEnabled_Object=MibTableColumn
devIDCredentialEnabled=_DevIDCredentialEnabled_Object((1,3,111,2,802,1,1,17,1,2,4,1,2),_DevIDCredentialEnabled_Type())
devIDCredentialEnabled.setMaxAccess(_O)
if mibBuilder.loadTexts:devIDCredentialEnabled.setStatus(_D)
_DevIDCredentialSHA1Hash_Type=SnmpAdminString
_DevIDCredentialSHA1Hash_Object=MibTableColumn
devIDCredentialSHA1Hash=_DevIDCredentialSHA1Hash_Object((1,3,111,2,802,1,1,17,1,2,4,1,3),_DevIDCredentialSHA1Hash_Type())
devIDCredentialSHA1Hash.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDCredentialSHA1Hash.setStatus(_D)
class _DevIDCredentialSerialNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_DevIDCredentialSerialNumber_Type.__name__=_N
_DevIDCredentialSerialNumber_Object=MibTableColumn
devIDCredentialSerialNumber=_DevIDCredentialSerialNumber_Object((1,3,111,2,802,1,1,17,1,2,4,1,4),_DevIDCredentialSerialNumber_Type())
devIDCredentialSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDCredentialSerialNumber.setStatus(_D)
_DevIDCredentialIssuer_Type=SnmpAdminString
_DevIDCredentialIssuer_Object=MibTableColumn
devIDCredentialIssuer=_DevIDCredentialIssuer_Object((1,3,111,2,802,1,1,17,1,2,4,1,5),_DevIDCredentialIssuer_Type())
devIDCredentialIssuer.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDCredentialIssuer.setStatus(_D)
_DevIDCredentialSubject_Type=SnmpAdminString
_DevIDCredentialSubject_Object=MibTableColumn
devIDCredentialSubject=_DevIDCredentialSubject_Object((1,3,111,2,802,1,1,17,1,2,4,1,6),_DevIDCredentialSubject_Type())
devIDCredentialSubject.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDCredentialSubject.setStatus(_D)
_DevIDCredentialSubjectAltName_Type=SnmpAdminString
_DevIDCredentialSubjectAltName_Object=MibTableColumn
devIDCredentialSubjectAltName=_DevIDCredentialSubjectAltName_Object((1,3,111,2,802,1,1,17,1,2,4,1,7),_DevIDCredentialSubjectAltName_Type())
devIDCredentialSubjectAltName.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDCredentialSubjectAltName.setStatus(_D)
_DevIDCredentialEntityIndex_Type=PhysicalIndex
_DevIDCredentialEntityIndex_Object=MibTableColumn
devIDCredentialEntityIndex=_DevIDCredentialEntityIndex_Object((1,3,111,2,802,1,1,17,1,2,4,1,8),_DevIDCredentialEntityIndex_Type())
devIDCredentialEntityIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDCredentialEntityIndex.setStatus(_D)
_DevIDCredentialPubkeyIndex_Type=Unsigned32
_DevIDCredentialPubkeyIndex_Object=MibTableColumn
devIDCredentialPubkeyIndex=_DevIDCredentialPubkeyIndex_Object((1,3,111,2,802,1,1,17,1,2,4,1,9),_DevIDCredentialPubkeyIndex_Type())
devIDCredentialPubkeyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDCredentialPubkeyIndex.setStatus(_D)
class _DevIDCredentialErrStatus_Type(DevIDErrorStatus):defaultValue=1
_DevIDCredentialErrStatus_Type.__name__=_I
_DevIDCredentialErrStatus_Object=MibTableColumn
devIDCredentialErrStatus=_DevIDCredentialErrStatus_Object((1,3,111,2,802,1,1,17,1,2,4,1,10),_DevIDCredentialErrStatus_Type())
devIDCredentialErrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDCredentialErrStatus.setStatus(_D)
_DevIDStatisticsTable_Object=MibTable
devIDStatisticsTable=_DevIDStatisticsTable_Object((1,3,111,2,802,1,1,17,1,2,5))
if mibBuilder.loadTexts:devIDStatisticsTable.setStatus(_C)
_DevIDStatisticsEntry_Object=MibTableRow
devIDStatisticsEntry=_DevIDStatisticsEntry_Object((1,3,111,2,802,1,1,17,1,2,5,1))
devIDStatisticsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:devIDStatisticsEntry.setStatus(_C)
_DevIDStatisticKeyGenerationCount_Type=Counter32
_DevIDStatisticKeyGenerationCount_Object=MibTableColumn
devIDStatisticKeyGenerationCount=_DevIDStatisticKeyGenerationCount_Object((1,3,111,2,802,1,1,17,1,2,5,1,1),_DevIDStatisticKeyGenerationCount_Type())
devIDStatisticKeyGenerationCount.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDStatisticKeyGenerationCount.setStatus(_C)
_DevIDStatisticKeyInsertionCount_Type=Counter32
_DevIDStatisticKeyInsertionCount_Object=MibTableColumn
devIDStatisticKeyInsertionCount=_DevIDStatisticKeyInsertionCount_Object((1,3,111,2,802,1,1,17,1,2,5,1,2),_DevIDStatisticKeyInsertionCount_Type())
devIDStatisticKeyInsertionCount.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDStatisticKeyInsertionCount.setStatus(_C)
_DevIDStatisticKeyDeletionCount_Type=Counter32
_DevIDStatisticKeyDeletionCount_Object=MibTableColumn
devIDStatisticKeyDeletionCount=_DevIDStatisticKeyDeletionCount_Object((1,3,111,2,802,1,1,17,1,2,5,1,3),_DevIDStatisticKeyDeletionCount_Type())
devIDStatisticKeyDeletionCount.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDStatisticKeyDeletionCount.setStatus(_C)
_DevIDStatisticCSRGenerationCount_Type=Counter32
_DevIDStatisticCSRGenerationCount_Object=MibTableColumn
devIDStatisticCSRGenerationCount=_DevIDStatisticCSRGenerationCount_Object((1,3,111,2,802,1,1,17,1,2,5,1,4),_DevIDStatisticCSRGenerationCount_Type())
devIDStatisticCSRGenerationCount.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDStatisticCSRGenerationCount.setStatus('deprecated')
_DevIDStatisticCredentialInsertionCount_Type=Counter32
_DevIDStatisticCredentialInsertionCount_Object=MibTableColumn
devIDStatisticCredentialInsertionCount=_DevIDStatisticCredentialInsertionCount_Object((1,3,111,2,802,1,1,17,1,2,5,1,5),_DevIDStatisticCredentialInsertionCount_Type())
devIDStatisticCredentialInsertionCount.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDStatisticCredentialInsertionCount.setStatus(_D)
_DevIDStatisticCredentialDeletionCount_Type=Counter32
_DevIDStatisticCredentialDeletionCount_Object=MibTableColumn
devIDStatisticCredentialDeletionCount=_DevIDStatisticCredentialDeletionCount_Object((1,3,111,2,802,1,1,17,1,2,5,1,6),_DevIDStatisticCredentialDeletionCount_Type())
devIDStatisticCredentialDeletionCount.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDStatisticCredentialDeletionCount.setStatus(_D)
_DevIDStatisticCertInsertionCount_Type=Counter32
_DevIDStatisticCertInsertionCount_Object=MibTableColumn
devIDStatisticCertInsertionCount=_DevIDStatisticCertInsertionCount_Object((1,3,111,2,802,1,1,17,1,2,5,1,7),_DevIDStatisticCertInsertionCount_Type())
devIDStatisticCertInsertionCount.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDStatisticCertInsertionCount.setStatus(_C)
_DevIDStatisticCertDeletionCount_Type=Counter32
_DevIDStatisticCertDeletionCount_Object=MibTableColumn
devIDStatisticCertDeletionCount=_DevIDStatisticCertDeletionCount_Object((1,3,111,2,802,1,1,17,1,2,5,1,8),_DevIDStatisticCertDeletionCount_Type())
devIDStatisticCertDeletionCount.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDStatisticCertDeletionCount.setStatus(_C)
_DevIDModuleTable_Object=MibTable
devIDModuleTable=_DevIDModuleTable_Object((1,3,111,2,802,1,1,17,1,2,6))
if mibBuilder.loadTexts:devIDModuleTable.setStatus(_C)
_DevIDModuleEntry_Object=MibTableRow
devIDModuleEntry=_DevIDModuleEntry_Object((1,3,111,2,802,1,1,17,1,2,6,1))
devIDModuleEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:devIDModuleEntry.setStatus(_C)
_DevIDModuleSupportsLDevIDs_Type=TruthValue
_DevIDModuleSupportsLDevIDs_Object=MibTableColumn
devIDModuleSupportsLDevIDs=_DevIDModuleSupportsLDevIDs_Object((1,3,111,2,802,1,1,17,1,2,6,1,1),_DevIDModuleSupportsLDevIDs_Type())
devIDModuleSupportsLDevIDs.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDModuleSupportsLDevIDs.setStatus(_C)
_DevIDModuleGeneratesLDevIDKeys_Type=TruthValue
_DevIDModuleGeneratesLDevIDKeys_Object=MibTableColumn
devIDModuleGeneratesLDevIDKeys=_DevIDModuleGeneratesLDevIDKeys_Object((1,3,111,2,802,1,1,17,1,2,6,1,2),_DevIDModuleGeneratesLDevIDKeys_Type())
devIDModuleGeneratesLDevIDKeys.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDModuleGeneratesLDevIDKeys.setStatus(_C)
_DevIDModuleInsertsLDevIDKeys_Type=TruthValue
_DevIDModuleInsertsLDevIDKeys_Object=MibTableColumn
devIDModuleInsertsLDevIDKeys=_DevIDModuleInsertsLDevIDKeys_Object((1,3,111,2,802,1,1,17,1,2,6,1,3),_DevIDModuleInsertsLDevIDKeys_Type())
devIDModuleInsertsLDevIDKeys.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDModuleInsertsLDevIDKeys.setStatus(_C)
_DevIDCertTable_Object=MibTable
devIDCertTable=_DevIDCertTable_Object((1,3,111,2,802,1,1,17,1,2,7))
if mibBuilder.loadTexts:devIDCertTable.setStatus(_C)
_DevIDCertEntry_Object=MibTableRow
devIDCertEntry=_DevIDCertEntry_Object((1,3,111,2,802,1,1,17,1,2,7,1))
devIDCertEntry.setIndexNames((0,_E,_F),(0,_A,_J))
if mibBuilder.loadTexts:devIDCertEntry.setStatus(_C)
_DevIDCertFingerprint_Type=DevIDFingerprint
_DevIDCertFingerprint_Object=MibTableColumn
devIDCertFingerprint=_DevIDCertFingerprint_Object((1,3,111,2,802,1,1,17,1,2,7,1,1),_DevIDCertFingerprint_Type())
devIDCertFingerprint.setMaxAccess(_G)
if mibBuilder.loadTexts:devIDCertFingerprint.setStatus(_C)
_DevIDCertPublicKeyInfoFprint_Type=DevIDFingerprint
_DevIDCertPublicKeyInfoFprint_Object=MibTableColumn
devIDCertPublicKeyInfoFprint=_DevIDCertPublicKeyInfoFprint_Object((1,3,111,2,802,1,1,17,1,2,7,1,2),_DevIDCertPublicKeyInfoFprint_Type())
devIDCertPublicKeyInfoFprint.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDCertPublicKeyInfoFprint.setStatus(_C)
_DevIDCertIDevID_Type=TruthValue
_DevIDCertIDevID_Object=MibTableColumn
devIDCertIDevID=_DevIDCertIDevID_Object((1,3,111,2,802,1,1,17,1,2,7,1,3),_DevIDCertIDevID_Type())
devIDCertIDevID.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDCertIDevID.setStatus(_C)
_DevIDCertKeyEnabled_Type=TruthValue
_DevIDCertKeyEnabled_Object=MibTableColumn
devIDCertKeyEnabled=_DevIDCertKeyEnabled_Object((1,3,111,2,802,1,1,17,1,2,7,1,4),_DevIDCertKeyEnabled_Type())
devIDCertKeyEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDCertKeyEnabled.setStatus(_C)
_DevIDCertEnabled_Type=TruthValue
_DevIDCertEnabled_Object=MibTableColumn
devIDCertEnabled=_DevIDCertEnabled_Object((1,3,111,2,802,1,1,17,1,2,7,1,5),_DevIDCertEnabled_Type())
devIDCertEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDCertEnabled.setStatus(_C)
_DevIDCert_Type=OctetString
_DevIDCert_Object=MibTableColumn
devIDCert=_DevIDCert_Object((1,3,111,2,802,1,1,17,1,2,7,1,6),_DevIDCert_Type())
devIDCert.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDCert.setStatus(_C)
_DevIDChainTable_Object=MibTable
devIDChainTable=_DevIDChainTable_Object((1,3,111,2,802,1,1,17,1,2,8))
if mibBuilder.loadTexts:devIDChainTable.setStatus(_C)
_DevIDChainEntry_Object=MibTableRow
devIDChainEntry=_DevIDChainEntry_Object((1,3,111,2,802,1,1,17,1,2,8,1))
devIDChainEntry.setIndexNames((0,_E,_F),(0,_A,_J),(0,_A,_Q))
if mibBuilder.loadTexts:devIDChainEntry.setStatus(_C)
_DevIDChainCertIndex_Type=Unsigned32
_DevIDChainCertIndex_Object=MibTableColumn
devIDChainCertIndex=_DevIDChainCertIndex_Object((1,3,111,2,802,1,1,17,1,2,8,1,1),_DevIDChainCertIndex_Type())
devIDChainCertIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:devIDChainCertIndex.setStatus(_C)
_DevIDChainCertFingerprint_Type=DevIDFingerprint
_DevIDChainCertFingerprint_Object=MibTableColumn
devIDChainCertFingerprint=_DevIDChainCertFingerprint_Object((1,3,111,2,802,1,1,17,1,2,8,1,2),_DevIDChainCertFingerprint_Type())
devIDChainCertFingerprint.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDChainCertFingerprint.setStatus(_C)
_DevIDChainCert_Type=OctetString
_DevIDChainCert_Object=MibTableColumn
devIDChainCert=_DevIDChainCert_Object((1,3,111,2,802,1,1,17,1,2,8,1,3),_DevIDChainCert_Type())
devIDChainCert.setMaxAccess(_B)
if mibBuilder.loadTexts:devIDChainCert.setStatus(_C)
_DevIDStatsMIBObjects_ObjectIdentity=ObjectIdentity
devIDStatsMIBObjects=_DevIDStatsMIBObjects_ObjectIdentity((1,3,111,2,802,1,1,17,1,3))
_DevIDMIBConformance_ObjectIdentity=ObjectIdentity
devIDMIBConformance=_DevIDMIBConformance_ObjectIdentity((1,3,111,2,802,1,1,17,2))
_DevIDMIBCompliances_ObjectIdentity=ObjectIdentity
devIDMIBCompliances=_DevIDMIBCompliances_ObjectIdentity((1,3,111,2,802,1,1,17,2,1))
_DevIDMIBGroups_ObjectIdentity=ObjectIdentity
devIDMIBGroups=_DevIDMIBGroups_ObjectIdentity((1,3,111,2,802,1,1,17,2,2))
devIDMIBObjectGroup=ObjectGroup((1,3,111,2,802,1,1,17,2,2,1))
devIDMIBObjectGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_K),(_A,_L),(_A,_M),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:devIDMIBObjectGroup.setStatus(_D)
devIDMIBModuleGroup=ObjectGroup((1,3,111,2,802,1,1,17,2,2,2))
devIDMIBModuleGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:devIDMIBModuleGroup.setStatus(_C)
devIDMIBCertificateGroup=ObjectGroup((1,3,111,2,802,1,1,17,2,2,3))
devIDMIBCertificateGroup.setObjects(*((_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:devIDMIBCertificateGroup.setStatus(_C)
devIDMIBAuditGroup=ObjectGroup((1,3,111,2,802,1,1,17,2,2,4))
devIDMIBAuditGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:devIDMIBAuditGroup.setStatus(_C)
devIDMIBModuleCompliance=ModuleCompliance((1,3,111,2,802,1,1,17,2,1,1))
devIDMIBModuleCompliance.setObjects((_A,_v))
if mibBuilder.loadTexts:devIDMIBModuleCompliance.setStatus(_D)
devIDMIBModuleCompliance2=ModuleCompliance((1,3,111,2,802,1,1,17,2,1,2))
devIDMIBModuleCompliance2.setObjects(*((_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:devIDMIBModuleCompliance2.setStatus(_C)
mibBuilder.exportSymbols(_A,**{'DevIDFingerprint':DevIDFingerprint,_I:DevIDErrorStatus,'DevIDAlgorithmIdentifier':DevIDAlgorithmIdentifier,'ieee8021DevIDMIB':ieee8021DevIDMIB,'devIDMIBNotifications':devIDMIBNotifications,'devIDMIBObjects':devIDMIBObjects,'devIDGlobalMIBObjects':devIDGlobalMIBObjects,'devIDMgmtMIBObjects':devIDMgmtMIBObjects,_R:devIDPublicKeyCount,'devIDPublicKeyTable':devIDPublicKeyTable,'devIDPublicKeyEntry':devIDPublicKeyEntry,'devIDPublicKeyIndex':devIDPublicKeyIndex,_S:devIDPublicKeyEnabled,_T:devIDPublicKeyAlgorithm,_U:devIDPublicKeyPubkeySHA1Hash,_V:devIDPublicKeyErrStatus,_W:devIDCredentialCount,'devIDCredentialTable':devIDCredentialTable,'devIDCredentialEntry':devIDCredentialEntry,_P:devIDCredentialIndex,_X:devIDCredentialEnabled,_Y:devIDCredentialSHA1Hash,_Z:devIDCredentialSerialNumber,_a:devIDCredentialIssuer,_b:devIDCredentialSubject,_c:devIDCredentialSubjectAltName,_d:devIDCredentialEntityIndex,_e:devIDCredentialPubkeyIndex,_f:devIDCredentialErrStatus,'devIDStatisticsTable':devIDStatisticsTable,'devIDStatisticsEntry':devIDStatisticsEntry,_K:devIDStatisticKeyGenerationCount,_L:devIDStatisticKeyInsertionCount,_M:devIDStatisticKeyDeletionCount,_g:devIDStatisticCSRGenerationCount,_h:devIDStatisticCredentialInsertionCount,_i:devIDStatisticCredentialDeletionCount,_t:devIDStatisticCertInsertionCount,_u:devIDStatisticCertDeletionCount,'devIDModuleTable':devIDModuleTable,'devIDModuleEntry':devIDModuleEntry,_j:devIDModuleSupportsLDevIDs,_k:devIDModuleGeneratesLDevIDKeys,_l:devIDModuleInsertsLDevIDKeys,'devIDCertTable':devIDCertTable,'devIDCertEntry':devIDCertEntry,_J:devIDCertFingerprint,_m:devIDCertPublicKeyInfoFprint,_n:devIDCertIDevID,_o:devIDCertKeyEnabled,_p:devIDCertEnabled,_q:devIDCert,'devIDChainTable':devIDChainTable,'devIDChainEntry':devIDChainEntry,_Q:devIDChainCertIndex,_r:devIDChainCertFingerprint,_s:devIDChainCert,'devIDStatsMIBObjects':devIDStatsMIBObjects,'devIDMIBConformance':devIDMIBConformance,'devIDMIBCompliances':devIDMIBCompliances,'devIDMIBModuleCompliance':devIDMIBModuleCompliance,'devIDMIBModuleCompliance2':devIDMIBModuleCompliance2,'devIDMIBGroups':devIDMIBGroups,_v:devIDMIBObjectGroup,_w:devIDMIBModuleGroup,_x:devIDMIBCertificateGroup,_y:devIDMIBAuditGroup})