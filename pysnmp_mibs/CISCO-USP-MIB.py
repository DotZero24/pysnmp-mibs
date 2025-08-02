_AQ='ciscoUspMIBNotifyGroup'
_AP='ciscoUspMIBMainObjectGroup'
_AO='cuspLicenseStateAlert'
_AN='cuspSipMessageQueueOverflowAlert'
_AM='cuspExtensiveLoggingAlert'
_AL='cuspLicenseExceededAlert'
_AK='cuspMemoryThresholdAlert'
_AJ='cuspServerGroupAlert'
_AI='cuspServerGroupElementAlert'
_AH='cuspConnectionExceptionAlert'
_AG='cuspDiskSpaceThresholdAlert'
_AF='cuspBackupProcessFailAlert'
_AE='cuspSystemStateAlert'
_AD='cuspSipMessageQueueOverflowAlertEnable'
_AC='cuspConnectionExceptionAlertEnable'
_AB='cuspMemoryThresholdAlertEnable'
_AA='cuspLicenseStateAlertEnable'
_A9='cuspServerGroupElementAlertEnable'
_A8='cuspElementPort'
_A7='cuspServerGroupLBType'
_A6='cuspServerGroupPingStatus'
_A5='cuspLicenseExceededAlertEnable'
_A4='cuspElementFailedCalls'
_A3='cuspElementTotalCalls'
_A2='cuspElementTransport'
_A1='cuspElementWeight'
_A0='cuspElementQValue'
_z='cuspServerGroupNetwork'
_y='cuspExtensiveLoggingAlertEnable'
_x='cuspBackupProcessFailAlertEnable'
_w='cuspDiskSpaceThresholdAlertEnable'
_v='cuspServerGroupAlertEnable'
_u='cuspSystemStateAlertEnable'
_t='cuspStrayMessageCount'
_s='cuspSmartAgentState'
_r='cuspNoOfMessagesRecieved'
_q='cuspSystemUpTime'
_p='cuspCallsDroppedExceedingLicense'
_o='cuspMaxCallsRoutedOneMin'
_n='cuspAvgCallsRoutedOneMin'
_m='cuspCallsRoutedOneSec'
_l='cuspMaxDroppedCPSOneMin'
_k='cuspAvgDroppedCPSOneMin'
_j='cuspDroppedCallsOneSec'
_i='cuspMaxCPSOneMin'
_h='cuspAvgCPSOneMin'
_g='cuspTotalFailedCalls'
_f='cuspTotalCalls'
_e='cuspLastCounterResetTime'
_d='accessible-for-notify'
_c='cuspElementIndex'
_b='not-accessible'
_a='MegaByte'
_Z='evalexpired'
_Y='Unsigned32'
_X='cuspLicenseState'
_W='cuspDiskSpaceUsed'
_V='cuspElementStatus'
_U='cuspElementName'
_T='cuspServerGroupStatus'
_S='cuspServerGroupName'
_R='cuspDiskSpaceThresholdValue'
_Q='cuspMemoryThresholdValue'
_P='cuspMemoryUsed'
_O='cuspConfiguredMemory'
_N='cuspSystemState'
_M='cuspCPS'
_L='cuspLicenseLimit'
_K='cuspServerGroupIndex'
_J='down'
_I='OctetString'
_H='CPS'
_G='cuspNotifDetail'
_F='Integer32'
_E='cuspNotifSeverity'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-USP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Y,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
ciscoUspMIB=ModuleIdentity((1,3,6,1,4,1,9,9,827))
if mibBuilder.loadTexts:ciscoUspMIB.setRevisions(('2015-07-20 00:00',))
_CiscoUspMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoUspMIBNotifs=_CiscoUspMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,827,0))
_CiscoUspMIBObjects_ObjectIdentity=ObjectIdentity
ciscoUspMIBObjects=_CiscoUspMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,827,1))
_CuspScalar_ObjectIdentity=ObjectIdentity
cuspScalar=_CuspScalar_ObjectIdentity((1,3,6,1,4,1,9,9,827,1,1))
_CuspLastCounterResetTime_Type=DateAndTime
_CuspLastCounterResetTime_Object=MibScalar
cuspLastCounterResetTime=_CuspLastCounterResetTime_Object((1,3,6,1,4,1,9,9,827,1,1,1),_CuspLastCounterResetTime_Type())
cuspLastCounterResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspLastCounterResetTime.setStatus(_B)
class _CuspSystemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_J,2)))
_CuspSystemState_Type.__name__=_F
_CuspSystemState_Object=MibScalar
cuspSystemState=_CuspSystemState_Object((1,3,6,1,4,1,9,9,827,1,1,2),_CuspSystemState_Type())
cuspSystemState.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspSystemState.setStatus(_B)
_CuspSystemUpTime_Type=TimeStamp
_CuspSystemUpTime_Object=MibScalar
cuspSystemUpTime=_CuspSystemUpTime_Object((1,3,6,1,4,1,9,9,827,1,1,3),_CuspSystemUpTime_Type())
cuspSystemUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspSystemUpTime.setStatus(_B)
class _CuspLicenseLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CuspLicenseLimit_Type.__name__=_Y
_CuspLicenseLimit_Object=MibScalar
cuspLicenseLimit=_CuspLicenseLimit_Object((1,3,6,1,4,1,9,9,827,1,1,4),_CuspLicenseLimit_Type())
cuspLicenseLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspLicenseLimit.setStatus(_B)
if mibBuilder.loadTexts:cuspLicenseLimit.setUnits(_H)
class _CuspLicenseState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('waiting',1),('overage',2),('outofcompliance',3),('notapplicable',4),('invalidtag',5),('invalid',6),('init',7),('incompliance',8),(_Z,9),('eval',10),('disabled',11),('authorizedperiodexpired',12)))
_CuspLicenseState_Type.__name__=_F
_CuspLicenseState_Object=MibScalar
cuspLicenseState=_CuspLicenseState_Object((1,3,6,1,4,1,9,9,827,1,1,5),_CuspLicenseState_Type())
cuspLicenseState.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspLicenseState.setStatus(_B)
class _CuspSmartAgentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unconfigured',1),('unidentified',2),(_Z,3),('registered',4),('outofcomplaince',5),('authorized',6),('authorizationexpiry',7),('transient',8)))
_CuspSmartAgentState_Type.__name__=_F
_CuspSmartAgentState_Object=MibScalar
cuspSmartAgentState=_CuspSmartAgentState_Object((1,3,6,1,4,1,9,9,827,1,1,6),_CuspSmartAgentState_Type())
cuspSmartAgentState.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspSmartAgentState.setStatus(_B)
_CuspConfiguredMemory_Type=Unsigned32
_CuspConfiguredMemory_Object=MibScalar
cuspConfiguredMemory=_CuspConfiguredMemory_Object((1,3,6,1,4,1,9,9,827,1,1,7),_CuspConfiguredMemory_Type())
cuspConfiguredMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspConfiguredMemory.setStatus(_B)
if mibBuilder.loadTexts:cuspConfiguredMemory.setUnits(_a)
_CuspMemoryUsed_Type=Unsigned32
_CuspMemoryUsed_Object=MibScalar
cuspMemoryUsed=_CuspMemoryUsed_Object((1,3,6,1,4,1,9,9,827,1,1,8),_CuspMemoryUsed_Type())
cuspMemoryUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspMemoryUsed.setStatus(_B)
if mibBuilder.loadTexts:cuspMemoryUsed.setUnits(_a)
_CuspDiskSpaceUsed_Type=Integer32
_CuspDiskSpaceUsed_Object=MibScalar
cuspDiskSpaceUsed=_CuspDiskSpaceUsed_Object((1,3,6,1,4,1,9,9,827,1,1,9),_CuspDiskSpaceUsed_Type())
cuspDiskSpaceUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspDiskSpaceUsed.setStatus(_B)
_CuspCallStats_ObjectIdentity=ObjectIdentity
cuspCallStats=_CuspCallStats_ObjectIdentity((1,3,6,1,4,1,9,9,827,1,1,10))
_CuspTotalCalls_Type=Counter32
_CuspTotalCalls_Object=MibScalar
cuspTotalCalls=_CuspTotalCalls_Object((1,3,6,1,4,1,9,9,827,1,1,10,1),_CuspTotalCalls_Type())
cuspTotalCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspTotalCalls.setStatus(_B)
_CuspTotalFailedCalls_Type=Counter32
_CuspTotalFailedCalls_Object=MibScalar
cuspTotalFailedCalls=_CuspTotalFailedCalls_Object((1,3,6,1,4,1,9,9,827,1,1,10,2),_CuspTotalFailedCalls_Type())
cuspTotalFailedCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspTotalFailedCalls.setStatus(_B)
_CuspCPS_Type=Unsigned32
_CuspCPS_Object=MibScalar
cuspCPS=_CuspCPS_Object((1,3,6,1,4,1,9,9,827,1,1,10,3),_CuspCPS_Type())
cuspCPS.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspCPS.setStatus(_B)
if mibBuilder.loadTexts:cuspCPS.setUnits(_H)
_CuspAvgCPSOneMin_Type=Unsigned32
_CuspAvgCPSOneMin_Object=MibScalar
cuspAvgCPSOneMin=_CuspAvgCPSOneMin_Object((1,3,6,1,4,1,9,9,827,1,1,10,4),_CuspAvgCPSOneMin_Type())
cuspAvgCPSOneMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspAvgCPSOneMin.setStatus(_B)
if mibBuilder.loadTexts:cuspAvgCPSOneMin.setUnits(_H)
_CuspMaxCPSOneMin_Type=Unsigned32
_CuspMaxCPSOneMin_Object=MibScalar
cuspMaxCPSOneMin=_CuspMaxCPSOneMin_Object((1,3,6,1,4,1,9,9,827,1,1,10,5),_CuspMaxCPSOneMin_Type())
cuspMaxCPSOneMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspMaxCPSOneMin.setStatus(_B)
if mibBuilder.loadTexts:cuspMaxCPSOneMin.setUnits(_H)
_CuspDroppedCallsOneSec_Type=Unsigned32
_CuspDroppedCallsOneSec_Object=MibScalar
cuspDroppedCallsOneSec=_CuspDroppedCallsOneSec_Object((1,3,6,1,4,1,9,9,827,1,1,10,6),_CuspDroppedCallsOneSec_Type())
cuspDroppedCallsOneSec.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspDroppedCallsOneSec.setStatus(_B)
_CuspAvgDroppedCPSOneMin_Type=Unsigned32
_CuspAvgDroppedCPSOneMin_Object=MibScalar
cuspAvgDroppedCPSOneMin=_CuspAvgDroppedCPSOneMin_Object((1,3,6,1,4,1,9,9,827,1,1,10,7),_CuspAvgDroppedCPSOneMin_Type())
cuspAvgDroppedCPSOneMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspAvgDroppedCPSOneMin.setStatus(_B)
_CuspMaxDroppedCPSOneMin_Type=Unsigned32
_CuspMaxDroppedCPSOneMin_Object=MibScalar
cuspMaxDroppedCPSOneMin=_CuspMaxDroppedCPSOneMin_Object((1,3,6,1,4,1,9,9,827,1,1,10,8),_CuspMaxDroppedCPSOneMin_Type())
cuspMaxDroppedCPSOneMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspMaxDroppedCPSOneMin.setStatus(_B)
_CuspCallsRoutedOneSec_Type=Unsigned32
_CuspCallsRoutedOneSec_Object=MibScalar
cuspCallsRoutedOneSec=_CuspCallsRoutedOneSec_Object((1,3,6,1,4,1,9,9,827,1,1,10,9),_CuspCallsRoutedOneSec_Type())
cuspCallsRoutedOneSec.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspCallsRoutedOneSec.setStatus(_B)
_CuspAvgCallsRoutedOneMin_Type=Unsigned32
_CuspAvgCallsRoutedOneMin_Object=MibScalar
cuspAvgCallsRoutedOneMin=_CuspAvgCallsRoutedOneMin_Object((1,3,6,1,4,1,9,9,827,1,1,10,10),_CuspAvgCallsRoutedOneMin_Type())
cuspAvgCallsRoutedOneMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspAvgCallsRoutedOneMin.setStatus(_B)
_CuspMaxCallsRoutedOneMin_Type=Unsigned32
_CuspMaxCallsRoutedOneMin_Object=MibScalar
cuspMaxCallsRoutedOneMin=_CuspMaxCallsRoutedOneMin_Object((1,3,6,1,4,1,9,9,827,1,1,10,11),_CuspMaxCallsRoutedOneMin_Type())
cuspMaxCallsRoutedOneMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspMaxCallsRoutedOneMin.setStatus(_B)
_CuspCallsDroppedExceedingLicense_Type=Unsigned32
_CuspCallsDroppedExceedingLicense_Object=MibScalar
cuspCallsDroppedExceedingLicense=_CuspCallsDroppedExceedingLicense_Object((1,3,6,1,4,1,9,9,827,1,1,10,12),_CuspCallsDroppedExceedingLicense_Type())
cuspCallsDroppedExceedingLicense.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspCallsDroppedExceedingLicense.setStatus(_B)
if mibBuilder.loadTexts:cuspCallsDroppedExceedingLicense.setUnits(_H)
_CuspMessageStats_ObjectIdentity=ObjectIdentity
cuspMessageStats=_CuspMessageStats_ObjectIdentity((1,3,6,1,4,1,9,9,827,1,1,11))
_CuspStrayMessageCount_Type=Unsigned32
_CuspStrayMessageCount_Object=MibScalar
cuspStrayMessageCount=_CuspStrayMessageCount_Object((1,3,6,1,4,1,9,9,827,1,1,11,1),_CuspStrayMessageCount_Type())
cuspStrayMessageCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspStrayMessageCount.setStatus(_B)
if mibBuilder.loadTexts:cuspStrayMessageCount.setUnits('Messages')
_CuspNoOfMessagesRecieved_Type=Unsigned32
_CuspNoOfMessagesRecieved_Object=MibScalar
cuspNoOfMessagesRecieved=_CuspNoOfMessagesRecieved_Object((1,3,6,1,4,1,9,9,827,1,1,11,2),_CuspNoOfMessagesRecieved_Type())
cuspNoOfMessagesRecieved.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspNoOfMessagesRecieved.setStatus(_B)
_CuspThresholdValues_ObjectIdentity=ObjectIdentity
cuspThresholdValues=_CuspThresholdValues_ObjectIdentity((1,3,6,1,4,1,9,9,827,1,1,12))
class _CuspDiskSpaceThresholdValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CuspDiskSpaceThresholdValue_Type.__name__=_F
_CuspDiskSpaceThresholdValue_Object=MibScalar
cuspDiskSpaceThresholdValue=_CuspDiskSpaceThresholdValue_Object((1,3,6,1,4,1,9,9,827,1,1,12,1),_CuspDiskSpaceThresholdValue_Type())
cuspDiskSpaceThresholdValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cuspDiskSpaceThresholdValue.setStatus(_B)
class _CuspMemoryThresholdValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CuspMemoryThresholdValue_Type.__name__=_F
_CuspMemoryThresholdValue_Object=MibScalar
cuspMemoryThresholdValue=_CuspMemoryThresholdValue_Object((1,3,6,1,4,1,9,9,827,1,1,12,2),_CuspMemoryThresholdValue_Type())
cuspMemoryThresholdValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cuspMemoryThresholdValue.setStatus(_B)
_CuspTable_ObjectIdentity=ObjectIdentity
cuspTable=_CuspTable_ObjectIdentity((1,3,6,1,4,1,9,9,827,1,2))
_CuspServerGroupTable_Object=MibTable
cuspServerGroupTable=_CuspServerGroupTable_Object((1,3,6,1,4,1,9,9,827,1,2,1))
if mibBuilder.loadTexts:cuspServerGroupTable.setStatus(_B)
_CuspServerGroupEntry_Object=MibTableRow
cuspServerGroupEntry=_CuspServerGroupEntry_Object((1,3,6,1,4,1,9,9,827,1,2,1,1))
cuspServerGroupEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:cuspServerGroupEntry.setStatus(_B)
_CuspServerGroupIndex_Type=Unsigned32
_CuspServerGroupIndex_Object=MibTableColumn
cuspServerGroupIndex=_CuspServerGroupIndex_Object((1,3,6,1,4,1,9,9,827,1,2,1,1,1),_CuspServerGroupIndex_Type())
cuspServerGroupIndex.setMaxAccess(_b)
if mibBuilder.loadTexts:cuspServerGroupIndex.setStatus(_B)
_CuspServerGroupName_Type=OctetString
_CuspServerGroupName_Object=MibTableColumn
cuspServerGroupName=_CuspServerGroupName_Object((1,3,6,1,4,1,9,9,827,1,2,1,1,2),_CuspServerGroupName_Type())
cuspServerGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspServerGroupName.setStatus(_B)
_CuspServerGroupNetwork_Type=OctetString
_CuspServerGroupNetwork_Object=MibTableColumn
cuspServerGroupNetwork=_CuspServerGroupNetwork_Object((1,3,6,1,4,1,9,9,827,1,2,1,1,3),_CuspServerGroupNetwork_Type())
cuspServerGroupNetwork.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspServerGroupNetwork.setStatus(_B)
class _CuspServerGroupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('partialdown',2),(_J,3)))
_CuspServerGroupStatus_Type.__name__=_F
_CuspServerGroupStatus_Object=MibTableColumn
cuspServerGroupStatus=_CuspServerGroupStatus_Object((1,3,6,1,4,1,9,9,827,1,2,1,1,4),_CuspServerGroupStatus_Type())
cuspServerGroupStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspServerGroupStatus.setStatus(_B)
_CuspServerGroupPingStatus_Type=TruthValue
_CuspServerGroupPingStatus_Object=MibTableColumn
cuspServerGroupPingStatus=_CuspServerGroupPingStatus_Object((1,3,6,1,4,1,9,9,827,1,2,1,1,5),_CuspServerGroupPingStatus_Type())
cuspServerGroupPingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspServerGroupPingStatus.setStatus(_B)
class _CuspServerGroupLBType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('global',1),('highestq',2),('requesturi',3),('callid',4),('touri',5),('weight',6)))
_CuspServerGroupLBType_Type.__name__=_F
_CuspServerGroupLBType_Object=MibTableColumn
cuspServerGroupLBType=_CuspServerGroupLBType_Object((1,3,6,1,4,1,9,9,827,1,2,1,1,6),_CuspServerGroupLBType_Type())
cuspServerGroupLBType.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspServerGroupLBType.setStatus(_B)
_CuspElementTable_Object=MibTable
cuspElementTable=_CuspElementTable_Object((1,3,6,1,4,1,9,9,827,1,2,2))
if mibBuilder.loadTexts:cuspElementTable.setStatus(_B)
_CuspElementEntry_Object=MibTableRow
cuspElementEntry=_CuspElementEntry_Object((1,3,6,1,4,1,9,9,827,1,2,2,1))
cuspElementEntry.setIndexNames((0,_A,_K),(0,_A,_c))
if mibBuilder.loadTexts:cuspElementEntry.setStatus(_B)
_CuspElementIndex_Type=Unsigned32
_CuspElementIndex_Object=MibTableColumn
cuspElementIndex=_CuspElementIndex_Object((1,3,6,1,4,1,9,9,827,1,2,2,1,1),_CuspElementIndex_Type())
cuspElementIndex.setMaxAccess(_b)
if mibBuilder.loadTexts:cuspElementIndex.setStatus(_B)
class _CuspElementName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CuspElementName_Type.__name__=_I
_CuspElementName_Object=MibTableColumn
cuspElementName=_CuspElementName_Object((1,3,6,1,4,1,9,9,827,1,2,2,1,2),_CuspElementName_Type())
cuspElementName.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspElementName.setStatus(_B)
class _CuspElementStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_J,2)))
_CuspElementStatus_Type.__name__=_F
_CuspElementStatus_Object=MibTableColumn
cuspElementStatus=_CuspElementStatus_Object((1,3,6,1,4,1,9,9,827,1,2,2,1,3),_CuspElementStatus_Type())
cuspElementStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspElementStatus.setStatus(_B)
_CuspElementQValue_Type=OctetString
_CuspElementQValue_Object=MibTableColumn
cuspElementQValue=_CuspElementQValue_Object((1,3,6,1,4,1,9,9,827,1,2,2,1,4),_CuspElementQValue_Type())
cuspElementQValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspElementQValue.setStatus(_B)
class _CuspElementWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CuspElementWeight_Type.__name__=_F
_CuspElementWeight_Object=MibTableColumn
cuspElementWeight=_CuspElementWeight_Object((1,3,6,1,4,1,9,9,827,1,2,2,1,5),_CuspElementWeight_Type())
cuspElementWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspElementWeight.setStatus(_B)
_CuspElementPort_Type=Integer32
_CuspElementPort_Object=MibTableColumn
cuspElementPort=_CuspElementPort_Object((1,3,6,1,4,1,9,9,827,1,2,2,1,6),_CuspElementPort_Type())
cuspElementPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspElementPort.setStatus(_B)
class _CuspElementTransport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('udp',1),('tcp',2),('tls',3)))
_CuspElementTransport_Type.__name__=_F
_CuspElementTransport_Object=MibTableColumn
cuspElementTransport=_CuspElementTransport_Object((1,3,6,1,4,1,9,9,827,1,2,2,1,7),_CuspElementTransport_Type())
cuspElementTransport.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspElementTransport.setStatus(_B)
_CuspElementTotalCalls_Type=Unsigned32
_CuspElementTotalCalls_Object=MibTableColumn
cuspElementTotalCalls=_CuspElementTotalCalls_Object((1,3,6,1,4,1,9,9,827,1,2,2,1,8),_CuspElementTotalCalls_Type())
cuspElementTotalCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspElementTotalCalls.setStatus(_B)
_CuspElementFailedCalls_Type=Unsigned32
_CuspElementFailedCalls_Object=MibTableColumn
cuspElementFailedCalls=_CuspElementFailedCalls_Object((1,3,6,1,4,1,9,9,827,1,2,2,1,9),_CuspElementFailedCalls_Type())
cuspElementFailedCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cuspElementFailedCalls.setStatus(_B)
_CuspNotifControlInfo_ObjectIdentity=ObjectIdentity
cuspNotifControlInfo=_CuspNotifControlInfo_ObjectIdentity((1,3,6,1,4,1,9,9,827,1,3))
class _CuspNotifSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('error',1),('warning',2),('informational',3)))
_CuspNotifSeverity_Type.__name__=_F
_CuspNotifSeverity_Object=MibScalar
cuspNotifSeverity=_CuspNotifSeverity_Object((1,3,6,1,4,1,9,9,827,1,3,1),_CuspNotifSeverity_Type())
cuspNotifSeverity.setMaxAccess(_d)
if mibBuilder.loadTexts:cuspNotifSeverity.setStatus(_B)
class _CuspNotifDetail_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CuspNotifDetail_Type.__name__=_I
_CuspNotifDetail_Object=MibScalar
cuspNotifDetail=_CuspNotifDetail_Object((1,3,6,1,4,1,9,9,827,1,3,2),_CuspNotifDetail_Type())
cuspNotifDetail.setMaxAccess(_d)
if mibBuilder.loadTexts:cuspNotifDetail.setStatus(_B)
_CuspSystemStateAlertEnable_Type=TruthValue
_CuspSystemStateAlertEnable_Object=MibScalar
cuspSystemStateAlertEnable=_CuspSystemStateAlertEnable_Object((1,3,6,1,4,1,9,9,827,1,3,3),_CuspSystemStateAlertEnable_Type())
cuspSystemStateAlertEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cuspSystemStateAlertEnable.setStatus(_B)
_CuspServerGroupAlertEnable_Type=TruthValue
_CuspServerGroupAlertEnable_Object=MibScalar
cuspServerGroupAlertEnable=_CuspServerGroupAlertEnable_Object((1,3,6,1,4,1,9,9,827,1,3,4),_CuspServerGroupAlertEnable_Type())
cuspServerGroupAlertEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cuspServerGroupAlertEnable.setStatus(_B)
_CuspServerGroupElementAlertEnable_Type=TruthValue
_CuspServerGroupElementAlertEnable_Object=MibScalar
cuspServerGroupElementAlertEnable=_CuspServerGroupElementAlertEnable_Object((1,3,6,1,4,1,9,9,827,1,3,5),_CuspServerGroupElementAlertEnable_Type())
cuspServerGroupElementAlertEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cuspServerGroupElementAlertEnable.setStatus(_B)
_CuspLicenseExceededAlertEnable_Type=TruthValue
_CuspLicenseExceededAlertEnable_Object=MibScalar
cuspLicenseExceededAlertEnable=_CuspLicenseExceededAlertEnable_Object((1,3,6,1,4,1,9,9,827,1,3,6),_CuspLicenseExceededAlertEnable_Type())
cuspLicenseExceededAlertEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cuspLicenseExceededAlertEnable.setStatus(_B)
_CuspLicenseStateAlertEnable_Type=TruthValue
_CuspLicenseStateAlertEnable_Object=MibScalar
cuspLicenseStateAlertEnable=_CuspLicenseStateAlertEnable_Object((1,3,6,1,4,1,9,9,827,1,3,7),_CuspLicenseStateAlertEnable_Type())
cuspLicenseStateAlertEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cuspLicenseStateAlertEnable.setStatus(_B)
_CuspExtensiveLoggingAlertEnable_Type=TruthValue
_CuspExtensiveLoggingAlertEnable_Object=MibScalar
cuspExtensiveLoggingAlertEnable=_CuspExtensiveLoggingAlertEnable_Object((1,3,6,1,4,1,9,9,827,1,3,8),_CuspExtensiveLoggingAlertEnable_Type())
cuspExtensiveLoggingAlertEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cuspExtensiveLoggingAlertEnable.setStatus(_B)
_CuspDiskSpaceThresholdAlertEnable_Type=TruthValue
_CuspDiskSpaceThresholdAlertEnable_Object=MibScalar
cuspDiskSpaceThresholdAlertEnable=_CuspDiskSpaceThresholdAlertEnable_Object((1,3,6,1,4,1,9,9,827,1,3,9),_CuspDiskSpaceThresholdAlertEnable_Type())
cuspDiskSpaceThresholdAlertEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cuspDiskSpaceThresholdAlertEnable.setStatus(_B)
_CuspMemoryThresholdAlertEnable_Type=TruthValue
_CuspMemoryThresholdAlertEnable_Object=MibScalar
cuspMemoryThresholdAlertEnable=_CuspMemoryThresholdAlertEnable_Object((1,3,6,1,4,1,9,9,827,1,3,10),_CuspMemoryThresholdAlertEnable_Type())
cuspMemoryThresholdAlertEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cuspMemoryThresholdAlertEnable.setStatus(_B)
_CuspBackupProcessFailAlertEnable_Type=TruthValue
_CuspBackupProcessFailAlertEnable_Object=MibScalar
cuspBackupProcessFailAlertEnable=_CuspBackupProcessFailAlertEnable_Object((1,3,6,1,4,1,9,9,827,1,3,11),_CuspBackupProcessFailAlertEnable_Type())
cuspBackupProcessFailAlertEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cuspBackupProcessFailAlertEnable.setStatus(_B)
_CuspConnectionExceptionAlertEnable_Type=TruthValue
_CuspConnectionExceptionAlertEnable_Object=MibScalar
cuspConnectionExceptionAlertEnable=_CuspConnectionExceptionAlertEnable_Object((1,3,6,1,4,1,9,9,827,1,3,12),_CuspConnectionExceptionAlertEnable_Type())
cuspConnectionExceptionAlertEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cuspConnectionExceptionAlertEnable.setStatus(_B)
_CuspSipMessageQueueOverflowAlertEnable_Type=TruthValue
_CuspSipMessageQueueOverflowAlertEnable_Object=MibScalar
cuspSipMessageQueueOverflowAlertEnable=_CuspSipMessageQueueOverflowAlertEnable_Object((1,3,6,1,4,1,9,9,827,1,3,13),_CuspSipMessageQueueOverflowAlertEnable_Type())
cuspSipMessageQueueOverflowAlertEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cuspSipMessageQueueOverflowAlertEnable.setStatus(_B)
_CiscoUspMIBConform_ObjectIdentity=ObjectIdentity
ciscoUspMIBConform=_CiscoUspMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,827,2))
_CiscoUspMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoUspMIBCompliances=_CiscoUspMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,827,2,1))
_CiscoUspMIBGroups_ObjectIdentity=ObjectIdentity
ciscoUspMIBGroups=_CiscoUspMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,827,2,2))
ciscoUspMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,827,2,2,1))
ciscoUspMIBMainObjectGroup.setObjects(*((_A,_L),(_A,_e),(_A,_f),(_A,_g),(_A,_M),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_N),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_O),(_A,_P),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_Q),(_A,_R),(_A,_S),(_A,_z),(_A,_T),(_A,_U),(_A,_V),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_E),(_A,_G),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_W),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_X)))
if mibBuilder.loadTexts:ciscoUspMIBMainObjectGroup.setStatus(_B)
cuspSystemStateAlert=NotificationType((1,3,6,1,4,1,9,9,827,0,1))
cuspSystemStateAlert.setObjects(*((_A,_E),(_A,_G),(_A,_N)))
if mibBuilder.loadTexts:cuspSystemStateAlert.setStatus(_B)
cuspServerGroupElementAlert=NotificationType((1,3,6,1,4,1,9,9,827,0,2))
cuspServerGroupElementAlert.setObjects(*((_A,_E),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:cuspServerGroupElementAlert.setStatus(_B)
cuspServerGroupAlert=NotificationType((1,3,6,1,4,1,9,9,827,0,3))
cuspServerGroupAlert.setObjects(*((_A,_E),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:cuspServerGroupAlert.setStatus(_B)
cuspMemoryThresholdAlert=NotificationType((1,3,6,1,4,1,9,9,827,0,4))
cuspMemoryThresholdAlert.setObjects(*((_A,_E),(_A,_Q),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:cuspMemoryThresholdAlert.setStatus(_B)
cuspLicenseExceededAlert=NotificationType((1,3,6,1,4,1,9,9,827,0,5))
cuspLicenseExceededAlert.setObjects(*((_A,_E),(_A,_M),(_A,_L)))
if mibBuilder.loadTexts:cuspLicenseExceededAlert.setStatus(_B)
cuspLicenseStateAlert=NotificationType((1,3,6,1,4,1,9,9,827,0,6))
cuspLicenseStateAlert.setObjects(*((_A,_E),(_A,_X)))
if mibBuilder.loadTexts:cuspLicenseStateAlert.setStatus(_B)
cuspExtensiveLoggingAlert=NotificationType((1,3,6,1,4,1,9,9,827,0,7))
cuspExtensiveLoggingAlert.setObjects(*((_A,_E),(_A,_G)))
if mibBuilder.loadTexts:cuspExtensiveLoggingAlert.setStatus(_B)
cuspDiskSpaceThresholdAlert=NotificationType((1,3,6,1,4,1,9,9,827,0,8))
cuspDiskSpaceThresholdAlert.setObjects(*((_A,_E),(_A,_R),(_A,_W)))
if mibBuilder.loadTexts:cuspDiskSpaceThresholdAlert.setStatus(_B)
cuspBackupProcessFailAlert=NotificationType((1,3,6,1,4,1,9,9,827,0,9))
cuspBackupProcessFailAlert.setObjects(*((_A,_E),(_A,_G)))
if mibBuilder.loadTexts:cuspBackupProcessFailAlert.setStatus(_B)
cuspConnectionExceptionAlert=NotificationType((1,3,6,1,4,1,9,9,827,0,10))
cuspConnectionExceptionAlert.setObjects(*((_A,_E),(_A,_G)))
if mibBuilder.loadTexts:cuspConnectionExceptionAlert.setStatus(_B)
cuspSipMessageQueueOverflowAlert=NotificationType((1,3,6,1,4,1,9,9,827,0,11))
cuspSipMessageQueueOverflowAlert.setObjects(*((_A,_E),(_A,_G)))
if mibBuilder.loadTexts:cuspSipMessageQueueOverflowAlert.setStatus(_B)
ciscoUspMIBNotifyGroup=NotificationGroup((1,3,6,1,4,1,9,9,827,2,2,2))
ciscoUspMIBNotifyGroup.setObjects(*((_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:ciscoUspMIBNotifyGroup.setStatus(_B)
ciscoUspMIBModuleCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,827,2,1,1))
ciscoUspMIBModuleCompliance.setObjects(*((_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:ciscoUspMIBModuleCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoUspMIB':ciscoUspMIB,'ciscoUspMIBNotifs':ciscoUspMIBNotifs,_AE:cuspSystemStateAlert,_AI:cuspServerGroupElementAlert,_AJ:cuspServerGroupAlert,_AK:cuspMemoryThresholdAlert,_AL:cuspLicenseExceededAlert,_AO:cuspLicenseStateAlert,_AM:cuspExtensiveLoggingAlert,_AG:cuspDiskSpaceThresholdAlert,_AF:cuspBackupProcessFailAlert,_AH:cuspConnectionExceptionAlert,_AN:cuspSipMessageQueueOverflowAlert,'ciscoUspMIBObjects':ciscoUspMIBObjects,'cuspScalar':cuspScalar,_e:cuspLastCounterResetTime,_N:cuspSystemState,_q:cuspSystemUpTime,_L:cuspLicenseLimit,_X:cuspLicenseState,_s:cuspSmartAgentState,_O:cuspConfiguredMemory,_P:cuspMemoryUsed,_W:cuspDiskSpaceUsed,'cuspCallStats':cuspCallStats,_f:cuspTotalCalls,_g:cuspTotalFailedCalls,_M:cuspCPS,_h:cuspAvgCPSOneMin,_i:cuspMaxCPSOneMin,_j:cuspDroppedCallsOneSec,_k:cuspAvgDroppedCPSOneMin,_l:cuspMaxDroppedCPSOneMin,_m:cuspCallsRoutedOneSec,_n:cuspAvgCallsRoutedOneMin,_o:cuspMaxCallsRoutedOneMin,_p:cuspCallsDroppedExceedingLicense,'cuspMessageStats':cuspMessageStats,_t:cuspStrayMessageCount,_r:cuspNoOfMessagesRecieved,'cuspThresholdValues':cuspThresholdValues,_R:cuspDiskSpaceThresholdValue,_Q:cuspMemoryThresholdValue,'cuspTable':cuspTable,'cuspServerGroupTable':cuspServerGroupTable,'cuspServerGroupEntry':cuspServerGroupEntry,_K:cuspServerGroupIndex,_S:cuspServerGroupName,_z:cuspServerGroupNetwork,_T:cuspServerGroupStatus,_A6:cuspServerGroupPingStatus,_A7:cuspServerGroupLBType,'cuspElementTable':cuspElementTable,'cuspElementEntry':cuspElementEntry,_c:cuspElementIndex,_U:cuspElementName,_V:cuspElementStatus,_A0:cuspElementQValue,_A1:cuspElementWeight,_A8:cuspElementPort,_A2:cuspElementTransport,_A3:cuspElementTotalCalls,_A4:cuspElementFailedCalls,'cuspNotifControlInfo':cuspNotifControlInfo,_E:cuspNotifSeverity,_G:cuspNotifDetail,_u:cuspSystemStateAlertEnable,_v:cuspServerGroupAlertEnable,_A9:cuspServerGroupElementAlertEnable,_A5:cuspLicenseExceededAlertEnable,_AA:cuspLicenseStateAlertEnable,_y:cuspExtensiveLoggingAlertEnable,_w:cuspDiskSpaceThresholdAlertEnable,_AB:cuspMemoryThresholdAlertEnable,_x:cuspBackupProcessFailAlertEnable,_AC:cuspConnectionExceptionAlertEnable,_AD:cuspSipMessageQueueOverflowAlertEnable,'ciscoUspMIBConform':ciscoUspMIBConform,'ciscoUspMIBCompliances':ciscoUspMIBCompliances,'ciscoUspMIBModuleCompliance':ciscoUspMIBModuleCompliance,'ciscoUspMIBGroups':ciscoUspMIBGroups,_AP:ciscoUspMIBMainObjectGroup,_AQ:ciscoUspMIBNotifyGroup})