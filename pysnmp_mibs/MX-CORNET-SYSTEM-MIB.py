_A6='corNetSystemServicesGroupVer1'
_A5='corNetSystemDataGroupVer1'
_A4='corNetSystemFaultManagementGroupVer1'
_A3='corNetSystemSecurityGroupVer1'
_A2='corNetSystemInitializationGroupVer1'
_A1='corNetSystemRegistrationGroupVer1'
_A0='corNetFaultManagementJitterBufferTrap'
_z='corNetFaultManagementPacketsLostTrap'
_y='corNetFaultManagementLanTrap'
_x='corNetFaultManagementAuthenticationFailureTrap'
_w='corNetFaultManagementRebootTrap'
_v='corNetSystemServicesTimeoutInterDigit'
_u='corNetSystemServices2StageEndKey'
_t='corNetSystemServices2StageTimeout'
_s='corNetSystemServices2StageEndingMethod'
_r='corNetSystemCallFeaturesEnable'
_q='corNetSystemServiceFirstDigitTimer'
_p='corNetSystemService2StageFlag'
_o='corNetSystemServiceActivationSequence'
_n='corNetSystemServiceKbKeyCode'
_m='corNetSystemServiceEnable'
_l='corNetSystemServiceName'
_k='corNetSystemDataVoiceOnlyModeEnable'
_j='corNetSystemDataRfc2833DefaultPayloadType'
_i='corNetSystemDataRfc2198DefaultPayloadType'
_h='corNetSystemDataRfc2198RedundancyLevel'
_g='ipAddressStatusCorNetFaultManagementTrapPort'
_f='ipAddressStatusCorNetFaultManagementHost'
_e='ipAddressConfigCorNetFaultManagementTrapPort'
_d='ipAddressConfigCorNetFaultManagementHost'
_c='corNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio'
_b='corNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio'
_a='corNetSystemFaultManagementTrapsMaximumPacketsLostRatio'
_Z='corNetSystemFaultManagementTrapsReportDelay'
_Y='corNetSystemFaultManagementTrapsComputePeriod'
_X='corNetSystemFaultManagementTrapsEnable'
_W='corNetSystemSecurityLevel'
_V='corNetSystemSecurityPassword'
_U='corNetSystemInitEmergencyNumber'
_T='corNetSystemRegLocationIdentifierNumber'
_S='corNetSystemRegSubscriberNumber'
_R='normal'
_Q='corNetFaultManagementJitterBufferStatus'
_P='corNetFaultManagementPacketsLostStatus'
_O='corNetSystemServicesIndex'
_N='sysMacAddress'
_M='sysObjectID'
_L='MxIpPort'
_K='MxIpHostName'
_J='MxEnableState'
_I='Integer32'
_H='read-only'
_G='ifIndex'
_F='IF-MIB'
_E='OctetString'
_D='Unsigned32'
_C='read-write'
_B='MX-CORNET-SYSTEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
corNet,ipAddressConfigCorNet,ipAddressConfigCorNetStatic,ipAddressStatusCorNet=mibBuilder.importSymbols('MX-CORNET-MIB','corNet','ipAddressConfigCorNet','ipAddressConfigCorNetStatic','ipAddressStatusCorNet')
ipAddressConfig,ipAddressStatus,mediatrixMgmt=mibBuilder.importSymbols('MX-SMI','ipAddressConfig','ipAddressStatus','mediatrixMgmt')
MxAdvancedIpPort,MxEnableState,MxIpHostName,MxIpPort=mibBuilder.importSymbols('MX-TC','MxAdvancedIpPort',_J,_K,_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
corNetSystemMIB=ModuleIdentity((1,3,6,1,4,1,4935,20,40,1))
if mibBuilder.loadTexts:corNetSystemMIB.setRevisions(('2006-07-17 00:00','2005-12-02 00:00','2005-07-07 00:00','2005-06-27 00:00','2005-06-10 00:00','2005-05-16 00:00','2005-05-06 00:00','2004-06-15 00:00'))
_IpAddressStatusCorNetPbxIfTable_Object=MibTable
ipAddressStatusCorNetPbxIfTable=_IpAddressStatusCorNetPbxIfTable_Object((1,3,6,1,4,1,4935,10,1,130,10))
if mibBuilder.loadTexts:ipAddressStatusCorNetPbxIfTable.setStatus(_A)
_IpAddressStatusCorNetPbxIfEntry_Object=MibTableRow
ipAddressStatusCorNetPbxIfEntry=_IpAddressStatusCorNetPbxIfEntry_Object((1,3,6,1,4,1,4935,10,1,130,10,1))
ipAddressStatusCorNetPbxIfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ipAddressStatusCorNetPbxIfEntry.setStatus(_A)
class _IpAddressStatusCorNetPbxHost_Type(MxIpHostName):defaultValue=OctetString('')
_IpAddressStatusCorNetPbxHost_Type.__name__=_K
_IpAddressStatusCorNetPbxHost_Object=MibTableColumn
ipAddressStatusCorNetPbxHost=_IpAddressStatusCorNetPbxHost_Object((1,3,6,1,4,1,4935,10,1,130,10,1,10),_IpAddressStatusCorNetPbxHost_Type())
ipAddressStatusCorNetPbxHost.setMaxAccess(_H)
if mibBuilder.loadTexts:ipAddressStatusCorNetPbxHost.setStatus(_A)
class _IpAddressStatusCorNetPbxPort_Type(MxIpPort):defaultValue=4060
_IpAddressStatusCorNetPbxPort_Type.__name__=_L
_IpAddressStatusCorNetPbxPort_Object=MibTableColumn
ipAddressStatusCorNetPbxPort=_IpAddressStatusCorNetPbxPort_Object((1,3,6,1,4,1,4935,10,1,130,10,1,20),_IpAddressStatusCorNetPbxPort_Type())
ipAddressStatusCorNetPbxPort.setMaxAccess(_H)
if mibBuilder.loadTexts:ipAddressStatusCorNetPbxPort.setStatus(_A)
class _IpAddressStatusCorNetFaultManagementHost_Type(MxIpHostName):defaultValue=OctetString('')
_IpAddressStatusCorNetFaultManagementHost_Type.__name__=_K
_IpAddressStatusCorNetFaultManagementHost_Object=MibScalar
ipAddressStatusCorNetFaultManagementHost=_IpAddressStatusCorNetFaultManagementHost_Object((1,3,6,1,4,1,4935,10,1,130,20),_IpAddressStatusCorNetFaultManagementHost_Type())
ipAddressStatusCorNetFaultManagementHost.setMaxAccess(_H)
if mibBuilder.loadTexts:ipAddressStatusCorNetFaultManagementHost.setStatus(_A)
class _IpAddressStatusCorNetFaultManagementTrapPort_Type(MxIpPort):defaultValue=162
_IpAddressStatusCorNetFaultManagementTrapPort_Type.__name__=_L
_IpAddressStatusCorNetFaultManagementTrapPort_Object=MibScalar
ipAddressStatusCorNetFaultManagementTrapPort=_IpAddressStatusCorNetFaultManagementTrapPort_Object((1,3,6,1,4,1,4935,10,1,130,30),_IpAddressStatusCorNetFaultManagementTrapPort_Type())
ipAddressStatusCorNetFaultManagementTrapPort.setMaxAccess(_H)
if mibBuilder.loadTexts:ipAddressStatusCorNetFaultManagementTrapPort.setStatus(_A)
_CorNetFaultManagementStatus_ObjectIdentity=ObjectIdentity
corNetFaultManagementStatus=_CorNetFaultManagementStatus_ObjectIdentity((1,3,6,1,4,1,4935,10,80))
class _CorNetFaultManagementPacketsLostStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_R,0),('error',1)))
_CorNetFaultManagementPacketsLostStatus_Type.__name__=_I
_CorNetFaultManagementPacketsLostStatus_Object=MibScalar
corNetFaultManagementPacketsLostStatus=_CorNetFaultManagementPacketsLostStatus_Object((1,3,6,1,4,1,4935,10,80,5),_CorNetFaultManagementPacketsLostStatus_Type())
corNetFaultManagementPacketsLostStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:corNetFaultManagementPacketsLostStatus.setStatus(_A)
class _CorNetFaultManagementJitterBufferStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_R,0),('overrun',1),('underrun',2)))
_CorNetFaultManagementJitterBufferStatus_Type.__name__=_I
_CorNetFaultManagementJitterBufferStatus_Object=MibScalar
corNetFaultManagementJitterBufferStatus=_CorNetFaultManagementJitterBufferStatus_Object((1,3,6,1,4,1,4935,10,80,10),_CorNetFaultManagementJitterBufferStatus_Type())
corNetFaultManagementJitterBufferStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:corNetFaultManagementJitterBufferStatus.setStatus(_A)
_IpAddressConfigCorNetPbxIfTable_Object=MibTable
ipAddressConfigCorNetPbxIfTable=_IpAddressConfigCorNetPbxIfTable_Object((1,3,6,1,4,1,4935,15,1,130,10,10))
if mibBuilder.loadTexts:ipAddressConfigCorNetPbxIfTable.setStatus(_A)
_IpAddressConfigCorNetPbxIfEntry_Object=MibTableRow
ipAddressConfigCorNetPbxIfEntry=_IpAddressConfigCorNetPbxIfEntry_Object((1,3,6,1,4,1,4935,15,1,130,10,10,1))
ipAddressConfigCorNetPbxIfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ipAddressConfigCorNetPbxIfEntry.setStatus(_A)
class _IpAddressConfigCorNetPbxHost_Type(MxIpHostName):defaultValue=OctetString('')
_IpAddressConfigCorNetPbxHost_Type.__name__=_K
_IpAddressConfigCorNetPbxHost_Object=MibTableColumn
ipAddressConfigCorNetPbxHost=_IpAddressConfigCorNetPbxHost_Object((1,3,6,1,4,1,4935,15,1,130,10,10,1,10),_IpAddressConfigCorNetPbxHost_Type())
ipAddressConfigCorNetPbxHost.setMaxAccess(_C)
if mibBuilder.loadTexts:ipAddressConfigCorNetPbxHost.setStatus(_A)
class _IpAddressConfigCorNetPbxPort_Type(MxIpPort):defaultValue=4060
_IpAddressConfigCorNetPbxPort_Type.__name__=_L
_IpAddressConfigCorNetPbxPort_Object=MibTableColumn
ipAddressConfigCorNetPbxPort=_IpAddressConfigCorNetPbxPort_Object((1,3,6,1,4,1,4935,15,1,130,10,10,1,20),_IpAddressConfigCorNetPbxPort_Type())
ipAddressConfigCorNetPbxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ipAddressConfigCorNetPbxPort.setStatus(_A)
class _IpAddressConfigCorNetFaultManagementHost_Type(MxIpHostName):defaultValue=OctetString('')
_IpAddressConfigCorNetFaultManagementHost_Type.__name__=_K
_IpAddressConfigCorNetFaultManagementHost_Object=MibScalar
ipAddressConfigCorNetFaultManagementHost=_IpAddressConfigCorNetFaultManagementHost_Object((1,3,6,1,4,1,4935,15,1,130,10,20),_IpAddressConfigCorNetFaultManagementHost_Type())
ipAddressConfigCorNetFaultManagementHost.setMaxAccess(_C)
if mibBuilder.loadTexts:ipAddressConfigCorNetFaultManagementHost.setStatus(_A)
class _IpAddressConfigCorNetFaultManagementTrapPort_Type(MxIpPort):defaultValue=162
_IpAddressConfigCorNetFaultManagementTrapPort_Type.__name__=_L
_IpAddressConfigCorNetFaultManagementTrapPort_Object=MibScalar
ipAddressConfigCorNetFaultManagementTrapPort=_IpAddressConfigCorNetFaultManagementTrapPort_Object((1,3,6,1,4,1,4935,15,1,130,10,30),_IpAddressConfigCorNetFaultManagementTrapPort_Type())
ipAddressConfigCorNetFaultManagementTrapPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ipAddressConfigCorNetFaultManagementTrapPort.setStatus(_A)
_CorNetSystemMIBObjects_ObjectIdentity=ObjectIdentity
corNetSystemMIBObjects=_CorNetSystemMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,20,40,1,1))
_CorNetSystemRegistration_ObjectIdentity=ObjectIdentity
corNetSystemRegistration=_CorNetSystemRegistration_ObjectIdentity((1,3,6,1,4,1,4935,20,40,1,1,10))
_CorNetSystemRegistrationIfTable_Object=MibTable
corNetSystemRegistrationIfTable=_CorNetSystemRegistrationIfTable_Object((1,3,6,1,4,1,4935,20,40,1,1,10,10))
if mibBuilder.loadTexts:corNetSystemRegistrationIfTable.setStatus(_A)
_CorNetSystemRegistrationIfEntry_Object=MibTableRow
corNetSystemRegistrationIfEntry=_CorNetSystemRegistrationIfEntry_Object((1,3,6,1,4,1,4935,20,40,1,1,10,10,1))
corNetSystemRegistrationIfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:corNetSystemRegistrationIfEntry.setStatus(_A)
class _CorNetSystemRegSubscriberNumber_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CorNetSystemRegSubscriberNumber_Type.__name__=_E
_CorNetSystemRegSubscriberNumber_Object=MibTableColumn
corNetSystemRegSubscriberNumber=_CorNetSystemRegSubscriberNumber_Object((1,3,6,1,4,1,4935,20,40,1,1,10,10,1,10),_CorNetSystemRegSubscriberNumber_Type())
corNetSystemRegSubscriberNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemRegSubscriberNumber.setStatus(_A)
class _CorNetSystemRegLocationIdentifierNumber_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CorNetSystemRegLocationIdentifierNumber_Type.__name__=_E
_CorNetSystemRegLocationIdentifierNumber_Object=MibTableColumn
corNetSystemRegLocationIdentifierNumber=_CorNetSystemRegLocationIdentifierNumber_Object((1,3,6,1,4,1,4935,20,40,1,1,10,10,1,20),_CorNetSystemRegLocationIdentifierNumber_Type())
corNetSystemRegLocationIdentifierNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemRegLocationIdentifierNumber.setStatus(_A)
_CorNetSystemInitialization_ObjectIdentity=ObjectIdentity
corNetSystemInitialization=_CorNetSystemInitialization_ObjectIdentity((1,3,6,1,4,1,4935,20,40,1,1,20))
_CorNetSystemInitializationIfTable_Object=MibTable
corNetSystemInitializationIfTable=_CorNetSystemInitializationIfTable_Object((1,3,6,1,4,1,4935,20,40,1,1,20,10))
if mibBuilder.loadTexts:corNetSystemInitializationIfTable.setStatus(_A)
_CorNetSystemInitializationIfEntry_Object=MibTableRow
corNetSystemInitializationIfEntry=_CorNetSystemInitializationIfEntry_Object((1,3,6,1,4,1,4935,20,40,1,1,20,10,1))
corNetSystemInitializationIfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:corNetSystemInitializationIfEntry.setStatus(_A)
class _CorNetSystemInitEmergencyNumber_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CorNetSystemInitEmergencyNumber_Type.__name__=_E
_CorNetSystemInitEmergencyNumber_Object=MibTableColumn
corNetSystemInitEmergencyNumber=_CorNetSystemInitEmergencyNumber_Object((1,3,6,1,4,1,4935,20,40,1,1,20,10,1,10),_CorNetSystemInitEmergencyNumber_Type())
corNetSystemInitEmergencyNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemInitEmergencyNumber.setStatus(_A)
_CorNetSystemSecurity_ObjectIdentity=ObjectIdentity
corNetSystemSecurity=_CorNetSystemSecurity_ObjectIdentity((1,3,6,1,4,1,4935,20,40,1,1,25))
_CorNetSystemSecurityIfTable_Object=MibTable
corNetSystemSecurityIfTable=_CorNetSystemSecurityIfTable_Object((1,3,6,1,4,1,4935,20,40,1,1,25,10))
if mibBuilder.loadTexts:corNetSystemSecurityIfTable.setStatus(_A)
_CorNetSystemSecurityIfEntry_Object=MibTableRow
corNetSystemSecurityIfEntry=_CorNetSystemSecurityIfEntry_Object((1,3,6,1,4,1,4935,20,40,1,1,25,10,1))
corNetSystemSecurityIfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:corNetSystemSecurityIfEntry.setStatus(_A)
class _CorNetSystemSecurityPassword_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CorNetSystemSecurityPassword_Type.__name__=_E
_CorNetSystemSecurityPassword_Object=MibTableColumn
corNetSystemSecurityPassword=_CorNetSystemSecurityPassword_Object((1,3,6,1,4,1,4935,20,40,1,1,25,10,1,10),_CorNetSystemSecurityPassword_Type())
corNetSystemSecurityPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemSecurityPassword.setStatus(_A)
class _CorNetSystemSecurityLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('reduced',1),('full',2)))
_CorNetSystemSecurityLevel_Type.__name__=_I
_CorNetSystemSecurityLevel_Object=MibTableColumn
corNetSystemSecurityLevel=_CorNetSystemSecurityLevel_Object((1,3,6,1,4,1,4935,20,40,1,1,25,10,1,50),_CorNetSystemSecurityLevel_Type())
corNetSystemSecurityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemSecurityLevel.setStatus(_A)
_CorNetSystemFaultManagement_ObjectIdentity=ObjectIdentity
corNetSystemFaultManagement=_CorNetSystemFaultManagement_ObjectIdentity((1,3,6,1,4,1,4935,20,40,1,1,30))
class _CorNetSystemFaultManagementTrapsEnable_Type(MxEnableState):defaultValue=1
_CorNetSystemFaultManagementTrapsEnable_Type.__name__=_J
_CorNetSystemFaultManagementTrapsEnable_Object=MibScalar
corNetSystemFaultManagementTrapsEnable=_CorNetSystemFaultManagementTrapsEnable_Object((1,3,6,1,4,1,4935,20,40,1,1,30,10),_CorNetSystemFaultManagementTrapsEnable_Type())
corNetSystemFaultManagementTrapsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemFaultManagementTrapsEnable.setStatus(_A)
class _CorNetSystemFaultManagementTrapsComputePeriod_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_CorNetSystemFaultManagementTrapsComputePeriod_Type.__name__=_D
_CorNetSystemFaultManagementTrapsComputePeriod_Object=MibScalar
corNetSystemFaultManagementTrapsComputePeriod=_CorNetSystemFaultManagementTrapsComputePeriod_Object((1,3,6,1,4,1,4935,20,40,1,1,30,20),_CorNetSystemFaultManagementTrapsComputePeriod_Type())
corNetSystemFaultManagementTrapsComputePeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemFaultManagementTrapsComputePeriod.setStatus(_A)
class _CorNetSystemFaultManagementTrapsReportDelay_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CorNetSystemFaultManagementTrapsReportDelay_Type.__name__=_D
_CorNetSystemFaultManagementTrapsReportDelay_Object=MibScalar
corNetSystemFaultManagementTrapsReportDelay=_CorNetSystemFaultManagementTrapsReportDelay_Object((1,3,6,1,4,1,4935,20,40,1,1,30,30),_CorNetSystemFaultManagementTrapsReportDelay_Type())
corNetSystemFaultManagementTrapsReportDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemFaultManagementTrapsReportDelay.setStatus(_A)
class _CorNetSystemFaultManagementTrapsMaximumPacketsLostRatio_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CorNetSystemFaultManagementTrapsMaximumPacketsLostRatio_Type.__name__=_D
_CorNetSystemFaultManagementTrapsMaximumPacketsLostRatio_Object=MibScalar
corNetSystemFaultManagementTrapsMaximumPacketsLostRatio=_CorNetSystemFaultManagementTrapsMaximumPacketsLostRatio_Object((1,3,6,1,4,1,4935,20,40,1,1,30,40),_CorNetSystemFaultManagementTrapsMaximumPacketsLostRatio_Type())
corNetSystemFaultManagementTrapsMaximumPacketsLostRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemFaultManagementTrapsMaximumPacketsLostRatio.setStatus(_A)
class _CorNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CorNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio_Type.__name__=_D
_CorNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio_Object=MibScalar
corNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio=_CorNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio_Object((1,3,6,1,4,1,4935,20,40,1,1,30,50),_CorNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio_Type())
corNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio.setStatus(_A)
class _CorNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CorNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio_Type.__name__=_D
_CorNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio_Object=MibScalar
corNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio=_CorNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio_Object((1,3,6,1,4,1,4935,20,40,1,1,30,60),_CorNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio_Type())
corNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio.setStatus(_A)
_CorNetSystemData_ObjectIdentity=ObjectIdentity
corNetSystemData=_CorNetSystemData_ObjectIdentity((1,3,6,1,4,1,4935,20,40,1,1,50))
_CorNetSystemDataIfTable_Object=MibTable
corNetSystemDataIfTable=_CorNetSystemDataIfTable_Object((1,3,6,1,4,1,4935,20,40,1,1,50,10))
if mibBuilder.loadTexts:corNetSystemDataIfTable.setStatus(_A)
_CorNetSystemDataIfEntry_Object=MibTableRow
corNetSystemDataIfEntry=_CorNetSystemDataIfEntry_Object((1,3,6,1,4,1,4935,20,40,1,1,50,10,1))
corNetSystemDataIfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:corNetSystemDataIfEntry.setStatus(_A)
class _CorNetSystemDataRfc2198RedundancyLevel_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_CorNetSystemDataRfc2198RedundancyLevel_Type.__name__=_D
_CorNetSystemDataRfc2198RedundancyLevel_Object=MibTableColumn
corNetSystemDataRfc2198RedundancyLevel=_CorNetSystemDataRfc2198RedundancyLevel_Object((1,3,6,1,4,1,4935,20,40,1,1,50,10,1,50),_CorNetSystemDataRfc2198RedundancyLevel_Type())
corNetSystemDataRfc2198RedundancyLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemDataRfc2198RedundancyLevel.setStatus(_A)
class _CorNetSystemDataRfc2198DefaultPayloadType_Type(Unsigned32):defaultValue=99;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_CorNetSystemDataRfc2198DefaultPayloadType_Type.__name__=_D
_CorNetSystemDataRfc2198DefaultPayloadType_Object=MibTableColumn
corNetSystemDataRfc2198DefaultPayloadType=_CorNetSystemDataRfc2198DefaultPayloadType_Object((1,3,6,1,4,1,4935,20,40,1,1,50,10,1,70),_CorNetSystemDataRfc2198DefaultPayloadType_Type())
corNetSystemDataRfc2198DefaultPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemDataRfc2198DefaultPayloadType.setStatus(_A)
class _CorNetSystemDataRfc2833DefaultPayloadType_Type(Unsigned32):defaultValue=98;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_CorNetSystemDataRfc2833DefaultPayloadType_Type.__name__=_D
_CorNetSystemDataRfc2833DefaultPayloadType_Object=MibTableColumn
corNetSystemDataRfc2833DefaultPayloadType=_CorNetSystemDataRfc2833DefaultPayloadType_Object((1,3,6,1,4,1,4935,20,40,1,1,50,10,1,90),_CorNetSystemDataRfc2833DefaultPayloadType_Type())
corNetSystemDataRfc2833DefaultPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemDataRfc2833DefaultPayloadType.setStatus(_A)
class _CorNetSystemDataVoiceOnlyModeEnable_Type(MxEnableState):defaultValue=0
_CorNetSystemDataVoiceOnlyModeEnable_Type.__name__=_J
_CorNetSystemDataVoiceOnlyModeEnable_Object=MibTableColumn
corNetSystemDataVoiceOnlyModeEnable=_CorNetSystemDataVoiceOnlyModeEnable_Object((1,3,6,1,4,1,4935,20,40,1,1,50,10,1,150),_CorNetSystemDataVoiceOnlyModeEnable_Type())
corNetSystemDataVoiceOnlyModeEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemDataVoiceOnlyModeEnable.setStatus(_A)
_CorNetSystemServices_ObjectIdentity=ObjectIdentity
corNetSystemServices=_CorNetSystemServices_ObjectIdentity((1,3,6,1,4,1,4935,20,40,1,1,100))
_CorNetSystemServicesTable_Object=MibTable
corNetSystemServicesTable=_CorNetSystemServicesTable_Object((1,3,6,1,4,1,4935,20,40,1,1,100,100))
if mibBuilder.loadTexts:corNetSystemServicesTable.setStatus(_A)
_CorNetSystemServicesEntry_Object=MibTableRow
corNetSystemServicesEntry=_CorNetSystemServicesEntry_Object((1,3,6,1,4,1,4935,20,40,1,1,100,100,1))
corNetSystemServicesEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:corNetSystemServicesEntry.setStatus(_A)
class _CorNetSystemServicesIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CorNetSystemServicesIndex_Type.__name__=_D
_CorNetSystemServicesIndex_Object=MibTableColumn
corNetSystemServicesIndex=_CorNetSystemServicesIndex_Object((1,3,6,1,4,1,4935,20,40,1,1,100,100,1,5),_CorNetSystemServicesIndex_Type())
corNetSystemServicesIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:corNetSystemServicesIndex.setStatus(_A)
class _CorNetSystemServiceName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CorNetSystemServiceName_Type.__name__=_E
_CorNetSystemServiceName_Object=MibTableColumn
corNetSystemServiceName=_CorNetSystemServiceName_Object((1,3,6,1,4,1,4935,20,40,1,1,100,100,1,10),_CorNetSystemServiceName_Type())
corNetSystemServiceName.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemServiceName.setStatus(_A)
class _CorNetSystemServiceEnable_Type(MxEnableState):defaultValue=0
_CorNetSystemServiceEnable_Type.__name__=_J
_CorNetSystemServiceEnable_Object=MibTableColumn
corNetSystemServiceEnable=_CorNetSystemServiceEnable_Object((1,3,6,1,4,1,4935,20,40,1,1,100,100,1,15),_CorNetSystemServiceEnable_Type())
corNetSystemServiceEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemServiceEnable.setStatus(_A)
class _CorNetSystemServiceKbKeyCode_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CorNetSystemServiceKbKeyCode_Type.__name__=_D
_CorNetSystemServiceKbKeyCode_Object=MibTableColumn
corNetSystemServiceKbKeyCode=_CorNetSystemServiceKbKeyCode_Object((1,3,6,1,4,1,4935,20,40,1,1,100,100,1,20),_CorNetSystemServiceKbKeyCode_Type())
corNetSystemServiceKbKeyCode.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemServiceKbKeyCode.setStatus(_A)
class _CorNetSystemServiceActivationSequence_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_CorNetSystemServiceActivationSequence_Type.__name__=_E
_CorNetSystemServiceActivationSequence_Object=MibTableColumn
corNetSystemServiceActivationSequence=_CorNetSystemServiceActivationSequence_Object((1,3,6,1,4,1,4935,20,40,1,1,100,100,1,25),_CorNetSystemServiceActivationSequence_Type())
corNetSystemServiceActivationSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemServiceActivationSequence.setStatus(_A)
class _CorNetSystemService2StageFlag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_CorNetSystemService2StageFlag_Type.__name__=_I
_CorNetSystemService2StageFlag_Object=MibTableColumn
corNetSystemService2StageFlag=_CorNetSystemService2StageFlag_Object((1,3,6,1,4,1,4935,20,40,1,1,100,100,1,30),_CorNetSystemService2StageFlag_Type())
corNetSystemService2StageFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemService2StageFlag.setStatus(_A)
class _CorNetSystemServiceFirstDigitTimer_Type(Unsigned32):defaultValue=20000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,180000))
_CorNetSystemServiceFirstDigitTimer_Type.__name__=_D
_CorNetSystemServiceFirstDigitTimer_Object=MibTableColumn
corNetSystemServiceFirstDigitTimer=_CorNetSystemServiceFirstDigitTimer_Object((1,3,6,1,4,1,4935,20,40,1,1,100,100,1,35),_CorNetSystemServiceFirstDigitTimer_Type())
corNetSystemServiceFirstDigitTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemServiceFirstDigitTimer.setStatus(_A)
class _CorNetSystemCallFeaturesEnable_Type(MxEnableState):defaultValue=0
_CorNetSystemCallFeaturesEnable_Type.__name__=_J
_CorNetSystemCallFeaturesEnable_Object=MibScalar
corNetSystemCallFeaturesEnable=_CorNetSystemCallFeaturesEnable_Object((1,3,6,1,4,1,4935,20,40,1,1,100,150),_CorNetSystemCallFeaturesEnable_Type())
corNetSystemCallFeaturesEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemCallFeaturesEnable.setStatus(_A)
class _CorNetSystemServices2StageEndingMethod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('timer',0),('endCharacter',1)))
_CorNetSystemServices2StageEndingMethod_Type.__name__=_I
_CorNetSystemServices2StageEndingMethod_Object=MibScalar
corNetSystemServices2StageEndingMethod=_CorNetSystemServices2StageEndingMethod_Object((1,3,6,1,4,1,4935,20,40,1,1,100,200),_CorNetSystemServices2StageEndingMethod_Type())
corNetSystemServices2StageEndingMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemServices2StageEndingMethod.setStatus(_A)
class _CorNetSystemServices2StageTimeout_Type(Unsigned32):defaultValue=4000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,10000))
_CorNetSystemServices2StageTimeout_Type.__name__=_D
_CorNetSystemServices2StageTimeout_Object=MibScalar
corNetSystemServices2StageTimeout=_CorNetSystemServices2StageTimeout_Object((1,3,6,1,4,1,4935,20,40,1,1,100,250),_CorNetSystemServices2StageTimeout_Type())
corNetSystemServices2StageTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemServices2StageTimeout.setStatus(_A)
class _CorNetSystemServices2StageEndKey_Type(OctetString):defaultValue=OctetString('#');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CorNetSystemServices2StageEndKey_Type.__name__=_E
_CorNetSystemServices2StageEndKey_Object=MibScalar
corNetSystemServices2StageEndKey=_CorNetSystemServices2StageEndKey_Object((1,3,6,1,4,1,4935,20,40,1,1,100,300),_CorNetSystemServices2StageEndKey_Type())
corNetSystemServices2StageEndKey.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemServices2StageEndKey.setStatus(_A)
class _CorNetSystemServicesTimeoutInterDigit_Type(Unsigned32):defaultValue=4000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,10000))
_CorNetSystemServicesTimeoutInterDigit_Type.__name__=_D
_CorNetSystemServicesTimeoutInterDigit_Object=MibScalar
corNetSystemServicesTimeoutInterDigit=_CorNetSystemServicesTimeoutInterDigit_Object((1,3,6,1,4,1,4935,20,40,1,1,100,350),_CorNetSystemServicesTimeoutInterDigit_Type())
corNetSystemServicesTimeoutInterDigit.setMaxAccess(_C)
if mibBuilder.loadTexts:corNetSystemServicesTimeoutInterDigit.setStatus(_A)
_CorNetSystemConformance_ObjectIdentity=ObjectIdentity
corNetSystemConformance=_CorNetSystemConformance_ObjectIdentity((1,3,6,1,4,1,4935,20,40,1,2))
_CorNetSystemCompliances_ObjectIdentity=ObjectIdentity
corNetSystemCompliances=_CorNetSystemCompliances_ObjectIdentity((1,3,6,1,4,1,4935,20,40,1,2,1))
_CorNetSystemGroups_ObjectIdentity=ObjectIdentity
corNetSystemGroups=_CorNetSystemGroups_ObjectIdentity((1,3,6,1,4,1,4935,20,40,1,2,2))
_CorNetSystemEvents_ObjectIdentity=ObjectIdentity
corNetSystemEvents=_CorNetSystemEvents_ObjectIdentity((1,3,6,1,4,1,4935,20,40,1,3))
_CorNetSystemFaultManagementNotifications_ObjectIdentity=ObjectIdentity
corNetSystemFaultManagementNotifications=_CorNetSystemFaultManagementNotifications_ObjectIdentity((1,3,6,1,4,1,4935,20,40,1,3,5))
corNetSystemRegistrationGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,40,1,2,2,5))
corNetSystemRegistrationGroupVer1.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:corNetSystemRegistrationGroupVer1.setStatus(_A)
corNetSystemInitializationGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,40,1,2,2,10))
corNetSystemInitializationGroupVer1.setObjects((_B,_U))
if mibBuilder.loadTexts:corNetSystemInitializationGroupVer1.setStatus(_A)
corNetSystemSecurityGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,40,1,2,2,13))
corNetSystemSecurityGroupVer1.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:corNetSystemSecurityGroupVer1.setStatus(_A)
corNetSystemFaultManagementGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,40,1,2,2,15))
corNetSystemFaultManagementGroupVer1.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_P),(_B,_Q),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:corNetSystemFaultManagementGroupVer1.setStatus(_A)
corNetSystemDataGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,40,1,2,2,50))
corNetSystemDataGroupVer1.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:corNetSystemDataGroupVer1.setStatus(_A)
corNetSystemServicesGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,40,1,2,2,100))
corNetSystemServicesGroupVer1.setObjects(*((_B,_O),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:corNetSystemServicesGroupVer1.setStatus(_A)
corNetFaultManagementRebootTrap=NotificationType((1,3,6,1,4,1,4935,20,40,1,3,5,1050))
corNetFaultManagementRebootTrap.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:corNetFaultManagementRebootTrap.setStatus(_A)
corNetFaultManagementAuthenticationFailureTrap=NotificationType((1,3,6,1,4,1,4935,20,40,1,3,5,1150))
corNetFaultManagementAuthenticationFailureTrap.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:corNetFaultManagementAuthenticationFailureTrap.setStatus(_A)
corNetFaultManagementLanTrap=NotificationType((1,3,6,1,4,1,4935,20,40,1,3,5,1250))
corNetFaultManagementLanTrap.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:corNetFaultManagementLanTrap.setStatus(_A)
corNetFaultManagementPacketsLostTrap=NotificationType((1,3,6,1,4,1,4935,20,40,1,3,5,1350))
corNetFaultManagementPacketsLostTrap.setObjects(*((_B,_M),(_B,_N),(_B,_P)))
if mibBuilder.loadTexts:corNetFaultManagementPacketsLostTrap.setStatus(_A)
corNetFaultManagementJitterBufferTrap=NotificationType((1,3,6,1,4,1,4935,20,40,1,3,5,1450))
corNetFaultManagementJitterBufferTrap.setObjects(*((_B,_M),(_B,_N),(_B,_Q)))
if mibBuilder.loadTexts:corNetFaultManagementJitterBufferTrap.setStatus(_A)
corNetSystemFaultManagementNotificationsGroupVer1=NotificationGroup((1,3,6,1,4,1,4935,20,40,1,2,2,20))
corNetSystemFaultManagementNotificationsGroupVer1.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:corNetSystemFaultManagementNotificationsGroupVer1.setStatus(_A)
corNetSystemBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,20,40,1,2,1,5))
corNetSystemBasicComplVer1.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:corNetSystemBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ipAddressStatusCorNetPbxIfTable':ipAddressStatusCorNetPbxIfTable,'ipAddressStatusCorNetPbxIfEntry':ipAddressStatusCorNetPbxIfEntry,'ipAddressStatusCorNetPbxHost':ipAddressStatusCorNetPbxHost,'ipAddressStatusCorNetPbxPort':ipAddressStatusCorNetPbxPort,_f:ipAddressStatusCorNetFaultManagementHost,_g:ipAddressStatusCorNetFaultManagementTrapPort,'corNetFaultManagementStatus':corNetFaultManagementStatus,_P:corNetFaultManagementPacketsLostStatus,_Q:corNetFaultManagementJitterBufferStatus,'ipAddressConfigCorNetPbxIfTable':ipAddressConfigCorNetPbxIfTable,'ipAddressConfigCorNetPbxIfEntry':ipAddressConfigCorNetPbxIfEntry,'ipAddressConfigCorNetPbxHost':ipAddressConfigCorNetPbxHost,'ipAddressConfigCorNetPbxPort':ipAddressConfigCorNetPbxPort,_d:ipAddressConfigCorNetFaultManagementHost,_e:ipAddressConfigCorNetFaultManagementTrapPort,'corNetSystemMIB':corNetSystemMIB,'corNetSystemMIBObjects':corNetSystemMIBObjects,'corNetSystemRegistration':corNetSystemRegistration,'corNetSystemRegistrationIfTable':corNetSystemRegistrationIfTable,'corNetSystemRegistrationIfEntry':corNetSystemRegistrationIfEntry,_S:corNetSystemRegSubscriberNumber,_T:corNetSystemRegLocationIdentifierNumber,'corNetSystemInitialization':corNetSystemInitialization,'corNetSystemInitializationIfTable':corNetSystemInitializationIfTable,'corNetSystemInitializationIfEntry':corNetSystemInitializationIfEntry,_U:corNetSystemInitEmergencyNumber,'corNetSystemSecurity':corNetSystemSecurity,'corNetSystemSecurityIfTable':corNetSystemSecurityIfTable,'corNetSystemSecurityIfEntry':corNetSystemSecurityIfEntry,_V:corNetSystemSecurityPassword,_W:corNetSystemSecurityLevel,'corNetSystemFaultManagement':corNetSystemFaultManagement,_X:corNetSystemFaultManagementTrapsEnable,_Y:corNetSystemFaultManagementTrapsComputePeriod,_Z:corNetSystemFaultManagementTrapsReportDelay,_a:corNetSystemFaultManagementTrapsMaximumPacketsLostRatio,_b:corNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio,_c:corNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio,'corNetSystemData':corNetSystemData,'corNetSystemDataIfTable':corNetSystemDataIfTable,'corNetSystemDataIfEntry':corNetSystemDataIfEntry,_h:corNetSystemDataRfc2198RedundancyLevel,_i:corNetSystemDataRfc2198DefaultPayloadType,_j:corNetSystemDataRfc2833DefaultPayloadType,_k:corNetSystemDataVoiceOnlyModeEnable,'corNetSystemServices':corNetSystemServices,'corNetSystemServicesTable':corNetSystemServicesTable,'corNetSystemServicesEntry':corNetSystemServicesEntry,_O:corNetSystemServicesIndex,_l:corNetSystemServiceName,_m:corNetSystemServiceEnable,_n:corNetSystemServiceKbKeyCode,_o:corNetSystemServiceActivationSequence,_p:corNetSystemService2StageFlag,_q:corNetSystemServiceFirstDigitTimer,_r:corNetSystemCallFeaturesEnable,_s:corNetSystemServices2StageEndingMethod,_t:corNetSystemServices2StageTimeout,_u:corNetSystemServices2StageEndKey,_v:corNetSystemServicesTimeoutInterDigit,'corNetSystemConformance':corNetSystemConformance,'corNetSystemCompliances':corNetSystemCompliances,'corNetSystemBasicComplVer1':corNetSystemBasicComplVer1,'corNetSystemGroups':corNetSystemGroups,_A1:corNetSystemRegistrationGroupVer1,_A2:corNetSystemInitializationGroupVer1,_A3:corNetSystemSecurityGroupVer1,_A4:corNetSystemFaultManagementGroupVer1,'corNetSystemFaultManagementNotificationsGroupVer1':corNetSystemFaultManagementNotificationsGroupVer1,_A5:corNetSystemDataGroupVer1,_A6:corNetSystemServicesGroupVer1,'corNetSystemEvents':corNetSystemEvents,'corNetSystemFaultManagementNotifications':corNetSystemFaultManagementNotifications,_w:corNetFaultManagementRebootTrap,_x:corNetFaultManagementAuthenticationFailureTrap,_y:corNetFaultManagementLanTrap,_z:corNetFaultManagementPacketsLostTrap,_A0:corNetFaultManagementJitterBufferTrap})