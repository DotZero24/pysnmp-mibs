_AC='cPppoeSystemLimitsThresholdsNotifGroup'
_AB='cPppoeSystemLimitsThresholdsNotifObjectsGroup'
_AA='cPppoeSystemLimitsThresholdsGroup'
_A9='cPppoePerInterfaceSessionLossPercentNotif'
_A8='cPppoeSystemSessionLossPercentNotif'
_A7='cPppoePerInterfaceSessionLossThresholdNotif'
_A6='cPppoeSystemSessionLossThresholdNotif'
_A5='cPppoeSystemSessionPerVCThrottleNotif'
_A4='cPppoeSystemSessionPerVCLimitNotif'
_A3='cPppoeSystemSessionPerVLANThrottleNotif'
_A2='cPppoeSystemSessionPerVLANLimitNotif'
_A1='cPppoeSystemSessionPerMACThrottleNotif'
_A0='cPppoeSystemSessionPerMACLimitNotif'
_z='cPppoeVcSessionThresholdTrap'
_y='cPppoeSystemSessionThresholdTrap'
_x='cPppoeSystemPerMacIWFSessionlimit'
_w='cPppoeTransSessions'
_v='cPppoeFwdedSessions'
_u='cPppoePtaSessions'
_t='cPppoeTotalSessions'
_s='cPppoeVcExceededSessionErrors'
_r='cPppoeVcHighWaterSessions'
_q='cPppoeVcEnable'
_p='cPppoeSystemExceededSessionErrors'
_o='cPppoeSystemHighWaterSessions'
_n='cPppoeVcCfgEntry'
_m='TruthValue'
_l='atmVclVpi'
_k='atmVclVci'
_j='cPppoeNotificationsGroup'
_i='cPppoePerInterfaceGroup'
_h='cPppoeVcSessionsGroup'
_g='cPppoeVcCfgGroup'
_f='cPppoeSystemGroup'
_e='cPppoeSystemSessionLossPercent'
_d='cPppoeSystemSessionLossThreshold'
_c='cPppoeSystemPerVCThrottleRatelimit'
_b='cPppoeSystemPerVClimit'
_a='cPppoeSystemPerVLANthrottleRatelimit'
_Z='cPppoeSystemPerVLANlimit'
_Y='cPppoeSystemPerMacThrottleRatelimit'
_X='cPppoeSystemPerMacSessionlimit'
_W='cPppoePerInterfaceSessionLossPercent'
_V='cPppoePerInterfaceSessionLossThreshold'
_U='cPppoeVcThresholdSessions'
_T='cPppoeVcMaxAllowedSessions'
_S='cPppoeVcCurrSessions'
_R='cPppoeSystemThresholdSessions'
_Q='cPppoeSystemMaxAllowedSessions'
_P='cPppoeSystemCurrSessions'
_O='ifIndex'
_N='ATM-MIB'
_M='cPppoeSystemSessionVpi'
_L='cPppoeSystemSessionVci'
_K='cPppoeSystemSessionInnerVlanID'
_J='cPppoeSystemSessionVlanID'
_I='cPppoeSystemSessionClientMacAddress'
_H='accessible-for-notify'
_G='ifDescr'
_F='IF-MIB'
_E='sessions'
_D='read-only'
_C='read-write'
_B='current'
_A='CISCO-PPPOE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmVclEntry,atmVclVci,atmVclVpi=mibBuilder.importSymbols(_N,'atmVclEntry',_k,_l)
AtmVcIdentifier,AtmVpIdentifier=mibBuilder.importSymbols('ATM-TC-MIB','AtmVcIdentifier','AtmVpIdentifier')
Percent,=mibBuilder.importSymbols('CISCO-QOS-PIB-MIB','Percent')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifDescr,ifIndex=mibBuilder.importSymbols(_F,_G,_O)
VlanId,VlanIndex=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_m)
ciscoPppoeMIB=ModuleIdentity((1,3,6,1,4,1,9,9,194))
if mibBuilder.loadTexts:ciscoPppoeMIB.setRevisions(('2011-04-25 00:00','2005-12-21 00:00','2001-02-20 00:00'))
_CiscoPppoeMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPppoeMIBObjects=_CiscoPppoeMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,194,1))
_CPppoeSystemSessionInfo_ObjectIdentity=ObjectIdentity
cPppoeSystemSessionInfo=_CPppoeSystemSessionInfo_ObjectIdentity((1,3,6,1,4,1,9,9,194,1,1))
_CPppoeSystemCurrSessions_Type=Gauge32
_CPppoeSystemCurrSessions_Object=MibScalar
cPppoeSystemCurrSessions=_CPppoeSystemCurrSessions_Object((1,3,6,1,4,1,9,9,194,1,1,1),_CPppoeSystemCurrSessions_Type())
cPppoeSystemCurrSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:cPppoeSystemCurrSessions.setStatus(_B)
if mibBuilder.loadTexts:cPppoeSystemCurrSessions.setUnits(_E)
_CPppoeSystemHighWaterSessions_Type=Gauge32
_CPppoeSystemHighWaterSessions_Object=MibScalar
cPppoeSystemHighWaterSessions=_CPppoeSystemHighWaterSessions_Object((1,3,6,1,4,1,9,9,194,1,1,2),_CPppoeSystemHighWaterSessions_Type())
cPppoeSystemHighWaterSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:cPppoeSystemHighWaterSessions.setStatus(_B)
if mibBuilder.loadTexts:cPppoeSystemHighWaterSessions.setUnits(_E)
_CPppoeSystemMaxAllowedSessions_Type=Unsigned32
_CPppoeSystemMaxAllowedSessions_Object=MibScalar
cPppoeSystemMaxAllowedSessions=_CPppoeSystemMaxAllowedSessions_Object((1,3,6,1,4,1,9,9,194,1,1,3),_CPppoeSystemMaxAllowedSessions_Type())
cPppoeSystemMaxAllowedSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:cPppoeSystemMaxAllowedSessions.setStatus(_B)
if mibBuilder.loadTexts:cPppoeSystemMaxAllowedSessions.setUnits(_E)
_CPppoeSystemThresholdSessions_Type=Unsigned32
_CPppoeSystemThresholdSessions_Object=MibScalar
cPppoeSystemThresholdSessions=_CPppoeSystemThresholdSessions_Object((1,3,6,1,4,1,9,9,194,1,1,4),_CPppoeSystemThresholdSessions_Type())
cPppoeSystemThresholdSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:cPppoeSystemThresholdSessions.setStatus(_B)
if mibBuilder.loadTexts:cPppoeSystemThresholdSessions.setUnits(_E)
_CPppoeSystemExceededSessionErrors_Type=Counter32
_CPppoeSystemExceededSessionErrors_Object=MibScalar
cPppoeSystemExceededSessionErrors=_CPppoeSystemExceededSessionErrors_Object((1,3,6,1,4,1,9,9,194,1,1,5),_CPppoeSystemExceededSessionErrors_Type())
cPppoeSystemExceededSessionErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:cPppoeSystemExceededSessionErrors.setStatus(_B)
_CPppoeSystemPerMacSessionlimit_Type=Unsigned32
_CPppoeSystemPerMacSessionlimit_Object=MibScalar
cPppoeSystemPerMacSessionlimit=_CPppoeSystemPerMacSessionlimit_Object((1,3,6,1,4,1,9,9,194,1,1,6),_CPppoeSystemPerMacSessionlimit_Type())
cPppoeSystemPerMacSessionlimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cPppoeSystemPerMacSessionlimit.setStatus(_B)
_CPppoeSystemPerMacIWFSessionlimit_Type=Unsigned32
_CPppoeSystemPerMacIWFSessionlimit_Object=MibScalar
cPppoeSystemPerMacIWFSessionlimit=_CPppoeSystemPerMacIWFSessionlimit_Object((1,3,6,1,4,1,9,9,194,1,1,7),_CPppoeSystemPerMacIWFSessionlimit_Type())
cPppoeSystemPerMacIWFSessionlimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cPppoeSystemPerMacIWFSessionlimit.setStatus(_B)
_CPppoeSystemPerMacThrottleRatelimit_Type=Unsigned32
_CPppoeSystemPerMacThrottleRatelimit_Object=MibScalar
cPppoeSystemPerMacThrottleRatelimit=_CPppoeSystemPerMacThrottleRatelimit_Object((1,3,6,1,4,1,9,9,194,1,1,8),_CPppoeSystemPerMacThrottleRatelimit_Type())
cPppoeSystemPerMacThrottleRatelimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cPppoeSystemPerMacThrottleRatelimit.setStatus(_B)
_CPppoeSystemPerVLANlimit_Type=Unsigned32
_CPppoeSystemPerVLANlimit_Object=MibScalar
cPppoeSystemPerVLANlimit=_CPppoeSystemPerVLANlimit_Object((1,3,6,1,4,1,9,9,194,1,1,9),_CPppoeSystemPerVLANlimit_Type())
cPppoeSystemPerVLANlimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cPppoeSystemPerVLANlimit.setStatus(_B)
_CPppoeSystemPerVLANthrottleRatelimit_Type=Unsigned32
_CPppoeSystemPerVLANthrottleRatelimit_Object=MibScalar
cPppoeSystemPerVLANthrottleRatelimit=_CPppoeSystemPerVLANthrottleRatelimit_Object((1,3,6,1,4,1,9,9,194,1,1,10),_CPppoeSystemPerVLANthrottleRatelimit_Type())
cPppoeSystemPerVLANthrottleRatelimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cPppoeSystemPerVLANthrottleRatelimit.setStatus(_B)
_CPppoeSystemPerVClimit_Type=Unsigned32
_CPppoeSystemPerVClimit_Object=MibScalar
cPppoeSystemPerVClimit=_CPppoeSystemPerVClimit_Object((1,3,6,1,4,1,9,9,194,1,1,11),_CPppoeSystemPerVClimit_Type())
cPppoeSystemPerVClimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cPppoeSystemPerVClimit.setStatus(_B)
_CPppoeSystemPerVCThrottleRatelimit_Type=Unsigned32
_CPppoeSystemPerVCThrottleRatelimit_Object=MibScalar
cPppoeSystemPerVCThrottleRatelimit=_CPppoeSystemPerVCThrottleRatelimit_Object((1,3,6,1,4,1,9,9,194,1,1,12),_CPppoeSystemPerVCThrottleRatelimit_Type())
cPppoeSystemPerVCThrottleRatelimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cPppoeSystemPerVCThrottleRatelimit.setStatus(_B)
_CPppoeSystemSessionLossThreshold_Type=Unsigned32
_CPppoeSystemSessionLossThreshold_Object=MibScalar
cPppoeSystemSessionLossThreshold=_CPppoeSystemSessionLossThreshold_Object((1,3,6,1,4,1,9,9,194,1,1,13),_CPppoeSystemSessionLossThreshold_Type())
cPppoeSystemSessionLossThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cPppoeSystemSessionLossThreshold.setStatus(_B)
_CPppoeSystemSessionLossPercent_Type=Percent
_CPppoeSystemSessionLossPercent_Object=MibScalar
cPppoeSystemSessionLossPercent=_CPppoeSystemSessionLossPercent_Object((1,3,6,1,4,1,9,9,194,1,1,14),_CPppoeSystemSessionLossPercent_Type())
cPppoeSystemSessionLossPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:cPppoeSystemSessionLossPercent.setStatus(_B)
_CPppoeVcCfgInfo_ObjectIdentity=ObjectIdentity
cPppoeVcCfgInfo=_CPppoeVcCfgInfo_ObjectIdentity((1,3,6,1,4,1,9,9,194,1,2))
_CPppoeVcCfgTable_Object=MibTable
cPppoeVcCfgTable=_CPppoeVcCfgTable_Object((1,3,6,1,4,1,9,9,194,1,2,1))
if mibBuilder.loadTexts:cPppoeVcCfgTable.setStatus(_B)
_CPppoeVcCfgEntry_Object=MibTableRow
cPppoeVcCfgEntry=_CPppoeVcCfgEntry_Object((1,3,6,1,4,1,9,9,194,1,2,1,1))
if mibBuilder.loadTexts:cPppoeVcCfgEntry.setStatus(_B)
class _CPppoeVcEnable_Type(TruthValue):defaultValue=2
_CPppoeVcEnable_Type.__name__=_m
_CPppoeVcEnable_Object=MibTableColumn
cPppoeVcEnable=_CPppoeVcEnable_Object((1,3,6,1,4,1,9,9,194,1,2,1,1,1),_CPppoeVcEnable_Type())
cPppoeVcEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cPppoeVcEnable.setStatus(_B)
_CPppoeVcSessionsInfo_ObjectIdentity=ObjectIdentity
cPppoeVcSessionsInfo=_CPppoeVcSessionsInfo_ObjectIdentity((1,3,6,1,4,1,9,9,194,1,3))
_CPppoeVcSessionsTable_Object=MibTable
cPppoeVcSessionsTable=_CPppoeVcSessionsTable_Object((1,3,6,1,4,1,9,9,194,1,3,1))
if mibBuilder.loadTexts:cPppoeVcSessionsTable.setStatus(_B)
_CPppoeVcSessionsEntry_Object=MibTableRow
cPppoeVcSessionsEntry=_CPppoeVcSessionsEntry_Object((1,3,6,1,4,1,9,9,194,1,3,1,1))
cPppoeVcSessionsEntry.setIndexNames((0,_F,_O),(0,_N,_l),(0,_N,_k))
if mibBuilder.loadTexts:cPppoeVcSessionsEntry.setStatus(_B)
_CPppoeVcCurrSessions_Type=Gauge32
_CPppoeVcCurrSessions_Object=MibTableColumn
cPppoeVcCurrSessions=_CPppoeVcCurrSessions_Object((1,3,6,1,4,1,9,9,194,1,3,1,1,1),_CPppoeVcCurrSessions_Type())
cPppoeVcCurrSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:cPppoeVcCurrSessions.setStatus(_B)
if mibBuilder.loadTexts:cPppoeVcCurrSessions.setUnits(_E)
_CPppoeVcHighWaterSessions_Type=Gauge32
_CPppoeVcHighWaterSessions_Object=MibTableColumn
cPppoeVcHighWaterSessions=_CPppoeVcHighWaterSessions_Object((1,3,6,1,4,1,9,9,194,1,3,1,1,2),_CPppoeVcHighWaterSessions_Type())
cPppoeVcHighWaterSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:cPppoeVcHighWaterSessions.setStatus(_B)
if mibBuilder.loadTexts:cPppoeVcHighWaterSessions.setUnits(_E)
_CPppoeVcMaxAllowedSessions_Type=Unsigned32
_CPppoeVcMaxAllowedSessions_Object=MibTableColumn
cPppoeVcMaxAllowedSessions=_CPppoeVcMaxAllowedSessions_Object((1,3,6,1,4,1,9,9,194,1,3,1,1,3),_CPppoeVcMaxAllowedSessions_Type())
cPppoeVcMaxAllowedSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:cPppoeVcMaxAllowedSessions.setStatus(_B)
if mibBuilder.loadTexts:cPppoeVcMaxAllowedSessions.setUnits(_E)
_CPppoeVcThresholdSessions_Type=Unsigned32
_CPppoeVcThresholdSessions_Object=MibTableColumn
cPppoeVcThresholdSessions=_CPppoeVcThresholdSessions_Object((1,3,6,1,4,1,9,9,194,1,3,1,1,4),_CPppoeVcThresholdSessions_Type())
cPppoeVcThresholdSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:cPppoeVcThresholdSessions.setStatus(_B)
if mibBuilder.loadTexts:cPppoeVcThresholdSessions.setUnits(_E)
_CPppoeVcExceededSessionErrors_Type=Counter32
_CPppoeVcExceededSessionErrors_Object=MibTableColumn
cPppoeVcExceededSessionErrors=_CPppoeVcExceededSessionErrors_Object((1,3,6,1,4,1,9,9,194,1,3,1,1,5),_CPppoeVcExceededSessionErrors_Type())
cPppoeVcExceededSessionErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:cPppoeVcExceededSessionErrors.setStatus(_B)
if mibBuilder.loadTexts:cPppoeVcExceededSessionErrors.setUnits('attempts')
_CPppoeSessionsPerInterfaceInfo_ObjectIdentity=ObjectIdentity
cPppoeSessionsPerInterfaceInfo=_CPppoeSessionsPerInterfaceInfo_ObjectIdentity((1,3,6,1,4,1,9,9,194,1,4))
_CPppoeSessionsPerInterfaceTable_Object=MibTable
cPppoeSessionsPerInterfaceTable=_CPppoeSessionsPerInterfaceTable_Object((1,3,6,1,4,1,9,9,194,1,4,1))
if mibBuilder.loadTexts:cPppoeSessionsPerInterfaceTable.setStatus(_B)
_CPppoeSessionsPerInterfaceEntry_Object=MibTableRow
cPppoeSessionsPerInterfaceEntry=_CPppoeSessionsPerInterfaceEntry_Object((1,3,6,1,4,1,9,9,194,1,4,1,1))
cPppoeSessionsPerInterfaceEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:cPppoeSessionsPerInterfaceEntry.setStatus(_B)
_CPppoeTotalSessions_Type=Gauge32
_CPppoeTotalSessions_Object=MibTableColumn
cPppoeTotalSessions=_CPppoeTotalSessions_Object((1,3,6,1,4,1,9,9,194,1,4,1,1,1),_CPppoeTotalSessions_Type())
cPppoeTotalSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:cPppoeTotalSessions.setStatus(_B)
if mibBuilder.loadTexts:cPppoeTotalSessions.setUnits(_E)
_CPppoePtaSessions_Type=Gauge32
_CPppoePtaSessions_Object=MibTableColumn
cPppoePtaSessions=_CPppoePtaSessions_Object((1,3,6,1,4,1,9,9,194,1,4,1,1,2),_CPppoePtaSessions_Type())
cPppoePtaSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:cPppoePtaSessions.setStatus(_B)
if mibBuilder.loadTexts:cPppoePtaSessions.setUnits(_E)
_CPppoeFwdedSessions_Type=Gauge32
_CPppoeFwdedSessions_Object=MibTableColumn
cPppoeFwdedSessions=_CPppoeFwdedSessions_Object((1,3,6,1,4,1,9,9,194,1,4,1,1,3),_CPppoeFwdedSessions_Type())
cPppoeFwdedSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:cPppoeFwdedSessions.setStatus(_B)
if mibBuilder.loadTexts:cPppoeFwdedSessions.setUnits(_E)
_CPppoeTransSessions_Type=Gauge32
_CPppoeTransSessions_Object=MibTableColumn
cPppoeTransSessions=_CPppoeTransSessions_Object((1,3,6,1,4,1,9,9,194,1,4,1,1,4),_CPppoeTransSessions_Type())
cPppoeTransSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:cPppoeTransSessions.setStatus(_B)
if mibBuilder.loadTexts:cPppoeTransSessions.setUnits(_E)
_CPppoePerInterfaceSessionLossThreshold_Type=Unsigned32
_CPppoePerInterfaceSessionLossThreshold_Object=MibTableColumn
cPppoePerInterfaceSessionLossThreshold=_CPppoePerInterfaceSessionLossThreshold_Object((1,3,6,1,4,1,9,9,194,1,4,1,1,5),_CPppoePerInterfaceSessionLossThreshold_Type())
cPppoePerInterfaceSessionLossThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cPppoePerInterfaceSessionLossThreshold.setStatus(_B)
_CPppoePerInterfaceSessionLossPercent_Type=Unsigned32
_CPppoePerInterfaceSessionLossPercent_Object=MibTableColumn
cPppoePerInterfaceSessionLossPercent=_CPppoePerInterfaceSessionLossPercent_Object((1,3,6,1,4,1,9,9,194,1,4,1,1,6),_CPppoePerInterfaceSessionLossPercent_Type())
cPppoePerInterfaceSessionLossPercent.setMaxAccess(_D)
if mibBuilder.loadTexts:cPppoePerInterfaceSessionLossPercent.setStatus(_B)
_CPppoeSystemSessionNotifyObjects_ObjectIdentity=ObjectIdentity
cPppoeSystemSessionNotifyObjects=_CPppoeSystemSessionNotifyObjects_ObjectIdentity((1,3,6,1,4,1,9,9,194,1,5))
_CPppoeSystemSessionClientMacAddress_Type=MacAddress
_CPppoeSystemSessionClientMacAddress_Object=MibScalar
cPppoeSystemSessionClientMacAddress=_CPppoeSystemSessionClientMacAddress_Object((1,3,6,1,4,1,9,9,194,1,5,1),_CPppoeSystemSessionClientMacAddress_Type())
cPppoeSystemSessionClientMacAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:cPppoeSystemSessionClientMacAddress.setStatus(_B)
_CPppoeSystemSessionVlanID_Type=VlanId
_CPppoeSystemSessionVlanID_Object=MibScalar
cPppoeSystemSessionVlanID=_CPppoeSystemSessionVlanID_Object((1,3,6,1,4,1,9,9,194,1,5,2),_CPppoeSystemSessionVlanID_Type())
cPppoeSystemSessionVlanID.setMaxAccess(_H)
if mibBuilder.loadTexts:cPppoeSystemSessionVlanID.setStatus(_B)
_CPppoeSystemSessionInnerVlanID_Type=VlanIndex
_CPppoeSystemSessionInnerVlanID_Object=MibScalar
cPppoeSystemSessionInnerVlanID=_CPppoeSystemSessionInnerVlanID_Object((1,3,6,1,4,1,9,9,194,1,5,3),_CPppoeSystemSessionInnerVlanID_Type())
cPppoeSystemSessionInnerVlanID.setMaxAccess(_H)
if mibBuilder.loadTexts:cPppoeSystemSessionInnerVlanID.setStatus(_B)
_CPppoeSystemSessionVci_Type=AtmVcIdentifier
_CPppoeSystemSessionVci_Object=MibScalar
cPppoeSystemSessionVci=_CPppoeSystemSessionVci_Object((1,3,6,1,4,1,9,9,194,1,5,4),_CPppoeSystemSessionVci_Type())
cPppoeSystemSessionVci.setMaxAccess(_H)
if mibBuilder.loadTexts:cPppoeSystemSessionVci.setStatus(_B)
_CPppoeSystemSessionVpi_Type=AtmVpIdentifier
_CPppoeSystemSessionVpi_Object=MibScalar
cPppoeSystemSessionVpi=_CPppoeSystemSessionVpi_Object((1,3,6,1,4,1,9,9,194,1,5,5),_CPppoeSystemSessionVpi_Type())
cPppoeSystemSessionVpi.setMaxAccess(_H)
if mibBuilder.loadTexts:cPppoeSystemSessionVpi.setStatus(_B)
_CiscoPppoeMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoPppoeMIBNotificationPrefix=_CiscoPppoeMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,194,2))
_CiscoPppoeMIBNotification_ObjectIdentity=ObjectIdentity
ciscoPppoeMIBNotification=_CiscoPppoeMIBNotification_ObjectIdentity((1,3,6,1,4,1,9,9,194,2,0))
_CiscoPppoeMIBConformance_ObjectIdentity=ObjectIdentity
ciscoPppoeMIBConformance=_CiscoPppoeMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,194,3))
_CiscoPppoeMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoPppoeMIBCompliances=_CiscoPppoeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,194,3,1))
_CiscoPppoeMIBGroups_ObjectIdentity=ObjectIdentity
ciscoPppoeMIBGroups=_CiscoPppoeMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,194,3,2))
atmVclEntry.registerAugmentions((_A,_n))
cPppoeVcCfgEntry.setIndexNames(*atmVclEntry.getIndexNames())
cPppoeSystemGroup=ObjectGroup((1,3,6,1,4,1,9,9,194,3,2,1))
cPppoeSystemGroup.setObjects(*((_A,_P),(_A,_o),(_A,_Q),(_A,_R),(_A,_p)))
if mibBuilder.loadTexts:cPppoeSystemGroup.setStatus(_B)
cPppoeVcCfgGroup=ObjectGroup((1,3,6,1,4,1,9,9,194,3,2,2))
cPppoeVcCfgGroup.setObjects((_A,_q))
if mibBuilder.loadTexts:cPppoeVcCfgGroup.setStatus(_B)
cPppoeVcSessionsGroup=ObjectGroup((1,3,6,1,4,1,9,9,194,3,2,3))
cPppoeVcSessionsGroup.setObjects(*((_A,_S),(_A,_r),(_A,_T),(_A,_U),(_A,_s)))
if mibBuilder.loadTexts:cPppoeVcSessionsGroup.setStatus(_B)
cPppoePerInterfaceGroup=ObjectGroup((1,3,6,1,4,1,9,9,194,3,2,5))
cPppoePerInterfaceGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:cPppoePerInterfaceGroup.setStatus(_B)
cPppoeSystemLimitsThresholdsGroup=ObjectGroup((1,3,6,1,4,1,9,9,194,3,2,6))
cPppoeSystemLimitsThresholdsGroup.setObjects(*((_A,_X),(_A,_x),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:cPppoeSystemLimitsThresholdsGroup.setStatus(_B)
cPppoeSystemLimitsThresholdsNotifObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,194,3,2,7))
cPppoeSystemLimitsThresholdsNotifObjectsGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:cPppoeSystemLimitsThresholdsNotifObjectsGroup.setStatus(_B)
cPppoeSystemSessionThresholdTrap=NotificationType((1,3,6,1,4,1,9,9,194,2,0,1))
cPppoeSystemSessionThresholdTrap.setObjects(*((_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:cPppoeSystemSessionThresholdTrap.setStatus(_B)
cPppoeVcSessionThresholdTrap=NotificationType((1,3,6,1,4,1,9,9,194,2,0,2))
cPppoeVcSessionThresholdTrap.setObjects(*((_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:cPppoeVcSessionThresholdTrap.setStatus(_B)
cPppoeSystemSessionPerMACLimitNotif=NotificationType((1,3,6,1,4,1,9,9,194,2,0,3))
cPppoeSystemSessionPerMACLimitNotif.setObjects(*((_A,_X),(_A,_I)))
if mibBuilder.loadTexts:cPppoeSystemSessionPerMACLimitNotif.setStatus(_B)
cPppoeSystemSessionPerMACThrottleNotif=NotificationType((1,3,6,1,4,1,9,9,194,2,0,4))
cPppoeSystemSessionPerMACThrottleNotif.setObjects(*((_A,_Y),(_A,_I)))
if mibBuilder.loadTexts:cPppoeSystemSessionPerMACThrottleNotif.setStatus(_B)
cPppoeSystemSessionPerVLANLimitNotif=NotificationType((1,3,6,1,4,1,9,9,194,2,0,5))
cPppoeSystemSessionPerVLANLimitNotif.setObjects(*((_A,_Z),(_F,_G),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:cPppoeSystemSessionPerVLANLimitNotif.setStatus(_B)
cPppoeSystemSessionPerVLANThrottleNotif=NotificationType((1,3,6,1,4,1,9,9,194,2,0,6))
cPppoeSystemSessionPerVLANThrottleNotif.setObjects(*((_A,_a),(_F,_G),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:cPppoeSystemSessionPerVLANThrottleNotif.setStatus(_B)
cPppoeSystemSessionPerVCLimitNotif=NotificationType((1,3,6,1,4,1,9,9,194,2,0,7))
cPppoeSystemSessionPerVCLimitNotif.setObjects(*((_A,_b),(_F,_G),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:cPppoeSystemSessionPerVCLimitNotif.setStatus(_B)
cPppoeSystemSessionPerVCThrottleNotif=NotificationType((1,3,6,1,4,1,9,9,194,2,0,8))
cPppoeSystemSessionPerVCThrottleNotif.setObjects(*((_A,_c),(_F,_G),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:cPppoeSystemSessionPerVCThrottleNotif.setStatus(_B)
cPppoeSystemSessionLossThresholdNotif=NotificationType((1,3,6,1,4,1,9,9,194,2,0,9))
cPppoeSystemSessionLossThresholdNotif.setObjects((_A,_d))
if mibBuilder.loadTexts:cPppoeSystemSessionLossThresholdNotif.setStatus(_B)
cPppoePerInterfaceSessionLossThresholdNotif=NotificationType((1,3,6,1,4,1,9,9,194,2,0,10))
cPppoePerInterfaceSessionLossThresholdNotif.setObjects(*((_F,_G),(_A,_V)))
if mibBuilder.loadTexts:cPppoePerInterfaceSessionLossThresholdNotif.setStatus(_B)
cPppoeSystemSessionLossPercentNotif=NotificationType((1,3,6,1,4,1,9,9,194,2,0,11))
cPppoeSystemSessionLossPercentNotif.setObjects((_A,_e))
if mibBuilder.loadTexts:cPppoeSystemSessionLossPercentNotif.setStatus(_B)
cPppoePerInterfaceSessionLossPercentNotif=NotificationType((1,3,6,1,4,1,9,9,194,2,0,12))
cPppoePerInterfaceSessionLossPercentNotif.setObjects(*((_F,_G),(_A,_W)))
if mibBuilder.loadTexts:cPppoePerInterfaceSessionLossPercentNotif.setStatus(_B)
cPppoeNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,194,3,2,4))
cPppoeNotificationsGroup.setObjects(*((_A,_y),(_A,_z)))
if mibBuilder.loadTexts:cPppoeNotificationsGroup.setStatus(_B)
cPppoeSystemLimitsThresholdsNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,194,3,2,8))
cPppoeSystemLimitsThresholdsNotifGroup.setObjects(*((_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:cPppoeSystemLimitsThresholdsNotifGroup.setStatus(_B)
ciscoPppoeMIBBasicCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,194,3,1,1))
ciscoPppoeMIBBasicCompliance.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ciscoPppoeMIBBasicCompliance.setStatus('deprecated')
ciscoPppoeMIBBasicComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,194,3,1,2))
ciscoPppoeMIBBasicComplianceRev1.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:ciscoPppoeMIBBasicComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoPppoeMIB':ciscoPppoeMIB,'ciscoPppoeMIBObjects':ciscoPppoeMIBObjects,'cPppoeSystemSessionInfo':cPppoeSystemSessionInfo,_P:cPppoeSystemCurrSessions,_o:cPppoeSystemHighWaterSessions,_Q:cPppoeSystemMaxAllowedSessions,_R:cPppoeSystemThresholdSessions,_p:cPppoeSystemExceededSessionErrors,_X:cPppoeSystemPerMacSessionlimit,_x:cPppoeSystemPerMacIWFSessionlimit,_Y:cPppoeSystemPerMacThrottleRatelimit,_Z:cPppoeSystemPerVLANlimit,_a:cPppoeSystemPerVLANthrottleRatelimit,_b:cPppoeSystemPerVClimit,_c:cPppoeSystemPerVCThrottleRatelimit,_d:cPppoeSystemSessionLossThreshold,_e:cPppoeSystemSessionLossPercent,'cPppoeVcCfgInfo':cPppoeVcCfgInfo,'cPppoeVcCfgTable':cPppoeVcCfgTable,_n:cPppoeVcCfgEntry,_q:cPppoeVcEnable,'cPppoeVcSessionsInfo':cPppoeVcSessionsInfo,'cPppoeVcSessionsTable':cPppoeVcSessionsTable,'cPppoeVcSessionsEntry':cPppoeVcSessionsEntry,_S:cPppoeVcCurrSessions,_r:cPppoeVcHighWaterSessions,_T:cPppoeVcMaxAllowedSessions,_U:cPppoeVcThresholdSessions,_s:cPppoeVcExceededSessionErrors,'cPppoeSessionsPerInterfaceInfo':cPppoeSessionsPerInterfaceInfo,'cPppoeSessionsPerInterfaceTable':cPppoeSessionsPerInterfaceTable,'cPppoeSessionsPerInterfaceEntry':cPppoeSessionsPerInterfaceEntry,_t:cPppoeTotalSessions,_u:cPppoePtaSessions,_v:cPppoeFwdedSessions,_w:cPppoeTransSessions,_V:cPppoePerInterfaceSessionLossThreshold,_W:cPppoePerInterfaceSessionLossPercent,'cPppoeSystemSessionNotifyObjects':cPppoeSystemSessionNotifyObjects,_I:cPppoeSystemSessionClientMacAddress,_J:cPppoeSystemSessionVlanID,_K:cPppoeSystemSessionInnerVlanID,_L:cPppoeSystemSessionVci,_M:cPppoeSystemSessionVpi,'ciscoPppoeMIBNotificationPrefix':ciscoPppoeMIBNotificationPrefix,'ciscoPppoeMIBNotification':ciscoPppoeMIBNotification,_y:cPppoeSystemSessionThresholdTrap,_z:cPppoeVcSessionThresholdTrap,_A0:cPppoeSystemSessionPerMACLimitNotif,_A1:cPppoeSystemSessionPerMACThrottleNotif,_A2:cPppoeSystemSessionPerVLANLimitNotif,_A3:cPppoeSystemSessionPerVLANThrottleNotif,_A4:cPppoeSystemSessionPerVCLimitNotif,_A5:cPppoeSystemSessionPerVCThrottleNotif,_A6:cPppoeSystemSessionLossThresholdNotif,_A7:cPppoePerInterfaceSessionLossThresholdNotif,_A8:cPppoeSystemSessionLossPercentNotif,_A9:cPppoePerInterfaceSessionLossPercentNotif,'ciscoPppoeMIBConformance':ciscoPppoeMIBConformance,'ciscoPppoeMIBCompliances':ciscoPppoeMIBCompliances,'ciscoPppoeMIBBasicCompliance':ciscoPppoeMIBBasicCompliance,'ciscoPppoeMIBBasicComplianceRev1':ciscoPppoeMIBBasicComplianceRev1,'ciscoPppoeMIBGroups':ciscoPppoeMIBGroups,_f:cPppoeSystemGroup,_g:cPppoeVcCfgGroup,_h:cPppoeVcSessionsGroup,_j:cPppoeNotificationsGroup,_i:cPppoePerInterfaceGroup,_AA:cPppoeSystemLimitsThresholdsGroup,_AB:cPppoeSystemLimitsThresholdsNotifObjectsGroup,_AC:cPppoeSystemLimitsThresholdsNotifGroup})