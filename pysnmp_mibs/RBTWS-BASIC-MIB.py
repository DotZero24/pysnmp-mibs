_G='rbtwsLicenseInfoEntryFeature'
_F='rbtwsMobilityMemberEntryAddr'
_E='RBTWS-BASIC-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rbtwsMibs,=mibBuilder.importSymbols('RBTWS-ROOT-MIB','rbtwsMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
rbtwsBasic=ModuleIdentity((1,3,6,1,4,1,52,4,15,1,4,2))
if mibBuilder.loadTexts:rbtwsBasic.setRevisions(('2006-07-10 00:08','2006-04-14 00:07','2005-01-01 00:00'))
class RbtwsLicenseFeature(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('maxSupportedAPsOrDAPs',2)))
_RbtwsBasicSystemInfo_ObjectIdentity=ObjectIdentity
rbtwsBasicSystemInfo=_RbtwsBasicSystemInfo_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,2,1))
class _RbtwsSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RbtwsSerialNumber_Type.__name__=_D
_RbtwsSerialNumber_Object=MibScalar
rbtwsSerialNumber=_RbtwsSerialNumber_Object((1,3,6,1,4,1,52,4,15,1,4,2,1,1),_RbtwsSerialNumber_Type())
rbtwsSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSerialNumber.setStatus(_A)
class _RbtwsSwMajorVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_RbtwsSwMajorVersionNumber_Type.__name__=_C
_RbtwsSwMajorVersionNumber_Object=MibScalar
rbtwsSwMajorVersionNumber=_RbtwsSwMajorVersionNumber_Object((1,3,6,1,4,1,52,4,15,1,4,2,1,2),_RbtwsSwMajorVersionNumber_Type())
rbtwsSwMajorVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSwMajorVersionNumber.setStatus(_A)
class _RbtwsSwMinorVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_RbtwsSwMinorVersionNumber_Type.__name__=_C
_RbtwsSwMinorVersionNumber_Object=MibScalar
rbtwsSwMinorVersionNumber=_RbtwsSwMinorVersionNumber_Object((1,3,6,1,4,1,52,4,15,1,4,2,1,3),_RbtwsSwMinorVersionNumber_Type())
rbtwsSwMinorVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsSwMinorVersionNumber.setStatus(_A)
class _RbtwsVersionString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_RbtwsVersionString_Type.__name__=_D
_RbtwsVersionString_Object=MibScalar
rbtwsVersionString=_RbtwsVersionString_Object((1,3,6,1,4,1,52,4,15,1,4,2,1,4),_RbtwsVersionString_Type())
rbtwsVersionString.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsVersionString.setStatus(_A)
_RbtwsMobilityDomainInfo_ObjectIdentity=ObjectIdentity
rbtwsMobilityDomainInfo=_RbtwsMobilityDomainInfo_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,2,2))
class _RbtwsMobilityDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RbtwsMobilityDomainName_Type.__name__=_D
_RbtwsMobilityDomainName_Object=MibScalar
rbtwsMobilityDomainName=_RbtwsMobilityDomainName_Object((1,3,6,1,4,1,52,4,15,1,4,2,2,1),_RbtwsMobilityDomainName_Type())
rbtwsMobilityDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsMobilityDomainName.setStatus(_A)
_RbtwsMobilitySeedIp_Type=IpAddress
_RbtwsMobilitySeedIp_Object=MibScalar
rbtwsMobilitySeedIp=_RbtwsMobilitySeedIp_Object((1,3,6,1,4,1,52,4,15,1,4,2,2,2),_RbtwsMobilitySeedIp_Type())
rbtwsMobilitySeedIp.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsMobilitySeedIp.setStatus(_A)
class _RbtwsMobilityMemberTableSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_RbtwsMobilityMemberTableSize_Type.__name__=_C
_RbtwsMobilityMemberTableSize_Object=MibScalar
rbtwsMobilityMemberTableSize=_RbtwsMobilityMemberTableSize_Object((1,3,6,1,4,1,52,4,15,1,4,2,2,3),_RbtwsMobilityMemberTableSize_Type())
rbtwsMobilityMemberTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsMobilityMemberTableSize.setStatus(_A)
_RbtwsMobilityMemberTable_Object=MibTable
rbtwsMobilityMemberTable=_RbtwsMobilityMemberTable_Object((1,3,6,1,4,1,52,4,15,1,4,2,2,4))
if mibBuilder.loadTexts:rbtwsMobilityMemberTable.setStatus(_A)
_RbtwsMobilityMemberEntry_Object=MibTableRow
rbtwsMobilityMemberEntry=_RbtwsMobilityMemberEntry_Object((1,3,6,1,4,1,52,4,15,1,4,2,2,4,1))
rbtwsMobilityMemberEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:rbtwsMobilityMemberEntry.setStatus(_A)
_RbtwsMobilityMemberEntryAddr_Type=IpAddress
_RbtwsMobilityMemberEntryAddr_Object=MibTableColumn
rbtwsMobilityMemberEntryAddr=_RbtwsMobilityMemberEntryAddr_Object((1,3,6,1,4,1,52,4,15,1,4,2,2,4,1,1),_RbtwsMobilityMemberEntryAddr_Type())
rbtwsMobilityMemberEntryAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsMobilityMemberEntryAddr.setStatus(_A)
_RbtwsLicenseInfoGroup_ObjectIdentity=ObjectIdentity
rbtwsLicenseInfoGroup=_RbtwsLicenseInfoGroup_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,2,3))
class _RbtwsLicenseInfoTableSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_RbtwsLicenseInfoTableSize_Type.__name__=_C
_RbtwsLicenseInfoTableSize_Object=MibScalar
rbtwsLicenseInfoTableSize=_RbtwsLicenseInfoTableSize_Object((1,3,6,1,4,1,52,4,15,1,4,2,3,1),_RbtwsLicenseInfoTableSize_Type())
rbtwsLicenseInfoTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsLicenseInfoTableSize.setStatus(_A)
_RbtwsLicenseInfoTable_Object=MibTable
rbtwsLicenseInfoTable=_RbtwsLicenseInfoTable_Object((1,3,6,1,4,1,52,4,15,1,4,2,3,2))
if mibBuilder.loadTexts:rbtwsLicenseInfoTable.setStatus(_A)
_RbtwsLicenseInfoEntry_Object=MibTableRow
rbtwsLicenseInfoEntry=_RbtwsLicenseInfoEntry_Object((1,3,6,1,4,1,52,4,15,1,4,2,3,2,1))
rbtwsLicenseInfoEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:rbtwsLicenseInfoEntry.setStatus(_A)
_RbtwsLicenseInfoEntryFeature_Type=RbtwsLicenseFeature
_RbtwsLicenseInfoEntryFeature_Object=MibTableColumn
rbtwsLicenseInfoEntryFeature=_RbtwsLicenseInfoEntryFeature_Object((1,3,6,1,4,1,52,4,15,1,4,2,3,2,1,1),_RbtwsLicenseInfoEntryFeature_Type())
rbtwsLicenseInfoEntryFeature.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rbtwsLicenseInfoEntryFeature.setStatus(_A)
class _RbtwsLicenseInfoEntryValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_RbtwsLicenseInfoEntryValue_Type.__name__=_C
_RbtwsLicenseInfoEntryValue_Object=MibTableColumn
rbtwsLicenseInfoEntryValue=_RbtwsLicenseInfoEntryValue_Object((1,3,6,1,4,1,52,4,15,1,4,2,3,2,1,2),_RbtwsLicenseInfoEntryValue_Type())
rbtwsLicenseInfoEntryValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsLicenseInfoEntryValue.setStatus(_A)
class _RbtwsLicenseInfoEntryDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RbtwsLicenseInfoEntryDescr_Type.__name__=_D
_RbtwsLicenseInfoEntryDescr_Object=MibTableColumn
rbtwsLicenseInfoEntryDescr=_RbtwsLicenseInfoEntryDescr_Object((1,3,6,1,4,1,52,4,15,1,4,2,3,2,1,3),_RbtwsLicenseInfoEntryDescr_Type())
rbtwsLicenseInfoEntryDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:rbtwsLicenseInfoEntryDescr.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'RbtwsLicenseFeature':RbtwsLicenseFeature,'rbtwsBasic':rbtwsBasic,'rbtwsBasicSystemInfo':rbtwsBasicSystemInfo,'rbtwsSerialNumber':rbtwsSerialNumber,'rbtwsSwMajorVersionNumber':rbtwsSwMajorVersionNumber,'rbtwsSwMinorVersionNumber':rbtwsSwMinorVersionNumber,'rbtwsVersionString':rbtwsVersionString,'rbtwsMobilityDomainInfo':rbtwsMobilityDomainInfo,'rbtwsMobilityDomainName':rbtwsMobilityDomainName,'rbtwsMobilitySeedIp':rbtwsMobilitySeedIp,'rbtwsMobilityMemberTableSize':rbtwsMobilityMemberTableSize,'rbtwsMobilityMemberTable':rbtwsMobilityMemberTable,'rbtwsMobilityMemberEntry':rbtwsMobilityMemberEntry,_F:rbtwsMobilityMemberEntryAddr,'rbtwsLicenseInfoGroup':rbtwsLicenseInfoGroup,'rbtwsLicenseInfoTableSize':rbtwsLicenseInfoTableSize,'rbtwsLicenseInfoTable':rbtwsLicenseInfoTable,'rbtwsLicenseInfoEntry':rbtwsLicenseInfoEntry,_G:rbtwsLicenseInfoEntryFeature,'rbtwsLicenseInfoEntryValue':rbtwsLicenseInfoEntryValue,'rbtwsLicenseInfoEntryDescr':rbtwsLicenseInfoEntryDescr})