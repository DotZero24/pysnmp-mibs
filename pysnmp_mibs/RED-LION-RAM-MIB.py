_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Redlionram_ObjectIdentity=ObjectIdentity
redlionram=_Redlionram_ObjectIdentity((1,3,6,1,4,1,1890))
_System_ObjectIdentity=ObjectIdentity
system=_System_ObjectIdentity((1,3,6,1,4,1,1890,1))
_UnitInfo_ObjectIdentity=ObjectIdentity
unitInfo=_UnitInfo_ObjectIdentity((1,3,6,1,4,1,1890,1,1))
_UnitDescription_Type=DisplayString
_UnitDescription_Object=MibScalar
unitDescription=_UnitDescription_Object((1,3,6,1,4,1,1890,1,1,1),_UnitDescription_Type())
unitDescription.setMaxAccess(_A)
if mibBuilder.loadTexts:unitDescription.setStatus(_B)
_UnitSerialNumber_Type=DisplayString
_UnitSerialNumber_Object=MibScalar
unitSerialNumber=_UnitSerialNumber_Object((1,3,6,1,4,1,1890,1,1,2),_UnitSerialNumber_Type())
unitSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:unitSerialNumber.setStatus(_B)
_UnitFirmwareVersion_Type=DisplayString
_UnitFirmwareVersion_Object=MibScalar
unitFirmwareVersion=_UnitFirmwareVersion_Object((1,3,6,1,4,1,1890,1,1,3),_UnitFirmwareVersion_Type())
unitFirmwareVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:unitFirmwareVersion.setStatus(_B)
_UnitName_Type=DisplayString
_UnitName_Object=MibScalar
unitName=_UnitName_Object((1,3,6,1,4,1,1890,1,1,4),_UnitName_Type())
unitName.setMaxAccess(_A)
if mibBuilder.loadTexts:unitName.setStatus(_B)
_Cellular_ObjectIdentity=ObjectIdentity
cellular=_Cellular_ObjectIdentity((1,3,6,1,4,1,1890,1,2))
_Mdn_Type=DisplayString
_Mdn_Object=MibScalar
mdn=_Mdn_Object((1,3,6,1,4,1,1890,1,2,1),_Mdn_Type())
mdn.setMaxAccess(_A)
if mibBuilder.loadTexts:mdn.setStatus(_B)
_MinIMEI_Type=DisplayString
_MinIMEI_Object=MibScalar
minIMEI=_MinIMEI_Object((1,3,6,1,4,1,1890,1,2,2),_MinIMEI_Type())
minIMEI.setMaxAccess(_A)
if mibBuilder.loadTexts:minIMEI.setStatus(_B)
_Nai_Type=DisplayString
_Nai_Object=MibScalar
nai=_Nai_Object((1,3,6,1,4,1,1890,1,2,3),_Nai_Type())
nai.setMaxAccess(_A)
if mibBuilder.loadTexts:nai.setStatus(_B)
_SipUser_Type=Integer32
_SipUser_Object=MibScalar
sipUser=_SipUser_Object((1,3,6,1,4,1,1890,1,2,4),_SipUser_Type())
sipUser.setMaxAccess(_A)
if mibBuilder.loadTexts:sipUser.setStatus(_B)
_Sid_Type=Integer32
_Sid_Object=MibScalar
sid=_Sid_Object((1,3,6,1,4,1,1890,1,2,5),_Sid_Type())
sid.setMaxAccess(_A)
if mibBuilder.loadTexts:sid.setStatus(_B)
_Nid_Type=Integer32
_Nid_Object=MibScalar
nid=_Nid_Object((1,3,6,1,4,1,1890,1,2,6),_Nid_Type())
nid.setMaxAccess(_A)
if mibBuilder.loadTexts:nid.setStatus(_B)
_Prl_Type=Integer32
_Prl_Object=MibScalar
prl=_Prl_Object((1,3,6,1,4,1,1890,1,2,7),_Prl_Type())
prl.setMaxAccess(_A)
if mibBuilder.loadTexts:prl.setStatus(_B)
_Activated_Type=Integer32
_Activated_Object=MibScalar
activated=_Activated_Object((1,3,6,1,4,1,1890,1,2,8),_Activated_Type())
activated.setMaxAccess(_A)
if mibBuilder.loadTexts:activated.setStatus(_B)
_OmaSupported_Type=Integer32
_OmaSupported_Object=MibScalar
omaSupported=_OmaSupported_Object((1,3,6,1,4,1,1890,1,2,9),_OmaSupported_Type())
omaSupported.setMaxAccess(_A)
if mibBuilder.loadTexts:omaSupported.setStatus(_B)
_CurrentMipProfile_Type=Integer32
_CurrentMipProfile_Object=MibScalar
currentMipProfile=_CurrentMipProfile_Object((1,3,6,1,4,1,1890,1,2,10),_CurrentMipProfile_Type())
currentMipProfile.setMaxAccess(_A)
if mibBuilder.loadTexts:currentMipProfile.setStatus(_B)
_Esn_Type=DisplayString
_Esn_Object=MibScalar
esn=_Esn_Object((1,3,6,1,4,1,1890,1,2,11),_Esn_Type())
esn.setMaxAccess(_A)
if mibBuilder.loadTexts:esn.setStatus(_B)
_Pesn_Type=DisplayString
_Pesn_Object=MibScalar
pesn=_Pesn_Object((1,3,6,1,4,1,1890,1,2,12),_Pesn_Type())
pesn.setMaxAccess(_A)
if mibBuilder.loadTexts:pesn.setStatus(_B)
_Meid_Type=DisplayString
_Meid_Object=MibScalar
meid=_Meid_Object((1,3,6,1,4,1,1890,1,2,13),_Meid_Type())
meid.setMaxAccess(_A)
if mibBuilder.loadTexts:meid.setStatus(_B)
_Vendor_Type=DisplayString
_Vendor_Object=MibScalar
vendor=_Vendor_Object((1,3,6,1,4,1,1890,1,2,14),_Vendor_Type())
vendor.setMaxAccess(_A)
if mibBuilder.loadTexts:vendor.setStatus(_B)
_ModelName_Type=DisplayString
_ModelName_Object=MibScalar
modelName=_ModelName_Object((1,3,6,1,4,1,1890,1,2,15),_ModelName_Type())
modelName.setMaxAccess(_A)
if mibBuilder.loadTexts:modelName.setStatus(_B)
_FwVersion_Type=DisplayString
_FwVersion_Object=MibScalar
fwVersion=_FwVersion_Object((1,3,6,1,4,1,1890,1,2,16),_FwVersion_Type())
fwVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:fwVersion.setStatus(_B)
_HwVersion_Type=DisplayString
_HwVersion_Object=MibScalar
hwVersion=_HwVersion_Object((1,3,6,1,4,1,1890,1,2,17),_HwVersion_Type())
hwVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:hwVersion.setStatus(_B)
_Carrier_Type=DisplayString
_Carrier_Object=MibScalar
carrier=_Carrier_Object((1,3,6,1,4,1,1890,1,2,18),_Carrier_Type())
carrier.setMaxAccess(_A)
if mibBuilder.loadTexts:carrier.setStatus(_B)
_LowRssi_Type=Integer32
_LowRssi_Object=MibScalar
lowRssi=_LowRssi_Object((1,3,6,1,4,1,1890,1,2,19),_LowRssi_Type())
lowRssi.setMaxAccess(_A)
if mibBuilder.loadTexts:lowRssi.setStatus(_B)
_LowEcio_Type=Integer32
_LowEcio_Object=MibScalar
lowEcio=_LowEcio_Object((1,3,6,1,4,1,1890,1,2,20),_LowEcio_Type())
lowEcio.setMaxAccess(_A)
if mibBuilder.loadTexts:lowEcio.setStatus(_B)
_HighRssi_Type=Integer32
_HighRssi_Object=MibScalar
highRssi=_HighRssi_Object((1,3,6,1,4,1,1890,1,2,21),_HighRssi_Type())
highRssi.setMaxAccess(_A)
if mibBuilder.loadTexts:highRssi.setStatus(_B)
_HighEcio_Type=Integer32
_HighEcio_Object=MibScalar
highEcio=_HighEcio_Object((1,3,6,1,4,1,1890,1,2,22),_HighEcio_Type())
highEcio.setMaxAccess(_A)
if mibBuilder.loadTexts:highEcio.setStatus(_B)
_CurrentRssi_Type=Integer32
_CurrentRssi_Object=MibScalar
currentRssi=_CurrentRssi_Object((1,3,6,1,4,1,1890,1,2,23),_CurrentRssi_Type())
currentRssi.setMaxAccess(_A)
if mibBuilder.loadTexts:currentRssi.setStatus(_B)
_CurrentEcio_Type=Integer32
_CurrentEcio_Object=MibScalar
currentEcio=_CurrentEcio_Object((1,3,6,1,4,1,1890,1,2,24),_CurrentEcio_Type())
currentEcio.setMaxAccess(_A)
if mibBuilder.loadTexts:currentEcio.setStatus(_B)
_SvcType_Type=DisplayString
_SvcType_Object=MibScalar
svcType=_SvcType_Object((1,3,6,1,4,1,1890,1,2,25),_SvcType_Type())
svcType.setMaxAccess(_A)
if mibBuilder.loadTexts:svcType.setStatus(_B)
_CurrentChannel_Type=Integer32
_CurrentChannel_Object=MibScalar
currentChannel=_CurrentChannel_Object((1,3,6,1,4,1,1890,1,2,29),_CurrentChannel_Type())
currentChannel.setMaxAccess(_A)
if mibBuilder.loadTexts:currentChannel.setStatus(_B)
_CdmaType_Type=DisplayString
_CdmaType_Object=MibScalar
cdmaType=_CdmaType_Object((1,3,6,1,4,1,1890,1,2,30),_CdmaType_Type())
cdmaType.setMaxAccess(_A)
if mibBuilder.loadTexts:cdmaType.setStatus(_B)
_HdrType_Type=DisplayString
_HdrType_Object=MibScalar
hdrType=_HdrType_Object((1,3,6,1,4,1,1890,1,2,31),_HdrType_Type())
hdrType.setMaxAccess(_A)
if mibBuilder.loadTexts:hdrType.setStatus(_B)
_CdmaRoaming_Type=DisplayString
_CdmaRoaming_Object=MibScalar
cdmaRoaming=_CdmaRoaming_Object((1,3,6,1,4,1,1890,1,2,32),_CdmaRoaming_Type())
cdmaRoaming.setMaxAccess(_A)
if mibBuilder.loadTexts:cdmaRoaming.setStatus(_B)
_HdrRoaming_Type=DisplayString
_HdrRoaming_Object=MibScalar
hdrRoaming=_HdrRoaming_Object((1,3,6,1,4,1,1890,1,2,33),_HdrRoaming_Type())
hdrRoaming.setMaxAccess(_A)
if mibBuilder.loadTexts:hdrRoaming.setStatus(_B)
_Roaming_Type=Integer32
_Roaming_Object=MibScalar
roaming=_Roaming_Object((1,3,6,1,4,1,1890,1,2,34),_Roaming_Type())
roaming.setMaxAccess(_A)
if mibBuilder.loadTexts:roaming.setStatus(_B)
_CurrentState_Type=Integer32
_CurrentState_Object=MibScalar
currentState=_CurrentState_Object((1,3,6,1,4,1,1890,1,2,35),_CurrentState_Type())
currentState.setMaxAccess(_A)
if mibBuilder.loadTexts:currentState.setStatus(_B)
_SpeedPref_Type=DisplayString
_SpeedPref_Object=MibScalar
speedPref=_SpeedPref_Object((1,3,6,1,4,1,1890,1,2,36),_SpeedPref_Type())
speedPref.setMaxAccess(_A)
if mibBuilder.loadTexts:speedPref.setStatus(_B)
_RoamPref_Type=DisplayString
_RoamPref_Object=MibScalar
roamPref=_RoamPref_Object((1,3,6,1,4,1,1890,1,2,37),_RoamPref_Type())
roamPref.setMaxAccess(_A)
if mibBuilder.loadTexts:roamPref.setStatus(_B)
_DevName_Type=DisplayString
_DevName_Object=MibScalar
devName=_DevName_Object((1,3,6,1,4,1,1890,1,2,38),_DevName_Type())
devName.setMaxAccess(_A)
if mibBuilder.loadTexts:devName.setStatus(_B)
_IfName_Type=DisplayString
_IfName_Object=MibScalar
ifName=_IfName_Object((1,3,6,1,4,1,1890,1,2,39),_IfName_Type())
ifName.setMaxAccess(_A)
if mibBuilder.loadTexts:ifName.setStatus(_B)
_TxCount_Type=Integer32
_TxCount_Object=MibScalar
txCount=_TxCount_Object((1,3,6,1,4,1,1890,1,2,40),_TxCount_Type())
txCount.setMaxAccess(_A)
if mibBuilder.loadTexts:txCount.setStatus(_B)
_RxCount_Type=Integer32
_RxCount_Object=MibScalar
rxCount=_RxCount_Object((1,3,6,1,4,1,1890,1,2,41),_RxCount_Type())
rxCount.setMaxAccess(_A)
if mibBuilder.loadTexts:rxCount.setStatus(_B)
_GprsState_Type=DisplayString
_GprsState_Object=MibScalar
gprsState=_GprsState_Object((1,3,6,1,4,1,1890,1,2,42),_GprsState_Type())
gprsState.setMaxAccess(_A)
if mibBuilder.loadTexts:gprsState.setStatus(_B)
_RxLevel_Type=DisplayString
_RxLevel_Object=MibScalar
rxLevel=_RxLevel_Object((1,3,6,1,4,1,1890,1,2,43),_RxLevel_Type())
rxLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:rxLevel.setStatus(_B)
_ServingCell_Type=DisplayString
_ServingCell_Object=MibScalar
servingCell=_ServingCell_Object((1,3,6,1,4,1,1890,1,2,44),_ServingCell_Type())
servingCell.setMaxAccess(_A)
if mibBuilder.loadTexts:servingCell.setStatus(_B)
_RccState_Type=DisplayString
_RccState_Object=MibScalar
rccState=_RccState_Object((1,3,6,1,4,1,1890,1,2,45),_RccState_Type())
rccState.setMaxAccess(_A)
if mibBuilder.loadTexts:rccState.setStatus(_B)
_GsmChannel_Type=DisplayString
_GsmChannel_Object=MibScalar
gsmChannel=_GsmChannel_Object((1,3,6,1,4,1,1890,1,2,46),_GsmChannel_Type())
gsmChannel.setMaxAccess(_A)
if mibBuilder.loadTexts:gsmChannel.setStatus(_B)
_PsState_Type=DisplayString
_PsState_Object=MibScalar
psState=_PsState_Object((1,3,6,1,4,1,1890,1,2,47),_PsState_Type())
psState.setMaxAccess(_A)
if mibBuilder.loadTexts:psState.setStatus(_B)
_Mode_Type=DisplayString
_Mode_Object=MibScalar
mode=_Mode_Object((1,3,6,1,4,1,1890,1,2,48),_Mode_Type())
mode.setMaxAccess(_A)
if mibBuilder.loadTexts:mode.setStatus(_B)
_Temperature_Type=DisplayString
_Temperature_Object=MibScalar
temperature=_Temperature_Object((1,3,6,1,4,1,1890,1,2,49),_Temperature_Type())
temperature.setMaxAccess(_A)
if mibBuilder.loadTexts:temperature.setStatus(_B)
_SimContextApn0_Type=DisplayString
_SimContextApn0_Object=MibScalar
simContextApn0=_SimContextApn0_Object((1,3,6,1,4,1,1890,1,2,50),_SimContextApn0_Type())
simContextApn0.setMaxAccess(_A)
if mibBuilder.loadTexts:simContextApn0.setStatus(_B)
_SimContextApn1_Type=DisplayString
_SimContextApn1_Object=MibScalar
simContextApn1=_SimContextApn1_Object((1,3,6,1,4,1,1890,1,2,51),_SimContextApn1_Type())
simContextApn1.setMaxAccess(_A)
if mibBuilder.loadTexts:simContextApn1.setStatus(_B)
_SimStatus_Type=DisplayString
_SimStatus_Object=MibScalar
simStatus=_SimStatus_Object((1,3,6,1,4,1,1890,1,2,52),_SimStatus_Type())
simStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:simStatus.setStatus(_B)
_ServiceDomain_Type=DisplayString
_ServiceDomain_Object=MibScalar
serviceDomain=_ServiceDomain_Object((1,3,6,1,4,1,1890,1,2,53),_ServiceDomain_Type())
serviceDomain.setMaxAccess(_A)
if mibBuilder.loadTexts:serviceDomain.setStatus(_B)
_AvailServiceType_Type=DisplayString
_AvailServiceType_Object=MibScalar
availServiceType=_AvailServiceType_Object((1,3,6,1,4,1,1890,1,2,54),_AvailServiceType_Type())
availServiceType.setMaxAccess(_A)
if mibBuilder.loadTexts:availServiceType.setStatus(_B)
_WCdmaL1State_Type=DisplayString
_WCdmaL1State_Object=MibScalar
wCdmaL1State=_WCdmaL1State_Object((1,3,6,1,4,1,1890,1,2,55),_WCdmaL1State_Type())
wCdmaL1State.setMaxAccess(_A)
if mibBuilder.loadTexts:wCdmaL1State.setStatus(_B)
_MmcsState_Type=DisplayString
_MmcsState_Object=MibScalar
mmcsState=_MmcsState_Object((1,3,6,1,4,1,1890,1,2,56),_MmcsState_Type())
mmcsState.setMaxAccess(_A)
if mibBuilder.loadTexts:mmcsState.setStatus(_B)
_GmmPsState_Type=DisplayString
_GmmPsState_Object=MibScalar
gmmPsState=_GmmPsState_Object((1,3,6,1,4,1,1890,1,2,57),_GmmPsState_Type())
gmmPsState.setMaxAccess(_A)
if mibBuilder.loadTexts:gmmPsState.setStatus(_B)
_WCdmaChannel_Type=DisplayString
_WCdmaChannel_Object=MibScalar
wCdmaChannel=_WCdmaChannel_Object((1,3,6,1,4,1,1890,1,2,58),_WCdmaChannel_Type())
wCdmaChannel.setMaxAccess(_A)
if mibBuilder.loadTexts:wCdmaChannel.setStatus(_B)
_WCdmaBand_Type=DisplayString
_WCdmaBand_Object=MibScalar
wCdmaBand=_WCdmaBand_Object((1,3,6,1,4,1,1890,1,2,59),_WCdmaBand_Type())
wCdmaBand.setMaxAccess(_A)
if mibBuilder.loadTexts:wCdmaBand.setStatus(_B)
_SystemMode_Type=DisplayString
_SystemMode_Object=MibScalar
systemMode=_SystemMode_Object((1,3,6,1,4,1,1890,1,2,60),_SystemMode_Type())
systemMode.setMaxAccess(_A)
if mibBuilder.loadTexts:systemMode.setStatus(_B)
_PowerOnTime_Type=DisplayString
_PowerOnTime_Object=MibScalar
powerOnTime=_PowerOnTime_Object((1,3,6,1,4,1,1890,1,2,61),_PowerOnTime_Type())
powerOnTime.setMaxAccess(_A)
if mibBuilder.loadTexts:powerOnTime.setStatus(_B)
_LowSpeedCsq_Type=DisplayString
_LowSpeedCsq_Object=MibScalar
lowSpeedCsq=_LowSpeedCsq_Object((1,3,6,1,4,1,1890,1,2,62),_LowSpeedCsq_Type())
lowSpeedCsq.setMaxAccess(_A)
if mibBuilder.loadTexts:lowSpeedCsq.setStatus(_B)
_HighSpeedCsq_Type=DisplayString
_HighSpeedCsq_Object=MibScalar
highSpeedCsq=_HighSpeedCsq_Object((1,3,6,1,4,1,1890,1,2,63),_HighSpeedCsq_Type())
highSpeedCsq.setMaxAccess(_A)
if mibBuilder.loadTexts:highSpeedCsq.setStatus(_B)
_Band_Type=DisplayString
_Band_Object=MibScalar
band=_Band_Object((1,3,6,1,4,1,1890,1,2,64),_Band_Type())
band.setMaxAccess(_A)
if mibBuilder.loadTexts:band.setStatus(_B)
_Imei_Type=DisplayString
_Imei_Object=MibScalar
imei=_Imei_Object((1,3,6,1,4,1,1890,1,2,65),_Imei_Type())
imei.setMaxAccess(_A)
if mibBuilder.loadTexts:imei.setStatus(_B)
_SimId_Type=DisplayString
_SimId_Object=MibScalar
simId=_SimId_Object((1,3,6,1,4,1,1890,1,2,66),_SimId_Type())
simId.setMaxAccess(_A)
if mibBuilder.loadTexts:simId.setStatus(_B)
_CarrPLMN_Type=DisplayString
_CarrPLMN_Object=MibScalar
carrPLMN=_CarrPLMN_Object((1,3,6,1,4,1,1890,1,2,67),_CarrPLMN_Type())
carrPLMN.setMaxAccess(_A)
if mibBuilder.loadTexts:carrPLMN.setStatus(_B)
_RxLevelC0_Type=DisplayString
_RxLevelC0_Object=MibScalar
rxLevelC0=_RxLevelC0_Object((1,3,6,1,4,1,1890,1,2,68),_RxLevelC0_Type())
rxLevelC0.setMaxAccess(_A)
if mibBuilder.loadTexts:rxLevelC0.setStatus(_B)
_RxLevelC1_Type=DisplayString
_RxLevelC1_Object=MibScalar
rxLevelC1=_RxLevelC1_Object((1,3,6,1,4,1,1890,1,2,69),_RxLevelC1_Type())
rxLevelC1.setMaxAccess(_A)
if mibBuilder.loadTexts:rxLevelC1.setStatus(_B)
_LocAreaCode_Type=DisplayString
_LocAreaCode_Object=MibScalar
locAreaCode=_LocAreaCode_Object((1,3,6,1,4,1,1890,1,2,70),_LocAreaCode_Type())
locAreaCode.setMaxAccess(_A)
if mibBuilder.loadTexts:locAreaCode.setStatus(_B)
_LteBand_Type=DisplayString
_LteBand_Object=MibScalar
lteBand=_LteBand_Object((1,3,6,1,4,1,1890,1,2,71),_LteBand_Type())
lteBand.setMaxAccess(_A)
if mibBuilder.loadTexts:lteBand.setStatus(_B)
_LteRxChan_Type=DisplayString
_LteRxChan_Object=MibScalar
lteRxChan=_LteRxChan_Object((1,3,6,1,4,1,1890,1,2,72),_LteRxChan_Type())
lteRxChan.setMaxAccess(_A)
if mibBuilder.loadTexts:lteRxChan.setStatus(_B)
_LteTxChan_Type=DisplayString
_LteTxChan_Object=MibScalar
lteTxChan=_LteTxChan_Object((1,3,6,1,4,1,1890,1,2,73),_LteTxChan_Type())
lteTxChan.setMaxAccess(_A)
if mibBuilder.loadTexts:lteTxChan.setStatus(_B)
_LteBW_Type=DisplayString
_LteBW_Object=MibScalar
lteBW=_LteBW_Object((1,3,6,1,4,1,1890,1,2,74),_LteBW_Type())
lteBW.setMaxAccess(_A)
if mibBuilder.loadTexts:lteBW.setStatus(_B)
_LteRSRP_Type=DisplayString
_LteRSRP_Object=MibScalar
lteRSRP=_LteRSRP_Object((1,3,6,1,4,1,1890,1,2,75),_LteRSRP_Type())
lteRSRP.setMaxAccess(_A)
if mibBuilder.loadTexts:lteRSRP.setStatus(_B)
_LteRSRQ_Type=DisplayString
_LteRSRQ_Object=MibScalar
lteRSRQ=_LteRSRQ_Object((1,3,6,1,4,1,1890,1,2,76),_LteRSRQ_Type())
lteRSRQ.setMaxAccess(_A)
if mibBuilder.loadTexts:lteRSRQ.setStatus(_B)
_LteTracAreaCode_Type=DisplayString
_LteTracAreaCode_Object=MibScalar
lteTracAreaCode=_LteTracAreaCode_Object((1,3,6,1,4,1,1890,1,2,77),_LteTracAreaCode_Type())
lteTracAreaCode.setMaxAccess(_A)
if mibBuilder.loadTexts:lteTracAreaCode.setStatus(_B)
_Creg_Type=DisplayString
_Creg_Object=MibScalar
creg=_Creg_Object((1,3,6,1,4,1,1890,1,2,78),_Creg_Type())
creg.setMaxAccess(_A)
if mibBuilder.loadTexts:creg.setStatus(_B)
_CellularUpTime_Type=Integer32
_CellularUpTime_Object=MibScalar
cellularUpTime=_CellularUpTime_Object((1,3,6,1,4,1,1890,1,2,79),_CellularUpTime_Type())
cellularUpTime.setMaxAccess(_A)
if mibBuilder.loadTexts:cellularUpTime.setStatus(_B)
_LteRSRPint_Type=Integer32
_LteRSRPint_Object=MibScalar
lteRSRPint=_LteRSRPint_Object((1,3,6,1,4,1,1890,1,2,80),_LteRSRPint_Type())
lteRSRPint.setMaxAccess(_A)
if mibBuilder.loadTexts:lteRSRPint.setStatus(_B)
_LteRSRQint_Type=Integer32
_LteRSRQint_Object=MibScalar
lteRSRQint=_LteRSRQint_Object((1,3,6,1,4,1,1890,1,2,81),_LteRSRQint_Type())
lteRSRQint.setMaxAccess(_A)
if mibBuilder.loadTexts:lteRSRQint.setStatus(_B)
_LteSINRint_Type=Integer32
_LteSINRint_Object=MibScalar
lteSINRint=_LteSINRint_Object((1,3,6,1,4,1,1890,1,2,82),_LteSINRint_Type())
lteSINRint.setMaxAccess(_A)
if mibBuilder.loadTexts:lteSINRint.setStatus(_B)
_Trafficppp0_ObjectIdentity=ObjectIdentity
trafficppp0=_Trafficppp0_ObjectIdentity((1,3,6,1,4,1,1890,1,3))
_TodayRxPpp0_Type=DisplayString
_TodayRxPpp0_Object=MibScalar
todayRxPpp0=_TodayRxPpp0_Object((1,3,6,1,4,1,1890,1,3,1),_TodayRxPpp0_Type())
todayRxPpp0.setMaxAccess(_A)
if mibBuilder.loadTexts:todayRxPpp0.setStatus(_B)
_TodayTxPpp0_Type=DisplayString
_TodayTxPpp0_Object=MibScalar
todayTxPpp0=_TodayTxPpp0_Object((1,3,6,1,4,1,1890,1,3,2),_TodayTxPpp0_Type())
todayTxPpp0.setMaxAccess(_A)
if mibBuilder.loadTexts:todayTxPpp0.setStatus(_B)
_TodayTotalPpp0_Type=DisplayString
_TodayTotalPpp0_Object=MibScalar
todayTotalPpp0=_TodayTotalPpp0_Object((1,3,6,1,4,1,1890,1,3,3),_TodayTotalPpp0_Type())
todayTotalPpp0.setMaxAccess(_A)
if mibBuilder.loadTexts:todayTotalPpp0.setStatus(_B)
_YesterdayRxPpp0_Type=DisplayString
_YesterdayRxPpp0_Object=MibScalar
yesterdayRxPpp0=_YesterdayRxPpp0_Object((1,3,6,1,4,1,1890,1,3,4),_YesterdayRxPpp0_Type())
yesterdayRxPpp0.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayRxPpp0.setStatus(_B)
_YesterdayTxPpp0_Type=DisplayString
_YesterdayTxPpp0_Object=MibScalar
yesterdayTxPpp0=_YesterdayTxPpp0_Object((1,3,6,1,4,1,1890,1,3,5),_YesterdayTxPpp0_Type())
yesterdayTxPpp0.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayTxPpp0.setStatus(_B)
_YesterdayTotalPpp0_Type=DisplayString
_YesterdayTotalPpp0_Object=MibScalar
yesterdayTotalPpp0=_YesterdayTotalPpp0_Object((1,3,6,1,4,1,1890,1,3,6),_YesterdayTotalPpp0_Type())
yesterdayTotalPpp0.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayTotalPpp0.setStatus(_B)
_CurrMonthRxPpp0_Type=DisplayString
_CurrMonthRxPpp0_Object=MibScalar
currMonthRxPpp0=_CurrMonthRxPpp0_Object((1,3,6,1,4,1,1890,1,3,7),_CurrMonthRxPpp0_Type())
currMonthRxPpp0.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthRxPpp0.setStatus(_B)
_CurrMonthTxPpp0_Type=DisplayString
_CurrMonthTxPpp0_Object=MibScalar
currMonthTxPpp0=_CurrMonthTxPpp0_Object((1,3,6,1,4,1,1890,1,3,8),_CurrMonthTxPpp0_Type())
currMonthTxPpp0.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthTxPpp0.setStatus(_B)
_CurrMonthTotalPpp0_Type=DisplayString
_CurrMonthTotalPpp0_Object=MibScalar
currMonthTotalPpp0=_CurrMonthTotalPpp0_Object((1,3,6,1,4,1,1890,1,3,9),_CurrMonthTotalPpp0_Type())
currMonthTotalPpp0.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthTotalPpp0.setStatus(_B)
_PreMonthRxPpp0_Type=DisplayString
_PreMonthRxPpp0_Object=MibScalar
preMonthRxPpp0=_PreMonthRxPpp0_Object((1,3,6,1,4,1,1890,1,3,10),_PreMonthRxPpp0_Type())
preMonthRxPpp0.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthRxPpp0.setStatus(_B)
_PreMonthTxPpp0_Type=DisplayString
_PreMonthTxPpp0_Object=MibScalar
preMonthTxPpp0=_PreMonthTxPpp0_Object((1,3,6,1,4,1,1890,1,3,11),_PreMonthTxPpp0_Type())
preMonthTxPpp0.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthTxPpp0.setStatus(_B)
_PreMonthTotalPpp0_Type=DisplayString
_PreMonthTotalPpp0_Object=MibScalar
preMonthTotalPpp0=_PreMonthTotalPpp0_Object((1,3,6,1,4,1,1890,1,3,12),_PreMonthTotalPpp0_Type())
preMonthTotalPpp0.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthTotalPpp0.setStatus(_B)
_TodayRxPpp0Kib_Type=Integer32
_TodayRxPpp0Kib_Object=MibScalar
todayRxPpp0Kib=_TodayRxPpp0Kib_Object((1,3,6,1,4,1,1890,1,3,13),_TodayRxPpp0Kib_Type())
todayRxPpp0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:todayRxPpp0Kib.setStatus(_B)
_TodayTxPpp0Kib_Type=Integer32
_TodayTxPpp0Kib_Object=MibScalar
todayTxPpp0Kib=_TodayTxPpp0Kib_Object((1,3,6,1,4,1,1890,1,3,14),_TodayTxPpp0Kib_Type())
todayTxPpp0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:todayTxPpp0Kib.setStatus(_B)
_TodayTotalPpp0Kib_Type=Integer32
_TodayTotalPpp0Kib_Object=MibScalar
todayTotalPpp0Kib=_TodayTotalPpp0Kib_Object((1,3,6,1,4,1,1890,1,3,15),_TodayTotalPpp0Kib_Type())
todayTotalPpp0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:todayTotalPpp0Kib.setStatus(_B)
_YesterdayRxPpp0Kib_Type=Integer32
_YesterdayRxPpp0Kib_Object=MibScalar
yesterdayRxPpp0Kib=_YesterdayRxPpp0Kib_Object((1,3,6,1,4,1,1890,1,3,16),_YesterdayRxPpp0Kib_Type())
yesterdayRxPpp0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayRxPpp0Kib.setStatus(_B)
_YesterdayTxPpp0Kib_Type=Integer32
_YesterdayTxPpp0Kib_Object=MibScalar
yesterdayTxPpp0Kib=_YesterdayTxPpp0Kib_Object((1,3,6,1,4,1,1890,1,3,17),_YesterdayTxPpp0Kib_Type())
yesterdayTxPpp0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayTxPpp0Kib.setStatus(_B)
_YesterdayTotalPpp0Kib_Type=Integer32
_YesterdayTotalPpp0Kib_Object=MibScalar
yesterdayTotalPpp0Kib=_YesterdayTotalPpp0Kib_Object((1,3,6,1,4,1,1890,1,3,18),_YesterdayTotalPpp0Kib_Type())
yesterdayTotalPpp0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayTotalPpp0Kib.setStatus(_B)
_CurrMonthRxPpp0Kib_Type=Integer32
_CurrMonthRxPpp0Kib_Object=MibScalar
currMonthRxPpp0Kib=_CurrMonthRxPpp0Kib_Object((1,3,6,1,4,1,1890,1,3,19),_CurrMonthRxPpp0Kib_Type())
currMonthRxPpp0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthRxPpp0Kib.setStatus(_B)
_CurrMonthTxPpp0Kib_Type=Integer32
_CurrMonthTxPpp0Kib_Object=MibScalar
currMonthTxPpp0Kib=_CurrMonthTxPpp0Kib_Object((1,3,6,1,4,1,1890,1,3,20),_CurrMonthTxPpp0Kib_Type())
currMonthTxPpp0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthTxPpp0Kib.setStatus(_B)
_CurrMonthTotalPpp0Kib_Type=Integer32
_CurrMonthTotalPpp0Kib_Object=MibScalar
currMonthTotalPpp0Kib=_CurrMonthTotalPpp0Kib_Object((1,3,6,1,4,1,1890,1,3,21),_CurrMonthTotalPpp0Kib_Type())
currMonthTotalPpp0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthTotalPpp0Kib.setStatus(_B)
_PreMonthRxPpp0Kib_Type=Integer32
_PreMonthRxPpp0Kib_Object=MibScalar
preMonthRxPpp0Kib=_PreMonthRxPpp0Kib_Object((1,3,6,1,4,1,1890,1,3,22),_PreMonthRxPpp0Kib_Type())
preMonthRxPpp0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthRxPpp0Kib.setStatus(_B)
_PreMonthTxPpp0Kib_Type=Integer32
_PreMonthTxPpp0Kib_Object=MibScalar
preMonthTxPpp0Kib=_PreMonthTxPpp0Kib_Object((1,3,6,1,4,1,1890,1,3,23),_PreMonthTxPpp0Kib_Type())
preMonthTxPpp0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthTxPpp0Kib.setStatus(_B)
_PreMonthTotalPpp0Kib_Type=Integer32
_PreMonthTotalPpp0Kib_Object=MibScalar
preMonthTotalPpp0Kib=_PreMonthTotalPpp0Kib_Object((1,3,6,1,4,1,1890,1,3,24),_PreMonthTotalPpp0Kib_Type())
preMonthTotalPpp0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthTotalPpp0Kib.setStatus(_B)
_Trafficwwan0_ObjectIdentity=ObjectIdentity
trafficwwan0=_Trafficwwan0_ObjectIdentity((1,3,6,1,4,1,1890,1,4))
_TodayRxWwan0_Type=DisplayString
_TodayRxWwan0_Object=MibScalar
todayRxWwan0=_TodayRxWwan0_Object((1,3,6,1,4,1,1890,1,4,1),_TodayRxWwan0_Type())
todayRxWwan0.setMaxAccess(_A)
if mibBuilder.loadTexts:todayRxWwan0.setStatus(_B)
_TodayTxWwan0_Type=DisplayString
_TodayTxWwan0_Object=MibScalar
todayTxWwan0=_TodayTxWwan0_Object((1,3,6,1,4,1,1890,1,4,2),_TodayTxWwan0_Type())
todayTxWwan0.setMaxAccess(_A)
if mibBuilder.loadTexts:todayTxWwan0.setStatus(_B)
_TodayTotalWwan0_Type=DisplayString
_TodayTotalWwan0_Object=MibScalar
todayTotalWwan0=_TodayTotalWwan0_Object((1,3,6,1,4,1,1890,1,4,3),_TodayTotalWwan0_Type())
todayTotalWwan0.setMaxAccess(_A)
if mibBuilder.loadTexts:todayTotalWwan0.setStatus(_B)
_YesterdayRxWwan0_Type=DisplayString
_YesterdayRxWwan0_Object=MibScalar
yesterdayRxWwan0=_YesterdayRxWwan0_Object((1,3,6,1,4,1,1890,1,4,4),_YesterdayRxWwan0_Type())
yesterdayRxWwan0.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayRxWwan0.setStatus(_B)
_YesterdayTxWwan0_Type=DisplayString
_YesterdayTxWwan0_Object=MibScalar
yesterdayTxWwan0=_YesterdayTxWwan0_Object((1,3,6,1,4,1,1890,1,4,5),_YesterdayTxWwan0_Type())
yesterdayTxWwan0.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayTxWwan0.setStatus(_B)
_YesterdayTotalWwan0_Type=DisplayString
_YesterdayTotalWwan0_Object=MibScalar
yesterdayTotalWwan0=_YesterdayTotalWwan0_Object((1,3,6,1,4,1,1890,1,4,6),_YesterdayTotalWwan0_Type())
yesterdayTotalWwan0.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayTotalWwan0.setStatus(_B)
_CurrMonthRxWwan0_Type=DisplayString
_CurrMonthRxWwan0_Object=MibScalar
currMonthRxWwan0=_CurrMonthRxWwan0_Object((1,3,6,1,4,1,1890,1,4,7),_CurrMonthRxWwan0_Type())
currMonthRxWwan0.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthRxWwan0.setStatus(_B)
_CurrMonthTxWwan0_Type=DisplayString
_CurrMonthTxWwan0_Object=MibScalar
currMonthTxWwan0=_CurrMonthTxWwan0_Object((1,3,6,1,4,1,1890,1,4,8),_CurrMonthTxWwan0_Type())
currMonthTxWwan0.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthTxWwan0.setStatus(_B)
_CurrMonthTotalWwan0_Type=DisplayString
_CurrMonthTotalWwan0_Object=MibScalar
currMonthTotalWwan0=_CurrMonthTotalWwan0_Object((1,3,6,1,4,1,1890,1,4,9),_CurrMonthTotalWwan0_Type())
currMonthTotalWwan0.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthTotalWwan0.setStatus(_B)
_PreMonthRxWwan0_Type=DisplayString
_PreMonthRxWwan0_Object=MibScalar
preMonthRxWwan0=_PreMonthRxWwan0_Object((1,3,6,1,4,1,1890,1,4,10),_PreMonthRxWwan0_Type())
preMonthRxWwan0.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthRxWwan0.setStatus(_B)
_PreMonthTxWwan0_Type=DisplayString
_PreMonthTxWwan0_Object=MibScalar
preMonthTxWwan0=_PreMonthTxWwan0_Object((1,3,6,1,4,1,1890,1,4,11),_PreMonthTxWwan0_Type())
preMonthTxWwan0.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthTxWwan0.setStatus(_B)
_PreMonthTotalWwan0_Type=DisplayString
_PreMonthTotalWwan0_Object=MibScalar
preMonthTotalWwan0=_PreMonthTotalWwan0_Object((1,3,6,1,4,1,1890,1,4,12),_PreMonthTotalWwan0_Type())
preMonthTotalWwan0.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthTotalWwan0.setStatus(_B)
_TodayRxWwan0Kib_Type=Integer32
_TodayRxWwan0Kib_Object=MibScalar
todayRxWwan0Kib=_TodayRxWwan0Kib_Object((1,3,6,1,4,1,1890,1,4,13),_TodayRxWwan0Kib_Type())
todayRxWwan0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:todayRxWwan0Kib.setStatus(_B)
_TodayTxWwan0Kib_Type=Integer32
_TodayTxWwan0Kib_Object=MibScalar
todayTxWwan0Kib=_TodayTxWwan0Kib_Object((1,3,6,1,4,1,1890,1,4,14),_TodayTxWwan0Kib_Type())
todayTxWwan0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:todayTxWwan0Kib.setStatus(_B)
_TodayTotalWwan0Kib_Type=Integer32
_TodayTotalWwan0Kib_Object=MibScalar
todayTotalWwan0Kib=_TodayTotalWwan0Kib_Object((1,3,6,1,4,1,1890,1,4,15),_TodayTotalWwan0Kib_Type())
todayTotalWwan0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:todayTotalWwan0Kib.setStatus(_B)
_YesterdayRxWwan0Kib_Type=Integer32
_YesterdayRxWwan0Kib_Object=MibScalar
yesterdayRxWwan0Kib=_YesterdayRxWwan0Kib_Object((1,3,6,1,4,1,1890,1,4,16),_YesterdayRxWwan0Kib_Type())
yesterdayRxWwan0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayRxWwan0Kib.setStatus(_B)
_YesterdayTxWwan0Kib_Type=Integer32
_YesterdayTxWwan0Kib_Object=MibScalar
yesterdayTxWwan0Kib=_YesterdayTxWwan0Kib_Object((1,3,6,1,4,1,1890,1,4,17),_YesterdayTxWwan0Kib_Type())
yesterdayTxWwan0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayTxWwan0Kib.setStatus(_B)
_YesterdayTotalWwan0Kib_Type=Integer32
_YesterdayTotalWwan0Kib_Object=MibScalar
yesterdayTotalWwan0Kib=_YesterdayTotalWwan0Kib_Object((1,3,6,1,4,1,1890,1,4,18),_YesterdayTotalWwan0Kib_Type())
yesterdayTotalWwan0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayTotalWwan0Kib.setStatus(_B)
_CurrMonthRxWwan0Kib_Type=Integer32
_CurrMonthRxWwan0Kib_Object=MibScalar
currMonthRxWwan0Kib=_CurrMonthRxWwan0Kib_Object((1,3,6,1,4,1,1890,1,4,19),_CurrMonthRxWwan0Kib_Type())
currMonthRxWwan0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthRxWwan0Kib.setStatus(_B)
_CurrMonthTxWwan0Kib_Type=Integer32
_CurrMonthTxWwan0Kib_Object=MibScalar
currMonthTxWwan0Kib=_CurrMonthTxWwan0Kib_Object((1,3,6,1,4,1,1890,1,4,20),_CurrMonthTxWwan0Kib_Type())
currMonthTxWwan0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthTxWwan0Kib.setStatus(_B)
_CurrMonthTotalWwan0Kib_Type=Integer32
_CurrMonthTotalWwan0Kib_Object=MibScalar
currMonthTotalWwan0Kib=_CurrMonthTotalWwan0Kib_Object((1,3,6,1,4,1,1890,1,4,21),_CurrMonthTotalWwan0Kib_Type())
currMonthTotalWwan0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthTotalWwan0Kib.setStatus(_B)
_PreMonthRxWwan0Kib_Type=Integer32
_PreMonthRxWwan0Kib_Object=MibScalar
preMonthRxWwan0Kib=_PreMonthRxWwan0Kib_Object((1,3,6,1,4,1,1890,1,4,22),_PreMonthRxWwan0Kib_Type())
preMonthRxWwan0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthRxWwan0Kib.setStatus(_B)
_PreMonthTxWwan0Kib_Type=Integer32
_PreMonthTxWwan0Kib_Object=MibScalar
preMonthTxWwan0Kib=_PreMonthTxWwan0Kib_Object((1,3,6,1,4,1,1890,1,4,23),_PreMonthTxWwan0Kib_Type())
preMonthTxWwan0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthTxWwan0Kib.setStatus(_B)
_PreMonthTotalWwan0Kib_Type=Integer32
_PreMonthTotalWwan0Kib_Object=MibScalar
preMonthTotalWwan0Kib=_PreMonthTotalWwan0Kib_Object((1,3,6,1,4,1,1890,1,4,24),_PreMonthTotalWwan0Kib_Type())
preMonthTotalWwan0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthTotalWwan0Kib.setStatus(_B)
_Trafficeth0_ObjectIdentity=ObjectIdentity
trafficeth0=_Trafficeth0_ObjectIdentity((1,3,6,1,4,1,1890,1,5))
_TodayRxEth0_Type=DisplayString
_TodayRxEth0_Object=MibScalar
todayRxEth0=_TodayRxEth0_Object((1,3,6,1,4,1,1890,1,5,1),_TodayRxEth0_Type())
todayRxEth0.setMaxAccess(_A)
if mibBuilder.loadTexts:todayRxEth0.setStatus(_B)
_TodayTxEth0_Type=DisplayString
_TodayTxEth0_Object=MibScalar
todayTxEth0=_TodayTxEth0_Object((1,3,6,1,4,1,1890,1,5,2),_TodayTxEth0_Type())
todayTxEth0.setMaxAccess(_A)
if mibBuilder.loadTexts:todayTxEth0.setStatus(_B)
_TodayTotalEth0_Type=DisplayString
_TodayTotalEth0_Object=MibScalar
todayTotalEth0=_TodayTotalEth0_Object((1,3,6,1,4,1,1890,1,5,3),_TodayTotalEth0_Type())
todayTotalEth0.setMaxAccess(_A)
if mibBuilder.loadTexts:todayTotalEth0.setStatus(_B)
_YesterdayRxEth0_Type=DisplayString
_YesterdayRxEth0_Object=MibScalar
yesterdayRxEth0=_YesterdayRxEth0_Object((1,3,6,1,4,1,1890,1,5,4),_YesterdayRxEth0_Type())
yesterdayRxEth0.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayRxEth0.setStatus(_B)
_YesterdayTxEth0_Type=DisplayString
_YesterdayTxEth0_Object=MibScalar
yesterdayTxEth0=_YesterdayTxEth0_Object((1,3,6,1,4,1,1890,1,5,5),_YesterdayTxEth0_Type())
yesterdayTxEth0.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayTxEth0.setStatus(_B)
_YesterdayTotalEth0_Type=DisplayString
_YesterdayTotalEth0_Object=MibScalar
yesterdayTotalEth0=_YesterdayTotalEth0_Object((1,3,6,1,4,1,1890,1,5,6),_YesterdayTotalEth0_Type())
yesterdayTotalEth0.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayTotalEth0.setStatus(_B)
_CurrMonthRxEth0_Type=DisplayString
_CurrMonthRxEth0_Object=MibScalar
currMonthRxEth0=_CurrMonthRxEth0_Object((1,3,6,1,4,1,1890,1,5,7),_CurrMonthRxEth0_Type())
currMonthRxEth0.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthRxEth0.setStatus(_B)
_CurrMonthTxEth0_Type=DisplayString
_CurrMonthTxEth0_Object=MibScalar
currMonthTxEth0=_CurrMonthTxEth0_Object((1,3,6,1,4,1,1890,1,5,8),_CurrMonthTxEth0_Type())
currMonthTxEth0.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthTxEth0.setStatus(_B)
_CurrMonthTotalEth0_Type=DisplayString
_CurrMonthTotalEth0_Object=MibScalar
currMonthTotalEth0=_CurrMonthTotalEth0_Object((1,3,6,1,4,1,1890,1,5,9),_CurrMonthTotalEth0_Type())
currMonthTotalEth0.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthTotalEth0.setStatus(_B)
_PreMonthRxEth0_Type=DisplayString
_PreMonthRxEth0_Object=MibScalar
preMonthRxEth0=_PreMonthRxEth0_Object((1,3,6,1,4,1,1890,1,5,10),_PreMonthRxEth0_Type())
preMonthRxEth0.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthRxEth0.setStatus(_B)
_PreMonthTxEth0_Type=DisplayString
_PreMonthTxEth0_Object=MibScalar
preMonthTxEth0=_PreMonthTxEth0_Object((1,3,6,1,4,1,1890,1,5,11),_PreMonthTxEth0_Type())
preMonthTxEth0.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthTxEth0.setStatus(_B)
_PreMonthTotalEth0_Type=DisplayString
_PreMonthTotalEth0_Object=MibScalar
preMonthTotalEth0=_PreMonthTotalEth0_Object((1,3,6,1,4,1,1890,1,5,12),_PreMonthTotalEth0_Type())
preMonthTotalEth0.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthTotalEth0.setStatus(_B)
_TodayRxEth0Kib_Type=Integer32
_TodayRxEth0Kib_Object=MibScalar
todayRxEth0Kib=_TodayRxEth0Kib_Object((1,3,6,1,4,1,1890,1,5,13),_TodayRxEth0Kib_Type())
todayRxEth0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:todayRxEth0Kib.setStatus(_B)
_TodayTxEth0Kib_Type=Integer32
_TodayTxEth0Kib_Object=MibScalar
todayTxEth0Kib=_TodayTxEth0Kib_Object((1,3,6,1,4,1,1890,1,5,14),_TodayTxEth0Kib_Type())
todayTxEth0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:todayTxEth0Kib.setStatus(_B)
_TodayTotalEth0Kib_Type=Integer32
_TodayTotalEth0Kib_Object=MibScalar
todayTotalEth0Kib=_TodayTotalEth0Kib_Object((1,3,6,1,4,1,1890,1,5,15),_TodayTotalEth0Kib_Type())
todayTotalEth0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:todayTotalEth0Kib.setStatus(_B)
_YesterdayRxEth0Kib_Type=Integer32
_YesterdayRxEth0Kib_Object=MibScalar
yesterdayRxEth0Kib=_YesterdayRxEth0Kib_Object((1,3,6,1,4,1,1890,1,5,16),_YesterdayRxEth0Kib_Type())
yesterdayRxEth0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayRxEth0Kib.setStatus(_B)
_YesterdayTxEth0Kib_Type=Integer32
_YesterdayTxEth0Kib_Object=MibScalar
yesterdayTxEth0Kib=_YesterdayTxEth0Kib_Object((1,3,6,1,4,1,1890,1,5,17),_YesterdayTxEth0Kib_Type())
yesterdayTxEth0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayTxEth0Kib.setStatus(_B)
_YesterdayTotalEth0Kib_Type=Integer32
_YesterdayTotalEth0Kib_Object=MibScalar
yesterdayTotalEth0Kib=_YesterdayTotalEth0Kib_Object((1,3,6,1,4,1,1890,1,5,18),_YesterdayTotalEth0Kib_Type())
yesterdayTotalEth0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayTotalEth0Kib.setStatus(_B)
_CurrMonthRxEth0Kib_Type=Integer32
_CurrMonthRxEth0Kib_Object=MibScalar
currMonthRxEth0Kib=_CurrMonthRxEth0Kib_Object((1,3,6,1,4,1,1890,1,5,19),_CurrMonthRxEth0Kib_Type())
currMonthRxEth0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthRxEth0Kib.setStatus(_B)
_CurrMonthTxEth0Kib_Type=Integer32
_CurrMonthTxEth0Kib_Object=MibScalar
currMonthTxEth0Kib=_CurrMonthTxEth0Kib_Object((1,3,6,1,4,1,1890,1,5,20),_CurrMonthTxEth0Kib_Type())
currMonthTxEth0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthTxEth0Kib.setStatus(_B)
_CurrMonthTotalEth0Kib_Type=Integer32
_CurrMonthTotalEth0Kib_Object=MibScalar
currMonthTotalEth0Kib=_CurrMonthTotalEth0Kib_Object((1,3,6,1,4,1,1890,1,5,21),_CurrMonthTotalEth0Kib_Type())
currMonthTotalEth0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthTotalEth0Kib.setStatus(_B)
_PreMonthRxEth0Kib_Type=Integer32
_PreMonthRxEth0Kib_Object=MibScalar
preMonthRxEth0Kib=_PreMonthRxEth0Kib_Object((1,3,6,1,4,1,1890,1,5,22),_PreMonthRxEth0Kib_Type())
preMonthRxEth0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthRxEth0Kib.setStatus(_B)
_PreMonthTxEth0Kib_Type=Integer32
_PreMonthTxEth0Kib_Object=MibScalar
preMonthTxEth0Kib=_PreMonthTxEth0Kib_Object((1,3,6,1,4,1,1890,1,5,23),_PreMonthTxEth0Kib_Type())
preMonthTxEth0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthTxEth0Kib.setStatus(_B)
_PreMonthTotalEth0Kib_Type=Integer32
_PreMonthTotalEth0Kib_Object=MibScalar
preMonthTotalEth0Kib=_PreMonthTotalEth0Kib_Object((1,3,6,1,4,1,1890,1,5,24),_PreMonthTotalEth0Kib_Type())
preMonthTotalEth0Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthTotalEth0Kib.setStatus(_B)
_Trafficeth1_ObjectIdentity=ObjectIdentity
trafficeth1=_Trafficeth1_ObjectIdentity((1,3,6,1,4,1,1890,1,6))
_TodayRxEth1_Type=DisplayString
_TodayRxEth1_Object=MibScalar
todayRxEth1=_TodayRxEth1_Object((1,3,6,1,4,1,1890,1,6,1),_TodayRxEth1_Type())
todayRxEth1.setMaxAccess(_A)
if mibBuilder.loadTexts:todayRxEth1.setStatus(_B)
_TodayTxEth1_Type=DisplayString
_TodayTxEth1_Object=MibScalar
todayTxEth1=_TodayTxEth1_Object((1,3,6,1,4,1,1890,1,6,2),_TodayTxEth1_Type())
todayTxEth1.setMaxAccess(_A)
if mibBuilder.loadTexts:todayTxEth1.setStatus(_B)
_TodayTotalEth1_Type=DisplayString
_TodayTotalEth1_Object=MibScalar
todayTotalEth1=_TodayTotalEth1_Object((1,3,6,1,4,1,1890,1,6,3),_TodayTotalEth1_Type())
todayTotalEth1.setMaxAccess(_A)
if mibBuilder.loadTexts:todayTotalEth1.setStatus(_B)
_YesterdayRxEth1_Type=DisplayString
_YesterdayRxEth1_Object=MibScalar
yesterdayRxEth1=_YesterdayRxEth1_Object((1,3,6,1,4,1,1890,1,6,4),_YesterdayRxEth1_Type())
yesterdayRxEth1.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayRxEth1.setStatus(_B)
_YesterdayTxEth1_Type=DisplayString
_YesterdayTxEth1_Object=MibScalar
yesterdayTxEth1=_YesterdayTxEth1_Object((1,3,6,1,4,1,1890,1,6,5),_YesterdayTxEth1_Type())
yesterdayTxEth1.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayTxEth1.setStatus(_B)
_YesterdayTotalEth1_Type=DisplayString
_YesterdayTotalEth1_Object=MibScalar
yesterdayTotalEth1=_YesterdayTotalEth1_Object((1,3,6,1,4,1,1890,1,6,6),_YesterdayTotalEth1_Type())
yesterdayTotalEth1.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayTotalEth1.setStatus(_B)
_CurrMonthRxEth1_Type=DisplayString
_CurrMonthRxEth1_Object=MibScalar
currMonthRxEth1=_CurrMonthRxEth1_Object((1,3,6,1,4,1,1890,1,6,7),_CurrMonthRxEth1_Type())
currMonthRxEth1.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthRxEth1.setStatus(_B)
_CurrMonthTxEth1_Type=DisplayString
_CurrMonthTxEth1_Object=MibScalar
currMonthTxEth1=_CurrMonthTxEth1_Object((1,3,6,1,4,1,1890,1,6,8),_CurrMonthTxEth1_Type())
currMonthTxEth1.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthTxEth1.setStatus(_B)
_CurrMonthTotalEth1_Type=DisplayString
_CurrMonthTotalEth1_Object=MibScalar
currMonthTotalEth1=_CurrMonthTotalEth1_Object((1,3,6,1,4,1,1890,1,6,9),_CurrMonthTotalEth1_Type())
currMonthTotalEth1.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthTotalEth1.setStatus(_B)
_PreMonthRxEth1_Type=DisplayString
_PreMonthRxEth1_Object=MibScalar
preMonthRxEth1=_PreMonthRxEth1_Object((1,3,6,1,4,1,1890,1,6,10),_PreMonthRxEth1_Type())
preMonthRxEth1.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthRxEth1.setStatus(_B)
_PreMonthTxEth1_Type=DisplayString
_PreMonthTxEth1_Object=MibScalar
preMonthTxEth1=_PreMonthTxEth1_Object((1,3,6,1,4,1,1890,1,6,11),_PreMonthTxEth1_Type())
preMonthTxEth1.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthTxEth1.setStatus(_B)
_PreMonthTotalEth1_Type=DisplayString
_PreMonthTotalEth1_Object=MibScalar
preMonthTotalEth1=_PreMonthTotalEth1_Object((1,3,6,1,4,1,1890,1,6,12),_PreMonthTotalEth1_Type())
preMonthTotalEth1.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthTotalEth1.setStatus(_B)
_TodayRxEth1Kib_Type=Integer32
_TodayRxEth1Kib_Object=MibScalar
todayRxEth1Kib=_TodayRxEth1Kib_Object((1,3,6,1,4,1,1890,1,6,13),_TodayRxEth1Kib_Type())
todayRxEth1Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:todayRxEth1Kib.setStatus(_B)
_TodayTxEth1Kib_Type=Integer32
_TodayTxEth1Kib_Object=MibScalar
todayTxEth1Kib=_TodayTxEth1Kib_Object((1,3,6,1,4,1,1890,1,6,14),_TodayTxEth1Kib_Type())
todayTxEth1Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:todayTxEth1Kib.setStatus(_B)
_TodayTotalEth1Kib_Type=Integer32
_TodayTotalEth1Kib_Object=MibScalar
todayTotalEth1Kib=_TodayTotalEth1Kib_Object((1,3,6,1,4,1,1890,1,6,15),_TodayTotalEth1Kib_Type())
todayTotalEth1Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:todayTotalEth1Kib.setStatus(_B)
_YesterdayRxEth1Kib_Type=Integer32
_YesterdayRxEth1Kib_Object=MibScalar
yesterdayRxEth1Kib=_YesterdayRxEth1Kib_Object((1,3,6,1,4,1,1890,1,6,16),_YesterdayRxEth1Kib_Type())
yesterdayRxEth1Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayRxEth1Kib.setStatus(_B)
_YesterdayTxEth1Kib_Type=Integer32
_YesterdayTxEth1Kib_Object=MibScalar
yesterdayTxEth1Kib=_YesterdayTxEth1Kib_Object((1,3,6,1,4,1,1890,1,6,17),_YesterdayTxEth1Kib_Type())
yesterdayTxEth1Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayTxEth1Kib.setStatus(_B)
_YesterdayTotalEth1Kib_Type=Integer32
_YesterdayTotalEth1Kib_Object=MibScalar
yesterdayTotalEth1Kib=_YesterdayTotalEth1Kib_Object((1,3,6,1,4,1,1890,1,6,18),_YesterdayTotalEth1Kib_Type())
yesterdayTotalEth1Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:yesterdayTotalEth1Kib.setStatus(_B)
_CurrMonthRxEth1Kib_Type=Integer32
_CurrMonthRxEth1Kib_Object=MibScalar
currMonthRxEth1Kib=_CurrMonthRxEth1Kib_Object((1,3,6,1,4,1,1890,1,6,19),_CurrMonthRxEth1Kib_Type())
currMonthRxEth1Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthRxEth1Kib.setStatus(_B)
_CurrMonthTxEth1Kib_Type=Integer32
_CurrMonthTxEth1Kib_Object=MibScalar
currMonthTxEth1Kib=_CurrMonthTxEth1Kib_Object((1,3,6,1,4,1,1890,1,6,20),_CurrMonthTxEth1Kib_Type())
currMonthTxEth1Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthTxEth1Kib.setStatus(_B)
_CurrMonthTotalEth1Kib_Type=Integer32
_CurrMonthTotalEth1Kib_Object=MibScalar
currMonthTotalEth1Kib=_CurrMonthTotalEth1Kib_Object((1,3,6,1,4,1,1890,1,6,21),_CurrMonthTotalEth1Kib_Type())
currMonthTotalEth1Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:currMonthTotalEth1Kib.setStatus(_B)
_PreMonthRxEth1Kib_Type=Integer32
_PreMonthRxEth1Kib_Object=MibScalar
preMonthRxEth1Kib=_PreMonthRxEth1Kib_Object((1,3,6,1,4,1,1890,1,6,22),_PreMonthRxEth1Kib_Type())
preMonthRxEth1Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthRxEth1Kib.setStatus(_B)
_PreMonthTxEth1Kib_Type=Integer32
_PreMonthTxEth1Kib_Object=MibScalar
preMonthTxEth1Kib=_PreMonthTxEth1Kib_Object((1,3,6,1,4,1,1890,1,6,23),_PreMonthTxEth1Kib_Type())
preMonthTxEth1Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthTxEth1Kib.setStatus(_B)
_PreMonthTotalEth1Kib_Type=Integer32
_PreMonthTotalEth1Kib_Object=MibScalar
preMonthTotalEth1Kib=_PreMonthTotalEth1Kib_Object((1,3,6,1,4,1,1890,1,6,24),_PreMonthTotalEth1Kib_Type())
preMonthTotalEth1Kib.setMaxAccess(_A)
if mibBuilder.loadTexts:preMonthTotalEth1Kib.setStatus(_B)
_Gpscurrent_ObjectIdentity=ObjectIdentity
gpscurrent=_Gpscurrent_ObjectIdentity((1,3,6,1,4,1,1890,1,7))
_CurrentGpsValid_Type=DisplayString
_CurrentGpsValid_Object=MibScalar
currentGpsValid=_CurrentGpsValid_Object((1,3,6,1,4,1,1890,1,7,1),_CurrentGpsValid_Type())
currentGpsValid.setMaxAccess(_A)
if mibBuilder.loadTexts:currentGpsValid.setStatus(_B)
_CurrentGpsLat_Type=DisplayString
_CurrentGpsLat_Object=MibScalar
currentGpsLat=_CurrentGpsLat_Object((1,3,6,1,4,1,1890,1,7,2),_CurrentGpsLat_Type())
currentGpsLat.setMaxAccess(_A)
if mibBuilder.loadTexts:currentGpsLat.setStatus(_B)
_CurrentGpsLong_Type=DisplayString
_CurrentGpsLong_Object=MibScalar
currentGpsLong=_CurrentGpsLong_Object((1,3,6,1,4,1,1890,1,7,3),_CurrentGpsLong_Type())
currentGpsLong.setMaxAccess(_A)
if mibBuilder.loadTexts:currentGpsLong.setStatus(_B)
_CurrentGpsAlt_Type=DisplayString
_CurrentGpsAlt_Object=MibScalar
currentGpsAlt=_CurrentGpsAlt_Object((1,3,6,1,4,1,1890,1,7,4),_CurrentGpsAlt_Type())
currentGpsAlt.setMaxAccess(_A)
if mibBuilder.loadTexts:currentGpsAlt.setStatus(_B)
_CurrentGpsTimeStamp_Type=DisplayString
_CurrentGpsTimeStamp_Object=MibScalar
currentGpsTimeStamp=_CurrentGpsTimeStamp_Object((1,3,6,1,4,1,1890,1,7,5),_CurrentGpsTimeStamp_Type())
currentGpsTimeStamp.setMaxAccess(_A)
if mibBuilder.loadTexts:currentGpsTimeStamp.setStatus(_B)
_CurrentGpsNumSat_Type=DisplayString
_CurrentGpsNumSat_Object=MibScalar
currentGpsNumSat=_CurrentGpsNumSat_Object((1,3,6,1,4,1,1890,1,7,6),_CurrentGpsNumSat_Type())
currentGpsNumSat.setMaxAccess(_A)
if mibBuilder.loadTexts:currentGpsNumSat.setStatus(_B)
_CurrentGpsFtfromcp_Type=DisplayString
_CurrentGpsFtfromcp_Object=MibScalar
currentGpsFtfromcp=_CurrentGpsFtfromcp_Object((1,3,6,1,4,1,1890,1,7,7),_CurrentGpsFtfromcp_Type())
currentGpsFtfromcp.setMaxAccess(_A)
if mibBuilder.loadTexts:currentGpsFtfromcp.setStatus(_B)
_CurrentGpsSpeed_Type=DisplayString
_CurrentGpsSpeed_Object=MibScalar
currentGpsSpeed=_CurrentGpsSpeed_Object((1,3,6,1,4,1,1890,1,7,8),_CurrentGpsSpeed_Type())
currentGpsSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:currentGpsSpeed.setStatus(_B)
_CurrentGpsCourse_Type=DisplayString
_CurrentGpsCourse_Object=MibScalar
currentGpsCourse=_CurrentGpsCourse_Object((1,3,6,1,4,1,1890,1,7,9),_CurrentGpsCourse_Type())
currentGpsCourse.setMaxAccess(_A)
if mibBuilder.loadTexts:currentGpsCourse.setStatus(_B)
_GpsSource_Type=DisplayString
_GpsSource_Object=MibScalar
gpsSource=_GpsSource_Object((1,3,6,1,4,1,1890,1,7,10),_GpsSource_Type())
gpsSource.setMaxAccess(_A)
if mibBuilder.loadTexts:gpsSource.setStatus(_B)
_GpsLockdownState_Type=DisplayString
_GpsLockdownState_Object=MibScalar
gpsLockdownState=_GpsLockdownState_Object((1,3,6,1,4,1,1890,1,7,11),_GpsLockdownState_Type())
gpsLockdownState.setMaxAccess(_A)
if mibBuilder.loadTexts:gpsLockdownState.setStatus(_B)
_GpsLockdownRadius_Type=DisplayString
_GpsLockdownRadius_Object=MibScalar
gpsLockdownRadius=_GpsLockdownRadius_Object((1,3,6,1,4,1,1890,1,7,12),_GpsLockdownRadius_Type())
gpsLockdownRadius.setMaxAccess(_A)
if mibBuilder.loadTexts:gpsLockdownRadius.setStatus(_B)
mibBuilder.exportSymbols('RED-LION-RAM-MIB',**{'redlionram':redlionram,'system':system,'unitInfo':unitInfo,'unitDescription':unitDescription,'unitSerialNumber':unitSerialNumber,'unitFirmwareVersion':unitFirmwareVersion,'unitName':unitName,'cellular':cellular,'mdn':mdn,'minIMEI':minIMEI,'nai':nai,'sipUser':sipUser,'sid':sid,'nid':nid,'prl':prl,'activated':activated,'omaSupported':omaSupported,'currentMipProfile':currentMipProfile,'esn':esn,'pesn':pesn,'meid':meid,'vendor':vendor,'modelName':modelName,'fwVersion':fwVersion,'hwVersion':hwVersion,'carrier':carrier,'lowRssi':lowRssi,'lowEcio':lowEcio,'highRssi':highRssi,'highEcio':highEcio,'currentRssi':currentRssi,'currentEcio':currentEcio,'svcType':svcType,'currentChannel':currentChannel,'cdmaType':cdmaType,'hdrType':hdrType,'cdmaRoaming':cdmaRoaming,'hdrRoaming':hdrRoaming,'roaming':roaming,'currentState':currentState,'speedPref':speedPref,'roamPref':roamPref,'devName':devName,'ifName':ifName,'txCount':txCount,'rxCount':rxCount,'gprsState':gprsState,'rxLevel':rxLevel,'servingCell':servingCell,'rccState':rccState,'gsmChannel':gsmChannel,'psState':psState,'mode':mode,'temperature':temperature,'simContextApn0':simContextApn0,'simContextApn1':simContextApn1,'simStatus':simStatus,'serviceDomain':serviceDomain,'availServiceType':availServiceType,'wCdmaL1State':wCdmaL1State,'mmcsState':mmcsState,'gmmPsState':gmmPsState,'wCdmaChannel':wCdmaChannel,'wCdmaBand':wCdmaBand,'systemMode':systemMode,'powerOnTime':powerOnTime,'lowSpeedCsq':lowSpeedCsq,'highSpeedCsq':highSpeedCsq,'band':band,'imei':imei,'simId':simId,'carrPLMN':carrPLMN,'rxLevelC0':rxLevelC0,'rxLevelC1':rxLevelC1,'locAreaCode':locAreaCode,'lteBand':lteBand,'lteRxChan':lteRxChan,'lteTxChan':lteTxChan,'lteBW':lteBW,'lteRSRP':lteRSRP,'lteRSRQ':lteRSRQ,'lteTracAreaCode':lteTracAreaCode,'creg':creg,'cellularUpTime':cellularUpTime,'lteRSRPint':lteRSRPint,'lteRSRQint':lteRSRQint,'lteSINRint':lteSINRint,'trafficppp0':trafficppp0,'todayRxPpp0':todayRxPpp0,'todayTxPpp0':todayTxPpp0,'todayTotalPpp0':todayTotalPpp0,'yesterdayRxPpp0':yesterdayRxPpp0,'yesterdayTxPpp0':yesterdayTxPpp0,'yesterdayTotalPpp0':yesterdayTotalPpp0,'currMonthRxPpp0':currMonthRxPpp0,'currMonthTxPpp0':currMonthTxPpp0,'currMonthTotalPpp0':currMonthTotalPpp0,'preMonthRxPpp0':preMonthRxPpp0,'preMonthTxPpp0':preMonthTxPpp0,'preMonthTotalPpp0':preMonthTotalPpp0,'todayRxPpp0Kib':todayRxPpp0Kib,'todayTxPpp0Kib':todayTxPpp0Kib,'todayTotalPpp0Kib':todayTotalPpp0Kib,'yesterdayRxPpp0Kib':yesterdayRxPpp0Kib,'yesterdayTxPpp0Kib':yesterdayTxPpp0Kib,'yesterdayTotalPpp0Kib':yesterdayTotalPpp0Kib,'currMonthRxPpp0Kib':currMonthRxPpp0Kib,'currMonthTxPpp0Kib':currMonthTxPpp0Kib,'currMonthTotalPpp0Kib':currMonthTotalPpp0Kib,'preMonthRxPpp0Kib':preMonthRxPpp0Kib,'preMonthTxPpp0Kib':preMonthTxPpp0Kib,'preMonthTotalPpp0Kib':preMonthTotalPpp0Kib,'trafficwwan0':trafficwwan0,'todayRxWwan0':todayRxWwan0,'todayTxWwan0':todayTxWwan0,'todayTotalWwan0':todayTotalWwan0,'yesterdayRxWwan0':yesterdayRxWwan0,'yesterdayTxWwan0':yesterdayTxWwan0,'yesterdayTotalWwan0':yesterdayTotalWwan0,'currMonthRxWwan0':currMonthRxWwan0,'currMonthTxWwan0':currMonthTxWwan0,'currMonthTotalWwan0':currMonthTotalWwan0,'preMonthRxWwan0':preMonthRxWwan0,'preMonthTxWwan0':preMonthTxWwan0,'preMonthTotalWwan0':preMonthTotalWwan0,'todayRxWwan0Kib':todayRxWwan0Kib,'todayTxWwan0Kib':todayTxWwan0Kib,'todayTotalWwan0Kib':todayTotalWwan0Kib,'yesterdayRxWwan0Kib':yesterdayRxWwan0Kib,'yesterdayTxWwan0Kib':yesterdayTxWwan0Kib,'yesterdayTotalWwan0Kib':yesterdayTotalWwan0Kib,'currMonthRxWwan0Kib':currMonthRxWwan0Kib,'currMonthTxWwan0Kib':currMonthTxWwan0Kib,'currMonthTotalWwan0Kib':currMonthTotalWwan0Kib,'preMonthRxWwan0Kib':preMonthRxWwan0Kib,'preMonthTxWwan0Kib':preMonthTxWwan0Kib,'preMonthTotalWwan0Kib':preMonthTotalWwan0Kib,'trafficeth0':trafficeth0,'todayRxEth0':todayRxEth0,'todayTxEth0':todayTxEth0,'todayTotalEth0':todayTotalEth0,'yesterdayRxEth0':yesterdayRxEth0,'yesterdayTxEth0':yesterdayTxEth0,'yesterdayTotalEth0':yesterdayTotalEth0,'currMonthRxEth0':currMonthRxEth0,'currMonthTxEth0':currMonthTxEth0,'currMonthTotalEth0':currMonthTotalEth0,'preMonthRxEth0':preMonthRxEth0,'preMonthTxEth0':preMonthTxEth0,'preMonthTotalEth0':preMonthTotalEth0,'todayRxEth0Kib':todayRxEth0Kib,'todayTxEth0Kib':todayTxEth0Kib,'todayTotalEth0Kib':todayTotalEth0Kib,'yesterdayRxEth0Kib':yesterdayRxEth0Kib,'yesterdayTxEth0Kib':yesterdayTxEth0Kib,'yesterdayTotalEth0Kib':yesterdayTotalEth0Kib,'currMonthRxEth0Kib':currMonthRxEth0Kib,'currMonthTxEth0Kib':currMonthTxEth0Kib,'currMonthTotalEth0Kib':currMonthTotalEth0Kib,'preMonthRxEth0Kib':preMonthRxEth0Kib,'preMonthTxEth0Kib':preMonthTxEth0Kib,'preMonthTotalEth0Kib':preMonthTotalEth0Kib,'trafficeth1':trafficeth1,'todayRxEth1':todayRxEth1,'todayTxEth1':todayTxEth1,'todayTotalEth1':todayTotalEth1,'yesterdayRxEth1':yesterdayRxEth1,'yesterdayTxEth1':yesterdayTxEth1,'yesterdayTotalEth1':yesterdayTotalEth1,'currMonthRxEth1':currMonthRxEth1,'currMonthTxEth1':currMonthTxEth1,'currMonthTotalEth1':currMonthTotalEth1,'preMonthRxEth1':preMonthRxEth1,'preMonthTxEth1':preMonthTxEth1,'preMonthTotalEth1':preMonthTotalEth1,'todayRxEth1Kib':todayRxEth1Kib,'todayTxEth1Kib':todayTxEth1Kib,'todayTotalEth1Kib':todayTotalEth1Kib,'yesterdayRxEth1Kib':yesterdayRxEth1Kib,'yesterdayTxEth1Kib':yesterdayTxEth1Kib,'yesterdayTotalEth1Kib':yesterdayTotalEth1Kib,'currMonthRxEth1Kib':currMonthRxEth1Kib,'currMonthTxEth1Kib':currMonthTxEth1Kib,'currMonthTotalEth1Kib':currMonthTotalEth1Kib,'preMonthRxEth1Kib':preMonthRxEth1Kib,'preMonthTxEth1Kib':preMonthTxEth1Kib,'preMonthTotalEth1Kib':preMonthTotalEth1Kib,'gpscurrent':gpscurrent,'currentGpsValid':currentGpsValid,'currentGpsLat':currentGpsLat,'currentGpsLong':currentGpsLong,'currentGpsAlt':currentGpsAlt,'currentGpsTimeStamp':currentGpsTimeStamp,'currentGpsNumSat':currentGpsNumSat,'currentGpsFtfromcp':currentGpsFtfromcp,'currentGpsSpeed':currentGpsSpeed,'currentGpsCourse':currentGpsCourse,'gpsSource':gpsSource,'gpsLockdownState':gpsLockdownState,'gpsLockdownRadius':gpsLockdownRadius})