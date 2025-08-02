_B4='ciscoSonetVTConfMIBGroup'
_B3='ciscoSonetApsMIBGroup1'
_B2='ciscoSonetApsMIBGroup'
_B1='ciscoSonetConfMIBGroup'
_B0='ciscoSonetVTStatusChange'
_A_='ciscoSonetPathStatusChange'
_Az='ciscoSonetLineStatusChange'
_Ay='ciscoSonetSectionStatusChange'
_Ax='csAu4Tug3Payload'
_Aw='cspTributaryGroupingType'
_Av='cspSignallingTransportMode'
_Au='cspTributaryMappingType'
_At='csNotificationsEnabled'
_As='cspSonetPathPayload'
_Ar='csTributaryGroupingType'
_Aq='csSignallingTransportMode'
_Ap='csTributaryFramingType'
_Ao='csTributaryMappingType'
_An='csTributaryType'
_Am='csConfigRDIVType'
_Al='csConfigRDIPType'
_Ak='csApsPrimarySection'
_Aj='csApsSwitchReason'
_Ai='csApsFailureStatus'
_Ah='cspTraceReceived'
_Ag='cspTraceFailure'
_Af='cspTraceToExpect'
_Ae='cspTraceToTransmit'
_Ad='cssTraceReceived'
_Ac='cssTraceFailure'
_Ab='cssTraceToExpect'
_Aa='cssTraceToTransmit'
_AZ='cspFarEndTotalUASs'
_AY='cspFarEndTotalCVs'
_AX='cspFarEndTotalSESs'
_AW='cspFarEndTotalESs'
_AV='cspTotalUASs'
_AU='cspTotalCVs'
_AT='cspTotalSESs'
_AS='cspTotalESs'
_AR='cslFarEndTotalUASs'
_AQ='cslFarEndTotalCVs'
_AP='cslFarEndTotalSESs'
_AO='cslFarEndTotalESs'
_AN='cslTotalUASs'
_AM='cslTotalCVs'
_AL='cslTotalSESs'
_AK='cslTotalESs'
_AJ='cssTotalCVs'
_AI='cssTotalSEFSs'
_AH='cssTotalSESs'
_AG='cssTotalESs'
_AF='cspConfigEntry'
_AE='csVTConfigEntry'
_AD='csAu4Tug3'
_AC='remote failure indications'
_AB='alarm indication signals'
_AA='biDirectional'
_A9='uniDirectional'
_A8='straightOnePlusOneNok1k2'
_A7='ycableOnePlusOneNok1k2'
_A6='anexBOnePlusOne'
_A5='onePlusOne'
_A4='not-accessible'
_A3='csApsWorkingIndex'
_A2='au4Grouping'
_A1='au3Grouping'
_A0='clearMode'
_z='signallingTransferMode'
_y='byteSynchronous'
_x='asynchronous'
_w='vt2vc12'
_v='vt15vc11'
_u='threebit'
_t='onebit'
_s='sonetVTCurrentStatus'
_r='sonetSectionCurrentStatus'
_q='sonetPathCurrentStatus'
_p='sonetLineCurrentStatus'
_o='TruthValue'
_n='ciscoSonetSectionNotifGroup'
_m='ciscoSonetNotifEnableGroup'
_l='ciscoSonetStatsMIBGroup'
_k='csApsChannelProtocol'
_j='csApsArchModeOperational'
_i='csApsDirectionOperational'
_h='csApsLineSwitchReason'
_g='csApsLineFailureCode'
_f='csApsDirection'
_e='csApsWaitToRestore'
_d='csApsSigDegradeBER'
_c='csApsSigFaultBER'
_b='csApsActiveLine'
_a='csApsArchMode'
_Z='csApsEnable'
_Y='csApsProtectionIndex'
_X='csConfigType'
_W='csConfigFrameScramble'
_V='csConfigXmtClockSource'
_U='csConfigLoopbackType'
_T='ciscoSonetConfMIBGroup1'
_S='unavailable seconds'
_R='csApsRevertive'
_Q='Unsigned32'
_P='ciscoSonetTraceMIBGroup'
_O='deprecated'
_N='coding violations'
_M='severely errored seconds'
_L='errored seconds'
_K='notApplicable'
_J='SONET-MIB'
_I='ifDescr'
_H='OctetString'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='CISCO-SONET-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,ifDescr,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndex',_I,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Q,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_o)
sonetLineCurrentStatus,sonetPathCurrentEntry,sonetPathCurrentStatus,sonetSectionCurrentStatus,sonetVTCurrentStatus=mibBuilder.importSymbols(_J,_p,'sonetPathCurrentEntry',_q,_r,_s)
ciscoSonetMIB=ModuleIdentity((1,3,6,1,4,1,9,9,126))
if mibBuilder.loadTexts:ciscoSonetMIB.setRevisions(('2003-03-07 00:00','2002-06-14 00:00','2002-05-22 00:00','2001-10-17 00:00','2000-07-12 00:00','1999-03-08 00:00'))
class CsApsLineFailureCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('csApsChannelMismatch',1),('csApsProtectionByteFail',2),('csApsFEProtectionFailure',3),('csApsModeMismatch',4)))
class CsApsLineFailureStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('noApsLineFailure',0),('csApsChannelMismatchBit',1),('csApsProtectionByteFailBit',2),('csApsFEProtectionFailureBit',3),('csApsModeMismatchBit',4)))
class CsApsLineSwitchReason(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('csApsOther',1),(_R,2),('csApsManual',3),('csApsSignalDefectLow',4),('csApsSignalDefectHigh',5),('csApsSignalFailureLow',6),('csApsSignalFailureHigh',7),('csApsForceSwitch',8),('csApsLockOut',9),('csApsNoSwitch',10)))
_CiscoSonetMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSonetMIBNotifs=_CiscoSonetMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,126,0))
_CiscoSonetMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSonetMIBObjects=_CiscoSonetMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,126,1))
_CsConfig_ObjectIdentity=ObjectIdentity
csConfig=_CsConfig_ObjectIdentity((1,3,6,1,4,1,9,9,126,1,1))
_CsConfigTable_Object=MibTable
csConfigTable=_CsConfigTable_Object((1,3,6,1,4,1,9,9,126,1,1,1))
if mibBuilder.loadTexts:csConfigTable.setStatus(_A)
_CsConfigEntry_Object=MibTableRow
csConfigEntry=_CsConfigEntry_Object((1,3,6,1,4,1,9,9,126,1,1,1,1))
csConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:csConfigEntry.setStatus(_A)
class _CsConfigLoopbackType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noLoopback',1),('lineLocal',2),('lineRemote',3)))
_CsConfigLoopbackType_Type.__name__=_E
_CsConfigLoopbackType_Object=MibTableColumn
csConfigLoopbackType=_CsConfigLoopbackType_Object((1,3,6,1,4,1,9,9,126,1,1,1,1,1),_CsConfigLoopbackType_Type())
csConfigLoopbackType.setMaxAccess(_D)
if mibBuilder.loadTexts:csConfigLoopbackType.setStatus(_A)
class _CsConfigXmtClockSource_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loopTiming',1),('localTiming',2)))
_CsConfigXmtClockSource_Type.__name__=_E
_CsConfigXmtClockSource_Object=MibTableColumn
csConfigXmtClockSource=_CsConfigXmtClockSource_Object((1,3,6,1,4,1,9,9,126,1,1,1,1,2),_CsConfigXmtClockSource_Type())
csConfigXmtClockSource.setMaxAccess(_D)
if mibBuilder.loadTexts:csConfigXmtClockSource.setStatus(_A)
class _CsConfigFrameScramble_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_CsConfigFrameScramble_Type.__name__=_E
_CsConfigFrameScramble_Object=MibTableColumn
csConfigFrameScramble=_CsConfigFrameScramble_Object((1,3,6,1,4,1,9,9,126,1,1,1,1,3),_CsConfigFrameScramble_Type())
csConfigFrameScramble.setMaxAccess(_D)
if mibBuilder.loadTexts:csConfigFrameScramble.setStatus(_A)
class _CsConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('sonetSts3c',1),('sonetStm1',2),('sonetSts12c',3),('sonetStm4',4),('sonetSts48c',5),('sonetStm16',6),('sonetSts192c',7),('sonetStm64',8),('sonetSts3',9)))
_CsConfigType_Type.__name__=_E
_CsConfigType_Object=MibTableColumn
csConfigType=_CsConfigType_Object((1,3,6,1,4,1,9,9,126,1,1,1,1,4),_CsConfigType_Type())
csConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:csConfigType.setStatus(_A)
class _CsConfigRDIVType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_t,1),(_u,3)))
_CsConfigRDIVType_Type.__name__=_E
_CsConfigRDIVType_Object=MibTableColumn
csConfigRDIVType=_CsConfigRDIVType_Object((1,3,6,1,4,1,9,9,126,1,1,1,1,5),_CsConfigRDIVType_Type())
csConfigRDIVType.setMaxAccess(_D)
if mibBuilder.loadTexts:csConfigRDIVType.setStatus(_A)
class _CsConfigRDIPType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_t,1),(_u,3)))
_CsConfigRDIPType_Type.__name__=_E
_CsConfigRDIPType_Object=MibTableColumn
csConfigRDIPType=_CsConfigRDIPType_Object((1,3,6,1,4,1,9,9,126,1,1,1,1,6),_CsConfigRDIPType_Type())
csConfigRDIPType.setMaxAccess(_D)
if mibBuilder.loadTexts:csConfigRDIPType.setStatus(_A)
_CsVTConfigTable_Object=MibTable
csVTConfigTable=_CsVTConfigTable_Object((1,3,6,1,4,1,9,9,126,1,1,2))
if mibBuilder.loadTexts:csVTConfigTable.setStatus(_A)
_CsVTConfigEntry_Object=MibTableRow
csVTConfigEntry=_CsVTConfigEntry_Object((1,3,6,1,4,1,9,9,126,1,1,2,1))
if mibBuilder.loadTexts:csVTConfigEntry.setStatus(_A)
class _CsTributaryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_w,2)))
_CsTributaryType_Type.__name__=_E
_CsTributaryType_Object=MibTableColumn
csTributaryType=_CsTributaryType_Object((1,3,6,1,4,1,9,9,126,1,1,2,1,1),_CsTributaryType_Type())
csTributaryType.setMaxAccess(_D)
if mibBuilder.loadTexts:csTributaryType.setStatus(_A)
class _CsTributaryMappingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_x,1),(_y,2)))
_CsTributaryMappingType_Type.__name__=_E
_CsTributaryMappingType_Object=MibTableColumn
csTributaryMappingType=_CsTributaryMappingType_Object((1,3,6,1,4,1,9,9,126,1,1,2,1,2),_CsTributaryMappingType_Type())
csTributaryMappingType.setMaxAccess(_D)
if mibBuilder.loadTexts:csTributaryMappingType.setStatus(_A)
class _CsTributaryFramingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('dsx1D4',2),('dsx1ESF',3)))
_CsTributaryFramingType_Type.__name__=_E
_CsTributaryFramingType_Object=MibTableColumn
csTributaryFramingType=_CsTributaryFramingType_Object((1,3,6,1,4,1,9,9,126,1,1,2,1,3),_CsTributaryFramingType_Type())
csTributaryFramingType.setMaxAccess(_D)
if mibBuilder.loadTexts:csTributaryFramingType.setStatus(_A)
class _CsSignallingTransportMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_z,2),(_A0,3)))
_CsSignallingTransportMode_Type.__name__=_E
_CsSignallingTransportMode_Object=MibTableColumn
csSignallingTransportMode=_CsSignallingTransportMode_Object((1,3,6,1,4,1,9,9,126,1,1,2,1,4),_CsSignallingTransportMode_Type())
csSignallingTransportMode.setMaxAccess(_D)
if mibBuilder.loadTexts:csSignallingTransportMode.setStatus(_A)
class _CsTributaryGroupingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_A1,2),(_A2,3)))
_CsTributaryGroupingType_Type.__name__=_E
_CsTributaryGroupingType_Object=MibTableColumn
csTributaryGroupingType=_CsTributaryGroupingType_Object((1,3,6,1,4,1,9,9,126,1,1,2,1,5),_CsTributaryGroupingType_Type())
csTributaryGroupingType.setMaxAccess(_D)
if mibBuilder.loadTexts:csTributaryGroupingType.setStatus(_A)
_CsApsConfig_ObjectIdentity=ObjectIdentity
csApsConfig=_CsApsConfig_ObjectIdentity((1,3,6,1,4,1,9,9,126,1,2))
_CsApsConfigTable_Object=MibTable
csApsConfigTable=_CsApsConfigTable_Object((1,3,6,1,4,1,9,9,126,1,2,1))
if mibBuilder.loadTexts:csApsConfigTable.setStatus(_A)
_CsApsConfigEntry_Object=MibTableRow
csApsConfigEntry=_CsApsConfigEntry_Object((1,3,6,1,4,1,9,9,126,1,2,1,1))
csApsConfigEntry.setIndexNames((0,_B,_A3))
if mibBuilder.loadTexts:csApsConfigEntry.setStatus(_A)
_CsApsWorkingIndex_Type=InterfaceIndex
_CsApsWorkingIndex_Object=MibTableColumn
csApsWorkingIndex=_CsApsWorkingIndex_Object((1,3,6,1,4,1,9,9,126,1,2,1,1,1),_CsApsWorkingIndex_Type())
csApsWorkingIndex.setMaxAccess(_A4)
if mibBuilder.loadTexts:csApsWorkingIndex.setStatus(_A)
_CsApsProtectionIndex_Type=InterfaceIndex
_CsApsProtectionIndex_Object=MibTableColumn
csApsProtectionIndex=_CsApsProtectionIndex_Object((1,3,6,1,4,1,9,9,126,1,2,1,1,2),_CsApsProtectionIndex_Type())
csApsProtectionIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:csApsProtectionIndex.setStatus(_A)
class _CsApsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('csApsDisabled',1),('csApsEnabled',2)))
_CsApsEnable_Type.__name__=_E
_CsApsEnable_Object=MibTableColumn
csApsEnable=_CsApsEnable_Object((1,3,6,1,4,1,9,9,126,1,2,1,1,3),_CsApsEnable_Type())
csApsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:csApsEnable.setStatus(_A)
class _CsApsArchMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_A5,1),('oneToOne',2),(_A6,3),(_A7,4),(_A8,5)))
_CsApsArchMode_Type.__name__=_E
_CsApsArchMode_Object=MibTableColumn
csApsArchMode=_CsApsArchMode_Object((1,3,6,1,4,1,9,9,126,1,2,1,1,4),_CsApsArchMode_Type())
csApsArchMode.setMaxAccess(_D)
if mibBuilder.loadTexts:csApsArchMode.setStatus(_A)
class _CsApsActiveLine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('csApsWorkingLine',1),('csApsProtectionLine',2),('csApsNone',3)))
_CsApsActiveLine_Type.__name__=_E
_CsApsActiveLine_Object=MibTableColumn
csApsActiveLine=_CsApsActiveLine_Object((1,3,6,1,4,1,9,9,126,1,2,1,1,5),_CsApsActiveLine_Type())
csApsActiveLine.setMaxAccess(_C)
if mibBuilder.loadTexts:csApsActiveLine.setStatus(_A)
class _CsApsSigFaultBER_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,5))
_CsApsSigFaultBER_Type.__name__=_Q
_CsApsSigFaultBER_Object=MibTableColumn
csApsSigFaultBER=_CsApsSigFaultBER_Object((1,3,6,1,4,1,9,9,126,1,2,1,1,6),_CsApsSigFaultBER_Type())
csApsSigFaultBER.setMaxAccess(_D)
if mibBuilder.loadTexts:csApsSigFaultBER.setStatus(_A)
class _CsApsSigDegradeBER_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,9))
_CsApsSigDegradeBER_Type.__name__=_Q
_CsApsSigDegradeBER_Object=MibTableColumn
csApsSigDegradeBER=_CsApsSigDegradeBER_Object((1,3,6,1,4,1,9,9,126,1,2,1,1,7),_CsApsSigDegradeBER_Type())
csApsSigDegradeBER.setMaxAccess(_D)
if mibBuilder.loadTexts:csApsSigDegradeBER.setStatus(_A)
class _CsApsWaitToRestore_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_CsApsWaitToRestore_Type.__name__=_Q
_CsApsWaitToRestore_Object=MibTableColumn
csApsWaitToRestore=_CsApsWaitToRestore_Object((1,3,6,1,4,1,9,9,126,1,2,1,1,8),_CsApsWaitToRestore_Type())
csApsWaitToRestore.setMaxAccess(_D)
if mibBuilder.loadTexts:csApsWaitToRestore.setStatus(_A)
if mibBuilder.loadTexts:csApsWaitToRestore.setUnits('minutes')
class _CsApsDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A9,1),(_AA,2)))
_CsApsDirection_Type.__name__=_E
_CsApsDirection_Object=MibTableColumn
csApsDirection=_CsApsDirection_Object((1,3,6,1,4,1,9,9,126,1,2,1,1,9),_CsApsDirection_Type())
csApsDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:csApsDirection.setStatus(_A)
class _CsApsRevertive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonrevertive',1),('revertive',2)))
_CsApsRevertive_Type.__name__=_E
_CsApsRevertive_Object=MibTableColumn
csApsRevertive=_CsApsRevertive_Object((1,3,6,1,4,1,9,9,126,1,2,1,1,10),_CsApsRevertive_Type())
csApsRevertive.setMaxAccess(_D)
if mibBuilder.loadTexts:csApsRevertive.setStatus(_A)
class _CsApsDirectionOperational_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A9,1),(_AA,2)))
_CsApsDirectionOperational_Type.__name__=_E
_CsApsDirectionOperational_Object=MibTableColumn
csApsDirectionOperational=_CsApsDirectionOperational_Object((1,3,6,1,4,1,9,9,126,1,2,1,1,11),_CsApsDirectionOperational_Type())
csApsDirectionOperational.setMaxAccess(_C)
if mibBuilder.loadTexts:csApsDirectionOperational.setStatus(_A)
class _CsApsArchModeOperational_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_A5,1),('oneToOne',2),(_A6,3),(_A7,4),(_A8,5)))
_CsApsArchModeOperational_Type.__name__=_E
_CsApsArchModeOperational_Object=MibTableColumn
csApsArchModeOperational=_CsApsArchModeOperational_Object((1,3,6,1,4,1,9,9,126,1,2,1,1,12),_CsApsArchModeOperational_Type())
csApsArchModeOperational.setMaxAccess(_C)
if mibBuilder.loadTexts:csApsArchModeOperational.setStatus(_A)
class _CsApsChannelProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bellcore',1),('itu',2)))
_CsApsChannelProtocol_Type.__name__=_E
_CsApsChannelProtocol_Object=MibTableColumn
csApsChannelProtocol=_CsApsChannelProtocol_Object((1,3,6,1,4,1,9,9,126,1,2,1,1,13),_CsApsChannelProtocol_Type())
csApsChannelProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:csApsChannelProtocol.setStatus(_A)
_CsApsFailureStatus_Type=CsApsLineFailureStatus
_CsApsFailureStatus_Object=MibTableColumn
csApsFailureStatus=_CsApsFailureStatus_Object((1,3,6,1,4,1,9,9,126,1,2,1,1,14),_CsApsFailureStatus_Type())
csApsFailureStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:csApsFailureStatus.setStatus(_A)
_CsApsSwitchReason_Type=CsApsLineSwitchReason
_CsApsSwitchReason_Object=MibTableColumn
csApsSwitchReason=_CsApsSwitchReason_Object((1,3,6,1,4,1,9,9,126,1,2,1,1,15),_CsApsSwitchReason_Type())
csApsSwitchReason.setMaxAccess(_C)
if mibBuilder.loadTexts:csApsSwitchReason.setStatus(_A)
class _CsApsPrimarySection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('workingSection1',1),('workingSection2',2),('none',3)))
_CsApsPrimarySection_Type.__name__=_E
_CsApsPrimarySection_Object=MibTableColumn
csApsPrimarySection=_CsApsPrimarySection_Object((1,3,6,1,4,1,9,9,126,1,2,1,1,16),_CsApsPrimarySection_Type())
csApsPrimarySection.setMaxAccess(_C)
if mibBuilder.loadTexts:csApsPrimarySection.setStatus(_A)
_CsApsLineFailureCode_Type=CsApsLineFailureCode
_CsApsLineFailureCode_Object=MibScalar
csApsLineFailureCode=_CsApsLineFailureCode_Object((1,3,6,1,4,1,9,9,126,1,2,2),_CsApsLineFailureCode_Type())
csApsLineFailureCode.setMaxAccess(_C)
if mibBuilder.loadTexts:csApsLineFailureCode.setStatus(_A)
_CsApsLineSwitchReason_Type=CsApsLineSwitchReason
_CsApsLineSwitchReason_Object=MibScalar
csApsLineSwitchReason=_CsApsLineSwitchReason_Object((1,3,6,1,4,1,9,9,126,1,2,3),_CsApsLineSwitchReason_Type())
csApsLineSwitchReason.setMaxAccess(_C)
if mibBuilder.loadTexts:csApsLineSwitchReason.setStatus(_A)
_CsSection_ObjectIdentity=ObjectIdentity
csSection=_CsSection_ObjectIdentity((1,3,6,1,4,1,9,9,126,1,3))
_CssTotalTable_Object=MibTable
cssTotalTable=_CssTotalTable_Object((1,3,6,1,4,1,9,9,126,1,3,1))
if mibBuilder.loadTexts:cssTotalTable.setStatus(_A)
_CssTotalEntry_Object=MibTableRow
cssTotalEntry=_CssTotalEntry_Object((1,3,6,1,4,1,9,9,126,1,3,1,1))
cssTotalEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cssTotalEntry.setStatus(_A)
_CssTotalESs_Type=Gauge32
_CssTotalESs_Object=MibTableColumn
cssTotalESs=_CssTotalESs_Object((1,3,6,1,4,1,9,9,126,1,3,1,1,1),_CssTotalESs_Type())
cssTotalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cssTotalESs.setStatus(_A)
if mibBuilder.loadTexts:cssTotalESs.setUnits(_L)
_CssTotalSESs_Type=Gauge32
_CssTotalSESs_Object=MibTableColumn
cssTotalSESs=_CssTotalSESs_Object((1,3,6,1,4,1,9,9,126,1,3,1,1,2),_CssTotalSESs_Type())
cssTotalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cssTotalSESs.setStatus(_A)
if mibBuilder.loadTexts:cssTotalSESs.setUnits(_M)
_CssTotalSEFSs_Type=Gauge32
_CssTotalSEFSs_Object=MibTableColumn
cssTotalSEFSs=_CssTotalSEFSs_Object((1,3,6,1,4,1,9,9,126,1,3,1,1,3),_CssTotalSEFSs_Type())
cssTotalSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:cssTotalSEFSs.setStatus(_A)
if mibBuilder.loadTexts:cssTotalSEFSs.setUnits('severely errored framing seconds')
_CssTotalCVs_Type=Gauge32
_CssTotalCVs_Object=MibTableColumn
cssTotalCVs=_CssTotalCVs_Object((1,3,6,1,4,1,9,9,126,1,3,1,1,4),_CssTotalCVs_Type())
cssTotalCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cssTotalCVs.setStatus(_A)
if mibBuilder.loadTexts:cssTotalCVs.setUnits(_N)
_CssTraceTable_Object=MibTable
cssTraceTable=_CssTraceTable_Object((1,3,6,1,4,1,9,9,126,1,3,2))
if mibBuilder.loadTexts:cssTraceTable.setStatus(_A)
_CssTraceEntry_Object=MibTableRow
cssTraceEntry=_CssTraceEntry_Object((1,3,6,1,4,1,9,9,126,1,3,2,1))
cssTraceEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cssTraceEntry.setStatus(_A)
class _CssTraceToTransmit_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16),ValueSizeConstraint(64,64))
_CssTraceToTransmit_Type.__name__=_H
_CssTraceToTransmit_Object=MibTableColumn
cssTraceToTransmit=_CssTraceToTransmit_Object((1,3,6,1,4,1,9,9,126,1,3,2,1,1),_CssTraceToTransmit_Type())
cssTraceToTransmit.setMaxAccess(_D)
if mibBuilder.loadTexts:cssTraceToTransmit.setStatus(_A)
class _CssTraceToExpect_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16),ValueSizeConstraint(64,64))
_CssTraceToExpect_Type.__name__=_H
_CssTraceToExpect_Object=MibTableColumn
cssTraceToExpect=_CssTraceToExpect_Object((1,3,6,1,4,1,9,9,126,1,3,2,1,2),_CssTraceToExpect_Type())
cssTraceToExpect.setMaxAccess(_D)
if mibBuilder.loadTexts:cssTraceToExpect.setStatus(_A)
_CssTraceFailure_Type=TruthValue
_CssTraceFailure_Object=MibTableColumn
cssTraceFailure=_CssTraceFailure_Object((1,3,6,1,4,1,9,9,126,1,3,2,1,3),_CssTraceFailure_Type())
cssTraceFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:cssTraceFailure.setStatus(_A)
class _CssTraceReceived_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16),ValueSizeConstraint(64,64))
_CssTraceReceived_Type.__name__=_H
_CssTraceReceived_Object=MibTableColumn
cssTraceReceived=_CssTraceReceived_Object((1,3,6,1,4,1,9,9,126,1,3,2,1,4),_CssTraceReceived_Type())
cssTraceReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:cssTraceReceived.setStatus(_A)
_CsLine_ObjectIdentity=ObjectIdentity
csLine=_CsLine_ObjectIdentity((1,3,6,1,4,1,9,9,126,1,4))
_CslTotalTable_Object=MibTable
cslTotalTable=_CslTotalTable_Object((1,3,6,1,4,1,9,9,126,1,4,1))
if mibBuilder.loadTexts:cslTotalTable.setStatus(_A)
_CslTotalEntry_Object=MibTableRow
cslTotalEntry=_CslTotalEntry_Object((1,3,6,1,4,1,9,9,126,1,4,1,1))
cslTotalEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cslTotalEntry.setStatus(_A)
_CslTotalESs_Type=Gauge32
_CslTotalESs_Object=MibTableColumn
cslTotalESs=_CslTotalESs_Object((1,3,6,1,4,1,9,9,126,1,4,1,1,1),_CslTotalESs_Type())
cslTotalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cslTotalESs.setStatus(_A)
if mibBuilder.loadTexts:cslTotalESs.setUnits(_L)
_CslTotalSESs_Type=Gauge32
_CslTotalSESs_Object=MibTableColumn
cslTotalSESs=_CslTotalSESs_Object((1,3,6,1,4,1,9,9,126,1,4,1,1,2),_CslTotalSESs_Type())
cslTotalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cslTotalSESs.setStatus(_A)
if mibBuilder.loadTexts:cslTotalSESs.setUnits(_M)
_CslTotalCVs_Type=Gauge32
_CslTotalCVs_Object=MibTableColumn
cslTotalCVs=_CslTotalCVs_Object((1,3,6,1,4,1,9,9,126,1,4,1,1,3),_CslTotalCVs_Type())
cslTotalCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cslTotalCVs.setStatus(_A)
if mibBuilder.loadTexts:cslTotalCVs.setUnits(_N)
_CslTotalUASs_Type=Gauge32
_CslTotalUASs_Object=MibTableColumn
cslTotalUASs=_CslTotalUASs_Object((1,3,6,1,4,1,9,9,126,1,4,1,1,4),_CslTotalUASs_Type())
cslTotalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cslTotalUASs.setStatus(_A)
if mibBuilder.loadTexts:cslTotalUASs.setUnits(_S)
_CslFarEndTotalTable_Object=MibTable
cslFarEndTotalTable=_CslFarEndTotalTable_Object((1,3,6,1,4,1,9,9,126,1,4,2))
if mibBuilder.loadTexts:cslFarEndTotalTable.setStatus(_A)
_CslFarEndTotalEntry_Object=MibTableRow
cslFarEndTotalEntry=_CslFarEndTotalEntry_Object((1,3,6,1,4,1,9,9,126,1,4,2,1))
cslFarEndTotalEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cslFarEndTotalEntry.setStatus(_A)
_CslFarEndTotalESs_Type=Gauge32
_CslFarEndTotalESs_Object=MibTableColumn
cslFarEndTotalESs=_CslFarEndTotalESs_Object((1,3,6,1,4,1,9,9,126,1,4,2,1,1),_CslFarEndTotalESs_Type())
cslFarEndTotalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cslFarEndTotalESs.setStatus(_A)
if mibBuilder.loadTexts:cslFarEndTotalESs.setUnits(_L)
_CslFarEndTotalSESs_Type=Gauge32
_CslFarEndTotalSESs_Object=MibTableColumn
cslFarEndTotalSESs=_CslFarEndTotalSESs_Object((1,3,6,1,4,1,9,9,126,1,4,2,1,2),_CslFarEndTotalSESs_Type())
cslFarEndTotalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cslFarEndTotalSESs.setStatus(_A)
if mibBuilder.loadTexts:cslFarEndTotalSESs.setUnits(_M)
_CslFarEndTotalCVs_Type=Gauge32
_CslFarEndTotalCVs_Object=MibTableColumn
cslFarEndTotalCVs=_CslFarEndTotalCVs_Object((1,3,6,1,4,1,9,9,126,1,4,2,1,3),_CslFarEndTotalCVs_Type())
cslFarEndTotalCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cslFarEndTotalCVs.setStatus(_A)
if mibBuilder.loadTexts:cslFarEndTotalCVs.setUnits(_N)
_CslFarEndTotalUASs_Type=Gauge32
_CslFarEndTotalUASs_Object=MibTableColumn
cslFarEndTotalUASs=_CslFarEndTotalUASs_Object((1,3,6,1,4,1,9,9,126,1,4,2,1,4),_CslFarEndTotalUASs_Type())
cslFarEndTotalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cslFarEndTotalUASs.setStatus(_A)
if mibBuilder.loadTexts:cslFarEndTotalUASs.setUnits(_S)
_CsPath_ObjectIdentity=ObjectIdentity
csPath=_CsPath_ObjectIdentity((1,3,6,1,4,1,9,9,126,1,5))
_CspTotalTable_Object=MibTable
cspTotalTable=_CspTotalTable_Object((1,3,6,1,4,1,9,9,126,1,5,1))
if mibBuilder.loadTexts:cspTotalTable.setStatus(_A)
_CspTotalEntry_Object=MibTableRow
cspTotalEntry=_CspTotalEntry_Object((1,3,6,1,4,1,9,9,126,1,5,1,1))
cspTotalEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cspTotalEntry.setStatus(_A)
_CspTotalESs_Type=Gauge32
_CspTotalESs_Object=MibTableColumn
cspTotalESs=_CspTotalESs_Object((1,3,6,1,4,1,9,9,126,1,5,1,1,1),_CspTotalESs_Type())
cspTotalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cspTotalESs.setStatus(_A)
if mibBuilder.loadTexts:cspTotalESs.setUnits(_L)
_CspTotalSESs_Type=Gauge32
_CspTotalSESs_Object=MibTableColumn
cspTotalSESs=_CspTotalSESs_Object((1,3,6,1,4,1,9,9,126,1,5,1,1,2),_CspTotalSESs_Type())
cspTotalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cspTotalSESs.setStatus(_A)
if mibBuilder.loadTexts:cspTotalSESs.setUnits(_M)
_CspTotalCVs_Type=Gauge32
_CspTotalCVs_Object=MibTableColumn
cspTotalCVs=_CspTotalCVs_Object((1,3,6,1,4,1,9,9,126,1,5,1,1,3),_CspTotalCVs_Type())
cspTotalCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cspTotalCVs.setStatus(_A)
if mibBuilder.loadTexts:cspTotalCVs.setUnits(_N)
_CspTotalUASs_Type=Gauge32
_CspTotalUASs_Object=MibTableColumn
cspTotalUASs=_CspTotalUASs_Object((1,3,6,1,4,1,9,9,126,1,5,1,1,4),_CspTotalUASs_Type())
cspTotalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cspTotalUASs.setStatus(_A)
if mibBuilder.loadTexts:cspTotalUASs.setUnits(_S)
_CspFarEndTotalTable_Object=MibTable
cspFarEndTotalTable=_CspFarEndTotalTable_Object((1,3,6,1,4,1,9,9,126,1,5,2))
if mibBuilder.loadTexts:cspFarEndTotalTable.setStatus(_A)
_CspFarEndTotalEntry_Object=MibTableRow
cspFarEndTotalEntry=_CspFarEndTotalEntry_Object((1,3,6,1,4,1,9,9,126,1,5,2,1))
cspFarEndTotalEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cspFarEndTotalEntry.setStatus(_A)
_CspFarEndTotalESs_Type=Gauge32
_CspFarEndTotalESs_Object=MibTableColumn
cspFarEndTotalESs=_CspFarEndTotalESs_Object((1,3,6,1,4,1,9,9,126,1,5,2,1,1),_CspFarEndTotalESs_Type())
cspFarEndTotalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cspFarEndTotalESs.setStatus(_A)
if mibBuilder.loadTexts:cspFarEndTotalESs.setUnits(_L)
_CspFarEndTotalSESs_Type=Gauge32
_CspFarEndTotalSESs_Object=MibTableColumn
cspFarEndTotalSESs=_CspFarEndTotalSESs_Object((1,3,6,1,4,1,9,9,126,1,5,2,1,2),_CspFarEndTotalSESs_Type())
cspFarEndTotalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cspFarEndTotalSESs.setStatus(_A)
if mibBuilder.loadTexts:cspFarEndTotalSESs.setUnits(_M)
_CspFarEndTotalCVs_Type=Gauge32
_CspFarEndTotalCVs_Object=MibTableColumn
cspFarEndTotalCVs=_CspFarEndTotalCVs_Object((1,3,6,1,4,1,9,9,126,1,5,2,1,3),_CspFarEndTotalCVs_Type())
cspFarEndTotalCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cspFarEndTotalCVs.setStatus(_A)
if mibBuilder.loadTexts:cspFarEndTotalCVs.setUnits(_N)
_CspFarEndTotalUASs_Type=Gauge32
_CspFarEndTotalUASs_Object=MibTableColumn
cspFarEndTotalUASs=_CspFarEndTotalUASs_Object((1,3,6,1,4,1,9,9,126,1,5,2,1,4),_CspFarEndTotalUASs_Type())
cspFarEndTotalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cspFarEndTotalUASs.setStatus(_A)
if mibBuilder.loadTexts:cspFarEndTotalUASs.setUnits(_S)
_CspTraceTable_Object=MibTable
cspTraceTable=_CspTraceTable_Object((1,3,6,1,4,1,9,9,126,1,5,3))
if mibBuilder.loadTexts:cspTraceTable.setStatus(_A)
_CspTraceEntry_Object=MibTableRow
cspTraceEntry=_CspTraceEntry_Object((1,3,6,1,4,1,9,9,126,1,5,3,1))
cspTraceEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cspTraceEntry.setStatus(_A)
class _CspTraceToTransmit_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16),ValueSizeConstraint(64,64))
_CspTraceToTransmit_Type.__name__=_H
_CspTraceToTransmit_Object=MibTableColumn
cspTraceToTransmit=_CspTraceToTransmit_Object((1,3,6,1,4,1,9,9,126,1,5,3,1,1),_CspTraceToTransmit_Type())
cspTraceToTransmit.setMaxAccess(_D)
if mibBuilder.loadTexts:cspTraceToTransmit.setStatus(_A)
class _CspTraceToExpect_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16),ValueSizeConstraint(64,64))
_CspTraceToExpect_Type.__name__=_H
_CspTraceToExpect_Object=MibTableColumn
cspTraceToExpect=_CspTraceToExpect_Object((1,3,6,1,4,1,9,9,126,1,5,3,1,2),_CspTraceToExpect_Type())
cspTraceToExpect.setMaxAccess(_D)
if mibBuilder.loadTexts:cspTraceToExpect.setStatus(_A)
_CspTraceFailure_Type=TruthValue
_CspTraceFailure_Object=MibTableColumn
cspTraceFailure=_CspTraceFailure_Object((1,3,6,1,4,1,9,9,126,1,5,3,1,3),_CspTraceFailure_Type())
cspTraceFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:cspTraceFailure.setStatus(_A)
class _CspTraceReceived_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16),ValueSizeConstraint(64,64))
_CspTraceReceived_Type.__name__=_H
_CspTraceReceived_Object=MibTableColumn
cspTraceReceived=_CspTraceReceived_Object((1,3,6,1,4,1,9,9,126,1,5,3,1,4),_CspTraceReceived_Type())
cspTraceReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:cspTraceReceived.setStatus(_A)
_CsStats_ObjectIdentity=ObjectIdentity
csStats=_CsStats_ObjectIdentity((1,3,6,1,4,1,9,9,126,1,6))
_CsStatsTable_Object=MibTable
csStatsTable=_CsStatsTable_Object((1,3,6,1,4,1,9,9,126,1,6,1))
if mibBuilder.loadTexts:csStatsTable.setStatus(_A)
_CsStatsEntry_Object=MibTableRow
csStatsEntry=_CsStatsEntry_Object((1,3,6,1,4,1,9,9,126,1,6,1,1))
csStatsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:csStatsEntry.setStatus(_A)
_CssLOSs_Type=Counter32
_CssLOSs_Object=MibTableColumn
cssLOSs=_CssLOSs_Object((1,3,6,1,4,1,9,9,126,1,6,1,1,1),_CssLOSs_Type())
cssLOSs.setMaxAccess(_C)
if mibBuilder.loadTexts:cssLOSs.setStatus(_A)
if mibBuilder.loadTexts:cssLOSs.setUnits('loss of signals')
_CssLOFs_Type=Counter32
_CssLOFs_Object=MibTableColumn
cssLOFs=_CssLOFs_Object((1,3,6,1,4,1,9,9,126,1,6,1,1,2),_CssLOFs_Type())
cssLOFs.setMaxAccess(_C)
if mibBuilder.loadTexts:cssLOFs.setStatus(_A)
if mibBuilder.loadTexts:cssLOFs.setUnits('loss of frames')
_CslAISs_Type=Counter32
_CslAISs_Object=MibTableColumn
cslAISs=_CslAISs_Object((1,3,6,1,4,1,9,9,126,1,6,1,1,3),_CslAISs_Type())
cslAISs.setMaxAccess(_C)
if mibBuilder.loadTexts:cslAISs.setStatus(_A)
if mibBuilder.loadTexts:cslAISs.setUnits(_AB)
_CslRFIs_Type=Counter32
_CslRFIs_Object=MibTableColumn
cslRFIs=_CslRFIs_Object((1,3,6,1,4,1,9,9,126,1,6,1,1,4),_CslRFIs_Type())
cslRFIs.setMaxAccess(_C)
if mibBuilder.loadTexts:cslRFIs.setStatus(_A)
if mibBuilder.loadTexts:cslRFIs.setUnits(_AC)
_CspAISs_Type=Counter32
_CspAISs_Object=MibTableColumn
cspAISs=_CspAISs_Object((1,3,6,1,4,1,9,9,126,1,6,1,1,5),_CspAISs_Type())
cspAISs.setMaxAccess(_C)
if mibBuilder.loadTexts:cspAISs.setStatus(_A)
if mibBuilder.loadTexts:cspAISs.setUnits(_AB)
_CspRFIs_Type=Counter32
_CspRFIs_Object=MibTableColumn
cspRFIs=_CspRFIs_Object((1,3,6,1,4,1,9,9,126,1,6,1,1,6),_CspRFIs_Type())
cspRFIs.setMaxAccess(_C)
if mibBuilder.loadTexts:cspRFIs.setStatus(_A)
if mibBuilder.loadTexts:cspRFIs.setUnits(_AC)
_CspConfig_ObjectIdentity=ObjectIdentity
cspConfig=_CspConfig_ObjectIdentity((1,3,6,1,4,1,9,9,126,1,7))
_CspConfigTable_Object=MibTable
cspConfigTable=_CspConfigTable_Object((1,3,6,1,4,1,9,9,126,1,7,1))
if mibBuilder.loadTexts:cspConfigTable.setStatus(_A)
_CspConfigEntry_Object=MibTableRow
cspConfigEntry=_CspConfigEntry_Object((1,3,6,1,4,1,9,9,126,1,7,1,1))
if mibBuilder.loadTexts:cspConfigEntry.setStatus(_A)
class _CspSonetPathPayload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('unequipped',1),('unspecified',2),('ds3',3),(_v,4),(_w,5),('atmCell',6),('hdlcFr',7),('e3',8),('vtStructured',9)))
_CspSonetPathPayload_Type.__name__=_E
_CspSonetPathPayload_Object=MibTableColumn
cspSonetPathPayload=_CspSonetPathPayload_Object((1,3,6,1,4,1,9,9,126,1,7,1,1,1),_CspSonetPathPayload_Type())
cspSonetPathPayload.setMaxAccess(_D)
if mibBuilder.loadTexts:cspSonetPathPayload.setStatus(_A)
class _CspTributaryMappingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_x,1),(_y,2)))
_CspTributaryMappingType_Type.__name__=_E
_CspTributaryMappingType_Object=MibTableColumn
cspTributaryMappingType=_CspTributaryMappingType_Object((1,3,6,1,4,1,9,9,126,1,7,1,1,2),_CspTributaryMappingType_Type())
cspTributaryMappingType.setMaxAccess(_D)
if mibBuilder.loadTexts:cspTributaryMappingType.setStatus(_A)
class _CspSignallingTransportMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_z,2),(_A0,3)))
_CspSignallingTransportMode_Type.__name__=_E
_CspSignallingTransportMode_Object=MibTableColumn
cspSignallingTransportMode=_CspSignallingTransportMode_Object((1,3,6,1,4,1,9,9,126,1,7,1,1,3),_CspSignallingTransportMode_Type())
cspSignallingTransportMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cspSignallingTransportMode.setStatus(_A)
class _CspTributaryGroupingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_A1,2),(_A2,3)))
_CspTributaryGroupingType_Type.__name__=_E
_CspTributaryGroupingType_Object=MibTableColumn
cspTributaryGroupingType=_CspTributaryGroupingType_Object((1,3,6,1,4,1,9,9,126,1,7,1,1,4),_CspTributaryGroupingType_Type())
cspTributaryGroupingType.setMaxAccess(_D)
if mibBuilder.loadTexts:cspTributaryGroupingType.setStatus(_A)
_CsNotifications_ObjectIdentity=ObjectIdentity
csNotifications=_CsNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,126,1,8))
class _CsNotificationsEnabled_Type(TruthValue):defaultValue=2
_CsNotificationsEnabled_Type.__name__=_o
_CsNotificationsEnabled_Object=MibScalar
csNotificationsEnabled=_CsNotificationsEnabled_Object((1,3,6,1,4,1,9,9,126,1,8,1),_CsNotificationsEnabled_Type())
csNotificationsEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:csNotificationsEnabled.setStatus(_A)
_CsAu4Tug3Config_ObjectIdentity=ObjectIdentity
csAu4Tug3Config=_CsAu4Tug3Config_ObjectIdentity((1,3,6,1,4,1,9,9,126,1,9))
_CsAu4Tug3ConfigTable_Object=MibTable
csAu4Tug3ConfigTable=_CsAu4Tug3ConfigTable_Object((1,3,6,1,4,1,9,9,126,1,9,1))
if mibBuilder.loadTexts:csAu4Tug3ConfigTable.setStatus(_A)
_CsAu4Tug3ConfigEntry_Object=MibTableRow
csAu4Tug3ConfigEntry=_CsAu4Tug3ConfigEntry_Object((1,3,6,1,4,1,9,9,126,1,9,1,1))
csAu4Tug3ConfigEntry.setIndexNames((0,_F,_G),(0,_B,_AD))
if mibBuilder.loadTexts:csAu4Tug3ConfigEntry.setStatus(_A)
class _CsAu4Tug3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_CsAu4Tug3_Type.__name__=_E
_CsAu4Tug3_Object=MibTableColumn
csAu4Tug3=_CsAu4Tug3_Object((1,3,6,1,4,1,9,9,126,1,9,1,1,1),_CsAu4Tug3_Type())
csAu4Tug3.setMaxAccess(_A4)
if mibBuilder.loadTexts:csAu4Tug3.setStatus(_A)
class _CsAu4Tug3Payload_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('vc11',2),('vc12',3),('tu3ds3',4),('tu3e3',5)))
_CsAu4Tug3Payload_Type.__name__=_E
_CsAu4Tug3Payload_Object=MibTableColumn
csAu4Tug3Payload=_CsAu4Tug3Payload_Object((1,3,6,1,4,1,9,9,126,1,9,1,1,2),_CsAu4Tug3Payload_Type())
csAu4Tug3Payload.setMaxAccess(_D)
if mibBuilder.loadTexts:csAu4Tug3Payload.setStatus(_A)
_CiscoSonetMIBConformance_ObjectIdentity=ObjectIdentity
ciscoSonetMIBConformance=_CiscoSonetMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,126,3))
_CiscoSonetMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSonetMIBCompliances=_CiscoSonetMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,126,3,1))
_CiscoSonetMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSonetMIBGroups=_CiscoSonetMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,126,3,2))
csConfigEntry.registerAugmentions((_B,_AE))
csVTConfigEntry.setIndexNames(*csConfigEntry.getIndexNames())
sonetPathCurrentEntry.registerAugmentions((_B,_AF))
cspConfigEntry.setIndexNames(*sonetPathCurrentEntry.getIndexNames())
ciscoSonetConfMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,126,3,2,1))
ciscoSonetConfMIBGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciscoSonetConfMIBGroup.setStatus(_O)
ciscoSonetStatsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,126,3,2,2))
ciscoSonetStatsMIBGroup.setObjects(*((_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,'cssLOSs'),(_B,'cssLOFs'),(_B,'cslAISs'),(_B,'cslRFIs'),(_B,'cspAISs'),(_B,'cspRFIs'),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:ciscoSonetStatsMIBGroup.setStatus(_A)
ciscoSonetTraceMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,126,3,2,3))
ciscoSonetTraceMIBGroup.setObjects(*((_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah)))
if mibBuilder.loadTexts:ciscoSonetTraceMIBGroup.setStatus(_A)
ciscoSonetApsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,126,3,2,4))
ciscoSonetApsMIBGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_R),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ciscoSonetApsMIBGroup.setStatus(_O)
ciscoSonetApsMIBGroup1=ObjectGroup((1,3,6,1,4,1,9,9,126,3,2,5))
ciscoSonetApsMIBGroup1.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_R),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_Ai),(_B,_Aj),(_B,_Ak)))
if mibBuilder.loadTexts:ciscoSonetApsMIBGroup1.setStatus(_A)
ciscoSonetConfMIBGroup1=ObjectGroup((1,3,6,1,4,1,9,9,126,3,2,6))
ciscoSonetConfMIBGroup1.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Al),(_B,_Am)))
if mibBuilder.loadTexts:ciscoSonetConfMIBGroup1.setStatus(_A)
ciscoSonetVTConfMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,126,3,2,7))
ciscoSonetVTConfMIBGroup.setObjects(*((_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar)))
if mibBuilder.loadTexts:ciscoSonetVTConfMIBGroup.setStatus(_A)
ciscoSonetPathConfMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,126,3,2,8))
ciscoSonetPathConfMIBGroup.setObjects((_B,_As))
if mibBuilder.loadTexts:ciscoSonetPathConfMIBGroup.setStatus(_A)
ciscoSonetNotifEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,126,3,2,9))
ciscoSonetNotifEnableGroup.setObjects((_B,_At))
if mibBuilder.loadTexts:ciscoSonetNotifEnableGroup.setStatus(_A)
ciscoSonetPathConfMIBGroup1=ObjectGroup((1,3,6,1,4,1,9,9,126,3,2,14))
ciscoSonetPathConfMIBGroup1.setObjects(*((_B,_Au),(_B,_Av),(_B,_Aw)))
if mibBuilder.loadTexts:ciscoSonetPathConfMIBGroup1.setStatus(_A)
ciscoSonetAu4Tug3Group=ObjectGroup((1,3,6,1,4,1,9,9,126,3,2,15))
ciscoSonetAu4Tug3Group.setObjects((_B,_Ax))
if mibBuilder.loadTexts:ciscoSonetAu4Tug3Group.setStatus(_A)
ciscoSonetSectionStatusChange=NotificationType((1,3,6,1,4,1,9,9,126,0,1))
ciscoSonetSectionStatusChange.setObjects(*((_J,_r),(_F,_I)))
if mibBuilder.loadTexts:ciscoSonetSectionStatusChange.setStatus(_A)
ciscoSonetLineStatusChange=NotificationType((1,3,6,1,4,1,9,9,126,0,2))
ciscoSonetLineStatusChange.setObjects(*((_J,_p),(_F,_I)))
if mibBuilder.loadTexts:ciscoSonetLineStatusChange.setStatus(_A)
ciscoSonetPathStatusChange=NotificationType((1,3,6,1,4,1,9,9,126,0,3))
ciscoSonetPathStatusChange.setObjects(*((_J,_q),(_F,_I)))
if mibBuilder.loadTexts:ciscoSonetPathStatusChange.setStatus(_A)
ciscoSonetVTStatusChange=NotificationType((1,3,6,1,4,1,9,9,126,0,4))
ciscoSonetVTStatusChange.setObjects(*((_J,_s),(_F,_I)))
if mibBuilder.loadTexts:ciscoSonetVTStatusChange.setStatus(_A)
ciscoSonetSectionNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,126,3,2,10))
ciscoSonetSectionNotifGroup.setObjects((_B,_Ay))
if mibBuilder.loadTexts:ciscoSonetSectionNotifGroup.setStatus(_A)
ciscoSonetLineNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,126,3,2,11))
ciscoSonetLineNotifGroup.setObjects((_B,_Az))
if mibBuilder.loadTexts:ciscoSonetLineNotifGroup.setStatus(_A)
ciscoSonetPathNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,126,3,2,12))
ciscoSonetPathNotifGroup.setObjects((_B,_A_))
if mibBuilder.loadTexts:ciscoSonetPathNotifGroup.setStatus(_A)
ciscoSonetVTNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,126,3,2,13))
ciscoSonetVTNotifGroup.setObjects((_B,_B0))
if mibBuilder.loadTexts:ciscoSonetVTNotifGroup.setStatus(_A)
ciscoSonetMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,126,3,1,1))
ciscoSonetMIBCompliance.setObjects(*((_B,_B1),(_B,_l),(_B,_P),(_B,_B2)))
if mibBuilder.loadTexts:ciscoSonetMIBCompliance.setStatus(_O)
ciscoSonetMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,126,3,1,2))
ciscoSonetMIBCompliance1.setObjects(*((_B,_T),(_B,_l),(_B,_P),(_B,_B3),(_B,_B4)))
if mibBuilder.loadTexts:ciscoSonetMIBCompliance1.setStatus(_O)
ciscoSonetMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,126,3,1,3))
ciscoSonetMIBCompliance2.setObjects(*((_B,_T),(_B,_P),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:ciscoSonetMIBCompliance2.setStatus(_O)
ciscoSonetMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,126,3,1,4))
ciscoSonetMIBCompliance3.setObjects(*((_B,_T),(_B,_P),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:ciscoSonetMIBCompliance3.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CsApsLineFailureCode':CsApsLineFailureCode,'CsApsLineFailureStatus':CsApsLineFailureStatus,'CsApsLineSwitchReason':CsApsLineSwitchReason,'ciscoSonetMIB':ciscoSonetMIB,'ciscoSonetMIBNotifs':ciscoSonetMIBNotifs,_Ay:ciscoSonetSectionStatusChange,_Az:ciscoSonetLineStatusChange,_A_:ciscoSonetPathStatusChange,_B0:ciscoSonetVTStatusChange,'ciscoSonetMIBObjects':ciscoSonetMIBObjects,'csConfig':csConfig,'csConfigTable':csConfigTable,'csConfigEntry':csConfigEntry,_U:csConfigLoopbackType,_V:csConfigXmtClockSource,_W:csConfigFrameScramble,_X:csConfigType,_Am:csConfigRDIVType,_Al:csConfigRDIPType,'csVTConfigTable':csVTConfigTable,_AE:csVTConfigEntry,_An:csTributaryType,_Ao:csTributaryMappingType,_Ap:csTributaryFramingType,_Aq:csSignallingTransportMode,_Ar:csTributaryGroupingType,'csApsConfig':csApsConfig,'csApsConfigTable':csApsConfigTable,'csApsConfigEntry':csApsConfigEntry,_A3:csApsWorkingIndex,_Y:csApsProtectionIndex,_Z:csApsEnable,_a:csApsArchMode,_b:csApsActiveLine,_c:csApsSigFaultBER,_d:csApsSigDegradeBER,_e:csApsWaitToRestore,_f:csApsDirection,_R:csApsRevertive,_i:csApsDirectionOperational,_j:csApsArchModeOperational,_k:csApsChannelProtocol,_Ai:csApsFailureStatus,_Aj:csApsSwitchReason,_Ak:csApsPrimarySection,_g:csApsLineFailureCode,_h:csApsLineSwitchReason,'csSection':csSection,'cssTotalTable':cssTotalTable,'cssTotalEntry':cssTotalEntry,_AG:cssTotalESs,_AH:cssTotalSESs,_AI:cssTotalSEFSs,_AJ:cssTotalCVs,'cssTraceTable':cssTraceTable,'cssTraceEntry':cssTraceEntry,_Aa:cssTraceToTransmit,_Ab:cssTraceToExpect,_Ac:cssTraceFailure,_Ad:cssTraceReceived,'csLine':csLine,'cslTotalTable':cslTotalTable,'cslTotalEntry':cslTotalEntry,_AK:cslTotalESs,_AL:cslTotalSESs,_AM:cslTotalCVs,_AN:cslTotalUASs,'cslFarEndTotalTable':cslFarEndTotalTable,'cslFarEndTotalEntry':cslFarEndTotalEntry,_AO:cslFarEndTotalESs,_AP:cslFarEndTotalSESs,_AQ:cslFarEndTotalCVs,_AR:cslFarEndTotalUASs,'csPath':csPath,'cspTotalTable':cspTotalTable,'cspTotalEntry':cspTotalEntry,_AS:cspTotalESs,_AT:cspTotalSESs,_AU:cspTotalCVs,_AV:cspTotalUASs,'cspFarEndTotalTable':cspFarEndTotalTable,'cspFarEndTotalEntry':cspFarEndTotalEntry,_AW:cspFarEndTotalESs,_AX:cspFarEndTotalSESs,_AY:cspFarEndTotalCVs,_AZ:cspFarEndTotalUASs,'cspTraceTable':cspTraceTable,'cspTraceEntry':cspTraceEntry,_Ae:cspTraceToTransmit,_Af:cspTraceToExpect,_Ag:cspTraceFailure,_Ah:cspTraceReceived,'csStats':csStats,'csStatsTable':csStatsTable,'csStatsEntry':csStatsEntry,'cssLOSs':cssLOSs,'cssLOFs':cssLOFs,'cslAISs':cslAISs,'cslRFIs':cslRFIs,'cspAISs':cspAISs,'cspRFIs':cspRFIs,'cspConfig':cspConfig,'cspConfigTable':cspConfigTable,_AF:cspConfigEntry,_As:cspSonetPathPayload,_Au:cspTributaryMappingType,_Av:cspSignallingTransportMode,_Aw:cspTributaryGroupingType,'csNotifications':csNotifications,_At:csNotificationsEnabled,'csAu4Tug3Config':csAu4Tug3Config,'csAu4Tug3ConfigTable':csAu4Tug3ConfigTable,'csAu4Tug3ConfigEntry':csAu4Tug3ConfigEntry,_AD:csAu4Tug3,_Ax:csAu4Tug3Payload,'ciscoSonetMIBConformance':ciscoSonetMIBConformance,'ciscoSonetMIBCompliances':ciscoSonetMIBCompliances,'ciscoSonetMIBCompliance':ciscoSonetMIBCompliance,'ciscoSonetMIBCompliance1':ciscoSonetMIBCompliance1,'ciscoSonetMIBCompliance2':ciscoSonetMIBCompliance2,'ciscoSonetMIBCompliance3':ciscoSonetMIBCompliance3,'ciscoSonetMIBGroups':ciscoSonetMIBGroups,_B1:ciscoSonetConfMIBGroup,_l:ciscoSonetStatsMIBGroup,_P:ciscoSonetTraceMIBGroup,_B2:ciscoSonetApsMIBGroup,_B3:ciscoSonetApsMIBGroup1,_T:ciscoSonetConfMIBGroup1,_B4:ciscoSonetVTConfMIBGroup,'ciscoSonetPathConfMIBGroup':ciscoSonetPathConfMIBGroup,_m:ciscoSonetNotifEnableGroup,_n:ciscoSonetSectionNotifGroup,'ciscoSonetLineNotifGroup':ciscoSonetLineNotifGroup,'ciscoSonetPathNotifGroup':ciscoSonetPathNotifGroup,'ciscoSonetVTNotifGroup':ciscoSonetVTNotifGroup,'ciscoSonetPathConfMIBGroup1':ciscoSonetPathConfMIBGroup1,'ciscoSonetAu4Tug3Group':ciscoSonetAu4Tug3Group})