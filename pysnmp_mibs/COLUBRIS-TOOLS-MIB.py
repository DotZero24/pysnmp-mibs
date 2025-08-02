_R='colubrisToolsNotificationGroup'
_Q='colubrisToolsMIBGroup'
_P='traceStatusNotification'
_O='traceNotificationEnabled'
_N='traceCaptureFilter'
_M='tracePacketSize'
_L='traceNumberOfPackets'
_K='traceTimeout'
_J='traceCaptureDestinationURL'
_I='traceCaptureDestination'
_H='traceInterface'
_G='ColubrisNotificationEnable'
_F='traceCaptureStatus'
_E='Integer32'
_D='Unsigned32'
_C='read-write'
_B='current'
_A='COLUBRIS-TOOLS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ColubrisNotificationEnable,=mibBuilder.importSymbols('COLUBRIS-TC',_G)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
colubrisToolsMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,12))
_ColubrisToolsMIBObjects_ObjectIdentity=ObjectIdentity
colubrisToolsMIBObjects=_ColubrisToolsMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,12,1))
_TraceToolConfig_ObjectIdentity=ObjectIdentity
traceToolConfig=_TraceToolConfig_ObjectIdentity((1,3,6,1,4,1,8744,5,12,1,1))
_TraceInterface_Type=InterfaceIndex
_TraceInterface_Object=MibScalar
traceInterface=_TraceInterface_Object((1,3,6,1,4,1,8744,5,12,1,1,1),_TraceInterface_Type())
traceInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:traceInterface.setStatus(_B)
class _TraceCaptureDestination_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_TraceCaptureDestination_Type.__name__=_E
_TraceCaptureDestination_Object=MibScalar
traceCaptureDestination=_TraceCaptureDestination_Object((1,3,6,1,4,1,8744,5,12,1,1,2),_TraceCaptureDestination_Type())
traceCaptureDestination.setMaxAccess(_C)
if mibBuilder.loadTexts:traceCaptureDestination.setStatus(_B)
_TraceCaptureDestinationURL_Type=DisplayString
_TraceCaptureDestinationURL_Object=MibScalar
traceCaptureDestinationURL=_TraceCaptureDestinationURL_Object((1,3,6,1,4,1,8744,5,12,1,1,3),_TraceCaptureDestinationURL_Type())
traceCaptureDestinationURL.setMaxAccess(_C)
if mibBuilder.loadTexts:traceCaptureDestinationURL.setStatus(_B)
class _TraceTimeout_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_TraceTimeout_Type.__name__=_D
_TraceTimeout_Object=MibScalar
traceTimeout=_TraceTimeout_Object((1,3,6,1,4,1,8744,5,12,1,1,4),_TraceTimeout_Type())
traceTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:traceTimeout.setStatus(_B)
if mibBuilder.loadTexts:traceTimeout.setUnits('seconds')
class _TraceNumberOfPackets_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_TraceNumberOfPackets_Type.__name__=_D
_TraceNumberOfPackets_Object=MibScalar
traceNumberOfPackets=_TraceNumberOfPackets_Object((1,3,6,1,4,1,8744,5,12,1,1,5),_TraceNumberOfPackets_Type())
traceNumberOfPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:traceNumberOfPackets.setStatus(_B)
if mibBuilder.loadTexts:traceNumberOfPackets.setUnits('packets')
class _TracePacketSize_Type(Unsigned32):defaultValue=128;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(68,4096))
_TracePacketSize_Type.__name__=_D
_TracePacketSize_Object=MibScalar
tracePacketSize=_TracePacketSize_Object((1,3,6,1,4,1,8744,5,12,1,1,6),_TracePacketSize_Type())
tracePacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tracePacketSize.setStatus(_B)
if mibBuilder.loadTexts:tracePacketSize.setUnits('bytes')
_TraceCaptureFilter_Type=DisplayString
_TraceCaptureFilter_Object=MibScalar
traceCaptureFilter=_TraceCaptureFilter_Object((1,3,6,1,4,1,8744,5,12,1,1,7),_TraceCaptureFilter_Type())
traceCaptureFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:traceCaptureFilter.setStatus(_B)
class _TraceCaptureStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_TraceCaptureStatus_Type.__name__=_E
_TraceCaptureStatus_Object=MibScalar
traceCaptureStatus=_TraceCaptureStatus_Object((1,3,6,1,4,1,8744,5,12,1,1,8),_TraceCaptureStatus_Type())
traceCaptureStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:traceCaptureStatus.setStatus(_B)
class _TraceNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=2
_TraceNotificationEnabled_Type.__name__=_G
_TraceNotificationEnabled_Object=MibScalar
traceNotificationEnabled=_TraceNotificationEnabled_Object((1,3,6,1,4,1,8744,5,12,1,1,9),_TraceNotificationEnabled_Type())
traceNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:traceNotificationEnabled.setStatus(_B)
_ColubrisToolsMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
colubrisToolsMIBNotificationPrefix=_ColubrisToolsMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,8744,5,12,2))
_ColubrisToolsMIBNotifications_ObjectIdentity=ObjectIdentity
colubrisToolsMIBNotifications=_ColubrisToolsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,8744,5,12,2,0))
_ColubrisToolsMIBConformance_ObjectIdentity=ObjectIdentity
colubrisToolsMIBConformance=_ColubrisToolsMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,12,3))
_ColubrisToolsMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisToolsMIBCompliances=_ColubrisToolsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,12,3,1))
_ColubrisToolsMIBGroups_ObjectIdentity=ObjectIdentity
colubrisToolsMIBGroups=_ColubrisToolsMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,12,3,2))
colubrisToolsMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,12,3,2,1))
colubrisToolsMIBGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_F),(_A,_O)))
if mibBuilder.loadTexts:colubrisToolsMIBGroup.setStatus(_B)
traceStatusNotification=NotificationType((1,3,6,1,4,1,8744,5,12,2,0,1))
traceStatusNotification.setObjects((_A,_F))
if mibBuilder.loadTexts:traceStatusNotification.setStatus(_B)
colubrisToolsNotificationGroup=NotificationGroup((1,3,6,1,4,1,8744,5,12,3,2,2))
colubrisToolsNotificationGroup.setObjects((_A,_P))
if mibBuilder.loadTexts:colubrisToolsNotificationGroup.setStatus(_B)
colubrisToolsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,12,3,1,1))
colubrisToolsMIBCompliance.setObjects(*((_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:colubrisToolsMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'colubrisToolsMIB':colubrisToolsMIB,'colubrisToolsMIBObjects':colubrisToolsMIBObjects,'traceToolConfig':traceToolConfig,_H:traceInterface,_I:traceCaptureDestination,_J:traceCaptureDestinationURL,_K:traceTimeout,_L:traceNumberOfPackets,_M:tracePacketSize,_N:traceCaptureFilter,_F:traceCaptureStatus,_O:traceNotificationEnabled,'colubrisToolsMIBNotificationPrefix':colubrisToolsMIBNotificationPrefix,'colubrisToolsMIBNotifications':colubrisToolsMIBNotifications,_P:traceStatusNotification,'colubrisToolsMIBConformance':colubrisToolsMIBConformance,'colubrisToolsMIBCompliances':colubrisToolsMIBCompliances,'colubrisToolsMIBCompliance':colubrisToolsMIBCompliance,'colubrisToolsMIBGroups':colubrisToolsMIBGroups,_Q:colubrisToolsMIBGroup,_R:colubrisToolsNotificationGroup})