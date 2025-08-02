_l='xgcpDefaultMGCGroup'
_k='xgcpVoiceQualityGroup'
_j='xgcpPackageGroup'
_i='xgcpExtensionGroup'
_h='xgcpCoreGroup'
_g='xgcpMGCCfgTimeStamp'
_f='xgcpMGCCfgConnStatus'
_e='xgcpMGCCfgUDPPort'
_d='xgcpMGCCfgAddress'
_c='xgcpHigherBoundForLatency'
_b='xgcpLowerBoundForLatency'
_a='xgcpHigherBoundForJitter'
_Z='xgcpLowerBoundForJitter'
_Y='xgcpHigherBoundForPacketLoss'
_X='xgcpLowerBoundForPacketLoss'
_W='xgcpDefaultPackage'
_V='xgcpCapabilityPackageEnable'
_U='xgcpRestartDelay'
_T='xgcpRestartInProgressMWD'
_S='xgcpFailMessages'
_R='xgcpSuccessMessages'
_Q='xgcpUnRecognizedPackets'
_P='xgcpAdminStatus'
_O='xgcpRequestRetries'
_N='xgcpRequestTimeOut'
_M='xgcpInBadVersions'
_L='xgcpCapabilityPackageName'
_K='not-accessible'
_J='xgcpIPAddress'
_I='TruthValue'
_H='xgcpOperStatus'
_G='DisplayString'
_F='milliseconds'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='XGCP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention','TimeStamp',_I)
xgcpMIB=ModuleIdentity((1,3,6,1,3,90))
if mibBuilder.loadTexts:xgcpMIB.setRevisions(('1999-02-17 00:00',))
_XgcpObjects_ObjectIdentity=ObjectIdentity
xgcpObjects=_XgcpObjects_ObjectIdentity((1,3,6,1,3,90,1))
_XgcpCoreObjects_ObjectIdentity=ObjectIdentity
xgcpCoreObjects=_XgcpCoreObjects_ObjectIdentity((1,3,6,1,3,90,1,1))
_XgcpInBadVersions_Type=Counter32
_XgcpInBadVersions_Object=MibScalar
xgcpInBadVersions=_XgcpInBadVersions_Object((1,3,6,1,3,90,1,1,1),_XgcpInBadVersions_Type())
xgcpInBadVersions.setMaxAccess(_E)
if mibBuilder.loadTexts:xgcpInBadVersions.setStatus(_A)
if mibBuilder.loadTexts:xgcpInBadVersions.setUnits('messages')
class _XgcpRequestTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_XgcpRequestTimeOut_Type.__name__=_C
_XgcpRequestTimeOut_Object=MibScalar
xgcpRequestTimeOut=_XgcpRequestTimeOut_Object((1,3,6,1,3,90,1,1,2),_XgcpRequestTimeOut_Type())
xgcpRequestTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:xgcpRequestTimeOut.setStatus(_A)
if mibBuilder.loadTexts:xgcpRequestTimeOut.setUnits(_F)
class _XgcpRequestRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_XgcpRequestRetries_Type.__name__=_C
_XgcpRequestRetries_Object=MibScalar
xgcpRequestRetries=_XgcpRequestRetries_Object((1,3,6,1,3,90,1,1,3),_XgcpRequestRetries_Type())
xgcpRequestRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:xgcpRequestRetries.setStatus(_A)
class _XgcpAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('gracefulDown',3)))
_XgcpAdminStatus_Type.__name__=_C
_XgcpAdminStatus_Object=MibScalar
xgcpAdminStatus=_XgcpAdminStatus_Object((1,3,6,1,3,90,1,1,4),_XgcpAdminStatus_Type())
xgcpAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:xgcpAdminStatus.setStatus(_A)
class _XgcpOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('shutDownInProgress',3)))
_XgcpOperStatus_Type.__name__=_C
_XgcpOperStatus_Object=MibScalar
xgcpOperStatus=_XgcpOperStatus_Object((1,3,6,1,3,90,1,1,5),_XgcpOperStatus_Type())
xgcpOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:xgcpOperStatus.setStatus(_A)
_XgcpUnRecognizedPackets_Type=Counter32
_XgcpUnRecognizedPackets_Object=MibScalar
xgcpUnRecognizedPackets=_XgcpUnRecognizedPackets_Object((1,3,6,1,3,90,1,1,6),_XgcpUnRecognizedPackets_Type())
xgcpUnRecognizedPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:xgcpUnRecognizedPackets.setStatus(_A)
_XgcpMsgStatTable_Object=MibTable
xgcpMsgStatTable=_XgcpMsgStatTable_Object((1,3,6,1,3,90,1,1,7))
if mibBuilder.loadTexts:xgcpMsgStatTable.setStatus(_A)
_XgcpMsgStatEntry_Object=MibTableRow
xgcpMsgStatEntry=_XgcpMsgStatEntry_Object((1,3,6,1,3,90,1,1,7,1))
xgcpMsgStatEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:xgcpMsgStatEntry.setStatus(_A)
_XgcpIPAddress_Type=IpAddress
_XgcpIPAddress_Object=MibTableColumn
xgcpIPAddress=_XgcpIPAddress_Object((1,3,6,1,3,90,1,1,7,1,1),_XgcpIPAddress_Type())
xgcpIPAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:xgcpIPAddress.setStatus(_A)
_XgcpSuccessMessages_Type=Counter32
_XgcpSuccessMessages_Object=MibTableColumn
xgcpSuccessMessages=_XgcpSuccessMessages_Object((1,3,6,1,3,90,1,1,7,1,2),_XgcpSuccessMessages_Type())
xgcpSuccessMessages.setMaxAccess(_E)
if mibBuilder.loadTexts:xgcpSuccessMessages.setStatus(_A)
_XgcpFailMessages_Type=Counter32
_XgcpFailMessages_Object=MibTableColumn
xgcpFailMessages=_XgcpFailMessages_Object((1,3,6,1,3,90,1,1,7,1,3),_XgcpFailMessages_Type())
xgcpFailMessages.setMaxAccess(_E)
if mibBuilder.loadTexts:xgcpFailMessages.setStatus(_A)
_XgcpExtensionObjects_ObjectIdentity=ObjectIdentity
xgcpExtensionObjects=_XgcpExtensionObjects_ObjectIdentity((1,3,6,1,3,90,1,2))
class _XgcpRestartInProgressMWD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600000))
_XgcpRestartInProgressMWD_Type.__name__=_C
_XgcpRestartInProgressMWD_Object=MibScalar
xgcpRestartInProgressMWD=_XgcpRestartInProgressMWD_Object((1,3,6,1,3,90,1,2,1),_XgcpRestartInProgressMWD_Type())
xgcpRestartInProgressMWD.setMaxAccess(_D)
if mibBuilder.loadTexts:xgcpRestartInProgressMWD.setStatus(_A)
if mibBuilder.loadTexts:xgcpRestartInProgressMWD.setUnits(_F)
class _XgcpRestartDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_XgcpRestartDelay_Type.__name__=_C
_XgcpRestartDelay_Object=MibScalar
xgcpRestartDelay=_XgcpRestartDelay_Object((1,3,6,1,3,90,1,2,2),_XgcpRestartDelay_Type())
xgcpRestartDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:xgcpRestartDelay.setStatus(_A)
if mibBuilder.loadTexts:xgcpRestartDelay.setUnits('seconds')
_XgcpPackageObjects_ObjectIdentity=ObjectIdentity
xgcpPackageObjects=_XgcpPackageObjects_ObjectIdentity((1,3,6,1,3,90,1,3))
_XgcpCapabilityPackageTable_Object=MibTable
xgcpCapabilityPackageTable=_XgcpCapabilityPackageTable_Object((1,3,6,1,3,90,1,3,1))
if mibBuilder.loadTexts:xgcpCapabilityPackageTable.setStatus(_A)
_XgcpCapabilityPackageEntry_Object=MibTableRow
xgcpCapabilityPackageEntry=_XgcpCapabilityPackageEntry_Object((1,3,6,1,3,90,1,3,1,1))
xgcpCapabilityPackageEntry.setIndexNames((1,_B,_L))
if mibBuilder.loadTexts:xgcpCapabilityPackageEntry.setStatus(_A)
class _XgcpCapabilityPackageName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_XgcpCapabilityPackageName_Type.__name__=_G
_XgcpCapabilityPackageName_Object=MibTableColumn
xgcpCapabilityPackageName=_XgcpCapabilityPackageName_Object((1,3,6,1,3,90,1,3,1,1,1),_XgcpCapabilityPackageName_Type())
xgcpCapabilityPackageName.setMaxAccess(_K)
if mibBuilder.loadTexts:xgcpCapabilityPackageName.setStatus(_A)
class _XgcpCapabilityPackageEnable_Type(TruthValue):defaultValue=1
_XgcpCapabilityPackageEnable_Type.__name__=_I
_XgcpCapabilityPackageEnable_Object=MibTableColumn
xgcpCapabilityPackageEnable=_XgcpCapabilityPackageEnable_Object((1,3,6,1,3,90,1,3,1,1,2),_XgcpCapabilityPackageEnable_Type())
xgcpCapabilityPackageEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:xgcpCapabilityPackageEnable.setStatus(_A)
class _XgcpDefaultPackage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_XgcpDefaultPackage_Type.__name__=_G
_XgcpDefaultPackage_Object=MibScalar
xgcpDefaultPackage=_XgcpDefaultPackage_Object((1,3,6,1,3,90,1,3,2),_XgcpDefaultPackage_Type())
xgcpDefaultPackage.setMaxAccess(_D)
if mibBuilder.loadTexts:xgcpDefaultPackage.setStatus(_A)
_XgcpVoiceQualityObjects_ObjectIdentity=ObjectIdentity
xgcpVoiceQualityObjects=_XgcpVoiceQualityObjects_ObjectIdentity((1,3,6,1,3,90,1,4))
class _XgcpLowerBoundForPacketLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3000))
_XgcpLowerBoundForPacketLoss_Type.__name__=_C
_XgcpLowerBoundForPacketLoss_Object=MibScalar
xgcpLowerBoundForPacketLoss=_XgcpLowerBoundForPacketLoss_Object((1,3,6,1,3,90,1,4,1),_XgcpLowerBoundForPacketLoss_Type())
xgcpLowerBoundForPacketLoss.setMaxAccess(_D)
if mibBuilder.loadTexts:xgcpLowerBoundForPacketLoss.setStatus(_A)
class _XgcpHigherBoundForPacketLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5000,25000))
_XgcpHigherBoundForPacketLoss_Type.__name__=_C
_XgcpHigherBoundForPacketLoss_Object=MibScalar
xgcpHigherBoundForPacketLoss=_XgcpHigherBoundForPacketLoss_Object((1,3,6,1,3,90,1,4,2),_XgcpHigherBoundForPacketLoss_Type())
xgcpHigherBoundForPacketLoss.setMaxAccess(_D)
if mibBuilder.loadTexts:xgcpHigherBoundForPacketLoss.setStatus(_A)
class _XgcpLowerBoundForJitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,60))
_XgcpLowerBoundForJitter_Type.__name__=_C
_XgcpLowerBoundForJitter_Object=MibScalar
xgcpLowerBoundForJitter=_XgcpLowerBoundForJitter_Object((1,3,6,1,3,90,1,4,3),_XgcpLowerBoundForJitter_Type())
xgcpLowerBoundForJitter.setMaxAccess(_D)
if mibBuilder.loadTexts:xgcpLowerBoundForJitter.setStatus(_A)
if mibBuilder.loadTexts:xgcpLowerBoundForJitter.setUnits(_F)
class _XgcpHigherBoundForJitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,200))
_XgcpHigherBoundForJitter_Type.__name__=_C
_XgcpHigherBoundForJitter_Object=MibScalar
xgcpHigherBoundForJitter=_XgcpHigherBoundForJitter_Object((1,3,6,1,3,90,1,4,4),_XgcpHigherBoundForJitter_Type())
xgcpHigherBoundForJitter.setMaxAccess(_D)
if mibBuilder.loadTexts:xgcpHigherBoundForJitter.setStatus(_A)
if mibBuilder.loadTexts:xgcpHigherBoundForJitter.setUnits(_F)
class _XgcpLowerBoundForLatency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(125,200))
_XgcpLowerBoundForLatency_Type.__name__=_C
_XgcpLowerBoundForLatency_Object=MibScalar
xgcpLowerBoundForLatency=_XgcpLowerBoundForLatency_Object((1,3,6,1,3,90,1,4,5),_XgcpLowerBoundForLatency_Type())
xgcpLowerBoundForLatency.setMaxAccess(_D)
if mibBuilder.loadTexts:xgcpLowerBoundForLatency.setStatus(_A)
if mibBuilder.loadTexts:xgcpLowerBoundForLatency.setUnits(_F)
class _XgcpHigherBoundForLatency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(250,400))
_XgcpHigherBoundForLatency_Type.__name__=_C
_XgcpHigherBoundForLatency_Object=MibScalar
xgcpHigherBoundForLatency=_XgcpHigherBoundForLatency_Object((1,3,6,1,3,90,1,4,6),_XgcpHigherBoundForLatency_Type())
xgcpHigherBoundForLatency.setMaxAccess(_D)
if mibBuilder.loadTexts:xgcpHigherBoundForLatency.setStatus(_A)
if mibBuilder.loadTexts:xgcpHigherBoundForLatency.setUnits(_F)
_XgcpDefaultMGCObjects_ObjectIdentity=ObjectIdentity
xgcpDefaultMGCObjects=_XgcpDefaultMGCObjects_ObjectIdentity((1,3,6,1,3,90,1,5))
class _XgcpMGCCfgAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_XgcpMGCCfgAddress_Type.__name__=_G
_XgcpMGCCfgAddress_Object=MibScalar
xgcpMGCCfgAddress=_XgcpMGCCfgAddress_Object((1,3,6,1,3,90,1,5,1),_XgcpMGCCfgAddress_Type())
xgcpMGCCfgAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgcpMGCCfgAddress.setStatus(_A)
class _XgcpMGCCfgUDPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_XgcpMGCCfgUDPPort_Type.__name__=_C
_XgcpMGCCfgUDPPort_Object=MibScalar
xgcpMGCCfgUDPPort=_XgcpMGCCfgUDPPort_Object((1,3,6,1,3,90,1,5,2),_XgcpMGCCfgUDPPort_Type())
xgcpMGCCfgUDPPort.setMaxAccess(_D)
if mibBuilder.loadTexts:xgcpMGCCfgUDPPort.setStatus(_A)
class _XgcpMGCCfgConnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('connected',2),('connecting',3),('unknownName',4),('noResponse',5)))
_XgcpMGCCfgConnStatus_Type.__name__=_C
_XgcpMGCCfgConnStatus_Object=MibScalar
xgcpMGCCfgConnStatus=_XgcpMGCCfgConnStatus_Object((1,3,6,1,3,90,1,5,3),_XgcpMGCCfgConnStatus_Type())
xgcpMGCCfgConnStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:xgcpMGCCfgConnStatus.setStatus(_A)
_XgcpMGCCfgTimeStamp_Type=TimeStamp
_XgcpMGCCfgTimeStamp_Object=MibScalar
xgcpMGCCfgTimeStamp=_XgcpMGCCfgTimeStamp_Object((1,3,6,1,3,90,1,5,4),_XgcpMGCCfgTimeStamp_Type())
xgcpMGCCfgTimeStamp.setMaxAccess(_E)
if mibBuilder.loadTexts:xgcpMGCCfgTimeStamp.setStatus(_A)
_XgcpNotificationPrefix_ObjectIdentity=ObjectIdentity
xgcpNotificationPrefix=_XgcpNotificationPrefix_ObjectIdentity((1,3,6,1,3,90,2))
_XgcpNotifications_ObjectIdentity=ObjectIdentity
xgcpNotifications=_XgcpNotifications_ObjectIdentity((1,3,6,1,3,90,2,0))
_XgcpMIBConformance_ObjectIdentity=ObjectIdentity
xgcpMIBConformance=_XgcpMIBConformance_ObjectIdentity((1,3,6,1,3,90,3))
_XgcpMIBCompliances_ObjectIdentity=ObjectIdentity
xgcpMIBCompliances=_XgcpMIBCompliances_ObjectIdentity((1,3,6,1,3,90,3,1))
_XgcpMIBGroups_ObjectIdentity=ObjectIdentity
xgcpMIBGroups=_XgcpMIBGroups_ObjectIdentity((1,3,6,1,3,90,3,2))
xgcpCoreGroup=ObjectGroup((1,3,6,1,3,90,3,2,1))
xgcpCoreGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_H),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:xgcpCoreGroup.setStatus(_A)
xgcpExtensionGroup=ObjectGroup((1,3,6,1,3,90,3,2,2))
xgcpExtensionGroup.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:xgcpExtensionGroup.setStatus(_A)
xgcpPackageGroup=ObjectGroup((1,3,6,1,3,90,3,2,3))
xgcpPackageGroup.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:xgcpPackageGroup.setStatus(_A)
xgcpVoiceQualityGroup=ObjectGroup((1,3,6,1,3,90,3,2,4))
xgcpVoiceQualityGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:xgcpVoiceQualityGroup.setStatus(_A)
xgcpDefaultMGCGroup=ObjectGroup((1,3,6,1,3,90,3,2,5))
xgcpDefaultMGCGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:xgcpDefaultMGCGroup.setStatus(_A)
xgcpUpDownNotification=NotificationType((1,3,6,1,3,90,2,0,1))
xgcpUpDownNotification.setObjects((_B,_H))
if mibBuilder.loadTexts:xgcpUpDownNotification.setStatus(_A)
xgcpMIBCompliance=ModuleCompliance((1,3,6,1,3,90,3,1,1))
xgcpMIBCompliance.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:xgcpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'xgcpMIB':xgcpMIB,'xgcpObjects':xgcpObjects,'xgcpCoreObjects':xgcpCoreObjects,_M:xgcpInBadVersions,_N:xgcpRequestTimeOut,_O:xgcpRequestRetries,_P:xgcpAdminStatus,_H:xgcpOperStatus,_Q:xgcpUnRecognizedPackets,'xgcpMsgStatTable':xgcpMsgStatTable,'xgcpMsgStatEntry':xgcpMsgStatEntry,_J:xgcpIPAddress,_R:xgcpSuccessMessages,_S:xgcpFailMessages,'xgcpExtensionObjects':xgcpExtensionObjects,_T:xgcpRestartInProgressMWD,_U:xgcpRestartDelay,'xgcpPackageObjects':xgcpPackageObjects,'xgcpCapabilityPackageTable':xgcpCapabilityPackageTable,'xgcpCapabilityPackageEntry':xgcpCapabilityPackageEntry,_L:xgcpCapabilityPackageName,_V:xgcpCapabilityPackageEnable,_W:xgcpDefaultPackage,'xgcpVoiceQualityObjects':xgcpVoiceQualityObjects,_X:xgcpLowerBoundForPacketLoss,_Y:xgcpHigherBoundForPacketLoss,_Z:xgcpLowerBoundForJitter,_a:xgcpHigherBoundForJitter,_b:xgcpLowerBoundForLatency,_c:xgcpHigherBoundForLatency,'xgcpDefaultMGCObjects':xgcpDefaultMGCObjects,_d:xgcpMGCCfgAddress,_e:xgcpMGCCfgUDPPort,_f:xgcpMGCCfgConnStatus,_g:xgcpMGCCfgTimeStamp,'xgcpNotificationPrefix':xgcpNotificationPrefix,'xgcpNotifications':xgcpNotifications,'xgcpUpDownNotification':xgcpUpDownNotification,'xgcpMIBConformance':xgcpMIBConformance,'xgcpMIBCompliances':xgcpMIBCompliances,'xgcpMIBCompliance':xgcpMIBCompliance,'xgcpMIBGroups':xgcpMIBGroups,_h:xgcpCoreGroup,_i:xgcpExtensionGroup,_j:xgcpPackageGroup,_k:xgcpVoiceQualityGroup,_l:xgcpDefaultMGCGroup})