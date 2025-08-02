_J='diagCtrlHistoryIndex'
_I='diagECCReadingsIndex'
_H='diagFanRPMIndex'
_G='not-accessible'
_F='diagHealthMonitorIndex'
_E='CISCO-DMN-DSG-DIAG-MIB'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
ciscoDSGDiag=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,18))
if mibBuilder.loadTexts:ciscoDSGDiag.setRevisions(('2012-03-20 08:00','2010-10-13 08:00','2010-08-03 10:00','2010-04-12 09:00','2010-02-12 12:00','2009-12-07 12:00'))
_PowerOn_ObjectIdentity=ObjectIdentity
powerOn=_PowerOn_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,18,1))
class _PowerOnCreationDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_PowerOnCreationDate_Type.__name__=_C
_PowerOnCreationDate_Object=MibScalar
powerOnCreationDate=_PowerOnCreationDate_Object((1,3,6,1,4,1,1429,2,2,5,18,1,1),_PowerOnCreationDate_Type())
powerOnCreationDate.setMaxAccess(_B)
if mibBuilder.loadTexts:powerOnCreationDate.setStatus(_A)
class _PowerOnDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_PowerOnDate_Type.__name__=_C
_PowerOnDate_Object=MibScalar
powerOnDate=_PowerOnDate_Object((1,3,6,1,4,1,1429,2,2,5,18,1,2),_PowerOnDate_Type())
powerOnDate.setMaxAccess(_B)
if mibBuilder.loadTexts:powerOnDate.setStatus(_A)
class _PowerOnTotalHours_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_PowerOnTotalHours_Type.__name__=_C
_PowerOnTotalHours_Object=MibScalar
powerOnTotalHours=_PowerOnTotalHours_Object((1,3,6,1,4,1,1429,2,2,5,18,1,3),_PowerOnTotalHours_Type())
powerOnTotalHours.setMaxAccess(_B)
if mibBuilder.loadTexts:powerOnTotalHours.setStatus(_A)
class _PowerOnHrsSinceLastPowerOff_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_PowerOnHrsSinceLastPowerOff_Type.__name__=_C
_PowerOnHrsSinceLastPowerOff_Object=MibScalar
powerOnHrsSinceLastPowerOff=_PowerOnHrsSinceLastPowerOff_Object((1,3,6,1,4,1,1429,2,2,5,18,1,4),_PowerOnHrsSinceLastPowerOff_Type())
powerOnHrsSinceLastPowerOff.setMaxAccess(_B)
if mibBuilder.loadTexts:powerOnHrsSinceLastPowerOff.setStatus(_A)
class _PowerOnTotResetCount_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_PowerOnTotResetCount_Type.__name__=_C
_PowerOnTotResetCount_Object=MibScalar
powerOnTotResetCount=_PowerOnTotResetCount_Object((1,3,6,1,4,1,1429,2,2,5,18,1,5),_PowerOnTotResetCount_Type())
powerOnTotResetCount.setMaxAccess(_B)
if mibBuilder.loadTexts:powerOnTotResetCount.setStatus(_A)
class _PowerOnClrableResetCount_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_PowerOnClrableResetCount_Type.__name__=_C
_PowerOnClrableResetCount_Object=MibScalar
powerOnClrableResetCount=_PowerOnClrableResetCount_Object((1,3,6,1,4,1,1429,2,2,5,18,1,6),_PowerOnClrableResetCount_Type())
powerOnClrableResetCount.setMaxAccess(_B)
if mibBuilder.loadTexts:powerOnClrableResetCount.setStatus(_A)
class _PowerOnReasonLastReset_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PowerOnReasonLastReset_Type.__name__=_C
_PowerOnReasonLastReset_Object=MibScalar
powerOnReasonLastReset=_PowerOnReasonLastReset_Object((1,3,6,1,4,1,1429,2,2,5,18,1,7),_PowerOnReasonLastReset_Type())
powerOnReasonLastReset.setMaxAccess(_B)
if mibBuilder.loadTexts:powerOnReasonLastReset.setStatus(_A)
class _PowerOnClearResetCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('writeOnly',1),('yes',2)))
_PowerOnClearResetCounter_Type.__name__=_D
_PowerOnClearResetCounter_Object=MibScalar
powerOnClearResetCounter=_PowerOnClearResetCounter_Object((1,3,6,1,4,1,1429,2,2,5,18,1,8),_PowerOnClearResetCounter_Type())
powerOnClearResetCounter.setMaxAccess('read-write')
if mibBuilder.loadTexts:powerOnClearResetCounter.setStatus(_A)
class _PowerOnFactoryResetCount_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_PowerOnFactoryResetCount_Type.__name__=_C
_PowerOnFactoryResetCount_Object=MibScalar
powerOnFactoryResetCount=_PowerOnFactoryResetCount_Object((1,3,6,1,4,1,1429,2,2,5,18,1,9),_PowerOnFactoryResetCount_Type())
powerOnFactoryResetCount.setMaxAccess(_B)
if mibBuilder.loadTexts:powerOnFactoryResetCount.setStatus(_A)
class _PowerOnCurrentDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_PowerOnCurrentDateTime_Type.__name__=_C
_PowerOnCurrentDateTime_Object=MibScalar
powerOnCurrentDateTime=_PowerOnCurrentDateTime_Object((1,3,6,1,4,1,1429,2,2,5,18,1,10),_PowerOnCurrentDateTime_Type())
powerOnCurrentDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:powerOnCurrentDateTime.setStatus(_A)
_DiagTable_ObjectIdentity=ObjectIdentity
diagTable=_DiagTable_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,18,2))
_DiagHealthMonitorTable_Object=MibTable
diagHealthMonitorTable=_DiagHealthMonitorTable_Object((1,3,6,1,4,1,1429,2,2,5,18,2,1))
if mibBuilder.loadTexts:diagHealthMonitorTable.setStatus(_A)
_DiagHealthMonitorEntry_Object=MibTableRow
diagHealthMonitorEntry=_DiagHealthMonitorEntry_Object((1,3,6,1,4,1,1429,2,2,5,18,2,1,1))
diagHealthMonitorEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:diagHealthMonitorEntry.setStatus(_A)
class _DiagHealthMonitorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_DiagHealthMonitorIndex_Type.__name__=_D
_DiagHealthMonitorIndex_Object=MibTableColumn
diagHealthMonitorIndex=_DiagHealthMonitorIndex_Object((1,3,6,1,4,1,1429,2,2,5,18,2,1,1,1),_DiagHealthMonitorIndex_Type())
diagHealthMonitorIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:diagHealthMonitorIndex.setStatus(_A)
class _DiagHealthMonitorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DiagHealthMonitorName_Type.__name__=_C
_DiagHealthMonitorName_Object=MibTableColumn
diagHealthMonitorName=_DiagHealthMonitorName_Object((1,3,6,1,4,1,1429,2,2,5,18,2,1,1,2),_DiagHealthMonitorName_Type())
diagHealthMonitorName.setMaxAccess(_B)
if mibBuilder.loadTexts:diagHealthMonitorName.setStatus(_A)
class _DiagHealthMonitorValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DiagHealthMonitorValue_Type.__name__=_C
_DiagHealthMonitorValue_Object=MibTableColumn
diagHealthMonitorValue=_DiagHealthMonitorValue_Object((1,3,6,1,4,1,1429,2,2,5,18,2,1,1,3),_DiagHealthMonitorValue_Type())
diagHealthMonitorValue.setMaxAccess(_B)
if mibBuilder.loadTexts:diagHealthMonitorValue.setStatus(_A)
_DiagFanRPMTable_Object=MibTable
diagFanRPMTable=_DiagFanRPMTable_Object((1,3,6,1,4,1,1429,2,2,5,18,2,2))
if mibBuilder.loadTexts:diagFanRPMTable.setStatus(_A)
_DiagFanRPMEntry_Object=MibTableRow
diagFanRPMEntry=_DiagFanRPMEntry_Object((1,3,6,1,4,1,1429,2,2,5,18,2,2,1))
diagFanRPMEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:diagFanRPMEntry.setStatus(_A)
class _DiagFanRPMIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DiagFanRPMIndex_Type.__name__=_D
_DiagFanRPMIndex_Object=MibTableColumn
diagFanRPMIndex=_DiagFanRPMIndex_Object((1,3,6,1,4,1,1429,2,2,5,18,2,2,1,1),_DiagFanRPMIndex_Type())
diagFanRPMIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:diagFanRPMIndex.setStatus(_A)
class _DiagFanRPMName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DiagFanRPMName_Type.__name__=_C
_DiagFanRPMName_Object=MibTableColumn
diagFanRPMName=_DiagFanRPMName_Object((1,3,6,1,4,1,1429,2,2,5,18,2,2,1,2),_DiagFanRPMName_Type())
diagFanRPMName.setMaxAccess(_B)
if mibBuilder.loadTexts:diagFanRPMName.setStatus(_A)
class _DiagFanRPMValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DiagFanRPMValue_Type.__name__=_C
_DiagFanRPMValue_Object=MibTableColumn
diagFanRPMValue=_DiagFanRPMValue_Object((1,3,6,1,4,1,1429,2,2,5,18,2,2,1,3),_DiagFanRPMValue_Type())
diagFanRPMValue.setMaxAccess(_B)
if mibBuilder.loadTexts:diagFanRPMValue.setStatus(_A)
_DiagECCReadingsTable_Object=MibTable
diagECCReadingsTable=_DiagECCReadingsTable_Object((1,3,6,1,4,1,1429,2,2,5,18,2,3))
if mibBuilder.loadTexts:diagECCReadingsTable.setStatus(_A)
_DiagECCReadingsEntry_Object=MibTableRow
diagECCReadingsEntry=_DiagECCReadingsEntry_Object((1,3,6,1,4,1,1429,2,2,5,18,2,3,1))
diagECCReadingsEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:diagECCReadingsEntry.setStatus(_A)
class _DiagECCReadingsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_DiagECCReadingsIndex_Type.__name__=_D
_DiagECCReadingsIndex_Object=MibTableColumn
diagECCReadingsIndex=_DiagECCReadingsIndex_Object((1,3,6,1,4,1,1429,2,2,5,18,2,3,1,1),_DiagECCReadingsIndex_Type())
diagECCReadingsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:diagECCReadingsIndex.setStatus(_A)
class _DiagECCReadingsLocat_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DiagECCReadingsLocat_Type.__name__=_C
_DiagECCReadingsLocat_Object=MibTableColumn
diagECCReadingsLocat=_DiagECCReadingsLocat_Object((1,3,6,1,4,1,1429,2,2,5,18,2,3,1,2),_DiagECCReadingsLocat_Type())
diagECCReadingsLocat.setMaxAccess(_B)
if mibBuilder.loadTexts:diagECCReadingsLocat.setStatus(_A)
class _DiagECCReadingsType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DiagECCReadingsType_Type.__name__=_C
_DiagECCReadingsType_Object=MibTableColumn
diagECCReadingsType=_DiagECCReadingsType_Object((1,3,6,1,4,1,1429,2,2,5,18,2,3,1,3),_DiagECCReadingsType_Type())
diagECCReadingsType.setMaxAccess(_B)
if mibBuilder.loadTexts:diagECCReadingsType.setStatus(_A)
class _DiagECCReadingsVal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DiagECCReadingsVal_Type.__name__=_C
_DiagECCReadingsVal_Object=MibTableColumn
diagECCReadingsVal=_DiagECCReadingsVal_Object((1,3,6,1,4,1,1429,2,2,5,18,2,3,1,4),_DiagECCReadingsVal_Type())
diagECCReadingsVal.setMaxAccess(_B)
if mibBuilder.loadTexts:diagECCReadingsVal.setStatus(_A)
class _DiagECCReadingsApplicability_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DiagECCReadingsApplicability_Type.__name__=_C
_DiagECCReadingsApplicability_Object=MibTableColumn
diagECCReadingsApplicability=_DiagECCReadingsApplicability_Object((1,3,6,1,4,1,1429,2,2,5,18,2,3,1,5),_DiagECCReadingsApplicability_Type())
diagECCReadingsApplicability.setMaxAccess(_B)
if mibBuilder.loadTexts:diagECCReadingsApplicability.setStatus(_A)
_DiagCtrlHistoryTable_Object=MibTable
diagCtrlHistoryTable=_DiagCtrlHistoryTable_Object((1,3,6,1,4,1,1429,2,2,5,18,2,4))
if mibBuilder.loadTexts:diagCtrlHistoryTable.setStatus(_A)
_DiagCtrlHistoryEntry_Object=MibTableRow
diagCtrlHistoryEntry=_DiagCtrlHistoryEntry_Object((1,3,6,1,4,1,1429,2,2,5,18,2,4,1))
diagCtrlHistoryEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:diagCtrlHistoryEntry.setStatus(_A)
_DiagCtrlHistoryIndex_Type=Counter32
_DiagCtrlHistoryIndex_Object=MibTableColumn
diagCtrlHistoryIndex=_DiagCtrlHistoryIndex_Object((1,3,6,1,4,1,1429,2,2,5,18,2,4,1,1),_DiagCtrlHistoryIndex_Type())
diagCtrlHistoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:diagCtrlHistoryIndex.setStatus(_A)
class _DiagCtrlHistoryHistory_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DiagCtrlHistoryHistory_Type.__name__=_C
_DiagCtrlHistoryHistory_Object=MibTableColumn
diagCtrlHistoryHistory=_DiagCtrlHistoryHistory_Object((1,3,6,1,4,1,1429,2,2,5,18,2,4,1,2),_DiagCtrlHistoryHistory_Type())
diagCtrlHistoryHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:diagCtrlHistoryHistory.setStatus(_A)
class _DiagCtrlHistoryDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DiagCtrlHistoryDateTime_Type.__name__=_C
_DiagCtrlHistoryDateTime_Object=MibTableColumn
diagCtrlHistoryDateTime=_DiagCtrlHistoryDateTime_Object((1,3,6,1,4,1,1429,2,2,5,18,2,4,1,3),_DiagCtrlHistoryDateTime_Type())
diagCtrlHistoryDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:diagCtrlHistoryDateTime.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ciscoDSGDiag':ciscoDSGDiag,'powerOn':powerOn,'powerOnCreationDate':powerOnCreationDate,'powerOnDate':powerOnDate,'powerOnTotalHours':powerOnTotalHours,'powerOnHrsSinceLastPowerOff':powerOnHrsSinceLastPowerOff,'powerOnTotResetCount':powerOnTotResetCount,'powerOnClrableResetCount':powerOnClrableResetCount,'powerOnReasonLastReset':powerOnReasonLastReset,'powerOnClearResetCounter':powerOnClearResetCounter,'powerOnFactoryResetCount':powerOnFactoryResetCount,'powerOnCurrentDateTime':powerOnCurrentDateTime,'diagTable':diagTable,'diagHealthMonitorTable':diagHealthMonitorTable,'diagHealthMonitorEntry':diagHealthMonitorEntry,_F:diagHealthMonitorIndex,'diagHealthMonitorName':diagHealthMonitorName,'diagHealthMonitorValue':diagHealthMonitorValue,'diagFanRPMTable':diagFanRPMTable,'diagFanRPMEntry':diagFanRPMEntry,_H:diagFanRPMIndex,'diagFanRPMName':diagFanRPMName,'diagFanRPMValue':diagFanRPMValue,'diagECCReadingsTable':diagECCReadingsTable,'diagECCReadingsEntry':diagECCReadingsEntry,_I:diagECCReadingsIndex,'diagECCReadingsLocat':diagECCReadingsLocat,'diagECCReadingsType':diagECCReadingsType,'diagECCReadingsVal':diagECCReadingsVal,'diagECCReadingsApplicability':diagECCReadingsApplicability,'diagCtrlHistoryTable':diagCtrlHistoryTable,'diagCtrlHistoryEntry':diagCtrlHistoryEntry,_J:diagCtrlHistoryIndex,'diagCtrlHistoryHistory':diagCtrlHistoryHistory,'diagCtrlHistoryDateTime':diagCtrlHistoryDateTime})