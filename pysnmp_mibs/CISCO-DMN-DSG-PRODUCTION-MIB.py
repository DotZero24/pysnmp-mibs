_D='Integer32'
_C='read-only'
_B='current'
_A='DisplayString'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_A,'PhysAddress','TextualConvention')
ciscoDSGProd=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,21))
if mibBuilder.loadTexts:ciscoDSGProd.setRevisions(('2010-08-24 07:00','2009-12-20 12:00'))
_ProdInfo_ObjectIdentity=ObjectIdentity
prodInfo=_ProdInfo_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,21,1))
class _ProdHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_ProdHostName_Type.__name__=_A
_ProdHostName_Object=MibScalar
prodHostName=_ProdHostName_Object((1,3,6,1,4,1,1429,2,2,5,21,1,1),_ProdHostName_Type())
prodHostName.setMaxAccess('read-write')
if mibBuilder.loadTexts:prodHostName.setStatus(_B)
class _ProdTrackingId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_ProdTrackingId_Type.__name__=_A
_ProdTrackingId_Object=MibScalar
prodTrackingId=_ProdTrackingId_Object((1,3,6,1,4,1,1429,2,2,5,21,1,2),_ProdTrackingId_Type())
prodTrackingId.setMaxAccess(_C)
if mibBuilder.loadTexts:prodTrackingId.setStatus(_B)
class _ProdModelNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,49))
_ProdModelNo_Type.__name__=_A
_ProdModelNo_Object=MibScalar
prodModelNo=_ProdModelNo_Object((1,3,6,1,4,1,1429,2,2,5,21,1,3),_ProdModelNo_Type())
prodModelNo.setMaxAccess(_C)
if mibBuilder.loadTexts:prodModelNo.setStatus(_B)
class _ProdModelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,49))
_ProdModelName_Type.__name__=_A
_ProdModelName_Object=MibScalar
prodModelName=_ProdModelName_Object((1,3,6,1,4,1,1429,2,2,5,21,1,4),_ProdModelName_Type())
prodModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:prodModelName.setStatus(_B)
class _ProdCatalogNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,49))
_ProdCatalogNo_Type.__name__=_A
_ProdCatalogNo_Object=MibScalar
prodCatalogNo=_ProdCatalogNo_Object((1,3,6,1,4,1,1429,2,2,5,21,1,5),_ProdCatalogNo_Type())
prodCatalogNo.setMaxAccess(_C)
if mibBuilder.loadTexts:prodCatalogNo.setStatus(_B)
class _ProdCustomerCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,49))
_ProdCustomerCode_Type.__name__=_A
_ProdCustomerCode_Object=MibScalar
prodCustomerCode=_ProdCustomerCode_Object((1,3,6,1,4,1,1429,2,2,5,21,1,6),_ProdCustomerCode_Type())
prodCustomerCode.setMaxAccess(_C)
if mibBuilder.loadTexts:prodCustomerCode.setStatus(_B)
class _ProdLimitVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,49))
_ProdLimitVer_Type.__name__=_A
_ProdLimitVer_Object=MibScalar
prodLimitVer=_ProdLimitVer_Object((1,3,6,1,4,1,1429,2,2,5,21,1,7),_ProdLimitVer_Type())
prodLimitVer.setMaxAccess(_C)
if mibBuilder.loadTexts:prodLimitVer.setStatus(_B)
class _ProdFPGADesignation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_ProdFPGADesignation_Type.__name__=_D
_ProdFPGADesignation_Object=MibScalar
prodFPGADesignation=_ProdFPGADesignation_Object((1,3,6,1,4,1,1429,2,2,5,21,1,8),_ProdFPGADesignation_Type())
prodFPGADesignation.setMaxAccess(_C)
if mibBuilder.loadTexts:prodFPGADesignation.setStatus(_B)
mibBuilder.exportSymbols('CISCO-DMN-DSG-PRODUCTION-MIB',**{'ciscoDSGProd':ciscoDSGProd,'prodInfo':prodInfo,'prodHostName':prodHostName,'prodTrackingId':prodTrackingId,'prodModelNo':prodModelNo,'prodModelName':prodModelName,'prodCatalogNo':prodCatalogNo,'prodCustomerCode':prodCustomerCode,'prodLimitVer':prodLimitVer,'prodFPGADesignation':prodFPGADesignation})