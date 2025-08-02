_c='ruckusZDWLANRogueIndex'
_b='ruckusZDWiredStaMacAddr'
_a='ruckusZDWLANStaMacAddr'
_Z='ruckusZDWLANAPEthPortId'
_Y='ruckusZDWLANAPMacAddress'
_X='testing'
_W='ruckusZDWLANAPIfIndex'
_V='ruckusZDWLANAPMac'
_U='ruckusZDWLANVapBSSID'
_T='1/10000'
_S='radio11bg'
_R='ruckusZDWLANAPRadioStatsRadioIndex'
_Q='ruckusZDWLANAPRadioStatsAPMacAddr'
_P='unknown'
_O='ruckusZDWLANAPMacAddr'
_N='ruckusZDWLANIndex'
_M='TruthValue'
_L='DisplayString'
_K='radio11ac'
_J='radio11na'
_I='radio11ng'
_H='radio11a'
_G='down'
_F='up'
_E='OctetString'
_D='RUCKUS-ZD-WLAN-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ruckusZDWLANModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusZDWLANModule')
RuckusAdminStatus,RuckusRadioMode,RuckusRateLimiting,RuckusSSID,RuckusdB=mibBuilder.importSymbols('RUCKUS-TC-MIB','RuckusAdminStatus','RuckusRadioMode','RuckusRateLimiting','RuckusSSID','RuckusdB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'MacAddress','PhysAddress','RowStatus','TextualConvention',_M)
ruckusZDWLANMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,2,2,1))
_RuckusZDWLANObjects_ObjectIdentity=ObjectIdentity
ruckusZDWLANObjects=_RuckusZDWLANObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,2,2,1,1))
_RuckusZDWLANInfo_ObjectIdentity=ObjectIdentity
ruckusZDWLANInfo=_RuckusZDWLANInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,2,2,1,1,1))
_RuckusZDWLANTable_Object=MibTable
ruckusZDWLANTable=_RuckusZDWLANTable_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1))
if mibBuilder.loadTexts:ruckusZDWLANTable.setStatus(_A)
_RuckusZDWLANEntry_Object=MibTableRow
ruckusZDWLANEntry=_RuckusZDWLANEntry_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1))
ruckusZDWLANEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:ruckusZDWLANEntry.setStatus(_A)
_RuckusZDWLANSSID_Type=RuckusSSID
_RuckusZDWLANSSID_Object=MibTableColumn
ruckusZDWLANSSID=_RuckusZDWLANSSID_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,1),_RuckusZDWLANSSID_Type())
ruckusZDWLANSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANSSID.setStatus(_A)
_RuckusZDWLANDescription_Type=DisplayString
_RuckusZDWLANDescription_Object=MibTableColumn
ruckusZDWLANDescription=_RuckusZDWLANDescription_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,2),_RuckusZDWLANDescription_Type())
ruckusZDWLANDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANDescription.setStatus(_A)
_RuckusZDWLANAuthentication_Type=DisplayString
_RuckusZDWLANAuthentication_Object=MibTableColumn
ruckusZDWLANAuthentication=_RuckusZDWLANAuthentication_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,3),_RuckusZDWLANAuthentication_Type())
ruckusZDWLANAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAuthentication.setStatus(_A)
_RuckusZDWLANEncryption_Type=DisplayString
_RuckusZDWLANEncryption_Object=MibTableColumn
ruckusZDWLANEncryption=_RuckusZDWLANEncryption_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,4),_RuckusZDWLANEncryption_Type())
ruckusZDWLANEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANEncryption.setStatus(_A)
_RuckusZDWLANIsGuest_Type=TruthValue
_RuckusZDWLANIsGuest_Object=MibTableColumn
ruckusZDWLANIsGuest=_RuckusZDWLANIsGuest_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,5),_RuckusZDWLANIsGuest_Type())
ruckusZDWLANIsGuest.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANIsGuest.setStatus(_A)
_RuckusZDWLANSSIDBcastDisable_Type=TruthValue
_RuckusZDWLANSSIDBcastDisable_Object=MibTableColumn
ruckusZDWLANSSIDBcastDisable=_RuckusZDWLANSSIDBcastDisable_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,6),_RuckusZDWLANSSIDBcastDisable_Type())
ruckusZDWLANSSIDBcastDisable.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANSSIDBcastDisable.setStatus(_A)
class _RuckusZDWLANVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RuckusZDWLANVlanID_Type.__name__=_C
_RuckusZDWLANVlanID_Object=MibTableColumn
ruckusZDWLANVlanID=_RuckusZDWLANVlanID_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,7),_RuckusZDWLANVlanID_Type())
ruckusZDWLANVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANVlanID.setStatus(_A)
class _RuckusZDWLANRateLimitingUp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_RuckusZDWLANRateLimitingUp_Type.__name__=_E
_RuckusZDWLANRateLimitingUp_Object=MibTableColumn
ruckusZDWLANRateLimitingUp=_RuckusZDWLANRateLimitingUp_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,8),_RuckusZDWLANRateLimitingUp_Type())
ruckusZDWLANRateLimitingUp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANRateLimitingUp.setStatus(_A)
class _RuckusZDWLANRateLimitingDown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_RuckusZDWLANRateLimitingDown_Type.__name__=_E
_RuckusZDWLANRateLimitingDown_Object=MibTableColumn
ruckusZDWLANRateLimitingDown=_RuckusZDWLANRateLimitingDown_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,9),_RuckusZDWLANRateLimitingDown_Type())
ruckusZDWLANRateLimitingDown.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANRateLimitingDown.setStatus(_A)
_RuckusZDWLANTunnelWLAN_Type=TruthValue
_RuckusZDWLANTunnelWLAN_Object=MibTableColumn
ruckusZDWLANTunnelWLAN=_RuckusZDWLANTunnelWLAN_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,10),_RuckusZDWLANTunnelWLAN_Type())
ruckusZDWLANTunnelWLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANTunnelWLAN.setStatus(_A)
_RuckusZDWLANNumVAP_Type=Unsigned32
_RuckusZDWLANNumVAP_Object=MibTableColumn
ruckusZDWLANNumVAP=_RuckusZDWLANNumVAP_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,11),_RuckusZDWLANNumVAP_Type())
ruckusZDWLANNumVAP.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANNumVAP.setStatus(_A)
_RuckusZDWLANNumSta_Type=Unsigned32
_RuckusZDWLANNumSta_Object=MibTableColumn
ruckusZDWLANNumSta=_RuckusZDWLANNumSta_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,12),_RuckusZDWLANNumSta_Type())
ruckusZDWLANNumSta.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANNumSta.setStatus(_A)
_RuckusZDWLANRxPkts_Type=Counter64
_RuckusZDWLANRxPkts_Object=MibTableColumn
ruckusZDWLANRxPkts=_RuckusZDWLANRxPkts_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,13),_RuckusZDWLANRxPkts_Type())
ruckusZDWLANRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANRxPkts.setStatus(_A)
_RuckusZDWLANRxBytes_Type=Counter64
_RuckusZDWLANRxBytes_Object=MibTableColumn
ruckusZDWLANRxBytes=_RuckusZDWLANRxBytes_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,14),_RuckusZDWLANRxBytes_Type())
ruckusZDWLANRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANRxBytes.setStatus(_A)
_RuckusZDWLANTxPkts_Type=Counter64
_RuckusZDWLANTxPkts_Object=MibTableColumn
ruckusZDWLANTxPkts=_RuckusZDWLANTxPkts_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,15),_RuckusZDWLANTxPkts_Type())
ruckusZDWLANTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANTxPkts.setStatus(_A)
_RuckusZDWLANTxBytes_Type=Counter64
_RuckusZDWLANTxBytes_Object=MibTableColumn
ruckusZDWLANTxBytes=_RuckusZDWLANTxBytes_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,16),_RuckusZDWLANTxBytes_Type())
ruckusZDWLANTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANTxBytes.setStatus(_A)
_RuckusZDWLANAssocNumSta_Type=Unsigned32
_RuckusZDWLANAssocNumSta_Object=MibTableColumn
ruckusZDWLANAssocNumSta=_RuckusZDWLANAssocNumSta_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,20),_RuckusZDWLANAssocNumSta_Type())
ruckusZDWLANAssocNumSta.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAssocNumSta.setStatus(_A)
_RuckusZDWLANAuthTotal_Type=Counter64
_RuckusZDWLANAuthTotal_Object=MibTableColumn
ruckusZDWLANAuthTotal=_RuckusZDWLANAuthTotal_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,26),_RuckusZDWLANAuthTotal_Type())
ruckusZDWLANAuthTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAuthTotal.setStatus(_A)
_RuckusZDWLANAuthResp_Type=Counter64
_RuckusZDWLANAuthResp_Object=MibTableColumn
ruckusZDWLANAuthResp=_RuckusZDWLANAuthResp_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,27),_RuckusZDWLANAuthResp_Type())
ruckusZDWLANAuthResp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAuthResp.setStatus(_A)
_RuckusZDWLANAuthSuccessTotal_Type=Counter64
_RuckusZDWLANAuthSuccessTotal_Object=MibTableColumn
ruckusZDWLANAuthSuccessTotal=_RuckusZDWLANAuthSuccessTotal_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,28),_RuckusZDWLANAuthSuccessTotal_Type())
ruckusZDWLANAuthSuccessTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAuthSuccessTotal.setStatus(_A)
_RuckusZDWLANAuthFail_Type=Counter64
_RuckusZDWLANAuthFail_Object=MibTableColumn
ruckusZDWLANAuthFail=_RuckusZDWLANAuthFail_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,29),_RuckusZDWLANAuthFail_Type())
ruckusZDWLANAuthFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAuthFail.setStatus(_A)
_RuckusZDWLANAssocTotal_Type=Counter64
_RuckusZDWLANAssocTotal_Object=MibTableColumn
ruckusZDWLANAssocTotal=_RuckusZDWLANAssocTotal_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,30),_RuckusZDWLANAssocTotal_Type())
ruckusZDWLANAssocTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAssocTotal.setStatus(_A)
_RuckusZDWLANAssocResp_Type=Counter64
_RuckusZDWLANAssocResp_Object=MibTableColumn
ruckusZDWLANAssocResp=_RuckusZDWLANAssocResp_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,31),_RuckusZDWLANAssocResp_Type())
ruckusZDWLANAssocResp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAssocResp.setStatus(_A)
_RuckusZDWLANReassocReq_Type=Counter64
_RuckusZDWLANReassocReq_Object=MibTableColumn
ruckusZDWLANReassocReq=_RuckusZDWLANReassocReq_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,32),_RuckusZDWLANReassocReq_Type())
ruckusZDWLANReassocReq.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANReassocReq.setStatus(_A)
_RuckusZDWLANReassocResp_Type=Counter64
_RuckusZDWLANReassocResp_Object=MibTableColumn
ruckusZDWLANReassocResp=_RuckusZDWLANReassocResp_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,33),_RuckusZDWLANReassocResp_Type())
ruckusZDWLANReassocResp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANReassocResp.setStatus(_A)
_RuckusZDWLANAssocSuccess_Type=Counter64
_RuckusZDWLANAssocSuccess_Object=MibTableColumn
ruckusZDWLANAssocSuccess=_RuckusZDWLANAssocSuccess_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,34),_RuckusZDWLANAssocSuccess_Type())
ruckusZDWLANAssocSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAssocSuccess.setStatus(_A)
_RuckusZDWLANAssocFail_Type=Counter64
_RuckusZDWLANAssocFail_Object=MibTableColumn
ruckusZDWLANAssocFail=_RuckusZDWLANAssocFail_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,35),_RuckusZDWLANAssocFail_Type())
ruckusZDWLANAssocFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAssocFail.setStatus(_A)
_RuckusZDWLANAssocDenied_Type=Counter64
_RuckusZDWLANAssocDenied_Object=MibTableColumn
ruckusZDWLANAssocDenied=_RuckusZDWLANAssocDenied_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,36),_RuckusZDWLANAssocDenied_Type())
ruckusZDWLANAssocDenied.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAssocDenied.setStatus(_A)
_RuckusZDWLANDiassocAbnormal_Type=Counter64
_RuckusZDWLANDiassocAbnormal_Object=MibTableColumn
ruckusZDWLANDiassocAbnormal=_RuckusZDWLANDiassocAbnormal_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,37),_RuckusZDWLANDiassocAbnormal_Type())
ruckusZDWLANDiassocAbnormal.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANDiassocAbnormal.setStatus(_A)
_RuckusZDWLANDiassocCapacity_Type=Counter64
_RuckusZDWLANDiassocCapacity_Object=MibTableColumn
ruckusZDWLANDiassocCapacity=_RuckusZDWLANDiassocCapacity_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,38),_RuckusZDWLANDiassocCapacity_Type())
ruckusZDWLANDiassocCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANDiassocCapacity.setStatus(_A)
_RuckusZDWLANDiassocLeave_Type=Counter64
_RuckusZDWLANDiassocLeave_Object=MibTableColumn
ruckusZDWLANDiassocLeave=_RuckusZDWLANDiassocLeave_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,39),_RuckusZDWLANDiassocLeave_Type())
ruckusZDWLANDiassocLeave.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANDiassocLeave.setStatus(_A)
_RuckusZDWLANDiassocMisc_Type=Counter64
_RuckusZDWLANDiassocMisc_Object=MibTableColumn
ruckusZDWLANDiassocMisc=_RuckusZDWLANDiassocMisc_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,40),_RuckusZDWLANDiassocMisc_Type())
ruckusZDWLANDiassocMisc.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANDiassocMisc.setStatus(_A)
_RuckusZDWLANRxByteRate_Type=Unsigned32
_RuckusZDWLANRxByteRate_Object=MibTableColumn
ruckusZDWLANRxByteRate=_RuckusZDWLANRxByteRate_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,41),_RuckusZDWLANRxByteRate_Type())
ruckusZDWLANRxByteRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANRxByteRate.setStatus(_A)
_RuckusZDWLANTxByteRate_Type=Unsigned32
_RuckusZDWLANTxByteRate_Object=MibTableColumn
ruckusZDWLANTxByteRate=_RuckusZDWLANTxByteRate_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,42),_RuckusZDWLANTxByteRate_Type())
ruckusZDWLANTxByteRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANTxByteRate.setStatus(_A)
_RuckusZDWLANRxDataFrameOnLan_Type=Counter64
_RuckusZDWLANRxDataFrameOnLan_Object=MibTableColumn
ruckusZDWLANRxDataFrameOnLan=_RuckusZDWLANRxDataFrameOnLan_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,43),_RuckusZDWLANRxDataFrameOnLan_Type())
ruckusZDWLANRxDataFrameOnLan.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANRxDataFrameOnLan.setStatus(_A)
_RuckusZDWLANRxByteOnLan_Type=Counter64
_RuckusZDWLANRxByteOnLan_Object=MibTableColumn
ruckusZDWLANRxByteOnLan=_RuckusZDWLANRxByteOnLan_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,44),_RuckusZDWLANRxByteOnLan_Type())
ruckusZDWLANRxByteOnLan.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANRxByteOnLan.setStatus(_A)
_RuckusZDWLANTxByteOnLan_Type=Counter64
_RuckusZDWLANTxByteOnLan_Object=MibTableColumn
ruckusZDWLANTxByteOnLan=_RuckusZDWLANTxByteOnLan_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,45),_RuckusZDWLANTxByteOnLan_Type())
ruckusZDWLANTxByteOnLan.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANTxByteOnLan.setStatus(_A)
_RuckusZDWLANDownDropFrame_Type=Counter64
_RuckusZDWLANDownDropFrame_Object=MibTableColumn
ruckusZDWLANDownDropFrame=_RuckusZDWLANDownDropFrame_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,46),_RuckusZDWLANDownDropFrame_Type())
ruckusZDWLANDownDropFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANDownDropFrame.setStatus(_A)
_RuckusZDWLANDownRetxFrame_Type=Counter64
_RuckusZDWLANDownRetxFrame_Object=MibTableColumn
ruckusZDWLANDownRetxFrame=_RuckusZDWLANDownRetxFrame_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,47),_RuckusZDWLANDownRetxFrame_Type())
ruckusZDWLANDownRetxFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANDownRetxFrame.setStatus(_A)
_RuckusZDWLANDownTotalFrame_Type=Counter64
_RuckusZDWLANDownTotalFrame_Object=MibTableColumn
ruckusZDWLANDownTotalFrame=_RuckusZDWLANDownTotalFrame_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,48),_RuckusZDWLANDownTotalFrame_Type())
ruckusZDWLANDownTotalFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANDownTotalFrame.setStatus(_A)
_RuckusZDWLANDownTotalErrFrame_Type=Counter64
_RuckusZDWLANDownTotalErrFrame_Object=MibTableColumn
ruckusZDWLANDownTotalErrFrame=_RuckusZDWLANDownTotalErrFrame_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,49),_RuckusZDWLANDownTotalErrFrame_Type())
ruckusZDWLANDownTotalErrFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANDownTotalErrFrame.setStatus(_A)
_RuckusZDWLANUpTotalFrame_Type=Counter64
_RuckusZDWLANUpTotalFrame_Object=MibTableColumn
ruckusZDWLANUpTotalFrame=_RuckusZDWLANUpTotalFrame_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,50),_RuckusZDWLANUpTotalFrame_Type())
ruckusZDWLANUpTotalFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANUpTotalFrame.setStatus(_A)
_RuckusZDWLANUpDropFrame_Type=Counter64
_RuckusZDWLANUpDropFrame_Object=MibTableColumn
ruckusZDWLANUpDropFrame=_RuckusZDWLANUpDropFrame_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,51),_RuckusZDWLANUpDropFrame_Type())
ruckusZDWLANUpDropFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANUpDropFrame.setStatus(_A)
_RuckusZDWLANUpRetxFrame_Type=Counter64
_RuckusZDWLANUpRetxFrame_Object=MibTableColumn
ruckusZDWLANUpRetxFrame=_RuckusZDWLANUpRetxFrame_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,52),_RuckusZDWLANUpRetxFrame_Type())
ruckusZDWLANUpRetxFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANUpRetxFrame.setStatus(_A)
_RuckusZDWLANNAME_Type=RuckusSSID
_RuckusZDWLANNAME_Object=MibTableColumn
ruckusZDWLANNAME=_RuckusZDWLANNAME_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,108),_RuckusZDWLANNAME_Type())
ruckusZDWLANNAME.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANNAME.setStatus(_A)
_RuckusZDWLANIndex_Type=InterfaceIndex
_RuckusZDWLANIndex_Object=MibTableColumn
ruckusZDWLANIndex=_RuckusZDWLANIndex_Object((1,3,6,1,4,1,25053,1,2,2,1,1,1,1,1,200),_RuckusZDWLANIndex_Type())
ruckusZDWLANIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANIndex.setStatus(_A)
_RuckusZDWLANAPInfo_ObjectIdentity=ObjectIdentity
ruckusZDWLANAPInfo=_RuckusZDWLANAPInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,2,2,1,1,2))
_RuckusZDWLANAPTable_Object=MibTable
ruckusZDWLANAPTable=_RuckusZDWLANAPTable_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1))
if mibBuilder.loadTexts:ruckusZDWLANAPTable.setStatus(_A)
_RuckusZDWLANAPEntry_Object=MibTableRow
ruckusZDWLANAPEntry=_RuckusZDWLANAPEntry_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1))
ruckusZDWLANAPEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:ruckusZDWLANAPEntry.setStatus(_A)
_RuckusZDWLANAPMacAddr_Type=MacAddress
_RuckusZDWLANAPMacAddr_Object=MibTableColumn
ruckusZDWLANAPMacAddr=_RuckusZDWLANAPMacAddr_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,1),_RuckusZDWLANAPMacAddr_Type())
ruckusZDWLANAPMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPMacAddr.setStatus(_A)
_RuckusZDWLANAPDescription_Type=DisplayString
_RuckusZDWLANAPDescription_Object=MibTableColumn
ruckusZDWLANAPDescription=_RuckusZDWLANAPDescription_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,2),_RuckusZDWLANAPDescription_Type())
ruckusZDWLANAPDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPDescription.setStatus(_A)
class _RuckusZDWLANAPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('disconnected',0),('connected',1),('approvalPending',2),('upgradingFirmware',3),('provisioning',4)))
_RuckusZDWLANAPStatus_Type.__name__=_C
_RuckusZDWLANAPStatus_Object=MibTableColumn
ruckusZDWLANAPStatus=_RuckusZDWLANAPStatus_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,3),_RuckusZDWLANAPStatus_Type())
ruckusZDWLANAPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPStatus.setStatus(_A)
_RuckusZDWLANAPModel_Type=DisplayString
_RuckusZDWLANAPModel_Object=MibTableColumn
ruckusZDWLANAPModel=_RuckusZDWLANAPModel_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,4),_RuckusZDWLANAPModel_Type())
ruckusZDWLANAPModel.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPModel.setStatus(_A)
_RuckusZDWLANAPSerialNumber_Type=DisplayString
_RuckusZDWLANAPSerialNumber_Object=MibTableColumn
ruckusZDWLANAPSerialNumber=_RuckusZDWLANAPSerialNumber_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,5),_RuckusZDWLANAPSerialNumber_Type())
ruckusZDWLANAPSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPSerialNumber.setStatus(_A)
_RuckusZDWLANAPUptime_Type=TimeTicks
_RuckusZDWLANAPUptime_Object=MibTableColumn
ruckusZDWLANAPUptime=_RuckusZDWLANAPUptime_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,6),_RuckusZDWLANAPUptime_Type())
ruckusZDWLANAPUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPUptime.setStatus(_A)
_RuckusZDWLANAPSWversion_Type=DisplayString
_RuckusZDWLANAPSWversion_Object=MibTableColumn
ruckusZDWLANAPSWversion=_RuckusZDWLANAPSWversion_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,7),_RuckusZDWLANAPSWversion_Type())
ruckusZDWLANAPSWversion.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPSWversion.setStatus(_A)
_RuckusZDWLANAPHWversion_Type=DisplayString
_RuckusZDWLANAPHWversion_Object=MibTableColumn
ruckusZDWLANAPHWversion=_RuckusZDWLANAPHWversion_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,8),_RuckusZDWLANAPHWversion_Type())
ruckusZDWLANAPHWversion.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPHWversion.setStatus(_A)
_RuckusZDWLANAPIPAddr_Type=IpAddress
_RuckusZDWLANAPIPAddr_Object=MibTableColumn
ruckusZDWLANAPIPAddr=_RuckusZDWLANAPIPAddr_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,10),_RuckusZDWLANAPIPAddr_Type())
ruckusZDWLANAPIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIPAddr.setStatus(_A)
_RuckusZDWLANAPNumRadios_Type=Unsigned32
_RuckusZDWLANAPNumRadios_Object=MibTableColumn
ruckusZDWLANAPNumRadios=_RuckusZDWLANAPNumRadios_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,13),_RuckusZDWLANAPNumRadios_Type())
ruckusZDWLANAPNumRadios.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPNumRadios.setStatus(_A)
_RuckusZDWLANAPNumVAP_Type=Unsigned32
_RuckusZDWLANAPNumVAP_Object=MibTableColumn
ruckusZDWLANAPNumVAP=_RuckusZDWLANAPNumVAP_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,14),_RuckusZDWLANAPNumVAP_Type())
ruckusZDWLANAPNumVAP.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPNumVAP.setStatus(_A)
_RuckusZDWLANAPNumSta_Type=Unsigned32
_RuckusZDWLANAPNumSta_Object=MibTableColumn
ruckusZDWLANAPNumSta=_RuckusZDWLANAPNumSta_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,15),_RuckusZDWLANAPNumSta_Type())
ruckusZDWLANAPNumSta.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPNumSta.setStatus(_A)
_RuckusZDWLANAPNumRogues_Type=Unsigned32
_RuckusZDWLANAPNumRogues_Object=MibTableColumn
ruckusZDWLANAPNumRogues=_RuckusZDWLANAPNumRogues_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,16),_RuckusZDWLANAPNumRogues_Type())
ruckusZDWLANAPNumRogues.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPNumRogues.setStatus(_A)
class _RuckusZDWLANAPConnectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('layer2',0),('layer3',1)))
_RuckusZDWLANAPConnectionMode_Type.__name__=_C
_RuckusZDWLANAPConnectionMode_Object=MibTableColumn
ruckusZDWLANAPConnectionMode=_RuckusZDWLANAPConnectionMode_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,17),_RuckusZDWLANAPConnectionMode_Type())
ruckusZDWLANAPConnectionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPConnectionMode.setStatus(_A)
_RuckusZDWLANAPMeshEnable_Type=TruthValue
_RuckusZDWLANAPMeshEnable_Object=MibTableColumn
ruckusZDWLANAPMeshEnable=_RuckusZDWLANAPMeshEnable_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,18),_RuckusZDWLANAPMeshEnable_Type())
ruckusZDWLANAPMeshEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPMeshEnable.setStatus(_A)
_RuckusZDWLANAPMeshHops_Type=Unsigned32
_RuckusZDWLANAPMeshHops_Object=MibTableColumn
ruckusZDWLANAPMeshHops=_RuckusZDWLANAPMeshHops_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,19),_RuckusZDWLANAPMeshHops_Type())
ruckusZDWLANAPMeshHops.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPMeshHops.setStatus(_A)
class _RuckusZDWLANAPMeshType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_P,0),('root',1),('mesh',2),('forming',3)))
_RuckusZDWLANAPMeshType_Type.__name__=_C
_RuckusZDWLANAPMeshType_Object=MibTableColumn
ruckusZDWLANAPMeshType=_RuckusZDWLANAPMeshType_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,20),_RuckusZDWLANAPMeshType_Type())
ruckusZDWLANAPMeshType.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPMeshType.setStatus(_A)
_RuckusZDWLANAPLANStatsRXByte_Type=Counter64
_RuckusZDWLANAPLANStatsRXByte_Object=MibTableColumn
ruckusZDWLANAPLANStatsRXByte=_RuckusZDWLANAPLANStatsRXByte_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,21),_RuckusZDWLANAPLANStatsRXByte_Type())
ruckusZDWLANAPLANStatsRXByte.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLANStatsRXByte.setStatus(_A)
_RuckusZDWLANAPLANStatsRXPkt_Type=Counter64
_RuckusZDWLANAPLANStatsRXPkt_Object=MibTableColumn
ruckusZDWLANAPLANStatsRXPkt=_RuckusZDWLANAPLANStatsRXPkt_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,22),_RuckusZDWLANAPLANStatsRXPkt_Type())
ruckusZDWLANAPLANStatsRXPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLANStatsRXPkt.setStatus(_A)
_RuckusZDWLANAPLANStatsRXPktErr_Type=Counter64
_RuckusZDWLANAPLANStatsRXPktErr_Object=MibTableColumn
ruckusZDWLANAPLANStatsRXPktErr=_RuckusZDWLANAPLANStatsRXPktErr_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,23),_RuckusZDWLANAPLANStatsRXPktErr_Type())
ruckusZDWLANAPLANStatsRXPktErr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLANStatsRXPktErr.setStatus(_A)
_RuckusZDWLANAPLANStatsRXPKTSucc_Type=Counter64
_RuckusZDWLANAPLANStatsRXPKTSucc_Object=MibTableColumn
ruckusZDWLANAPLANStatsRXPKTSucc=_RuckusZDWLANAPLANStatsRXPKTSucc_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,24),_RuckusZDWLANAPLANStatsRXPKTSucc_Type())
ruckusZDWLANAPLANStatsRXPKTSucc.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLANStatsRXPKTSucc.setStatus(_A)
_RuckusZDWLANAPLANStatsTXByte_Type=Counter64
_RuckusZDWLANAPLANStatsTXByte_Object=MibTableColumn
ruckusZDWLANAPLANStatsTXByte=_RuckusZDWLANAPLANStatsTXByte_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,25),_RuckusZDWLANAPLANStatsTXByte_Type())
ruckusZDWLANAPLANStatsTXByte.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLANStatsTXByte.setStatus(_A)
_RuckusZDWLANAPLANStatsTXPkt_Type=Counter64
_RuckusZDWLANAPLANStatsTXPkt_Object=MibTableColumn
ruckusZDWLANAPLANStatsTXPkt=_RuckusZDWLANAPLANStatsTXPkt_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,26),_RuckusZDWLANAPLANStatsTXPkt_Type())
ruckusZDWLANAPLANStatsTXPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLANStatsTXPkt.setStatus(_A)
_RuckusZDWLANAPMemUtil_Type=Integer32
_RuckusZDWLANAPMemUtil_Object=MibTableColumn
ruckusZDWLANAPMemUtil=_RuckusZDWLANAPMemUtil_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,27),_RuckusZDWLANAPMemUtil_Type())
ruckusZDWLANAPMemUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPMemUtil.setStatus(_A)
_RuckusZDWLANAPMemTotal_Type=Unsigned32
_RuckusZDWLANAPMemTotal_Object=MibTableColumn
ruckusZDWLANAPMemTotal=_RuckusZDWLANAPMemTotal_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,28),_RuckusZDWLANAPMemTotal_Type())
ruckusZDWLANAPMemTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPMemTotal.setStatus(_A)
_RuckusZDWLANAPCPUUtil_Type=Integer32
_RuckusZDWLANAPCPUUtil_Object=MibTableColumn
ruckusZDWLANAPCPUUtil=_RuckusZDWLANAPCPUUtil_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,29),_RuckusZDWLANAPCPUUtil_Type())
ruckusZDWLANAPCPUUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPCPUUtil.setStatus(_A)
_RuckusZDWLANAPFWSize_Type=Unsigned32
_RuckusZDWLANAPFWSize_Object=MibTableColumn
ruckusZDWLANAPFWSize=_RuckusZDWLANAPFWSize_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,30),_RuckusZDWLANAPFWSize_Type())
ruckusZDWLANAPFWSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPFWSize.setStatus(_A)
_RuckusZDWLANAPFWAvail_Type=Unsigned32
_RuckusZDWLANAPFWAvail_Object=MibTableColumn
ruckusZDWLANAPFWAvail=_RuckusZDWLANAPFWAvail_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,31),_RuckusZDWLANAPFWAvail_Type())
ruckusZDWLANAPFWAvail.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPFWAvail.setStatus(_A)
_RuckusZDWLANAPMultipleVlanCapability_Type=TruthValue
_RuckusZDWLANAPMultipleVlanCapability_Object=MibTableColumn
ruckusZDWLANAPMultipleVlanCapability=_RuckusZDWLANAPMultipleVlanCapability_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,32),_RuckusZDWLANAPMultipleVlanCapability_Type())
ruckusZDWLANAPMultipleVlanCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPMultipleVlanCapability.setStatus(_A)
_RuckusZDWLANAP11bCapable_Type=TruthValue
_RuckusZDWLANAP11bCapable_Object=MibTableColumn
ruckusZDWLANAP11bCapable=_RuckusZDWLANAP11bCapable_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,36),_RuckusZDWLANAP11bCapable_Type())
ruckusZDWLANAP11bCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAP11bCapable.setStatus(_A)
_RuckusZDWLANAP11gCapable_Type=TruthValue
_RuckusZDWLANAP11gCapable_Object=MibTableColumn
ruckusZDWLANAP11gCapable=_RuckusZDWLANAP11gCapable_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,37),_RuckusZDWLANAP11gCapable_Type())
ruckusZDWLANAP11gCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAP11gCapable.setStatus(_A)
class _RuckusZDWLANAPMultiModeAccessStatus_Type(TruthValue):subtypeSpec=TruthValue.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_RuckusZDWLANAPMultiModeAccessStatus_Type.__name__=_M
_RuckusZDWLANAPMultiModeAccessStatus_Object=MibTableColumn
ruckusZDWLANAPMultiModeAccessStatus=_RuckusZDWLANAPMultiModeAccessStatus_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,38),_RuckusZDWLANAPMultiModeAccessStatus_Type())
ruckusZDWLANAPMultiModeAccessStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPMultiModeAccessStatus.setStatus(_A)
_RuckusZDWLANAPEthStateChange_Type=Counter32
_RuckusZDWLANAPEthStateChange_Object=MibTableColumn
ruckusZDWLANAPEthStateChange=_RuckusZDWLANAPEthStateChange_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,39),_RuckusZDWLANAPEthStateChange_Type())
ruckusZDWLANAPEthStateChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPEthStateChange.setStatus(_A)
_RuckusZDWLANAPSyncConf_Type=TruthValue
_RuckusZDWLANAPSyncConf_Object=MibTableColumn
ruckusZDWLANAPSyncConf=_RuckusZDWLANAPSyncConf_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,41),_RuckusZDWLANAPSyncConf_Type())
ruckusZDWLANAPSyncConf.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPSyncConf.setStatus(_A)
_RuckusZDWLANAPUpgrade_Type=TruthValue
_RuckusZDWLANAPUpgrade_Object=MibTableColumn
ruckusZDWLANAPUpgrade=_RuckusZDWLANAPUpgrade_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,42),_RuckusZDWLANAPUpgrade_Type())
ruckusZDWLANAPUpgrade.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPUpgrade.setStatus(_A)
_RuckusZDWLANAPFirstJoinTime_Type=DisplayString
_RuckusZDWLANAPFirstJoinTime_Object=MibTableColumn
ruckusZDWLANAPFirstJoinTime=_RuckusZDWLANAPFirstJoinTime_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,43),_RuckusZDWLANAPFirstJoinTime_Type())
ruckusZDWLANAPFirstJoinTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPFirstJoinTime.setStatus(_A)
_RuckusZDWLANAPLastBootTime_Type=DisplayString
_RuckusZDWLANAPLastBootTime_Object=MibTableColumn
ruckusZDWLANAPLastBootTime=_RuckusZDWLANAPLastBootTime_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,44),_RuckusZDWLANAPLastBootTime_Type())
ruckusZDWLANAPLastBootTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLastBootTime.setStatus(_A)
_RuckusZDWLANAPLastUpgradeTime_Type=DisplayString
_RuckusZDWLANAPLastUpgradeTime_Object=MibTableColumn
ruckusZDWLANAPLastUpgradeTime=_RuckusZDWLANAPLastUpgradeTime_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,45),_RuckusZDWLANAPLastUpgradeTime_Type())
ruckusZDWLANAPLastUpgradeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLastUpgradeTime.setStatus(_A)
_RuckusZDWLANAPLastConfSyncTime_Type=DisplayString
_RuckusZDWLANAPLastConfSyncTime_Object=MibTableColumn
ruckusZDWLANAPLastConfSyncTime=_RuckusZDWLANAPLastConfSyncTime_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,46),_RuckusZDWLANAPLastConfSyncTime_Type())
ruckusZDWLANAPLastConfSyncTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLastConfSyncTime.setStatus(_A)
_RuckusZDWLANAPLANStatsRXPKTBcast_Type=Counter64
_RuckusZDWLANAPLANStatsRXPKTBcast_Object=MibTableColumn
ruckusZDWLANAPLANStatsRXPKTBcast=_RuckusZDWLANAPLANStatsRXPKTBcast_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,47),_RuckusZDWLANAPLANStatsRXPKTBcast_Type())
ruckusZDWLANAPLANStatsRXPKTBcast.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLANStatsRXPKTBcast.setStatus(_A)
_RuckusZDWLANAPLANStatsRXPKTMcast_Type=Counter64
_RuckusZDWLANAPLANStatsRXPKTMcast_Object=MibTableColumn
ruckusZDWLANAPLANStatsRXPKTMcast=_RuckusZDWLANAPLANStatsRXPKTMcast_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,48),_RuckusZDWLANAPLANStatsRXPKTMcast_Type())
ruckusZDWLANAPLANStatsRXPKTMcast.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLANStatsRXPKTMcast.setStatus(_A)
_RuckusZDWLANAPLANStatsRXPKTUcast_Type=Counter64
_RuckusZDWLANAPLANStatsRXPKTUcast_Object=MibTableColumn
ruckusZDWLANAPLANStatsRXPKTUcast=_RuckusZDWLANAPLANStatsRXPKTUcast_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,49),_RuckusZDWLANAPLANStatsRXPKTUcast_Type())
ruckusZDWLANAPLANStatsRXPKTUcast.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLANStatsRXPKTUcast.setStatus(_A)
_RuckusZDWLANAPLANStatsTXPKTBcast_Type=Counter64
_RuckusZDWLANAPLANStatsTXPKTBcast_Object=MibTableColumn
ruckusZDWLANAPLANStatsTXPKTBcast=_RuckusZDWLANAPLANStatsTXPKTBcast_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,50),_RuckusZDWLANAPLANStatsTXPKTBcast_Type())
ruckusZDWLANAPLANStatsTXPKTBcast.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLANStatsTXPKTBcast.setStatus(_A)
_RuckusZDWLANAPLANStatsTXPKTMcast_Type=Counter64
_RuckusZDWLANAPLANStatsTXPKTMcast_Object=MibTableColumn
ruckusZDWLANAPLANStatsTXPKTMcast=_RuckusZDWLANAPLANStatsTXPKTMcast_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,51),_RuckusZDWLANAPLANStatsTXPKTMcast_Type())
ruckusZDWLANAPLANStatsTXPKTMcast.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLANStatsTXPKTMcast.setStatus(_A)
_RuckusZDWLANAPLANStatsTXPKTUcast_Type=Counter64
_RuckusZDWLANAPLANStatsTXPKTUcast_Object=MibTableColumn
ruckusZDWLANAPLANStatsTXPKTUcast=_RuckusZDWLANAPLANStatsTXPKTUcast_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,52),_RuckusZDWLANAPLANStatsTXPKTUcast_Type())
ruckusZDWLANAPLANStatsTXPKTUcast.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLANStatsTXPKTUcast.setStatus(_A)
_RuckusZDWLANAPLANStatsDropped_Type=Counter64
_RuckusZDWLANAPLANStatsDropped_Object=MibTableColumn
ruckusZDWLANAPLANStatsDropped=_RuckusZDWLANAPLANStatsDropped_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,53),_RuckusZDWLANAPLANStatsDropped_Type())
ruckusZDWLANAPLANStatsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLANStatsDropped.setStatus(_A)
_RuckusZDWLANAPMeshUpPortCntUpdown_Type=Counter32
_RuckusZDWLANAPMeshUpPortCntUpdown_Object=MibTableColumn
ruckusZDWLANAPMeshUpPortCntUpdown=_RuckusZDWLANAPMeshUpPortCntUpdown_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,54),_RuckusZDWLANAPMeshUpPortCntUpdown_Type())
ruckusZDWLANAPMeshUpPortCntUpdown.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPMeshUpPortCntUpdown.setStatus(_A)
_RuckusZDWLANAPMeshDownPortCntUpdown_Type=Counter32
_RuckusZDWLANAPMeshDownPortCntUpdown_Object=MibTableColumn
ruckusZDWLANAPMeshDownPortCntUpdown=_RuckusZDWLANAPMeshDownPortCntUpdown_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,55),_RuckusZDWLANAPMeshDownPortCntUpdown_Type())
ruckusZDWLANAPMeshDownPortCntUpdown.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPMeshDownPortCntUpdown.setStatus(_A)
_RuckusZDWLANAPTxFrameDropped_Type=Counter32
_RuckusZDWLANAPTxFrameDropped_Object=MibTableColumn
ruckusZDWLANAPTxFrameDropped=_RuckusZDWLANAPTxFrameDropped_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,57),_RuckusZDWLANAPTxFrameDropped_Type())
ruckusZDWLANAPTxFrameDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPTxFrameDropped.setStatus(_A)
_RuckusZDWLANAPTxFrameError_Type=Counter32
_RuckusZDWLANAPTxFrameError_Object=MibTableColumn
ruckusZDWLANAPTxFrameError=_RuckusZDWLANAPTxFrameError_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,58),_RuckusZDWLANAPTxFrameError_Type())
ruckusZDWLANAPTxFrameError.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPTxFrameError.setStatus(_A)
class _RuckusZDWLANAPCoverageTech_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('indoor',1),('indoor-distribute',2),('outdoor',3)))
_RuckusZDWLANAPCoverageTech_Type.__name__=_C
_RuckusZDWLANAPCoverageTech_Object=MibTableColumn
ruckusZDWLANAPCoverageTech=_RuckusZDWLANAPCoverageTech_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,59),_RuckusZDWLANAPCoverageTech_Type())
ruckusZDWLANAPCoverageTech.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPCoverageTech.setStatus(_A)
_RuckusZDWLANAPStaTxBytes_Type=Counter64
_RuckusZDWLANAPStaTxBytes_Object=MibTableColumn
ruckusZDWLANAPStaTxBytes=_RuckusZDWLANAPStaTxBytes_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,61),_RuckusZDWLANAPStaTxBytes_Type())
ruckusZDWLANAPStaTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPStaTxBytes.setStatus(_A)
_RuckusZDWLANAPStaRxBytes_Type=Counter64
_RuckusZDWLANAPStaRxBytes_Object=MibTableColumn
ruckusZDWLANAPStaRxBytes=_RuckusZDWLANAPStaRxBytes_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,62),_RuckusZDWLANAPStaRxBytes_Type())
ruckusZDWLANAPStaRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPStaRxBytes.setStatus(_A)
_RuckusZDWLANAPNetmask_Type=IpAddress
_RuckusZDWLANAPNetmask_Object=MibTableColumn
ruckusZDWLANAPNetmask=_RuckusZDWLANAPNetmask_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,100),_RuckusZDWLANAPNetmask_Type())
ruckusZDWLANAPNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPNetmask.setStatus(_A)
_RuckusZDWLANAPGateway_Type=IpAddress
_RuckusZDWLANAPGateway_Object=MibTableColumn
ruckusZDWLANAPGateway=_RuckusZDWLANAPGateway_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,101),_RuckusZDWLANAPGateway_Type())
ruckusZDWLANAPGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPGateway.setStatus(_A)
_RuckusZDWLANAPDNS1_Type=IpAddress
_RuckusZDWLANAPDNS1_Object=MibTableColumn
ruckusZDWLANAPDNS1=_RuckusZDWLANAPDNS1_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,105),_RuckusZDWLANAPDNS1_Type())
ruckusZDWLANAPDNS1.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPDNS1.setStatus(_A)
_RuckusZDWLANAPDNS2_Type=IpAddress
_RuckusZDWLANAPDNS2_Object=MibTableColumn
ruckusZDWLANAPDNS2=_RuckusZDWLANAPDNS2_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,106),_RuckusZDWLANAPDNS2_Type())
ruckusZDWLANAPDNS2.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPDNS2.setStatus(_A)
_RuckusZDWLANAPTotalUser_Type=Unsigned32
_RuckusZDWLANAPTotalUser_Object=MibTableColumn
ruckusZDWLANAPTotalUser=_RuckusZDWLANAPTotalUser_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,110),_RuckusZDWLANAPTotalUser_Type())
ruckusZDWLANAPTotalUser.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPTotalUser.setStatus(_A)
_RuckusZDWLANAPLANStatsRXByteRate_Type=Counter32
_RuckusZDWLANAPLANStatsRXByteRate_Object=MibTableColumn
ruckusZDWLANAPLANStatsRXByteRate=_RuckusZDWLANAPLANStatsRXByteRate_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,111),_RuckusZDWLANAPLANStatsRXByteRate_Type())
ruckusZDWLANAPLANStatsRXByteRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLANStatsRXByteRate.setStatus(_A)
_RuckusZDWLANAPLANStatsTXByteRate_Type=Counter32
_RuckusZDWLANAPLANStatsTXByteRate_Object=MibTableColumn
ruckusZDWLANAPLANStatsTXByteRate=_RuckusZDWLANAPLANStatsTXByteRate_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,1,1,112),_RuckusZDWLANAPLANStatsTXByteRate_Type())
ruckusZDWLANAPLANStatsTXByteRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPLANStatsTXByteRate.setStatus(_A)
_RuckusZDWLANAPRadioStatsTable_Object=MibTable
ruckusZDWLANAPRadioStatsTable=_RuckusZDWLANAPRadioStatsTable_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2))
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsTable.setStatus(_A)
_RuckusZDWLANAPRadioStatsEntry_Object=MibTableRow
ruckusZDWLANAPRadioStatsEntry=_RuckusZDWLANAPRadioStatsEntry_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1))
ruckusZDWLANAPRadioStatsEntry.setIndexNames((0,_D,_Q),(0,_D,_R))
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsEntry.setStatus(_A)
_RuckusZDWLANAPRadioStatsAPMacAddr_Type=MacAddress
_RuckusZDWLANAPRadioStatsAPMacAddr_Object=MibTableColumn
ruckusZDWLANAPRadioStatsAPMacAddr=_RuckusZDWLANAPRadioStatsAPMacAddr_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,1),_RuckusZDWLANAPRadioStatsAPMacAddr_Type())
ruckusZDWLANAPRadioStatsAPMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsAPMacAddr.setStatus(_A)
_RuckusZDWLANAPRadioStatsRadioIndex_Type=Unsigned32
_RuckusZDWLANAPRadioStatsRadioIndex_Object=MibTableColumn
ruckusZDWLANAPRadioStatsRadioIndex=_RuckusZDWLANAPRadioStatsRadioIndex_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,2),_RuckusZDWLANAPRadioStatsRadioIndex_Type())
ruckusZDWLANAPRadioStatsRadioIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsRadioIndex.setStatus(_A)
class _RuckusZDWLANAPRadioStatsRadioType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_S,0),(_H,1),(_I,2),(_J,3),(_K,4)))
_RuckusZDWLANAPRadioStatsRadioType_Type.__name__=_C
_RuckusZDWLANAPRadioStatsRadioType_Object=MibTableColumn
ruckusZDWLANAPRadioStatsRadioType=_RuckusZDWLANAPRadioStatsRadioType_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,3),_RuckusZDWLANAPRadioStatsRadioType_Type())
ruckusZDWLANAPRadioStatsRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsRadioType.setStatus(_A)
_RuckusZDWLANAPRadioStatsChannel_Type=Unsigned32
_RuckusZDWLANAPRadioStatsChannel_Object=MibTableColumn
ruckusZDWLANAPRadioStatsChannel=_RuckusZDWLANAPRadioStatsChannel_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,4),_RuckusZDWLANAPRadioStatsChannel_Type())
ruckusZDWLANAPRadioStatsChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsChannel.setStatus(_A)
class _RuckusZDWLANAPRadioStatsTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('full',0),('half',1),('quarter',2),('eighth',3)))
_RuckusZDWLANAPRadioStatsTxPower_Type.__name__=_C
_RuckusZDWLANAPRadioStatsTxPower_Object=MibTableColumn
ruckusZDWLANAPRadioStatsTxPower=_RuckusZDWLANAPRadioStatsTxPower_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,5),_RuckusZDWLANAPRadioStatsTxPower_Type())
ruckusZDWLANAPRadioStatsTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsTxPower.setStatus(_A)
_RuckusZDWLANAPRadioStatsMeshEnable_Type=TruthValue
_RuckusZDWLANAPRadioStatsMeshEnable_Object=MibTableColumn
ruckusZDWLANAPRadioStatsMeshEnable=_RuckusZDWLANAPRadioStatsMeshEnable_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,6),_RuckusZDWLANAPRadioStatsMeshEnable_Type())
ruckusZDWLANAPRadioStatsMeshEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsMeshEnable.setStatus(_A)
_RuckusZDWLANAPRadioStatsNumVAP_Type=Unsigned32
_RuckusZDWLANAPRadioStatsNumVAP_Object=MibTableColumn
ruckusZDWLANAPRadioStatsNumVAP=_RuckusZDWLANAPRadioStatsNumVAP_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,7),_RuckusZDWLANAPRadioStatsNumVAP_Type())
ruckusZDWLANAPRadioStatsNumVAP.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsNumVAP.setStatus(_A)
_RuckusZDWLANAPRadioStatsNumSta_Type=Unsigned32
_RuckusZDWLANAPRadioStatsNumSta_Object=MibTableColumn
ruckusZDWLANAPRadioStatsNumSta=_RuckusZDWLANAPRadioStatsNumSta_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,8),_RuckusZDWLANAPRadioStatsNumSta_Type())
ruckusZDWLANAPRadioStatsNumSta.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsNumSta.setStatus(_A)
_RuckusZDWLANAPRadioStatsAvgStaRSSI_Type=Integer32
_RuckusZDWLANAPRadioStatsAvgStaRSSI_Object=MibTableColumn
ruckusZDWLANAPRadioStatsAvgStaRSSI=_RuckusZDWLANAPRadioStatsAvgStaRSSI_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,9),_RuckusZDWLANAPRadioStatsAvgStaRSSI_Type())
ruckusZDWLANAPRadioStatsAvgStaRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsAvgStaRSSI.setStatus(_A)
_RuckusZDWLANAPRadioStatsRxPkts_Type=Counter64
_RuckusZDWLANAPRadioStatsRxPkts_Object=MibTableColumn
ruckusZDWLANAPRadioStatsRxPkts=_RuckusZDWLANAPRadioStatsRxPkts_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,10),_RuckusZDWLANAPRadioStatsRxPkts_Type())
ruckusZDWLANAPRadioStatsRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsRxPkts.setStatus(_A)
_RuckusZDWLANAPRadioStatsRxBytes_Type=Counter64
_RuckusZDWLANAPRadioStatsRxBytes_Object=MibTableColumn
ruckusZDWLANAPRadioStatsRxBytes=_RuckusZDWLANAPRadioStatsRxBytes_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,11),_RuckusZDWLANAPRadioStatsRxBytes_Type())
ruckusZDWLANAPRadioStatsRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsRxBytes.setStatus(_A)
_RuckusZDWLANAPRadioStatsRxMulticast_Type=Counter64
_RuckusZDWLANAPRadioStatsRxMulticast_Object=MibTableColumn
ruckusZDWLANAPRadioStatsRxMulticast=_RuckusZDWLANAPRadioStatsRxMulticast_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,12),_RuckusZDWLANAPRadioStatsRxMulticast_Type())
ruckusZDWLANAPRadioStatsRxMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsRxMulticast.setStatus(_A)
_RuckusZDWLANAPRadioStatsTxPkts_Type=Counter64
_RuckusZDWLANAPRadioStatsTxPkts_Object=MibTableColumn
ruckusZDWLANAPRadioStatsTxPkts=_RuckusZDWLANAPRadioStatsTxPkts_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,13),_RuckusZDWLANAPRadioStatsTxPkts_Type())
ruckusZDWLANAPRadioStatsTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsTxPkts.setStatus(_A)
_RuckusZDWLANAPRadioStatsTxBytes_Type=Counter64
_RuckusZDWLANAPRadioStatsTxBytes_Object=MibTableColumn
ruckusZDWLANAPRadioStatsTxBytes=_RuckusZDWLANAPRadioStatsTxBytes_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,14),_RuckusZDWLANAPRadioStatsTxBytes_Type())
ruckusZDWLANAPRadioStatsTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsTxBytes.setStatus(_A)
_RuckusZDWLANAPRadioStatsTxMulticast_Type=Counter64
_RuckusZDWLANAPRadioStatsTxMulticast_Object=MibTableColumn
ruckusZDWLANAPRadioStatsTxMulticast=_RuckusZDWLANAPRadioStatsTxMulticast_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,15),_RuckusZDWLANAPRadioStatsTxMulticast_Type())
ruckusZDWLANAPRadioStatsTxMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsTxMulticast.setStatus(_A)
_RuckusZDWLANAPRadioStatsTxFail_Type=Counter64
_RuckusZDWLANAPRadioStatsTxFail_Object=MibTableColumn
ruckusZDWLANAPRadioStatsTxFail=_RuckusZDWLANAPRadioStatsTxFail_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,16),_RuckusZDWLANAPRadioStatsTxFail_Type())
ruckusZDWLANAPRadioStatsTxFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsTxFail.setStatus(_A)
_RuckusZDWLANAPRadioStatsTxRetries_Type=Counter64
_RuckusZDWLANAPRadioStatsTxRetries_Object=MibTableColumn
ruckusZDWLANAPRadioStatsTxRetries=_RuckusZDWLANAPRadioStatsTxRetries_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,17),_RuckusZDWLANAPRadioStatsTxRetries_Type())
ruckusZDWLANAPRadioStatsTxRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsTxRetries.setStatus(_A)
_RuckusZDWLANAPRadioStatsPowerMgmt_Type=TruthValue
_RuckusZDWLANAPRadioStatsPowerMgmt_Object=MibTableColumn
ruckusZDWLANAPRadioStatsPowerMgmt=_RuckusZDWLANAPRadioStatsPowerMgmt_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,18),_RuckusZDWLANAPRadioStatsPowerMgmt_Type())
ruckusZDWLANAPRadioStatsPowerMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsPowerMgmt.setStatus(_A)
_RuckusZDWLANAPRadioStatsMaxSta_Type=Unsigned32
_RuckusZDWLANAPRadioStatsMaxSta_Object=MibTableColumn
ruckusZDWLANAPRadioStatsMaxSta=_RuckusZDWLANAPRadioStatsMaxSta_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,19),_RuckusZDWLANAPRadioStatsMaxSta_Type())
ruckusZDWLANAPRadioStatsMaxSta.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsMaxSta.setStatus(_A)
_RuckusZDWLANAPRadioStatsFrameErrorRate_Type=Unsigned32
_RuckusZDWLANAPRadioStatsFrameErrorRate_Object=MibTableColumn
ruckusZDWLANAPRadioStatsFrameErrorRate=_RuckusZDWLANAPRadioStatsFrameErrorRate_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,20),_RuckusZDWLANAPRadioStatsFrameErrorRate_Type())
ruckusZDWLANAPRadioStatsFrameErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsFrameErrorRate.setStatus(_A)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsFrameErrorRate.setUnits(_T)
_RuckusZDWLANAPRadioStatsFrameRetryRate_Type=Unsigned32
_RuckusZDWLANAPRadioStatsFrameRetryRate_Object=MibTableColumn
ruckusZDWLANAPRadioStatsFrameRetryRate=_RuckusZDWLANAPRadioStatsFrameRetryRate_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,21),_RuckusZDWLANAPRadioStatsFrameRetryRate_Type())
ruckusZDWLANAPRadioStatsFrameRetryRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsFrameRetryRate.setStatus(_A)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsFrameRetryRate.setUnits(_T)
_RuckusZDWLANAPRadioStatsMonitoredTime_Type=TimeTicks
_RuckusZDWLANAPRadioStatsMonitoredTime_Object=MibTableColumn
ruckusZDWLANAPRadioStatsMonitoredTime=_RuckusZDWLANAPRadioStatsMonitoredTime_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,22),_RuckusZDWLANAPRadioStatsMonitoredTime_Type())
ruckusZDWLANAPRadioStatsMonitoredTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsMonitoredTime.setStatus(_A)
_RuckusZDWLANAPRadioStatsTotalAssocTime_Type=Counter64
_RuckusZDWLANAPRadioStatsTotalAssocTime_Object=MibTableColumn
ruckusZDWLANAPRadioStatsTotalAssocTime=_RuckusZDWLANAPRadioStatsTotalAssocTime_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,24),_RuckusZDWLANAPRadioStatsTotalAssocTime_Type())
ruckusZDWLANAPRadioStatsTotalAssocTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsTotalAssocTime.setStatus(_A)
_RuckusZDWLANAPRadioStatsAuthReq_Type=Counter64
_RuckusZDWLANAPRadioStatsAuthReq_Object=MibTableColumn
ruckusZDWLANAPRadioStatsAuthReq=_RuckusZDWLANAPRadioStatsAuthReq_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,25),_RuckusZDWLANAPRadioStatsAuthReq_Type())
ruckusZDWLANAPRadioStatsAuthReq.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsAuthReq.setStatus(_A)
_RuckusZDWLANAPRadioStatsAuthResp_Type=Counter64
_RuckusZDWLANAPRadioStatsAuthResp_Object=MibTableColumn
ruckusZDWLANAPRadioStatsAuthResp=_RuckusZDWLANAPRadioStatsAuthResp_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,26),_RuckusZDWLANAPRadioStatsAuthResp_Type())
ruckusZDWLANAPRadioStatsAuthResp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsAuthResp.setStatus(_A)
_RuckusZDWLANAPRadioStatsAuthSuccess_Type=Counter64
_RuckusZDWLANAPRadioStatsAuthSuccess_Object=MibTableColumn
ruckusZDWLANAPRadioStatsAuthSuccess=_RuckusZDWLANAPRadioStatsAuthSuccess_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,27),_RuckusZDWLANAPRadioStatsAuthSuccess_Type())
ruckusZDWLANAPRadioStatsAuthSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsAuthSuccess.setStatus(_A)
_RuckusZDWLANAPRadioStatsAuthFail_Type=Counter64
_RuckusZDWLANAPRadioStatsAuthFail_Object=MibTableColumn
ruckusZDWLANAPRadioStatsAuthFail=_RuckusZDWLANAPRadioStatsAuthFail_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,28),_RuckusZDWLANAPRadioStatsAuthFail_Type())
ruckusZDWLANAPRadioStatsAuthFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsAuthFail.setStatus(_A)
_RuckusZDWLANAPRadioStatsAssocReq_Type=Counter64
_RuckusZDWLANAPRadioStatsAssocReq_Object=MibTableColumn
ruckusZDWLANAPRadioStatsAssocReq=_RuckusZDWLANAPRadioStatsAssocReq_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,29),_RuckusZDWLANAPRadioStatsAssocReq_Type())
ruckusZDWLANAPRadioStatsAssocReq.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsAssocReq.setStatus(_A)
_RuckusZDWLANAPRadioStatsAssocResp_Type=Counter64
_RuckusZDWLANAPRadioStatsAssocResp_Object=MibTableColumn
ruckusZDWLANAPRadioStatsAssocResp=_RuckusZDWLANAPRadioStatsAssocResp_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,30),_RuckusZDWLANAPRadioStatsAssocResp_Type())
ruckusZDWLANAPRadioStatsAssocResp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsAssocResp.setStatus(_A)
_RuckusZDWLANAPRadioStatsReassocReq_Type=Counter64
_RuckusZDWLANAPRadioStatsReassocReq_Object=MibTableColumn
ruckusZDWLANAPRadioStatsReassocReq=_RuckusZDWLANAPRadioStatsReassocReq_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,31),_RuckusZDWLANAPRadioStatsReassocReq_Type())
ruckusZDWLANAPRadioStatsReassocReq.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsReassocReq.setStatus(_A)
_RuckusZDWLANAPRadioStatsReassocResp_Type=Counter64
_RuckusZDWLANAPRadioStatsReassocResp_Object=MibTableColumn
ruckusZDWLANAPRadioStatsReassocResp=_RuckusZDWLANAPRadioStatsReassocResp_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,32),_RuckusZDWLANAPRadioStatsReassocResp_Type())
ruckusZDWLANAPRadioStatsReassocResp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsReassocResp.setStatus(_A)
_RuckusZDWLANAPRadioStatsAssocSuccess_Type=Counter64
_RuckusZDWLANAPRadioStatsAssocSuccess_Object=MibTableColumn
ruckusZDWLANAPRadioStatsAssocSuccess=_RuckusZDWLANAPRadioStatsAssocSuccess_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,33),_RuckusZDWLANAPRadioStatsAssocSuccess_Type())
ruckusZDWLANAPRadioStatsAssocSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsAssocSuccess.setStatus(_A)
_RuckusZDWLANAPRadioStatsAssocFail_Type=Counter64
_RuckusZDWLANAPRadioStatsAssocFail_Object=MibTableColumn
ruckusZDWLANAPRadioStatsAssocFail=_RuckusZDWLANAPRadioStatsAssocFail_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,34),_RuckusZDWLANAPRadioStatsAssocFail_Type())
ruckusZDWLANAPRadioStatsAssocFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsAssocFail.setStatus(_A)
_RuckusZDWLANAPRadioStatsAssocDenied_Type=Counter64
_RuckusZDWLANAPRadioStatsAssocDenied_Object=MibTableColumn
ruckusZDWLANAPRadioStatsAssocDenied=_RuckusZDWLANAPRadioStatsAssocDenied_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,35),_RuckusZDWLANAPRadioStatsAssocDenied_Type())
ruckusZDWLANAPRadioStatsAssocDenied.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsAssocDenied.setStatus(_A)
_RuckusZDWLANAPRadioStatsDiassocAbnormal_Type=Counter64
_RuckusZDWLANAPRadioStatsDiassocAbnormal_Object=MibTableColumn
ruckusZDWLANAPRadioStatsDiassocAbnormal=_RuckusZDWLANAPRadioStatsDiassocAbnormal_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,36),_RuckusZDWLANAPRadioStatsDiassocAbnormal_Type())
ruckusZDWLANAPRadioStatsDiassocAbnormal.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsDiassocAbnormal.setStatus(_A)
_RuckusZDWLANAPRadioStatsDiassocCapacity_Type=Counter64
_RuckusZDWLANAPRadioStatsDiassocCapacity_Object=MibTableColumn
ruckusZDWLANAPRadioStatsDiassocCapacity=_RuckusZDWLANAPRadioStatsDiassocCapacity_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,37),_RuckusZDWLANAPRadioStatsDiassocCapacity_Type())
ruckusZDWLANAPRadioStatsDiassocCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsDiassocCapacity.setStatus(_A)
_RuckusZDWLANAPRadioStatsDiassocLeave_Type=Counter64
_RuckusZDWLANAPRadioStatsDiassocLeave_Object=MibTableColumn
ruckusZDWLANAPRadioStatsDiassocLeave=_RuckusZDWLANAPRadioStatsDiassocLeave_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,38),_RuckusZDWLANAPRadioStatsDiassocLeave_Type())
ruckusZDWLANAPRadioStatsDiassocLeave.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsDiassocLeave.setStatus(_A)
_RuckusZDWLANAPRadioStatsDiassocMisc_Type=Counter64
_RuckusZDWLANAPRadioStatsDiassocMisc_Object=MibTableColumn
ruckusZDWLANAPRadioStatsDiassocMisc=_RuckusZDWLANAPRadioStatsDiassocMisc_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,39),_RuckusZDWLANAPRadioStatsDiassocMisc_Type())
ruckusZDWLANAPRadioStatsDiassocMisc.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsDiassocMisc.setStatus(_A)
_RuckusZDWLANAPRadioStatsResourceUtil_Type=Unsigned32
_RuckusZDWLANAPRadioStatsResourceUtil_Object=MibTableColumn
ruckusZDWLANAPRadioStatsResourceUtil=_RuckusZDWLANAPRadioStatsResourceUtil_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,40),_RuckusZDWLANAPRadioStatsResourceUtil_Type())
ruckusZDWLANAPRadioStatsResourceUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsResourceUtil.setStatus(_A)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsResourceUtil.setUnits('percentage')
_RuckusZDWLANAPRadioStatsRxSignalFrm_Type=Counter64
_RuckusZDWLANAPRadioStatsRxSignalFrm_Object=MibTableColumn
ruckusZDWLANAPRadioStatsRxSignalFrm=_RuckusZDWLANAPRadioStatsRxSignalFrm_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,41),_RuckusZDWLANAPRadioStatsRxSignalFrm_Type())
ruckusZDWLANAPRadioStatsRxSignalFrm.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsRxSignalFrm.setStatus(_A)
_RuckusZDWLANAPRadioStatsTxSignalFrm_Type=Counter64
_RuckusZDWLANAPRadioStatsTxSignalFrm_Object=MibTableColumn
ruckusZDWLANAPRadioStatsTxSignalFrm=_RuckusZDWLANAPRadioStatsTxSignalFrm_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,42),_RuckusZDWLANAPRadioStatsTxSignalFrm_Type())
ruckusZDWLANAPRadioStatsTxSignalFrm.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsTxSignalFrm.setStatus(_A)
_RuckusZDWLANAPRadioStatsTotalSignalFrm_Type=Counter64
_RuckusZDWLANAPRadioStatsTotalSignalFrm_Object=MibTableColumn
ruckusZDWLANAPRadioStatsTotalSignalFrm=_RuckusZDWLANAPRadioStatsTotalSignalFrm_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,43),_RuckusZDWLANAPRadioStatsTotalSignalFrm_Type())
ruckusZDWLANAPRadioStatsTotalSignalFrm.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsTotalSignalFrm.setStatus(_A)
_RuckusZDWLANAPRadioStatsAntennaGain_Type=Unsigned32
_RuckusZDWLANAPRadioStatsAntennaGain_Object=MibTableColumn
ruckusZDWLANAPRadioStatsAntennaGain=_RuckusZDWLANAPRadioStatsAntennaGain_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,44),_RuckusZDWLANAPRadioStatsAntennaGain_Type())
ruckusZDWLANAPRadioStatsAntennaGain.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsAntennaGain.setStatus(_A)
_RuckusZDWLANAPRadioStatsBeaconPeriod_Type=Unsigned32
_RuckusZDWLANAPRadioStatsBeaconPeriod_Object=MibTableColumn
ruckusZDWLANAPRadioStatsBeaconPeriod=_RuckusZDWLANAPRadioStatsBeaconPeriod_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,45),_RuckusZDWLANAPRadioStatsBeaconPeriod_Type())
ruckusZDWLANAPRadioStatsBeaconPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsBeaconPeriod.setStatus(_A)
_RuckusZDWLANAPRadioStatsRTSThreshold_Type=Unsigned32
_RuckusZDWLANAPRadioStatsRTSThreshold_Object=MibTableColumn
ruckusZDWLANAPRadioStatsRTSThreshold=_RuckusZDWLANAPRadioStatsRTSThreshold_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,46),_RuckusZDWLANAPRadioStatsRTSThreshold_Type())
ruckusZDWLANAPRadioStatsRTSThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsRTSThreshold.setStatus(_A)
_RuckusZDWLANAPRadioStatsFragThreshold_Type=Unsigned32
_RuckusZDWLANAPRadioStatsFragThreshold_Object=MibTableColumn
ruckusZDWLANAPRadioStatsFragThreshold=_RuckusZDWLANAPRadioStatsFragThreshold_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,2,1,47),_RuckusZDWLANAPRadioStatsFragThreshold_Type())
ruckusZDWLANAPRadioStatsFragThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPRadioStatsFragThreshold.setStatus(_A)
_RuckusZDWLANVapTable_Object=MibTable
ruckusZDWLANVapTable=_RuckusZDWLANVapTable_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3))
if mibBuilder.loadTexts:ruckusZDWLANVapTable.setStatus(_A)
_RuckusZDWLANVapEntry_Object=MibTableRow
ruckusZDWLANVapEntry=_RuckusZDWLANVapEntry_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3,1))
ruckusZDWLANVapEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:ruckusZDWLANVapEntry.setStatus(_A)
_RuckusZDWLANVapBSSID_Type=MacAddress
_RuckusZDWLANVapBSSID_Object=MibTableColumn
ruckusZDWLANVapBSSID=_RuckusZDWLANVapBSSID_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3,1,1),_RuckusZDWLANVapBSSID_Type())
ruckusZDWLANVapBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANVapBSSID.setStatus(_A)
_RuckusZDWLANVapPAPAddr_Type=MacAddress
_RuckusZDWLANVapPAPAddr_Object=MibTableColumn
ruckusZDWLANVapPAPAddr=_RuckusZDWLANVapPAPAddr_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3,1,2),_RuckusZDWLANVapPAPAddr_Type())
ruckusZDWLANVapPAPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANVapPAPAddr.setStatus(_A)
_RuckusZDWLANVapSSID_Type=RuckusSSID
_RuckusZDWLANVapSSID_Object=MibTableColumn
ruckusZDWLANVapSSID=_RuckusZDWLANVapSSID_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3,1,3),_RuckusZDWLANVapSSID_Type())
ruckusZDWLANVapSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANVapSSID.setStatus(_A)
_RuckusZDWLANVapLanRxBytes_Type=Counter64
_RuckusZDWLANVapLanRxBytes_Object=MibTableColumn
ruckusZDWLANVapLanRxBytes=_RuckusZDWLANVapLanRxBytes_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3,1,6),_RuckusZDWLANVapLanRxBytes_Type())
ruckusZDWLANVapLanRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANVapLanRxBytes.setStatus(_A)
_RuckusZDWLANVapLanTxBytes_Type=Counter64
_RuckusZDWLANVapLanTxBytes_Object=MibTableColumn
ruckusZDWLANVapLanTxBytes=_RuckusZDWLANVapLanTxBytes_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3,1,7),_RuckusZDWLANVapLanTxBytes_Type())
ruckusZDWLANVapLanTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANVapLanTxBytes.setStatus(_A)
_RuckusZDWLANVapWlanRxBytes_Type=Counter64
_RuckusZDWLANVapWlanRxBytes_Object=MibTableColumn
ruckusZDWLANVapWlanRxBytes=_RuckusZDWLANVapWlanRxBytes_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3,1,8),_RuckusZDWLANVapWlanRxBytes_Type())
ruckusZDWLANVapWlanRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANVapWlanRxBytes.setStatus(_A)
_RuckusZDWLANVapWlanTxBytes_Type=Counter64
_RuckusZDWLANVapWlanTxBytes_Object=MibTableColumn
ruckusZDWLANVapWlanTxBytes=_RuckusZDWLANVapWlanTxBytes_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3,1,9),_RuckusZDWLANVapWlanTxBytes_Type())
ruckusZDWLANVapWlanTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANVapWlanTxBytes.setStatus(_A)
_RuckusZDWLANVapWlanRxErrorPkt_Type=Counter64
_RuckusZDWLANVapWlanRxErrorPkt_Object=MibTableColumn
ruckusZDWLANVapWlanRxErrorPkt=_RuckusZDWLANVapWlanRxErrorPkt_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3,1,11),_RuckusZDWLANVapWlanRxErrorPkt_Type())
ruckusZDWLANVapWlanRxErrorPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANVapWlanRxErrorPkt.setStatus(_A)
_RuckusZDWLANVapWlanRxUnicastPkt_Type=Counter64
_RuckusZDWLANVapWlanRxUnicastPkt_Object=MibTableColumn
ruckusZDWLANVapWlanRxUnicastPkt=_RuckusZDWLANVapWlanRxUnicastPkt_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3,1,12),_RuckusZDWLANVapWlanRxUnicastPkt_Type())
ruckusZDWLANVapWlanRxUnicastPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANVapWlanRxUnicastPkt.setStatus(_A)
_RuckusZDWLANVapWlanTxUnicastPkt_Type=Counter64
_RuckusZDWLANVapWlanTxUnicastPkt_Object=MibTableColumn
ruckusZDWLANVapWlanTxUnicastPkt=_RuckusZDWLANVapWlanTxUnicastPkt_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3,1,13),_RuckusZDWLANVapWlanTxUnicastPkt_Type())
ruckusZDWLANVapWlanTxUnicastPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANVapWlanTxUnicastPkt.setStatus(_A)
_RuckusZDWLANVapWlanRxPkt_Type=Counter64
_RuckusZDWLANVapWlanRxPkt_Object=MibTableColumn
ruckusZDWLANVapWlanRxPkt=_RuckusZDWLANVapWlanRxPkt_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3,1,14),_RuckusZDWLANVapWlanRxPkt_Type())
ruckusZDWLANVapWlanRxPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANVapWlanRxPkt.setStatus(_A)
_RuckusZDWLANVapWlanRxDropPkt_Type=Counter64
_RuckusZDWLANVapWlanRxDropPkt_Object=MibTableColumn
ruckusZDWLANVapWlanRxDropPkt=_RuckusZDWLANVapWlanRxDropPkt_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3,1,15),_RuckusZDWLANVapWlanRxDropPkt_Type())
ruckusZDWLANVapWlanRxDropPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANVapWlanRxDropPkt.setStatus(_A)
_RuckusZDWLANVapWlanTxErrPkt_Type=Counter64
_RuckusZDWLANVapWlanTxErrPkt_Object=MibTableColumn
ruckusZDWLANVapWlanTxErrPkt=_RuckusZDWLANVapWlanTxErrPkt_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3,1,16),_RuckusZDWLANVapWlanTxErrPkt_Type())
ruckusZDWLANVapWlanTxErrPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANVapWlanTxErrPkt.setStatus(_A)
_RuckusZDWLANVapWlanTxPkt_Type=Counter64
_RuckusZDWLANVapWlanTxPkt_Object=MibTableColumn
ruckusZDWLANVapWlanTxPkt=_RuckusZDWLANVapWlanTxPkt_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3,1,17),_RuckusZDWLANVapWlanTxPkt_Type())
ruckusZDWLANVapWlanTxPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANVapWlanTxPkt.setStatus(_A)
_RuckusZDWLANVapWlanTxDropPkt_Type=Counter64
_RuckusZDWLANVapWlanTxDropPkt_Object=MibTableColumn
ruckusZDWLANVapWlanTxDropPkt=_RuckusZDWLANVapWlanTxDropPkt_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,3,1,18),_RuckusZDWLANVapWlanTxDropPkt_Type())
ruckusZDWLANVapWlanTxDropPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANVapWlanTxDropPkt.setStatus(_A)
_RuckusZDWLANIfTable_Object=MibTable
ruckusZDWLANIfTable=_RuckusZDWLANIfTable_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4))
if mibBuilder.loadTexts:ruckusZDWLANIfTable.setStatus(_A)
_RuckusZDWLANIfEntry_Object=MibTableRow
ruckusZDWLANIfEntry=_RuckusZDWLANIfEntry_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1))
ruckusZDWLANIfEntry.setIndexNames((0,_D,_V),(0,_D,_W))
if mibBuilder.loadTexts:ruckusZDWLANIfEntry.setStatus(_A)
_RuckusZDWLANAPMac_Type=MacAddress
_RuckusZDWLANAPMac_Object=MibTableColumn
ruckusZDWLANAPMac=_RuckusZDWLANAPMac_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,1),_RuckusZDWLANAPMac_Type())
ruckusZDWLANAPMac.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPMac.setStatus(_A)
_RuckusZDWLANAPIfIndex_Type=InterfaceIndex
_RuckusZDWLANAPIfIndex_Object=MibTableColumn
ruckusZDWLANAPIfIndex=_RuckusZDWLANAPIfIndex_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,2),_RuckusZDWLANAPIfIndex_Type())
ruckusZDWLANAPIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfIndex.setStatus(_A)
_RuckusZDWLANAPIfDescr_Type=DisplayString
_RuckusZDWLANAPIfDescr_Object=MibTableColumn
ruckusZDWLANAPIfDescr=_RuckusZDWLANAPIfDescr_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,3),_RuckusZDWLANAPIfDescr_Type())
ruckusZDWLANAPIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfDescr.setStatus(_A)
_RuckusZDWLANAPIfType_Type=IANAifType
_RuckusZDWLANAPIfType_Object=MibTableColumn
ruckusZDWLANAPIfType=_RuckusZDWLANAPIfType_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,4),_RuckusZDWLANAPIfType_Type())
ruckusZDWLANAPIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfType.setStatus(_A)
_RuckusZDWLANAPIfMtu_Type=Integer32
_RuckusZDWLANAPIfMtu_Object=MibTableColumn
ruckusZDWLANAPIfMtu=_RuckusZDWLANAPIfMtu_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,5),_RuckusZDWLANAPIfMtu_Type())
ruckusZDWLANAPIfMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfMtu.setStatus(_A)
_RuckusZDWLANAPIfSpeed_Type=DisplayString
_RuckusZDWLANAPIfSpeed_Object=MibTableColumn
ruckusZDWLANAPIfSpeed=_RuckusZDWLANAPIfSpeed_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,6),_RuckusZDWLANAPIfSpeed_Type())
ruckusZDWLANAPIfSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfSpeed.setStatus(_A)
_RuckusZDWLANAPIfPhysAddress_Type=DisplayString
_RuckusZDWLANAPIfPhysAddress_Object=MibTableColumn
ruckusZDWLANAPIfPhysAddress=_RuckusZDWLANAPIfPhysAddress_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,7),_RuckusZDWLANAPIfPhysAddress_Type())
ruckusZDWLANAPIfPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfPhysAddress.setStatus(_A)
class _RuckusZDWLANAPIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_X,3)))
_RuckusZDWLANAPIfAdminStatus_Type.__name__=_C
_RuckusZDWLANAPIfAdminStatus_Object=MibTableColumn
ruckusZDWLANAPIfAdminStatus=_RuckusZDWLANAPIfAdminStatus_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,8),_RuckusZDWLANAPIfAdminStatus_Type())
ruckusZDWLANAPIfAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfAdminStatus.setStatus(_A)
class _RuckusZDWLANAPIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),(_G,2),(_X,3),(_P,4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
_RuckusZDWLANAPIfOperStatus_Type.__name__=_C
_RuckusZDWLANAPIfOperStatus_Object=MibTableColumn
ruckusZDWLANAPIfOperStatus=_RuckusZDWLANAPIfOperStatus_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,9),_RuckusZDWLANAPIfOperStatus_Type())
ruckusZDWLANAPIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfOperStatus.setStatus(_A)
_RuckusZDWLANAPIfInOctets_Type=Counter32
_RuckusZDWLANAPIfInOctets_Object=MibTableColumn
ruckusZDWLANAPIfInOctets=_RuckusZDWLANAPIfInOctets_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,10),_RuckusZDWLANAPIfInOctets_Type())
ruckusZDWLANAPIfInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfInOctets.setStatus(_A)
_RuckusZDWLANAPIfInUcastPkts_Type=Counter32
_RuckusZDWLANAPIfInUcastPkts_Object=MibTableColumn
ruckusZDWLANAPIfInUcastPkts=_RuckusZDWLANAPIfInUcastPkts_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,11),_RuckusZDWLANAPIfInUcastPkts_Type())
ruckusZDWLANAPIfInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfInUcastPkts.setStatus(_A)
_RuckusZDWLANAPIfInNUcastPkts_Type=Counter32
_RuckusZDWLANAPIfInNUcastPkts_Object=MibTableColumn
ruckusZDWLANAPIfInNUcastPkts=_RuckusZDWLANAPIfInNUcastPkts_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,12),_RuckusZDWLANAPIfInNUcastPkts_Type())
ruckusZDWLANAPIfInNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfInNUcastPkts.setStatus(_A)
_RuckusZDWLANAPIfInDiscards_Type=Counter32
_RuckusZDWLANAPIfInDiscards_Object=MibTableColumn
ruckusZDWLANAPIfInDiscards=_RuckusZDWLANAPIfInDiscards_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,13),_RuckusZDWLANAPIfInDiscards_Type())
ruckusZDWLANAPIfInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfInDiscards.setStatus(_A)
_RuckusZDWLANAPIfInErrors_Type=Counter32
_RuckusZDWLANAPIfInErrors_Object=MibTableColumn
ruckusZDWLANAPIfInErrors=_RuckusZDWLANAPIfInErrors_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,14),_RuckusZDWLANAPIfInErrors_Type())
ruckusZDWLANAPIfInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfInErrors.setStatus(_A)
_RuckusZDWLANAPIfInUnknownProtos_Type=Counter32
_RuckusZDWLANAPIfInUnknownProtos_Object=MibTableColumn
ruckusZDWLANAPIfInUnknownProtos=_RuckusZDWLANAPIfInUnknownProtos_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,15),_RuckusZDWLANAPIfInUnknownProtos_Type())
ruckusZDWLANAPIfInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfInUnknownProtos.setStatus(_A)
_RuckusZDWLANAPIfOutOctets_Type=Counter32
_RuckusZDWLANAPIfOutOctets_Object=MibTableColumn
ruckusZDWLANAPIfOutOctets=_RuckusZDWLANAPIfOutOctets_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,16),_RuckusZDWLANAPIfOutOctets_Type())
ruckusZDWLANAPIfOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfOutOctets.setStatus(_A)
_RuckusZDWLANAPIfOutUcastPkts_Type=Counter32
_RuckusZDWLANAPIfOutUcastPkts_Object=MibTableColumn
ruckusZDWLANAPIfOutUcastPkts=_RuckusZDWLANAPIfOutUcastPkts_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,17),_RuckusZDWLANAPIfOutUcastPkts_Type())
ruckusZDWLANAPIfOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfOutUcastPkts.setStatus(_A)
_RuckusZDWLANAPIfOutNUcastPkts_Type=Counter32
_RuckusZDWLANAPIfOutNUcastPkts_Object=MibTableColumn
ruckusZDWLANAPIfOutNUcastPkts=_RuckusZDWLANAPIfOutNUcastPkts_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,18),_RuckusZDWLANAPIfOutNUcastPkts_Type())
ruckusZDWLANAPIfOutNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfOutNUcastPkts.setStatus(_A)
_RuckusZDWLANAPIfOutDiscards_Type=Counter32
_RuckusZDWLANAPIfOutDiscards_Object=MibTableColumn
ruckusZDWLANAPIfOutDiscards=_RuckusZDWLANAPIfOutDiscards_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,19),_RuckusZDWLANAPIfOutDiscards_Type())
ruckusZDWLANAPIfOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfOutDiscards.setStatus(_A)
_RuckusZDWLANAPIfOutErrors_Type=Counter32
_RuckusZDWLANAPIfOutErrors_Object=MibTableColumn
ruckusZDWLANAPIfOutErrors=_RuckusZDWLANAPIfOutErrors_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,20),_RuckusZDWLANAPIfOutErrors_Type())
ruckusZDWLANAPIfOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfOutErrors.setStatus(_A)
_RuckusZDWLANAPIfName_Type=DisplayString
_RuckusZDWLANAPIfName_Object=MibTableColumn
ruckusZDWLANAPIfName=_RuckusZDWLANAPIfName_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,21),_RuckusZDWLANAPIfName_Type())
ruckusZDWLANAPIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfName.setStatus(_A)
_RuckusZDWLANAPIfNameDefined_Type=DisplayString
_RuckusZDWLANAPIfNameDefined_Object=MibTableColumn
ruckusZDWLANAPIfNameDefined=_RuckusZDWLANAPIfNameDefined_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,4,1,22),_RuckusZDWLANAPIfNameDefined_Type())
ruckusZDWLANAPIfNameDefined.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPIfNameDefined.setStatus(_A)
_RuckusZDWLANAPEthStatusTable_Object=MibTable
ruckusZDWLANAPEthStatusTable=_RuckusZDWLANAPEthStatusTable_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,8))
if mibBuilder.loadTexts:ruckusZDWLANAPEthStatusTable.setStatus(_A)
_RuckusZDWLANAPEthStatusEntry_Object=MibTableRow
ruckusZDWLANAPEthStatusEntry=_RuckusZDWLANAPEthStatusEntry_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,8,1))
ruckusZDWLANAPEthStatusEntry.setIndexNames((0,_D,_Y),(0,_D,_Z))
if mibBuilder.loadTexts:ruckusZDWLANAPEthStatusEntry.setStatus(_A)
_RuckusZDWLANAPMacAddress_Type=MacAddress
_RuckusZDWLANAPMacAddress_Object=MibTableColumn
ruckusZDWLANAPMacAddress=_RuckusZDWLANAPMacAddress_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,8,1,1),_RuckusZDWLANAPMacAddress_Type())
ruckusZDWLANAPMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPMacAddress.setStatus(_A)
_RuckusZDWLANAPEthPortId_Type=Integer32
_RuckusZDWLANAPEthPortId_Object=MibTableColumn
ruckusZDWLANAPEthPortId=_RuckusZDWLANAPEthPortId_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,8,1,2),_RuckusZDWLANAPEthPortId_Type())
ruckusZDWLANAPEthPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPEthPortId.setStatus(_A)
_RuckusZDWLANAPEthIfname_Type=OctetString
_RuckusZDWLANAPEthIfname_Object=MibTableColumn
ruckusZDWLANAPEthIfname=_RuckusZDWLANAPEthIfname_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,8,1,5),_RuckusZDWLANAPEthIfname_Type())
ruckusZDWLANAPEthIfname.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPEthIfname.setStatus(_A)
class _RuckusZDWLANAPEthDot1xStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auth',1),('supp',2),('none',3)))
_RuckusZDWLANAPEthDot1xStatus_Type.__name__=_C
_RuckusZDWLANAPEthDot1xStatus_Object=MibTableColumn
ruckusZDWLANAPEthDot1xStatus=_RuckusZDWLANAPEthDot1xStatus_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,8,1,6),_RuckusZDWLANAPEthDot1xStatus_Type())
ruckusZDWLANAPEthDot1xStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPEthDot1xStatus.setStatus(_A)
class _RuckusZDWLANAPEthLogicalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RuckusZDWLANAPEthLogicalStatus_Type.__name__=_C
_RuckusZDWLANAPEthLogicalStatus_Object=MibTableColumn
ruckusZDWLANAPEthLogicalStatus=_RuckusZDWLANAPEthLogicalStatus_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,8,1,7),_RuckusZDWLANAPEthLogicalStatus_Type())
ruckusZDWLANAPEthLogicalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPEthLogicalStatus.setStatus(_A)
class _RuckusZDWLANAPEthPhyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RuckusZDWLANAPEthPhyStatus_Type.__name__=_C
_RuckusZDWLANAPEthPhyStatus_Object=MibTableColumn
ruckusZDWLANAPEthPhyStatus=_RuckusZDWLANAPEthPhyStatus_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,8,1,8),_RuckusZDWLANAPEthPhyStatus_Type())
ruckusZDWLANAPEthPhyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPEthPhyStatus.setStatus(_A)
_RuckusZDWLANAPEthPhyIfSpeed_Type=Integer32
_RuckusZDWLANAPEthPhyIfSpeed_Object=MibTableColumn
ruckusZDWLANAPEthPhyIfSpeed=_RuckusZDWLANAPEthPhyIfSpeed_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,8,1,9),_RuckusZDWLANAPEthPhyIfSpeed_Type())
ruckusZDWLANAPEthPhyIfSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPEthPhyIfSpeed.setStatus(_A)
class _RuckusZDWLANAPEthPhyLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('full',1),('half',2)))
_RuckusZDWLANAPEthPhyLinkStatus_Type.__name__=_C
_RuckusZDWLANAPEthPhyLinkStatus_Object=MibTableColumn
ruckusZDWLANAPEthPhyLinkStatus=_RuckusZDWLANAPEthPhyLinkStatus_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,8,1,10),_RuckusZDWLANAPEthPhyLinkStatus_Type())
ruckusZDWLANAPEthPhyLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPEthPhyLinkStatus.setStatus(_A)
_RuckusZDWLANAPEthLabel_Type=OctetString
_RuckusZDWLANAPEthLabel_Object=MibTableColumn
ruckusZDWLANAPEthLabel=_RuckusZDWLANAPEthLabel_Object((1,3,6,1,4,1,25053,1,2,2,1,1,2,8,1,11),_RuckusZDWLANAPEthLabel_Type())
ruckusZDWLANAPEthLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANAPEthLabel.setStatus(_A)
_RuckusZDWLANStaInfo_ObjectIdentity=ObjectIdentity
ruckusZDWLANStaInfo=_RuckusZDWLANStaInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,2,2,1,1,3))
_RuckusZDWLANStaTable_Object=MibTable
ruckusZDWLANStaTable=_RuckusZDWLANStaTable_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1))
if mibBuilder.loadTexts:ruckusZDWLANStaTable.setStatus(_A)
_RuckusZDWLANStaEntry_Object=MibTableRow
ruckusZDWLANStaEntry=_RuckusZDWLANStaEntry_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1))
ruckusZDWLANStaEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:ruckusZDWLANStaEntry.setStatus(_A)
_RuckusZDWLANStaMacAddr_Type=MacAddress
_RuckusZDWLANStaMacAddr_Object=MibTableColumn
ruckusZDWLANStaMacAddr=_RuckusZDWLANStaMacAddr_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,1),_RuckusZDWLANStaMacAddr_Type())
ruckusZDWLANStaMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaMacAddr.setStatus(_A)
_RuckusZDWLANStaAPMacAddr_Type=MacAddress
_RuckusZDWLANStaAPMacAddr_Object=MibTableColumn
ruckusZDWLANStaAPMacAddr=_RuckusZDWLANStaAPMacAddr_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,2),_RuckusZDWLANStaAPMacAddr_Type())
ruckusZDWLANStaAPMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaAPMacAddr.setStatus(_A)
_RuckusZDWLANStaBSSID_Type=MacAddress
_RuckusZDWLANStaBSSID_Object=MibTableColumn
ruckusZDWLANStaBSSID=_RuckusZDWLANStaBSSID_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,3),_RuckusZDWLANStaBSSID_Type())
ruckusZDWLANStaBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaBSSID.setStatus(_A)
_RuckusZDWLANStaSSID_Type=RuckusSSID
_RuckusZDWLANStaSSID_Object=MibTableColumn
ruckusZDWLANStaSSID=_RuckusZDWLANStaSSID_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,4),_RuckusZDWLANStaSSID_Type())
ruckusZDWLANStaSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaSSID.setStatus(_A)
_RuckusZDWLANStaUser_Type=DisplayString
_RuckusZDWLANStaUser_Object=MibTableColumn
ruckusZDWLANStaUser=_RuckusZDWLANStaUser_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,5),_RuckusZDWLANStaUser_Type())
ruckusZDWLANStaUser.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaUser.setStatus(_A)
class _RuckusZDWLANStaRadioType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_H,0),('radio11b',1),('radio11g',2),(_I,3),(_J,4),(_K,5)))
_RuckusZDWLANStaRadioType_Type.__name__=_C
_RuckusZDWLANStaRadioType_Object=MibTableColumn
ruckusZDWLANStaRadioType=_RuckusZDWLANStaRadioType_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,6),_RuckusZDWLANStaRadioType_Type())
ruckusZDWLANStaRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaRadioType.setStatus(_A)
_RuckusZDWLANStaChannel_Type=Unsigned32
_RuckusZDWLANStaChannel_Object=MibTableColumn
ruckusZDWLANStaChannel=_RuckusZDWLANStaChannel_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,7),_RuckusZDWLANStaChannel_Type())
ruckusZDWLANStaChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaChannel.setStatus(_A)
_RuckusZDWLANStaIPAddr_Type=IpAddress
_RuckusZDWLANStaIPAddr_Object=MibTableColumn
ruckusZDWLANStaIPAddr=_RuckusZDWLANStaIPAddr_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,8),_RuckusZDWLANStaIPAddr_Type())
ruckusZDWLANStaIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaIPAddr.setStatus(_A)
_RuckusZDWLANStaAvgSNR_Type=Integer32
_RuckusZDWLANStaAvgSNR_Object=MibTableColumn
ruckusZDWLANStaAvgSNR=_RuckusZDWLANStaAvgSNR_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,9),_RuckusZDWLANStaAvgSNR_Type())
ruckusZDWLANStaAvgSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaAvgSNR.setStatus(_A)
_RuckusZDWLANStaRxPkts_Type=Counter32
_RuckusZDWLANStaRxPkts_Object=MibTableColumn
ruckusZDWLANStaRxPkts=_RuckusZDWLANStaRxPkts_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,10),_RuckusZDWLANStaRxPkts_Type())
ruckusZDWLANStaRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaRxPkts.setStatus(_A)
_RuckusZDWLANStaRxBytes_Type=Counter64
_RuckusZDWLANStaRxBytes_Object=MibTableColumn
ruckusZDWLANStaRxBytes=_RuckusZDWLANStaRxBytes_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,11),_RuckusZDWLANStaRxBytes_Type())
ruckusZDWLANStaRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaRxBytes.setStatus(_A)
_RuckusZDWLANStaTxPkts_Type=Counter32
_RuckusZDWLANStaTxPkts_Object=MibTableColumn
ruckusZDWLANStaTxPkts=_RuckusZDWLANStaTxPkts_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,12),_RuckusZDWLANStaTxPkts_Type())
ruckusZDWLANStaTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaTxPkts.setStatus(_A)
_RuckusZDWLANStaTxBytes_Type=Counter64
_RuckusZDWLANStaTxBytes_Object=MibTableColumn
ruckusZDWLANStaTxBytes=_RuckusZDWLANStaTxBytes_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,13),_RuckusZDWLANStaTxBytes_Type())
ruckusZDWLANStaTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaTxBytes.setStatus(_A)
_RuckusZDWLANStaRetries_Type=Counter32
_RuckusZDWLANStaRetries_Object=MibTableColumn
ruckusZDWLANStaRetries=_RuckusZDWLANStaRetries_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,14),_RuckusZDWLANStaRetries_Type())
ruckusZDWLANStaRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaRetries.setStatus(_A)
_RuckusZDWLANStaAssocTime_Type=TimeTicks
_RuckusZDWLANStaAssocTime_Object=MibTableColumn
ruckusZDWLANStaAssocTime=_RuckusZDWLANStaAssocTime_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,15),_RuckusZDWLANStaAssocTime_Type())
ruckusZDWLANStaAssocTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaAssocTime.setStatus(_A)
_RuckusZDWLANStaRxError_Type=Counter32
_RuckusZDWLANStaRxError_Object=MibTableColumn
ruckusZDWLANStaRxError=_RuckusZDWLANStaRxError_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,16),_RuckusZDWLANStaRxError_Type())
ruckusZDWLANStaRxError.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaRxError.setStatus(_A)
_RuckusZDWLANStaTxSuccess_Type=Counter32
_RuckusZDWLANStaTxSuccess_Object=MibTableColumn
ruckusZDWLANStaTxSuccess=_RuckusZDWLANStaTxSuccess_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,17),_RuckusZDWLANStaTxSuccess_Type())
ruckusZDWLANStaTxSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaTxSuccess.setStatus(_A)
_RuckusZDWLANSta11bgReassoc_Type=Counter32
_RuckusZDWLANSta11bgReassoc_Object=MibTableColumn
ruckusZDWLANSta11bgReassoc=_RuckusZDWLANSta11bgReassoc_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,18),_RuckusZDWLANSta11bgReassoc_Type())
ruckusZDWLANSta11bgReassoc.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANSta11bgReassoc.setStatus(_A)
_RuckusZDWLANStaAssocTimestamp_Type=DisplayString
_RuckusZDWLANStaAssocTimestamp_Object=MibTableColumn
ruckusZDWLANStaAssocTimestamp=_RuckusZDWLANStaAssocTimestamp_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,19),_RuckusZDWLANStaAssocTimestamp_Type())
ruckusZDWLANStaAssocTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaAssocTimestamp.setStatus(_A)
_RuckusZDWLANStaRetryBytes_Type=Counter32
_RuckusZDWLANStaRetryBytes_Object=MibTableColumn
ruckusZDWLANStaRetryBytes=_RuckusZDWLANStaRetryBytes_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,20),_RuckusZDWLANStaRetryBytes_Type())
ruckusZDWLANStaRetryBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaRetryBytes.setStatus(_A)
_RuckusZDWLANStaSNR_Type=Integer32
_RuckusZDWLANStaSNR_Object=MibTableColumn
ruckusZDWLANStaSNR=_RuckusZDWLANStaSNR_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,21),_RuckusZDWLANStaSNR_Type())
ruckusZDWLANStaSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaSNR.setStatus(_A)
_RuckusZDWLANStaRxDrop_Type=Counter32
_RuckusZDWLANStaRxDrop_Object=MibTableColumn
ruckusZDWLANStaRxDrop=_RuckusZDWLANStaRxDrop_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,22),_RuckusZDWLANStaRxDrop_Type())
ruckusZDWLANStaRxDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaRxDrop.setStatus(_A)
_RuckusZDWLANStaTxDrop_Type=Counter32
_RuckusZDWLANStaTxDrop_Object=MibTableColumn
ruckusZDWLANStaTxDrop=_RuckusZDWLANStaTxDrop_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,23),_RuckusZDWLANStaTxDrop_Type())
ruckusZDWLANStaTxDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaTxDrop.setStatus(_A)
_RuckusZDWLANStaTxError_Type=Counter32
_RuckusZDWLANStaTxError_Object=MibTableColumn
ruckusZDWLANStaTxError=_RuckusZDWLANStaTxError_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,24),_RuckusZDWLANStaTxError_Type())
ruckusZDWLANStaTxError.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaTxError.setStatus(_A)
class _RuckusZDWLANStaVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RuckusZDWLANStaVlanID_Type.__name__=_C
_RuckusZDWLANStaVlanID_Object=MibTableColumn
ruckusZDWLANStaVlanID=_RuckusZDWLANStaVlanID_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,30),_RuckusZDWLANStaVlanID_Type())
ruckusZDWLANStaVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaVlanID.setStatus(_A)
_RuckusZDWLANStaAuthMode_Type=DisplayString
_RuckusZDWLANStaAuthMode_Object=MibTableColumn
ruckusZDWLANStaAuthMode=_RuckusZDWLANStaAuthMode_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,80),_RuckusZDWLANStaAuthMode_Type())
ruckusZDWLANStaAuthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaAuthMode.setStatus(_A)
_RuckusZDWLANStaSignalStrength_Type=Integer32
_RuckusZDWLANStaSignalStrength_Object=MibTableColumn
ruckusZDWLANStaSignalStrength=_RuckusZDWLANStaSignalStrength_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,1,1,81),_RuckusZDWLANStaSignalStrength_Type())
ruckusZDWLANStaSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANStaSignalStrength.setStatus(_A)
if mibBuilder.loadTexts:ruckusZDWLANStaSignalStrength.setUnits('dBm')
_RuckusZDWiredStaTable_Object=MibTable
ruckusZDWiredStaTable=_RuckusZDWiredStaTable_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,2))
if mibBuilder.loadTexts:ruckusZDWiredStaTable.setStatus(_A)
_RuckusZDWiredStaEntry_Object=MibTableRow
ruckusZDWiredStaEntry=_RuckusZDWiredStaEntry_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,2,1))
ruckusZDWiredStaEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:ruckusZDWiredStaEntry.setStatus(_A)
_RuckusZDWiredStaMacAddr_Type=MacAddress
_RuckusZDWiredStaMacAddr_Object=MibTableColumn
ruckusZDWiredStaMacAddr=_RuckusZDWiredStaMacAddr_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,2,1,1),_RuckusZDWiredStaMacAddr_Type())
ruckusZDWiredStaMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWiredStaMacAddr.setStatus(_A)
_RuckusZDWiredStaAPMacAddr_Type=MacAddress
_RuckusZDWiredStaAPMacAddr_Object=MibTableColumn
ruckusZDWiredStaAPMacAddr=_RuckusZDWiredStaAPMacAddr_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,2,1,3),_RuckusZDWiredStaAPMacAddr_Type())
ruckusZDWiredStaAPMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWiredStaAPMacAddr.setStatus(_A)
_RuckusZDWiredStaIPAddr_Type=IpAddress
_RuckusZDWiredStaIPAddr_Object=MibTableColumn
ruckusZDWiredStaIPAddr=_RuckusZDWiredStaIPAddr_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,2,1,5),_RuckusZDWiredStaIPAddr_Type())
ruckusZDWiredStaIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWiredStaIPAddr.setStatus(_A)
class _RuckusZDWiredStaIPV6Addr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusZDWiredStaIPV6Addr_Type.__name__=_E
_RuckusZDWiredStaIPV6Addr_Object=MibTableColumn
ruckusZDWiredStaIPV6Addr=_RuckusZDWiredStaIPV6Addr_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,2,1,6),_RuckusZDWiredStaIPV6Addr_Type())
ruckusZDWiredStaIPV6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWiredStaIPV6Addr.setStatus(_A)
class _RuckusZDWiredStaVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RuckusZDWiredStaVlanID_Type.__name__=_C
_RuckusZDWiredStaVlanID_Object=MibTableColumn
ruckusZDWiredStaVlanID=_RuckusZDWiredStaVlanID_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,2,1,8),_RuckusZDWiredStaVlanID_Type())
ruckusZDWiredStaVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWiredStaVlanID.setStatus(_A)
class _RuckusZDWiredStaUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RuckusZDWiredStaUserName_Type.__name__=_L
_RuckusZDWiredStaUserName_Object=MibTableColumn
ruckusZDWiredStaUserName=_RuckusZDWiredStaUserName_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,2,1,9),_RuckusZDWiredStaUserName_Type())
ruckusZDWiredStaUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWiredStaUserName.setStatus(_A)
class _RuckusZDWiredStaAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('Unauthorized',0),('Authorized',1),('Authorized-as-guest',2)))
_RuckusZDWiredStaAuthState_Type.__name__=_C
_RuckusZDWiredStaAuthState_Object=MibTableColumn
ruckusZDWiredStaAuthState=_RuckusZDWiredStaAuthState_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,2,1,10),_RuckusZDWiredStaAuthState_Type())
ruckusZDWiredStaAuthState.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWiredStaAuthState.setStatus(_A)
_RuckusZDWiredStaAssocTime_Type=TimeTicks
_RuckusZDWiredStaAssocTime_Object=MibTableColumn
ruckusZDWiredStaAssocTime=_RuckusZDWiredStaAssocTime_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,2,1,11),_RuckusZDWiredStaAssocTime_Type())
ruckusZDWiredStaAssocTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWiredStaAssocTime.setStatus(_A)
_RuckusZDWiredStaRxPkts_Type=Counter32
_RuckusZDWiredStaRxPkts_Object=MibTableColumn
ruckusZDWiredStaRxPkts=_RuckusZDWiredStaRxPkts_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,2,1,15),_RuckusZDWiredStaRxPkts_Type())
ruckusZDWiredStaRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWiredStaRxPkts.setStatus(_A)
_RuckusZDWiredStaRxBytes_Type=Counter64
_RuckusZDWiredStaRxBytes_Object=MibTableColumn
ruckusZDWiredStaRxBytes=_RuckusZDWiredStaRxBytes_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,2,1,16),_RuckusZDWiredStaRxBytes_Type())
ruckusZDWiredStaRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWiredStaRxBytes.setStatus(_A)
_RuckusZDWiredStaTxPkts_Type=Counter32
_RuckusZDWiredStaTxPkts_Object=MibTableColumn
ruckusZDWiredStaTxPkts=_RuckusZDWiredStaTxPkts_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,2,1,17),_RuckusZDWiredStaTxPkts_Type())
ruckusZDWiredStaTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWiredStaTxPkts.setStatus(_A)
_RuckusZDWiredStaTxBytes_Type=Counter64
_RuckusZDWiredStaTxBytes_Object=MibTableColumn
ruckusZDWiredStaTxBytes=_RuckusZDWiredStaTxBytes_Object((1,3,6,1,4,1,25053,1,2,2,1,1,3,2,1,18),_RuckusZDWiredStaTxBytes_Type())
ruckusZDWiredStaTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWiredStaTxBytes.setStatus(_A)
_RuckusZDWLANRogueInfo_ObjectIdentity=ObjectIdentity
ruckusZDWLANRogueInfo=_RuckusZDWLANRogueInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,2,2,1,1,4))
_RuckusZDWLANRogueTable_Object=MibTable
ruckusZDWLANRogueTable=_RuckusZDWLANRogueTable_Object((1,3,6,1,4,1,25053,1,2,2,1,1,4,1))
if mibBuilder.loadTexts:ruckusZDWLANRogueTable.setStatus(_A)
_RuckusZDWLANRogueEntry_Object=MibTableRow
ruckusZDWLANRogueEntry=_RuckusZDWLANRogueEntry_Object((1,3,6,1,4,1,25053,1,2,2,1,1,4,1,1))
ruckusZDWLANRogueEntry.setIndexNames((0,_D,_c))
if mibBuilder.loadTexts:ruckusZDWLANRogueEntry.setStatus(_A)
_RuckusZDWLANRogueMacAddr_Type=MacAddress
_RuckusZDWLANRogueMacAddr_Object=MibTableColumn
ruckusZDWLANRogueMacAddr=_RuckusZDWLANRogueMacAddr_Object((1,3,6,1,4,1,25053,1,2,2,1,1,4,1,1,1),_RuckusZDWLANRogueMacAddr_Type())
ruckusZDWLANRogueMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANRogueMacAddr.setStatus(_A)
_RuckusZDWLANRogueSSID_Type=RuckusSSID
_RuckusZDWLANRogueSSID_Object=MibTableColumn
ruckusZDWLANRogueSSID=_RuckusZDWLANRogueSSID_Object((1,3,6,1,4,1,25053,1,2,2,1,1,4,1,1,2),_RuckusZDWLANRogueSSID_Type())
ruckusZDWLANRogueSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANRogueSSID.setStatus(_A)
class _RuckusZDWLANRogueRadioType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_S,0),(_H,1),(_I,2),(_J,3),(_K,4)))
_RuckusZDWLANRogueRadioType_Type.__name__=_C
_RuckusZDWLANRogueRadioType_Object=MibTableColumn
ruckusZDWLANRogueRadioType=_RuckusZDWLANRogueRadioType_Object((1,3,6,1,4,1,25053,1,2,2,1,1,4,1,1,3),_RuckusZDWLANRogueRadioType_Type())
ruckusZDWLANRogueRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANRogueRadioType.setStatus(_A)
_RuckusZDWLANRogueChannel_Type=Unsigned32
_RuckusZDWLANRogueChannel_Object=MibTableColumn
ruckusZDWLANRogueChannel=_RuckusZDWLANRogueChannel_Object((1,3,6,1,4,1,25053,1,2,2,1,1,4,1,1,4),_RuckusZDWLANRogueChannel_Type())
ruckusZDWLANRogueChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANRogueChannel.setStatus(_A)
_RuckusZDWLANRogueRSSI_Type=Integer32
_RuckusZDWLANRogueRSSI_Object=MibTableColumn
ruckusZDWLANRogueRSSI=_RuckusZDWLANRogueRSSI_Object((1,3,6,1,4,1,25053,1,2,2,1,1,4,1,1,5),_RuckusZDWLANRogueRSSI_Type())
ruckusZDWLANRogueRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANRogueRSSI.setStatus(_A)
class _RuckusZDWLANRogueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ap',0),('ad-hoc',1)))
_RuckusZDWLANRogueType_Type.__name__=_C
_RuckusZDWLANRogueType_Object=MibTableColumn
ruckusZDWLANRogueType=_RuckusZDWLANRogueType_Object((1,3,6,1,4,1,25053,1,2,2,1,1,4,1,1,6),_RuckusZDWLANRogueType_Type())
ruckusZDWLANRogueType.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANRogueType.setStatus(_A)
class _RuckusZDWLANRogueEncrypted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('open',0),('encrypted',1)))
_RuckusZDWLANRogueEncrypted_Type.__name__=_C
_RuckusZDWLANRogueEncrypted_Object=MibTableColumn
ruckusZDWLANRogueEncrypted=_RuckusZDWLANRogueEncrypted_Object((1,3,6,1,4,1,25053,1,2,2,1,1,4,1,1,7),_RuckusZDWLANRogueEncrypted_Type())
ruckusZDWLANRogueEncrypted.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANRogueEncrypted.setStatus(_A)
_RuckusZDWLANRogueSignalStrength_Type=Integer32
_RuckusZDWLANRogueSignalStrength_Object=MibTableColumn
ruckusZDWLANRogueSignalStrength=_RuckusZDWLANRogueSignalStrength_Object((1,3,6,1,4,1,25053,1,2,2,1,1,4,1,1,11),_RuckusZDWLANRogueSignalStrength_Type())
ruckusZDWLANRogueSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANRogueSignalStrength.setStatus(_A)
if mibBuilder.loadTexts:ruckusZDWLANRogueSignalStrength.setUnits('dBm')
_RuckusZDWLANRogueIndex_Type=InterfaceIndex
_RuckusZDWLANRogueIndex_Object=MibTableColumn
ruckusZDWLANRogueIndex=_RuckusZDWLANRogueIndex_Object((1,3,6,1,4,1,25053,1,2,2,1,1,4,1,1,200),_RuckusZDWLANRogueIndex_Type())
ruckusZDWLANRogueIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANRogueIndex.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ruckusZDWLANMIB':ruckusZDWLANMIB,'ruckusZDWLANObjects':ruckusZDWLANObjects,'ruckusZDWLANInfo':ruckusZDWLANInfo,'ruckusZDWLANTable':ruckusZDWLANTable,'ruckusZDWLANEntry':ruckusZDWLANEntry,'ruckusZDWLANSSID':ruckusZDWLANSSID,'ruckusZDWLANDescription':ruckusZDWLANDescription,'ruckusZDWLANAuthentication':ruckusZDWLANAuthentication,'ruckusZDWLANEncryption':ruckusZDWLANEncryption,'ruckusZDWLANIsGuest':ruckusZDWLANIsGuest,'ruckusZDWLANSSIDBcastDisable':ruckusZDWLANSSIDBcastDisable,'ruckusZDWLANVlanID':ruckusZDWLANVlanID,'ruckusZDWLANRateLimitingUp':ruckusZDWLANRateLimitingUp,'ruckusZDWLANRateLimitingDown':ruckusZDWLANRateLimitingDown,'ruckusZDWLANTunnelWLAN':ruckusZDWLANTunnelWLAN,'ruckusZDWLANNumVAP':ruckusZDWLANNumVAP,'ruckusZDWLANNumSta':ruckusZDWLANNumSta,'ruckusZDWLANRxPkts':ruckusZDWLANRxPkts,'ruckusZDWLANRxBytes':ruckusZDWLANRxBytes,'ruckusZDWLANTxPkts':ruckusZDWLANTxPkts,'ruckusZDWLANTxBytes':ruckusZDWLANTxBytes,'ruckusZDWLANAssocNumSta':ruckusZDWLANAssocNumSta,'ruckusZDWLANAuthTotal':ruckusZDWLANAuthTotal,'ruckusZDWLANAuthResp':ruckusZDWLANAuthResp,'ruckusZDWLANAuthSuccessTotal':ruckusZDWLANAuthSuccessTotal,'ruckusZDWLANAuthFail':ruckusZDWLANAuthFail,'ruckusZDWLANAssocTotal':ruckusZDWLANAssocTotal,'ruckusZDWLANAssocResp':ruckusZDWLANAssocResp,'ruckusZDWLANReassocReq':ruckusZDWLANReassocReq,'ruckusZDWLANReassocResp':ruckusZDWLANReassocResp,'ruckusZDWLANAssocSuccess':ruckusZDWLANAssocSuccess,'ruckusZDWLANAssocFail':ruckusZDWLANAssocFail,'ruckusZDWLANAssocDenied':ruckusZDWLANAssocDenied,'ruckusZDWLANDiassocAbnormal':ruckusZDWLANDiassocAbnormal,'ruckusZDWLANDiassocCapacity':ruckusZDWLANDiassocCapacity,'ruckusZDWLANDiassocLeave':ruckusZDWLANDiassocLeave,'ruckusZDWLANDiassocMisc':ruckusZDWLANDiassocMisc,'ruckusZDWLANRxByteRate':ruckusZDWLANRxByteRate,'ruckusZDWLANTxByteRate':ruckusZDWLANTxByteRate,'ruckusZDWLANRxDataFrameOnLan':ruckusZDWLANRxDataFrameOnLan,'ruckusZDWLANRxByteOnLan':ruckusZDWLANRxByteOnLan,'ruckusZDWLANTxByteOnLan':ruckusZDWLANTxByteOnLan,'ruckusZDWLANDownDropFrame':ruckusZDWLANDownDropFrame,'ruckusZDWLANDownRetxFrame':ruckusZDWLANDownRetxFrame,'ruckusZDWLANDownTotalFrame':ruckusZDWLANDownTotalFrame,'ruckusZDWLANDownTotalErrFrame':ruckusZDWLANDownTotalErrFrame,'ruckusZDWLANUpTotalFrame':ruckusZDWLANUpTotalFrame,'ruckusZDWLANUpDropFrame':ruckusZDWLANUpDropFrame,'ruckusZDWLANUpRetxFrame':ruckusZDWLANUpRetxFrame,'ruckusZDWLANNAME':ruckusZDWLANNAME,_N:ruckusZDWLANIndex,'ruckusZDWLANAPInfo':ruckusZDWLANAPInfo,'ruckusZDWLANAPTable':ruckusZDWLANAPTable,'ruckusZDWLANAPEntry':ruckusZDWLANAPEntry,_O:ruckusZDWLANAPMacAddr,'ruckusZDWLANAPDescription':ruckusZDWLANAPDescription,'ruckusZDWLANAPStatus':ruckusZDWLANAPStatus,'ruckusZDWLANAPModel':ruckusZDWLANAPModel,'ruckusZDWLANAPSerialNumber':ruckusZDWLANAPSerialNumber,'ruckusZDWLANAPUptime':ruckusZDWLANAPUptime,'ruckusZDWLANAPSWversion':ruckusZDWLANAPSWversion,'ruckusZDWLANAPHWversion':ruckusZDWLANAPHWversion,'ruckusZDWLANAPIPAddr':ruckusZDWLANAPIPAddr,'ruckusZDWLANAPNumRadios':ruckusZDWLANAPNumRadios,'ruckusZDWLANAPNumVAP':ruckusZDWLANAPNumVAP,'ruckusZDWLANAPNumSta':ruckusZDWLANAPNumSta,'ruckusZDWLANAPNumRogues':ruckusZDWLANAPNumRogues,'ruckusZDWLANAPConnectionMode':ruckusZDWLANAPConnectionMode,'ruckusZDWLANAPMeshEnable':ruckusZDWLANAPMeshEnable,'ruckusZDWLANAPMeshHops':ruckusZDWLANAPMeshHops,'ruckusZDWLANAPMeshType':ruckusZDWLANAPMeshType,'ruckusZDWLANAPLANStatsRXByte':ruckusZDWLANAPLANStatsRXByte,'ruckusZDWLANAPLANStatsRXPkt':ruckusZDWLANAPLANStatsRXPkt,'ruckusZDWLANAPLANStatsRXPktErr':ruckusZDWLANAPLANStatsRXPktErr,'ruckusZDWLANAPLANStatsRXPKTSucc':ruckusZDWLANAPLANStatsRXPKTSucc,'ruckusZDWLANAPLANStatsTXByte':ruckusZDWLANAPLANStatsTXByte,'ruckusZDWLANAPLANStatsTXPkt':ruckusZDWLANAPLANStatsTXPkt,'ruckusZDWLANAPMemUtil':ruckusZDWLANAPMemUtil,'ruckusZDWLANAPMemTotal':ruckusZDWLANAPMemTotal,'ruckusZDWLANAPCPUUtil':ruckusZDWLANAPCPUUtil,'ruckusZDWLANAPFWSize':ruckusZDWLANAPFWSize,'ruckusZDWLANAPFWAvail':ruckusZDWLANAPFWAvail,'ruckusZDWLANAPMultipleVlanCapability':ruckusZDWLANAPMultipleVlanCapability,'ruckusZDWLANAP11bCapable':ruckusZDWLANAP11bCapable,'ruckusZDWLANAP11gCapable':ruckusZDWLANAP11gCapable,'ruckusZDWLANAPMultiModeAccessStatus':ruckusZDWLANAPMultiModeAccessStatus,'ruckusZDWLANAPEthStateChange':ruckusZDWLANAPEthStateChange,'ruckusZDWLANAPSyncConf':ruckusZDWLANAPSyncConf,'ruckusZDWLANAPUpgrade':ruckusZDWLANAPUpgrade,'ruckusZDWLANAPFirstJoinTime':ruckusZDWLANAPFirstJoinTime,'ruckusZDWLANAPLastBootTime':ruckusZDWLANAPLastBootTime,'ruckusZDWLANAPLastUpgradeTime':ruckusZDWLANAPLastUpgradeTime,'ruckusZDWLANAPLastConfSyncTime':ruckusZDWLANAPLastConfSyncTime,'ruckusZDWLANAPLANStatsRXPKTBcast':ruckusZDWLANAPLANStatsRXPKTBcast,'ruckusZDWLANAPLANStatsRXPKTMcast':ruckusZDWLANAPLANStatsRXPKTMcast,'ruckusZDWLANAPLANStatsRXPKTUcast':ruckusZDWLANAPLANStatsRXPKTUcast,'ruckusZDWLANAPLANStatsTXPKTBcast':ruckusZDWLANAPLANStatsTXPKTBcast,'ruckusZDWLANAPLANStatsTXPKTMcast':ruckusZDWLANAPLANStatsTXPKTMcast,'ruckusZDWLANAPLANStatsTXPKTUcast':ruckusZDWLANAPLANStatsTXPKTUcast,'ruckusZDWLANAPLANStatsDropped':ruckusZDWLANAPLANStatsDropped,'ruckusZDWLANAPMeshUpPortCntUpdown':ruckusZDWLANAPMeshUpPortCntUpdown,'ruckusZDWLANAPMeshDownPortCntUpdown':ruckusZDWLANAPMeshDownPortCntUpdown,'ruckusZDWLANAPTxFrameDropped':ruckusZDWLANAPTxFrameDropped,'ruckusZDWLANAPTxFrameError':ruckusZDWLANAPTxFrameError,'ruckusZDWLANAPCoverageTech':ruckusZDWLANAPCoverageTech,'ruckusZDWLANAPStaTxBytes':ruckusZDWLANAPStaTxBytes,'ruckusZDWLANAPStaRxBytes':ruckusZDWLANAPStaRxBytes,'ruckusZDWLANAPNetmask':ruckusZDWLANAPNetmask,'ruckusZDWLANAPGateway':ruckusZDWLANAPGateway,'ruckusZDWLANAPDNS1':ruckusZDWLANAPDNS1,'ruckusZDWLANAPDNS2':ruckusZDWLANAPDNS2,'ruckusZDWLANAPTotalUser':ruckusZDWLANAPTotalUser,'ruckusZDWLANAPLANStatsRXByteRate':ruckusZDWLANAPLANStatsRXByteRate,'ruckusZDWLANAPLANStatsTXByteRate':ruckusZDWLANAPLANStatsTXByteRate,'ruckusZDWLANAPRadioStatsTable':ruckusZDWLANAPRadioStatsTable,'ruckusZDWLANAPRadioStatsEntry':ruckusZDWLANAPRadioStatsEntry,_Q:ruckusZDWLANAPRadioStatsAPMacAddr,_R:ruckusZDWLANAPRadioStatsRadioIndex,'ruckusZDWLANAPRadioStatsRadioType':ruckusZDWLANAPRadioStatsRadioType,'ruckusZDWLANAPRadioStatsChannel':ruckusZDWLANAPRadioStatsChannel,'ruckusZDWLANAPRadioStatsTxPower':ruckusZDWLANAPRadioStatsTxPower,'ruckusZDWLANAPRadioStatsMeshEnable':ruckusZDWLANAPRadioStatsMeshEnable,'ruckusZDWLANAPRadioStatsNumVAP':ruckusZDWLANAPRadioStatsNumVAP,'ruckusZDWLANAPRadioStatsNumSta':ruckusZDWLANAPRadioStatsNumSta,'ruckusZDWLANAPRadioStatsAvgStaRSSI':ruckusZDWLANAPRadioStatsAvgStaRSSI,'ruckusZDWLANAPRadioStatsRxPkts':ruckusZDWLANAPRadioStatsRxPkts,'ruckusZDWLANAPRadioStatsRxBytes':ruckusZDWLANAPRadioStatsRxBytes,'ruckusZDWLANAPRadioStatsRxMulticast':ruckusZDWLANAPRadioStatsRxMulticast,'ruckusZDWLANAPRadioStatsTxPkts':ruckusZDWLANAPRadioStatsTxPkts,'ruckusZDWLANAPRadioStatsTxBytes':ruckusZDWLANAPRadioStatsTxBytes,'ruckusZDWLANAPRadioStatsTxMulticast':ruckusZDWLANAPRadioStatsTxMulticast,'ruckusZDWLANAPRadioStatsTxFail':ruckusZDWLANAPRadioStatsTxFail,'ruckusZDWLANAPRadioStatsTxRetries':ruckusZDWLANAPRadioStatsTxRetries,'ruckusZDWLANAPRadioStatsPowerMgmt':ruckusZDWLANAPRadioStatsPowerMgmt,'ruckusZDWLANAPRadioStatsMaxSta':ruckusZDWLANAPRadioStatsMaxSta,'ruckusZDWLANAPRadioStatsFrameErrorRate':ruckusZDWLANAPRadioStatsFrameErrorRate,'ruckusZDWLANAPRadioStatsFrameRetryRate':ruckusZDWLANAPRadioStatsFrameRetryRate,'ruckusZDWLANAPRadioStatsMonitoredTime':ruckusZDWLANAPRadioStatsMonitoredTime,'ruckusZDWLANAPRadioStatsTotalAssocTime':ruckusZDWLANAPRadioStatsTotalAssocTime,'ruckusZDWLANAPRadioStatsAuthReq':ruckusZDWLANAPRadioStatsAuthReq,'ruckusZDWLANAPRadioStatsAuthResp':ruckusZDWLANAPRadioStatsAuthResp,'ruckusZDWLANAPRadioStatsAuthSuccess':ruckusZDWLANAPRadioStatsAuthSuccess,'ruckusZDWLANAPRadioStatsAuthFail':ruckusZDWLANAPRadioStatsAuthFail,'ruckusZDWLANAPRadioStatsAssocReq':ruckusZDWLANAPRadioStatsAssocReq,'ruckusZDWLANAPRadioStatsAssocResp':ruckusZDWLANAPRadioStatsAssocResp,'ruckusZDWLANAPRadioStatsReassocReq':ruckusZDWLANAPRadioStatsReassocReq,'ruckusZDWLANAPRadioStatsReassocResp':ruckusZDWLANAPRadioStatsReassocResp,'ruckusZDWLANAPRadioStatsAssocSuccess':ruckusZDWLANAPRadioStatsAssocSuccess,'ruckusZDWLANAPRadioStatsAssocFail':ruckusZDWLANAPRadioStatsAssocFail,'ruckusZDWLANAPRadioStatsAssocDenied':ruckusZDWLANAPRadioStatsAssocDenied,'ruckusZDWLANAPRadioStatsDiassocAbnormal':ruckusZDWLANAPRadioStatsDiassocAbnormal,'ruckusZDWLANAPRadioStatsDiassocCapacity':ruckusZDWLANAPRadioStatsDiassocCapacity,'ruckusZDWLANAPRadioStatsDiassocLeave':ruckusZDWLANAPRadioStatsDiassocLeave,'ruckusZDWLANAPRadioStatsDiassocMisc':ruckusZDWLANAPRadioStatsDiassocMisc,'ruckusZDWLANAPRadioStatsResourceUtil':ruckusZDWLANAPRadioStatsResourceUtil,'ruckusZDWLANAPRadioStatsRxSignalFrm':ruckusZDWLANAPRadioStatsRxSignalFrm,'ruckusZDWLANAPRadioStatsTxSignalFrm':ruckusZDWLANAPRadioStatsTxSignalFrm,'ruckusZDWLANAPRadioStatsTotalSignalFrm':ruckusZDWLANAPRadioStatsTotalSignalFrm,'ruckusZDWLANAPRadioStatsAntennaGain':ruckusZDWLANAPRadioStatsAntennaGain,'ruckusZDWLANAPRadioStatsBeaconPeriod':ruckusZDWLANAPRadioStatsBeaconPeriod,'ruckusZDWLANAPRadioStatsRTSThreshold':ruckusZDWLANAPRadioStatsRTSThreshold,'ruckusZDWLANAPRadioStatsFragThreshold':ruckusZDWLANAPRadioStatsFragThreshold,'ruckusZDWLANVapTable':ruckusZDWLANVapTable,'ruckusZDWLANVapEntry':ruckusZDWLANVapEntry,_U:ruckusZDWLANVapBSSID,'ruckusZDWLANVapPAPAddr':ruckusZDWLANVapPAPAddr,'ruckusZDWLANVapSSID':ruckusZDWLANVapSSID,'ruckusZDWLANVapLanRxBytes':ruckusZDWLANVapLanRxBytes,'ruckusZDWLANVapLanTxBytes':ruckusZDWLANVapLanTxBytes,'ruckusZDWLANVapWlanRxBytes':ruckusZDWLANVapWlanRxBytes,'ruckusZDWLANVapWlanTxBytes':ruckusZDWLANVapWlanTxBytes,'ruckusZDWLANVapWlanRxErrorPkt':ruckusZDWLANVapWlanRxErrorPkt,'ruckusZDWLANVapWlanRxUnicastPkt':ruckusZDWLANVapWlanRxUnicastPkt,'ruckusZDWLANVapWlanTxUnicastPkt':ruckusZDWLANVapWlanTxUnicastPkt,'ruckusZDWLANVapWlanRxPkt':ruckusZDWLANVapWlanRxPkt,'ruckusZDWLANVapWlanRxDropPkt':ruckusZDWLANVapWlanRxDropPkt,'ruckusZDWLANVapWlanTxErrPkt':ruckusZDWLANVapWlanTxErrPkt,'ruckusZDWLANVapWlanTxPkt':ruckusZDWLANVapWlanTxPkt,'ruckusZDWLANVapWlanTxDropPkt':ruckusZDWLANVapWlanTxDropPkt,'ruckusZDWLANIfTable':ruckusZDWLANIfTable,'ruckusZDWLANIfEntry':ruckusZDWLANIfEntry,_V:ruckusZDWLANAPMac,_W:ruckusZDWLANAPIfIndex,'ruckusZDWLANAPIfDescr':ruckusZDWLANAPIfDescr,'ruckusZDWLANAPIfType':ruckusZDWLANAPIfType,'ruckusZDWLANAPIfMtu':ruckusZDWLANAPIfMtu,'ruckusZDWLANAPIfSpeed':ruckusZDWLANAPIfSpeed,'ruckusZDWLANAPIfPhysAddress':ruckusZDWLANAPIfPhysAddress,'ruckusZDWLANAPIfAdminStatus':ruckusZDWLANAPIfAdminStatus,'ruckusZDWLANAPIfOperStatus':ruckusZDWLANAPIfOperStatus,'ruckusZDWLANAPIfInOctets':ruckusZDWLANAPIfInOctets,'ruckusZDWLANAPIfInUcastPkts':ruckusZDWLANAPIfInUcastPkts,'ruckusZDWLANAPIfInNUcastPkts':ruckusZDWLANAPIfInNUcastPkts,'ruckusZDWLANAPIfInDiscards':ruckusZDWLANAPIfInDiscards,'ruckusZDWLANAPIfInErrors':ruckusZDWLANAPIfInErrors,'ruckusZDWLANAPIfInUnknownProtos':ruckusZDWLANAPIfInUnknownProtos,'ruckusZDWLANAPIfOutOctets':ruckusZDWLANAPIfOutOctets,'ruckusZDWLANAPIfOutUcastPkts':ruckusZDWLANAPIfOutUcastPkts,'ruckusZDWLANAPIfOutNUcastPkts':ruckusZDWLANAPIfOutNUcastPkts,'ruckusZDWLANAPIfOutDiscards':ruckusZDWLANAPIfOutDiscards,'ruckusZDWLANAPIfOutErrors':ruckusZDWLANAPIfOutErrors,'ruckusZDWLANAPIfName':ruckusZDWLANAPIfName,'ruckusZDWLANAPIfNameDefined':ruckusZDWLANAPIfNameDefined,'ruckusZDWLANAPEthStatusTable':ruckusZDWLANAPEthStatusTable,'ruckusZDWLANAPEthStatusEntry':ruckusZDWLANAPEthStatusEntry,_Y:ruckusZDWLANAPMacAddress,_Z:ruckusZDWLANAPEthPortId,'ruckusZDWLANAPEthIfname':ruckusZDWLANAPEthIfname,'ruckusZDWLANAPEthDot1xStatus':ruckusZDWLANAPEthDot1xStatus,'ruckusZDWLANAPEthLogicalStatus':ruckusZDWLANAPEthLogicalStatus,'ruckusZDWLANAPEthPhyStatus':ruckusZDWLANAPEthPhyStatus,'ruckusZDWLANAPEthPhyIfSpeed':ruckusZDWLANAPEthPhyIfSpeed,'ruckusZDWLANAPEthPhyLinkStatus':ruckusZDWLANAPEthPhyLinkStatus,'ruckusZDWLANAPEthLabel':ruckusZDWLANAPEthLabel,'ruckusZDWLANStaInfo':ruckusZDWLANStaInfo,'ruckusZDWLANStaTable':ruckusZDWLANStaTable,'ruckusZDWLANStaEntry':ruckusZDWLANStaEntry,_a:ruckusZDWLANStaMacAddr,'ruckusZDWLANStaAPMacAddr':ruckusZDWLANStaAPMacAddr,'ruckusZDWLANStaBSSID':ruckusZDWLANStaBSSID,'ruckusZDWLANStaSSID':ruckusZDWLANStaSSID,'ruckusZDWLANStaUser':ruckusZDWLANStaUser,'ruckusZDWLANStaRadioType':ruckusZDWLANStaRadioType,'ruckusZDWLANStaChannel':ruckusZDWLANStaChannel,'ruckusZDWLANStaIPAddr':ruckusZDWLANStaIPAddr,'ruckusZDWLANStaAvgSNR':ruckusZDWLANStaAvgSNR,'ruckusZDWLANStaRxPkts':ruckusZDWLANStaRxPkts,'ruckusZDWLANStaRxBytes':ruckusZDWLANStaRxBytes,'ruckusZDWLANStaTxPkts':ruckusZDWLANStaTxPkts,'ruckusZDWLANStaTxBytes':ruckusZDWLANStaTxBytes,'ruckusZDWLANStaRetries':ruckusZDWLANStaRetries,'ruckusZDWLANStaAssocTime':ruckusZDWLANStaAssocTime,'ruckusZDWLANStaRxError':ruckusZDWLANStaRxError,'ruckusZDWLANStaTxSuccess':ruckusZDWLANStaTxSuccess,'ruckusZDWLANSta11bgReassoc':ruckusZDWLANSta11bgReassoc,'ruckusZDWLANStaAssocTimestamp':ruckusZDWLANStaAssocTimestamp,'ruckusZDWLANStaRetryBytes':ruckusZDWLANStaRetryBytes,'ruckusZDWLANStaSNR':ruckusZDWLANStaSNR,'ruckusZDWLANStaRxDrop':ruckusZDWLANStaRxDrop,'ruckusZDWLANStaTxDrop':ruckusZDWLANStaTxDrop,'ruckusZDWLANStaTxError':ruckusZDWLANStaTxError,'ruckusZDWLANStaVlanID':ruckusZDWLANStaVlanID,'ruckusZDWLANStaAuthMode':ruckusZDWLANStaAuthMode,'ruckusZDWLANStaSignalStrength':ruckusZDWLANStaSignalStrength,'ruckusZDWiredStaTable':ruckusZDWiredStaTable,'ruckusZDWiredStaEntry':ruckusZDWiredStaEntry,_b:ruckusZDWiredStaMacAddr,'ruckusZDWiredStaAPMacAddr':ruckusZDWiredStaAPMacAddr,'ruckusZDWiredStaIPAddr':ruckusZDWiredStaIPAddr,'ruckusZDWiredStaIPV6Addr':ruckusZDWiredStaIPV6Addr,'ruckusZDWiredStaVlanID':ruckusZDWiredStaVlanID,'ruckusZDWiredStaUserName':ruckusZDWiredStaUserName,'ruckusZDWiredStaAuthState':ruckusZDWiredStaAuthState,'ruckusZDWiredStaAssocTime':ruckusZDWiredStaAssocTime,'ruckusZDWiredStaRxPkts':ruckusZDWiredStaRxPkts,'ruckusZDWiredStaRxBytes':ruckusZDWiredStaRxBytes,'ruckusZDWiredStaTxPkts':ruckusZDWiredStaTxPkts,'ruckusZDWiredStaTxBytes':ruckusZDWiredStaTxBytes,'ruckusZDWLANRogueInfo':ruckusZDWLANRogueInfo,'ruckusZDWLANRogueTable':ruckusZDWLANRogueTable,'ruckusZDWLANRogueEntry':ruckusZDWLANRogueEntry,'ruckusZDWLANRogueMacAddr':ruckusZDWLANRogueMacAddr,'ruckusZDWLANRogueSSID':ruckusZDWLANRogueSSID,'ruckusZDWLANRogueRadioType':ruckusZDWLANRogueRadioType,'ruckusZDWLANRogueChannel':ruckusZDWLANRogueChannel,'ruckusZDWLANRogueRSSI':ruckusZDWLANRogueRSSI,'ruckusZDWLANRogueType':ruckusZDWLANRogueType,'ruckusZDWLANRogueEncrypted':ruckusZDWLANRogueEncrypted,'ruckusZDWLANRogueSignalStrength':ruckusZDWLANRogueSignalStrength,_c:ruckusZDWLANRogueIndex})