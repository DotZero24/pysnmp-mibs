_BE='cpqSasPhyDrvSSDWearStatus'
_BD='cpqSasTapeDrvStatus'
_BC='cpqSasTapeDrvSasAddress'
_BB='cpqSasTapeDrvSerialNumber'
_BA='cpqSasTapeDrvFWRev'
_B9='cpqSasTapeDrvName'
_B8='cpqSasTapeDrvLocationString'
_B7='cpqSasLogDrvOsName'
_B6='cpqSasLogDrvStatus'
_B5='cpqSasPhyDrvStatus'
_B4='cpqScsiLogDrvOsName'
_B3='cpqScsiPhyDrvOsName'
_B2='cpqTapePhyDrvSerialNumber'
_B1='cpqTapePhyDrvFwRev'
_B0='cpqTapePhyDrvName'
_A_='cpqTapeLibraryState'
_Az='cpqTapeLibraryFwRev'
_Ay='cpqTapeLibraryName'
_Ax='cpqCdLibraryStatus'
_Aw='cpqSbDevScsiIdIndex'
_Av='cpqSbDevBusIndex'
_Au='cpqSbDevCntlrIndex'
_At='ssdWearOut'
_As='cpqSasHbaIndex'
_Ar='notCapable'
_Aq='cpqTapeCountersLunIndex'
_Ap='cpqTapeCountersScsiIdIndex'
_Ao='cpqTapeCountersBusIndex'
_An='cpqTapeCountersCntlrIndex'
_Am='cpqScsi2PhyDrvStatusChange'
_Al='cpqScsi2LogDrvStatusChange'
_Ak='cpqScsi2CntlrStatusChange'
_Aj='cpqScsiPhyDrvStatusChange'
_Ai='cpqScsiLogDrvStatusChange'
_Ah='cpqScsiCntlrStatusChange'
_Ag='cpqScsiTrapLogIndex'
_Af='cpqCdLibraryLunIndex'
_Ae='cpqScsiCdDrvLunIndex'
_Ad='cpqScsiCdDrvScsiIdIndex'
_Ac='cpqScsiCdDrvBusIndex'
_Ab='cpqScsiCdDrvCntlrIndex'
_Aa='wormDrive'
_AZ='processor'
_AY='cpqScsiTargetScsiIdIndex'
_AX='cpqScsiTargetBusIndex'
_AW='cpqScsiTargetCntlrIndex'
_AV='nonMember'
_AU='missingWasPredictiveFailure'
_AT='predictiveFailure'
_AS='rebuilding'
_AR='cpqScsiCntlrBusIndex'
_AQ='cpqScsiCntlrIndex'
_AP='cpqScsiOsCommonModuleIndex'
_AO='cpqScsiNw3xVolLogDrvIndex'
_AN='cpqScsiNw3xVolBusIndex'
_AM='cpqScsiNw3xVolCntlrIndex'
_AL='cpqScsiNw3xStatLogDrvIndex'
_AK='cpqScsiNw3xStatBusIndex'
_AJ='cpqScsiNw3xStatCntlrIndex'
_AI='cpqScsiNw3xBusIndex'
_AH='cpqScsiNw3xCntlrIndex'
_AG='NotificationType'
_AF='cpqSasPhyDrvSasAddress'
_AE='cpqSasPhyDrvSerialNumber'
_AD='cpqSasPhyDrvFWRev'
_AC='cpqSasPhyDrvModel'
_AB='cpqSasPhyDrvType'
_AA='cpqSasPhyDrvLocationString'
_A9='cpqScsiPhyDrvSerialNum'
_A8='cpqScsiPhyDrvFWRev'
_A7='cpqScsiPhyDrvModel'
_A6='cpqScsiPhyDrvVendor'
_A5='cpqTapePhyDrvStatus'
_A4='cpqSasTapeDrvIndex'
_A3='cpqSasTapeDrvHbaIndex'
_A2='cpqSasLogDrvIndex'
_A1='cpqSasLogDrvHbaIndex'
_A0='cpqTapeLibraryLunIndex'
_z='cpqTapeLibraryScsiIdIndex'
_y='cpqTapeLibraryBusIndex'
_x='cpqTapeLibraryCntlrIndex'
_w='false'
_v='true'
_u='cpqTapePhyDrvLunIndex'
_t='cpqCdLibraryScsiIdIndex'
_s='cpqCdLibraryBusIndex'
_r='cpqCdLibraryCntlrIndex'
_q='external'
_p='internal'
_o='nonHotPlug'
_n='hotPlug'
_m='proliant'
_l='missingWasOffline'
_k='missingWasFailed'
_j='missingWasOk'
_i='cpqScsiLogDrvIndex'
_h='cpqScsiLogDrvBusIndex'
_g='cpqScsiLogDrvCntlrIndex'
_f='cpqScsiLogDrvStatus'
_e='cpqScsiCntlrStatus'
_d='cpqSasPhyDrvIndex'
_c='cpqSasPhyDrvHbaIndex'
_b='cpqTapePhyDrvScsiIdIndex'
_a='cpqTapePhyDrvBusIndex'
_Z='cpqTapePhyDrvCntlrIndex'
_Y='cpqScsiPhyDrvIndex'
_X='cpqScsiPhyDrvBusIndex'
_W='cpqScsiPhyDrvCntlrIndex'
_V='optional'
_U='cpqSasHbaHwLocation'
_T='cpqTapePhyDrvCondition'
_S='notSupported'
_R='cpqScsiPhyDrvStatus'
_Q='cpqTapeLibrarySerialNumber'
_P='offline'
_O='OctetString'
_N='degraded'
_M='failed'
_L='sysName'
_K='SNMPv2-MIB'
_J='cpqHoTrapFlags'
_I='CPQHOST-MIB'
_H='ok'
_G='other'
_F='DisplayString'
_E='deprecated'
_D='Integer32'
_C='CPQSCSI-MIB'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols(_I,'compaq',_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_K,_L)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_AG,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_AG,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_CpqScsi_ObjectIdentity=ObjectIdentity
cpqScsi=_CpqScsi_ObjectIdentity((1,3,6,1,4,1,232,5))
_CpqScsiMibRev_ObjectIdentity=ObjectIdentity
cpqScsiMibRev=_CpqScsiMibRev_ObjectIdentity((1,3,6,1,4,1,232,5,1))
class _CpqScsiMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqScsiMibRevMajor_Type.__name__=_D
_CpqScsiMibRevMajor_Object=MibScalar
cpqScsiMibRevMajor=_CpqScsiMibRevMajor_Object((1,3,6,1,4,1,232,5,1,1),_CpqScsiMibRevMajor_Type())
cpqScsiMibRevMajor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiMibRevMajor.setStatus(_B)
class _CpqScsiMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqScsiMibRevMinor_Type.__name__=_D
_CpqScsiMibRevMinor_Object=MibScalar
cpqScsiMibRevMinor=_CpqScsiMibRevMinor_Object((1,3,6,1,4,1,232,5,1,2),_CpqScsiMibRevMinor_Type())
cpqScsiMibRevMinor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiMibRevMinor.setStatus(_B)
class _CpqScsiMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_N,3),(_M,4)))
_CpqScsiMibCondition_Type.__name__=_D
_CpqScsiMibCondition_Object=MibScalar
cpqScsiMibCondition=_CpqScsiMibCondition_Object((1,3,6,1,4,1,232,5,1,3),_CpqScsiMibCondition_Type())
cpqScsiMibCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiMibCondition.setStatus(_B)
_CpqScsiComponent_ObjectIdentity=ObjectIdentity
cpqScsiComponent=_CpqScsiComponent_ObjectIdentity((1,3,6,1,4,1,232,5,2))
_CpqScsiInterface_ObjectIdentity=ObjectIdentity
cpqScsiInterface=_CpqScsiInterface_ObjectIdentity((1,3,6,1,4,1,232,5,2,1))
_CpqScsiOsNetWare_ObjectIdentity=ObjectIdentity
cpqScsiOsNetWare=_CpqScsiOsNetWare_ObjectIdentity((1,3,6,1,4,1,232,5,2,1,1))
class _CpqScsiNw3xDriverName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CpqScsiNw3xDriverName_Type.__name__=_F
_CpqScsiNw3xDriverName_Object=MibScalar
cpqScsiNw3xDriverName=_CpqScsiNw3xDriverName_Object((1,3,6,1,4,1,232,5,2,1,1,1),_CpqScsiNw3xDriverName_Type())
cpqScsiNw3xDriverName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xDriverName.setStatus(_E)
class _CpqScsiNw3xDriverVers_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqScsiNw3xDriverVers_Type.__name__=_F
_CpqScsiNw3xDriverVers_Object=MibScalar
cpqScsiNw3xDriverVers=_CpqScsiNw3xDriverVers_Object((1,3,6,1,4,1,232,5,2,1,1,2),_CpqScsiNw3xDriverVers_Type())
cpqScsiNw3xDriverVers.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xDriverVers.setStatus(_E)
class _CpqScsiNw3xDriverPollType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('polled',2),('demand',3)))
_CpqScsiNw3xDriverPollType_Type.__name__=_D
_CpqScsiNw3xDriverPollType_Object=MibScalar
cpqScsiNw3xDriverPollType=_CpqScsiNw3xDriverPollType_Object((1,3,6,1,4,1,232,5,2,1,1,3),_CpqScsiNw3xDriverPollType_Type())
cpqScsiNw3xDriverPollType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xDriverPollType.setStatus(_E)
class _CpqScsiNw3xDriverPollTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_CpqScsiNw3xDriverPollTime_Type.__name__=_D
_CpqScsiNw3xDriverPollTime_Object=MibScalar
cpqScsiNw3xDriverPollTime=_CpqScsiNw3xDriverPollTime_Object((1,3,6,1,4,1,232,5,2,1,1,4),_CpqScsiNw3xDriverPollTime_Type())
cpqScsiNw3xDriverPollTime.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xDriverPollTime.setStatus(_E)
_CpqScsiNw3xCntlrInfoTable_Object=MibTable
cpqScsiNw3xCntlrInfoTable=_CpqScsiNw3xCntlrInfoTable_Object((1,3,6,1,4,1,232,5,2,1,1,5))
if mibBuilder.loadTexts:cpqScsiNw3xCntlrInfoTable.setStatus(_E)
_CpqScsiNw3xCntlrInfoEntry_Object=MibTableRow
cpqScsiNw3xCntlrInfoEntry=_CpqScsiNw3xCntlrInfoEntry_Object((1,3,6,1,4,1,232,5,2,1,1,5,1))
cpqScsiNw3xCntlrInfoEntry.setIndexNames((0,_C,_AH),(0,_C,_AI))
if mibBuilder.loadTexts:cpqScsiNw3xCntlrInfoEntry.setStatus(_E)
class _CpqScsiNw3xCntlrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiNw3xCntlrIndex_Type.__name__=_D
_CpqScsiNw3xCntlrIndex_Object=MibTableColumn
cpqScsiNw3xCntlrIndex=_CpqScsiNw3xCntlrIndex_Object((1,3,6,1,4,1,232,5,2,1,1,5,1,1),_CpqScsiNw3xCntlrIndex_Type())
cpqScsiNw3xCntlrIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xCntlrIndex.setStatus(_E)
class _CpqScsiNw3xBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiNw3xBusIndex_Type.__name__=_D
_CpqScsiNw3xBusIndex_Object=MibTableColumn
cpqScsiNw3xBusIndex=_CpqScsiNw3xBusIndex_Object((1,3,6,1,4,1,232,5,2,1,1,5,1,2),_CpqScsiNw3xBusIndex_Type())
cpqScsiNw3xBusIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xBusIndex.setStatus(_E)
class _CpqScsiNw3xXptDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CpqScsiNw3xXptDesc_Type.__name__=_F
_CpqScsiNw3xXptDesc_Object=MibTableColumn
cpqScsiNw3xXptDesc=_CpqScsiNw3xXptDesc_Object((1,3,6,1,4,1,232,5,2,1,1,5,1,3),_CpqScsiNw3xXptDesc_Type())
cpqScsiNw3xXptDesc.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xXptDesc.setStatus(_E)
class _CpqScsiNw3xXptVers_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqScsiNw3xXptVers_Type.__name__=_F
_CpqScsiNw3xXptVers_Object=MibTableColumn
cpqScsiNw3xXptVers=_CpqScsiNw3xXptVers_Object((1,3,6,1,4,1,232,5,2,1,1,5,1,4),_CpqScsiNw3xXptVers_Type())
cpqScsiNw3xXptVers.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xXptVers.setStatus(_E)
class _CpqScsiNw3xSimDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CpqScsiNw3xSimDesc_Type.__name__=_F
_CpqScsiNw3xSimDesc_Object=MibTableColumn
cpqScsiNw3xSimDesc=_CpqScsiNw3xSimDesc_Object((1,3,6,1,4,1,232,5,2,1,1,5,1,5),_CpqScsiNw3xSimDesc_Type())
cpqScsiNw3xSimDesc.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xSimDesc.setStatus(_E)
class _CpqScsiNw3xSimVers_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqScsiNw3xSimVers_Type.__name__=_F
_CpqScsiNw3xSimVers_Object=MibTableColumn
cpqScsiNw3xSimVers=_CpqScsiNw3xSimVers_Object((1,3,6,1,4,1,232,5,2,1,1,5,1,6),_CpqScsiNw3xSimVers_Type())
cpqScsiNw3xSimVers.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xSimVers.setStatus(_E)
class _CpqScsiNw3xHbaDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqScsiNw3xHbaDesc_Type.__name__=_F
_CpqScsiNw3xHbaDesc_Object=MibTableColumn
cpqScsiNw3xHbaDesc=_CpqScsiNw3xHbaDesc_Object((1,3,6,1,4,1,232,5,2,1,1,5,1,7),_CpqScsiNw3xHbaDesc_Type())
cpqScsiNw3xHbaDesc.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xHbaDesc.setStatus(_E)
_CpqScsiLogDrvStatTable_Object=MibTable
cpqScsiLogDrvStatTable=_CpqScsiLogDrvStatTable_Object((1,3,6,1,4,1,232,5,2,1,1,6))
if mibBuilder.loadTexts:cpqScsiLogDrvStatTable.setStatus(_E)
_CpqScsiLogDrvStatEntry_Object=MibTableRow
cpqScsiLogDrvStatEntry=_CpqScsiLogDrvStatEntry_Object((1,3,6,1,4,1,232,5,2,1,1,6,1))
cpqScsiLogDrvStatEntry.setIndexNames((0,_C,_AJ),(0,_C,_AK),(0,_C,_AL))
if mibBuilder.loadTexts:cpqScsiLogDrvStatEntry.setStatus(_E)
class _CpqScsiNw3xStatCntlrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiNw3xStatCntlrIndex_Type.__name__=_D
_CpqScsiNw3xStatCntlrIndex_Object=MibTableColumn
cpqScsiNw3xStatCntlrIndex=_CpqScsiNw3xStatCntlrIndex_Object((1,3,6,1,4,1,232,5,2,1,1,6,1,1),_CpqScsiNw3xStatCntlrIndex_Type())
cpqScsiNw3xStatCntlrIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xStatCntlrIndex.setStatus(_E)
class _CpqScsiNw3xStatBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,225))
_CpqScsiNw3xStatBusIndex_Type.__name__=_D
_CpqScsiNw3xStatBusIndex_Object=MibTableColumn
cpqScsiNw3xStatBusIndex=_CpqScsiNw3xStatBusIndex_Object((1,3,6,1,4,1,232,5,2,1,1,6,1,2),_CpqScsiNw3xStatBusIndex_Type())
cpqScsiNw3xStatBusIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xStatBusIndex.setStatus(_E)
class _CpqScsiNw3xStatLogDrvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,225))
_CpqScsiNw3xStatLogDrvIndex_Type.__name__=_D
_CpqScsiNw3xStatLogDrvIndex_Object=MibTableColumn
cpqScsiNw3xStatLogDrvIndex=_CpqScsiNw3xStatLogDrvIndex_Object((1,3,6,1,4,1,232,5,2,1,1,6,1,3),_CpqScsiNw3xStatLogDrvIndex_Type())
cpqScsiNw3xStatLogDrvIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xStatLogDrvIndex.setStatus(_E)
_CpqScsiNw3xTotalReads_Type=Counter32
_CpqScsiNw3xTotalReads_Object=MibTableColumn
cpqScsiNw3xTotalReads=_CpqScsiNw3xTotalReads_Object((1,3,6,1,4,1,232,5,2,1,1,6,1,4),_CpqScsiNw3xTotalReads_Type())
cpqScsiNw3xTotalReads.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xTotalReads.setStatus(_E)
_CpqScsiNw3xTotalWrites_Type=Counter32
_CpqScsiNw3xTotalWrites_Object=MibTableColumn
cpqScsiNw3xTotalWrites=_CpqScsiNw3xTotalWrites_Object((1,3,6,1,4,1,232,5,2,1,1,6,1,5),_CpqScsiNw3xTotalWrites_Type())
cpqScsiNw3xTotalWrites.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xTotalWrites.setStatus(_E)
_CpqScsiNw3xCorrReads_Type=Counter32
_CpqScsiNw3xCorrReads_Object=MibTableColumn
cpqScsiNw3xCorrReads=_CpqScsiNw3xCorrReads_Object((1,3,6,1,4,1,232,5,2,1,1,6,1,6),_CpqScsiNw3xCorrReads_Type())
cpqScsiNw3xCorrReads.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xCorrReads.setStatus(_E)
_CpqScsiNw3xCorrWrites_Type=Counter32
_CpqScsiNw3xCorrWrites_Object=MibTableColumn
cpqScsiNw3xCorrWrites=_CpqScsiNw3xCorrWrites_Object((1,3,6,1,4,1,232,5,2,1,1,6,1,7),_CpqScsiNw3xCorrWrites_Type())
cpqScsiNw3xCorrWrites.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xCorrWrites.setStatus(_E)
_CpqScsiNw3xFatalReads_Type=Counter32
_CpqScsiNw3xFatalReads_Object=MibTableColumn
cpqScsiNw3xFatalReads=_CpqScsiNw3xFatalReads_Object((1,3,6,1,4,1,232,5,2,1,1,6,1,8),_CpqScsiNw3xFatalReads_Type())
cpqScsiNw3xFatalReads.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xFatalReads.setStatus(_E)
_CpqScsiNw3xFatalWrites_Type=Counter32
_CpqScsiNw3xFatalWrites_Object=MibTableColumn
cpqScsiNw3xFatalWrites=_CpqScsiNw3xFatalWrites_Object((1,3,6,1,4,1,232,5,2,1,1,6,1,9),_CpqScsiNw3xFatalWrites_Type())
cpqScsiNw3xFatalWrites.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xFatalWrites.setStatus(_E)
_CpqScsiVolMapTable_Object=MibTable
cpqScsiVolMapTable=_CpqScsiVolMapTable_Object((1,3,6,1,4,1,232,5,2,1,1,7))
if mibBuilder.loadTexts:cpqScsiVolMapTable.setStatus(_E)
_CpqScsiVolMapEntry_Object=MibTableRow
cpqScsiVolMapEntry=_CpqScsiVolMapEntry_Object((1,3,6,1,4,1,232,5,2,1,1,7,1))
cpqScsiVolMapEntry.setIndexNames((0,_C,_AM),(0,_C,_AN),(0,_C,_AO))
if mibBuilder.loadTexts:cpqScsiVolMapEntry.setStatus(_E)
class _CpqScsiNw3xVolCntlrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,225))
_CpqScsiNw3xVolCntlrIndex_Type.__name__=_D
_CpqScsiNw3xVolCntlrIndex_Object=MibTableColumn
cpqScsiNw3xVolCntlrIndex=_CpqScsiNw3xVolCntlrIndex_Object((1,3,6,1,4,1,232,5,2,1,1,7,1,1),_CpqScsiNw3xVolCntlrIndex_Type())
cpqScsiNw3xVolCntlrIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xVolCntlrIndex.setStatus(_E)
class _CpqScsiNw3xVolBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,225))
_CpqScsiNw3xVolBusIndex_Type.__name__=_D
_CpqScsiNw3xVolBusIndex_Object=MibTableColumn
cpqScsiNw3xVolBusIndex=_CpqScsiNw3xVolBusIndex_Object((1,3,6,1,4,1,232,5,2,1,1,7,1,2),_CpqScsiNw3xVolBusIndex_Type())
cpqScsiNw3xVolBusIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xVolBusIndex.setStatus(_E)
class _CpqScsiNw3xVolLogDrvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,225))
_CpqScsiNw3xVolLogDrvIndex_Type.__name__=_D
_CpqScsiNw3xVolLogDrvIndex_Object=MibTableColumn
cpqScsiNw3xVolLogDrvIndex=_CpqScsiNw3xVolLogDrvIndex_Object((1,3,6,1,4,1,232,5,2,1,1,7,1,3),_CpqScsiNw3xVolLogDrvIndex_Type())
cpqScsiNw3xVolLogDrvIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xVolLogDrvIndex.setStatus(_E)
class _CpqScsiNw3xVolMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqScsiNw3xVolMap_Type.__name__=_O
_CpqScsiNw3xVolMap_Object=MibTableColumn
cpqScsiNw3xVolMap=_CpqScsiNw3xVolMap_Object((1,3,6,1,4,1,232,5,2,1,1,7,1,4),_CpqScsiNw3xVolMap_Type())
cpqScsiNw3xVolMap.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiNw3xVolMap.setStatus(_E)
_CpqScsiOsCommon_ObjectIdentity=ObjectIdentity
cpqScsiOsCommon=_CpqScsiOsCommon_ObjectIdentity((1,3,6,1,4,1,232,5,2,1,4))
class _CpqScsiOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqScsiOsCommonPollFreq_Type.__name__=_D
_CpqScsiOsCommonPollFreq_Object=MibScalar
cpqScsiOsCommonPollFreq=_CpqScsiOsCommonPollFreq_Object((1,3,6,1,4,1,232,5,2,1,4,1),_CpqScsiOsCommonPollFreq_Type())
cpqScsiOsCommonPollFreq.setMaxAccess('read-write')
if mibBuilder.loadTexts:cpqScsiOsCommonPollFreq.setStatus(_B)
_CpqScsiOsCommonModuleTable_Object=MibTable
cpqScsiOsCommonModuleTable=_CpqScsiOsCommonModuleTable_Object((1,3,6,1,4,1,232,5,2,1,4,2))
if mibBuilder.loadTexts:cpqScsiOsCommonModuleTable.setStatus(_E)
_CpqScsiOsCommonModuleEntry_Object=MibTableRow
cpqScsiOsCommonModuleEntry=_CpqScsiOsCommonModuleEntry_Object((1,3,6,1,4,1,232,5,2,1,4,2,1))
cpqScsiOsCommonModuleEntry.setIndexNames((0,_C,_AP))
if mibBuilder.loadTexts:cpqScsiOsCommonModuleEntry.setStatus(_E)
class _CpqScsiOsCommonModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiOsCommonModuleIndex_Type.__name__=_D
_CpqScsiOsCommonModuleIndex_Object=MibTableColumn
cpqScsiOsCommonModuleIndex=_CpqScsiOsCommonModuleIndex_Object((1,3,6,1,4,1,232,5,2,1,4,2,1,1),_CpqScsiOsCommonModuleIndex_Type())
cpqScsiOsCommonModuleIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiOsCommonModuleIndex.setStatus(_E)
class _CpqScsiOsCommonModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqScsiOsCommonModuleName_Type.__name__=_F
_CpqScsiOsCommonModuleName_Object=MibTableColumn
cpqScsiOsCommonModuleName=_CpqScsiOsCommonModuleName_Object((1,3,6,1,4,1,232,5,2,1,4,2,1,2),_CpqScsiOsCommonModuleName_Type())
cpqScsiOsCommonModuleName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiOsCommonModuleName.setStatus(_E)
class _CpqScsiOsCommonModuleVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqScsiOsCommonModuleVersion_Type.__name__=_F
_CpqScsiOsCommonModuleVersion_Object=MibTableColumn
cpqScsiOsCommonModuleVersion=_CpqScsiOsCommonModuleVersion_Object((1,3,6,1,4,1,232,5,2,1,4,2,1,3),_CpqScsiOsCommonModuleVersion_Type())
cpqScsiOsCommonModuleVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiOsCommonModuleVersion.setStatus(_E)
class _CpqScsiOsCommonModuleDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqScsiOsCommonModuleDate_Type.__name__=_O
_CpqScsiOsCommonModuleDate_Object=MibTableColumn
cpqScsiOsCommonModuleDate=_CpqScsiOsCommonModuleDate_Object((1,3,6,1,4,1,232,5,2,1,4,2,1,4),_CpqScsiOsCommonModuleDate_Type())
cpqScsiOsCommonModuleDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiOsCommonModuleDate.setStatus(_E)
class _CpqScsiOsCommonModulePurpose_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqScsiOsCommonModulePurpose_Type.__name__=_F
_CpqScsiOsCommonModulePurpose_Object=MibTableColumn
cpqScsiOsCommonModulePurpose=_CpqScsiOsCommonModulePurpose_Object((1,3,6,1,4,1,232,5,2,1,4,2,1,5),_CpqScsiOsCommonModulePurpose_Type())
cpqScsiOsCommonModulePurpose.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiOsCommonModulePurpose.setStatus(_E)
_CpqScsiCntlr_ObjectIdentity=ObjectIdentity
cpqScsiCntlr=_CpqScsiCntlr_ObjectIdentity((1,3,6,1,4,1,232,5,2,2))
_CpqScsiCntlrTable_Object=MibTable
cpqScsiCntlrTable=_CpqScsiCntlrTable_Object((1,3,6,1,4,1,232,5,2,2,1))
if mibBuilder.loadTexts:cpqScsiCntlrTable.setStatus(_B)
_CpqScsiCntlrEntry_Object=MibTableRow
cpqScsiCntlrEntry=_CpqScsiCntlrEntry_Object((1,3,6,1,4,1,232,5,2,2,1,1))
cpqScsiCntlrEntry.setIndexNames((0,_C,_AQ),(0,_C,_AR))
if mibBuilder.loadTexts:cpqScsiCntlrEntry.setStatus(_B)
_CpqScsiCntlrIndex_Type=Integer32
_CpqScsiCntlrIndex_Object=MibTableColumn
cpqScsiCntlrIndex=_CpqScsiCntlrIndex_Object((1,3,6,1,4,1,232,5,2,2,1,1,1),_CpqScsiCntlrIndex_Type())
cpqScsiCntlrIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrIndex.setStatus(_B)
class _CpqScsiCntlrBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiCntlrBusIndex_Type.__name__=_D
_CpqScsiCntlrBusIndex_Object=MibTableColumn
cpqScsiCntlrBusIndex=_CpqScsiCntlrBusIndex_Object((1,3,6,1,4,1,232,5,2,2,1,1,2),_CpqScsiCntlrBusIndex_Type())
cpqScsiCntlrBusIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrBusIndex.setStatus(_B)
class _CpqScsiCntlrModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*((_G,1),('cpqs710',2),('cpqs94',3),('cpqs810p',4),('cpqs825e',5),('cpqs825p',6),('cpqs974p',7),('cpqs875p',8),('extended',9),('cpqs895p',10),('cpqs896p',11),('cpqa789x',12),('cpqs876t',13),('hpu320',14),('hpu320r',15),('generic',16),('hp1u320g2',17),('hp1u320g1',18),('hpSc11Xe',19)))
_CpqScsiCntlrModel_Type.__name__=_D
_CpqScsiCntlrModel_Object=MibTableColumn
cpqScsiCntlrModel=_CpqScsiCntlrModel_Object((1,3,6,1,4,1,232,5,2,2,1,1,3),_CpqScsiCntlrModel_Type())
cpqScsiCntlrModel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrModel.setStatus(_B)
_CpqScsiCntlrFWVers_Type=DisplayString
_CpqScsiCntlrFWVers_Object=MibTableColumn
cpqScsiCntlrFWVers=_CpqScsiCntlrFWVers_Object((1,3,6,1,4,1,232,5,2,2,1,1,4),_CpqScsiCntlrFWVers_Type())
cpqScsiCntlrFWVers.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrFWVers.setStatus(_B)
class _CpqScsiCntlrSWVers_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqScsiCntlrSWVers_Type.__name__=_F
_CpqScsiCntlrSWVers_Object=MibTableColumn
cpqScsiCntlrSWVers=_CpqScsiCntlrSWVers_Object((1,3,6,1,4,1,232,5,2,2,1,1,5),_CpqScsiCntlrSWVers_Type())
cpqScsiCntlrSWVers.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrSWVers.setStatus(_E)
class _CpqScsiCntlrSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiCntlrSlot_Type.__name__=_D
_CpqScsiCntlrSlot_Object=MibTableColumn
cpqScsiCntlrSlot=_CpqScsiCntlrSlot_Object((1,3,6,1,4,1,232,5,2,2,1,1,6),_CpqScsiCntlrSlot_Type())
cpqScsiCntlrSlot.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrSlot.setStatus(_B)
class _CpqScsiCntlrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_M,3)))
_CpqScsiCntlrStatus_Type.__name__=_D
_CpqScsiCntlrStatus_Object=MibTableColumn
cpqScsiCntlrStatus=_CpqScsiCntlrStatus_Object((1,3,6,1,4,1,232,5,2,2,1,1,7),_CpqScsiCntlrStatus_Type())
cpqScsiCntlrStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrStatus.setStatus(_B)
_CpqScsiCntlrHardResets_Type=Counter32
_CpqScsiCntlrHardResets_Object=MibTableColumn
cpqScsiCntlrHardResets=_CpqScsiCntlrHardResets_Object((1,3,6,1,4,1,232,5,2,2,1,1,8),_CpqScsiCntlrHardResets_Type())
cpqScsiCntlrHardResets.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrHardResets.setStatus(_B)
_CpqScsiCntlrSoftResets_Type=Counter32
_CpqScsiCntlrSoftResets_Object=MibTableColumn
cpqScsiCntlrSoftResets=_CpqScsiCntlrSoftResets_Object((1,3,6,1,4,1,232,5,2,2,1,1,9),_CpqScsiCntlrSoftResets_Type())
cpqScsiCntlrSoftResets.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrSoftResets.setStatus(_B)
_CpqScsiCntlrTimeouts_Type=Counter32
_CpqScsiCntlrTimeouts_Object=MibTableColumn
cpqScsiCntlrTimeouts=_CpqScsiCntlrTimeouts_Object((1,3,6,1,4,1,232,5,2,2,1,1,10),_CpqScsiCntlrTimeouts_Type())
cpqScsiCntlrTimeouts.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrTimeouts.setStatus(_B)
_CpqScsiCntlrBaseIOAddr_Type=Integer32
_CpqScsiCntlrBaseIOAddr_Object=MibTableColumn
cpqScsiCntlrBaseIOAddr=_CpqScsiCntlrBaseIOAddr_Object((1,3,6,1,4,1,232,5,2,2,1,1,11),_CpqScsiCntlrBaseIOAddr_Type())
cpqScsiCntlrBaseIOAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrBaseIOAddr.setStatus(_B)
class _CpqScsiCntlrCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_N,3),(_M,4)))
_CpqScsiCntlrCondition_Type.__name__=_D
_CpqScsiCntlrCondition_Object=MibTableColumn
cpqScsiCntlrCondition=_CpqScsiCntlrCondition_Object((1,3,6,1,4,1,232,5,2,2,1,1,12),_CpqScsiCntlrCondition_Type())
cpqScsiCntlrCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrCondition.setStatus(_B)
class _CpqScsiCntlrSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqScsiCntlrSerialNum_Type.__name__=_F
_CpqScsiCntlrSerialNum_Object=MibTableColumn
cpqScsiCntlrSerialNum=_CpqScsiCntlrSerialNum_Object((1,3,6,1,4,1,232,5,2,2,1,1,13),_CpqScsiCntlrSerialNum_Type())
cpqScsiCntlrSerialNum.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrSerialNum.setStatus(_B)
class _CpqScsiCntlrBusWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('narrow',2),('wide16',3)))
_CpqScsiCntlrBusWidth_Type.__name__=_D
_CpqScsiCntlrBusWidth_Object=MibTableColumn
cpqScsiCntlrBusWidth=_CpqScsiCntlrBusWidth_Object((1,3,6,1,4,1,232,5,2,2,1,1,14),_CpqScsiCntlrBusWidth_Type())
cpqScsiCntlrBusWidth.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrBusWidth.setStatus(_B)
class _CpqScsiCntlrModelExtended_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CpqScsiCntlrModelExtended_Type.__name__=_F
_CpqScsiCntlrModelExtended_Object=MibTableColumn
cpqScsiCntlrModelExtended=_CpqScsiCntlrModelExtended_Object((1,3,6,1,4,1,232,5,2,2,1,1,15),_CpqScsiCntlrModelExtended_Type())
cpqScsiCntlrModelExtended.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrModelExtended.setStatus(_B)
class _CpqScsiCntlrHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqScsiCntlrHwLocation_Type.__name__=_F
_CpqScsiCntlrHwLocation_Object=MibTableColumn
cpqScsiCntlrHwLocation=_CpqScsiCntlrHwLocation_Object((1,3,6,1,4,1,232,5,2,2,1,1,16),_CpqScsiCntlrHwLocation_Type())
cpqScsiCntlrHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrHwLocation.setStatus(_V)
class _CpqScsiCntlrPciLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqScsiCntlrPciLocation_Type.__name__=_F
_CpqScsiCntlrPciLocation_Object=MibTableColumn
cpqScsiCntlrPciLocation=_CpqScsiCntlrPciLocation_Object((1,3,6,1,4,1,232,5,2,2,1,1,17),_CpqScsiCntlrPciLocation_Type())
cpqScsiCntlrPciLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCntlrPciLocation.setStatus(_V)
_CpqScsiLogDrv_ObjectIdentity=ObjectIdentity
cpqScsiLogDrv=_CpqScsiLogDrv_ObjectIdentity((1,3,6,1,4,1,232,5,2,3))
_CpqScsiLogDrvTable_Object=MibTable
cpqScsiLogDrvTable=_CpqScsiLogDrvTable_Object((1,3,6,1,4,1,232,5,2,3,1))
if mibBuilder.loadTexts:cpqScsiLogDrvTable.setStatus(_B)
_CpqScsiLogDrvEntry_Object=MibTableRow
cpqScsiLogDrvEntry=_CpqScsiLogDrvEntry_Object((1,3,6,1,4,1,232,5,2,3,1,1))
cpqScsiLogDrvEntry.setIndexNames((0,_C,_g),(0,_C,_h),(0,_C,_i))
if mibBuilder.loadTexts:cpqScsiLogDrvEntry.setStatus(_B)
_CpqScsiLogDrvCntlrIndex_Type=Integer32
_CpqScsiLogDrvCntlrIndex_Object=MibTableColumn
cpqScsiLogDrvCntlrIndex=_CpqScsiLogDrvCntlrIndex_Object((1,3,6,1,4,1,232,5,2,3,1,1,1),_CpqScsiLogDrvCntlrIndex_Type())
cpqScsiLogDrvCntlrIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiLogDrvCntlrIndex.setStatus(_B)
class _CpqScsiLogDrvBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiLogDrvBusIndex_Type.__name__=_D
_CpqScsiLogDrvBusIndex_Object=MibTableColumn
cpqScsiLogDrvBusIndex=_CpqScsiLogDrvBusIndex_Object((1,3,6,1,4,1,232,5,2,3,1,1,2),_CpqScsiLogDrvBusIndex_Type())
cpqScsiLogDrvBusIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiLogDrvBusIndex.setStatus(_B)
class _CpqScsiLogDrvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiLogDrvIndex_Type.__name__=_D
_CpqScsiLogDrvIndex_Object=MibTableColumn
cpqScsiLogDrvIndex=_CpqScsiLogDrvIndex_Object((1,3,6,1,4,1,232,5,2,3,1,1,3),_CpqScsiLogDrvIndex_Type())
cpqScsiLogDrvIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiLogDrvIndex.setStatus(_B)
class _CpqScsiLogDrvFaultTol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('none',2),('mirroring',3),('dataGuard',4),('distribDataGuard',5),('enhancedMirroring',6)))
_CpqScsiLogDrvFaultTol_Type.__name__=_D
_CpqScsiLogDrvFaultTol_Object=MibTableColumn
cpqScsiLogDrvFaultTol=_CpqScsiLogDrvFaultTol_Object((1,3,6,1,4,1,232,5,2,3,1,1,4),_CpqScsiLogDrvFaultTol_Type())
cpqScsiLogDrvFaultTol.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiLogDrvFaultTol.setStatus(_B)
class _CpqScsiLogDrvStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_G,1),(_H,2),(_M,3),('unconfigured',4),('recovering',5),('readyForRebuild',6),(_AS,7),('wrongDrive',8),('badConnect',9),(_N,10),('disabled',11)))
_CpqScsiLogDrvStatus_Type.__name__=_D
_CpqScsiLogDrvStatus_Object=MibTableColumn
cpqScsiLogDrvStatus=_CpqScsiLogDrvStatus_Object((1,3,6,1,4,1,232,5,2,3,1,1,5),_CpqScsiLogDrvStatus_Type())
cpqScsiLogDrvStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiLogDrvStatus.setStatus(_B)
class _CpqScsiLogDrvSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqScsiLogDrvSize_Type.__name__=_D
_CpqScsiLogDrvSize_Object=MibTableColumn
cpqScsiLogDrvSize=_CpqScsiLogDrvSize_Object((1,3,6,1,4,1,232,5,2,3,1,1,6),_CpqScsiLogDrvSize_Type())
cpqScsiLogDrvSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiLogDrvSize.setStatus(_B)
class _CpqScsiLogDrvPhyDrvIDs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqScsiLogDrvPhyDrvIDs_Type.__name__=_O
_CpqScsiLogDrvPhyDrvIDs_Object=MibTableColumn
cpqScsiLogDrvPhyDrvIDs=_CpqScsiLogDrvPhyDrvIDs_Object((1,3,6,1,4,1,232,5,2,3,1,1,7),_CpqScsiLogDrvPhyDrvIDs_Type())
cpqScsiLogDrvPhyDrvIDs.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiLogDrvPhyDrvIDs.setStatus(_B)
class _CpqScsiLogDrvCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_N,3),(_M,4)))
_CpqScsiLogDrvCondition_Type.__name__=_D
_CpqScsiLogDrvCondition_Object=MibTableColumn
cpqScsiLogDrvCondition=_CpqScsiLogDrvCondition_Object((1,3,6,1,4,1,232,5,2,3,1,1,8),_CpqScsiLogDrvCondition_Type())
cpqScsiLogDrvCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiLogDrvCondition.setStatus(_B)
_CpqScsiLogDrvStripeSize_Type=Integer32
_CpqScsiLogDrvStripeSize_Object=MibTableColumn
cpqScsiLogDrvStripeSize=_CpqScsiLogDrvStripeSize_Object((1,3,6,1,4,1,232,5,2,3,1,1,9),_CpqScsiLogDrvStripeSize_Type())
cpqScsiLogDrvStripeSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiLogDrvStripeSize.setStatus(_B)
class _CpqScsiLogDrvAvailSpares_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqScsiLogDrvAvailSpares_Type.__name__=_O
_CpqScsiLogDrvAvailSpares_Object=MibTableColumn
cpqScsiLogDrvAvailSpares=_CpqScsiLogDrvAvailSpares_Object((1,3,6,1,4,1,232,5,2,3,1,1,10),_CpqScsiLogDrvAvailSpares_Type())
cpqScsiLogDrvAvailSpares.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiLogDrvAvailSpares.setStatus(_B)
_CpqScsiLogDrvPercentRebuild_Type=Gauge32
_CpqScsiLogDrvPercentRebuild_Object=MibTableColumn
cpqScsiLogDrvPercentRebuild=_CpqScsiLogDrvPercentRebuild_Object((1,3,6,1,4,1,232,5,2,3,1,1,11),_CpqScsiLogDrvPercentRebuild_Type())
cpqScsiLogDrvPercentRebuild.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiLogDrvPercentRebuild.setStatus(_B)
class _CpqScsiLogDrvOsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqScsiLogDrvOsName_Type.__name__=_F
_CpqScsiLogDrvOsName_Object=MibTableColumn
cpqScsiLogDrvOsName=_CpqScsiLogDrvOsName_Object((1,3,6,1,4,1,232,5,2,3,1,1,12),_CpqScsiLogDrvOsName_Type())
cpqScsiLogDrvOsName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiLogDrvOsName.setStatus(_B)
_CpqScsiPhyDrv_ObjectIdentity=ObjectIdentity
cpqScsiPhyDrv=_CpqScsiPhyDrv_ObjectIdentity((1,3,6,1,4,1,232,5,2,4))
_CpqScsiPhyDrvTable_Object=MibTable
cpqScsiPhyDrvTable=_CpqScsiPhyDrvTable_Object((1,3,6,1,4,1,232,5,2,4,1))
if mibBuilder.loadTexts:cpqScsiPhyDrvTable.setStatus(_B)
_CpqScsiPhyDrvEntry_Object=MibTableRow
cpqScsiPhyDrvEntry=_CpqScsiPhyDrvEntry_Object((1,3,6,1,4,1,232,5,2,4,1,1))
cpqScsiPhyDrvEntry.setIndexNames((0,_C,_W),(0,_C,_X),(0,_C,_Y))
if mibBuilder.loadTexts:cpqScsiPhyDrvEntry.setStatus(_B)
_CpqScsiPhyDrvCntlrIndex_Type=Integer32
_CpqScsiPhyDrvCntlrIndex_Object=MibTableColumn
cpqScsiPhyDrvCntlrIndex=_CpqScsiPhyDrvCntlrIndex_Object((1,3,6,1,4,1,232,5,2,4,1,1,1),_CpqScsiPhyDrvCntlrIndex_Type())
cpqScsiPhyDrvCntlrIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvCntlrIndex.setStatus(_B)
class _CpqScsiPhyDrvBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiPhyDrvBusIndex_Type.__name__=_D
_CpqScsiPhyDrvBusIndex_Object=MibTableColumn
cpqScsiPhyDrvBusIndex=_CpqScsiPhyDrvBusIndex_Object((1,3,6,1,4,1,232,5,2,4,1,1,2),_CpqScsiPhyDrvBusIndex_Type())
cpqScsiPhyDrvBusIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvBusIndex.setStatus(_B)
class _CpqScsiPhyDrvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiPhyDrvIndex_Type.__name__=_D
_CpqScsiPhyDrvIndex_Object=MibTableColumn
cpqScsiPhyDrvIndex=_CpqScsiPhyDrvIndex_Object((1,3,6,1,4,1,232,5,2,4,1,1,3),_CpqScsiPhyDrvIndex_Type())
cpqScsiPhyDrvIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvIndex.setStatus(_B)
class _CpqScsiPhyDrvModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_CpqScsiPhyDrvModel_Type.__name__=_F
_CpqScsiPhyDrvModel_Object=MibTableColumn
cpqScsiPhyDrvModel=_CpqScsiPhyDrvModel_Object((1,3,6,1,4,1,232,5,2,4,1,1,4),_CpqScsiPhyDrvModel_Type())
cpqScsiPhyDrvModel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvModel.setStatus(_B)
class _CpqScsiPhyDrvFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqScsiPhyDrvFWRev_Type.__name__=_F
_CpqScsiPhyDrvFWRev_Object=MibTableColumn
cpqScsiPhyDrvFWRev=_CpqScsiPhyDrvFWRev_Object((1,3,6,1,4,1,232,5,2,4,1,1,5),_CpqScsiPhyDrvFWRev_Type())
cpqScsiPhyDrvFWRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvFWRev.setStatus(_B)
class _CpqScsiPhyDrvVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_CpqScsiPhyDrvVendor_Type.__name__=_F
_CpqScsiPhyDrvVendor_Object=MibTableColumn
cpqScsiPhyDrvVendor=_CpqScsiPhyDrvVendor_Object((1,3,6,1,4,1,232,5,2,4,1,1,6),_CpqScsiPhyDrvVendor_Type())
cpqScsiPhyDrvVendor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvVendor.setStatus(_B)
class _CpqScsiPhyDrvSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqScsiPhyDrvSize_Type.__name__=_D
_CpqScsiPhyDrvSize_Object=MibTableColumn
cpqScsiPhyDrvSize=_CpqScsiPhyDrvSize_Object((1,3,6,1,4,1,232,5,2,4,1,1,7),_CpqScsiPhyDrvSize_Type())
cpqScsiPhyDrvSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvSize.setStatus(_B)
class _CpqScsiPhyDrvScsiID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiPhyDrvScsiID_Type.__name__=_D
_CpqScsiPhyDrvScsiID_Object=MibTableColumn
cpqScsiPhyDrvScsiID=_CpqScsiPhyDrvScsiID_Object((1,3,6,1,4,1,232,5,2,4,1,1,8),_CpqScsiPhyDrvScsiID_Type())
cpqScsiPhyDrvScsiID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvScsiID.setStatus(_B)
class _CpqScsiPhyDrvStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_G,1),(_H,2),(_M,3),('notConfigured',4),('badCable',5),(_j,6),(_k,7),(_AT,8),(_AU,9),(_P,10),(_l,11),('hardError',12)))
_CpqScsiPhyDrvStatus_Type.__name__=_D
_CpqScsiPhyDrvStatus_Object=MibTableColumn
cpqScsiPhyDrvStatus=_CpqScsiPhyDrvStatus_Object((1,3,6,1,4,1,232,5,2,4,1,1,9),_CpqScsiPhyDrvStatus_Type())
cpqScsiPhyDrvStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvStatus.setStatus(_B)
_CpqScsiPhyDrvServiceHours_Type=Counter32
_CpqScsiPhyDrvServiceHours_Object=MibTableColumn
cpqScsiPhyDrvServiceHours=_CpqScsiPhyDrvServiceHours_Object((1,3,6,1,4,1,232,5,2,4,1,1,10),_CpqScsiPhyDrvServiceHours_Type())
cpqScsiPhyDrvServiceHours.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvServiceHours.setStatus(_B)
_CpqScsiPhyDrvHighReadSectors_Type=Counter32
_CpqScsiPhyDrvHighReadSectors_Object=MibTableColumn
cpqScsiPhyDrvHighReadSectors=_CpqScsiPhyDrvHighReadSectors_Object((1,3,6,1,4,1,232,5,2,4,1,1,11),_CpqScsiPhyDrvHighReadSectors_Type())
cpqScsiPhyDrvHighReadSectors.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvHighReadSectors.setStatus(_B)
_CpqScsiPhyDrvLowReadSectors_Type=Counter32
_CpqScsiPhyDrvLowReadSectors_Object=MibTableColumn
cpqScsiPhyDrvLowReadSectors=_CpqScsiPhyDrvLowReadSectors_Object((1,3,6,1,4,1,232,5,2,4,1,1,12),_CpqScsiPhyDrvLowReadSectors_Type())
cpqScsiPhyDrvLowReadSectors.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvLowReadSectors.setStatus(_B)
_CpqScsiPhyDrvHighWriteSectors_Type=Counter32
_CpqScsiPhyDrvHighWriteSectors_Object=MibTableColumn
cpqScsiPhyDrvHighWriteSectors=_CpqScsiPhyDrvHighWriteSectors_Object((1,3,6,1,4,1,232,5,2,4,1,1,13),_CpqScsiPhyDrvHighWriteSectors_Type())
cpqScsiPhyDrvHighWriteSectors.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvHighWriteSectors.setStatus(_B)
_CpqScsiPhyDrvLowWriteSectors_Type=Counter32
_CpqScsiPhyDrvLowWriteSectors_Object=MibTableColumn
cpqScsiPhyDrvLowWriteSectors=_CpqScsiPhyDrvLowWriteSectors_Object((1,3,6,1,4,1,232,5,2,4,1,1,14),_CpqScsiPhyDrvLowWriteSectors_Type())
cpqScsiPhyDrvLowWriteSectors.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvLowWriteSectors.setStatus(_B)
_CpqScsiPhyDrvHardReadErrs_Type=Counter32
_CpqScsiPhyDrvHardReadErrs_Object=MibTableColumn
cpqScsiPhyDrvHardReadErrs=_CpqScsiPhyDrvHardReadErrs_Object((1,3,6,1,4,1,232,5,2,4,1,1,15),_CpqScsiPhyDrvHardReadErrs_Type())
cpqScsiPhyDrvHardReadErrs.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvHardReadErrs.setStatus(_B)
_CpqScsiPhyDrvHardWriteErrs_Type=Counter32
_CpqScsiPhyDrvHardWriteErrs_Object=MibTableColumn
cpqScsiPhyDrvHardWriteErrs=_CpqScsiPhyDrvHardWriteErrs_Object((1,3,6,1,4,1,232,5,2,4,1,1,16),_CpqScsiPhyDrvHardWriteErrs_Type())
cpqScsiPhyDrvHardWriteErrs.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvHardWriteErrs.setStatus(_B)
_CpqScsiPhyDrvEccCorrReads_Type=Counter32
_CpqScsiPhyDrvEccCorrReads_Object=MibTableColumn
cpqScsiPhyDrvEccCorrReads=_CpqScsiPhyDrvEccCorrReads_Object((1,3,6,1,4,1,232,5,2,4,1,1,17),_CpqScsiPhyDrvEccCorrReads_Type())
cpqScsiPhyDrvEccCorrReads.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvEccCorrReads.setStatus(_B)
_CpqScsiPhyDrvRecvReadErrs_Type=Counter32
_CpqScsiPhyDrvRecvReadErrs_Object=MibTableColumn
cpqScsiPhyDrvRecvReadErrs=_CpqScsiPhyDrvRecvReadErrs_Object((1,3,6,1,4,1,232,5,2,4,1,1,18),_CpqScsiPhyDrvRecvReadErrs_Type())
cpqScsiPhyDrvRecvReadErrs.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvRecvReadErrs.setStatus(_B)
_CpqScsiPhyDrvRecvWriteErrs_Type=Counter32
_CpqScsiPhyDrvRecvWriteErrs_Object=MibTableColumn
cpqScsiPhyDrvRecvWriteErrs=_CpqScsiPhyDrvRecvWriteErrs_Object((1,3,6,1,4,1,232,5,2,4,1,1,19),_CpqScsiPhyDrvRecvWriteErrs_Type())
cpqScsiPhyDrvRecvWriteErrs.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvRecvWriteErrs.setStatus(_B)
_CpqScsiPhyDrvSeekErrs_Type=Counter32
_CpqScsiPhyDrvSeekErrs_Object=MibTableColumn
cpqScsiPhyDrvSeekErrs=_CpqScsiPhyDrvSeekErrs_Object((1,3,6,1,4,1,232,5,2,4,1,1,20),_CpqScsiPhyDrvSeekErrs_Type())
cpqScsiPhyDrvSeekErrs.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvSeekErrs.setStatus(_B)
_CpqScsiPhyDrvSpinupTime_Type=Integer32
_CpqScsiPhyDrvSpinupTime_Object=MibTableColumn
cpqScsiPhyDrvSpinupTime=_CpqScsiPhyDrvSpinupTime_Object((1,3,6,1,4,1,232,5,2,4,1,1,21),_CpqScsiPhyDrvSpinupTime_Type())
cpqScsiPhyDrvSpinupTime.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvSpinupTime.setStatus(_B)
_CpqScsiPhyDrvUsedReallocs_Type=Counter32
_CpqScsiPhyDrvUsedReallocs_Object=MibTableColumn
cpqScsiPhyDrvUsedReallocs=_CpqScsiPhyDrvUsedReallocs_Object((1,3,6,1,4,1,232,5,2,4,1,1,22),_CpqScsiPhyDrvUsedReallocs_Type())
cpqScsiPhyDrvUsedReallocs.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvUsedReallocs.setStatus(_B)
_CpqScsiPhyDrvTimeouts_Type=Counter32
_CpqScsiPhyDrvTimeouts_Object=MibTableColumn
cpqScsiPhyDrvTimeouts=_CpqScsiPhyDrvTimeouts_Object((1,3,6,1,4,1,232,5,2,4,1,1,23),_CpqScsiPhyDrvTimeouts_Type())
cpqScsiPhyDrvTimeouts.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvTimeouts.setStatus(_B)
_CpqScsiPhyDrvPostErrs_Type=Counter32
_CpqScsiPhyDrvPostErrs_Object=MibTableColumn
cpqScsiPhyDrvPostErrs=_CpqScsiPhyDrvPostErrs_Object((1,3,6,1,4,1,232,5,2,4,1,1,24),_CpqScsiPhyDrvPostErrs_Type())
cpqScsiPhyDrvPostErrs.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvPostErrs.setStatus(_B)
_CpqScsiPhyDrvPostErrCode_Type=Integer32
_CpqScsiPhyDrvPostErrCode_Object=MibTableColumn
cpqScsiPhyDrvPostErrCode=_CpqScsiPhyDrvPostErrCode_Object((1,3,6,1,4,1,232,5,2,4,1,1,25),_CpqScsiPhyDrvPostErrCode_Type())
cpqScsiPhyDrvPostErrCode.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvPostErrCode.setStatus(_B)
class _CpqScsiPhyDrvCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_N,3),(_M,4)))
_CpqScsiPhyDrvCondition_Type.__name__=_D
_CpqScsiPhyDrvCondition_Object=MibTableColumn
cpqScsiPhyDrvCondition=_CpqScsiPhyDrvCondition_Object((1,3,6,1,4,1,232,5,2,4,1,1,26),_CpqScsiPhyDrvCondition_Type())
cpqScsiPhyDrvCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvCondition.setStatus(_B)
_CpqScsiPhyDrvFuncTest1_Type=Gauge32
_CpqScsiPhyDrvFuncTest1_Object=MibTableColumn
cpqScsiPhyDrvFuncTest1=_CpqScsiPhyDrvFuncTest1_Object((1,3,6,1,4,1,232,5,2,4,1,1,27),_CpqScsiPhyDrvFuncTest1_Type())
cpqScsiPhyDrvFuncTest1.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvFuncTest1.setStatus(_B)
_CpqScsiPhyDrvFuncTest2_Type=Gauge32
_CpqScsiPhyDrvFuncTest2_Object=MibTableColumn
cpqScsiPhyDrvFuncTest2=_CpqScsiPhyDrvFuncTest2_Object((1,3,6,1,4,1,232,5,2,4,1,1,28),_CpqScsiPhyDrvFuncTest2_Type())
cpqScsiPhyDrvFuncTest2.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvFuncTest2.setStatus(_B)
class _CpqScsiPhyDrvStatsPreserved_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,1),('inNVRAM',2),('onDisk',3),('noCPUSupport',4),('noFreeNVRAM',5),('noDrvSupport',6),('noSoftwareSupport',7),('statsNotSupported',8)))
_CpqScsiPhyDrvStatsPreserved_Type.__name__=_D
_CpqScsiPhyDrvStatsPreserved_Object=MibTableColumn
cpqScsiPhyDrvStatsPreserved=_CpqScsiPhyDrvStatsPreserved_Object((1,3,6,1,4,1,232,5,2,4,1,1,29),_CpqScsiPhyDrvStatsPreserved_Type())
cpqScsiPhyDrvStatsPreserved.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvStatsPreserved.setStatus(_B)
class _CpqScsiPhyDrvSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CpqScsiPhyDrvSerialNum_Type.__name__=_F
_CpqScsiPhyDrvSerialNum_Object=MibTableColumn
cpqScsiPhyDrvSerialNum=_CpqScsiPhyDrvSerialNum_Object((1,3,6,1,4,1,232,5,2,4,1,1,30),_CpqScsiPhyDrvSerialNum_Type())
cpqScsiPhyDrvSerialNum.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvSerialNum.setStatus(_B)
class _CpqScsiPhyDrvLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_m,2)))
_CpqScsiPhyDrvLocation_Type.__name__=_D
_CpqScsiPhyDrvLocation_Object=MibTableColumn
cpqScsiPhyDrvLocation=_CpqScsiPhyDrvLocation_Object((1,3,6,1,4,1,232,5,2,4,1,1,31),_CpqScsiPhyDrvLocation_Type())
cpqScsiPhyDrvLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvLocation.setStatus(_E)
class _CpqScsiPhyDrvParent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiPhyDrvParent_Type.__name__=_D
_CpqScsiPhyDrvParent_Object=MibTableColumn
cpqScsiPhyDrvParent=_CpqScsiPhyDrvParent_Object((1,3,6,1,4,1,232,5,2,4,1,1,32),_CpqScsiPhyDrvParent_Type())
cpqScsiPhyDrvParent.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvParent.setStatus(_B)
class _CpqScsiPhyDrvSectorSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqScsiPhyDrvSectorSize_Type.__name__=_D
_CpqScsiPhyDrvSectorSize_Object=MibTableColumn
cpqScsiPhyDrvSectorSize=_CpqScsiPhyDrvSectorSize_Object((1,3,6,1,4,1,232,5,2,4,1,1,33),_CpqScsiPhyDrvSectorSize_Type())
cpqScsiPhyDrvSectorSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvSectorSize.setStatus(_B)
class _CpqScsiPhyDrvHotPlug_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_n,2),(_o,3)))
_CpqScsiPhyDrvHotPlug_Type.__name__=_D
_CpqScsiPhyDrvHotPlug_Object=MibTableColumn
cpqScsiPhyDrvHotPlug=_CpqScsiPhyDrvHotPlug_Object((1,3,6,1,4,1,232,5,2,4,1,1,34),_CpqScsiPhyDrvHotPlug_Type())
cpqScsiPhyDrvHotPlug.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvHotPlug.setStatus(_B)
class _CpqScsiPhyDrvPlacement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_p,2),(_q,3)))
_CpqScsiPhyDrvPlacement_Type.__name__=_D
_CpqScsiPhyDrvPlacement_Object=MibTableColumn
cpqScsiPhyDrvPlacement=_CpqScsiPhyDrvPlacement_Object((1,3,6,1,4,1,232,5,2,4,1,1,35),_CpqScsiPhyDrvPlacement_Type())
cpqScsiPhyDrvPlacement.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvPlacement.setStatus(_B)
class _CpqScsiPhyDrvPreFailMonitoring_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('notAvailable',2),('available',3)))
_CpqScsiPhyDrvPreFailMonitoring_Type.__name__=_D
_CpqScsiPhyDrvPreFailMonitoring_Object=MibTableColumn
cpqScsiPhyDrvPreFailMonitoring=_CpqScsiPhyDrvPreFailMonitoring_Object((1,3,6,1,4,1,232,5,2,4,1,1,36),_CpqScsiPhyDrvPreFailMonitoring_Type())
cpqScsiPhyDrvPreFailMonitoring.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvPreFailMonitoring.setStatus(_B)
class _CpqScsiPhyDrvOsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqScsiPhyDrvOsName_Type.__name__=_F
_CpqScsiPhyDrvOsName_Object=MibTableColumn
cpqScsiPhyDrvOsName=_CpqScsiPhyDrvOsName_Object((1,3,6,1,4,1,232,5,2,4,1,1,37),_CpqScsiPhyDrvOsName_Type())
cpqScsiPhyDrvOsName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvOsName.setStatus(_B)
class _CpqScsiPhyDrvRotationalSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('rpm7200',2),('rpm10K',3),('rpm15K',4)))
_CpqScsiPhyDrvRotationalSpeed_Type.__name__=_D
_CpqScsiPhyDrvRotationalSpeed_Object=MibTableColumn
cpqScsiPhyDrvRotationalSpeed=_CpqScsiPhyDrvRotationalSpeed_Object((1,3,6,1,4,1,232,5,2,4,1,1,38),_CpqScsiPhyDrvRotationalSpeed_Type())
cpqScsiPhyDrvRotationalSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvRotationalSpeed.setStatus(_B)
class _CpqScsiPhyDrvMemberLogDrv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('member',2),('spare',3),(_AV,4)))
_CpqScsiPhyDrvMemberLogDrv_Type.__name__=_D
_CpqScsiPhyDrvMemberLogDrv_Object=MibTableColumn
cpqScsiPhyDrvMemberLogDrv=_CpqScsiPhyDrvMemberLogDrv_Object((1,3,6,1,4,1,232,5,2,4,1,1,39),_CpqScsiPhyDrvMemberLogDrv_Type())
cpqScsiPhyDrvMemberLogDrv.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiPhyDrvMemberLogDrv.setStatus(_B)
_CpqScsiTarget_ObjectIdentity=ObjectIdentity
cpqScsiTarget=_CpqScsiTarget_ObjectIdentity((1,3,6,1,4,1,232,5,2,5))
_CpqScsiTargetTable_Object=MibTable
cpqScsiTargetTable=_CpqScsiTargetTable_Object((1,3,6,1,4,1,232,5,2,5,1))
if mibBuilder.loadTexts:cpqScsiTargetTable.setStatus(_B)
_CpqScsiTargetEntry_Object=MibTableRow
cpqScsiTargetEntry=_CpqScsiTargetEntry_Object((1,3,6,1,4,1,232,5,2,5,1,1))
cpqScsiTargetEntry.setIndexNames((0,_C,_AW),(0,_C,_AX),(0,_C,_AY))
if mibBuilder.loadTexts:cpqScsiTargetEntry.setStatus(_B)
_CpqScsiTargetCntlrIndex_Type=Integer32
_CpqScsiTargetCntlrIndex_Object=MibTableColumn
cpqScsiTargetCntlrIndex=_CpqScsiTargetCntlrIndex_Object((1,3,6,1,4,1,232,5,2,5,1,1,1),_CpqScsiTargetCntlrIndex_Type())
cpqScsiTargetCntlrIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetCntlrIndex.setStatus(_B)
class _CpqScsiTargetBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiTargetBusIndex_Type.__name__=_D
_CpqScsiTargetBusIndex_Object=MibTableColumn
cpqScsiTargetBusIndex=_CpqScsiTargetBusIndex_Object((1,3,6,1,4,1,232,5,2,5,1,1,2),_CpqScsiTargetBusIndex_Type())
cpqScsiTargetBusIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetBusIndex.setStatus(_B)
class _CpqScsiTargetScsiIdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiTargetScsiIdIndex_Type.__name__=_D
_CpqScsiTargetScsiIdIndex_Object=MibTableColumn
cpqScsiTargetScsiIdIndex=_CpqScsiTargetScsiIdIndex_Object((1,3,6,1,4,1,232,5,2,5,1,1,3),_CpqScsiTargetScsiIdIndex_Type())
cpqScsiTargetScsiIdIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetScsiIdIndex.setStatus(_B)
class _CpqScsiTargetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_G,1),('disk',2),('tape',3),('printer',4),(_AZ,5),(_Aa,6),('cd-rom',7),('scanner',8),('optical',9),('jukeBox',10),('commDev',11)))
_CpqScsiTargetType_Type.__name__=_D
_CpqScsiTargetType_Object=MibTableColumn
cpqScsiTargetType=_CpqScsiTargetType_Object((1,3,6,1,4,1,232,5,2,5,1,1,4),_CpqScsiTargetType_Type())
cpqScsiTargetType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetType.setStatus(_B)
class _CpqScsiTargetModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_CpqScsiTargetModel_Type.__name__=_F
_CpqScsiTargetModel_Object=MibTableColumn
cpqScsiTargetModel=_CpqScsiTargetModel_Object((1,3,6,1,4,1,232,5,2,5,1,1,5),_CpqScsiTargetModel_Type())
cpqScsiTargetModel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetModel.setStatus(_B)
class _CpqScsiTargetFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqScsiTargetFWRev_Type.__name__=_F
_CpqScsiTargetFWRev_Object=MibTableColumn
cpqScsiTargetFWRev=_CpqScsiTargetFWRev_Object((1,3,6,1,4,1,232,5,2,5,1,1,6),_CpqScsiTargetFWRev_Type())
cpqScsiTargetFWRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetFWRev.setStatus(_B)
class _CpqScsiTargetVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_CpqScsiTargetVendor_Type.__name__=_F
_CpqScsiTargetVendor_Object=MibTableColumn
cpqScsiTargetVendor=_CpqScsiTargetVendor_Object((1,3,6,1,4,1,232,5,2,5,1,1,7),_CpqScsiTargetVendor_Type())
cpqScsiTargetVendor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetVendor.setStatus(_B)
_CpqScsiTargetParityErrs_Type=Counter32
_CpqScsiTargetParityErrs_Object=MibTableColumn
cpqScsiTargetParityErrs=_CpqScsiTargetParityErrs_Object((1,3,6,1,4,1,232,5,2,5,1,1,8),_CpqScsiTargetParityErrs_Type())
cpqScsiTargetParityErrs.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetParityErrs.setStatus(_B)
_CpqScsiTargetPhaseErrs_Type=Counter32
_CpqScsiTargetPhaseErrs_Object=MibTableColumn
cpqScsiTargetPhaseErrs=_CpqScsiTargetPhaseErrs_Object((1,3,6,1,4,1,232,5,2,5,1,1,9),_CpqScsiTargetPhaseErrs_Type())
cpqScsiTargetPhaseErrs.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetPhaseErrs.setStatus(_B)
_CpqScsiTargetSelectTimeouts_Type=Counter32
_CpqScsiTargetSelectTimeouts_Object=MibTableColumn
cpqScsiTargetSelectTimeouts=_CpqScsiTargetSelectTimeouts_Object((1,3,6,1,4,1,232,5,2,5,1,1,10),_CpqScsiTargetSelectTimeouts_Type())
cpqScsiTargetSelectTimeouts.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetSelectTimeouts.setStatus(_B)
_CpqScsiTargetMsgRejects_Type=Counter32
_CpqScsiTargetMsgRejects_Object=MibTableColumn
cpqScsiTargetMsgRejects=_CpqScsiTargetMsgRejects_Object((1,3,6,1,4,1,232,5,2,5,1,1,11),_CpqScsiTargetMsgRejects_Type())
cpqScsiTargetMsgRejects.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetMsgRejects.setStatus(_B)
class _CpqScsiTargetNegPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqScsiTargetNegPeriod_Type.__name__=_D
_CpqScsiTargetNegPeriod_Object=MibTableColumn
cpqScsiTargetNegPeriod=_CpqScsiTargetNegPeriod_Object((1,3,6,1,4,1,232,5,2,5,1,1,12),_CpqScsiTargetNegPeriod_Type())
cpqScsiTargetNegPeriod.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetNegPeriod.setStatus(_E)
class _CpqScsiTargetLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_m,2)))
_CpqScsiTargetLocation_Type.__name__=_D
_CpqScsiTargetLocation_Object=MibTableColumn
cpqScsiTargetLocation=_CpqScsiTargetLocation_Object((1,3,6,1,4,1,232,5,2,5,1,1,13),_CpqScsiTargetLocation_Type())
cpqScsiTargetLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetLocation.setStatus(_B)
_CpqScsiTargetNegSpeed_Type=Integer32
_CpqScsiTargetNegSpeed_Object=MibTableColumn
cpqScsiTargetNegSpeed=_CpqScsiTargetNegSpeed_Object((1,3,6,1,4,1,232,5,2,5,1,1,14),_CpqScsiTargetNegSpeed_Type())
cpqScsiTargetNegSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetNegSpeed.setStatus(_B)
class _CpqScsiTargetPhysWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('narrow',2),('wide16',3)))
_CpqScsiTargetPhysWidth_Type.__name__=_D
_CpqScsiTargetPhysWidth_Object=MibTableColumn
cpqScsiTargetPhysWidth=_CpqScsiTargetPhysWidth_Object((1,3,6,1,4,1,232,5,2,5,1,1,15),_CpqScsiTargetPhysWidth_Type())
cpqScsiTargetPhysWidth.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetPhysWidth.setStatus(_B)
_CpqScsiTargetNegWidth_Type=Integer32
_CpqScsiTargetNegWidth_Object=MibTableColumn
cpqScsiTargetNegWidth=_CpqScsiTargetNegWidth_Object((1,3,6,1,4,1,232,5,2,5,1,1,16),_CpqScsiTargetNegWidth_Type())
cpqScsiTargetNegWidth.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetNegWidth.setStatus(_B)
class _CpqScsiTargetTypeExtended_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),('pdcd',2),('removableDisk',3),('dltAutoloader',4),('cdJukebox',5),('cr3500',6),('autoloader',7)))
_CpqScsiTargetTypeExtended_Type.__name__=_D
_CpqScsiTargetTypeExtended_Object=MibTableColumn
cpqScsiTargetTypeExtended=_CpqScsiTargetTypeExtended_Object((1,3,6,1,4,1,232,5,2,5,1,1,17),_CpqScsiTargetTypeExtended_Type())
cpqScsiTargetTypeExtended.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetTypeExtended.setStatus(_B)
class _CpqScsiTargetCurrentSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,1),('asynchronous',2),('fast',3),('ultra',4),('ultra2',5),('ultra3',6),('scsi1',7),('ultra4',8)))
_CpqScsiTargetCurrentSpeed_Type.__name__=_D
_CpqScsiTargetCurrentSpeed_Object=MibTableColumn
cpqScsiTargetCurrentSpeed=_CpqScsiTargetCurrentSpeed_Object((1,3,6,1,4,1,232,5,2,5,1,1,18),_CpqScsiTargetCurrentSpeed_Type())
cpqScsiTargetCurrentSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTargetCurrentSpeed.setStatus(_B)
_CpqScsiCd_ObjectIdentity=ObjectIdentity
cpqScsiCd=_CpqScsiCd_ObjectIdentity((1,3,6,1,4,1,232,5,2,6))
_CpqScsiCdDrvTable_Object=MibTable
cpqScsiCdDrvTable=_CpqScsiCdDrvTable_Object((1,3,6,1,4,1,232,5,2,6,1))
if mibBuilder.loadTexts:cpqScsiCdDrvTable.setStatus(_B)
_CpqScsiCdDrvEntry_Object=MibTableRow
cpqScsiCdDrvEntry=_CpqScsiCdDrvEntry_Object((1,3,6,1,4,1,232,5,2,6,1,1))
cpqScsiCdDrvEntry.setIndexNames((0,_C,_Ab),(0,_C,_Ac),(0,_C,_Ad),(0,_C,_Ae))
if mibBuilder.loadTexts:cpqScsiCdDrvEntry.setStatus(_B)
_CpqScsiCdDrvCntlrIndex_Type=Integer32
_CpqScsiCdDrvCntlrIndex_Object=MibTableColumn
cpqScsiCdDrvCntlrIndex=_CpqScsiCdDrvCntlrIndex_Object((1,3,6,1,4,1,232,5,2,6,1,1,1),_CpqScsiCdDrvCntlrIndex_Type())
cpqScsiCdDrvCntlrIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCdDrvCntlrIndex.setStatus(_B)
class _CpqScsiCdDrvBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiCdDrvBusIndex_Type.__name__=_D
_CpqScsiCdDrvBusIndex_Object=MibTableColumn
cpqScsiCdDrvBusIndex=_CpqScsiCdDrvBusIndex_Object((1,3,6,1,4,1,232,5,2,6,1,1,2),_CpqScsiCdDrvBusIndex_Type())
cpqScsiCdDrvBusIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCdDrvBusIndex.setStatus(_B)
class _CpqScsiCdDrvScsiIdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiCdDrvScsiIdIndex_Type.__name__=_D
_CpqScsiCdDrvScsiIdIndex_Object=MibTableColumn
cpqScsiCdDrvScsiIdIndex=_CpqScsiCdDrvScsiIdIndex_Object((1,3,6,1,4,1,232,5,2,6,1,1,3),_CpqScsiCdDrvScsiIdIndex_Type())
cpqScsiCdDrvScsiIdIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCdDrvScsiIdIndex.setStatus(_B)
class _CpqScsiCdDrvLunIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqScsiCdDrvLunIndex_Type.__name__=_D
_CpqScsiCdDrvLunIndex_Object=MibTableColumn
cpqScsiCdDrvLunIndex=_CpqScsiCdDrvLunIndex_Object((1,3,6,1,4,1,232,5,2,6,1,1,4),_CpqScsiCdDrvLunIndex_Type())
cpqScsiCdDrvLunIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCdDrvLunIndex.setStatus(_B)
class _CpqScsiCdDrvModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_CpqScsiCdDrvModel_Type.__name__=_F
_CpqScsiCdDrvModel_Object=MibTableColumn
cpqScsiCdDrvModel=_CpqScsiCdDrvModel_Object((1,3,6,1,4,1,232,5,2,6,1,1,5),_CpqScsiCdDrvModel_Type())
cpqScsiCdDrvModel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCdDrvModel.setStatus(_B)
class _CpqScsiCdDrvVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_CpqScsiCdDrvVendor_Type.__name__=_F
_CpqScsiCdDrvVendor_Object=MibTableColumn
cpqScsiCdDrvVendor=_CpqScsiCdDrvVendor_Object((1,3,6,1,4,1,232,5,2,6,1,1,6),_CpqScsiCdDrvVendor_Type())
cpqScsiCdDrvVendor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCdDrvVendor.setStatus(_B)
class _CpqScsiCdDrvFwRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqScsiCdDrvFwRev_Type.__name__=_F
_CpqScsiCdDrvFwRev_Object=MibTableColumn
cpqScsiCdDrvFwRev=_CpqScsiCdDrvFwRev_Object((1,3,6,1,4,1,232,5,2,6,1,1,7),_CpqScsiCdDrvFwRev_Type())
cpqScsiCdDrvFwRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiCdDrvFwRev.setStatus(_B)
_CpqCdLibraryTable_Object=MibTable
cpqCdLibraryTable=_CpqCdLibraryTable_Object((1,3,6,1,4,1,232,5,2,6,2))
if mibBuilder.loadTexts:cpqCdLibraryTable.setStatus(_B)
_CpqCdLibraryEntry_Object=MibTableRow
cpqCdLibraryEntry=_CpqCdLibraryEntry_Object((1,3,6,1,4,1,232,5,2,6,2,1))
cpqCdLibraryEntry.setIndexNames((0,_C,_r),(0,_C,_s),(0,_C,_t),(0,_C,_Af))
if mibBuilder.loadTexts:cpqCdLibraryEntry.setStatus(_B)
_CpqCdLibraryCntlrIndex_Type=Integer32
_CpqCdLibraryCntlrIndex_Object=MibTableColumn
cpqCdLibraryCntlrIndex=_CpqCdLibraryCntlrIndex_Object((1,3,6,1,4,1,232,5,2,6,2,1,1),_CpqCdLibraryCntlrIndex_Type())
cpqCdLibraryCntlrIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqCdLibraryCntlrIndex.setStatus(_B)
class _CpqCdLibraryBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCdLibraryBusIndex_Type.__name__=_D
_CpqCdLibraryBusIndex_Object=MibTableColumn
cpqCdLibraryBusIndex=_CpqCdLibraryBusIndex_Object((1,3,6,1,4,1,232,5,2,6,2,1,2),_CpqCdLibraryBusIndex_Type())
cpqCdLibraryBusIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqCdLibraryBusIndex.setStatus(_B)
class _CpqCdLibraryScsiIdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCdLibraryScsiIdIndex_Type.__name__=_D
_CpqCdLibraryScsiIdIndex_Object=MibTableColumn
cpqCdLibraryScsiIdIndex=_CpqCdLibraryScsiIdIndex_Object((1,3,6,1,4,1,232,5,2,6,2,1,3),_CpqCdLibraryScsiIdIndex_Type())
cpqCdLibraryScsiIdIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqCdLibraryScsiIdIndex.setStatus(_B)
class _CpqCdLibraryLunIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCdLibraryLunIndex_Type.__name__=_D
_CpqCdLibraryLunIndex_Object=MibTableColumn
cpqCdLibraryLunIndex=_CpqCdLibraryLunIndex_Object((1,3,6,1,4,1,232,5,2,6,2,1,4),_CpqCdLibraryLunIndex_Type())
cpqCdLibraryLunIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqCdLibraryLunIndex.setStatus(_B)
class _CpqCdLibraryCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_N,3),(_M,4)))
_CpqCdLibraryCondition_Type.__name__=_D
_CpqCdLibraryCondition_Object=MibTableColumn
cpqCdLibraryCondition=_CpqCdLibraryCondition_Object((1,3,6,1,4,1,232,5,2,6,2,1,5),_CpqCdLibraryCondition_Type())
cpqCdLibraryCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqCdLibraryCondition.setStatus(_B)
class _CpqCdLibraryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_M,3),(_P,4)))
_CpqCdLibraryStatus_Type.__name__=_D
_CpqCdLibraryStatus_Object=MibTableColumn
cpqCdLibraryStatus=_CpqCdLibraryStatus_Object((1,3,6,1,4,1,232,5,2,6,2,1,6),_CpqCdLibraryStatus_Type())
cpqCdLibraryStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqCdLibraryStatus.setStatus(_B)
class _CpqCdLibraryModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_CpqCdLibraryModel_Type.__name__=_F
_CpqCdLibraryModel_Object=MibTableColumn
cpqCdLibraryModel=_CpqCdLibraryModel_Object((1,3,6,1,4,1,232,5,2,6,2,1,7),_CpqCdLibraryModel_Type())
cpqCdLibraryModel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqCdLibraryModel.setStatus(_B)
class _CpqCdLibraryVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_CpqCdLibraryVendor_Type.__name__=_F
_CpqCdLibraryVendor_Object=MibTableColumn
cpqCdLibraryVendor=_CpqCdLibraryVendor_Object((1,3,6,1,4,1,232,5,2,6,2,1,8),_CpqCdLibraryVendor_Type())
cpqCdLibraryVendor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqCdLibraryVendor.setStatus(_B)
class _CpqCdLibrarySerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqCdLibrarySerialNumber_Type.__name__=_F
_CpqCdLibrarySerialNumber_Object=MibTableColumn
cpqCdLibrarySerialNumber=_CpqCdLibrarySerialNumber_Object((1,3,6,1,4,1,232,5,2,6,2,1,9),_CpqCdLibrarySerialNumber_Type())
cpqCdLibrarySerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqCdLibrarySerialNumber.setStatus(_B)
class _CpqCdLibraryDriveList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqCdLibraryDriveList_Type.__name__=_O
_CpqCdLibraryDriveList_Object=MibTableColumn
cpqCdLibraryDriveList=_CpqCdLibraryDriveList_Object((1,3,6,1,4,1,232,5,2,6,2,1,10),_CpqCdLibraryDriveList_Type())
cpqCdLibraryDriveList.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqCdLibraryDriveList.setStatus(_B)
class _CpqCdLibraryFwRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqCdLibraryFwRev_Type.__name__=_F
_CpqCdLibraryFwRev_Object=MibTableColumn
cpqCdLibraryFwRev=_CpqCdLibraryFwRev_Object((1,3,6,1,4,1,232,5,2,6,2,1,11),_CpqCdLibraryFwRev_Type())
cpqCdLibraryFwRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqCdLibraryFwRev.setStatus(_B)
class _CpqCdLibraryFwSubtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCdLibraryFwSubtype_Type.__name__=_D
_CpqCdLibraryFwSubtype_Object=MibTableColumn
cpqCdLibraryFwSubtype=_CpqCdLibraryFwSubtype_Object((1,3,6,1,4,1,232,5,2,6,2,1,12),_CpqCdLibraryFwSubtype_Type())
cpqCdLibraryFwSubtype.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqCdLibraryFwSubtype.setStatus(_B)
_CpqScsiTrap_ObjectIdentity=ObjectIdentity
cpqScsiTrap=_CpqScsiTrap_ObjectIdentity((1,3,6,1,4,1,232,5,3))
_CpqScsiTrapPkts_Type=Counter32
_CpqScsiTrapPkts_Object=MibScalar
cpqScsiTrapPkts=_CpqScsiTrapPkts_Object((1,3,6,1,4,1,232,5,3,1),_CpqScsiTrapPkts_Type())
cpqScsiTrapPkts.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTrapPkts.setStatus(_E)
class _CpqScsiTrapLogMaxSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqScsiTrapLogMaxSize_Type.__name__=_D
_CpqScsiTrapLogMaxSize_Object=MibScalar
cpqScsiTrapLogMaxSize=_CpqScsiTrapLogMaxSize_Object((1,3,6,1,4,1,232,5,3,2),_CpqScsiTrapLogMaxSize_Type())
cpqScsiTrapLogMaxSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTrapLogMaxSize.setStatus(_E)
_CpqScsiTrapLogTable_Object=MibTable
cpqScsiTrapLogTable=_CpqScsiTrapLogTable_Object((1,3,6,1,4,1,232,5,3,3))
if mibBuilder.loadTexts:cpqScsiTrapLogTable.setStatus(_E)
_CpqScsiTrapLogEntry_Object=MibTableRow
cpqScsiTrapLogEntry=_CpqScsiTrapLogEntry_Object((1,3,6,1,4,1,232,5,3,3,1))
cpqScsiTrapLogEntry.setIndexNames((0,_C,_Ag))
if mibBuilder.loadTexts:cpqScsiTrapLogEntry.setStatus(_E)
class _CpqScsiTrapLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqScsiTrapLogIndex_Type.__name__=_D
_CpqScsiTrapLogIndex_Object=MibTableColumn
cpqScsiTrapLogIndex=_CpqScsiTrapLogIndex_Object((1,3,6,1,4,1,232,5,3,3,1,1),_CpqScsiTrapLogIndex_Type())
cpqScsiTrapLogIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTrapLogIndex.setStatus(_E)
class _CpqScsiTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5001,5002,5003)));namedValues=NamedValues(*((_Ah,1),(_Ai,2),(_Aj,3),(_Ak,5001),(_Al,5002),(_Am,5003)))
_CpqScsiTrapType_Type.__name__=_D
_CpqScsiTrapType_Object=MibTableColumn
cpqScsiTrapType=_CpqScsiTrapType_Object((1,3,6,1,4,1,232,5,3,3,1,2),_CpqScsiTrapType_Type())
cpqScsiTrapType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTrapType.setStatus(_E)
class _CpqScsiTrapTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_CpqScsiTrapTime_Type.__name__=_O
_CpqScsiTrapTime_Object=MibTableColumn
cpqScsiTrapTime=_CpqScsiTrapTime_Object((1,3,6,1,4,1,232,5,3,3,1,3),_CpqScsiTrapTime_Type())
cpqScsiTrapTime.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqScsiTrapTime.setStatus(_E)
_CpqTapeComponent_ObjectIdentity=ObjectIdentity
cpqTapeComponent=_CpqTapeComponent_ObjectIdentity((1,3,6,1,4,1,232,5,4))
_CpqTapePhyDrv_ObjectIdentity=ObjectIdentity
cpqTapePhyDrv=_CpqTapePhyDrv_ObjectIdentity((1,3,6,1,4,1,232,5,4,1))
_CpqTapePhyDrvTable_Object=MibTable
cpqTapePhyDrvTable=_CpqTapePhyDrvTable_Object((1,3,6,1,4,1,232,5,4,1,1))
if mibBuilder.loadTexts:cpqTapePhyDrvTable.setStatus(_B)
_CpqTapePhyDrvEntry_Object=MibTableRow
cpqTapePhyDrvEntry=_CpqTapePhyDrvEntry_Object((1,3,6,1,4,1,232,5,4,1,1,1))
cpqTapePhyDrvEntry.setIndexNames((0,_C,_Z),(0,_C,_a),(0,_C,_b),(0,_C,_u))
if mibBuilder.loadTexts:cpqTapePhyDrvEntry.setStatus(_B)
_CpqTapePhyDrvCntlrIndex_Type=Integer32
_CpqTapePhyDrvCntlrIndex_Object=MibTableColumn
cpqTapePhyDrvCntlrIndex=_CpqTapePhyDrvCntlrIndex_Object((1,3,6,1,4,1,232,5,4,1,1,1,1),_CpqTapePhyDrvCntlrIndex_Type())
cpqTapePhyDrvCntlrIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvCntlrIndex.setStatus(_B)
class _CpqTapePhyDrvBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqTapePhyDrvBusIndex_Type.__name__=_D
_CpqTapePhyDrvBusIndex_Object=MibTableColumn
cpqTapePhyDrvBusIndex=_CpqTapePhyDrvBusIndex_Object((1,3,6,1,4,1,232,5,4,1,1,1,2),_CpqTapePhyDrvBusIndex_Type())
cpqTapePhyDrvBusIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvBusIndex.setStatus(_B)
class _CpqTapePhyDrvScsiIdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqTapePhyDrvScsiIdIndex_Type.__name__=_D
_CpqTapePhyDrvScsiIdIndex_Object=MibTableColumn
cpqTapePhyDrvScsiIdIndex=_CpqTapePhyDrvScsiIdIndex_Object((1,3,6,1,4,1,232,5,4,1,1,1,3),_CpqTapePhyDrvScsiIdIndex_Type())
cpqTapePhyDrvScsiIdIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvScsiIdIndex.setStatus(_B)
class _CpqTapePhyDrvLunIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqTapePhyDrvLunIndex_Type.__name__=_D
_CpqTapePhyDrvLunIndex_Object=MibTableColumn
cpqTapePhyDrvLunIndex=_CpqTapePhyDrvLunIndex_Object((1,3,6,1,4,1,232,5,4,1,1,1,4),_CpqTapePhyDrvLunIndex_Type())
cpqTapePhyDrvLunIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvLunIndex.setStatus(_B)
class _CpqTapePhyDrvType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*((_G,1),('cpqDat4-16',2),('cpqDatAuto',3),('cpqDat2-8',4),('cpqDlt10-20',5),('cpqDlt20-40',6),('cpqDlt15-30',7),('cpqDlt35-70',8),('cpqDat4-8',9),('cpqSlr4-8',10),('cpqDat12-24',11),('cpqDatAuto12-24',12),('cpqMlr16-32',13),('cpqAit35',14),('cpqAit50',15),('cpqDat20-40',16),('cpqDlt40-80',17),('cpqDatAuto20-40',18),('cpqSuperDlt1',19),('cpqAit35Lvd',20),('cpqCompaq',21)))
_CpqTapePhyDrvType_Type.__name__=_D
_CpqTapePhyDrvType_Object=MibTableColumn
cpqTapePhyDrvType=_CpqTapePhyDrvType_Object((1,3,6,1,4,1,232,5,4,1,1,1,5),_CpqTapePhyDrvType_Type())
cpqTapePhyDrvType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvType.setStatus(_B)
class _CpqTapePhyDrvCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_N,3),(_M,4)))
_CpqTapePhyDrvCondition_Type.__name__=_D
_CpqTapePhyDrvCondition_Object=MibTableColumn
cpqTapePhyDrvCondition=_CpqTapePhyDrvCondition_Object((1,3,6,1,4,1,232,5,4,1,1,1,6),_CpqTapePhyDrvCondition_Type())
cpqTapePhyDrvCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvCondition.setStatus(_B)
class _CpqTapePhyDrvMagSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CpqTapePhyDrvMagSize_Type.__name__=_D
_CpqTapePhyDrvMagSize_Object=MibTableColumn
cpqTapePhyDrvMagSize=_CpqTapePhyDrvMagSize_Object((1,3,6,1,4,1,232,5,4,1,1,1,7),_CpqTapePhyDrvMagSize_Type())
cpqTapePhyDrvMagSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvMagSize.setStatus(_B)
class _CpqTapePhyDrvSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqTapePhyDrvSerialNumber_Type.__name__=_F
_CpqTapePhyDrvSerialNumber_Object=MibTableColumn
cpqTapePhyDrvSerialNumber=_CpqTapePhyDrvSerialNumber_Object((1,3,6,1,4,1,232,5,4,1,1,1,8),_CpqTapePhyDrvSerialNumber_Type())
cpqTapePhyDrvSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvSerialNumber.setStatus(_B)
class _CpqTapePhyDrvCleanReq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_v,2),(_w,3)))
_CpqTapePhyDrvCleanReq_Type.__name__=_D
_CpqTapePhyDrvCleanReq_Object=MibTableColumn
cpqTapePhyDrvCleanReq=_CpqTapePhyDrvCleanReq_Object((1,3,6,1,4,1,232,5,4,1,1,1,9),_CpqTapePhyDrvCleanReq_Type())
cpqTapePhyDrvCleanReq.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvCleanReq.setStatus(_B)
class _CpqTapePhyDrvCleanTapeRepl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_v,2),(_w,3)))
_CpqTapePhyDrvCleanTapeRepl_Type.__name__=_D
_CpqTapePhyDrvCleanTapeRepl_Object=MibTableColumn
cpqTapePhyDrvCleanTapeRepl=_CpqTapePhyDrvCleanTapeRepl_Object((1,3,6,1,4,1,232,5,4,1,1,1,10),_CpqTapePhyDrvCleanTapeRepl_Type())
cpqTapePhyDrvCleanTapeRepl.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvCleanTapeRepl.setStatus(_B)
class _CpqTapePhyDrvFwSubtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqTapePhyDrvFwSubtype_Type.__name__=_D
_CpqTapePhyDrvFwSubtype_Object=MibTableColumn
cpqTapePhyDrvFwSubtype=_CpqTapePhyDrvFwSubtype_Object((1,3,6,1,4,1,232,5,4,1,1,1,11),_CpqTapePhyDrvFwSubtype_Type())
cpqTapePhyDrvFwSubtype.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvFwSubtype.setStatus(_B)
class _CpqTapePhyDrvName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpqTapePhyDrvName_Type.__name__=_F
_CpqTapePhyDrvName_Object=MibTableColumn
cpqTapePhyDrvName=_CpqTapePhyDrvName_Object((1,3,6,1,4,1,232,5,4,1,1,1,12),_CpqTapePhyDrvName_Type())
cpqTapePhyDrvName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvName.setStatus(_B)
_CpqTapePhyDrvCleanTapeCount_Type=Integer32
_CpqTapePhyDrvCleanTapeCount_Object=MibTableColumn
cpqTapePhyDrvCleanTapeCount=_CpqTapePhyDrvCleanTapeCount_Object((1,3,6,1,4,1,232,5,4,1,1,1,13),_CpqTapePhyDrvCleanTapeCount_Type())
cpqTapePhyDrvCleanTapeCount.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvCleanTapeCount.setStatus(_B)
class _CpqTapePhyDrvFwRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqTapePhyDrvFwRev_Type.__name__=_F
_CpqTapePhyDrvFwRev_Object=MibTableColumn
cpqTapePhyDrvFwRev=_CpqTapePhyDrvFwRev_Object((1,3,6,1,4,1,232,5,4,1,1,1,14),_CpqTapePhyDrvFwRev_Type())
cpqTapePhyDrvFwRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvFwRev.setStatus(_B)
class _CpqTapePhyDrvStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6,7,8)));namedValues=NamedValues(*((_G,1),(_H,2),(_M,4),(_P,5),(_j,6),(_k,7),(_l,8)))
_CpqTapePhyDrvStatus_Type.__name__=_D
_CpqTapePhyDrvStatus_Object=MibTableColumn
cpqTapePhyDrvStatus=_CpqTapePhyDrvStatus_Object((1,3,6,1,4,1,232,5,4,1,1,1,15),_CpqTapePhyDrvStatus_Type())
cpqTapePhyDrvStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvStatus.setStatus(_B)
class _CpqTapePhyDrvHotPlug_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_n,2),(_o,3)))
_CpqTapePhyDrvHotPlug_Type.__name__=_D
_CpqTapePhyDrvHotPlug_Object=MibTableColumn
cpqTapePhyDrvHotPlug=_CpqTapePhyDrvHotPlug_Object((1,3,6,1,4,1,232,5,4,1,1,1,16),_CpqTapePhyDrvHotPlug_Type())
cpqTapePhyDrvHotPlug.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvHotPlug.setStatus(_B)
class _CpqTapePhyDrvPlacement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_p,2),(_q,3)))
_CpqTapePhyDrvPlacement_Type.__name__=_D
_CpqTapePhyDrvPlacement_Object=MibTableColumn
cpqTapePhyDrvPlacement=_CpqTapePhyDrvPlacement_Object((1,3,6,1,4,1,232,5,4,1,1,1,17),_CpqTapePhyDrvPlacement_Type())
cpqTapePhyDrvPlacement.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvPlacement.setStatus(_B)
class _CpqTapePhyDrvLibraryDrive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_v,2),(_w,3)))
_CpqTapePhyDrvLibraryDrive_Type.__name__=_D
_CpqTapePhyDrvLibraryDrive_Object=MibTableColumn
cpqTapePhyDrvLibraryDrive=_CpqTapePhyDrvLibraryDrive_Object((1,3,6,1,4,1,232,5,4,1,1,1,18),_CpqTapePhyDrvLibraryDrive_Type())
cpqTapePhyDrvLibraryDrive.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvLibraryDrive.setStatus(_B)
class _CpqTapePhyDrvLoaderName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpqTapePhyDrvLoaderName_Type.__name__=_F
_CpqTapePhyDrvLoaderName_Object=MibTableColumn
cpqTapePhyDrvLoaderName=_CpqTapePhyDrvLoaderName_Object((1,3,6,1,4,1,232,5,4,1,1,1,19),_CpqTapePhyDrvLoaderName_Type())
cpqTapePhyDrvLoaderName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvLoaderName.setStatus(_B)
class _CpqTapePhyDrvLoaderFwRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqTapePhyDrvLoaderFwRev_Type.__name__=_F
_CpqTapePhyDrvLoaderFwRev_Object=MibTableColumn
cpqTapePhyDrvLoaderFwRev=_CpqTapePhyDrvLoaderFwRev_Object((1,3,6,1,4,1,232,5,4,1,1,1,20),_CpqTapePhyDrvLoaderFwRev_Type())
cpqTapePhyDrvLoaderFwRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvLoaderFwRev.setStatus(_B)
class _CpqTapePhyDrvLoaderSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqTapePhyDrvLoaderSerialNum_Type.__name__=_F
_CpqTapePhyDrvLoaderSerialNum_Object=MibTableColumn
cpqTapePhyDrvLoaderSerialNum=_CpqTapePhyDrvLoaderSerialNum_Object((1,3,6,1,4,1,232,5,4,1,1,1,21),_CpqTapePhyDrvLoaderSerialNum_Type())
cpqTapePhyDrvLoaderSerialNum.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapePhyDrvLoaderSerialNum.setStatus(_B)
_CpqTapeCounters_ObjectIdentity=ObjectIdentity
cpqTapeCounters=_CpqTapeCounters_ObjectIdentity((1,3,6,1,4,1,232,5,4,2))
_CpqTapeCountersTable_Object=MibTable
cpqTapeCountersTable=_CpqTapeCountersTable_Object((1,3,6,1,4,1,232,5,4,2,1))
if mibBuilder.loadTexts:cpqTapeCountersTable.setStatus(_B)
_CpqTapeCountersEntry_Object=MibTableRow
cpqTapeCountersEntry=_CpqTapeCountersEntry_Object((1,3,6,1,4,1,232,5,4,2,1,1))
cpqTapeCountersEntry.setIndexNames((0,_C,_An),(0,_C,_Ao),(0,_C,_Ap),(0,_C,_Aq))
if mibBuilder.loadTexts:cpqTapeCountersEntry.setStatus(_B)
_CpqTapeCountersCntlrIndex_Type=Integer32
_CpqTapeCountersCntlrIndex_Object=MibTableColumn
cpqTapeCountersCntlrIndex=_CpqTapeCountersCntlrIndex_Object((1,3,6,1,4,1,232,5,4,2,1,1,1),_CpqTapeCountersCntlrIndex_Type())
cpqTapeCountersCntlrIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeCountersCntlrIndex.setStatus(_B)
class _CpqTapeCountersBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqTapeCountersBusIndex_Type.__name__=_D
_CpqTapeCountersBusIndex_Object=MibTableColumn
cpqTapeCountersBusIndex=_CpqTapeCountersBusIndex_Object((1,3,6,1,4,1,232,5,4,2,1,1,2),_CpqTapeCountersBusIndex_Type())
cpqTapeCountersBusIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeCountersBusIndex.setStatus(_B)
class _CpqTapeCountersScsiIdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqTapeCountersScsiIdIndex_Type.__name__=_D
_CpqTapeCountersScsiIdIndex_Object=MibTableColumn
cpqTapeCountersScsiIdIndex=_CpqTapeCountersScsiIdIndex_Object((1,3,6,1,4,1,232,5,4,2,1,1,3),_CpqTapeCountersScsiIdIndex_Type())
cpqTapeCountersScsiIdIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeCountersScsiIdIndex.setStatus(_B)
class _CpqTapeCountersLunIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqTapeCountersLunIndex_Type.__name__=_D
_CpqTapeCountersLunIndex_Object=MibTableColumn
cpqTapeCountersLunIndex=_CpqTapeCountersLunIndex_Object((1,3,6,1,4,1,232,5,4,2,1,1,4),_CpqTapeCountersLunIndex_Type())
cpqTapeCountersLunIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeCountersLunIndex.setStatus(_B)
_CpqTapeCountersReWrites_Type=Counter32
_CpqTapeCountersReWrites_Object=MibTableColumn
cpqTapeCountersReWrites=_CpqTapeCountersReWrites_Object((1,3,6,1,4,1,232,5,4,2,1,1,5),_CpqTapeCountersReWrites_Type())
cpqTapeCountersReWrites.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeCountersReWrites.setStatus(_B)
_CpqTapeCountersReReads_Type=Counter32
_CpqTapeCountersReReads_Object=MibTableColumn
cpqTapeCountersReReads=_CpqTapeCountersReReads_Object((1,3,6,1,4,1,232,5,4,2,1,1,6),_CpqTapeCountersReReads_Type())
cpqTapeCountersReReads.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeCountersReReads.setStatus(_B)
_CpqTapeCountersTotalErrors_Type=Counter32
_CpqTapeCountersTotalErrors_Object=MibTableColumn
cpqTapeCountersTotalErrors=_CpqTapeCountersTotalErrors_Object((1,3,6,1,4,1,232,5,4,2,1,1,7),_CpqTapeCountersTotalErrors_Type())
cpqTapeCountersTotalErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeCountersTotalErrors.setStatus(_B)
_CpqTapeCountersTotalUncorrectable_Type=Counter32
_CpqTapeCountersTotalUncorrectable_Object=MibTableColumn
cpqTapeCountersTotalUncorrectable=_CpqTapeCountersTotalUncorrectable_Object((1,3,6,1,4,1,232,5,4,2,1,1,8),_CpqTapeCountersTotalUncorrectable_Type())
cpqTapeCountersTotalUncorrectable.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeCountersTotalUncorrectable.setStatus(_B)
_CpqTapeCountersTotalBytes_Type=Counter32
_CpqTapeCountersTotalBytes_Object=MibTableColumn
cpqTapeCountersTotalBytes=_CpqTapeCountersTotalBytes_Object((1,3,6,1,4,1,232,5,4,2,1,1,9),_CpqTapeCountersTotalBytes_Type())
cpqTapeCountersTotalBytes.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeCountersTotalBytes.setStatus(_B)
_CpqTapeLibrary_ObjectIdentity=ObjectIdentity
cpqTapeLibrary=_CpqTapeLibrary_ObjectIdentity((1,3,6,1,4,1,232,5,4,3))
_CpqTapeLibraryTable_Object=MibTable
cpqTapeLibraryTable=_CpqTapeLibraryTable_Object((1,3,6,1,4,1,232,5,4,3,1))
if mibBuilder.loadTexts:cpqTapeLibraryTable.setStatus(_B)
_CpqTapeLibraryEntry_Object=MibTableRow
cpqTapeLibraryEntry=_CpqTapeLibraryEntry_Object((1,3,6,1,4,1,232,5,4,3,1,1))
cpqTapeLibraryEntry.setIndexNames((0,_C,_x),(0,_C,_y),(0,_C,_z),(0,_C,_A0))
if mibBuilder.loadTexts:cpqTapeLibraryEntry.setStatus(_B)
_CpqTapeLibraryCntlrIndex_Type=Integer32
_CpqTapeLibraryCntlrIndex_Object=MibTableColumn
cpqTapeLibraryCntlrIndex=_CpqTapeLibraryCntlrIndex_Object((1,3,6,1,4,1,232,5,4,3,1,1,1),_CpqTapeLibraryCntlrIndex_Type())
cpqTapeLibraryCntlrIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryCntlrIndex.setStatus(_B)
class _CpqTapeLibraryBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqTapeLibraryBusIndex_Type.__name__=_D
_CpqTapeLibraryBusIndex_Object=MibTableColumn
cpqTapeLibraryBusIndex=_CpqTapeLibraryBusIndex_Object((1,3,6,1,4,1,232,5,4,3,1,1,2),_CpqTapeLibraryBusIndex_Type())
cpqTapeLibraryBusIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryBusIndex.setStatus(_B)
class _CpqTapeLibraryScsiIdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqTapeLibraryScsiIdIndex_Type.__name__=_D
_CpqTapeLibraryScsiIdIndex_Object=MibTableColumn
cpqTapeLibraryScsiIdIndex=_CpqTapeLibraryScsiIdIndex_Object((1,3,6,1,4,1,232,5,4,3,1,1,3),_CpqTapeLibraryScsiIdIndex_Type())
cpqTapeLibraryScsiIdIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryScsiIdIndex.setStatus(_B)
class _CpqTapeLibraryLunIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqTapeLibraryLunIndex_Type.__name__=_D
_CpqTapeLibraryLunIndex_Object=MibTableColumn
cpqTapeLibraryLunIndex=_CpqTapeLibraryLunIndex_Object((1,3,6,1,4,1,232,5,4,3,1,1,4),_CpqTapeLibraryLunIndex_Type())
cpqTapeLibraryLunIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryLunIndex.setStatus(_B)
class _CpqTapeLibraryCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_N,3),(_M,4)))
_CpqTapeLibraryCondition_Type.__name__=_D
_CpqTapeLibraryCondition_Object=MibTableColumn
cpqTapeLibraryCondition=_CpqTapeLibraryCondition_Object((1,3,6,1,4,1,232,5,4,3,1,1,5),_CpqTapeLibraryCondition_Type())
cpqTapeLibraryCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryCondition.setStatus(_B)
class _CpqTapeLibraryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64535))
_CpqTapeLibraryStatus_Type.__name__=_D
_CpqTapeLibraryStatus_Object=MibTableColumn
cpqTapeLibraryStatus=_CpqTapeLibraryStatus_Object((1,3,6,1,4,1,232,5,4,3,1,1,6),_CpqTapeLibraryStatus_Type())
cpqTapeLibraryStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryStatus.setStatus(_B)
class _CpqTapeLibraryDoorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('closed',2),('open',3),(_S,4)))
_CpqTapeLibraryDoorStatus_Type.__name__=_D
_CpqTapeLibraryDoorStatus_Object=MibTableColumn
cpqTapeLibraryDoorStatus=_CpqTapeLibraryDoorStatus_Object((1,3,6,1,4,1,232,5,4,3,1,1,7),_CpqTapeLibraryDoorStatus_Type())
cpqTapeLibraryDoorStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryDoorStatus.setStatus(_B)
_CpqTapeLibraryStatHours_Type=Counter32
_CpqTapeLibraryStatHours_Object=MibTableColumn
cpqTapeLibraryStatHours=_CpqTapeLibraryStatHours_Object((1,3,6,1,4,1,232,5,4,3,1,1,8),_CpqTapeLibraryStatHours_Type())
cpqTapeLibraryStatHours.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryStatHours.setStatus(_B)
_CpqTapeLibraryStatMoves_Type=Counter32
_CpqTapeLibraryStatMoves_Object=MibTableColumn
cpqTapeLibraryStatMoves=_CpqTapeLibraryStatMoves_Object((1,3,6,1,4,1,232,5,4,3,1,1,9),_CpqTapeLibraryStatMoves_Type())
cpqTapeLibraryStatMoves.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryStatMoves.setStatus(_B)
class _CpqTapeLibraryName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpqTapeLibraryName_Type.__name__=_F
_CpqTapeLibraryName_Object=MibTableColumn
cpqTapeLibraryName=_CpqTapeLibraryName_Object((1,3,6,1,4,1,232,5,4,3,1,1,10),_CpqTapeLibraryName_Type())
cpqTapeLibraryName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryName.setStatus(_B)
class _CpqTapeLibrarySerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqTapeLibrarySerialNumber_Type.__name__=_F
_CpqTapeLibrarySerialNumber_Object=MibTableColumn
cpqTapeLibrarySerialNumber=_CpqTapeLibrarySerialNumber_Object((1,3,6,1,4,1,232,5,4,3,1,1,11),_CpqTapeLibrarySerialNumber_Type())
cpqTapeLibrarySerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibrarySerialNumber.setStatus(_B)
class _CpqTapeLibraryDriveList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,320))
_CpqTapeLibraryDriveList_Type.__name__=_O
_CpqTapeLibraryDriveList_Object=MibTableColumn
cpqTapeLibraryDriveList=_CpqTapeLibraryDriveList_Object((1,3,6,1,4,1,232,5,4,3,1,1,12),_CpqTapeLibraryDriveList_Type())
cpqTapeLibraryDriveList.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryDriveList.setStatus(_E)
class _CpqTapeLibraryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_H,2),(_N,3),(_M,4),(_P,5)))
_CpqTapeLibraryState_Type.__name__=_D
_CpqTapeLibraryState_Object=MibTableColumn
cpqTapeLibraryState=_CpqTapeLibraryState_Object((1,3,6,1,4,1,232,5,4,3,1,1,13),_CpqTapeLibraryState_Type())
cpqTapeLibraryState.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryState.setStatus(_B)
class _CpqTapeLibraryTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_S,2),(_H,3),('safeTempExceeded',4),('maxTempExceeded',5)))
_CpqTapeLibraryTemperature_Type.__name__=_D
_CpqTapeLibraryTemperature_Object=MibTableColumn
cpqTapeLibraryTemperature=_CpqTapeLibraryTemperature_Object((1,3,6,1,4,1,232,5,4,3,1,1,14),_CpqTapeLibraryTemperature_Type())
cpqTapeLibraryTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryTemperature.setStatus(_B)
class _CpqTapeLibraryRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_S,2),('capable',3),(_Ar,4),('active',5)))
_CpqTapeLibraryRedundancy_Type.__name__=_D
_CpqTapeLibraryRedundancy_Object=MibTableColumn
cpqTapeLibraryRedundancy=_CpqTapeLibraryRedundancy_Object((1,3,6,1,4,1,232,5,4,3,1,1,15),_CpqTapeLibraryRedundancy_Type())
cpqTapeLibraryRedundancy.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryRedundancy.setStatus(_B)
class _CpqTapeLibraryHotSwap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_S,2),('capable',3),(_Ar,4)))
_CpqTapeLibraryHotSwap_Type.__name__=_D
_CpqTapeLibraryHotSwap_Object=MibTableColumn
cpqTapeLibraryHotSwap=_CpqTapeLibraryHotSwap_Object((1,3,6,1,4,1,232,5,4,3,1,1,16),_CpqTapeLibraryHotSwap_Type())
cpqTapeLibraryHotSwap.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryHotSwap.setStatus(_B)
class _CpqTapeLibraryFwRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqTapeLibraryFwRev_Type.__name__=_F
_CpqTapeLibraryFwRev_Object=MibTableColumn
cpqTapeLibraryFwRev=_CpqTapeLibraryFwRev_Object((1,3,6,1,4,1,232,5,4,3,1,1,17),_CpqTapeLibraryFwRev_Type())
cpqTapeLibraryFwRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryFwRev.setStatus(_B)
class _CpqTapeLibraryTapeList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,560))
_CpqTapeLibraryTapeList_Type.__name__=_O
_CpqTapeLibraryTapeList_Object=MibTableColumn
cpqTapeLibraryTapeList=_CpqTapeLibraryTapeList_Object((1,3,6,1,4,1,232,5,4,3,1,1,18),_CpqTapeLibraryTapeList_Type())
cpqTapeLibraryTapeList.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqTapeLibraryTapeList.setStatus(_B)
_CpqSasComponent_ObjectIdentity=ObjectIdentity
cpqSasComponent=_CpqSasComponent_ObjectIdentity((1,3,6,1,4,1,232,5,5))
_CpqSasHba_ObjectIdentity=ObjectIdentity
cpqSasHba=_CpqSasHba_ObjectIdentity((1,3,6,1,4,1,232,5,5,1))
_CpqSasHbaTable_Object=MibTable
cpqSasHbaTable=_CpqSasHbaTable_Object((1,3,6,1,4,1,232,5,5,1,1))
if mibBuilder.loadTexts:cpqSasHbaTable.setStatus(_B)
_CpqSasHbaEntry_Object=MibTableRow
cpqSasHbaEntry=_CpqSasHbaEntry_Object((1,3,6,1,4,1,232,5,5,1,1,1))
cpqSasHbaEntry.setIndexNames((0,_C,_As))
if mibBuilder.loadTexts:cpqSasHbaEntry.setStatus(_B)
_CpqSasHbaIndex_Type=Integer32
_CpqSasHbaIndex_Object=MibTableColumn
cpqSasHbaIndex=_CpqSasHbaIndex_Object((1,3,6,1,4,1,232,5,5,1,1,1,1),_CpqSasHbaIndex_Type())
cpqSasHbaIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasHbaIndex.setStatus(_B)
class _CpqSasHbaHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSasHbaHwLocation_Type.__name__=_F
_CpqSasHbaHwLocation_Object=MibTableColumn
cpqSasHbaHwLocation=_CpqSasHbaHwLocation_Object((1,3,6,1,4,1,232,5,5,1,1,1,2),_CpqSasHbaHwLocation_Type())
cpqSasHbaHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasHbaHwLocation.setStatus(_V)
class _CpqSasHbaModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_G,1),('generic',2),('sas8int',3),('sas4int',4),('sasSc44Ge',5),('sasSc40Ge',6),('sasSc08Ge',7),('sasSc08e',8),('sasH220i',9),('sasH221',10),('sasH210i',11),('sasH220',12),('sasH222',13),('sasP824ip',14)))
_CpqSasHbaModel_Type.__name__=_D
_CpqSasHbaModel_Object=MibTableColumn
cpqSasHbaModel=_CpqSasHbaModel_Object((1,3,6,1,4,1,232,5,5,1,1,1,3),_CpqSasHbaModel_Type())
cpqSasHbaModel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasHbaModel.setStatus(_B)
class _CpqSasHbaStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_M,3)))
_CpqSasHbaStatus_Type.__name__=_D
_CpqSasHbaStatus_Object=MibTableColumn
cpqSasHbaStatus=_CpqSasHbaStatus_Object((1,3,6,1,4,1,232,5,5,1,1,1,4),_CpqSasHbaStatus_Type())
cpqSasHbaStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasHbaStatus.setStatus(_B)
class _CpqSasHbaCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_N,3),(_M,4)))
_CpqSasHbaCondition_Type.__name__=_D
_CpqSasHbaCondition_Object=MibTableColumn
cpqSasHbaCondition=_CpqSasHbaCondition_Object((1,3,6,1,4,1,232,5,5,1,1,1,5),_CpqSasHbaCondition_Type())
cpqSasHbaCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasHbaCondition.setStatus(_B)
class _CpqSasHbaOverallCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_N,3),(_M,4)))
_CpqSasHbaOverallCondition_Type.__name__=_D
_CpqSasHbaOverallCondition_Object=MibTableColumn
cpqSasHbaOverallCondition=_CpqSasHbaOverallCondition_Object((1,3,6,1,4,1,232,5,5,1,1,1,6),_CpqSasHbaOverallCondition_Type())
cpqSasHbaOverallCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasHbaOverallCondition.setStatus(_B)
class _CpqSasHbaSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CpqSasHbaSerialNumber_Type.__name__=_F
_CpqSasHbaSerialNumber_Object=MibTableColumn
cpqSasHbaSerialNumber=_CpqSasHbaSerialNumber_Object((1,3,6,1,4,1,232,5,5,1,1,1,7),_CpqSasHbaSerialNumber_Type())
cpqSasHbaSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasHbaSerialNumber.setStatus(_B)
_CpqSasHbaFwVersion_Type=DisplayString
_CpqSasHbaFwVersion_Object=MibTableColumn
cpqSasHbaFwVersion=_CpqSasHbaFwVersion_Object((1,3,6,1,4,1,232,5,5,1,1,1,8),_CpqSasHbaFwVersion_Type())
cpqSasHbaFwVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasHbaFwVersion.setStatus(_B)
_CpqSasHbaBiosVersion_Type=DisplayString
_CpqSasHbaBiosVersion_Object=MibTableColumn
cpqSasHbaBiosVersion=_CpqSasHbaBiosVersion_Object((1,3,6,1,4,1,232,5,5,1,1,1,9),_CpqSasHbaBiosVersion_Type())
cpqSasHbaBiosVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasHbaBiosVersion.setStatus(_B)
class _CpqSasHbaPciLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSasHbaPciLocation_Type.__name__=_F
_CpqSasHbaPciLocation_Object=MibTableColumn
cpqSasHbaPciLocation=_CpqSasHbaPciLocation_Object((1,3,6,1,4,1,232,5,5,1,1,1,10),_CpqSasHbaPciLocation_Type())
cpqSasHbaPciLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasHbaPciLocation.setStatus(_V)
_CpqSasPhyDrv_ObjectIdentity=ObjectIdentity
cpqSasPhyDrv=_CpqSasPhyDrv_ObjectIdentity((1,3,6,1,4,1,232,5,5,2))
_CpqSasPhyDrvTable_Object=MibTable
cpqSasPhyDrvTable=_CpqSasPhyDrvTable_Object((1,3,6,1,4,1,232,5,5,2,1))
if mibBuilder.loadTexts:cpqSasPhyDrvTable.setStatus(_B)
_CpqSasPhyDrvEntry_Object=MibTableRow
cpqSasPhyDrvEntry=_CpqSasPhyDrvEntry_Object((1,3,6,1,4,1,232,5,5,2,1,1))
cpqSasPhyDrvEntry.setIndexNames((0,_C,_c),(0,_C,_d))
if mibBuilder.loadTexts:cpqSasPhyDrvEntry.setStatus(_B)
_CpqSasPhyDrvHbaIndex_Type=Integer32
_CpqSasPhyDrvHbaIndex_Object=MibTableColumn
cpqSasPhyDrvHbaIndex=_CpqSasPhyDrvHbaIndex_Object((1,3,6,1,4,1,232,5,5,2,1,1,1),_CpqSasPhyDrvHbaIndex_Type())
cpqSasPhyDrvHbaIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvHbaIndex.setStatus(_B)
_CpqSasPhyDrvIndex_Type=Integer32
_CpqSasPhyDrvIndex_Object=MibTableColumn
cpqSasPhyDrvIndex=_CpqSasPhyDrvIndex_Object((1,3,6,1,4,1,232,5,5,2,1,1,2),_CpqSasPhyDrvIndex_Type())
cpqSasPhyDrvIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvIndex.setStatus(_B)
class _CpqSasPhyDrvLocationString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSasPhyDrvLocationString_Type.__name__=_F
_CpqSasPhyDrvLocationString_Object=MibTableColumn
cpqSasPhyDrvLocationString=_CpqSasPhyDrvLocationString_Object((1,3,6,1,4,1,232,5,5,2,1,1,3),_CpqSasPhyDrvLocationString_Type())
cpqSasPhyDrvLocationString.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvLocationString.setStatus(_B)
class _CpqSasPhyDrvModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CpqSasPhyDrvModel_Type.__name__=_F
_CpqSasPhyDrvModel_Object=MibTableColumn
cpqSasPhyDrvModel=_CpqSasPhyDrvModel_Object((1,3,6,1,4,1,232,5,5,2,1,1,4),_CpqSasPhyDrvModel_Type())
cpqSasPhyDrvModel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvModel.setStatus(_B)
class _CpqSasPhyDrvStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_G,1),(_H,2),(_AT,3),(_P,4),(_M,5),(_j,6),(_AU,7),(_l,8),(_k,9),(_At,10),('missingWasSSDWearOut',11),('notAuthenticated',12),('missingWasNotAuthenticated',13)))
_CpqSasPhyDrvStatus_Type.__name__=_D
_CpqSasPhyDrvStatus_Object=MibTableColumn
cpqSasPhyDrvStatus=_CpqSasPhyDrvStatus_Object((1,3,6,1,4,1,232,5,5,2,1,1,5),_CpqSasPhyDrvStatus_Type())
cpqSasPhyDrvStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvStatus.setStatus(_B)
class _CpqSasPhyDrvCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_N,3),(_M,4)))
_CpqSasPhyDrvCondition_Type.__name__=_D
_CpqSasPhyDrvCondition_Object=MibTableColumn
cpqSasPhyDrvCondition=_CpqSasPhyDrvCondition_Object((1,3,6,1,4,1,232,5,5,2,1,1,6),_CpqSasPhyDrvCondition_Type())
cpqSasPhyDrvCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvCondition.setStatus(_B)
class _CpqSasPhyDrvFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqSasPhyDrvFWRev_Type.__name__=_F
_CpqSasPhyDrvFWRev_Object=MibTableColumn
cpqSasPhyDrvFWRev=_CpqSasPhyDrvFWRev_Object((1,3,6,1,4,1,232,5,5,2,1,1,7),_CpqSasPhyDrvFWRev_Type())
cpqSasPhyDrvFWRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvFWRev.setStatus(_B)
class _CpqSasPhyDrvSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSasPhyDrvSize_Type.__name__=_D
_CpqSasPhyDrvSize_Object=MibTableColumn
cpqSasPhyDrvSize=_CpqSasPhyDrvSize_Object((1,3,6,1,4,1,232,5,5,2,1,1,8),_CpqSasPhyDrvSize_Type())
cpqSasPhyDrvSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvSize.setStatus(_B)
_CpqSasPhyDrvUsedReallocs_Type=Counter32
_CpqSasPhyDrvUsedReallocs_Object=MibTableColumn
cpqSasPhyDrvUsedReallocs=_CpqSasPhyDrvUsedReallocs_Object((1,3,6,1,4,1,232,5,5,2,1,1,9),_CpqSasPhyDrvUsedReallocs_Type())
cpqSasPhyDrvUsedReallocs.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvUsedReallocs.setStatus(_B)
class _CpqSasPhyDrvSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CpqSasPhyDrvSerialNumber_Type.__name__=_F
_CpqSasPhyDrvSerialNumber_Object=MibTableColumn
cpqSasPhyDrvSerialNumber=_CpqSasPhyDrvSerialNumber_Object((1,3,6,1,4,1,232,5,5,2,1,1,10),_CpqSasPhyDrvSerialNumber_Type())
cpqSasPhyDrvSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvSerialNumber.setStatus(_B)
class _CpqSasPhyDrvMemberLogDrv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('member',2),('spare',3),(_AV,4)))
_CpqSasPhyDrvMemberLogDrv_Type.__name__=_D
_CpqSasPhyDrvMemberLogDrv_Object=MibTableColumn
cpqSasPhyDrvMemberLogDrv=_CpqSasPhyDrvMemberLogDrv_Object((1,3,6,1,4,1,232,5,5,2,1,1,11),_CpqSasPhyDrvMemberLogDrv_Type())
cpqSasPhyDrvMemberLogDrv.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvMemberLogDrv.setStatus(_B)
class _CpqSasPhyDrvRotationalSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('rpm7200',2),('rpm10K',3),('rpm15K',4),('rpmSsd',5)))
_CpqSasPhyDrvRotationalSpeed_Type.__name__=_D
_CpqSasPhyDrvRotationalSpeed_Object=MibTableColumn
cpqSasPhyDrvRotationalSpeed=_CpqSasPhyDrvRotationalSpeed_Object((1,3,6,1,4,1,232,5,5,2,1,1,12),_CpqSasPhyDrvRotationalSpeed_Type())
cpqSasPhyDrvRotationalSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvRotationalSpeed.setStatus(_B)
class _CpqSasPhyDrvOsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSasPhyDrvOsName_Type.__name__=_F
_CpqSasPhyDrvOsName_Object=MibTableColumn
cpqSasPhyDrvOsName=_CpqSasPhyDrvOsName_Object((1,3,6,1,4,1,232,5,5,2,1,1,13),_CpqSasPhyDrvOsName_Type())
cpqSasPhyDrvOsName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvOsName.setStatus(_B)
class _CpqSasPhyDrvPlacement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_p,2),(_q,3)))
_CpqSasPhyDrvPlacement_Type.__name__=_D
_CpqSasPhyDrvPlacement_Object=MibTableColumn
cpqSasPhyDrvPlacement=_CpqSasPhyDrvPlacement_Object((1,3,6,1,4,1,232,5,5,2,1,1,14),_CpqSasPhyDrvPlacement_Type())
cpqSasPhyDrvPlacement.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvPlacement.setStatus(_B)
class _CpqSasPhyDrvHotPlug_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_n,2),(_o,3)))
_CpqSasPhyDrvHotPlug_Type.__name__=_D
_CpqSasPhyDrvHotPlug_Object=MibTableColumn
cpqSasPhyDrvHotPlug=_CpqSasPhyDrvHotPlug_Object((1,3,6,1,4,1,232,5,5,2,1,1,15),_CpqSasPhyDrvHotPlug_Type())
cpqSasPhyDrvHotPlug.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvHotPlug.setStatus(_B)
class _CpqSasPhyDrvType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('sas',2),('sata',3)))
_CpqSasPhyDrvType_Type.__name__=_D
_CpqSasPhyDrvType_Object=MibTableColumn
cpqSasPhyDrvType=_CpqSasPhyDrvType_Object((1,3,6,1,4,1,232,5,5,2,1,1,16),_CpqSasPhyDrvType_Type())
cpqSasPhyDrvType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvType.setStatus(_B)
class _CpqSasPhyDrvSasAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqSasPhyDrvSasAddress_Type.__name__=_F
_CpqSasPhyDrvSasAddress_Object=MibTableColumn
cpqSasPhyDrvSasAddress=_CpqSasPhyDrvSasAddress_Object((1,3,6,1,4,1,232,5,5,2,1,1,17),_CpqSasPhyDrvSasAddress_Type())
cpqSasPhyDrvSasAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvSasAddress.setStatus(_B)
class _CpqSasPhyDrvMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('rotatingPlatters',2),('solidState',3)))
_CpqSasPhyDrvMediaType_Type.__name__=_D
_CpqSasPhyDrvMediaType_Object=MibTableColumn
cpqSasPhyDrvMediaType=_CpqSasPhyDrvMediaType_Object((1,3,6,1,4,1,232,5,5,2,1,1,18),_CpqSasPhyDrvMediaType_Type())
cpqSasPhyDrvMediaType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvMediaType.setStatus(_B)
class _CpqSasPhyDrvSSDWearStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_H,2),('fiftySixDayThreshold',3),('fivePercentThreshold',4),('twoPercentThreshold',5),(_At,6)))
_CpqSasPhyDrvSSDWearStatus_Type.__name__=_D
_CpqSasPhyDrvSSDWearStatus_Object=MibTableColumn
cpqSasPhyDrvSSDWearStatus=_CpqSasPhyDrvSSDWearStatus_Object((1,3,6,1,4,1,232,5,5,2,1,1,19),_CpqSasPhyDrvSSDWearStatus_Type())
cpqSasPhyDrvSSDWearStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvSSDWearStatus.setStatus(_B)
_CpqSasPhyDrvPowerOnHours_Type=Counter32
_CpqSasPhyDrvPowerOnHours_Object=MibTableColumn
cpqSasPhyDrvPowerOnHours=_CpqSasPhyDrvPowerOnHours_Object((1,3,6,1,4,1,232,5,5,2,1,1,20),_CpqSasPhyDrvPowerOnHours_Type())
cpqSasPhyDrvPowerOnHours.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvPowerOnHours.setStatus(_B)
_CpqSasPhyDrvSSDPercntEndrnceUsed_Type=Gauge32
_CpqSasPhyDrvSSDPercntEndrnceUsed_Object=MibTableColumn
cpqSasPhyDrvSSDPercntEndrnceUsed=_CpqSasPhyDrvSSDPercntEndrnceUsed_Object((1,3,6,1,4,1,232,5,5,2,1,1,21),_CpqSasPhyDrvSSDPercntEndrnceUsed_Type())
cpqSasPhyDrvSSDPercntEndrnceUsed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvSSDPercntEndrnceUsed.setStatus(_B)
_CpqSasPhyDrvSSDEstTimeRemainingHours_Type=Counter32
_CpqSasPhyDrvSSDEstTimeRemainingHours_Object=MibTableColumn
cpqSasPhyDrvSSDEstTimeRemainingHours=_CpqSasPhyDrvSSDEstTimeRemainingHours_Object((1,3,6,1,4,1,232,5,5,2,1,1,22),_CpqSasPhyDrvSSDEstTimeRemainingHours_Type())
cpqSasPhyDrvSSDEstTimeRemainingHours.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvSSDEstTimeRemainingHours.setStatus(_B)
class _CpqSasPhyDrvAuthenticationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_S,2),('authenticationFailed',3),('authenticationPassed',4)))
_CpqSasPhyDrvAuthenticationStatus_Type.__name__=_D
_CpqSasPhyDrvAuthenticationStatus_Object=MibTableColumn
cpqSasPhyDrvAuthenticationStatus=_CpqSasPhyDrvAuthenticationStatus_Object((1,3,6,1,4,1,232,5,5,2,1,1,23),_CpqSasPhyDrvAuthenticationStatus_Type())
cpqSasPhyDrvAuthenticationStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvAuthenticationStatus.setStatus(_B)
_CpqSasPhyDrvSmartCarrierAppFWRev_Type=Integer32
_CpqSasPhyDrvSmartCarrierAppFWRev_Object=MibTableColumn
cpqSasPhyDrvSmartCarrierAppFWRev=_CpqSasPhyDrvSmartCarrierAppFWRev_Object((1,3,6,1,4,1,232,5,5,2,1,1,24),_CpqSasPhyDrvSmartCarrierAppFWRev_Type())
cpqSasPhyDrvSmartCarrierAppFWRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvSmartCarrierAppFWRev.setStatus(_B)
_CpqSasPhyDrvSmartCarrierBootldrFWRev_Type=Integer32
_CpqSasPhyDrvSmartCarrierBootldrFWRev_Object=MibTableColumn
cpqSasPhyDrvSmartCarrierBootldrFWRev=_CpqSasPhyDrvSmartCarrierBootldrFWRev_Object((1,3,6,1,4,1,232,5,5,2,1,1,25),_CpqSasPhyDrvSmartCarrierBootldrFWRev_Type())
cpqSasPhyDrvSmartCarrierBootldrFWRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvSmartCarrierBootldrFWRev.setStatus(_B)
_CpqSasPhyDrvCurrTemperature_Type=Gauge32
_CpqSasPhyDrvCurrTemperature_Object=MibTableColumn
cpqSasPhyDrvCurrTemperature=_CpqSasPhyDrvCurrTemperature_Object((1,3,6,1,4,1,232,5,5,2,1,1,26),_CpqSasPhyDrvCurrTemperature_Type())
cpqSasPhyDrvCurrTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvCurrTemperature.setStatus(_B)
_CpqSasPhyDrvTemperatureThreshold_Type=Gauge32
_CpqSasPhyDrvTemperatureThreshold_Object=MibTableColumn
cpqSasPhyDrvTemperatureThreshold=_CpqSasPhyDrvTemperatureThreshold_Object((1,3,6,1,4,1,232,5,5,2,1,1,27),_CpqSasPhyDrvTemperatureThreshold_Type())
cpqSasPhyDrvTemperatureThreshold.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvTemperatureThreshold.setStatus(_B)
class _CpqSasPhyDrvSsBoxModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_CpqSasPhyDrvSsBoxModel_Type.__name__=_F
_CpqSasPhyDrvSsBoxModel_Object=MibTableColumn
cpqSasPhyDrvSsBoxModel=_CpqSasPhyDrvSsBoxModel_Object((1,3,6,1,4,1,232,5,5,2,1,1,28),_CpqSasPhyDrvSsBoxModel_Type())
cpqSasPhyDrvSsBoxModel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvSsBoxModel.setStatus(_B)
class _CpqSasPhyDrvSsBoxFwRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqSasPhyDrvSsBoxFwRev_Type.__name__=_F
_CpqSasPhyDrvSsBoxFwRev_Object=MibTableColumn
cpqSasPhyDrvSsBoxFwRev=_CpqSasPhyDrvSsBoxFwRev_Object((1,3,6,1,4,1,232,5,5,2,1,1,29),_CpqSasPhyDrvSsBoxFwRev_Type())
cpqSasPhyDrvSsBoxFwRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvSsBoxFwRev.setStatus(_B)
class _CpqSasPhyDrvSsBoxVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_CpqSasPhyDrvSsBoxVendor_Type.__name__=_F
_CpqSasPhyDrvSsBoxVendor_Object=MibTableColumn
cpqSasPhyDrvSsBoxVendor=_CpqSasPhyDrvSsBoxVendor_Object((1,3,6,1,4,1,232,5,5,2,1,1,30),_CpqSasPhyDrvSsBoxVendor_Type())
cpqSasPhyDrvSsBoxVendor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvSsBoxVendor.setStatus(_B)
class _CpqSasPhyDrvSsBoxSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CpqSasPhyDrvSsBoxSerialNumber_Type.__name__=_F
_CpqSasPhyDrvSsBoxSerialNumber_Object=MibTableColumn
cpqSasPhyDrvSsBoxSerialNumber=_CpqSasPhyDrvSsBoxSerialNumber_Object((1,3,6,1,4,1,232,5,5,2,1,1,31),_CpqSasPhyDrvSsBoxSerialNumber_Type())
cpqSasPhyDrvSsBoxSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasPhyDrvSsBoxSerialNumber.setStatus(_B)
_CpqSasLogDrv_ObjectIdentity=ObjectIdentity
cpqSasLogDrv=_CpqSasLogDrv_ObjectIdentity((1,3,6,1,4,1,232,5,5,3))
_CpqSasLogDrvTable_Object=MibTable
cpqSasLogDrvTable=_CpqSasLogDrvTable_Object((1,3,6,1,4,1,232,5,5,3,1))
if mibBuilder.loadTexts:cpqSasLogDrvTable.setStatus(_B)
_CpqSasLogDrvEntry_Object=MibTableRow
cpqSasLogDrvEntry=_CpqSasLogDrvEntry_Object((1,3,6,1,4,1,232,5,5,3,1,1))
cpqSasLogDrvEntry.setIndexNames((0,_C,_A1),(0,_C,_A2))
if mibBuilder.loadTexts:cpqSasLogDrvEntry.setStatus(_B)
_CpqSasLogDrvHbaIndex_Type=Integer32
_CpqSasLogDrvHbaIndex_Object=MibTableColumn
cpqSasLogDrvHbaIndex=_CpqSasLogDrvHbaIndex_Object((1,3,6,1,4,1,232,5,5,3,1,1,1),_CpqSasLogDrvHbaIndex_Type())
cpqSasLogDrvHbaIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasLogDrvHbaIndex.setStatus(_B)
_CpqSasLogDrvIndex_Type=Integer32
_CpqSasLogDrvIndex_Object=MibTableColumn
cpqSasLogDrvIndex=_CpqSasLogDrvIndex_Object((1,3,6,1,4,1,232,5,5,3,1,1,2),_CpqSasLogDrvIndex_Type())
cpqSasLogDrvIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasLogDrvIndex.setStatus(_B)
class _CpqSasLogDrvRaidLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),('raid0',2),('raid1',3),('raid0plus1',4),('raid5',5),('raid15',6),('volume',7)))
_CpqSasLogDrvRaidLevel_Type.__name__=_D
_CpqSasLogDrvRaidLevel_Object=MibTableColumn
cpqSasLogDrvRaidLevel=_CpqSasLogDrvRaidLevel_Object((1,3,6,1,4,1,232,5,5,3,1,1,3),_CpqSasLogDrvRaidLevel_Type())
cpqSasLogDrvRaidLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasLogDrvRaidLevel.setStatus(_B)
class _CpqSasLogDrvStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_H,2),(_N,3),(_AS,4),(_M,5),(_P,6)))
_CpqSasLogDrvStatus_Type.__name__=_D
_CpqSasLogDrvStatus_Object=MibTableColumn
cpqSasLogDrvStatus=_CpqSasLogDrvStatus_Object((1,3,6,1,4,1,232,5,5,3,1,1,4),_CpqSasLogDrvStatus_Type())
cpqSasLogDrvStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasLogDrvStatus.setStatus(_B)
class _CpqSasLogDrvCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_N,3),(_M,4)))
_CpqSasLogDrvCondition_Type.__name__=_D
_CpqSasLogDrvCondition_Object=MibTableColumn
cpqSasLogDrvCondition=_CpqSasLogDrvCondition_Object((1,3,6,1,4,1,232,5,5,3,1,1,5),_CpqSasLogDrvCondition_Type())
cpqSasLogDrvCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasLogDrvCondition.setStatus(_B)
_CpqSasLogDrvRebuildingDisk_Type=Integer32
_CpqSasLogDrvRebuildingDisk_Object=MibTableColumn
cpqSasLogDrvRebuildingDisk=_CpqSasLogDrvRebuildingDisk_Object((1,3,6,1,4,1,232,5,5,3,1,1,6),_CpqSasLogDrvRebuildingDisk_Type())
cpqSasLogDrvRebuildingDisk.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasLogDrvRebuildingDisk.setStatus(_B)
class _CpqSasLogDrvCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSasLogDrvCapacity_Type.__name__=_D
_CpqSasLogDrvCapacity_Object=MibTableColumn
cpqSasLogDrvCapacity=_CpqSasLogDrvCapacity_Object((1,3,6,1,4,1,232,5,5,3,1,1,7),_CpqSasLogDrvCapacity_Type())
cpqSasLogDrvCapacity.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasLogDrvCapacity.setStatus(_B)
_CpqSasLogDrvStripeSize_Type=Integer32
_CpqSasLogDrvStripeSize_Object=MibTableColumn
cpqSasLogDrvStripeSize=_CpqSasLogDrvStripeSize_Object((1,3,6,1,4,1,232,5,5,3,1,1,8),_CpqSasLogDrvStripeSize_Type())
cpqSasLogDrvStripeSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasLogDrvStripeSize.setStatus(_B)
class _CpqSasLogDrvPhyDrvIds_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqSasLogDrvPhyDrvIds_Type.__name__=_O
_CpqSasLogDrvPhyDrvIds_Object=MibTableColumn
cpqSasLogDrvPhyDrvIds=_CpqSasLogDrvPhyDrvIds_Object((1,3,6,1,4,1,232,5,5,3,1,1,9),_CpqSasLogDrvPhyDrvIds_Type())
cpqSasLogDrvPhyDrvIds.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasLogDrvPhyDrvIds.setStatus(_B)
class _CpqSasLogDrvSpareIds_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqSasLogDrvSpareIds_Type.__name__=_O
_CpqSasLogDrvSpareIds_Object=MibTableColumn
cpqSasLogDrvSpareIds=_CpqSasLogDrvSpareIds_Object((1,3,6,1,4,1,232,5,5,3,1,1,10),_CpqSasLogDrvSpareIds_Type())
cpqSasLogDrvSpareIds.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasLogDrvSpareIds.setStatus(_B)
class _CpqSasLogDrvOsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSasLogDrvOsName_Type.__name__=_F
_CpqSasLogDrvOsName_Object=MibTableColumn
cpqSasLogDrvOsName=_CpqSasLogDrvOsName_Object((1,3,6,1,4,1,232,5,5,3,1,1,11),_CpqSasLogDrvOsName_Type())
cpqSasLogDrvOsName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasLogDrvOsName.setStatus(_B)
_CpqSasLogDrvRebuildingPercent_Type=Gauge32
_CpqSasLogDrvRebuildingPercent_Object=MibTableColumn
cpqSasLogDrvRebuildingPercent=_CpqSasLogDrvRebuildingPercent_Object((1,3,6,1,4,1,232,5,5,3,1,1,12),_CpqSasLogDrvRebuildingPercent_Type())
cpqSasLogDrvRebuildingPercent.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasLogDrvRebuildingPercent.setStatus(_B)
_CpqSasTapeDrv_ObjectIdentity=ObjectIdentity
cpqSasTapeDrv=_CpqSasTapeDrv_ObjectIdentity((1,3,6,1,4,1,232,5,5,4))
_CpqSasTapeDrvTable_Object=MibTable
cpqSasTapeDrvTable=_CpqSasTapeDrvTable_Object((1,3,6,1,4,1,232,5,5,4,1))
if mibBuilder.loadTexts:cpqSasTapeDrvTable.setStatus(_B)
_CpqSasTapeDrvEntry_Object=MibTableRow
cpqSasTapeDrvEntry=_CpqSasTapeDrvEntry_Object((1,3,6,1,4,1,232,5,5,4,1,1))
cpqSasTapeDrvEntry.setIndexNames((0,_C,_A3),(0,_C,_A4))
if mibBuilder.loadTexts:cpqSasTapeDrvEntry.setStatus(_B)
_CpqSasTapeDrvHbaIndex_Type=Integer32
_CpqSasTapeDrvHbaIndex_Object=MibTableColumn
cpqSasTapeDrvHbaIndex=_CpqSasTapeDrvHbaIndex_Object((1,3,6,1,4,1,232,5,5,4,1,1,1),_CpqSasTapeDrvHbaIndex_Type())
cpqSasTapeDrvHbaIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasTapeDrvHbaIndex.setStatus(_B)
_CpqSasTapeDrvIndex_Type=Integer32
_CpqSasTapeDrvIndex_Object=MibTableColumn
cpqSasTapeDrvIndex=_CpqSasTapeDrvIndex_Object((1,3,6,1,4,1,232,5,5,4,1,1,2),_CpqSasTapeDrvIndex_Type())
cpqSasTapeDrvIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasTapeDrvIndex.setStatus(_B)
class _CpqSasTapeDrvLocationString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSasTapeDrvLocationString_Type.__name__=_F
_CpqSasTapeDrvLocationString_Object=MibTableColumn
cpqSasTapeDrvLocationString=_CpqSasTapeDrvLocationString_Object((1,3,6,1,4,1,232,5,5,4,1,1,3),_CpqSasTapeDrvLocationString_Type())
cpqSasTapeDrvLocationString.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasTapeDrvLocationString.setStatus(_B)
class _CpqSasTapeDrvName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CpqSasTapeDrvName_Type.__name__=_F
_CpqSasTapeDrvName_Object=MibTableColumn
cpqSasTapeDrvName=_CpqSasTapeDrvName_Object((1,3,6,1,4,1,232,5,5,4,1,1,4),_CpqSasTapeDrvName_Type())
cpqSasTapeDrvName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasTapeDrvName.setStatus(_B)
class _CpqSasTapeDrvStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_P,3)))
_CpqSasTapeDrvStatus_Type.__name__=_D
_CpqSasTapeDrvStatus_Object=MibTableColumn
cpqSasTapeDrvStatus=_CpqSasTapeDrvStatus_Object((1,3,6,1,4,1,232,5,5,4,1,1,5),_CpqSasTapeDrvStatus_Type())
cpqSasTapeDrvStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasTapeDrvStatus.setStatus(_B)
class _CpqSasTapeDrvCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_N,3),(_M,4)))
_CpqSasTapeDrvCondition_Type.__name__=_D
_CpqSasTapeDrvCondition_Object=MibTableColumn
cpqSasTapeDrvCondition=_CpqSasTapeDrvCondition_Object((1,3,6,1,4,1,232,5,5,4,1,1,6),_CpqSasTapeDrvCondition_Type())
cpqSasTapeDrvCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasTapeDrvCondition.setStatus(_B)
class _CpqSasTapeDrvFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqSasTapeDrvFWRev_Type.__name__=_F
_CpqSasTapeDrvFWRev_Object=MibTableColumn
cpqSasTapeDrvFWRev=_CpqSasTapeDrvFWRev_Object((1,3,6,1,4,1,232,5,5,4,1,1,7),_CpqSasTapeDrvFWRev_Type())
cpqSasTapeDrvFWRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasTapeDrvFWRev.setStatus(_B)
class _CpqSasTapeDrvSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CpqSasTapeDrvSerialNumber_Type.__name__=_F
_CpqSasTapeDrvSerialNumber_Object=MibTableColumn
cpqSasTapeDrvSerialNumber=_CpqSasTapeDrvSerialNumber_Object((1,3,6,1,4,1,232,5,5,4,1,1,8),_CpqSasTapeDrvSerialNumber_Type())
cpqSasTapeDrvSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasTapeDrvSerialNumber.setStatus(_B)
class _CpqSasTapeDrvSasAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqSasTapeDrvSasAddress_Type.__name__=_F
_CpqSasTapeDrvSasAddress_Object=MibTableColumn
cpqSasTapeDrvSasAddress=_CpqSasTapeDrvSasAddress_Object((1,3,6,1,4,1,232,5,5,4,1,1,9),_CpqSasTapeDrvSasAddress_Type())
cpqSasTapeDrvSasAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSasTapeDrvSasAddress.setStatus(_B)
_CpqSbScsiBus_ObjectIdentity=ObjectIdentity
cpqSbScsiBus=_CpqSbScsiBus_ObjectIdentity((1,3,6,1,4,1,232,7))
_CpqSbScsiMibRev_ObjectIdentity=ObjectIdentity
cpqSbScsiMibRev=_CpqSbScsiMibRev_ObjectIdentity((1,3,6,1,4,1,232,7,1))
class _CpqSbMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqSbMibRevMajor_Type.__name__=_D
_CpqSbMibRevMajor_Object=MibScalar
cpqSbMibRevMajor=_CpqSbMibRevMajor_Object((1,3,6,1,4,1,232,7,1,1),_CpqSbMibRevMajor_Type())
cpqSbMibRevMajor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSbMibRevMajor.setStatus(_E)
class _CpqSbMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSbMibRevMinor_Type.__name__=_D
_CpqSbMibRevMinor_Object=MibScalar
cpqSbMibRevMinor=_CpqSbMibRevMinor_Object((1,3,6,1,4,1,232,7,1,2),_CpqSbMibRevMinor_Type())
cpqSbMibRevMinor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSbMibRevMinor.setStatus(_E)
_CpqSbDevice_ObjectIdentity=ObjectIdentity
cpqSbDevice=_CpqSbDevice_ObjectIdentity((1,3,6,1,4,1,232,7,2))
_CpqSbDeviceTable_Object=MibTable
cpqSbDeviceTable=_CpqSbDeviceTable_Object((1,3,6,1,4,1,232,7,2,2))
if mibBuilder.loadTexts:cpqSbDeviceTable.setStatus(_E)
_CpqSbDeviceEntry_Object=MibTableRow
cpqSbDeviceEntry=_CpqSbDeviceEntry_Object((1,3,6,1,4,1,232,7,2,2,1))
cpqSbDeviceEntry.setIndexNames((0,_C,_Au),(0,_C,_Av),(0,_C,_Aw))
if mibBuilder.loadTexts:cpqSbDeviceEntry.setStatus(_E)
class _CpqSbDevCntlrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSbDevCntlrIndex_Type.__name__=_D
_CpqSbDevCntlrIndex_Object=MibTableColumn
cpqSbDevCntlrIndex=_CpqSbDevCntlrIndex_Object((1,3,6,1,4,1,232,7,2,2,1,1),_CpqSbDevCntlrIndex_Type())
cpqSbDevCntlrIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSbDevCntlrIndex.setStatus(_E)
class _CpqSbDevBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSbDevBusIndex_Type.__name__=_D
_CpqSbDevBusIndex_Object=MibTableColumn
cpqSbDevBusIndex=_CpqSbDevBusIndex_Object((1,3,6,1,4,1,232,7,2,2,1,2),_CpqSbDevBusIndex_Type())
cpqSbDevBusIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSbDevBusIndex.setStatus(_E)
class _CpqSbDevScsiIdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSbDevScsiIdIndex_Type.__name__=_D
_CpqSbDevScsiIdIndex_Object=MibTableColumn
cpqSbDevScsiIdIndex=_CpqSbDevScsiIdIndex_Object((1,3,6,1,4,1,232,7,2,2,1,3),_CpqSbDevScsiIdIndex_Type())
cpqSbDevScsiIdIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSbDevScsiIdIndex.setStatus(_E)
class _CpqSbDevType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_G,1),('disk',2),('tape',3),('printer',4),(_AZ,5),(_Aa,6),('cd-rom',7),('scanner',8),('optical',9),('jukeBox',10),('commDev',11)))
_CpqSbDevType_Type.__name__=_D
_CpqSbDevType_Object=MibTableColumn
cpqSbDevType=_CpqSbDevType_Object((1,3,6,1,4,1,232,7,2,2,1,4),_CpqSbDevType_Type())
cpqSbDevType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSbDevType.setStatus(_E)
class _CpqSbDevModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_CpqSbDevModel_Type.__name__=_F
_CpqSbDevModel_Object=MibTableColumn
cpqSbDevModel=_CpqSbDevModel_Object((1,3,6,1,4,1,232,7,2,2,1,5),_CpqSbDevModel_Type())
cpqSbDevModel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSbDevModel.setStatus(_E)
class _CpqSbDevFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqSbDevFWRev_Type.__name__=_F
_CpqSbDevFWRev_Object=MibTableColumn
cpqSbDevFWRev=_CpqSbDevFWRev_Object((1,3,6,1,4,1,232,7,2,2,1,6),_CpqSbDevFWRev_Type())
cpqSbDevFWRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSbDevFWRev.setStatus(_E)
class _CpqSbDevVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_CpqSbDevVendor_Type.__name__=_F
_CpqSbDevVendor_Object=MibTableColumn
cpqSbDevVendor=_CpqSbDevVendor_Object((1,3,6,1,4,1,232,7,2,2,1,7),_CpqSbDevVendor_Type())
cpqSbDevVendor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSbDevVendor.setStatus(_E)
_CpqSbDevParityErrs_Type=Counter32
_CpqSbDevParityErrs_Object=MibTableColumn
cpqSbDevParityErrs=_CpqSbDevParityErrs_Object((1,3,6,1,4,1,232,7,2,2,1,8),_CpqSbDevParityErrs_Type())
cpqSbDevParityErrs.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSbDevParityErrs.setStatus(_E)
_CpqSbDevPhaseErrs_Type=Counter32
_CpqSbDevPhaseErrs_Object=MibTableColumn
cpqSbDevPhaseErrs=_CpqSbDevPhaseErrs_Object((1,3,6,1,4,1,232,7,2,2,1,9),_CpqSbDevPhaseErrs_Type())
cpqSbDevPhaseErrs.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSbDevPhaseErrs.setStatus(_E)
_CpqSbDevSelectTimeouts_Type=Counter32
_CpqSbDevSelectTimeouts_Object=MibTableColumn
cpqSbDevSelectTimeouts=_CpqSbDevSelectTimeouts_Object((1,3,6,1,4,1,232,7,2,2,1,10),_CpqSbDevSelectTimeouts_Type())
cpqSbDevSelectTimeouts.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSbDevSelectTimeouts.setStatus(_E)
_CpqSbDevMsgRejects_Type=Counter32
_CpqSbDevMsgRejects_Object=MibTableColumn
cpqSbDevMsgRejects=_CpqSbDevMsgRejects_Object((1,3,6,1,4,1,232,7,2,2,1,11),_CpqSbDevMsgRejects_Type())
cpqSbDevMsgRejects.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSbDevMsgRejects.setStatus(_E)
class _CpqSbDevNegPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSbDevNegPeriod_Type.__name__=_D
_CpqSbDevNegPeriod_Object=MibTableColumn
cpqSbDevNegPeriod=_CpqSbDevNegPeriod_Object((1,3,6,1,4,1,232,7,2,2,1,12),_CpqSbDevNegPeriod_Type())
cpqSbDevNegPeriod.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSbDevNegPeriod.setStatus(_E)
class _CpqSbDevLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_m,2)))
_CpqSbDevLocation_Type.__name__=_D
_CpqSbDevLocation_Object=MibTableColumn
cpqSbDevLocation=_CpqSbDevLocation_Object((1,3,6,1,4,1,232,7,2,2,1,13),_CpqSbDevLocation_Type())
cpqSbDevLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSbDevLocation.setStatus(_E)
cpqScsi2CntlrStatusChange=NotificationType((1,3,6,1,4,1,232,0,5001))
cpqScsi2CntlrStatusChange.setObjects((_C,_e))
if mibBuilder.loadTexts:cpqScsi2CntlrStatusChange.setStatus('')
cpqScsi2LogDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,5002))
cpqScsi2LogDrvStatusChange.setObjects((_C,_f))
if mibBuilder.loadTexts:cpqScsi2LogDrvStatusChange.setStatus('')
cpqScsi2PhyDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,5003))
cpqScsi2PhyDrvStatusChange.setObjects((_C,_R))
if mibBuilder.loadTexts:cpqScsi2PhyDrvStatusChange.setStatus('')
cpqTapePhyDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,5004))
cpqTapePhyDrvStatusChange.setObjects((_C,_T))
if mibBuilder.loadTexts:cpqTapePhyDrvStatusChange.setStatus('')
cpqScsi3CntlrStatusChange=NotificationType((1,3,6,1,4,1,232,0,5005))
cpqScsi3CntlrStatusChange.setObjects(*((_K,_L),(_I,_J),(_C,_e)))
if mibBuilder.loadTexts:cpqScsi3CntlrStatusChange.setStatus('')
cpqScsi3PhyDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,5006))
cpqScsi3PhyDrvStatusChange.setObjects(*((_K,_L),(_I,_J),(_C,_R)))
if mibBuilder.loadTexts:cpqScsi3PhyDrvStatusChange.setStatus('')
cpqTape3PhyDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,5007))
cpqTape3PhyDrvStatusChange.setObjects(*((_K,_L),(_I,_J),(_C,_T)))
if mibBuilder.loadTexts:cpqTape3PhyDrvStatusChange.setStatus('')
cpqTape3PhyDrvCleaningRequired=NotificationType((1,3,6,1,4,1,232,0,5008))
cpqTape3PhyDrvCleaningRequired.setObjects(*((_K,_L),(_I,_J),(_C,_T)))
if mibBuilder.loadTexts:cpqTape3PhyDrvCleaningRequired.setStatus('')
cpqTape3PhyDrvCleanTapeReplace=NotificationType((1,3,6,1,4,1,232,0,5009))
cpqTape3PhyDrvCleanTapeReplace.setObjects(*((_K,_L),(_I,_J),(_C,_T)))
if mibBuilder.loadTexts:cpqTape3PhyDrvCleanTapeReplace.setStatus('')
cpqTape3LibraryFailed=NotificationType((1,3,6,1,4,1,232,0,5010))
cpqTape3LibraryFailed.setObjects(*((_K,_L),(_I,_J),(_C,_Q)))
if mibBuilder.loadTexts:cpqTape3LibraryFailed.setStatus('')
cpqTape3LibraryOkay=NotificationType((1,3,6,1,4,1,232,0,5011))
cpqTape3LibraryOkay.setObjects(*((_K,_L),(_I,_J),(_C,_Q)))
if mibBuilder.loadTexts:cpqTape3LibraryOkay.setStatus('')
cpqTape3LibraryDegraded=NotificationType((1,3,6,1,4,1,232,0,5012))
cpqTape3LibraryDegraded.setObjects(*((_K,_L),(_I,_J),(_C,_Q)))
if mibBuilder.loadTexts:cpqTape3LibraryDegraded.setStatus('')
cpqTape3LibraryDoorOpen=NotificationType((1,3,6,1,4,1,232,0,5013))
cpqTape3LibraryDoorOpen.setObjects(*((_K,_L),(_I,_J),(_C,_Q)))
if mibBuilder.loadTexts:cpqTape3LibraryDoorOpen.setStatus('')
cpqTape3LibraryDoorClosed=NotificationType((1,3,6,1,4,1,232,0,5014))
cpqTape3LibraryDoorClosed.setObjects(*((_K,_L),(_I,_J),(_C,_Q)))
if mibBuilder.loadTexts:cpqTape3LibraryDoorClosed.setStatus('')
cpqScsiCdLibraryStatusChange=NotificationType((1,3,6,1,4,1,232,0,5015))
cpqScsiCdLibraryStatusChange.setObjects(*((_K,_L),(_I,_J),(_C,_r),(_C,_s),(_C,_t),(_C,_Ax)))
if mibBuilder.loadTexts:cpqScsiCdLibraryStatusChange.setStatus('')
cpqTape4PhyDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,5016))
cpqTape4PhyDrvStatusChange.setObjects(*((_K,_L),(_I,_J),(_C,_Z),(_C,_a),(_C,_b),(_C,_A5)))
if mibBuilder.loadTexts:cpqTape4PhyDrvStatusChange.setStatus('')
cpqScsi4PhyDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,5017))
cpqScsi4PhyDrvStatusChange.setObjects(*((_K,_L),(_I,_J),(_C,_R),(_C,_W),(_C,_X),(_C,_Y),(_C,_A6),(_C,_A7),(_C,_A8),(_C,_A9)))
if mibBuilder.loadTexts:cpqScsi4PhyDrvStatusChange.setStatus('')
cpqTapeLibraryStatusChange=NotificationType((1,3,6,1,4,1,232,0,5018))
cpqTapeLibraryStatusChange.setObjects(*((_K,_L),(_I,_J),(_C,_x),(_C,_y),(_C,_z),(_C,_A0),(_C,_Ay),(_C,_Az),(_C,_Q),(_C,_A_)))
if mibBuilder.loadTexts:cpqTapeLibraryStatusChange.setStatus('')
cpqTape5PhyDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,5019))
cpqTape5PhyDrvStatusChange.setObjects(*((_K,_L),(_I,_J),(_C,_Z),(_C,_a),(_C,_b),(_C,_u),(_C,_B0),(_C,_B1),(_C,_B2),(_C,_A5)))
if mibBuilder.loadTexts:cpqTape5PhyDrvStatusChange.setStatus('')
cpqScsi5PhyDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,5020))
cpqScsi5PhyDrvStatusChange.setObjects(*((_K,_L),(_I,_J),(_C,_R),(_C,_W),(_C,_X),(_C,_Y),(_C,_A6),(_C,_A7),(_C,_A8),(_C,_A9),(_C,_B3)))
if mibBuilder.loadTexts:cpqScsi5PhyDrvStatusChange.setStatus('')
cpqScsi3LogDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,5021))
cpqScsi3LogDrvStatusChange.setObjects(*((_K,_L),(_I,_J),(_C,_f),(_C,_g),(_C,_h),(_C,_i),(_C,_B4)))
if mibBuilder.loadTexts:cpqScsi3LogDrvStatusChange.setStatus('')
cpqSasPhyDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,5022))
cpqSasPhyDrvStatusChange.setObjects(*((_K,_L),(_I,_J),(_C,_U),(_C,_AA),(_C,_c),(_C,_d),(_C,_B5),(_C,_AB),(_C,_AC),(_C,_AD),(_C,_AE),(_C,_AF)))
if mibBuilder.loadTexts:cpqSasPhyDrvStatusChange.setStatus('')
cpqSasLogDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,5023))
cpqSasLogDrvStatusChange.setObjects(*((_K,_L),(_I,_J),(_C,_U),(_C,_A1),(_C,_A2),(_C,_B6),(_C,_B7)))
if mibBuilder.loadTexts:cpqSasLogDrvStatusChange.setStatus('')
cpqSas2TapeDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,5025))
cpqSas2TapeDrvStatusChange.setObjects(*((_K,_L),(_I,_J),(_C,_U),(_C,_B8),(_C,_A3),(_C,_A4),(_C,_B9),(_C,_BA),(_C,_BB),(_C,_BC),(_C,_BD)))
if mibBuilder.loadTexts:cpqSas2TapeDrvStatusChange.setStatus('')
cpqSasPhyDrvSSDWearStatusChange=NotificationType((1,3,6,1,4,1,232,0,5026))
cpqSasPhyDrvSSDWearStatusChange.setObjects(*((_K,_L),(_I,_J),(_C,_U),(_C,_AA),(_C,_c),(_C,_d),(_C,_AB),(_C,_AC),(_C,_AD),(_C,_AE),(_C,_AF),(_C,_BE)))
if mibBuilder.loadTexts:cpqSasPhyDrvSSDWearStatusChange.setStatus('')
cpqScsiCntlrStatusChange=NotificationType((1,3,6,1,4,1,232,5,0,1))
cpqScsiCntlrStatusChange.setObjects((_C,_e))
if mibBuilder.loadTexts:cpqScsiCntlrStatusChange.setStatus('')
cpqScsiLogDrvStatusChange=NotificationType((1,3,6,1,4,1,232,5,0,2))
cpqScsiLogDrvStatusChange.setObjects((_C,_f))
if mibBuilder.loadTexts:cpqScsiLogDrvStatusChange.setStatus('')
cpqScsiPhyDrvStatusChange=NotificationType((1,3,6,1,4,1,232,5,0,3))
cpqScsiPhyDrvStatusChange.setObjects((_C,_R))
if mibBuilder.loadTexts:cpqScsiPhyDrvStatusChange.setStatus('')
mibBuilder.exportSymbols(_C,**{_Ak:cpqScsi2CntlrStatusChange,_Al:cpqScsi2LogDrvStatusChange,_Am:cpqScsi2PhyDrvStatusChange,'cpqTapePhyDrvStatusChange':cpqTapePhyDrvStatusChange,'cpqScsi3CntlrStatusChange':cpqScsi3CntlrStatusChange,'cpqScsi3PhyDrvStatusChange':cpqScsi3PhyDrvStatusChange,'cpqTape3PhyDrvStatusChange':cpqTape3PhyDrvStatusChange,'cpqTape3PhyDrvCleaningRequired':cpqTape3PhyDrvCleaningRequired,'cpqTape3PhyDrvCleanTapeReplace':cpqTape3PhyDrvCleanTapeReplace,'cpqTape3LibraryFailed':cpqTape3LibraryFailed,'cpqTape3LibraryOkay':cpqTape3LibraryOkay,'cpqTape3LibraryDegraded':cpqTape3LibraryDegraded,'cpqTape3LibraryDoorOpen':cpqTape3LibraryDoorOpen,'cpqTape3LibraryDoorClosed':cpqTape3LibraryDoorClosed,'cpqScsiCdLibraryStatusChange':cpqScsiCdLibraryStatusChange,'cpqTape4PhyDrvStatusChange':cpqTape4PhyDrvStatusChange,'cpqScsi4PhyDrvStatusChange':cpqScsi4PhyDrvStatusChange,'cpqTapeLibraryStatusChange':cpqTapeLibraryStatusChange,'cpqTape5PhyDrvStatusChange':cpqTape5PhyDrvStatusChange,'cpqScsi5PhyDrvStatusChange':cpqScsi5PhyDrvStatusChange,'cpqScsi3LogDrvStatusChange':cpqScsi3LogDrvStatusChange,'cpqSasPhyDrvStatusChange':cpqSasPhyDrvStatusChange,'cpqSasLogDrvStatusChange':cpqSasLogDrvStatusChange,'cpqSas2TapeDrvStatusChange':cpqSas2TapeDrvStatusChange,'cpqSasPhyDrvSSDWearStatusChange':cpqSasPhyDrvSSDWearStatusChange,'cpqScsi':cpqScsi,_Ah:cpqScsiCntlrStatusChange,_Ai:cpqScsiLogDrvStatusChange,_Aj:cpqScsiPhyDrvStatusChange,'cpqScsiMibRev':cpqScsiMibRev,'cpqScsiMibRevMajor':cpqScsiMibRevMajor,'cpqScsiMibRevMinor':cpqScsiMibRevMinor,'cpqScsiMibCondition':cpqScsiMibCondition,'cpqScsiComponent':cpqScsiComponent,'cpqScsiInterface':cpqScsiInterface,'cpqScsiOsNetWare':cpqScsiOsNetWare,'cpqScsiNw3xDriverName':cpqScsiNw3xDriverName,'cpqScsiNw3xDriverVers':cpqScsiNw3xDriverVers,'cpqScsiNw3xDriverPollType':cpqScsiNw3xDriverPollType,'cpqScsiNw3xDriverPollTime':cpqScsiNw3xDriverPollTime,'cpqScsiNw3xCntlrInfoTable':cpqScsiNw3xCntlrInfoTable,'cpqScsiNw3xCntlrInfoEntry':cpqScsiNw3xCntlrInfoEntry,_AH:cpqScsiNw3xCntlrIndex,_AI:cpqScsiNw3xBusIndex,'cpqScsiNw3xXptDesc':cpqScsiNw3xXptDesc,'cpqScsiNw3xXptVers':cpqScsiNw3xXptVers,'cpqScsiNw3xSimDesc':cpqScsiNw3xSimDesc,'cpqScsiNw3xSimVers':cpqScsiNw3xSimVers,'cpqScsiNw3xHbaDesc':cpqScsiNw3xHbaDesc,'cpqScsiLogDrvStatTable':cpqScsiLogDrvStatTable,'cpqScsiLogDrvStatEntry':cpqScsiLogDrvStatEntry,_AJ:cpqScsiNw3xStatCntlrIndex,_AK:cpqScsiNw3xStatBusIndex,_AL:cpqScsiNw3xStatLogDrvIndex,'cpqScsiNw3xTotalReads':cpqScsiNw3xTotalReads,'cpqScsiNw3xTotalWrites':cpqScsiNw3xTotalWrites,'cpqScsiNw3xCorrReads':cpqScsiNw3xCorrReads,'cpqScsiNw3xCorrWrites':cpqScsiNw3xCorrWrites,'cpqScsiNw3xFatalReads':cpqScsiNw3xFatalReads,'cpqScsiNw3xFatalWrites':cpqScsiNw3xFatalWrites,'cpqScsiVolMapTable':cpqScsiVolMapTable,'cpqScsiVolMapEntry':cpqScsiVolMapEntry,_AM:cpqScsiNw3xVolCntlrIndex,_AN:cpqScsiNw3xVolBusIndex,_AO:cpqScsiNw3xVolLogDrvIndex,'cpqScsiNw3xVolMap':cpqScsiNw3xVolMap,'cpqScsiOsCommon':cpqScsiOsCommon,'cpqScsiOsCommonPollFreq':cpqScsiOsCommonPollFreq,'cpqScsiOsCommonModuleTable':cpqScsiOsCommonModuleTable,'cpqScsiOsCommonModuleEntry':cpqScsiOsCommonModuleEntry,_AP:cpqScsiOsCommonModuleIndex,'cpqScsiOsCommonModuleName':cpqScsiOsCommonModuleName,'cpqScsiOsCommonModuleVersion':cpqScsiOsCommonModuleVersion,'cpqScsiOsCommonModuleDate':cpqScsiOsCommonModuleDate,'cpqScsiOsCommonModulePurpose':cpqScsiOsCommonModulePurpose,'cpqScsiCntlr':cpqScsiCntlr,'cpqScsiCntlrTable':cpqScsiCntlrTable,'cpqScsiCntlrEntry':cpqScsiCntlrEntry,_AQ:cpqScsiCntlrIndex,_AR:cpqScsiCntlrBusIndex,'cpqScsiCntlrModel':cpqScsiCntlrModel,'cpqScsiCntlrFWVers':cpqScsiCntlrFWVers,'cpqScsiCntlrSWVers':cpqScsiCntlrSWVers,'cpqScsiCntlrSlot':cpqScsiCntlrSlot,_e:cpqScsiCntlrStatus,'cpqScsiCntlrHardResets':cpqScsiCntlrHardResets,'cpqScsiCntlrSoftResets':cpqScsiCntlrSoftResets,'cpqScsiCntlrTimeouts':cpqScsiCntlrTimeouts,'cpqScsiCntlrBaseIOAddr':cpqScsiCntlrBaseIOAddr,'cpqScsiCntlrCondition':cpqScsiCntlrCondition,'cpqScsiCntlrSerialNum':cpqScsiCntlrSerialNum,'cpqScsiCntlrBusWidth':cpqScsiCntlrBusWidth,'cpqScsiCntlrModelExtended':cpqScsiCntlrModelExtended,'cpqScsiCntlrHwLocation':cpqScsiCntlrHwLocation,'cpqScsiCntlrPciLocation':cpqScsiCntlrPciLocation,'cpqScsiLogDrv':cpqScsiLogDrv,'cpqScsiLogDrvTable':cpqScsiLogDrvTable,'cpqScsiLogDrvEntry':cpqScsiLogDrvEntry,_g:cpqScsiLogDrvCntlrIndex,_h:cpqScsiLogDrvBusIndex,_i:cpqScsiLogDrvIndex,'cpqScsiLogDrvFaultTol':cpqScsiLogDrvFaultTol,_f:cpqScsiLogDrvStatus,'cpqScsiLogDrvSize':cpqScsiLogDrvSize,'cpqScsiLogDrvPhyDrvIDs':cpqScsiLogDrvPhyDrvIDs,'cpqScsiLogDrvCondition':cpqScsiLogDrvCondition,'cpqScsiLogDrvStripeSize':cpqScsiLogDrvStripeSize,'cpqScsiLogDrvAvailSpares':cpqScsiLogDrvAvailSpares,'cpqScsiLogDrvPercentRebuild':cpqScsiLogDrvPercentRebuild,_B4:cpqScsiLogDrvOsName,'cpqScsiPhyDrv':cpqScsiPhyDrv,'cpqScsiPhyDrvTable':cpqScsiPhyDrvTable,'cpqScsiPhyDrvEntry':cpqScsiPhyDrvEntry,_W:cpqScsiPhyDrvCntlrIndex,_X:cpqScsiPhyDrvBusIndex,_Y:cpqScsiPhyDrvIndex,_A7:cpqScsiPhyDrvModel,_A8:cpqScsiPhyDrvFWRev,_A6:cpqScsiPhyDrvVendor,'cpqScsiPhyDrvSize':cpqScsiPhyDrvSize,'cpqScsiPhyDrvScsiID':cpqScsiPhyDrvScsiID,_R:cpqScsiPhyDrvStatus,'cpqScsiPhyDrvServiceHours':cpqScsiPhyDrvServiceHours,'cpqScsiPhyDrvHighReadSectors':cpqScsiPhyDrvHighReadSectors,'cpqScsiPhyDrvLowReadSectors':cpqScsiPhyDrvLowReadSectors,'cpqScsiPhyDrvHighWriteSectors':cpqScsiPhyDrvHighWriteSectors,'cpqScsiPhyDrvLowWriteSectors':cpqScsiPhyDrvLowWriteSectors,'cpqScsiPhyDrvHardReadErrs':cpqScsiPhyDrvHardReadErrs,'cpqScsiPhyDrvHardWriteErrs':cpqScsiPhyDrvHardWriteErrs,'cpqScsiPhyDrvEccCorrReads':cpqScsiPhyDrvEccCorrReads,'cpqScsiPhyDrvRecvReadErrs':cpqScsiPhyDrvRecvReadErrs,'cpqScsiPhyDrvRecvWriteErrs':cpqScsiPhyDrvRecvWriteErrs,'cpqScsiPhyDrvSeekErrs':cpqScsiPhyDrvSeekErrs,'cpqScsiPhyDrvSpinupTime':cpqScsiPhyDrvSpinupTime,'cpqScsiPhyDrvUsedReallocs':cpqScsiPhyDrvUsedReallocs,'cpqScsiPhyDrvTimeouts':cpqScsiPhyDrvTimeouts,'cpqScsiPhyDrvPostErrs':cpqScsiPhyDrvPostErrs,'cpqScsiPhyDrvPostErrCode':cpqScsiPhyDrvPostErrCode,'cpqScsiPhyDrvCondition':cpqScsiPhyDrvCondition,'cpqScsiPhyDrvFuncTest1':cpqScsiPhyDrvFuncTest1,'cpqScsiPhyDrvFuncTest2':cpqScsiPhyDrvFuncTest2,'cpqScsiPhyDrvStatsPreserved':cpqScsiPhyDrvStatsPreserved,_A9:cpqScsiPhyDrvSerialNum,'cpqScsiPhyDrvLocation':cpqScsiPhyDrvLocation,'cpqScsiPhyDrvParent':cpqScsiPhyDrvParent,'cpqScsiPhyDrvSectorSize':cpqScsiPhyDrvSectorSize,'cpqScsiPhyDrvHotPlug':cpqScsiPhyDrvHotPlug,'cpqScsiPhyDrvPlacement':cpqScsiPhyDrvPlacement,'cpqScsiPhyDrvPreFailMonitoring':cpqScsiPhyDrvPreFailMonitoring,_B3:cpqScsiPhyDrvOsName,'cpqScsiPhyDrvRotationalSpeed':cpqScsiPhyDrvRotationalSpeed,'cpqScsiPhyDrvMemberLogDrv':cpqScsiPhyDrvMemberLogDrv,'cpqScsiTarget':cpqScsiTarget,'cpqScsiTargetTable':cpqScsiTargetTable,'cpqScsiTargetEntry':cpqScsiTargetEntry,_AW:cpqScsiTargetCntlrIndex,_AX:cpqScsiTargetBusIndex,_AY:cpqScsiTargetScsiIdIndex,'cpqScsiTargetType':cpqScsiTargetType,'cpqScsiTargetModel':cpqScsiTargetModel,'cpqScsiTargetFWRev':cpqScsiTargetFWRev,'cpqScsiTargetVendor':cpqScsiTargetVendor,'cpqScsiTargetParityErrs':cpqScsiTargetParityErrs,'cpqScsiTargetPhaseErrs':cpqScsiTargetPhaseErrs,'cpqScsiTargetSelectTimeouts':cpqScsiTargetSelectTimeouts,'cpqScsiTargetMsgRejects':cpqScsiTargetMsgRejects,'cpqScsiTargetNegPeriod':cpqScsiTargetNegPeriod,'cpqScsiTargetLocation':cpqScsiTargetLocation,'cpqScsiTargetNegSpeed':cpqScsiTargetNegSpeed,'cpqScsiTargetPhysWidth':cpqScsiTargetPhysWidth,'cpqScsiTargetNegWidth':cpqScsiTargetNegWidth,'cpqScsiTargetTypeExtended':cpqScsiTargetTypeExtended,'cpqScsiTargetCurrentSpeed':cpqScsiTargetCurrentSpeed,'cpqScsiCd':cpqScsiCd,'cpqScsiCdDrvTable':cpqScsiCdDrvTable,'cpqScsiCdDrvEntry':cpqScsiCdDrvEntry,_Ab:cpqScsiCdDrvCntlrIndex,_Ac:cpqScsiCdDrvBusIndex,_Ad:cpqScsiCdDrvScsiIdIndex,_Ae:cpqScsiCdDrvLunIndex,'cpqScsiCdDrvModel':cpqScsiCdDrvModel,'cpqScsiCdDrvVendor':cpqScsiCdDrvVendor,'cpqScsiCdDrvFwRev':cpqScsiCdDrvFwRev,'cpqCdLibraryTable':cpqCdLibraryTable,'cpqCdLibraryEntry':cpqCdLibraryEntry,_r:cpqCdLibraryCntlrIndex,_s:cpqCdLibraryBusIndex,_t:cpqCdLibraryScsiIdIndex,_Af:cpqCdLibraryLunIndex,'cpqCdLibraryCondition':cpqCdLibraryCondition,_Ax:cpqCdLibraryStatus,'cpqCdLibraryModel':cpqCdLibraryModel,'cpqCdLibraryVendor':cpqCdLibraryVendor,'cpqCdLibrarySerialNumber':cpqCdLibrarySerialNumber,'cpqCdLibraryDriveList':cpqCdLibraryDriveList,'cpqCdLibraryFwRev':cpqCdLibraryFwRev,'cpqCdLibraryFwSubtype':cpqCdLibraryFwSubtype,'cpqScsiTrap':cpqScsiTrap,'cpqScsiTrapPkts':cpqScsiTrapPkts,'cpqScsiTrapLogMaxSize':cpqScsiTrapLogMaxSize,'cpqScsiTrapLogTable':cpqScsiTrapLogTable,'cpqScsiTrapLogEntry':cpqScsiTrapLogEntry,_Ag:cpqScsiTrapLogIndex,'cpqScsiTrapType':cpqScsiTrapType,'cpqScsiTrapTime':cpqScsiTrapTime,'cpqTapeComponent':cpqTapeComponent,'cpqTapePhyDrv':cpqTapePhyDrv,'cpqTapePhyDrvTable':cpqTapePhyDrvTable,'cpqTapePhyDrvEntry':cpqTapePhyDrvEntry,_Z:cpqTapePhyDrvCntlrIndex,_a:cpqTapePhyDrvBusIndex,_b:cpqTapePhyDrvScsiIdIndex,_u:cpqTapePhyDrvLunIndex,'cpqTapePhyDrvType':cpqTapePhyDrvType,_T:cpqTapePhyDrvCondition,'cpqTapePhyDrvMagSize':cpqTapePhyDrvMagSize,_B2:cpqTapePhyDrvSerialNumber,'cpqTapePhyDrvCleanReq':cpqTapePhyDrvCleanReq,'cpqTapePhyDrvCleanTapeRepl':cpqTapePhyDrvCleanTapeRepl,'cpqTapePhyDrvFwSubtype':cpqTapePhyDrvFwSubtype,_B0:cpqTapePhyDrvName,'cpqTapePhyDrvCleanTapeCount':cpqTapePhyDrvCleanTapeCount,_B1:cpqTapePhyDrvFwRev,_A5:cpqTapePhyDrvStatus,'cpqTapePhyDrvHotPlug':cpqTapePhyDrvHotPlug,'cpqTapePhyDrvPlacement':cpqTapePhyDrvPlacement,'cpqTapePhyDrvLibraryDrive':cpqTapePhyDrvLibraryDrive,'cpqTapePhyDrvLoaderName':cpqTapePhyDrvLoaderName,'cpqTapePhyDrvLoaderFwRev':cpqTapePhyDrvLoaderFwRev,'cpqTapePhyDrvLoaderSerialNum':cpqTapePhyDrvLoaderSerialNum,'cpqTapeCounters':cpqTapeCounters,'cpqTapeCountersTable':cpqTapeCountersTable,'cpqTapeCountersEntry':cpqTapeCountersEntry,_An:cpqTapeCountersCntlrIndex,_Ao:cpqTapeCountersBusIndex,_Ap:cpqTapeCountersScsiIdIndex,_Aq:cpqTapeCountersLunIndex,'cpqTapeCountersReWrites':cpqTapeCountersReWrites,'cpqTapeCountersReReads':cpqTapeCountersReReads,'cpqTapeCountersTotalErrors':cpqTapeCountersTotalErrors,'cpqTapeCountersTotalUncorrectable':cpqTapeCountersTotalUncorrectable,'cpqTapeCountersTotalBytes':cpqTapeCountersTotalBytes,'cpqTapeLibrary':cpqTapeLibrary,'cpqTapeLibraryTable':cpqTapeLibraryTable,'cpqTapeLibraryEntry':cpqTapeLibraryEntry,_x:cpqTapeLibraryCntlrIndex,_y:cpqTapeLibraryBusIndex,_z:cpqTapeLibraryScsiIdIndex,_A0:cpqTapeLibraryLunIndex,'cpqTapeLibraryCondition':cpqTapeLibraryCondition,'cpqTapeLibraryStatus':cpqTapeLibraryStatus,'cpqTapeLibraryDoorStatus':cpqTapeLibraryDoorStatus,'cpqTapeLibraryStatHours':cpqTapeLibraryStatHours,'cpqTapeLibraryStatMoves':cpqTapeLibraryStatMoves,_Ay:cpqTapeLibraryName,_Q:cpqTapeLibrarySerialNumber,'cpqTapeLibraryDriveList':cpqTapeLibraryDriveList,_A_:cpqTapeLibraryState,'cpqTapeLibraryTemperature':cpqTapeLibraryTemperature,'cpqTapeLibraryRedundancy':cpqTapeLibraryRedundancy,'cpqTapeLibraryHotSwap':cpqTapeLibraryHotSwap,_Az:cpqTapeLibraryFwRev,'cpqTapeLibraryTapeList':cpqTapeLibraryTapeList,'cpqSasComponent':cpqSasComponent,'cpqSasHba':cpqSasHba,'cpqSasHbaTable':cpqSasHbaTable,'cpqSasHbaEntry':cpqSasHbaEntry,_As:cpqSasHbaIndex,_U:cpqSasHbaHwLocation,'cpqSasHbaModel':cpqSasHbaModel,'cpqSasHbaStatus':cpqSasHbaStatus,'cpqSasHbaCondition':cpqSasHbaCondition,'cpqSasHbaOverallCondition':cpqSasHbaOverallCondition,'cpqSasHbaSerialNumber':cpqSasHbaSerialNumber,'cpqSasHbaFwVersion':cpqSasHbaFwVersion,'cpqSasHbaBiosVersion':cpqSasHbaBiosVersion,'cpqSasHbaPciLocation':cpqSasHbaPciLocation,'cpqSasPhyDrv':cpqSasPhyDrv,'cpqSasPhyDrvTable':cpqSasPhyDrvTable,'cpqSasPhyDrvEntry':cpqSasPhyDrvEntry,_c:cpqSasPhyDrvHbaIndex,_d:cpqSasPhyDrvIndex,_AA:cpqSasPhyDrvLocationString,_AC:cpqSasPhyDrvModel,_B5:cpqSasPhyDrvStatus,'cpqSasPhyDrvCondition':cpqSasPhyDrvCondition,_AD:cpqSasPhyDrvFWRev,'cpqSasPhyDrvSize':cpqSasPhyDrvSize,'cpqSasPhyDrvUsedReallocs':cpqSasPhyDrvUsedReallocs,_AE:cpqSasPhyDrvSerialNumber,'cpqSasPhyDrvMemberLogDrv':cpqSasPhyDrvMemberLogDrv,'cpqSasPhyDrvRotationalSpeed':cpqSasPhyDrvRotationalSpeed,'cpqSasPhyDrvOsName':cpqSasPhyDrvOsName,'cpqSasPhyDrvPlacement':cpqSasPhyDrvPlacement,'cpqSasPhyDrvHotPlug':cpqSasPhyDrvHotPlug,_AB:cpqSasPhyDrvType,_AF:cpqSasPhyDrvSasAddress,'cpqSasPhyDrvMediaType':cpqSasPhyDrvMediaType,_BE:cpqSasPhyDrvSSDWearStatus,'cpqSasPhyDrvPowerOnHours':cpqSasPhyDrvPowerOnHours,'cpqSasPhyDrvSSDPercntEndrnceUsed':cpqSasPhyDrvSSDPercntEndrnceUsed,'cpqSasPhyDrvSSDEstTimeRemainingHours':cpqSasPhyDrvSSDEstTimeRemainingHours,'cpqSasPhyDrvAuthenticationStatus':cpqSasPhyDrvAuthenticationStatus,'cpqSasPhyDrvSmartCarrierAppFWRev':cpqSasPhyDrvSmartCarrierAppFWRev,'cpqSasPhyDrvSmartCarrierBootldrFWRev':cpqSasPhyDrvSmartCarrierBootldrFWRev,'cpqSasPhyDrvCurrTemperature':cpqSasPhyDrvCurrTemperature,'cpqSasPhyDrvTemperatureThreshold':cpqSasPhyDrvTemperatureThreshold,'cpqSasPhyDrvSsBoxModel':cpqSasPhyDrvSsBoxModel,'cpqSasPhyDrvSsBoxFwRev':cpqSasPhyDrvSsBoxFwRev,'cpqSasPhyDrvSsBoxVendor':cpqSasPhyDrvSsBoxVendor,'cpqSasPhyDrvSsBoxSerialNumber':cpqSasPhyDrvSsBoxSerialNumber,'cpqSasLogDrv':cpqSasLogDrv,'cpqSasLogDrvTable':cpqSasLogDrvTable,'cpqSasLogDrvEntry':cpqSasLogDrvEntry,_A1:cpqSasLogDrvHbaIndex,_A2:cpqSasLogDrvIndex,'cpqSasLogDrvRaidLevel':cpqSasLogDrvRaidLevel,_B6:cpqSasLogDrvStatus,'cpqSasLogDrvCondition':cpqSasLogDrvCondition,'cpqSasLogDrvRebuildingDisk':cpqSasLogDrvRebuildingDisk,'cpqSasLogDrvCapacity':cpqSasLogDrvCapacity,'cpqSasLogDrvStripeSize':cpqSasLogDrvStripeSize,'cpqSasLogDrvPhyDrvIds':cpqSasLogDrvPhyDrvIds,'cpqSasLogDrvSpareIds':cpqSasLogDrvSpareIds,_B7:cpqSasLogDrvOsName,'cpqSasLogDrvRebuildingPercent':cpqSasLogDrvRebuildingPercent,'cpqSasTapeDrv':cpqSasTapeDrv,'cpqSasTapeDrvTable':cpqSasTapeDrvTable,'cpqSasTapeDrvEntry':cpqSasTapeDrvEntry,_A3:cpqSasTapeDrvHbaIndex,_A4:cpqSasTapeDrvIndex,_B8:cpqSasTapeDrvLocationString,_B9:cpqSasTapeDrvName,_BD:cpqSasTapeDrvStatus,'cpqSasTapeDrvCondition':cpqSasTapeDrvCondition,_BA:cpqSasTapeDrvFWRev,_BB:cpqSasTapeDrvSerialNumber,_BC:cpqSasTapeDrvSasAddress,'cpqSbScsiBus':cpqSbScsiBus,'cpqSbScsiMibRev':cpqSbScsiMibRev,'cpqSbMibRevMajor':cpqSbMibRevMajor,'cpqSbMibRevMinor':cpqSbMibRevMinor,'cpqSbDevice':cpqSbDevice,'cpqSbDeviceTable':cpqSbDeviceTable,'cpqSbDeviceEntry':cpqSbDeviceEntry,_Au:cpqSbDevCntlrIndex,_Av:cpqSbDevBusIndex,_Aw:cpqSbDevScsiIdIndex,'cpqSbDevType':cpqSbDevType,'cpqSbDevModel':cpqSbDevModel,'cpqSbDevFWRev':cpqSbDevFWRev,'cpqSbDevVendor':cpqSbDevVendor,'cpqSbDevParityErrs':cpqSbDevParityErrs,'cpqSbDevPhaseErrs':cpqSbDevPhaseErrs,'cpqSbDevSelectTimeouts':cpqSbDevSelectTimeouts,'cpqSbDevMsgRejects':cpqSbDevMsgRejects,'cpqSbDevNegPeriod':cpqSbDevNegPeriod,'cpqSbDevLocation':cpqSbDevLocation})