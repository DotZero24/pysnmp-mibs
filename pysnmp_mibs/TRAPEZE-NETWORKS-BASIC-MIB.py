_G='trpzLicenseInfoEntryFeature'
_F='trpzMobilityMemberEntryAddr'
_E='TRAPEZE-NETWORKS-BASIC-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
TrpzLicenseFeature,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-LICENSE-FEATURE-TC-MIB','TrpzLicenseFeature')
trpzMibs,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-ROOT-MIB','trpzMibs')
trpzBasic=ModuleIdentity((1,3,6,1,4,1,14525,4,2))
if mibBuilder.loadTexts:trpzBasic.setRevisions(('2009-11-16 00:10','2006-07-10 00:08','2006-04-14 00:07','2005-01-01 00:00'))
_TrpzBasicSystemInfo_ObjectIdentity=ObjectIdentity
trpzBasicSystemInfo=_TrpzBasicSystemInfo_ObjectIdentity((1,3,6,1,4,1,14525,4,2,1))
class _TrpzSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TrpzSerialNumber_Type.__name__=_D
_TrpzSerialNumber_Object=MibScalar
trpzSerialNumber=_TrpzSerialNumber_Object((1,3,6,1,4,1,14525,4,2,1,1),_TrpzSerialNumber_Type())
trpzSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSerialNumber.setStatus(_A)
class _TrpzSwMajorVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_TrpzSwMajorVersionNumber_Type.__name__=_C
_TrpzSwMajorVersionNumber_Object=MibScalar
trpzSwMajorVersionNumber=_TrpzSwMajorVersionNumber_Object((1,3,6,1,4,1,14525,4,2,1,2),_TrpzSwMajorVersionNumber_Type())
trpzSwMajorVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSwMajorVersionNumber.setStatus(_A)
class _TrpzSwMinorVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_TrpzSwMinorVersionNumber_Type.__name__=_C
_TrpzSwMinorVersionNumber_Object=MibScalar
trpzSwMinorVersionNumber=_TrpzSwMinorVersionNumber_Object((1,3,6,1,4,1,14525,4,2,1,3),_TrpzSwMinorVersionNumber_Type())
trpzSwMinorVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzSwMinorVersionNumber.setStatus(_A)
class _TrpzVersionString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TrpzVersionString_Type.__name__=_D
_TrpzVersionString_Object=MibScalar
trpzVersionString=_TrpzVersionString_Object((1,3,6,1,4,1,14525,4,2,1,4),_TrpzVersionString_Type())
trpzVersionString.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzVersionString.setStatus(_A)
_TrpzMobilityDomainInfo_ObjectIdentity=ObjectIdentity
trpzMobilityDomainInfo=_TrpzMobilityDomainInfo_ObjectIdentity((1,3,6,1,4,1,14525,4,2,2))
class _TrpzMobilityDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TrpzMobilityDomainName_Type.__name__=_D
_TrpzMobilityDomainName_Object=MibScalar
trpzMobilityDomainName=_TrpzMobilityDomainName_Object((1,3,6,1,4,1,14525,4,2,2,1),_TrpzMobilityDomainName_Type())
trpzMobilityDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzMobilityDomainName.setStatus(_A)
_TrpzMobilitySeedIp_Type=IpAddress
_TrpzMobilitySeedIp_Object=MibScalar
trpzMobilitySeedIp=_TrpzMobilitySeedIp_Object((1,3,6,1,4,1,14525,4,2,2,2),_TrpzMobilitySeedIp_Type())
trpzMobilitySeedIp.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzMobilitySeedIp.setStatus(_A)
class _TrpzMobilityMemberTableSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_TrpzMobilityMemberTableSize_Type.__name__=_C
_TrpzMobilityMemberTableSize_Object=MibScalar
trpzMobilityMemberTableSize=_TrpzMobilityMemberTableSize_Object((1,3,6,1,4,1,14525,4,2,2,3),_TrpzMobilityMemberTableSize_Type())
trpzMobilityMemberTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzMobilityMemberTableSize.setStatus(_A)
_TrpzMobilityMemberTable_Object=MibTable
trpzMobilityMemberTable=_TrpzMobilityMemberTable_Object((1,3,6,1,4,1,14525,4,2,2,4))
if mibBuilder.loadTexts:trpzMobilityMemberTable.setStatus(_A)
_TrpzMobilityMemberEntry_Object=MibTableRow
trpzMobilityMemberEntry=_TrpzMobilityMemberEntry_Object((1,3,6,1,4,1,14525,4,2,2,4,1))
trpzMobilityMemberEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:trpzMobilityMemberEntry.setStatus(_A)
_TrpzMobilityMemberEntryAddr_Type=IpAddress
_TrpzMobilityMemberEntryAddr_Object=MibTableColumn
trpzMobilityMemberEntryAddr=_TrpzMobilityMemberEntryAddr_Object((1,3,6,1,4,1,14525,4,2,2,4,1,1),_TrpzMobilityMemberEntryAddr_Type())
trpzMobilityMemberEntryAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzMobilityMemberEntryAddr.setStatus(_A)
_TrpzLicenseInfoGroup_ObjectIdentity=ObjectIdentity
trpzLicenseInfoGroup=_TrpzLicenseInfoGroup_ObjectIdentity((1,3,6,1,4,1,14525,4,2,3))
class _TrpzLicenseInfoTableSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_TrpzLicenseInfoTableSize_Type.__name__=_C
_TrpzLicenseInfoTableSize_Object=MibScalar
trpzLicenseInfoTableSize=_TrpzLicenseInfoTableSize_Object((1,3,6,1,4,1,14525,4,2,3,1),_TrpzLicenseInfoTableSize_Type())
trpzLicenseInfoTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzLicenseInfoTableSize.setStatus(_A)
_TrpzLicenseInfoTable_Object=MibTable
trpzLicenseInfoTable=_TrpzLicenseInfoTable_Object((1,3,6,1,4,1,14525,4,2,3,2))
if mibBuilder.loadTexts:trpzLicenseInfoTable.setStatus(_A)
_TrpzLicenseInfoEntry_Object=MibTableRow
trpzLicenseInfoEntry=_TrpzLicenseInfoEntry_Object((1,3,6,1,4,1,14525,4,2,3,2,1))
trpzLicenseInfoEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:trpzLicenseInfoEntry.setStatus(_A)
_TrpzLicenseInfoEntryFeature_Type=TrpzLicenseFeature
_TrpzLicenseInfoEntryFeature_Object=MibTableColumn
trpzLicenseInfoEntryFeature=_TrpzLicenseInfoEntryFeature_Object((1,3,6,1,4,1,14525,4,2,3,2,1,1),_TrpzLicenseInfoEntryFeature_Type())
trpzLicenseInfoEntryFeature.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:trpzLicenseInfoEntryFeature.setStatus(_A)
class _TrpzLicenseInfoEntryValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_TrpzLicenseInfoEntryValue_Type.__name__=_C
_TrpzLicenseInfoEntryValue_Object=MibTableColumn
trpzLicenseInfoEntryValue=_TrpzLicenseInfoEntryValue_Object((1,3,6,1,4,1,14525,4,2,3,2,1,2),_TrpzLicenseInfoEntryValue_Type())
trpzLicenseInfoEntryValue.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzLicenseInfoEntryValue.setStatus(_A)
class _TrpzLicenseInfoEntryDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TrpzLicenseInfoEntryDescr_Type.__name__=_D
_TrpzLicenseInfoEntryDescr_Object=MibTableColumn
trpzLicenseInfoEntryDescr=_TrpzLicenseInfoEntryDescr_Object((1,3,6,1,4,1,14525,4,2,3,2,1,3),_TrpzLicenseInfoEntryDescr_Type())
trpzLicenseInfoEntryDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:trpzLicenseInfoEntryDescr.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'trpzBasic':trpzBasic,'trpzBasicSystemInfo':trpzBasicSystemInfo,'trpzSerialNumber':trpzSerialNumber,'trpzSwMajorVersionNumber':trpzSwMajorVersionNumber,'trpzSwMinorVersionNumber':trpzSwMinorVersionNumber,'trpzVersionString':trpzVersionString,'trpzMobilityDomainInfo':trpzMobilityDomainInfo,'trpzMobilityDomainName':trpzMobilityDomainName,'trpzMobilitySeedIp':trpzMobilitySeedIp,'trpzMobilityMemberTableSize':trpzMobilityMemberTableSize,'trpzMobilityMemberTable':trpzMobilityMemberTable,'trpzMobilityMemberEntry':trpzMobilityMemberEntry,_F:trpzMobilityMemberEntryAddr,'trpzLicenseInfoGroup':trpzLicenseInfoGroup,'trpzLicenseInfoTableSize':trpzLicenseInfoTableSize,'trpzLicenseInfoTable':trpzLicenseInfoTable,'trpzLicenseInfoEntry':trpzLicenseInfoEntry,_G:trpzLicenseInfoEntryFeature,'trpzLicenseInfoEntryValue':trpzLicenseInfoEntryValue,'trpzLicenseInfoEntryDescr':trpzLicenseInfoEntryDescr})