_y='ciscoMspMIBMetaParamsObjectGroup'
_x='ciscoMspMIBRsvpParamsObjectGroup'
_w='ciscoMspMIBProfileNameObjectGroup'
_v='ciscoMspMIBIfProfileObjectGroup'
_u='ciscoMspMIBScalarObjectGroup'
_t='cMspMetaParamsRowStatus'
_s='cMspMetaParamsStorageType'
_r='cMspMetaParamsAppVersion'
_q='cMspMetaParamsAppVendor'
_p='cMspMetaParamsAppName'
_o='cMspMetaParamsSipEmail'
_n='cMspMetaParamsSipUserName'
_m='cMspMetaParamsPayloadType'
_l='cMspMetaParamsMimeType'
_k='cMspMetaParamsCname'
_j='cMspMetaParamsDomainName'
_i='cMspMetaParamsSessId'
_h='cMspMetaParamsClockFreq'
_g='cMspMetaParamsSyncSrc'
_f='cMspMetaParamsBandwidth'
_e='cMspRsvpParamsRowStatus'
_d='cMspRsvpParamsStorageType'
_c='cMspRsvpParamsPriorityDefend'
_b='cMspRsvpParamsPriorityPrempt'
_a='cMspRsvpParamsMaxBurst'
_Z='cMspRsvpParamsPeakRate'
_Y='cMspRsvpParamsBandwidth'
_X='cMspProfileRowStatus'
_W='cMspProfileStorageType'
_V='cMspProfileMetadata'
_U='cMspProfileRsvp'
_T='cMspProfileService'
_S='cMspIfProfileRowStatus'
_R='cMspIfProfileStorageType'
_Q='cMspIfProfileName'
_P='cMspGlobalProfile'
_O='cMspGlobalStatus'
_N='read-write'
_M='Integer32'
_L='ifIndex'
_K='IF-MIB'
_J='cMspMetaParamsName'
_I='kbps'
_H='cMspRsvpParamsName'
_G='cMspProfileName'
_F='StorageType'
_E='Unsigned32'
_D='SnmpAdminString'
_C='read-create'
_B='CISCO-MSP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_K,_L)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_F,'TextualConvention')
ciscoMspMIB=ModuleIdentity((1,3,6,1,4,1,9,9,793))
if mibBuilder.loadTexts:ciscoMspMIB.setRevisions(('2012-04-19 00:00',))
_CiscoMspMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoMspMIBNotifs=_CiscoMspMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,793,0))
_CiscoMspMIBObjects_ObjectIdentity=ObjectIdentity
ciscoMspMIBObjects=_CiscoMspMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,793,1))
class _CMspGlobalStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_CMspGlobalStatus_Type.__name__=_M
_CMspGlobalStatus_Object=MibScalar
cMspGlobalStatus=_CMspGlobalStatus_Object((1,3,6,1,4,1,9,9,793,1,1),_CMspGlobalStatus_Type())
cMspGlobalStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:cMspGlobalStatus.setStatus(_A)
class _CMspGlobalProfile_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CMspGlobalProfile_Type.__name__=_D
_CMspGlobalProfile_Object=MibScalar
cMspGlobalProfile=_CMspGlobalProfile_Object((1,3,6,1,4,1,9,9,793,1,2),_CMspGlobalProfile_Type())
cMspGlobalProfile.setMaxAccess(_N)
if mibBuilder.loadTexts:cMspGlobalProfile.setStatus(_A)
_CMspIfProfileTable_Object=MibTable
cMspIfProfileTable=_CMspIfProfileTable_Object((1,3,6,1,4,1,9,9,793,1,3))
if mibBuilder.loadTexts:cMspIfProfileTable.setStatus(_A)
_CMspIfProfileEntry_Object=MibTableRow
cMspIfProfileEntry=_CMspIfProfileEntry_Object((1,3,6,1,4,1,9,9,793,1,3,1))
cMspIfProfileEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:cMspIfProfileEntry.setStatus(_A)
class _CMspIfProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CMspIfProfileName_Type.__name__=_D
_CMspIfProfileName_Object=MibTableColumn
cMspIfProfileName=_CMspIfProfileName_Object((1,3,6,1,4,1,9,9,793,1,3,1,1),_CMspIfProfileName_Type())
cMspIfProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspIfProfileName.setStatus(_A)
class _CMspIfProfileStorageType_Type(StorageType):defaultValue=3
_CMspIfProfileStorageType_Type.__name__=_F
_CMspIfProfileStorageType_Object=MibTableColumn
cMspIfProfileStorageType=_CMspIfProfileStorageType_Object((1,3,6,1,4,1,9,9,793,1,3,1,2),_CMspIfProfileStorageType_Type())
cMspIfProfileStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspIfProfileStorageType.setStatus(_A)
_CMspIfProfileRowStatus_Type=RowStatus
_CMspIfProfileRowStatus_Object=MibTableColumn
cMspIfProfileRowStatus=_CMspIfProfileRowStatus_Object((1,3,6,1,4,1,9,9,793,1,3,1,3),_CMspIfProfileRowStatus_Type())
cMspIfProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspIfProfileRowStatus.setStatus(_A)
_CMspProfileTable_Object=MibTable
cMspProfileTable=_CMspProfileTable_Object((1,3,6,1,4,1,9,9,793,1,4))
if mibBuilder.loadTexts:cMspProfileTable.setStatus(_A)
_CMspProfileEntry_Object=MibTableRow
cMspProfileEntry=_CMspProfileEntry_Object((1,3,6,1,4,1,9,9,793,1,4,1))
cMspProfileEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:cMspProfileEntry.setStatus(_A)
class _CMspProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CMspProfileName_Type.__name__=_D
_CMspProfileName_Object=MibTableColumn
cMspProfileName=_CMspProfileName_Object((1,3,6,1,4,1,9,9,793,1,4,1,1),_CMspProfileName_Type())
cMspProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspProfileName.setStatus(_A)
class _CMspProfileService_Type(Bits):namedValues=NamedValues(*(('rsvp',0),('metadata',1)))
_CMspProfileService_Type.__name__='Bits'
_CMspProfileService_Object=MibTableColumn
cMspProfileService=_CMspProfileService_Object((1,3,6,1,4,1,9,9,793,1,4,1,2),_CMspProfileService_Type())
cMspProfileService.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspProfileService.setStatus(_A)
class _CMspProfileRsvp_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CMspProfileRsvp_Type.__name__=_D
_CMspProfileRsvp_Object=MibTableColumn
cMspProfileRsvp=_CMspProfileRsvp_Object((1,3,6,1,4,1,9,9,793,1,4,1,3),_CMspProfileRsvp_Type())
cMspProfileRsvp.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspProfileRsvp.setStatus(_A)
class _CMspProfileMetadata_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CMspProfileMetadata_Type.__name__=_D
_CMspProfileMetadata_Object=MibTableColumn
cMspProfileMetadata=_CMspProfileMetadata_Object((1,3,6,1,4,1,9,9,793,1,4,1,4),_CMspProfileMetadata_Type())
cMspProfileMetadata.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspProfileMetadata.setStatus(_A)
class _CMspProfileStorageType_Type(StorageType):defaultValue=3
_CMspProfileStorageType_Type.__name__=_F
_CMspProfileStorageType_Object=MibTableColumn
cMspProfileStorageType=_CMspProfileStorageType_Object((1,3,6,1,4,1,9,9,793,1,4,1,5),_CMspProfileStorageType_Type())
cMspProfileStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspProfileStorageType.setStatus(_A)
_CMspProfileRowStatus_Type=RowStatus
_CMspProfileRowStatus_Object=MibTableColumn
cMspProfileRowStatus=_CMspProfileRowStatus_Object((1,3,6,1,4,1,9,9,793,1,4,1,6),_CMspProfileRowStatus_Type())
cMspProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspProfileRowStatus.setStatus(_A)
_CMspRsvpParamsTable_Object=MibTable
cMspRsvpParamsTable=_CMspRsvpParamsTable_Object((1,3,6,1,4,1,9,9,793,1,5))
if mibBuilder.loadTexts:cMspRsvpParamsTable.setStatus(_A)
_CMspRsvpParamsEntry_Object=MibTableRow
cMspRsvpParamsEntry=_CMspRsvpParamsEntry_Object((1,3,6,1,4,1,9,9,793,1,5,1))
cMspRsvpParamsEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cMspRsvpParamsEntry.setStatus(_A)
class _CMspRsvpParamsName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CMspRsvpParamsName_Type.__name__=_D
_CMspRsvpParamsName_Object=MibTableColumn
cMspRsvpParamsName=_CMspRsvpParamsName_Object((1,3,6,1,4,1,9,9,793,1,5,1,1),_CMspRsvpParamsName_Type())
cMspRsvpParamsName.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspRsvpParamsName.setStatus(_A)
class _CMspRsvpParamsBandwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000000))
_CMspRsvpParamsBandwidth_Type.__name__=_E
_CMspRsvpParamsBandwidth_Object=MibTableColumn
cMspRsvpParamsBandwidth=_CMspRsvpParamsBandwidth_Object((1,3,6,1,4,1,9,9,793,1,5,1,2),_CMspRsvpParamsBandwidth_Type())
cMspRsvpParamsBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspRsvpParamsBandwidth.setStatus(_A)
if mibBuilder.loadTexts:cMspRsvpParamsBandwidth.setUnits(_I)
class _CMspRsvpParamsPeakRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000000))
_CMspRsvpParamsPeakRate_Type.__name__=_E
_CMspRsvpParamsPeakRate_Object=MibTableColumn
cMspRsvpParamsPeakRate=_CMspRsvpParamsPeakRate_Object((1,3,6,1,4,1,9,9,793,1,5,1,3),_CMspRsvpParamsPeakRate_Type())
cMspRsvpParamsPeakRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspRsvpParamsPeakRate.setStatus(_A)
if mibBuilder.loadTexts:cMspRsvpParamsPeakRate.setUnits(_I)
class _CMspRsvpParamsMaxBurst_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CMspRsvpParamsMaxBurst_Type.__name__=_E
_CMspRsvpParamsMaxBurst_Object=MibTableColumn
cMspRsvpParamsMaxBurst=_CMspRsvpParamsMaxBurst_Object((1,3,6,1,4,1,9,9,793,1,5,1,4),_CMspRsvpParamsMaxBurst_Type())
cMspRsvpParamsMaxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspRsvpParamsMaxBurst.setStatus(_A)
if mibBuilder.loadTexts:cMspRsvpParamsMaxBurst.setUnits('kB')
class _CMspRsvpParamsPriorityPrempt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CMspRsvpParamsPriorityPrempt_Type.__name__=_E
_CMspRsvpParamsPriorityPrempt_Object=MibTableColumn
cMspRsvpParamsPriorityPrempt=_CMspRsvpParamsPriorityPrempt_Object((1,3,6,1,4,1,9,9,793,1,5,1,5),_CMspRsvpParamsPriorityPrempt_Type())
cMspRsvpParamsPriorityPrempt.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspRsvpParamsPriorityPrempt.setStatus(_A)
class _CMspRsvpParamsPriorityDefend_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CMspRsvpParamsPriorityDefend_Type.__name__=_E
_CMspRsvpParamsPriorityDefend_Object=MibTableColumn
cMspRsvpParamsPriorityDefend=_CMspRsvpParamsPriorityDefend_Object((1,3,6,1,4,1,9,9,793,1,5,1,6),_CMspRsvpParamsPriorityDefend_Type())
cMspRsvpParamsPriorityDefend.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspRsvpParamsPriorityDefend.setStatus(_A)
class _CMspRsvpParamsStorageType_Type(StorageType):defaultValue=3
_CMspRsvpParamsStorageType_Type.__name__=_F
_CMspRsvpParamsStorageType_Object=MibTableColumn
cMspRsvpParamsStorageType=_CMspRsvpParamsStorageType_Object((1,3,6,1,4,1,9,9,793,1,5,1,7),_CMspRsvpParamsStorageType_Type())
cMspRsvpParamsStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspRsvpParamsStorageType.setStatus(_A)
_CMspRsvpParamsRowStatus_Type=RowStatus
_CMspRsvpParamsRowStatus_Object=MibTableColumn
cMspRsvpParamsRowStatus=_CMspRsvpParamsRowStatus_Object((1,3,6,1,4,1,9,9,793,1,5,1,8),_CMspRsvpParamsRowStatus_Type())
cMspRsvpParamsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspRsvpParamsRowStatus.setStatus(_A)
_CMspMetaParamsTable_Object=MibTable
cMspMetaParamsTable=_CMspMetaParamsTable_Object((1,3,6,1,4,1,9,9,793,1,6))
if mibBuilder.loadTexts:cMspMetaParamsTable.setStatus(_A)
_CMspMetaParamsEntry_Object=MibTableRow
cMspMetaParamsEntry=_CMspMetaParamsEntry_Object((1,3,6,1,4,1,9,9,793,1,6,1))
cMspMetaParamsEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cMspMetaParamsEntry.setStatus(_A)
class _CMspMetaParamsName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CMspMetaParamsName_Type.__name__=_D
_CMspMetaParamsName_Object=MibTableColumn
cMspMetaParamsName=_CMspMetaParamsName_Object((1,3,6,1,4,1,9,9,793,1,6,1,1),_CMspMetaParamsName_Type())
cMspMetaParamsName.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspMetaParamsName.setStatus(_A)
class _CMspMetaParamsBandwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000000))
_CMspMetaParamsBandwidth_Type.__name__=_E
_CMspMetaParamsBandwidth_Object=MibTableColumn
cMspMetaParamsBandwidth=_CMspMetaParamsBandwidth_Object((1,3,6,1,4,1,9,9,793,1,6,1,2),_CMspMetaParamsBandwidth_Type())
cMspMetaParamsBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspMetaParamsBandwidth.setStatus(_A)
if mibBuilder.loadTexts:cMspMetaParamsBandwidth.setUnits(_I)
_CMspMetaParamsSyncSrc_Type=Unsigned32
_CMspMetaParamsSyncSrc_Object=MibTableColumn
cMspMetaParamsSyncSrc=_CMspMetaParamsSyncSrc_Object((1,3,6,1,4,1,9,9,793,1,6,1,3),_CMspMetaParamsSyncSrc_Type())
cMspMetaParamsSyncSrc.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspMetaParamsSyncSrc.setStatus(_A)
_CMspMetaParamsClockFreq_Type=Unsigned32
_CMspMetaParamsClockFreq_Object=MibTableColumn
cMspMetaParamsClockFreq=_CMspMetaParamsClockFreq_Object((1,3,6,1,4,1,9,9,793,1,6,1,4),_CMspMetaParamsClockFreq_Type())
cMspMetaParamsClockFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspMetaParamsClockFreq.setStatus(_A)
class _CMspMetaParamsSessId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CMspMetaParamsSessId_Type.__name__=_D
_CMspMetaParamsSessId_Object=MibTableColumn
cMspMetaParamsSessId=_CMspMetaParamsSessId_Object((1,3,6,1,4,1,9,9,793,1,6,1,5),_CMspMetaParamsSessId_Type())
cMspMetaParamsSessId.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspMetaParamsSessId.setStatus(_A)
class _CMspMetaParamsDomainName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CMspMetaParamsDomainName_Type.__name__=_D
_CMspMetaParamsDomainName_Object=MibTableColumn
cMspMetaParamsDomainName=_CMspMetaParamsDomainName_Object((1,3,6,1,4,1,9,9,793,1,6,1,6),_CMspMetaParamsDomainName_Type())
cMspMetaParamsDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspMetaParamsDomainName.setStatus(_A)
class _CMspMetaParamsCname_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CMspMetaParamsCname_Type.__name__=_D
_CMspMetaParamsCname_Object=MibTableColumn
cMspMetaParamsCname=_CMspMetaParamsCname_Object((1,3,6,1,4,1,9,9,793,1,6,1,7),_CMspMetaParamsCname_Type())
cMspMetaParamsCname.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspMetaParamsCname.setStatus(_A)
class _CMspMetaParamsMimeType_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CMspMetaParamsMimeType_Type.__name__=_D
_CMspMetaParamsMimeType_Object=MibTableColumn
cMspMetaParamsMimeType=_CMspMetaParamsMimeType_Object((1,3,6,1,4,1,9,9,793,1,6,1,8),_CMspMetaParamsMimeType_Type())
cMspMetaParamsMimeType.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspMetaParamsMimeType.setStatus(_A)
class _CMspMetaParamsPayloadType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_CMspMetaParamsPayloadType_Type.__name__=_E
_CMspMetaParamsPayloadType_Object=MibTableColumn
cMspMetaParamsPayloadType=_CMspMetaParamsPayloadType_Object((1,3,6,1,4,1,9,9,793,1,6,1,9),_CMspMetaParamsPayloadType_Type())
cMspMetaParamsPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspMetaParamsPayloadType.setStatus(_A)
class _CMspMetaParamsSipUserName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CMspMetaParamsSipUserName_Type.__name__=_D
_CMspMetaParamsSipUserName_Object=MibTableColumn
cMspMetaParamsSipUserName=_CMspMetaParamsSipUserName_Object((1,3,6,1,4,1,9,9,793,1,6,1,10),_CMspMetaParamsSipUserName_Type())
cMspMetaParamsSipUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspMetaParamsSipUserName.setStatus(_A)
class _CMspMetaParamsSipEmail_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CMspMetaParamsSipEmail_Type.__name__=_D
_CMspMetaParamsSipEmail_Object=MibTableColumn
cMspMetaParamsSipEmail=_CMspMetaParamsSipEmail_Object((1,3,6,1,4,1,9,9,793,1,6,1,11),_CMspMetaParamsSipEmail_Type())
cMspMetaParamsSipEmail.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspMetaParamsSipEmail.setStatus(_A)
class _CMspMetaParamsAppName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CMspMetaParamsAppName_Type.__name__=_D
_CMspMetaParamsAppName_Object=MibTableColumn
cMspMetaParamsAppName=_CMspMetaParamsAppName_Object((1,3,6,1,4,1,9,9,793,1,6,1,12),_CMspMetaParamsAppName_Type())
cMspMetaParamsAppName.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspMetaParamsAppName.setStatus(_A)
class _CMspMetaParamsAppVendor_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CMspMetaParamsAppVendor_Type.__name__=_D
_CMspMetaParamsAppVendor_Object=MibTableColumn
cMspMetaParamsAppVendor=_CMspMetaParamsAppVendor_Object((1,3,6,1,4,1,9,9,793,1,6,1,13),_CMspMetaParamsAppVendor_Type())
cMspMetaParamsAppVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspMetaParamsAppVendor.setStatus(_A)
class _CMspMetaParamsAppVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CMspMetaParamsAppVersion_Type.__name__=_D
_CMspMetaParamsAppVersion_Object=MibTableColumn
cMspMetaParamsAppVersion=_CMspMetaParamsAppVersion_Object((1,3,6,1,4,1,9,9,793,1,6,1,14),_CMspMetaParamsAppVersion_Type())
cMspMetaParamsAppVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspMetaParamsAppVersion.setStatus(_A)
class _CMspMetaParamsStorageType_Type(StorageType):defaultValue=3
_CMspMetaParamsStorageType_Type.__name__=_F
_CMspMetaParamsStorageType_Object=MibTableColumn
cMspMetaParamsStorageType=_CMspMetaParamsStorageType_Object((1,3,6,1,4,1,9,9,793,1,6,1,15),_CMspMetaParamsStorageType_Type())
cMspMetaParamsStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspMetaParamsStorageType.setStatus(_A)
_CMspMetaParamsRowStatus_Type=RowStatus
_CMspMetaParamsRowStatus_Object=MibTableColumn
cMspMetaParamsRowStatus=_CMspMetaParamsRowStatus_Object((1,3,6,1,4,1,9,9,793,1,6,1,16),_CMspMetaParamsRowStatus_Type())
cMspMetaParamsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cMspMetaParamsRowStatus.setStatus(_A)
_CiscoMspMIBConform_ObjectIdentity=ObjectIdentity
ciscoMspMIBConform=_CiscoMspMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,793,2))
_CiscoMspMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoMspMIBCompliances=_CiscoMspMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,793,2,1))
_CiscoMspMIBGroups_ObjectIdentity=ObjectIdentity
ciscoMspMIBGroups=_CiscoMspMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,793,2,2))
ciscoMspMIBScalarObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,793,2,2,1))
ciscoMspMIBScalarObjectGroup.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ciscoMspMIBScalarObjectGroup.setStatus(_A)
ciscoMspMIBIfProfileObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,793,2,2,2))
ciscoMspMIBIfProfileObjectGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:ciscoMspMIBIfProfileObjectGroup.setStatus(_A)
ciscoMspMIBProfileNameObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,793,2,2,3))
ciscoMspMIBProfileNameObjectGroup.setObjects(*((_B,_G),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciscoMspMIBProfileNameObjectGroup.setStatus(_A)
ciscoMspMIBRsvpParamsObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,793,2,2,4))
ciscoMspMIBRsvpParamsObjectGroup.setObjects(*((_B,_H),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:ciscoMspMIBRsvpParamsObjectGroup.setStatus(_A)
ciscoMspMIBMetaParamsObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,793,2,2,5))
ciscoMspMIBMetaParamsObjectGroup.setObjects(*((_B,_J),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:ciscoMspMIBMetaParamsObjectGroup.setStatus(_A)
ciscoMspMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,793,2,1,1))
ciscoMspMIBCompliance.setObjects(*((_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:ciscoMspMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoMspMIB':ciscoMspMIB,'ciscoMspMIBNotifs':ciscoMspMIBNotifs,'ciscoMspMIBObjects':ciscoMspMIBObjects,_O:cMspGlobalStatus,_P:cMspGlobalProfile,'cMspIfProfileTable':cMspIfProfileTable,'cMspIfProfileEntry':cMspIfProfileEntry,_Q:cMspIfProfileName,_R:cMspIfProfileStorageType,_S:cMspIfProfileRowStatus,'cMspProfileTable':cMspProfileTable,'cMspProfileEntry':cMspProfileEntry,_G:cMspProfileName,_T:cMspProfileService,_U:cMspProfileRsvp,_V:cMspProfileMetadata,_W:cMspProfileStorageType,_X:cMspProfileRowStatus,'cMspRsvpParamsTable':cMspRsvpParamsTable,'cMspRsvpParamsEntry':cMspRsvpParamsEntry,_H:cMspRsvpParamsName,_Y:cMspRsvpParamsBandwidth,_Z:cMspRsvpParamsPeakRate,_a:cMspRsvpParamsMaxBurst,_b:cMspRsvpParamsPriorityPrempt,_c:cMspRsvpParamsPriorityDefend,_d:cMspRsvpParamsStorageType,_e:cMspRsvpParamsRowStatus,'cMspMetaParamsTable':cMspMetaParamsTable,'cMspMetaParamsEntry':cMspMetaParamsEntry,_J:cMspMetaParamsName,_f:cMspMetaParamsBandwidth,_g:cMspMetaParamsSyncSrc,_h:cMspMetaParamsClockFreq,_i:cMspMetaParamsSessId,_j:cMspMetaParamsDomainName,_k:cMspMetaParamsCname,_l:cMspMetaParamsMimeType,_m:cMspMetaParamsPayloadType,_n:cMspMetaParamsSipUserName,_o:cMspMetaParamsSipEmail,_p:cMspMetaParamsAppName,_q:cMspMetaParamsAppVendor,_r:cMspMetaParamsAppVersion,_s:cMspMetaParamsStorageType,_t:cMspMetaParamsRowStatus,'ciscoMspMIBConform':ciscoMspMIBConform,'ciscoMspMIBCompliances':ciscoMspMIBCompliances,'ciscoMspMIBCompliance':ciscoMspMIBCompliance,'ciscoMspMIBGroups':ciscoMspMIBGroups,_u:ciscoMspMIBScalarObjectGroup,_v:ciscoMspMIBIfProfileObjectGroup,_w:ciscoMspMIBProfileNameObjectGroup,_x:ciscoMspMIBRsvpParamsObjectGroup,_y:ciscoMspMIBMetaParamsObjectGroup})