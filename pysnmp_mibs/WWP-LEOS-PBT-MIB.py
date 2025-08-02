_AJ='wwpLeosTcePbtTunnelReversionNotification'
_AI='wwpLeosTcePbtTunnelDeactivateNotification'
_AH='wwpLeosTcePbtTunnelActivateNotification'
_AG='wwpLeosPbtTunnelFaultNotification'
_AF='wwpLeosTcePbtEncapTnlReversionFromPairIndex'
_AE='wwpLeosTcePbtEncapTnlReversionToPairIndex'
_AD='wwpLeosPbtVirtualCircuitRxBytesLo'
_AC='wwpLeosPbtVirtualCircuitRxBytesHi'
_AB='wwpLeosPbtVirtualCircuitTxBytesLo'
_AA='wwpLeosPbtVirtualCircuitTxBytesHi'
_A9='wwpLeosPbtVirtualCircuitRowStatus'
_A8='wwpLeosPbtVirtualCircuitEncapTunnelIdInUse'
_A7='wwpLeosPbtVirtualCircuitOperState'
_A6='wwpLeosPbtVirtualCircuitEgressISID'
_A5='wwpLeosPbtVirtualCircuitIngressISID'
_A4='wwpLeosPbtVirtualCircuitDestBridgeIndex'
_A3='wwpLeosPbtVirtualCircuitFixedEncapTunnelId'
_A2='wwpLeosPbtVirtualCircuitName'
_A1='wwpLeosPbtReservedBVIDRowStatus'
_A0='wwpLeosPbtBridgeNameMacMapRowStatus'
_z='wwpLeosPbtBridgeNameMacMapUseCount'
_y='wwpLeosPbtBridgeNameMacMapMacAddr'
_x='wwpLeosPbtBridgeNameMacMapBridgeName'
_w='wwpLeosPbtServiceVlanTpid'
_v='wwpLeosPbtOperMode'
_u='wwpLeosPbtAdminMode'
_t='wwpLeosPbtTunnelReversionHoldTime'
_s='wwpLeosPbtTunnelReversionState'
_r='wwpLeosPbtTunnelTagEtype'
_q='wwpLeosPbtServiceTagEType'
_p='wwpLeosPbtBridgeMac'
_o='wwpLeosTcePbtServiceUserFrameL2TransformTagIndex'
_n='wwpLeosTcePbtServiceUserFrameL2TransformDirection'
_m='wwpLeosTcePbtDecapTnlIndex'
_l='standby'
_k='active'
_j='isidPcpMap'
_i='ignore'
_h='isidPcPMap'
_g='wwpLeosPbtLocalBridgeNameMacMapIndex'
_f='native'
_e='nonNative'
_d='milliseconds'
_c='wwpLeosTcePbtEncapTnlFwdState'
_b='wwpLeosTcePbtEncapTnlName'
_a='wwpLeosTcePbtServiceIndex'
_Z='wwpLeosPbtReservedBVID'
_Y='wwpLeosPbtBridgeNameMacMapIndex'
_X='wwpLeosVplsEncapTunnelBVID'
_W='wwpLeosVplsEncapTunnelActive'
_V='Unsigned32'
_U='wwpLeosTcePbtTnlGroupName'
_T='wwpLeosTcePbtEncapTnlIndex'
_S='accessible-for-notify'
_R='fixed'
_Q='not-accessible'
_P='wwpLeosPbtVirtualCircuitIndex'
_O='TruthValue'
_N='OctetString'
_M='wwpLeosTcePbtTnlGroupIndex'
_L='wwpLeosVplsEncapTunnelName'
_K='wwpLeosVplsEncapTunnelId'
_J='disabled'
_I='enabled'
_H='WWP-LEOS-VPLS-MIB'
_G='read-write'
_F='DisplayString'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='WWP-LEOS-PBT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_V,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention',_O)
wwpLeosVplsEncapTunnelActive,wwpLeosVplsEncapTunnelBVID,wwpLeosVplsEncapTunnelId,wwpLeosVplsEncapTunnelName=mibBuilder.importSymbols(_H,_W,_X,_K,_L)
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosPbtMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,38))
if mibBuilder.loadTexts:wwpLeosPbtMIB.setRevisions(('2011-07-05 00:00','2011-05-05 16:00','2011-01-31 00:00','2007-03-02 17:00','2006-08-25 17:00'))
_WwpLeosPbtMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosPbtMIBObjects=_WwpLeosPbtMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,38,1))
_WwpLeosPbt_ObjectIdentity=ObjectIdentity
wwpLeosPbt=_WwpLeosPbt_ObjectIdentity((1,3,6,1,4,1,6141,2,60,38,1,1))
_WwpLeosPbtGlobalAttrs_ObjectIdentity=ObjectIdentity
wwpLeosPbtGlobalAttrs=_WwpLeosPbtGlobalAttrs_ObjectIdentity((1,3,6,1,4,1,6141,2,60,38,1,1,1))
_WwpLeosPbtBridgeMac_Type=MacAddress
_WwpLeosPbtBridgeMac_Object=MibScalar
wwpLeosPbtBridgeMac=_WwpLeosPbtBridgeMac_Object((1,3,6,1,4,1,6141,2,60,38,1,1,1,1),_WwpLeosPbtBridgeMac_Type())
wwpLeosPbtBridgeMac.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosPbtBridgeMac.setStatus(_A)
class _WwpLeosPbtServiceTagEType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,2))
_WwpLeosPbtServiceTagEType_Type.__name__=_N
_WwpLeosPbtServiceTagEType_Object=MibScalar
wwpLeosPbtServiceTagEType=_WwpLeosPbtServiceTagEType_Object((1,3,6,1,4,1,6141,2,60,38,1,1,1,2),_WwpLeosPbtServiceTagEType_Type())
wwpLeosPbtServiceTagEType.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosPbtServiceTagEType.setStatus(_A)
class _WwpLeosPbtTunnelTagEtype_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,2))
_WwpLeosPbtTunnelTagEtype_Type.__name__=_N
_WwpLeosPbtTunnelTagEtype_Object=MibScalar
wwpLeosPbtTunnelTagEtype=_WwpLeosPbtTunnelTagEtype_Object((1,3,6,1,4,1,6141,2,60,38,1,1,1,3),_WwpLeosPbtTunnelTagEtype_Type())
wwpLeosPbtTunnelTagEtype.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosPbtTunnelTagEtype.setStatus(_A)
class _WwpLeosPbtTunnelReversionState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosPbtTunnelReversionState_Type.__name__=_E
_WwpLeosPbtTunnelReversionState_Object=MibScalar
wwpLeosPbtTunnelReversionState=_WwpLeosPbtTunnelReversionState_Object((1,3,6,1,4,1,6141,2,60,38,1,1,1,4),_WwpLeosPbtTunnelReversionState_Type())
wwpLeosPbtTunnelReversionState.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosPbtTunnelReversionState.setStatus(_A)
class _WwpLeosPbtTunnelReversionHoldTime_Type(Unsigned32):defaultValue=3000
_WwpLeosPbtTunnelReversionHoldTime_Type.__name__=_V
_WwpLeosPbtTunnelReversionHoldTime_Object=MibScalar
wwpLeosPbtTunnelReversionHoldTime=_WwpLeosPbtTunnelReversionHoldTime_Object((1,3,6,1,4,1,6141,2,60,38,1,1,1,5),_WwpLeosPbtTunnelReversionHoldTime_Type())
wwpLeosPbtTunnelReversionHoldTime.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosPbtTunnelReversionHoldTime.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosPbtTunnelReversionHoldTime.setUnits(_d)
class _WwpLeosPbtTransitTunnelEtypeRemark_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosPbtTransitTunnelEtypeRemark_Type.__name__=_E
_WwpLeosPbtTransitTunnelEtypeRemark_Object=MibScalar
wwpLeosPbtTransitTunnelEtypeRemark=_WwpLeosPbtTransitTunnelEtypeRemark_Object((1,3,6,1,4,1,6141,2,60,38,1,1,1,6),_WwpLeosPbtTransitTunnelEtypeRemark_Type())
wwpLeosPbtTransitTunnelEtypeRemark.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosPbtTransitTunnelEtypeRemark.setStatus(_A)
class _WwpLeosPbtAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_WwpLeosPbtAdminMode_Type.__name__=_E
_WwpLeosPbtAdminMode_Object=MibScalar
wwpLeosPbtAdminMode=_WwpLeosPbtAdminMode_Object((1,3,6,1,4,1,6141,2,60,38,1,1,1,7),_WwpLeosPbtAdminMode_Type())
wwpLeosPbtAdminMode.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosPbtAdminMode.setStatus(_A)
class _WwpLeosPbtOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_WwpLeosPbtOperMode_Type.__name__=_E
_WwpLeosPbtOperMode_Object=MibScalar
wwpLeosPbtOperMode=_WwpLeosPbtOperMode_Object((1,3,6,1,4,1,6141,2,60,38,1,1,1,8),_WwpLeosPbtOperMode_Type())
wwpLeosPbtOperMode.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosPbtOperMode.setStatus(_A)
class _WwpLeosPbtServiceVlanTpid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,2))
_WwpLeosPbtServiceVlanTpid_Type.__name__=_N
_WwpLeosPbtServiceVlanTpid_Object=MibScalar
wwpLeosPbtServiceVlanTpid=_WwpLeosPbtServiceVlanTpid_Object((1,3,6,1,4,1,6141,2,60,38,1,1,1,9),_WwpLeosPbtServiceVlanTpid_Type())
wwpLeosPbtServiceVlanTpid.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosPbtServiceVlanTpid.setStatus(_A)
class _WwpLeosPbtTunnelSwitchOverHoldTime_Type(Unsigned32):defaultValue=0
_WwpLeosPbtTunnelSwitchOverHoldTime_Type.__name__=_V
_WwpLeosPbtTunnelSwitchOverHoldTime_Object=MibScalar
wwpLeosPbtTunnelSwitchOverHoldTime=_WwpLeosPbtTunnelSwitchOverHoldTime_Object((1,3,6,1,4,1,6141,2,60,38,1,1,1,10),_WwpLeosPbtTunnelSwitchOverHoldTime_Type())
wwpLeosPbtTunnelSwitchOverHoldTime.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosPbtTunnelSwitchOverHoldTime.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosPbtTunnelSwitchOverHoldTime.setUnits(_d)
_WwpLeosPbtBridgeNameMacMapTable_Object=MibTable
wwpLeosPbtBridgeNameMacMapTable=_WwpLeosPbtBridgeNameMacMapTable_Object((1,3,6,1,4,1,6141,2,60,38,1,1,2))
if mibBuilder.loadTexts:wwpLeosPbtBridgeNameMacMapTable.setStatus(_A)
_WwpLeosPbtBridgeNameMacMapEntry_Object=MibTableRow
wwpLeosPbtBridgeNameMacMapEntry=_WwpLeosPbtBridgeNameMacMapEntry_Object((1,3,6,1,4,1,6141,2,60,38,1,1,2,1))
wwpLeosPbtBridgeNameMacMapEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:wwpLeosPbtBridgeNameMacMapEntry.setStatus(_A)
class _WwpLeosPbtBridgeNameMacMapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_WwpLeosPbtBridgeNameMacMapIndex_Type.__name__=_E
_WwpLeosPbtBridgeNameMacMapIndex_Object=MibTableColumn
wwpLeosPbtBridgeNameMacMapIndex=_WwpLeosPbtBridgeNameMacMapIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,2,1,1),_WwpLeosPbtBridgeNameMacMapIndex_Type())
wwpLeosPbtBridgeNameMacMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPbtBridgeNameMacMapIndex.setStatus(_A)
class _WwpLeosPbtBridgeNameMacMapBridgeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_WwpLeosPbtBridgeNameMacMapBridgeName_Type.__name__=_F
_WwpLeosPbtBridgeNameMacMapBridgeName_Object=MibTableColumn
wwpLeosPbtBridgeNameMacMapBridgeName=_WwpLeosPbtBridgeNameMacMapBridgeName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,2,1,2),_WwpLeosPbtBridgeNameMacMapBridgeName_Type())
wwpLeosPbtBridgeNameMacMapBridgeName.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosPbtBridgeNameMacMapBridgeName.setStatus(_A)
_WwpLeosPbtBridgeNameMacMapMacAddr_Type=MacAddress
_WwpLeosPbtBridgeNameMacMapMacAddr_Object=MibTableColumn
wwpLeosPbtBridgeNameMacMapMacAddr=_WwpLeosPbtBridgeNameMacMapMacAddr_Object((1,3,6,1,4,1,6141,2,60,38,1,1,2,1,3),_WwpLeosPbtBridgeNameMacMapMacAddr_Type())
wwpLeosPbtBridgeNameMacMapMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosPbtBridgeNameMacMapMacAddr.setStatus(_A)
_WwpLeosPbtBridgeNameMacMapUseCount_Type=Counter32
_WwpLeosPbtBridgeNameMacMapUseCount_Object=MibTableColumn
wwpLeosPbtBridgeNameMacMapUseCount=_WwpLeosPbtBridgeNameMacMapUseCount_Object((1,3,6,1,4,1,6141,2,60,38,1,1,2,1,4),_WwpLeosPbtBridgeNameMacMapUseCount_Type())
wwpLeosPbtBridgeNameMacMapUseCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPbtBridgeNameMacMapUseCount.setStatus(_A)
_WwpLeosPbtBridgeNameMacMapRowStatus_Type=RowStatus
_WwpLeosPbtBridgeNameMacMapRowStatus_Object=MibTableColumn
wwpLeosPbtBridgeNameMacMapRowStatus=_WwpLeosPbtBridgeNameMacMapRowStatus_Object((1,3,6,1,4,1,6141,2,60,38,1,1,2,1,5),_WwpLeosPbtBridgeNameMacMapRowStatus_Type())
wwpLeosPbtBridgeNameMacMapRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosPbtBridgeNameMacMapRowStatus.setStatus(_A)
_WwpLeosPbtReservedBVIDTable_Object=MibTable
wwpLeosPbtReservedBVIDTable=_WwpLeosPbtReservedBVIDTable_Object((1,3,6,1,4,1,6141,2,60,38,1,1,3))
if mibBuilder.loadTexts:wwpLeosPbtReservedBVIDTable.setStatus(_A)
_WwpLeosPbtReservedBVIDEntry_Object=MibTableRow
wwpLeosPbtReservedBVIDEntry=_WwpLeosPbtReservedBVIDEntry_Object((1,3,6,1,4,1,6141,2,60,38,1,1,3,1))
wwpLeosPbtReservedBVIDEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:wwpLeosPbtReservedBVIDEntry.setStatus(_A)
class _WwpLeosPbtReservedBVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_WwpLeosPbtReservedBVID_Type.__name__=_E
_WwpLeosPbtReservedBVID_Object=MibTableColumn
wwpLeosPbtReservedBVID=_WwpLeosPbtReservedBVID_Object((1,3,6,1,4,1,6141,2,60,38,1,1,3,1,1),_WwpLeosPbtReservedBVID_Type())
wwpLeosPbtReservedBVID.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPbtReservedBVID.setStatus(_A)
_WwpLeosPbtReservedBVIDRowStatus_Type=RowStatus
_WwpLeosPbtReservedBVIDRowStatus_Object=MibTableColumn
wwpLeosPbtReservedBVIDRowStatus=_WwpLeosPbtReservedBVIDRowStatus_Object((1,3,6,1,4,1,6141,2,60,38,1,1,3,1,2),_WwpLeosPbtReservedBVIDRowStatus_Type())
wwpLeosPbtReservedBVIDRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosPbtReservedBVIDRowStatus.setStatus(_A)
_WwpLeosPbtVirtualCircuitTable_Object=MibTable
wwpLeosPbtVirtualCircuitTable=_WwpLeosPbtVirtualCircuitTable_Object((1,3,6,1,4,1,6141,2,60,38,1,1,4))
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitTable.setStatus(_A)
_WwpLeosPbtVirtualCircuitEntry_Object=MibTableRow
wwpLeosPbtVirtualCircuitEntry=_WwpLeosPbtVirtualCircuitEntry_Object((1,3,6,1,4,1,6141,2,60,38,1,1,4,1))
wwpLeosPbtVirtualCircuitEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitEntry.setStatus(_A)
class _WwpLeosPbtVirtualCircuitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPbtVirtualCircuitIndex_Type.__name__=_E
_WwpLeosPbtVirtualCircuitIndex_Object=MibTableColumn
wwpLeosPbtVirtualCircuitIndex=_WwpLeosPbtVirtualCircuitIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,4,1,1),_WwpLeosPbtVirtualCircuitIndex_Type())
wwpLeosPbtVirtualCircuitIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitIndex.setStatus(_A)
class _WwpLeosPbtVirtualCircuitName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_WwpLeosPbtVirtualCircuitName_Type.__name__=_F
_WwpLeosPbtVirtualCircuitName_Object=MibTableColumn
wwpLeosPbtVirtualCircuitName=_WwpLeosPbtVirtualCircuitName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,4,1,2),_WwpLeosPbtVirtualCircuitName_Type())
wwpLeosPbtVirtualCircuitName.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitName.setStatus(_A)
_WwpLeosPbtVirtualCircuitFixedEncapTunnelId_Type=Integer32
_WwpLeosPbtVirtualCircuitFixedEncapTunnelId_Object=MibTableColumn
wwpLeosPbtVirtualCircuitFixedEncapTunnelId=_WwpLeosPbtVirtualCircuitFixedEncapTunnelId_Object((1,3,6,1,4,1,6141,2,60,38,1,1,4,1,3),_WwpLeosPbtVirtualCircuitFixedEncapTunnelId_Type())
wwpLeosPbtVirtualCircuitFixedEncapTunnelId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitFixedEncapTunnelId.setStatus(_A)
class _WwpLeosPbtVirtualCircuitDestBridgeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_WwpLeosPbtVirtualCircuitDestBridgeIndex_Type.__name__=_E
_WwpLeosPbtVirtualCircuitDestBridgeIndex_Object=MibTableColumn
wwpLeosPbtVirtualCircuitDestBridgeIndex=_WwpLeosPbtVirtualCircuitDestBridgeIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,4,1,4),_WwpLeosPbtVirtualCircuitDestBridgeIndex_Type())
wwpLeosPbtVirtualCircuitDestBridgeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitDestBridgeIndex.setStatus(_A)
class _WwpLeosPbtVirtualCircuitIngressISID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777215))
_WwpLeosPbtVirtualCircuitIngressISID_Type.__name__=_E
_WwpLeosPbtVirtualCircuitIngressISID_Object=MibTableColumn
wwpLeosPbtVirtualCircuitIngressISID=_WwpLeosPbtVirtualCircuitIngressISID_Object((1,3,6,1,4,1,6141,2,60,38,1,1,4,1,5),_WwpLeosPbtVirtualCircuitIngressISID_Type())
wwpLeosPbtVirtualCircuitIngressISID.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitIngressISID.setStatus(_A)
class _WwpLeosPbtVirtualCircuitEgressISID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777215))
_WwpLeosPbtVirtualCircuitEgressISID_Type.__name__=_E
_WwpLeosPbtVirtualCircuitEgressISID_Object=MibTableColumn
wwpLeosPbtVirtualCircuitEgressISID=_WwpLeosPbtVirtualCircuitEgressISID_Object((1,3,6,1,4,1,6141,2,60,38,1,1,4,1,6),_WwpLeosPbtVirtualCircuitEgressISID_Type())
wwpLeosPbtVirtualCircuitEgressISID.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitEgressISID.setStatus(_A)
class _WwpLeosPbtVirtualCircuitOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_WwpLeosPbtVirtualCircuitOperState_Type.__name__=_E
_WwpLeosPbtVirtualCircuitOperState_Object=MibTableColumn
wwpLeosPbtVirtualCircuitOperState=_WwpLeosPbtVirtualCircuitOperState_Object((1,3,6,1,4,1,6141,2,60,38,1,1,4,1,7),_WwpLeosPbtVirtualCircuitOperState_Type())
wwpLeosPbtVirtualCircuitOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitOperState.setStatus(_A)
_WwpLeosPbtVirtualCircuitEncapTunnelIdInUse_Type=Integer32
_WwpLeosPbtVirtualCircuitEncapTunnelIdInUse_Object=MibTableColumn
wwpLeosPbtVirtualCircuitEncapTunnelIdInUse=_WwpLeosPbtVirtualCircuitEncapTunnelIdInUse_Object((1,3,6,1,4,1,6141,2,60,38,1,1,4,1,8),_WwpLeosPbtVirtualCircuitEncapTunnelIdInUse_Type())
wwpLeosPbtVirtualCircuitEncapTunnelIdInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitEncapTunnelIdInUse.setStatus(_A)
_WwpLeosPbtVirtualCircuitRowStatus_Type=RowStatus
_WwpLeosPbtVirtualCircuitRowStatus_Object=MibTableColumn
wwpLeosPbtVirtualCircuitRowStatus=_WwpLeosPbtVirtualCircuitRowStatus_Object((1,3,6,1,4,1,6141,2,60,38,1,1,4,1,9),_WwpLeosPbtVirtualCircuitRowStatus_Type())
wwpLeosPbtVirtualCircuitRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitRowStatus.setStatus(_A)
_WwpLeosPbtVirtualCircuitRetainSTAG_Type=TruthValue
_WwpLeosPbtVirtualCircuitRetainSTAG_Object=MibTableColumn
wwpLeosPbtVirtualCircuitRetainSTAG=_WwpLeosPbtVirtualCircuitRetainSTAG_Object((1,3,6,1,4,1,6141,2,60,38,1,1,4,1,10),_WwpLeosPbtVirtualCircuitRetainSTAG_Type())
wwpLeosPbtVirtualCircuitRetainSTAG.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitRetainSTAG.setStatus(_A)
_WwpLeosPbtVirtualCircuitStag_Type=Integer32
_WwpLeosPbtVirtualCircuitStag_Object=MibTableColumn
wwpLeosPbtVirtualCircuitStag=_WwpLeosPbtVirtualCircuitStag_Object((1,3,6,1,4,1,6141,2,60,38,1,1,4,1,11),_WwpLeosPbtVirtualCircuitStag_Type())
wwpLeosPbtVirtualCircuitStag.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitStag.setStatus(_A)
_WwpLeosPbtVirtualCircuitStatsTable_Object=MibTable
wwpLeosPbtVirtualCircuitStatsTable=_WwpLeosPbtVirtualCircuitStatsTable_Object((1,3,6,1,4,1,6141,2,60,38,1,1,5))
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitStatsTable.setStatus(_A)
_WwpLeosPbtVirtualCircuitStatsEntry_Object=MibTableRow
wwpLeosPbtVirtualCircuitStatsEntry=_WwpLeosPbtVirtualCircuitStatsEntry_Object((1,3,6,1,4,1,6141,2,60,38,1,1,5,1))
wwpLeosPbtVirtualCircuitStatsEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitStatsEntry.setStatus(_A)
_WwpLeosPbtVirtualCircuitTxBytesHi_Type=Counter32
_WwpLeosPbtVirtualCircuitTxBytesHi_Object=MibTableColumn
wwpLeosPbtVirtualCircuitTxBytesHi=_WwpLeosPbtVirtualCircuitTxBytesHi_Object((1,3,6,1,4,1,6141,2,60,38,1,1,5,1,1),_WwpLeosPbtVirtualCircuitTxBytesHi_Type())
wwpLeosPbtVirtualCircuitTxBytesHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitTxBytesHi.setStatus(_A)
_WwpLeosPbtVirtualCircuitTxBytesLo_Type=Counter32
_WwpLeosPbtVirtualCircuitTxBytesLo_Object=MibTableColumn
wwpLeosPbtVirtualCircuitTxBytesLo=_WwpLeosPbtVirtualCircuitTxBytesLo_Object((1,3,6,1,4,1,6141,2,60,38,1,1,5,1,2),_WwpLeosPbtVirtualCircuitTxBytesLo_Type())
wwpLeosPbtVirtualCircuitTxBytesLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitTxBytesLo.setStatus(_A)
_WwpLeosPbtVirtualCircuitRxBytesHi_Type=Counter32
_WwpLeosPbtVirtualCircuitRxBytesHi_Object=MibTableColumn
wwpLeosPbtVirtualCircuitRxBytesHi=_WwpLeosPbtVirtualCircuitRxBytesHi_Object((1,3,6,1,4,1,6141,2,60,38,1,1,5,1,3),_WwpLeosPbtVirtualCircuitRxBytesHi_Type())
wwpLeosPbtVirtualCircuitRxBytesHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitRxBytesHi.setStatus(_A)
_WwpLeosPbtVirtualCircuitRxBytesLo_Type=Counter32
_WwpLeosPbtVirtualCircuitRxBytesLo_Object=MibTableColumn
wwpLeosPbtVirtualCircuitRxBytesLo=_WwpLeosPbtVirtualCircuitRxBytesLo_Object((1,3,6,1,4,1,6141,2,60,38,1,1,5,1,4),_WwpLeosPbtVirtualCircuitRxBytesLo_Type())
wwpLeosPbtVirtualCircuitRxBytesLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPbtVirtualCircuitRxBytesLo.setStatus(_A)
_WwpLeosPbtLocalBridgeNameMacMapTable_Object=MibTable
wwpLeosPbtLocalBridgeNameMacMapTable=_WwpLeosPbtLocalBridgeNameMacMapTable_Object((1,3,6,1,4,1,6141,2,60,38,1,1,6))
if mibBuilder.loadTexts:wwpLeosPbtLocalBridgeNameMacMapTable.setStatus(_A)
_WwpLeosPbtLocalBridgeNameMacMapEntry_Object=MibTableRow
wwpLeosPbtLocalBridgeNameMacMapEntry=_WwpLeosPbtLocalBridgeNameMacMapEntry_Object((1,3,6,1,4,1,6141,2,60,38,1,1,6,1))
wwpLeosPbtLocalBridgeNameMacMapEntry.setIndexNames((0,_B,_g))
if mibBuilder.loadTexts:wwpLeosPbtLocalBridgeNameMacMapEntry.setStatus(_A)
class _WwpLeosPbtLocalBridgeNameMacMapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_WwpLeosPbtLocalBridgeNameMacMapIndex_Type.__name__=_E
_WwpLeosPbtLocalBridgeNameMacMapIndex_Object=MibTableColumn
wwpLeosPbtLocalBridgeNameMacMapIndex=_WwpLeosPbtLocalBridgeNameMacMapIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,6,1,1),_WwpLeosPbtLocalBridgeNameMacMapIndex_Type())
wwpLeosPbtLocalBridgeNameMacMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPbtLocalBridgeNameMacMapIndex.setStatus(_A)
class _WwpLeosPbtLocalBridgeNameMacMapBridgeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_WwpLeosPbtLocalBridgeNameMacMapBridgeName_Type.__name__=_F
_WwpLeosPbtLocalBridgeNameMacMapBridgeName_Object=MibTableColumn
wwpLeosPbtLocalBridgeNameMacMapBridgeName=_WwpLeosPbtLocalBridgeNameMacMapBridgeName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,6,1,2),_WwpLeosPbtLocalBridgeNameMacMapBridgeName_Type())
wwpLeosPbtLocalBridgeNameMacMapBridgeName.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosPbtLocalBridgeNameMacMapBridgeName.setStatus(_A)
_WwpLeosPbtLocalBridgeNameMacMapMacAddr_Type=MacAddress
_WwpLeosPbtLocalBridgeNameMacMapMacAddr_Object=MibTableColumn
wwpLeosPbtLocalBridgeNameMacMapMacAddr=_WwpLeosPbtLocalBridgeNameMacMapMacAddr_Object((1,3,6,1,4,1,6141,2,60,38,1,1,6,1,3),_WwpLeosPbtLocalBridgeNameMacMapMacAddr_Type())
wwpLeosPbtLocalBridgeNameMacMapMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPbtLocalBridgeNameMacMapMacAddr.setStatus(_A)
_WwpLeosPbtLocalBridgeNameMacMapUseCount_Type=Counter32
_WwpLeosPbtLocalBridgeNameMacMapUseCount_Object=MibTableColumn
wwpLeosPbtLocalBridgeNameMacMapUseCount=_WwpLeosPbtLocalBridgeNameMacMapUseCount_Object((1,3,6,1,4,1,6141,2,60,38,1,1,6,1,4),_WwpLeosPbtLocalBridgeNameMacMapUseCount_Type())
wwpLeosPbtLocalBridgeNameMacMapUseCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPbtLocalBridgeNameMacMapUseCount.setStatus(_A)
_WwpLeosPbtLocalBridgeNameMacMapRowStatus_Type=RowStatus
_WwpLeosPbtLocalBridgeNameMacMapRowStatus_Object=MibTableColumn
wwpLeosPbtLocalBridgeNameMacMapRowStatus=_WwpLeosPbtLocalBridgeNameMacMapRowStatus_Object((1,3,6,1,4,1,6141,2,60,38,1,1,6,1,5),_WwpLeosPbtLocalBridgeNameMacMapRowStatus_Type())
wwpLeosPbtLocalBridgeNameMacMapRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosPbtLocalBridgeNameMacMapRowStatus.setStatus(_A)
_WwpLeosTcePbt_ObjectIdentity=ObjectIdentity
wwpLeosTcePbt=_WwpLeosTcePbt_ObjectIdentity((1,3,6,1,4,1,6141,2,60,38,1,1,10))
_WwpLeosTcePbtServiceTable_Object=MibTable
wwpLeosTcePbtServiceTable=_WwpLeosTcePbtServiceTable_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1))
if mibBuilder.loadTexts:wwpLeosTcePbtServiceTable.setStatus(_A)
_WwpLeosTcePbtServiceEntry_Object=MibTableRow
wwpLeosTcePbtServiceEntry=_WwpLeosTcePbtServiceEntry_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1))
wwpLeosTcePbtServiceEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:wwpLeosTcePbtServiceEntry.setStatus(_A)
_WwpLeosTcePbtServiceIndex_Type=Unsigned32
_WwpLeosTcePbtServiceIndex_Object=MibTableColumn
wwpLeosTcePbtServiceIndex=_WwpLeosTcePbtServiceIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,1),_WwpLeosTcePbtServiceIndex_Type())
wwpLeosTcePbtServiceIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceIndex.setStatus(_A)
class _WwpLeosTcePbtServiceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosTcePbtServiceName_Type.__name__=_F
_WwpLeosTcePbtServiceName_Object=MibTableColumn
wwpLeosTcePbtServiceName=_WwpLeosTcePbtServiceName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,2),_WwpLeosTcePbtServiceName_Type())
wwpLeosTcePbtServiceName.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceName.setStatus(_A)
class _WwpLeosTcePbtServiceOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_WwpLeosTcePbtServiceOperStatus_Type.__name__=_E
_WwpLeosTcePbtServiceOperStatus_Object=MibTableColumn
wwpLeosTcePbtServiceOperStatus=_WwpLeosTcePbtServiceOperStatus_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,3),_WwpLeosTcePbtServiceOperStatus_Type())
wwpLeosTcePbtServiceOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceOperStatus.setStatus(_A)
class _WwpLeosTcePbtServiceFloodContProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosTcePbtServiceFloodContProfileId_Type.__name__=_E
_WwpLeosTcePbtServiceFloodContProfileId_Object=MibTableColumn
wwpLeosTcePbtServiceFloodContProfileId=_WwpLeosTcePbtServiceFloodContProfileId_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,4),_WwpLeosTcePbtServiceFloodContProfileId_Type())
wwpLeosTcePbtServiceFloodContProfileId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceFloodContProfileId.setStatus(_A)
class _WwpLeosTcePbtServiceFloodContProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WwpLeosTcePbtServiceFloodContProfileName_Type.__name__=_F
_WwpLeosTcePbtServiceFloodContProfileName_Object=MibTableColumn
wwpLeosTcePbtServiceFloodContProfileName=_WwpLeosTcePbtServiceFloodContProfileName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,5),_WwpLeosTcePbtServiceFloodContProfileName_Type())
wwpLeosTcePbtServiceFloodContProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceFloodContProfileName.setStatus(_A)
_WwpLeosTcePbtServiceVsIndex_Type=Unsigned32
_WwpLeosTcePbtServiceVsIndex_Object=MibTableColumn
wwpLeosTcePbtServiceVsIndex=_WwpLeosTcePbtServiceVsIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,6),_WwpLeosTcePbtServiceVsIndex_Type())
wwpLeosTcePbtServiceVsIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceVsIndex.setStatus(_A)
class _WwpLeosTcePbtServiceVsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WwpLeosTcePbtServiceVsName_Type.__name__=_F
_WwpLeosTcePbtServiceVsName_Object=MibTableColumn
wwpLeosTcePbtServiceVsName=_WwpLeosTcePbtServiceVsName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,7),_WwpLeosTcePbtServiceVsName_Type())
wwpLeosTcePbtServiceVsName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceVsName.setStatus(_A)
_WwpLeosTcePbtServiceTnlGroupIndex_Type=Unsigned32
_WwpLeosTcePbtServiceTnlGroupIndex_Object=MibTableColumn
wwpLeosTcePbtServiceTnlGroupIndex=_WwpLeosTcePbtServiceTnlGroupIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,8),_WwpLeosTcePbtServiceTnlGroupIndex_Type())
wwpLeosTcePbtServiceTnlGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceTnlGroupIndex.setStatus(_A)
class _WwpLeosTcePbtServiceTnlGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosTcePbtServiceTnlGroupName_Type.__name__=_F
_WwpLeosTcePbtServiceTnlGroupName_Object=MibTableColumn
wwpLeosTcePbtServiceTnlGroupName=_WwpLeosTcePbtServiceTnlGroupName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,9),_WwpLeosTcePbtServiceTnlGroupName_Type())
wwpLeosTcePbtServiceTnlGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceTnlGroupName.setStatus(_A)
_WwpLeosTcePbtServiceIngressIsId_Type=Unsigned32
_WwpLeosTcePbtServiceIngressIsId_Object=MibTableColumn
wwpLeosTcePbtServiceIngressIsId=_WwpLeosTcePbtServiceIngressIsId_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,10),_WwpLeosTcePbtServiceIngressIsId_Type())
wwpLeosTcePbtServiceIngressIsId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceIngressIsId.setStatus(_A)
_WwpLeosTcePbtServiceEgressIsId_Type=Unsigned32
_WwpLeosTcePbtServiceEgressIsId_Object=MibTableColumn
wwpLeosTcePbtServiceEgressIsId=_WwpLeosTcePbtServiceEgressIsId_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,11),_WwpLeosTcePbtServiceEgressIsId_Type())
wwpLeosTcePbtServiceEgressIsId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceEgressIsId.setStatus(_A)
class _WwpLeosTcePbtServiceFixedEgressPcp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_WwpLeosTcePbtServiceFixedEgressPcp_Type.__name__=_E
_WwpLeosTcePbtServiceFixedEgressPcp_Object=MibTableColumn
wwpLeosTcePbtServiceFixedEgressPcp=_WwpLeosTcePbtServiceFixedEgressPcp_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,12),_WwpLeosTcePbtServiceFixedEgressPcp_Type())
wwpLeosTcePbtServiceFixedEgressPcp.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceFixedEgressPcp.setStatus(_A)
class _WwpLeosTcePbtServiceFrameCosPolicy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_h,2)))
_WwpLeosTcePbtServiceFrameCosPolicy_Type.__name__=_E
_WwpLeosTcePbtServiceFrameCosPolicy_Object=MibTableColumn
wwpLeosTcePbtServiceFrameCosPolicy=_WwpLeosTcePbtServiceFrameCosPolicy_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,13),_WwpLeosTcePbtServiceFrameCosPolicy_Type())
wwpLeosTcePbtServiceFrameCosPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceFrameCosPolicy.setStatus(_A)
class _WwpLeosTcePbtServiceFrameCosMapIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosTcePbtServiceFrameCosMapIndex_Type.__name__=_E
_WwpLeosTcePbtServiceFrameCosMapIndex_Object=MibTableColumn
wwpLeosTcePbtServiceFrameCosMapIndex=_WwpLeosTcePbtServiceFrameCosMapIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,14),_WwpLeosTcePbtServiceFrameCosMapIndex_Type())
wwpLeosTcePbtServiceFrameCosMapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceFrameCosMapIndex.setStatus(_A)
class _WwpLeosTcePbtServiceFrameCosMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WwpLeosTcePbtServiceFrameCosMapName_Type.__name__=_F
_WwpLeosTcePbtServiceFrameCosMapName_Object=MibTableColumn
wwpLeosTcePbtServiceFrameCosMapName=_WwpLeosTcePbtServiceFrameCosMapName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,15),_WwpLeosTcePbtServiceFrameCosMapName_Type())
wwpLeosTcePbtServiceFrameCosMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceFrameCosMapName.setStatus(_A)
class _WwpLeosTcePbtServiceResolvedCosPolicy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),(_R,2),(_j,3)))
_WwpLeosTcePbtServiceResolvedCosPolicy_Type.__name__=_E
_WwpLeosTcePbtServiceResolvedCosPolicy_Object=MibTableColumn
wwpLeosTcePbtServiceResolvedCosPolicy=_WwpLeosTcePbtServiceResolvedCosPolicy_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,16),_WwpLeosTcePbtServiceResolvedCosPolicy_Type())
wwpLeosTcePbtServiceResolvedCosPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceResolvedCosPolicy.setStatus(_A)
class _WwpLeosTcePbtServiceResolvedCosProfileIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosTcePbtServiceResolvedCosProfileIndex_Type.__name__=_E
_WwpLeosTcePbtServiceResolvedCosProfileIndex_Object=MibTableColumn
wwpLeosTcePbtServiceResolvedCosProfileIndex=_WwpLeosTcePbtServiceResolvedCosProfileIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,17),_WwpLeosTcePbtServiceResolvedCosProfileIndex_Type())
wwpLeosTcePbtServiceResolvedCosProfileIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceResolvedCosProfileIndex.setStatus(_A)
class _WwpLeosTcePbtServiceResolvedCosProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WwpLeosTcePbtServiceResolvedCosProfileName_Type.__name__=_F
_WwpLeosTcePbtServiceResolvedCosProfileName_Object=MibTableColumn
wwpLeosTcePbtServiceResolvedCosProfileName=_WwpLeosTcePbtServiceResolvedCosProfileName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,18),_WwpLeosTcePbtServiceResolvedCosProfileName_Type())
wwpLeosTcePbtServiceResolvedCosProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceResolvedCosProfileName.setStatus(_A)
class _WwpLeosTcePbtServiceIngressMeterProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosTcePbtServiceIngressMeterProfileId_Type.__name__=_E
_WwpLeosTcePbtServiceIngressMeterProfileId_Object=MibTableColumn
wwpLeosTcePbtServiceIngressMeterProfileId=_WwpLeosTcePbtServiceIngressMeterProfileId_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,19),_WwpLeosTcePbtServiceIngressMeterProfileId_Type())
wwpLeosTcePbtServiceIngressMeterProfileId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceIngressMeterProfileId.setStatus(_A)
_WwpLeosTcePbtServiceIngressMeterProfileName_Type=DisplayString
_WwpLeosTcePbtServiceIngressMeterProfileName_Object=MibTableColumn
wwpLeosTcePbtServiceIngressMeterProfileName=_WwpLeosTcePbtServiceIngressMeterProfileName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,20),_WwpLeosTcePbtServiceIngressMeterProfileName_Type())
wwpLeosTcePbtServiceIngressMeterProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceIngressMeterProfileName.setStatus(_A)
class _WwpLeosTcePbtServiceIngressMeterPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonhierarchical',1),('hierarchical',2)))
_WwpLeosTcePbtServiceIngressMeterPolicy_Type.__name__=_E
_WwpLeosTcePbtServiceIngressMeterPolicy_Object=MibTableColumn
wwpLeosTcePbtServiceIngressMeterPolicy=_WwpLeosTcePbtServiceIngressMeterPolicy_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,21),_WwpLeosTcePbtServiceIngressMeterPolicy_Type())
wwpLeosTcePbtServiceIngressMeterPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceIngressMeterPolicy.setStatus(_A)
_WwpLeosTcePbtServiceRowStatus_Type=RowStatus
_WwpLeosTcePbtServiceRowStatus_Object=MibTableColumn
wwpLeosTcePbtServiceRowStatus=_WwpLeosTcePbtServiceRowStatus_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,1,1,64),_WwpLeosTcePbtServiceRowStatus_Type())
wwpLeosTcePbtServiceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceRowStatus.setStatus(_A)
_WwpLeosTcePbtTnlGroupTable_Object=MibTable
wwpLeosTcePbtTnlGroupTable=_WwpLeosTcePbtTnlGroupTable_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,5))
if mibBuilder.loadTexts:wwpLeosTcePbtTnlGroupTable.setStatus(_A)
_WwpLeosTcePbtTnlGroupEntry_Object=MibTableRow
wwpLeosTcePbtTnlGroupEntry=_WwpLeosTcePbtTnlGroupEntry_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,5,1))
wwpLeosTcePbtTnlGroupEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:wwpLeosTcePbtTnlGroupEntry.setStatus(_A)
_WwpLeosTcePbtTnlGroupIndex_Type=Unsigned32
_WwpLeosTcePbtTnlGroupIndex_Object=MibTableColumn
wwpLeosTcePbtTnlGroupIndex=_WwpLeosTcePbtTnlGroupIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,5,1,1),_WwpLeosTcePbtTnlGroupIndex_Type())
wwpLeosTcePbtTnlGroupIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:wwpLeosTcePbtTnlGroupIndex.setStatus(_A)
class _WwpLeosTcePbtTnlGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosTcePbtTnlGroupName_Type.__name__=_F
_WwpLeosTcePbtTnlGroupName_Object=MibTableColumn
wwpLeosTcePbtTnlGroupName=_WwpLeosTcePbtTnlGroupName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,5,1,2),_WwpLeosTcePbtTnlGroupName_Type())
wwpLeosTcePbtTnlGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtTnlGroupName.setStatus(_A)
class _WwpLeosTcePbtTnlGroupSyncEnabled_Type(TruthValue):defaultValue=2
_WwpLeosTcePbtTnlGroupSyncEnabled_Type.__name__=_O
_WwpLeosTcePbtTnlGroupSyncEnabled_Object=MibTableColumn
wwpLeosTcePbtTnlGroupSyncEnabled=_WwpLeosTcePbtTnlGroupSyncEnabled_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,5,1,3),_WwpLeosTcePbtTnlGroupSyncEnabled_Type())
wwpLeosTcePbtTnlGroupSyncEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtTnlGroupSyncEnabled.setStatus(_A)
class _WwpLeosTcePbtTnlGroupOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_WwpLeosTcePbtTnlGroupOperStatus_Type.__name__=_E
_WwpLeosTcePbtTnlGroupOperStatus_Object=MibTableColumn
wwpLeosTcePbtTnlGroupOperStatus=_WwpLeosTcePbtTnlGroupOperStatus_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,5,1,4),_WwpLeosTcePbtTnlGroupOperStatus_Type())
wwpLeosTcePbtTnlGroupOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtTnlGroupOperStatus.setStatus(_A)
_WwpLeosTcePbtTnlGroupUseCount_Type=Unsigned32
_WwpLeosTcePbtTnlGroupUseCount_Object=MibTableColumn
wwpLeosTcePbtTnlGroupUseCount=_WwpLeosTcePbtTnlGroupUseCount_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,5,1,5),_WwpLeosTcePbtTnlGroupUseCount_Type())
wwpLeosTcePbtTnlGroupUseCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtTnlGroupUseCount.setStatus(_A)
_WwpLeosTcePbtTnlGroupActivePair_Type=Unsigned32
_WwpLeosTcePbtTnlGroupActivePair_Object=MibTableColumn
wwpLeosTcePbtTnlGroupActivePair=_WwpLeosTcePbtTnlGroupActivePair_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,5,1,6),_WwpLeosTcePbtTnlGroupActivePair_Type())
wwpLeosTcePbtTnlGroupActivePair.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtTnlGroupActivePair.setStatus(_A)
_WwpLeosTcePbtTnlGroupReverting_Type=TruthValue
_WwpLeosTcePbtTnlGroupReverting_Object=MibTableColumn
wwpLeosTcePbtTnlGroupReverting=_WwpLeosTcePbtTnlGroupReverting_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,5,1,7),_WwpLeosTcePbtTnlGroupReverting_Type())
wwpLeosTcePbtTnlGroupReverting.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtTnlGroupReverting.setStatus(_A)
_WwpLeosTcePbtTnlGroupRowStatus_Type=RowStatus
_WwpLeosTcePbtTnlGroupRowStatus_Object=MibTableColumn
wwpLeosTcePbtTnlGroupRowStatus=_WwpLeosTcePbtTnlGroupRowStatus_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,5,1,64),_WwpLeosTcePbtTnlGroupRowStatus_Type())
wwpLeosTcePbtTnlGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtTnlGroupRowStatus.setStatus(_A)
_WwpLeosTcePbtEncapTnlTable_Object=MibTable
wwpLeosTcePbtEncapTnlTable=_WwpLeosTcePbtEncapTnlTable_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6))
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlTable.setStatus(_A)
_WwpLeosTcePbtEncapTnlEntry_Object=MibTableRow
wwpLeosTcePbtEncapTnlEntry=_WwpLeosTcePbtEncapTnlEntry_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1))
wwpLeosTcePbtEncapTnlEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlEntry.setStatus(_A)
_WwpLeosTcePbtEncapTnlIndex_Type=Unsigned32
_WwpLeosTcePbtEncapTnlIndex_Object=MibTableColumn
wwpLeosTcePbtEncapTnlIndex=_WwpLeosTcePbtEncapTnlIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,1),_WwpLeosTcePbtEncapTnlIndex_Type())
wwpLeosTcePbtEncapTnlIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlIndex.setStatus(_A)
class _WwpLeosTcePbtEncapTnlName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosTcePbtEncapTnlName_Type.__name__=_F
_WwpLeosTcePbtEncapTnlName_Object=MibTableColumn
wwpLeosTcePbtEncapTnlName=_WwpLeosTcePbtEncapTnlName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,2),_WwpLeosTcePbtEncapTnlName_Type())
wwpLeosTcePbtEncapTnlName.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlName.setStatus(_A)
_WwpLeosTcePbtEncapTnlRemoteBridgeIndex_Type=Unsigned32
_WwpLeosTcePbtEncapTnlRemoteBridgeIndex_Object=MibTableColumn
wwpLeosTcePbtEncapTnlRemoteBridgeIndex=_WwpLeosTcePbtEncapTnlRemoteBridgeIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,3),_WwpLeosTcePbtEncapTnlRemoteBridgeIndex_Type())
wwpLeosTcePbtEncapTnlRemoteBridgeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlRemoteBridgeIndex.setStatus(_A)
class _WwpLeosTcePbtEncapTnlRemoteBridgeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosTcePbtEncapTnlRemoteBridgeName_Type.__name__=_F
_WwpLeosTcePbtEncapTnlRemoteBridgeName_Object=MibTableColumn
wwpLeosTcePbtEncapTnlRemoteBridgeName=_WwpLeosTcePbtEncapTnlRemoteBridgeName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,4),_WwpLeosTcePbtEncapTnlRemoteBridgeName_Type())
wwpLeosTcePbtEncapTnlRemoteBridgeName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlRemoteBridgeName.setStatus(_A)
_WwpLeosTcePbtEncapTnlGroupIndex_Type=Unsigned32
_WwpLeosTcePbtEncapTnlGroupIndex_Object=MibTableColumn
wwpLeosTcePbtEncapTnlGroupIndex=_WwpLeosTcePbtEncapTnlGroupIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,5),_WwpLeosTcePbtEncapTnlGroupIndex_Type())
wwpLeosTcePbtEncapTnlGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlGroupIndex.setStatus(_A)
class _WwpLeosTcePbtEncapTnlGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosTcePbtEncapTnlGroupName_Type.__name__=_F
_WwpLeosTcePbtEncapTnlGroupName_Object=MibTableColumn
wwpLeosTcePbtEncapTnlGroupName=_WwpLeosTcePbtEncapTnlGroupName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,6),_WwpLeosTcePbtEncapTnlGroupName_Type())
wwpLeosTcePbtEncapTnlGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlGroupName.setStatus(_A)
_WwpLeosTcePbtEncapTnlBvId_Type=Unsigned32
_WwpLeosTcePbtEncapTnlBvId_Object=MibTableColumn
wwpLeosTcePbtEncapTnlBvId=_WwpLeosTcePbtEncapTnlBvId_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,7),_WwpLeosTcePbtEncapTnlBvId_Type())
wwpLeosTcePbtEncapTnlBvId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlBvId.setStatus(_A)
_WwpLeosTcePbtEncapTnlPgId_Type=Unsigned32
_WwpLeosTcePbtEncapTnlPgId_Object=MibTableColumn
wwpLeosTcePbtEncapTnlPgId=_WwpLeosTcePbtEncapTnlPgId_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,8),_WwpLeosTcePbtEncapTnlPgId_Type())
wwpLeosTcePbtEncapTnlPgId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlPgId.setStatus(_A)
class _WwpLeosTcePbtEncapTnlPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosTcePbtEncapTnlPortName_Type.__name__=_F
_WwpLeosTcePbtEncapTnlPortName_Object=MibTableColumn
wwpLeosTcePbtEncapTnlPortName=_WwpLeosTcePbtEncapTnlPortName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,9),_WwpLeosTcePbtEncapTnlPortName_Type())
wwpLeosTcePbtEncapTnlPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlPortName.setStatus(_A)
_WwpLeosTcePbtEncapTnlFaults_Type=Unsigned32
_WwpLeosTcePbtEncapTnlFaults_Object=MibTableColumn
wwpLeosTcePbtEncapTnlFaults=_WwpLeosTcePbtEncapTnlFaults_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,10),_WwpLeosTcePbtEncapTnlFaults_Type())
wwpLeosTcePbtEncapTnlFaults.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlFaults.setStatus(_A)
class _WwpLeosTcePbtEncapTnlAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTcePbtEncapTnlAdminState_Type.__name__=_E
_WwpLeosTcePbtEncapTnlAdminState_Object=MibTableColumn
wwpLeosTcePbtEncapTnlAdminState=_WwpLeosTcePbtEncapTnlAdminState_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,11),_WwpLeosTcePbtEncapTnlAdminState_Type())
wwpLeosTcePbtEncapTnlAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlAdminState.setStatus(_A)
class _WwpLeosTcePbtEncapTnlOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTcePbtEncapTnlOperState_Type.__name__=_E
_WwpLeosTcePbtEncapTnlOperState_Object=MibTableColumn
wwpLeosTcePbtEncapTnlOperState=_WwpLeosTcePbtEncapTnlOperState_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,12),_WwpLeosTcePbtEncapTnlOperState_Type())
wwpLeosTcePbtEncapTnlOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlOperState.setStatus(_A)
class _WwpLeosTcePbtEncapTnlFwdState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),(_l,2)))
_WwpLeosTcePbtEncapTnlFwdState_Type.__name__=_E
_WwpLeosTcePbtEncapTnlFwdState_Object=MibTableColumn
wwpLeosTcePbtEncapTnlFwdState=_WwpLeosTcePbtEncapTnlFwdState_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,13),_WwpLeosTcePbtEncapTnlFwdState_Type())
wwpLeosTcePbtEncapTnlFwdState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlFwdState.setStatus(_A)
_WwpLeosTcePbtEncapTnlPaired_Type=TruthValue
_WwpLeosTcePbtEncapTnlPaired_Object=MibTableColumn
wwpLeosTcePbtEncapTnlPaired=_WwpLeosTcePbtEncapTnlPaired_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,14),_WwpLeosTcePbtEncapTnlPaired_Type())
wwpLeosTcePbtEncapTnlPaired.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlPaired.setStatus(_A)
class _WwpLeosTcePbtEncapTnlPairIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosTcePbtEncapTnlPairIndex_Type.__name__=_E
_WwpLeosTcePbtEncapTnlPairIndex_Object=MibTableColumn
wwpLeosTcePbtEncapTnlPairIndex=_WwpLeosTcePbtEncapTnlPairIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,15),_WwpLeosTcePbtEncapTnlPairIndex_Type())
wwpLeosTcePbtEncapTnlPairIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlPairIndex.setStatus(_A)
class _WwpLeosTcePbtEncapTnlPairOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTcePbtEncapTnlPairOperState_Type.__name__=_E
_WwpLeosTcePbtEncapTnlPairOperState_Object=MibTableColumn
wwpLeosTcePbtEncapTnlPairOperState=_WwpLeosTcePbtEncapTnlPairOperState_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,16),_WwpLeosTcePbtEncapTnlPairOperState_Type())
wwpLeosTcePbtEncapTnlPairOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlPairOperState.setStatus(_A)
class _WwpLeosTcePbtEncapTnlFrameCosPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_h,2)))
_WwpLeosTcePbtEncapTnlFrameCosPolicy_Type.__name__=_E
_WwpLeosTcePbtEncapTnlFrameCosPolicy_Object=MibTableColumn
wwpLeosTcePbtEncapTnlFrameCosPolicy=_WwpLeosTcePbtEncapTnlFrameCosPolicy_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,17),_WwpLeosTcePbtEncapTnlFrameCosPolicy_Type())
wwpLeosTcePbtEncapTnlFrameCosPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlFrameCosPolicy.setStatus(_A)
_WwpLeosTcePbtEncapTnlFrameCosMapIndex_Type=Unsigned32
_WwpLeosTcePbtEncapTnlFrameCosMapIndex_Object=MibTableColumn
wwpLeosTcePbtEncapTnlFrameCosMapIndex=_WwpLeosTcePbtEncapTnlFrameCosMapIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,18),_WwpLeosTcePbtEncapTnlFrameCosMapIndex_Type())
wwpLeosTcePbtEncapTnlFrameCosMapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlFrameCosMapIndex.setStatus(_A)
class _WwpLeosTcePbtEncapTnlFrameCosMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WwpLeosTcePbtEncapTnlFrameCosMapName_Type.__name__=_F
_WwpLeosTcePbtEncapTnlFrameCosMapName_Object=MibTableColumn
wwpLeosTcePbtEncapTnlFrameCosMapName=_WwpLeosTcePbtEncapTnlFrameCosMapName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,19),_WwpLeosTcePbtEncapTnlFrameCosMapName_Type())
wwpLeosTcePbtEncapTnlFrameCosMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlFrameCosMapName.setStatus(_A)
class _WwpLeosTcePbtEncapTnlFixedPcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosTcePbtEncapTnlFixedPcp_Type.__name__=_E
_WwpLeosTcePbtEncapTnlFixedPcp_Object=MibTableColumn
wwpLeosTcePbtEncapTnlFixedPcp=_WwpLeosTcePbtEncapTnlFixedPcp_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,20),_WwpLeosTcePbtEncapTnlFixedPcp_Type())
wwpLeosTcePbtEncapTnlFixedPcp.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlFixedPcp.setStatus(_A)
_WwpLeosTcePbtEncapTnlCfmConfigured_Type=TruthValue
_WwpLeosTcePbtEncapTnlCfmConfigured_Object=MibTableColumn
wwpLeosTcePbtEncapTnlCfmConfigured=_WwpLeosTcePbtEncapTnlCfmConfigured_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,21),_WwpLeosTcePbtEncapTnlCfmConfigured_Type())
wwpLeosTcePbtEncapTnlCfmConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlCfmConfigured.setStatus(_A)
_WwpLeosTcePbtEncapTnlPairedDecapIndex_Type=Unsigned32
_WwpLeosTcePbtEncapTnlPairedDecapIndex_Object=MibTableColumn
wwpLeosTcePbtEncapTnlPairedDecapIndex=_WwpLeosTcePbtEncapTnlPairedDecapIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,22),_WwpLeosTcePbtEncapTnlPairedDecapIndex_Type())
wwpLeosTcePbtEncapTnlPairedDecapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlPairedDecapIndex.setStatus(_A)
class _WwpLeosTcePbtEncapTnlPairedDecapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WwpLeosTcePbtEncapTnlPairedDecapName_Type.__name__=_F
_WwpLeosTcePbtEncapTnlPairedDecapName_Object=MibTableColumn
wwpLeosTcePbtEncapTnlPairedDecapName=_WwpLeosTcePbtEncapTnlPairedDecapName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,23),_WwpLeosTcePbtEncapTnlPairedDecapName_Type())
wwpLeosTcePbtEncapTnlPairedDecapName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlPairedDecapName.setStatus(_A)
_WwpLeosTcePbtEncapTnlWeight_Type=Unsigned32
_WwpLeosTcePbtEncapTnlWeight_Object=MibTableColumn
wwpLeosTcePbtEncapTnlWeight=_WwpLeosTcePbtEncapTnlWeight_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,24),_WwpLeosTcePbtEncapTnlWeight_Type())
wwpLeosTcePbtEncapTnlWeight.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlWeight.setStatus(_A)
_WwpLeosTcePbtEncapTnlStatsEnabled_Type=TruthValue
_WwpLeosTcePbtEncapTnlStatsEnabled_Object=MibTableColumn
wwpLeosTcePbtEncapTnlStatsEnabled=_WwpLeosTcePbtEncapTnlStatsEnabled_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,25),_WwpLeosTcePbtEncapTnlStatsEnabled_Type())
wwpLeosTcePbtEncapTnlStatsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlStatsEnabled.setStatus(_A)
_WwpLeosTcePbtEncapTnlLocalBridgeIndex_Type=Unsigned32
_WwpLeosTcePbtEncapTnlLocalBridgeIndex_Object=MibTableColumn
wwpLeosTcePbtEncapTnlLocalBridgeIndex=_WwpLeosTcePbtEncapTnlLocalBridgeIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,26),_WwpLeosTcePbtEncapTnlLocalBridgeIndex_Type())
wwpLeosTcePbtEncapTnlLocalBridgeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlLocalBridgeIndex.setStatus(_A)
_WwpLeosTcePbtEncapTnlLocalBridgeName_Type=DisplayString
_WwpLeosTcePbtEncapTnlLocalBridgeName_Object=MibTableColumn
wwpLeosTcePbtEncapTnlLocalBridgeName=_WwpLeosTcePbtEncapTnlLocalBridgeName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,27),_WwpLeosTcePbtEncapTnlLocalBridgeName_Type())
wwpLeosTcePbtEncapTnlLocalBridgeName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlLocalBridgeName.setStatus(_A)
_WwpLeosTcePbtEncapTnlReversionToPairIndex_Type=Unsigned32
_WwpLeosTcePbtEncapTnlReversionToPairIndex_Object=MibTableColumn
wwpLeosTcePbtEncapTnlReversionToPairIndex=_WwpLeosTcePbtEncapTnlReversionToPairIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,28),_WwpLeosTcePbtEncapTnlReversionToPairIndex_Type())
wwpLeosTcePbtEncapTnlReversionToPairIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlReversionToPairIndex.setStatus(_A)
_WwpLeosTcePbtEncapTnlReversionFromPairIndex_Type=Unsigned32
_WwpLeosTcePbtEncapTnlReversionFromPairIndex_Object=MibTableColumn
wwpLeosTcePbtEncapTnlReversionFromPairIndex=_WwpLeosTcePbtEncapTnlReversionFromPairIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,29),_WwpLeosTcePbtEncapTnlReversionFromPairIndex_Type())
wwpLeosTcePbtEncapTnlReversionFromPairIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlReversionFromPairIndex.setStatus(_A)
_WwpLeosTcePbtEncapTnlRowStatus_Type=RowStatus
_WwpLeosTcePbtEncapTnlRowStatus_Object=MibTableColumn
wwpLeosTcePbtEncapTnlRowStatus=_WwpLeosTcePbtEncapTnlRowStatus_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,6,1,64),_WwpLeosTcePbtEncapTnlRowStatus_Type())
wwpLeosTcePbtEncapTnlRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtEncapTnlRowStatus.setStatus(_A)
_WwpLeosTcePbtDecapTnlTable_Object=MibTable
wwpLeosTcePbtDecapTnlTable=_WwpLeosTcePbtDecapTnlTable_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7))
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlTable.setStatus(_A)
_WwpLeosTcePbtDecapTnlEntry_Object=MibTableRow
wwpLeosTcePbtDecapTnlEntry=_WwpLeosTcePbtDecapTnlEntry_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1))
wwpLeosTcePbtDecapTnlEntry.setIndexNames((0,_B,_m))
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlEntry.setStatus(_A)
_WwpLeosTcePbtDecapTnlIndex_Type=Unsigned32
_WwpLeosTcePbtDecapTnlIndex_Object=MibTableColumn
wwpLeosTcePbtDecapTnlIndex=_WwpLeosTcePbtDecapTnlIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,1),_WwpLeosTcePbtDecapTnlIndex_Type())
wwpLeosTcePbtDecapTnlIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlIndex.setStatus(_A)
class _WwpLeosTcePbtDecapTnlName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WwpLeosTcePbtDecapTnlName_Type.__name__=_F
_WwpLeosTcePbtDecapTnlName_Object=MibTableColumn
wwpLeosTcePbtDecapTnlName=_WwpLeosTcePbtDecapTnlName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,2),_WwpLeosTcePbtDecapTnlName_Type())
wwpLeosTcePbtDecapTnlName.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlName.setStatus(_A)
_WwpLeosTcePbtDecapTnlRemoteBridgeIndex_Type=Unsigned32
_WwpLeosTcePbtDecapTnlRemoteBridgeIndex_Object=MibTableColumn
wwpLeosTcePbtDecapTnlRemoteBridgeIndex=_WwpLeosTcePbtDecapTnlRemoteBridgeIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,3),_WwpLeosTcePbtDecapTnlRemoteBridgeIndex_Type())
wwpLeosTcePbtDecapTnlRemoteBridgeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlRemoteBridgeIndex.setStatus(_A)
class _WwpLeosTcePbtDecapTnlRemoteBridgeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WwpLeosTcePbtDecapTnlRemoteBridgeName_Type.__name__=_F
_WwpLeosTcePbtDecapTnlRemoteBridgeName_Object=MibTableColumn
wwpLeosTcePbtDecapTnlRemoteBridgeName=_WwpLeosTcePbtDecapTnlRemoteBridgeName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,4),_WwpLeosTcePbtDecapTnlRemoteBridgeName_Type())
wwpLeosTcePbtDecapTnlRemoteBridgeName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlRemoteBridgeName.setStatus(_A)
_WwpLeosTcePbtDecapTnlGroupIndex_Type=Unsigned32
_WwpLeosTcePbtDecapTnlGroupIndex_Object=MibTableColumn
wwpLeosTcePbtDecapTnlGroupIndex=_WwpLeosTcePbtDecapTnlGroupIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,5),_WwpLeosTcePbtDecapTnlGroupIndex_Type())
wwpLeosTcePbtDecapTnlGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlGroupIndex.setStatus(_A)
class _WwpLeosTcePbtDecapTnlGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosTcePbtDecapTnlGroupName_Type.__name__=_F
_WwpLeosTcePbtDecapTnlGroupName_Object=MibTableColumn
wwpLeosTcePbtDecapTnlGroupName=_WwpLeosTcePbtDecapTnlGroupName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,6),_WwpLeosTcePbtDecapTnlGroupName_Type())
wwpLeosTcePbtDecapTnlGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlGroupName.setStatus(_A)
_WwpLeosTcePbtDecapTnlBvId_Type=Unsigned32
_WwpLeosTcePbtDecapTnlBvId_Object=MibTableColumn
wwpLeosTcePbtDecapTnlBvId=_WwpLeosTcePbtDecapTnlBvId_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,7),_WwpLeosTcePbtDecapTnlBvId_Type())
wwpLeosTcePbtDecapTnlBvId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlBvId.setStatus(_A)
_WwpLeosTcePbtDecapTnlPgId_Type=Unsigned32
_WwpLeosTcePbtDecapTnlPgId_Object=MibTableColumn
wwpLeosTcePbtDecapTnlPgId=_WwpLeosTcePbtDecapTnlPgId_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,8),_WwpLeosTcePbtDecapTnlPgId_Type())
wwpLeosTcePbtDecapTnlPgId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlPgId.setStatus(_A)
class _WwpLeosTcePbtDecapTnlPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WwpLeosTcePbtDecapTnlPortName_Type.__name__=_F
_WwpLeosTcePbtDecapTnlPortName_Object=MibTableColumn
wwpLeosTcePbtDecapTnlPortName=_WwpLeosTcePbtDecapTnlPortName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,9),_WwpLeosTcePbtDecapTnlPortName_Type())
wwpLeosTcePbtDecapTnlPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlPortName.setStatus(_A)
_WwpLeosTcePbtDecapTnlFaults_Type=Unsigned32
_WwpLeosTcePbtDecapTnlFaults_Object=MibTableColumn
wwpLeosTcePbtDecapTnlFaults=_WwpLeosTcePbtDecapTnlFaults_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,10),_WwpLeosTcePbtDecapTnlFaults_Type())
wwpLeosTcePbtDecapTnlFaults.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlFaults.setStatus(_A)
class _WwpLeosTcePbtDecapTnlOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTcePbtDecapTnlOperState_Type.__name__=_E
_WwpLeosTcePbtDecapTnlOperState_Object=MibTableColumn
wwpLeosTcePbtDecapTnlOperState=_WwpLeosTcePbtDecapTnlOperState_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,11),_WwpLeosTcePbtDecapTnlOperState_Type())
wwpLeosTcePbtDecapTnlOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlOperState.setStatus(_A)
class _WwpLeosTcePbtDecapTnlFwdState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),(_l,2)))
_WwpLeosTcePbtDecapTnlFwdState_Type.__name__=_E
_WwpLeosTcePbtDecapTnlFwdState_Object=MibTableColumn
wwpLeosTcePbtDecapTnlFwdState=_WwpLeosTcePbtDecapTnlFwdState_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,12),_WwpLeosTcePbtDecapTnlFwdState_Type())
wwpLeosTcePbtDecapTnlFwdState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlFwdState.setStatus(_A)
_WwpLeosTcePbtDecapTnlPaired_Type=TruthValue
_WwpLeosTcePbtDecapTnlPaired_Object=MibTableColumn
wwpLeosTcePbtDecapTnlPaired=_WwpLeosTcePbtDecapTnlPaired_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,13),_WwpLeosTcePbtDecapTnlPaired_Type())
wwpLeosTcePbtDecapTnlPaired.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlPaired.setStatus(_A)
class _WwpLeosTcePbtDecapTnlPairIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosTcePbtDecapTnlPairIndex_Type.__name__=_E
_WwpLeosTcePbtDecapTnlPairIndex_Object=MibTableColumn
wwpLeosTcePbtDecapTnlPairIndex=_WwpLeosTcePbtDecapTnlPairIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,14),_WwpLeosTcePbtDecapTnlPairIndex_Type())
wwpLeosTcePbtDecapTnlPairIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlPairIndex.setStatus(_A)
class _WwpLeosTcePbtDecapTnlPairOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTcePbtDecapTnlPairOperState_Type.__name__=_E
_WwpLeosTcePbtDecapTnlPairOperState_Object=MibTableColumn
wwpLeosTcePbtDecapTnlPairOperState=_WwpLeosTcePbtDecapTnlPairOperState_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,15),_WwpLeosTcePbtDecapTnlPairOperState_Type())
wwpLeosTcePbtDecapTnlPairOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlPairOperState.setStatus(_A)
class _WwpLeosTcePbtDecapTnlResolvedCosPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),(_R,2),(_j,3)))
_WwpLeosTcePbtDecapTnlResolvedCosPolicy_Type.__name__=_E
_WwpLeosTcePbtDecapTnlResolvedCosPolicy_Object=MibTableColumn
wwpLeosTcePbtDecapTnlResolvedCosPolicy=_WwpLeosTcePbtDecapTnlResolvedCosPolicy_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,16),_WwpLeosTcePbtDecapTnlResolvedCosPolicy_Type())
wwpLeosTcePbtDecapTnlResolvedCosPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlResolvedCosPolicy.setStatus(_A)
_WwpLeosTcePbtDecapTnlResolvedCosMapIndex_Type=Unsigned32
_WwpLeosTcePbtDecapTnlResolvedCosMapIndex_Object=MibTableColumn
wwpLeosTcePbtDecapTnlResolvedCosMapIndex=_WwpLeosTcePbtDecapTnlResolvedCosMapIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,17),_WwpLeosTcePbtDecapTnlResolvedCosMapIndex_Type())
wwpLeosTcePbtDecapTnlResolvedCosMapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlResolvedCosMapIndex.setStatus(_A)
class _WwpLeosTcePbtDecapTnlResolvedCosMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WwpLeosTcePbtDecapTnlResolvedCosMapName_Type.__name__=_F
_WwpLeosTcePbtDecapTnlResolvedCosMapName_Object=MibTableColumn
wwpLeosTcePbtDecapTnlResolvedCosMapName=_WwpLeosTcePbtDecapTnlResolvedCosMapName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,18),_WwpLeosTcePbtDecapTnlResolvedCosMapName_Type())
wwpLeosTcePbtDecapTnlResolvedCosMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlResolvedCosMapName.setStatus(_A)
_WwpLeosTcePbtDecapTnlCfmConfigured_Type=TruthValue
_WwpLeosTcePbtDecapTnlCfmConfigured_Object=MibTableColumn
wwpLeosTcePbtDecapTnlCfmConfigured=_WwpLeosTcePbtDecapTnlCfmConfigured_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,19),_WwpLeosTcePbtDecapTnlCfmConfigured_Type())
wwpLeosTcePbtDecapTnlCfmConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlCfmConfigured.setStatus(_A)
_WwpLeosTcePbtDecapTnlPairedEncapIndex_Type=Unsigned32
_WwpLeosTcePbtDecapTnlPairedEncapIndex_Object=MibTableColumn
wwpLeosTcePbtDecapTnlPairedEncapIndex=_WwpLeosTcePbtDecapTnlPairedEncapIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,20),_WwpLeosTcePbtDecapTnlPairedEncapIndex_Type())
wwpLeosTcePbtDecapTnlPairedEncapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlPairedEncapIndex.setStatus(_A)
class _WwpLeosTcePbtDecapTnlPairedEncapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WwpLeosTcePbtDecapTnlPairedEncapName_Type.__name__=_F
_WwpLeosTcePbtDecapTnlPairedEncapName_Object=MibTableColumn
wwpLeosTcePbtDecapTnlPairedEncapName=_WwpLeosTcePbtDecapTnlPairedEncapName_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,21),_WwpLeosTcePbtDecapTnlPairedEncapName_Type())
wwpLeosTcePbtDecapTnlPairedEncapName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlPairedEncapName.setStatus(_A)
_WwpLeosTcePbtDecapTnlStatsEnabled_Type=TruthValue
_WwpLeosTcePbtDecapTnlStatsEnabled_Object=MibTableColumn
wwpLeosTcePbtDecapTnlStatsEnabled=_WwpLeosTcePbtDecapTnlStatsEnabled_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,22),_WwpLeosTcePbtDecapTnlStatsEnabled_Type())
wwpLeosTcePbtDecapTnlStatsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlStatsEnabled.setStatus(_A)
_WwpLeosTcePbtDecapTnlRowStatus_Type=RowStatus
_WwpLeosTcePbtDecapTnlRowStatus_Object=MibTableColumn
wwpLeosTcePbtDecapTnlRowStatus=_WwpLeosTcePbtDecapTnlRowStatus_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,7,1,64),_WwpLeosTcePbtDecapTnlRowStatus_Type())
wwpLeosTcePbtDecapTnlRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTcePbtDecapTnlRowStatus.setStatus(_A)
_WwpLeosTcePbtServiceUserFrameL2TransformTable_Object=MibTable
wwpLeosTcePbtServiceUserFrameL2TransformTable=_WwpLeosTcePbtServiceUserFrameL2TransformTable_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,8))
if mibBuilder.loadTexts:wwpLeosTcePbtServiceUserFrameL2TransformTable.setStatus(_A)
_WwpLeosTcePbtServiceUserFrameL2TransformEntry_Object=MibTableRow
wwpLeosTcePbtServiceUserFrameL2TransformEntry=_WwpLeosTcePbtServiceUserFrameL2TransformEntry_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,8,1))
wwpLeosTcePbtServiceUserFrameL2TransformEntry.setIndexNames((0,_B,_a),(0,_B,_n),(0,_B,_o))
if mibBuilder.loadTexts:wwpLeosTcePbtServiceUserFrameL2TransformEntry.setStatus(_A)
class _WwpLeosTcePbtServiceUserFrameL2TransformDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ingress',1),('egress',2)))
_WwpLeosTcePbtServiceUserFrameL2TransformDirection_Type.__name__=_E
_WwpLeosTcePbtServiceUserFrameL2TransformDirection_Object=MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformDirection=_WwpLeosTcePbtServiceUserFrameL2TransformDirection_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,8,1,1),_WwpLeosTcePbtServiceUserFrameL2TransformDirection_Type())
wwpLeosTcePbtServiceUserFrameL2TransformDirection.setMaxAccess(_Q)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceUserFrameL2TransformDirection.setStatus(_A)
class _WwpLeosTcePbtServiceUserFrameL2TransformTagIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WwpLeosTcePbtServiceUserFrameL2TransformTagIndex_Type.__name__=_E
_WwpLeosTcePbtServiceUserFrameL2TransformTagIndex_Object=MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformTagIndex=_WwpLeosTcePbtServiceUserFrameL2TransformTagIndex_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,8,1,2),_WwpLeosTcePbtServiceUserFrameL2TransformTagIndex_Type())
wwpLeosTcePbtServiceUserFrameL2TransformTagIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceUserFrameL2TransformTagIndex.setStatus(_A)
class _WwpLeosTcePbtServiceUserFrameL2TransformTagAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('push',2),('pop',3),('stamp1',4),('stamp2',5)))
_WwpLeosTcePbtServiceUserFrameL2TransformTagAction_Type.__name__=_E
_WwpLeosTcePbtServiceUserFrameL2TransformTagAction_Object=MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformTagAction=_WwpLeosTcePbtServiceUserFrameL2TransformTagAction_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,8,1,3),_WwpLeosTcePbtServiceUserFrameL2TransformTagAction_Type())
wwpLeosTcePbtServiceUserFrameL2TransformTagAction.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceUserFrameL2TransformTagAction.setStatus(_A)
class _WwpLeosTcePbtServiceUserFrameL2TransformTagValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_WwpLeosTcePbtServiceUserFrameL2TransformTagValue_Type.__name__=_E
_WwpLeosTcePbtServiceUserFrameL2TransformTagValue_Object=MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformTagValue=_WwpLeosTcePbtServiceUserFrameL2TransformTagValue_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,8,1,4),_WwpLeosTcePbtServiceUserFrameL2TransformTagValue_Type())
wwpLeosTcePbtServiceUserFrameL2TransformTagValue.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceUserFrameL2TransformTagValue.setStatus(_A)
class _WwpLeosTcePbtServiceUserFrameL2TransformTagEtype_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_WwpLeosTcePbtServiceUserFrameL2TransformTagEtype_Type.__name__=_E
_WwpLeosTcePbtServiceUserFrameL2TransformTagEtype_Object=MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformTagEtype=_WwpLeosTcePbtServiceUserFrameL2TransformTagEtype_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,8,1,5),_WwpLeosTcePbtServiceUserFrameL2TransformTagEtype_Type())
wwpLeosTcePbtServiceUserFrameL2TransformTagEtype.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceUserFrameL2TransformTagEtype.setStatus(_A)
class _WwpLeosTcePbtServiceUserFrameL2TransformTagPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosTcePbtServiceUserFrameL2TransformTagPriority_Type.__name__=_E
_WwpLeosTcePbtServiceUserFrameL2TransformTagPriority_Object=MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformTagPriority=_WwpLeosTcePbtServiceUserFrameL2TransformTagPriority_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,8,1,6),_WwpLeosTcePbtServiceUserFrameL2TransformTagPriority_Type())
wwpLeosTcePbtServiceUserFrameL2TransformTagPriority.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceUserFrameL2TransformTagPriority.setStatus(_A)
class _WwpLeosTcePbtServiceUserFrameL2TransformPriPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('leave',1),('static',2),('mapped',3)))
_WwpLeosTcePbtServiceUserFrameL2TransformPriPolicy_Type.__name__=_E
_WwpLeosTcePbtServiceUserFrameL2TransformPriPolicy_Object=MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformPriPolicy=_WwpLeosTcePbtServiceUserFrameL2TransformPriPolicy_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,8,1,7),_WwpLeosTcePbtServiceUserFrameL2TransformPriPolicy_Type())
wwpLeosTcePbtServiceUserFrameL2TransformPriPolicy.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceUserFrameL2TransformPriPolicy.setStatus(_A)
class _WwpLeosTcePbtServiceUserFrameL2TransformUseTagValue_Type(TruthValue):defaultValue=2
_WwpLeosTcePbtServiceUserFrameL2TransformUseTagValue_Type.__name__=_O
_WwpLeosTcePbtServiceUserFrameL2TransformUseTagValue_Object=MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformUseTagValue=_WwpLeosTcePbtServiceUserFrameL2TransformUseTagValue_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,8,1,8),_WwpLeosTcePbtServiceUserFrameL2TransformUseTagValue_Type())
wwpLeosTcePbtServiceUserFrameL2TransformUseTagValue.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceUserFrameL2TransformUseTagValue.setStatus(_A)
class _WwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype_Type(TruthValue):defaultValue=2
_WwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype_Type.__name__=_O
_WwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype_Object=MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype=_WwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype_Object((1,3,6,1,4,1,6141,2,60,38,1,1,10,8,1,9),_WwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype_Type())
wwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype.setStatus(_A)
_WwpLeosPbtMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosPbtMIBNotificationPrefix=_WwpLeosPbtMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,38,2))
_WwpLeosPbtMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosPbtMIBNotifications=_WwpLeosPbtMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,38,2,0))
_WwpLeosPbtMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosPbtMIBConformance=_WwpLeosPbtMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,38,3))
_WwpLeosPbtMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosPbtMIBCompliances=_WwpLeosPbtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,38,3,1))
_WwpLeosPbtMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosPbtMIBGroups=_WwpLeosPbtMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,38,3,2))
pbtGlobalConfigGroup=ObjectGroup((1,3,6,1,4,1,6141,2,60,38,3,2,1))
pbtGlobalConfigGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:pbtGlobalConfigGroup.setStatus(_A)
pbtBridgeNameMacMapGroup=ObjectGroup((1,3,6,1,4,1,6141,2,60,38,3,2,2))
pbtBridgeNameMacMapGroup.setObjects(*((_B,_Y),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:pbtBridgeNameMacMapGroup.setStatus(_A)
pbtReserveBvidGroup=ObjectGroup((1,3,6,1,4,1,6141,2,60,38,3,2,3))
pbtReserveBvidGroup.setObjects(*((_B,_Z),(_B,_A1)))
if mibBuilder.loadTexts:pbtReserveBvidGroup.setStatus(_A)
pbtVirtualCircuitGroup=ObjectGroup((1,3,6,1,4,1,6141,2,60,38,3,2,4))
pbtVirtualCircuitGroup.setObjects(*((_B,_P),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:pbtVirtualCircuitGroup.setStatus(_A)
pbtVirtualCircuitStatsGroup=ObjectGroup((1,3,6,1,4,1,6141,2,60,38,3,2,5))
pbtVirtualCircuitStatsGroup.setObjects(*((_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:pbtVirtualCircuitStatsGroup.setStatus(_A)
wwpLeosPbtTunnelFaultNotification=NotificationType((1,3,6,1,4,1,6141,2,60,38,2,0,1))
wwpLeosPbtTunnelFaultNotification.setObjects((_H,_K))
if mibBuilder.loadTexts:wwpLeosPbtTunnelFaultNotification.setStatus('deprecated')
wwpLeosPbtTunnelReversionNotification=NotificationType((1,3,6,1,4,1,6141,2,60,38,2,0,2))
wwpLeosPbtTunnelReversionNotification.setObjects(*((_H,_K),(_H,_L)))
if mibBuilder.loadTexts:wwpLeosPbtTunnelReversionNotification.setStatus(_A)
wwpLeosPbtTunnelActivateNotification=NotificationType((1,3,6,1,4,1,6141,2,60,38,2,0,3))
wwpLeosPbtTunnelActivateNotification.setObjects(*((_H,_K),(_H,_L),(_H,_K),(_H,_L),(_H,_W),(_H,_X)))
if mibBuilder.loadTexts:wwpLeosPbtTunnelActivateNotification.setStatus(_A)
wwpLeosPbtTunnelDeactivateNotification=NotificationType((1,3,6,1,4,1,6141,2,60,38,2,0,4))
wwpLeosPbtTunnelDeactivateNotification.setObjects(*((_H,_K),(_H,_L),(_H,_K),(_H,_L),(_H,_W),(_H,_X)))
if mibBuilder.loadTexts:wwpLeosPbtTunnelDeactivateNotification.setStatus(_A)
wwpLeosTcePbtTunnelActivateNotification=NotificationType((1,3,6,1,4,1,6141,2,60,38,2,0,10))
wwpLeosTcePbtTunnelActivateNotification.setObjects(*((_B,_T),(_B,_b),(_B,_M),(_B,_U),(_B,_c)))
if mibBuilder.loadTexts:wwpLeosTcePbtTunnelActivateNotification.setStatus(_A)
wwpLeosTcePbtTunnelDeactivateNotification=NotificationType((1,3,6,1,4,1,6141,2,60,38,2,0,11))
wwpLeosTcePbtTunnelDeactivateNotification.setObjects(*((_B,_T),(_B,_b),(_B,_M),(_B,_U),(_B,_c)))
if mibBuilder.loadTexts:wwpLeosTcePbtTunnelDeactivateNotification.setStatus(_A)
wwpLeosTcePbtTunnelReversionNotification=NotificationType((1,3,6,1,4,1,6141,2,60,38,2,0,12))
wwpLeosTcePbtTunnelReversionNotification.setObjects(*((_B,_M),(_B,_U),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:wwpLeosTcePbtTunnelReversionNotification.setStatus(_A)
pbtNotificationGroups=NotificationGroup((1,3,6,1,4,1,6141,2,60,38,3,2,6))
pbtNotificationGroups.setObjects(*((_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:pbtNotificationGroups.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'wwpLeosPbtMIB':wwpLeosPbtMIB,'wwpLeosPbtMIBObjects':wwpLeosPbtMIBObjects,'wwpLeosPbt':wwpLeosPbt,'wwpLeosPbtGlobalAttrs':wwpLeosPbtGlobalAttrs,_p:wwpLeosPbtBridgeMac,_q:wwpLeosPbtServiceTagEType,_r:wwpLeosPbtTunnelTagEtype,_s:wwpLeosPbtTunnelReversionState,_t:wwpLeosPbtTunnelReversionHoldTime,'wwpLeosPbtTransitTunnelEtypeRemark':wwpLeosPbtTransitTunnelEtypeRemark,_u:wwpLeosPbtAdminMode,_v:wwpLeosPbtOperMode,_w:wwpLeosPbtServiceVlanTpid,'wwpLeosPbtTunnelSwitchOverHoldTime':wwpLeosPbtTunnelSwitchOverHoldTime,'wwpLeosPbtBridgeNameMacMapTable':wwpLeosPbtBridgeNameMacMapTable,'wwpLeosPbtBridgeNameMacMapEntry':wwpLeosPbtBridgeNameMacMapEntry,_Y:wwpLeosPbtBridgeNameMacMapIndex,_x:wwpLeosPbtBridgeNameMacMapBridgeName,_y:wwpLeosPbtBridgeNameMacMapMacAddr,_z:wwpLeosPbtBridgeNameMacMapUseCount,_A0:wwpLeosPbtBridgeNameMacMapRowStatus,'wwpLeosPbtReservedBVIDTable':wwpLeosPbtReservedBVIDTable,'wwpLeosPbtReservedBVIDEntry':wwpLeosPbtReservedBVIDEntry,_Z:wwpLeosPbtReservedBVID,_A1:wwpLeosPbtReservedBVIDRowStatus,'wwpLeosPbtVirtualCircuitTable':wwpLeosPbtVirtualCircuitTable,'wwpLeosPbtVirtualCircuitEntry':wwpLeosPbtVirtualCircuitEntry,_P:wwpLeosPbtVirtualCircuitIndex,_A2:wwpLeosPbtVirtualCircuitName,_A3:wwpLeosPbtVirtualCircuitFixedEncapTunnelId,_A4:wwpLeosPbtVirtualCircuitDestBridgeIndex,_A5:wwpLeosPbtVirtualCircuitIngressISID,_A6:wwpLeosPbtVirtualCircuitEgressISID,_A7:wwpLeosPbtVirtualCircuitOperState,_A8:wwpLeosPbtVirtualCircuitEncapTunnelIdInUse,_A9:wwpLeosPbtVirtualCircuitRowStatus,'wwpLeosPbtVirtualCircuitRetainSTAG':wwpLeosPbtVirtualCircuitRetainSTAG,'wwpLeosPbtVirtualCircuitStag':wwpLeosPbtVirtualCircuitStag,'wwpLeosPbtVirtualCircuitStatsTable':wwpLeosPbtVirtualCircuitStatsTable,'wwpLeosPbtVirtualCircuitStatsEntry':wwpLeosPbtVirtualCircuitStatsEntry,_AA:wwpLeosPbtVirtualCircuitTxBytesHi,_AB:wwpLeosPbtVirtualCircuitTxBytesLo,_AC:wwpLeosPbtVirtualCircuitRxBytesHi,_AD:wwpLeosPbtVirtualCircuitRxBytesLo,'wwpLeosPbtLocalBridgeNameMacMapTable':wwpLeosPbtLocalBridgeNameMacMapTable,'wwpLeosPbtLocalBridgeNameMacMapEntry':wwpLeosPbtLocalBridgeNameMacMapEntry,_g:wwpLeosPbtLocalBridgeNameMacMapIndex,'wwpLeosPbtLocalBridgeNameMacMapBridgeName':wwpLeosPbtLocalBridgeNameMacMapBridgeName,'wwpLeosPbtLocalBridgeNameMacMapMacAddr':wwpLeosPbtLocalBridgeNameMacMapMacAddr,'wwpLeosPbtLocalBridgeNameMacMapUseCount':wwpLeosPbtLocalBridgeNameMacMapUseCount,'wwpLeosPbtLocalBridgeNameMacMapRowStatus':wwpLeosPbtLocalBridgeNameMacMapRowStatus,'wwpLeosTcePbt':wwpLeosTcePbt,'wwpLeosTcePbtServiceTable':wwpLeosTcePbtServiceTable,'wwpLeosTcePbtServiceEntry':wwpLeosTcePbtServiceEntry,_a:wwpLeosTcePbtServiceIndex,'wwpLeosTcePbtServiceName':wwpLeosTcePbtServiceName,'wwpLeosTcePbtServiceOperStatus':wwpLeosTcePbtServiceOperStatus,'wwpLeosTcePbtServiceFloodContProfileId':wwpLeosTcePbtServiceFloodContProfileId,'wwpLeosTcePbtServiceFloodContProfileName':wwpLeosTcePbtServiceFloodContProfileName,'wwpLeosTcePbtServiceVsIndex':wwpLeosTcePbtServiceVsIndex,'wwpLeosTcePbtServiceVsName':wwpLeosTcePbtServiceVsName,'wwpLeosTcePbtServiceTnlGroupIndex':wwpLeosTcePbtServiceTnlGroupIndex,'wwpLeosTcePbtServiceTnlGroupName':wwpLeosTcePbtServiceTnlGroupName,'wwpLeosTcePbtServiceIngressIsId':wwpLeosTcePbtServiceIngressIsId,'wwpLeosTcePbtServiceEgressIsId':wwpLeosTcePbtServiceEgressIsId,'wwpLeosTcePbtServiceFixedEgressPcp':wwpLeosTcePbtServiceFixedEgressPcp,'wwpLeosTcePbtServiceFrameCosPolicy':wwpLeosTcePbtServiceFrameCosPolicy,'wwpLeosTcePbtServiceFrameCosMapIndex':wwpLeosTcePbtServiceFrameCosMapIndex,'wwpLeosTcePbtServiceFrameCosMapName':wwpLeosTcePbtServiceFrameCosMapName,'wwpLeosTcePbtServiceResolvedCosPolicy':wwpLeosTcePbtServiceResolvedCosPolicy,'wwpLeosTcePbtServiceResolvedCosProfileIndex':wwpLeosTcePbtServiceResolvedCosProfileIndex,'wwpLeosTcePbtServiceResolvedCosProfileName':wwpLeosTcePbtServiceResolvedCosProfileName,'wwpLeosTcePbtServiceIngressMeterProfileId':wwpLeosTcePbtServiceIngressMeterProfileId,'wwpLeosTcePbtServiceIngressMeterProfileName':wwpLeosTcePbtServiceIngressMeterProfileName,'wwpLeosTcePbtServiceIngressMeterPolicy':wwpLeosTcePbtServiceIngressMeterPolicy,'wwpLeosTcePbtServiceRowStatus':wwpLeosTcePbtServiceRowStatus,'wwpLeosTcePbtTnlGroupTable':wwpLeosTcePbtTnlGroupTable,'wwpLeosTcePbtTnlGroupEntry':wwpLeosTcePbtTnlGroupEntry,_M:wwpLeosTcePbtTnlGroupIndex,_U:wwpLeosTcePbtTnlGroupName,'wwpLeosTcePbtTnlGroupSyncEnabled':wwpLeosTcePbtTnlGroupSyncEnabled,'wwpLeosTcePbtTnlGroupOperStatus':wwpLeosTcePbtTnlGroupOperStatus,'wwpLeosTcePbtTnlGroupUseCount':wwpLeosTcePbtTnlGroupUseCount,'wwpLeosTcePbtTnlGroupActivePair':wwpLeosTcePbtTnlGroupActivePair,'wwpLeosTcePbtTnlGroupReverting':wwpLeosTcePbtTnlGroupReverting,'wwpLeosTcePbtTnlGroupRowStatus':wwpLeosTcePbtTnlGroupRowStatus,'wwpLeosTcePbtEncapTnlTable':wwpLeosTcePbtEncapTnlTable,'wwpLeosTcePbtEncapTnlEntry':wwpLeosTcePbtEncapTnlEntry,_T:wwpLeosTcePbtEncapTnlIndex,_b:wwpLeosTcePbtEncapTnlName,'wwpLeosTcePbtEncapTnlRemoteBridgeIndex':wwpLeosTcePbtEncapTnlRemoteBridgeIndex,'wwpLeosTcePbtEncapTnlRemoteBridgeName':wwpLeosTcePbtEncapTnlRemoteBridgeName,'wwpLeosTcePbtEncapTnlGroupIndex':wwpLeosTcePbtEncapTnlGroupIndex,'wwpLeosTcePbtEncapTnlGroupName':wwpLeosTcePbtEncapTnlGroupName,'wwpLeosTcePbtEncapTnlBvId':wwpLeosTcePbtEncapTnlBvId,'wwpLeosTcePbtEncapTnlPgId':wwpLeosTcePbtEncapTnlPgId,'wwpLeosTcePbtEncapTnlPortName':wwpLeosTcePbtEncapTnlPortName,'wwpLeosTcePbtEncapTnlFaults':wwpLeosTcePbtEncapTnlFaults,'wwpLeosTcePbtEncapTnlAdminState':wwpLeosTcePbtEncapTnlAdminState,'wwpLeosTcePbtEncapTnlOperState':wwpLeosTcePbtEncapTnlOperState,_c:wwpLeosTcePbtEncapTnlFwdState,'wwpLeosTcePbtEncapTnlPaired':wwpLeosTcePbtEncapTnlPaired,'wwpLeosTcePbtEncapTnlPairIndex':wwpLeosTcePbtEncapTnlPairIndex,'wwpLeosTcePbtEncapTnlPairOperState':wwpLeosTcePbtEncapTnlPairOperState,'wwpLeosTcePbtEncapTnlFrameCosPolicy':wwpLeosTcePbtEncapTnlFrameCosPolicy,'wwpLeosTcePbtEncapTnlFrameCosMapIndex':wwpLeosTcePbtEncapTnlFrameCosMapIndex,'wwpLeosTcePbtEncapTnlFrameCosMapName':wwpLeosTcePbtEncapTnlFrameCosMapName,'wwpLeosTcePbtEncapTnlFixedPcp':wwpLeosTcePbtEncapTnlFixedPcp,'wwpLeosTcePbtEncapTnlCfmConfigured':wwpLeosTcePbtEncapTnlCfmConfigured,'wwpLeosTcePbtEncapTnlPairedDecapIndex':wwpLeosTcePbtEncapTnlPairedDecapIndex,'wwpLeosTcePbtEncapTnlPairedDecapName':wwpLeosTcePbtEncapTnlPairedDecapName,'wwpLeosTcePbtEncapTnlWeight':wwpLeosTcePbtEncapTnlWeight,'wwpLeosTcePbtEncapTnlStatsEnabled':wwpLeosTcePbtEncapTnlStatsEnabled,'wwpLeosTcePbtEncapTnlLocalBridgeIndex':wwpLeosTcePbtEncapTnlLocalBridgeIndex,'wwpLeosTcePbtEncapTnlLocalBridgeName':wwpLeosTcePbtEncapTnlLocalBridgeName,_AE:wwpLeosTcePbtEncapTnlReversionToPairIndex,_AF:wwpLeosTcePbtEncapTnlReversionFromPairIndex,'wwpLeosTcePbtEncapTnlRowStatus':wwpLeosTcePbtEncapTnlRowStatus,'wwpLeosTcePbtDecapTnlTable':wwpLeosTcePbtDecapTnlTable,'wwpLeosTcePbtDecapTnlEntry':wwpLeosTcePbtDecapTnlEntry,_m:wwpLeosTcePbtDecapTnlIndex,'wwpLeosTcePbtDecapTnlName':wwpLeosTcePbtDecapTnlName,'wwpLeosTcePbtDecapTnlRemoteBridgeIndex':wwpLeosTcePbtDecapTnlRemoteBridgeIndex,'wwpLeosTcePbtDecapTnlRemoteBridgeName':wwpLeosTcePbtDecapTnlRemoteBridgeName,'wwpLeosTcePbtDecapTnlGroupIndex':wwpLeosTcePbtDecapTnlGroupIndex,'wwpLeosTcePbtDecapTnlGroupName':wwpLeosTcePbtDecapTnlGroupName,'wwpLeosTcePbtDecapTnlBvId':wwpLeosTcePbtDecapTnlBvId,'wwpLeosTcePbtDecapTnlPgId':wwpLeosTcePbtDecapTnlPgId,'wwpLeosTcePbtDecapTnlPortName':wwpLeosTcePbtDecapTnlPortName,'wwpLeosTcePbtDecapTnlFaults':wwpLeosTcePbtDecapTnlFaults,'wwpLeosTcePbtDecapTnlOperState':wwpLeosTcePbtDecapTnlOperState,'wwpLeosTcePbtDecapTnlFwdState':wwpLeosTcePbtDecapTnlFwdState,'wwpLeosTcePbtDecapTnlPaired':wwpLeosTcePbtDecapTnlPaired,'wwpLeosTcePbtDecapTnlPairIndex':wwpLeosTcePbtDecapTnlPairIndex,'wwpLeosTcePbtDecapTnlPairOperState':wwpLeosTcePbtDecapTnlPairOperState,'wwpLeosTcePbtDecapTnlResolvedCosPolicy':wwpLeosTcePbtDecapTnlResolvedCosPolicy,'wwpLeosTcePbtDecapTnlResolvedCosMapIndex':wwpLeosTcePbtDecapTnlResolvedCosMapIndex,'wwpLeosTcePbtDecapTnlResolvedCosMapName':wwpLeosTcePbtDecapTnlResolvedCosMapName,'wwpLeosTcePbtDecapTnlCfmConfigured':wwpLeosTcePbtDecapTnlCfmConfigured,'wwpLeosTcePbtDecapTnlPairedEncapIndex':wwpLeosTcePbtDecapTnlPairedEncapIndex,'wwpLeosTcePbtDecapTnlPairedEncapName':wwpLeosTcePbtDecapTnlPairedEncapName,'wwpLeosTcePbtDecapTnlStatsEnabled':wwpLeosTcePbtDecapTnlStatsEnabled,'wwpLeosTcePbtDecapTnlRowStatus':wwpLeosTcePbtDecapTnlRowStatus,'wwpLeosTcePbtServiceUserFrameL2TransformTable':wwpLeosTcePbtServiceUserFrameL2TransformTable,'wwpLeosTcePbtServiceUserFrameL2TransformEntry':wwpLeosTcePbtServiceUserFrameL2TransformEntry,_n:wwpLeosTcePbtServiceUserFrameL2TransformDirection,_o:wwpLeosTcePbtServiceUserFrameL2TransformTagIndex,'wwpLeosTcePbtServiceUserFrameL2TransformTagAction':wwpLeosTcePbtServiceUserFrameL2TransformTagAction,'wwpLeosTcePbtServiceUserFrameL2TransformTagValue':wwpLeosTcePbtServiceUserFrameL2TransformTagValue,'wwpLeosTcePbtServiceUserFrameL2TransformTagEtype':wwpLeosTcePbtServiceUserFrameL2TransformTagEtype,'wwpLeosTcePbtServiceUserFrameL2TransformTagPriority':wwpLeosTcePbtServiceUserFrameL2TransformTagPriority,'wwpLeosTcePbtServiceUserFrameL2TransformPriPolicy':wwpLeosTcePbtServiceUserFrameL2TransformPriPolicy,'wwpLeosTcePbtServiceUserFrameL2TransformUseTagValue':wwpLeosTcePbtServiceUserFrameL2TransformUseTagValue,'wwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype':wwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype,'wwpLeosPbtMIBNotificationPrefix':wwpLeosPbtMIBNotificationPrefix,'wwpLeosPbtMIBNotifications':wwpLeosPbtMIBNotifications,_AG:wwpLeosPbtTunnelFaultNotification,'wwpLeosPbtTunnelReversionNotification':wwpLeosPbtTunnelReversionNotification,'wwpLeosPbtTunnelActivateNotification':wwpLeosPbtTunnelActivateNotification,'wwpLeosPbtTunnelDeactivateNotification':wwpLeosPbtTunnelDeactivateNotification,_AH:wwpLeosTcePbtTunnelActivateNotification,_AI:wwpLeosTcePbtTunnelDeactivateNotification,_AJ:wwpLeosTcePbtTunnelReversionNotification,'wwpLeosPbtMIBConformance':wwpLeosPbtMIBConformance,'wwpLeosPbtMIBCompliances':wwpLeosPbtMIBCompliances,'wwpLeosPbtMIBGroups':wwpLeosPbtMIBGroups,'pbtGlobalConfigGroup':pbtGlobalConfigGroup,'pbtBridgeNameMacMapGroup':pbtBridgeNameMacMapGroup,'pbtReserveBvidGroup':pbtReserveBvidGroup,'pbtVirtualCircuitGroup':pbtVirtualCircuitGroup,'pbtVirtualCircuitStatsGroup':pbtVirtualCircuitStatsGroup,'pbtNotificationGroups':pbtNotificationGroups})