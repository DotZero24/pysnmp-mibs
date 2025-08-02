_H='ctFDDIStatsIndex'
_G='ctFDDIPath'
_F='ctFDDISMT'
_E='Integer32'
_D='ctFDDISlot'
_C='CTRON-FDDI-STAT-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctFDDIStats,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctFDDIStats')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtFDDIStatsUtil_ObjectIdentity=ObjectIdentity
ctFDDIStatsUtil=_CtFDDIStatsUtil_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,5,2,1))
_CtFDDIStatsCtlTable_Object=MibTable
ctFDDIStatsCtlTable=_CtFDDIStatsCtlTable_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,1))
if mibBuilder.loadTexts:ctFDDIStatsCtlTable.setStatus(_A)
_CtFDDIStatsCtlEntry_Object=MibTableRow
ctFDDIStatsCtlEntry=_CtFDDIStatsCtlEntry_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,1,1))
ctFDDIStatsCtlEntry.setIndexNames((0,_C,_D),(0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:ctFDDIStatsCtlEntry.setStatus(_A)
_CtFDDISlot_Type=Integer32
_CtFDDISlot_Object=MibTableColumn
ctFDDISlot=_CtFDDISlot_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,1,1,1),_CtFDDISlot_Type())
ctFDDISlot.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDISlot.setStatus(_A)
_CtFDDISMT_Type=Integer32
_CtFDDISMT_Object=MibTableColumn
ctFDDISMT=_CtFDDISMT_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,1,1,2),_CtFDDISMT_Type())
ctFDDISMT.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDISMT.setStatus(_A)
_CtFDDIPath_Type=Integer32
_CtFDDIPath_Object=MibTableColumn
ctFDDIPath=_CtFDDIPath_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,1,1,3),_CtFDDIPath_Type())
ctFDDIPath.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIPath.setStatus(_A)
_CtFDDINextEntry_Type=Integer32
_CtFDDINextEntry_Object=MibTableColumn
ctFDDINextEntry=_CtFDDINextEntry_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,1,1,4),_CtFDDINextEntry_Type())
ctFDDINextEntry.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDINextEntry.setStatus(_A)
class _CtFDDIResetPeak_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('reset',2)))
_CtFDDIResetPeak_Type.__name__=_E
_CtFDDIResetPeak_Object=MibTableColumn
ctFDDIResetPeak=_CtFDDIResetPeak_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,1,1,5),_CtFDDIResetPeak_Type())
ctFDDIResetPeak.setMaxAccess('read-write')
if mibBuilder.loadTexts:ctFDDIResetPeak.setStatus(_A)
_CtFDDIStatsHistoryTable_Object=MibTable
ctFDDIStatsHistoryTable=_CtFDDIStatsHistoryTable_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,2))
if mibBuilder.loadTexts:ctFDDIStatsHistoryTable.setStatus(_A)
_CtFDDIStatsHistoryEntry_Object=MibTableRow
ctFDDIStatsHistoryEntry=_CtFDDIStatsHistoryEntry_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,2,1))
ctFDDIStatsHistoryEntry.setIndexNames((0,_C,_D),(0,_C,_H))
if mibBuilder.loadTexts:ctFDDIStatsHistoryEntry.setStatus(_A)
_CtFDDIStatsIndex_Type=Integer32
_CtFDDIStatsIndex_Object=MibTableColumn
ctFDDIStatsIndex=_CtFDDIStatsIndex_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,2,1,1),_CtFDDIStatsIndex_Type())
ctFDDIStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIStatsIndex.setStatus(_A)
_CtFDDIStatsTimeStamp_Type=TimeTicks
_CtFDDIStatsTimeStamp_Object=MibTableColumn
ctFDDIStatsTimeStamp=_CtFDDIStatsTimeStamp_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,2,1,2),_CtFDDIStatsTimeStamp_Type())
ctFDDIStatsTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIStatsTimeStamp.setStatus(_A)
_CtFDDIFrames_Type=Integer32
_CtFDDIFrames_Object=MibTableColumn
ctFDDIFrames=_CtFDDIFrames_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,2,1,3),_CtFDDIFrames_Type())
ctFDDIFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIFrames.setStatus(_A)
_CtFDDIBytes_Type=Integer32
_CtFDDIBytes_Object=MibTableColumn
ctFDDIBytes=_CtFDDIBytes_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,2,1,4),_CtFDDIBytes_Type())
ctFDDIBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIBytes.setStatus(_A)
_CtFDDIPeakBytes_Type=Integer32
_CtFDDIPeakBytes_Object=MibTableColumn
ctFDDIPeakBytes=_CtFDDIPeakBytes_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,2,1,5),_CtFDDIPeakBytes_Type())
ctFDDIPeakBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIPeakBytes.setStatus(_A)
_CtFDDIPeakTime_Type=Integer32
_CtFDDIPeakTime_Object=MibTableColumn
ctFDDIPeakTime=_CtFDDIPeakTime_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,2,1,6),_CtFDDIPeakTime_Type())
ctFDDIPeakTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIPeakTime.setStatus(_A)
_CtFDDIStatsSMT_Type=Integer32
_CtFDDIStatsSMT_Object=MibTableColumn
ctFDDIStatsSMT=_CtFDDIStatsSMT_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,2,1,7),_CtFDDIStatsSMT_Type())
ctFDDIStatsSMT.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIStatsSMT.setStatus(_A)
_CtFDDIStatsPath_Type=Integer32
_CtFDDIStatsPath_Object=MibTableColumn
ctFDDIStatsPath=_CtFDDIStatsPath_Object((1,3,6,1,4,1,52,4,1,2,5,2,1,2,1,8),_CtFDDIStatsPath_Type())
ctFDDIStatsPath.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIStatsPath.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ctFDDIStatsUtil':ctFDDIStatsUtil,'ctFDDIStatsCtlTable':ctFDDIStatsCtlTable,'ctFDDIStatsCtlEntry':ctFDDIStatsCtlEntry,_D:ctFDDISlot,_F:ctFDDISMT,_G:ctFDDIPath,'ctFDDINextEntry':ctFDDINextEntry,'ctFDDIResetPeak':ctFDDIResetPeak,'ctFDDIStatsHistoryTable':ctFDDIStatsHistoryTable,'ctFDDIStatsHistoryEntry':ctFDDIStatsHistoryEntry,_H:ctFDDIStatsIndex,'ctFDDIStatsTimeStamp':ctFDDIStatsTimeStamp,'ctFDDIFrames':ctFDDIFrames,'ctFDDIBytes':ctFDDIBytes,'ctFDDIPeakBytes':ctFDDIPeakBytes,'ctFDDIPeakTime':ctFDDIPeakTime,'ctFDDIStatsSMT':ctFDDIStatsSMT,'ctFDDIStatsPath':ctFDDIStatsPath})