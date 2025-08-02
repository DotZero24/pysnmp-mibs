_s='ciscoLwappLocalAuthMIBConfigGroupSup1'
_r='ciscoLwappLocalAuthMIBConfigGroup'
_q='cllaEapBroadcastKeyInterval'
_p='cllaEapKeyMaxRetries'
_o='cllaEapKeyTimeout'
_n='cllaEapMaxLoginIgnIdResp'
_m='cllaEapReqMaxRetries'
_l='cllaEapReqTimeout'
_k='cllaEapDynamicWepKeyIndex'
_j='cllaEapIdentityReqMaxRetries'
_i='cllaEapIdentityReqTimeout'
_h='deprecated'
_g='cllaUserCredential'
_f='not-accessible'
_e='cllaEapProfileName'
_d='cLWlanIndex'
_c='CISCO-LWAPP-WLAN-MIB'
_b='cllaEapAuthorityIdLength'
_a='cllaEapServerKey'
_Z='cllaEapAuthorityInfo'
_Y='cllaEapAuthorityId'
_X='cllaEapAnonymousProvEnabled'
_W='cllaEapMethodPacTtl'
_V='cllaUserPriorityNumber'
_U='cllaWlanProfileState'
_T='cllaWlanProfileName'
_S='cllaEapProfileRowStatus'
_R='cllaEapProfileClientCertificateRequired'
_Q='cllaEapProfileLocalCertificateRequired'
_P='cllaEapProfileDateValidityEnabled'
_O='cllaEapProfileCnCertificationIdVerify'
_N='cllaEapProfileCaCertificationCheck'
_M='cllaEapProfileCertIssuer'
_L='cllaEapProfileMethods'
_K='cllaActiveTimeout'
_J='DisplayString'
_I='seconds'
_H='Integer32'
_G='OctetString'
_F='read-create'
_E='TruthValue'
_D='Unsigned32'
_C='read-write'
_B='current'
_A='CISCO-LWAPP-LOCAL-AUTH-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cLWlanIndex,=mibBuilder.importSymbols(_c,_d)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention',_E)
ciscoLwappLocalAuthMIB=ModuleIdentity((1,3,6,1,4,1,9,9,619))
if mibBuilder.loadTexts:ciscoLwappLocalAuthMIB.setRevisions(('2017-04-27 00:00','2010-02-09 00:00','2009-11-24 00:00','2007-03-15 00:00'))
_CiscoLwappLocalAuthMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoLwappLocalAuthMIBNotifs=_CiscoLwappLocalAuthMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,619,0))
_CiscoLwappLocalAuthMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLwappLocalAuthMIBObjects=_CiscoLwappLocalAuthMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,619,1))
_CllaConfig_ObjectIdentity=ObjectIdentity
cllaConfig=_CllaConfig_ObjectIdentity((1,3,6,1,4,1,9,9,619,1,1))
_CllaLocalAuth_ObjectIdentity=ObjectIdentity
cllaLocalAuth=_CllaLocalAuth_ObjectIdentity((1,3,6,1,4,1,9,9,619,1,1,1))
class _CllaActiveTimeout_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_CllaActiveTimeout_Type.__name__=_D
_CllaActiveTimeout_Object=MibScalar
cllaActiveTimeout=_CllaActiveTimeout_Object((1,3,6,1,4,1,9,9,619,1,1,1,1),_CllaActiveTimeout_Type())
cllaActiveTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaActiveTimeout.setStatus(_B)
if mibBuilder.loadTexts:cllaActiveTimeout.setUnits(_I)
class _CllaEapIdentityReqTimeout_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_CllaEapIdentityReqTimeout_Type.__name__=_D
_CllaEapIdentityReqTimeout_Object=MibScalar
cllaEapIdentityReqTimeout=_CllaEapIdentityReqTimeout_Object((1,3,6,1,4,1,9,9,619,1,1,1,2),_CllaEapIdentityReqTimeout_Type())
cllaEapIdentityReqTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaEapIdentityReqTimeout.setStatus(_B)
if mibBuilder.loadTexts:cllaEapIdentityReqTimeout.setUnits(_I)
class _CllaEapIdentityReqMaxRetries_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CllaEapIdentityReqMaxRetries_Type.__name__=_D
_CllaEapIdentityReqMaxRetries_Object=MibScalar
cllaEapIdentityReqMaxRetries=_CllaEapIdentityReqMaxRetries_Object((1,3,6,1,4,1,9,9,619,1,1,1,3),_CllaEapIdentityReqMaxRetries_Type())
cllaEapIdentityReqMaxRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaEapIdentityReqMaxRetries.setStatus(_B)
class _CllaEapDynamicWepKeyIndex_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_CllaEapDynamicWepKeyIndex_Type.__name__=_D
_CllaEapDynamicWepKeyIndex_Object=MibScalar
cllaEapDynamicWepKeyIndex=_CllaEapDynamicWepKeyIndex_Object((1,3,6,1,4,1,9,9,619,1,1,1,4),_CllaEapDynamicWepKeyIndex_Type())
cllaEapDynamicWepKeyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaEapDynamicWepKeyIndex.setStatus(_B)
class _CllaEapReqTimeout_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_CllaEapReqTimeout_Type.__name__=_D
_CllaEapReqTimeout_Object=MibScalar
cllaEapReqTimeout=_CllaEapReqTimeout_Object((1,3,6,1,4,1,9,9,619,1,1,1,5),_CllaEapReqTimeout_Type())
cllaEapReqTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaEapReqTimeout.setStatus(_B)
if mibBuilder.loadTexts:cllaEapReqTimeout.setUnits(_I)
class _CllaEapReqMaxRetries_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_CllaEapReqMaxRetries_Type.__name__=_D
_CllaEapReqMaxRetries_Object=MibScalar
cllaEapReqMaxRetries=_CllaEapReqMaxRetries_Object((1,3,6,1,4,1,9,9,619,1,1,1,6),_CllaEapReqMaxRetries_Type())
cllaEapReqMaxRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaEapReqMaxRetries.setStatus(_B)
class _CllaEapMaxLoginIgnIdResp_Type(TruthValue):defaultValue=1
_CllaEapMaxLoginIgnIdResp_Type.__name__=_E
_CllaEapMaxLoginIgnIdResp_Object=MibScalar
cllaEapMaxLoginIgnIdResp=_CllaEapMaxLoginIgnIdResp_Object((1,3,6,1,4,1,9,9,619,1,1,1,7),_CllaEapMaxLoginIgnIdResp_Type())
cllaEapMaxLoginIgnIdResp.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaEapMaxLoginIgnIdResp.setStatus(_B)
class _CllaEapKeyTimeout_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,5000))
_CllaEapKeyTimeout_Type.__name__=_D
_CllaEapKeyTimeout_Object=MibScalar
cllaEapKeyTimeout=_CllaEapKeyTimeout_Object((1,3,6,1,4,1,9,9,619,1,1,1,8),_CllaEapKeyTimeout_Type())
cllaEapKeyTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaEapKeyTimeout.setStatus(_B)
if mibBuilder.loadTexts:cllaEapKeyTimeout.setUnits('milliseconds')
class _CllaEapKeyMaxRetries_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_CllaEapKeyMaxRetries_Type.__name__=_D
_CllaEapKeyMaxRetries_Object=MibScalar
cllaEapKeyMaxRetries=_CllaEapKeyMaxRetries_Object((1,3,6,1,4,1,9,9,619,1,1,1,9),_CllaEapKeyMaxRetries_Type())
cllaEapKeyMaxRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaEapKeyMaxRetries.setStatus(_B)
class _CllaEapBroadcastKeyInterval_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(120,86400))
_CllaEapBroadcastKeyInterval_Type.__name__=_D
_CllaEapBroadcastKeyInterval_Object=MibScalar
cllaEapBroadcastKeyInterval=_CllaEapBroadcastKeyInterval_Object((1,3,6,1,4,1,9,9,619,1,1,1,10),_CllaEapBroadcastKeyInterval_Type())
cllaEapBroadcastKeyInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaEapBroadcastKeyInterval.setStatus(_B)
if mibBuilder.loadTexts:cllaEapBroadcastKeyInterval.setUnits(_I)
_CllaEapProfileTable_Object=MibTable
cllaEapProfileTable=_CllaEapProfileTable_Object((1,3,6,1,4,1,9,9,619,1,1,2))
if mibBuilder.loadTexts:cllaEapProfileTable.setStatus(_B)
_CllaEapProfileEntry_Object=MibTableRow
cllaEapProfileEntry=_CllaEapProfileEntry_Object((1,3,6,1,4,1,9,9,619,1,1,2,1))
cllaEapProfileEntry.setIndexNames((0,_A,_e))
if mibBuilder.loadTexts:cllaEapProfileEntry.setStatus(_B)
class _CllaEapProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_CllaEapProfileName_Type.__name__=_J
_CllaEapProfileName_Object=MibTableColumn
cllaEapProfileName=_CllaEapProfileName_Object((1,3,6,1,4,1,9,9,619,1,1,2,1,1),_CllaEapProfileName_Type())
cllaEapProfileName.setMaxAccess(_f)
if mibBuilder.loadTexts:cllaEapProfileName.setStatus(_B)
class _CllaEapProfileMethods_Type(Bits):namedValues=NamedValues(*(('none',0),('leap',1),('eapFast',2),('tls',3),('peap',4)))
_CllaEapProfileMethods_Type.__name__='Bits'
_CllaEapProfileMethods_Object=MibTableColumn
cllaEapProfileMethods=_CllaEapProfileMethods_Object((1,3,6,1,4,1,9,9,619,1,1,2,1,2),_CllaEapProfileMethods_Type())
cllaEapProfileMethods.setMaxAccess(_F)
if mibBuilder.loadTexts:cllaEapProfileMethods.setStatus(_B)
class _CllaEapProfileCertIssuer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cisco',1),('vendor',2)))
_CllaEapProfileCertIssuer_Type.__name__=_H
_CllaEapProfileCertIssuer_Object=MibTableColumn
cllaEapProfileCertIssuer=_CllaEapProfileCertIssuer_Object((1,3,6,1,4,1,9,9,619,1,1,2,1,3),_CllaEapProfileCertIssuer_Type())
cllaEapProfileCertIssuer.setMaxAccess(_F)
if mibBuilder.loadTexts:cllaEapProfileCertIssuer.setStatus(_B)
class _CllaEapProfileCaCertificationCheck_Type(TruthValue):defaultValue=1
_CllaEapProfileCaCertificationCheck_Type.__name__=_E
_CllaEapProfileCaCertificationCheck_Object=MibTableColumn
cllaEapProfileCaCertificationCheck=_CllaEapProfileCaCertificationCheck_Object((1,3,6,1,4,1,9,9,619,1,1,2,1,4),_CllaEapProfileCaCertificationCheck_Type())
cllaEapProfileCaCertificationCheck.setMaxAccess(_F)
if mibBuilder.loadTexts:cllaEapProfileCaCertificationCheck.setStatus(_B)
class _CllaEapProfileCnCertificationIdVerify_Type(TruthValue):defaultValue=2
_CllaEapProfileCnCertificationIdVerify_Type.__name__=_E
_CllaEapProfileCnCertificationIdVerify_Object=MibTableColumn
cllaEapProfileCnCertificationIdVerify=_CllaEapProfileCnCertificationIdVerify_Object((1,3,6,1,4,1,9,9,619,1,1,2,1,5),_CllaEapProfileCnCertificationIdVerify_Type())
cllaEapProfileCnCertificationIdVerify.setMaxAccess(_F)
if mibBuilder.loadTexts:cllaEapProfileCnCertificationIdVerify.setStatus(_B)
class _CllaEapProfileDateValidityEnabled_Type(TruthValue):defaultValue=1
_CllaEapProfileDateValidityEnabled_Type.__name__=_E
_CllaEapProfileDateValidityEnabled_Object=MibTableColumn
cllaEapProfileDateValidityEnabled=_CllaEapProfileDateValidityEnabled_Object((1,3,6,1,4,1,9,9,619,1,1,2,1,6),_CllaEapProfileDateValidityEnabled_Type())
cllaEapProfileDateValidityEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:cllaEapProfileDateValidityEnabled.setStatus(_B)
class _CllaEapProfileLocalCertificateRequired_Type(TruthValue):defaultValue=2
_CllaEapProfileLocalCertificateRequired_Type.__name__=_E
_CllaEapProfileLocalCertificateRequired_Object=MibTableColumn
cllaEapProfileLocalCertificateRequired=_CllaEapProfileLocalCertificateRequired_Object((1,3,6,1,4,1,9,9,619,1,1,2,1,7),_CllaEapProfileLocalCertificateRequired_Type())
cllaEapProfileLocalCertificateRequired.setMaxAccess(_F)
if mibBuilder.loadTexts:cllaEapProfileLocalCertificateRequired.setStatus(_B)
class _CllaEapProfileClientCertificateRequired_Type(TruthValue):defaultValue=2
_CllaEapProfileClientCertificateRequired_Type.__name__=_E
_CllaEapProfileClientCertificateRequired_Object=MibTableColumn
cllaEapProfileClientCertificateRequired=_CllaEapProfileClientCertificateRequired_Object((1,3,6,1,4,1,9,9,619,1,1,2,1,8),_CllaEapProfileClientCertificateRequired_Type())
cllaEapProfileClientCertificateRequired.setMaxAccess(_F)
if mibBuilder.loadTexts:cllaEapProfileClientCertificateRequired.setStatus(_B)
_CllaEapProfileRowStatus_Type=RowStatus
_CllaEapProfileRowStatus_Object=MibTableColumn
cllaEapProfileRowStatus=_CllaEapProfileRowStatus_Object((1,3,6,1,4,1,9,9,619,1,1,2,1,9),_CllaEapProfileRowStatus_Type())
cllaEapProfileRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cllaEapProfileRowStatus.setStatus(_B)
_CllaWlanProfileTable_Object=MibTable
cllaWlanProfileTable=_CllaWlanProfileTable_Object((1,3,6,1,4,1,9,9,619,1,1,3))
if mibBuilder.loadTexts:cllaWlanProfileTable.setStatus(_B)
_CllaWlanProfileEntry_Object=MibTableRow
cllaWlanProfileEntry=_CllaWlanProfileEntry_Object((1,3,6,1,4,1,9,9,619,1,1,3,1))
cllaWlanProfileEntry.setIndexNames((0,_c,_d))
if mibBuilder.loadTexts:cllaWlanProfileEntry.setStatus(_B)
class _CllaWlanProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_CllaWlanProfileName_Type.__name__=_J
_CllaWlanProfileName_Object=MibTableColumn
cllaWlanProfileName=_CllaWlanProfileName_Object((1,3,6,1,4,1,9,9,619,1,1,3,1,1),_CllaWlanProfileName_Type())
cllaWlanProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaWlanProfileName.setStatus(_B)
_CllaWlanProfileState_Type=TruthValue
_CllaWlanProfileState_Object=MibTableColumn
cllaWlanProfileState=_CllaWlanProfileState_Object((1,3,6,1,4,1,9,9,619,1,1,3,1,2),_CllaWlanProfileState_Type())
cllaWlanProfileState.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaWlanProfileState.setStatus(_B)
_CllaUserPriorityTable_Object=MibTable
cllaUserPriorityTable=_CllaUserPriorityTable_Object((1,3,6,1,4,1,9,9,619,1,1,4))
if mibBuilder.loadTexts:cllaUserPriorityTable.setStatus(_B)
_CllaUserPriorityEntry_Object=MibTableRow
cllaUserPriorityEntry=_CllaUserPriorityEntry_Object((1,3,6,1,4,1,9,9,619,1,1,4,1))
cllaUserPriorityEntry.setIndexNames((0,_A,_g))
if mibBuilder.loadTexts:cllaUserPriorityEntry.setStatus(_B)
class _CllaUserCredential_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('ldap',2)))
_CllaUserCredential_Type.__name__=_H
_CllaUserCredential_Object=MibTableColumn
cllaUserCredential=_CllaUserCredential_Object((1,3,6,1,4,1,9,9,619,1,1,4,1,1),_CllaUserCredential_Type())
cllaUserCredential.setMaxAccess(_f)
if mibBuilder.loadTexts:cllaUserCredential.setStatus(_B)
class _CllaUserPriorityNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_CllaUserPriorityNumber_Type.__name__=_H
_CllaUserPriorityNumber_Object=MibTableColumn
cllaUserPriorityNumber=_CllaUserPriorityNumber_Object((1,3,6,1,4,1,9,9,619,1,1,4,1,2),_CllaUserPriorityNumber_Type())
cllaUserPriorityNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaUserPriorityNumber.setStatus(_B)
_CllaEapParams_ObjectIdentity=ObjectIdentity
cllaEapParams=_CllaEapParams_ObjectIdentity((1,3,6,1,4,1,9,9,619,1,1,5))
class _CllaEapMethodPacTtl_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CllaEapMethodPacTtl_Type.__name__=_D
_CllaEapMethodPacTtl_Object=MibScalar
cllaEapMethodPacTtl=_CllaEapMethodPacTtl_Object((1,3,6,1,4,1,9,9,619,1,1,5,1),_CllaEapMethodPacTtl_Type())
cllaEapMethodPacTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaEapMethodPacTtl.setStatus(_B)
if mibBuilder.loadTexts:cllaEapMethodPacTtl.setUnits('days')
class _CllaEapAnonymousProvEnabled_Type(TruthValue):defaultValue=1
_CllaEapAnonymousProvEnabled_Type.__name__=_E
_CllaEapAnonymousProvEnabled_Object=MibScalar
cllaEapAnonymousProvEnabled=_CllaEapAnonymousProvEnabled_Object((1,3,6,1,4,1,9,9,619,1,1,5,2),_CllaEapAnonymousProvEnabled_Type())
cllaEapAnonymousProvEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaEapAnonymousProvEnabled.setStatus(_B)
class _CllaEapAuthorityId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CllaEapAuthorityId_Type.__name__=_G
_CllaEapAuthorityId_Object=MibScalar
cllaEapAuthorityId=_CllaEapAuthorityId_Object((1,3,6,1,4,1,9,9,619,1,1,5,3),_CllaEapAuthorityId_Type())
cllaEapAuthorityId.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaEapAuthorityId.setStatus(_B)
class _CllaEapAuthorityInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CllaEapAuthorityInfo_Type.__name__=_G
_CllaEapAuthorityInfo_Object=MibScalar
cllaEapAuthorityInfo=_CllaEapAuthorityInfo_Object((1,3,6,1,4,1,9,9,619,1,1,5,4),_CllaEapAuthorityInfo_Type())
cllaEapAuthorityInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaEapAuthorityInfo.setStatus(_B)
class _CllaEapServerKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CllaEapServerKey_Type.__name__=_G
_CllaEapServerKey_Object=MibScalar
cllaEapServerKey=_CllaEapServerKey_Object((1,3,6,1,4,1,9,9,619,1,1,5,5),_CllaEapServerKey_Type())
cllaEapServerKey.setMaxAccess(_C)
if mibBuilder.loadTexts:cllaEapServerKey.setStatus(_B)
class _CllaEapAuthorityIdLength_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_CllaEapAuthorityIdLength_Type.__name__=_D
_CllaEapAuthorityIdLength_Object=MibScalar
cllaEapAuthorityIdLength=_CllaEapAuthorityIdLength_Object((1,3,6,1,4,1,9,9,619,1,1,5,6),_CllaEapAuthorityIdLength_Type())
cllaEapAuthorityIdLength.setMaxAccess('read-only')
if mibBuilder.loadTexts:cllaEapAuthorityIdLength.setStatus(_B)
_CiscoLwappLocalAuthMIBConform_ObjectIdentity=ObjectIdentity
ciscoLwappLocalAuthMIBConform=_CiscoLwappLocalAuthMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,619,2))
_CiscoLwappLocalAuthMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLwappLocalAuthMIBCompliances=_CiscoLwappLocalAuthMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,619,2,1))
_CiscoLwappLocalAuthMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLwappLocalAuthMIBGroups=_CiscoLwappLocalAuthMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,619,2,2))
ciscoLwappLocalAuthMIBConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,619,2,2,1))
ciscoLwappLocalAuthMIBConfigGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:ciscoLwappLocalAuthMIBConfigGroup.setStatus(_h)
ciscoLwappLocalAuthMIBConfigGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,619,2,2,2))
ciscoLwappLocalAuthMIBConfigGroupSup1.setObjects(*((_A,_K),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:ciscoLwappLocalAuthMIBConfigGroupSup1.setStatus(_B)
ciscoLwappLocalAuthMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,619,2,1,1))
ciscoLwappLocalAuthMIBCompliance.setObjects((_A,_r))
if mibBuilder.loadTexts:ciscoLwappLocalAuthMIBCompliance.setStatus(_h)
ciscoLwappLocalAuthMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,619,2,1,2))
ciscoLwappLocalAuthMIBComplianceRev1.setObjects((_A,_s))
if mibBuilder.loadTexts:ciscoLwappLocalAuthMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoLwappLocalAuthMIB':ciscoLwappLocalAuthMIB,'ciscoLwappLocalAuthMIBNotifs':ciscoLwappLocalAuthMIBNotifs,'ciscoLwappLocalAuthMIBObjects':ciscoLwappLocalAuthMIBObjects,'cllaConfig':cllaConfig,'cllaLocalAuth':cllaLocalAuth,_K:cllaActiveTimeout,_i:cllaEapIdentityReqTimeout,_j:cllaEapIdentityReqMaxRetries,_k:cllaEapDynamicWepKeyIndex,_l:cllaEapReqTimeout,_m:cllaEapReqMaxRetries,_n:cllaEapMaxLoginIgnIdResp,_o:cllaEapKeyTimeout,_p:cllaEapKeyMaxRetries,_q:cllaEapBroadcastKeyInterval,'cllaEapProfileTable':cllaEapProfileTable,'cllaEapProfileEntry':cllaEapProfileEntry,_e:cllaEapProfileName,_L:cllaEapProfileMethods,_M:cllaEapProfileCertIssuer,_N:cllaEapProfileCaCertificationCheck,_O:cllaEapProfileCnCertificationIdVerify,_P:cllaEapProfileDateValidityEnabled,_Q:cllaEapProfileLocalCertificateRequired,_R:cllaEapProfileClientCertificateRequired,_S:cllaEapProfileRowStatus,'cllaWlanProfileTable':cllaWlanProfileTable,'cllaWlanProfileEntry':cllaWlanProfileEntry,_T:cllaWlanProfileName,_U:cllaWlanProfileState,'cllaUserPriorityTable':cllaUserPriorityTable,'cllaUserPriorityEntry':cllaUserPriorityEntry,_g:cllaUserCredential,_V:cllaUserPriorityNumber,'cllaEapParams':cllaEapParams,_W:cllaEapMethodPacTtl,_X:cllaEapAnonymousProvEnabled,_Y:cllaEapAuthorityId,_Z:cllaEapAuthorityInfo,_a:cllaEapServerKey,_b:cllaEapAuthorityIdLength,'ciscoLwappLocalAuthMIBConform':ciscoLwappLocalAuthMIBConform,'ciscoLwappLocalAuthMIBCompliances':ciscoLwappLocalAuthMIBCompliances,'ciscoLwappLocalAuthMIBCompliance':ciscoLwappLocalAuthMIBCompliance,'ciscoLwappLocalAuthMIBComplianceRev1':ciscoLwappLocalAuthMIBComplianceRev1,'ciscoLwappLocalAuthMIBGroups':ciscoLwappLocalAuthMIBGroups,_r:ciscoLwappLocalAuthMIBConfigGroup,_s:ciscoLwappLocalAuthMIBConfigGroupSup1})