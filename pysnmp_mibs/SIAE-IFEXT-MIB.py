_L='read-create'
_K='enable'
_J='disable'
_I='copper'
_H='DisplayString'
_G='AlarmSeverityCode'
_F='read-write'
_E='ifextIfIndex'
_D='SIAE-IFEXT-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
AlarmSeverityCode,AlarmStatus=mibBuilder.importSymbols('SIAE-ALARM-MIB',_G,'AlarmStatus')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention')
ifext=ModuleIdentity((1,3,6,1,4,1,3373,1103,73))
if mibBuilder.loadTexts:ifext.setRevisions(('2019-05-29 00:00','2016-11-02 00:00','2016-09-14 00:00','2016-08-05 00:00','2016-07-13 00:00','2016-04-18 00:00','2015-07-21 00:00','2014-12-02 00:00','2014-09-26 00:00','2014-06-05 00:00','2014-02-21 00:00','2013-10-28 00:00'))
class _IfextMibVersion_Type(Integer32):defaultValue=1
_IfextMibVersion_Type.__name__=_B
_IfextMibVersion_Object=MibScalar
ifextMibVersion=_IfextMibVersion_Object((1,3,6,1,4,1,3373,1103,73,1),_IfextMibVersion_Type())
ifextMibVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ifextMibVersion.setStatus(_A)
_IfextTable_Object=MibTable
ifextTable=_IfextTable_Object((1,3,6,1,4,1,3373,1103,73,2))
if mibBuilder.loadTexts:ifextTable.setStatus(_A)
_IfextTableEntry_Object=MibTableRow
ifextTableEntry=_IfextTableEntry_Object((1,3,6,1,4,1,3373,1103,73,2,1))
ifextTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ifextTableEntry.setStatus(_A)
_IfextIfIndex_Type=InterfaceIndex
_IfextIfIndex_Object=MibTableColumn
ifextIfIndex=_IfextIfIndex_Object((1,3,6,1,4,1,3373,1103,73,2,1,1),_IfextIfIndex_Type())
ifextIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ifextIfIndex.setStatus(_A)
class _IfextLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_IfextLabel_Type.__name__=_H
_IfextLabel_Object=MibTableColumn
ifextLabel=_IfextLabel_Object((1,3,6,1,4,1,3373,1103,73,2,1,2),_IfextLabel_Type())
ifextLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:ifextLabel.setStatus(_A)
class _IfextAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),('loopback',4),('loopbackExternal',5)))
_IfextAdminStatus_Type.__name__=_B
_IfextAdminStatus_Object=MibTableColumn
ifextAdminStatus=_IfextAdminStatus_Object((1,3,6,1,4,1,3373,1103,73,2,1,3),_IfextAdminStatus_Type())
ifextAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifextAdminStatus.setStatus(_A)
class _IfextPortUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('unused',0),('lan',1),('radio',2),('mgmt',3),('stack',4),('aux',5),('pwe3',6)))
_IfextPortUsage_Type.__name__=_B
_IfextPortUsage_Object=MibTableColumn
ifextPortUsage=_IfextPortUsage_Object((1,3,6,1,4,1,3373,1103,73,2,1,4),_IfextPortUsage_Type())
ifextPortUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:ifextPortUsage.setStatus(_A)
class _IfextMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('fiber',2),('combo',3),('other',4)))
_IfextMediumType_Type.__name__=_B
_IfextMediumType_Object=MibTableColumn
ifextMediumType=_IfextMediumType_Object((1,3,6,1,4,1,3373,1103,73,2,1,5),_IfextMediumType_Type())
ifextMediumType.setMaxAccess(_C)
if mibBuilder.loadTexts:ifextMediumType.setStatus(_A)
class _IfextMediumSelection_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),(_I,1),('fiber',2)))
_IfextMediumSelection_Type.__name__=_B
_IfextMediumSelection_Object=MibTableColumn
ifextMediumSelection=_IfextMediumSelection_Object((1,3,6,1,4,1,3373,1103,73,2,1,6),_IfextMediumSelection_Type())
ifextMediumSelection.setMaxAccess(_C)
if mibBuilder.loadTexts:ifextMediumSelection.setStatus(_A)
class _IfextAlarmReportEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_IfextAlarmReportEnable_Type.__name__=_B
_IfextAlarmReportEnable_Object=MibTableColumn
ifextAlarmReportEnable=_IfextAlarmReportEnable_Object((1,3,6,1,4,1,3373,1103,73,2,1,7),_IfextAlarmReportEnable_Type())
ifextAlarmReportEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:ifextAlarmReportEnable.setStatus(_A)
_IfextSfpId_Type=Integer32
_IfextSfpId_Object=MibTableColumn
ifextSfpId=_IfextSfpId_Object((1,3,6,1,4,1,3373,1103,73,2,1,8),_IfextSfpId_Type())
ifextSfpId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifextSfpId.setStatus(_A)
class _IfextCapabilities_Type(Bits):namedValues=NamedValues(*(('ifextCapabilityLoop',0),('ifextCapability2g5Bps',1),('ifextCapabilityMabSensor',2),('ifextCapabilityEncrypt',3),('ifextCapability10gBps',4),('ifextCapabilityIeee1588',5),('ifextCapabilityHRLmember',6),('ifextCapabilityHRLcarrier',7),('ifextCapabilityFixedSpeed',8),('ifextCapabilityPortProtection',9)))
_IfextCapabilities_Type.__name__='Bits'
_IfextCapabilities_Object=MibTableColumn
ifextCapabilities=_IfextCapabilities_Object((1,3,6,1,4,1,3373,1103,73,2,1,9),_IfextCapabilities_Type())
ifextCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:ifextCapabilities.setStatus(_A)
_IfextLosAlarm_Type=AlarmStatus
_IfextLosAlarm_Object=MibTableColumn
ifextLosAlarm=_IfextLosAlarm_Object((1,3,6,1,4,1,3373,1103,73,2,1,10),_IfextLosAlarm_Type())
ifextLosAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ifextLosAlarm.setStatus(_A)
_IfextRowStatus_Type=RowStatus
_IfextRowStatus_Object=MibTableColumn
ifextRowStatus=_IfextRowStatus_Object((1,3,6,1,4,1,3373,1103,73,2,1,11),_IfextRowStatus_Type())
ifextRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:ifextRowStatus.setStatus(_A)
_IfextMaintTable_Object=MibTable
ifextMaintTable=_IfextMaintTable_Object((1,3,6,1,4,1,3373,1103,73,3))
if mibBuilder.loadTexts:ifextMaintTable.setStatus(_A)
_IfextMaintTableEntry_Object=MibTableRow
ifextMaintTableEntry=_IfextMaintTableEntry_Object((1,3,6,1,4,1,3373,1103,73,3,1))
ifextMaintTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ifextMaintTableEntry.setStatus(_A)
class _IfextLineLoop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),('enableExt',3)))
_IfextLineLoop_Type.__name__=_B
_IfextLineLoop_Object=MibTableColumn
ifextLineLoop=_IfextLineLoop_Object((1,3,6,1,4,1,3373,1103,73,3,1,1),_IfextLineLoop_Type())
ifextLineLoop.setMaxAccess(_C)
if mibBuilder.loadTexts:ifextLineLoop.setStatus(_A)
_IfextRmonTable_Object=MibTable
ifextRmonTable=_IfextRmonTable_Object((1,3,6,1,4,1,3373,1103,73,4))
if mibBuilder.loadTexts:ifextRmonTable.setStatus(_A)
_IfextRmonTableEntry_Object=MibTableRow
ifextRmonTableEntry=_IfextRmonTableEntry_Object((1,3,6,1,4,1,3373,1103,73,4,1))
ifextRmonTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ifextRmonTableEntry.setStatus(_A)
class _IfextRmonPortSpeedMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rmonSpeedCurrent',1),('rmonSpeedConfigured',2)))
_IfextRmonPortSpeedMode_Type.__name__=_B
_IfextRmonPortSpeedMode_Object=MibTableColumn
ifextRmonPortSpeedMode=_IfextRmonPortSpeedMode_Object((1,3,6,1,4,1,3373,1103,73,4,1,1),_IfextRmonPortSpeedMode_Type())
ifextRmonPortSpeedMode.setMaxAccess(_F)
if mibBuilder.loadTexts:ifextRmonPortSpeedMode.setStatus(_A)
class _IfextRmonPortSpeedValue_Type(Integer32):defaultValue=1000
_IfextRmonPortSpeedValue_Type.__name__=_B
_IfextRmonPortSpeedValue_Object=MibTableColumn
ifextRmonPortSpeedValue=_IfextRmonPortSpeedValue_Object((1,3,6,1,4,1,3373,1103,73,4,1,2),_IfextRmonPortSpeedValue_Type())
ifextRmonPortSpeedValue.setMaxAccess(_F)
if mibBuilder.loadTexts:ifextRmonPortSpeedValue.setStatus(_A)
if mibBuilder.loadTexts:ifextRmonPortSpeedValue.setUnits('Mbps')
class _IfextLosAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_IfextLosAlarmSeverityCode_Type.__name__=_G
_IfextLosAlarmSeverityCode_Object=MibScalar
ifextLosAlarmSeverityCode=_IfextLosAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,73,5),_IfextLosAlarmSeverityCode_Type())
ifextLosAlarmSeverityCode.setMaxAccess(_F)
if mibBuilder.loadTexts:ifextLosAlarmSeverityCode.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ifext':ifext,'ifextMibVersion':ifextMibVersion,'ifextTable':ifextTable,'ifextTableEntry':ifextTableEntry,_E:ifextIfIndex,'ifextLabel':ifextLabel,'ifextAdminStatus':ifextAdminStatus,'ifextPortUsage':ifextPortUsage,'ifextMediumType':ifextMediumType,'ifextMediumSelection':ifextMediumSelection,'ifextAlarmReportEnable':ifextAlarmReportEnable,'ifextSfpId':ifextSfpId,'ifextCapabilities':ifextCapabilities,'ifextLosAlarm':ifextLosAlarm,'ifextRowStatus':ifextRowStatus,'ifextMaintTable':ifextMaintTable,'ifextMaintTableEntry':ifextMaintTableEntry,'ifextLineLoop':ifextLineLoop,'ifextRmonTable':ifextRmonTable,'ifextRmonTableEntry':ifextRmonTableEntry,'ifextRmonPortSpeedMode':ifextRmonPortSpeedMode,'ifextRmonPortSpeedValue':ifextRmonPortSpeedValue,'ifextLosAlarmSeverityCode':ifextLosAlarmSeverityCode})