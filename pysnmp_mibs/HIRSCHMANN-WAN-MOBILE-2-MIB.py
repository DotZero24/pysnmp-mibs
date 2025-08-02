_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmWanMgmt,=mibBuilder.importSymbols('HIRSCHMANN-WAN-MIB','hmWanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hmWanMobile2Mib=ModuleIdentity((1,3,6,1,4,1,248,40,1,5))
if mibBuilder.loadTexts:hmWanMobile2Mib.setRevisions(('2015-02-13 00:00',))
_HmWanMobileToday_ObjectIdentity=ObjectIdentity
hmWanMobileToday=_HmWanMobileToday_ObjectIdentity((1,3,6,1,4,1,248,40,1,5,1))
_HmWanMobileTodayRxPri_Type=Counter32
_HmWanMobileTodayRxPri_Object=MibScalar
hmWanMobileTodayRxPri=_HmWanMobileTodayRxPri_Object((1,3,6,1,4,1,248,40,1,5,1,1),_HmWanMobileTodayRxPri_Type())
hmWanMobileTodayRxPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileTodayRxPri.setStatus(_B)
_HmWanMobileTodayRxSec_Type=Counter32
_HmWanMobileTodayRxSec_Object=MibScalar
hmWanMobileTodayRxSec=_HmWanMobileTodayRxSec_Object((1,3,6,1,4,1,248,40,1,5,1,2),_HmWanMobileTodayRxSec_Type())
hmWanMobileTodayRxSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileTodayRxSec.setStatus(_B)
_HmWanMobileTodayTxPri_Type=Counter32
_HmWanMobileTodayTxPri_Object=MibScalar
hmWanMobileTodayTxPri=_HmWanMobileTodayTxPri_Object((1,3,6,1,4,1,248,40,1,5,1,3),_HmWanMobileTodayTxPri_Type())
hmWanMobileTodayTxPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileTodayTxPri.setStatus(_B)
_HmWanMobileTodayTxSec_Type=Counter32
_HmWanMobileTodayTxSec_Object=MibScalar
hmWanMobileTodayTxSec=_HmWanMobileTodayTxSec_Object((1,3,6,1,4,1,248,40,1,5,1,4),_HmWanMobileTodayTxSec_Type())
hmWanMobileTodayTxSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileTodayTxSec.setStatus(_B)
_HmWanMobileTodayConnectionsPri_Type=Counter32
_HmWanMobileTodayConnectionsPri_Object=MibScalar
hmWanMobileTodayConnectionsPri=_HmWanMobileTodayConnectionsPri_Object((1,3,6,1,4,1,248,40,1,5,1,5),_HmWanMobileTodayConnectionsPri_Type())
hmWanMobileTodayConnectionsPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileTodayConnectionsPri.setStatus(_B)
_HmWanMobileTodayConnectionsSec_Type=Counter32
_HmWanMobileTodayConnectionsSec_Object=MibScalar
hmWanMobileTodayConnectionsSec=_HmWanMobileTodayConnectionsSec_Object((1,3,6,1,4,1,248,40,1,5,1,6),_HmWanMobileTodayConnectionsSec_Type())
hmWanMobileTodayConnectionsSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileTodayConnectionsSec.setStatus(_B)
_HmWanMobileTodayOnlinePri_Type=TimeTicks
_HmWanMobileTodayOnlinePri_Object=MibScalar
hmWanMobileTodayOnlinePri=_HmWanMobileTodayOnlinePri_Object((1,3,6,1,4,1,248,40,1,5,1,7),_HmWanMobileTodayOnlinePri_Type())
hmWanMobileTodayOnlinePri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileTodayOnlinePri.setStatus(_B)
_HmWanMobileTodayOnlineSec_Type=TimeTicks
_HmWanMobileTodayOnlineSec_Object=MibScalar
hmWanMobileTodayOnlineSec=_HmWanMobileTodayOnlineSec_Object((1,3,6,1,4,1,248,40,1,5,1,8),_HmWanMobileTodayOnlineSec_Type())
hmWanMobileTodayOnlineSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileTodayOnlineSec.setStatus(_B)
_HmWanMobileTodayOffline_Type=TimeTicks
_HmWanMobileTodayOffline_Object=MibScalar
hmWanMobileTodayOffline=_HmWanMobileTodayOffline_Object((1,3,6,1,4,1,248,40,1,5,1,9),_HmWanMobileTodayOffline_Type())
hmWanMobileTodayOffline.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileTodayOffline.setStatus(_B)
_HmWanMobileTodayCells_Type=Counter32
_HmWanMobileTodayCells_Object=MibScalar
hmWanMobileTodayCells=_HmWanMobileTodayCells_Object((1,3,6,1,4,1,248,40,1,5,1,10),_HmWanMobileTodayCells_Type())
hmWanMobileTodayCells.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileTodayCells.setStatus(_B)
_HmWanMobileTodaySignalAvg_Type=Integer32
_HmWanMobileTodaySignalAvg_Object=MibScalar
hmWanMobileTodaySignalAvg=_HmWanMobileTodaySignalAvg_Object((1,3,6,1,4,1,248,40,1,5,1,11),_HmWanMobileTodaySignalAvg_Type())
hmWanMobileTodaySignalAvg.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileTodaySignalAvg.setStatus(_B)
_HmWanMobileTodaySignalMin_Type=Integer32
_HmWanMobileTodaySignalMin_Object=MibScalar
hmWanMobileTodaySignalMin=_HmWanMobileTodaySignalMin_Object((1,3,6,1,4,1,248,40,1,5,1,12),_HmWanMobileTodaySignalMin_Type())
hmWanMobileTodaySignalMin.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileTodaySignalMin.setStatus(_B)
_HmWanMobileTodaySignalMax_Type=Integer32
_HmWanMobileTodaySignalMax_Object=MibScalar
hmWanMobileTodaySignalMax=_HmWanMobileTodaySignalMax_Object((1,3,6,1,4,1,248,40,1,5,1,13),_HmWanMobileTodaySignalMax_Type())
hmWanMobileTodaySignalMax.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileTodaySignalMax.setStatus(_B)
_HmWanMobileTodayDateMin_Type=Counter32
_HmWanMobileTodayDateMin_Object=MibScalar
hmWanMobileTodayDateMin=_HmWanMobileTodayDateMin_Object((1,3,6,1,4,1,248,40,1,5,1,14),_HmWanMobileTodayDateMin_Type())
hmWanMobileTodayDateMin.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileTodayDateMin.setStatus(_B)
_HmWanMobileTodayDateMax_Type=Counter32
_HmWanMobileTodayDateMax_Object=MibScalar
hmWanMobileTodayDateMax=_HmWanMobileTodayDateMax_Object((1,3,6,1,4,1,248,40,1,5,1,15),_HmWanMobileTodayDateMax_Type())
hmWanMobileTodayDateMax.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileTodayDateMax.setStatus(_B)
_HmWanMobileYesterday_ObjectIdentity=ObjectIdentity
hmWanMobileYesterday=_HmWanMobileYesterday_ObjectIdentity((1,3,6,1,4,1,248,40,1,5,2))
_HmWanMobileYesterdayRxPri_Type=Counter32
_HmWanMobileYesterdayRxPri_Object=MibScalar
hmWanMobileYesterdayRxPri=_HmWanMobileYesterdayRxPri_Object((1,3,6,1,4,1,248,40,1,5,2,1),_HmWanMobileYesterdayRxPri_Type())
hmWanMobileYesterdayRxPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileYesterdayRxPri.setStatus(_B)
_HmWanMobileYesterdayRxSec_Type=Counter32
_HmWanMobileYesterdayRxSec_Object=MibScalar
hmWanMobileYesterdayRxSec=_HmWanMobileYesterdayRxSec_Object((1,3,6,1,4,1,248,40,1,5,2,2),_HmWanMobileYesterdayRxSec_Type())
hmWanMobileYesterdayRxSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileYesterdayRxSec.setStatus(_B)
_HmWanMobileYesterdayTxPri_Type=Counter32
_HmWanMobileYesterdayTxPri_Object=MibScalar
hmWanMobileYesterdayTxPri=_HmWanMobileYesterdayTxPri_Object((1,3,6,1,4,1,248,40,1,5,2,3),_HmWanMobileYesterdayTxPri_Type())
hmWanMobileYesterdayTxPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileYesterdayTxPri.setStatus(_B)
_HmWanMobileYesterdayTxSec_Type=Counter32
_HmWanMobileYesterdayTxSec_Object=MibScalar
hmWanMobileYesterdayTxSec=_HmWanMobileYesterdayTxSec_Object((1,3,6,1,4,1,248,40,1,5,2,4),_HmWanMobileYesterdayTxSec_Type())
hmWanMobileYesterdayTxSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileYesterdayTxSec.setStatus(_B)
_HmWanMobileYesterdayConnectionsPri_Type=Counter32
_HmWanMobileYesterdayConnectionsPri_Object=MibScalar
hmWanMobileYesterdayConnectionsPri=_HmWanMobileYesterdayConnectionsPri_Object((1,3,6,1,4,1,248,40,1,5,2,5),_HmWanMobileYesterdayConnectionsPri_Type())
hmWanMobileYesterdayConnectionsPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileYesterdayConnectionsPri.setStatus(_B)
_HmWanMobileYesterdayConnectionsSec_Type=Counter32
_HmWanMobileYesterdayConnectionsSec_Object=MibScalar
hmWanMobileYesterdayConnectionsSec=_HmWanMobileYesterdayConnectionsSec_Object((1,3,6,1,4,1,248,40,1,5,2,6),_HmWanMobileYesterdayConnectionsSec_Type())
hmWanMobileYesterdayConnectionsSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileYesterdayConnectionsSec.setStatus(_B)
_HmWanMobileYesterdayOnlinePri_Type=TimeTicks
_HmWanMobileYesterdayOnlinePri_Object=MibScalar
hmWanMobileYesterdayOnlinePri=_HmWanMobileYesterdayOnlinePri_Object((1,3,6,1,4,1,248,40,1,5,2,7),_HmWanMobileYesterdayOnlinePri_Type())
hmWanMobileYesterdayOnlinePri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileYesterdayOnlinePri.setStatus(_B)
_HmWanMobileYesterdayOnlineSec_Type=TimeTicks
_HmWanMobileYesterdayOnlineSec_Object=MibScalar
hmWanMobileYesterdayOnlineSec=_HmWanMobileYesterdayOnlineSec_Object((1,3,6,1,4,1,248,40,1,5,2,8),_HmWanMobileYesterdayOnlineSec_Type())
hmWanMobileYesterdayOnlineSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileYesterdayOnlineSec.setStatus(_B)
_HmWanMobileYesterdayOffline_Type=TimeTicks
_HmWanMobileYesterdayOffline_Object=MibScalar
hmWanMobileYesterdayOffline=_HmWanMobileYesterdayOffline_Object((1,3,6,1,4,1,248,40,1,5,2,9),_HmWanMobileYesterdayOffline_Type())
hmWanMobileYesterdayOffline.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileYesterdayOffline.setStatus(_B)
_HmWanMobileYesterdayCells_Type=Counter32
_HmWanMobileYesterdayCells_Object=MibScalar
hmWanMobileYesterdayCells=_HmWanMobileYesterdayCells_Object((1,3,6,1,4,1,248,40,1,5,2,10),_HmWanMobileYesterdayCells_Type())
hmWanMobileYesterdayCells.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileYesterdayCells.setStatus(_B)
_HmWanMobileYesterdaySignalAvg_Type=Integer32
_HmWanMobileYesterdaySignalAvg_Object=MibScalar
hmWanMobileYesterdaySignalAvg=_HmWanMobileYesterdaySignalAvg_Object((1,3,6,1,4,1,248,40,1,5,2,11),_HmWanMobileYesterdaySignalAvg_Type())
hmWanMobileYesterdaySignalAvg.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileYesterdaySignalAvg.setStatus(_B)
_HmWanMobileYesterdaySignalMin_Type=Integer32
_HmWanMobileYesterdaySignalMin_Object=MibScalar
hmWanMobileYesterdaySignalMin=_HmWanMobileYesterdaySignalMin_Object((1,3,6,1,4,1,248,40,1,5,2,12),_HmWanMobileYesterdaySignalMin_Type())
hmWanMobileYesterdaySignalMin.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileYesterdaySignalMin.setStatus(_B)
_HmWanMobileYesterdaySignalMax_Type=Integer32
_HmWanMobileYesterdaySignalMax_Object=MibScalar
hmWanMobileYesterdaySignalMax=_HmWanMobileYesterdaySignalMax_Object((1,3,6,1,4,1,248,40,1,5,2,13),_HmWanMobileYesterdaySignalMax_Type())
hmWanMobileYesterdaySignalMax.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileYesterdaySignalMax.setStatus(_B)
_HmWanMobileYesterdayDateMin_Type=Counter32
_HmWanMobileYesterdayDateMin_Object=MibScalar
hmWanMobileYesterdayDateMin=_HmWanMobileYesterdayDateMin_Object((1,3,6,1,4,1,248,40,1,5,2,14),_HmWanMobileYesterdayDateMin_Type())
hmWanMobileYesterdayDateMin.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileYesterdayDateMin.setStatus(_B)
_HmWanMobileYesterdayDateMax_Type=Counter32
_HmWanMobileYesterdayDateMax_Object=MibScalar
hmWanMobileYesterdayDateMax=_HmWanMobileYesterdayDateMax_Object((1,3,6,1,4,1,248,40,1,5,2,15),_HmWanMobileYesterdayDateMax_Type())
hmWanMobileYesterdayDateMax.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileYesterdayDateMax.setStatus(_B)
_HmWanMobileThisWeek_ObjectIdentity=ObjectIdentity
hmWanMobileThisWeek=_HmWanMobileThisWeek_ObjectIdentity((1,3,6,1,4,1,248,40,1,5,3))
_HmWanMobileThisWeekRxPri_Type=Counter32
_HmWanMobileThisWeekRxPri_Object=MibScalar
hmWanMobileThisWeekRxPri=_HmWanMobileThisWeekRxPri_Object((1,3,6,1,4,1,248,40,1,5,3,1),_HmWanMobileThisWeekRxPri_Type())
hmWanMobileThisWeekRxPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisWeekRxPri.setStatus(_B)
_HmWanMobileThisWeekRxSec_Type=Counter32
_HmWanMobileThisWeekRxSec_Object=MibScalar
hmWanMobileThisWeekRxSec=_HmWanMobileThisWeekRxSec_Object((1,3,6,1,4,1,248,40,1,5,3,2),_HmWanMobileThisWeekRxSec_Type())
hmWanMobileThisWeekRxSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisWeekRxSec.setStatus(_B)
_HmWanMobileThisWeekTxPri_Type=Counter32
_HmWanMobileThisWeekTxPri_Object=MibScalar
hmWanMobileThisWeekTxPri=_HmWanMobileThisWeekTxPri_Object((1,3,6,1,4,1,248,40,1,5,3,3),_HmWanMobileThisWeekTxPri_Type())
hmWanMobileThisWeekTxPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisWeekTxPri.setStatus(_B)
_HmWanMobileThisWeekTxSec_Type=Counter32
_HmWanMobileThisWeekTxSec_Object=MibScalar
hmWanMobileThisWeekTxSec=_HmWanMobileThisWeekTxSec_Object((1,3,6,1,4,1,248,40,1,5,3,4),_HmWanMobileThisWeekTxSec_Type())
hmWanMobileThisWeekTxSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisWeekTxSec.setStatus(_B)
_HmWanMobileThisWeekConnectionsPri_Type=Counter32
_HmWanMobileThisWeekConnectionsPri_Object=MibScalar
hmWanMobileThisWeekConnectionsPri=_HmWanMobileThisWeekConnectionsPri_Object((1,3,6,1,4,1,248,40,1,5,3,5),_HmWanMobileThisWeekConnectionsPri_Type())
hmWanMobileThisWeekConnectionsPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisWeekConnectionsPri.setStatus(_B)
_HmWanMobileThisWeekConnectionsSec_Type=Counter32
_HmWanMobileThisWeekConnectionsSec_Object=MibScalar
hmWanMobileThisWeekConnectionsSec=_HmWanMobileThisWeekConnectionsSec_Object((1,3,6,1,4,1,248,40,1,5,3,6),_HmWanMobileThisWeekConnectionsSec_Type())
hmWanMobileThisWeekConnectionsSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisWeekConnectionsSec.setStatus(_B)
_HmWanMobileThisWeekOnlinePri_Type=TimeTicks
_HmWanMobileThisWeekOnlinePri_Object=MibScalar
hmWanMobileThisWeekOnlinePri=_HmWanMobileThisWeekOnlinePri_Object((1,3,6,1,4,1,248,40,1,5,3,7),_HmWanMobileThisWeekOnlinePri_Type())
hmWanMobileThisWeekOnlinePri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisWeekOnlinePri.setStatus(_B)
_HmWanMobileThisWeekOnlineSec_Type=TimeTicks
_HmWanMobileThisWeekOnlineSec_Object=MibScalar
hmWanMobileThisWeekOnlineSec=_HmWanMobileThisWeekOnlineSec_Object((1,3,6,1,4,1,248,40,1,5,3,8),_HmWanMobileThisWeekOnlineSec_Type())
hmWanMobileThisWeekOnlineSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisWeekOnlineSec.setStatus(_B)
_HmWanMobileThisWeekOffline_Type=TimeTicks
_HmWanMobileThisWeekOffline_Object=MibScalar
hmWanMobileThisWeekOffline=_HmWanMobileThisWeekOffline_Object((1,3,6,1,4,1,248,40,1,5,3,9),_HmWanMobileThisWeekOffline_Type())
hmWanMobileThisWeekOffline.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisWeekOffline.setStatus(_B)
_HmWanMobileThisWeekCells_Type=Counter32
_HmWanMobileThisWeekCells_Object=MibScalar
hmWanMobileThisWeekCells=_HmWanMobileThisWeekCells_Object((1,3,6,1,4,1,248,40,1,5,3,10),_HmWanMobileThisWeekCells_Type())
hmWanMobileThisWeekCells.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisWeekCells.setStatus(_B)
_HmWanMobileThisWeekSignalAvg_Type=Integer32
_HmWanMobileThisWeekSignalAvg_Object=MibScalar
hmWanMobileThisWeekSignalAvg=_HmWanMobileThisWeekSignalAvg_Object((1,3,6,1,4,1,248,40,1,5,3,11),_HmWanMobileThisWeekSignalAvg_Type())
hmWanMobileThisWeekSignalAvg.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisWeekSignalAvg.setStatus(_B)
_HmWanMobileThisWeekSignalMin_Type=Integer32
_HmWanMobileThisWeekSignalMin_Object=MibScalar
hmWanMobileThisWeekSignalMin=_HmWanMobileThisWeekSignalMin_Object((1,3,6,1,4,1,248,40,1,5,3,12),_HmWanMobileThisWeekSignalMin_Type())
hmWanMobileThisWeekSignalMin.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisWeekSignalMin.setStatus(_B)
_HmWanMobileThisWeekSignalMax_Type=Integer32
_HmWanMobileThisWeekSignalMax_Object=MibScalar
hmWanMobileThisWeekSignalMax=_HmWanMobileThisWeekSignalMax_Object((1,3,6,1,4,1,248,40,1,5,3,13),_HmWanMobileThisWeekSignalMax_Type())
hmWanMobileThisWeekSignalMax.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisWeekSignalMax.setStatus(_B)
_HmWanMobileThisWeekDateMin_Type=Counter32
_HmWanMobileThisWeekDateMin_Object=MibScalar
hmWanMobileThisWeekDateMin=_HmWanMobileThisWeekDateMin_Object((1,3,6,1,4,1,248,40,1,5,3,14),_HmWanMobileThisWeekDateMin_Type())
hmWanMobileThisWeekDateMin.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisWeekDateMin.setStatus(_B)
_HmWanMobileThisWeekDateMax_Type=Counter32
_HmWanMobileThisWeekDateMax_Object=MibScalar
hmWanMobileThisWeekDateMax=_HmWanMobileThisWeekDateMax_Object((1,3,6,1,4,1,248,40,1,5,3,15),_HmWanMobileThisWeekDateMax_Type())
hmWanMobileThisWeekDateMax.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisWeekDateMax.setStatus(_B)
_HmWanMobileLastWeek_ObjectIdentity=ObjectIdentity
hmWanMobileLastWeek=_HmWanMobileLastWeek_ObjectIdentity((1,3,6,1,4,1,248,40,1,5,4))
_HmWanMobileLastWeekRxPri_Type=Counter32
_HmWanMobileLastWeekRxPri_Object=MibScalar
hmWanMobileLastWeekRxPri=_HmWanMobileLastWeekRxPri_Object((1,3,6,1,4,1,248,40,1,5,4,1),_HmWanMobileLastWeekRxPri_Type())
hmWanMobileLastWeekRxPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastWeekRxPri.setStatus(_B)
_HmWanMobileLastWeekRxSec_Type=Counter32
_HmWanMobileLastWeekRxSec_Object=MibScalar
hmWanMobileLastWeekRxSec=_HmWanMobileLastWeekRxSec_Object((1,3,6,1,4,1,248,40,1,5,4,2),_HmWanMobileLastWeekRxSec_Type())
hmWanMobileLastWeekRxSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastWeekRxSec.setStatus(_B)
_HmWanMobileLastWeekTxPri_Type=Counter32
_HmWanMobileLastWeekTxPri_Object=MibScalar
hmWanMobileLastWeekTxPri=_HmWanMobileLastWeekTxPri_Object((1,3,6,1,4,1,248,40,1,5,4,3),_HmWanMobileLastWeekTxPri_Type())
hmWanMobileLastWeekTxPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastWeekTxPri.setStatus(_B)
_HmWanMobileLastWeekTxSec_Type=Counter32
_HmWanMobileLastWeekTxSec_Object=MibScalar
hmWanMobileLastWeekTxSec=_HmWanMobileLastWeekTxSec_Object((1,3,6,1,4,1,248,40,1,5,4,4),_HmWanMobileLastWeekTxSec_Type())
hmWanMobileLastWeekTxSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastWeekTxSec.setStatus(_B)
_HmWanMobileLastWeekConnectionsPri_Type=Counter32
_HmWanMobileLastWeekConnectionsPri_Object=MibScalar
hmWanMobileLastWeekConnectionsPri=_HmWanMobileLastWeekConnectionsPri_Object((1,3,6,1,4,1,248,40,1,5,4,5),_HmWanMobileLastWeekConnectionsPri_Type())
hmWanMobileLastWeekConnectionsPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastWeekConnectionsPri.setStatus(_B)
_HmWanMobileLastWeekConnectionsSec_Type=Counter32
_HmWanMobileLastWeekConnectionsSec_Object=MibScalar
hmWanMobileLastWeekConnectionsSec=_HmWanMobileLastWeekConnectionsSec_Object((1,3,6,1,4,1,248,40,1,5,4,6),_HmWanMobileLastWeekConnectionsSec_Type())
hmWanMobileLastWeekConnectionsSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastWeekConnectionsSec.setStatus(_B)
_HmWanMobileLastWeekOnlinePri_Type=TimeTicks
_HmWanMobileLastWeekOnlinePri_Object=MibScalar
hmWanMobileLastWeekOnlinePri=_HmWanMobileLastWeekOnlinePri_Object((1,3,6,1,4,1,248,40,1,5,4,7),_HmWanMobileLastWeekOnlinePri_Type())
hmWanMobileLastWeekOnlinePri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastWeekOnlinePri.setStatus(_B)
_HmWanMobileLastWeekOnlineSec_Type=TimeTicks
_HmWanMobileLastWeekOnlineSec_Object=MibScalar
hmWanMobileLastWeekOnlineSec=_HmWanMobileLastWeekOnlineSec_Object((1,3,6,1,4,1,248,40,1,5,4,8),_HmWanMobileLastWeekOnlineSec_Type())
hmWanMobileLastWeekOnlineSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastWeekOnlineSec.setStatus(_B)
_HmWanMobileLastWeekOffline_Type=TimeTicks
_HmWanMobileLastWeekOffline_Object=MibScalar
hmWanMobileLastWeekOffline=_HmWanMobileLastWeekOffline_Object((1,3,6,1,4,1,248,40,1,5,4,9),_HmWanMobileLastWeekOffline_Type())
hmWanMobileLastWeekOffline.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastWeekOffline.setStatus(_B)
_HmWanMobileLastWeekCells_Type=Counter32
_HmWanMobileLastWeekCells_Object=MibScalar
hmWanMobileLastWeekCells=_HmWanMobileLastWeekCells_Object((1,3,6,1,4,1,248,40,1,5,4,10),_HmWanMobileLastWeekCells_Type())
hmWanMobileLastWeekCells.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastWeekCells.setStatus(_B)
_HmWanMobileLastWeekSignalAvg_Type=Integer32
_HmWanMobileLastWeekSignalAvg_Object=MibScalar
hmWanMobileLastWeekSignalAvg=_HmWanMobileLastWeekSignalAvg_Object((1,3,6,1,4,1,248,40,1,5,4,11),_HmWanMobileLastWeekSignalAvg_Type())
hmWanMobileLastWeekSignalAvg.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastWeekSignalAvg.setStatus(_B)
_HmWanMobileLastWeekSignalMin_Type=Integer32
_HmWanMobileLastWeekSignalMin_Object=MibScalar
hmWanMobileLastWeekSignalMin=_HmWanMobileLastWeekSignalMin_Object((1,3,6,1,4,1,248,40,1,5,4,12),_HmWanMobileLastWeekSignalMin_Type())
hmWanMobileLastWeekSignalMin.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastWeekSignalMin.setStatus(_B)
_HmWanMobileLastWeekSignalMax_Type=Integer32
_HmWanMobileLastWeekSignalMax_Object=MibScalar
hmWanMobileLastWeekSignalMax=_HmWanMobileLastWeekSignalMax_Object((1,3,6,1,4,1,248,40,1,5,4,13),_HmWanMobileLastWeekSignalMax_Type())
hmWanMobileLastWeekSignalMax.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastWeekSignalMax.setStatus(_B)
_HmWanMobileLastWeekDateMin_Type=Counter32
_HmWanMobileLastWeekDateMin_Object=MibScalar
hmWanMobileLastWeekDateMin=_HmWanMobileLastWeekDateMin_Object((1,3,6,1,4,1,248,40,1,5,4,14),_HmWanMobileLastWeekDateMin_Type())
hmWanMobileLastWeekDateMin.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastWeekDateMin.setStatus(_B)
_HmWanMobileLastWeekDateMax_Type=Counter32
_HmWanMobileLastWeekDateMax_Object=MibScalar
hmWanMobileLastWeekDateMax=_HmWanMobileLastWeekDateMax_Object((1,3,6,1,4,1,248,40,1,5,4,15),_HmWanMobileLastWeekDateMax_Type())
hmWanMobileLastWeekDateMax.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastWeekDateMax.setStatus(_B)
_HmWanMobileThisPeriod_ObjectIdentity=ObjectIdentity
hmWanMobileThisPeriod=_HmWanMobileThisPeriod_ObjectIdentity((1,3,6,1,4,1,248,40,1,5,5))
_HmWanMobileThisPeriodRxPri_Type=Counter32
_HmWanMobileThisPeriodRxPri_Object=MibScalar
hmWanMobileThisPeriodRxPri=_HmWanMobileThisPeriodRxPri_Object((1,3,6,1,4,1,248,40,1,5,5,1),_HmWanMobileThisPeriodRxPri_Type())
hmWanMobileThisPeriodRxPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisPeriodRxPri.setStatus(_B)
_HmWanMobileThisPeriodRxSec_Type=Counter32
_HmWanMobileThisPeriodRxSec_Object=MibScalar
hmWanMobileThisPeriodRxSec=_HmWanMobileThisPeriodRxSec_Object((1,3,6,1,4,1,248,40,1,5,5,2),_HmWanMobileThisPeriodRxSec_Type())
hmWanMobileThisPeriodRxSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisPeriodRxSec.setStatus(_B)
_HmWanMobileThisPeriodTxPri_Type=Counter32
_HmWanMobileThisPeriodTxPri_Object=MibScalar
hmWanMobileThisPeriodTxPri=_HmWanMobileThisPeriodTxPri_Object((1,3,6,1,4,1,248,40,1,5,5,3),_HmWanMobileThisPeriodTxPri_Type())
hmWanMobileThisPeriodTxPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisPeriodTxPri.setStatus(_B)
_HmWanMobileThisPeriodTxSec_Type=Counter32
_HmWanMobileThisPeriodTxSec_Object=MibScalar
hmWanMobileThisPeriodTxSec=_HmWanMobileThisPeriodTxSec_Object((1,3,6,1,4,1,248,40,1,5,5,4),_HmWanMobileThisPeriodTxSec_Type())
hmWanMobileThisPeriodTxSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisPeriodTxSec.setStatus(_B)
_HmWanMobileThisPeriodConnectionsPri_Type=Counter32
_HmWanMobileThisPeriodConnectionsPri_Object=MibScalar
hmWanMobileThisPeriodConnectionsPri=_HmWanMobileThisPeriodConnectionsPri_Object((1,3,6,1,4,1,248,40,1,5,5,5),_HmWanMobileThisPeriodConnectionsPri_Type())
hmWanMobileThisPeriodConnectionsPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisPeriodConnectionsPri.setStatus(_B)
_HmWanMobileThisPeriodConnectionsSec_Type=Counter32
_HmWanMobileThisPeriodConnectionsSec_Object=MibScalar
hmWanMobileThisPeriodConnectionsSec=_HmWanMobileThisPeriodConnectionsSec_Object((1,3,6,1,4,1,248,40,1,5,5,6),_HmWanMobileThisPeriodConnectionsSec_Type())
hmWanMobileThisPeriodConnectionsSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisPeriodConnectionsSec.setStatus(_B)
_HmWanMobileThisPeriodOnlinePri_Type=TimeTicks
_HmWanMobileThisPeriodOnlinePri_Object=MibScalar
hmWanMobileThisPeriodOnlinePri=_HmWanMobileThisPeriodOnlinePri_Object((1,3,6,1,4,1,248,40,1,5,5,7),_HmWanMobileThisPeriodOnlinePri_Type())
hmWanMobileThisPeriodOnlinePri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisPeriodOnlinePri.setStatus(_B)
_HmWanMobileThisPeriodOnlineSec_Type=TimeTicks
_HmWanMobileThisPeriodOnlineSec_Object=MibScalar
hmWanMobileThisPeriodOnlineSec=_HmWanMobileThisPeriodOnlineSec_Object((1,3,6,1,4,1,248,40,1,5,5,8),_HmWanMobileThisPeriodOnlineSec_Type())
hmWanMobileThisPeriodOnlineSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisPeriodOnlineSec.setStatus(_B)
_HmWanMobileThisPeriodOffline_Type=TimeTicks
_HmWanMobileThisPeriodOffline_Object=MibScalar
hmWanMobileThisPeriodOffline=_HmWanMobileThisPeriodOffline_Object((1,3,6,1,4,1,248,40,1,5,5,9),_HmWanMobileThisPeriodOffline_Type())
hmWanMobileThisPeriodOffline.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisPeriodOffline.setStatus(_B)
_HmWanMobileThisPeriodCells_Type=Counter32
_HmWanMobileThisPeriodCells_Object=MibScalar
hmWanMobileThisPeriodCells=_HmWanMobileThisPeriodCells_Object((1,3,6,1,4,1,248,40,1,5,5,10),_HmWanMobileThisPeriodCells_Type())
hmWanMobileThisPeriodCells.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisPeriodCells.setStatus(_B)
_HmWanMobileThisPeriodSignalAvg_Type=Integer32
_HmWanMobileThisPeriodSignalAvg_Object=MibScalar
hmWanMobileThisPeriodSignalAvg=_HmWanMobileThisPeriodSignalAvg_Object((1,3,6,1,4,1,248,40,1,5,5,11),_HmWanMobileThisPeriodSignalAvg_Type())
hmWanMobileThisPeriodSignalAvg.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisPeriodSignalAvg.setStatus(_B)
_HmWanMobileThisPeriodSignalMin_Type=Integer32
_HmWanMobileThisPeriodSignalMin_Object=MibScalar
hmWanMobileThisPeriodSignalMin=_HmWanMobileThisPeriodSignalMin_Object((1,3,6,1,4,1,248,40,1,5,5,12),_HmWanMobileThisPeriodSignalMin_Type())
hmWanMobileThisPeriodSignalMin.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisPeriodSignalMin.setStatus(_B)
_HmWanMobileThisPeriodSignalMax_Type=Integer32
_HmWanMobileThisPeriodSignalMax_Object=MibScalar
hmWanMobileThisPeriodSignalMax=_HmWanMobileThisPeriodSignalMax_Object((1,3,6,1,4,1,248,40,1,5,5,13),_HmWanMobileThisPeriodSignalMax_Type())
hmWanMobileThisPeriodSignalMax.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisPeriodSignalMax.setStatus(_B)
_HmWanMobileThisPeriodDateMin_Type=Counter32
_HmWanMobileThisPeriodDateMin_Object=MibScalar
hmWanMobileThisPeriodDateMin=_HmWanMobileThisPeriodDateMin_Object((1,3,6,1,4,1,248,40,1,5,5,14),_HmWanMobileThisPeriodDateMin_Type())
hmWanMobileThisPeriodDateMin.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisPeriodDateMin.setStatus(_B)
_HmWanMobileThisPeriodDateMax_Type=Counter32
_HmWanMobileThisPeriodDateMax_Object=MibScalar
hmWanMobileThisPeriodDateMax=_HmWanMobileThisPeriodDateMax_Object((1,3,6,1,4,1,248,40,1,5,5,15),_HmWanMobileThisPeriodDateMax_Type())
hmWanMobileThisPeriodDateMax.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileThisPeriodDateMax.setStatus(_B)
_HmWanMobileLastPeriod_ObjectIdentity=ObjectIdentity
hmWanMobileLastPeriod=_HmWanMobileLastPeriod_ObjectIdentity((1,3,6,1,4,1,248,40,1,5,6))
_HmWanMobileLastPeriodRxPri_Type=Counter32
_HmWanMobileLastPeriodRxPri_Object=MibScalar
hmWanMobileLastPeriodRxPri=_HmWanMobileLastPeriodRxPri_Object((1,3,6,1,4,1,248,40,1,5,6,1),_HmWanMobileLastPeriodRxPri_Type())
hmWanMobileLastPeriodRxPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastPeriodRxPri.setStatus(_B)
_HmWanMobileLastPeriodRxSec_Type=Counter32
_HmWanMobileLastPeriodRxSec_Object=MibScalar
hmWanMobileLastPeriodRxSec=_HmWanMobileLastPeriodRxSec_Object((1,3,6,1,4,1,248,40,1,5,6,2),_HmWanMobileLastPeriodRxSec_Type())
hmWanMobileLastPeriodRxSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastPeriodRxSec.setStatus(_B)
_HmWanMobileLastPeriodTxPri_Type=Counter32
_HmWanMobileLastPeriodTxPri_Object=MibScalar
hmWanMobileLastPeriodTxPri=_HmWanMobileLastPeriodTxPri_Object((1,3,6,1,4,1,248,40,1,5,6,3),_HmWanMobileLastPeriodTxPri_Type())
hmWanMobileLastPeriodTxPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastPeriodTxPri.setStatus(_B)
_HmWanMobileLastPeriodTxSec_Type=Counter32
_HmWanMobileLastPeriodTxSec_Object=MibScalar
hmWanMobileLastPeriodTxSec=_HmWanMobileLastPeriodTxSec_Object((1,3,6,1,4,1,248,40,1,5,6,4),_HmWanMobileLastPeriodTxSec_Type())
hmWanMobileLastPeriodTxSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastPeriodTxSec.setStatus(_B)
_HmWanMobileLastPeriodConnectionsPri_Type=Counter32
_HmWanMobileLastPeriodConnectionsPri_Object=MibScalar
hmWanMobileLastPeriodConnectionsPri=_HmWanMobileLastPeriodConnectionsPri_Object((1,3,6,1,4,1,248,40,1,5,6,5),_HmWanMobileLastPeriodConnectionsPri_Type())
hmWanMobileLastPeriodConnectionsPri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastPeriodConnectionsPri.setStatus(_B)
_HmWanMobileLastPeriodConnectionsSec_Type=Counter32
_HmWanMobileLastPeriodConnectionsSec_Object=MibScalar
hmWanMobileLastPeriodConnectionsSec=_HmWanMobileLastPeriodConnectionsSec_Object((1,3,6,1,4,1,248,40,1,5,6,6),_HmWanMobileLastPeriodConnectionsSec_Type())
hmWanMobileLastPeriodConnectionsSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastPeriodConnectionsSec.setStatus(_B)
_HmWanMobileLastPeriodOnlinePri_Type=TimeTicks
_HmWanMobileLastPeriodOnlinePri_Object=MibScalar
hmWanMobileLastPeriodOnlinePri=_HmWanMobileLastPeriodOnlinePri_Object((1,3,6,1,4,1,248,40,1,5,6,7),_HmWanMobileLastPeriodOnlinePri_Type())
hmWanMobileLastPeriodOnlinePri.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastPeriodOnlinePri.setStatus(_B)
_HmWanMobileLastPeriodOnlineSec_Type=TimeTicks
_HmWanMobileLastPeriodOnlineSec_Object=MibScalar
hmWanMobileLastPeriodOnlineSec=_HmWanMobileLastPeriodOnlineSec_Object((1,3,6,1,4,1,248,40,1,5,6,8),_HmWanMobileLastPeriodOnlineSec_Type())
hmWanMobileLastPeriodOnlineSec.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastPeriodOnlineSec.setStatus(_B)
_HmWanMobileLastPeriodOffline_Type=TimeTicks
_HmWanMobileLastPeriodOffline_Object=MibScalar
hmWanMobileLastPeriodOffline=_HmWanMobileLastPeriodOffline_Object((1,3,6,1,4,1,248,40,1,5,6,9),_HmWanMobileLastPeriodOffline_Type())
hmWanMobileLastPeriodOffline.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastPeriodOffline.setStatus(_B)
_HmWanMobileLastPeriodCells_Type=Counter32
_HmWanMobileLastPeriodCells_Object=MibScalar
hmWanMobileLastPeriodCells=_HmWanMobileLastPeriodCells_Object((1,3,6,1,4,1,248,40,1,5,6,10),_HmWanMobileLastPeriodCells_Type())
hmWanMobileLastPeriodCells.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastPeriodCells.setStatus(_B)
_HmWanMobileLastPeriodSignalAvg_Type=Integer32
_HmWanMobileLastPeriodSignalAvg_Object=MibScalar
hmWanMobileLastPeriodSignalAvg=_HmWanMobileLastPeriodSignalAvg_Object((1,3,6,1,4,1,248,40,1,5,6,11),_HmWanMobileLastPeriodSignalAvg_Type())
hmWanMobileLastPeriodSignalAvg.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastPeriodSignalAvg.setStatus(_B)
_HmWanMobileLastPeriodSignalMin_Type=Integer32
_HmWanMobileLastPeriodSignalMin_Object=MibScalar
hmWanMobileLastPeriodSignalMin=_HmWanMobileLastPeriodSignalMin_Object((1,3,6,1,4,1,248,40,1,5,6,12),_HmWanMobileLastPeriodSignalMin_Type())
hmWanMobileLastPeriodSignalMin.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastPeriodSignalMin.setStatus(_B)
_HmWanMobileLastPeriodSignalMax_Type=Integer32
_HmWanMobileLastPeriodSignalMax_Object=MibScalar
hmWanMobileLastPeriodSignalMax=_HmWanMobileLastPeriodSignalMax_Object((1,3,6,1,4,1,248,40,1,5,6,13),_HmWanMobileLastPeriodSignalMax_Type())
hmWanMobileLastPeriodSignalMax.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastPeriodSignalMax.setStatus(_B)
_HmWanMobileLastPeriodDateMin_Type=Counter32
_HmWanMobileLastPeriodDateMin_Object=MibScalar
hmWanMobileLastPeriodDateMin=_HmWanMobileLastPeriodDateMin_Object((1,3,6,1,4,1,248,40,1,5,6,14),_HmWanMobileLastPeriodDateMin_Type())
hmWanMobileLastPeriodDateMin.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastPeriodDateMin.setStatus(_B)
_HmWanMobileLastPeriodDateMax_Type=Counter32
_HmWanMobileLastPeriodDateMax_Object=MibScalar
hmWanMobileLastPeriodDateMax=_HmWanMobileLastPeriodDateMax_Object((1,3,6,1,4,1,248,40,1,5,6,15),_HmWanMobileLastPeriodDateMax_Type())
hmWanMobileLastPeriodDateMax.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLastPeriodDateMax.setStatus(_B)
mibBuilder.exportSymbols('HIRSCHMANN-WAN-MOBILE-2-MIB',**{'hmWanMobile2Mib':hmWanMobile2Mib,'hmWanMobileToday':hmWanMobileToday,'hmWanMobileTodayRxPri':hmWanMobileTodayRxPri,'hmWanMobileTodayRxSec':hmWanMobileTodayRxSec,'hmWanMobileTodayTxPri':hmWanMobileTodayTxPri,'hmWanMobileTodayTxSec':hmWanMobileTodayTxSec,'hmWanMobileTodayConnectionsPri':hmWanMobileTodayConnectionsPri,'hmWanMobileTodayConnectionsSec':hmWanMobileTodayConnectionsSec,'hmWanMobileTodayOnlinePri':hmWanMobileTodayOnlinePri,'hmWanMobileTodayOnlineSec':hmWanMobileTodayOnlineSec,'hmWanMobileTodayOffline':hmWanMobileTodayOffline,'hmWanMobileTodayCells':hmWanMobileTodayCells,'hmWanMobileTodaySignalAvg':hmWanMobileTodaySignalAvg,'hmWanMobileTodaySignalMin':hmWanMobileTodaySignalMin,'hmWanMobileTodaySignalMax':hmWanMobileTodaySignalMax,'hmWanMobileTodayDateMin':hmWanMobileTodayDateMin,'hmWanMobileTodayDateMax':hmWanMobileTodayDateMax,'hmWanMobileYesterday':hmWanMobileYesterday,'hmWanMobileYesterdayRxPri':hmWanMobileYesterdayRxPri,'hmWanMobileYesterdayRxSec':hmWanMobileYesterdayRxSec,'hmWanMobileYesterdayTxPri':hmWanMobileYesterdayTxPri,'hmWanMobileYesterdayTxSec':hmWanMobileYesterdayTxSec,'hmWanMobileYesterdayConnectionsPri':hmWanMobileYesterdayConnectionsPri,'hmWanMobileYesterdayConnectionsSec':hmWanMobileYesterdayConnectionsSec,'hmWanMobileYesterdayOnlinePri':hmWanMobileYesterdayOnlinePri,'hmWanMobileYesterdayOnlineSec':hmWanMobileYesterdayOnlineSec,'hmWanMobileYesterdayOffline':hmWanMobileYesterdayOffline,'hmWanMobileYesterdayCells':hmWanMobileYesterdayCells,'hmWanMobileYesterdaySignalAvg':hmWanMobileYesterdaySignalAvg,'hmWanMobileYesterdaySignalMin':hmWanMobileYesterdaySignalMin,'hmWanMobileYesterdaySignalMax':hmWanMobileYesterdaySignalMax,'hmWanMobileYesterdayDateMin':hmWanMobileYesterdayDateMin,'hmWanMobileYesterdayDateMax':hmWanMobileYesterdayDateMax,'hmWanMobileThisWeek':hmWanMobileThisWeek,'hmWanMobileThisWeekRxPri':hmWanMobileThisWeekRxPri,'hmWanMobileThisWeekRxSec':hmWanMobileThisWeekRxSec,'hmWanMobileThisWeekTxPri':hmWanMobileThisWeekTxPri,'hmWanMobileThisWeekTxSec':hmWanMobileThisWeekTxSec,'hmWanMobileThisWeekConnectionsPri':hmWanMobileThisWeekConnectionsPri,'hmWanMobileThisWeekConnectionsSec':hmWanMobileThisWeekConnectionsSec,'hmWanMobileThisWeekOnlinePri':hmWanMobileThisWeekOnlinePri,'hmWanMobileThisWeekOnlineSec':hmWanMobileThisWeekOnlineSec,'hmWanMobileThisWeekOffline':hmWanMobileThisWeekOffline,'hmWanMobileThisWeekCells':hmWanMobileThisWeekCells,'hmWanMobileThisWeekSignalAvg':hmWanMobileThisWeekSignalAvg,'hmWanMobileThisWeekSignalMin':hmWanMobileThisWeekSignalMin,'hmWanMobileThisWeekSignalMax':hmWanMobileThisWeekSignalMax,'hmWanMobileThisWeekDateMin':hmWanMobileThisWeekDateMin,'hmWanMobileThisWeekDateMax':hmWanMobileThisWeekDateMax,'hmWanMobileLastWeek':hmWanMobileLastWeek,'hmWanMobileLastWeekRxPri':hmWanMobileLastWeekRxPri,'hmWanMobileLastWeekRxSec':hmWanMobileLastWeekRxSec,'hmWanMobileLastWeekTxPri':hmWanMobileLastWeekTxPri,'hmWanMobileLastWeekTxSec':hmWanMobileLastWeekTxSec,'hmWanMobileLastWeekConnectionsPri':hmWanMobileLastWeekConnectionsPri,'hmWanMobileLastWeekConnectionsSec':hmWanMobileLastWeekConnectionsSec,'hmWanMobileLastWeekOnlinePri':hmWanMobileLastWeekOnlinePri,'hmWanMobileLastWeekOnlineSec':hmWanMobileLastWeekOnlineSec,'hmWanMobileLastWeekOffline':hmWanMobileLastWeekOffline,'hmWanMobileLastWeekCells':hmWanMobileLastWeekCells,'hmWanMobileLastWeekSignalAvg':hmWanMobileLastWeekSignalAvg,'hmWanMobileLastWeekSignalMin':hmWanMobileLastWeekSignalMin,'hmWanMobileLastWeekSignalMax':hmWanMobileLastWeekSignalMax,'hmWanMobileLastWeekDateMin':hmWanMobileLastWeekDateMin,'hmWanMobileLastWeekDateMax':hmWanMobileLastWeekDateMax,'hmWanMobileThisPeriod':hmWanMobileThisPeriod,'hmWanMobileThisPeriodRxPri':hmWanMobileThisPeriodRxPri,'hmWanMobileThisPeriodRxSec':hmWanMobileThisPeriodRxSec,'hmWanMobileThisPeriodTxPri':hmWanMobileThisPeriodTxPri,'hmWanMobileThisPeriodTxSec':hmWanMobileThisPeriodTxSec,'hmWanMobileThisPeriodConnectionsPri':hmWanMobileThisPeriodConnectionsPri,'hmWanMobileThisPeriodConnectionsSec':hmWanMobileThisPeriodConnectionsSec,'hmWanMobileThisPeriodOnlinePri':hmWanMobileThisPeriodOnlinePri,'hmWanMobileThisPeriodOnlineSec':hmWanMobileThisPeriodOnlineSec,'hmWanMobileThisPeriodOffline':hmWanMobileThisPeriodOffline,'hmWanMobileThisPeriodCells':hmWanMobileThisPeriodCells,'hmWanMobileThisPeriodSignalAvg':hmWanMobileThisPeriodSignalAvg,'hmWanMobileThisPeriodSignalMin':hmWanMobileThisPeriodSignalMin,'hmWanMobileThisPeriodSignalMax':hmWanMobileThisPeriodSignalMax,'hmWanMobileThisPeriodDateMin':hmWanMobileThisPeriodDateMin,'hmWanMobileThisPeriodDateMax':hmWanMobileThisPeriodDateMax,'hmWanMobileLastPeriod':hmWanMobileLastPeriod,'hmWanMobileLastPeriodRxPri':hmWanMobileLastPeriodRxPri,'hmWanMobileLastPeriodRxSec':hmWanMobileLastPeriodRxSec,'hmWanMobileLastPeriodTxPri':hmWanMobileLastPeriodTxPri,'hmWanMobileLastPeriodTxSec':hmWanMobileLastPeriodTxSec,'hmWanMobileLastPeriodConnectionsPri':hmWanMobileLastPeriodConnectionsPri,'hmWanMobileLastPeriodConnectionsSec':hmWanMobileLastPeriodConnectionsSec,'hmWanMobileLastPeriodOnlinePri':hmWanMobileLastPeriodOnlinePri,'hmWanMobileLastPeriodOnlineSec':hmWanMobileLastPeriodOnlineSec,'hmWanMobileLastPeriodOffline':hmWanMobileLastPeriodOffline,'hmWanMobileLastPeriodCells':hmWanMobileLastPeriodCells,'hmWanMobileLastPeriodSignalAvg':hmWanMobileLastPeriodSignalAvg,'hmWanMobileLastPeriodSignalMin':hmWanMobileLastPeriodSignalMin,'hmWanMobileLastPeriodSignalMax':hmWanMobileLastPeriodSignalMax,'hmWanMobileLastPeriodDateMin':hmWanMobileLastPeriodDateMin,'hmWanMobileLastPeriodDateMax':hmWanMobileLastPeriodDateMax})