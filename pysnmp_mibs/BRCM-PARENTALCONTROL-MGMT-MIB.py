_D='OctetString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataMgmtMIBObjects,=mibBuilder.importSymbols('BRCM-CABLEDATA-MGMT-MIB','cableDataMgmtMIBObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
parentalControlMgmt=ModuleIdentity((1,3,6,1,4,1,4413,2,2,2,1,8))
if mibBuilder.loadTexts:parentalControlMgmt.setRevisions(('2007-02-05 00:00','2003-07-30 00:00','2003-04-17 00:00','2003-04-04 00:00'))
_PctlService_ObjectIdentity=ObjectIdentity
pctlService=_PctlService_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,8,1))
_PctlSubscriptionURL_Type=DisplayString
_PctlSubscriptionURL_Object=MibScalar
pctlSubscriptionURL=_PctlSubscriptionURL_Object((1,3,6,1,4,1,4413,2,2,2,1,8,1,1),_PctlSubscriptionURL_Type())
pctlSubscriptionURL.setMaxAccess(_B)
if mibBuilder.loadTexts:pctlSubscriptionURL.setStatus(_A)
class _PctlServiceModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('cerberianCMR',1),('cerberianADR',2),('rulespace',3)))
_PctlServiceModel_Type.__name__=_C
_PctlServiceModel_Object=MibScalar
pctlServiceModel=_PctlServiceModel_Object((1,3,6,1,4,1,4413,2,2,2,1,8,1,2),_PctlServiceModel_Type())
pctlServiceModel.setMaxAccess(_B)
if mibBuilder.loadTexts:pctlServiceModel.setStatus(_A)
_PctlServicePrimaryURL_Type=DisplayString
_PctlServicePrimaryURL_Object=MibScalar
pctlServicePrimaryURL=_PctlServicePrimaryURL_Object((1,3,6,1,4,1,4413,2,2,2,1,8,1,3),_PctlServicePrimaryURL_Type())
pctlServicePrimaryURL.setMaxAccess(_B)
if mibBuilder.loadTexts:pctlServicePrimaryURL.setStatus(_A)
_PctlServiceSecondaryURL_Type=DisplayString
_PctlServiceSecondaryURL_Object=MibScalar
pctlServiceSecondaryURL=_PctlServiceSecondaryURL_Object((1,3,6,1,4,1,4413,2,2,2,1,8,1,4),_PctlServiceSecondaryURL_Type())
pctlServiceSecondaryURL.setMaxAccess(_B)
if mibBuilder.loadTexts:pctlServiceSecondaryURL.setStatus(_A)
_PctlLicenseKey_Type=OctetString
_PctlLicenseKey_Object=MibScalar
pctlLicenseKey=_PctlLicenseKey_Object((1,3,6,1,4,1,4413,2,2,2,1,8,1,5),_PctlLicenseKey_Type())
pctlLicenseKey.setMaxAccess(_B)
if mibBuilder.loadTexts:pctlLicenseKey.setStatus(_A)
_PctlLicenseExpiration_Type=DateAndTime
_PctlLicenseExpiration_Object=MibScalar
pctlLicenseExpiration=_PctlLicenseExpiration_Object((1,3,6,1,4,1,4413,2,2,2,1,8,1,6),_PctlLicenseExpiration_Type())
pctlLicenseExpiration.setMaxAccess(_B)
if mibBuilder.loadTexts:pctlLicenseExpiration.setStatus(_A)
_PctlServiceSubscribeNow_Type=TruthValue
_PctlServiceSubscribeNow_Object=MibScalar
pctlServiceSubscribeNow=_PctlServiceSubscribeNow_Object((1,3,6,1,4,1,4413,2,2,2,1,8,1,7),_PctlServiceSubscribeNow_Type())
pctlServiceSubscribeNow.setMaxAccess(_B)
if mibBuilder.loadTexts:pctlServiceSubscribeNow.setStatus(_A)
class _PctlServiceSubscriptionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('notAttempted',0),('readyToSubscribe',1),('subscribedServiceNotStarted',2),('subscribedEstablishingService',3),('subscribedServiceRunning',4),('subscribedServiceError',5),('subscriptionFailed',6),('subscriptionExpired',7)))
_PctlServiceSubscriptionStatus_Type.__name__=_C
_PctlServiceSubscriptionStatus_Object=MibScalar
pctlServiceSubscriptionStatus=_PctlServiceSubscriptionStatus_Object((1,3,6,1,4,1,4413,2,2,2,1,8,1,8),_PctlServiceSubscriptionStatus_Type())
pctlServiceSubscriptionStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:pctlServiceSubscriptionStatus.setStatus(_A)
class _PctlCategoryList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_PctlCategoryList_Type.__name__=_D
_PctlCategoryList_Object=MibScalar
pctlCategoryList=_PctlCategoryList_Object((1,3,6,1,4,1,4413,2,2,2,1,8,1,9),_PctlCategoryList_Type())
pctlCategoryList.setMaxAccess(_B)
if mibBuilder.loadTexts:pctlCategoryList.setStatus(_A)
mibBuilder.exportSymbols('BRCM-PARENTALCONTROL-MGMT-MIB',**{'parentalControlMgmt':parentalControlMgmt,'pctlService':pctlService,'pctlSubscriptionURL':pctlSubscriptionURL,'pctlServiceModel':pctlServiceModel,'pctlServicePrimaryURL':pctlServicePrimaryURL,'pctlServiceSecondaryURL':pctlServiceSecondaryURL,'pctlLicenseKey':pctlLicenseKey,'pctlLicenseExpiration':pctlLicenseExpiration,'pctlServiceSubscribeNow':pctlServiceSubscribeNow,'pctlServiceSubscriptionStatus':pctlServiceSubscriptionStatus,'pctlCategoryList':pctlCategoryList})