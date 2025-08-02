_W='hpHttpMgBasicNetCitizenTrapGroup'
_V='hpHttpMgBasicNetCitizenGroup'
_U='hpHttpMgShutdown'
_T='hpHttpMgHealthTrap'
_S='hpHttpMgPhone'
_R='hpHttpMgAssetNumber'
_Q='hpHttpMgSerialNumber'
_P='hpHttpMgROMVersion'
_O='hpHttpMgHWVersion'
_N='hpHttpMgVersion'
_M='hpHttpMgProduct'
_L='hpHttpMgManufacturer'
_K='hpHttpMgID'
_J='hpHttpMgMgmtSrvrURL'
_I='hpHttpMgDefaultURL'
_H='Integer32'
_G='hpHttpMgDefaultGroup'
_F='hpHttpMgHealth'
_E='read-write'
_D='read-only'
_C='Utf8String'
_B='HP-httpManageable-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpHttpMgMod=ModuleIdentity((1,3,6,1,4,1,11,2,36,1))
if mibBuilder.loadTexts:hpHttpMgMod.setRevisions(('1997-06-26 00:00','1996-06-12 00:00'))
class Utf8String(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_HpWebMgmt_ObjectIdentity=ObjectIdentity
hpWebMgmt=_HpWebMgmt_ObjectIdentity((1,3,6,1,4,1,11,2,36))
_HpHttpMgTraps_ObjectIdentity=ObjectIdentity
hpHttpMgTraps=_HpHttpMgTraps_ObjectIdentity((1,3,6,1,4,1,11,2,36,1,0))
_HpHttpMgObjects_ObjectIdentity=ObjectIdentity
hpHttpMgObjects=_HpHttpMgObjects_ObjectIdentity((1,3,6,1,4,1,11,2,36,1,1))
_HpHttpMgDefaults_ObjectIdentity=ObjectIdentity
hpHttpMgDefaults=_HpHttpMgDefaults_ObjectIdentity((1,3,6,1,4,1,11,2,36,1,1,1))
_HpHttpMgDefaultURL_Type=Utf8String
_HpHttpMgDefaultURL_Object=MibScalar
hpHttpMgDefaultURL=_HpHttpMgDefaultURL_Object((1,3,6,1,4,1,11,2,36,1,1,1,1),_HpHttpMgDefaultURL_Type())
hpHttpMgDefaultURL.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgDefaultURL.setStatus(_A)
_HpHttpMgNetCitizen_ObjectIdentity=ObjectIdentity
hpHttpMgNetCitizen=_HpHttpMgNetCitizen_ObjectIdentity((1,3,6,1,4,1,11,2,36,1,1,2))
_HpHttpMgMgmtSrvrURL_Type=Utf8String
_HpHttpMgMgmtSrvrURL_Object=MibScalar
hpHttpMgMgmtSrvrURL=_HpHttpMgMgmtSrvrURL_Object((1,3,6,1,4,1,11,2,36,1,1,2,1),_HpHttpMgMgmtSrvrURL_Type())
hpHttpMgMgmtSrvrURL.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgMgmtSrvrURL.setStatus(_A)
_HpHttpMgID_Type=Utf8String
_HpHttpMgID_Object=MibScalar
hpHttpMgID=_HpHttpMgID_Object((1,3,6,1,4,1,11,2,36,1,1,2,2),_HpHttpMgID_Type())
hpHttpMgID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpHttpMgID.setStatus(_A)
class _HpHttpMgHealth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',1),('information',2),('ok',3),('warning',4),('critical',5),('nonrecoverable',6)))
_HpHttpMgHealth_Type.__name__=_H
_HpHttpMgHealth_Object=MibScalar
hpHttpMgHealth=_HpHttpMgHealth_Object((1,3,6,1,4,1,11,2,36,1,1,2,3),_HpHttpMgHealth_Type())
hpHttpMgHealth.setMaxAccess(_D)
if mibBuilder.loadTexts:hpHttpMgHealth.setStatus(_A)
_HpHttpMgManufacturer_Type=Utf8String
_HpHttpMgManufacturer_Object=MibScalar
hpHttpMgManufacturer=_HpHttpMgManufacturer_Object((1,3,6,1,4,1,11,2,36,1,1,2,4),_HpHttpMgManufacturer_Type())
hpHttpMgManufacturer.setMaxAccess(_D)
if mibBuilder.loadTexts:hpHttpMgManufacturer.setStatus(_A)
class _HpHttpMgProduct_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgProduct_Type.__name__=_C
_HpHttpMgProduct_Object=MibScalar
hpHttpMgProduct=_HpHttpMgProduct_Object((1,3,6,1,4,1,11,2,36,1,1,2,5),_HpHttpMgProduct_Type())
hpHttpMgProduct.setMaxAccess(_D)
if mibBuilder.loadTexts:hpHttpMgProduct.setStatus(_A)
class _HpHttpMgVersion_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgVersion_Type.__name__=_C
_HpHttpMgVersion_Object=MibScalar
hpHttpMgVersion=_HpHttpMgVersion_Object((1,3,6,1,4,1,11,2,36,1,1,2,6),_HpHttpMgVersion_Type())
hpHttpMgVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hpHttpMgVersion.setStatus(_A)
class _HpHttpMgHWVersion_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgHWVersion_Type.__name__=_C
_HpHttpMgHWVersion_Object=MibScalar
hpHttpMgHWVersion=_HpHttpMgHWVersion_Object((1,3,6,1,4,1,11,2,36,1,1,2,7),_HpHttpMgHWVersion_Type())
hpHttpMgHWVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hpHttpMgHWVersion.setStatus(_A)
class _HpHttpMgROMVersion_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgROMVersion_Type.__name__=_C
_HpHttpMgROMVersion_Object=MibScalar
hpHttpMgROMVersion=_HpHttpMgROMVersion_Object((1,3,6,1,4,1,11,2,36,1,1,2,8),_HpHttpMgROMVersion_Type())
hpHttpMgROMVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hpHttpMgROMVersion.setStatus(_A)
class _HpHttpMgSerialNumber_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgSerialNumber_Type.__name__=_C
_HpHttpMgSerialNumber_Object=MibScalar
hpHttpMgSerialNumber=_HpHttpMgSerialNumber_Object((1,3,6,1,4,1,11,2,36,1,1,2,9),_HpHttpMgSerialNumber_Type())
hpHttpMgSerialNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgSerialNumber.setStatus(_A)
class _HpHttpMgAssetNumber_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgAssetNumber_Type.__name__=_C
_HpHttpMgAssetNumber_Object=MibScalar
hpHttpMgAssetNumber=_HpHttpMgAssetNumber_Object((1,3,6,1,4,1,11,2,36,1,1,2,10),_HpHttpMgAssetNumber_Type())
hpHttpMgAssetNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgAssetNumber.setStatus(_A)
class _HpHttpMgPhone_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpHttpMgPhone_Type.__name__=_C
_HpHttpMgPhone_Object=MibScalar
hpHttpMgPhone=_HpHttpMgPhone_Object((1,3,6,1,4,1,11,2,36,1,1,2,11),_HpHttpMgPhone_Type())
hpHttpMgPhone.setMaxAccess(_E)
if mibBuilder.loadTexts:hpHttpMgPhone.setStatus(_A)
_HpHttpMgGroups_ObjectIdentity=ObjectIdentity
hpHttpMgGroups=_HpHttpMgGroups_ObjectIdentity((1,3,6,1,4,1,11,2,36,1,2))
_HpHttpMgCompliances_ObjectIdentity=ObjectIdentity
hpHttpMgCompliances=_HpHttpMgCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,36,1,3))
hpHttpMgDefaultGroup=ObjectGroup((1,3,6,1,4,1,11,2,36,1,2,1))
hpHttpMgDefaultGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:hpHttpMgDefaultGroup.setStatus(_A)
hpHttpMgBasicNetCitizenGroup=ObjectGroup((1,3,6,1,4,1,11,2,36,1,2,2))
hpHttpMgBasicNetCitizenGroup.setObjects(*((_B,_J),(_B,_K),(_B,_F),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hpHttpMgBasicNetCitizenGroup.setStatus(_A)
hpHttpMgExtendedNetCitizenGroup=ObjectGroup((1,3,6,1,4,1,11,2,36,1,2,4))
hpHttpMgExtendedNetCitizenGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:hpHttpMgExtendedNetCitizenGroup.setStatus(_A)
hpHttpMgHealthTrap=NotificationType((1,3,6,1,4,1,11,2,36,1,0,1))
hpHttpMgHealthTrap.setObjects((_B,_F))
if mibBuilder.loadTexts:hpHttpMgHealthTrap.setStatus(_A)
hpHttpMgShutdown=NotificationType((1,3,6,1,4,1,11,2,36,1,0,2))
if mibBuilder.loadTexts:hpHttpMgShutdown.setStatus(_A)
hpHttpMgBasicNetCitizenTrapGroup=NotificationGroup((1,3,6,1,4,1,11,2,36,1,2,3))
hpHttpMgBasicNetCitizenTrapGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:hpHttpMgBasicNetCitizenTrapGroup.setStatus(_A)
hpHttpMgExtendedNetCitizenTrapGroup=NotificationGroup((1,3,6,1,4,1,11,2,36,1,2,5))
hpHttpMgExtendedNetCitizenTrapGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:hpHttpMgExtendedNetCitizenTrapGroup.setStatus(_A)
hpHttpMgMinCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,36,1,3,1))
hpHttpMgMinCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:hpHttpMgMinCompliance.setStatus(_A)
hpHttpMgBasicNetCitizenCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,36,1,3,2))
hpHttpMgBasicNetCitizenCompliance.setObjects(*((_B,_G),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:hpHttpMgBasicNetCitizenCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_C:Utf8String,'hp':hp,'nm':nm,'hpWebMgmt':hpWebMgmt,'hpHttpMgMod':hpHttpMgMod,'hpHttpMgTraps':hpHttpMgTraps,_T:hpHttpMgHealthTrap,_U:hpHttpMgShutdown,'hpHttpMgObjects':hpHttpMgObjects,'hpHttpMgDefaults':hpHttpMgDefaults,_I:hpHttpMgDefaultURL,'hpHttpMgNetCitizen':hpHttpMgNetCitizen,_J:hpHttpMgMgmtSrvrURL,_K:hpHttpMgID,_F:hpHttpMgHealth,_L:hpHttpMgManufacturer,_M:hpHttpMgProduct,_N:hpHttpMgVersion,_O:hpHttpMgHWVersion,_P:hpHttpMgROMVersion,_Q:hpHttpMgSerialNumber,_R:hpHttpMgAssetNumber,_S:hpHttpMgPhone,'hpHttpMgGroups':hpHttpMgGroups,_G:hpHttpMgDefaultGroup,_V:hpHttpMgBasicNetCitizenGroup,_W:hpHttpMgBasicNetCitizenTrapGroup,'hpHttpMgExtendedNetCitizenGroup':hpHttpMgExtendedNetCitizenGroup,'hpHttpMgExtendedNetCitizenTrapGroup':hpHttpMgExtendedNetCitizenTrapGroup,'hpHttpMgCompliances':hpHttpMgCompliances,'hpHttpMgMinCompliance':hpHttpMgMinCompliance,'hpHttpMgBasicNetCitizenCompliance':hpHttpMgBasicNetCitizenCompliance})