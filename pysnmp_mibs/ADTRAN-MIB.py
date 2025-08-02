_N='adCNDGroup'
_M='adBaseGroup'
_L='adProdTransType'
_K='adProdProductID'
_J='adProdPhysAddress'
_I='adProdSwVersion'
_H='adProdRevision'
_G='adProdSerialNumber'
_F='adProdCLEIcode'
_E='adProdPartNumber'
_D='adProdName'
_C='read-only'
_B='ADTRAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adtran=ModuleIdentity((1,3,6,1,4,1,664))
_AdProducts_ObjectIdentity=ObjectIdentity
adProducts=_AdProducts_ObjectIdentity((1,3,6,1,4,1,664,1))
_AdMgmt_ObjectIdentity=ObjectIdentity
adMgmt=_AdMgmt_ObjectIdentity((1,3,6,1,4,1,664,2))
_AdAdmin_ObjectIdentity=ObjectIdentity
adAdmin=_AdAdmin_ObjectIdentity((1,3,6,1,4,1,664,3))
_AdProductInfo_ObjectIdentity=ObjectIdentity
adProductInfo=_AdProductInfo_ObjectIdentity((1,3,6,1,4,1,664,3,1))
_AdProdName_Type=DisplayString
_AdProdName_Object=MibScalar
adProdName=_AdProdName_Object((1,3,6,1,4,1,664,3,1,1),_AdProdName_Type())
adProdName.setMaxAccess(_C)
if mibBuilder.loadTexts:adProdName.setStatus(_A)
_AdProdPartNumber_Type=DisplayString
_AdProdPartNumber_Object=MibScalar
adProdPartNumber=_AdProdPartNumber_Object((1,3,6,1,4,1,664,3,1,2),_AdProdPartNumber_Type())
adProdPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adProdPartNumber.setStatus(_A)
_AdProdCLEIcode_Type=DisplayString
_AdProdCLEIcode_Object=MibScalar
adProdCLEIcode=_AdProdCLEIcode_Object((1,3,6,1,4,1,664,3,1,3),_AdProdCLEIcode_Type())
adProdCLEIcode.setMaxAccess(_C)
if mibBuilder.loadTexts:adProdCLEIcode.setStatus(_A)
_AdProdSerialNumber_Type=DisplayString
_AdProdSerialNumber_Object=MibScalar
adProdSerialNumber=_AdProdSerialNumber_Object((1,3,6,1,4,1,664,3,1,4),_AdProdSerialNumber_Type())
adProdSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adProdSerialNumber.setStatus(_A)
_AdProdRevision_Type=DisplayString
_AdProdRevision_Object=MibScalar
adProdRevision=_AdProdRevision_Object((1,3,6,1,4,1,664,3,1,5),_AdProdRevision_Type())
adProdRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:adProdRevision.setStatus(_A)
_AdProdSwVersion_Type=DisplayString
_AdProdSwVersion_Object=MibScalar
adProdSwVersion=_AdProdSwVersion_Object((1,3,6,1,4,1,664,3,1,6),_AdProdSwVersion_Type())
adProdSwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adProdSwVersion.setStatus(_A)
_AdProdPhysAddress_Type=PhysAddress
_AdProdPhysAddress_Object=MibScalar
adProdPhysAddress=_AdProdPhysAddress_Object((1,3,6,1,4,1,664,3,1,7),_AdProdPhysAddress_Type())
adProdPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adProdPhysAddress.setStatus(_A)
_AdProdProductID_Type=ObjectIdentifier
_AdProdProductID_Object=MibScalar
adProdProductID=_AdProdProductID_Object((1,3,6,1,4,1,664,3,1,8),_AdProdProductID_Type())
adProdProductID.setMaxAccess(_C)
if mibBuilder.loadTexts:adProdProductID.setStatus(_A)
_AdProdTransType_Type=DisplayString
_AdProdTransType_Object=MibScalar
adProdTransType=_AdProdTransType_Object((1,3,6,1,4,1,664,3,1,9),_AdProdTransType_Type())
adProdTransType.setMaxAccess(_C)
if mibBuilder.loadTexts:adProdTransType.setStatus(_A)
_AdPerform_ObjectIdentity=ObjectIdentity
adPerform=_AdPerform_ObjectIdentity((1,3,6,1,4,1,664,4))
_AdShared_ObjectIdentity=ObjectIdentity
adShared=_AdShared_ObjectIdentity((1,3,6,1,4,1,664,5))
_AdIdentity_ObjectIdentity=ObjectIdentity
adIdentity=_AdIdentity_ObjectIdentity((1,3,6,1,4,1,664,6))
_AdIdentityShared_ObjectIdentity=ObjectIdentity
adIdentityShared=_AdIdentityShared_ObjectIdentity((1,3,6,1,4,1,664,6,10000))
_AdAgentCapModule_ObjectIdentity=ObjectIdentity
adAgentCapModule=_AdAgentCapModule_ObjectIdentity((1,3,6,1,4,1,664,7))
_AdAgentCapProduct_ObjectIdentity=ObjectIdentity
adAgentCapProduct=_AdAgentCapProduct_ObjectIdentity((1,3,6,1,4,1,664,7,1))
_AdAgentCapShared_ObjectIdentity=ObjectIdentity
adAgentCapShared=_AdAgentCapShared_ObjectIdentity((1,3,6,1,4,1,664,7,2))
_AdConformance_ObjectIdentity=ObjectIdentity
adConformance=_AdConformance_ObjectIdentity((1,3,6,1,4,1,664,99))
_AdCompliances_ObjectIdentity=ObjectIdentity
adCompliances=_AdCompliances_ObjectIdentity((1,3,6,1,4,1,664,99,1))
_AdMIBGroups_ObjectIdentity=ObjectIdentity
adMIBGroups=_AdMIBGroups_ObjectIdentity((1,3,6,1,4,1,664,99,2))
_AdComplianceShared_ObjectIdentity=ObjectIdentity
adComplianceShared=_AdComplianceShared_ObjectIdentity((1,3,6,1,4,1,664,99,10000))
_AdLegalPolicy_ObjectIdentity=ObjectIdentity
adLegalPolicy=_AdLegalPolicy_ObjectIdentity((1,3,6,1,4,1,664,100))
_AdManagementPolicy_ObjectIdentity=ObjectIdentity
adManagementPolicy=_AdManagementPolicy_ObjectIdentity((1,3,6,1,4,1,664,101))
adBaseGroup=ObjectGroup((1,3,6,1,4,1,664,99,2,1))
adBaseGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:adBaseGroup.setStatus(_A)
adCNDGroup=ObjectGroup((1,3,6,1,4,1,664,99,2,2))
adCNDGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:adCNDGroup.setStatus(_A)
adCompliance=ModuleCompliance((1,3,6,1,4,1,664,99,1,1))
adCompliance.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:adCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adtran':adtran,'adProducts':adProducts,'adMgmt':adMgmt,'adAdmin':adAdmin,'adProductInfo':adProductInfo,_D:adProdName,_E:adProdPartNumber,_F:adProdCLEIcode,_G:adProdSerialNumber,_H:adProdRevision,_I:adProdSwVersion,_J:adProdPhysAddress,_K:adProdProductID,_L:adProdTransType,'adPerform':adPerform,'adShared':adShared,'adIdentity':adIdentity,'adIdentityShared':adIdentityShared,'adAgentCapModule':adAgentCapModule,'adAgentCapProduct':adAgentCapProduct,'adAgentCapShared':adAgentCapShared,'adConformance':adConformance,'adCompliances':adCompliances,'adCompliance':adCompliance,'adMIBGroups':adMIBGroups,_M:adBaseGroup,_N:adCNDGroup,'adComplianceShared':adComplianceShared,'adLegalPolicy':adLegalPolicy,'adManagementPolicy':adManagementPolicy})