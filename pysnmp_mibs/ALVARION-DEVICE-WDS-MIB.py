_AJ='alvarionDeviceWdsNetworkScanMIBGroup'
_AI='alvarionDeviceWdsLinkMIBGroup'
_AH='alvarionDeviceWdsGroupMIBGroup'
_AG='alvarionDeviceWdsRadioMIBGroup'
_AF='alvarionDeviceWdsInfoMIBGroup'
_AE='coDevWDSScanAvailable'
_AD='coDevWDSScanMode'
_AC='coDevWDSScanSNR'
_AB='coDevWDSScanChannel'
_AA='coDevWDSScanPeerMacAddress'
_A9='coDevWDSScanGroupId'
_A8='coDevWDSLinkStsPktsRxRate54'
_A7='coDevWDSLinkStsPktsRxRate48'
_A6='coDevWDSLinkStsPktsRxRate36'
_A5='coDevWDSLinkStsPktsRxRate24'
_A4='coDevWDSLinkStsPktsRxRate18'
_A3='coDevWDSLinkStsPktsRxRate12'
_A2='coDevWDSLinkStsPktsRxRate9'
_A1='coDevWDSLinkStsPktsRxRate6'
_A0='coDevWDSLinkStsPktsRxRate11'
_z='coDevWDSLinkStsPktsRxRate5dot5'
_y='coDevWDSLinkStsPktsRxRate2'
_x='coDevWDSLinkStsPktsRxRate1'
_w='coDevWDSLinkStsPktsTxRate54'
_v='coDevWDSLinkStsPktsTxRate48'
_u='coDevWDSLinkStsPktsTxRate36'
_t='coDevWDSLinkStsPktsTxRate24'
_s='coDevWDSLinkStsPktsTxRate18'
_r='coDevWDSLinkStsPktsTxRate12'
_q='coDevWDSLinkStsPktsTxRate9'
_p='coDevWDSLinkStsPktsTxRate6'
_o='coDevWDSLinkStsPktsTxRate11'
_n='coDevWDSLinkStsPktsTxRate5dot5'
_m='coDevWDSLinkStsPktsTxRate2'
_l='coDevWDSLinkStsPktsTxRate1'
_k='coDevWDSLinkStaIfIndex'
_j='coDevWDSLinkStaRxRate'
_i='coDevWDSLinkStaTxRate'
_h='coDevWDSLinkStaSNR'
_g='coDevWDSLinkStaIdleTime'
_f='coDevWDSLinkStaEncryption'
_e='coDevWDSLinkStaAuthorized'
_d='coDevWDSLinkStaMaster'
_c='coDevWDSLinkStaPeerMacAddress'
_b='coDevWDSLinkStaRadio'
_a='coDevWDSLinkStaState'
_Z='coDevWDSGroupDynamicGroupId'
_Y='coDevWDSGroupDynamicMode'
_X='coDevWDSGroupSecurity'
_W='coDevWDSGroupState'
_V='coDevWDSGroupName'
_U='coDevWDSRadioQoS'
_T='coDevWDSRadioAckDistance'
_S='coDevWDSInfoMaxNumberOfGroup'
_R='coDeviceWDSLinkStatsRatesEntry'
_Q='coDevWDSScanPeerIndex'
_P='coDevWDSScanRadioIndex'
_O='500Kb/s'
_N='coDevWDSLinkStaIndex'
_M='alternateMaster'
_L='master'
_K='coDevWDSRadioIndex'
_J='DisplayString'
_I='coDevWDSGroupIndex'
_H='Unsigned32'
_G='not-accessible'
_F='coDevDisIndex'
_E='ALVARION-DEVICE-MIB'
_D='Integer32'
_C='read-only'
_B='ALVARION-DEVICE-WDS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
coDevDisIndex,=mibBuilder.importSymbols(_E,_F)
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','TextualConvention','TruthValue')
alvarionDeviceWdsMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,34))
_AlvarionDeviceWdsMIBObjects_ObjectIdentity=ObjectIdentity
alvarionDeviceWdsMIBObjects=_AlvarionDeviceWdsMIBObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,34,1))
_CoDeviceWDSInfoGroup_ObjectIdentity=ObjectIdentity
coDeviceWDSInfoGroup=_CoDeviceWDSInfoGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,34,1,2))
_CoDeviceWdsInfoTable_Object=MibTable
coDeviceWdsInfoTable=_CoDeviceWdsInfoTable_Object((1,3,6,1,4,1,12394,1,10,5,34,1,2,1))
if mibBuilder.loadTexts:coDeviceWdsInfoTable.setStatus(_A)
_CoDeviceWdsInfoEntry_Object=MibTableRow
coDeviceWdsInfoEntry=_CoDeviceWdsInfoEntry_Object((1,3,6,1,4,1,12394,1,10,5,34,1,2,1,1))
coDeviceWdsInfoEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:coDeviceWdsInfoEntry.setStatus(_A)
class _CoDevWDSInfoMaxNumberOfGroup_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_CoDevWDSInfoMaxNumberOfGroup_Type.__name__=_H
_CoDevWDSInfoMaxNumberOfGroup_Object=MibTableColumn
coDevWDSInfoMaxNumberOfGroup=_CoDevWDSInfoMaxNumberOfGroup_Object((1,3,6,1,4,1,12394,1,10,5,34,1,2,1,1,1),_CoDevWDSInfoMaxNumberOfGroup_Type())
coDevWDSInfoMaxNumberOfGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSInfoMaxNumberOfGroup.setStatus(_A)
_CoDeviceWDSRadioGroup_ObjectIdentity=ObjectIdentity
coDeviceWDSRadioGroup=_CoDeviceWDSRadioGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,34,1,3))
_CoDeviceWDSRadioTable_Object=MibTable
coDeviceWDSRadioTable=_CoDeviceWDSRadioTable_Object((1,3,6,1,4,1,12394,1,10,5,34,1,3,1))
if mibBuilder.loadTexts:coDeviceWDSRadioTable.setStatus(_A)
_CoDeviceWDSRadioEntry_Object=MibTableRow
coDeviceWDSRadioEntry=_CoDeviceWDSRadioEntry_Object((1,3,6,1,4,1,12394,1,10,5,34,1,3,1,1))
coDeviceWDSRadioEntry.setIndexNames((0,_E,_F),(0,_B,_K))
if mibBuilder.loadTexts:coDeviceWDSRadioEntry.setStatus(_A)
class _CoDevWDSRadioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_CoDevWDSRadioIndex_Type.__name__=_D
_CoDevWDSRadioIndex_Object=MibTableColumn
coDevWDSRadioIndex=_CoDevWDSRadioIndex_Object((1,3,6,1,4,1,12394,1,10,5,34,1,3,1,1,1),_CoDevWDSRadioIndex_Type())
coDevWDSRadioIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:coDevWDSRadioIndex.setStatus(_A)
_CoDevWDSRadioAckDistance_Type=Unsigned32
_CoDevWDSRadioAckDistance_Object=MibTableColumn
coDevWDSRadioAckDistance=_CoDevWDSRadioAckDistance_Object((1,3,6,1,4,1,12394,1,10,5,34,1,3,1,1,2),_CoDevWDSRadioAckDistance_Type())
coDevWDSRadioAckDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSRadioAckDistance.setStatus(_A)
if mibBuilder.loadTexts:coDevWDSRadioAckDistance.setUnits('km')
class _CoDevWDSRadioQoS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('disabled',1),('vlan',2),('veryHigh',3),('high',4),('normal',5),('low',6),('diffSrv',7),('tos',8),('ipQos',9)))
_CoDevWDSRadioQoS_Type.__name__=_D
_CoDevWDSRadioQoS_Object=MibTableColumn
coDevWDSRadioQoS=_CoDevWDSRadioQoS_Object((1,3,6,1,4,1,12394,1,10,5,34,1,3,1,1,3),_CoDevWDSRadioQoS_Type())
coDevWDSRadioQoS.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSRadioQoS.setStatus(_A)
_CoDeviceWDSGroupGroup_ObjectIdentity=ObjectIdentity
coDeviceWDSGroupGroup=_CoDeviceWDSGroupGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,34,1,4))
_CoDeviceWDSGroupTable_Object=MibTable
coDeviceWDSGroupTable=_CoDeviceWDSGroupTable_Object((1,3,6,1,4,1,12394,1,10,5,34,1,4,1))
if mibBuilder.loadTexts:coDeviceWDSGroupTable.setStatus(_A)
_CoDeviceWDSGroupEntry_Object=MibTableRow
coDeviceWDSGroupEntry=_CoDeviceWDSGroupEntry_Object((1,3,6,1,4,1,12394,1,10,5,34,1,4,1,1))
coDeviceWDSGroupEntry.setIndexNames((0,_E,_F),(0,_B,_I))
if mibBuilder.loadTexts:coDeviceWDSGroupEntry.setStatus(_A)
class _CoDevWDSGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_CoDevWDSGroupIndex_Type.__name__=_D
_CoDevWDSGroupIndex_Object=MibTableColumn
coDevWDSGroupIndex=_CoDevWDSGroupIndex_Object((1,3,6,1,4,1,12394,1,10,5,34,1,4,1,1,1),_CoDevWDSGroupIndex_Type())
coDevWDSGroupIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:coDevWDSGroupIndex.setStatus(_A)
class _CoDevWDSGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CoDevWDSGroupName_Type.__name__=_J
_CoDevWDSGroupName_Object=MibTableColumn
coDevWDSGroupName=_CoDevWDSGroupName_Object((1,3,6,1,4,1,12394,1,10,5,34,1,4,1,1,2),_CoDevWDSGroupName_Type())
coDevWDSGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSGroupName.setStatus(_A)
class _CoDevWDSGroupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('discovery',1),('negotiation',2),('acquisition',3),('locked',4),('shutdown',5)))
_CoDevWDSGroupState_Type.__name__=_D
_CoDevWDSGroupState_Object=MibTableColumn
coDevWDSGroupState=_CoDevWDSGroupState_Object((1,3,6,1,4,1,12394,1,10,5,34,1,4,1,1,3),_CoDevWDSGroupState_Type())
coDevWDSGroupState.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSGroupState.setStatus(_A)
class _CoDevWDSGroupSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('wep',2),('tkip',3),('aes',4)))
_CoDevWDSGroupSecurity_Type.__name__=_D
_CoDevWDSGroupSecurity_Object=MibTableColumn
coDevWDSGroupSecurity=_CoDevWDSGroupSecurity_Object((1,3,6,1,4,1,12394,1,10,5,34,1,4,1,1,4),_CoDevWDSGroupSecurity_Type())
coDevWDSGroupSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSGroupSecurity.setStatus(_A)
class _CoDevWDSGroupDynamicMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('slave',2),(_M,3)))
_CoDevWDSGroupDynamicMode_Type.__name__=_D
_CoDevWDSGroupDynamicMode_Object=MibTableColumn
coDevWDSGroupDynamicMode=_CoDevWDSGroupDynamicMode_Object((1,3,6,1,4,1,12394,1,10,5,34,1,4,1,1,5),_CoDevWDSGroupDynamicMode_Type())
coDevWDSGroupDynamicMode.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSGroupDynamicMode.setStatus(_A)
_CoDevWDSGroupDynamicGroupId_Type=Unsigned32
_CoDevWDSGroupDynamicGroupId_Object=MibTableColumn
coDevWDSGroupDynamicGroupId=_CoDevWDSGroupDynamicGroupId_Object((1,3,6,1,4,1,12394,1,10,5,34,1,4,1,1,6),_CoDevWDSGroupDynamicGroupId_Type())
coDevWDSGroupDynamicGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSGroupDynamicGroupId.setStatus(_A)
_CoDeviceWDSLinkGroup_ObjectIdentity=ObjectIdentity
coDeviceWDSLinkGroup=_CoDeviceWDSLinkGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,34,1,5))
_CoDeviceWDSLinkStatusTable_Object=MibTable
coDeviceWDSLinkStatusTable=_CoDeviceWDSLinkStatusTable_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,1))
if mibBuilder.loadTexts:coDeviceWDSLinkStatusTable.setStatus(_A)
_CoDeviceWDSLinkStatusEntry_Object=MibTableRow
coDeviceWDSLinkStatusEntry=_CoDeviceWDSLinkStatusEntry_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,1,1))
coDeviceWDSLinkStatusEntry.setIndexNames((0,_E,_F),(0,_B,_I),(0,_B,_N))
if mibBuilder.loadTexts:coDeviceWDSLinkStatusEntry.setStatus(_A)
class _CoDevWDSLinkStaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,54))
_CoDevWDSLinkStaIndex_Type.__name__=_D
_CoDevWDSLinkStaIndex_Object=MibTableColumn
coDevWDSLinkStaIndex=_CoDevWDSLinkStaIndex_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,1,1,1),_CoDevWDSLinkStaIndex_Type())
coDevWDSLinkStaIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:coDevWDSLinkStaIndex.setStatus(_A)
class _CoDevWDSLinkStaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('down',1),('acquiring',2),('inactive',3),('active',4)))
_CoDevWDSLinkStaState_Type.__name__=_D
_CoDevWDSLinkStaState_Object=MibTableColumn
coDevWDSLinkStaState=_CoDevWDSLinkStaState_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,1,1,2),_CoDevWDSLinkStaState_Type())
coDevWDSLinkStaState.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStaState.setStatus(_A)
class _CoDevWDSLinkStaRadio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_CoDevWDSLinkStaRadio_Type.__name__=_D
_CoDevWDSLinkStaRadio_Object=MibTableColumn
coDevWDSLinkStaRadio=_CoDevWDSLinkStaRadio_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,1,1,3),_CoDevWDSLinkStaRadio_Type())
coDevWDSLinkStaRadio.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStaRadio.setStatus(_A)
_CoDevWDSLinkStaPeerMacAddress_Type=MacAddress
_CoDevWDSLinkStaPeerMacAddress_Object=MibTableColumn
coDevWDSLinkStaPeerMacAddress=_CoDevWDSLinkStaPeerMacAddress_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,1,1,4),_CoDevWDSLinkStaPeerMacAddress_Type())
coDevWDSLinkStaPeerMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStaPeerMacAddress.setStatus(_A)
_CoDevWDSLinkStaMaster_Type=TruthValue
_CoDevWDSLinkStaMaster_Object=MibTableColumn
coDevWDSLinkStaMaster=_CoDevWDSLinkStaMaster_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,1,1,5),_CoDevWDSLinkStaMaster_Type())
coDevWDSLinkStaMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStaMaster.setStatus(_A)
_CoDevWDSLinkStaAuthorized_Type=TruthValue
_CoDevWDSLinkStaAuthorized_Object=MibTableColumn
coDevWDSLinkStaAuthorized=_CoDevWDSLinkStaAuthorized_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,1,1,6),_CoDevWDSLinkStaAuthorized_Type())
coDevWDSLinkStaAuthorized.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStaAuthorized.setStatus(_A)
class _CoDevWDSLinkStaEncryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('wep',2),('tkip',3),('aes',4)))
_CoDevWDSLinkStaEncryption_Type.__name__=_D
_CoDevWDSLinkStaEncryption_Object=MibTableColumn
coDevWDSLinkStaEncryption=_CoDevWDSLinkStaEncryption_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,1,1,7),_CoDevWDSLinkStaEncryption_Type())
coDevWDSLinkStaEncryption.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStaEncryption.setStatus(_A)
_CoDevWDSLinkStaIdleTime_Type=Unsigned32
_CoDevWDSLinkStaIdleTime_Object=MibTableColumn
coDevWDSLinkStaIdleTime=_CoDevWDSLinkStaIdleTime_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,1,1,8),_CoDevWDSLinkStaIdleTime_Type())
coDevWDSLinkStaIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStaIdleTime.setStatus(_A)
if mibBuilder.loadTexts:coDevWDSLinkStaIdleTime.setUnits('seconds')
class _CoDevWDSLinkStaSNR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,92))
_CoDevWDSLinkStaSNR_Type.__name__=_D
_CoDevWDSLinkStaSNR_Object=MibTableColumn
coDevWDSLinkStaSNR=_CoDevWDSLinkStaSNR_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,1,1,9),_CoDevWDSLinkStaSNR_Type())
coDevWDSLinkStaSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStaSNR.setStatus(_A)
if mibBuilder.loadTexts:coDevWDSLinkStaSNR.setUnits('dBm')
_CoDevWDSLinkStaTxRate_Type=Unsigned32
_CoDevWDSLinkStaTxRate_Object=MibTableColumn
coDevWDSLinkStaTxRate=_CoDevWDSLinkStaTxRate_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,1,1,10),_CoDevWDSLinkStaTxRate_Type())
coDevWDSLinkStaTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStaTxRate.setStatus(_A)
if mibBuilder.loadTexts:coDevWDSLinkStaTxRate.setUnits(_O)
_CoDevWDSLinkStaRxRate_Type=Unsigned32
_CoDevWDSLinkStaRxRate_Object=MibTableColumn
coDevWDSLinkStaRxRate=_CoDevWDSLinkStaRxRate_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,1,1,11),_CoDevWDSLinkStaRxRate_Type())
coDevWDSLinkStaRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStaRxRate.setStatus(_A)
if mibBuilder.loadTexts:coDevWDSLinkStaRxRate.setUnits(_O)
class _CoDevWDSLinkStaIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoDevWDSLinkStaIfIndex_Type.__name__=_D
_CoDevWDSLinkStaIfIndex_Object=MibTableColumn
coDevWDSLinkStaIfIndex=_CoDevWDSLinkStaIfIndex_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,1,1,12),_CoDevWDSLinkStaIfIndex_Type())
coDevWDSLinkStaIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStaIfIndex.setStatus(_A)
_CoDeviceWDSLinkStatsRatesTable_Object=MibTable
coDeviceWDSLinkStatsRatesTable=_CoDeviceWDSLinkStatsRatesTable_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2))
if mibBuilder.loadTexts:coDeviceWDSLinkStatsRatesTable.setStatus(_A)
_CoDeviceWDSLinkStatsRatesEntry_Object=MibTableRow
coDeviceWDSLinkStatsRatesEntry=_CoDeviceWDSLinkStatsRatesEntry_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1))
if mibBuilder.loadTexts:coDeviceWDSLinkStatsRatesEntry.setStatus(_A)
_CoDevWDSLinkStsPktsTxRate1_Type=Counter32
_CoDevWDSLinkStsPktsTxRate1_Object=MibTableColumn
coDevWDSLinkStsPktsTxRate1=_CoDevWDSLinkStsPktsTxRate1_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,1),_CoDevWDSLinkStsPktsTxRate1_Type())
coDevWDSLinkStsPktsTxRate1.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsTxRate1.setStatus(_A)
_CoDevWDSLinkStsPktsTxRate2_Type=Counter32
_CoDevWDSLinkStsPktsTxRate2_Object=MibTableColumn
coDevWDSLinkStsPktsTxRate2=_CoDevWDSLinkStsPktsTxRate2_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,2),_CoDevWDSLinkStsPktsTxRate2_Type())
coDevWDSLinkStsPktsTxRate2.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsTxRate2.setStatus(_A)
_CoDevWDSLinkStsPktsTxRate5dot5_Type=Counter32
_CoDevWDSLinkStsPktsTxRate5dot5_Object=MibTableColumn
coDevWDSLinkStsPktsTxRate5dot5=_CoDevWDSLinkStsPktsTxRate5dot5_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,3),_CoDevWDSLinkStsPktsTxRate5dot5_Type())
coDevWDSLinkStsPktsTxRate5dot5.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsTxRate5dot5.setStatus(_A)
_CoDevWDSLinkStsPktsTxRate11_Type=Counter32
_CoDevWDSLinkStsPktsTxRate11_Object=MibTableColumn
coDevWDSLinkStsPktsTxRate11=_CoDevWDSLinkStsPktsTxRate11_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,4),_CoDevWDSLinkStsPktsTxRate11_Type())
coDevWDSLinkStsPktsTxRate11.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsTxRate11.setStatus(_A)
_CoDevWDSLinkStsPktsTxRate6_Type=Counter32
_CoDevWDSLinkStsPktsTxRate6_Object=MibTableColumn
coDevWDSLinkStsPktsTxRate6=_CoDevWDSLinkStsPktsTxRate6_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,5),_CoDevWDSLinkStsPktsTxRate6_Type())
coDevWDSLinkStsPktsTxRate6.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsTxRate6.setStatus(_A)
_CoDevWDSLinkStsPktsTxRate9_Type=Counter32
_CoDevWDSLinkStsPktsTxRate9_Object=MibTableColumn
coDevWDSLinkStsPktsTxRate9=_CoDevWDSLinkStsPktsTxRate9_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,6),_CoDevWDSLinkStsPktsTxRate9_Type())
coDevWDSLinkStsPktsTxRate9.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsTxRate9.setStatus(_A)
_CoDevWDSLinkStsPktsTxRate12_Type=Counter32
_CoDevWDSLinkStsPktsTxRate12_Object=MibTableColumn
coDevWDSLinkStsPktsTxRate12=_CoDevWDSLinkStsPktsTxRate12_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,7),_CoDevWDSLinkStsPktsTxRate12_Type())
coDevWDSLinkStsPktsTxRate12.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsTxRate12.setStatus(_A)
_CoDevWDSLinkStsPktsTxRate18_Type=Counter32
_CoDevWDSLinkStsPktsTxRate18_Object=MibTableColumn
coDevWDSLinkStsPktsTxRate18=_CoDevWDSLinkStsPktsTxRate18_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,8),_CoDevWDSLinkStsPktsTxRate18_Type())
coDevWDSLinkStsPktsTxRate18.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsTxRate18.setStatus(_A)
_CoDevWDSLinkStsPktsTxRate24_Type=Counter32
_CoDevWDSLinkStsPktsTxRate24_Object=MibTableColumn
coDevWDSLinkStsPktsTxRate24=_CoDevWDSLinkStsPktsTxRate24_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,9),_CoDevWDSLinkStsPktsTxRate24_Type())
coDevWDSLinkStsPktsTxRate24.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsTxRate24.setStatus(_A)
_CoDevWDSLinkStsPktsTxRate36_Type=Counter32
_CoDevWDSLinkStsPktsTxRate36_Object=MibTableColumn
coDevWDSLinkStsPktsTxRate36=_CoDevWDSLinkStsPktsTxRate36_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,10),_CoDevWDSLinkStsPktsTxRate36_Type())
coDevWDSLinkStsPktsTxRate36.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsTxRate36.setStatus(_A)
_CoDevWDSLinkStsPktsTxRate48_Type=Counter32
_CoDevWDSLinkStsPktsTxRate48_Object=MibTableColumn
coDevWDSLinkStsPktsTxRate48=_CoDevWDSLinkStsPktsTxRate48_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,11),_CoDevWDSLinkStsPktsTxRate48_Type())
coDevWDSLinkStsPktsTxRate48.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsTxRate48.setStatus(_A)
_CoDevWDSLinkStsPktsTxRate54_Type=Counter32
_CoDevWDSLinkStsPktsTxRate54_Object=MibTableColumn
coDevWDSLinkStsPktsTxRate54=_CoDevWDSLinkStsPktsTxRate54_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,12),_CoDevWDSLinkStsPktsTxRate54_Type())
coDevWDSLinkStsPktsTxRate54.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsTxRate54.setStatus(_A)
_CoDevWDSLinkStsPktsRxRate1_Type=Counter32
_CoDevWDSLinkStsPktsRxRate1_Object=MibTableColumn
coDevWDSLinkStsPktsRxRate1=_CoDevWDSLinkStsPktsRxRate1_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,13),_CoDevWDSLinkStsPktsRxRate1_Type())
coDevWDSLinkStsPktsRxRate1.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsRxRate1.setStatus(_A)
_CoDevWDSLinkStsPktsRxRate2_Type=Counter32
_CoDevWDSLinkStsPktsRxRate2_Object=MibTableColumn
coDevWDSLinkStsPktsRxRate2=_CoDevWDSLinkStsPktsRxRate2_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,14),_CoDevWDSLinkStsPktsRxRate2_Type())
coDevWDSLinkStsPktsRxRate2.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsRxRate2.setStatus(_A)
_CoDevWDSLinkStsPktsRxRate5dot5_Type=Counter32
_CoDevWDSLinkStsPktsRxRate5dot5_Object=MibTableColumn
coDevWDSLinkStsPktsRxRate5dot5=_CoDevWDSLinkStsPktsRxRate5dot5_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,15),_CoDevWDSLinkStsPktsRxRate5dot5_Type())
coDevWDSLinkStsPktsRxRate5dot5.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsRxRate5dot5.setStatus(_A)
_CoDevWDSLinkStsPktsRxRate11_Type=Counter32
_CoDevWDSLinkStsPktsRxRate11_Object=MibTableColumn
coDevWDSLinkStsPktsRxRate11=_CoDevWDSLinkStsPktsRxRate11_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,16),_CoDevWDSLinkStsPktsRxRate11_Type())
coDevWDSLinkStsPktsRxRate11.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsRxRate11.setStatus(_A)
_CoDevWDSLinkStsPktsRxRate6_Type=Counter32
_CoDevWDSLinkStsPktsRxRate6_Object=MibTableColumn
coDevWDSLinkStsPktsRxRate6=_CoDevWDSLinkStsPktsRxRate6_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,17),_CoDevWDSLinkStsPktsRxRate6_Type())
coDevWDSLinkStsPktsRxRate6.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsRxRate6.setStatus(_A)
_CoDevWDSLinkStsPktsRxRate9_Type=Counter32
_CoDevWDSLinkStsPktsRxRate9_Object=MibTableColumn
coDevWDSLinkStsPktsRxRate9=_CoDevWDSLinkStsPktsRxRate9_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,18),_CoDevWDSLinkStsPktsRxRate9_Type())
coDevWDSLinkStsPktsRxRate9.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsRxRate9.setStatus(_A)
_CoDevWDSLinkStsPktsRxRate12_Type=Counter32
_CoDevWDSLinkStsPktsRxRate12_Object=MibTableColumn
coDevWDSLinkStsPktsRxRate12=_CoDevWDSLinkStsPktsRxRate12_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,19),_CoDevWDSLinkStsPktsRxRate12_Type())
coDevWDSLinkStsPktsRxRate12.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsRxRate12.setStatus(_A)
_CoDevWDSLinkStsPktsRxRate18_Type=Counter32
_CoDevWDSLinkStsPktsRxRate18_Object=MibTableColumn
coDevWDSLinkStsPktsRxRate18=_CoDevWDSLinkStsPktsRxRate18_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,20),_CoDevWDSLinkStsPktsRxRate18_Type())
coDevWDSLinkStsPktsRxRate18.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsRxRate18.setStatus(_A)
_CoDevWDSLinkStsPktsRxRate24_Type=Counter32
_CoDevWDSLinkStsPktsRxRate24_Object=MibTableColumn
coDevWDSLinkStsPktsRxRate24=_CoDevWDSLinkStsPktsRxRate24_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,21),_CoDevWDSLinkStsPktsRxRate24_Type())
coDevWDSLinkStsPktsRxRate24.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsRxRate24.setStatus(_A)
_CoDevWDSLinkStsPktsRxRate36_Type=Counter32
_CoDevWDSLinkStsPktsRxRate36_Object=MibTableColumn
coDevWDSLinkStsPktsRxRate36=_CoDevWDSLinkStsPktsRxRate36_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,22),_CoDevWDSLinkStsPktsRxRate36_Type())
coDevWDSLinkStsPktsRxRate36.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsRxRate36.setStatus(_A)
_CoDevWDSLinkStsPktsRxRate48_Type=Counter32
_CoDevWDSLinkStsPktsRxRate48_Object=MibTableColumn
coDevWDSLinkStsPktsRxRate48=_CoDevWDSLinkStsPktsRxRate48_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,23),_CoDevWDSLinkStsPktsRxRate48_Type())
coDevWDSLinkStsPktsRxRate48.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsRxRate48.setStatus(_A)
_CoDevWDSLinkStsPktsRxRate54_Type=Counter32
_CoDevWDSLinkStsPktsRxRate54_Object=MibTableColumn
coDevWDSLinkStsPktsRxRate54=_CoDevWDSLinkStsPktsRxRate54_Object((1,3,6,1,4,1,12394,1,10,5,34,1,5,2,1,24),_CoDevWDSLinkStsPktsRxRate54_Type())
coDevWDSLinkStsPktsRxRate54.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSLinkStsPktsRxRate54.setStatus(_A)
_CoDeviceWDSNetworkScanGroup_ObjectIdentity=ObjectIdentity
coDeviceWDSNetworkScanGroup=_CoDeviceWDSNetworkScanGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,34,1,6))
_CoDeviceWDSNetworkScanTable_Object=MibTable
coDeviceWDSNetworkScanTable=_CoDeviceWDSNetworkScanTable_Object((1,3,6,1,4,1,12394,1,10,5,34,1,6,1))
if mibBuilder.loadTexts:coDeviceWDSNetworkScanTable.setStatus(_A)
_CoDeviceWDSNetworkScanEntry_Object=MibTableRow
coDeviceWDSNetworkScanEntry=_CoDeviceWDSNetworkScanEntry_Object((1,3,6,1,4,1,12394,1,10,5,34,1,6,1,1))
coDeviceWDSNetworkScanEntry.setIndexNames((0,_E,_F),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:coDeviceWDSNetworkScanEntry.setStatus(_A)
class _CoDevWDSScanRadioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_CoDevWDSScanRadioIndex_Type.__name__=_D
_CoDevWDSScanRadioIndex_Object=MibTableColumn
coDevWDSScanRadioIndex=_CoDevWDSScanRadioIndex_Object((1,3,6,1,4,1,12394,1,10,5,34,1,6,1,1,1),_CoDevWDSScanRadioIndex_Type())
coDevWDSScanRadioIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:coDevWDSScanRadioIndex.setStatus(_A)
class _CoDevWDSScanPeerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CoDevWDSScanPeerIndex_Type.__name__=_D
_CoDevWDSScanPeerIndex_Object=MibTableColumn
coDevWDSScanPeerIndex=_CoDevWDSScanPeerIndex_Object((1,3,6,1,4,1,12394,1,10,5,34,1,6,1,1,2),_CoDevWDSScanPeerIndex_Type())
coDevWDSScanPeerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:coDevWDSScanPeerIndex.setStatus(_A)
_CoDevWDSScanGroupId_Type=Unsigned32
_CoDevWDSScanGroupId_Object=MibTableColumn
coDevWDSScanGroupId=_CoDevWDSScanGroupId_Object((1,3,6,1,4,1,12394,1,10,5,34,1,6,1,1,3),_CoDevWDSScanGroupId_Type())
coDevWDSScanGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSScanGroupId.setStatus(_A)
_CoDevWDSScanPeerMacAddress_Type=MacAddress
_CoDevWDSScanPeerMacAddress_Object=MibTableColumn
coDevWDSScanPeerMacAddress=_CoDevWDSScanPeerMacAddress_Object((1,3,6,1,4,1,12394,1,10,5,34,1,6,1,1,4),_CoDevWDSScanPeerMacAddress_Type())
coDevWDSScanPeerMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSScanPeerMacAddress.setStatus(_A)
class _CoDevWDSScanChannel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
_CoDevWDSScanChannel_Type.__name__=_H
_CoDevWDSScanChannel_Object=MibTableColumn
coDevWDSScanChannel=_CoDevWDSScanChannel_Object((1,3,6,1,4,1,12394,1,10,5,34,1,6,1,1,5),_CoDevWDSScanChannel_Type())
coDevWDSScanChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSScanChannel.setStatus(_A)
class _CoDevWDSScanSNR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,92))
_CoDevWDSScanSNR_Type.__name__=_D
_CoDevWDSScanSNR_Object=MibTableColumn
coDevWDSScanSNR=_CoDevWDSScanSNR_Object((1,3,6,1,4,1,12394,1,10,5,34,1,6,1,1,6),_CoDevWDSScanSNR_Type())
coDevWDSScanSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSScanSNR.setStatus(_A)
if mibBuilder.loadTexts:coDevWDSScanSNR.setUnits('dBm')
class _CoDevWDSScanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('slave',2),(_M,3)))
_CoDevWDSScanMode_Type.__name__=_D
_CoDevWDSScanMode_Object=MibTableColumn
coDevWDSScanMode=_CoDevWDSScanMode_Object((1,3,6,1,4,1,12394,1,10,5,34,1,6,1,1,7),_CoDevWDSScanMode_Type())
coDevWDSScanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSScanMode.setStatus(_A)
_CoDevWDSScanAvailable_Type=TruthValue
_CoDevWDSScanAvailable_Object=MibTableColumn
coDevWDSScanAvailable=_CoDevWDSScanAvailable_Object((1,3,6,1,4,1,12394,1,10,5,34,1,6,1,1,8),_CoDevWDSScanAvailable_Type())
coDevWDSScanAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevWDSScanAvailable.setStatus(_A)
_AlvarionDeviceWdsMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
alvarionDeviceWdsMIBNotificationPrefix=_AlvarionDeviceWdsMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,34,2))
_AlvarionDeviceWdsMIBNotifications_ObjectIdentity=ObjectIdentity
alvarionDeviceWdsMIBNotifications=_AlvarionDeviceWdsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,34,2,0))
_AlvarionDeviceWdsMIBConformance_ObjectIdentity=ObjectIdentity
alvarionDeviceWdsMIBConformance=_AlvarionDeviceWdsMIBConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,34,3))
_AlvarionDeviceWdsMIBCompliances_ObjectIdentity=ObjectIdentity
alvarionDeviceWdsMIBCompliances=_AlvarionDeviceWdsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,34,3,1))
_AlvarionDeviceWdsMIBGroups_ObjectIdentity=ObjectIdentity
alvarionDeviceWdsMIBGroups=_AlvarionDeviceWdsMIBGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,34,3,2))
coDeviceWDSLinkStatusEntry.registerAugmentions((_B,_R))
coDeviceWDSLinkStatsRatesEntry.setIndexNames(*coDeviceWDSLinkStatusEntry.getIndexNames())
alvarionDeviceWdsInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,34,3,2,1))
alvarionDeviceWdsInfoMIBGroup.setObjects((_B,_S))
if mibBuilder.loadTexts:alvarionDeviceWdsInfoMIBGroup.setStatus(_A)
alvarionDeviceWdsRadioMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,34,3,2,2))
alvarionDeviceWdsRadioMIBGroup.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:alvarionDeviceWdsRadioMIBGroup.setStatus(_A)
alvarionDeviceWdsGroupMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,34,3,2,3))
alvarionDeviceWdsGroupMIBGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:alvarionDeviceWdsGroupMIBGroup.setStatus(_A)
alvarionDeviceWdsLinkMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,34,3,2,4))
alvarionDeviceWdsLinkMIBGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:alvarionDeviceWdsLinkMIBGroup.setStatus(_A)
alvarionDeviceWdsNetworkScanMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,34,3,2,5))
alvarionDeviceWdsNetworkScanMIBGroup.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:alvarionDeviceWdsNetworkScanMIBGroup.setStatus(_A)
alvarionDeviceWdsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,34,3,1,1))
alvarionDeviceWdsMIBCompliance.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:alvarionDeviceWdsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alvarionDeviceWdsMIB':alvarionDeviceWdsMIB,'alvarionDeviceWdsMIBObjects':alvarionDeviceWdsMIBObjects,'coDeviceWDSInfoGroup':coDeviceWDSInfoGroup,'coDeviceWdsInfoTable':coDeviceWdsInfoTable,'coDeviceWdsInfoEntry':coDeviceWdsInfoEntry,_S:coDevWDSInfoMaxNumberOfGroup,'coDeviceWDSRadioGroup':coDeviceWDSRadioGroup,'coDeviceWDSRadioTable':coDeviceWDSRadioTable,'coDeviceWDSRadioEntry':coDeviceWDSRadioEntry,_K:coDevWDSRadioIndex,_T:coDevWDSRadioAckDistance,_U:coDevWDSRadioQoS,'coDeviceWDSGroupGroup':coDeviceWDSGroupGroup,'coDeviceWDSGroupTable':coDeviceWDSGroupTable,'coDeviceWDSGroupEntry':coDeviceWDSGroupEntry,_I:coDevWDSGroupIndex,_V:coDevWDSGroupName,_W:coDevWDSGroupState,_X:coDevWDSGroupSecurity,_Y:coDevWDSGroupDynamicMode,_Z:coDevWDSGroupDynamicGroupId,'coDeviceWDSLinkGroup':coDeviceWDSLinkGroup,'coDeviceWDSLinkStatusTable':coDeviceWDSLinkStatusTable,'coDeviceWDSLinkStatusEntry':coDeviceWDSLinkStatusEntry,_N:coDevWDSLinkStaIndex,_a:coDevWDSLinkStaState,_b:coDevWDSLinkStaRadio,_c:coDevWDSLinkStaPeerMacAddress,_d:coDevWDSLinkStaMaster,_e:coDevWDSLinkStaAuthorized,_f:coDevWDSLinkStaEncryption,_g:coDevWDSLinkStaIdleTime,_h:coDevWDSLinkStaSNR,_i:coDevWDSLinkStaTxRate,_j:coDevWDSLinkStaRxRate,_k:coDevWDSLinkStaIfIndex,'coDeviceWDSLinkStatsRatesTable':coDeviceWDSLinkStatsRatesTable,_R:coDeviceWDSLinkStatsRatesEntry,_l:coDevWDSLinkStsPktsTxRate1,_m:coDevWDSLinkStsPktsTxRate2,_n:coDevWDSLinkStsPktsTxRate5dot5,_o:coDevWDSLinkStsPktsTxRate11,_p:coDevWDSLinkStsPktsTxRate6,_q:coDevWDSLinkStsPktsTxRate9,_r:coDevWDSLinkStsPktsTxRate12,_s:coDevWDSLinkStsPktsTxRate18,_t:coDevWDSLinkStsPktsTxRate24,_u:coDevWDSLinkStsPktsTxRate36,_v:coDevWDSLinkStsPktsTxRate48,_w:coDevWDSLinkStsPktsTxRate54,_x:coDevWDSLinkStsPktsRxRate1,_y:coDevWDSLinkStsPktsRxRate2,_z:coDevWDSLinkStsPktsRxRate5dot5,_A0:coDevWDSLinkStsPktsRxRate11,_A1:coDevWDSLinkStsPktsRxRate6,_A2:coDevWDSLinkStsPktsRxRate9,_A3:coDevWDSLinkStsPktsRxRate12,_A4:coDevWDSLinkStsPktsRxRate18,_A5:coDevWDSLinkStsPktsRxRate24,_A6:coDevWDSLinkStsPktsRxRate36,_A7:coDevWDSLinkStsPktsRxRate48,_A8:coDevWDSLinkStsPktsRxRate54,'coDeviceWDSNetworkScanGroup':coDeviceWDSNetworkScanGroup,'coDeviceWDSNetworkScanTable':coDeviceWDSNetworkScanTable,'coDeviceWDSNetworkScanEntry':coDeviceWDSNetworkScanEntry,_P:coDevWDSScanRadioIndex,_Q:coDevWDSScanPeerIndex,_A9:coDevWDSScanGroupId,_AA:coDevWDSScanPeerMacAddress,_AB:coDevWDSScanChannel,_AC:coDevWDSScanSNR,_AD:coDevWDSScanMode,_AE:coDevWDSScanAvailable,'alvarionDeviceWdsMIBNotificationPrefix':alvarionDeviceWdsMIBNotificationPrefix,'alvarionDeviceWdsMIBNotifications':alvarionDeviceWdsMIBNotifications,'alvarionDeviceWdsMIBConformance':alvarionDeviceWdsMIBConformance,'alvarionDeviceWdsMIBCompliances':alvarionDeviceWdsMIBCompliances,'alvarionDeviceWdsMIBCompliance':alvarionDeviceWdsMIBCompliance,'alvarionDeviceWdsMIBGroups':alvarionDeviceWdsMIBGroups,_AF:alvarionDeviceWdsInfoMIBGroup,_AG:alvarionDeviceWdsRadioMIBGroup,_AH:alvarionDeviceWdsGroupMIBGroup,_AI:alvarionDeviceWdsLinkMIBGroup,_AJ:alvarionDeviceWdsNetworkScanMIBGroup})