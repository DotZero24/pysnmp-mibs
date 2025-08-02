_x='mitelBWMHistoricalStatisticsGroup'
_w='mitelBWMCumulativeStatisticsGroup'
_v='mitelBWMCurrentStatisticsGroup'
_u='mitelBWM24HrPeakBwdthAboveLimit'
_t='mitelBWM24HrPeakBandwidthRatio'
_s='mitelBWM24HrFinalBandwidthLimit'
_r='mitelBWM24HrAverageAvailable'
_q='mitelBWM24HrPeakBandwidthUsed'
_p='mitelBWM24HrAverageBandwidthUsed'
_o='mitelBWM24HrCACRejectionRatio'
_n='mitelBWM24HrCACRejections'
_m='mitelBWM24HrCACAdmissions'
_l='mitelBWM24HrZAPLabel'
_k='mitelBWM15MinPeakBwdthAboveLimit'
_j='mitelBWM15MinPeakBandwidthRatio'
_i='mitelBWM15MinFinalBandwidthLimit'
_h='mitelBWM15MinAverageAvailable'
_g='mitelBWM15MinPeakBandwidthUsed'
_f='mitelBWM15MinAverageBandwidthUsed'
_e='mitelBWM15MinCACRejectionRatio'
_d='mitelBWM15MinCACRejections'
_c='mitelBWM15MinCACAdmissions'
_b='mitelBWM15MinZAPLabel'
_a='mitelBWMCumCACRejectionRatio'
_Z='mitelBWMCumCACRejections'
_Y='mitelBWMCumCACAdmissions'
_X='mitelBWMCumZAPLabel'
_W='mitelBWMCurrentBandwidthRatio'
_V='mitelBWMCurrentBandwidthLimit'
_U='mitelBWMCurrentBandwidthInUse'
_T='mitelBWMCurrentZAPLabel'
_S='mitelBWM24HrDateAndTime'
_R='mitelBWM24HrZAPID'
_Q='mitelBWM24HrParentZoneID'
_P='mitelBWM24HrZoneID'
_O='mitelBWM15MinDateAndTime'
_N='mitelBWM15MinZAPID'
_M='mitelBWM15MinParentZoneID'
_L='mitelBWM15MinZoneID'
_K='mitelBWMCumZAPID'
_J='mitelBWMCumParentZoneID'
_I='mitelBWMCumZoneID'
_H='mitelBWMCurrentZAPID'
_G='mitelBWMCurrentParentZoneID'
_F='mitelBWMCurrentZoneID'
_E='calls'
_D='kilobits per second'
_C='read-only'
_B='current'
_A='MITEL-BWM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mitelIpera3000Applications,=mibBuilder.importSymbols('MITEL-IperaVoiceLAN-MIB','mitelIpera3000Applications')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
mitelBandWidthManagement=ModuleIdentity((1,3,6,1,4,1,1027,4,1,1,2,5,1))
if mibBuilder.loadTexts:mitelBandWidthManagement.setRevisions(('2007-03-26 15:41','2006-08-28 16:26'))
class MitelBWMPercentage(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class MitelBWMZoneID(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,250))
class MitelBWMZAPID(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_MitelBWMObjects_ObjectIdentity=ObjectIdentity
mitelBWMObjects=_MitelBWMObjects_ObjectIdentity((1,3,6,1,4,1,1027,4,1,1,2,5,1,1))
_MitelBWMCurrentTable_Object=MibTable
mitelBWMCurrentTable=_MitelBWMCurrentTable_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,1))
if mibBuilder.loadTexts:mitelBWMCurrentTable.setStatus(_B)
_MitelBWMCurrentTableEntry_Object=MibTableRow
mitelBWMCurrentTableEntry=_MitelBWMCurrentTableEntry_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,1,1))
mitelBWMCurrentTableEntry.setIndexNames((0,_A,_F),(0,_A,_G),(0,_A,_H))
if mibBuilder.loadTexts:mitelBWMCurrentTableEntry.setStatus(_B)
_MitelBWMCurrentZoneID_Type=MitelBWMZoneID
_MitelBWMCurrentZoneID_Object=MibTableColumn
mitelBWMCurrentZoneID=_MitelBWMCurrentZoneID_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,1,1,1),_MitelBWMCurrentZoneID_Type())
mitelBWMCurrentZoneID.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWMCurrentZoneID.setStatus(_B)
_MitelBWMCurrentParentZoneID_Type=MitelBWMZoneID
_MitelBWMCurrentParentZoneID_Object=MibTableColumn
mitelBWMCurrentParentZoneID=_MitelBWMCurrentParentZoneID_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,1,1,2),_MitelBWMCurrentParentZoneID_Type())
mitelBWMCurrentParentZoneID.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWMCurrentParentZoneID.setStatus(_B)
_MitelBWMCurrentZAPID_Type=MitelBWMZAPID
_MitelBWMCurrentZAPID_Object=MibTableColumn
mitelBWMCurrentZAPID=_MitelBWMCurrentZAPID_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,1,1,3),_MitelBWMCurrentZAPID_Type())
mitelBWMCurrentZAPID.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWMCurrentZAPID.setStatus(_B)
_MitelBWMCurrentZAPLabel_Type=DisplayString
_MitelBWMCurrentZAPLabel_Object=MibTableColumn
mitelBWMCurrentZAPLabel=_MitelBWMCurrentZAPLabel_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,1,1,4),_MitelBWMCurrentZAPLabel_Type())
mitelBWMCurrentZAPLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWMCurrentZAPLabel.setStatus(_B)
_MitelBWMCurrentBandwidthInUse_Type=Gauge32
_MitelBWMCurrentBandwidthInUse_Object=MibTableColumn
mitelBWMCurrentBandwidthInUse=_MitelBWMCurrentBandwidthInUse_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,1,1,5),_MitelBWMCurrentBandwidthInUse_Type())
mitelBWMCurrentBandwidthInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWMCurrentBandwidthInUse.setStatus(_B)
if mibBuilder.loadTexts:mitelBWMCurrentBandwidthInUse.setUnits(_D)
_MitelBWMCurrentBandwidthLimit_Type=Gauge32
_MitelBWMCurrentBandwidthLimit_Object=MibTableColumn
mitelBWMCurrentBandwidthLimit=_MitelBWMCurrentBandwidthLimit_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,1,1,6),_MitelBWMCurrentBandwidthLimit_Type())
mitelBWMCurrentBandwidthLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWMCurrentBandwidthLimit.setStatus(_B)
if mibBuilder.loadTexts:mitelBWMCurrentBandwidthLimit.setUnits(_D)
_MitelBWMCurrentBandwidthRatio_Type=MitelBWMPercentage
_MitelBWMCurrentBandwidthRatio_Object=MibTableColumn
mitelBWMCurrentBandwidthRatio=_MitelBWMCurrentBandwidthRatio_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,1,1,7),_MitelBWMCurrentBandwidthRatio_Type())
mitelBWMCurrentBandwidthRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWMCurrentBandwidthRatio.setStatus(_B)
_MitelBWMCumCACTable_Object=MibTable
mitelBWMCumCACTable=_MitelBWMCumCACTable_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,2))
if mibBuilder.loadTexts:mitelBWMCumCACTable.setStatus(_B)
_MitelBWMCumCACTableEntry_Object=MibTableRow
mitelBWMCumCACTableEntry=_MitelBWMCumCACTableEntry_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,2,1))
mitelBWMCumCACTableEntry.setIndexNames((0,_A,_I),(0,_A,_J),(0,_A,_K))
if mibBuilder.loadTexts:mitelBWMCumCACTableEntry.setStatus(_B)
_MitelBWMCumZoneID_Type=MitelBWMZoneID
_MitelBWMCumZoneID_Object=MibTableColumn
mitelBWMCumZoneID=_MitelBWMCumZoneID_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,2,1,1),_MitelBWMCumZoneID_Type())
mitelBWMCumZoneID.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWMCumZoneID.setStatus(_B)
_MitelBWMCumParentZoneID_Type=MitelBWMZoneID
_MitelBWMCumParentZoneID_Object=MibTableColumn
mitelBWMCumParentZoneID=_MitelBWMCumParentZoneID_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,2,1,2),_MitelBWMCumParentZoneID_Type())
mitelBWMCumParentZoneID.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWMCumParentZoneID.setStatus(_B)
_MitelBWMCumZAPID_Type=MitelBWMZAPID
_MitelBWMCumZAPID_Object=MibTableColumn
mitelBWMCumZAPID=_MitelBWMCumZAPID_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,2,1,3),_MitelBWMCumZAPID_Type())
mitelBWMCumZAPID.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWMCumZAPID.setStatus(_B)
_MitelBWMCumZAPLabel_Type=DisplayString
_MitelBWMCumZAPLabel_Object=MibTableColumn
mitelBWMCumZAPLabel=_MitelBWMCumZAPLabel_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,2,1,4),_MitelBWMCumZAPLabel_Type())
mitelBWMCumZAPLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWMCumZAPLabel.setStatus(_B)
_MitelBWMCumCACAdmissions_Type=Counter32
_MitelBWMCumCACAdmissions_Object=MibTableColumn
mitelBWMCumCACAdmissions=_MitelBWMCumCACAdmissions_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,2,1,5),_MitelBWMCumCACAdmissions_Type())
mitelBWMCumCACAdmissions.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWMCumCACAdmissions.setStatus(_B)
if mibBuilder.loadTexts:mitelBWMCumCACAdmissions.setUnits(_E)
_MitelBWMCumCACRejections_Type=Counter32
_MitelBWMCumCACRejections_Object=MibTableColumn
mitelBWMCumCACRejections=_MitelBWMCumCACRejections_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,2,1,6),_MitelBWMCumCACRejections_Type())
mitelBWMCumCACRejections.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWMCumCACRejections.setStatus(_B)
if mibBuilder.loadTexts:mitelBWMCumCACRejections.setUnits(_E)
_MitelBWMCumCACRejectionRatio_Type=MitelBWMPercentage
_MitelBWMCumCACRejectionRatio_Object=MibTableColumn
mitelBWMCumCACRejectionRatio=_MitelBWMCumCACRejectionRatio_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,2,1,7),_MitelBWMCumCACRejectionRatio_Type())
mitelBWMCumCACRejectionRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWMCumCACRejectionRatio.setStatus(_B)
_MitelBWM15MinHistoryTable_Object=MibTable
mitelBWM15MinHistoryTable=_MitelBWM15MinHistoryTable_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,3))
if mibBuilder.loadTexts:mitelBWM15MinHistoryTable.setStatus(_B)
_MitelBWM15MinHistoryTableEntry_Object=MibTableRow
mitelBWM15MinHistoryTableEntry=_MitelBWM15MinHistoryTableEntry_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,3,1))
mitelBWM15MinHistoryTableEntry.setIndexNames((0,_A,_L),(0,_A,_M),(0,_A,_N),(0,_A,_O))
if mibBuilder.loadTexts:mitelBWM15MinHistoryTableEntry.setStatus(_B)
_MitelBWM15MinZoneID_Type=MitelBWMZoneID
_MitelBWM15MinZoneID_Object=MibTableColumn
mitelBWM15MinZoneID=_MitelBWM15MinZoneID_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,3,1,1),_MitelBWM15MinZoneID_Type())
mitelBWM15MinZoneID.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM15MinZoneID.setStatus(_B)
_MitelBWM15MinParentZoneID_Type=MitelBWMZoneID
_MitelBWM15MinParentZoneID_Object=MibTableColumn
mitelBWM15MinParentZoneID=_MitelBWM15MinParentZoneID_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,3,1,2),_MitelBWM15MinParentZoneID_Type())
mitelBWM15MinParentZoneID.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM15MinParentZoneID.setStatus(_B)
_MitelBWM15MinZAPID_Type=MitelBWMZAPID
_MitelBWM15MinZAPID_Object=MibTableColumn
mitelBWM15MinZAPID=_MitelBWM15MinZAPID_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,3,1,3),_MitelBWM15MinZAPID_Type())
mitelBWM15MinZAPID.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM15MinZAPID.setStatus(_B)
_MitelBWM15MinDateAndTime_Type=DateAndTime
_MitelBWM15MinDateAndTime_Object=MibTableColumn
mitelBWM15MinDateAndTime=_MitelBWM15MinDateAndTime_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,3,1,4),_MitelBWM15MinDateAndTime_Type())
mitelBWM15MinDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM15MinDateAndTime.setStatus(_B)
_MitelBWM15MinZAPLabel_Type=DisplayString
_MitelBWM15MinZAPLabel_Object=MibTableColumn
mitelBWM15MinZAPLabel=_MitelBWM15MinZAPLabel_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,3,1,5),_MitelBWM15MinZAPLabel_Type())
mitelBWM15MinZAPLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM15MinZAPLabel.setStatus(_B)
_MitelBWM15MinCACAdmissions_Type=Counter32
_MitelBWM15MinCACAdmissions_Object=MibTableColumn
mitelBWM15MinCACAdmissions=_MitelBWM15MinCACAdmissions_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,3,1,6),_MitelBWM15MinCACAdmissions_Type())
mitelBWM15MinCACAdmissions.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM15MinCACAdmissions.setStatus(_B)
if mibBuilder.loadTexts:mitelBWM15MinCACAdmissions.setUnits(_E)
_MitelBWM15MinCACRejections_Type=Counter32
_MitelBWM15MinCACRejections_Object=MibTableColumn
mitelBWM15MinCACRejections=_MitelBWM15MinCACRejections_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,3,1,7),_MitelBWM15MinCACRejections_Type())
mitelBWM15MinCACRejections.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM15MinCACRejections.setStatus(_B)
if mibBuilder.loadTexts:mitelBWM15MinCACRejections.setUnits(_E)
_MitelBWM15MinCACRejectionRatio_Type=MitelBWMPercentage
_MitelBWM15MinCACRejectionRatio_Object=MibTableColumn
mitelBWM15MinCACRejectionRatio=_MitelBWM15MinCACRejectionRatio_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,3,1,8),_MitelBWM15MinCACRejectionRatio_Type())
mitelBWM15MinCACRejectionRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM15MinCACRejectionRatio.setStatus(_B)
_MitelBWM15MinAverageBandwidthUsed_Type=Gauge32
_MitelBWM15MinAverageBandwidthUsed_Object=MibTableColumn
mitelBWM15MinAverageBandwidthUsed=_MitelBWM15MinAverageBandwidthUsed_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,3,1,9),_MitelBWM15MinAverageBandwidthUsed_Type())
mitelBWM15MinAverageBandwidthUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM15MinAverageBandwidthUsed.setStatus(_B)
if mibBuilder.loadTexts:mitelBWM15MinAverageBandwidthUsed.setUnits(_D)
_MitelBWM15MinPeakBandwidthUsed_Type=Gauge32
_MitelBWM15MinPeakBandwidthUsed_Object=MibTableColumn
mitelBWM15MinPeakBandwidthUsed=_MitelBWM15MinPeakBandwidthUsed_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,3,1,10),_MitelBWM15MinPeakBandwidthUsed_Type())
mitelBWM15MinPeakBandwidthUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM15MinPeakBandwidthUsed.setStatus(_B)
if mibBuilder.loadTexts:mitelBWM15MinPeakBandwidthUsed.setUnits(_D)
_MitelBWM15MinAverageAvailable_Type=Gauge32
_MitelBWM15MinAverageAvailable_Object=MibTableColumn
mitelBWM15MinAverageAvailable=_MitelBWM15MinAverageAvailable_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,3,1,11),_MitelBWM15MinAverageAvailable_Type())
mitelBWM15MinAverageAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM15MinAverageAvailable.setStatus(_B)
if mibBuilder.loadTexts:mitelBWM15MinAverageAvailable.setUnits(_D)
_MitelBWM15MinFinalBandwidthLimit_Type=Gauge32
_MitelBWM15MinFinalBandwidthLimit_Object=MibTableColumn
mitelBWM15MinFinalBandwidthLimit=_MitelBWM15MinFinalBandwidthLimit_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,3,1,12),_MitelBWM15MinFinalBandwidthLimit_Type())
mitelBWM15MinFinalBandwidthLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM15MinFinalBandwidthLimit.setStatus(_B)
if mibBuilder.loadTexts:mitelBWM15MinFinalBandwidthLimit.setUnits(_D)
_MitelBWM15MinPeakBandwidthRatio_Type=MitelBWMPercentage
_MitelBWM15MinPeakBandwidthRatio_Object=MibTableColumn
mitelBWM15MinPeakBandwidthRatio=_MitelBWM15MinPeakBandwidthRatio_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,3,1,13),_MitelBWM15MinPeakBandwidthRatio_Type())
mitelBWM15MinPeakBandwidthRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM15MinPeakBandwidthRatio.setStatus(_B)
_MitelBWM15MinPeakBwdthAboveLimit_Type=Gauge32
_MitelBWM15MinPeakBwdthAboveLimit_Object=MibTableColumn
mitelBWM15MinPeakBwdthAboveLimit=_MitelBWM15MinPeakBwdthAboveLimit_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,3,1,14),_MitelBWM15MinPeakBwdthAboveLimit_Type())
mitelBWM15MinPeakBwdthAboveLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM15MinPeakBwdthAboveLimit.setStatus(_B)
if mibBuilder.loadTexts:mitelBWM15MinPeakBwdthAboveLimit.setUnits(_D)
_MitelBWM24HrHistoryTable_Object=MibTable
mitelBWM24HrHistoryTable=_MitelBWM24HrHistoryTable_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,4))
if mibBuilder.loadTexts:mitelBWM24HrHistoryTable.setStatus(_B)
_MitelBWM24HrHistoryTableEntry_Object=MibTableRow
mitelBWM24HrHistoryTableEntry=_MitelBWM24HrHistoryTableEntry_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,4,1))
mitelBWM24HrHistoryTableEntry.setIndexNames((0,_A,_P),(0,_A,_Q),(0,_A,_R),(0,_A,_S))
if mibBuilder.loadTexts:mitelBWM24HrHistoryTableEntry.setStatus(_B)
_MitelBWM24HrZoneID_Type=MitelBWMZoneID
_MitelBWM24HrZoneID_Object=MibTableColumn
mitelBWM24HrZoneID=_MitelBWM24HrZoneID_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,4,1,1),_MitelBWM24HrZoneID_Type())
mitelBWM24HrZoneID.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM24HrZoneID.setStatus(_B)
_MitelBWM24HrParentZoneID_Type=MitelBWMZoneID
_MitelBWM24HrParentZoneID_Object=MibTableColumn
mitelBWM24HrParentZoneID=_MitelBWM24HrParentZoneID_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,4,1,2),_MitelBWM24HrParentZoneID_Type())
mitelBWM24HrParentZoneID.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM24HrParentZoneID.setStatus(_B)
_MitelBWM24HrZAPID_Type=MitelBWMZAPID
_MitelBWM24HrZAPID_Object=MibTableColumn
mitelBWM24HrZAPID=_MitelBWM24HrZAPID_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,4,1,3),_MitelBWM24HrZAPID_Type())
mitelBWM24HrZAPID.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM24HrZAPID.setStatus(_B)
_MitelBWM24HrDateAndTime_Type=DateAndTime
_MitelBWM24HrDateAndTime_Object=MibTableColumn
mitelBWM24HrDateAndTime=_MitelBWM24HrDateAndTime_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,4,1,4),_MitelBWM24HrDateAndTime_Type())
mitelBWM24HrDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM24HrDateAndTime.setStatus(_B)
_MitelBWM24HrZAPLabel_Type=DisplayString
_MitelBWM24HrZAPLabel_Object=MibTableColumn
mitelBWM24HrZAPLabel=_MitelBWM24HrZAPLabel_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,4,1,5),_MitelBWM24HrZAPLabel_Type())
mitelBWM24HrZAPLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM24HrZAPLabel.setStatus(_B)
_MitelBWM24HrCACAdmissions_Type=Counter32
_MitelBWM24HrCACAdmissions_Object=MibTableColumn
mitelBWM24HrCACAdmissions=_MitelBWM24HrCACAdmissions_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,4,1,6),_MitelBWM24HrCACAdmissions_Type())
mitelBWM24HrCACAdmissions.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM24HrCACAdmissions.setStatus(_B)
if mibBuilder.loadTexts:mitelBWM24HrCACAdmissions.setUnits(_E)
_MitelBWM24HrCACRejections_Type=Counter32
_MitelBWM24HrCACRejections_Object=MibTableColumn
mitelBWM24HrCACRejections=_MitelBWM24HrCACRejections_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,4,1,7),_MitelBWM24HrCACRejections_Type())
mitelBWM24HrCACRejections.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM24HrCACRejections.setStatus(_B)
if mibBuilder.loadTexts:mitelBWM24HrCACRejections.setUnits(_E)
_MitelBWM24HrCACRejectionRatio_Type=MitelBWMPercentage
_MitelBWM24HrCACRejectionRatio_Object=MibTableColumn
mitelBWM24HrCACRejectionRatio=_MitelBWM24HrCACRejectionRatio_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,4,1,8),_MitelBWM24HrCACRejectionRatio_Type())
mitelBWM24HrCACRejectionRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM24HrCACRejectionRatio.setStatus(_B)
_MitelBWM24HrAverageBandwidthUsed_Type=Gauge32
_MitelBWM24HrAverageBandwidthUsed_Object=MibTableColumn
mitelBWM24HrAverageBandwidthUsed=_MitelBWM24HrAverageBandwidthUsed_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,4,1,9),_MitelBWM24HrAverageBandwidthUsed_Type())
mitelBWM24HrAverageBandwidthUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM24HrAverageBandwidthUsed.setStatus(_B)
if mibBuilder.loadTexts:mitelBWM24HrAverageBandwidthUsed.setUnits(_D)
_MitelBWM24HrPeakBandwidthUsed_Type=Gauge32
_MitelBWM24HrPeakBandwidthUsed_Object=MibTableColumn
mitelBWM24HrPeakBandwidthUsed=_MitelBWM24HrPeakBandwidthUsed_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,4,1,10),_MitelBWM24HrPeakBandwidthUsed_Type())
mitelBWM24HrPeakBandwidthUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM24HrPeakBandwidthUsed.setStatus(_B)
if mibBuilder.loadTexts:mitelBWM24HrPeakBandwidthUsed.setUnits(_D)
_MitelBWM24HrAverageAvailable_Type=Gauge32
_MitelBWM24HrAverageAvailable_Object=MibTableColumn
mitelBWM24HrAverageAvailable=_MitelBWM24HrAverageAvailable_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,4,1,11),_MitelBWM24HrAverageAvailable_Type())
mitelBWM24HrAverageAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM24HrAverageAvailable.setStatus(_B)
if mibBuilder.loadTexts:mitelBWM24HrAverageAvailable.setUnits(_D)
_MitelBWM24HrFinalBandwidthLimit_Type=Gauge32
_MitelBWM24HrFinalBandwidthLimit_Object=MibTableColumn
mitelBWM24HrFinalBandwidthLimit=_MitelBWM24HrFinalBandwidthLimit_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,4,1,12),_MitelBWM24HrFinalBandwidthLimit_Type())
mitelBWM24HrFinalBandwidthLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM24HrFinalBandwidthLimit.setStatus(_B)
if mibBuilder.loadTexts:mitelBWM24HrFinalBandwidthLimit.setUnits(_D)
_MitelBWM24HrPeakBandwidthRatio_Type=MitelBWMPercentage
_MitelBWM24HrPeakBandwidthRatio_Object=MibTableColumn
mitelBWM24HrPeakBandwidthRatio=_MitelBWM24HrPeakBandwidthRatio_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,4,1,13),_MitelBWM24HrPeakBandwidthRatio_Type())
mitelBWM24HrPeakBandwidthRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM24HrPeakBandwidthRatio.setStatus(_B)
_MitelBWM24HrPeakBwdthAboveLimit_Type=Gauge32
_MitelBWM24HrPeakBwdthAboveLimit_Object=MibTableColumn
mitelBWM24HrPeakBwdthAboveLimit=_MitelBWM24HrPeakBwdthAboveLimit_Object((1,3,6,1,4,1,1027,4,1,1,2,5,1,1,4,1,14),_MitelBWM24HrPeakBwdthAboveLimit_Type())
mitelBWM24HrPeakBwdthAboveLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBWM24HrPeakBwdthAboveLimit.setStatus(_B)
if mibBuilder.loadTexts:mitelBWM24HrPeakBwdthAboveLimit.setUnits(_D)
_MitelBWMConformance_ObjectIdentity=ObjectIdentity
mitelBWMConformance=_MitelBWMConformance_ObjectIdentity((1,3,6,1,4,1,1027,4,1,1,2,5,1,2))
_MitelBWMGroups_ObjectIdentity=ObjectIdentity
mitelBWMGroups=_MitelBWMGroups_ObjectIdentity((1,3,6,1,4,1,1027,4,1,1,2,5,1,2,1))
if mibBuilder.loadTexts:mitelBWMGroups.setStatus(_B)
_MitelBWMCompliances_ObjectIdentity=ObjectIdentity
mitelBWMCompliances=_MitelBWMCompliances_ObjectIdentity((1,3,6,1,4,1,1027,4,1,1,2,5,1,2,2))
if mibBuilder.loadTexts:mitelBWMCompliances.setStatus(_B)
mitelBWMCurrentStatisticsGroup=ObjectGroup((1,3,6,1,4,1,1027,4,1,1,2,5,1,2,1,1))
mitelBWMCurrentStatisticsGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:mitelBWMCurrentStatisticsGroup.setStatus(_B)
mitelBWMCumulativeStatisticsGroup=ObjectGroup((1,3,6,1,4,1,1027,4,1,1,2,5,1,2,1,2))
mitelBWMCumulativeStatisticsGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:mitelBWMCumulativeStatisticsGroup.setStatus(_B)
mitelBWMHistoricalStatisticsGroup=ObjectGroup((1,3,6,1,4,1,1027,4,1,1,2,5,1,2,1,3))
mitelBWMHistoricalStatisticsGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:mitelBWMHistoricalStatisticsGroup.setStatus(_B)
mitelBWMCompliance=ModuleCompliance((1,3,6,1,4,1,1027,4,1,1,2,5,1,2,2,1))
mitelBWMCompliance.setObjects(*((_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:mitelBWMCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'MitelBWMPercentage':MitelBWMPercentage,'MitelBWMZoneID':MitelBWMZoneID,'MitelBWMZAPID':MitelBWMZAPID,'mitelBandWidthManagement':mitelBandWidthManagement,'mitelBWMObjects':mitelBWMObjects,'mitelBWMCurrentTable':mitelBWMCurrentTable,'mitelBWMCurrentTableEntry':mitelBWMCurrentTableEntry,_F:mitelBWMCurrentZoneID,_G:mitelBWMCurrentParentZoneID,_H:mitelBWMCurrentZAPID,_T:mitelBWMCurrentZAPLabel,_U:mitelBWMCurrentBandwidthInUse,_V:mitelBWMCurrentBandwidthLimit,_W:mitelBWMCurrentBandwidthRatio,'mitelBWMCumCACTable':mitelBWMCumCACTable,'mitelBWMCumCACTableEntry':mitelBWMCumCACTableEntry,_I:mitelBWMCumZoneID,_J:mitelBWMCumParentZoneID,_K:mitelBWMCumZAPID,_X:mitelBWMCumZAPLabel,_Y:mitelBWMCumCACAdmissions,_Z:mitelBWMCumCACRejections,_a:mitelBWMCumCACRejectionRatio,'mitelBWM15MinHistoryTable':mitelBWM15MinHistoryTable,'mitelBWM15MinHistoryTableEntry':mitelBWM15MinHistoryTableEntry,_L:mitelBWM15MinZoneID,_M:mitelBWM15MinParentZoneID,_N:mitelBWM15MinZAPID,_O:mitelBWM15MinDateAndTime,_b:mitelBWM15MinZAPLabel,_c:mitelBWM15MinCACAdmissions,_d:mitelBWM15MinCACRejections,_e:mitelBWM15MinCACRejectionRatio,_f:mitelBWM15MinAverageBandwidthUsed,_g:mitelBWM15MinPeakBandwidthUsed,_h:mitelBWM15MinAverageAvailable,_i:mitelBWM15MinFinalBandwidthLimit,_j:mitelBWM15MinPeakBandwidthRatio,_k:mitelBWM15MinPeakBwdthAboveLimit,'mitelBWM24HrHistoryTable':mitelBWM24HrHistoryTable,'mitelBWM24HrHistoryTableEntry':mitelBWM24HrHistoryTableEntry,_P:mitelBWM24HrZoneID,_Q:mitelBWM24HrParentZoneID,_R:mitelBWM24HrZAPID,_S:mitelBWM24HrDateAndTime,_l:mitelBWM24HrZAPLabel,_m:mitelBWM24HrCACAdmissions,_n:mitelBWM24HrCACRejections,_o:mitelBWM24HrCACRejectionRatio,_p:mitelBWM24HrAverageBandwidthUsed,_q:mitelBWM24HrPeakBandwidthUsed,_r:mitelBWM24HrAverageAvailable,_s:mitelBWM24HrFinalBandwidthLimit,_t:mitelBWM24HrPeakBandwidthRatio,_u:mitelBWM24HrPeakBwdthAboveLimit,'mitelBWMConformance':mitelBWMConformance,'mitelBWMGroups':mitelBWMGroups,_v:mitelBWMCurrentStatisticsGroup,_w:mitelBWMCumulativeStatisticsGroup,_x:mitelBWMHistoricalStatisticsGroup,'mitelBWMCompliances':mitelBWMCompliances,'mitelBWMCompliance':mitelBWMCompliance})