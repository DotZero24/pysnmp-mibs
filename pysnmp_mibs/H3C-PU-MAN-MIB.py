_P='h3cPUVersionServerAddr'
_O='h3cPUECVideoChannelID'
_N='h3cPUExternalOutputAlarmChannelID'
_M='DisplayString'
_L='h3cPUCMSAddr'
_K='h3cPUECRegionCoordinateY2'
_J='h3cPUECRegionCoordinateX2'
_I='h3cPUECRegionCoordinateY1'
_H='h3cPUECRegionCoordinateX1'
_G='h3cPUExternalInputAlarmChannelID'
_F='Unsigned32'
_E='h3cPUECVideoChannelName'
_D='accessible-for-notify'
_C='read-only'
_B='H3C-PU-MAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cSurveillanceMIB,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cSurveillanceMIB')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','TextualConvention','TruthValue')
h3cPUMan=ModuleIdentity((1,3,6,1,4,1,2011,10,9,2))
_H3cPUCommonMan_ObjectIdentity=ObjectIdentity
h3cPUCommonMan=_H3cPUCommonMan_ObjectIdentity((1,3,6,1,4,1,2011,10,9,2,1))
_H3cPUCommonManObjects_ObjectIdentity=ObjectIdentity
h3cPUCommonManObjects=_H3cPUCommonManObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,9,2,1,1))
_H3cPUisOnline_Type=TruthValue
_H3cPUisOnline_Object=MibScalar
h3cPUisOnline=_H3cPUisOnline_Object((1,3,6,1,4,1,2011,10,9,2,1,1,1),_H3cPUisOnline_Type())
h3cPUisOnline.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPUisOnline.setStatus(_A)
_H3cPUCMSAddr_Type=IpAddress
_H3cPUCMSAddr_Object=MibScalar
h3cPUCMSAddr=_H3cPUCMSAddr_Object((1,3,6,1,4,1,2011,10,9,2,1,1,2),_H3cPUCMSAddr_Type())
h3cPUCMSAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPUCMSAddr.setStatus(_A)
_H3cPUVersionServerAddr_Type=IpAddress
_H3cPUVersionServerAddr_Object=MibScalar
h3cPUVersionServerAddr=_H3cPUVersionServerAddr_Object((1,3,6,1,4,1,2011,10,9,2,1,1,3),_H3cPUVersionServerAddr_Type())
h3cPUVersionServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPUVersionServerAddr.setStatus(_A)
_H3cPUCommonManTables_ObjectIdentity=ObjectIdentity
h3cPUCommonManTables=_H3cPUCommonManTables_ObjectIdentity((1,3,6,1,4,1,2011,10,9,2,1,2))
_H3cPUExternalInputAlarmTable_Object=MibTable
h3cPUExternalInputAlarmTable=_H3cPUExternalInputAlarmTable_Object((1,3,6,1,4,1,2011,10,9,2,1,2,1))
if mibBuilder.loadTexts:h3cPUExternalInputAlarmTable.setStatus(_A)
_H3cPUExternalInputAlarmEntry_Object=MibTableRow
h3cPUExternalInputAlarmEntry=_H3cPUExternalInputAlarmEntry_Object((1,3,6,1,4,1,2011,10,9,2,1,2,1,1))
h3cPUExternalInputAlarmEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3cPUExternalInputAlarmEntry.setStatus(_A)
_H3cPUExternalInputAlarmChannelID_Type=Unsigned32
_H3cPUExternalInputAlarmChannelID_Object=MibTableColumn
h3cPUExternalInputAlarmChannelID=_H3cPUExternalInputAlarmChannelID_Object((1,3,6,1,4,1,2011,10,9,2,1,2,1,1,1),_H3cPUExternalInputAlarmChannelID_Type())
h3cPUExternalInputAlarmChannelID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPUExternalInputAlarmChannelID.setStatus(_A)
_H3cPUExternalInputAlarmStatus_Type=TruthValue
_H3cPUExternalInputAlarmStatus_Object=MibTableColumn
h3cPUExternalInputAlarmStatus=_H3cPUExternalInputAlarmStatus_Object((1,3,6,1,4,1,2011,10,9,2,1,2,1,1,2),_H3cPUExternalInputAlarmStatus_Type())
h3cPUExternalInputAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPUExternalInputAlarmStatus.setStatus(_A)
_H3cPUExternalOutputAlarmTable_Object=MibTable
h3cPUExternalOutputAlarmTable=_H3cPUExternalOutputAlarmTable_Object((1,3,6,1,4,1,2011,10,9,2,1,2,2))
if mibBuilder.loadTexts:h3cPUExternalOutputAlarmTable.setStatus(_A)
_H3cPUExternalOutputAlarmEntry_Object=MibTableRow
h3cPUExternalOutputAlarmEntry=_H3cPUExternalOutputAlarmEntry_Object((1,3,6,1,4,1,2011,10,9,2,1,2,2,1))
h3cPUExternalOutputAlarmEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:h3cPUExternalOutputAlarmEntry.setStatus(_A)
_H3cPUExternalOutputAlarmChannelID_Type=Unsigned32
_H3cPUExternalOutputAlarmChannelID_Object=MibTableColumn
h3cPUExternalOutputAlarmChannelID=_H3cPUExternalOutputAlarmChannelID_Object((1,3,6,1,4,1,2011,10,9,2,1,2,2,1,1),_H3cPUExternalOutputAlarmChannelID_Type())
h3cPUExternalOutputAlarmChannelID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPUExternalOutputAlarmChannelID.setStatus(_A)
_H3cPUExternalOutputAlarmStatus_Type=TruthValue
_H3cPUExternalOutputAlarmStatus_Object=MibTableColumn
h3cPUExternalOutputAlarmStatus=_H3cPUExternalOutputAlarmStatus_Object((1,3,6,1,4,1,2011,10,9,2,1,2,2,1,2),_H3cPUExternalOutputAlarmStatus_Type())
h3cPUExternalOutputAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPUExternalOutputAlarmStatus.setStatus(_A)
_H3cPUECMan_ObjectIdentity=ObjectIdentity
h3cPUECMan=_H3cPUECMan_ObjectIdentity((1,3,6,1,4,1,2011,10,9,2,2))
_H3cPUECManObjects_ObjectIdentity=ObjectIdentity
h3cPUECManObjects=_H3cPUECManObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,9,2,2,1))
class _H3cPUECCameraOnlines_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cPUECCameraOnlines_Type.__name__=_F
_H3cPUECCameraOnlines_Object=MibScalar
h3cPUECCameraOnlines=_H3cPUECCameraOnlines_Object((1,3,6,1,4,1,2011,10,9,2,2,1,1),_H3cPUECCameraOnlines_Type())
h3cPUECCameraOnlines.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPUECCameraOnlines.setStatus(_A)
class _H3cPUECCameraAvailRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cPUECCameraAvailRate_Type.__name__=_F
_H3cPUECCameraAvailRate_Object=MibScalar
h3cPUECCameraAvailRate=_H3cPUECCameraAvailRate_Object((1,3,6,1,4,1,2011,10,9,2,2,1,2),_H3cPUECCameraAvailRate_Type())
h3cPUECCameraAvailRate.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPUECCameraAvailRate.setStatus(_A)
_H3cPUECManTables_ObjectIdentity=ObjectIdentity
h3cPUECManTables=_H3cPUECManTables_ObjectIdentity((1,3,6,1,4,1,2011,10,9,2,2,2))
_H3cPUECVideoChannelTable_Object=MibTable
h3cPUECVideoChannelTable=_H3cPUECVideoChannelTable_Object((1,3,6,1,4,1,2011,10,9,2,2,2,1))
if mibBuilder.loadTexts:h3cPUECVideoChannelTable.setStatus(_A)
_H3cPUECVideoChannelEntry_Object=MibTableRow
h3cPUECVideoChannelEntry=_H3cPUECVideoChannelEntry_Object((1,3,6,1,4,1,2011,10,9,2,2,2,1,1))
h3cPUECVideoChannelEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:h3cPUECVideoChannelEntry.setStatus(_A)
_H3cPUECVideoChannelID_Type=Unsigned32
_H3cPUECVideoChannelID_Object=MibTableColumn
h3cPUECVideoChannelID=_H3cPUECVideoChannelID_Object((1,3,6,1,4,1,2011,10,9,2,2,2,1,1,1),_H3cPUECVideoChannelID_Type())
h3cPUECVideoChannelID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPUECVideoChannelID.setStatus(_A)
class _H3cPUECVideoChannelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cPUECVideoChannelName_Type.__name__=_M
_H3cPUECVideoChannelName_Object=MibTableColumn
h3cPUECVideoChannelName=_H3cPUECVideoChannelName_Object((1,3,6,1,4,1,2011,10,9,2,2,2,1,1,2),_H3cPUECVideoChannelName_Type())
h3cPUECVideoChannelName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPUECVideoChannelName.setStatus(_A)
class _H3cPUECVideoChannelServiceStatus_Type(Bits):namedValues=NamedValues(*(('unknown',0),('unused',1),('kinescope',2),('snapshot',3)))
_H3cPUECVideoChannelServiceStatus_Type.__name__='Bits'
_H3cPUECVideoChannelServiceStatus_Object=MibTableColumn
h3cPUECVideoChannelServiceStatus=_H3cPUECVideoChannelServiceStatus_Object((1,3,6,1,4,1,2011,10,9,2,2,2,1,1,3),_H3cPUECVideoChannelServiceStatus_Type())
h3cPUECVideoChannelServiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPUECVideoChannelServiceStatus.setStatus(_A)
_H3cPUECManMIBTrap_ObjectIdentity=ObjectIdentity
h3cPUECManMIBTrap=_H3cPUECManMIBTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,9,2,2,3))
_H3cPUECManTrapPrex_ObjectIdentity=ObjectIdentity
h3cPUECManTrapPrex=_H3cPUECManTrapPrex_ObjectIdentity((1,3,6,1,4,1,2011,10,9,2,2,3,0))
_H3cPUECManTrapObjects_ObjectIdentity=ObjectIdentity
h3cPUECManTrapObjects=_H3cPUECManTrapObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,9,2,2,3,1))
_H3cPUECRegionCoordinateX1_Type=Unsigned32
_H3cPUECRegionCoordinateX1_Object=MibScalar
h3cPUECRegionCoordinateX1=_H3cPUECRegionCoordinateX1_Object((1,3,6,1,4,1,2011,10,9,2,2,3,1,1),_H3cPUECRegionCoordinateX1_Type())
h3cPUECRegionCoordinateX1.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPUECRegionCoordinateX1.setStatus(_A)
_H3cPUECRegionCoordinateY1_Type=Unsigned32
_H3cPUECRegionCoordinateY1_Object=MibScalar
h3cPUECRegionCoordinateY1=_H3cPUECRegionCoordinateY1_Object((1,3,6,1,4,1,2011,10,9,2,2,3,1,2),_H3cPUECRegionCoordinateY1_Type())
h3cPUECRegionCoordinateY1.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPUECRegionCoordinateY1.setStatus(_A)
_H3cPUECRegionCoordinateX2_Type=Unsigned32
_H3cPUECRegionCoordinateX2_Object=MibScalar
h3cPUECRegionCoordinateX2=_H3cPUECRegionCoordinateX2_Object((1,3,6,1,4,1,2011,10,9,2,2,3,1,3),_H3cPUECRegionCoordinateX2_Type())
h3cPUECRegionCoordinateX2.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPUECRegionCoordinateX2.setStatus(_A)
_H3cPUECRegionCoordinateY2_Type=Unsigned32
_H3cPUECRegionCoordinateY2_Object=MibScalar
h3cPUECRegionCoordinateY2=_H3cPUECRegionCoordinateY2_Object((1,3,6,1,4,1,2011,10,9,2,2,3,1,4),_H3cPUECRegionCoordinateY2_Type())
h3cPUECRegionCoordinateY2.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPUECRegionCoordinateY2.setStatus(_A)
_H3cPUDCMan_ObjectIdentity=ObjectIdentity
h3cPUDCMan=_H3cPUDCMan_ObjectIdentity((1,3,6,1,4,1,2011,10,9,2,3))
_H3cPUDCManObjects_ObjectIdentity=ObjectIdentity
h3cPUDCManObjects=_H3cPUDCManObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,9,2,3,1))
_H3cPUDCRcvVideoPackets_Type=Counter32
_H3cPUDCRcvVideoPackets_Object=MibScalar
h3cPUDCRcvVideoPackets=_H3cPUDCRcvVideoPackets_Object((1,3,6,1,4,1,2011,10,9,2,3,1,1),_H3cPUDCRcvVideoPackets_Type())
h3cPUDCRcvVideoPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPUDCRcvVideoPackets.setStatus(_A)
_H3cPUDCRcvVideoRefFrames_Type=Counter32
_H3cPUDCRcvVideoRefFrames_Object=MibScalar
h3cPUDCRcvVideoRefFrames=_H3cPUDCRcvVideoRefFrames_Object((1,3,6,1,4,1,2011,10,9,2,3,1,2),_H3cPUDCRcvVideoRefFrames_Type())
h3cPUDCRcvVideoRefFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPUDCRcvVideoRefFrames.setStatus(_A)
_H3cPUDCVideoPacketsLoss_Type=Counter32
_H3cPUDCVideoPacketsLoss_Object=MibScalar
h3cPUDCVideoPacketsLoss=_H3cPUDCVideoPacketsLoss_Object((1,3,6,1,4,1,2011,10,9,2,3,1,3),_H3cPUDCVideoPacketsLoss_Type())
h3cPUDCVideoPacketsLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPUDCVideoPacketsLoss.setStatus(_A)
_H3cPUDCVideoRefFramesLoss_Type=Counter32
_H3cPUDCVideoRefFramesLoss_Object=MibScalar
h3cPUDCVideoRefFramesLoss=_H3cPUDCVideoRefFramesLoss_Object((1,3,6,1,4,1,2011,10,9,2,3,1,4),_H3cPUDCVideoRefFramesLoss_Type())
h3cPUDCVideoRefFramesLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPUDCVideoRefFramesLoss.setStatus(_A)
h3cPUECManExternalSemaphoreTrap=NotificationType((1,3,6,1,4,1,2011,10,9,2,2,3,0,1))
h3cPUECManExternalSemaphoreTrap.setObjects((_B,_G))
if mibBuilder.loadTexts:h3cPUECManExternalSemaphoreTrap.setStatus(_A)
h3cPUECManVideoLossTrap=NotificationType((1,3,6,1,4,1,2011,10,9,2,2,3,0,2))
h3cPUECManVideoLossTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:h3cPUECManVideoLossTrap.setStatus(_A)
h3cPUECManVideoRecoverTrap=NotificationType((1,3,6,1,4,1,2011,10,9,2,2,3,0,3))
h3cPUECManVideoRecoverTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:h3cPUECManVideoRecoverTrap.setStatus(_A)
h3cPUECManMotionDetectTrap=NotificationType((1,3,6,1,4,1,2011,10,9,2,2,3,0,4))
h3cPUECManMotionDetectTrap.setObjects(*((_B,_E),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:h3cPUECManMotionDetectTrap.setStatus(_A)
h3cPUECManOnLineFailureTrap=NotificationType((1,3,6,1,4,1,2011,10,9,2,2,3,0,5))
h3cPUECManOnLineFailureTrap.setObjects((_B,_L))
if mibBuilder.loadTexts:h3cPUECManOnLineFailureTrap.setStatus(_A)
h3cPUECManConnectionCMSFailureTrap=NotificationType((1,3,6,1,4,1,2011,10,9,2,2,3,0,6))
h3cPUECManConnectionCMSFailureTrap.setObjects((_B,_L))
if mibBuilder.loadTexts:h3cPUECManConnectionCMSFailureTrap.setStatus(_A)
h3cPUECManConnectionVerSrvFailureTrap=NotificationType((1,3,6,1,4,1,2011,10,9,2,2,3,0,7))
h3cPUECManConnectionVerSrvFailureTrap.setObjects((_B,_P))
if mibBuilder.loadTexts:h3cPUECManConnectionVerSrvFailureTrap.setStatus(_A)
h3cPUECManFlashFailureTrap=NotificationType((1,3,6,1,4,1,2011,10,9,2,2,3,0,8))
if mibBuilder.loadTexts:h3cPUECManFlashFailureTrap.setStatus(_A)
h3cPUECManCameraShelterTrap=NotificationType((1,3,6,1,4,1,2011,10,9,2,2,3,0,9))
h3cPUECManCameraShelterTrap.setObjects(*((_B,_E),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:h3cPUECManCameraShelterTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cPUMan':h3cPUMan,'h3cPUCommonMan':h3cPUCommonMan,'h3cPUCommonManObjects':h3cPUCommonManObjects,'h3cPUisOnline':h3cPUisOnline,_L:h3cPUCMSAddr,_P:h3cPUVersionServerAddr,'h3cPUCommonManTables':h3cPUCommonManTables,'h3cPUExternalInputAlarmTable':h3cPUExternalInputAlarmTable,'h3cPUExternalInputAlarmEntry':h3cPUExternalInputAlarmEntry,_G:h3cPUExternalInputAlarmChannelID,'h3cPUExternalInputAlarmStatus':h3cPUExternalInputAlarmStatus,'h3cPUExternalOutputAlarmTable':h3cPUExternalOutputAlarmTable,'h3cPUExternalOutputAlarmEntry':h3cPUExternalOutputAlarmEntry,_N:h3cPUExternalOutputAlarmChannelID,'h3cPUExternalOutputAlarmStatus':h3cPUExternalOutputAlarmStatus,'h3cPUECMan':h3cPUECMan,'h3cPUECManObjects':h3cPUECManObjects,'h3cPUECCameraOnlines':h3cPUECCameraOnlines,'h3cPUECCameraAvailRate':h3cPUECCameraAvailRate,'h3cPUECManTables':h3cPUECManTables,'h3cPUECVideoChannelTable':h3cPUECVideoChannelTable,'h3cPUECVideoChannelEntry':h3cPUECVideoChannelEntry,_O:h3cPUECVideoChannelID,_E:h3cPUECVideoChannelName,'h3cPUECVideoChannelServiceStatus':h3cPUECVideoChannelServiceStatus,'h3cPUECManMIBTrap':h3cPUECManMIBTrap,'h3cPUECManTrapPrex':h3cPUECManTrapPrex,'h3cPUECManExternalSemaphoreTrap':h3cPUECManExternalSemaphoreTrap,'h3cPUECManVideoLossTrap':h3cPUECManVideoLossTrap,'h3cPUECManVideoRecoverTrap':h3cPUECManVideoRecoverTrap,'h3cPUECManMotionDetectTrap':h3cPUECManMotionDetectTrap,'h3cPUECManOnLineFailureTrap':h3cPUECManOnLineFailureTrap,'h3cPUECManConnectionCMSFailureTrap':h3cPUECManConnectionCMSFailureTrap,'h3cPUECManConnectionVerSrvFailureTrap':h3cPUECManConnectionVerSrvFailureTrap,'h3cPUECManFlashFailureTrap':h3cPUECManFlashFailureTrap,'h3cPUECManCameraShelterTrap':h3cPUECManCameraShelterTrap,'h3cPUECManTrapObjects':h3cPUECManTrapObjects,_H:h3cPUECRegionCoordinateX1,_I:h3cPUECRegionCoordinateY1,_J:h3cPUECRegionCoordinateX2,_K:h3cPUECRegionCoordinateY2,'h3cPUDCMan':h3cPUDCMan,'h3cPUDCManObjects':h3cPUDCManObjects,'h3cPUDCRcvVideoPackets':h3cPUDCRcvVideoPackets,'h3cPUDCRcvVideoRefFrames':h3cPUDCRcvVideoRefFrames,'h3cPUDCVideoPacketsLoss':h3cPUDCVideoPacketsLoss,'h3cPUDCVideoRefFramesLoss':h3cPUDCVideoRefFramesLoss})