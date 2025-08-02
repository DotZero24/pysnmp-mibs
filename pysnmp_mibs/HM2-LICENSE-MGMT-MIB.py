_Y='hm2LMFeatureStatus'
_X='hm2LMFeatureLicenseId'
_W='hm2LMFeatureCount'
_V='hm2LMFeatureBinaryID'
_U='hm2LMFeatureDescription'
_T='hm2LMLicenseAdminStatus'
_S='hm2LMLicenseOperStatus'
_R='hm2LMLicenseExpiryPeriod'
_Q='hm2LMLicenseModel'
_P='hm2LMLicenseKey'
_O='hm2LMLicenseVersion'
_N='hm2LMLicenseDescription'
_M='HmLmSwLvlCap'
_L='expired'
_K='accessible-for-notify'
_J='hm2LMFeatureId'
_I='inactive'
_H='active'
_G='hm2LMLicenseId'
_F='read-write'
_E='Integer32'
_D='SnmpAdminString'
_C='HM2-LICENSE-MGMT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2ConfigurationMibs,=mibBuilder.importSymbols('HM2-TC-MIB','hm2ConfigurationMibs')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hm2LicenseMgmtMib=ModuleIdentity((1,3,6,1,4,1,248,11,3))
if mibBuilder.loadTexts:hm2LicenseMgmtMib.setRevisions(('2012-08-03 00:00',))
class HmLmSwLvlCap(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('sw-lvl-default',0),('sw-lvl-2e',1),('sw-lvl-2s',2),('sw-lvl-2a',3),('sw-lvl-3s',4),('sw-lvl-3a',5)))
class HmLmLicenseLvlCap(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('none',0),('unicast-routing',1),('multicast-routing',2)))
_Hm2LicenseMgmtMibNotifications_ObjectIdentity=ObjectIdentity
hm2LicenseMgmtMibNotifications=_Hm2LicenseMgmtMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,3,0))
_Hm2LicenseMgmtMibObjects_ObjectIdentity=ObjectIdentity
hm2LicenseMgmtMibObjects=_Hm2LicenseMgmtMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,3,1))
_Hm2LMLicenseKeyGroup_ObjectIdentity=ObjectIdentity
hm2LMLicenseKeyGroup=_Hm2LMLicenseKeyGroup_ObjectIdentity((1,3,6,1,4,1,248,11,3,1,1))
class _Hm2LMLicenseKeyUdi_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2LMLicenseKeyUdi_Type.__name__=_D
_Hm2LMLicenseKeyUdi_Object=MibScalar
hm2LMLicenseKeyUdi=_Hm2LMLicenseKeyUdi_Object((1,3,6,1,4,1,248,11,3,1,1,1),_Hm2LMLicenseKeyUdi_Type())
hm2LMLicenseKeyUdi.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMLicenseKeyUdi.setStatus(_A)
class _Hm2LMLicenseKeyInstall_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2LMLicenseKeyInstall_Type.__name__=_D
_Hm2LMLicenseKeyInstall_Object=MibScalar
hm2LMLicenseKeyInstall=_Hm2LMLicenseKeyInstall_Object((1,3,6,1,4,1,248,11,3,1,1,2),_Hm2LMLicenseKeyInstall_Type())
hm2LMLicenseKeyInstall.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2LMLicenseKeyInstall.setStatus(_A)
class _Hm2LMLicenseKeyDelete_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2LMLicenseKeyDelete_Type.__name__=_D
_Hm2LMLicenseKeyDelete_Object=MibScalar
hm2LMLicenseKeyDelete=_Hm2LMLicenseKeyDelete_Object((1,3,6,1,4,1,248,11,3,1,1,3),_Hm2LMLicenseKeyDelete_Type())
hm2LMLicenseKeyDelete.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2LMLicenseKeyDelete.setStatus(_A)
_Hm2LMLicenseGroup_ObjectIdentity=ObjectIdentity
hm2LMLicenseGroup=_Hm2LMLicenseGroup_ObjectIdentity((1,3,6,1,4,1,248,11,3,1,2))
_Hm2LMLicenseTable_Object=MibTable
hm2LMLicenseTable=_Hm2LMLicenseTable_Object((1,3,6,1,4,1,248,11,3,1,2,1))
if mibBuilder.loadTexts:hm2LMLicenseTable.setStatus(_A)
_Hm2LMLicenseEntry_Object=MibTableRow
hm2LMLicenseEntry=_Hm2LMLicenseEntry_Object((1,3,6,1,4,1,248,11,3,1,2,1,1))
hm2LMLicenseEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:hm2LMLicenseEntry.setStatus(_A)
_Hm2LMLicenseId_Type=Integer32
_Hm2LMLicenseId_Object=MibTableColumn
hm2LMLicenseId=_Hm2LMLicenseId_Object((1,3,6,1,4,1,248,11,3,1,2,1,1,1),_Hm2LMLicenseId_Type())
hm2LMLicenseId.setMaxAccess(_K)
if mibBuilder.loadTexts:hm2LMLicenseId.setStatus(_A)
class _Hm2LMLicenseDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_Hm2LMLicenseDescription_Type.__name__=_D
_Hm2LMLicenseDescription_Object=MibTableColumn
hm2LMLicenseDescription=_Hm2LMLicenseDescription_Object((1,3,6,1,4,1,248,11,3,1,2,1,1,2),_Hm2LMLicenseDescription_Type())
hm2LMLicenseDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMLicenseDescription.setStatus(_A)
class _Hm2LMLicenseVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Hm2LMLicenseVersion_Type.__name__=_D
_Hm2LMLicenseVersion_Object=MibTableColumn
hm2LMLicenseVersion=_Hm2LMLicenseVersion_Object((1,3,6,1,4,1,248,11,3,1,2,1,1,3),_Hm2LMLicenseVersion_Type())
hm2LMLicenseVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMLicenseVersion.setStatus(_A)
class _Hm2LMLicenseKey_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2LMLicenseKey_Type.__name__=_D
_Hm2LMLicenseKey_Object=MibTableColumn
hm2LMLicenseKey=_Hm2LMLicenseKey_Object((1,3,6,1,4,1,248,11,3,1,2,1,1,4),_Hm2LMLicenseKey_Type())
hm2LMLicenseKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMLicenseKey.setStatus(_A)
class _Hm2LMLicenseModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('demo',1),('permanent',2)))
_Hm2LMLicenseModel_Type.__name__=_E
_Hm2LMLicenseModel_Object=MibTableColumn
hm2LMLicenseModel=_Hm2LMLicenseModel_Object((1,3,6,1,4,1,248,11,3,1,2,1,1,5),_Hm2LMLicenseModel_Type())
hm2LMLicenseModel.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMLicenseModel.setStatus(_A)
_Hm2LMLicenseExpiryPeriod_Type=Integer32
_Hm2LMLicenseExpiryPeriod_Object=MibTableColumn
hm2LMLicenseExpiryPeriod=_Hm2LMLicenseExpiryPeriod_Object((1,3,6,1,4,1,248,11,3,1,2,1,1,6),_Hm2LMLicenseExpiryPeriod_Type())
hm2LMLicenseExpiryPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMLicenseExpiryPeriod.setStatus(_A)
class _Hm2LMLicenseOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_I,2),(_L,3),('error',4),('no-license',5)))
_Hm2LMLicenseOperStatus_Type.__name__=_E
_Hm2LMLicenseOperStatus_Object=MibTableColumn
hm2LMLicenseOperStatus=_Hm2LMLicenseOperStatus_Object((1,3,6,1,4,1,248,11,3,1,2,1,1,9),_Hm2LMLicenseOperStatus_Type())
hm2LMLicenseOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMLicenseOperStatus.setStatus(_A)
class _Hm2LMLicenseAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_Hm2LMLicenseAdminStatus_Type.__name__=_E
_Hm2LMLicenseAdminStatus_Object=MibTableColumn
hm2LMLicenseAdminStatus=_Hm2LMLicenseAdminStatus_Object((1,3,6,1,4,1,248,11,3,1,2,1,1,10),_Hm2LMLicenseAdminStatus_Type())
hm2LMLicenseAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2LMLicenseAdminStatus.setStatus(_A)
_Hm2LMLicenseSwLvlCap_Type=HmLmSwLvlCap
_Hm2LMLicenseSwLvlCap_Object=MibTableColumn
hm2LMLicenseSwLvlCap=_Hm2LMLicenseSwLvlCap_Object((1,3,6,1,4,1,248,11,3,1,2,1,1,11),_Hm2LMLicenseSwLvlCap_Type())
hm2LMLicenseSwLvlCap.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMLicenseSwLvlCap.setStatus(_A)
_Hm2LMFeatureGroup_ObjectIdentity=ObjectIdentity
hm2LMFeatureGroup=_Hm2LMFeatureGroup_ObjectIdentity((1,3,6,1,4,1,248,11,3,1,3))
_Hm2LMFeatureTable_Object=MibTable
hm2LMFeatureTable=_Hm2LMFeatureTable_Object((1,3,6,1,4,1,248,11,3,1,3,1))
if mibBuilder.loadTexts:hm2LMFeatureTable.setStatus(_A)
_Hm2LMFeatureEntry_Object=MibTableRow
hm2LMFeatureEntry=_Hm2LMFeatureEntry_Object((1,3,6,1,4,1,248,11,3,1,3,1,1))
hm2LMFeatureEntry.setIndexNames((1,_C,_J))
if mibBuilder.loadTexts:hm2LMFeatureEntry.setStatus(_A)
_Hm2LMFeatureId_Type=ObjectIdentifier
_Hm2LMFeatureId_Object=MibTableColumn
hm2LMFeatureId=_Hm2LMFeatureId_Object((1,3,6,1,4,1,248,11,3,1,3,1,1,1),_Hm2LMFeatureId_Type())
hm2LMFeatureId.setMaxAccess(_K)
if mibBuilder.loadTexts:hm2LMFeatureId.setStatus(_A)
_Hm2LMFeatureDescription_Type=SnmpAdminString
_Hm2LMFeatureDescription_Object=MibTableColumn
hm2LMFeatureDescription=_Hm2LMFeatureDescription_Object((1,3,6,1,4,1,248,11,3,1,3,1,1,2),_Hm2LMFeatureDescription_Type())
hm2LMFeatureDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMFeatureDescription.setStatus(_A)
_Hm2LMFeatureBinaryID_Type=Unsigned32
_Hm2LMFeatureBinaryID_Object=MibTableColumn
hm2LMFeatureBinaryID=_Hm2LMFeatureBinaryID_Object((1,3,6,1,4,1,248,11,3,1,3,1,1,3),_Hm2LMFeatureBinaryID_Type())
hm2LMFeatureBinaryID.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMFeatureBinaryID.setStatus(_A)
_Hm2LMFeatureCount_Type=Unsigned32
_Hm2LMFeatureCount_Object=MibTableColumn
hm2LMFeatureCount=_Hm2LMFeatureCount_Object((1,3,6,1,4,1,248,11,3,1,3,1,1,4),_Hm2LMFeatureCount_Type())
hm2LMFeatureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMFeatureCount.setStatus(_A)
_Hm2LMFeatureLicenseId_Type=Integer32
_Hm2LMFeatureLicenseId_Object=MibTableColumn
hm2LMFeatureLicenseId=_Hm2LMFeatureLicenseId_Object((1,3,6,1,4,1,248,11,3,1,3,1,1,5),_Hm2LMFeatureLicenseId_Type())
hm2LMFeatureLicenseId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMFeatureLicenseId.setStatus(_A)
class _Hm2LMFeatureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_I,2),(_L,3),('error',4)))
_Hm2LMFeatureStatus_Type.__name__=_E
_Hm2LMFeatureStatus_Object=MibTableColumn
hm2LMFeatureStatus=_Hm2LMFeatureStatus_Object((1,3,6,1,4,1,248,11,3,1,3,1,1,9),_Hm2LMFeatureStatus_Type())
hm2LMFeatureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMFeatureStatus.setStatus(_A)
_Hm2LMFeatureSwLvlCap_Type=HmLmSwLvlCap
_Hm2LMFeatureSwLvlCap_Object=MibTableColumn
hm2LMFeatureSwLvlCap=_Hm2LMFeatureSwLvlCap_Object((1,3,6,1,4,1,248,11,3,1,3,1,1,10),_Hm2LMFeatureSwLvlCap_Type())
hm2LMFeatureSwLvlCap.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMFeatureSwLvlCap.setStatus(_A)
_Hm2LMFeatureSwLicCap_Type=HmLmLicenseLvlCap
_Hm2LMFeatureSwLicCap_Object=MibTableColumn
hm2LMFeatureSwLicCap=_Hm2LMFeatureSwLicCap_Object((1,3,6,1,4,1,248,11,3,1,3,1,1,11),_Hm2LMFeatureSwLicCap_Type())
hm2LMFeatureSwLicCap.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMFeatureSwLicCap.setStatus(_A)
_Hm2LMSwLvlGroup_ObjectIdentity=ObjectIdentity
hm2LMSwLvlGroup=_Hm2LMSwLvlGroup_ObjectIdentity((1,3,6,1,4,1,248,11,3,1,4))
_Hm2LMSwLvlDescription_Type=SnmpAdminString
_Hm2LMSwLvlDescription_Object=MibScalar
hm2LMSwLvlDescription=_Hm2LMSwLvlDescription_Object((1,3,6,1,4,1,248,11,3,1,4,1),_Hm2LMSwLvlDescription_Type())
hm2LMSwLvlDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMSwLvlDescription.setStatus(_A)
_Hm2LMSwLvlCap_Type=HmLmSwLvlCap
_Hm2LMSwLvlCap_Object=MibScalar
hm2LMSwLvlCap=_Hm2LMSwLvlCap_Object((1,3,6,1,4,1,248,11,3,1,4,2),_Hm2LMSwLvlCap_Type())
hm2LMSwLvlCap.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMSwLvlCap.setStatus(_A)
class _Hm2LMSwLvlAdminStatus_Type(HmLmSwLvlCap):defaultBinValue='1'
_Hm2LMSwLvlAdminStatus_Type.__name__=_M
_Hm2LMSwLvlAdminStatus_Object=MibScalar
hm2LMSwLvlAdminStatus=_Hm2LMSwLvlAdminStatus_Object((1,3,6,1,4,1,248,11,3,1,4,3),_Hm2LMSwLvlAdminStatus_Type())
hm2LMSwLvlAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2LMSwLvlAdminStatus.setStatus(_A)
_Hm2LMSwLvlOperStatus_Type=HmLmSwLvlCap
_Hm2LMSwLvlOperStatus_Object=MibScalar
hm2LMSwLvlOperStatus=_Hm2LMSwLvlOperStatus_Object((1,3,6,1,4,1,248,11,3,1,4,4),_Hm2LMSwLvlOperStatus_Type())
hm2LMSwLvlOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LMSwLvlOperStatus.setStatus(_A)
hm2LMLicenseChangeTrap=NotificationType((1,3,6,1,4,1,248,11,3,0,1))
hm2LMLicenseChangeTrap.setObjects(*((_C,_G),(_C,_N),(_C,_O),(_C,_P),(_C,_Q),(_C,_R),(_C,_S),(_C,_T)))
if mibBuilder.loadTexts:hm2LMLicenseChangeTrap.setStatus(_A)
hm2LMFeatureChangeTrap=NotificationType((1,3,6,1,4,1,248,11,3,0,2))
hm2LMFeatureChangeTrap.setObjects(*((_C,_J),(_C,_U),(_C,_V),(_C,_W),(_C,_X),(_C,_Y)))
if mibBuilder.loadTexts:hm2LMFeatureChangeTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_M:HmLmSwLvlCap,'HmLmLicenseLvlCap':HmLmLicenseLvlCap,'hm2LicenseMgmtMib':hm2LicenseMgmtMib,'hm2LicenseMgmtMibNotifications':hm2LicenseMgmtMibNotifications,'hm2LMLicenseChangeTrap':hm2LMLicenseChangeTrap,'hm2LMFeatureChangeTrap':hm2LMFeatureChangeTrap,'hm2LicenseMgmtMibObjects':hm2LicenseMgmtMibObjects,'hm2LMLicenseKeyGroup':hm2LMLicenseKeyGroup,'hm2LMLicenseKeyUdi':hm2LMLicenseKeyUdi,'hm2LMLicenseKeyInstall':hm2LMLicenseKeyInstall,'hm2LMLicenseKeyDelete':hm2LMLicenseKeyDelete,'hm2LMLicenseGroup':hm2LMLicenseGroup,'hm2LMLicenseTable':hm2LMLicenseTable,'hm2LMLicenseEntry':hm2LMLicenseEntry,_G:hm2LMLicenseId,_N:hm2LMLicenseDescription,_O:hm2LMLicenseVersion,_P:hm2LMLicenseKey,_Q:hm2LMLicenseModel,_R:hm2LMLicenseExpiryPeriod,_S:hm2LMLicenseOperStatus,_T:hm2LMLicenseAdminStatus,'hm2LMLicenseSwLvlCap':hm2LMLicenseSwLvlCap,'hm2LMFeatureGroup':hm2LMFeatureGroup,'hm2LMFeatureTable':hm2LMFeatureTable,'hm2LMFeatureEntry':hm2LMFeatureEntry,_J:hm2LMFeatureId,_U:hm2LMFeatureDescription,_V:hm2LMFeatureBinaryID,_W:hm2LMFeatureCount,_X:hm2LMFeatureLicenseId,_Y:hm2LMFeatureStatus,'hm2LMFeatureSwLvlCap':hm2LMFeatureSwLvlCap,'hm2LMFeatureSwLicCap':hm2LMFeatureSwLicCap,'hm2LMSwLvlGroup':hm2LMSwLvlGroup,'hm2LMSwLvlDescription':hm2LMSwLvlDescription,'hm2LMSwLvlCap':hm2LMSwLvlCap,'hm2LMSwLvlAdminStatus':hm2LMSwLvlAdminStatus,'hm2LMSwLvlOperStatus':hm2LMSwLvlOperStatus})