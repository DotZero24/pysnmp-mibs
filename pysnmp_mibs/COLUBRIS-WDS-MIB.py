_A3='colubrisWDSScanMIBGroup'
_A2='colubrisWDSLinkMIBGroup'
_A1='colubrisWDSGroupMIBGroup'
_A0='colubrisWDSRadioMIBGroup'
_z='colubrisWDSInfoMIBGroup'
_y='coWDSScanAvailable'
_x='coWDSScanMode'
_w='coWDSScanSNR'
_v='coWDSScanChannel'
_u='coWDSScanPeerMacAddress'
_t='coWDSScanGroupId'
_s='coWDSLinkVHT'
_r='coWDSLinkNoise'
_q='coWDSLinkSignal'
_p='coWDSLinkRxMCS'
_o='coWDSLinkTxMCS'
_n='coWDSLinkHT'
_m='coWDSLinkIfIndex'
_l='coWDSLinkRxRate'
_k='coWDSLinkTxRate'
_j='coWDSLinkSNR'
_i='coWDSLinkIdleTime'
_h='coWDSLinkEncryption'
_g='coWDSLinkAuthorized'
_f='coWDSLinkMaster'
_e='coWDSLinkPeerMacAddress'
_d='coWDSLinkRadio'
_c='coWDSLinkState'
_b='coWDSGroupDynamicGroupId'
_a='coWDSGroupDynamicMode'
_Z='coWDSGroupStaticMacAddress'
_Y='coWDSGroupAddressing'
_X='coWDSGroupSecurity'
_W='coWDSGroupState'
_V='coWDSGroupName'
_U='coWDSRadioQoS'
_T='coWDSRadioAckDistance'
_S='coWDSDynamicModeImplemented'
_R='coWDSNumberOfGroup'
_Q='coWDSScanPeerIndex'
_P='coWDSScanRadioIndex'
_O='500Kb/s'
_N='coWDSLinkIndex'
_M='alternateMaster'
_L='master'
_K='coWDSRadioIndex'
_J='DisplayString'
_I='none'
_H='coWDSGroupIndex'
_G='Unsigned32'
_F='dBm'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='COLUBRIS-WDS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','TextualConvention','TruthValue')
colubrisWdsMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,33))
_ColubrisWdsMIBObjects_ObjectIdentity=ObjectIdentity
colubrisWdsMIBObjects=_ColubrisWdsMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,33,1))
_CoWDSInfoGroup_ObjectIdentity=ObjectIdentity
coWDSInfoGroup=_CoWDSInfoGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,33,1,1))
class _CoWDSNumberOfGroup_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_CoWDSNumberOfGroup_Type.__name__=_G
_CoWDSNumberOfGroup_Object=MibScalar
coWDSNumberOfGroup=_CoWDSNumberOfGroup_Object((1,3,6,1,4,1,8744,5,33,1,1,1),_CoWDSNumberOfGroup_Type())
coWDSNumberOfGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSNumberOfGroup.setStatus(_A)
_CoWDSDynamicModeImplemented_Type=TruthValue
_CoWDSDynamicModeImplemented_Object=MibScalar
coWDSDynamicModeImplemented=_CoWDSDynamicModeImplemented_Object((1,3,6,1,4,1,8744,5,33,1,1,2),_CoWDSDynamicModeImplemented_Type())
coWDSDynamicModeImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSDynamicModeImplemented.setStatus(_A)
_CoWDSRadioGroup_ObjectIdentity=ObjectIdentity
coWDSRadioGroup=_CoWDSRadioGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,33,1,2))
_CoWDSRadioTable_Object=MibTable
coWDSRadioTable=_CoWDSRadioTable_Object((1,3,6,1,4,1,8744,5,33,1,2,1))
if mibBuilder.loadTexts:coWDSRadioTable.setStatus(_A)
_CoWDSRadioEntry_Object=MibTableRow
coWDSRadioEntry=_CoWDSRadioEntry_Object((1,3,6,1,4,1,8744,5,33,1,2,1,1))
coWDSRadioEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:coWDSRadioEntry.setStatus(_A)
class _CoWDSRadioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_CoWDSRadioIndex_Type.__name__=_D
_CoWDSRadioIndex_Object=MibTableColumn
coWDSRadioIndex=_CoWDSRadioIndex_Object((1,3,6,1,4,1,8744,5,33,1,2,1,1,1),_CoWDSRadioIndex_Type())
coWDSRadioIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:coWDSRadioIndex.setStatus(_A)
_CoWDSRadioAckDistance_Type=Unsigned32
_CoWDSRadioAckDistance_Object=MibTableColumn
coWDSRadioAckDistance=_CoWDSRadioAckDistance_Object((1,3,6,1,4,1,8744,5,33,1,2,1,1,2),_CoWDSRadioAckDistance_Type())
coWDSRadioAckDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSRadioAckDistance.setStatus(_A)
if mibBuilder.loadTexts:coWDSRadioAckDistance.setUnits('km')
class _CoWDSRadioQoS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('disabled',1),('vlan',2),('veryHigh',3),('high',4),('normal',5),('low',6),('diffSrv',7),('tos',8),('ipQos',9)))
_CoWDSRadioQoS_Type.__name__=_D
_CoWDSRadioQoS_Object=MibTableColumn
coWDSRadioQoS=_CoWDSRadioQoS_Object((1,3,6,1,4,1,8744,5,33,1,2,1,1,3),_CoWDSRadioQoS_Type())
coWDSRadioQoS.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSRadioQoS.setStatus(_A)
_CoWDSGroupGroup_ObjectIdentity=ObjectIdentity
coWDSGroupGroup=_CoWDSGroupGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,33,1,3))
_CoWDSGroupTable_Object=MibTable
coWDSGroupTable=_CoWDSGroupTable_Object((1,3,6,1,4,1,8744,5,33,1,3,1))
if mibBuilder.loadTexts:coWDSGroupTable.setStatus(_A)
_CoWDSGroupEntry_Object=MibTableRow
coWDSGroupEntry=_CoWDSGroupEntry_Object((1,3,6,1,4,1,8744,5,33,1,3,1,1))
coWDSGroupEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:coWDSGroupEntry.setStatus(_A)
class _CoWDSGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_CoWDSGroupIndex_Type.__name__=_D
_CoWDSGroupIndex_Object=MibTableColumn
coWDSGroupIndex=_CoWDSGroupIndex_Object((1,3,6,1,4,1,8744,5,33,1,3,1,1,1),_CoWDSGroupIndex_Type())
coWDSGroupIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:coWDSGroupIndex.setStatus(_A)
class _CoWDSGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CoWDSGroupName_Type.__name__=_J
_CoWDSGroupName_Object=MibTableColumn
coWDSGroupName=_CoWDSGroupName_Object((1,3,6,1,4,1,8744,5,33,1,3,1,1,2),_CoWDSGroupName_Type())
coWDSGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSGroupName.setStatus(_A)
class _CoWDSGroupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_CoWDSGroupState_Type.__name__=_D
_CoWDSGroupState_Object=MibTableColumn
coWDSGroupState=_CoWDSGroupState_Object((1,3,6,1,4,1,8744,5,33,1,3,1,1,3),_CoWDSGroupState_Type())
coWDSGroupState.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSGroupState.setStatus(_A)
class _CoWDSGroupSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('wep',2),('tkip',3),('aes',4)))
_CoWDSGroupSecurity_Type.__name__=_D
_CoWDSGroupSecurity_Object=MibTableColumn
coWDSGroupSecurity=_CoWDSGroupSecurity_Object((1,3,6,1,4,1,8744,5,33,1,3,1,1,4),_CoWDSGroupSecurity_Type())
coWDSGroupSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSGroupSecurity.setStatus(_A)
class _CoWDSGroupAddressing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_CoWDSGroupAddressing_Type.__name__=_D
_CoWDSGroupAddressing_Object=MibTableColumn
coWDSGroupAddressing=_CoWDSGroupAddressing_Object((1,3,6,1,4,1,8744,5,33,1,3,1,1,5),_CoWDSGroupAddressing_Type())
coWDSGroupAddressing.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSGroupAddressing.setStatus(_A)
_CoWDSGroupStaticMacAddress_Type=MacAddress
_CoWDSGroupStaticMacAddress_Object=MibTableColumn
coWDSGroupStaticMacAddress=_CoWDSGroupStaticMacAddress_Object((1,3,6,1,4,1,8744,5,33,1,3,1,1,6),_CoWDSGroupStaticMacAddress_Type())
coWDSGroupStaticMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSGroupStaticMacAddress.setStatus(_A)
class _CoWDSGroupDynamicMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_L,1),('slave',2),(_M,3)))
_CoWDSGroupDynamicMode_Type.__name__=_D
_CoWDSGroupDynamicMode_Object=MibTableColumn
coWDSGroupDynamicMode=_CoWDSGroupDynamicMode_Object((1,3,6,1,4,1,8744,5,33,1,3,1,1,7),_CoWDSGroupDynamicMode_Type())
coWDSGroupDynamicMode.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSGroupDynamicMode.setStatus(_A)
_CoWDSGroupDynamicGroupId_Type=Unsigned32
_CoWDSGroupDynamicGroupId_Object=MibTableColumn
coWDSGroupDynamicGroupId=_CoWDSGroupDynamicGroupId_Object((1,3,6,1,4,1,8744,5,33,1,3,1,1,8),_CoWDSGroupDynamicGroupId_Type())
coWDSGroupDynamicGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSGroupDynamicGroupId.setStatus(_A)
_CoWDSLinkGroup_ObjectIdentity=ObjectIdentity
coWDSLinkGroup=_CoWDSLinkGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,33,1,4))
_CoWDSLinkTable_Object=MibTable
coWDSLinkTable=_CoWDSLinkTable_Object((1,3,6,1,4,1,8744,5,33,1,4,1))
if mibBuilder.loadTexts:coWDSLinkTable.setStatus(_A)
_CoWDSLinkEntry_Object=MibTableRow
coWDSLinkEntry=_CoWDSLinkEntry_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1))
coWDSLinkEntry.setIndexNames((0,_B,_H),(0,_B,_N))
if mibBuilder.loadTexts:coWDSLinkEntry.setStatus(_A)
class _CoWDSLinkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,54))
_CoWDSLinkIndex_Type.__name__=_D
_CoWDSLinkIndex_Object=MibTableColumn
coWDSLinkIndex=_CoWDSLinkIndex_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,1),_CoWDSLinkIndex_Type())
coWDSLinkIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:coWDSLinkIndex.setStatus(_A)
class _CoWDSLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('down',1),('acquiring',2),('inactive',3),('active',4)))
_CoWDSLinkState_Type.__name__=_D
_CoWDSLinkState_Object=MibTableColumn
coWDSLinkState=_CoWDSLinkState_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,2),_CoWDSLinkState_Type())
coWDSLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkState.setStatus(_A)
class _CoWDSLinkRadio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_CoWDSLinkRadio_Type.__name__=_D
_CoWDSLinkRadio_Object=MibTableColumn
coWDSLinkRadio=_CoWDSLinkRadio_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,3),_CoWDSLinkRadio_Type())
coWDSLinkRadio.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkRadio.setStatus(_A)
_CoWDSLinkPeerMacAddress_Type=MacAddress
_CoWDSLinkPeerMacAddress_Object=MibTableColumn
coWDSLinkPeerMacAddress=_CoWDSLinkPeerMacAddress_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,4),_CoWDSLinkPeerMacAddress_Type())
coWDSLinkPeerMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkPeerMacAddress.setStatus(_A)
_CoWDSLinkMaster_Type=TruthValue
_CoWDSLinkMaster_Object=MibTableColumn
coWDSLinkMaster=_CoWDSLinkMaster_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,5),_CoWDSLinkMaster_Type())
coWDSLinkMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkMaster.setStatus(_A)
_CoWDSLinkAuthorized_Type=TruthValue
_CoWDSLinkAuthorized_Object=MibTableColumn
coWDSLinkAuthorized=_CoWDSLinkAuthorized_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,6),_CoWDSLinkAuthorized_Type())
coWDSLinkAuthorized.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkAuthorized.setStatus(_A)
class _CoWDSLinkEncryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('wep',2),('tkip',3),('aes',4)))
_CoWDSLinkEncryption_Type.__name__=_D
_CoWDSLinkEncryption_Object=MibTableColumn
coWDSLinkEncryption=_CoWDSLinkEncryption_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,7),_CoWDSLinkEncryption_Type())
coWDSLinkEncryption.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkEncryption.setStatus(_A)
_CoWDSLinkIdleTime_Type=Unsigned32
_CoWDSLinkIdleTime_Object=MibTableColumn
coWDSLinkIdleTime=_CoWDSLinkIdleTime_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,8),_CoWDSLinkIdleTime_Type())
coWDSLinkIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkIdleTime.setStatus(_A)
if mibBuilder.loadTexts:coWDSLinkIdleTime.setUnits('seconds')
class _CoWDSLinkSNR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,92))
_CoWDSLinkSNR_Type.__name__=_D
_CoWDSLinkSNR_Object=MibTableColumn
coWDSLinkSNR=_CoWDSLinkSNR_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,9),_CoWDSLinkSNR_Type())
coWDSLinkSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkSNR.setStatus(_A)
if mibBuilder.loadTexts:coWDSLinkSNR.setUnits(_F)
_CoWDSLinkTxRate_Type=Unsigned32
_CoWDSLinkTxRate_Object=MibTableColumn
coWDSLinkTxRate=_CoWDSLinkTxRate_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,10),_CoWDSLinkTxRate_Type())
coWDSLinkTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkTxRate.setStatus(_A)
if mibBuilder.loadTexts:coWDSLinkTxRate.setUnits(_O)
_CoWDSLinkRxRate_Type=Unsigned32
_CoWDSLinkRxRate_Object=MibTableColumn
coWDSLinkRxRate=_CoWDSLinkRxRate_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,11),_CoWDSLinkRxRate_Type())
coWDSLinkRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkRxRate.setStatus(_A)
if mibBuilder.loadTexts:coWDSLinkRxRate.setUnits(_O)
class _CoWDSLinkIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoWDSLinkIfIndex_Type.__name__=_D
_CoWDSLinkIfIndex_Object=MibTableColumn
coWDSLinkIfIndex=_CoWDSLinkIfIndex_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,12),_CoWDSLinkIfIndex_Type())
coWDSLinkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkIfIndex.setStatus(_A)
_CoWDSLinkHT_Type=TruthValue
_CoWDSLinkHT_Object=MibTableColumn
coWDSLinkHT=_CoWDSLinkHT_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,13),_CoWDSLinkHT_Type())
coWDSLinkHT.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkHT.setStatus(_A)
_CoWDSLinkTxMCS_Type=Unsigned32
_CoWDSLinkTxMCS_Object=MibTableColumn
coWDSLinkTxMCS=_CoWDSLinkTxMCS_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,14),_CoWDSLinkTxMCS_Type())
coWDSLinkTxMCS.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkTxMCS.setStatus(_A)
_CoWDSLinkRxMCS_Type=Unsigned32
_CoWDSLinkRxMCS_Object=MibTableColumn
coWDSLinkRxMCS=_CoWDSLinkRxMCS_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,15),_CoWDSLinkRxMCS_Type())
coWDSLinkRxMCS.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkRxMCS.setStatus(_A)
_CoWDSLinkSignal_Type=Integer32
_CoWDSLinkSignal_Object=MibTableColumn
coWDSLinkSignal=_CoWDSLinkSignal_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,16),_CoWDSLinkSignal_Type())
coWDSLinkSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkSignal.setStatus(_A)
if mibBuilder.loadTexts:coWDSLinkSignal.setUnits(_F)
_CoWDSLinkNoise_Type=Integer32
_CoWDSLinkNoise_Object=MibTableColumn
coWDSLinkNoise=_CoWDSLinkNoise_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,17),_CoWDSLinkNoise_Type())
coWDSLinkNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkNoise.setStatus(_A)
if mibBuilder.loadTexts:coWDSLinkNoise.setUnits(_F)
_CoWDSLinkVHT_Type=TruthValue
_CoWDSLinkVHT_Object=MibTableColumn
coWDSLinkVHT=_CoWDSLinkVHT_Object((1,3,6,1,4,1,8744,5,33,1,4,1,1,18),_CoWDSLinkVHT_Type())
coWDSLinkVHT.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkVHT.setStatus(_A)
_CoWDSNetworkScanGroup_ObjectIdentity=ObjectIdentity
coWDSNetworkScanGroup=_CoWDSNetworkScanGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,33,1,5))
_CoWDSNetworkScanTable_Object=MibTable
coWDSNetworkScanTable=_CoWDSNetworkScanTable_Object((1,3,6,1,4,1,8744,5,33,1,5,1))
if mibBuilder.loadTexts:coWDSNetworkScanTable.setStatus(_A)
_CoWDSNetworkScanEntry_Object=MibTableRow
coWDSNetworkScanEntry=_CoWDSNetworkScanEntry_Object((1,3,6,1,4,1,8744,5,33,1,5,1,1))
coWDSNetworkScanEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:coWDSNetworkScanEntry.setStatus(_A)
class _CoWDSScanRadioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_CoWDSScanRadioIndex_Type.__name__=_D
_CoWDSScanRadioIndex_Object=MibTableColumn
coWDSScanRadioIndex=_CoWDSScanRadioIndex_Object((1,3,6,1,4,1,8744,5,33,1,5,1,1,1),_CoWDSScanRadioIndex_Type())
coWDSScanRadioIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:coWDSScanRadioIndex.setStatus(_A)
class _CoWDSScanPeerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CoWDSScanPeerIndex_Type.__name__=_D
_CoWDSScanPeerIndex_Object=MibTableColumn
coWDSScanPeerIndex=_CoWDSScanPeerIndex_Object((1,3,6,1,4,1,8744,5,33,1,5,1,1,2),_CoWDSScanPeerIndex_Type())
coWDSScanPeerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:coWDSScanPeerIndex.setStatus(_A)
_CoWDSScanGroupId_Type=Unsigned32
_CoWDSScanGroupId_Object=MibTableColumn
coWDSScanGroupId=_CoWDSScanGroupId_Object((1,3,6,1,4,1,8744,5,33,1,5,1,1,3),_CoWDSScanGroupId_Type())
coWDSScanGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSScanGroupId.setStatus(_A)
_CoWDSScanPeerMacAddress_Type=MacAddress
_CoWDSScanPeerMacAddress_Object=MibTableColumn
coWDSScanPeerMacAddress=_CoWDSScanPeerMacAddress_Object((1,3,6,1,4,1,8744,5,33,1,5,1,1,4),_CoWDSScanPeerMacAddress_Type())
coWDSScanPeerMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSScanPeerMacAddress.setStatus(_A)
class _CoWDSScanChannel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
_CoWDSScanChannel_Type.__name__=_G
_CoWDSScanChannel_Object=MibTableColumn
coWDSScanChannel=_CoWDSScanChannel_Object((1,3,6,1,4,1,8744,5,33,1,5,1,1,5),_CoWDSScanChannel_Type())
coWDSScanChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSScanChannel.setStatus(_A)
class _CoWDSScanSNR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,92))
_CoWDSScanSNR_Type.__name__=_D
_CoWDSScanSNR_Object=MibTableColumn
coWDSScanSNR=_CoWDSScanSNR_Object((1,3,6,1,4,1,8744,5,33,1,5,1,1,6),_CoWDSScanSNR_Type())
coWDSScanSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSScanSNR.setStatus(_A)
if mibBuilder.loadTexts:coWDSScanSNR.setUnits(_F)
class _CoWDSScanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('slave',2),(_M,3)))
_CoWDSScanMode_Type.__name__=_D
_CoWDSScanMode_Object=MibTableColumn
coWDSScanMode=_CoWDSScanMode_Object((1,3,6,1,4,1,8744,5,33,1,5,1,1,7),_CoWDSScanMode_Type())
coWDSScanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSScanMode.setStatus(_A)
_CoWDSScanAvailable_Type=TruthValue
_CoWDSScanAvailable_Object=MibTableColumn
coWDSScanAvailable=_CoWDSScanAvailable_Object((1,3,6,1,4,1,8744,5,33,1,5,1,1,8),_CoWDSScanAvailable_Type())
coWDSScanAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSScanAvailable.setStatus(_A)
_ColubrisWdsMIBConformance_ObjectIdentity=ObjectIdentity
colubrisWdsMIBConformance=_ColubrisWdsMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,33,2))
_ColubrisWdsMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisWdsMIBCompliances=_ColubrisWdsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,33,2,1))
_ColubrisWdsMIBGroups_ObjectIdentity=ObjectIdentity
colubrisWdsMIBGroups=_ColubrisWdsMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,33,2,2))
colubrisWDSInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,33,2,2,1))
colubrisWDSInfoMIBGroup.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:colubrisWDSInfoMIBGroup.setStatus(_A)
colubrisWDSRadioMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,33,2,2,2))
colubrisWDSRadioMIBGroup.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:colubrisWDSRadioMIBGroup.setStatus(_A)
colubrisWDSGroupMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,33,2,2,3))
colubrisWDSGroupMIBGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:colubrisWDSGroupMIBGroup.setStatus(_A)
colubrisWDSLinkMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,33,2,2,4))
colubrisWDSLinkMIBGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:colubrisWDSLinkMIBGroup.setStatus(_A)
colubrisWDSScanMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,33,2,2,5))
colubrisWDSScanMIBGroup.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:colubrisWDSScanMIBGroup.setStatus(_A)
colubrisWdsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,33,2,1,1))
colubrisWdsMIBCompliance.setObjects(*((_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:colubrisWdsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'colubrisWdsMIB':colubrisWdsMIB,'colubrisWdsMIBObjects':colubrisWdsMIBObjects,'coWDSInfoGroup':coWDSInfoGroup,_R:coWDSNumberOfGroup,_S:coWDSDynamicModeImplemented,'coWDSRadioGroup':coWDSRadioGroup,'coWDSRadioTable':coWDSRadioTable,'coWDSRadioEntry':coWDSRadioEntry,_K:coWDSRadioIndex,_T:coWDSRadioAckDistance,_U:coWDSRadioQoS,'coWDSGroupGroup':coWDSGroupGroup,'coWDSGroupTable':coWDSGroupTable,'coWDSGroupEntry':coWDSGroupEntry,_H:coWDSGroupIndex,_V:coWDSGroupName,_W:coWDSGroupState,_X:coWDSGroupSecurity,_Y:coWDSGroupAddressing,_Z:coWDSGroupStaticMacAddress,_a:coWDSGroupDynamicMode,_b:coWDSGroupDynamicGroupId,'coWDSLinkGroup':coWDSLinkGroup,'coWDSLinkTable':coWDSLinkTable,'coWDSLinkEntry':coWDSLinkEntry,_N:coWDSLinkIndex,_c:coWDSLinkState,_d:coWDSLinkRadio,_e:coWDSLinkPeerMacAddress,_f:coWDSLinkMaster,_g:coWDSLinkAuthorized,_h:coWDSLinkEncryption,_i:coWDSLinkIdleTime,_j:coWDSLinkSNR,_k:coWDSLinkTxRate,_l:coWDSLinkRxRate,_m:coWDSLinkIfIndex,_n:coWDSLinkHT,_o:coWDSLinkTxMCS,_p:coWDSLinkRxMCS,_q:coWDSLinkSignal,_r:coWDSLinkNoise,_s:coWDSLinkVHT,'coWDSNetworkScanGroup':coWDSNetworkScanGroup,'coWDSNetworkScanTable':coWDSNetworkScanTable,'coWDSNetworkScanEntry':coWDSNetworkScanEntry,_P:coWDSScanRadioIndex,_Q:coWDSScanPeerIndex,_t:coWDSScanGroupId,_u:coWDSScanPeerMacAddress,_v:coWDSScanChannel,_w:coWDSScanSNR,_x:coWDSScanMode,_y:coWDSScanAvailable,'colubrisWdsMIBConformance':colubrisWdsMIBConformance,'colubrisWdsMIBCompliances':colubrisWdsMIBCompliances,'colubrisWdsMIBCompliance':colubrisWdsMIBCompliance,'colubrisWdsMIBGroups':colubrisWdsMIBGroups,_z:colubrisWDSInfoMIBGroup,_A0:colubrisWDSRadioMIBGroup,_A1:colubrisWDSGroupMIBGroup,_A2:colubrisWDSLinkMIBGroup,_A3:colubrisWDSScanMIBGroup})