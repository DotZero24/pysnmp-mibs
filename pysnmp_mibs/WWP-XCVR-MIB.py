_J='wwpXcvrErrorType'
_I='wwpXcvrEventType'
_H='wwpXcvrPortXcvrId'
_G='wwpXcvrPortId'
_F='read-write'
_E='wwpXcvrId'
_D='WWP-XCVR-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpXcvrMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,14))
if mibBuilder.loadTexts:wwpXcvrMIB.setRevisions(('2001-04-03 17:00',))
_WwpXcvrMIBObjects_ObjectIdentity=ObjectIdentity
wwpXcvrMIBObjects=_WwpXcvrMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,14,1))
_WwpXcvr_ObjectIdentity=ObjectIdentity
wwpXcvr=_WwpXcvr_ObjectIdentity((1,3,6,1,4,1,6141,2,14,1,1))
_WwpXcvrTable_Object=MibTable
wwpXcvrTable=_WwpXcvrTable_Object((1,3,6,1,4,1,6141,2,14,1,1,1))
if mibBuilder.loadTexts:wwpXcvrTable.setStatus(_A)
_WwpXcvrEntry_Object=MibTableRow
wwpXcvrEntry=_WwpXcvrEntry_Object((1,3,6,1,4,1,6141,2,14,1,1,1,1))
wwpXcvrEntry.setIndexNames((0,_D,_H),(0,_D,_E))
if mibBuilder.loadTexts:wwpXcvrEntry.setStatus(_A)
class _WwpXcvrPortXcvrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpXcvrPortXcvrId_Type.__name__=_B
_WwpXcvrPortXcvrId_Object=MibTableColumn
wwpXcvrPortXcvrId=_WwpXcvrPortXcvrId_Object((1,3,6,1,4,1,6141,2,14,1,1,1,1,1),_WwpXcvrPortXcvrId_Type())
wwpXcvrPortXcvrId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpXcvrPortXcvrId.setStatus(_A)
class _WwpXcvrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WwpXcvrId_Type.__name__=_B
_WwpXcvrId_Object=MibTableColumn
wwpXcvrId=_WwpXcvrId_Object((1,3,6,1,4,1,6141,2,14,1,1,1,1,2),_WwpXcvrId_Type())
wwpXcvrId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpXcvrId.setStatus(_A)
class _WwpXcvrFiberType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('lx',1),('sx',2),('cx',3),('t',4),('unknown',5)))
_WwpXcvrFiberType_Type.__name__=_B
_WwpXcvrFiberType_Object=MibTableColumn
wwpXcvrFiberType=_WwpXcvrFiberType_Object((1,3,6,1,4,1,6141,2,14,1,1,1,1,3),_WwpXcvrFiberType_Type())
wwpXcvrFiberType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpXcvrFiberType.setStatus(_A)
_WwpXcvrVendorName_Type=DisplayString
_WwpXcvrVendorName_Object=MibTableColumn
wwpXcvrVendorName=_WwpXcvrVendorName_Object((1,3,6,1,4,1,6141,2,14,1,1,1,1,4),_WwpXcvrVendorName_Type())
wwpXcvrVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpXcvrVendorName.setStatus(_A)
_WwpXcvrPartNum_Type=DisplayString
_WwpXcvrPartNum_Object=MibTableColumn
wwpXcvrPartNum=_WwpXcvrPartNum_Object((1,3,6,1,4,1,6141,2,14,1,1,1,1,5),_WwpXcvrPartNum_Type())
wwpXcvrPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpXcvrPartNum.setStatus(_A)
_WwpXcvrPartRev_Type=DisplayString
_WwpXcvrPartRev_Object=MibTableColumn
wwpXcvrPartRev=_WwpXcvrPartRev_Object((1,3,6,1,4,1,6141,2,14,1,1,1,1,6),_WwpXcvrPartRev_Type())
wwpXcvrPartRev.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpXcvrPartRev.setStatus(_A)
class _WwpXcvrTxEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_WwpXcvrTxEnabled_Type.__name__=_B
_WwpXcvrTxEnabled_Object=MibTableColumn
wwpXcvrTxEnabled=_WwpXcvrTxEnabled_Object((1,3,6,1,4,1,6141,2,14,1,1,1,1,7),_WwpXcvrTxEnabled_Type())
wwpXcvrTxEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpXcvrTxEnabled.setStatus(_A)
class _WwpXcvrRxSignalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('detected',1),('notDetected',2)))
_WwpXcvrRxSignalStatus_Type.__name__=_B
_WwpXcvrRxSignalStatus_Object=MibTableColumn
wwpXcvrRxSignalStatus=_WwpXcvrRxSignalStatus_Object((1,3,6,1,4,1,6141,2,14,1,1,1,1,8),_WwpXcvrRxSignalStatus_Type())
wwpXcvrRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpXcvrRxSignalStatus.setStatus(_A)
class _WwpXcvrTxFaultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fault',1),('noFault',2)))
_WwpXcvrTxFaultStatus_Type.__name__=_B
_WwpXcvrTxFaultStatus_Object=MibTableColumn
wwpXcvrTxFaultStatus=_WwpXcvrTxFaultStatus_Object((1,3,6,1,4,1,6141,2,14,1,1,1,1,9),_WwpXcvrTxFaultStatus_Type())
wwpXcvrTxFaultStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpXcvrTxFaultStatus.setStatus(_A)
_WwpXcvrPortTable_Object=MibTable
wwpXcvrPortTable=_WwpXcvrPortTable_Object((1,3,6,1,4,1,6141,2,14,1,1,2))
if mibBuilder.loadTexts:wwpXcvrPortTable.setStatus(_A)
_WwpXcvrPortEntry_Object=MibTableRow
wwpXcvrPortEntry=_WwpXcvrPortEntry_Object((1,3,6,1,4,1,6141,2,14,1,1,2,1))
wwpXcvrPortEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:wwpXcvrPortEntry.setStatus(_A)
class _WwpXcvrPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpXcvrPortId_Type.__name__=_B
_WwpXcvrPortId_Object=MibTableColumn
wwpXcvrPortId=_WwpXcvrPortId_Object((1,3,6,1,4,1,6141,2,14,1,1,2,1,1),_WwpXcvrPortId_Type())
wwpXcvrPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpXcvrPortId.setStatus(_A)
class _WwpXcvrPortHoldDownTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_WwpXcvrPortHoldDownTime_Type.__name__=_B
_WwpXcvrPortHoldDownTime_Object=MibTableColumn
wwpXcvrPortHoldDownTime=_WwpXcvrPortHoldDownTime_Object((1,3,6,1,4,1,6141,2,14,1,1,2,1,2),_WwpXcvrPortHoldDownTime_Type())
wwpXcvrPortHoldDownTime.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpXcvrPortHoldDownTime.setStatus('deprecated')
class _WwpXcvrPortRedOrDiagMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_WwpXcvrPortRedOrDiagMode_Type.__name__=_B
_WwpXcvrPortRedOrDiagMode_Object=MibTableColumn
wwpXcvrPortRedOrDiagMode=_WwpXcvrPortRedOrDiagMode_Object((1,3,6,1,4,1,6141,2,14,1,1,2,1,3),_WwpXcvrPortRedOrDiagMode_Type())
wwpXcvrPortRedOrDiagMode.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpXcvrPortRedOrDiagMode.setStatus(_A)
class _WwpXcvrPortPreferredXcvr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WwpXcvrPortPreferredXcvr_Type.__name__=_B
_WwpXcvrPortPreferredXcvr_Object=MibTableColumn
wwpXcvrPortPreferredXcvr=_WwpXcvrPortPreferredXcvr_Object((1,3,6,1,4,1,6141,2,14,1,1,2,1,4),_WwpXcvrPortPreferredXcvr_Type())
wwpXcvrPortPreferredXcvr.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpXcvrPortPreferredXcvr.setStatus(_A)
class _WwpXcvrPortActiveXcvr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WwpXcvrPortActiveXcvr_Type.__name__=_B
_WwpXcvrPortActiveXcvr_Object=MibTableColumn
wwpXcvrPortActiveXcvr=_WwpXcvrPortActiveXcvr_Object((1,3,6,1,4,1,6141,2,14,1,1,2,1,5),_WwpXcvrPortActiveXcvr_Type())
wwpXcvrPortActiveXcvr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpXcvrPortActiveXcvr.setStatus(_A)
_WwpXcvrNotif_ObjectIdentity=ObjectIdentity
wwpXcvrNotif=_WwpXcvrNotif_ObjectIdentity((1,3,6,1,4,1,6141,2,14,1,2))
class _WwpXcvrEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('up',1),('down',2),('select',3)))
_WwpXcvrEventType_Type.__name__=_B
_WwpXcvrEventType_Object=MibScalar
wwpXcvrEventType=_WwpXcvrEventType_Object((1,3,6,1,4,1,6141,2,14,1,2,1),_WwpXcvrEventType_Type())
wwpXcvrEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpXcvrEventType.setStatus(_A)
class _WwpXcvrErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('chksumFailed',1),('opticalFault',2)))
_WwpXcvrErrorType_Type.__name__=_B
_WwpXcvrErrorType_Object=MibScalar
wwpXcvrErrorType=_WwpXcvrErrorType_Object((1,3,6,1,4,1,6141,2,14,1,2,2),_WwpXcvrErrorType_Type())
wwpXcvrErrorType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpXcvrErrorType.setStatus(_A)
_WwpXcvrMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpXcvrMIBNotificationPrefix=_WwpXcvrMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,14,2))
_WwpXcvrMIBNotifications_ObjectIdentity=ObjectIdentity
wwpXcvrMIBNotifications=_WwpXcvrMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,14,2,0))
_WwpXcvrMIBConformance_ObjectIdentity=ObjectIdentity
wwpXcvrMIBConformance=_WwpXcvrMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,14,3))
_WwpXcvrMIBCompliances_ObjectIdentity=ObjectIdentity
wwpXcvrMIBCompliances=_WwpXcvrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,14,3,1))
_WwpXcvrMIBGroups_ObjectIdentity=ObjectIdentity
wwpXcvrMIBGroups=_WwpXcvrMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,14,3,2))
wwpXcvrLinkStateChangeNotification=NotificationType((1,3,6,1,4,1,6141,2,14,2,0,4))
wwpXcvrLinkStateChangeNotification.setObjects(*((_D,_G),(_D,_E),(_D,_I)))
if mibBuilder.loadTexts:wwpXcvrLinkStateChangeNotification.setStatus(_A)
wwpXcvrErrorTypeNotification=NotificationType((1,3,6,1,4,1,6141,2,14,2,0,5))
wwpXcvrErrorTypeNotification.setObjects(*((_D,_G),(_D,_E),(_D,_J)))
if mibBuilder.loadTexts:wwpXcvrErrorTypeNotification.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'wwpXcvrMIB':wwpXcvrMIB,'wwpXcvrMIBObjects':wwpXcvrMIBObjects,'wwpXcvr':wwpXcvr,'wwpXcvrTable':wwpXcvrTable,'wwpXcvrEntry':wwpXcvrEntry,_H:wwpXcvrPortXcvrId,_E:wwpXcvrId,'wwpXcvrFiberType':wwpXcvrFiberType,'wwpXcvrVendorName':wwpXcvrVendorName,'wwpXcvrPartNum':wwpXcvrPartNum,'wwpXcvrPartRev':wwpXcvrPartRev,'wwpXcvrTxEnabled':wwpXcvrTxEnabled,'wwpXcvrRxSignalStatus':wwpXcvrRxSignalStatus,'wwpXcvrTxFaultStatus':wwpXcvrTxFaultStatus,'wwpXcvrPortTable':wwpXcvrPortTable,'wwpXcvrPortEntry':wwpXcvrPortEntry,_G:wwpXcvrPortId,'wwpXcvrPortHoldDownTime':wwpXcvrPortHoldDownTime,'wwpXcvrPortRedOrDiagMode':wwpXcvrPortRedOrDiagMode,'wwpXcvrPortPreferredXcvr':wwpXcvrPortPreferredXcvr,'wwpXcvrPortActiveXcvr':wwpXcvrPortActiveXcvr,'wwpXcvrNotif':wwpXcvrNotif,_I:wwpXcvrEventType,_J:wwpXcvrErrorType,'wwpXcvrMIBNotificationPrefix':wwpXcvrMIBNotificationPrefix,'wwpXcvrMIBNotifications':wwpXcvrMIBNotifications,'wwpXcvrLinkStateChangeNotification':wwpXcvrLinkStateChangeNotification,'wwpXcvrErrorTypeNotification':wwpXcvrErrorTypeNotification,'wwpXcvrMIBConformance':wwpXcvrMIBConformance,'wwpXcvrMIBCompliances':wwpXcvrMIBCompliances,'wwpXcvrMIBGroups':wwpXcvrMIBGroups})