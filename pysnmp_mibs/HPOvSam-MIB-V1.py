_U='storageDmn'
_T='serialNo'
_S='prodRev'
_R='prodId'
_Q='vendorId'
_P='uniqueId'
_O='sourceName'
_N='NotificationType'
_M='Integer32'
_L='contactFax'
_K='contactPager'
_J='contactHomePhone'
_I='contactWorkPhone'
_H='contactEmail'
_G='contactName'
_F='msgString'
_E='category'
_D='severityLevel'
_C='mandatory'
_B='read-only'
_A='HPOvSam-MIB-V1'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier',_N,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_N,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_HpStorageAssistant_ObjectIdentity=ObjectIdentity
hpStorageAssistant=_HpStorageAssistant_ObjectIdentity((1,3,6,1,4,1,11,2,27))
_HpSanManager_ObjectIdentity=ObjectIdentity
hpSanManager=_HpSanManager_ObjectIdentity((1,3,6,1,4,1,11,2,27,3))
_HpSanManagerTraps_ObjectIdentity=ObjectIdentity
hpSanManagerTraps=_HpSanManagerTraps_ObjectIdentity((1,3,6,1,4,1,11,2,27,3,0))
_HpSanManagerModules_ObjectIdentity=ObjectIdentity
hpSanManagerModules=_HpSanManagerModules_ObjectIdentity((1,3,6,1,4,1,11,2,27,3,1))
_HpSanManagerMibModule_ObjectIdentity=ObjectIdentity
hpSanManagerMibModule=_HpSanManagerMibModule_ObjectIdentity((1,3,6,1,4,1,11,2,27,3,1,1))
_MibModuleEventVars_ObjectIdentity=ObjectIdentity
mibModuleEventVars=_MibModuleEventVars_ObjectIdentity((1,3,6,1,4,1,11,2,27,3,1,1,1))
class _SeverityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('informational',1),('warning',2),('minor',3),('major',4),('critical',5)))
_SeverityLevel_Type.__name__=_M
_SeverityLevel_Object=MibScalar
severityLevel=_SeverityLevel_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,1),_SeverityLevel_Type())
severityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:severityLevel.setStatus(_C)
_Category_Type=DisplayString
_Category_Object=MibScalar
category=_Category_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,2),_Category_Type())
category.setMaxAccess(_B)
if mibBuilder.loadTexts:category.setStatus(_C)
_Id_Type=Integer32
_Id_Object=MibScalar
id=_Id_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,3),_Id_Type())
id.setMaxAccess(_B)
if mibBuilder.loadTexts:id.setStatus(_C)
_MsgString_Type=DisplayString
_MsgString_Object=MibScalar
msgString=_MsgString_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,4),_MsgString_Type())
msgString.setMaxAccess(_B)
if mibBuilder.loadTexts:msgString.setStatus(_C)
_ContactName_Type=DisplayString
_ContactName_Object=MibScalar
contactName=_ContactName_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,5),_ContactName_Type())
contactName.setMaxAccess(_B)
if mibBuilder.loadTexts:contactName.setStatus(_C)
_ContactEmail_Type=DisplayString
_ContactEmail_Object=MibScalar
contactEmail=_ContactEmail_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,6),_ContactEmail_Type())
contactEmail.setMaxAccess(_B)
if mibBuilder.loadTexts:contactEmail.setStatus(_C)
_ContactHomePhone_Type=DisplayString
_ContactHomePhone_Object=MibScalar
contactHomePhone=_ContactHomePhone_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,7),_ContactHomePhone_Type())
contactHomePhone.setMaxAccess(_B)
if mibBuilder.loadTexts:contactHomePhone.setStatus(_C)
_ContactWorkPhone_Type=DisplayString
_ContactWorkPhone_Object=MibScalar
contactWorkPhone=_ContactWorkPhone_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,8),_ContactWorkPhone_Type())
contactWorkPhone.setMaxAccess(_B)
if mibBuilder.loadTexts:contactWorkPhone.setStatus(_C)
_ContactPager_Type=DisplayString
_ContactPager_Object=MibScalar
contactPager=_ContactPager_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,9),_ContactPager_Type())
contactPager.setMaxAccess(_B)
if mibBuilder.loadTexts:contactPager.setStatus(_C)
_ContactFax_Type=DisplayString
_ContactFax_Object=MibScalar
contactFax=_ContactFax_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,10),_ContactFax_Type())
contactFax.setMaxAccess(_B)
if mibBuilder.loadTexts:contactFax.setStatus(_C)
_SourceName_Type=DisplayString
_SourceName_Object=MibScalar
sourceName=_SourceName_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,11),_SourceName_Type())
sourceName.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceName.setStatus(_C)
_UniqueId_Type=DisplayString
_UniqueId_Object=MibScalar
uniqueId=_UniqueId_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,12),_UniqueId_Type())
uniqueId.setMaxAccess(_B)
if mibBuilder.loadTexts:uniqueId.setStatus(_C)
_VendorId_Type=DisplayString
_VendorId_Object=MibScalar
vendorId=_VendorId_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,13),_VendorId_Type())
vendorId.setMaxAccess(_B)
if mibBuilder.loadTexts:vendorId.setStatus(_C)
_ProdId_Type=DisplayString
_ProdId_Object=MibScalar
prodId=_ProdId_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,14),_ProdId_Type())
prodId.setMaxAccess(_B)
if mibBuilder.loadTexts:prodId.setStatus(_C)
_ProdRev_Type=DisplayString
_ProdRev_Object=MibScalar
prodRev=_ProdRev_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,15),_ProdRev_Type())
prodRev.setMaxAccess(_B)
if mibBuilder.loadTexts:prodRev.setStatus(_C)
_SerialNo_Type=DisplayString
_SerialNo_Object=MibScalar
serialNo=_SerialNo_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,16),_SerialNo_Type())
serialNo.setMaxAccess(_B)
if mibBuilder.loadTexts:serialNo.setStatus(_C)
_StorageDmn_Type=DisplayString
_StorageDmn_Object=MibScalar
storageDmn=_StorageDmn_Object((1,3,6,1,4,1,11,2,27,3,1,1,1,17),_StorageDmn_Type())
storageDmn.setMaxAccess(_B)
if mibBuilder.loadTexts:storageDmn.setStatus(_C)
genericSanEvent=NotificationType((1,3,6,1,4,1,11,2,27,3,0,1))
genericSanEvent.setObjects(*((_A,_D),(_A,_E),(_A,'id'),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:genericSanEvent.setStatus('')
sanDeviceEvent=NotificationType((1,3,6,1,4,1,11,2,27,3,0,2))
sanDeviceEvent.setObjects(*((_A,_D),(_A,_E),(_A,'id'),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:sanDeviceEvent.setStatus('')
mibBuilder.exportSymbols(_A,**{'hp':hp,'nm':nm,'hpStorageAssistant':hpStorageAssistant,'hpSanManager':hpSanManager,'hpSanManagerTraps':hpSanManagerTraps,'genericSanEvent':genericSanEvent,'sanDeviceEvent':sanDeviceEvent,'hpSanManagerModules':hpSanManagerModules,'hpSanManagerMibModule':hpSanManagerMibModule,'mibModuleEventVars':mibModuleEventVars,_D:severityLevel,_E:category,'id':id,_F:msgString,_G:contactName,_H:contactEmail,_J:contactHomePhone,_I:contactWorkPhone,_K:contactPager,_L:contactFax,_O:sourceName,_P:uniqueId,_Q:vendorId,_R:prodId,_S:prodRev,_T:serialNo,_U:storageDmn})