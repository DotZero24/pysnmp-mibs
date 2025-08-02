_r='cpkiConfigGroup'
_q='cpkiTrustPointConfigRowStatus'
_p='cpkiTrustPointStorageType'
_o='cpkiLastActionFailureReason'
_n='cpkiLastActionResult'
_m='cpkiLastAction'
_l='cpkiActionPassword'
_k='cpkiActionUrl'
_j='cpkiAction'
_i='cpkiOCSPurl'
_h='cpkiRevokeCheckMethods'
_g='cpkiIssuerCertFingerPrint'
_f='cpkiIssuerCertEndDate'
_e='cpkiIssuerCertStartDate'
_d='cpkiIssuerCertSerialNum'
_c='cpkiIssuerCertSubjectName'
_b='cpkiIssuerCertFileName'
_a='cpkiIdCertFingerPrint'
_Z='cpkiIdCertEndDate'
_Y='cpkiIdCertStartDate'
_X='cpkiIdCertSerialNum'
_W='cpkiIdCertSubjectName'
_V='cpkiIdCertFileName'
_U='cpkiKeyPairName'
_T='cpkiTrustPointId'
_S='cpkiRSAKeyPairConfigRowStatus'
_R='cpkiRSAKeyPairStorageType'
_Q='cpkiRSAKeyPairExportable'
_P='cpkiRSAPvtKeyFileName'
_O='cpkiRSAKeyPairSize'
_N='cpkiRSAKeyPairId'
_M='CiscoPkiAction'
_L='cpkiTrustPointName'
_K='not-accessible'
_J='cpkiRSAKeyPairName'
_I='TruthValue'
_H='Integer32'
_G='OctetString'
_F='StorageType'
_E='read-create'
_D='SnmpAdminString'
_C='read-only'
_B='CISCO-PKI-PARTICIPATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus',_F,'TextualConvention',_I)
cpkiMIB=ModuleIdentity((1,3,6,1,4,1,9,9,505))
if mibBuilder.loadTexts:cpkiMIB.setRevisions(('2005-10-22 00:00',))
class CiscoPkiAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('noop',1),('caauth',2),('cadelete',3),('certreq',4),('certimport',5),('certdelete',6),('pkcs12import',7),('pkcs12export',8),('certconfirm',9),('certnoconfirm',10),('forcecertdelete',11),('crlimport',12),('crldelete',13)))
class CiscoPkiActionResult(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('success',2),('failed',3),('inProgress',4),('needConfirm',5)))
_CpkiMIBNotifs_ObjectIdentity=ObjectIdentity
cpkiMIBNotifs=_CpkiMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,505,0))
_CpkiMIBObjects_ObjectIdentity=ObjectIdentity
cpkiMIBObjects=_CpkiMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,505,1))
_CpkiConfig_ObjectIdentity=ObjectIdentity
cpkiConfig=_CpkiConfig_ObjectIdentity((1,3,6,1,4,1,9,9,505,1,1))
_CpkiRSAKeyPairTable_Object=MibTable
cpkiRSAKeyPairTable=_CpkiRSAKeyPairTable_Object((1,3,6,1,4,1,9,9,505,1,1,1))
if mibBuilder.loadTexts:cpkiRSAKeyPairTable.setStatus(_A)
_CpkiRSAKeyPairEntry_Object=MibTableRow
cpkiRSAKeyPairEntry=_CpkiRSAKeyPairEntry_Object((1,3,6,1,4,1,9,9,505,1,1,1,1))
cpkiRSAKeyPairEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cpkiRSAKeyPairEntry.setStatus(_A)
class _CpkiRSAKeyPairName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CpkiRSAKeyPairName_Type.__name__=_D
_CpkiRSAKeyPairName_Object=MibTableColumn
cpkiRSAKeyPairName=_CpkiRSAKeyPairName_Object((1,3,6,1,4,1,9,9,505,1,1,1,1,1),_CpkiRSAKeyPairName_Type())
cpkiRSAKeyPairName.setMaxAccess(_K)
if mibBuilder.loadTexts:cpkiRSAKeyPairName.setStatus(_A)
_CpkiRSAKeyPairId_Type=Unsigned32
_CpkiRSAKeyPairId_Object=MibTableColumn
cpkiRSAKeyPairId=_CpkiRSAKeyPairId_Object((1,3,6,1,4,1,9,9,505,1,1,1,1,2),_CpkiRSAKeyPairId_Type())
cpkiRSAKeyPairId.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiRSAKeyPairId.setStatus(_A)
class _CpkiRSAKeyPairSize_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('rsa512',1),('rsa768',2),('rsa1024',3),('rsa1536',4),('rsa2048',5)))
_CpkiRSAKeyPairSize_Type.__name__=_H
_CpkiRSAKeyPairSize_Object=MibTableColumn
cpkiRSAKeyPairSize=_CpkiRSAKeyPairSize_Object((1,3,6,1,4,1,9,9,505,1,1,1,1,3),_CpkiRSAKeyPairSize_Type())
cpkiRSAKeyPairSize.setMaxAccess(_E)
if mibBuilder.loadTexts:cpkiRSAKeyPairSize.setStatus(_A)
class _CpkiRSAPvtKeyFileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpkiRSAPvtKeyFileName_Type.__name__=_D
_CpkiRSAPvtKeyFileName_Object=MibTableColumn
cpkiRSAPvtKeyFileName=_CpkiRSAPvtKeyFileName_Object((1,3,6,1,4,1,9,9,505,1,1,1,1,4),_CpkiRSAPvtKeyFileName_Type())
cpkiRSAPvtKeyFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiRSAPvtKeyFileName.setStatus(_A)
class _CpkiRSAKeyPairExportable_Type(TruthValue):defaultValue=1
_CpkiRSAKeyPairExportable_Type.__name__=_I
_CpkiRSAKeyPairExportable_Object=MibTableColumn
cpkiRSAKeyPairExportable=_CpkiRSAKeyPairExportable_Object((1,3,6,1,4,1,9,9,505,1,1,1,1,5),_CpkiRSAKeyPairExportable_Type())
cpkiRSAKeyPairExportable.setMaxAccess(_E)
if mibBuilder.loadTexts:cpkiRSAKeyPairExportable.setStatus(_A)
class _CpkiRSAKeyPairStorageType_Type(StorageType):defaultValue=3
_CpkiRSAKeyPairStorageType_Type.__name__=_F
_CpkiRSAKeyPairStorageType_Object=MibTableColumn
cpkiRSAKeyPairStorageType=_CpkiRSAKeyPairStorageType_Object((1,3,6,1,4,1,9,9,505,1,1,1,1,6),_CpkiRSAKeyPairStorageType_Type())
cpkiRSAKeyPairStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:cpkiRSAKeyPairStorageType.setStatus(_A)
_CpkiRSAKeyPairConfigRowStatus_Type=RowStatus
_CpkiRSAKeyPairConfigRowStatus_Object=MibTableColumn
cpkiRSAKeyPairConfigRowStatus=_CpkiRSAKeyPairConfigRowStatus_Object((1,3,6,1,4,1,9,9,505,1,1,1,1,7),_CpkiRSAKeyPairConfigRowStatus_Type())
cpkiRSAKeyPairConfigRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cpkiRSAKeyPairConfigRowStatus.setStatus(_A)
_CpkiTrustPointTable_Object=MibTable
cpkiTrustPointTable=_CpkiTrustPointTable_Object((1,3,6,1,4,1,9,9,505,1,1,2))
if mibBuilder.loadTexts:cpkiTrustPointTable.setStatus(_A)
_CpkiTrustPointEntry_Object=MibTableRow
cpkiTrustPointEntry=_CpkiTrustPointEntry_Object((1,3,6,1,4,1,9,9,505,1,1,2,1))
cpkiTrustPointEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:cpkiTrustPointEntry.setStatus(_A)
class _CpkiTrustPointName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CpkiTrustPointName_Type.__name__=_D
_CpkiTrustPointName_Object=MibTableColumn
cpkiTrustPointName=_CpkiTrustPointName_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,1),_CpkiTrustPointName_Type())
cpkiTrustPointName.setMaxAccess(_K)
if mibBuilder.loadTexts:cpkiTrustPointName.setStatus(_A)
_CpkiTrustPointId_Type=Unsigned32
_CpkiTrustPointId_Object=MibTableColumn
cpkiTrustPointId=_CpkiTrustPointId_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,2),_CpkiTrustPointId_Type())
cpkiTrustPointId.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiTrustPointId.setStatus(_A)
class _CpkiKeyPairName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpkiKeyPairName_Type.__name__=_D
_CpkiKeyPairName_Object=MibTableColumn
cpkiKeyPairName=_CpkiKeyPairName_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,3),_CpkiKeyPairName_Type())
cpkiKeyPairName.setMaxAccess(_E)
if mibBuilder.loadTexts:cpkiKeyPairName.setStatus(_A)
class _CpkiIdCertFileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpkiIdCertFileName_Type.__name__=_D
_CpkiIdCertFileName_Object=MibTableColumn
cpkiIdCertFileName=_CpkiIdCertFileName_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,4),_CpkiIdCertFileName_Type())
cpkiIdCertFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiIdCertFileName.setStatus(_A)
class _CpkiIdCertSubjectName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpkiIdCertSubjectName_Type.__name__=_D
_CpkiIdCertSubjectName_Object=MibTableColumn
cpkiIdCertSubjectName=_CpkiIdCertSubjectName_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,5),_CpkiIdCertSubjectName_Type())
cpkiIdCertSubjectName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiIdCertSubjectName.setStatus(_A)
class _CpkiIdCertSerialNum_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpkiIdCertSerialNum_Type.__name__=_D
_CpkiIdCertSerialNum_Object=MibTableColumn
cpkiIdCertSerialNum=_CpkiIdCertSerialNum_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,6),_CpkiIdCertSerialNum_Type())
cpkiIdCertSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiIdCertSerialNum.setStatus(_A)
_CpkiIdCertStartDate_Type=DateAndTime
_CpkiIdCertStartDate_Object=MibTableColumn
cpkiIdCertStartDate=_CpkiIdCertStartDate_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,7),_CpkiIdCertStartDate_Type())
cpkiIdCertStartDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiIdCertStartDate.setStatus(_A)
_CpkiIdCertEndDate_Type=DateAndTime
_CpkiIdCertEndDate_Object=MibTableColumn
cpkiIdCertEndDate=_CpkiIdCertEndDate_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,8),_CpkiIdCertEndDate_Type())
cpkiIdCertEndDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiIdCertEndDate.setStatus(_A)
class _CpkiIdCertFingerPrint_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpkiIdCertFingerPrint_Type.__name__=_D
_CpkiIdCertFingerPrint_Object=MibTableColumn
cpkiIdCertFingerPrint=_CpkiIdCertFingerPrint_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,9),_CpkiIdCertFingerPrint_Type())
cpkiIdCertFingerPrint.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiIdCertFingerPrint.setStatus(_A)
class _CpkiIssuerCertFileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpkiIssuerCertFileName_Type.__name__=_D
_CpkiIssuerCertFileName_Object=MibTableColumn
cpkiIssuerCertFileName=_CpkiIssuerCertFileName_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,10),_CpkiIssuerCertFileName_Type())
cpkiIssuerCertFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiIssuerCertFileName.setStatus(_A)
class _CpkiIssuerCertSubjectName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpkiIssuerCertSubjectName_Type.__name__=_D
_CpkiIssuerCertSubjectName_Object=MibTableColumn
cpkiIssuerCertSubjectName=_CpkiIssuerCertSubjectName_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,11),_CpkiIssuerCertSubjectName_Type())
cpkiIssuerCertSubjectName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiIssuerCertSubjectName.setStatus(_A)
class _CpkiIssuerCertSerialNum_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpkiIssuerCertSerialNum_Type.__name__=_D
_CpkiIssuerCertSerialNum_Object=MibTableColumn
cpkiIssuerCertSerialNum=_CpkiIssuerCertSerialNum_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,12),_CpkiIssuerCertSerialNum_Type())
cpkiIssuerCertSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiIssuerCertSerialNum.setStatus(_A)
_CpkiIssuerCertStartDate_Type=DateAndTime
_CpkiIssuerCertStartDate_Object=MibTableColumn
cpkiIssuerCertStartDate=_CpkiIssuerCertStartDate_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,13),_CpkiIssuerCertStartDate_Type())
cpkiIssuerCertStartDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiIssuerCertStartDate.setStatus(_A)
_CpkiIssuerCertEndDate_Type=DateAndTime
_CpkiIssuerCertEndDate_Object=MibTableColumn
cpkiIssuerCertEndDate=_CpkiIssuerCertEndDate_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,14),_CpkiIssuerCertEndDate_Type())
cpkiIssuerCertEndDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiIssuerCertEndDate.setStatus(_A)
class _CpkiIssuerCertFingerPrint_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpkiIssuerCertFingerPrint_Type.__name__=_D
_CpkiIssuerCertFingerPrint_Object=MibTableColumn
cpkiIssuerCertFingerPrint=_CpkiIssuerCertFingerPrint_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,15),_CpkiIssuerCertFingerPrint_Type())
cpkiIssuerCertFingerPrint.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiIssuerCertFingerPrint.setStatus(_A)
class _CpkiRevokeCheckMethods_Type(OctetString):defaultHexValue='02000000000000000000000000000000';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_CpkiRevokeCheckMethods_Type.__name__=_G
_CpkiRevokeCheckMethods_Object=MibTableColumn
cpkiRevokeCheckMethods=_CpkiRevokeCheckMethods_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,16),_CpkiRevokeCheckMethods_Type())
cpkiRevokeCheckMethods.setMaxAccess(_E)
if mibBuilder.loadTexts:cpkiRevokeCheckMethods.setStatus(_A)
class _CpkiOCSPurl_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpkiOCSPurl_Type.__name__=_D
_CpkiOCSPurl_Object=MibTableColumn
cpkiOCSPurl=_CpkiOCSPurl_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,17),_CpkiOCSPurl_Type())
cpkiOCSPurl.setMaxAccess(_E)
if mibBuilder.loadTexts:cpkiOCSPurl.setStatus(_A)
class _CpkiAction_Type(CiscoPkiAction):defaultValue=1
_CpkiAction_Type.__name__=_M
_CpkiAction_Object=MibTableColumn
cpkiAction=_CpkiAction_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,18),_CpkiAction_Type())
cpkiAction.setMaxAccess(_E)
if mibBuilder.loadTexts:cpkiAction.setStatus(_A)
_CpkiActionUrl_Type=SnmpAdminString
_CpkiActionUrl_Object=MibTableColumn
cpkiActionUrl=_CpkiActionUrl_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,19),_CpkiActionUrl_Type())
cpkiActionUrl.setMaxAccess(_E)
if mibBuilder.loadTexts:cpkiActionUrl.setStatus(_A)
class _CpkiActionPassword_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpkiActionPassword_Type.__name__=_D
_CpkiActionPassword_Object=MibTableColumn
cpkiActionPassword=_CpkiActionPassword_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,20),_CpkiActionPassword_Type())
cpkiActionPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:cpkiActionPassword.setStatus(_A)
_CpkiLastAction_Type=CiscoPkiAction
_CpkiLastAction_Object=MibTableColumn
cpkiLastAction=_CpkiLastAction_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,21),_CpkiLastAction_Type())
cpkiLastAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiLastAction.setStatus(_A)
_CpkiLastActionResult_Type=CiscoPkiActionResult
_CpkiLastActionResult_Object=MibTableColumn
cpkiLastActionResult=_CpkiLastActionResult_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,22),_CpkiLastActionResult_Type())
cpkiLastActionResult.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiLastActionResult.setStatus(_A)
_CpkiLastActionFailureReason_Type=SnmpAdminString
_CpkiLastActionFailureReason_Object=MibTableColumn
cpkiLastActionFailureReason=_CpkiLastActionFailureReason_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,23),_CpkiLastActionFailureReason_Type())
cpkiLastActionFailureReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cpkiLastActionFailureReason.setStatus(_A)
class _CpkiTrustPointStorageType_Type(StorageType):defaultValue=3
_CpkiTrustPointStorageType_Type.__name__=_F
_CpkiTrustPointStorageType_Object=MibTableColumn
cpkiTrustPointStorageType=_CpkiTrustPointStorageType_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,24),_CpkiTrustPointStorageType_Type())
cpkiTrustPointStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:cpkiTrustPointStorageType.setStatus(_A)
_CpkiTrustPointConfigRowStatus_Type=RowStatus
_CpkiTrustPointConfigRowStatus_Object=MibTableColumn
cpkiTrustPointConfigRowStatus=_CpkiTrustPointConfigRowStatus_Object((1,3,6,1,4,1,9,9,505,1,1,2,1,25),_CpkiTrustPointConfigRowStatus_Type())
cpkiTrustPointConfigRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cpkiTrustPointConfigRowStatus.setStatus(_A)
_CpkiMIBConform_ObjectIdentity=ObjectIdentity
cpkiMIBConform=_CpkiMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,505,2))
_CpkiMIBCompliances_ObjectIdentity=ObjectIdentity
cpkiMIBCompliances=_CpkiMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,505,2,1))
_CpkiMIBGroups_ObjectIdentity=ObjectIdentity
cpkiMIBGroups=_CpkiMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,505,2,2))
cpkiConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,505,2,2,1))
cpkiConfigGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:cpkiConfigGroup.setStatus(_A)
cpkiMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,505,2,1,1))
cpkiMIBCompliance.setObjects((_B,_r))
if mibBuilder.loadTexts:cpkiMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_M:CiscoPkiAction,'CiscoPkiActionResult':CiscoPkiActionResult,'cpkiMIB':cpkiMIB,'cpkiMIBNotifs':cpkiMIBNotifs,'cpkiMIBObjects':cpkiMIBObjects,'cpkiConfig':cpkiConfig,'cpkiRSAKeyPairTable':cpkiRSAKeyPairTable,'cpkiRSAKeyPairEntry':cpkiRSAKeyPairEntry,_J:cpkiRSAKeyPairName,_N:cpkiRSAKeyPairId,_O:cpkiRSAKeyPairSize,_P:cpkiRSAPvtKeyFileName,_Q:cpkiRSAKeyPairExportable,_R:cpkiRSAKeyPairStorageType,_S:cpkiRSAKeyPairConfigRowStatus,'cpkiTrustPointTable':cpkiTrustPointTable,'cpkiTrustPointEntry':cpkiTrustPointEntry,_L:cpkiTrustPointName,_T:cpkiTrustPointId,_U:cpkiKeyPairName,_V:cpkiIdCertFileName,_W:cpkiIdCertSubjectName,_X:cpkiIdCertSerialNum,_Y:cpkiIdCertStartDate,_Z:cpkiIdCertEndDate,_a:cpkiIdCertFingerPrint,_b:cpkiIssuerCertFileName,_c:cpkiIssuerCertSubjectName,_d:cpkiIssuerCertSerialNum,_e:cpkiIssuerCertStartDate,_f:cpkiIssuerCertEndDate,_g:cpkiIssuerCertFingerPrint,_h:cpkiRevokeCheckMethods,_i:cpkiOCSPurl,_j:cpkiAction,_k:cpkiActionUrl,_l:cpkiActionPassword,_m:cpkiLastAction,_n:cpkiLastActionResult,_o:cpkiLastActionFailureReason,_p:cpkiTrustPointStorageType,_q:cpkiTrustPointConfigRowStatus,'cpkiMIBConform':cpkiMIBConform,'cpkiMIBCompliances':cpkiMIBCompliances,'cpkiMIBCompliance':cpkiMIBCompliance,'cpkiMIBGroups':cpkiMIBGroups,_r:cpkiConfigGroup})