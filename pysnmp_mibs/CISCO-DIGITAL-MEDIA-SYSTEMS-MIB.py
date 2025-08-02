_B4='ciscoDmsNotificationsGroupRev1'
_B3='ciscoDmsNotificationCntlGroupRev1'
_B2='ciscoDmsNotificationsGroup'
_B1='ciscoDmsNotificationCntlGroup'
_B0='ciscoDmsHaAdvancedGroup'
_A_='ciscoDmsHaClusterNodeDown'
_Az='ciscoDmsHaClusterNodeUp'
_Ay='cdmsDmsHaClusterConfigChange'
_Ax='cdmsHaClusterHistNodeNewStatus'
_Aw='cdmsHaClusterHistTimestamp'
_Av='cdmsHaClusterLastVpStatusChangeVpAddress'
_Au='cdmsHaClusterLastStatusChangeVpAddrType'
_At='cdmsHaClusterLastVpStatusChangeCluster'
_As='cdmsHaClusterLastVpStatusChangeTime'
_Ar='cdmsHaClusterLastDmmStatusChangeAddress'
_Aq='cdmsHaClusterLastDmmStatusChangeAddrType'
_Ap='cdmsHaClusterLastDmmStatusChangeTime'
_Ao='cdmsHaVpClusterMemberOperState'
_An='cdmsHaVpClusterMemberIsPrimary'
_Am='cdmsHaVpClusterNumClusters'
_Al='cdmsHaDmmClusterMemberOperState'
_Ak='cdmsHaDmmClusterMemberIsPrimary'
_Aj='cdmsHaClusterDmmVip'
_Ai='cdmsHaClusterDmmVipType'
_Ah='cdmsHaClusterNumActiveDmms'
_Ag='cdmsHaClusterNumTotalDmms'
_Af='cdmsHaClusterName'
_Ae='cdmsHaClusterEnabled'
_Ad='cdmsNumNotificationRate'
_Ac='cdmsNumNotifications'
_Ab='cdmsNumAlarmRate'
_Aa='cdmsNumAlarms'
_AZ='cdmsNumEventRate'
_AY='cdmsNumEvents'
_AX='cdmsLastUserLastChange'
_AW='cdmsNumActiveVpUsers'
_AV='cdmsNumActiveDmmUsers'
_AU='cdmsNumUsers'
_AT='cdmsAuthenticationMode'
_AS='cdmsNumAuthenRequestsDeclined'
_AR='cdmsNumAuthenRequestsApproved'
_AQ='cdmsNumAuthenRequests'
_AP='cdmsNumContentElements'
_AO='cdmsServerStatus'
_AN='cdmsServerState'
_AM='cdmsInventoryElementState'
_AL='cdmsInventoryElementMetadata'
_AK='cdmsNumVideoPortalDevices'
_AJ='cdmsNumMediaIngestionDevices'
_AI='cdmsLicensedFeatureInstallDate'
_AH='cdmsLicensedFeatureDescription'
_AG='cdmsLicensedFeatureLimit'
_AF='cdmsLastLicenseUpdate'
_AE='cdmsLicensedFeatures'
_AD='cdmsLicensableFeatures'
_AC='cdmsAdministrator'
_AB='cdmsPatchVersion'
_AA='cdmsMinorVersion'
_A9='cdmsMajorVersion'
_A8='cdmsHaClusterHistId'
_A7='cdmsHaVpClusterMemberAddress'
_A6='cdmsHaVpClusterMemberAddrType'
_A5='cdmsHaVpClusterMemberVip'
_A4='cdmsHaVpClusterMemberVipType'
_A3='cdmsHaVpClusterMemberClusterName'
_A2='cdmsHaDmmClusterMemberAddress'
_A1='cdmsHaDmmClusterMemberAddrType'
_A0='cdmsServerAddress'
_z='cdmsServerAddrType'
_y='cdmsServerType'
_x='cdmsInventoryElementId'
_w='cdmsInventoryElementType'
_v='cdmsLicensedFeatureIndex'
_u='cdmsLicensedFeature'
_t='Gauge32'
_s='InetAddress'
_r='ciscoDmsAdvancedNotificationsGroup'
_q='ciscoDmsHaGroup'
_p='ciscoDmsEventGroup'
_o='ciscoDmsUserGroup'
_n='ciscoDmsSecurityGroup'
_m='ciscoDamGroup'
_l='ciscoDmsServerGroup'
_k='ciscoDmsFeatureAdvancedGroup'
_j='ciscoDmsInventoryGroup'
_i='ciscoDmsFeatureGroup'
_h='ciscoDmsSystemGroup'
_g='ciscoDmsMediaPlayerAddrTaken'
_f='ciscoDmsMediaPlayerDown'
_e='ciscoDmsMediaPlayerUp'
_d='ciscoDmsMediaPlayerRegistered'
_c='cdmsHaClusterHistoryMaxRecords'
_b='cdmsHaClusterConfigChangeEnable'
_a='cdmsHaClusterNodeDownEnable'
_Z='cdmsHaClusterNodeUpEnable'
_Y='cdmsMediaPlayerAddrTakenEnable'
_X='cdmsMediaPlayerDownEnable'
_W='cdmsMediaPlayerUpEnable'
_V='cdmsMediaPlayerRegisteredEnable'
_U='Users'
_T='requests'
_S='Unsigned32'
_R='cdmsHaClusterHistNodeAddr'
_Q='cdmsHaClusterHistNodeAddrType'
_P='cdmsHaClusterHistNodeType'
_O='cdmsInventoryElementMacAddress'
_N='deprecated'
_M='cdmsHaClusterHistClusterName'
_L='cdmsNumMediaPlayerDevices'
_K='other'
_J='cdmsInventoryElementAddress'
_I='cdmsInventoryElementAddrType'
_H='Integer32'
_G='TruthValue'
_F='SnmpAdminString'
_E='read-write'
_D='not-accessible'
_C='read-only'
_B='current'
_A='CISCO-DIGITAL-MEDIA-SYSTEMS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_s,'InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_t,_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_S,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_G)
ciscoDigitalMediaSystemsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,655))
if mibBuilder.loadTexts:ciscoDigitalMediaSystemsMIB.setRevisions(('2011-09-07 00:00','2011-07-29 00:00','2009-10-12 00:00','2008-05-15 00:00'))
class CDmsUserAuthenMethod(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('none',1),(_K,2),('radius',3),('tacacsPlus',4),('kerberos',5),('local',6),('ldap',7),('ntlm',8),('sdi',9)))
class CDmsServerType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_K,1),('dnsServer',2),('ldapServer',3),('snmpServer',4),('smtpServer',5),('syslogServer',6),('aaaServer',7),('ntpServer',8)))
class CDmsElementType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_K,1),('encoder',2),('videoPortal',3),('mediaPlayer',4),('transCoder',5),('storageServer',6),('streamingServer',7),('dmm',8)))
class CDmsFunctionalStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),('initialize',2),('active',3),('shutdown',4),('standby',5)))
class CDmsEmailAddress(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
class CDmsLicensedFeature(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_K,1),('base',2),('deskTopVideo',3),('liveWebcastEnabler',4),('digitalSignage',5),('enterpriseTv',6),('snmpManagement',7),('digitalMediaPlayer',8),('digitalMediaPlayerAuthorPack',9),('digitalMedialPlayerProofOfPlayPack',10),('clustering',11)))
_CiscoDmsMonitorMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoDmsMonitorMIBNotifs=_CiscoDmsMonitorMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,655,0))
_CiscoDmsMonitorMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDmsMonitorMIBObjects=_CiscoDmsMonitorMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,655,1))
_CdmsSystem_ObjectIdentity=ObjectIdentity
cdmsSystem=_CdmsSystem_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,1))
class _CdmsMajorVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_CdmsMajorVersion_Type.__name__=_F
_CdmsMajorVersion_Object=MibScalar
cdmsMajorVersion=_CdmsMajorVersion_Object((1,3,6,1,4,1,9,9,655,1,1,1),_CdmsMajorVersion_Type())
cdmsMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsMajorVersion.setStatus(_B)
class _CdmsMinorVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_CdmsMinorVersion_Type.__name__=_F
_CdmsMinorVersion_Object=MibScalar
cdmsMinorVersion=_CdmsMinorVersion_Object((1,3,6,1,4,1,9,9,655,1,1,2),_CdmsMinorVersion_Type())
cdmsMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsMinorVersion.setStatus(_B)
class _CdmsPatchVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_CdmsPatchVersion_Type.__name__=_F
_CdmsPatchVersion_Object=MibScalar
cdmsPatchVersion=_CdmsPatchVersion_Object((1,3,6,1,4,1,9,9,655,1,1,3),_CdmsPatchVersion_Type())
cdmsPatchVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsPatchVersion.setStatus(_B)
_CdmsAdministrator_Type=CDmsEmailAddress
_CdmsAdministrator_Object=MibScalar
cdmsAdministrator=_CdmsAdministrator_Object((1,3,6,1,4,1,9,9,655,1,1,4),_CdmsAdministrator_Type())
cdmsAdministrator.setMaxAccess(_E)
if mibBuilder.loadTexts:cdmsAdministrator.setStatus(_B)
_CdmsFeatures_ObjectIdentity=ObjectIdentity
cdmsFeatures=_CdmsFeatures_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,2))
_CdmsFeatureSummary_ObjectIdentity=ObjectIdentity
cdmsFeatureSummary=_CdmsFeatureSummary_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,2,1))
_CdmsLicensableFeatures_Type=Unsigned32
_CdmsLicensableFeatures_Object=MibScalar
cdmsLicensableFeatures=_CdmsLicensableFeatures_Object((1,3,6,1,4,1,9,9,655,1,2,1,1),_CdmsLicensableFeatures_Type())
cdmsLicensableFeatures.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsLicensableFeatures.setStatus(_B)
_CdmsLicensedFeatures_Type=Unsigned32
_CdmsLicensedFeatures_Object=MibScalar
cdmsLicensedFeatures=_CdmsLicensedFeatures_Object((1,3,6,1,4,1,9,9,655,1,2,1,2),_CdmsLicensedFeatures_Type())
cdmsLicensedFeatures.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsLicensedFeatures.setStatus(_B)
_CdmsLastLicenseUpdate_Type=DateAndTime
_CdmsLastLicenseUpdate_Object=MibScalar
cdmsLastLicenseUpdate=_CdmsLastLicenseUpdate_Object((1,3,6,1,4,1,9,9,655,1,2,1,3),_CdmsLastLicenseUpdate_Type())
cdmsLastLicenseUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsLastLicenseUpdate.setStatus(_B)
_CdmsLicensedFeatureTable_Object=MibTable
cdmsLicensedFeatureTable=_CdmsLicensedFeatureTable_Object((1,3,6,1,4,1,9,9,655,1,2,2))
if mibBuilder.loadTexts:cdmsLicensedFeatureTable.setStatus(_B)
_CdmsLicensedFeatureEntry_Object=MibTableRow
cdmsLicensedFeatureEntry=_CdmsLicensedFeatureEntry_Object((1,3,6,1,4,1,9,9,655,1,2,2,1))
cdmsLicensedFeatureEntry.setIndexNames((0,_A,_u),(0,_A,_v))
if mibBuilder.loadTexts:cdmsLicensedFeatureEntry.setStatus(_B)
_CdmsLicensedFeature_Type=CDmsLicensedFeature
_CdmsLicensedFeature_Object=MibTableColumn
cdmsLicensedFeature=_CdmsLicensedFeature_Object((1,3,6,1,4,1,9,9,655,1,2,2,1,1),_CdmsLicensedFeature_Type())
cdmsLicensedFeature.setMaxAccess(_D)
if mibBuilder.loadTexts:cdmsLicensedFeature.setStatus(_B)
class _CdmsLicensedFeatureIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_CdmsLicensedFeatureIndex_Type.__name__=_S
_CdmsLicensedFeatureIndex_Object=MibTableColumn
cdmsLicensedFeatureIndex=_CdmsLicensedFeatureIndex_Object((1,3,6,1,4,1,9,9,655,1,2,2,1,2),_CdmsLicensedFeatureIndex_Type())
cdmsLicensedFeatureIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cdmsLicensedFeatureIndex.setStatus(_B)
class _CdmsLicensedFeatureLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CdmsLicensedFeatureLimit_Type.__name__=_S
_CdmsLicensedFeatureLimit_Object=MibTableColumn
cdmsLicensedFeatureLimit=_CdmsLicensedFeatureLimit_Object((1,3,6,1,4,1,9,9,655,1,2,2,1,3),_CdmsLicensedFeatureLimit_Type())
cdmsLicensedFeatureLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsLicensedFeatureLimit.setStatus(_N)
_CdmsLicensedFeatureDescription_Type=SnmpAdminString
_CdmsLicensedFeatureDescription_Object=MibTableColumn
cdmsLicensedFeatureDescription=_CdmsLicensedFeatureDescription_Object((1,3,6,1,4,1,9,9,655,1,2,2,1,4),_CdmsLicensedFeatureDescription_Type())
cdmsLicensedFeatureDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsLicensedFeatureDescription.setStatus(_B)
_CdmsLicensedFeatureInstallDate_Type=DateAndTime
_CdmsLicensedFeatureInstallDate_Object=MibTableColumn
cdmsLicensedFeatureInstallDate=_CdmsLicensedFeatureInstallDate_Object((1,3,6,1,4,1,9,9,655,1,2,2,1,5),_CdmsLicensedFeatureInstallDate_Type())
cdmsLicensedFeatureInstallDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsLicensedFeatureInstallDate.setStatus(_B)
class _CdmsLicensedFeatureLimitRev1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-3,2147483647))
_CdmsLicensedFeatureLimitRev1_Type.__name__=_H
_CdmsLicensedFeatureLimitRev1_Object=MibTableColumn
cdmsLicensedFeatureLimitRev1=_CdmsLicensedFeatureLimitRev1_Object((1,3,6,1,4,1,9,9,655,1,2,2,1,6),_CdmsLicensedFeatureLimitRev1_Type())
cdmsLicensedFeatureLimitRev1.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsLicensedFeatureLimitRev1.setStatus(_B)
_CdmsInventory_ObjectIdentity=ObjectIdentity
cdmsInventory=_CdmsInventory_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,3))
_CdmsInventoryGlobalCounters_ObjectIdentity=ObjectIdentity
cdmsInventoryGlobalCounters=_CdmsInventoryGlobalCounters_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,3,1))
_CdmsNumMediaIngestionDevices_Type=Gauge32
_CdmsNumMediaIngestionDevices_Object=MibScalar
cdmsNumMediaIngestionDevices=_CdmsNumMediaIngestionDevices_Object((1,3,6,1,4,1,9,9,655,1,3,1,1),_CdmsNumMediaIngestionDevices_Type())
cdmsNumMediaIngestionDevices.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsNumMediaIngestionDevices.setStatus(_B)
if mibBuilder.loadTexts:cdmsNumMediaIngestionDevices.setUnits('Encoders')
_CdmsNumMediaPlayerDevices_Type=Gauge32
_CdmsNumMediaPlayerDevices_Object=MibScalar
cdmsNumMediaPlayerDevices=_CdmsNumMediaPlayerDevices_Object((1,3,6,1,4,1,9,9,655,1,3,1,2),_CdmsNumMediaPlayerDevices_Type())
cdmsNumMediaPlayerDevices.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsNumMediaPlayerDevices.setStatus(_B)
if mibBuilder.loadTexts:cdmsNumMediaPlayerDevices.setUnits('Media Players')
_CdmsNumVideoPortalDevices_Type=Gauge32
_CdmsNumVideoPortalDevices_Object=MibScalar
cdmsNumVideoPortalDevices=_CdmsNumVideoPortalDevices_Object((1,3,6,1,4,1,9,9,655,1,3,1,3),_CdmsNumVideoPortalDevices_Type())
cdmsNumVideoPortalDevices.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsNumVideoPortalDevices.setStatus(_B)
if mibBuilder.loadTexts:cdmsNumVideoPortalDevices.setUnits('Video Portals')
_CdmsInventoryTable_Object=MibTable
cdmsInventoryTable=_CdmsInventoryTable_Object((1,3,6,1,4,1,9,9,655,1,3,2))
if mibBuilder.loadTexts:cdmsInventoryTable.setStatus(_B)
_CdmsInventoryEntry_Object=MibTableRow
cdmsInventoryEntry=_CdmsInventoryEntry_Object((1,3,6,1,4,1,9,9,655,1,3,2,1))
cdmsInventoryEntry.setIndexNames((0,_A,_w),(0,_A,_x))
if mibBuilder.loadTexts:cdmsInventoryEntry.setStatus(_B)
_CdmsInventoryElementType_Type=CDmsElementType
_CdmsInventoryElementType_Object=MibTableColumn
cdmsInventoryElementType=_CdmsInventoryElementType_Object((1,3,6,1,4,1,9,9,655,1,3,2,1,1),_CdmsInventoryElementType_Type())
cdmsInventoryElementType.setMaxAccess(_D)
if mibBuilder.loadTexts:cdmsInventoryElementType.setStatus(_B)
class _CdmsInventoryElementId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CdmsInventoryElementId_Type.__name__=_F
_CdmsInventoryElementId_Object=MibTableColumn
cdmsInventoryElementId=_CdmsInventoryElementId_Object((1,3,6,1,4,1,9,9,655,1,3,2,1,2),_CdmsInventoryElementId_Type())
cdmsInventoryElementId.setMaxAccess(_D)
if mibBuilder.loadTexts:cdmsInventoryElementId.setStatus(_B)
_CdmsInventoryElementMacAddress_Type=MacAddress
_CdmsInventoryElementMacAddress_Object=MibTableColumn
cdmsInventoryElementMacAddress=_CdmsInventoryElementMacAddress_Object((1,3,6,1,4,1,9,9,655,1,3,2,1,3),_CdmsInventoryElementMacAddress_Type())
cdmsInventoryElementMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsInventoryElementMacAddress.setStatus(_B)
_CdmsInventoryElementAddrType_Type=InetAddressType
_CdmsInventoryElementAddrType_Object=MibTableColumn
cdmsInventoryElementAddrType=_CdmsInventoryElementAddrType_Object((1,3,6,1,4,1,9,9,655,1,3,2,1,4),_CdmsInventoryElementAddrType_Type())
cdmsInventoryElementAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsInventoryElementAddrType.setStatus(_B)
_CdmsInventoryElementAddress_Type=InetAddress
_CdmsInventoryElementAddress_Object=MibTableColumn
cdmsInventoryElementAddress=_CdmsInventoryElementAddress_Object((1,3,6,1,4,1,9,9,655,1,3,2,1,5),_CdmsInventoryElementAddress_Type())
cdmsInventoryElementAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsInventoryElementAddress.setStatus(_B)
_CdmsInventoryElementMetadata_Type=SnmpAdminString
_CdmsInventoryElementMetadata_Object=MibTableColumn
cdmsInventoryElementMetadata=_CdmsInventoryElementMetadata_Object((1,3,6,1,4,1,9,9,655,1,3,2,1,6),_CdmsInventoryElementMetadata_Type())
cdmsInventoryElementMetadata.setMaxAccess(_E)
if mibBuilder.loadTexts:cdmsInventoryElementMetadata.setStatus(_B)
_CdmsInventoryElementState_Type=CDmsFunctionalStatus
_CdmsInventoryElementState_Object=MibTableColumn
cdmsInventoryElementState=_CdmsInventoryElementState_Object((1,3,6,1,4,1,9,9,655,1,3,2,1,7),_CdmsInventoryElementState_Type())
cdmsInventoryElementState.setMaxAccess(_E)
if mibBuilder.loadTexts:cdmsInventoryElementState.setStatus(_B)
_CdmsServers_ObjectIdentity=ObjectIdentity
cdmsServers=_CdmsServers_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,4))
_CdmsServerTable_Object=MibTable
cdmsServerTable=_CdmsServerTable_Object((1,3,6,1,4,1,9,9,655,1,4,1))
if mibBuilder.loadTexts:cdmsServerTable.setStatus(_B)
_CdmsServerEntry_Object=MibTableRow
cdmsServerEntry=_CdmsServerEntry_Object((1,3,6,1,4,1,9,9,655,1,4,1,1))
cdmsServerEntry.setIndexNames((0,_A,_y),(0,_A,_z),(0,_A,_A0))
if mibBuilder.loadTexts:cdmsServerEntry.setStatus(_B)
_CdmsServerType_Type=CDmsServerType
_CdmsServerType_Object=MibTableColumn
cdmsServerType=_CdmsServerType_Object((1,3,6,1,4,1,9,9,655,1,4,1,1,1),_CdmsServerType_Type())
cdmsServerType.setMaxAccess(_D)
if mibBuilder.loadTexts:cdmsServerType.setStatus(_B)
_CdmsServerAddrType_Type=InetAddressType
_CdmsServerAddrType_Object=MibTableColumn
cdmsServerAddrType=_CdmsServerAddrType_Object((1,3,6,1,4,1,9,9,655,1,4,1,1,2),_CdmsServerAddrType_Type())
cdmsServerAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cdmsServerAddrType.setStatus(_B)
class _CdmsServerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CdmsServerAddress_Type.__name__=_s
_CdmsServerAddress_Object=MibTableColumn
cdmsServerAddress=_CdmsServerAddress_Object((1,3,6,1,4,1,9,9,655,1,4,1,1,3),_CdmsServerAddress_Type())
cdmsServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cdmsServerAddress.setStatus(_B)
_CdmsServerState_Type=CDmsFunctionalStatus
_CdmsServerState_Object=MibTableColumn
cdmsServerState=_CdmsServerState_Object((1,3,6,1,4,1,9,9,655,1,4,1,1,4),_CdmsServerState_Type())
cdmsServerState.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsServerState.setStatus(_B)
_CdmsServerStatus_Type=RowStatus
_CdmsServerStatus_Object=MibTableColumn
cdmsServerStatus=_CdmsServerStatus_Object((1,3,6,1,4,1,9,9,655,1,4,1,1,5),_CdmsServerStatus_Type())
cdmsServerStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:cdmsServerStatus.setStatus(_B)
_CdmsDamServices_ObjectIdentity=ObjectIdentity
cdmsDamServices=_CdmsDamServices_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,5))
_CdmsDamGlobalCounters_ObjectIdentity=ObjectIdentity
cdmsDamGlobalCounters=_CdmsDamGlobalCounters_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,5,1))
_CdmsNumContentElements_Type=Gauge32
_CdmsNumContentElements_Object=MibScalar
cdmsNumContentElements=_CdmsNumContentElements_Object((1,3,6,1,4,1,9,9,655,1,5,1,1),_CdmsNumContentElements_Type())
cdmsNumContentElements.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsNumContentElements.setStatus(_B)
if mibBuilder.loadTexts:cdmsNumContentElements.setUnits('content elements')
_CdmsNumAuthenRequestsApproved_Type=Counter64
_CdmsNumAuthenRequestsApproved_Object=MibScalar
cdmsNumAuthenRequestsApproved=_CdmsNumAuthenRequestsApproved_Object((1,3,6,1,4,1,9,9,655,1,5,1,2),_CdmsNumAuthenRequestsApproved_Type())
cdmsNumAuthenRequestsApproved.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsNumAuthenRequestsApproved.setStatus(_B)
if mibBuilder.loadTexts:cdmsNumAuthenRequestsApproved.setUnits(_T)
_CdmsNumAuthenRequestsDeclined_Type=Counter64
_CdmsNumAuthenRequestsDeclined_Object=MibScalar
cdmsNumAuthenRequestsDeclined=_CdmsNumAuthenRequestsDeclined_Object((1,3,6,1,4,1,9,9,655,1,5,1,3),_CdmsNumAuthenRequestsDeclined_Type())
cdmsNumAuthenRequestsDeclined.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsNumAuthenRequestsDeclined.setStatus(_B)
if mibBuilder.loadTexts:cdmsNumAuthenRequestsDeclined.setUnits(_T)
_CdmsSecurity_ObjectIdentity=ObjectIdentity
cdmsSecurity=_CdmsSecurity_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,6))
_CdmsSecurityGlobalCounters_ObjectIdentity=ObjectIdentity
cdmsSecurityGlobalCounters=_CdmsSecurityGlobalCounters_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,6,1))
_CdmsNumAuthenRequests_Type=Counter64
_CdmsNumAuthenRequests_Object=MibScalar
cdmsNumAuthenRequests=_CdmsNumAuthenRequests_Object((1,3,6,1,4,1,9,9,655,1,6,1,1),_CdmsNumAuthenRequests_Type())
cdmsNumAuthenRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsNumAuthenRequests.setStatus(_B)
if mibBuilder.loadTexts:cdmsNumAuthenRequests.setUnits(_T)
_CdmsSecurityConfiguration_ObjectIdentity=ObjectIdentity
cdmsSecurityConfiguration=_CdmsSecurityConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,6,2))
_CdmsAuthenticationMode_Type=CDmsUserAuthenMethod
_CdmsAuthenticationMode_Object=MibScalar
cdmsAuthenticationMode=_CdmsAuthenticationMode_Object((1,3,6,1,4,1,9,9,655,1,6,2,1),_CdmsAuthenticationMode_Type())
cdmsAuthenticationMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cdmsAuthenticationMode.setStatus(_B)
_CdmsUserGroup_ObjectIdentity=ObjectIdentity
cdmsUserGroup=_CdmsUserGroup_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,7))
_CdmsNumUsers_Type=Gauge32
_CdmsNumUsers_Object=MibScalar
cdmsNumUsers=_CdmsNumUsers_Object((1,3,6,1,4,1,9,9,655,1,7,1),_CdmsNumUsers_Type())
cdmsNumUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsNumUsers.setStatus(_B)
if mibBuilder.loadTexts:cdmsNumUsers.setUnits(_U)
_CdmsNumActiveDmmUsers_Type=Gauge32
_CdmsNumActiveDmmUsers_Object=MibScalar
cdmsNumActiveDmmUsers=_CdmsNumActiveDmmUsers_Object((1,3,6,1,4,1,9,9,655,1,7,2),_CdmsNumActiveDmmUsers_Type())
cdmsNumActiveDmmUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsNumActiveDmmUsers.setStatus(_B)
if mibBuilder.loadTexts:cdmsNumActiveDmmUsers.setUnits(_U)
_CdmsNumActiveVpUsers_Type=Gauge32
_CdmsNumActiveVpUsers_Object=MibScalar
cdmsNumActiveVpUsers=_CdmsNumActiveVpUsers_Object((1,3,6,1,4,1,9,9,655,1,7,3),_CdmsNumActiveVpUsers_Type())
cdmsNumActiveVpUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsNumActiveVpUsers.setStatus(_B)
if mibBuilder.loadTexts:cdmsNumActiveVpUsers.setUnits(_U)
_CdmsLastUserLastChange_Type=DateAndTime
_CdmsLastUserLastChange_Object=MibScalar
cdmsLastUserLastChange=_CdmsLastUserLastChange_Object((1,3,6,1,4,1,9,9,655,1,7,4),_CdmsLastUserLastChange_Type())
cdmsLastUserLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsLastUserLastChange.setStatus(_B)
_CdmsEvents_ObjectIdentity=ObjectIdentity
cdmsEvents=_CdmsEvents_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,8))
_CdmsEventConfiguration_ObjectIdentity=ObjectIdentity
cdmsEventConfiguration=_CdmsEventConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,8,1))
_CdmsEventStatistics_ObjectIdentity=ObjectIdentity
cdmsEventStatistics=_CdmsEventStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,8,2))
_CdmsNumEvents_Type=Counter64
_CdmsNumEvents_Object=MibScalar
cdmsNumEvents=_CdmsNumEvents_Object((1,3,6,1,4,1,9,9,655,1,8,2,1),_CdmsNumEvents_Type())
cdmsNumEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsNumEvents.setStatus(_B)
if mibBuilder.loadTexts:cdmsNumEvents.setUnits('Events')
_CdmsNumEventRate_Type=Gauge32
_CdmsNumEventRate_Object=MibScalar
cdmsNumEventRate=_CdmsNumEventRate_Object((1,3,6,1,4,1,9,9,655,1,8,2,2),_CdmsNumEventRate_Type())
cdmsNumEventRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsNumEventRate.setStatus(_B)
if mibBuilder.loadTexts:cdmsNumEventRate.setUnits('Events per minute')
_CdmsNumAlarms_Type=Counter64
_CdmsNumAlarms_Object=MibScalar
cdmsNumAlarms=_CdmsNumAlarms_Object((1,3,6,1,4,1,9,9,655,1,8,2,3),_CdmsNumAlarms_Type())
cdmsNumAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsNumAlarms.setStatus(_B)
if mibBuilder.loadTexts:cdmsNumAlarms.setUnits('Alarms')
_CdmsNumAlarmRate_Type=Gauge32
_CdmsNumAlarmRate_Object=MibScalar
cdmsNumAlarmRate=_CdmsNumAlarmRate_Object((1,3,6,1,4,1,9,9,655,1,8,2,4),_CdmsNumAlarmRate_Type())
cdmsNumAlarmRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsNumAlarmRate.setStatus(_B)
if mibBuilder.loadTexts:cdmsNumAlarmRate.setUnits('Alarms per minute')
_CdmsNumNotifications_Type=Counter64
_CdmsNumNotifications_Object=MibScalar
cdmsNumNotifications=_CdmsNumNotifications_Object((1,3,6,1,4,1,9,9,655,1,8,2,5),_CdmsNumNotifications_Type())
cdmsNumNotifications.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsNumNotifications.setStatus(_B)
if mibBuilder.loadTexts:cdmsNumNotifications.setUnits('Notifications')
_CdmsNumNotificationRate_Type=Gauge32
_CdmsNumNotificationRate_Object=MibScalar
cdmsNumNotificationRate=_CdmsNumNotificationRate_Object((1,3,6,1,4,1,9,9,655,1,8,2,6),_CdmsNumNotificationRate_Type())
cdmsNumNotificationRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsNumNotificationRate.setStatus(_B)
if mibBuilder.loadTexts:cdmsNumNotificationRate.setUnits('Notifications per minute')
_CdmsHa_ObjectIdentity=ObjectIdentity
cdmsHa=_CdmsHa_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,10))
_CdmsHaClusterInfo_ObjectIdentity=ObjectIdentity
cdmsHaClusterInfo=_CdmsHaClusterInfo_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,10,1))
class _CdmsHaClusterEnabled_Type(TruthValue):defaultValue=2
_CdmsHaClusterEnabled_Type.__name__=_G
_CdmsHaClusterEnabled_Object=MibScalar
cdmsHaClusterEnabled=_CdmsHaClusterEnabled_Object((1,3,6,1,4,1,9,9,655,1,10,1,1),_CdmsHaClusterEnabled_Type())
cdmsHaClusterEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterEnabled.setStatus(_B)
class _CdmsHaClusterName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CdmsHaClusterName_Type.__name__=_F
_CdmsHaClusterName_Object=MibScalar
cdmsHaClusterName=_CdmsHaClusterName_Object((1,3,6,1,4,1,9,9,655,1,10,1,2),_CdmsHaClusterName_Type())
cdmsHaClusterName.setMaxAccess(_E)
if mibBuilder.loadTexts:cdmsHaClusterName.setStatus(_B)
_CdmsHaClusterComposition_ObjectIdentity=ObjectIdentity
cdmsHaClusterComposition=_CdmsHaClusterComposition_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,10,2))
_CdmsHaDmmCluster_ObjectIdentity=ObjectIdentity
cdmsHaDmmCluster=_CdmsHaDmmCluster_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,10,2,1))
class _CdmsHaClusterNumTotalDmms_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_CdmsHaClusterNumTotalDmms_Type.__name__=_H
_CdmsHaClusterNumTotalDmms_Object=MibScalar
cdmsHaClusterNumTotalDmms=_CdmsHaClusterNumTotalDmms_Object((1,3,6,1,4,1,9,9,655,1,10,2,1,1),_CdmsHaClusterNumTotalDmms_Type())
cdmsHaClusterNumTotalDmms.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterNumTotalDmms.setStatus(_B)
if mibBuilder.loadTexts:cdmsHaClusterNumTotalDmms.setUnits('Nodes')
class _CdmsHaClusterNumActiveDmms_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CdmsHaClusterNumActiveDmms_Type.__name__=_t
_CdmsHaClusterNumActiveDmms_Object=MibScalar
cdmsHaClusterNumActiveDmms=_CdmsHaClusterNumActiveDmms_Object((1,3,6,1,4,1,9,9,655,1,10,2,1,2),_CdmsHaClusterNumActiveDmms_Type())
cdmsHaClusterNumActiveDmms.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterNumActiveDmms.setStatus(_B)
if mibBuilder.loadTexts:cdmsHaClusterNumActiveDmms.setUnits('Nodes')
_CdmsHaClusterDmmVipType_Type=InetAddressType
_CdmsHaClusterDmmVipType_Object=MibScalar
cdmsHaClusterDmmVipType=_CdmsHaClusterDmmVipType_Object((1,3,6,1,4,1,9,9,655,1,10,2,1,3),_CdmsHaClusterDmmVipType_Type())
cdmsHaClusterDmmVipType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterDmmVipType.setStatus(_B)
_CdmsHaClusterDmmVip_Type=InetAddress
_CdmsHaClusterDmmVip_Object=MibScalar
cdmsHaClusterDmmVip=_CdmsHaClusterDmmVip_Object((1,3,6,1,4,1,9,9,655,1,10,2,1,4),_CdmsHaClusterDmmVip_Type())
cdmsHaClusterDmmVip.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterDmmVip.setStatus(_B)
_CdmsHaDmmClusterMemberTable_Object=MibTable
cdmsHaDmmClusterMemberTable=_CdmsHaDmmClusterMemberTable_Object((1,3,6,1,4,1,9,9,655,1,10,2,1,5))
if mibBuilder.loadTexts:cdmsHaDmmClusterMemberTable.setStatus(_B)
_CdmsHaDmmClusterMemberEntry_Object=MibTableRow
cdmsHaDmmClusterMemberEntry=_CdmsHaDmmClusterMemberEntry_Object((1,3,6,1,4,1,9,9,655,1,10,2,1,5,1))
cdmsHaDmmClusterMemberEntry.setIndexNames((0,_A,_A1),(0,_A,_A2))
if mibBuilder.loadTexts:cdmsHaDmmClusterMemberEntry.setStatus(_B)
_CdmsHaDmmClusterMemberAddrType_Type=InetAddressType
_CdmsHaDmmClusterMemberAddrType_Object=MibTableColumn
cdmsHaDmmClusterMemberAddrType=_CdmsHaDmmClusterMemberAddrType_Object((1,3,6,1,4,1,9,9,655,1,10,2,1,5,1,1),_CdmsHaDmmClusterMemberAddrType_Type())
cdmsHaDmmClusterMemberAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cdmsHaDmmClusterMemberAddrType.setStatus(_B)
_CdmsHaDmmClusterMemberAddress_Type=InetAddress
_CdmsHaDmmClusterMemberAddress_Object=MibTableColumn
cdmsHaDmmClusterMemberAddress=_CdmsHaDmmClusterMemberAddress_Object((1,3,6,1,4,1,9,9,655,1,10,2,1,5,1,2),_CdmsHaDmmClusterMemberAddress_Type())
cdmsHaDmmClusterMemberAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cdmsHaDmmClusterMemberAddress.setStatus(_B)
_CdmsHaDmmClusterMemberIsPrimary_Type=TruthValue
_CdmsHaDmmClusterMemberIsPrimary_Object=MibTableColumn
cdmsHaDmmClusterMemberIsPrimary=_CdmsHaDmmClusterMemberIsPrimary_Object((1,3,6,1,4,1,9,9,655,1,10,2,1,5,1,3),_CdmsHaDmmClusterMemberIsPrimary_Type())
cdmsHaDmmClusterMemberIsPrimary.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaDmmClusterMemberIsPrimary.setStatus(_B)
_CdmsHaDmmClusterMemberOperState_Type=CDmsFunctionalStatus
_CdmsHaDmmClusterMemberOperState_Object=MibTableColumn
cdmsHaDmmClusterMemberOperState=_CdmsHaDmmClusterMemberOperState_Object((1,3,6,1,4,1,9,9,655,1,10,2,1,5,1,4),_CdmsHaDmmClusterMemberOperState_Type())
cdmsHaDmmClusterMemberOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaDmmClusterMemberOperState.setStatus(_B)
_CdmsHaVpCluster_ObjectIdentity=ObjectIdentity
cdmsHaVpCluster=_CdmsHaVpCluster_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,10,2,2))
class _CdmsHaVpClusterNumClusters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_CdmsHaVpClusterNumClusters_Type.__name__=_H
_CdmsHaVpClusterNumClusters_Object=MibScalar
cdmsHaVpClusterNumClusters=_CdmsHaVpClusterNumClusters_Object((1,3,6,1,4,1,9,9,655,1,10,2,2,1),_CdmsHaVpClusterNumClusters_Type())
cdmsHaVpClusterNumClusters.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaVpClusterNumClusters.setStatus(_B)
_CdmsHaVpClusterMemberTable_Object=MibTable
cdmsHaVpClusterMemberTable=_CdmsHaVpClusterMemberTable_Object((1,3,6,1,4,1,9,9,655,1,10,2,2,2))
if mibBuilder.loadTexts:cdmsHaVpClusterMemberTable.setStatus(_B)
_CdmsHaVpClusterMemberEntry_Object=MibTableRow
cdmsHaVpClusterMemberEntry=_CdmsHaVpClusterMemberEntry_Object((1,3,6,1,4,1,9,9,655,1,10,2,2,2,1))
cdmsHaVpClusterMemberEntry.setIndexNames((0,_A,_A3),(0,_A,_A4),(0,_A,_A5),(0,_A,_A6),(0,_A,_A7))
if mibBuilder.loadTexts:cdmsHaVpClusterMemberEntry.setStatus(_B)
class _CdmsHaVpClusterMemberClusterName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CdmsHaVpClusterMemberClusterName_Type.__name__=_F
_CdmsHaVpClusterMemberClusterName_Object=MibTableColumn
cdmsHaVpClusterMemberClusterName=_CdmsHaVpClusterMemberClusterName_Object((1,3,6,1,4,1,9,9,655,1,10,2,2,2,1,1),_CdmsHaVpClusterMemberClusterName_Type())
cdmsHaVpClusterMemberClusterName.setMaxAccess(_D)
if mibBuilder.loadTexts:cdmsHaVpClusterMemberClusterName.setStatus(_B)
_CdmsHaVpClusterMemberVipType_Type=InetAddressType
_CdmsHaVpClusterMemberVipType_Object=MibTableColumn
cdmsHaVpClusterMemberVipType=_CdmsHaVpClusterMemberVipType_Object((1,3,6,1,4,1,9,9,655,1,10,2,2,2,1,2),_CdmsHaVpClusterMemberVipType_Type())
cdmsHaVpClusterMemberVipType.setMaxAccess(_D)
if mibBuilder.loadTexts:cdmsHaVpClusterMemberVipType.setStatus(_B)
_CdmsHaVpClusterMemberVip_Type=InetAddress
_CdmsHaVpClusterMemberVip_Object=MibTableColumn
cdmsHaVpClusterMemberVip=_CdmsHaVpClusterMemberVip_Object((1,3,6,1,4,1,9,9,655,1,10,2,2,2,1,3),_CdmsHaVpClusterMemberVip_Type())
cdmsHaVpClusterMemberVip.setMaxAccess(_D)
if mibBuilder.loadTexts:cdmsHaVpClusterMemberVip.setStatus(_B)
_CdmsHaVpClusterMemberAddrType_Type=InetAddressType
_CdmsHaVpClusterMemberAddrType_Object=MibTableColumn
cdmsHaVpClusterMemberAddrType=_CdmsHaVpClusterMemberAddrType_Object((1,3,6,1,4,1,9,9,655,1,10,2,2,2,1,4),_CdmsHaVpClusterMemberAddrType_Type())
cdmsHaVpClusterMemberAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cdmsHaVpClusterMemberAddrType.setStatus(_B)
_CdmsHaVpClusterMemberAddress_Type=InetAddress
_CdmsHaVpClusterMemberAddress_Object=MibTableColumn
cdmsHaVpClusterMemberAddress=_CdmsHaVpClusterMemberAddress_Object((1,3,6,1,4,1,9,9,655,1,10,2,2,2,1,5),_CdmsHaVpClusterMemberAddress_Type())
cdmsHaVpClusterMemberAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cdmsHaVpClusterMemberAddress.setStatus(_B)
_CdmsHaVpClusterMemberIsPrimary_Type=TruthValue
_CdmsHaVpClusterMemberIsPrimary_Object=MibTableColumn
cdmsHaVpClusterMemberIsPrimary=_CdmsHaVpClusterMemberIsPrimary_Object((1,3,6,1,4,1,9,9,655,1,10,2,2,2,1,6),_CdmsHaVpClusterMemberIsPrimary_Type())
cdmsHaVpClusterMemberIsPrimary.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaVpClusterMemberIsPrimary.setStatus(_B)
_CdmsHaVpClusterMemberOperState_Type=CDmsFunctionalStatus
_CdmsHaVpClusterMemberOperState_Object=MibTableColumn
cdmsHaVpClusterMemberOperState=_CdmsHaVpClusterMemberOperState_Object((1,3,6,1,4,1,9,9,655,1,10,2,2,2,1,7),_CdmsHaVpClusterMemberOperState_Type())
cdmsHaVpClusterMemberOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaVpClusterMemberOperState.setStatus(_B)
_CdmsHaClusterStatus_ObjectIdentity=ObjectIdentity
cdmsHaClusterStatus=_CdmsHaClusterStatus_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,10,3))
_CdmsHaClusterLastDmmStatusChangeTime_Type=DateAndTime
_CdmsHaClusterLastDmmStatusChangeTime_Object=MibScalar
cdmsHaClusterLastDmmStatusChangeTime=_CdmsHaClusterLastDmmStatusChangeTime_Object((1,3,6,1,4,1,9,9,655,1,10,3,1),_CdmsHaClusterLastDmmStatusChangeTime_Type())
cdmsHaClusterLastDmmStatusChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterLastDmmStatusChangeTime.setStatus(_B)
_CdmsHaClusterLastDmmStatusChangeAddrType_Type=InetAddressType
_CdmsHaClusterLastDmmStatusChangeAddrType_Object=MibScalar
cdmsHaClusterLastDmmStatusChangeAddrType=_CdmsHaClusterLastDmmStatusChangeAddrType_Object((1,3,6,1,4,1,9,9,655,1,10,3,2),_CdmsHaClusterLastDmmStatusChangeAddrType_Type())
cdmsHaClusterLastDmmStatusChangeAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterLastDmmStatusChangeAddrType.setStatus(_B)
_CdmsHaClusterLastDmmStatusChangeAddress_Type=InetAddress
_CdmsHaClusterLastDmmStatusChangeAddress_Object=MibScalar
cdmsHaClusterLastDmmStatusChangeAddress=_CdmsHaClusterLastDmmStatusChangeAddress_Object((1,3,6,1,4,1,9,9,655,1,10,3,3),_CdmsHaClusterLastDmmStatusChangeAddress_Type())
cdmsHaClusterLastDmmStatusChangeAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterLastDmmStatusChangeAddress.setStatus(_B)
_CdmsHaClusterLastVpStatusChangeTime_Type=DateAndTime
_CdmsHaClusterLastVpStatusChangeTime_Object=MibScalar
cdmsHaClusterLastVpStatusChangeTime=_CdmsHaClusterLastVpStatusChangeTime_Object((1,3,6,1,4,1,9,9,655,1,10,3,4),_CdmsHaClusterLastVpStatusChangeTime_Type())
cdmsHaClusterLastVpStatusChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterLastVpStatusChangeTime.setStatus(_B)
class _CdmsHaClusterLastVpStatusChangeCluster_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CdmsHaClusterLastVpStatusChangeCluster_Type.__name__=_F
_CdmsHaClusterLastVpStatusChangeCluster_Object=MibScalar
cdmsHaClusterLastVpStatusChangeCluster=_CdmsHaClusterLastVpStatusChangeCluster_Object((1,3,6,1,4,1,9,9,655,1,10,3,5),_CdmsHaClusterLastVpStatusChangeCluster_Type())
cdmsHaClusterLastVpStatusChangeCluster.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterLastVpStatusChangeCluster.setStatus(_B)
_CdmsHaClusterLastStatusChangeVpAddrType_Type=InetAddressType
_CdmsHaClusterLastStatusChangeVpAddrType_Object=MibScalar
cdmsHaClusterLastStatusChangeVpAddrType=_CdmsHaClusterLastStatusChangeVpAddrType_Object((1,3,6,1,4,1,9,9,655,1,10,3,6),_CdmsHaClusterLastStatusChangeVpAddrType_Type())
cdmsHaClusterLastStatusChangeVpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterLastStatusChangeVpAddrType.setStatus(_B)
_CdmsHaClusterLastVpStatusChangeVpAddress_Type=InetAddress
_CdmsHaClusterLastVpStatusChangeVpAddress_Object=MibScalar
cdmsHaClusterLastVpStatusChangeVpAddress=_CdmsHaClusterLastVpStatusChangeVpAddress_Object((1,3,6,1,4,1,9,9,655,1,10,3,7),_CdmsHaClusterLastVpStatusChangeVpAddress_Type())
cdmsHaClusterLastVpStatusChangeVpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterLastVpStatusChangeVpAddress.setStatus(_B)
_CdmsHaClusterStatusHistory_ObjectIdentity=ObjectIdentity
cdmsHaClusterStatusHistory=_CdmsHaClusterStatusHistory_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,10,3,8))
class _CdmsHaClusterHistoryMaxRecords_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CdmsHaClusterHistoryMaxRecords_Type.__name__=_H
_CdmsHaClusterHistoryMaxRecords_Object=MibScalar
cdmsHaClusterHistoryMaxRecords=_CdmsHaClusterHistoryMaxRecords_Object((1,3,6,1,4,1,9,9,655,1,10,3,8,1),_CdmsHaClusterHistoryMaxRecords_Type())
cdmsHaClusterHistoryMaxRecords.setMaxAccess(_E)
if mibBuilder.loadTexts:cdmsHaClusterHistoryMaxRecords.setStatus(_B)
_CdmsHaClusterHistoryTable_Object=MibTable
cdmsHaClusterHistoryTable=_CdmsHaClusterHistoryTable_Object((1,3,6,1,4,1,9,9,655,1,10,3,8,2))
if mibBuilder.loadTexts:cdmsHaClusterHistoryTable.setStatus(_B)
_CdmsHaClusterHistoryEntry_Object=MibTableRow
cdmsHaClusterHistoryEntry=_CdmsHaClusterHistoryEntry_Object((1,3,6,1,4,1,9,9,655,1,10,3,8,2,1))
cdmsHaClusterHistoryEntry.setIndexNames((0,_A,_A8))
if mibBuilder.loadTexts:cdmsHaClusterHistoryEntry.setStatus(_B)
class _CdmsHaClusterHistId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CdmsHaClusterHistId_Type.__name__=_H
_CdmsHaClusterHistId_Object=MibTableColumn
cdmsHaClusterHistId=_CdmsHaClusterHistId_Object((1,3,6,1,4,1,9,9,655,1,10,3,8,2,1,1),_CdmsHaClusterHistId_Type())
cdmsHaClusterHistId.setMaxAccess(_D)
if mibBuilder.loadTexts:cdmsHaClusterHistId.setStatus(_B)
_CdmsHaClusterHistTimestamp_Type=TimeStamp
_CdmsHaClusterHistTimestamp_Object=MibTableColumn
cdmsHaClusterHistTimestamp=_CdmsHaClusterHistTimestamp_Object((1,3,6,1,4,1,9,9,655,1,10,3,8,2,1,2),_CdmsHaClusterHistTimestamp_Type())
cdmsHaClusterHistTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterHistTimestamp.setStatus(_B)
class _CdmsHaClusterHistClusterName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CdmsHaClusterHistClusterName_Type.__name__=_F
_CdmsHaClusterHistClusterName_Object=MibTableColumn
cdmsHaClusterHistClusterName=_CdmsHaClusterHistClusterName_Object((1,3,6,1,4,1,9,9,655,1,10,3,8,2,1,3),_CdmsHaClusterHistClusterName_Type())
cdmsHaClusterHistClusterName.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterHistClusterName.setStatus(_B)
_CdmsHaClusterHistNodeType_Type=CDmsElementType
_CdmsHaClusterHistNodeType_Object=MibTableColumn
cdmsHaClusterHistNodeType=_CdmsHaClusterHistNodeType_Object((1,3,6,1,4,1,9,9,655,1,10,3,8,2,1,4),_CdmsHaClusterHistNodeType_Type())
cdmsHaClusterHistNodeType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterHistNodeType.setStatus(_B)
_CdmsHaClusterHistNodeNewStatus_Type=CDmsFunctionalStatus
_CdmsHaClusterHistNodeNewStatus_Object=MibTableColumn
cdmsHaClusterHistNodeNewStatus=_CdmsHaClusterHistNodeNewStatus_Object((1,3,6,1,4,1,9,9,655,1,10,3,8,2,1,5),_CdmsHaClusterHistNodeNewStatus_Type())
cdmsHaClusterHistNodeNewStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterHistNodeNewStatus.setStatus(_B)
_CdmsHaClusterHistNodeAddrType_Type=InetAddressType
_CdmsHaClusterHistNodeAddrType_Object=MibTableColumn
cdmsHaClusterHistNodeAddrType=_CdmsHaClusterHistNodeAddrType_Object((1,3,6,1,4,1,9,9,655,1,10,3,8,2,1,6),_CdmsHaClusterHistNodeAddrType_Type())
cdmsHaClusterHistNodeAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterHistNodeAddrType.setStatus(_B)
_CdmsHaClusterHistNodeAddr_Type=InetAddress
_CdmsHaClusterHistNodeAddr_Object=MibTableColumn
cdmsHaClusterHistNodeAddr=_CdmsHaClusterHistNodeAddr_Object((1,3,6,1,4,1,9,9,655,1,10,3,8,2,1,7),_CdmsHaClusterHistNodeAddr_Type())
cdmsHaClusterHistNodeAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cdmsHaClusterHistNodeAddr.setStatus(_B)
_CdmsNotifControl_ObjectIdentity=ObjectIdentity
cdmsNotifControl=_CdmsNotifControl_ObjectIdentity((1,3,6,1,4,1,9,9,655,1,13))
class _CdmsMediaPlayerRegisteredEnable_Type(TruthValue):defaultValue=2
_CdmsMediaPlayerRegisteredEnable_Type.__name__=_G
_CdmsMediaPlayerRegisteredEnable_Object=MibScalar
cdmsMediaPlayerRegisteredEnable=_CdmsMediaPlayerRegisteredEnable_Object((1,3,6,1,4,1,9,9,655,1,13,1),_CdmsMediaPlayerRegisteredEnable_Type())
cdmsMediaPlayerRegisteredEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cdmsMediaPlayerRegisteredEnable.setStatus(_B)
class _CdmsMediaPlayerUpEnable_Type(TruthValue):defaultValue=2
_CdmsMediaPlayerUpEnable_Type.__name__=_G
_CdmsMediaPlayerUpEnable_Object=MibScalar
cdmsMediaPlayerUpEnable=_CdmsMediaPlayerUpEnable_Object((1,3,6,1,4,1,9,9,655,1,13,2),_CdmsMediaPlayerUpEnable_Type())
cdmsMediaPlayerUpEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cdmsMediaPlayerUpEnable.setStatus(_B)
class _CdmsMediaPlayerDownEnable_Type(TruthValue):defaultValue=2
_CdmsMediaPlayerDownEnable_Type.__name__=_G
_CdmsMediaPlayerDownEnable_Object=MibScalar
cdmsMediaPlayerDownEnable=_CdmsMediaPlayerDownEnable_Object((1,3,6,1,4,1,9,9,655,1,13,3),_CdmsMediaPlayerDownEnable_Type())
cdmsMediaPlayerDownEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cdmsMediaPlayerDownEnable.setStatus(_B)
class _CdmsMediaPlayerAddrTakenEnable_Type(TruthValue):defaultValue=2
_CdmsMediaPlayerAddrTakenEnable_Type.__name__=_G
_CdmsMediaPlayerAddrTakenEnable_Object=MibScalar
cdmsMediaPlayerAddrTakenEnable=_CdmsMediaPlayerAddrTakenEnable_Object((1,3,6,1,4,1,9,9,655,1,13,4),_CdmsMediaPlayerAddrTakenEnable_Type())
cdmsMediaPlayerAddrTakenEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cdmsMediaPlayerAddrTakenEnable.setStatus(_B)
class _CdmsHaClusterNodeUpEnable_Type(TruthValue):defaultValue=2
_CdmsHaClusterNodeUpEnable_Type.__name__=_G
_CdmsHaClusterNodeUpEnable_Object=MibScalar
cdmsHaClusterNodeUpEnable=_CdmsHaClusterNodeUpEnable_Object((1,3,6,1,4,1,9,9,655,1,13,5),_CdmsHaClusterNodeUpEnable_Type())
cdmsHaClusterNodeUpEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cdmsHaClusterNodeUpEnable.setStatus(_B)
class _CdmsHaClusterNodeDownEnable_Type(TruthValue):defaultValue=2
_CdmsHaClusterNodeDownEnable_Type.__name__=_G
_CdmsHaClusterNodeDownEnable_Object=MibScalar
cdmsHaClusterNodeDownEnable=_CdmsHaClusterNodeDownEnable_Object((1,3,6,1,4,1,9,9,655,1,13,6),_CdmsHaClusterNodeDownEnable_Type())
cdmsHaClusterNodeDownEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cdmsHaClusterNodeDownEnable.setStatus(_B)
class _CdmsHaClusterConfigChangeEnable_Type(TruthValue):defaultValue=2
_CdmsHaClusterConfigChangeEnable_Type.__name__=_G
_CdmsHaClusterConfigChangeEnable_Object=MibScalar
cdmsHaClusterConfigChangeEnable=_CdmsHaClusterConfigChangeEnable_Object((1,3,6,1,4,1,9,9,655,1,13,7),_CdmsHaClusterConfigChangeEnable_Type())
cdmsHaClusterConfigChangeEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cdmsHaClusterConfigChangeEnable.setStatus(_B)
_CiscoDmsMonitorMIBConform_ObjectIdentity=ObjectIdentity
ciscoDmsMonitorMIBConform=_CiscoDmsMonitorMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,655,2))
_CiscoDmsMonitorMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDmsMonitorMIBCompliances=_CiscoDmsMonitorMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,655,2,1))
_CiscoDmsMonitorMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDmsMonitorMIBGroups=_CiscoDmsMonitorMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,655,2,2))
ciscoDmsSystemGroup=ObjectGroup((1,3,6,1,4,1,9,9,655,2,2,1))
ciscoDmsSystemGroup.setObjects(*((_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:ciscoDmsSystemGroup.setStatus(_B)
ciscoDmsFeatureGroup=ObjectGroup((1,3,6,1,4,1,9,9,655,2,2,2))
ciscoDmsFeatureGroup.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:ciscoDmsFeatureGroup.setStatus(_B)
ciscoDmsFeatureAdvancedGroup=ObjectGroup((1,3,6,1,4,1,9,9,655,2,2,3))
ciscoDmsFeatureAdvancedGroup.setObjects((_A,_AI))
if mibBuilder.loadTexts:ciscoDmsFeatureAdvancedGroup.setStatus(_B)
ciscoDmsInventoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,655,2,2,4))
ciscoDmsInventoryGroup.setObjects(*((_A,_AJ),(_A,_L),(_A,_AK),(_A,_O),(_A,_I),(_A,_J),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:ciscoDmsInventoryGroup.setStatus(_B)
ciscoDmsServerGroup=ObjectGroup((1,3,6,1,4,1,9,9,655,2,2,5))
ciscoDmsServerGroup.setObjects(*((_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:ciscoDmsServerGroup.setStatus(_B)
ciscoDamGroup=ObjectGroup((1,3,6,1,4,1,9,9,655,2,2,6))
ciscoDamGroup.setObjects((_A,_AP))
if mibBuilder.loadTexts:ciscoDamGroup.setStatus(_B)
ciscoDmsSecurityGroup=ObjectGroup((1,3,6,1,4,1,9,9,655,2,2,7))
ciscoDmsSecurityGroup.setObjects(*((_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:ciscoDmsSecurityGroup.setStatus(_B)
ciscoDmsUserGroup=ObjectGroup((1,3,6,1,4,1,9,9,655,2,2,8))
ciscoDmsUserGroup.setObjects(*((_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:ciscoDmsUserGroup.setStatus(_B)
ciscoDmsEventGroup=ObjectGroup((1,3,6,1,4,1,9,9,655,2,2,9))
ciscoDmsEventGroup.setObjects(*((_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad)))
if mibBuilder.loadTexts:ciscoDmsEventGroup.setStatus(_B)
ciscoDmsNotificationCntlGroup=ObjectGroup((1,3,6,1,4,1,9,9,655,2,2,10))
ciscoDmsNotificationCntlGroup.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:ciscoDmsNotificationCntlGroup.setStatus(_N)
ciscoDmsHaGroup=ObjectGroup((1,3,6,1,4,1,9,9,655,2,2,13))
ciscoDmsHaGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_c)))
if mibBuilder.loadTexts:ciscoDmsHaGroup.setStatus(_B)
ciscoDmsHaAdvancedGroup=ObjectGroup((1,3,6,1,4,1,9,9,655,2,2,14))
ciscoDmsHaAdvancedGroup.setObjects(*((_A,_Aw),(_A,_M),(_A,_P),(_A,_Ax),(_A,_Q),(_A,_R),(_A,_c)))
if mibBuilder.loadTexts:ciscoDmsHaAdvancedGroup.setStatus(_B)
ciscoDmsNotificationCntlGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,655,2,2,15))
ciscoDmsNotificationCntlGroupRev1.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:ciscoDmsNotificationCntlGroupRev1.setStatus(_B)
ciscoDmsMediaPlayerRegistered=NotificationType((1,3,6,1,4,1,9,9,655,0,1))
ciscoDmsMediaPlayerRegistered.setObjects(*((_A,_L),(_A,_O),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ciscoDmsMediaPlayerRegistered.setStatus(_B)
ciscoDmsMediaPlayerUp=NotificationType((1,3,6,1,4,1,9,9,655,0,2))
ciscoDmsMediaPlayerUp.setObjects(*((_A,_L),(_A,_O),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ciscoDmsMediaPlayerUp.setStatus(_B)
ciscoDmsMediaPlayerDown=NotificationType((1,3,6,1,4,1,9,9,655,0,3))
ciscoDmsMediaPlayerDown.setObjects(*((_A,_L),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ciscoDmsMediaPlayerDown.setStatus(_B)
ciscoDmsMediaPlayerAddrTaken=NotificationType((1,3,6,1,4,1,9,9,655,0,4))
ciscoDmsMediaPlayerAddrTaken.setObjects(*((_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ciscoDmsMediaPlayerAddrTaken.setStatus(_B)
ciscoDmsHaClusterNodeUp=NotificationType((1,3,6,1,4,1,9,9,655,0,5))
ciscoDmsHaClusterNodeUp.setObjects(*((_A,_M),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ciscoDmsHaClusterNodeUp.setStatus(_B)
ciscoDmsHaClusterNodeDown=NotificationType((1,3,6,1,4,1,9,9,655,0,6))
ciscoDmsHaClusterNodeDown.setObjects(*((_A,_M),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ciscoDmsHaClusterNodeDown.setStatus(_B)
cdmsDmsHaClusterConfigChange=NotificationType((1,3,6,1,4,1,9,9,655,0,7))
cdmsDmsHaClusterConfigChange.setObjects((_A,_M))
if mibBuilder.loadTexts:cdmsDmsHaClusterConfigChange.setStatus(_B)
ciscoDmsNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,655,2,2,11))
ciscoDmsNotificationsGroup.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:ciscoDmsNotificationsGroup.setStatus(_N)
ciscoDmsAdvancedNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,655,2,2,12))
ciscoDmsAdvancedNotificationsGroup.setObjects((_A,_Ay))
if mibBuilder.loadTexts:ciscoDmsAdvancedNotificationsGroup.setStatus(_B)
ciscoDmsNotificationsGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,655,2,2,16))
ciscoDmsNotificationsGroupRev1.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_Az),(_A,_A_)))
if mibBuilder.loadTexts:ciscoDmsNotificationsGroupRev1.setStatus(_B)
ciscoDmsMonitorMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,655,2,1,1))
ciscoDmsMonitorMIBCompliance.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_r)))
if mibBuilder.loadTexts:ciscoDmsMonitorMIBCompliance.setStatus(_N)
ciscoDmsMonitorMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,655,2,1,2))
ciscoDmsMonitorMIBComplianceRev1.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_B3),(_A,_B4),(_A,_r),(_A,_q)))
if mibBuilder.loadTexts:ciscoDmsMonitorMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CDmsUserAuthenMethod':CDmsUserAuthenMethod,'CDmsServerType':CDmsServerType,'CDmsElementType':CDmsElementType,'CDmsFunctionalStatus':CDmsFunctionalStatus,'CDmsEmailAddress':CDmsEmailAddress,'CDmsLicensedFeature':CDmsLicensedFeature,'ciscoDigitalMediaSystemsMIB':ciscoDigitalMediaSystemsMIB,'ciscoDmsMonitorMIBNotifs':ciscoDmsMonitorMIBNotifs,_d:ciscoDmsMediaPlayerRegistered,_e:ciscoDmsMediaPlayerUp,_f:ciscoDmsMediaPlayerDown,_g:ciscoDmsMediaPlayerAddrTaken,_Az:ciscoDmsHaClusterNodeUp,_A_:ciscoDmsHaClusterNodeDown,_Ay:cdmsDmsHaClusterConfigChange,'ciscoDmsMonitorMIBObjects':ciscoDmsMonitorMIBObjects,'cdmsSystem':cdmsSystem,_A9:cdmsMajorVersion,_AA:cdmsMinorVersion,_AB:cdmsPatchVersion,_AC:cdmsAdministrator,'cdmsFeatures':cdmsFeatures,'cdmsFeatureSummary':cdmsFeatureSummary,_AD:cdmsLicensableFeatures,_AE:cdmsLicensedFeatures,_AF:cdmsLastLicenseUpdate,'cdmsLicensedFeatureTable':cdmsLicensedFeatureTable,'cdmsLicensedFeatureEntry':cdmsLicensedFeatureEntry,_u:cdmsLicensedFeature,_v:cdmsLicensedFeatureIndex,_AG:cdmsLicensedFeatureLimit,_AH:cdmsLicensedFeatureDescription,_AI:cdmsLicensedFeatureInstallDate,'cdmsLicensedFeatureLimitRev1':cdmsLicensedFeatureLimitRev1,'cdmsInventory':cdmsInventory,'cdmsInventoryGlobalCounters':cdmsInventoryGlobalCounters,_AJ:cdmsNumMediaIngestionDevices,_L:cdmsNumMediaPlayerDevices,_AK:cdmsNumVideoPortalDevices,'cdmsInventoryTable':cdmsInventoryTable,'cdmsInventoryEntry':cdmsInventoryEntry,_w:cdmsInventoryElementType,_x:cdmsInventoryElementId,_O:cdmsInventoryElementMacAddress,_I:cdmsInventoryElementAddrType,_J:cdmsInventoryElementAddress,_AL:cdmsInventoryElementMetadata,_AM:cdmsInventoryElementState,'cdmsServers':cdmsServers,'cdmsServerTable':cdmsServerTable,'cdmsServerEntry':cdmsServerEntry,_y:cdmsServerType,_z:cdmsServerAddrType,_A0:cdmsServerAddress,_AN:cdmsServerState,_AO:cdmsServerStatus,'cdmsDamServices':cdmsDamServices,'cdmsDamGlobalCounters':cdmsDamGlobalCounters,_AP:cdmsNumContentElements,_AR:cdmsNumAuthenRequestsApproved,_AS:cdmsNumAuthenRequestsDeclined,'cdmsSecurity':cdmsSecurity,'cdmsSecurityGlobalCounters':cdmsSecurityGlobalCounters,_AQ:cdmsNumAuthenRequests,'cdmsSecurityConfiguration':cdmsSecurityConfiguration,_AT:cdmsAuthenticationMode,'cdmsUserGroup':cdmsUserGroup,_AU:cdmsNumUsers,_AV:cdmsNumActiveDmmUsers,_AW:cdmsNumActiveVpUsers,_AX:cdmsLastUserLastChange,'cdmsEvents':cdmsEvents,'cdmsEventConfiguration':cdmsEventConfiguration,'cdmsEventStatistics':cdmsEventStatistics,_AY:cdmsNumEvents,_AZ:cdmsNumEventRate,_Aa:cdmsNumAlarms,_Ab:cdmsNumAlarmRate,_Ac:cdmsNumNotifications,_Ad:cdmsNumNotificationRate,'cdmsHa':cdmsHa,'cdmsHaClusterInfo':cdmsHaClusterInfo,_Ae:cdmsHaClusterEnabled,_Af:cdmsHaClusterName,'cdmsHaClusterComposition':cdmsHaClusterComposition,'cdmsHaDmmCluster':cdmsHaDmmCluster,_Ag:cdmsHaClusterNumTotalDmms,_Ah:cdmsHaClusterNumActiveDmms,_Ai:cdmsHaClusterDmmVipType,_Aj:cdmsHaClusterDmmVip,'cdmsHaDmmClusterMemberTable':cdmsHaDmmClusterMemberTable,'cdmsHaDmmClusterMemberEntry':cdmsHaDmmClusterMemberEntry,_A1:cdmsHaDmmClusterMemberAddrType,_A2:cdmsHaDmmClusterMemberAddress,_Ak:cdmsHaDmmClusterMemberIsPrimary,_Al:cdmsHaDmmClusterMemberOperState,'cdmsHaVpCluster':cdmsHaVpCluster,_Am:cdmsHaVpClusterNumClusters,'cdmsHaVpClusterMemberTable':cdmsHaVpClusterMemberTable,'cdmsHaVpClusterMemberEntry':cdmsHaVpClusterMemberEntry,_A3:cdmsHaVpClusterMemberClusterName,_A4:cdmsHaVpClusterMemberVipType,_A5:cdmsHaVpClusterMemberVip,_A6:cdmsHaVpClusterMemberAddrType,_A7:cdmsHaVpClusterMemberAddress,_An:cdmsHaVpClusterMemberIsPrimary,_Ao:cdmsHaVpClusterMemberOperState,'cdmsHaClusterStatus':cdmsHaClusterStatus,_Ap:cdmsHaClusterLastDmmStatusChangeTime,_Aq:cdmsHaClusterLastDmmStatusChangeAddrType,_Ar:cdmsHaClusterLastDmmStatusChangeAddress,_As:cdmsHaClusterLastVpStatusChangeTime,_At:cdmsHaClusterLastVpStatusChangeCluster,_Au:cdmsHaClusterLastStatusChangeVpAddrType,_Av:cdmsHaClusterLastVpStatusChangeVpAddress,'cdmsHaClusterStatusHistory':cdmsHaClusterStatusHistory,_c:cdmsHaClusterHistoryMaxRecords,'cdmsHaClusterHistoryTable':cdmsHaClusterHistoryTable,'cdmsHaClusterHistoryEntry':cdmsHaClusterHistoryEntry,_A8:cdmsHaClusterHistId,_Aw:cdmsHaClusterHistTimestamp,_M:cdmsHaClusterHistClusterName,_P:cdmsHaClusterHistNodeType,_Ax:cdmsHaClusterHistNodeNewStatus,_Q:cdmsHaClusterHistNodeAddrType,_R:cdmsHaClusterHistNodeAddr,'cdmsNotifControl':cdmsNotifControl,_V:cdmsMediaPlayerRegisteredEnable,_W:cdmsMediaPlayerUpEnable,_X:cdmsMediaPlayerDownEnable,_Y:cdmsMediaPlayerAddrTakenEnable,_Z:cdmsHaClusterNodeUpEnable,_a:cdmsHaClusterNodeDownEnable,_b:cdmsHaClusterConfigChangeEnable,'ciscoDmsMonitorMIBConform':ciscoDmsMonitorMIBConform,'ciscoDmsMonitorMIBCompliances':ciscoDmsMonitorMIBCompliances,'ciscoDmsMonitorMIBCompliance':ciscoDmsMonitorMIBCompliance,'ciscoDmsMonitorMIBComplianceRev1':ciscoDmsMonitorMIBComplianceRev1,'ciscoDmsMonitorMIBGroups':ciscoDmsMonitorMIBGroups,_h:ciscoDmsSystemGroup,_i:ciscoDmsFeatureGroup,_k:ciscoDmsFeatureAdvancedGroup,_j:ciscoDmsInventoryGroup,_l:ciscoDmsServerGroup,_m:ciscoDamGroup,_n:ciscoDmsSecurityGroup,_o:ciscoDmsUserGroup,_p:ciscoDmsEventGroup,_B1:ciscoDmsNotificationCntlGroup,_B2:ciscoDmsNotificationsGroup,_r:ciscoDmsAdvancedNotificationsGroup,_q:ciscoDmsHaGroup,_B0:ciscoDmsHaAdvancedGroup,_B3:ciscoDmsNotificationCntlGroupRev1,_B4:ciscoDmsNotificationsGroupRev1})