_g='zxAnTRTdmSrcSlotNo'
_f='zxAnTRTdmSrcShelfNo'
_e='zxAnTRTdmSrcRackNo'
_d='zxAnTRPwIndex'
_c='zxAnVplsVfiMacAddr'
_b='zxAnVplsVfiMacAddrType'
_a='zxAnL3IfVfiIfIndex'
_Z='zxAnVplsVfiPeerIpAddr'
_Y='zxAnVplsVfiPeerIpAddrType'
_X='static'
_W='dynamic'
_V='second'
_U='disable'
_T='enable'
_S='zxAnVpwsL3IfIndex'
_R='zxAnMplsStaticPwName'
_Q='reserved5'
_P='reserved4'
_O='reserved3'
_N='reserved2'
_M='reserved1'
_L='kbps'
_K='TruthValue'
_J='zxAnVplsVfiName'
_I='DisplayString'
_H='read-only'
_G='InetAddressType'
_F='Unsigned32'
_E='not-accessible'
_D='ZTE-AN-MPLS-L2VPN-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'experimental','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','RowStatus','TextualConvention',_K)
ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIfindex','zxAn')
IANAPwPsnTypeTC,IANAPwTypeTC=mibBuilder.importSymbols('ZX-PWE3-MIB','IANAPwPsnTypeTC','IANAPwTypeTC')
PwIndexType,=mibBuilder.importSymbols('ZXPW-TC-STD-MIB','PwIndexType')
zxAnMplsL2vpnMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,59))
class ZxAnMplsVccvCcType(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('pwAch',0),('mplsRouterAlertLbl',1),('mplsPwLblTtlEqualsOne',2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7)))
class ZxAnMplsVccvCvType(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('icmpPing',0),('lspPing',1),('bfd',2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7)))
_ZxAnL2vpnGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnL2vpnGlobalObjects=_ZxAnL2vpnGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,59,1))
_ZxAnMplsStaticPwTable_Object=MibTable
zxAnMplsStaticPwTable=_ZxAnMplsStaticPwTable_Object((1,3,6,1,4,1,3902,1015,59,1,11))
if mibBuilder.loadTexts:zxAnMplsStaticPwTable.setStatus(_A)
_ZxAnMplsStaticPwEntry_Object=MibTableRow
zxAnMplsStaticPwEntry=_ZxAnMplsStaticPwEntry_Object((1,3,6,1,4,1,3902,1015,59,1,11,1))
zxAnMplsStaticPwEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:zxAnMplsStaticPwEntry.setStatus(_A)
class _ZxAnMplsStaticPwName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_ZxAnMplsStaticPwName_Type.__name__=_I
_ZxAnMplsStaticPwName_Object=MibTableColumn
zxAnMplsStaticPwName=_ZxAnMplsStaticPwName_Object((1,3,6,1,4,1,3902,1015,59,1,11,1,2),_ZxAnMplsStaticPwName_Type())
zxAnMplsStaticPwName.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMplsStaticPwName.setStatus(_A)
class _ZxAnMplsOutgoingPwLabel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1044479,1048575))
_ZxAnMplsOutgoingPwLabel_Type.__name__=_F
_ZxAnMplsOutgoingPwLabel_Object=MibTableColumn
zxAnMplsOutgoingPwLabel=_ZxAnMplsOutgoingPwLabel_Object((1,3,6,1,4,1,3902,1015,59,1,11,1,3),_ZxAnMplsOutgoingPwLabel_Type())
zxAnMplsOutgoingPwLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMplsOutgoingPwLabel.setStatus(_A)
class _ZxAnMplsIncomingPwLabel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1048575))
_ZxAnMplsIncomingPwLabel_Type.__name__=_F
_ZxAnMplsIncomingPwLabel_Object=MibTableColumn
zxAnMplsIncomingPwLabel=_ZxAnMplsIncomingPwLabel_Object((1,3,6,1,4,1,3902,1015,59,1,11,1,4),_ZxAnMplsIncomingPwLabel_Type())
zxAnMplsIncomingPwLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMplsIncomingPwLabel.setStatus(_A)
_ZxAnMplsStaticPwRowStatus_Type=RowStatus
_ZxAnMplsStaticPwRowStatus_Object=MibTableColumn
zxAnMplsStaticPwRowStatus=_ZxAnMplsStaticPwRowStatus_Object((1,3,6,1,4,1,3902,1015,59,1,11,1,31),_ZxAnMplsStaticPwRowStatus_Type())
zxAnMplsStaticPwRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMplsStaticPwRowStatus.setStatus(_A)
_ZxAnVpwsObjects_ObjectIdentity=ObjectIdentity
zxAnVpwsObjects=_ZxAnVpwsObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,59,2))
_ZxAnVpwsTable_Object=MibTable
zxAnVpwsTable=_ZxAnVpwsTable_Object((1,3,6,1,4,1,3902,1015,59,2,11))
if mibBuilder.loadTexts:zxAnVpwsTable.setStatus(_A)
_ZxAnVpwsEntry_Object=MibTableRow
zxAnVpwsEntry=_ZxAnVpwsEntry_Object((1,3,6,1,4,1,3902,1015,59,2,11,1))
zxAnVpwsEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:zxAnVpwsEntry.setStatus(_A)
_ZxAnVpwsL3IfIndex_Type=ZxAnIfindex
_ZxAnVpwsL3IfIndex_Object=MibTableColumn
zxAnVpwsL3IfIndex=_ZxAnVpwsL3IfIndex_Object((1,3,6,1,4,1,3902,1015,59,2,11,1,1),_ZxAnVpwsL3IfIndex_Type())
zxAnVpwsL3IfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVpwsL3IfIndex.setStatus(_A)
class _ZxAnVpwsPeerIpAddrType_Type(InetAddressType):defaultValue=1
_ZxAnVpwsPeerIpAddrType_Type.__name__=_G
_ZxAnVpwsPeerIpAddrType_Object=MibTableColumn
zxAnVpwsPeerIpAddrType=_ZxAnVpwsPeerIpAddrType_Object((1,3,6,1,4,1,3902,1015,59,2,11,1,2),_ZxAnVpwsPeerIpAddrType_Type())
zxAnVpwsPeerIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVpwsPeerIpAddrType.setStatus(_A)
_ZxAnVpwsPeerIpAddr_Type=InetAddress
_ZxAnVpwsPeerIpAddr_Object=MibTableColumn
zxAnVpwsPeerIpAddr=_ZxAnVpwsPeerIpAddr_Object((1,3,6,1,4,1,3902,1015,59,2,11,1,3),_ZxAnVpwsPeerIpAddr_Type())
zxAnVpwsPeerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVpwsPeerIpAddr.setStatus(_A)
class _ZxAnVpwsVcId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ZxAnVpwsVcId_Type.__name__=_F
_ZxAnVpwsVcId_Object=MibTableColumn
zxAnVpwsVcId=_ZxAnVpwsVcId_Object((1,3,6,1,4,1,3902,1015,59,2,11,1,4),_ZxAnVpwsVcId_Type())
zxAnVpwsVcId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVpwsVcId.setStatus(_A)
_ZxAnVpwsPwType_Type=IANAPwTypeTC
_ZxAnVpwsPwType_Object=MibTableColumn
zxAnVpwsPwType=_ZxAnVpwsPwType_Object((1,3,6,1,4,1,3902,1015,59,2,11,1,5),_ZxAnVpwsPwType_Type())
zxAnVpwsPwType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVpwsPwType.setStatus(_A)
_ZxAnVpwsStaticPwName_Type=DisplayString
_ZxAnVpwsStaticPwName_Object=MibTableColumn
zxAnVpwsStaticPwName=_ZxAnVpwsStaticPwName_Object((1,3,6,1,4,1,3902,1015,59,2,11,1,6),_ZxAnVpwsStaticPwName_Type())
zxAnVpwsStaticPwName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVpwsStaticPwName.setStatus(_A)
class _ZxAnVpwsStandbyPeerIpAddrType_Type(InetAddressType):defaultValue=1
_ZxAnVpwsStandbyPeerIpAddrType_Type.__name__=_G
_ZxAnVpwsStandbyPeerIpAddrType_Object=MibTableColumn
zxAnVpwsStandbyPeerIpAddrType=_ZxAnVpwsStandbyPeerIpAddrType_Object((1,3,6,1,4,1,3902,1015,59,2,11,1,7),_ZxAnVpwsStandbyPeerIpAddrType_Type())
zxAnVpwsStandbyPeerIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVpwsStandbyPeerIpAddrType.setStatus(_A)
_ZxAnVpwsStandbyPeerIpAddr_Type=InetAddress
_ZxAnVpwsStandbyPeerIpAddr_Object=MibTableColumn
zxAnVpwsStandbyPeerIpAddr=_ZxAnVpwsStandbyPeerIpAddr_Object((1,3,6,1,4,1,3902,1015,59,2,11,1,8),_ZxAnVpwsStandbyPeerIpAddr_Type())
zxAnVpwsStandbyPeerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVpwsStandbyPeerIpAddr.setStatus(_A)
class _ZxAnVpwsStandbyVcId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ZxAnVpwsStandbyVcId_Type.__name__=_F
_ZxAnVpwsStandbyVcId_Object=MibTableColumn
zxAnVpwsStandbyVcId=_ZxAnVpwsStandbyVcId_Object((1,3,6,1,4,1,3902,1015,59,2,11,1,9),_ZxAnVpwsStandbyVcId_Type())
zxAnVpwsStandbyVcId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVpwsStandbyVcId.setStatus(_A)
class _ZxAnVpwsPwe3CWPreferred_Type(TruthValue):defaultValue=2
_ZxAnVpwsPwe3CWPreferred_Type.__name__=_K
_ZxAnVpwsPwe3CWPreferred_Object=MibTableColumn
zxAnVpwsPwe3CWPreferred=_ZxAnVpwsPwe3CWPreferred_Object((1,3,6,1,4,1,3902,1015,59,2,11,1,10),_ZxAnVpwsPwe3CWPreferred_Type())
zxAnVpwsPwe3CWPreferred.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVpwsPwe3CWPreferred.setStatus(_A)
class _ZxAnVpwsVccvEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_ZxAnVpwsVccvEnable_Type.__name__=_C
_ZxAnVpwsVccvEnable_Object=MibTableColumn
zxAnVpwsVccvEnable=_ZxAnVpwsVccvEnable_Object((1,3,6,1,4,1,3902,1015,59,2,11,1,11),_ZxAnVpwsVccvEnable_Type())
zxAnVpwsVccvEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVpwsVccvEnable.setStatus(_A)
_ZxAnVpwsCcTypeCapability_Type=ZxAnMplsVccvCcType
_ZxAnVpwsCcTypeCapability_Object=MibTableColumn
zxAnVpwsCcTypeCapability=_ZxAnVpwsCcTypeCapability_Object((1,3,6,1,4,1,3902,1015,59,2,11,1,12),_ZxAnVpwsCcTypeCapability_Type())
zxAnVpwsCcTypeCapability.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnVpwsCcTypeCapability.setStatus(_A)
_ZxAnVpwsCvTypeCapability_Type=ZxAnMplsVccvCvType
_ZxAnVpwsCvTypeCapability_Object=MibTableColumn
zxAnVpwsCvTypeCapability=_ZxAnVpwsCvTypeCapability_Object((1,3,6,1,4,1,3902,1015,59,2,11,1,13),_ZxAnVpwsCvTypeCapability_Type())
zxAnVpwsCvTypeCapability.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnVpwsCvTypeCapability.setStatus(_A)
_ZxAnVpwsRowStatus_Type=RowStatus
_ZxAnVpwsRowStatus_Object=MibTableColumn
zxAnVpwsRowStatus=_ZxAnVpwsRowStatus_Object((1,3,6,1,4,1,3902,1015,59,2,11,1,31),_ZxAnVpwsRowStatus_Type())
zxAnVpwsRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVpwsRowStatus.setStatus(_A)
_ZxAnVplsObjects_ObjectIdentity=ObjectIdentity
zxAnVplsObjects=_ZxAnVplsObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,59,3))
_ZxAnVplsVfiConfigTable_Object=MibTable
zxAnVplsVfiConfigTable=_ZxAnVplsVfiConfigTable_Object((1,3,6,1,4,1,3902,1015,59,3,11))
if mibBuilder.loadTexts:zxAnVplsVfiConfigTable.setStatus(_A)
_ZxAnVplsVfiConfigEntry_Object=MibTableRow
zxAnVplsVfiConfigEntry=_ZxAnVplsVfiConfigEntry_Object((1,3,6,1,4,1,3902,1015,59,3,11,1))
zxAnVplsVfiConfigEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:zxAnVplsVfiConfigEntry.setStatus(_A)
class _ZxAnVplsVfiName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_ZxAnVplsVfiName_Type.__name__=_I
_ZxAnVplsVfiName_Object=MibTableColumn
zxAnVplsVfiName=_ZxAnVplsVfiName_Object((1,3,6,1,4,1,3902,1015,59,3,11,1,1),_ZxAnVplsVfiName_Type())
zxAnVplsVfiName.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVplsVfiName.setStatus(_A)
class _ZxAnVplsVfiVcid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ZxAnVplsVfiVcid_Type.__name__=_F
_ZxAnVplsVfiVcid_Object=MibTableColumn
zxAnVplsVfiVcid=_ZxAnVplsVfiVcid_Object((1,3,6,1,4,1,3902,1015,59,3,11,1,2),_ZxAnVplsVfiVcid_Type())
zxAnVplsVfiVcid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiVcid.setStatus(_A)
_ZxAnVplsVfiPwType_Type=IANAPwTypeTC
_ZxAnVplsVfiPwType_Object=MibTableColumn
zxAnVplsVfiPwType=_ZxAnVplsVfiPwType_Object((1,3,6,1,4,1,3902,1015,59,3,11,1,3),_ZxAnVplsVfiPwType_Type())
zxAnVplsVfiPwType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiPwType.setStatus(_A)
class _ZxAnVplsVfiMaxMacLearningNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_ZxAnVplsVfiMaxMacLearningNum_Type.__name__=_C
_ZxAnVplsVfiMaxMacLearningNum_Object=MibTableColumn
zxAnVplsVfiMaxMacLearningNum=_ZxAnVplsVfiMaxMacLearningNum_Object((1,3,6,1,4,1,3902,1015,59,3,11,1,4),_ZxAnVplsVfiMaxMacLearningNum_Type())
zxAnVplsVfiMaxMacLearningNum.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiMaxMacLearningNum.setStatus(_A)
class _ZxAnVplsVfiRemoteMacAgingTime_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(180,3600))
_ZxAnVplsVfiRemoteMacAgingTime_Type.__name__=_C
_ZxAnVplsVfiRemoteMacAgingTime_Object=MibTableColumn
zxAnVplsVfiRemoteMacAgingTime=_ZxAnVplsVfiRemoteMacAgingTime_Object((1,3,6,1,4,1,3902,1015,59,3,11,1,5),_ZxAnVplsVfiRemoteMacAgingTime_Type())
zxAnVplsVfiRemoteMacAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiRemoteMacAgingTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnVplsVfiRemoteMacAgingTime.setUnits(_V)
class _ZxAnVplsVfiLocalMacAgingTime_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(180,3600))
_ZxAnVplsVfiLocalMacAgingTime_Type.__name__=_C
_ZxAnVplsVfiLocalMacAgingTime_Object=MibTableColumn
zxAnVplsVfiLocalMacAgingTime=_ZxAnVplsVfiLocalMacAgingTime_Object((1,3,6,1,4,1,3902,1015,59,3,11,1,6),_ZxAnVplsVfiLocalMacAgingTime_Type())
zxAnVplsVfiLocalMacAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiLocalMacAgingTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnVplsVfiLocalMacAgingTime.setUnits(_V)
class _ZxAnVplsVfiBCastRateLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,16384000))
_ZxAnVplsVfiBCastRateLimit_Type.__name__=_C
_ZxAnVplsVfiBCastRateLimit_Object=MibTableColumn
zxAnVplsVfiBCastRateLimit=_ZxAnVplsVfiBCastRateLimit_Object((1,3,6,1,4,1,3902,1015,59,3,11,1,7),_ZxAnVplsVfiBCastRateLimit_Type())
zxAnVplsVfiBCastRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiBCastRateLimit.setStatus(_A)
if mibBuilder.loadTexts:zxAnVplsVfiBCastRateLimit.setUnits(_L)
class _ZxAnVplsVfiMCastRateLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,16384000))
_ZxAnVplsVfiMCastRateLimit_Type.__name__=_C
_ZxAnVplsVfiMCastRateLimit_Object=MibTableColumn
zxAnVplsVfiMCastRateLimit=_ZxAnVplsVfiMCastRateLimit_Object((1,3,6,1,4,1,3902,1015,59,3,11,1,8),_ZxAnVplsVfiMCastRateLimit_Type())
zxAnVplsVfiMCastRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiMCastRateLimit.setStatus(_A)
if mibBuilder.loadTexts:zxAnVplsVfiMCastRateLimit.setUnits(_L)
class _ZxAnVplsVfiUnknownUCastRateLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,16384000))
_ZxAnVplsVfiUnknownUCastRateLimit_Type.__name__=_C
_ZxAnVplsVfiUnknownUCastRateLimit_Object=MibTableColumn
zxAnVplsVfiUnknownUCastRateLimit=_ZxAnVplsVfiUnknownUCastRateLimit_Object((1,3,6,1,4,1,3902,1015,59,3,11,1,9),_ZxAnVplsVfiUnknownUCastRateLimit_Type())
zxAnVplsVfiUnknownUCastRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiUnknownUCastRateLimit.setStatus(_A)
if mibBuilder.loadTexts:zxAnVplsVfiUnknownUCastRateLimit.setUnits(_L)
class _ZxAnVplsVfiVcidType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_ZxAnVplsVfiVcidType_Type.__name__=_C
_ZxAnVplsVfiVcidType_Object=MibTableColumn
zxAnVplsVfiVcidType=_ZxAnVplsVfiVcidType_Object((1,3,6,1,4,1,3902,1015,59,3,11,1,10),_ZxAnVplsVfiVcidType_Type())
zxAnVplsVfiVcidType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiVcidType.setStatus(_A)
class _ZxAnVplsVfiPwe3CWPreferred_Type(TruthValue):defaultValue=2
_ZxAnVplsVfiPwe3CWPreferred_Type.__name__=_K
_ZxAnVplsVfiPwe3CWPreferred_Object=MibTableColumn
zxAnVplsVfiPwe3CWPreferred=_ZxAnVplsVfiPwe3CWPreferred_Object((1,3,6,1,4,1,3902,1015,59,3,11,1,11),_ZxAnVplsVfiPwe3CWPreferred_Type())
zxAnVplsVfiPwe3CWPreferred.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiPwe3CWPreferred.setStatus(_A)
class _ZxAnVplsVfiVccvEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_ZxAnVplsVfiVccvEnable_Type.__name__=_C
_ZxAnVplsVfiVccvEnable_Object=MibTableColumn
zxAnVplsVfiVccvEnable=_ZxAnVplsVfiVccvEnable_Object((1,3,6,1,4,1,3902,1015,59,3,11,1,12),_ZxAnVplsVfiVccvEnable_Type())
zxAnVplsVfiVccvEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiVccvEnable.setStatus(_A)
_ZxAnVplsVfiCcTypeCapability_Type=ZxAnMplsVccvCcType
_ZxAnVplsVfiCcTypeCapability_Object=MibTableColumn
zxAnVplsVfiCcTypeCapability=_ZxAnVplsVfiCcTypeCapability_Object((1,3,6,1,4,1,3902,1015,59,3,11,1,13),_ZxAnVplsVfiCcTypeCapability_Type())
zxAnVplsVfiCcTypeCapability.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnVplsVfiCcTypeCapability.setStatus(_A)
_ZxAnVplsVfiCvTypeCapability_Type=ZxAnMplsVccvCvType
_ZxAnVplsVfiCvTypeCapability_Object=MibTableColumn
zxAnVplsVfiCvTypeCapability=_ZxAnVplsVfiCvTypeCapability_Object((1,3,6,1,4,1,3902,1015,59,3,11,1,14),_ZxAnVplsVfiCvTypeCapability_Type())
zxAnVplsVfiCvTypeCapability.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnVplsVfiCvTypeCapability.setStatus(_A)
_ZxAnVplsVfiRowStatus_Type=RowStatus
_ZxAnVplsVfiRowStatus_Object=MibTableColumn
zxAnVplsVfiRowStatus=_ZxAnVplsVfiRowStatus_Object((1,3,6,1,4,1,3902,1015,59,3,11,1,30),_ZxAnVplsVfiRowStatus_Type())
zxAnVplsVfiRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiRowStatus.setStatus(_A)
_ZxAnVplsVfiPeerIpAddrTable_Object=MibTable
zxAnVplsVfiPeerIpAddrTable=_ZxAnVplsVfiPeerIpAddrTable_Object((1,3,6,1,4,1,3902,1015,59,3,12))
if mibBuilder.loadTexts:zxAnVplsVfiPeerIpAddrTable.setStatus(_A)
_ZxAnVplsVfiPeerIpAddrEntry_Object=MibTableRow
zxAnVplsVfiPeerIpAddrEntry=_ZxAnVplsVfiPeerIpAddrEntry_Object((1,3,6,1,4,1,3902,1015,59,3,12,1))
zxAnVplsVfiPeerIpAddrEntry.setIndexNames((0,_D,_J),(0,_D,_Y),(0,_D,_Z))
if mibBuilder.loadTexts:zxAnVplsVfiPeerIpAddrEntry.setStatus(_A)
class _ZxAnVplsVfiPeerIpAddrType_Type(InetAddressType):defaultValue=1
_ZxAnVplsVfiPeerIpAddrType_Type.__name__=_G
_ZxAnVplsVfiPeerIpAddrType_Object=MibTableColumn
zxAnVplsVfiPeerIpAddrType=_ZxAnVplsVfiPeerIpAddrType_Object((1,3,6,1,4,1,3902,1015,59,3,12,1,1),_ZxAnVplsVfiPeerIpAddrType_Type())
zxAnVplsVfiPeerIpAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVplsVfiPeerIpAddrType.setStatus(_A)
_ZxAnVplsVfiPeerIpAddr_Type=InetAddress
_ZxAnVplsVfiPeerIpAddr_Object=MibTableColumn
zxAnVplsVfiPeerIpAddr=_ZxAnVplsVfiPeerIpAddr_Object((1,3,6,1,4,1,3902,1015,59,3,12,1,2),_ZxAnVplsVfiPeerIpAddr_Type())
zxAnVplsVfiPeerIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVplsVfiPeerIpAddr.setStatus(_A)
class _ZxAnVplsVfiStandbyPeerIpAddrType_Type(InetAddressType):defaultValue=1
_ZxAnVplsVfiStandbyPeerIpAddrType_Type.__name__=_G
_ZxAnVplsVfiStandbyPeerIpAddrType_Object=MibTableColumn
zxAnVplsVfiStandbyPeerIpAddrType=_ZxAnVplsVfiStandbyPeerIpAddrType_Object((1,3,6,1,4,1,3902,1015,59,3,12,1,3),_ZxAnVplsVfiStandbyPeerIpAddrType_Type())
zxAnVplsVfiStandbyPeerIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiStandbyPeerIpAddrType.setStatus(_A)
_ZxAnVplsVfiStandbyPeerIpAddr_Type=InetAddress
_ZxAnVplsVfiStandbyPeerIpAddr_Object=MibTableColumn
zxAnVplsVfiStandbyPeerIpAddr=_ZxAnVplsVfiStandbyPeerIpAddr_Object((1,3,6,1,4,1,3902,1015,59,3,12,1,4),_ZxAnVplsVfiStandbyPeerIpAddr_Type())
zxAnVplsVfiStandbyPeerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiStandbyPeerIpAddr.setStatus(_A)
class _ZxAnVplsVfiStaticPwName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_ZxAnVplsVfiStaticPwName_Type.__name__=_I
_ZxAnVplsVfiStaticPwName_Object=MibTableColumn
zxAnVplsVfiStaticPwName=_ZxAnVplsVfiStaticPwName_Object((1,3,6,1,4,1,3902,1015,59,3,12,1,5),_ZxAnVplsVfiStaticPwName_Type())
zxAnVplsVfiStaticPwName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiStaticPwName.setStatus(_A)
class _ZxAnVplsVfiPwNetType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('spoke',1),('hub',2)))
_ZxAnVplsVfiPwNetType_Type.__name__=_C
_ZxAnVplsVfiPwNetType_Object=MibTableColumn
zxAnVplsVfiPwNetType=_ZxAnVplsVfiPwNetType_Object((1,3,6,1,4,1,3902,1015,59,3,12,1,6),_ZxAnVplsVfiPwNetType_Type())
zxAnVplsVfiPwNetType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiPwNetType.setStatus(_A)
_ZxAnVplsVfiPeerRowStatus_Type=RowStatus
_ZxAnVplsVfiPeerRowStatus_Object=MibTableColumn
zxAnVplsVfiPeerRowStatus=_ZxAnVplsVfiPeerRowStatus_Object((1,3,6,1,4,1,3902,1015,59,3,12,1,20),_ZxAnVplsVfiPeerRowStatus_Type())
zxAnVplsVfiPeerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiPeerRowStatus.setStatus(_A)
_ZxAnL3IfVfiConfigTable_Object=MibTable
zxAnL3IfVfiConfigTable=_ZxAnL3IfVfiConfigTable_Object((1,3,6,1,4,1,3902,1015,59,3,13))
if mibBuilder.loadTexts:zxAnL3IfVfiConfigTable.setStatus(_A)
_ZxAnL3IfVfiConfigEntry_Object=MibTableRow
zxAnL3IfVfiConfigEntry=_ZxAnL3IfVfiConfigEntry_Object((1,3,6,1,4,1,3902,1015,59,3,13,1))
zxAnL3IfVfiConfigEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:zxAnL3IfVfiConfigEntry.setStatus(_A)
_ZxAnL3IfVfiIfIndex_Type=ZxAnIfindex
_ZxAnL3IfVfiIfIndex_Object=MibTableColumn
zxAnL3IfVfiIfIndex=_ZxAnL3IfVfiIfIndex_Object((1,3,6,1,4,1,3902,1015,59,3,13,1,1),_ZxAnL3IfVfiIfIndex_Type())
zxAnL3IfVfiIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnL3IfVfiIfIndex.setStatus(_A)
class _ZxAnL3IfVfiName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_ZxAnL3IfVfiName_Type.__name__=_I
_ZxAnL3IfVfiName_Object=MibTableColumn
zxAnL3IfVfiName=_ZxAnL3IfVfiName_Object((1,3,6,1,4,1,3902,1015,59,3,13,1,2),_ZxAnL3IfVfiName_Type())
zxAnL3IfVfiName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnL3IfVfiName.setStatus(_A)
_ZxAnL3IfVfiRowStatus_Type=RowStatus
_ZxAnL3IfVfiRowStatus_Object=MibTableColumn
zxAnL3IfVfiRowStatus=_ZxAnL3IfVfiRowStatus_Object((1,3,6,1,4,1,3902,1015,59,3,13,1,20),_ZxAnL3IfVfiRowStatus_Type())
zxAnL3IfVfiRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnL3IfVfiRowStatus.setStatus(_A)
_ZxAnVplsVfiMacTable_Object=MibTable
zxAnVplsVfiMacTable=_ZxAnVplsVfiMacTable_Object((1,3,6,1,4,1,3902,1015,59,3,14))
if mibBuilder.loadTexts:zxAnVplsVfiMacTable.setStatus(_A)
_ZxAnVplsVfiMacEntry_Object=MibTableRow
zxAnVplsVfiMacEntry=_ZxAnVplsVfiMacEntry_Object((1,3,6,1,4,1,3902,1015,59,3,14,1))
zxAnVplsVfiMacEntry.setIndexNames((0,_D,_J),(0,_D,_b),(0,_D,_c))
if mibBuilder.loadTexts:zxAnVplsVfiMacEntry.setStatus(_A)
class _ZxAnVplsVfiMacAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_ZxAnVplsVfiMacAddrType_Type.__name__=_C
_ZxAnVplsVfiMacAddrType_Object=MibTableColumn
zxAnVplsVfiMacAddrType=_ZxAnVplsVfiMacAddrType_Object((1,3,6,1,4,1,3902,1015,59,3,14,1,1),_ZxAnVplsVfiMacAddrType_Type())
zxAnVplsVfiMacAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVplsVfiMacAddrType.setStatus(_A)
_ZxAnVplsVfiMacAddr_Type=MacAddress
_ZxAnVplsVfiMacAddr_Object=MibTableColumn
zxAnVplsVfiMacAddr=_ZxAnVplsVfiMacAddr_Object((1,3,6,1,4,1,3902,1015,59,3,14,1,2),_ZxAnVplsVfiMacAddr_Type())
zxAnVplsVfiMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVplsVfiMacAddr.setStatus(_A)
class _ZxAnVplsVfiMacAddrConfLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_ZxAnVplsVfiMacAddrConfLocation_Type.__name__=_C
_ZxAnVplsVfiMacAddrConfLocation_Object=MibTableColumn
zxAnVplsVfiMacAddrConfLocation=_ZxAnVplsVfiMacAddrConfLocation_Object((1,3,6,1,4,1,3902,1015,59,3,14,1,3),_ZxAnVplsVfiMacAddrConfLocation_Type())
zxAnVplsVfiMacAddrConfLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiMacAddrConfLocation.setStatus(_A)
_ZxAnVplsVfiMacL3IfVlanIndex_Type=ZxAnIfindex
_ZxAnVplsVfiMacL3IfVlanIndex_Object=MibTableColumn
zxAnVplsVfiMacL3IfVlanIndex=_ZxAnVplsVfiMacL3IfVlanIndex_Object((1,3,6,1,4,1,3902,1015,59,3,14,1,4),_ZxAnVplsVfiMacL3IfVlanIndex_Type())
zxAnVplsVfiMacL3IfVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiMacL3IfVlanIndex.setStatus(_A)
class _ZxAnVplsVfiMacPeerIpAddrType_Type(InetAddressType):defaultValue=1
_ZxAnVplsVfiMacPeerIpAddrType_Type.__name__=_G
_ZxAnVplsVfiMacPeerIpAddrType_Object=MibTableColumn
zxAnVplsVfiMacPeerIpAddrType=_ZxAnVplsVfiMacPeerIpAddrType_Object((1,3,6,1,4,1,3902,1015,59,3,14,1,5),_ZxAnVplsVfiMacPeerIpAddrType_Type())
zxAnVplsVfiMacPeerIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiMacPeerIpAddrType.setStatus(_A)
_ZxAnVplsVfiMacPeerIpAddr_Type=InetAddress
_ZxAnVplsVfiMacPeerIpAddr_Object=MibTableColumn
zxAnVplsVfiMacPeerIpAddr=_ZxAnVplsVfiMacPeerIpAddr_Object((1,3,6,1,4,1,3902,1015,59,3,14,1,6),_ZxAnVplsVfiMacPeerIpAddr_Type())
zxAnVplsVfiMacPeerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiMacPeerIpAddr.setStatus(_A)
class _ZxAnVplsVfiMacInnerOutgoingLabel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1048575))
_ZxAnVplsVfiMacInnerOutgoingLabel_Type.__name__=_C
_ZxAnVplsVfiMacInnerOutgoingLabel_Object=MibTableColumn
zxAnVplsVfiMacInnerOutgoingLabel=_ZxAnVplsVfiMacInnerOutgoingLabel_Object((1,3,6,1,4,1,3902,1015,59,3,14,1,7),_ZxAnVplsVfiMacInnerOutgoingLabel_Type())
zxAnVplsVfiMacInnerOutgoingLabel.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnVplsVfiMacInnerOutgoingLabel.setStatus(_A)
class _ZxAnVplsVfiMacOuterOutgoingLabel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1048575))
_ZxAnVplsVfiMacOuterOutgoingLabel_Type.__name__=_C
_ZxAnVplsVfiMacOuterOutgoingLabel_Object=MibTableColumn
zxAnVplsVfiMacOuterOutgoingLabel=_ZxAnVplsVfiMacOuterOutgoingLabel_Object((1,3,6,1,4,1,3902,1015,59,3,14,1,8),_ZxAnVplsVfiMacOuterOutgoingLabel_Type())
zxAnVplsVfiMacOuterOutgoingLabel.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnVplsVfiMacOuterOutgoingLabel.setStatus(_A)
_ZxAnVplsVfiMacRowStatus_Type=RowStatus
_ZxAnVplsVfiMacRowStatus_Object=MibTableColumn
zxAnVplsVfiMacRowStatus=_ZxAnVplsVfiMacRowStatus_Object((1,3,6,1,4,1,3902,1015,59,3,14,1,30),_ZxAnVplsVfiMacRowStatus_Type())
zxAnVplsVfiMacRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVplsVfiMacRowStatus.setStatus(_A)
_ZxAnTdmRelayObjects_ObjectIdentity=ObjectIdentity
zxAnTdmRelayObjects=_ZxAnTdmRelayObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,59,4))
_ZxAnTRPwTable_Object=MibTable
zxAnTRPwTable=_ZxAnTRPwTable_Object((1,3,6,1,4,1,3902,1015,59,4,11))
if mibBuilder.loadTexts:zxAnTRPwTable.setStatus(_A)
_ZxAnTRPwEntry_Object=MibTableRow
zxAnTRPwEntry=_ZxAnTRPwEntry_Object((1,3,6,1,4,1,3902,1015,59,4,11,1))
zxAnTRPwEntry.setIndexNames((0,_D,_d))
if mibBuilder.loadTexts:zxAnTRPwEntry.setStatus(_A)
_ZxAnTRPwIndex_Type=PwIndexType
_ZxAnTRPwIndex_Object=MibTableColumn
zxAnTRPwIndex=_ZxAnTRPwIndex_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,1),_ZxAnTRPwIndex_Type())
zxAnTRPwIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnTRPwIndex.setStatus(_A)
_ZxAnTRPwType_Type=IANAPwTypeTC
_ZxAnTRPwType_Object=MibTableColumn
zxAnTRPwType=_ZxAnTRPwType_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,2),_ZxAnTRPwType_Type())
zxAnTRPwType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwType.setStatus(_A)
_ZxAnTRPwPsnType_Type=IANAPwPsnTypeTC
_ZxAnTRPwPsnType_Object=MibTableColumn
zxAnTRPwPsnType=_ZxAnTRPwPsnType_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,3),_ZxAnTRPwPsnType_Type())
zxAnTRPwPsnType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwPsnType.setStatus(_A)
_ZxAnTRPwPeerIpAddrType_Type=InetAddressType
_ZxAnTRPwPeerIpAddrType_Object=MibTableColumn
zxAnTRPwPeerIpAddrType=_ZxAnTRPwPeerIpAddrType_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,4),_ZxAnTRPwPeerIpAddrType_Type())
zxAnTRPwPeerIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwPeerIpAddrType.setStatus(_A)
_ZxAnTRPwPeerIpAddr_Type=InetAddress
_ZxAnTRPwPeerIpAddr_Object=MibTableColumn
zxAnTRPwPeerIpAddr=_ZxAnTRPwPeerIpAddr_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,5),_ZxAnTRPwPeerIpAddr_Type())
zxAnTRPwPeerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwPeerIpAddr.setStatus(_A)
_ZxAnTRPwPeerVcId_Type=Unsigned32
_ZxAnTRPwPeerVcId_Object=MibTableColumn
zxAnTRPwPeerVcId=_ZxAnTRPwPeerVcId_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,6),_ZxAnTRPwPeerVcId_Type())
zxAnTRPwPeerVcId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwPeerVcId.setStatus(_A)
_ZxAnTRPwStandbyPeerIpAddrType_Type=InetAddressType
_ZxAnTRPwStandbyPeerIpAddrType_Object=MibTableColumn
zxAnTRPwStandbyPeerIpAddrType=_ZxAnTRPwStandbyPeerIpAddrType_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,7),_ZxAnTRPwStandbyPeerIpAddrType_Type())
zxAnTRPwStandbyPeerIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwStandbyPeerIpAddrType.setStatus(_A)
_ZxAnTRPwStandbyPeerIpAddr_Type=InetAddress
_ZxAnTRPwStandbyPeerIpAddr_Object=MibTableColumn
zxAnTRPwStandbyPeerIpAddr=_ZxAnTRPwStandbyPeerIpAddr_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,8),_ZxAnTRPwStandbyPeerIpAddr_Type())
zxAnTRPwStandbyPeerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwStandbyPeerIpAddr.setStatus(_A)
_ZxAnTRPwStandbyPeerVcId_Type=Unsigned32
_ZxAnTRPwStandbyPeerVcId_Object=MibTableColumn
zxAnTRPwStandbyPeerVcId=_ZxAnTRPwStandbyPeerVcId_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,9),_ZxAnTRPwStandbyPeerVcId_Type())
zxAnTRPwStandbyPeerVcId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwStandbyPeerVcId.setStatus(_A)
_ZxAnTRPwOutboundLabel_Type=Unsigned32
_ZxAnTRPwOutboundLabel_Object=MibTableColumn
zxAnTRPwOutboundLabel=_ZxAnTRPwOutboundLabel_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,10),_ZxAnTRPwOutboundLabel_Type())
zxAnTRPwOutboundLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwOutboundLabel.setStatus(_A)
_ZxAnTRPwInboundLabel_Type=Unsigned32
_ZxAnTRPwInboundLabel_Object=MibTableColumn
zxAnTRPwInboundLabel=_ZxAnTRPwInboundLabel_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,11),_ZxAnTRPwInboundLabel_Type())
zxAnTRPwInboundLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwInboundLabel.setStatus(_A)
_ZxAnTRPwOutboundTunnelLabel_Type=Unsigned32
_ZxAnTRPwOutboundTunnelLabel_Object=MibTableColumn
zxAnTRPwOutboundTunnelLabel=_ZxAnTRPwOutboundTunnelLabel_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,12),_ZxAnTRPwOutboundTunnelLabel_Type())
zxAnTRPwOutboundTunnelLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwOutboundTunnelLabel.setStatus(_A)
_ZxAnTRPwInboundTunnelLabel_Type=Unsigned32
_ZxAnTRPwInboundTunnelLabel_Object=MibTableColumn
zxAnTRPwInboundTunnelLabel=_ZxAnTRPwInboundTunnelLabel_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,13),_ZxAnTRPwInboundTunnelLabel_Type())
zxAnTRPwInboundTunnelLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwInboundTunnelLabel.setStatus(_A)
_ZxAnTRPwPayloadSize_Type=Unsigned32
_ZxAnTRPwPayloadSize_Object=MibTableColumn
zxAnTRPwPayloadSize=_ZxAnTRPwPayloadSize_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,14),_ZxAnTRPwPayloadSize_Type())
zxAnTRPwPayloadSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwPayloadSize.setStatus(_A)
if mibBuilder.loadTexts:zxAnTRPwPayloadSize.setUnits('bytes')
_ZxAnTRPwDstMac_Type=MacAddress
_ZxAnTRPwDstMac_Object=MibTableColumn
zxAnTRPwDstMac=_ZxAnTRPwDstMac_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,15),_ZxAnTRPwDstMac_Type())
zxAnTRPwDstMac.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwDstMac.setStatus(_A)
class _ZxAnTRPwVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnTRPwVlanId_Type.__name__=_F
_ZxAnTRPwVlanId_Object=MibTableColumn
zxAnTRPwVlanId=_ZxAnTRPwVlanId_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,16),_ZxAnTRPwVlanId_Type())
zxAnTRPwVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwVlanId.setStatus(_A)
class _ZxAnTRPwPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnTRPwPrio_Type.__name__=_C
_ZxAnTRPwPrio_Object=MibTableColumn
zxAnTRPwPrio=_ZxAnTRPwPrio_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,17),_ZxAnTRPwPrio_Type())
zxAnTRPwPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwPrio.setStatus(_A)
_ZxAnTRPwRowStatus_Type=RowStatus
_ZxAnTRPwRowStatus_Object=MibTableColumn
zxAnTRPwRowStatus=_ZxAnTRPwRowStatus_Object((1,3,6,1,4,1,3902,1015,59,4,11,1,30),_ZxAnTRPwRowStatus_Type())
zxAnTRPwRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnTRPwRowStatus.setStatus(_A)
_ZxAnTRTdmSrcMacTable_Object=MibTable
zxAnTRTdmSrcMacTable=_ZxAnTRTdmSrcMacTable_Object((1,3,6,1,4,1,3902,1015,59,4,12))
if mibBuilder.loadTexts:zxAnTRTdmSrcMacTable.setStatus(_A)
_ZxAnTRTdmSrcMacEntry_Object=MibTableRow
zxAnTRTdmSrcMacEntry=_ZxAnTRTdmSrcMacEntry_Object((1,3,6,1,4,1,3902,1015,59,4,12,1))
zxAnTRTdmSrcMacEntry.setIndexNames((0,_D,_e),(0,_D,_f),(0,_D,_g))
if mibBuilder.loadTexts:zxAnTRTdmSrcMacEntry.setStatus(_A)
_ZxAnTRTdmSrcRackNo_Type=Integer32
_ZxAnTRTdmSrcRackNo_Object=MibTableColumn
zxAnTRTdmSrcRackNo=_ZxAnTRTdmSrcRackNo_Object((1,3,6,1,4,1,3902,1015,59,4,12,1,1),_ZxAnTRTdmSrcRackNo_Type())
zxAnTRTdmSrcRackNo.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnTRTdmSrcRackNo.setStatus(_A)
_ZxAnTRTdmSrcShelfNo_Type=Integer32
_ZxAnTRTdmSrcShelfNo_Object=MibTableColumn
zxAnTRTdmSrcShelfNo=_ZxAnTRTdmSrcShelfNo_Object((1,3,6,1,4,1,3902,1015,59,4,12,1,2),_ZxAnTRTdmSrcShelfNo_Type())
zxAnTRTdmSrcShelfNo.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnTRTdmSrcShelfNo.setStatus(_A)
_ZxAnTRTdmSrcSlotNo_Type=Integer32
_ZxAnTRTdmSrcSlotNo_Object=MibTableColumn
zxAnTRTdmSrcSlotNo=_ZxAnTRTdmSrcSlotNo_Object((1,3,6,1,4,1,3902,1015,59,4,12,1,3),_ZxAnTRTdmSrcSlotNo_Type())
zxAnTRTdmSrcSlotNo.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnTRTdmSrcSlotNo.setStatus(_A)
_ZxAnTRTdmSrcMac_Type=MacAddress
_ZxAnTRTdmSrcMac_Object=MibTableColumn
zxAnTRTdmSrcMac=_ZxAnTRTdmSrcMac_Object((1,3,6,1,4,1,3902,1015,59,4,12,1,4),_ZxAnTRTdmSrcMac_Type())
zxAnTRTdmSrcMac.setMaxAccess('read-write')
if mibBuilder.loadTexts:zxAnTRTdmSrcMac.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ZxAnMplsVccvCcType':ZxAnMplsVccvCcType,'ZxAnMplsVccvCvType':ZxAnMplsVccvCvType,'zxAnMplsL2vpnMib':zxAnMplsL2vpnMib,'zxAnL2vpnGlobalObjects':zxAnL2vpnGlobalObjects,'zxAnMplsStaticPwTable':zxAnMplsStaticPwTable,'zxAnMplsStaticPwEntry':zxAnMplsStaticPwEntry,_R:zxAnMplsStaticPwName,'zxAnMplsOutgoingPwLabel':zxAnMplsOutgoingPwLabel,'zxAnMplsIncomingPwLabel':zxAnMplsIncomingPwLabel,'zxAnMplsStaticPwRowStatus':zxAnMplsStaticPwRowStatus,'zxAnVpwsObjects':zxAnVpwsObjects,'zxAnVpwsTable':zxAnVpwsTable,'zxAnVpwsEntry':zxAnVpwsEntry,_S:zxAnVpwsL3IfIndex,'zxAnVpwsPeerIpAddrType':zxAnVpwsPeerIpAddrType,'zxAnVpwsPeerIpAddr':zxAnVpwsPeerIpAddr,'zxAnVpwsVcId':zxAnVpwsVcId,'zxAnVpwsPwType':zxAnVpwsPwType,'zxAnVpwsStaticPwName':zxAnVpwsStaticPwName,'zxAnVpwsStandbyPeerIpAddrType':zxAnVpwsStandbyPeerIpAddrType,'zxAnVpwsStandbyPeerIpAddr':zxAnVpwsStandbyPeerIpAddr,'zxAnVpwsStandbyVcId':zxAnVpwsStandbyVcId,'zxAnVpwsPwe3CWPreferred':zxAnVpwsPwe3CWPreferred,'zxAnVpwsVccvEnable':zxAnVpwsVccvEnable,'zxAnVpwsCcTypeCapability':zxAnVpwsCcTypeCapability,'zxAnVpwsCvTypeCapability':zxAnVpwsCvTypeCapability,'zxAnVpwsRowStatus':zxAnVpwsRowStatus,'zxAnVplsObjects':zxAnVplsObjects,'zxAnVplsVfiConfigTable':zxAnVplsVfiConfigTable,'zxAnVplsVfiConfigEntry':zxAnVplsVfiConfigEntry,_J:zxAnVplsVfiName,'zxAnVplsVfiVcid':zxAnVplsVfiVcid,'zxAnVplsVfiPwType':zxAnVplsVfiPwType,'zxAnVplsVfiMaxMacLearningNum':zxAnVplsVfiMaxMacLearningNum,'zxAnVplsVfiRemoteMacAgingTime':zxAnVplsVfiRemoteMacAgingTime,'zxAnVplsVfiLocalMacAgingTime':zxAnVplsVfiLocalMacAgingTime,'zxAnVplsVfiBCastRateLimit':zxAnVplsVfiBCastRateLimit,'zxAnVplsVfiMCastRateLimit':zxAnVplsVfiMCastRateLimit,'zxAnVplsVfiUnknownUCastRateLimit':zxAnVplsVfiUnknownUCastRateLimit,'zxAnVplsVfiVcidType':zxAnVplsVfiVcidType,'zxAnVplsVfiPwe3CWPreferred':zxAnVplsVfiPwe3CWPreferred,'zxAnVplsVfiVccvEnable':zxAnVplsVfiVccvEnable,'zxAnVplsVfiCcTypeCapability':zxAnVplsVfiCcTypeCapability,'zxAnVplsVfiCvTypeCapability':zxAnVplsVfiCvTypeCapability,'zxAnVplsVfiRowStatus':zxAnVplsVfiRowStatus,'zxAnVplsVfiPeerIpAddrTable':zxAnVplsVfiPeerIpAddrTable,'zxAnVplsVfiPeerIpAddrEntry':zxAnVplsVfiPeerIpAddrEntry,_Y:zxAnVplsVfiPeerIpAddrType,_Z:zxAnVplsVfiPeerIpAddr,'zxAnVplsVfiStandbyPeerIpAddrType':zxAnVplsVfiStandbyPeerIpAddrType,'zxAnVplsVfiStandbyPeerIpAddr':zxAnVplsVfiStandbyPeerIpAddr,'zxAnVplsVfiStaticPwName':zxAnVplsVfiStaticPwName,'zxAnVplsVfiPwNetType':zxAnVplsVfiPwNetType,'zxAnVplsVfiPeerRowStatus':zxAnVplsVfiPeerRowStatus,'zxAnL3IfVfiConfigTable':zxAnL3IfVfiConfigTable,'zxAnL3IfVfiConfigEntry':zxAnL3IfVfiConfigEntry,_a:zxAnL3IfVfiIfIndex,'zxAnL3IfVfiName':zxAnL3IfVfiName,'zxAnL3IfVfiRowStatus':zxAnL3IfVfiRowStatus,'zxAnVplsVfiMacTable':zxAnVplsVfiMacTable,'zxAnVplsVfiMacEntry':zxAnVplsVfiMacEntry,_b:zxAnVplsVfiMacAddrType,_c:zxAnVplsVfiMacAddr,'zxAnVplsVfiMacAddrConfLocation':zxAnVplsVfiMacAddrConfLocation,'zxAnVplsVfiMacL3IfVlanIndex':zxAnVplsVfiMacL3IfVlanIndex,'zxAnVplsVfiMacPeerIpAddrType':zxAnVplsVfiMacPeerIpAddrType,'zxAnVplsVfiMacPeerIpAddr':zxAnVplsVfiMacPeerIpAddr,'zxAnVplsVfiMacInnerOutgoingLabel':zxAnVplsVfiMacInnerOutgoingLabel,'zxAnVplsVfiMacOuterOutgoingLabel':zxAnVplsVfiMacOuterOutgoingLabel,'zxAnVplsVfiMacRowStatus':zxAnVplsVfiMacRowStatus,'zxAnTdmRelayObjects':zxAnTdmRelayObjects,'zxAnTRPwTable':zxAnTRPwTable,'zxAnTRPwEntry':zxAnTRPwEntry,_d:zxAnTRPwIndex,'zxAnTRPwType':zxAnTRPwType,'zxAnTRPwPsnType':zxAnTRPwPsnType,'zxAnTRPwPeerIpAddrType':zxAnTRPwPeerIpAddrType,'zxAnTRPwPeerIpAddr':zxAnTRPwPeerIpAddr,'zxAnTRPwPeerVcId':zxAnTRPwPeerVcId,'zxAnTRPwStandbyPeerIpAddrType':zxAnTRPwStandbyPeerIpAddrType,'zxAnTRPwStandbyPeerIpAddr':zxAnTRPwStandbyPeerIpAddr,'zxAnTRPwStandbyPeerVcId':zxAnTRPwStandbyPeerVcId,'zxAnTRPwOutboundLabel':zxAnTRPwOutboundLabel,'zxAnTRPwInboundLabel':zxAnTRPwInboundLabel,'zxAnTRPwOutboundTunnelLabel':zxAnTRPwOutboundTunnelLabel,'zxAnTRPwInboundTunnelLabel':zxAnTRPwInboundTunnelLabel,'zxAnTRPwPayloadSize':zxAnTRPwPayloadSize,'zxAnTRPwDstMac':zxAnTRPwDstMac,'zxAnTRPwVlanId':zxAnTRPwVlanId,'zxAnTRPwPrio':zxAnTRPwPrio,'zxAnTRPwRowStatus':zxAnTRPwRowStatus,'zxAnTRTdmSrcMacTable':zxAnTRTdmSrcMacTable,'zxAnTRTdmSrcMacEntry':zxAnTRTdmSrcMacEntry,_e:zxAnTRTdmSrcRackNo,_f:zxAnTRTdmSrcShelfNo,_g:zxAnTRTdmSrcSlotNo,'zxAnTRTdmSrcMac':zxAnTRTdmSrcMac})