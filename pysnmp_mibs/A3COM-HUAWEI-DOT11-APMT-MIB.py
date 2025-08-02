_Ad='h3cDot11APTrapUserThreshold'
_Ac='h3cDot11APTrapUserCnt'
_Ab='h3cDot11APRadioDownReason'
_Aa='h3cDot11CurrAPSoftwareVersion'
_AZ='h3cDot11CurrAPIPAddress'
_AY='h3cDot11CurrAPName'
_AX='h3cDot11APMtFormerApVersion'
_AW='h3cDot11APMtTrapOldIPAddr'
_AV='h3cDot11APIPAddress'
_AU='h3cDot11APMtChanlChgCount'
_AT='h3cDot11APMtTrapNewChannel'
_AS='h3cDot11APMtTrapOldChannel'
_AR='h3cDot11APChannelChgMode'
_AQ='h3cDot11APMtTrapRadioFailReason'
_AP='h3cDot11APMtTrapCfgErrReason'
_AO='h3cDot11APChgWorkMode'
_AN='h3cDot11SSIDIndex'
_AM='h3cDot11APUserMacAddr'
_AL='h3cDot11APPacketMCSRate'
_AK='h3cDot11APPacketRate'
_AJ='h3cDot11APPacketSize'
_AI='h3cDot11MngFrmType'
_AH='lowerLayerDown'
_AG='notPresent'
_AF='h3cDot11APAssocFailStatis2Type'
_AE='h3cDot11APDeassocStatisType'
_AD='exception'
_AC='stationLeaving'
_AB='h3cDot11APDeauthStatisType'
_AA='h3cDot11UserAuthStatisType'
_A9='h3cDot11APReassocStatisType'
_A8='h3cDot11APAssocFailStatisType'
_A7='h3cDot11APAuthFailStatisType'
_A6='deauthentication'
_A5='authentication'
_A4='disassociation'
_A3='probeResp'
_A2='reassocResp'
_A1='reassocReq'
_A0='assocResp'
_z='h3cDot11MngFrameType'
_y='h3cDot11RadioStatisIndex'
_x='byte/s'
_w='h3cDot11APIdleTemplateName'
_v='downloadingImage'
_u='deassociated'
_t='associated'
_s='h3cDot11APConfigSPID'
_r='h3cDot11APModelAlias'
_q='read-write'
_p='config'
_o='H3cDot11MACModeType'
_n='h3cDot11APMtAdjChannel'
_m='h3cDot11APMemRTUsage'
_l='h3cDot11APCPURTUsage'
_k='h3cDot11StaFullReason'
_j='h3cDot11StaLimitNumber'
_i='h3cDot11InterfMacList'
_h='h3cDot11CurrInterfDetectedNum'
_g='h3cDot11APIntfDevMACAddress'
_f='unknown'
_e='shortResource'
_d='dBm'
_c='kbytes'
_b='h3cDot11APElementIndex'
_a='A3COM-HUAWEI-DOT11-REF-MIB'
_Z='total'
_Y='rejected'
_X='overtime'
_W='invalidation'
_V='h3cDot11APIfIndex'
_U='h3cDot11APObjID'
_T='h3cDot11WlanID'
_S='OctetString'
_R='h3cDot11APMtChannel'
_Q='bytes'
_P='h3cDot11APMtInterfMacAdd'
_O='other'
_N='h3cDot11APMtRadioID'
_M='h3cDot11Channel'
_L='onepercent'
_K='h3cDot11APMtAPID'
_J='h3cDot11APID'
_I='h3cDot11APMtFirstTrapTime'
_H='not-accessible'
_G='h3cDot11RadioID'
_F='accessible-for-notify'
_E='h3cDot11CurAPID'
_D='Integer32'
_C='A3COM-HUAWEI-DOT11-APMT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
H3cDot11ChannelScopeType,H3cDot11MACModeType,H3cDot11NotifyReasonType,H3cDot11ObjectIDType,H3cDot11RFModeType,H3cDot11RadioElementIndex,H3cDot11RadioScopeType,H3cDot11SSIDStringType,H3cDot11ServicePolicyIDType,H3cDot11TxPwrLevelScopeType,h3cDot11,h3cDot11APElementIndex=mibBuilder.importSymbols(_a,'H3cDot11ChannelScopeType',_o,'H3cDot11NotifyReasonType','H3cDot11ObjectIDType','H3cDot11RFModeType','H3cDot11RadioElementIndex','H3cDot11RadioScopeType','H3cDot11SSIDStringType','H3cDot11ServicePolicyIDType','H3cDot11TxPwrLevelScopeType','h3cDot11',_b)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
h3cDot11APMT=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,75,2))
if mibBuilder.loadTexts:h3cDot11APMT.setRevisions(('2010-10-11 18:00','2010-09-15 12:00','2009-08-07 18:00','2009-07-29 18:00','2009-05-07 20:00','2008-11-07 10:00','2008-07-09 18:00','2008-02-25 18:00','2007-12-21 18:00','2007-06-19 18:00','2007-04-27 20:00','2007-02-01 20:00','2006-05-10 19:00'))
_H3cDot11APObjectGroup_ObjectIdentity=ObjectIdentity
h3cDot11APObjectGroup=_H3cDot11APObjectGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,2,1))
_H3cDot11APObjectStatusTable_Object=MibTable
h3cDot11APObjectStatusTable=_H3cDot11APObjectStatusTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,1))
if mibBuilder.loadTexts:h3cDot11APObjectStatusTable.setStatus(_A)
_H3cDot11APObjectStatusEntry_Object=MibTableRow
h3cDot11APObjectStatusEntry=_H3cDot11APObjectStatusEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,1,1))
h3cDot11APObjectStatusEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:h3cDot11APObjectStatusEntry.setStatus(_A)
_H3cDot11APID_Type=H3cDot11ObjectIDType
_H3cDot11APID_Object=MibTableColumn
h3cDot11APID=_H3cDot11APID_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,1,1,1),_H3cDot11APID_Type())
h3cDot11APID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APID.setStatus(_A)
_H3cDot11APIPAddress_Type=IpAddress
_H3cDot11APIPAddress_Object=MibTableColumn
h3cDot11APIPAddress=_H3cDot11APIPAddress_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,1,1,2),_H3cDot11APIPAddress_Type())
h3cDot11APIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIPAddress.setStatus(_A)
_H3cDot11APMacAddress_Type=MacAddress
_H3cDot11APMacAddress_Object=MibTableColumn
h3cDot11APMacAddress=_H3cDot11APMacAddress_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,1,1,3),_H3cDot11APMacAddress_Type())
h3cDot11APMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APMacAddress.setStatus(_A)
class _H3cDot11APOperationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('join',1),('joinConfirm',2),('download',3),(_p,4),('run',5)))
_H3cDot11APOperationStatus_Type.__name__=_D
_H3cDot11APOperationStatus_Object=MibTableColumn
h3cDot11APOperationStatus=_H3cDot11APOperationStatus_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,1,1,4),_H3cDot11APOperationStatus_Type())
h3cDot11APOperationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APOperationStatus.setStatus(_A)
_H3cDot11APTemplateNameOfAP_Type=OctetString
_H3cDot11APTemplateNameOfAP_Object=MibTableColumn
h3cDot11APTemplateNameOfAP=_H3cDot11APTemplateNameOfAP_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,1,1,5),_H3cDot11APTemplateNameOfAP_Type())
h3cDot11APTemplateNameOfAP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APTemplateNameOfAP.setStatus(_A)
_H3cDot11APReset_Type=TruthValue
_H3cDot11APReset_Object=MibTableColumn
h3cDot11APReset=_H3cDot11APReset_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,1,1,6),_H3cDot11APReset_Type())
h3cDot11APReset.setMaxAccess(_q)
if mibBuilder.loadTexts:h3cDot11APReset.setStatus(_A)
class _H3cDot11APCpuUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11APCpuUsage_Type.__name__=_D
_H3cDot11APCpuUsage_Object=MibTableColumn
h3cDot11APCpuUsage=_H3cDot11APCpuUsage_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,1,1,7),_H3cDot11APCpuUsage_Type())
h3cDot11APCpuUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APCpuUsage.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APCpuUsage.setUnits(_L)
class _H3cDot11APConnectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),('notAvailable',3)))
_H3cDot11APConnectionType_Type.__name__=_D
_H3cDot11APConnectionType_Object=MibTableColumn
h3cDot11APConnectionType=_H3cDot11APConnectionType_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,1,1,8),_H3cDot11APConnectionType_Type())
h3cDot11APConnectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APConnectionType.setStatus(_A)
_H3cDot11APLastImgDownloadTime_Type=DateAndTime
_H3cDot11APLastImgDownloadTime_Object=MibTableColumn
h3cDot11APLastImgDownloadTime=_H3cDot11APLastImgDownloadTime_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,1,1,9),_H3cDot11APLastImgDownloadTime_Type())
h3cDot11APLastImgDownloadTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APLastImgDownloadTime.setStatus(_A)
_H3cDot11APIPv6Address_Type=OctetString
_H3cDot11APIPv6Address_Object=MibTableColumn
h3cDot11APIPv6Address=_H3cDot11APIPv6Address_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,1,1,10),_H3cDot11APIPv6Address_Type())
h3cDot11APIPv6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIPv6Address.setStatus(_A)
_H3cDot11APLastRegisterTime_Type=DateAndTime
_H3cDot11APLastRegisterTime_Object=MibTableColumn
h3cDot11APLastRegisterTime=_H3cDot11APLastRegisterTime_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,1,1,11),_H3cDot11APLastRegisterTime_Type())
h3cDot11APLastRegisterTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APLastRegisterTime.setStatus(_A)
_H3cDot11APObjectTable_Object=MibTable
h3cDot11APObjectTable=_H3cDot11APObjectTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2))
if mibBuilder.loadTexts:h3cDot11APObjectTable.setStatus(_A)
_H3cDot11APObjectEntry_Object=MibTableRow
h3cDot11APObjectEntry=_H3cDot11APObjectEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1))
h3cDot11APObjectEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:h3cDot11APObjectEntry.setStatus(_A)
_H3cDot11APObjID_Type=H3cDot11ObjectIDType
_H3cDot11APObjID_Object=MibTableColumn
h3cDot11APObjID=_H3cDot11APObjID_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,1),_H3cDot11APObjID_Type())
h3cDot11APObjID.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11APObjID.setStatus(_A)
_H3cDot11CurrAPIPAddress_Type=IpAddress
_H3cDot11CurrAPIPAddress_Object=MibTableColumn
h3cDot11CurrAPIPAddress=_H3cDot11CurrAPIPAddress_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,2),_H3cDot11CurrAPIPAddress_Type())
h3cDot11CurrAPIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPIPAddress.setStatus(_A)
_H3cDot11CurrAPMacAddress_Type=MacAddress
_H3cDot11CurrAPMacAddress_Object=MibTableColumn
h3cDot11CurrAPMacAddress=_H3cDot11CurrAPMacAddress_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,3),_H3cDot11CurrAPMacAddress_Type())
h3cDot11CurrAPMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPMacAddress.setStatus(_A)
_H3cDot11CurrACPortIndex_Type=Integer32
_H3cDot11CurrACPortIndex_Object=MibTableColumn
h3cDot11CurrACPortIndex=_H3cDot11CurrACPortIndex_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,4),_H3cDot11CurrACPortIndex_Type())
h3cDot11CurrACPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrACPortIndex.setStatus(_A)
_H3cDot11CurrAPMACMode_Type=H3cDot11MACModeType
_H3cDot11CurrAPMACMode_Object=MibTableColumn
h3cDot11CurrAPMACMode=_H3cDot11CurrAPMACMode_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,5),_H3cDot11CurrAPMACMode_Type())
h3cDot11CurrAPMACMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPMACMode.setStatus(_A)
_H3cDot11CurrAPTemplateName_Type=OctetString
_H3cDot11CurrAPTemplateName_Object=MibTableColumn
h3cDot11CurrAPTemplateName=_H3cDot11CurrAPTemplateName_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,6),_H3cDot11CurrAPTemplateName_Type())
h3cDot11CurrAPTemplateName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPTemplateName.setStatus(_A)
_H3cDot11CurrAPStationAssocCount_Type=Integer32
_H3cDot11CurrAPStationAssocCount_Object=MibTableColumn
h3cDot11CurrAPStationAssocCount=_H3cDot11CurrAPStationAssocCount_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,7),_H3cDot11CurrAPStationAssocCount_Type())
h3cDot11CurrAPStationAssocCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPStationAssocCount.setStatus(_A)
_H3cDot11CurrAPName_Type=OctetString
_H3cDot11CurrAPName_Object=MibTableColumn
h3cDot11CurrAPName=_H3cDot11CurrAPName_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,8),_H3cDot11CurrAPName_Type())
h3cDot11CurrAPName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPName.setStatus(_A)
_H3cDot11CurrAPModelName_Type=OctetString
_H3cDot11CurrAPModelName_Object=MibTableColumn
h3cDot11CurrAPModelName=_H3cDot11CurrAPModelName_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,9),_H3cDot11CurrAPModelName_Type())
h3cDot11CurrAPModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPModelName.setStatus(_A)
_H3cDot11CurrAPImageName_Type=OctetString
_H3cDot11CurrAPImageName_Object=MibTableColumn
h3cDot11CurrAPImageName=_H3cDot11CurrAPImageName_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,10),_H3cDot11CurrAPImageName_Type())
h3cDot11CurrAPImageName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPImageName.setStatus(_A)
_H3cDot11CurrAPSoftwareVersion_Type=OctetString
_H3cDot11CurrAPSoftwareVersion_Object=MibTableColumn
h3cDot11CurrAPSoftwareVersion=_H3cDot11CurrAPSoftwareVersion_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,11),_H3cDot11CurrAPSoftwareVersion_Type())
h3cDot11CurrAPSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPSoftwareVersion.setStatus(_A)
_H3cDot11CurrAPIPNetMask_Type=IpAddress
_H3cDot11CurrAPIPNetMask_Object=MibTableColumn
h3cDot11CurrAPIPNetMask=_H3cDot11CurrAPIPNetMask_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,12),_H3cDot11CurrAPIPNetMask_Type())
h3cDot11CurrAPIPNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPIPNetMask.setStatus(_A)
_H3cDot11CurrRadioModeSupport_Type=Integer32
_H3cDot11CurrRadioModeSupport_Object=MibTableColumn
h3cDot11CurrRadioModeSupport=_H3cDot11CurrRadioModeSupport_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,13),_H3cDot11CurrRadioModeSupport_Type())
h3cDot11CurrRadioModeSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrRadioModeSupport.setStatus(_A)
_H3cDot11CurrIfNumber_Type=Integer32
_H3cDot11CurrIfNumber_Object=MibTableColumn
h3cDot11CurrIfNumber=_H3cDot11CurrIfNumber_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,14),_H3cDot11CurrIfNumber_Type())
h3cDot11CurrIfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrIfNumber.setStatus(_A)
_H3cDot11CurrAPElementID_Type=Integer32
_H3cDot11CurrAPElementID_Object=MibTableColumn
h3cDot11CurrAPElementID=_H3cDot11CurrAPElementID_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,15),_H3cDot11CurrAPElementID_Type())
h3cDot11CurrAPElementID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPElementID.setStatus(_A)
class _H3cDot11CurrAPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bridge',1),('route',2)))
_H3cDot11CurrAPMode_Type.__name__=_D
_H3cDot11CurrAPMode_Object=MibTableColumn
h3cDot11CurrAPMode=_H3cDot11CurrAPMode_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,16),_H3cDot11CurrAPMode_Type())
h3cDot11CurrAPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPMode.setStatus(_A)
_H3cDot11CurrAPIPv6Address_Type=OctetString
_H3cDot11CurrAPIPv6Address_Object=MibTableColumn
h3cDot11CurrAPIPv6Address=_H3cDot11CurrAPIPv6Address_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,17),_H3cDot11CurrAPIPv6Address_Type())
h3cDot11CurrAPIPv6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPIPv6Address.setStatus(_A)
_H3cDot11CurrAPSSIDNumber_Type=Integer32
_H3cDot11CurrAPSSIDNumber_Object=MibTableColumn
h3cDot11CurrAPSSIDNumber=_H3cDot11CurrAPSSIDNumber_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,18),_H3cDot11CurrAPSSIDNumber_Type())
h3cDot11CurrAPSSIDNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPSSIDNumber.setStatus(_A)
_H3cDot11CurrAPManufacturer_Type=OctetString
_H3cDot11CurrAPManufacturer_Object=MibTableColumn
h3cDot11CurrAPManufacturer=_H3cDot11CurrAPManufacturer_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,19),_H3cDot11CurrAPManufacturer_Type())
h3cDot11CurrAPManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPManufacturer.setStatus(_A)
_H3cDot11CurrAPMemorySize_Type=Integer32
_H3cDot11CurrAPMemorySize_Object=MibTableColumn
h3cDot11CurrAPMemorySize=_H3cDot11CurrAPMemorySize_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,20),_H3cDot11CurrAPMemorySize_Type())
h3cDot11CurrAPMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPMemorySize.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11CurrAPMemorySize.setUnits(_c)
_H3cDot11CurrAPMemSizeInBytes_Type=Integer32
_H3cDot11CurrAPMemSizeInBytes_Object=MibTableColumn
h3cDot11CurrAPMemSizeInBytes=_H3cDot11CurrAPMemSizeInBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,21),_H3cDot11CurrAPMemSizeInBytes_Type())
h3cDot11CurrAPMemSizeInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPMemSizeInBytes.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11CurrAPMemSizeInBytes.setUnits(_Q)
_H3cDot11CurrAPFlashSize_Type=Integer32
_H3cDot11CurrAPFlashSize_Object=MibTableColumn
h3cDot11CurrAPFlashSize=_H3cDot11CurrAPFlashSize_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,22),_H3cDot11CurrAPFlashSize_Type())
h3cDot11CurrAPFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPFlashSize.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11CurrAPFlashSize.setUnits('Kbytes')
_H3cDot11CurrAPFlashSizeInBytes_Type=Integer32
_H3cDot11CurrAPFlashSizeInBytes_Object=MibTableColumn
h3cDot11CurrAPFlashSizeInBytes=_H3cDot11CurrAPFlashSizeInBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,23),_H3cDot11CurrAPFlashSizeInBytes_Type())
h3cDot11CurrAPFlashSizeInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPFlashSizeInBytes.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11CurrAPFlashSizeInBytes.setUnits(_Q)
_H3cDot11CurrAPReleasedVersion_Type=OctetString
_H3cDot11CurrAPReleasedVersion_Object=MibTableColumn
h3cDot11CurrAPReleasedVersion=_H3cDot11CurrAPReleasedVersion_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,24),_H3cDot11CurrAPReleasedVersion_Type())
h3cDot11CurrAPReleasedVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrAPReleasedVersion.setStatus(_A)
_H3cDot11CurrRadioModeSupport2_Type=Integer32
_H3cDot11CurrRadioModeSupport2_Object=MibTableColumn
h3cDot11CurrRadioModeSupport2=_H3cDot11CurrRadioModeSupport2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,2,1,25),_H3cDot11CurrRadioModeSupport2_Type())
h3cDot11CurrRadioModeSupport2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrRadioModeSupport2.setStatus(_A)
_H3cDot11APRadioTable_Object=MibTable
h3cDot11APRadioTable=_H3cDot11APRadioTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3))
if mibBuilder.loadTexts:h3cDot11APRadioTable.setStatus(_A)
_H3cDot11APRadioEntry_Object=MibTableRow
h3cDot11APRadioEntry=_H3cDot11APRadioEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1))
h3cDot11APRadioEntry.setIndexNames((0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:h3cDot11APRadioEntry.setStatus(_A)
_H3cDot11CurAPID_Type=H3cDot11ObjectIDType
_H3cDot11CurAPID_Object=MibTableColumn
h3cDot11CurAPID=_H3cDot11CurAPID_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,1),_H3cDot11CurAPID_Type())
h3cDot11CurAPID.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11CurAPID.setStatus(_A)
_H3cDot11RadioID_Type=H3cDot11RadioScopeType
_H3cDot11RadioID_Object=MibTableColumn
h3cDot11RadioID=_H3cDot11RadioID_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,2),_H3cDot11RadioID_Type())
h3cDot11RadioID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11RadioID.setStatus(_A)
_H3cDot11AdminStatus_Type=TruthValue
_H3cDot11AdminStatus_Object=MibTableColumn
h3cDot11AdminStatus=_H3cDot11AdminStatus_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,3),_H3cDot11AdminStatus_Type())
h3cDot11AdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AdminStatus.setStatus(_A)
_H3cDot11OperStatus_Type=TruthValue
_H3cDot11OperStatus_Object=MibTableColumn
h3cDot11OperStatus=_H3cDot11OperStatus_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,4),_H3cDot11OperStatus_Type())
h3cDot11OperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11OperStatus.setStatus(_A)
_H3cDot11Channel_Type=H3cDot11ChannelScopeType
_H3cDot11Channel_Object=MibTableColumn
h3cDot11Channel=_H3cDot11Channel_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,5),_H3cDot11Channel_Type())
h3cDot11Channel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11Channel.setStatus(_A)
_H3cDot11TxPowerLevel_Type=H3cDot11TxPwrLevelScopeType
_H3cDot11TxPowerLevel_Object=MibTableColumn
h3cDot11TxPowerLevel=_H3cDot11TxPowerLevel_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,6),_H3cDot11TxPowerLevel_Type())
h3cDot11TxPowerLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxPowerLevel.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11TxPowerLevel.setUnits('dbm')
_H3cDot11APRadioIfIndex_Type=Integer32
_H3cDot11APRadioIfIndex_Object=MibTableColumn
h3cDot11APRadioIfIndex=_H3cDot11APRadioIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,7),_H3cDot11APRadioIfIndex_Type())
h3cDot11APRadioIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APRadioIfIndex.setStatus(_A)
_H3cDot11AntennaGain_Type=Integer32
_H3cDot11AntennaGain_Object=MibTableColumn
h3cDot11AntennaGain=_H3cDot11AntennaGain_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,8),_H3cDot11AntennaGain_Type())
h3cDot11AntennaGain.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AntennaGain.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11AntennaGain.setUnits('dBi')
_H3cDot11MaxBandwidth_Type=Integer32
_H3cDot11MaxBandwidth_Object=MibTableColumn
h3cDot11MaxBandwidth=_H3cDot11MaxBandwidth_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,9),_H3cDot11MaxBandwidth_Type())
h3cDot11MaxBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MaxBandwidth.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11MaxBandwidth.setUnits('Mbps')
_H3cDot11ResourceUseRatio_Type=Integer32
_H3cDot11ResourceUseRatio_Object=MibTableColumn
h3cDot11ResourceUseRatio=_H3cDot11ResourceUseRatio_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,10),_H3cDot11ResourceUseRatio_Type())
h3cDot11ResourceUseRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ResourceUseRatio.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11ResourceUseRatio.setUnits(_L)
_H3cDot11RadioModeSupport_Type=Unsigned32
_H3cDot11RadioModeSupport_Object=MibTableColumn
h3cDot11RadioModeSupport=_H3cDot11RadioModeSupport_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,11),_H3cDot11RadioModeSupport_Type())
h3cDot11RadioModeSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioModeSupport.setStatus(_A)
class _H3cDot11TxPowerLevel2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_H3cDot11TxPowerLevel2_Type.__name__=_D
_H3cDot11TxPowerLevel2_Object=MibTableColumn
h3cDot11TxPowerLevel2=_H3cDot11TxPowerLevel2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,12),_H3cDot11TxPowerLevel2_Type())
h3cDot11TxPowerLevel2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxPowerLevel2.setStatus(_A)
_H3cDot11PowerMgmtStatus_Type=TruthValue
_H3cDot11PowerMgmtStatus_Object=MibTableColumn
h3cDot11PowerMgmtStatus=_H3cDot11PowerMgmtStatus_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,13),_H3cDot11PowerMgmtStatus_Type())
h3cDot11PowerMgmtStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11PowerMgmtStatus.setStatus(_A)
_H3cDot11ChannelSwitchTimes_Type=Counter32
_H3cDot11ChannelSwitchTimes_Object=MibTableColumn
h3cDot11ChannelSwitchTimes=_H3cDot11ChannelSwitchTimes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,14),_H3cDot11ChannelSwitchTimes_Type())
h3cDot11ChannelSwitchTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ChannelSwitchTimes.setStatus(_A)
_H3cDot11AntennaType_Type=OctetString
_H3cDot11AntennaType_Object=MibTableColumn
h3cDot11AntennaType=_H3cDot11AntennaType_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,15),_H3cDot11AntennaType_Type())
h3cDot11AntennaType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AntennaType.setStatus(_A)
_H3cDot11DiversitySelectionRx_Type=TruthValue
_H3cDot11DiversitySelectionRx_Object=MibTableColumn
h3cDot11DiversitySelectionRx=_H3cDot11DiversitySelectionRx_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,16),_H3cDot11DiversitySelectionRx_Type())
h3cDot11DiversitySelectionRx.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DiversitySelectionRx.setStatus(_A)
_H3cDot11MaxTxPwrLvl_Type=OctetString
_H3cDot11MaxTxPwrLvl_Object=MibTableColumn
h3cDot11MaxTxPwrLvl=_H3cDot11MaxTxPwrLvl_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,17),_H3cDot11MaxTxPwrLvl_Type())
h3cDot11MaxTxPwrLvl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MaxTxPwrLvl.setStatus(_A)
_H3cDot11PwrAttRange_Type=Integer32
_H3cDot11PwrAttRange_Object=MibTableColumn
h3cDot11PwrAttRange=_H3cDot11PwrAttRange_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,18),_H3cDot11PwrAttRange_Type())
h3cDot11PwrAttRange.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11PwrAttRange.setStatus(_A)
_H3cDot11AvgRxSignalStrength_Type=Integer32
_H3cDot11AvgRxSignalStrength_Object=MibTableColumn
h3cDot11AvgRxSignalStrength=_H3cDot11AvgRxSignalStrength_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,19),_H3cDot11AvgRxSignalStrength_Type())
h3cDot11AvgRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AvgRxSignalStrength.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11AvgRxSignalStrength.setUnits(_d)
_H3cDot11HighestRxSignalStrength_Type=Integer32
_H3cDot11HighestRxSignalStrength_Object=MibTableColumn
h3cDot11HighestRxSignalStrength=_H3cDot11HighestRxSignalStrength_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,20),_H3cDot11HighestRxSignalStrength_Type())
h3cDot11HighestRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11HighestRxSignalStrength.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11HighestRxSignalStrength.setUnits(_d)
_H3cDot11LowestRxSignalStrength_Type=Integer32
_H3cDot11LowestRxSignalStrength_Object=MibTableColumn
h3cDot11LowestRxSignalStrength=_H3cDot11LowestRxSignalStrength_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,21),_H3cDot11LowestRxSignalStrength_Type())
h3cDot11LowestRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LowestRxSignalStrength.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11LowestRxSignalStrength.setUnits(_d)
_H3cDot11RadioIfUpdownTimes_Type=Counter32
_H3cDot11RadioIfUpdownTimes_Object=MibTableColumn
h3cDot11RadioIfUpdownTimes=_H3cDot11RadioIfUpdownTimes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,22),_H3cDot11RadioIfUpdownTimes_Type())
h3cDot11RadioIfUpdownTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioIfUpdownTimes.setStatus(_A)
_H3cDot11RadioIfLastChange_Type=TimeTicks
_H3cDot11RadioIfLastChange_Object=MibTableColumn
h3cDot11RadioIfLastChange=_H3cDot11RadioIfLastChange_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,23),_H3cDot11RadioIfLastChange_Type())
h3cDot11RadioIfLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioIfLastChange.setStatus(_A)
_H3cDot11RadioModeSupport2_Type=Unsigned32
_H3cDot11RadioModeSupport2_Object=MibTableColumn
h3cDot11RadioModeSupport2=_H3cDot11RadioModeSupport2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,3,1,24),_H3cDot11RadioModeSupport2_Type())
h3cDot11RadioModeSupport2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioModeSupport2.setStatus(_A)
_H3cDot11APBSSTable_Object=MibTable
h3cDot11APBSSTable=_H3cDot11APBSSTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,4))
if mibBuilder.loadTexts:h3cDot11APBSSTable.setStatus(_A)
_H3cDot11APBSSEntry_Object=MibTableRow
h3cDot11APBSSEntry=_H3cDot11APBSSEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,4,1))
h3cDot11APBSSEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_T))
if mibBuilder.loadTexts:h3cDot11APBSSEntry.setStatus(_A)
_H3cDot11WlanID_Type=Integer32
_H3cDot11WlanID_Object=MibTableColumn
h3cDot11WlanID=_H3cDot11WlanID_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,4,1,1),_H3cDot11WlanID_Type())
h3cDot11WlanID.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11WlanID.setStatus(_A)
_H3cDot11BSSID_Type=MacAddress
_H3cDot11BSSID_Object=MibTableColumn
h3cDot11BSSID=_H3cDot11BSSID_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,4,1,2),_H3cDot11BSSID_Type())
h3cDot11BSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSID.setStatus(_A)
_H3cDot11CurrSvcPolicyID_Type=H3cDot11ServicePolicyIDType
_H3cDot11CurrSvcPolicyID_Object=MibTableColumn
h3cDot11CurrSvcPolicyID=_H3cDot11CurrSvcPolicyID_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,4,1,3),_H3cDot11CurrSvcPolicyID_Type())
h3cDot11CurrSvcPolicyID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrSvcPolicyID.setStatus(_A)
_H3cDot11SSID_Type=OctetString
_H3cDot11SSID_Object=MibTableColumn
h3cDot11SSID=_H3cDot11SSID_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,4,1,4),_H3cDot11SSID_Type())
h3cDot11SSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11SSID.setStatus(_A)
_H3cDot11CurrSSIDResourceUseRatio_Type=Integer32
_H3cDot11CurrSSIDResourceUseRatio_Object=MibTableColumn
h3cDot11CurrSSIDResourceUseRatio=_H3cDot11CurrSSIDResourceUseRatio_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,4,1,5),_H3cDot11CurrSSIDResourceUseRatio_Type())
h3cDot11CurrSSIDResourceUseRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CurrSSIDResourceUseRatio.setStatus(_A)
_H3cDot11APEssVlanId_Type=Integer32
_H3cDot11APEssVlanId_Object=MibTableColumn
h3cDot11APEssVlanId=_H3cDot11APEssVlanId_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,4,1,6),_H3cDot11APEssVlanId_Type())
h3cDot11APEssVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APEssVlanId.setStatus(_A)
_H3cDot11APModelTable_Object=MibTable
h3cDot11APModelTable=_H3cDot11APModelTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,5))
if mibBuilder.loadTexts:h3cDot11APModelTable.setStatus(_A)
_H3cDot11APModelEntry_Object=MibTableRow
h3cDot11APModelEntry=_H3cDot11APModelEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,5,1))
h3cDot11APModelEntry.setIndexNames((1,_C,_r))
if mibBuilder.loadTexts:h3cDot11APModelEntry.setStatus(_A)
class _H3cDot11APModelAlias_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11APModelAlias_Type.__name__=_S
_H3cDot11APModelAlias_Object=MibTableColumn
h3cDot11APModelAlias=_H3cDot11APModelAlias_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,5,1,1),_H3cDot11APModelAlias_Type())
h3cDot11APModelAlias.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11APModelAlias.setStatus(_A)
_H3cDot11APModelName_Type=OctetString
_H3cDot11APModelName_Object=MibTableColumn
h3cDot11APModelName=_H3cDot11APModelName_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,5,1,2),_H3cDot11APModelName_Type())
h3cDot11APModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APModelName.setStatus(_A)
_H3cDot11RadioNumSupport_Type=H3cDot11RadioScopeType
_H3cDot11RadioNumSupport_Object=MibTableColumn
h3cDot11RadioNumSupport=_H3cDot11RadioNumSupport_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,5,1,3),_H3cDot11RadioNumSupport_Type())
h3cDot11RadioNumSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioNumSupport.setStatus(_A)
_H3cDot11StationNumSupport_Type=Integer32
_H3cDot11StationNumSupport_Object=MibTableColumn
h3cDot11StationNumSupport=_H3cDot11StationNumSupport_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,5,1,4),_H3cDot11StationNumSupport_Type())
h3cDot11StationNumSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StationNumSupport.setStatus(_A)
class _H3cDot11MACModeSupport_Type(H3cDot11MACModeType):defaultValue=1
_H3cDot11MACModeSupport_Type.__name__=_o
_H3cDot11MACModeSupport_Object=MibTableColumn
h3cDot11MACModeSupport=_H3cDot11MACModeSupport_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,5,1,5),_H3cDot11MACModeSupport_Type())
h3cDot11MACModeSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MACModeSupport.setStatus(_A)
_H3cDot11APManufacturer_Type=OctetString
_H3cDot11APManufacturer_Object=MibTableColumn
h3cDot11APManufacturer=_H3cDot11APManufacturer_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,5,1,6),_H3cDot11APManufacturer_Type())
h3cDot11APManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APManufacturer.setStatus(_A)
_H3cDot11APCPUType_Type=OctetString
_H3cDot11APCPUType_Object=MibTableColumn
h3cDot11APCPUType=_H3cDot11APCPUType_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,5,1,7),_H3cDot11APCPUType_Type())
h3cDot11APCPUType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APCPUType.setStatus(_A)
_H3cDot11APCPUClockSpeed_Type=Unsigned32
_H3cDot11APCPUClockSpeed_Object=MibTableColumn
h3cDot11APCPUClockSpeed=_H3cDot11APCPUClockSpeed_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,5,1,8),_H3cDot11APCPUClockSpeed_Type())
h3cDot11APCPUClockSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APCPUClockSpeed.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APCPUClockSpeed.setUnits('Hz')
_H3cDot11APMemoryType_Type=OctetString
_H3cDot11APMemoryType_Object=MibTableColumn
h3cDot11APMemoryType=_H3cDot11APMemoryType_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,5,1,9),_H3cDot11APMemoryType_Type())
h3cDot11APMemoryType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APMemoryType.setStatus(_A)
_H3cDot11APFlashType_Type=OctetString
_H3cDot11APFlashType_Object=MibTableColumn
h3cDot11APFlashType=_H3cDot11APFlashType_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,5,1,11),_H3cDot11APFlashType_Type())
h3cDot11APFlashType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APFlashType.setStatus(_A)
_H3cDot11APFlashSize_Type=Unsigned32
_H3cDot11APFlashSize_Object=MibTableColumn
h3cDot11APFlashSize=_H3cDot11APFlashSize_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,5,1,12),_H3cDot11APFlashSize_Type())
h3cDot11APFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APFlashSize.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APFlashSize.setUnits(_c)
_H3cDot11APMemSize_Type=Gauge32
_H3cDot11APMemSize_Object=MibTableColumn
h3cDot11APMemSize=_H3cDot11APMemSize_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,5,1,13),_H3cDot11APMemSize_Type())
h3cDot11APMemSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APMemSize.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APMemSize.setUnits(_Q)
_H3cDot11APFlashSizeInBytes_Type=Unsigned32
_H3cDot11APFlashSizeInBytes_Object=MibTableColumn
h3cDot11APFlashSizeInBytes=_H3cDot11APFlashSizeInBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,5,1,14),_H3cDot11APFlashSizeInBytes_Type())
h3cDot11APFlashSizeInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APFlashSizeInBytes.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APFlashSizeInBytes.setUnits(_Q)
_H3cDot11APMemorySize_Type=Unsigned32
_H3cDot11APMemorySize_Object=MibTableColumn
h3cDot11APMemorySize=_H3cDot11APMemorySize_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,5,1,20),_H3cDot11APMemorySize_Type())
h3cDot11APMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APMemorySize.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APMemorySize.setUnits(_c)
_H3cDot11APIfTable_Object=MibTable
h3cDot11APIfTable=_H3cDot11APIfTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,6))
if mibBuilder.loadTexts:h3cDot11APIfTable.setStatus(_A)
_H3cDot11APIfEntry_Object=MibTableRow
h3cDot11APIfEntry=_H3cDot11APIfEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,6,1))
h3cDot11APIfEntry.setIndexNames((0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:h3cDot11APIfEntry.setStatus(_A)
_H3cDot11APIfIndex_Type=Integer32
_H3cDot11APIfIndex_Object=MibTableColumn
h3cDot11APIfIndex=_H3cDot11APIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,6,1,1),_H3cDot11APIfIndex_Type())
h3cDot11APIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11APIfIndex.setStatus(_A)
_H3cDot11APIfDescr_Type=OctetString
_H3cDot11APIfDescr_Object=MibTableColumn
h3cDot11APIfDescr=_H3cDot11APIfDescr_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,6,1,2),_H3cDot11APIfDescr_Type())
h3cDot11APIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfDescr.setStatus(_A)
_H3cDot11APIfType_Type=Integer32
_H3cDot11APIfType_Object=MibTableColumn
h3cDot11APIfType=_H3cDot11APIfType_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,6,1,3),_H3cDot11APIfType_Type())
h3cDot11APIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfType.setStatus(_A)
_H3cDot11APIfMtu_Type=Integer32
_H3cDot11APIfMtu_Object=MibTableColumn
h3cDot11APIfMtu=_H3cDot11APIfMtu_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,6,1,4),_H3cDot11APIfMtu_Type())
h3cDot11APIfMtu.setMaxAccess(_q)
if mibBuilder.loadTexts:h3cDot11APIfMtu.setStatus(_A)
_H3cDot11APIfPHYAddress_Type=OctetString
_H3cDot11APIfPHYAddress_Object=MibTableColumn
h3cDot11APIfPHYAddress=_H3cDot11APIfPHYAddress_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,6,1,5),_H3cDot11APIfPHYAddress_Type())
h3cDot11APIfPHYAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfPHYAddress.setStatus(_A)
_H3cDot11APIfSpeed_Type=Integer32
_H3cDot11APIfSpeed_Object=MibTableColumn
h3cDot11APIfSpeed=_H3cDot11APIfSpeed_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,6,1,6),_H3cDot11APIfSpeed_Type())
h3cDot11APIfSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfSpeed.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APIfSpeed.setUnits('Mbps')
_H3cDot11APIfInDataRate_Type=Integer32
_H3cDot11APIfInDataRate_Object=MibTableColumn
h3cDot11APIfInDataRate=_H3cDot11APIfInDataRate_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,6,1,7),_H3cDot11APIfInDataRate_Type())
h3cDot11APIfInDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInDataRate.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APIfInDataRate.setUnits('Kbps')
_H3cDot11APIfOutDataRate_Type=Integer32
_H3cDot11APIfOutDataRate_Object=MibTableColumn
h3cDot11APIfOutDataRate=_H3cDot11APIfOutDataRate_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,6,1,8),_H3cDot11APIfOutDataRate_Type())
h3cDot11APIfOutDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutDataRate.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APIfOutDataRate.setUnits('Kbps')
_H3cDot11APIfSpeedKbps_Type=Gauge32
_H3cDot11APIfSpeedKbps_Object=MibTableColumn
h3cDot11APIfSpeedKbps=_H3cDot11APIfSpeedKbps_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,6,1,9),_H3cDot11APIfSpeedKbps_Type())
h3cDot11APIfSpeedKbps.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfSpeedKbps.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APIfSpeedKbps.setUnits('kbps')
_H3cDot11APSSIDObjectTable_Object=MibTable
h3cDot11APSSIDObjectTable=_H3cDot11APSSIDObjectTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,7))
if mibBuilder.loadTexts:h3cDot11APSSIDObjectTable.setStatus(_A)
_H3cDot11APSSIDObjectEntry_Object=MibTableRow
h3cDot11APSSIDObjectEntry=_H3cDot11APSSIDObjectEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,7,1))
h3cDot11APSSIDObjectEntry.setIndexNames((0,_C,_s))
if mibBuilder.loadTexts:h3cDot11APSSIDObjectEntry.setStatus(_A)
_H3cDot11APConfigSPID_Type=H3cDot11ServicePolicyIDType
_H3cDot11APConfigSPID_Object=MibTableColumn
h3cDot11APConfigSPID=_H3cDot11APConfigSPID_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,7,1,1),_H3cDot11APConfigSPID_Type())
h3cDot11APConfigSPID.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11APConfigSPID.setStatus(_A)
_H3cDot11APConfigSSIDName_Type=H3cDot11SSIDStringType
_H3cDot11APConfigSSIDName_Object=MibTableColumn
h3cDot11APConfigSSIDName=_H3cDot11APConfigSSIDName_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,7,1,2),_H3cDot11APConfigSSIDName_Type())
h3cDot11APConfigSSIDName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APConfigSSIDName.setStatus(_A)
_H3cDot11APConfigBSSIDNum_Type=Integer32
_H3cDot11APConfigBSSIDNum_Object=MibTableColumn
h3cDot11APConfigBSSIDNum=_H3cDot11APConfigBSSIDNum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,7,1,3),_H3cDot11APConfigBSSIDNum_Type())
h3cDot11APConfigBSSIDNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APConfigBSSIDNum.setStatus(_A)
_H3cDot11APConfigPortalStaNum_Type=Integer32
_H3cDot11APConfigPortalStaNum_Object=MibTableColumn
h3cDot11APConfigPortalStaNum=_H3cDot11APConfigPortalStaNum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,7,1,4),_H3cDot11APConfigPortalStaNum_Type())
h3cDot11APConfigPortalStaNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APConfigPortalStaNum.setStatus(_A)
_H3cDot11APSysInfoTable_Object=MibTable
h3cDot11APSysInfoTable=_H3cDot11APSysInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,8))
if mibBuilder.loadTexts:h3cDot11APSysInfoTable.setStatus(_A)
_H3cDot11APSysInfoEntry_Object=MibTableRow
h3cDot11APSysInfoEntry=_H3cDot11APSysInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,8,1))
h3cDot11APSysInfoEntry.setIndexNames((0,_a,_b))
if mibBuilder.loadTexts:h3cDot11APSysInfoEntry.setStatus(_A)
_H3cDot11APSysUpTime_Type=TimeTicks
_H3cDot11APSysUpTime_Object=MibTableColumn
h3cDot11APSysUpTime=_H3cDot11APSysUpTime_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,8,1,1),_H3cDot11APSysUpTime_Type())
h3cDot11APSysUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APSysUpTime.setStatus(_A)
class _H3cDot11APCPURTUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11APCPURTUsage_Type.__name__=_D
_H3cDot11APCPURTUsage_Object=MibTableColumn
h3cDot11APCPURTUsage=_H3cDot11APCPURTUsage_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,8,1,2),_H3cDot11APCPURTUsage_Type())
h3cDot11APCPURTUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APCPURTUsage.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APCPURTUsage.setUnits(_L)
class _H3cDot11APCPUAvgUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11APCPUAvgUsage_Type.__name__=_D
_H3cDot11APCPUAvgUsage_Object=MibTableColumn
h3cDot11APCPUAvgUsage=_H3cDot11APCPUAvgUsage_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,8,1,3),_H3cDot11APCPUAvgUsage_Type())
h3cDot11APCPUAvgUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APCPUAvgUsage.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APCPUAvgUsage.setUnits(_L)
class _H3cDot11APMemRTUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11APMemRTUsage_Type.__name__=_D
_H3cDot11APMemRTUsage_Object=MibTableColumn
h3cDot11APMemRTUsage=_H3cDot11APMemRTUsage_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,8,1,4),_H3cDot11APMemRTUsage_Type())
h3cDot11APMemRTUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APMemRTUsage.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APMemRTUsage.setUnits(_L)
class _H3cDot11APMemAvgUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11APMemAvgUsage_Type.__name__=_D
_H3cDot11APMemAvgUsage_Object=MibTableColumn
h3cDot11APMemAvgUsage=_H3cDot11APMemAvgUsage_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,8,1,5),_H3cDot11APMemAvgUsage_Type())
h3cDot11APMemAvgUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APMemAvgUsage.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APMemAvgUsage.setUnits(_L)
_H3cDot11APIPAddressGateway_Type=IpAddress
_H3cDot11APIPAddressGateway_Object=MibTableColumn
h3cDot11APIPAddressGateway=_H3cDot11APIPAddressGateway_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,8,1,6),_H3cDot11APIPAddressGateway_Type())
h3cDot11APIPAddressGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIPAddressGateway.setStatus(_A)
class _H3cDot11APACAssociateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_t,1),(_u,2),(_v,3)))
_H3cDot11APACAssociateStatus_Type.__name__=_D
_H3cDot11APACAssociateStatus_Object=MibTableColumn
h3cDot11APACAssociateStatus=_H3cDot11APACAssociateStatus_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,8,1,7),_H3cDot11APACAssociateStatus_Type())
h3cDot11APACAssociateStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APACAssociateStatus.setStatus(_A)
class _H3cDot11APManuBuildInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cDot11APManuBuildInfo_Type.__name__=_S
_H3cDot11APManuBuildInfo_Object=MibTableColumn
h3cDot11APManuBuildInfo=_H3cDot11APManuBuildInfo_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,8,1,8),_H3cDot11APManuBuildInfo_Type())
h3cDot11APManuBuildInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APManuBuildInfo.setStatus(_A)
_H3cDot11APFlashFreeSize_Type=Unsigned32
_H3cDot11APFlashFreeSize_Object=MibTableColumn
h3cDot11APFlashFreeSize=_H3cDot11APFlashFreeSize_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,8,1,9),_H3cDot11APFlashFreeSize_Type())
h3cDot11APFlashFreeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APFlashFreeSize.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APFlashFreeSize.setUnits(_Q)
_H3cDot11APTemperature_Type=Integer32
_H3cDot11APTemperature_Object=MibTableColumn
h3cDot11APTemperature=_H3cDot11APTemperature_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,8,1,10),_H3cDot11APTemperature_Type())
h3cDot11APTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APTemperature.setStatus(_A)
_H3cDot11APIdleListTable_Object=MibTable
h3cDot11APIdleListTable=_H3cDot11APIdleListTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,9))
if mibBuilder.loadTexts:h3cDot11APIdleListTable.setStatus(_A)
_H3cDot11APIdleListEntry_Object=MibTableRow
h3cDot11APIdleListEntry=_H3cDot11APIdleListEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,9,1))
h3cDot11APIdleListEntry.setIndexNames((0,_C,_w))
if mibBuilder.loadTexts:h3cDot11APIdleListEntry.setStatus(_A)
class _H3cDot11APIdleTemplateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11APIdleTemplateName_Type.__name__=_S
_H3cDot11APIdleTemplateName_Object=MibTableColumn
h3cDot11APIdleTemplateName=_H3cDot11APIdleTemplateName_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,9,1,1),_H3cDot11APIdleTemplateName_Type())
h3cDot11APIdleTemplateName.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11APIdleTemplateName.setStatus(_A)
_H3cDot11APIdleSerialID_Type=OctetString
_H3cDot11APIdleSerialID_Object=MibTableColumn
h3cDot11APIdleSerialID=_H3cDot11APIdleSerialID_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,9,1,2),_H3cDot11APIdleSerialID_Type())
h3cDot11APIdleSerialID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIdleSerialID.setStatus(_A)
_H3cDot11APSysInfoByAPIDTable_Object=MibTable
h3cDot11APSysInfoByAPIDTable=_H3cDot11APSysInfoByAPIDTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,10))
if mibBuilder.loadTexts:h3cDot11APSysInfoByAPIDTable.setStatus(_A)
_H3cDot11APSysInfoByAPIDEntry_Object=MibTableRow
h3cDot11APSysInfoByAPIDEntry=_H3cDot11APSysInfoByAPIDEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,10,1))
h3cDot11APSysInfoByAPIDEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:h3cDot11APSysInfoByAPIDEntry.setStatus(_A)
_H3cDot11APSysUpTime2_Type=TimeTicks
_H3cDot11APSysUpTime2_Object=MibTableColumn
h3cDot11APSysUpTime2=_H3cDot11APSysUpTime2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,10,1,1),_H3cDot11APSysUpTime2_Type())
h3cDot11APSysUpTime2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APSysUpTime2.setStatus(_A)
class _H3cDot11APCPURTUsage2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11APCPURTUsage2_Type.__name__=_D
_H3cDot11APCPURTUsage2_Object=MibTableColumn
h3cDot11APCPURTUsage2=_H3cDot11APCPURTUsage2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,10,1,2),_H3cDot11APCPURTUsage2_Type())
h3cDot11APCPURTUsage2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APCPURTUsage2.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APCPURTUsage2.setUnits(_L)
class _H3cDot11APCPUAvgUsage2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11APCPUAvgUsage2_Type.__name__=_D
_H3cDot11APCPUAvgUsage2_Object=MibTableColumn
h3cDot11APCPUAvgUsage2=_H3cDot11APCPUAvgUsage2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,10,1,3),_H3cDot11APCPUAvgUsage2_Type())
h3cDot11APCPUAvgUsage2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APCPUAvgUsage2.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APCPUAvgUsage2.setUnits(_L)
class _H3cDot11APMemRTUsage2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11APMemRTUsage2_Type.__name__=_D
_H3cDot11APMemRTUsage2_Object=MibTableColumn
h3cDot11APMemRTUsage2=_H3cDot11APMemRTUsage2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,10,1,4),_H3cDot11APMemRTUsage2_Type())
h3cDot11APMemRTUsage2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APMemRTUsage2.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APMemRTUsage2.setUnits(_L)
class _H3cDot11APMemAvgUsage2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11APMemAvgUsage2_Type.__name__=_D
_H3cDot11APMemAvgUsage2_Object=MibTableColumn
h3cDot11APMemAvgUsage2=_H3cDot11APMemAvgUsage2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,10,1,5),_H3cDot11APMemAvgUsage2_Type())
h3cDot11APMemAvgUsage2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APMemAvgUsage2.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APMemAvgUsage2.setUnits(_L)
_H3cDot11APIPAddressGateway2_Type=IpAddress
_H3cDot11APIPAddressGateway2_Object=MibTableColumn
h3cDot11APIPAddressGateway2=_H3cDot11APIPAddressGateway2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,10,1,6),_H3cDot11APIPAddressGateway2_Type())
h3cDot11APIPAddressGateway2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIPAddressGateway2.setStatus(_A)
class _H3cDot11APACAssociateStatus2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_t,1),(_u,2),(_v,3)))
_H3cDot11APACAssociateStatus2_Type.__name__=_D
_H3cDot11APACAssociateStatus2_Object=MibTableColumn
h3cDot11APACAssociateStatus2=_H3cDot11APACAssociateStatus2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,10,1,7),_H3cDot11APACAssociateStatus2_Type())
h3cDot11APACAssociateStatus2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APACAssociateStatus2.setStatus(_A)
class _H3cDot11APManuBuildInfo2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cDot11APManuBuildInfo2_Type.__name__=_S
_H3cDot11APManuBuildInfo2_Object=MibTableColumn
h3cDot11APManuBuildInfo2=_H3cDot11APManuBuildInfo2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,10,1,8),_H3cDot11APManuBuildInfo2_Type())
h3cDot11APManuBuildInfo2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APManuBuildInfo2.setStatus(_A)
_H3cDot11APFlashFreeSize2_Type=Unsigned32
_H3cDot11APFlashFreeSize2_Object=MibTableColumn
h3cDot11APFlashFreeSize2=_H3cDot11APFlashFreeSize2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,10,1,9),_H3cDot11APFlashFreeSize2_Type())
h3cDot11APFlashFreeSize2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APFlashFreeSize2.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APFlashFreeSize2.setUnits(_Q)
_H3cDot11APTemperature2_Type=Integer32
_H3cDot11APTemperature2_Object=MibTableColumn
h3cDot11APTemperature2=_H3cDot11APTemperature2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,10,1,10),_H3cDot11APTemperature2_Type())
h3cDot11APTemperature2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APTemperature2.setStatus(_A)
_H3cDot11APMacAddress2_Type=MacAddress
_H3cDot11APMacAddress2_Object=MibTableColumn
h3cDot11APMacAddress2=_H3cDot11APMacAddress2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,1,10,1,11),_H3cDot11APMacAddress2_Type())
h3cDot11APMacAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APMacAddress2.setStatus(_A)
_H3cDot11APStatisGroup_ObjectIdentity=ObjectIdentity
h3cDot11APStatisGroup=_H3cDot11APStatisGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,2,2))
_H3cDot11APRxStatisTable_Object=MibTable
h3cDot11APRxStatisTable=_H3cDot11APRxStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1))
if mibBuilder.loadTexts:h3cDot11APRxStatisTable.setStatus(_A)
_H3cDot11APRxStatisEntry_Object=MibTableRow
h3cDot11APRxStatisEntry=_H3cDot11APRxStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1))
h3cDot11APRxStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:h3cDot11APRxStatisEntry.setStatus(_A)
_H3cDot11RxFrameDupCnt_Type=Counter32
_H3cDot11RxFrameDupCnt_Object=MibTableColumn
h3cDot11RxFrameDupCnt=_H3cDot11RxFrameDupCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,1),_H3cDot11RxFrameDupCnt_Type())
h3cDot11RxFrameDupCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxFrameDupCnt.setStatus(_A)
_H3cDot11RxFrameCnt_Type=Counter32
_H3cDot11RxFrameCnt_Object=MibTableColumn
h3cDot11RxFrameCnt=_H3cDot11RxFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,2),_H3cDot11RxFrameCnt_Type())
h3cDot11RxFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxFrameCnt.setStatus(_A)
_H3cDot11RxUcastFrameCnt_Type=Counter32
_H3cDot11RxUcastFrameCnt_Object=MibTableColumn
h3cDot11RxUcastFrameCnt=_H3cDot11RxUcastFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,3),_H3cDot11RxUcastFrameCnt_Type())
h3cDot11RxUcastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxUcastFrameCnt.setStatus(_A)
_H3cDot11RxBcastFrameCnt_Type=Counter32
_H3cDot11RxBcastFrameCnt_Object=MibTableColumn
h3cDot11RxBcastFrameCnt=_H3cDot11RxBcastFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,4),_H3cDot11RxBcastFrameCnt_Type())
h3cDot11RxBcastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxBcastFrameCnt.setStatus(_A)
_H3cDot11RxMcastFrameCnt_Type=Counter32
_H3cDot11RxMcastFrameCnt_Object=MibTableColumn
h3cDot11RxMcastFrameCnt=_H3cDot11RxMcastFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,5),_H3cDot11RxMcastFrameCnt_Type())
h3cDot11RxMcastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxMcastFrameCnt.setStatus(_A)
_H3cDot11RxDiscardFrameCnt_Type=Counter32
_H3cDot11RxDiscardFrameCnt_Object=MibTableColumn
h3cDot11RxDiscardFrameCnt=_H3cDot11RxDiscardFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,6),_H3cDot11RxDiscardFrameCnt_Type())
h3cDot11RxDiscardFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxDiscardFrameCnt.setStatus(_A)
_H3cDot11RxFragCnt_Type=Counter32
_H3cDot11RxFragCnt_Object=MibTableColumn
h3cDot11RxFragCnt=_H3cDot11RxFragCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,7),_H3cDot11RxFragCnt_Type())
h3cDot11RxFragCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxFragCnt.setStatus(_A)
_H3cDot11RxFcsErrCnt_Type=Counter32
_H3cDot11RxFcsErrCnt_Object=MibTableColumn
h3cDot11RxFcsErrCnt=_H3cDot11RxFcsErrCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,8),_H3cDot11RxFcsErrCnt_Type())
h3cDot11RxFcsErrCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxFcsErrCnt.setStatus(_A)
_H3cDot11RxFrameBytes_Type=Counter32
_H3cDot11RxFrameBytes_Object=MibTableColumn
h3cDot11RxFrameBytes=_H3cDot11RxFrameBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,9),_H3cDot11RxFrameBytes_Type())
h3cDot11RxFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxFrameBytes.setStatus(_A)
_H3cDot11RxUcastFrameBytes_Type=Counter32
_H3cDot11RxUcastFrameBytes_Object=MibTableColumn
h3cDot11RxUcastFrameBytes=_H3cDot11RxUcastFrameBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,10),_H3cDot11RxUcastFrameBytes_Type())
h3cDot11RxUcastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxUcastFrameBytes.setStatus(_A)
_H3cDot11RxBcastFrameBytes_Type=Counter32
_H3cDot11RxBcastFrameBytes_Object=MibTableColumn
h3cDot11RxBcastFrameBytes=_H3cDot11RxBcastFrameBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,11),_H3cDot11RxBcastFrameBytes_Type())
h3cDot11RxBcastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxBcastFrameBytes.setStatus(_A)
_H3cDot11RxMcastFrameBytes_Type=Counter32
_H3cDot11RxMcastFrameBytes_Object=MibTableColumn
h3cDot11RxMcastFrameBytes=_H3cDot11RxMcastFrameBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,12),_H3cDot11RxMcastFrameBytes_Type())
h3cDot11RxMcastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxMcastFrameBytes.setStatus(_A)
_H3cDot11RxDiscardFrameBytes_Type=Counter32
_H3cDot11RxDiscardFrameBytes_Object=MibTableColumn
h3cDot11RxDiscardFrameBytes=_H3cDot11RxDiscardFrameBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,13),_H3cDot11RxDiscardFrameBytes_Type())
h3cDot11RxDiscardFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxDiscardFrameBytes.setStatus(_A)
_H3cDot11RxMgmtFrameCnt_Type=Counter32
_H3cDot11RxMgmtFrameCnt_Object=MibTableColumn
h3cDot11RxMgmtFrameCnt=_H3cDot11RxMgmtFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,14),_H3cDot11RxMgmtFrameCnt_Type())
h3cDot11RxMgmtFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxMgmtFrameCnt.setStatus(_A)
_H3cDot11RxCtrlFrameCnt_Type=Counter32
_H3cDot11RxCtrlFrameCnt_Object=MibTableColumn
h3cDot11RxCtrlFrameCnt=_H3cDot11RxCtrlFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,15),_H3cDot11RxCtrlFrameCnt_Type())
h3cDot11RxCtrlFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxCtrlFrameCnt.setStatus(_A)
_H3cDot11RxDataFrameCnt_Type=Counter32
_H3cDot11RxDataFrameCnt_Object=MibTableColumn
h3cDot11RxDataFrameCnt=_H3cDot11RxDataFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,16),_H3cDot11RxDataFrameCnt_Type())
h3cDot11RxDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxDataFrameCnt.setStatus(_A)
_H3cDot11RxDecryptErrorCnt_Type=Counter32
_H3cDot11RxDecryptErrorCnt_Object=MibTableColumn
h3cDot11RxDecryptErrorCnt=_H3cDot11RxDecryptErrorCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,17),_H3cDot11RxDecryptErrorCnt_Type())
h3cDot11RxDecryptErrorCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxDecryptErrorCnt.setStatus(_A)
_H3cDot11RxAuthenFrameCnt_Type=Counter32
_H3cDot11RxAuthenFrameCnt_Object=MibTableColumn
h3cDot11RxAuthenFrameCnt=_H3cDot11RxAuthenFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,18),_H3cDot11RxAuthenFrameCnt_Type())
h3cDot11RxAuthenFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxAuthenFrameCnt.setStatus(_A)
_H3cDot11RxAssociateFrameCnt_Type=Counter32
_H3cDot11RxAssociateFrameCnt_Object=MibTableColumn
h3cDot11RxAssociateFrameCnt=_H3cDot11RxAssociateFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,19),_H3cDot11RxAssociateFrameCnt_Type())
h3cDot11RxAssociateFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxAssociateFrameCnt.setStatus(_A)
_H3cDot11RxFrameErrorRatio_Type=Integer32
_H3cDot11RxFrameErrorRatio_Object=MibTableColumn
h3cDot11RxFrameErrorRatio=_H3cDot11RxFrameErrorRatio_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,20),_H3cDot11RxFrameErrorRatio_Type())
h3cDot11RxFrameErrorRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxFrameErrorRatio.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RxFrameErrorRatio.setUnits(_L)
_H3cDot11RxPhyErrorCnt_Type=Counter32
_H3cDot11RxPhyErrorCnt_Object=MibTableColumn
h3cDot11RxPhyErrorCnt=_H3cDot11RxPhyErrorCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,21),_H3cDot11RxPhyErrorCnt_Type())
h3cDot11RxPhyErrorCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxPhyErrorCnt.setStatus(_A)
_H3cDot11RxMICErrorCnt_Type=Counter32
_H3cDot11RxMICErrorCnt_Object=MibTableColumn
h3cDot11RxMICErrorCnt=_H3cDot11RxMICErrorCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,22),_H3cDot11RxMICErrorCnt_Type())
h3cDot11RxMICErrorCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxMICErrorCnt.setStatus(_A)
_H3cDot11RxDataFrameBytes_Type=Counter32
_H3cDot11RxDataFrameBytes_Object=MibTableColumn
h3cDot11RxDataFrameBytes=_H3cDot11RxDataFrameBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,23),_H3cDot11RxDataFrameBytes_Type())
h3cDot11RxDataFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxDataFrameBytes.setStatus(_A)
_H3cDot11RadioRxAverSnr_Type=Integer32
_H3cDot11RadioRxAverSnr_Object=MibTableColumn
h3cDot11RadioRxAverSnr=_H3cDot11RadioRxAverSnr_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,24),_H3cDot11RadioRxAverSnr_Type())
h3cDot11RadioRxAverSnr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioRxAverSnr.setStatus(_A)
_H3cDot11RxPayloadBytes_Type=Counter32
_H3cDot11RxPayloadBytes_Object=MibTableColumn
h3cDot11RxPayloadBytes=_H3cDot11RxPayloadBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,25),_H3cDot11RxPayloadBytes_Type())
h3cDot11RxPayloadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxPayloadBytes.setStatus(_A)
_H3cDot11RxTrafficSpeed_Type=Integer32
_H3cDot11RxTrafficSpeed_Object=MibTableColumn
h3cDot11RxTrafficSpeed=_H3cDot11RxTrafficSpeed_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,26),_H3cDot11RxTrafficSpeed_Type())
h3cDot11RxTrafficSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxTrafficSpeed.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RxTrafficSpeed.setUnits(_x)
_H3cDot11RxUcastDataFrameCnt_Type=Counter64
_H3cDot11RxUcastDataFrameCnt_Object=MibTableColumn
h3cDot11RxUcastDataFrameCnt=_H3cDot11RxUcastDataFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,27),_H3cDot11RxUcastDataFrameCnt_Type())
h3cDot11RxUcastDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxUcastDataFrameCnt.setStatus(_A)
_H3cDot11RxNUcastDataFrameCnt_Type=Counter64
_H3cDot11RxNUcastDataFrameCnt_Object=MibTableColumn
h3cDot11RxNUcastDataFrameCnt=_H3cDot11RxNUcastDataFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,28),_H3cDot11RxNUcastDataFrameCnt_Type())
h3cDot11RxNUcastDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxNUcastDataFrameCnt.setStatus(_A)
_H3cDot11RxTotalDiscardFrameCnt_Type=Counter64
_H3cDot11RxTotalDiscardFrameCnt_Object=MibTableColumn
h3cDot11RxTotalDiscardFrameCnt=_H3cDot11RxTotalDiscardFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,29),_H3cDot11RxTotalDiscardFrameCnt_Type())
h3cDot11RxTotalDiscardFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxTotalDiscardFrameCnt.setStatus(_A)
_H3cDot11RxTotalIPCheckErrPacketCnt_Type=Counter64
_H3cDot11RxTotalIPCheckErrPacketCnt_Object=MibTableColumn
h3cDot11RxTotalIPCheckErrPacketCnt=_H3cDot11RxTotalIPCheckErrPacketCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,1,1,30),_H3cDot11RxTotalIPCheckErrPacketCnt_Type())
h3cDot11RxTotalIPCheckErrPacketCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RxTotalIPCheckErrPacketCnt.setStatus(_A)
_H3cDot11APTxStatisTable_Object=MibTable
h3cDot11APTxStatisTable=_H3cDot11APTxStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2))
if mibBuilder.loadTexts:h3cDot11APTxStatisTable.setStatus(_A)
_H3cDot11APTxStatisEntry_Object=MibTableRow
h3cDot11APTxStatisEntry=_H3cDot11APTxStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1))
h3cDot11APTxStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:h3cDot11APTxStatisEntry.setStatus(_A)
_H3cDot11TxFragCnt_Type=Counter32
_H3cDot11TxFragCnt_Object=MibTableColumn
h3cDot11TxFragCnt=_H3cDot11TxFragCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,1),_H3cDot11TxFragCnt_Type())
h3cDot11TxFragCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxFragCnt.setStatus(_A)
_H3cDot11FailedCnt_Type=Counter32
_H3cDot11FailedCnt_Object=MibTableColumn
h3cDot11FailedCnt=_H3cDot11FailedCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,2),_H3cDot11FailedCnt_Type())
h3cDot11FailedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11FailedCnt.setStatus(_A)
_H3cDot11RetryCnt_Type=Counter32
_H3cDot11RetryCnt_Object=MibTableColumn
h3cDot11RetryCnt=_H3cDot11RetryCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,3),_H3cDot11RetryCnt_Type())
h3cDot11RetryCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RetryCnt.setStatus(_A)
_H3cDot11MultiRetryCnt_Type=Counter32
_H3cDot11MultiRetryCnt_Object=MibTableColumn
h3cDot11MultiRetryCnt=_H3cDot11MultiRetryCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,4),_H3cDot11MultiRetryCnt_Type())
h3cDot11MultiRetryCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MultiRetryCnt.setStatus(_A)
_H3cDot11RtsSuccessCnt_Type=Counter32
_H3cDot11RtsSuccessCnt_Object=MibTableColumn
h3cDot11RtsSuccessCnt=_H3cDot11RtsSuccessCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,5),_H3cDot11RtsSuccessCnt_Type())
h3cDot11RtsSuccessCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RtsSuccessCnt.setStatus(_A)
_H3cDot11RtsFailCnt_Type=Counter32
_H3cDot11RtsFailCnt_Object=MibTableColumn
h3cDot11RtsFailCnt=_H3cDot11RtsFailCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,6),_H3cDot11RtsFailCnt_Type())
h3cDot11RtsFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RtsFailCnt.setStatus(_A)
_H3cDot11AckFailCnt_Type=Counter32
_H3cDot11AckFailCnt_Object=MibTableColumn
h3cDot11AckFailCnt=_H3cDot11AckFailCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,7),_H3cDot11AckFailCnt_Type())
h3cDot11AckFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AckFailCnt.setStatus(_A)
_H3cDot11TxFrameCnt_Type=Counter32
_H3cDot11TxFrameCnt_Object=MibTableColumn
h3cDot11TxFrameCnt=_H3cDot11TxFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,8),_H3cDot11TxFrameCnt_Type())
h3cDot11TxFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxFrameCnt.setStatus(_A)
_H3cDot11TxUcastFrameCnt_Type=Counter32
_H3cDot11TxUcastFrameCnt_Object=MibTableColumn
h3cDot11TxUcastFrameCnt=_H3cDot11TxUcastFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,9),_H3cDot11TxUcastFrameCnt_Type())
h3cDot11TxUcastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxUcastFrameCnt.setStatus(_A)
_H3cDot11TxBcastFrameCnt_Type=Counter32
_H3cDot11TxBcastFrameCnt_Object=MibTableColumn
h3cDot11TxBcastFrameCnt=_H3cDot11TxBcastFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,10),_H3cDot11TxBcastFrameCnt_Type())
h3cDot11TxBcastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxBcastFrameCnt.setStatus(_A)
_H3cDot11TxMcastFrameCnt_Type=Counter32
_H3cDot11TxMcastFrameCnt_Object=MibTableColumn
h3cDot11TxMcastFrameCnt=_H3cDot11TxMcastFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,11),_H3cDot11TxMcastFrameCnt_Type())
h3cDot11TxMcastFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxMcastFrameCnt.setStatus(_A)
_H3cDot11TxDiscardFrameCnt_Type=Counter32
_H3cDot11TxDiscardFrameCnt_Object=MibTableColumn
h3cDot11TxDiscardFrameCnt=_H3cDot11TxDiscardFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,12),_H3cDot11TxDiscardFrameCnt_Type())
h3cDot11TxDiscardFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxDiscardFrameCnt.setStatus(_A)
_H3cDot11TxFrameBytes_Type=Counter32
_H3cDot11TxFrameBytes_Object=MibTableColumn
h3cDot11TxFrameBytes=_H3cDot11TxFrameBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,13),_H3cDot11TxFrameBytes_Type())
h3cDot11TxFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxFrameBytes.setStatus(_A)
_H3cDot11TxUcastFrameBytes_Type=Counter32
_H3cDot11TxUcastFrameBytes_Object=MibTableColumn
h3cDot11TxUcastFrameBytes=_H3cDot11TxUcastFrameBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,14),_H3cDot11TxUcastFrameBytes_Type())
h3cDot11TxUcastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxUcastFrameBytes.setStatus(_A)
_H3cDot11TxBcastFrameBytes_Type=Counter32
_H3cDot11TxBcastFrameBytes_Object=MibTableColumn
h3cDot11TxBcastFrameBytes=_H3cDot11TxBcastFrameBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,15),_H3cDot11TxBcastFrameBytes_Type())
h3cDot11TxBcastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxBcastFrameBytes.setStatus(_A)
_H3cDot11TxMcastFrameBytes_Type=Counter32
_H3cDot11TxMcastFrameBytes_Object=MibTableColumn
h3cDot11TxMcastFrameBytes=_H3cDot11TxMcastFrameBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,16),_H3cDot11TxMcastFrameBytes_Type())
h3cDot11TxMcastFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxMcastFrameBytes.setStatus(_A)
_H3cDot11TxDiscardFrameBytes_Type=Counter32
_H3cDot11TxDiscardFrameBytes_Object=MibTableColumn
h3cDot11TxDiscardFrameBytes=_H3cDot11TxDiscardFrameBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,17),_H3cDot11TxDiscardFrameBytes_Type())
h3cDot11TxDiscardFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxDiscardFrameBytes.setStatus(_A)
_H3cDot11TxAuthenFrameCnt_Type=Counter32
_H3cDot11TxAuthenFrameCnt_Object=MibTableColumn
h3cDot11TxAuthenFrameCnt=_H3cDot11TxAuthenFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,18),_H3cDot11TxAuthenFrameCnt_Type())
h3cDot11TxAuthenFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxAuthenFrameCnt.setStatus(_A)
_H3cDot11TxAssociateFrameCnt_Type=Counter32
_H3cDot11TxAssociateFrameCnt_Object=MibTableColumn
h3cDot11TxAssociateFrameCnt=_H3cDot11TxAssociateFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,19),_H3cDot11TxAssociateFrameCnt_Type())
h3cDot11TxAssociateFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxAssociateFrameCnt.setStatus(_A)
_H3cDot11TxFrameRetryRatio_Type=Integer32
_H3cDot11TxFrameRetryRatio_Object=MibTableColumn
h3cDot11TxFrameRetryRatio=_H3cDot11TxFrameRetryRatio_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,20),_H3cDot11TxFrameRetryRatio_Type())
h3cDot11TxFrameRetryRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxFrameRetryRatio.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11TxFrameRetryRatio.setUnits(_L)
_H3cDot11TxDataFrameCnt_Type=Counter32
_H3cDot11TxDataFrameCnt_Object=MibTableColumn
h3cDot11TxDataFrameCnt=_H3cDot11TxDataFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,21),_H3cDot11TxDataFrameCnt_Type())
h3cDot11TxDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxDataFrameCnt.setStatus(_A)
_H3cDot11TxDataFrameBytes_Type=Counter32
_H3cDot11TxDataFrameBytes_Object=MibTableColumn
h3cDot11TxDataFrameBytes=_H3cDot11TxDataFrameBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,22),_H3cDot11TxDataFrameBytes_Type())
h3cDot11TxDataFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxDataFrameBytes.setStatus(_A)
_H3cDot11TxMSDUCnt_Type=Counter32
_H3cDot11TxMSDUCnt_Object=MibTableColumn
h3cDot11TxMSDUCnt=_H3cDot11TxMSDUCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,23),_H3cDot11TxMSDUCnt_Type())
h3cDot11TxMSDUCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxMSDUCnt.setStatus(_A)
_H3cDot11TxDiscardMSDUCnt_Type=Counter32
_H3cDot11TxDiscardMSDUCnt_Object=MibTableColumn
h3cDot11TxDiscardMSDUCnt=_H3cDot11TxDiscardMSDUCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,24),_H3cDot11TxDiscardMSDUCnt_Type())
h3cDot11TxDiscardMSDUCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxDiscardMSDUCnt.setStatus(_A)
_H3cDot11RetryMSDUCnt_Type=Counter32
_H3cDot11RetryMSDUCnt_Object=MibTableColumn
h3cDot11RetryMSDUCnt=_H3cDot11RetryMSDUCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,25),_H3cDot11RetryMSDUCnt_Type())
h3cDot11RetryMSDUCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RetryMSDUCnt.setStatus(_A)
_H3cDot11TxPayloadBytes_Type=Counter32
_H3cDot11TxPayloadBytes_Object=MibTableColumn
h3cDot11TxPayloadBytes=_H3cDot11TxPayloadBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,26),_H3cDot11TxPayloadBytes_Type())
h3cDot11TxPayloadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxPayloadBytes.setStatus(_A)
_H3cDot11TxTrafficSpeed_Type=Integer32
_H3cDot11TxTrafficSpeed_Object=MibTableColumn
h3cDot11TxTrafficSpeed=_H3cDot11TxTrafficSpeed_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,27),_H3cDot11TxTrafficSpeed_Type())
h3cDot11TxTrafficSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxTrafficSpeed.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11TxTrafficSpeed.setUnits(_x)
_H3cDot11TxErrFrameRatio_Type=Integer32
_H3cDot11TxErrFrameRatio_Object=MibTableColumn
h3cDot11TxErrFrameRatio=_H3cDot11TxErrFrameRatio_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,28),_H3cDot11TxErrFrameRatio_Type())
h3cDot11TxErrFrameRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxErrFrameRatio.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11TxErrFrameRatio.setUnits(_L)
_H3cDot11TxFrameRate_Type=Integer32
_H3cDot11TxFrameRate_Object=MibTableColumn
h3cDot11TxFrameRate=_H3cDot11TxFrameRate_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,29),_H3cDot11TxFrameRate_Type())
h3cDot11TxFrameRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxFrameRate.setStatus(_A)
_H3cDot11TxMgtFrameCnt_Type=Counter32
_H3cDot11TxMgtFrameCnt_Object=MibTableColumn
h3cDot11TxMgtFrameCnt=_H3cDot11TxMgtFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,30),_H3cDot11TxMgtFrameCnt_Type())
h3cDot11TxMgtFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxMgtFrameCnt.setStatus(_A)
_H3cDot11TxCtrlFrameCnt_Type=Counter32
_H3cDot11TxCtrlFrameCnt_Object=MibTableColumn
h3cDot11TxCtrlFrameCnt=_H3cDot11TxCtrlFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,31),_H3cDot11TxCtrlFrameCnt_Type())
h3cDot11TxCtrlFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxCtrlFrameCnt.setStatus(_A)
_H3cDot11TxMACErrCnt_Type=Counter32
_H3cDot11TxMACErrCnt_Object=MibTableColumn
h3cDot11TxMACErrCnt=_H3cDot11TxMACErrCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,32),_H3cDot11TxMACErrCnt_Type())
h3cDot11TxMACErrCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxMACErrCnt.setStatus(_A)
_H3cDot11TxErrFrameCnt_Type=Counter32
_H3cDot11TxErrFrameCnt_Object=MibTableColumn
h3cDot11TxErrFrameCnt=_H3cDot11TxErrFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,33),_H3cDot11TxErrFrameCnt_Type())
h3cDot11TxErrFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxErrFrameCnt.setStatus(_A)
_H3cDot11TxUcastDataFrameCnt_Type=Counter64
_H3cDot11TxUcastDataFrameCnt_Object=MibTableColumn
h3cDot11TxUcastDataFrameCnt=_H3cDot11TxUcastDataFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,34),_H3cDot11TxUcastDataFrameCnt_Type())
h3cDot11TxUcastDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxUcastDataFrameCnt.setStatus(_A)
_H3cDot11TxNUcastDataFrameCnt_Type=Counter64
_H3cDot11TxNUcastDataFrameCnt_Object=MibTableColumn
h3cDot11TxNUcastDataFrameCnt=_H3cDot11TxNUcastDataFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,2,1,35),_H3cDot11TxNUcastDataFrameCnt_Type())
h3cDot11TxNUcastDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TxNUcastDataFrameCnt.setStatus(_A)
_H3cDot11APAssocStatisTable_Object=MibTable
h3cDot11APAssocStatisTable=_H3cDot11APAssocStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,3))
if mibBuilder.loadTexts:h3cDot11APAssocStatisTable.setStatus(_A)
_H3cDot11APAssocStatisEntry_Object=MibTableRow
h3cDot11APAssocStatisEntry=_H3cDot11APAssocStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,3,1))
h3cDot11APAssocStatisEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:h3cDot11APAssocStatisEntry.setStatus(_A)
_H3cDot11ApStationAssocSum_Type=Counter32
_H3cDot11ApStationAssocSum_Object=MibTableColumn
h3cDot11ApStationAssocSum=_H3cDot11ApStationAssocSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,3,1,1),_H3cDot11ApStationAssocSum_Type())
h3cDot11ApStationAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ApStationAssocSum.setStatus(_A)
_H3cDot11ApStationAssocFailSum_Type=Counter32
_H3cDot11ApStationAssocFailSum_Object=MibTableColumn
h3cDot11ApStationAssocFailSum=_H3cDot11ApStationAssocFailSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,3,1,2),_H3cDot11ApStationAssocFailSum_Type())
h3cDot11ApStationAssocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ApStationAssocFailSum.setStatus(_A)
_H3cDot11ApStationReassocSum_Type=Counter32
_H3cDot11ApStationReassocSum_Object=MibTableColumn
h3cDot11ApStationReassocSum=_H3cDot11ApStationReassocSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,3,1,3),_H3cDot11ApStationReassocSum_Type())
h3cDot11ApStationReassocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ApStationReassocSum.setStatus(_A)
_H3cDot11ApStationAssocRejectSum_Type=Counter32
_H3cDot11ApStationAssocRejectSum_Object=MibTableColumn
h3cDot11ApStationAssocRejectSum=_H3cDot11ApStationAssocRejectSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,3,1,4),_H3cDot11ApStationAssocRejectSum_Type())
h3cDot11ApStationAssocRejectSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ApStationAssocRejectSum.setStatus(_A)
_H3cDot11ApStationExDeAuthenSum_Type=Counter32
_H3cDot11ApStationExDeAuthenSum_Object=MibTableColumn
h3cDot11ApStationExDeAuthenSum=_H3cDot11ApStationExDeAuthenSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,3,1,5),_H3cDot11ApStationExDeAuthenSum_Type())
h3cDot11ApStationExDeAuthenSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ApStationExDeAuthenSum.setStatus(_A)
_H3cDot11ApStationCurAssocSum_Type=Integer32
_H3cDot11ApStationCurAssocSum_Object=MibTableColumn
h3cDot11ApStationCurAssocSum=_H3cDot11ApStationCurAssocSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,3,1,6),_H3cDot11ApStationCurAssocSum_Type())
h3cDot11ApStationCurAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ApStationCurAssocSum.setStatus(_A)
_H3cDot11ApStaCurAuthSuccSum_Type=Integer32
_H3cDot11ApStaCurAuthSuccSum_Object=MibTableColumn
h3cDot11ApStaCurAuthSuccSum=_H3cDot11ApStaCurAuthSuccSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,3,1,7),_H3cDot11ApStaCurAuthSuccSum_Type())
h3cDot11ApStaCurAuthSuccSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ApStaCurAuthSuccSum.setStatus(_A)
_H3cDot11AllStationUpSumTime_Type=Counter32
_H3cDot11AllStationUpSumTime_Object=MibTableColumn
h3cDot11AllStationUpSumTime=_H3cDot11AllStationUpSumTime_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,3,1,8),_H3cDot11AllStationUpSumTime_Type())
h3cDot11AllStationUpSumTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AllStationUpSumTime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11AllStationUpSumTime.setUnits('minute')
_H3cDot11ApStationAssocReqSum_Type=Counter32
_H3cDot11ApStationAssocReqSum_Object=MibTableColumn
h3cDot11ApStationAssocReqSum=_H3cDot11ApStationAssocReqSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,3,1,9),_H3cDot11ApStationAssocReqSum_Type())
h3cDot11ApStationAssocReqSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ApStationAssocReqSum.setStatus(_A)
_H3cDot11AllStationUpSumTimeTicks_Type=TimeTicks
_H3cDot11AllStationUpSumTimeTicks_Object=MibTableColumn
h3cDot11AllStationUpSumTimeTicks=_H3cDot11AllStationUpSumTimeTicks_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,3,1,10),_H3cDot11AllStationUpSumTimeTicks_Type())
h3cDot11AllStationUpSumTimeTicks.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AllStationUpSumTimeTicks.setStatus(_A)
_H3cDot11BSSRxStatisTable_Object=MibTable
h3cDot11BSSRxStatisTable=_H3cDot11BSSRxStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,4))
if mibBuilder.loadTexts:h3cDot11BSSRxStatisTable.setStatus(_A)
_H3cDot11BSSRxStatisEntry_Object=MibTableRow
h3cDot11BSSRxStatisEntry=_H3cDot11BSSRxStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,4,1))
h3cDot11BSSRxStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_T))
if mibBuilder.loadTexts:h3cDot11BSSRxStatisEntry.setStatus(_A)
_H3cDot11BSSRxFrameCnt_Type=Counter32
_H3cDot11BSSRxFrameCnt_Object=MibTableColumn
h3cDot11BSSRxFrameCnt=_H3cDot11BSSRxFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,4,1,1),_H3cDot11BSSRxFrameCnt_Type())
h3cDot11BSSRxFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSRxFrameCnt.setStatus(_A)
_H3cDot11BSSRxFrameBytes_Type=Counter32
_H3cDot11BSSRxFrameBytes_Object=MibTableColumn
h3cDot11BSSRxFrameBytes=_H3cDot11BSSRxFrameBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,4,1,2),_H3cDot11BSSRxFrameBytes_Type())
h3cDot11BSSRxFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSRxFrameBytes.setStatus(_A)
_H3cDot11BSSRxDataFrameCnt_Type=Counter32
_H3cDot11BSSRxDataFrameCnt_Object=MibTableColumn
h3cDot11BSSRxDataFrameCnt=_H3cDot11BSSRxDataFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,4,1,3),_H3cDot11BSSRxDataFrameCnt_Type())
h3cDot11BSSRxDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSRxDataFrameCnt.setStatus(_A)
_H3cDot11BSSRxDataFrameBytes_Type=Counter32
_H3cDot11BSSRxDataFrameBytes_Object=MibTableColumn
h3cDot11BSSRxDataFrameBytes=_H3cDot11BSSRxDataFrameBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,4,1,4),_H3cDot11BSSRxDataFrameBytes_Type())
h3cDot11BSSRxDataFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSRxDataFrameBytes.setStatus(_A)
_H3cDot11BSSRxAssociateFrameCnt_Type=Counter32
_H3cDot11BSSRxAssociateFrameCnt_Object=MibTableColumn
h3cDot11BSSRxAssociateFrameCnt=_H3cDot11BSSRxAssociateFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,4,1,5),_H3cDot11BSSRxAssociateFrameCnt_Type())
h3cDot11BSSRxAssociateFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSRxAssociateFrameCnt.setStatus(_A)
_H3cDot11BSSRxFrameErrorRatio_Type=Integer32
_H3cDot11BSSRxFrameErrorRatio_Object=MibTableColumn
h3cDot11BSSRxFrameErrorRatio=_H3cDot11BSSRxFrameErrorRatio_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,4,1,6),_H3cDot11BSSRxFrameErrorRatio_Type())
h3cDot11BSSRxFrameErrorRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSRxFrameErrorRatio.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11BSSRxFrameErrorRatio.setUnits('percent')
_H3cDot11BSSRxPayloadBytes_Type=Counter32
_H3cDot11BSSRxPayloadBytes_Object=MibTableColumn
h3cDot11BSSRxPayloadBytes=_H3cDot11BSSRxPayloadBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,4,1,7),_H3cDot11BSSRxPayloadBytes_Type())
h3cDot11BSSRxPayloadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSRxPayloadBytes.setStatus(_A)
_H3cDot11BSSRxUniFrameCnt_Type=Counter32
_H3cDot11BSSRxUniFrameCnt_Object=MibTableColumn
h3cDot11BSSRxUniFrameCnt=_H3cDot11BSSRxUniFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,4,1,8),_H3cDot11BSSRxUniFrameCnt_Type())
h3cDot11BSSRxUniFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSRxUniFrameCnt.setStatus(_A)
_H3cDot11BSSRxNonUniFrameCnt_Type=Integer32
_H3cDot11BSSRxNonUniFrameCnt_Object=MibTableColumn
h3cDot11BSSRxNonUniFrameCnt=_H3cDot11BSSRxNonUniFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,4,1,9),_H3cDot11BSSRxNonUniFrameCnt_Type())
h3cDot11BSSRxNonUniFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSRxNonUniFrameCnt.setStatus(_A)
_H3cDot11BSSRxAuthenFrameCnt_Type=Counter32
_H3cDot11BSSRxAuthenFrameCnt_Object=MibTableColumn
h3cDot11BSSRxAuthenFrameCnt=_H3cDot11BSSRxAuthenFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,4,1,10),_H3cDot11BSSRxAuthenFrameCnt_Type())
h3cDot11BSSRxAuthenFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSRxAuthenFrameCnt.setStatus(_A)
_H3cDot11BSSTxStatisTable_Object=MibTable
h3cDot11BSSTxStatisTable=_H3cDot11BSSTxStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,5))
if mibBuilder.loadTexts:h3cDot11BSSTxStatisTable.setStatus(_A)
_H3cDot11BSSTxStatisEntry_Object=MibTableRow
h3cDot11BSSTxStatisEntry=_H3cDot11BSSTxStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,5,1))
h3cDot11BSSTxStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_T))
if mibBuilder.loadTexts:h3cDot11BSSTxStatisEntry.setStatus(_A)
_H3cDot11BSSTxFrameCnt_Type=Counter32
_H3cDot11BSSTxFrameCnt_Object=MibTableColumn
h3cDot11BSSTxFrameCnt=_H3cDot11BSSTxFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,5,1,1),_H3cDot11BSSTxFrameCnt_Type())
h3cDot11BSSTxFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSTxFrameCnt.setStatus(_A)
_H3cDot11BSSTxFrameBytes_Type=Counter32
_H3cDot11BSSTxFrameBytes_Object=MibTableColumn
h3cDot11BSSTxFrameBytes=_H3cDot11BSSTxFrameBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,5,1,2),_H3cDot11BSSTxFrameBytes_Type())
h3cDot11BSSTxFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSTxFrameBytes.setStatus(_A)
_H3cDot11BSSTxDataFrameCnt_Type=Counter32
_H3cDot11BSSTxDataFrameCnt_Object=MibTableColumn
h3cDot11BSSTxDataFrameCnt=_H3cDot11BSSTxDataFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,5,1,3),_H3cDot11BSSTxDataFrameCnt_Type())
h3cDot11BSSTxDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSTxDataFrameCnt.setStatus(_A)
_H3cDot11BSSTxDataFrameBytes_Type=Counter32
_H3cDot11BSSTxDataFrameBytes_Object=MibTableColumn
h3cDot11BSSTxDataFrameBytes=_H3cDot11BSSTxDataFrameBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,5,1,4),_H3cDot11BSSTxDataFrameBytes_Type())
h3cDot11BSSTxDataFrameBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSTxDataFrameBytes.setStatus(_A)
_H3cDot11BSSTxAssociateFrameCnt_Type=Counter32
_H3cDot11BSSTxAssociateFrameCnt_Object=MibTableColumn
h3cDot11BSSTxAssociateFrameCnt=_H3cDot11BSSTxAssociateFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,5,1,5),_H3cDot11BSSTxAssociateFrameCnt_Type())
h3cDot11BSSTxAssociateFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSTxAssociateFrameCnt.setStatus(_A)
_H3cDot11BSSTxPayloadBytes_Type=Counter32
_H3cDot11BSSTxPayloadBytes_Object=MibTableColumn
h3cDot11BSSTxPayloadBytes=_H3cDot11BSSTxPayloadBytes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,5,1,6),_H3cDot11BSSTxPayloadBytes_Type())
h3cDot11BSSTxPayloadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSTxPayloadBytes.setStatus(_A)
_H3cDot11BSSTxRetryCnt_Type=Counter32
_H3cDot11BSSTxRetryCnt_Object=MibTableColumn
h3cDot11BSSTxRetryCnt=_H3cDot11BSSTxRetryCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,5,1,7),_H3cDot11BSSTxRetryCnt_Type())
h3cDot11BSSTxRetryCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSTxRetryCnt.setStatus(_A)
_H3cDot11BSSTxUniFrameCnt_Type=Counter32
_H3cDot11BSSTxUniFrameCnt_Object=MibTableColumn
h3cDot11BSSTxUniFrameCnt=_H3cDot11BSSTxUniFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,5,1,8),_H3cDot11BSSTxUniFrameCnt_Type())
h3cDot11BSSTxUniFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSTxUniFrameCnt.setStatus(_A)
_H3cDot11BSSTxNonUniFrameCnt_Type=Integer32
_H3cDot11BSSTxNonUniFrameCnt_Object=MibTableColumn
h3cDot11BSSTxNonUniFrameCnt=_H3cDot11BSSTxNonUniFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,5,1,9),_H3cDot11BSSTxNonUniFrameCnt_Type())
h3cDot11BSSTxNonUniFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSTxNonUniFrameCnt.setStatus(_A)
_H3cDot11BSSTxAuthenFrameCnt_Type=Counter32
_H3cDot11BSSTxAuthenFrameCnt_Object=MibTableColumn
h3cDot11BSSTxAuthenFrameCnt=_H3cDot11BSSTxAuthenFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,5,1,10),_H3cDot11BSSTxAuthenFrameCnt_Type())
h3cDot11BSSTxAuthenFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSTxAuthenFrameCnt.setStatus(_A)
_H3cDot11BSSAssocStatisTable_Object=MibTable
h3cDot11BSSAssocStatisTable=_H3cDot11BSSAssocStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,6))
if mibBuilder.loadTexts:h3cDot11BSSAssocStatisTable.setStatus(_A)
_H3cDot11BSSAssocStatisEntry_Object=MibTableRow
h3cDot11BSSAssocStatisEntry=_H3cDot11BSSAssocStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,6,1))
h3cDot11BSSAssocStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_T))
if mibBuilder.loadTexts:h3cDot11BSSAssocStatisEntry.setStatus(_A)
_H3cDot11BSSStationAssocSum_Type=Counter32
_H3cDot11BSSStationAssocSum_Object=MibTableColumn
h3cDot11BSSStationAssocSum=_H3cDot11BSSStationAssocSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,6,1,1),_H3cDot11BSSStationAssocSum_Type())
h3cDot11BSSStationAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSStationAssocSum.setStatus(_A)
_H3cDot11BSSStationAssocFailSum_Type=Counter32
_H3cDot11BSSStationAssocFailSum_Object=MibTableColumn
h3cDot11BSSStationAssocFailSum=_H3cDot11BSSStationAssocFailSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,6,1,2),_H3cDot11BSSStationAssocFailSum_Type())
h3cDot11BSSStationAssocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSStationAssocFailSum.setStatus(_A)
_H3cDot11BSSStationReassocSum_Type=Counter32
_H3cDot11BSSStationReassocSum_Object=MibTableColumn
h3cDot11BSSStationReassocSum=_H3cDot11BSSStationReassocSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,6,1,3),_H3cDot11BSSStationReassocSum_Type())
h3cDot11BSSStationReassocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSStationReassocSum.setStatus(_A)
_H3cDot11BSSStationAssocRejectSum_Type=Counter32
_H3cDot11BSSStationAssocRejectSum_Object=MibTableColumn
h3cDot11BSSStationAssocRejectSum=_H3cDot11BSSStationAssocRejectSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,6,1,4),_H3cDot11BSSStationAssocRejectSum_Type())
h3cDot11BSSStationAssocRejectSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSStationAssocRejectSum.setStatus(_A)
_H3cDot11BSSStationExDeAssocSum_Type=Counter32
_H3cDot11BSSStationExDeAssocSum_Object=MibTableColumn
h3cDot11BSSStationExDeAssocSum=_H3cDot11BSSStationExDeAssocSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,6,1,5),_H3cDot11BSSStationExDeAssocSum_Type())
h3cDot11BSSStationExDeAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSStationExDeAssocSum.setStatus(_A)
_H3cDot11BSSStationCurAssocSum_Type=Integer32
_H3cDot11BSSStationCurAssocSum_Object=MibTableColumn
h3cDot11BSSStationCurAssocSum=_H3cDot11BSSStationCurAssocSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,6,1,6),_H3cDot11BSSStationCurAssocSum_Type())
h3cDot11BSSStationCurAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSStationCurAssocSum.setStatus(_A)
_H3cDot11BSSStationAssocReqSum_Type=Counter32
_H3cDot11BSSStationAssocReqSum_Object=MibTableColumn
h3cDot11BSSStationAssocReqSum=_H3cDot11BSSStationAssocReqSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,6,1,7),_H3cDot11BSSStationAssocReqSum_Type())
h3cDot11BSSStationAssocReqSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSStationAssocReqSum.setStatus(_A)
_H3cDot11BSSStationCurAuthSum_Type=Integer32
_H3cDot11BSSStationCurAuthSum_Object=MibTableColumn
h3cDot11BSSStationCurAuthSum=_H3cDot11BSSStationCurAuthSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,6,1,8),_H3cDot11BSSStationCurAuthSum_Type())
h3cDot11BSSStationCurAuthSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BSSStationCurAuthSum.setStatus(_A)
_H3cDot11APLinkStatisTable_Object=MibTable
h3cDot11APLinkStatisTable=_H3cDot11APLinkStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,7))
if mibBuilder.loadTexts:h3cDot11APLinkStatisTable.setStatus(_A)
_H3cDot11APLinkStatisEntry_Object=MibTableRow
h3cDot11APLinkStatisEntry=_H3cDot11APLinkStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,7,1))
h3cDot11APLinkStatisEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:h3cDot11APLinkStatisEntry.setStatus(_A)
_H3cDot11UpLinkUpDownTimes_Type=Counter32
_H3cDot11UpLinkUpDownTimes_Object=MibTableColumn
h3cDot11UpLinkUpDownTimes=_H3cDot11UpLinkUpDownTimes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,7,1,1),_H3cDot11UpLinkUpDownTimes_Type())
h3cDot11UpLinkUpDownTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11UpLinkUpDownTimes.setStatus(_A)
_H3cDot11DownLinkUpDownTimes_Type=Counter32
_H3cDot11DownLinkUpDownTimes_Object=MibTableColumn
h3cDot11DownLinkUpDownTimes=_H3cDot11DownLinkUpDownTimes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,7,1,2),_H3cDot11DownLinkUpDownTimes_Type())
h3cDot11DownLinkUpDownTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DownLinkUpDownTimes.setStatus(_A)
_H3cDot11RadioAssocStatisTable_Object=MibTable
h3cDot11RadioAssocStatisTable=_H3cDot11RadioAssocStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,8))
if mibBuilder.loadTexts:h3cDot11RadioAssocStatisTable.setStatus(_A)
_H3cDot11RadioAssocStatisEntry_Object=MibTableRow
h3cDot11RadioAssocStatisEntry=_H3cDot11RadioAssocStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,8,1))
h3cDot11RadioAssocStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:h3cDot11RadioAssocStatisEntry.setStatus(_A)
_H3cDot11RadioStaAssocSum_Type=Counter32
_H3cDot11RadioStaAssocSum_Object=MibTableColumn
h3cDot11RadioStaAssocSum=_H3cDot11RadioStaAssocSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,8,1,1),_H3cDot11RadioStaAssocSum_Type())
h3cDot11RadioStaAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioStaAssocSum.setStatus(_A)
_H3cDot11RadioStaAssocFailSum_Type=Counter32
_H3cDot11RadioStaAssocFailSum_Object=MibTableColumn
h3cDot11RadioStaAssocFailSum=_H3cDot11RadioStaAssocFailSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,8,1,2),_H3cDot11RadioStaAssocFailSum_Type())
h3cDot11RadioStaAssocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioStaAssocFailSum.setStatus(_A)
_H3cDot11RadioStaReassocSum_Type=Counter32
_H3cDot11RadioStaReassocSum_Object=MibTableColumn
h3cDot11RadioStaReassocSum=_H3cDot11RadioStaReassocSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,8,1,3),_H3cDot11RadioStaReassocSum_Type())
h3cDot11RadioStaReassocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioStaReassocSum.setStatus(_A)
_H3cDot11RadioStaAssocRejectSum_Type=Counter32
_H3cDot11RadioStaAssocRejectSum_Object=MibTableColumn
h3cDot11RadioStaAssocRejectSum=_H3cDot11RadioStaAssocRejectSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,8,1,4),_H3cDot11RadioStaAssocRejectSum_Type())
h3cDot11RadioStaAssocRejectSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioStaAssocRejectSum.setStatus(_A)
_H3cDot11RadioStaExDeAssocSum_Type=Counter32
_H3cDot11RadioStaExDeAssocSum_Object=MibTableColumn
h3cDot11RadioStaExDeAssocSum=_H3cDot11RadioStaExDeAssocSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,8,1,5),_H3cDot11RadioStaExDeAssocSum_Type())
h3cDot11RadioStaExDeAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioStaExDeAssocSum.setStatus(_A)
_H3cDot11RadioStaCurAssocSum_Type=Integer32
_H3cDot11RadioStaCurAssocSum_Object=MibTableColumn
h3cDot11RadioStaCurAssocSum=_H3cDot11RadioStaCurAssocSum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,8,1,6),_H3cDot11RadioStaCurAssocSum_Type())
h3cDot11RadioStaCurAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioStaCurAssocSum.setStatus(_A)
_H3cDot11RadioMngFrameStatisTable_Object=MibTable
h3cDot11RadioMngFrameStatisTable=_H3cDot11RadioMngFrameStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,9))
if mibBuilder.loadTexts:h3cDot11RadioMngFrameStatisTable.setStatus(_A)
_H3cDot11RadioMngFrameStatisEntry_Object=MibTableRow
h3cDot11RadioMngFrameStatisEntry=_H3cDot11RadioMngFrameStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,9,1))
h3cDot11RadioMngFrameStatisEntry.setIndexNames((0,_C,_y),(0,_C,_z))
if mibBuilder.loadTexts:h3cDot11RadioMngFrameStatisEntry.setStatus(_A)
_H3cDot11RadioStatisIndex_Type=H3cDot11RadioElementIndex
_H3cDot11RadioStatisIndex_Object=MibTableColumn
h3cDot11RadioStatisIndex=_H3cDot11RadioStatisIndex_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,9,1,1),_H3cDot11RadioStatisIndex_Type())
h3cDot11RadioStatisIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11RadioStatisIndex.setStatus(_A)
class _H3cDot11MngFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('assocReq',1),(_A0,2),(_A1,3),(_A2,4),('probeReq',5),(_A3,6),('beacon',7),('atim',8),(_A4,9),(_A5,10),(_A6,11),('action',12)))
_H3cDot11MngFrameType_Type.__name__=_D
_H3cDot11MngFrameType_Object=MibTableColumn
h3cDot11MngFrameType=_H3cDot11MngFrameType_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,9,1,2),_H3cDot11MngFrameType_Type())
h3cDot11MngFrameType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11MngFrameType.setStatus(_A)
_H3cDot11MngFrameCnt_Type=Counter32
_H3cDot11MngFrameCnt_Object=MibTableColumn
h3cDot11MngFrameCnt=_H3cDot11MngFrameCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,9,1,3),_H3cDot11MngFrameCnt_Type())
h3cDot11MngFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MngFrameCnt.setStatus(_A)
_H3cDot11APAuthFailStatisTable_Object=MibTable
h3cDot11APAuthFailStatisTable=_H3cDot11APAuthFailStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,10))
if mibBuilder.loadTexts:h3cDot11APAuthFailStatisTable.setStatus(_A)
_H3cDot11APAuthFailStatisEntry_Object=MibTableRow
h3cDot11APAuthFailStatisEntry=_H3cDot11APAuthFailStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,10,1))
h3cDot11APAuthFailStatisEntry.setIndexNames((0,_C,_E),(0,_C,_A7))
if mibBuilder.loadTexts:h3cDot11APAuthFailStatisEntry.setStatus(_A)
class _H3cDot11APAuthFailStatisType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3),(_O,4)))
_H3cDot11APAuthFailStatisType_Type.__name__=_D
_H3cDot11APAuthFailStatisType_Object=MibTableColumn
h3cDot11APAuthFailStatisType=_H3cDot11APAuthFailStatisType_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,10,1,1),_H3cDot11APAuthFailStatisType_Type())
h3cDot11APAuthFailStatisType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11APAuthFailStatisType.setStatus(_A)
_H3cDot11APAuthFailStatisCnt_Type=Counter32
_H3cDot11APAuthFailStatisCnt_Object=MibTableColumn
h3cDot11APAuthFailStatisCnt=_H3cDot11APAuthFailStatisCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,10,1,2),_H3cDot11APAuthFailStatisCnt_Type())
h3cDot11APAuthFailStatisCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APAuthFailStatisCnt.setStatus(_A)
_H3cDot11APAssocFailStatisTable_Object=MibTable
h3cDot11APAssocFailStatisTable=_H3cDot11APAssocFailStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,11))
if mibBuilder.loadTexts:h3cDot11APAssocFailStatisTable.setStatus(_A)
_H3cDot11APAssocFailStatisEntry_Object=MibTableRow
h3cDot11APAssocFailStatisEntry=_H3cDot11APAssocFailStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,11,1))
h3cDot11APAssocFailStatisEntry.setIndexNames((0,_C,_E),(0,_C,_A8))
if mibBuilder.loadTexts:h3cDot11APAssocFailStatisEntry.setStatus(_A)
class _H3cDot11APAssocFailStatisType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3),(_O,4)))
_H3cDot11APAssocFailStatisType_Type.__name__=_D
_H3cDot11APAssocFailStatisType_Object=MibTableColumn
h3cDot11APAssocFailStatisType=_H3cDot11APAssocFailStatisType_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,11,1,1),_H3cDot11APAssocFailStatisType_Type())
h3cDot11APAssocFailStatisType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11APAssocFailStatisType.setStatus(_A)
_H3cDot11APAssocFailStatisCnt_Type=Counter32
_H3cDot11APAssocFailStatisCnt_Object=MibTableColumn
h3cDot11APAssocFailStatisCnt=_H3cDot11APAssocFailStatisCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,11,1,2),_H3cDot11APAssocFailStatisCnt_Type())
h3cDot11APAssocFailStatisCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APAssocFailStatisCnt.setStatus(_A)
_H3cDot11APReassocStatisTable_Object=MibTable
h3cDot11APReassocStatisTable=_H3cDot11APReassocStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,12))
if mibBuilder.loadTexts:h3cDot11APReassocStatisTable.setStatus(_A)
_H3cDot11APReassocStatisEntry_Object=MibTableRow
h3cDot11APReassocStatisEntry=_H3cDot11APReassocStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,12,1))
h3cDot11APReassocStatisEntry.setIndexNames((0,_C,_E),(0,_C,_A9))
if mibBuilder.loadTexts:h3cDot11APReassocStatisEntry.setStatus(_A)
class _H3cDot11APReassocStatisType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Z,1),('success',2),(_W,3),(_X,4),(_Y,5),(_O,6)))
_H3cDot11APReassocStatisType_Type.__name__=_D
_H3cDot11APReassocStatisType_Object=MibTableColumn
h3cDot11APReassocStatisType=_H3cDot11APReassocStatisType_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,12,1,1),_H3cDot11APReassocStatisType_Type())
h3cDot11APReassocStatisType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11APReassocStatisType.setStatus(_A)
_H3cDot11APReassocStatisCnt_Type=Counter32
_H3cDot11APReassocStatisCnt_Object=MibTableColumn
h3cDot11APReassocStatisCnt=_H3cDot11APReassocStatisCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,12,1,2),_H3cDot11APReassocStatisCnt_Type())
h3cDot11APReassocStatisCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APReassocStatisCnt.setStatus(_A)
_H3cDot11APUserAuthStatisTable_Object=MibTable
h3cDot11APUserAuthStatisTable=_H3cDot11APUserAuthStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,13))
if mibBuilder.loadTexts:h3cDot11APUserAuthStatisTable.setStatus(_A)
_H3cDot11APUserAuthStatisEntry_Object=MibTableRow
h3cDot11APUserAuthStatisEntry=_H3cDot11APUserAuthStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,13,1))
h3cDot11APUserAuthStatisEntry.setIndexNames((0,_C,_E),(0,_C,_AA))
if mibBuilder.loadTexts:h3cDot11APUserAuthStatisEntry.setStatus(_A)
class _H3cDot11UserAuthStatisType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Z,1),('success',2),('keyError',3),(_W,4),(_X,5),(_Y,6),(_O,7)))
_H3cDot11UserAuthStatisType_Type.__name__=_D
_H3cDot11UserAuthStatisType_Object=MibTableColumn
h3cDot11UserAuthStatisType=_H3cDot11UserAuthStatisType_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,13,1,1),_H3cDot11UserAuthStatisType_Type())
h3cDot11UserAuthStatisType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11UserAuthStatisType.setStatus(_A)
_H3cDot11UserAuthStatisCnt_Type=Counter32
_H3cDot11UserAuthStatisCnt_Object=MibTableColumn
h3cDot11UserAuthStatisCnt=_H3cDot11UserAuthStatisCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,13,1,2),_H3cDot11UserAuthStatisCnt_Type())
h3cDot11UserAuthStatisCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11UserAuthStatisCnt.setStatus(_A)
_H3cDot11APDeauthStatisTable_Object=MibTable
h3cDot11APDeauthStatisTable=_H3cDot11APDeauthStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,14))
if mibBuilder.loadTexts:h3cDot11APDeauthStatisTable.setStatus(_A)
_H3cDot11APDeauthStatisEntry_Object=MibTableRow
h3cDot11APDeauthStatisEntry=_H3cDot11APDeauthStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,14,1))
h3cDot11APDeauthStatisEntry.setIndexNames((0,_C,_E),(0,_C,_AB))
if mibBuilder.loadTexts:h3cDot11APDeauthStatisEntry.setStatus(_A)
class _H3cDot11APDeauthStatisType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Z,1),(_AC,2),(_e,3),(_AD,4),(_O,5)))
_H3cDot11APDeauthStatisType_Type.__name__=_D
_H3cDot11APDeauthStatisType_Object=MibTableColumn
h3cDot11APDeauthStatisType=_H3cDot11APDeauthStatisType_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,14,1,1),_H3cDot11APDeauthStatisType_Type())
h3cDot11APDeauthStatisType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11APDeauthStatisType.setStatus(_A)
_H3cDot11APDeauthStatisCnt_Type=Counter32
_H3cDot11APDeauthStatisCnt_Object=MibTableColumn
h3cDot11APDeauthStatisCnt=_H3cDot11APDeauthStatisCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,14,1,2),_H3cDot11APDeauthStatisCnt_Type())
h3cDot11APDeauthStatisCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APDeauthStatisCnt.setStatus(_A)
_H3cDot11APDeassocStatisTable_Object=MibTable
h3cDot11APDeassocStatisTable=_H3cDot11APDeassocStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,15))
if mibBuilder.loadTexts:h3cDot11APDeassocStatisTable.setStatus(_A)
_H3cDot11APDeassocStatisEntry_Object=MibTableRow
h3cDot11APDeassocStatisEntry=_H3cDot11APDeassocStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,15,1))
h3cDot11APDeassocStatisEntry.setIndexNames((0,_C,_E),(0,_C,_AE))
if mibBuilder.loadTexts:h3cDot11APDeassocStatisEntry.setStatus(_A)
class _H3cDot11APDeassocStatisType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Z,1),(_AC,2),(_e,3),(_AD,4),(_O,5)))
_H3cDot11APDeassocStatisType_Type.__name__=_D
_H3cDot11APDeassocStatisType_Object=MibTableColumn
h3cDot11APDeassocStatisType=_H3cDot11APDeassocStatisType_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,15,1,1),_H3cDot11APDeassocStatisType_Type())
h3cDot11APDeassocStatisType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11APDeassocStatisType.setStatus(_A)
_H3cDot11APDeassocStatisCnt_Type=Counter32
_H3cDot11APDeassocStatisCnt_Object=MibTableColumn
h3cDot11APDeassocStatisCnt=_H3cDot11APDeassocStatisCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,15,1,2),_H3cDot11APDeassocStatisCnt_Type())
h3cDot11APDeassocStatisCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APDeassocStatisCnt.setStatus(_A)
_H3cDot11APAssocFailStatis2Table_Object=MibTable
h3cDot11APAssocFailStatis2Table=_H3cDot11APAssocFailStatis2Table_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,16))
if mibBuilder.loadTexts:h3cDot11APAssocFailStatis2Table.setStatus(_A)
_H3cDot11APAssocFailStatis2Entry_Object=MibTableRow
h3cDot11APAssocFailStatis2Entry=_H3cDot11APAssocFailStatis2Entry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,16,1))
h3cDot11APAssocFailStatis2Entry.setIndexNames((0,_C,_E),(0,_C,_AF))
if mibBuilder.loadTexts:h3cDot11APAssocFailStatis2Entry.setStatus(_A)
class _H3cDot11APAssocFailStatis2Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_e,1),('notSupportRateSet',2),('unknownReasonCode',3),(_O,4)))
_H3cDot11APAssocFailStatis2Type_Type.__name__=_D
_H3cDot11APAssocFailStatis2Type_Object=MibTableColumn
h3cDot11APAssocFailStatis2Type=_H3cDot11APAssocFailStatis2Type_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,16,1,1),_H3cDot11APAssocFailStatis2Type_Type())
h3cDot11APAssocFailStatis2Type.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11APAssocFailStatis2Type.setStatus(_A)
_H3cDot11APAssocFailStatis2Cnt_Type=Counter32
_H3cDot11APAssocFailStatis2Cnt_Object=MibTableColumn
h3cDot11APAssocFailStatis2Cnt=_H3cDot11APAssocFailStatis2Cnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,16,1,2),_H3cDot11APAssocFailStatis2Cnt_Type())
h3cDot11APAssocFailStatis2Cnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APAssocFailStatis2Cnt.setStatus(_A)
_H3cDot11APIfStatisTable_Object=MibTable
h3cDot11APIfStatisTable=_H3cDot11APIfStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17))
if mibBuilder.loadTexts:h3cDot11APIfStatisTable.setStatus(_A)
_H3cDot11APIfStatisEntry_Object=MibTableRow
h3cDot11APIfStatisEntry=_H3cDot11APIfStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1))
h3cDot11APIfStatisEntry.setIndexNames((0,_a,_b),(0,_C,_V))
if mibBuilder.loadTexts:h3cDot11APIfStatisEntry.setStatus(_A)
_H3cDot11APIfInPkts_Type=Counter32
_H3cDot11APIfInPkts_Object=MibTableColumn
h3cDot11APIfInPkts=_H3cDot11APIfInPkts_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,1),_H3cDot11APIfInPkts_Type())
h3cDot11APIfInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInPkts.setStatus(_A)
_H3cDot11APIfInNormalPkts_Type=Counter32
_H3cDot11APIfInNormalPkts_Object=MibTableColumn
h3cDot11APIfInNormalPkts=_H3cDot11APIfInNormalPkts_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,2),_H3cDot11APIfInNormalPkts_Type())
h3cDot11APIfInNormalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInNormalPkts.setStatus(_A)
_H3cDot11APIfInErrorPkts_Type=Counter32
_H3cDot11APIfInErrorPkts_Object=MibTableColumn
h3cDot11APIfInErrorPkts=_H3cDot11APIfInErrorPkts_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,3),_H3cDot11APIfInErrorPkts_Type())
h3cDot11APIfInErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInErrorPkts.setStatus(_A)
_H3cDot11APIfOutPkts_Type=Counter32
_H3cDot11APIfOutPkts_Object=MibTableColumn
h3cDot11APIfOutPkts=_H3cDot11APIfOutPkts_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,4),_H3cDot11APIfOutPkts_Type())
h3cDot11APIfOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutPkts.setStatus(_A)
_H3cDot11APIfInOctets_Type=Counter32
_H3cDot11APIfInOctets_Object=MibTableColumn
h3cDot11APIfInOctets=_H3cDot11APIfInOctets_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,5),_H3cDot11APIfInOctets_Type())
h3cDot11APIfInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInOctets.setStatus(_A)
_H3cDot11APIfOutOctets_Type=Counter32
_H3cDot11APIfOutOctets_Object=MibTableColumn
h3cDot11APIfOutOctets=_H3cDot11APIfOutOctets_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,6),_H3cDot11APIfOutOctets_Type())
h3cDot11APIfOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutOctets.setStatus(_A)
_H3cDot11APIfFlowOut_Type=Unsigned32
_H3cDot11APIfFlowOut_Object=MibTableColumn
h3cDot11APIfFlowOut=_H3cDot11APIfFlowOut_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,7),_H3cDot11APIfFlowOut_Type())
h3cDot11APIfFlowOut.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfFlowOut.setStatus(_A)
_H3cDot11APIfFlowIN_Type=Unsigned32
_H3cDot11APIfFlowIN_Object=MibTableColumn
h3cDot11APIfFlowIN=_H3cDot11APIfFlowIN_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,8),_H3cDot11APIfFlowIN_Type())
h3cDot11APIfFlowIN.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfFlowIN.setStatus(_A)
_H3cDot11APIfInUcastPkts_Type=Counter32
_H3cDot11APIfInUcastPkts_Object=MibTableColumn
h3cDot11APIfInUcastPkts=_H3cDot11APIfInUcastPkts_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,9),_H3cDot11APIfInUcastPkts_Type())
h3cDot11APIfInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInUcastPkts.setStatus(_A)
_H3cDot11APIfInNUcastPkts_Type=Counter32
_H3cDot11APIfInNUcastPkts_Object=MibTableColumn
h3cDot11APIfInNUcastPkts=_H3cDot11APIfInNUcastPkts_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,10),_H3cDot11APIfInNUcastPkts_Type())
h3cDot11APIfInNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInNUcastPkts.setStatus(_A)
_H3cDot11APIfInDiscardPkts_Type=Counter32
_H3cDot11APIfInDiscardPkts_Object=MibTableColumn
h3cDot11APIfInDiscardPkts=_H3cDot11APIfInDiscardPkts_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,11),_H3cDot11APIfInDiscardPkts_Type())
h3cDot11APIfInDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInDiscardPkts.setStatus(_A)
_H3cDot11APIfOutUcastPkts_Type=Counter32
_H3cDot11APIfOutUcastPkts_Object=MibTableColumn
h3cDot11APIfOutUcastPkts=_H3cDot11APIfOutUcastPkts_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,12),_H3cDot11APIfOutUcastPkts_Type())
h3cDot11APIfOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutUcastPkts.setStatus(_A)
_H3cDot11APIfOutNUcastPkts_Type=Counter32
_H3cDot11APIfOutNUcastPkts_Object=MibTableColumn
h3cDot11APIfOutNUcastPkts=_H3cDot11APIfOutNUcastPkts_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,13),_H3cDot11APIfOutNUcastPkts_Type())
h3cDot11APIfOutNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutNUcastPkts.setStatus(_A)
_H3cDot11APIfOutDiscardPkts_Type=Counter32
_H3cDot11APIfOutDiscardPkts_Object=MibTableColumn
h3cDot11APIfOutDiscardPkts=_H3cDot11APIfOutDiscardPkts_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,14),_H3cDot11APIfOutDiscardPkts_Type())
h3cDot11APIfOutDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutDiscardPkts.setStatus(_A)
_H3cDot11APIfOutErrorPkts_Type=Counter32
_H3cDot11APIfOutErrorPkts_Object=MibTableColumn
h3cDot11APIfOutErrorPkts=_H3cDot11APIfOutErrorPkts_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,15),_H3cDot11APIfOutErrorPkts_Type())
h3cDot11APIfOutErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutErrorPkts.setStatus(_A)
_H3cDot11APIfUpdownTimes_Type=Counter32
_H3cDot11APIfUpdownTimes_Object=MibTableColumn
h3cDot11APIfUpdownTimes=_H3cDot11APIfUpdownTimes_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,16),_H3cDot11APIfUpdownTimes_Type())
h3cDot11APIfUpdownTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfUpdownTimes.setStatus(_A)
_H3cDot11APIfStatusKeepTime_Type=TimeTicks
_H3cDot11APIfStatusKeepTime_Object=MibTableColumn
h3cDot11APIfStatusKeepTime=_H3cDot11APIfStatusKeepTime_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,17),_H3cDot11APIfStatusKeepTime_Type())
h3cDot11APIfStatusKeepTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfStatusKeepTime.setStatus(_A)
class _H3cDot11APIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),(_f,4),('dormant',5),(_AG,6),(_AH,7)))
_H3cDot11APIfOperStatus_Type.__name__=_D
_H3cDot11APIfOperStatus_Object=MibTableColumn
h3cDot11APIfOperStatus=_H3cDot11APIfOperStatus_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,18),_H3cDot11APIfOperStatus_Type())
h3cDot11APIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOperStatus.setStatus(_A)
_H3cDot11APIfInBrdcastPkts_Type=Counter64
_H3cDot11APIfInBrdcastPkts_Object=MibTableColumn
h3cDot11APIfInBrdcastPkts=_H3cDot11APIfInBrdcastPkts_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,19),_H3cDot11APIfInBrdcastPkts_Type())
h3cDot11APIfInBrdcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInBrdcastPkts.setStatus(_A)
_H3cDot11APIfOutBrdcastPkts_Type=Counter64
_H3cDot11APIfOutBrdcastPkts_Object=MibTableColumn
h3cDot11APIfOutBrdcastPkts=_H3cDot11APIfOutBrdcastPkts_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,20),_H3cDot11APIfOutBrdcastPkts_Type())
h3cDot11APIfOutBrdcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutBrdcastPkts.setStatus(_A)
_H3cDot11APIfInMulcastPkts_Type=Counter64
_H3cDot11APIfInMulcastPkts_Object=MibTableColumn
h3cDot11APIfInMulcastPkts=_H3cDot11APIfInMulcastPkts_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,21),_H3cDot11APIfInMulcastPkts_Type())
h3cDot11APIfInMulcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInMulcastPkts.setStatus(_A)
_H3cDot11APIfOutMulcastPkts_Type=Counter64
_H3cDot11APIfOutMulcastPkts_Object=MibTableColumn
h3cDot11APIfOutMulcastPkts=_H3cDot11APIfOutMulcastPkts_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,22),_H3cDot11APIfOutMulcastPkts_Type())
h3cDot11APIfOutMulcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutMulcastPkts.setStatus(_A)
_H3cDot11APIfInPayloadOctets_Type=Counter64
_H3cDot11APIfInPayloadOctets_Object=MibTableColumn
h3cDot11APIfInPayloadOctets=_H3cDot11APIfInPayloadOctets_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,23),_H3cDot11APIfInPayloadOctets_Type())
h3cDot11APIfInPayloadOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInPayloadOctets.setStatus(_A)
_H3cDot11APIfOutPayloadOctets_Type=Counter64
_H3cDot11APIfOutPayloadOctets_Object=MibTableColumn
h3cDot11APIfOutPayloadOctets=_H3cDot11APIfOutPayloadOctets_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,17,1,24),_H3cDot11APIfOutPayloadOctets_Type())
h3cDot11APIfOutPayloadOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutPayloadOctets.setStatus(_A)
_H3cDot11RadioMngFrmStatisTable_Object=MibTable
h3cDot11RadioMngFrmStatisTable=_H3cDot11RadioMngFrmStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,18))
if mibBuilder.loadTexts:h3cDot11RadioMngFrmStatisTable.setStatus(_A)
_H3cDot11RadioMngFrmStatisEntry_Object=MibTableRow
h3cDot11RadioMngFrmStatisEntry=_H3cDot11RadioMngFrmStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,18,1))
h3cDot11RadioMngFrmStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_AI))
if mibBuilder.loadTexts:h3cDot11RadioMngFrmStatisEntry.setStatus(_A)
class _H3cDot11MngFrmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('assocReq',1),(_A0,2),(_A1,3),(_A2,4),('probeReq',5),(_A3,6),('beacon',7),('atim',8),(_A4,9),(_A5,10),(_A6,11),('action',12)))
_H3cDot11MngFrmType_Type.__name__=_D
_H3cDot11MngFrmType_Object=MibTableColumn
h3cDot11MngFrmType=_H3cDot11MngFrmType_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,18,1,1),_H3cDot11MngFrmType_Type())
h3cDot11MngFrmType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11MngFrmType.setStatus(_A)
_H3cDot11MngFrmCnt_Type=Counter32
_H3cDot11MngFrmCnt_Object=MibTableColumn
h3cDot11MngFrmCnt=_H3cDot11MngFrmCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,18,1,2),_H3cDot11MngFrmCnt_Type())
h3cDot11MngFrmCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MngFrmCnt.setStatus(_A)
_H3cDot11APPacketSizeStatisTable_Object=MibTable
h3cDot11APPacketSizeStatisTable=_H3cDot11APPacketSizeStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,19))
if mibBuilder.loadTexts:h3cDot11APPacketSizeStatisTable.setStatus(_A)
_H3cDot11APPacketSizeStatisEntry_Object=MibTableRow
h3cDot11APPacketSizeStatisEntry=_H3cDot11APPacketSizeStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,19,1))
h3cDot11APPacketSizeStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_AJ))
if mibBuilder.loadTexts:h3cDot11APPacketSizeStatisEntry.setStatus(_A)
class _H3cDot11APPacketSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sizeLevel1',1),('sizeLevel2',2),('sizeLevel3',3),('sizeLevel4',4)))
_H3cDot11APPacketSize_Type.__name__=_D
_H3cDot11APPacketSize_Object=MibTableColumn
h3cDot11APPacketSize=_H3cDot11APPacketSize_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,19,1,1),_H3cDot11APPacketSize_Type())
h3cDot11APPacketSize.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11APPacketSize.setStatus(_A)
_H3cDot11APRXPacketSizeCount_Type=Counter64
_H3cDot11APRXPacketSizeCount_Object=MibTableColumn
h3cDot11APRXPacketSizeCount=_H3cDot11APRXPacketSizeCount_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,19,1,2),_H3cDot11APRXPacketSizeCount_Type())
h3cDot11APRXPacketSizeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APRXPacketSizeCount.setStatus(_A)
_H3cDot11APTXPacketSizeCount_Type=Counter64
_H3cDot11APTXPacketSizeCount_Object=MibTableColumn
h3cDot11APTXPacketSizeCount=_H3cDot11APTXPacketSizeCount_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,19,1,3),_H3cDot11APTXPacketSizeCount_Type())
h3cDot11APTXPacketSizeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APTXPacketSizeCount.setStatus(_A)
_H3cDot11APPacketRateStatisTable_Object=MibTable
h3cDot11APPacketRateStatisTable=_H3cDot11APPacketRateStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,20))
if mibBuilder.loadTexts:h3cDot11APPacketRateStatisTable.setStatus(_A)
_H3cDot11APPacketRateStatisEntry_Object=MibTableRow
h3cDot11APPacketRateStatisEntry=_H3cDot11APPacketRateStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,20,1))
h3cDot11APPacketRateStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_AK))
if mibBuilder.loadTexts:h3cDot11APPacketRateStatisEntry.setStatus(_A)
_H3cDot11APPacketRate_Type=Integer32
_H3cDot11APPacketRate_Object=MibTableColumn
h3cDot11APPacketRate=_H3cDot11APPacketRate_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,20,1,1),_H3cDot11APPacketRate_Type())
h3cDot11APPacketRate.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11APPacketRate.setStatus(_A)
_H3cDot11APRXPacketRateCount_Type=Counter64
_H3cDot11APRXPacketRateCount_Object=MibTableColumn
h3cDot11APRXPacketRateCount=_H3cDot11APRXPacketRateCount_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,20,1,2),_H3cDot11APRXPacketRateCount_Type())
h3cDot11APRXPacketRateCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APRXPacketRateCount.setStatus(_A)
_H3cDot11APTXPacketRateCount_Type=Counter64
_H3cDot11APTXPacketRateCount_Object=MibTableColumn
h3cDot11APTXPacketRateCount=_H3cDot11APTXPacketRateCount_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,20,1,3),_H3cDot11APTXPacketRateCount_Type())
h3cDot11APTXPacketRateCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APTXPacketRateCount.setStatus(_A)
_H3cDot11APPacketMCSRateStatisTable_Object=MibTable
h3cDot11APPacketMCSRateStatisTable=_H3cDot11APPacketMCSRateStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,21))
if mibBuilder.loadTexts:h3cDot11APPacketMCSRateStatisTable.setStatus(_A)
_H3cDot11APPacketMCSRateStatisEntry_Object=MibTableRow
h3cDot11APPacketMCSRateStatisEntry=_H3cDot11APPacketMCSRateStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,21,1))
h3cDot11APPacketMCSRateStatisEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_AL))
if mibBuilder.loadTexts:h3cDot11APPacketMCSRateStatisEntry.setStatus(_A)
_H3cDot11APPacketMCSRate_Type=Integer32
_H3cDot11APPacketMCSRate_Object=MibTableColumn
h3cDot11APPacketMCSRate=_H3cDot11APPacketMCSRate_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,21,1,1),_H3cDot11APPacketMCSRate_Type())
h3cDot11APPacketMCSRate.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11APPacketMCSRate.setStatus(_A)
_H3cDot11APRXPacketMCSRateCount_Type=Counter64
_H3cDot11APRXPacketMCSRateCount_Object=MibTableColumn
h3cDot11APRXPacketMCSRateCount=_H3cDot11APRXPacketMCSRateCount_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,21,1,2),_H3cDot11APRXPacketMCSRateCount_Type())
h3cDot11APRXPacketMCSRateCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APRXPacketMCSRateCount.setStatus(_A)
_H3cDot11APTXPacketMCSRateCount_Type=Counter64
_H3cDot11APTXPacketMCSRateCount_Object=MibTableColumn
h3cDot11APTXPacketMCSRateCount=_H3cDot11APTXPacketMCSRateCount_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,21,1,3),_H3cDot11APTXPacketMCSRateCount_Type())
h3cDot11APTXPacketMCSRateCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APTXPacketMCSRateCount.setStatus(_A)
_H3cDot11APAssocFailStatis3Table_Object=MibTable
h3cDot11APAssocFailStatis3Table=_H3cDot11APAssocFailStatis3Table_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,22))
if mibBuilder.loadTexts:h3cDot11APAssocFailStatis3Table.setStatus(_A)
_H3cDot11APAssocFailStatis3Entry_Object=MibTableRow
h3cDot11APAssocFailStatis3Entry=_H3cDot11APAssocFailStatis3Entry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,22,1))
h3cDot11APAssocFailStatis3Entry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:h3cDot11APAssocFailStatis3Entry.setStatus(_A)
_H3cDot11APAssocFailStatis3SRCnt_Type=Counter32
_H3cDot11APAssocFailStatis3SRCnt_Object=MibTableColumn
h3cDot11APAssocFailStatis3SRCnt=_H3cDot11APAssocFailStatis3SRCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,22,1,1),_H3cDot11APAssocFailStatis3SRCnt_Type())
h3cDot11APAssocFailStatis3SRCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APAssocFailStatis3SRCnt.setStatus(_A)
_H3cDot11APAssocFailStatis3NSRCnt_Type=Counter32
_H3cDot11APAssocFailStatis3NSRCnt_Object=MibTableColumn
h3cDot11APAssocFailStatis3NSRCnt=_H3cDot11APAssocFailStatis3NSRCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,22,1,2),_H3cDot11APAssocFailStatis3NSRCnt_Type())
h3cDot11APAssocFailStatis3NSRCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APAssocFailStatis3NSRCnt.setStatus(_A)
_H3cDot11APAssocFailStatis3URCCnt_Type=Counter32
_H3cDot11APAssocFailStatis3URCCnt_Object=MibTableColumn
h3cDot11APAssocFailStatis3URCCnt=_H3cDot11APAssocFailStatis3URCCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,22,1,3),_H3cDot11APAssocFailStatis3URCCnt_Type())
h3cDot11APAssocFailStatis3URCCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APAssocFailStatis3URCCnt.setStatus(_A)
_H3cDot11APAssocFailStatis3RFCnt_Type=Counter32
_H3cDot11APAssocFailStatis3RFCnt_Object=MibTableColumn
h3cDot11APAssocFailStatis3RFCnt=_H3cDot11APAssocFailStatis3RFCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,22,1,4),_H3cDot11APAssocFailStatis3RFCnt_Type())
h3cDot11APAssocFailStatis3RFCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APAssocFailStatis3RFCnt.setStatus(_A)
_H3cDot11APAssocFailStatis3OtherCnt_Type=Counter32
_H3cDot11APAssocFailStatis3OtherCnt_Object=MibTableColumn
h3cDot11APAssocFailStatis3OtherCnt=_H3cDot11APAssocFailStatis3OtherCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,22,1,5),_H3cDot11APAssocFailStatis3OtherCnt_Type())
h3cDot11APAssocFailStatis3OtherCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APAssocFailStatis3OtherCnt.setStatus(_A)
_H3cDot11APIfStatisByAPIDTable_Object=MibTable
h3cDot11APIfStatisByAPIDTable=_H3cDot11APIfStatisByAPIDTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23))
if mibBuilder.loadTexts:h3cDot11APIfStatisByAPIDTable.setStatus(_A)
_H3cDot11APIfStatisByAPIDEntry_Object=MibTableRow
h3cDot11APIfStatisByAPIDEntry=_H3cDot11APIfStatisByAPIDEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1))
h3cDot11APIfStatisByAPIDEntry.setIndexNames((0,_C,_E),(0,_C,_V))
if mibBuilder.loadTexts:h3cDot11APIfStatisByAPIDEntry.setStatus(_A)
_H3cDot11APIfInPkts2_Type=Counter64
_H3cDot11APIfInPkts2_Object=MibTableColumn
h3cDot11APIfInPkts2=_H3cDot11APIfInPkts2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,1),_H3cDot11APIfInPkts2_Type())
h3cDot11APIfInPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInPkts2.setStatus(_A)
_H3cDot11APIfInNormalPkts2_Type=Counter64
_H3cDot11APIfInNormalPkts2_Object=MibTableColumn
h3cDot11APIfInNormalPkts2=_H3cDot11APIfInNormalPkts2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,2),_H3cDot11APIfInNormalPkts2_Type())
h3cDot11APIfInNormalPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInNormalPkts2.setStatus(_A)
_H3cDot11APIfInErrorPkts2_Type=Counter64
_H3cDot11APIfInErrorPkts2_Object=MibTableColumn
h3cDot11APIfInErrorPkts2=_H3cDot11APIfInErrorPkts2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,3),_H3cDot11APIfInErrorPkts2_Type())
h3cDot11APIfInErrorPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInErrorPkts2.setStatus(_A)
_H3cDot11APIfOutPkts2_Type=Counter64
_H3cDot11APIfOutPkts2_Object=MibTableColumn
h3cDot11APIfOutPkts2=_H3cDot11APIfOutPkts2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,4),_H3cDot11APIfOutPkts2_Type())
h3cDot11APIfOutPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutPkts2.setStatus(_A)
_H3cDot11APIfInOctets2_Type=Counter64
_H3cDot11APIfInOctets2_Object=MibTableColumn
h3cDot11APIfInOctets2=_H3cDot11APIfInOctets2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,5),_H3cDot11APIfInOctets2_Type())
h3cDot11APIfInOctets2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInOctets2.setStatus(_A)
_H3cDot11APIfOutOctets2_Type=Counter64
_H3cDot11APIfOutOctets2_Object=MibTableColumn
h3cDot11APIfOutOctets2=_H3cDot11APIfOutOctets2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,6),_H3cDot11APIfOutOctets2_Type())
h3cDot11APIfOutOctets2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutOctets2.setStatus(_A)
_H3cDot11APIfFlowOut2_Type=Unsigned32
_H3cDot11APIfFlowOut2_Object=MibTableColumn
h3cDot11APIfFlowOut2=_H3cDot11APIfFlowOut2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,7),_H3cDot11APIfFlowOut2_Type())
h3cDot11APIfFlowOut2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfFlowOut2.setStatus(_A)
_H3cDot11APIfFlowIN2_Type=Unsigned32
_H3cDot11APIfFlowIN2_Object=MibTableColumn
h3cDot11APIfFlowIN2=_H3cDot11APIfFlowIN2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,8),_H3cDot11APIfFlowIN2_Type())
h3cDot11APIfFlowIN2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfFlowIN2.setStatus(_A)
_H3cDot11APIfInUcastPkts2_Type=Counter64
_H3cDot11APIfInUcastPkts2_Object=MibTableColumn
h3cDot11APIfInUcastPkts2=_H3cDot11APIfInUcastPkts2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,9),_H3cDot11APIfInUcastPkts2_Type())
h3cDot11APIfInUcastPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInUcastPkts2.setStatus(_A)
_H3cDot11APIfInNUcastPkts2_Type=Counter64
_H3cDot11APIfInNUcastPkts2_Object=MibTableColumn
h3cDot11APIfInNUcastPkts2=_H3cDot11APIfInNUcastPkts2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,10),_H3cDot11APIfInNUcastPkts2_Type())
h3cDot11APIfInNUcastPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInNUcastPkts2.setStatus(_A)
_H3cDot11APIfInDiscardPkts2_Type=Counter64
_H3cDot11APIfInDiscardPkts2_Object=MibTableColumn
h3cDot11APIfInDiscardPkts2=_H3cDot11APIfInDiscardPkts2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,11),_H3cDot11APIfInDiscardPkts2_Type())
h3cDot11APIfInDiscardPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInDiscardPkts2.setStatus(_A)
_H3cDot11APIfOutUcastPkts2_Type=Counter64
_H3cDot11APIfOutUcastPkts2_Object=MibTableColumn
h3cDot11APIfOutUcastPkts2=_H3cDot11APIfOutUcastPkts2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,12),_H3cDot11APIfOutUcastPkts2_Type())
h3cDot11APIfOutUcastPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutUcastPkts2.setStatus(_A)
_H3cDot11APIfOutNUcastPkts2_Type=Counter64
_H3cDot11APIfOutNUcastPkts2_Object=MibTableColumn
h3cDot11APIfOutNUcastPkts2=_H3cDot11APIfOutNUcastPkts2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,13),_H3cDot11APIfOutNUcastPkts2_Type())
h3cDot11APIfOutNUcastPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutNUcastPkts2.setStatus(_A)
_H3cDot11APIfOutDiscardPkts2_Type=Counter64
_H3cDot11APIfOutDiscardPkts2_Object=MibTableColumn
h3cDot11APIfOutDiscardPkts2=_H3cDot11APIfOutDiscardPkts2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,14),_H3cDot11APIfOutDiscardPkts2_Type())
h3cDot11APIfOutDiscardPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutDiscardPkts2.setStatus(_A)
_H3cDot11APIfOutErrorPkts2_Type=Counter64
_H3cDot11APIfOutErrorPkts2_Object=MibTableColumn
h3cDot11APIfOutErrorPkts2=_H3cDot11APIfOutErrorPkts2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,15),_H3cDot11APIfOutErrorPkts2_Type())
h3cDot11APIfOutErrorPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutErrorPkts2.setStatus(_A)
_H3cDot11APIfUpdownTimes2_Type=Counter32
_H3cDot11APIfUpdownTimes2_Object=MibTableColumn
h3cDot11APIfUpdownTimes2=_H3cDot11APIfUpdownTimes2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,16),_H3cDot11APIfUpdownTimes2_Type())
h3cDot11APIfUpdownTimes2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfUpdownTimes2.setStatus(_A)
_H3cDot11APIfStatusKeepTime2_Type=TimeTicks
_H3cDot11APIfStatusKeepTime2_Object=MibTableColumn
h3cDot11APIfStatusKeepTime2=_H3cDot11APIfStatusKeepTime2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,17),_H3cDot11APIfStatusKeepTime2_Type())
h3cDot11APIfStatusKeepTime2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfStatusKeepTime2.setStatus(_A)
class _H3cDot11APIfOperStatus2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),(_f,4),('dormant',5),(_AG,6),(_AH,7)))
_H3cDot11APIfOperStatus2_Type.__name__=_D
_H3cDot11APIfOperStatus2_Object=MibTableColumn
h3cDot11APIfOperStatus2=_H3cDot11APIfOperStatus2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,18),_H3cDot11APIfOperStatus2_Type())
h3cDot11APIfOperStatus2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOperStatus2.setStatus(_A)
_H3cDot11APIfInBrdcastPkts2_Type=Counter64
_H3cDot11APIfInBrdcastPkts2_Object=MibTableColumn
h3cDot11APIfInBrdcastPkts2=_H3cDot11APIfInBrdcastPkts2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,19),_H3cDot11APIfInBrdcastPkts2_Type())
h3cDot11APIfInBrdcastPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInBrdcastPkts2.setStatus(_A)
_H3cDot11APIfOutBrdcastPkts2_Type=Counter64
_H3cDot11APIfOutBrdcastPkts2_Object=MibTableColumn
h3cDot11APIfOutBrdcastPkts2=_H3cDot11APIfOutBrdcastPkts2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,20),_H3cDot11APIfOutBrdcastPkts2_Type())
h3cDot11APIfOutBrdcastPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutBrdcastPkts2.setStatus(_A)
_H3cDot11APIfInMulcastPkts2_Type=Counter64
_H3cDot11APIfInMulcastPkts2_Object=MibTableColumn
h3cDot11APIfInMulcastPkts2=_H3cDot11APIfInMulcastPkts2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,21),_H3cDot11APIfInMulcastPkts2_Type())
h3cDot11APIfInMulcastPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInMulcastPkts2.setStatus(_A)
_H3cDot11APIfOutMulcastPkts2_Type=Counter64
_H3cDot11APIfOutMulcastPkts2_Object=MibTableColumn
h3cDot11APIfOutMulcastPkts2=_H3cDot11APIfOutMulcastPkts2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,22),_H3cDot11APIfOutMulcastPkts2_Type())
h3cDot11APIfOutMulcastPkts2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutMulcastPkts2.setStatus(_A)
_H3cDot11APIfInPayloadOctets2_Type=Counter64
_H3cDot11APIfInPayloadOctets2_Object=MibTableColumn
h3cDot11APIfInPayloadOctets2=_H3cDot11APIfInPayloadOctets2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,23),_H3cDot11APIfInPayloadOctets2_Type())
h3cDot11APIfInPayloadOctets2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInPayloadOctets2.setStatus(_A)
_H3cDot11APIfOutPayloadOctets2_Type=Counter64
_H3cDot11APIfOutPayloadOctets2_Object=MibTableColumn
h3cDot11APIfOutPayloadOctets2=_H3cDot11APIfOutPayloadOctets2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,24),_H3cDot11APIfOutPayloadOctets2_Type())
h3cDot11APIfOutPayloadOctets2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutPayloadOctets2.setStatus(_A)
_H3cDot11APIfInDataOctets2_Type=Counter64
_H3cDot11APIfInDataOctets2_Object=MibTableColumn
h3cDot11APIfInDataOctets2=_H3cDot11APIfInDataOctets2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,25),_H3cDot11APIfInDataOctets2_Type())
h3cDot11APIfInDataOctets2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfInDataOctets2.setStatus(_A)
_H3cDot11APIfOutDataOctets2_Type=Counter64
_H3cDot11APIfOutDataOctets2_Object=MibTableColumn
h3cDot11APIfOutDataOctets2=_H3cDot11APIfOutDataOctets2_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,23,1,26),_H3cDot11APIfOutDataOctets2_Type())
h3cDot11APIfOutDataOctets2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfOutDataOctets2.setStatus(_A)
_H3cDot11APUserSecAuthStatisTable_Object=MibTable
h3cDot11APUserSecAuthStatisTable=_H3cDot11APUserSecAuthStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,24))
if mibBuilder.loadTexts:h3cDot11APUserSecAuthStatisTable.setStatus(_A)
_H3cDot11APUserSecAuthStatisEntry_Object=MibTableRow
h3cDot11APUserSecAuthStatisEntry=_H3cDot11APUserSecAuthStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,24,1))
h3cDot11APUserSecAuthStatisEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:h3cDot11APUserSecAuthStatisEntry.setStatus(_A)
_H3cDot11APUserAuthCurNumber_Type=Integer32
_H3cDot11APUserAuthCurNumber_Object=MibTableColumn
h3cDot11APUserAuthCurNumber=_H3cDot11APUserAuthCurNumber_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,24,1,1),_H3cDot11APUserAuthCurNumber_Type())
h3cDot11APUserAuthCurNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APUserAuthCurNumber.setStatus(_A)
_H3cDot11APUserConnFailCnt_Type=Counter32
_H3cDot11APUserConnFailCnt_Object=MibTableColumn
h3cDot11APUserConnFailCnt=_H3cDot11APUserConnFailCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,24,1,2),_H3cDot11APUserConnFailCnt_Type())
h3cDot11APUserConnFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APUserConnFailCnt.setStatus(_A)
_H3cDot11APUserAuthReqCnt_Type=Counter32
_H3cDot11APUserAuthReqCnt_Object=MibTableColumn
h3cDot11APUserAuthReqCnt=_H3cDot11APUserAuthReqCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,24,1,3),_H3cDot11APUserAuthReqCnt_Type())
h3cDot11APUserAuthReqCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APUserAuthReqCnt.setStatus(_A)
_H3cDot11APUserAuthSuccCnt_Type=Counter32
_H3cDot11APUserAuthSuccCnt_Object=MibTableColumn
h3cDot11APUserAuthSuccCnt=_H3cDot11APUserAuthSuccCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,24,1,4),_H3cDot11APUserAuthSuccCnt_Type())
h3cDot11APUserAuthSuccCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APUserAuthSuccCnt.setStatus(_A)
_H3cDot11APUserAuthFailCnt_Type=Counter32
_H3cDot11APUserAuthFailCnt_Object=MibTableColumn
h3cDot11APUserAuthFailCnt=_H3cDot11APUserAuthFailCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,24,1,5),_H3cDot11APUserAuthFailCnt_Type())
h3cDot11APUserAuthFailCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APUserAuthFailCnt.setStatus(_A)
_H3cDot11AllUserOnlineTime_Type=TimeTicks
_H3cDot11AllUserOnlineTime_Object=MibTableColumn
h3cDot11AllUserOnlineTime=_H3cDot11AllUserOnlineTime_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,24,1,6),_H3cDot11AllUserOnlineTime_Type())
h3cDot11AllUserOnlineTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AllUserOnlineTime.setStatus(_A)
_H3cDot11APUserInfoStatisTable_Object=MibTable
h3cDot11APUserInfoStatisTable=_H3cDot11APUserInfoStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,25))
if mibBuilder.loadTexts:h3cDot11APUserInfoStatisTable.setStatus(_A)
_H3cDot11APUserInfoStatisEntry_Object=MibTableRow
h3cDot11APUserInfoStatisEntry=_H3cDot11APUserInfoStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,25,1))
h3cDot11APUserInfoStatisEntry.setIndexNames((0,_C,_E),(0,_C,_AM))
if mibBuilder.loadTexts:h3cDot11APUserInfoStatisEntry.setStatus(_A)
_H3cDot11APUserMacAddr_Type=MacAddress
_H3cDot11APUserMacAddr_Object=MibTableColumn
h3cDot11APUserMacAddr=_H3cDot11APUserMacAddr_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,25,1,1),_H3cDot11APUserMacAddr_Type())
h3cDot11APUserMacAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11APUserMacAddr.setStatus(_A)
_H3cDot11APUserIpAddr_Type=IpAddress
_H3cDot11APUserIpAddr_Object=MibTableColumn
h3cDot11APUserIpAddr=_H3cDot11APUserIpAddr_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,25,1,2),_H3cDot11APUserIpAddr_Type())
h3cDot11APUserIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APUserIpAddr.setStatus(_A)
_H3cDot11APUserLoginName_Type=OctetString
_H3cDot11APUserLoginName_Object=MibTableColumn
h3cDot11APUserLoginName=_H3cDot11APUserLoginName_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,25,1,3),_H3cDot11APUserLoginName_Type())
h3cDot11APUserLoginName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APUserLoginName.setStatus(_A)
_H3cDot11APUserLoginTime_Type=OctetString
_H3cDot11APUserLoginTime_Object=MibTableColumn
h3cDot11APUserLoginTime=_H3cDot11APUserLoginTime_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,25,1,4),_H3cDot11APUserLoginTime_Type())
h3cDot11APUserLoginTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APUserLoginTime.setStatus(_A)
_H3cDot11APUserOnlineTime_Type=TimeTicks
_H3cDot11APUserOnlineTime_Object=MibTableColumn
h3cDot11APUserOnlineTime=_H3cDot11APUserOnlineTime_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,25,1,5),_H3cDot11APUserOnlineTime_Type())
h3cDot11APUserOnlineTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APUserOnlineTime.setStatus(_A)
_H3cDot11APReassocStatis2Table_Object=MibTable
h3cDot11APReassocStatis2Table=_H3cDot11APReassocStatis2Table_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,26))
if mibBuilder.loadTexts:h3cDot11APReassocStatis2Table.setStatus(_A)
_H3cDot11APReassocStatis2Entry_Object=MibTableRow
h3cDot11APReassocStatis2Entry=_H3cDot11APReassocStatis2Entry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,26,1))
h3cDot11APReassocStatis2Entry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:h3cDot11APReassocStatis2Entry.setStatus(_A)
_H3cDot11APReassocFailStatis2Cnt_Type=Counter32
_H3cDot11APReassocFailStatis2Cnt_Object=MibTableColumn
h3cDot11APReassocFailStatis2Cnt=_H3cDot11APReassocFailStatis2Cnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,26,1,1),_H3cDot11APReassocFailStatis2Cnt_Type())
h3cDot11APReassocFailStatis2Cnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APReassocFailStatis2Cnt.setStatus(_A)
_H3cDot11TrafficTable_Object=MibTable
h3cDot11TrafficTable=_H3cDot11TrafficTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,27))
if mibBuilder.loadTexts:h3cDot11TrafficTable.setStatus(_A)
_H3cDot11TrafficEntry_Object=MibTableRow
h3cDot11TrafficEntry=_H3cDot11TrafficEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,27,1))
h3cDot11TrafficEntry.setIndexNames((0,_C,_AN))
if mibBuilder.loadTexts:h3cDot11TrafficEntry.setStatus(_A)
_H3cDot11SSIDIndex_Type=OctetString
_H3cDot11SSIDIndex_Object=MibTableColumn
h3cDot11SSIDIndex=_H3cDot11SSIDIndex_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,27,1,1),_H3cDot11SSIDIndex_Type())
h3cDot11SSIDIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDot11SSIDIndex.setStatus(_A)
_H3cDot11UpPacketNumber_Type=Counter64
_H3cDot11UpPacketNumber_Object=MibTableColumn
h3cDot11UpPacketNumber=_H3cDot11UpPacketNumber_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,27,1,2),_H3cDot11UpPacketNumber_Type())
h3cDot11UpPacketNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11UpPacketNumber.setStatus(_A)
_H3cDot11UpByteNumber_Type=Counter64
_H3cDot11UpByteNumber_Object=MibTableColumn
h3cDot11UpByteNumber=_H3cDot11UpByteNumber_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,27,1,3),_H3cDot11UpByteNumber_Type())
h3cDot11UpByteNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11UpByteNumber.setStatus(_A)
_H3cDot11DownPacketNumber_Type=Counter64
_H3cDot11DownPacketNumber_Object=MibTableColumn
h3cDot11DownPacketNumber=_H3cDot11DownPacketNumber_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,27,1,4),_H3cDot11DownPacketNumber_Type())
h3cDot11DownPacketNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DownPacketNumber.setStatus(_A)
_H3cDot11DownByteNumber_Type=Counter64
_H3cDot11DownByteNumber_Object=MibTableColumn
h3cDot11DownByteNumber=_H3cDot11DownByteNumber_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,27,1,5),_H3cDot11DownByteNumber_Type())
h3cDot11DownByteNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DownByteNumber.setStatus(_A)
_H3cDot11APEchoStatisTable_Object=MibTable
h3cDot11APEchoStatisTable=_H3cDot11APEchoStatisTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,28))
if mibBuilder.loadTexts:h3cDot11APEchoStatisTable.setStatus(_A)
_H3cDot11APEchoInfoStatisEntry_Object=MibTableRow
h3cDot11APEchoInfoStatisEntry=_H3cDot11APEchoInfoStatisEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,28,1))
h3cDot11APEchoInfoStatisEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:h3cDot11APEchoInfoStatisEntry.setStatus(_A)
_H3cDot11APEchoAvgDelay_Type=Integer32
_H3cDot11APEchoAvgDelay_Object=MibTableColumn
h3cDot11APEchoAvgDelay=_H3cDot11APEchoAvgDelay_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,28,1,1),_H3cDot11APEchoAvgDelay_Type())
h3cDot11APEchoAvgDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APEchoAvgDelay.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APEchoAvgDelay.setUnits('millisecond')
_H3cDot11APEchoRequestCnt_Type=Counter64
_H3cDot11APEchoRequestCnt_Object=MibTableColumn
h3cDot11APEchoRequestCnt=_H3cDot11APEchoRequestCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,28,1,2),_H3cDot11APEchoRequestCnt_Type())
h3cDot11APEchoRequestCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APEchoRequestCnt.setStatus(_A)
_H3cDot11APEchoRespLossCnt_Type=Counter64
_H3cDot11APEchoRespLossCnt_Object=MibTableColumn
h3cDot11APEchoRespLossCnt=_H3cDot11APEchoRespLossCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,2,28,1,3),_H3cDot11APEchoRespLossCnt_Type())
h3cDot11APEchoRespLossCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APEchoRespLossCnt.setStatus(_A)
_H3cDot11APMtNotifyGroup_ObjectIdentity=ObjectIdentity
h3cDot11APMtNotifyGroup=_H3cDot11APMtNotifyGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,2,3))
_H3cDot11APMtTraps_ObjectIdentity=ObjectIdentity
h3cDot11APMtTraps=_H3cDot11APMtTraps_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0))
_H3cDot11APMtTrapVarObjects_ObjectIdentity=ObjectIdentity
h3cDot11APMtTrapVarObjects=_H3cDot11APMtTrapVarObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1))
_H3cDot11APMtTrapCfgErrReason_Type=H3cDot11NotifyReasonType
_H3cDot11APMtTrapCfgErrReason_Object=MibScalar
h3cDot11APMtTrapCfgErrReason=_H3cDot11APMtTrapCfgErrReason_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,1),_H3cDot11APMtTrapCfgErrReason_Type())
h3cDot11APMtTrapCfgErrReason.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APMtTrapCfgErrReason.setStatus(_A)
class _H3cDot11APMtTrapRadioFailReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,8)));namedValues=NamedValues(*((_p,1),('hwerror',2),('swerror',3),('radar',4),(_f,8)))
_H3cDot11APMtTrapRadioFailReason_Type.__name__=_D
_H3cDot11APMtTrapRadioFailReason_Object=MibScalar
h3cDot11APMtTrapRadioFailReason=_H3cDot11APMtTrapRadioFailReason_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,2),_H3cDot11APMtTrapRadioFailReason_Type())
h3cDot11APMtTrapRadioFailReason.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APMtTrapRadioFailReason.setStatus(_A)
_H3cDot11APMtTrapOldChannel_Type=H3cDot11ChannelScopeType
_H3cDot11APMtTrapOldChannel_Object=MibScalar
h3cDot11APMtTrapOldChannel=_H3cDot11APMtTrapOldChannel_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,3),_H3cDot11APMtTrapOldChannel_Type())
h3cDot11APMtTrapOldChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APMtTrapOldChannel.setStatus(_A)
_H3cDot11APMtTrapNewChannel_Type=H3cDot11ChannelScopeType
_H3cDot11APMtTrapNewChannel_Object=MibScalar
h3cDot11APMtTrapNewChannel=_H3cDot11APMtTrapNewChannel_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,4),_H3cDot11APMtTrapNewChannel_Type())
h3cDot11APMtTrapNewChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APMtTrapNewChannel.setStatus(_A)
_H3cDot11APChannelChgMode_Type=H3cDot11RFModeType
_H3cDot11APChannelChgMode_Object=MibScalar
h3cDot11APChannelChgMode=_H3cDot11APChannelChgMode_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,5),_H3cDot11APChannelChgMode_Type())
h3cDot11APChannelChgMode.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APChannelChgMode.setStatus(_A)
class _H3cDot11APChgWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('monitor',2),('hybrid',3)))
_H3cDot11APChgWorkMode_Type.__name__=_D
_H3cDot11APChgWorkMode_Object=MibScalar
h3cDot11APChgWorkMode=_H3cDot11APChgWorkMode_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,6),_H3cDot11APChgWorkMode_Type())
h3cDot11APChgWorkMode.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APChgWorkMode.setStatus(_A)
_H3cDot11APIntfDevMACAddress_Type=MacAddress
_H3cDot11APIntfDevMACAddress_Object=MibScalar
h3cDot11APIntfDevMACAddress=_H3cDot11APIntfDevMACAddress_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,7),_H3cDot11APIntfDevMACAddress_Type())
h3cDot11APIntfDevMACAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APIntfDevMACAddress.setStatus(_A)
_H3cDot11APMtTrapOldIPAddr_Type=IpAddress
_H3cDot11APMtTrapOldIPAddr_Object=MibScalar
h3cDot11APMtTrapOldIPAddr=_H3cDot11APMtTrapOldIPAddr_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,8),_H3cDot11APMtTrapOldIPAddr_Type())
h3cDot11APMtTrapOldIPAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APMtTrapOldIPAddr.setStatus(_A)
_H3cDot11CurrInterfDetectedNum_Type=Integer32
_H3cDot11CurrInterfDetectedNum_Object=MibScalar
h3cDot11CurrInterfDetectedNum=_H3cDot11CurrInterfDetectedNum_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,9),_H3cDot11CurrInterfDetectedNum_Type())
h3cDot11CurrInterfDetectedNum.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11CurrInterfDetectedNum.setStatus(_A)
class _H3cDot11StaFullReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('ap',1),('bss',2),('radio',3),('radioConcur',4),('radiopolicy',5),('ac',6),('acConcur',7),('aid',8)))
_H3cDot11StaFullReason_Type.__name__=_D
_H3cDot11StaFullReason_Object=MibScalar
h3cDot11StaFullReason=_H3cDot11StaFullReason_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,10),_H3cDot11StaFullReason_Type())
h3cDot11StaFullReason.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11StaFullReason.setStatus(_A)
_H3cDot11StaLimitNumber_Type=Integer32
_H3cDot11StaLimitNumber_Object=MibScalar
h3cDot11StaLimitNumber=_H3cDot11StaLimitNumber_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,11),_H3cDot11StaLimitNumber_Type())
h3cDot11StaLimitNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11StaLimitNumber.setStatus(_A)
class _H3cDot11APRadioDownReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('phyicalUnusable',1),('configDisable',2),('operatinUnusable',3),('apTunnelDown',4)))
_H3cDot11APRadioDownReason_Type.__name__=_D
_H3cDot11APRadioDownReason_Object=MibScalar
h3cDot11APRadioDownReason=_H3cDot11APRadioDownReason_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,12),_H3cDot11APRadioDownReason_Type())
h3cDot11APRadioDownReason.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APRadioDownReason.setStatus(_A)
_H3cDot11InterfMacList_Type=OctetString
_H3cDot11InterfMacList_Object=MibScalar
h3cDot11InterfMacList=_H3cDot11InterfMacList_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,13),_H3cDot11InterfMacList_Type())
h3cDot11InterfMacList.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11InterfMacList.setStatus(_A)
_H3cDot11APTrapUserCnt_Type=Integer32
_H3cDot11APTrapUserCnt_Object=MibScalar
h3cDot11APTrapUserCnt=_H3cDot11APTrapUserCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,14),_H3cDot11APTrapUserCnt_Type())
h3cDot11APTrapUserCnt.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APTrapUserCnt.setStatus(_A)
_H3cDot11APTrapUserThreshold_Type=Integer32
_H3cDot11APTrapUserThreshold_Object=MibScalar
h3cDot11APTrapUserThreshold=_H3cDot11APTrapUserThreshold_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,15),_H3cDot11APTrapUserThreshold_Type())
h3cDot11APTrapUserThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APTrapUserThreshold.setStatus(_A)
_H3cDot11APMtChanlChgCount_Type=Integer32
_H3cDot11APMtChanlChgCount_Object=MibScalar
h3cDot11APMtChanlChgCount=_H3cDot11APMtChanlChgCount_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,16),_H3cDot11APMtChanlChgCount_Type())
h3cDot11APMtChanlChgCount.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APMtChanlChgCount.setStatus(_A)
_H3cDot11APMtFormerApVersion_Type=OctetString
_H3cDot11APMtFormerApVersion_Object=MibScalar
h3cDot11APMtFormerApVersion=_H3cDot11APMtFormerApVersion_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,17),_H3cDot11APMtFormerApVersion_Type())
h3cDot11APMtFormerApVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APMtFormerApVersion.setStatus(_A)
_H3cDot11APMtAPID_Type=H3cDot11ObjectIDType
_H3cDot11APMtAPID_Object=MibScalar
h3cDot11APMtAPID=_H3cDot11APMtAPID_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,18),_H3cDot11APMtAPID_Type())
h3cDot11APMtAPID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APMtAPID.setStatus(_A)
_H3cDot11APMtRadioID_Type=H3cDot11RadioScopeType
_H3cDot11APMtRadioID_Object=MibScalar
h3cDot11APMtRadioID=_H3cDot11APMtRadioID_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,19),_H3cDot11APMtRadioID_Type())
h3cDot11APMtRadioID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APMtRadioID.setStatus(_A)
_H3cDot11APMtChannel_Type=H3cDot11ChannelScopeType
_H3cDot11APMtChannel_Object=MibScalar
h3cDot11APMtChannel=_H3cDot11APMtChannel_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,20),_H3cDot11APMtChannel_Type())
h3cDot11APMtChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APMtChannel.setStatus(_A)
_H3cDot11APMtInterfMacAdd_Type=MacAddress
_H3cDot11APMtInterfMacAdd_Object=MibScalar
h3cDot11APMtInterfMacAdd=_H3cDot11APMtInterfMacAdd_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,21),_H3cDot11APMtInterfMacAdd_Type())
h3cDot11APMtInterfMacAdd.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APMtInterfMacAdd.setStatus(_A)
_H3cDot11APMtAdjChannel_Type=H3cDot11ChannelScopeType
_H3cDot11APMtAdjChannel_Object=MibScalar
h3cDot11APMtAdjChannel=_H3cDot11APMtAdjChannel_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,22),_H3cDot11APMtAdjChannel_Type())
h3cDot11APMtAdjChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APMtAdjChannel.setStatus(_A)
_H3cDot11APMtFirstTrapTime_Type=TimeTicks
_H3cDot11APMtFirstTrapTime_Object=MibScalar
h3cDot11APMtFirstTrapTime=_H3cDot11APMtFirstTrapTime_Object((1,3,6,1,4,1,43,45,1,10,2,75,2,3,1,23),_H3cDot11APMtFirstTrapTime_Type())
h3cDot11APMtFirstTrapTime.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APMtFirstTrapTime.setStatus(_A)
h3cDot11APMtWorkModeChgTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,1))
h3cDot11APMtWorkModeChgTrap.setObjects(*((_C,_J),(_C,_AO)))
if mibBuilder.loadTexts:h3cDot11APMtWorkModeChgTrap.setStatus(_A)
h3cDot11APMtCfgErrorTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,2))
h3cDot11APMtCfgErrorTrap.setObjects(*((_C,_J),(_C,_G),(_C,_AP)))
if mibBuilder.loadTexts:h3cDot11APMtCfgErrorTrap.setStatus(_A)
h3cDot11APMtRadioFailTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,3))
h3cDot11APMtRadioFailTrap.setObjects(*((_C,_J),(_C,_G),(_C,_AQ)))
if mibBuilder.loadTexts:h3cDot11APMtRadioFailTrap.setStatus(_A)
h3cDot11APMtRadioFailRecoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,4))
h3cDot11APMtRadioFailRecoverTrap.setObjects(*((_C,_J),(_C,_G)))
if mibBuilder.loadTexts:h3cDot11APMtRadioFailRecoverTrap.setStatus(_A)
h3cDot11APMtRdoChanlChgTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,5))
h3cDot11APMtRdoChanlChgTrap.setObjects(*((_C,_J),(_C,_G),(_C,_AR),(_C,_AS),(_C,_AT),(_C,_AU)))
if mibBuilder.loadTexts:h3cDot11APMtRdoChanlChgTrap.setStatus(_A)
h3cDot11APMtTimeSynFail=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,6))
h3cDot11APMtTimeSynFail.setObjects((_C,_J))
if mibBuilder.loadTexts:h3cDot11APMtTimeSynFail.setStatus(_A)
h3cDot11APMtChlIntfDetected=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,7))
h3cDot11APMtChlIntfDetected.setObjects((_C,_M))
if mibBuilder.loadTexts:h3cDot11APMtChlIntfDetected.setStatus(_A)
h3cDot11APMtIntfAPDetected=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,8))
h3cDot11APMtIntfAPDetected.setObjects(*((_C,_M),(_C,_g)))
if mibBuilder.loadTexts:h3cDot11APMtIntfAPDetected.setStatus(_A)
h3cDot11APMtIntfStaDetected=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,9))
h3cDot11APMtIntfStaDetected.setObjects(*((_C,_M),(_C,_g)))
if mibBuilder.loadTexts:h3cDot11APMtIntfStaDetected.setStatus(_A)
h3cDot11APMtIPChange=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,10))
h3cDot11APMtIPChange.setObjects(*((_C,_AV),(_C,_AW)))
if mibBuilder.loadTexts:h3cDot11APMtIPChange.setStatus(_A)
h3cDot11APFlashWriteFailure=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,11))
h3cDot11APFlashWriteFailure.setObjects(*((_C,_J),(_C,_AX)))
if mibBuilder.loadTexts:h3cDot11APFlashWriteFailure.setStatus(_A)
h3cDot11APSysReboot=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,12))
h3cDot11APSysReboot.setObjects((_C,_J))
if mibBuilder.loadTexts:h3cDot11APSysReboot.setStatus(_A)
h3cDot11APMtAvailChlTooLow=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,13))
h3cDot11APMtAvailChlTooLow.setObjects(*((_C,_G),(_C,_K)))
if mibBuilder.loadTexts:h3cDot11APMtAvailChlTooLow.setStatus(_A)
h3cDot11APImgDwldSuccess=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,14))
h3cDot11APImgDwldSuccess.setObjects(*((_C,_AY),(_C,_AZ),(_C,_Aa)))
if mibBuilder.loadTexts:h3cDot11APImgDwldSuccess.setStatus(_A)
h3cDot11APInterfDetectedTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,15))
h3cDot11APInterfDetectedTrap.setObjects(*((_C,_M),(_C,_h),(_C,_i)))
if mibBuilder.loadTexts:h3cDot11APInterfDetectedTrap.setStatus(_A)
h3cDot11APInterfClearTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,16))
h3cDot11APInterfClearTrap.setObjects(*((_C,_M),(_C,_K),(_C,_N),(_C,_P),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11APInterfClearTrap.setStatus(_A)
h3cDot11StaInterfDetectedTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,17))
h3cDot11StaInterfDetectedTrap.setObjects(*((_C,_M),(_C,_h),(_C,_i),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11StaInterfDetectedTrap.setStatus(_A)
h3cDot11StaInterfClearTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,18))
h3cDot11StaInterfClearTrap.setObjects(*((_C,_M),(_C,_K),(_C,_N),(_C,_P),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11StaInterfClearTrap.setStatus(_A)
h3cDot11OtherDevIntDetectedTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,19))
h3cDot11OtherDevIntDetectedTrap.setObjects(*((_C,_M),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11OtherDevIntDetectedTrap.setStatus(_A)
h3cDot11OtherDevIntClearTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,20))
h3cDot11OtherDevIntClearTrap.setObjects(*((_C,_M),(_C,_K),(_C,_N),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11OtherDevIntClearTrap.setStatus(_A)
h3cDot11APModuleTroubleTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,21))
h3cDot11APModuleTroubleTrap.setObjects(*((_C,_G),(_C,_K)))
if mibBuilder.loadTexts:h3cDot11APModuleTroubleTrap.setStatus(_A)
h3cDot11APModuleTroubleClearTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,22))
h3cDot11APModuleTroubleClearTrap.setObjects(*((_C,_G),(_C,_K)))
if mibBuilder.loadTexts:h3cDot11APModuleTroubleClearTrap.setStatus(_A)
h3cDot11APRadioDownTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,23))
h3cDot11APRadioDownTrap.setObjects(*((_C,_G),(_C,_Ab),(_C,_K),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11APRadioDownTrap.setStatus(_A)
h3cDot11APRadioDownRecovTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,24))
h3cDot11APRadioDownRecovTrap.setObjects(*((_C,_G),(_C,_K),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11APRadioDownRecovTrap.setStatus(_A)
h3cDot11APStaFullTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,25))
h3cDot11APStaFullTrap.setObjects(*((_C,_J),(_C,_j),(_C,_k),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11APStaFullTrap.setStatus(_A)
h3cDot11APStaFullRecoverTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,26))
h3cDot11APStaFullRecoverTrap.setObjects(*((_C,_J),(_C,_j),(_C,_k),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11APStaFullRecoverTrap.setStatus(_A)
h3cDot11DFSFreeCntBelowThrRecov=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,27))
h3cDot11DFSFreeCntBelowThrRecov.setObjects(*((_C,_G),(_C,_K)))
if mibBuilder.loadTexts:h3cDot11DFSFreeCntBelowThrRecov.setStatus(_A)
h3cDot11APCpuUsageHigh=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,28))
h3cDot11APCpuUsageHigh.setObjects(*((_C,_J),(_C,_l),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11APCpuUsageHigh.setStatus(_A)
h3cDot11APCpuUsageHighRecover=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,29))
h3cDot11APCpuUsageHighRecover.setObjects(*((_C,_J),(_C,_l),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11APCpuUsageHighRecover.setStatus(_A)
h3cDot11APMemUsageHigh=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,30))
h3cDot11APMemUsageHigh.setObjects(*((_C,_J),(_C,_m),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11APMemUsageHigh.setStatus(_A)
h3cDot11APMemUsageHighRecover=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,31))
h3cDot11APMemUsageHighRecover.setObjects(*((_C,_J),(_C,_m),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11APMemUsageHighRecover.setStatus(_A)
h3cDot11APTrapUserCntExceedThre=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,32))
h3cDot11APTrapUserCntExceedThre.setObjects(*((_C,_J),(_C,_Ac),(_C,_Ad)))
if mibBuilder.loadTexts:h3cDot11APTrapUserCntExceedThre.setStatus(_A)
h3cDot11APMtDetectedIntfAP=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,33))
h3cDot11APMtDetectedIntfAP.setObjects(*((_C,_K),(_C,_N),(_C,_R),(_C,_P),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11APMtDetectedIntfAP.setStatus(_A)
h3cDot11APMtDetectedIntfSTA=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,34))
h3cDot11APMtDetectedIntfSTA.setObjects(*((_C,_K),(_C,_N),(_C,_R),(_C,_P),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11APMtDetectedIntfSTA.setStatus(_A)
h3cDot11APMtDetectedIntfOtherDev=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,35))
h3cDot11APMtDetectedIntfOtherDev.setObjects(*((_C,_K),(_C,_N),(_C,_R)))
if mibBuilder.loadTexts:h3cDot11APMtDetectedIntfOtherDev.setStatus(_A)
h3cDot11DetcAdjChlIntfAP=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,36))
h3cDot11DetcAdjChlIntfAP.setObjects(*((_C,_K),(_C,_N),(_C,_R),(_C,_n),(_C,_P),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11DetcAdjChlIntfAP.setStatus(_A)
h3cDot11DetcAdjChlIntfAPClear=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,2,3,0,37))
h3cDot11DetcAdjChlIntfAPClear.setObjects(*((_C,_K),(_C,_N),(_C,_R),(_C,_n),(_C,_P),(_C,_I)))
if mibBuilder.loadTexts:h3cDot11DetcAdjChlIntfAPClear.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3cDot11APMT':h3cDot11APMT,'h3cDot11APObjectGroup':h3cDot11APObjectGroup,'h3cDot11APObjectStatusTable':h3cDot11APObjectStatusTable,'h3cDot11APObjectStatusEntry':h3cDot11APObjectStatusEntry,_J:h3cDot11APID,_AV:h3cDot11APIPAddress,'h3cDot11APMacAddress':h3cDot11APMacAddress,'h3cDot11APOperationStatus':h3cDot11APOperationStatus,'h3cDot11APTemplateNameOfAP':h3cDot11APTemplateNameOfAP,'h3cDot11APReset':h3cDot11APReset,'h3cDot11APCpuUsage':h3cDot11APCpuUsage,'h3cDot11APConnectionType':h3cDot11APConnectionType,'h3cDot11APLastImgDownloadTime':h3cDot11APLastImgDownloadTime,'h3cDot11APIPv6Address':h3cDot11APIPv6Address,'h3cDot11APLastRegisterTime':h3cDot11APLastRegisterTime,'h3cDot11APObjectTable':h3cDot11APObjectTable,'h3cDot11APObjectEntry':h3cDot11APObjectEntry,_U:h3cDot11APObjID,_AZ:h3cDot11CurrAPIPAddress,'h3cDot11CurrAPMacAddress':h3cDot11CurrAPMacAddress,'h3cDot11CurrACPortIndex':h3cDot11CurrACPortIndex,'h3cDot11CurrAPMACMode':h3cDot11CurrAPMACMode,'h3cDot11CurrAPTemplateName':h3cDot11CurrAPTemplateName,'h3cDot11CurrAPStationAssocCount':h3cDot11CurrAPStationAssocCount,_AY:h3cDot11CurrAPName,'h3cDot11CurrAPModelName':h3cDot11CurrAPModelName,'h3cDot11CurrAPImageName':h3cDot11CurrAPImageName,_Aa:h3cDot11CurrAPSoftwareVersion,'h3cDot11CurrAPIPNetMask':h3cDot11CurrAPIPNetMask,'h3cDot11CurrRadioModeSupport':h3cDot11CurrRadioModeSupport,'h3cDot11CurrIfNumber':h3cDot11CurrIfNumber,'h3cDot11CurrAPElementID':h3cDot11CurrAPElementID,'h3cDot11CurrAPMode':h3cDot11CurrAPMode,'h3cDot11CurrAPIPv6Address':h3cDot11CurrAPIPv6Address,'h3cDot11CurrAPSSIDNumber':h3cDot11CurrAPSSIDNumber,'h3cDot11CurrAPManufacturer':h3cDot11CurrAPManufacturer,'h3cDot11CurrAPMemorySize':h3cDot11CurrAPMemorySize,'h3cDot11CurrAPMemSizeInBytes':h3cDot11CurrAPMemSizeInBytes,'h3cDot11CurrAPFlashSize':h3cDot11CurrAPFlashSize,'h3cDot11CurrAPFlashSizeInBytes':h3cDot11CurrAPFlashSizeInBytes,'h3cDot11CurrAPReleasedVersion':h3cDot11CurrAPReleasedVersion,'h3cDot11CurrRadioModeSupport2':h3cDot11CurrRadioModeSupport2,'h3cDot11APRadioTable':h3cDot11APRadioTable,'h3cDot11APRadioEntry':h3cDot11APRadioEntry,_E:h3cDot11CurAPID,_G:h3cDot11RadioID,'h3cDot11AdminStatus':h3cDot11AdminStatus,'h3cDot11OperStatus':h3cDot11OperStatus,_M:h3cDot11Channel,'h3cDot11TxPowerLevel':h3cDot11TxPowerLevel,'h3cDot11APRadioIfIndex':h3cDot11APRadioIfIndex,'h3cDot11AntennaGain':h3cDot11AntennaGain,'h3cDot11MaxBandwidth':h3cDot11MaxBandwidth,'h3cDot11ResourceUseRatio':h3cDot11ResourceUseRatio,'h3cDot11RadioModeSupport':h3cDot11RadioModeSupport,'h3cDot11TxPowerLevel2':h3cDot11TxPowerLevel2,'h3cDot11PowerMgmtStatus':h3cDot11PowerMgmtStatus,'h3cDot11ChannelSwitchTimes':h3cDot11ChannelSwitchTimes,'h3cDot11AntennaType':h3cDot11AntennaType,'h3cDot11DiversitySelectionRx':h3cDot11DiversitySelectionRx,'h3cDot11MaxTxPwrLvl':h3cDot11MaxTxPwrLvl,'h3cDot11PwrAttRange':h3cDot11PwrAttRange,'h3cDot11AvgRxSignalStrength':h3cDot11AvgRxSignalStrength,'h3cDot11HighestRxSignalStrength':h3cDot11HighestRxSignalStrength,'h3cDot11LowestRxSignalStrength':h3cDot11LowestRxSignalStrength,'h3cDot11RadioIfUpdownTimes':h3cDot11RadioIfUpdownTimes,'h3cDot11RadioIfLastChange':h3cDot11RadioIfLastChange,'h3cDot11RadioModeSupport2':h3cDot11RadioModeSupport2,'h3cDot11APBSSTable':h3cDot11APBSSTable,'h3cDot11APBSSEntry':h3cDot11APBSSEntry,_T:h3cDot11WlanID,'h3cDot11BSSID':h3cDot11BSSID,'h3cDot11CurrSvcPolicyID':h3cDot11CurrSvcPolicyID,'h3cDot11SSID':h3cDot11SSID,'h3cDot11CurrSSIDResourceUseRatio':h3cDot11CurrSSIDResourceUseRatio,'h3cDot11APEssVlanId':h3cDot11APEssVlanId,'h3cDot11APModelTable':h3cDot11APModelTable,'h3cDot11APModelEntry':h3cDot11APModelEntry,_r:h3cDot11APModelAlias,'h3cDot11APModelName':h3cDot11APModelName,'h3cDot11RadioNumSupport':h3cDot11RadioNumSupport,'h3cDot11StationNumSupport':h3cDot11StationNumSupport,'h3cDot11MACModeSupport':h3cDot11MACModeSupport,'h3cDot11APManufacturer':h3cDot11APManufacturer,'h3cDot11APCPUType':h3cDot11APCPUType,'h3cDot11APCPUClockSpeed':h3cDot11APCPUClockSpeed,'h3cDot11APMemoryType':h3cDot11APMemoryType,'h3cDot11APFlashType':h3cDot11APFlashType,'h3cDot11APFlashSize':h3cDot11APFlashSize,'h3cDot11APMemSize':h3cDot11APMemSize,'h3cDot11APFlashSizeInBytes':h3cDot11APFlashSizeInBytes,'h3cDot11APMemorySize':h3cDot11APMemorySize,'h3cDot11APIfTable':h3cDot11APIfTable,'h3cDot11APIfEntry':h3cDot11APIfEntry,_V:h3cDot11APIfIndex,'h3cDot11APIfDescr':h3cDot11APIfDescr,'h3cDot11APIfType':h3cDot11APIfType,'h3cDot11APIfMtu':h3cDot11APIfMtu,'h3cDot11APIfPHYAddress':h3cDot11APIfPHYAddress,'h3cDot11APIfSpeed':h3cDot11APIfSpeed,'h3cDot11APIfInDataRate':h3cDot11APIfInDataRate,'h3cDot11APIfOutDataRate':h3cDot11APIfOutDataRate,'h3cDot11APIfSpeedKbps':h3cDot11APIfSpeedKbps,'h3cDot11APSSIDObjectTable':h3cDot11APSSIDObjectTable,'h3cDot11APSSIDObjectEntry':h3cDot11APSSIDObjectEntry,_s:h3cDot11APConfigSPID,'h3cDot11APConfigSSIDName':h3cDot11APConfigSSIDName,'h3cDot11APConfigBSSIDNum':h3cDot11APConfigBSSIDNum,'h3cDot11APConfigPortalStaNum':h3cDot11APConfigPortalStaNum,'h3cDot11APSysInfoTable':h3cDot11APSysInfoTable,'h3cDot11APSysInfoEntry':h3cDot11APSysInfoEntry,'h3cDot11APSysUpTime':h3cDot11APSysUpTime,_l:h3cDot11APCPURTUsage,'h3cDot11APCPUAvgUsage':h3cDot11APCPUAvgUsage,_m:h3cDot11APMemRTUsage,'h3cDot11APMemAvgUsage':h3cDot11APMemAvgUsage,'h3cDot11APIPAddressGateway':h3cDot11APIPAddressGateway,'h3cDot11APACAssociateStatus':h3cDot11APACAssociateStatus,'h3cDot11APManuBuildInfo':h3cDot11APManuBuildInfo,'h3cDot11APFlashFreeSize':h3cDot11APFlashFreeSize,'h3cDot11APTemperature':h3cDot11APTemperature,'h3cDot11APIdleListTable':h3cDot11APIdleListTable,'h3cDot11APIdleListEntry':h3cDot11APIdleListEntry,_w:h3cDot11APIdleTemplateName,'h3cDot11APIdleSerialID':h3cDot11APIdleSerialID,'h3cDot11APSysInfoByAPIDTable':h3cDot11APSysInfoByAPIDTable,'h3cDot11APSysInfoByAPIDEntry':h3cDot11APSysInfoByAPIDEntry,'h3cDot11APSysUpTime2':h3cDot11APSysUpTime2,'h3cDot11APCPURTUsage2':h3cDot11APCPURTUsage2,'h3cDot11APCPUAvgUsage2':h3cDot11APCPUAvgUsage2,'h3cDot11APMemRTUsage2':h3cDot11APMemRTUsage2,'h3cDot11APMemAvgUsage2':h3cDot11APMemAvgUsage2,'h3cDot11APIPAddressGateway2':h3cDot11APIPAddressGateway2,'h3cDot11APACAssociateStatus2':h3cDot11APACAssociateStatus2,'h3cDot11APManuBuildInfo2':h3cDot11APManuBuildInfo2,'h3cDot11APFlashFreeSize2':h3cDot11APFlashFreeSize2,'h3cDot11APTemperature2':h3cDot11APTemperature2,'h3cDot11APMacAddress2':h3cDot11APMacAddress2,'h3cDot11APStatisGroup':h3cDot11APStatisGroup,'h3cDot11APRxStatisTable':h3cDot11APRxStatisTable,'h3cDot11APRxStatisEntry':h3cDot11APRxStatisEntry,'h3cDot11RxFrameDupCnt':h3cDot11RxFrameDupCnt,'h3cDot11RxFrameCnt':h3cDot11RxFrameCnt,'h3cDot11RxUcastFrameCnt':h3cDot11RxUcastFrameCnt,'h3cDot11RxBcastFrameCnt':h3cDot11RxBcastFrameCnt,'h3cDot11RxMcastFrameCnt':h3cDot11RxMcastFrameCnt,'h3cDot11RxDiscardFrameCnt':h3cDot11RxDiscardFrameCnt,'h3cDot11RxFragCnt':h3cDot11RxFragCnt,'h3cDot11RxFcsErrCnt':h3cDot11RxFcsErrCnt,'h3cDot11RxFrameBytes':h3cDot11RxFrameBytes,'h3cDot11RxUcastFrameBytes':h3cDot11RxUcastFrameBytes,'h3cDot11RxBcastFrameBytes':h3cDot11RxBcastFrameBytes,'h3cDot11RxMcastFrameBytes':h3cDot11RxMcastFrameBytes,'h3cDot11RxDiscardFrameBytes':h3cDot11RxDiscardFrameBytes,'h3cDot11RxMgmtFrameCnt':h3cDot11RxMgmtFrameCnt,'h3cDot11RxCtrlFrameCnt':h3cDot11RxCtrlFrameCnt,'h3cDot11RxDataFrameCnt':h3cDot11RxDataFrameCnt,'h3cDot11RxDecryptErrorCnt':h3cDot11RxDecryptErrorCnt,'h3cDot11RxAuthenFrameCnt':h3cDot11RxAuthenFrameCnt,'h3cDot11RxAssociateFrameCnt':h3cDot11RxAssociateFrameCnt,'h3cDot11RxFrameErrorRatio':h3cDot11RxFrameErrorRatio,'h3cDot11RxPhyErrorCnt':h3cDot11RxPhyErrorCnt,'h3cDot11RxMICErrorCnt':h3cDot11RxMICErrorCnt,'h3cDot11RxDataFrameBytes':h3cDot11RxDataFrameBytes,'h3cDot11RadioRxAverSnr':h3cDot11RadioRxAverSnr,'h3cDot11RxPayloadBytes':h3cDot11RxPayloadBytes,'h3cDot11RxTrafficSpeed':h3cDot11RxTrafficSpeed,'h3cDot11RxUcastDataFrameCnt':h3cDot11RxUcastDataFrameCnt,'h3cDot11RxNUcastDataFrameCnt':h3cDot11RxNUcastDataFrameCnt,'h3cDot11RxTotalDiscardFrameCnt':h3cDot11RxTotalDiscardFrameCnt,'h3cDot11RxTotalIPCheckErrPacketCnt':h3cDot11RxTotalIPCheckErrPacketCnt,'h3cDot11APTxStatisTable':h3cDot11APTxStatisTable,'h3cDot11APTxStatisEntry':h3cDot11APTxStatisEntry,'h3cDot11TxFragCnt':h3cDot11TxFragCnt,'h3cDot11FailedCnt':h3cDot11FailedCnt,'h3cDot11RetryCnt':h3cDot11RetryCnt,'h3cDot11MultiRetryCnt':h3cDot11MultiRetryCnt,'h3cDot11RtsSuccessCnt':h3cDot11RtsSuccessCnt,'h3cDot11RtsFailCnt':h3cDot11RtsFailCnt,'h3cDot11AckFailCnt':h3cDot11AckFailCnt,'h3cDot11TxFrameCnt':h3cDot11TxFrameCnt,'h3cDot11TxUcastFrameCnt':h3cDot11TxUcastFrameCnt,'h3cDot11TxBcastFrameCnt':h3cDot11TxBcastFrameCnt,'h3cDot11TxMcastFrameCnt':h3cDot11TxMcastFrameCnt,'h3cDot11TxDiscardFrameCnt':h3cDot11TxDiscardFrameCnt,'h3cDot11TxFrameBytes':h3cDot11TxFrameBytes,'h3cDot11TxUcastFrameBytes':h3cDot11TxUcastFrameBytes,'h3cDot11TxBcastFrameBytes':h3cDot11TxBcastFrameBytes,'h3cDot11TxMcastFrameBytes':h3cDot11TxMcastFrameBytes,'h3cDot11TxDiscardFrameBytes':h3cDot11TxDiscardFrameBytes,'h3cDot11TxAuthenFrameCnt':h3cDot11TxAuthenFrameCnt,'h3cDot11TxAssociateFrameCnt':h3cDot11TxAssociateFrameCnt,'h3cDot11TxFrameRetryRatio':h3cDot11TxFrameRetryRatio,'h3cDot11TxDataFrameCnt':h3cDot11TxDataFrameCnt,'h3cDot11TxDataFrameBytes':h3cDot11TxDataFrameBytes,'h3cDot11TxMSDUCnt':h3cDot11TxMSDUCnt,'h3cDot11TxDiscardMSDUCnt':h3cDot11TxDiscardMSDUCnt,'h3cDot11RetryMSDUCnt':h3cDot11RetryMSDUCnt,'h3cDot11TxPayloadBytes':h3cDot11TxPayloadBytes,'h3cDot11TxTrafficSpeed':h3cDot11TxTrafficSpeed,'h3cDot11TxErrFrameRatio':h3cDot11TxErrFrameRatio,'h3cDot11TxFrameRate':h3cDot11TxFrameRate,'h3cDot11TxMgtFrameCnt':h3cDot11TxMgtFrameCnt,'h3cDot11TxCtrlFrameCnt':h3cDot11TxCtrlFrameCnt,'h3cDot11TxMACErrCnt':h3cDot11TxMACErrCnt,'h3cDot11TxErrFrameCnt':h3cDot11TxErrFrameCnt,'h3cDot11TxUcastDataFrameCnt':h3cDot11TxUcastDataFrameCnt,'h3cDot11TxNUcastDataFrameCnt':h3cDot11TxNUcastDataFrameCnt,'h3cDot11APAssocStatisTable':h3cDot11APAssocStatisTable,'h3cDot11APAssocStatisEntry':h3cDot11APAssocStatisEntry,'h3cDot11ApStationAssocSum':h3cDot11ApStationAssocSum,'h3cDot11ApStationAssocFailSum':h3cDot11ApStationAssocFailSum,'h3cDot11ApStationReassocSum':h3cDot11ApStationReassocSum,'h3cDot11ApStationAssocRejectSum':h3cDot11ApStationAssocRejectSum,'h3cDot11ApStationExDeAuthenSum':h3cDot11ApStationExDeAuthenSum,'h3cDot11ApStationCurAssocSum':h3cDot11ApStationCurAssocSum,'h3cDot11ApStaCurAuthSuccSum':h3cDot11ApStaCurAuthSuccSum,'h3cDot11AllStationUpSumTime':h3cDot11AllStationUpSumTime,'h3cDot11ApStationAssocReqSum':h3cDot11ApStationAssocReqSum,'h3cDot11AllStationUpSumTimeTicks':h3cDot11AllStationUpSumTimeTicks,'h3cDot11BSSRxStatisTable':h3cDot11BSSRxStatisTable,'h3cDot11BSSRxStatisEntry':h3cDot11BSSRxStatisEntry,'h3cDot11BSSRxFrameCnt':h3cDot11BSSRxFrameCnt,'h3cDot11BSSRxFrameBytes':h3cDot11BSSRxFrameBytes,'h3cDot11BSSRxDataFrameCnt':h3cDot11BSSRxDataFrameCnt,'h3cDot11BSSRxDataFrameBytes':h3cDot11BSSRxDataFrameBytes,'h3cDot11BSSRxAssociateFrameCnt':h3cDot11BSSRxAssociateFrameCnt,'h3cDot11BSSRxFrameErrorRatio':h3cDot11BSSRxFrameErrorRatio,'h3cDot11BSSRxPayloadBytes':h3cDot11BSSRxPayloadBytes,'h3cDot11BSSRxUniFrameCnt':h3cDot11BSSRxUniFrameCnt,'h3cDot11BSSRxNonUniFrameCnt':h3cDot11BSSRxNonUniFrameCnt,'h3cDot11BSSRxAuthenFrameCnt':h3cDot11BSSRxAuthenFrameCnt,'h3cDot11BSSTxStatisTable':h3cDot11BSSTxStatisTable,'h3cDot11BSSTxStatisEntry':h3cDot11BSSTxStatisEntry,'h3cDot11BSSTxFrameCnt':h3cDot11BSSTxFrameCnt,'h3cDot11BSSTxFrameBytes':h3cDot11BSSTxFrameBytes,'h3cDot11BSSTxDataFrameCnt':h3cDot11BSSTxDataFrameCnt,'h3cDot11BSSTxDataFrameBytes':h3cDot11BSSTxDataFrameBytes,'h3cDot11BSSTxAssociateFrameCnt':h3cDot11BSSTxAssociateFrameCnt,'h3cDot11BSSTxPayloadBytes':h3cDot11BSSTxPayloadBytes,'h3cDot11BSSTxRetryCnt':h3cDot11BSSTxRetryCnt,'h3cDot11BSSTxUniFrameCnt':h3cDot11BSSTxUniFrameCnt,'h3cDot11BSSTxNonUniFrameCnt':h3cDot11BSSTxNonUniFrameCnt,'h3cDot11BSSTxAuthenFrameCnt':h3cDot11BSSTxAuthenFrameCnt,'h3cDot11BSSAssocStatisTable':h3cDot11BSSAssocStatisTable,'h3cDot11BSSAssocStatisEntry':h3cDot11BSSAssocStatisEntry,'h3cDot11BSSStationAssocSum':h3cDot11BSSStationAssocSum,'h3cDot11BSSStationAssocFailSum':h3cDot11BSSStationAssocFailSum,'h3cDot11BSSStationReassocSum':h3cDot11BSSStationReassocSum,'h3cDot11BSSStationAssocRejectSum':h3cDot11BSSStationAssocRejectSum,'h3cDot11BSSStationExDeAssocSum':h3cDot11BSSStationExDeAssocSum,'h3cDot11BSSStationCurAssocSum':h3cDot11BSSStationCurAssocSum,'h3cDot11BSSStationAssocReqSum':h3cDot11BSSStationAssocReqSum,'h3cDot11BSSStationCurAuthSum':h3cDot11BSSStationCurAuthSum,'h3cDot11APLinkStatisTable':h3cDot11APLinkStatisTable,'h3cDot11APLinkStatisEntry':h3cDot11APLinkStatisEntry,'h3cDot11UpLinkUpDownTimes':h3cDot11UpLinkUpDownTimes,'h3cDot11DownLinkUpDownTimes':h3cDot11DownLinkUpDownTimes,'h3cDot11RadioAssocStatisTable':h3cDot11RadioAssocStatisTable,'h3cDot11RadioAssocStatisEntry':h3cDot11RadioAssocStatisEntry,'h3cDot11RadioStaAssocSum':h3cDot11RadioStaAssocSum,'h3cDot11RadioStaAssocFailSum':h3cDot11RadioStaAssocFailSum,'h3cDot11RadioStaReassocSum':h3cDot11RadioStaReassocSum,'h3cDot11RadioStaAssocRejectSum':h3cDot11RadioStaAssocRejectSum,'h3cDot11RadioStaExDeAssocSum':h3cDot11RadioStaExDeAssocSum,'h3cDot11RadioStaCurAssocSum':h3cDot11RadioStaCurAssocSum,'h3cDot11RadioMngFrameStatisTable':h3cDot11RadioMngFrameStatisTable,'h3cDot11RadioMngFrameStatisEntry':h3cDot11RadioMngFrameStatisEntry,_y:h3cDot11RadioStatisIndex,_z:h3cDot11MngFrameType,'h3cDot11MngFrameCnt':h3cDot11MngFrameCnt,'h3cDot11APAuthFailStatisTable':h3cDot11APAuthFailStatisTable,'h3cDot11APAuthFailStatisEntry':h3cDot11APAuthFailStatisEntry,_A7:h3cDot11APAuthFailStatisType,'h3cDot11APAuthFailStatisCnt':h3cDot11APAuthFailStatisCnt,'h3cDot11APAssocFailStatisTable':h3cDot11APAssocFailStatisTable,'h3cDot11APAssocFailStatisEntry':h3cDot11APAssocFailStatisEntry,_A8:h3cDot11APAssocFailStatisType,'h3cDot11APAssocFailStatisCnt':h3cDot11APAssocFailStatisCnt,'h3cDot11APReassocStatisTable':h3cDot11APReassocStatisTable,'h3cDot11APReassocStatisEntry':h3cDot11APReassocStatisEntry,_A9:h3cDot11APReassocStatisType,'h3cDot11APReassocStatisCnt':h3cDot11APReassocStatisCnt,'h3cDot11APUserAuthStatisTable':h3cDot11APUserAuthStatisTable,'h3cDot11APUserAuthStatisEntry':h3cDot11APUserAuthStatisEntry,_AA:h3cDot11UserAuthStatisType,'h3cDot11UserAuthStatisCnt':h3cDot11UserAuthStatisCnt,'h3cDot11APDeauthStatisTable':h3cDot11APDeauthStatisTable,'h3cDot11APDeauthStatisEntry':h3cDot11APDeauthStatisEntry,_AB:h3cDot11APDeauthStatisType,'h3cDot11APDeauthStatisCnt':h3cDot11APDeauthStatisCnt,'h3cDot11APDeassocStatisTable':h3cDot11APDeassocStatisTable,'h3cDot11APDeassocStatisEntry':h3cDot11APDeassocStatisEntry,_AE:h3cDot11APDeassocStatisType,'h3cDot11APDeassocStatisCnt':h3cDot11APDeassocStatisCnt,'h3cDot11APAssocFailStatis2Table':h3cDot11APAssocFailStatis2Table,'h3cDot11APAssocFailStatis2Entry':h3cDot11APAssocFailStatis2Entry,_AF:h3cDot11APAssocFailStatis2Type,'h3cDot11APAssocFailStatis2Cnt':h3cDot11APAssocFailStatis2Cnt,'h3cDot11APIfStatisTable':h3cDot11APIfStatisTable,'h3cDot11APIfStatisEntry':h3cDot11APIfStatisEntry,'h3cDot11APIfInPkts':h3cDot11APIfInPkts,'h3cDot11APIfInNormalPkts':h3cDot11APIfInNormalPkts,'h3cDot11APIfInErrorPkts':h3cDot11APIfInErrorPkts,'h3cDot11APIfOutPkts':h3cDot11APIfOutPkts,'h3cDot11APIfInOctets':h3cDot11APIfInOctets,'h3cDot11APIfOutOctets':h3cDot11APIfOutOctets,'h3cDot11APIfFlowOut':h3cDot11APIfFlowOut,'h3cDot11APIfFlowIN':h3cDot11APIfFlowIN,'h3cDot11APIfInUcastPkts':h3cDot11APIfInUcastPkts,'h3cDot11APIfInNUcastPkts':h3cDot11APIfInNUcastPkts,'h3cDot11APIfInDiscardPkts':h3cDot11APIfInDiscardPkts,'h3cDot11APIfOutUcastPkts':h3cDot11APIfOutUcastPkts,'h3cDot11APIfOutNUcastPkts':h3cDot11APIfOutNUcastPkts,'h3cDot11APIfOutDiscardPkts':h3cDot11APIfOutDiscardPkts,'h3cDot11APIfOutErrorPkts':h3cDot11APIfOutErrorPkts,'h3cDot11APIfUpdownTimes':h3cDot11APIfUpdownTimes,'h3cDot11APIfStatusKeepTime':h3cDot11APIfStatusKeepTime,'h3cDot11APIfOperStatus':h3cDot11APIfOperStatus,'h3cDot11APIfInBrdcastPkts':h3cDot11APIfInBrdcastPkts,'h3cDot11APIfOutBrdcastPkts':h3cDot11APIfOutBrdcastPkts,'h3cDot11APIfInMulcastPkts':h3cDot11APIfInMulcastPkts,'h3cDot11APIfOutMulcastPkts':h3cDot11APIfOutMulcastPkts,'h3cDot11APIfInPayloadOctets':h3cDot11APIfInPayloadOctets,'h3cDot11APIfOutPayloadOctets':h3cDot11APIfOutPayloadOctets,'h3cDot11RadioMngFrmStatisTable':h3cDot11RadioMngFrmStatisTable,'h3cDot11RadioMngFrmStatisEntry':h3cDot11RadioMngFrmStatisEntry,_AI:h3cDot11MngFrmType,'h3cDot11MngFrmCnt':h3cDot11MngFrmCnt,'h3cDot11APPacketSizeStatisTable':h3cDot11APPacketSizeStatisTable,'h3cDot11APPacketSizeStatisEntry':h3cDot11APPacketSizeStatisEntry,_AJ:h3cDot11APPacketSize,'h3cDot11APRXPacketSizeCount':h3cDot11APRXPacketSizeCount,'h3cDot11APTXPacketSizeCount':h3cDot11APTXPacketSizeCount,'h3cDot11APPacketRateStatisTable':h3cDot11APPacketRateStatisTable,'h3cDot11APPacketRateStatisEntry':h3cDot11APPacketRateStatisEntry,_AK:h3cDot11APPacketRate,'h3cDot11APRXPacketRateCount':h3cDot11APRXPacketRateCount,'h3cDot11APTXPacketRateCount':h3cDot11APTXPacketRateCount,'h3cDot11APPacketMCSRateStatisTable':h3cDot11APPacketMCSRateStatisTable,'h3cDot11APPacketMCSRateStatisEntry':h3cDot11APPacketMCSRateStatisEntry,_AL:h3cDot11APPacketMCSRate,'h3cDot11APRXPacketMCSRateCount':h3cDot11APRXPacketMCSRateCount,'h3cDot11APTXPacketMCSRateCount':h3cDot11APTXPacketMCSRateCount,'h3cDot11APAssocFailStatis3Table':h3cDot11APAssocFailStatis3Table,'h3cDot11APAssocFailStatis3Entry':h3cDot11APAssocFailStatis3Entry,'h3cDot11APAssocFailStatis3SRCnt':h3cDot11APAssocFailStatis3SRCnt,'h3cDot11APAssocFailStatis3NSRCnt':h3cDot11APAssocFailStatis3NSRCnt,'h3cDot11APAssocFailStatis3URCCnt':h3cDot11APAssocFailStatis3URCCnt,'h3cDot11APAssocFailStatis3RFCnt':h3cDot11APAssocFailStatis3RFCnt,'h3cDot11APAssocFailStatis3OtherCnt':h3cDot11APAssocFailStatis3OtherCnt,'h3cDot11APIfStatisByAPIDTable':h3cDot11APIfStatisByAPIDTable,'h3cDot11APIfStatisByAPIDEntry':h3cDot11APIfStatisByAPIDEntry,'h3cDot11APIfInPkts2':h3cDot11APIfInPkts2,'h3cDot11APIfInNormalPkts2':h3cDot11APIfInNormalPkts2,'h3cDot11APIfInErrorPkts2':h3cDot11APIfInErrorPkts2,'h3cDot11APIfOutPkts2':h3cDot11APIfOutPkts2,'h3cDot11APIfInOctets2':h3cDot11APIfInOctets2,'h3cDot11APIfOutOctets2':h3cDot11APIfOutOctets2,'h3cDot11APIfFlowOut2':h3cDot11APIfFlowOut2,'h3cDot11APIfFlowIN2':h3cDot11APIfFlowIN2,'h3cDot11APIfInUcastPkts2':h3cDot11APIfInUcastPkts2,'h3cDot11APIfInNUcastPkts2':h3cDot11APIfInNUcastPkts2,'h3cDot11APIfInDiscardPkts2':h3cDot11APIfInDiscardPkts2,'h3cDot11APIfOutUcastPkts2':h3cDot11APIfOutUcastPkts2,'h3cDot11APIfOutNUcastPkts2':h3cDot11APIfOutNUcastPkts2,'h3cDot11APIfOutDiscardPkts2':h3cDot11APIfOutDiscardPkts2,'h3cDot11APIfOutErrorPkts2':h3cDot11APIfOutErrorPkts2,'h3cDot11APIfUpdownTimes2':h3cDot11APIfUpdownTimes2,'h3cDot11APIfStatusKeepTime2':h3cDot11APIfStatusKeepTime2,'h3cDot11APIfOperStatus2':h3cDot11APIfOperStatus2,'h3cDot11APIfInBrdcastPkts2':h3cDot11APIfInBrdcastPkts2,'h3cDot11APIfOutBrdcastPkts2':h3cDot11APIfOutBrdcastPkts2,'h3cDot11APIfInMulcastPkts2':h3cDot11APIfInMulcastPkts2,'h3cDot11APIfOutMulcastPkts2':h3cDot11APIfOutMulcastPkts2,'h3cDot11APIfInPayloadOctets2':h3cDot11APIfInPayloadOctets2,'h3cDot11APIfOutPayloadOctets2':h3cDot11APIfOutPayloadOctets2,'h3cDot11APIfInDataOctets2':h3cDot11APIfInDataOctets2,'h3cDot11APIfOutDataOctets2':h3cDot11APIfOutDataOctets2,'h3cDot11APUserSecAuthStatisTable':h3cDot11APUserSecAuthStatisTable,'h3cDot11APUserSecAuthStatisEntry':h3cDot11APUserSecAuthStatisEntry,'h3cDot11APUserAuthCurNumber':h3cDot11APUserAuthCurNumber,'h3cDot11APUserConnFailCnt':h3cDot11APUserConnFailCnt,'h3cDot11APUserAuthReqCnt':h3cDot11APUserAuthReqCnt,'h3cDot11APUserAuthSuccCnt':h3cDot11APUserAuthSuccCnt,'h3cDot11APUserAuthFailCnt':h3cDot11APUserAuthFailCnt,'h3cDot11AllUserOnlineTime':h3cDot11AllUserOnlineTime,'h3cDot11APUserInfoStatisTable':h3cDot11APUserInfoStatisTable,'h3cDot11APUserInfoStatisEntry':h3cDot11APUserInfoStatisEntry,_AM:h3cDot11APUserMacAddr,'h3cDot11APUserIpAddr':h3cDot11APUserIpAddr,'h3cDot11APUserLoginName':h3cDot11APUserLoginName,'h3cDot11APUserLoginTime':h3cDot11APUserLoginTime,'h3cDot11APUserOnlineTime':h3cDot11APUserOnlineTime,'h3cDot11APReassocStatis2Table':h3cDot11APReassocStatis2Table,'h3cDot11APReassocStatis2Entry':h3cDot11APReassocStatis2Entry,'h3cDot11APReassocFailStatis2Cnt':h3cDot11APReassocFailStatis2Cnt,'h3cDot11TrafficTable':h3cDot11TrafficTable,'h3cDot11TrafficEntry':h3cDot11TrafficEntry,_AN:h3cDot11SSIDIndex,'h3cDot11UpPacketNumber':h3cDot11UpPacketNumber,'h3cDot11UpByteNumber':h3cDot11UpByteNumber,'h3cDot11DownPacketNumber':h3cDot11DownPacketNumber,'h3cDot11DownByteNumber':h3cDot11DownByteNumber,'h3cDot11APEchoStatisTable':h3cDot11APEchoStatisTable,'h3cDot11APEchoInfoStatisEntry':h3cDot11APEchoInfoStatisEntry,'h3cDot11APEchoAvgDelay':h3cDot11APEchoAvgDelay,'h3cDot11APEchoRequestCnt':h3cDot11APEchoRequestCnt,'h3cDot11APEchoRespLossCnt':h3cDot11APEchoRespLossCnt,'h3cDot11APMtNotifyGroup':h3cDot11APMtNotifyGroup,'h3cDot11APMtTraps':h3cDot11APMtTraps,'h3cDot11APMtWorkModeChgTrap':h3cDot11APMtWorkModeChgTrap,'h3cDot11APMtCfgErrorTrap':h3cDot11APMtCfgErrorTrap,'h3cDot11APMtRadioFailTrap':h3cDot11APMtRadioFailTrap,'h3cDot11APMtRadioFailRecoverTrap':h3cDot11APMtRadioFailRecoverTrap,'h3cDot11APMtRdoChanlChgTrap':h3cDot11APMtRdoChanlChgTrap,'h3cDot11APMtTimeSynFail':h3cDot11APMtTimeSynFail,'h3cDot11APMtChlIntfDetected':h3cDot11APMtChlIntfDetected,'h3cDot11APMtIntfAPDetected':h3cDot11APMtIntfAPDetected,'h3cDot11APMtIntfStaDetected':h3cDot11APMtIntfStaDetected,'h3cDot11APMtIPChange':h3cDot11APMtIPChange,'h3cDot11APFlashWriteFailure':h3cDot11APFlashWriteFailure,'h3cDot11APSysReboot':h3cDot11APSysReboot,'h3cDot11APMtAvailChlTooLow':h3cDot11APMtAvailChlTooLow,'h3cDot11APImgDwldSuccess':h3cDot11APImgDwldSuccess,'h3cDot11APInterfDetectedTrap':h3cDot11APInterfDetectedTrap,'h3cDot11APInterfClearTrap':h3cDot11APInterfClearTrap,'h3cDot11StaInterfDetectedTrap':h3cDot11StaInterfDetectedTrap,'h3cDot11StaInterfClearTrap':h3cDot11StaInterfClearTrap,'h3cDot11OtherDevIntDetectedTrap':h3cDot11OtherDevIntDetectedTrap,'h3cDot11OtherDevIntClearTrap':h3cDot11OtherDevIntClearTrap,'h3cDot11APModuleTroubleTrap':h3cDot11APModuleTroubleTrap,'h3cDot11APModuleTroubleClearTrap':h3cDot11APModuleTroubleClearTrap,'h3cDot11APRadioDownTrap':h3cDot11APRadioDownTrap,'h3cDot11APRadioDownRecovTrap':h3cDot11APRadioDownRecovTrap,'h3cDot11APStaFullTrap':h3cDot11APStaFullTrap,'h3cDot11APStaFullRecoverTrap':h3cDot11APStaFullRecoverTrap,'h3cDot11DFSFreeCntBelowThrRecov':h3cDot11DFSFreeCntBelowThrRecov,'h3cDot11APCpuUsageHigh':h3cDot11APCpuUsageHigh,'h3cDot11APCpuUsageHighRecover':h3cDot11APCpuUsageHighRecover,'h3cDot11APMemUsageHigh':h3cDot11APMemUsageHigh,'h3cDot11APMemUsageHighRecover':h3cDot11APMemUsageHighRecover,'h3cDot11APTrapUserCntExceedThre':h3cDot11APTrapUserCntExceedThre,'h3cDot11APMtDetectedIntfAP':h3cDot11APMtDetectedIntfAP,'h3cDot11APMtDetectedIntfSTA':h3cDot11APMtDetectedIntfSTA,'h3cDot11APMtDetectedIntfOtherDev':h3cDot11APMtDetectedIntfOtherDev,'h3cDot11DetcAdjChlIntfAP':h3cDot11DetcAdjChlIntfAP,'h3cDot11DetcAdjChlIntfAPClear':h3cDot11DetcAdjChlIntfAPClear,'h3cDot11APMtTrapVarObjects':h3cDot11APMtTrapVarObjects,_AP:h3cDot11APMtTrapCfgErrReason,_AQ:h3cDot11APMtTrapRadioFailReason,_AS:h3cDot11APMtTrapOldChannel,_AT:h3cDot11APMtTrapNewChannel,_AR:h3cDot11APChannelChgMode,_AO:h3cDot11APChgWorkMode,_g:h3cDot11APIntfDevMACAddress,_AW:h3cDot11APMtTrapOldIPAddr,_h:h3cDot11CurrInterfDetectedNum,_k:h3cDot11StaFullReason,_j:h3cDot11StaLimitNumber,_Ab:h3cDot11APRadioDownReason,_i:h3cDot11InterfMacList,_Ac:h3cDot11APTrapUserCnt,_Ad:h3cDot11APTrapUserThreshold,_AU:h3cDot11APMtChanlChgCount,_AX:h3cDot11APMtFormerApVersion,_K:h3cDot11APMtAPID,_N:h3cDot11APMtRadioID,_R:h3cDot11APMtChannel,_P:h3cDot11APMtInterfMacAdd,_n:h3cDot11APMtAdjChannel,_I:h3cDot11APMtFirstTrapTime})