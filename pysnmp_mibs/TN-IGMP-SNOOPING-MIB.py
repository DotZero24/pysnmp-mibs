_p='sdpBndIgmpSnpgStaticSourceAddr'
_o='sdpBndIgmpSnpgStaticGroupAddr'
_n='sdpBndIgmpSnpgGrpSrcAddr'
_m='read-create'
_l='tnSapIgmpSnpgStaticSourceAddr'
_k='tnSapIgmpSnpgStaticGroupAddr'
_j='tnSapIgmpSnpgGrpSrcAddr'
_i='tnTlsIgmpSnpgMRouterAddress'
_h='tnTlsIgmpSnpgProxyGrpSrcAddr'
_g='00000000'
_f='TmnxServId'
_e='TmnxPortID'
_d='TmnxEncapVal'
_c='TmnxAdminState'
_b='TItemDescription'
_a='sdpBndIgmpSnpgGrpAddress'
_Z='tnSapIgmpSnpgGrpAddress'
_Y='tnTlsIgmpSnpgProxyGroupAddress'
_X='TmnxIgmpVersion'
_W='TruthValue'
_V='IpAddress'
_U='deci-seconds'
_T='TPolicyStatementNameOrEmpty'
_S='tnSapPortId'
_R='tnSapEncapValue'
_Q='sdpBindId'
_P='TIMETRA-SDP-MIB'
_O='AlxIgmpSnpgAdminState'
_N='Integer32'
_M='not-accessible'
_L='TN-SAP-MIB'
_K='kbps'
_J='Unsigned32'
_I='TN-IGMP-SNOOPING-MIB'
_H='seconds'
_G='tnSysSwitchId'
_F='TROPIC-SYSTEM-MIB'
_E='tnSvcId'
_D='TN-SERV-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_N,_V,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_W)
sdpBindId,=mibBuilder.importSymbols(_P,_Q)
tnSapEncapValue,tnSapPortId=mibBuilder.importSymbols(_L,_R,_S)
SdpId,tnSvcId=mibBuilder.importSymbols(_D,'SdpId',_E)
TItemDescription,TPolicyStatementNameOrEmpty,TmnxAdminState,TmnxEncapVal,TmnxIgmpGroupFilterMode,TmnxIgmpGroupType,TmnxIgmpVersion,TmnxPortID,TmnxServId,TmnxVcIdOrNone=mibBuilder.importSymbols('TN-TC-MIB',_b,_T,_c,_d,'TmnxIgmpGroupFilterMode','TmnxIgmpGroupType',_X,_e,_f,'TmnxVcIdOrNone')
tnSRMIBModules,tnSRNotifyPrefix,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRNotifyPrefix','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_F,_G)
tnIgmpSnoopingMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,2))
if mibBuilder.loadTexts:tnIgmpSnoopingMIBModule.setRevisions(('2019-02-15 00:00','2018-08-31 00:00','2018-04-27 00:00','2017-11-10 00:00','2015-05-08 00:00','2012-12-05 00:00','2012-09-01 00:00','2008-01-01 00:00','2007-01-01 00:00','2005-08-31 00:00','2005-03-29 00:00','2004-05-17 00:00'))
class AlxIgmpSnpgAdminState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
class AlxIgmpSnpgLocation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sap',1),('sdp',2)))
_TnIgmpSnoopingObjs_ObjectIdentity=ObjectIdentity
tnIgmpSnoopingObjs=_TnIgmpSnoopingObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,24))
_TnIgmpSnoopingTlsObjs_ObjectIdentity=ObjectIdentity
tnIgmpSnoopingTlsObjs=_TnIgmpSnoopingTlsObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,24,1))
_TnTlsIgmpSnpgConfigTable_Object=MibTable
tnTlsIgmpSnpgConfigTable=_TnTlsIgmpSnpgConfigTable_Object((1,3,6,1,4,1,7483,6,1,2,24,1,1))
if mibBuilder.loadTexts:tnTlsIgmpSnpgConfigTable.setStatus(_A)
_TnTlsIgmpSnpgConfigEntry_Object=MibTableRow
tnTlsIgmpSnpgConfigEntry=_TnTlsIgmpSnpgConfigEntry_Object((1,3,6,1,4,1,7483,6,1,2,24,1,1,1))
tnTlsIgmpSnpgConfigEntry.setIndexNames((0,_F,_G),(0,_D,_E))
if mibBuilder.loadTexts:tnTlsIgmpSnpgConfigEntry.setStatus(_A)
class _TnTlsIgmpSnpgCfgAdminState_Type(AlxIgmpSnpgAdminState):defaultValue=2
_TnTlsIgmpSnpgCfgAdminState_Type.__name__=_O
_TnTlsIgmpSnpgCfgAdminState_Object=MibTableColumn
tnTlsIgmpSnpgCfgAdminState=_TnTlsIgmpSnpgCfgAdminState_Object((1,3,6,1,4,1,7483,6,1,2,24,1,1,1,1),_TnTlsIgmpSnpgCfgAdminState_Type())
tnTlsIgmpSnpgCfgAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsIgmpSnpgCfgAdminState.setStatus(_A)
class _TnTlsIgmpSnpgCfgGenQueryIntvl_Type(Unsigned32):defaultValue=125;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TnTlsIgmpSnpgCfgGenQueryIntvl_Type.__name__=_J
_TnTlsIgmpSnpgCfgGenQueryIntvl_Object=MibTableColumn
tnTlsIgmpSnpgCfgGenQueryIntvl=_TnTlsIgmpSnpgCfgGenQueryIntvl_Object((1,3,6,1,4,1,7483,6,1,2,24,1,1,1,2),_TnTlsIgmpSnpgCfgGenQueryIntvl_Type())
tnTlsIgmpSnpgCfgGenQueryIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsIgmpSnpgCfgGenQueryIntvl.setStatus(_A)
if mibBuilder.loadTexts:tnTlsIgmpSnpgCfgGenQueryIntvl.setUnits(_H)
class _TnTlsIgmpSnpgCfgRobustCount_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TnTlsIgmpSnpgCfgRobustCount_Type.__name__=_J
_TnTlsIgmpSnpgCfgRobustCount_Object=MibTableColumn
tnTlsIgmpSnpgCfgRobustCount=_TnTlsIgmpSnpgCfgRobustCount_Object((1,3,6,1,4,1,7483,6,1,2,24,1,1,1,3),_TnTlsIgmpSnpgCfgRobustCount_Type())
tnTlsIgmpSnpgCfgRobustCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsIgmpSnpgCfgRobustCount.setStatus(_A)
class _TnTlsIgmpSnpgCfgReportSrcAddress_Type(IpAddress):defaultHexValue=_g
_TnTlsIgmpSnpgCfgReportSrcAddress_Type.__name__=_V
_TnTlsIgmpSnpgCfgReportSrcAddress_Object=MibTableColumn
tnTlsIgmpSnpgCfgReportSrcAddress=_TnTlsIgmpSnpgCfgReportSrcAddress_Object((1,3,6,1,4,1,7483,6,1,2,24,1,1,1,4),_TnTlsIgmpSnpgCfgReportSrcAddress_Type())
tnTlsIgmpSnpgCfgReportSrcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsIgmpSnpgCfgReportSrcAddress.setStatus(_A)
class _TnTlsIgmpSnpgCfgMvrAdminState_Type(AlxIgmpSnpgAdminState):defaultValue=2
_TnTlsIgmpSnpgCfgMvrAdminState_Type.__name__=_O
_TnTlsIgmpSnpgCfgMvrAdminState_Object=MibTableColumn
tnTlsIgmpSnpgCfgMvrAdminState=_TnTlsIgmpSnpgCfgMvrAdminState_Object((1,3,6,1,4,1,7483,6,1,2,24,1,1,1,5),_TnTlsIgmpSnpgCfgMvrAdminState_Type())
tnTlsIgmpSnpgCfgMvrAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsIgmpSnpgCfgMvrAdminState.setStatus(_A)
class _TnTlsIgmpSnpgCfgMvrDescription_Type(TItemDescription):defaultValue=OctetString('')
_TnTlsIgmpSnpgCfgMvrDescription_Type.__name__=_b
_TnTlsIgmpSnpgCfgMvrDescription_Object=MibTableColumn
tnTlsIgmpSnpgCfgMvrDescription=_TnTlsIgmpSnpgCfgMvrDescription_Object((1,3,6,1,4,1,7483,6,1,2,24,1,1,1,6),_TnTlsIgmpSnpgCfgMvrDescription_Type())
tnTlsIgmpSnpgCfgMvrDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsIgmpSnpgCfgMvrDescription.setStatus(_A)
class _TnTlsIgmpSnpgCfgMvrPolicy_Type(TPolicyStatementNameOrEmpty):defaultValue=OctetString('')
_TnTlsIgmpSnpgCfgMvrPolicy_Type.__name__=_T
_TnTlsIgmpSnpgCfgMvrPolicy_Object=MibTableColumn
tnTlsIgmpSnpgCfgMvrPolicy=_TnTlsIgmpSnpgCfgMvrPolicy_Object((1,3,6,1,4,1,7483,6,1,2,24,1,1,1,7),_TnTlsIgmpSnpgCfgMvrPolicy_Type())
tnTlsIgmpSnpgCfgMvrPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsIgmpSnpgCfgMvrPolicy.setStatus(_A)
class _TnTlsIgmpSnpgCfgQuerySrcAddress_Type(IpAddress):defaultHexValue=_g
_TnTlsIgmpSnpgCfgQuerySrcAddress_Type.__name__=_V
_TnTlsIgmpSnpgCfgQuerySrcAddress_Object=MibTableColumn
tnTlsIgmpSnpgCfgQuerySrcAddress=_TnTlsIgmpSnpgCfgQuerySrcAddress_Object((1,3,6,1,4,1,7483,6,1,2,24,1,1,1,8),_TnTlsIgmpSnpgCfgQuerySrcAddress_Type())
tnTlsIgmpSnpgCfgQuerySrcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsIgmpSnpgCfgQuerySrcAddress.setStatus(_A)
class _TnTlsIgmpSnpgCfgQuerySrcAddrType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('querySrcAddr',1),('systemIpAddr',2)))
_TnTlsIgmpSnpgCfgQuerySrcAddrType_Type.__name__=_N
_TnTlsIgmpSnpgCfgQuerySrcAddrType_Object=MibTableColumn
tnTlsIgmpSnpgCfgQuerySrcAddrType=_TnTlsIgmpSnpgCfgQuerySrcAddrType_Object((1,3,6,1,4,1,7483,6,1,2,24,1,1,1,9),_TnTlsIgmpSnpgCfgQuerySrcAddrType_Type())
tnTlsIgmpSnpgCfgQuerySrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsIgmpSnpgCfgQuerySrcAddrType.setStatus(_A)
_TnTlsIgmpSnpgCfgLastChangeTime_Type=TimeStamp
_TnTlsIgmpSnpgCfgLastChangeTime_Object=MibTableColumn
tnTlsIgmpSnpgCfgLastChangeTime=_TnTlsIgmpSnpgCfgLastChangeTime_Object((1,3,6,1,4,1,7483,6,1,2,24,1,1,1,10),_TnTlsIgmpSnpgCfgLastChangeTime_Type())
tnTlsIgmpSnpgCfgLastChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgCfgLastChangeTime.setStatus(_A)
_TnTlsIgmpSnpgQuerierTable_Object=MibTable
tnTlsIgmpSnpgQuerierTable=_TnTlsIgmpSnpgQuerierTable_Object((1,3,6,1,4,1,7483,6,1,2,24,1,2))
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierTable.setStatus(_A)
_TnTlsIgmpSnpgQuerierEntry_Object=MibTableRow
tnTlsIgmpSnpgQuerierEntry=_TnTlsIgmpSnpgQuerierEntry_Object((1,3,6,1,4,1,7483,6,1,2,24,1,2,1))
tnTlsIgmpSnpgQuerierEntry.setIndexNames((0,_F,_G),(0,_D,_E))
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierEntry.setStatus(_A)
_TnTlsIgmpSnpgQuerierVersion_Type=TmnxIgmpVersion
_TnTlsIgmpSnpgQuerierVersion_Object=MibTableColumn
tnTlsIgmpSnpgQuerierVersion=_TnTlsIgmpSnpgQuerierVersion_Object((1,3,6,1,4,1,7483,6,1,2,24,1,2,1,1),_TnTlsIgmpSnpgQuerierVersion_Type())
tnTlsIgmpSnpgQuerierVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierVersion.setStatus(_A)
_TnTlsIgmpSnpgQuerierAddress_Type=IpAddress
_TnTlsIgmpSnpgQuerierAddress_Object=MibTableColumn
tnTlsIgmpSnpgQuerierAddress=_TnTlsIgmpSnpgQuerierAddress_Object((1,3,6,1,4,1,7483,6,1,2,24,1,2,1,2),_TnTlsIgmpSnpgQuerierAddress_Type())
tnTlsIgmpSnpgQuerierAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierAddress.setStatus(_A)
_TnTlsIgmpSnpgQuerierLocale_Type=AlxIgmpSnpgLocation
_TnTlsIgmpSnpgQuerierLocale_Object=MibTableColumn
tnTlsIgmpSnpgQuerierLocale=_TnTlsIgmpSnpgQuerierLocale_Object((1,3,6,1,4,1,7483,6,1,2,24,1,2,1,3),_TnTlsIgmpSnpgQuerierLocale_Type())
tnTlsIgmpSnpgQuerierLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierLocale.setStatus(_A)
_TnTlsIgmpSnpgQuerierPortId_Type=TmnxPortID
_TnTlsIgmpSnpgQuerierPortId_Object=MibTableColumn
tnTlsIgmpSnpgQuerierPortId=_TnTlsIgmpSnpgQuerierPortId_Object((1,3,6,1,4,1,7483,6,1,2,24,1,2,1,4),_TnTlsIgmpSnpgQuerierPortId_Type())
tnTlsIgmpSnpgQuerierPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierPortId.setStatus(_A)
_TnTlsIgmpSnpgQuerierEncapValue_Type=TmnxEncapVal
_TnTlsIgmpSnpgQuerierEncapValue_Object=MibTableColumn
tnTlsIgmpSnpgQuerierEncapValue=_TnTlsIgmpSnpgQuerierEncapValue_Object((1,3,6,1,4,1,7483,6,1,2,24,1,2,1,5),_TnTlsIgmpSnpgQuerierEncapValue_Type())
tnTlsIgmpSnpgQuerierEncapValue.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierEncapValue.setStatus(_A)
_TnTlsIgmpSnpgQuerierSdpId_Type=SdpId
_TnTlsIgmpSnpgQuerierSdpId_Object=MibTableColumn
tnTlsIgmpSnpgQuerierSdpId=_TnTlsIgmpSnpgQuerierSdpId_Object((1,3,6,1,4,1,7483,6,1,2,24,1,2,1,6),_TnTlsIgmpSnpgQuerierSdpId_Type())
tnTlsIgmpSnpgQuerierSdpId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierSdpId.setStatus(_A)
_TnTlsIgmpSnpgQuerierVcId_Type=TmnxVcIdOrNone
_TnTlsIgmpSnpgQuerierVcId_Object=MibTableColumn
tnTlsIgmpSnpgQuerierVcId=_TnTlsIgmpSnpgQuerierVcId_Object((1,3,6,1,4,1,7483,6,1,2,24,1,2,1,7),_TnTlsIgmpSnpgQuerierVcId_Type())
tnTlsIgmpSnpgQuerierVcId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierVcId.setStatus(_A)
_TnTlsIgmpSnpgQuerierUpTime_Type=TimeTicks
_TnTlsIgmpSnpgQuerierUpTime_Object=MibTableColumn
tnTlsIgmpSnpgQuerierUpTime=_TnTlsIgmpSnpgQuerierUpTime_Object((1,3,6,1,4,1,7483,6,1,2,24,1,2,1,8),_TnTlsIgmpSnpgQuerierUpTime_Type())
tnTlsIgmpSnpgQuerierUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierUpTime.setStatus(_A)
_TnTlsIgmpSnpgQuerierExpiryTime_Type=Unsigned32
_TnTlsIgmpSnpgQuerierExpiryTime_Object=MibTableColumn
tnTlsIgmpSnpgQuerierExpiryTime=_TnTlsIgmpSnpgQuerierExpiryTime_Object((1,3,6,1,4,1,7483,6,1,2,24,1,2,1,9),_TnTlsIgmpSnpgQuerierExpiryTime_Type())
tnTlsIgmpSnpgQuerierExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierExpiryTime.setStatus(_A)
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierExpiryTime.setUnits(_H)
_TnTlsIgmpSnpgQuerierGenQueryIntvl_Type=Unsigned32
_TnTlsIgmpSnpgQuerierGenQueryIntvl_Object=MibTableColumn
tnTlsIgmpSnpgQuerierGenQueryIntvl=_TnTlsIgmpSnpgQuerierGenQueryIntvl_Object((1,3,6,1,4,1,7483,6,1,2,24,1,2,1,10),_TnTlsIgmpSnpgQuerierGenQueryIntvl_Type())
tnTlsIgmpSnpgQuerierGenQueryIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierGenQueryIntvl.setStatus(_A)
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierGenQueryIntvl.setUnits(_H)
_TnTlsIgmpSnpgQuerierGenRespIntvl_Type=Unsigned32
_TnTlsIgmpSnpgQuerierGenRespIntvl_Object=MibTableColumn
tnTlsIgmpSnpgQuerierGenRespIntvl=_TnTlsIgmpSnpgQuerierGenRespIntvl_Object((1,3,6,1,4,1,7483,6,1,2,24,1,2,1,11),_TnTlsIgmpSnpgQuerierGenRespIntvl_Type())
tnTlsIgmpSnpgQuerierGenRespIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierGenRespIntvl.setStatus(_A)
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierGenRespIntvl.setUnits(_U)
_TnTlsIgmpSnpgQuerierRobustCount_Type=Unsigned32
_TnTlsIgmpSnpgQuerierRobustCount_Object=MibTableColumn
tnTlsIgmpSnpgQuerierRobustCount=_TnTlsIgmpSnpgQuerierRobustCount_Object((1,3,6,1,4,1,7483,6,1,2,24,1,2,1,12),_TnTlsIgmpSnpgQuerierRobustCount_Type())
tnTlsIgmpSnpgQuerierRobustCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgQuerierRobustCount.setStatus(_A)
_TnTlsIgmpSnpgProxyGroupTable_Object=MibTable
tnTlsIgmpSnpgProxyGroupTable=_TnTlsIgmpSnpgProxyGroupTable_Object((1,3,6,1,4,1,7483,6,1,2,24,1,3))
if mibBuilder.loadTexts:tnTlsIgmpSnpgProxyGroupTable.setStatus(_A)
_TnTlsIgmpSnpgProxyGroupEntry_Object=MibTableRow
tnTlsIgmpSnpgProxyGroupEntry=_TnTlsIgmpSnpgProxyGroupEntry_Object((1,3,6,1,4,1,7483,6,1,2,24,1,3,1))
tnTlsIgmpSnpgProxyGroupEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_I,_Y))
if mibBuilder.loadTexts:tnTlsIgmpSnpgProxyGroupEntry.setStatus(_A)
_TnTlsIgmpSnpgProxyGroupAddress_Type=IpAddress
_TnTlsIgmpSnpgProxyGroupAddress_Object=MibTableColumn
tnTlsIgmpSnpgProxyGroupAddress=_TnTlsIgmpSnpgProxyGroupAddress_Object((1,3,6,1,4,1,7483,6,1,2,24,1,3,1,1),_TnTlsIgmpSnpgProxyGroupAddress_Type())
tnTlsIgmpSnpgProxyGroupAddress.setMaxAccess(_M)
if mibBuilder.loadTexts:tnTlsIgmpSnpgProxyGroupAddress.setStatus(_A)
_TnTlsIgmpSnpgProxyGroupFilterMode_Type=TmnxIgmpGroupFilterMode
_TnTlsIgmpSnpgProxyGroupFilterMode_Object=MibTableColumn
tnTlsIgmpSnpgProxyGroupFilterMode=_TnTlsIgmpSnpgProxyGroupFilterMode_Object((1,3,6,1,4,1,7483,6,1,2,24,1,3,1,2),_TnTlsIgmpSnpgProxyGroupFilterMode_Type())
tnTlsIgmpSnpgProxyGroupFilterMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgProxyGroupFilterMode.setStatus(_A)
_TnTlsIgmpSnpgProxyGroupUpTime_Type=TimeTicks
_TnTlsIgmpSnpgProxyGroupUpTime_Object=MibTableColumn
tnTlsIgmpSnpgProxyGroupUpTime=_TnTlsIgmpSnpgProxyGroupUpTime_Object((1,3,6,1,4,1,7483,6,1,2,24,1,3,1,3),_TnTlsIgmpSnpgProxyGroupUpTime_Type())
tnTlsIgmpSnpgProxyGroupUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgProxyGroupUpTime.setStatus(_A)
_TnTlsIgmpSnpgProxyGrpSrcTable_Object=MibTable
tnTlsIgmpSnpgProxyGrpSrcTable=_TnTlsIgmpSnpgProxyGrpSrcTable_Object((1,3,6,1,4,1,7483,6,1,2,24,1,4))
if mibBuilder.loadTexts:tnTlsIgmpSnpgProxyGrpSrcTable.setStatus(_A)
_TnTlsIgmpSnpgProxyGrpSrcEntry_Object=MibTableRow
tnTlsIgmpSnpgProxyGrpSrcEntry=_TnTlsIgmpSnpgProxyGrpSrcEntry_Object((1,3,6,1,4,1,7483,6,1,2,24,1,4,1))
tnTlsIgmpSnpgProxyGrpSrcEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_I,_Y),(0,_I,_h))
if mibBuilder.loadTexts:tnTlsIgmpSnpgProxyGrpSrcEntry.setStatus(_A)
_TnTlsIgmpSnpgProxyGrpSrcAddr_Type=IpAddress
_TnTlsIgmpSnpgProxyGrpSrcAddr_Object=MibTableColumn
tnTlsIgmpSnpgProxyGrpSrcAddr=_TnTlsIgmpSnpgProxyGrpSrcAddr_Object((1,3,6,1,4,1,7483,6,1,2,24,1,4,1,1),_TnTlsIgmpSnpgProxyGrpSrcAddr_Type())
tnTlsIgmpSnpgProxyGrpSrcAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:tnTlsIgmpSnpgProxyGrpSrcAddr.setStatus(_A)
_TnTlsIgmpSnpgProxyGrpSrcUpTime_Type=TimeTicks
_TnTlsIgmpSnpgProxyGrpSrcUpTime_Object=MibTableColumn
tnTlsIgmpSnpgProxyGrpSrcUpTime=_TnTlsIgmpSnpgProxyGrpSrcUpTime_Object((1,3,6,1,4,1,7483,6,1,2,24,1,4,1,2),_TnTlsIgmpSnpgProxyGrpSrcUpTime_Type())
tnTlsIgmpSnpgProxyGrpSrcUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgProxyGrpSrcUpTime.setStatus(_A)
_TnTlsIgmpSnpgMRouterTable_Object=MibTable
tnTlsIgmpSnpgMRouterTable=_TnTlsIgmpSnpgMRouterTable_Object((1,3,6,1,4,1,7483,6,1,2,24,1,5))
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterTable.setStatus(_A)
_TnTlsIgmpSnpgMRouterEntry_Object=MibTableRow
tnTlsIgmpSnpgMRouterEntry=_TnTlsIgmpSnpgMRouterEntry_Object((1,3,6,1,4,1,7483,6,1,2,24,1,5,1))
tnTlsIgmpSnpgMRouterEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_I,_i))
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterEntry.setStatus(_A)
_TnTlsIgmpSnpgMRouterAddress_Type=IpAddress
_TnTlsIgmpSnpgMRouterAddress_Object=MibTableColumn
tnTlsIgmpSnpgMRouterAddress=_TnTlsIgmpSnpgMRouterAddress_Object((1,3,6,1,4,1,7483,6,1,2,24,1,5,1,1),_TnTlsIgmpSnpgMRouterAddress_Type())
tnTlsIgmpSnpgMRouterAddress.setMaxAccess(_M)
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterAddress.setStatus(_A)
_TnTlsIgmpSnpgMRouterLocale_Type=AlxIgmpSnpgLocation
_TnTlsIgmpSnpgMRouterLocale_Object=MibTableColumn
tnTlsIgmpSnpgMRouterLocale=_TnTlsIgmpSnpgMRouterLocale_Object((1,3,6,1,4,1,7483,6,1,2,24,1,5,1,2),_TnTlsIgmpSnpgMRouterLocale_Type())
tnTlsIgmpSnpgMRouterLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterLocale.setStatus(_A)
_TnTlsIgmpSnpgMRouterPortId_Type=TmnxPortID
_TnTlsIgmpSnpgMRouterPortId_Object=MibTableColumn
tnTlsIgmpSnpgMRouterPortId=_TnTlsIgmpSnpgMRouterPortId_Object((1,3,6,1,4,1,7483,6,1,2,24,1,5,1,3),_TnTlsIgmpSnpgMRouterPortId_Type())
tnTlsIgmpSnpgMRouterPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterPortId.setStatus(_A)
_TnTlsIgmpSnpgMRouterEncapValue_Type=TmnxEncapVal
_TnTlsIgmpSnpgMRouterEncapValue_Object=MibTableColumn
tnTlsIgmpSnpgMRouterEncapValue=_TnTlsIgmpSnpgMRouterEncapValue_Object((1,3,6,1,4,1,7483,6,1,2,24,1,5,1,4),_TnTlsIgmpSnpgMRouterEncapValue_Type())
tnTlsIgmpSnpgMRouterEncapValue.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterEncapValue.setStatus(_A)
_TnTlsIgmpSnpgMRouterSdpId_Type=SdpId
_TnTlsIgmpSnpgMRouterSdpId_Object=MibTableColumn
tnTlsIgmpSnpgMRouterSdpId=_TnTlsIgmpSnpgMRouterSdpId_Object((1,3,6,1,4,1,7483,6,1,2,24,1,5,1,5),_TnTlsIgmpSnpgMRouterSdpId_Type())
tnTlsIgmpSnpgMRouterSdpId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterSdpId.setStatus(_A)
_TnTlsIgmpSnpgMRouterVcId_Type=TmnxVcIdOrNone
_TnTlsIgmpSnpgMRouterVcId_Object=MibTableColumn
tnTlsIgmpSnpgMRouterVcId=_TnTlsIgmpSnpgMRouterVcId_Object((1,3,6,1,4,1,7483,6,1,2,24,1,5,1,6),_TnTlsIgmpSnpgMRouterVcId_Type())
tnTlsIgmpSnpgMRouterVcId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterVcId.setStatus(_A)
_TnTlsIgmpSnpgMRouterVersion_Type=TmnxIgmpVersion
_TnTlsIgmpSnpgMRouterVersion_Object=MibTableColumn
tnTlsIgmpSnpgMRouterVersion=_TnTlsIgmpSnpgMRouterVersion_Object((1,3,6,1,4,1,7483,6,1,2,24,1,5,1,7),_TnTlsIgmpSnpgMRouterVersion_Type())
tnTlsIgmpSnpgMRouterVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterVersion.setStatus(_A)
_TnTlsIgmpSnpgMRouterExpiryTime_Type=Unsigned32
_TnTlsIgmpSnpgMRouterExpiryTime_Object=MibTableColumn
tnTlsIgmpSnpgMRouterExpiryTime=_TnTlsIgmpSnpgMRouterExpiryTime_Object((1,3,6,1,4,1,7483,6,1,2,24,1,5,1,8),_TnTlsIgmpSnpgMRouterExpiryTime_Type())
tnTlsIgmpSnpgMRouterExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterExpiryTime.setStatus(_A)
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterExpiryTime.setUnits(_H)
_TnTlsIgmpSnpgMRouterUpTime_Type=TimeTicks
_TnTlsIgmpSnpgMRouterUpTime_Object=MibTableColumn
tnTlsIgmpSnpgMRouterUpTime=_TnTlsIgmpSnpgMRouterUpTime_Object((1,3,6,1,4,1,7483,6,1,2,24,1,5,1,9),_TnTlsIgmpSnpgMRouterUpTime_Type())
tnTlsIgmpSnpgMRouterUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterUpTime.setStatus(_A)
_TnTlsIgmpSnpgMRouterGenQueryIntvl_Type=Unsigned32
_TnTlsIgmpSnpgMRouterGenQueryIntvl_Object=MibTableColumn
tnTlsIgmpSnpgMRouterGenQueryIntvl=_TnTlsIgmpSnpgMRouterGenQueryIntvl_Object((1,3,6,1,4,1,7483,6,1,2,24,1,5,1,10),_TnTlsIgmpSnpgMRouterGenQueryIntvl_Type())
tnTlsIgmpSnpgMRouterGenQueryIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterGenQueryIntvl.setStatus(_A)
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterGenQueryIntvl.setUnits(_H)
_TnTlsIgmpSnpgMRouterGenRespIntvl_Type=Unsigned32
_TnTlsIgmpSnpgMRouterGenRespIntvl_Object=MibTableColumn
tnTlsIgmpSnpgMRouterGenRespIntvl=_TnTlsIgmpSnpgMRouterGenRespIntvl_Object((1,3,6,1,4,1,7483,6,1,2,24,1,5,1,11),_TnTlsIgmpSnpgMRouterGenRespIntvl_Type())
tnTlsIgmpSnpgMRouterGenRespIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterGenRespIntvl.setStatus(_A)
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterGenRespIntvl.setUnits(_U)
_TnTlsIgmpSnpgMRouterRobustCount_Type=Unsigned32
_TnTlsIgmpSnpgMRouterRobustCount_Object=MibTableColumn
tnTlsIgmpSnpgMRouterRobustCount=_TnTlsIgmpSnpgMRouterRobustCount_Object((1,3,6,1,4,1,7483,6,1,2,24,1,5,1,12),_TnTlsIgmpSnpgMRouterRobustCount_Type())
tnTlsIgmpSnpgMRouterRobustCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsIgmpSnpgMRouterRobustCount.setStatus(_A)
_TnIgmpSnoopingTlsScalar1_Type=Unsigned32
_TnIgmpSnoopingTlsScalar1_Object=MibScalar
tnIgmpSnoopingTlsScalar1=_TnIgmpSnoopingTlsScalar1_Object((1,3,6,1,4,1,7483,6,1,2,24,1,101),_TnIgmpSnoopingTlsScalar1_Type())
tnIgmpSnoopingTlsScalar1.setMaxAccess(_B)
if mibBuilder.loadTexts:tnIgmpSnoopingTlsScalar1.setStatus(_A)
_TnIgmpSnoopingTlsScalar2_Type=Unsigned32
_TnIgmpSnoopingTlsScalar2_Object=MibScalar
tnIgmpSnoopingTlsScalar2=_TnIgmpSnoopingTlsScalar2_Object((1,3,6,1,4,1,7483,6,1,2,24,1,102),_TnIgmpSnoopingTlsScalar2_Type())
tnIgmpSnoopingTlsScalar2.setMaxAccess(_B)
if mibBuilder.loadTexts:tnIgmpSnoopingTlsScalar2.setStatus(_A)
_TnIgmpSnoopingSapObjs_ObjectIdentity=ObjectIdentity
tnIgmpSnoopingSapObjs=_TnIgmpSnoopingSapObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,24,2))
_TnSapIgmpSnpgConfigTable_Object=MibTable
tnSapIgmpSnpgConfigTable=_TnSapIgmpSnpgConfigTable_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1))
if mibBuilder.loadTexts:tnSapIgmpSnpgConfigTable.setStatus(_A)
_TnSapIgmpSnpgConfigEntry_Object=MibTableRow
tnSapIgmpSnpgConfigEntry=_TnSapIgmpSnpgConfigEntry_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1))
tnSapIgmpSnpgConfigEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_L,_S),(0,_L,_R))
if mibBuilder.loadTexts:tnSapIgmpSnpgConfigEntry.setStatus(_A)
class _TnSapIgmpSnpgCfgImportPlcy_Type(TPolicyStatementNameOrEmpty):defaultValue=OctetString('')
_TnSapIgmpSnpgCfgImportPlcy_Type.__name__=_T
_TnSapIgmpSnpgCfgImportPlcy_Object=MibTableColumn
tnSapIgmpSnpgCfgImportPlcy=_TnSapIgmpSnpgCfgImportPlcy_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,1),_TnSapIgmpSnpgCfgImportPlcy_Type())
tnSapIgmpSnpgCfgImportPlcy.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgImportPlcy.setStatus(_A)
class _TnSapIgmpSnpgCfgFastLeave_Type(AlxIgmpSnpgAdminState):defaultValue=2
_TnSapIgmpSnpgCfgFastLeave_Type.__name__=_O
_TnSapIgmpSnpgCfgFastLeave_Object=MibTableColumn
tnSapIgmpSnpgCfgFastLeave=_TnSapIgmpSnpgCfgFastLeave_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,2),_TnSapIgmpSnpgCfgFastLeave_Type())
tnSapIgmpSnpgCfgFastLeave.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgFastLeave.setStatus(_A)
class _TnSapIgmpSnpgCfgMRouter_Type(TruthValue):defaultValue=2
_TnSapIgmpSnpgCfgMRouter_Type.__name__=_W
_TnSapIgmpSnpgCfgMRouter_Object=MibTableColumn
tnSapIgmpSnpgCfgMRouter=_TnSapIgmpSnpgCfgMRouter_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,3),_TnSapIgmpSnpgCfgMRouter_Type())
tnSapIgmpSnpgCfgMRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMRouter.setStatus(_A)
class _TnSapIgmpSnpgCfgSendQueries_Type(AlxIgmpSnpgAdminState):defaultValue=2
_TnSapIgmpSnpgCfgSendQueries_Type.__name__=_O
_TnSapIgmpSnpgCfgSendQueries_Object=MibTableColumn
tnSapIgmpSnpgCfgSendQueries=_TnSapIgmpSnpgCfgSendQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,4),_TnSapIgmpSnpgCfgSendQueries_Type())
tnSapIgmpSnpgCfgSendQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgSendQueries.setStatus(_A)
class _TnSapIgmpSnpgCfgGenQueryIntvl_Type(Unsigned32):defaultValue=125;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,1024))
_TnSapIgmpSnpgCfgGenQueryIntvl_Type.__name__=_J
_TnSapIgmpSnpgCfgGenQueryIntvl_Object=MibTableColumn
tnSapIgmpSnpgCfgGenQueryIntvl=_TnSapIgmpSnpgCfgGenQueryIntvl_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,5),_TnSapIgmpSnpgCfgGenQueryIntvl_Type())
tnSapIgmpSnpgCfgGenQueryIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgGenQueryIntvl.setStatus(_A)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgGenQueryIntvl.setUnits(_H)
class _TnSapIgmpSnpgCfgQueryRespIntvl_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_TnSapIgmpSnpgCfgQueryRespIntvl_Type.__name__=_J
_TnSapIgmpSnpgCfgQueryRespIntvl_Object=MibTableColumn
tnSapIgmpSnpgCfgQueryRespIntvl=_TnSapIgmpSnpgCfgQueryRespIntvl_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,6),_TnSapIgmpSnpgCfgQueryRespIntvl_Type())
tnSapIgmpSnpgCfgQueryRespIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgQueryRespIntvl.setStatus(_A)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgQueryRespIntvl.setUnits(_H)
class _TnSapIgmpSnpgCfgRobustCount_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,7))
_TnSapIgmpSnpgCfgRobustCount_Type.__name__=_J
_TnSapIgmpSnpgCfgRobustCount_Object=MibTableColumn
tnSapIgmpSnpgCfgRobustCount=_TnSapIgmpSnpgCfgRobustCount_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,7),_TnSapIgmpSnpgCfgRobustCount_Type())
tnSapIgmpSnpgCfgRobustCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgRobustCount.setStatus(_A)
class _TnSapIgmpSnpgCfgLastMembIntvl_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_TnSapIgmpSnpgCfgLastMembIntvl_Type.__name__=_J
_TnSapIgmpSnpgCfgLastMembIntvl_Object=MibTableColumn
tnSapIgmpSnpgCfgLastMembIntvl=_TnSapIgmpSnpgCfgLastMembIntvl_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,8),_TnSapIgmpSnpgCfgLastMembIntvl_Type())
tnSapIgmpSnpgCfgLastMembIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgLastMembIntvl.setStatus(_A)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgLastMembIntvl.setUnits(_U)
class _TnSapIgmpSnpgCfgMaxNbrGrps_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2047))
_TnSapIgmpSnpgCfgMaxNbrGrps_Type.__name__=_N
_TnSapIgmpSnpgCfgMaxNbrGrps_Object=MibTableColumn
tnSapIgmpSnpgCfgMaxNbrGrps=_TnSapIgmpSnpgCfgMaxNbrGrps_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,9),_TnSapIgmpSnpgCfgMaxNbrGrps_Type())
tnSapIgmpSnpgCfgMaxNbrGrps.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMaxNbrGrps.setStatus(_A)
class _TnSapIgmpSnpgCfgMvrFromVplsId_Type(TmnxServId):defaultValue=0
_TnSapIgmpSnpgCfgMvrFromVplsId_Type.__name__=_f
_TnSapIgmpSnpgCfgMvrFromVplsId_Object=MibTableColumn
tnSapIgmpSnpgCfgMvrFromVplsId=_TnSapIgmpSnpgCfgMvrFromVplsId_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,10),_TnSapIgmpSnpgCfgMvrFromVplsId_Type())
tnSapIgmpSnpgCfgMvrFromVplsId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMvrFromVplsId.setStatus(_A)
class _TnSapIgmpSnpgCfgMvrToSapPortId_Type(TmnxPortID):defaultValue=0
_TnSapIgmpSnpgCfgMvrToSapPortId_Type.__name__=_e
_TnSapIgmpSnpgCfgMvrToSapPortId_Object=MibTableColumn
tnSapIgmpSnpgCfgMvrToSapPortId=_TnSapIgmpSnpgCfgMvrToSapPortId_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,11),_TnSapIgmpSnpgCfgMvrToSapPortId_Type())
tnSapIgmpSnpgCfgMvrToSapPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMvrToSapPortId.setStatus(_A)
class _TnSapIgmpSnpgCfgMvrToSapEncapVal_Type(TmnxEncapVal):defaultValue=0
_TnSapIgmpSnpgCfgMvrToSapEncapVal_Type.__name__=_d
_TnSapIgmpSnpgCfgMvrToSapEncapVal_Object=MibTableColumn
tnSapIgmpSnpgCfgMvrToSapEncapVal=_TnSapIgmpSnpgCfgMvrToSapEncapVal_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,12),_TnSapIgmpSnpgCfgMvrToSapEncapVal_Type())
tnSapIgmpSnpgCfgMvrToSapEncapVal.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMvrToSapEncapVal.setStatus(_A)
class _TnSapIgmpSnpgCfgVersion_Type(TmnxIgmpVersion):defaultValue=3
_TnSapIgmpSnpgCfgVersion_Type.__name__=_X
_TnSapIgmpSnpgCfgVersion_Object=MibTableColumn
tnSapIgmpSnpgCfgVersion=_TnSapIgmpSnpgCfgVersion_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,13),_TnSapIgmpSnpgCfgVersion_Type())
tnSapIgmpSnpgCfgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgVersion.setStatus(_A)
class _TnSapIgmpSnpgCfgMcacPolicyName_Type(TPolicyStatementNameOrEmpty):defaultValue=OctetString('')
_TnSapIgmpSnpgCfgMcacPolicyName_Type.__name__=_T
_TnSapIgmpSnpgCfgMcacPolicyName_Object=MibTableColumn
tnSapIgmpSnpgCfgMcacPolicyName=_TnSapIgmpSnpgCfgMcacPolicyName_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,14),_TnSapIgmpSnpgCfgMcacPolicyName_Type())
tnSapIgmpSnpgCfgMcacPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMcacPolicyName.setStatus(_A)
class _TnSapIgmpSnpgCfgMcacUnconstBW_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_TnSapIgmpSnpgCfgMcacUnconstBW_Type.__name__=_N
_TnSapIgmpSnpgCfgMcacUnconstBW_Object=MibTableColumn
tnSapIgmpSnpgCfgMcacUnconstBW=_TnSapIgmpSnpgCfgMcacUnconstBW_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,15),_TnSapIgmpSnpgCfgMcacUnconstBW_Type())
tnSapIgmpSnpgCfgMcacUnconstBW.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMcacUnconstBW.setStatus(_A)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMcacUnconstBW.setUnits(_K)
class _TnSapIgmpSnpgCfgMcacConstAdmSt_Type(TmnxAdminState):defaultValue=2
_TnSapIgmpSnpgCfgMcacConstAdmSt_Type.__name__=_c
_TnSapIgmpSnpgCfgMcacConstAdmSt_Object=MibTableColumn
tnSapIgmpSnpgCfgMcacConstAdmSt=_TnSapIgmpSnpgCfgMcacConstAdmSt_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,16),_TnSapIgmpSnpgCfgMcacConstAdmSt_Type())
tnSapIgmpSnpgCfgMcacConstAdmSt.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMcacConstAdmSt.setStatus(_A)
class _TnSapIgmpSnpgCfgMcacPrRsvMndBW_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_TnSapIgmpSnpgCfgMcacPrRsvMndBW_Type.__name__=_N
_TnSapIgmpSnpgCfgMcacPrRsvMndBW_Object=MibTableColumn
tnSapIgmpSnpgCfgMcacPrRsvMndBW=_TnSapIgmpSnpgCfgMcacPrRsvMndBW_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,17),_TnSapIgmpSnpgCfgMcacPrRsvMndBW_Type())
tnSapIgmpSnpgCfgMcacPrRsvMndBW.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMcacPrRsvMndBW.setStatus(_A)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMcacPrRsvMndBW.setUnits(_K)
_TnSapIgmpSnpgCfgMcacinUseMandBw_Type=Unsigned32
_TnSapIgmpSnpgCfgMcacinUseMandBw_Object=MibTableColumn
tnSapIgmpSnpgCfgMcacinUseMandBw=_TnSapIgmpSnpgCfgMcacinUseMandBw_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,18),_TnSapIgmpSnpgCfgMcacinUseMandBw_Type())
tnSapIgmpSnpgCfgMcacinUseMandBw.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMcacinUseMandBw.setStatus(_A)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMcacinUseMandBw.setUnits(_K)
_TnSapIgmpSnpgCfgMcacinUseOpnlBw_Type=Unsigned32
_TnSapIgmpSnpgCfgMcacinUseOpnlBw_Object=MibTableColumn
tnSapIgmpSnpgCfgMcacinUseOpnlBw=_TnSapIgmpSnpgCfgMcacinUseOpnlBw_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,19),_TnSapIgmpSnpgCfgMcacinUseOpnlBw_Type())
tnSapIgmpSnpgCfgMcacinUseOpnlBw.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMcacinUseOpnlBw.setStatus(_A)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMcacinUseOpnlBw.setUnits(_K)
_TnSapIgmpSnpgCfgMcacAvailMandBw_Type=Unsigned32
_TnSapIgmpSnpgCfgMcacAvailMandBw_Object=MibTableColumn
tnSapIgmpSnpgCfgMcacAvailMandBw=_TnSapIgmpSnpgCfgMcacAvailMandBw_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,20),_TnSapIgmpSnpgCfgMcacAvailMandBw_Type())
tnSapIgmpSnpgCfgMcacAvailMandBw.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMcacAvailMandBw.setStatus(_A)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMcacAvailMandBw.setUnits(_K)
_TnSapIgmpSnpgCfgMcacAvailOpnlBw_Type=Unsigned32
_TnSapIgmpSnpgCfgMcacAvailOpnlBw_Object=MibTableColumn
tnSapIgmpSnpgCfgMcacAvailOpnlBw=_TnSapIgmpSnpgCfgMcacAvailOpnlBw_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,21),_TnSapIgmpSnpgCfgMcacAvailOpnlBw_Type())
tnSapIgmpSnpgCfgMcacAvailOpnlBw.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMcacAvailOpnlBw.setStatus(_A)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMcacAvailOpnlBw.setUnits(_K)
_TnSapIgmpSnpgCfgMcacValInTrans_Type=TruthValue
_TnSapIgmpSnpgCfgMcacValInTrans_Object=MibTableColumn
tnSapIgmpSnpgCfgMcacValInTrans=_TnSapIgmpSnpgCfgMcacValInTrans_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,22),_TnSapIgmpSnpgCfgMcacValInTrans_Type())
tnSapIgmpSnpgCfgMcacValInTrans.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMcacValInTrans.setStatus(_A)
_TnSapIgmpSnpgCfgLastChangeTime_Type=TimeStamp
_TnSapIgmpSnpgCfgLastChangeTime_Object=MibTableColumn
tnSapIgmpSnpgCfgLastChangeTime=_TnSapIgmpSnpgCfgLastChangeTime_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,23),_TnSapIgmpSnpgCfgLastChangeTime_Type())
tnSapIgmpSnpgCfgLastChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgLastChangeTime.setStatus(_A)
class _TnSapIgmpSnpgCfgMaxNbrSrcs_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2047))
_TnSapIgmpSnpgCfgMaxNbrSrcs_Type.__name__=_J
_TnSapIgmpSnpgCfgMaxNbrSrcs_Object=MibTableColumn
tnSapIgmpSnpgCfgMaxNbrSrcs=_TnSapIgmpSnpgCfgMaxNbrSrcs_Object((1,3,6,1,4,1,7483,6,1,2,24,2,1,1,24),_TnSapIgmpSnpgCfgMaxNbrSrcs_Type())
tnSapIgmpSnpgCfgMaxNbrSrcs.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIgmpSnpgCfgMaxNbrSrcs.setStatus(_A)
_TnSapIgmpSnpgGroupTable_Object=MibTable
tnSapIgmpSnpgGroupTable=_TnSapIgmpSnpgGroupTable_Object((1,3,6,1,4,1,7483,6,1,2,24,2,2))
if mibBuilder.loadTexts:tnSapIgmpSnpgGroupTable.setStatus(_A)
_TnSapIgmpSnpgGroupEntry_Object=MibTableRow
tnSapIgmpSnpgGroupEntry=_TnSapIgmpSnpgGroupEntry_Object((1,3,6,1,4,1,7483,6,1,2,24,2,2,1))
tnSapIgmpSnpgGroupEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_L,_S),(0,_L,_R),(0,_I,_Z))
if mibBuilder.loadTexts:tnSapIgmpSnpgGroupEntry.setStatus(_A)
_TnSapIgmpSnpgGrpAddress_Type=IpAddress
_TnSapIgmpSnpgGrpAddress_Object=MibTableColumn
tnSapIgmpSnpgGrpAddress=_TnSapIgmpSnpgGrpAddress_Object((1,3,6,1,4,1,7483,6,1,2,24,2,2,1,1),_TnSapIgmpSnpgGrpAddress_Type())
tnSapIgmpSnpgGrpAddress.setMaxAccess(_M)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpAddress.setStatus(_A)
_TnSapIgmpSnpgGrpType_Type=TmnxIgmpGroupType
_TnSapIgmpSnpgGrpType_Object=MibTableColumn
tnSapIgmpSnpgGrpType=_TnSapIgmpSnpgGrpType_Object((1,3,6,1,4,1,7483,6,1,2,24,2,2,1,2),_TnSapIgmpSnpgGrpType_Type())
tnSapIgmpSnpgGrpType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpType.setStatus(_A)
_TnSapIgmpSnpgGrpFilterMode_Type=TmnxIgmpGroupFilterMode
_TnSapIgmpSnpgGrpFilterMode_Object=MibTableColumn
tnSapIgmpSnpgGrpFilterMode=_TnSapIgmpSnpgGrpFilterMode_Object((1,3,6,1,4,1,7483,6,1,2,24,2,2,1,3),_TnSapIgmpSnpgGrpFilterMode_Type())
tnSapIgmpSnpgGrpFilterMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpFilterMode.setStatus(_A)
_TnSapIgmpSnpgGrpUpTime_Type=TimeTicks
_TnSapIgmpSnpgGrpUpTime_Object=MibTableColumn
tnSapIgmpSnpgGrpUpTime=_TnSapIgmpSnpgGrpUpTime_Object((1,3,6,1,4,1,7483,6,1,2,24,2,2,1,4),_TnSapIgmpSnpgGrpUpTime_Type())
tnSapIgmpSnpgGrpUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpUpTime.setStatus(_A)
_TnSapIgmpSnpgGrpExpiryTime_Type=Unsigned32
_TnSapIgmpSnpgGrpExpiryTime_Object=MibTableColumn
tnSapIgmpSnpgGrpExpiryTime=_TnSapIgmpSnpgGrpExpiryTime_Object((1,3,6,1,4,1,7483,6,1,2,24,2,2,1,5),_TnSapIgmpSnpgGrpExpiryTime_Type())
tnSapIgmpSnpgGrpExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpExpiryTime.setStatus(_A)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpExpiryTime.setUnits(_H)
_TnSapIgmpSnpgGrpCompatMode_Type=Unsigned32
_TnSapIgmpSnpgGrpCompatMode_Object=MibTableColumn
tnSapIgmpSnpgGrpCompatMode=_TnSapIgmpSnpgGrpCompatMode_Object((1,3,6,1,4,1,7483,6,1,2,24,2,2,1,6),_TnSapIgmpSnpgGrpCompatMode_Type())
tnSapIgmpSnpgGrpCompatMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpCompatMode.setStatus(_A)
_TnSapIgmpSnpgGrpV1HostExpTime_Type=Unsigned32
_TnSapIgmpSnpgGrpV1HostExpTime_Object=MibTableColumn
tnSapIgmpSnpgGrpV1HostExpTime=_TnSapIgmpSnpgGrpV1HostExpTime_Object((1,3,6,1,4,1,7483,6,1,2,24,2,2,1,7),_TnSapIgmpSnpgGrpV1HostExpTime_Type())
tnSapIgmpSnpgGrpV1HostExpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpV1HostExpTime.setStatus(_A)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpV1HostExpTime.setUnits(_H)
_TnSapIgmpSnpgGrpV2HostExpTime_Type=Unsigned32
_TnSapIgmpSnpgGrpV2HostExpTime_Object=MibTableColumn
tnSapIgmpSnpgGrpV2HostExpTime=_TnSapIgmpSnpgGrpV2HostExpTime_Object((1,3,6,1,4,1,7483,6,1,2,24,2,2,1,8),_TnSapIgmpSnpgGrpV2HostExpTime_Type())
tnSapIgmpSnpgGrpV2HostExpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpV2HostExpTime.setStatus(_A)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpV2HostExpTime.setUnits(_H)
_TnSapIgmpSnpgGrpMvrFromVplsId_Type=TmnxServId
_TnSapIgmpSnpgGrpMvrFromVplsId_Object=MibTableColumn
tnSapIgmpSnpgGrpMvrFromVplsId=_TnSapIgmpSnpgGrpMvrFromVplsId_Object((1,3,6,1,4,1,7483,6,1,2,24,2,2,1,9),_TnSapIgmpSnpgGrpMvrFromVplsId_Type())
tnSapIgmpSnpgGrpMvrFromVplsId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpMvrFromVplsId.setStatus(_A)
_TnSapIgmpSnpgGrpMvrToSapPortId_Type=TmnxPortID
_TnSapIgmpSnpgGrpMvrToSapPortId_Object=MibTableColumn
tnSapIgmpSnpgGrpMvrToSapPortId=_TnSapIgmpSnpgGrpMvrToSapPortId_Object((1,3,6,1,4,1,7483,6,1,2,24,2,2,1,10),_TnSapIgmpSnpgGrpMvrToSapPortId_Type())
tnSapIgmpSnpgGrpMvrToSapPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpMvrToSapPortId.setStatus(_A)
_TnSapIgmpSnpgGrpMvrToSapEncapVal_Type=TmnxEncapVal
_TnSapIgmpSnpgGrpMvrToSapEncapVal_Object=MibTableColumn
tnSapIgmpSnpgGrpMvrToSapEncapVal=_TnSapIgmpSnpgGrpMvrToSapEncapVal_Object((1,3,6,1,4,1,7483,6,1,2,24,2,2,1,11),_TnSapIgmpSnpgGrpMvrToSapEncapVal_Type())
tnSapIgmpSnpgGrpMvrToSapEncapVal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpMvrToSapEncapVal.setStatus(_A)
_TnSapIgmpSnpgGrpNumSrc_Type=Counter32
_TnSapIgmpSnpgGrpNumSrc_Object=MibTableColumn
tnSapIgmpSnpgGrpNumSrc=_TnSapIgmpSnpgGrpNumSrc_Object((1,3,6,1,4,1,7483,6,1,2,24,2,2,1,12),_TnSapIgmpSnpgGrpNumSrc_Type())
tnSapIgmpSnpgGrpNumSrc.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpNumSrc.setStatus(_A)
_TnSapIgmpSnpgGrpSrcTable_Object=MibTable
tnSapIgmpSnpgGrpSrcTable=_TnSapIgmpSnpgGrpSrcTable_Object((1,3,6,1,4,1,7483,6,1,2,24,2,3))
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpSrcTable.setStatus(_A)
_TnSapIgmpSnpgGrpSrcEntry_Object=MibTableRow
tnSapIgmpSnpgGrpSrcEntry=_TnSapIgmpSnpgGrpSrcEntry_Object((1,3,6,1,4,1,7483,6,1,2,24,2,3,1))
tnSapIgmpSnpgGrpSrcEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_L,_S),(0,_L,_R),(0,_I,_Z),(0,_I,_j))
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpSrcEntry.setStatus(_A)
_TnSapIgmpSnpgGrpSrcAddr_Type=IpAddress
_TnSapIgmpSnpgGrpSrcAddr_Object=MibTableColumn
tnSapIgmpSnpgGrpSrcAddr=_TnSapIgmpSnpgGrpSrcAddr_Object((1,3,6,1,4,1,7483,6,1,2,24,2,3,1,1),_TnSapIgmpSnpgGrpSrcAddr_Type())
tnSapIgmpSnpgGrpSrcAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpSrcAddr.setStatus(_A)
_TnSapIgmpSnpgGrpSrcType_Type=TmnxIgmpGroupType
_TnSapIgmpSnpgGrpSrcType_Object=MibTableColumn
tnSapIgmpSnpgGrpSrcType=_TnSapIgmpSnpgGrpSrcType_Object((1,3,6,1,4,1,7483,6,1,2,24,2,3,1,2),_TnSapIgmpSnpgGrpSrcType_Type())
tnSapIgmpSnpgGrpSrcType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpSrcType.setStatus(_A)
_TnSapIgmpSnpgGrpSrcUpTime_Type=TimeTicks
_TnSapIgmpSnpgGrpSrcUpTime_Object=MibTableColumn
tnSapIgmpSnpgGrpSrcUpTime=_TnSapIgmpSnpgGrpSrcUpTime_Object((1,3,6,1,4,1,7483,6,1,2,24,2,3,1,3),_TnSapIgmpSnpgGrpSrcUpTime_Type())
tnSapIgmpSnpgGrpSrcUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpSrcUpTime.setStatus(_A)
_TnSapIgmpSnpgGrpSrcExpiryTime_Type=Unsigned32
_TnSapIgmpSnpgGrpSrcExpiryTime_Object=MibTableColumn
tnSapIgmpSnpgGrpSrcExpiryTime=_TnSapIgmpSnpgGrpSrcExpiryTime_Object((1,3,6,1,4,1,7483,6,1,2,24,2,3,1,4),_TnSapIgmpSnpgGrpSrcExpiryTime_Type())
tnSapIgmpSnpgGrpSrcExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpSrcExpiryTime.setStatus(_A)
if mibBuilder.loadTexts:tnSapIgmpSnpgGrpSrcExpiryTime.setUnits(_H)
_TnSapIgmpSnpgStaticGrpSrcTable_Object=MibTable
tnSapIgmpSnpgStaticGrpSrcTable=_TnSapIgmpSnpgStaticGrpSrcTable_Object((1,3,6,1,4,1,7483,6,1,2,24,2,4))
if mibBuilder.loadTexts:tnSapIgmpSnpgStaticGrpSrcTable.setStatus(_A)
_TnSapIgmpSnpgStaticGrpSrcEntry_Object=MibTableRow
tnSapIgmpSnpgStaticGrpSrcEntry=_TnSapIgmpSnpgStaticGrpSrcEntry_Object((1,3,6,1,4,1,7483,6,1,2,24,2,4,1))
tnSapIgmpSnpgStaticGrpSrcEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_L,_S),(0,_L,_R),(0,_I,_k),(0,_I,_l))
if mibBuilder.loadTexts:tnSapIgmpSnpgStaticGrpSrcEntry.setStatus(_A)
_TnSapIgmpSnpgStaticGroupAddr_Type=IpAddress
_TnSapIgmpSnpgStaticGroupAddr_Object=MibTableColumn
tnSapIgmpSnpgStaticGroupAddr=_TnSapIgmpSnpgStaticGroupAddr_Object((1,3,6,1,4,1,7483,6,1,2,24,2,4,1,1),_TnSapIgmpSnpgStaticGroupAddr_Type())
tnSapIgmpSnpgStaticGroupAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:tnSapIgmpSnpgStaticGroupAddr.setStatus(_A)
_TnSapIgmpSnpgStaticSourceAddr_Type=IpAddress
_TnSapIgmpSnpgStaticSourceAddr_Object=MibTableColumn
tnSapIgmpSnpgStaticSourceAddr=_TnSapIgmpSnpgStaticSourceAddr_Object((1,3,6,1,4,1,7483,6,1,2,24,2,4,1,2),_TnSapIgmpSnpgStaticSourceAddr_Type())
tnSapIgmpSnpgStaticSourceAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:tnSapIgmpSnpgStaticSourceAddr.setStatus(_A)
_TnSapIgmpSnpgStaticRowstatus_Type=RowStatus
_TnSapIgmpSnpgStaticRowstatus_Object=MibTableColumn
tnSapIgmpSnpgStaticRowstatus=_TnSapIgmpSnpgStaticRowstatus_Object((1,3,6,1,4,1,7483,6,1,2,24,2,4,1,3),_TnSapIgmpSnpgStaticRowstatus_Type())
tnSapIgmpSnpgStaticRowstatus.setMaxAccess(_m)
if mibBuilder.loadTexts:tnSapIgmpSnpgStaticRowstatus.setStatus(_A)
_TnSapIgmpSnpgStaticLastChangeTime_Type=TimeStamp
_TnSapIgmpSnpgStaticLastChangeTime_Object=MibTableColumn
tnSapIgmpSnpgStaticLastChangeTime=_TnSapIgmpSnpgStaticLastChangeTime_Object((1,3,6,1,4,1,7483,6,1,2,24,2,4,1,4),_TnSapIgmpSnpgStaticLastChangeTime_Type())
tnSapIgmpSnpgStaticLastChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgStaticLastChangeTime.setStatus(_A)
_TnSapIgmpSnpgStatsTable_Object=MibTable
tnSapIgmpSnpgStatsTable=_TnSapIgmpSnpgStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5))
if mibBuilder.loadTexts:tnSapIgmpSnpgStatsTable.setStatus(_A)
_TnSapIgmpSnpgStatsEntry_Object=MibTableRow
tnSapIgmpSnpgStatsEntry=_TnSapIgmpSnpgStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1))
tnSapIgmpSnpgStatsEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_L,_S),(0,_L,_R))
if mibBuilder.loadTexts:tnSapIgmpSnpgStatsEntry.setStatus(_A)
_TnSapIgmpSnpgTxGenQueries_Type=Counter32
_TnSapIgmpSnpgTxGenQueries_Object=MibTableColumn
tnSapIgmpSnpgTxGenQueries=_TnSapIgmpSnpgTxGenQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,1),_TnSapIgmpSnpgTxGenQueries_Type())
tnSapIgmpSnpgTxGenQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgTxGenQueries.setStatus(_A)
_TnSapIgmpSnpgTxGrpSpecQueries_Type=Counter32
_TnSapIgmpSnpgTxGrpSpecQueries_Object=MibTableColumn
tnSapIgmpSnpgTxGrpSpecQueries=_TnSapIgmpSnpgTxGrpSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,2),_TnSapIgmpSnpgTxGrpSpecQueries_Type())
tnSapIgmpSnpgTxGrpSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgTxGrpSpecQueries.setStatus(_A)
_TnSapIgmpSnpgTxSrcSpecQueries_Type=Counter32
_TnSapIgmpSnpgTxSrcSpecQueries_Object=MibTableColumn
tnSapIgmpSnpgTxSrcSpecQueries=_TnSapIgmpSnpgTxSrcSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,3),_TnSapIgmpSnpgTxSrcSpecQueries_Type())
tnSapIgmpSnpgTxSrcSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgTxSrcSpecQueries.setStatus(_A)
_TnSapIgmpSnpgTxV1Reports_Type=Counter32
_TnSapIgmpSnpgTxV1Reports_Object=MibTableColumn
tnSapIgmpSnpgTxV1Reports=_TnSapIgmpSnpgTxV1Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,4),_TnSapIgmpSnpgTxV1Reports_Type())
tnSapIgmpSnpgTxV1Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgTxV1Reports.setStatus(_A)
_TnSapIgmpSnpgTxV2Reports_Type=Counter32
_TnSapIgmpSnpgTxV2Reports_Object=MibTableColumn
tnSapIgmpSnpgTxV2Reports=_TnSapIgmpSnpgTxV2Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,5),_TnSapIgmpSnpgTxV2Reports_Type())
tnSapIgmpSnpgTxV2Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgTxV2Reports.setStatus(_A)
_TnSapIgmpSnpgTxV3Reports_Type=Counter32
_TnSapIgmpSnpgTxV3Reports_Object=MibTableColumn
tnSapIgmpSnpgTxV3Reports=_TnSapIgmpSnpgTxV3Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,6),_TnSapIgmpSnpgTxV3Reports_Type())
tnSapIgmpSnpgTxV3Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgTxV3Reports.setStatus(_A)
_TnSapIgmpSnpgTxV2Leaves_Type=Counter32
_TnSapIgmpSnpgTxV2Leaves_Object=MibTableColumn
tnSapIgmpSnpgTxV2Leaves=_TnSapIgmpSnpgTxV2Leaves_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,7),_TnSapIgmpSnpgTxV2Leaves_Type())
tnSapIgmpSnpgTxV2Leaves.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgTxV2Leaves.setStatus(_A)
_TnSapIgmpSnpgRxGenQueries_Type=Counter32
_TnSapIgmpSnpgRxGenQueries_Object=MibTableColumn
tnSapIgmpSnpgRxGenQueries=_TnSapIgmpSnpgRxGenQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,8),_TnSapIgmpSnpgRxGenQueries_Type())
tnSapIgmpSnpgRxGenQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxGenQueries.setStatus(_A)
_TnSapIgmpSnpgRxGrpSpecQueries_Type=Counter32
_TnSapIgmpSnpgRxGrpSpecQueries_Object=MibTableColumn
tnSapIgmpSnpgRxGrpSpecQueries=_TnSapIgmpSnpgRxGrpSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,9),_TnSapIgmpSnpgRxGrpSpecQueries_Type())
tnSapIgmpSnpgRxGrpSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxGrpSpecQueries.setStatus(_A)
_TnSapIgmpSnpgRxSrcSpecQueries_Type=Counter32
_TnSapIgmpSnpgRxSrcSpecQueries_Object=MibTableColumn
tnSapIgmpSnpgRxSrcSpecQueries=_TnSapIgmpSnpgRxSrcSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,10),_TnSapIgmpSnpgRxSrcSpecQueries_Type())
tnSapIgmpSnpgRxSrcSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxSrcSpecQueries.setStatus(_A)
_TnSapIgmpSnpgRxV1Reports_Type=Counter32
_TnSapIgmpSnpgRxV1Reports_Object=MibTableColumn
tnSapIgmpSnpgRxV1Reports=_TnSapIgmpSnpgRxV1Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,11),_TnSapIgmpSnpgRxV1Reports_Type())
tnSapIgmpSnpgRxV1Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxV1Reports.setStatus(_A)
_TnSapIgmpSnpgRxV2Reports_Type=Counter32
_TnSapIgmpSnpgRxV2Reports_Object=MibTableColumn
tnSapIgmpSnpgRxV2Reports=_TnSapIgmpSnpgRxV2Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,12),_TnSapIgmpSnpgRxV2Reports_Type())
tnSapIgmpSnpgRxV2Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxV2Reports.setStatus(_A)
_TnSapIgmpSnpgRxV3Reports_Type=Counter32
_TnSapIgmpSnpgRxV3Reports_Object=MibTableColumn
tnSapIgmpSnpgRxV3Reports=_TnSapIgmpSnpgRxV3Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,13),_TnSapIgmpSnpgRxV3Reports_Type())
tnSapIgmpSnpgRxV3Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxV3Reports.setStatus(_A)
_TnSapIgmpSnpgRxV2Leaves_Type=Counter32
_TnSapIgmpSnpgRxV2Leaves_Object=MibTableColumn
tnSapIgmpSnpgRxV2Leaves=_TnSapIgmpSnpgRxV2Leaves_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,14),_TnSapIgmpSnpgRxV2Leaves_Type())
tnSapIgmpSnpgRxV2Leaves.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxV2Leaves.setStatus(_A)
_TnSapIgmpSnpgRxUnknownType_Type=Counter32
_TnSapIgmpSnpgRxUnknownType_Object=MibTableColumn
tnSapIgmpSnpgRxUnknownType=_TnSapIgmpSnpgRxUnknownType_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,15),_TnSapIgmpSnpgRxUnknownType_Type())
tnSapIgmpSnpgRxUnknownType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxUnknownType.setStatus(_A)
_TnSapIgmpSnpgFwdGenQueries_Type=Counter32
_TnSapIgmpSnpgFwdGenQueries_Object=MibTableColumn
tnSapIgmpSnpgFwdGenQueries=_TnSapIgmpSnpgFwdGenQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,16),_TnSapIgmpSnpgFwdGenQueries_Type())
tnSapIgmpSnpgFwdGenQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgFwdGenQueries.setStatus(_A)
_TnSapIgmpSnpgFwdGrpSpecQueries_Type=Counter32
_TnSapIgmpSnpgFwdGrpSpecQueries_Object=MibTableColumn
tnSapIgmpSnpgFwdGrpSpecQueries=_TnSapIgmpSnpgFwdGrpSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,17),_TnSapIgmpSnpgFwdGrpSpecQueries_Type())
tnSapIgmpSnpgFwdGrpSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgFwdGrpSpecQueries.setStatus(_A)
_TnSapIgmpSnpgFwdSrcSpecQueries_Type=Counter32
_TnSapIgmpSnpgFwdSrcSpecQueries_Object=MibTableColumn
tnSapIgmpSnpgFwdSrcSpecQueries=_TnSapIgmpSnpgFwdSrcSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,18),_TnSapIgmpSnpgFwdSrcSpecQueries_Type())
tnSapIgmpSnpgFwdSrcSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgFwdSrcSpecQueries.setStatus(_A)
_TnSapIgmpSnpgFwdV1Reports_Type=Counter32
_TnSapIgmpSnpgFwdV1Reports_Object=MibTableColumn
tnSapIgmpSnpgFwdV1Reports=_TnSapIgmpSnpgFwdV1Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,19),_TnSapIgmpSnpgFwdV1Reports_Type())
tnSapIgmpSnpgFwdV1Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgFwdV1Reports.setStatus(_A)
_TnSapIgmpSnpgFwdV2Reports_Type=Counter32
_TnSapIgmpSnpgFwdV2Reports_Object=MibTableColumn
tnSapIgmpSnpgFwdV2Reports=_TnSapIgmpSnpgFwdV2Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,20),_TnSapIgmpSnpgFwdV2Reports_Type())
tnSapIgmpSnpgFwdV2Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgFwdV2Reports.setStatus(_A)
_TnSapIgmpSnpgFwdV3Reports_Type=Counter32
_TnSapIgmpSnpgFwdV3Reports_Object=MibTableColumn
tnSapIgmpSnpgFwdV3Reports=_TnSapIgmpSnpgFwdV3Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,21),_TnSapIgmpSnpgFwdV3Reports_Type())
tnSapIgmpSnpgFwdV3Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgFwdV3Reports.setStatus(_A)
_TnSapIgmpSnpgFwdV2Leaves_Type=Counter32
_TnSapIgmpSnpgFwdV2Leaves_Object=MibTableColumn
tnSapIgmpSnpgFwdV2Leaves=_TnSapIgmpSnpgFwdV2Leaves_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,22),_TnSapIgmpSnpgFwdV2Leaves_Type())
tnSapIgmpSnpgFwdV2Leaves.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgFwdV2Leaves.setStatus(_A)
_TnSapIgmpSnpgFwdUnknownType_Type=Counter32
_TnSapIgmpSnpgFwdUnknownType_Object=MibTableColumn
tnSapIgmpSnpgFwdUnknownType=_TnSapIgmpSnpgFwdUnknownType_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,23),_TnSapIgmpSnpgFwdUnknownType_Type())
tnSapIgmpSnpgFwdUnknownType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgFwdUnknownType.setStatus(_A)
_TnSapIgmpSnpgRxBadLenPkts_Type=Counter32
_TnSapIgmpSnpgRxBadLenPkts_Object=MibTableColumn
tnSapIgmpSnpgRxBadLenPkts=_TnSapIgmpSnpgRxBadLenPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,24),_TnSapIgmpSnpgRxBadLenPkts_Type())
tnSapIgmpSnpgRxBadLenPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxBadLenPkts.setStatus(_A)
_TnSapIgmpSnpgRxBadIpChksmPkts_Type=Counter32
_TnSapIgmpSnpgRxBadIpChksmPkts_Object=MibTableColumn
tnSapIgmpSnpgRxBadIpChksmPkts=_TnSapIgmpSnpgRxBadIpChksmPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,25),_TnSapIgmpSnpgRxBadIpChksmPkts_Type())
tnSapIgmpSnpgRxBadIpChksmPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxBadIpChksmPkts.setStatus(_A)
_TnSapIgmpSnpgRxBadIgmpChksmPkts_Type=Counter32
_TnSapIgmpSnpgRxBadIgmpChksmPkts_Object=MibTableColumn
tnSapIgmpSnpgRxBadIgmpChksmPkts=_TnSapIgmpSnpgRxBadIgmpChksmPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,26),_TnSapIgmpSnpgRxBadIgmpChksmPkts_Type())
tnSapIgmpSnpgRxBadIgmpChksmPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxBadIgmpChksmPkts.setStatus(_A)
_TnSapIgmpSnpgRxBadEncodedPkts_Type=Counter32
_TnSapIgmpSnpgRxBadEncodedPkts_Object=MibTableColumn
tnSapIgmpSnpgRxBadEncodedPkts=_TnSapIgmpSnpgRxBadEncodedPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,27),_TnSapIgmpSnpgRxBadEncodedPkts_Type())
tnSapIgmpSnpgRxBadEncodedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxBadEncodedPkts.setStatus(_A)
_TnSapIgmpSnpgRxNoRtrAlertPkts_Type=Counter32
_TnSapIgmpSnpgRxNoRtrAlertPkts_Object=MibTableColumn
tnSapIgmpSnpgRxNoRtrAlertPkts=_TnSapIgmpSnpgRxNoRtrAlertPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,28),_TnSapIgmpSnpgRxNoRtrAlertPkts_Type())
tnSapIgmpSnpgRxNoRtrAlertPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxNoRtrAlertPkts.setStatus(_A)
_TnSapIgmpSnpgRxZeroSrcAdrPkts_Type=Counter32
_TnSapIgmpSnpgRxZeroSrcAdrPkts_Object=MibTableColumn
tnSapIgmpSnpgRxZeroSrcAdrPkts=_TnSapIgmpSnpgRxZeroSrcAdrPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,29),_TnSapIgmpSnpgRxZeroSrcAdrPkts_Type())
tnSapIgmpSnpgRxZeroSrcAdrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxZeroSrcAdrPkts.setStatus(_A)
_TnSapIgmpSnpgSendQueryCfgDrops_Type=Counter32
_TnSapIgmpSnpgSendQueryCfgDrops_Object=MibTableColumn
tnSapIgmpSnpgSendQueryCfgDrops=_TnSapIgmpSnpgSendQueryCfgDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,30),_TnSapIgmpSnpgSendQueryCfgDrops_Type())
tnSapIgmpSnpgSendQueryCfgDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgSendQueryCfgDrops.setStatus(_A)
_TnSapIgmpSnpgImportPolicyDrops_Type=Counter32
_TnSapIgmpSnpgImportPolicyDrops_Object=MibTableColumn
tnSapIgmpSnpgImportPolicyDrops=_TnSapIgmpSnpgImportPolicyDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,31),_TnSapIgmpSnpgImportPolicyDrops_Type())
tnSapIgmpSnpgImportPolicyDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgImportPolicyDrops.setStatus(_A)
_TnSapIgmpSnpgMaxNumGroupsDrops_Type=Counter32
_TnSapIgmpSnpgMaxNumGroupsDrops_Object=MibTableColumn
tnSapIgmpSnpgMaxNumGroupsDrops=_TnSapIgmpSnpgMaxNumGroupsDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,32),_TnSapIgmpSnpgMaxNumGroupsDrops_Type())
tnSapIgmpSnpgMaxNumGroupsDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgMaxNumGroupsDrops.setStatus(_A)
_TnSapIgmpSnpgMvrFromVplsCfgDrops_Type=Counter32
_TnSapIgmpSnpgMvrFromVplsCfgDrops_Object=MibTableColumn
tnSapIgmpSnpgMvrFromVplsCfgDrops=_TnSapIgmpSnpgMvrFromVplsCfgDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,33),_TnSapIgmpSnpgMvrFromVplsCfgDrops_Type())
tnSapIgmpSnpgMvrFromVplsCfgDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgMvrFromVplsCfgDrops.setStatus(_A)
_TnSapIgmpSnpgMvrToSapCfgDrops_Type=Counter32
_TnSapIgmpSnpgMvrToSapCfgDrops_Object=MibTableColumn
tnSapIgmpSnpgMvrToSapCfgDrops=_TnSapIgmpSnpgMvrToSapCfgDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,34),_TnSapIgmpSnpgMvrToSapCfgDrops_Type())
tnSapIgmpSnpgMvrToSapCfgDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgMvrToSapCfgDrops.setStatus(_A)
_TnSapIgmpSnpgRxWrongVersionPkts_Type=Counter32
_TnSapIgmpSnpgRxWrongVersionPkts_Object=MibTableColumn
tnSapIgmpSnpgRxWrongVersionPkts=_TnSapIgmpSnpgRxWrongVersionPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,35),_TnSapIgmpSnpgRxWrongVersionPkts_Type())
tnSapIgmpSnpgRxWrongVersionPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxWrongVersionPkts.setStatus(_A)
_TnSapIgmpSnpgMcacPolicyDrops_Type=Counter32
_TnSapIgmpSnpgMcacPolicyDrops_Object=MibTableColumn
tnSapIgmpSnpgMcacPolicyDrops=_TnSapIgmpSnpgMcacPolicyDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,36),_TnSapIgmpSnpgMcacPolicyDrops_Type())
tnSapIgmpSnpgMcacPolicyDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgMcacPolicyDrops.setStatus(_A)
_TnSapIgmpSnpgMcsFailures_Type=Counter32
_TnSapIgmpSnpgMcsFailures_Object=MibTableColumn
tnSapIgmpSnpgMcsFailures=_TnSapIgmpSnpgMcsFailures_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,37),_TnSapIgmpSnpgMcsFailures_Type())
tnSapIgmpSnpgMcsFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgMcsFailures.setStatus(_A)
_TnSapIgmpSnpgRxLocalScopePkts_Type=Counter32
_TnSapIgmpSnpgRxLocalScopePkts_Object=MibTableColumn
tnSapIgmpSnpgRxLocalScopePkts=_TnSapIgmpSnpgRxLocalScopePkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,38),_TnSapIgmpSnpgRxLocalScopePkts_Type())
tnSapIgmpSnpgRxLocalScopePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxLocalScopePkts.setStatus(_A)
_TnSapIgmpSnpgRxRsvdScopePkts_Type=Counter32
_TnSapIgmpSnpgRxRsvdScopePkts_Object=MibTableColumn
tnSapIgmpSnpgRxRsvdScopePkts=_TnSapIgmpSnpgRxRsvdScopePkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,39),_TnSapIgmpSnpgRxRsvdScopePkts_Type())
tnSapIgmpSnpgRxRsvdScopePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxRsvdScopePkts.setStatus(_A)
_TnSapIgmpSnpgMaxNumSourcesDrops_Type=Counter32
_TnSapIgmpSnpgMaxNumSourcesDrops_Object=MibTableColumn
tnSapIgmpSnpgMaxNumSourcesDrops=_TnSapIgmpSnpgMaxNumSourcesDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,40),_TnSapIgmpSnpgMaxNumSourcesDrops_Type())
tnSapIgmpSnpgMaxNumSourcesDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgMaxNumSourcesDrops.setStatus(_A)
_TnSapIgmpSnpgNumGrps_Type=Counter32
_TnSapIgmpSnpgNumGrps_Object=MibTableColumn
tnSapIgmpSnpgNumGrps=_TnSapIgmpSnpgNumGrps_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,41),_TnSapIgmpSnpgNumGrps_Type())
tnSapIgmpSnpgNumGrps.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgNumGrps.setStatus(_A)
_TnSapIgmpSnpgRxQueryDrops_Type=Counter32
_TnSapIgmpSnpgRxQueryDrops_Object=MibTableColumn
tnSapIgmpSnpgRxQueryDrops=_TnSapIgmpSnpgRxQueryDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,2,5,1,42),_TnSapIgmpSnpgRxQueryDrops_Type())
tnSapIgmpSnpgRxQueryDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapIgmpSnpgRxQueryDrops.setStatus(_A)
_TnSvcIgmpSnpgStatsTable_Object=MibTable
tnSvcIgmpSnpgStatsTable=_TnSvcIgmpSnpgStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6))
if mibBuilder.loadTexts:tnSvcIgmpSnpgStatsTable.setStatus(_A)
_TnSvcIgmpSnpgStatsEntry_Object=MibTableRow
tnSvcIgmpSnpgStatsEntry=_TnSvcIgmpSnpgStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1))
tnSvcIgmpSnpgStatsEntry.setIndexNames((0,_F,_G),(0,_D,_E))
if mibBuilder.loadTexts:tnSvcIgmpSnpgStatsEntry.setStatus(_A)
_TnSvcIgmpSnpgTxGenQueries_Type=Counter32
_TnSvcIgmpSnpgTxGenQueries_Object=MibTableColumn
tnSvcIgmpSnpgTxGenQueries=_TnSvcIgmpSnpgTxGenQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,1),_TnSvcIgmpSnpgTxGenQueries_Type())
tnSvcIgmpSnpgTxGenQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgTxGenQueries.setStatus(_A)
_TnSvcIgmpSnpgTxGrpSpecQueries_Type=Counter32
_TnSvcIgmpSnpgTxGrpSpecQueries_Object=MibTableColumn
tnSvcIgmpSnpgTxGrpSpecQueries=_TnSvcIgmpSnpgTxGrpSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,2),_TnSvcIgmpSnpgTxGrpSpecQueries_Type())
tnSvcIgmpSnpgTxGrpSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgTxGrpSpecQueries.setStatus(_A)
_TnSvcIgmpSnpgTxSrcSpecQueries_Type=Counter32
_TnSvcIgmpSnpgTxSrcSpecQueries_Object=MibTableColumn
tnSvcIgmpSnpgTxSrcSpecQueries=_TnSvcIgmpSnpgTxSrcSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,3),_TnSvcIgmpSnpgTxSrcSpecQueries_Type())
tnSvcIgmpSnpgTxSrcSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgTxSrcSpecQueries.setStatus(_A)
_TnSvcIgmpSnpgTxV1Reports_Type=Counter32
_TnSvcIgmpSnpgTxV1Reports_Object=MibTableColumn
tnSvcIgmpSnpgTxV1Reports=_TnSvcIgmpSnpgTxV1Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,4),_TnSvcIgmpSnpgTxV1Reports_Type())
tnSvcIgmpSnpgTxV1Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgTxV1Reports.setStatus(_A)
_TnSvcIgmpSnpgTxV2Reports_Type=Counter32
_TnSvcIgmpSnpgTxV2Reports_Object=MibTableColumn
tnSvcIgmpSnpgTxV2Reports=_TnSvcIgmpSnpgTxV2Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,5),_TnSvcIgmpSnpgTxV2Reports_Type())
tnSvcIgmpSnpgTxV2Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgTxV2Reports.setStatus(_A)
_TnSvcIgmpSnpgTxV3Reports_Type=Counter32
_TnSvcIgmpSnpgTxV3Reports_Object=MibTableColumn
tnSvcIgmpSnpgTxV3Reports=_TnSvcIgmpSnpgTxV3Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,6),_TnSvcIgmpSnpgTxV3Reports_Type())
tnSvcIgmpSnpgTxV3Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgTxV3Reports.setStatus(_A)
_TnSvcIgmpSnpgTxV2Leaves_Type=Counter32
_TnSvcIgmpSnpgTxV2Leaves_Object=MibTableColumn
tnSvcIgmpSnpgTxV2Leaves=_TnSvcIgmpSnpgTxV2Leaves_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,7),_TnSvcIgmpSnpgTxV2Leaves_Type())
tnSvcIgmpSnpgTxV2Leaves.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgTxV2Leaves.setStatus(_A)
_TnSvcIgmpSnpgRxGenQueries_Type=Counter32
_TnSvcIgmpSnpgRxGenQueries_Object=MibTableColumn
tnSvcIgmpSnpgRxGenQueries=_TnSvcIgmpSnpgRxGenQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,8),_TnSvcIgmpSnpgRxGenQueries_Type())
tnSvcIgmpSnpgRxGenQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxGenQueries.setStatus(_A)
_TnSvcIgmpSnpgRxGrpSpecQueries_Type=Counter32
_TnSvcIgmpSnpgRxGrpSpecQueries_Object=MibTableColumn
tnSvcIgmpSnpgRxGrpSpecQueries=_TnSvcIgmpSnpgRxGrpSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,9),_TnSvcIgmpSnpgRxGrpSpecQueries_Type())
tnSvcIgmpSnpgRxGrpSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxGrpSpecQueries.setStatus(_A)
_TnSvcIgmpSnpgRxSrcSpecQueries_Type=Counter32
_TnSvcIgmpSnpgRxSrcSpecQueries_Object=MibTableColumn
tnSvcIgmpSnpgRxSrcSpecQueries=_TnSvcIgmpSnpgRxSrcSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,10),_TnSvcIgmpSnpgRxSrcSpecQueries_Type())
tnSvcIgmpSnpgRxSrcSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxSrcSpecQueries.setStatus(_A)
_TnSvcIgmpSnpgRxV1Reports_Type=Counter32
_TnSvcIgmpSnpgRxV1Reports_Object=MibTableColumn
tnSvcIgmpSnpgRxV1Reports=_TnSvcIgmpSnpgRxV1Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,11),_TnSvcIgmpSnpgRxV1Reports_Type())
tnSvcIgmpSnpgRxV1Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxV1Reports.setStatus(_A)
_TnSvcIgmpSnpgRxV2Reports_Type=Counter32
_TnSvcIgmpSnpgRxV2Reports_Object=MibTableColumn
tnSvcIgmpSnpgRxV2Reports=_TnSvcIgmpSnpgRxV2Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,12),_TnSvcIgmpSnpgRxV2Reports_Type())
tnSvcIgmpSnpgRxV2Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxV2Reports.setStatus(_A)
_TnSvcIgmpSnpgRxV3Reports_Type=Counter32
_TnSvcIgmpSnpgRxV3Reports_Object=MibTableColumn
tnSvcIgmpSnpgRxV3Reports=_TnSvcIgmpSnpgRxV3Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,13),_TnSvcIgmpSnpgRxV3Reports_Type())
tnSvcIgmpSnpgRxV3Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxV3Reports.setStatus(_A)
_TnSvcIgmpSnpgRxV2Leaves_Type=Counter32
_TnSvcIgmpSnpgRxV2Leaves_Object=MibTableColumn
tnSvcIgmpSnpgRxV2Leaves=_TnSvcIgmpSnpgRxV2Leaves_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,14),_TnSvcIgmpSnpgRxV2Leaves_Type())
tnSvcIgmpSnpgRxV2Leaves.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxV2Leaves.setStatus(_A)
_TnSvcIgmpSnpgRxUnknownType_Type=Counter32
_TnSvcIgmpSnpgRxUnknownType_Object=MibTableColumn
tnSvcIgmpSnpgRxUnknownType=_TnSvcIgmpSnpgRxUnknownType_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,15),_TnSvcIgmpSnpgRxUnknownType_Type())
tnSvcIgmpSnpgRxUnknownType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxUnknownType.setStatus(_A)
_TnSvcIgmpSnpgFwdGenQueries_Type=Counter32
_TnSvcIgmpSnpgFwdGenQueries_Object=MibTableColumn
tnSvcIgmpSnpgFwdGenQueries=_TnSvcIgmpSnpgFwdGenQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,16),_TnSvcIgmpSnpgFwdGenQueries_Type())
tnSvcIgmpSnpgFwdGenQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgFwdGenQueries.setStatus(_A)
_TnSvcIgmpSnpgFwdGrpSpecQueries_Type=Counter32
_TnSvcIgmpSnpgFwdGrpSpecQueries_Object=MibTableColumn
tnSvcIgmpSnpgFwdGrpSpecQueries=_TnSvcIgmpSnpgFwdGrpSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,17),_TnSvcIgmpSnpgFwdGrpSpecQueries_Type())
tnSvcIgmpSnpgFwdGrpSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgFwdGrpSpecQueries.setStatus(_A)
_TnSvcIgmpSnpgFwdSrcSpecQueries_Type=Counter32
_TnSvcIgmpSnpgFwdSrcSpecQueries_Object=MibTableColumn
tnSvcIgmpSnpgFwdSrcSpecQueries=_TnSvcIgmpSnpgFwdSrcSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,18),_TnSvcIgmpSnpgFwdSrcSpecQueries_Type())
tnSvcIgmpSnpgFwdSrcSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgFwdSrcSpecQueries.setStatus(_A)
_TnSvcIgmpSnpgFwdV1Reports_Type=Counter32
_TnSvcIgmpSnpgFwdV1Reports_Object=MibTableColumn
tnSvcIgmpSnpgFwdV1Reports=_TnSvcIgmpSnpgFwdV1Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,19),_TnSvcIgmpSnpgFwdV1Reports_Type())
tnSvcIgmpSnpgFwdV1Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgFwdV1Reports.setStatus(_A)
_TnSvcIgmpSnpgFwdV2Reports_Type=Counter32
_TnSvcIgmpSnpgFwdV2Reports_Object=MibTableColumn
tnSvcIgmpSnpgFwdV2Reports=_TnSvcIgmpSnpgFwdV2Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,20),_TnSvcIgmpSnpgFwdV2Reports_Type())
tnSvcIgmpSnpgFwdV2Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgFwdV2Reports.setStatus(_A)
_TnSvcIgmpSnpgFwdV3Reports_Type=Counter32
_TnSvcIgmpSnpgFwdV3Reports_Object=MibTableColumn
tnSvcIgmpSnpgFwdV3Reports=_TnSvcIgmpSnpgFwdV3Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,21),_TnSvcIgmpSnpgFwdV3Reports_Type())
tnSvcIgmpSnpgFwdV3Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgFwdV3Reports.setStatus(_A)
_TnSvcIgmpSnpgFwdV2Leaves_Type=Counter32
_TnSvcIgmpSnpgFwdV2Leaves_Object=MibTableColumn
tnSvcIgmpSnpgFwdV2Leaves=_TnSvcIgmpSnpgFwdV2Leaves_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,22),_TnSvcIgmpSnpgFwdV2Leaves_Type())
tnSvcIgmpSnpgFwdV2Leaves.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgFwdV2Leaves.setStatus(_A)
_TnSvcIgmpSnpgFwdUnknownType_Type=Counter32
_TnSvcIgmpSnpgFwdUnknownType_Object=MibTableColumn
tnSvcIgmpSnpgFwdUnknownType=_TnSvcIgmpSnpgFwdUnknownType_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,23),_TnSvcIgmpSnpgFwdUnknownType_Type())
tnSvcIgmpSnpgFwdUnknownType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgFwdUnknownType.setStatus(_A)
_TnSvcIgmpSnpgRxBadLenPkts_Type=Counter32
_TnSvcIgmpSnpgRxBadLenPkts_Object=MibTableColumn
tnSvcIgmpSnpgRxBadLenPkts=_TnSvcIgmpSnpgRxBadLenPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,24),_TnSvcIgmpSnpgRxBadLenPkts_Type())
tnSvcIgmpSnpgRxBadLenPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxBadLenPkts.setStatus(_A)
_TnSvcIgmpSnpgRxBadIpChksmPkts_Type=Counter32
_TnSvcIgmpSnpgRxBadIpChksmPkts_Object=MibTableColumn
tnSvcIgmpSnpgRxBadIpChksmPkts=_TnSvcIgmpSnpgRxBadIpChksmPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,25),_TnSvcIgmpSnpgRxBadIpChksmPkts_Type())
tnSvcIgmpSnpgRxBadIpChksmPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxBadIpChksmPkts.setStatus(_A)
_TnSvcIgmpSnpgRxBadIgmpChksmPkts_Type=Counter32
_TnSvcIgmpSnpgRxBadIgmpChksmPkts_Object=MibTableColumn
tnSvcIgmpSnpgRxBadIgmpChksmPkts=_TnSvcIgmpSnpgRxBadIgmpChksmPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,26),_TnSvcIgmpSnpgRxBadIgmpChksmPkts_Type())
tnSvcIgmpSnpgRxBadIgmpChksmPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxBadIgmpChksmPkts.setStatus(_A)
_TnSvcIgmpSnpgRxBadEncodedPkts_Type=Counter32
_TnSvcIgmpSnpgRxBadEncodedPkts_Object=MibTableColumn
tnSvcIgmpSnpgRxBadEncodedPkts=_TnSvcIgmpSnpgRxBadEncodedPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,27),_TnSvcIgmpSnpgRxBadEncodedPkts_Type())
tnSvcIgmpSnpgRxBadEncodedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxBadEncodedPkts.setStatus(_A)
_TnSvcIgmpSnpgRxNoRtrAlertPkts_Type=Counter32
_TnSvcIgmpSnpgRxNoRtrAlertPkts_Object=MibTableColumn
tnSvcIgmpSnpgRxNoRtrAlertPkts=_TnSvcIgmpSnpgRxNoRtrAlertPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,28),_TnSvcIgmpSnpgRxNoRtrAlertPkts_Type())
tnSvcIgmpSnpgRxNoRtrAlertPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxNoRtrAlertPkts.setStatus(_A)
_TnSvcIgmpSnpgRxZeroSrcAdrPkts_Type=Counter32
_TnSvcIgmpSnpgRxZeroSrcAdrPkts_Object=MibTableColumn
tnSvcIgmpSnpgRxZeroSrcAdrPkts=_TnSvcIgmpSnpgRxZeroSrcAdrPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,29),_TnSvcIgmpSnpgRxZeroSrcAdrPkts_Type())
tnSvcIgmpSnpgRxZeroSrcAdrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxZeroSrcAdrPkts.setStatus(_A)
_TnSvcIgmpSnpgSendQueryCfgDrops_Type=Counter32
_TnSvcIgmpSnpgSendQueryCfgDrops_Object=MibTableColumn
tnSvcIgmpSnpgSendQueryCfgDrops=_TnSvcIgmpSnpgSendQueryCfgDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,30),_TnSvcIgmpSnpgSendQueryCfgDrops_Type())
tnSvcIgmpSnpgSendQueryCfgDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgSendQueryCfgDrops.setStatus(_A)
_TnSvcIgmpSnpgImportPolicyDrops_Type=Counter32
_TnSvcIgmpSnpgImportPolicyDrops_Object=MibTableColumn
tnSvcIgmpSnpgImportPolicyDrops=_TnSvcIgmpSnpgImportPolicyDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,31),_TnSvcIgmpSnpgImportPolicyDrops_Type())
tnSvcIgmpSnpgImportPolicyDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgImportPolicyDrops.setStatus(_A)
_TnSvcIgmpSnpgMaxNumGroupsDrops_Type=Counter32
_TnSvcIgmpSnpgMaxNumGroupsDrops_Object=MibTableColumn
tnSvcIgmpSnpgMaxNumGroupsDrops=_TnSvcIgmpSnpgMaxNumGroupsDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,32),_TnSvcIgmpSnpgMaxNumGroupsDrops_Type())
tnSvcIgmpSnpgMaxNumGroupsDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgMaxNumGroupsDrops.setStatus(_A)
_TnSvcIgmpSnpgMvrFromVplsCfgDrops_Type=Counter32
_TnSvcIgmpSnpgMvrFromVplsCfgDrops_Object=MibTableColumn
tnSvcIgmpSnpgMvrFromVplsCfgDrops=_TnSvcIgmpSnpgMvrFromVplsCfgDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,33),_TnSvcIgmpSnpgMvrFromVplsCfgDrops_Type())
tnSvcIgmpSnpgMvrFromVplsCfgDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgMvrFromVplsCfgDrops.setStatus(_A)
_TnSvcIgmpSnpgMvrToSapCfgDrops_Type=Counter32
_TnSvcIgmpSnpgMvrToSapCfgDrops_Object=MibTableColumn
tnSvcIgmpSnpgMvrToSapCfgDrops=_TnSvcIgmpSnpgMvrToSapCfgDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,34),_TnSvcIgmpSnpgMvrToSapCfgDrops_Type())
tnSvcIgmpSnpgMvrToSapCfgDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgMvrToSapCfgDrops.setStatus(_A)
_TnSvcIgmpSnpgRxWrongVersionPkts_Type=Counter32
_TnSvcIgmpSnpgRxWrongVersionPkts_Object=MibTableColumn
tnSvcIgmpSnpgRxWrongVersionPkts=_TnSvcIgmpSnpgRxWrongVersionPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,35),_TnSvcIgmpSnpgRxWrongVersionPkts_Type())
tnSvcIgmpSnpgRxWrongVersionPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxWrongVersionPkts.setStatus(_A)
_TnSvcIgmpSnpgMcacPolicyDrops_Type=Counter32
_TnSvcIgmpSnpgMcacPolicyDrops_Object=MibTableColumn
tnSvcIgmpSnpgMcacPolicyDrops=_TnSvcIgmpSnpgMcacPolicyDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,36),_TnSvcIgmpSnpgMcacPolicyDrops_Type())
tnSvcIgmpSnpgMcacPolicyDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgMcacPolicyDrops.setStatus(_A)
_TnSvcIgmpSnpgMcsFailures_Type=Counter32
_TnSvcIgmpSnpgMcsFailures_Object=MibTableColumn
tnSvcIgmpSnpgMcsFailures=_TnSvcIgmpSnpgMcsFailures_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,37),_TnSvcIgmpSnpgMcsFailures_Type())
tnSvcIgmpSnpgMcsFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgMcsFailures.setStatus(_A)
_TnSvcIgmpSnpgRxLocalScopePkts_Type=Counter32
_TnSvcIgmpSnpgRxLocalScopePkts_Object=MibTableColumn
tnSvcIgmpSnpgRxLocalScopePkts=_TnSvcIgmpSnpgRxLocalScopePkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,38),_TnSvcIgmpSnpgRxLocalScopePkts_Type())
tnSvcIgmpSnpgRxLocalScopePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxLocalScopePkts.setStatus(_A)
_TnSvcIgmpSnpgRxRsvdScopePkts_Type=Counter32
_TnSvcIgmpSnpgRxRsvdScopePkts_Object=MibTableColumn
tnSvcIgmpSnpgRxRsvdScopePkts=_TnSvcIgmpSnpgRxRsvdScopePkts_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,39),_TnSvcIgmpSnpgRxRsvdScopePkts_Type())
tnSvcIgmpSnpgRxRsvdScopePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxRsvdScopePkts.setStatus(_A)
_TnSvcIgmpSnpgMaxNumSourcesDrops_Type=Counter32
_TnSvcIgmpSnpgMaxNumSourcesDrops_Object=MibTableColumn
tnSvcIgmpSnpgMaxNumSourcesDrops=_TnSvcIgmpSnpgMaxNumSourcesDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,40),_TnSvcIgmpSnpgMaxNumSourcesDrops_Type())
tnSvcIgmpSnpgMaxNumSourcesDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgMaxNumSourcesDrops.setStatus(_A)
_TnSvcIgmpSnpgNumGrps_Type=Counter32
_TnSvcIgmpSnpgNumGrps_Object=MibTableColumn
tnSvcIgmpSnpgNumGrps=_TnSvcIgmpSnpgNumGrps_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,41),_TnSvcIgmpSnpgNumGrps_Type())
tnSvcIgmpSnpgNumGrps.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgNumGrps.setStatus(_A)
_TnSvcIgmpSnpgRxQueryDrops_Type=Counter32
_TnSvcIgmpSnpgRxQueryDrops_Object=MibTableColumn
tnSvcIgmpSnpgRxQueryDrops=_TnSvcIgmpSnpgRxQueryDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,2,6,1,42),_TnSvcIgmpSnpgRxQueryDrops_Type())
tnSvcIgmpSnpgRxQueryDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpSnpgRxQueryDrops.setStatus(_A)
_TnIgmpSnoopingSapScalar1_Type=Unsigned32
_TnIgmpSnoopingSapScalar1_Object=MibScalar
tnIgmpSnoopingSapScalar1=_TnIgmpSnoopingSapScalar1_Object((1,3,6,1,4,1,7483,6,1,2,24,2,101),_TnIgmpSnoopingSapScalar1_Type())
tnIgmpSnoopingSapScalar1.setMaxAccess(_B)
if mibBuilder.loadTexts:tnIgmpSnoopingSapScalar1.setStatus(_A)
_TnIgmpSnoopingSapScalar2_Type=Unsigned32
_TnIgmpSnoopingSapScalar2_Object=MibScalar
tnIgmpSnoopingSapScalar2=_TnIgmpSnoopingSapScalar2_Object((1,3,6,1,4,1,7483,6,1,2,24,2,102),_TnIgmpSnoopingSapScalar2_Type())
tnIgmpSnoopingSapScalar2.setMaxAccess(_B)
if mibBuilder.loadTexts:tnIgmpSnoopingSapScalar2.setStatus(_A)
_TnIgmpSnoopingSdpBindObjs_ObjectIdentity=ObjectIdentity
tnIgmpSnoopingSdpBindObjs=_TnIgmpSnoopingSdpBindObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,24,3))
_TnSdpBindIgmpSnpgConfigTable_Object=MibTable
tnSdpBindIgmpSnpgConfigTable=_TnSdpBindIgmpSnpgConfigTable_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1))
if mibBuilder.loadTexts:tnSdpBindIgmpSnpgConfigTable.setStatus(_A)
_TnSdpBindIgmpSnpgConfigEntry_Object=MibTableRow
tnSdpBindIgmpSnpgConfigEntry=_TnSdpBindIgmpSnpgConfigEntry_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1))
tnSdpBindIgmpSnpgConfigEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_P,_Q))
if mibBuilder.loadTexts:tnSdpBindIgmpSnpgConfigEntry.setStatus(_A)
class _SdpBndIgmpSnpgCfgImportPlcy_Type(TPolicyStatementNameOrEmpty):defaultValue=OctetString('')
_SdpBndIgmpSnpgCfgImportPlcy_Type.__name__=_T
_SdpBndIgmpSnpgCfgImportPlcy_Object=MibTableColumn
sdpBndIgmpSnpgCfgImportPlcy=_SdpBndIgmpSnpgCfgImportPlcy_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,1),_SdpBndIgmpSnpgCfgImportPlcy_Type())
sdpBndIgmpSnpgCfgImportPlcy.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgImportPlcy.setStatus(_A)
class _SdpBndIgmpSnpgCfgFastLeave_Type(AlxIgmpSnpgAdminState):defaultValue=2
_SdpBndIgmpSnpgCfgFastLeave_Type.__name__=_O
_SdpBndIgmpSnpgCfgFastLeave_Object=MibTableColumn
sdpBndIgmpSnpgCfgFastLeave=_SdpBndIgmpSnpgCfgFastLeave_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,2),_SdpBndIgmpSnpgCfgFastLeave_Type())
sdpBndIgmpSnpgCfgFastLeave.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgFastLeave.setStatus(_A)
class _SdpBndIgmpSnpgCfgMRouter_Type(TruthValue):defaultValue=2
_SdpBndIgmpSnpgCfgMRouter_Type.__name__=_W
_SdpBndIgmpSnpgCfgMRouter_Object=MibTableColumn
sdpBndIgmpSnpgCfgMRouter=_SdpBndIgmpSnpgCfgMRouter_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,3),_SdpBndIgmpSnpgCfgMRouter_Type())
sdpBndIgmpSnpgCfgMRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMRouter.setStatus(_A)
class _SdpBndIgmpSnpgCfgSendQueries_Type(AlxIgmpSnpgAdminState):defaultValue=2
_SdpBndIgmpSnpgCfgSendQueries_Type.__name__=_O
_SdpBndIgmpSnpgCfgSendQueries_Object=MibTableColumn
sdpBndIgmpSnpgCfgSendQueries=_SdpBndIgmpSnpgCfgSendQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,4),_SdpBndIgmpSnpgCfgSendQueries_Type())
sdpBndIgmpSnpgCfgSendQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgSendQueries.setStatus(_A)
class _SdpBndIgmpSnpgCfgGenQueryIntvl_Type(Unsigned32):defaultValue=125;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,1024))
_SdpBndIgmpSnpgCfgGenQueryIntvl_Type.__name__=_J
_SdpBndIgmpSnpgCfgGenQueryIntvl_Object=MibTableColumn
sdpBndIgmpSnpgCfgGenQueryIntvl=_SdpBndIgmpSnpgCfgGenQueryIntvl_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,5),_SdpBndIgmpSnpgCfgGenQueryIntvl_Type())
sdpBndIgmpSnpgCfgGenQueryIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgGenQueryIntvl.setStatus(_A)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgGenQueryIntvl.setUnits(_H)
class _SdpBndIgmpSnpgCfgQueryRespIntvl_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_SdpBndIgmpSnpgCfgQueryRespIntvl_Type.__name__=_J
_SdpBndIgmpSnpgCfgQueryRespIntvl_Object=MibTableColumn
sdpBndIgmpSnpgCfgQueryRespIntvl=_SdpBndIgmpSnpgCfgQueryRespIntvl_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,6),_SdpBndIgmpSnpgCfgQueryRespIntvl_Type())
sdpBndIgmpSnpgCfgQueryRespIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgQueryRespIntvl.setStatus(_A)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgQueryRespIntvl.setUnits(_H)
class _SdpBndIgmpSnpgCfgRobustCount_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,7))
_SdpBndIgmpSnpgCfgRobustCount_Type.__name__=_J
_SdpBndIgmpSnpgCfgRobustCount_Object=MibTableColumn
sdpBndIgmpSnpgCfgRobustCount=_SdpBndIgmpSnpgCfgRobustCount_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,7),_SdpBndIgmpSnpgCfgRobustCount_Type())
sdpBndIgmpSnpgCfgRobustCount.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgRobustCount.setStatus(_A)
class _SdpBndIgmpSnpgCfgLastMembIntvl_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_SdpBndIgmpSnpgCfgLastMembIntvl_Type.__name__=_J
_SdpBndIgmpSnpgCfgLastMembIntvl_Object=MibTableColumn
sdpBndIgmpSnpgCfgLastMembIntvl=_SdpBndIgmpSnpgCfgLastMembIntvl_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,8),_SdpBndIgmpSnpgCfgLastMembIntvl_Type())
sdpBndIgmpSnpgCfgLastMembIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgLastMembIntvl.setStatus(_A)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgLastMembIntvl.setUnits(_U)
class _SdpBndIgmpSnpgCfgMaxNbrGrps_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2047))
_SdpBndIgmpSnpgCfgMaxNbrGrps_Type.__name__=_N
_SdpBndIgmpSnpgCfgMaxNbrGrps_Object=MibTableColumn
sdpBndIgmpSnpgCfgMaxNbrGrps=_SdpBndIgmpSnpgCfgMaxNbrGrps_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,9),_SdpBndIgmpSnpgCfgMaxNbrGrps_Type())
sdpBndIgmpSnpgCfgMaxNbrGrps.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMaxNbrGrps.setStatus(_A)
class _SdpBndIgmpSnpgCfgVersion_Type(TmnxIgmpVersion):defaultValue=3
_SdpBndIgmpSnpgCfgVersion_Type.__name__=_X
_SdpBndIgmpSnpgCfgVersion_Object=MibTableColumn
sdpBndIgmpSnpgCfgVersion=_SdpBndIgmpSnpgCfgVersion_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,10),_SdpBndIgmpSnpgCfgVersion_Type())
sdpBndIgmpSnpgCfgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgVersion.setStatus(_A)
class _SdpBndIgmpSnpgCfgMcacPolicyName_Type(TPolicyStatementNameOrEmpty):defaultValue=OctetString('')
_SdpBndIgmpSnpgCfgMcacPolicyName_Type.__name__=_T
_SdpBndIgmpSnpgCfgMcacPolicyName_Object=MibTableColumn
sdpBndIgmpSnpgCfgMcacPolicyName=_SdpBndIgmpSnpgCfgMcacPolicyName_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,11),_SdpBndIgmpSnpgCfgMcacPolicyName_Type())
sdpBndIgmpSnpgCfgMcacPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMcacPolicyName.setStatus(_A)
class _SdpBndIgmpSnpgCfgMcacUnconstBW_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_SdpBndIgmpSnpgCfgMcacUnconstBW_Type.__name__=_N
_SdpBndIgmpSnpgCfgMcacUnconstBW_Object=MibTableColumn
sdpBndIgmpSnpgCfgMcacUnconstBW=_SdpBndIgmpSnpgCfgMcacUnconstBW_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,12),_SdpBndIgmpSnpgCfgMcacUnconstBW_Type())
sdpBndIgmpSnpgCfgMcacUnconstBW.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMcacUnconstBW.setStatus(_A)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMcacUnconstBW.setUnits(_K)
class _SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Type.__name__=_N
_SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Object=MibTableColumn
sdpBndIgmpSnpgCfgMcacPrRsvMndBW=_SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,13),_SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Type())
sdpBndIgmpSnpgCfgMcacPrRsvMndBW.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMcacPrRsvMndBW.setStatus(_A)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMcacPrRsvMndBW.setUnits(_K)
_SdpBndIgmpSnpgCfgMcacinUseMndBw_Type=Unsigned32
_SdpBndIgmpSnpgCfgMcacinUseMndBw_Object=MibTableColumn
sdpBndIgmpSnpgCfgMcacinUseMndBw=_SdpBndIgmpSnpgCfgMcacinUseMndBw_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,14),_SdpBndIgmpSnpgCfgMcacinUseMndBw_Type())
sdpBndIgmpSnpgCfgMcacinUseMndBw.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMcacinUseMndBw.setStatus(_A)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMcacinUseMndBw.setUnits(_K)
_SdpBndIgmpSnpgCfgMcacinUseOplBw_Type=Unsigned32
_SdpBndIgmpSnpgCfgMcacinUseOplBw_Object=MibTableColumn
sdpBndIgmpSnpgCfgMcacinUseOplBw=_SdpBndIgmpSnpgCfgMcacinUseOplBw_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,15),_SdpBndIgmpSnpgCfgMcacinUseOplBw_Type())
sdpBndIgmpSnpgCfgMcacinUseOplBw.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMcacinUseOplBw.setStatus(_A)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMcacinUseOplBw.setUnits(_K)
_SdpBndIgmpSnpgCfgMcacAvailMndBw_Type=Unsigned32
_SdpBndIgmpSnpgCfgMcacAvailMndBw_Object=MibTableColumn
sdpBndIgmpSnpgCfgMcacAvailMndBw=_SdpBndIgmpSnpgCfgMcacAvailMndBw_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,16),_SdpBndIgmpSnpgCfgMcacAvailMndBw_Type())
sdpBndIgmpSnpgCfgMcacAvailMndBw.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMcacAvailMndBw.setStatus(_A)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMcacAvailMndBw.setUnits(_K)
_SdpBndIgmpSnpgCfgMcacAvailOplBw_Type=Unsigned32
_SdpBndIgmpSnpgCfgMcacAvailOplBw_Object=MibTableColumn
sdpBndIgmpSnpgCfgMcacAvailOplBw=_SdpBndIgmpSnpgCfgMcacAvailOplBw_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,17),_SdpBndIgmpSnpgCfgMcacAvailOplBw_Type())
sdpBndIgmpSnpgCfgMcacAvailOplBw.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMcacAvailOplBw.setStatus(_A)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMcacAvailOplBw.setUnits(_K)
_SdpBndIgmpSnpgCfgMcacValInTrans_Type=TruthValue
_SdpBndIgmpSnpgCfgMcacValInTrans_Object=MibTableColumn
sdpBndIgmpSnpgCfgMcacValInTrans=_SdpBndIgmpSnpgCfgMcacValInTrans_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,18),_SdpBndIgmpSnpgCfgMcacValInTrans_Type())
sdpBndIgmpSnpgCfgMcacValInTrans.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMcacValInTrans.setStatus(_A)
_SdpBndIgmpSnpgCfgLastChangeTime_Type=TimeStamp
_SdpBndIgmpSnpgCfgLastChangeTime_Object=MibTableColumn
sdpBndIgmpSnpgCfgLastChangeTime=_SdpBndIgmpSnpgCfgLastChangeTime_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,19),_SdpBndIgmpSnpgCfgLastChangeTime_Type())
sdpBndIgmpSnpgCfgLastChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgLastChangeTime.setStatus(_A)
class _SdpBndIgmpSnpgCfgMaxNbrSrcs_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_SdpBndIgmpSnpgCfgMaxNbrSrcs_Type.__name__=_J
_SdpBndIgmpSnpgCfgMaxNbrSrcs_Object=MibTableColumn
sdpBndIgmpSnpgCfgMaxNbrSrcs=_SdpBndIgmpSnpgCfgMaxNbrSrcs_Object((1,3,6,1,4,1,7483,6,1,2,24,3,1,1,20),_SdpBndIgmpSnpgCfgMaxNbrSrcs_Type())
sdpBndIgmpSnpgCfgMaxNbrSrcs.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBndIgmpSnpgCfgMaxNbrSrcs.setStatus(_A)
_TnSdpBindIgmpSnpgGroupTable_Object=MibTable
tnSdpBindIgmpSnpgGroupTable=_TnSdpBindIgmpSnpgGroupTable_Object((1,3,6,1,4,1,7483,6,1,2,24,3,2))
if mibBuilder.loadTexts:tnSdpBindIgmpSnpgGroupTable.setStatus(_A)
_TnSdpBindIgmpSnpgGroupEntry_Object=MibTableRow
tnSdpBindIgmpSnpgGroupEntry=_TnSdpBindIgmpSnpgGroupEntry_Object((1,3,6,1,4,1,7483,6,1,2,24,3,2,1))
tnSdpBindIgmpSnpgGroupEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_P,_Q),(0,_I,_a))
if mibBuilder.loadTexts:tnSdpBindIgmpSnpgGroupEntry.setStatus(_A)
_SdpBndIgmpSnpgGrpAddress_Type=IpAddress
_SdpBndIgmpSnpgGrpAddress_Object=MibTableColumn
sdpBndIgmpSnpgGrpAddress=_SdpBndIgmpSnpgGrpAddress_Object((1,3,6,1,4,1,7483,6,1,2,24,3,2,1,1),_SdpBndIgmpSnpgGrpAddress_Type())
sdpBndIgmpSnpgGrpAddress.setMaxAccess(_M)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpAddress.setStatus(_A)
_SdpBndIgmpSnpgGrpType_Type=TmnxIgmpGroupType
_SdpBndIgmpSnpgGrpType_Object=MibTableColumn
sdpBndIgmpSnpgGrpType=_SdpBndIgmpSnpgGrpType_Object((1,3,6,1,4,1,7483,6,1,2,24,3,2,1,2),_SdpBndIgmpSnpgGrpType_Type())
sdpBndIgmpSnpgGrpType.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpType.setStatus(_A)
_SdpBndIgmpSnpgGrpFilterMode_Type=TmnxIgmpGroupFilterMode
_SdpBndIgmpSnpgGrpFilterMode_Object=MibTableColumn
sdpBndIgmpSnpgGrpFilterMode=_SdpBndIgmpSnpgGrpFilterMode_Object((1,3,6,1,4,1,7483,6,1,2,24,3,2,1,3),_SdpBndIgmpSnpgGrpFilterMode_Type())
sdpBndIgmpSnpgGrpFilterMode.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpFilterMode.setStatus(_A)
_SdpBndIgmpSnpgGrpUpTime_Type=TimeTicks
_SdpBndIgmpSnpgGrpUpTime_Object=MibTableColumn
sdpBndIgmpSnpgGrpUpTime=_SdpBndIgmpSnpgGrpUpTime_Object((1,3,6,1,4,1,7483,6,1,2,24,3,2,1,4),_SdpBndIgmpSnpgGrpUpTime_Type())
sdpBndIgmpSnpgGrpUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpUpTime.setStatus(_A)
_SdpBndIgmpSnpgGrpExpiryTime_Type=Unsigned32
_SdpBndIgmpSnpgGrpExpiryTime_Object=MibTableColumn
sdpBndIgmpSnpgGrpExpiryTime=_SdpBndIgmpSnpgGrpExpiryTime_Object((1,3,6,1,4,1,7483,6,1,2,24,3,2,1,5),_SdpBndIgmpSnpgGrpExpiryTime_Type())
sdpBndIgmpSnpgGrpExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpExpiryTime.setStatus(_A)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpExpiryTime.setUnits(_H)
_SdpBndIgmpSnpgGrpCompatMode_Type=Unsigned32
_SdpBndIgmpSnpgGrpCompatMode_Object=MibTableColumn
sdpBndIgmpSnpgGrpCompatMode=_SdpBndIgmpSnpgGrpCompatMode_Object((1,3,6,1,4,1,7483,6,1,2,24,3,2,1,6),_SdpBndIgmpSnpgGrpCompatMode_Type())
sdpBndIgmpSnpgGrpCompatMode.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpCompatMode.setStatus(_A)
_SdpBndIgmpSnpgGrpV1HostExpTime_Type=Unsigned32
_SdpBndIgmpSnpgGrpV1HostExpTime_Object=MibTableColumn
sdpBndIgmpSnpgGrpV1HostExpTime=_SdpBndIgmpSnpgGrpV1HostExpTime_Object((1,3,6,1,4,1,7483,6,1,2,24,3,2,1,7),_SdpBndIgmpSnpgGrpV1HostExpTime_Type())
sdpBndIgmpSnpgGrpV1HostExpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpV1HostExpTime.setStatus(_A)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpV1HostExpTime.setUnits(_H)
_SdpBndIgmpSnpgGrpV2HostExpTime_Type=Unsigned32
_SdpBndIgmpSnpgGrpV2HostExpTime_Object=MibTableColumn
sdpBndIgmpSnpgGrpV2HostExpTime=_SdpBndIgmpSnpgGrpV2HostExpTime_Object((1,3,6,1,4,1,7483,6,1,2,24,3,2,1,8),_SdpBndIgmpSnpgGrpV2HostExpTime_Type())
sdpBndIgmpSnpgGrpV2HostExpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpV2HostExpTime.setStatus(_A)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpV2HostExpTime.setUnits(_H)
_SdpBndIgmpSnpgGrpNumSrc_Type=Counter32
_SdpBndIgmpSnpgGrpNumSrc_Object=MibTableColumn
sdpBndIgmpSnpgGrpNumSrc=_SdpBndIgmpSnpgGrpNumSrc_Object((1,3,6,1,4,1,7483,6,1,2,24,3,2,1,9),_SdpBndIgmpSnpgGrpNumSrc_Type())
sdpBndIgmpSnpgGrpNumSrc.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpNumSrc.setStatus(_A)
_TnSdpBindIgmpSnpgGrpSrcTable_Object=MibTable
tnSdpBindIgmpSnpgGrpSrcTable=_TnSdpBindIgmpSnpgGrpSrcTable_Object((1,3,6,1,4,1,7483,6,1,2,24,3,3))
if mibBuilder.loadTexts:tnSdpBindIgmpSnpgGrpSrcTable.setStatus(_A)
_TnSdpBindIgmpSnpgGrpSrcEntry_Object=MibTableRow
tnSdpBindIgmpSnpgGrpSrcEntry=_TnSdpBindIgmpSnpgGrpSrcEntry_Object((1,3,6,1,4,1,7483,6,1,2,24,3,3,1))
tnSdpBindIgmpSnpgGrpSrcEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_P,_Q),(0,_I,_a),(0,_I,_n))
if mibBuilder.loadTexts:tnSdpBindIgmpSnpgGrpSrcEntry.setStatus(_A)
_SdpBndIgmpSnpgGrpSrcAddr_Type=IpAddress
_SdpBndIgmpSnpgGrpSrcAddr_Object=MibTableColumn
sdpBndIgmpSnpgGrpSrcAddr=_SdpBndIgmpSnpgGrpSrcAddr_Object((1,3,6,1,4,1,7483,6,1,2,24,3,3,1,1),_SdpBndIgmpSnpgGrpSrcAddr_Type())
sdpBndIgmpSnpgGrpSrcAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpSrcAddr.setStatus(_A)
_SdpBndIgmpSnpgGrpSrcType_Type=TmnxIgmpGroupType
_SdpBndIgmpSnpgGrpSrcType_Object=MibTableColumn
sdpBndIgmpSnpgGrpSrcType=_SdpBndIgmpSnpgGrpSrcType_Object((1,3,6,1,4,1,7483,6,1,2,24,3,3,1,2),_SdpBndIgmpSnpgGrpSrcType_Type())
sdpBndIgmpSnpgGrpSrcType.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpSrcType.setStatus(_A)
_SdpBndIgmpSnpgGrpSrcUpTime_Type=TimeTicks
_SdpBndIgmpSnpgGrpSrcUpTime_Object=MibTableColumn
sdpBndIgmpSnpgGrpSrcUpTime=_SdpBndIgmpSnpgGrpSrcUpTime_Object((1,3,6,1,4,1,7483,6,1,2,24,3,3,1,3),_SdpBndIgmpSnpgGrpSrcUpTime_Type())
sdpBndIgmpSnpgGrpSrcUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpSrcUpTime.setStatus(_A)
_SdpBndIgmpSnpgGrpSrcExpiryTime_Type=Unsigned32
_SdpBndIgmpSnpgGrpSrcExpiryTime_Object=MibTableColumn
sdpBndIgmpSnpgGrpSrcExpiryTime=_SdpBndIgmpSnpgGrpSrcExpiryTime_Object((1,3,6,1,4,1,7483,6,1,2,24,3,3,1,4),_SdpBndIgmpSnpgGrpSrcExpiryTime_Type())
sdpBndIgmpSnpgGrpSrcExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpSrcExpiryTime.setStatus(_A)
if mibBuilder.loadTexts:sdpBndIgmpSnpgGrpSrcExpiryTime.setUnits(_H)
_TnSdpBindIgmpSnpgStaticGrpSrcTable_Object=MibTable
tnSdpBindIgmpSnpgStaticGrpSrcTable=_TnSdpBindIgmpSnpgStaticGrpSrcTable_Object((1,3,6,1,4,1,7483,6,1,2,24,3,4))
if mibBuilder.loadTexts:tnSdpBindIgmpSnpgStaticGrpSrcTable.setStatus(_A)
_TnSdpBindIgmpSnpgStaticGrpSrcEntry_Object=MibTableRow
tnSdpBindIgmpSnpgStaticGrpSrcEntry=_TnSdpBindIgmpSnpgStaticGrpSrcEntry_Object((1,3,6,1,4,1,7483,6,1,2,24,3,4,1))
tnSdpBindIgmpSnpgStaticGrpSrcEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_P,_Q),(0,_I,_o),(0,_I,_p))
if mibBuilder.loadTexts:tnSdpBindIgmpSnpgStaticGrpSrcEntry.setStatus(_A)
_SdpBndIgmpSnpgStaticGroupAddr_Type=IpAddress
_SdpBndIgmpSnpgStaticGroupAddr_Object=MibTableColumn
sdpBndIgmpSnpgStaticGroupAddr=_SdpBndIgmpSnpgStaticGroupAddr_Object((1,3,6,1,4,1,7483,6,1,2,24,3,4,1,1),_SdpBndIgmpSnpgStaticGroupAddr_Type())
sdpBndIgmpSnpgStaticGroupAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:sdpBndIgmpSnpgStaticGroupAddr.setStatus(_A)
_SdpBndIgmpSnpgStaticSourceAddr_Type=IpAddress
_SdpBndIgmpSnpgStaticSourceAddr_Object=MibTableColumn
sdpBndIgmpSnpgStaticSourceAddr=_SdpBndIgmpSnpgStaticSourceAddr_Object((1,3,6,1,4,1,7483,6,1,2,24,3,4,1,2),_SdpBndIgmpSnpgStaticSourceAddr_Type())
sdpBndIgmpSnpgStaticSourceAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:sdpBndIgmpSnpgStaticSourceAddr.setStatus(_A)
_SdpBndIgmpSnpgStaticRowstatus_Type=RowStatus
_SdpBndIgmpSnpgStaticRowstatus_Object=MibTableColumn
sdpBndIgmpSnpgStaticRowstatus=_SdpBndIgmpSnpgStaticRowstatus_Object((1,3,6,1,4,1,7483,6,1,2,24,3,4,1,3),_SdpBndIgmpSnpgStaticRowstatus_Type())
sdpBndIgmpSnpgStaticRowstatus.setMaxAccess(_m)
if mibBuilder.loadTexts:sdpBndIgmpSnpgStaticRowstatus.setStatus(_A)
_SdpBndIgmpSnpgStaticLastChange_Type=TimeStamp
_SdpBndIgmpSnpgStaticLastChange_Object=MibTableColumn
sdpBndIgmpSnpgStaticLastChange=_SdpBndIgmpSnpgStaticLastChange_Object((1,3,6,1,4,1,7483,6,1,2,24,3,4,1,4),_SdpBndIgmpSnpgStaticLastChange_Type())
sdpBndIgmpSnpgStaticLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgStaticLastChange.setStatus(_A)
_TnSdpBindIgmpSnpgStatsTable_Object=MibTable
tnSdpBindIgmpSnpgStatsTable=_TnSdpBindIgmpSnpgStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5))
if mibBuilder.loadTexts:tnSdpBindIgmpSnpgStatsTable.setStatus(_A)
_TnSdpBindIgmpSnpgStatsEntry_Object=MibTableRow
tnSdpBindIgmpSnpgStatsEntry=_TnSdpBindIgmpSnpgStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1))
tnSdpBindIgmpSnpgStatsEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_P,_Q))
if mibBuilder.loadTexts:tnSdpBindIgmpSnpgStatsEntry.setStatus(_A)
_SdpBndIgmpSnpgTxGenQueries_Type=Counter32
_SdpBndIgmpSnpgTxGenQueries_Object=MibTableColumn
sdpBndIgmpSnpgTxGenQueries=_SdpBndIgmpSnpgTxGenQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,1),_SdpBndIgmpSnpgTxGenQueries_Type())
sdpBndIgmpSnpgTxGenQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgTxGenQueries.setStatus(_A)
_SdpBndIgmpSnpgTxGrpSpecQueries_Type=Counter32
_SdpBndIgmpSnpgTxGrpSpecQueries_Object=MibTableColumn
sdpBndIgmpSnpgTxGrpSpecQueries=_SdpBndIgmpSnpgTxGrpSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,2),_SdpBndIgmpSnpgTxGrpSpecQueries_Type())
sdpBndIgmpSnpgTxGrpSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgTxGrpSpecQueries.setStatus(_A)
_SdpBndIgmpSnpgTxSrcSpecQueries_Type=Counter32
_SdpBndIgmpSnpgTxSrcSpecQueries_Object=MibTableColumn
sdpBndIgmpSnpgTxSrcSpecQueries=_SdpBndIgmpSnpgTxSrcSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,3),_SdpBndIgmpSnpgTxSrcSpecQueries_Type())
sdpBndIgmpSnpgTxSrcSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgTxSrcSpecQueries.setStatus(_A)
_SdpBndIgmpSnpgTxV1Reports_Type=Counter32
_SdpBndIgmpSnpgTxV1Reports_Object=MibTableColumn
sdpBndIgmpSnpgTxV1Reports=_SdpBndIgmpSnpgTxV1Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,4),_SdpBndIgmpSnpgTxV1Reports_Type())
sdpBndIgmpSnpgTxV1Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgTxV1Reports.setStatus(_A)
_SdpBndIgmpSnpgTxV2Reports_Type=Counter32
_SdpBndIgmpSnpgTxV2Reports_Object=MibTableColumn
sdpBndIgmpSnpgTxV2Reports=_SdpBndIgmpSnpgTxV2Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,5),_SdpBndIgmpSnpgTxV2Reports_Type())
sdpBndIgmpSnpgTxV2Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgTxV2Reports.setStatus(_A)
_SdpBndIgmpSnpgTxV3Reports_Type=Counter32
_SdpBndIgmpSnpgTxV3Reports_Object=MibTableColumn
sdpBndIgmpSnpgTxV3Reports=_SdpBndIgmpSnpgTxV3Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,6),_SdpBndIgmpSnpgTxV3Reports_Type())
sdpBndIgmpSnpgTxV3Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgTxV3Reports.setStatus(_A)
_SdpBndIgmpSnpgTxV2Leaves_Type=Counter32
_SdpBndIgmpSnpgTxV2Leaves_Object=MibTableColumn
sdpBndIgmpSnpgTxV2Leaves=_SdpBndIgmpSnpgTxV2Leaves_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,7),_SdpBndIgmpSnpgTxV2Leaves_Type())
sdpBndIgmpSnpgTxV2Leaves.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgTxV2Leaves.setStatus(_A)
_SdpBndIgmpSnpgRxGenQueries_Type=Counter32
_SdpBndIgmpSnpgRxGenQueries_Object=MibTableColumn
sdpBndIgmpSnpgRxGenQueries=_SdpBndIgmpSnpgRxGenQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,8),_SdpBndIgmpSnpgRxGenQueries_Type())
sdpBndIgmpSnpgRxGenQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxGenQueries.setStatus(_A)
_SdpBndIgmpSnpgRxGrpSpecQueries_Type=Counter32
_SdpBndIgmpSnpgRxGrpSpecQueries_Object=MibTableColumn
sdpBndIgmpSnpgRxGrpSpecQueries=_SdpBndIgmpSnpgRxGrpSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,9),_SdpBndIgmpSnpgRxGrpSpecQueries_Type())
sdpBndIgmpSnpgRxGrpSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxGrpSpecQueries.setStatus(_A)
_SdpBndIgmpSnpgRxSrcSpecQueries_Type=Counter32
_SdpBndIgmpSnpgRxSrcSpecQueries_Object=MibTableColumn
sdpBndIgmpSnpgRxSrcSpecQueries=_SdpBndIgmpSnpgRxSrcSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,10),_SdpBndIgmpSnpgRxSrcSpecQueries_Type())
sdpBndIgmpSnpgRxSrcSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxSrcSpecQueries.setStatus(_A)
_SdpBndIgmpSnpgRxV1Reports_Type=Counter32
_SdpBndIgmpSnpgRxV1Reports_Object=MibTableColumn
sdpBndIgmpSnpgRxV1Reports=_SdpBndIgmpSnpgRxV1Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,11),_SdpBndIgmpSnpgRxV1Reports_Type())
sdpBndIgmpSnpgRxV1Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxV1Reports.setStatus(_A)
_SdpBndIgmpSnpgRxV2Reports_Type=Counter32
_SdpBndIgmpSnpgRxV2Reports_Object=MibTableColumn
sdpBndIgmpSnpgRxV2Reports=_SdpBndIgmpSnpgRxV2Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,12),_SdpBndIgmpSnpgRxV2Reports_Type())
sdpBndIgmpSnpgRxV2Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxV2Reports.setStatus(_A)
_SdpBndIgmpSnpgRxV3Reports_Type=Counter32
_SdpBndIgmpSnpgRxV3Reports_Object=MibTableColumn
sdpBndIgmpSnpgRxV3Reports=_SdpBndIgmpSnpgRxV3Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,13),_SdpBndIgmpSnpgRxV3Reports_Type())
sdpBndIgmpSnpgRxV3Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxV3Reports.setStatus(_A)
_SdpBndIgmpSnpgRxV2Leaves_Type=Counter32
_SdpBndIgmpSnpgRxV2Leaves_Object=MibTableColumn
sdpBndIgmpSnpgRxV2Leaves=_SdpBndIgmpSnpgRxV2Leaves_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,14),_SdpBndIgmpSnpgRxV2Leaves_Type())
sdpBndIgmpSnpgRxV2Leaves.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxV2Leaves.setStatus(_A)
_SdpBndIgmpSnpgRxUnknownType_Type=Counter32
_SdpBndIgmpSnpgRxUnknownType_Object=MibTableColumn
sdpBndIgmpSnpgRxUnknownType=_SdpBndIgmpSnpgRxUnknownType_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,15),_SdpBndIgmpSnpgRxUnknownType_Type())
sdpBndIgmpSnpgRxUnknownType.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxUnknownType.setStatus(_A)
_SdpBndIgmpSnpgFwdGenQueries_Type=Counter32
_SdpBndIgmpSnpgFwdGenQueries_Object=MibTableColumn
sdpBndIgmpSnpgFwdGenQueries=_SdpBndIgmpSnpgFwdGenQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,16),_SdpBndIgmpSnpgFwdGenQueries_Type())
sdpBndIgmpSnpgFwdGenQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgFwdGenQueries.setStatus(_A)
_SdpBndIgmpSnpgFwdGrpSpecQueries_Type=Counter32
_SdpBndIgmpSnpgFwdGrpSpecQueries_Object=MibTableColumn
sdpBndIgmpSnpgFwdGrpSpecQueries=_SdpBndIgmpSnpgFwdGrpSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,17),_SdpBndIgmpSnpgFwdGrpSpecQueries_Type())
sdpBndIgmpSnpgFwdGrpSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgFwdGrpSpecQueries.setStatus(_A)
_SdpBndIgmpSnpgFwdSrcSpecQueries_Type=Counter32
_SdpBndIgmpSnpgFwdSrcSpecQueries_Object=MibTableColumn
sdpBndIgmpSnpgFwdSrcSpecQueries=_SdpBndIgmpSnpgFwdSrcSpecQueries_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,18),_SdpBndIgmpSnpgFwdSrcSpecQueries_Type())
sdpBndIgmpSnpgFwdSrcSpecQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgFwdSrcSpecQueries.setStatus(_A)
_SdpBndIgmpSnpgFwdV1Reports_Type=Counter32
_SdpBndIgmpSnpgFwdV1Reports_Object=MibTableColumn
sdpBndIgmpSnpgFwdV1Reports=_SdpBndIgmpSnpgFwdV1Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,19),_SdpBndIgmpSnpgFwdV1Reports_Type())
sdpBndIgmpSnpgFwdV1Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgFwdV1Reports.setStatus(_A)
_SdpBndIgmpSnpgFwdV2Reports_Type=Counter32
_SdpBndIgmpSnpgFwdV2Reports_Object=MibTableColumn
sdpBndIgmpSnpgFwdV2Reports=_SdpBndIgmpSnpgFwdV2Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,20),_SdpBndIgmpSnpgFwdV2Reports_Type())
sdpBndIgmpSnpgFwdV2Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgFwdV2Reports.setStatus(_A)
_SdpBndIgmpSnpgFwdV3Reports_Type=Counter32
_SdpBndIgmpSnpgFwdV3Reports_Object=MibTableColumn
sdpBndIgmpSnpgFwdV3Reports=_SdpBndIgmpSnpgFwdV3Reports_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,21),_SdpBndIgmpSnpgFwdV3Reports_Type())
sdpBndIgmpSnpgFwdV3Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgFwdV3Reports.setStatus(_A)
_SdpBndIgmpSnpgFwdV2Leaves_Type=Counter32
_SdpBndIgmpSnpgFwdV2Leaves_Object=MibTableColumn
sdpBndIgmpSnpgFwdV2Leaves=_SdpBndIgmpSnpgFwdV2Leaves_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,22),_SdpBndIgmpSnpgFwdV2Leaves_Type())
sdpBndIgmpSnpgFwdV2Leaves.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgFwdV2Leaves.setStatus(_A)
_SdpBndIgmpSnpgFwdUnknownType_Type=Counter32
_SdpBndIgmpSnpgFwdUnknownType_Object=MibTableColumn
sdpBndIgmpSnpgFwdUnknownType=_SdpBndIgmpSnpgFwdUnknownType_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,23),_SdpBndIgmpSnpgFwdUnknownType_Type())
sdpBndIgmpSnpgFwdUnknownType.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgFwdUnknownType.setStatus(_A)
_SdpBndIgmpSnpgRxBadLenPkts_Type=Counter32
_SdpBndIgmpSnpgRxBadLenPkts_Object=MibTableColumn
sdpBndIgmpSnpgRxBadLenPkts=_SdpBndIgmpSnpgRxBadLenPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,24),_SdpBndIgmpSnpgRxBadLenPkts_Type())
sdpBndIgmpSnpgRxBadLenPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxBadLenPkts.setStatus(_A)
_SdpBndIgmpSnpgRxBadIpChksmPkts_Type=Counter32
_SdpBndIgmpSnpgRxBadIpChksmPkts_Object=MibTableColumn
sdpBndIgmpSnpgRxBadIpChksmPkts=_SdpBndIgmpSnpgRxBadIpChksmPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,25),_SdpBndIgmpSnpgRxBadIpChksmPkts_Type())
sdpBndIgmpSnpgRxBadIpChksmPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxBadIpChksmPkts.setStatus(_A)
_SdpBndIgmpSnpgRxBadIgmpChksmPkts_Type=Counter32
_SdpBndIgmpSnpgRxBadIgmpChksmPkts_Object=MibTableColumn
sdpBndIgmpSnpgRxBadIgmpChksmPkts=_SdpBndIgmpSnpgRxBadIgmpChksmPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,26),_SdpBndIgmpSnpgRxBadIgmpChksmPkts_Type())
sdpBndIgmpSnpgRxBadIgmpChksmPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxBadIgmpChksmPkts.setStatus(_A)
_SdpBndIgmpSnpgRxBadEncodedPkts_Type=Counter32
_SdpBndIgmpSnpgRxBadEncodedPkts_Object=MibTableColumn
sdpBndIgmpSnpgRxBadEncodedPkts=_SdpBndIgmpSnpgRxBadEncodedPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,27),_SdpBndIgmpSnpgRxBadEncodedPkts_Type())
sdpBndIgmpSnpgRxBadEncodedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxBadEncodedPkts.setStatus(_A)
_SdpBndIgmpSnpgRxNoRtrAlertPkts_Type=Counter32
_SdpBndIgmpSnpgRxNoRtrAlertPkts_Object=MibTableColumn
sdpBndIgmpSnpgRxNoRtrAlertPkts=_SdpBndIgmpSnpgRxNoRtrAlertPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,28),_SdpBndIgmpSnpgRxNoRtrAlertPkts_Type())
sdpBndIgmpSnpgRxNoRtrAlertPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxNoRtrAlertPkts.setStatus(_A)
_SdpBndIgmpSnpgRxZeroSrcAdrPkts_Type=Counter32
_SdpBndIgmpSnpgRxZeroSrcAdrPkts_Object=MibTableColumn
sdpBndIgmpSnpgRxZeroSrcAdrPkts=_SdpBndIgmpSnpgRxZeroSrcAdrPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,29),_SdpBndIgmpSnpgRxZeroSrcAdrPkts_Type())
sdpBndIgmpSnpgRxZeroSrcAdrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxZeroSrcAdrPkts.setStatus(_A)
_SdpBndIgmpSnpgSendQueryCfgDrops_Type=Counter32
_SdpBndIgmpSnpgSendQueryCfgDrops_Object=MibTableColumn
sdpBndIgmpSnpgSendQueryCfgDrops=_SdpBndIgmpSnpgSendQueryCfgDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,30),_SdpBndIgmpSnpgSendQueryCfgDrops_Type())
sdpBndIgmpSnpgSendQueryCfgDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgSendQueryCfgDrops.setStatus(_A)
_SdpBndIgmpSnpgImportPolicyDrops_Type=Counter32
_SdpBndIgmpSnpgImportPolicyDrops_Object=MibTableColumn
sdpBndIgmpSnpgImportPolicyDrops=_SdpBndIgmpSnpgImportPolicyDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,31),_SdpBndIgmpSnpgImportPolicyDrops_Type())
sdpBndIgmpSnpgImportPolicyDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgImportPolicyDrops.setStatus(_A)
_SdpBndIgmpSnpgMaxNumGroupsDrops_Type=Counter32
_SdpBndIgmpSnpgMaxNumGroupsDrops_Object=MibTableColumn
sdpBndIgmpSnpgMaxNumGroupsDrops=_SdpBndIgmpSnpgMaxNumGroupsDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,32),_SdpBndIgmpSnpgMaxNumGroupsDrops_Type())
sdpBndIgmpSnpgMaxNumGroupsDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgMaxNumGroupsDrops.setStatus(_A)
_SdpBndIgmpSnpgRxWrongVersionPkts_Type=Counter32
_SdpBndIgmpSnpgRxWrongVersionPkts_Object=MibTableColumn
sdpBndIgmpSnpgRxWrongVersionPkts=_SdpBndIgmpSnpgRxWrongVersionPkts_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,33),_SdpBndIgmpSnpgRxWrongVersionPkts_Type())
sdpBndIgmpSnpgRxWrongVersionPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxWrongVersionPkts.setStatus(_A)
_SdpBndIgmpSnpgMcacPolicyDrops_Type=Counter32
_SdpBndIgmpSnpgMcacPolicyDrops_Object=MibTableColumn
sdpBndIgmpSnpgMcacPolicyDrops=_SdpBndIgmpSnpgMcacPolicyDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,34),_SdpBndIgmpSnpgMcacPolicyDrops_Type())
sdpBndIgmpSnpgMcacPolicyDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgMcacPolicyDrops.setStatus(_A)
_SdpBndIgmpSnpgRxLocalScopePkts_Type=Counter32
_SdpBndIgmpSnpgRxLocalScopePkts_Object=MibTableColumn
sdpBndIgmpSnpgRxLocalScopePkts=_SdpBndIgmpSnpgRxLocalScopePkts_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,35),_SdpBndIgmpSnpgRxLocalScopePkts_Type())
sdpBndIgmpSnpgRxLocalScopePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxLocalScopePkts.setStatus(_A)
_SdpBndIgmpSnpgRxRsvdScopePkts_Type=Counter32
_SdpBndIgmpSnpgRxRsvdScopePkts_Object=MibTableColumn
sdpBndIgmpSnpgRxRsvdScopePkts=_SdpBndIgmpSnpgRxRsvdScopePkts_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,36),_SdpBndIgmpSnpgRxRsvdScopePkts_Type())
sdpBndIgmpSnpgRxRsvdScopePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxRsvdScopePkts.setStatus(_A)
_SdpBndIgmpSnpgMaxNumSourcesDrops_Type=Counter32
_SdpBndIgmpSnpgMaxNumSourcesDrops_Object=MibTableColumn
sdpBndIgmpSnpgMaxNumSourcesDrops=_SdpBndIgmpSnpgMaxNumSourcesDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,37),_SdpBndIgmpSnpgMaxNumSourcesDrops_Type())
sdpBndIgmpSnpgMaxNumSourcesDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgMaxNumSourcesDrops.setStatus(_A)
_SdpBndIgmpSnpgNumGrps_Type=Counter32
_SdpBndIgmpSnpgNumGrps_Object=MibTableColumn
sdpBndIgmpSnpgNumGrps=_SdpBndIgmpSnpgNumGrps_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,38),_SdpBndIgmpSnpgNumGrps_Type())
sdpBndIgmpSnpgNumGrps.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgNumGrps.setStatus(_A)
_SdpBndIgmpSnpgRxQueryDrops_Type=Counter32
_SdpBndIgmpSnpgRxQueryDrops_Object=MibTableColumn
sdpBndIgmpSnpgRxQueryDrops=_SdpBndIgmpSnpgRxQueryDrops_Object((1,3,6,1,4,1,7483,6,1,2,24,3,5,1,39),_SdpBndIgmpSnpgRxQueryDrops_Type())
sdpBndIgmpSnpgRxQueryDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBndIgmpSnpgRxQueryDrops.setStatus(_A)
_TnIgmpSnoopingNotifyPrefix_ObjectIdentity=ObjectIdentity
tnIgmpSnoopingNotifyPrefix=_TnIgmpSnoopingNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,24))
_TnIgmpSnoopingSapPrefix_ObjectIdentity=ObjectIdentity
tnIgmpSnoopingSapPrefix=_TnIgmpSnoopingSapPrefix_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,24,1))
_TnIgmpSnpgSapNotifications_ObjectIdentity=ObjectIdentity
tnIgmpSnpgSapNotifications=_TnIgmpSnpgSapNotifications_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,24,1,0))
mibBuilder.exportSymbols(_I,**{_O:AlxIgmpSnpgAdminState,'AlxIgmpSnpgLocation':AlxIgmpSnpgLocation,'tnIgmpSnoopingMIBModule':tnIgmpSnoopingMIBModule,'tnIgmpSnoopingObjs':tnIgmpSnoopingObjs,'tnIgmpSnoopingTlsObjs':tnIgmpSnoopingTlsObjs,'tnTlsIgmpSnpgConfigTable':tnTlsIgmpSnpgConfigTable,'tnTlsIgmpSnpgConfigEntry':tnTlsIgmpSnpgConfigEntry,'tnTlsIgmpSnpgCfgAdminState':tnTlsIgmpSnpgCfgAdminState,'tnTlsIgmpSnpgCfgGenQueryIntvl':tnTlsIgmpSnpgCfgGenQueryIntvl,'tnTlsIgmpSnpgCfgRobustCount':tnTlsIgmpSnpgCfgRobustCount,'tnTlsIgmpSnpgCfgReportSrcAddress':tnTlsIgmpSnpgCfgReportSrcAddress,'tnTlsIgmpSnpgCfgMvrAdminState':tnTlsIgmpSnpgCfgMvrAdminState,'tnTlsIgmpSnpgCfgMvrDescription':tnTlsIgmpSnpgCfgMvrDescription,'tnTlsIgmpSnpgCfgMvrPolicy':tnTlsIgmpSnpgCfgMvrPolicy,'tnTlsIgmpSnpgCfgQuerySrcAddress':tnTlsIgmpSnpgCfgQuerySrcAddress,'tnTlsIgmpSnpgCfgQuerySrcAddrType':tnTlsIgmpSnpgCfgQuerySrcAddrType,'tnTlsIgmpSnpgCfgLastChangeTime':tnTlsIgmpSnpgCfgLastChangeTime,'tnTlsIgmpSnpgQuerierTable':tnTlsIgmpSnpgQuerierTable,'tnTlsIgmpSnpgQuerierEntry':tnTlsIgmpSnpgQuerierEntry,'tnTlsIgmpSnpgQuerierVersion':tnTlsIgmpSnpgQuerierVersion,'tnTlsIgmpSnpgQuerierAddress':tnTlsIgmpSnpgQuerierAddress,'tnTlsIgmpSnpgQuerierLocale':tnTlsIgmpSnpgQuerierLocale,'tnTlsIgmpSnpgQuerierPortId':tnTlsIgmpSnpgQuerierPortId,'tnTlsIgmpSnpgQuerierEncapValue':tnTlsIgmpSnpgQuerierEncapValue,'tnTlsIgmpSnpgQuerierSdpId':tnTlsIgmpSnpgQuerierSdpId,'tnTlsIgmpSnpgQuerierVcId':tnTlsIgmpSnpgQuerierVcId,'tnTlsIgmpSnpgQuerierUpTime':tnTlsIgmpSnpgQuerierUpTime,'tnTlsIgmpSnpgQuerierExpiryTime':tnTlsIgmpSnpgQuerierExpiryTime,'tnTlsIgmpSnpgQuerierGenQueryIntvl':tnTlsIgmpSnpgQuerierGenQueryIntvl,'tnTlsIgmpSnpgQuerierGenRespIntvl':tnTlsIgmpSnpgQuerierGenRespIntvl,'tnTlsIgmpSnpgQuerierRobustCount':tnTlsIgmpSnpgQuerierRobustCount,'tnTlsIgmpSnpgProxyGroupTable':tnTlsIgmpSnpgProxyGroupTable,'tnTlsIgmpSnpgProxyGroupEntry':tnTlsIgmpSnpgProxyGroupEntry,_Y:tnTlsIgmpSnpgProxyGroupAddress,'tnTlsIgmpSnpgProxyGroupFilterMode':tnTlsIgmpSnpgProxyGroupFilterMode,'tnTlsIgmpSnpgProxyGroupUpTime':tnTlsIgmpSnpgProxyGroupUpTime,'tnTlsIgmpSnpgProxyGrpSrcTable':tnTlsIgmpSnpgProxyGrpSrcTable,'tnTlsIgmpSnpgProxyGrpSrcEntry':tnTlsIgmpSnpgProxyGrpSrcEntry,_h:tnTlsIgmpSnpgProxyGrpSrcAddr,'tnTlsIgmpSnpgProxyGrpSrcUpTime':tnTlsIgmpSnpgProxyGrpSrcUpTime,'tnTlsIgmpSnpgMRouterTable':tnTlsIgmpSnpgMRouterTable,'tnTlsIgmpSnpgMRouterEntry':tnTlsIgmpSnpgMRouterEntry,_i:tnTlsIgmpSnpgMRouterAddress,'tnTlsIgmpSnpgMRouterLocale':tnTlsIgmpSnpgMRouterLocale,'tnTlsIgmpSnpgMRouterPortId':tnTlsIgmpSnpgMRouterPortId,'tnTlsIgmpSnpgMRouterEncapValue':tnTlsIgmpSnpgMRouterEncapValue,'tnTlsIgmpSnpgMRouterSdpId':tnTlsIgmpSnpgMRouterSdpId,'tnTlsIgmpSnpgMRouterVcId':tnTlsIgmpSnpgMRouterVcId,'tnTlsIgmpSnpgMRouterVersion':tnTlsIgmpSnpgMRouterVersion,'tnTlsIgmpSnpgMRouterExpiryTime':tnTlsIgmpSnpgMRouterExpiryTime,'tnTlsIgmpSnpgMRouterUpTime':tnTlsIgmpSnpgMRouterUpTime,'tnTlsIgmpSnpgMRouterGenQueryIntvl':tnTlsIgmpSnpgMRouterGenQueryIntvl,'tnTlsIgmpSnpgMRouterGenRespIntvl':tnTlsIgmpSnpgMRouterGenRespIntvl,'tnTlsIgmpSnpgMRouterRobustCount':tnTlsIgmpSnpgMRouterRobustCount,'tnIgmpSnoopingTlsScalar1':tnIgmpSnoopingTlsScalar1,'tnIgmpSnoopingTlsScalar2':tnIgmpSnoopingTlsScalar2,'tnIgmpSnoopingSapObjs':tnIgmpSnoopingSapObjs,'tnSapIgmpSnpgConfigTable':tnSapIgmpSnpgConfigTable,'tnSapIgmpSnpgConfigEntry':tnSapIgmpSnpgConfigEntry,'tnSapIgmpSnpgCfgImportPlcy':tnSapIgmpSnpgCfgImportPlcy,'tnSapIgmpSnpgCfgFastLeave':tnSapIgmpSnpgCfgFastLeave,'tnSapIgmpSnpgCfgMRouter':tnSapIgmpSnpgCfgMRouter,'tnSapIgmpSnpgCfgSendQueries':tnSapIgmpSnpgCfgSendQueries,'tnSapIgmpSnpgCfgGenQueryIntvl':tnSapIgmpSnpgCfgGenQueryIntvl,'tnSapIgmpSnpgCfgQueryRespIntvl':tnSapIgmpSnpgCfgQueryRespIntvl,'tnSapIgmpSnpgCfgRobustCount':tnSapIgmpSnpgCfgRobustCount,'tnSapIgmpSnpgCfgLastMembIntvl':tnSapIgmpSnpgCfgLastMembIntvl,'tnSapIgmpSnpgCfgMaxNbrGrps':tnSapIgmpSnpgCfgMaxNbrGrps,'tnSapIgmpSnpgCfgMvrFromVplsId':tnSapIgmpSnpgCfgMvrFromVplsId,'tnSapIgmpSnpgCfgMvrToSapPortId':tnSapIgmpSnpgCfgMvrToSapPortId,'tnSapIgmpSnpgCfgMvrToSapEncapVal':tnSapIgmpSnpgCfgMvrToSapEncapVal,'tnSapIgmpSnpgCfgVersion':tnSapIgmpSnpgCfgVersion,'tnSapIgmpSnpgCfgMcacPolicyName':tnSapIgmpSnpgCfgMcacPolicyName,'tnSapIgmpSnpgCfgMcacUnconstBW':tnSapIgmpSnpgCfgMcacUnconstBW,'tnSapIgmpSnpgCfgMcacConstAdmSt':tnSapIgmpSnpgCfgMcacConstAdmSt,'tnSapIgmpSnpgCfgMcacPrRsvMndBW':tnSapIgmpSnpgCfgMcacPrRsvMndBW,'tnSapIgmpSnpgCfgMcacinUseMandBw':tnSapIgmpSnpgCfgMcacinUseMandBw,'tnSapIgmpSnpgCfgMcacinUseOpnlBw':tnSapIgmpSnpgCfgMcacinUseOpnlBw,'tnSapIgmpSnpgCfgMcacAvailMandBw':tnSapIgmpSnpgCfgMcacAvailMandBw,'tnSapIgmpSnpgCfgMcacAvailOpnlBw':tnSapIgmpSnpgCfgMcacAvailOpnlBw,'tnSapIgmpSnpgCfgMcacValInTrans':tnSapIgmpSnpgCfgMcacValInTrans,'tnSapIgmpSnpgCfgLastChangeTime':tnSapIgmpSnpgCfgLastChangeTime,'tnSapIgmpSnpgCfgMaxNbrSrcs':tnSapIgmpSnpgCfgMaxNbrSrcs,'tnSapIgmpSnpgGroupTable':tnSapIgmpSnpgGroupTable,'tnSapIgmpSnpgGroupEntry':tnSapIgmpSnpgGroupEntry,_Z:tnSapIgmpSnpgGrpAddress,'tnSapIgmpSnpgGrpType':tnSapIgmpSnpgGrpType,'tnSapIgmpSnpgGrpFilterMode':tnSapIgmpSnpgGrpFilterMode,'tnSapIgmpSnpgGrpUpTime':tnSapIgmpSnpgGrpUpTime,'tnSapIgmpSnpgGrpExpiryTime':tnSapIgmpSnpgGrpExpiryTime,'tnSapIgmpSnpgGrpCompatMode':tnSapIgmpSnpgGrpCompatMode,'tnSapIgmpSnpgGrpV1HostExpTime':tnSapIgmpSnpgGrpV1HostExpTime,'tnSapIgmpSnpgGrpV2HostExpTime':tnSapIgmpSnpgGrpV2HostExpTime,'tnSapIgmpSnpgGrpMvrFromVplsId':tnSapIgmpSnpgGrpMvrFromVplsId,'tnSapIgmpSnpgGrpMvrToSapPortId':tnSapIgmpSnpgGrpMvrToSapPortId,'tnSapIgmpSnpgGrpMvrToSapEncapVal':tnSapIgmpSnpgGrpMvrToSapEncapVal,'tnSapIgmpSnpgGrpNumSrc':tnSapIgmpSnpgGrpNumSrc,'tnSapIgmpSnpgGrpSrcTable':tnSapIgmpSnpgGrpSrcTable,'tnSapIgmpSnpgGrpSrcEntry':tnSapIgmpSnpgGrpSrcEntry,_j:tnSapIgmpSnpgGrpSrcAddr,'tnSapIgmpSnpgGrpSrcType':tnSapIgmpSnpgGrpSrcType,'tnSapIgmpSnpgGrpSrcUpTime':tnSapIgmpSnpgGrpSrcUpTime,'tnSapIgmpSnpgGrpSrcExpiryTime':tnSapIgmpSnpgGrpSrcExpiryTime,'tnSapIgmpSnpgStaticGrpSrcTable':tnSapIgmpSnpgStaticGrpSrcTable,'tnSapIgmpSnpgStaticGrpSrcEntry':tnSapIgmpSnpgStaticGrpSrcEntry,_k:tnSapIgmpSnpgStaticGroupAddr,_l:tnSapIgmpSnpgStaticSourceAddr,'tnSapIgmpSnpgStaticRowstatus':tnSapIgmpSnpgStaticRowstatus,'tnSapIgmpSnpgStaticLastChangeTime':tnSapIgmpSnpgStaticLastChangeTime,'tnSapIgmpSnpgStatsTable':tnSapIgmpSnpgStatsTable,'tnSapIgmpSnpgStatsEntry':tnSapIgmpSnpgStatsEntry,'tnSapIgmpSnpgTxGenQueries':tnSapIgmpSnpgTxGenQueries,'tnSapIgmpSnpgTxGrpSpecQueries':tnSapIgmpSnpgTxGrpSpecQueries,'tnSapIgmpSnpgTxSrcSpecQueries':tnSapIgmpSnpgTxSrcSpecQueries,'tnSapIgmpSnpgTxV1Reports':tnSapIgmpSnpgTxV1Reports,'tnSapIgmpSnpgTxV2Reports':tnSapIgmpSnpgTxV2Reports,'tnSapIgmpSnpgTxV3Reports':tnSapIgmpSnpgTxV3Reports,'tnSapIgmpSnpgTxV2Leaves':tnSapIgmpSnpgTxV2Leaves,'tnSapIgmpSnpgRxGenQueries':tnSapIgmpSnpgRxGenQueries,'tnSapIgmpSnpgRxGrpSpecQueries':tnSapIgmpSnpgRxGrpSpecQueries,'tnSapIgmpSnpgRxSrcSpecQueries':tnSapIgmpSnpgRxSrcSpecQueries,'tnSapIgmpSnpgRxV1Reports':tnSapIgmpSnpgRxV1Reports,'tnSapIgmpSnpgRxV2Reports':tnSapIgmpSnpgRxV2Reports,'tnSapIgmpSnpgRxV3Reports':tnSapIgmpSnpgRxV3Reports,'tnSapIgmpSnpgRxV2Leaves':tnSapIgmpSnpgRxV2Leaves,'tnSapIgmpSnpgRxUnknownType':tnSapIgmpSnpgRxUnknownType,'tnSapIgmpSnpgFwdGenQueries':tnSapIgmpSnpgFwdGenQueries,'tnSapIgmpSnpgFwdGrpSpecQueries':tnSapIgmpSnpgFwdGrpSpecQueries,'tnSapIgmpSnpgFwdSrcSpecQueries':tnSapIgmpSnpgFwdSrcSpecQueries,'tnSapIgmpSnpgFwdV1Reports':tnSapIgmpSnpgFwdV1Reports,'tnSapIgmpSnpgFwdV2Reports':tnSapIgmpSnpgFwdV2Reports,'tnSapIgmpSnpgFwdV3Reports':tnSapIgmpSnpgFwdV3Reports,'tnSapIgmpSnpgFwdV2Leaves':tnSapIgmpSnpgFwdV2Leaves,'tnSapIgmpSnpgFwdUnknownType':tnSapIgmpSnpgFwdUnknownType,'tnSapIgmpSnpgRxBadLenPkts':tnSapIgmpSnpgRxBadLenPkts,'tnSapIgmpSnpgRxBadIpChksmPkts':tnSapIgmpSnpgRxBadIpChksmPkts,'tnSapIgmpSnpgRxBadIgmpChksmPkts':tnSapIgmpSnpgRxBadIgmpChksmPkts,'tnSapIgmpSnpgRxBadEncodedPkts':tnSapIgmpSnpgRxBadEncodedPkts,'tnSapIgmpSnpgRxNoRtrAlertPkts':tnSapIgmpSnpgRxNoRtrAlertPkts,'tnSapIgmpSnpgRxZeroSrcAdrPkts':tnSapIgmpSnpgRxZeroSrcAdrPkts,'tnSapIgmpSnpgSendQueryCfgDrops':tnSapIgmpSnpgSendQueryCfgDrops,'tnSapIgmpSnpgImportPolicyDrops':tnSapIgmpSnpgImportPolicyDrops,'tnSapIgmpSnpgMaxNumGroupsDrops':tnSapIgmpSnpgMaxNumGroupsDrops,'tnSapIgmpSnpgMvrFromVplsCfgDrops':tnSapIgmpSnpgMvrFromVplsCfgDrops,'tnSapIgmpSnpgMvrToSapCfgDrops':tnSapIgmpSnpgMvrToSapCfgDrops,'tnSapIgmpSnpgRxWrongVersionPkts':tnSapIgmpSnpgRxWrongVersionPkts,'tnSapIgmpSnpgMcacPolicyDrops':tnSapIgmpSnpgMcacPolicyDrops,'tnSapIgmpSnpgMcsFailures':tnSapIgmpSnpgMcsFailures,'tnSapIgmpSnpgRxLocalScopePkts':tnSapIgmpSnpgRxLocalScopePkts,'tnSapIgmpSnpgRxRsvdScopePkts':tnSapIgmpSnpgRxRsvdScopePkts,'tnSapIgmpSnpgMaxNumSourcesDrops':tnSapIgmpSnpgMaxNumSourcesDrops,'tnSapIgmpSnpgNumGrps':tnSapIgmpSnpgNumGrps,'tnSapIgmpSnpgRxQueryDrops':tnSapIgmpSnpgRxQueryDrops,'tnSvcIgmpSnpgStatsTable':tnSvcIgmpSnpgStatsTable,'tnSvcIgmpSnpgStatsEntry':tnSvcIgmpSnpgStatsEntry,'tnSvcIgmpSnpgTxGenQueries':tnSvcIgmpSnpgTxGenQueries,'tnSvcIgmpSnpgTxGrpSpecQueries':tnSvcIgmpSnpgTxGrpSpecQueries,'tnSvcIgmpSnpgTxSrcSpecQueries':tnSvcIgmpSnpgTxSrcSpecQueries,'tnSvcIgmpSnpgTxV1Reports':tnSvcIgmpSnpgTxV1Reports,'tnSvcIgmpSnpgTxV2Reports':tnSvcIgmpSnpgTxV2Reports,'tnSvcIgmpSnpgTxV3Reports':tnSvcIgmpSnpgTxV3Reports,'tnSvcIgmpSnpgTxV2Leaves':tnSvcIgmpSnpgTxV2Leaves,'tnSvcIgmpSnpgRxGenQueries':tnSvcIgmpSnpgRxGenQueries,'tnSvcIgmpSnpgRxGrpSpecQueries':tnSvcIgmpSnpgRxGrpSpecQueries,'tnSvcIgmpSnpgRxSrcSpecQueries':tnSvcIgmpSnpgRxSrcSpecQueries,'tnSvcIgmpSnpgRxV1Reports':tnSvcIgmpSnpgRxV1Reports,'tnSvcIgmpSnpgRxV2Reports':tnSvcIgmpSnpgRxV2Reports,'tnSvcIgmpSnpgRxV3Reports':tnSvcIgmpSnpgRxV3Reports,'tnSvcIgmpSnpgRxV2Leaves':tnSvcIgmpSnpgRxV2Leaves,'tnSvcIgmpSnpgRxUnknownType':tnSvcIgmpSnpgRxUnknownType,'tnSvcIgmpSnpgFwdGenQueries':tnSvcIgmpSnpgFwdGenQueries,'tnSvcIgmpSnpgFwdGrpSpecQueries':tnSvcIgmpSnpgFwdGrpSpecQueries,'tnSvcIgmpSnpgFwdSrcSpecQueries':tnSvcIgmpSnpgFwdSrcSpecQueries,'tnSvcIgmpSnpgFwdV1Reports':tnSvcIgmpSnpgFwdV1Reports,'tnSvcIgmpSnpgFwdV2Reports':tnSvcIgmpSnpgFwdV2Reports,'tnSvcIgmpSnpgFwdV3Reports':tnSvcIgmpSnpgFwdV3Reports,'tnSvcIgmpSnpgFwdV2Leaves':tnSvcIgmpSnpgFwdV2Leaves,'tnSvcIgmpSnpgFwdUnknownType':tnSvcIgmpSnpgFwdUnknownType,'tnSvcIgmpSnpgRxBadLenPkts':tnSvcIgmpSnpgRxBadLenPkts,'tnSvcIgmpSnpgRxBadIpChksmPkts':tnSvcIgmpSnpgRxBadIpChksmPkts,'tnSvcIgmpSnpgRxBadIgmpChksmPkts':tnSvcIgmpSnpgRxBadIgmpChksmPkts,'tnSvcIgmpSnpgRxBadEncodedPkts':tnSvcIgmpSnpgRxBadEncodedPkts,'tnSvcIgmpSnpgRxNoRtrAlertPkts':tnSvcIgmpSnpgRxNoRtrAlertPkts,'tnSvcIgmpSnpgRxZeroSrcAdrPkts':tnSvcIgmpSnpgRxZeroSrcAdrPkts,'tnSvcIgmpSnpgSendQueryCfgDrops':tnSvcIgmpSnpgSendQueryCfgDrops,'tnSvcIgmpSnpgImportPolicyDrops':tnSvcIgmpSnpgImportPolicyDrops,'tnSvcIgmpSnpgMaxNumGroupsDrops':tnSvcIgmpSnpgMaxNumGroupsDrops,'tnSvcIgmpSnpgMvrFromVplsCfgDrops':tnSvcIgmpSnpgMvrFromVplsCfgDrops,'tnSvcIgmpSnpgMvrToSapCfgDrops':tnSvcIgmpSnpgMvrToSapCfgDrops,'tnSvcIgmpSnpgRxWrongVersionPkts':tnSvcIgmpSnpgRxWrongVersionPkts,'tnSvcIgmpSnpgMcacPolicyDrops':tnSvcIgmpSnpgMcacPolicyDrops,'tnSvcIgmpSnpgMcsFailures':tnSvcIgmpSnpgMcsFailures,'tnSvcIgmpSnpgRxLocalScopePkts':tnSvcIgmpSnpgRxLocalScopePkts,'tnSvcIgmpSnpgRxRsvdScopePkts':tnSvcIgmpSnpgRxRsvdScopePkts,'tnSvcIgmpSnpgMaxNumSourcesDrops':tnSvcIgmpSnpgMaxNumSourcesDrops,'tnSvcIgmpSnpgNumGrps':tnSvcIgmpSnpgNumGrps,'tnSvcIgmpSnpgRxQueryDrops':tnSvcIgmpSnpgRxQueryDrops,'tnIgmpSnoopingSapScalar1':tnIgmpSnoopingSapScalar1,'tnIgmpSnoopingSapScalar2':tnIgmpSnoopingSapScalar2,'tnIgmpSnoopingSdpBindObjs':tnIgmpSnoopingSdpBindObjs,'tnSdpBindIgmpSnpgConfigTable':tnSdpBindIgmpSnpgConfigTable,'tnSdpBindIgmpSnpgConfigEntry':tnSdpBindIgmpSnpgConfigEntry,'sdpBndIgmpSnpgCfgImportPlcy':sdpBndIgmpSnpgCfgImportPlcy,'sdpBndIgmpSnpgCfgFastLeave':sdpBndIgmpSnpgCfgFastLeave,'sdpBndIgmpSnpgCfgMRouter':sdpBndIgmpSnpgCfgMRouter,'sdpBndIgmpSnpgCfgSendQueries':sdpBndIgmpSnpgCfgSendQueries,'sdpBndIgmpSnpgCfgGenQueryIntvl':sdpBndIgmpSnpgCfgGenQueryIntvl,'sdpBndIgmpSnpgCfgQueryRespIntvl':sdpBndIgmpSnpgCfgQueryRespIntvl,'sdpBndIgmpSnpgCfgRobustCount':sdpBndIgmpSnpgCfgRobustCount,'sdpBndIgmpSnpgCfgLastMembIntvl':sdpBndIgmpSnpgCfgLastMembIntvl,'sdpBndIgmpSnpgCfgMaxNbrGrps':sdpBndIgmpSnpgCfgMaxNbrGrps,'sdpBndIgmpSnpgCfgVersion':sdpBndIgmpSnpgCfgVersion,'sdpBndIgmpSnpgCfgMcacPolicyName':sdpBndIgmpSnpgCfgMcacPolicyName,'sdpBndIgmpSnpgCfgMcacUnconstBW':sdpBndIgmpSnpgCfgMcacUnconstBW,'sdpBndIgmpSnpgCfgMcacPrRsvMndBW':sdpBndIgmpSnpgCfgMcacPrRsvMndBW,'sdpBndIgmpSnpgCfgMcacinUseMndBw':sdpBndIgmpSnpgCfgMcacinUseMndBw,'sdpBndIgmpSnpgCfgMcacinUseOplBw':sdpBndIgmpSnpgCfgMcacinUseOplBw,'sdpBndIgmpSnpgCfgMcacAvailMndBw':sdpBndIgmpSnpgCfgMcacAvailMndBw,'sdpBndIgmpSnpgCfgMcacAvailOplBw':sdpBndIgmpSnpgCfgMcacAvailOplBw,'sdpBndIgmpSnpgCfgMcacValInTrans':sdpBndIgmpSnpgCfgMcacValInTrans,'sdpBndIgmpSnpgCfgLastChangeTime':sdpBndIgmpSnpgCfgLastChangeTime,'sdpBndIgmpSnpgCfgMaxNbrSrcs':sdpBndIgmpSnpgCfgMaxNbrSrcs,'tnSdpBindIgmpSnpgGroupTable':tnSdpBindIgmpSnpgGroupTable,'tnSdpBindIgmpSnpgGroupEntry':tnSdpBindIgmpSnpgGroupEntry,_a:sdpBndIgmpSnpgGrpAddress,'sdpBndIgmpSnpgGrpType':sdpBndIgmpSnpgGrpType,'sdpBndIgmpSnpgGrpFilterMode':sdpBndIgmpSnpgGrpFilterMode,'sdpBndIgmpSnpgGrpUpTime':sdpBndIgmpSnpgGrpUpTime,'sdpBndIgmpSnpgGrpExpiryTime':sdpBndIgmpSnpgGrpExpiryTime,'sdpBndIgmpSnpgGrpCompatMode':sdpBndIgmpSnpgGrpCompatMode,'sdpBndIgmpSnpgGrpV1HostExpTime':sdpBndIgmpSnpgGrpV1HostExpTime,'sdpBndIgmpSnpgGrpV2HostExpTime':sdpBndIgmpSnpgGrpV2HostExpTime,'sdpBndIgmpSnpgGrpNumSrc':sdpBndIgmpSnpgGrpNumSrc,'tnSdpBindIgmpSnpgGrpSrcTable':tnSdpBindIgmpSnpgGrpSrcTable,'tnSdpBindIgmpSnpgGrpSrcEntry':tnSdpBindIgmpSnpgGrpSrcEntry,_n:sdpBndIgmpSnpgGrpSrcAddr,'sdpBndIgmpSnpgGrpSrcType':sdpBndIgmpSnpgGrpSrcType,'sdpBndIgmpSnpgGrpSrcUpTime':sdpBndIgmpSnpgGrpSrcUpTime,'sdpBndIgmpSnpgGrpSrcExpiryTime':sdpBndIgmpSnpgGrpSrcExpiryTime,'tnSdpBindIgmpSnpgStaticGrpSrcTable':tnSdpBindIgmpSnpgStaticGrpSrcTable,'tnSdpBindIgmpSnpgStaticGrpSrcEntry':tnSdpBindIgmpSnpgStaticGrpSrcEntry,_o:sdpBndIgmpSnpgStaticGroupAddr,_p:sdpBndIgmpSnpgStaticSourceAddr,'sdpBndIgmpSnpgStaticRowstatus':sdpBndIgmpSnpgStaticRowstatus,'sdpBndIgmpSnpgStaticLastChange':sdpBndIgmpSnpgStaticLastChange,'tnSdpBindIgmpSnpgStatsTable':tnSdpBindIgmpSnpgStatsTable,'tnSdpBindIgmpSnpgStatsEntry':tnSdpBindIgmpSnpgStatsEntry,'sdpBndIgmpSnpgTxGenQueries':sdpBndIgmpSnpgTxGenQueries,'sdpBndIgmpSnpgTxGrpSpecQueries':sdpBndIgmpSnpgTxGrpSpecQueries,'sdpBndIgmpSnpgTxSrcSpecQueries':sdpBndIgmpSnpgTxSrcSpecQueries,'sdpBndIgmpSnpgTxV1Reports':sdpBndIgmpSnpgTxV1Reports,'sdpBndIgmpSnpgTxV2Reports':sdpBndIgmpSnpgTxV2Reports,'sdpBndIgmpSnpgTxV3Reports':sdpBndIgmpSnpgTxV3Reports,'sdpBndIgmpSnpgTxV2Leaves':sdpBndIgmpSnpgTxV2Leaves,'sdpBndIgmpSnpgRxGenQueries':sdpBndIgmpSnpgRxGenQueries,'sdpBndIgmpSnpgRxGrpSpecQueries':sdpBndIgmpSnpgRxGrpSpecQueries,'sdpBndIgmpSnpgRxSrcSpecQueries':sdpBndIgmpSnpgRxSrcSpecQueries,'sdpBndIgmpSnpgRxV1Reports':sdpBndIgmpSnpgRxV1Reports,'sdpBndIgmpSnpgRxV2Reports':sdpBndIgmpSnpgRxV2Reports,'sdpBndIgmpSnpgRxV3Reports':sdpBndIgmpSnpgRxV3Reports,'sdpBndIgmpSnpgRxV2Leaves':sdpBndIgmpSnpgRxV2Leaves,'sdpBndIgmpSnpgRxUnknownType':sdpBndIgmpSnpgRxUnknownType,'sdpBndIgmpSnpgFwdGenQueries':sdpBndIgmpSnpgFwdGenQueries,'sdpBndIgmpSnpgFwdGrpSpecQueries':sdpBndIgmpSnpgFwdGrpSpecQueries,'sdpBndIgmpSnpgFwdSrcSpecQueries':sdpBndIgmpSnpgFwdSrcSpecQueries,'sdpBndIgmpSnpgFwdV1Reports':sdpBndIgmpSnpgFwdV1Reports,'sdpBndIgmpSnpgFwdV2Reports':sdpBndIgmpSnpgFwdV2Reports,'sdpBndIgmpSnpgFwdV3Reports':sdpBndIgmpSnpgFwdV3Reports,'sdpBndIgmpSnpgFwdV2Leaves':sdpBndIgmpSnpgFwdV2Leaves,'sdpBndIgmpSnpgFwdUnknownType':sdpBndIgmpSnpgFwdUnknownType,'sdpBndIgmpSnpgRxBadLenPkts':sdpBndIgmpSnpgRxBadLenPkts,'sdpBndIgmpSnpgRxBadIpChksmPkts':sdpBndIgmpSnpgRxBadIpChksmPkts,'sdpBndIgmpSnpgRxBadIgmpChksmPkts':sdpBndIgmpSnpgRxBadIgmpChksmPkts,'sdpBndIgmpSnpgRxBadEncodedPkts':sdpBndIgmpSnpgRxBadEncodedPkts,'sdpBndIgmpSnpgRxNoRtrAlertPkts':sdpBndIgmpSnpgRxNoRtrAlertPkts,'sdpBndIgmpSnpgRxZeroSrcAdrPkts':sdpBndIgmpSnpgRxZeroSrcAdrPkts,'sdpBndIgmpSnpgSendQueryCfgDrops':sdpBndIgmpSnpgSendQueryCfgDrops,'sdpBndIgmpSnpgImportPolicyDrops':sdpBndIgmpSnpgImportPolicyDrops,'sdpBndIgmpSnpgMaxNumGroupsDrops':sdpBndIgmpSnpgMaxNumGroupsDrops,'sdpBndIgmpSnpgRxWrongVersionPkts':sdpBndIgmpSnpgRxWrongVersionPkts,'sdpBndIgmpSnpgMcacPolicyDrops':sdpBndIgmpSnpgMcacPolicyDrops,'sdpBndIgmpSnpgRxLocalScopePkts':sdpBndIgmpSnpgRxLocalScopePkts,'sdpBndIgmpSnpgRxRsvdScopePkts':sdpBndIgmpSnpgRxRsvdScopePkts,'sdpBndIgmpSnpgMaxNumSourcesDrops':sdpBndIgmpSnpgMaxNumSourcesDrops,'sdpBndIgmpSnpgNumGrps':sdpBndIgmpSnpgNumGrps,'sdpBndIgmpSnpgRxQueryDrops':sdpBndIgmpSnpgRxQueryDrops,'tnIgmpSnoopingNotifyPrefix':tnIgmpSnoopingNotifyPrefix,'tnIgmpSnoopingSapPrefix':tnIgmpSnoopingSapPrefix,'tnIgmpSnpgSapNotifications':tnIgmpSnpgSapNotifications})