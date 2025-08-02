_F='deviceDiskStatus'
_E='deviceDiskIndex'
_D='Integer32'
_C='BLUECOAT-SG-DISK-MIB'
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
deviceDiskMIB=ModuleIdentity((1,3,6,1,4,1,3417,2,2))
if mibBuilder.loadTexts:deviceDiskMIB.setRevisions(('2013-07-11 03:00','2007-11-05 03:00','2002-11-06 03:00'))
class DiskStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('present',1),('initializing',2),('inserted',3),('offline',4),('removed',5),('notpresent',6),('empty',7),('ioerror',8),('unusable',9),('unknown',10)))
_DeviceDiskMIBObjects_ObjectIdentity=ObjectIdentity
deviceDiskMIBObjects=_DeviceDiskMIBObjects_ObjectIdentity((1,3,6,1,4,1,3417,2,2,1))
_DeviceDiskValues_ObjectIdentity=ObjectIdentity
deviceDiskValues=_DeviceDiskValues_ObjectIdentity((1,3,6,1,4,1,3417,2,2,1,1))
_DeviceDiskValueTable_Object=MibTable
deviceDiskValueTable=_DeviceDiskValueTable_Object((1,3,6,1,4,1,3417,2,2,1,1,1))
if mibBuilder.loadTexts:deviceDiskValueTable.setStatus(_A)
_DeviceDiskValueEntry_Object=MibTableRow
deviceDiskValueEntry=_DeviceDiskValueEntry_Object((1,3,6,1,4,1,3417,2,2,1,1,1,1))
deviceDiskValueEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:deviceDiskValueEntry.setStatus(_A)
class _DeviceDiskIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DeviceDiskIndex_Type.__name__=_D
_DeviceDiskIndex_Object=MibTableColumn
deviceDiskIndex=_DeviceDiskIndex_Object((1,3,6,1,4,1,3417,2,2,1,1,1,1,1),_DeviceDiskIndex_Type())
deviceDiskIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:deviceDiskIndex.setStatus(_A)
_DeviceDiskTrapEnabled_Type=TruthValue
_DeviceDiskTrapEnabled_Object=MibTableColumn
deviceDiskTrapEnabled=_DeviceDiskTrapEnabled_Object((1,3,6,1,4,1,3417,2,2,1,1,1,1,2),_DeviceDiskTrapEnabled_Type())
deviceDiskTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceDiskTrapEnabled.setStatus(_A)
_DeviceDiskStatus_Type=DiskStatus
_DeviceDiskStatus_Object=MibTableColumn
deviceDiskStatus=_DeviceDiskStatus_Object((1,3,6,1,4,1,3417,2,2,1,1,1,1,3),_DeviceDiskStatus_Type())
deviceDiskStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceDiskStatus.setStatus(_A)
_DeviceDiskTimeStamp_Type=TimeStamp
_DeviceDiskTimeStamp_Object=MibTableColumn
deviceDiskTimeStamp=_DeviceDiskTimeStamp_Object((1,3,6,1,4,1,3417,2,2,1,1,1,1,4),_DeviceDiskTimeStamp_Type())
deviceDiskTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceDiskTimeStamp.setStatus(_A)
if mibBuilder.loadTexts:deviceDiskTimeStamp.setUnits('Hundredths of seconds')
_DeviceDiskVendor_Type=DisplayString
_DeviceDiskVendor_Object=MibTableColumn
deviceDiskVendor=_DeviceDiskVendor_Object((1,3,6,1,4,1,3417,2,2,1,1,1,1,5),_DeviceDiskVendor_Type())
deviceDiskVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceDiskVendor.setStatus(_A)
_DeviceDiskProduct_Type=DisplayString
_DeviceDiskProduct_Object=MibTableColumn
deviceDiskProduct=_DeviceDiskProduct_Object((1,3,6,1,4,1,3417,2,2,1,1,1,1,6),_DeviceDiskProduct_Type())
deviceDiskProduct.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceDiskProduct.setStatus(_A)
_DeviceDiskRevision_Type=DisplayString
_DeviceDiskRevision_Object=MibTableColumn
deviceDiskRevision=_DeviceDiskRevision_Object((1,3,6,1,4,1,3417,2,2,1,1,1,1,7),_DeviceDiskRevision_Type())
deviceDiskRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceDiskRevision.setStatus(_A)
_DeviceDiskSerialN_Type=DisplayString
_DeviceDiskSerialN_Object=MibTableColumn
deviceDiskSerialN=_DeviceDiskSerialN_Object((1,3,6,1,4,1,3417,2,2,1,1,1,1,8),_DeviceDiskSerialN_Type())
deviceDiskSerialN.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceDiskSerialN.setStatus(_A)
_DeviceDiskBlockSize_Type=Counter32
_DeviceDiskBlockSize_Object=MibTableColumn
deviceDiskBlockSize=_DeviceDiskBlockSize_Object((1,3,6,1,4,1,3417,2,2,1,1,1,1,9),_DeviceDiskBlockSize_Type())
deviceDiskBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceDiskBlockSize.setStatus(_A)
if mibBuilder.loadTexts:deviceDiskBlockSize.setUnits('Bytes')
_DeviceDiskBlockCount_Type=Counter32
_DeviceDiskBlockCount_Object=MibTableColumn
deviceDiskBlockCount=_DeviceDiskBlockCount_Object((1,3,6,1,4,1,3417,2,2,1,1,1,1,10),_DeviceDiskBlockCount_Type())
deviceDiskBlockCount.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceDiskBlockCount.setStatus(_A)
_DeviceDiskMIBNotifications_ObjectIdentity=ObjectIdentity
deviceDiskMIBNotifications=_DeviceDiskMIBNotifications_ObjectIdentity((1,3,6,1,4,1,3417,2,2,2))
_DeviceDiskMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
deviceDiskMIBNotificationsPrefix=_DeviceDiskMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,3417,2,2,2,0))
deviceDiskTrap=NotificationType((1,3,6,1,4,1,3417,2,2,2,0,1))
deviceDiskTrap.setObjects((_C,_F))
if mibBuilder.loadTexts:deviceDiskTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'DiskStatus':DiskStatus,'deviceDiskMIB':deviceDiskMIB,'deviceDiskMIBObjects':deviceDiskMIBObjects,'deviceDiskValues':deviceDiskValues,'deviceDiskValueTable':deviceDiskValueTable,'deviceDiskValueEntry':deviceDiskValueEntry,_E:deviceDiskIndex,'deviceDiskTrapEnabled':deviceDiskTrapEnabled,_F:deviceDiskStatus,'deviceDiskTimeStamp':deviceDiskTimeStamp,'deviceDiskVendor':deviceDiskVendor,'deviceDiskProduct':deviceDiskProduct,'deviceDiskRevision':deviceDiskRevision,'deviceDiskSerialN':deviceDiskSerialN,'deviceDiskBlockSize':deviceDiskBlockSize,'deviceDiskBlockCount':deviceDiskBlockCount,'deviceDiskMIBNotifications':deviceDiskMIBNotifications,'deviceDiskMIBNotificationsPrefix':deviceDiskMIBNotificationsPrefix,'deviceDiskTrap':deviceDiskTrap})