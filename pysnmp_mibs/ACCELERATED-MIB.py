_h='acceleratedNetworkGroup'
_g='acceleratedLocationGroup'
_f='acceleratedStatusGroup'
_e='acceleratedHardwareGroup'
_d='eventMessage'
_c='mPassthroughV6'
_b='mPassthroughV4'
_a='mNetmaskV6'
_Z='mGatewayV6'
_Y='mNetmaskV4'
_X='mGatewayV4'
_W='mIPV4Pending'
_V='mSignal'
_U='mState'
_T='mUSBspeed'
_S='mRevision'
_R='mModel'
_Q='mManufacturer'
_P='mICCID'
_O='mProviderPLMN'
_N='mProvider'
_M='mPhone'
_L='mCarrierPLMN'
_K='mCarrier'
_J='mNetworkIndex'
_I='mLocationIndex'
_H='mStatusIndex'
_G='mHardwareIndex'
_F='not-accessible'
_E='Integer32'
_D='OctetString'
_C='read-only'
_B='ACCELERATED-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
acceleratedMIB=ModuleIdentity((1,3,6,1,4,1,40083,11000))
if mibBuilder.loadTexts:acceleratedMIB.setRevisions(('2021-11-28 00:00',))
_Accelerated_ObjectIdentity=ObjectIdentity
accelerated=_Accelerated_ObjectIdentity((1,3,6,1,4,1,40083))
_ModemHardwareTable_Object=MibTable
modemHardwareTable=_ModemHardwareTable_Object((1,3,6,1,4,1,40083,1))
if mibBuilder.loadTexts:modemHardwareTable.setStatus(_A)
_ModemHardwareEntry_Object=MibTableRow
modemHardwareEntry=_ModemHardwareEntry_Object((1,3,6,1,4,1,40083,1,1))
modemHardwareEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:modemHardwareEntry.setStatus(_A)
class _MHardwareIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MHardwareIndex_Type.__name__=_E
_MHardwareIndex_Object=MibTableColumn
mHardwareIndex=_MHardwareIndex_Object((1,3,6,1,4,1,40083,1,1,1),_MHardwareIndex_Type())
mHardwareIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mHardwareIndex.setStatus(_A)
class _MCarrier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MCarrier_Type.__name__=_D
_MCarrier_Object=MibTableColumn
mCarrier=_MCarrier_Object((1,3,6,1,4,1,40083,1,1,2),_MCarrier_Type())
mCarrier.setMaxAccess(_C)
if mibBuilder.loadTexts:mCarrier.setStatus(_A)
class _MCarrierPLMN_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MCarrierPLMN_Type.__name__=_D
_MCarrierPLMN_Object=MibTableColumn
mCarrierPLMN=_MCarrierPLMN_Object((1,3,6,1,4,1,40083,1,1,3),_MCarrierPLMN_Type())
mCarrierPLMN.setMaxAccess(_C)
if mibBuilder.loadTexts:mCarrierPLMN.setStatus(_A)
class _MPhone_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MPhone_Type.__name__=_D
_MPhone_Object=MibTableColumn
mPhone=_MPhone_Object((1,3,6,1,4,1,40083,1,1,4),_MPhone_Type())
mPhone.setMaxAccess(_C)
if mibBuilder.loadTexts:mPhone.setStatus(_A)
class _MAPN_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MAPN_Type.__name__=_D
_MAPN_Object=MibTableColumn
mAPN=_MAPN_Object((1,3,6,1,4,1,40083,1,1,5),_MAPN_Type())
mAPN.setMaxAccess(_C)
if mibBuilder.loadTexts:mAPN.setStatus(_A)
class _MProvider_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MProvider_Type.__name__=_D
_MProvider_Object=MibTableColumn
mProvider=_MProvider_Object((1,3,6,1,4,1,40083,1,1,6),_MProvider_Type())
mProvider.setMaxAccess(_C)
if mibBuilder.loadTexts:mProvider.setStatus(_A)
class _MProviderPLMN_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MProviderPLMN_Type.__name__=_D
_MProviderPLMN_Object=MibTableColumn
mProviderPLMN=_MProviderPLMN_Object((1,3,6,1,4,1,40083,1,1,7),_MProviderPLMN_Type())
mProviderPLMN.setMaxAccess(_C)
if mibBuilder.loadTexts:mProviderPLMN.setStatus(_A)
class _MIMEI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MIMEI_Type.__name__=_D
_MIMEI_Object=MibTableColumn
mIMEI=_MIMEI_Object((1,3,6,1,4,1,40083,1,1,8),_MIMEI_Type())
mIMEI.setMaxAccess(_C)
if mibBuilder.loadTexts:mIMEI.setStatus(_A)
class _MIMSI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MIMSI_Type.__name__=_D
_MIMSI_Object=MibTableColumn
mIMSI=_MIMSI_Object((1,3,6,1,4,1,40083,1,1,9),_MIMSI_Type())
mIMSI.setMaxAccess(_C)
if mibBuilder.loadTexts:mIMSI.setStatus(_A)
class _MICCID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MICCID_Type.__name__=_D
_MICCID_Object=MibTableColumn
mICCID=_MICCID_Object((1,3,6,1,4,1,40083,1,1,10),_MICCID_Type())
mICCID.setMaxAccess(_C)
if mibBuilder.loadTexts:mICCID.setStatus(_A)
class _MSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MSID_Type.__name__=_D
_MSID_Object=MibTableColumn
mSID=_MSID_Object((1,3,6,1,4,1,40083,1,1,11),_MSID_Type())
mSID.setMaxAccess(_C)
if mibBuilder.loadTexts:mSID.setStatus(_A)
class _MNID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MNID_Type.__name__=_D
_MNID_Object=MibTableColumn
mNID=_MNID_Object((1,3,6,1,4,1,40083,1,1,12),_MNID_Type())
mNID.setMaxAccess(_C)
if mibBuilder.loadTexts:mNID.setStatus(_A)
class _MManufacturer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MManufacturer_Type.__name__=_D
_MManufacturer_Object=MibTableColumn
mManufacturer=_MManufacturer_Object((1,3,6,1,4,1,40083,1,1,13),_MManufacturer_Type())
mManufacturer.setMaxAccess(_C)
if mibBuilder.loadTexts:mManufacturer.setStatus(_A)
class _MModel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MModel_Type.__name__=_D
_MModel_Object=MibTableColumn
mModel=_MModel_Object((1,3,6,1,4,1,40083,1,1,14),_MModel_Type())
mModel.setMaxAccess(_C)
if mibBuilder.loadTexts:mModel.setStatus(_A)
class _MSKU_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MSKU_Type.__name__=_D
_MSKU_Object=MibTableColumn
mSKU=_MSKU_Object((1,3,6,1,4,1,40083,1,1,15),_MSKU_Type())
mSKU.setMaxAccess(_C)
if mibBuilder.loadTexts:mSKU.setStatus(_A)
class _MRevision_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MRevision_Type.__name__=_D
_MRevision_Object=MibTableColumn
mRevision=_MRevision_Object((1,3,6,1,4,1,40083,1,1,16),_MRevision_Type())
mRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:mRevision.setStatus(_A)
_MUSBspeed_Type=Integer32
_MUSBspeed_Object=MibTableColumn
mUSBspeed=_MUSBspeed_Object((1,3,6,1,4,1,40083,1,1,17),_MUSBspeed_Type())
mUSBspeed.setMaxAccess(_C)
if mibBuilder.loadTexts:mUSBspeed.setStatus(_A)
class _MPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MPort_Type.__name__=_D
_MPort_Object=MibTableColumn
mPort=_MPort_Object((1,3,6,1,4,1,40083,1,1,18),_MPort_Type())
mPort.setMaxAccess(_C)
if mibBuilder.loadTexts:mPort.setStatus(_A)
_ModemStatusTable_Object=MibTable
modemStatusTable=_ModemStatusTable_Object((1,3,6,1,4,1,40083,2))
if mibBuilder.loadTexts:modemStatusTable.setStatus(_A)
_ModemStatusEntry_Object=MibTableRow
modemStatusEntry=_ModemStatusEntry_Object((1,3,6,1,4,1,40083,2,1))
modemStatusEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:modemStatusEntry.setStatus(_A)
class _MStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MStatusIndex_Type.__name__=_E
_MStatusIndex_Object=MibTableColumn
mStatusIndex=_MStatusIndex_Object((1,3,6,1,4,1,40083,2,1,1),_MStatusIndex_Type())
mStatusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mStatusIndex.setStatus(_A)
class _MSim_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MSim_Type.__name__=_D
_MSim_Object=MibTableColumn
mSim=_MSim_Object((1,3,6,1,4,1,40083,2,1,2),_MSim_Type())
mSim.setMaxAccess(_C)
if mibBuilder.loadTexts:mSim.setStatus(_A)
class _MState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MState_Type.__name__=_D
_MState_Object=MibTableColumn
mState=_MState_Object((1,3,6,1,4,1,40083,2,1,3),_MState_Type())
mState.setMaxAccess(_C)
if mibBuilder.loadTexts:mState.setStatus(_A)
_MSignal_Type=Integer32
_MSignal_Object=MibTableColumn
mSignal=_MSignal_Object((1,3,6,1,4,1,40083,2,1,4),_MSignal_Type())
mSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:mSignal.setStatus(_A)
class _MMode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MMode_Type.__name__=_D
_MMode_Object=MibTableColumn
mMode=_MMode_Object((1,3,6,1,4,1,40083,2,1,5),_MMode_Type())
mMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mMode.setStatus(_A)
class _MCNTI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MCNTI_Type.__name__=_D
_MCNTI_Object=MibTableColumn
mCNTI=_MCNTI_Object((1,3,6,1,4,1,40083,2,1,6),_MCNTI_Type())
mCNTI.setMaxAccess(_C)
if mibBuilder.loadTexts:mCNTI.setStatus(_A)
class _MBand_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MBand_Type.__name__=_D
_MBand_Object=MibTableColumn
mBand=_MBand_Object((1,3,6,1,4,1,40083,2,1,7),_MBand_Type())
mBand.setMaxAccess(_C)
if mibBuilder.loadTexts:mBand.setStatus(_A)
class _MIf_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MIf_Type.__name__=_D
_MIf_Object=MibTableColumn
mIf=_MIf_Object((1,3,6,1,4,1,40083,2,1,8),_MIf_Type())
mIf.setMaxAccess(_C)
if mibBuilder.loadTexts:mIf.setStatus(_A)
class _MRx_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MRx_Type.__name__=_D
_MRx_Object=MibTableColumn
mRx=_MRx_Object((1,3,6,1,4,1,40083,2,1,9),_MRx_Type())
mRx.setMaxAccess(_C)
if mibBuilder.loadTexts:mRx.setStatus(_A)
class _MTx_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MTx_Type.__name__=_D
_MTx_Object=MibTableColumn
mTx=_MTx_Object((1,3,6,1,4,1,40083,2,1,10),_MTx_Type())
mTx.setMaxAccess(_C)
if mibBuilder.loadTexts:mTx.setStatus(_A)
class _MRsrp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MRsrp_Type.__name__=_D
_MRsrp_Object=MibTableColumn
mRsrp=_MRsrp_Object((1,3,6,1,4,1,40083,2,1,11),_MRsrp_Type())
mRsrp.setMaxAccess(_C)
if mibBuilder.loadTexts:mRsrp.setStatus(_A)
class _MRsrq_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MRsrq_Type.__name__=_D
_MRsrq_Object=MibTableColumn
mRsrq=_MRsrq_Object((1,3,6,1,4,1,40083,2,1,12),_MRsrq_Type())
mRsrq.setMaxAccess(_C)
if mibBuilder.loadTexts:mRsrq.setStatus(_A)
class _MSnr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MSnr_Type.__name__=_D
_MSnr_Object=MibTableColumn
mSnr=_MSnr_Object((1,3,6,1,4,1,40083,2,1,13),_MSnr_Type())
mSnr.setMaxAccess(_C)
if mibBuilder.loadTexts:mSnr.setStatus(_A)
class _MSinr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MSinr_Type.__name__=_D
_MSinr_Object=MibTableColumn
mSinr=_MSinr_Object((1,3,6,1,4,1,40083,2,1,14),_MSinr_Type())
mSinr.setMaxAccess(_C)
if mibBuilder.loadTexts:mSinr.setStatus(_A)
class _MEcio_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MEcio_Type.__name__=_D
_MEcio_Object=MibTableColumn
mEcio=_MEcio_Object((1,3,6,1,4,1,40083,2,1,15),_MEcio_Type())
mEcio.setMaxAccess(_C)
if mibBuilder.loadTexts:mEcio.setStatus(_A)
class _MRssi_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MRssi_Type.__name__=_D
_MRssi_Object=MibTableColumn
mRssi=_MRssi_Object((1,3,6,1,4,1,40083,2,1,16),_MRssi_Type())
mRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:mRssi.setStatus(_A)
class _MBars_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MBars_Type.__name__=_D
_MBars_Object=MibTableColumn
mBars=_MBars_Object((1,3,6,1,4,1,40083,2,1,17),_MBars_Type())
mBars.setMaxAccess(_C)
if mibBuilder.loadTexts:mBars.setStatus(_A)
class _MTemp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MTemp_Type.__name__=_D
_MTemp_Object=MibTableColumn
mTemp=_MTemp_Object((1,3,6,1,4,1,40083,2,1,18),_MTemp_Type())
mTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:mTemp.setStatus(_A)
_ModemLocationTable_Object=MibTable
modemLocationTable=_ModemLocationTable_Object((1,3,6,1,4,1,40083,3))
if mibBuilder.loadTexts:modemLocationTable.setStatus(_A)
_ModemLocationEntry_Object=MibTableRow
modemLocationEntry=_ModemLocationEntry_Object((1,3,6,1,4,1,40083,3,1))
modemLocationEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:modemLocationEntry.setStatus(_A)
class _MLocationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MLocationIndex_Type.__name__=_E
_MLocationIndex_Object=MibTableColumn
mLocationIndex=_MLocationIndex_Object((1,3,6,1,4,1,40083,3,1,1),_MLocationIndex_Type())
mLocationIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mLocationIndex.setStatus(_A)
class _MCid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MCid_Type.__name__=_D
_MCid_Object=MibTableColumn
mCid=_MCid_Object((1,3,6,1,4,1,40083,3,1,2),_MCid_Type())
mCid.setMaxAccess(_C)
if mibBuilder.loadTexts:mCid.setStatus(_A)
class _MLac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MLac_Type.__name__=_D
_MLac_Object=MibTableColumn
mLac=_MLac_Object((1,3,6,1,4,1,40083,3,1,3),_MLac_Type())
mLac.setMaxAccess(_C)
if mibBuilder.loadTexts:mLac.setStatus(_A)
class _MMcc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MMcc_Type.__name__=_D
_MMcc_Object=MibTableColumn
mMcc=_MMcc_Object((1,3,6,1,4,1,40083,3,1,4),_MMcc_Type())
mMcc.setMaxAccess(_C)
if mibBuilder.loadTexts:mMcc.setStatus(_A)
class _MMnc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MMnc_Type.__name__=_D
_MMnc_Object=MibTableColumn
mMnc=_MMnc_Object((1,3,6,1,4,1,40083,3,1,5),_MMnc_Type())
mMnc.setMaxAccess(_C)
if mibBuilder.loadTexts:mMnc.setStatus(_A)
_ModemNetworkTable_Object=MibTable
modemNetworkTable=_ModemNetworkTable_Object((1,3,6,1,4,1,40083,4))
if mibBuilder.loadTexts:modemNetworkTable.setStatus(_A)
_ModemNetworkEntry_Object=MibTableRow
modemNetworkEntry=_ModemNetworkEntry_Object((1,3,6,1,4,1,40083,4,1))
modemNetworkEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:modemNetworkEntry.setStatus(_A)
class _MNetworkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MNetworkIndex_Type.__name__=_E
_MNetworkIndex_Object=MibTableColumn
mNetworkIndex=_MNetworkIndex_Object((1,3,6,1,4,1,40083,4,1,1),_MNetworkIndex_Type())
mNetworkIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mNetworkIndex.setStatus(_A)
class _MIPV4Pending_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MIPV4Pending_Type.__name__=_D
_MIPV4Pending_Object=MibTableColumn
mIPV4Pending=_MIPV4Pending_Object((1,3,6,1,4,1,40083,4,1,2),_MIPV4Pending_Type())
mIPV4Pending.setMaxAccess(_C)
if mibBuilder.loadTexts:mIPV4Pending.setStatus(_A)
class _MIPV4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MIPV4_Type.__name__=_D
_MIPV4_Object=MibTableColumn
mIPV4=_MIPV4_Object((1,3,6,1,4,1,40083,4,1,3),_MIPV4_Type())
mIPV4.setMaxAccess(_C)
if mibBuilder.loadTexts:mIPV4.setStatus(_A)
class _MGatewayV4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MGatewayV4_Type.__name__=_D
_MGatewayV4_Object=MibTableColumn
mGatewayV4=_MGatewayV4_Object((1,3,6,1,4,1,40083,4,1,4),_MGatewayV4_Type())
mGatewayV4.setMaxAccess(_C)
if mibBuilder.loadTexts:mGatewayV4.setStatus(_A)
class _MNetmaskV4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MNetmaskV4_Type.__name__=_D
_MNetmaskV4_Object=MibTableColumn
mNetmaskV4=_MNetmaskV4_Object((1,3,6,1,4,1,40083,4,1,5),_MNetmaskV4_Type())
mNetmaskV4.setMaxAccess(_C)
if mibBuilder.loadTexts:mNetmaskV4.setStatus(_A)
class _MIPV6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MIPV6_Type.__name__=_D
_MIPV6_Object=MibTableColumn
mIPV6=_MIPV6_Object((1,3,6,1,4,1,40083,4,1,6),_MIPV6_Type())
mIPV6.setMaxAccess(_C)
if mibBuilder.loadTexts:mIPV6.setStatus(_A)
class _MGatewayV6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MGatewayV6_Type.__name__=_D
_MGatewayV6_Object=MibTableColumn
mGatewayV6=_MGatewayV6_Object((1,3,6,1,4,1,40083,4,1,7),_MGatewayV6_Type())
mGatewayV6.setMaxAccess(_C)
if mibBuilder.loadTexts:mGatewayV6.setStatus(_A)
class _MNetmaskV6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MNetmaskV6_Type.__name__=_D
_MNetmaskV6_Object=MibTableColumn
mNetmaskV6=_MNetmaskV6_Object((1,3,6,1,4,1,40083,4,1,8),_MNetmaskV6_Type())
mNetmaskV6.setMaxAccess(_C)
if mibBuilder.loadTexts:mNetmaskV6.setStatus(_A)
class _MPassthroughV4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MPassthroughV4_Type.__name__=_D
_MPassthroughV4_Object=MibTableColumn
mPassthroughV4=_MPassthroughV4_Object((1,3,6,1,4,1,40083,4,1,9),_MPassthroughV4_Type())
mPassthroughV4.setMaxAccess(_C)
if mibBuilder.loadTexts:mPassthroughV4.setStatus(_A)
class _MPassthroughV6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MPassthroughV6_Type.__name__=_D
_MPassthroughV6_Object=MibTableColumn
mPassthroughV6=_MPassthroughV6_Object((1,3,6,1,4,1,40083,4,1,10),_MPassthroughV6_Type())
mPassthroughV6.setMaxAccess(_C)
if mibBuilder.loadTexts:mPassthroughV6.setStatus(_A)
class _EventMessage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_EventMessage_Type.__name__=_D
_EventMessage_Object=MibScalar
eventMessage=_EventMessage_Object((1,3,6,1,4,1,40083,5,1),_EventMessage_Type())
eventMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:eventMessage.setStatus(_A)
_AcceleratedConformance_ObjectIdentity=ObjectIdentity
acceleratedConformance=_AcceleratedConformance_ObjectIdentity((1,3,6,1,4,1,40083,100))
_AcceleratedConformanceGroups_ObjectIdentity=ObjectIdentity
acceleratedConformanceGroups=_AcceleratedConformanceGroups_ObjectIdentity((1,3,6,1,4,1,40083,100,1))
_AcceleratedConformanceCompliances_ObjectIdentity=ObjectIdentity
acceleratedConformanceCompliances=_AcceleratedConformanceCompliances_ObjectIdentity((1,3,6,1,4,1,40083,100,2))
acceleratedHardwareGroup=ObjectGroup((1,3,6,1,4,1,40083,100,1,1))
acceleratedHardwareGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,'mAPN'),(_B,_N),(_B,_O),(_B,'mIMEI'),(_B,'mIMSI'),(_B,_P),(_B,'mSID'),(_B,'mNID'),(_B,_Q),(_B,_R),(_B,'mSKU'),(_B,_S),(_B,_T),(_B,'mPort')))
if mibBuilder.loadTexts:acceleratedHardwareGroup.setStatus(_A)
acceleratedStatusGroup=ObjectGroup((1,3,6,1,4,1,40083,100,1,2))
acceleratedStatusGroup.setObjects(*((_B,'mSim'),(_B,_U),(_B,_V),(_B,'mMode'),(_B,'mCNTI'),(_B,'mBand'),(_B,'mIf'),(_B,'mRx'),(_B,'mTx'),(_B,'mRsrp'),(_B,'mRsrq'),(_B,'mSnr'),(_B,'mSinr'),(_B,'mEcio'),(_B,'mRssi'),(_B,'mBars'),(_B,'mTemp')))
if mibBuilder.loadTexts:acceleratedStatusGroup.setStatus(_A)
acceleratedLocationGroup=ObjectGroup((1,3,6,1,4,1,40083,100,1,3))
acceleratedLocationGroup.setObjects(*((_B,'mCid'),(_B,'mLac'),(_B,'mMcc'),(_B,'mMnc')))
if mibBuilder.loadTexts:acceleratedLocationGroup.setStatus(_A)
acceleratedNetworkGroup=ObjectGroup((1,3,6,1,4,1,40083,100,1,4))
acceleratedNetworkGroup.setObjects(*((_B,_W),(_B,'mIPV4'),(_B,_X),(_B,_Y),(_B,'mIPV6'),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:acceleratedNetworkGroup.setStatus(_A)
event=NotificationType((1,3,6,1,4,1,40083,5))
event.setObjects((_B,_d))
if mibBuilder.loadTexts:event.setStatus(_A)
acceleratedConformanceCompliance=ModuleCompliance((1,3,6,1,4,1,40083,100,2,1))
acceleratedConformanceCompliance.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:acceleratedConformanceCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'accelerated':accelerated,'modemHardwareTable':modemHardwareTable,'modemHardwareEntry':modemHardwareEntry,_G:mHardwareIndex,_K:mCarrier,_L:mCarrierPLMN,_M:mPhone,'mAPN':mAPN,_N:mProvider,_O:mProviderPLMN,'mIMEI':mIMEI,'mIMSI':mIMSI,_P:mICCID,'mSID':mSID,'mNID':mNID,_Q:mManufacturer,_R:mModel,'mSKU':mSKU,_S:mRevision,_T:mUSBspeed,'mPort':mPort,'modemStatusTable':modemStatusTable,'modemStatusEntry':modemStatusEntry,_H:mStatusIndex,'mSim':mSim,_U:mState,_V:mSignal,'mMode':mMode,'mCNTI':mCNTI,'mBand':mBand,'mIf':mIf,'mRx':mRx,'mTx':mTx,'mRsrp':mRsrp,'mRsrq':mRsrq,'mSnr':mSnr,'mSinr':mSinr,'mEcio':mEcio,'mRssi':mRssi,'mBars':mBars,'mTemp':mTemp,'modemLocationTable':modemLocationTable,'modemLocationEntry':modemLocationEntry,_I:mLocationIndex,'mCid':mCid,'mLac':mLac,'mMcc':mMcc,'mMnc':mMnc,'modemNetworkTable':modemNetworkTable,'modemNetworkEntry':modemNetworkEntry,_J:mNetworkIndex,_W:mIPV4Pending,'mIPV4':mIPV4,_X:mGatewayV4,_Y:mNetmaskV4,'mIPV6':mIPV6,_Z:mGatewayV6,_a:mNetmaskV6,_b:mPassthroughV4,_c:mPassthroughV6,'event':event,_d:eventMessage,'acceleratedConformance':acceleratedConformance,'acceleratedConformanceGroups':acceleratedConformanceGroups,_e:acceleratedHardwareGroup,_f:acceleratedStatusGroup,_g:acceleratedLocationGroup,_h:acceleratedNetworkGroup,'acceleratedConformanceCompliances':acceleratedConformanceCompliances,'acceleratedConformanceCompliance':acceleratedConformanceCompliance,'acceleratedMIB':acceleratedMIB})