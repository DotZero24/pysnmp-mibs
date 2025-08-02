_A7='nbsEfmOamOperState'
_A6='nbsEfmOamAdminState'
_A5='nbsEfmOamFramesLostDueToOamError'
_A4='nbsEfmOamErrFrmSecSumEvtCount'
_A3='nbsEfmOamErrFrmSecSumEvtThreshld'
_A2='nbsEfmOamErrFrmSecSumEvtWindow'
_A1='nbsEfmOamErrFrmSecSumEvtTime'
_A0='nbsEfmOamErrFrmSecSumCfgThreshld'
_z='nbsEfmOamErrFrmSecSumCfgDuration'
_y='nbsEfmOamErrFrmPerEvtCount'
_x='nbsEfmOamErrFrmPerEvtThreshld'
_w='nbsEfmOamErrFrmPerEvtWindow'
_v='nbsEfmOamErrFrmPerEvtTime'
_u='nbsEfmOamErrFrmPerCfgThreshld'
_t='nbsEfmOamErrFrmPerCfgDuration'
_s='nbsEfmOamErrFrmEvtCount'
_r='nbsEfmOamErrFrmEvtThreshld'
_q='nbsEfmOamErrFrmEvtWindow'
_p='nbsEfmOamErrFrmEvtTime'
_o='nbsEfmOamErrFrmCfgThreshld'
_n='nbsEfmOamErrFrmCfgDuration'
_m='nbsEfmOamErrSymPerEvtCount'
_l='nbsEfmOamErrSymPerEvtThreshld'
_k='nbsEfmOamErrSymPerEvtWindow'
_j='nbsEfmOamErrSymPerEvtTime'
_i='nbsEfmOamErrSymPerCfgThreshld'
_h='nbsEfmOamErrSymPerCfgDuration'
_g='nbsEfmOamOrganizationSpecificRx'
_f='nbsEfmOamOrganizationSpecificTx'
_e='nbsEfmOamVariableResponseRx'
_d='nbsEfmOamVariableResponseTx'
_c='nbsEfmOamVariableRequestRx'
_b='nbsEfmOamVariableRequestTx'
_a='nbsEfmOamLoopbackControlRx'
_Z='nbsEfmOamLoopbackControlTx'
_Y='nbsEfmOamDupEventNotificationRx'
_X='nbsEfmOamUniEventNotificationRx'
_W='nbsEfmOamEventNotificationTx'
_V='nbsEfmOamInformationRx'
_U='nbsEfmOamInformationTx'
_T='nbsEfmOamUnsupportedCodesRx'
_S='nbsEfmOamPDURx'
_R='nbsEfmOamPDUTx'
_Q='nbsEfmOamVendorDeviceVersion'
_P='nbsEfmOamVendorDeviceId'
_O='nbsEfmOamVendorOUI'
_N='nbsEfmOamState'
_M='nbsEfmOamFlagsField'
_L='nbsEfmOamPduCfg'
_K='nbsEfmOamCfg'
_J='nbsEfmOamMode'
_I='nbsEfmOamPeerIfIndex'
_H='nbsEfmOamIfIndex'
_G='notSupported'
_F='nbsEfmPhysicalIfIndex'
_E='Integer32'
_D='OctetString'
_C='read-only'
_B='NBS-EFM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
Unsigned16TC,nbs=mibBuilder.importSymbols('NBS-MIB','Unsigned16TC','nbs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsEfmMib=ModuleIdentity((1,3,6,1,4,1,629,300))
_NbsEfmObjects_ObjectIdentity=ObjectIdentity
nbsEfmObjects=_NbsEfmObjects_ObjectIdentity((1,3,6,1,4,1,629,300,1))
if mibBuilder.loadTexts:nbsEfmObjects.setStatus(_A)
_NbsEfmOamGrp_ObjectIdentity=ObjectIdentity
nbsEfmOamGrp=_NbsEfmOamGrp_ObjectIdentity((1,3,6,1,4,1,629,300,1,3))
if mibBuilder.loadTexts:nbsEfmOamGrp.setStatus(_A)
_NbsEfmOamTable_Object=MibTable
nbsEfmOamTable=_NbsEfmOamTable_Object((1,3,6,1,4,1,629,300,1,3,1))
if mibBuilder.loadTexts:nbsEfmOamTable.setStatus(_A)
_NbsEfmOamEntry_Object=MibTableRow
nbsEfmOamEntry=_NbsEfmOamEntry_Object((1,3,6,1,4,1,629,300,1,3,1,1))
nbsEfmOamEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:nbsEfmOamEntry.setStatus(_A)
_NbsEfmPhysicalIfIndex_Type=InterfaceIndex
_NbsEfmPhysicalIfIndex_Object=MibTableColumn
nbsEfmPhysicalIfIndex=_NbsEfmPhysicalIfIndex_Object((1,3,6,1,4,1,629,300,1,3,1,1,1),_NbsEfmPhysicalIfIndex_Type())
nbsEfmPhysicalIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmPhysicalIfIndex.setStatus(_A)
_NbsEfmOamIfIndex_Type=InterfaceIndex
_NbsEfmOamIfIndex_Object=MibTableColumn
nbsEfmOamIfIndex=_NbsEfmOamIfIndex_Object((1,3,6,1,4,1,629,300,1,3,1,1,2),_NbsEfmOamIfIndex_Type())
nbsEfmOamIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamIfIndex.setStatus(_A)
_NbsEfmOamPeerIfIndex_Type=InterfaceIndex
_NbsEfmOamPeerIfIndex_Object=MibTableColumn
nbsEfmOamPeerIfIndex=_NbsEfmOamPeerIfIndex_Object((1,3,6,1,4,1,629,300,1,3,1,1,3),_NbsEfmOamPeerIfIndex_Type())
nbsEfmOamPeerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamPeerIfIndex.setStatus(_A)
class _NbsEfmOamMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('passive',2),('active',3)))
_NbsEfmOamMode_Type.__name__=_E
_NbsEfmOamMode_Object=MibTableColumn
nbsEfmOamMode=_NbsEfmOamMode_Object((1,3,6,1,4,1,629,300,1,3,1,1,4),_NbsEfmOamMode_Type())
nbsEfmOamMode.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamMode.setStatus(_A)
class _NbsEfmOamCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_NbsEfmOamCfg_Type.__name__=_D
_NbsEfmOamCfg_Object=MibTableColumn
nbsEfmOamCfg=_NbsEfmOamCfg_Object((1,3,6,1,4,1,629,300,1,3,1,1,5),_NbsEfmOamCfg_Type())
nbsEfmOamCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamCfg.setStatus(_A)
_NbsEfmOamPduCfg_Type=Unsigned16TC
_NbsEfmOamPduCfg_Object=MibTableColumn
nbsEfmOamPduCfg=_NbsEfmOamPduCfg_Object((1,3,6,1,4,1,629,300,1,3,1,1,6),_NbsEfmOamPduCfg_Type())
nbsEfmOamPduCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamPduCfg.setStatus(_A)
class _NbsEfmOamFlagsField_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_NbsEfmOamFlagsField_Type.__name__=_D
_NbsEfmOamFlagsField_Object=MibTableColumn
nbsEfmOamFlagsField=_NbsEfmOamFlagsField_Object((1,3,6,1,4,1,629,300,1,3,1,1,7),_NbsEfmOamFlagsField_Type())
nbsEfmOamFlagsField.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamFlagsField.setStatus(_A)
class _NbsEfmOamState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_NbsEfmOamState_Type.__name__=_D
_NbsEfmOamState_Object=MibTableColumn
nbsEfmOamState=_NbsEfmOamState_Object((1,3,6,1,4,1,629,300,1,3,1,1,8),_NbsEfmOamState_Type())
nbsEfmOamState.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamState.setStatus(_A)
class _NbsEfmOamVendorOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_NbsEfmOamVendorOUI_Type.__name__=_D
_NbsEfmOamVendorOUI_Object=MibTableColumn
nbsEfmOamVendorOUI=_NbsEfmOamVendorOUI_Object((1,3,6,1,4,1,629,300,1,3,1,1,9),_NbsEfmOamVendorOUI_Type())
nbsEfmOamVendorOUI.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamVendorOUI.setStatus(_A)
_NbsEfmOamVendorDeviceId_Type=Unsigned16TC
_NbsEfmOamVendorDeviceId_Object=MibTableColumn
nbsEfmOamVendorDeviceId=_NbsEfmOamVendorDeviceId_Object((1,3,6,1,4,1,629,300,1,3,1,1,10),_NbsEfmOamVendorDeviceId_Type())
nbsEfmOamVendorDeviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamVendorDeviceId.setStatus(_A)
_NbsEfmOamVendorDeviceVersion_Type=Unsigned16TC
_NbsEfmOamVendorDeviceVersion_Object=MibTableColumn
nbsEfmOamVendorDeviceVersion=_NbsEfmOamVendorDeviceVersion_Object((1,3,6,1,4,1,629,300,1,3,1,1,11),_NbsEfmOamVendorDeviceVersion_Type())
nbsEfmOamVendorDeviceVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamVendorDeviceVersion.setStatus(_A)
_NbsEfmOamPDUTx_Type=Counter32
_NbsEfmOamPDUTx_Object=MibTableColumn
nbsEfmOamPDUTx=_NbsEfmOamPDUTx_Object((1,3,6,1,4,1,629,300,1,3,1,1,12),_NbsEfmOamPDUTx_Type())
nbsEfmOamPDUTx.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamPDUTx.setStatus(_A)
_NbsEfmOamPDURx_Type=Counter32
_NbsEfmOamPDURx_Object=MibTableColumn
nbsEfmOamPDURx=_NbsEfmOamPDURx_Object((1,3,6,1,4,1,629,300,1,3,1,1,13),_NbsEfmOamPDURx_Type())
nbsEfmOamPDURx.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamPDURx.setStatus(_A)
_NbsEfmOamUnsupportedCodesRx_Type=Counter32
_NbsEfmOamUnsupportedCodesRx_Object=MibTableColumn
nbsEfmOamUnsupportedCodesRx=_NbsEfmOamUnsupportedCodesRx_Object((1,3,6,1,4,1,629,300,1,3,1,1,14),_NbsEfmOamUnsupportedCodesRx_Type())
nbsEfmOamUnsupportedCodesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamUnsupportedCodesRx.setStatus(_A)
_NbsEfmOamInformationTx_Type=Counter32
_NbsEfmOamInformationTx_Object=MibTableColumn
nbsEfmOamInformationTx=_NbsEfmOamInformationTx_Object((1,3,6,1,4,1,629,300,1,3,1,1,15),_NbsEfmOamInformationTx_Type())
nbsEfmOamInformationTx.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamInformationTx.setStatus(_A)
_NbsEfmOamInformationRx_Type=Counter32
_NbsEfmOamInformationRx_Object=MibTableColumn
nbsEfmOamInformationRx=_NbsEfmOamInformationRx_Object((1,3,6,1,4,1,629,300,1,3,1,1,16),_NbsEfmOamInformationRx_Type())
nbsEfmOamInformationRx.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamInformationRx.setStatus(_A)
_NbsEfmOamEventNotificationTx_Type=Counter32
_NbsEfmOamEventNotificationTx_Object=MibTableColumn
nbsEfmOamEventNotificationTx=_NbsEfmOamEventNotificationTx_Object((1,3,6,1,4,1,629,300,1,3,1,1,17),_NbsEfmOamEventNotificationTx_Type())
nbsEfmOamEventNotificationTx.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamEventNotificationTx.setStatus(_A)
_NbsEfmOamUniEventNotificationRx_Type=Counter32
_NbsEfmOamUniEventNotificationRx_Object=MibTableColumn
nbsEfmOamUniEventNotificationRx=_NbsEfmOamUniEventNotificationRx_Object((1,3,6,1,4,1,629,300,1,3,1,1,18),_NbsEfmOamUniEventNotificationRx_Type())
nbsEfmOamUniEventNotificationRx.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamUniEventNotificationRx.setStatus(_A)
_NbsEfmOamDupEventNotificationRx_Type=Counter32
_NbsEfmOamDupEventNotificationRx_Object=MibTableColumn
nbsEfmOamDupEventNotificationRx=_NbsEfmOamDupEventNotificationRx_Object((1,3,6,1,4,1,629,300,1,3,1,1,19),_NbsEfmOamDupEventNotificationRx_Type())
nbsEfmOamDupEventNotificationRx.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamDupEventNotificationRx.setStatus(_A)
_NbsEfmOamLoopbackControlTx_Type=Counter32
_NbsEfmOamLoopbackControlTx_Object=MibTableColumn
nbsEfmOamLoopbackControlTx=_NbsEfmOamLoopbackControlTx_Object((1,3,6,1,4,1,629,300,1,3,1,1,20),_NbsEfmOamLoopbackControlTx_Type())
nbsEfmOamLoopbackControlTx.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamLoopbackControlTx.setStatus(_A)
_NbsEfmOamLoopbackControlRx_Type=Counter32
_NbsEfmOamLoopbackControlRx_Object=MibTableColumn
nbsEfmOamLoopbackControlRx=_NbsEfmOamLoopbackControlRx_Object((1,3,6,1,4,1,629,300,1,3,1,1,21),_NbsEfmOamLoopbackControlRx_Type())
nbsEfmOamLoopbackControlRx.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamLoopbackControlRx.setStatus(_A)
_NbsEfmOamVariableRequestTx_Type=Counter32
_NbsEfmOamVariableRequestTx_Object=MibTableColumn
nbsEfmOamVariableRequestTx=_NbsEfmOamVariableRequestTx_Object((1,3,6,1,4,1,629,300,1,3,1,1,22),_NbsEfmOamVariableRequestTx_Type())
nbsEfmOamVariableRequestTx.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamVariableRequestTx.setStatus(_A)
_NbsEfmOamVariableRequestRx_Type=Counter32
_NbsEfmOamVariableRequestRx_Object=MibTableColumn
nbsEfmOamVariableRequestRx=_NbsEfmOamVariableRequestRx_Object((1,3,6,1,4,1,629,300,1,3,1,1,23),_NbsEfmOamVariableRequestRx_Type())
nbsEfmOamVariableRequestRx.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamVariableRequestRx.setStatus(_A)
_NbsEfmOamVariableResponseTx_Type=Counter32
_NbsEfmOamVariableResponseTx_Object=MibTableColumn
nbsEfmOamVariableResponseTx=_NbsEfmOamVariableResponseTx_Object((1,3,6,1,4,1,629,300,1,3,1,1,24),_NbsEfmOamVariableResponseTx_Type())
nbsEfmOamVariableResponseTx.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamVariableResponseTx.setStatus(_A)
_NbsEfmOamVariableResponseRx_Type=Counter32
_NbsEfmOamVariableResponseRx_Object=MibTableColumn
nbsEfmOamVariableResponseRx=_NbsEfmOamVariableResponseRx_Object((1,3,6,1,4,1,629,300,1,3,1,1,25),_NbsEfmOamVariableResponseRx_Type())
nbsEfmOamVariableResponseRx.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamVariableResponseRx.setStatus(_A)
_NbsEfmOamOrganizationSpecificTx_Type=Counter32
_NbsEfmOamOrganizationSpecificTx_Object=MibTableColumn
nbsEfmOamOrganizationSpecificTx=_NbsEfmOamOrganizationSpecificTx_Object((1,3,6,1,4,1,629,300,1,3,1,1,26),_NbsEfmOamOrganizationSpecificTx_Type())
nbsEfmOamOrganizationSpecificTx.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamOrganizationSpecificTx.setStatus(_A)
_NbsEfmOamOrganizationSpecificRx_Type=Counter32
_NbsEfmOamOrganizationSpecificRx_Object=MibTableColumn
nbsEfmOamOrganizationSpecificRx=_NbsEfmOamOrganizationSpecificRx_Object((1,3,6,1,4,1,629,300,1,3,1,1,27),_NbsEfmOamOrganizationSpecificRx_Type())
nbsEfmOamOrganizationSpecificRx.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamOrganizationSpecificRx.setStatus(_A)
_NbsEfmOamErrSymPerCfgDuration_Type=Counter64
_NbsEfmOamErrSymPerCfgDuration_Object=MibTableColumn
nbsEfmOamErrSymPerCfgDuration=_NbsEfmOamErrSymPerCfgDuration_Object((1,3,6,1,4,1,629,300,1,3,1,1,28),_NbsEfmOamErrSymPerCfgDuration_Type())
nbsEfmOamErrSymPerCfgDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrSymPerCfgDuration.setStatus(_A)
_NbsEfmOamErrSymPerCfgThreshld_Type=Counter32
_NbsEfmOamErrSymPerCfgThreshld_Object=MibTableColumn
nbsEfmOamErrSymPerCfgThreshld=_NbsEfmOamErrSymPerCfgThreshld_Object((1,3,6,1,4,1,629,300,1,3,1,1,29),_NbsEfmOamErrSymPerCfgThreshld_Type())
nbsEfmOamErrSymPerCfgThreshld.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrSymPerCfgThreshld.setStatus(_A)
_NbsEfmOamErrSymPerEvtTime_Type=Unsigned16TC
_NbsEfmOamErrSymPerEvtTime_Object=MibTableColumn
nbsEfmOamErrSymPerEvtTime=_NbsEfmOamErrSymPerEvtTime_Object((1,3,6,1,4,1,629,300,1,3,1,1,30),_NbsEfmOamErrSymPerEvtTime_Type())
nbsEfmOamErrSymPerEvtTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrSymPerEvtTime.setStatus(_A)
_NbsEfmOamErrSymPerEvtWindow_Type=Counter64
_NbsEfmOamErrSymPerEvtWindow_Object=MibTableColumn
nbsEfmOamErrSymPerEvtWindow=_NbsEfmOamErrSymPerEvtWindow_Object((1,3,6,1,4,1,629,300,1,3,1,1,31),_NbsEfmOamErrSymPerEvtWindow_Type())
nbsEfmOamErrSymPerEvtWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrSymPerEvtWindow.setStatus(_A)
_NbsEfmOamErrSymPerEvtThreshld_Type=Counter64
_NbsEfmOamErrSymPerEvtThreshld_Object=MibTableColumn
nbsEfmOamErrSymPerEvtThreshld=_NbsEfmOamErrSymPerEvtThreshld_Object((1,3,6,1,4,1,629,300,1,3,1,1,32),_NbsEfmOamErrSymPerEvtThreshld_Type())
nbsEfmOamErrSymPerEvtThreshld.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrSymPerEvtThreshld.setStatus(_A)
_NbsEfmOamErrSymPerEvtCount_Type=Counter64
_NbsEfmOamErrSymPerEvtCount_Object=MibTableColumn
nbsEfmOamErrSymPerEvtCount=_NbsEfmOamErrSymPerEvtCount_Object((1,3,6,1,4,1,629,300,1,3,1,1,33),_NbsEfmOamErrSymPerEvtCount_Type())
nbsEfmOamErrSymPerEvtCount.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrSymPerEvtCount.setStatus(_A)
_NbsEfmOamErrFrmCfgDuration_Type=Counter32
_NbsEfmOamErrFrmCfgDuration_Object=MibTableColumn
nbsEfmOamErrFrmCfgDuration=_NbsEfmOamErrFrmCfgDuration_Object((1,3,6,1,4,1,629,300,1,3,1,1,34),_NbsEfmOamErrFrmCfgDuration_Type())
nbsEfmOamErrFrmCfgDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmCfgDuration.setStatus(_A)
_NbsEfmOamErrFrmCfgThreshld_Type=Counter32
_NbsEfmOamErrFrmCfgThreshld_Object=MibTableColumn
nbsEfmOamErrFrmCfgThreshld=_NbsEfmOamErrFrmCfgThreshld_Object((1,3,6,1,4,1,629,300,1,3,1,1,35),_NbsEfmOamErrFrmCfgThreshld_Type())
nbsEfmOamErrFrmCfgThreshld.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmCfgThreshld.setStatus(_A)
_NbsEfmOamErrFrmEvtTime_Type=Unsigned16TC
_NbsEfmOamErrFrmEvtTime_Object=MibTableColumn
nbsEfmOamErrFrmEvtTime=_NbsEfmOamErrFrmEvtTime_Object((1,3,6,1,4,1,629,300,1,3,1,1,36),_NbsEfmOamErrFrmEvtTime_Type())
nbsEfmOamErrFrmEvtTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmEvtTime.setStatus(_A)
_NbsEfmOamErrFrmEvtWindow_Type=Unsigned16TC
_NbsEfmOamErrFrmEvtWindow_Object=MibTableColumn
nbsEfmOamErrFrmEvtWindow=_NbsEfmOamErrFrmEvtWindow_Object((1,3,6,1,4,1,629,300,1,3,1,1,37),_NbsEfmOamErrFrmEvtWindow_Type())
nbsEfmOamErrFrmEvtWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmEvtWindow.setStatus(_A)
_NbsEfmOamErrFrmEvtThreshld_Type=Counter32
_NbsEfmOamErrFrmEvtThreshld_Object=MibTableColumn
nbsEfmOamErrFrmEvtThreshld=_NbsEfmOamErrFrmEvtThreshld_Object((1,3,6,1,4,1,629,300,1,3,1,1,38),_NbsEfmOamErrFrmEvtThreshld_Type())
nbsEfmOamErrFrmEvtThreshld.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmEvtThreshld.setStatus(_A)
_NbsEfmOamErrFrmEvtCount_Type=Counter64
_NbsEfmOamErrFrmEvtCount_Object=MibTableColumn
nbsEfmOamErrFrmEvtCount=_NbsEfmOamErrFrmEvtCount_Object((1,3,6,1,4,1,629,300,1,3,1,1,39),_NbsEfmOamErrFrmEvtCount_Type())
nbsEfmOamErrFrmEvtCount.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmEvtCount.setStatus(_A)
_NbsEfmOamErrFrmPerCfgDuration_Type=Counter32
_NbsEfmOamErrFrmPerCfgDuration_Object=MibTableColumn
nbsEfmOamErrFrmPerCfgDuration=_NbsEfmOamErrFrmPerCfgDuration_Object((1,3,6,1,4,1,629,300,1,3,1,1,40),_NbsEfmOamErrFrmPerCfgDuration_Type())
nbsEfmOamErrFrmPerCfgDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmPerCfgDuration.setStatus(_A)
_NbsEfmOamErrFrmPerCfgThreshld_Type=Counter32
_NbsEfmOamErrFrmPerCfgThreshld_Object=MibTableColumn
nbsEfmOamErrFrmPerCfgThreshld=_NbsEfmOamErrFrmPerCfgThreshld_Object((1,3,6,1,4,1,629,300,1,3,1,1,41),_NbsEfmOamErrFrmPerCfgThreshld_Type())
nbsEfmOamErrFrmPerCfgThreshld.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmPerCfgThreshld.setStatus(_A)
_NbsEfmOamErrFrmPerEvtTime_Type=Unsigned16TC
_NbsEfmOamErrFrmPerEvtTime_Object=MibTableColumn
nbsEfmOamErrFrmPerEvtTime=_NbsEfmOamErrFrmPerEvtTime_Object((1,3,6,1,4,1,629,300,1,3,1,1,42),_NbsEfmOamErrFrmPerEvtTime_Type())
nbsEfmOamErrFrmPerEvtTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmPerEvtTime.setStatus(_A)
_NbsEfmOamErrFrmPerEvtWindow_Type=Counter32
_NbsEfmOamErrFrmPerEvtWindow_Object=MibTableColumn
nbsEfmOamErrFrmPerEvtWindow=_NbsEfmOamErrFrmPerEvtWindow_Object((1,3,6,1,4,1,629,300,1,3,1,1,43),_NbsEfmOamErrFrmPerEvtWindow_Type())
nbsEfmOamErrFrmPerEvtWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmPerEvtWindow.setStatus(_A)
_NbsEfmOamErrFrmPerEvtThreshld_Type=Counter32
_NbsEfmOamErrFrmPerEvtThreshld_Object=MibTableColumn
nbsEfmOamErrFrmPerEvtThreshld=_NbsEfmOamErrFrmPerEvtThreshld_Object((1,3,6,1,4,1,629,300,1,3,1,1,44),_NbsEfmOamErrFrmPerEvtThreshld_Type())
nbsEfmOamErrFrmPerEvtThreshld.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmPerEvtThreshld.setStatus(_A)
_NbsEfmOamErrFrmPerEvtCount_Type=Counter64
_NbsEfmOamErrFrmPerEvtCount_Object=MibTableColumn
nbsEfmOamErrFrmPerEvtCount=_NbsEfmOamErrFrmPerEvtCount_Object((1,3,6,1,4,1,629,300,1,3,1,1,45),_NbsEfmOamErrFrmPerEvtCount_Type())
nbsEfmOamErrFrmPerEvtCount.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmPerEvtCount.setStatus(_A)
_NbsEfmOamErrFrmSecSumCfgDuration_Type=Unsigned16TC
_NbsEfmOamErrFrmSecSumCfgDuration_Object=MibTableColumn
nbsEfmOamErrFrmSecSumCfgDuration=_NbsEfmOamErrFrmSecSumCfgDuration_Object((1,3,6,1,4,1,629,300,1,3,1,1,46),_NbsEfmOamErrFrmSecSumCfgDuration_Type())
nbsEfmOamErrFrmSecSumCfgDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmSecSumCfgDuration.setStatus(_A)
_NbsEfmOamErrFrmSecSumCfgThreshld_Type=Unsigned16TC
_NbsEfmOamErrFrmSecSumCfgThreshld_Object=MibTableColumn
nbsEfmOamErrFrmSecSumCfgThreshld=_NbsEfmOamErrFrmSecSumCfgThreshld_Object((1,3,6,1,4,1,629,300,1,3,1,1,47),_NbsEfmOamErrFrmSecSumCfgThreshld_Type())
nbsEfmOamErrFrmSecSumCfgThreshld.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmSecSumCfgThreshld.setStatus(_A)
_NbsEfmOamErrFrmSecSumEvtTime_Type=Unsigned16TC
_NbsEfmOamErrFrmSecSumEvtTime_Object=MibTableColumn
nbsEfmOamErrFrmSecSumEvtTime=_NbsEfmOamErrFrmSecSumEvtTime_Object((1,3,6,1,4,1,629,300,1,3,1,1,48),_NbsEfmOamErrFrmSecSumEvtTime_Type())
nbsEfmOamErrFrmSecSumEvtTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmSecSumEvtTime.setStatus(_A)
_NbsEfmOamErrFrmSecSumEvtWindow_Type=Unsigned16TC
_NbsEfmOamErrFrmSecSumEvtWindow_Object=MibTableColumn
nbsEfmOamErrFrmSecSumEvtWindow=_NbsEfmOamErrFrmSecSumEvtWindow_Object((1,3,6,1,4,1,629,300,1,3,1,1,49),_NbsEfmOamErrFrmSecSumEvtWindow_Type())
nbsEfmOamErrFrmSecSumEvtWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmSecSumEvtWindow.setStatus(_A)
_NbsEfmOamErrFrmSecSumEvtThreshld_Type=Unsigned16TC
_NbsEfmOamErrFrmSecSumEvtThreshld_Object=MibTableColumn
nbsEfmOamErrFrmSecSumEvtThreshld=_NbsEfmOamErrFrmSecSumEvtThreshld_Object((1,3,6,1,4,1,629,300,1,3,1,1,50),_NbsEfmOamErrFrmSecSumEvtThreshld_Type())
nbsEfmOamErrFrmSecSumEvtThreshld.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmSecSumEvtThreshld.setStatus(_A)
_NbsEfmOamErrFrmSecSumEvtCount_Type=Counter32
_NbsEfmOamErrFrmSecSumEvtCount_Object=MibTableColumn
nbsEfmOamErrFrmSecSumEvtCount=_NbsEfmOamErrFrmSecSumEvtCount_Object((1,3,6,1,4,1,629,300,1,3,1,1,51),_NbsEfmOamErrFrmSecSumEvtCount_Type())
nbsEfmOamErrFrmSecSumEvtCount.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamErrFrmSecSumEvtCount.setStatus(_A)
_NbsEfmOamFramesLostDueToOamError_Type=Counter32
_NbsEfmOamFramesLostDueToOamError_Object=MibTableColumn
nbsEfmOamFramesLostDueToOamError=_NbsEfmOamFramesLostDueToOamError_Object((1,3,6,1,4,1,629,300,1,3,1,1,52),_NbsEfmOamFramesLostDueToOamError_Type())
nbsEfmOamFramesLostDueToOamError.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamFramesLostDueToOamError.setStatus(_A)
class _NbsEfmOamAdminState_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('disable',2),('enable',3)))
_NbsEfmOamAdminState_Type.__name__=_E
_NbsEfmOamAdminState_Object=MibTableColumn
nbsEfmOamAdminState=_NbsEfmOamAdminState_Object((1,3,6,1,4,1,629,300,1,3,1,1,53),_NbsEfmOamAdminState_Type())
nbsEfmOamAdminState.setMaxAccess('read-write')
if mibBuilder.loadTexts:nbsEfmOamAdminState.setStatus(_A)
class _NbsEfmOamOperState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_NbsEfmOamOperState_Type.__name__=_D
_NbsEfmOamOperState_Object=MibTableColumn
nbsEfmOamOperState=_NbsEfmOamOperState_Object((1,3,6,1,4,1,629,300,1,3,1,1,54),_NbsEfmOamOperState_Type())
nbsEfmOamOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsEfmOamOperState.setStatus(_A)
_NbsEfmProduct_ObjectIdentity=ObjectIdentity
nbsEfmProduct=_NbsEfmProduct_ObjectIdentity((1,3,6,1,4,1,629,300,2))
_NbsEfmNc316Nm_ObjectIdentity=ObjectIdentity
nbsEfmNc316Nm=_NbsEfmNc316Nm_ObjectIdentity((1,3,6,1,4,1,629,300,2,1))
_NbsEfmConformance_ObjectIdentity=ObjectIdentity
nbsEfmConformance=_NbsEfmConformance_ObjectIdentity((1,3,6,1,4,1,629,300,3))
_NbsEfmGroups_ObjectIdentity=ObjectIdentity
nbsEfmGroups=_NbsEfmGroups_ObjectIdentity((1,3,6,1,4,1,629,300,3,1))
nbsEfmOamGroup=ObjectGroup((1,3,6,1,4,1,629,300,3,1,3))
nbsEfmOamGroup.setObjects(*((_B,_F),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:nbsEfmOamGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nbsEfmMib':nbsEfmMib,'nbsEfmObjects':nbsEfmObjects,'nbsEfmOamGrp':nbsEfmOamGrp,'nbsEfmOamTable':nbsEfmOamTable,'nbsEfmOamEntry':nbsEfmOamEntry,_F:nbsEfmPhysicalIfIndex,_H:nbsEfmOamIfIndex,_I:nbsEfmOamPeerIfIndex,_J:nbsEfmOamMode,_K:nbsEfmOamCfg,_L:nbsEfmOamPduCfg,_M:nbsEfmOamFlagsField,_N:nbsEfmOamState,_O:nbsEfmOamVendorOUI,_P:nbsEfmOamVendorDeviceId,_Q:nbsEfmOamVendorDeviceVersion,_R:nbsEfmOamPDUTx,_S:nbsEfmOamPDURx,_T:nbsEfmOamUnsupportedCodesRx,_U:nbsEfmOamInformationTx,_V:nbsEfmOamInformationRx,_W:nbsEfmOamEventNotificationTx,_X:nbsEfmOamUniEventNotificationRx,_Y:nbsEfmOamDupEventNotificationRx,_Z:nbsEfmOamLoopbackControlTx,_a:nbsEfmOamLoopbackControlRx,_b:nbsEfmOamVariableRequestTx,_c:nbsEfmOamVariableRequestRx,_d:nbsEfmOamVariableResponseTx,_e:nbsEfmOamVariableResponseRx,_f:nbsEfmOamOrganizationSpecificTx,_g:nbsEfmOamOrganizationSpecificRx,_h:nbsEfmOamErrSymPerCfgDuration,_i:nbsEfmOamErrSymPerCfgThreshld,_j:nbsEfmOamErrSymPerEvtTime,_k:nbsEfmOamErrSymPerEvtWindow,_l:nbsEfmOamErrSymPerEvtThreshld,_m:nbsEfmOamErrSymPerEvtCount,_n:nbsEfmOamErrFrmCfgDuration,_o:nbsEfmOamErrFrmCfgThreshld,_p:nbsEfmOamErrFrmEvtTime,_q:nbsEfmOamErrFrmEvtWindow,_r:nbsEfmOamErrFrmEvtThreshld,_s:nbsEfmOamErrFrmEvtCount,_t:nbsEfmOamErrFrmPerCfgDuration,_u:nbsEfmOamErrFrmPerCfgThreshld,_v:nbsEfmOamErrFrmPerEvtTime,_w:nbsEfmOamErrFrmPerEvtWindow,_x:nbsEfmOamErrFrmPerEvtThreshld,_y:nbsEfmOamErrFrmPerEvtCount,_z:nbsEfmOamErrFrmSecSumCfgDuration,_A0:nbsEfmOamErrFrmSecSumCfgThreshld,_A1:nbsEfmOamErrFrmSecSumEvtTime,_A2:nbsEfmOamErrFrmSecSumEvtWindow,_A3:nbsEfmOamErrFrmSecSumEvtThreshld,_A4:nbsEfmOamErrFrmSecSumEvtCount,_A5:nbsEfmOamFramesLostDueToOamError,_A6:nbsEfmOamAdminState,_A7:nbsEfmOamOperState,'nbsEfmProduct':nbsEfmProduct,'nbsEfmNc316Nm':nbsEfmNc316Nm,'nbsEfmConformance':nbsEfmConformance,'nbsEfmGroups':nbsEfmGroups,'nbsEfmOamGroup':nbsEfmOamGroup})