_Ac='acdRegulatorTidGroup'
_Ab='acdRegulatorHistStatsGroup'
_Aa='acdRegulatorStatsGroup'
_AZ='acdRegulatorGroup'
_AY='acdRegulatorTableLastChangeTid'
_AX='acdRegulatorHistStatsRedMaxRate'
_AW='acdRegulatorHistStatsRedMinRate'
_AV='acdRegulatorHistStatsRedAvgRate'
_AU='acdRegulatorHistStatsYellowMaxRate'
_AT='acdRegulatorHistStatsYellowMinRate'
_AS='acdRegulatorHistStatsYellowAvgRate'
_AR='acdRegulatorHistStatsGreenMaxRate'
_AQ='acdRegulatorHistStatsGreenMinRate'
_AP='acdRegulatorHistStatsGreenAvgRate'
_AO='acdRegulatorHistStatsRedHCPkts'
_AN='acdRegulatorHistStatsRedHCOctets'
_AM='acdRegulatorHistStatsYellowHCPkts'
_AL='acdRegulatorHistStatsYellowHCOctets'
_AK='acdRegulatorHistStatsGreenHCPkts'
_AJ='acdRegulatorHistStatsGreenHCOctets'
_AI='acdRegulatorHistStatsDropMaxRate'
_AH='acdRegulatorHistStatsDropMinRate'
_AG='acdRegulatorHistStatsDropAvgRate'
_AF='acdRegulatorHistStatsDropHCPkts'
_AE='acdRegulatorHistStatsDropOverflowPkts'
_AD='acdRegulatorHistStatsDropPkts'
_AC='acdRegulatorHistStatsDropHCOctets'
_AB='acdRegulatorHistStatsDropOverflowOctets'
_AA='acdRegulatorHistStatsDropOctets'
_A9='acdRegulatorHistStatsAcceptMaxRate'
_A8='acdRegulatorHistStatsAcceptMinRate'
_A7='acdRegulatorHistStatsAcceptAvgRate'
_A6='acdRegulatorHistStatsAcceptHCPkts'
_A5='acdRegulatorHistStatsAcceptOverflowPkts'
_A4='acdRegulatorHistStatsAcceptPkts'
_A3='acdRegulatorHistStatsAcceptHCOctets'
_A2='acdRegulatorHistStatsAcceptOverflowOctets'
_A1='acdRegulatorHistStatsAcceptOctets'
_A0='acdRegulatorHistStatsIntervalEnd'
_z='acdRegulatorHistStatsDuration'
_y='acdRegulatorHistStatsStatus'
_x='acdRegulatorStatsRedRate'
_w='acdRegulatorStatsYellowRate'
_v='acdRegulatorStatsGreenRate'
_u='acdRegulatorStatsRedHCPkts'
_t='acdRegulatorStatsRedHCOctets'
_s='acdRegulatorStatsYellowHCPkts'
_r='acdRegulatorStatsYellowHCOctets'
_q='acdRegulatorStatsGreenHCPkts'
_p='acdRegulatorStatsGreenHCOctets'
_o='acdRegulatorStatsDropRate'
_n='acdRegulatorStatsDropHCPkts'
_m='acdRegulatorStatsDropOverflowPkts'
_l='acdRegulatorStatsDropPkts'
_k='acdRegulatorStatsDropHCOctets'
_j='acdRegulatorStatsDropOverflowOctets'
_i='acdRegulatorStatsDropOctets'
_h='acdRegulatorStatsAcceptRate'
_g='acdRegulatorStatsAcceptHCPkts'
_f='acdRegulatorStatsAcceptOverflowPkts'
_e='acdRegulatorStatsAcceptPkts'
_d='acdRegulatorStatsAcceptHCOctets'
_c='acdRegulatorStatsAcceptOverflowOctets'
_b='acdRegulatorStatsAcceptOctets'
_a='acdRegulatorEirMax'
_Z='acdRegulatorCirMax'
_Y='acdRegulatorWorkingRate'
_X='acdRegulatorRowStatus'
_W='acdRegulatorIsCouple'
_V='acdRegulatorIsBlind'
_U='acdRegulatorEbs'
_T='acdRegulatorEir'
_S='acdRegulatorCbs'
_R='acdRegulatorCir'
_Q='acdRegulatorName'
_P='acdRegulatorStatsID'
_O='not-accessible'
_N='acdRegulatorID'
_M='DisplayString'
_L='acdRegulatorHistStatsSampleIndex'
_K='acdRegulatorHistStatsID'
_J='TruthValue'
_I='Integer32'
_H='Unsigned32'
_G='read-create'
_F='Packets'
_E='Octets'
_D='Kbps'
_C='read-only'
_B='ACD-REGULATOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acdMibs,=mibBuilder.importSymbols('ACCEDIAN-SMI','acdMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_M,'PhysAddress','RowStatus','TextualConvention',_J)
acdRegulator=ModuleIdentity((1,3,6,1,4,1,22420,2,6))
if mibBuilder.loadTexts:acdRegulator.setRevisions(('2017-02-21 01:00','2016-09-23 01:00','2016-05-26 01:00','2014-06-09 00:00','2013-12-01 00:00','2012-01-10 01:00','2011-10-10 01:00','2010-11-10 01:00','2008-05-01 01:00','2008-02-06 01:00','2007-03-28 01:00'))
_AcdRegulatorTable_Object=MibTable
acdRegulatorTable=_AcdRegulatorTable_Object((1,3,6,1,4,1,22420,2,6,1))
if mibBuilder.loadTexts:acdRegulatorTable.setStatus(_A)
_AcdRegulatorEntry_Object=MibTableRow
acdRegulatorEntry=_AcdRegulatorEntry_Object((1,3,6,1,4,1,22420,2,6,1,1))
acdRegulatorEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:acdRegulatorEntry.setStatus(_A)
_AcdRegulatorID_Type=Unsigned32
_AcdRegulatorID_Object=MibTableColumn
acdRegulatorID=_AcdRegulatorID_Object((1,3,6,1,4,1,22420,2,6,1,1,1),_AcdRegulatorID_Type())
acdRegulatorID.setMaxAccess(_O)
if mibBuilder.loadTexts:acdRegulatorID.setStatus(_A)
class _AcdRegulatorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AcdRegulatorName_Type.__name__=_M
_AcdRegulatorName_Object=MibTableColumn
acdRegulatorName=_AcdRegulatorName_Object((1,3,6,1,4,1,22420,2,6,1,1,2),_AcdRegulatorName_Type())
acdRegulatorName.setMaxAccess(_G)
if mibBuilder.loadTexts:acdRegulatorName.setStatus(_A)
class _AcdRegulatorCir_Type(Unsigned32):defaultValue=20000
_AcdRegulatorCir_Type.__name__=_H
_AcdRegulatorCir_Object=MibTableColumn
acdRegulatorCir=_AcdRegulatorCir_Object((1,3,6,1,4,1,22420,2,6,1,1,3),_AcdRegulatorCir_Type())
acdRegulatorCir.setMaxAccess(_G)
if mibBuilder.loadTexts:acdRegulatorCir.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorCir.setUnits(_D)
class _AcdRegulatorCbs_Type(Unsigned32):defaultValue=8
_AcdRegulatorCbs_Type.__name__=_H
_AcdRegulatorCbs_Object=MibTableColumn
acdRegulatorCbs=_AcdRegulatorCbs_Object((1,3,6,1,4,1,22420,2,6,1,1,4),_AcdRegulatorCbs_Type())
acdRegulatorCbs.setMaxAccess(_G)
if mibBuilder.loadTexts:acdRegulatorCbs.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorCbs.setUnits('KiB')
class _AcdRegulatorEir_Type(Unsigned32):defaultValue=1000
_AcdRegulatorEir_Type.__name__=_H
_AcdRegulatorEir_Object=MibTableColumn
acdRegulatorEir=_AcdRegulatorEir_Object((1,3,6,1,4,1,22420,2,6,1,1,5),_AcdRegulatorEir_Type())
acdRegulatorEir.setMaxAccess(_G)
if mibBuilder.loadTexts:acdRegulatorEir.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorEir.setUnits(_D)
class _AcdRegulatorEbs_Type(Unsigned32):defaultValue=8
_AcdRegulatorEbs_Type.__name__=_H
_AcdRegulatorEbs_Object=MibTableColumn
acdRegulatorEbs=_AcdRegulatorEbs_Object((1,3,6,1,4,1,22420,2,6,1,1,6),_AcdRegulatorEbs_Type())
acdRegulatorEbs.setMaxAccess(_G)
if mibBuilder.loadTexts:acdRegulatorEbs.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorEbs.setUnits('KiB')
class _AcdRegulatorIsBlind_Type(TruthValue):defaultValue=2
_AcdRegulatorIsBlind_Type.__name__=_J
_AcdRegulatorIsBlind_Object=MibTableColumn
acdRegulatorIsBlind=_AcdRegulatorIsBlind_Object((1,3,6,1,4,1,22420,2,6,1,1,7),_AcdRegulatorIsBlind_Type())
acdRegulatorIsBlind.setMaxAccess(_G)
if mibBuilder.loadTexts:acdRegulatorIsBlind.setStatus(_A)
class _AcdRegulatorIsCouple_Type(TruthValue):defaultValue=2
_AcdRegulatorIsCouple_Type.__name__=_J
_AcdRegulatorIsCouple_Object=MibTableColumn
acdRegulatorIsCouple=_AcdRegulatorIsCouple_Object((1,3,6,1,4,1,22420,2,6,1,1,8),_AcdRegulatorIsCouple_Type())
acdRegulatorIsCouple.setMaxAccess(_G)
if mibBuilder.loadTexts:acdRegulatorIsCouple.setStatus(_A)
_AcdRegulatorRowStatus_Type=RowStatus
_AcdRegulatorRowStatus_Object=MibTableColumn
acdRegulatorRowStatus=_AcdRegulatorRowStatus_Object((1,3,6,1,4,1,22420,2,6,1,1,9),_AcdRegulatorRowStatus_Type())
acdRegulatorRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:acdRegulatorRowStatus.setStatus(_A)
class _AcdRegulatorWorkingRate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('layer1',1),('layer2',2)))
_AcdRegulatorWorkingRate_Type.__name__=_I
_AcdRegulatorWorkingRate_Object=MibTableColumn
acdRegulatorWorkingRate=_AcdRegulatorWorkingRate_Object((1,3,6,1,4,1,22420,2,6,1,1,10),_AcdRegulatorWorkingRate_Type())
acdRegulatorWorkingRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorWorkingRate.setStatus(_A)
class _AcdRegulatorCirMax_Type(Unsigned32):defaultValue=20000
_AcdRegulatorCirMax_Type.__name__=_H
_AcdRegulatorCirMax_Object=MibTableColumn
acdRegulatorCirMax=_AcdRegulatorCirMax_Object((1,3,6,1,4,1,22420,2,6,1,1,11),_AcdRegulatorCirMax_Type())
acdRegulatorCirMax.setMaxAccess(_G)
if mibBuilder.loadTexts:acdRegulatorCirMax.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorCirMax.setUnits(_D)
class _AcdRegulatorEirMax_Type(Unsigned32):defaultValue=1000
_AcdRegulatorEirMax_Type.__name__=_H
_AcdRegulatorEirMax_Object=MibTableColumn
acdRegulatorEirMax=_AcdRegulatorEirMax_Object((1,3,6,1,4,1,22420,2,6,1,1,12),_AcdRegulatorEirMax_Type())
acdRegulatorEirMax.setMaxAccess(_G)
if mibBuilder.loadTexts:acdRegulatorEirMax.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorEirMax.setUnits(_D)
_AcdRegulatorStatsTable_Object=MibTable
acdRegulatorStatsTable=_AcdRegulatorStatsTable_Object((1,3,6,1,4,1,22420,2,6,2))
if mibBuilder.loadTexts:acdRegulatorStatsTable.setStatus(_A)
_AcdRegulatorStatsEntry_Object=MibTableRow
acdRegulatorStatsEntry=_AcdRegulatorStatsEntry_Object((1,3,6,1,4,1,22420,2,6,2,1))
acdRegulatorStatsEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:acdRegulatorStatsEntry.setStatus(_A)
_AcdRegulatorStatsID_Type=Unsigned32
_AcdRegulatorStatsID_Object=MibTableColumn
acdRegulatorStatsID=_AcdRegulatorStatsID_Object((1,3,6,1,4,1,22420,2,6,2,1,1),_AcdRegulatorStatsID_Type())
acdRegulatorStatsID.setMaxAccess(_O)
if mibBuilder.loadTexts:acdRegulatorStatsID.setStatus(_A)
_AcdRegulatorStatsAcceptOctets_Type=Counter32
_AcdRegulatorStatsAcceptOctets_Object=MibTableColumn
acdRegulatorStatsAcceptOctets=_AcdRegulatorStatsAcceptOctets_Object((1,3,6,1,4,1,22420,2,6,2,1,2),_AcdRegulatorStatsAcceptOctets_Type())
acdRegulatorStatsAcceptOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsAcceptOctets.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsAcceptOctets.setUnits(_E)
_AcdRegulatorStatsAcceptOverflowOctets_Type=Counter32
_AcdRegulatorStatsAcceptOverflowOctets_Object=MibTableColumn
acdRegulatorStatsAcceptOverflowOctets=_AcdRegulatorStatsAcceptOverflowOctets_Object((1,3,6,1,4,1,22420,2,6,2,1,3),_AcdRegulatorStatsAcceptOverflowOctets_Type())
acdRegulatorStatsAcceptOverflowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsAcceptOverflowOctets.setStatus(_A)
_AcdRegulatorStatsAcceptHCOctets_Type=Counter64
_AcdRegulatorStatsAcceptHCOctets_Object=MibTableColumn
acdRegulatorStatsAcceptHCOctets=_AcdRegulatorStatsAcceptHCOctets_Object((1,3,6,1,4,1,22420,2,6,2,1,4),_AcdRegulatorStatsAcceptHCOctets_Type())
acdRegulatorStatsAcceptHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsAcceptHCOctets.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsAcceptHCOctets.setUnits(_E)
_AcdRegulatorStatsAcceptPkts_Type=Counter32
_AcdRegulatorStatsAcceptPkts_Object=MibTableColumn
acdRegulatorStatsAcceptPkts=_AcdRegulatorStatsAcceptPkts_Object((1,3,6,1,4,1,22420,2,6,2,1,5),_AcdRegulatorStatsAcceptPkts_Type())
acdRegulatorStatsAcceptPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsAcceptPkts.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsAcceptPkts.setUnits(_F)
_AcdRegulatorStatsAcceptOverflowPkts_Type=Counter32
_AcdRegulatorStatsAcceptOverflowPkts_Object=MibTableColumn
acdRegulatorStatsAcceptOverflowPkts=_AcdRegulatorStatsAcceptOverflowPkts_Object((1,3,6,1,4,1,22420,2,6,2,1,6),_AcdRegulatorStatsAcceptOverflowPkts_Type())
acdRegulatorStatsAcceptOverflowPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsAcceptOverflowPkts.setStatus(_A)
_AcdRegulatorStatsAcceptHCPkts_Type=Counter64
_AcdRegulatorStatsAcceptHCPkts_Object=MibTableColumn
acdRegulatorStatsAcceptHCPkts=_AcdRegulatorStatsAcceptHCPkts_Object((1,3,6,1,4,1,22420,2,6,2,1,7),_AcdRegulatorStatsAcceptHCPkts_Type())
acdRegulatorStatsAcceptHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsAcceptHCPkts.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsAcceptHCPkts.setUnits(_F)
_AcdRegulatorStatsAcceptRate_Type=Gauge32
_AcdRegulatorStatsAcceptRate_Object=MibTableColumn
acdRegulatorStatsAcceptRate=_AcdRegulatorStatsAcceptRate_Object((1,3,6,1,4,1,22420,2,6,2,1,8),_AcdRegulatorStatsAcceptRate_Type())
acdRegulatorStatsAcceptRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsAcceptRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsAcceptRate.setUnits(_D)
_AcdRegulatorStatsDropOctets_Type=Counter32
_AcdRegulatorStatsDropOctets_Object=MibTableColumn
acdRegulatorStatsDropOctets=_AcdRegulatorStatsDropOctets_Object((1,3,6,1,4,1,22420,2,6,2,1,9),_AcdRegulatorStatsDropOctets_Type())
acdRegulatorStatsDropOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsDropOctets.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsDropOctets.setUnits(_E)
_AcdRegulatorStatsDropOverflowOctets_Type=Counter32
_AcdRegulatorStatsDropOverflowOctets_Object=MibTableColumn
acdRegulatorStatsDropOverflowOctets=_AcdRegulatorStatsDropOverflowOctets_Object((1,3,6,1,4,1,22420,2,6,2,1,10),_AcdRegulatorStatsDropOverflowOctets_Type())
acdRegulatorStatsDropOverflowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsDropOverflowOctets.setStatus(_A)
_AcdRegulatorStatsDropHCOctets_Type=Counter64
_AcdRegulatorStatsDropHCOctets_Object=MibTableColumn
acdRegulatorStatsDropHCOctets=_AcdRegulatorStatsDropHCOctets_Object((1,3,6,1,4,1,22420,2,6,2,1,11),_AcdRegulatorStatsDropHCOctets_Type())
acdRegulatorStatsDropHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsDropHCOctets.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsDropHCOctets.setUnits(_E)
_AcdRegulatorStatsDropPkts_Type=Counter32
_AcdRegulatorStatsDropPkts_Object=MibTableColumn
acdRegulatorStatsDropPkts=_AcdRegulatorStatsDropPkts_Object((1,3,6,1,4,1,22420,2,6,2,1,12),_AcdRegulatorStatsDropPkts_Type())
acdRegulatorStatsDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsDropPkts.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsDropPkts.setUnits(_F)
_AcdRegulatorStatsDropOverflowPkts_Type=Counter32
_AcdRegulatorStatsDropOverflowPkts_Object=MibTableColumn
acdRegulatorStatsDropOverflowPkts=_AcdRegulatorStatsDropOverflowPkts_Object((1,3,6,1,4,1,22420,2,6,2,1,13),_AcdRegulatorStatsDropOverflowPkts_Type())
acdRegulatorStatsDropOverflowPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsDropOverflowPkts.setStatus(_A)
_AcdRegulatorStatsDropHCPkts_Type=Counter64
_AcdRegulatorStatsDropHCPkts_Object=MibTableColumn
acdRegulatorStatsDropHCPkts=_AcdRegulatorStatsDropHCPkts_Object((1,3,6,1,4,1,22420,2,6,2,1,14),_AcdRegulatorStatsDropHCPkts_Type())
acdRegulatorStatsDropHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsDropHCPkts.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsDropHCPkts.setUnits(_F)
_AcdRegulatorStatsDropRate_Type=Gauge32
_AcdRegulatorStatsDropRate_Object=MibTableColumn
acdRegulatorStatsDropRate=_AcdRegulatorStatsDropRate_Object((1,3,6,1,4,1,22420,2,6,2,1,15),_AcdRegulatorStatsDropRate_Type())
acdRegulatorStatsDropRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsDropRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsDropRate.setUnits(_D)
_AcdRegulatorStatsGreenHCOctets_Type=Counter64
_AcdRegulatorStatsGreenHCOctets_Object=MibTableColumn
acdRegulatorStatsGreenHCOctets=_AcdRegulatorStatsGreenHCOctets_Object((1,3,6,1,4,1,22420,2,6,2,1,16),_AcdRegulatorStatsGreenHCOctets_Type())
acdRegulatorStatsGreenHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsGreenHCOctets.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsGreenHCOctets.setUnits(_E)
_AcdRegulatorStatsGreenHCPkts_Type=Counter64
_AcdRegulatorStatsGreenHCPkts_Object=MibTableColumn
acdRegulatorStatsGreenHCPkts=_AcdRegulatorStatsGreenHCPkts_Object((1,3,6,1,4,1,22420,2,6,2,1,17),_AcdRegulatorStatsGreenHCPkts_Type())
acdRegulatorStatsGreenHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsGreenHCPkts.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsGreenHCPkts.setUnits(_F)
_AcdRegulatorStatsYellowHCOctets_Type=Counter64
_AcdRegulatorStatsYellowHCOctets_Object=MibTableColumn
acdRegulatorStatsYellowHCOctets=_AcdRegulatorStatsYellowHCOctets_Object((1,3,6,1,4,1,22420,2,6,2,1,18),_AcdRegulatorStatsYellowHCOctets_Type())
acdRegulatorStatsYellowHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsYellowHCOctets.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsYellowHCOctets.setUnits(_E)
_AcdRegulatorStatsYellowHCPkts_Type=Counter64
_AcdRegulatorStatsYellowHCPkts_Object=MibTableColumn
acdRegulatorStatsYellowHCPkts=_AcdRegulatorStatsYellowHCPkts_Object((1,3,6,1,4,1,22420,2,6,2,1,19),_AcdRegulatorStatsYellowHCPkts_Type())
acdRegulatorStatsYellowHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsYellowHCPkts.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsYellowHCPkts.setUnits(_F)
_AcdRegulatorStatsRedHCOctets_Type=Counter64
_AcdRegulatorStatsRedHCOctets_Object=MibTableColumn
acdRegulatorStatsRedHCOctets=_AcdRegulatorStatsRedHCOctets_Object((1,3,6,1,4,1,22420,2,6,2,1,20),_AcdRegulatorStatsRedHCOctets_Type())
acdRegulatorStatsRedHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsRedHCOctets.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsRedHCOctets.setUnits(_E)
_AcdRegulatorStatsRedHCPkts_Type=Counter64
_AcdRegulatorStatsRedHCPkts_Object=MibTableColumn
acdRegulatorStatsRedHCPkts=_AcdRegulatorStatsRedHCPkts_Object((1,3,6,1,4,1,22420,2,6,2,1,21),_AcdRegulatorStatsRedHCPkts_Type())
acdRegulatorStatsRedHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsRedHCPkts.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsRedHCPkts.setUnits(_F)
_AcdRegulatorStatsGreenRate_Type=Gauge32
_AcdRegulatorStatsGreenRate_Object=MibTableColumn
acdRegulatorStatsGreenRate=_AcdRegulatorStatsGreenRate_Object((1,3,6,1,4,1,22420,2,6,2,1,22),_AcdRegulatorStatsGreenRate_Type())
acdRegulatorStatsGreenRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsGreenRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsGreenRate.setUnits(_D)
_AcdRegulatorStatsYellowRate_Type=Gauge32
_AcdRegulatorStatsYellowRate_Object=MibTableColumn
acdRegulatorStatsYellowRate=_AcdRegulatorStatsYellowRate_Object((1,3,6,1,4,1,22420,2,6,2,1,23),_AcdRegulatorStatsYellowRate_Type())
acdRegulatorStatsYellowRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsYellowRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsYellowRate.setUnits(_D)
_AcdRegulatorStatsRedRate_Type=Gauge32
_AcdRegulatorStatsRedRate_Object=MibTableColumn
acdRegulatorStatsRedRate=_AcdRegulatorStatsRedRate_Object((1,3,6,1,4,1,22420,2,6,2,1,24),_AcdRegulatorStatsRedRate_Type())
acdRegulatorStatsRedRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorStatsRedRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorStatsRedRate.setUnits(_D)
_AcdRegulatorHistStatsTable_Object=MibTable
acdRegulatorHistStatsTable=_AcdRegulatorHistStatsTable_Object((1,3,6,1,4,1,22420,2,6,3))
if mibBuilder.loadTexts:acdRegulatorHistStatsTable.setStatus(_A)
_AcdRegulatorHistStatsEntry_Object=MibTableRow
acdRegulatorHistStatsEntry=_AcdRegulatorHistStatsEntry_Object((1,3,6,1,4,1,22420,2,6,3,1))
acdRegulatorHistStatsEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:acdRegulatorHistStatsEntry.setStatus(_A)
_AcdRegulatorHistStatsID_Type=Unsigned32
_AcdRegulatorHistStatsID_Object=MibTableColumn
acdRegulatorHistStatsID=_AcdRegulatorHistStatsID_Object((1,3,6,1,4,1,22420,2,6,3,1,1),_AcdRegulatorHistStatsID_Type())
acdRegulatorHistStatsID.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsID.setStatus(_A)
_AcdRegulatorHistStatsSampleIndex_Type=Unsigned32
_AcdRegulatorHistStatsSampleIndex_Object=MibTableColumn
acdRegulatorHistStatsSampleIndex=_AcdRegulatorHistStatsSampleIndex_Object((1,3,6,1,4,1,22420,2,6,3,1,2),_AcdRegulatorHistStatsSampleIndex_Type())
acdRegulatorHistStatsSampleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsSampleIndex.setStatus(_A)
class _AcdRegulatorHistStatsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_AcdRegulatorHistStatsStatus_Type.__name__=_I
_AcdRegulatorHistStatsStatus_Object=MibTableColumn
acdRegulatorHistStatsStatus=_AcdRegulatorHistStatsStatus_Object((1,3,6,1,4,1,22420,2,6,3,1,3),_AcdRegulatorHistStatsStatus_Type())
acdRegulatorHistStatsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsStatus.setStatus(_A)
_AcdRegulatorHistStatsDuration_Type=Unsigned32
_AcdRegulatorHistStatsDuration_Object=MibTableColumn
acdRegulatorHistStatsDuration=_AcdRegulatorHistStatsDuration_Object((1,3,6,1,4,1,22420,2,6,3,1,4),_AcdRegulatorHistStatsDuration_Type())
acdRegulatorHistStatsDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsDuration.setStatus(_A)
_AcdRegulatorHistStatsIntervalEnd_Type=DateAndTime
_AcdRegulatorHistStatsIntervalEnd_Object=MibTableColumn
acdRegulatorHistStatsIntervalEnd=_AcdRegulatorHistStatsIntervalEnd_Object((1,3,6,1,4,1,22420,2,6,3,1,5),_AcdRegulatorHistStatsIntervalEnd_Type())
acdRegulatorHistStatsIntervalEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsIntervalEnd.setStatus(_A)
_AcdRegulatorHistStatsAcceptOctets_Type=Counter32
_AcdRegulatorHistStatsAcceptOctets_Object=MibTableColumn
acdRegulatorHistStatsAcceptOctets=_AcdRegulatorHistStatsAcceptOctets_Object((1,3,6,1,4,1,22420,2,6,3,1,6),_AcdRegulatorHistStatsAcceptOctets_Type())
acdRegulatorHistStatsAcceptOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsAcceptOctets.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsAcceptOctets.setUnits(_E)
_AcdRegulatorHistStatsAcceptOverflowOctets_Type=Counter32
_AcdRegulatorHistStatsAcceptOverflowOctets_Object=MibTableColumn
acdRegulatorHistStatsAcceptOverflowOctets=_AcdRegulatorHistStatsAcceptOverflowOctets_Object((1,3,6,1,4,1,22420,2,6,3,1,7),_AcdRegulatorHistStatsAcceptOverflowOctets_Type())
acdRegulatorHistStatsAcceptOverflowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsAcceptOverflowOctets.setStatus(_A)
_AcdRegulatorHistStatsAcceptHCOctets_Type=Counter64
_AcdRegulatorHistStatsAcceptHCOctets_Object=MibTableColumn
acdRegulatorHistStatsAcceptHCOctets=_AcdRegulatorHistStatsAcceptHCOctets_Object((1,3,6,1,4,1,22420,2,6,3,1,8),_AcdRegulatorHistStatsAcceptHCOctets_Type())
acdRegulatorHistStatsAcceptHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsAcceptHCOctets.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsAcceptHCOctets.setUnits(_E)
_AcdRegulatorHistStatsAcceptPkts_Type=Counter32
_AcdRegulatorHistStatsAcceptPkts_Object=MibTableColumn
acdRegulatorHistStatsAcceptPkts=_AcdRegulatorHistStatsAcceptPkts_Object((1,3,6,1,4,1,22420,2,6,3,1,9),_AcdRegulatorHistStatsAcceptPkts_Type())
acdRegulatorHistStatsAcceptPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsAcceptPkts.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsAcceptPkts.setUnits(_F)
_AcdRegulatorHistStatsAcceptOverflowPkts_Type=Counter32
_AcdRegulatorHistStatsAcceptOverflowPkts_Object=MibTableColumn
acdRegulatorHistStatsAcceptOverflowPkts=_AcdRegulatorHistStatsAcceptOverflowPkts_Object((1,3,6,1,4,1,22420,2,6,3,1,10),_AcdRegulatorHistStatsAcceptOverflowPkts_Type())
acdRegulatorHistStatsAcceptOverflowPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsAcceptOverflowPkts.setStatus(_A)
_AcdRegulatorHistStatsAcceptHCPkts_Type=Counter64
_AcdRegulatorHistStatsAcceptHCPkts_Object=MibTableColumn
acdRegulatorHistStatsAcceptHCPkts=_AcdRegulatorHistStatsAcceptHCPkts_Object((1,3,6,1,4,1,22420,2,6,3,1,11),_AcdRegulatorHistStatsAcceptHCPkts_Type())
acdRegulatorHistStatsAcceptHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsAcceptHCPkts.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsAcceptHCPkts.setUnits(_F)
_AcdRegulatorHistStatsAcceptAvgRate_Type=Gauge32
_AcdRegulatorHistStatsAcceptAvgRate_Object=MibTableColumn
acdRegulatorHistStatsAcceptAvgRate=_AcdRegulatorHistStatsAcceptAvgRate_Object((1,3,6,1,4,1,22420,2,6,3,1,12),_AcdRegulatorHistStatsAcceptAvgRate_Type())
acdRegulatorHistStatsAcceptAvgRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsAcceptAvgRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsAcceptAvgRate.setUnits(_D)
_AcdRegulatorHistStatsAcceptMinRate_Type=Gauge32
_AcdRegulatorHistStatsAcceptMinRate_Object=MibTableColumn
acdRegulatorHistStatsAcceptMinRate=_AcdRegulatorHistStatsAcceptMinRate_Object((1,3,6,1,4,1,22420,2,6,3,1,13),_AcdRegulatorHistStatsAcceptMinRate_Type())
acdRegulatorHistStatsAcceptMinRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsAcceptMinRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsAcceptMinRate.setUnits(_D)
_AcdRegulatorHistStatsAcceptMaxRate_Type=Gauge32
_AcdRegulatorHistStatsAcceptMaxRate_Object=MibTableColumn
acdRegulatorHistStatsAcceptMaxRate=_AcdRegulatorHistStatsAcceptMaxRate_Object((1,3,6,1,4,1,22420,2,6,3,1,14),_AcdRegulatorHistStatsAcceptMaxRate_Type())
acdRegulatorHistStatsAcceptMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsAcceptMaxRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsAcceptMaxRate.setUnits(_D)
_AcdRegulatorHistStatsDropOctets_Type=Counter32
_AcdRegulatorHistStatsDropOctets_Object=MibTableColumn
acdRegulatorHistStatsDropOctets=_AcdRegulatorHistStatsDropOctets_Object((1,3,6,1,4,1,22420,2,6,3,1,15),_AcdRegulatorHistStatsDropOctets_Type())
acdRegulatorHistStatsDropOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsDropOctets.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsDropOctets.setUnits(_E)
_AcdRegulatorHistStatsDropOverflowOctets_Type=Counter32
_AcdRegulatorHistStatsDropOverflowOctets_Object=MibTableColumn
acdRegulatorHistStatsDropOverflowOctets=_AcdRegulatorHistStatsDropOverflowOctets_Object((1,3,6,1,4,1,22420,2,6,3,1,16),_AcdRegulatorHistStatsDropOverflowOctets_Type())
acdRegulatorHistStatsDropOverflowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsDropOverflowOctets.setStatus(_A)
_AcdRegulatorHistStatsDropHCOctets_Type=Counter64
_AcdRegulatorHistStatsDropHCOctets_Object=MibTableColumn
acdRegulatorHistStatsDropHCOctets=_AcdRegulatorHistStatsDropHCOctets_Object((1,3,6,1,4,1,22420,2,6,3,1,17),_AcdRegulatorHistStatsDropHCOctets_Type())
acdRegulatorHistStatsDropHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsDropHCOctets.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsDropHCOctets.setUnits(_E)
_AcdRegulatorHistStatsDropPkts_Type=Counter32
_AcdRegulatorHistStatsDropPkts_Object=MibTableColumn
acdRegulatorHistStatsDropPkts=_AcdRegulatorHistStatsDropPkts_Object((1,3,6,1,4,1,22420,2,6,3,1,18),_AcdRegulatorHistStatsDropPkts_Type())
acdRegulatorHistStatsDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsDropPkts.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsDropPkts.setUnits(_F)
_AcdRegulatorHistStatsDropOverflowPkts_Type=Counter32
_AcdRegulatorHistStatsDropOverflowPkts_Object=MibTableColumn
acdRegulatorHistStatsDropOverflowPkts=_AcdRegulatorHistStatsDropOverflowPkts_Object((1,3,6,1,4,1,22420,2,6,3,1,19),_AcdRegulatorHistStatsDropOverflowPkts_Type())
acdRegulatorHistStatsDropOverflowPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsDropOverflowPkts.setStatus(_A)
_AcdRegulatorHistStatsDropHCPkts_Type=Counter64
_AcdRegulatorHistStatsDropHCPkts_Object=MibTableColumn
acdRegulatorHistStatsDropHCPkts=_AcdRegulatorHistStatsDropHCPkts_Object((1,3,6,1,4,1,22420,2,6,3,1,20),_AcdRegulatorHistStatsDropHCPkts_Type())
acdRegulatorHistStatsDropHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsDropHCPkts.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsDropHCPkts.setUnits(_F)
_AcdRegulatorHistStatsDropAvgRate_Type=Gauge32
_AcdRegulatorHistStatsDropAvgRate_Object=MibTableColumn
acdRegulatorHistStatsDropAvgRate=_AcdRegulatorHistStatsDropAvgRate_Object((1,3,6,1,4,1,22420,2,6,3,1,21),_AcdRegulatorHistStatsDropAvgRate_Type())
acdRegulatorHistStatsDropAvgRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsDropAvgRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsDropAvgRate.setUnits(_D)
_AcdRegulatorHistStatsDropMinRate_Type=Gauge32
_AcdRegulatorHistStatsDropMinRate_Object=MibTableColumn
acdRegulatorHistStatsDropMinRate=_AcdRegulatorHistStatsDropMinRate_Object((1,3,6,1,4,1,22420,2,6,3,1,22),_AcdRegulatorHistStatsDropMinRate_Type())
acdRegulatorHistStatsDropMinRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsDropMinRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsDropMinRate.setUnits(_D)
_AcdRegulatorHistStatsDropMaxRate_Type=Gauge32
_AcdRegulatorHistStatsDropMaxRate_Object=MibTableColumn
acdRegulatorHistStatsDropMaxRate=_AcdRegulatorHistStatsDropMaxRate_Object((1,3,6,1,4,1,22420,2,6,3,1,23),_AcdRegulatorHistStatsDropMaxRate_Type())
acdRegulatorHistStatsDropMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsDropMaxRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsDropMaxRate.setUnits(_D)
_AcdRegulatorHistStatsGreenHCOctets_Type=Counter64
_AcdRegulatorHistStatsGreenHCOctets_Object=MibTableColumn
acdRegulatorHistStatsGreenHCOctets=_AcdRegulatorHistStatsGreenHCOctets_Object((1,3,6,1,4,1,22420,2,6,3,1,24),_AcdRegulatorHistStatsGreenHCOctets_Type())
acdRegulatorHistStatsGreenHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsGreenHCOctets.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsGreenHCOctets.setUnits(_E)
_AcdRegulatorHistStatsGreenHCPkts_Type=Counter64
_AcdRegulatorHistStatsGreenHCPkts_Object=MibTableColumn
acdRegulatorHistStatsGreenHCPkts=_AcdRegulatorHistStatsGreenHCPkts_Object((1,3,6,1,4,1,22420,2,6,3,1,25),_AcdRegulatorHistStatsGreenHCPkts_Type())
acdRegulatorHistStatsGreenHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsGreenHCPkts.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsGreenHCPkts.setUnits(_F)
_AcdRegulatorHistStatsYellowHCOctets_Type=Counter64
_AcdRegulatorHistStatsYellowHCOctets_Object=MibTableColumn
acdRegulatorHistStatsYellowHCOctets=_AcdRegulatorHistStatsYellowHCOctets_Object((1,3,6,1,4,1,22420,2,6,3,1,26),_AcdRegulatorHistStatsYellowHCOctets_Type())
acdRegulatorHistStatsYellowHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsYellowHCOctets.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsYellowHCOctets.setUnits(_E)
_AcdRegulatorHistStatsYellowHCPkts_Type=Counter64
_AcdRegulatorHistStatsYellowHCPkts_Object=MibTableColumn
acdRegulatorHistStatsYellowHCPkts=_AcdRegulatorHistStatsYellowHCPkts_Object((1,3,6,1,4,1,22420,2,6,3,1,27),_AcdRegulatorHistStatsYellowHCPkts_Type())
acdRegulatorHistStatsYellowHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsYellowHCPkts.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsYellowHCPkts.setUnits(_F)
_AcdRegulatorHistStatsRedHCOctets_Type=Counter64
_AcdRegulatorHistStatsRedHCOctets_Object=MibTableColumn
acdRegulatorHistStatsRedHCOctets=_AcdRegulatorHistStatsRedHCOctets_Object((1,3,6,1,4,1,22420,2,6,3,1,28),_AcdRegulatorHistStatsRedHCOctets_Type())
acdRegulatorHistStatsRedHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsRedHCOctets.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsRedHCOctets.setUnits(_E)
_AcdRegulatorHistStatsRedHCPkts_Type=Counter64
_AcdRegulatorHistStatsRedHCPkts_Object=MibTableColumn
acdRegulatorHistStatsRedHCPkts=_AcdRegulatorHistStatsRedHCPkts_Object((1,3,6,1,4,1,22420,2,6,3,1,29),_AcdRegulatorHistStatsRedHCPkts_Type())
acdRegulatorHistStatsRedHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsRedHCPkts.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsRedHCPkts.setUnits(_F)
_AcdRegulatorHistStatsGreenAvgRate_Type=Gauge32
_AcdRegulatorHistStatsGreenAvgRate_Object=MibTableColumn
acdRegulatorHistStatsGreenAvgRate=_AcdRegulatorHistStatsGreenAvgRate_Object((1,3,6,1,4,1,22420,2,6,3,1,30),_AcdRegulatorHistStatsGreenAvgRate_Type())
acdRegulatorHistStatsGreenAvgRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsGreenAvgRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsGreenAvgRate.setUnits(_D)
_AcdRegulatorHistStatsGreenMinRate_Type=Gauge32
_AcdRegulatorHistStatsGreenMinRate_Object=MibTableColumn
acdRegulatorHistStatsGreenMinRate=_AcdRegulatorHistStatsGreenMinRate_Object((1,3,6,1,4,1,22420,2,6,3,1,31),_AcdRegulatorHistStatsGreenMinRate_Type())
acdRegulatorHistStatsGreenMinRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsGreenMinRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsGreenMinRate.setUnits(_D)
_AcdRegulatorHistStatsGreenMaxRate_Type=Gauge32
_AcdRegulatorHistStatsGreenMaxRate_Object=MibTableColumn
acdRegulatorHistStatsGreenMaxRate=_AcdRegulatorHistStatsGreenMaxRate_Object((1,3,6,1,4,1,22420,2,6,3,1,32),_AcdRegulatorHistStatsGreenMaxRate_Type())
acdRegulatorHistStatsGreenMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsGreenMaxRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsGreenMaxRate.setUnits(_D)
_AcdRegulatorHistStatsYellowAvgRate_Type=Gauge32
_AcdRegulatorHistStatsYellowAvgRate_Object=MibTableColumn
acdRegulatorHistStatsYellowAvgRate=_AcdRegulatorHistStatsYellowAvgRate_Object((1,3,6,1,4,1,22420,2,6,3,1,33),_AcdRegulatorHistStatsYellowAvgRate_Type())
acdRegulatorHistStatsYellowAvgRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsYellowAvgRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsYellowAvgRate.setUnits(_D)
_AcdRegulatorHistStatsYellowMinRate_Type=Gauge32
_AcdRegulatorHistStatsYellowMinRate_Object=MibTableColumn
acdRegulatorHistStatsYellowMinRate=_AcdRegulatorHistStatsYellowMinRate_Object((1,3,6,1,4,1,22420,2,6,3,1,34),_AcdRegulatorHistStatsYellowMinRate_Type())
acdRegulatorHistStatsYellowMinRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsYellowMinRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsYellowMinRate.setUnits(_D)
_AcdRegulatorHistStatsYellowMaxRate_Type=Gauge32
_AcdRegulatorHistStatsYellowMaxRate_Object=MibTableColumn
acdRegulatorHistStatsYellowMaxRate=_AcdRegulatorHistStatsYellowMaxRate_Object((1,3,6,1,4,1,22420,2,6,3,1,35),_AcdRegulatorHistStatsYellowMaxRate_Type())
acdRegulatorHistStatsYellowMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsYellowMaxRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsYellowMaxRate.setUnits(_D)
_AcdRegulatorHistStatsRedAvgRate_Type=Gauge32
_AcdRegulatorHistStatsRedAvgRate_Object=MibTableColumn
acdRegulatorHistStatsRedAvgRate=_AcdRegulatorHistStatsRedAvgRate_Object((1,3,6,1,4,1,22420,2,6,3,1,36),_AcdRegulatorHistStatsRedAvgRate_Type())
acdRegulatorHistStatsRedAvgRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsRedAvgRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsRedAvgRate.setUnits(_D)
_AcdRegulatorHistStatsRedMinRate_Type=Gauge32
_AcdRegulatorHistStatsRedMinRate_Object=MibTableColumn
acdRegulatorHistStatsRedMinRate=_AcdRegulatorHistStatsRedMinRate_Object((1,3,6,1,4,1,22420,2,6,3,1,37),_AcdRegulatorHistStatsRedMinRate_Type())
acdRegulatorHistStatsRedMinRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsRedMinRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsRedMinRate.setUnits(_D)
_AcdRegulatorHistStatsRedMaxRate_Type=Gauge32
_AcdRegulatorHistStatsRedMaxRate_Object=MibTableColumn
acdRegulatorHistStatsRedMaxRate=_AcdRegulatorHistStatsRedMaxRate_Object((1,3,6,1,4,1,22420,2,6,3,1,38),_AcdRegulatorHistStatsRedMaxRate_Type())
acdRegulatorHistStatsRedMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorHistStatsRedMaxRate.setStatus(_A)
if mibBuilder.loadTexts:acdRegulatorHistStatsRedMaxRate.setUnits(_D)
_AcdRegulatorNotifications_ObjectIdentity=ObjectIdentity
acdRegulatorNotifications=_AcdRegulatorNotifications_ObjectIdentity((1,3,6,1,4,1,22420,2,6,4))
_AcdRegulatorMIBObjects_ObjectIdentity=ObjectIdentity
acdRegulatorMIBObjects=_AcdRegulatorMIBObjects_ObjectIdentity((1,3,6,1,4,1,22420,2,6,5))
_AcdRegulatorTableTid_ObjectIdentity=ObjectIdentity
acdRegulatorTableTid=_AcdRegulatorTableTid_ObjectIdentity((1,3,6,1,4,1,22420,2,6,5,1))
_AcdRegulatorTableLastChangeTid_Type=Unsigned32
_AcdRegulatorTableLastChangeTid_Object=MibScalar
acdRegulatorTableLastChangeTid=_AcdRegulatorTableLastChangeTid_Object((1,3,6,1,4,1,22420,2,6,5,1,1),_AcdRegulatorTableLastChangeTid_Type())
acdRegulatorTableLastChangeTid.setMaxAccess(_C)
if mibBuilder.loadTexts:acdRegulatorTableLastChangeTid.setStatus(_A)
_AcdRegulatorConformance_ObjectIdentity=ObjectIdentity
acdRegulatorConformance=_AcdRegulatorConformance_ObjectIdentity((1,3,6,1,4,1,22420,2,6,6))
_AcdRegulatorCompliances_ObjectIdentity=ObjectIdentity
acdRegulatorCompliances=_AcdRegulatorCompliances_ObjectIdentity((1,3,6,1,4,1,22420,2,6,6,1))
_AcdRegulatorGroups_ObjectIdentity=ObjectIdentity
acdRegulatorGroups=_AcdRegulatorGroups_ObjectIdentity((1,3,6,1,4,1,22420,2,6,6,2))
acdRegulatorGroup=ObjectGroup((1,3,6,1,4,1,22420,2,6,6,2,1))
acdRegulatorGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:acdRegulatorGroup.setStatus(_A)
acdRegulatorStatsGroup=ObjectGroup((1,3,6,1,4,1,22420,2,6,6,2,2))
acdRegulatorStatsGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:acdRegulatorStatsGroup.setStatus(_A)
acdRegulatorHistStatsGroup=ObjectGroup((1,3,6,1,4,1,22420,2,6,6,2,3))
acdRegulatorHistStatsGroup.setObjects(*((_B,_K),(_B,_L),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:acdRegulatorHistStatsGroup.setStatus(_A)
acdRegulatorTidGroup=ObjectGroup((1,3,6,1,4,1,22420,2,6,6,2,4))
acdRegulatorTidGroup.setObjects((_B,_AY))
if mibBuilder.loadTexts:acdRegulatorTidGroup.setStatus(_A)
acdRegulatorCompliance=ModuleCompliance((1,3,6,1,4,1,22420,2,6,6,1,1))
acdRegulatorCompliance.setObjects(*((_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac)))
if mibBuilder.loadTexts:acdRegulatorCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'acdRegulator':acdRegulator,'acdRegulatorTable':acdRegulatorTable,'acdRegulatorEntry':acdRegulatorEntry,_N:acdRegulatorID,_Q:acdRegulatorName,_R:acdRegulatorCir,_S:acdRegulatorCbs,_T:acdRegulatorEir,_U:acdRegulatorEbs,_V:acdRegulatorIsBlind,_W:acdRegulatorIsCouple,_X:acdRegulatorRowStatus,_Y:acdRegulatorWorkingRate,_Z:acdRegulatorCirMax,_a:acdRegulatorEirMax,'acdRegulatorStatsTable':acdRegulatorStatsTable,'acdRegulatorStatsEntry':acdRegulatorStatsEntry,_P:acdRegulatorStatsID,_b:acdRegulatorStatsAcceptOctets,_c:acdRegulatorStatsAcceptOverflowOctets,_d:acdRegulatorStatsAcceptHCOctets,_e:acdRegulatorStatsAcceptPkts,_f:acdRegulatorStatsAcceptOverflowPkts,_g:acdRegulatorStatsAcceptHCPkts,_h:acdRegulatorStatsAcceptRate,_i:acdRegulatorStatsDropOctets,_j:acdRegulatorStatsDropOverflowOctets,_k:acdRegulatorStatsDropHCOctets,_l:acdRegulatorStatsDropPkts,_m:acdRegulatorStatsDropOverflowPkts,_n:acdRegulatorStatsDropHCPkts,_o:acdRegulatorStatsDropRate,_p:acdRegulatorStatsGreenHCOctets,_q:acdRegulatorStatsGreenHCPkts,_r:acdRegulatorStatsYellowHCOctets,_s:acdRegulatorStatsYellowHCPkts,_t:acdRegulatorStatsRedHCOctets,_u:acdRegulatorStatsRedHCPkts,_v:acdRegulatorStatsGreenRate,_w:acdRegulatorStatsYellowRate,_x:acdRegulatorStatsRedRate,'acdRegulatorHistStatsTable':acdRegulatorHistStatsTable,'acdRegulatorHistStatsEntry':acdRegulatorHistStatsEntry,_K:acdRegulatorHistStatsID,_L:acdRegulatorHistStatsSampleIndex,_y:acdRegulatorHistStatsStatus,_z:acdRegulatorHistStatsDuration,_A0:acdRegulatorHistStatsIntervalEnd,_A1:acdRegulatorHistStatsAcceptOctets,_A2:acdRegulatorHistStatsAcceptOverflowOctets,_A3:acdRegulatorHistStatsAcceptHCOctets,_A4:acdRegulatorHistStatsAcceptPkts,_A5:acdRegulatorHistStatsAcceptOverflowPkts,_A6:acdRegulatorHistStatsAcceptHCPkts,_A7:acdRegulatorHistStatsAcceptAvgRate,_A8:acdRegulatorHistStatsAcceptMinRate,_A9:acdRegulatorHistStatsAcceptMaxRate,_AA:acdRegulatorHistStatsDropOctets,_AB:acdRegulatorHistStatsDropOverflowOctets,_AC:acdRegulatorHistStatsDropHCOctets,_AD:acdRegulatorHistStatsDropPkts,_AE:acdRegulatorHistStatsDropOverflowPkts,_AF:acdRegulatorHistStatsDropHCPkts,_AG:acdRegulatorHistStatsDropAvgRate,_AH:acdRegulatorHistStatsDropMinRate,_AI:acdRegulatorHistStatsDropMaxRate,_AJ:acdRegulatorHistStatsGreenHCOctets,_AK:acdRegulatorHistStatsGreenHCPkts,_AL:acdRegulatorHistStatsYellowHCOctets,_AM:acdRegulatorHistStatsYellowHCPkts,_AN:acdRegulatorHistStatsRedHCOctets,_AO:acdRegulatorHistStatsRedHCPkts,_AP:acdRegulatorHistStatsGreenAvgRate,_AQ:acdRegulatorHistStatsGreenMinRate,_AR:acdRegulatorHistStatsGreenMaxRate,_AS:acdRegulatorHistStatsYellowAvgRate,_AT:acdRegulatorHistStatsYellowMinRate,_AU:acdRegulatorHistStatsYellowMaxRate,_AV:acdRegulatorHistStatsRedAvgRate,_AW:acdRegulatorHistStatsRedMinRate,_AX:acdRegulatorHistStatsRedMaxRate,'acdRegulatorNotifications':acdRegulatorNotifications,'acdRegulatorMIBObjects':acdRegulatorMIBObjects,'acdRegulatorTableTid':acdRegulatorTableTid,_AY:acdRegulatorTableLastChangeTid,'acdRegulatorConformance':acdRegulatorConformance,'acdRegulatorCompliances':acdRegulatorCompliances,'acdRegulatorCompliance':acdRegulatorCompliance,'acdRegulatorGroups':acdRegulatorGroups,_AZ:acdRegulatorGroup,_Aa:acdRegulatorStatsGroup,_Ab:acdRegulatorHistStatsGroup,_Ac:acdRegulatorTidGroup})