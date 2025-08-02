_H='Seconds'
_G='oacGdoiGmKekSPI'
_F='oacGdoiGmActiveKEK'
_E='Bits'
_D='oacGdoiGroupName'
_C='ONEACCESS-GDOI-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oacExpIMManagement,=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMManagement')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_E,'Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
oacExpIMGdoiMIB=ModuleIdentity((1,3,6,1,4,1,13191,10,3,4,1224))
class OacGdoiIdentificationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('keyID',1),('ipv4',2)))
class OacGdoiIdentificationValue(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
class OacGdoiSPI(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
class OacGdoiKEKEncryptionAlgorithm(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enc-des',1),('enc-3des',2),('enc-aes',3)))
class OacGdoiHashAlogrithm(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('md5',1),('sha1',2)))
class OacGdoiSignatureMethod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rsa',1),('dss',2),('ecdss',3)))
_OacGdoiMIBObjects_ObjectIdentity=ObjectIdentity
oacGdoiMIBObjects=_OacGdoiMIBObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,1224,1))
_OacGdoiGroupTable_Object=MibTable
oacGdoiGroupTable=_OacGdoiGroupTable_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,1))
if mibBuilder.loadTexts:oacGdoiGroupTable.setStatus(_A)
_OacGdoiGroupEntry_Object=MibTableRow
oacGdoiGroupEntry=_OacGdoiGroupEntry_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,1,1))
oacGdoiGroupEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:oacGdoiGroupEntry.setStatus(_A)
_OacGdoiGroupName_Type=DisplayString
_OacGdoiGroupName_Object=MibTableColumn
oacGdoiGroupName=_OacGdoiGroupName_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,1,1,1),_OacGdoiGroupName_Type())
oacGdoiGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGroupName.setStatus(_A)
_OacGdoiGroupIdType_Type=OacGdoiIdentificationType
_OacGdoiGroupIdType_Object=MibTableColumn
oacGdoiGroupIdType=_OacGdoiGroupIdType_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,1,1,2),_OacGdoiGroupIdType_Type())
oacGdoiGroupIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGroupIdType.setStatus(_A)
_OacGdoiGroupIdValue_Type=OacGdoiIdentificationValue
_OacGdoiGroupIdValue_Object=MibTableColumn
oacGdoiGroupIdValue=_OacGdoiGroupIdValue_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,1,1,3),_OacGdoiGroupIdValue_Type())
oacGdoiGroupIdValue.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGroupIdValue.setStatus(_A)
_OacGdoiGm_ObjectIdentity=ObjectIdentity
oacGdoiGm=_OacGdoiGm_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,1224,1,2))
_OacGdoiGmTable_Object=MibTable
oacGdoiGmTable=_OacGdoiGmTable_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,2,2))
if mibBuilder.loadTexts:oacGdoiGmTable.setStatus(_A)
_OacGdoiGmEntry_Object=MibTableRow
oacGdoiGmEntry=_OacGdoiGmEntry_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,2,2,1))
oacGdoiGmEntry.setIndexNames((0,_C,_D),(0,_C,_F))
if mibBuilder.loadTexts:oacGdoiGmEntry.setStatus(_A)
_OacGdoiGmIdType_Type=OacGdoiIdentificationType
_OacGdoiGmIdType_Object=MibTableColumn
oacGdoiGmIdType=_OacGdoiGmIdType_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,2,2,1,1),_OacGdoiGmIdType_Type())
oacGdoiGmIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGmIdType.setStatus(_A)
_OacGdoiGmIdValue_Type=OacGdoiIdentificationValue
_OacGdoiGmIdValue_Object=MibTableColumn
oacGdoiGmIdValue=_OacGdoiGmIdValue_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,2,2,1,2),_OacGdoiGmIdValue_Type())
oacGdoiGmIdValue.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGmIdValue.setStatus(_A)
_OacGdoiGmRegKeyServerIdValue_Type=OacGdoiIdentificationValue
_OacGdoiGmRegKeyServerIdValue_Object=MibTableColumn
oacGdoiGmRegKeyServerIdValue=_OacGdoiGmRegKeyServerIdValue_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,2,2,1,3),_OacGdoiGmRegKeyServerIdValue_Type())
oacGdoiGmRegKeyServerIdValue.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGmRegKeyServerIdValue.setStatus(_A)
_OacGdoiGmActiveKEK_Type=OacGdoiSPI
_OacGdoiGmActiveKEK_Object=MibTableColumn
oacGdoiGmActiveKEK=_OacGdoiGmActiveKEK_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,2,2,1,4),_OacGdoiGmActiveKEK_Type())
oacGdoiGmActiveKEK.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGmActiveKEK.setStatus(_A)
_OacGdoiGmRekeysReceived_Type=Counter32
_OacGdoiGmRekeysReceived_Object=MibTableColumn
oacGdoiGmRekeysReceived=_OacGdoiGmRekeysReceived_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,2,2,1,5),_OacGdoiGmRekeysReceived_Type())
oacGdoiGmRekeysReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGmRekeysReceived.setStatus(_A)
if mibBuilder.loadTexts:oacGdoiGmRekeysReceived.setUnits('GROUPKEY-PUSH Messages')
_OacGdoiPolicy_ObjectIdentity=ObjectIdentity
oacGdoiPolicy=_OacGdoiPolicy_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,1224,1,3))
_OacGdoiGmKekTable_Object=MibTable
oacGdoiGmKekTable=_OacGdoiGmKekTable_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,3,2))
if mibBuilder.loadTexts:oacGdoiGmKekTable.setStatus(_A)
_OacGdoiGmKekEntry_Object=MibTableRow
oacGdoiGmKekEntry=_OacGdoiGmKekEntry_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,3,2,1))
oacGdoiGmKekEntry.setIndexNames((0,_C,_D),(0,_C,_G))
if mibBuilder.loadTexts:oacGdoiGmKekEntry.setStatus(_A)
_OacGdoiGmKekSPI_Type=OacGdoiSPI
_OacGdoiGmKekSPI_Object=MibTableColumn
oacGdoiGmKekSPI=_OacGdoiGmKekSPI_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,3,2,1,1),_OacGdoiGmKekSPI_Type())
oacGdoiGmKekSPI.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGmKekSPI.setStatus(_A)
_OacGdoiGmKekSrcIdValue_Type=OacGdoiIdentificationValue
_OacGdoiGmKekSrcIdValue_Object=MibTableColumn
oacGdoiGmKekSrcIdValue=_OacGdoiGmKekSrcIdValue_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,3,2,1,2),_OacGdoiGmKekSrcIdValue_Type())
oacGdoiGmKekSrcIdValue.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGmKekSrcIdValue.setStatus(_A)
_OacGdoiGmKekDstIdValue_Type=OacGdoiIdentificationValue
_OacGdoiGmKekDstIdValue_Object=MibTableColumn
oacGdoiGmKekDstIdValue=_OacGdoiGmKekDstIdValue_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,3,2,1,3),_OacGdoiGmKekDstIdValue_Type())
oacGdoiGmKekDstIdValue.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGmKekDstIdValue.setStatus(_A)
_OacGdoiGmKekEncryptAlg_Type=OacGdoiKEKEncryptionAlgorithm
_OacGdoiGmKekEncryptAlg_Object=MibTableColumn
oacGdoiGmKekEncryptAlg=_OacGdoiGmKekEncryptAlg_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,3,2,1,4),_OacGdoiGmKekEncryptAlg_Type())
oacGdoiGmKekEncryptAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGmKekEncryptAlg.setStatus(_A)
_OacGdoiGmKekEncryptKeyLength_Type=Unsigned32
_OacGdoiGmKekEncryptKeyLength_Object=MibTableColumn
oacGdoiGmKekEncryptKeyLength=_OacGdoiGmKekEncryptKeyLength_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,3,2,1,5),_OacGdoiGmKekEncryptKeyLength_Type())
oacGdoiGmKekEncryptKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGmKekEncryptKeyLength.setStatus(_A)
if mibBuilder.loadTexts:oacGdoiGmKekEncryptKeyLength.setUnits(_E)
_OacGdoiGmKekSigHashAlg_Type=OacGdoiHashAlogrithm
_OacGdoiGmKekSigHashAlg_Object=MibTableColumn
oacGdoiGmKekSigHashAlg=_OacGdoiGmKekSigHashAlg_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,3,2,1,6),_OacGdoiGmKekSigHashAlg_Type())
oacGdoiGmKekSigHashAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGmKekSigHashAlg.setStatus(_A)
_OacGdoiGmKekSigAlg_Type=OacGdoiSignatureMethod
_OacGdoiGmKekSigAlg_Object=MibTableColumn
oacGdoiGmKekSigAlg=_OacGdoiGmKekSigAlg_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,3,2,1,7),_OacGdoiGmKekSigAlg_Type())
oacGdoiGmKekSigAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGmKekSigAlg.setStatus(_A)
_OacGdoiGmKekSigKeyLength_Type=Unsigned32
_OacGdoiGmKekSigKeyLength_Object=MibTableColumn
oacGdoiGmKekSigKeyLength=_OacGdoiGmKekSigKeyLength_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,3,2,1,8),_OacGdoiGmKekSigKeyLength_Type())
oacGdoiGmKekSigKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGmKekSigKeyLength.setStatus(_A)
if mibBuilder.loadTexts:oacGdoiGmKekSigKeyLength.setUnits(_E)
_OacGdoiGmKekOriginalLifetime_Type=Unsigned32
_OacGdoiGmKekOriginalLifetime_Object=MibTableColumn
oacGdoiGmKekOriginalLifetime=_OacGdoiGmKekOriginalLifetime_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,3,2,1,9),_OacGdoiGmKekOriginalLifetime_Type())
oacGdoiGmKekOriginalLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGmKekOriginalLifetime.setStatus(_A)
if mibBuilder.loadTexts:oacGdoiGmKekOriginalLifetime.setUnits(_H)
_OacGdoiGmKekRemainingLifetime_Type=Unsigned32
_OacGdoiGmKekRemainingLifetime_Object=MibTableColumn
oacGdoiGmKekRemainingLifetime=_OacGdoiGmKekRemainingLifetime_Object((1,3,6,1,4,1,13191,10,3,4,1224,1,3,2,1,10),_OacGdoiGmKekRemainingLifetime_Type())
oacGdoiGmKekRemainingLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:oacGdoiGmKekRemainingLifetime.setStatus(_A)
if mibBuilder.loadTexts:oacGdoiGmKekRemainingLifetime.setUnits(_H)
mibBuilder.exportSymbols(_C,**{'OacGdoiIdentificationType':OacGdoiIdentificationType,'OacGdoiIdentificationValue':OacGdoiIdentificationValue,'OacGdoiSPI':OacGdoiSPI,'OacGdoiKEKEncryptionAlgorithm':OacGdoiKEKEncryptionAlgorithm,'OacGdoiHashAlogrithm':OacGdoiHashAlogrithm,'OacGdoiSignatureMethod':OacGdoiSignatureMethod,'oacExpIMGdoiMIB':oacExpIMGdoiMIB,'oacGdoiMIBObjects':oacGdoiMIBObjects,'oacGdoiGroupTable':oacGdoiGroupTable,'oacGdoiGroupEntry':oacGdoiGroupEntry,_D:oacGdoiGroupName,'oacGdoiGroupIdType':oacGdoiGroupIdType,'oacGdoiGroupIdValue':oacGdoiGroupIdValue,'oacGdoiGm':oacGdoiGm,'oacGdoiGmTable':oacGdoiGmTable,'oacGdoiGmEntry':oacGdoiGmEntry,'oacGdoiGmIdType':oacGdoiGmIdType,'oacGdoiGmIdValue':oacGdoiGmIdValue,'oacGdoiGmRegKeyServerIdValue':oacGdoiGmRegKeyServerIdValue,_F:oacGdoiGmActiveKEK,'oacGdoiGmRekeysReceived':oacGdoiGmRekeysReceived,'oacGdoiPolicy':oacGdoiPolicy,'oacGdoiGmKekTable':oacGdoiGmKekTable,'oacGdoiGmKekEntry':oacGdoiGmKekEntry,_G:oacGdoiGmKekSPI,'oacGdoiGmKekSrcIdValue':oacGdoiGmKekSrcIdValue,'oacGdoiGmKekDstIdValue':oacGdoiGmKekDstIdValue,'oacGdoiGmKekEncryptAlg':oacGdoiGmKekEncryptAlg,'oacGdoiGmKekEncryptKeyLength':oacGdoiGmKekEncryptKeyLength,'oacGdoiGmKekSigHashAlg':oacGdoiGmKekSigHashAlg,'oacGdoiGmKekSigAlg':oacGdoiGmKekSigAlg,'oacGdoiGmKekSigKeyLength':oacGdoiGmKekSigKeyLength,'oacGdoiGmKekOriginalLifetime':oacGdoiGmKekOriginalLifetime,'oacGdoiGmKekRemainingLifetime':oacGdoiGmKekRemainingLifetime})