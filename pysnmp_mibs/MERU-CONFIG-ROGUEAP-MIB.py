_J='mwRogueDetectionApTableIndex'
_I='mwRogueApListTableIndex'
_H='mwRogueapBlockTableIndex'
_G='mwRogueapAclTableIndex'
_F='Integer32'
_E='not-accessible'
_D='MERU-CONFIG-ROGUEAP-MIB'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwConfiguration,=mibBuilder.importSymbols('MERU-SMI','mwConfiguration')
MwlApType,MwlArrayDataTypeAction,MwlBlock,MwlOnOffSwitch,MwlSpectrumBandsBits=mibBuilder.importSymbols('MERU-TC','MwlApType','MwlArrayDataTypeAction','MwlBlock','MwlOnOffSwitch','MwlSpectrumBandsBits')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwConfigRogueAp=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,7))
_MwRogueapVars_ObjectIdentity=ObjectIdentity
mwRogueapVars=_MwRogueapVars_ObjectIdentity((1,3,6,1,4,1,15983,1,1,4,7,1))
_MwRogueapVarsDetection_Type=MwlOnOffSwitch
_MwRogueapVarsDetection_Object=MibScalar
mwRogueapVarsDetection=_MwRogueapVarsDetection_Object((1,3,6,1,4,1,15983,1,1,4,7,1,1),_MwRogueapVarsDetection_Type())
mwRogueapVarsDetection.setMaxAccess(_C)
if mibBuilder.loadTexts:mwRogueapVarsDetection.setStatus(_A)
_MwRogueapVarsBlock_Type=MwlBlock
_MwRogueapVarsBlock_Object=MibScalar
mwRogueapVarsBlock=_MwRogueapVarsBlock_Object((1,3,6,1,4,1,15983,1,1,4,7,1,2),_MwRogueapVarsBlock_Type())
mwRogueapVarsBlock.setMaxAccess(_C)
if mibBuilder.loadTexts:mwRogueapVarsBlock.setStatus(_A)
_MwRogueapVarsAging_Type=Unsigned32
_MwRogueapVarsAging_Object=MibScalar
mwRogueapVarsAging=_MwRogueapVarsAging_Object((1,3,6,1,4,1,15983,1,1,4,7,1,3),_MwRogueapVarsAging_Type())
mwRogueapVarsAging.setMaxAccess(_C)
if mibBuilder.loadTexts:mwRogueapVarsAging.setStatus(_A)
_MwRogueapVarsMitigateAps_Type=Unsigned32
_MwRogueapVarsMitigateAps_Object=MibScalar
mwRogueapVarsMitigateAps=_MwRogueapVarsMitigateAps_Object((1,3,6,1,4,1,15983,1,1,4,7,1,4),_MwRogueapVarsMitigateAps_Type())
mwRogueapVarsMitigateAps.setMaxAccess(_C)
if mibBuilder.loadTexts:mwRogueapVarsMitigateAps.setStatus(_A)
_MwRogueapVarsScanningTime_Type=Unsigned32
_MwRogueapVarsScanningTime_Object=MibScalar
mwRogueapVarsScanningTime=_MwRogueapVarsScanningTime_Object((1,3,6,1,4,1,15983,1,1,4,7,1,5),_MwRogueapVarsScanningTime_Type())
mwRogueapVarsScanningTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mwRogueapVarsScanningTime.setStatus(_A)
_MwRogueapVarsOperationalTime_Type=Unsigned32
_MwRogueapVarsOperationalTime_Object=MibScalar
mwRogueapVarsOperationalTime=_MwRogueapVarsOperationalTime_Object((1,3,6,1,4,1,15983,1,1,4,7,1,6),_MwRogueapVarsOperationalTime_Type())
mwRogueapVarsOperationalTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mwRogueapVarsOperationalTime.setStatus(_A)
_MwRogueapVarsMitigationFrames_Type=Unsigned32
_MwRogueapVarsMitigationFrames_Object=MibScalar
mwRogueapVarsMitigationFrames=_MwRogueapVarsMitigationFrames_Object((1,3,6,1,4,1,15983,1,1,4,7,1,7),_MwRogueapVarsMitigationFrames_Type())
mwRogueapVarsMitigationFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:mwRogueapVarsMitigationFrames.setStatus(_A)
_MwRogueapVarsScanChannelMask_Type=DisplayString
_MwRogueapVarsScanChannelMask_Object=MibScalar
mwRogueapVarsScanChannelMask=_MwRogueapVarsScanChannelMask_Object((1,3,6,1,4,1,15983,1,1,4,7,1,8),_MwRogueapVarsScanChannelMask_Type())
mwRogueapVarsScanChannelMask.setMaxAccess(_C)
if mibBuilder.loadTexts:mwRogueapVarsScanChannelMask.setStatus(_A)
class _MwRogueapVarsMinRSSI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,0))
_MwRogueapVarsMinRSSI_Type.__name__=_F
_MwRogueapVarsMinRSSI_Object=MibScalar
mwRogueapVarsMinRSSI=_MwRogueapVarsMinRSSI_Object((1,3,6,1,4,1,15983,1,1,4,7,1,9),_MwRogueapVarsMinRSSI_Type())
mwRogueapVarsMinRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:mwRogueapVarsMinRSSI.setStatus(_A)
_MwRogueapVarsSpectrumBands_Type=MwlSpectrumBandsBits
_MwRogueapVarsSpectrumBands_Object=MibScalar
mwRogueapVarsSpectrumBands=_MwRogueapVarsSpectrumBands_Object((1,3,6,1,4,1,15983,1,1,4,7,1,10),_MwRogueapVarsSpectrumBands_Type())
mwRogueapVarsSpectrumBands.setMaxAccess(_C)
if mibBuilder.loadTexts:mwRogueapVarsSpectrumBands.setStatus(_A)
_MwRogueapAclTable_Object=MibTable
mwRogueapAclTable=_MwRogueapAclTable_Object((1,3,6,1,4,1,15983,1,1,4,7,2))
if mibBuilder.loadTexts:mwRogueapAclTable.setStatus(_A)
_MwRogueapAclEntry_Object=MibTableRow
mwRogueapAclEntry=_MwRogueapAclEntry_Object((1,3,6,1,4,1,15983,1,1,4,7,2,1))
mwRogueapAclEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:mwRogueapAclEntry.setStatus(_A)
_MwRogueapAclTableIndex_Type=Integer32
_MwRogueapAclTableIndex_Object=MibTableColumn
mwRogueapAclTableIndex=_MwRogueapAclTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,7,2,1,1),_MwRogueapAclTableIndex_Type())
mwRogueapAclTableIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mwRogueapAclTableIndex.setStatus(_A)
_MwRogueapAclBssId_Type=MacAddress
_MwRogueapAclBssId_Object=MibTableColumn
mwRogueapAclBssId=_MwRogueapAclBssId_Object((1,3,6,1,4,1,15983,1,1,4,7,2,1,2),_MwRogueapAclBssId_Type())
mwRogueapAclBssId.setMaxAccess(_C)
if mibBuilder.loadTexts:mwRogueapAclBssId.setStatus(_A)
_MwRogueapAclRowStatus_Type=RowStatus
_MwRogueapAclRowStatus_Object=MibTableColumn
mwRogueapAclRowStatus=_MwRogueapAclRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,7,2,1,3),_MwRogueapAclRowStatus_Type())
mwRogueapAclRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mwRogueapAclRowStatus.setStatus(_A)
_MwRogueapBlockTable_Object=MibTable
mwRogueapBlockTable=_MwRogueapBlockTable_Object((1,3,6,1,4,1,15983,1,1,4,7,3))
if mibBuilder.loadTexts:mwRogueapBlockTable.setStatus(_A)
_MwRogueapBlockEntry_Object=MibTableRow
mwRogueapBlockEntry=_MwRogueapBlockEntry_Object((1,3,6,1,4,1,15983,1,1,4,7,3,1))
mwRogueapBlockEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:mwRogueapBlockEntry.setStatus(_A)
_MwRogueapBlockTableIndex_Type=Integer32
_MwRogueapBlockTableIndex_Object=MibTableColumn
mwRogueapBlockTableIndex=_MwRogueapBlockTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,7,3,1,1),_MwRogueapBlockTableIndex_Type())
mwRogueapBlockTableIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mwRogueapBlockTableIndex.setStatus(_A)
_MwRogueapBlockBssId_Type=MacAddress
_MwRogueapBlockBssId_Object=MibTableColumn
mwRogueapBlockBssId=_MwRogueapBlockBssId_Object((1,3,6,1,4,1,15983,1,1,4,7,3,1,2),_MwRogueapBlockBssId_Type())
mwRogueapBlockBssId.setMaxAccess(_C)
if mibBuilder.loadTexts:mwRogueapBlockBssId.setStatus(_A)
_MwRogueapBlockCreationDate_Type=DateAndTime
_MwRogueapBlockCreationDate_Object=MibTableColumn
mwRogueapBlockCreationDate=_MwRogueapBlockCreationDate_Object((1,3,6,1,4,1,15983,1,1,4,7,3,1,3),_MwRogueapBlockCreationDate_Type())
mwRogueapBlockCreationDate.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueapBlockCreationDate.setStatus(_A)
_MwRogueapBlockLastReported_Type=DateAndTime
_MwRogueapBlockLastReported_Object=MibTableColumn
mwRogueapBlockLastReported=_MwRogueapBlockLastReported_Object((1,3,6,1,4,1,15983,1,1,4,7,3,1,4),_MwRogueapBlockLastReported_Type())
mwRogueapBlockLastReported.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueapBlockLastReported.setStatus(_A)
_MwRogueapBlockRowStatus_Type=RowStatus
_MwRogueapBlockRowStatus_Object=MibTableColumn
mwRogueapBlockRowStatus=_MwRogueapBlockRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,7,3,1,5),_MwRogueapBlockRowStatus_Type())
mwRogueapBlockRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mwRogueapBlockRowStatus.setStatus(_A)
_MwRogueApListTable_Object=MibTable
mwRogueApListTable=_MwRogueApListTable_Object((1,3,6,1,4,1,15983,1,1,4,7,4))
if mibBuilder.loadTexts:mwRogueApListTable.setStatus(_A)
_MwRogueApListEntry_Object=MibTableRow
mwRogueApListEntry=_MwRogueApListEntry_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1))
mwRogueApListEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:mwRogueApListEntry.setStatus(_A)
_MwRogueApListTableIndex_Type=Integer32
_MwRogueApListTableIndex_Object=MibTableColumn
mwRogueApListTableIndex=_MwRogueApListTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1,1),_MwRogueApListTableIndex_Type())
mwRogueApListTableIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mwRogueApListTableIndex.setStatus(_A)
_MwRogueApListMac_Type=MacAddress
_MwRogueApListMac_Object=MibTableColumn
mwRogueApListMac=_MwRogueApListMac_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1,2),_MwRogueApListMac_Type())
mwRogueApListMac.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueApListMac.setStatus(_A)
_MwRogueApListEssid_Type=DisplayString
_MwRogueApListEssid_Object=MibTableColumn
mwRogueApListEssid=_MwRogueApListEssid_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1,3),_MwRogueApListEssid_Type())
mwRogueApListEssid.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueApListEssid.setStatus(_A)
_MwRogueApListBssid_Type=MacAddress
_MwRogueApListBssid_Object=MibTableColumn
mwRogueApListBssid=_MwRogueApListBssid_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1,4),_MwRogueApListBssid_Type())
mwRogueApListBssid.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueApListBssid.setStatus(_A)
_MwRogueApListChannel_Type=Unsigned32
_MwRogueApListChannel_Object=MibTableColumn
mwRogueApListChannel=_MwRogueApListChannel_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1,5),_MwRogueApListChannel_Type())
mwRogueApListChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueApListChannel.setStatus(_A)
_MwRogueApListMeruAp1Id_Type=Integer32
_MwRogueApListMeruAp1Id_Object=MibTableColumn
mwRogueApListMeruAp1Id=_MwRogueApListMeruAp1Id_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1,6),_MwRogueApListMeruAp1Id_Type())
mwRogueApListMeruAp1Id.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueApListMeruAp1Id.setStatus(_A)
_MwRogueApListMeruAp2Id_Type=Integer32
_MwRogueApListMeruAp2Id_Object=MibTableColumn
mwRogueApListMeruAp2Id=_MwRogueApListMeruAp2Id_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1,7),_MwRogueApListMeruAp2Id_Type())
mwRogueApListMeruAp2Id.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueApListMeruAp2Id.setStatus(_A)
_MwRogueApListMeruAp3Id_Type=Integer32
_MwRogueApListMeruAp3Id_Object=MibTableColumn
mwRogueApListMeruAp3Id=_MwRogueApListMeruAp3Id_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1,8),_MwRogueApListMeruAp3Id_Type())
mwRogueApListMeruAp3Id.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueApListMeruAp3Id.setStatus(_A)
_MwRogueApListDeviceType_Type=MwlApType
_MwRogueApListDeviceType_Object=MibTableColumn
mwRogueApListDeviceType=_MwRogueApListDeviceType_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1,9),_MwRogueApListDeviceType_Type())
mwRogueApListDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueApListDeviceType.setStatus(_A)
_MwRogueApListMeruAp1Rssi_Type=Integer32
_MwRogueApListMeruAp1Rssi_Object=MibTableColumn
mwRogueApListMeruAp1Rssi=_MwRogueApListMeruAp1Rssi_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1,11),_MwRogueApListMeruAp1Rssi_Type())
mwRogueApListMeruAp1Rssi.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueApListMeruAp1Rssi.setStatus(_A)
_MwRogueApListMeruAp2Rssi_Type=Integer32
_MwRogueApListMeruAp2Rssi_Object=MibTableColumn
mwRogueApListMeruAp2Rssi=_MwRogueApListMeruAp2Rssi_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1,12),_MwRogueApListMeruAp2Rssi_Type())
mwRogueApListMeruAp2Rssi.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueApListMeruAp2Rssi.setStatus(_A)
_MwRogueApListMeruAp3Rssi_Type=Integer32
_MwRogueApListMeruAp3Rssi_Object=MibTableColumn
mwRogueApListMeruAp3Rssi=_MwRogueApListMeruAp3Rssi_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1,13),_MwRogueApListMeruAp3Rssi_Type())
mwRogueApListMeruAp3Rssi.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueApListMeruAp3Rssi.setStatus(_A)
_MwRogueApListNonReportedAudits_Type=Unsigned32
_MwRogueApListNonReportedAudits_Object=MibTableColumn
mwRogueApListNonReportedAudits=_MwRogueApListNonReportedAudits_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1,14),_MwRogueApListNonReportedAudits_Type())
mwRogueApListNonReportedAudits.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueApListNonReportedAudits.setStatus(_A)
_MwRogueApListMeruAp1LastActivity_Type=TimeTicks
_MwRogueApListMeruAp1LastActivity_Object=MibTableColumn
mwRogueApListMeruAp1LastActivity=_MwRogueApListMeruAp1LastActivity_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1,15),_MwRogueApListMeruAp1LastActivity_Type())
mwRogueApListMeruAp1LastActivity.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueApListMeruAp1LastActivity.setStatus(_A)
_MwRogueApListMeruAp2LastActivity_Type=TimeTicks
_MwRogueApListMeruAp2LastActivity_Object=MibTableColumn
mwRogueApListMeruAp2LastActivity=_MwRogueApListMeruAp2LastActivity_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1,16),_MwRogueApListMeruAp2LastActivity_Type())
mwRogueApListMeruAp2LastActivity.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueApListMeruAp2LastActivity.setStatus(_A)
_MwRogueApListMeruAp3LastActivity_Type=TimeTicks
_MwRogueApListMeruAp3LastActivity_Object=MibTableColumn
mwRogueApListMeruAp3LastActivity=_MwRogueApListMeruAp3LastActivity_Object((1,3,6,1,4,1,15983,1,1,4,7,4,1,17),_MwRogueApListMeruAp3LastActivity_Type())
mwRogueApListMeruAp3LastActivity.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRogueApListMeruAp3LastActivity.setStatus(_A)
_MwRogueDetectionApTable_Object=MibTable
mwRogueDetectionApTable=_MwRogueDetectionApTable_Object((1,3,6,1,4,1,15983,1,1,4,7,5))
if mibBuilder.loadTexts:mwRogueDetectionApTable.setStatus(_A)
_MwRogueDetectionApEntry_Object=MibTableRow
mwRogueDetectionApEntry=_MwRogueDetectionApEntry_Object((1,3,6,1,4,1,15983,1,1,4,7,5,1))
mwRogueDetectionApEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:mwRogueDetectionApEntry.setStatus(_A)
_MwRogueDetectionApTableIndex_Type=Integer32
_MwRogueDetectionApTableIndex_Object=MibTableColumn
mwRogueDetectionApTableIndex=_MwRogueDetectionApTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,7,5,1,1),_MwRogueDetectionApTableIndex_Type())
mwRogueDetectionApTableIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mwRogueDetectionApTableIndex.setStatus(_A)
_MwRogueDetectionApNmsApNodeId_Type=Integer32
_MwRogueDetectionApNmsApNodeId_Object=MibTableColumn
mwRogueDetectionApNmsApNodeId=_MwRogueDetectionApNmsApNodeId_Object((1,3,6,1,4,1,15983,1,1,4,7,5,1,2),_MwRogueDetectionApNmsApNodeId_Type())
mwRogueDetectionApNmsApNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:mwRogueDetectionApNmsApNodeId.setStatus(_A)
_MwRogueDetectionApRowStatus_Type=RowStatus
_MwRogueDetectionApRowStatus_Object=MibTableColumn
mwRogueDetectionApRowStatus=_MwRogueDetectionApRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,7,5,1,3),_MwRogueDetectionApRowStatus_Type())
mwRogueDetectionApRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mwRogueDetectionApRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'mwConfigRogueAp':mwConfigRogueAp,'mwRogueapVars':mwRogueapVars,'mwRogueapVarsDetection':mwRogueapVarsDetection,'mwRogueapVarsBlock':mwRogueapVarsBlock,'mwRogueapVarsAging':mwRogueapVarsAging,'mwRogueapVarsMitigateAps':mwRogueapVarsMitigateAps,'mwRogueapVarsScanningTime':mwRogueapVarsScanningTime,'mwRogueapVarsOperationalTime':mwRogueapVarsOperationalTime,'mwRogueapVarsMitigationFrames':mwRogueapVarsMitigationFrames,'mwRogueapVarsScanChannelMask':mwRogueapVarsScanChannelMask,'mwRogueapVarsMinRSSI':mwRogueapVarsMinRSSI,'mwRogueapVarsSpectrumBands':mwRogueapVarsSpectrumBands,'mwRogueapAclTable':mwRogueapAclTable,'mwRogueapAclEntry':mwRogueapAclEntry,_G:mwRogueapAclTableIndex,'mwRogueapAclBssId':mwRogueapAclBssId,'mwRogueapAclRowStatus':mwRogueapAclRowStatus,'mwRogueapBlockTable':mwRogueapBlockTable,'mwRogueapBlockEntry':mwRogueapBlockEntry,_H:mwRogueapBlockTableIndex,'mwRogueapBlockBssId':mwRogueapBlockBssId,'mwRogueapBlockCreationDate':mwRogueapBlockCreationDate,'mwRogueapBlockLastReported':mwRogueapBlockLastReported,'mwRogueapBlockRowStatus':mwRogueapBlockRowStatus,'mwRogueApListTable':mwRogueApListTable,'mwRogueApListEntry':mwRogueApListEntry,_I:mwRogueApListTableIndex,'mwRogueApListMac':mwRogueApListMac,'mwRogueApListEssid':mwRogueApListEssid,'mwRogueApListBssid':mwRogueApListBssid,'mwRogueApListChannel':mwRogueApListChannel,'mwRogueApListMeruAp1Id':mwRogueApListMeruAp1Id,'mwRogueApListMeruAp2Id':mwRogueApListMeruAp2Id,'mwRogueApListMeruAp3Id':mwRogueApListMeruAp3Id,'mwRogueApListDeviceType':mwRogueApListDeviceType,'mwRogueApListMeruAp1Rssi':mwRogueApListMeruAp1Rssi,'mwRogueApListMeruAp2Rssi':mwRogueApListMeruAp2Rssi,'mwRogueApListMeruAp3Rssi':mwRogueApListMeruAp3Rssi,'mwRogueApListNonReportedAudits':mwRogueApListNonReportedAudits,'mwRogueApListMeruAp1LastActivity':mwRogueApListMeruAp1LastActivity,'mwRogueApListMeruAp2LastActivity':mwRogueApListMeruAp2LastActivity,'mwRogueApListMeruAp3LastActivity':mwRogueApListMeruAp3LastActivity,'mwRogueDetectionApTable':mwRogueDetectionApTable,'mwRogueDetectionApEntry':mwRogueDetectionApEntry,_J:mwRogueDetectionApTableIndex,'mwRogueDetectionApNmsApNodeId':mwRogueDetectionApNmsApNodeId,'mwRogueDetectionApRowStatus':mwRogueDetectionApRowStatus})