_O='apUsbcSysCpuUtil'
_N='apUsbcSysAllBogoMips'
_M='apUsbcSysMyBogoMips'
_L='apUsbcSysKernelMemUtil'
_K='apUsbcSysAppMemUtil'
_J='apUsbcSysMemSzGB'
_I='apUsbcSysMemSzMB'
_H='apUsbcSysCpuSpeedMHz'
_G='apUsbcSysCpuCount'
_F='apUsbcSysCpuUtilAll'
_E='apUsbcSysCpuNum'
_D='Integer32'
_C='read-only'
_B='APUSBCSYS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acmepacketMgmt,=mibBuilder.importSymbols('ACMEPACKET-SMI','acmepacketMgmt')
ApHardwareModuleFamily,ApPhyPortType,ApPresence,ApRedundancyState,ApServerStatus=mibBuilder.importSymbols('ACMEPACKET-TC','ApHardwareModuleFamily','ApPhyPortType','ApPresence','ApRedundancyState','ApServerStatus')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
apUsbcSysModule=ModuleIdentity((1,3,6,1,4,1,9148,3,17))
if mibBuilder.loadTexts:apUsbcSysModule.setRevisions(('2012-03-07 00:00',))
class UsbcSysPercent(TextualConvention,Gauge32):status=_A;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ApUsbcSysMIBObjects_ObjectIdentity=ObjectIdentity
apUsbcSysMIBObjects=_ApUsbcSysMIBObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,17,1))
_ApUsbcSysObjects_ObjectIdentity=ObjectIdentity
apUsbcSysObjects=_ApUsbcSysObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,17,1,1))
_ApUsbcSysCpuUtilAll_Type=UsbcSysPercent
_ApUsbcSysCpuUtilAll_Object=MibScalar
apUsbcSysCpuUtilAll=_ApUsbcSysCpuUtilAll_Object((1,3,6,1,4,1,9148,3,17,1,1,1),_ApUsbcSysCpuUtilAll_Type())
apUsbcSysCpuUtilAll.setMaxAccess(_C)
if mibBuilder.loadTexts:apUsbcSysCpuUtilAll.setStatus(_A)
class _ApUsbcSysCpuCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ApUsbcSysCpuCount_Type.__name__=_D
_ApUsbcSysCpuCount_Object=MibScalar
apUsbcSysCpuCount=_ApUsbcSysCpuCount_Object((1,3,6,1,4,1,9148,3,17,1,1,2),_ApUsbcSysCpuCount_Type())
apUsbcSysCpuCount.setMaxAccess(_C)
if mibBuilder.loadTexts:apUsbcSysCpuCount.setStatus(_A)
_ApUsbcSysCpuSpeedMHz_Type=Integer32
_ApUsbcSysCpuSpeedMHz_Object=MibScalar
apUsbcSysCpuSpeedMHz=_ApUsbcSysCpuSpeedMHz_Object((1,3,6,1,4,1,9148,3,17,1,1,3),_ApUsbcSysCpuSpeedMHz_Type())
apUsbcSysCpuSpeedMHz.setMaxAccess(_C)
if mibBuilder.loadTexts:apUsbcSysCpuSpeedMHz.setStatus(_A)
_ApUsbcSysMemSzMB_Type=Integer32
_ApUsbcSysMemSzMB_Object=MibScalar
apUsbcSysMemSzMB=_ApUsbcSysMemSzMB_Object((1,3,6,1,4,1,9148,3,17,1,1,4),_ApUsbcSysMemSzMB_Type())
apUsbcSysMemSzMB.setMaxAccess(_C)
if mibBuilder.loadTexts:apUsbcSysMemSzMB.setStatus(_A)
_ApUsbcSysMemSzGB_Type=Integer32
_ApUsbcSysMemSzGB_Object=MibScalar
apUsbcSysMemSzGB=_ApUsbcSysMemSzGB_Object((1,3,6,1,4,1,9148,3,17,1,1,5),_ApUsbcSysMemSzGB_Type())
apUsbcSysMemSzGB.setMaxAccess(_C)
if mibBuilder.loadTexts:apUsbcSysMemSzGB.setStatus(_A)
_ApUsbcSysAppMemUtil_Type=UsbcSysPercent
_ApUsbcSysAppMemUtil_Object=MibScalar
apUsbcSysAppMemUtil=_ApUsbcSysAppMemUtil_Object((1,3,6,1,4,1,9148,3,17,1,1,6),_ApUsbcSysAppMemUtil_Type())
apUsbcSysAppMemUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:apUsbcSysAppMemUtil.setStatus(_A)
_ApUsbcSysKernelMemUtil_Type=UsbcSysPercent
_ApUsbcSysKernelMemUtil_Object=MibScalar
apUsbcSysKernelMemUtil=_ApUsbcSysKernelMemUtil_Object((1,3,6,1,4,1,9148,3,17,1,1,7),_ApUsbcSysKernelMemUtil_Type())
apUsbcSysKernelMemUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:apUsbcSysKernelMemUtil.setStatus(_A)
_ApUsbcSysMyBogoMips_Type=Integer32
_ApUsbcSysMyBogoMips_Object=MibScalar
apUsbcSysMyBogoMips=_ApUsbcSysMyBogoMips_Object((1,3,6,1,4,1,9148,3,17,1,1,8),_ApUsbcSysMyBogoMips_Type())
apUsbcSysMyBogoMips.setMaxAccess(_C)
if mibBuilder.loadTexts:apUsbcSysMyBogoMips.setStatus(_A)
_ApUsbcSysAllBogoMips_Type=Integer32
_ApUsbcSysAllBogoMips_Object=MibScalar
apUsbcSysAllBogoMips=_ApUsbcSysAllBogoMips_Object((1,3,6,1,4,1,9148,3,17,1,1,9),_ApUsbcSysAllBogoMips_Type())
apUsbcSysAllBogoMips.setMaxAccess(_C)
if mibBuilder.loadTexts:apUsbcSysAllBogoMips.setStatus(_A)
_ApUsbcSysCpuTblObjects_ObjectIdentity=ObjectIdentity
apUsbcSysCpuTblObjects=_ApUsbcSysCpuTblObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,17,1,1,10))
_ApUsbcSysCpuTable_Object=MibTable
apUsbcSysCpuTable=_ApUsbcSysCpuTable_Object((1,3,6,1,4,1,9148,3,17,1,1,10,1))
if mibBuilder.loadTexts:apUsbcSysCpuTable.setStatus(_A)
_ApUsbcSysCpuEntry_Object=MibTableRow
apUsbcSysCpuEntry=_ApUsbcSysCpuEntry_Object((1,3,6,1,4,1,9148,3,17,1,1,10,1,1))
apUsbcSysCpuEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:apUsbcSysCpuEntry.setStatus(_A)
class _ApUsbcSysCpuNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ApUsbcSysCpuNum_Type.__name__=_D
_ApUsbcSysCpuNum_Object=MibTableColumn
apUsbcSysCpuNum=_ApUsbcSysCpuNum_Object((1,3,6,1,4,1,9148,3,17,1,1,10,1,1,1),_ApUsbcSysCpuNum_Type())
apUsbcSysCpuNum.setMaxAccess(_C)
if mibBuilder.loadTexts:apUsbcSysCpuNum.setStatus(_A)
_ApUsbcSysCpuUtil_Type=UsbcSysPercent
_ApUsbcSysCpuUtil_Object=MibTableColumn
apUsbcSysCpuUtil=_ApUsbcSysCpuUtil_Object((1,3,6,1,4,1,9148,3,17,1,1,10,1,1,2),_ApUsbcSysCpuUtil_Type())
apUsbcSysCpuUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:apUsbcSysCpuUtil.setStatus(_A)
_ApUsbcSysNotificationObjects_ObjectIdentity=ObjectIdentity
apUsbcSysNotificationObjects=_ApUsbcSysNotificationObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,17,2))
_ApUsbcSysNotifObjects_ObjectIdentity=ObjectIdentity
apUsbcSysNotifObjects=_ApUsbcSysNotifObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,17,2,1))
_ApUsbcSysNotifPrefix_ObjectIdentity=ObjectIdentity
apUsbcSysNotifPrefix=_ApUsbcSysNotifPrefix_ObjectIdentity((1,3,6,1,4,1,9148,3,17,2,2))
_ApUsbcSysCpuNotifications_ObjectIdentity=ObjectIdentity
apUsbcSysCpuNotifications=_ApUsbcSysCpuNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,17,2,2,1,0))
_ApUsbcSysConformance_ObjectIdentity=ObjectIdentity
apUsbcSysConformance=_ApUsbcSysConformance_ObjectIdentity((1,3,6,1,4,1,9148,3,17,3))
_ApUsbcSysObjectGroups_ObjectIdentity=ObjectIdentity
apUsbcSysObjectGroups=_ApUsbcSysObjectGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,17,3,1))
_ApUsbcSysNotificationGroups_ObjectIdentity=ObjectIdentity
apUsbcSysNotificationGroups=_ApUsbcSysNotificationGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,17,3,2))
apUsbcSysGroup=ObjectGroup((1,3,6,1,4,1,9148,3,17,3,1,1))
apUsbcSysGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:apUsbcSysGroup.setStatus(_A)
apUsbcSysCpuTblGroup=ObjectGroup((1,3,6,1,4,1,9148,3,17,3,1,2))
apUsbcSysCpuTblGroup.setObjects(*((_B,_E),(_B,_O)))
if mibBuilder.loadTexts:apUsbcSysCpuTblGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'UsbcSysPercent':UsbcSysPercent,'apUsbcSysModule':apUsbcSysModule,'apUsbcSysMIBObjects':apUsbcSysMIBObjects,'apUsbcSysObjects':apUsbcSysObjects,_F:apUsbcSysCpuUtilAll,_G:apUsbcSysCpuCount,_H:apUsbcSysCpuSpeedMHz,_I:apUsbcSysMemSzMB,_J:apUsbcSysMemSzGB,_K:apUsbcSysAppMemUtil,_L:apUsbcSysKernelMemUtil,_M:apUsbcSysMyBogoMips,_N:apUsbcSysAllBogoMips,'apUsbcSysCpuTblObjects':apUsbcSysCpuTblObjects,'apUsbcSysCpuTable':apUsbcSysCpuTable,'apUsbcSysCpuEntry':apUsbcSysCpuEntry,_E:apUsbcSysCpuNum,_O:apUsbcSysCpuUtil,'apUsbcSysNotificationObjects':apUsbcSysNotificationObjects,'apUsbcSysNotifObjects':apUsbcSysNotifObjects,'apUsbcSysNotifPrefix':apUsbcSysNotifPrefix,'apUsbcSysCpuNotifications':apUsbcSysCpuNotifications,'apUsbcSysConformance':apUsbcSysConformance,'apUsbcSysObjectGroups':apUsbcSysObjectGroups,'apUsbcSysGroup':apUsbcSysGroup,'apUsbcSysCpuTblGroup':apUsbcSysCpuTblGroup,'apUsbcSysNotificationGroups':apUsbcSysNotificationGroups})