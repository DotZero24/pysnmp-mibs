_Ab='cienaWsSystemGroup'
_Aa='cwsSystemRootPassword'
_AZ='cwsSystemLampFlashTestPorts'
_AY='cwsSystemLampFlashTestTimeout'
_AX='cwsSystemLampFlashTestTargetType'
_AW='cwsSystemLampFlashTestMode'
_AV='cwsSystemLampFlashTestOperationalState'
_AU='cwsSystemLineConfigLineProtection'
_AT='cwsSystemLineConfigBandPlan'
_AS='cwsSystemFrontDisplayUserMessage'
_AR='cwsSystemFrontDisplayUserMessageState'
_AQ='cwsSystemFrontDisplayInputButtonState'
_AP='cwsSystemFrontDisplayScreensaverTimeout'
_AO='cwsSystemFrontDisplayScreensaverState'
_AN='cwsSystemFrontDisplayAdminState'
_AM='cwsSystemGlobalProvisioningChassisFunctionality'
_AL='cwsSystemGlobalProvisioningFcsErrorForwarding'
_AK='cwsSystemGlobalProvisioningResetToFactoryDefaultButton'
_AJ='cwsSystemGlobalProvisioningLampTest'
_AI='cwsSystemGlobalProvisioningLowPowerMode'
_AH='cwsSystemScpSecret'
_AG='cwsSystemScpPassword'
_AF='cwsSystemScpUserName'
_AE='cwsSystemScpHostName'
_AD='cwsSystemSftpSecret'
_AC='cwsSystemSftpPassword'
_AB='cwsSystemSftpUserName'
_AA='cwsSystemSftpHostName'
_A9='cwsSystemFtpSecret'
_A8='cwsSystemFtpPassword'
_A7='cwsSystemFtpUserName'
_A6='cwsSystemFtpHostName'
_A5='cwsSystemTftpCurrentHostName'
_A4='cwsSystemTftpDhcpHostName'
_A3='cwsSystemTftpConfigHostName'
_A2='cwsSystemXftpConfigMode'
_A1='cwsSystemDhcpAdminState'
_A0='cwsSystemServerConfigRestconfServerState'
_z='cwsSystemServerConfigNetconfServerState'
_y='cwsSystemServerConfigWebServerState'
_x='cwsSystemServerConfigSftpServerState'
_w='cwsSystemTimeConfigSystemUptime'
_v='cwsSystemTimeConfigCoordinatedUniversalTime'
_u='cwsSystemTimeConfigLocalDateTime'
_t='cwsSystemTimeConfigTimeStamp'
_s='cwsSystemTimeConfigTimeOffset'
_r='cwsSystemTimeConfigTime'
_q='cwsSystemTimeConfigDate'
_p='cwsSystemHostNameDhcpHostName'
_o='cwsSystemHostNameConfigHostName'
_n='cwsSystemHostNameCurrentHostName'
_m='cwsSystemMemberRackUnitNumber'
_l='cwsSystemMemberFrameIdentification'
_k='cwsSystemMemberDescription'
_j='cwsSystemMemberName'
_i='cwsSystemMemberId'
_h='cwsSystemGroupDescription'
_g='cwsSystemGroupName'
_f='cwsSystemGroupId'
_e='cwsSystemSiteAddress'
_d='cwsSystemSiteLongitude'
_c='cwsSystemSiteLatitude'
_b='cwsSystemSiteDescription'
_a='cwsSystemSiteName'
_Z='cwsSystemSiteId'
_Y='cwsSystemDhcpTableSnmpKey'
_X='cwsSystemScpTableSnmpKey'
_W='cwsSystemRootTableSnmpKey'
_V='cwsSystemLampFlashTestTableSnmpKey'
_U='cwsSystemLineConfigTableSnmpKey'
_T='cwsSystemFrontDisplayTableSnmpKey'
_S='cwsSystemGlobalProvisioningTableSnmpKey'
_R='cwsSystemSftpTableSnmpKey'
_Q='cwsSystemFtpTableSnmpKey'
_P='cwsSystemTftpTableSnmpKey'
_O='cwsSystemXftpConfigTableSnmpKey'
_N='cwsSystemServerConfigTableSnmpKey'
_M='cwsSystemTimeConfigTableSnmpKey'
_L='cwsSystemHostNameTableSnmpKey'
_K='cwsSystemMemberTableSnmpKey'
_J='cwsSystemGroupTableSnmpKey'
_I='cwsSystemSiteTableSnmpKey'
_H='obsolete'
_G='read-only'
_F='OctetString'
_E='not-accessible'
_D='Integer32'
_C='read-write'
_B='CIENA-WS-SYSTEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaWsConfig,=mibBuilder.importSymbols('CIENA-WS-MIB','cienaWsConfig')
EnabledDisabledEnum,StringMaxl128,StringMaxl16,StringMaxl256,StringMaxl32,StringMaxl64=mibBuilder.importSymbols('CIENA-WS-TYPEDEFS-MIB','EnabledDisabledEnum','StringMaxl128','StringMaxl16','StringMaxl256','StringMaxl32','StringMaxl64')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cienaWsSystemMIB=ModuleIdentity((1,3,6,1,4,1,1271,3,4,12))
if mibBuilder.loadTexts:cienaWsSystemMIB.setRevisions(('2017-07-26 00:00','2017-02-28 00:00','2016-12-12 00:00','2016-06-14 00:00','2016-04-06 00:00','2015-06-08 00:00'))
class BandplanEnum(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('none',0),('flex12',1),('fixed44',2),('fixed88',3),('fixed96',4)))
class Decimal32Len2(TextualConvention,Integer32):status=_A;displayHint='d-2';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-4320000,5040000))
class Decimal32Len5(TextualConvention,Integer32):status=_A;displayHint='d-5';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-18000000,18000000))
class LampModeEnum(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('flash',0))
class LampTargetTypeEnum(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chassis',1),('port',2)))
class LineProtectionEnum(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unprotected',0),('trunkOps',1)))
_CienaWsSystemObjects_ObjectIdentity=ObjectIdentity
cienaWsSystemObjects=_CienaWsSystemObjects_ObjectIdentity((1,3,6,1,4,1,1271,3,4,12,1))
_CienaWsSystemConformance_ObjectIdentity=ObjectIdentity
cienaWsSystemConformance=_CienaWsSystemConformance_ObjectIdentity((1,3,6,1,4,1,1271,3,4,12,2))
_CienaWsSystemGroups_ObjectIdentity=ObjectIdentity
cienaWsSystemGroups=_CienaWsSystemGroups_ObjectIdentity((1,3,6,1,4,1,1271,3,4,12,2,1))
_CienaWsSystemCompliances_ObjectIdentity=ObjectIdentity
cienaWsSystemCompliances=_CienaWsSystemCompliances_ObjectIdentity((1,3,6,1,4,1,1271,3,4,12,2,2))
_CwsSystemSiteTable_Object=MibTable
cwsSystemSiteTable=_CwsSystemSiteTable_Object((1,3,6,1,4,1,1271,3,4,12,3))
if mibBuilder.loadTexts:cwsSystemSiteTable.setStatus(_A)
_CwsSystemSiteEntry_Object=MibTableRow
cwsSystemSiteEntry=_CwsSystemSiteEntry_Object((1,3,6,1,4,1,1271,3,4,12,3,1))
cwsSystemSiteEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cwsSystemSiteEntry.setStatus(_A)
class _CwsSystemSiteTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemSiteTableSnmpKey_Type.__name__=_D
_CwsSystemSiteTableSnmpKey_Object=MibTableColumn
cwsSystemSiteTableSnmpKey=_CwsSystemSiteTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,3,1,1),_CwsSystemSiteTableSnmpKey_Type())
cwsSystemSiteTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemSiteTableSnmpKey.setStatus(_A)
_CwsSystemSiteId_Type=Unsigned32
_CwsSystemSiteId_Object=MibTableColumn
cwsSystemSiteId=_CwsSystemSiteId_Object((1,3,6,1,4,1,1271,3,4,12,3,1,2),_CwsSystemSiteId_Type())
cwsSystemSiteId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemSiteId.setStatus(_A)
class _CwsSystemSiteName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CwsSystemSiteName_Type.__name__=_F
_CwsSystemSiteName_Object=MibTableColumn
cwsSystemSiteName=_CwsSystemSiteName_Object((1,3,6,1,4,1,1271,3,4,12,3,1,3),_CwsSystemSiteName_Type())
cwsSystemSiteName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemSiteName.setStatus(_A)
class _CwsSystemSiteDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CwsSystemSiteDescription_Type.__name__=_F
_CwsSystemSiteDescription_Object=MibTableColumn
cwsSystemSiteDescription=_CwsSystemSiteDescription_Object((1,3,6,1,4,1,1271,3,4,12,3,1,4),_CwsSystemSiteDescription_Type())
cwsSystemSiteDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemSiteDescription.setStatus(_A)
_CwsSystemSiteLatitude_Type=Decimal32Len5
_CwsSystemSiteLatitude_Object=MibTableColumn
cwsSystemSiteLatitude=_CwsSystemSiteLatitude_Object((1,3,6,1,4,1,1271,3,4,12,3,1,5),_CwsSystemSiteLatitude_Type())
cwsSystemSiteLatitude.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemSiteLatitude.setStatus(_A)
_CwsSystemSiteLongitude_Type=Decimal32Len5
_CwsSystemSiteLongitude_Object=MibTableColumn
cwsSystemSiteLongitude=_CwsSystemSiteLongitude_Object((1,3,6,1,4,1,1271,3,4,12,3,1,6),_CwsSystemSiteLongitude_Type())
cwsSystemSiteLongitude.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemSiteLongitude.setStatus(_A)
class _CwsSystemSiteAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CwsSystemSiteAddress_Type.__name__=_F
_CwsSystemSiteAddress_Object=MibTableColumn
cwsSystemSiteAddress=_CwsSystemSiteAddress_Object((1,3,6,1,4,1,1271,3,4,12,3,1,7),_CwsSystemSiteAddress_Type())
cwsSystemSiteAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemSiteAddress.setStatus(_A)
_CwsSystemGroupTable_Object=MibTable
cwsSystemGroupTable=_CwsSystemGroupTable_Object((1,3,6,1,4,1,1271,3,4,12,4))
if mibBuilder.loadTexts:cwsSystemGroupTable.setStatus(_A)
_CwsSystemGroupEntry_Object=MibTableRow
cwsSystemGroupEntry=_CwsSystemGroupEntry_Object((1,3,6,1,4,1,1271,3,4,12,4,1))
cwsSystemGroupEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cwsSystemGroupEntry.setStatus(_A)
class _CwsSystemGroupTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemGroupTableSnmpKey_Type.__name__=_D
_CwsSystemGroupTableSnmpKey_Object=MibTableColumn
cwsSystemGroupTableSnmpKey=_CwsSystemGroupTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,4,1,1),_CwsSystemGroupTableSnmpKey_Type())
cwsSystemGroupTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemGroupTableSnmpKey.setStatus(_A)
_CwsSystemGroupId_Type=Unsigned32
_CwsSystemGroupId_Object=MibTableColumn
cwsSystemGroupId=_CwsSystemGroupId_Object((1,3,6,1,4,1,1271,3,4,12,4,1,2),_CwsSystemGroupId_Type())
cwsSystemGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemGroupId.setStatus(_A)
class _CwsSystemGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CwsSystemGroupName_Type.__name__=_F
_CwsSystemGroupName_Object=MibTableColumn
cwsSystemGroupName=_CwsSystemGroupName_Object((1,3,6,1,4,1,1271,3,4,12,4,1,3),_CwsSystemGroupName_Type())
cwsSystemGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemGroupName.setStatus(_A)
class _CwsSystemGroupDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CwsSystemGroupDescription_Type.__name__=_F
_CwsSystemGroupDescription_Object=MibTableColumn
cwsSystemGroupDescription=_CwsSystemGroupDescription_Object((1,3,6,1,4,1,1271,3,4,12,4,1,4),_CwsSystemGroupDescription_Type())
cwsSystemGroupDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemGroupDescription.setStatus(_A)
_CwsSystemMemberTable_Object=MibTable
cwsSystemMemberTable=_CwsSystemMemberTable_Object((1,3,6,1,4,1,1271,3,4,12,5))
if mibBuilder.loadTexts:cwsSystemMemberTable.setStatus(_A)
_CwsSystemMemberEntry_Object=MibTableRow
cwsSystemMemberEntry=_CwsSystemMemberEntry_Object((1,3,6,1,4,1,1271,3,4,12,5,1))
cwsSystemMemberEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:cwsSystemMemberEntry.setStatus(_A)
class _CwsSystemMemberTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemMemberTableSnmpKey_Type.__name__=_D
_CwsSystemMemberTableSnmpKey_Object=MibTableColumn
cwsSystemMemberTableSnmpKey=_CwsSystemMemberTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,5,1,1),_CwsSystemMemberTableSnmpKey_Type())
cwsSystemMemberTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemMemberTableSnmpKey.setStatus(_A)
_CwsSystemMemberId_Type=Unsigned32
_CwsSystemMemberId_Object=MibTableColumn
cwsSystemMemberId=_CwsSystemMemberId_Object((1,3,6,1,4,1,1271,3,4,12,5,1,2),_CwsSystemMemberId_Type())
cwsSystemMemberId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemMemberId.setStatus(_A)
class _CwsSystemMemberName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CwsSystemMemberName_Type.__name__=_F
_CwsSystemMemberName_Object=MibTableColumn
cwsSystemMemberName=_CwsSystemMemberName_Object((1,3,6,1,4,1,1271,3,4,12,5,1,3),_CwsSystemMemberName_Type())
cwsSystemMemberName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemMemberName.setStatus(_A)
class _CwsSystemMemberDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CwsSystemMemberDescription_Type.__name__=_F
_CwsSystemMemberDescription_Object=MibTableColumn
cwsSystemMemberDescription=_CwsSystemMemberDescription_Object((1,3,6,1,4,1,1271,3,4,12,5,1,4),_CwsSystemMemberDescription_Type())
cwsSystemMemberDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemMemberDescription.setStatus(_A)
class _CwsSystemMemberFrameIdentification_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CwsSystemMemberFrameIdentification_Type.__name__=_F
_CwsSystemMemberFrameIdentification_Object=MibTableColumn
cwsSystemMemberFrameIdentification=_CwsSystemMemberFrameIdentification_Object((1,3,6,1,4,1,1271,3,4,12,5,1,5),_CwsSystemMemberFrameIdentification_Type())
cwsSystemMemberFrameIdentification.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemMemberFrameIdentification.setStatus(_A)
_CwsSystemMemberRackUnitNumber_Type=Unsigned32
_CwsSystemMemberRackUnitNumber_Object=MibTableColumn
cwsSystemMemberRackUnitNumber=_CwsSystemMemberRackUnitNumber_Object((1,3,6,1,4,1,1271,3,4,12,5,1,6),_CwsSystemMemberRackUnitNumber_Type())
cwsSystemMemberRackUnitNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemMemberRackUnitNumber.setStatus(_A)
_CwsSystemHostNameTable_Object=MibTable
cwsSystemHostNameTable=_CwsSystemHostNameTable_Object((1,3,6,1,4,1,1271,3,4,12,6))
if mibBuilder.loadTexts:cwsSystemHostNameTable.setStatus(_A)
_CwsSystemHostNameEntry_Object=MibTableRow
cwsSystemHostNameEntry=_CwsSystemHostNameEntry_Object((1,3,6,1,4,1,1271,3,4,12,6,1))
cwsSystemHostNameEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:cwsSystemHostNameEntry.setStatus(_A)
class _CwsSystemHostNameTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemHostNameTableSnmpKey_Type.__name__=_D
_CwsSystemHostNameTableSnmpKey_Object=MibTableColumn
cwsSystemHostNameTableSnmpKey=_CwsSystemHostNameTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,6,1,1),_CwsSystemHostNameTableSnmpKey_Type())
cwsSystemHostNameTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemHostNameTableSnmpKey.setStatus(_A)
_CwsSystemHostNameCurrentHostName_Type=StringMaxl64
_CwsSystemHostNameCurrentHostName_Object=MibTableColumn
cwsSystemHostNameCurrentHostName=_CwsSystemHostNameCurrentHostName_Object((1,3,6,1,4,1,1271,3,4,12,6,1,2),_CwsSystemHostNameCurrentHostName_Type())
cwsSystemHostNameCurrentHostName.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsSystemHostNameCurrentHostName.setStatus(_A)
_CwsSystemHostNameConfigHostName_Type=StringMaxl64
_CwsSystemHostNameConfigHostName_Object=MibTableColumn
cwsSystemHostNameConfigHostName=_CwsSystemHostNameConfigHostName_Object((1,3,6,1,4,1,1271,3,4,12,6,1,3),_CwsSystemHostNameConfigHostName_Type())
cwsSystemHostNameConfigHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemHostNameConfigHostName.setStatus(_A)
_CwsSystemHostNameDhcpHostName_Type=StringMaxl64
_CwsSystemHostNameDhcpHostName_Object=MibTableColumn
cwsSystemHostNameDhcpHostName=_CwsSystemHostNameDhcpHostName_Object((1,3,6,1,4,1,1271,3,4,12,6,1,4),_CwsSystemHostNameDhcpHostName_Type())
cwsSystemHostNameDhcpHostName.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsSystemHostNameDhcpHostName.setStatus(_A)
_CwsSystemTimeConfigTable_Object=MibTable
cwsSystemTimeConfigTable=_CwsSystemTimeConfigTable_Object((1,3,6,1,4,1,1271,3,4,12,7))
if mibBuilder.loadTexts:cwsSystemTimeConfigTable.setStatus(_A)
_CwsSystemTimeConfigEntry_Object=MibTableRow
cwsSystemTimeConfigEntry=_CwsSystemTimeConfigEntry_Object((1,3,6,1,4,1,1271,3,4,12,7,1))
cwsSystemTimeConfigEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:cwsSystemTimeConfigEntry.setStatus(_A)
class _CwsSystemTimeConfigTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemTimeConfigTableSnmpKey_Type.__name__=_D
_CwsSystemTimeConfigTableSnmpKey_Object=MibTableColumn
cwsSystemTimeConfigTableSnmpKey=_CwsSystemTimeConfigTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,7,1,1),_CwsSystemTimeConfigTableSnmpKey_Type())
cwsSystemTimeConfigTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemTimeConfigTableSnmpKey.setStatus(_A)
class _CwsSystemTimeConfigDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,11))
_CwsSystemTimeConfigDate_Type.__name__=_F
_CwsSystemTimeConfigDate_Object=MibTableColumn
cwsSystemTimeConfigDate=_CwsSystemTimeConfigDate_Object((1,3,6,1,4,1,1271,3,4,12,7,1,2),_CwsSystemTimeConfigDate_Type())
cwsSystemTimeConfigDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemTimeConfigDate.setStatus(_A)
class _CwsSystemTimeConfigTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_CwsSystemTimeConfigTime_Type.__name__=_F
_CwsSystemTimeConfigTime_Object=MibTableColumn
cwsSystemTimeConfigTime=_CwsSystemTimeConfigTime_Object((1,3,6,1,4,1,1271,3,4,12,7,1,3),_CwsSystemTimeConfigTime_Type())
cwsSystemTimeConfigTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemTimeConfigTime.setStatus(_A)
_CwsSystemTimeConfigTimeOffset_Type=Decimal32Len2
_CwsSystemTimeConfigTimeOffset_Object=MibTableColumn
cwsSystemTimeConfigTimeOffset=_CwsSystemTimeConfigTimeOffset_Object((1,3,6,1,4,1,1271,3,4,12,7,1,4),_CwsSystemTimeConfigTimeOffset_Type())
cwsSystemTimeConfigTimeOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemTimeConfigTimeOffset.setStatus(_A)
class _CwsSystemTimeConfigTimeStamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('utc',0),('local',1)))
_CwsSystemTimeConfigTimeStamp_Type.__name__=_D
_CwsSystemTimeConfigTimeStamp_Object=MibTableColumn
cwsSystemTimeConfigTimeStamp=_CwsSystemTimeConfigTimeStamp_Object((1,3,6,1,4,1,1271,3,4,12,7,1,5),_CwsSystemTimeConfigTimeStamp_Type())
cwsSystemTimeConfigTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemTimeConfigTimeStamp.setStatus(_A)
class _CwsSystemTimeConfigLocalDateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,41))
_CwsSystemTimeConfigLocalDateTime_Type.__name__=_F
_CwsSystemTimeConfigLocalDateTime_Object=MibTableColumn
cwsSystemTimeConfigLocalDateTime=_CwsSystemTimeConfigLocalDateTime_Object((1,3,6,1,4,1,1271,3,4,12,7,1,6),_CwsSystemTimeConfigLocalDateTime_Type())
cwsSystemTimeConfigLocalDateTime.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsSystemTimeConfigLocalDateTime.setStatus(_A)
class _CwsSystemTimeConfigCoordinatedUniversalTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,41))
_CwsSystemTimeConfigCoordinatedUniversalTime_Type.__name__=_F
_CwsSystemTimeConfigCoordinatedUniversalTime_Object=MibTableColumn
cwsSystemTimeConfigCoordinatedUniversalTime=_CwsSystemTimeConfigCoordinatedUniversalTime_Object((1,3,6,1,4,1,1271,3,4,12,7,1,7),_CwsSystemTimeConfigCoordinatedUniversalTime_Type())
cwsSystemTimeConfigCoordinatedUniversalTime.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsSystemTimeConfigCoordinatedUniversalTime.setStatus(_A)
class _CwsSystemTimeConfigSystemUptime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,17))
_CwsSystemTimeConfigSystemUptime_Type.__name__=_F
_CwsSystemTimeConfigSystemUptime_Object=MibTableColumn
cwsSystemTimeConfigSystemUptime=_CwsSystemTimeConfigSystemUptime_Object((1,3,6,1,4,1,1271,3,4,12,7,1,8),_CwsSystemTimeConfigSystemUptime_Type())
cwsSystemTimeConfigSystemUptime.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsSystemTimeConfigSystemUptime.setStatus(_A)
_CwsSystemServerConfigTable_Object=MibTable
cwsSystemServerConfigTable=_CwsSystemServerConfigTable_Object((1,3,6,1,4,1,1271,3,4,12,8))
if mibBuilder.loadTexts:cwsSystemServerConfigTable.setStatus(_A)
_CwsSystemServerConfigEntry_Object=MibTableRow
cwsSystemServerConfigEntry=_CwsSystemServerConfigEntry_Object((1,3,6,1,4,1,1271,3,4,12,8,1))
cwsSystemServerConfigEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:cwsSystemServerConfigEntry.setStatus(_A)
class _CwsSystemServerConfigTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemServerConfigTableSnmpKey_Type.__name__=_D
_CwsSystemServerConfigTableSnmpKey_Object=MibTableColumn
cwsSystemServerConfigTableSnmpKey=_CwsSystemServerConfigTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,8,1,1),_CwsSystemServerConfigTableSnmpKey_Type())
cwsSystemServerConfigTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemServerConfigTableSnmpKey.setStatus(_A)
_CwsSystemServerConfigSftpServerState_Type=EnabledDisabledEnum
_CwsSystemServerConfigSftpServerState_Object=MibTableColumn
cwsSystemServerConfigSftpServerState=_CwsSystemServerConfigSftpServerState_Object((1,3,6,1,4,1,1271,3,4,12,8,1,2),_CwsSystemServerConfigSftpServerState_Type())
cwsSystemServerConfigSftpServerState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemServerConfigSftpServerState.setStatus(_A)
_CwsSystemServerConfigWebServerState_Type=EnabledDisabledEnum
_CwsSystemServerConfigWebServerState_Object=MibTableColumn
cwsSystemServerConfigWebServerState=_CwsSystemServerConfigWebServerState_Object((1,3,6,1,4,1,1271,3,4,12,8,1,3),_CwsSystemServerConfigWebServerState_Type())
cwsSystemServerConfigWebServerState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemServerConfigWebServerState.setStatus(_A)
_CwsSystemServerConfigNetconfServerState_Type=EnabledDisabledEnum
_CwsSystemServerConfigNetconfServerState_Object=MibTableColumn
cwsSystemServerConfigNetconfServerState=_CwsSystemServerConfigNetconfServerState_Object((1,3,6,1,4,1,1271,3,4,12,8,1,4),_CwsSystemServerConfigNetconfServerState_Type())
cwsSystemServerConfigNetconfServerState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemServerConfigNetconfServerState.setStatus(_A)
_CwsSystemServerConfigRestconfServerState_Type=EnabledDisabledEnum
_CwsSystemServerConfigRestconfServerState_Object=MibTableColumn
cwsSystemServerConfigRestconfServerState=_CwsSystemServerConfigRestconfServerState_Object((1,3,6,1,4,1,1271,3,4,12,8,1,5),_CwsSystemServerConfigRestconfServerState_Type())
cwsSystemServerConfigRestconfServerState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemServerConfigRestconfServerState.setStatus(_A)
_CwsSystemXftpConfigTable_Object=MibTable
cwsSystemXftpConfigTable=_CwsSystemXftpConfigTable_Object((1,3,6,1,4,1,1271,3,4,12,9))
if mibBuilder.loadTexts:cwsSystemXftpConfigTable.setStatus(_A)
_CwsSystemXftpConfigEntry_Object=MibTableRow
cwsSystemXftpConfigEntry=_CwsSystemXftpConfigEntry_Object((1,3,6,1,4,1,1271,3,4,12,9,1))
cwsSystemXftpConfigEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:cwsSystemXftpConfigEntry.setStatus(_A)
class _CwsSystemXftpConfigTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemXftpConfigTableSnmpKey_Type.__name__=_D
_CwsSystemXftpConfigTableSnmpKey_Object=MibTableColumn
cwsSystemXftpConfigTableSnmpKey=_CwsSystemXftpConfigTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,9,1,1),_CwsSystemXftpConfigTableSnmpKey_Type())
cwsSystemXftpConfigTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemXftpConfigTableSnmpKey.setStatus(_A)
class _CwsSystemXftpConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('none',0),('tftp',1),('ftp',2),('sftp',3),('scp',4)))
_CwsSystemXftpConfigMode_Type.__name__=_D
_CwsSystemXftpConfigMode_Object=MibTableColumn
cwsSystemXftpConfigMode=_CwsSystemXftpConfigMode_Object((1,3,6,1,4,1,1271,3,4,12,9,1,2),_CwsSystemXftpConfigMode_Type())
cwsSystemXftpConfigMode.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsSystemXftpConfigMode.setStatus(_A)
_CwsSystemTftpTable_Object=MibTable
cwsSystemTftpTable=_CwsSystemTftpTable_Object((1,3,6,1,4,1,1271,3,4,12,10))
if mibBuilder.loadTexts:cwsSystemTftpTable.setStatus(_A)
_CwsSystemTftpEntry_Object=MibTableRow
cwsSystemTftpEntry=_CwsSystemTftpEntry_Object((1,3,6,1,4,1,1271,3,4,12,10,1))
cwsSystemTftpEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:cwsSystemTftpEntry.setStatus(_A)
class _CwsSystemTftpTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemTftpTableSnmpKey_Type.__name__=_D
_CwsSystemTftpTableSnmpKey_Object=MibTableColumn
cwsSystemTftpTableSnmpKey=_CwsSystemTftpTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,10,1,1),_CwsSystemTftpTableSnmpKey_Type())
cwsSystemTftpTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemTftpTableSnmpKey.setStatus(_A)
_CwsSystemTftpConfigHostName_Type=StringMaxl64
_CwsSystemTftpConfigHostName_Object=MibTableColumn
cwsSystemTftpConfigHostName=_CwsSystemTftpConfigHostName_Object((1,3,6,1,4,1,1271,3,4,12,10,1,2),_CwsSystemTftpConfigHostName_Type())
cwsSystemTftpConfigHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemTftpConfigHostName.setStatus(_A)
_CwsSystemTftpDhcpHostName_Type=StringMaxl64
_CwsSystemTftpDhcpHostName_Object=MibTableColumn
cwsSystemTftpDhcpHostName=_CwsSystemTftpDhcpHostName_Object((1,3,6,1,4,1,1271,3,4,12,10,1,3),_CwsSystemTftpDhcpHostName_Type())
cwsSystemTftpDhcpHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemTftpDhcpHostName.setStatus(_A)
_CwsSystemTftpCurrentHostName_Type=StringMaxl64
_CwsSystemTftpCurrentHostName_Object=MibTableColumn
cwsSystemTftpCurrentHostName=_CwsSystemTftpCurrentHostName_Object((1,3,6,1,4,1,1271,3,4,12,10,1,4),_CwsSystemTftpCurrentHostName_Type())
cwsSystemTftpCurrentHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemTftpCurrentHostName.setStatus(_A)
_CwsSystemFtpTable_Object=MibTable
cwsSystemFtpTable=_CwsSystemFtpTable_Object((1,3,6,1,4,1,1271,3,4,12,11))
if mibBuilder.loadTexts:cwsSystemFtpTable.setStatus(_A)
_CwsSystemFtpEntry_Object=MibTableRow
cwsSystemFtpEntry=_CwsSystemFtpEntry_Object((1,3,6,1,4,1,1271,3,4,12,11,1))
cwsSystemFtpEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:cwsSystemFtpEntry.setStatus(_A)
class _CwsSystemFtpTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemFtpTableSnmpKey_Type.__name__=_D
_CwsSystemFtpTableSnmpKey_Object=MibTableColumn
cwsSystemFtpTableSnmpKey=_CwsSystemFtpTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,11,1,1),_CwsSystemFtpTableSnmpKey_Type())
cwsSystemFtpTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemFtpTableSnmpKey.setStatus(_A)
_CwsSystemFtpHostName_Type=StringMaxl64
_CwsSystemFtpHostName_Object=MibTableColumn
cwsSystemFtpHostName=_CwsSystemFtpHostName_Object((1,3,6,1,4,1,1271,3,4,12,11,1,2),_CwsSystemFtpHostName_Type())
cwsSystemFtpHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemFtpHostName.setStatus(_A)
_CwsSystemFtpUserName_Type=StringMaxl32
_CwsSystemFtpUserName_Object=MibTableColumn
cwsSystemFtpUserName=_CwsSystemFtpUserName_Object((1,3,6,1,4,1,1271,3,4,12,11,1,3),_CwsSystemFtpUserName_Type())
cwsSystemFtpUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemFtpUserName.setStatus(_A)
_CwsSystemFtpPassword_Type=StringMaxl128
_CwsSystemFtpPassword_Object=MibTableColumn
cwsSystemFtpPassword=_CwsSystemFtpPassword_Object((1,3,6,1,4,1,1271,3,4,12,11,1,4),_CwsSystemFtpPassword_Type())
cwsSystemFtpPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemFtpPassword.setStatus(_A)
_CwsSystemFtpSecret_Type=StringMaxl256
_CwsSystemFtpSecret_Object=MibTableColumn
cwsSystemFtpSecret=_CwsSystemFtpSecret_Object((1,3,6,1,4,1,1271,3,4,12,11,1,5),_CwsSystemFtpSecret_Type())
cwsSystemFtpSecret.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemFtpSecret.setStatus(_A)
_CwsSystemSftpTable_Object=MibTable
cwsSystemSftpTable=_CwsSystemSftpTable_Object((1,3,6,1,4,1,1271,3,4,12,12))
if mibBuilder.loadTexts:cwsSystemSftpTable.setStatus(_A)
_CwsSystemSftpEntry_Object=MibTableRow
cwsSystemSftpEntry=_CwsSystemSftpEntry_Object((1,3,6,1,4,1,1271,3,4,12,12,1))
cwsSystemSftpEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:cwsSystemSftpEntry.setStatus(_A)
class _CwsSystemSftpTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemSftpTableSnmpKey_Type.__name__=_D
_CwsSystemSftpTableSnmpKey_Object=MibTableColumn
cwsSystemSftpTableSnmpKey=_CwsSystemSftpTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,12,1,1),_CwsSystemSftpTableSnmpKey_Type())
cwsSystemSftpTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemSftpTableSnmpKey.setStatus(_A)
_CwsSystemSftpHostName_Type=StringMaxl64
_CwsSystemSftpHostName_Object=MibTableColumn
cwsSystemSftpHostName=_CwsSystemSftpHostName_Object((1,3,6,1,4,1,1271,3,4,12,12,1,2),_CwsSystemSftpHostName_Type())
cwsSystemSftpHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemSftpHostName.setStatus(_A)
_CwsSystemSftpUserName_Type=StringMaxl32
_CwsSystemSftpUserName_Object=MibTableColumn
cwsSystemSftpUserName=_CwsSystemSftpUserName_Object((1,3,6,1,4,1,1271,3,4,12,12,1,3),_CwsSystemSftpUserName_Type())
cwsSystemSftpUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemSftpUserName.setStatus(_A)
_CwsSystemSftpPassword_Type=StringMaxl128
_CwsSystemSftpPassword_Object=MibTableColumn
cwsSystemSftpPassword=_CwsSystemSftpPassword_Object((1,3,6,1,4,1,1271,3,4,12,12,1,4),_CwsSystemSftpPassword_Type())
cwsSystemSftpPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemSftpPassword.setStatus(_A)
_CwsSystemSftpSecret_Type=StringMaxl256
_CwsSystemSftpSecret_Object=MibTableColumn
cwsSystemSftpSecret=_CwsSystemSftpSecret_Object((1,3,6,1,4,1,1271,3,4,12,12,1,5),_CwsSystemSftpSecret_Type())
cwsSystemSftpSecret.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemSftpSecret.setStatus(_A)
_CwsSystemGlobalProvisioningTable_Object=MibTable
cwsSystemGlobalProvisioningTable=_CwsSystemGlobalProvisioningTable_Object((1,3,6,1,4,1,1271,3,4,12,13))
if mibBuilder.loadTexts:cwsSystemGlobalProvisioningTable.setStatus(_A)
_CwsSystemGlobalProvisioningEntry_Object=MibTableRow
cwsSystemGlobalProvisioningEntry=_CwsSystemGlobalProvisioningEntry_Object((1,3,6,1,4,1,1271,3,4,12,13,1))
cwsSystemGlobalProvisioningEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:cwsSystemGlobalProvisioningEntry.setStatus(_A)
class _CwsSystemGlobalProvisioningTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemGlobalProvisioningTableSnmpKey_Type.__name__=_D
_CwsSystemGlobalProvisioningTableSnmpKey_Object=MibTableColumn
cwsSystemGlobalProvisioningTableSnmpKey=_CwsSystemGlobalProvisioningTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,13,1,1),_CwsSystemGlobalProvisioningTableSnmpKey_Type())
cwsSystemGlobalProvisioningTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemGlobalProvisioningTableSnmpKey.setStatus(_A)
_CwsSystemGlobalProvisioningLowPowerMode_Type=EnabledDisabledEnum
_CwsSystemGlobalProvisioningLowPowerMode_Object=MibTableColumn
cwsSystemGlobalProvisioningLowPowerMode=_CwsSystemGlobalProvisioningLowPowerMode_Object((1,3,6,1,4,1,1271,3,4,12,13,1,2),_CwsSystemGlobalProvisioningLowPowerMode_Type())
cwsSystemGlobalProvisioningLowPowerMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemGlobalProvisioningLowPowerMode.setStatus(_A)
_CwsSystemGlobalProvisioningLampTest_Type=EnabledDisabledEnum
_CwsSystemGlobalProvisioningLampTest_Object=MibTableColumn
cwsSystemGlobalProvisioningLampTest=_CwsSystemGlobalProvisioningLampTest_Object((1,3,6,1,4,1,1271,3,4,12,13,1,3),_CwsSystemGlobalProvisioningLampTest_Type())
cwsSystemGlobalProvisioningLampTest.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemGlobalProvisioningLampTest.setStatus(_H)
_CwsSystemGlobalProvisioningResetToFactoryDefaultButton_Type=EnabledDisabledEnum
_CwsSystemGlobalProvisioningResetToFactoryDefaultButton_Object=MibTableColumn
cwsSystemGlobalProvisioningResetToFactoryDefaultButton=_CwsSystemGlobalProvisioningResetToFactoryDefaultButton_Object((1,3,6,1,4,1,1271,3,4,12,13,1,4),_CwsSystemGlobalProvisioningResetToFactoryDefaultButton_Type())
cwsSystemGlobalProvisioningResetToFactoryDefaultButton.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemGlobalProvisioningResetToFactoryDefaultButton.setStatus(_H)
_CwsSystemGlobalProvisioningFcsErrorForwarding_Type=TruthValue
_CwsSystemGlobalProvisioningFcsErrorForwarding_Object=MibTableColumn
cwsSystemGlobalProvisioningFcsErrorForwarding=_CwsSystemGlobalProvisioningFcsErrorForwarding_Object((1,3,6,1,4,1,1271,3,4,12,13,1,5),_CwsSystemGlobalProvisioningFcsErrorForwarding_Type())
cwsSystemGlobalProvisioningFcsErrorForwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemGlobalProvisioningFcsErrorForwarding.setStatus(_A)
_CwsSystemGlobalProvisioningChassisFunctionality_Type=StringMaxl16
_CwsSystemGlobalProvisioningChassisFunctionality_Object=MibTableColumn
cwsSystemGlobalProvisioningChassisFunctionality=_CwsSystemGlobalProvisioningChassisFunctionality_Object((1,3,6,1,4,1,1271,3,4,12,13,1,6),_CwsSystemGlobalProvisioningChassisFunctionality_Type())
cwsSystemGlobalProvisioningChassisFunctionality.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemGlobalProvisioningChassisFunctionality.setStatus(_A)
_CwsSystemFrontDisplayTable_Object=MibTable
cwsSystemFrontDisplayTable=_CwsSystemFrontDisplayTable_Object((1,3,6,1,4,1,1271,3,4,12,14))
if mibBuilder.loadTexts:cwsSystemFrontDisplayTable.setStatus(_A)
_CwsSystemFrontDisplayEntry_Object=MibTableRow
cwsSystemFrontDisplayEntry=_CwsSystemFrontDisplayEntry_Object((1,3,6,1,4,1,1271,3,4,12,14,1))
cwsSystemFrontDisplayEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:cwsSystemFrontDisplayEntry.setStatus(_A)
class _CwsSystemFrontDisplayTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemFrontDisplayTableSnmpKey_Type.__name__=_D
_CwsSystemFrontDisplayTableSnmpKey_Object=MibTableColumn
cwsSystemFrontDisplayTableSnmpKey=_CwsSystemFrontDisplayTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,14,1,1),_CwsSystemFrontDisplayTableSnmpKey_Type())
cwsSystemFrontDisplayTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemFrontDisplayTableSnmpKey.setStatus(_A)
_CwsSystemFrontDisplayAdminState_Type=EnabledDisabledEnum
_CwsSystemFrontDisplayAdminState_Object=MibTableColumn
cwsSystemFrontDisplayAdminState=_CwsSystemFrontDisplayAdminState_Object((1,3,6,1,4,1,1271,3,4,12,14,1,2),_CwsSystemFrontDisplayAdminState_Type())
cwsSystemFrontDisplayAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemFrontDisplayAdminState.setStatus(_A)
_CwsSystemFrontDisplayScreensaverState_Type=EnabledDisabledEnum
_CwsSystemFrontDisplayScreensaverState_Object=MibTableColumn
cwsSystemFrontDisplayScreensaverState=_CwsSystemFrontDisplayScreensaverState_Object((1,3,6,1,4,1,1271,3,4,12,14,1,3),_CwsSystemFrontDisplayScreensaverState_Type())
cwsSystemFrontDisplayScreensaverState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemFrontDisplayScreensaverState.setStatus(_A)
_CwsSystemFrontDisplayScreensaverTimeout_Type=Unsigned32
_CwsSystemFrontDisplayScreensaverTimeout_Object=MibTableColumn
cwsSystemFrontDisplayScreensaverTimeout=_CwsSystemFrontDisplayScreensaverTimeout_Object((1,3,6,1,4,1,1271,3,4,12,14,1,4),_CwsSystemFrontDisplayScreensaverTimeout_Type())
cwsSystemFrontDisplayScreensaverTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemFrontDisplayScreensaverTimeout.setStatus(_A)
_CwsSystemFrontDisplayInputButtonState_Type=EnabledDisabledEnum
_CwsSystemFrontDisplayInputButtonState_Object=MibTableColumn
cwsSystemFrontDisplayInputButtonState=_CwsSystemFrontDisplayInputButtonState_Object((1,3,6,1,4,1,1271,3,4,12,14,1,5),_CwsSystemFrontDisplayInputButtonState_Type())
cwsSystemFrontDisplayInputButtonState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemFrontDisplayInputButtonState.setStatus(_A)
_CwsSystemFrontDisplayUserMessageState_Type=EnabledDisabledEnum
_CwsSystemFrontDisplayUserMessageState_Object=MibTableColumn
cwsSystemFrontDisplayUserMessageState=_CwsSystemFrontDisplayUserMessageState_Object((1,3,6,1,4,1,1271,3,4,12,14,1,6),_CwsSystemFrontDisplayUserMessageState_Type())
cwsSystemFrontDisplayUserMessageState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemFrontDisplayUserMessageState.setStatus(_H)
class _CwsSystemFrontDisplayUserMessage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,144))
_CwsSystemFrontDisplayUserMessage_Type.__name__=_F
_CwsSystemFrontDisplayUserMessage_Object=MibTableColumn
cwsSystemFrontDisplayUserMessage=_CwsSystemFrontDisplayUserMessage_Object((1,3,6,1,4,1,1271,3,4,12,14,1,7),_CwsSystemFrontDisplayUserMessage_Type())
cwsSystemFrontDisplayUserMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemFrontDisplayUserMessage.setStatus(_A)
_CwsSystemLineConfigTable_Object=MibTable
cwsSystemLineConfigTable=_CwsSystemLineConfigTable_Object((1,3,6,1,4,1,1271,3,4,12,15))
if mibBuilder.loadTexts:cwsSystemLineConfigTable.setStatus(_A)
_CwsSystemLineConfigEntry_Object=MibTableRow
cwsSystemLineConfigEntry=_CwsSystemLineConfigEntry_Object((1,3,6,1,4,1,1271,3,4,12,15,1))
cwsSystemLineConfigEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:cwsSystemLineConfigEntry.setStatus(_A)
class _CwsSystemLineConfigTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemLineConfigTableSnmpKey_Type.__name__=_D
_CwsSystemLineConfigTableSnmpKey_Object=MibTableColumn
cwsSystemLineConfigTableSnmpKey=_CwsSystemLineConfigTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,15,1,1),_CwsSystemLineConfigTableSnmpKey_Type())
cwsSystemLineConfigTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemLineConfigTableSnmpKey.setStatus(_A)
_CwsSystemLineConfigBandPlan_Type=BandplanEnum
_CwsSystemLineConfigBandPlan_Object=MibTableColumn
cwsSystemLineConfigBandPlan=_CwsSystemLineConfigBandPlan_Object((1,3,6,1,4,1,1271,3,4,12,15,1,2),_CwsSystemLineConfigBandPlan_Type())
cwsSystemLineConfigBandPlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemLineConfigBandPlan.setStatus(_A)
_CwsSystemLineConfigLineProtection_Type=LineProtectionEnum
_CwsSystemLineConfigLineProtection_Object=MibTableColumn
cwsSystemLineConfigLineProtection=_CwsSystemLineConfigLineProtection_Object((1,3,6,1,4,1,1271,3,4,12,15,1,3),_CwsSystemLineConfigLineProtection_Type())
cwsSystemLineConfigLineProtection.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemLineConfigLineProtection.setStatus(_A)
_CwsSystemLampFlashTestTable_Object=MibTable
cwsSystemLampFlashTestTable=_CwsSystemLampFlashTestTable_Object((1,3,6,1,4,1,1271,3,4,12,16))
if mibBuilder.loadTexts:cwsSystemLampFlashTestTable.setStatus(_A)
_CwsSystemLampFlashTestEntry_Object=MibTableRow
cwsSystemLampFlashTestEntry=_CwsSystemLampFlashTestEntry_Object((1,3,6,1,4,1,1271,3,4,12,16,1))
cwsSystemLampFlashTestEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:cwsSystemLampFlashTestEntry.setStatus(_A)
class _CwsSystemLampFlashTestTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemLampFlashTestTableSnmpKey_Type.__name__=_D
_CwsSystemLampFlashTestTableSnmpKey_Object=MibTableColumn
cwsSystemLampFlashTestTableSnmpKey=_CwsSystemLampFlashTestTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,16,1,1),_CwsSystemLampFlashTestTableSnmpKey_Type())
cwsSystemLampFlashTestTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemLampFlashTestTableSnmpKey.setStatus(_A)
_CwsSystemLampFlashTestOperationalState_Type=EnabledDisabledEnum
_CwsSystemLampFlashTestOperationalState_Object=MibTableColumn
cwsSystemLampFlashTestOperationalState=_CwsSystemLampFlashTestOperationalState_Object((1,3,6,1,4,1,1271,3,4,12,16,1,2),_CwsSystemLampFlashTestOperationalState_Type())
cwsSystemLampFlashTestOperationalState.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsSystemLampFlashTestOperationalState.setStatus(_A)
_CwsSystemLampFlashTestMode_Type=LampModeEnum
_CwsSystemLampFlashTestMode_Object=MibTableColumn
cwsSystemLampFlashTestMode=_CwsSystemLampFlashTestMode_Object((1,3,6,1,4,1,1271,3,4,12,16,1,3),_CwsSystemLampFlashTestMode_Type())
cwsSystemLampFlashTestMode.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsSystemLampFlashTestMode.setStatus(_A)
_CwsSystemLampFlashTestTargetType_Type=LampTargetTypeEnum
_CwsSystemLampFlashTestTargetType_Object=MibTableColumn
cwsSystemLampFlashTestTargetType=_CwsSystemLampFlashTestTargetType_Object((1,3,6,1,4,1,1271,3,4,12,16,1,4),_CwsSystemLampFlashTestTargetType_Type())
cwsSystemLampFlashTestTargetType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemLampFlashTestTargetType.setStatus(_A)
_CwsSystemLampFlashTestTimeout_Type=Unsigned32
_CwsSystemLampFlashTestTimeout_Object=MibTableColumn
cwsSystemLampFlashTestTimeout=_CwsSystemLampFlashTestTimeout_Object((1,3,6,1,4,1,1271,3,4,12,16,1,5),_CwsSystemLampFlashTestTimeout_Type())
cwsSystemLampFlashTestTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemLampFlashTestTimeout.setStatus(_A)
class _CwsSystemLampFlashTestPorts_Type(Bits):namedValues=NamedValues(*(('port1',0),('port2',1),('port3',2),('port4',3),('port5',4),('port6',5),('port7',6),('port8',7),('port9',8),('port10',9),('port11',10),('port12',11)))
_CwsSystemLampFlashTestPorts_Type.__name__='Bits'
_CwsSystemLampFlashTestPorts_Object=MibTableColumn
cwsSystemLampFlashTestPorts=_CwsSystemLampFlashTestPorts_Object((1,3,6,1,4,1,1271,3,4,12,16,1,6),_CwsSystemLampFlashTestPorts_Type())
cwsSystemLampFlashTestPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemLampFlashTestPorts.setStatus(_A)
_CwsSystemRootTable_Object=MibTable
cwsSystemRootTable=_CwsSystemRootTable_Object((1,3,6,1,4,1,1271,3,4,12,18))
if mibBuilder.loadTexts:cwsSystemRootTable.setStatus(_A)
_CwsSystemRootEntry_Object=MibTableRow
cwsSystemRootEntry=_CwsSystemRootEntry_Object((1,3,6,1,4,1,1271,3,4,12,18,1))
cwsSystemRootEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:cwsSystemRootEntry.setStatus(_A)
class _CwsSystemRootTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemRootTableSnmpKey_Type.__name__=_D
_CwsSystemRootTableSnmpKey_Object=MibTableColumn
cwsSystemRootTableSnmpKey=_CwsSystemRootTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,18,1,1),_CwsSystemRootTableSnmpKey_Type())
cwsSystemRootTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemRootTableSnmpKey.setStatus(_A)
_CwsSystemRootPassword_Type=StringMaxl128
_CwsSystemRootPassword_Object=MibTableColumn
cwsSystemRootPassword=_CwsSystemRootPassword_Object((1,3,6,1,4,1,1271,3,4,12,18,1,2),_CwsSystemRootPassword_Type())
cwsSystemRootPassword.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsSystemRootPassword.setStatus(_A)
_CwsSystemScpTable_Object=MibTable
cwsSystemScpTable=_CwsSystemScpTable_Object((1,3,6,1,4,1,1271,3,4,12,19))
if mibBuilder.loadTexts:cwsSystemScpTable.setStatus(_A)
_CwsSystemScpEntry_Object=MibTableRow
cwsSystemScpEntry=_CwsSystemScpEntry_Object((1,3,6,1,4,1,1271,3,4,12,19,1))
cwsSystemScpEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:cwsSystemScpEntry.setStatus(_A)
class _CwsSystemScpTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemScpTableSnmpKey_Type.__name__=_D
_CwsSystemScpTableSnmpKey_Object=MibTableColumn
cwsSystemScpTableSnmpKey=_CwsSystemScpTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,19,1,1),_CwsSystemScpTableSnmpKey_Type())
cwsSystemScpTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemScpTableSnmpKey.setStatus(_A)
_CwsSystemScpHostName_Type=StringMaxl64
_CwsSystemScpHostName_Object=MibTableColumn
cwsSystemScpHostName=_CwsSystemScpHostName_Object((1,3,6,1,4,1,1271,3,4,12,19,1,2),_CwsSystemScpHostName_Type())
cwsSystemScpHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemScpHostName.setStatus(_A)
_CwsSystemScpUserName_Type=StringMaxl32
_CwsSystemScpUserName_Object=MibTableColumn
cwsSystemScpUserName=_CwsSystemScpUserName_Object((1,3,6,1,4,1,1271,3,4,12,19,1,3),_CwsSystemScpUserName_Type())
cwsSystemScpUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemScpUserName.setStatus(_A)
_CwsSystemScpPassword_Type=StringMaxl128
_CwsSystemScpPassword_Object=MibTableColumn
cwsSystemScpPassword=_CwsSystemScpPassword_Object((1,3,6,1,4,1,1271,3,4,12,19,1,4),_CwsSystemScpPassword_Type())
cwsSystemScpPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemScpPassword.setStatus(_A)
_CwsSystemScpSecret_Type=StringMaxl256
_CwsSystemScpSecret_Object=MibTableColumn
cwsSystemScpSecret=_CwsSystemScpSecret_Object((1,3,6,1,4,1,1271,3,4,12,19,1,5),_CwsSystemScpSecret_Type())
cwsSystemScpSecret.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSystemScpSecret.setStatus(_A)
_CwsSystemDhcpTable_Object=MibTable
cwsSystemDhcpTable=_CwsSystemDhcpTable_Object((1,3,6,1,4,1,1271,3,4,12,21))
if mibBuilder.loadTexts:cwsSystemDhcpTable.setStatus(_A)
_CwsSystemDhcpEntry_Object=MibTableRow
cwsSystemDhcpEntry=_CwsSystemDhcpEntry_Object((1,3,6,1,4,1,1271,3,4,12,21,1))
cwsSystemDhcpEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:cwsSystemDhcpEntry.setStatus(_A)
class _CwsSystemDhcpTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSystemDhcpTableSnmpKey_Type.__name__=_D
_CwsSystemDhcpTableSnmpKey_Object=MibTableColumn
cwsSystemDhcpTableSnmpKey=_CwsSystemDhcpTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,12,21,1,1),_CwsSystemDhcpTableSnmpKey_Type())
cwsSystemDhcpTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSystemDhcpTableSnmpKey.setStatus(_A)
_CwsSystemDhcpAdminState_Type=EnabledDisabledEnum
_CwsSystemDhcpAdminState_Object=MibTableColumn
cwsSystemDhcpAdminState=_CwsSystemDhcpAdminState_Object((1,3,6,1,4,1,1271,3,4,12,21,1,2),_CwsSystemDhcpAdminState_Type())
cwsSystemDhcpAdminState.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsSystemDhcpAdminState.setStatus(_A)
cienaWsSystemGroup=ObjectGroup((1,3,6,1,4,1,1271,3,4,12,2,1,1))
cienaWsSystemGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:cienaWsSystemGroup.setStatus(_A)
cienaWsSystemCompliance=ModuleCompliance((1,3,6,1,4,1,1271,3,4,12,2,2,1))
cienaWsSystemCompliance.setObjects((_B,_Ab))
if mibBuilder.loadTexts:cienaWsSystemCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'BandplanEnum':BandplanEnum,'Decimal32Len2':Decimal32Len2,'Decimal32Len5':Decimal32Len5,'LampModeEnum':LampModeEnum,'LampTargetTypeEnum':LampTargetTypeEnum,'LineProtectionEnum':LineProtectionEnum,'cienaWsSystemMIB':cienaWsSystemMIB,'cienaWsSystemObjects':cienaWsSystemObjects,'cienaWsSystemConformance':cienaWsSystemConformance,'cienaWsSystemGroups':cienaWsSystemGroups,_Ab:cienaWsSystemGroup,'cienaWsSystemCompliances':cienaWsSystemCompliances,'cienaWsSystemCompliance':cienaWsSystemCompliance,'cwsSystemSiteTable':cwsSystemSiteTable,'cwsSystemSiteEntry':cwsSystemSiteEntry,_I:cwsSystemSiteTableSnmpKey,_Z:cwsSystemSiteId,_a:cwsSystemSiteName,_b:cwsSystemSiteDescription,_c:cwsSystemSiteLatitude,_d:cwsSystemSiteLongitude,_e:cwsSystemSiteAddress,'cwsSystemGroupTable':cwsSystemGroupTable,'cwsSystemGroupEntry':cwsSystemGroupEntry,_J:cwsSystemGroupTableSnmpKey,_f:cwsSystemGroupId,_g:cwsSystemGroupName,_h:cwsSystemGroupDescription,'cwsSystemMemberTable':cwsSystemMemberTable,'cwsSystemMemberEntry':cwsSystemMemberEntry,_K:cwsSystemMemberTableSnmpKey,_i:cwsSystemMemberId,_j:cwsSystemMemberName,_k:cwsSystemMemberDescription,_l:cwsSystemMemberFrameIdentification,_m:cwsSystemMemberRackUnitNumber,'cwsSystemHostNameTable':cwsSystemHostNameTable,'cwsSystemHostNameEntry':cwsSystemHostNameEntry,_L:cwsSystemHostNameTableSnmpKey,_n:cwsSystemHostNameCurrentHostName,_o:cwsSystemHostNameConfigHostName,_p:cwsSystemHostNameDhcpHostName,'cwsSystemTimeConfigTable':cwsSystemTimeConfigTable,'cwsSystemTimeConfigEntry':cwsSystemTimeConfigEntry,_M:cwsSystemTimeConfigTableSnmpKey,_q:cwsSystemTimeConfigDate,_r:cwsSystemTimeConfigTime,_s:cwsSystemTimeConfigTimeOffset,_t:cwsSystemTimeConfigTimeStamp,_u:cwsSystemTimeConfigLocalDateTime,_v:cwsSystemTimeConfigCoordinatedUniversalTime,_w:cwsSystemTimeConfigSystemUptime,'cwsSystemServerConfigTable':cwsSystemServerConfigTable,'cwsSystemServerConfigEntry':cwsSystemServerConfigEntry,_N:cwsSystemServerConfigTableSnmpKey,_x:cwsSystemServerConfigSftpServerState,_y:cwsSystemServerConfigWebServerState,_z:cwsSystemServerConfigNetconfServerState,_A0:cwsSystemServerConfigRestconfServerState,'cwsSystemXftpConfigTable':cwsSystemXftpConfigTable,'cwsSystemXftpConfigEntry':cwsSystemXftpConfigEntry,_O:cwsSystemXftpConfigTableSnmpKey,_A2:cwsSystemXftpConfigMode,'cwsSystemTftpTable':cwsSystemTftpTable,'cwsSystemTftpEntry':cwsSystemTftpEntry,_P:cwsSystemTftpTableSnmpKey,_A3:cwsSystemTftpConfigHostName,_A4:cwsSystemTftpDhcpHostName,_A5:cwsSystemTftpCurrentHostName,'cwsSystemFtpTable':cwsSystemFtpTable,'cwsSystemFtpEntry':cwsSystemFtpEntry,_Q:cwsSystemFtpTableSnmpKey,_A6:cwsSystemFtpHostName,_A7:cwsSystemFtpUserName,_A8:cwsSystemFtpPassword,_A9:cwsSystemFtpSecret,'cwsSystemSftpTable':cwsSystemSftpTable,'cwsSystemSftpEntry':cwsSystemSftpEntry,_R:cwsSystemSftpTableSnmpKey,_AA:cwsSystemSftpHostName,_AB:cwsSystemSftpUserName,_AC:cwsSystemSftpPassword,_AD:cwsSystemSftpSecret,'cwsSystemGlobalProvisioningTable':cwsSystemGlobalProvisioningTable,'cwsSystemGlobalProvisioningEntry':cwsSystemGlobalProvisioningEntry,_S:cwsSystemGlobalProvisioningTableSnmpKey,_AI:cwsSystemGlobalProvisioningLowPowerMode,_AJ:cwsSystemGlobalProvisioningLampTest,_AK:cwsSystemGlobalProvisioningResetToFactoryDefaultButton,_AL:cwsSystemGlobalProvisioningFcsErrorForwarding,_AM:cwsSystemGlobalProvisioningChassisFunctionality,'cwsSystemFrontDisplayTable':cwsSystemFrontDisplayTable,'cwsSystemFrontDisplayEntry':cwsSystemFrontDisplayEntry,_T:cwsSystemFrontDisplayTableSnmpKey,_AN:cwsSystemFrontDisplayAdminState,_AO:cwsSystemFrontDisplayScreensaverState,_AP:cwsSystemFrontDisplayScreensaverTimeout,_AQ:cwsSystemFrontDisplayInputButtonState,_AR:cwsSystemFrontDisplayUserMessageState,_AS:cwsSystemFrontDisplayUserMessage,'cwsSystemLineConfigTable':cwsSystemLineConfigTable,'cwsSystemLineConfigEntry':cwsSystemLineConfigEntry,_U:cwsSystemLineConfigTableSnmpKey,_AT:cwsSystemLineConfigBandPlan,_AU:cwsSystemLineConfigLineProtection,'cwsSystemLampFlashTestTable':cwsSystemLampFlashTestTable,'cwsSystemLampFlashTestEntry':cwsSystemLampFlashTestEntry,_V:cwsSystemLampFlashTestTableSnmpKey,_AV:cwsSystemLampFlashTestOperationalState,_AW:cwsSystemLampFlashTestMode,_AX:cwsSystemLampFlashTestTargetType,_AY:cwsSystemLampFlashTestTimeout,_AZ:cwsSystemLampFlashTestPorts,'cwsSystemRootTable':cwsSystemRootTable,'cwsSystemRootEntry':cwsSystemRootEntry,_W:cwsSystemRootTableSnmpKey,_Aa:cwsSystemRootPassword,'cwsSystemScpTable':cwsSystemScpTable,'cwsSystemScpEntry':cwsSystemScpEntry,_X:cwsSystemScpTableSnmpKey,_AE:cwsSystemScpHostName,_AF:cwsSystemScpUserName,_AG:cwsSystemScpPassword,_AH:cwsSystemScpSecret,'cwsSystemDhcpTable':cwsSystemDhcpTable,'cwsSystemDhcpEntry':cwsSystemDhcpEntry,_Y:cwsSystemDhcpTableSnmpKey,_A1:cwsSystemDhcpAdminState})