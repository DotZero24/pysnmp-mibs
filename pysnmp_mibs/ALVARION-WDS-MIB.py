_w='alvarionWDSScanMIBGroup'
_v='alvarionWDSLinkMIBGroup'
_u='alvarionWDSGroupMIBGroup'
_t='alvarionWDSRadioMIBGroup'
_s='alvarionWDSInfoMIBGroup'
_r='coWDSScanAvailable'
_q='coWDSScanMode'
_p='coWDSScanSNR'
_o='coWDSScanChannel'
_n='coWDSScanPeerMacAddress'
_m='coWDSScanGroupId'
_l='coWDSLinkIfIndex'
_k='coWDSLinkRxRate'
_j='coWDSLinkTxRate'
_i='coWDSLinkSNR'
_h='coWDSLinkIdleTime'
_g='coWDSLinkEncryption'
_f='coWDSLinkAuthorized'
_e='coWDSLinkMaster'
_d='coWDSLinkPeerMacAddress'
_c='coWDSLinkRadio'
_b='coWDSLinkState'
_a='coWDSGroupDynamicGroupId'
_Z='coWDSGroupDynamicMode'
_Y='coWDSGroupStaticMacAddress'
_X='coWDSGroupAddressing'
_W='coWDSGroupSecurity'
_V='coWDSGroupState'
_U='coWDSGroupName'
_T='coWDSRadioQoS'
_S='coWDSRadioAckDistance'
_R='coWDSDynamicModeImplemented'
_Q='coWDSNumberOfGroup'
_P='coWDSScanPeerIndex'
_O='coWDSScanRadioIndex'
_N='500Kb/s'
_M='coWDSLinkIndex'
_L='alternateMaster'
_K='master'
_J='coWDSRadioIndex'
_I='DisplayString'
_H='none'
_G='coWDSGroupIndex'
_F='Unsigned32'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='ALVARION-WDS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','TextualConvention','TruthValue')
alvarionWdsMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,33))
_AlvarionWdsMIBObjects_ObjectIdentity=ObjectIdentity
alvarionWdsMIBObjects=_AlvarionWdsMIBObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,33,1))
_CoWDSInfoGroup_ObjectIdentity=ObjectIdentity
coWDSInfoGroup=_CoWDSInfoGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,33,1,1))
class _CoWDSNumberOfGroup_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_CoWDSNumberOfGroup_Type.__name__=_F
_CoWDSNumberOfGroup_Object=MibScalar
coWDSNumberOfGroup=_CoWDSNumberOfGroup_Object((1,3,6,1,4,1,12394,1,10,5,33,1,1,1),_CoWDSNumberOfGroup_Type())
coWDSNumberOfGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSNumberOfGroup.setStatus(_A)
_CoWDSDynamicModeImplemented_Type=TruthValue
_CoWDSDynamicModeImplemented_Object=MibScalar
coWDSDynamicModeImplemented=_CoWDSDynamicModeImplemented_Object((1,3,6,1,4,1,12394,1,10,5,33,1,1,2),_CoWDSDynamicModeImplemented_Type())
coWDSDynamicModeImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSDynamicModeImplemented.setStatus(_A)
_CoWDSRadioGroup_ObjectIdentity=ObjectIdentity
coWDSRadioGroup=_CoWDSRadioGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,33,1,2))
_CoWDSRadioTable_Object=MibTable
coWDSRadioTable=_CoWDSRadioTable_Object((1,3,6,1,4,1,12394,1,10,5,33,1,2,1))
if mibBuilder.loadTexts:coWDSRadioTable.setStatus(_A)
_CoWDSRadioEntry_Object=MibTableRow
coWDSRadioEntry=_CoWDSRadioEntry_Object((1,3,6,1,4,1,12394,1,10,5,33,1,2,1,1))
coWDSRadioEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:coWDSRadioEntry.setStatus(_A)
class _CoWDSRadioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_CoWDSRadioIndex_Type.__name__=_D
_CoWDSRadioIndex_Object=MibTableColumn
coWDSRadioIndex=_CoWDSRadioIndex_Object((1,3,6,1,4,1,12394,1,10,5,33,1,2,1,1,1),_CoWDSRadioIndex_Type())
coWDSRadioIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:coWDSRadioIndex.setStatus(_A)
_CoWDSRadioAckDistance_Type=Unsigned32
_CoWDSRadioAckDistance_Object=MibTableColumn
coWDSRadioAckDistance=_CoWDSRadioAckDistance_Object((1,3,6,1,4,1,12394,1,10,5,33,1,2,1,1,2),_CoWDSRadioAckDistance_Type())
coWDSRadioAckDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSRadioAckDistance.setStatus(_A)
if mibBuilder.loadTexts:coWDSRadioAckDistance.setUnits('km')
class _CoWDSRadioQoS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('disabled',1),('vlan',2),('veryHigh',3),('high',4),('normal',5),('low',6),('diffSrv',7),('tos',8),('ipQos',9)))
_CoWDSRadioQoS_Type.__name__=_D
_CoWDSRadioQoS_Object=MibTableColumn
coWDSRadioQoS=_CoWDSRadioQoS_Object((1,3,6,1,4,1,12394,1,10,5,33,1,2,1,1,3),_CoWDSRadioQoS_Type())
coWDSRadioQoS.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSRadioQoS.setStatus(_A)
_CoWDSGroupGroup_ObjectIdentity=ObjectIdentity
coWDSGroupGroup=_CoWDSGroupGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,33,1,3))
_CoWDSGroupTable_Object=MibTable
coWDSGroupTable=_CoWDSGroupTable_Object((1,3,6,1,4,1,12394,1,10,5,33,1,3,1))
if mibBuilder.loadTexts:coWDSGroupTable.setStatus(_A)
_CoWDSGroupEntry_Object=MibTableRow
coWDSGroupEntry=_CoWDSGroupEntry_Object((1,3,6,1,4,1,12394,1,10,5,33,1,3,1,1))
coWDSGroupEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:coWDSGroupEntry.setStatus(_A)
class _CoWDSGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_CoWDSGroupIndex_Type.__name__=_D
_CoWDSGroupIndex_Object=MibTableColumn
coWDSGroupIndex=_CoWDSGroupIndex_Object((1,3,6,1,4,1,12394,1,10,5,33,1,3,1,1,1),_CoWDSGroupIndex_Type())
coWDSGroupIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:coWDSGroupIndex.setStatus(_A)
class _CoWDSGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CoWDSGroupName_Type.__name__=_I
_CoWDSGroupName_Object=MibTableColumn
coWDSGroupName=_CoWDSGroupName_Object((1,3,6,1,4,1,12394,1,10,5,33,1,3,1,1,2),_CoWDSGroupName_Type())
coWDSGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSGroupName.setStatus(_A)
class _CoWDSGroupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_CoWDSGroupState_Type.__name__=_D
_CoWDSGroupState_Object=MibTableColumn
coWDSGroupState=_CoWDSGroupState_Object((1,3,6,1,4,1,12394,1,10,5,33,1,3,1,1,3),_CoWDSGroupState_Type())
coWDSGroupState.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSGroupState.setStatus(_A)
class _CoWDSGroupSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('wep',2),('tkip',3),('aes',4)))
_CoWDSGroupSecurity_Type.__name__=_D
_CoWDSGroupSecurity_Object=MibTableColumn
coWDSGroupSecurity=_CoWDSGroupSecurity_Object((1,3,6,1,4,1,12394,1,10,5,33,1,3,1,1,4),_CoWDSGroupSecurity_Type())
coWDSGroupSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSGroupSecurity.setStatus(_A)
class _CoWDSGroupAddressing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_CoWDSGroupAddressing_Type.__name__=_D
_CoWDSGroupAddressing_Object=MibTableColumn
coWDSGroupAddressing=_CoWDSGroupAddressing_Object((1,3,6,1,4,1,12394,1,10,5,33,1,3,1,1,5),_CoWDSGroupAddressing_Type())
coWDSGroupAddressing.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSGroupAddressing.setStatus(_A)
_CoWDSGroupStaticMacAddress_Type=MacAddress
_CoWDSGroupStaticMacAddress_Object=MibTableColumn
coWDSGroupStaticMacAddress=_CoWDSGroupStaticMacAddress_Object((1,3,6,1,4,1,12394,1,10,5,33,1,3,1,1,6),_CoWDSGroupStaticMacAddress_Type())
coWDSGroupStaticMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSGroupStaticMacAddress.setStatus(_A)
class _CoWDSGroupDynamicMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),(_K,1),('slave',2),(_L,3)))
_CoWDSGroupDynamicMode_Type.__name__=_D
_CoWDSGroupDynamicMode_Object=MibTableColumn
coWDSGroupDynamicMode=_CoWDSGroupDynamicMode_Object((1,3,6,1,4,1,12394,1,10,5,33,1,3,1,1,7),_CoWDSGroupDynamicMode_Type())
coWDSGroupDynamicMode.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSGroupDynamicMode.setStatus(_A)
_CoWDSGroupDynamicGroupId_Type=Unsigned32
_CoWDSGroupDynamicGroupId_Object=MibTableColumn
coWDSGroupDynamicGroupId=_CoWDSGroupDynamicGroupId_Object((1,3,6,1,4,1,12394,1,10,5,33,1,3,1,1,8),_CoWDSGroupDynamicGroupId_Type())
coWDSGroupDynamicGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSGroupDynamicGroupId.setStatus(_A)
_CoWDSLinkGroup_ObjectIdentity=ObjectIdentity
coWDSLinkGroup=_CoWDSLinkGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,33,1,4))
_CoWDSLinkTable_Object=MibTable
coWDSLinkTable=_CoWDSLinkTable_Object((1,3,6,1,4,1,12394,1,10,5,33,1,4,1))
if mibBuilder.loadTexts:coWDSLinkTable.setStatus(_A)
_CoWDSLinkEntry_Object=MibTableRow
coWDSLinkEntry=_CoWDSLinkEntry_Object((1,3,6,1,4,1,12394,1,10,5,33,1,4,1,1))
coWDSLinkEntry.setIndexNames((0,_B,_G),(0,_B,_M))
if mibBuilder.loadTexts:coWDSLinkEntry.setStatus(_A)
class _CoWDSLinkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,54))
_CoWDSLinkIndex_Type.__name__=_D
_CoWDSLinkIndex_Object=MibTableColumn
coWDSLinkIndex=_CoWDSLinkIndex_Object((1,3,6,1,4,1,12394,1,10,5,33,1,4,1,1,1),_CoWDSLinkIndex_Type())
coWDSLinkIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:coWDSLinkIndex.setStatus(_A)
class _CoWDSLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('down',1),('acquiring',2),('inactive',3),('active',4)))
_CoWDSLinkState_Type.__name__=_D
_CoWDSLinkState_Object=MibTableColumn
coWDSLinkState=_CoWDSLinkState_Object((1,3,6,1,4,1,12394,1,10,5,33,1,4,1,1,2),_CoWDSLinkState_Type())
coWDSLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkState.setStatus(_A)
class _CoWDSLinkRadio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_CoWDSLinkRadio_Type.__name__=_D
_CoWDSLinkRadio_Object=MibTableColumn
coWDSLinkRadio=_CoWDSLinkRadio_Object((1,3,6,1,4,1,12394,1,10,5,33,1,4,1,1,3),_CoWDSLinkRadio_Type())
coWDSLinkRadio.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkRadio.setStatus(_A)
_CoWDSLinkPeerMacAddress_Type=MacAddress
_CoWDSLinkPeerMacAddress_Object=MibTableColumn
coWDSLinkPeerMacAddress=_CoWDSLinkPeerMacAddress_Object((1,3,6,1,4,1,12394,1,10,5,33,1,4,1,1,4),_CoWDSLinkPeerMacAddress_Type())
coWDSLinkPeerMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkPeerMacAddress.setStatus(_A)
_CoWDSLinkMaster_Type=TruthValue
_CoWDSLinkMaster_Object=MibTableColumn
coWDSLinkMaster=_CoWDSLinkMaster_Object((1,3,6,1,4,1,12394,1,10,5,33,1,4,1,1,5),_CoWDSLinkMaster_Type())
coWDSLinkMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkMaster.setStatus(_A)
_CoWDSLinkAuthorized_Type=TruthValue
_CoWDSLinkAuthorized_Object=MibTableColumn
coWDSLinkAuthorized=_CoWDSLinkAuthorized_Object((1,3,6,1,4,1,12394,1,10,5,33,1,4,1,1,6),_CoWDSLinkAuthorized_Type())
coWDSLinkAuthorized.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkAuthorized.setStatus(_A)
class _CoWDSLinkEncryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('wep',2),('tkip',3),('aes',4)))
_CoWDSLinkEncryption_Type.__name__=_D
_CoWDSLinkEncryption_Object=MibTableColumn
coWDSLinkEncryption=_CoWDSLinkEncryption_Object((1,3,6,1,4,1,12394,1,10,5,33,1,4,1,1,7),_CoWDSLinkEncryption_Type())
coWDSLinkEncryption.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkEncryption.setStatus(_A)
_CoWDSLinkIdleTime_Type=Unsigned32
_CoWDSLinkIdleTime_Object=MibTableColumn
coWDSLinkIdleTime=_CoWDSLinkIdleTime_Object((1,3,6,1,4,1,12394,1,10,5,33,1,4,1,1,8),_CoWDSLinkIdleTime_Type())
coWDSLinkIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkIdleTime.setStatus(_A)
if mibBuilder.loadTexts:coWDSLinkIdleTime.setUnits('seconds')
class _CoWDSLinkSNR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,92))
_CoWDSLinkSNR_Type.__name__=_D
_CoWDSLinkSNR_Object=MibTableColumn
coWDSLinkSNR=_CoWDSLinkSNR_Object((1,3,6,1,4,1,12394,1,10,5,33,1,4,1,1,9),_CoWDSLinkSNR_Type())
coWDSLinkSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkSNR.setStatus(_A)
if mibBuilder.loadTexts:coWDSLinkSNR.setUnits('dBm')
_CoWDSLinkTxRate_Type=Unsigned32
_CoWDSLinkTxRate_Object=MibTableColumn
coWDSLinkTxRate=_CoWDSLinkTxRate_Object((1,3,6,1,4,1,12394,1,10,5,33,1,4,1,1,10),_CoWDSLinkTxRate_Type())
coWDSLinkTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkTxRate.setStatus(_A)
if mibBuilder.loadTexts:coWDSLinkTxRate.setUnits(_N)
_CoWDSLinkRxRate_Type=Unsigned32
_CoWDSLinkRxRate_Object=MibTableColumn
coWDSLinkRxRate=_CoWDSLinkRxRate_Object((1,3,6,1,4,1,12394,1,10,5,33,1,4,1,1,11),_CoWDSLinkRxRate_Type())
coWDSLinkRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkRxRate.setStatus(_A)
if mibBuilder.loadTexts:coWDSLinkRxRate.setUnits(_N)
class _CoWDSLinkIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoWDSLinkIfIndex_Type.__name__=_D
_CoWDSLinkIfIndex_Object=MibTableColumn
coWDSLinkIfIndex=_CoWDSLinkIfIndex_Object((1,3,6,1,4,1,12394,1,10,5,33,1,4,1,1,12),_CoWDSLinkIfIndex_Type())
coWDSLinkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSLinkIfIndex.setStatus(_A)
_CoWDSNetworkScanGroup_ObjectIdentity=ObjectIdentity
coWDSNetworkScanGroup=_CoWDSNetworkScanGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,33,1,5))
_CoWDSNetworkScanTable_Object=MibTable
coWDSNetworkScanTable=_CoWDSNetworkScanTable_Object((1,3,6,1,4,1,12394,1,10,5,33,1,5,1))
if mibBuilder.loadTexts:coWDSNetworkScanTable.setStatus(_A)
_CoWDSNetworkScanEntry_Object=MibTableRow
coWDSNetworkScanEntry=_CoWDSNetworkScanEntry_Object((1,3,6,1,4,1,12394,1,10,5,33,1,5,1,1))
coWDSNetworkScanEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:coWDSNetworkScanEntry.setStatus(_A)
class _CoWDSScanRadioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_CoWDSScanRadioIndex_Type.__name__=_D
_CoWDSScanRadioIndex_Object=MibTableColumn
coWDSScanRadioIndex=_CoWDSScanRadioIndex_Object((1,3,6,1,4,1,12394,1,10,5,33,1,5,1,1,1),_CoWDSScanRadioIndex_Type())
coWDSScanRadioIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:coWDSScanRadioIndex.setStatus(_A)
class _CoWDSScanPeerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CoWDSScanPeerIndex_Type.__name__=_D
_CoWDSScanPeerIndex_Object=MibTableColumn
coWDSScanPeerIndex=_CoWDSScanPeerIndex_Object((1,3,6,1,4,1,12394,1,10,5,33,1,5,1,1,2),_CoWDSScanPeerIndex_Type())
coWDSScanPeerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:coWDSScanPeerIndex.setStatus(_A)
_CoWDSScanGroupId_Type=Unsigned32
_CoWDSScanGroupId_Object=MibTableColumn
coWDSScanGroupId=_CoWDSScanGroupId_Object((1,3,6,1,4,1,12394,1,10,5,33,1,5,1,1,3),_CoWDSScanGroupId_Type())
coWDSScanGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSScanGroupId.setStatus(_A)
_CoWDSScanPeerMacAddress_Type=MacAddress
_CoWDSScanPeerMacAddress_Object=MibTableColumn
coWDSScanPeerMacAddress=_CoWDSScanPeerMacAddress_Object((1,3,6,1,4,1,12394,1,10,5,33,1,5,1,1,4),_CoWDSScanPeerMacAddress_Type())
coWDSScanPeerMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSScanPeerMacAddress.setStatus(_A)
class _CoWDSScanChannel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
_CoWDSScanChannel_Type.__name__=_F
_CoWDSScanChannel_Object=MibTableColumn
coWDSScanChannel=_CoWDSScanChannel_Object((1,3,6,1,4,1,12394,1,10,5,33,1,5,1,1,5),_CoWDSScanChannel_Type())
coWDSScanChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSScanChannel.setStatus(_A)
class _CoWDSScanSNR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,92))
_CoWDSScanSNR_Type.__name__=_D
_CoWDSScanSNR_Object=MibTableColumn
coWDSScanSNR=_CoWDSScanSNR_Object((1,3,6,1,4,1,12394,1,10,5,33,1,5,1,1,6),_CoWDSScanSNR_Type())
coWDSScanSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSScanSNR.setStatus(_A)
if mibBuilder.loadTexts:coWDSScanSNR.setUnits('dBm')
class _CoWDSScanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('slave',2),(_L,3)))
_CoWDSScanMode_Type.__name__=_D
_CoWDSScanMode_Object=MibTableColumn
coWDSScanMode=_CoWDSScanMode_Object((1,3,6,1,4,1,12394,1,10,5,33,1,5,1,1,7),_CoWDSScanMode_Type())
coWDSScanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSScanMode.setStatus(_A)
_CoWDSScanAvailable_Type=TruthValue
_CoWDSScanAvailable_Object=MibTableColumn
coWDSScanAvailable=_CoWDSScanAvailable_Object((1,3,6,1,4,1,12394,1,10,5,33,1,5,1,1,8),_CoWDSScanAvailable_Type())
coWDSScanAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:coWDSScanAvailable.setStatus(_A)
_AlvarionWdsMIBConformance_ObjectIdentity=ObjectIdentity
alvarionWdsMIBConformance=_AlvarionWdsMIBConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,33,2))
_AlvarionWdsMIBCompliances_ObjectIdentity=ObjectIdentity
alvarionWdsMIBCompliances=_AlvarionWdsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,33,2,1))
_AlvarionWdsMIBGroups_ObjectIdentity=ObjectIdentity
alvarionWdsMIBGroups=_AlvarionWdsMIBGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,33,2,2))
alvarionWDSInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,33,2,2,1))
alvarionWDSInfoMIBGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:alvarionWDSInfoMIBGroup.setStatus(_A)
alvarionWDSRadioMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,33,2,2,2))
alvarionWDSRadioMIBGroup.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:alvarionWDSRadioMIBGroup.setStatus(_A)
alvarionWDSGroupMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,33,2,2,3))
alvarionWDSGroupMIBGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:alvarionWDSGroupMIBGroup.setStatus(_A)
alvarionWDSLinkMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,33,2,2,4))
alvarionWDSLinkMIBGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:alvarionWDSLinkMIBGroup.setStatus(_A)
alvarionWDSScanMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,33,2,2,5))
alvarionWDSScanMIBGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:alvarionWDSScanMIBGroup.setStatus(_A)
alvarionWdsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,33,2,1,1))
alvarionWdsMIBCompliance.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:alvarionWdsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alvarionWdsMIB':alvarionWdsMIB,'alvarionWdsMIBObjects':alvarionWdsMIBObjects,'coWDSInfoGroup':coWDSInfoGroup,_Q:coWDSNumberOfGroup,_R:coWDSDynamicModeImplemented,'coWDSRadioGroup':coWDSRadioGroup,'coWDSRadioTable':coWDSRadioTable,'coWDSRadioEntry':coWDSRadioEntry,_J:coWDSRadioIndex,_S:coWDSRadioAckDistance,_T:coWDSRadioQoS,'coWDSGroupGroup':coWDSGroupGroup,'coWDSGroupTable':coWDSGroupTable,'coWDSGroupEntry':coWDSGroupEntry,_G:coWDSGroupIndex,_U:coWDSGroupName,_V:coWDSGroupState,_W:coWDSGroupSecurity,_X:coWDSGroupAddressing,_Y:coWDSGroupStaticMacAddress,_Z:coWDSGroupDynamicMode,_a:coWDSGroupDynamicGroupId,'coWDSLinkGroup':coWDSLinkGroup,'coWDSLinkTable':coWDSLinkTable,'coWDSLinkEntry':coWDSLinkEntry,_M:coWDSLinkIndex,_b:coWDSLinkState,_c:coWDSLinkRadio,_d:coWDSLinkPeerMacAddress,_e:coWDSLinkMaster,_f:coWDSLinkAuthorized,_g:coWDSLinkEncryption,_h:coWDSLinkIdleTime,_i:coWDSLinkSNR,_j:coWDSLinkTxRate,_k:coWDSLinkRxRate,_l:coWDSLinkIfIndex,'coWDSNetworkScanGroup':coWDSNetworkScanGroup,'coWDSNetworkScanTable':coWDSNetworkScanTable,'coWDSNetworkScanEntry':coWDSNetworkScanEntry,_O:coWDSScanRadioIndex,_P:coWDSScanPeerIndex,_m:coWDSScanGroupId,_n:coWDSScanPeerMacAddress,_o:coWDSScanChannel,_p:coWDSScanSNR,_q:coWDSScanMode,_r:coWDSScanAvailable,'alvarionWdsMIBConformance':alvarionWdsMIBConformance,'alvarionWdsMIBCompliances':alvarionWdsMIBCompliances,'alvarionWdsMIBCompliance':alvarionWdsMIBCompliance,'alvarionWdsMIBGroups':alvarionWdsMIBGroups,_s:alvarionWDSInfoMIBGroup,_t:alvarionWDSRadioMIBGroup,_u:alvarionWDSGroupMIBGroup,_v:alvarionWDSLinkMIBGroup,_w:alvarionWDSScanMIBGroup})