_AT='osCountersOptGroup'
_AS='osCountersMandatoryGroup'
_AR='osCntVBindLastError'
_AQ='osCntVBindIsActive'
_AP='osCntBindLastError'
_AO='osCntBindCountersRange'
_AN='osCntBindCountersMode'
_AM='osCntAclMatchPkts'
_AL='osCntAclMatchOcts'
_AK='osCntAclEntryStatus'
_AJ='osCntEgrSuiteTxqDropPkts'
_AI='osCntEgrSuiteBcPassPkts'
_AH='osCntEgrSuiteMcPassPkts'
_AG='osCntEgrSuiteUcPassPkts'
_AF='osCntEgrSuiteEntryStatus'
_AE='osCntEgrSuiteIsIntPort'
_AD='osCntEgrSuiteIsSkip'
_AC='osCntEgrSuiteDpLevel'
_AB='osCntEgrSuiteServiceLevel'
_AA='osCntEgrSuiteVifIndex'
_A9='osCntEgrSuitePortIndex'
_A8='osCntIngSuiteOtherDropPkts'
_A7='osCntIngSuiteSecDropPkts'
_A6='osCntIngSuiteVlanDropPkts'
_A5='osCntIngSuitePassPkts'
_A4='osCntIngSuiteEntryStatus'
_A3='osCntIngSuiteServiceLevel'
_A2='osCntIngSuiteVifIndex'
_A1='osCntIngSuitePortIndex'
_A0='osCntVifDropPkts'
_z='osCntVifDropOcts'
_y='osCntVifPassPkts'
_x='osCntVifPassOcts'
_w='osCntVifEntryStatus'
_v='osCntPrtEgrDropPkts'
_u='osCntPrtEgrDropOcts'
_t='osCntPrtEgrDropRedPkts'
_s='osCntPrtEgrDropRedOcts'
_r='osCntPrtEgrDropYlwPkts'
_q='osCntPrtEgrDropYlwOcts'
_p='osCntPrtEgrDropGrnPkts'
_o='osCntPrtEgrDropGrnOcts'
_n='osCntPrtEgrPassPkts'
_m='osCntPrtEgrPassOcts'
_l='osCntPrtEgrPassRedPkts'
_k='osCntPrtEgrPassRedOcts'
_j='osCntPrtEgrPassYlwPkts'
_i='osCntPrtEgrPassYlwOcts'
_h='osCntPrtEgrPassGrnPkts'
_g='osCntPrtEgrPassGrnOcts'
_f='osCntPrtEgrEntryStatus'
_e='osCountersVFeaturesSupport'
_d='osCntEgrSuiteCaps'
_c='osCntEgrSuiteTblStatus'
_b='osCntIngSuiteCaps'
_a='osCntIngSuiteTblStatus'
_Z='osCntVifCaps'
_Y='osCntVifDirTblStatus'
_X='osCntPrtEgrCaps'
_W='osCntPrtEgrTblStatus'
_V='osCountersFeaturesSupport'
_U='osCntVBindClient'
_T='osCntBindBlockIndex'
_S='osCntAclMatchingIndex'
_R='osCntAclDirection'
_Q='osCntEgrSuiteIndex'
_P='osCntIngSuiteIndex'
_O='osCntVifServiceLevel'
_N='osCntVifIndex'
_M='osCntPrtEgrServiceLevel'
_L='osCntPrtEgrPortIndex'
_K='invalid'
_J='osCntVifDirection'
_I='DisplayString'
_H='none'
_G='Integer32'
_F='Bits'
_E='not-accessible'
_D='read-write'
_C='read-only'
_B='OS-COUNTERS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oaOptiSwitch,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_F,'Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention','TruthValue')
osCounters=ModuleIdentity((1,3,6,1,4,1,6926,2,8))
if mibBuilder.loadTexts:osCounters.setRevisions(('2016-12-27 00:00','2011-04-05 00:00','2010-07-17 00:00'))
class CntBooleanFlag(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*(('other',-1),('no',0),('yes',1)))
class CntEntryStatusVal(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_K,2),('valid',3),('clear',4)))
class CntEntryStatusExtVal(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),(_K,2),('valid',3),('delete',4),('create',5),('clear',6)))
class CntTableStatusVal(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('invalidTbl',2),('validTbl',3),('clearAll',4)))
class CntPortIndex(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class CntPortIndexOrAll(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
class CntVlanId(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
class CntVlanIdOrAll(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4095))
class CntServiceLevelOrAll(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,8))
class CntDpLevelOrAll(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('all',0),('green',1),('yellow',2),('red',3)))
class CntDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ingress',1),('egress',2)))
class CntMatchingId(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_OsCountersCapabilities_ObjectIdentity=ObjectIdentity
osCountersCapabilities=_OsCountersCapabilities_ObjectIdentity((1,3,6,1,4,1,6926,2,8,1))
class _OsCountersFeaturesSupport_Type(Bits):namedValues=NamedValues(*(('portIngressCounters',0),('portEgressCounters',1),('vifIngressCounters',2),('vifEgressCounters',3),('ingressSetCounters',4),('egressSetCounters',5),('ingressMatchingCounters',6),('egressMatchingCounters',7),('tunnelCounters',8)))
_OsCountersFeaturesSupport_Type.__name__=_F
_OsCountersFeaturesSupport_Object=MibScalar
osCountersFeaturesSupport=_OsCountersFeaturesSupport_Object((1,3,6,1,4,1,6926,2,8,1,1),_OsCountersFeaturesSupport_Type())
osCountersFeaturesSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:osCountersFeaturesSupport.setStatus(_A)
_OsCntPrtEgrTblStatus_Type=CntTableStatusVal
_OsCntPrtEgrTblStatus_Object=MibScalar
osCntPrtEgrTblStatus=_OsCntPrtEgrTblStatus_Object((1,3,6,1,4,1,6926,2,8,1,2),_OsCntPrtEgrTblStatus_Type())
osCntPrtEgrTblStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntPrtEgrTblStatus.setStatus(_A)
class _OsCntPrtEgrCaps_Type(Bits):namedValues=NamedValues(*(('hasPassGrnOcts',0),('hasPassGrnPkts',1),('hasPassYelOcts',2),('hasPassYelPkts',3),('hasPassRedOcts',4),('hasPassRedPkts',5),('hasDropGrnOcts',6),('hasDropGrnPkts',7),('hasDropYelOcts',8),('hasDropYelPkts',9),('hasDropRedOcts',10),('hasDropRedPkts',11)))
_OsCntPrtEgrCaps_Type.__name__=_F
_OsCntPrtEgrCaps_Object=MibScalar
osCntPrtEgrCaps=_OsCntPrtEgrCaps_Object((1,3,6,1,4,1,6926,2,8,1,3),_OsCntPrtEgrCaps_Type())
osCntPrtEgrCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrCaps.setStatus(_A)
_OsCntVifDirTable_Object=MibTable
osCntVifDirTable=_OsCntVifDirTable_Object((1,3,6,1,4,1,6926,2,8,1,4))
if mibBuilder.loadTexts:osCntVifDirTable.setStatus(_A)
_OsCntVifDirEntry_Object=MibTableRow
osCntVifDirEntry=_OsCntVifDirEntry_Object((1,3,6,1,4,1,6926,2,8,1,4,1))
osCntVifDirEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:osCntVifDirEntry.setStatus(_A)
_OsCntVifDirection_Type=CntDirection
_OsCntVifDirection_Object=MibTableColumn
osCntVifDirection=_OsCntVifDirection_Object((1,3,6,1,4,1,6926,2,8,1,4,1,1),_OsCntVifDirection_Type())
osCntVifDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:osCntVifDirection.setStatus(_A)
_OsCntVifDirTblStatus_Type=CntTableStatusVal
_OsCntVifDirTblStatus_Object=MibTableColumn
osCntVifDirTblStatus=_OsCntVifDirTblStatus_Object((1,3,6,1,4,1,6926,2,8,1,4,1,2),_OsCntVifDirTblStatus_Type())
osCntVifDirTblStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntVifDirTblStatus.setStatus(_A)
class _OsCntVifCaps_Type(Bits):namedValues=NamedValues(*(('hasIngPassOcts',0),('hasIngPassPkts',1),('hasEgrPassOcts',2),('hasEgrPassPkts',3)))
_OsCntVifCaps_Type.__name__=_F
_OsCntVifCaps_Object=MibScalar
osCntVifCaps=_OsCntVifCaps_Object((1,3,6,1,4,1,6926,2,8,1,5),_OsCntVifCaps_Type())
osCntVifCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntVifCaps.setStatus(_A)
_OsCntIngSuiteTblStatus_Type=CntTableStatusVal
_OsCntIngSuiteTblStatus_Object=MibScalar
osCntIngSuiteTblStatus=_OsCntIngSuiteTblStatus_Object((1,3,6,1,4,1,6926,2,8,1,6),_OsCntIngSuiteTblStatus_Type())
osCntIngSuiteTblStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntIngSuiteTblStatus.setStatus(_A)
class _OsCntIngSuiteCaps_Type(Bits):namedValues=NamedValues(*(('hasPassPkts',0),('hasVlanDropPkts',1),('hasSecDropPkts',2),('hasOtherDropPkts',3),('hasServiceLevel',4)))
_OsCntIngSuiteCaps_Type.__name__=_F
_OsCntIngSuiteCaps_Object=MibScalar
osCntIngSuiteCaps=_OsCntIngSuiteCaps_Object((1,3,6,1,4,1,6926,2,8,1,7),_OsCntIngSuiteCaps_Type())
osCntIngSuiteCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntIngSuiteCaps.setStatus(_A)
_OsCntEgrSuiteTblStatus_Type=CntTableStatusVal
_OsCntEgrSuiteTblStatus_Object=MibScalar
osCntEgrSuiteTblStatus=_OsCntEgrSuiteTblStatus_Object((1,3,6,1,4,1,6926,2,8,1,8),_OsCntEgrSuiteTblStatus_Type())
osCntEgrSuiteTblStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntEgrSuiteTblStatus.setStatus(_A)
class _OsCntEgrSuiteCaps_Type(Bits):namedValues=NamedValues(*(('hasUcPassPkts',0),('hasMcPassPkts',1),('hasBcPassPkts',2),('hasTxqDropPkts',3),('hasYellow',4),('hasSkip',5),('hasIntPort',6)))
_OsCntEgrSuiteCaps_Type.__name__=_F
_OsCntEgrSuiteCaps_Object=MibScalar
osCntEgrSuiteCaps=_OsCntEgrSuiteCaps_Object((1,3,6,1,4,1,6926,2,8,1,9),_OsCntEgrSuiteCaps_Type())
osCntEgrSuiteCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntEgrSuiteCaps.setStatus(_A)
class _OsCountersVFeaturesSupport_Type(Bits):namedValues=NamedValues(*(('hasAclIngress',0),('hasAclSecondIngress',1),('hasAclEgress',2),('hasVlanPassIngress',3),('hasVlanDropIngress',4),('hasVlanPassEgress',5),('hasVlanDropEgress',6),('hasPortEgress',7),('hasReserved1VBit',8),('hasReserved2VBit',9),('hasTrafficManager',10)))
_OsCountersVFeaturesSupport_Type.__name__=_F
_OsCountersVFeaturesSupport_Object=MibScalar
osCountersVFeaturesSupport=_OsCountersVFeaturesSupport_Object((1,3,6,1,4,1,6926,2,8,1,10),_OsCountersVFeaturesSupport_Type())
osCountersVFeaturesSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:osCountersVFeaturesSupport.setStatus(_A)
_OsCntPrtEgrTable_Object=MibTable
osCntPrtEgrTable=_OsCntPrtEgrTable_Object((1,3,6,1,4,1,6926,2,8,2))
if mibBuilder.loadTexts:osCntPrtEgrTable.setStatus(_A)
_OsCntPrtEgrEntry_Object=MibTableRow
osCntPrtEgrEntry=_OsCntPrtEgrEntry_Object((1,3,6,1,4,1,6926,2,8,2,1))
osCntPrtEgrEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:osCntPrtEgrEntry.setStatus(_A)
_OsCntPrtEgrPortIndex_Type=CntPortIndex
_OsCntPrtEgrPortIndex_Object=MibTableColumn
osCntPrtEgrPortIndex=_OsCntPrtEgrPortIndex_Object((1,3,6,1,4,1,6926,2,8,2,1,1),_OsCntPrtEgrPortIndex_Type())
osCntPrtEgrPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:osCntPrtEgrPortIndex.setStatus(_A)
_OsCntPrtEgrServiceLevel_Type=CntServiceLevelOrAll
_OsCntPrtEgrServiceLevel_Object=MibTableColumn
osCntPrtEgrServiceLevel=_OsCntPrtEgrServiceLevel_Object((1,3,6,1,4,1,6926,2,8,2,1,2),_OsCntPrtEgrServiceLevel_Type())
osCntPrtEgrServiceLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:osCntPrtEgrServiceLevel.setStatus(_A)
_OsCntPrtEgrEntryStatus_Type=CntEntryStatusVal
_OsCntPrtEgrEntryStatus_Object=MibTableColumn
osCntPrtEgrEntryStatus=_OsCntPrtEgrEntryStatus_Object((1,3,6,1,4,1,6926,2,8,2,1,3),_OsCntPrtEgrEntryStatus_Type())
osCntPrtEgrEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntPrtEgrEntryStatus.setStatus(_A)
_OsCntPrtEgrPassGrnOcts_Type=Counter64
_OsCntPrtEgrPassGrnOcts_Object=MibTableColumn
osCntPrtEgrPassGrnOcts=_OsCntPrtEgrPassGrnOcts_Object((1,3,6,1,4,1,6926,2,8,2,1,4),_OsCntPrtEgrPassGrnOcts_Type())
osCntPrtEgrPassGrnOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrPassGrnOcts.setStatus(_A)
_OsCntPrtEgrPassGrnPkts_Type=Counter64
_OsCntPrtEgrPassGrnPkts_Object=MibTableColumn
osCntPrtEgrPassGrnPkts=_OsCntPrtEgrPassGrnPkts_Object((1,3,6,1,4,1,6926,2,8,2,1,5),_OsCntPrtEgrPassGrnPkts_Type())
osCntPrtEgrPassGrnPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrPassGrnPkts.setStatus(_A)
_OsCntPrtEgrPassYlwOcts_Type=Counter64
_OsCntPrtEgrPassYlwOcts_Object=MibTableColumn
osCntPrtEgrPassYlwOcts=_OsCntPrtEgrPassYlwOcts_Object((1,3,6,1,4,1,6926,2,8,2,1,6),_OsCntPrtEgrPassYlwOcts_Type())
osCntPrtEgrPassYlwOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrPassYlwOcts.setStatus(_A)
_OsCntPrtEgrPassYlwPkts_Type=Counter64
_OsCntPrtEgrPassYlwPkts_Object=MibTableColumn
osCntPrtEgrPassYlwPkts=_OsCntPrtEgrPassYlwPkts_Object((1,3,6,1,4,1,6926,2,8,2,1,7),_OsCntPrtEgrPassYlwPkts_Type())
osCntPrtEgrPassYlwPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrPassYlwPkts.setStatus(_A)
_OsCntPrtEgrPassRedOcts_Type=Counter64
_OsCntPrtEgrPassRedOcts_Object=MibTableColumn
osCntPrtEgrPassRedOcts=_OsCntPrtEgrPassRedOcts_Object((1,3,6,1,4,1,6926,2,8,2,1,8),_OsCntPrtEgrPassRedOcts_Type())
osCntPrtEgrPassRedOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrPassRedOcts.setStatus(_A)
_OsCntPrtEgrPassRedPkts_Type=Counter64
_OsCntPrtEgrPassRedPkts_Object=MibTableColumn
osCntPrtEgrPassRedPkts=_OsCntPrtEgrPassRedPkts_Object((1,3,6,1,4,1,6926,2,8,2,1,9),_OsCntPrtEgrPassRedPkts_Type())
osCntPrtEgrPassRedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrPassRedPkts.setStatus(_A)
_OsCntPrtEgrPassOcts_Type=Counter64
_OsCntPrtEgrPassOcts_Object=MibTableColumn
osCntPrtEgrPassOcts=_OsCntPrtEgrPassOcts_Object((1,3,6,1,4,1,6926,2,8,2,1,10),_OsCntPrtEgrPassOcts_Type())
osCntPrtEgrPassOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrPassOcts.setStatus(_A)
_OsCntPrtEgrPassPkts_Type=Counter64
_OsCntPrtEgrPassPkts_Object=MibTableColumn
osCntPrtEgrPassPkts=_OsCntPrtEgrPassPkts_Object((1,3,6,1,4,1,6926,2,8,2,1,11),_OsCntPrtEgrPassPkts_Type())
osCntPrtEgrPassPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrPassPkts.setStatus(_A)
_OsCntPrtEgrDropGrnOcts_Type=Counter64
_OsCntPrtEgrDropGrnOcts_Object=MibTableColumn
osCntPrtEgrDropGrnOcts=_OsCntPrtEgrDropGrnOcts_Object((1,3,6,1,4,1,6926,2,8,2,1,12),_OsCntPrtEgrDropGrnOcts_Type())
osCntPrtEgrDropGrnOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrDropGrnOcts.setStatus(_A)
_OsCntPrtEgrDropGrnPkts_Type=Counter64
_OsCntPrtEgrDropGrnPkts_Object=MibTableColumn
osCntPrtEgrDropGrnPkts=_OsCntPrtEgrDropGrnPkts_Object((1,3,6,1,4,1,6926,2,8,2,1,13),_OsCntPrtEgrDropGrnPkts_Type())
osCntPrtEgrDropGrnPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrDropGrnPkts.setStatus(_A)
_OsCntPrtEgrDropYlwOcts_Type=Counter64
_OsCntPrtEgrDropYlwOcts_Object=MibTableColumn
osCntPrtEgrDropYlwOcts=_OsCntPrtEgrDropYlwOcts_Object((1,3,6,1,4,1,6926,2,8,2,1,14),_OsCntPrtEgrDropYlwOcts_Type())
osCntPrtEgrDropYlwOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrDropYlwOcts.setStatus(_A)
_OsCntPrtEgrDropYlwPkts_Type=Counter64
_OsCntPrtEgrDropYlwPkts_Object=MibTableColumn
osCntPrtEgrDropYlwPkts=_OsCntPrtEgrDropYlwPkts_Object((1,3,6,1,4,1,6926,2,8,2,1,15),_OsCntPrtEgrDropYlwPkts_Type())
osCntPrtEgrDropYlwPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrDropYlwPkts.setStatus(_A)
_OsCntPrtEgrDropRedOcts_Type=Counter64
_OsCntPrtEgrDropRedOcts_Object=MibTableColumn
osCntPrtEgrDropRedOcts=_OsCntPrtEgrDropRedOcts_Object((1,3,6,1,4,1,6926,2,8,2,1,16),_OsCntPrtEgrDropRedOcts_Type())
osCntPrtEgrDropRedOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrDropRedOcts.setStatus(_A)
_OsCntPrtEgrDropRedPkts_Type=Counter64
_OsCntPrtEgrDropRedPkts_Object=MibTableColumn
osCntPrtEgrDropRedPkts=_OsCntPrtEgrDropRedPkts_Object((1,3,6,1,4,1,6926,2,8,2,1,17),_OsCntPrtEgrDropRedPkts_Type())
osCntPrtEgrDropRedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrDropRedPkts.setStatus(_A)
_OsCntPrtEgrDropOcts_Type=Counter64
_OsCntPrtEgrDropOcts_Object=MibTableColumn
osCntPrtEgrDropOcts=_OsCntPrtEgrDropOcts_Object((1,3,6,1,4,1,6926,2,8,2,1,18),_OsCntPrtEgrDropOcts_Type())
osCntPrtEgrDropOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrDropOcts.setStatus(_A)
_OsCntPrtEgrDropPkts_Type=Counter64
_OsCntPrtEgrDropPkts_Object=MibTableColumn
osCntPrtEgrDropPkts=_OsCntPrtEgrDropPkts_Object((1,3,6,1,4,1,6926,2,8,2,1,19),_OsCntPrtEgrDropPkts_Type())
osCntPrtEgrDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntPrtEgrDropPkts.setStatus(_A)
_OsCntVifTable_Object=MibTable
osCntVifTable=_OsCntVifTable_Object((1,3,6,1,4,1,6926,2,8,3))
if mibBuilder.loadTexts:osCntVifTable.setStatus(_A)
_OsCntVifEntry_Object=MibTableRow
osCntVifEntry=_OsCntVifEntry_Object((1,3,6,1,4,1,6926,2,8,3,1))
osCntVifEntry.setIndexNames((0,_B,_J),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:osCntVifEntry.setStatus(_A)
_OsCntVifIndex_Type=CntVlanId
_OsCntVifIndex_Object=MibTableColumn
osCntVifIndex=_OsCntVifIndex_Object((1,3,6,1,4,1,6926,2,8,3,1,1),_OsCntVifIndex_Type())
osCntVifIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:osCntVifIndex.setStatus(_A)
_OsCntVifServiceLevel_Type=CntServiceLevelOrAll
_OsCntVifServiceLevel_Object=MibTableColumn
osCntVifServiceLevel=_OsCntVifServiceLevel_Object((1,3,6,1,4,1,6926,2,8,3,1,2),_OsCntVifServiceLevel_Type())
osCntVifServiceLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:osCntVifServiceLevel.setStatus(_A)
_OsCntVifEntryStatus_Type=CntEntryStatusVal
_OsCntVifEntryStatus_Object=MibTableColumn
osCntVifEntryStatus=_OsCntVifEntryStatus_Object((1,3,6,1,4,1,6926,2,8,3,1,3),_OsCntVifEntryStatus_Type())
osCntVifEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntVifEntryStatus.setStatus(_A)
_OsCntVifPassOcts_Type=Counter64
_OsCntVifPassOcts_Object=MibTableColumn
osCntVifPassOcts=_OsCntVifPassOcts_Object((1,3,6,1,4,1,6926,2,8,3,1,4),_OsCntVifPassOcts_Type())
osCntVifPassOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntVifPassOcts.setStatus(_A)
_OsCntVifPassPkts_Type=Counter64
_OsCntVifPassPkts_Object=MibTableColumn
osCntVifPassPkts=_OsCntVifPassPkts_Object((1,3,6,1,4,1,6926,2,8,3,1,5),_OsCntVifPassPkts_Type())
osCntVifPassPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntVifPassPkts.setStatus(_A)
_OsCntVifDropOcts_Type=Counter64
_OsCntVifDropOcts_Object=MibTableColumn
osCntVifDropOcts=_OsCntVifDropOcts_Object((1,3,6,1,4,1,6926,2,8,3,1,6),_OsCntVifDropOcts_Type())
osCntVifDropOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntVifDropOcts.setStatus(_A)
_OsCntVifDropPkts_Type=Counter64
_OsCntVifDropPkts_Object=MibTableColumn
osCntVifDropPkts=_OsCntVifDropPkts_Object((1,3,6,1,4,1,6926,2,8,3,1,7),_OsCntVifDropPkts_Type())
osCntVifDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntVifDropPkts.setStatus(_A)
_OsCntIngSuiteTable_Object=MibTable
osCntIngSuiteTable=_OsCntIngSuiteTable_Object((1,3,6,1,4,1,6926,2,8,4))
if mibBuilder.loadTexts:osCntIngSuiteTable.setStatus(_A)
_OsCntIngSuiteEntry_Object=MibTableRow
osCntIngSuiteEntry=_OsCntIngSuiteEntry_Object((1,3,6,1,4,1,6926,2,8,4,1))
osCntIngSuiteEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:osCntIngSuiteEntry.setStatus(_A)
_OsCntIngSuiteIndex_Type=Unsigned32
_OsCntIngSuiteIndex_Object=MibTableColumn
osCntIngSuiteIndex=_OsCntIngSuiteIndex_Object((1,3,6,1,4,1,6926,2,8,4,1,1),_OsCntIngSuiteIndex_Type())
osCntIngSuiteIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:osCntIngSuiteIndex.setStatus(_A)
_OsCntIngSuitePortIndex_Type=CntPortIndexOrAll
_OsCntIngSuitePortIndex_Object=MibTableColumn
osCntIngSuitePortIndex=_OsCntIngSuitePortIndex_Object((1,3,6,1,4,1,6926,2,8,4,1,2),_OsCntIngSuitePortIndex_Type())
osCntIngSuitePortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntIngSuitePortIndex.setStatus(_A)
_OsCntIngSuiteVifIndex_Type=CntVlanIdOrAll
_OsCntIngSuiteVifIndex_Object=MibTableColumn
osCntIngSuiteVifIndex=_OsCntIngSuiteVifIndex_Object((1,3,6,1,4,1,6926,2,8,4,1,3),_OsCntIngSuiteVifIndex_Type())
osCntIngSuiteVifIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntIngSuiteVifIndex.setStatus(_A)
_OsCntIngSuiteServiceLevel_Type=CntServiceLevelOrAll
_OsCntIngSuiteServiceLevel_Object=MibTableColumn
osCntIngSuiteServiceLevel=_OsCntIngSuiteServiceLevel_Object((1,3,6,1,4,1,6926,2,8,4,1,4),_OsCntIngSuiteServiceLevel_Type())
osCntIngSuiteServiceLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntIngSuiteServiceLevel.setStatus(_A)
_OsCntIngSuiteEntryStatus_Type=CntEntryStatusExtVal
_OsCntIngSuiteEntryStatus_Object=MibTableColumn
osCntIngSuiteEntryStatus=_OsCntIngSuiteEntryStatus_Object((1,3,6,1,4,1,6926,2,8,4,1,5),_OsCntIngSuiteEntryStatus_Type())
osCntIngSuiteEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntIngSuiteEntryStatus.setStatus(_A)
_OsCntIngSuitePassPkts_Type=Counter64
_OsCntIngSuitePassPkts_Object=MibTableColumn
osCntIngSuitePassPkts=_OsCntIngSuitePassPkts_Object((1,3,6,1,4,1,6926,2,8,4,1,6),_OsCntIngSuitePassPkts_Type())
osCntIngSuitePassPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntIngSuitePassPkts.setStatus(_A)
_OsCntIngSuiteVlanDropPkts_Type=Counter64
_OsCntIngSuiteVlanDropPkts_Object=MibTableColumn
osCntIngSuiteVlanDropPkts=_OsCntIngSuiteVlanDropPkts_Object((1,3,6,1,4,1,6926,2,8,4,1,7),_OsCntIngSuiteVlanDropPkts_Type())
osCntIngSuiteVlanDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntIngSuiteVlanDropPkts.setStatus(_A)
_OsCntIngSuiteSecDropPkts_Type=Counter64
_OsCntIngSuiteSecDropPkts_Object=MibTableColumn
osCntIngSuiteSecDropPkts=_OsCntIngSuiteSecDropPkts_Object((1,3,6,1,4,1,6926,2,8,4,1,8),_OsCntIngSuiteSecDropPkts_Type())
osCntIngSuiteSecDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntIngSuiteSecDropPkts.setStatus(_A)
_OsCntIngSuiteOtherDropPkts_Type=Counter64
_OsCntIngSuiteOtherDropPkts_Object=MibTableColumn
osCntIngSuiteOtherDropPkts=_OsCntIngSuiteOtherDropPkts_Object((1,3,6,1,4,1,6926,2,8,4,1,9),_OsCntIngSuiteOtherDropPkts_Type())
osCntIngSuiteOtherDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntIngSuiteOtherDropPkts.setStatus(_A)
_OsCntEgrSuiteTable_Object=MibTable
osCntEgrSuiteTable=_OsCntEgrSuiteTable_Object((1,3,6,1,4,1,6926,2,8,5))
if mibBuilder.loadTexts:osCntEgrSuiteTable.setStatus(_A)
_OsCntEgrSuiteEntry_Object=MibTableRow
osCntEgrSuiteEntry=_OsCntEgrSuiteEntry_Object((1,3,6,1,4,1,6926,2,8,5,1))
osCntEgrSuiteEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:osCntEgrSuiteEntry.setStatus(_A)
_OsCntEgrSuiteIndex_Type=Unsigned32
_OsCntEgrSuiteIndex_Object=MibTableColumn
osCntEgrSuiteIndex=_OsCntEgrSuiteIndex_Object((1,3,6,1,4,1,6926,2,8,5,1,1),_OsCntEgrSuiteIndex_Type())
osCntEgrSuiteIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:osCntEgrSuiteIndex.setStatus(_A)
_OsCntEgrSuitePortIndex_Type=CntPortIndexOrAll
_OsCntEgrSuitePortIndex_Object=MibTableColumn
osCntEgrSuitePortIndex=_OsCntEgrSuitePortIndex_Object((1,3,6,1,4,1,6926,2,8,5,1,2),_OsCntEgrSuitePortIndex_Type())
osCntEgrSuitePortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntEgrSuitePortIndex.setStatus(_A)
_OsCntEgrSuiteVifIndex_Type=CntVlanIdOrAll
_OsCntEgrSuiteVifIndex_Object=MibTableColumn
osCntEgrSuiteVifIndex=_OsCntEgrSuiteVifIndex_Object((1,3,6,1,4,1,6926,2,8,5,1,3),_OsCntEgrSuiteVifIndex_Type())
osCntEgrSuiteVifIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntEgrSuiteVifIndex.setStatus(_A)
_OsCntEgrSuiteServiceLevel_Type=CntServiceLevelOrAll
_OsCntEgrSuiteServiceLevel_Object=MibTableColumn
osCntEgrSuiteServiceLevel=_OsCntEgrSuiteServiceLevel_Object((1,3,6,1,4,1,6926,2,8,5,1,4),_OsCntEgrSuiteServiceLevel_Type())
osCntEgrSuiteServiceLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntEgrSuiteServiceLevel.setStatus(_A)
_OsCntEgrSuiteDpLevel_Type=CntDpLevelOrAll
_OsCntEgrSuiteDpLevel_Object=MibTableColumn
osCntEgrSuiteDpLevel=_OsCntEgrSuiteDpLevel_Object((1,3,6,1,4,1,6926,2,8,5,1,5),_OsCntEgrSuiteDpLevel_Type())
osCntEgrSuiteDpLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntEgrSuiteDpLevel.setStatus(_A)
_OsCntEgrSuiteIsSkip_Type=CntBooleanFlag
_OsCntEgrSuiteIsSkip_Object=MibTableColumn
osCntEgrSuiteIsSkip=_OsCntEgrSuiteIsSkip_Object((1,3,6,1,4,1,6926,2,8,5,1,6),_OsCntEgrSuiteIsSkip_Type())
osCntEgrSuiteIsSkip.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntEgrSuiteIsSkip.setStatus(_A)
_OsCntEgrSuiteIsIntPort_Type=CntBooleanFlag
_OsCntEgrSuiteIsIntPort_Object=MibTableColumn
osCntEgrSuiteIsIntPort=_OsCntEgrSuiteIsIntPort_Object((1,3,6,1,4,1,6926,2,8,5,1,7),_OsCntEgrSuiteIsIntPort_Type())
osCntEgrSuiteIsIntPort.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntEgrSuiteIsIntPort.setStatus(_A)
_OsCntEgrSuiteEntryStatus_Type=CntEntryStatusExtVal
_OsCntEgrSuiteEntryStatus_Object=MibTableColumn
osCntEgrSuiteEntryStatus=_OsCntEgrSuiteEntryStatus_Object((1,3,6,1,4,1,6926,2,8,5,1,8),_OsCntEgrSuiteEntryStatus_Type())
osCntEgrSuiteEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntEgrSuiteEntryStatus.setStatus(_A)
_OsCntEgrSuiteUcPassPkts_Type=Counter64
_OsCntEgrSuiteUcPassPkts_Object=MibTableColumn
osCntEgrSuiteUcPassPkts=_OsCntEgrSuiteUcPassPkts_Object((1,3,6,1,4,1,6926,2,8,5,1,9),_OsCntEgrSuiteUcPassPkts_Type())
osCntEgrSuiteUcPassPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntEgrSuiteUcPassPkts.setStatus(_A)
_OsCntEgrSuiteMcPassPkts_Type=Counter64
_OsCntEgrSuiteMcPassPkts_Object=MibTableColumn
osCntEgrSuiteMcPassPkts=_OsCntEgrSuiteMcPassPkts_Object((1,3,6,1,4,1,6926,2,8,5,1,10),_OsCntEgrSuiteMcPassPkts_Type())
osCntEgrSuiteMcPassPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntEgrSuiteMcPassPkts.setStatus(_A)
_OsCntEgrSuiteBcPassPkts_Type=Counter64
_OsCntEgrSuiteBcPassPkts_Object=MibTableColumn
osCntEgrSuiteBcPassPkts=_OsCntEgrSuiteBcPassPkts_Object((1,3,6,1,4,1,6926,2,8,5,1,11),_OsCntEgrSuiteBcPassPkts_Type())
osCntEgrSuiteBcPassPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntEgrSuiteBcPassPkts.setStatus(_A)
_OsCntEgrSuiteTxqDropPkts_Type=Counter64
_OsCntEgrSuiteTxqDropPkts_Object=MibTableColumn
osCntEgrSuiteTxqDropPkts=_OsCntEgrSuiteTxqDropPkts_Object((1,3,6,1,4,1,6926,2,8,5,1,12),_OsCntEgrSuiteTxqDropPkts_Type())
osCntEgrSuiteTxqDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntEgrSuiteTxqDropPkts.setStatus(_A)
_OsCntAclTable_Object=MibTable
osCntAclTable=_OsCntAclTable_Object((1,3,6,1,4,1,6926,2,8,6))
if mibBuilder.loadTexts:osCntAclTable.setStatus(_A)
_OsCntAclEntry_Object=MibTableRow
osCntAclEntry=_OsCntAclEntry_Object((1,3,6,1,4,1,6926,2,8,6,1))
osCntAclEntry.setIndexNames((0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:osCntAclEntry.setStatus(_A)
_OsCntAclDirection_Type=CntDirection
_OsCntAclDirection_Object=MibTableColumn
osCntAclDirection=_OsCntAclDirection_Object((1,3,6,1,4,1,6926,2,8,6,1,1),_OsCntAclDirection_Type())
osCntAclDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:osCntAclDirection.setStatus(_A)
_OsCntAclMatchingIndex_Type=CntMatchingId
_OsCntAclMatchingIndex_Object=MibTableColumn
osCntAclMatchingIndex=_OsCntAclMatchingIndex_Object((1,3,6,1,4,1,6926,2,8,6,1,2),_OsCntAclMatchingIndex_Type())
osCntAclMatchingIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:osCntAclMatchingIndex.setStatus(_A)
_OsCntAclEntryStatus_Type=CntEntryStatusVal
_OsCntAclEntryStatus_Object=MibTableColumn
osCntAclEntryStatus=_OsCntAclEntryStatus_Object((1,3,6,1,4,1,6926,2,8,6,1,3),_OsCntAclEntryStatus_Type())
osCntAclEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntAclEntryStatus.setStatus(_A)
_OsCntAclMatchOcts_Type=Counter64
_OsCntAclMatchOcts_Object=MibTableColumn
osCntAclMatchOcts=_OsCntAclMatchOcts_Object((1,3,6,1,4,1,6926,2,8,6,1,4),_OsCntAclMatchOcts_Type())
osCntAclMatchOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntAclMatchOcts.setStatus(_A)
_OsCntAclMatchPkts_Type=Counter64
_OsCntAclMatchPkts_Object=MibTableColumn
osCntAclMatchPkts=_OsCntAclMatchPkts_Object((1,3,6,1,4,1,6926,2,8,6,1,5),_OsCntAclMatchPkts_Type())
osCntAclMatchPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntAclMatchPkts.setStatus(_A)
_OsCntBindTable_Object=MibTable
osCntBindTable=_OsCntBindTable_Object((1,3,6,1,4,1,6926,2,8,10))
if mibBuilder.loadTexts:osCntBindTable.setStatus(_A)
_OsCntBindEntry_Object=MibTableRow
osCntBindEntry=_OsCntBindEntry_Object((1,3,6,1,4,1,6926,2,8,10,1))
osCntBindEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:osCntBindEntry.setStatus(_A)
_OsCntBindBlockIndex_Type=Unsigned32
_OsCntBindBlockIndex_Object=MibTableColumn
osCntBindBlockIndex=_OsCntBindBlockIndex_Object((1,3,6,1,4,1,6926,2,8,10,1,1),_OsCntBindBlockIndex_Type())
osCntBindBlockIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:osCntBindBlockIndex.setStatus(_A)
class _OsCntBindCountersMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),('aclIngressCounter',2),('aclEgressCounter',3),('portEgressCounter',4),('vlanEgressCounter',5),('vlanIngressCounter',6)))
_OsCntBindCountersMode_Type.__name__=_G
_OsCntBindCountersMode_Object=MibTableColumn
osCntBindCountersMode=_OsCntBindCountersMode_Object((1,3,6,1,4,1,6926,2,8,10,1,2),_OsCntBindCountersMode_Type())
osCntBindCountersMode.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntBindCountersMode.setStatus(_A)
class _OsCntBindCountersRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('range2k',1),('range4k',2)))
_OsCntBindCountersRange_Type.__name__=_G
_OsCntBindCountersRange_Object=MibTableColumn
osCntBindCountersRange=_OsCntBindCountersRange_Object((1,3,6,1,4,1,6926,2,8,10,1,3),_OsCntBindCountersRange_Type())
osCntBindCountersRange.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntBindCountersRange.setStatus(_A)
class _OsCntBindLastError_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,160))
_OsCntBindLastError_Type.__name__=_I
_OsCntBindLastError_Object=MibTableColumn
osCntBindLastError=_OsCntBindLastError_Object((1,3,6,1,4,1,6926,2,8,10,1,4),_OsCntBindLastError_Type())
osCntBindLastError.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntBindLastError.setStatus(_A)
_OsCntVBindTable_Object=MibTable
osCntVBindTable=_OsCntVBindTable_Object((1,3,6,1,4,1,6926,2,8,11))
if mibBuilder.loadTexts:osCntVBindTable.setStatus(_A)
_OsCntVBindEntry_Object=MibTableRow
osCntVBindEntry=_OsCntVBindEntry_Object((1,3,6,1,4,1,6926,2,8,11,1))
osCntVBindEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:osCntVBindEntry.setStatus(_A)
class _OsCntVBindClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('cncAclIngress',1),('cncAclSecondIngress',2),('cncAclEgress',3),('cncVlanPassIngress',4),('cncVlanDropIngress',5),('cncVlanPassEgress',6),('cncVlanDropEgress',7),('cncPortEgress',8),('cncReserved1VBit',9),('cncReserved2VBit',10),('cncTrafficManager',11)))
_OsCntVBindClient_Type.__name__=_G
_OsCntVBindClient_Object=MibTableColumn
osCntVBindClient=_OsCntVBindClient_Object((1,3,6,1,4,1,6926,2,8,11,1,1),_OsCntVBindClient_Type())
osCntVBindClient.setMaxAccess(_E)
if mibBuilder.loadTexts:osCntVBindClient.setStatus(_A)
_OsCntVBindIsActive_Type=TruthValue
_OsCntVBindIsActive_Object=MibTableColumn
osCntVBindIsActive=_OsCntVBindIsActive_Object((1,3,6,1,4,1,6926,2,8,11,1,3),_OsCntVBindIsActive_Type())
osCntVBindIsActive.setMaxAccess(_D)
if mibBuilder.loadTexts:osCntVBindIsActive.setStatus(_A)
class _OsCntVBindLastError_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,160))
_OsCntVBindLastError_Type.__name__=_I
_OsCntVBindLastError_Object=MibTableColumn
osCntVBindLastError=_OsCntVBindLastError_Object((1,3,6,1,4,1,6926,2,8,11,1,4),_OsCntVBindLastError_Type())
osCntVBindLastError.setMaxAccess(_C)
if mibBuilder.loadTexts:osCntVBindLastError.setStatus(_A)
_OsCountersConformance_ObjectIdentity=ObjectIdentity
osCountersConformance=_OsCountersConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,8,100))
_OsCountersMIBCompliances_ObjectIdentity=ObjectIdentity
osCountersMIBCompliances=_OsCountersMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,8,100,1))
_OsCountersMIBGroups_ObjectIdentity=ObjectIdentity
osCountersMIBGroups=_OsCountersMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,8,100,2))
osCountersMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,8,100,2,1))
osCountersMandatoryGroup.setObjects((_B,_V))
if mibBuilder.loadTexts:osCountersMandatoryGroup.setStatus(_A)
osCountersOptGroup=ObjectGroup((1,3,6,1,4,1,6926,2,8,100,2,2))
osCountersOptGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:osCountersOptGroup.setStatus(_A)
osCountersMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,8,100,1,1))
osCountersMIBCompliance.setObjects(*((_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:osCountersMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CntBooleanFlag':CntBooleanFlag,'CntEntryStatusVal':CntEntryStatusVal,'CntEntryStatusExtVal':CntEntryStatusExtVal,'CntTableStatusVal':CntTableStatusVal,'CntPortIndex':CntPortIndex,'CntPortIndexOrAll':CntPortIndexOrAll,'CntVlanId':CntVlanId,'CntVlanIdOrAll':CntVlanIdOrAll,'CntServiceLevelOrAll':CntServiceLevelOrAll,'CntDpLevelOrAll':CntDpLevelOrAll,'CntDirection':CntDirection,'CntMatchingId':CntMatchingId,'osCounters':osCounters,'osCountersCapabilities':osCountersCapabilities,_V:osCountersFeaturesSupport,_W:osCntPrtEgrTblStatus,_X:osCntPrtEgrCaps,'osCntVifDirTable':osCntVifDirTable,'osCntVifDirEntry':osCntVifDirEntry,_J:osCntVifDirection,_Y:osCntVifDirTblStatus,_Z:osCntVifCaps,_a:osCntIngSuiteTblStatus,_b:osCntIngSuiteCaps,_c:osCntEgrSuiteTblStatus,_d:osCntEgrSuiteCaps,_e:osCountersVFeaturesSupport,'osCntPrtEgrTable':osCntPrtEgrTable,'osCntPrtEgrEntry':osCntPrtEgrEntry,_L:osCntPrtEgrPortIndex,_M:osCntPrtEgrServiceLevel,_f:osCntPrtEgrEntryStatus,_g:osCntPrtEgrPassGrnOcts,_h:osCntPrtEgrPassGrnPkts,_i:osCntPrtEgrPassYlwOcts,_j:osCntPrtEgrPassYlwPkts,_k:osCntPrtEgrPassRedOcts,_l:osCntPrtEgrPassRedPkts,_m:osCntPrtEgrPassOcts,_n:osCntPrtEgrPassPkts,_o:osCntPrtEgrDropGrnOcts,_p:osCntPrtEgrDropGrnPkts,_q:osCntPrtEgrDropYlwOcts,_r:osCntPrtEgrDropYlwPkts,_s:osCntPrtEgrDropRedOcts,_t:osCntPrtEgrDropRedPkts,_u:osCntPrtEgrDropOcts,_v:osCntPrtEgrDropPkts,'osCntVifTable':osCntVifTable,'osCntVifEntry':osCntVifEntry,_N:osCntVifIndex,_O:osCntVifServiceLevel,_w:osCntVifEntryStatus,_x:osCntVifPassOcts,_y:osCntVifPassPkts,_z:osCntVifDropOcts,_A0:osCntVifDropPkts,'osCntIngSuiteTable':osCntIngSuiteTable,'osCntIngSuiteEntry':osCntIngSuiteEntry,_P:osCntIngSuiteIndex,_A1:osCntIngSuitePortIndex,_A2:osCntIngSuiteVifIndex,_A3:osCntIngSuiteServiceLevel,_A4:osCntIngSuiteEntryStatus,_A5:osCntIngSuitePassPkts,_A6:osCntIngSuiteVlanDropPkts,_A7:osCntIngSuiteSecDropPkts,_A8:osCntIngSuiteOtherDropPkts,'osCntEgrSuiteTable':osCntEgrSuiteTable,'osCntEgrSuiteEntry':osCntEgrSuiteEntry,_Q:osCntEgrSuiteIndex,_A9:osCntEgrSuitePortIndex,_AA:osCntEgrSuiteVifIndex,_AB:osCntEgrSuiteServiceLevel,_AC:osCntEgrSuiteDpLevel,_AD:osCntEgrSuiteIsSkip,_AE:osCntEgrSuiteIsIntPort,_AF:osCntEgrSuiteEntryStatus,_AG:osCntEgrSuiteUcPassPkts,_AH:osCntEgrSuiteMcPassPkts,_AI:osCntEgrSuiteBcPassPkts,_AJ:osCntEgrSuiteTxqDropPkts,'osCntAclTable':osCntAclTable,'osCntAclEntry':osCntAclEntry,_R:osCntAclDirection,_S:osCntAclMatchingIndex,_AK:osCntAclEntryStatus,_AL:osCntAclMatchOcts,_AM:osCntAclMatchPkts,'osCntBindTable':osCntBindTable,'osCntBindEntry':osCntBindEntry,_T:osCntBindBlockIndex,_AN:osCntBindCountersMode,_AO:osCntBindCountersRange,_AP:osCntBindLastError,'osCntVBindTable':osCntVBindTable,'osCntVBindEntry':osCntVBindEntry,_U:osCntVBindClient,_AQ:osCntVBindIsActive,_AR:osCntVBindLastError,'osCountersConformance':osCountersConformance,'osCountersMIBCompliances':osCountersMIBCompliances,'osCountersMIBCompliance':osCountersMIBCompliance,'osCountersMIBGroups':osCountersMIBGroups,_AS:osCountersMandatoryGroup,_AT:osCountersOptGroup})