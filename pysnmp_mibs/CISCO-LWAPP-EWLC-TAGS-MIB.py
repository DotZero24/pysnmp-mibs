_A7='ciscoLwappApLocationConfigGroup'
_A6='ciscoLwappRlanConfigGroup'
_A5='ciscoLwappFilterConfigGroup'
_A4='ciscoLwappTagsConfigGroup'
_A3='cLAssociatedApsConfigRowStatus'
_A2='cLApLocationDesc'
_A1='cLApLocationConfigRowStatus'
_A0='cLApLocationPolicyTag'
_z='cLApLocationRfTag'
_y='cLApLocationSiteTag'
_x='cLRlanPolicyProfileRowStatus'
_w='cLRlanPolicyProfile'
_v='cLApFilterPriorityFilterName'
_u='cLApFilterPriorityRowStatus'
_t='cLApFilterSiteTag'
_s='cLApFilterRfTag'
_r='cLApFilterPolicyTag'
_q='cLApFilterNameApNameRule'
_p='cLApFilterRowStatus'
_o='cLApTagSrcList'
_n='cLApTagSrcRowStatus'
_m='cLApConfigTagRowStatus'
_l='cLApConfigSiteTagName'
_k='cLApConfigRfTagName'
_j='cLApConfigPolicyTagName'
_i='cLIsLocalSite'
_h='cLReapSiteTagStartCertificateDownload'
_g='cLReapSiteUpgradeStart'
_f='cLSiteTagDescription'
_e='cLFlexProfName'
_d='cLApJoinProfName'
_c='cLSiteTagRowStatus'
_b='cL6GHzBandRfProfName'
_a='cL11bRfProfName'
_Z='cL11aRfProfName'
_Y='cLRfTagDescription'
_X='cLRfTagRowStatus'
_W='cLPolicyProfileRowStatus'
_V='cLPolicyProfileName'
_U='cLPolicyTagRowStatus'
_T='cLPolicyTagDescription'
_S='cLApFilterPriority'
_R='cLApFilterName'
_Q='cLApTagSrcPriority'
_P='cLApConfigTagSysMacAddress'
_O='cLRfTagName'
_N='cLSiteTagName'
_M='cLRlanPortID'
_L='cLProfileName'
_K='cLAssociatedApsApMac'
_J='cLApLocationName'
_I='TruthValue'
_H='cLPolicyTagName'
_G='Integer32'
_F='not-accessible'
_E='read-create'
_D='SnmpAdminString'
_C='read-write'
_B='CISCO-LWAPP-EWLC-TAGS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_I)
ciscoLwappTagsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,987))
if mibBuilder.loadTexts:ciscoLwappTagsMIB.setRevisions(('2018-09-20 00:00',))
_CiscoLwappTagsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoLwappTagsMIBNotifs=_CiscoLwappTagsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,987,0))
_CiscoLwappApLocationConfig_ObjectIdentity=ObjectIdentity
ciscoLwappApLocationConfig=_CiscoLwappApLocationConfig_ObjectIdentity((1,3,6,1,4,1,9,9,987,0,13))
_CLApLocationConfigTable_Object=MibTable
cLApLocationConfigTable=_CLApLocationConfigTable_Object((1,3,6,1,4,1,9,9,987,0,13,1))
if mibBuilder.loadTexts:cLApLocationConfigTable.setStatus(_A)
_CLApLocationConfigEntry_Object=MibTableRow
cLApLocationConfigEntry=_CLApLocationConfigEntry_Object((1,3,6,1,4,1,9,9,987,0,13,1,1))
cLApLocationConfigEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cLApLocationConfigEntry.setStatus(_A)
_CLApLocationName_Type=SnmpAdminString
_CLApLocationName_Object=MibTableColumn
cLApLocationName=_CLApLocationName_Object((1,3,6,1,4,1,9,9,987,0,13,1,1,1),_CLApLocationName_Type())
cLApLocationName.setMaxAccess(_F)
if mibBuilder.loadTexts:cLApLocationName.setStatus(_A)
_CLApLocationSiteTag_Type=SnmpAdminString
_CLApLocationSiteTag_Object=MibTableColumn
cLApLocationSiteTag=_CLApLocationSiteTag_Object((1,3,6,1,4,1,9,9,987,0,13,1,1,2),_CLApLocationSiteTag_Type())
cLApLocationSiteTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cLApLocationSiteTag.setStatus(_A)
_CLApLocationRfTag_Type=SnmpAdminString
_CLApLocationRfTag_Object=MibTableColumn
cLApLocationRfTag=_CLApLocationRfTag_Object((1,3,6,1,4,1,9,9,987,0,13,1,1,3),_CLApLocationRfTag_Type())
cLApLocationRfTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cLApLocationRfTag.setStatus(_A)
_CLApLocationPolicyTag_Type=SnmpAdminString
_CLApLocationPolicyTag_Object=MibTableColumn
cLApLocationPolicyTag=_CLApLocationPolicyTag_Object((1,3,6,1,4,1,9,9,987,0,13,1,1,4),_CLApLocationPolicyTag_Type())
cLApLocationPolicyTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cLApLocationPolicyTag.setStatus(_A)
_CLApLocationConfigRowStatus_Type=RowStatus
_CLApLocationConfigRowStatus_Object=MibTableColumn
cLApLocationConfigRowStatus=_CLApLocationConfigRowStatus_Object((1,3,6,1,4,1,9,9,987,0,13,1,1,5),_CLApLocationConfigRowStatus_Type())
cLApLocationConfigRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cLApLocationConfigRowStatus.setStatus(_A)
_CLApLocationDesc_Type=SnmpAdminString
_CLApLocationDesc_Object=MibTableColumn
cLApLocationDesc=_CLApLocationDesc_Object((1,3,6,1,4,1,9,9,987,0,13,1,1,6),_CLApLocationDesc_Type())
cLApLocationDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:cLApLocationDesc.setStatus(_A)
_CiscoLwappAssociatedApsConfig_ObjectIdentity=ObjectIdentity
ciscoLwappAssociatedApsConfig=_CiscoLwappAssociatedApsConfig_ObjectIdentity((1,3,6,1,4,1,9,9,987,0,14))
_CLAssociatedApsConfigTable_Object=MibTable
cLAssociatedApsConfigTable=_CLAssociatedApsConfigTable_Object((1,3,6,1,4,1,9,9,987,0,14,1))
if mibBuilder.loadTexts:cLAssociatedApsConfigTable.setStatus(_A)
_CLAssociatedApsConfigEntry_Object=MibTableRow
cLAssociatedApsConfigEntry=_CLAssociatedApsConfigEntry_Object((1,3,6,1,4,1,9,9,987,0,14,1,1))
cLAssociatedApsConfigEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:cLAssociatedApsConfigEntry.setStatus(_A)
_CLAssociatedApsApMac_Type=MacAddress
_CLAssociatedApsApMac_Object=MibTableColumn
cLAssociatedApsApMac=_CLAssociatedApsApMac_Object((1,3,6,1,4,1,9,9,987,0,14,1,1,1),_CLAssociatedApsApMac_Type())
cLAssociatedApsApMac.setMaxAccess(_F)
if mibBuilder.loadTexts:cLAssociatedApsApMac.setStatus(_A)
_CLAssociatedApsConfigRowStatus_Type=RowStatus
_CLAssociatedApsConfigRowStatus_Object=MibTableColumn
cLAssociatedApsConfigRowStatus=_CLAssociatedApsConfigRowStatus_Object((1,3,6,1,4,1,9,9,987,0,14,1,1,2),_CLAssociatedApsConfigRowStatus_Type())
cLAssociatedApsConfigRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cLAssociatedApsConfigRowStatus.setStatus(_A)
_CiscoLwappTagsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLwappTagsMIBObjects=_CiscoLwappTagsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,987,1))
_CiscoLwappPolicyTagConfig_ObjectIdentity=ObjectIdentity
ciscoLwappPolicyTagConfig=_CiscoLwappPolicyTagConfig_ObjectIdentity((1,3,6,1,4,1,9,9,987,1,1))
_CLPolicyTagConfigTable_Object=MibTable
cLPolicyTagConfigTable=_CLPolicyTagConfigTable_Object((1,3,6,1,4,1,9,9,987,1,1,1))
if mibBuilder.loadTexts:cLPolicyTagConfigTable.setStatus(_A)
_CLPolicyTagConfigEntry_Object=MibTableRow
cLPolicyTagConfigEntry=_CLPolicyTagConfigEntry_Object((1,3,6,1,4,1,9,9,987,1,1,1,1))
cLPolicyTagConfigEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cLPolicyTagConfigEntry.setStatus(_A)
class _CLPolicyTagName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CLPolicyTagName_Type.__name__=_D
_CLPolicyTagName_Object=MibTableColumn
cLPolicyTagName=_CLPolicyTagName_Object((1,3,6,1,4,1,9,9,987,1,1,1,1,1),_CLPolicyTagName_Type())
cLPolicyTagName.setMaxAccess(_F)
if mibBuilder.loadTexts:cLPolicyTagName.setStatus(_A)
class _CLPolicyTagDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CLPolicyTagDescription_Type.__name__=_D
_CLPolicyTagDescription_Object=MibTableColumn
cLPolicyTagDescription=_CLPolicyTagDescription_Object((1,3,6,1,4,1,9,9,987,1,1,1,1,2),_CLPolicyTagDescription_Type())
cLPolicyTagDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cLPolicyTagDescription.setStatus(_A)
_CLPolicyTagRowStatus_Type=RowStatus
_CLPolicyTagRowStatus_Object=MibTableColumn
cLPolicyTagRowStatus=_CLPolicyTagRowStatus_Object((1,3,6,1,4,1,9,9,987,1,1,1,1,3),_CLPolicyTagRowStatus_Type())
cLPolicyTagRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cLPolicyTagRowStatus.setStatus(_A)
_CLPolicyProfileConfigTable_Object=MibTable
cLPolicyProfileConfigTable=_CLPolicyProfileConfigTable_Object((1,3,6,1,4,1,9,9,987,1,1,2))
if mibBuilder.loadTexts:cLPolicyProfileConfigTable.setStatus(_A)
_CLPolicyProfileConfigEntry_Object=MibTableRow
cLPolicyProfileConfigEntry=_CLPolicyProfileConfigEntry_Object((1,3,6,1,4,1,9,9,987,1,1,2,1))
cLPolicyProfileConfigEntry.setIndexNames((0,_B,_H),(0,_B,_L))
if mibBuilder.loadTexts:cLPolicyProfileConfigEntry.setStatus(_A)
class _CLProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CLProfileName_Type.__name__=_D
_CLProfileName_Object=MibTableColumn
cLProfileName=_CLProfileName_Object((1,3,6,1,4,1,9,9,987,1,1,2,1,1),_CLProfileName_Type())
cLProfileName.setMaxAccess(_F)
if mibBuilder.loadTexts:cLProfileName.setStatus(_A)
class _CLPolicyProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CLPolicyProfileName_Type.__name__=_D
_CLPolicyProfileName_Object=MibTableColumn
cLPolicyProfileName=_CLPolicyProfileName_Object((1,3,6,1,4,1,9,9,987,1,1,2,1,2),_CLPolicyProfileName_Type())
cLPolicyProfileName.setMaxAccess(_E)
if mibBuilder.loadTexts:cLPolicyProfileName.setStatus(_A)
_CLPolicyProfileRowStatus_Type=RowStatus
_CLPolicyProfileRowStatus_Object=MibTableColumn
cLPolicyProfileRowStatus=_CLPolicyProfileRowStatus_Object((1,3,6,1,4,1,9,9,987,1,1,2,1,3),_CLPolicyProfileRowStatus_Type())
cLPolicyProfileRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cLPolicyProfileRowStatus.setStatus(_A)
_CLRlanPolicyProfileConfigTable_Object=MibTable
cLRlanPolicyProfileConfigTable=_CLRlanPolicyProfileConfigTable_Object((1,3,6,1,4,1,9,9,987,1,1,3))
if mibBuilder.loadTexts:cLRlanPolicyProfileConfigTable.setStatus(_A)
_CLRlanPolicyProfileConfigEntry_Object=MibTableRow
cLRlanPolicyProfileConfigEntry=_CLRlanPolicyProfileConfigEntry_Object((1,3,6,1,4,1,9,9,987,1,1,3,1))
cLRlanPolicyProfileConfigEntry.setIndexNames((0,_B,_H),(0,_B,_M))
if mibBuilder.loadTexts:cLRlanPolicyProfileConfigEntry.setStatus(_A)
class _CLRlanPortID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CLRlanPortID_Type.__name__=_G
_CLRlanPortID_Object=MibTableColumn
cLRlanPortID=_CLRlanPortID_Object((1,3,6,1,4,1,9,9,987,1,1,3,1,1),_CLRlanPortID_Type())
cLRlanPortID.setMaxAccess(_F)
if mibBuilder.loadTexts:cLRlanPortID.setStatus(_A)
class _CLRlanProfile_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CLRlanProfile_Type.__name__=_D
_CLRlanProfile_Object=MibTableColumn
cLRlanProfile=_CLRlanProfile_Object((1,3,6,1,4,1,9,9,987,1,1,3,1,2),_CLRlanProfile_Type())
cLRlanProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:cLRlanProfile.setStatus(_A)
class _CLRlanPolicyProfile_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CLRlanPolicyProfile_Type.__name__=_D
_CLRlanPolicyProfile_Object=MibTableColumn
cLRlanPolicyProfile=_CLRlanPolicyProfile_Object((1,3,6,1,4,1,9,9,987,1,1,3,1,3),_CLRlanPolicyProfile_Type())
cLRlanPolicyProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:cLRlanPolicyProfile.setStatus(_A)
_CLRlanPolicyProfileRowStatus_Type=RowStatus
_CLRlanPolicyProfileRowStatus_Object=MibTableColumn
cLRlanPolicyProfileRowStatus=_CLRlanPolicyProfileRowStatus_Object((1,3,6,1,4,1,9,9,987,1,1,3,1,4),_CLRlanPolicyProfileRowStatus_Type())
cLRlanPolicyProfileRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cLRlanPolicyProfileRowStatus.setStatus(_A)
_CiscoLwappSiteTagConfig_ObjectIdentity=ObjectIdentity
ciscoLwappSiteTagConfig=_CiscoLwappSiteTagConfig_ObjectIdentity((1,3,6,1,4,1,9,9,987,1,2))
_CLSiteTagConfigTable_Object=MibTable
cLSiteTagConfigTable=_CLSiteTagConfigTable_Object((1,3,6,1,4,1,9,9,987,1,2,1))
if mibBuilder.loadTexts:cLSiteTagConfigTable.setStatus(_A)
_CLSiteTagConfigEntry_Object=MibTableRow
cLSiteTagConfigEntry=_CLSiteTagConfigEntry_Object((1,3,6,1,4,1,9,9,987,1,2,1,1))
cLSiteTagConfigEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:cLSiteTagConfigEntry.setStatus(_A)
class _CLSiteTagName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CLSiteTagName_Type.__name__=_D
_CLSiteTagName_Object=MibTableColumn
cLSiteTagName=_CLSiteTagName_Object((1,3,6,1,4,1,9,9,987,1,2,1,1,1),_CLSiteTagName_Type())
cLSiteTagName.setMaxAccess(_F)
if mibBuilder.loadTexts:cLSiteTagName.setStatus(_A)
_CLSiteTagRowStatus_Type=RowStatus
_CLSiteTagRowStatus_Object=MibTableColumn
cLSiteTagRowStatus=_CLSiteTagRowStatus_Object((1,3,6,1,4,1,9,9,987,1,2,1,1,2),_CLSiteTagRowStatus_Type())
cLSiteTagRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cLSiteTagRowStatus.setStatus(_A)
class _CLApJoinProfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CLApJoinProfName_Type.__name__=_D
_CLApJoinProfName_Object=MibTableColumn
cLApJoinProfName=_CLApJoinProfName_Object((1,3,6,1,4,1,9,9,987,1,2,1,1,3),_CLApJoinProfName_Type())
cLApJoinProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cLApJoinProfName.setStatus(_A)
class _CLFlexProfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CLFlexProfName_Type.__name__=_D
_CLFlexProfName_Object=MibTableColumn
cLFlexProfName=_CLFlexProfName_Object((1,3,6,1,4,1,9,9,987,1,2,1,1,4),_CLFlexProfName_Type())
cLFlexProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cLFlexProfName.setStatus(_A)
class _CLSiteTagDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CLSiteTagDescription_Type.__name__=_D
_CLSiteTagDescription_Object=MibTableColumn
cLSiteTagDescription=_CLSiteTagDescription_Object((1,3,6,1,4,1,9,9,987,1,2,1,1,5),_CLSiteTagDescription_Type())
cLSiteTagDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cLSiteTagDescription.setStatus(_A)
class _CLReapSiteUpgradeStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('initiatePrimary',1),('initiateBackup',2),('abort',3)))
_CLReapSiteUpgradeStart_Type.__name__=_G
_CLReapSiteUpgradeStart_Object=MibTableColumn
cLReapSiteUpgradeStart=_CLReapSiteUpgradeStart_Object((1,3,6,1,4,1,9,9,987,1,2,1,1,6),_CLReapSiteUpgradeStart_Type())
cLReapSiteUpgradeStart.setMaxAccess(_C)
if mibBuilder.loadTexts:cLReapSiteUpgradeStart.setStatus(_A)
class _CLReapSiteTagStartCertificateDownload_Type(TruthValue):defaultValue=2
_CLReapSiteTagStartCertificateDownload_Type.__name__=_I
_CLReapSiteTagStartCertificateDownload_Object=MibTableColumn
cLReapSiteTagStartCertificateDownload=_CLReapSiteTagStartCertificateDownload_Object((1,3,6,1,4,1,9,9,987,1,2,1,1,7),_CLReapSiteTagStartCertificateDownload_Type())
cLReapSiteTagStartCertificateDownload.setMaxAccess(_C)
if mibBuilder.loadTexts:cLReapSiteTagStartCertificateDownload.setStatus(_A)
class _CLIsLocalSite_Type(TruthValue):defaultValue=1
_CLIsLocalSite_Type.__name__=_I
_CLIsLocalSite_Object=MibTableColumn
cLIsLocalSite=_CLIsLocalSite_Object((1,3,6,1,4,1,9,9,987,1,2,1,1,8),_CLIsLocalSite_Type())
cLIsLocalSite.setMaxAccess(_C)
if mibBuilder.loadTexts:cLIsLocalSite.setStatus(_A)
_CiscoLwappRfTagConfig_ObjectIdentity=ObjectIdentity
ciscoLwappRfTagConfig=_CiscoLwappRfTagConfig_ObjectIdentity((1,3,6,1,4,1,9,9,987,1,3))
_CLRfTagConfigTable_Object=MibTable
cLRfTagConfigTable=_CLRfTagConfigTable_Object((1,3,6,1,4,1,9,9,987,1,3,1))
if mibBuilder.loadTexts:cLRfTagConfigTable.setStatus(_A)
_CLRfTagConfigEntry_Object=MibTableRow
cLRfTagConfigEntry=_CLRfTagConfigEntry_Object((1,3,6,1,4,1,9,9,987,1,3,1,1))
cLRfTagConfigEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:cLRfTagConfigEntry.setStatus(_A)
class _CLRfTagName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CLRfTagName_Type.__name__=_D
_CLRfTagName_Object=MibTableColumn
cLRfTagName=_CLRfTagName_Object((1,3,6,1,4,1,9,9,987,1,3,1,1,1),_CLRfTagName_Type())
cLRfTagName.setMaxAccess(_F)
if mibBuilder.loadTexts:cLRfTagName.setStatus(_A)
_CLRfTagRowStatus_Type=RowStatus
_CLRfTagRowStatus_Object=MibTableColumn
cLRfTagRowStatus=_CLRfTagRowStatus_Object((1,3,6,1,4,1,9,9,987,1,3,1,1,2),_CLRfTagRowStatus_Type())
cLRfTagRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cLRfTagRowStatus.setStatus(_A)
class _CL11aRfProfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CL11aRfProfName_Type.__name__=_D
_CL11aRfProfName_Object=MibTableColumn
cL11aRfProfName=_CL11aRfProfName_Object((1,3,6,1,4,1,9,9,987,1,3,1,1,3),_CL11aRfProfName_Type())
cL11aRfProfName.setMaxAccess(_E)
if mibBuilder.loadTexts:cL11aRfProfName.setStatus(_A)
class _CL11bRfProfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CL11bRfProfName_Type.__name__=_D
_CL11bRfProfName_Object=MibTableColumn
cL11bRfProfName=_CL11bRfProfName_Object((1,3,6,1,4,1,9,9,987,1,3,1,1,4),_CL11bRfProfName_Type())
cL11bRfProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cL11bRfProfName.setStatus(_A)
class _CLRfTagDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CLRfTagDescription_Type.__name__=_D
_CLRfTagDescription_Object=MibTableColumn
cLRfTagDescription=_CLRfTagDescription_Object((1,3,6,1,4,1,9,9,987,1,3,1,1,5),_CLRfTagDescription_Type())
cLRfTagDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cLRfTagDescription.setStatus(_A)
class _CL6GHzBandRfProfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CL6GHzBandRfProfName_Type.__name__=_D
_CL6GHzBandRfProfName_Object=MibTableColumn
cL6GHzBandRfProfName=_CL6GHzBandRfProfName_Object((1,3,6,1,4,1,9,9,987,1,3,1,1,6),_CL6GHzBandRfProfName_Type())
cL6GHzBandRfProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cL6GHzBandRfProfName.setStatus(_A)
_CiscoLwappApTag_ObjectIdentity=ObjectIdentity
ciscoLwappApTag=_CiscoLwappApTag_ObjectIdentity((1,3,6,1,4,1,9,9,987,1,4))
_CLApConfigTagTable_Object=MibTable
cLApConfigTagTable=_CLApConfigTagTable_Object((1,3,6,1,4,1,9,9,987,1,4,1))
if mibBuilder.loadTexts:cLApConfigTagTable.setStatus(_A)
_CLApConfigTagEntry_Object=MibTableRow
cLApConfigTagEntry=_CLApConfigTagEntry_Object((1,3,6,1,4,1,9,9,987,1,4,1,1))
cLApConfigTagEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:cLApConfigTagEntry.setStatus(_A)
_CLApConfigTagSysMacAddress_Type=MacAddress
_CLApConfigTagSysMacAddress_Object=MibTableColumn
cLApConfigTagSysMacAddress=_CLApConfigTagSysMacAddress_Object((1,3,6,1,4,1,9,9,987,1,4,1,1,1),_CLApConfigTagSysMacAddress_Type())
cLApConfigTagSysMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cLApConfigTagSysMacAddress.setStatus(_A)
class _CLApConfigPolicyTagName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CLApConfigPolicyTagName_Type.__name__=_D
_CLApConfigPolicyTagName_Object=MibTableColumn
cLApConfigPolicyTagName=_CLApConfigPolicyTagName_Object((1,3,6,1,4,1,9,9,987,1,4,1,1,2),_CLApConfigPolicyTagName_Type())
cLApConfigPolicyTagName.setMaxAccess(_C)
if mibBuilder.loadTexts:cLApConfigPolicyTagName.setStatus(_A)
class _CLApConfigRfTagName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CLApConfigRfTagName_Type.__name__=_D
_CLApConfigRfTagName_Object=MibTableColumn
cLApConfigRfTagName=_CLApConfigRfTagName_Object((1,3,6,1,4,1,9,9,987,1,4,1,1,3),_CLApConfigRfTagName_Type())
cLApConfigRfTagName.setMaxAccess(_C)
if mibBuilder.loadTexts:cLApConfigRfTagName.setStatus(_A)
class _CLApConfigSiteTagName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CLApConfigSiteTagName_Type.__name__=_D
_CLApConfigSiteTagName_Object=MibTableColumn
cLApConfigSiteTagName=_CLApConfigSiteTagName_Object((1,3,6,1,4,1,9,9,987,1,4,1,1,4),_CLApConfigSiteTagName_Type())
cLApConfigSiteTagName.setMaxAccess(_C)
if mibBuilder.loadTexts:cLApConfigSiteTagName.setStatus(_A)
_CLApConfigTagRowStatus_Type=RowStatus
_CLApConfigTagRowStatus_Object=MibTableColumn
cLApConfigTagRowStatus=_CLApConfigTagRowStatus_Object((1,3,6,1,4,1,9,9,987,1,4,1,1,5),_CLApConfigTagRowStatus_Type())
cLApConfigTagRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cLApConfigTagRowStatus.setStatus(_A)
_CLApTagSrcTable_Object=MibTable
cLApTagSrcTable=_CLApTagSrcTable_Object((1,3,6,1,4,1,9,9,987,1,4,2))
if mibBuilder.loadTexts:cLApTagSrcTable.setStatus(_A)
_CLApTagSrcEntry_Object=MibTableRow
cLApTagSrcEntry=_CLApTagSrcEntry_Object((1,3,6,1,4,1,9,9,987,1,4,2,1))
cLApTagSrcEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:cLApTagSrcEntry.setStatus(_A)
class _CLApTagSrcPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_CLApTagSrcPriority_Type.__name__=_G
_CLApTagSrcPriority_Object=MibTableColumn
cLApTagSrcPriority=_CLApTagSrcPriority_Object((1,3,6,1,4,1,9,9,987,1,4,2,1,1),_CLApTagSrcPriority_Type())
cLApTagSrcPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:cLApTagSrcPriority.setStatus(_A)
_CLApTagSrcRowStatus_Type=RowStatus
_CLApTagSrcRowStatus_Object=MibTableColumn
cLApTagSrcRowStatus=_CLApTagSrcRowStatus_Object((1,3,6,1,4,1,9,9,987,1,4,2,1,2),_CLApTagSrcRowStatus_Type())
cLApTagSrcRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cLApTagSrcRowStatus.setStatus(_A)
class _CLApTagSrcList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('static',2),('filter',3),('ap',4),('default',5),('location',6)))
_CLApTagSrcList_Type.__name__=_G
_CLApTagSrcList_Object=MibTableColumn
cLApTagSrcList=_CLApTagSrcList_Object((1,3,6,1,4,1,9,9,987,1,4,2,1,3),_CLApTagSrcList_Type())
cLApTagSrcList.setMaxAccess(_E)
if mibBuilder.loadTexts:cLApTagSrcList.setStatus(_A)
_CiscoLwappApFilter_ObjectIdentity=ObjectIdentity
ciscoLwappApFilter=_CiscoLwappApFilter_ObjectIdentity((1,3,6,1,4,1,9,9,987,1,5))
_CLApFilterTable_Object=MibTable
cLApFilterTable=_CLApFilterTable_Object((1,3,6,1,4,1,9,9,987,1,5,1))
if mibBuilder.loadTexts:cLApFilterTable.setStatus(_A)
_CLApFilterEntry_Object=MibTableRow
cLApFilterEntry=_CLApFilterEntry_Object((1,3,6,1,4,1,9,9,987,1,5,1,1))
cLApFilterEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:cLApFilterEntry.setStatus(_A)
class _CLApFilterName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CLApFilterName_Type.__name__=_D
_CLApFilterName_Object=MibTableColumn
cLApFilterName=_CLApFilterName_Object((1,3,6,1,4,1,9,9,987,1,5,1,1,1),_CLApFilterName_Type())
cLApFilterName.setMaxAccess(_F)
if mibBuilder.loadTexts:cLApFilterName.setStatus(_A)
_CLApFilterRowStatus_Type=RowStatus
_CLApFilterRowStatus_Object=MibTableColumn
cLApFilterRowStatus=_CLApFilterRowStatus_Object((1,3,6,1,4,1,9,9,987,1,5,1,1,2),_CLApFilterRowStatus_Type())
cLApFilterRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cLApFilterRowStatus.setStatus(_A)
_CLApFilterNameApNameRule_Type=SnmpAdminString
_CLApFilterNameApNameRule_Object=MibTableColumn
cLApFilterNameApNameRule=_CLApFilterNameApNameRule_Object((1,3,6,1,4,1,9,9,987,1,5,1,1,3),_CLApFilterNameApNameRule_Type())
cLApFilterNameApNameRule.setMaxAccess(_C)
if mibBuilder.loadTexts:cLApFilterNameApNameRule.setStatus(_A)
_CLApFilterPolicyTag_Type=SnmpAdminString
_CLApFilterPolicyTag_Object=MibTableColumn
cLApFilterPolicyTag=_CLApFilterPolicyTag_Object((1,3,6,1,4,1,9,9,987,1,5,1,1,4),_CLApFilterPolicyTag_Type())
cLApFilterPolicyTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cLApFilterPolicyTag.setStatus(_A)
_CLApFilterSiteTag_Type=SnmpAdminString
_CLApFilterSiteTag_Object=MibTableColumn
cLApFilterSiteTag=_CLApFilterSiteTag_Object((1,3,6,1,4,1,9,9,987,1,5,1,1,5),_CLApFilterSiteTag_Type())
cLApFilterSiteTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cLApFilterSiteTag.setStatus(_A)
_CLApFilterRfTag_Type=SnmpAdminString
_CLApFilterRfTag_Object=MibTableColumn
cLApFilterRfTag=_CLApFilterRfTag_Object((1,3,6,1,4,1,9,9,987,1,5,1,1,6),_CLApFilterRfTag_Type())
cLApFilterRfTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cLApFilterRfTag.setStatus(_A)
_CLApFilterPriorityTable_Object=MibTable
cLApFilterPriorityTable=_CLApFilterPriorityTable_Object((1,3,6,1,4,1,9,9,987,1,5,2))
if mibBuilder.loadTexts:cLApFilterPriorityTable.setStatus(_A)
_CLApFilterPriorityEntry_Object=MibTableRow
cLApFilterPriorityEntry=_CLApFilterPriorityEntry_Object((1,3,6,1,4,1,9,9,987,1,5,2,1))
cLApFilterPriorityEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:cLApFilterPriorityEntry.setStatus(_A)
class _CLApFilterPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_CLApFilterPriority_Type.__name__=_G
_CLApFilterPriority_Object=MibTableColumn
cLApFilterPriority=_CLApFilterPriority_Object((1,3,6,1,4,1,9,9,987,1,5,2,1,1),_CLApFilterPriority_Type())
cLApFilterPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:cLApFilterPriority.setStatus(_A)
_CLApFilterPriorityRowStatus_Type=RowStatus
_CLApFilterPriorityRowStatus_Object=MibTableColumn
cLApFilterPriorityRowStatus=_CLApFilterPriorityRowStatus_Object((1,3,6,1,4,1,9,9,987,1,5,2,1,2),_CLApFilterPriorityRowStatus_Type())
cLApFilterPriorityRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cLApFilterPriorityRowStatus.setStatus(_A)
_CLApFilterPriorityFilterName_Type=SnmpAdminString
_CLApFilterPriorityFilterName_Object=MibTableColumn
cLApFilterPriorityFilterName=_CLApFilterPriorityFilterName_Object((1,3,6,1,4,1,9,9,987,1,5,2,1,3),_CLApFilterPriorityFilterName_Type())
cLApFilterPriorityFilterName.setMaxAccess(_C)
if mibBuilder.loadTexts:cLApFilterPriorityFilterName.setStatus(_A)
_CiscoLwappTagsMIBConform_ObjectIdentity=ObjectIdentity
ciscoLwappTagsMIBConform=_CiscoLwappTagsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,987,2))
_CiscoLwappTagsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLwappTagsMIBCompliances=_CiscoLwappTagsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,987,2,1))
_CiscoLwappTagsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLwappTagsMIBGroups=_CiscoLwappTagsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,987,2,2))
ciscoLwappTagsConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,987,2,2,1))
ciscoLwappTagsConfigGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ciscoLwappTagsConfigGroup.setStatus(_A)
ciscoLwappFilterConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,987,2,2,2))
ciscoLwappFilterConfigGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:ciscoLwappFilterConfigGroup.setStatus(_A)
ciscoLwappRlanConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,987,2,2,3))
ciscoLwappRlanConfigGroup.setObjects(*((_B,_w),(_B,_x)))
if mibBuilder.loadTexts:ciscoLwappRlanConfigGroup.setStatus(_A)
ciscoLwappApLocationConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,987,2,2,4))
ciscoLwappApLocationConfigGroup.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:ciscoLwappApLocationConfigGroup.setStatus(_A)
ciscoLwappTagsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,987,2,1,1))
ciscoLwappTagsMIBCompliance.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:ciscoLwappTagsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoLwappTagsMIB':ciscoLwappTagsMIB,'ciscoLwappTagsMIBNotifs':ciscoLwappTagsMIBNotifs,'ciscoLwappApLocationConfig':ciscoLwappApLocationConfig,'cLApLocationConfigTable':cLApLocationConfigTable,'cLApLocationConfigEntry':cLApLocationConfigEntry,_J:cLApLocationName,_y:cLApLocationSiteTag,_z:cLApLocationRfTag,_A0:cLApLocationPolicyTag,_A1:cLApLocationConfigRowStatus,_A2:cLApLocationDesc,'ciscoLwappAssociatedApsConfig':ciscoLwappAssociatedApsConfig,'cLAssociatedApsConfigTable':cLAssociatedApsConfigTable,'cLAssociatedApsConfigEntry':cLAssociatedApsConfigEntry,_K:cLAssociatedApsApMac,_A3:cLAssociatedApsConfigRowStatus,'ciscoLwappTagsMIBObjects':ciscoLwappTagsMIBObjects,'ciscoLwappPolicyTagConfig':ciscoLwappPolicyTagConfig,'cLPolicyTagConfigTable':cLPolicyTagConfigTable,'cLPolicyTagConfigEntry':cLPolicyTagConfigEntry,_H:cLPolicyTagName,_T:cLPolicyTagDescription,_U:cLPolicyTagRowStatus,'cLPolicyProfileConfigTable':cLPolicyProfileConfigTable,'cLPolicyProfileConfigEntry':cLPolicyProfileConfigEntry,_L:cLProfileName,_V:cLPolicyProfileName,_W:cLPolicyProfileRowStatus,'cLRlanPolicyProfileConfigTable':cLRlanPolicyProfileConfigTable,'cLRlanPolicyProfileConfigEntry':cLRlanPolicyProfileConfigEntry,_M:cLRlanPortID,'cLRlanProfile':cLRlanProfile,_w:cLRlanPolicyProfile,_x:cLRlanPolicyProfileRowStatus,'ciscoLwappSiteTagConfig':ciscoLwappSiteTagConfig,'cLSiteTagConfigTable':cLSiteTagConfigTable,'cLSiteTagConfigEntry':cLSiteTagConfigEntry,_N:cLSiteTagName,_c:cLSiteTagRowStatus,_d:cLApJoinProfName,_e:cLFlexProfName,_f:cLSiteTagDescription,_g:cLReapSiteUpgradeStart,_h:cLReapSiteTagStartCertificateDownload,_i:cLIsLocalSite,'ciscoLwappRfTagConfig':ciscoLwappRfTagConfig,'cLRfTagConfigTable':cLRfTagConfigTable,'cLRfTagConfigEntry':cLRfTagConfigEntry,_O:cLRfTagName,_X:cLRfTagRowStatus,_Z:cL11aRfProfName,_a:cL11bRfProfName,_Y:cLRfTagDescription,_b:cL6GHzBandRfProfName,'ciscoLwappApTag':ciscoLwappApTag,'cLApConfigTagTable':cLApConfigTagTable,'cLApConfigTagEntry':cLApConfigTagEntry,_P:cLApConfigTagSysMacAddress,_j:cLApConfigPolicyTagName,_k:cLApConfigRfTagName,_l:cLApConfigSiteTagName,_m:cLApConfigTagRowStatus,'cLApTagSrcTable':cLApTagSrcTable,'cLApTagSrcEntry':cLApTagSrcEntry,_Q:cLApTagSrcPriority,_n:cLApTagSrcRowStatus,_o:cLApTagSrcList,'ciscoLwappApFilter':ciscoLwappApFilter,'cLApFilterTable':cLApFilterTable,'cLApFilterEntry':cLApFilterEntry,_R:cLApFilterName,_p:cLApFilterRowStatus,_q:cLApFilterNameApNameRule,_r:cLApFilterPolicyTag,_t:cLApFilterSiteTag,_s:cLApFilterRfTag,'cLApFilterPriorityTable':cLApFilterPriorityTable,'cLApFilterPriorityEntry':cLApFilterPriorityEntry,_S:cLApFilterPriority,_u:cLApFilterPriorityRowStatus,_v:cLApFilterPriorityFilterName,'ciscoLwappTagsMIBConform':ciscoLwappTagsMIBConform,'ciscoLwappTagsMIBCompliances':ciscoLwappTagsMIBCompliances,'ciscoLwappTagsMIBCompliance':ciscoLwappTagsMIBCompliance,'ciscoLwappTagsMIBGroups':ciscoLwappTagsMIBGroups,_A4:ciscoLwappTagsConfigGroup,_A5:ciscoLwappFilterConfigGroup,_A6:ciscoLwappRlanConfigGroup,_A7:ciscoLwappApLocationConfigGroup})