_A2='ciscoPkiMIBNotificationGroup'
_A1='ciscoPkiMIBMainObjectGroup'
_A0='ciscoPkiCertExpiryAlert'
_z='ciscoPkiCertInstallAlert'
_y='reenrolSourceInter'
_x='reenrolVrf'
_w='reenrolLocation'
_v='reenrolMethod'
_u='enrolSourceInter'
_t='enrolVrf'
_s='enrolLocation'
_r='authSourceInter'
_q='authVrf'
_p='authMethod'
_o='authLocation'
_n='enrolCredentials'
_m='hashAlgo'
_l='nexUpdate'
_k='thisUpdate'
_j='responderID'
_i='deltaCRLFlag'
_h='crlSize'
_g='nextUpdate'
_f='sequenceNumb'
_e='issuerName'
_d='keyPairLabel'
_c='autoEnroll'
_b='sourceInter'
_a='vrfConfig'
_Z='aaaListInfo'
_Y='subjectAltName'
_X='subjectName'
_W='enrollmentConfig'
_V='revocationMethod'
_U='trustpointState'
_T='enrolMethod'
_S='ocspTpLabel'
_R='crlTpLabel'
_Q='certChainLabel'
_P='tpLabel'
_O='enrollProfLabel'
_N='certEndDate'
_M='certStartDate'
_L='certRemainingLife'
_K='Unsigned32'
_J='certSubName'
_I='certTpLabel'
_H='certType'
_G='certIssuerName'
_F='certSerialNum'
_E='not-accessible'
_D='DisplayString'
_C='read-only'
_B='current'
_A='CISCO-PKI-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TimeInterval')
ciscoPkiMIB=ModuleIdentity((1,3,6,1,4,1,9,9,854))
if mibBuilder.loadTexts:ciscoPkiMIB.setRevisions(('2014-10-15 00:00',))
_CiscoPkiMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoPkiMIBNotifs=_CiscoPkiMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,854,1))
_CiscoPkiMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPkiMIBObjects=_CiscoPkiMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,854,2))
_CiscoPkiConfiguration_ObjectIdentity=ObjectIdentity
ciscoPkiConfiguration=_CiscoPkiConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,854,2,1))
_CiscoPkiEnrollmentProfile_ObjectIdentity=ObjectIdentity
ciscoPkiEnrollmentProfile=_CiscoPkiEnrollmentProfile_ObjectIdentity((1,3,6,1,4,1,9,9,854,2,1,1))
_CiscoPkiEnrollmentTable_Object=MibTable
ciscoPkiEnrollmentTable=_CiscoPkiEnrollmentTable_Object((1,3,6,1,4,1,9,9,854,2,1,1,1))
if mibBuilder.loadTexts:ciscoPkiEnrollmentTable.setStatus(_B)
_EnrollProfEntry_Object=MibTableRow
enrollProfEntry=_EnrollProfEntry_Object((1,3,6,1,4,1,9,9,854,2,1,1,1,1))
enrollProfEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:enrollProfEntry.setStatus(_B)
class _EnrollProfLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EnrollProfLabel_Type.__name__=_D
_EnrollProfLabel_Object=MibTableColumn
enrollProfLabel=_EnrollProfLabel_Object((1,3,6,1,4,1,9,9,854,2,1,1,1,1,3),_EnrollProfLabel_Type())
enrollProfLabel.setMaxAccess(_E)
if mibBuilder.loadTexts:enrollProfLabel.setStatus(_B)
_EnrolCredentials_Type=DisplayString
_EnrolCredentials_Object=MibTableColumn
enrolCredentials=_EnrolCredentials_Object((1,3,6,1,4,1,9,9,854,2,1,1,1,1,4),_EnrolCredentials_Type())
enrolCredentials.setMaxAccess(_C)
if mibBuilder.loadTexts:enrolCredentials.setStatus(_B)
_AuthLocation_Type=DisplayString
_AuthLocation_Object=MibTableColumn
authLocation=_AuthLocation_Object((1,3,6,1,4,1,9,9,854,2,1,1,1,1,5),_AuthLocation_Type())
authLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:authLocation.setStatus(_B)
_AuthMethod_Type=DisplayString
_AuthMethod_Object=MibTableColumn
authMethod=_AuthMethod_Object((1,3,6,1,4,1,9,9,854,2,1,1,1,1,6),_AuthMethod_Type())
authMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:authMethod.setStatus(_B)
_AuthVrf_Type=DisplayString
_AuthVrf_Object=MibTableColumn
authVrf=_AuthVrf_Object((1,3,6,1,4,1,9,9,854,2,1,1,1,1,7),_AuthVrf_Type())
authVrf.setMaxAccess(_C)
if mibBuilder.loadTexts:authVrf.setStatus(_B)
_AuthSourceInter_Type=DisplayString
_AuthSourceInter_Object=MibTableColumn
authSourceInter=_AuthSourceInter_Object((1,3,6,1,4,1,9,9,854,2,1,1,1,1,8),_AuthSourceInter_Type())
authSourceInter.setMaxAccess(_C)
if mibBuilder.loadTexts:authSourceInter.setStatus(_B)
class _EnrolMethod_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EnrolMethod_Type.__name__=_D
_EnrolMethod_Object=MibTableColumn
enrolMethod=_EnrolMethod_Object((1,3,6,1,4,1,9,9,854,2,1,1,1,1,9),_EnrolMethod_Type())
enrolMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:enrolMethod.setStatus(_B)
_EnrolLocation_Type=DisplayString
_EnrolLocation_Object=MibTableColumn
enrolLocation=_EnrolLocation_Object((1,3,6,1,4,1,9,9,854,2,1,1,1,1,10),_EnrolLocation_Type())
enrolLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:enrolLocation.setStatus(_B)
_EnrolVrf_Type=DisplayString
_EnrolVrf_Object=MibTableColumn
enrolVrf=_EnrolVrf_Object((1,3,6,1,4,1,9,9,854,2,1,1,1,1,11),_EnrolVrf_Type())
enrolVrf.setMaxAccess(_C)
if mibBuilder.loadTexts:enrolVrf.setStatus(_B)
_EnrolSourceInter_Type=DisplayString
_EnrolSourceInter_Object=MibTableColumn
enrolSourceInter=_EnrolSourceInter_Object((1,3,6,1,4,1,9,9,854,2,1,1,1,1,12),_EnrolSourceInter_Type())
enrolSourceInter.setMaxAccess(_C)
if mibBuilder.loadTexts:enrolSourceInter.setStatus(_B)
_ReenrolMethod_Type=DisplayString
_ReenrolMethod_Object=MibTableColumn
reenrolMethod=_ReenrolMethod_Object((1,3,6,1,4,1,9,9,854,2,1,1,1,1,13),_ReenrolMethod_Type())
reenrolMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:reenrolMethod.setStatus(_B)
_ReenrolLocation_Type=DisplayString
_ReenrolLocation_Object=MibTableColumn
reenrolLocation=_ReenrolLocation_Object((1,3,6,1,4,1,9,9,854,2,1,1,1,1,14),_ReenrolLocation_Type())
reenrolLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:reenrolLocation.setStatus(_B)
_ReenrolVrf_Type=DisplayString
_ReenrolVrf_Object=MibTableColumn
reenrolVrf=_ReenrolVrf_Object((1,3,6,1,4,1,9,9,854,2,1,1,1,1,15),_ReenrolVrf_Type())
reenrolVrf.setMaxAccess(_C)
if mibBuilder.loadTexts:reenrolVrf.setStatus(_B)
_ReenrolSourceInter_Type=DisplayString
_ReenrolSourceInter_Object=MibTableColumn
reenrolSourceInter=_ReenrolSourceInter_Object((1,3,6,1,4,1,9,9,854,2,1,1,1,1,16),_ReenrolSourceInter_Type())
reenrolSourceInter.setMaxAccess(_C)
if mibBuilder.loadTexts:reenrolSourceInter.setStatus(_B)
_CiscoPkiTrustpoints_ObjectIdentity=ObjectIdentity
ciscoPkiTrustpoints=_CiscoPkiTrustpoints_ObjectIdentity((1,3,6,1,4,1,9,9,854,2,1,2))
_PkiTPTable_Object=MibTable
pkiTPTable=_PkiTPTable_Object((1,3,6,1,4,1,9,9,854,2,1,2,1))
if mibBuilder.loadTexts:pkiTPTable.setStatus(_B)
_PkiTPEntry_Object=MibTableRow
pkiTPEntry=_PkiTPEntry_Object((1,3,6,1,4,1,9,9,854,2,1,2,1,1))
pkiTPEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:pkiTPEntry.setStatus(_B)
class _TpLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpLabel_Type.__name__=_D
_TpLabel_Object=MibTableColumn
tpLabel=_TpLabel_Object((1,3,6,1,4,1,9,9,854,2,1,2,1,1,1),_TpLabel_Type())
tpLabel.setMaxAccess(_E)
if mibBuilder.loadTexts:tpLabel.setStatus(_B)
class _SubjectName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SubjectName_Type.__name__=_D
_SubjectName_Object=MibTableColumn
subjectName=_SubjectName_Object((1,3,6,1,4,1,9,9,854,2,1,2,1,1,2),_SubjectName_Type())
subjectName.setMaxAccess(_C)
if mibBuilder.loadTexts:subjectName.setStatus(_B)
class _SubjectAltName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SubjectAltName_Type.__name__=_D
_SubjectAltName_Object=MibTableColumn
subjectAltName=_SubjectAltName_Object((1,3,6,1,4,1,9,9,854,2,1,2,1,1,3),_SubjectAltName_Type())
subjectAltName.setMaxAccess(_C)
if mibBuilder.loadTexts:subjectAltName.setStatus(_B)
class _AaaListInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_AaaListInfo_Type.__name__=_D
_AaaListInfo_Object=MibTableColumn
aaaListInfo=_AaaListInfo_Object((1,3,6,1,4,1,9,9,854,2,1,2,1,1,4),_AaaListInfo_Type())
aaaListInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:aaaListInfo.setStatus(_B)
class _EnrollmentConfig_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EnrollmentConfig_Type.__name__=_D
_EnrollmentConfig_Object=MibTableColumn
enrollmentConfig=_EnrollmentConfig_Object((1,3,6,1,4,1,9,9,854,2,1,2,1,1,5),_EnrollmentConfig_Type())
enrollmentConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:enrollmentConfig.setStatus(_B)
class _VrfConfig_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_VrfConfig_Type.__name__=_D
_VrfConfig_Object=MibTableColumn
vrfConfig=_VrfConfig_Object((1,3,6,1,4,1,9,9,854,2,1,2,1,1,6),_VrfConfig_Type())
vrfConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:vrfConfig.setStatus(_B)
class _SourceInter_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SourceInter_Type.__name__=_D
_SourceInter_Object=MibTableColumn
sourceInter=_SourceInter_Object((1,3,6,1,4,1,9,9,854,2,1,2,1,1,7),_SourceInter_Type())
sourceInter.setMaxAccess(_C)
if mibBuilder.loadTexts:sourceInter.setStatus(_B)
class _AutoEnroll_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AutoEnroll_Type.__name__=_D
_AutoEnroll_Object=MibTableColumn
autoEnroll=_AutoEnroll_Object((1,3,6,1,4,1,9,9,854,2,1,2,1,1,8),_AutoEnroll_Type())
autoEnroll.setMaxAccess(_C)
if mibBuilder.loadTexts:autoEnroll.setStatus(_B)
class _KeyPairLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_KeyPairLabel_Type.__name__=_D
_KeyPairLabel_Object=MibTableColumn
keyPairLabel=_KeyPairLabel_Object((1,3,6,1,4,1,9,9,854,2,1,2,1,1,10),_KeyPairLabel_Type())
keyPairLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:keyPairLabel.setStatus(_B)
class _RevocationMethod_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_RevocationMethod_Type.__name__=_D
_RevocationMethod_Object=MibTableColumn
revocationMethod=_RevocationMethod_Object((1,3,6,1,4,1,9,9,854,2,1,2,1,1,11),_RevocationMethod_Type())
revocationMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:revocationMethod.setStatus(_B)
_HashAlgo_Type=DisplayString
_HashAlgo_Object=MibTableColumn
hashAlgo=_HashAlgo_Object((1,3,6,1,4,1,9,9,854,2,1,2,1,1,12),_HashAlgo_Type())
hashAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:hashAlgo.setStatus(_B)
class _TrustpointState_Type(DisplayString):defaultValue=OctetString('0');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_TrustpointState_Type.__name__=_D
_TrustpointState_Object=MibTableColumn
trustpointState=_TrustpointState_Object((1,3,6,1,4,1,9,9,854,2,1,2,1,1,13),_TrustpointState_Type())
trustpointState.setMaxAccess(_C)
if mibBuilder.loadTexts:trustpointState.setStatus(_B)
_CiscoPkiCertificates_ObjectIdentity=ObjectIdentity
ciscoPkiCertificates=_CiscoPkiCertificates_ObjectIdentity((1,3,6,1,4,1,9,9,854,2,2))
_CertChainTable_Object=MibTable
certChainTable=_CertChainTable_Object((1,3,6,1,4,1,9,9,854,2,2,1))
if mibBuilder.loadTexts:certChainTable.setStatus(_B)
_CertChainEntry_Object=MibTableRow
certChainEntry=_CertChainEntry_Object((1,3,6,1,4,1,9,9,854,2,2,1,1))
certChainEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:certChainEntry.setStatus(_B)
_CertChainLabel_Type=DisplayString
_CertChainLabel_Object=MibTableColumn
certChainLabel=_CertChainLabel_Object((1,3,6,1,4,1,9,9,854,2,2,1,1,1),_CertChainLabel_Type())
certChainLabel.setMaxAccess(_E)
if mibBuilder.loadTexts:certChainLabel.setStatus(_B)
_CertSerialNum_Type=DisplayString
_CertSerialNum_Object=MibTableColumn
certSerialNum=_CertSerialNum_Object((1,3,6,1,4,1,9,9,854,2,2,1,1,2),_CertSerialNum_Type())
certSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:certSerialNum.setStatus(_B)
_CertIssuerName_Type=DisplayString
_CertIssuerName_Object=MibTableColumn
certIssuerName=_CertIssuerName_Object((1,3,6,1,4,1,9,9,854,2,2,1,1,3),_CertIssuerName_Type())
certIssuerName.setMaxAccess(_C)
if mibBuilder.loadTexts:certIssuerName.setStatus(_B)
_CertStartDate_Type=DisplayString
_CertStartDate_Object=MibTableColumn
certStartDate=_CertStartDate_Object((1,3,6,1,4,1,9,9,854,2,2,1,1,4),_CertStartDate_Type())
certStartDate.setMaxAccess(_C)
if mibBuilder.loadTexts:certStartDate.setStatus(_B)
_CertEndDate_Type=DisplayString
_CertEndDate_Object=MibTableColumn
certEndDate=_CertEndDate_Object((1,3,6,1,4,1,9,9,854,2,2,1,1,5),_CertEndDate_Type())
certEndDate.setMaxAccess(_C)
if mibBuilder.loadTexts:certEndDate.setStatus(_B)
_CertType_Type=DisplayString
_CertType_Object=MibTableColumn
certType=_CertType_Object((1,3,6,1,4,1,9,9,854,2,2,1,1,6),_CertType_Type())
certType.setMaxAccess(_C)
if mibBuilder.loadTexts:certType.setStatus(_B)
_CertRemainingLife_Type=DisplayString
_CertRemainingLife_Object=MibTableColumn
certRemainingLife=_CertRemainingLife_Object((1,3,6,1,4,1,9,9,854,2,2,1,1,7),_CertRemainingLife_Type())
certRemainingLife.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:certRemainingLife.setStatus(_B)
_CertTpLabel_Type=DisplayString
_CertTpLabel_Object=MibTableColumn
certTpLabel=_CertTpLabel_Object((1,3,6,1,4,1,9,9,854,2,2,1,1,8),_CertTpLabel_Type())
certTpLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:certTpLabel.setStatus(_B)
_CertSubName_Type=DisplayString
_CertSubName_Object=MibTableColumn
certSubName=_CertSubName_Object((1,3,6,1,4,1,9,9,854,2,2,1,1,9),_CertSubName_Type())
certSubName.setMaxAccess(_C)
if mibBuilder.loadTexts:certSubName.setStatus(_B)
_CiscoPkiRevocationInfo_ObjectIdentity=ObjectIdentity
ciscoPkiRevocationInfo=_CiscoPkiRevocationInfo_ObjectIdentity((1,3,6,1,4,1,9,9,854,2,3))
_CiscoPkiCRLInfo_ObjectIdentity=ObjectIdentity
ciscoPkiCRLInfo=_CiscoPkiCRLInfo_ObjectIdentity((1,3,6,1,4,1,9,9,854,2,3,1))
_PkiCRLTable_Object=MibTable
pkiCRLTable=_PkiCRLTable_Object((1,3,6,1,4,1,9,9,854,2,3,1,1))
if mibBuilder.loadTexts:pkiCRLTable.setStatus(_B)
_PkiCRLEntry_Object=MibTableRow
pkiCRLEntry=_PkiCRLEntry_Object((1,3,6,1,4,1,9,9,854,2,3,1,1,1))
pkiCRLEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:pkiCRLEntry.setStatus(_B)
_CrlTpLabel_Type=DisplayString
_CrlTpLabel_Object=MibTableColumn
crlTpLabel=_CrlTpLabel_Object((1,3,6,1,4,1,9,9,854,2,3,1,1,1,1),_CrlTpLabel_Type())
crlTpLabel.setMaxAccess(_E)
if mibBuilder.loadTexts:crlTpLabel.setStatus(_B)
class _IssuerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IssuerName_Type.__name__=_D
_IssuerName_Object=MibTableColumn
issuerName=_IssuerName_Object((1,3,6,1,4,1,9,9,854,2,3,1,1,1,2),_IssuerName_Type())
issuerName.setMaxAccess(_C)
if mibBuilder.loadTexts:issuerName.setStatus(_B)
class _SequenceNumb_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SequenceNumb_Type.__name__=_D
_SequenceNumb_Object=MibTableColumn
sequenceNumb=_SequenceNumb_Object((1,3,6,1,4,1,9,9,854,2,3,1,1,1,3),_SequenceNumb_Type())
sequenceNumb.setMaxAccess(_C)
if mibBuilder.loadTexts:sequenceNumb.setStatus(_B)
class _NextUpdate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NextUpdate_Type.__name__=_D
_NextUpdate_Object=MibTableColumn
nextUpdate=_NextUpdate_Object((1,3,6,1,4,1,9,9,854,2,3,1,1,1,4),_NextUpdate_Type())
nextUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:nextUpdate.setStatus(_B)
class _CrlSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_CrlSize_Type.__name__=_K
_CrlSize_Object=MibTableColumn
crlSize=_CrlSize_Object((1,3,6,1,4,1,9,9,854,2,3,1,1,1,5),_CrlSize_Type())
crlSize.setMaxAccess(_C)
if mibBuilder.loadTexts:crlSize.setStatus(_B)
class _DeltaCRLFlag_Type(Unsigned32):defaultValue=0
_DeltaCRLFlag_Type.__name__=_K
_DeltaCRLFlag_Object=MibTableColumn
deltaCRLFlag=_DeltaCRLFlag_Object((1,3,6,1,4,1,9,9,854,2,3,1,1,1,6),_DeltaCRLFlag_Type())
deltaCRLFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:deltaCRLFlag.setStatus(_B)
_CiscoPkiOSCPInfo_ObjectIdentity=ObjectIdentity
ciscoPkiOSCPInfo=_CiscoPkiOSCPInfo_ObjectIdentity((1,3,6,1,4,1,9,9,854,2,3,2))
_PkiOCSPTable_Object=MibTable
pkiOCSPTable=_PkiOCSPTable_Object((1,3,6,1,4,1,9,9,854,2,3,2,1))
if mibBuilder.loadTexts:pkiOCSPTable.setStatus(_B)
_PkiOCSPEntry_Object=MibTableRow
pkiOCSPEntry=_PkiOCSPEntry_Object((1,3,6,1,4,1,9,9,854,2,3,2,1,1))
pkiOCSPEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:pkiOCSPEntry.setStatus(_B)
class _OcspTpLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OcspTpLabel_Type.__name__=_D
_OcspTpLabel_Object=MibTableColumn
ocspTpLabel=_OcspTpLabel_Object((1,3,6,1,4,1,9,9,854,2,3,2,1,1,1),_OcspTpLabel_Type())
ocspTpLabel.setMaxAccess(_E)
if mibBuilder.loadTexts:ocspTpLabel.setStatus(_B)
class _ResponderID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ResponderID_Type.__name__=_D
_ResponderID_Object=MibTableColumn
responderID=_ResponderID_Object((1,3,6,1,4,1,9,9,854,2,3,2,1,1,2),_ResponderID_Type())
responderID.setMaxAccess(_C)
if mibBuilder.loadTexts:responderID.setStatus(_B)
class _ThisUpdate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ThisUpdate_Type.__name__=_D
_ThisUpdate_Object=MibTableColumn
thisUpdate=_ThisUpdate_Object((1,3,6,1,4,1,9,9,854,2,3,2,1,1,3),_ThisUpdate_Type())
thisUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:thisUpdate.setStatus(_B)
class _NexUpdate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NexUpdate_Type.__name__=_D
_NexUpdate_Object=MibTableColumn
nexUpdate=_NexUpdate_Object((1,3,6,1,4,1,9,9,854,2,3,2,1,1,4),_NexUpdate_Type())
nexUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:nexUpdate.setStatus(_B)
_CiscoPkiMIBConform_ObjectIdentity=ObjectIdentity
ciscoPkiMIBConform=_CiscoPkiMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,854,3))
_CiscoPkiMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoPkiMIBCompliances=_CiscoPkiMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,854,3,1))
_CiscoPkiMIBGroups_ObjectIdentity=ObjectIdentity
ciscoPkiMIBGroups=_CiscoPkiMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,854,3,2))
ciscoPkiMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,854,3,2,1))
ciscoPkiMIBMainObjectGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_L),(_A,_F),(_A,_G),(_A,_M),(_A,_N),(_A,_H),(_A,_I),(_A,_J),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:ciscoPkiMIBMainObjectGroup.setStatus(_B)
ciscoPkiCertInstallAlert=NotificationType((1,3,6,1,4,1,9,9,854,1,1))
ciscoPkiCertInstallAlert.setObjects(*((_A,_F),(_A,_G),(_A,_M),(_A,_N),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ciscoPkiCertInstallAlert.setStatus(_B)
ciscoPkiCertExpiryAlert=NotificationType((1,3,6,1,4,1,9,9,854,1,2))
ciscoPkiCertExpiryAlert.setObjects(*((_A,_F),(_A,_J),(_A,_G),(_A,_H),(_A,_I),(_A,_L)))
if mibBuilder.loadTexts:ciscoPkiCertExpiryAlert.setStatus(_B)
ciscoPkiMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,854,3,2,2))
ciscoPkiMIBNotificationGroup.setObjects(*((_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:ciscoPkiMIBNotificationGroup.setStatus(_B)
ciscoPkiMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,854,3,1,1))
ciscoPkiMIBCompliance.setObjects(*((_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:ciscoPkiMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoPkiMIB':ciscoPkiMIB,'ciscoPkiMIBNotifs':ciscoPkiMIBNotifs,_z:ciscoPkiCertInstallAlert,_A0:ciscoPkiCertExpiryAlert,'ciscoPkiMIBObjects':ciscoPkiMIBObjects,'ciscoPkiConfiguration':ciscoPkiConfiguration,'ciscoPkiEnrollmentProfile':ciscoPkiEnrollmentProfile,'ciscoPkiEnrollmentTable':ciscoPkiEnrollmentTable,'enrollProfEntry':enrollProfEntry,_O:enrollProfLabel,_n:enrolCredentials,_o:authLocation,_p:authMethod,_q:authVrf,_r:authSourceInter,_T:enrolMethod,_s:enrolLocation,_t:enrolVrf,_u:enrolSourceInter,_v:reenrolMethod,_w:reenrolLocation,_x:reenrolVrf,_y:reenrolSourceInter,'ciscoPkiTrustpoints':ciscoPkiTrustpoints,'pkiTPTable':pkiTPTable,'pkiTPEntry':pkiTPEntry,_P:tpLabel,_X:subjectName,_Y:subjectAltName,_Z:aaaListInfo,_W:enrollmentConfig,_a:vrfConfig,_b:sourceInter,_c:autoEnroll,_d:keyPairLabel,_V:revocationMethod,_m:hashAlgo,_U:trustpointState,'ciscoPkiCertificates':ciscoPkiCertificates,'certChainTable':certChainTable,'certChainEntry':certChainEntry,_Q:certChainLabel,_F:certSerialNum,_G:certIssuerName,_M:certStartDate,_N:certEndDate,_H:certType,_L:certRemainingLife,_I:certTpLabel,_J:certSubName,'ciscoPkiRevocationInfo':ciscoPkiRevocationInfo,'ciscoPkiCRLInfo':ciscoPkiCRLInfo,'pkiCRLTable':pkiCRLTable,'pkiCRLEntry':pkiCRLEntry,_R:crlTpLabel,_e:issuerName,_f:sequenceNumb,_g:nextUpdate,_h:crlSize,_i:deltaCRLFlag,'ciscoPkiOSCPInfo':ciscoPkiOSCPInfo,'pkiOCSPTable':pkiOCSPTable,'pkiOCSPEntry':pkiOCSPEntry,_S:ocspTpLabel,_j:responderID,_k:thisUpdate,_l:nexUpdate,'ciscoPkiMIBConform':ciscoPkiMIBConform,'ciscoPkiMIBCompliances':ciscoPkiMIBCompliances,'ciscoPkiMIBCompliance':ciscoPkiMIBCompliance,'ciscoPkiMIBGroups':ciscoPkiMIBGroups,_A1:ciscoPkiMIBMainObjectGroup,_A2:ciscoPkiMIBNotificationGroup})