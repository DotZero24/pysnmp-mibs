_Af='ciscoWANSonetFEPathPrev24HrMIBGroup'
_Ae='ciscoWANSonetFEPathAlarmMIBGroup'
_Ad='ciscoWANSonetPathPrev24HrMIBGroup'
_Ac='ciscoWANSonetFELinePrev24HrMIBGroup'
_Ab='ciscoWANSonetFELineAlarmMIBGroup'
_Aa='ciscoWANSonetLinePrev24HrMIBGroup'
_AZ='ciscoWANSonetPathAlarmMIBGroup'
_AY='ciscoWANSonetLineAlarmMIBGroup'
_AX='ciscoWANSonetSectAlarmMIBGroup'
_AW='cwsFEPathPrevious24HrUASs'
_AV='cwsFEPathPrevious24HrCVs'
_AU='cwsFEPathPrevious24HrSESs'
_AT='cwsFEPathPrevious24HrESs'
_AS='cwsPathPrevious24HrUASs'
_AR='cwsPathPrevious24HrCVs'
_AQ='cwsPathPrevious24HrSESs'
_AP='cwsPathPrevious24HrESs'
_AO='cwsFEPathCurrent24HrUASs'
_AN='cwsFEPathCurrent24HrCVs'
_AM='cwsFEPathCurrent24HrSESs'
_AL='cwsFEPathCurrent24HrESs'
_AK='cwsPathCurrent24HrUASs'
_AJ='cwsPathCurrent24HrCVs'
_AI='cwsPathCurrent24HrSESs'
_AH='cwsPathCurrent24HrESs'
_AG='cwsPathStatAlarmStatus'
_AF='cwsPathTotalUASsThreshold'
_AE='cwsPathCurrentUASsThreshold'
_AD='cwsPathTotalCVsThreshold'
_AC='cwsPathCurrentCVsThreshold'
_AB='cwsPathTotalSESsThreshold'
_AA='cwsPathCurrentSESsThreshold'
_A9='cwsPathTotalESsThreshold'
_A8='cwsPathCurrentESsThreshold'
_A7='cwsPathStatisticalAlarmSeverity'
_A6='cwsFELinePrevious24HrUASs'
_A5='cwsFELinePrevious24HrCVs'
_A4='cwsFELinePrevious24HrSESs'
_A3='cwsFELinePrevious24HrESs'
_A2='cwsLinePrevious24HrUASs'
_A1='cwsLinePrevious24HrCVs'
_A0='cwsLinePrevious24HrSESs'
_z='cwsLinePrevious24HrESs'
_y='cwsFELineCurrent24HrUASs'
_x='cwsFELineCurrent24HrCVs'
_w='cwsFELineCurrent24HrSESs'
_v='cwsFELineCurrent24HrESs'
_u='cwsLineCurrent24HrUASs'
_t='cwsLineCurrent24HrCVs'
_s='cwsLineCurrent24HrSESs'
_r='cwsLineCurrent24HrESs'
_q='cwsLineStatAlarmStatus'
_p='cwsLineTotalUASsThreshold'
_o='cwsLineCurrentUASsThreshold'
_n='cwsLineTotalCVsThreshold'
_m='cwsLineCurrentCVsThreshold'
_l='cwsLineTotalSESsThreshold'
_k='cwsLineCurrentSESsThreshold'
_j='cwsLineTotalESsThreshold'
_i='cwsLineCurrentESsThreshold'
_h='cwsLineStatisticalAlarmSeverity'
_g='cwsSectionPrevious24HrCVs'
_f='cwsSectionPrevious24HrSEFSs'
_e='cwsSectionPrevious24HrSESs'
_d='cwsSectionPrevious24HrESs'
_c='cwsSectionCurrent24HrCVs'
_b='cwsSectionCurrent24HrSEFSs'
_a='cwsSectionCurrent24HrSESs'
_Z='cwsSectionCurrent24HrESs'
_Y='cwsSectionStatAlarmStatus'
_X='cwsSectionTotalCVsThreshold'
_W='cwsSectionCurrentCVsThreshold'
_V='cwsSectionTotalSEFSsThreshold'
_U='cwsSectionCurrentSEFSsThreshold'
_T='cwsSectionTotalSESsThreshold'
_S='cwsSectionCurrentSESsThreshold'
_R='cwsSectionTotalESsThreshold'
_Q='cwsSectionCurrentESsThreshold'
_P='cwsSectionStatisticalAlarmSeverity'
_O='none'
_N='major'
_M='minor'
_L='severely errored framing seconds'
_K='Integer32'
_J='Unavailable seconds'
_I='ifIndex'
_H='IF-MIB'
_G='coding violations'
_F='severely errored seconds'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='CISCO-WAN-SONET-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ifIndex,=mibBuilder.importSymbols(_H,_I)
PerfIntervalCount,=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfIntervalCount')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWANSonetMIB=ModuleIdentity((1,3,6,1,4,1,351,150,3))
if mibBuilder.loadTexts:ciscoWANSonetMIB.setRevisions(('2002-05-20 00:00','2000-03-06 00:00'))
_CiscoWANSonetMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWANSonetMIBObjects=_CiscoWANSonetMIBObjects_ObjectIdentity((1,3,6,1,4,1,351,150,3,1))
_CwsSection_ObjectIdentity=ObjectIdentity
cwsSection=_CwsSection_ObjectIdentity((1,3,6,1,4,1,351,150,3,1,1))
_CwsSectionAlarmTable_Object=MibTable
cwsSectionAlarmTable=_CwsSectionAlarmTable_Object((1,3,6,1,4,1,351,150,3,1,1,1))
if mibBuilder.loadTexts:cwsSectionAlarmTable.setStatus(_A)
_CwsSectionAlarmEntry_Object=MibTableRow
cwsSectionAlarmEntry=_CwsSectionAlarmEntry_Object((1,3,6,1,4,1,351,150,3,1,1,1,1))
cwsSectionAlarmEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cwsSectionAlarmEntry.setStatus(_A)
class _CwsSectionStatisticalAlarmSeverity_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_CwsSectionStatisticalAlarmSeverity_Type.__name__=_K
_CwsSectionStatisticalAlarmSeverity_Object=MibTableColumn
cwsSectionStatisticalAlarmSeverity=_CwsSectionStatisticalAlarmSeverity_Object((1,3,6,1,4,1,351,150,3,1,1,1,1,1),_CwsSectionStatisticalAlarmSeverity_Type())
cwsSectionStatisticalAlarmSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsSectionStatisticalAlarmSeverity.setStatus(_A)
class _CwsSectionCurrentESsThreshold_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSectionCurrentESsThreshold_Type.__name__=_E
_CwsSectionCurrentESsThreshold_Object=MibTableColumn
cwsSectionCurrentESsThreshold=_CwsSectionCurrentESsThreshold_Object((1,3,6,1,4,1,351,150,3,1,1,1,1,2),_CwsSectionCurrentESsThreshold_Type())
cwsSectionCurrentESsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsSectionCurrentESsThreshold.setStatus(_A)
class _CwsSectionTotalESsThreshold_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSectionTotalESsThreshold_Type.__name__=_E
_CwsSectionTotalESsThreshold_Object=MibTableColumn
cwsSectionTotalESsThreshold=_CwsSectionTotalESsThreshold_Object((1,3,6,1,4,1,351,150,3,1,1,1,1,3),_CwsSectionTotalESsThreshold_Type())
cwsSectionTotalESsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsSectionTotalESsThreshold.setStatus(_A)
class _CwsSectionCurrentSESsThreshold_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSectionCurrentSESsThreshold_Type.__name__=_E
_CwsSectionCurrentSESsThreshold_Object=MibTableColumn
cwsSectionCurrentSESsThreshold=_CwsSectionCurrentSESsThreshold_Object((1,3,6,1,4,1,351,150,3,1,1,1,1,4),_CwsSectionCurrentSESsThreshold_Type())
cwsSectionCurrentSESsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsSectionCurrentSESsThreshold.setStatus(_A)
if mibBuilder.loadTexts:cwsSectionCurrentSESsThreshold.setUnits(_F)
class _CwsSectionTotalSESsThreshold_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSectionTotalSESsThreshold_Type.__name__=_E
_CwsSectionTotalSESsThreshold_Object=MibTableColumn
cwsSectionTotalSESsThreshold=_CwsSectionTotalSESsThreshold_Object((1,3,6,1,4,1,351,150,3,1,1,1,1,5),_CwsSectionTotalSESsThreshold_Type())
cwsSectionTotalSESsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsSectionTotalSESsThreshold.setStatus(_A)
if mibBuilder.loadTexts:cwsSectionTotalSESsThreshold.setUnits(_F)
class _CwsSectionCurrentSEFSsThreshold_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSectionCurrentSEFSsThreshold_Type.__name__=_E
_CwsSectionCurrentSEFSsThreshold_Object=MibTableColumn
cwsSectionCurrentSEFSsThreshold=_CwsSectionCurrentSEFSsThreshold_Object((1,3,6,1,4,1,351,150,3,1,1,1,1,6),_CwsSectionCurrentSEFSsThreshold_Type())
cwsSectionCurrentSEFSsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsSectionCurrentSEFSsThreshold.setStatus(_A)
if mibBuilder.loadTexts:cwsSectionCurrentSEFSsThreshold.setUnits(_L)
class _CwsSectionTotalSEFSsThreshold_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSectionTotalSEFSsThreshold_Type.__name__=_E
_CwsSectionTotalSEFSsThreshold_Object=MibTableColumn
cwsSectionTotalSEFSsThreshold=_CwsSectionTotalSEFSsThreshold_Object((1,3,6,1,4,1,351,150,3,1,1,1,1,7),_CwsSectionTotalSEFSsThreshold_Type())
cwsSectionTotalSEFSsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsSectionTotalSEFSsThreshold.setStatus(_A)
if mibBuilder.loadTexts:cwsSectionTotalSEFSsThreshold.setUnits(_L)
class _CwsSectionCurrentCVsThreshold_Type(Unsigned32):defaultValue=25;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSectionCurrentCVsThreshold_Type.__name__=_E
_CwsSectionCurrentCVsThreshold_Object=MibTableColumn
cwsSectionCurrentCVsThreshold=_CwsSectionCurrentCVsThreshold_Object((1,3,6,1,4,1,351,150,3,1,1,1,1,8),_CwsSectionCurrentCVsThreshold_Type())
cwsSectionCurrentCVsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsSectionCurrentCVsThreshold.setStatus(_A)
if mibBuilder.loadTexts:cwsSectionCurrentCVsThreshold.setUnits(_G)
class _CwsSectionTotalCVsThreshold_Type(Unsigned32):defaultValue=25;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSectionTotalCVsThreshold_Type.__name__=_E
_CwsSectionTotalCVsThreshold_Object=MibTableColumn
cwsSectionTotalCVsThreshold=_CwsSectionTotalCVsThreshold_Object((1,3,6,1,4,1,351,150,3,1,1,1,1,9),_CwsSectionTotalCVsThreshold_Type())
cwsSectionTotalCVsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsSectionTotalCVsThreshold.setStatus(_A)
if mibBuilder.loadTexts:cwsSectionTotalCVsThreshold.setUnits(_G)
class _CwsSectionStatAlarmStatus_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,511))
_CwsSectionStatAlarmStatus_Type.__name__=_E
_CwsSectionStatAlarmStatus_Object=MibTableColumn
cwsSectionStatAlarmStatus=_CwsSectionStatAlarmStatus_Object((1,3,6,1,4,1,351,150,3,1,1,1,1,10),_CwsSectionStatAlarmStatus_Type())
cwsSectionStatAlarmStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsSectionStatAlarmStatus.setStatus(_A)
_CwsSectionCurrent24HrTable_Object=MibTable
cwsSectionCurrent24HrTable=_CwsSectionCurrent24HrTable_Object((1,3,6,1,4,1,351,150,3,1,1,2))
if mibBuilder.loadTexts:cwsSectionCurrent24HrTable.setStatus(_A)
_CwsSectionCurrent24HrEntry_Object=MibTableRow
cwsSectionCurrent24HrEntry=_CwsSectionCurrent24HrEntry_Object((1,3,6,1,4,1,351,150,3,1,1,2,1))
cwsSectionCurrent24HrEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cwsSectionCurrent24HrEntry.setStatus(_A)
_CwsSectionCurrent24HrESs_Type=PerfIntervalCount
_CwsSectionCurrent24HrESs_Object=MibTableColumn
cwsSectionCurrent24HrESs=_CwsSectionCurrent24HrESs_Object((1,3,6,1,4,1,351,150,3,1,1,2,1,1),_CwsSectionCurrent24HrESs_Type())
cwsSectionCurrent24HrESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSectionCurrent24HrESs.setStatus(_A)
_CwsSectionCurrent24HrSESs_Type=PerfIntervalCount
_CwsSectionCurrent24HrSESs_Object=MibTableColumn
cwsSectionCurrent24HrSESs=_CwsSectionCurrent24HrSESs_Object((1,3,6,1,4,1,351,150,3,1,1,2,1,2),_CwsSectionCurrent24HrSESs_Type())
cwsSectionCurrent24HrSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSectionCurrent24HrSESs.setStatus(_A)
if mibBuilder.loadTexts:cwsSectionCurrent24HrSESs.setUnits(_F)
_CwsSectionCurrent24HrSEFSs_Type=PerfIntervalCount
_CwsSectionCurrent24HrSEFSs_Object=MibTableColumn
cwsSectionCurrent24HrSEFSs=_CwsSectionCurrent24HrSEFSs_Object((1,3,6,1,4,1,351,150,3,1,1,2,1,3),_CwsSectionCurrent24HrSEFSs_Type())
cwsSectionCurrent24HrSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSectionCurrent24HrSEFSs.setStatus(_A)
if mibBuilder.loadTexts:cwsSectionCurrent24HrSEFSs.setUnits(_L)
_CwsSectionCurrent24HrCVs_Type=PerfIntervalCount
_CwsSectionCurrent24HrCVs_Object=MibTableColumn
cwsSectionCurrent24HrCVs=_CwsSectionCurrent24HrCVs_Object((1,3,6,1,4,1,351,150,3,1,1,2,1,4),_CwsSectionCurrent24HrCVs_Type())
cwsSectionCurrent24HrCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSectionCurrent24HrCVs.setStatus(_A)
if mibBuilder.loadTexts:cwsSectionCurrent24HrCVs.setUnits(_G)
_CwsSectionPrevious24HrTable_Object=MibTable
cwsSectionPrevious24HrTable=_CwsSectionPrevious24HrTable_Object((1,3,6,1,4,1,351,150,3,1,1,3))
if mibBuilder.loadTexts:cwsSectionPrevious24HrTable.setStatus(_A)
_CwsSectionPrevious24HrEntry_Object=MibTableRow
cwsSectionPrevious24HrEntry=_CwsSectionPrevious24HrEntry_Object((1,3,6,1,4,1,351,150,3,1,1,3,1))
cwsSectionPrevious24HrEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cwsSectionPrevious24HrEntry.setStatus(_A)
_CwsSectionPrevious24HrESs_Type=PerfIntervalCount
_CwsSectionPrevious24HrESs_Object=MibTableColumn
cwsSectionPrevious24HrESs=_CwsSectionPrevious24HrESs_Object((1,3,6,1,4,1,351,150,3,1,1,3,1,1),_CwsSectionPrevious24HrESs_Type())
cwsSectionPrevious24HrESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSectionPrevious24HrESs.setStatus(_A)
_CwsSectionPrevious24HrSESs_Type=PerfIntervalCount
_CwsSectionPrevious24HrSESs_Object=MibTableColumn
cwsSectionPrevious24HrSESs=_CwsSectionPrevious24HrSESs_Object((1,3,6,1,4,1,351,150,3,1,1,3,1,2),_CwsSectionPrevious24HrSESs_Type())
cwsSectionPrevious24HrSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSectionPrevious24HrSESs.setStatus(_A)
if mibBuilder.loadTexts:cwsSectionPrevious24HrSESs.setUnits(_F)
_CwsSectionPrevious24HrSEFSs_Type=PerfIntervalCount
_CwsSectionPrevious24HrSEFSs_Object=MibTableColumn
cwsSectionPrevious24HrSEFSs=_CwsSectionPrevious24HrSEFSs_Object((1,3,6,1,4,1,351,150,3,1,1,3,1,3),_CwsSectionPrevious24HrSEFSs_Type())
cwsSectionPrevious24HrSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSectionPrevious24HrSEFSs.setStatus(_A)
if mibBuilder.loadTexts:cwsSectionPrevious24HrSEFSs.setUnits(_L)
_CwsSectionPrevious24HrCVs_Type=PerfIntervalCount
_CwsSectionPrevious24HrCVs_Object=MibTableColumn
cwsSectionPrevious24HrCVs=_CwsSectionPrevious24HrCVs_Object((1,3,6,1,4,1,351,150,3,1,1,3,1,4),_CwsSectionPrevious24HrCVs_Type())
cwsSectionPrevious24HrCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSectionPrevious24HrCVs.setStatus(_A)
if mibBuilder.loadTexts:cwsSectionPrevious24HrCVs.setUnits(_G)
_CwsLine_ObjectIdentity=ObjectIdentity
cwsLine=_CwsLine_ObjectIdentity((1,3,6,1,4,1,351,150,3,1,2))
_CwsLineAlarmTable_Object=MibTable
cwsLineAlarmTable=_CwsLineAlarmTable_Object((1,3,6,1,4,1,351,150,3,1,2,1))
if mibBuilder.loadTexts:cwsLineAlarmTable.setStatus(_A)
_CwsLineAlarmEntry_Object=MibTableRow
cwsLineAlarmEntry=_CwsLineAlarmEntry_Object((1,3,6,1,4,1,351,150,3,1,2,1,1))
cwsLineAlarmEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cwsLineAlarmEntry.setStatus(_A)
class _CwsLineStatisticalAlarmSeverity_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_CwsLineStatisticalAlarmSeverity_Type.__name__=_K
_CwsLineStatisticalAlarmSeverity_Object=MibTableColumn
cwsLineStatisticalAlarmSeverity=_CwsLineStatisticalAlarmSeverity_Object((1,3,6,1,4,1,351,150,3,1,2,1,1,1),_CwsLineStatisticalAlarmSeverity_Type())
cwsLineStatisticalAlarmSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsLineStatisticalAlarmSeverity.setStatus(_A)
class _CwsLineCurrentESsThreshold_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsLineCurrentESsThreshold_Type.__name__=_E
_CwsLineCurrentESsThreshold_Object=MibTableColumn
cwsLineCurrentESsThreshold=_CwsLineCurrentESsThreshold_Object((1,3,6,1,4,1,351,150,3,1,2,1,1,2),_CwsLineCurrentESsThreshold_Type())
cwsLineCurrentESsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsLineCurrentESsThreshold.setStatus(_A)
class _CwsLineTotalESsThreshold_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsLineTotalESsThreshold_Type.__name__=_E
_CwsLineTotalESsThreshold_Object=MibTableColumn
cwsLineTotalESsThreshold=_CwsLineTotalESsThreshold_Object((1,3,6,1,4,1,351,150,3,1,2,1,1,3),_CwsLineTotalESsThreshold_Type())
cwsLineTotalESsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsLineTotalESsThreshold.setStatus(_A)
class _CwsLineCurrentSESsThreshold_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsLineCurrentSESsThreshold_Type.__name__=_E
_CwsLineCurrentSESsThreshold_Object=MibTableColumn
cwsLineCurrentSESsThreshold=_CwsLineCurrentSESsThreshold_Object((1,3,6,1,4,1,351,150,3,1,2,1,1,4),_CwsLineCurrentSESsThreshold_Type())
cwsLineCurrentSESsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsLineCurrentSESsThreshold.setStatus(_A)
class _CwsLineTotalSESsThreshold_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsLineTotalSESsThreshold_Type.__name__=_E
_CwsLineTotalSESsThreshold_Object=MibTableColumn
cwsLineTotalSESsThreshold=_CwsLineTotalSESsThreshold_Object((1,3,6,1,4,1,351,150,3,1,2,1,1,5),_CwsLineTotalSESsThreshold_Type())
cwsLineTotalSESsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsLineTotalSESsThreshold.setStatus(_A)
class _CwsLineCurrentCVsThreshold_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsLineCurrentCVsThreshold_Type.__name__=_E
_CwsLineCurrentCVsThreshold_Object=MibTableColumn
cwsLineCurrentCVsThreshold=_CwsLineCurrentCVsThreshold_Object((1,3,6,1,4,1,351,150,3,1,2,1,1,6),_CwsLineCurrentCVsThreshold_Type())
cwsLineCurrentCVsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsLineCurrentCVsThreshold.setStatus(_A)
class _CwsLineTotalCVsThreshold_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsLineTotalCVsThreshold_Type.__name__=_E
_CwsLineTotalCVsThreshold_Object=MibTableColumn
cwsLineTotalCVsThreshold=_CwsLineTotalCVsThreshold_Object((1,3,6,1,4,1,351,150,3,1,2,1,1,7),_CwsLineTotalCVsThreshold_Type())
cwsLineTotalCVsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsLineTotalCVsThreshold.setStatus(_A)
class _CwsLineCurrentUASsThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsLineCurrentUASsThreshold_Type.__name__=_E
_CwsLineCurrentUASsThreshold_Object=MibTableColumn
cwsLineCurrentUASsThreshold=_CwsLineCurrentUASsThreshold_Object((1,3,6,1,4,1,351,150,3,1,2,1,1,8),_CwsLineCurrentUASsThreshold_Type())
cwsLineCurrentUASsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsLineCurrentUASsThreshold.setStatus(_A)
class _CwsLineTotalUASsThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsLineTotalUASsThreshold_Type.__name__=_E
_CwsLineTotalUASsThreshold_Object=MibTableColumn
cwsLineTotalUASsThreshold=_CwsLineTotalUASsThreshold_Object((1,3,6,1,4,1,351,150,3,1,2,1,1,9),_CwsLineTotalUASsThreshold_Type())
cwsLineTotalUASsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsLineTotalUASsThreshold.setStatus(_A)
_CwsLineStatAlarmStatus_Type=Unsigned32
_CwsLineStatAlarmStatus_Object=MibTableColumn
cwsLineStatAlarmStatus=_CwsLineStatAlarmStatus_Object((1,3,6,1,4,1,351,150,3,1,2,1,1,10),_CwsLineStatAlarmStatus_Type())
cwsLineStatAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLineStatAlarmStatus.setStatus(_A)
_CwsLineCurrent24HrTable_Object=MibTable
cwsLineCurrent24HrTable=_CwsLineCurrent24HrTable_Object((1,3,6,1,4,1,351,150,3,1,2,2))
if mibBuilder.loadTexts:cwsLineCurrent24HrTable.setStatus(_A)
_CwsLineCurrent24HrEntry_Object=MibTableRow
cwsLineCurrent24HrEntry=_CwsLineCurrent24HrEntry_Object((1,3,6,1,4,1,351,150,3,1,2,2,1))
cwsLineCurrent24HrEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cwsLineCurrent24HrEntry.setStatus(_A)
_CwsLineCurrent24HrESs_Type=PerfIntervalCount
_CwsLineCurrent24HrESs_Object=MibTableColumn
cwsLineCurrent24HrESs=_CwsLineCurrent24HrESs_Object((1,3,6,1,4,1,351,150,3,1,2,2,1,1),_CwsLineCurrent24HrESs_Type())
cwsLineCurrent24HrESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLineCurrent24HrESs.setStatus(_A)
_CwsLineCurrent24HrSESs_Type=PerfIntervalCount
_CwsLineCurrent24HrSESs_Object=MibTableColumn
cwsLineCurrent24HrSESs=_CwsLineCurrent24HrSESs_Object((1,3,6,1,4,1,351,150,3,1,2,2,1,2),_CwsLineCurrent24HrSESs_Type())
cwsLineCurrent24HrSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLineCurrent24HrSESs.setStatus(_A)
if mibBuilder.loadTexts:cwsLineCurrent24HrSESs.setUnits(_F)
_CwsLineCurrent24HrCVs_Type=PerfIntervalCount
_CwsLineCurrent24HrCVs_Object=MibTableColumn
cwsLineCurrent24HrCVs=_CwsLineCurrent24HrCVs_Object((1,3,6,1,4,1,351,150,3,1,2,2,1,3),_CwsLineCurrent24HrCVs_Type())
cwsLineCurrent24HrCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLineCurrent24HrCVs.setStatus(_A)
if mibBuilder.loadTexts:cwsLineCurrent24HrCVs.setUnits(_G)
_CwsLineCurrent24HrUASs_Type=PerfIntervalCount
_CwsLineCurrent24HrUASs_Object=MibTableColumn
cwsLineCurrent24HrUASs=_CwsLineCurrent24HrUASs_Object((1,3,6,1,4,1,351,150,3,1,2,2,1,4),_CwsLineCurrent24HrUASs_Type())
cwsLineCurrent24HrUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLineCurrent24HrUASs.setStatus(_A)
if mibBuilder.loadTexts:cwsLineCurrent24HrUASs.setUnits(_J)
_CwsFELineCurrent24HrESs_Type=PerfIntervalCount
_CwsFELineCurrent24HrESs_Object=MibTableColumn
cwsFELineCurrent24HrESs=_CwsFELineCurrent24HrESs_Object((1,3,6,1,4,1,351,150,3,1,2,2,1,5),_CwsFELineCurrent24HrESs_Type())
cwsFELineCurrent24HrESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsFELineCurrent24HrESs.setStatus(_A)
_CwsFELineCurrent24HrSESs_Type=PerfIntervalCount
_CwsFELineCurrent24HrSESs_Object=MibTableColumn
cwsFELineCurrent24HrSESs=_CwsFELineCurrent24HrSESs_Object((1,3,6,1,4,1,351,150,3,1,2,2,1,6),_CwsFELineCurrent24HrSESs_Type())
cwsFELineCurrent24HrSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsFELineCurrent24HrSESs.setStatus(_A)
if mibBuilder.loadTexts:cwsFELineCurrent24HrSESs.setUnits(_F)
_CwsFELineCurrent24HrCVs_Type=PerfIntervalCount
_CwsFELineCurrent24HrCVs_Object=MibTableColumn
cwsFELineCurrent24HrCVs=_CwsFELineCurrent24HrCVs_Object((1,3,6,1,4,1,351,150,3,1,2,2,1,7),_CwsFELineCurrent24HrCVs_Type())
cwsFELineCurrent24HrCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsFELineCurrent24HrCVs.setStatus(_A)
if mibBuilder.loadTexts:cwsFELineCurrent24HrCVs.setUnits(_G)
_CwsFELineCurrent24HrUASs_Type=PerfIntervalCount
_CwsFELineCurrent24HrUASs_Object=MibTableColumn
cwsFELineCurrent24HrUASs=_CwsFELineCurrent24HrUASs_Object((1,3,6,1,4,1,351,150,3,1,2,2,1,8),_CwsFELineCurrent24HrUASs_Type())
cwsFELineCurrent24HrUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsFELineCurrent24HrUASs.setStatus(_A)
if mibBuilder.loadTexts:cwsFELineCurrent24HrUASs.setUnits(_J)
_CwsLinePrevious24HrTable_Object=MibTable
cwsLinePrevious24HrTable=_CwsLinePrevious24HrTable_Object((1,3,6,1,4,1,351,150,3,1,2,3))
if mibBuilder.loadTexts:cwsLinePrevious24HrTable.setStatus(_A)
_CwsLinePrevious24HrEntry_Object=MibTableRow
cwsLinePrevious24HrEntry=_CwsLinePrevious24HrEntry_Object((1,3,6,1,4,1,351,150,3,1,2,3,1))
cwsLinePrevious24HrEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cwsLinePrevious24HrEntry.setStatus(_A)
_CwsLinePrevious24HrESs_Type=PerfIntervalCount
_CwsLinePrevious24HrESs_Object=MibTableColumn
cwsLinePrevious24HrESs=_CwsLinePrevious24HrESs_Object((1,3,6,1,4,1,351,150,3,1,2,3,1,1),_CwsLinePrevious24HrESs_Type())
cwsLinePrevious24HrESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLinePrevious24HrESs.setStatus(_A)
_CwsLinePrevious24HrSESs_Type=PerfIntervalCount
_CwsLinePrevious24HrSESs_Object=MibTableColumn
cwsLinePrevious24HrSESs=_CwsLinePrevious24HrSESs_Object((1,3,6,1,4,1,351,150,3,1,2,3,1,2),_CwsLinePrevious24HrSESs_Type())
cwsLinePrevious24HrSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLinePrevious24HrSESs.setStatus(_A)
if mibBuilder.loadTexts:cwsLinePrevious24HrSESs.setUnits(_F)
_CwsLinePrevious24HrCVs_Type=PerfIntervalCount
_CwsLinePrevious24HrCVs_Object=MibTableColumn
cwsLinePrevious24HrCVs=_CwsLinePrevious24HrCVs_Object((1,3,6,1,4,1,351,150,3,1,2,3,1,3),_CwsLinePrevious24HrCVs_Type())
cwsLinePrevious24HrCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLinePrevious24HrCVs.setStatus(_A)
if mibBuilder.loadTexts:cwsLinePrevious24HrCVs.setUnits(_G)
_CwsLinePrevious24HrUASs_Type=PerfIntervalCount
_CwsLinePrevious24HrUASs_Object=MibTableColumn
cwsLinePrevious24HrUASs=_CwsLinePrevious24HrUASs_Object((1,3,6,1,4,1,351,150,3,1,2,3,1,4),_CwsLinePrevious24HrUASs_Type())
cwsLinePrevious24HrUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLinePrevious24HrUASs.setStatus(_A)
if mibBuilder.loadTexts:cwsLinePrevious24HrUASs.setUnits(_J)
_CwsFELinePrevious24HrESs_Type=PerfIntervalCount
_CwsFELinePrevious24HrESs_Object=MibTableColumn
cwsFELinePrevious24HrESs=_CwsFELinePrevious24HrESs_Object((1,3,6,1,4,1,351,150,3,1,2,3,1,5),_CwsFELinePrevious24HrESs_Type())
cwsFELinePrevious24HrESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsFELinePrevious24HrESs.setStatus(_A)
_CwsFELinePrevious24HrSESs_Type=PerfIntervalCount
_CwsFELinePrevious24HrSESs_Object=MibTableColumn
cwsFELinePrevious24HrSESs=_CwsFELinePrevious24HrSESs_Object((1,3,6,1,4,1,351,150,3,1,2,3,1,6),_CwsFELinePrevious24HrSESs_Type())
cwsFELinePrevious24HrSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsFELinePrevious24HrSESs.setStatus(_A)
if mibBuilder.loadTexts:cwsFELinePrevious24HrSESs.setUnits(_F)
_CwsFELinePrevious24HrCVs_Type=PerfIntervalCount
_CwsFELinePrevious24HrCVs_Object=MibTableColumn
cwsFELinePrevious24HrCVs=_CwsFELinePrevious24HrCVs_Object((1,3,6,1,4,1,351,150,3,1,2,3,1,7),_CwsFELinePrevious24HrCVs_Type())
cwsFELinePrevious24HrCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsFELinePrevious24HrCVs.setStatus(_A)
if mibBuilder.loadTexts:cwsFELinePrevious24HrCVs.setUnits(_G)
_CwsFELinePrevious24HrUASs_Type=PerfIntervalCount
_CwsFELinePrevious24HrUASs_Object=MibTableColumn
cwsFELinePrevious24HrUASs=_CwsFELinePrevious24HrUASs_Object((1,3,6,1,4,1,351,150,3,1,2,3,1,8),_CwsFELinePrevious24HrUASs_Type())
cwsFELinePrevious24HrUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsFELinePrevious24HrUASs.setStatus(_A)
if mibBuilder.loadTexts:cwsFELinePrevious24HrUASs.setUnits(_J)
_CwsPath_ObjectIdentity=ObjectIdentity
cwsPath=_CwsPath_ObjectIdentity((1,3,6,1,4,1,351,150,3,1,3))
_CwsPathAlarmTable_Object=MibTable
cwsPathAlarmTable=_CwsPathAlarmTable_Object((1,3,6,1,4,1,351,150,3,1,3,1))
if mibBuilder.loadTexts:cwsPathAlarmTable.setStatus(_A)
_CwsPathAlarmEntry_Object=MibTableRow
cwsPathAlarmEntry=_CwsPathAlarmEntry_Object((1,3,6,1,4,1,351,150,3,1,3,1,1))
cwsPathAlarmEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cwsPathAlarmEntry.setStatus(_A)
class _CwsPathStatisticalAlarmSeverity_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_CwsPathStatisticalAlarmSeverity_Type.__name__=_K
_CwsPathStatisticalAlarmSeverity_Object=MibTableColumn
cwsPathStatisticalAlarmSeverity=_CwsPathStatisticalAlarmSeverity_Object((1,3,6,1,4,1,351,150,3,1,3,1,1,1),_CwsPathStatisticalAlarmSeverity_Type())
cwsPathStatisticalAlarmSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsPathStatisticalAlarmSeverity.setStatus(_A)
class _CwsPathCurrentESsThreshold_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPathCurrentESsThreshold_Type.__name__=_E
_CwsPathCurrentESsThreshold_Object=MibTableColumn
cwsPathCurrentESsThreshold=_CwsPathCurrentESsThreshold_Object((1,3,6,1,4,1,351,150,3,1,3,1,1,2),_CwsPathCurrentESsThreshold_Type())
cwsPathCurrentESsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsPathCurrentESsThreshold.setStatus(_A)
class _CwsPathTotalESsThreshold_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPathTotalESsThreshold_Type.__name__=_E
_CwsPathTotalESsThreshold_Object=MibTableColumn
cwsPathTotalESsThreshold=_CwsPathTotalESsThreshold_Object((1,3,6,1,4,1,351,150,3,1,3,1,1,3),_CwsPathTotalESsThreshold_Type())
cwsPathTotalESsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsPathTotalESsThreshold.setStatus(_A)
class _CwsPathCurrentSESsThreshold_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPathCurrentSESsThreshold_Type.__name__=_E
_CwsPathCurrentSESsThreshold_Object=MibTableColumn
cwsPathCurrentSESsThreshold=_CwsPathCurrentSESsThreshold_Object((1,3,6,1,4,1,351,150,3,1,3,1,1,4),_CwsPathCurrentSESsThreshold_Type())
cwsPathCurrentSESsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsPathCurrentSESsThreshold.setStatus(_A)
class _CwsPathTotalSESsThreshold_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPathTotalSESsThreshold_Type.__name__=_E
_CwsPathTotalSESsThreshold_Object=MibTableColumn
cwsPathTotalSESsThreshold=_CwsPathTotalSESsThreshold_Object((1,3,6,1,4,1,351,150,3,1,3,1,1,5),_CwsPathTotalSESsThreshold_Type())
cwsPathTotalSESsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsPathTotalSESsThreshold.setStatus(_A)
class _CwsPathCurrentCVsThreshold_Type(Unsigned32):defaultValue=25;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPathCurrentCVsThreshold_Type.__name__=_E
_CwsPathCurrentCVsThreshold_Object=MibTableColumn
cwsPathCurrentCVsThreshold=_CwsPathCurrentCVsThreshold_Object((1,3,6,1,4,1,351,150,3,1,3,1,1,6),_CwsPathCurrentCVsThreshold_Type())
cwsPathCurrentCVsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsPathCurrentCVsThreshold.setStatus(_A)
class _CwsPathTotalCVsThreshold_Type(Unsigned32):defaultValue=25;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPathTotalCVsThreshold_Type.__name__=_E
_CwsPathTotalCVsThreshold_Object=MibTableColumn
cwsPathTotalCVsThreshold=_CwsPathTotalCVsThreshold_Object((1,3,6,1,4,1,351,150,3,1,3,1,1,7),_CwsPathTotalCVsThreshold_Type())
cwsPathTotalCVsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsPathTotalCVsThreshold.setStatus(_A)
class _CwsPathCurrentUASsThreshold_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPathCurrentUASsThreshold_Type.__name__=_E
_CwsPathCurrentUASsThreshold_Object=MibTableColumn
cwsPathCurrentUASsThreshold=_CwsPathCurrentUASsThreshold_Object((1,3,6,1,4,1,351,150,3,1,3,1,1,8),_CwsPathCurrentUASsThreshold_Type())
cwsPathCurrentUASsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsPathCurrentUASsThreshold.setStatus(_A)
class _CwsPathTotalUASsThreshold_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPathTotalUASsThreshold_Type.__name__=_E
_CwsPathTotalUASsThreshold_Object=MibTableColumn
cwsPathTotalUASsThreshold=_CwsPathTotalUASsThreshold_Object((1,3,6,1,4,1,351,150,3,1,3,1,1,9),_CwsPathTotalUASsThreshold_Type())
cwsPathTotalUASsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cwsPathTotalUASsThreshold.setStatus(_A)
_CwsPathStatAlarmStatus_Type=Unsigned32
_CwsPathStatAlarmStatus_Object=MibTableColumn
cwsPathStatAlarmStatus=_CwsPathStatAlarmStatus_Object((1,3,6,1,4,1,351,150,3,1,3,1,1,10),_CwsPathStatAlarmStatus_Type())
cwsPathStatAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPathStatAlarmStatus.setStatus(_A)
_CwsPathCurrent24HrTable_Object=MibTable
cwsPathCurrent24HrTable=_CwsPathCurrent24HrTable_Object((1,3,6,1,4,1,351,150,3,1,3,2))
if mibBuilder.loadTexts:cwsPathCurrent24HrTable.setStatus(_A)
_CwsPathCurrent24HrEntry_Object=MibTableRow
cwsPathCurrent24HrEntry=_CwsPathCurrent24HrEntry_Object((1,3,6,1,4,1,351,150,3,1,3,2,1))
cwsPathCurrent24HrEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cwsPathCurrent24HrEntry.setStatus(_A)
_CwsPathCurrent24HrESs_Type=PerfIntervalCount
_CwsPathCurrent24HrESs_Object=MibTableColumn
cwsPathCurrent24HrESs=_CwsPathCurrent24HrESs_Object((1,3,6,1,4,1,351,150,3,1,3,2,1,1),_CwsPathCurrent24HrESs_Type())
cwsPathCurrent24HrESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPathCurrent24HrESs.setStatus(_A)
_CwsPathCurrent24HrSESs_Type=PerfIntervalCount
_CwsPathCurrent24HrSESs_Object=MibTableColumn
cwsPathCurrent24HrSESs=_CwsPathCurrent24HrSESs_Object((1,3,6,1,4,1,351,150,3,1,3,2,1,2),_CwsPathCurrent24HrSESs_Type())
cwsPathCurrent24HrSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPathCurrent24HrSESs.setStatus(_A)
if mibBuilder.loadTexts:cwsPathCurrent24HrSESs.setUnits(_F)
_CwsPathCurrent24HrCVs_Type=PerfIntervalCount
_CwsPathCurrent24HrCVs_Object=MibTableColumn
cwsPathCurrent24HrCVs=_CwsPathCurrent24HrCVs_Object((1,3,6,1,4,1,351,150,3,1,3,2,1,3),_CwsPathCurrent24HrCVs_Type())
cwsPathCurrent24HrCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPathCurrent24HrCVs.setStatus(_A)
if mibBuilder.loadTexts:cwsPathCurrent24HrCVs.setUnits(_G)
_CwsPathCurrent24HrUASs_Type=PerfIntervalCount
_CwsPathCurrent24HrUASs_Object=MibTableColumn
cwsPathCurrent24HrUASs=_CwsPathCurrent24HrUASs_Object((1,3,6,1,4,1,351,150,3,1,3,2,1,4),_CwsPathCurrent24HrUASs_Type())
cwsPathCurrent24HrUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPathCurrent24HrUASs.setStatus(_A)
if mibBuilder.loadTexts:cwsPathCurrent24HrUASs.setUnits(_J)
_CwsFEPathCurrent24HrESs_Type=PerfIntervalCount
_CwsFEPathCurrent24HrESs_Object=MibTableColumn
cwsFEPathCurrent24HrESs=_CwsFEPathCurrent24HrESs_Object((1,3,6,1,4,1,351,150,3,1,3,2,1,5),_CwsFEPathCurrent24HrESs_Type())
cwsFEPathCurrent24HrESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsFEPathCurrent24HrESs.setStatus(_A)
_CwsFEPathCurrent24HrSESs_Type=PerfIntervalCount
_CwsFEPathCurrent24HrSESs_Object=MibTableColumn
cwsFEPathCurrent24HrSESs=_CwsFEPathCurrent24HrSESs_Object((1,3,6,1,4,1,351,150,3,1,3,2,1,6),_CwsFEPathCurrent24HrSESs_Type())
cwsFEPathCurrent24HrSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsFEPathCurrent24HrSESs.setStatus(_A)
if mibBuilder.loadTexts:cwsFEPathCurrent24HrSESs.setUnits(_F)
_CwsFEPathCurrent24HrCVs_Type=PerfIntervalCount
_CwsFEPathCurrent24HrCVs_Object=MibTableColumn
cwsFEPathCurrent24HrCVs=_CwsFEPathCurrent24HrCVs_Object((1,3,6,1,4,1,351,150,3,1,3,2,1,7),_CwsFEPathCurrent24HrCVs_Type())
cwsFEPathCurrent24HrCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsFEPathCurrent24HrCVs.setStatus(_A)
if mibBuilder.loadTexts:cwsFEPathCurrent24HrCVs.setUnits(_G)
_CwsFEPathCurrent24HrUASs_Type=PerfIntervalCount
_CwsFEPathCurrent24HrUASs_Object=MibTableColumn
cwsFEPathCurrent24HrUASs=_CwsFEPathCurrent24HrUASs_Object((1,3,6,1,4,1,351,150,3,1,3,2,1,8),_CwsFEPathCurrent24HrUASs_Type())
cwsFEPathCurrent24HrUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsFEPathCurrent24HrUASs.setStatus(_A)
if mibBuilder.loadTexts:cwsFEPathCurrent24HrUASs.setUnits(_J)
_CwsPathPrevious24HrTable_Object=MibTable
cwsPathPrevious24HrTable=_CwsPathPrevious24HrTable_Object((1,3,6,1,4,1,351,150,3,1,3,3))
if mibBuilder.loadTexts:cwsPathPrevious24HrTable.setStatus(_A)
_CwsPathPrevious24HrEntry_Object=MibTableRow
cwsPathPrevious24HrEntry=_CwsPathPrevious24HrEntry_Object((1,3,6,1,4,1,351,150,3,1,3,3,1))
cwsPathPrevious24HrEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cwsPathPrevious24HrEntry.setStatus(_A)
_CwsPathPrevious24HrESs_Type=PerfIntervalCount
_CwsPathPrevious24HrESs_Object=MibTableColumn
cwsPathPrevious24HrESs=_CwsPathPrevious24HrESs_Object((1,3,6,1,4,1,351,150,3,1,3,3,1,1),_CwsPathPrevious24HrESs_Type())
cwsPathPrevious24HrESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPathPrevious24HrESs.setStatus(_A)
_CwsPathPrevious24HrSESs_Type=PerfIntervalCount
_CwsPathPrevious24HrSESs_Object=MibTableColumn
cwsPathPrevious24HrSESs=_CwsPathPrevious24HrSESs_Object((1,3,6,1,4,1,351,150,3,1,3,3,1,2),_CwsPathPrevious24HrSESs_Type())
cwsPathPrevious24HrSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPathPrevious24HrSESs.setStatus(_A)
if mibBuilder.loadTexts:cwsPathPrevious24HrSESs.setUnits(_F)
_CwsPathPrevious24HrCVs_Type=PerfIntervalCount
_CwsPathPrevious24HrCVs_Object=MibTableColumn
cwsPathPrevious24HrCVs=_CwsPathPrevious24HrCVs_Object((1,3,6,1,4,1,351,150,3,1,3,3,1,3),_CwsPathPrevious24HrCVs_Type())
cwsPathPrevious24HrCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPathPrevious24HrCVs.setStatus(_A)
if mibBuilder.loadTexts:cwsPathPrevious24HrCVs.setUnits(_G)
_CwsPathPrevious24HrUASs_Type=PerfIntervalCount
_CwsPathPrevious24HrUASs_Object=MibTableColumn
cwsPathPrevious24HrUASs=_CwsPathPrevious24HrUASs_Object((1,3,6,1,4,1,351,150,3,1,3,3,1,4),_CwsPathPrevious24HrUASs_Type())
cwsPathPrevious24HrUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPathPrevious24HrUASs.setStatus(_A)
if mibBuilder.loadTexts:cwsPathPrevious24HrUASs.setUnits(_J)
_CwsFEPathPrevious24HrESs_Type=PerfIntervalCount
_CwsFEPathPrevious24HrESs_Object=MibTableColumn
cwsFEPathPrevious24HrESs=_CwsFEPathPrevious24HrESs_Object((1,3,6,1,4,1,351,150,3,1,3,3,1,5),_CwsFEPathPrevious24HrESs_Type())
cwsFEPathPrevious24HrESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsFEPathPrevious24HrESs.setStatus(_A)
_CwsFEPathPrevious24HrSESs_Type=PerfIntervalCount
_CwsFEPathPrevious24HrSESs_Object=MibTableColumn
cwsFEPathPrevious24HrSESs=_CwsFEPathPrevious24HrSESs_Object((1,3,6,1,4,1,351,150,3,1,3,3,1,6),_CwsFEPathPrevious24HrSESs_Type())
cwsFEPathPrevious24HrSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsFEPathPrevious24HrSESs.setStatus(_A)
if mibBuilder.loadTexts:cwsFEPathPrevious24HrSESs.setUnits(_F)
_CwsFEPathPrevious24HrCVs_Type=PerfIntervalCount
_CwsFEPathPrevious24HrCVs_Object=MibTableColumn
cwsFEPathPrevious24HrCVs=_CwsFEPathPrevious24HrCVs_Object((1,3,6,1,4,1,351,150,3,1,3,3,1,7),_CwsFEPathPrevious24HrCVs_Type())
cwsFEPathPrevious24HrCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsFEPathPrevious24HrCVs.setStatus(_A)
if mibBuilder.loadTexts:cwsFEPathPrevious24HrCVs.setUnits(_G)
_CwsFEPathPrevious24HrUASs_Type=PerfIntervalCount
_CwsFEPathPrevious24HrUASs_Object=MibTableColumn
cwsFEPathPrevious24HrUASs=_CwsFEPathPrevious24HrUASs_Object((1,3,6,1,4,1,351,150,3,1,3,3,1,8),_CwsFEPathPrevious24HrUASs_Type())
cwsFEPathPrevious24HrUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsFEPathPrevious24HrUASs.setStatus(_A)
if mibBuilder.loadTexts:cwsFEPathPrevious24HrUASs.setUnits(_J)
_CiscoWANSonetMIBConformance_ObjectIdentity=ObjectIdentity
ciscoWANSonetMIBConformance=_CiscoWANSonetMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,3,2))
_CiscoWANSonetMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWANSonetMIBCompliances=_CiscoWANSonetMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,3,2,1))
_CiscoWANSonetMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWANSonetMIBGroups=_CiscoWANSonetMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,3,2,2))
ciscoWANSonetSectAlarmMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,3,2,2,1))
ciscoWANSonetSectAlarmMIBGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:ciscoWANSonetSectAlarmMIBGroup.setStatus(_A)
ciscoWANSonetSectPrev24HrMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,3,2,2,2))
ciscoWANSonetSectPrev24HrMIBGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ciscoWANSonetSectPrev24HrMIBGroup.setStatus(_A)
ciscoWANSonetLineAlarmMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,3,2,2,3))
ciscoWANSonetLineAlarmMIBGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:ciscoWANSonetLineAlarmMIBGroup.setStatus(_A)
ciscoWANSonetFELineAlarmMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,3,2,2,4))
ciscoWANSonetFELineAlarmMIBGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:ciscoWANSonetFELineAlarmMIBGroup.setStatus(_A)
ciscoWANSonetLinePrev24HrMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,3,2,2,5))
ciscoWANSonetLinePrev24HrMIBGroup.setObjects(*((_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:ciscoWANSonetLinePrev24HrMIBGroup.setStatus(_A)
ciscoWANSonetFELinePrev24HrMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,3,2,2,6))
ciscoWANSonetFELinePrev24HrMIBGroup.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:ciscoWANSonetFELinePrev24HrMIBGroup.setStatus(_A)
ciscoWANSonetPathAlarmMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,3,2,2,7))
ciscoWANSonetPathAlarmMIBGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:ciscoWANSonetPathAlarmMIBGroup.setStatus(_A)
ciscoWANSonetFEPathAlarmMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,3,2,2,8))
ciscoWANSonetFEPathAlarmMIBGroup.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:ciscoWANSonetFEPathAlarmMIBGroup.setStatus(_A)
ciscoWANSonetPathPrev24HrMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,3,2,2,9))
ciscoWANSonetPathPrev24HrMIBGroup.setObjects(*((_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:ciscoWANSonetPathPrev24HrMIBGroup.setStatus(_A)
ciscoWANSonetFEPathPrev24HrMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,3,2,2,10))
ciscoWANSonetFEPathPrev24HrMIBGroup.setObjects(*((_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:ciscoWANSonetFEPathPrev24HrMIBGroup.setStatus(_A)
ciscoWANSonetMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,3,2,1,1))
ciscoWANSonetMIBCompliance.setObjects(*((_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af)))
if mibBuilder.loadTexts:ciscoWANSonetMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWANSonetMIB':ciscoWANSonetMIB,'ciscoWANSonetMIBObjects':ciscoWANSonetMIBObjects,'cwsSection':cwsSection,'cwsSectionAlarmTable':cwsSectionAlarmTable,'cwsSectionAlarmEntry':cwsSectionAlarmEntry,_P:cwsSectionStatisticalAlarmSeverity,_Q:cwsSectionCurrentESsThreshold,_R:cwsSectionTotalESsThreshold,_S:cwsSectionCurrentSESsThreshold,_T:cwsSectionTotalSESsThreshold,_U:cwsSectionCurrentSEFSsThreshold,_V:cwsSectionTotalSEFSsThreshold,_W:cwsSectionCurrentCVsThreshold,_X:cwsSectionTotalCVsThreshold,_Y:cwsSectionStatAlarmStatus,'cwsSectionCurrent24HrTable':cwsSectionCurrent24HrTable,'cwsSectionCurrent24HrEntry':cwsSectionCurrent24HrEntry,_Z:cwsSectionCurrent24HrESs,_a:cwsSectionCurrent24HrSESs,_b:cwsSectionCurrent24HrSEFSs,_c:cwsSectionCurrent24HrCVs,'cwsSectionPrevious24HrTable':cwsSectionPrevious24HrTable,'cwsSectionPrevious24HrEntry':cwsSectionPrevious24HrEntry,_d:cwsSectionPrevious24HrESs,_e:cwsSectionPrevious24HrSESs,_f:cwsSectionPrevious24HrSEFSs,_g:cwsSectionPrevious24HrCVs,'cwsLine':cwsLine,'cwsLineAlarmTable':cwsLineAlarmTable,'cwsLineAlarmEntry':cwsLineAlarmEntry,_h:cwsLineStatisticalAlarmSeverity,_i:cwsLineCurrentESsThreshold,_j:cwsLineTotalESsThreshold,_k:cwsLineCurrentSESsThreshold,_l:cwsLineTotalSESsThreshold,_m:cwsLineCurrentCVsThreshold,_n:cwsLineTotalCVsThreshold,_o:cwsLineCurrentUASsThreshold,_p:cwsLineTotalUASsThreshold,_q:cwsLineStatAlarmStatus,'cwsLineCurrent24HrTable':cwsLineCurrent24HrTable,'cwsLineCurrent24HrEntry':cwsLineCurrent24HrEntry,_r:cwsLineCurrent24HrESs,_s:cwsLineCurrent24HrSESs,_t:cwsLineCurrent24HrCVs,_u:cwsLineCurrent24HrUASs,_v:cwsFELineCurrent24HrESs,_w:cwsFELineCurrent24HrSESs,_x:cwsFELineCurrent24HrCVs,_y:cwsFELineCurrent24HrUASs,'cwsLinePrevious24HrTable':cwsLinePrevious24HrTable,'cwsLinePrevious24HrEntry':cwsLinePrevious24HrEntry,_z:cwsLinePrevious24HrESs,_A0:cwsLinePrevious24HrSESs,_A1:cwsLinePrevious24HrCVs,_A2:cwsLinePrevious24HrUASs,_A3:cwsFELinePrevious24HrESs,_A4:cwsFELinePrevious24HrSESs,_A5:cwsFELinePrevious24HrCVs,_A6:cwsFELinePrevious24HrUASs,'cwsPath':cwsPath,'cwsPathAlarmTable':cwsPathAlarmTable,'cwsPathAlarmEntry':cwsPathAlarmEntry,_A7:cwsPathStatisticalAlarmSeverity,_A8:cwsPathCurrentESsThreshold,_A9:cwsPathTotalESsThreshold,_AA:cwsPathCurrentSESsThreshold,_AB:cwsPathTotalSESsThreshold,_AC:cwsPathCurrentCVsThreshold,_AD:cwsPathTotalCVsThreshold,_AE:cwsPathCurrentUASsThreshold,_AF:cwsPathTotalUASsThreshold,_AG:cwsPathStatAlarmStatus,'cwsPathCurrent24HrTable':cwsPathCurrent24HrTable,'cwsPathCurrent24HrEntry':cwsPathCurrent24HrEntry,_AH:cwsPathCurrent24HrESs,_AI:cwsPathCurrent24HrSESs,_AJ:cwsPathCurrent24HrCVs,_AK:cwsPathCurrent24HrUASs,_AL:cwsFEPathCurrent24HrESs,_AM:cwsFEPathCurrent24HrSESs,_AN:cwsFEPathCurrent24HrCVs,_AO:cwsFEPathCurrent24HrUASs,'cwsPathPrevious24HrTable':cwsPathPrevious24HrTable,'cwsPathPrevious24HrEntry':cwsPathPrevious24HrEntry,_AP:cwsPathPrevious24HrESs,_AQ:cwsPathPrevious24HrSESs,_AR:cwsPathPrevious24HrCVs,_AS:cwsPathPrevious24HrUASs,_AT:cwsFEPathPrevious24HrESs,_AU:cwsFEPathPrevious24HrSESs,_AV:cwsFEPathPrevious24HrCVs,_AW:cwsFEPathPrevious24HrUASs,'ciscoWANSonetMIBConformance':ciscoWANSonetMIBConformance,'ciscoWANSonetMIBCompliances':ciscoWANSonetMIBCompliances,'ciscoWANSonetMIBCompliance':ciscoWANSonetMIBCompliance,'ciscoWANSonetMIBGroups':ciscoWANSonetMIBGroups,_AX:ciscoWANSonetSectAlarmMIBGroup,'ciscoWANSonetSectPrev24HrMIBGroup':ciscoWANSonetSectPrev24HrMIBGroup,_AY:ciscoWANSonetLineAlarmMIBGroup,_Ab:ciscoWANSonetFELineAlarmMIBGroup,_Aa:ciscoWANSonetLinePrev24HrMIBGroup,_Ac:ciscoWANSonetFELinePrev24HrMIBGroup,_AZ:ciscoWANSonetPathAlarmMIBGroup,_Ae:ciscoWANSonetFEPathAlarmMIBGroup,_Ad:ciscoWANSonetPathPrev24HrMIBGroup,_Af:ciscoWANSonetFEPathPrev24HrMIBGroup})