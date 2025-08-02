_AO='clmLicenseFeatureStatusGroup'
_AN='clmLicenseInformationGroup2'
_AM='clmLicenseInformationGroup1'
_AL='clmLicenseInformationGroup'
_AK='clmLicenseExpiryWarningNotify'
_AJ='clmLicenseFileMissingNotify'
_AI='clmNoLicenseForFeatureNotify'
_AH='clmLicenseExpiryNotify'
_AG='clmWebOptimization'
_AF='clmCompressionPerformance'
_AE='clmModuleBandwidth'
_AD='clmMaxVirtualizedContext'
_AC='clmMaxSslTransactions'
_AB='clmPortLicCountUsedInternal'
_AA='clmPortLicCountMaxInternal'
_A9='clmPortLicCountUsed'
_A8='clmPortLicCountMax'
_A7='clmPortLicensingOper'
_A6='clmPortLicensingConfig'
_A5='clmLicenseDefaultLicenses'
_A4='clmLicenseEnabled'
_A3='clmLicenseRequestCommandStatus'
_A2='clmLicenseRequestCommand'
_A1='clmLicenseRequestAppName'
_A0='clmLicenseRequestFeatureName'
_z='clmLicenseRequestSpinLock'
_y='clmNotificationsEnable'
_x='clmNoOfLicensedFeatures'
_w='clmNoOfLicenseFilesInstalled'
_v='clmLicenseConfigCommandStatus'
_u='clmLicenseConfigCommand'
_t='clmLicenseFileTargetName'
_s='clmLicenseFileURI'
_r='clmLicenseConfigSpinLock'
_q='clmHostId'
_p='licenses'
_o='clmLicensedAppIndex'
_n='seconds'
_m='clmLicenseFileRowNumber'
_l='clmLicenseFileName'
_k='generalLicensingFailure'
_j='success'
_i='TruthValue'
_h='ifIndex'
_g='IF-MIB'
_f='clmLicenseInformationPortLicGroup'
_e='clmLicenseInformationGroupSup2'
_d='clmLicenseGracePeriodLeft'
_c='clmLicenseViolationWarnFlag'
_b='clmPortLicensingType'
_a='clmLicenseFeatureName'
_Z='Unsigned32'
_Y='clmLicenseInformationGroupSup1'
_X='clmLicenseInformationGroup3'
_W='clmLicensedAppName'
_V='clmLicenseGracePeriod'
_U='clmNoOfLicenseCurrentUsages'
_T='clmNoOfLicenseMaxUsages'
_S='clmLicenseFlag'
_R='clmLicenseFileRowContents'
_Q='clmLicenseFileNoOfRows'
_P='clmLicenseFileTimeStamp'
_O='not-accessible'
_N='clmLicenseRequestGroup'
_M='clmNoOfMissingUsageLicenses'
_L='clmNotificationGroup'
_K='clmNotificationsEnableGroup'
_J='clmNoOfInstalledLicensesGroup'
_I='clmLicenseInstallGroup'
_H='clmLicenseExpiryDate'
_G='deprecated'
_F='read-write'
_E='SnmpAdminString'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-LICENSE-MGR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_g,_h)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Z,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TestAndIncr,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TestAndIncr',_i)
ciscoLicenseMgrMIB=ModuleIdentity((1,3,6,1,4,1,9,9,369))
if mibBuilder.loadTexts:ciscoLicenseMgrMIB.setRevisions(('2008-11-04 00:00','2008-04-22 00:00','2007-08-02 00:00','2006-12-17 00:00','2005-09-30 00:00','2004-12-01 00:00','2004-07-20 00:00','2003-11-27 00:00','2003-10-30 00:00','2003-09-12 00:00'))
class ClmLicenseType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('portActivation',1),('portActivation10G',2)))
_CiscoLicenseMgrMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLicenseMgrMIBObjects=_CiscoLicenseMgrMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,369,1))
_CiscoLicenseMgrConfig_ObjectIdentity=ObjectIdentity
ciscoLicenseMgrConfig=_CiscoLicenseMgrConfig_ObjectIdentity((1,3,6,1,4,1,9,9,369,1,1))
class _ClmHostId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(40,40));fixedLength=40
_ClmHostId_Type.__name__=_E
_ClmHostId_Object=MibScalar
clmHostId=_ClmHostId_Object((1,3,6,1,4,1,9,9,369,1,1,1),_ClmHostId_Type())
clmHostId.setMaxAccess(_C)
if mibBuilder.loadTexts:clmHostId.setStatus(_B)
class _ClmNotificationsEnable_Type(TruthValue):defaultValue=1
_ClmNotificationsEnable_Type.__name__=_i
_ClmNotificationsEnable_Object=MibScalar
clmNotificationsEnable=_ClmNotificationsEnable_Object((1,3,6,1,4,1,9,9,369,1,1,2),_ClmNotificationsEnable_Type())
clmNotificationsEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:clmNotificationsEnable.setStatus(_B)
_ClmLicenseConfiguration_ObjectIdentity=ObjectIdentity
clmLicenseConfiguration=_ClmLicenseConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,369,1,2))
_ClmLicenseConfigSpinLock_Type=TestAndIncr
_ClmLicenseConfigSpinLock_Object=MibScalar
clmLicenseConfigSpinLock=_ClmLicenseConfigSpinLock_Object((1,3,6,1,4,1,9,9,369,1,2,1),_ClmLicenseConfigSpinLock_Type())
clmLicenseConfigSpinLock.setMaxAccess(_F)
if mibBuilder.loadTexts:clmLicenseConfigSpinLock.setStatus(_B)
class _ClmLicenseFileURI_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ClmLicenseFileURI_Type.__name__=_E
_ClmLicenseFileURI_Object=MibScalar
clmLicenseFileURI=_ClmLicenseFileURI_Object((1,3,6,1,4,1,9,9,369,1,2,2),_ClmLicenseFileURI_Type())
clmLicenseFileURI.setMaxAccess(_F)
if mibBuilder.loadTexts:clmLicenseFileURI.setStatus(_B)
class _ClmLicenseFileTargetName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ClmLicenseFileTargetName_Type.__name__=_E
_ClmLicenseFileTargetName_Object=MibScalar
clmLicenseFileTargetName=_ClmLicenseFileTargetName_Object((1,3,6,1,4,1,9,9,369,1,2,3),_ClmLicenseFileTargetName_Type())
clmLicenseFileTargetName.setMaxAccess(_F)
if mibBuilder.loadTexts:clmLicenseFileTargetName.setStatus(_B)
class _ClmLicenseConfigCommand_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('install',1),('uninstall',2),('noOp',3),('update',4)))
_ClmLicenseConfigCommand_Type.__name__=_D
_ClmLicenseConfigCommand_Object=MibScalar
clmLicenseConfigCommand=_ClmLicenseConfigCommand_Object((1,3,6,1,4,1,9,9,369,1,2,4),_ClmLicenseConfigCommand_Type())
clmLicenseConfigCommand.setMaxAccess(_F)
if mibBuilder.loadTexts:clmLicenseConfigCommand.setStatus(_B)
class _ClmLicenseConfigCommandStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)));namedValues=NamedValues(*((_j,1),('inProgress',2),('corruptedLicenseFile',3),('targetLicenseFileAlreadyExist',4),('invalidLicenseFileName',5),('duplicateLicense',6),('licenseInUse',7),(_k,8),('none',9),('licenseExpiryConflict',10),('invalidLicenseCount',11),('notThisHost',12),('licenseInGraceExceeded',13),('licenseFileNotFound',14),('licenseFileMissing',15),('invalidLicenseFileExtension',16),('invalidURI',17),('noDemoLicenseSupport',18),('invalidPlatform',19),('licenseServerBusy',20),('invalidLicenseFeature',21),('noFeatureSupport',22),('emptyLicenseFile',23),('invalidServerLine',24),('invalidVendorLine',25),('invalidLicFilenameSize',26),('permanentLicenseExpiryConflict',27)))
_ClmLicenseConfigCommandStatus_Type.__name__=_D
_ClmLicenseConfigCommandStatus_Object=MibScalar
clmLicenseConfigCommandStatus=_ClmLicenseConfigCommandStatus_Object((1,3,6,1,4,1,9,9,369,1,2,5),_ClmLicenseConfigCommandStatus_Type())
clmLicenseConfigCommandStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clmLicenseConfigCommandStatus.setStatus(_B)
_ClmLicenseRequestSpinLock_Type=TestAndIncr
_ClmLicenseRequestSpinLock_Object=MibScalar
clmLicenseRequestSpinLock=_ClmLicenseRequestSpinLock_Object((1,3,6,1,4,1,9,9,369,1,2,6),_ClmLicenseRequestSpinLock_Type())
clmLicenseRequestSpinLock.setMaxAccess(_F)
if mibBuilder.loadTexts:clmLicenseRequestSpinLock.setStatus(_B)
class _ClmLicenseRequestFeatureName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_ClmLicenseRequestFeatureName_Type.__name__=_E
_ClmLicenseRequestFeatureName_Object=MibScalar
clmLicenseRequestFeatureName=_ClmLicenseRequestFeatureName_Object((1,3,6,1,4,1,9,9,369,1,2,7),_ClmLicenseRequestFeatureName_Type())
clmLicenseRequestFeatureName.setMaxAccess(_F)
if mibBuilder.loadTexts:clmLicenseRequestFeatureName.setStatus(_B)
class _ClmLicenseRequestAppName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ClmLicenseRequestAppName_Type.__name__=_E
_ClmLicenseRequestAppName_Object=MibScalar
clmLicenseRequestAppName=_ClmLicenseRequestAppName_Object((1,3,6,1,4,1,9,9,369,1,2,8),_ClmLicenseRequestAppName_Type())
clmLicenseRequestAppName.setMaxAccess(_F)
if mibBuilder.loadTexts:clmLicenseRequestAppName.setStatus(_B)
class _ClmLicenseRequestCommand_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('checkIn',1),('checkOut',2),('noOp',3)))
_ClmLicenseRequestCommand_Type.__name__=_D
_ClmLicenseRequestCommand_Object=MibScalar
clmLicenseRequestCommand=_ClmLicenseRequestCommand_Object((1,3,6,1,4,1,9,9,369,1,2,9),_ClmLicenseRequestCommand_Type())
clmLicenseRequestCommand.setMaxAccess(_F)
if mibBuilder.loadTexts:clmLicenseRequestCommand.setStatus(_B)
class _ClmLicenseRequestCommandStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_j,1),('none',2),('licenseDenied',3),('licenseTooMany',4),(_k,5),('invalidFeature',6),('licenseExpired',7),('licenseServerDown',8)))
_ClmLicenseRequestCommandStatus_Type.__name__=_D
_ClmLicenseRequestCommandStatus_Object=MibScalar
clmLicenseRequestCommandStatus=_ClmLicenseRequestCommandStatus_Object((1,3,6,1,4,1,9,9,369,1,2,10),_ClmLicenseRequestCommandStatus_Type())
clmLicenseRequestCommandStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clmLicenseRequestCommandStatus.setStatus(_B)
_ClmLicenseInformation_ObjectIdentity=ObjectIdentity
clmLicenseInformation=_ClmLicenseInformation_ObjectIdentity((1,3,6,1,4,1,9,9,369,1,3))
class _ClmNoOfLicenseFilesInstalled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_ClmNoOfLicenseFilesInstalled_Type.__name__=_D
_ClmNoOfLicenseFilesInstalled_Object=MibScalar
clmNoOfLicenseFilesInstalled=_ClmNoOfLicenseFilesInstalled_Object((1,3,6,1,4,1,9,9,369,1,3,1),_ClmNoOfLicenseFilesInstalled_Type())
clmNoOfLicenseFilesInstalled.setMaxAccess(_C)
if mibBuilder.loadTexts:clmNoOfLicenseFilesInstalled.setStatus(_B)
_ClmLicenseFileContentsTable_Object=MibTable
clmLicenseFileContentsTable=_ClmLicenseFileContentsTable_Object((1,3,6,1,4,1,9,9,369,1,3,2))
if mibBuilder.loadTexts:clmLicenseFileContentsTable.setStatus(_B)
_ClmLicenseFileContentsEntry_Object=MibTableRow
clmLicenseFileContentsEntry=_ClmLicenseFileContentsEntry_Object((1,3,6,1,4,1,9,9,369,1,3,2,1))
clmLicenseFileContentsEntry.setIndexNames((0,_A,_l),(0,_A,_m))
if mibBuilder.loadTexts:clmLicenseFileContentsEntry.setStatus(_B)
class _ClmLicenseFileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ClmLicenseFileName_Type.__name__=_E
_ClmLicenseFileName_Object=MibTableColumn
clmLicenseFileName=_ClmLicenseFileName_Object((1,3,6,1,4,1,9,9,369,1,3,2,1,1),_ClmLicenseFileName_Type())
clmLicenseFileName.setMaxAccess(_O)
if mibBuilder.loadTexts:clmLicenseFileName.setStatus(_B)
_ClmLicenseFileRowNumber_Type=Unsigned32
_ClmLicenseFileRowNumber_Object=MibTableColumn
clmLicenseFileRowNumber=_ClmLicenseFileRowNumber_Object((1,3,6,1,4,1,9,9,369,1,3,2,1,2),_ClmLicenseFileRowNumber_Type())
clmLicenseFileRowNumber.setMaxAccess(_O)
if mibBuilder.loadTexts:clmLicenseFileRowNumber.setStatus(_B)
_ClmLicenseFileTimeStamp_Type=DateAndTime
_ClmLicenseFileTimeStamp_Object=MibTableColumn
clmLicenseFileTimeStamp=_ClmLicenseFileTimeStamp_Object((1,3,6,1,4,1,9,9,369,1,3,2,1,3),_ClmLicenseFileTimeStamp_Type())
clmLicenseFileTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:clmLicenseFileTimeStamp.setStatus(_B)
_ClmLicenseFileNoOfRows_Type=Unsigned32
_ClmLicenseFileNoOfRows_Object=MibTableColumn
clmLicenseFileNoOfRows=_ClmLicenseFileNoOfRows_Object((1,3,6,1,4,1,9,9,369,1,3,2,1,4),_ClmLicenseFileNoOfRows_Type())
clmLicenseFileNoOfRows.setMaxAccess(_C)
if mibBuilder.loadTexts:clmLicenseFileNoOfRows.setStatus(_B)
class _ClmLicenseFileRowContents_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ClmLicenseFileRowContents_Type.__name__=_E
_ClmLicenseFileRowContents_Object=MibTableColumn
clmLicenseFileRowContents=_ClmLicenseFileRowContents_Object((1,3,6,1,4,1,9,9,369,1,3,2,1,5),_ClmLicenseFileRowContents_Type())
clmLicenseFileRowContents.setMaxAccess(_C)
if mibBuilder.loadTexts:clmLicenseFileRowContents.setStatus(_B)
class _ClmNoOfLicensedFeatures_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_ClmNoOfLicensedFeatures_Type.__name__=_D
_ClmNoOfLicensedFeatures_Object=MibScalar
clmNoOfLicensedFeatures=_ClmNoOfLicensedFeatures_Object((1,3,6,1,4,1,9,9,369,1,3,3),_ClmNoOfLicensedFeatures_Type())
clmNoOfLicensedFeatures.setMaxAccess(_C)
if mibBuilder.loadTexts:clmNoOfLicensedFeatures.setStatus(_B)
_ClmLicenseFeatureUsageTable_Object=MibTable
clmLicenseFeatureUsageTable=_ClmLicenseFeatureUsageTable_Object((1,3,6,1,4,1,9,9,369,1,3,4))
if mibBuilder.loadTexts:clmLicenseFeatureUsageTable.setStatus(_B)
_ClmLicenseFeatureUsageEntry_Object=MibTableRow
clmLicenseFeatureUsageEntry=_ClmLicenseFeatureUsageEntry_Object((1,3,6,1,4,1,9,9,369,1,3,4,1))
clmLicenseFeatureUsageEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:clmLicenseFeatureUsageEntry.setStatus(_B)
class _ClmLicenseFeatureName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_ClmLicenseFeatureName_Type.__name__=_E
_ClmLicenseFeatureName_Object=MibTableColumn
clmLicenseFeatureName=_ClmLicenseFeatureName_Object((1,3,6,1,4,1,9,9,369,1,3,4,1,1),_ClmLicenseFeatureName_Type())
clmLicenseFeatureName.setMaxAccess(_O)
if mibBuilder.loadTexts:clmLicenseFeatureName.setStatus(_B)
class _ClmLicenseFlag_Type(Bits):namedValues=NamedValues(*(('demo',0),('permanent',1),('counted',2),('unlicensed',3),('inGracePeriod',4),('inHonorPeriod',5)))
_ClmLicenseFlag_Type.__name__='Bits'
_ClmLicenseFlag_Object=MibTableColumn
clmLicenseFlag=_ClmLicenseFlag_Object((1,3,6,1,4,1,9,9,369,1,3,4,1,2),_ClmLicenseFlag_Type())
clmLicenseFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:clmLicenseFlag.setStatus(_B)
class _ClmNoOfLicenseMaxUsages_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ClmNoOfLicenseMaxUsages_Type.__name__=_D
_ClmNoOfLicenseMaxUsages_Object=MibTableColumn
clmNoOfLicenseMaxUsages=_ClmNoOfLicenseMaxUsages_Object((1,3,6,1,4,1,9,9,369,1,3,4,1,3),_ClmNoOfLicenseMaxUsages_Type())
clmNoOfLicenseMaxUsages.setMaxAccess(_C)
if mibBuilder.loadTexts:clmNoOfLicenseMaxUsages.setStatus(_B)
class _ClmNoOfMissingUsageLicenses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ClmNoOfMissingUsageLicenses_Type.__name__=_D
_ClmNoOfMissingUsageLicenses_Object=MibTableColumn
clmNoOfMissingUsageLicenses=_ClmNoOfMissingUsageLicenses_Object((1,3,6,1,4,1,9,9,369,1,3,4,1,4),_ClmNoOfMissingUsageLicenses_Type())
clmNoOfMissingUsageLicenses.setMaxAccess(_C)
if mibBuilder.loadTexts:clmNoOfMissingUsageLicenses.setStatus(_B)
class _ClmNoOfLicenseCurrentUsages_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ClmNoOfLicenseCurrentUsages_Type.__name__=_D
_ClmNoOfLicenseCurrentUsages_Object=MibTableColumn
clmNoOfLicenseCurrentUsages=_ClmNoOfLicenseCurrentUsages_Object((1,3,6,1,4,1,9,9,369,1,3,4,1,5),_ClmNoOfLicenseCurrentUsages_Type())
clmNoOfLicenseCurrentUsages.setMaxAccess(_C)
if mibBuilder.loadTexts:clmNoOfLicenseCurrentUsages.setStatus(_B)
_ClmLicenseExpiryDate_Type=DateAndTime
_ClmLicenseExpiryDate_Object=MibTableColumn
clmLicenseExpiryDate=_ClmLicenseExpiryDate_Object((1,3,6,1,4,1,9,9,369,1,3,4,1,6),_ClmLicenseExpiryDate_Type())
clmLicenseExpiryDate.setMaxAccess(_C)
if mibBuilder.loadTexts:clmLicenseExpiryDate.setStatus(_B)
class _ClmLicenseGracePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5184000))
_ClmLicenseGracePeriod_Type.__name__=_D
_ClmLicenseGracePeriod_Object=MibTableColumn
clmLicenseGracePeriod=_ClmLicenseGracePeriod_Object((1,3,6,1,4,1,9,9,369,1,3,4,1,7),_ClmLicenseGracePeriod_Type())
clmLicenseGracePeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:clmLicenseGracePeriod.setStatus(_G)
if mibBuilder.loadTexts:clmLicenseGracePeriod.setUnits(_n)
_ClmLicenseEnabled_Type=TruthValue
_ClmLicenseEnabled_Object=MibTableColumn
clmLicenseEnabled=_ClmLicenseEnabled_Object((1,3,6,1,4,1,9,9,369,1,3,4,1,8),_ClmLicenseEnabled_Type())
clmLicenseEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:clmLicenseEnabled.setStatus(_B)
class _ClmLicenseGracePeriodLeft_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ClmLicenseGracePeriodLeft_Type.__name__=_Z
_ClmLicenseGracePeriodLeft_Object=MibTableColumn
clmLicenseGracePeriodLeft=_ClmLicenseGracePeriodLeft_Object((1,3,6,1,4,1,9,9,369,1,3,4,1,9),_ClmLicenseGracePeriodLeft_Type())
clmLicenseGracePeriodLeft.setMaxAccess(_C)
if mibBuilder.loadTexts:clmLicenseGracePeriodLeft.setStatus(_B)
if mibBuilder.loadTexts:clmLicenseGracePeriodLeft.setUnits(_n)
class _ClmLicenseDefaultLicenses_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ClmLicenseDefaultLicenses_Type.__name__=_Z
_ClmLicenseDefaultLicenses_Object=MibTableColumn
clmLicenseDefaultLicenses=_ClmLicenseDefaultLicenses_Object((1,3,6,1,4,1,9,9,369,1,3,4,1,10),_ClmLicenseDefaultLicenses_Type())
clmLicenseDefaultLicenses.setMaxAccess(_C)
if mibBuilder.loadTexts:clmLicenseDefaultLicenses.setStatus(_B)
_ClmFeatureUsageDetailsTable_Object=MibTable
clmFeatureUsageDetailsTable=_ClmFeatureUsageDetailsTable_Object((1,3,6,1,4,1,9,9,369,1,3,5))
if mibBuilder.loadTexts:clmFeatureUsageDetailsTable.setStatus(_B)
_ClmFeatureUsageDetailsEntry_Object=MibTableRow
clmFeatureUsageDetailsEntry=_ClmFeatureUsageDetailsEntry_Object((1,3,6,1,4,1,9,9,369,1,3,5,1))
clmFeatureUsageDetailsEntry.setIndexNames((0,_A,_a),(0,_A,_o))
if mibBuilder.loadTexts:clmFeatureUsageDetailsEntry.setStatus(_B)
_ClmLicensedAppIndex_Type=Unsigned32
_ClmLicensedAppIndex_Object=MibTableColumn
clmLicensedAppIndex=_ClmLicensedAppIndex_Object((1,3,6,1,4,1,9,9,369,1,3,5,1,1),_ClmLicensedAppIndex_Type())
clmLicensedAppIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:clmLicensedAppIndex.setStatus(_B)
class _ClmLicensedAppName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_ClmLicensedAppName_Type.__name__=_E
_ClmLicensedAppName_Object=MibTableColumn
clmLicensedAppName=_ClmLicensedAppName_Object((1,3,6,1,4,1,9,9,369,1,3,5,1,2),_ClmLicensedAppName_Type())
clmLicensedAppName.setMaxAccess(_C)
if mibBuilder.loadTexts:clmLicensedAppName.setStatus(_B)
_ClmLicenseViolationWarnFlag_Type=TruthValue
_ClmLicenseViolationWarnFlag_Object=MibScalar
clmLicenseViolationWarnFlag=_ClmLicenseViolationWarnFlag_Object((1,3,6,1,4,1,9,9,369,1,3,6),_ClmLicenseViolationWarnFlag_Type())
clmLicenseViolationWarnFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:clmLicenseViolationWarnFlag.setStatus(_B)
_ClmPortLicensingTable_Object=MibTable
clmPortLicensingTable=_ClmPortLicensingTable_Object((1,3,6,1,4,1,9,9,369,1,3,7))
if mibBuilder.loadTexts:clmPortLicensingTable.setStatus(_B)
_ClmPortLicensingEntry_Object=MibTableRow
clmPortLicensingEntry=_ClmPortLicensingEntry_Object((1,3,6,1,4,1,9,9,369,1,3,7,1))
clmPortLicensingEntry.setIndexNames((0,_g,_h),(0,_A,_b))
if mibBuilder.loadTexts:clmPortLicensingEntry.setStatus(_B)
_ClmPortLicensingType_Type=ClmLicenseType
_ClmPortLicensingType_Object=MibTableColumn
clmPortLicensingType=_ClmPortLicensingType_Object((1,3,6,1,4,1,9,9,369,1,3,7,1,1),_ClmPortLicensingType_Type())
clmPortLicensingType.setMaxAccess(_O)
if mibBuilder.loadTexts:clmPortLicensingType.setStatus(_B)
class _ClmPortLicensingConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('eligible',1),('inEligible',2),('acquire',3)))
_ClmPortLicensingConfig_Type.__name__=_D
_ClmPortLicensingConfig_Object=MibTableColumn
clmPortLicensingConfig=_ClmPortLicensingConfig_Object((1,3,6,1,4,1,9,9,369,1,3,7,1,2),_ClmPortLicensingConfig_Type())
clmPortLicensingConfig.setMaxAccess(_F)
if mibBuilder.loadTexts:clmPortLicensingConfig.setStatus(_B)
class _ClmPortLicensingOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notAcquired',1),('acquired',2)))
_ClmPortLicensingOper_Type.__name__=_D
_ClmPortLicensingOper_Object=MibTableColumn
clmPortLicensingOper=_ClmPortLicensingOper_Object((1,3,6,1,4,1,9,9,369,1,3,7,1,3),_ClmPortLicensingOper_Type())
clmPortLicensingOper.setMaxAccess(_C)
if mibBuilder.loadTexts:clmPortLicensingOper.setStatus(_B)
_ClmPortLicCountTable_Object=MibTable
clmPortLicCountTable=_ClmPortLicCountTable_Object((1,3,6,1,4,1,9,9,369,1,3,8))
if mibBuilder.loadTexts:clmPortLicCountTable.setStatus(_B)
_ClmPortLicCountEntry_Object=MibTableRow
clmPortLicCountEntry=_ClmPortLicCountEntry_Object((1,3,6,1,4,1,9,9,369,1,3,8,1))
clmPortLicCountEntry.setIndexNames((0,_A,_b))
if mibBuilder.loadTexts:clmPortLicCountEntry.setStatus(_B)
_ClmPortLicCountMax_Type=Unsigned32
_ClmPortLicCountMax_Object=MibTableColumn
clmPortLicCountMax=_ClmPortLicCountMax_Object((1,3,6,1,4,1,9,9,369,1,3,8,1,1),_ClmPortLicCountMax_Type())
clmPortLicCountMax.setMaxAccess(_C)
if mibBuilder.loadTexts:clmPortLicCountMax.setStatus(_B)
_ClmPortLicCountUsed_Type=Gauge32
_ClmPortLicCountUsed_Object=MibTableColumn
clmPortLicCountUsed=_ClmPortLicCountUsed_Object((1,3,6,1,4,1,9,9,369,1,3,8,1,2),_ClmPortLicCountUsed_Type())
clmPortLicCountUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:clmPortLicCountUsed.setStatus(_B)
if mibBuilder.loadTexts:clmPortLicCountUsed.setUnits(_p)
_ClmPortLicCountMaxInternal_Type=Unsigned32
_ClmPortLicCountMaxInternal_Object=MibTableColumn
clmPortLicCountMaxInternal=_ClmPortLicCountMaxInternal_Object((1,3,6,1,4,1,9,9,369,1,3,8,1,3),_ClmPortLicCountMaxInternal_Type())
clmPortLicCountMaxInternal.setMaxAccess(_C)
if mibBuilder.loadTexts:clmPortLicCountMaxInternal.setStatus(_B)
_ClmPortLicCountUsedInternal_Type=Gauge32
_ClmPortLicCountUsedInternal_Object=MibTableColumn
clmPortLicCountUsedInternal=_ClmPortLicCountUsedInternal_Object((1,3,6,1,4,1,9,9,369,1,3,8,1,4),_ClmPortLicCountUsedInternal_Type())
clmPortLicCountUsedInternal.setMaxAccess(_C)
if mibBuilder.loadTexts:clmPortLicCountUsedInternal.setStatus(_B)
if mibBuilder.loadTexts:clmPortLicCountUsedInternal.setUnits(_p)
_ClmLicenseFeatureStatus_ObjectIdentity=ObjectIdentity
clmLicenseFeatureStatus=_ClmLicenseFeatureStatus_ObjectIdentity((1,3,6,1,4,1,9,9,369,1,3,9))
_ClmMaxSslTransactions_Type=Integer32
_ClmMaxSslTransactions_Object=MibScalar
clmMaxSslTransactions=_ClmMaxSslTransactions_Object((1,3,6,1,4,1,9,9,369,1,3,9,1),_ClmMaxSslTransactions_Type())
clmMaxSslTransactions.setMaxAccess(_C)
if mibBuilder.loadTexts:clmMaxSslTransactions.setStatus(_B)
_ClmMaxVirtualizedContext_Type=Integer32
_ClmMaxVirtualizedContext_Object=MibScalar
clmMaxVirtualizedContext=_ClmMaxVirtualizedContext_Object((1,3,6,1,4,1,9,9,369,1,3,9,2),_ClmMaxVirtualizedContext_Type())
clmMaxVirtualizedContext.setMaxAccess(_C)
if mibBuilder.loadTexts:clmMaxVirtualizedContext.setStatus(_B)
_ClmModuleBandwidth_Type=Integer32
_ClmModuleBandwidth_Object=MibScalar
clmModuleBandwidth=_ClmModuleBandwidth_Object((1,3,6,1,4,1,9,9,369,1,3,9,3),_ClmModuleBandwidth_Type())
clmModuleBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:clmModuleBandwidth.setStatus(_B)
if mibBuilder.loadTexts:clmModuleBandwidth.setUnits('Gbps')
_ClmCompressionPerformance_Type=Integer32
_ClmCompressionPerformance_Object=MibScalar
clmCompressionPerformance=_ClmCompressionPerformance_Object((1,3,6,1,4,1,9,9,369,1,3,9,4),_ClmCompressionPerformance_Type())
clmCompressionPerformance.setMaxAccess(_C)
if mibBuilder.loadTexts:clmCompressionPerformance.setStatus(_B)
if mibBuilder.loadTexts:clmCompressionPerformance.setUnits('Mbps')
_ClmWebOptimization_Type=Integer32
_ClmWebOptimization_Object=MibScalar
clmWebOptimization=_ClmWebOptimization_Object((1,3,6,1,4,1,9,9,369,1,3,9,5),_ClmWebOptimization_Type())
clmWebOptimization.setMaxAccess(_C)
if mibBuilder.loadTexts:clmWebOptimization.setStatus(_B)
if mibBuilder.loadTexts:clmWebOptimization.setUnits('Cps')
_CiscoLicenseMgrMIBConform_ObjectIdentity=ObjectIdentity
ciscoLicenseMgrMIBConform=_CiscoLicenseMgrMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,369,2))
_CiscoLicenseMgrCompliances_ObjectIdentity=ObjectIdentity
ciscoLicenseMgrCompliances=_CiscoLicenseMgrCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,369,2,1))
_CiscoLicenseMgrGroups_ObjectIdentity=ObjectIdentity
ciscoLicenseMgrGroups=_CiscoLicenseMgrGroups_ObjectIdentity((1,3,6,1,4,1,9,9,369,2,2))
_CiscoLicenseMgrMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoLicenseMgrMIBNotifs=_CiscoLicenseMgrMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,369,3))
_CiscoLicenseMgrNotifications_ObjectIdentity=ObjectIdentity
ciscoLicenseMgrNotifications=_CiscoLicenseMgrNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,369,3,0))
clmLicenseInstallGroup=ObjectGroup((1,3,6,1,4,1,9,9,369,2,2,1))
clmLicenseInstallGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:clmLicenseInstallGroup.setStatus(_B)
clmNoOfInstalledLicensesGroup=ObjectGroup((1,3,6,1,4,1,9,9,369,2,2,2))
clmNoOfInstalledLicensesGroup.setObjects(*((_A,_w),(_A,_x)))
if mibBuilder.loadTexts:clmNoOfInstalledLicensesGroup.setStatus(_B)
clmLicenseInformationGroup=ObjectGroup((1,3,6,1,4,1,9,9,369,2,2,3))
clmLicenseInformationGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_M),(_A,_U),(_A,_H),(_A,_V)))
if mibBuilder.loadTexts:clmLicenseInformationGroup.setStatus(_G)
clmNotificationsEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,369,2,2,4))
clmNotificationsEnableGroup.setObjects((_A,_y))
if mibBuilder.loadTexts:clmNotificationsEnableGroup.setStatus(_B)
clmLicenseRequestGroup=ObjectGroup((1,3,6,1,4,1,9,9,369,2,2,6))
clmLicenseRequestGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:clmLicenseRequestGroup.setStatus(_B)
clmLicenseInformationGroup1=ObjectGroup((1,3,6,1,4,1,9,9,369,2,2,7))
clmLicenseInformationGroup1.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_M),(_A,_U),(_A,_H),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:clmLicenseInformationGroup1.setStatus(_G)
clmLicenseInformationGroup2=ObjectGroup((1,3,6,1,4,1,9,9,369,2,2,8))
clmLicenseInformationGroup2.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_M),(_A,_U),(_A,_H),(_A,_V),(_A,_W),(_A,_c)))
if mibBuilder.loadTexts:clmLicenseInformationGroup2.setStatus(_G)
clmLicenseInformationGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,369,2,2,9))
clmLicenseInformationGroupSup1.setObjects((_A,_A4))
if mibBuilder.loadTexts:clmLicenseInformationGroupSup1.setStatus(_B)
clmLicenseInformationGroup3=ObjectGroup((1,3,6,1,4,1,9,9,369,2,2,10))
clmLicenseInformationGroup3.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_M),(_A,_U),(_A,_H),(_A,_d),(_A,_W),(_A,_c)))
if mibBuilder.loadTexts:clmLicenseInformationGroup3.setStatus(_B)
clmLicenseInformationGroupSup2=ObjectGroup((1,3,6,1,4,1,9,9,369,2,2,11))
clmLicenseInformationGroupSup2.setObjects((_A,_A5))
if mibBuilder.loadTexts:clmLicenseInformationGroupSup2.setStatus(_B)
clmLicenseInformationPortLicGroup=ObjectGroup((1,3,6,1,4,1,9,9,369,2,2,12))
clmLicenseInformationPortLicGroup.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:clmLicenseInformationPortLicGroup.setStatus(_B)
clmLicenseFeatureStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,369,2,2,13))
clmLicenseFeatureStatusGroup.setObjects(*((_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:clmLicenseFeatureStatusGroup.setStatus(_B)
clmLicenseExpiryNotify=NotificationType((1,3,6,1,4,1,9,9,369,3,0,1))
clmLicenseExpiryNotify.setObjects((_A,_H))
if mibBuilder.loadTexts:clmLicenseExpiryNotify.setStatus(_B)
clmNoLicenseForFeatureNotify=NotificationType((1,3,6,1,4,1,9,9,369,3,0,2))
clmNoLicenseForFeatureNotify.setObjects((_A,_d))
if mibBuilder.loadTexts:clmNoLicenseForFeatureNotify.setStatus(_B)
clmLicenseFileMissingNotify=NotificationType((1,3,6,1,4,1,9,9,369,3,0,3))
clmLicenseFileMissingNotify.setObjects((_A,_M))
if mibBuilder.loadTexts:clmLicenseFileMissingNotify.setStatus(_B)
clmLicenseExpiryWarningNotify=NotificationType((1,3,6,1,4,1,9,9,369,3,0,4))
clmLicenseExpiryWarningNotify.setObjects((_A,_H))
if mibBuilder.loadTexts:clmLicenseExpiryWarningNotify.setStatus(_B)
clmNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,369,2,2,5))
clmNotificationGroup.setObjects(*((_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:clmNotificationGroup.setStatus(_B)
ciscoLicenseMgrCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,369,2,1,1))
ciscoLicenseMgrCompliance.setObjects(*((_A,_I),(_A,_J),(_A,_AL),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoLicenseMgrCompliance.setStatus(_G)
ciscoLicenseMgrCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,369,2,1,2))
ciscoLicenseMgrCompliance1.setObjects(*((_A,_I),(_A,_N),(_A,_J),(_A,_AM),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoLicenseMgrCompliance1.setStatus(_G)
ciscoLicenseMgrCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,369,2,1,3))
ciscoLicenseMgrCompliance2.setObjects(*((_A,_I),(_A,_N),(_A,_J),(_A,_AN),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoLicenseMgrCompliance2.setStatus(_G)
ciscoLicenseMgrCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,369,2,1,4))
ciscoLicenseMgrCompliance3.setObjects(*((_A,_I),(_A,_N),(_A,_J),(_A,_X),(_A,_K),(_A,_L),(_A,_Y)))
if mibBuilder.loadTexts:ciscoLicenseMgrCompliance3.setStatus(_G)
ciscoLicenseMgrCompliance4=ModuleCompliance((1,3,6,1,4,1,9,9,369,2,1,5))
ciscoLicenseMgrCompliance4.setObjects(*((_A,_I),(_A,_N),(_A,_J),(_A,_X),(_A,_K),(_A,_L),(_A,_e),(_A,_f),(_A,_Y)))
if mibBuilder.loadTexts:ciscoLicenseMgrCompliance4.setStatus(_G)
ciscoLicenseMgrCompliance5=ModuleCompliance((1,3,6,1,4,1,9,9,369,2,1,6))
ciscoLicenseMgrCompliance5.setObjects(*((_A,_I),(_A,_N),(_A,_J),(_A,_X),(_A,_K),(_A,_L),(_A,_e),(_A,_f),(_A,_AO),(_A,_Y)))
if mibBuilder.loadTexts:ciscoLicenseMgrCompliance5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ClmLicenseType':ClmLicenseType,'ciscoLicenseMgrMIB':ciscoLicenseMgrMIB,'ciscoLicenseMgrMIBObjects':ciscoLicenseMgrMIBObjects,'ciscoLicenseMgrConfig':ciscoLicenseMgrConfig,_q:clmHostId,_y:clmNotificationsEnable,'clmLicenseConfiguration':clmLicenseConfiguration,_r:clmLicenseConfigSpinLock,_s:clmLicenseFileURI,_t:clmLicenseFileTargetName,_u:clmLicenseConfigCommand,_v:clmLicenseConfigCommandStatus,_z:clmLicenseRequestSpinLock,_A0:clmLicenseRequestFeatureName,_A1:clmLicenseRequestAppName,_A2:clmLicenseRequestCommand,_A3:clmLicenseRequestCommandStatus,'clmLicenseInformation':clmLicenseInformation,_w:clmNoOfLicenseFilesInstalled,'clmLicenseFileContentsTable':clmLicenseFileContentsTable,'clmLicenseFileContentsEntry':clmLicenseFileContentsEntry,_l:clmLicenseFileName,_m:clmLicenseFileRowNumber,_P:clmLicenseFileTimeStamp,_Q:clmLicenseFileNoOfRows,_R:clmLicenseFileRowContents,_x:clmNoOfLicensedFeatures,'clmLicenseFeatureUsageTable':clmLicenseFeatureUsageTable,'clmLicenseFeatureUsageEntry':clmLicenseFeatureUsageEntry,_a:clmLicenseFeatureName,_S:clmLicenseFlag,_T:clmNoOfLicenseMaxUsages,_M:clmNoOfMissingUsageLicenses,_U:clmNoOfLicenseCurrentUsages,_H:clmLicenseExpiryDate,_V:clmLicenseGracePeriod,_A4:clmLicenseEnabled,_d:clmLicenseGracePeriodLeft,_A5:clmLicenseDefaultLicenses,'clmFeatureUsageDetailsTable':clmFeatureUsageDetailsTable,'clmFeatureUsageDetailsEntry':clmFeatureUsageDetailsEntry,_o:clmLicensedAppIndex,_W:clmLicensedAppName,_c:clmLicenseViolationWarnFlag,'clmPortLicensingTable':clmPortLicensingTable,'clmPortLicensingEntry':clmPortLicensingEntry,_b:clmPortLicensingType,_A6:clmPortLicensingConfig,_A7:clmPortLicensingOper,'clmPortLicCountTable':clmPortLicCountTable,'clmPortLicCountEntry':clmPortLicCountEntry,_A8:clmPortLicCountMax,_A9:clmPortLicCountUsed,_AA:clmPortLicCountMaxInternal,_AB:clmPortLicCountUsedInternal,'clmLicenseFeatureStatus':clmLicenseFeatureStatus,_AC:clmMaxSslTransactions,_AD:clmMaxVirtualizedContext,_AE:clmModuleBandwidth,_AF:clmCompressionPerformance,_AG:clmWebOptimization,'ciscoLicenseMgrMIBConform':ciscoLicenseMgrMIBConform,'ciscoLicenseMgrCompliances':ciscoLicenseMgrCompliances,'ciscoLicenseMgrCompliance':ciscoLicenseMgrCompliance,'ciscoLicenseMgrCompliance1':ciscoLicenseMgrCompliance1,'ciscoLicenseMgrCompliance2':ciscoLicenseMgrCompliance2,'ciscoLicenseMgrCompliance3':ciscoLicenseMgrCompliance3,'ciscoLicenseMgrCompliance4':ciscoLicenseMgrCompliance4,'ciscoLicenseMgrCompliance5':ciscoLicenseMgrCompliance5,'ciscoLicenseMgrGroups':ciscoLicenseMgrGroups,_I:clmLicenseInstallGroup,_J:clmNoOfInstalledLicensesGroup,_AL:clmLicenseInformationGroup,_K:clmNotificationsEnableGroup,_L:clmNotificationGroup,_N:clmLicenseRequestGroup,_AM:clmLicenseInformationGroup1,_AN:clmLicenseInformationGroup2,_Y:clmLicenseInformationGroupSup1,_X:clmLicenseInformationGroup3,_e:clmLicenseInformationGroupSup2,_f:clmLicenseInformationPortLicGroup,_AO:clmLicenseFeatureStatusGroup,'ciscoLicenseMgrMIBNotifs':ciscoLicenseMgrMIBNotifs,'ciscoLicenseMgrNotifications':ciscoLicenseMgrNotifications,_AH:clmLicenseExpiryNotify,_AI:clmNoLicenseForFeatureNotify,_AJ:clmLicenseFileMissingNotify,_AK:clmLicenseExpiryWarningNotify})