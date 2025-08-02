_L='swTimeRangeCPUACLAccessID'
_K='swTimeRangeCPUACLProfileID'
_J='read-write'
_I='swTimeRangeACLAccessID'
_H='swTimeRangeACLProfileID'
_G='swTimeRangeMgmtRangeName'
_F='Integer32'
_E='read-create'
_D='read-only'
_C='TIMERANGE-MIB'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_B,'PhysAddress','RowStatus','TextualConvention')
swTimeRangeMIB=ModuleIdentity((1,3,6,1,4,1,171,12,50))
_SwTimeRangeCtrl_ObjectIdentity=ObjectIdentity
swTimeRangeCtrl=_SwTimeRangeCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,50,1))
_SwTimeRangeInfo_ObjectIdentity=ObjectIdentity
swTimeRangeInfo=_SwTimeRangeInfo_ObjectIdentity((1,3,6,1,4,1,171,12,50,2))
_SwTimeRangeMgmt_ObjectIdentity=ObjectIdentity
swTimeRangeMgmt=_SwTimeRangeMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,50,3))
_SwTimeRangeMgmtTable_Object=MibTable
swTimeRangeMgmtTable=_SwTimeRangeMgmtTable_Object((1,3,6,1,4,1,171,12,50,3,1))
if mibBuilder.loadTexts:swTimeRangeMgmtTable.setStatus(_A)
_SwTimeRangeMgmtEntry_Object=MibTableRow
swTimeRangeMgmtEntry=_SwTimeRangeMgmtEntry_Object((1,3,6,1,4,1,171,12,50,3,1,1))
swTimeRangeMgmtEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:swTimeRangeMgmtEntry.setStatus(_A)
class _SwTimeRangeMgmtRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwTimeRangeMgmtRangeName_Type.__name__=_B
_SwTimeRangeMgmtRangeName_Object=MibTableColumn
swTimeRangeMgmtRangeName=_SwTimeRangeMgmtRangeName_Object((1,3,6,1,4,1,171,12,50,3,1,1,1),_SwTimeRangeMgmtRangeName_Type())
swTimeRangeMgmtRangeName.setMaxAccess(_D)
if mibBuilder.loadTexts:swTimeRangeMgmtRangeName.setStatus(_A)
_SwTimeRangeMgmtSelectDays_Type=DisplayString
_SwTimeRangeMgmtSelectDays_Object=MibTableColumn
swTimeRangeMgmtSelectDays=_SwTimeRangeMgmtSelectDays_Object((1,3,6,1,4,1,171,12,50,3,1,1,2),_SwTimeRangeMgmtSelectDays_Type())
swTimeRangeMgmtSelectDays.setMaxAccess(_E)
if mibBuilder.loadTexts:swTimeRangeMgmtSelectDays.setStatus(_A)
class _SwTimeRangeMgmtStartTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwTimeRangeMgmtStartTime_Type.__name__=_B
_SwTimeRangeMgmtStartTime_Object=MibTableColumn
swTimeRangeMgmtStartTime=_SwTimeRangeMgmtStartTime_Object((1,3,6,1,4,1,171,12,50,3,1,1,3),_SwTimeRangeMgmtStartTime_Type())
swTimeRangeMgmtStartTime.setMaxAccess(_E)
if mibBuilder.loadTexts:swTimeRangeMgmtStartTime.setStatus(_A)
class _SwTimeRangeMgmtEndTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwTimeRangeMgmtEndTime_Type.__name__=_B
_SwTimeRangeMgmtEndTime_Object=MibTableColumn
swTimeRangeMgmtEndTime=_SwTimeRangeMgmtEndTime_Object((1,3,6,1,4,1,171,12,50,3,1,1,4),_SwTimeRangeMgmtEndTime_Type())
swTimeRangeMgmtEndTime.setMaxAccess(_E)
if mibBuilder.loadTexts:swTimeRangeMgmtEndTime.setStatus(_A)
_SwTimeRangeMgmtStatus_Type=RowStatus
_SwTimeRangeMgmtStatus_Object=MibTableColumn
swTimeRangeMgmtStatus=_SwTimeRangeMgmtStatus_Object((1,3,6,1,4,1,171,12,50,3,1,1,5),_SwTimeRangeMgmtStatus_Type())
swTimeRangeMgmtStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swTimeRangeMgmtStatus.setStatus(_A)
_SwTimeRangeACLTable_Object=MibTable
swTimeRangeACLTable=_SwTimeRangeACLTable_Object((1,3,6,1,4,1,171,12,50,3,2))
if mibBuilder.loadTexts:swTimeRangeACLTable.setStatus(_A)
_SwTimeRangeACLEntry_Object=MibTableRow
swTimeRangeACLEntry=_SwTimeRangeACLEntry_Object((1,3,6,1,4,1,171,12,50,3,2,1))
swTimeRangeACLEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:swTimeRangeACLEntry.setStatus(_A)
_SwTimeRangeACLProfileID_Type=Integer32
_SwTimeRangeACLProfileID_Object=MibTableColumn
swTimeRangeACLProfileID=_SwTimeRangeACLProfileID_Object((1,3,6,1,4,1,171,12,50,3,2,1,1),_SwTimeRangeACLProfileID_Type())
swTimeRangeACLProfileID.setMaxAccess(_D)
if mibBuilder.loadTexts:swTimeRangeACLProfileID.setStatus(_A)
class _SwTimeRangeACLAccessID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwTimeRangeACLAccessID_Type.__name__=_F
_SwTimeRangeACLAccessID_Object=MibTableColumn
swTimeRangeACLAccessID=_SwTimeRangeACLAccessID_Object((1,3,6,1,4,1,171,12,50,3,2,1,2),_SwTimeRangeACLAccessID_Type())
swTimeRangeACLAccessID.setMaxAccess(_D)
if mibBuilder.loadTexts:swTimeRangeACLAccessID.setStatus(_A)
class _SwTimeRangeACLTimeRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwTimeRangeACLTimeRangeName_Type.__name__=_B
_SwTimeRangeACLTimeRangeName_Object=MibTableColumn
swTimeRangeACLTimeRangeName=_SwTimeRangeACLTimeRangeName_Object((1,3,6,1,4,1,171,12,50,3,2,1,3),_SwTimeRangeACLTimeRangeName_Type())
swTimeRangeACLTimeRangeName.setMaxAccess(_J)
if mibBuilder.loadTexts:swTimeRangeACLTimeRangeName.setStatus(_A)
_SwTimeRangeCPUACLTable_Object=MibTable
swTimeRangeCPUACLTable=_SwTimeRangeCPUACLTable_Object((1,3,6,1,4,1,171,12,50,3,3))
if mibBuilder.loadTexts:swTimeRangeCPUACLTable.setStatus(_A)
_SwTimeRangeCPUACLEntry_Object=MibTableRow
swTimeRangeCPUACLEntry=_SwTimeRangeCPUACLEntry_Object((1,3,6,1,4,1,171,12,50,3,3,1))
swTimeRangeCPUACLEntry.setIndexNames((0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:swTimeRangeCPUACLEntry.setStatus(_A)
_SwTimeRangeCPUACLProfileID_Type=Integer32
_SwTimeRangeCPUACLProfileID_Object=MibTableColumn
swTimeRangeCPUACLProfileID=_SwTimeRangeCPUACLProfileID_Object((1,3,6,1,4,1,171,12,50,3,3,1,1),_SwTimeRangeCPUACLProfileID_Type())
swTimeRangeCPUACLProfileID.setMaxAccess(_D)
if mibBuilder.loadTexts:swTimeRangeCPUACLProfileID.setStatus(_A)
class _SwTimeRangeCPUACLAccessID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwTimeRangeCPUACLAccessID_Type.__name__=_F
_SwTimeRangeCPUACLAccessID_Object=MibTableColumn
swTimeRangeCPUACLAccessID=_SwTimeRangeCPUACLAccessID_Object((1,3,6,1,4,1,171,12,50,3,3,1,2),_SwTimeRangeCPUACLAccessID_Type())
swTimeRangeCPUACLAccessID.setMaxAccess(_D)
if mibBuilder.loadTexts:swTimeRangeCPUACLAccessID.setStatus(_A)
class _SwTimeRangeCPUACLTimeRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwTimeRangeCPUACLTimeRangeName_Type.__name__=_B
_SwTimeRangeCPUACLTimeRangeName_Object=MibTableColumn
swTimeRangeCPUACLTimeRangeName=_SwTimeRangeCPUACLTimeRangeName_Object((1,3,6,1,4,1,171,12,50,3,3,1,3),_SwTimeRangeCPUACLTimeRangeName_Type())
swTimeRangeCPUACLTimeRangeName.setMaxAccess(_J)
if mibBuilder.loadTexts:swTimeRangeCPUACLTimeRangeName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'swTimeRangeMIB':swTimeRangeMIB,'swTimeRangeCtrl':swTimeRangeCtrl,'swTimeRangeInfo':swTimeRangeInfo,'swTimeRangeMgmt':swTimeRangeMgmt,'swTimeRangeMgmtTable':swTimeRangeMgmtTable,'swTimeRangeMgmtEntry':swTimeRangeMgmtEntry,_G:swTimeRangeMgmtRangeName,'swTimeRangeMgmtSelectDays':swTimeRangeMgmtSelectDays,'swTimeRangeMgmtStartTime':swTimeRangeMgmtStartTime,'swTimeRangeMgmtEndTime':swTimeRangeMgmtEndTime,'swTimeRangeMgmtStatus':swTimeRangeMgmtStatus,'swTimeRangeACLTable':swTimeRangeACLTable,'swTimeRangeACLEntry':swTimeRangeACLEntry,_H:swTimeRangeACLProfileID,_I:swTimeRangeACLAccessID,'swTimeRangeACLTimeRangeName':swTimeRangeACLTimeRangeName,'swTimeRangeCPUACLTable':swTimeRangeCPUACLTable,'swTimeRangeCPUACLEntry':swTimeRangeCPUACLEntry,_K:swTimeRangeCPUACLProfileID,_L:swTimeRangeCPUACLAccessID,'swTimeRangeCPUACLTimeRangeName':swTimeRangeCPUACLTimeRangeName})