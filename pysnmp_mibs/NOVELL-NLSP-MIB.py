_x='nlspLSPOptIndex'
_w='nlspLSPOptLSPID'
_v='nlspLSPOptSysInstance'
_u='nlspLSPID'
_t='nlspLSPSysInstance'
_s='nlspGraphServTypeValue'
_r='nlspGraphServName'
_q='nlspGraphServNLSPID'
_p='nlspGraphServSysInstance'
_o='nlspGraphXRouteNetNum'
_n='nlspGraphXRouteNLSPID'
_m='nlspGraphXRouteSysInstance'
_l='nlspPathLinkIndex'
_k='nlspPathDestNLSPID'
_j='nlspPathSysInstance'
_i='nlspLinkIndex'
_h='nlspLinkNLSPID'
_g='nlspLinkSysInstance'
_f='nlspNodeID'
_e='nlspNodeSysInstance'
_d='nlspNameMapServerName'
_c='nlspNameMapSysInstance'
_b='nlspNetMapNetNum'
_a='nlspNetMapSysInstance'
_Z='nlspIDMapID'
_Y='nlspIDMapSysInstance'
_X='nlspNeighIndex'
_W='nlspNeighCircIndex'
_V='nlspNeighSysInstance'
_U='nlspDestNetNum'
_T='nlspDestSysInstance'
_S='nlspCircIndex'
_R='nlspCircSysInstance'
_Q='nlspActAreaMask'
_P='nlspActAreaNet'
_O='nlspActAreaSysInstance'
_N='nlspSysAreaMask'
_M='nlspSysAreaNet'
_L='nlspSysAreaSysInstance'
_K='nlspSysInstance'
_J='unknown'
_I='nlspLevel1Router'
_H='yes'
_G='no'
_F='OctetString'
_E='read-write'
_D='Integer32'
_C='NOVELL-NLSP-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mibDoc,=mibBuilder.importSymbols('NOVELL-IPX-MIB','mibDoc')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class SystemID(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class NLSPID(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
class NetNumber(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_Nlsp_ObjectIdentity=ObjectIdentity
nlsp=_Nlsp_ObjectIdentity((1,3,6,1,4,1,23,2,19))
_NlspSystem_ObjectIdentity=ObjectIdentity
nlspSystem=_NlspSystem_ObjectIdentity((1,3,6,1,4,1,23,2,19,1))
_NlspSysTable_Object=MibTable
nlspSysTable=_NlspSysTable_Object((1,3,6,1,4,1,23,2,19,1,1))
if mibBuilder.loadTexts:nlspSysTable.setStatus(_A)
_NlspSysEntry_Object=MibTableRow
nlspSysEntry=_NlspSysEntry_Object((1,3,6,1,4,1,23,2,19,1,1,1))
nlspSysEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:nlspSysEntry.setStatus(_A)
_NlspSysInstance_Type=Integer32
_NlspSysInstance_Object=MibTableColumn
nlspSysInstance=_NlspSysInstance_Object((1,3,6,1,4,1,23,2,19,1,1,1,1),_NlspSysInstance_Type())
nlspSysInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysInstance.setStatus(_A)
class _NlspSysState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),(_I,2)))
_NlspSysState_Type.__name__=_D
_NlspSysState_Object=MibTableColumn
nlspSysState=_NlspSysState_Object((1,3,6,1,4,1,23,2,19,1,1,1,2),_NlspSysState_Type())
nlspSysState.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysState.setStatus(_A)
_NlspSysID_Type=SystemID
_NlspSysID_Object=MibTableColumn
nlspSysID=_NlspSysID_Object((1,3,6,1,4,1,23,2,19,1,1,1,3),_NlspSysID_Type())
nlspSysID.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysID.setStatus(_A)
class _NlspSysMinNonBcastLSPTransInt_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_NlspSysMinNonBcastLSPTransInt_Type.__name__=_D
_NlspSysMinNonBcastLSPTransInt_Object=MibTableColumn
nlspSysMinNonBcastLSPTransInt=_NlspSysMinNonBcastLSPTransInt_Object((1,3,6,1,4,1,23,2,19,1,1,1,4),_NlspSysMinNonBcastLSPTransInt_Type())
nlspSysMinNonBcastLSPTransInt.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysMinNonBcastLSPTransInt.setStatus(_A)
class _NlspSysMinBcastLSPTransInt_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_NlspSysMinBcastLSPTransInt_Type.__name__=_D
_NlspSysMinBcastLSPTransInt_Object=MibTableColumn
nlspSysMinBcastLSPTransInt=_NlspSysMinBcastLSPTransInt_Object((1,3,6,1,4,1,23,2,19,1,1,1,5),_NlspSysMinBcastLSPTransInt_Type())
nlspSysMinBcastLSPTransInt.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysMinBcastLSPTransInt.setStatus(_A)
class _NlspSysMinLSPGenInt_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_NlspSysMinLSPGenInt_Type.__name__=_D
_NlspSysMinLSPGenInt_Object=MibTableColumn
nlspSysMinLSPGenInt=_NlspSysMinLSPGenInt_Object((1,3,6,1,4,1,23,2,19,1,1,1,6),_NlspSysMinLSPGenInt_Type())
nlspSysMinLSPGenInt.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysMinLSPGenInt.setStatus(_A)
class _NlspSysMaxLSPGenInt_Type(Integer32):defaultValue=7200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50000))
_NlspSysMaxLSPGenInt_Type.__name__=_D
_NlspSysMaxLSPGenInt_Object=MibTableColumn
nlspSysMaxLSPGenInt=_NlspSysMaxLSPGenInt_Object((1,3,6,1,4,1,23,2,19,1,1,1,7),_NlspSysMaxLSPGenInt_Type())
nlspSysMaxLSPGenInt.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysMaxLSPGenInt.setStatus(_A)
class _NlspSysMaxLSPAge_Type(Integer32):defaultValue=7500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50000))
_NlspSysMaxLSPAge_Type.__name__=_D
_NlspSysMaxLSPAge_Object=MibTableColumn
nlspSysMaxLSPAge=_NlspSysMaxLSPAge_Object((1,3,6,1,4,1,23,2,19,1,1,1,8),_NlspSysMaxLSPAge_Type())
nlspSysMaxLSPAge.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysMaxLSPAge.setStatus(_A)
class _NlspSysBcastHelloInt_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NlspSysBcastHelloInt_Type.__name__=_D
_NlspSysBcastHelloInt_Object=MibTableColumn
nlspSysBcastHelloInt=_NlspSysBcastHelloInt_Object((1,3,6,1,4,1,23,2,19,1,1,1,9),_NlspSysBcastHelloInt_Type())
nlspSysBcastHelloInt.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysBcastHelloInt.setStatus(_A)
class _NlspSysNonBcastHelloInt_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NlspSysNonBcastHelloInt_Type.__name__=_D
_NlspSysNonBcastHelloInt_Object=MibTableColumn
nlspSysNonBcastHelloInt=_NlspSysNonBcastHelloInt_Object((1,3,6,1,4,1,23,2,19,1,1,1,10),_NlspSysNonBcastHelloInt_Type())
nlspSysNonBcastHelloInt.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysNonBcastHelloInt.setStatus(_A)
class _NlspSysDRBcastHelloInt_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NlspSysDRBcastHelloInt_Type.__name__=_D
_NlspSysDRBcastHelloInt_Object=MibTableColumn
nlspSysDRBcastHelloInt=_NlspSysDRBcastHelloInt_Object((1,3,6,1,4,1,23,2,19,1,1,1,11),_NlspSysDRBcastHelloInt_Type())
nlspSysDRBcastHelloInt.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysDRBcastHelloInt.setStatus(_A)
class _NlspSysHoldTimeMultiplier_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,20))
_NlspSysHoldTimeMultiplier_Type.__name__=_D
_NlspSysHoldTimeMultiplier_Object=MibTableColumn
nlspSysHoldTimeMultiplier=_NlspSysHoldTimeMultiplier_Object((1,3,6,1,4,1,23,2,19,1,1,1,12),_NlspSysHoldTimeMultiplier_Type())
nlspSysHoldTimeMultiplier.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysHoldTimeMultiplier.setStatus(_A)
class _NlspSysCompSNPInt_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_NlspSysCompSNPInt_Type.__name__=_D
_NlspSysCompSNPInt_Object=MibTableColumn
nlspSysCompSNPInt=_NlspSysCompSNPInt_Object((1,3,6,1,4,1,23,2,19,1,1,1,13),_NlspSysCompSNPInt_Type())
nlspSysCompSNPInt.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysCompSNPInt.setStatus(_A)
class _NlspSysPartSNPInt_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_NlspSysPartSNPInt_Type.__name__=_D
_NlspSysPartSNPInt_Object=MibTableColumn
nlspSysPartSNPInt=_NlspSysPartSNPInt_Object((1,3,6,1,4,1,23,2,19,1,1,1,14),_NlspSysPartSNPInt_Type())
nlspSysPartSNPInt.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysPartSNPInt.setStatus(_A)
class _NlspSysWaitTime_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_NlspSysWaitTime_Type.__name__=_D
_NlspSysWaitTime_Object=MibTableColumn
nlspSysWaitTime=_NlspSysWaitTime_Object((1,3,6,1,4,1,23,2,19,1,1,1,15),_NlspSysWaitTime_Type())
nlspSysWaitTime.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysWaitTime.setStatus(_A)
class _NlspSysOrigL1LSPBufSize_Type(Integer32):defaultValue=512;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,4096))
_NlspSysOrigL1LSPBufSize_Type.__name__=_D
_NlspSysOrigL1LSPBufSize_Object=MibTableColumn
nlspSysOrigL1LSPBufSize=_NlspSysOrigL1LSPBufSize_Object((1,3,6,1,4,1,23,2,19,1,1,1,16),_NlspSysOrigL1LSPBufSize_Type())
nlspSysOrigL1LSPBufSize.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysOrigL1LSPBufSize.setStatus(_A)
_NlspSysVersion_Type=Integer32
_NlspSysVersion_Object=MibTableColumn
nlspSysVersion=_NlspSysVersion_Object((1,3,6,1,4,1,23,2,19,1,1,1,17),_NlspSysVersion_Type())
nlspSysVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspSysVersion.setStatus(_A)
_NlspSysCorrLSPs_Type=Counter32
_NlspSysCorrLSPs_Object=MibTableColumn
nlspSysCorrLSPs=_NlspSysCorrLSPs_Object((1,3,6,1,4,1,23,2,19,1,1,1,18),_NlspSysCorrLSPs_Type())
nlspSysCorrLSPs.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspSysCorrLSPs.setStatus(_A)
class _NlspSysL1Overloaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NlspSysL1Overloaded_Type.__name__=_D
_NlspSysL1Overloaded_Object=MibTableColumn
nlspSysL1Overloaded=_NlspSysL1Overloaded_Object((1,3,6,1,4,1,23,2,19,1,1,1,19),_NlspSysL1Overloaded_Type())
nlspSysL1Overloaded.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspSysL1Overloaded.setStatus(_A)
_NlspSysL1DbaseOverloads_Type=Counter32
_NlspSysL1DbaseOverloads_Object=MibTableColumn
nlspSysL1DbaseOverloads=_NlspSysL1DbaseOverloads_Object((1,3,6,1,4,1,23,2,19,1,1,1,20),_NlspSysL1DbaseOverloads_Type())
nlspSysL1DbaseOverloads.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspSysL1DbaseOverloads.setStatus(_A)
_NlspSysMaxSeqNums_Type=Counter32
_NlspSysMaxSeqNums_Object=MibTableColumn
nlspSysMaxSeqNums=_NlspSysMaxSeqNums_Object((1,3,6,1,4,1,23,2,19,1,1,1,21),_NlspSysMaxSeqNums_Type())
nlspSysMaxSeqNums.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspSysMaxSeqNums.setStatus(_A)
_NlspSysSeqNumSkips_Type=Counter32
_NlspSysSeqNumSkips_Object=MibTableColumn
nlspSysSeqNumSkips=_NlspSysSeqNumSkips_Object((1,3,6,1,4,1,23,2,19,1,1,1,22),_NlspSysSeqNumSkips_Type())
nlspSysSeqNumSkips.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspSysSeqNumSkips.setStatus(_A)
_NlspSysTransmittedLSPs_Type=Counter32
_NlspSysTransmittedLSPs_Object=MibTableColumn
nlspSysTransmittedLSPs=_NlspSysTransmittedLSPs_Object((1,3,6,1,4,1,23,2,19,1,1,1,23),_NlspSysTransmittedLSPs_Type())
nlspSysTransmittedLSPs.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspSysTransmittedLSPs.setStatus(_A)
_NlspSysReceivedLSPs_Type=Counter32
_NlspSysReceivedLSPs_Object=MibTableColumn
nlspSysReceivedLSPs=_NlspSysReceivedLSPs_Object((1,3,6,1,4,1,23,2,19,1,1,1,24),_NlspSysReceivedLSPs_Type())
nlspSysReceivedLSPs.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspSysReceivedLSPs.setStatus(_A)
_NlspSysOwnLSPPurges_Type=Counter32
_NlspSysOwnLSPPurges_Object=MibTableColumn
nlspSysOwnLSPPurges=_NlspSysOwnLSPPurges_Object((1,3,6,1,4,1,23,2,19,1,1,1,25),_NlspSysOwnLSPPurges_Type())
nlspSysOwnLSPPurges.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspSysOwnLSPPurges.setStatus(_A)
_NlspSysVersionErrors_Type=Counter32
_NlspSysVersionErrors_Object=MibTableColumn
nlspSysVersionErrors=_NlspSysVersionErrors_Object((1,3,6,1,4,1,23,2,19,1,1,1,26),_NlspSysVersionErrors_Type())
nlspSysVersionErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspSysVersionErrors.setStatus(_A)
_NlspSysIncorrectPackets_Type=Counter32
_NlspSysIncorrectPackets_Object=MibTableColumn
nlspSysIncorrectPackets=_NlspSysIncorrectPackets_Object((1,3,6,1,4,1,23,2,19,1,1,1,27),_NlspSysIncorrectPackets_Type())
nlspSysIncorrectPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspSysIncorrectPackets.setStatus(_A)
class _NlspSysNearestL2DefaultExists_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NlspSysNearestL2DefaultExists_Type.__name__=_D
_NlspSysNearestL2DefaultExists_Object=MibTableColumn
nlspSysNearestL2DefaultExists=_NlspSysNearestL2DefaultExists_Object((1,3,6,1,4,1,23,2,19,1,1,1,28),_NlspSysNearestL2DefaultExists_Type())
nlspSysNearestL2DefaultExists.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspSysNearestL2DefaultExists.setStatus(_A)
_NlspSysNearestL2DefaultRouter_Type=SystemID
_NlspSysNearestL2DefaultRouter_Object=MibTableColumn
nlspSysNearestL2DefaultRouter=_NlspSysNearestL2DefaultRouter_Object((1,3,6,1,4,1,23,2,19,1,1,1,29),_NlspSysNearestL2DefaultRouter_Type())
nlspSysNearestL2DefaultRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspSysNearestL2DefaultRouter.setStatus(_A)
_NlspSysResourceFailures_Type=Counter32
_NlspSysResourceFailures_Object=MibTableColumn
nlspSysResourceFailures=_NlspSysResourceFailures_Object((1,3,6,1,4,1,23,2,19,1,1,1,30),_NlspSysResourceFailures_Type())
nlspSysResourceFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspSysResourceFailures.setStatus(_A)
_NlspSysAreaTable_Object=MibTable
nlspSysAreaTable=_NlspSysAreaTable_Object((1,3,6,1,4,1,23,2,19,1,2))
if mibBuilder.loadTexts:nlspSysAreaTable.setStatus(_A)
_NlspSysAreaEntry_Object=MibTableRow
nlspSysAreaEntry=_NlspSysAreaEntry_Object((1,3,6,1,4,1,23,2,19,1,2,1))
nlspSysAreaEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:nlspSysAreaEntry.setStatus(_A)
_NlspSysAreaSysInstance_Type=Integer32
_NlspSysAreaSysInstance_Object=MibTableColumn
nlspSysAreaSysInstance=_NlspSysAreaSysInstance_Object((1,3,6,1,4,1,23,2,19,1,2,1,1),_NlspSysAreaSysInstance_Type())
nlspSysAreaSysInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysAreaSysInstance.setStatus(_A)
class _NlspSysAreaNet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_NlspSysAreaNet_Type.__name__=_F
_NlspSysAreaNet_Object=MibTableColumn
nlspSysAreaNet=_NlspSysAreaNet_Object((1,3,6,1,4,1,23,2,19,1,2,1,2),_NlspSysAreaNet_Type())
nlspSysAreaNet.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysAreaNet.setStatus(_A)
class _NlspSysAreaMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_NlspSysAreaMask_Type.__name__=_F
_NlspSysAreaMask_Object=MibTableColumn
nlspSysAreaMask=_NlspSysAreaMask_Object((1,3,6,1,4,1,23,2,19,1,2,1,3),_NlspSysAreaMask_Type())
nlspSysAreaMask.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspSysAreaMask.setStatus(_A)
_NlspActAreaTable_Object=MibTable
nlspActAreaTable=_NlspActAreaTable_Object((1,3,6,1,4,1,23,2,19,1,3))
if mibBuilder.loadTexts:nlspActAreaTable.setStatus(_A)
_NlspActAreaEntry_Object=MibTableRow
nlspActAreaEntry=_NlspActAreaEntry_Object((1,3,6,1,4,1,23,2,19,1,3,1))
nlspActAreaEntry.setIndexNames((0,_C,_O),(0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:nlspActAreaEntry.setStatus(_A)
_NlspActAreaSysInstance_Type=Integer32
_NlspActAreaSysInstance_Object=MibTableColumn
nlspActAreaSysInstance=_NlspActAreaSysInstance_Object((1,3,6,1,4,1,23,2,19,1,3,1,1),_NlspActAreaSysInstance_Type())
nlspActAreaSysInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspActAreaSysInstance.setStatus(_A)
class _NlspActAreaNet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_NlspActAreaNet_Type.__name__=_F
_NlspActAreaNet_Object=MibTableColumn
nlspActAreaNet=_NlspActAreaNet_Object((1,3,6,1,4,1,23,2,19,1,3,1,2),_NlspActAreaNet_Type())
nlspActAreaNet.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspActAreaNet.setStatus(_A)
class _NlspActAreaMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_NlspActAreaMask_Type.__name__=_F
_NlspActAreaMask_Object=MibTableColumn
nlspActAreaMask=_NlspActAreaMask_Object((1,3,6,1,4,1,23,2,19,1,3,1,3),_NlspActAreaMask_Type())
nlspActAreaMask.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspActAreaMask.setStatus(_A)
_NlspCircuit_ObjectIdentity=ObjectIdentity
nlspCircuit=_NlspCircuit_ObjectIdentity((1,3,6,1,4,1,23,2,19,2))
_NlspCircTable_Object=MibTable
nlspCircTable=_NlspCircTable_Object((1,3,6,1,4,1,23,2,19,2,1))
if mibBuilder.loadTexts:nlspCircTable.setStatus(_A)
_NlspCircEntry_Object=MibTableRow
nlspCircEntry=_NlspCircEntry_Object((1,3,6,1,4,1,23,2,19,2,1,1))
nlspCircEntry.setIndexNames((0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:nlspCircEntry.setStatus(_A)
_NlspCircSysInstance_Type=Integer32
_NlspCircSysInstance_Object=MibTableColumn
nlspCircSysInstance=_NlspCircSysInstance_Object((1,3,6,1,4,1,23,2,19,2,1,1,1),_NlspCircSysInstance_Type())
nlspCircSysInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspCircSysInstance.setStatus(_A)
_NlspCircIndex_Type=Integer32
_NlspCircIndex_Object=MibTableColumn
nlspCircIndex=_NlspCircIndex_Object((1,3,6,1,4,1,23,2,19,2,1,1,2),_NlspCircIndex_Type())
nlspCircIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspCircIndex.setStatus(_A)
class _NlspCircState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_NlspCircState_Type.__name__=_D
_NlspCircState_Object=MibTableColumn
nlspCircState=_NlspCircState_Object((1,3,6,1,4,1,23,2,19,2,1,1,3),_NlspCircState_Type())
nlspCircState.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspCircState.setStatus(_A)
_NlspCircPace_Type=Integer32
_NlspCircPace_Object=MibTableColumn
nlspCircPace=_NlspCircPace_Object((1,3,6,1,4,1,23,2,19,2,1,1,4),_NlspCircPace_Type())
nlspCircPace.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspCircPace.setStatus(_A)
class _NlspCircHelloTimer_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NlspCircHelloTimer_Type.__name__=_D
_NlspCircHelloTimer_Object=MibTableColumn
nlspCircHelloTimer=_NlspCircHelloTimer_Object((1,3,6,1,4,1,23,2,19,2,1,1,5),_NlspCircHelloTimer_Type())
nlspCircHelloTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspCircHelloTimer.setStatus(_A)
class _NlspCircL1DefaultCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_NlspCircL1DefaultCost_Type.__name__=_D
_NlspCircL1DefaultCost_Object=MibTableColumn
nlspCircL1DefaultCost=_NlspCircL1DefaultCost_Object((1,3,6,1,4,1,23,2,19,2,1,1,6),_NlspCircL1DefaultCost_Type())
nlspCircL1DefaultCost.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspCircL1DefaultCost.setStatus(_A)
class _NlspCircL1DesRouterPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_NlspCircL1DesRouterPriority_Type.__name__=_D
_NlspCircL1DesRouterPriority_Object=MibTableColumn
nlspCircL1DesRouterPriority=_NlspCircL1DesRouterPriority_Object((1,3,6,1,4,1,23,2,19,2,1,1,7),_NlspCircL1DesRouterPriority_Type())
nlspCircL1DesRouterPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:nlspCircL1DesRouterPriority.setStatus(_A)
class _NlspCircL1CircID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_NlspCircL1CircID_Type.__name__=_F
_NlspCircL1CircID_Object=MibTableColumn
nlspCircL1CircID=_NlspCircL1CircID_Object((1,3,6,1,4,1,23,2,19,2,1,1,8),_NlspCircL1CircID_Type())
nlspCircL1CircID.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspCircL1CircID.setStatus(_A)
_NlspCircL1DesRouter_Type=SystemID
_NlspCircL1DesRouter_Object=MibTableColumn
nlspCircL1DesRouter=_NlspCircL1DesRouter_Object((1,3,6,1,4,1,23,2,19,2,1,1,9),_NlspCircL1DesRouter_Type())
nlspCircL1DesRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspCircL1DesRouter.setStatus(_A)
_NlspCircLANL1DesRouterChanges_Type=Counter32
_NlspCircLANL1DesRouterChanges_Object=MibTableColumn
nlspCircLANL1DesRouterChanges=_NlspCircLANL1DesRouterChanges_Object((1,3,6,1,4,1,23,2,19,2,1,1,10),_NlspCircLANL1DesRouterChanges_Type())
nlspCircLANL1DesRouterChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspCircLANL1DesRouterChanges.setStatus(_A)
_NlspCircNeighChanges_Type=Counter32
_NlspCircNeighChanges_Object=MibTableColumn
nlspCircNeighChanges=_NlspCircNeighChanges_Object((1,3,6,1,4,1,23,2,19,2,1,1,11),_NlspCircNeighChanges_Type())
nlspCircNeighChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspCircNeighChanges.setStatus(_A)
_NlspCircRejNeighbors_Type=Counter32
_NlspCircRejNeighbors_Object=MibTableColumn
nlspCircRejNeighbors=_NlspCircRejNeighbors_Object((1,3,6,1,4,1,23,2,19,2,1,1,12),_NlspCircRejNeighbors_Type())
nlspCircRejNeighbors.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspCircRejNeighbors.setStatus(_A)
_NlspCircOutPackets_Type=Counter32
_NlspCircOutPackets_Object=MibTableColumn
nlspCircOutPackets=_NlspCircOutPackets_Object((1,3,6,1,4,1,23,2,19,2,1,1,13),_NlspCircOutPackets_Type())
nlspCircOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspCircOutPackets.setStatus(_A)
_NlspCircInPackets_Type=Counter32
_NlspCircInPackets_Object=MibTableColumn
nlspCircInPackets=_NlspCircInPackets_Object((1,3,6,1,4,1,23,2,19,2,1,1,14),_NlspCircInPackets_Type())
nlspCircInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspCircInPackets.setStatus(_A)
_NlspCircActualMaxPacketSize_Type=Integer32
_NlspCircActualMaxPacketSize_Object=MibTableColumn
nlspCircActualMaxPacketSize=_NlspCircActualMaxPacketSize_Object((1,3,6,1,4,1,23,2,19,2,1,1,15),_NlspCircActualMaxPacketSize_Type())
nlspCircActualMaxPacketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspCircActualMaxPacketSize.setStatus(_A)
_NlspCircPSNPsSent_Type=Counter32
_NlspCircPSNPsSent_Object=MibTableColumn
nlspCircPSNPsSent=_NlspCircPSNPsSent_Object((1,3,6,1,4,1,23,2,19,2,1,1,16),_NlspCircPSNPsSent_Type())
nlspCircPSNPsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspCircPSNPsSent.setStatus(_A)
_NlspCircPSNPsReceived_Type=Counter32
_NlspCircPSNPsReceived_Object=MibTableColumn
nlspCircPSNPsReceived=_NlspCircPSNPsReceived_Object((1,3,6,1,4,1,23,2,19,2,1,1,17),_NlspCircPSNPsReceived_Type())
nlspCircPSNPsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspCircPSNPsReceived.setStatus(_A)
_NlspForwarding_ObjectIdentity=ObjectIdentity
nlspForwarding=_NlspForwarding_ObjectIdentity((1,3,6,1,4,1,23,2,19,3))
_NlspDestTable_Object=MibTable
nlspDestTable=_NlspDestTable_Object((1,3,6,1,4,1,23,2,19,3,1))
if mibBuilder.loadTexts:nlspDestTable.setStatus(_A)
_NlspDestEntry_Object=MibTableRow
nlspDestEntry=_NlspDestEntry_Object((1,3,6,1,4,1,23,2,19,3,1,1))
nlspDestEntry.setIndexNames((0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:nlspDestEntry.setStatus(_A)
_NlspDestSysInstance_Type=Integer32
_NlspDestSysInstance_Object=MibTableColumn
nlspDestSysInstance=_NlspDestSysInstance_Object((1,3,6,1,4,1,23,2,19,3,1,1,1),_NlspDestSysInstance_Type())
nlspDestSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspDestSysInstance.setStatus(_A)
_NlspDestNetNum_Type=NetNumber
_NlspDestNetNum_Object=MibTableColumn
nlspDestNetNum=_NlspDestNetNum_Object((1,3,6,1,4,1,23,2,19,3,1,1,2),_NlspDestNetNum_Type())
nlspDestNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspDestNetNum.setStatus(_A)
_NlspDestID_Type=NLSPID
_NlspDestID_Object=MibTableColumn
nlspDestID=_NlspDestID_Object((1,3,6,1,4,1,23,2,19,3,1,1,3),_NlspDestID_Type())
nlspDestID.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspDestID.setStatus(_A)
_NlspDestEstDelay_Type=Integer32
_NlspDestEstDelay_Object=MibTableColumn
nlspDestEstDelay=_NlspDestEstDelay_Object((1,3,6,1,4,1,23,2,19,3,1,1,4),_NlspDestEstDelay_Type())
nlspDestEstDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspDestEstDelay.setStatus(_A)
_NlspDestEstThroughput_Type=Integer32
_NlspDestEstThroughput_Object=MibTableColumn
nlspDestEstThroughput=_NlspDestEstThroughput_Object((1,3,6,1,4,1,23,2,19,3,1,1,5),_NlspDestEstThroughput_Type())
nlspDestEstThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspDestEstThroughput.setStatus(_A)
_NlspDestNextHopID_Type=NLSPID
_NlspDestNextHopID_Object=MibTableColumn
nlspDestNextHopID=_NlspDestNextHopID_Object((1,3,6,1,4,1,23,2,19,3,1,1,6),_NlspDestNextHopID_Type())
nlspDestNextHopID.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspDestNextHopID.setStatus(_A)
_NlspDestCost_Type=Integer32
_NlspDestCost_Object=MibTableColumn
nlspDestCost=_NlspDestCost_Object((1,3,6,1,4,1,23,2,19,3,1,1,7),_NlspDestCost_Type())
nlspDestCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspDestCost.setStatus(_A)
_NlspNeighbors_ObjectIdentity=ObjectIdentity
nlspNeighbors=_NlspNeighbors_ObjectIdentity((1,3,6,1,4,1,23,2,19,4))
_NlspNeighTable_Object=MibTable
nlspNeighTable=_NlspNeighTable_Object((1,3,6,1,4,1,23,2,19,4,1))
if mibBuilder.loadTexts:nlspNeighTable.setStatus(_A)
_NlspNeighEntry_Object=MibTableRow
nlspNeighEntry=_NlspNeighEntry_Object((1,3,6,1,4,1,23,2,19,4,1,1))
nlspNeighEntry.setIndexNames((0,_C,_V),(0,_C,_W),(0,_C,_X))
if mibBuilder.loadTexts:nlspNeighEntry.setStatus(_A)
_NlspNeighSysInstance_Type=Integer32
_NlspNeighSysInstance_Object=MibTableColumn
nlspNeighSysInstance=_NlspNeighSysInstance_Object((1,3,6,1,4,1,23,2,19,4,1,1,1),_NlspNeighSysInstance_Type())
nlspNeighSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNeighSysInstance.setStatus(_A)
_NlspNeighCircIndex_Type=Integer32
_NlspNeighCircIndex_Object=MibTableColumn
nlspNeighCircIndex=_NlspNeighCircIndex_Object((1,3,6,1,4,1,23,2,19,4,1,1,2),_NlspNeighCircIndex_Type())
nlspNeighCircIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNeighCircIndex.setStatus(_A)
_NlspNeighIndex_Type=Integer32
_NlspNeighIndex_Object=MibTableColumn
nlspNeighIndex=_NlspNeighIndex_Object((1,3,6,1,4,1,23,2,19,4,1,1,3),_NlspNeighIndex_Type())
nlspNeighIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNeighIndex.setStatus(_A)
class _NlspNeighState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('initializing',1),('up',2),('failed',3),('down',4)))
_NlspNeighState_Type.__name__=_D
_NlspNeighState_Object=MibTableColumn
nlspNeighState=_NlspNeighState_Object((1,3,6,1,4,1,23,2,19,4,1,1,4),_NlspNeighState_Type())
nlspNeighState.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNeighState.setStatus(_A)
_NlspNeighNICAddress_Type=PhysAddress
_NlspNeighNICAddress_Object=MibTableColumn
nlspNeighNICAddress=_NlspNeighNICAddress_Object((1,3,6,1,4,1,23,2,19,4,1,1,5),_NlspNeighNICAddress_Type())
nlspNeighNICAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNeighNICAddress.setStatus(_A)
class _NlspNeighSysType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_NlspNeighSysType_Type.__name__=_D
_NlspNeighSysType_Object=MibTableColumn
nlspNeighSysType=_NlspNeighSysType_Object((1,3,6,1,4,1,23,2,19,4,1,1,6),_NlspNeighSysType_Type())
nlspNeighSysType.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNeighSysType.setStatus(_A)
_NlspNeighSysID_Type=SystemID
_NlspNeighSysID_Object=MibTableColumn
nlspNeighSysID=_NlspNeighSysID_Object((1,3,6,1,4,1,23,2,19,4,1,1,7),_NlspNeighSysID_Type())
nlspNeighSysID.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNeighSysID.setStatus(_A)
class _NlspNeighName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_NlspNeighName_Type.__name__=_F
_NlspNeighName_Object=MibTableColumn
nlspNeighName=_NlspNeighName_Object((1,3,6,1,4,1,23,2,19,4,1,1,8),_NlspNeighName_Type())
nlspNeighName.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNeighName.setStatus(_A)
class _NlspNeighUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('undefined',1),('level1',2)))
_NlspNeighUsage_Type.__name__=_D
_NlspNeighUsage_Object=MibTableColumn
nlspNeighUsage=_NlspNeighUsage_Object((1,3,6,1,4,1,23,2,19,4,1,1,9),_NlspNeighUsage_Type())
nlspNeighUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNeighUsage.setStatus(_A)
class _NlspNeighHoldTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NlspNeighHoldTimer_Type.__name__=_D
_NlspNeighHoldTimer_Object=MibTableColumn
nlspNeighHoldTimer=_NlspNeighHoldTimer_Object((1,3,6,1,4,1,23,2,19,4,1,1,10),_NlspNeighHoldTimer_Type())
nlspNeighHoldTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNeighHoldTimer.setStatus(_A)
_NlspNeighRemainingTime_Type=Integer32
_NlspNeighRemainingTime_Object=MibTableColumn
nlspNeighRemainingTime=_NlspNeighRemainingTime_Object((1,3,6,1,4,1,23,2,19,4,1,1,11),_NlspNeighRemainingTime_Type())
nlspNeighRemainingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNeighRemainingTime.setStatus(_A)
class _NlspNeighPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_NlspNeighPriority_Type.__name__=_D
_NlspNeighPriority_Object=MibTableColumn
nlspNeighPriority=_NlspNeighPriority_Object((1,3,6,1,4,1,23,2,19,4,1,1,12),_NlspNeighPriority_Type())
nlspNeighPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNeighPriority.setStatus(_A)
_NlspTranslation_ObjectIdentity=ObjectIdentity
nlspTranslation=_NlspTranslation_ObjectIdentity((1,3,6,1,4,1,23,2,19,5))
_NlspIDMapTable_Object=MibTable
nlspIDMapTable=_NlspIDMapTable_Object((1,3,6,1,4,1,23,2,19,5,1))
if mibBuilder.loadTexts:nlspIDMapTable.setStatus(_A)
_NlspIDMapEntry_Object=MibTableRow
nlspIDMapEntry=_NlspIDMapEntry_Object((1,3,6,1,4,1,23,2,19,5,1,1))
nlspIDMapEntry.setIndexNames((0,_C,_Y),(0,_C,_Z))
if mibBuilder.loadTexts:nlspIDMapEntry.setStatus(_A)
_NlspIDMapSysInstance_Type=Integer32
_NlspIDMapSysInstance_Object=MibTableColumn
nlspIDMapSysInstance=_NlspIDMapSysInstance_Object((1,3,6,1,4,1,23,2,19,5,1,1,1),_NlspIDMapSysInstance_Type())
nlspIDMapSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspIDMapSysInstance.setStatus(_A)
_NlspIDMapID_Type=NLSPID
_NlspIDMapID_Object=MibTableColumn
nlspIDMapID=_NlspIDMapID_Object((1,3,6,1,4,1,23,2,19,5,1,1,2),_NlspIDMapID_Type())
nlspIDMapID.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspIDMapID.setStatus(_A)
class _NlspIDMapServerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_NlspIDMapServerName_Type.__name__=_F
_NlspIDMapServerName_Object=MibTableColumn
nlspIDMapServerName=_NlspIDMapServerName_Object((1,3,6,1,4,1,23,2,19,5,1,1,3),_NlspIDMapServerName_Type())
nlspIDMapServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspIDMapServerName.setStatus(_A)
_NlspIDMapNetNum_Type=NetNumber
_NlspIDMapNetNum_Object=MibTableColumn
nlspIDMapNetNum=_NlspIDMapNetNum_Object((1,3,6,1,4,1,23,2,19,5,1,1,4),_NlspIDMapNetNum_Type())
nlspIDMapNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspIDMapNetNum.setStatus(_A)
_NlspNetMapTable_Object=MibTable
nlspNetMapTable=_NlspNetMapTable_Object((1,3,6,1,4,1,23,2,19,5,2))
if mibBuilder.loadTexts:nlspNetMapTable.setStatus(_A)
_NlspNetMapEntry_Object=MibTableRow
nlspNetMapEntry=_NlspNetMapEntry_Object((1,3,6,1,4,1,23,2,19,5,2,1))
nlspNetMapEntry.setIndexNames((0,_C,_a),(0,_C,_b))
if mibBuilder.loadTexts:nlspNetMapEntry.setStatus(_A)
_NlspNetMapSysInstance_Type=Integer32
_NlspNetMapSysInstance_Object=MibTableColumn
nlspNetMapSysInstance=_NlspNetMapSysInstance_Object((1,3,6,1,4,1,23,2,19,5,2,1,1),_NlspNetMapSysInstance_Type())
nlspNetMapSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNetMapSysInstance.setStatus(_A)
_NlspNetMapNetNum_Type=NetNumber
_NlspNetMapNetNum_Object=MibTableColumn
nlspNetMapNetNum=_NlspNetMapNetNum_Object((1,3,6,1,4,1,23,2,19,5,2,1,2),_NlspNetMapNetNum_Type())
nlspNetMapNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNetMapNetNum.setStatus(_A)
class _NlspNetMapServerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_NlspNetMapServerName_Type.__name__=_F
_NlspNetMapServerName_Object=MibTableColumn
nlspNetMapServerName=_NlspNetMapServerName_Object((1,3,6,1,4,1,23,2,19,5,2,1,3),_NlspNetMapServerName_Type())
nlspNetMapServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNetMapServerName.setStatus(_A)
_NlspNetMapID_Type=NLSPID
_NlspNetMapID_Object=MibTableColumn
nlspNetMapID=_NlspNetMapID_Object((1,3,6,1,4,1,23,2,19,5,2,1,4),_NlspNetMapID_Type())
nlspNetMapID.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNetMapID.setStatus(_A)
_NlspNameMapTable_Object=MibTable
nlspNameMapTable=_NlspNameMapTable_Object((1,3,6,1,4,1,23,2,19,5,3))
if mibBuilder.loadTexts:nlspNameMapTable.setStatus(_A)
_NlspNameMapEntry_Object=MibTableRow
nlspNameMapEntry=_NlspNameMapEntry_Object((1,3,6,1,4,1,23,2,19,5,3,1))
nlspNameMapEntry.setIndexNames((0,_C,_c),(0,_C,_d))
if mibBuilder.loadTexts:nlspNameMapEntry.setStatus(_A)
_NlspNameMapSysInstance_Type=Integer32
_NlspNameMapSysInstance_Object=MibTableColumn
nlspNameMapSysInstance=_NlspNameMapSysInstance_Object((1,3,6,1,4,1,23,2,19,5,3,1,1),_NlspNameMapSysInstance_Type())
nlspNameMapSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNameMapSysInstance.setStatus(_A)
class _NlspNameMapServerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_NlspNameMapServerName_Type.__name__=_F
_NlspNameMapServerName_Object=MibTableColumn
nlspNameMapServerName=_NlspNameMapServerName_Object((1,3,6,1,4,1,23,2,19,5,3,1,2),_NlspNameMapServerName_Type())
nlspNameMapServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNameMapServerName.setStatus(_A)
_NlspNameMapNetNum_Type=NetNumber
_NlspNameMapNetNum_Object=MibTableColumn
nlspNameMapNetNum=_NlspNameMapNetNum_Object((1,3,6,1,4,1,23,2,19,5,3,1,3),_NlspNameMapNetNum_Type())
nlspNameMapNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNameMapNetNum.setStatus(_A)
_NlspNameMapID_Type=NLSPID
_NlspNameMapID_Object=MibTableColumn
nlspNameMapID=_NlspNameMapID_Object((1,3,6,1,4,1,23,2,19,5,3,1,4),_NlspNameMapID_Type())
nlspNameMapID.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNameMapID.setStatus(_A)
_NlspGraph_ObjectIdentity=ObjectIdentity
nlspGraph=_NlspGraph_ObjectIdentity((1,3,6,1,4,1,23,2,19,6))
_NlspNodeTable_Object=MibTable
nlspNodeTable=_NlspNodeTable_Object((1,3,6,1,4,1,23,2,19,6,1))
if mibBuilder.loadTexts:nlspNodeTable.setStatus(_A)
_NlspNodeEntry_Object=MibTableRow
nlspNodeEntry=_NlspNodeEntry_Object((1,3,6,1,4,1,23,2,19,6,1,1))
nlspNodeEntry.setIndexNames((0,_C,_e),(0,_C,_f))
if mibBuilder.loadTexts:nlspNodeEntry.setStatus(_A)
_NlspNodeSysInstance_Type=Integer32
_NlspNodeSysInstance_Object=MibTableColumn
nlspNodeSysInstance=_NlspNodeSysInstance_Object((1,3,6,1,4,1,23,2,19,6,1,1,1),_NlspNodeSysInstance_Type())
nlspNodeSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNodeSysInstance.setStatus(_A)
_NlspNodeID_Type=NLSPID
_NlspNodeID_Object=MibTableColumn
nlspNodeID=_NlspNodeID_Object((1,3,6,1,4,1,23,2,19,6,1,1,2),_NlspNodeID_Type())
nlspNodeID.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNodeID.setStatus(_A)
_NlspNodeNetNum_Type=NetNumber
_NlspNodeNetNum_Object=MibTableColumn
nlspNodeNetNum=_NlspNodeNetNum_Object((1,3,6,1,4,1,23,2,19,6,1,1,3),_NlspNodeNetNum_Type())
nlspNodeNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNodeNetNum.setStatus(_A)
class _NlspNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_I,2),('nlspLevel2Router',3),('router',4),('network',5)))
_NlspNodeType_Type.__name__=_D
_NlspNodeType_Object=MibTableColumn
nlspNodeType=_NlspNodeType_Object((1,3,6,1,4,1,23,2,19,6,1,1,4),_NlspNodeType_Type())
nlspNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNodeType.setStatus(_A)
_NlspNodeEstDelay_Type=Integer32
_NlspNodeEstDelay_Object=MibTableColumn
nlspNodeEstDelay=_NlspNodeEstDelay_Object((1,3,6,1,4,1,23,2,19,6,1,1,5),_NlspNodeEstDelay_Type())
nlspNodeEstDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNodeEstDelay.setStatus(_A)
_NlspNodeEstThroughput_Type=Integer32
_NlspNodeEstThroughput_Object=MibTableColumn
nlspNodeEstThroughput=_NlspNodeEstThroughput_Object((1,3,6,1,4,1,23,2,19,6,1,1,6),_NlspNodeEstThroughput_Type())
nlspNodeEstThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNodeEstThroughput.setStatus(_A)
_NlspNodeMaxPacketSize_Type=Integer32
_NlspNodeMaxPacketSize_Object=MibTableColumn
nlspNodeMaxPacketSize=_NlspNodeMaxPacketSize_Object((1,3,6,1,4,1,23,2,19,6,1,1,7),_NlspNodeMaxPacketSize_Type())
nlspNodeMaxPacketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNodeMaxPacketSize.setStatus(_A)
_NlspNodeCost_Type=Integer32
_NlspNodeCost_Object=MibTableColumn
nlspNodeCost=_NlspNodeCost_Object((1,3,6,1,4,1,23,2,19,6,1,1,8),_NlspNodeCost_Type())
nlspNodeCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNodeCost.setStatus(_A)
class _NlspNodeOverload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NlspNodeOverload_Type.__name__=_D
_NlspNodeOverload_Object=MibTableColumn
nlspNodeOverload=_NlspNodeOverload_Object((1,3,6,1,4,1,23,2,19,6,1,1,9),_NlspNodeOverload_Type())
nlspNodeOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNodeOverload.setStatus(_A)
class _NlspNodeReachable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NlspNodeReachable_Type.__name__=_D
_NlspNodeReachable_Object=MibTableColumn
nlspNodeReachable=_NlspNodeReachable_Object((1,3,6,1,4,1,23,2,19,6,1,1,10),_NlspNodeReachable_Type())
nlspNodeReachable.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspNodeReachable.setStatus(_A)
_NlspLinkTable_Object=MibTable
nlspLinkTable=_NlspLinkTable_Object((1,3,6,1,4,1,23,2,19,6,2))
if mibBuilder.loadTexts:nlspLinkTable.setStatus(_A)
_NlspLinkEntry_Object=MibTableRow
nlspLinkEntry=_NlspLinkEntry_Object((1,3,6,1,4,1,23,2,19,6,2,1))
nlspLinkEntry.setIndexNames((0,_C,_g),(0,_C,_h),(0,_C,_i))
if mibBuilder.loadTexts:nlspLinkEntry.setStatus(_A)
_NlspLinkSysInstance_Type=Integer32
_NlspLinkSysInstance_Object=MibTableColumn
nlspLinkSysInstance=_NlspLinkSysInstance_Object((1,3,6,1,4,1,23,2,19,6,2,1,1),_NlspLinkSysInstance_Type())
nlspLinkSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLinkSysInstance.setStatus(_A)
_NlspLinkNLSPID_Type=NLSPID
_NlspLinkNLSPID_Object=MibTableColumn
nlspLinkNLSPID=_NlspLinkNLSPID_Object((1,3,6,1,4,1,23,2,19,6,2,1,2),_NlspLinkNLSPID_Type())
nlspLinkNLSPID.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLinkNLSPID.setStatus(_A)
_NlspLinkIndex_Type=Integer32
_NlspLinkIndex_Object=MibTableColumn
nlspLinkIndex=_NlspLinkIndex_Object((1,3,6,1,4,1,23,2,19,6,2,1,3),_NlspLinkIndex_Type())
nlspLinkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLinkIndex.setStatus(_A)
_NlspLinkNeighNLSPID_Type=NLSPID
_NlspLinkNeighNLSPID_Object=MibTableColumn
nlspLinkNeighNLSPID=_NlspLinkNeighNLSPID_Object((1,3,6,1,4,1,23,2,19,6,2,1,4),_NlspLinkNeighNLSPID_Type())
nlspLinkNeighNLSPID.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLinkNeighNLSPID.setStatus(_A)
_NlspLinkFromNeighCost_Type=Integer32
_NlspLinkFromNeighCost_Object=MibTableColumn
nlspLinkFromNeighCost=_NlspLinkFromNeighCost_Object((1,3,6,1,4,1,23,2,19,6,2,1,5),_NlspLinkFromNeighCost_Type())
nlspLinkFromNeighCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLinkFromNeighCost.setStatus(_A)
_NlspLinkMaxPacketSize_Type=Integer32
_NlspLinkMaxPacketSize_Object=MibTableColumn
nlspLinkMaxPacketSize=_NlspLinkMaxPacketSize_Object((1,3,6,1,4,1,23,2,19,6,2,1,6),_NlspLinkMaxPacketSize_Type())
nlspLinkMaxPacketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLinkMaxPacketSize.setStatus(_A)
_NlspLinkThroughput_Type=Integer32
_NlspLinkThroughput_Object=MibTableColumn
nlspLinkThroughput=_NlspLinkThroughput_Object((1,3,6,1,4,1,23,2,19,6,2,1,7),_NlspLinkThroughput_Type())
nlspLinkThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLinkThroughput.setStatus(_A)
_NlspLinkDelay_Type=Integer32
_NlspLinkDelay_Object=MibTableColumn
nlspLinkDelay=_NlspLinkDelay_Object((1,3,6,1,4,1,23,2,19,6,2,1,8),_NlspLinkDelay_Type())
nlspLinkDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLinkDelay.setStatus(_A)
class _NlspLinkMediaType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_NlspLinkMediaType_Type.__name__=_F
_NlspLinkMediaType_Object=MibTableColumn
nlspLinkMediaType=_NlspLinkMediaType_Object((1,3,6,1,4,1,23,2,19,6,2,1,9),_NlspLinkMediaType_Type())
nlspLinkMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLinkMediaType.setStatus(_A)
_NlspLinkToNeighCost_Type=Integer32
_NlspLinkToNeighCost_Object=MibTableColumn
nlspLinkToNeighCost=_NlspLinkToNeighCost_Object((1,3,6,1,4,1,23,2,19,6,2,1,10),_NlspLinkToNeighCost_Type())
nlspLinkToNeighCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLinkToNeighCost.setStatus(_A)
_NlspPathTable_Object=MibTable
nlspPathTable=_NlspPathTable_Object((1,3,6,1,4,1,23,2,19,6,3))
if mibBuilder.loadTexts:nlspPathTable.setStatus(_A)
_NlspPathEntry_Object=MibTableRow
nlspPathEntry=_NlspPathEntry_Object((1,3,6,1,4,1,23,2,19,6,3,1))
nlspPathEntry.setIndexNames((0,_C,_j),(0,_C,_k),(0,_C,_l))
if mibBuilder.loadTexts:nlspPathEntry.setStatus(_A)
_NlspPathSysInstance_Type=Integer32
_NlspPathSysInstance_Object=MibTableColumn
nlspPathSysInstance=_NlspPathSysInstance_Object((1,3,6,1,4,1,23,2,19,6,3,1,1),_NlspPathSysInstance_Type())
nlspPathSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspPathSysInstance.setStatus(_A)
_NlspPathDestNLSPID_Type=NLSPID
_NlspPathDestNLSPID_Object=MibTableColumn
nlspPathDestNLSPID=_NlspPathDestNLSPID_Object((1,3,6,1,4,1,23,2,19,6,3,1,2),_NlspPathDestNLSPID_Type())
nlspPathDestNLSPID.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspPathDestNLSPID.setStatus(_A)
_NlspPathLinkIndex_Type=Integer32
_NlspPathLinkIndex_Object=MibTableColumn
nlspPathLinkIndex=_NlspPathLinkIndex_Object((1,3,6,1,4,1,23,2,19,6,3,1,3),_NlspPathLinkIndex_Type())
nlspPathLinkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspPathLinkIndex.setStatus(_A)
_NlspGraphXRouteTable_Object=MibTable
nlspGraphXRouteTable=_NlspGraphXRouteTable_Object((1,3,6,1,4,1,23,2,19,6,4))
if mibBuilder.loadTexts:nlspGraphXRouteTable.setStatus(_A)
_NlspGraphXRouteEntry_Object=MibTableRow
nlspGraphXRouteEntry=_NlspGraphXRouteEntry_Object((1,3,6,1,4,1,23,2,19,6,4,1))
nlspGraphXRouteEntry.setIndexNames((0,_C,_m),(0,_C,_n),(0,_C,_o))
if mibBuilder.loadTexts:nlspGraphXRouteEntry.setStatus(_A)
_NlspGraphXRouteSysInstance_Type=Integer32
_NlspGraphXRouteSysInstance_Object=MibTableColumn
nlspGraphXRouteSysInstance=_NlspGraphXRouteSysInstance_Object((1,3,6,1,4,1,23,2,19,6,4,1,1),_NlspGraphXRouteSysInstance_Type())
nlspGraphXRouteSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspGraphXRouteSysInstance.setStatus(_A)
_NlspGraphXRouteNLSPID_Type=NLSPID
_NlspGraphXRouteNLSPID_Object=MibTableColumn
nlspGraphXRouteNLSPID=_NlspGraphXRouteNLSPID_Object((1,3,6,1,4,1,23,2,19,6,4,1,2),_NlspGraphXRouteNLSPID_Type())
nlspGraphXRouteNLSPID.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspGraphXRouteNLSPID.setStatus(_A)
_NlspGraphXRouteNetNum_Type=NetNumber
_NlspGraphXRouteNetNum_Object=MibTableColumn
nlspGraphXRouteNetNum=_NlspGraphXRouteNetNum_Object((1,3,6,1,4,1,23,2,19,6,4,1,3),_NlspGraphXRouteNetNum_Type())
nlspGraphXRouteNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspGraphXRouteNetNum.setStatus(_A)
_NlspGraphXRouteCost_Type=Integer32
_NlspGraphXRouteCost_Object=MibTableColumn
nlspGraphXRouteCost=_NlspGraphXRouteCost_Object((1,3,6,1,4,1,23,2,19,6,4,1,4),_NlspGraphXRouteCost_Type())
nlspGraphXRouteCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspGraphXRouteCost.setStatus(_A)
_NlspGraphXRouteHopCount_Type=Integer32
_NlspGraphXRouteHopCount_Object=MibTableColumn
nlspGraphXRouteHopCount=_NlspGraphXRouteHopCount_Object((1,3,6,1,4,1,23,2,19,6,4,1,5),_NlspGraphXRouteHopCount_Type())
nlspGraphXRouteHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspGraphXRouteHopCount.setStatus(_A)
_NlspGraphServTable_Object=MibTable
nlspGraphServTable=_NlspGraphServTable_Object((1,3,6,1,4,1,23,2,19,6,5))
if mibBuilder.loadTexts:nlspGraphServTable.setStatus(_A)
_NlspGraphServEntry_Object=MibTableRow
nlspGraphServEntry=_NlspGraphServEntry_Object((1,3,6,1,4,1,23,2,19,6,5,1))
nlspGraphServEntry.setIndexNames((0,_C,_p),(0,_C,_q),(0,_C,_r),(0,_C,_s))
if mibBuilder.loadTexts:nlspGraphServEntry.setStatus(_A)
_NlspGraphServSysInstance_Type=Integer32
_NlspGraphServSysInstance_Object=MibTableColumn
nlspGraphServSysInstance=_NlspGraphServSysInstance_Object((1,3,6,1,4,1,23,2,19,6,5,1,1),_NlspGraphServSysInstance_Type())
nlspGraphServSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspGraphServSysInstance.setStatus(_A)
_NlspGraphServNLSPID_Type=NLSPID
_NlspGraphServNLSPID_Object=MibTableColumn
nlspGraphServNLSPID=_NlspGraphServNLSPID_Object((1,3,6,1,4,1,23,2,19,6,5,1,2),_NlspGraphServNLSPID_Type())
nlspGraphServNLSPID.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspGraphServNLSPID.setStatus(_A)
class _NlspGraphServName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_NlspGraphServName_Type.__name__=_F
_NlspGraphServName_Object=MibTableColumn
nlspGraphServName=_NlspGraphServName_Object((1,3,6,1,4,1,23,2,19,6,5,1,3),_NlspGraphServName_Type())
nlspGraphServName.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspGraphServName.setStatus(_A)
class _NlspGraphServTypeValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_NlspGraphServTypeValue_Type.__name__=_F
_NlspGraphServTypeValue_Object=MibTableColumn
nlspGraphServTypeValue=_NlspGraphServTypeValue_Object((1,3,6,1,4,1,23,2,19,6,5,1,4),_NlspGraphServTypeValue_Type())
nlspGraphServTypeValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspGraphServTypeValue.setStatus(_A)
class _NlspGraphServType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_J,1))
_NlspGraphServType_Type.__name__=_D
_NlspGraphServType_Object=MibTableColumn
nlspGraphServType=_NlspGraphServType_Object((1,3,6,1,4,1,23,2,19,6,5,1,5),_NlspGraphServType_Type())
nlspGraphServType.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspGraphServType.setStatus(_A)
_NlspGraphServNetNum_Type=NetNumber
_NlspGraphServNetNum_Object=MibTableColumn
nlspGraphServNetNum=_NlspGraphServNetNum_Object((1,3,6,1,4,1,23,2,19,6,5,1,6),_NlspGraphServNetNum_Type())
nlspGraphServNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspGraphServNetNum.setStatus(_A)
class _NlspGraphServNode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_NlspGraphServNode_Type.__name__=_F
_NlspGraphServNode_Object=MibTableColumn
nlspGraphServNode=_NlspGraphServNode_Object((1,3,6,1,4,1,23,2,19,6,5,1,7),_NlspGraphServNode_Type())
nlspGraphServNode.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspGraphServNode.setStatus(_A)
class _NlspGraphServSocket_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_NlspGraphServSocket_Type.__name__=_F
_NlspGraphServSocket_Object=MibTableColumn
nlspGraphServSocket=_NlspGraphServSocket_Object((1,3,6,1,4,1,23,2,19,6,5,1,8),_NlspGraphServSocket_Type())
nlspGraphServSocket.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspGraphServSocket.setStatus(_A)
_NlspLSP_ObjectIdentity=ObjectIdentity
nlspLSP=_NlspLSP_ObjectIdentity((1,3,6,1,4,1,23,2,19,7))
_NlspLSPTable_Object=MibTable
nlspLSPTable=_NlspLSPTable_Object((1,3,6,1,4,1,23,2,19,7,1))
if mibBuilder.loadTexts:nlspLSPTable.setStatus(_A)
_NlspLSPEntry_Object=MibTableRow
nlspLSPEntry=_NlspLSPEntry_Object((1,3,6,1,4,1,23,2,19,7,1,1))
nlspLSPEntry.setIndexNames((0,_C,_t),(0,_C,_u))
if mibBuilder.loadTexts:nlspLSPEntry.setStatus(_A)
_NlspLSPSysInstance_Type=Integer32
_NlspLSPSysInstance_Object=MibTableColumn
nlspLSPSysInstance=_NlspLSPSysInstance_Object((1,3,6,1,4,1,23,2,19,7,1,1,1),_NlspLSPSysInstance_Type())
nlspLSPSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLSPSysInstance.setStatus(_A)
class _NlspLSPID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_NlspLSPID_Type.__name__=_F
_NlspLSPID_Object=MibTableColumn
nlspLSPID=_NlspLSPID_Object((1,3,6,1,4,1,23,2,19,7,1,1,2),_NlspLSPID_Type())
nlspLSPID.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLSPID.setStatus(_A)
class _NlspLSPLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NlspLSPLifetime_Type.__name__=_D
_NlspLSPLifetime_Object=MibTableColumn
nlspLSPLifetime=_NlspLSPLifetime_Object((1,3,6,1,4,1,23,2,19,7,1,1,3),_NlspLSPLifetime_Type())
nlspLSPLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLSPLifetime.setStatus(_A)
class _NlspLSPSeqNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NlspLSPSeqNum_Type.__name__=_D
_NlspLSPSeqNum_Object=MibTableColumn
nlspLSPSeqNum=_NlspLSPSeqNum_Object((1,3,6,1,4,1,23,2,19,7,1,1,4),_NlspLSPSeqNum_Type())
nlspLSPSeqNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLSPSeqNum.setStatus(_A)
class _NlspLSPChecksum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NlspLSPChecksum_Type.__name__=_D
_NlspLSPChecksum_Object=MibTableColumn
nlspLSPChecksum=_NlspLSPChecksum_Object((1,3,6,1,4,1,23,2,19,7,1,1,5),_NlspLSPChecksum_Type())
nlspLSPChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLSPChecksum.setStatus(_A)
class _NlspLSPRouterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_NlspLSPRouterType_Type.__name__=_D
_NlspLSPRouterType_Object=MibTableColumn
nlspLSPRouterType=_NlspLSPRouterType_Object((1,3,6,1,4,1,23,2,19,7,1,1,6),_NlspLSPRouterType_Type())
nlspLSPRouterType.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLSPRouterType.setStatus(_A)
class _NlspLSPOverload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NlspLSPOverload_Type.__name__=_D
_NlspLSPOverload_Object=MibTableColumn
nlspLSPOverload=_NlspLSPOverload_Object((1,3,6,1,4,1,23,2,19,7,1,1,7),_NlspLSPOverload_Type())
nlspLSPOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLSPOverload.setStatus(_A)
class _NlspLSPHeader_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(27,27));fixedLength=27
_NlspLSPHeader_Type.__name__=_F
_NlspLSPHeader_Object=MibTableColumn
nlspLSPHeader=_NlspLSPHeader_Object((1,3,6,1,4,1,23,2,19,7,1,1,8),_NlspLSPHeader_Type())
nlspLSPHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLSPHeader.setStatus(_A)
_NlspLSPOptTable_Object=MibTable
nlspLSPOptTable=_NlspLSPOptTable_Object((1,3,6,1,4,1,23,2,19,7,2))
if mibBuilder.loadTexts:nlspLSPOptTable.setStatus(_A)
_NlspLSPOptEntry_Object=MibTableRow
nlspLSPOptEntry=_NlspLSPOptEntry_Object((1,3,6,1,4,1,23,2,19,7,2,1))
nlspLSPOptEntry.setIndexNames((0,_C,_v),(0,_C,_w),(0,_C,_x))
if mibBuilder.loadTexts:nlspLSPOptEntry.setStatus(_A)
_NlspLSPOptSysInstance_Type=Integer32
_NlspLSPOptSysInstance_Object=MibTableColumn
nlspLSPOptSysInstance=_NlspLSPOptSysInstance_Object((1,3,6,1,4,1,23,2,19,7,2,1,1),_NlspLSPOptSysInstance_Type())
nlspLSPOptSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLSPOptSysInstance.setStatus(_A)
class _NlspLSPOptLSPID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_NlspLSPOptLSPID_Type.__name__=_F
_NlspLSPOptLSPID_Object=MibTableColumn
nlspLSPOptLSPID=_NlspLSPOptLSPID_Object((1,3,6,1,4,1,23,2,19,7,2,1,2),_NlspLSPOptLSPID_Type())
nlspLSPOptLSPID.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLSPOptLSPID.setStatus(_A)
_NlspLSPOptIndex_Type=Integer32
_NlspLSPOptIndex_Object=MibTableColumn
nlspLSPOptIndex=_NlspLSPOptIndex_Object((1,3,6,1,4,1,23,2,19,7,2,1,3),_NlspLSPOptIndex_Type())
nlspLSPOptIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLSPOptIndex.setStatus(_A)
class _NlspLSPOptCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NlspLSPOptCode_Type.__name__=_D
_NlspLSPOptCode_Object=MibTableColumn
nlspLSPOptCode=_NlspLSPOptCode_Object((1,3,6,1,4,1,23,2,19,7,2,1,4),_NlspLSPOptCode_Type())
nlspLSPOptCode.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLSPOptCode.setStatus(_A)
class _NlspLSPOptLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NlspLSPOptLength_Type.__name__=_D
_NlspLSPOptLength_Object=MibTableColumn
nlspLSPOptLength=_NlspLSPOptLength_Object((1,3,6,1,4,1,23,2,19,7,2,1,5),_NlspLSPOptLength_Type())
nlspLSPOptLength.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLSPOptLength.setStatus(_A)
class _NlspLSPOptValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NlspLSPOptValue_Type.__name__=_F
_NlspLSPOptValue_Object=MibTableColumn
nlspLSPOptValue=_NlspLSPOptValue_Object((1,3,6,1,4,1,23,2,19,7,2,1,6),_NlspLSPOptValue_Type())
nlspLSPOptValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nlspLSPOptValue.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'SystemID':SystemID,'NLSPID':NLSPID,'NetNumber':NetNumber,'nlsp':nlsp,'nlspSystem':nlspSystem,'nlspSysTable':nlspSysTable,'nlspSysEntry':nlspSysEntry,_K:nlspSysInstance,'nlspSysState':nlspSysState,'nlspSysID':nlspSysID,'nlspSysMinNonBcastLSPTransInt':nlspSysMinNonBcastLSPTransInt,'nlspSysMinBcastLSPTransInt':nlspSysMinBcastLSPTransInt,'nlspSysMinLSPGenInt':nlspSysMinLSPGenInt,'nlspSysMaxLSPGenInt':nlspSysMaxLSPGenInt,'nlspSysMaxLSPAge':nlspSysMaxLSPAge,'nlspSysBcastHelloInt':nlspSysBcastHelloInt,'nlspSysNonBcastHelloInt':nlspSysNonBcastHelloInt,'nlspSysDRBcastHelloInt':nlspSysDRBcastHelloInt,'nlspSysHoldTimeMultiplier':nlspSysHoldTimeMultiplier,'nlspSysCompSNPInt':nlspSysCompSNPInt,'nlspSysPartSNPInt':nlspSysPartSNPInt,'nlspSysWaitTime':nlspSysWaitTime,'nlspSysOrigL1LSPBufSize':nlspSysOrigL1LSPBufSize,'nlspSysVersion':nlspSysVersion,'nlspSysCorrLSPs':nlspSysCorrLSPs,'nlspSysL1Overloaded':nlspSysL1Overloaded,'nlspSysL1DbaseOverloads':nlspSysL1DbaseOverloads,'nlspSysMaxSeqNums':nlspSysMaxSeqNums,'nlspSysSeqNumSkips':nlspSysSeqNumSkips,'nlspSysTransmittedLSPs':nlspSysTransmittedLSPs,'nlspSysReceivedLSPs':nlspSysReceivedLSPs,'nlspSysOwnLSPPurges':nlspSysOwnLSPPurges,'nlspSysVersionErrors':nlspSysVersionErrors,'nlspSysIncorrectPackets':nlspSysIncorrectPackets,'nlspSysNearestL2DefaultExists':nlspSysNearestL2DefaultExists,'nlspSysNearestL2DefaultRouter':nlspSysNearestL2DefaultRouter,'nlspSysResourceFailures':nlspSysResourceFailures,'nlspSysAreaTable':nlspSysAreaTable,'nlspSysAreaEntry':nlspSysAreaEntry,_L:nlspSysAreaSysInstance,_M:nlspSysAreaNet,_N:nlspSysAreaMask,'nlspActAreaTable':nlspActAreaTable,'nlspActAreaEntry':nlspActAreaEntry,_O:nlspActAreaSysInstance,_P:nlspActAreaNet,_Q:nlspActAreaMask,'nlspCircuit':nlspCircuit,'nlspCircTable':nlspCircTable,'nlspCircEntry':nlspCircEntry,_R:nlspCircSysInstance,_S:nlspCircIndex,'nlspCircState':nlspCircState,'nlspCircPace':nlspCircPace,'nlspCircHelloTimer':nlspCircHelloTimer,'nlspCircL1DefaultCost':nlspCircL1DefaultCost,'nlspCircL1DesRouterPriority':nlspCircL1DesRouterPriority,'nlspCircL1CircID':nlspCircL1CircID,'nlspCircL1DesRouter':nlspCircL1DesRouter,'nlspCircLANL1DesRouterChanges':nlspCircLANL1DesRouterChanges,'nlspCircNeighChanges':nlspCircNeighChanges,'nlspCircRejNeighbors':nlspCircRejNeighbors,'nlspCircOutPackets':nlspCircOutPackets,'nlspCircInPackets':nlspCircInPackets,'nlspCircActualMaxPacketSize':nlspCircActualMaxPacketSize,'nlspCircPSNPsSent':nlspCircPSNPsSent,'nlspCircPSNPsReceived':nlspCircPSNPsReceived,'nlspForwarding':nlspForwarding,'nlspDestTable':nlspDestTable,'nlspDestEntry':nlspDestEntry,_T:nlspDestSysInstance,_U:nlspDestNetNum,'nlspDestID':nlspDestID,'nlspDestEstDelay':nlspDestEstDelay,'nlspDestEstThroughput':nlspDestEstThroughput,'nlspDestNextHopID':nlspDestNextHopID,'nlspDestCost':nlspDestCost,'nlspNeighbors':nlspNeighbors,'nlspNeighTable':nlspNeighTable,'nlspNeighEntry':nlspNeighEntry,_V:nlspNeighSysInstance,_W:nlspNeighCircIndex,_X:nlspNeighIndex,'nlspNeighState':nlspNeighState,'nlspNeighNICAddress':nlspNeighNICAddress,'nlspNeighSysType':nlspNeighSysType,'nlspNeighSysID':nlspNeighSysID,'nlspNeighName':nlspNeighName,'nlspNeighUsage':nlspNeighUsage,'nlspNeighHoldTimer':nlspNeighHoldTimer,'nlspNeighRemainingTime':nlspNeighRemainingTime,'nlspNeighPriority':nlspNeighPriority,'nlspTranslation':nlspTranslation,'nlspIDMapTable':nlspIDMapTable,'nlspIDMapEntry':nlspIDMapEntry,_Y:nlspIDMapSysInstance,_Z:nlspIDMapID,'nlspIDMapServerName':nlspIDMapServerName,'nlspIDMapNetNum':nlspIDMapNetNum,'nlspNetMapTable':nlspNetMapTable,'nlspNetMapEntry':nlspNetMapEntry,_a:nlspNetMapSysInstance,_b:nlspNetMapNetNum,'nlspNetMapServerName':nlspNetMapServerName,'nlspNetMapID':nlspNetMapID,'nlspNameMapTable':nlspNameMapTable,'nlspNameMapEntry':nlspNameMapEntry,_c:nlspNameMapSysInstance,_d:nlspNameMapServerName,'nlspNameMapNetNum':nlspNameMapNetNum,'nlspNameMapID':nlspNameMapID,'nlspGraph':nlspGraph,'nlspNodeTable':nlspNodeTable,'nlspNodeEntry':nlspNodeEntry,_e:nlspNodeSysInstance,_f:nlspNodeID,'nlspNodeNetNum':nlspNodeNetNum,'nlspNodeType':nlspNodeType,'nlspNodeEstDelay':nlspNodeEstDelay,'nlspNodeEstThroughput':nlspNodeEstThroughput,'nlspNodeMaxPacketSize':nlspNodeMaxPacketSize,'nlspNodeCost':nlspNodeCost,'nlspNodeOverload':nlspNodeOverload,'nlspNodeReachable':nlspNodeReachable,'nlspLinkTable':nlspLinkTable,'nlspLinkEntry':nlspLinkEntry,_g:nlspLinkSysInstance,_h:nlspLinkNLSPID,_i:nlspLinkIndex,'nlspLinkNeighNLSPID':nlspLinkNeighNLSPID,'nlspLinkFromNeighCost':nlspLinkFromNeighCost,'nlspLinkMaxPacketSize':nlspLinkMaxPacketSize,'nlspLinkThroughput':nlspLinkThroughput,'nlspLinkDelay':nlspLinkDelay,'nlspLinkMediaType':nlspLinkMediaType,'nlspLinkToNeighCost':nlspLinkToNeighCost,'nlspPathTable':nlspPathTable,'nlspPathEntry':nlspPathEntry,_j:nlspPathSysInstance,_k:nlspPathDestNLSPID,_l:nlspPathLinkIndex,'nlspGraphXRouteTable':nlspGraphXRouteTable,'nlspGraphXRouteEntry':nlspGraphXRouteEntry,_m:nlspGraphXRouteSysInstance,_n:nlspGraphXRouteNLSPID,_o:nlspGraphXRouteNetNum,'nlspGraphXRouteCost':nlspGraphXRouteCost,'nlspGraphXRouteHopCount':nlspGraphXRouteHopCount,'nlspGraphServTable':nlspGraphServTable,'nlspGraphServEntry':nlspGraphServEntry,_p:nlspGraphServSysInstance,_q:nlspGraphServNLSPID,_r:nlspGraphServName,_s:nlspGraphServTypeValue,'nlspGraphServType':nlspGraphServType,'nlspGraphServNetNum':nlspGraphServNetNum,'nlspGraphServNode':nlspGraphServNode,'nlspGraphServSocket':nlspGraphServSocket,'nlspLSP':nlspLSP,'nlspLSPTable':nlspLSPTable,'nlspLSPEntry':nlspLSPEntry,_t:nlspLSPSysInstance,_u:nlspLSPID,'nlspLSPLifetime':nlspLSPLifetime,'nlspLSPSeqNum':nlspLSPSeqNum,'nlspLSPChecksum':nlspLSPChecksum,'nlspLSPRouterType':nlspLSPRouterType,'nlspLSPOverload':nlspLSPOverload,'nlspLSPHeader':nlspLSPHeader,'nlspLSPOptTable':nlspLSPOptTable,'nlspLSPOptEntry':nlspLSPOptEntry,_v:nlspLSPOptSysInstance,_w:nlspLSPOptLSPID,_x:nlspLSPOptIndex,'nlspLSPOptCode':nlspLSPOptCode,'nlspLSPOptLength':nlspLSPOptLength,'nlspLSPOptValue':nlspLSPOptValue})