_G='ntwsLicenseInfoEntryFeature'
_F='ntwsMobilityMemberEntryAddr'
_E='NTWS-BASIC-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
NtwsLicenseFeature,=mibBuilder.importSymbols('NTWS-LICENSE-FEATURE-TC-MIB','NtwsLicenseFeature')
ntwsMibs,=mibBuilder.importSymbols('NTWS-ROOT-MIB','ntwsMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
ntwsBasic=ModuleIdentity((1,3,6,1,4,1,45,6,1,4,2))
if mibBuilder.loadTexts:ntwsBasic.setRevisions(('2009-11-16 00:10','2007-08-16 00:09','2006-07-10 00:08','2006-04-14 00:07','2005-01-01 00:00'))
_NtwsBasicSystemInfo_ObjectIdentity=ObjectIdentity
ntwsBasicSystemInfo=_NtwsBasicSystemInfo_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,2,1))
class _NtwsSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtwsSerialNumber_Type.__name__=_D
_NtwsSerialNumber_Object=MibScalar
ntwsSerialNumber=_NtwsSerialNumber_Object((1,3,6,1,4,1,45,6,1,4,2,1,1),_NtwsSerialNumber_Type())
ntwsSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSerialNumber.setStatus(_A)
class _NtwsSwMajorVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_NtwsSwMajorVersionNumber_Type.__name__=_C
_NtwsSwMajorVersionNumber_Object=MibScalar
ntwsSwMajorVersionNumber=_NtwsSwMajorVersionNumber_Object((1,3,6,1,4,1,45,6,1,4,2,1,2),_NtwsSwMajorVersionNumber_Type())
ntwsSwMajorVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSwMajorVersionNumber.setStatus(_A)
class _NtwsSwMinorVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_NtwsSwMinorVersionNumber_Type.__name__=_C
_NtwsSwMinorVersionNumber_Object=MibScalar
ntwsSwMinorVersionNumber=_NtwsSwMinorVersionNumber_Object((1,3,6,1,4,1,45,6,1,4,2,1,3),_NtwsSwMinorVersionNumber_Type())
ntwsSwMinorVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsSwMinorVersionNumber.setStatus(_A)
class _NtwsVersionString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NtwsVersionString_Type.__name__=_D
_NtwsVersionString_Object=MibScalar
ntwsVersionString=_NtwsVersionString_Object((1,3,6,1,4,1,45,6,1,4,2,1,4),_NtwsVersionString_Type())
ntwsVersionString.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsVersionString.setStatus(_A)
_NtwsMobilityDomainInfo_ObjectIdentity=ObjectIdentity
ntwsMobilityDomainInfo=_NtwsMobilityDomainInfo_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,2,2))
class _NtwsMobilityDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtwsMobilityDomainName_Type.__name__=_D
_NtwsMobilityDomainName_Object=MibScalar
ntwsMobilityDomainName=_NtwsMobilityDomainName_Object((1,3,6,1,4,1,45,6,1,4,2,2,1),_NtwsMobilityDomainName_Type())
ntwsMobilityDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsMobilityDomainName.setStatus(_A)
_NtwsMobilitySeedIp_Type=IpAddress
_NtwsMobilitySeedIp_Object=MibScalar
ntwsMobilitySeedIp=_NtwsMobilitySeedIp_Object((1,3,6,1,4,1,45,6,1,4,2,2,2),_NtwsMobilitySeedIp_Type())
ntwsMobilitySeedIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsMobilitySeedIp.setStatus(_A)
class _NtwsMobilityMemberTableSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_NtwsMobilityMemberTableSize_Type.__name__=_C
_NtwsMobilityMemberTableSize_Object=MibScalar
ntwsMobilityMemberTableSize=_NtwsMobilityMemberTableSize_Object((1,3,6,1,4,1,45,6,1,4,2,2,3),_NtwsMobilityMemberTableSize_Type())
ntwsMobilityMemberTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsMobilityMemberTableSize.setStatus(_A)
_NtwsMobilityMemberTable_Object=MibTable
ntwsMobilityMemberTable=_NtwsMobilityMemberTable_Object((1,3,6,1,4,1,45,6,1,4,2,2,4))
if mibBuilder.loadTexts:ntwsMobilityMemberTable.setStatus(_A)
_NtwsMobilityMemberEntry_Object=MibTableRow
ntwsMobilityMemberEntry=_NtwsMobilityMemberEntry_Object((1,3,6,1,4,1,45,6,1,4,2,2,4,1))
ntwsMobilityMemberEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ntwsMobilityMemberEntry.setStatus(_A)
_NtwsMobilityMemberEntryAddr_Type=IpAddress
_NtwsMobilityMemberEntryAddr_Object=MibTableColumn
ntwsMobilityMemberEntryAddr=_NtwsMobilityMemberEntryAddr_Object((1,3,6,1,4,1,45,6,1,4,2,2,4,1,1),_NtwsMobilityMemberEntryAddr_Type())
ntwsMobilityMemberEntryAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsMobilityMemberEntryAddr.setStatus(_A)
_NtwsLicenseInfoGroup_ObjectIdentity=ObjectIdentity
ntwsLicenseInfoGroup=_NtwsLicenseInfoGroup_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,2,3))
class _NtwsLicenseInfoTableSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_NtwsLicenseInfoTableSize_Type.__name__=_C
_NtwsLicenseInfoTableSize_Object=MibScalar
ntwsLicenseInfoTableSize=_NtwsLicenseInfoTableSize_Object((1,3,6,1,4,1,45,6,1,4,2,3,1),_NtwsLicenseInfoTableSize_Type())
ntwsLicenseInfoTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsLicenseInfoTableSize.setStatus(_A)
_NtwsLicenseInfoTable_Object=MibTable
ntwsLicenseInfoTable=_NtwsLicenseInfoTable_Object((1,3,6,1,4,1,45,6,1,4,2,3,2))
if mibBuilder.loadTexts:ntwsLicenseInfoTable.setStatus(_A)
_NtwsLicenseInfoEntry_Object=MibTableRow
ntwsLicenseInfoEntry=_NtwsLicenseInfoEntry_Object((1,3,6,1,4,1,45,6,1,4,2,3,2,1))
ntwsLicenseInfoEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:ntwsLicenseInfoEntry.setStatus(_A)
_NtwsLicenseInfoEntryFeature_Type=NtwsLicenseFeature
_NtwsLicenseInfoEntryFeature_Object=MibTableColumn
ntwsLicenseInfoEntryFeature=_NtwsLicenseInfoEntryFeature_Object((1,3,6,1,4,1,45,6,1,4,2,3,2,1,1),_NtwsLicenseInfoEntryFeature_Type())
ntwsLicenseInfoEntryFeature.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ntwsLicenseInfoEntryFeature.setStatus(_A)
class _NtwsLicenseInfoEntryValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_NtwsLicenseInfoEntryValue_Type.__name__=_C
_NtwsLicenseInfoEntryValue_Object=MibTableColumn
ntwsLicenseInfoEntryValue=_NtwsLicenseInfoEntryValue_Object((1,3,6,1,4,1,45,6,1,4,2,3,2,1,2),_NtwsLicenseInfoEntryValue_Type())
ntwsLicenseInfoEntryValue.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsLicenseInfoEntryValue.setStatus(_A)
class _NtwsLicenseInfoEntryDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtwsLicenseInfoEntryDescr_Type.__name__=_D
_NtwsLicenseInfoEntryDescr_Object=MibTableColumn
ntwsLicenseInfoEntryDescr=_NtwsLicenseInfoEntryDescr_Object((1,3,6,1,4,1,45,6,1,4,2,3,2,1,3),_NtwsLicenseInfoEntryDescr_Type())
ntwsLicenseInfoEntryDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:ntwsLicenseInfoEntryDescr.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ntwsBasic':ntwsBasic,'ntwsBasicSystemInfo':ntwsBasicSystemInfo,'ntwsSerialNumber':ntwsSerialNumber,'ntwsSwMajorVersionNumber':ntwsSwMajorVersionNumber,'ntwsSwMinorVersionNumber':ntwsSwMinorVersionNumber,'ntwsVersionString':ntwsVersionString,'ntwsMobilityDomainInfo':ntwsMobilityDomainInfo,'ntwsMobilityDomainName':ntwsMobilityDomainName,'ntwsMobilitySeedIp':ntwsMobilitySeedIp,'ntwsMobilityMemberTableSize':ntwsMobilityMemberTableSize,'ntwsMobilityMemberTable':ntwsMobilityMemberTable,'ntwsMobilityMemberEntry':ntwsMobilityMemberEntry,_F:ntwsMobilityMemberEntryAddr,'ntwsLicenseInfoGroup':ntwsLicenseInfoGroup,'ntwsLicenseInfoTableSize':ntwsLicenseInfoTableSize,'ntwsLicenseInfoTable':ntwsLicenseInfoTable,'ntwsLicenseInfoEntry':ntwsLicenseInfoEntry,_G:ntwsLicenseInfoEntryFeature,'ntwsLicenseInfoEntryValue':ntwsLicenseInfoEntryValue,'ntwsLicenseInfoEntryDescr':ntwsLicenseInfoEntryDescr})