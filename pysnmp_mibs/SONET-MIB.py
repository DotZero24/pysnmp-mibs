_Aq='sonetSectionStuff2'
_Ap='sonetMediumStuff2'
_Ao='sonetFarEndVTStuff'
_An='sonetVTStuff'
_Am='sonetFarEndPathStuff'
_Al='sonetPathStuff'
_Ak='sonetFarEndLineStuff'
_Aj='sonetLineStuff'
_Ai='sonetSectionStuff'
_Ah='sonetMediumStuff'
_Ag='sonetFarEndVTIntervalValidData'
_Af='sonetFarEndPathIntervalValidData'
_Ae='sonetFarEndLineIntervalValidData'
_Ad='sonetVTIntervalValidData'
_Ac='sonetPathIntervalValidData'
_Ab='sonetLineIntervalValidData'
_Aa='sonetSectionIntervalValidData'
_AZ='sonetSESthresholdSet'
_AY='sonetMediumLoopbackConfig'
_AX='sonetMediumInvalidIntervals'
_AW='sonetFarEndVTIntervalNumber'
_AV='sonetVTIntervalNumber'
_AU='sonetFarEndPathIntervalNumber'
_AT='sonetPathIntervalNumber'
_AS='sonetFarEndLineIntervalNumber'
_AR='sonetLineIntervalNumber'
_AQ='sonetSectionIntervalNumber'
_AP='DisplayString'
_AO='sonetFarEndVTIntervalUASs'
_AN='sonetFarEndVTIntervalCVs'
_AM='sonetFarEndVTIntervalSESs'
_AL='sonetFarEndVTIntervalESs'
_AK='sonetFarEndVTCurrentUASs'
_AJ='sonetFarEndVTCurrentCVs'
_AI='sonetFarEndVTCurrentSESs'
_AH='sonetFarEndVTCurrentESs'
_AG='sonetVTIntervalUASs'
_AF='sonetVTIntervalCVs'
_AE='sonetVTIntervalSESs'
_AD='sonetVTIntervalESs'
_AC='sonetVTCurrentUASs'
_AB='sonetVTCurrentCVs'
_AA='sonetVTCurrentSESs'
_A9='sonetVTCurrentESs'
_A8='sonetVTCurrentStatus'
_A7='sonetVTCurrentWidth'
_A6='sonetFarEndPathIntervalUASs'
_A5='sonetFarEndPathIntervalCVs'
_A4='sonetFarEndPathIntervalSESs'
_A3='sonetFarEndPathIntervalESs'
_A2='sonetFarEndPathCurrentUASs'
_A1='sonetFarEndPathCurrentCVs'
_A0='sonetFarEndPathCurrentSESs'
_z='sonetFarEndPathCurrentESs'
_y='sonetPathIntervalUASs'
_x='sonetPathIntervalCVs'
_w='sonetPathIntervalSESs'
_v='sonetPathIntervalESs'
_u='sonetPathCurrentUASs'
_t='sonetPathCurrentCVs'
_s='sonetPathCurrentSESs'
_r='sonetPathCurrentESs'
_q='sonetPathCurrentStatus'
_p='sonetPathCurrentWidth'
_o='sonetFarEndLineIntervalUASs'
_n='sonetFarEndLineIntervalCVs'
_m='sonetFarEndLineIntervalSESs'
_l='sonetFarEndLineIntervalESs'
_k='sonetFarEndLineCurrentUASs'
_j='sonetFarEndLineCurrentCVs'
_i='sonetFarEndLineCurrentSESs'
_h='sonetFarEndLineCurrentESs'
_g='sonetLineIntervalUASs'
_f='sonetLineIntervalCVs'
_e='sonetLineIntervalSESs'
_d='sonetLineIntervalESs'
_c='sonetLineCurrentUASs'
_b='sonetLineCurrentCVs'
_a='sonetLineCurrentSESs'
_Z='sonetLineCurrentESs'
_Y='sonetLineCurrentStatus'
_X='sonetSectionIntervalCVs'
_W='sonetSectionIntervalSEFSs'
_V='sonetSectionIntervalSESs'
_U='sonetSectionIntervalESs'
_T='sonetSectionCurrentCVs'
_S='sonetSectionCurrentSEFSs'
_R='sonetSectionCurrentSESs'
_Q='sonetSectionCurrentESs'
_P='sonetSectionCurrentStatus'
_O='sonetMediumCircuitIdentifier'
_N='sonetMediumLineType'
_M='sonetMediumLineCoding'
_L='sonetMediumValidIntervals'
_K='sonetMediumTimeElapsed'
_J='sonetMediumType'
_I='not-accessible'
_H='read-write'
_G='deprecated'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='current'
_A='SONET-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
PerfCurrentCount,PerfIntervalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_AP,'PhysAddress','TextualConvention','TruthValue')
sonetMIB=ModuleIdentity((1,3,6,1,2,1,10,39))
if mibBuilder.loadTexts:sonetMIB.setRevisions(('2003-08-11 00:00','1998-10-19 00:00','1994-01-03 00:00'))
_SonetObjects_ObjectIdentity=ObjectIdentity
sonetObjects=_SonetObjects_ObjectIdentity((1,3,6,1,2,1,10,39,1))
_SonetMedium_ObjectIdentity=ObjectIdentity
sonetMedium=_SonetMedium_ObjectIdentity((1,3,6,1,2,1,10,39,1,1))
_SonetMediumTable_Object=MibTable
sonetMediumTable=_SonetMediumTable_Object((1,3,6,1,2,1,10,39,1,1,1))
if mibBuilder.loadTexts:sonetMediumTable.setStatus(_B)
_SonetMediumEntry_Object=MibTableRow
sonetMediumEntry=_SonetMediumEntry_Object((1,3,6,1,2,1,10,39,1,1,1,1))
sonetMediumEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:sonetMediumEntry.setStatus(_B)
class _SonetMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sonet',1),('sdh',2)))
_SonetMediumType_Type.__name__=_D
_SonetMediumType_Object=MibTableColumn
sonetMediumType=_SonetMediumType_Object((1,3,6,1,2,1,10,39,1,1,1,1,1),_SonetMediumType_Type())
sonetMediumType.setMaxAccess(_H)
if mibBuilder.loadTexts:sonetMediumType.setStatus(_B)
class _SonetMediumTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_SonetMediumTimeElapsed_Type.__name__=_D
_SonetMediumTimeElapsed_Object=MibTableColumn
sonetMediumTimeElapsed=_SonetMediumTimeElapsed_Object((1,3,6,1,2,1,10,39,1,1,1,1,2),_SonetMediumTimeElapsed_Type())
sonetMediumTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetMediumTimeElapsed.setStatus(_B)
class _SonetMediumValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_SonetMediumValidIntervals_Type.__name__=_D
_SonetMediumValidIntervals_Object=MibTableColumn
sonetMediumValidIntervals=_SonetMediumValidIntervals_Object((1,3,6,1,2,1,10,39,1,1,1,1,3),_SonetMediumValidIntervals_Type())
sonetMediumValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetMediumValidIntervals.setStatus(_B)
class _SonetMediumLineCoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('sonetMediumOther',1),('sonetMediumB3ZS',2),('sonetMediumCMI',3),('sonetMediumNRZ',4),('sonetMediumRZ',5)))
_SonetMediumLineCoding_Type.__name__=_D
_SonetMediumLineCoding_Object=MibTableColumn
sonetMediumLineCoding=_SonetMediumLineCoding_Object((1,3,6,1,2,1,10,39,1,1,1,1,4),_SonetMediumLineCoding_Type())
sonetMediumLineCoding.setMaxAccess(_H)
if mibBuilder.loadTexts:sonetMediumLineCoding.setStatus(_B)
class _SonetMediumLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('sonetOther',1),('sonetShortSingleMode',2),('sonetLongSingleMode',3),('sonetMultiMode',4),('sonetCoax',5),('sonetUTP',6)))
_SonetMediumLineType_Type.__name__=_D
_SonetMediumLineType_Object=MibTableColumn
sonetMediumLineType=_SonetMediumLineType_Object((1,3,6,1,2,1,10,39,1,1,1,1,5),_SonetMediumLineType_Type())
sonetMediumLineType.setMaxAccess(_H)
if mibBuilder.loadTexts:sonetMediumLineType.setStatus(_B)
class _SonetMediumCircuitIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SonetMediumCircuitIdentifier_Type.__name__=_AP
_SonetMediumCircuitIdentifier_Object=MibTableColumn
sonetMediumCircuitIdentifier=_SonetMediumCircuitIdentifier_Object((1,3,6,1,2,1,10,39,1,1,1,1,6),_SonetMediumCircuitIdentifier_Type())
sonetMediumCircuitIdentifier.setMaxAccess(_H)
if mibBuilder.loadTexts:sonetMediumCircuitIdentifier.setStatus(_B)
class _SonetMediumInvalidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_SonetMediumInvalidIntervals_Type.__name__=_D
_SonetMediumInvalidIntervals_Object=MibTableColumn
sonetMediumInvalidIntervals=_SonetMediumInvalidIntervals_Object((1,3,6,1,2,1,10,39,1,1,1,1,7),_SonetMediumInvalidIntervals_Type())
sonetMediumInvalidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetMediumInvalidIntervals.setStatus(_B)
class _SonetMediumLoopbackConfig_Type(Bits):namedValues=NamedValues(*(('sonetNoLoop',0),('sonetFacilityLoop',1),('sonetTerminalLoop',2),('sonetOtherLoop',3)))
_SonetMediumLoopbackConfig_Type.__name__='Bits'
_SonetMediumLoopbackConfig_Object=MibTableColumn
sonetMediumLoopbackConfig=_SonetMediumLoopbackConfig_Object((1,3,6,1,2,1,10,39,1,1,1,1,8),_SonetMediumLoopbackConfig_Type())
sonetMediumLoopbackConfig.setMaxAccess(_H)
if mibBuilder.loadTexts:sonetMediumLoopbackConfig.setStatus(_B)
class _SonetSESthresholdSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('bellcore1991',2),('ansi1993',3),('itu1995',4),('ansi1997',5)))
_SonetSESthresholdSet_Type.__name__=_D
_SonetSESthresholdSet_Object=MibScalar
sonetSESthresholdSet=_SonetSESthresholdSet_Object((1,3,6,1,2,1,10,39,1,1,2),_SonetSESthresholdSet_Type())
sonetSESthresholdSet.setMaxAccess(_H)
if mibBuilder.loadTexts:sonetSESthresholdSet.setStatus(_B)
_SonetSection_ObjectIdentity=ObjectIdentity
sonetSection=_SonetSection_ObjectIdentity((1,3,6,1,2,1,10,39,1,2))
_SonetSectionCurrentTable_Object=MibTable
sonetSectionCurrentTable=_SonetSectionCurrentTable_Object((1,3,6,1,2,1,10,39,1,2,1))
if mibBuilder.loadTexts:sonetSectionCurrentTable.setStatus(_B)
_SonetSectionCurrentEntry_Object=MibTableRow
sonetSectionCurrentEntry=_SonetSectionCurrentEntry_Object((1,3,6,1,2,1,10,39,1,2,1,1))
sonetSectionCurrentEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:sonetSectionCurrentEntry.setStatus(_B)
class _SonetSectionCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_SonetSectionCurrentStatus_Type.__name__=_D
_SonetSectionCurrentStatus_Object=MibTableColumn
sonetSectionCurrentStatus=_SonetSectionCurrentStatus_Object((1,3,6,1,2,1,10,39,1,2,1,1,1),_SonetSectionCurrentStatus_Type())
sonetSectionCurrentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionCurrentStatus.setStatus(_B)
_SonetSectionCurrentESs_Type=PerfCurrentCount
_SonetSectionCurrentESs_Object=MibTableColumn
sonetSectionCurrentESs=_SonetSectionCurrentESs_Object((1,3,6,1,2,1,10,39,1,2,1,1,2),_SonetSectionCurrentESs_Type())
sonetSectionCurrentESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionCurrentESs.setStatus(_B)
_SonetSectionCurrentSESs_Type=PerfCurrentCount
_SonetSectionCurrentSESs_Object=MibTableColumn
sonetSectionCurrentSESs=_SonetSectionCurrentSESs_Object((1,3,6,1,2,1,10,39,1,2,1,1,3),_SonetSectionCurrentSESs_Type())
sonetSectionCurrentSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionCurrentSESs.setStatus(_B)
_SonetSectionCurrentSEFSs_Type=PerfCurrentCount
_SonetSectionCurrentSEFSs_Object=MibTableColumn
sonetSectionCurrentSEFSs=_SonetSectionCurrentSEFSs_Object((1,3,6,1,2,1,10,39,1,2,1,1,4),_SonetSectionCurrentSEFSs_Type())
sonetSectionCurrentSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionCurrentSEFSs.setStatus(_B)
_SonetSectionCurrentCVs_Type=PerfCurrentCount
_SonetSectionCurrentCVs_Object=MibTableColumn
sonetSectionCurrentCVs=_SonetSectionCurrentCVs_Object((1,3,6,1,2,1,10,39,1,2,1,1,5),_SonetSectionCurrentCVs_Type())
sonetSectionCurrentCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionCurrentCVs.setStatus(_B)
_SonetSectionIntervalTable_Object=MibTable
sonetSectionIntervalTable=_SonetSectionIntervalTable_Object((1,3,6,1,2,1,10,39,1,2,2))
if mibBuilder.loadTexts:sonetSectionIntervalTable.setStatus(_B)
_SonetSectionIntervalEntry_Object=MibTableRow
sonetSectionIntervalEntry=_SonetSectionIntervalEntry_Object((1,3,6,1,2,1,10,39,1,2,2,1))
sonetSectionIntervalEntry.setIndexNames((0,_E,_F),(0,_A,_AQ))
if mibBuilder.loadTexts:sonetSectionIntervalEntry.setStatus(_B)
class _SonetSectionIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_SonetSectionIntervalNumber_Type.__name__=_D
_SonetSectionIntervalNumber_Object=MibTableColumn
sonetSectionIntervalNumber=_SonetSectionIntervalNumber_Object((1,3,6,1,2,1,10,39,1,2,2,1,1),_SonetSectionIntervalNumber_Type())
sonetSectionIntervalNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:sonetSectionIntervalNumber.setStatus(_B)
_SonetSectionIntervalESs_Type=PerfIntervalCount
_SonetSectionIntervalESs_Object=MibTableColumn
sonetSectionIntervalESs=_SonetSectionIntervalESs_Object((1,3,6,1,2,1,10,39,1,2,2,1,2),_SonetSectionIntervalESs_Type())
sonetSectionIntervalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionIntervalESs.setStatus(_B)
_SonetSectionIntervalSESs_Type=PerfIntervalCount
_SonetSectionIntervalSESs_Object=MibTableColumn
sonetSectionIntervalSESs=_SonetSectionIntervalSESs_Object((1,3,6,1,2,1,10,39,1,2,2,1,3),_SonetSectionIntervalSESs_Type())
sonetSectionIntervalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionIntervalSESs.setStatus(_B)
_SonetSectionIntervalSEFSs_Type=PerfIntervalCount
_SonetSectionIntervalSEFSs_Object=MibTableColumn
sonetSectionIntervalSEFSs=_SonetSectionIntervalSEFSs_Object((1,3,6,1,2,1,10,39,1,2,2,1,4),_SonetSectionIntervalSEFSs_Type())
sonetSectionIntervalSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionIntervalSEFSs.setStatus(_B)
_SonetSectionIntervalCVs_Type=PerfIntervalCount
_SonetSectionIntervalCVs_Object=MibTableColumn
sonetSectionIntervalCVs=_SonetSectionIntervalCVs_Object((1,3,6,1,2,1,10,39,1,2,2,1,5),_SonetSectionIntervalCVs_Type())
sonetSectionIntervalCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionIntervalCVs.setStatus(_B)
_SonetSectionIntervalValidData_Type=TruthValue
_SonetSectionIntervalValidData_Object=MibTableColumn
sonetSectionIntervalValidData=_SonetSectionIntervalValidData_Object((1,3,6,1,2,1,10,39,1,2,2,1,6),_SonetSectionIntervalValidData_Type())
sonetSectionIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionIntervalValidData.setStatus(_B)
_SonetLine_ObjectIdentity=ObjectIdentity
sonetLine=_SonetLine_ObjectIdentity((1,3,6,1,2,1,10,39,1,3))
_SonetLineCurrentTable_Object=MibTable
sonetLineCurrentTable=_SonetLineCurrentTable_Object((1,3,6,1,2,1,10,39,1,3,1))
if mibBuilder.loadTexts:sonetLineCurrentTable.setStatus(_B)
_SonetLineCurrentEntry_Object=MibTableRow
sonetLineCurrentEntry=_SonetLineCurrentEntry_Object((1,3,6,1,2,1,10,39,1,3,1,1))
sonetLineCurrentEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:sonetLineCurrentEntry.setStatus(_B)
class _SonetLineCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_SonetLineCurrentStatus_Type.__name__=_D
_SonetLineCurrentStatus_Object=MibTableColumn
sonetLineCurrentStatus=_SonetLineCurrentStatus_Object((1,3,6,1,2,1,10,39,1,3,1,1,1),_SonetLineCurrentStatus_Type())
sonetLineCurrentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineCurrentStatus.setStatus(_B)
_SonetLineCurrentESs_Type=PerfCurrentCount
_SonetLineCurrentESs_Object=MibTableColumn
sonetLineCurrentESs=_SonetLineCurrentESs_Object((1,3,6,1,2,1,10,39,1,3,1,1,2),_SonetLineCurrentESs_Type())
sonetLineCurrentESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineCurrentESs.setStatus(_B)
_SonetLineCurrentSESs_Type=PerfCurrentCount
_SonetLineCurrentSESs_Object=MibTableColumn
sonetLineCurrentSESs=_SonetLineCurrentSESs_Object((1,3,6,1,2,1,10,39,1,3,1,1,3),_SonetLineCurrentSESs_Type())
sonetLineCurrentSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineCurrentSESs.setStatus(_B)
_SonetLineCurrentCVs_Type=PerfCurrentCount
_SonetLineCurrentCVs_Object=MibTableColumn
sonetLineCurrentCVs=_SonetLineCurrentCVs_Object((1,3,6,1,2,1,10,39,1,3,1,1,4),_SonetLineCurrentCVs_Type())
sonetLineCurrentCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineCurrentCVs.setStatus(_B)
_SonetLineCurrentUASs_Type=PerfCurrentCount
_SonetLineCurrentUASs_Object=MibTableColumn
sonetLineCurrentUASs=_SonetLineCurrentUASs_Object((1,3,6,1,2,1,10,39,1,3,1,1,5),_SonetLineCurrentUASs_Type())
sonetLineCurrentUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineCurrentUASs.setStatus(_B)
_SonetLineIntervalTable_Object=MibTable
sonetLineIntervalTable=_SonetLineIntervalTable_Object((1,3,6,1,2,1,10,39,1,3,2))
if mibBuilder.loadTexts:sonetLineIntervalTable.setStatus(_B)
_SonetLineIntervalEntry_Object=MibTableRow
sonetLineIntervalEntry=_SonetLineIntervalEntry_Object((1,3,6,1,2,1,10,39,1,3,2,1))
sonetLineIntervalEntry.setIndexNames((0,_E,_F),(0,_A,_AR))
if mibBuilder.loadTexts:sonetLineIntervalEntry.setStatus(_B)
class _SonetLineIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_SonetLineIntervalNumber_Type.__name__=_D
_SonetLineIntervalNumber_Object=MibTableColumn
sonetLineIntervalNumber=_SonetLineIntervalNumber_Object((1,3,6,1,2,1,10,39,1,3,2,1,1),_SonetLineIntervalNumber_Type())
sonetLineIntervalNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:sonetLineIntervalNumber.setStatus(_B)
_SonetLineIntervalESs_Type=PerfIntervalCount
_SonetLineIntervalESs_Object=MibTableColumn
sonetLineIntervalESs=_SonetLineIntervalESs_Object((1,3,6,1,2,1,10,39,1,3,2,1,2),_SonetLineIntervalESs_Type())
sonetLineIntervalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineIntervalESs.setStatus(_B)
_SonetLineIntervalSESs_Type=PerfIntervalCount
_SonetLineIntervalSESs_Object=MibTableColumn
sonetLineIntervalSESs=_SonetLineIntervalSESs_Object((1,3,6,1,2,1,10,39,1,3,2,1,3),_SonetLineIntervalSESs_Type())
sonetLineIntervalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineIntervalSESs.setStatus(_B)
_SonetLineIntervalCVs_Type=PerfIntervalCount
_SonetLineIntervalCVs_Object=MibTableColumn
sonetLineIntervalCVs=_SonetLineIntervalCVs_Object((1,3,6,1,2,1,10,39,1,3,2,1,4),_SonetLineIntervalCVs_Type())
sonetLineIntervalCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineIntervalCVs.setStatus(_B)
_SonetLineIntervalUASs_Type=PerfIntervalCount
_SonetLineIntervalUASs_Object=MibTableColumn
sonetLineIntervalUASs=_SonetLineIntervalUASs_Object((1,3,6,1,2,1,10,39,1,3,2,1,5),_SonetLineIntervalUASs_Type())
sonetLineIntervalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineIntervalUASs.setStatus(_B)
_SonetLineIntervalValidData_Type=TruthValue
_SonetLineIntervalValidData_Object=MibTableColumn
sonetLineIntervalValidData=_SonetLineIntervalValidData_Object((1,3,6,1,2,1,10,39,1,3,2,1,6),_SonetLineIntervalValidData_Type())
sonetLineIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineIntervalValidData.setStatus(_B)
_SonetFarEndLine_ObjectIdentity=ObjectIdentity
sonetFarEndLine=_SonetFarEndLine_ObjectIdentity((1,3,6,1,2,1,10,39,1,4))
_SonetFarEndLineCurrentTable_Object=MibTable
sonetFarEndLineCurrentTable=_SonetFarEndLineCurrentTable_Object((1,3,6,1,2,1,10,39,1,4,1))
if mibBuilder.loadTexts:sonetFarEndLineCurrentTable.setStatus(_B)
_SonetFarEndLineCurrentEntry_Object=MibTableRow
sonetFarEndLineCurrentEntry=_SonetFarEndLineCurrentEntry_Object((1,3,6,1,2,1,10,39,1,4,1,1))
sonetFarEndLineCurrentEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:sonetFarEndLineCurrentEntry.setStatus(_B)
_SonetFarEndLineCurrentESs_Type=PerfCurrentCount
_SonetFarEndLineCurrentESs_Object=MibTableColumn
sonetFarEndLineCurrentESs=_SonetFarEndLineCurrentESs_Object((1,3,6,1,2,1,10,39,1,4,1,1,1),_SonetFarEndLineCurrentESs_Type())
sonetFarEndLineCurrentESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndLineCurrentESs.setStatus(_B)
_SonetFarEndLineCurrentSESs_Type=PerfCurrentCount
_SonetFarEndLineCurrentSESs_Object=MibTableColumn
sonetFarEndLineCurrentSESs=_SonetFarEndLineCurrentSESs_Object((1,3,6,1,2,1,10,39,1,4,1,1,2),_SonetFarEndLineCurrentSESs_Type())
sonetFarEndLineCurrentSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndLineCurrentSESs.setStatus(_B)
_SonetFarEndLineCurrentCVs_Type=PerfCurrentCount
_SonetFarEndLineCurrentCVs_Object=MibTableColumn
sonetFarEndLineCurrentCVs=_SonetFarEndLineCurrentCVs_Object((1,3,6,1,2,1,10,39,1,4,1,1,3),_SonetFarEndLineCurrentCVs_Type())
sonetFarEndLineCurrentCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndLineCurrentCVs.setStatus(_B)
_SonetFarEndLineCurrentUASs_Type=PerfCurrentCount
_SonetFarEndLineCurrentUASs_Object=MibTableColumn
sonetFarEndLineCurrentUASs=_SonetFarEndLineCurrentUASs_Object((1,3,6,1,2,1,10,39,1,4,1,1,4),_SonetFarEndLineCurrentUASs_Type())
sonetFarEndLineCurrentUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndLineCurrentUASs.setStatus(_B)
_SonetFarEndLineIntervalTable_Object=MibTable
sonetFarEndLineIntervalTable=_SonetFarEndLineIntervalTable_Object((1,3,6,1,2,1,10,39,1,4,2))
if mibBuilder.loadTexts:sonetFarEndLineIntervalTable.setStatus(_B)
_SonetFarEndLineIntervalEntry_Object=MibTableRow
sonetFarEndLineIntervalEntry=_SonetFarEndLineIntervalEntry_Object((1,3,6,1,2,1,10,39,1,4,2,1))
sonetFarEndLineIntervalEntry.setIndexNames((0,_E,_F),(0,_A,_AS))
if mibBuilder.loadTexts:sonetFarEndLineIntervalEntry.setStatus(_B)
class _SonetFarEndLineIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_SonetFarEndLineIntervalNumber_Type.__name__=_D
_SonetFarEndLineIntervalNumber_Object=MibTableColumn
sonetFarEndLineIntervalNumber=_SonetFarEndLineIntervalNumber_Object((1,3,6,1,2,1,10,39,1,4,2,1,1),_SonetFarEndLineIntervalNumber_Type())
sonetFarEndLineIntervalNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:sonetFarEndLineIntervalNumber.setStatus(_B)
_SonetFarEndLineIntervalESs_Type=PerfIntervalCount
_SonetFarEndLineIntervalESs_Object=MibTableColumn
sonetFarEndLineIntervalESs=_SonetFarEndLineIntervalESs_Object((1,3,6,1,2,1,10,39,1,4,2,1,2),_SonetFarEndLineIntervalESs_Type())
sonetFarEndLineIntervalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndLineIntervalESs.setStatus(_B)
_SonetFarEndLineIntervalSESs_Type=PerfIntervalCount
_SonetFarEndLineIntervalSESs_Object=MibTableColumn
sonetFarEndLineIntervalSESs=_SonetFarEndLineIntervalSESs_Object((1,3,6,1,2,1,10,39,1,4,2,1,3),_SonetFarEndLineIntervalSESs_Type())
sonetFarEndLineIntervalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndLineIntervalSESs.setStatus(_B)
_SonetFarEndLineIntervalCVs_Type=PerfIntervalCount
_SonetFarEndLineIntervalCVs_Object=MibTableColumn
sonetFarEndLineIntervalCVs=_SonetFarEndLineIntervalCVs_Object((1,3,6,1,2,1,10,39,1,4,2,1,4),_SonetFarEndLineIntervalCVs_Type())
sonetFarEndLineIntervalCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndLineIntervalCVs.setStatus(_B)
_SonetFarEndLineIntervalUASs_Type=PerfIntervalCount
_SonetFarEndLineIntervalUASs_Object=MibTableColumn
sonetFarEndLineIntervalUASs=_SonetFarEndLineIntervalUASs_Object((1,3,6,1,2,1,10,39,1,4,2,1,5),_SonetFarEndLineIntervalUASs_Type())
sonetFarEndLineIntervalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndLineIntervalUASs.setStatus(_B)
_SonetFarEndLineIntervalValidData_Type=TruthValue
_SonetFarEndLineIntervalValidData_Object=MibTableColumn
sonetFarEndLineIntervalValidData=_SonetFarEndLineIntervalValidData_Object((1,3,6,1,2,1,10,39,1,4,2,1,6),_SonetFarEndLineIntervalValidData_Type())
sonetFarEndLineIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndLineIntervalValidData.setStatus(_B)
_SonetObjectsPath_ObjectIdentity=ObjectIdentity
sonetObjectsPath=_SonetObjectsPath_ObjectIdentity((1,3,6,1,2,1,10,39,2))
_SonetPath_ObjectIdentity=ObjectIdentity
sonetPath=_SonetPath_ObjectIdentity((1,3,6,1,2,1,10,39,2,1))
_SonetPathCurrentTable_Object=MibTable
sonetPathCurrentTable=_SonetPathCurrentTable_Object((1,3,6,1,2,1,10,39,2,1,1))
if mibBuilder.loadTexts:sonetPathCurrentTable.setStatus(_B)
_SonetPathCurrentEntry_Object=MibTableRow
sonetPathCurrentEntry=_SonetPathCurrentEntry_Object((1,3,6,1,2,1,10,39,2,1,1,1))
sonetPathCurrentEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:sonetPathCurrentEntry.setStatus(_B)
class _SonetPathCurrentWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('sts1',1),('sts3cSTM1',2),('sts12cSTM4',3),('sts24c',4),('sts48cSTM16',5),('sts192cSTM64',6),('sts768cSTM256',7)))
_SonetPathCurrentWidth_Type.__name__=_D
_SonetPathCurrentWidth_Object=MibTableColumn
sonetPathCurrentWidth=_SonetPathCurrentWidth_Object((1,3,6,1,2,1,10,39,2,1,1,1,1),_SonetPathCurrentWidth_Type())
sonetPathCurrentWidth.setMaxAccess(_H)
if mibBuilder.loadTexts:sonetPathCurrentWidth.setStatus(_B)
class _SonetPathCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,62))
_SonetPathCurrentStatus_Type.__name__=_D
_SonetPathCurrentStatus_Object=MibTableColumn
sonetPathCurrentStatus=_SonetPathCurrentStatus_Object((1,3,6,1,2,1,10,39,2,1,1,1,2),_SonetPathCurrentStatus_Type())
sonetPathCurrentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathCurrentStatus.setStatus(_B)
_SonetPathCurrentESs_Type=PerfCurrentCount
_SonetPathCurrentESs_Object=MibTableColumn
sonetPathCurrentESs=_SonetPathCurrentESs_Object((1,3,6,1,2,1,10,39,2,1,1,1,3),_SonetPathCurrentESs_Type())
sonetPathCurrentESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathCurrentESs.setStatus(_B)
_SonetPathCurrentSESs_Type=PerfCurrentCount
_SonetPathCurrentSESs_Object=MibTableColumn
sonetPathCurrentSESs=_SonetPathCurrentSESs_Object((1,3,6,1,2,1,10,39,2,1,1,1,4),_SonetPathCurrentSESs_Type())
sonetPathCurrentSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathCurrentSESs.setStatus(_B)
_SonetPathCurrentCVs_Type=PerfCurrentCount
_SonetPathCurrentCVs_Object=MibTableColumn
sonetPathCurrentCVs=_SonetPathCurrentCVs_Object((1,3,6,1,2,1,10,39,2,1,1,1,5),_SonetPathCurrentCVs_Type())
sonetPathCurrentCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathCurrentCVs.setStatus(_B)
_SonetPathCurrentUASs_Type=PerfCurrentCount
_SonetPathCurrentUASs_Object=MibTableColumn
sonetPathCurrentUASs=_SonetPathCurrentUASs_Object((1,3,6,1,2,1,10,39,2,1,1,1,6),_SonetPathCurrentUASs_Type())
sonetPathCurrentUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathCurrentUASs.setStatus(_B)
_SonetPathIntervalTable_Object=MibTable
sonetPathIntervalTable=_SonetPathIntervalTable_Object((1,3,6,1,2,1,10,39,2,1,2))
if mibBuilder.loadTexts:sonetPathIntervalTable.setStatus(_B)
_SonetPathIntervalEntry_Object=MibTableRow
sonetPathIntervalEntry=_SonetPathIntervalEntry_Object((1,3,6,1,2,1,10,39,2,1,2,1))
sonetPathIntervalEntry.setIndexNames((0,_E,_F),(0,_A,_AT))
if mibBuilder.loadTexts:sonetPathIntervalEntry.setStatus(_B)
class _SonetPathIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_SonetPathIntervalNumber_Type.__name__=_D
_SonetPathIntervalNumber_Object=MibTableColumn
sonetPathIntervalNumber=_SonetPathIntervalNumber_Object((1,3,6,1,2,1,10,39,2,1,2,1,1),_SonetPathIntervalNumber_Type())
sonetPathIntervalNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:sonetPathIntervalNumber.setStatus(_B)
_SonetPathIntervalESs_Type=PerfIntervalCount
_SonetPathIntervalESs_Object=MibTableColumn
sonetPathIntervalESs=_SonetPathIntervalESs_Object((1,3,6,1,2,1,10,39,2,1,2,1,2),_SonetPathIntervalESs_Type())
sonetPathIntervalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathIntervalESs.setStatus(_B)
_SonetPathIntervalSESs_Type=PerfIntervalCount
_SonetPathIntervalSESs_Object=MibTableColumn
sonetPathIntervalSESs=_SonetPathIntervalSESs_Object((1,3,6,1,2,1,10,39,2,1,2,1,3),_SonetPathIntervalSESs_Type())
sonetPathIntervalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathIntervalSESs.setStatus(_B)
_SonetPathIntervalCVs_Type=PerfIntervalCount
_SonetPathIntervalCVs_Object=MibTableColumn
sonetPathIntervalCVs=_SonetPathIntervalCVs_Object((1,3,6,1,2,1,10,39,2,1,2,1,4),_SonetPathIntervalCVs_Type())
sonetPathIntervalCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathIntervalCVs.setStatus(_B)
_SonetPathIntervalUASs_Type=PerfIntervalCount
_SonetPathIntervalUASs_Object=MibTableColumn
sonetPathIntervalUASs=_SonetPathIntervalUASs_Object((1,3,6,1,2,1,10,39,2,1,2,1,5),_SonetPathIntervalUASs_Type())
sonetPathIntervalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathIntervalUASs.setStatus(_B)
_SonetPathIntervalValidData_Type=TruthValue
_SonetPathIntervalValidData_Object=MibTableColumn
sonetPathIntervalValidData=_SonetPathIntervalValidData_Object((1,3,6,1,2,1,10,39,2,1,2,1,6),_SonetPathIntervalValidData_Type())
sonetPathIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathIntervalValidData.setStatus(_B)
_SonetFarEndPath_ObjectIdentity=ObjectIdentity
sonetFarEndPath=_SonetFarEndPath_ObjectIdentity((1,3,6,1,2,1,10,39,2,2))
_SonetFarEndPathCurrentTable_Object=MibTable
sonetFarEndPathCurrentTable=_SonetFarEndPathCurrentTable_Object((1,3,6,1,2,1,10,39,2,2,1))
if mibBuilder.loadTexts:sonetFarEndPathCurrentTable.setStatus(_B)
_SonetFarEndPathCurrentEntry_Object=MibTableRow
sonetFarEndPathCurrentEntry=_SonetFarEndPathCurrentEntry_Object((1,3,6,1,2,1,10,39,2,2,1,1))
sonetFarEndPathCurrentEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:sonetFarEndPathCurrentEntry.setStatus(_B)
_SonetFarEndPathCurrentESs_Type=PerfCurrentCount
_SonetFarEndPathCurrentESs_Object=MibTableColumn
sonetFarEndPathCurrentESs=_SonetFarEndPathCurrentESs_Object((1,3,6,1,2,1,10,39,2,2,1,1,1),_SonetFarEndPathCurrentESs_Type())
sonetFarEndPathCurrentESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndPathCurrentESs.setStatus(_B)
_SonetFarEndPathCurrentSESs_Type=PerfCurrentCount
_SonetFarEndPathCurrentSESs_Object=MibTableColumn
sonetFarEndPathCurrentSESs=_SonetFarEndPathCurrentSESs_Object((1,3,6,1,2,1,10,39,2,2,1,1,2),_SonetFarEndPathCurrentSESs_Type())
sonetFarEndPathCurrentSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndPathCurrentSESs.setStatus(_B)
_SonetFarEndPathCurrentCVs_Type=PerfCurrentCount
_SonetFarEndPathCurrentCVs_Object=MibTableColumn
sonetFarEndPathCurrentCVs=_SonetFarEndPathCurrentCVs_Object((1,3,6,1,2,1,10,39,2,2,1,1,3),_SonetFarEndPathCurrentCVs_Type())
sonetFarEndPathCurrentCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndPathCurrentCVs.setStatus(_B)
_SonetFarEndPathCurrentUASs_Type=PerfCurrentCount
_SonetFarEndPathCurrentUASs_Object=MibTableColumn
sonetFarEndPathCurrentUASs=_SonetFarEndPathCurrentUASs_Object((1,3,6,1,2,1,10,39,2,2,1,1,4),_SonetFarEndPathCurrentUASs_Type())
sonetFarEndPathCurrentUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndPathCurrentUASs.setStatus(_B)
_SonetFarEndPathIntervalTable_Object=MibTable
sonetFarEndPathIntervalTable=_SonetFarEndPathIntervalTable_Object((1,3,6,1,2,1,10,39,2,2,2))
if mibBuilder.loadTexts:sonetFarEndPathIntervalTable.setStatus(_B)
_SonetFarEndPathIntervalEntry_Object=MibTableRow
sonetFarEndPathIntervalEntry=_SonetFarEndPathIntervalEntry_Object((1,3,6,1,2,1,10,39,2,2,2,1))
sonetFarEndPathIntervalEntry.setIndexNames((0,_E,_F),(0,_A,_AU))
if mibBuilder.loadTexts:sonetFarEndPathIntervalEntry.setStatus(_B)
class _SonetFarEndPathIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_SonetFarEndPathIntervalNumber_Type.__name__=_D
_SonetFarEndPathIntervalNumber_Object=MibTableColumn
sonetFarEndPathIntervalNumber=_SonetFarEndPathIntervalNumber_Object((1,3,6,1,2,1,10,39,2,2,2,1,1),_SonetFarEndPathIntervalNumber_Type())
sonetFarEndPathIntervalNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:sonetFarEndPathIntervalNumber.setStatus(_B)
_SonetFarEndPathIntervalESs_Type=PerfIntervalCount
_SonetFarEndPathIntervalESs_Object=MibTableColumn
sonetFarEndPathIntervalESs=_SonetFarEndPathIntervalESs_Object((1,3,6,1,2,1,10,39,2,2,2,1,2),_SonetFarEndPathIntervalESs_Type())
sonetFarEndPathIntervalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndPathIntervalESs.setStatus(_B)
_SonetFarEndPathIntervalSESs_Type=PerfIntervalCount
_SonetFarEndPathIntervalSESs_Object=MibTableColumn
sonetFarEndPathIntervalSESs=_SonetFarEndPathIntervalSESs_Object((1,3,6,1,2,1,10,39,2,2,2,1,3),_SonetFarEndPathIntervalSESs_Type())
sonetFarEndPathIntervalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndPathIntervalSESs.setStatus(_B)
_SonetFarEndPathIntervalCVs_Type=PerfIntervalCount
_SonetFarEndPathIntervalCVs_Object=MibTableColumn
sonetFarEndPathIntervalCVs=_SonetFarEndPathIntervalCVs_Object((1,3,6,1,2,1,10,39,2,2,2,1,4),_SonetFarEndPathIntervalCVs_Type())
sonetFarEndPathIntervalCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndPathIntervalCVs.setStatus(_B)
_SonetFarEndPathIntervalUASs_Type=PerfIntervalCount
_SonetFarEndPathIntervalUASs_Object=MibTableColumn
sonetFarEndPathIntervalUASs=_SonetFarEndPathIntervalUASs_Object((1,3,6,1,2,1,10,39,2,2,2,1,5),_SonetFarEndPathIntervalUASs_Type())
sonetFarEndPathIntervalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndPathIntervalUASs.setStatus(_B)
_SonetFarEndPathIntervalValidData_Type=TruthValue
_SonetFarEndPathIntervalValidData_Object=MibTableColumn
sonetFarEndPathIntervalValidData=_SonetFarEndPathIntervalValidData_Object((1,3,6,1,2,1,10,39,2,2,2,1,6),_SonetFarEndPathIntervalValidData_Type())
sonetFarEndPathIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndPathIntervalValidData.setStatus(_B)
_SonetObjectsVT_ObjectIdentity=ObjectIdentity
sonetObjectsVT=_SonetObjectsVT_ObjectIdentity((1,3,6,1,2,1,10,39,3))
_SonetVT_ObjectIdentity=ObjectIdentity
sonetVT=_SonetVT_ObjectIdentity((1,3,6,1,2,1,10,39,3,1))
_SonetVTCurrentTable_Object=MibTable
sonetVTCurrentTable=_SonetVTCurrentTable_Object((1,3,6,1,2,1,10,39,3,1,1))
if mibBuilder.loadTexts:sonetVTCurrentTable.setStatus(_B)
_SonetVTCurrentEntry_Object=MibTableRow
sonetVTCurrentEntry=_SonetVTCurrentEntry_Object((1,3,6,1,2,1,10,39,3,1,1,1))
sonetVTCurrentEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:sonetVTCurrentEntry.setStatus(_B)
class _SonetVTCurrentWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('vtWidth15VC11',1),('vtWidth2VC12',2),('vtWidth3',3),('vtWidth6VC2',4),('vtWidth6c',5)))
_SonetVTCurrentWidth_Type.__name__=_D
_SonetVTCurrentWidth_Object=MibTableColumn
sonetVTCurrentWidth=_SonetVTCurrentWidth_Object((1,3,6,1,2,1,10,39,3,1,1,1,1),_SonetVTCurrentWidth_Type())
sonetVTCurrentWidth.setMaxAccess(_H)
if mibBuilder.loadTexts:sonetVTCurrentWidth.setStatus(_B)
class _SonetVTCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,126))
_SonetVTCurrentStatus_Type.__name__=_D
_SonetVTCurrentStatus_Object=MibTableColumn
sonetVTCurrentStatus=_SonetVTCurrentStatus_Object((1,3,6,1,2,1,10,39,3,1,1,1,2),_SonetVTCurrentStatus_Type())
sonetVTCurrentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTCurrentStatus.setStatus(_B)
_SonetVTCurrentESs_Type=PerfCurrentCount
_SonetVTCurrentESs_Object=MibTableColumn
sonetVTCurrentESs=_SonetVTCurrentESs_Object((1,3,6,1,2,1,10,39,3,1,1,1,3),_SonetVTCurrentESs_Type())
sonetVTCurrentESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTCurrentESs.setStatus(_B)
_SonetVTCurrentSESs_Type=PerfCurrentCount
_SonetVTCurrentSESs_Object=MibTableColumn
sonetVTCurrentSESs=_SonetVTCurrentSESs_Object((1,3,6,1,2,1,10,39,3,1,1,1,4),_SonetVTCurrentSESs_Type())
sonetVTCurrentSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTCurrentSESs.setStatus(_B)
_SonetVTCurrentCVs_Type=PerfCurrentCount
_SonetVTCurrentCVs_Object=MibTableColumn
sonetVTCurrentCVs=_SonetVTCurrentCVs_Object((1,3,6,1,2,1,10,39,3,1,1,1,5),_SonetVTCurrentCVs_Type())
sonetVTCurrentCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTCurrentCVs.setStatus(_B)
_SonetVTCurrentUASs_Type=PerfCurrentCount
_SonetVTCurrentUASs_Object=MibTableColumn
sonetVTCurrentUASs=_SonetVTCurrentUASs_Object((1,3,6,1,2,1,10,39,3,1,1,1,6),_SonetVTCurrentUASs_Type())
sonetVTCurrentUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTCurrentUASs.setStatus(_B)
_SonetVTIntervalTable_Object=MibTable
sonetVTIntervalTable=_SonetVTIntervalTable_Object((1,3,6,1,2,1,10,39,3,1,2))
if mibBuilder.loadTexts:sonetVTIntervalTable.setStatus(_B)
_SonetVTIntervalEntry_Object=MibTableRow
sonetVTIntervalEntry=_SonetVTIntervalEntry_Object((1,3,6,1,2,1,10,39,3,1,2,1))
sonetVTIntervalEntry.setIndexNames((0,_E,_F),(0,_A,_AV))
if mibBuilder.loadTexts:sonetVTIntervalEntry.setStatus(_B)
class _SonetVTIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_SonetVTIntervalNumber_Type.__name__=_D
_SonetVTIntervalNumber_Object=MibTableColumn
sonetVTIntervalNumber=_SonetVTIntervalNumber_Object((1,3,6,1,2,1,10,39,3,1,2,1,1),_SonetVTIntervalNumber_Type())
sonetVTIntervalNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:sonetVTIntervalNumber.setStatus(_B)
_SonetVTIntervalESs_Type=PerfIntervalCount
_SonetVTIntervalESs_Object=MibTableColumn
sonetVTIntervalESs=_SonetVTIntervalESs_Object((1,3,6,1,2,1,10,39,3,1,2,1,2),_SonetVTIntervalESs_Type())
sonetVTIntervalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTIntervalESs.setStatus(_B)
_SonetVTIntervalSESs_Type=PerfIntervalCount
_SonetVTIntervalSESs_Object=MibTableColumn
sonetVTIntervalSESs=_SonetVTIntervalSESs_Object((1,3,6,1,2,1,10,39,3,1,2,1,3),_SonetVTIntervalSESs_Type())
sonetVTIntervalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTIntervalSESs.setStatus(_B)
_SonetVTIntervalCVs_Type=PerfIntervalCount
_SonetVTIntervalCVs_Object=MibTableColumn
sonetVTIntervalCVs=_SonetVTIntervalCVs_Object((1,3,6,1,2,1,10,39,3,1,2,1,4),_SonetVTIntervalCVs_Type())
sonetVTIntervalCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTIntervalCVs.setStatus(_B)
_SonetVTIntervalUASs_Type=PerfIntervalCount
_SonetVTIntervalUASs_Object=MibTableColumn
sonetVTIntervalUASs=_SonetVTIntervalUASs_Object((1,3,6,1,2,1,10,39,3,1,2,1,5),_SonetVTIntervalUASs_Type())
sonetVTIntervalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTIntervalUASs.setStatus(_B)
_SonetVTIntervalValidData_Type=TruthValue
_SonetVTIntervalValidData_Object=MibTableColumn
sonetVTIntervalValidData=_SonetVTIntervalValidData_Object((1,3,6,1,2,1,10,39,3,1,2,1,6),_SonetVTIntervalValidData_Type())
sonetVTIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTIntervalValidData.setStatus(_B)
_SonetFarEndVT_ObjectIdentity=ObjectIdentity
sonetFarEndVT=_SonetFarEndVT_ObjectIdentity((1,3,6,1,2,1,10,39,3,2))
_SonetFarEndVTCurrentTable_Object=MibTable
sonetFarEndVTCurrentTable=_SonetFarEndVTCurrentTable_Object((1,3,6,1,2,1,10,39,3,2,1))
if mibBuilder.loadTexts:sonetFarEndVTCurrentTable.setStatus(_B)
_SonetFarEndVTCurrentEntry_Object=MibTableRow
sonetFarEndVTCurrentEntry=_SonetFarEndVTCurrentEntry_Object((1,3,6,1,2,1,10,39,3,2,1,1))
sonetFarEndVTCurrentEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:sonetFarEndVTCurrentEntry.setStatus(_B)
_SonetFarEndVTCurrentESs_Type=PerfCurrentCount
_SonetFarEndVTCurrentESs_Object=MibTableColumn
sonetFarEndVTCurrentESs=_SonetFarEndVTCurrentESs_Object((1,3,6,1,2,1,10,39,3,2,1,1,1),_SonetFarEndVTCurrentESs_Type())
sonetFarEndVTCurrentESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndVTCurrentESs.setStatus(_B)
_SonetFarEndVTCurrentSESs_Type=PerfCurrentCount
_SonetFarEndVTCurrentSESs_Object=MibTableColumn
sonetFarEndVTCurrentSESs=_SonetFarEndVTCurrentSESs_Object((1,3,6,1,2,1,10,39,3,2,1,1,2),_SonetFarEndVTCurrentSESs_Type())
sonetFarEndVTCurrentSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndVTCurrentSESs.setStatus(_B)
_SonetFarEndVTCurrentCVs_Type=PerfCurrentCount
_SonetFarEndVTCurrentCVs_Object=MibTableColumn
sonetFarEndVTCurrentCVs=_SonetFarEndVTCurrentCVs_Object((1,3,6,1,2,1,10,39,3,2,1,1,3),_SonetFarEndVTCurrentCVs_Type())
sonetFarEndVTCurrentCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndVTCurrentCVs.setStatus(_B)
_SonetFarEndVTCurrentUASs_Type=PerfCurrentCount
_SonetFarEndVTCurrentUASs_Object=MibTableColumn
sonetFarEndVTCurrentUASs=_SonetFarEndVTCurrentUASs_Object((1,3,6,1,2,1,10,39,3,2,1,1,4),_SonetFarEndVTCurrentUASs_Type())
sonetFarEndVTCurrentUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndVTCurrentUASs.setStatus(_B)
_SonetFarEndVTIntervalTable_Object=MibTable
sonetFarEndVTIntervalTable=_SonetFarEndVTIntervalTable_Object((1,3,6,1,2,1,10,39,3,2,2))
if mibBuilder.loadTexts:sonetFarEndVTIntervalTable.setStatus(_B)
_SonetFarEndVTIntervalEntry_Object=MibTableRow
sonetFarEndVTIntervalEntry=_SonetFarEndVTIntervalEntry_Object((1,3,6,1,2,1,10,39,3,2,2,1))
sonetFarEndVTIntervalEntry.setIndexNames((0,_E,_F),(0,_A,_AW))
if mibBuilder.loadTexts:sonetFarEndVTIntervalEntry.setStatus(_B)
class _SonetFarEndVTIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_SonetFarEndVTIntervalNumber_Type.__name__=_D
_SonetFarEndVTIntervalNumber_Object=MibTableColumn
sonetFarEndVTIntervalNumber=_SonetFarEndVTIntervalNumber_Object((1,3,6,1,2,1,10,39,3,2,2,1,1),_SonetFarEndVTIntervalNumber_Type())
sonetFarEndVTIntervalNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:sonetFarEndVTIntervalNumber.setStatus(_B)
_SonetFarEndVTIntervalESs_Type=PerfIntervalCount
_SonetFarEndVTIntervalESs_Object=MibTableColumn
sonetFarEndVTIntervalESs=_SonetFarEndVTIntervalESs_Object((1,3,6,1,2,1,10,39,3,2,2,1,2),_SonetFarEndVTIntervalESs_Type())
sonetFarEndVTIntervalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndVTIntervalESs.setStatus(_B)
_SonetFarEndVTIntervalSESs_Type=PerfIntervalCount
_SonetFarEndVTIntervalSESs_Object=MibTableColumn
sonetFarEndVTIntervalSESs=_SonetFarEndVTIntervalSESs_Object((1,3,6,1,2,1,10,39,3,2,2,1,3),_SonetFarEndVTIntervalSESs_Type())
sonetFarEndVTIntervalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndVTIntervalSESs.setStatus(_B)
_SonetFarEndVTIntervalCVs_Type=PerfIntervalCount
_SonetFarEndVTIntervalCVs_Object=MibTableColumn
sonetFarEndVTIntervalCVs=_SonetFarEndVTIntervalCVs_Object((1,3,6,1,2,1,10,39,3,2,2,1,4),_SonetFarEndVTIntervalCVs_Type())
sonetFarEndVTIntervalCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndVTIntervalCVs.setStatus(_B)
_SonetFarEndVTIntervalUASs_Type=PerfIntervalCount
_SonetFarEndVTIntervalUASs_Object=MibTableColumn
sonetFarEndVTIntervalUASs=_SonetFarEndVTIntervalUASs_Object((1,3,6,1,2,1,10,39,3,2,2,1,5),_SonetFarEndVTIntervalUASs_Type())
sonetFarEndVTIntervalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndVTIntervalUASs.setStatus(_B)
_SonetFarEndVTIntervalValidData_Type=TruthValue
_SonetFarEndVTIntervalValidData_Object=MibTableColumn
sonetFarEndVTIntervalValidData=_SonetFarEndVTIntervalValidData_Object((1,3,6,1,2,1,10,39,3,2,2,1,6),_SonetFarEndVTIntervalValidData_Type())
sonetFarEndVTIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndVTIntervalValidData.setStatus(_B)
_SonetConformance_ObjectIdentity=ObjectIdentity
sonetConformance=_SonetConformance_ObjectIdentity((1,3,6,1,2,1,10,39,4))
_SonetGroups_ObjectIdentity=ObjectIdentity
sonetGroups=_SonetGroups_ObjectIdentity((1,3,6,1,2,1,10,39,4,1))
_SonetCompliances_ObjectIdentity=ObjectIdentity
sonetCompliances=_SonetCompliances_ObjectIdentity((1,3,6,1,2,1,10,39,4,2))
sonetMediumStuff=ObjectGroup((1,3,6,1,2,1,10,39,4,1,1))
sonetMediumStuff.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:sonetMediumStuff.setStatus(_G)
sonetSectionStuff=ObjectGroup((1,3,6,1,2,1,10,39,4,1,2))
sonetSectionStuff.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:sonetSectionStuff.setStatus(_G)
sonetLineStuff=ObjectGroup((1,3,6,1,2,1,10,39,4,1,3))
sonetLineStuff.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:sonetLineStuff.setStatus(_G)
sonetFarEndLineStuff=ObjectGroup((1,3,6,1,2,1,10,39,4,1,4))
sonetFarEndLineStuff.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:sonetFarEndLineStuff.setStatus(_G)
sonetPathStuff=ObjectGroup((1,3,6,1,2,1,10,39,4,1,5))
sonetPathStuff.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:sonetPathStuff.setStatus(_G)
sonetFarEndPathStuff=ObjectGroup((1,3,6,1,2,1,10,39,4,1,6))
sonetFarEndPathStuff.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:sonetFarEndPathStuff.setStatus(_G)
sonetVTStuff=ObjectGroup((1,3,6,1,2,1,10,39,4,1,7))
sonetVTStuff.setObjects(*((_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:sonetVTStuff.setStatus(_G)
sonetFarEndVTStuff=ObjectGroup((1,3,6,1,2,1,10,39,4,1,8))
sonetFarEndVTStuff.setObjects(*((_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:sonetFarEndVTStuff.setStatus(_G)
sonetMediumStuff2=ObjectGroup((1,3,6,1,2,1,10,39,4,1,9))
sonetMediumStuff2.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:sonetMediumStuff2.setStatus(_B)
sonetSectionStuff2=ObjectGroup((1,3,6,1,2,1,10,39,4,1,10))
sonetSectionStuff2.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Aa)))
if mibBuilder.loadTexts:sonetSectionStuff2.setStatus(_B)
sonetLineStuff2=ObjectGroup((1,3,6,1,2,1,10,39,4,1,11))
sonetLineStuff2.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_Ab)))
if mibBuilder.loadTexts:sonetLineStuff2.setStatus(_B)
sonetPathStuff2=ObjectGroup((1,3,6,1,2,1,10,39,4,1,12))
sonetPathStuff2.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_Ac)))
if mibBuilder.loadTexts:sonetPathStuff2.setStatus(_B)
sonetVTStuff2=ObjectGroup((1,3,6,1,2,1,10,39,4,1,13))
sonetVTStuff2.setObjects(*((_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_Ad)))
if mibBuilder.loadTexts:sonetVTStuff2.setStatus(_B)
sonetFarEndLineStuff2=ObjectGroup((1,3,6,1,2,1,10,39,4,1,14))
sonetFarEndLineStuff2.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_Ae)))
if mibBuilder.loadTexts:sonetFarEndLineStuff2.setStatus(_B)
sonetFarEndPathStuff2=ObjectGroup((1,3,6,1,2,1,10,39,4,1,15))
sonetFarEndPathStuff2.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_Af)))
if mibBuilder.loadTexts:sonetFarEndPathStuff2.setStatus(_B)
sonetFarEndVTStuff2=ObjectGroup((1,3,6,1,2,1,10,39,4,1,16))
sonetFarEndVTStuff2.setObjects(*((_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_Ag)))
if mibBuilder.loadTexts:sonetFarEndVTStuff2.setStatus(_B)
sonetCompliance=ModuleCompliance((1,3,6,1,2,1,10,39,4,2,1))
sonetCompliance.setObjects(*((_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao)))
if mibBuilder.loadTexts:sonetCompliance.setStatus(_G)
sonetCompliance2=ModuleCompliance((1,3,6,1,2,1,10,39,4,2,2))
sonetCompliance2.setObjects(*((_A,_Ap),(_A,_Aq)))
if mibBuilder.loadTexts:sonetCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'sonetMIB':sonetMIB,'sonetObjects':sonetObjects,'sonetMedium':sonetMedium,'sonetMediumTable':sonetMediumTable,'sonetMediumEntry':sonetMediumEntry,_J:sonetMediumType,_K:sonetMediumTimeElapsed,_L:sonetMediumValidIntervals,_M:sonetMediumLineCoding,_N:sonetMediumLineType,_O:sonetMediumCircuitIdentifier,_AX:sonetMediumInvalidIntervals,_AY:sonetMediumLoopbackConfig,_AZ:sonetSESthresholdSet,'sonetSection':sonetSection,'sonetSectionCurrentTable':sonetSectionCurrentTable,'sonetSectionCurrentEntry':sonetSectionCurrentEntry,_P:sonetSectionCurrentStatus,_Q:sonetSectionCurrentESs,_R:sonetSectionCurrentSESs,_S:sonetSectionCurrentSEFSs,_T:sonetSectionCurrentCVs,'sonetSectionIntervalTable':sonetSectionIntervalTable,'sonetSectionIntervalEntry':sonetSectionIntervalEntry,_AQ:sonetSectionIntervalNumber,_U:sonetSectionIntervalESs,_V:sonetSectionIntervalSESs,_W:sonetSectionIntervalSEFSs,_X:sonetSectionIntervalCVs,_Aa:sonetSectionIntervalValidData,'sonetLine':sonetLine,'sonetLineCurrentTable':sonetLineCurrentTable,'sonetLineCurrentEntry':sonetLineCurrentEntry,_Y:sonetLineCurrentStatus,_Z:sonetLineCurrentESs,_a:sonetLineCurrentSESs,_b:sonetLineCurrentCVs,_c:sonetLineCurrentUASs,'sonetLineIntervalTable':sonetLineIntervalTable,'sonetLineIntervalEntry':sonetLineIntervalEntry,_AR:sonetLineIntervalNumber,_d:sonetLineIntervalESs,_e:sonetLineIntervalSESs,_f:sonetLineIntervalCVs,_g:sonetLineIntervalUASs,_Ab:sonetLineIntervalValidData,'sonetFarEndLine':sonetFarEndLine,'sonetFarEndLineCurrentTable':sonetFarEndLineCurrentTable,'sonetFarEndLineCurrentEntry':sonetFarEndLineCurrentEntry,_h:sonetFarEndLineCurrentESs,_i:sonetFarEndLineCurrentSESs,_j:sonetFarEndLineCurrentCVs,_k:sonetFarEndLineCurrentUASs,'sonetFarEndLineIntervalTable':sonetFarEndLineIntervalTable,'sonetFarEndLineIntervalEntry':sonetFarEndLineIntervalEntry,_AS:sonetFarEndLineIntervalNumber,_l:sonetFarEndLineIntervalESs,_m:sonetFarEndLineIntervalSESs,_n:sonetFarEndLineIntervalCVs,_o:sonetFarEndLineIntervalUASs,_Ae:sonetFarEndLineIntervalValidData,'sonetObjectsPath':sonetObjectsPath,'sonetPath':sonetPath,'sonetPathCurrentTable':sonetPathCurrentTable,'sonetPathCurrentEntry':sonetPathCurrentEntry,_p:sonetPathCurrentWidth,_q:sonetPathCurrentStatus,_r:sonetPathCurrentESs,_s:sonetPathCurrentSESs,_t:sonetPathCurrentCVs,_u:sonetPathCurrentUASs,'sonetPathIntervalTable':sonetPathIntervalTable,'sonetPathIntervalEntry':sonetPathIntervalEntry,_AT:sonetPathIntervalNumber,_v:sonetPathIntervalESs,_w:sonetPathIntervalSESs,_x:sonetPathIntervalCVs,_y:sonetPathIntervalUASs,_Ac:sonetPathIntervalValidData,'sonetFarEndPath':sonetFarEndPath,'sonetFarEndPathCurrentTable':sonetFarEndPathCurrentTable,'sonetFarEndPathCurrentEntry':sonetFarEndPathCurrentEntry,_z:sonetFarEndPathCurrentESs,_A0:sonetFarEndPathCurrentSESs,_A1:sonetFarEndPathCurrentCVs,_A2:sonetFarEndPathCurrentUASs,'sonetFarEndPathIntervalTable':sonetFarEndPathIntervalTable,'sonetFarEndPathIntervalEntry':sonetFarEndPathIntervalEntry,_AU:sonetFarEndPathIntervalNumber,_A3:sonetFarEndPathIntervalESs,_A4:sonetFarEndPathIntervalSESs,_A5:sonetFarEndPathIntervalCVs,_A6:sonetFarEndPathIntervalUASs,_Af:sonetFarEndPathIntervalValidData,'sonetObjectsVT':sonetObjectsVT,'sonetVT':sonetVT,'sonetVTCurrentTable':sonetVTCurrentTable,'sonetVTCurrentEntry':sonetVTCurrentEntry,_A7:sonetVTCurrentWidth,_A8:sonetVTCurrentStatus,_A9:sonetVTCurrentESs,_AA:sonetVTCurrentSESs,_AB:sonetVTCurrentCVs,_AC:sonetVTCurrentUASs,'sonetVTIntervalTable':sonetVTIntervalTable,'sonetVTIntervalEntry':sonetVTIntervalEntry,_AV:sonetVTIntervalNumber,_AD:sonetVTIntervalESs,_AE:sonetVTIntervalSESs,_AF:sonetVTIntervalCVs,_AG:sonetVTIntervalUASs,_Ad:sonetVTIntervalValidData,'sonetFarEndVT':sonetFarEndVT,'sonetFarEndVTCurrentTable':sonetFarEndVTCurrentTable,'sonetFarEndVTCurrentEntry':sonetFarEndVTCurrentEntry,_AH:sonetFarEndVTCurrentESs,_AI:sonetFarEndVTCurrentSESs,_AJ:sonetFarEndVTCurrentCVs,_AK:sonetFarEndVTCurrentUASs,'sonetFarEndVTIntervalTable':sonetFarEndVTIntervalTable,'sonetFarEndVTIntervalEntry':sonetFarEndVTIntervalEntry,_AW:sonetFarEndVTIntervalNumber,_AL:sonetFarEndVTIntervalESs,_AM:sonetFarEndVTIntervalSESs,_AN:sonetFarEndVTIntervalCVs,_AO:sonetFarEndVTIntervalUASs,_Ag:sonetFarEndVTIntervalValidData,'sonetConformance':sonetConformance,'sonetGroups':sonetGroups,_Ah:sonetMediumStuff,_Ai:sonetSectionStuff,_Aj:sonetLineStuff,_Ak:sonetFarEndLineStuff,_Al:sonetPathStuff,_Am:sonetFarEndPathStuff,_An:sonetVTStuff,_Ao:sonetFarEndVTStuff,_Ap:sonetMediumStuff2,_Aq:sonetSectionStuff2,'sonetLineStuff2':sonetLineStuff2,'sonetPathStuff2':sonetPathStuff2,'sonetVTStuff2':sonetVTStuff2,'sonetFarEndLineStuff2':sonetFarEndLineStuff2,'sonetFarEndPathStuff2':sonetFarEndPathStuff2,'sonetFarEndVTStuff2':sonetFarEndVTStuff2,'sonetCompliances':sonetCompliances,'sonetCompliance':sonetCompliance,'sonetCompliance2':sonetCompliance2})