_Q='sfpsATMSvcHistoryEventIndex'
_P='sfpsATMPortsPhysIntf'
_O='sfpsAnibIfoStatsPhysIntf'
_N='sfpsATMLecPortLogPort'
_M='sfpsVccPortLogPort'
_L='sfpsPoolTableIndex'
_K='sfpsSysStatsSwitchInstance'
_J='sfpsSysConfigSwitchInstance'
_I='reset'
_H='enabled'
_G='disabled'
_F='CTRON-SFPS-ESYS-MIB'
_E='other'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsATMAnibIfoStats,sfpsATMElan,sfpsATMPorts,sfpsATMPortsMgr,sfpsATMResolver,sfpsATMResolverCounters,sfpsATMSvcHistoryEvent,sfpsATMSvcHistoryMgr,sfpsMemHeapStats,sfpsSystemConfig,sfpsSystemPool,sfpsSystemStats=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsATMAnibIfoStats','sfpsATMElan','sfpsATMPorts','sfpsATMPortsMgr','sfpsATMResolver','sfpsATMResolverCounters','sfpsATMSvcHistoryEvent','sfpsATMSvcHistoryMgr','sfpsMemHeapStats','sfpsSystemConfig','sfpsSystemPool','sfpsSystemStats')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class HexInteger(Integer32):0
class SfpsSwitchInstance(Integer32):0
class SfpsAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SfpsSysConfigTable_Object=MibTable
sfpsSysConfigTable=_SfpsSysConfigTable_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1))
if mibBuilder.loadTexts:sfpsSysConfigTable.setStatus(_A)
_SfpsSysConfigEntry_Object=MibTableRow
sfpsSysConfigEntry=_SfpsSysConfigEntry_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1))
sfpsSysConfigEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:sfpsSysConfigEntry.setStatus(_A)
_SfpsSysConfigSwitchInstance_Type=Integer32
_SfpsSysConfigSwitchInstance_Object=MibTableColumn
sfpsSysConfigSwitchInstance=_SfpsSysConfigSwitchInstance_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,1),_SfpsSysConfigSwitchInstance_Type())
sfpsSysConfigSwitchInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysConfigSwitchInstance.setStatus(_A)
class _SfpsSysConfigAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SfpsSysConfigAdminStatus_Type.__name__=_D
_SfpsSysConfigAdminStatus_Object=MibTableColumn
sfpsSysConfigAdminStatus=_SfpsSysConfigAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,2),_SfpsSysConfigAdminStatus_Type())
sfpsSysConfigAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSysConfigAdminStatus.setStatus(_A)
class _SfpsSysConfigAdminReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_SfpsSysConfigAdminReset_Type.__name__=_D
_SfpsSysConfigAdminReset_Object=MibTableColumn
sfpsSysConfigAdminReset=_SfpsSysConfigAdminReset_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,3),_SfpsSysConfigAdminReset_Type())
sfpsSysConfigAdminReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSysConfigAdminReset.setStatus(_A)
class _SfpsSysConfigOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),('pending-disable',4),('pending-enable',5),('invalid-config',6)))
_SfpsSysConfigOperStatus_Type.__name__=_D
_SfpsSysConfigOperStatus_Object=MibTableColumn
sfpsSysConfigOperStatus=_SfpsSysConfigOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,4),_SfpsSysConfigOperStatus_Type())
sfpsSysConfigOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysConfigOperStatus.setStatus(_A)
_SfpsSysConfigOperTime_Type=TimeTicks
_SfpsSysConfigOperTime_Object=MibTableColumn
sfpsSysConfigOperTime=_SfpsSysConfigOperTime_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,5),_SfpsSysConfigOperTime_Type())
sfpsSysConfigOperTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysConfigOperTime.setStatus(_A)
_SfpsSysConfigLastChange_Type=TimeTicks
_SfpsSysConfigLastChange_Object=MibTableColumn
sfpsSysConfigLastChange=_SfpsSysConfigLastChange_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,6),_SfpsSysConfigLastChange_Type())
sfpsSysConfigLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysConfigLastChange.setStatus(_A)
_SfpsSysConfigVersion_Type=DisplayString
_SfpsSysConfigVersion_Object=MibTableColumn
sfpsSysConfigVersion=_SfpsSysConfigVersion_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,7),_SfpsSysConfigVersion_Type())
sfpsSysConfigVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysConfigVersion.setStatus(_A)
_SfpsSysConfigMIBRev_Type=DisplayString
_SfpsSysConfigMIBRev_Object=MibTableColumn
sfpsSysConfigMIBRev=_SfpsSysConfigMIBRev_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,8),_SfpsSysConfigMIBRev_Type())
sfpsSysConfigMIBRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysConfigMIBRev.setStatus(_A)
_SfpsSysConfigHostMgmtPort_Type=Integer32
_SfpsSysConfigHostMgmtPort_Object=MibTableColumn
sfpsSysConfigHostMgmtPort=_SfpsSysConfigHostMgmtPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,9),_SfpsSysConfigHostMgmtPort_Type())
sfpsSysConfigHostMgmtPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSysConfigHostMgmtPort.setStatus(_A)
_SfpsSysConfigHostCtrlPort_Type=Integer32
_SfpsSysConfigHostCtrlPort_Object=MibTableColumn
sfpsSysConfigHostCtrlPort=_SfpsSysConfigHostCtrlPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,10),_SfpsSysConfigHostCtrlPort_Type())
sfpsSysConfigHostCtrlPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysConfigHostCtrlPort.setStatus(_A)
_SfpsSysConfigHostDataPort_Type=Integer32
_SfpsSysConfigHostDataPort_Object=MibTableColumn
sfpsSysConfigHostDataPort=_SfpsSysConfigHostDataPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,11),_SfpsSysConfigHostDataPort_Type())
sfpsSysConfigHostDataPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysConfigHostDataPort.setStatus(_A)
_SfpsSysConfigHostCtrlThrottleCount_Type=Integer32
_SfpsSysConfigHostCtrlThrottleCount_Object=MibTableColumn
sfpsSysConfigHostCtrlThrottleCount=_SfpsSysConfigHostCtrlThrottleCount_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,12),_SfpsSysConfigHostCtrlThrottleCount_Type())
sfpsSysConfigHostCtrlThrottleCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysConfigHostCtrlThrottleCount.setStatus(_A)
_SfpsSysConfigHostDataThrottleCount_Type=Integer32
_SfpsSysConfigHostDataThrottleCount_Object=MibTableColumn
sfpsSysConfigHostDataThrottleCount=_SfpsSysConfigHostDataThrottleCount_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,13),_SfpsSysConfigHostDataThrottleCount_Type())
sfpsSysConfigHostDataThrottleCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysConfigHostDataThrottleCount.setStatus(_A)
_SfpsSysConfigTrunkSwitch_Type=Integer32
_SfpsSysConfigTrunkSwitch_Object=MibTableColumn
sfpsSysConfigTrunkSwitch=_SfpsSysConfigTrunkSwitch_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,14),_SfpsSysConfigTrunkSwitch_Type())
sfpsSysConfigTrunkSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSysConfigTrunkSwitch.setStatus(_A)
class _SfpsSysConfigSwitchMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('vNET',1),('vLAN',2),('aNVLLobo',3),('aNVLFrontEnd',4)))
_SfpsSysConfigSwitchMode_Type.__name__=_D
_SfpsSysConfigSwitchMode_Object=MibTableColumn
sfpsSysConfigSwitchMode=_SfpsSysConfigSwitchMode_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,20),_SfpsSysConfigSwitchMode_Type())
sfpsSysConfigSwitchMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSysConfigSwitchMode.setStatus(_A)
_SfpsSysConfigSwitchMAC_Type=SfpsAddress
_SfpsSysConfigSwitchMAC_Object=MibTableColumn
sfpsSysConfigSwitchMAC=_SfpsSysConfigSwitchMAC_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,21),_SfpsSysConfigSwitchMAC_Type())
sfpsSysConfigSwitchMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysConfigSwitchMAC.setStatus(_A)
class _SfpsSysConfigMgmtAccessType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mgmt-Only',1),('mgmt-and-Access',2)))
_SfpsSysConfigMgmtAccessType_Type.__name__=_D
_SfpsSysConfigMgmtAccessType_Object=MibTableColumn
sfpsSysConfigMgmtAccessType=_SfpsSysConfigMgmtAccessType_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,22),_SfpsSysConfigMgmtAccessType_Type())
sfpsSysConfigMgmtAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSysConfigMgmtAccessType.setStatus(_A)
_SfpsSysConfigChassisMAC_Type=SfpsAddress
_SfpsSysConfigChassisMAC_Object=MibTableColumn
sfpsSysConfigChassisMAC=_SfpsSysConfigChassisMAC_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,23),_SfpsSysConfigChassisMAC_Type())
sfpsSysConfigChassisMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysConfigChassisMAC.setStatus(_A)
_SfpsSysConfigChassisIP_Type=IpAddress
_SfpsSysConfigChassisIP_Object=MibTableColumn
sfpsSysConfigChassisIP=_SfpsSysConfigChassisIP_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,1,1,1,24),_SfpsSysConfigChassisIP_Type())
sfpsSysConfigChassisIP.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysConfigChassisIP.setStatus(_A)
_SfpsSysStatsTable_Object=MibTable
sfpsSysStatsTable=_SfpsSysStatsTable_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,1))
if mibBuilder.loadTexts:sfpsSysStatsTable.setStatus(_A)
_SfpsSysStatsEntry_Object=MibTableRow
sfpsSysStatsEntry=_SfpsSysStatsEntry_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,1,1))
sfpsSysStatsEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:sfpsSysStatsEntry.setStatus(_A)
_SfpsSysStatsSwitchInstance_Type=SfpsSwitchInstance
_SfpsSysStatsSwitchInstance_Object=MibTableColumn
sfpsSysStatsSwitchInstance=_SfpsSysStatsSwitchInstance_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,1,1,1),_SfpsSysStatsSwitchInstance_Type())
sfpsSysStatsSwitchInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysStatsSwitchInstance.setStatus(_A)
class _SfpsSysStatsAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SfpsSysStatsAdminStatus_Type.__name__=_D
_SfpsSysStatsAdminStatus_Object=MibTableColumn
sfpsSysStatsAdminStatus=_SfpsSysStatsAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,1,1,2),_SfpsSysStatsAdminStatus_Type())
sfpsSysStatsAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSysStatsAdminStatus.setStatus(_A)
class _SfpsSysStatsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_SfpsSysStatsReset_Type.__name__=_D
_SfpsSysStatsReset_Object=MibTableColumn
sfpsSysStatsReset=_SfpsSysStatsReset_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,1,1,3),_SfpsSysStatsReset_Type())
sfpsSysStatsReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSysStatsReset.setStatus(_A)
_SfpsSysStatsOperTime_Type=TimeTicks
_SfpsSysStatsOperTime_Object=MibTableColumn
sfpsSysStatsOperTime=_SfpsSysStatsOperTime_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,1,1,4),_SfpsSysStatsOperTime_Type())
sfpsSysStatsOperTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysStatsOperTime.setStatus(_A)
_SfpsSysStatsInPkts_Type=Counter32
_SfpsSysStatsInPkts_Object=MibTableColumn
sfpsSysStatsInPkts=_SfpsSysStatsInPkts_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,1,1,5),_SfpsSysStatsInPkts_Type())
sfpsSysStatsInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysStatsInPkts.setStatus(_A)
_SfpsSysStatsOutPkts_Type=Counter32
_SfpsSysStatsOutPkts_Object=MibTableColumn
sfpsSysStatsOutPkts=_SfpsSysStatsOutPkts_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,1,1,6),_SfpsSysStatsOutPkts_Type())
sfpsSysStatsOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysStatsOutPkts.setStatus(_A)
_SfpsSysStatsDiscardPkts_Type=Counter32
_SfpsSysStatsDiscardPkts_Object=MibTableColumn
sfpsSysStatsDiscardPkts=_SfpsSysStatsDiscardPkts_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,1,1,7),_SfpsSysStatsDiscardPkts_Type())
sfpsSysStatsDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysStatsDiscardPkts.setStatus(_A)
_SfpsSysStatsFilteredPkts_Type=Counter32
_SfpsSysStatsFilteredPkts_Object=MibTableColumn
sfpsSysStatsFilteredPkts=_SfpsSysStatsFilteredPkts_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,1,1,8),_SfpsSysStatsFilteredPkts_Type())
sfpsSysStatsFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysStatsFilteredPkts.setStatus(_A)
_SfpsSysStatsInOctets_Type=Counter32
_SfpsSysStatsInOctets_Object=MibTableColumn
sfpsSysStatsInOctets=_SfpsSysStatsInOctets_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,1,1,9),_SfpsSysStatsInOctets_Type())
sfpsSysStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysStatsInOctets.setStatus(_A)
_SfpsSysStatsOutOctets_Type=Counter32
_SfpsSysStatsOutOctets_Object=MibTableColumn
sfpsSysStatsOutOctets=_SfpsSysStatsOutOctets_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,1,1,10),_SfpsSysStatsOutOctets_Type())
sfpsSysStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysStatsOutOctets.setStatus(_A)
_SfpsSysStatsDiscardOctets_Type=Counter32
_SfpsSysStatsDiscardOctets_Object=MibTableColumn
sfpsSysStatsDiscardOctets=_SfpsSysStatsDiscardOctets_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,1,1,11),_SfpsSysStatsDiscardOctets_Type())
sfpsSysStatsDiscardOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysStatsDiscardOctets.setStatus(_A)
_SfpsSysStatsFilteredOctets_Type=Counter32
_SfpsSysStatsFilteredOctets_Object=MibTableColumn
sfpsSysStatsFilteredOctets=_SfpsSysStatsFilteredOctets_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,1,1,12),_SfpsSysStatsFilteredOctets_Type())
sfpsSysStatsFilteredOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSysStatsFilteredOctets.setStatus(_A)
_SfpsMemHeapStatsHeapInit_Type=HexInteger
_SfpsMemHeapStatsHeapInit_Object=MibScalar
sfpsMemHeapStatsHeapInit=_SfpsMemHeapStatsHeapInit_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,2,1,1),_SfpsMemHeapStatsHeapInit_Type())
sfpsMemHeapStatsHeapInit.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMemHeapStatsHeapInit.setStatus(_A)
_SfpsMemHeapStatsHeapMax_Type=HexInteger
_SfpsMemHeapStatsHeapMax_Object=MibScalar
sfpsMemHeapStatsHeapMax=_SfpsMemHeapStatsHeapMax_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,2,1,2),_SfpsMemHeapStatsHeapMax_Type())
sfpsMemHeapStatsHeapMax.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMemHeapStatsHeapMax.setStatus(_A)
_SfpsMemHeapStatsHeapEnd_Type=HexInteger
_SfpsMemHeapStatsHeapEnd_Object=MibScalar
sfpsMemHeapStatsHeapEnd=_SfpsMemHeapStatsHeapEnd_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,2,1,3),_SfpsMemHeapStatsHeapEnd_Type())
sfpsMemHeapStatsHeapEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMemHeapStatsHeapEnd.setStatus(_A)
_SfpsMemHeapStatsHeapSize_Type=Integer32
_SfpsMemHeapStatsHeapSize_Object=MibScalar
sfpsMemHeapStatsHeapSize=_SfpsMemHeapStatsHeapSize_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,2,1,4),_SfpsMemHeapStatsHeapSize_Type())
sfpsMemHeapStatsHeapSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMemHeapStatsHeapSize.setStatus(_A)
_SfpsMemHeapStatsFragCount_Type=Integer32
_SfpsMemHeapStatsFragCount_Object=MibScalar
sfpsMemHeapStatsFragCount=_SfpsMemHeapStatsFragCount_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,2,1,5),_SfpsMemHeapStatsFragCount_Type())
sfpsMemHeapStatsFragCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMemHeapStatsFragCount.setStatus(_A)
_SfpsMemHeapStatsFragLargest_Type=Integer32
_SfpsMemHeapStatsFragLargest_Object=MibScalar
sfpsMemHeapStatsFragLargest=_SfpsMemHeapStatsFragLargest_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,2,1,6),_SfpsMemHeapStatsFragLargest_Type())
sfpsMemHeapStatsFragLargest.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMemHeapStatsFragLargest.setStatus(_A)
_SfpsMemHeapStatsFragBytes_Type=Integer32
_SfpsMemHeapStatsFragBytes_Object=MibScalar
sfpsMemHeapStatsFragBytes=_SfpsMemHeapStatsFragBytes_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,2,1,7),_SfpsMemHeapStatsFragBytes_Type())
sfpsMemHeapStatsFragBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMemHeapStatsFragBytes.setStatus(_A)
_SfpsMemHeapStatsHeapUsed_Type=Integer32
_SfpsMemHeapStatsHeapUsed_Object=MibScalar
sfpsMemHeapStatsHeapUsed=_SfpsMemHeapStatsHeapUsed_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,2,1,8),_SfpsMemHeapStatsHeapUsed_Type())
sfpsMemHeapStatsHeapUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMemHeapStatsHeapUsed.setStatus(_A)
_SfpsMemHeapStatsHeapAvail_Type=Integer32
_SfpsMemHeapStatsHeapAvail_Object=MibScalar
sfpsMemHeapStatsHeapAvail=_SfpsMemHeapStatsHeapAvail_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,2,1,9),_SfpsMemHeapStatsHeapAvail_Type())
sfpsMemHeapStatsHeapAvail.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMemHeapStatsHeapAvail.setStatus(_A)
_SfpsMemHeapStatsHeapUseMax_Type=OctetString
_SfpsMemHeapStatsHeapUseMax_Object=MibScalar
sfpsMemHeapStatsHeapUseMax=_SfpsMemHeapStatsHeapUseMax_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,2,1,10),_SfpsMemHeapStatsHeapUseMax_Type())
sfpsMemHeapStatsHeapUseMax.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMemHeapStatsHeapUseMax.setStatus(_A)
_SfpsMemHeapStatsHeapUsePercent_Type=OctetString
_SfpsMemHeapStatsHeapUsePercent_Object=MibScalar
sfpsMemHeapStatsHeapUsePercent=_SfpsMemHeapStatsHeapUsePercent_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,2,2,1,11),_SfpsMemHeapStatsHeapUsePercent_Type())
sfpsMemHeapStatsHeapUsePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMemHeapStatsHeapUsePercent.setStatus(_A)
_SfpsPoolTable_Object=MibTable
sfpsPoolTable=_SfpsPoolTable_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,4,1))
if mibBuilder.loadTexts:sfpsPoolTable.setStatus(_A)
_SfpsPoolTableEntry_Object=MibTableRow
sfpsPoolTableEntry=_SfpsPoolTableEntry_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,4,1,1))
sfpsPoolTableEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:sfpsPoolTableEntry.setStatus(_A)
_SfpsPoolTableIndex_Type=Integer32
_SfpsPoolTableIndex_Object=MibTableColumn
sfpsPoolTableIndex=_SfpsPoolTableIndex_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,4,1,1,1),_SfpsPoolTableIndex_Type())
sfpsPoolTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPoolTableIndex.setStatus(_A)
_SfpsPoolTableName_Type=DisplayString
_SfpsPoolTableName_Object=MibTableColumn
sfpsPoolTableName=_SfpsPoolTableName_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,4,1,1,2),_SfpsPoolTableName_Type())
sfpsPoolTableName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPoolTableName.setStatus(_A)
_SfpsPoolTableRAM_Type=Integer32
_SfpsPoolTableRAM_Object=MibTableColumn
sfpsPoolTableRAM=_SfpsPoolTableRAM_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,4,1,1,3),_SfpsPoolTableRAM_Type())
sfpsPoolTableRAM.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPoolTableRAM.setStatus(_A)
_SfpsPoolTableBlockSize_Type=Integer32
_SfpsPoolTableBlockSize_Object=MibTableColumn
sfpsPoolTableBlockSize=_SfpsPoolTableBlockSize_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,4,1,1,4),_SfpsPoolTableBlockSize_Type())
sfpsPoolTableBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPoolTableBlockSize.setStatus(_A)
_SfpsPoolTableBlockCount_Type=Integer32
_SfpsPoolTableBlockCount_Object=MibTableColumn
sfpsPoolTableBlockCount=_SfpsPoolTableBlockCount_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,4,1,1,5),_SfpsPoolTableBlockCount_Type())
sfpsPoolTableBlockCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPoolTableBlockCount.setStatus(_A)
_SfpsPoolTableBlockMax_Type=Integer32
_SfpsPoolTableBlockMax_Object=MibTableColumn
sfpsPoolTableBlockMax=_SfpsPoolTableBlockMax_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,4,1,1,6),_SfpsPoolTableBlockMax_Type())
sfpsPoolTableBlockMax.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPoolTableBlockMax.setStatus(_A)
_SfpsPoolTableObjSize_Type=Integer32
_SfpsPoolTableObjSize_Object=MibTableColumn
sfpsPoolTableObjSize=_SfpsPoolTableObjSize_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,4,1,1,7),_SfpsPoolTableObjSize_Type())
sfpsPoolTableObjSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPoolTableObjSize.setStatus(_A)
_SfpsPoolTableObjInUse_Type=Integer32
_SfpsPoolTableObjInUse_Object=MibTableColumn
sfpsPoolTableObjInUse=_SfpsPoolTableObjInUse_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,4,1,1,8),_SfpsPoolTableObjInUse_Type())
sfpsPoolTableObjInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPoolTableObjInUse.setStatus(_A)
_SfpsPoolTableObjMax_Type=Integer32
_SfpsPoolTableObjMax_Object=MibTableColumn
sfpsPoolTableObjMax=_SfpsPoolTableObjMax_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,4,1,1,9),_SfpsPoolTableObjMax_Type())
sfpsPoolTableObjMax.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPoolTableObjMax.setStatus(_A)
_SfpsPoolTableObjInBlock_Type=Integer32
_SfpsPoolTableObjInBlock_Object=MibTableColumn
sfpsPoolTableObjInBlock=_SfpsPoolTableObjInBlock_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,4,1,1,10),_SfpsPoolTableObjInBlock_Type())
sfpsPoolTableObjInBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPoolTableObjInBlock.setStatus(_A)
_SfpsVccPortTable_Object=MibTable
sfpsVccPortTable=_SfpsVccPortTable_Object((1,3,6,1,4,1,52,4,2,4,2,4,1,6))
if mibBuilder.loadTexts:sfpsVccPortTable.setStatus(_A)
_SfpsVccPortEntry_Object=MibTableRow
sfpsVccPortEntry=_SfpsVccPortEntry_Object((1,3,6,1,4,1,52,4,2,4,2,4,1,6,1))
sfpsVccPortEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:sfpsVccPortEntry.setStatus(_A)
_SfpsVccPortLogPort_Type=Integer32
_SfpsVccPortLogPort_Object=MibTableColumn
sfpsVccPortLogPort=_SfpsVccPortLogPort_Object((1,3,6,1,4,1,52,4,2,4,2,4,1,6,1,1),_SfpsVccPortLogPort_Type())
sfpsVccPortLogPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVccPortLogPort.setStatus(_A)
_SfpsVccPortPhyPort_Type=Integer32
_SfpsVccPortPhyPort_Object=MibTableColumn
sfpsVccPortPhyPort=_SfpsVccPortPhyPort_Object((1,3,6,1,4,1,52,4,2,4,2,4,1,6,1,2),_SfpsVccPortPhyPort_Type())
sfpsVccPortPhyPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVccPortPhyPort.setStatus(_A)
_SfpsVccPortVpi_Type=Integer32
_SfpsVccPortVpi_Object=MibTableColumn
sfpsVccPortVpi=_SfpsVccPortVpi_Object((1,3,6,1,4,1,52,4,2,4,2,4,1,6,1,3),_SfpsVccPortVpi_Type())
sfpsVccPortVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVccPortVpi.setStatus(_A)
_SfpsVccPortVci_Type=Integer32
_SfpsVccPortVci_Object=MibTableColumn
sfpsVccPortVci=_SfpsVccPortVci_Object((1,3,6,1,4,1,52,4,2,4,2,4,1,6,1,4),_SfpsVccPortVci_Type())
sfpsVccPortVci.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVccPortVci.setStatus(_A)
class _SfpsVccPortPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('atmLec',1),('atmSvc',2),('atmPvc',3),(_E,4)))
_SfpsVccPortPortType_Type.__name__=_D
_SfpsVccPortPortType_Object=MibTableColumn
sfpsVccPortPortType=_SfpsVccPortPortType_Object((1,3,6,1,4,1,52,4,2,4,2,4,1,6,1,5),_SfpsVccPortPortType_Type())
sfpsVccPortPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVccPortPortType.setStatus(_A)
class _SfpsVccPortLogPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('pendingUp',1),('portUp',2),('portDown',3),(_E,4)))
_SfpsVccPortLogPortType_Type.__name__=_D
_SfpsVccPortLogPortType_Object=MibTableColumn
sfpsVccPortLogPortType=_SfpsVccPortLogPortType_Object((1,3,6,1,4,1,52,4,2,4,2,4,1,6,1,6),_SfpsVccPortLogPortType_Type())
sfpsVccPortLogPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVccPortLogPortType.setStatus(_A)
class _SfpsVccPortPhyLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('linkUp',1),('linkDown',2),(_E,3)))
_SfpsVccPortPhyLinkState_Type.__name__=_D
_SfpsVccPortPhyLinkState_Object=MibTableColumn
sfpsVccPortPhyLinkState=_SfpsVccPortPhyLinkState_Object((1,3,6,1,4,1,52,4,2,4,2,4,1,6,1,7),_SfpsVccPortPhyLinkState_Type())
sfpsVccPortPhyLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVccPortPhyLinkState.setStatus(_A)
_SfpsATMLecPortTable_Object=MibTable
sfpsATMLecPortTable=_SfpsATMLecPortTable_Object((1,3,6,1,4,1,52,4,2,4,2,4,1,7))
if mibBuilder.loadTexts:sfpsATMLecPortTable.setStatus(_A)
_SfpsATMLecPortTableEntry_Object=MibTableRow
sfpsATMLecPortTableEntry=_SfpsATMLecPortTableEntry_Object((1,3,6,1,4,1,52,4,2,4,2,4,1,7,1))
sfpsATMLecPortTableEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:sfpsATMLecPortTableEntry.setStatus(_A)
_SfpsATMLecPortLogPort_Type=Integer32
_SfpsATMLecPortLogPort_Object=MibTableColumn
sfpsATMLecPortLogPort=_SfpsATMLecPortLogPort_Object((1,3,6,1,4,1,52,4,2,4,2,4,1,7,1,1),_SfpsATMLecPortLogPort_Type())
sfpsATMLecPortLogPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMLecPortLogPort.setStatus(_A)
_SfpsATMLecPortPhyPort_Type=Integer32
_SfpsATMLecPortPhyPort_Object=MibTableColumn
sfpsATMLecPortPhyPort=_SfpsATMLecPortPhyPort_Object((1,3,6,1,4,1,52,4,2,4,2,4,1,7,1,2),_SfpsATMLecPortPhyPort_Type())
sfpsATMLecPortPhyPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMLecPortPhyPort.setStatus(_A)
_SfpsATMLecPortElanName_Type=Integer32
_SfpsATMLecPortElanName_Object=MibTableColumn
sfpsATMLecPortElanName=_SfpsATMLecPortElanName_Object((1,3,6,1,4,1,52,4,2,4,2,4,1,7,1,3),_SfpsATMLecPortElanName_Type())
sfpsATMLecPortElanName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMLecPortElanName.setStatus(_A)
_SfpsATMLecPortPhyLinkState_Type=Integer32
_SfpsATMLecPortPhyLinkState_Object=MibTableColumn
sfpsATMLecPortPhyLinkState=_SfpsATMLecPortPhyLinkState_Object((1,3,6,1,4,1,52,4,2,4,2,4,1,7,1,4),_SfpsATMLecPortPhyLinkState_Type())
sfpsATMLecPortPhyLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMLecPortPhyLinkState.setStatus(_A)
_SfpsATMLecPortLECType_Type=Integer32
_SfpsATMLecPortLECType_Object=MibTableColumn
sfpsATMLecPortLECType=_SfpsATMLecPortLECType_Object((1,3,6,1,4,1,52,4,2,4,2,4,1,7,1,5),_SfpsATMLecPortLECType_Type())
sfpsATMLecPortLECType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMLecPortLECType.setStatus(_A)
_SfpsATMResolveSystemLearnTableSize_Type=Integer32
_SfpsATMResolveSystemLearnTableSize_Object=MibScalar
sfpsATMResolveSystemLearnTableSize=_SfpsATMResolveSystemLearnTableSize_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,1),_SfpsATMResolveSystemLearnTableSize_Type())
sfpsATMResolveSystemLearnTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsATMResolveSystemLearnTableSize.setStatus(_A)
class _SfpsATMResolveCountersVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_SfpsATMResolveCountersVerb_Type.__name__=_D
_SfpsATMResolveCountersVerb_Object=MibScalar
sfpsATMResolveCountersVerb=_SfpsATMResolveCountersVerb_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,1),_SfpsATMResolveCountersVerb_Type())
sfpsATMResolveCountersVerb.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersVerb.setStatus(_A)
_SfpsATMResolveCountersUptime_Type=Integer32
_SfpsATMResolveCountersUptime_Object=MibScalar
sfpsATMResolveCountersUptime=_SfpsATMResolveCountersUptime_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,2),_SfpsATMResolveCountersUptime_Type())
sfpsATMResolveCountersUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersUptime.setStatus(_A)
_SfpsATMResolveCountersQueryMACReq_Type=Integer32
_SfpsATMResolveCountersQueryMACReq_Object=MibScalar
sfpsATMResolveCountersQueryMACReq=_SfpsATMResolveCountersQueryMACReq_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,3),_SfpsATMResolveCountersQueryMACReq_Type())
sfpsATMResolveCountersQueryMACReq.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersQueryMACReq.setStatus(_A)
_SfpsATMResolveCountersQueryMACFail_Type=Integer32
_SfpsATMResolveCountersQueryMACFail_Object=MibScalar
sfpsATMResolveCountersQueryMACFail=_SfpsATMResolveCountersQueryMACFail_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,4),_SfpsATMResolveCountersQueryMACFail_Type())
sfpsATMResolveCountersQueryMACFail.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersQueryMACFail.setStatus(_A)
_SfpsATMResolveCountersQueryMACGood_Type=Integer32
_SfpsATMResolveCountersQueryMACGood_Object=MibScalar
sfpsATMResolveCountersQueryMACGood=_SfpsATMResolveCountersQueryMACGood_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,5),_SfpsATMResolveCountersQueryMACGood_Type())
sfpsATMResolveCountersQueryMACGood.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersQueryMACGood.setStatus(_A)
_SfpsATMResolveCountersQueryMACDaSaChecks_Type=Integer32
_SfpsATMResolveCountersQueryMACDaSaChecks_Object=MibScalar
sfpsATMResolveCountersQueryMACDaSaChecks=_SfpsATMResolveCountersQueryMACDaSaChecks_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,6),_SfpsATMResolveCountersQueryMACDaSaChecks_Type())
sfpsATMResolveCountersQueryMACDaSaChecks.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersQueryMACDaSaChecks.setStatus(_A)
_SfpsATMResolveCountersQueryMACDaSaHits_Type=Integer32
_SfpsATMResolveCountersQueryMACDaSaHits_Object=MibScalar
sfpsATMResolveCountersQueryMACDaSaHits=_SfpsATMResolveCountersQueryMACDaSaHits_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,7),_SfpsATMResolveCountersQueryMACDaSaHits_Type())
sfpsATMResolveCountersQueryMACDaSaHits.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersQueryMACDaSaHits.setStatus(_A)
_SfpsATMResolveCountersQueryMACDaSaMissess_Type=Integer32
_SfpsATMResolveCountersQueryMACDaSaMissess_Object=MibScalar
sfpsATMResolveCountersQueryMACDaSaMissess=_SfpsATMResolveCountersQueryMACDaSaMissess_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,8),_SfpsATMResolveCountersQueryMACDaSaMissess_Type())
sfpsATMResolveCountersQueryMACDaSaMissess.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersQueryMACDaSaMissess.setStatus(_A)
_SfpsATMResolveCountersQueryMACVdirChecks_Type=Integer32
_SfpsATMResolveCountersQueryMACVdirChecks_Object=MibScalar
sfpsATMResolveCountersQueryMACVdirChecks=_SfpsATMResolveCountersQueryMACVdirChecks_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,9),_SfpsATMResolveCountersQueryMACVdirChecks_Type())
sfpsATMResolveCountersQueryMACVdirChecks.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersQueryMACVdirChecks.setStatus(_A)
_SfpsATMResolveCountersQueryMACVdirHits_Type=Integer32
_SfpsATMResolveCountersQueryMACVdirHits_Object=MibScalar
sfpsATMResolveCountersQueryMACVdirHits=_SfpsATMResolveCountersQueryMACVdirHits_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,10),_SfpsATMResolveCountersQueryMACVdirHits_Type())
sfpsATMResolveCountersQueryMACVdirHits.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersQueryMACVdirHits.setStatus(_A)
_SfpsATMResolveCountersQueryMACVdirMisses_Type=Integer32
_SfpsATMResolveCountersQueryMACVdirMisses_Object=MibScalar
sfpsATMResolveCountersQueryMACVdirMisses=_SfpsATMResolveCountersQueryMACVdirMisses_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,11),_SfpsATMResolveCountersQueryMACVdirMisses_Type())
sfpsATMResolveCountersQueryMACVdirMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersQueryMACVdirMisses.setStatus(_A)
_SfpsATMResolveCountersQueryMACErrors_Type=Integer32
_SfpsATMResolveCountersQueryMACErrors_Object=MibScalar
sfpsATMResolveCountersQueryMACErrors=_SfpsATMResolveCountersQueryMACErrors_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,12),_SfpsATMResolveCountersQueryMACErrors_Type())
sfpsATMResolveCountersQueryMACErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersQueryMACErrors.setStatus(_A)
_SfpsATMResolveCountersQueryMACLecPortSuppress_Type=Integer32
_SfpsATMResolveCountersQueryMACLecPortSuppress_Object=MibScalar
sfpsATMResolveCountersQueryMACLecPortSuppress=_SfpsATMResolveCountersQueryMACLecPortSuppress_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,13),_SfpsATMResolveCountersQueryMACLecPortSuppress_Type())
sfpsATMResolveCountersQueryMACLecPortSuppress.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersQueryMACLecPortSuppress.setStatus(_A)
_SfpsATMResolveCountersQueryMACStandbyDrops_Type=Integer32
_SfpsATMResolveCountersQueryMACStandbyDrops_Object=MibScalar
sfpsATMResolveCountersQueryMACStandbyDrops=_SfpsATMResolveCountersQueryMACStandbyDrops_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,14),_SfpsATMResolveCountersQueryMACStandbyDrops_Type())
sfpsATMResolveCountersQueryMACStandbyDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersQueryMACStandbyDrops.setStatus(_A)
_SfpsATMResolveCountersQueryDaSaRequests_Type=Integer32
_SfpsATMResolveCountersQueryDaSaRequests_Object=MibScalar
sfpsATMResolveCountersQueryDaSaRequests=_SfpsATMResolveCountersQueryDaSaRequests_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,15),_SfpsATMResolveCountersQueryDaSaRequests_Type())
sfpsATMResolveCountersQueryDaSaRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersQueryDaSaRequests.setStatus(_A)
_SfpsATMResolveCountersQueryDaSaHits_Type=Integer32
_SfpsATMResolveCountersQueryDaSaHits_Object=MibScalar
sfpsATMResolveCountersQueryDaSaHits=_SfpsATMResolveCountersQueryDaSaHits_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,16),_SfpsATMResolveCountersQueryDaSaHits_Type())
sfpsATMResolveCountersQueryDaSaHits.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersQueryDaSaHits.setStatus(_A)
_SfpsATMResolveCountersQueryDaSaMisses_Type=Integer32
_SfpsATMResolveCountersQueryDaSaMisses_Object=MibScalar
sfpsATMResolveCountersQueryDaSaMisses=_SfpsATMResolveCountersQueryDaSaMisses_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,17),_SfpsATMResolveCountersQueryDaSaMisses_Type())
sfpsATMResolveCountersQueryDaSaMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersQueryDaSaMisses.setStatus(_A)
_SfpsATMResolveCountersQueryDaSaErrors_Type=Integer32
_SfpsATMResolveCountersQueryDaSaErrors_Object=MibScalar
sfpsATMResolveCountersQueryDaSaErrors=_SfpsATMResolveCountersQueryDaSaErrors_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,2,18),_SfpsATMResolveCountersQueryDaSaErrors_Type())
sfpsATMResolveCountersQueryDaSaErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveCountersQueryDaSaErrors.setStatus(_A)
_SfpsATMResolveDiagAPIVerb_Type=Integer32
_SfpsATMResolveDiagAPIVerb_Object=MibScalar
sfpsATMResolveDiagAPIVerb=_SfpsATMResolveDiagAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,3),_SfpsATMResolveDiagAPIVerb_Type())
sfpsATMResolveDiagAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsATMResolveDiagAPIVerb.setStatus(_A)
_SfpsATMResolveDiagAPIInDA_Type=Integer32
_SfpsATMResolveDiagAPIInDA_Object=MibScalar
sfpsATMResolveDiagAPIInDA=_SfpsATMResolveDiagAPIInDA_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,8),_SfpsATMResolveDiagAPIInDA_Type())
sfpsATMResolveDiagAPIInDA.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsATMResolveDiagAPIInDA.setStatus(_A)
_SfpsATMResolveDiagAPIInSA_Type=Integer32
_SfpsATMResolveDiagAPIInSA_Object=MibScalar
sfpsATMResolveDiagAPIInSA=_SfpsATMResolveDiagAPIInSA_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,9),_SfpsATMResolveDiagAPIInSA_Type())
sfpsATMResolveDiagAPIInSA.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsATMResolveDiagAPIInSA.setStatus(_A)
_SfpsATMResolveDiagAPIInSrcLecPort_Type=Integer32
_SfpsATMResolveDiagAPIInSrcLecPort_Object=MibScalar
sfpsATMResolveDiagAPIInSrcLecPort=_SfpsATMResolveDiagAPIInSrcLecPort_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,10),_SfpsATMResolveDiagAPIInSrcLecPort_Type())
sfpsATMResolveDiagAPIInSrcLecPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsATMResolveDiagAPIInSrcLecPort.setStatus(_A)
_SfpsATMResolveDiagAPIOutStatus_Type=Integer32
_SfpsATMResolveDiagAPIOutStatus_Object=MibScalar
sfpsATMResolveDiagAPIOutStatus=_SfpsATMResolveDiagAPIOutStatus_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,11),_SfpsATMResolveDiagAPIOutStatus_Type())
sfpsATMResolveDiagAPIOutStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveDiagAPIOutStatus.setStatus(_A)
_SfpsATMResolveDiagAPIOutPort_Type=Integer32
_SfpsATMResolveDiagAPIOutPort_Object=MibScalar
sfpsATMResolveDiagAPIOutPort=_SfpsATMResolveDiagAPIOutPort_Object((1,3,6,1,4,1,52,4,2,4,2,4,3,12),_SfpsATMResolveDiagAPIOutPort_Type())
sfpsATMResolveDiagAPIOutPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMResolveDiagAPIOutPort.setStatus(_A)
_SfpsAnibIfoStatsTable_Object=MibTable
sfpsAnibIfoStatsTable=_SfpsAnibIfoStatsTable_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1))
if mibBuilder.loadTexts:sfpsAnibIfoStatsTable.setStatus(_A)
_SfpsAnibIfoStatsTableEntry_Object=MibTableRow
sfpsAnibIfoStatsTableEntry=_SfpsAnibIfoStatsTableEntry_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1,1))
sfpsAnibIfoStatsTableEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:sfpsAnibIfoStatsTableEntry.setStatus(_A)
_SfpsAnibIfoStatsPhysIntf_Type=Integer32
_SfpsAnibIfoStatsPhysIntf_Object=MibTableColumn
sfpsAnibIfoStatsPhysIntf=_SfpsAnibIfoStatsPhysIntf_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1,1,1),_SfpsAnibIfoStatsPhysIntf_Type())
sfpsAnibIfoStatsPhysIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAnibIfoStatsPhysIntf.setStatus(_A)
_SfpsAnibIfoStatsCtrlMessages_Type=Integer32
_SfpsAnibIfoStatsCtrlMessages_Object=MibTableColumn
sfpsAnibIfoStatsCtrlMessages=_SfpsAnibIfoStatsCtrlMessages_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1,1,2),_SfpsAnibIfoStatsCtrlMessages_Type())
sfpsAnibIfoStatsCtrlMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAnibIfoStatsCtrlMessages.setStatus(_A)
_SfpsAnibIfoStatsIlmiMessages_Type=Integer32
_SfpsAnibIfoStatsIlmiMessages_Object=MibTableColumn
sfpsAnibIfoStatsIlmiMessages=_SfpsAnibIfoStatsIlmiMessages_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1,1,3),_SfpsAnibIfoStatsIlmiMessages_Type())
sfpsAnibIfoStatsIlmiMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAnibIfoStatsIlmiMessages.setStatus(_A)
_SfpsAnibIfoStatsUniMessages_Type=Integer32
_SfpsAnibIfoStatsUniMessages_Object=MibTableColumn
sfpsAnibIfoStatsUniMessages=_SfpsAnibIfoStatsUniMessages_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1,1,4),_SfpsAnibIfoStatsUniMessages_Type())
sfpsAnibIfoStatsUniMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAnibIfoStatsUniMessages.setStatus(_A)
_SfpsAnibIfoStatsLaneMessages_Type=Integer32
_SfpsAnibIfoStatsLaneMessages_Object=MibTableColumn
sfpsAnibIfoStatsLaneMessages=_SfpsAnibIfoStatsLaneMessages_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1,1,5),_SfpsAnibIfoStatsLaneMessages_Type())
sfpsAnibIfoStatsLaneMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAnibIfoStatsLaneMessages.setStatus(_A)
_SfpsAnibIfoStatsPCSPoolSize_Type=Integer32
_SfpsAnibIfoStatsPCSPoolSize_Object=MibTableColumn
sfpsAnibIfoStatsPCSPoolSize=_SfpsAnibIfoStatsPCSPoolSize_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1,1,6),_SfpsAnibIfoStatsPCSPoolSize_Type())
sfpsAnibIfoStatsPCSPoolSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAnibIfoStatsPCSPoolSize.setStatus(_A)
_SfpsAnibIfoStatsPCSPoolDrops_Type=Integer32
_SfpsAnibIfoStatsPCSPoolDrops_Object=MibTableColumn
sfpsAnibIfoStatsPCSPoolDrops=_SfpsAnibIfoStatsPCSPoolDrops_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1,1,7),_SfpsAnibIfoStatsPCSPoolDrops_Type())
sfpsAnibIfoStatsPCSPoolDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAnibIfoStatsPCSPoolDrops.setStatus(_A)
_SfpsAnibIfoStatsPoolIlmiDrops_Type=Integer32
_SfpsAnibIfoStatsPoolIlmiDrops_Object=MibTableColumn
sfpsAnibIfoStatsPoolIlmiDrops=_SfpsAnibIfoStatsPoolIlmiDrops_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1,1,8),_SfpsAnibIfoStatsPoolIlmiDrops_Type())
sfpsAnibIfoStatsPoolIlmiDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAnibIfoStatsPoolIlmiDrops.setStatus(_A)
_SfpsAnibIfoStatsPoolUniDrops_Type=Integer32
_SfpsAnibIfoStatsPoolUniDrops_Object=MibTableColumn
sfpsAnibIfoStatsPoolUniDrops=_SfpsAnibIfoStatsPoolUniDrops_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1,1,9),_SfpsAnibIfoStatsPoolUniDrops_Type())
sfpsAnibIfoStatsPoolUniDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAnibIfoStatsPoolUniDrops.setStatus(_A)
_SfpsAnibIfoStatsPCSAvail_Type=Integer32
_SfpsAnibIfoStatsPCSAvail_Object=MibTableColumn
sfpsAnibIfoStatsPCSAvail=_SfpsAnibIfoStatsPCSAvail_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1,1,11),_SfpsAnibIfoStatsPCSAvail_Type())
sfpsAnibIfoStatsPCSAvail.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAnibIfoStatsPCSAvail.setStatus(_A)
_SfpsAnibIfoStatsPCSInUse_Type=Integer32
_SfpsAnibIfoStatsPCSInUse_Object=MibTableColumn
sfpsAnibIfoStatsPCSInUse=_SfpsAnibIfoStatsPCSInUse_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1,1,12),_SfpsAnibIfoStatsPCSInUse_Type())
sfpsAnibIfoStatsPCSInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAnibIfoStatsPCSInUse.setStatus(_A)
_SfpsAnibIfoStatsStandbyLeArpsDrops_Type=Integer32
_SfpsAnibIfoStatsStandbyLeArpsDrops_Object=MibTableColumn
sfpsAnibIfoStatsStandbyLeArpsDrops=_SfpsAnibIfoStatsStandbyLeArpsDrops_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1,1,13),_SfpsAnibIfoStatsStandbyLeArpsDrops_Type())
sfpsAnibIfoStatsStandbyLeArpsDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAnibIfoStatsStandbyLeArpsDrops.setStatus(_A)
_SfpsAnibIfoStatsStandbyUnknownsDrops_Type=Integer32
_SfpsAnibIfoStatsStandbyUnknownsDrops_Object=MibTableColumn
sfpsAnibIfoStatsStandbyUnknownsDrops=_SfpsAnibIfoStatsStandbyUnknownsDrops_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1,1,14),_SfpsAnibIfoStatsStandbyUnknownsDrops_Type())
sfpsAnibIfoStatsStandbyUnknownsDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAnibIfoStatsStandbyUnknownsDrops.setStatus(_A)
_SfpsAnibIfoStatsStandbyANIBUnknownsDrops_Type=Integer32
_SfpsAnibIfoStatsStandbyANIBUnknownsDrops_Object=MibTableColumn
sfpsAnibIfoStatsStandbyANIBUnknownsDrops=_SfpsAnibIfoStatsStandbyANIBUnknownsDrops_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1,1,15),_SfpsAnibIfoStatsStandbyANIBUnknownsDrops_Type())
sfpsAnibIfoStatsStandbyANIBUnknownsDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAnibIfoStatsStandbyANIBUnknownsDrops.setStatus(_A)
_SfpsAnibIfoStatsPoolLaneDrops_Type=Integer32
_SfpsAnibIfoStatsPoolLaneDrops_Object=MibTableColumn
sfpsAnibIfoStatsPoolLaneDrops=_SfpsAnibIfoStatsPoolLaneDrops_Object((1,3,6,1,4,1,52,4,2,4,2,4,4,1,1,19),_SfpsAnibIfoStatsPoolLaneDrops_Type())
sfpsAnibIfoStatsPoolLaneDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAnibIfoStatsPoolLaneDrops.setStatus(_A)
_SfpsATMPortsTable_Object=MibTable
sfpsATMPortsTable=_SfpsATMPortsTable_Object((1,3,6,1,4,1,52,4,2,4,2,4,5,1))
if mibBuilder.loadTexts:sfpsATMPortsTable.setStatus(_A)
_SfpsATMPortsTableEntry_Object=MibTableRow
sfpsATMPortsTableEntry=_SfpsATMPortsTableEntry_Object((1,3,6,1,4,1,52,4,2,4,2,4,5,1,1))
sfpsATMPortsTableEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:sfpsATMPortsTableEntry.setStatus(_A)
_SfpsATMPortsPhysIntf_Type=Integer32
_SfpsATMPortsPhysIntf_Object=MibTableColumn
sfpsATMPortsPhysIntf=_SfpsATMPortsPhysIntf_Object((1,3,6,1,4,1,52,4,2,4,2,4,5,1,1,1),_SfpsATMPortsPhysIntf_Type())
sfpsATMPortsPhysIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMPortsPhysIntf.setStatus(_A)
_SfpsATMPortsTotalLECPorts_Type=Integer32
_SfpsATMPortsTotalLECPorts_Object=MibTableColumn
sfpsATMPortsTotalLECPorts=_SfpsATMPortsTotalLECPorts_Object((1,3,6,1,4,1,52,4,2,4,2,4,5,1,1,2),_SfpsATMPortsTotalLECPorts_Type())
sfpsATMPortsTotalLECPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMPortsTotalLECPorts.setStatus(_A)
_SfpsATMPortsTotalPVCPorts_Type=Integer32
_SfpsATMPortsTotalPVCPorts_Object=MibTableColumn
sfpsATMPortsTotalPVCPorts=_SfpsATMPortsTotalPVCPorts_Object((1,3,6,1,4,1,52,4,2,4,2,4,5,1,1,3),_SfpsATMPortsTotalPVCPorts_Type())
sfpsATMPortsTotalPVCPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMPortsTotalPVCPorts.setStatus(_A)
_SfpsATMPortsTotalSVCPorts_Type=Integer32
_SfpsATMPortsTotalSVCPorts_Object=MibTableColumn
sfpsATMPortsTotalSVCPorts=_SfpsATMPortsTotalSVCPorts_Object((1,3,6,1,4,1,52,4,2,4,2,4,5,1,1,4),_SfpsATMPortsTotalSVCPorts_Type())
sfpsATMPortsTotalSVCPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMPortsTotalSVCPorts.setStatus(_A)
_SfpsATMPortsBaseIntfNum_Type=Integer32
_SfpsATMPortsBaseIntfNum_Object=MibTableColumn
sfpsATMPortsBaseIntfNum=_SfpsATMPortsBaseIntfNum_Object((1,3,6,1,4,1,52,4,2,4,2,4,5,1,1,5),_SfpsATMPortsBaseIntfNum_Type())
sfpsATMPortsBaseIntfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMPortsBaseIntfNum.setStatus(_A)
_SfpsATMPortsInUse_Type=Integer32
_SfpsATMPortsInUse_Object=MibTableColumn
sfpsATMPortsInUse=_SfpsATMPortsInUse_Object((1,3,6,1,4,1,52,4,2,4,2,4,5,1,1,6),_SfpsATMPortsInUse_Type())
sfpsATMPortsInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMPortsInUse.setStatus(_A)
class _SfpsATMPortsMgrVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('set',2),('setToDefaults',3),('coldResetNV',4),('warmResetNB',5)))
_SfpsATMPortsMgrVerb_Type.__name__=_D
_SfpsATMPortsMgrVerb_Object=MibScalar
sfpsATMPortsMgrVerb=_SfpsATMPortsMgrVerb_Object((1,3,6,1,4,1,52,4,2,4,2,4,5,2,1),_SfpsATMPortsMgrVerb_Type())
sfpsATMPortsMgrVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsATMPortsMgrVerb.setStatus(_A)
_SfpsATMPortsMgrPhysIntf_Type=Integer32
_SfpsATMPortsMgrPhysIntf_Object=MibScalar
sfpsATMPortsMgrPhysIntf=_SfpsATMPortsMgrPhysIntf_Object((1,3,6,1,4,1,52,4,2,4,2,4,5,2,2),_SfpsATMPortsMgrPhysIntf_Type())
sfpsATMPortsMgrPhysIntf.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsATMPortsMgrPhysIntf.setStatus(_A)
_SfpsATMPortsMgrTotalLECPorts_Type=Integer32
_SfpsATMPortsMgrTotalLECPorts_Object=MibScalar
sfpsATMPortsMgrTotalLECPorts=_SfpsATMPortsMgrTotalLECPorts_Object((1,3,6,1,4,1,52,4,2,4,2,4,5,2,3),_SfpsATMPortsMgrTotalLECPorts_Type())
sfpsATMPortsMgrTotalLECPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsATMPortsMgrTotalLECPorts.setStatus(_A)
_SfpsATMPortsMgrTotalPVCPorts_Type=Integer32
_SfpsATMPortsMgrTotalPVCPorts_Object=MibScalar
sfpsATMPortsMgrTotalPVCPorts=_SfpsATMPortsMgrTotalPVCPorts_Object((1,3,6,1,4,1,52,4,2,4,2,4,5,2,4),_SfpsATMPortsMgrTotalPVCPorts_Type())
sfpsATMPortsMgrTotalPVCPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsATMPortsMgrTotalPVCPorts.setStatus(_A)
_SfpsATMPortsMgrTotalSVCPorts_Type=Integer32
_SfpsATMPortsMgrTotalSVCPorts_Object=MibScalar
sfpsATMPortsMgrTotalSVCPorts=_SfpsATMPortsMgrTotalSVCPorts_Object((1,3,6,1,4,1,52,4,2,4,2,4,5,2,5),_SfpsATMPortsMgrTotalSVCPorts_Type())
sfpsATMPortsMgrTotalSVCPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsATMPortsMgrTotalSVCPorts.setStatus(_A)
class _SfpsATMPortsMgrVerbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ok',1),('exceededMaxAllotment',2),('badIf',3),('error',4)))
_SfpsATMPortsMgrVerbStatus_Type.__name__=_D
_SfpsATMPortsMgrVerbStatus_Object=MibScalar
sfpsATMPortsMgrVerbStatus=_SfpsATMPortsMgrVerbStatus_Object((1,3,6,1,4,1,52,4,2,4,2,4,5,2,6),_SfpsATMPortsMgrVerbStatus_Type())
sfpsATMPortsMgrVerbStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsATMPortsMgrVerbStatus.setStatus(_A)
class _SfpsATMSvcHistoryMgrVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('resetSvcHistory',2),('isableSvcLogging',3),('enableSvcLogging',4),('enableSvcLogsNoWrapping',5)))
_SfpsATMSvcHistoryMgrVerb_Type.__name__=_D
_SfpsATMSvcHistoryMgrVerb_Object=MibScalar
sfpsATMSvcHistoryMgrVerb=_SfpsATMSvcHistoryMgrVerb_Object((1,3,6,1,4,1,52,4,2,4,2,4,8,1,1),_SfpsATMSvcHistoryMgrVerb_Type())
sfpsATMSvcHistoryMgrVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsATMSvcHistoryMgrVerb.setStatus(_A)
_SfpsATMSvcHistoryMgrSvcHistoryWraps_Type=Integer32
_SfpsATMSvcHistoryMgrSvcHistoryWraps_Object=MibScalar
sfpsATMSvcHistoryMgrSvcHistoryWraps=_SfpsATMSvcHistoryMgrSvcHistoryWraps_Object((1,3,6,1,4,1,52,4,2,4,2,4,8,1,2),_SfpsATMSvcHistoryMgrSvcHistoryWraps_Type())
sfpsATMSvcHistoryMgrSvcHistoryWraps.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMSvcHistoryMgrSvcHistoryWraps.setStatus(_A)
class _SfpsATMSvcHistoryMgrLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('enabledNoWrap',2),(_G,3)))
_SfpsATMSvcHistoryMgrLogState_Type.__name__=_D
_SfpsATMSvcHistoryMgrLogState_Object=MibScalar
sfpsATMSvcHistoryMgrLogState=_SfpsATMSvcHistoryMgrLogState_Object((1,3,6,1,4,1,52,4,2,4,2,4,8,1,3),_SfpsATMSvcHistoryMgrLogState_Type())
sfpsATMSvcHistoryMgrLogState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMSvcHistoryMgrLogState.setStatus(_A)
_SfpsATMSvcHistoryMgrEntriesCount_Type=Integer32
_SfpsATMSvcHistoryMgrEntriesCount_Object=MibScalar
sfpsATMSvcHistoryMgrEntriesCount=_SfpsATMSvcHistoryMgrEntriesCount_Object((1,3,6,1,4,1,52,4,2,4,2,4,8,1,4),_SfpsATMSvcHistoryMgrEntriesCount_Type())
sfpsATMSvcHistoryMgrEntriesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMSvcHistoryMgrEntriesCount.setStatus(_A)
_SfpsATMSvcHistoryEventTable_Object=MibTable
sfpsATMSvcHistoryEventTable=_SfpsATMSvcHistoryEventTable_Object((1,3,6,1,4,1,52,4,2,4,2,4,8,2,1))
if mibBuilder.loadTexts:sfpsATMSvcHistoryEventTable.setStatus(_A)
_SfpsATMSvcHistoryEventTableEntry_Object=MibTableRow
sfpsATMSvcHistoryEventTableEntry=_SfpsATMSvcHistoryEventTableEntry_Object((1,3,6,1,4,1,52,4,2,4,2,4,8,2,1,1))
sfpsATMSvcHistoryEventTableEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:sfpsATMSvcHistoryEventTableEntry.setStatus(_A)
_SfpsATMSvcHistoryEventIndex_Type=Integer32
_SfpsATMSvcHistoryEventIndex_Object=MibTableColumn
sfpsATMSvcHistoryEventIndex=_SfpsATMSvcHistoryEventIndex_Object((1,3,6,1,4,1,52,4,2,4,2,4,8,2,1,1,1),_SfpsATMSvcHistoryEventIndex_Type())
sfpsATMSvcHistoryEventIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMSvcHistoryEventIndex.setStatus(_A)
_SfpsATMSvcHistoryEventATMAddr_Type=OctetString
_SfpsATMSvcHistoryEventATMAddr_Object=MibTableColumn
sfpsATMSvcHistoryEventATMAddr=_SfpsATMSvcHistoryEventATMAddr_Object((1,3,6,1,4,1,52,4,2,4,2,4,8,2,1,1,2),_SfpsATMSvcHistoryEventATMAddr_Type())
sfpsATMSvcHistoryEventATMAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMSvcHistoryEventATMAddr.setStatus(_A)
_SfpsATMSvcHistoryEventPortNumber_Type=Integer32
_SfpsATMSvcHistoryEventPortNumber_Object=MibTableColumn
sfpsATMSvcHistoryEventPortNumber=_SfpsATMSvcHistoryEventPortNumber_Object((1,3,6,1,4,1,52,4,2,4,2,4,8,2,1,1,3),_SfpsATMSvcHistoryEventPortNumber_Type())
sfpsATMSvcHistoryEventPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMSvcHistoryEventPortNumber.setStatus(_A)
class _SfpsATMSvcHistoryEventEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('idle',1),('opening',2),('openResponse',3),('peerOpenResponse',4),('openAck',5),('open',6),('closeResponse',7),('closeAck',8),('close',9),('clean',10),('cleanCloseResp',11),('cleanCloseAck',12)))
_SfpsATMSvcHistoryEventEvent_Type.__name__=_D
_SfpsATMSvcHistoryEventEvent_Object=MibTableColumn
sfpsATMSvcHistoryEventEvent=_SfpsATMSvcHistoryEventEvent_Object((1,3,6,1,4,1,52,4,2,4,2,4,8,2,1,1,4),_SfpsATMSvcHistoryEventEvent_Type())
sfpsATMSvcHistoryEventEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMSvcHistoryEventEvent.setStatus(_A)
class _SfpsATMSvcHistoryEventEventChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('error',1),('normal',2)))
_SfpsATMSvcHistoryEventEventChange_Type.__name__=_D
_SfpsATMSvcHistoryEventEventChange_Object=MibTableColumn
sfpsATMSvcHistoryEventEventChange=_SfpsATMSvcHistoryEventEventChange_Object((1,3,6,1,4,1,52,4,2,4,2,4,8,2,1,1,5),_SfpsATMSvcHistoryEventEventChange_Type())
sfpsATMSvcHistoryEventEventChange.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMSvcHistoryEventEventChange.setStatus(_A)
_SfpsATMSvcHistoryEventVccHand_Type=Integer32
_SfpsATMSvcHistoryEventVccHand_Object=MibTableColumn
sfpsATMSvcHistoryEventVccHand=_SfpsATMSvcHistoryEventVccHand_Object((1,3,6,1,4,1,52,4,2,4,2,4,8,2,1,1,6),_SfpsATMSvcHistoryEventVccHand_Type())
sfpsATMSvcHistoryEventVccHand.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMSvcHistoryEventVccHand.setStatus(_A)
_SfpsATMSvcHistoryEventVpi_Type=Integer32
_SfpsATMSvcHistoryEventVpi_Object=MibTableColumn
sfpsATMSvcHistoryEventVpi=_SfpsATMSvcHistoryEventVpi_Object((1,3,6,1,4,1,52,4,2,4,2,4,8,2,1,1,7),_SfpsATMSvcHistoryEventVpi_Type())
sfpsATMSvcHistoryEventVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMSvcHistoryEventVpi.setStatus(_A)
_SfpsATMSvcHistoryEventVci_Type=Integer32
_SfpsATMSvcHistoryEventVci_Object=MibTableColumn
sfpsATMSvcHistoryEventVci=_SfpsATMSvcHistoryEventVci_Object((1,3,6,1,4,1,52,4,2,4,2,4,8,2,1,1,8),_SfpsATMSvcHistoryEventVci_Type())
sfpsATMSvcHistoryEventVci.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMSvcHistoryEventVci.setStatus(_A)
_SfpsATMSvcHistoryEventTime_Type=TimeTicks
_SfpsATMSvcHistoryEventTime_Object=MibTableColumn
sfpsATMSvcHistoryEventTime=_SfpsATMSvcHistoryEventTime_Object((1,3,6,1,4,1,52,4,2,4,2,4,8,2,1,1,9),_SfpsATMSvcHistoryEventTime_Type())
sfpsATMSvcHistoryEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATMSvcHistoryEventTime.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'HexInteger':HexInteger,'SfpsSwitchInstance':SfpsSwitchInstance,'SfpsAddress':SfpsAddress,'sfpsSysConfigTable':sfpsSysConfigTable,'sfpsSysConfigEntry':sfpsSysConfigEntry,_J:sfpsSysConfigSwitchInstance,'sfpsSysConfigAdminStatus':sfpsSysConfigAdminStatus,'sfpsSysConfigAdminReset':sfpsSysConfigAdminReset,'sfpsSysConfigOperStatus':sfpsSysConfigOperStatus,'sfpsSysConfigOperTime':sfpsSysConfigOperTime,'sfpsSysConfigLastChange':sfpsSysConfigLastChange,'sfpsSysConfigVersion':sfpsSysConfigVersion,'sfpsSysConfigMIBRev':sfpsSysConfigMIBRev,'sfpsSysConfigHostMgmtPort':sfpsSysConfigHostMgmtPort,'sfpsSysConfigHostCtrlPort':sfpsSysConfigHostCtrlPort,'sfpsSysConfigHostDataPort':sfpsSysConfigHostDataPort,'sfpsSysConfigHostCtrlThrottleCount':sfpsSysConfigHostCtrlThrottleCount,'sfpsSysConfigHostDataThrottleCount':sfpsSysConfigHostDataThrottleCount,'sfpsSysConfigTrunkSwitch':sfpsSysConfigTrunkSwitch,'sfpsSysConfigSwitchMode':sfpsSysConfigSwitchMode,'sfpsSysConfigSwitchMAC':sfpsSysConfigSwitchMAC,'sfpsSysConfigMgmtAccessType':sfpsSysConfigMgmtAccessType,'sfpsSysConfigChassisMAC':sfpsSysConfigChassisMAC,'sfpsSysConfigChassisIP':sfpsSysConfigChassisIP,'sfpsSysStatsTable':sfpsSysStatsTable,'sfpsSysStatsEntry':sfpsSysStatsEntry,_K:sfpsSysStatsSwitchInstance,'sfpsSysStatsAdminStatus':sfpsSysStatsAdminStatus,'sfpsSysStatsReset':sfpsSysStatsReset,'sfpsSysStatsOperTime':sfpsSysStatsOperTime,'sfpsSysStatsInPkts':sfpsSysStatsInPkts,'sfpsSysStatsOutPkts':sfpsSysStatsOutPkts,'sfpsSysStatsDiscardPkts':sfpsSysStatsDiscardPkts,'sfpsSysStatsFilteredPkts':sfpsSysStatsFilteredPkts,'sfpsSysStatsInOctets':sfpsSysStatsInOctets,'sfpsSysStatsOutOctets':sfpsSysStatsOutOctets,'sfpsSysStatsDiscardOctets':sfpsSysStatsDiscardOctets,'sfpsSysStatsFilteredOctets':sfpsSysStatsFilteredOctets,'sfpsMemHeapStatsHeapInit':sfpsMemHeapStatsHeapInit,'sfpsMemHeapStatsHeapMax':sfpsMemHeapStatsHeapMax,'sfpsMemHeapStatsHeapEnd':sfpsMemHeapStatsHeapEnd,'sfpsMemHeapStatsHeapSize':sfpsMemHeapStatsHeapSize,'sfpsMemHeapStatsFragCount':sfpsMemHeapStatsFragCount,'sfpsMemHeapStatsFragLargest':sfpsMemHeapStatsFragLargest,'sfpsMemHeapStatsFragBytes':sfpsMemHeapStatsFragBytes,'sfpsMemHeapStatsHeapUsed':sfpsMemHeapStatsHeapUsed,'sfpsMemHeapStatsHeapAvail':sfpsMemHeapStatsHeapAvail,'sfpsMemHeapStatsHeapUseMax':sfpsMemHeapStatsHeapUseMax,'sfpsMemHeapStatsHeapUsePercent':sfpsMemHeapStatsHeapUsePercent,'sfpsPoolTable':sfpsPoolTable,'sfpsPoolTableEntry':sfpsPoolTableEntry,_L:sfpsPoolTableIndex,'sfpsPoolTableName':sfpsPoolTableName,'sfpsPoolTableRAM':sfpsPoolTableRAM,'sfpsPoolTableBlockSize':sfpsPoolTableBlockSize,'sfpsPoolTableBlockCount':sfpsPoolTableBlockCount,'sfpsPoolTableBlockMax':sfpsPoolTableBlockMax,'sfpsPoolTableObjSize':sfpsPoolTableObjSize,'sfpsPoolTableObjInUse':sfpsPoolTableObjInUse,'sfpsPoolTableObjMax':sfpsPoolTableObjMax,'sfpsPoolTableObjInBlock':sfpsPoolTableObjInBlock,'sfpsVccPortTable':sfpsVccPortTable,'sfpsVccPortEntry':sfpsVccPortEntry,_M:sfpsVccPortLogPort,'sfpsVccPortPhyPort':sfpsVccPortPhyPort,'sfpsVccPortVpi':sfpsVccPortVpi,'sfpsVccPortVci':sfpsVccPortVci,'sfpsVccPortPortType':sfpsVccPortPortType,'sfpsVccPortLogPortType':sfpsVccPortLogPortType,'sfpsVccPortPhyLinkState':sfpsVccPortPhyLinkState,'sfpsATMLecPortTable':sfpsATMLecPortTable,'sfpsATMLecPortTableEntry':sfpsATMLecPortTableEntry,_N:sfpsATMLecPortLogPort,'sfpsATMLecPortPhyPort':sfpsATMLecPortPhyPort,'sfpsATMLecPortElanName':sfpsATMLecPortElanName,'sfpsATMLecPortPhyLinkState':sfpsATMLecPortPhyLinkState,'sfpsATMLecPortLECType':sfpsATMLecPortLECType,'sfpsATMResolveSystemLearnTableSize':sfpsATMResolveSystemLearnTableSize,'sfpsATMResolveCountersVerb':sfpsATMResolveCountersVerb,'sfpsATMResolveCountersUptime':sfpsATMResolveCountersUptime,'sfpsATMResolveCountersQueryMACReq':sfpsATMResolveCountersQueryMACReq,'sfpsATMResolveCountersQueryMACFail':sfpsATMResolveCountersQueryMACFail,'sfpsATMResolveCountersQueryMACGood':sfpsATMResolveCountersQueryMACGood,'sfpsATMResolveCountersQueryMACDaSaChecks':sfpsATMResolveCountersQueryMACDaSaChecks,'sfpsATMResolveCountersQueryMACDaSaHits':sfpsATMResolveCountersQueryMACDaSaHits,'sfpsATMResolveCountersQueryMACDaSaMissess':sfpsATMResolveCountersQueryMACDaSaMissess,'sfpsATMResolveCountersQueryMACVdirChecks':sfpsATMResolveCountersQueryMACVdirChecks,'sfpsATMResolveCountersQueryMACVdirHits':sfpsATMResolveCountersQueryMACVdirHits,'sfpsATMResolveCountersQueryMACVdirMisses':sfpsATMResolveCountersQueryMACVdirMisses,'sfpsATMResolveCountersQueryMACErrors':sfpsATMResolveCountersQueryMACErrors,'sfpsATMResolveCountersQueryMACLecPortSuppress':sfpsATMResolveCountersQueryMACLecPortSuppress,'sfpsATMResolveCountersQueryMACStandbyDrops':sfpsATMResolveCountersQueryMACStandbyDrops,'sfpsATMResolveCountersQueryDaSaRequests':sfpsATMResolveCountersQueryDaSaRequests,'sfpsATMResolveCountersQueryDaSaHits':sfpsATMResolveCountersQueryDaSaHits,'sfpsATMResolveCountersQueryDaSaMisses':sfpsATMResolveCountersQueryDaSaMisses,'sfpsATMResolveCountersQueryDaSaErrors':sfpsATMResolveCountersQueryDaSaErrors,'sfpsATMResolveDiagAPIVerb':sfpsATMResolveDiagAPIVerb,'sfpsATMResolveDiagAPIInDA':sfpsATMResolveDiagAPIInDA,'sfpsATMResolveDiagAPIInSA':sfpsATMResolveDiagAPIInSA,'sfpsATMResolveDiagAPIInSrcLecPort':sfpsATMResolveDiagAPIInSrcLecPort,'sfpsATMResolveDiagAPIOutStatus':sfpsATMResolveDiagAPIOutStatus,'sfpsATMResolveDiagAPIOutPort':sfpsATMResolveDiagAPIOutPort,'sfpsAnibIfoStatsTable':sfpsAnibIfoStatsTable,'sfpsAnibIfoStatsTableEntry':sfpsAnibIfoStatsTableEntry,_O:sfpsAnibIfoStatsPhysIntf,'sfpsAnibIfoStatsCtrlMessages':sfpsAnibIfoStatsCtrlMessages,'sfpsAnibIfoStatsIlmiMessages':sfpsAnibIfoStatsIlmiMessages,'sfpsAnibIfoStatsUniMessages':sfpsAnibIfoStatsUniMessages,'sfpsAnibIfoStatsLaneMessages':sfpsAnibIfoStatsLaneMessages,'sfpsAnibIfoStatsPCSPoolSize':sfpsAnibIfoStatsPCSPoolSize,'sfpsAnibIfoStatsPCSPoolDrops':sfpsAnibIfoStatsPCSPoolDrops,'sfpsAnibIfoStatsPoolIlmiDrops':sfpsAnibIfoStatsPoolIlmiDrops,'sfpsAnibIfoStatsPoolUniDrops':sfpsAnibIfoStatsPoolUniDrops,'sfpsAnibIfoStatsPCSAvail':sfpsAnibIfoStatsPCSAvail,'sfpsAnibIfoStatsPCSInUse':sfpsAnibIfoStatsPCSInUse,'sfpsAnibIfoStatsStandbyLeArpsDrops':sfpsAnibIfoStatsStandbyLeArpsDrops,'sfpsAnibIfoStatsStandbyUnknownsDrops':sfpsAnibIfoStatsStandbyUnknownsDrops,'sfpsAnibIfoStatsStandbyANIBUnknownsDrops':sfpsAnibIfoStatsStandbyANIBUnknownsDrops,'sfpsAnibIfoStatsPoolLaneDrops':sfpsAnibIfoStatsPoolLaneDrops,'sfpsATMPortsTable':sfpsATMPortsTable,'sfpsATMPortsTableEntry':sfpsATMPortsTableEntry,_P:sfpsATMPortsPhysIntf,'sfpsATMPortsTotalLECPorts':sfpsATMPortsTotalLECPorts,'sfpsATMPortsTotalPVCPorts':sfpsATMPortsTotalPVCPorts,'sfpsATMPortsTotalSVCPorts':sfpsATMPortsTotalSVCPorts,'sfpsATMPortsBaseIntfNum':sfpsATMPortsBaseIntfNum,'sfpsATMPortsInUse':sfpsATMPortsInUse,'sfpsATMPortsMgrVerb':sfpsATMPortsMgrVerb,'sfpsATMPortsMgrPhysIntf':sfpsATMPortsMgrPhysIntf,'sfpsATMPortsMgrTotalLECPorts':sfpsATMPortsMgrTotalLECPorts,'sfpsATMPortsMgrTotalPVCPorts':sfpsATMPortsMgrTotalPVCPorts,'sfpsATMPortsMgrTotalSVCPorts':sfpsATMPortsMgrTotalSVCPorts,'sfpsATMPortsMgrVerbStatus':sfpsATMPortsMgrVerbStatus,'sfpsATMSvcHistoryMgrVerb':sfpsATMSvcHistoryMgrVerb,'sfpsATMSvcHistoryMgrSvcHistoryWraps':sfpsATMSvcHistoryMgrSvcHistoryWraps,'sfpsATMSvcHistoryMgrLogState':sfpsATMSvcHistoryMgrLogState,'sfpsATMSvcHistoryMgrEntriesCount':sfpsATMSvcHistoryMgrEntriesCount,'sfpsATMSvcHistoryEventTable':sfpsATMSvcHistoryEventTable,'sfpsATMSvcHistoryEventTableEntry':sfpsATMSvcHistoryEventTableEntry,_Q:sfpsATMSvcHistoryEventIndex,'sfpsATMSvcHistoryEventATMAddr':sfpsATMSvcHistoryEventATMAddr,'sfpsATMSvcHistoryEventPortNumber':sfpsATMSvcHistoryEventPortNumber,'sfpsATMSvcHistoryEventEvent':sfpsATMSvcHistoryEventEvent,'sfpsATMSvcHistoryEventEventChange':sfpsATMSvcHistoryEventEventChange,'sfpsATMSvcHistoryEventVccHand':sfpsATMSvcHistoryEventVccHand,'sfpsATMSvcHistoryEventVpi':sfpsATMSvcHistoryEventVpi,'sfpsATMSvcHistoryEventVci':sfpsATMSvcHistoryEventVci,'sfpsATMSvcHistoryEventTime':sfpsATMSvcHistoryEventTime})