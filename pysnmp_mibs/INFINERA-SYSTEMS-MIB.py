_F='InfnSysArcBehaviour'
_E='InfnArc'
_D='DisplayString'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
infnNE,=mibBuilder.importSymbols('INFINERA-REG-MIB','infnNE')
InfnALSAdminPolicy,InfnAdminState,InfnArc,InfnCurrentDcnGatewayType,InfnEnableDisable,InfnMigrationStatus,InfnNeType,InfnPhyConnDcnGwType,InfnSysArcBehaviour,InfnSysEnableAuxTosByteAlteration,InfnSysTermLoopBackBehaviour,InfnSyslogFeature,InfnUpgradePrepStatus=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnALSAdminPolicy','InfnAdminState',_E,'InfnCurrentDcnGatewayType','InfnEnableDisable','InfnMigrationStatus','InfnNeType','InfnPhyConnDcnGwType',_F,'InfnSysEnableAuxTosByteAlteration','InfnSysTermLoopBackBehaviour','InfnSyslogFeature','InfnUpgradePrepStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
infnSystem=ModuleIdentity((1,3,6,1,4,1,21296,2,2,1,8,1))
_InfnSystemMoId_Type=DisplayString
_InfnSystemMoId_Object=MibScalar
infnSystemMoId=_InfnSystemMoId_Object((1,3,6,1,4,1,21296,2,2,1,8,1,1),_InfnSystemMoId_Type())
infnSystemMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemMoId.setStatus(_A)
class _InfnSystemLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_InfnSystemLabel_Type.__name__=_D
_InfnSystemLabel_Object=MibScalar
infnSystemLabel=_InfnSystemLabel_Object((1,3,6,1,4,1,21296,2,2,1,8,1,2),_InfnSystemLabel_Type())
infnSystemLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemLabel.setStatus(_A)
class _InfnSystemAlarmReportControl_Type(InfnArc):defaultValue=1
_InfnSystemAlarmReportControl_Type.__name__=_E
_InfnSystemAlarmReportControl_Object=MibScalar
infnSystemAlarmReportControl=_InfnSystemAlarmReportControl_Object((1,3,6,1,4,1,21296,2,2,1,8,1,3),_InfnSystemAlarmReportControl_Type())
infnSystemAlarmReportControl.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemAlarmReportControl.setStatus(_A)
_InfnSystemAlarmInhibitState_Type=InfnArc
_InfnSystemAlarmInhibitState_Object=MibScalar
infnSystemAlarmInhibitState=_InfnSystemAlarmInhibitState_Object((1,3,6,1,4,1,21296,2,2,1,8,1,4),_InfnSystemAlarmInhibitState_Type())
infnSystemAlarmInhibitState.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemAlarmInhibitState.setStatus(_A)
_InfnSystemNodeId_Type=DisplayString
_InfnSystemNodeId_Object=MibScalar
infnSystemNodeId=_InfnSystemNodeId_Object((1,3,6,1,4,1,21296,2,2,1,8,1,5),_InfnSystemNodeId_Type())
infnSystemNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemNodeId.setStatus(_A)
class _InfnSystemNeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_InfnSystemNeName_Type.__name__=_D
_InfnSystemNeName_Object=MibScalar
infnSystemNeName=_InfnSystemNeName_Object((1,3,6,1,4,1,21296,2,2,1,8,1,6),_InfnSystemNeName_Type())
infnSystemNeName.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemNeName.setStatus(_A)
_InfnSystemNeType_Type=InfnNeType
_InfnSystemNeType_Object=MibScalar
infnSystemNeType=_InfnSystemNeType_Object((1,3,6,1,4,1,21296,2,2,1,8,1,7),_InfnSystemNeType_Type())
infnSystemNeType.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemNeType.setStatus(_A)
class _InfnSystemArcBehaviour_Type(InfnSysArcBehaviour):defaultValue=2
_InfnSystemArcBehaviour_Type.__name__=_F
_InfnSystemArcBehaviour_Object=MibScalar
infnSystemArcBehaviour=_InfnSystemArcBehaviour_Object((1,3,6,1,4,1,21296,2,2,1,8,1,8),_InfnSystemArcBehaviour_Type())
infnSystemArcBehaviour.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemArcBehaviour.setStatus(_A)
class _InfnSystemLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_InfnSystemLocation_Type.__name__=_D
_InfnSystemLocation_Object=MibScalar
infnSystemLocation=_InfnSystemLocation_Object((1,3,6,1,4,1,21296,2,2,1,8,1,9),_InfnSystemLocation_Type())
infnSystemLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemLocation.setStatus(_A)
class _InfnSystemLatitude_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_InfnSystemLatitude_Type.__name__=_D
_InfnSystemLatitude_Object=MibScalar
infnSystemLatitude=_InfnSystemLatitude_Object((1,3,6,1,4,1,21296,2,2,1,8,1,10),_InfnSystemLatitude_Type())
infnSystemLatitude.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemLatitude.setStatus(_A)
class _InfnSystemLongitude_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_InfnSystemLongitude_Type.__name__=_D
_InfnSystemLongitude_Object=MibScalar
infnSystemLongitude=_InfnSystemLongitude_Object((1,3,6,1,4,1,21296,2,2,1,8,1,11),_InfnSystemLongitude_Type())
infnSystemLongitude.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemLongitude.setStatus(_A)
_InfnSystemTime_Type=DisplayString
_InfnSystemTime_Object=MibScalar
infnSystemTime=_InfnSystemTime_Object((1,3,6,1,4,1,21296,2,2,1,8,1,12),_InfnSystemTime_Type())
infnSystemTime.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemTime.setStatus(_A)
_InfnSystemTimeZoneOffset_Type=Integer32
_InfnSystemTimeZoneOffset_Object=MibScalar
infnSystemTimeZoneOffset=_InfnSystemTimeZoneOffset_Object((1,3,6,1,4,1,21296,2,2,1,8,1,13),_InfnSystemTimeZoneOffset_Type())
infnSystemTimeZoneOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemTimeZoneOffset.setStatus(_A)
_InfnSystemActiveTime_Type=DisplayString
_InfnSystemActiveTime_Object=MibScalar
infnSystemActiveTime=_InfnSystemActiveTime_Object((1,3,6,1,4,1,21296,2,2,1,8,1,14),_InfnSystemActiveTime_Type())
infnSystemActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemActiveTime.setStatus(_A)
_InfnSystemDbVer_Type=DisplayString
_InfnSystemDbVer_Object=MibScalar
infnSystemDbVer=_InfnSystemDbVer_Object((1,3,6,1,4,1,21296,2,2,1,8,1,15),_InfnSystemDbVer_Type())
infnSystemDbVer.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemDbVer.setStatus(_A)
_InfnSystemSwGenVer_Type=DisplayString
_InfnSystemSwGenVer_Object=MibScalar
infnSystemSwGenVer=_InfnSystemSwGenVer_Object((1,3,6,1,4,1,21296,2,2,1,8,1,16),_InfnSystemSwGenVer_Type())
infnSystemSwGenVer.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemSwGenVer.setStatus(_A)
_InfnSystemRouterId_Type=InetAddressIPv4
_InfnSystemRouterId_Object=MibScalar
infnSystemRouterId=_InfnSystemRouterId_Object((1,3,6,1,4,1,21296,2,2,1,8,1,17),_InfnSystemRouterId_Type())
infnSystemRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemRouterId.setStatus(_A)
_InfnSystemDcnIp_Type=InetAddressIPv4
_InfnSystemDcnIp_Object=MibScalar
infnSystemDcnIp=_InfnSystemDcnIp_Object((1,3,6,1,4,1,21296,2,2,1,8,1,18),_InfnSystemDcnIp_Type())
infnSystemDcnIp.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemDcnIp.setStatus(_A)
_InfnSystemDcnIpNetMask_Type=InetAddressIPv4
_InfnSystemDcnIpNetMask_Object=MibScalar
infnSystemDcnIpNetMask=_InfnSystemDcnIpNetMask_Object((1,3,6,1,4,1,21296,2,2,1,8,1,19),_InfnSystemDcnIpNetMask_Type())
infnSystemDcnIpNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemDcnIpNetMask.setStatus(_A)
_InfnSystemDcnDestination_Type=InetAddressIPv4
_InfnSystemDcnDestination_Object=MibScalar
infnSystemDcnDestination=_InfnSystemDcnDestination_Object((1,3,6,1,4,1,21296,2,2,1,8,1,20),_InfnSystemDcnDestination_Type())
infnSystemDcnDestination.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemDcnDestination.setStatus(_A)
_InfnSystemDcnGateway_Type=InetAddressIPv4
_InfnSystemDcnGateway_Object=MibScalar
infnSystemDcnGateway=_InfnSystemDcnGateway_Object((1,3,6,1,4,1,21296,2,2,1,8,1,21),_InfnSystemDcnGateway_Type())
infnSystemDcnGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemDcnGateway.setStatus(_A)
_InfnSystemDcnPrefixLen_Type=Integer32
_InfnSystemDcnPrefixLen_Object=MibScalar
infnSystemDcnPrefixLen=_InfnSystemDcnPrefixLen_Object((1,3,6,1,4,1,21296,2,2,1,8,1,22),_InfnSystemDcnPrefixLen_Type())
infnSystemDcnPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemDcnPrefixLen.setStatus(_A)
_InfnSystemDcnGlobalRoute_Type=TruthValue
_InfnSystemDcnGlobalRoute_Object=MibScalar
infnSystemDcnGlobalRoute=_InfnSystemDcnGlobalRoute_Object((1,3,6,1,4,1,21296,2,2,1,8,1,23),_InfnSystemDcnGlobalRoute_Type())
infnSystemDcnGlobalRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemDcnGlobalRoute.setStatus(_A)
_InfnSystemSwBuildInfo_Type=DisplayString
_InfnSystemSwBuildInfo_Object=MibScalar
infnSystemSwBuildInfo=_InfnSystemSwBuildInfo_Object((1,3,6,1,4,1,21296,2,2,1,8,1,24),_InfnSystemSwBuildInfo_Type())
infnSystemSwBuildInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemSwBuildInfo.setStatus(_A)
_InfnSystemCraftIp_Type=InetAddressIPv4
_InfnSystemCraftIp_Object=MibScalar
infnSystemCraftIp=_InfnSystemCraftIp_Object((1,3,6,1,4,1,21296,2,2,1,8,1,25),_InfnSystemCraftIp_Type())
infnSystemCraftIp.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemCraftIp.setStatus(_A)
_InfnSystemCraftIpNetMask_Type=InetAddressIPv4
_InfnSystemCraftIpNetMask_Object=MibScalar
infnSystemCraftIpNetMask=_InfnSystemCraftIpNetMask_Object((1,3,6,1,4,1,21296,2,2,1,8,1,26),_InfnSystemCraftIpNetMask_Type())
infnSystemCraftIpNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemCraftIpNetMask.setStatus(_A)
_InfnSystemCraftIPInterfaceAdministrativeState_Type=InfnAdminState
_InfnSystemCraftIPInterfaceAdministrativeState_Object=MibScalar
infnSystemCraftIPInterfaceAdministrativeState=_InfnSystemCraftIPInterfaceAdministrativeState_Object((1,3,6,1,4,1,21296,2,2,1,8,1,27),_InfnSystemCraftIPInterfaceAdministrativeState_Type())
infnSystemCraftIPInterfaceAdministrativeState.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemCraftIPInterfaceAdministrativeState.setStatus(_A)
_InfnSystemAuxIp_Type=InetAddressIPv4
_InfnSystemAuxIp_Object=MibScalar
infnSystemAuxIp=_InfnSystemAuxIp_Object((1,3,6,1,4,1,21296,2,2,1,8,1,28),_InfnSystemAuxIp_Type())
infnSystemAuxIp.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemAuxIp.setStatus(_A)
_InfnSystemAuxIpNetMask_Type=InetAddressIPv4
_InfnSystemAuxIpNetMask_Object=MibScalar
infnSystemAuxIpNetMask=_InfnSystemAuxIpNetMask_Object((1,3,6,1,4,1,21296,2,2,1,8,1,29),_InfnSystemAuxIpNetMask_Type())
infnSystemAuxIpNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemAuxIpNetMask.setStatus(_A)
_InfnSystemAuxIPInterfaceAdministrativeState_Type=InfnAdminState
_InfnSystemAuxIPInterfaceAdministrativeState_Object=MibScalar
infnSystemAuxIPInterfaceAdministrativeState=_InfnSystemAuxIPInterfaceAdministrativeState_Object((1,3,6,1,4,1,21296,2,2,1,8,1,30),_InfnSystemAuxIPInterfaceAdministrativeState_Type())
infnSystemAuxIPInterfaceAdministrativeState.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemAuxIPInterfaceAdministrativeState.setStatus(_A)
_InfnSystemDetectedSerialNumberList_Type=DisplayString
_InfnSystemDetectedSerialNumberList_Object=MibScalar
infnSystemDetectedSerialNumberList=_InfnSystemDetectedSerialNumberList_Object((1,3,6,1,4,1,21296,2,2,1,8,1,31),_InfnSystemDetectedSerialNumberList_Type())
infnSystemDetectedSerialNumberList.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemDetectedSerialNumberList.setStatus(_A)
_InfnSystemAvailPersistentSpace_Type=DisplayString
_InfnSystemAvailPersistentSpace_Object=MibScalar
infnSystemAvailPersistentSpace=_InfnSystemAvailPersistentSpace_Object((1,3,6,1,4,1,21296,2,2,1,8,1,32),_InfnSystemAvailPersistentSpace_Type())
infnSystemAvailPersistentSpace.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemAvailPersistentSpace.setStatus(_A)
if mibBuilder.loadTexts:infnSystemAvailPersistentSpace.setUnits('Bytes')
_InfnSystemTotalPersistentSpace_Type=DisplayString
_InfnSystemTotalPersistentSpace_Object=MibScalar
infnSystemTotalPersistentSpace=_InfnSystemTotalPersistentSpace_Object((1,3,6,1,4,1,21296,2,2,1,8,1,33),_InfnSystemTotalPersistentSpace_Type())
infnSystemTotalPersistentSpace.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemTotalPersistentSpace.setStatus(_A)
if mibBuilder.loadTexts:infnSystemTotalPersistentSpace.setUnits('Bytes')
_InfnSystemGatewayProxyEnabled_Type=TruthValue
_InfnSystemGatewayProxyEnabled_Object=MibScalar
infnSystemGatewayProxyEnabled=_InfnSystemGatewayProxyEnabled_Object((1,3,6,1,4,1,21296,2,2,1,8,1,34),_InfnSystemGatewayProxyEnabled_Type())
infnSystemGatewayProxyEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemGatewayProxyEnabled.setStatus(_A)
_InfnSystemPrimaryGneIp_Type=InetAddressIPv4
_InfnSystemPrimaryGneIp_Object=MibScalar
infnSystemPrimaryGneIp=_InfnSystemPrimaryGneIp_Object((1,3,6,1,4,1,21296,2,2,1,8,1,35),_InfnSystemPrimaryGneIp_Type())
infnSystemPrimaryGneIp.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemPrimaryGneIp.setStatus(_A)
_InfnSystemSecondaryGneIp_Type=InetAddressIPv4
_InfnSystemSecondaryGneIp_Object=MibScalar
infnSystemSecondaryGneIp=_InfnSystemSecondaryGneIp_Object((1,3,6,1,4,1,21296,2,2,1,8,1,36),_InfnSystemSecondaryGneIp_Type())
infnSystemSecondaryGneIp.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemSecondaryGneIp.setStatus(_A)
_InfnSystemMaxNoOfChassisSupported_Type=Integer32
_InfnSystemMaxNoOfChassisSupported_Object=MibScalar
infnSystemMaxNoOfChassisSupported=_InfnSystemMaxNoOfChassisSupported_Object((1,3,6,1,4,1,21296,2,2,1,8,1,37),_InfnSystemMaxNoOfChassisSupported_Type())
infnSystemMaxNoOfChassisSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemMaxNoOfChassisSupported.setStatus(_A)
_InfnSystemIsForcedSyncNeeded_Type=TruthValue
_InfnSystemIsForcedSyncNeeded_Object=MibScalar
infnSystemIsForcedSyncNeeded=_InfnSystemIsForcedSyncNeeded_Object((1,3,6,1,4,1,21296,2,2,1,8,1,38),_InfnSystemIsForcedSyncNeeded_Type())
infnSystemIsForcedSyncNeeded.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemIsForcedSyncNeeded.setStatus(_A)
_InfnSystemEnableAuxTosByteAlteration_Type=InfnSysEnableAuxTosByteAlteration
_InfnSystemEnableAuxTosByteAlteration_Object=MibScalar
infnSystemEnableAuxTosByteAlteration=_InfnSystemEnableAuxTosByteAlteration_Object((1,3,6,1,4,1,21296,2,2,1,8,1,39),_InfnSystemEnableAuxTosByteAlteration_Type())
infnSystemEnableAuxTosByteAlteration.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemEnableAuxTosByteAlteration.setStatus(_A)
_InfnSystemAuxPortRate_Type=Integer32
_InfnSystemAuxPortRate_Object=MibScalar
infnSystemAuxPortRate=_InfnSystemAuxPortRate_Object((1,3,6,1,4,1,21296,2,2,1,8,1,40),_InfnSystemAuxPortRate_Type())
infnSystemAuxPortRate.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemAuxPortRate.setStatus(_A)
class _InfnSystemClli_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_InfnSystemClli_Type.__name__=_D
_InfnSystemClli_Object=MibScalar
infnSystemClli=_InfnSystemClli_Object((1,3,6,1,4,1,21296,2,2,1,8,1,41),_InfnSystemClli_Type())
infnSystemClli.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemClli.setStatus(_A)
class _InfnSystemLocation2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_InfnSystemLocation2_Type.__name__=_D
_InfnSystemLocation2_Object=MibScalar
infnSystemLocation2=_InfnSystemLocation2_Object((1,3,6,1,4,1,21296,2,2,1,8,1,42),_InfnSystemLocation2_Type())
infnSystemLocation2.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemLocation2.setStatus(_A)
_InfnSystemCliPortId_Type=Integer32
_InfnSystemCliPortId_Object=MibScalar
infnSystemCliPortId=_InfnSystemCliPortId_Object((1,3,6,1,4,1,21296,2,2,1,8,1,43),_InfnSystemCliPortId_Type())
infnSystemCliPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemCliPortId.setStatus(_A)
_InfnSystemLayer2Enabled_Type=TruthValue
_InfnSystemLayer2Enabled_Object=MibScalar
infnSystemLayer2Enabled=_InfnSystemLayer2Enabled_Object((1,3,6,1,4,1,21296,2,2,1,8,1,44),_InfnSystemLayer2Enabled_Type())
infnSystemLayer2Enabled.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemLayer2Enabled.setStatus(_A)
_InfnSystemSecondaryDcnIp_Type=InetAddressIPv4
_InfnSystemSecondaryDcnIp_Object=MibScalar
infnSystemSecondaryDcnIp=_InfnSystemSecondaryDcnIp_Object((1,3,6,1,4,1,21296,2,2,1,8,1,45),_InfnSystemSecondaryDcnIp_Type())
infnSystemSecondaryDcnIp.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemSecondaryDcnIp.setStatus(_A)
_InfnSystemSecondaryDcnIpNetMask_Type=InetAddressIPv4
_InfnSystemSecondaryDcnIpNetMask_Object=MibScalar
infnSystemSecondaryDcnIpNetMask=_InfnSystemSecondaryDcnIpNetMask_Object((1,3,6,1,4,1,21296,2,2,1,8,1,46),_InfnSystemSecondaryDcnIpNetMask_Type())
infnSystemSecondaryDcnIpNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemSecondaryDcnIpNetMask.setStatus(_A)
_InfnSystemSecondaryDcnGateway_Type=InetAddressIPv4
_InfnSystemSecondaryDcnGateway_Object=MibScalar
infnSystemSecondaryDcnGateway=_InfnSystemSecondaryDcnGateway_Object((1,3,6,1,4,1,21296,2,2,1,8,1,47),_InfnSystemSecondaryDcnGateway_Type())
infnSystemSecondaryDcnGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemSecondaryDcnGateway.setStatus(_A)
_InfnSystemCurrentDcnGateway_Type=InfnCurrentDcnGatewayType
_InfnSystemCurrentDcnGateway_Object=MibScalar
infnSystemCurrentDcnGateway=_InfnSystemCurrentDcnGateway_Object((1,3,6,1,4,1,21296,2,2,1,8,1,48),_InfnSystemCurrentDcnGateway_Type())
infnSystemCurrentDcnGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemCurrentDcnGateway.setStatus(_A)
_InfnSystemPhyConnDcnGw_Type=InfnPhyConnDcnGwType
_InfnSystemPhyConnDcnGw_Object=MibScalar
infnSystemPhyConnDcnGw=_InfnSystemPhyConnDcnGw_Object((1,3,6,1,4,1,21296,2,2,1,8,1,49),_InfnSystemPhyConnDcnGw_Type())
infnSystemPhyConnDcnGw.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemPhyConnDcnGw.setStatus(_A)
_InfnSystemTermLoopBackBehaviour_Type=InfnSysTermLoopBackBehaviour
_InfnSystemTermLoopBackBehaviour_Object=MibScalar
infnSystemTermLoopBackBehaviour=_InfnSystemTermLoopBackBehaviour_Object((1,3,6,1,4,1,21296,2,2,1,8,1,50),_InfnSystemTermLoopBackBehaviour_Type())
infnSystemTermLoopBackBehaviour.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemTermLoopBackBehaviour.setStatus(_A)
class _InfnSystemOscOobEnable_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_InfnSystemOscOobEnable_Type.__name__=_D
_InfnSystemOscOobEnable_Object=MibScalar
infnSystemOscOobEnable=_InfnSystemOscOobEnable_Object((1,3,6,1,4,1,21296,2,2,1,8,1,51),_InfnSystemOscOobEnable_Type())
infnSystemOscOobEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemOscOobEnable.setStatus(_A)
_InfnLastUpgradeTime_Type=DisplayString
_InfnLastUpgradeTime_Object=MibScalar
infnLastUpgradeTime=_InfnLastUpgradeTime_Object((1,3,6,1,4,1,21296,2,2,1,8,1,52),_InfnLastUpgradeTime_Type())
infnLastUpgradeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:infnLastUpgradeTime.setStatus(_A)
_InfnRestHoldOffTimer0_Type=Integer32
_InfnRestHoldOffTimer0_Object=MibScalar
infnRestHoldOffTimer0=_InfnRestHoldOffTimer0_Object((1,3,6,1,4,1,21296,2,2,1,8,1,53),_InfnRestHoldOffTimer0_Type())
infnRestHoldOffTimer0.setMaxAccess(_B)
if mibBuilder.loadTexts:infnRestHoldOffTimer0.setStatus(_A)
_InfnRestHoldOffTimer1_Type=Integer32
_InfnRestHoldOffTimer1_Object=MibScalar
infnRestHoldOffTimer1=_InfnRestHoldOffTimer1_Object((1,3,6,1,4,1,21296,2,2,1,8,1,54),_InfnRestHoldOffTimer1_Type())
infnRestHoldOffTimer1.setMaxAccess(_B)
if mibBuilder.loadTexts:infnRestHoldOffTimer1.setStatus(_A)
_InfnRestHoldOffTimer2_Type=Integer32
_InfnRestHoldOffTimer2_Object=MibScalar
infnRestHoldOffTimer2=_InfnRestHoldOffTimer2_Object((1,3,6,1,4,1,21296,2,2,1,8,1,55),_InfnRestHoldOffTimer2_Type())
infnRestHoldOffTimer2.setMaxAccess(_B)
if mibBuilder.loadTexts:infnRestHoldOffTimer2.setStatus(_A)
_InfnRestHoldOffTimer3_Type=Integer32
_InfnRestHoldOffTimer3_Object=MibScalar
infnRestHoldOffTimer3=_InfnRestHoldOffTimer3_Object((1,3,6,1,4,1,21296,2,2,1,8,1,56),_InfnRestHoldOffTimer3_Type())
infnRestHoldOffTimer3.setMaxAccess(_B)
if mibBuilder.loadTexts:infnRestHoldOffTimer3.setStatus(_A)
_InfnRestHoldOffTimer4_Type=Integer32
_InfnRestHoldOffTimer4_Object=MibScalar
infnRestHoldOffTimer4=_InfnRestHoldOffTimer4_Object((1,3,6,1,4,1,21296,2,2,1,8,1,57),_InfnRestHoldOffTimer4_Type())
infnRestHoldOffTimer4.setMaxAccess(_B)
if mibBuilder.loadTexts:infnRestHoldOffTimer4.setStatus(_A)
_InfnRestHoldOffTimer5_Type=Integer32
_InfnRestHoldOffTimer5_Object=MibScalar
infnRestHoldOffTimer5=_InfnRestHoldOffTimer5_Object((1,3,6,1,4,1,21296,2,2,1,8,1,58),_InfnRestHoldOffTimer5_Type())
infnRestHoldOffTimer5.setMaxAccess(_B)
if mibBuilder.loadTexts:infnRestHoldOffTimer5.setStatus(_A)
_InfnRestHoldOffTimer6_Type=Integer32
_InfnRestHoldOffTimer6_Object=MibScalar
infnRestHoldOffTimer6=_InfnRestHoldOffTimer6_Object((1,3,6,1,4,1,21296,2,2,1,8,1,59),_InfnRestHoldOffTimer6_Type())
infnRestHoldOffTimer6.setMaxAccess(_B)
if mibBuilder.loadTexts:infnRestHoldOffTimer6.setStatus(_A)
_InfnRestHoldOffTimer7_Type=Integer32
_InfnRestHoldOffTimer7_Object=MibScalar
infnRestHoldOffTimer7=_InfnRestHoldOffTimer7_Object((1,3,6,1,4,1,21296,2,2,1,8,1,60),_InfnRestHoldOffTimer7_Type())
infnRestHoldOffTimer7.setMaxAccess(_B)
if mibBuilder.loadTexts:infnRestHoldOffTimer7.setStatus(_A)
_InfnEnhProtSw_Type=InfnEnableDisable
_InfnEnhProtSw_Object=MibScalar
infnEnhProtSw=_InfnEnhProtSw_Object((1,3,6,1,4,1,21296,2,2,1,8,1,61),_InfnEnhProtSw_Type())
infnEnhProtSw.setMaxAccess(_B)
if mibBuilder.loadTexts:infnEnhProtSw.setStatus(_A)
_InfnALSAdministrationPolicy_Type=InfnALSAdminPolicy
_InfnALSAdministrationPolicy_Object=MibScalar
infnALSAdministrationPolicy=_InfnALSAdministrationPolicy_Object((1,3,6,1,4,1,21296,2,2,1,8,1,62),_InfnALSAdministrationPolicy_Type())
infnALSAdministrationPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:infnALSAdministrationPolicy.setStatus(_A)
_InfnOpticalGmplsMscId_Type=Integer32
_InfnOpticalGmplsMscId_Object=MibScalar
infnOpticalGmplsMscId=_InfnOpticalGmplsMscId_Object((1,3,6,1,4,1,21296,2,2,1,8,1,63),_InfnOpticalGmplsMscId_Type())
infnOpticalGmplsMscId.setMaxAccess(_B)
if mibBuilder.loadTexts:infnOpticalGmplsMscId.setStatus(_A)
_InfnPrepareUpgradeStatus_Type=InfnUpgradePrepStatus
_InfnPrepareUpgradeStatus_Object=MibScalar
infnPrepareUpgradeStatus=_InfnPrepareUpgradeStatus_Object((1,3,6,1,4,1,21296,2,2,1,8,1,64),_InfnPrepareUpgradeStatus_Type())
infnPrepareUpgradeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:infnPrepareUpgradeStatus.setStatus(_A)
_InfnPreUpgradeLastAttemptedTime_Type=DisplayString
_InfnPreUpgradeLastAttemptedTime_Object=MibScalar
infnPreUpgradeLastAttemptedTime=_InfnPreUpgradeLastAttemptedTime_Object((1,3,6,1,4,1,21296,2,2,1,8,1,65),_InfnPreUpgradeLastAttemptedTime_Type())
infnPreUpgradeLastAttemptedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:infnPreUpgradeLastAttemptedTime.setStatus(_A)
_InfnPreUpgradeLastSuccessfulTime_Type=DisplayString
_InfnPreUpgradeLastSuccessfulTime_Object=MibScalar
infnPreUpgradeLastSuccessfulTime=_InfnPreUpgradeLastSuccessfulTime_Object((1,3,6,1,4,1,21296,2,2,1,8,1,66),_InfnPreUpgradeLastSuccessfulTime_Type())
infnPreUpgradeLastSuccessfulTime.setMaxAccess(_B)
if mibBuilder.loadTexts:infnPreUpgradeLastSuccessfulTime.setStatus(_A)
_InfnSystemDcnIp6_Type=InetAddressIPv6
_InfnSystemDcnIp6_Object=MibScalar
infnSystemDcnIp6=_InfnSystemDcnIp6_Object((1,3,6,1,4,1,21296,2,2,1,8,1,67),_InfnSystemDcnIp6_Type())
infnSystemDcnIp6.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemDcnIp6.setStatus(_A)
_InfnSystemDcnIpNetMask6_Type=Integer32
_InfnSystemDcnIpNetMask6_Object=MibScalar
infnSystemDcnIpNetMask6=_InfnSystemDcnIpNetMask6_Object((1,3,6,1,4,1,21296,2,2,1,8,1,68),_InfnSystemDcnIpNetMask6_Type())
infnSystemDcnIpNetMask6.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemDcnIpNetMask6.setStatus(_A)
_InfnSystemDcnDestination6_Type=InetAddressIPv6
_InfnSystemDcnDestination6_Object=MibScalar
infnSystemDcnDestination6=_InfnSystemDcnDestination6_Object((1,3,6,1,4,1,21296,2,2,1,8,1,69),_InfnSystemDcnDestination6_Type())
infnSystemDcnDestination6.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemDcnDestination6.setStatus(_A)
_InfnSystemDcnGateway6_Type=InetAddressIPv6
_InfnSystemDcnGateway6_Object=MibScalar
infnSystemDcnGateway6=_InfnSystemDcnGateway6_Object((1,3,6,1,4,1,21296,2,2,1,8,1,70),_InfnSystemDcnGateway6_Type())
infnSystemDcnGateway6.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemDcnGateway6.setStatus(_A)
_InfnSystemDcnPrefixLen6_Type=Integer32
_InfnSystemDcnPrefixLen6_Object=MibScalar
infnSystemDcnPrefixLen6=_InfnSystemDcnPrefixLen6_Object((1,3,6,1,4,1,21296,2,2,1,8,1,71),_InfnSystemDcnPrefixLen6_Type())
infnSystemDcnPrefixLen6.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemDcnPrefixLen6.setStatus(_A)
_InfnSystemCraftIp6_Type=InetAddressIPv6
_InfnSystemCraftIp6_Object=MibScalar
infnSystemCraftIp6=_InfnSystemCraftIp6_Object((1,3,6,1,4,1,21296,2,2,1,8,1,72),_InfnSystemCraftIp6_Type())
infnSystemCraftIp6.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemCraftIp6.setStatus(_A)
_InfnSystemDcnLinkLocal_Type=InetAddressIPv6
_InfnSystemDcnLinkLocal_Object=MibScalar
infnSystemDcnLinkLocal=_InfnSystemDcnLinkLocal_Object((1,3,6,1,4,1,21296,2,2,1,8,1,73),_InfnSystemDcnLinkLocal_Type())
infnSystemDcnLinkLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSystemDcnLinkLocal.setStatus(_A)
_InfnSystemMigrationStatus_Type=InfnMigrationStatus
_InfnSystemMigrationStatus_Object=MibScalar
infnSystemMigrationStatus=_InfnSystemMigrationStatus_Object((1,3,6,1,4,1,21296,2,2,1,8,1,74),_InfnSystemMigrationStatus_Type())
infnSystemMigrationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemMigrationStatus.setStatus(_A)
_InfnSystemSysLogFeature_Type=InfnSyslogFeature
_InfnSystemSysLogFeature_Object=MibScalar
infnSystemSysLogFeature=_InfnSystemSysLogFeature_Object((1,3,6,1,4,1,21296,2,2,1,8,1,75),_InfnSystemSysLogFeature_Type())
infnSystemSysLogFeature.setMaxAccess(_B)
if mibBuilder.loadTexts:infnSystemSysLogFeature.setStatus(_A)
mibBuilder.exportSymbols('INFINERA-SYSTEMS-MIB',**{'infnSystem':infnSystem,'infnSystemMoId':infnSystemMoId,'infnSystemLabel':infnSystemLabel,'infnSystemAlarmReportControl':infnSystemAlarmReportControl,'infnSystemAlarmInhibitState':infnSystemAlarmInhibitState,'infnSystemNodeId':infnSystemNodeId,'infnSystemNeName':infnSystemNeName,'infnSystemNeType':infnSystemNeType,'infnSystemArcBehaviour':infnSystemArcBehaviour,'infnSystemLocation':infnSystemLocation,'infnSystemLatitude':infnSystemLatitude,'infnSystemLongitude':infnSystemLongitude,'infnSystemTime':infnSystemTime,'infnSystemTimeZoneOffset':infnSystemTimeZoneOffset,'infnSystemActiveTime':infnSystemActiveTime,'infnSystemDbVer':infnSystemDbVer,'infnSystemSwGenVer':infnSystemSwGenVer,'infnSystemRouterId':infnSystemRouterId,'infnSystemDcnIp':infnSystemDcnIp,'infnSystemDcnIpNetMask':infnSystemDcnIpNetMask,'infnSystemDcnDestination':infnSystemDcnDestination,'infnSystemDcnGateway':infnSystemDcnGateway,'infnSystemDcnPrefixLen':infnSystemDcnPrefixLen,'infnSystemDcnGlobalRoute':infnSystemDcnGlobalRoute,'infnSystemSwBuildInfo':infnSystemSwBuildInfo,'infnSystemCraftIp':infnSystemCraftIp,'infnSystemCraftIpNetMask':infnSystemCraftIpNetMask,'infnSystemCraftIPInterfaceAdministrativeState':infnSystemCraftIPInterfaceAdministrativeState,'infnSystemAuxIp':infnSystemAuxIp,'infnSystemAuxIpNetMask':infnSystemAuxIpNetMask,'infnSystemAuxIPInterfaceAdministrativeState':infnSystemAuxIPInterfaceAdministrativeState,'infnSystemDetectedSerialNumberList':infnSystemDetectedSerialNumberList,'infnSystemAvailPersistentSpace':infnSystemAvailPersistentSpace,'infnSystemTotalPersistentSpace':infnSystemTotalPersistentSpace,'infnSystemGatewayProxyEnabled':infnSystemGatewayProxyEnabled,'infnSystemPrimaryGneIp':infnSystemPrimaryGneIp,'infnSystemSecondaryGneIp':infnSystemSecondaryGneIp,'infnSystemMaxNoOfChassisSupported':infnSystemMaxNoOfChassisSupported,'infnSystemIsForcedSyncNeeded':infnSystemIsForcedSyncNeeded,'infnSystemEnableAuxTosByteAlteration':infnSystemEnableAuxTosByteAlteration,'infnSystemAuxPortRate':infnSystemAuxPortRate,'infnSystemClli':infnSystemClli,'infnSystemLocation2':infnSystemLocation2,'infnSystemCliPortId':infnSystemCliPortId,'infnSystemLayer2Enabled':infnSystemLayer2Enabled,'infnSystemSecondaryDcnIp':infnSystemSecondaryDcnIp,'infnSystemSecondaryDcnIpNetMask':infnSystemSecondaryDcnIpNetMask,'infnSystemSecondaryDcnGateway':infnSystemSecondaryDcnGateway,'infnSystemCurrentDcnGateway':infnSystemCurrentDcnGateway,'infnSystemPhyConnDcnGw':infnSystemPhyConnDcnGw,'infnSystemTermLoopBackBehaviour':infnSystemTermLoopBackBehaviour,'infnSystemOscOobEnable':infnSystemOscOobEnable,'infnLastUpgradeTime':infnLastUpgradeTime,'infnRestHoldOffTimer0':infnRestHoldOffTimer0,'infnRestHoldOffTimer1':infnRestHoldOffTimer1,'infnRestHoldOffTimer2':infnRestHoldOffTimer2,'infnRestHoldOffTimer3':infnRestHoldOffTimer3,'infnRestHoldOffTimer4':infnRestHoldOffTimer4,'infnRestHoldOffTimer5':infnRestHoldOffTimer5,'infnRestHoldOffTimer6':infnRestHoldOffTimer6,'infnRestHoldOffTimer7':infnRestHoldOffTimer7,'infnEnhProtSw':infnEnhProtSw,'infnALSAdministrationPolicy':infnALSAdministrationPolicy,'infnOpticalGmplsMscId':infnOpticalGmplsMscId,'infnPrepareUpgradeStatus':infnPrepareUpgradeStatus,'infnPreUpgradeLastAttemptedTime':infnPreUpgradeLastAttemptedTime,'infnPreUpgradeLastSuccessfulTime':infnPreUpgradeLastSuccessfulTime,'infnSystemDcnIp6':infnSystemDcnIp6,'infnSystemDcnIpNetMask6':infnSystemDcnIpNetMask6,'infnSystemDcnDestination6':infnSystemDcnDestination6,'infnSystemDcnGateway6':infnSystemDcnGateway6,'infnSystemDcnPrefixLen6':infnSystemDcnPrefixLen6,'infnSystemCraftIp6':infnSystemCraftIp6,'infnSystemDcnLinkLocal':infnSystemDcnLinkLocal,'infnSystemMigrationStatus':infnSystemMigrationStatus,'infnSystemSysLogFeature':infnSystemSysLogFeature})