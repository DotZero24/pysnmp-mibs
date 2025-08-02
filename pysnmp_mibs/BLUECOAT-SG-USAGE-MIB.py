_H='deviceUsageStatus'
_G='deviceUsagePercent'
_F='deviceUsageName'
_E='deviceUsageIndex'
_D='Integer32'
_C='BLUECOAT-SG-USAGE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
blueCoatMgmt,=mibBuilder.importSymbols('BLUECOAT-MIB','blueCoatMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
deviceUsageMIB=ModuleIdentity((1,3,6,1,4,1,3417,2,4))
if mibBuilder.loadTexts:deviceUsageMIB.setRevisions(('2013-07-11 03:00','2008-01-16 03:00','2007-12-07 03:00','2002-11-06 03:00'))
class Percent(TextualConvention,Integer32):status=_A;displayHint='d%';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class UsageStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('high',2)))
_DeviceUsageMIBObjects_ObjectIdentity=ObjectIdentity
deviceUsageMIBObjects=_DeviceUsageMIBObjects_ObjectIdentity((1,3,6,1,4,1,3417,2,4,1))
_DeviceUsageTable_Object=MibTable
deviceUsageTable=_DeviceUsageTable_Object((1,3,6,1,4,1,3417,2,4,1,1))
if mibBuilder.loadTexts:deviceUsageTable.setStatus(_A)
_DeviceUsageEntry_Object=MibTableRow
deviceUsageEntry=_DeviceUsageEntry_Object((1,3,6,1,4,1,3417,2,4,1,1,1))
deviceUsageEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:deviceUsageEntry.setStatus(_A)
class _DeviceUsageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DeviceUsageIndex_Type.__name__=_D
_DeviceUsageIndex_Object=MibTableColumn
deviceUsageIndex=_DeviceUsageIndex_Object((1,3,6,1,4,1,3417,2,4,1,1,1,1),_DeviceUsageIndex_Type())
deviceUsageIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:deviceUsageIndex.setStatus(_A)
_DeviceUsageTrapEnabled_Type=TruthValue
_DeviceUsageTrapEnabled_Object=MibTableColumn
deviceUsageTrapEnabled=_DeviceUsageTrapEnabled_Object((1,3,6,1,4,1,3417,2,4,1,1,1,2),_DeviceUsageTrapEnabled_Type())
deviceUsageTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceUsageTrapEnabled.setStatus(_A)
_DeviceUsageName_Type=DisplayString
_DeviceUsageName_Object=MibTableColumn
deviceUsageName=_DeviceUsageName_Object((1,3,6,1,4,1,3417,2,4,1,1,1,3),_DeviceUsageName_Type())
deviceUsageName.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceUsageName.setStatus(_A)
_DeviceUsagePercent_Type=Percent
_DeviceUsagePercent_Object=MibTableColumn
deviceUsagePercent=_DeviceUsagePercent_Object((1,3,6,1,4,1,3417,2,4,1,1,1,4),_DeviceUsagePercent_Type())
deviceUsagePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceUsagePercent.setStatus(_A)
_DeviceUsageHigh_Type=Percent
_DeviceUsageHigh_Object=MibTableColumn
deviceUsageHigh=_DeviceUsageHigh_Object((1,3,6,1,4,1,3417,2,4,1,1,1,5),_DeviceUsageHigh_Type())
deviceUsageHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceUsageHigh.setStatus(_A)
_DeviceUsageStatus_Type=UsageStatus
_DeviceUsageStatus_Object=MibTableColumn
deviceUsageStatus=_DeviceUsageStatus_Object((1,3,6,1,4,1,3417,2,4,1,1,1,6),_DeviceUsageStatus_Type())
deviceUsageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceUsageStatus.setStatus(_A)
_DeviceUsageTime_Type=TimeStamp
_DeviceUsageTime_Object=MibTableColumn
deviceUsageTime=_DeviceUsageTime_Object((1,3,6,1,4,1,3417,2,4,1,1,1,7),_DeviceUsageTime_Type())
deviceUsageTime.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceUsageTime.setStatus(_A)
if mibBuilder.loadTexts:deviceUsageTime.setUnits('Hundredths of seconds')
_DeviceUsageMIBNotifications_ObjectIdentity=ObjectIdentity
deviceUsageMIBNotifications=_DeviceUsageMIBNotifications_ObjectIdentity((1,3,6,1,4,1,3417,2,4,2))
_DeviceUsageMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
deviceUsageMIBNotificationsPrefix=_DeviceUsageMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,3417,2,4,2,0))
deviceUsageTrap=NotificationType((1,3,6,1,4,1,3417,2,4,2,0,1))
deviceUsageTrap.setObjects(*((_C,_F),(_C,_G),(_C,_H)))
if mibBuilder.loadTexts:deviceUsageTrap.setStatus('deprecated')
mibBuilder.exportSymbols(_C,**{'Percent':Percent,'UsageStatus':UsageStatus,'deviceUsageMIB':deviceUsageMIB,'deviceUsageMIBObjects':deviceUsageMIBObjects,'deviceUsageTable':deviceUsageTable,'deviceUsageEntry':deviceUsageEntry,_E:deviceUsageIndex,'deviceUsageTrapEnabled':deviceUsageTrapEnabled,_F:deviceUsageName,_G:deviceUsagePercent,'deviceUsageHigh':deviceUsageHigh,_H:deviceUsageStatus,'deviceUsageTime':deviceUsageTime,'deviceUsageMIBNotifications':deviceUsageMIBNotifications,'deviceUsageMIBNotificationsPrefix':deviceUsageMIBNotificationsPrefix,'deviceUsageTrap':deviceUsageTrap})