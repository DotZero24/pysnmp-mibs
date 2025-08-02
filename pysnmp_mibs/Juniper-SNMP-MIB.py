_AW='juniSnmpGeneralGroup4'
_AV='juniSnmpGeneralGroup'
_AU='juniSnmpGroup3'
_AT='juniSnmpGroup2'
_AS='juniSnmpGroup'
_AR='juniSnmpIntfCompMaskDisplay'
_AQ='juniSnmpIntfCompMask'
_AP='juniSnmpIntfCompEntryCompressed'
_AO='juniSnmpTrapSeverityFilter'
_AN='juniSnmpInterfaceMode'
_AM='juniSnmpAuthFailIdReason'
_AL='juniSnmpAuthFailIdCommunity'
_AK='juniSnmpAuthFailIdUdpPort'
_AJ='juniSnmpAuthFailIdIpAddress'
_AI='juniSnmpTrapCategory'
_AH='juniSnmpManagementApplicationIndex'
_AG='juniSnmpManagementApplicationRouterIndex'
_AF='juniSnmpIntfCompTableType'
_AE='JuniEnable'
_AD='juniSnmpTrapGroup3'
_AC='juniSnmpGeneralGroup3'
_AB='juniSnmpTrapGroup2'
_AA='juniSnmpGeneralGroup2'
_A9='juniSnmpTrapGroup'
_A8='juniSnmpManagementApplicationRowStatus'
_A7='juniSnmpAccessPermission'
_A6='juniSnmpTrapTotalProxyOut'
_A5='juniSnmpTrapTotalTrapsOut'
_A4='juniSnmpTrapAgentSnmpNotAbleDiscards'
_A3='juniSnmpTrapNoQueueResourceDiscards'
_A2='juniSnmpTrapNoMemoryDiscards'
_A1='juniSnmpTrapTotalTrapsDiscarded'
_A0='juniSnmpTrapProxyTrapsSubmitted'
_z='juniSnmpTrapLocalTrapsSubmitted'
_y='juniSnmpTrapTotalTrapsReceived'
_x='juniSnmpTrapHostNoResponseDiscards'
_w='juniSnmpTrapHostQueueFullDiscards'
_v='juniSnmpTrapHostBadEncodingDiscards'
_u='juniSnmpTrapHostQueueFull'
_t='juniSnmpTrapHostQueueDrainRate'
_s='juniSnmpTrapHostQueueSize'
_r='juniSnmpTrapHostIncludeLogVarbinds'
_q='juniSnmpTrapHostPingTimeOut'
_p='SnmpAdminString'
_o='juniSnmpProxyStatus'
_n='juniSnmpTrapGlobalSeverityFilter'
_m='juniSnmpTrapGlobalDiscards'
_l='juniSnmpTrapTrapSeverity'
_k='juniSnmpTrapHostSeverityFilter'
_j='juniSnmpTrapHostDiscards'
_i='juniSnmpCommunityView'
_h='juniSnmpCommunityAccessListName'
_g='not-accessible'
_f='TruthValue'
_e='juniSnmpIntfCompRestrictedDisplay'
_d='juniSnmpIntfCompRestricted'
_c='juniSnmpIntfCompEnhancedDisplay'
_b='juniSnmpIntfCompEnhanced'
_a='juniSnmpIntfCompCompressed'
_Z='juniSnmpCommunityAccessList'
_Y='juniSnmpCommunityPrivilege'
_X='juniSnmpCommunityRowStatus'
_W='accessible-for-notify'
_V='OctetString'
_U='juniSnmpCommunityName'
_T='juniSnmpAccessGroup'
_S='juniSnmpTrapHostSends'
_R='juniSnmpTrapHostFilter'
_Q='juniSnmpTrapHostProtocolVersion'
_P='juniSnmpTrapHostCommunity'
_O='juniSnmpTrapHostUdpPort'
_N='juniSnmpTrapHostRowStatus'
_M='juniSnmpTrapProxy'
_L='juniSnmpTrapSource'
_K='juniSnmpTrapGlobalFilter'
_J='juniSnmpMaxPduSize'
_I='juniSnmpTrapHostIpAddress'
_H='juniSnmpAuthFailGroup'
_G='read-write'
_F='Integer32'
_E='read-create'
_D='obsolete'
_C='read-only'
_B='current'
_A='Juniper-SNMP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_V,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniEnable,=mibBuilder.importSymbols('Juniper-TC',_AE)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_p)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_f)
juniSnmpMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,16))
if mibBuilder.loadTexts:juniSnmpMIB.setRevisions(('2008-09-30 06:59','2008-04-03 10:29','2006-09-18 08:09','2006-04-26 13:49','2006-01-01 00:00','2005-06-23 13:49','2005-05-12 21:53','2004-06-23 13:49','2004-01-05 16:09','2003-12-10 15:00','2003-02-05 22:24','2002-11-20 14:40','2002-08-15 20:18','2002-08-14 19:09','2001-11-07 17:09','2001-11-07 15:00','2001-05-08 12:06','2000-08-02 00:00','2000-05-09 00:00','1999-02-17 00:00'))
class JuniSnmpCommunityName(TextualConvention,OctetString):status=_B;displayHint='31a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
class JuniSnmpAccessListName(TextualConvention,OctetString):status=_B;displayHint='31a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
class JuniSnmpTrapMask(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class JuniTrapSeverity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('trapEmergency',0),('trapAlert',1),('trapCritical',2),('trapError',3),('trapWarning',4),('trapNotice',5),('trapInformational',6),('trapDebug',7)))
class JuniSnmpIntfCompRestrictedMask(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class JuniSnmpManagementApplicationIndex(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('eventMgr',1))
_JuniSnmpObjects_ObjectIdentity=ObjectIdentity
juniSnmpObjects=_JuniSnmpObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,16,1))
_JuniSnmpGeneral_ObjectIdentity=ObjectIdentity
juniSnmpGeneral=_JuniSnmpGeneral_ObjectIdentity((1,3,6,1,4,1,4874,2,2,16,1,1))
class _JuniSnmpMaxPduSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(484,8192))
_JuniSnmpMaxPduSize_Type.__name__=_F
_JuniSnmpMaxPduSize_Object=MibScalar
juniSnmpMaxPduSize=_JuniSnmpMaxPduSize_Object((1,3,6,1,4,1,4874,2,2,16,1,1,1),_JuniSnmpMaxPduSize_Type())
juniSnmpMaxPduSize.setMaxAccess(_G)
if mibBuilder.loadTexts:juniSnmpMaxPduSize.setStatus(_B)
class _JuniSnmpInterfaceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('verbose',1),('compress',2),('enhanced',3)))
_JuniSnmpInterfaceMode_Type.__name__=_F
_JuniSnmpInterfaceMode_Object=MibScalar
juniSnmpInterfaceMode=_JuniSnmpInterfaceMode_Object((1,3,6,1,4,1,4874,2,2,16,1,1,2),_JuniSnmpInterfaceMode_Type())
juniSnmpInterfaceMode.setMaxAccess(_G)
if mibBuilder.loadTexts:juniSnmpInterfaceMode.setStatus(_D)
_JuniSnmpInterfaceCompress_ObjectIdentity=ObjectIdentity
juniSnmpInterfaceCompress=_JuniSnmpInterfaceCompress_ObjectIdentity((1,3,6,1,4,1,4874,2,2,16,1,1,3))
class _JuniSnmpIntfCompCompressed_Type(TruthValue):defaultValue=2
_JuniSnmpIntfCompCompressed_Type.__name__=_f
_JuniSnmpIntfCompCompressed_Object=MibScalar
juniSnmpIntfCompCompressed=_JuniSnmpIntfCompCompressed_Object((1,3,6,1,4,1,4874,2,2,16,1,1,3,1),_JuniSnmpIntfCompCompressed_Type())
juniSnmpIntfCompCompressed.setMaxAccess(_G)
if mibBuilder.loadTexts:juniSnmpIntfCompCompressed.setStatus(_B)
class _JuniSnmpIntfCompEnhanced_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,16))
_JuniSnmpIntfCompEnhanced_Type.__name__=_V
_JuniSnmpIntfCompEnhanced_Object=MibScalar
juniSnmpIntfCompEnhanced=_JuniSnmpIntfCompEnhanced_Object((1,3,6,1,4,1,4874,2,2,16,1,1,3,2),_JuniSnmpIntfCompEnhanced_Type())
juniSnmpIntfCompEnhanced.setMaxAccess(_G)
if mibBuilder.loadTexts:juniSnmpIntfCompEnhanced.setStatus(_B)
class _JuniSnmpIntfCompEnhancedDisplay_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1000))
_JuniSnmpIntfCompEnhancedDisplay_Type.__name__=_V
_JuniSnmpIntfCompEnhancedDisplay_Object=MibScalar
juniSnmpIntfCompEnhancedDisplay=_JuniSnmpIntfCompEnhancedDisplay_Object((1,3,6,1,4,1,4874,2,2,16,1,1,3,3),_JuniSnmpIntfCompEnhancedDisplay_Type())
juniSnmpIntfCompEnhancedDisplay.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpIntfCompEnhancedDisplay.setStatus(_B)
_JuniSnmpIntfCompRestricted_Type=JuniSnmpIntfCompRestrictedMask
_JuniSnmpIntfCompRestricted_Object=MibScalar
juniSnmpIntfCompRestricted=_JuniSnmpIntfCompRestricted_Object((1,3,6,1,4,1,4874,2,2,16,1,1,3,4),_JuniSnmpIntfCompRestricted_Type())
juniSnmpIntfCompRestricted.setMaxAccess(_G)
if mibBuilder.loadTexts:juniSnmpIntfCompRestricted.setStatus(_B)
class _JuniSnmpIntfCompRestrictedDisplay_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_JuniSnmpIntfCompRestrictedDisplay_Type.__name__=_p
_JuniSnmpIntfCompRestrictedDisplay_Object=MibScalar
juniSnmpIntfCompRestrictedDisplay=_JuniSnmpIntfCompRestrictedDisplay_Object((1,3,6,1,4,1,4874,2,2,16,1,1,3,5),_JuniSnmpIntfCompRestrictedDisplay_Type())
juniSnmpIntfCompRestrictedDisplay.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpIntfCompRestrictedDisplay.setStatus(_B)
_JuniSnmpIntfCompTable_Object=MibTable
juniSnmpIntfCompTable=_JuniSnmpIntfCompTable_Object((1,3,6,1,4,1,4874,2,2,16,1,1,3,6))
if mibBuilder.loadTexts:juniSnmpIntfCompTable.setStatus(_B)
_JuniSnmpIntfCompEntry_Object=MibTableRow
juniSnmpIntfCompEntry=_JuniSnmpIntfCompEntry_Object((1,3,6,1,4,1,4874,2,2,16,1,1,3,6,1))
juniSnmpIntfCompEntry.setIndexNames((0,_A,_AF))
if mibBuilder.loadTexts:juniSnmpIntfCompEntry.setStatus(_B)
class _JuniSnmpIntfCompTableType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('others',0),('ifTables',1),('ifStackTables',2)))
_JuniSnmpIntfCompTableType_Type.__name__=_F
_JuniSnmpIntfCompTableType_Object=MibTableColumn
juniSnmpIntfCompTableType=_JuniSnmpIntfCompTableType_Object((1,3,6,1,4,1,4874,2,2,16,1,1,3,6,1,1),_JuniSnmpIntfCompTableType_Type())
juniSnmpIntfCompTableType.setMaxAccess(_g)
if mibBuilder.loadTexts:juniSnmpIntfCompTableType.setStatus(_B)
class _JuniSnmpIntfCompEntryCompressed_Type(TruthValue):defaultValue=2
_JuniSnmpIntfCompEntryCompressed_Type.__name__=_f
_JuniSnmpIntfCompEntryCompressed_Object=MibTableColumn
juniSnmpIntfCompEntryCompressed=_JuniSnmpIntfCompEntryCompressed_Object((1,3,6,1,4,1,4874,2,2,16,1,1,3,6,1,2),_JuniSnmpIntfCompEntryCompressed_Type())
juniSnmpIntfCompEntryCompressed.setMaxAccess(_G)
if mibBuilder.loadTexts:juniSnmpIntfCompEntryCompressed.setStatus(_B)
class _JuniSnmpIntfCompMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,16))
_JuniSnmpIntfCompMask_Type.__name__=_V
_JuniSnmpIntfCompMask_Object=MibTableColumn
juniSnmpIntfCompMask=_JuniSnmpIntfCompMask_Object((1,3,6,1,4,1,4874,2,2,16,1,1,3,6,1,3),_JuniSnmpIntfCompMask_Type())
juniSnmpIntfCompMask.setMaxAccess(_G)
if mibBuilder.loadTexts:juniSnmpIntfCompMask.setStatus(_B)
class _JuniSnmpIntfCompMaskDisplay_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1000))
_JuniSnmpIntfCompMaskDisplay_Type.__name__=_V
_JuniSnmpIntfCompMaskDisplay_Object=MibTableColumn
juniSnmpIntfCompMaskDisplay=_JuniSnmpIntfCompMaskDisplay_Object((1,3,6,1,4,1,4874,2,2,16,1,1,3,6,1,4),_JuniSnmpIntfCompMaskDisplay_Type())
juniSnmpIntfCompMaskDisplay.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpIntfCompMaskDisplay.setStatus(_B)
class _JuniSnmpProxyStatus_Type(JuniEnable):defaultValue=1
_JuniSnmpProxyStatus_Type.__name__=_AE
_JuniSnmpProxyStatus_Object=MibScalar
juniSnmpProxyStatus=_JuniSnmpProxyStatus_Object((1,3,6,1,4,1,4874,2,2,16,1,1,4),_JuniSnmpProxyStatus_Type())
juniSnmpProxyStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:juniSnmpProxyStatus.setStatus(_B)
class _JuniSnmpAccessPermission_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAccess',1),('readAccess',2),('readWriteAccess',3)))
_JuniSnmpAccessPermission_Type.__name__=_F
_JuniSnmpAccessPermission_Object=MibScalar
juniSnmpAccessPermission=_JuniSnmpAccessPermission_Object((1,3,6,1,4,1,4874,2,2,16,1,1,5),_JuniSnmpAccessPermission_Type())
juniSnmpAccessPermission.setMaxAccess(_G)
if mibBuilder.loadTexts:juniSnmpAccessPermission.setStatus(_B)
_JuniSnmpManagementApplicationTable_Object=MibTable
juniSnmpManagementApplicationTable=_JuniSnmpManagementApplicationTable_Object((1,3,6,1,4,1,4874,2,2,16,1,1,6))
if mibBuilder.loadTexts:juniSnmpManagementApplicationTable.setStatus(_B)
_JuniSnmpManagementApplicationEntry_Object=MibTableRow
juniSnmpManagementApplicationEntry=_JuniSnmpManagementApplicationEntry_Object((1,3,6,1,4,1,4874,2,2,16,1,1,6,1))
juniSnmpManagementApplicationEntry.setIndexNames((0,_A,_AG),(0,_A,_AH))
if mibBuilder.loadTexts:juniSnmpManagementApplicationEntry.setStatus(_B)
_JuniSnmpManagementApplicationRouterIndex_Type=Unsigned32
_JuniSnmpManagementApplicationRouterIndex_Object=MibTableColumn
juniSnmpManagementApplicationRouterIndex=_JuniSnmpManagementApplicationRouterIndex_Object((1,3,6,1,4,1,4874,2,2,16,1,1,6,1,1),_JuniSnmpManagementApplicationRouterIndex_Type())
juniSnmpManagementApplicationRouterIndex.setMaxAccess(_g)
if mibBuilder.loadTexts:juniSnmpManagementApplicationRouterIndex.setStatus(_B)
_JuniSnmpManagementApplicationIndex_Type=JuniSnmpManagementApplicationIndex
_JuniSnmpManagementApplicationIndex_Object=MibTableColumn
juniSnmpManagementApplicationIndex=_JuniSnmpManagementApplicationIndex_Object((1,3,6,1,4,1,4874,2,2,16,1,1,6,1,2),_JuniSnmpManagementApplicationIndex_Type())
juniSnmpManagementApplicationIndex.setMaxAccess(_g)
if mibBuilder.loadTexts:juniSnmpManagementApplicationIndex.setStatus(_B)
_JuniSnmpManagementApplicationRowStatus_Type=RowStatus
_JuniSnmpManagementApplicationRowStatus_Object=MibTableColumn
juniSnmpManagementApplicationRowStatus=_JuniSnmpManagementApplicationRowStatus_Object((1,3,6,1,4,1,4874,2,2,16,1,1,6,1,3),_JuniSnmpManagementApplicationRowStatus_Type())
juniSnmpManagementApplicationRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpManagementApplicationRowStatus.setStatus(_B)
_JuniSnmpCommunity_ObjectIdentity=ObjectIdentity
juniSnmpCommunity=_JuniSnmpCommunity_ObjectIdentity((1,3,6,1,4,1,4874,2,2,16,1,2))
_JuniSnmpCommunityTable_Object=MibTable
juniSnmpCommunityTable=_JuniSnmpCommunityTable_Object((1,3,6,1,4,1,4874,2,2,16,1,2,1))
if mibBuilder.loadTexts:juniSnmpCommunityTable.setStatus(_B)
_JuniSnmpCommunityEntry_Object=MibTableRow
juniSnmpCommunityEntry=_JuniSnmpCommunityEntry_Object((1,3,6,1,4,1,4874,2,2,16,1,2,1,1))
juniSnmpCommunityEntry.setIndexNames((1,_A,_U))
if mibBuilder.loadTexts:juniSnmpCommunityEntry.setStatus(_B)
_JuniSnmpCommunityName_Type=JuniSnmpCommunityName
_JuniSnmpCommunityName_Object=MibTableColumn
juniSnmpCommunityName=_JuniSnmpCommunityName_Object((1,3,6,1,4,1,4874,2,2,16,1,2,1,1,1),_JuniSnmpCommunityName_Type())
juniSnmpCommunityName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpCommunityName.setStatus(_B)
_JuniSnmpCommunityRowStatus_Type=RowStatus
_JuniSnmpCommunityRowStatus_Object=MibTableColumn
juniSnmpCommunityRowStatus=_JuniSnmpCommunityRowStatus_Object((1,3,6,1,4,1,4874,2,2,16,1,2,1,1,2),_JuniSnmpCommunityRowStatus_Type())
juniSnmpCommunityRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpCommunityRowStatus.setStatus(_B)
class _JuniSnmpCommunityPrivilege_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('readOnly',1),('readWrite',2),('admin',3)))
_JuniSnmpCommunityPrivilege_Type.__name__=_F
_JuniSnmpCommunityPrivilege_Object=MibTableColumn
juniSnmpCommunityPrivilege=_JuniSnmpCommunityPrivilege_Object((1,3,6,1,4,1,4874,2,2,16,1,2,1,1,3),_JuniSnmpCommunityPrivilege_Type())
juniSnmpCommunityPrivilege.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpCommunityPrivilege.setStatus(_B)
class _JuniSnmpCommunityAccessList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_JuniSnmpCommunityAccessList_Type.__name__=_F
_JuniSnmpCommunityAccessList_Object=MibTableColumn
juniSnmpCommunityAccessList=_JuniSnmpCommunityAccessList_Object((1,3,6,1,4,1,4874,2,2,16,1,2,1,1,4),_JuniSnmpCommunityAccessList_Type())
juniSnmpCommunityAccessList.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpCommunityAccessList.setStatus(_B)
_JuniSnmpCommunityAccessListName_Type=JuniSnmpAccessListName
_JuniSnmpCommunityAccessListName_Object=MibTableColumn
juniSnmpCommunityAccessListName=_JuniSnmpCommunityAccessListName_Object((1,3,6,1,4,1,4874,2,2,16,1,2,1,1,5),_JuniSnmpCommunityAccessListName_Type())
juniSnmpCommunityAccessListName.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpCommunityAccessListName.setStatus(_B)
class _JuniSnmpCommunityView_Type(SnmpAdminString):defaultValue=OctetString('user');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_JuniSnmpCommunityView_Type.__name__=_p
_JuniSnmpCommunityView_Object=MibTableColumn
juniSnmpCommunityView=_JuniSnmpCommunityView_Object((1,3,6,1,4,1,4874,2,2,16,1,2,1,1,6),_JuniSnmpCommunityView_Type())
juniSnmpCommunityView.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpCommunityView.setStatus(_B)
_JuniSnmpTrap_ObjectIdentity=ObjectIdentity
juniSnmpTrap=_JuniSnmpTrap_ObjectIdentity((1,3,6,1,4,1,4874,2,2,16,1,3))
_JuniSnmpTrapGlobalFilter_Type=JuniSnmpTrapMask
_JuniSnmpTrapGlobalFilter_Object=MibScalar
juniSnmpTrapGlobalFilter=_JuniSnmpTrapGlobalFilter_Object((1,3,6,1,4,1,4874,2,2,16,1,3,1),_JuniSnmpTrapGlobalFilter_Type())
juniSnmpTrapGlobalFilter.setMaxAccess(_G)
if mibBuilder.loadTexts:juniSnmpTrapGlobalFilter.setStatus(_B)
class _JuniSnmpTrapSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniSnmpTrapSource_Type.__name__=_F
_JuniSnmpTrapSource_Object=MibScalar
juniSnmpTrapSource=_JuniSnmpTrapSource_Object((1,3,6,1,4,1,4874,2,2,16,1,3,2),_JuniSnmpTrapSource_Type())
juniSnmpTrapSource.setMaxAccess(_G)
if mibBuilder.loadTexts:juniSnmpTrapSource.setStatus(_B)
_JuniSnmpTrapHostTable_Object=MibTable
juniSnmpTrapHostTable=_JuniSnmpTrapHostTable_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3))
if mibBuilder.loadTexts:juniSnmpTrapHostTable.setStatus(_B)
_JuniSnmpTrapHostEntry_Object=MibTableRow
juniSnmpTrapHostEntry=_JuniSnmpTrapHostEntry_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1))
juniSnmpTrapHostEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:juniSnmpTrapHostEntry.setStatus(_B)
_JuniSnmpTrapHostIpAddress_Type=IpAddress
_JuniSnmpTrapHostIpAddress_Object=MibTableColumn
juniSnmpTrapHostIpAddress=_JuniSnmpTrapHostIpAddress_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,1),_JuniSnmpTrapHostIpAddress_Type())
juniSnmpTrapHostIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpTrapHostIpAddress.setStatus(_B)
_JuniSnmpTrapHostRowStatus_Type=RowStatus
_JuniSnmpTrapHostRowStatus_Object=MibTableColumn
juniSnmpTrapHostRowStatus=_JuniSnmpTrapHostRowStatus_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,2),_JuniSnmpTrapHostRowStatus_Type())
juniSnmpTrapHostRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpTrapHostRowStatus.setStatus(_B)
class _JuniSnmpTrapHostUdpPort_Type(Integer32):defaultValue=162;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JuniSnmpTrapHostUdpPort_Type.__name__=_F
_JuniSnmpTrapHostUdpPort_Object=MibTableColumn
juniSnmpTrapHostUdpPort=_JuniSnmpTrapHostUdpPort_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,3),_JuniSnmpTrapHostUdpPort_Type())
juniSnmpTrapHostUdpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpTrapHostUdpPort.setStatus(_B)
_JuniSnmpTrapHostCommunity_Type=JuniSnmpCommunityName
_JuniSnmpTrapHostCommunity_Object=MibTableColumn
juniSnmpTrapHostCommunity=_JuniSnmpTrapHostCommunity_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,4),_JuniSnmpTrapHostCommunity_Type())
juniSnmpTrapHostCommunity.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpTrapHostCommunity.setStatus(_B)
class _JuniSnmpTrapHostProtocolVersion_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('v1',0),('v2c',1),('v3',2)))
_JuniSnmpTrapHostProtocolVersion_Type.__name__=_F
_JuniSnmpTrapHostProtocolVersion_Object=MibTableColumn
juniSnmpTrapHostProtocolVersion=_JuniSnmpTrapHostProtocolVersion_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,5),_JuniSnmpTrapHostProtocolVersion_Type())
juniSnmpTrapHostProtocolVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpTrapHostProtocolVersion.setStatus(_B)
_JuniSnmpTrapHostFilter_Type=JuniSnmpTrapMask
_JuniSnmpTrapHostFilter_Object=MibTableColumn
juniSnmpTrapHostFilter=_JuniSnmpTrapHostFilter_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,6),_JuniSnmpTrapHostFilter_Type())
juniSnmpTrapHostFilter.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpTrapHostFilter.setStatus(_B)
_JuniSnmpTrapHostSends_Type=Counter32
_JuniSnmpTrapHostSends_Object=MibTableColumn
juniSnmpTrapHostSends=_JuniSnmpTrapHostSends_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,7),_JuniSnmpTrapHostSends_Type())
juniSnmpTrapHostSends.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpTrapHostSends.setStatus(_B)
_JuniSnmpTrapHostDiscards_Type=Counter32
_JuniSnmpTrapHostDiscards_Object=MibTableColumn
juniSnmpTrapHostDiscards=_JuniSnmpTrapHostDiscards_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,8),_JuniSnmpTrapHostDiscards_Type())
juniSnmpTrapHostDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpTrapHostDiscards.setStatus(_B)
_JuniSnmpTrapHostSeverityFilter_Type=JuniTrapSeverity
_JuniSnmpTrapHostSeverityFilter_Object=MibTableColumn
juniSnmpTrapHostSeverityFilter=_JuniSnmpTrapHostSeverityFilter_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,9),_JuniSnmpTrapHostSeverityFilter_Type())
juniSnmpTrapHostSeverityFilter.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpTrapHostSeverityFilter.setStatus(_B)
class _JuniSnmpTrapHostPingTimeOut_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90))
_JuniSnmpTrapHostPingTimeOut_Type.__name__=_F
_JuniSnmpTrapHostPingTimeOut_Object=MibTableColumn
juniSnmpTrapHostPingTimeOut=_JuniSnmpTrapHostPingTimeOut_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,10),_JuniSnmpTrapHostPingTimeOut_Type())
juniSnmpTrapHostPingTimeOut.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpTrapHostPingTimeOut.setStatus(_B)
if mibBuilder.loadTexts:juniSnmpTrapHostPingTimeOut.setUnits('Minutes')
class _JuniSnmpTrapHostIncludeLogVarbinds_Type(TruthValue):defaultValue=2
_JuniSnmpTrapHostIncludeLogVarbinds_Type.__name__=_f
_JuniSnmpTrapHostIncludeLogVarbinds_Object=MibTableColumn
juniSnmpTrapHostIncludeLogVarbinds=_JuniSnmpTrapHostIncludeLogVarbinds_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,11),_JuniSnmpTrapHostIncludeLogVarbinds_Type())
juniSnmpTrapHostIncludeLogVarbinds.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpTrapHostIncludeLogVarbinds.setStatus(_B)
class _JuniSnmpTrapHostQueueSize_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,2147483647))
_JuniSnmpTrapHostQueueSize_Type.__name__=_F
_JuniSnmpTrapHostQueueSize_Object=MibTableColumn
juniSnmpTrapHostQueueSize=_JuniSnmpTrapHostQueueSize_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,12),_JuniSnmpTrapHostQueueSize_Type())
juniSnmpTrapHostQueueSize.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpTrapHostQueueSize.setStatus(_B)
class _JuniSnmpTrapHostQueueDrainRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniSnmpTrapHostQueueDrainRate_Type.__name__=_F
_JuniSnmpTrapHostQueueDrainRate_Object=MibTableColumn
juniSnmpTrapHostQueueDrainRate=_JuniSnmpTrapHostQueueDrainRate_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,13),_JuniSnmpTrapHostQueueDrainRate_Type())
juniSnmpTrapHostQueueDrainRate.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpTrapHostQueueDrainRate.setStatus(_B)
class _JuniSnmpTrapHostQueueFull_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dropLastIn',0),('dropFirstIn',1)))
_JuniSnmpTrapHostQueueFull_Type.__name__=_F
_JuniSnmpTrapHostQueueFull_Object=MibTableColumn
juniSnmpTrapHostQueueFull=_JuniSnmpTrapHostQueueFull_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,14),_JuniSnmpTrapHostQueueFull_Type())
juniSnmpTrapHostQueueFull.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSnmpTrapHostQueueFull.setStatus(_B)
_JuniSnmpTrapHostBadEncodingDiscards_Type=Counter32
_JuniSnmpTrapHostBadEncodingDiscards_Object=MibTableColumn
juniSnmpTrapHostBadEncodingDiscards=_JuniSnmpTrapHostBadEncodingDiscards_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,15),_JuniSnmpTrapHostBadEncodingDiscards_Type())
juniSnmpTrapHostBadEncodingDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpTrapHostBadEncodingDiscards.setStatus(_B)
_JuniSnmpTrapHostQueueFullDiscards_Type=Counter32
_JuniSnmpTrapHostQueueFullDiscards_Object=MibTableColumn
juniSnmpTrapHostQueueFullDiscards=_JuniSnmpTrapHostQueueFullDiscards_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,16),_JuniSnmpTrapHostQueueFullDiscards_Type())
juniSnmpTrapHostQueueFullDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpTrapHostQueueFullDiscards.setStatus(_B)
_JuniSnmpTrapHostNoResponseDiscards_Type=Counter32
_JuniSnmpTrapHostNoResponseDiscards_Object=MibTableColumn
juniSnmpTrapHostNoResponseDiscards=_JuniSnmpTrapHostNoResponseDiscards_Object((1,3,6,1,4,1,4874,2,2,16,1,3,3,1,17),_JuniSnmpTrapHostNoResponseDiscards_Type())
juniSnmpTrapHostNoResponseDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpTrapHostNoResponseDiscards.setStatus(_B)
_JuniSnmpTrapProxy_Type=TruthValue
_JuniSnmpTrapProxy_Object=MibScalar
juniSnmpTrapProxy=_JuniSnmpTrapProxy_Object((1,3,6,1,4,1,4874,2,2,16,1,3,4),_JuniSnmpTrapProxy_Type())
juniSnmpTrapProxy.setMaxAccess(_G)
if mibBuilder.loadTexts:juniSnmpTrapProxy.setStatus(_B)
_JuniSnmpTrapTrapSeverity_Type=JuniTrapSeverity
_JuniSnmpTrapTrapSeverity_Object=MibScalar
juniSnmpTrapTrapSeverity=_JuniSnmpTrapTrapSeverity_Object((1,3,6,1,4,1,4874,2,2,16,1,3,5),_JuniSnmpTrapTrapSeverity_Type())
juniSnmpTrapTrapSeverity.setMaxAccess(_W)
if mibBuilder.loadTexts:juniSnmpTrapTrapSeverity.setStatus(_B)
_JuniSnmpTrapGlobalDiscards_Type=Counter32
_JuniSnmpTrapGlobalDiscards_Object=MibScalar
juniSnmpTrapGlobalDiscards=_JuniSnmpTrapGlobalDiscards_Object((1,3,6,1,4,1,4874,2,2,16,1,3,6),_JuniSnmpTrapGlobalDiscards_Type())
juniSnmpTrapGlobalDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpTrapGlobalDiscards.setStatus(_B)
_JuniSnmpTrapGlobalSeverityFilter_Type=JuniTrapSeverity
_JuniSnmpTrapGlobalSeverityFilter_Object=MibScalar
juniSnmpTrapGlobalSeverityFilter=_JuniSnmpTrapGlobalSeverityFilter_Object((1,3,6,1,4,1,4874,2,2,16,1,3,7),_JuniSnmpTrapGlobalSeverityFilter_Type())
juniSnmpTrapGlobalSeverityFilter.setMaxAccess(_G)
if mibBuilder.loadTexts:juniSnmpTrapGlobalSeverityFilter.setStatus(_B)
_JuniSnmpTrapTotalTrapsReceived_Type=Counter32
_JuniSnmpTrapTotalTrapsReceived_Object=MibScalar
juniSnmpTrapTotalTrapsReceived=_JuniSnmpTrapTotalTrapsReceived_Object((1,3,6,1,4,1,4874,2,2,16,1,3,8),_JuniSnmpTrapTotalTrapsReceived_Type())
juniSnmpTrapTotalTrapsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpTrapTotalTrapsReceived.setStatus(_B)
_JuniSnmpTrapLocalTrapsSubmitted_Type=Counter32
_JuniSnmpTrapLocalTrapsSubmitted_Object=MibScalar
juniSnmpTrapLocalTrapsSubmitted=_JuniSnmpTrapLocalTrapsSubmitted_Object((1,3,6,1,4,1,4874,2,2,16,1,3,9),_JuniSnmpTrapLocalTrapsSubmitted_Type())
juniSnmpTrapLocalTrapsSubmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpTrapLocalTrapsSubmitted.setStatus(_B)
_JuniSnmpTrapProxyTrapsSubmitted_Type=Counter32
_JuniSnmpTrapProxyTrapsSubmitted_Object=MibScalar
juniSnmpTrapProxyTrapsSubmitted=_JuniSnmpTrapProxyTrapsSubmitted_Object((1,3,6,1,4,1,4874,2,2,16,1,3,10),_JuniSnmpTrapProxyTrapsSubmitted_Type())
juniSnmpTrapProxyTrapsSubmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpTrapProxyTrapsSubmitted.setStatus(_B)
_JuniSnmpTrapTotalTrapsDiscarded_Type=Counter32
_JuniSnmpTrapTotalTrapsDiscarded_Object=MibScalar
juniSnmpTrapTotalTrapsDiscarded=_JuniSnmpTrapTotalTrapsDiscarded_Object((1,3,6,1,4,1,4874,2,2,16,1,3,11),_JuniSnmpTrapTotalTrapsDiscarded_Type())
juniSnmpTrapTotalTrapsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpTrapTotalTrapsDiscarded.setStatus(_B)
_JuniSnmpTrapNoMemoryDiscards_Type=Counter32
_JuniSnmpTrapNoMemoryDiscards_Object=MibScalar
juniSnmpTrapNoMemoryDiscards=_JuniSnmpTrapNoMemoryDiscards_Object((1,3,6,1,4,1,4874,2,2,16,1,3,12),_JuniSnmpTrapNoMemoryDiscards_Type())
juniSnmpTrapNoMemoryDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpTrapNoMemoryDiscards.setStatus(_B)
_JuniSnmpTrapNoQueueResourceDiscards_Type=Counter32
_JuniSnmpTrapNoQueueResourceDiscards_Object=MibScalar
juniSnmpTrapNoQueueResourceDiscards=_JuniSnmpTrapNoQueueResourceDiscards_Object((1,3,6,1,4,1,4874,2,2,16,1,3,13),_JuniSnmpTrapNoQueueResourceDiscards_Type())
juniSnmpTrapNoQueueResourceDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpTrapNoQueueResourceDiscards.setStatus(_B)
_JuniSnmpTrapAgentSnmpNotAbleDiscards_Type=Counter32
_JuniSnmpTrapAgentSnmpNotAbleDiscards_Object=MibScalar
juniSnmpTrapAgentSnmpNotAbleDiscards=_JuniSnmpTrapAgentSnmpNotAbleDiscards_Object((1,3,6,1,4,1,4874,2,2,16,1,3,14),_JuniSnmpTrapAgentSnmpNotAbleDiscards_Type())
juniSnmpTrapAgentSnmpNotAbleDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpTrapAgentSnmpNotAbleDiscards.setStatus(_B)
_JuniSnmpTrapTotalTrapsOut_Type=Counter32
_JuniSnmpTrapTotalTrapsOut_Object=MibScalar
juniSnmpTrapTotalTrapsOut=_JuniSnmpTrapTotalTrapsOut_Object((1,3,6,1,4,1,4874,2,2,16,1,3,15),_JuniSnmpTrapTotalTrapsOut_Type())
juniSnmpTrapTotalTrapsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpTrapTotalTrapsOut.setStatus(_B)
_JuniSnmpTrapTotalProxyOut_Type=Counter32
_JuniSnmpTrapTotalProxyOut_Object=MibScalar
juniSnmpTrapTotalProxyOut=_JuniSnmpTrapTotalProxyOut_Object((1,3,6,1,4,1,4874,2,2,16,1,3,16),_JuniSnmpTrapTotalProxyOut_Type())
juniSnmpTrapTotalProxyOut.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSnmpTrapTotalProxyOut.setStatus(_B)
_JuniSnmpTrapSeverityFilterTable_Object=MibTable
juniSnmpTrapSeverityFilterTable=_JuniSnmpTrapSeverityFilterTable_Object((1,3,6,1,4,1,4874,2,2,16,1,3,17))
if mibBuilder.loadTexts:juniSnmpTrapSeverityFilterTable.setStatus(_B)
_JuniSnmpTrapSeverityFilterEntry_Object=MibTableRow
juniSnmpTrapSeverityFilterEntry=_JuniSnmpTrapSeverityFilterEntry_Object((1,3,6,1,4,1,4874,2,2,16,1,3,17,1))
juniSnmpTrapSeverityFilterEntry.setIndexNames((0,_A,_AI))
if mibBuilder.loadTexts:juniSnmpTrapSeverityFilterEntry.setStatus(_B)
class _JuniSnmpTrapCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_JuniSnmpTrapCategory_Type.__name__=_F
_JuniSnmpTrapCategory_Object=MibTableColumn
juniSnmpTrapCategory=_JuniSnmpTrapCategory_Object((1,3,6,1,4,1,4874,2,2,16,1,3,17,1,1),_JuniSnmpTrapCategory_Type())
juniSnmpTrapCategory.setMaxAccess(_g)
if mibBuilder.loadTexts:juniSnmpTrapCategory.setStatus(_B)
_JuniSnmpTrapSeverityFilter_Type=JuniTrapSeverity
_JuniSnmpTrapSeverityFilter_Object=MibTableColumn
juniSnmpTrapSeverityFilter=_JuniSnmpTrapSeverityFilter_Object((1,3,6,1,4,1,4874,2,2,16,1,3,17,1,2),_JuniSnmpTrapSeverityFilter_Type())
juniSnmpTrapSeverityFilter.setMaxAccess(_G)
if mibBuilder.loadTexts:juniSnmpTrapSeverityFilter.setStatus(_B)
_JuniSnmpAuthFailId_ObjectIdentity=ObjectIdentity
juniSnmpAuthFailId=_JuniSnmpAuthFailId_ObjectIdentity((1,3,6,1,4,1,4874,2,2,16,1,4))
_JuniSnmpAuthFailIdIpAddress_Type=IpAddress
_JuniSnmpAuthFailIdIpAddress_Object=MibScalar
juniSnmpAuthFailIdIpAddress=_JuniSnmpAuthFailIdIpAddress_Object((1,3,6,1,4,1,4874,2,2,16,1,4,1),_JuniSnmpAuthFailIdIpAddress_Type())
juniSnmpAuthFailIdIpAddress.setMaxAccess(_W)
if mibBuilder.loadTexts:juniSnmpAuthFailIdIpAddress.setStatus(_B)
_JuniSnmpAuthFailIdUdpPort_Type=Integer32
_JuniSnmpAuthFailIdUdpPort_Object=MibScalar
juniSnmpAuthFailIdUdpPort=_JuniSnmpAuthFailIdUdpPort_Object((1,3,6,1,4,1,4874,2,2,16,1,4,2),_JuniSnmpAuthFailIdUdpPort_Type())
juniSnmpAuthFailIdUdpPort.setMaxAccess(_W)
if mibBuilder.loadTexts:juniSnmpAuthFailIdUdpPort.setStatus(_B)
_JuniSnmpAuthFailIdCommunity_Type=OctetString
_JuniSnmpAuthFailIdCommunity_Object=MibScalar
juniSnmpAuthFailIdCommunity=_JuniSnmpAuthFailIdCommunity_Object((1,3,6,1,4,1,4874,2,2,16,1,4,3),_JuniSnmpAuthFailIdCommunity_Type())
juniSnmpAuthFailIdCommunity.setMaxAccess(_W)
if mibBuilder.loadTexts:juniSnmpAuthFailIdCommunity.setStatus(_B)
class _JuniSnmpAuthFailIdReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('other',0),('badCommunityName',1),('badCommmunityUse',2),('hostDenied',3)))
_JuniSnmpAuthFailIdReason_Type.__name__=_F
_JuniSnmpAuthFailIdReason_Object=MibScalar
juniSnmpAuthFailIdReason=_JuniSnmpAuthFailIdReason_Object((1,3,6,1,4,1,4874,2,2,16,1,4,4),_JuniSnmpAuthFailIdReason_Type())
juniSnmpAuthFailIdReason.setMaxAccess(_W)
if mibBuilder.loadTexts:juniSnmpAuthFailIdReason.setStatus(_B)
_JuniSnmpConformance_ObjectIdentity=ObjectIdentity
juniSnmpConformance=_JuniSnmpConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,16,2))
_JuniSnmpCompliances_ObjectIdentity=ObjectIdentity
juniSnmpCompliances=_JuniSnmpCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,16,2,1))
_JuniSnmpGroups_ObjectIdentity=ObjectIdentity
juniSnmpGroups=_JuniSnmpGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,16,2,2))
juniSnmpGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,16,2,2,1))
juniSnmpGroup.setObjects(*((_A,_J),(_A,_U),(_A,_X),(_A,_Y),(_A,_Z),(_A,_K),(_A,_L),(_A,_M),(_A,_I),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniSnmpGroup.setStatus(_D)
juniSnmpAuthFailGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,16,2,2,2))
juniSnmpAuthFailGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:juniSnmpAuthFailGroup.setStatus(_B)
juniSnmpGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,16,2,2,3))
juniSnmpGroup2.setObjects(*((_A,_J),(_A,_U),(_A,_X),(_A,_Y),(_A,_Z),(_A,_h),(_A,_i),(_A,_K),(_A,_L),(_A,_M),(_A,_I),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniSnmpGroup2.setStatus(_D)
juniSnmpGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,16,2,2,4))
juniSnmpGroup3.setObjects(*((_A,_J),(_A,_AN),(_A,_U),(_A,_X),(_A,_Y),(_A,_Z),(_A,_h),(_A,_i),(_A,_K),(_A,_L),(_A,_M),(_A,_I),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniSnmpGroup3.setStatus(_D)
juniSnmpGeneralGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,16,2,2,5))
juniSnmpGeneralGroup.setObjects(*((_A,_J),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:juniSnmpGeneralGroup.setStatus(_D)
juniSnmpAccessGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,16,2,2,6))
juniSnmpAccessGroup.setObjects(*((_A,_U),(_A,_X),(_A,_Y),(_A,_Z),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:juniSnmpAccessGroup.setStatus(_B)
juniSnmpTrapGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,16,2,2,7))
juniSnmpTrapGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_I),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:juniSnmpTrapGroup.setStatus(_D)
juniSnmpGeneralGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,16,2,2,8))
juniSnmpGeneralGroup2.setObjects(*((_A,_J),(_A,_o),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:juniSnmpGeneralGroup2.setStatus(_D)
juniSnmpTrapGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,16,2,2,9))
juniSnmpTrapGroup2.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_I),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_j),(_A,_k),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_l),(_A,_m),(_A,_n),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:juniSnmpTrapGroup2.setStatus(_D)
juniSnmpGeneralGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,16,2,2,10))
juniSnmpGeneralGroup3.setObjects(*((_A,_J),(_A,_o),(_A,_A7),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_A8)))
if mibBuilder.loadTexts:juniSnmpGeneralGroup3.setStatus(_D)
juniSnmpTrapGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,16,2,2,11))
juniSnmpTrapGroup3.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_I),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_j),(_A,_k),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_l),(_A,_m),(_A,_n),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_AO)))
if mibBuilder.loadTexts:juniSnmpTrapGroup3.setStatus(_B)
juniSnmpGeneralGroup4=ObjectGroup((1,3,6,1,4,1,4874,2,2,16,2,2,12))
juniSnmpGeneralGroup4.setObjects(*((_A,_J),(_A,_o),(_A,_A7),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_A8),(_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:juniSnmpGeneralGroup4.setStatus(_B)
juniSnmpCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,16,2,1,1))
juniSnmpCompliance.setObjects(*((_A,_AS),(_A,_H)))
if mibBuilder.loadTexts:juniSnmpCompliance.setStatus(_D)
juniSnmpCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,16,2,1,2))
juniSnmpCompliance2.setObjects(*((_A,_AT),(_A,_H)))
if mibBuilder.loadTexts:juniSnmpCompliance2.setStatus(_D)
juniSnmpCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,16,2,1,3))
juniSnmpCompliance3.setObjects(*((_A,_AU),(_A,_H)))
if mibBuilder.loadTexts:juniSnmpCompliance3.setStatus(_D)
juniSnmpCompliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,16,2,1,4))
juniSnmpCompliance4.setObjects(*((_A,_AV),(_A,_T),(_A,_A9),(_A,_H)))
if mibBuilder.loadTexts:juniSnmpCompliance4.setStatus(_D)
juniSnmpCompliance5=ModuleCompliance((1,3,6,1,4,1,4874,2,2,16,2,1,5))
juniSnmpCompliance5.setObjects(*((_A,_AA),(_A,_T),(_A,_A9),(_A,_H)))
if mibBuilder.loadTexts:juniSnmpCompliance5.setStatus(_D)
juniSnmpCompliance6=ModuleCompliance((1,3,6,1,4,1,4874,2,2,16,2,1,6))
juniSnmpCompliance6.setObjects(*((_A,_AA),(_A,_T),(_A,_AB),(_A,_H)))
if mibBuilder.loadTexts:juniSnmpCompliance6.setStatus(_D)
juniSnmpCompliance7=ModuleCompliance((1,3,6,1,4,1,4874,2,2,16,2,1,7))
juniSnmpCompliance7.setObjects(*((_A,_AC),(_A,_T),(_A,_AB),(_A,_H)))
if mibBuilder.loadTexts:juniSnmpCompliance7.setStatus(_D)
juniSnmpCompliance8=ModuleCompliance((1,3,6,1,4,1,4874,2,2,16,2,1,8))
juniSnmpCompliance8.setObjects(*((_A,_AC),(_A,_T),(_A,_AD),(_A,_H)))
if mibBuilder.loadTexts:juniSnmpCompliance8.setStatus(_D)
juniSnmpCompliance9=ModuleCompliance((1,3,6,1,4,1,4874,2,2,16,2,1,9))
juniSnmpCompliance9.setObjects(*((_A,_AW),(_A,_T),(_A,_AD),(_A,_H)))
if mibBuilder.loadTexts:juniSnmpCompliance9.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'JuniSnmpCommunityName':JuniSnmpCommunityName,'JuniSnmpAccessListName':JuniSnmpAccessListName,'JuniSnmpTrapMask':JuniSnmpTrapMask,'JuniTrapSeverity':JuniTrapSeverity,'JuniSnmpIntfCompRestrictedMask':JuniSnmpIntfCompRestrictedMask,'JuniSnmpManagementApplicationIndex':JuniSnmpManagementApplicationIndex,'juniSnmpMIB':juniSnmpMIB,'juniSnmpObjects':juniSnmpObjects,'juniSnmpGeneral':juniSnmpGeneral,_J:juniSnmpMaxPduSize,_AN:juniSnmpInterfaceMode,'juniSnmpInterfaceCompress':juniSnmpInterfaceCompress,_a:juniSnmpIntfCompCompressed,_b:juniSnmpIntfCompEnhanced,_c:juniSnmpIntfCompEnhancedDisplay,_d:juniSnmpIntfCompRestricted,_e:juniSnmpIntfCompRestrictedDisplay,'juniSnmpIntfCompTable':juniSnmpIntfCompTable,'juniSnmpIntfCompEntry':juniSnmpIntfCompEntry,_AF:juniSnmpIntfCompTableType,_AP:juniSnmpIntfCompEntryCompressed,_AQ:juniSnmpIntfCompMask,_AR:juniSnmpIntfCompMaskDisplay,_o:juniSnmpProxyStatus,_A7:juniSnmpAccessPermission,'juniSnmpManagementApplicationTable':juniSnmpManagementApplicationTable,'juniSnmpManagementApplicationEntry':juniSnmpManagementApplicationEntry,_AG:juniSnmpManagementApplicationRouterIndex,_AH:juniSnmpManagementApplicationIndex,_A8:juniSnmpManagementApplicationRowStatus,'juniSnmpCommunity':juniSnmpCommunity,'juniSnmpCommunityTable':juniSnmpCommunityTable,'juniSnmpCommunityEntry':juniSnmpCommunityEntry,_U:juniSnmpCommunityName,_X:juniSnmpCommunityRowStatus,_Y:juniSnmpCommunityPrivilege,_Z:juniSnmpCommunityAccessList,_h:juniSnmpCommunityAccessListName,_i:juniSnmpCommunityView,'juniSnmpTrap':juniSnmpTrap,_K:juniSnmpTrapGlobalFilter,_L:juniSnmpTrapSource,'juniSnmpTrapHostTable':juniSnmpTrapHostTable,'juniSnmpTrapHostEntry':juniSnmpTrapHostEntry,_I:juniSnmpTrapHostIpAddress,_N:juniSnmpTrapHostRowStatus,_O:juniSnmpTrapHostUdpPort,_P:juniSnmpTrapHostCommunity,_Q:juniSnmpTrapHostProtocolVersion,_R:juniSnmpTrapHostFilter,_S:juniSnmpTrapHostSends,_j:juniSnmpTrapHostDiscards,_k:juniSnmpTrapHostSeverityFilter,_q:juniSnmpTrapHostPingTimeOut,_r:juniSnmpTrapHostIncludeLogVarbinds,_s:juniSnmpTrapHostQueueSize,_t:juniSnmpTrapHostQueueDrainRate,_u:juniSnmpTrapHostQueueFull,_v:juniSnmpTrapHostBadEncodingDiscards,_w:juniSnmpTrapHostQueueFullDiscards,_x:juniSnmpTrapHostNoResponseDiscards,_M:juniSnmpTrapProxy,_l:juniSnmpTrapTrapSeverity,_m:juniSnmpTrapGlobalDiscards,_n:juniSnmpTrapGlobalSeverityFilter,_y:juniSnmpTrapTotalTrapsReceived,_z:juniSnmpTrapLocalTrapsSubmitted,_A0:juniSnmpTrapProxyTrapsSubmitted,_A1:juniSnmpTrapTotalTrapsDiscarded,_A2:juniSnmpTrapNoMemoryDiscards,_A3:juniSnmpTrapNoQueueResourceDiscards,_A4:juniSnmpTrapAgentSnmpNotAbleDiscards,_A5:juniSnmpTrapTotalTrapsOut,_A6:juniSnmpTrapTotalProxyOut,'juniSnmpTrapSeverityFilterTable':juniSnmpTrapSeverityFilterTable,'juniSnmpTrapSeverityFilterEntry':juniSnmpTrapSeverityFilterEntry,_AI:juniSnmpTrapCategory,_AO:juniSnmpTrapSeverityFilter,'juniSnmpAuthFailId':juniSnmpAuthFailId,_AJ:juniSnmpAuthFailIdIpAddress,_AK:juniSnmpAuthFailIdUdpPort,_AL:juniSnmpAuthFailIdCommunity,_AM:juniSnmpAuthFailIdReason,'juniSnmpConformance':juniSnmpConformance,'juniSnmpCompliances':juniSnmpCompliances,'juniSnmpCompliance':juniSnmpCompliance,'juniSnmpCompliance2':juniSnmpCompliance2,'juniSnmpCompliance3':juniSnmpCompliance3,'juniSnmpCompliance4':juniSnmpCompliance4,'juniSnmpCompliance5':juniSnmpCompliance5,'juniSnmpCompliance6':juniSnmpCompliance6,'juniSnmpCompliance7':juniSnmpCompliance7,'juniSnmpCompliance8':juniSnmpCompliance8,'juniSnmpCompliance9':juniSnmpCompliance9,'juniSnmpGroups':juniSnmpGroups,_AS:juniSnmpGroup,_H:juniSnmpAuthFailGroup,_AT:juniSnmpGroup2,_AU:juniSnmpGroup3,_AV:juniSnmpGeneralGroup,_T:juniSnmpAccessGroup,_A9:juniSnmpTrapGroup,_AA:juniSnmpGeneralGroup2,_AB:juniSnmpTrapGroup2,_AC:juniSnmpGeneralGroup3,_AD:juniSnmpTrapGroup3,_AW:juniSnmpGeneralGroup4})