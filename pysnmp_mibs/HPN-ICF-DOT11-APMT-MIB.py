_As='hpnicfDot11APMtActiveBand'
_Ar='hpnicfDot11APMtOldBand'
_Aq='hpnicfDot11APMtCurCellId'
_Ap='hpnicfDot11APMtOldCellId'
_Ao='hpnicfDot11APMtUpLinkSwitchTime'
_An='hpnicfDot11APMtUpLinkSwitchInfo'
_Am='hpnicfDot11APTrapUserThreshold'
_Al='hpnicfDot11APTrapUserCnt'
_Ak='hpnicfDot11APRadioDownReason'
_Aj='hpnicfDot11CurrAPSoftwareVersion'
_Ai='hpnicfDot11CurrAPIPAddress'
_Ah='hpnicfDot11CurrAPName'
_Ag='hpnicfDot11APMtFormerApVersion'
_Af='hpnicfDot11APMtTrapOldIPAddr'
_Ae='hpnicfDot11APIPAddress'
_Ad='hpnicfDot11APMtChanlChgCount'
_Ac='hpnicfDot11APMtTrapNewChannel'
_Ab='hpnicfDot11APMtTrapOldChannel'
_Aa='hpnicfDot11APChannelChgMode'
_AZ='hpnicfDot11APMtTrapRadioFailReason'
_AY='hpnicfDot11APMtTrapCfgErrReason'
_AX='hpnicfDot11APChgWorkMode'
_AW='hpnicfDot11APUserMacAddr2CM'
_AV='hpnicfDot11APPacketMCS2Rate'
_AU='hpnicfDot11SSIDIndex'
_AT='portalAuth'
_AS='associateAuth'
_AR='hpnicfDot11APUserMacAddr'
_AQ='hpnicfDot11APPacketMCSRate'
_AP='hpnicfDot11APPacketRate'
_AO='hpnicfDot11APPacketSize'
_AN='hpnicfDot11MngFrmType'
_AM='lowerLayerDown'
_AL='notPresent'
_AK='hpnicfDot11APAssocFailStatis2Type'
_AJ='hpnicfDot11APDeassocStatisType'
_AI='exception'
_AH='stationLeaving'
_AG='hpnicfDot11APDeauthStatisType'
_AF='hpnicfDot11UserAuthStatisType'
_AE='hpnicfDot11APReassocStatisType'
_AD='hpnicfDot11APAssocFailStatisType'
_AC='hpnicfDot11APAuthFailStatisType'
_AB='deauthentication'
_AA='authentication'
_A9='disassociation'
_A8='probeResp'
_A7='reassocResp'
_A6='reassocReq'
_A5='assocResp'
_A4='hpnicfDot11MngFrameType'
_A3='hpnicfDot11RadioStatisIndex'
_A2='hpnicfDot11APIdleTemplateName'
_A1='downloadingImage'
_A0='hpnicfDot11APConfigSPID'
_z='hpnicfDot11APModelAlias'
_y='admindown'
_x='normal'
_w='config'
_v='HpnicfDot11MACModeType'
_u='hpnicfDot11APMtAdjChannel'
_t='hpnicfDot11APMemRTUsage'
_s='hpnicfDot11APCPURTUsage'
_r='hpnicfDot11StaFullReason'
_q='hpnicfDot11StaLimitNumber'
_p='hpnicfDot11InterfMacList'
_o='hpnicfDot11CurrInterfDetectedNum'
_n='hpnicfDot11APIntfDevMACAddress'
_m='shortResource'
_l='deassociated'
_k='associated'
_j='dBm'
_i='kbytes'
_h='hpnicfDot11APElementIndex'
_g='HPN-ICF-DOT11-REF-MIB'
_f='unknown'
_e='total'
_d='rejected'
_c='overtime'
_b='invalidation'
_a='hpnicfDot11APIfIndex'
_Z='hpnicfDot11APObjID'
_Y='read-write'
_X='testing'
_W='down'
_V='up'
_U='hpnicfDot11APMtChannel'
_T='bytes'
_S='OctetString'
_R='hpnicfDot11APMtInterfMacAdd'
_Q='other'
_P='hpnicfDot11WlanID'
_O='hpnicfDot11APMtRadioID'
_N='hpnicfDot11Channel'
_M='onepercent'
_L='hpnicfDot11APID'
_K='hpnicfDot11APMtFirstTrapTime'
_J='hpnicfDot11APMtAPID'
_I='hpnicfDot11APMtTrapAPMacAddress'
_H='not-accessible'
_G='hpnicfDot11RadioID'
_F='accessible-for-notify'
_E='hpnicfDot11CurAPID'
_D='Integer32'
_C='HPN-ICF-DOT11-APMT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HpnicfDot11ChannelScopeType,HpnicfDot11MACModeType,HpnicfDot11NotifyReasonType,HpnicfDot11ObjectIDType,HpnicfDot11RFModeType,HpnicfDot11RadioElementIndex,HpnicfDot11RadioScopeType,HpnicfDot11SSIDStringType,HpnicfDot11ServicePolicyIDType,HpnicfDot11TxPwrLevelScopeType,hpnicfDot11,hpnicfDot11APElementIndex=mibBuilder.importSymbols(_g,'HpnicfDot11ChannelScopeType',_v,'HpnicfDot11NotifyReasonType','HpnicfDot11ObjectIDType','HpnicfDot11RFModeType','HpnicfDot11RadioElementIndex','HpnicfDot11RadioScopeType','HpnicfDot11SSIDStringType','HpnicfDot11ServicePolicyIDType','HpnicfDot11TxPwrLevelScopeType','hpnicfDot11',_h)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp','TruthValue')
hpnicfDot11APMT=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,2))
if mibBuilder.loadTexts:hpnicfDot11APMT.setRevisions(('2012-05-07 18:00','2010-10-11 18:00','2010-09-15 12:00','2009-08-07 18:00','2009-07-29 18:00','2009-05-07 20:00','2008-11-07 10:00','2008-07-09 18:00','2008-02-25 18:00','2007-12-21 18:00','2007-06-19 18:00','2007-04-27 20:00','2007-02-01 20:00','2006-05-10 19:00'))
_HpnicfDot11APObjectGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11APObjectGroup=_HpnicfDot11APObjectGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1))
_HpnicfDot11APObjectStatusTable_Object=MibTable
hpnicfDot11APObjectStatusTable=_HpnicfDot11APObjectStatusTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,1))
if mibBuilder.loadTexts:hpnicfDot11APObjectStatusTable.setStatus(_A)
_HpnicfDot11APObjectStatusEntry_Object=MibTableRow
hpnicfDot11APObjectStatusEntry=_HpnicfDot11APObjectStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,1,1))
hpnicfDot11APObjectStatusEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:hpnicfDot11APObjectStatusEntry.setStatus(_A)
_HpnicfDot11APID_Type=HpnicfDot11ObjectIDType
_HpnicfDot11APID_Object=MibTableColumn
hpnicfDot11APID=_HpnicfDot11APID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,1,1,1),_HpnicfDot11APID_Type())
hpnicfDot11APID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APID.setStatus(_A)
_HpnicfDot11APIPAddress_Type=IpAddress
_HpnicfDot11APIPAddress_Object=MibTableColumn
hpnicfDot11APIPAddress=_HpnicfDot11APIPAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,1,1,2),_HpnicfDot11APIPAddress_Type())
hpnicfDot11APIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIPAddress.setStatus(_A)
_HpnicfDot11APMacAddress_Type=MacAddress
_HpnicfDot11APMacAddress_Object=MibTableColumn
hpnicfDot11APMacAddress=_HpnicfDot11APMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,1,1,3),_HpnicfDot11APMacAddress_Type())
hpnicfDot11APMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APMacAddress.setStatus(_A)
class _HpnicfDot11APOperationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('join',1),('joinConfirm',2),('download',3),(_w,4),('run',5)))
_HpnicfDot11APOperationStatus_Type.__name__=_D
_HpnicfDot11APOperationStatus_Object=MibTableColumn
hpnicfDot11APOperationStatus=_HpnicfDot11APOperationStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,1,1,4),_HpnicfDot11APOperationStatus_Type())
hpnicfDot11APOperationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APOperationStatus.setStatus(_A)
_HpnicfDot11APTemplateNameOfAP_Type=OctetString
_HpnicfDot11APTemplateNameOfAP_Object=MibTableColumn
hpnicfDot11APTemplateNameOfAP=_HpnicfDot11APTemplateNameOfAP_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,1,1,5),_HpnicfDot11APTemplateNameOfAP_Type())
hpnicfDot11APTemplateNameOfAP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APTemplateNameOfAP.setStatus(_A)
_HpnicfDot11APReset_Type=TruthValue
_HpnicfDot11APReset_Object=MibTableColumn
hpnicfDot11APReset=_HpnicfDot11APReset_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,1,1,6),_HpnicfDot11APReset_Type())
hpnicfDot11APReset.setMaxAccess(_Y)
if mibBuilder.loadTexts:hpnicfDot11APReset.setStatus(_A)
class _HpnicfDot11APCpuUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11APCpuUsage_Type.__name__=_D
_HpnicfDot11APCpuUsage_Object=MibTableColumn
hpnicfDot11APCpuUsage=_HpnicfDot11APCpuUsage_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,1,1,7),_HpnicfDot11APCpuUsage_Type())
hpnicfDot11APCpuUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APCpuUsage.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APCpuUsage.setUnits(_M)
class _HpnicfDot11APConnectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),('notAvailable',3)))
_HpnicfDot11APConnectionType_Type.__name__=_D
_HpnicfDot11APConnectionType_Object=MibTableColumn
hpnicfDot11APConnectionType=_HpnicfDot11APConnectionType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,1,1,8),_HpnicfDot11APConnectionType_Type())
hpnicfDot11APConnectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APConnectionType.setStatus(_A)
_HpnicfDot11APLastImgDownloadTime_Type=DateAndTime
_HpnicfDot11APLastImgDownloadTime_Object=MibTableColumn
hpnicfDot11APLastImgDownloadTime=_HpnicfDot11APLastImgDownloadTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,1,1,9),_HpnicfDot11APLastImgDownloadTime_Type())
hpnicfDot11APLastImgDownloadTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APLastImgDownloadTime.setStatus(_A)
_HpnicfDot11APIPv6Address_Type=OctetString
_HpnicfDot11APIPv6Address_Object=MibTableColumn
hpnicfDot11APIPv6Address=_HpnicfDot11APIPv6Address_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,1,1,10),_HpnicfDot11APIPv6Address_Type())
hpnicfDot11APIPv6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIPv6Address.setStatus(_A)
_HpnicfDot11APLastRegisterTime_Type=DateAndTime
_HpnicfDot11APLastRegisterTime_Object=MibTableColumn
hpnicfDot11APLastRegisterTime=_HpnicfDot11APLastRegisterTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,1,1,11),_HpnicfDot11APLastRegisterTime_Type())
hpnicfDot11APLastRegisterTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APLastRegisterTime.setStatus(_A)
class _HpnicfDot11APResetCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_x,0),('restart',1)))
_HpnicfDot11APResetCM_Type.__name__=_D
_HpnicfDot11APResetCM_Object=MibTableColumn
hpnicfDot11APResetCM=_HpnicfDot11APResetCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,1,1,12),_HpnicfDot11APResetCM_Type())
hpnicfDot11APResetCM.setMaxAccess(_Y)
if mibBuilder.loadTexts:hpnicfDot11APResetCM.setStatus(_A)
_HpnicfDot11APObjectTable_Object=MibTable
hpnicfDot11APObjectTable=_HpnicfDot11APObjectTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2))
if mibBuilder.loadTexts:hpnicfDot11APObjectTable.setStatus(_A)
_HpnicfDot11APObjectEntry_Object=MibTableRow
hpnicfDot11APObjectEntry=_HpnicfDot11APObjectEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1))
hpnicfDot11APObjectEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:hpnicfDot11APObjectEntry.setStatus(_A)
_HpnicfDot11APObjID_Type=HpnicfDot11ObjectIDType
_HpnicfDot11APObjID_Object=MibTableColumn
hpnicfDot11APObjID=_HpnicfDot11APObjID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,1),_HpnicfDot11APObjID_Type())
hpnicfDot11APObjID.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APObjID.setStatus(_A)
_HpnicfDot11CurrAPIPAddress_Type=IpAddress
_HpnicfDot11CurrAPIPAddress_Object=MibTableColumn
hpnicfDot11CurrAPIPAddress=_HpnicfDot11CurrAPIPAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,2),_HpnicfDot11CurrAPIPAddress_Type())
hpnicfDot11CurrAPIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPIPAddress.setStatus(_A)
_HpnicfDot11CurrAPMacAddress_Type=MacAddress
_HpnicfDot11CurrAPMacAddress_Object=MibTableColumn
hpnicfDot11CurrAPMacAddress=_HpnicfDot11CurrAPMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,3),_HpnicfDot11CurrAPMacAddress_Type())
hpnicfDot11CurrAPMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPMacAddress.setStatus(_A)
_HpnicfDot11CurrACPortIndex_Type=Integer32
_HpnicfDot11CurrACPortIndex_Object=MibTableColumn
hpnicfDot11CurrACPortIndex=_HpnicfDot11CurrACPortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,4),_HpnicfDot11CurrACPortIndex_Type())
hpnicfDot11CurrACPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrACPortIndex.setStatus(_A)
_HpnicfDot11CurrAPMACMode_Type=HpnicfDot11MACModeType
_HpnicfDot11CurrAPMACMode_Object=MibTableColumn
hpnicfDot11CurrAPMACMode=_HpnicfDot11CurrAPMACMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,5),_HpnicfDot11CurrAPMACMode_Type())
hpnicfDot11CurrAPMACMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPMACMode.setStatus(_A)
_HpnicfDot11CurrAPTemplateName_Type=OctetString
_HpnicfDot11CurrAPTemplateName_Object=MibTableColumn
hpnicfDot11CurrAPTemplateName=_HpnicfDot11CurrAPTemplateName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,6),_HpnicfDot11CurrAPTemplateName_Type())
hpnicfDot11CurrAPTemplateName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPTemplateName.setStatus(_A)
_HpnicfDot11CurrAPStationAssocCount_Type=Integer32
_HpnicfDot11CurrAPStationAssocCount_Object=MibTableColumn
hpnicfDot11CurrAPStationAssocCount=_HpnicfDot11CurrAPStationAssocCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,7),_HpnicfDot11CurrAPStationAssocCount_Type())
hpnicfDot11CurrAPStationAssocCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPStationAssocCount.setStatus(_A)
_HpnicfDot11CurrAPName_Type=OctetString
_HpnicfDot11CurrAPName_Object=MibTableColumn
hpnicfDot11CurrAPName=_HpnicfDot11CurrAPName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,8),_HpnicfDot11CurrAPName_Type())
hpnicfDot11CurrAPName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPName.setStatus(_A)
_HpnicfDot11CurrAPModelName_Type=OctetString
_HpnicfDot11CurrAPModelName_Object=MibTableColumn
hpnicfDot11CurrAPModelName=_HpnicfDot11CurrAPModelName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,9),_HpnicfDot11CurrAPModelName_Type())
hpnicfDot11CurrAPModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPModelName.setStatus(_A)
_HpnicfDot11CurrAPImageName_Type=OctetString
_HpnicfDot11CurrAPImageName_Object=MibTableColumn
hpnicfDot11CurrAPImageName=_HpnicfDot11CurrAPImageName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,10),_HpnicfDot11CurrAPImageName_Type())
hpnicfDot11CurrAPImageName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPImageName.setStatus(_A)
_HpnicfDot11CurrAPSoftwareVersion_Type=OctetString
_HpnicfDot11CurrAPSoftwareVersion_Object=MibTableColumn
hpnicfDot11CurrAPSoftwareVersion=_HpnicfDot11CurrAPSoftwareVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,11),_HpnicfDot11CurrAPSoftwareVersion_Type())
hpnicfDot11CurrAPSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPSoftwareVersion.setStatus(_A)
_HpnicfDot11CurrAPIPNetMask_Type=IpAddress
_HpnicfDot11CurrAPIPNetMask_Object=MibTableColumn
hpnicfDot11CurrAPIPNetMask=_HpnicfDot11CurrAPIPNetMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,12),_HpnicfDot11CurrAPIPNetMask_Type())
hpnicfDot11CurrAPIPNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPIPNetMask.setStatus(_A)
_HpnicfDot11CurrRadioModeSupport_Type=Integer32
_HpnicfDot11CurrRadioModeSupport_Object=MibTableColumn
hpnicfDot11CurrRadioModeSupport=_HpnicfDot11CurrRadioModeSupport_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,13),_HpnicfDot11CurrRadioModeSupport_Type())
hpnicfDot11CurrRadioModeSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrRadioModeSupport.setStatus(_A)
_HpnicfDot11CurrIfNumber_Type=Integer32
_HpnicfDot11CurrIfNumber_Object=MibTableColumn
hpnicfDot11CurrIfNumber=_HpnicfDot11CurrIfNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,14),_HpnicfDot11CurrIfNumber_Type())
hpnicfDot11CurrIfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrIfNumber.setStatus(_A)
_HpnicfDot11CurrAPElementID_Type=Integer32
_HpnicfDot11CurrAPElementID_Object=MibTableColumn
hpnicfDot11CurrAPElementID=_HpnicfDot11CurrAPElementID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,15),_HpnicfDot11CurrAPElementID_Type())
hpnicfDot11CurrAPElementID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPElementID.setStatus(_A)
class _HpnicfDot11CurrAPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bridge',1),('route',2)))
_HpnicfDot11CurrAPMode_Type.__name__=_D
_HpnicfDot11CurrAPMode_Object=MibTableColumn
hpnicfDot11CurrAPMode=_HpnicfDot11CurrAPMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,16),_HpnicfDot11CurrAPMode_Type())
hpnicfDot11CurrAPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPMode.setStatus(_A)
_HpnicfDot11CurrAPIPv6Address_Type=OctetString
_HpnicfDot11CurrAPIPv6Address_Object=MibTableColumn
hpnicfDot11CurrAPIPv6Address=_HpnicfDot11CurrAPIPv6Address_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,17),_HpnicfDot11CurrAPIPv6Address_Type())
hpnicfDot11CurrAPIPv6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPIPv6Address.setStatus(_A)
_HpnicfDot11CurrAPSSIDNumber_Type=Integer32
_HpnicfDot11CurrAPSSIDNumber_Object=MibTableColumn
hpnicfDot11CurrAPSSIDNumber=_HpnicfDot11CurrAPSSIDNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,18),_HpnicfDot11CurrAPSSIDNumber_Type())
hpnicfDot11CurrAPSSIDNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPSSIDNumber.setStatus(_A)
_HpnicfDot11CurrAPManufacturer_Type=OctetString
_HpnicfDot11CurrAPManufacturer_Object=MibTableColumn
hpnicfDot11CurrAPManufacturer=_HpnicfDot11CurrAPManufacturer_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,19),_HpnicfDot11CurrAPManufacturer_Type())
hpnicfDot11CurrAPManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPManufacturer.setStatus(_A)
_HpnicfDot11CurrAPMemorySize_Type=Integer32
_HpnicfDot11CurrAPMemorySize_Object=MibTableColumn
hpnicfDot11CurrAPMemorySize=_HpnicfDot11CurrAPMemorySize_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,20),_HpnicfDot11CurrAPMemorySize_Type())
hpnicfDot11CurrAPMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPMemorySize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11CurrAPMemorySize.setUnits(_i)
_HpnicfDot11CurrAPMemSizeInBytes_Type=Integer32
_HpnicfDot11CurrAPMemSizeInBytes_Object=MibTableColumn
hpnicfDot11CurrAPMemSizeInBytes=_HpnicfDot11CurrAPMemSizeInBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,21),_HpnicfDot11CurrAPMemSizeInBytes_Type())
hpnicfDot11CurrAPMemSizeInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPMemSizeInBytes.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11CurrAPMemSizeInBytes.setUnits(_T)
_HpnicfDot11CurrAPFlashSize_Type=Integer32
_HpnicfDot11CurrAPFlashSize_Object=MibTableColumn
hpnicfDot11CurrAPFlashSize=_HpnicfDot11CurrAPFlashSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,22),_HpnicfDot11CurrAPFlashSize_Type())
hpnicfDot11CurrAPFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPFlashSize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11CurrAPFlashSize.setUnits('Kbytes')
_HpnicfDot11CurrAPFlashSizeInBytes_Type=Integer32
_HpnicfDot11CurrAPFlashSizeInBytes_Object=MibTableColumn
hpnicfDot11CurrAPFlashSizeInBytes=_HpnicfDot11CurrAPFlashSizeInBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,23),_HpnicfDot11CurrAPFlashSizeInBytes_Type())
hpnicfDot11CurrAPFlashSizeInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPFlashSizeInBytes.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11CurrAPFlashSizeInBytes.setUnits(_T)
_HpnicfDot11CurrAPReleasedVersion_Type=OctetString
_HpnicfDot11CurrAPReleasedVersion_Object=MibTableColumn
hpnicfDot11CurrAPReleasedVersion=_HpnicfDot11CurrAPReleasedVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,24),_HpnicfDot11CurrAPReleasedVersion_Type())
hpnicfDot11CurrAPReleasedVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPReleasedVersion.setStatus(_A)
_HpnicfDot11CurrRadioModeSupport2_Type=Integer32
_HpnicfDot11CurrRadioModeSupport2_Object=MibTableColumn
hpnicfDot11CurrRadioModeSupport2=_HpnicfDot11CurrRadioModeSupport2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,25),_HpnicfDot11CurrRadioModeSupport2_Type())
hpnicfDot11CurrRadioModeSupport2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrRadioModeSupport2.setStatus(_A)
_HpnicfDot11CurrAPCPUTypeCM_Type=OctetString
_HpnicfDot11CurrAPCPUTypeCM_Object=MibTableColumn
hpnicfDot11CurrAPCPUTypeCM=_HpnicfDot11CurrAPCPUTypeCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,26),_HpnicfDot11CurrAPCPUTypeCM_Type())
hpnicfDot11CurrAPCPUTypeCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPCPUTypeCM.setStatus(_A)
_HpnicfDot11CurrAPMemoryTypeCM_Type=OctetString
_HpnicfDot11CurrAPMemoryTypeCM_Object=MibTableColumn
hpnicfDot11CurrAPMemoryTypeCM=_HpnicfDot11CurrAPMemoryTypeCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,27),_HpnicfDot11CurrAPMemoryTypeCM_Type())
hpnicfDot11CurrAPMemoryTypeCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPMemoryTypeCM.setStatus(_A)
_HpnicfDot11CurrAPBSSIDNumberCM_Type=Integer32
_HpnicfDot11CurrAPBSSIDNumberCM_Object=MibTableColumn
hpnicfDot11CurrAPBSSIDNumberCM=_HpnicfDot11CurrAPBSSIDNumberCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,2,1,28),_HpnicfDot11CurrAPBSSIDNumberCM_Type())
hpnicfDot11CurrAPBSSIDNumberCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrAPBSSIDNumberCM.setStatus(_A)
_HpnicfDot11APRadioTable_Object=MibTable
hpnicfDot11APRadioTable=_HpnicfDot11APRadioTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3))
if mibBuilder.loadTexts:hpnicfDot11APRadioTable.setStatus(_A)
_HpnicfDot11APRadioEntry_Object=MibTableRow
hpnicfDot11APRadioEntry=_HpnicfDot11APRadioEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1))
hpnicfDot11APRadioEntry.setIndexNames((0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:hpnicfDot11APRadioEntry.setStatus(_A)
class _HpnicfDot11CurAPID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfDot11CurAPID_Type.__name__=_S
_HpnicfDot11CurAPID_Object=MibTableColumn
hpnicfDot11CurAPID=_HpnicfDot11CurAPID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,1),_HpnicfDot11CurAPID_Type())
hpnicfDot11CurAPID.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11CurAPID.setStatus(_A)
class _HpnicfDot11RadioID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfDot11RadioID_Type.__name__=_D
_HpnicfDot11RadioID_Object=MibTableColumn
hpnicfDot11RadioID=_HpnicfDot11RadioID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,2),_HpnicfDot11RadioID_Type())
hpnicfDot11RadioID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11RadioID.setStatus(_A)
_HpnicfDot11AdminStatus_Type=TruthValue
_HpnicfDot11AdminStatus_Object=MibTableColumn
hpnicfDot11AdminStatus=_HpnicfDot11AdminStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,3),_HpnicfDot11AdminStatus_Type())
hpnicfDot11AdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AdminStatus.setStatus(_A)
_HpnicfDot11OperStatus_Type=TruthValue
_HpnicfDot11OperStatus_Object=MibTableColumn
hpnicfDot11OperStatus=_HpnicfDot11OperStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,4),_HpnicfDot11OperStatus_Type())
hpnicfDot11OperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11OperStatus.setStatus(_A)
_HpnicfDot11Channel_Type=HpnicfDot11ChannelScopeType
_HpnicfDot11Channel_Object=MibTableColumn
hpnicfDot11Channel=_HpnicfDot11Channel_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,5),_HpnicfDot11Channel_Type())
hpnicfDot11Channel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Channel.setStatus(_A)
_HpnicfDot11TxPowerLevel_Type=HpnicfDot11TxPwrLevelScopeType
_HpnicfDot11TxPowerLevel_Object=MibTableColumn
hpnicfDot11TxPowerLevel=_HpnicfDot11TxPowerLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,6),_HpnicfDot11TxPowerLevel_Type())
hpnicfDot11TxPowerLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxPowerLevel.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11TxPowerLevel.setUnits('dbm')
_HpnicfDot11APRadioIfIndex_Type=Integer32
_HpnicfDot11APRadioIfIndex_Object=MibTableColumn
hpnicfDot11APRadioIfIndex=_HpnicfDot11APRadioIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,7),_HpnicfDot11APRadioIfIndex_Type())
hpnicfDot11APRadioIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APRadioIfIndex.setStatus(_A)
_HpnicfDot11AntennaGain_Type=Integer32
_HpnicfDot11AntennaGain_Object=MibTableColumn
hpnicfDot11AntennaGain=_HpnicfDot11AntennaGain_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,8),_HpnicfDot11AntennaGain_Type())
hpnicfDot11AntennaGain.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AntennaGain.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11AntennaGain.setUnits('dBi')
_HpnicfDot11MaxBandwidth_Type=Integer32
_HpnicfDot11MaxBandwidth_Object=MibTableColumn
hpnicfDot11MaxBandwidth=_HpnicfDot11MaxBandwidth_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,9),_HpnicfDot11MaxBandwidth_Type())
hpnicfDot11MaxBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11MaxBandwidth.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11MaxBandwidth.setUnits('Mbps')
_HpnicfDot11ResourceUseRatio_Type=Integer32
_HpnicfDot11ResourceUseRatio_Object=MibTableColumn
hpnicfDot11ResourceUseRatio=_HpnicfDot11ResourceUseRatio_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,10),_HpnicfDot11ResourceUseRatio_Type())
hpnicfDot11ResourceUseRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ResourceUseRatio.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11ResourceUseRatio.setUnits(_M)
_HpnicfDot11RadioModeSupport_Type=Unsigned32
_HpnicfDot11RadioModeSupport_Object=MibTableColumn
hpnicfDot11RadioModeSupport=_HpnicfDot11RadioModeSupport_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,11),_HpnicfDot11RadioModeSupport_Type())
hpnicfDot11RadioModeSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioModeSupport.setStatus(_A)
class _HpnicfDot11TxPowerLevel2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_HpnicfDot11TxPowerLevel2_Type.__name__=_D
_HpnicfDot11TxPowerLevel2_Object=MibTableColumn
hpnicfDot11TxPowerLevel2=_HpnicfDot11TxPowerLevel2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,12),_HpnicfDot11TxPowerLevel2_Type())
hpnicfDot11TxPowerLevel2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxPowerLevel2.setStatus(_A)
_HpnicfDot11PowerMgmtStatus_Type=TruthValue
_HpnicfDot11PowerMgmtStatus_Object=MibTableColumn
hpnicfDot11PowerMgmtStatus=_HpnicfDot11PowerMgmtStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,13),_HpnicfDot11PowerMgmtStatus_Type())
hpnicfDot11PowerMgmtStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11PowerMgmtStatus.setStatus(_A)
_HpnicfDot11ChannelSwitchTimes_Type=Counter32
_HpnicfDot11ChannelSwitchTimes_Object=MibTableColumn
hpnicfDot11ChannelSwitchTimes=_HpnicfDot11ChannelSwitchTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,14),_HpnicfDot11ChannelSwitchTimes_Type())
hpnicfDot11ChannelSwitchTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ChannelSwitchTimes.setStatus(_A)
_HpnicfDot11AntennaType_Type=OctetString
_HpnicfDot11AntennaType_Object=MibTableColumn
hpnicfDot11AntennaType=_HpnicfDot11AntennaType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,15),_HpnicfDot11AntennaType_Type())
hpnicfDot11AntennaType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AntennaType.setStatus(_A)
_HpnicfDot11DiversitySelectionRx_Type=TruthValue
_HpnicfDot11DiversitySelectionRx_Object=MibTableColumn
hpnicfDot11DiversitySelectionRx=_HpnicfDot11DiversitySelectionRx_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,16),_HpnicfDot11DiversitySelectionRx_Type())
hpnicfDot11DiversitySelectionRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11DiversitySelectionRx.setStatus(_A)
_HpnicfDot11MaxTxPwrLvl_Type=OctetString
_HpnicfDot11MaxTxPwrLvl_Object=MibTableColumn
hpnicfDot11MaxTxPwrLvl=_HpnicfDot11MaxTxPwrLvl_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,17),_HpnicfDot11MaxTxPwrLvl_Type())
hpnicfDot11MaxTxPwrLvl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11MaxTxPwrLvl.setStatus(_A)
_HpnicfDot11PwrAttRange_Type=Integer32
_HpnicfDot11PwrAttRange_Object=MibTableColumn
hpnicfDot11PwrAttRange=_HpnicfDot11PwrAttRange_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,18),_HpnicfDot11PwrAttRange_Type())
hpnicfDot11PwrAttRange.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11PwrAttRange.setStatus(_A)
_HpnicfDot11AvgRxSignalStrength_Type=Integer32
_HpnicfDot11AvgRxSignalStrength_Object=MibTableColumn
hpnicfDot11AvgRxSignalStrength=_HpnicfDot11AvgRxSignalStrength_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,19),_HpnicfDot11AvgRxSignalStrength_Type())
hpnicfDot11AvgRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AvgRxSignalStrength.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11AvgRxSignalStrength.setUnits(_j)
_HpnicfDot11HighestRxSignalStrength_Type=Integer32
_HpnicfDot11HighestRxSignalStrength_Object=MibTableColumn
hpnicfDot11HighestRxSignalStrength=_HpnicfDot11HighestRxSignalStrength_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,20),_HpnicfDot11HighestRxSignalStrength_Type())
hpnicfDot11HighestRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11HighestRxSignalStrength.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11HighestRxSignalStrength.setUnits(_j)
_HpnicfDot11LowestRxSignalStrength_Type=Integer32
_HpnicfDot11LowestRxSignalStrength_Object=MibTableColumn
hpnicfDot11LowestRxSignalStrength=_HpnicfDot11LowestRxSignalStrength_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,21),_HpnicfDot11LowestRxSignalStrength_Type())
hpnicfDot11LowestRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LowestRxSignalStrength.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11LowestRxSignalStrength.setUnits(_j)
_HpnicfDot11RadioIfUpdownTimes_Type=Counter32
_HpnicfDot11RadioIfUpdownTimes_Object=MibTableColumn
hpnicfDot11RadioIfUpdownTimes=_HpnicfDot11RadioIfUpdownTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,22),_HpnicfDot11RadioIfUpdownTimes_Type())
hpnicfDot11RadioIfUpdownTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioIfUpdownTimes.setStatus(_A)
_HpnicfDot11RadioIfLastChange_Type=TimeTicks
_HpnicfDot11RadioIfLastChange_Object=MibTableColumn
hpnicfDot11RadioIfLastChange=_HpnicfDot11RadioIfLastChange_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,23),_HpnicfDot11RadioIfLastChange_Type())
hpnicfDot11RadioIfLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioIfLastChange.setStatus(_A)
_HpnicfDot11RadioModeSupport2_Type=Unsigned32
_HpnicfDot11RadioModeSupport2_Object=MibTableColumn
hpnicfDot11RadioModeSupport2=_HpnicfDot11RadioModeSupport2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,24),_HpnicfDot11RadioModeSupport2_Type())
hpnicfDot11RadioModeSupport2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioModeSupport2.setStatus(_A)
class _HpnicfDot11OperStatusCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_y,4)))
_HpnicfDot11OperStatusCM_Type.__name__=_D
_HpnicfDot11OperStatusCM_Object=MibTableColumn
hpnicfDot11OperStatusCM=_HpnicfDot11OperStatusCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,3,1,25),_HpnicfDot11OperStatusCM_Type())
hpnicfDot11OperStatusCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11OperStatusCM.setStatus(_A)
_HpnicfDot11APBSSTable_Object=MibTable
hpnicfDot11APBSSTable=_HpnicfDot11APBSSTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,4))
if mibBuilder.loadTexts:hpnicfDot11APBSSTable.setStatus(_A)
_HpnicfDot11APBSSEntry_Object=MibTableRow
hpnicfDot11APBSSEntry=_HpnicfDot11APBSSEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,4,1))
hpnicfDot11APBSSEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_P))
if mibBuilder.loadTexts:hpnicfDot11APBSSEntry.setStatus(_A)
class _HpnicfDot11WlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfDot11WlanID_Type.__name__=_D
_HpnicfDot11WlanID_Object=MibTableColumn
hpnicfDot11WlanID=_HpnicfDot11WlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,4,1,1),_HpnicfDot11WlanID_Type())
hpnicfDot11WlanID.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11WlanID.setStatus(_A)
_HpnicfDot11BSSID_Type=MacAddress
_HpnicfDot11BSSID_Object=MibTableColumn
hpnicfDot11BSSID=_HpnicfDot11BSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,4,1,2),_HpnicfDot11BSSID_Type())
hpnicfDot11BSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSID.setStatus(_A)
_HpnicfDot11CurrSvcPolicyID_Type=HpnicfDot11ServicePolicyIDType
_HpnicfDot11CurrSvcPolicyID_Object=MibTableColumn
hpnicfDot11CurrSvcPolicyID=_HpnicfDot11CurrSvcPolicyID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,4,1,3),_HpnicfDot11CurrSvcPolicyID_Type())
hpnicfDot11CurrSvcPolicyID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrSvcPolicyID.setStatus(_A)
_HpnicfDot11SSID_Type=OctetString
_HpnicfDot11SSID_Object=MibTableColumn
hpnicfDot11SSID=_HpnicfDot11SSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,4,1,4),_HpnicfDot11SSID_Type())
hpnicfDot11SSID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11SSID.setStatus(_A)
_HpnicfDot11CurrSSIDResourceUseRatio_Type=Integer32
_HpnicfDot11CurrSSIDResourceUseRatio_Object=MibTableColumn
hpnicfDot11CurrSSIDResourceUseRatio=_HpnicfDot11CurrSSIDResourceUseRatio_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,4,1,5),_HpnicfDot11CurrSSIDResourceUseRatio_Type())
hpnicfDot11CurrSSIDResourceUseRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CurrSSIDResourceUseRatio.setStatus(_A)
_HpnicfDot11APEssVlanId_Type=Integer32
_HpnicfDot11APEssVlanId_Object=MibTableColumn
hpnicfDot11APEssVlanId=_HpnicfDot11APEssVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,4,1,6),_HpnicfDot11APEssVlanId_Type())
hpnicfDot11APEssVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APEssVlanId.setStatus(_A)
_HpnicfDot11APModelTable_Object=MibTable
hpnicfDot11APModelTable=_HpnicfDot11APModelTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,5))
if mibBuilder.loadTexts:hpnicfDot11APModelTable.setStatus(_A)
_HpnicfDot11APModelEntry_Object=MibTableRow
hpnicfDot11APModelEntry=_HpnicfDot11APModelEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,5,1))
hpnicfDot11APModelEntry.setIndexNames((1,_C,_z))
if mibBuilder.loadTexts:hpnicfDot11APModelEntry.setStatus(_A)
class _HpnicfDot11APModelAlias_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDot11APModelAlias_Type.__name__=_S
_HpnicfDot11APModelAlias_Object=MibTableColumn
hpnicfDot11APModelAlias=_HpnicfDot11APModelAlias_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,5,1,1),_HpnicfDot11APModelAlias_Type())
hpnicfDot11APModelAlias.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APModelAlias.setStatus(_A)
_HpnicfDot11APModelName_Type=OctetString
_HpnicfDot11APModelName_Object=MibTableColumn
hpnicfDot11APModelName=_HpnicfDot11APModelName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,5,1,2),_HpnicfDot11APModelName_Type())
hpnicfDot11APModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APModelName.setStatus(_A)
_HpnicfDot11RadioNumSupport_Type=HpnicfDot11RadioScopeType
_HpnicfDot11RadioNumSupport_Object=MibTableColumn
hpnicfDot11RadioNumSupport=_HpnicfDot11RadioNumSupport_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,5,1,3),_HpnicfDot11RadioNumSupport_Type())
hpnicfDot11RadioNumSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioNumSupport.setStatus(_A)
_HpnicfDot11StationNumSupport_Type=Integer32
_HpnicfDot11StationNumSupport_Object=MibTableColumn
hpnicfDot11StationNumSupport=_HpnicfDot11StationNumSupport_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,5,1,4),_HpnicfDot11StationNumSupport_Type())
hpnicfDot11StationNumSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11StationNumSupport.setStatus(_A)
class _HpnicfDot11MACModeSupport_Type(HpnicfDot11MACModeType):defaultValue=1
_HpnicfDot11MACModeSupport_Type.__name__=_v
_HpnicfDot11MACModeSupport_Object=MibTableColumn
hpnicfDot11MACModeSupport=_HpnicfDot11MACModeSupport_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,5,1,5),_HpnicfDot11MACModeSupport_Type())
hpnicfDot11MACModeSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11MACModeSupport.setStatus(_A)
_HpnicfDot11APManufacturer_Type=OctetString
_HpnicfDot11APManufacturer_Object=MibTableColumn
hpnicfDot11APManufacturer=_HpnicfDot11APManufacturer_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,5,1,6),_HpnicfDot11APManufacturer_Type())
hpnicfDot11APManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APManufacturer.setStatus(_A)
_HpnicfDot11APCPUType_Type=OctetString
_HpnicfDot11APCPUType_Object=MibTableColumn
hpnicfDot11APCPUType=_HpnicfDot11APCPUType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,5,1,7),_HpnicfDot11APCPUType_Type())
hpnicfDot11APCPUType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APCPUType.setStatus(_A)
_HpnicfDot11APCPUClockSpeed_Type=Unsigned32
_HpnicfDot11APCPUClockSpeed_Object=MibTableColumn
hpnicfDot11APCPUClockSpeed=_HpnicfDot11APCPUClockSpeed_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,5,1,8),_HpnicfDot11APCPUClockSpeed_Type())
hpnicfDot11APCPUClockSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APCPUClockSpeed.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APCPUClockSpeed.setUnits('Hz')
_HpnicfDot11APMemoryType_Type=OctetString
_HpnicfDot11APMemoryType_Object=MibTableColumn
hpnicfDot11APMemoryType=_HpnicfDot11APMemoryType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,5,1,9),_HpnicfDot11APMemoryType_Type())
hpnicfDot11APMemoryType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APMemoryType.setStatus(_A)
_HpnicfDot11APFlashType_Type=OctetString
_HpnicfDot11APFlashType_Object=MibTableColumn
hpnicfDot11APFlashType=_HpnicfDot11APFlashType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,5,1,11),_HpnicfDot11APFlashType_Type())
hpnicfDot11APFlashType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APFlashType.setStatus(_A)
_HpnicfDot11APFlashSize_Type=Unsigned32
_HpnicfDot11APFlashSize_Object=MibTableColumn
hpnicfDot11APFlashSize=_HpnicfDot11APFlashSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,5,1,12),_HpnicfDot11APFlashSize_Type())
hpnicfDot11APFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APFlashSize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APFlashSize.setUnits(_i)
_HpnicfDot11APMemSize_Type=Gauge32
_HpnicfDot11APMemSize_Object=MibTableColumn
hpnicfDot11APMemSize=_HpnicfDot11APMemSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,5,1,13),_HpnicfDot11APMemSize_Type())
hpnicfDot11APMemSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APMemSize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APMemSize.setUnits(_T)
_HpnicfDot11APFlashSizeInBytes_Type=Unsigned32
_HpnicfDot11APFlashSizeInBytes_Object=MibTableColumn
hpnicfDot11APFlashSizeInBytes=_HpnicfDot11APFlashSizeInBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,5,1,14),_HpnicfDot11APFlashSizeInBytes_Type())
hpnicfDot11APFlashSizeInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APFlashSizeInBytes.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APFlashSizeInBytes.setUnits(_T)
_HpnicfDot11APMemorySize_Type=Unsigned32
_HpnicfDot11APMemorySize_Object=MibTableColumn
hpnicfDot11APMemorySize=_HpnicfDot11APMemorySize_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,5,1,20),_HpnicfDot11APMemorySize_Type())
hpnicfDot11APMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APMemorySize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APMemorySize.setUnits(_i)
_HpnicfDot11APIfTable_Object=MibTable
hpnicfDot11APIfTable=_HpnicfDot11APIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,6))
if mibBuilder.loadTexts:hpnicfDot11APIfTable.setStatus(_A)
_HpnicfDot11APIfEntry_Object=MibTableRow
hpnicfDot11APIfEntry=_HpnicfDot11APIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,6,1))
hpnicfDot11APIfEntry.setIndexNames((0,_C,_Z),(0,_C,_a))
if mibBuilder.loadTexts:hpnicfDot11APIfEntry.setStatus(_A)
_HpnicfDot11APIfIndex_Type=Integer32
_HpnicfDot11APIfIndex_Object=MibTableColumn
hpnicfDot11APIfIndex=_HpnicfDot11APIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,6,1,1),_HpnicfDot11APIfIndex_Type())
hpnicfDot11APIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APIfIndex.setStatus(_A)
_HpnicfDot11APIfDescr_Type=OctetString
_HpnicfDot11APIfDescr_Object=MibTableColumn
hpnicfDot11APIfDescr=_HpnicfDot11APIfDescr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,6,1,2),_HpnicfDot11APIfDescr_Type())
hpnicfDot11APIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfDescr.setStatus(_A)
_HpnicfDot11APIfType_Type=Integer32
_HpnicfDot11APIfType_Object=MibTableColumn
hpnicfDot11APIfType=_HpnicfDot11APIfType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,6,1,3),_HpnicfDot11APIfType_Type())
hpnicfDot11APIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfType.setStatus(_A)
_HpnicfDot11APIfMtu_Type=Integer32
_HpnicfDot11APIfMtu_Object=MibTableColumn
hpnicfDot11APIfMtu=_HpnicfDot11APIfMtu_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,6,1,4),_HpnicfDot11APIfMtu_Type())
hpnicfDot11APIfMtu.setMaxAccess(_Y)
if mibBuilder.loadTexts:hpnicfDot11APIfMtu.setStatus(_A)
_HpnicfDot11APIfPHYAddress_Type=OctetString
_HpnicfDot11APIfPHYAddress_Object=MibTableColumn
hpnicfDot11APIfPHYAddress=_HpnicfDot11APIfPHYAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,6,1,5),_HpnicfDot11APIfPHYAddress_Type())
hpnicfDot11APIfPHYAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfPHYAddress.setStatus(_A)
_HpnicfDot11APIfSpeed_Type=Integer32
_HpnicfDot11APIfSpeed_Object=MibTableColumn
hpnicfDot11APIfSpeed=_HpnicfDot11APIfSpeed_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,6,1,6),_HpnicfDot11APIfSpeed_Type())
hpnicfDot11APIfSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfSpeed.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APIfSpeed.setUnits('Mbps')
_HpnicfDot11APIfInDataRate_Type=Integer32
_HpnicfDot11APIfInDataRate_Object=MibTableColumn
hpnicfDot11APIfInDataRate=_HpnicfDot11APIfInDataRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,6,1,7),_HpnicfDot11APIfInDataRate_Type())
hpnicfDot11APIfInDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInDataRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APIfInDataRate.setUnits('Kbps')
_HpnicfDot11APIfOutDataRate_Type=Integer32
_HpnicfDot11APIfOutDataRate_Object=MibTableColumn
hpnicfDot11APIfOutDataRate=_HpnicfDot11APIfOutDataRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,6,1,8),_HpnicfDot11APIfOutDataRate_Type())
hpnicfDot11APIfOutDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutDataRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APIfOutDataRate.setUnits('Kbps')
_HpnicfDot11APIfSpeedKbps_Type=Gauge32
_HpnicfDot11APIfSpeedKbps_Object=MibTableColumn
hpnicfDot11APIfSpeedKbps=_HpnicfDot11APIfSpeedKbps_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,6,1,9),_HpnicfDot11APIfSpeedKbps_Type())
hpnicfDot11APIfSpeedKbps.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfSpeedKbps.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APIfSpeedKbps.setUnits('kbps')
_HpnicfDot11APIfTypeCM_Type=Integer32
_HpnicfDot11APIfTypeCM_Object=MibTableColumn
hpnicfDot11APIfTypeCM=_HpnicfDot11APIfTypeCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,6,1,10),_HpnicfDot11APIfTypeCM_Type())
hpnicfDot11APIfTypeCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfTypeCM.setStatus(_A)
_HpnicfDot11APSSIDObjectTable_Object=MibTable
hpnicfDot11APSSIDObjectTable=_HpnicfDot11APSSIDObjectTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,7))
if mibBuilder.loadTexts:hpnicfDot11APSSIDObjectTable.setStatus(_A)
_HpnicfDot11APSSIDObjectEntry_Object=MibTableRow
hpnicfDot11APSSIDObjectEntry=_HpnicfDot11APSSIDObjectEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,7,1))
hpnicfDot11APSSIDObjectEntry.setIndexNames((0,_C,_A0))
if mibBuilder.loadTexts:hpnicfDot11APSSIDObjectEntry.setStatus(_A)
_HpnicfDot11APConfigSPID_Type=HpnicfDot11ServicePolicyIDType
_HpnicfDot11APConfigSPID_Object=MibTableColumn
hpnicfDot11APConfigSPID=_HpnicfDot11APConfigSPID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,7,1,1),_HpnicfDot11APConfigSPID_Type())
hpnicfDot11APConfigSPID.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APConfigSPID.setStatus(_A)
_HpnicfDot11APConfigSSIDName_Type=HpnicfDot11SSIDStringType
_HpnicfDot11APConfigSSIDName_Object=MibTableColumn
hpnicfDot11APConfigSSIDName=_HpnicfDot11APConfigSSIDName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,7,1,2),_HpnicfDot11APConfigSSIDName_Type())
hpnicfDot11APConfigSSIDName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APConfigSSIDName.setStatus(_A)
_HpnicfDot11APConfigBSSIDNum_Type=Integer32
_HpnicfDot11APConfigBSSIDNum_Object=MibTableColumn
hpnicfDot11APConfigBSSIDNum=_HpnicfDot11APConfigBSSIDNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,7,1,3),_HpnicfDot11APConfigBSSIDNum_Type())
hpnicfDot11APConfigBSSIDNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APConfigBSSIDNum.setStatus(_A)
_HpnicfDot11APConfigPortalStaNum_Type=Integer32
_HpnicfDot11APConfigPortalStaNum_Object=MibTableColumn
hpnicfDot11APConfigPortalStaNum=_HpnicfDot11APConfigPortalStaNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,7,1,4),_HpnicfDot11APConfigPortalStaNum_Type())
hpnicfDot11APConfigPortalStaNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APConfigPortalStaNum.setStatus(_A)
_HpnicfDot11APSysInfoTable_Object=MibTable
hpnicfDot11APSysInfoTable=_HpnicfDot11APSysInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,8))
if mibBuilder.loadTexts:hpnicfDot11APSysInfoTable.setStatus(_A)
_HpnicfDot11APSysInfoEntry_Object=MibTableRow
hpnicfDot11APSysInfoEntry=_HpnicfDot11APSysInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,8,1))
hpnicfDot11APSysInfoEntry.setIndexNames((0,_g,_h))
if mibBuilder.loadTexts:hpnicfDot11APSysInfoEntry.setStatus(_A)
_HpnicfDot11APSysUpTime_Type=TimeTicks
_HpnicfDot11APSysUpTime_Object=MibTableColumn
hpnicfDot11APSysUpTime=_HpnicfDot11APSysUpTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,8,1,1),_HpnicfDot11APSysUpTime_Type())
hpnicfDot11APSysUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APSysUpTime.setStatus(_A)
class _HpnicfDot11APCPURTUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11APCPURTUsage_Type.__name__=_D
_HpnicfDot11APCPURTUsage_Object=MibTableColumn
hpnicfDot11APCPURTUsage=_HpnicfDot11APCPURTUsage_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,8,1,2),_HpnicfDot11APCPURTUsage_Type())
hpnicfDot11APCPURTUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APCPURTUsage.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APCPURTUsage.setUnits(_M)
class _HpnicfDot11APCPUAvgUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11APCPUAvgUsage_Type.__name__=_D
_HpnicfDot11APCPUAvgUsage_Object=MibTableColumn
hpnicfDot11APCPUAvgUsage=_HpnicfDot11APCPUAvgUsage_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,8,1,3),_HpnicfDot11APCPUAvgUsage_Type())
hpnicfDot11APCPUAvgUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APCPUAvgUsage.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APCPUAvgUsage.setUnits(_M)
class _HpnicfDot11APMemRTUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11APMemRTUsage_Type.__name__=_D
_HpnicfDot11APMemRTUsage_Object=MibTableColumn
hpnicfDot11APMemRTUsage=_HpnicfDot11APMemRTUsage_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,8,1,4),_HpnicfDot11APMemRTUsage_Type())
hpnicfDot11APMemRTUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APMemRTUsage.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APMemRTUsage.setUnits(_M)
class _HpnicfDot11APMemAvgUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11APMemAvgUsage_Type.__name__=_D
_HpnicfDot11APMemAvgUsage_Object=MibTableColumn
hpnicfDot11APMemAvgUsage=_HpnicfDot11APMemAvgUsage_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,8,1,5),_HpnicfDot11APMemAvgUsage_Type())
hpnicfDot11APMemAvgUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APMemAvgUsage.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APMemAvgUsage.setUnits(_M)
_HpnicfDot11APIPAddressGateway_Type=IpAddress
_HpnicfDot11APIPAddressGateway_Object=MibTableColumn
hpnicfDot11APIPAddressGateway=_HpnicfDot11APIPAddressGateway_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,8,1,6),_HpnicfDot11APIPAddressGateway_Type())
hpnicfDot11APIPAddressGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIPAddressGateway.setStatus(_A)
class _HpnicfDot11APACAssociateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_k,1),(_l,2),(_A1,3)))
_HpnicfDot11APACAssociateStatus_Type.__name__=_D
_HpnicfDot11APACAssociateStatus_Object=MibTableColumn
hpnicfDot11APACAssociateStatus=_HpnicfDot11APACAssociateStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,8,1,7),_HpnicfDot11APACAssociateStatus_Type())
hpnicfDot11APACAssociateStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APACAssociateStatus.setStatus(_A)
class _HpnicfDot11APManuBuildInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDot11APManuBuildInfo_Type.__name__=_S
_HpnicfDot11APManuBuildInfo_Object=MibTableColumn
hpnicfDot11APManuBuildInfo=_HpnicfDot11APManuBuildInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,8,1,8),_HpnicfDot11APManuBuildInfo_Type())
hpnicfDot11APManuBuildInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APManuBuildInfo.setStatus(_A)
_HpnicfDot11APFlashFreeSize_Type=Unsigned32
_HpnicfDot11APFlashFreeSize_Object=MibTableColumn
hpnicfDot11APFlashFreeSize=_HpnicfDot11APFlashFreeSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,8,1,9),_HpnicfDot11APFlashFreeSize_Type())
hpnicfDot11APFlashFreeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APFlashFreeSize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APFlashFreeSize.setUnits(_T)
_HpnicfDot11APTemperature_Type=Integer32
_HpnicfDot11APTemperature_Object=MibTableColumn
hpnicfDot11APTemperature=_HpnicfDot11APTemperature_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,8,1,10),_HpnicfDot11APTemperature_Type())
hpnicfDot11APTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APTemperature.setStatus(_A)
_HpnicfDot11APIdleListTable_Object=MibTable
hpnicfDot11APIdleListTable=_HpnicfDot11APIdleListTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,9))
if mibBuilder.loadTexts:hpnicfDot11APIdleListTable.setStatus(_A)
_HpnicfDot11APIdleListEntry_Object=MibTableRow
hpnicfDot11APIdleListEntry=_HpnicfDot11APIdleListEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,9,1))
hpnicfDot11APIdleListEntry.setIndexNames((0,_C,_A2))
if mibBuilder.loadTexts:hpnicfDot11APIdleListEntry.setStatus(_A)
class _HpnicfDot11APIdleTemplateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDot11APIdleTemplateName_Type.__name__=_S
_HpnicfDot11APIdleTemplateName_Object=MibTableColumn
hpnicfDot11APIdleTemplateName=_HpnicfDot11APIdleTemplateName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,9,1,1),_HpnicfDot11APIdleTemplateName_Type())
hpnicfDot11APIdleTemplateName.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APIdleTemplateName.setStatus(_A)
_HpnicfDot11APIdleSerialID_Type=OctetString
_HpnicfDot11APIdleSerialID_Object=MibTableColumn
hpnicfDot11APIdleSerialID=_HpnicfDot11APIdleSerialID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,9,1,2),_HpnicfDot11APIdleSerialID_Type())
hpnicfDot11APIdleSerialID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIdleSerialID.setStatus(_A)
_HpnicfDot11APSysInfoByAPIDTable_Object=MibTable
hpnicfDot11APSysInfoByAPIDTable=_HpnicfDot11APSysInfoByAPIDTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,10))
if mibBuilder.loadTexts:hpnicfDot11APSysInfoByAPIDTable.setStatus(_A)
_HpnicfDot11APSysInfoByAPIDEntry_Object=MibTableRow
hpnicfDot11APSysInfoByAPIDEntry=_HpnicfDot11APSysInfoByAPIDEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,10,1))
hpnicfDot11APSysInfoByAPIDEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:hpnicfDot11APSysInfoByAPIDEntry.setStatus(_A)
_HpnicfDot11APSysUpTime2_Type=TimeTicks
_HpnicfDot11APSysUpTime2_Object=MibTableColumn
hpnicfDot11APSysUpTime2=_HpnicfDot11APSysUpTime2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,10,1,1),_HpnicfDot11APSysUpTime2_Type())
hpnicfDot11APSysUpTime2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APSysUpTime2.setStatus(_A)
class _HpnicfDot11APCPURTUsage2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11APCPURTUsage2_Type.__name__=_D
_HpnicfDot11APCPURTUsage2_Object=MibTableColumn
hpnicfDot11APCPURTUsage2=_HpnicfDot11APCPURTUsage2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,10,1,2),_HpnicfDot11APCPURTUsage2_Type())
hpnicfDot11APCPURTUsage2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APCPURTUsage2.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APCPURTUsage2.setUnits(_M)
class _HpnicfDot11APCPUAvgUsage2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11APCPUAvgUsage2_Type.__name__=_D
_HpnicfDot11APCPUAvgUsage2_Object=MibTableColumn
hpnicfDot11APCPUAvgUsage2=_HpnicfDot11APCPUAvgUsage2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,10,1,3),_HpnicfDot11APCPUAvgUsage2_Type())
hpnicfDot11APCPUAvgUsage2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APCPUAvgUsage2.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APCPUAvgUsage2.setUnits(_M)
class _HpnicfDot11APMemRTUsage2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11APMemRTUsage2_Type.__name__=_D
_HpnicfDot11APMemRTUsage2_Object=MibTableColumn
hpnicfDot11APMemRTUsage2=_HpnicfDot11APMemRTUsage2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,10,1,4),_HpnicfDot11APMemRTUsage2_Type())
hpnicfDot11APMemRTUsage2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APMemRTUsage2.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APMemRTUsage2.setUnits(_M)
class _HpnicfDot11APMemAvgUsage2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11APMemAvgUsage2_Type.__name__=_D
_HpnicfDot11APMemAvgUsage2_Object=MibTableColumn
hpnicfDot11APMemAvgUsage2=_HpnicfDot11APMemAvgUsage2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,10,1,5),_HpnicfDot11APMemAvgUsage2_Type())
hpnicfDot11APMemAvgUsage2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APMemAvgUsage2.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APMemAvgUsage2.setUnits(_M)
_HpnicfDot11APIPAddressGateway2_Type=IpAddress
_HpnicfDot11APIPAddressGateway2_Object=MibTableColumn
hpnicfDot11APIPAddressGateway2=_HpnicfDot11APIPAddressGateway2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,10,1,6),_HpnicfDot11APIPAddressGateway2_Type())
hpnicfDot11APIPAddressGateway2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIPAddressGateway2.setStatus(_A)
class _HpnicfDot11APACAssociateStatus2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_k,1),(_l,2),(_A1,3)))
_HpnicfDot11APACAssociateStatus2_Type.__name__=_D
_HpnicfDot11APACAssociateStatus2_Object=MibTableColumn
hpnicfDot11APACAssociateStatus2=_HpnicfDot11APACAssociateStatus2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,10,1,7),_HpnicfDot11APACAssociateStatus2_Type())
hpnicfDot11APACAssociateStatus2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APACAssociateStatus2.setStatus(_A)
class _HpnicfDot11APManuBuildInfo2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDot11APManuBuildInfo2_Type.__name__=_S
_HpnicfDot11APManuBuildInfo2_Object=MibTableColumn
hpnicfDot11APManuBuildInfo2=_HpnicfDot11APManuBuildInfo2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,10,1,8),_HpnicfDot11APManuBuildInfo2_Type())
hpnicfDot11APManuBuildInfo2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APManuBuildInfo2.setStatus(_A)
_HpnicfDot11APFlashFreeSize2_Type=Unsigned32
_HpnicfDot11APFlashFreeSize2_Object=MibTableColumn
hpnicfDot11APFlashFreeSize2=_HpnicfDot11APFlashFreeSize2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,10,1,9),_HpnicfDot11APFlashFreeSize2_Type())
hpnicfDot11APFlashFreeSize2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APFlashFreeSize2.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APFlashFreeSize2.setUnits(_T)
_HpnicfDot11APTemperature2_Type=Integer32
_HpnicfDot11APTemperature2_Object=MibTableColumn
hpnicfDot11APTemperature2=_HpnicfDot11APTemperature2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,10,1,10),_HpnicfDot11APTemperature2_Type())
hpnicfDot11APTemperature2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APTemperature2.setStatus(_A)
_HpnicfDot11APMacAddress2_Type=MacAddress
_HpnicfDot11APMacAddress2_Object=MibTableColumn
hpnicfDot11APMacAddress2=_HpnicfDot11APMacAddress2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,10,1,11),_HpnicfDot11APMacAddress2_Type())
hpnicfDot11APMacAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APMacAddress2.setStatus(_A)
class _HpnicfDot11APACAssociateStatusCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_l,0),(_k,1)))
_HpnicfDot11APACAssociateStatusCM_Type.__name__=_D
_HpnicfDot11APACAssociateStatusCM_Object=MibTableColumn
hpnicfDot11APACAssociateStatusCM=_HpnicfDot11APACAssociateStatusCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,1,10,1,12),_HpnicfDot11APACAssociateStatusCM_Type())
hpnicfDot11APACAssociateStatusCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APACAssociateStatusCM.setStatus(_A)
_HpnicfDot11APStatisGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11APStatisGroup=_HpnicfDot11APStatisGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2))
_HpnicfDot11APRxStatisTable_Object=MibTable
hpnicfDot11APRxStatisTable=_HpnicfDot11APRxStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1))
if mibBuilder.loadTexts:hpnicfDot11APRxStatisTable.setStatus(_A)
_HpnicfDot11APRxStatisEntry_Object=MibTableRow
hpnicfDot11APRxStatisEntry=_HpnicfDot11APRxStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1))
hpnicfDot11APRxStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:hpnicfDot11APRxStatisEntry.setStatus(_A)
_HpnicfDot11RxFrameDupCnt_Type=Counter32
_HpnicfDot11RxFrameDupCnt_Object=MibTableColumn
hpnicfDot11RxFrameDupCnt=_HpnicfDot11RxFrameDupCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,1),_HpnicfDot11RxFrameDupCnt_Type())
hpnicfDot11RxFrameDupCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxFrameDupCnt.setStatus(_A)
_HpnicfDot11RxFrameCnt_Type=Counter32
_HpnicfDot11RxFrameCnt_Object=MibTableColumn
hpnicfDot11RxFrameCnt=_HpnicfDot11RxFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,2),_HpnicfDot11RxFrameCnt_Type())
hpnicfDot11RxFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxFrameCnt.setStatus(_A)
_HpnicfDot11RxUcastFrameCnt_Type=Counter32
_HpnicfDot11RxUcastFrameCnt_Object=MibTableColumn
hpnicfDot11RxUcastFrameCnt=_HpnicfDot11RxUcastFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,3),_HpnicfDot11RxUcastFrameCnt_Type())
hpnicfDot11RxUcastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxUcastFrameCnt.setStatus(_A)
_HpnicfDot11RxBcastFrameCnt_Type=Counter32
_HpnicfDot11RxBcastFrameCnt_Object=MibTableColumn
hpnicfDot11RxBcastFrameCnt=_HpnicfDot11RxBcastFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,4),_HpnicfDot11RxBcastFrameCnt_Type())
hpnicfDot11RxBcastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxBcastFrameCnt.setStatus(_A)
_HpnicfDot11RxMcastFrameCnt_Type=Counter32
_HpnicfDot11RxMcastFrameCnt_Object=MibTableColumn
hpnicfDot11RxMcastFrameCnt=_HpnicfDot11RxMcastFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,5),_HpnicfDot11RxMcastFrameCnt_Type())
hpnicfDot11RxMcastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxMcastFrameCnt.setStatus(_A)
_HpnicfDot11RxDiscardFrameCnt_Type=Counter32
_HpnicfDot11RxDiscardFrameCnt_Object=MibTableColumn
hpnicfDot11RxDiscardFrameCnt=_HpnicfDot11RxDiscardFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,6),_HpnicfDot11RxDiscardFrameCnt_Type())
hpnicfDot11RxDiscardFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxDiscardFrameCnt.setStatus(_A)
_HpnicfDot11RxFragCnt_Type=Counter32
_HpnicfDot11RxFragCnt_Object=MibTableColumn
hpnicfDot11RxFragCnt=_HpnicfDot11RxFragCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,7),_HpnicfDot11RxFragCnt_Type())
hpnicfDot11RxFragCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxFragCnt.setStatus(_A)
_HpnicfDot11RxFcsErrCnt_Type=Counter32
_HpnicfDot11RxFcsErrCnt_Object=MibTableColumn
hpnicfDot11RxFcsErrCnt=_HpnicfDot11RxFcsErrCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,8),_HpnicfDot11RxFcsErrCnt_Type())
hpnicfDot11RxFcsErrCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxFcsErrCnt.setStatus(_A)
_HpnicfDot11RxFrameBytes_Type=Counter32
_HpnicfDot11RxFrameBytes_Object=MibTableColumn
hpnicfDot11RxFrameBytes=_HpnicfDot11RxFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,9),_HpnicfDot11RxFrameBytes_Type())
hpnicfDot11RxFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxFrameBytes.setStatus(_A)
_HpnicfDot11RxUcastFrameBytes_Type=Counter32
_HpnicfDot11RxUcastFrameBytes_Object=MibTableColumn
hpnicfDot11RxUcastFrameBytes=_HpnicfDot11RxUcastFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,10),_HpnicfDot11RxUcastFrameBytes_Type())
hpnicfDot11RxUcastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxUcastFrameBytes.setStatus(_A)
_HpnicfDot11RxBcastFrameBytes_Type=Counter32
_HpnicfDot11RxBcastFrameBytes_Object=MibTableColumn
hpnicfDot11RxBcastFrameBytes=_HpnicfDot11RxBcastFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,11),_HpnicfDot11RxBcastFrameBytes_Type())
hpnicfDot11RxBcastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxBcastFrameBytes.setStatus(_A)
_HpnicfDot11RxMcastFrameBytes_Type=Counter32
_HpnicfDot11RxMcastFrameBytes_Object=MibTableColumn
hpnicfDot11RxMcastFrameBytes=_HpnicfDot11RxMcastFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,12),_HpnicfDot11RxMcastFrameBytes_Type())
hpnicfDot11RxMcastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxMcastFrameBytes.setStatus(_A)
_HpnicfDot11RxDiscardFrameBytes_Type=Counter32
_HpnicfDot11RxDiscardFrameBytes_Object=MibTableColumn
hpnicfDot11RxDiscardFrameBytes=_HpnicfDot11RxDiscardFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,13),_HpnicfDot11RxDiscardFrameBytes_Type())
hpnicfDot11RxDiscardFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxDiscardFrameBytes.setStatus(_A)
_HpnicfDot11RxMgmtFrameCnt_Type=Counter32
_HpnicfDot11RxMgmtFrameCnt_Object=MibTableColumn
hpnicfDot11RxMgmtFrameCnt=_HpnicfDot11RxMgmtFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,14),_HpnicfDot11RxMgmtFrameCnt_Type())
hpnicfDot11RxMgmtFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxMgmtFrameCnt.setStatus(_A)
_HpnicfDot11RxCtrlFrameCnt_Type=Counter32
_HpnicfDot11RxCtrlFrameCnt_Object=MibTableColumn
hpnicfDot11RxCtrlFrameCnt=_HpnicfDot11RxCtrlFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,15),_HpnicfDot11RxCtrlFrameCnt_Type())
hpnicfDot11RxCtrlFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxCtrlFrameCnt.setStatus(_A)
_HpnicfDot11RxDataFrameCnt_Type=Counter32
_HpnicfDot11RxDataFrameCnt_Object=MibTableColumn
hpnicfDot11RxDataFrameCnt=_HpnicfDot11RxDataFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,16),_HpnicfDot11RxDataFrameCnt_Type())
hpnicfDot11RxDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxDataFrameCnt.setStatus(_A)
_HpnicfDot11RxDecryptErrorCnt_Type=Counter32
_HpnicfDot11RxDecryptErrorCnt_Object=MibTableColumn
hpnicfDot11RxDecryptErrorCnt=_HpnicfDot11RxDecryptErrorCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,17),_HpnicfDot11RxDecryptErrorCnt_Type())
hpnicfDot11RxDecryptErrorCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxDecryptErrorCnt.setStatus(_A)
_HpnicfDot11RxAuthenFrameCnt_Type=Counter32
_HpnicfDot11RxAuthenFrameCnt_Object=MibTableColumn
hpnicfDot11RxAuthenFrameCnt=_HpnicfDot11RxAuthenFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,18),_HpnicfDot11RxAuthenFrameCnt_Type())
hpnicfDot11RxAuthenFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxAuthenFrameCnt.setStatus(_A)
_HpnicfDot11RxAssociateFrameCnt_Type=Counter32
_HpnicfDot11RxAssociateFrameCnt_Object=MibTableColumn
hpnicfDot11RxAssociateFrameCnt=_HpnicfDot11RxAssociateFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,19),_HpnicfDot11RxAssociateFrameCnt_Type())
hpnicfDot11RxAssociateFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxAssociateFrameCnt.setStatus(_A)
_HpnicfDot11RxFrameErrorRatio_Type=Integer32
_HpnicfDot11RxFrameErrorRatio_Object=MibTableColumn
hpnicfDot11RxFrameErrorRatio=_HpnicfDot11RxFrameErrorRatio_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,20),_HpnicfDot11RxFrameErrorRatio_Type())
hpnicfDot11RxFrameErrorRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxFrameErrorRatio.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RxFrameErrorRatio.setUnits(_M)
_HpnicfDot11RxPhyErrorCnt_Type=Counter32
_HpnicfDot11RxPhyErrorCnt_Object=MibTableColumn
hpnicfDot11RxPhyErrorCnt=_HpnicfDot11RxPhyErrorCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,21),_HpnicfDot11RxPhyErrorCnt_Type())
hpnicfDot11RxPhyErrorCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxPhyErrorCnt.setStatus(_A)
_HpnicfDot11RxMICErrorCnt_Type=Counter32
_HpnicfDot11RxMICErrorCnt_Object=MibTableColumn
hpnicfDot11RxMICErrorCnt=_HpnicfDot11RxMICErrorCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,22),_HpnicfDot11RxMICErrorCnt_Type())
hpnicfDot11RxMICErrorCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxMICErrorCnt.setStatus(_A)
_HpnicfDot11RxDataFrameBytes_Type=Counter32
_HpnicfDot11RxDataFrameBytes_Object=MibTableColumn
hpnicfDot11RxDataFrameBytes=_HpnicfDot11RxDataFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,23),_HpnicfDot11RxDataFrameBytes_Type())
hpnicfDot11RxDataFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxDataFrameBytes.setStatus(_A)
_HpnicfDot11RadioRxAverSnr_Type=Integer32
_HpnicfDot11RadioRxAverSnr_Object=MibTableColumn
hpnicfDot11RadioRxAverSnr=_HpnicfDot11RadioRxAverSnr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,24),_HpnicfDot11RadioRxAverSnr_Type())
hpnicfDot11RadioRxAverSnr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioRxAverSnr.setStatus(_A)
_HpnicfDot11RxPayloadBytes_Type=Counter32
_HpnicfDot11RxPayloadBytes_Object=MibTableColumn
hpnicfDot11RxPayloadBytes=_HpnicfDot11RxPayloadBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,25),_HpnicfDot11RxPayloadBytes_Type())
hpnicfDot11RxPayloadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxPayloadBytes.setStatus(_A)
_HpnicfDot11RxTrafficSpeed_Type=Integer32
_HpnicfDot11RxTrafficSpeed_Object=MibTableColumn
hpnicfDot11RxTrafficSpeed=_HpnicfDot11RxTrafficSpeed_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,26),_HpnicfDot11RxTrafficSpeed_Type())
hpnicfDot11RxTrafficSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxTrafficSpeed.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RxTrafficSpeed.setUnits('byte/s')
_HpnicfDot11RxUcastDataFrameCnt_Type=Counter64
_HpnicfDot11RxUcastDataFrameCnt_Object=MibTableColumn
hpnicfDot11RxUcastDataFrameCnt=_HpnicfDot11RxUcastDataFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,27),_HpnicfDot11RxUcastDataFrameCnt_Type())
hpnicfDot11RxUcastDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxUcastDataFrameCnt.setStatus(_A)
_HpnicfDot11RxNUcastDataFrameCnt_Type=Counter64
_HpnicfDot11RxNUcastDataFrameCnt_Object=MibTableColumn
hpnicfDot11RxNUcastDataFrameCnt=_HpnicfDot11RxNUcastDataFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,28),_HpnicfDot11RxNUcastDataFrameCnt_Type())
hpnicfDot11RxNUcastDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxNUcastDataFrameCnt.setStatus(_A)
_HpnicfDot11RxTotalDiscardFrameCnt_Type=Counter64
_HpnicfDot11RxTotalDiscardFrameCnt_Object=MibTableColumn
hpnicfDot11RxTotalDiscardFrameCnt=_HpnicfDot11RxTotalDiscardFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,29),_HpnicfDot11RxTotalDiscardFrameCnt_Type())
hpnicfDot11RxTotalDiscardFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxTotalDiscardFrameCnt.setStatus(_A)
_HpnicfDot11RxTotalIPCheckErrPacketCnt_Type=Counter64
_HpnicfDot11RxTotalIPCheckErrPacketCnt_Object=MibTableColumn
hpnicfDot11RxTotalIPCheckErrPacketCnt=_HpnicfDot11RxTotalIPCheckErrPacketCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,30),_HpnicfDot11RxTotalIPCheckErrPacketCnt_Type())
hpnicfDot11RxTotalIPCheckErrPacketCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxTotalIPCheckErrPacketCnt.setStatus(_A)
_HpnicfDot11RxSignalStrengthPacketCntCM_Type=OctetString
_HpnicfDot11RxSignalStrengthPacketCntCM_Object=MibTableColumn
hpnicfDot11RxSignalStrengthPacketCntCM=_HpnicfDot11RxSignalStrengthPacketCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,31),_HpnicfDot11RxSignalStrengthPacketCntCM_Type())
hpnicfDot11RxSignalStrengthPacketCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxSignalStrengthPacketCntCM.setStatus(_A)
_HpnicfDot11RxDataFrameCntCM_Type=Counter32
_HpnicfDot11RxDataFrameCntCM_Object=MibTableColumn
hpnicfDot11RxDataFrameCntCM=_HpnicfDot11RxDataFrameCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,32),_HpnicfDot11RxDataFrameCntCM_Type())
hpnicfDot11RxDataFrameCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxDataFrameCntCM.setStatus(_A)
_HpnicfDot11RxTotalFrameCnt_Type=Counter64
_HpnicfDot11RxTotalFrameCnt_Object=MibTableColumn
hpnicfDot11RxTotalFrameCnt=_HpnicfDot11RxTotalFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,1,1,33),_HpnicfDot11RxTotalFrameCnt_Type())
hpnicfDot11RxTotalFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RxTotalFrameCnt.setStatus(_A)
_HpnicfDot11APTxStatisTable_Object=MibTable
hpnicfDot11APTxStatisTable=_HpnicfDot11APTxStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2))
if mibBuilder.loadTexts:hpnicfDot11APTxStatisTable.setStatus(_A)
_HpnicfDot11APTxStatisEntry_Object=MibTableRow
hpnicfDot11APTxStatisEntry=_HpnicfDot11APTxStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1))
hpnicfDot11APTxStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:hpnicfDot11APTxStatisEntry.setStatus(_A)
_HpnicfDot11TxFragCnt_Type=Counter32
_HpnicfDot11TxFragCnt_Object=MibTableColumn
hpnicfDot11TxFragCnt=_HpnicfDot11TxFragCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,1),_HpnicfDot11TxFragCnt_Type())
hpnicfDot11TxFragCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxFragCnt.setStatus(_A)
_HpnicfDot11FailedCnt_Type=Counter32
_HpnicfDot11FailedCnt_Object=MibTableColumn
hpnicfDot11FailedCnt=_HpnicfDot11FailedCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,2),_HpnicfDot11FailedCnt_Type())
hpnicfDot11FailedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11FailedCnt.setStatus(_A)
_HpnicfDot11RetryCnt_Type=Counter32
_HpnicfDot11RetryCnt_Object=MibTableColumn
hpnicfDot11RetryCnt=_HpnicfDot11RetryCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,3),_HpnicfDot11RetryCnt_Type())
hpnicfDot11RetryCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RetryCnt.setStatus(_A)
_HpnicfDot11MultiRetryCnt_Type=Counter32
_HpnicfDot11MultiRetryCnt_Object=MibTableColumn
hpnicfDot11MultiRetryCnt=_HpnicfDot11MultiRetryCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,4),_HpnicfDot11MultiRetryCnt_Type())
hpnicfDot11MultiRetryCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11MultiRetryCnt.setStatus(_A)
_HpnicfDot11RtsSuccessCnt_Type=Counter32
_HpnicfDot11RtsSuccessCnt_Object=MibTableColumn
hpnicfDot11RtsSuccessCnt=_HpnicfDot11RtsSuccessCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,5),_HpnicfDot11RtsSuccessCnt_Type())
hpnicfDot11RtsSuccessCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RtsSuccessCnt.setStatus(_A)
_HpnicfDot11RtsFailCnt_Type=Counter32
_HpnicfDot11RtsFailCnt_Object=MibTableColumn
hpnicfDot11RtsFailCnt=_HpnicfDot11RtsFailCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,6),_HpnicfDot11RtsFailCnt_Type())
hpnicfDot11RtsFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RtsFailCnt.setStatus(_A)
_HpnicfDot11AckFailCnt_Type=Counter32
_HpnicfDot11AckFailCnt_Object=MibTableColumn
hpnicfDot11AckFailCnt=_HpnicfDot11AckFailCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,7),_HpnicfDot11AckFailCnt_Type())
hpnicfDot11AckFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AckFailCnt.setStatus(_A)
_HpnicfDot11TxFrameCnt_Type=Counter32
_HpnicfDot11TxFrameCnt_Object=MibTableColumn
hpnicfDot11TxFrameCnt=_HpnicfDot11TxFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,8),_HpnicfDot11TxFrameCnt_Type())
hpnicfDot11TxFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxFrameCnt.setStatus(_A)
_HpnicfDot11TxUcastFrameCnt_Type=Counter32
_HpnicfDot11TxUcastFrameCnt_Object=MibTableColumn
hpnicfDot11TxUcastFrameCnt=_HpnicfDot11TxUcastFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,9),_HpnicfDot11TxUcastFrameCnt_Type())
hpnicfDot11TxUcastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxUcastFrameCnt.setStatus(_A)
_HpnicfDot11TxBcastFrameCnt_Type=Counter32
_HpnicfDot11TxBcastFrameCnt_Object=MibTableColumn
hpnicfDot11TxBcastFrameCnt=_HpnicfDot11TxBcastFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,10),_HpnicfDot11TxBcastFrameCnt_Type())
hpnicfDot11TxBcastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxBcastFrameCnt.setStatus(_A)
_HpnicfDot11TxMcastFrameCnt_Type=Counter32
_HpnicfDot11TxMcastFrameCnt_Object=MibTableColumn
hpnicfDot11TxMcastFrameCnt=_HpnicfDot11TxMcastFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,11),_HpnicfDot11TxMcastFrameCnt_Type())
hpnicfDot11TxMcastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxMcastFrameCnt.setStatus(_A)
_HpnicfDot11TxDiscardFrameCnt_Type=Counter32
_HpnicfDot11TxDiscardFrameCnt_Object=MibTableColumn
hpnicfDot11TxDiscardFrameCnt=_HpnicfDot11TxDiscardFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,12),_HpnicfDot11TxDiscardFrameCnt_Type())
hpnicfDot11TxDiscardFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxDiscardFrameCnt.setStatus(_A)
_HpnicfDot11TxFrameBytes_Type=Counter32
_HpnicfDot11TxFrameBytes_Object=MibTableColumn
hpnicfDot11TxFrameBytes=_HpnicfDot11TxFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,13),_HpnicfDot11TxFrameBytes_Type())
hpnicfDot11TxFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxFrameBytes.setStatus(_A)
_HpnicfDot11TxUcastFrameBytes_Type=Counter32
_HpnicfDot11TxUcastFrameBytes_Object=MibTableColumn
hpnicfDot11TxUcastFrameBytes=_HpnicfDot11TxUcastFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,14),_HpnicfDot11TxUcastFrameBytes_Type())
hpnicfDot11TxUcastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxUcastFrameBytes.setStatus(_A)
_HpnicfDot11TxBcastFrameBytes_Type=Counter32
_HpnicfDot11TxBcastFrameBytes_Object=MibTableColumn
hpnicfDot11TxBcastFrameBytes=_HpnicfDot11TxBcastFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,15),_HpnicfDot11TxBcastFrameBytes_Type())
hpnicfDot11TxBcastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxBcastFrameBytes.setStatus(_A)
_HpnicfDot11TxMcastFrameBytes_Type=Counter32
_HpnicfDot11TxMcastFrameBytes_Object=MibTableColumn
hpnicfDot11TxMcastFrameBytes=_HpnicfDot11TxMcastFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,16),_HpnicfDot11TxMcastFrameBytes_Type())
hpnicfDot11TxMcastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxMcastFrameBytes.setStatus(_A)
_HpnicfDot11TxDiscardFrameBytes_Type=Counter32
_HpnicfDot11TxDiscardFrameBytes_Object=MibTableColumn
hpnicfDot11TxDiscardFrameBytes=_HpnicfDot11TxDiscardFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,17),_HpnicfDot11TxDiscardFrameBytes_Type())
hpnicfDot11TxDiscardFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxDiscardFrameBytes.setStatus(_A)
_HpnicfDot11TxAuthenFrameCnt_Type=Counter32
_HpnicfDot11TxAuthenFrameCnt_Object=MibTableColumn
hpnicfDot11TxAuthenFrameCnt=_HpnicfDot11TxAuthenFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,18),_HpnicfDot11TxAuthenFrameCnt_Type())
hpnicfDot11TxAuthenFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxAuthenFrameCnt.setStatus(_A)
_HpnicfDot11TxAssociateFrameCnt_Type=Counter32
_HpnicfDot11TxAssociateFrameCnt_Object=MibTableColumn
hpnicfDot11TxAssociateFrameCnt=_HpnicfDot11TxAssociateFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,19),_HpnicfDot11TxAssociateFrameCnt_Type())
hpnicfDot11TxAssociateFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxAssociateFrameCnt.setStatus(_A)
_HpnicfDot11TxFrameRetryRatio_Type=Integer32
_HpnicfDot11TxFrameRetryRatio_Object=MibTableColumn
hpnicfDot11TxFrameRetryRatio=_HpnicfDot11TxFrameRetryRatio_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,20),_HpnicfDot11TxFrameRetryRatio_Type())
hpnicfDot11TxFrameRetryRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxFrameRetryRatio.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11TxFrameRetryRatio.setUnits(_M)
_HpnicfDot11TxDataFrameCnt_Type=Counter32
_HpnicfDot11TxDataFrameCnt_Object=MibTableColumn
hpnicfDot11TxDataFrameCnt=_HpnicfDot11TxDataFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,21),_HpnicfDot11TxDataFrameCnt_Type())
hpnicfDot11TxDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxDataFrameCnt.setStatus(_A)
_HpnicfDot11TxDataFrameBytes_Type=Counter32
_HpnicfDot11TxDataFrameBytes_Object=MibTableColumn
hpnicfDot11TxDataFrameBytes=_HpnicfDot11TxDataFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,22),_HpnicfDot11TxDataFrameBytes_Type())
hpnicfDot11TxDataFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxDataFrameBytes.setStatus(_A)
_HpnicfDot11TxMSDUCnt_Type=Counter32
_HpnicfDot11TxMSDUCnt_Object=MibTableColumn
hpnicfDot11TxMSDUCnt=_HpnicfDot11TxMSDUCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,23),_HpnicfDot11TxMSDUCnt_Type())
hpnicfDot11TxMSDUCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxMSDUCnt.setStatus(_A)
_HpnicfDot11TxDiscardMSDUCnt_Type=Counter32
_HpnicfDot11TxDiscardMSDUCnt_Object=MibTableColumn
hpnicfDot11TxDiscardMSDUCnt=_HpnicfDot11TxDiscardMSDUCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,24),_HpnicfDot11TxDiscardMSDUCnt_Type())
hpnicfDot11TxDiscardMSDUCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxDiscardMSDUCnt.setStatus(_A)
_HpnicfDot11RetryMSDUCnt_Type=Counter32
_HpnicfDot11RetryMSDUCnt_Object=MibTableColumn
hpnicfDot11RetryMSDUCnt=_HpnicfDot11RetryMSDUCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,25),_HpnicfDot11RetryMSDUCnt_Type())
hpnicfDot11RetryMSDUCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RetryMSDUCnt.setStatus(_A)
_HpnicfDot11TxPayloadBytes_Type=Counter32
_HpnicfDot11TxPayloadBytes_Object=MibTableColumn
hpnicfDot11TxPayloadBytes=_HpnicfDot11TxPayloadBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,26),_HpnicfDot11TxPayloadBytes_Type())
hpnicfDot11TxPayloadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxPayloadBytes.setStatus(_A)
_HpnicfDot11TxTrafficSpeed_Type=Integer32
_HpnicfDot11TxTrafficSpeed_Object=MibTableColumn
hpnicfDot11TxTrafficSpeed=_HpnicfDot11TxTrafficSpeed_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,27),_HpnicfDot11TxTrafficSpeed_Type())
hpnicfDot11TxTrafficSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxTrafficSpeed.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11TxTrafficSpeed.setUnits('byte/s')
_HpnicfDot11TxErrFrameRatio_Type=Integer32
_HpnicfDot11TxErrFrameRatio_Object=MibTableColumn
hpnicfDot11TxErrFrameRatio=_HpnicfDot11TxErrFrameRatio_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,28),_HpnicfDot11TxErrFrameRatio_Type())
hpnicfDot11TxErrFrameRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxErrFrameRatio.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11TxErrFrameRatio.setUnits(_M)
_HpnicfDot11TxFrameRate_Type=Integer32
_HpnicfDot11TxFrameRate_Object=MibTableColumn
hpnicfDot11TxFrameRate=_HpnicfDot11TxFrameRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,29),_HpnicfDot11TxFrameRate_Type())
hpnicfDot11TxFrameRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxFrameRate.setStatus(_A)
_HpnicfDot11TxMgtFrameCnt_Type=Counter32
_HpnicfDot11TxMgtFrameCnt_Object=MibTableColumn
hpnicfDot11TxMgtFrameCnt=_HpnicfDot11TxMgtFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,30),_HpnicfDot11TxMgtFrameCnt_Type())
hpnicfDot11TxMgtFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxMgtFrameCnt.setStatus(_A)
_HpnicfDot11TxCtrlFrameCnt_Type=Counter32
_HpnicfDot11TxCtrlFrameCnt_Object=MibTableColumn
hpnicfDot11TxCtrlFrameCnt=_HpnicfDot11TxCtrlFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,31),_HpnicfDot11TxCtrlFrameCnt_Type())
hpnicfDot11TxCtrlFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxCtrlFrameCnt.setStatus(_A)
_HpnicfDot11TxMACErrCnt_Type=Counter32
_HpnicfDot11TxMACErrCnt_Object=MibTableColumn
hpnicfDot11TxMACErrCnt=_HpnicfDot11TxMACErrCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,32),_HpnicfDot11TxMACErrCnt_Type())
hpnicfDot11TxMACErrCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxMACErrCnt.setStatus(_A)
_HpnicfDot11TxErrFrameCnt_Type=Counter32
_HpnicfDot11TxErrFrameCnt_Object=MibTableColumn
hpnicfDot11TxErrFrameCnt=_HpnicfDot11TxErrFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,33),_HpnicfDot11TxErrFrameCnt_Type())
hpnicfDot11TxErrFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxErrFrameCnt.setStatus(_A)
_HpnicfDot11TxUcastDataFrameCnt_Type=Counter64
_HpnicfDot11TxUcastDataFrameCnt_Object=MibTableColumn
hpnicfDot11TxUcastDataFrameCnt=_HpnicfDot11TxUcastDataFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,34),_HpnicfDot11TxUcastDataFrameCnt_Type())
hpnicfDot11TxUcastDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxUcastDataFrameCnt.setStatus(_A)
_HpnicfDot11TxNUcastDataFrameCnt_Type=Counter64
_HpnicfDot11TxNUcastDataFrameCnt_Object=MibTableColumn
hpnicfDot11TxNUcastDataFrameCnt=_HpnicfDot11TxNUcastDataFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,35),_HpnicfDot11TxNUcastDataFrameCnt_Type())
hpnicfDot11TxNUcastDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxNUcastDataFrameCnt.setStatus(_A)
_HpnicfDot11TxTotalFrameCnt_Type=Counter64
_HpnicfDot11TxTotalFrameCnt_Object=MibTableColumn
hpnicfDot11TxTotalFrameCnt=_HpnicfDot11TxTotalFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,2,1,36),_HpnicfDot11TxTotalFrameCnt_Type())
hpnicfDot11TxTotalFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11TxTotalFrameCnt.setStatus(_A)
_HpnicfDot11APAssocStatisTable_Object=MibTable
hpnicfDot11APAssocStatisTable=_HpnicfDot11APAssocStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,3))
if mibBuilder.loadTexts:hpnicfDot11APAssocStatisTable.setStatus(_A)
_HpnicfDot11APAssocStatisEntry_Object=MibTableRow
hpnicfDot11APAssocStatisEntry=_HpnicfDot11APAssocStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,3,1))
hpnicfDot11APAssocStatisEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:hpnicfDot11APAssocStatisEntry.setStatus(_A)
_HpnicfDot11ApStationAssocSum_Type=Counter32
_HpnicfDot11ApStationAssocSum_Object=MibTableColumn
hpnicfDot11ApStationAssocSum=_HpnicfDot11ApStationAssocSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,3,1,1),_HpnicfDot11ApStationAssocSum_Type())
hpnicfDot11ApStationAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ApStationAssocSum.setStatus(_A)
_HpnicfDot11ApStationAssocFailSum_Type=Counter32
_HpnicfDot11ApStationAssocFailSum_Object=MibTableColumn
hpnicfDot11ApStationAssocFailSum=_HpnicfDot11ApStationAssocFailSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,3,1,2),_HpnicfDot11ApStationAssocFailSum_Type())
hpnicfDot11ApStationAssocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ApStationAssocFailSum.setStatus(_A)
_HpnicfDot11ApStationReassocSum_Type=Counter32
_HpnicfDot11ApStationReassocSum_Object=MibTableColumn
hpnicfDot11ApStationReassocSum=_HpnicfDot11ApStationReassocSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,3,1,3),_HpnicfDot11ApStationReassocSum_Type())
hpnicfDot11ApStationReassocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ApStationReassocSum.setStatus(_A)
_HpnicfDot11ApStationAssocRejectSum_Type=Counter32
_HpnicfDot11ApStationAssocRejectSum_Object=MibTableColumn
hpnicfDot11ApStationAssocRejectSum=_HpnicfDot11ApStationAssocRejectSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,3,1,4),_HpnicfDot11ApStationAssocRejectSum_Type())
hpnicfDot11ApStationAssocRejectSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ApStationAssocRejectSum.setStatus(_A)
_HpnicfDot11ApStationExDeAuthenSum_Type=Counter32
_HpnicfDot11ApStationExDeAuthenSum_Object=MibTableColumn
hpnicfDot11ApStationExDeAuthenSum=_HpnicfDot11ApStationExDeAuthenSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,3,1,5),_HpnicfDot11ApStationExDeAuthenSum_Type())
hpnicfDot11ApStationExDeAuthenSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ApStationExDeAuthenSum.setStatus(_A)
_HpnicfDot11ApStationCurAssocSum_Type=Integer32
_HpnicfDot11ApStationCurAssocSum_Object=MibTableColumn
hpnicfDot11ApStationCurAssocSum=_HpnicfDot11ApStationCurAssocSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,3,1,6),_HpnicfDot11ApStationCurAssocSum_Type())
hpnicfDot11ApStationCurAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ApStationCurAssocSum.setStatus(_A)
_HpnicfDot11ApStaCurAuthSuccSum_Type=Integer32
_HpnicfDot11ApStaCurAuthSuccSum_Object=MibTableColumn
hpnicfDot11ApStaCurAuthSuccSum=_HpnicfDot11ApStaCurAuthSuccSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,3,1,7),_HpnicfDot11ApStaCurAuthSuccSum_Type())
hpnicfDot11ApStaCurAuthSuccSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ApStaCurAuthSuccSum.setStatus(_A)
_HpnicfDot11AllStationUpSumTime_Type=Counter32
_HpnicfDot11AllStationUpSumTime_Object=MibTableColumn
hpnicfDot11AllStationUpSumTime=_HpnicfDot11AllStationUpSumTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,3,1,8),_HpnicfDot11AllStationUpSumTime_Type())
hpnicfDot11AllStationUpSumTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AllStationUpSumTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11AllStationUpSumTime.setUnits('minute')
_HpnicfDot11ApStationAssocReqSum_Type=Counter32
_HpnicfDot11ApStationAssocReqSum_Object=MibTableColumn
hpnicfDot11ApStationAssocReqSum=_HpnicfDot11ApStationAssocReqSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,3,1,9),_HpnicfDot11ApStationAssocReqSum_Type())
hpnicfDot11ApStationAssocReqSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ApStationAssocReqSum.setStatus(_A)
_HpnicfDot11AllStationUpSumTimeTicks_Type=TimeTicks
_HpnicfDot11AllStationUpSumTimeTicks_Object=MibTableColumn
hpnicfDot11AllStationUpSumTimeTicks=_HpnicfDot11AllStationUpSumTimeTicks_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,3,1,10),_HpnicfDot11AllStationUpSumTimeTicks_Type())
hpnicfDot11AllStationUpSumTimeTicks.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AllStationUpSumTimeTicks.setStatus(_A)
_HpnicfDot11ApStationReassocReqSum_Type=Counter32
_HpnicfDot11ApStationReassocReqSum_Object=MibTableColumn
hpnicfDot11ApStationReassocReqSum=_HpnicfDot11ApStationReassocReqSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,3,1,11),_HpnicfDot11ApStationReassocReqSum_Type())
hpnicfDot11ApStationReassocReqSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ApStationReassocReqSum.setStatus(_A)
_HpnicfDot11ApStationReassocFailSum_Type=Counter32
_HpnicfDot11ApStationReassocFailSum_Object=MibTableColumn
hpnicfDot11ApStationReassocFailSum=_HpnicfDot11ApStationReassocFailSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,3,1,12),_HpnicfDot11ApStationReassocFailSum_Type())
hpnicfDot11ApStationReassocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ApStationReassocFailSum.setStatus(_A)
_HpnicfDot11BSSRxStatisTable_Object=MibTable
hpnicfDot11BSSRxStatisTable=_HpnicfDot11BSSRxStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,4))
if mibBuilder.loadTexts:hpnicfDot11BSSRxStatisTable.setStatus(_A)
_HpnicfDot11BSSRxStatisEntry_Object=MibTableRow
hpnicfDot11BSSRxStatisEntry=_HpnicfDot11BSSRxStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,4,1))
hpnicfDot11BSSRxStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_P))
if mibBuilder.loadTexts:hpnicfDot11BSSRxStatisEntry.setStatus(_A)
_HpnicfDot11BSSRxFrameCnt_Type=Counter32
_HpnicfDot11BSSRxFrameCnt_Object=MibTableColumn
hpnicfDot11BSSRxFrameCnt=_HpnicfDot11BSSRxFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,4,1,1),_HpnicfDot11BSSRxFrameCnt_Type())
hpnicfDot11BSSRxFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRxFrameCnt.setStatus(_A)
_HpnicfDot11BSSRxFrameBytes_Type=Counter32
_HpnicfDot11BSSRxFrameBytes_Object=MibTableColumn
hpnicfDot11BSSRxFrameBytes=_HpnicfDot11BSSRxFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,4,1,2),_HpnicfDot11BSSRxFrameBytes_Type())
hpnicfDot11BSSRxFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRxFrameBytes.setStatus(_A)
_HpnicfDot11BSSRxDataFrameCnt_Type=Counter32
_HpnicfDot11BSSRxDataFrameCnt_Object=MibTableColumn
hpnicfDot11BSSRxDataFrameCnt=_HpnicfDot11BSSRxDataFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,4,1,3),_HpnicfDot11BSSRxDataFrameCnt_Type())
hpnicfDot11BSSRxDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRxDataFrameCnt.setStatus(_A)
_HpnicfDot11BSSRxDataFrameBytes_Type=Counter32
_HpnicfDot11BSSRxDataFrameBytes_Object=MibTableColumn
hpnicfDot11BSSRxDataFrameBytes=_HpnicfDot11BSSRxDataFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,4,1,4),_HpnicfDot11BSSRxDataFrameBytes_Type())
hpnicfDot11BSSRxDataFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRxDataFrameBytes.setStatus(_A)
_HpnicfDot11BSSRxAssociateFrameCnt_Type=Counter32
_HpnicfDot11BSSRxAssociateFrameCnt_Object=MibTableColumn
hpnicfDot11BSSRxAssociateFrameCnt=_HpnicfDot11BSSRxAssociateFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,4,1,5),_HpnicfDot11BSSRxAssociateFrameCnt_Type())
hpnicfDot11BSSRxAssociateFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRxAssociateFrameCnt.setStatus(_A)
_HpnicfDot11BSSRxFrameErrorRatio_Type=Integer32
_HpnicfDot11BSSRxFrameErrorRatio_Object=MibTableColumn
hpnicfDot11BSSRxFrameErrorRatio=_HpnicfDot11BSSRxFrameErrorRatio_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,4,1,6),_HpnicfDot11BSSRxFrameErrorRatio_Type())
hpnicfDot11BSSRxFrameErrorRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRxFrameErrorRatio.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11BSSRxFrameErrorRatio.setUnits('percent')
_HpnicfDot11BSSRxPayloadBytes_Type=Counter32
_HpnicfDot11BSSRxPayloadBytes_Object=MibTableColumn
hpnicfDot11BSSRxPayloadBytes=_HpnicfDot11BSSRxPayloadBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,4,1,7),_HpnicfDot11BSSRxPayloadBytes_Type())
hpnicfDot11BSSRxPayloadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRxPayloadBytes.setStatus(_A)
_HpnicfDot11BSSRxUniFrameCnt_Type=Counter32
_HpnicfDot11BSSRxUniFrameCnt_Object=MibTableColumn
hpnicfDot11BSSRxUniFrameCnt=_HpnicfDot11BSSRxUniFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,4,1,8),_HpnicfDot11BSSRxUniFrameCnt_Type())
hpnicfDot11BSSRxUniFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRxUniFrameCnt.setStatus(_A)
_HpnicfDot11BSSRxNonUniFrameCnt_Type=Integer32
_HpnicfDot11BSSRxNonUniFrameCnt_Object=MibTableColumn
hpnicfDot11BSSRxNonUniFrameCnt=_HpnicfDot11BSSRxNonUniFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,4,1,9),_HpnicfDot11BSSRxNonUniFrameCnt_Type())
hpnicfDot11BSSRxNonUniFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRxNonUniFrameCnt.setStatus(_A)
_HpnicfDot11BSSRxAuthenFrameCnt_Type=Counter32
_HpnicfDot11BSSRxAuthenFrameCnt_Object=MibTableColumn
hpnicfDot11BSSRxAuthenFrameCnt=_HpnicfDot11BSSRxAuthenFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,4,1,10),_HpnicfDot11BSSRxAuthenFrameCnt_Type())
hpnicfDot11BSSRxAuthenFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRxAuthenFrameCnt.setStatus(_A)
_HpnicfDot11BSSTxStatisTable_Object=MibTable
hpnicfDot11BSSTxStatisTable=_HpnicfDot11BSSTxStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,5))
if mibBuilder.loadTexts:hpnicfDot11BSSTxStatisTable.setStatus(_A)
_HpnicfDot11BSSTxStatisEntry_Object=MibTableRow
hpnicfDot11BSSTxStatisEntry=_HpnicfDot11BSSTxStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,5,1))
hpnicfDot11BSSTxStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_P))
if mibBuilder.loadTexts:hpnicfDot11BSSTxStatisEntry.setStatus(_A)
_HpnicfDot11BSSTxFrameCnt_Type=Counter32
_HpnicfDot11BSSTxFrameCnt_Object=MibTableColumn
hpnicfDot11BSSTxFrameCnt=_HpnicfDot11BSSTxFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,5,1,1),_HpnicfDot11BSSTxFrameCnt_Type())
hpnicfDot11BSSTxFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTxFrameCnt.setStatus(_A)
_HpnicfDot11BSSTxFrameBytes_Type=Counter32
_HpnicfDot11BSSTxFrameBytes_Object=MibTableColumn
hpnicfDot11BSSTxFrameBytes=_HpnicfDot11BSSTxFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,5,1,2),_HpnicfDot11BSSTxFrameBytes_Type())
hpnicfDot11BSSTxFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTxFrameBytes.setStatus(_A)
_HpnicfDot11BSSTxDataFrameCnt_Type=Counter32
_HpnicfDot11BSSTxDataFrameCnt_Object=MibTableColumn
hpnicfDot11BSSTxDataFrameCnt=_HpnicfDot11BSSTxDataFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,5,1,3),_HpnicfDot11BSSTxDataFrameCnt_Type())
hpnicfDot11BSSTxDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTxDataFrameCnt.setStatus(_A)
_HpnicfDot11BSSTxDataFrameBytes_Type=Counter32
_HpnicfDot11BSSTxDataFrameBytes_Object=MibTableColumn
hpnicfDot11BSSTxDataFrameBytes=_HpnicfDot11BSSTxDataFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,5,1,4),_HpnicfDot11BSSTxDataFrameBytes_Type())
hpnicfDot11BSSTxDataFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTxDataFrameBytes.setStatus(_A)
_HpnicfDot11BSSTxAssociateFrameCnt_Type=Counter32
_HpnicfDot11BSSTxAssociateFrameCnt_Object=MibTableColumn
hpnicfDot11BSSTxAssociateFrameCnt=_HpnicfDot11BSSTxAssociateFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,5,1,5),_HpnicfDot11BSSTxAssociateFrameCnt_Type())
hpnicfDot11BSSTxAssociateFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTxAssociateFrameCnt.setStatus(_A)
_HpnicfDot11BSSTxPayloadBytes_Type=Counter32
_HpnicfDot11BSSTxPayloadBytes_Object=MibTableColumn
hpnicfDot11BSSTxPayloadBytes=_HpnicfDot11BSSTxPayloadBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,5,1,6),_HpnicfDot11BSSTxPayloadBytes_Type())
hpnicfDot11BSSTxPayloadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTxPayloadBytes.setStatus(_A)
_HpnicfDot11BSSTxRetryCnt_Type=Counter32
_HpnicfDot11BSSTxRetryCnt_Object=MibTableColumn
hpnicfDot11BSSTxRetryCnt=_HpnicfDot11BSSTxRetryCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,5,1,7),_HpnicfDot11BSSTxRetryCnt_Type())
hpnicfDot11BSSTxRetryCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTxRetryCnt.setStatus(_A)
_HpnicfDot11BSSTxUniFrameCnt_Type=Counter32
_HpnicfDot11BSSTxUniFrameCnt_Object=MibTableColumn
hpnicfDot11BSSTxUniFrameCnt=_HpnicfDot11BSSTxUniFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,5,1,8),_HpnicfDot11BSSTxUniFrameCnt_Type())
hpnicfDot11BSSTxUniFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTxUniFrameCnt.setStatus(_A)
_HpnicfDot11BSSTxNonUniFrameCnt_Type=Integer32
_HpnicfDot11BSSTxNonUniFrameCnt_Object=MibTableColumn
hpnicfDot11BSSTxNonUniFrameCnt=_HpnicfDot11BSSTxNonUniFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,5,1,9),_HpnicfDot11BSSTxNonUniFrameCnt_Type())
hpnicfDot11BSSTxNonUniFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTxNonUniFrameCnt.setStatus(_A)
_HpnicfDot11BSSTxAuthenFrameCnt_Type=Counter32
_HpnicfDot11BSSTxAuthenFrameCnt_Object=MibTableColumn
hpnicfDot11BSSTxAuthenFrameCnt=_HpnicfDot11BSSTxAuthenFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,5,1,10),_HpnicfDot11BSSTxAuthenFrameCnt_Type())
hpnicfDot11BSSTxAuthenFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTxAuthenFrameCnt.setStatus(_A)
_HpnicfDot11BSSAssocStatisTable_Object=MibTable
hpnicfDot11BSSAssocStatisTable=_HpnicfDot11BSSAssocStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,6))
if mibBuilder.loadTexts:hpnicfDot11BSSAssocStatisTable.setStatus(_A)
_HpnicfDot11BSSAssocStatisEntry_Object=MibTableRow
hpnicfDot11BSSAssocStatisEntry=_HpnicfDot11BSSAssocStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,6,1))
hpnicfDot11BSSAssocStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_P))
if mibBuilder.loadTexts:hpnicfDot11BSSAssocStatisEntry.setStatus(_A)
_HpnicfDot11BSSStationAssocSum_Type=Counter32
_HpnicfDot11BSSStationAssocSum_Object=MibTableColumn
hpnicfDot11BSSStationAssocSum=_HpnicfDot11BSSStationAssocSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,6,1,1),_HpnicfDot11BSSStationAssocSum_Type())
hpnicfDot11BSSStationAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSStationAssocSum.setStatus(_A)
_HpnicfDot11BSSStationAssocFailSum_Type=Counter32
_HpnicfDot11BSSStationAssocFailSum_Object=MibTableColumn
hpnicfDot11BSSStationAssocFailSum=_HpnicfDot11BSSStationAssocFailSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,6,1,2),_HpnicfDot11BSSStationAssocFailSum_Type())
hpnicfDot11BSSStationAssocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSStationAssocFailSum.setStatus(_A)
_HpnicfDot11BSSStationReassocSum_Type=Counter32
_HpnicfDot11BSSStationReassocSum_Object=MibTableColumn
hpnicfDot11BSSStationReassocSum=_HpnicfDot11BSSStationReassocSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,6,1,3),_HpnicfDot11BSSStationReassocSum_Type())
hpnicfDot11BSSStationReassocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSStationReassocSum.setStatus(_A)
_HpnicfDot11BSSStationAssocRejectSum_Type=Counter32
_HpnicfDot11BSSStationAssocRejectSum_Object=MibTableColumn
hpnicfDot11BSSStationAssocRejectSum=_HpnicfDot11BSSStationAssocRejectSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,6,1,4),_HpnicfDot11BSSStationAssocRejectSum_Type())
hpnicfDot11BSSStationAssocRejectSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSStationAssocRejectSum.setStatus(_A)
_HpnicfDot11BSSStationExDeAssocSum_Type=Counter32
_HpnicfDot11BSSStationExDeAssocSum_Object=MibTableColumn
hpnicfDot11BSSStationExDeAssocSum=_HpnicfDot11BSSStationExDeAssocSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,6,1,5),_HpnicfDot11BSSStationExDeAssocSum_Type())
hpnicfDot11BSSStationExDeAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSStationExDeAssocSum.setStatus(_A)
_HpnicfDot11BSSStationCurAssocSum_Type=Integer32
_HpnicfDot11BSSStationCurAssocSum_Object=MibTableColumn
hpnicfDot11BSSStationCurAssocSum=_HpnicfDot11BSSStationCurAssocSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,6,1,6),_HpnicfDot11BSSStationCurAssocSum_Type())
hpnicfDot11BSSStationCurAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSStationCurAssocSum.setStatus(_A)
_HpnicfDot11BSSStationAssocReqSum_Type=Counter32
_HpnicfDot11BSSStationAssocReqSum_Object=MibTableColumn
hpnicfDot11BSSStationAssocReqSum=_HpnicfDot11BSSStationAssocReqSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,6,1,7),_HpnicfDot11BSSStationAssocReqSum_Type())
hpnicfDot11BSSStationAssocReqSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSStationAssocReqSum.setStatus(_A)
_HpnicfDot11BSSStationCurAuthSum_Type=Integer32
_HpnicfDot11BSSStationCurAuthSum_Object=MibTableColumn
hpnicfDot11BSSStationCurAuthSum=_HpnicfDot11BSSStationCurAuthSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,6,1,8),_HpnicfDot11BSSStationCurAuthSum_Type())
hpnicfDot11BSSStationCurAuthSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSStationCurAuthSum.setStatus(_A)
_HpnicfDot11APLinkStatisTable_Object=MibTable
hpnicfDot11APLinkStatisTable=_HpnicfDot11APLinkStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,7))
if mibBuilder.loadTexts:hpnicfDot11APLinkStatisTable.setStatus(_A)
_HpnicfDot11APLinkStatisEntry_Object=MibTableRow
hpnicfDot11APLinkStatisEntry=_HpnicfDot11APLinkStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,7,1))
hpnicfDot11APLinkStatisEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:hpnicfDot11APLinkStatisEntry.setStatus(_A)
_HpnicfDot11UpLinkUpDownTimes_Type=Counter32
_HpnicfDot11UpLinkUpDownTimes_Object=MibTableColumn
hpnicfDot11UpLinkUpDownTimes=_HpnicfDot11UpLinkUpDownTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,7,1,1),_HpnicfDot11UpLinkUpDownTimes_Type())
hpnicfDot11UpLinkUpDownTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11UpLinkUpDownTimes.setStatus(_A)
_HpnicfDot11DownLinkUpDownTimes_Type=Counter32
_HpnicfDot11DownLinkUpDownTimes_Object=MibTableColumn
hpnicfDot11DownLinkUpDownTimes=_HpnicfDot11DownLinkUpDownTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,7,1,2),_HpnicfDot11DownLinkUpDownTimes_Type())
hpnicfDot11DownLinkUpDownTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11DownLinkUpDownTimes.setStatus(_A)
_HpnicfDot11PrivateSrvRxFrameBytes_Type=Counter64
_HpnicfDot11PrivateSrvRxFrameBytes_Object=MibTableColumn
hpnicfDot11PrivateSrvRxFrameBytes=_HpnicfDot11PrivateSrvRxFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,7,1,3),_HpnicfDot11PrivateSrvRxFrameBytes_Type())
hpnicfDot11PrivateSrvRxFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11PrivateSrvRxFrameBytes.setStatus(_A)
_HpnicfDot11PrivateSrvTxFrameBytes_Type=Counter64
_HpnicfDot11PrivateSrvTxFrameBytes_Object=MibTableColumn
hpnicfDot11PrivateSrvTxFrameBytes=_HpnicfDot11PrivateSrvTxFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,7,1,4),_HpnicfDot11PrivateSrvTxFrameBytes_Type())
hpnicfDot11PrivateSrvTxFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11PrivateSrvTxFrameBytes.setStatus(_A)
_HpnicfDot11APInternetAllRxBytes_Type=Counter64
_HpnicfDot11APInternetAllRxBytes_Object=MibTableColumn
hpnicfDot11APInternetAllRxBytes=_HpnicfDot11APInternetAllRxBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,7,1,5),_HpnicfDot11APInternetAllRxBytes_Type())
hpnicfDot11APInternetAllRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APInternetAllRxBytes.setStatus(_A)
_HpnicfDot11APInternetAllTxBytes_Type=Counter64
_HpnicfDot11APInternetAllTxBytes_Object=MibTableColumn
hpnicfDot11APInternetAllTxBytes=_HpnicfDot11APInternetAllTxBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,7,1,6),_HpnicfDot11APInternetAllTxBytes_Type())
hpnicfDot11APInternetAllTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APInternetAllTxBytes.setStatus(_A)
_HpnicfDot11APLocalAllRxBytes_Type=Counter64
_HpnicfDot11APLocalAllRxBytes_Object=MibTableColumn
hpnicfDot11APLocalAllRxBytes=_HpnicfDot11APLocalAllRxBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,7,1,7),_HpnicfDot11APLocalAllRxBytes_Type())
hpnicfDot11APLocalAllRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APLocalAllRxBytes.setStatus(_A)
_HpnicfDot11APLocalAllTxBytes_Type=Counter64
_HpnicfDot11APLocalAllTxBytes_Object=MibTableColumn
hpnicfDot11APLocalAllTxBytes=_HpnicfDot11APLocalAllTxBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,7,1,8),_HpnicfDot11APLocalAllTxBytes_Type())
hpnicfDot11APLocalAllTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APLocalAllTxBytes.setStatus(_A)
_HpnicfDot11RadioAssocStatisTable_Object=MibTable
hpnicfDot11RadioAssocStatisTable=_HpnicfDot11RadioAssocStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,8))
if mibBuilder.loadTexts:hpnicfDot11RadioAssocStatisTable.setStatus(_A)
_HpnicfDot11RadioAssocStatisEntry_Object=MibTableRow
hpnicfDot11RadioAssocStatisEntry=_HpnicfDot11RadioAssocStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,8,1))
hpnicfDot11RadioAssocStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:hpnicfDot11RadioAssocStatisEntry.setStatus(_A)
_HpnicfDot11RadioStaAssocSum_Type=Counter32
_HpnicfDot11RadioStaAssocSum_Object=MibTableColumn
hpnicfDot11RadioStaAssocSum=_HpnicfDot11RadioStaAssocSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,8,1,1),_HpnicfDot11RadioStaAssocSum_Type())
hpnicfDot11RadioStaAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioStaAssocSum.setStatus(_A)
_HpnicfDot11RadioStaAssocFailSum_Type=Counter32
_HpnicfDot11RadioStaAssocFailSum_Object=MibTableColumn
hpnicfDot11RadioStaAssocFailSum=_HpnicfDot11RadioStaAssocFailSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,8,1,2),_HpnicfDot11RadioStaAssocFailSum_Type())
hpnicfDot11RadioStaAssocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioStaAssocFailSum.setStatus(_A)
_HpnicfDot11RadioStaReassocSum_Type=Counter32
_HpnicfDot11RadioStaReassocSum_Object=MibTableColumn
hpnicfDot11RadioStaReassocSum=_HpnicfDot11RadioStaReassocSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,8,1,3),_HpnicfDot11RadioStaReassocSum_Type())
hpnicfDot11RadioStaReassocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioStaReassocSum.setStatus(_A)
_HpnicfDot11RadioStaAssocRejectSum_Type=Counter32
_HpnicfDot11RadioStaAssocRejectSum_Object=MibTableColumn
hpnicfDot11RadioStaAssocRejectSum=_HpnicfDot11RadioStaAssocRejectSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,8,1,4),_HpnicfDot11RadioStaAssocRejectSum_Type())
hpnicfDot11RadioStaAssocRejectSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioStaAssocRejectSum.setStatus(_A)
_HpnicfDot11RadioStaExDeAssocSum_Type=Counter32
_HpnicfDot11RadioStaExDeAssocSum_Object=MibTableColumn
hpnicfDot11RadioStaExDeAssocSum=_HpnicfDot11RadioStaExDeAssocSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,8,1,5),_HpnicfDot11RadioStaExDeAssocSum_Type())
hpnicfDot11RadioStaExDeAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioStaExDeAssocSum.setStatus(_A)
_HpnicfDot11RadioStaCurAssocSum_Type=Integer32
_HpnicfDot11RadioStaCurAssocSum_Object=MibTableColumn
hpnicfDot11RadioStaCurAssocSum=_HpnicfDot11RadioStaCurAssocSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,8,1,6),_HpnicfDot11RadioStaCurAssocSum_Type())
hpnicfDot11RadioStaCurAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioStaCurAssocSum.setStatus(_A)
_HpnicfDot11RadioMngFrameStatisTable_Object=MibTable
hpnicfDot11RadioMngFrameStatisTable=_HpnicfDot11RadioMngFrameStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,9))
if mibBuilder.loadTexts:hpnicfDot11RadioMngFrameStatisTable.setStatus(_A)
_HpnicfDot11RadioMngFrameStatisEntry_Object=MibTableRow
hpnicfDot11RadioMngFrameStatisEntry=_HpnicfDot11RadioMngFrameStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,9,1))
hpnicfDot11RadioMngFrameStatisEntry.setIndexNames((0,_C,_A3),(0,_C,_A4))
if mibBuilder.loadTexts:hpnicfDot11RadioMngFrameStatisEntry.setStatus(_A)
_HpnicfDot11RadioStatisIndex_Type=HpnicfDot11RadioElementIndex
_HpnicfDot11RadioStatisIndex_Object=MibTableColumn
hpnicfDot11RadioStatisIndex=_HpnicfDot11RadioStatisIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,9,1,1),_HpnicfDot11RadioStatisIndex_Type())
hpnicfDot11RadioStatisIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11RadioStatisIndex.setStatus(_A)
class _HpnicfDot11MngFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('assocReq',1),(_A5,2),(_A6,3),(_A7,4),('probeReq',5),(_A8,6),('beacon',7),('atim',8),(_A9,9),(_AA,10),(_AB,11),('action',12)))
_HpnicfDot11MngFrameType_Type.__name__=_D
_HpnicfDot11MngFrameType_Object=MibTableColumn
hpnicfDot11MngFrameType=_HpnicfDot11MngFrameType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,9,1,2),_HpnicfDot11MngFrameType_Type())
hpnicfDot11MngFrameType.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11MngFrameType.setStatus(_A)
_HpnicfDot11MngFrameCnt_Type=Counter32
_HpnicfDot11MngFrameCnt_Object=MibTableColumn
hpnicfDot11MngFrameCnt=_HpnicfDot11MngFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,9,1,3),_HpnicfDot11MngFrameCnt_Type())
hpnicfDot11MngFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11MngFrameCnt.setStatus(_A)
_HpnicfDot11APAuthFailStatisTable_Object=MibTable
hpnicfDot11APAuthFailStatisTable=_HpnicfDot11APAuthFailStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,10))
if mibBuilder.loadTexts:hpnicfDot11APAuthFailStatisTable.setStatus(_A)
_HpnicfDot11APAuthFailStatisEntry_Object=MibTableRow
hpnicfDot11APAuthFailStatisEntry=_HpnicfDot11APAuthFailStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,10,1))
hpnicfDot11APAuthFailStatisEntry.setIndexNames((0,_C,_E),(0,_C,_AC))
if mibBuilder.loadTexts:hpnicfDot11APAuthFailStatisEntry.setStatus(_A)
class _HpnicfDot11APAuthFailStatisType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_b,1),(_c,2),(_d,3),(_Q,4)))
_HpnicfDot11APAuthFailStatisType_Type.__name__=_D
_HpnicfDot11APAuthFailStatisType_Object=MibTableColumn
hpnicfDot11APAuthFailStatisType=_HpnicfDot11APAuthFailStatisType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,10,1,1),_HpnicfDot11APAuthFailStatisType_Type())
hpnicfDot11APAuthFailStatisType.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APAuthFailStatisType.setStatus(_A)
_HpnicfDot11APAuthFailStatisCnt_Type=Counter32
_HpnicfDot11APAuthFailStatisCnt_Object=MibTableColumn
hpnicfDot11APAuthFailStatisCnt=_HpnicfDot11APAuthFailStatisCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,10,1,2),_HpnicfDot11APAuthFailStatisCnt_Type())
hpnicfDot11APAuthFailStatisCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAuthFailStatisCnt.setStatus(_A)
_HpnicfDot11APAssocFailStatisTable_Object=MibTable
hpnicfDot11APAssocFailStatisTable=_HpnicfDot11APAssocFailStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,11))
if mibBuilder.loadTexts:hpnicfDot11APAssocFailStatisTable.setStatus(_A)
_HpnicfDot11APAssocFailStatisEntry_Object=MibTableRow
hpnicfDot11APAssocFailStatisEntry=_HpnicfDot11APAssocFailStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,11,1))
hpnicfDot11APAssocFailStatisEntry.setIndexNames((0,_C,_E),(0,_C,_AD))
if mibBuilder.loadTexts:hpnicfDot11APAssocFailStatisEntry.setStatus(_A)
class _HpnicfDot11APAssocFailStatisType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_b,1),(_c,2),(_d,3),(_Q,4)))
_HpnicfDot11APAssocFailStatisType_Type.__name__=_D
_HpnicfDot11APAssocFailStatisType_Object=MibTableColumn
hpnicfDot11APAssocFailStatisType=_HpnicfDot11APAssocFailStatisType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,11,1,1),_HpnicfDot11APAssocFailStatisType_Type())
hpnicfDot11APAssocFailStatisType.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APAssocFailStatisType.setStatus(_A)
_HpnicfDot11APAssocFailStatisCnt_Type=Counter32
_HpnicfDot11APAssocFailStatisCnt_Object=MibTableColumn
hpnicfDot11APAssocFailStatisCnt=_HpnicfDot11APAssocFailStatisCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,11,1,2),_HpnicfDot11APAssocFailStatisCnt_Type())
hpnicfDot11APAssocFailStatisCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAssocFailStatisCnt.setStatus(_A)
_HpnicfDot11APReassocStatisTable_Object=MibTable
hpnicfDot11APReassocStatisTable=_HpnicfDot11APReassocStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,12))
if mibBuilder.loadTexts:hpnicfDot11APReassocStatisTable.setStatus(_A)
_HpnicfDot11APReassocStatisEntry_Object=MibTableRow
hpnicfDot11APReassocStatisEntry=_HpnicfDot11APReassocStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,12,1))
hpnicfDot11APReassocStatisEntry.setIndexNames((0,_C,_E),(0,_C,_AE))
if mibBuilder.loadTexts:hpnicfDot11APReassocStatisEntry.setStatus(_A)
class _HpnicfDot11APReassocStatisType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_e,1),('success',2),(_b,3),(_c,4),(_d,5),(_Q,6)))
_HpnicfDot11APReassocStatisType_Type.__name__=_D
_HpnicfDot11APReassocStatisType_Object=MibTableColumn
hpnicfDot11APReassocStatisType=_HpnicfDot11APReassocStatisType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,12,1,1),_HpnicfDot11APReassocStatisType_Type())
hpnicfDot11APReassocStatisType.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APReassocStatisType.setStatus(_A)
_HpnicfDot11APReassocStatisCnt_Type=Counter32
_HpnicfDot11APReassocStatisCnt_Object=MibTableColumn
hpnicfDot11APReassocStatisCnt=_HpnicfDot11APReassocStatisCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,12,1,2),_HpnicfDot11APReassocStatisCnt_Type())
hpnicfDot11APReassocStatisCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APReassocStatisCnt.setStatus(_A)
_HpnicfDot11APUserAuthStatisTable_Object=MibTable
hpnicfDot11APUserAuthStatisTable=_HpnicfDot11APUserAuthStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,13))
if mibBuilder.loadTexts:hpnicfDot11APUserAuthStatisTable.setStatus(_A)
_HpnicfDot11APUserAuthStatisEntry_Object=MibTableRow
hpnicfDot11APUserAuthStatisEntry=_HpnicfDot11APUserAuthStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,13,1))
hpnicfDot11APUserAuthStatisEntry.setIndexNames((0,_C,_E),(0,_C,_AF))
if mibBuilder.loadTexts:hpnicfDot11APUserAuthStatisEntry.setStatus(_A)
class _HpnicfDot11UserAuthStatisType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_e,1),('success',2),('keyError',3),(_b,4),(_c,5),(_d,6),(_Q,7)))
_HpnicfDot11UserAuthStatisType_Type.__name__=_D
_HpnicfDot11UserAuthStatisType_Object=MibTableColumn
hpnicfDot11UserAuthStatisType=_HpnicfDot11UserAuthStatisType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,13,1,1),_HpnicfDot11UserAuthStatisType_Type())
hpnicfDot11UserAuthStatisType.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11UserAuthStatisType.setStatus(_A)
_HpnicfDot11UserAuthStatisCnt_Type=Counter32
_HpnicfDot11UserAuthStatisCnt_Object=MibTableColumn
hpnicfDot11UserAuthStatisCnt=_HpnicfDot11UserAuthStatisCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,13,1,2),_HpnicfDot11UserAuthStatisCnt_Type())
hpnicfDot11UserAuthStatisCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11UserAuthStatisCnt.setStatus(_A)
_HpnicfDot11APDeauthStatisTable_Object=MibTable
hpnicfDot11APDeauthStatisTable=_HpnicfDot11APDeauthStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,14))
if mibBuilder.loadTexts:hpnicfDot11APDeauthStatisTable.setStatus(_A)
_HpnicfDot11APDeauthStatisEntry_Object=MibTableRow
hpnicfDot11APDeauthStatisEntry=_HpnicfDot11APDeauthStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,14,1))
hpnicfDot11APDeauthStatisEntry.setIndexNames((0,_C,_E),(0,_C,_AG))
if mibBuilder.loadTexts:hpnicfDot11APDeauthStatisEntry.setStatus(_A)
class _HpnicfDot11APDeauthStatisType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_e,1),(_AH,2),(_m,3),(_AI,4),(_Q,5)))
_HpnicfDot11APDeauthStatisType_Type.__name__=_D
_HpnicfDot11APDeauthStatisType_Object=MibTableColumn
hpnicfDot11APDeauthStatisType=_HpnicfDot11APDeauthStatisType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,14,1,1),_HpnicfDot11APDeauthStatisType_Type())
hpnicfDot11APDeauthStatisType.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APDeauthStatisType.setStatus(_A)
_HpnicfDot11APDeauthStatisCnt_Type=Counter32
_HpnicfDot11APDeauthStatisCnt_Object=MibTableColumn
hpnicfDot11APDeauthStatisCnt=_HpnicfDot11APDeauthStatisCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,14,1,2),_HpnicfDot11APDeauthStatisCnt_Type())
hpnicfDot11APDeauthStatisCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APDeauthStatisCnt.setStatus(_A)
_HpnicfDot11APDeassocStatisTable_Object=MibTable
hpnicfDot11APDeassocStatisTable=_HpnicfDot11APDeassocStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,15))
if mibBuilder.loadTexts:hpnicfDot11APDeassocStatisTable.setStatus(_A)
_HpnicfDot11APDeassocStatisEntry_Object=MibTableRow
hpnicfDot11APDeassocStatisEntry=_HpnicfDot11APDeassocStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,15,1))
hpnicfDot11APDeassocStatisEntry.setIndexNames((0,_C,_E),(0,_C,_AJ))
if mibBuilder.loadTexts:hpnicfDot11APDeassocStatisEntry.setStatus(_A)
class _HpnicfDot11APDeassocStatisType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_e,1),(_AH,2),(_m,3),(_AI,4),(_Q,5)))
_HpnicfDot11APDeassocStatisType_Type.__name__=_D
_HpnicfDot11APDeassocStatisType_Object=MibTableColumn
hpnicfDot11APDeassocStatisType=_HpnicfDot11APDeassocStatisType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,15,1,1),_HpnicfDot11APDeassocStatisType_Type())
hpnicfDot11APDeassocStatisType.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APDeassocStatisType.setStatus(_A)
_HpnicfDot11APDeassocStatisCnt_Type=Counter32
_HpnicfDot11APDeassocStatisCnt_Object=MibTableColumn
hpnicfDot11APDeassocStatisCnt=_HpnicfDot11APDeassocStatisCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,15,1,2),_HpnicfDot11APDeassocStatisCnt_Type())
hpnicfDot11APDeassocStatisCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APDeassocStatisCnt.setStatus(_A)
_HpnicfDot11APAssocFailStatis2Table_Object=MibTable
hpnicfDot11APAssocFailStatis2Table=_HpnicfDot11APAssocFailStatis2Table_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,16))
if mibBuilder.loadTexts:hpnicfDot11APAssocFailStatis2Table.setStatus(_A)
_HpnicfDot11APAssocFailStatis2Entry_Object=MibTableRow
hpnicfDot11APAssocFailStatis2Entry=_HpnicfDot11APAssocFailStatis2Entry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,16,1))
hpnicfDot11APAssocFailStatis2Entry.setIndexNames((0,_C,_E),(0,_C,_AK))
if mibBuilder.loadTexts:hpnicfDot11APAssocFailStatis2Entry.setStatus(_A)
class _HpnicfDot11APAssocFailStatis2Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_m,1),('notSupportRateSet',2),('unknownReasonCode',3),(_Q,4),('rssiLowness',5)))
_HpnicfDot11APAssocFailStatis2Type_Type.__name__=_D
_HpnicfDot11APAssocFailStatis2Type_Object=MibTableColumn
hpnicfDot11APAssocFailStatis2Type=_HpnicfDot11APAssocFailStatis2Type_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,16,1,1),_HpnicfDot11APAssocFailStatis2Type_Type())
hpnicfDot11APAssocFailStatis2Type.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APAssocFailStatis2Type.setStatus(_A)
_HpnicfDot11APAssocFailStatis2Cnt_Type=Counter32
_HpnicfDot11APAssocFailStatis2Cnt_Object=MibTableColumn
hpnicfDot11APAssocFailStatis2Cnt=_HpnicfDot11APAssocFailStatis2Cnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,16,1,2),_HpnicfDot11APAssocFailStatis2Cnt_Type())
hpnicfDot11APAssocFailStatis2Cnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAssocFailStatis2Cnt.setStatus(_A)
_HpnicfDot11APIfStatisTable_Object=MibTable
hpnicfDot11APIfStatisTable=_HpnicfDot11APIfStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17))
if mibBuilder.loadTexts:hpnicfDot11APIfStatisTable.setStatus(_A)
_HpnicfDot11APIfStatisEntry_Object=MibTableRow
hpnicfDot11APIfStatisEntry=_HpnicfDot11APIfStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1))
hpnicfDot11APIfStatisEntry.setIndexNames((0,_g,_h),(0,_C,_a))
if mibBuilder.loadTexts:hpnicfDot11APIfStatisEntry.setStatus(_A)
_HpnicfDot11APIfInPkts_Type=Counter32
_HpnicfDot11APIfInPkts_Object=MibTableColumn
hpnicfDot11APIfInPkts=_HpnicfDot11APIfInPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,1),_HpnicfDot11APIfInPkts_Type())
hpnicfDot11APIfInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInPkts.setStatus(_A)
_HpnicfDot11APIfInNormalPkts_Type=Counter32
_HpnicfDot11APIfInNormalPkts_Object=MibTableColumn
hpnicfDot11APIfInNormalPkts=_HpnicfDot11APIfInNormalPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,2),_HpnicfDot11APIfInNormalPkts_Type())
hpnicfDot11APIfInNormalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInNormalPkts.setStatus(_A)
_HpnicfDot11APIfInErrorPkts_Type=Counter32
_HpnicfDot11APIfInErrorPkts_Object=MibTableColumn
hpnicfDot11APIfInErrorPkts=_HpnicfDot11APIfInErrorPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,3),_HpnicfDot11APIfInErrorPkts_Type())
hpnicfDot11APIfInErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInErrorPkts.setStatus(_A)
_HpnicfDot11APIfOutPkts_Type=Counter32
_HpnicfDot11APIfOutPkts_Object=MibTableColumn
hpnicfDot11APIfOutPkts=_HpnicfDot11APIfOutPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,4),_HpnicfDot11APIfOutPkts_Type())
hpnicfDot11APIfOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutPkts.setStatus(_A)
_HpnicfDot11APIfInOctets_Type=Counter32
_HpnicfDot11APIfInOctets_Object=MibTableColumn
hpnicfDot11APIfInOctets=_HpnicfDot11APIfInOctets_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,5),_HpnicfDot11APIfInOctets_Type())
hpnicfDot11APIfInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInOctets.setStatus(_A)
_HpnicfDot11APIfOutOctets_Type=Counter32
_HpnicfDot11APIfOutOctets_Object=MibTableColumn
hpnicfDot11APIfOutOctets=_HpnicfDot11APIfOutOctets_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,6),_HpnicfDot11APIfOutOctets_Type())
hpnicfDot11APIfOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutOctets.setStatus(_A)
_HpnicfDot11APIfFlowOut_Type=Unsigned32
_HpnicfDot11APIfFlowOut_Object=MibTableColumn
hpnicfDot11APIfFlowOut=_HpnicfDot11APIfFlowOut_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,7),_HpnicfDot11APIfFlowOut_Type())
hpnicfDot11APIfFlowOut.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfFlowOut.setStatus(_A)
_HpnicfDot11APIfFlowIN_Type=Unsigned32
_HpnicfDot11APIfFlowIN_Object=MibTableColumn
hpnicfDot11APIfFlowIN=_HpnicfDot11APIfFlowIN_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,8),_HpnicfDot11APIfFlowIN_Type())
hpnicfDot11APIfFlowIN.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfFlowIN.setStatus(_A)
_HpnicfDot11APIfInUcastPkts_Type=Counter32
_HpnicfDot11APIfInUcastPkts_Object=MibTableColumn
hpnicfDot11APIfInUcastPkts=_HpnicfDot11APIfInUcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,9),_HpnicfDot11APIfInUcastPkts_Type())
hpnicfDot11APIfInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInUcastPkts.setStatus(_A)
_HpnicfDot11APIfInNUcastPkts_Type=Counter32
_HpnicfDot11APIfInNUcastPkts_Object=MibTableColumn
hpnicfDot11APIfInNUcastPkts=_HpnicfDot11APIfInNUcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,10),_HpnicfDot11APIfInNUcastPkts_Type())
hpnicfDot11APIfInNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInNUcastPkts.setStatus(_A)
_HpnicfDot11APIfInDiscardPkts_Type=Counter32
_HpnicfDot11APIfInDiscardPkts_Object=MibTableColumn
hpnicfDot11APIfInDiscardPkts=_HpnicfDot11APIfInDiscardPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,11),_HpnicfDot11APIfInDiscardPkts_Type())
hpnicfDot11APIfInDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInDiscardPkts.setStatus(_A)
_HpnicfDot11APIfOutUcastPkts_Type=Counter32
_HpnicfDot11APIfOutUcastPkts_Object=MibTableColumn
hpnicfDot11APIfOutUcastPkts=_HpnicfDot11APIfOutUcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,12),_HpnicfDot11APIfOutUcastPkts_Type())
hpnicfDot11APIfOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutUcastPkts.setStatus(_A)
_HpnicfDot11APIfOutNUcastPkts_Type=Counter32
_HpnicfDot11APIfOutNUcastPkts_Object=MibTableColumn
hpnicfDot11APIfOutNUcastPkts=_HpnicfDot11APIfOutNUcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,13),_HpnicfDot11APIfOutNUcastPkts_Type())
hpnicfDot11APIfOutNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutNUcastPkts.setStatus(_A)
_HpnicfDot11APIfOutDiscardPkts_Type=Counter32
_HpnicfDot11APIfOutDiscardPkts_Object=MibTableColumn
hpnicfDot11APIfOutDiscardPkts=_HpnicfDot11APIfOutDiscardPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,14),_HpnicfDot11APIfOutDiscardPkts_Type())
hpnicfDot11APIfOutDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutDiscardPkts.setStatus(_A)
_HpnicfDot11APIfOutErrorPkts_Type=Counter32
_HpnicfDot11APIfOutErrorPkts_Object=MibTableColumn
hpnicfDot11APIfOutErrorPkts=_HpnicfDot11APIfOutErrorPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,15),_HpnicfDot11APIfOutErrorPkts_Type())
hpnicfDot11APIfOutErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutErrorPkts.setStatus(_A)
_HpnicfDot11APIfUpdownTimes_Type=Counter32
_HpnicfDot11APIfUpdownTimes_Object=MibTableColumn
hpnicfDot11APIfUpdownTimes=_HpnicfDot11APIfUpdownTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,16),_HpnicfDot11APIfUpdownTimes_Type())
hpnicfDot11APIfUpdownTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfUpdownTimes.setStatus(_A)
_HpnicfDot11APIfStatusKeepTime_Type=TimeTicks
_HpnicfDot11APIfStatusKeepTime_Object=MibTableColumn
hpnicfDot11APIfStatusKeepTime=_HpnicfDot11APIfStatusKeepTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,17),_HpnicfDot11APIfStatusKeepTime_Type())
hpnicfDot11APIfStatusKeepTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfStatusKeepTime.setStatus(_A)
class _HpnicfDot11APIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_f,4),('dormant',5),(_AL,6),(_AM,7)))
_HpnicfDot11APIfOperStatus_Type.__name__=_D
_HpnicfDot11APIfOperStatus_Object=MibTableColumn
hpnicfDot11APIfOperStatus=_HpnicfDot11APIfOperStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,18),_HpnicfDot11APIfOperStatus_Type())
hpnicfDot11APIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOperStatus.setStatus(_A)
_HpnicfDot11APIfInBrdcastPkts_Type=Counter64
_HpnicfDot11APIfInBrdcastPkts_Object=MibTableColumn
hpnicfDot11APIfInBrdcastPkts=_HpnicfDot11APIfInBrdcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,19),_HpnicfDot11APIfInBrdcastPkts_Type())
hpnicfDot11APIfInBrdcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInBrdcastPkts.setStatus(_A)
_HpnicfDot11APIfOutBrdcastPkts_Type=Counter64
_HpnicfDot11APIfOutBrdcastPkts_Object=MibTableColumn
hpnicfDot11APIfOutBrdcastPkts=_HpnicfDot11APIfOutBrdcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,20),_HpnicfDot11APIfOutBrdcastPkts_Type())
hpnicfDot11APIfOutBrdcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutBrdcastPkts.setStatus(_A)
_HpnicfDot11APIfInMulcastPkts_Type=Counter64
_HpnicfDot11APIfInMulcastPkts_Object=MibTableColumn
hpnicfDot11APIfInMulcastPkts=_HpnicfDot11APIfInMulcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,21),_HpnicfDot11APIfInMulcastPkts_Type())
hpnicfDot11APIfInMulcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInMulcastPkts.setStatus(_A)
_HpnicfDot11APIfOutMulcastPkts_Type=Counter64
_HpnicfDot11APIfOutMulcastPkts_Object=MibTableColumn
hpnicfDot11APIfOutMulcastPkts=_HpnicfDot11APIfOutMulcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,22),_HpnicfDot11APIfOutMulcastPkts_Type())
hpnicfDot11APIfOutMulcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutMulcastPkts.setStatus(_A)
_HpnicfDot11APIfInPayloadOctets_Type=Counter64
_HpnicfDot11APIfInPayloadOctets_Object=MibTableColumn
hpnicfDot11APIfInPayloadOctets=_HpnicfDot11APIfInPayloadOctets_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,23),_HpnicfDot11APIfInPayloadOctets_Type())
hpnicfDot11APIfInPayloadOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInPayloadOctets.setStatus(_A)
_HpnicfDot11APIfOutPayloadOctets_Type=Counter64
_HpnicfDot11APIfOutPayloadOctets_Object=MibTableColumn
hpnicfDot11APIfOutPayloadOctets=_HpnicfDot11APIfOutPayloadOctets_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,17,1,24),_HpnicfDot11APIfOutPayloadOctets_Type())
hpnicfDot11APIfOutPayloadOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutPayloadOctets.setStatus(_A)
_HpnicfDot11RadioMngFrmStatisTable_Object=MibTable
hpnicfDot11RadioMngFrmStatisTable=_HpnicfDot11RadioMngFrmStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,18))
if mibBuilder.loadTexts:hpnicfDot11RadioMngFrmStatisTable.setStatus(_A)
_HpnicfDot11RadioMngFrmStatisEntry_Object=MibTableRow
hpnicfDot11RadioMngFrmStatisEntry=_HpnicfDot11RadioMngFrmStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,18,1))
hpnicfDot11RadioMngFrmStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_AN))
if mibBuilder.loadTexts:hpnicfDot11RadioMngFrmStatisEntry.setStatus(_A)
class _HpnicfDot11MngFrmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('assocReq',1),(_A5,2),(_A6,3),(_A7,4),('probeReq',5),(_A8,6),('beacon',7),('atim',8),(_A9,9),(_AA,10),(_AB,11),('action',12)))
_HpnicfDot11MngFrmType_Type.__name__=_D
_HpnicfDot11MngFrmType_Object=MibTableColumn
hpnicfDot11MngFrmType=_HpnicfDot11MngFrmType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,18,1,1),_HpnicfDot11MngFrmType_Type())
hpnicfDot11MngFrmType.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11MngFrmType.setStatus(_A)
_HpnicfDot11MngFrmCnt_Type=Counter32
_HpnicfDot11MngFrmCnt_Object=MibTableColumn
hpnicfDot11MngFrmCnt=_HpnicfDot11MngFrmCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,18,1,2),_HpnicfDot11MngFrmCnt_Type())
hpnicfDot11MngFrmCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11MngFrmCnt.setStatus(_A)
_HpnicfDot11APPacketSizeStatisTable_Object=MibTable
hpnicfDot11APPacketSizeStatisTable=_HpnicfDot11APPacketSizeStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,19))
if mibBuilder.loadTexts:hpnicfDot11APPacketSizeStatisTable.setStatus(_A)
_HpnicfDot11APPacketSizeStatisEntry_Object=MibTableRow
hpnicfDot11APPacketSizeStatisEntry=_HpnicfDot11APPacketSizeStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,19,1))
hpnicfDot11APPacketSizeStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_AO))
if mibBuilder.loadTexts:hpnicfDot11APPacketSizeStatisEntry.setStatus(_A)
class _HpnicfDot11APPacketSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sizeLevel1',1),('sizeLevel2',2),('sizeLevel3',3),('sizeLevel4',4)))
_HpnicfDot11APPacketSize_Type.__name__=_D
_HpnicfDot11APPacketSize_Object=MibTableColumn
hpnicfDot11APPacketSize=_HpnicfDot11APPacketSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,19,1,1),_HpnicfDot11APPacketSize_Type())
hpnicfDot11APPacketSize.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APPacketSize.setStatus(_A)
_HpnicfDot11APRXPacketSizeCount_Type=Counter64
_HpnicfDot11APRXPacketSizeCount_Object=MibTableColumn
hpnicfDot11APRXPacketSizeCount=_HpnicfDot11APRXPacketSizeCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,19,1,2),_HpnicfDot11APRXPacketSizeCount_Type())
hpnicfDot11APRXPacketSizeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APRXPacketSizeCount.setStatus(_A)
_HpnicfDot11APTXPacketSizeCount_Type=Counter64
_HpnicfDot11APTXPacketSizeCount_Object=MibTableColumn
hpnicfDot11APTXPacketSizeCount=_HpnicfDot11APTXPacketSizeCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,19,1,3),_HpnicfDot11APTXPacketSizeCount_Type())
hpnicfDot11APTXPacketSizeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APTXPacketSizeCount.setStatus(_A)
_HpnicfDot11APPacketRateStatisTable_Object=MibTable
hpnicfDot11APPacketRateStatisTable=_HpnicfDot11APPacketRateStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,20))
if mibBuilder.loadTexts:hpnicfDot11APPacketRateStatisTable.setStatus(_A)
_HpnicfDot11APPacketRateStatisEntry_Object=MibTableRow
hpnicfDot11APPacketRateStatisEntry=_HpnicfDot11APPacketRateStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,20,1))
hpnicfDot11APPacketRateStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_AP))
if mibBuilder.loadTexts:hpnicfDot11APPacketRateStatisEntry.setStatus(_A)
_HpnicfDot11APPacketRate_Type=Integer32
_HpnicfDot11APPacketRate_Object=MibTableColumn
hpnicfDot11APPacketRate=_HpnicfDot11APPacketRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,20,1,1),_HpnicfDot11APPacketRate_Type())
hpnicfDot11APPacketRate.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APPacketRate.setStatus(_A)
_HpnicfDot11APRXPacketRateCount_Type=Counter64
_HpnicfDot11APRXPacketRateCount_Object=MibTableColumn
hpnicfDot11APRXPacketRateCount=_HpnicfDot11APRXPacketRateCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,20,1,2),_HpnicfDot11APRXPacketRateCount_Type())
hpnicfDot11APRXPacketRateCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APRXPacketRateCount.setStatus(_A)
_HpnicfDot11APTXPacketRateCount_Type=Counter64
_HpnicfDot11APTXPacketRateCount_Object=MibTableColumn
hpnicfDot11APTXPacketRateCount=_HpnicfDot11APTXPacketRateCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,20,1,3),_HpnicfDot11APTXPacketRateCount_Type())
hpnicfDot11APTXPacketRateCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APTXPacketRateCount.setStatus(_A)
_HpnicfDot11APPacketMCSRateStatisTable_Object=MibTable
hpnicfDot11APPacketMCSRateStatisTable=_HpnicfDot11APPacketMCSRateStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,21))
if mibBuilder.loadTexts:hpnicfDot11APPacketMCSRateStatisTable.setStatus(_A)
_HpnicfDot11APPacketMCSRateStatisEntry_Object=MibTableRow
hpnicfDot11APPacketMCSRateStatisEntry=_HpnicfDot11APPacketMCSRateStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,21,1))
hpnicfDot11APPacketMCSRateStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_AQ))
if mibBuilder.loadTexts:hpnicfDot11APPacketMCSRateStatisEntry.setStatus(_A)
_HpnicfDot11APPacketMCSRate_Type=Integer32
_HpnicfDot11APPacketMCSRate_Object=MibTableColumn
hpnicfDot11APPacketMCSRate=_HpnicfDot11APPacketMCSRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,21,1,1),_HpnicfDot11APPacketMCSRate_Type())
hpnicfDot11APPacketMCSRate.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APPacketMCSRate.setStatus(_A)
_HpnicfDot11APRXPacketMCSRateCount_Type=Counter64
_HpnicfDot11APRXPacketMCSRateCount_Object=MibTableColumn
hpnicfDot11APRXPacketMCSRateCount=_HpnicfDot11APRXPacketMCSRateCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,21,1,2),_HpnicfDot11APRXPacketMCSRateCount_Type())
hpnicfDot11APRXPacketMCSRateCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APRXPacketMCSRateCount.setStatus(_A)
_HpnicfDot11APTXPacketMCSRateCount_Type=Counter64
_HpnicfDot11APTXPacketMCSRateCount_Object=MibTableColumn
hpnicfDot11APTXPacketMCSRateCount=_HpnicfDot11APTXPacketMCSRateCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,21,1,3),_HpnicfDot11APTXPacketMCSRateCount_Type())
hpnicfDot11APTXPacketMCSRateCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APTXPacketMCSRateCount.setStatus(_A)
_HpnicfDot11APAssocFailStatis3Table_Object=MibTable
hpnicfDot11APAssocFailStatis3Table=_HpnicfDot11APAssocFailStatis3Table_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,22))
if mibBuilder.loadTexts:hpnicfDot11APAssocFailStatis3Table.setStatus(_A)
_HpnicfDot11APAssocFailStatis3Entry_Object=MibTableRow
hpnicfDot11APAssocFailStatis3Entry=_HpnicfDot11APAssocFailStatis3Entry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,22,1))
hpnicfDot11APAssocFailStatis3Entry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:hpnicfDot11APAssocFailStatis3Entry.setStatus(_A)
_HpnicfDot11APAssocFailStatis3SRCnt_Type=Counter32
_HpnicfDot11APAssocFailStatis3SRCnt_Object=MibTableColumn
hpnicfDot11APAssocFailStatis3SRCnt=_HpnicfDot11APAssocFailStatis3SRCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,22,1,1),_HpnicfDot11APAssocFailStatis3SRCnt_Type())
hpnicfDot11APAssocFailStatis3SRCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAssocFailStatis3SRCnt.setStatus(_A)
_HpnicfDot11APAssocFailStatis3NSRCnt_Type=Counter32
_HpnicfDot11APAssocFailStatis3NSRCnt_Object=MibTableColumn
hpnicfDot11APAssocFailStatis3NSRCnt=_HpnicfDot11APAssocFailStatis3NSRCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,22,1,2),_HpnicfDot11APAssocFailStatis3NSRCnt_Type())
hpnicfDot11APAssocFailStatis3NSRCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAssocFailStatis3NSRCnt.setStatus(_A)
_HpnicfDot11APAssocFailStatis3URCCnt_Type=Counter32
_HpnicfDot11APAssocFailStatis3URCCnt_Object=MibTableColumn
hpnicfDot11APAssocFailStatis3URCCnt=_HpnicfDot11APAssocFailStatis3URCCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,22,1,3),_HpnicfDot11APAssocFailStatis3URCCnt_Type())
hpnicfDot11APAssocFailStatis3URCCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAssocFailStatis3URCCnt.setStatus(_A)
_HpnicfDot11APAssocFailStatis3RFCnt_Type=Counter32
_HpnicfDot11APAssocFailStatis3RFCnt_Object=MibTableColumn
hpnicfDot11APAssocFailStatis3RFCnt=_HpnicfDot11APAssocFailStatis3RFCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,22,1,4),_HpnicfDot11APAssocFailStatis3RFCnt_Type())
hpnicfDot11APAssocFailStatis3RFCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAssocFailStatis3RFCnt.setStatus(_A)
_HpnicfDot11APAssocFailStatis3OtherCnt_Type=Counter32
_HpnicfDot11APAssocFailStatis3OtherCnt_Object=MibTableColumn
hpnicfDot11APAssocFailStatis3OtherCnt=_HpnicfDot11APAssocFailStatis3OtherCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,22,1,5),_HpnicfDot11APAssocFailStatis3OtherCnt_Type())
hpnicfDot11APAssocFailStatis3OtherCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAssocFailStatis3OtherCnt.setStatus(_A)
_HpnicfDot11APAssocFailStatis3RSSILowCntCM_Type=Counter32
_HpnicfDot11APAssocFailStatis3RSSILowCntCM_Object=MibTableColumn
hpnicfDot11APAssocFailStatis3RSSILowCntCM=_HpnicfDot11APAssocFailStatis3RSSILowCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,22,1,6),_HpnicfDot11APAssocFailStatis3RSSILowCntCM_Type())
hpnicfDot11APAssocFailStatis3RSSILowCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAssocFailStatis3RSSILowCntCM.setStatus(_A)
_HpnicfDot11APIfStatisByAPIDTable_Object=MibTable
hpnicfDot11APIfStatisByAPIDTable=_HpnicfDot11APIfStatisByAPIDTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23))
if mibBuilder.loadTexts:hpnicfDot11APIfStatisByAPIDTable.setStatus(_A)
_HpnicfDot11APIfStatisByAPIDEntry_Object=MibTableRow
hpnicfDot11APIfStatisByAPIDEntry=_HpnicfDot11APIfStatisByAPIDEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1))
hpnicfDot11APIfStatisByAPIDEntry.setIndexNames((0,_C,_E),(0,_C,_a))
if mibBuilder.loadTexts:hpnicfDot11APIfStatisByAPIDEntry.setStatus(_A)
_HpnicfDot11APIfInPkts2_Type=Counter64
_HpnicfDot11APIfInPkts2_Object=MibTableColumn
hpnicfDot11APIfInPkts2=_HpnicfDot11APIfInPkts2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,1),_HpnicfDot11APIfInPkts2_Type())
hpnicfDot11APIfInPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInPkts2.setStatus(_A)
_HpnicfDot11APIfInNormalPkts2_Type=Counter64
_HpnicfDot11APIfInNormalPkts2_Object=MibTableColumn
hpnicfDot11APIfInNormalPkts2=_HpnicfDot11APIfInNormalPkts2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,2),_HpnicfDot11APIfInNormalPkts2_Type())
hpnicfDot11APIfInNormalPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInNormalPkts2.setStatus(_A)
_HpnicfDot11APIfInErrorPkts2_Type=Counter64
_HpnicfDot11APIfInErrorPkts2_Object=MibTableColumn
hpnicfDot11APIfInErrorPkts2=_HpnicfDot11APIfInErrorPkts2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,3),_HpnicfDot11APIfInErrorPkts2_Type())
hpnicfDot11APIfInErrorPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInErrorPkts2.setStatus(_A)
_HpnicfDot11APIfOutPkts2_Type=Counter64
_HpnicfDot11APIfOutPkts2_Object=MibTableColumn
hpnicfDot11APIfOutPkts2=_HpnicfDot11APIfOutPkts2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,4),_HpnicfDot11APIfOutPkts2_Type())
hpnicfDot11APIfOutPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutPkts2.setStatus(_A)
_HpnicfDot11APIfInOctets2_Type=Counter64
_HpnicfDot11APIfInOctets2_Object=MibTableColumn
hpnicfDot11APIfInOctets2=_HpnicfDot11APIfInOctets2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,5),_HpnicfDot11APIfInOctets2_Type())
hpnicfDot11APIfInOctets2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInOctets2.setStatus(_A)
_HpnicfDot11APIfOutOctets2_Type=Counter64
_HpnicfDot11APIfOutOctets2_Object=MibTableColumn
hpnicfDot11APIfOutOctets2=_HpnicfDot11APIfOutOctets2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,6),_HpnicfDot11APIfOutOctets2_Type())
hpnicfDot11APIfOutOctets2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutOctets2.setStatus(_A)
_HpnicfDot11APIfFlowOut2_Type=Unsigned32
_HpnicfDot11APIfFlowOut2_Object=MibTableColumn
hpnicfDot11APIfFlowOut2=_HpnicfDot11APIfFlowOut2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,7),_HpnicfDot11APIfFlowOut2_Type())
hpnicfDot11APIfFlowOut2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfFlowOut2.setStatus(_A)
_HpnicfDot11APIfFlowIN2_Type=Unsigned32
_HpnicfDot11APIfFlowIN2_Object=MibTableColumn
hpnicfDot11APIfFlowIN2=_HpnicfDot11APIfFlowIN2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,8),_HpnicfDot11APIfFlowIN2_Type())
hpnicfDot11APIfFlowIN2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfFlowIN2.setStatus(_A)
_HpnicfDot11APIfInUcastPkts2_Type=Counter64
_HpnicfDot11APIfInUcastPkts2_Object=MibTableColumn
hpnicfDot11APIfInUcastPkts2=_HpnicfDot11APIfInUcastPkts2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,9),_HpnicfDot11APIfInUcastPkts2_Type())
hpnicfDot11APIfInUcastPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInUcastPkts2.setStatus(_A)
_HpnicfDot11APIfInNUcastPkts2_Type=Counter64
_HpnicfDot11APIfInNUcastPkts2_Object=MibTableColumn
hpnicfDot11APIfInNUcastPkts2=_HpnicfDot11APIfInNUcastPkts2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,10),_HpnicfDot11APIfInNUcastPkts2_Type())
hpnicfDot11APIfInNUcastPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInNUcastPkts2.setStatus(_A)
_HpnicfDot11APIfInDiscardPkts2_Type=Counter64
_HpnicfDot11APIfInDiscardPkts2_Object=MibTableColumn
hpnicfDot11APIfInDiscardPkts2=_HpnicfDot11APIfInDiscardPkts2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,11),_HpnicfDot11APIfInDiscardPkts2_Type())
hpnicfDot11APIfInDiscardPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInDiscardPkts2.setStatus(_A)
_HpnicfDot11APIfOutUcastPkts2_Type=Counter64
_HpnicfDot11APIfOutUcastPkts2_Object=MibTableColumn
hpnicfDot11APIfOutUcastPkts2=_HpnicfDot11APIfOutUcastPkts2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,12),_HpnicfDot11APIfOutUcastPkts2_Type())
hpnicfDot11APIfOutUcastPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutUcastPkts2.setStatus(_A)
_HpnicfDot11APIfOutNUcastPkts2_Type=Counter64
_HpnicfDot11APIfOutNUcastPkts2_Object=MibTableColumn
hpnicfDot11APIfOutNUcastPkts2=_HpnicfDot11APIfOutNUcastPkts2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,13),_HpnicfDot11APIfOutNUcastPkts2_Type())
hpnicfDot11APIfOutNUcastPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutNUcastPkts2.setStatus(_A)
_HpnicfDot11APIfOutDiscardPkts2_Type=Counter64
_HpnicfDot11APIfOutDiscardPkts2_Object=MibTableColumn
hpnicfDot11APIfOutDiscardPkts2=_HpnicfDot11APIfOutDiscardPkts2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,14),_HpnicfDot11APIfOutDiscardPkts2_Type())
hpnicfDot11APIfOutDiscardPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutDiscardPkts2.setStatus(_A)
_HpnicfDot11APIfOutErrorPkts2_Type=Counter64
_HpnicfDot11APIfOutErrorPkts2_Object=MibTableColumn
hpnicfDot11APIfOutErrorPkts2=_HpnicfDot11APIfOutErrorPkts2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,15),_HpnicfDot11APIfOutErrorPkts2_Type())
hpnicfDot11APIfOutErrorPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutErrorPkts2.setStatus(_A)
_HpnicfDot11APIfUpdownTimes2_Type=Counter32
_HpnicfDot11APIfUpdownTimes2_Object=MibTableColumn
hpnicfDot11APIfUpdownTimes2=_HpnicfDot11APIfUpdownTimes2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,16),_HpnicfDot11APIfUpdownTimes2_Type())
hpnicfDot11APIfUpdownTimes2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfUpdownTimes2.setStatus(_A)
_HpnicfDot11APIfStatusKeepTime2_Type=TimeTicks
_HpnicfDot11APIfStatusKeepTime2_Object=MibTableColumn
hpnicfDot11APIfStatusKeepTime2=_HpnicfDot11APIfStatusKeepTime2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,17),_HpnicfDot11APIfStatusKeepTime2_Type())
hpnicfDot11APIfStatusKeepTime2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfStatusKeepTime2.setStatus(_A)
class _HpnicfDot11APIfOperStatus2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_f,4),('dormant',5),(_AL,6),(_AM,7)))
_HpnicfDot11APIfOperStatus2_Type.__name__=_D
_HpnicfDot11APIfOperStatus2_Object=MibTableColumn
hpnicfDot11APIfOperStatus2=_HpnicfDot11APIfOperStatus2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,18),_HpnicfDot11APIfOperStatus2_Type())
hpnicfDot11APIfOperStatus2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOperStatus2.setStatus(_A)
_HpnicfDot11APIfInBrdcastPkts2_Type=Counter64
_HpnicfDot11APIfInBrdcastPkts2_Object=MibTableColumn
hpnicfDot11APIfInBrdcastPkts2=_HpnicfDot11APIfInBrdcastPkts2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,19),_HpnicfDot11APIfInBrdcastPkts2_Type())
hpnicfDot11APIfInBrdcastPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInBrdcastPkts2.setStatus(_A)
_HpnicfDot11APIfOutBrdcastPkts2_Type=Counter64
_HpnicfDot11APIfOutBrdcastPkts2_Object=MibTableColumn
hpnicfDot11APIfOutBrdcastPkts2=_HpnicfDot11APIfOutBrdcastPkts2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,20),_HpnicfDot11APIfOutBrdcastPkts2_Type())
hpnicfDot11APIfOutBrdcastPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutBrdcastPkts2.setStatus(_A)
_HpnicfDot11APIfInMulcastPkts2_Type=Counter64
_HpnicfDot11APIfInMulcastPkts2_Object=MibTableColumn
hpnicfDot11APIfInMulcastPkts2=_HpnicfDot11APIfInMulcastPkts2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,21),_HpnicfDot11APIfInMulcastPkts2_Type())
hpnicfDot11APIfInMulcastPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInMulcastPkts2.setStatus(_A)
_HpnicfDot11APIfOutMulcastPkts2_Type=Counter64
_HpnicfDot11APIfOutMulcastPkts2_Object=MibTableColumn
hpnicfDot11APIfOutMulcastPkts2=_HpnicfDot11APIfOutMulcastPkts2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,22),_HpnicfDot11APIfOutMulcastPkts2_Type())
hpnicfDot11APIfOutMulcastPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutMulcastPkts2.setStatus(_A)
_HpnicfDot11APIfInPayloadOctets2_Type=Counter64
_HpnicfDot11APIfInPayloadOctets2_Object=MibTableColumn
hpnicfDot11APIfInPayloadOctets2=_HpnicfDot11APIfInPayloadOctets2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,23),_HpnicfDot11APIfInPayloadOctets2_Type())
hpnicfDot11APIfInPayloadOctets2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInPayloadOctets2.setStatus(_A)
_HpnicfDot11APIfOutPayloadOctets2_Type=Counter64
_HpnicfDot11APIfOutPayloadOctets2_Object=MibTableColumn
hpnicfDot11APIfOutPayloadOctets2=_HpnicfDot11APIfOutPayloadOctets2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,24),_HpnicfDot11APIfOutPayloadOctets2_Type())
hpnicfDot11APIfOutPayloadOctets2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutPayloadOctets2.setStatus(_A)
_HpnicfDot11APIfInDataOctets2_Type=Counter64
_HpnicfDot11APIfInDataOctets2_Object=MibTableColumn
hpnicfDot11APIfInDataOctets2=_HpnicfDot11APIfInDataOctets2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,25),_HpnicfDot11APIfInDataOctets2_Type())
hpnicfDot11APIfInDataOctets2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfInDataOctets2.setStatus(_A)
_HpnicfDot11APIfOutDataOctets2_Type=Counter64
_HpnicfDot11APIfOutDataOctets2_Object=MibTableColumn
hpnicfDot11APIfOutDataOctets2=_HpnicfDot11APIfOutDataOctets2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,26),_HpnicfDot11APIfOutDataOctets2_Type())
hpnicfDot11APIfOutDataOctets2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOutDataOctets2.setStatus(_A)
class _HpnicfDot11APIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3)))
_HpnicfDot11APIfAdminStatus_Type.__name__=_D
_HpnicfDot11APIfAdminStatus_Object=MibTableColumn
hpnicfDot11APIfAdminStatus=_HpnicfDot11APIfAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,27),_HpnicfDot11APIfAdminStatus_Type())
hpnicfDot11APIfAdminStatus.setMaxAccess(_Y)
if mibBuilder.loadTexts:hpnicfDot11APIfAdminStatus.setStatus(_A)
class _HpnicfDot11APIfOperStatusCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_y,4)))
_HpnicfDot11APIfOperStatusCM_Type.__name__=_D
_HpnicfDot11APIfOperStatusCM_Object=MibTableColumn
hpnicfDot11APIfOperStatusCM=_HpnicfDot11APIfOperStatusCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,23,1,28),_HpnicfDot11APIfOperStatusCM_Type())
hpnicfDot11APIfOperStatusCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfOperStatusCM.setStatus(_A)
_HpnicfDot11APUserSecAuthStatisTable_Object=MibTable
hpnicfDot11APUserSecAuthStatisTable=_HpnicfDot11APUserSecAuthStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,24))
if mibBuilder.loadTexts:hpnicfDot11APUserSecAuthStatisTable.setStatus(_A)
_HpnicfDot11APUserSecAuthStatisEntry_Object=MibTableRow
hpnicfDot11APUserSecAuthStatisEntry=_HpnicfDot11APUserSecAuthStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,24,1))
hpnicfDot11APUserSecAuthStatisEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:hpnicfDot11APUserSecAuthStatisEntry.setStatus(_A)
_HpnicfDot11APUserAuthCurNumber_Type=Integer32
_HpnicfDot11APUserAuthCurNumber_Object=MibTableColumn
hpnicfDot11APUserAuthCurNumber=_HpnicfDot11APUserAuthCurNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,24,1,1),_HpnicfDot11APUserAuthCurNumber_Type())
hpnicfDot11APUserAuthCurNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserAuthCurNumber.setStatus(_A)
_HpnicfDot11APUserConnFailCnt_Type=Counter32
_HpnicfDot11APUserConnFailCnt_Object=MibTableColumn
hpnicfDot11APUserConnFailCnt=_HpnicfDot11APUserConnFailCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,24,1,2),_HpnicfDot11APUserConnFailCnt_Type())
hpnicfDot11APUserConnFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserConnFailCnt.setStatus(_A)
_HpnicfDot11APUserAuthReqCnt_Type=Counter32
_HpnicfDot11APUserAuthReqCnt_Object=MibTableColumn
hpnicfDot11APUserAuthReqCnt=_HpnicfDot11APUserAuthReqCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,24,1,3),_HpnicfDot11APUserAuthReqCnt_Type())
hpnicfDot11APUserAuthReqCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserAuthReqCnt.setStatus(_A)
_HpnicfDot11APUserAuthSuccCnt_Type=Counter32
_HpnicfDot11APUserAuthSuccCnt_Object=MibTableColumn
hpnicfDot11APUserAuthSuccCnt=_HpnicfDot11APUserAuthSuccCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,24,1,4),_HpnicfDot11APUserAuthSuccCnt_Type())
hpnicfDot11APUserAuthSuccCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserAuthSuccCnt.setStatus(_A)
_HpnicfDot11APUserAuthFailCnt_Type=Counter32
_HpnicfDot11APUserAuthFailCnt_Object=MibTableColumn
hpnicfDot11APUserAuthFailCnt=_HpnicfDot11APUserAuthFailCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,24,1,5),_HpnicfDot11APUserAuthFailCnt_Type())
hpnicfDot11APUserAuthFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserAuthFailCnt.setStatus(_A)
_HpnicfDot11AllUserOnlineTime_Type=TimeTicks
_HpnicfDot11AllUserOnlineTime_Object=MibTableColumn
hpnicfDot11AllUserOnlineTime=_HpnicfDot11AllUserOnlineTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,24,1,6),_HpnicfDot11AllUserOnlineTime_Type())
hpnicfDot11AllUserOnlineTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AllUserOnlineTime.setStatus(_A)
_HpnicfDot11APUserInfoStatisTable_Object=MibTable
hpnicfDot11APUserInfoStatisTable=_HpnicfDot11APUserInfoStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,25))
if mibBuilder.loadTexts:hpnicfDot11APUserInfoStatisTable.setStatus(_A)
_HpnicfDot11APUserInfoStatisEntry_Object=MibTableRow
hpnicfDot11APUserInfoStatisEntry=_HpnicfDot11APUserInfoStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,25,1))
hpnicfDot11APUserInfoStatisEntry.setIndexNames((0,_C,_E),(0,_C,_AR))
if mibBuilder.loadTexts:hpnicfDot11APUserInfoStatisEntry.setStatus(_A)
_HpnicfDot11APUserMacAddr_Type=MacAddress
_HpnicfDot11APUserMacAddr_Object=MibTableColumn
hpnicfDot11APUserMacAddr=_HpnicfDot11APUserMacAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,25,1,1),_HpnicfDot11APUserMacAddr_Type())
hpnicfDot11APUserMacAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APUserMacAddr.setStatus(_A)
_HpnicfDot11APUserIpAddr_Type=IpAddress
_HpnicfDot11APUserIpAddr_Object=MibTableColumn
hpnicfDot11APUserIpAddr=_HpnicfDot11APUserIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,25,1,2),_HpnicfDot11APUserIpAddr_Type())
hpnicfDot11APUserIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserIpAddr.setStatus(_A)
_HpnicfDot11APUserLoginName_Type=OctetString
_HpnicfDot11APUserLoginName_Object=MibTableColumn
hpnicfDot11APUserLoginName=_HpnicfDot11APUserLoginName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,25,1,3),_HpnicfDot11APUserLoginName_Type())
hpnicfDot11APUserLoginName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserLoginName.setStatus(_A)
_HpnicfDot11APUserLoginTime_Type=OctetString
_HpnicfDot11APUserLoginTime_Object=MibTableColumn
hpnicfDot11APUserLoginTime=_HpnicfDot11APUserLoginTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,25,1,4),_HpnicfDot11APUserLoginTime_Type())
hpnicfDot11APUserLoginTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserLoginTime.setStatus(_A)
_HpnicfDot11APUserOnlineTime_Type=TimeTicks
_HpnicfDot11APUserOnlineTime_Object=MibTableColumn
hpnicfDot11APUserOnlineTime=_HpnicfDot11APUserOnlineTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,25,1,5),_HpnicfDot11APUserOnlineTime_Type())
hpnicfDot11APUserOnlineTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserOnlineTime.setStatus(_A)
_HpnicfDot11APUserLoginNameCM_Type=OctetString
_HpnicfDot11APUserLoginNameCM_Object=MibTableColumn
hpnicfDot11APUserLoginNameCM=_HpnicfDot11APUserLoginNameCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,25,1,6),_HpnicfDot11APUserLoginNameCM_Type())
hpnicfDot11APUserLoginNameCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserLoginNameCM.setStatus(_A)
class _HpnicfDot11APUserAuthTypeCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('authFree',1),(_AS,2),(_AT,3),('autoAuth',4)))
_HpnicfDot11APUserAuthTypeCM_Type.__name__=_D
_HpnicfDot11APUserAuthTypeCM_Object=MibTableColumn
hpnicfDot11APUserAuthTypeCM=_HpnicfDot11APUserAuthTypeCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,25,1,7),_HpnicfDot11APUserAuthTypeCM_Type())
hpnicfDot11APUserAuthTypeCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserAuthTypeCM.setStatus(_A)
_HpnicfDot11APUserTxPacketCntCM_Type=Counter32
_HpnicfDot11APUserTxPacketCntCM_Object=MibTableColumn
hpnicfDot11APUserTxPacketCntCM=_HpnicfDot11APUserTxPacketCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,25,1,8),_HpnicfDot11APUserTxPacketCntCM_Type())
hpnicfDot11APUserTxPacketCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserTxPacketCntCM.setStatus(_A)
_HpnicfDot11APUserTxBytesCM_Type=Counter64
_HpnicfDot11APUserTxBytesCM_Object=MibTableColumn
hpnicfDot11APUserTxBytesCM=_HpnicfDot11APUserTxBytesCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,25,1,9),_HpnicfDot11APUserTxBytesCM_Type())
hpnicfDot11APUserTxBytesCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserTxBytesCM.setStatus(_A)
_HpnicfDot11APUserRxPacketCntCM_Type=Counter32
_HpnicfDot11APUserRxPacketCntCM_Object=MibTableColumn
hpnicfDot11APUserRxPacketCntCM=_HpnicfDot11APUserRxPacketCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,25,1,10),_HpnicfDot11APUserRxPacketCntCM_Type())
hpnicfDot11APUserRxPacketCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserRxPacketCntCM.setStatus(_A)
_HpnicfDot11APUserRxBytesCM_Type=Counter64
_HpnicfDot11APUserRxBytesCM_Object=MibTableColumn
hpnicfDot11APUserRxBytesCM=_HpnicfDot11APUserRxBytesCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,25,1,11),_HpnicfDot11APUserRxBytesCM_Type())
hpnicfDot11APUserRxBytesCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserRxBytesCM.setStatus(_A)
_HpnicfDot11APReassocStatis2Table_Object=MibTable
hpnicfDot11APReassocStatis2Table=_HpnicfDot11APReassocStatis2Table_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,26))
if mibBuilder.loadTexts:hpnicfDot11APReassocStatis2Table.setStatus(_A)
_HpnicfDot11APReassocStatis2Entry_Object=MibTableRow
hpnicfDot11APReassocStatis2Entry=_HpnicfDot11APReassocStatis2Entry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,26,1))
hpnicfDot11APReassocStatis2Entry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:hpnicfDot11APReassocStatis2Entry.setStatus(_A)
_HpnicfDot11APReassocFailStatis2Cnt_Type=Counter32
_HpnicfDot11APReassocFailStatis2Cnt_Object=MibTableColumn
hpnicfDot11APReassocFailStatis2Cnt=_HpnicfDot11APReassocFailStatis2Cnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,26,1,1),_HpnicfDot11APReassocFailStatis2Cnt_Type())
hpnicfDot11APReassocFailStatis2Cnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APReassocFailStatis2Cnt.setStatus(_A)
_HpnicfDot11TrafficTable_Object=MibTable
hpnicfDot11TrafficTable=_HpnicfDot11TrafficTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,27))
if mibBuilder.loadTexts:hpnicfDot11TrafficTable.setStatus(_A)
_HpnicfDot11TrafficEntry_Object=MibTableRow
hpnicfDot11TrafficEntry=_HpnicfDot11TrafficEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,27,1))
hpnicfDot11TrafficEntry.setIndexNames((0,_C,_AU))
if mibBuilder.loadTexts:hpnicfDot11TrafficEntry.setStatus(_A)
_HpnicfDot11SSIDIndex_Type=OctetString
_HpnicfDot11SSIDIndex_Object=MibTableColumn
hpnicfDot11SSIDIndex=_HpnicfDot11SSIDIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,27,1,1),_HpnicfDot11SSIDIndex_Type())
hpnicfDot11SSIDIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11SSIDIndex.setStatus(_A)
_HpnicfDot11UpPacketNumber_Type=Counter64
_HpnicfDot11UpPacketNumber_Object=MibTableColumn
hpnicfDot11UpPacketNumber=_HpnicfDot11UpPacketNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,27,1,2),_HpnicfDot11UpPacketNumber_Type())
hpnicfDot11UpPacketNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11UpPacketNumber.setStatus(_A)
_HpnicfDot11UpByteNumber_Type=Counter64
_HpnicfDot11UpByteNumber_Object=MibTableColumn
hpnicfDot11UpByteNumber=_HpnicfDot11UpByteNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,27,1,3),_HpnicfDot11UpByteNumber_Type())
hpnicfDot11UpByteNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11UpByteNumber.setStatus(_A)
_HpnicfDot11DownPacketNumber_Type=Counter64
_HpnicfDot11DownPacketNumber_Object=MibTableColumn
hpnicfDot11DownPacketNumber=_HpnicfDot11DownPacketNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,27,1,4),_HpnicfDot11DownPacketNumber_Type())
hpnicfDot11DownPacketNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11DownPacketNumber.setStatus(_A)
_HpnicfDot11DownByteNumber_Type=Counter64
_HpnicfDot11DownByteNumber_Object=MibTableColumn
hpnicfDot11DownByteNumber=_HpnicfDot11DownByteNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,27,1,5),_HpnicfDot11DownByteNumber_Type())
hpnicfDot11DownByteNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11DownByteNumber.setStatus(_A)
_HpnicfDot11APEchoStatisTable_Object=MibTable
hpnicfDot11APEchoStatisTable=_HpnicfDot11APEchoStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,28))
if mibBuilder.loadTexts:hpnicfDot11APEchoStatisTable.setStatus(_A)
_HpnicfDot11APEchoInfoStatisEntry_Object=MibTableRow
hpnicfDot11APEchoInfoStatisEntry=_HpnicfDot11APEchoInfoStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,28,1))
hpnicfDot11APEchoInfoStatisEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:hpnicfDot11APEchoInfoStatisEntry.setStatus(_A)
_HpnicfDot11APEchoAvgDelay_Type=Integer32
_HpnicfDot11APEchoAvgDelay_Object=MibTableColumn
hpnicfDot11APEchoAvgDelay=_HpnicfDot11APEchoAvgDelay_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,28,1,1),_HpnicfDot11APEchoAvgDelay_Type())
hpnicfDot11APEchoAvgDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APEchoAvgDelay.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APEchoAvgDelay.setUnits('millisecond')
_HpnicfDot11APEchoRequestCnt_Type=Counter64
_HpnicfDot11APEchoRequestCnt_Object=MibTableColumn
hpnicfDot11APEchoRequestCnt=_HpnicfDot11APEchoRequestCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,28,1,2),_HpnicfDot11APEchoRequestCnt_Type())
hpnicfDot11APEchoRequestCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APEchoRequestCnt.setStatus(_A)
_HpnicfDot11APEchoRespLossCnt_Type=Counter64
_HpnicfDot11APEchoRespLossCnt_Object=MibTableColumn
hpnicfDot11APEchoRespLossCnt=_HpnicfDot11APEchoRespLossCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,28,1,3),_HpnicfDot11APEchoRespLossCnt_Type())
hpnicfDot11APEchoRespLossCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APEchoRespLossCnt.setStatus(_A)
_HpnicfDot11APUserSecAuthTypeStatisTable_Object=MibTable
hpnicfDot11APUserSecAuthTypeStatisTable=_HpnicfDot11APUserSecAuthTypeStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29))
if mibBuilder.loadTexts:hpnicfDot11APUserSecAuthTypeStatisTable.setStatus(_A)
_HpnicfDot11APUserSecAuthTypeStatisEntry_Object=MibTableRow
hpnicfDot11APUserSecAuthTypeStatisEntry=_HpnicfDot11APUserSecAuthTypeStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1))
hpnicfDot11APUserSecAuthTypeStatisEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:hpnicfDot11APUserSecAuthTypeStatisEntry.setStatus(_A)
_HpnicfDot11APPortalOnlineUserNum_Type=Integer32
_HpnicfDot11APPortalOnlineUserNum_Object=MibTableColumn
hpnicfDot11APPortalOnlineUserNum=_HpnicfDot11APPortalOnlineUserNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,1),_HpnicfDot11APPortalOnlineUserNum_Type())
hpnicfDot11APPortalOnlineUserNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APPortalOnlineUserNum.setStatus(_A)
_HpnicfDot11APAuthFreeOnlineUserNum_Type=Integer32
_HpnicfDot11APAuthFreeOnlineUserNum_Object=MibTableColumn
hpnicfDot11APAuthFreeOnlineUserNum=_HpnicfDot11APAuthFreeOnlineUserNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,2),_HpnicfDot11APAuthFreeOnlineUserNum_Type())
hpnicfDot11APAuthFreeOnlineUserNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAuthFreeOnlineUserNum.setStatus(_A)
_HpnicfDot11APAssocAuthOnlineUserNum_Type=Integer32
_HpnicfDot11APAssocAuthOnlineUserNum_Object=MibTableColumn
hpnicfDot11APAssocAuthOnlineUserNum=_HpnicfDot11APAssocAuthOnlineUserNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,3),_HpnicfDot11APAssocAuthOnlineUserNum_Type())
hpnicfDot11APAssocAuthOnlineUserNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAssocAuthOnlineUserNum.setStatus(_A)
_HpnicfDot11APMacAuthOnlineUserNum_Type=Integer32
_HpnicfDot11APMacAuthOnlineUserNum_Object=MibTableColumn
hpnicfDot11APMacAuthOnlineUserNum=_HpnicfDot11APMacAuthOnlineUserNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,4),_HpnicfDot11APMacAuthOnlineUserNum_Type())
hpnicfDot11APMacAuthOnlineUserNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APMacAuthOnlineUserNum.setStatus(_A)
_HpnicfDot11APAllPortalUserOnlineTime_Type=TimeTicks
_HpnicfDot11APAllPortalUserOnlineTime_Object=MibTableColumn
hpnicfDot11APAllPortalUserOnlineTime=_HpnicfDot11APAllPortalUserOnlineTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,5),_HpnicfDot11APAllPortalUserOnlineTime_Type())
hpnicfDot11APAllPortalUserOnlineTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAllPortalUserOnlineTime.setStatus(_A)
_HpnicfDot11APAllAuthFreeUserOnlineTime_Type=TimeTicks
_HpnicfDot11APAllAuthFreeUserOnlineTime_Object=MibTableColumn
hpnicfDot11APAllAuthFreeUserOnlineTime=_HpnicfDot11APAllAuthFreeUserOnlineTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,6),_HpnicfDot11APAllAuthFreeUserOnlineTime_Type())
hpnicfDot11APAllAuthFreeUserOnlineTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAllAuthFreeUserOnlineTime.setStatus(_A)
_HpnicfDot11APAllAssocAuthUserOnlineTime_Type=TimeTicks
_HpnicfDot11APAllAssocAuthUserOnlineTime_Object=MibTableColumn
hpnicfDot11APAllAssocAuthUserOnlineTime=_HpnicfDot11APAllAssocAuthUserOnlineTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,7),_HpnicfDot11APAllAssocAuthUserOnlineTime_Type())
hpnicfDot11APAllAssocAuthUserOnlineTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAllAssocAuthUserOnlineTime.setStatus(_A)
_HpnicfDot11APAllMacAuthUserOnlineTime_Type=TimeTicks
_HpnicfDot11APAllMacAuthUserOnlineTime_Object=MibTableColumn
hpnicfDot11APAllMacAuthUserOnlineTime=_HpnicfDot11APAllMacAuthUserOnlineTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,8),_HpnicfDot11APAllMacAuthUserOnlineTime_Type())
hpnicfDot11APAllMacAuthUserOnlineTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAllMacAuthUserOnlineTime.setStatus(_A)
_HpnicfDot11APPortalUserLostCnntCnt_Type=Counter32
_HpnicfDot11APPortalUserLostCnntCnt_Object=MibTableColumn
hpnicfDot11APPortalUserLostCnntCnt=_HpnicfDot11APPortalUserLostCnntCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,9),_HpnicfDot11APPortalUserLostCnntCnt_Type())
hpnicfDot11APPortalUserLostCnntCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APPortalUserLostCnntCnt.setStatus(_A)
_HpnicfDot11APAuthFreeUserLostCnntCnt_Type=Counter32
_HpnicfDot11APAuthFreeUserLostCnntCnt_Object=MibTableColumn
hpnicfDot11APAuthFreeUserLostCnntCnt=_HpnicfDot11APAuthFreeUserLostCnntCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,10),_HpnicfDot11APAuthFreeUserLostCnntCnt_Type())
hpnicfDot11APAuthFreeUserLostCnntCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAuthFreeUserLostCnntCnt.setStatus(_A)
_HpnicfDot11APAssocAuthUserLostCnntCnt_Type=Counter32
_HpnicfDot11APAssocAuthUserLostCnntCnt_Object=MibTableColumn
hpnicfDot11APAssocAuthUserLostCnntCnt=_HpnicfDot11APAssocAuthUserLostCnntCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,11),_HpnicfDot11APAssocAuthUserLostCnntCnt_Type())
hpnicfDot11APAssocAuthUserLostCnntCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAssocAuthUserLostCnntCnt.setStatus(_A)
_HpnicfDot11APMacAuthUserLostCnntCnt_Type=Counter32
_HpnicfDot11APMacAuthUserLostCnntCnt_Object=MibTableColumn
hpnicfDot11APMacAuthUserLostCnntCnt=_HpnicfDot11APMacAuthUserLostCnntCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,12),_HpnicfDot11APMacAuthUserLostCnntCnt_Type())
hpnicfDot11APMacAuthUserLostCnntCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APMacAuthUserLostCnntCnt.setStatus(_A)
_HpnicfDot11APPortalAuthReqCnt_Type=Counter32
_HpnicfDot11APPortalAuthReqCnt_Object=MibTableColumn
hpnicfDot11APPortalAuthReqCnt=_HpnicfDot11APPortalAuthReqCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,13),_HpnicfDot11APPortalAuthReqCnt_Type())
hpnicfDot11APPortalAuthReqCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APPortalAuthReqCnt.setStatus(_A)
_HpnicfDot11APAssocAuthReqCnt_Type=Counter32
_HpnicfDot11APAssocAuthReqCnt_Object=MibTableColumn
hpnicfDot11APAssocAuthReqCnt=_HpnicfDot11APAssocAuthReqCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,14),_HpnicfDot11APAssocAuthReqCnt_Type())
hpnicfDot11APAssocAuthReqCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAssocAuthReqCnt.setStatus(_A)
_HpnicfDot11APMacAuthReqCnt_Type=Counter32
_HpnicfDot11APMacAuthReqCnt_Object=MibTableColumn
hpnicfDot11APMacAuthReqCnt=_HpnicfDot11APMacAuthReqCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,15),_HpnicfDot11APMacAuthReqCnt_Type())
hpnicfDot11APMacAuthReqCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APMacAuthReqCnt.setStatus(_A)
_HpnicfDot11APPortalAuthSucCnt_Type=Counter32
_HpnicfDot11APPortalAuthSucCnt_Object=MibTableColumn
hpnicfDot11APPortalAuthSucCnt=_HpnicfDot11APPortalAuthSucCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,16),_HpnicfDot11APPortalAuthSucCnt_Type())
hpnicfDot11APPortalAuthSucCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APPortalAuthSucCnt.setStatus(_A)
_HpnicfDot11APAssocAuthSucCnt_Type=Counter32
_HpnicfDot11APAssocAuthSucCnt_Object=MibTableColumn
hpnicfDot11APAssocAuthSucCnt=_HpnicfDot11APAssocAuthSucCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,17),_HpnicfDot11APAssocAuthSucCnt_Type())
hpnicfDot11APAssocAuthSucCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAssocAuthSucCnt.setStatus(_A)
_HpnicfDot11APMacAuthSucCnt_Type=Counter32
_HpnicfDot11APMacAuthSucCnt_Object=MibTableColumn
hpnicfDot11APMacAuthSucCnt=_HpnicfDot11APMacAuthSucCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,18),_HpnicfDot11APMacAuthSucCnt_Type())
hpnicfDot11APMacAuthSucCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APMacAuthSucCnt.setStatus(_A)
_HpnicfDot11APPortalAuthReqFailCnt_Type=Counter32
_HpnicfDot11APPortalAuthReqFailCnt_Object=MibTableColumn
hpnicfDot11APPortalAuthReqFailCnt=_HpnicfDot11APPortalAuthReqFailCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,19),_HpnicfDot11APPortalAuthReqFailCnt_Type())
hpnicfDot11APPortalAuthReqFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APPortalAuthReqFailCnt.setStatus(_A)
_HpnicfDot11APAssocAuthReqFailCnt_Type=Counter32
_HpnicfDot11APAssocAuthReqFailCnt_Object=MibTableColumn
hpnicfDot11APAssocAuthReqFailCnt=_HpnicfDot11APAssocAuthReqFailCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,20),_HpnicfDot11APAssocAuthReqFailCnt_Type())
hpnicfDot11APAssocAuthReqFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAssocAuthReqFailCnt.setStatus(_A)
_HpnicfDot11APMacAuthReqFailCnt_Type=Counter32
_HpnicfDot11APMacAuthReqFailCnt_Object=MibTableColumn
hpnicfDot11APMacAuthReqFailCnt=_HpnicfDot11APMacAuthReqFailCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,21),_HpnicfDot11APMacAuthReqFailCnt_Type())
hpnicfDot11APMacAuthReqFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APMacAuthReqFailCnt.setStatus(_A)
_HpnicfDot11APAutoAuthOnlineUserNumCM_Type=Integer32
_HpnicfDot11APAutoAuthOnlineUserNumCM_Object=MibTableColumn
hpnicfDot11APAutoAuthOnlineUserNumCM=_HpnicfDot11APAutoAuthOnlineUserNumCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,22),_HpnicfDot11APAutoAuthOnlineUserNumCM_Type())
hpnicfDot11APAutoAuthOnlineUserNumCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAutoAuthOnlineUserNumCM.setStatus(_A)
_HpnicfDot11APAllAutoAuthUserOnlineTimeCM_Type=TimeTicks
_HpnicfDot11APAllAutoAuthUserOnlineTimeCM_Object=MibTableColumn
hpnicfDot11APAllAutoAuthUserOnlineTimeCM=_HpnicfDot11APAllAutoAuthUserOnlineTimeCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,23),_HpnicfDot11APAllAutoAuthUserOnlineTimeCM_Type())
hpnicfDot11APAllAutoAuthUserOnlineTimeCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAllAutoAuthUserOnlineTimeCM.setStatus(_A)
_HpnicfDot11APAutoAuthUserLostCnntCntCM_Type=Counter32
_HpnicfDot11APAutoAuthUserLostCnntCntCM_Object=MibTableColumn
hpnicfDot11APAutoAuthUserLostCnntCntCM=_HpnicfDot11APAutoAuthUserLostCnntCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,24),_HpnicfDot11APAutoAuthUserLostCnntCntCM_Type())
hpnicfDot11APAutoAuthUserLostCnntCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAutoAuthUserLostCnntCntCM.setStatus(_A)
_HpnicfDot11APAutoAuthReqCntCM_Type=Counter32
_HpnicfDot11APAutoAuthReqCntCM_Object=MibTableColumn
hpnicfDot11APAutoAuthReqCntCM=_HpnicfDot11APAutoAuthReqCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,25),_HpnicfDot11APAutoAuthReqCntCM_Type())
hpnicfDot11APAutoAuthReqCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAutoAuthReqCntCM.setStatus(_A)
_HpnicfDot11APAutoAuthSucCntCM_Type=Counter32
_HpnicfDot11APAutoAuthSucCntCM_Object=MibTableColumn
hpnicfDot11APAutoAuthSucCntCM=_HpnicfDot11APAutoAuthSucCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,26),_HpnicfDot11APAutoAuthSucCntCM_Type())
hpnicfDot11APAutoAuthSucCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAutoAuthSucCntCM.setStatus(_A)
_HpnicfDot11APAutoAuthReqFailCntCM_Type=Counter32
_HpnicfDot11APAutoAuthReqFailCntCM_Object=MibTableColumn
hpnicfDot11APAutoAuthReqFailCntCM=_HpnicfDot11APAutoAuthReqFailCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,29,1,27),_HpnicfDot11APAutoAuthReqFailCntCM_Type())
hpnicfDot11APAutoAuthReqFailCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APAutoAuthReqFailCntCM.setStatus(_A)
_HpnicfDot11RadioRxStatis64Table_Object=MibTable
hpnicfDot11RadioRxStatis64Table=_HpnicfDot11RadioRxStatis64Table_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30))
if mibBuilder.loadTexts:hpnicfDot11RadioRxStatis64Table.setStatus(_A)
_HpnicfDot11RadioRxStatis64Entry_Object=MibTableRow
hpnicfDot11RadioRxStatis64Entry=_HpnicfDot11RadioRxStatis64Entry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1))
hpnicfDot11RadioRxStatis64Entry.setIndexNames((0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:hpnicfDot11RadioRxStatis64Entry.setStatus(_A)
_HpnicfDot11Rx64FrameDupCnt_Type=Counter64
_HpnicfDot11Rx64FrameDupCnt_Object=MibTableColumn
hpnicfDot11Rx64FrameDupCnt=_HpnicfDot11Rx64FrameDupCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,1),_HpnicfDot11Rx64FrameDupCnt_Type())
hpnicfDot11Rx64FrameDupCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64FrameDupCnt.setStatus(_A)
_HpnicfDot11Rx64FrameCnt_Type=Counter64
_HpnicfDot11Rx64FrameCnt_Object=MibTableColumn
hpnicfDot11Rx64FrameCnt=_HpnicfDot11Rx64FrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,2),_HpnicfDot11Rx64FrameCnt_Type())
hpnicfDot11Rx64FrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64FrameCnt.setStatus(_A)
_HpnicfDot11Rx64UcastFrameCnt_Type=Counter64
_HpnicfDot11Rx64UcastFrameCnt_Object=MibTableColumn
hpnicfDot11Rx64UcastFrameCnt=_HpnicfDot11Rx64UcastFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,3),_HpnicfDot11Rx64UcastFrameCnt_Type())
hpnicfDot11Rx64UcastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64UcastFrameCnt.setStatus(_A)
_HpnicfDot11Rx64BcastFrameCnt_Type=Counter64
_HpnicfDot11Rx64BcastFrameCnt_Object=MibTableColumn
hpnicfDot11Rx64BcastFrameCnt=_HpnicfDot11Rx64BcastFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,4),_HpnicfDot11Rx64BcastFrameCnt_Type())
hpnicfDot11Rx64BcastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64BcastFrameCnt.setStatus(_A)
_HpnicfDot11Rx64McastFrameCnt_Type=Counter64
_HpnicfDot11Rx64McastFrameCnt_Object=MibTableColumn
hpnicfDot11Rx64McastFrameCnt=_HpnicfDot11Rx64McastFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,5),_HpnicfDot11Rx64McastFrameCnt_Type())
hpnicfDot11Rx64McastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64McastFrameCnt.setStatus(_A)
_HpnicfDot11Rx64DiscardFrameCnt_Type=Counter64
_HpnicfDot11Rx64DiscardFrameCnt_Object=MibTableColumn
hpnicfDot11Rx64DiscardFrameCnt=_HpnicfDot11Rx64DiscardFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,6),_HpnicfDot11Rx64DiscardFrameCnt_Type())
hpnicfDot11Rx64DiscardFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64DiscardFrameCnt.setStatus(_A)
_HpnicfDot11Rx64FragCnt_Type=Counter64
_HpnicfDot11Rx64FragCnt_Object=MibTableColumn
hpnicfDot11Rx64FragCnt=_HpnicfDot11Rx64FragCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,7),_HpnicfDot11Rx64FragCnt_Type())
hpnicfDot11Rx64FragCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64FragCnt.setStatus(_A)
_HpnicfDot11Rx64FcsErrCnt_Type=Counter64
_HpnicfDot11Rx64FcsErrCnt_Object=MibTableColumn
hpnicfDot11Rx64FcsErrCnt=_HpnicfDot11Rx64FcsErrCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,8),_HpnicfDot11Rx64FcsErrCnt_Type())
hpnicfDot11Rx64FcsErrCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64FcsErrCnt.setStatus(_A)
_HpnicfDot11Rx64FrameBytes_Type=Counter64
_HpnicfDot11Rx64FrameBytes_Object=MibTableColumn
hpnicfDot11Rx64FrameBytes=_HpnicfDot11Rx64FrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,9),_HpnicfDot11Rx64FrameBytes_Type())
hpnicfDot11Rx64FrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64FrameBytes.setStatus(_A)
_HpnicfDot11Rx64UcastFrameBytes_Type=Counter64
_HpnicfDot11Rx64UcastFrameBytes_Object=MibTableColumn
hpnicfDot11Rx64UcastFrameBytes=_HpnicfDot11Rx64UcastFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,10),_HpnicfDot11Rx64UcastFrameBytes_Type())
hpnicfDot11Rx64UcastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64UcastFrameBytes.setStatus(_A)
_HpnicfDot11Rx64BcastFrameBytes_Type=Counter64
_HpnicfDot11Rx64BcastFrameBytes_Object=MibTableColumn
hpnicfDot11Rx64BcastFrameBytes=_HpnicfDot11Rx64BcastFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,11),_HpnicfDot11Rx64BcastFrameBytes_Type())
hpnicfDot11Rx64BcastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64BcastFrameBytes.setStatus(_A)
_HpnicfDot11Rx64McastFrameBytes_Type=Counter64
_HpnicfDot11Rx64McastFrameBytes_Object=MibTableColumn
hpnicfDot11Rx64McastFrameBytes=_HpnicfDot11Rx64McastFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,12),_HpnicfDot11Rx64McastFrameBytes_Type())
hpnicfDot11Rx64McastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64McastFrameBytes.setStatus(_A)
_HpnicfDot11Rx64DiscardFrameBytes_Type=Counter64
_HpnicfDot11Rx64DiscardFrameBytes_Object=MibTableColumn
hpnicfDot11Rx64DiscardFrameBytes=_HpnicfDot11Rx64DiscardFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,13),_HpnicfDot11Rx64DiscardFrameBytes_Type())
hpnicfDot11Rx64DiscardFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64DiscardFrameBytes.setStatus(_A)
_HpnicfDot11Rx64MgmtFrameCnt_Type=Counter64
_HpnicfDot11Rx64MgmtFrameCnt_Object=MibTableColumn
hpnicfDot11Rx64MgmtFrameCnt=_HpnicfDot11Rx64MgmtFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,14),_HpnicfDot11Rx64MgmtFrameCnt_Type())
hpnicfDot11Rx64MgmtFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64MgmtFrameCnt.setStatus(_A)
_HpnicfDot11Rx64CtrlFrameCnt_Type=Counter64
_HpnicfDot11Rx64CtrlFrameCnt_Object=MibTableColumn
hpnicfDot11Rx64CtrlFrameCnt=_HpnicfDot11Rx64CtrlFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,15),_HpnicfDot11Rx64CtrlFrameCnt_Type())
hpnicfDot11Rx64CtrlFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64CtrlFrameCnt.setStatus(_A)
_HpnicfDot11Rx64DataFrameCnt_Type=Counter64
_HpnicfDot11Rx64DataFrameCnt_Object=MibTableColumn
hpnicfDot11Rx64DataFrameCnt=_HpnicfDot11Rx64DataFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,16),_HpnicfDot11Rx64DataFrameCnt_Type())
hpnicfDot11Rx64DataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64DataFrameCnt.setStatus(_A)
_HpnicfDot11Rx64DecryptErrorCnt_Type=Counter64
_HpnicfDot11Rx64DecryptErrorCnt_Object=MibTableColumn
hpnicfDot11Rx64DecryptErrorCnt=_HpnicfDot11Rx64DecryptErrorCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,17),_HpnicfDot11Rx64DecryptErrorCnt_Type())
hpnicfDot11Rx64DecryptErrorCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64DecryptErrorCnt.setStatus(_A)
_HpnicfDot11Rx64AuthenFrameCnt_Type=Counter64
_HpnicfDot11Rx64AuthenFrameCnt_Object=MibTableColumn
hpnicfDot11Rx64AuthenFrameCnt=_HpnicfDot11Rx64AuthenFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,18),_HpnicfDot11Rx64AuthenFrameCnt_Type())
hpnicfDot11Rx64AuthenFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64AuthenFrameCnt.setStatus(_A)
_HpnicfDot11Rx64AssociateFrameCnt_Type=Counter64
_HpnicfDot11Rx64AssociateFrameCnt_Object=MibTableColumn
hpnicfDot11Rx64AssociateFrameCnt=_HpnicfDot11Rx64AssociateFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,19),_HpnicfDot11Rx64AssociateFrameCnt_Type())
hpnicfDot11Rx64AssociateFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64AssociateFrameCnt.setStatus(_A)
_HpnicfDot11Rx64PhyErrorCnt_Type=Counter64
_HpnicfDot11Rx64PhyErrorCnt_Object=MibTableColumn
hpnicfDot11Rx64PhyErrorCnt=_HpnicfDot11Rx64PhyErrorCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,20),_HpnicfDot11Rx64PhyErrorCnt_Type())
hpnicfDot11Rx64PhyErrorCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64PhyErrorCnt.setStatus(_A)
_HpnicfDot11Rx64MICErrorCnt_Type=Counter64
_HpnicfDot11Rx64MICErrorCnt_Object=MibTableColumn
hpnicfDot11Rx64MICErrorCnt=_HpnicfDot11Rx64MICErrorCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,21),_HpnicfDot11Rx64MICErrorCnt_Type())
hpnicfDot11Rx64MICErrorCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64MICErrorCnt.setStatus(_A)
_HpnicfDot11Rx64DataFrameBytes_Type=Counter64
_HpnicfDot11Rx64DataFrameBytes_Object=MibTableColumn
hpnicfDot11Rx64DataFrameBytes=_HpnicfDot11Rx64DataFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,22),_HpnicfDot11Rx64DataFrameBytes_Type())
hpnicfDot11Rx64DataFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64DataFrameBytes.setStatus(_A)
_HpnicfDot11Rx64PayloadBytes_Type=Counter64
_HpnicfDot11Rx64PayloadBytes_Object=MibTableColumn
hpnicfDot11Rx64PayloadBytes=_HpnicfDot11Rx64PayloadBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,23),_HpnicfDot11Rx64PayloadBytes_Type())
hpnicfDot11Rx64PayloadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64PayloadBytes.setStatus(_A)
_HpnicfDot11Rx64DataFrameBytesCM_Type=Counter64
_HpnicfDot11Rx64DataFrameBytesCM_Object=MibTableColumn
hpnicfDot11Rx64DataFrameBytesCM=_HpnicfDot11Rx64DataFrameBytesCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,30,1,24),_HpnicfDot11Rx64DataFrameBytesCM_Type())
hpnicfDot11Rx64DataFrameBytesCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Rx64DataFrameBytesCM.setStatus(_A)
_HpnicfDot11RadioTxStatis64Table_Object=MibTable
hpnicfDot11RadioTxStatis64Table=_HpnicfDot11RadioTxStatis64Table_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31))
if mibBuilder.loadTexts:hpnicfDot11RadioTxStatis64Table.setStatus(_A)
_HpnicfDot11RadioTxStatis64Entry_Object=MibTableRow
hpnicfDot11RadioTxStatis64Entry=_HpnicfDot11RadioTxStatis64Entry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1))
hpnicfDot11RadioTxStatis64Entry.setIndexNames((0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:hpnicfDot11RadioTxStatis64Entry.setStatus(_A)
_HpnicfDot11Tx64FragCnt_Type=Counter64
_HpnicfDot11Tx64FragCnt_Object=MibTableColumn
hpnicfDot11Tx64FragCnt=_HpnicfDot11Tx64FragCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,1),_HpnicfDot11Tx64FragCnt_Type())
hpnicfDot11Tx64FragCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64FragCnt.setStatus(_A)
_HpnicfDot11Tx64FailedCnt_Type=Counter64
_HpnicfDot11Tx64FailedCnt_Object=MibTableColumn
hpnicfDot11Tx64FailedCnt=_HpnicfDot11Tx64FailedCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,2),_HpnicfDot11Tx64FailedCnt_Type())
hpnicfDot11Tx64FailedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64FailedCnt.setStatus(_A)
_HpnicfDot11Tx64RetryCnt_Type=Counter64
_HpnicfDot11Tx64RetryCnt_Object=MibTableColumn
hpnicfDot11Tx64RetryCnt=_HpnicfDot11Tx64RetryCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,3),_HpnicfDot11Tx64RetryCnt_Type())
hpnicfDot11Tx64RetryCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64RetryCnt.setStatus(_A)
_HpnicfDot11Tx64MultiRetryCnt_Type=Counter64
_HpnicfDot11Tx64MultiRetryCnt_Object=MibTableColumn
hpnicfDot11Tx64MultiRetryCnt=_HpnicfDot11Tx64MultiRetryCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,4),_HpnicfDot11Tx64MultiRetryCnt_Type())
hpnicfDot11Tx64MultiRetryCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64MultiRetryCnt.setStatus(_A)
_HpnicfDot11Tx64RtsSuccessCnt_Type=Counter64
_HpnicfDot11Tx64RtsSuccessCnt_Object=MibTableColumn
hpnicfDot11Tx64RtsSuccessCnt=_HpnicfDot11Tx64RtsSuccessCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,5),_HpnicfDot11Tx64RtsSuccessCnt_Type())
hpnicfDot11Tx64RtsSuccessCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64RtsSuccessCnt.setStatus(_A)
_HpnicfDot11Tx64RtsFailCnt_Type=Counter64
_HpnicfDot11Tx64RtsFailCnt_Object=MibTableColumn
hpnicfDot11Tx64RtsFailCnt=_HpnicfDot11Tx64RtsFailCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,6),_HpnicfDot11Tx64RtsFailCnt_Type())
hpnicfDot11Tx64RtsFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64RtsFailCnt.setStatus(_A)
_HpnicfDot11Tx64AckFailCnt_Type=Counter64
_HpnicfDot11Tx64AckFailCnt_Object=MibTableColumn
hpnicfDot11Tx64AckFailCnt=_HpnicfDot11Tx64AckFailCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,7),_HpnicfDot11Tx64AckFailCnt_Type())
hpnicfDot11Tx64AckFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64AckFailCnt.setStatus(_A)
_HpnicfDot11Tx64FrameCnt_Type=Counter64
_HpnicfDot11Tx64FrameCnt_Object=MibTableColumn
hpnicfDot11Tx64FrameCnt=_HpnicfDot11Tx64FrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,8),_HpnicfDot11Tx64FrameCnt_Type())
hpnicfDot11Tx64FrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64FrameCnt.setStatus(_A)
_HpnicfDot11Tx64UcastFrameCnt_Type=Counter64
_HpnicfDot11Tx64UcastFrameCnt_Object=MibTableColumn
hpnicfDot11Tx64UcastFrameCnt=_HpnicfDot11Tx64UcastFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,9),_HpnicfDot11Tx64UcastFrameCnt_Type())
hpnicfDot11Tx64UcastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64UcastFrameCnt.setStatus(_A)
_HpnicfDot11Tx64BcastFrameCnt_Type=Counter64
_HpnicfDot11Tx64BcastFrameCnt_Object=MibTableColumn
hpnicfDot11Tx64BcastFrameCnt=_HpnicfDot11Tx64BcastFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,10),_HpnicfDot11Tx64BcastFrameCnt_Type())
hpnicfDot11Tx64BcastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64BcastFrameCnt.setStatus(_A)
_HpnicfDot11Tx64McastFrameCnt_Type=Counter64
_HpnicfDot11Tx64McastFrameCnt_Object=MibTableColumn
hpnicfDot11Tx64McastFrameCnt=_HpnicfDot11Tx64McastFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,11),_HpnicfDot11Tx64McastFrameCnt_Type())
hpnicfDot11Tx64McastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64McastFrameCnt.setStatus(_A)
_HpnicfDot11Tx64DiscardFrameCnt_Type=Counter64
_HpnicfDot11Tx64DiscardFrameCnt_Object=MibTableColumn
hpnicfDot11Tx64DiscardFrameCnt=_HpnicfDot11Tx64DiscardFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,12),_HpnicfDot11Tx64DiscardFrameCnt_Type())
hpnicfDot11Tx64DiscardFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64DiscardFrameCnt.setStatus(_A)
_HpnicfDot11Tx64FrameBytes_Type=Counter64
_HpnicfDot11Tx64FrameBytes_Object=MibTableColumn
hpnicfDot11Tx64FrameBytes=_HpnicfDot11Tx64FrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,13),_HpnicfDot11Tx64FrameBytes_Type())
hpnicfDot11Tx64FrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64FrameBytes.setStatus(_A)
_HpnicfDot11Tx64UcastFrameBytes_Type=Counter64
_HpnicfDot11Tx64UcastFrameBytes_Object=MibTableColumn
hpnicfDot11Tx64UcastFrameBytes=_HpnicfDot11Tx64UcastFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,14),_HpnicfDot11Tx64UcastFrameBytes_Type())
hpnicfDot11Tx64UcastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64UcastFrameBytes.setStatus(_A)
_HpnicfDot11Tx64BcastFrameBytes_Type=Counter64
_HpnicfDot11Tx64BcastFrameBytes_Object=MibTableColumn
hpnicfDot11Tx64BcastFrameBytes=_HpnicfDot11Tx64BcastFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,15),_HpnicfDot11Tx64BcastFrameBytes_Type())
hpnicfDot11Tx64BcastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64BcastFrameBytes.setStatus(_A)
_HpnicfDot11Tx64McastFrameBytes_Type=Counter64
_HpnicfDot11Tx64McastFrameBytes_Object=MibTableColumn
hpnicfDot11Tx64McastFrameBytes=_HpnicfDot11Tx64McastFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,16),_HpnicfDot11Tx64McastFrameBytes_Type())
hpnicfDot11Tx64McastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64McastFrameBytes.setStatus(_A)
_HpnicfDot11Tx64DiscardFrameBytes_Type=Counter64
_HpnicfDot11Tx64DiscardFrameBytes_Object=MibTableColumn
hpnicfDot11Tx64DiscardFrameBytes=_HpnicfDot11Tx64DiscardFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,17),_HpnicfDot11Tx64DiscardFrameBytes_Type())
hpnicfDot11Tx64DiscardFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64DiscardFrameBytes.setStatus(_A)
_HpnicfDot11Tx64AuthenFrameCnt_Type=Counter64
_HpnicfDot11Tx64AuthenFrameCnt_Object=MibTableColumn
hpnicfDot11Tx64AuthenFrameCnt=_HpnicfDot11Tx64AuthenFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,18),_HpnicfDot11Tx64AuthenFrameCnt_Type())
hpnicfDot11Tx64AuthenFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64AuthenFrameCnt.setStatus(_A)
_HpnicfDot11Tx64AssociateFrameCnt_Type=Counter64
_HpnicfDot11Tx64AssociateFrameCnt_Object=MibTableColumn
hpnicfDot11Tx64AssociateFrameCnt=_HpnicfDot11Tx64AssociateFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,19),_HpnicfDot11Tx64AssociateFrameCnt_Type())
hpnicfDot11Tx64AssociateFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64AssociateFrameCnt.setStatus(_A)
_HpnicfDot11Tx64DataFrameCnt_Type=Counter64
_HpnicfDot11Tx64DataFrameCnt_Object=MibTableColumn
hpnicfDot11Tx64DataFrameCnt=_HpnicfDot11Tx64DataFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,20),_HpnicfDot11Tx64DataFrameCnt_Type())
hpnicfDot11Tx64DataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64DataFrameCnt.setStatus(_A)
_HpnicfDot11Tx64DataFrameBytes_Type=Counter64
_HpnicfDot11Tx64DataFrameBytes_Object=MibTableColumn
hpnicfDot11Tx64DataFrameBytes=_HpnicfDot11Tx64DataFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,21),_HpnicfDot11Tx64DataFrameBytes_Type())
hpnicfDot11Tx64DataFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64DataFrameBytes.setStatus(_A)
_HpnicfDot11Tx64MSDUCnt_Type=Counter64
_HpnicfDot11Tx64MSDUCnt_Object=MibTableColumn
hpnicfDot11Tx64MSDUCnt=_HpnicfDot11Tx64MSDUCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,22),_HpnicfDot11Tx64MSDUCnt_Type())
hpnicfDot11Tx64MSDUCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64MSDUCnt.setStatus(_A)
_HpnicfDot11Tx64DiscardMSDUCnt_Type=Counter64
_HpnicfDot11Tx64DiscardMSDUCnt_Object=MibTableColumn
hpnicfDot11Tx64DiscardMSDUCnt=_HpnicfDot11Tx64DiscardMSDUCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,23),_HpnicfDot11Tx64DiscardMSDUCnt_Type())
hpnicfDot11Tx64DiscardMSDUCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64DiscardMSDUCnt.setStatus(_A)
_HpnicfDot11Tx64RetryMSDUCnt_Type=Counter64
_HpnicfDot11Tx64RetryMSDUCnt_Object=MibTableColumn
hpnicfDot11Tx64RetryMSDUCnt=_HpnicfDot11Tx64RetryMSDUCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,24),_HpnicfDot11Tx64RetryMSDUCnt_Type())
hpnicfDot11Tx64RetryMSDUCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64RetryMSDUCnt.setStatus(_A)
_HpnicfDot11Tx64PayloadBytes_Type=Counter64
_HpnicfDot11Tx64PayloadBytes_Object=MibTableColumn
hpnicfDot11Tx64PayloadBytes=_HpnicfDot11Tx64PayloadBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,25),_HpnicfDot11Tx64PayloadBytes_Type())
hpnicfDot11Tx64PayloadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64PayloadBytes.setStatus(_A)
_HpnicfDot11Tx64MgtFrameCnt_Type=Counter64
_HpnicfDot11Tx64MgtFrameCnt_Object=MibTableColumn
hpnicfDot11Tx64MgtFrameCnt=_HpnicfDot11Tx64MgtFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,26),_HpnicfDot11Tx64MgtFrameCnt_Type())
hpnicfDot11Tx64MgtFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64MgtFrameCnt.setStatus(_A)
_HpnicfDot11Tx64CtrlFrameCnt_Type=Counter64
_HpnicfDot11Tx64CtrlFrameCnt_Object=MibTableColumn
hpnicfDot11Tx64CtrlFrameCnt=_HpnicfDot11Tx64CtrlFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,27),_HpnicfDot11Tx64CtrlFrameCnt_Type())
hpnicfDot11Tx64CtrlFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64CtrlFrameCnt.setStatus(_A)
_HpnicfDot11Tx64MACErrCnt_Type=Counter64
_HpnicfDot11Tx64MACErrCnt_Object=MibTableColumn
hpnicfDot11Tx64MACErrCnt=_HpnicfDot11Tx64MACErrCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,28),_HpnicfDot11Tx64MACErrCnt_Type())
hpnicfDot11Tx64MACErrCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64MACErrCnt.setStatus(_A)
_HpnicfDot11Tx64ErrFrameCnt_Type=Counter64
_HpnicfDot11Tx64ErrFrameCnt_Object=MibTableColumn
hpnicfDot11Tx64ErrFrameCnt=_HpnicfDot11Tx64ErrFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,31,1,29),_HpnicfDot11Tx64ErrFrameCnt_Type())
hpnicfDot11Tx64ErrFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11Tx64ErrFrameCnt.setStatus(_A)
_HpnicfDot11BSSRxStatis64Table_Object=MibTable
hpnicfDot11BSSRxStatis64Table=_HpnicfDot11BSSRxStatis64Table_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,32))
if mibBuilder.loadTexts:hpnicfDot11BSSRxStatis64Table.setStatus(_A)
_HpnicfDot11BSSRxStatis64Entry_Object=MibTableRow
hpnicfDot11BSSRxStatis64Entry=_HpnicfDot11BSSRxStatis64Entry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,32,1))
hpnicfDot11BSSRxStatis64Entry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_P))
if mibBuilder.loadTexts:hpnicfDot11BSSRxStatis64Entry.setStatus(_A)
_HpnicfDot11BSSRx64FrameCnt_Type=Counter64
_HpnicfDot11BSSRx64FrameCnt_Object=MibTableColumn
hpnicfDot11BSSRx64FrameCnt=_HpnicfDot11BSSRx64FrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,32,1,1),_HpnicfDot11BSSRx64FrameCnt_Type())
hpnicfDot11BSSRx64FrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRx64FrameCnt.setStatus(_A)
_HpnicfDot11BSSRx64FrameBytes_Type=Counter64
_HpnicfDot11BSSRx64FrameBytes_Object=MibTableColumn
hpnicfDot11BSSRx64FrameBytes=_HpnicfDot11BSSRx64FrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,32,1,2),_HpnicfDot11BSSRx64FrameBytes_Type())
hpnicfDot11BSSRx64FrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRx64FrameBytes.setStatus(_A)
_HpnicfDot11BSSRx64DataFrameCnt_Type=Counter64
_HpnicfDot11BSSRx64DataFrameCnt_Object=MibTableColumn
hpnicfDot11BSSRx64DataFrameCnt=_HpnicfDot11BSSRx64DataFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,32,1,3),_HpnicfDot11BSSRx64DataFrameCnt_Type())
hpnicfDot11BSSRx64DataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRx64DataFrameCnt.setStatus(_A)
_HpnicfDot11BSSRx64DataFrameBytes_Type=Counter64
_HpnicfDot11BSSRx64DataFrameBytes_Object=MibTableColumn
hpnicfDot11BSSRx64DataFrameBytes=_HpnicfDot11BSSRx64DataFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,32,1,4),_HpnicfDot11BSSRx64DataFrameBytes_Type())
hpnicfDot11BSSRx64DataFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRx64DataFrameBytes.setStatus(_A)
_HpnicfDot11BSSRx64AssocFrameCnt_Type=Counter64
_HpnicfDot11BSSRx64AssocFrameCnt_Object=MibTableColumn
hpnicfDot11BSSRx64AssocFrameCnt=_HpnicfDot11BSSRx64AssocFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,32,1,5),_HpnicfDot11BSSRx64AssocFrameCnt_Type())
hpnicfDot11BSSRx64AssocFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRx64AssocFrameCnt.setStatus(_A)
_HpnicfDot11BSSRx64PayloadBytes_Type=Counter64
_HpnicfDot11BSSRx64PayloadBytes_Object=MibTableColumn
hpnicfDot11BSSRx64PayloadBytes=_HpnicfDot11BSSRx64PayloadBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,32,1,6),_HpnicfDot11BSSRx64PayloadBytes_Type())
hpnicfDot11BSSRx64PayloadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRx64PayloadBytes.setStatus(_A)
_HpnicfDot11BSSRx64UniFrameCnt_Type=Counter64
_HpnicfDot11BSSRx64UniFrameCnt_Object=MibTableColumn
hpnicfDot11BSSRx64UniFrameCnt=_HpnicfDot11BSSRx64UniFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,32,1,7),_HpnicfDot11BSSRx64UniFrameCnt_Type())
hpnicfDot11BSSRx64UniFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRx64UniFrameCnt.setStatus(_A)
_HpnicfDot11BSSRx64NonUniFrameCnt_Type=Counter64
_HpnicfDot11BSSRx64NonUniFrameCnt_Object=MibTableColumn
hpnicfDot11BSSRx64NonUniFrameCnt=_HpnicfDot11BSSRx64NonUniFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,32,1,8),_HpnicfDot11BSSRx64NonUniFrameCnt_Type())
hpnicfDot11BSSRx64NonUniFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRx64NonUniFrameCnt.setStatus(_A)
_HpnicfDot11BSSRx64AuthenFrameCnt_Type=Counter64
_HpnicfDot11BSSRx64AuthenFrameCnt_Object=MibTableColumn
hpnicfDot11BSSRx64AuthenFrameCnt=_HpnicfDot11BSSRx64AuthenFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,32,1,9),_HpnicfDot11BSSRx64AuthenFrameCnt_Type())
hpnicfDot11BSSRx64AuthenFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSRx64AuthenFrameCnt.setStatus(_A)
_HpnicfDot11BSSTxStatis64Table_Object=MibTable
hpnicfDot11BSSTxStatis64Table=_HpnicfDot11BSSTxStatis64Table_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,33))
if mibBuilder.loadTexts:hpnicfDot11BSSTxStatis64Table.setStatus(_A)
_HpnicfDot11BSSTxStatis64Entry_Object=MibTableRow
hpnicfDot11BSSTxStatis64Entry=_HpnicfDot11BSSTxStatis64Entry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,33,1))
hpnicfDot11BSSTxStatis64Entry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_P))
if mibBuilder.loadTexts:hpnicfDot11BSSTxStatis64Entry.setStatus(_A)
_HpnicfDot11BSSTx64FrameCnt_Type=Counter64
_HpnicfDot11BSSTx64FrameCnt_Object=MibTableColumn
hpnicfDot11BSSTx64FrameCnt=_HpnicfDot11BSSTx64FrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,33,1,1),_HpnicfDot11BSSTx64FrameCnt_Type())
hpnicfDot11BSSTx64FrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTx64FrameCnt.setStatus(_A)
_HpnicfDot11BSSTx64FrameBytes_Type=Counter64
_HpnicfDot11BSSTx64FrameBytes_Object=MibTableColumn
hpnicfDot11BSSTx64FrameBytes=_HpnicfDot11BSSTx64FrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,33,1,2),_HpnicfDot11BSSTx64FrameBytes_Type())
hpnicfDot11BSSTx64FrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTx64FrameBytes.setStatus(_A)
_HpnicfDot11BSSTx64DataFrameCnt_Type=Counter64
_HpnicfDot11BSSTx64DataFrameCnt_Object=MibTableColumn
hpnicfDot11BSSTx64DataFrameCnt=_HpnicfDot11BSSTx64DataFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,33,1,3),_HpnicfDot11BSSTx64DataFrameCnt_Type())
hpnicfDot11BSSTx64DataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTx64DataFrameCnt.setStatus(_A)
_HpnicfDot11BSSTx64DataFrameBytes_Type=Counter64
_HpnicfDot11BSSTx64DataFrameBytes_Object=MibTableColumn
hpnicfDot11BSSTx64DataFrameBytes=_HpnicfDot11BSSTx64DataFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,33,1,4),_HpnicfDot11BSSTx64DataFrameBytes_Type())
hpnicfDot11BSSTx64DataFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTx64DataFrameBytes.setStatus(_A)
_HpnicfDot11BSSTx64AssocFrameCnt_Type=Counter64
_HpnicfDot11BSSTx64AssocFrameCnt_Object=MibTableColumn
hpnicfDot11BSSTx64AssocFrameCnt=_HpnicfDot11BSSTx64AssocFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,33,1,5),_HpnicfDot11BSSTx64AssocFrameCnt_Type())
hpnicfDot11BSSTx64AssocFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTx64AssocFrameCnt.setStatus(_A)
_HpnicfDot11BSSTx64PayloadBytes_Type=Counter64
_HpnicfDot11BSSTx64PayloadBytes_Object=MibTableColumn
hpnicfDot11BSSTx64PayloadBytes=_HpnicfDot11BSSTx64PayloadBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,33,1,6),_HpnicfDot11BSSTx64PayloadBytes_Type())
hpnicfDot11BSSTx64PayloadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTx64PayloadBytes.setStatus(_A)
_HpnicfDot11BSSTx64RetryCnt_Type=Counter64
_HpnicfDot11BSSTx64RetryCnt_Object=MibTableColumn
hpnicfDot11BSSTx64RetryCnt=_HpnicfDot11BSSTx64RetryCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,33,1,7),_HpnicfDot11BSSTx64RetryCnt_Type())
hpnicfDot11BSSTx64RetryCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTx64RetryCnt.setStatus(_A)
_HpnicfDot11BSSTx64UniFrameCnt_Type=Counter64
_HpnicfDot11BSSTx64UniFrameCnt_Object=MibTableColumn
hpnicfDot11BSSTx64UniFrameCnt=_HpnicfDot11BSSTx64UniFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,33,1,8),_HpnicfDot11BSSTx64UniFrameCnt_Type())
hpnicfDot11BSSTx64UniFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTx64UniFrameCnt.setStatus(_A)
_HpnicfDot11BSSTx64NonUniFrameCnt_Type=Counter64
_HpnicfDot11BSSTx64NonUniFrameCnt_Object=MibTableColumn
hpnicfDot11BSSTx64NonUniFrameCnt=_HpnicfDot11BSSTx64NonUniFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,33,1,9),_HpnicfDot11BSSTx64NonUniFrameCnt_Type())
hpnicfDot11BSSTx64NonUniFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTx64NonUniFrameCnt.setStatus(_A)
_HpnicfDot11BSSTx64AuthenFrameCnt_Type=Counter64
_HpnicfDot11BSSTx64AuthenFrameCnt_Object=MibTableColumn
hpnicfDot11BSSTx64AuthenFrameCnt=_HpnicfDot11BSSTx64AuthenFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,33,1,10),_HpnicfDot11BSSTx64AuthenFrameCnt_Type())
hpnicfDot11BSSTx64AuthenFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BSSTx64AuthenFrameCnt.setStatus(_A)
_HpnicfDot11APPacketMCSRateStatis2Table_Object=MibTable
hpnicfDot11APPacketMCSRateStatis2Table=_HpnicfDot11APPacketMCSRateStatis2Table_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,34))
if mibBuilder.loadTexts:hpnicfDot11APPacketMCSRateStatis2Table.setStatus(_A)
_HpnicfDot11APPacketMCSRateStatis2Entry_Object=MibTableRow
hpnicfDot11APPacketMCSRateStatis2Entry=_HpnicfDot11APPacketMCSRateStatis2Entry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,34,1))
hpnicfDot11APPacketMCSRateStatis2Entry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_AV))
if mibBuilder.loadTexts:hpnicfDot11APPacketMCSRateStatis2Entry.setStatus(_A)
class _HpnicfDot11APPacketMCS2Rate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000000000))
_HpnicfDot11APPacketMCS2Rate_Type.__name__=_D
_HpnicfDot11APPacketMCS2Rate_Object=MibTableColumn
hpnicfDot11APPacketMCS2Rate=_HpnicfDot11APPacketMCS2Rate_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,34,1,1),_HpnicfDot11APPacketMCS2Rate_Type())
hpnicfDot11APPacketMCS2Rate.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APPacketMCS2Rate.setStatus(_A)
_HpnicfDot11APRXPacketMCSRate2Count_Type=Counter64
_HpnicfDot11APRXPacketMCSRate2Count_Object=MibTableColumn
hpnicfDot11APRXPacketMCSRate2Count=_HpnicfDot11APRXPacketMCSRate2Count_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,34,1,2),_HpnicfDot11APRXPacketMCSRate2Count_Type())
hpnicfDot11APRXPacketMCSRate2Count.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APRXPacketMCSRate2Count.setStatus(_A)
_HpnicfDot11APTXPacketMCSRate2Count_Type=Counter64
_HpnicfDot11APTXPacketMCSRate2Count_Object=MibTableColumn
hpnicfDot11APTXPacketMCSRate2Count=_HpnicfDot11APTXPacketMCSRate2Count_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,34,1,3),_HpnicfDot11APTXPacketMCSRate2Count_Type())
hpnicfDot11APTXPacketMCSRate2Count.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APTXPacketMCSRate2Count.setStatus(_A)
_HpnicfDot11APUserSecAuthStatisCMTable_Object=MibTable
hpnicfDot11APUserSecAuthStatisCMTable=_HpnicfDot11APUserSecAuthStatisCMTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,35))
if mibBuilder.loadTexts:hpnicfDot11APUserSecAuthStatisCMTable.setStatus(_A)
_HpnicfDot11APUserSecAuthStatisCMEntry_Object=MibTableRow
hpnicfDot11APUserSecAuthStatisCMEntry=_HpnicfDot11APUserSecAuthStatisCMEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,35,1))
hpnicfDot11APUserSecAuthStatisCMEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_P))
if mibBuilder.loadTexts:hpnicfDot11APUserSecAuthStatisCMEntry.setStatus(_A)
_HpnicfDot11APUserConnFailCntCM_Type=Counter32
_HpnicfDot11APUserConnFailCntCM_Object=MibTableColumn
hpnicfDot11APUserConnFailCntCM=_HpnicfDot11APUserConnFailCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,35,1,1),_HpnicfDot11APUserConnFailCntCM_Type())
hpnicfDot11APUserConnFailCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserConnFailCntCM.setStatus(_A)
_HpnicfDot11APUserAuthReqCntCM_Type=Counter32
_HpnicfDot11APUserAuthReqCntCM_Object=MibTableColumn
hpnicfDot11APUserAuthReqCntCM=_HpnicfDot11APUserAuthReqCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,35,1,2),_HpnicfDot11APUserAuthReqCntCM_Type())
hpnicfDot11APUserAuthReqCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserAuthReqCntCM.setStatus(_A)
_HpnicfDot11APUserAuthSuccCntCM_Type=Counter32
_HpnicfDot11APUserAuthSuccCntCM_Object=MibTableColumn
hpnicfDot11APUserAuthSuccCntCM=_HpnicfDot11APUserAuthSuccCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,35,1,3),_HpnicfDot11APUserAuthSuccCntCM_Type())
hpnicfDot11APUserAuthSuccCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserAuthSuccCntCM.setStatus(_A)
_HpnicfDot11APUserAuthFailCntCM_Type=Counter32
_HpnicfDot11APUserAuthFailCntCM_Object=MibTableColumn
hpnicfDot11APUserAuthFailCntCM=_HpnicfDot11APUserAuthFailCntCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,35,1,4),_HpnicfDot11APUserAuthFailCntCM_Type())
hpnicfDot11APUserAuthFailCntCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserAuthFailCntCM.setStatus(_A)
_HpnicfDot11AllUserOnlineTimeCM_Type=TimeTicks
_HpnicfDot11AllUserOnlineTimeCM_Object=MibTableColumn
hpnicfDot11AllUserOnlineTimeCM=_HpnicfDot11AllUserOnlineTimeCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,35,1,5),_HpnicfDot11AllUserOnlineTimeCM_Type())
hpnicfDot11AllUserOnlineTimeCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AllUserOnlineTimeCM.setStatus(_A)
_HpnicfDot11APUserInfoStatis2CMTable_Object=MibTable
hpnicfDot11APUserInfoStatis2CMTable=_HpnicfDot11APUserInfoStatis2CMTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,36))
if mibBuilder.loadTexts:hpnicfDot11APUserInfoStatis2CMTable.setStatus(_A)
_HpnicfDot11APUserInfoStatis2CMEntry_Object=MibTableRow
hpnicfDot11APUserInfoStatis2CMEntry=_HpnicfDot11APUserInfoStatis2CMEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,36,1))
hpnicfDot11APUserInfoStatis2CMEntry.setIndexNames((0,_C,_E),(0,_C,_AW))
if mibBuilder.loadTexts:hpnicfDot11APUserInfoStatis2CMEntry.setStatus(_A)
_HpnicfDot11APUserMacAddr2CM_Type=MacAddress
_HpnicfDot11APUserMacAddr2CM_Object=MibTableColumn
hpnicfDot11APUserMacAddr2CM=_HpnicfDot11APUserMacAddr2CM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,36,1,1),_HpnicfDot11APUserMacAddr2CM_Type())
hpnicfDot11APUserMacAddr2CM.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDot11APUserMacAddr2CM.setStatus(_A)
_HpnicfDot11APUserIpAddr2CM_Type=IpAddress
_HpnicfDot11APUserIpAddr2CM_Object=MibTableColumn
hpnicfDot11APUserIpAddr2CM=_HpnicfDot11APUserIpAddr2CM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,36,1,2),_HpnicfDot11APUserIpAddr2CM_Type())
hpnicfDot11APUserIpAddr2CM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserIpAddr2CM.setStatus(_A)
_HpnicfDot11APUserLoginName2CM_Type=OctetString
_HpnicfDot11APUserLoginName2CM_Object=MibTableColumn
hpnicfDot11APUserLoginName2CM=_HpnicfDot11APUserLoginName2CM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,36,1,3),_HpnicfDot11APUserLoginName2CM_Type())
hpnicfDot11APUserLoginName2CM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserLoginName2CM.setStatus(_A)
_HpnicfDot11APUserLoginTime2CM_Type=OctetString
_HpnicfDot11APUserLoginTime2CM_Object=MibTableColumn
hpnicfDot11APUserLoginTime2CM=_HpnicfDot11APUserLoginTime2CM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,36,1,4),_HpnicfDot11APUserLoginTime2CM_Type())
hpnicfDot11APUserLoginTime2CM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserLoginTime2CM.setStatus(_A)
_HpnicfDot11APUserOnlineTime2CM_Type=TimeTicks
_HpnicfDot11APUserOnlineTime2CM_Object=MibTableColumn
hpnicfDot11APUserOnlineTime2CM=_HpnicfDot11APUserOnlineTime2CM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,36,1,5),_HpnicfDot11APUserOnlineTime2CM_Type())
hpnicfDot11APUserOnlineTime2CM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserOnlineTime2CM.setStatus(_A)
class _HpnicfDot11APUserAuthType2CM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('authFree',1),(_AS,2),(_AT,3),('autoAuth',4)))
_HpnicfDot11APUserAuthType2CM_Type.__name__=_D
_HpnicfDot11APUserAuthType2CM_Object=MibTableColumn
hpnicfDot11APUserAuthType2CM=_HpnicfDot11APUserAuthType2CM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,36,1,6),_HpnicfDot11APUserAuthType2CM_Type())
hpnicfDot11APUserAuthType2CM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserAuthType2CM.setStatus(_A)
_HpnicfDot11APUserTxPacketCnt2CM_Type=Counter32
_HpnicfDot11APUserTxPacketCnt2CM_Object=MibTableColumn
hpnicfDot11APUserTxPacketCnt2CM=_HpnicfDot11APUserTxPacketCnt2CM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,36,1,7),_HpnicfDot11APUserTxPacketCnt2CM_Type())
hpnicfDot11APUserTxPacketCnt2CM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserTxPacketCnt2CM.setStatus(_A)
_HpnicfDot11APUserTxBytes2CM_Type=Counter64
_HpnicfDot11APUserTxBytes2CM_Object=MibTableColumn
hpnicfDot11APUserTxBytes2CM=_HpnicfDot11APUserTxBytes2CM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,36,1,8),_HpnicfDot11APUserTxBytes2CM_Type())
hpnicfDot11APUserTxBytes2CM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserTxBytes2CM.setStatus(_A)
_HpnicfDot11APUserRxPacketCnt2CM_Type=Counter32
_HpnicfDot11APUserRxPacketCnt2CM_Object=MibTableColumn
hpnicfDot11APUserRxPacketCnt2CM=_HpnicfDot11APUserRxPacketCnt2CM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,36,1,9),_HpnicfDot11APUserRxPacketCnt2CM_Type())
hpnicfDot11APUserRxPacketCnt2CM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserRxPacketCnt2CM.setStatus(_A)
_HpnicfDot11APUserRxBytes2CM_Type=Counter64
_HpnicfDot11APUserRxBytes2CM_Object=MibTableColumn
hpnicfDot11APUserRxBytes2CM=_HpnicfDot11APUserRxBytes2CM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,2,36,1,10),_HpnicfDot11APUserRxBytes2CM_Type())
hpnicfDot11APUserRxBytes2CM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserRxBytes2CM.setStatus(_A)
_HpnicfDot11APMtNotifyGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11APMtNotifyGroup=_HpnicfDot11APMtNotifyGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3))
_HpnicfDot11APMtTraps_ObjectIdentity=ObjectIdentity
hpnicfDot11APMtTraps=_HpnicfDot11APMtTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0))
_HpnicfDot11APMtTrapVarObjects_ObjectIdentity=ObjectIdentity
hpnicfDot11APMtTrapVarObjects=_HpnicfDot11APMtTrapVarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1))
_HpnicfDot11APMtTrapCfgErrReason_Type=HpnicfDot11NotifyReasonType
_HpnicfDot11APMtTrapCfgErrReason_Object=MibScalar
hpnicfDot11APMtTrapCfgErrReason=_HpnicfDot11APMtTrapCfgErrReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,1),_HpnicfDot11APMtTrapCfgErrReason_Type())
hpnicfDot11APMtTrapCfgErrReason.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtTrapCfgErrReason.setStatus(_A)
class _HpnicfDot11APMtTrapRadioFailReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,8)));namedValues=NamedValues(*((_w,1),('hpnicferror',2),('swerror',3),('radar',4),(_f,8)))
_HpnicfDot11APMtTrapRadioFailReason_Type.__name__=_D
_HpnicfDot11APMtTrapRadioFailReason_Object=MibScalar
hpnicfDot11APMtTrapRadioFailReason=_HpnicfDot11APMtTrapRadioFailReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,2),_HpnicfDot11APMtTrapRadioFailReason_Type())
hpnicfDot11APMtTrapRadioFailReason.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtTrapRadioFailReason.setStatus(_A)
_HpnicfDot11APMtTrapOldChannel_Type=HpnicfDot11ChannelScopeType
_HpnicfDot11APMtTrapOldChannel_Object=MibScalar
hpnicfDot11APMtTrapOldChannel=_HpnicfDot11APMtTrapOldChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,3),_HpnicfDot11APMtTrapOldChannel_Type())
hpnicfDot11APMtTrapOldChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtTrapOldChannel.setStatus(_A)
_HpnicfDot11APMtTrapNewChannel_Type=HpnicfDot11ChannelScopeType
_HpnicfDot11APMtTrapNewChannel_Object=MibScalar
hpnicfDot11APMtTrapNewChannel=_HpnicfDot11APMtTrapNewChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,4),_HpnicfDot11APMtTrapNewChannel_Type())
hpnicfDot11APMtTrapNewChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtTrapNewChannel.setStatus(_A)
_HpnicfDot11APChannelChgMode_Type=HpnicfDot11RFModeType
_HpnicfDot11APChannelChgMode_Object=MibScalar
hpnicfDot11APChannelChgMode=_HpnicfDot11APChannelChgMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,5),_HpnicfDot11APChannelChgMode_Type())
hpnicfDot11APChannelChgMode.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APChannelChgMode.setStatus(_A)
class _HpnicfDot11APChgWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_x,1),('monitor',2),('hybrid',3)))
_HpnicfDot11APChgWorkMode_Type.__name__=_D
_HpnicfDot11APChgWorkMode_Object=MibScalar
hpnicfDot11APChgWorkMode=_HpnicfDot11APChgWorkMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,6),_HpnicfDot11APChgWorkMode_Type())
hpnicfDot11APChgWorkMode.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APChgWorkMode.setStatus(_A)
_HpnicfDot11APIntfDevMACAddress_Type=MacAddress
_HpnicfDot11APIntfDevMACAddress_Object=MibScalar
hpnicfDot11APIntfDevMACAddress=_HpnicfDot11APIntfDevMACAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,7),_HpnicfDot11APIntfDevMACAddress_Type())
hpnicfDot11APIntfDevMACAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APIntfDevMACAddress.setStatus(_A)
_HpnicfDot11APMtTrapOldIPAddr_Type=IpAddress
_HpnicfDot11APMtTrapOldIPAddr_Object=MibScalar
hpnicfDot11APMtTrapOldIPAddr=_HpnicfDot11APMtTrapOldIPAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,8),_HpnicfDot11APMtTrapOldIPAddr_Type())
hpnicfDot11APMtTrapOldIPAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtTrapOldIPAddr.setStatus(_A)
_HpnicfDot11CurrInterfDetectedNum_Type=Integer32
_HpnicfDot11CurrInterfDetectedNum_Object=MibScalar
hpnicfDot11CurrInterfDetectedNum=_HpnicfDot11CurrInterfDetectedNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,9),_HpnicfDot11CurrInterfDetectedNum_Type())
hpnicfDot11CurrInterfDetectedNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11CurrInterfDetectedNum.setStatus(_A)
class _HpnicfDot11StaFullReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('ap',1),('bss',2),('radio',3),('radioConcur',4),('radiopolicy',5),('ac',6),('acConcur',7),('aid',8)))
_HpnicfDot11StaFullReason_Type.__name__=_D
_HpnicfDot11StaFullReason_Object=MibScalar
hpnicfDot11StaFullReason=_HpnicfDot11StaFullReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,10),_HpnicfDot11StaFullReason_Type())
hpnicfDot11StaFullReason.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11StaFullReason.setStatus(_A)
_HpnicfDot11StaLimitNumber_Type=Integer32
_HpnicfDot11StaLimitNumber_Object=MibScalar
hpnicfDot11StaLimitNumber=_HpnicfDot11StaLimitNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,11),_HpnicfDot11StaLimitNumber_Type())
hpnicfDot11StaLimitNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11StaLimitNumber.setStatus(_A)
class _HpnicfDot11APRadioDownReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('phyicalUnusable',1),('configDisable',2),('operatinUnusable',3),('apTunnelDown',4)))
_HpnicfDot11APRadioDownReason_Type.__name__=_D
_HpnicfDot11APRadioDownReason_Object=MibScalar
hpnicfDot11APRadioDownReason=_HpnicfDot11APRadioDownReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,12),_HpnicfDot11APRadioDownReason_Type())
hpnicfDot11APRadioDownReason.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APRadioDownReason.setStatus(_A)
_HpnicfDot11InterfMacList_Type=OctetString
_HpnicfDot11InterfMacList_Object=MibScalar
hpnicfDot11InterfMacList=_HpnicfDot11InterfMacList_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,13),_HpnicfDot11InterfMacList_Type())
hpnicfDot11InterfMacList.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11InterfMacList.setStatus(_A)
_HpnicfDot11APTrapUserCnt_Type=Integer32
_HpnicfDot11APTrapUserCnt_Object=MibScalar
hpnicfDot11APTrapUserCnt=_HpnicfDot11APTrapUserCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,14),_HpnicfDot11APTrapUserCnt_Type())
hpnicfDot11APTrapUserCnt.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APTrapUserCnt.setStatus(_A)
_HpnicfDot11APTrapUserThreshold_Type=Integer32
_HpnicfDot11APTrapUserThreshold_Object=MibScalar
hpnicfDot11APTrapUserThreshold=_HpnicfDot11APTrapUserThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,15),_HpnicfDot11APTrapUserThreshold_Type())
hpnicfDot11APTrapUserThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APTrapUserThreshold.setStatus(_A)
_HpnicfDot11APMtChanlChgCount_Type=Integer32
_HpnicfDot11APMtChanlChgCount_Object=MibScalar
hpnicfDot11APMtChanlChgCount=_HpnicfDot11APMtChanlChgCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,16),_HpnicfDot11APMtChanlChgCount_Type())
hpnicfDot11APMtChanlChgCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtChanlChgCount.setStatus(_A)
_HpnicfDot11APMtFormerApVersion_Type=OctetString
_HpnicfDot11APMtFormerApVersion_Object=MibScalar
hpnicfDot11APMtFormerApVersion=_HpnicfDot11APMtFormerApVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,17),_HpnicfDot11APMtFormerApVersion_Type())
hpnicfDot11APMtFormerApVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtFormerApVersion.setStatus(_A)
_HpnicfDot11APMtAPID_Type=HpnicfDot11ObjectIDType
_HpnicfDot11APMtAPID_Object=MibScalar
hpnicfDot11APMtAPID=_HpnicfDot11APMtAPID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,18),_HpnicfDot11APMtAPID_Type())
hpnicfDot11APMtAPID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtAPID.setStatus(_A)
_HpnicfDot11APMtRadioID_Type=HpnicfDot11RadioScopeType
_HpnicfDot11APMtRadioID_Object=MibScalar
hpnicfDot11APMtRadioID=_HpnicfDot11APMtRadioID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,19),_HpnicfDot11APMtRadioID_Type())
hpnicfDot11APMtRadioID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtRadioID.setStatus(_A)
_HpnicfDot11APMtChannel_Type=HpnicfDot11ChannelScopeType
_HpnicfDot11APMtChannel_Object=MibScalar
hpnicfDot11APMtChannel=_HpnicfDot11APMtChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,20),_HpnicfDot11APMtChannel_Type())
hpnicfDot11APMtChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtChannel.setStatus(_A)
_HpnicfDot11APMtInterfMacAdd_Type=MacAddress
_HpnicfDot11APMtInterfMacAdd_Object=MibScalar
hpnicfDot11APMtInterfMacAdd=_HpnicfDot11APMtInterfMacAdd_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,21),_HpnicfDot11APMtInterfMacAdd_Type())
hpnicfDot11APMtInterfMacAdd.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtInterfMacAdd.setStatus(_A)
_HpnicfDot11APMtAdjChannel_Type=HpnicfDot11ChannelScopeType
_HpnicfDot11APMtAdjChannel_Object=MibScalar
hpnicfDot11APMtAdjChannel=_HpnicfDot11APMtAdjChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,22),_HpnicfDot11APMtAdjChannel_Type())
hpnicfDot11APMtAdjChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtAdjChannel.setStatus(_A)
_HpnicfDot11APMtFirstTrapTime_Type=TimeTicks
_HpnicfDot11APMtFirstTrapTime_Object=MibScalar
hpnicfDot11APMtFirstTrapTime=_HpnicfDot11APMtFirstTrapTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,23),_HpnicfDot11APMtFirstTrapTime_Type())
hpnicfDot11APMtFirstTrapTime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtFirstTrapTime.setStatus(_A)
_HpnicfDot11APMtTrapAPMacAddress_Type=MacAddress
_HpnicfDot11APMtTrapAPMacAddress_Object=MibScalar
hpnicfDot11APMtTrapAPMacAddress=_HpnicfDot11APMtTrapAPMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,24),_HpnicfDot11APMtTrapAPMacAddress_Type())
hpnicfDot11APMtTrapAPMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtTrapAPMacAddress.setStatus(_A)
class _HpnicfDot11APMtUpLinkSwitchInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_f,1),('tdscdma',2),('tdlte',3)))
_HpnicfDot11APMtUpLinkSwitchInfo_Type.__name__=_D
_HpnicfDot11APMtUpLinkSwitchInfo_Object=MibScalar
hpnicfDot11APMtUpLinkSwitchInfo=_HpnicfDot11APMtUpLinkSwitchInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,25),_HpnicfDot11APMtUpLinkSwitchInfo_Type())
hpnicfDot11APMtUpLinkSwitchInfo.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtUpLinkSwitchInfo.setStatus(_A)
_HpnicfDot11APMtUpLinkSwitchTime_Type=TimeStamp
_HpnicfDot11APMtUpLinkSwitchTime_Object=MibScalar
hpnicfDot11APMtUpLinkSwitchTime=_HpnicfDot11APMtUpLinkSwitchTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,26),_HpnicfDot11APMtUpLinkSwitchTime_Type())
hpnicfDot11APMtUpLinkSwitchTime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtUpLinkSwitchTime.setStatus(_A)
_HpnicfDot11APMtOldCellId_Type=Integer32
_HpnicfDot11APMtOldCellId_Object=MibScalar
hpnicfDot11APMtOldCellId=_HpnicfDot11APMtOldCellId_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,27),_HpnicfDot11APMtOldCellId_Type())
hpnicfDot11APMtOldCellId.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtOldCellId.setStatus(_A)
_HpnicfDot11APMtCurCellId_Type=Integer32
_HpnicfDot11APMtCurCellId_Object=MibScalar
hpnicfDot11APMtCurCellId=_HpnicfDot11APMtCurCellId_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,28),_HpnicfDot11APMtCurCellId_Type())
hpnicfDot11APMtCurCellId.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtCurCellId.setStatus(_A)
_HpnicfDot11APMtOldBand_Type=OctetString
_HpnicfDot11APMtOldBand_Object=MibScalar
hpnicfDot11APMtOldBand=_HpnicfDot11APMtOldBand_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,29),_HpnicfDot11APMtOldBand_Type())
hpnicfDot11APMtOldBand.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtOldBand.setStatus(_A)
_HpnicfDot11APMtActiveBand_Type=OctetString
_HpnicfDot11APMtActiveBand_Object=MibScalar
hpnicfDot11APMtActiveBand=_HpnicfDot11APMtActiveBand_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,1,30),_HpnicfDot11APMtActiveBand_Type())
hpnicfDot11APMtActiveBand.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APMtActiveBand.setStatus(_A)
hpnicfDot11APMtWorkModeChgTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,1))
hpnicfDot11APMtWorkModeChgTrap.setObjects(*((_C,_L),(_C,_AX),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APMtWorkModeChgTrap.setStatus(_A)
hpnicfDot11APMtCfgErrorTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,2))
hpnicfDot11APMtCfgErrorTrap.setObjects(*((_C,_L),(_C,_G),(_C,_AY)))
if mibBuilder.loadTexts:hpnicfDot11APMtCfgErrorTrap.setStatus(_A)
hpnicfDot11APMtRadioFailTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,3))
hpnicfDot11APMtRadioFailTrap.setObjects(*((_C,_L),(_C,_G),(_C,_AZ)))
if mibBuilder.loadTexts:hpnicfDot11APMtRadioFailTrap.setStatus(_A)
hpnicfDot11APMtRadioFailRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,4))
hpnicfDot11APMtRadioFailRecoverTrap.setObjects(*((_C,_L),(_C,_G)))
if mibBuilder.loadTexts:hpnicfDot11APMtRadioFailRecoverTrap.setStatus(_A)
hpnicfDot11APMtRdoChanlChgTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,5))
hpnicfDot11APMtRdoChanlChgTrap.setObjects(*((_C,_L),(_C,_G),(_C,_Aa),(_C,_Ab),(_C,_Ac),(_C,_Ad),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APMtRdoChanlChgTrap.setStatus(_A)
hpnicfDot11APMtTimeSynFail=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,6))
hpnicfDot11APMtTimeSynFail.setObjects((_C,_L))
if mibBuilder.loadTexts:hpnicfDot11APMtTimeSynFail.setStatus(_A)
hpnicfDot11APMtChlIntfDetected=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,7))
hpnicfDot11APMtChlIntfDetected.setObjects((_C,_N))
if mibBuilder.loadTexts:hpnicfDot11APMtChlIntfDetected.setStatus(_A)
hpnicfDot11APMtIntfAPDetected=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,8))
hpnicfDot11APMtIntfAPDetected.setObjects(*((_C,_N),(_C,_n)))
if mibBuilder.loadTexts:hpnicfDot11APMtIntfAPDetected.setStatus(_A)
hpnicfDot11APMtIntfStaDetected=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,9))
hpnicfDot11APMtIntfStaDetected.setObjects(*((_C,_N),(_C,_n)))
if mibBuilder.loadTexts:hpnicfDot11APMtIntfStaDetected.setStatus(_A)
hpnicfDot11APMtIPChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,10))
hpnicfDot11APMtIPChange.setObjects(*((_C,_Ae),(_C,_Af)))
if mibBuilder.loadTexts:hpnicfDot11APMtIPChange.setStatus(_A)
hpnicfDot11APFlashWriteFailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,11))
hpnicfDot11APFlashWriteFailure.setObjects(*((_C,_L),(_C,_Ag),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APFlashWriteFailure.setStatus(_A)
hpnicfDot11APSysReboot=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,12))
hpnicfDot11APSysReboot.setObjects((_C,_L))
if mibBuilder.loadTexts:hpnicfDot11APSysReboot.setStatus(_A)
hpnicfDot11APMtAvailChlTooLow=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,13))
hpnicfDot11APMtAvailChlTooLow.setObjects(*((_C,_G),(_C,_J),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APMtAvailChlTooLow.setStatus(_A)
hpnicfDot11APImgDwldSuccess=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,14))
hpnicfDot11APImgDwldSuccess.setObjects(*((_C,_Ah),(_C,_Ai),(_C,_Aj)))
if mibBuilder.loadTexts:hpnicfDot11APImgDwldSuccess.setStatus(_A)
hpnicfDot11APInterfDetectedTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,15))
hpnicfDot11APInterfDetectedTrap.setObjects(*((_C,_N),(_C,_o),(_C,_p)))
if mibBuilder.loadTexts:hpnicfDot11APInterfDetectedTrap.setStatus(_A)
hpnicfDot11APInterfClearTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,16))
hpnicfDot11APInterfClearTrap.setObjects(*((_C,_N),(_C,_J),(_C,_O),(_C,_R),(_C,_K),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APInterfClearTrap.setStatus(_A)
hpnicfDot11StaInterfDetectedTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,17))
hpnicfDot11StaInterfDetectedTrap.setObjects(*((_C,_N),(_C,_o),(_C,_p),(_C,_K)))
if mibBuilder.loadTexts:hpnicfDot11StaInterfDetectedTrap.setStatus(_A)
hpnicfDot11StaInterfClearTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,18))
hpnicfDot11StaInterfClearTrap.setObjects(*((_C,_N),(_C,_J),(_C,_O),(_C,_R),(_C,_K),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11StaInterfClearTrap.setStatus(_A)
hpnicfDot11OtherDevIntDetectedTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,19))
hpnicfDot11OtherDevIntDetectedTrap.setObjects(*((_C,_N),(_C,_K)))
if mibBuilder.loadTexts:hpnicfDot11OtherDevIntDetectedTrap.setStatus(_A)
hpnicfDot11OtherDevIntClearTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,20))
hpnicfDot11OtherDevIntClearTrap.setObjects(*((_C,_N),(_C,_J),(_C,_O),(_C,_K),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11OtherDevIntClearTrap.setStatus(_A)
hpnicfDot11APModuleTroubleTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,21))
hpnicfDot11APModuleTroubleTrap.setObjects(*((_C,_G),(_C,_J),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APModuleTroubleTrap.setStatus(_A)
hpnicfDot11APModuleTroubleClearTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,22))
hpnicfDot11APModuleTroubleClearTrap.setObjects(*((_C,_G),(_C,_J),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APModuleTroubleClearTrap.setStatus(_A)
hpnicfDot11APRadioDownTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,23))
hpnicfDot11APRadioDownTrap.setObjects(*((_C,_G),(_C,_Ak),(_C,_J),(_C,_K),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APRadioDownTrap.setStatus(_A)
hpnicfDot11APRadioDownRecovTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,24))
hpnicfDot11APRadioDownRecovTrap.setObjects(*((_C,_G),(_C,_J),(_C,_K),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APRadioDownRecovTrap.setStatus(_A)
hpnicfDot11APStaFullTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,25))
hpnicfDot11APStaFullTrap.setObjects(*((_C,_L),(_C,_q),(_C,_r),(_C,_K),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APStaFullTrap.setStatus(_A)
hpnicfDot11APStaFullRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,26))
hpnicfDot11APStaFullRecoverTrap.setObjects(*((_C,_L),(_C,_q),(_C,_r),(_C,_K),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APStaFullRecoverTrap.setStatus(_A)
hpnicfDot11DFSFreeCntBelowThrRecov=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,27))
hpnicfDot11DFSFreeCntBelowThrRecov.setObjects(*((_C,_G),(_C,_J),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11DFSFreeCntBelowThrRecov.setStatus(_A)
hpnicfDot11APCpuUsageHigh=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,28))
hpnicfDot11APCpuUsageHigh.setObjects(*((_C,_L),(_C,_s),(_C,_K),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APCpuUsageHigh.setStatus(_A)
hpnicfDot11APCpuUsageHighRecover=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,29))
hpnicfDot11APCpuUsageHighRecover.setObjects(*((_C,_L),(_C,_s),(_C,_K),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APCpuUsageHighRecover.setStatus(_A)
hpnicfDot11APMemUsageHigh=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,30))
hpnicfDot11APMemUsageHigh.setObjects(*((_C,_L),(_C,_t),(_C,_K),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APMemUsageHigh.setStatus(_A)
hpnicfDot11APMemUsageHighRecover=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,31))
hpnicfDot11APMemUsageHighRecover.setObjects(*((_C,_L),(_C,_t),(_C,_K),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APMemUsageHighRecover.setStatus(_A)
hpnicfDot11APTrapUserCntExceedThre=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,32))
hpnicfDot11APTrapUserCntExceedThre.setObjects(*((_C,_L),(_C,_Al),(_C,_Am)))
if mibBuilder.loadTexts:hpnicfDot11APTrapUserCntExceedThre.setStatus(_A)
hpnicfDot11APMtDetectedIntfAP=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,33))
hpnicfDot11APMtDetectedIntfAP.setObjects(*((_C,_J),(_C,_O),(_C,_U),(_C,_R),(_C,_K),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APMtDetectedIntfAP.setStatus(_A)
hpnicfDot11APMtDetectedIntfSTA=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,34))
hpnicfDot11APMtDetectedIntfSTA.setObjects(*((_C,_J),(_C,_O),(_C,_U),(_C,_R),(_C,_K),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APMtDetectedIntfSTA.setStatus(_A)
hpnicfDot11APMtDetectedIntfOtherDev=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,35))
hpnicfDot11APMtDetectedIntfOtherDev.setObjects(*((_C,_J),(_C,_O),(_C,_U),(_C,_I)))
if mibBuilder.loadTexts:hpnicfDot11APMtDetectedIntfOtherDev.setStatus(_A)
hpnicfDot11DetcAdjChlIntfAP=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,36))
hpnicfDot11DetcAdjChlIntfAP.setObjects(*((_C,_J),(_C,_O),(_C,_U),(_C,_u),(_C,_R),(_C,_K)))
if mibBuilder.loadTexts:hpnicfDot11DetcAdjChlIntfAP.setStatus(_A)
hpnicfDot11DetcAdjChlIntfAPClear=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,37))
hpnicfDot11DetcAdjChlIntfAPClear.setObjects(*((_C,_J),(_C,_O),(_C,_U),(_C,_u),(_C,_R),(_C,_K)))
if mibBuilder.loadTexts:hpnicfDot11DetcAdjChlIntfAPClear.setStatus(_A)
hpnicfDot11APPowerOffTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,38))
hpnicfDot11APPowerOffTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:hpnicfDot11APPowerOffTrap.setStatus(_A)
hpnicfDot11APPowerOnTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,39))
hpnicfDot11APPowerOnTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:hpnicfDot11APPowerOnTrap.setStatus(_A)
hpnicfDot11UpLinkSwitchTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,2,3,0,40))
hpnicfDot11UpLinkSwitchTrap.setObjects(*((_C,_J),(_C,_An),(_C,_I),(_C,_Ao),(_C,_Ap),(_C,_Aq),(_C,_Ar),(_C,_As)))
if mibBuilder.loadTexts:hpnicfDot11UpLinkSwitchTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfDot11APMT':hpnicfDot11APMT,'hpnicfDot11APObjectGroup':hpnicfDot11APObjectGroup,'hpnicfDot11APObjectStatusTable':hpnicfDot11APObjectStatusTable,'hpnicfDot11APObjectStatusEntry':hpnicfDot11APObjectStatusEntry,_L:hpnicfDot11APID,_Ae:hpnicfDot11APIPAddress,'hpnicfDot11APMacAddress':hpnicfDot11APMacAddress,'hpnicfDot11APOperationStatus':hpnicfDot11APOperationStatus,'hpnicfDot11APTemplateNameOfAP':hpnicfDot11APTemplateNameOfAP,'hpnicfDot11APReset':hpnicfDot11APReset,'hpnicfDot11APCpuUsage':hpnicfDot11APCpuUsage,'hpnicfDot11APConnectionType':hpnicfDot11APConnectionType,'hpnicfDot11APLastImgDownloadTime':hpnicfDot11APLastImgDownloadTime,'hpnicfDot11APIPv6Address':hpnicfDot11APIPv6Address,'hpnicfDot11APLastRegisterTime':hpnicfDot11APLastRegisterTime,'hpnicfDot11APResetCM':hpnicfDot11APResetCM,'hpnicfDot11APObjectTable':hpnicfDot11APObjectTable,'hpnicfDot11APObjectEntry':hpnicfDot11APObjectEntry,_Z:hpnicfDot11APObjID,_Ai:hpnicfDot11CurrAPIPAddress,'hpnicfDot11CurrAPMacAddress':hpnicfDot11CurrAPMacAddress,'hpnicfDot11CurrACPortIndex':hpnicfDot11CurrACPortIndex,'hpnicfDot11CurrAPMACMode':hpnicfDot11CurrAPMACMode,'hpnicfDot11CurrAPTemplateName':hpnicfDot11CurrAPTemplateName,'hpnicfDot11CurrAPStationAssocCount':hpnicfDot11CurrAPStationAssocCount,_Ah:hpnicfDot11CurrAPName,'hpnicfDot11CurrAPModelName':hpnicfDot11CurrAPModelName,'hpnicfDot11CurrAPImageName':hpnicfDot11CurrAPImageName,_Aj:hpnicfDot11CurrAPSoftwareVersion,'hpnicfDot11CurrAPIPNetMask':hpnicfDot11CurrAPIPNetMask,'hpnicfDot11CurrRadioModeSupport':hpnicfDot11CurrRadioModeSupport,'hpnicfDot11CurrIfNumber':hpnicfDot11CurrIfNumber,'hpnicfDot11CurrAPElementID':hpnicfDot11CurrAPElementID,'hpnicfDot11CurrAPMode':hpnicfDot11CurrAPMode,'hpnicfDot11CurrAPIPv6Address':hpnicfDot11CurrAPIPv6Address,'hpnicfDot11CurrAPSSIDNumber':hpnicfDot11CurrAPSSIDNumber,'hpnicfDot11CurrAPManufacturer':hpnicfDot11CurrAPManufacturer,'hpnicfDot11CurrAPMemorySize':hpnicfDot11CurrAPMemorySize,'hpnicfDot11CurrAPMemSizeInBytes':hpnicfDot11CurrAPMemSizeInBytes,'hpnicfDot11CurrAPFlashSize':hpnicfDot11CurrAPFlashSize,'hpnicfDot11CurrAPFlashSizeInBytes':hpnicfDot11CurrAPFlashSizeInBytes,'hpnicfDot11CurrAPReleasedVersion':hpnicfDot11CurrAPReleasedVersion,'hpnicfDot11CurrRadioModeSupport2':hpnicfDot11CurrRadioModeSupport2,'hpnicfDot11CurrAPCPUTypeCM':hpnicfDot11CurrAPCPUTypeCM,'hpnicfDot11CurrAPMemoryTypeCM':hpnicfDot11CurrAPMemoryTypeCM,'hpnicfDot11CurrAPBSSIDNumberCM':hpnicfDot11CurrAPBSSIDNumberCM,'hpnicfDot11APRadioTable':hpnicfDot11APRadioTable,'hpnicfDot11APRadioEntry':hpnicfDot11APRadioEntry,_E:hpnicfDot11CurAPID,_G:hpnicfDot11RadioID,'hpnicfDot11AdminStatus':hpnicfDot11AdminStatus,'hpnicfDot11OperStatus':hpnicfDot11OperStatus,_N:hpnicfDot11Channel,'hpnicfDot11TxPowerLevel':hpnicfDot11TxPowerLevel,'hpnicfDot11APRadioIfIndex':hpnicfDot11APRadioIfIndex,'hpnicfDot11AntennaGain':hpnicfDot11AntennaGain,'hpnicfDot11MaxBandwidth':hpnicfDot11MaxBandwidth,'hpnicfDot11ResourceUseRatio':hpnicfDot11ResourceUseRatio,'hpnicfDot11RadioModeSupport':hpnicfDot11RadioModeSupport,'hpnicfDot11TxPowerLevel2':hpnicfDot11TxPowerLevel2,'hpnicfDot11PowerMgmtStatus':hpnicfDot11PowerMgmtStatus,'hpnicfDot11ChannelSwitchTimes':hpnicfDot11ChannelSwitchTimes,'hpnicfDot11AntennaType':hpnicfDot11AntennaType,'hpnicfDot11DiversitySelectionRx':hpnicfDot11DiversitySelectionRx,'hpnicfDot11MaxTxPwrLvl':hpnicfDot11MaxTxPwrLvl,'hpnicfDot11PwrAttRange':hpnicfDot11PwrAttRange,'hpnicfDot11AvgRxSignalStrength':hpnicfDot11AvgRxSignalStrength,'hpnicfDot11HighestRxSignalStrength':hpnicfDot11HighestRxSignalStrength,'hpnicfDot11LowestRxSignalStrength':hpnicfDot11LowestRxSignalStrength,'hpnicfDot11RadioIfUpdownTimes':hpnicfDot11RadioIfUpdownTimes,'hpnicfDot11RadioIfLastChange':hpnicfDot11RadioIfLastChange,'hpnicfDot11RadioModeSupport2':hpnicfDot11RadioModeSupport2,'hpnicfDot11OperStatusCM':hpnicfDot11OperStatusCM,'hpnicfDot11APBSSTable':hpnicfDot11APBSSTable,'hpnicfDot11APBSSEntry':hpnicfDot11APBSSEntry,_P:hpnicfDot11WlanID,'hpnicfDot11BSSID':hpnicfDot11BSSID,'hpnicfDot11CurrSvcPolicyID':hpnicfDot11CurrSvcPolicyID,'hpnicfDot11SSID':hpnicfDot11SSID,'hpnicfDot11CurrSSIDResourceUseRatio':hpnicfDot11CurrSSIDResourceUseRatio,'hpnicfDot11APEssVlanId':hpnicfDot11APEssVlanId,'hpnicfDot11APModelTable':hpnicfDot11APModelTable,'hpnicfDot11APModelEntry':hpnicfDot11APModelEntry,_z:hpnicfDot11APModelAlias,'hpnicfDot11APModelName':hpnicfDot11APModelName,'hpnicfDot11RadioNumSupport':hpnicfDot11RadioNumSupport,'hpnicfDot11StationNumSupport':hpnicfDot11StationNumSupport,'hpnicfDot11MACModeSupport':hpnicfDot11MACModeSupport,'hpnicfDot11APManufacturer':hpnicfDot11APManufacturer,'hpnicfDot11APCPUType':hpnicfDot11APCPUType,'hpnicfDot11APCPUClockSpeed':hpnicfDot11APCPUClockSpeed,'hpnicfDot11APMemoryType':hpnicfDot11APMemoryType,'hpnicfDot11APFlashType':hpnicfDot11APFlashType,'hpnicfDot11APFlashSize':hpnicfDot11APFlashSize,'hpnicfDot11APMemSize':hpnicfDot11APMemSize,'hpnicfDot11APFlashSizeInBytes':hpnicfDot11APFlashSizeInBytes,'hpnicfDot11APMemorySize':hpnicfDot11APMemorySize,'hpnicfDot11APIfTable':hpnicfDot11APIfTable,'hpnicfDot11APIfEntry':hpnicfDot11APIfEntry,_a:hpnicfDot11APIfIndex,'hpnicfDot11APIfDescr':hpnicfDot11APIfDescr,'hpnicfDot11APIfType':hpnicfDot11APIfType,'hpnicfDot11APIfMtu':hpnicfDot11APIfMtu,'hpnicfDot11APIfPHYAddress':hpnicfDot11APIfPHYAddress,'hpnicfDot11APIfSpeed':hpnicfDot11APIfSpeed,'hpnicfDot11APIfInDataRate':hpnicfDot11APIfInDataRate,'hpnicfDot11APIfOutDataRate':hpnicfDot11APIfOutDataRate,'hpnicfDot11APIfSpeedKbps':hpnicfDot11APIfSpeedKbps,'hpnicfDot11APIfTypeCM':hpnicfDot11APIfTypeCM,'hpnicfDot11APSSIDObjectTable':hpnicfDot11APSSIDObjectTable,'hpnicfDot11APSSIDObjectEntry':hpnicfDot11APSSIDObjectEntry,_A0:hpnicfDot11APConfigSPID,'hpnicfDot11APConfigSSIDName':hpnicfDot11APConfigSSIDName,'hpnicfDot11APConfigBSSIDNum':hpnicfDot11APConfigBSSIDNum,'hpnicfDot11APConfigPortalStaNum':hpnicfDot11APConfigPortalStaNum,'hpnicfDot11APSysInfoTable':hpnicfDot11APSysInfoTable,'hpnicfDot11APSysInfoEntry':hpnicfDot11APSysInfoEntry,'hpnicfDot11APSysUpTime':hpnicfDot11APSysUpTime,_s:hpnicfDot11APCPURTUsage,'hpnicfDot11APCPUAvgUsage':hpnicfDot11APCPUAvgUsage,_t:hpnicfDot11APMemRTUsage,'hpnicfDot11APMemAvgUsage':hpnicfDot11APMemAvgUsage,'hpnicfDot11APIPAddressGateway':hpnicfDot11APIPAddressGateway,'hpnicfDot11APACAssociateStatus':hpnicfDot11APACAssociateStatus,'hpnicfDot11APManuBuildInfo':hpnicfDot11APManuBuildInfo,'hpnicfDot11APFlashFreeSize':hpnicfDot11APFlashFreeSize,'hpnicfDot11APTemperature':hpnicfDot11APTemperature,'hpnicfDot11APIdleListTable':hpnicfDot11APIdleListTable,'hpnicfDot11APIdleListEntry':hpnicfDot11APIdleListEntry,_A2:hpnicfDot11APIdleTemplateName,'hpnicfDot11APIdleSerialID':hpnicfDot11APIdleSerialID,'hpnicfDot11APSysInfoByAPIDTable':hpnicfDot11APSysInfoByAPIDTable,'hpnicfDot11APSysInfoByAPIDEntry':hpnicfDot11APSysInfoByAPIDEntry,'hpnicfDot11APSysUpTime2':hpnicfDot11APSysUpTime2,'hpnicfDot11APCPURTUsage2':hpnicfDot11APCPURTUsage2,'hpnicfDot11APCPUAvgUsage2':hpnicfDot11APCPUAvgUsage2,'hpnicfDot11APMemRTUsage2':hpnicfDot11APMemRTUsage2,'hpnicfDot11APMemAvgUsage2':hpnicfDot11APMemAvgUsage2,'hpnicfDot11APIPAddressGateway2':hpnicfDot11APIPAddressGateway2,'hpnicfDot11APACAssociateStatus2':hpnicfDot11APACAssociateStatus2,'hpnicfDot11APManuBuildInfo2':hpnicfDot11APManuBuildInfo2,'hpnicfDot11APFlashFreeSize2':hpnicfDot11APFlashFreeSize2,'hpnicfDot11APTemperature2':hpnicfDot11APTemperature2,'hpnicfDot11APMacAddress2':hpnicfDot11APMacAddress2,'hpnicfDot11APACAssociateStatusCM':hpnicfDot11APACAssociateStatusCM,'hpnicfDot11APStatisGroup':hpnicfDot11APStatisGroup,'hpnicfDot11APRxStatisTable':hpnicfDot11APRxStatisTable,'hpnicfDot11APRxStatisEntry':hpnicfDot11APRxStatisEntry,'hpnicfDot11RxFrameDupCnt':hpnicfDot11RxFrameDupCnt,'hpnicfDot11RxFrameCnt':hpnicfDot11RxFrameCnt,'hpnicfDot11RxUcastFrameCnt':hpnicfDot11RxUcastFrameCnt,'hpnicfDot11RxBcastFrameCnt':hpnicfDot11RxBcastFrameCnt,'hpnicfDot11RxMcastFrameCnt':hpnicfDot11RxMcastFrameCnt,'hpnicfDot11RxDiscardFrameCnt':hpnicfDot11RxDiscardFrameCnt,'hpnicfDot11RxFragCnt':hpnicfDot11RxFragCnt,'hpnicfDot11RxFcsErrCnt':hpnicfDot11RxFcsErrCnt,'hpnicfDot11RxFrameBytes':hpnicfDot11RxFrameBytes,'hpnicfDot11RxUcastFrameBytes':hpnicfDot11RxUcastFrameBytes,'hpnicfDot11RxBcastFrameBytes':hpnicfDot11RxBcastFrameBytes,'hpnicfDot11RxMcastFrameBytes':hpnicfDot11RxMcastFrameBytes,'hpnicfDot11RxDiscardFrameBytes':hpnicfDot11RxDiscardFrameBytes,'hpnicfDot11RxMgmtFrameCnt':hpnicfDot11RxMgmtFrameCnt,'hpnicfDot11RxCtrlFrameCnt':hpnicfDot11RxCtrlFrameCnt,'hpnicfDot11RxDataFrameCnt':hpnicfDot11RxDataFrameCnt,'hpnicfDot11RxDecryptErrorCnt':hpnicfDot11RxDecryptErrorCnt,'hpnicfDot11RxAuthenFrameCnt':hpnicfDot11RxAuthenFrameCnt,'hpnicfDot11RxAssociateFrameCnt':hpnicfDot11RxAssociateFrameCnt,'hpnicfDot11RxFrameErrorRatio':hpnicfDot11RxFrameErrorRatio,'hpnicfDot11RxPhyErrorCnt':hpnicfDot11RxPhyErrorCnt,'hpnicfDot11RxMICErrorCnt':hpnicfDot11RxMICErrorCnt,'hpnicfDot11RxDataFrameBytes':hpnicfDot11RxDataFrameBytes,'hpnicfDot11RadioRxAverSnr':hpnicfDot11RadioRxAverSnr,'hpnicfDot11RxPayloadBytes':hpnicfDot11RxPayloadBytes,'hpnicfDot11RxTrafficSpeed':hpnicfDot11RxTrafficSpeed,'hpnicfDot11RxUcastDataFrameCnt':hpnicfDot11RxUcastDataFrameCnt,'hpnicfDot11RxNUcastDataFrameCnt':hpnicfDot11RxNUcastDataFrameCnt,'hpnicfDot11RxTotalDiscardFrameCnt':hpnicfDot11RxTotalDiscardFrameCnt,'hpnicfDot11RxTotalIPCheckErrPacketCnt':hpnicfDot11RxTotalIPCheckErrPacketCnt,'hpnicfDot11RxSignalStrengthPacketCntCM':hpnicfDot11RxSignalStrengthPacketCntCM,'hpnicfDot11RxDataFrameCntCM':hpnicfDot11RxDataFrameCntCM,'hpnicfDot11RxTotalFrameCnt':hpnicfDot11RxTotalFrameCnt,'hpnicfDot11APTxStatisTable':hpnicfDot11APTxStatisTable,'hpnicfDot11APTxStatisEntry':hpnicfDot11APTxStatisEntry,'hpnicfDot11TxFragCnt':hpnicfDot11TxFragCnt,'hpnicfDot11FailedCnt':hpnicfDot11FailedCnt,'hpnicfDot11RetryCnt':hpnicfDot11RetryCnt,'hpnicfDot11MultiRetryCnt':hpnicfDot11MultiRetryCnt,'hpnicfDot11RtsSuccessCnt':hpnicfDot11RtsSuccessCnt,'hpnicfDot11RtsFailCnt':hpnicfDot11RtsFailCnt,'hpnicfDot11AckFailCnt':hpnicfDot11AckFailCnt,'hpnicfDot11TxFrameCnt':hpnicfDot11TxFrameCnt,'hpnicfDot11TxUcastFrameCnt':hpnicfDot11TxUcastFrameCnt,'hpnicfDot11TxBcastFrameCnt':hpnicfDot11TxBcastFrameCnt,'hpnicfDot11TxMcastFrameCnt':hpnicfDot11TxMcastFrameCnt,'hpnicfDot11TxDiscardFrameCnt':hpnicfDot11TxDiscardFrameCnt,'hpnicfDot11TxFrameBytes':hpnicfDot11TxFrameBytes,'hpnicfDot11TxUcastFrameBytes':hpnicfDot11TxUcastFrameBytes,'hpnicfDot11TxBcastFrameBytes':hpnicfDot11TxBcastFrameBytes,'hpnicfDot11TxMcastFrameBytes':hpnicfDot11TxMcastFrameBytes,'hpnicfDot11TxDiscardFrameBytes':hpnicfDot11TxDiscardFrameBytes,'hpnicfDot11TxAuthenFrameCnt':hpnicfDot11TxAuthenFrameCnt,'hpnicfDot11TxAssociateFrameCnt':hpnicfDot11TxAssociateFrameCnt,'hpnicfDot11TxFrameRetryRatio':hpnicfDot11TxFrameRetryRatio,'hpnicfDot11TxDataFrameCnt':hpnicfDot11TxDataFrameCnt,'hpnicfDot11TxDataFrameBytes':hpnicfDot11TxDataFrameBytes,'hpnicfDot11TxMSDUCnt':hpnicfDot11TxMSDUCnt,'hpnicfDot11TxDiscardMSDUCnt':hpnicfDot11TxDiscardMSDUCnt,'hpnicfDot11RetryMSDUCnt':hpnicfDot11RetryMSDUCnt,'hpnicfDot11TxPayloadBytes':hpnicfDot11TxPayloadBytes,'hpnicfDot11TxTrafficSpeed':hpnicfDot11TxTrafficSpeed,'hpnicfDot11TxErrFrameRatio':hpnicfDot11TxErrFrameRatio,'hpnicfDot11TxFrameRate':hpnicfDot11TxFrameRate,'hpnicfDot11TxMgtFrameCnt':hpnicfDot11TxMgtFrameCnt,'hpnicfDot11TxCtrlFrameCnt':hpnicfDot11TxCtrlFrameCnt,'hpnicfDot11TxMACErrCnt':hpnicfDot11TxMACErrCnt,'hpnicfDot11TxErrFrameCnt':hpnicfDot11TxErrFrameCnt,'hpnicfDot11TxUcastDataFrameCnt':hpnicfDot11TxUcastDataFrameCnt,'hpnicfDot11TxNUcastDataFrameCnt':hpnicfDot11TxNUcastDataFrameCnt,'hpnicfDot11TxTotalFrameCnt':hpnicfDot11TxTotalFrameCnt,'hpnicfDot11APAssocStatisTable':hpnicfDot11APAssocStatisTable,'hpnicfDot11APAssocStatisEntry':hpnicfDot11APAssocStatisEntry,'hpnicfDot11ApStationAssocSum':hpnicfDot11ApStationAssocSum,'hpnicfDot11ApStationAssocFailSum':hpnicfDot11ApStationAssocFailSum,'hpnicfDot11ApStationReassocSum':hpnicfDot11ApStationReassocSum,'hpnicfDot11ApStationAssocRejectSum':hpnicfDot11ApStationAssocRejectSum,'hpnicfDot11ApStationExDeAuthenSum':hpnicfDot11ApStationExDeAuthenSum,'hpnicfDot11ApStationCurAssocSum':hpnicfDot11ApStationCurAssocSum,'hpnicfDot11ApStaCurAuthSuccSum':hpnicfDot11ApStaCurAuthSuccSum,'hpnicfDot11AllStationUpSumTime':hpnicfDot11AllStationUpSumTime,'hpnicfDot11ApStationAssocReqSum':hpnicfDot11ApStationAssocReqSum,'hpnicfDot11AllStationUpSumTimeTicks':hpnicfDot11AllStationUpSumTimeTicks,'hpnicfDot11ApStationReassocReqSum':hpnicfDot11ApStationReassocReqSum,'hpnicfDot11ApStationReassocFailSum':hpnicfDot11ApStationReassocFailSum,'hpnicfDot11BSSRxStatisTable':hpnicfDot11BSSRxStatisTable,'hpnicfDot11BSSRxStatisEntry':hpnicfDot11BSSRxStatisEntry,'hpnicfDot11BSSRxFrameCnt':hpnicfDot11BSSRxFrameCnt,'hpnicfDot11BSSRxFrameBytes':hpnicfDot11BSSRxFrameBytes,'hpnicfDot11BSSRxDataFrameCnt':hpnicfDot11BSSRxDataFrameCnt,'hpnicfDot11BSSRxDataFrameBytes':hpnicfDot11BSSRxDataFrameBytes,'hpnicfDot11BSSRxAssociateFrameCnt':hpnicfDot11BSSRxAssociateFrameCnt,'hpnicfDot11BSSRxFrameErrorRatio':hpnicfDot11BSSRxFrameErrorRatio,'hpnicfDot11BSSRxPayloadBytes':hpnicfDot11BSSRxPayloadBytes,'hpnicfDot11BSSRxUniFrameCnt':hpnicfDot11BSSRxUniFrameCnt,'hpnicfDot11BSSRxNonUniFrameCnt':hpnicfDot11BSSRxNonUniFrameCnt,'hpnicfDot11BSSRxAuthenFrameCnt':hpnicfDot11BSSRxAuthenFrameCnt,'hpnicfDot11BSSTxStatisTable':hpnicfDot11BSSTxStatisTable,'hpnicfDot11BSSTxStatisEntry':hpnicfDot11BSSTxStatisEntry,'hpnicfDot11BSSTxFrameCnt':hpnicfDot11BSSTxFrameCnt,'hpnicfDot11BSSTxFrameBytes':hpnicfDot11BSSTxFrameBytes,'hpnicfDot11BSSTxDataFrameCnt':hpnicfDot11BSSTxDataFrameCnt,'hpnicfDot11BSSTxDataFrameBytes':hpnicfDot11BSSTxDataFrameBytes,'hpnicfDot11BSSTxAssociateFrameCnt':hpnicfDot11BSSTxAssociateFrameCnt,'hpnicfDot11BSSTxPayloadBytes':hpnicfDot11BSSTxPayloadBytes,'hpnicfDot11BSSTxRetryCnt':hpnicfDot11BSSTxRetryCnt,'hpnicfDot11BSSTxUniFrameCnt':hpnicfDot11BSSTxUniFrameCnt,'hpnicfDot11BSSTxNonUniFrameCnt':hpnicfDot11BSSTxNonUniFrameCnt,'hpnicfDot11BSSTxAuthenFrameCnt':hpnicfDot11BSSTxAuthenFrameCnt,'hpnicfDot11BSSAssocStatisTable':hpnicfDot11BSSAssocStatisTable,'hpnicfDot11BSSAssocStatisEntry':hpnicfDot11BSSAssocStatisEntry,'hpnicfDot11BSSStationAssocSum':hpnicfDot11BSSStationAssocSum,'hpnicfDot11BSSStationAssocFailSum':hpnicfDot11BSSStationAssocFailSum,'hpnicfDot11BSSStationReassocSum':hpnicfDot11BSSStationReassocSum,'hpnicfDot11BSSStationAssocRejectSum':hpnicfDot11BSSStationAssocRejectSum,'hpnicfDot11BSSStationExDeAssocSum':hpnicfDot11BSSStationExDeAssocSum,'hpnicfDot11BSSStationCurAssocSum':hpnicfDot11BSSStationCurAssocSum,'hpnicfDot11BSSStationAssocReqSum':hpnicfDot11BSSStationAssocReqSum,'hpnicfDot11BSSStationCurAuthSum':hpnicfDot11BSSStationCurAuthSum,'hpnicfDot11APLinkStatisTable':hpnicfDot11APLinkStatisTable,'hpnicfDot11APLinkStatisEntry':hpnicfDot11APLinkStatisEntry,'hpnicfDot11UpLinkUpDownTimes':hpnicfDot11UpLinkUpDownTimes,'hpnicfDot11DownLinkUpDownTimes':hpnicfDot11DownLinkUpDownTimes,'hpnicfDot11PrivateSrvRxFrameBytes':hpnicfDot11PrivateSrvRxFrameBytes,'hpnicfDot11PrivateSrvTxFrameBytes':hpnicfDot11PrivateSrvTxFrameBytes,'hpnicfDot11APInternetAllRxBytes':hpnicfDot11APInternetAllRxBytes,'hpnicfDot11APInternetAllTxBytes':hpnicfDot11APInternetAllTxBytes,'hpnicfDot11APLocalAllRxBytes':hpnicfDot11APLocalAllRxBytes,'hpnicfDot11APLocalAllTxBytes':hpnicfDot11APLocalAllTxBytes,'hpnicfDot11RadioAssocStatisTable':hpnicfDot11RadioAssocStatisTable,'hpnicfDot11RadioAssocStatisEntry':hpnicfDot11RadioAssocStatisEntry,'hpnicfDot11RadioStaAssocSum':hpnicfDot11RadioStaAssocSum,'hpnicfDot11RadioStaAssocFailSum':hpnicfDot11RadioStaAssocFailSum,'hpnicfDot11RadioStaReassocSum':hpnicfDot11RadioStaReassocSum,'hpnicfDot11RadioStaAssocRejectSum':hpnicfDot11RadioStaAssocRejectSum,'hpnicfDot11RadioStaExDeAssocSum':hpnicfDot11RadioStaExDeAssocSum,'hpnicfDot11RadioStaCurAssocSum':hpnicfDot11RadioStaCurAssocSum,'hpnicfDot11RadioMngFrameStatisTable':hpnicfDot11RadioMngFrameStatisTable,'hpnicfDot11RadioMngFrameStatisEntry':hpnicfDot11RadioMngFrameStatisEntry,_A3:hpnicfDot11RadioStatisIndex,_A4:hpnicfDot11MngFrameType,'hpnicfDot11MngFrameCnt':hpnicfDot11MngFrameCnt,'hpnicfDot11APAuthFailStatisTable':hpnicfDot11APAuthFailStatisTable,'hpnicfDot11APAuthFailStatisEntry':hpnicfDot11APAuthFailStatisEntry,_AC:hpnicfDot11APAuthFailStatisType,'hpnicfDot11APAuthFailStatisCnt':hpnicfDot11APAuthFailStatisCnt,'hpnicfDot11APAssocFailStatisTable':hpnicfDot11APAssocFailStatisTable,'hpnicfDot11APAssocFailStatisEntry':hpnicfDot11APAssocFailStatisEntry,_AD:hpnicfDot11APAssocFailStatisType,'hpnicfDot11APAssocFailStatisCnt':hpnicfDot11APAssocFailStatisCnt,'hpnicfDot11APReassocStatisTable':hpnicfDot11APReassocStatisTable,'hpnicfDot11APReassocStatisEntry':hpnicfDot11APReassocStatisEntry,_AE:hpnicfDot11APReassocStatisType,'hpnicfDot11APReassocStatisCnt':hpnicfDot11APReassocStatisCnt,'hpnicfDot11APUserAuthStatisTable':hpnicfDot11APUserAuthStatisTable,'hpnicfDot11APUserAuthStatisEntry':hpnicfDot11APUserAuthStatisEntry,_AF:hpnicfDot11UserAuthStatisType,'hpnicfDot11UserAuthStatisCnt':hpnicfDot11UserAuthStatisCnt,'hpnicfDot11APDeauthStatisTable':hpnicfDot11APDeauthStatisTable,'hpnicfDot11APDeauthStatisEntry':hpnicfDot11APDeauthStatisEntry,_AG:hpnicfDot11APDeauthStatisType,'hpnicfDot11APDeauthStatisCnt':hpnicfDot11APDeauthStatisCnt,'hpnicfDot11APDeassocStatisTable':hpnicfDot11APDeassocStatisTable,'hpnicfDot11APDeassocStatisEntry':hpnicfDot11APDeassocStatisEntry,_AJ:hpnicfDot11APDeassocStatisType,'hpnicfDot11APDeassocStatisCnt':hpnicfDot11APDeassocStatisCnt,'hpnicfDot11APAssocFailStatis2Table':hpnicfDot11APAssocFailStatis2Table,'hpnicfDot11APAssocFailStatis2Entry':hpnicfDot11APAssocFailStatis2Entry,_AK:hpnicfDot11APAssocFailStatis2Type,'hpnicfDot11APAssocFailStatis2Cnt':hpnicfDot11APAssocFailStatis2Cnt,'hpnicfDot11APIfStatisTable':hpnicfDot11APIfStatisTable,'hpnicfDot11APIfStatisEntry':hpnicfDot11APIfStatisEntry,'hpnicfDot11APIfInPkts':hpnicfDot11APIfInPkts,'hpnicfDot11APIfInNormalPkts':hpnicfDot11APIfInNormalPkts,'hpnicfDot11APIfInErrorPkts':hpnicfDot11APIfInErrorPkts,'hpnicfDot11APIfOutPkts':hpnicfDot11APIfOutPkts,'hpnicfDot11APIfInOctets':hpnicfDot11APIfInOctets,'hpnicfDot11APIfOutOctets':hpnicfDot11APIfOutOctets,'hpnicfDot11APIfFlowOut':hpnicfDot11APIfFlowOut,'hpnicfDot11APIfFlowIN':hpnicfDot11APIfFlowIN,'hpnicfDot11APIfInUcastPkts':hpnicfDot11APIfInUcastPkts,'hpnicfDot11APIfInNUcastPkts':hpnicfDot11APIfInNUcastPkts,'hpnicfDot11APIfInDiscardPkts':hpnicfDot11APIfInDiscardPkts,'hpnicfDot11APIfOutUcastPkts':hpnicfDot11APIfOutUcastPkts,'hpnicfDot11APIfOutNUcastPkts':hpnicfDot11APIfOutNUcastPkts,'hpnicfDot11APIfOutDiscardPkts':hpnicfDot11APIfOutDiscardPkts,'hpnicfDot11APIfOutErrorPkts':hpnicfDot11APIfOutErrorPkts,'hpnicfDot11APIfUpdownTimes':hpnicfDot11APIfUpdownTimes,'hpnicfDot11APIfStatusKeepTime':hpnicfDot11APIfStatusKeepTime,'hpnicfDot11APIfOperStatus':hpnicfDot11APIfOperStatus,'hpnicfDot11APIfInBrdcastPkts':hpnicfDot11APIfInBrdcastPkts,'hpnicfDot11APIfOutBrdcastPkts':hpnicfDot11APIfOutBrdcastPkts,'hpnicfDot11APIfInMulcastPkts':hpnicfDot11APIfInMulcastPkts,'hpnicfDot11APIfOutMulcastPkts':hpnicfDot11APIfOutMulcastPkts,'hpnicfDot11APIfInPayloadOctets':hpnicfDot11APIfInPayloadOctets,'hpnicfDot11APIfOutPayloadOctets':hpnicfDot11APIfOutPayloadOctets,'hpnicfDot11RadioMngFrmStatisTable':hpnicfDot11RadioMngFrmStatisTable,'hpnicfDot11RadioMngFrmStatisEntry':hpnicfDot11RadioMngFrmStatisEntry,_AN:hpnicfDot11MngFrmType,'hpnicfDot11MngFrmCnt':hpnicfDot11MngFrmCnt,'hpnicfDot11APPacketSizeStatisTable':hpnicfDot11APPacketSizeStatisTable,'hpnicfDot11APPacketSizeStatisEntry':hpnicfDot11APPacketSizeStatisEntry,_AO:hpnicfDot11APPacketSize,'hpnicfDot11APRXPacketSizeCount':hpnicfDot11APRXPacketSizeCount,'hpnicfDot11APTXPacketSizeCount':hpnicfDot11APTXPacketSizeCount,'hpnicfDot11APPacketRateStatisTable':hpnicfDot11APPacketRateStatisTable,'hpnicfDot11APPacketRateStatisEntry':hpnicfDot11APPacketRateStatisEntry,_AP:hpnicfDot11APPacketRate,'hpnicfDot11APRXPacketRateCount':hpnicfDot11APRXPacketRateCount,'hpnicfDot11APTXPacketRateCount':hpnicfDot11APTXPacketRateCount,'hpnicfDot11APPacketMCSRateStatisTable':hpnicfDot11APPacketMCSRateStatisTable,'hpnicfDot11APPacketMCSRateStatisEntry':hpnicfDot11APPacketMCSRateStatisEntry,_AQ:hpnicfDot11APPacketMCSRate,'hpnicfDot11APRXPacketMCSRateCount':hpnicfDot11APRXPacketMCSRateCount,'hpnicfDot11APTXPacketMCSRateCount':hpnicfDot11APTXPacketMCSRateCount,'hpnicfDot11APAssocFailStatis3Table':hpnicfDot11APAssocFailStatis3Table,'hpnicfDot11APAssocFailStatis3Entry':hpnicfDot11APAssocFailStatis3Entry,'hpnicfDot11APAssocFailStatis3SRCnt':hpnicfDot11APAssocFailStatis3SRCnt,'hpnicfDot11APAssocFailStatis3NSRCnt':hpnicfDot11APAssocFailStatis3NSRCnt,'hpnicfDot11APAssocFailStatis3URCCnt':hpnicfDot11APAssocFailStatis3URCCnt,'hpnicfDot11APAssocFailStatis3RFCnt':hpnicfDot11APAssocFailStatis3RFCnt,'hpnicfDot11APAssocFailStatis3OtherCnt':hpnicfDot11APAssocFailStatis3OtherCnt,'hpnicfDot11APAssocFailStatis3RSSILowCntCM':hpnicfDot11APAssocFailStatis3RSSILowCntCM,'hpnicfDot11APIfStatisByAPIDTable':hpnicfDot11APIfStatisByAPIDTable,'hpnicfDot11APIfStatisByAPIDEntry':hpnicfDot11APIfStatisByAPIDEntry,'hpnicfDot11APIfInPkts2':hpnicfDot11APIfInPkts2,'hpnicfDot11APIfInNormalPkts2':hpnicfDot11APIfInNormalPkts2,'hpnicfDot11APIfInErrorPkts2':hpnicfDot11APIfInErrorPkts2,'hpnicfDot11APIfOutPkts2':hpnicfDot11APIfOutPkts2,'hpnicfDot11APIfInOctets2':hpnicfDot11APIfInOctets2,'hpnicfDot11APIfOutOctets2':hpnicfDot11APIfOutOctets2,'hpnicfDot11APIfFlowOut2':hpnicfDot11APIfFlowOut2,'hpnicfDot11APIfFlowIN2':hpnicfDot11APIfFlowIN2,'hpnicfDot11APIfInUcastPkts2':hpnicfDot11APIfInUcastPkts2,'hpnicfDot11APIfInNUcastPkts2':hpnicfDot11APIfInNUcastPkts2,'hpnicfDot11APIfInDiscardPkts2':hpnicfDot11APIfInDiscardPkts2,'hpnicfDot11APIfOutUcastPkts2':hpnicfDot11APIfOutUcastPkts2,'hpnicfDot11APIfOutNUcastPkts2':hpnicfDot11APIfOutNUcastPkts2,'hpnicfDot11APIfOutDiscardPkts2':hpnicfDot11APIfOutDiscardPkts2,'hpnicfDot11APIfOutErrorPkts2':hpnicfDot11APIfOutErrorPkts2,'hpnicfDot11APIfUpdownTimes2':hpnicfDot11APIfUpdownTimes2,'hpnicfDot11APIfStatusKeepTime2':hpnicfDot11APIfStatusKeepTime2,'hpnicfDot11APIfOperStatus2':hpnicfDot11APIfOperStatus2,'hpnicfDot11APIfInBrdcastPkts2':hpnicfDot11APIfInBrdcastPkts2,'hpnicfDot11APIfOutBrdcastPkts2':hpnicfDot11APIfOutBrdcastPkts2,'hpnicfDot11APIfInMulcastPkts2':hpnicfDot11APIfInMulcastPkts2,'hpnicfDot11APIfOutMulcastPkts2':hpnicfDot11APIfOutMulcastPkts2,'hpnicfDot11APIfInPayloadOctets2':hpnicfDot11APIfInPayloadOctets2,'hpnicfDot11APIfOutPayloadOctets2':hpnicfDot11APIfOutPayloadOctets2,'hpnicfDot11APIfInDataOctets2':hpnicfDot11APIfInDataOctets2,'hpnicfDot11APIfOutDataOctets2':hpnicfDot11APIfOutDataOctets2,'hpnicfDot11APIfAdminStatus':hpnicfDot11APIfAdminStatus,'hpnicfDot11APIfOperStatusCM':hpnicfDot11APIfOperStatusCM,'hpnicfDot11APUserSecAuthStatisTable':hpnicfDot11APUserSecAuthStatisTable,'hpnicfDot11APUserSecAuthStatisEntry':hpnicfDot11APUserSecAuthStatisEntry,'hpnicfDot11APUserAuthCurNumber':hpnicfDot11APUserAuthCurNumber,'hpnicfDot11APUserConnFailCnt':hpnicfDot11APUserConnFailCnt,'hpnicfDot11APUserAuthReqCnt':hpnicfDot11APUserAuthReqCnt,'hpnicfDot11APUserAuthSuccCnt':hpnicfDot11APUserAuthSuccCnt,'hpnicfDot11APUserAuthFailCnt':hpnicfDot11APUserAuthFailCnt,'hpnicfDot11AllUserOnlineTime':hpnicfDot11AllUserOnlineTime,'hpnicfDot11APUserInfoStatisTable':hpnicfDot11APUserInfoStatisTable,'hpnicfDot11APUserInfoStatisEntry':hpnicfDot11APUserInfoStatisEntry,_AR:hpnicfDot11APUserMacAddr,'hpnicfDot11APUserIpAddr':hpnicfDot11APUserIpAddr,'hpnicfDot11APUserLoginName':hpnicfDot11APUserLoginName,'hpnicfDot11APUserLoginTime':hpnicfDot11APUserLoginTime,'hpnicfDot11APUserOnlineTime':hpnicfDot11APUserOnlineTime,'hpnicfDot11APUserLoginNameCM':hpnicfDot11APUserLoginNameCM,'hpnicfDot11APUserAuthTypeCM':hpnicfDot11APUserAuthTypeCM,'hpnicfDot11APUserTxPacketCntCM':hpnicfDot11APUserTxPacketCntCM,'hpnicfDot11APUserTxBytesCM':hpnicfDot11APUserTxBytesCM,'hpnicfDot11APUserRxPacketCntCM':hpnicfDot11APUserRxPacketCntCM,'hpnicfDot11APUserRxBytesCM':hpnicfDot11APUserRxBytesCM,'hpnicfDot11APReassocStatis2Table':hpnicfDot11APReassocStatis2Table,'hpnicfDot11APReassocStatis2Entry':hpnicfDot11APReassocStatis2Entry,'hpnicfDot11APReassocFailStatis2Cnt':hpnicfDot11APReassocFailStatis2Cnt,'hpnicfDot11TrafficTable':hpnicfDot11TrafficTable,'hpnicfDot11TrafficEntry':hpnicfDot11TrafficEntry,_AU:hpnicfDot11SSIDIndex,'hpnicfDot11UpPacketNumber':hpnicfDot11UpPacketNumber,'hpnicfDot11UpByteNumber':hpnicfDot11UpByteNumber,'hpnicfDot11DownPacketNumber':hpnicfDot11DownPacketNumber,'hpnicfDot11DownByteNumber':hpnicfDot11DownByteNumber,'hpnicfDot11APEchoStatisTable':hpnicfDot11APEchoStatisTable,'hpnicfDot11APEchoInfoStatisEntry':hpnicfDot11APEchoInfoStatisEntry,'hpnicfDot11APEchoAvgDelay':hpnicfDot11APEchoAvgDelay,'hpnicfDot11APEchoRequestCnt':hpnicfDot11APEchoRequestCnt,'hpnicfDot11APEchoRespLossCnt':hpnicfDot11APEchoRespLossCnt,'hpnicfDot11APUserSecAuthTypeStatisTable':hpnicfDot11APUserSecAuthTypeStatisTable,'hpnicfDot11APUserSecAuthTypeStatisEntry':hpnicfDot11APUserSecAuthTypeStatisEntry,'hpnicfDot11APPortalOnlineUserNum':hpnicfDot11APPortalOnlineUserNum,'hpnicfDot11APAuthFreeOnlineUserNum':hpnicfDot11APAuthFreeOnlineUserNum,'hpnicfDot11APAssocAuthOnlineUserNum':hpnicfDot11APAssocAuthOnlineUserNum,'hpnicfDot11APMacAuthOnlineUserNum':hpnicfDot11APMacAuthOnlineUserNum,'hpnicfDot11APAllPortalUserOnlineTime':hpnicfDot11APAllPortalUserOnlineTime,'hpnicfDot11APAllAuthFreeUserOnlineTime':hpnicfDot11APAllAuthFreeUserOnlineTime,'hpnicfDot11APAllAssocAuthUserOnlineTime':hpnicfDot11APAllAssocAuthUserOnlineTime,'hpnicfDot11APAllMacAuthUserOnlineTime':hpnicfDot11APAllMacAuthUserOnlineTime,'hpnicfDot11APPortalUserLostCnntCnt':hpnicfDot11APPortalUserLostCnntCnt,'hpnicfDot11APAuthFreeUserLostCnntCnt':hpnicfDot11APAuthFreeUserLostCnntCnt,'hpnicfDot11APAssocAuthUserLostCnntCnt':hpnicfDot11APAssocAuthUserLostCnntCnt,'hpnicfDot11APMacAuthUserLostCnntCnt':hpnicfDot11APMacAuthUserLostCnntCnt,'hpnicfDot11APPortalAuthReqCnt':hpnicfDot11APPortalAuthReqCnt,'hpnicfDot11APAssocAuthReqCnt':hpnicfDot11APAssocAuthReqCnt,'hpnicfDot11APMacAuthReqCnt':hpnicfDot11APMacAuthReqCnt,'hpnicfDot11APPortalAuthSucCnt':hpnicfDot11APPortalAuthSucCnt,'hpnicfDot11APAssocAuthSucCnt':hpnicfDot11APAssocAuthSucCnt,'hpnicfDot11APMacAuthSucCnt':hpnicfDot11APMacAuthSucCnt,'hpnicfDot11APPortalAuthReqFailCnt':hpnicfDot11APPortalAuthReqFailCnt,'hpnicfDot11APAssocAuthReqFailCnt':hpnicfDot11APAssocAuthReqFailCnt,'hpnicfDot11APMacAuthReqFailCnt':hpnicfDot11APMacAuthReqFailCnt,'hpnicfDot11APAutoAuthOnlineUserNumCM':hpnicfDot11APAutoAuthOnlineUserNumCM,'hpnicfDot11APAllAutoAuthUserOnlineTimeCM':hpnicfDot11APAllAutoAuthUserOnlineTimeCM,'hpnicfDot11APAutoAuthUserLostCnntCntCM':hpnicfDot11APAutoAuthUserLostCnntCntCM,'hpnicfDot11APAutoAuthReqCntCM':hpnicfDot11APAutoAuthReqCntCM,'hpnicfDot11APAutoAuthSucCntCM':hpnicfDot11APAutoAuthSucCntCM,'hpnicfDot11APAutoAuthReqFailCntCM':hpnicfDot11APAutoAuthReqFailCntCM,'hpnicfDot11RadioRxStatis64Table':hpnicfDot11RadioRxStatis64Table,'hpnicfDot11RadioRxStatis64Entry':hpnicfDot11RadioRxStatis64Entry,'hpnicfDot11Rx64FrameDupCnt':hpnicfDot11Rx64FrameDupCnt,'hpnicfDot11Rx64FrameCnt':hpnicfDot11Rx64FrameCnt,'hpnicfDot11Rx64UcastFrameCnt':hpnicfDot11Rx64UcastFrameCnt,'hpnicfDot11Rx64BcastFrameCnt':hpnicfDot11Rx64BcastFrameCnt,'hpnicfDot11Rx64McastFrameCnt':hpnicfDot11Rx64McastFrameCnt,'hpnicfDot11Rx64DiscardFrameCnt':hpnicfDot11Rx64DiscardFrameCnt,'hpnicfDot11Rx64FragCnt':hpnicfDot11Rx64FragCnt,'hpnicfDot11Rx64FcsErrCnt':hpnicfDot11Rx64FcsErrCnt,'hpnicfDot11Rx64FrameBytes':hpnicfDot11Rx64FrameBytes,'hpnicfDot11Rx64UcastFrameBytes':hpnicfDot11Rx64UcastFrameBytes,'hpnicfDot11Rx64BcastFrameBytes':hpnicfDot11Rx64BcastFrameBytes,'hpnicfDot11Rx64McastFrameBytes':hpnicfDot11Rx64McastFrameBytes,'hpnicfDot11Rx64DiscardFrameBytes':hpnicfDot11Rx64DiscardFrameBytes,'hpnicfDot11Rx64MgmtFrameCnt':hpnicfDot11Rx64MgmtFrameCnt,'hpnicfDot11Rx64CtrlFrameCnt':hpnicfDot11Rx64CtrlFrameCnt,'hpnicfDot11Rx64DataFrameCnt':hpnicfDot11Rx64DataFrameCnt,'hpnicfDot11Rx64DecryptErrorCnt':hpnicfDot11Rx64DecryptErrorCnt,'hpnicfDot11Rx64AuthenFrameCnt':hpnicfDot11Rx64AuthenFrameCnt,'hpnicfDot11Rx64AssociateFrameCnt':hpnicfDot11Rx64AssociateFrameCnt,'hpnicfDot11Rx64PhyErrorCnt':hpnicfDot11Rx64PhyErrorCnt,'hpnicfDot11Rx64MICErrorCnt':hpnicfDot11Rx64MICErrorCnt,'hpnicfDot11Rx64DataFrameBytes':hpnicfDot11Rx64DataFrameBytes,'hpnicfDot11Rx64PayloadBytes':hpnicfDot11Rx64PayloadBytes,'hpnicfDot11Rx64DataFrameBytesCM':hpnicfDot11Rx64DataFrameBytesCM,'hpnicfDot11RadioTxStatis64Table':hpnicfDot11RadioTxStatis64Table,'hpnicfDot11RadioTxStatis64Entry':hpnicfDot11RadioTxStatis64Entry,'hpnicfDot11Tx64FragCnt':hpnicfDot11Tx64FragCnt,'hpnicfDot11Tx64FailedCnt':hpnicfDot11Tx64FailedCnt,'hpnicfDot11Tx64RetryCnt':hpnicfDot11Tx64RetryCnt,'hpnicfDot11Tx64MultiRetryCnt':hpnicfDot11Tx64MultiRetryCnt,'hpnicfDot11Tx64RtsSuccessCnt':hpnicfDot11Tx64RtsSuccessCnt,'hpnicfDot11Tx64RtsFailCnt':hpnicfDot11Tx64RtsFailCnt,'hpnicfDot11Tx64AckFailCnt':hpnicfDot11Tx64AckFailCnt,'hpnicfDot11Tx64FrameCnt':hpnicfDot11Tx64FrameCnt,'hpnicfDot11Tx64UcastFrameCnt':hpnicfDot11Tx64UcastFrameCnt,'hpnicfDot11Tx64BcastFrameCnt':hpnicfDot11Tx64BcastFrameCnt,'hpnicfDot11Tx64McastFrameCnt':hpnicfDot11Tx64McastFrameCnt,'hpnicfDot11Tx64DiscardFrameCnt':hpnicfDot11Tx64DiscardFrameCnt,'hpnicfDot11Tx64FrameBytes':hpnicfDot11Tx64FrameBytes,'hpnicfDot11Tx64UcastFrameBytes':hpnicfDot11Tx64UcastFrameBytes,'hpnicfDot11Tx64BcastFrameBytes':hpnicfDot11Tx64BcastFrameBytes,'hpnicfDot11Tx64McastFrameBytes':hpnicfDot11Tx64McastFrameBytes,'hpnicfDot11Tx64DiscardFrameBytes':hpnicfDot11Tx64DiscardFrameBytes,'hpnicfDot11Tx64AuthenFrameCnt':hpnicfDot11Tx64AuthenFrameCnt,'hpnicfDot11Tx64AssociateFrameCnt':hpnicfDot11Tx64AssociateFrameCnt,'hpnicfDot11Tx64DataFrameCnt':hpnicfDot11Tx64DataFrameCnt,'hpnicfDot11Tx64DataFrameBytes':hpnicfDot11Tx64DataFrameBytes,'hpnicfDot11Tx64MSDUCnt':hpnicfDot11Tx64MSDUCnt,'hpnicfDot11Tx64DiscardMSDUCnt':hpnicfDot11Tx64DiscardMSDUCnt,'hpnicfDot11Tx64RetryMSDUCnt':hpnicfDot11Tx64RetryMSDUCnt,'hpnicfDot11Tx64PayloadBytes':hpnicfDot11Tx64PayloadBytes,'hpnicfDot11Tx64MgtFrameCnt':hpnicfDot11Tx64MgtFrameCnt,'hpnicfDot11Tx64CtrlFrameCnt':hpnicfDot11Tx64CtrlFrameCnt,'hpnicfDot11Tx64MACErrCnt':hpnicfDot11Tx64MACErrCnt,'hpnicfDot11Tx64ErrFrameCnt':hpnicfDot11Tx64ErrFrameCnt,'hpnicfDot11BSSRxStatis64Table':hpnicfDot11BSSRxStatis64Table,'hpnicfDot11BSSRxStatis64Entry':hpnicfDot11BSSRxStatis64Entry,'hpnicfDot11BSSRx64FrameCnt':hpnicfDot11BSSRx64FrameCnt,'hpnicfDot11BSSRx64FrameBytes':hpnicfDot11BSSRx64FrameBytes,'hpnicfDot11BSSRx64DataFrameCnt':hpnicfDot11BSSRx64DataFrameCnt,'hpnicfDot11BSSRx64DataFrameBytes':hpnicfDot11BSSRx64DataFrameBytes,'hpnicfDot11BSSRx64AssocFrameCnt':hpnicfDot11BSSRx64AssocFrameCnt,'hpnicfDot11BSSRx64PayloadBytes':hpnicfDot11BSSRx64PayloadBytes,'hpnicfDot11BSSRx64UniFrameCnt':hpnicfDot11BSSRx64UniFrameCnt,'hpnicfDot11BSSRx64NonUniFrameCnt':hpnicfDot11BSSRx64NonUniFrameCnt,'hpnicfDot11BSSRx64AuthenFrameCnt':hpnicfDot11BSSRx64AuthenFrameCnt,'hpnicfDot11BSSTxStatis64Table':hpnicfDot11BSSTxStatis64Table,'hpnicfDot11BSSTxStatis64Entry':hpnicfDot11BSSTxStatis64Entry,'hpnicfDot11BSSTx64FrameCnt':hpnicfDot11BSSTx64FrameCnt,'hpnicfDot11BSSTx64FrameBytes':hpnicfDot11BSSTx64FrameBytes,'hpnicfDot11BSSTx64DataFrameCnt':hpnicfDot11BSSTx64DataFrameCnt,'hpnicfDot11BSSTx64DataFrameBytes':hpnicfDot11BSSTx64DataFrameBytes,'hpnicfDot11BSSTx64AssocFrameCnt':hpnicfDot11BSSTx64AssocFrameCnt,'hpnicfDot11BSSTx64PayloadBytes':hpnicfDot11BSSTx64PayloadBytes,'hpnicfDot11BSSTx64RetryCnt':hpnicfDot11BSSTx64RetryCnt,'hpnicfDot11BSSTx64UniFrameCnt':hpnicfDot11BSSTx64UniFrameCnt,'hpnicfDot11BSSTx64NonUniFrameCnt':hpnicfDot11BSSTx64NonUniFrameCnt,'hpnicfDot11BSSTx64AuthenFrameCnt':hpnicfDot11BSSTx64AuthenFrameCnt,'hpnicfDot11APPacketMCSRateStatis2Table':hpnicfDot11APPacketMCSRateStatis2Table,'hpnicfDot11APPacketMCSRateStatis2Entry':hpnicfDot11APPacketMCSRateStatis2Entry,_AV:hpnicfDot11APPacketMCS2Rate,'hpnicfDot11APRXPacketMCSRate2Count':hpnicfDot11APRXPacketMCSRate2Count,'hpnicfDot11APTXPacketMCSRate2Count':hpnicfDot11APTXPacketMCSRate2Count,'hpnicfDot11APUserSecAuthStatisCMTable':hpnicfDot11APUserSecAuthStatisCMTable,'hpnicfDot11APUserSecAuthStatisCMEntry':hpnicfDot11APUserSecAuthStatisCMEntry,'hpnicfDot11APUserConnFailCntCM':hpnicfDot11APUserConnFailCntCM,'hpnicfDot11APUserAuthReqCntCM':hpnicfDot11APUserAuthReqCntCM,'hpnicfDot11APUserAuthSuccCntCM':hpnicfDot11APUserAuthSuccCntCM,'hpnicfDot11APUserAuthFailCntCM':hpnicfDot11APUserAuthFailCntCM,'hpnicfDot11AllUserOnlineTimeCM':hpnicfDot11AllUserOnlineTimeCM,'hpnicfDot11APUserInfoStatis2CMTable':hpnicfDot11APUserInfoStatis2CMTable,'hpnicfDot11APUserInfoStatis2CMEntry':hpnicfDot11APUserInfoStatis2CMEntry,_AW:hpnicfDot11APUserMacAddr2CM,'hpnicfDot11APUserIpAddr2CM':hpnicfDot11APUserIpAddr2CM,'hpnicfDot11APUserLoginName2CM':hpnicfDot11APUserLoginName2CM,'hpnicfDot11APUserLoginTime2CM':hpnicfDot11APUserLoginTime2CM,'hpnicfDot11APUserOnlineTime2CM':hpnicfDot11APUserOnlineTime2CM,'hpnicfDot11APUserAuthType2CM':hpnicfDot11APUserAuthType2CM,'hpnicfDot11APUserTxPacketCnt2CM':hpnicfDot11APUserTxPacketCnt2CM,'hpnicfDot11APUserTxBytes2CM':hpnicfDot11APUserTxBytes2CM,'hpnicfDot11APUserRxPacketCnt2CM':hpnicfDot11APUserRxPacketCnt2CM,'hpnicfDot11APUserRxBytes2CM':hpnicfDot11APUserRxBytes2CM,'hpnicfDot11APMtNotifyGroup':hpnicfDot11APMtNotifyGroup,'hpnicfDot11APMtTraps':hpnicfDot11APMtTraps,'hpnicfDot11APMtWorkModeChgTrap':hpnicfDot11APMtWorkModeChgTrap,'hpnicfDot11APMtCfgErrorTrap':hpnicfDot11APMtCfgErrorTrap,'hpnicfDot11APMtRadioFailTrap':hpnicfDot11APMtRadioFailTrap,'hpnicfDot11APMtRadioFailRecoverTrap':hpnicfDot11APMtRadioFailRecoverTrap,'hpnicfDot11APMtRdoChanlChgTrap':hpnicfDot11APMtRdoChanlChgTrap,'hpnicfDot11APMtTimeSynFail':hpnicfDot11APMtTimeSynFail,'hpnicfDot11APMtChlIntfDetected':hpnicfDot11APMtChlIntfDetected,'hpnicfDot11APMtIntfAPDetected':hpnicfDot11APMtIntfAPDetected,'hpnicfDot11APMtIntfStaDetected':hpnicfDot11APMtIntfStaDetected,'hpnicfDot11APMtIPChange':hpnicfDot11APMtIPChange,'hpnicfDot11APFlashWriteFailure':hpnicfDot11APFlashWriteFailure,'hpnicfDot11APSysReboot':hpnicfDot11APSysReboot,'hpnicfDot11APMtAvailChlTooLow':hpnicfDot11APMtAvailChlTooLow,'hpnicfDot11APImgDwldSuccess':hpnicfDot11APImgDwldSuccess,'hpnicfDot11APInterfDetectedTrap':hpnicfDot11APInterfDetectedTrap,'hpnicfDot11APInterfClearTrap':hpnicfDot11APInterfClearTrap,'hpnicfDot11StaInterfDetectedTrap':hpnicfDot11StaInterfDetectedTrap,'hpnicfDot11StaInterfClearTrap':hpnicfDot11StaInterfClearTrap,'hpnicfDot11OtherDevIntDetectedTrap':hpnicfDot11OtherDevIntDetectedTrap,'hpnicfDot11OtherDevIntClearTrap':hpnicfDot11OtherDevIntClearTrap,'hpnicfDot11APModuleTroubleTrap':hpnicfDot11APModuleTroubleTrap,'hpnicfDot11APModuleTroubleClearTrap':hpnicfDot11APModuleTroubleClearTrap,'hpnicfDot11APRadioDownTrap':hpnicfDot11APRadioDownTrap,'hpnicfDot11APRadioDownRecovTrap':hpnicfDot11APRadioDownRecovTrap,'hpnicfDot11APStaFullTrap':hpnicfDot11APStaFullTrap,'hpnicfDot11APStaFullRecoverTrap':hpnicfDot11APStaFullRecoverTrap,'hpnicfDot11DFSFreeCntBelowThrRecov':hpnicfDot11DFSFreeCntBelowThrRecov,'hpnicfDot11APCpuUsageHigh':hpnicfDot11APCpuUsageHigh,'hpnicfDot11APCpuUsageHighRecover':hpnicfDot11APCpuUsageHighRecover,'hpnicfDot11APMemUsageHigh':hpnicfDot11APMemUsageHigh,'hpnicfDot11APMemUsageHighRecover':hpnicfDot11APMemUsageHighRecover,'hpnicfDot11APTrapUserCntExceedThre':hpnicfDot11APTrapUserCntExceedThre,'hpnicfDot11APMtDetectedIntfAP':hpnicfDot11APMtDetectedIntfAP,'hpnicfDot11APMtDetectedIntfSTA':hpnicfDot11APMtDetectedIntfSTA,'hpnicfDot11APMtDetectedIntfOtherDev':hpnicfDot11APMtDetectedIntfOtherDev,'hpnicfDot11DetcAdjChlIntfAP':hpnicfDot11DetcAdjChlIntfAP,'hpnicfDot11DetcAdjChlIntfAPClear':hpnicfDot11DetcAdjChlIntfAPClear,'hpnicfDot11APPowerOffTrap':hpnicfDot11APPowerOffTrap,'hpnicfDot11APPowerOnTrap':hpnicfDot11APPowerOnTrap,'hpnicfDot11UpLinkSwitchTrap':hpnicfDot11UpLinkSwitchTrap,'hpnicfDot11APMtTrapVarObjects':hpnicfDot11APMtTrapVarObjects,_AY:hpnicfDot11APMtTrapCfgErrReason,_AZ:hpnicfDot11APMtTrapRadioFailReason,_Ab:hpnicfDot11APMtTrapOldChannel,_Ac:hpnicfDot11APMtTrapNewChannel,_Aa:hpnicfDot11APChannelChgMode,_AX:hpnicfDot11APChgWorkMode,_n:hpnicfDot11APIntfDevMACAddress,_Af:hpnicfDot11APMtTrapOldIPAddr,_o:hpnicfDot11CurrInterfDetectedNum,_r:hpnicfDot11StaFullReason,_q:hpnicfDot11StaLimitNumber,_Ak:hpnicfDot11APRadioDownReason,_p:hpnicfDot11InterfMacList,_Al:hpnicfDot11APTrapUserCnt,_Am:hpnicfDot11APTrapUserThreshold,_Ad:hpnicfDot11APMtChanlChgCount,_Ag:hpnicfDot11APMtFormerApVersion,_J:hpnicfDot11APMtAPID,_O:hpnicfDot11APMtRadioID,_U:hpnicfDot11APMtChannel,_R:hpnicfDot11APMtInterfMacAdd,_u:hpnicfDot11APMtAdjChannel,_K:hpnicfDot11APMtFirstTrapTime,_I:hpnicfDot11APMtTrapAPMacAddress,_An:hpnicfDot11APMtUpLinkSwitchInfo,_Ao:hpnicfDot11APMtUpLinkSwitchTime,_Ap:hpnicfDot11APMtOldCellId,_Aq:hpnicfDot11APMtCurCellId,_Ar:hpnicfDot11APMtOldBand,_As:hpnicfDot11APMtActiveBand})