_I='cmmSoftwareProcessLastRestartReason'
_H='Unsigned32'
_G='cmmSoftwareProcessStartTime'
_F='cmmSoftwareProcessName'
_E='cmmSoftwareProcessID'
_D='Integer32'
_C='read-only'
_B='OCNOS-PSERV-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CmmChassisObject,=mibBuilder.importSymbols('CMM-CHASSIS-MIB','CmmChassisObject')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
ipi,=mibBuilder.importSymbols('OCNOS-IPI-MODULE-MIB','ipi')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
cmmSoftwareObjects=ModuleIdentity((1,3,6,1,4,1,36673,100,1,4))
if mibBuilder.loadTexts:cmmSoftwareObjects.setRevisions(('2018-04-05 00:00',))
_CmmSoftwareObjectsNotificationsPrefix_ObjectIdentity=ObjectIdentity
cmmSoftwareObjectsNotificationsPrefix=_CmmSoftwareObjectsNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,36673,100,1,4,0))
class _CmmSoftwareProcessKeepaliveTime_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,1800))
_CmmSoftwareProcessKeepaliveTime_Type.__name__=_H
_CmmSoftwareProcessKeepaliveTime_Object=MibScalar
cmmSoftwareProcessKeepaliveTime=_CmmSoftwareProcessKeepaliveTime_Object((1,3,6,1,4,1,36673,100,1,4,1),_CmmSoftwareProcessKeepaliveTime_Type())
cmmSoftwareProcessKeepaliveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSoftwareProcessKeepaliveTime.setStatus(_A)
class _CmmSoftwareProcessWatchdogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_CmmSoftwareProcessWatchdogStatus_Type.__name__=_D
_CmmSoftwareProcessWatchdogStatus_Object=MibScalar
cmmSoftwareProcessWatchdogStatus=_CmmSoftwareProcessWatchdogStatus_Object((1,3,6,1,4,1,36673,100,1,4,2),_CmmSoftwareProcessWatchdogStatus_Type())
cmmSoftwareProcessWatchdogStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSoftwareProcessWatchdogStatus.setStatus(_A)
class _CmmSoftwareProcessStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_CmmSoftwareProcessStatus_Type.__name__=_D
_CmmSoftwareProcessStatus_Object=MibScalar
cmmSoftwareProcessStatus=_CmmSoftwareProcessStatus_Object((1,3,6,1,4,1,36673,100,1,4,3),_CmmSoftwareProcessStatus_Type())
cmmSoftwareProcessStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSoftwareProcessStatus.setStatus(_A)
_CmmSoftwareProcessObjectsTable_Object=MibTable
cmmSoftwareProcessObjectsTable=_CmmSoftwareProcessObjectsTable_Object((1,3,6,1,4,1,36673,100,1,4,4))
if mibBuilder.loadTexts:cmmSoftwareProcessObjectsTable.setStatus(_A)
_CmmSoftwareProcessObjectsEntry_Object=MibTableRow
cmmSoftwareProcessObjectsEntry=_CmmSoftwareProcessObjectsEntry_Object((1,3,6,1,4,1,36673,100,1,4,4,1))
cmmSoftwareProcessObjectsEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cmmSoftwareProcessObjectsEntry.setStatus(_A)
_CmmSoftwareProcessID_Type=Unsigned32
_CmmSoftwareProcessID_Object=MibTableColumn
cmmSoftwareProcessID=_CmmSoftwareProcessID_Object((1,3,6,1,4,1,36673,100,1,4,4,1,1),_CmmSoftwareProcessID_Type())
cmmSoftwareProcessID.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSoftwareProcessID.setStatus(_A)
_CmmSoftwareProcessName_Type=OctetString
_CmmSoftwareProcessName_Object=MibTableColumn
cmmSoftwareProcessName=_CmmSoftwareProcessName_Object((1,3,6,1,4,1,36673,100,1,4,4,1,2),_CmmSoftwareProcessName_Type())
cmmSoftwareProcessName.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSoftwareProcessName.setStatus(_A)
class _CmmSoftwareProcessState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notrunning',0),('running',1)))
_CmmSoftwareProcessState_Type.__name__=_D
_CmmSoftwareProcessState_Object=MibTableColumn
cmmSoftwareProcessState=_CmmSoftwareProcessState_Object((1,3,6,1,4,1,36673,100,1,4,4,1,3),_CmmSoftwareProcessState_Type())
cmmSoftwareProcessState.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSoftwareProcessState.setStatus(_A)
_CmmSoftwareProcessStartTime_Type=DateAndTime
_CmmSoftwareProcessStartTime_Object=MibTableColumn
cmmSoftwareProcessStartTime=_CmmSoftwareProcessStartTime_Object((1,3,6,1,4,1,36673,100,1,4,4,1,4),_CmmSoftwareProcessStartTime_Type())
cmmSoftwareProcessStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSoftwareProcessStartTime.setStatus(_A)
_CmmSoftwareProcessLastRestartReason_Type=OctetString
_CmmSoftwareProcessLastRestartReason_Object=MibTableColumn
cmmSoftwareProcessLastRestartReason=_CmmSoftwareProcessLastRestartReason_Object((1,3,6,1,4,1,36673,100,1,4,4,1,5),_CmmSoftwareProcessLastRestartReason_Type())
cmmSoftwareProcessLastRestartReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSoftwareProcessLastRestartReason.setStatus(_A)
cmmSysPsDownNotification=NotificationType((1,3,6,1,4,1,36673,100,1,4,0,1))
cmmSysPsDownNotification.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_I)))
if mibBuilder.loadTexts:cmmSysPsDownNotification.setStatus(_A)
cmmSysPsRestartNotification=NotificationType((1,3,6,1,4,1,36673,100,1,4,0,2))
cmmSysPsRestartNotification.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:cmmSysPsRestartNotification.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cmmSoftwareObjects':cmmSoftwareObjects,'cmmSoftwareObjectsNotificationsPrefix':cmmSoftwareObjectsNotificationsPrefix,'cmmSysPsDownNotification':cmmSysPsDownNotification,'cmmSysPsRestartNotification':cmmSysPsRestartNotification,'cmmSoftwareProcessKeepaliveTime':cmmSoftwareProcessKeepaliveTime,'cmmSoftwareProcessWatchdogStatus':cmmSoftwareProcessWatchdogStatus,'cmmSoftwareProcessStatus':cmmSoftwareProcessStatus,'cmmSoftwareProcessObjectsTable':cmmSoftwareProcessObjectsTable,'cmmSoftwareProcessObjectsEntry':cmmSoftwareProcessObjectsEntry,_E:cmmSoftwareProcessID,_F:cmmSoftwareProcessName,'cmmSoftwareProcessState':cmmSoftwareProcessState,_G:cmmSoftwareProcessStartTime,_I:cmmSoftwareProcessLastRestartReason})