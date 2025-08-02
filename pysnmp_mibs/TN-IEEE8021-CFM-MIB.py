_A6='tnDot1agCfmMepOndemandLmUnack'
_A5='tnDot1agCfmMepOndemandLmTfLF'
_A4='tnDot1agCfmMepOndemandLmTfTF'
_A3='tnDot1agCfmMepOndemandLmTnLF'
_A2='tnDot1agCfmMepOndemandLmTnTF'
_A1='tnDot1agCfmMepSlmPacketUnack'
_A0='tnDot1agCfmMepSlmPacketLossOut'
_z='tnDot1agCfmMepSlmPacketLossIn'
_y='tnDot1agCfmMepSlmPacketIn'
_x='tnDot1agCfmMepSlmLastTxSeqF'
_w='tnDot1agCfmMepSlmRemoteMepId'
_v='tnDot1agCfmMepSlmTestId'
_u='tnDot1agCfmMepEthRxAis'
_t='tnDot1agCfmMepDelayTestDelay'
_s='tnDot1agCfmMepOndemandLmTestEntry'
_r='tnDot1agCfmMepSlmOWTestEntry'
_q='tnDot1agCfmMepSlmTWTestEntry'
_p='tnDot1agCfmMepCsfEntry'
_o='tnDot1agCfmMepEntry'
_n='tnDot1agCfmMaMepListEntry'
_m='tnDot1agCfmMaNetEntry'
_l='tnDot1agCfmMepSlmRemoteMacAddr'
_k='tnDot1agCfmMepSlmTestType'
_j='twoWayTest'
_i='oneWayTest'
_h='tnDot1agCfmMepDelayTestType'
_g='tnDot1agCfmMepDelaySrcMacAddr'
_f='tnDot1agCfmCompMinorIndex'
_e='tnDot1agCfmCompMajorIndex'
_d='tnDot1agCfmStackDirection'
_c='tnDot1agCfmStackMdLevel'
_b='tnDot1agCfmStackVlanIdOrNone'
_a='tnDot1agCfmStackifIndex'
_Z='dot1agCfmMepTransmitLtmSeqNumber'
_Y='dot1agCfmMepTransmitLbmDestMacAddress'
_X='OctetString'
_W='read-write'
_V='tnSysSwitchId'
_U='TROPIC-SYSTEM-MIB'
_T='Dot1agCfmCcmInterval'
_S='TmnxEnabledDisabled'
_R='bytes'
_Q='dot1agCfmMepIdentifier'
_P='dot1agCfmMdIndex'
_O='dot1agCfmMaIndex'
_N='TruthValue'
_M='000000000000'
_L='seconds'
_K='MacAddress'
_J='microseconds'
_I='not-accessible'
_H='packets'
_G='Integer32'
_F='IEEE8021-CFM-MIB'
_E='Unsigned32'
_D='TN-IEEE8021-CFM-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_X,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dot1agCfmCcmInterval,Dot1agCfmMDLevel,Dot1agCfmMepId,Dot1agCfmMepIdOrZero,Dot1agCfmMpDirection,dot1agCfmMaIndex,dot1agCfmMaMepListEntry,dot1agCfmMaNetEntry,dot1agCfmMdIndex,dot1agCfmMepEntry,dot1agCfmMepIdentifier,dot1agCfmMepTransmitLbmDestMacAddress,dot1agCfmMepTransmitLtmSeqNumber=mibBuilder.importSymbols(_F,_T,'Dot1agCfmMDLevel','Dot1agCfmMepId','Dot1agCfmMepIdOrZero','Dot1agCfmMpDirection',_O,'dot1agCfmMaMepListEntry','dot1agCfmMaNetEntry',_P,'dot1agCfmMepEntry',_Q,_Y,_Z)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_K,'PhysAddress','TextualConvention',_N)
SdpId,=mibBuilder.importSymbols('TN-SERV-MIB','SdpId')
TNamedItem,TmnxEnabledDisabled,TmnxServId=mibBuilder.importSymbols('TN-TC-MIB','TNamedItem',_S,'TmnxServId')
tnSRMIBModules,tnSRNotifyPrefix,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRNotifyPrefix','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_U,_V)
tnIEEE8021CfmMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,52))
if mibBuilder.loadTexts:tnIEEE8021CfmMIBModule.setRevisions(('2021-09-17 12:00','2021-06-04 12:00','2020-05-22 12:00','2019-11-22 12:00','2019-08-03 12:00','2019-05-03 12:00','2019-03-29 12:00','2017-10-06 12:00','2015-05-08 12:00','2014-09-18 12:00','2014-07-24 12:00','2014-02-10 00:00','2013-08-22 00:00','2012-12-13 00:00','2012-12-05 00:00','2012-09-09 12:00','2012-03-29 12:00','2009-02-28 00:00','2008-01-01 00:00'))
class NokiaPmonUnitType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('hundred-nano-seconds',2),('nano-seconds',3)))
_TnDot1agMIBObjs_ObjectIdentity=ObjectIdentity
tnDot1agMIBObjs=_TnDot1agMIBObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,52))
_TnDot1agCfmStack_ObjectIdentity=ObjectIdentity
tnDot1agCfmStack=_TnDot1agCfmStack_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,52,1))
_TnDot1agCfmStackTable_Object=MibTable
tnDot1agCfmStackTable=_TnDot1agCfmStackTable_Object((1,3,6,1,4,1,7483,6,1,2,52,1,2))
if mibBuilder.loadTexts:tnDot1agCfmStackTable.setStatus(_A)
_TnDot1agCfmStackEntry_Object=MibTableRow
tnDot1agCfmStackEntry=_TnDot1agCfmStackEntry_Object((1,3,6,1,4,1,7483,6,1,2,52,1,2,1))
tnDot1agCfmStackEntry.setIndexNames((0,_D,_a),(0,_D,_b),(0,_D,_c),(0,_D,_d))
if mibBuilder.loadTexts:tnDot1agCfmStackEntry.setStatus(_A)
_TnDot1agCfmStackifIndex_Type=InterfaceIndex
_TnDot1agCfmStackifIndex_Object=MibTableColumn
tnDot1agCfmStackifIndex=_TnDot1agCfmStackifIndex_Object((1,3,6,1,4,1,7483,6,1,2,52,1,2,1,1),_TnDot1agCfmStackifIndex_Type())
tnDot1agCfmStackifIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:tnDot1agCfmStackifIndex.setStatus(_A)
_TnDot1agCfmStackVlanIdOrNone_Type=Unsigned32
_TnDot1agCfmStackVlanIdOrNone_Object=MibTableColumn
tnDot1agCfmStackVlanIdOrNone=_TnDot1agCfmStackVlanIdOrNone_Object((1,3,6,1,4,1,7483,6,1,2,52,1,2,1,2),_TnDot1agCfmStackVlanIdOrNone_Type())
tnDot1agCfmStackVlanIdOrNone.setMaxAccess(_I)
if mibBuilder.loadTexts:tnDot1agCfmStackVlanIdOrNone.setStatus(_A)
_TnDot1agCfmStackMdLevel_Type=Dot1agCfmMDLevel
_TnDot1agCfmStackMdLevel_Object=MibTableColumn
tnDot1agCfmStackMdLevel=_TnDot1agCfmStackMdLevel_Object((1,3,6,1,4,1,7483,6,1,2,52,1,2,1,3),_TnDot1agCfmStackMdLevel_Type())
tnDot1agCfmStackMdLevel.setMaxAccess(_I)
if mibBuilder.loadTexts:tnDot1agCfmStackMdLevel.setStatus(_A)
_TnDot1agCfmStackDirection_Type=Dot1agCfmMpDirection
_TnDot1agCfmStackDirection_Object=MibTableColumn
tnDot1agCfmStackDirection=_TnDot1agCfmStackDirection_Object((1,3,6,1,4,1,7483,6,1,2,52,1,2,1,4),_TnDot1agCfmStackDirection_Type())
tnDot1agCfmStackDirection.setMaxAccess(_I)
if mibBuilder.loadTexts:tnDot1agCfmStackDirection.setStatus(_A)
_TnDot1agCfmStackMdIndex_Type=Unsigned32
_TnDot1agCfmStackMdIndex_Object=MibTableColumn
tnDot1agCfmStackMdIndex=_TnDot1agCfmStackMdIndex_Object((1,3,6,1,4,1,7483,6,1,2,52,1,2,1,5),_TnDot1agCfmStackMdIndex_Type())
tnDot1agCfmStackMdIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmStackMdIndex.setStatus(_A)
_TnDot1agCfmStackMaIndex_Type=Unsigned32
_TnDot1agCfmStackMaIndex_Object=MibTableColumn
tnDot1agCfmStackMaIndex=_TnDot1agCfmStackMaIndex_Object((1,3,6,1,4,1,7483,6,1,2,52,1,2,1,6),_TnDot1agCfmStackMaIndex_Type())
tnDot1agCfmStackMaIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmStackMaIndex.setStatus(_A)
_TnDot1agCfmStackMepId_Type=Dot1agCfmMepIdOrZero
_TnDot1agCfmStackMepId_Object=MibTableColumn
tnDot1agCfmStackMepId=_TnDot1agCfmStackMepId_Object((1,3,6,1,4,1,7483,6,1,2,52,1,2,1,7),_TnDot1agCfmStackMepId_Type())
tnDot1agCfmStackMepId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmStackMepId.setStatus(_A)
_TnDot1agCfmStackMacAddress_Type=MacAddress
_TnDot1agCfmStackMacAddress_Object=MibTableColumn
tnDot1agCfmStackMacAddress=_TnDot1agCfmStackMacAddress_Object((1,3,6,1,4,1,7483,6,1,2,52,1,2,1,8),_TnDot1agCfmStackMacAddress_Type())
tnDot1agCfmStackMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmStackMacAddress.setStatus(_A)
class _TnDot1agCfmStackMPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('sap',1),('ethTun',2),('ethRing',3),('facPort',4),('facInterface',5)))
_TnDot1agCfmStackMPType_Type.__name__=_G
_TnDot1agCfmStackMPType_Object=MibTableColumn
tnDot1agCfmStackMPType=_TnDot1agCfmStackMPType_Object((1,3,6,1,4,1,7483,6,1,2,52,1,2,1,9),_TnDot1agCfmStackMPType_Type())
tnDot1agCfmStackMPType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmStackMPType.setStatus(_A)
_TnDot1agCfmGlobalObjs_ObjectIdentity=ObjectIdentity
tnDot1agCfmGlobalObjs=_TnDot1agCfmGlobalObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,52,2))
_TnDot1agCfmMcLagConfigTable_Object=MibTable
tnDot1agCfmMcLagConfigTable=_TnDot1agCfmMcLagConfigTable_Object((1,3,6,1,4,1,7483,6,1,2,52,2,1))
if mibBuilder.loadTexts:tnDot1agCfmMcLagConfigTable.setStatus(_A)
_TnDot1agCfmMcLagConfigEntry_Object=MibTableRow
tnDot1agCfmMcLagConfigEntry=_TnDot1agCfmMcLagConfigEntry_Object((1,3,6,1,4,1,7483,6,1,2,52,2,1,1))
tnDot1agCfmMcLagConfigEntry.setIndexNames((0,_U,_V))
if mibBuilder.loadTexts:tnDot1agCfmMcLagConfigEntry.setStatus(_A)
class _TnDot1agCfmMcLagConfigStdbyInactive_Type(TruthValue):defaultValue=2
_TnDot1agCfmMcLagConfigStdbyInactive_Type.__name__=_N
_TnDot1agCfmMcLagConfigStdbyInactive_Object=MibTableColumn
tnDot1agCfmMcLagConfigStdbyInactive=_TnDot1agCfmMcLagConfigStdbyInactive_Object((1,3,6,1,4,1,7483,6,1,2,52,2,1,1,1),_TnDot1agCfmMcLagConfigStdbyInactive_Type())
tnDot1agCfmMcLagConfigStdbyInactive.setMaxAccess(_W)
if mibBuilder.loadTexts:tnDot1agCfmMcLagConfigStdbyInactive.setStatus(_A)
class _TnDot1agCfmMcLagConfigPropHoldTime_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_TnDot1agCfmMcLagConfigPropHoldTime_Type.__name__=_E
_TnDot1agCfmMcLagConfigPropHoldTime_Object=MibTableColumn
tnDot1agCfmMcLagConfigPropHoldTime=_TnDot1agCfmMcLagConfigPropHoldTime_Object((1,3,6,1,4,1,7483,6,1,2,52,2,1,1,2),_TnDot1agCfmMcLagConfigPropHoldTime_Type())
tnDot1agCfmMcLagConfigPropHoldTime.setMaxAccess(_W)
if mibBuilder.loadTexts:tnDot1agCfmMcLagConfigPropHoldTime.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMcLagConfigPropHoldTime.setUnits(_L)
_TnDot1agCfmStatisticsGroup_ObjectIdentity=ObjectIdentity
tnDot1agCfmStatisticsGroup=_TnDot1agCfmStatisticsGroup_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,52,2,3))
_TnDot1agCfmComponentLimitTable_Object=MibTable
tnDot1agCfmComponentLimitTable=_TnDot1agCfmComponentLimitTable_Object((1,3,6,1,4,1,7483,6,1,2,52,2,3,1))
if mibBuilder.loadTexts:tnDot1agCfmComponentLimitTable.setStatus(_A)
_TnDot1agCfmComponentLimitEntry_Object=MibTableRow
tnDot1agCfmComponentLimitEntry=_TnDot1agCfmComponentLimitEntry_Object((1,3,6,1,4,1,7483,6,1,2,52,2,3,1,1))
tnDot1agCfmComponentLimitEntry.setIndexNames((0,_U,_V),(0,_D,_e),(0,_D,_f))
if mibBuilder.loadTexts:tnDot1agCfmComponentLimitEntry.setStatus(_A)
_TnDot1agCfmCompMajorIndex_Type=Unsigned32
_TnDot1agCfmCompMajorIndex_Object=MibTableColumn
tnDot1agCfmCompMajorIndex=_TnDot1agCfmCompMajorIndex_Object((1,3,6,1,4,1,7483,6,1,2,52,2,3,1,1,1),_TnDot1agCfmCompMajorIndex_Type())
tnDot1agCfmCompMajorIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:tnDot1agCfmCompMajorIndex.setStatus(_A)
_TnDot1agCfmCompMinorIndex_Type=Unsigned32
_TnDot1agCfmCompMinorIndex_Object=MibTableColumn
tnDot1agCfmCompMinorIndex=_TnDot1agCfmCompMinorIndex_Object((1,3,6,1,4,1,7483,6,1,2,52,2,3,1,1,2),_TnDot1agCfmCompMinorIndex_Type())
tnDot1agCfmCompMinorIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:tnDot1agCfmCompMinorIndex.setStatus(_A)
_TnDot1agCfmCompName_Type=TNamedItem
_TnDot1agCfmCompName_Object=MibTableColumn
tnDot1agCfmCompName=_TnDot1agCfmCompName_Object((1,3,6,1,4,1,7483,6,1,2,52,2,3,1,1,3),_TnDot1agCfmCompName_Type())
tnDot1agCfmCompName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmCompName.setStatus(_A)
_TnDot1agCfmCompResourceUsage_Type=Unsigned32
_TnDot1agCfmCompResourceUsage_Object=MibTableColumn
tnDot1agCfmCompResourceUsage=_TnDot1agCfmCompResourceUsage_Object((1,3,6,1,4,1,7483,6,1,2,52,2,3,1,1,4),_TnDot1agCfmCompResourceUsage_Type())
tnDot1agCfmCompResourceUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmCompResourceUsage.setStatus(_A)
_TnDot1agCfmCompResourceLimit_Type=Unsigned32
_TnDot1agCfmCompResourceLimit_Object=MibTableColumn
tnDot1agCfmCompResourceLimit=_TnDot1agCfmCompResourceLimit_Object((1,3,6,1,4,1,7483,6,1,2,52,2,3,1,1,5),_TnDot1agCfmCompResourceLimit_Type())
tnDot1agCfmCompResourceLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmCompResourceLimit.setStatus(_A)
_TnDot1agCfmGlobalScalar1_Type=Unsigned32
_TnDot1agCfmGlobalScalar1_Object=MibScalar
tnDot1agCfmGlobalScalar1=_TnDot1agCfmGlobalScalar1_Object((1,3,6,1,4,1,7483,6,1,2,52,2,101),_TnDot1agCfmGlobalScalar1_Type())
tnDot1agCfmGlobalScalar1.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmGlobalScalar1.setStatus(_A)
_TnDot1agCfmGlobalScalar2_Type=Unsigned32
_TnDot1agCfmGlobalScalar2_Object=MibScalar
tnDot1agCfmGlobalScalar2=_TnDot1agCfmGlobalScalar2_Object((1,3,6,1,4,1,7483,6,1,2,52,2,102),_TnDot1agCfmGlobalScalar2_Type())
tnDot1agCfmGlobalScalar2.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmGlobalScalar2.setStatus(_A)
_TnDot1agCfmMa_ObjectIdentity=ObjectIdentity
tnDot1agCfmMa=_TnDot1agCfmMa_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,52,6))
_TnDot1agCfmMaNetTable_Object=MibTable
tnDot1agCfmMaNetTable=_TnDot1agCfmMaNetTable_Object((1,3,6,1,4,1,7483,6,1,2,52,6,1))
if mibBuilder.loadTexts:tnDot1agCfmMaNetTable.setStatus(_A)
_TnDot1agCfmMaNetEntry_Object=MibTableRow
tnDot1agCfmMaNetEntry=_TnDot1agCfmMaNetEntry_Object((1,3,6,1,4,1,7483,6,1,2,52,6,1,1))
if mibBuilder.loadTexts:tnDot1agCfmMaNetEntry.setStatus(_A)
_TnDot1agCfmMaNetTotalMEPCount_Type=Counter32
_TnDot1agCfmMaNetTotalMEPCount_Object=MibTableColumn
tnDot1agCfmMaNetTotalMEPCount=_TnDot1agCfmMaNetTotalMEPCount_Object((1,3,6,1,4,1,7483,6,1,2,52,6,1,1,1),_TnDot1agCfmMaNetTotalMEPCount_Type())
tnDot1agCfmMaNetTotalMEPCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMaNetTotalMEPCount.setStatus(_A)
_TnDot1agCfmMaMepListTable_Object=MibTable
tnDot1agCfmMaMepListTable=_TnDot1agCfmMaMepListTable_Object((1,3,6,1,4,1,7483,6,1,2,52,6,3))
if mibBuilder.loadTexts:tnDot1agCfmMaMepListTable.setStatus(_A)
_TnDot1agCfmMaMepListEntry_Object=MibTableRow
tnDot1agCfmMaMepListEntry=_TnDot1agCfmMaMepListEntry_Object((1,3,6,1,4,1,7483,6,1,2,52,6,3,1))
if mibBuilder.loadTexts:tnDot1agCfmMaMepListEntry.setStatus(_A)
class _TnDot1agCfmMaMepListMacAddress_Type(MacAddress):defaultHexValue=_M
_TnDot1agCfmMaMepListMacAddress_Type.__name__=_K
_TnDot1agCfmMaMepListMacAddress_Object=MibTableColumn
tnDot1agCfmMaMepListMacAddress=_TnDot1agCfmMaMepListMacAddress_Object((1,3,6,1,4,1,7483,6,1,2,52,6,3,1,1),_TnDot1agCfmMaMepListMacAddress_Type())
tnDot1agCfmMaMepListMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMaMepListMacAddress.setStatus(_A)
class _TnDot1agCfmMaMepListSapSubType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('regular',0),('etree-root',1),('etree-leaf',2)))
_TnDot1agCfmMaMepListSapSubType_Type.__name__=_G
_TnDot1agCfmMaMepListSapSubType_Object=MibTableColumn
tnDot1agCfmMaMepListSapSubType=_TnDot1agCfmMaMepListSapSubType_Object((1,3,6,1,4,1,7483,6,1,2,52,6,3,1,2),_TnDot1agCfmMaMepListSapSubType_Type())
tnDot1agCfmMaMepListSapSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMaMepListSapSubType.setStatus(_A)
_TnDot1agCfmMep_ObjectIdentity=ObjectIdentity
tnDot1agCfmMep=_TnDot1agCfmMep_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,52,7))
_TnDot1agCfmMepTable_Object=MibTable
tnDot1agCfmMepTable=_TnDot1agCfmMepTable_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1))
if mibBuilder.loadTexts:tnDot1agCfmMepTable.setStatus(_A)
_TnDot1agCfmMepEntry_Object=MibTableRow
tnDot1agCfmMepEntry=_TnDot1agCfmMepEntry_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1))
if mibBuilder.loadTexts:tnDot1agCfmMepEntry.setStatus(_A)
_TnDot1agCfmMepSdpId_Type=SdpId
_TnDot1agCfmMepSdpId_Object=MibTableColumn
tnDot1agCfmMepSdpId=_TnDot1agCfmMepSdpId_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,1),_TnDot1agCfmMepSdpId_Type())
tnDot1agCfmMepSdpId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSdpId.setStatus(_A)
_TnDot1agCfmMepVcId_Type=Unsigned32
_TnDot1agCfmMepVcId_Object=MibTableColumn
tnDot1agCfmMepVcId=_TnDot1agCfmMepVcId_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,2),_TnDot1agCfmMepVcId_Type())
tnDot1agCfmMepVcId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepVcId.setStatus(_A)
_TnDot1agCfmMepMacAddress_Type=MacAddress
_TnDot1agCfmMepMacAddress_Object=MibTableColumn
tnDot1agCfmMepMacAddress=_TnDot1agCfmMepMacAddress_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,3),_TnDot1agCfmMepMacAddress_Type())
tnDot1agCfmMepMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepMacAddress.setStatus(_A)
class _TnDot1agCfmMepAisEnable_Type(TruthValue):defaultValue=2
_TnDot1agCfmMepAisEnable_Type.__name__=_N
_TnDot1agCfmMepAisEnable_Object=MibTableColumn
tnDot1agCfmMepAisEnable=_TnDot1agCfmMepAisEnable_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,4),_TnDot1agCfmMepAisEnable_Type())
tnDot1agCfmMepAisEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepAisEnable.setStatus(_A)
class _TnDot1agCfmMepAisMegLevel_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('level1',0),('level2',1),('level3',2),('level4',3),('level5',4),('level6',5),('level7',6)))
_TnDot1agCfmMepAisMegLevel_Type.__name__='Bits'
_TnDot1agCfmMepAisMegLevel_Object=MibTableColumn
tnDot1agCfmMepAisMegLevel=_TnDot1agCfmMepAisMegLevel_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,5),_TnDot1agCfmMepAisMegLevel_Type())
tnDot1agCfmMepAisMegLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepAisMegLevel.setStatus(_A)
class _TnDot1agCfmMepAisPriority_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TnDot1agCfmMepAisPriority_Type.__name__=_E
_TnDot1agCfmMepAisPriority_Object=MibTableColumn
tnDot1agCfmMepAisPriority=_TnDot1agCfmMepAisPriority_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,6),_TnDot1agCfmMepAisPriority_Type())
tnDot1agCfmMepAisPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepAisPriority.setStatus(_A)
class _TnDot1agCfmMepAisInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(60,60))
_TnDot1agCfmMepAisInterval_Type.__name__=_E
_TnDot1agCfmMepAisInterval_Object=MibTableColumn
tnDot1agCfmMepAisInterval=_TnDot1agCfmMepAisInterval_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,7),_TnDot1agCfmMepAisInterval_Type())
tnDot1agCfmMepAisInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepAisInterval.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepAisInterval.setUnits(_L)
class _TnDot1agCfmMepEthRxAisInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(60,60))
_TnDot1agCfmMepEthRxAisInterval_Type.__name__=_E
_TnDot1agCfmMepEthRxAisInterval_Object=MibTableColumn
tnDot1agCfmMepEthRxAisInterval=_TnDot1agCfmMepEthRxAisInterval_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,8),_TnDot1agCfmMepEthRxAisInterval_Type())
tnDot1agCfmMepEthRxAisInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepEthRxAisInterval.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepEthRxAisInterval.setUnits(_L)
class _TnDot1agCfmMepEthRxAis_Type(TruthValue):defaultValue=2
_TnDot1agCfmMepEthRxAis_Type.__name__=_N
_TnDot1agCfmMepEthRxAis_Object=MibTableColumn
tnDot1agCfmMepEthRxAis=_TnDot1agCfmMepEthRxAis_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,9),_TnDot1agCfmMepEthRxAis_Type())
tnDot1agCfmMepEthRxAis.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepEthRxAis.setStatus(_A)
_TnDot1agCfmMepEthAisTxCount_Type=Counter32
_TnDot1agCfmMepEthAisTxCount_Object=MibTableColumn
tnDot1agCfmMepEthAisTxCount=_TnDot1agCfmMepEthAisTxCount_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,10),_TnDot1agCfmMepEthAisTxCount_Type())
tnDot1agCfmMepEthAisTxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepEthAisTxCount.setStatus(_A)
class _TnDot1agCfmMepEthTestEnable_Type(TruthValue):defaultValue=2
_TnDot1agCfmMepEthTestEnable_Type.__name__=_N
_TnDot1agCfmMepEthTestEnable_Object=MibTableColumn
tnDot1agCfmMepEthTestEnable=_TnDot1agCfmMepEthTestEnable_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,11),_TnDot1agCfmMepEthTestEnable_Type())
tnDot1agCfmMepEthTestEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepEthTestEnable.setStatus(_A)
class _TnDot1agCfmMepEthTestPattern_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('allZerosNoCrc',0),('allZerosCrc',1),('prbsNoCrc',2),('prbsCrc',3),('allOnesNoCrc',4),('allOnesCrc',5)))
_TnDot1agCfmMepEthTestPattern_Type.__name__=_G
_TnDot1agCfmMepEthTestPattern_Object=MibTableColumn
tnDot1agCfmMepEthTestPattern=_TnDot1agCfmMepEthTestPattern_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,12),_TnDot1agCfmMepEthTestPattern_Type())
tnDot1agCfmMepEthTestPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepEthTestPattern.setStatus(_A)
class _TnDot1agCfmMepEthTestMacAddr_Type(MacAddress):defaultHexValue=_M
_TnDot1agCfmMepEthTestMacAddr_Type.__name__=_K
_TnDot1agCfmMepEthTestMacAddr_Object=MibTableColumn
tnDot1agCfmMepEthTestMacAddr=_TnDot1agCfmMepEthTestMacAddr_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,13),_TnDot1agCfmMepEthTestMacAddr_Type())
tnDot1agCfmMepEthTestMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepEthTestMacAddr.setStatus(_A)
class _TnDot1agCfmMepEthTestDataLen_Type(Unsigned32):defaultValue=64;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1500))
_TnDot1agCfmMepEthTestDataLen_Type.__name__=_E
_TnDot1agCfmMepEthTestDataLen_Object=MibTableColumn
tnDot1agCfmMepEthTestDataLen=_TnDot1agCfmMepEthTestDataLen_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,14),_TnDot1agCfmMepEthTestDataLen_Type())
tnDot1agCfmMepEthTestDataLen.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepEthTestDataLen.setStatus(_A)
class _TnDot1agCfmMepEthTestPriority_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TnDot1agCfmMepEthTestPriority_Type.__name__=_E
_TnDot1agCfmMepEthTestPriority_Object=MibTableColumn
tnDot1agCfmMepEthTestPriority=_TnDot1agCfmMepEthTestPriority_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,15),_TnDot1agCfmMepEthTestPriority_Type())
tnDot1agCfmMepEthTestPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepEthTestPriority.setStatus(_A)
class _TnDot1agCfmMepOWDTMacAddress_Type(MacAddress):defaultHexValue=_M
_TnDot1agCfmMepOWDTMacAddress_Type.__name__=_K
_TnDot1agCfmMepOWDTMacAddress_Object=MibTableColumn
tnDot1agCfmMepOWDTMacAddress=_TnDot1agCfmMepOWDTMacAddress_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,16),_TnDot1agCfmMepOWDTMacAddress_Type())
tnDot1agCfmMepOWDTMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepOWDTMacAddress.setStatus(_A)
class _TnDot1agCfmMepOWDTPriority_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TnDot1agCfmMepOWDTPriority_Type.__name__=_E
_TnDot1agCfmMepOWDTPriority_Object=MibTableColumn
tnDot1agCfmMepOWDTPriority=_TnDot1agCfmMepOWDTPriority_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,17),_TnDot1agCfmMepOWDTPriority_Type())
tnDot1agCfmMepOWDTPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepOWDTPriority.setStatus(_A)
class _TnDot1agCfmMepTWDTMacAddress_Type(MacAddress):defaultHexValue=_M
_TnDot1agCfmMepTWDTMacAddress_Type.__name__=_K
_TnDot1agCfmMepTWDTMacAddress_Object=MibTableColumn
tnDot1agCfmMepTWDTMacAddress=_TnDot1agCfmMepTWDTMacAddress_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,18),_TnDot1agCfmMepTWDTMacAddress_Type())
tnDot1agCfmMepTWDTMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepTWDTMacAddress.setStatus(_A)
class _TnDot1agCfmMepTWDTPriority_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TnDot1agCfmMepTWDTPriority_Type.__name__=_E
_TnDot1agCfmMepTWDTPriority_Object=MibTableColumn
tnDot1agCfmMepTWDTPriority=_TnDot1agCfmMepTWDTPriority_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,19),_TnDot1agCfmMepTWDTPriority_Type())
tnDot1agCfmMepTWDTPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepTWDTPriority.setStatus(_A)
_TnDot1agCfmMepSvcId_Type=TmnxServId
_TnDot1agCfmMepSvcId_Object=MibTableColumn
tnDot1agCfmMepSvcId=_TnDot1agCfmMepSvcId_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,20),_TnDot1agCfmMepSvcId_Type())
tnDot1agCfmMepSvcId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSvcId.setStatus(_A)
class _TnDot1agCfmMepControlMep_Type(TruthValue):defaultValue=2
_TnDot1agCfmMepControlMep_Type.__name__=_N
_TnDot1agCfmMepControlMep_Object=MibTableColumn
tnDot1agCfmMepControlMep=_TnDot1agCfmMepControlMep_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,21),_TnDot1agCfmMepControlMep_Type())
tnDot1agCfmMepControlMep.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepControlMep.setStatus(_A)
class _TnDot1agCfmMepEthTestThreshold_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11840))
_TnDot1agCfmMepEthTestThreshold_Type.__name__=_E
_TnDot1agCfmMepEthTestThreshold_Object=MibTableColumn
tnDot1agCfmMepEthTestThreshold=_TnDot1agCfmMepEthTestThreshold_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,22),_TnDot1agCfmMepEthTestThreshold_Type())
tnDot1agCfmMepEthTestThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepEthTestThreshold.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepEthTestThreshold.setUnits('bit-errors')
class _TnDot1agCfmMepOWDTThreshold_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_TnDot1agCfmMepOWDTThreshold_Type.__name__=_E
_TnDot1agCfmMepOWDTThreshold_Object=MibTableColumn
tnDot1agCfmMepOWDTThreshold=_TnDot1agCfmMepOWDTThreshold_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,23),_TnDot1agCfmMepOWDTThreshold_Type())
tnDot1agCfmMepOWDTThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepOWDTThreshold.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepOWDTThreshold.setUnits(_L)
class _TnDot1agCfmMepMcLagInactive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notApplicable',0),('standby',1),('active',2)))
_TnDot1agCfmMepMcLagInactive_Type.__name__=_G
_TnDot1agCfmMepMcLagInactive_Object=MibTableColumn
tnDot1agCfmMepMcLagInactive=_TnDot1agCfmMepMcLagInactive_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,24),_TnDot1agCfmMepMcLagInactive_Type())
tnDot1agCfmMepMcLagInactive.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepMcLagInactive.setStatus(_A)
class _TnDot1agCfmMepTWDTDataSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9542))
_TnDot1agCfmMepTWDTDataSize_Type.__name__=_E
_TnDot1agCfmMepTWDTDataSize_Object=MibTableColumn
tnDot1agCfmMepTWDTDataSize=_TnDot1agCfmMepTWDTDataSize_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,25),_TnDot1agCfmMepTWDTDataSize_Type())
tnDot1agCfmMepTWDTDataSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepTWDTDataSize.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepTWDTDataSize.setUnits(_R)
class _TnDot1agCfmMepTransmitLbmDataTlvSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9570))
_TnDot1agCfmMepTransmitLbmDataTlvSize_Type.__name__=_E
_TnDot1agCfmMepTransmitLbmDataTlvSize_Object=MibTableColumn
tnDot1agCfmMepTransmitLbmDataTlvSize=_TnDot1agCfmMepTransmitLbmDataTlvSize_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,26),_TnDot1agCfmMepTransmitLbmDataTlvSize_Type())
tnDot1agCfmMepTransmitLbmDataTlvSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepTransmitLbmDataTlvSize.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepTransmitLbmDataTlvSize.setUnits(_R)
class _TnDot1agCfmMepType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('default',0),('facilityPort',1),('facilityInterface',2),('sapPrimaryVlan',3)))
_TnDot1agCfmMepType_Type.__name__=_G
_TnDot1agCfmMepType_Object=MibTableColumn
tnDot1agCfmMepType=_TnDot1agCfmMepType_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,27),_TnDot1agCfmMepType_Type())
tnDot1agCfmMepType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepType.setStatus(_A)
class _TnDot1agCfmMepFaultPropagation_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disabled',0),('useIfStatusTLV',1),('suspendCCM',2)))
_TnDot1agCfmMepFaultPropagation_Type.__name__=_G
_TnDot1agCfmMepFaultPropagation_Object=MibTableColumn
tnDot1agCfmMepFaultPropagation=_TnDot1agCfmMepFaultPropagation_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,28),_TnDot1agCfmMepFaultPropagation_Type())
tnDot1agCfmMepFaultPropagation.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepFaultPropagation.setStatus(_A)
class _TnDot1agCfmMepOWDTDataSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9542))
_TnDot1agCfmMepOWDTDataSize_Type.__name__=_E
_TnDot1agCfmMepOWDTDataSize_Object=MibTableColumn
tnDot1agCfmMepOWDTDataSize=_TnDot1agCfmMepOWDTDataSize_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,29),_TnDot1agCfmMepOWDTDataSize_Type())
tnDot1agCfmMepOWDTDataSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepOWDTDataSize.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepOWDTDataSize.setUnits(_R)
class _TnDot1agCfmMepAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnDot1agCfmMepAlmProfName_Type.__name__=_X
_TnDot1agCfmMepAlmProfName_Object=MibTableColumn
tnDot1agCfmMepAlmProfName=_TnDot1agCfmMepAlmProfName_Object((1,3,6,1,4,1,7483,6,1,2,52,7,1,1,30),_TnDot1agCfmMepAlmProfName_Type())
tnDot1agCfmMepAlmProfName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepAlmProfName.setStatus(_A)
_TnDot1agCfmMepDelayRsltTable_Object=MibTable
tnDot1agCfmMepDelayRsltTable=_TnDot1agCfmMepDelayRsltTable_Object((1,3,6,1,4,1,7483,6,1,2,52,7,3))
if mibBuilder.loadTexts:tnDot1agCfmMepDelayRsltTable.setStatus(_A)
_TnDot1agCfmMepDelayRsltEntry_Object=MibTableRow
tnDot1agCfmMepDelayRsltEntry=_TnDot1agCfmMepDelayRsltEntry_Object((1,3,6,1,4,1,7483,6,1,2,52,7,3,1))
tnDot1agCfmMepDelayRsltEntry.setIndexNames((0,_F,_P),(0,_F,_O),(0,_F,_Q),(0,_D,_g),(0,_D,_h))
if mibBuilder.loadTexts:tnDot1agCfmMepDelayRsltEntry.setStatus(_A)
_TnDot1agCfmMepDelaySrcMacAddr_Type=MacAddress
_TnDot1agCfmMepDelaySrcMacAddr_Object=MibTableColumn
tnDot1agCfmMepDelaySrcMacAddr=_TnDot1agCfmMepDelaySrcMacAddr_Object((1,3,6,1,4,1,7483,6,1,2,52,7,3,1,1),_TnDot1agCfmMepDelaySrcMacAddr_Type())
tnDot1agCfmMepDelaySrcMacAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:tnDot1agCfmMepDelaySrcMacAddr.setStatus(_A)
class _TnDot1agCfmMepDelayTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),(_j,2)))
_TnDot1agCfmMepDelayTestType_Type.__name__=_G
_TnDot1agCfmMepDelayTestType_Object=MibTableColumn
tnDot1agCfmMepDelayTestType=_TnDot1agCfmMepDelayTestType_Object((1,3,6,1,4,1,7483,6,1,2,52,7,3,1,2),_TnDot1agCfmMepDelayTestType_Type())
tnDot1agCfmMepDelayTestType.setMaxAccess(_I)
if mibBuilder.loadTexts:tnDot1agCfmMepDelayTestType.setStatus(_A)
_TnDot1agCfmMepDelayTestDelay_Type=Integer32
_TnDot1agCfmMepDelayTestDelay_Object=MibTableColumn
tnDot1agCfmMepDelayTestDelay=_TnDot1agCfmMepDelayTestDelay_Object((1,3,6,1,4,1,7483,6,1,2,52,7,3,1,3),_TnDot1agCfmMepDelayTestDelay_Type())
tnDot1agCfmMepDelayTestDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepDelayTestDelay.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepDelayTestDelay.setUnits(_J)
_TnDot1agCfmMepDelayVariation_Type=Unsigned32
_TnDot1agCfmMepDelayVariation_Object=MibTableColumn
tnDot1agCfmMepDelayVariation=_TnDot1agCfmMepDelayVariation_Object((1,3,6,1,4,1,7483,6,1,2,52,7,3,1,4),_TnDot1agCfmMepDelayVariation_Type())
tnDot1agCfmMepDelayVariation.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepDelayVariation.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepDelayVariation.setUnits(_J)
_TnDot1agCfmMepDelayNearEndTestDelay_Type=Integer32
_TnDot1agCfmMepDelayNearEndTestDelay_Object=MibTableColumn
tnDot1agCfmMepDelayNearEndTestDelay=_TnDot1agCfmMepDelayNearEndTestDelay_Object((1,3,6,1,4,1,7483,6,1,2,52,7,3,1,5),_TnDot1agCfmMepDelayNearEndTestDelay_Type())
tnDot1agCfmMepDelayNearEndTestDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepDelayNearEndTestDelay.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepDelayNearEndTestDelay.setUnits(_J)
_TnDot1agCfmMepDelayNearEndVariation_Type=Unsigned32
_TnDot1agCfmMepDelayNearEndVariation_Object=MibTableColumn
tnDot1agCfmMepDelayNearEndVariation=_TnDot1agCfmMepDelayNearEndVariation_Object((1,3,6,1,4,1,7483,6,1,2,52,7,3,1,6),_TnDot1agCfmMepDelayNearEndVariation_Type())
tnDot1agCfmMepDelayNearEndVariation.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepDelayNearEndVariation.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepDelayNearEndVariation.setUnits(_J)
_TnDot1agCfmMepDelayFarEndTestDelay_Type=Integer32
_TnDot1agCfmMepDelayFarEndTestDelay_Object=MibTableColumn
tnDot1agCfmMepDelayFarEndTestDelay=_TnDot1agCfmMepDelayFarEndTestDelay_Object((1,3,6,1,4,1,7483,6,1,2,52,7,3,1,7),_TnDot1agCfmMepDelayFarEndTestDelay_Type())
tnDot1agCfmMepDelayFarEndTestDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepDelayFarEndTestDelay.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepDelayFarEndTestDelay.setUnits(_J)
_TnDot1agCfmMepDelayFarEndVariation_Type=Unsigned32
_TnDot1agCfmMepDelayFarEndVariation_Object=MibTableColumn
tnDot1agCfmMepDelayFarEndVariation=_TnDot1agCfmMepDelayFarEndVariation_Object((1,3,6,1,4,1,7483,6,1,2,52,7,3,1,8),_TnDot1agCfmMepDelayFarEndVariation_Type())
tnDot1agCfmMepDelayFarEndVariation.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepDelayFarEndVariation.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepDelayFarEndVariation.setUnits(_J)
_TnDot1agCfmMepCsfTable_Object=MibTable
tnDot1agCfmMepCsfTable=_TnDot1agCfmMepCsfTable_Object((1,3,6,1,4,1,7483,6,1,2,52,7,4))
if mibBuilder.loadTexts:tnDot1agCfmMepCsfTable.setStatus(_A)
_TnDot1agCfmMepCsfEntry_Object=MibTableRow
tnDot1agCfmMepCsfEntry=_TnDot1agCfmMepCsfEntry_Object((1,3,6,1,4,1,7483,6,1,2,52,7,4,1))
if mibBuilder.loadTexts:tnDot1agCfmMepCsfEntry.setStatus(_A)
class _TnDot1agCfmMepCsfInterval_Type(Dot1agCfmCcmInterval):defaultValue=6
_TnDot1agCfmMepCsfInterval_Type.__name__=_T
_TnDot1agCfmMepCsfInterval_Object=MibTableColumn
tnDot1agCfmMepCsfInterval=_TnDot1agCfmMepCsfInterval_Object((1,3,6,1,4,1,7483,6,1,2,52,7,4,1,1),_TnDot1agCfmMepCsfInterval_Type())
tnDot1agCfmMepCsfInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepCsfInterval.setStatus(_A)
class _TnDot1agCfmMepCsfDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disable',1),('unidirection',2),('bi-dirction',3)))
_TnDot1agCfmMepCsfDirection_Type.__name__=_G
_TnDot1agCfmMepCsfDirection_Object=MibTableColumn
tnDot1agCfmMepCsfDirection=_TnDot1agCfmMepCsfDirection_Object((1,3,6,1,4,1,7483,6,1,2,52,7,4,1,2),_TnDot1agCfmMepCsfDirection_Type())
tnDot1agCfmMepCsfDirection.setMaxAccess(_W)
if mibBuilder.loadTexts:tnDot1agCfmMepCsfDirection.setStatus(_A)
class _TnDot1agCfmMepCsfPriority_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TnDot1agCfmMepCsfPriority_Type.__name__=_G
_TnDot1agCfmMepCsfPriority_Object=MibTableColumn
tnDot1agCfmMepCsfPriority=_TnDot1agCfmMepCsfPriority_Object((1,3,6,1,4,1,7483,6,1,2,52,7,4,1,3),_TnDot1agCfmMepCsfPriority_Type())
tnDot1agCfmMepCsfPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepCsfPriority.setStatus(_A)
_TnDot1agCfmMepSlmTWTestTable_Object=MibTable
tnDot1agCfmMepSlmTWTestTable=_TnDot1agCfmMepSlmTWTestTable_Object((1,3,6,1,4,1,7483,6,1,2,52,7,5))
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTWTestTable.setStatus(_A)
_TnDot1agCfmMepSlmTWTestEntry_Object=MibTableRow
tnDot1agCfmMepSlmTWTestEntry=_TnDot1agCfmMepSlmTWTestEntry_Object((1,3,6,1,4,1,7483,6,1,2,52,7,5,1))
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTWTestEntry.setStatus(_A)
class _TnDot1agCfmMepSlmTWTestStatus_Type(TmnxEnabledDisabled):defaultValue=2
_TnDot1agCfmMepSlmTWTestStatus_Type.__name__=_S
_TnDot1agCfmMepSlmTWTestStatus_Object=MibTableColumn
tnDot1agCfmMepSlmTWTestStatus=_TnDot1agCfmMepSlmTWTestStatus_Object((1,3,6,1,4,1,7483,6,1,2,52,7,5,1,1),_TnDot1agCfmMepSlmTWTestStatus_Type())
tnDot1agCfmMepSlmTWTestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTWTestStatus.setStatus(_A)
_TnDot1agCfmMepSlmTWTestId_Type=Unsigned32
_TnDot1agCfmMepSlmTWTestId_Object=MibTableColumn
tnDot1agCfmMepSlmTWTestId=_TnDot1agCfmMepSlmTWTestId_Object((1,3,6,1,4,1,7483,6,1,2,52,7,5,1,2),_TnDot1agCfmMepSlmTWTestId_Type())
tnDot1agCfmMepSlmTWTestId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTWTestId.setStatus(_A)
class _TnDot1agCfmMepSlmTWMacAddress_Type(MacAddress):defaultHexValue=_M
_TnDot1agCfmMepSlmTWMacAddress_Type.__name__=_K
_TnDot1agCfmMepSlmTWMacAddress_Object=MibTableColumn
tnDot1agCfmMepSlmTWMacAddress=_TnDot1agCfmMepSlmTWMacAddress_Object((1,3,6,1,4,1,7483,6,1,2,52,7,5,1,3),_TnDot1agCfmMepSlmTWMacAddress_Type())
tnDot1agCfmMepSlmTWMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTWMacAddress.setStatus(_A)
class _TnDot1agCfmMepSlmTWPriority_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TnDot1agCfmMepSlmTWPriority_Type.__name__=_E
_TnDot1agCfmMepSlmTWPriority_Object=MibTableColumn
tnDot1agCfmMepSlmTWPriority=_TnDot1agCfmMepSlmTWPriority_Object((1,3,6,1,4,1,7483,6,1,2,52,7,5,1,4),_TnDot1agCfmMepSlmTWPriority_Type())
tnDot1agCfmMepSlmTWPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTWPriority.setStatus(_A)
class _TnDot1agCfmMepSlmTWInterval_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5000))
_TnDot1agCfmMepSlmTWInterval_Type.__name__=_E
_TnDot1agCfmMepSlmTWInterval_Object=MibTableColumn
tnDot1agCfmMepSlmTWInterval=_TnDot1agCfmMepSlmTWInterval_Object((1,3,6,1,4,1,7483,6,1,2,52,7,5,1,5),_TnDot1agCfmMepSlmTWInterval_Type())
tnDot1agCfmMepSlmTWInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTWInterval.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTWInterval.setUnits(_L)
class _TnDot1agCfmMepSlmTWTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TnDot1agCfmMepSlmTWTimeout_Type.__name__=_E
_TnDot1agCfmMepSlmTWTimeout_Object=MibTableColumn
tnDot1agCfmMepSlmTWTimeout=_TnDot1agCfmMepSlmTWTimeout_Object((1,3,6,1,4,1,7483,6,1,2,52,7,5,1,6),_TnDot1agCfmMepSlmTWTimeout_Type())
tnDot1agCfmMepSlmTWTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTWTimeout.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTWTimeout.setUnits(_L)
class _TnDot1agCfmMepSlmTWDataSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9558))
_TnDot1agCfmMepSlmTWDataSize_Type.__name__=_E
_TnDot1agCfmMepSlmTWDataSize_Object=MibTableColumn
tnDot1agCfmMepSlmTWDataSize=_TnDot1agCfmMepSlmTWDataSize_Object((1,3,6,1,4,1,7483,6,1,2,52,7,5,1,7),_TnDot1agCfmMepSlmTWDataSize_Type())
tnDot1agCfmMepSlmTWDataSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTWDataSize.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTWDataSize.setUnits(_R)
class _TnDot1agCfmMepSlmTWSendCount_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_TnDot1agCfmMepSlmTWSendCount_Type.__name__=_E
_TnDot1agCfmMepSlmTWSendCount_Object=MibTableColumn
tnDot1agCfmMepSlmTWSendCount=_TnDot1agCfmMepSlmTWSendCount_Object((1,3,6,1,4,1,7483,6,1,2,52,7,5,1,8),_TnDot1agCfmMepSlmTWSendCount_Type())
tnDot1agCfmMepSlmTWSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTWSendCount.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTWSendCount.setUnits(_H)
class _TnDot1agCfmMepSlmTWIntervalRedef_Type(Unsigned32):defaultValue=1
_TnDot1agCfmMepSlmTWIntervalRedef_Type.__name__=_E
_TnDot1agCfmMepSlmTWIntervalRedef_Object=MibTableColumn
tnDot1agCfmMepSlmTWIntervalRedef=_TnDot1agCfmMepSlmTWIntervalRedef_Object((1,3,6,1,4,1,7483,6,1,2,52,7,5,1,9),_TnDot1agCfmMepSlmTWIntervalRedef_Type())
tnDot1agCfmMepSlmTWIntervalRedef.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTWIntervalRedef.setStatus(_A)
class _TnDot1agCfmMepSlmTWIntrvlUnits_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('centiseconds',2),('decimilliseconds',3)))
_TnDot1agCfmMepSlmTWIntrvlUnits_Type.__name__=_G
_TnDot1agCfmMepSlmTWIntrvlUnits_Object=MibTableColumn
tnDot1agCfmMepSlmTWIntrvlUnits=_TnDot1agCfmMepSlmTWIntrvlUnits_Object((1,3,6,1,4,1,7483,6,1,2,52,7,5,1,10),_TnDot1agCfmMepSlmTWIntrvlUnits_Type())
tnDot1agCfmMepSlmTWIntrvlUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTWIntrvlUnits.setStatus(_A)
_TnDot1agCfmMepSlmOWTestTable_Object=MibTable
tnDot1agCfmMepSlmOWTestTable=_TnDot1agCfmMepSlmOWTestTable_Object((1,3,6,1,4,1,7483,6,1,2,52,7,6))
if mibBuilder.loadTexts:tnDot1agCfmMepSlmOWTestTable.setStatus(_A)
_TnDot1agCfmMepSlmOWTestEntry_Object=MibTableRow
tnDot1agCfmMepSlmOWTestEntry=_TnDot1agCfmMepSlmOWTestEntry_Object((1,3,6,1,4,1,7483,6,1,2,52,7,6,1))
if mibBuilder.loadTexts:tnDot1agCfmMepSlmOWTestEntry.setStatus(_A)
class _TnDot1agCfmMepSlmOWTestStatus_Type(TmnxEnabledDisabled):defaultValue=2
_TnDot1agCfmMepSlmOWTestStatus_Type.__name__=_S
_TnDot1agCfmMepSlmOWTestStatus_Object=MibTableColumn
tnDot1agCfmMepSlmOWTestStatus=_TnDot1agCfmMepSlmOWTestStatus_Object((1,3,6,1,4,1,7483,6,1,2,52,7,6,1,1),_TnDot1agCfmMepSlmOWTestStatus_Type())
tnDot1agCfmMepSlmOWTestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmOWTestStatus.setStatus(_A)
_TnDot1agCfmMepSlmOWTestId_Type=Unsigned32
_TnDot1agCfmMepSlmOWTestId_Object=MibTableColumn
tnDot1agCfmMepSlmOWTestId=_TnDot1agCfmMepSlmOWTestId_Object((1,3,6,1,4,1,7483,6,1,2,52,7,6,1,2),_TnDot1agCfmMepSlmOWTestId_Type())
tnDot1agCfmMepSlmOWTestId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmOWTestId.setStatus(_A)
class _TnDot1agCfmMepSlmOWMacAddress_Type(MacAddress):defaultHexValue=_M
_TnDot1agCfmMepSlmOWMacAddress_Type.__name__=_K
_TnDot1agCfmMepSlmOWMacAddress_Object=MibTableColumn
tnDot1agCfmMepSlmOWMacAddress=_TnDot1agCfmMepSlmOWMacAddress_Object((1,3,6,1,4,1,7483,6,1,2,52,7,6,1,3),_TnDot1agCfmMepSlmOWMacAddress_Type())
tnDot1agCfmMepSlmOWMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmOWMacAddress.setStatus(_A)
class _TnDot1agCfmMepSlmOWPriority_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TnDot1agCfmMepSlmOWPriority_Type.__name__=_E
_TnDot1agCfmMepSlmOWPriority_Object=MibTableColumn
tnDot1agCfmMepSlmOWPriority=_TnDot1agCfmMepSlmOWPriority_Object((1,3,6,1,4,1,7483,6,1,2,52,7,6,1,4),_TnDot1agCfmMepSlmOWPriority_Type())
tnDot1agCfmMepSlmOWPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmOWPriority.setStatus(_A)
class _TnDot1agCfmMepSlmOWInterval_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TnDot1agCfmMepSlmOWInterval_Type.__name__=_E
_TnDot1agCfmMepSlmOWInterval_Object=MibTableColumn
tnDot1agCfmMepSlmOWInterval=_TnDot1agCfmMepSlmOWInterval_Object((1,3,6,1,4,1,7483,6,1,2,52,7,6,1,5),_TnDot1agCfmMepSlmOWInterval_Type())
tnDot1agCfmMepSlmOWInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmOWInterval.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmOWInterval.setUnits(_L)
class _TnDot1agCfmMepSlmOWDataSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1500))
_TnDot1agCfmMepSlmOWDataSize_Type.__name__=_E
_TnDot1agCfmMepSlmOWDataSize_Object=MibTableColumn
tnDot1agCfmMepSlmOWDataSize=_TnDot1agCfmMepSlmOWDataSize_Object((1,3,6,1,4,1,7483,6,1,2,52,7,6,1,6),_TnDot1agCfmMepSlmOWDataSize_Type())
tnDot1agCfmMepSlmOWDataSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmOWDataSize.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmOWDataSize.setUnits(_R)
class _TnDot1agCfmMepSlmOWSendCount_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_TnDot1agCfmMepSlmOWSendCount_Type.__name__=_E
_TnDot1agCfmMepSlmOWSendCount_Object=MibTableColumn
tnDot1agCfmMepSlmOWSendCount=_TnDot1agCfmMepSlmOWSendCount_Object((1,3,6,1,4,1,7483,6,1,2,52,7,6,1,7),_TnDot1agCfmMepSlmOWSendCount_Type())
tnDot1agCfmMepSlmOWSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmOWSendCount.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmOWSendCount.setUnits(_H)
_TnDot1agCfmMepSlmTestRsltTable_Object=MibTable
tnDot1agCfmMepSlmTestRsltTable=_TnDot1agCfmMepSlmTestRsltTable_Object((1,3,6,1,4,1,7483,6,1,2,52,7,7))
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTestRsltTable.setStatus(_A)
_TnDot1agCfmMepSlmTestRsltEntry_Object=MibTableRow
tnDot1agCfmMepSlmTestRsltEntry=_TnDot1agCfmMepSlmTestRsltEntry_Object((1,3,6,1,4,1,7483,6,1,2,52,7,7,1))
tnDot1agCfmMepSlmTestRsltEntry.setIndexNames((0,_F,_P),(0,_F,_O),(0,_F,_Q),(0,_D,_k),(0,_D,_l))
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTestRsltEntry.setStatus(_A)
class _TnDot1agCfmMepSlmTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),(_j,2)))
_TnDot1agCfmMepSlmTestType_Type.__name__=_G
_TnDot1agCfmMepSlmTestType_Object=MibTableColumn
tnDot1agCfmMepSlmTestType=_TnDot1agCfmMepSlmTestType_Object((1,3,6,1,4,1,7483,6,1,2,52,7,7,1,1),_TnDot1agCfmMepSlmTestType_Type())
tnDot1agCfmMepSlmTestType.setMaxAccess(_I)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTestType.setStatus(_A)
_TnDot1agCfmMepSlmRemoteMacAddr_Type=MacAddress
_TnDot1agCfmMepSlmRemoteMacAddr_Object=MibTableColumn
tnDot1agCfmMepSlmRemoteMacAddr=_TnDot1agCfmMepSlmRemoteMacAddr_Object((1,3,6,1,4,1,7483,6,1,2,52,7,7,1,2),_TnDot1agCfmMepSlmRemoteMacAddr_Type())
tnDot1agCfmMepSlmRemoteMacAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmRemoteMacAddr.setStatus(_A)
_TnDot1agCfmMepSlmTestId_Type=Unsigned32
_TnDot1agCfmMepSlmTestId_Object=MibTableColumn
tnDot1agCfmMepSlmTestId=_TnDot1agCfmMepSlmTestId_Object((1,3,6,1,4,1,7483,6,1,2,52,7,7,1,3),_TnDot1agCfmMepSlmTestId_Type())
tnDot1agCfmMepSlmTestId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmTestId.setStatus(_A)
_TnDot1agCfmMepSlmRemoteMepId_Type=Dot1agCfmMepId
_TnDot1agCfmMepSlmRemoteMepId_Object=MibTableColumn
tnDot1agCfmMepSlmRemoteMepId=_TnDot1agCfmMepSlmRemoteMepId_Object((1,3,6,1,4,1,7483,6,1,2,52,7,7,1,4),_TnDot1agCfmMepSlmRemoteMepId_Type())
tnDot1agCfmMepSlmRemoteMepId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmRemoteMepId.setStatus(_A)
_TnDot1agCfmMepSlmLastTxSeqF_Type=Unsigned32
_TnDot1agCfmMepSlmLastTxSeqF_Object=MibTableColumn
tnDot1agCfmMepSlmLastTxSeqF=_TnDot1agCfmMepSlmLastTxSeqF_Object((1,3,6,1,4,1,7483,6,1,2,52,7,7,1,5),_TnDot1agCfmMepSlmLastTxSeqF_Type())
tnDot1agCfmMepSlmLastTxSeqF.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmLastTxSeqF.setStatus(_A)
_TnDot1agCfmMepSlmPacketIn_Type=Counter32
_TnDot1agCfmMepSlmPacketIn_Object=MibTableColumn
tnDot1agCfmMepSlmPacketIn=_TnDot1agCfmMepSlmPacketIn_Object((1,3,6,1,4,1,7483,6,1,2,52,7,7,1,6),_TnDot1agCfmMepSlmPacketIn_Type())
tnDot1agCfmMepSlmPacketIn.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmPacketIn.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmPacketIn.setUnits(_H)
_TnDot1agCfmMepSlmPacketLossIn_Type=Integer32
_TnDot1agCfmMepSlmPacketLossIn_Object=MibTableColumn
tnDot1agCfmMepSlmPacketLossIn=_TnDot1agCfmMepSlmPacketLossIn_Object((1,3,6,1,4,1,7483,6,1,2,52,7,7,1,7),_TnDot1agCfmMepSlmPacketLossIn_Type())
tnDot1agCfmMepSlmPacketLossIn.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmPacketLossIn.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmPacketLossIn.setUnits(_H)
_TnDot1agCfmMepSlmPacketLossOut_Type=Integer32
_TnDot1agCfmMepSlmPacketLossOut_Object=MibTableColumn
tnDot1agCfmMepSlmPacketLossOut=_TnDot1agCfmMepSlmPacketLossOut_Object((1,3,6,1,4,1,7483,6,1,2,52,7,7,1,8),_TnDot1agCfmMepSlmPacketLossOut_Type())
tnDot1agCfmMepSlmPacketLossOut.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmPacketLossOut.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmPacketLossOut.setUnits(_H)
_TnDot1agCfmMepSlmPacketUnack_Type=Gauge32
_TnDot1agCfmMepSlmPacketUnack_Object=MibTableColumn
tnDot1agCfmMepSlmPacketUnack=_TnDot1agCfmMepSlmPacketUnack_Object((1,3,6,1,4,1,7483,6,1,2,52,7,7,1,9),_TnDot1agCfmMepSlmPacketUnack_Type())
tnDot1agCfmMepSlmPacketUnack.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmPacketUnack.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepSlmPacketUnack.setUnits(_H)
_TnDot1agCfmMepOndemandLmTestTable_Object=MibTable
tnDot1agCfmMepOndemandLmTestTable=_TnDot1agCfmMepOndemandLmTestTable_Object((1,3,6,1,4,1,7483,6,1,2,52,7,8))
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmTestTable.setStatus(_A)
_TnDot1agCfmMepOndemandLmTestEntry_Object=MibTableRow
tnDot1agCfmMepOndemandLmTestEntry=_TnDot1agCfmMepOndemandLmTestEntry_Object((1,3,6,1,4,1,7483,6,1,2,52,7,8,1))
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmTestEntry.setStatus(_A)
class _TnDot1agCfmMepOndemandLmTestStatus_Type(TmnxEnabledDisabled):defaultValue=2
_TnDot1agCfmMepOndemandLmTestStatus_Type.__name__=_S
_TnDot1agCfmMepOndemandLmTestStatus_Object=MibTableColumn
tnDot1agCfmMepOndemandLmTestStatus=_TnDot1agCfmMepOndemandLmTestStatus_Object((1,3,6,1,4,1,7483,6,1,2,52,7,8,1,1),_TnDot1agCfmMepOndemandLmTestStatus_Type())
tnDot1agCfmMepOndemandLmTestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmTestStatus.setStatus(_A)
class _TnDot1agCfmMepOndemandLmDestMacAddress_Type(MacAddress):defaultHexValue=_M
_TnDot1agCfmMepOndemandLmDestMacAddress_Type.__name__=_K
_TnDot1agCfmMepOndemandLmDestMacAddress_Object=MibTableColumn
tnDot1agCfmMepOndemandLmDestMacAddress=_TnDot1agCfmMepOndemandLmDestMacAddress_Object((1,3,6,1,4,1,7483,6,1,2,52,7,8,1,2),_TnDot1agCfmMepOndemandLmDestMacAddress_Type())
tnDot1agCfmMepOndemandLmDestMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmDestMacAddress.setStatus(_A)
class _TnDot1agCfmMepOndemandLmPriority_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TnDot1agCfmMepOndemandLmPriority_Type.__name__=_E
_TnDot1agCfmMepOndemandLmPriority_Object=MibTableColumn
tnDot1agCfmMepOndemandLmPriority=_TnDot1agCfmMepOndemandLmPriority_Object((1,3,6,1,4,1,7483,6,1,2,52,7,8,1,3),_TnDot1agCfmMepOndemandLmPriority_Type())
tnDot1agCfmMepOndemandLmPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmPriority.setStatus(_A)
class _TnDot1agCfmMepOndemandLmInterval_Type(Dot1agCfmCcmInterval):defaultValue=4
_TnDot1agCfmMepOndemandLmInterval_Type.__name__=_T
_TnDot1agCfmMepOndemandLmInterval_Object=MibTableColumn
tnDot1agCfmMepOndemandLmInterval=_TnDot1agCfmMepOndemandLmInterval_Object((1,3,6,1,4,1,7483,6,1,2,52,7,8,1,4),_TnDot1agCfmMepOndemandLmInterval_Type())
tnDot1agCfmMepOndemandLmInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmInterval.setStatus(_A)
class _TnDot1agCfmMepOndemandLmSendCount_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,101))
_TnDot1agCfmMepOndemandLmSendCount_Type.__name__=_E
_TnDot1agCfmMepOndemandLmSendCount_Object=MibTableColumn
tnDot1agCfmMepOndemandLmSendCount=_TnDot1agCfmMepOndemandLmSendCount_Object((1,3,6,1,4,1,7483,6,1,2,52,7,8,1,5),_TnDot1agCfmMepOndemandLmSendCount_Type())
tnDot1agCfmMepOndemandLmSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmSendCount.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmSendCount.setUnits(_H)
class _TnDot1agCfmMepOndemandLmTimeout_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,10000))
_TnDot1agCfmMepOndemandLmTimeout_Type.__name__=_E
_TnDot1agCfmMepOndemandLmTimeout_Object=MibTableColumn
tnDot1agCfmMepOndemandLmTimeout=_TnDot1agCfmMepOndemandLmTimeout_Object((1,3,6,1,4,1,7483,6,1,2,52,7,8,1,6),_TnDot1agCfmMepOndemandLmTimeout_Type())
tnDot1agCfmMepOndemandLmTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmTimeout.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmTimeout.setUnits('milliseconds')
_TnDot1agCfmMepOndemandLmTestRsltTable_Object=MibTable
tnDot1agCfmMepOndemandLmTestRsltTable=_TnDot1agCfmMepOndemandLmTestRsltTable_Object((1,3,6,1,4,1,7483,6,1,2,52,7,9))
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmTestRsltTable.setStatus(_A)
_TnDot1agCfmMepOndemandLmTestRsltEntry_Object=MibTableRow
tnDot1agCfmMepOndemandLmTestRsltEntry=_TnDot1agCfmMepOndemandLmTestRsltEntry_Object((1,3,6,1,4,1,7483,6,1,2,52,7,9,1))
tnDot1agCfmMepOndemandLmTestRsltEntry.setIndexNames((0,_F,_P),(0,_F,_O),(0,_F,_Q))
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmTestRsltEntry.setStatus(_A)
_TnDot1agCfmMepOndemandLmTnTF_Type=Counter32
_TnDot1agCfmMepOndemandLmTnTF_Object=MibTableColumn
tnDot1agCfmMepOndemandLmTnTF=_TnDot1agCfmMepOndemandLmTnTF_Object((1,3,6,1,4,1,7483,6,1,2,52,7,9,1,1),_TnDot1agCfmMepOndemandLmTnTF_Type())
tnDot1agCfmMepOndemandLmTnTF.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmTnTF.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmTnTF.setUnits(_H)
_TnDot1agCfmMepOndemandLmTnLF_Type=Counter32
_TnDot1agCfmMepOndemandLmTnLF_Object=MibTableColumn
tnDot1agCfmMepOndemandLmTnLF=_TnDot1agCfmMepOndemandLmTnLF_Object((1,3,6,1,4,1,7483,6,1,2,52,7,9,1,2),_TnDot1agCfmMepOndemandLmTnLF_Type())
tnDot1agCfmMepOndemandLmTnLF.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmTnLF.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmTnLF.setUnits(_H)
_TnDot1agCfmMepOndemandLmTfTF_Type=Counter32
_TnDot1agCfmMepOndemandLmTfTF_Object=MibTableColumn
tnDot1agCfmMepOndemandLmTfTF=_TnDot1agCfmMepOndemandLmTfTF_Object((1,3,6,1,4,1,7483,6,1,2,52,7,9,1,3),_TnDot1agCfmMepOndemandLmTfTF_Type())
tnDot1agCfmMepOndemandLmTfTF.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmTfTF.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmTfTF.setUnits(_H)
_TnDot1agCfmMepOndemandLmTfLF_Type=Counter32
_TnDot1agCfmMepOndemandLmTfLF_Object=MibTableColumn
tnDot1agCfmMepOndemandLmTfLF=_TnDot1agCfmMepOndemandLmTfLF_Object((1,3,6,1,4,1,7483,6,1,2,52,7,9,1,4),_TnDot1agCfmMepOndemandLmTfLF_Type())
tnDot1agCfmMepOndemandLmTfLF.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmTfLF.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmTfLF.setUnits(_H)
_TnDot1agCfmMepOndemandLmUnack_Type=Gauge32
_TnDot1agCfmMepOndemandLmUnack_Object=MibTableColumn
tnDot1agCfmMepOndemandLmUnack=_TnDot1agCfmMepOndemandLmUnack_Object((1,3,6,1,4,1,7483,6,1,2,52,7,9,1,5),_TnDot1agCfmMepOndemandLmUnack_Type())
tnDot1agCfmMepOndemandLmUnack.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmUnack.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmUnack.setUnits(_H)
_TnDot1agCfmMepOndemandLmRemoteMacAddr_Type=MacAddress
_TnDot1agCfmMepOndemandLmRemoteMacAddr_Object=MibTableColumn
tnDot1agCfmMepOndemandLmRemoteMacAddr=_TnDot1agCfmMepOndemandLmRemoteMacAddr_Object((1,3,6,1,4,1,7483,6,1,2,52,7,9,1,6),_TnDot1agCfmMepOndemandLmRemoteMacAddr_Type())
tnDot1agCfmMepOndemandLmRemoteMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmRemoteMacAddr.setStatus(_A)
_TnDot1agCfmMepOWDelayRsltExtTable_Object=MibTable
tnDot1agCfmMepOWDelayRsltExtTable=_TnDot1agCfmMepOWDelayRsltExtTable_Object((1,3,6,1,4,1,7483,6,1,2,52,7,10))
if mibBuilder.loadTexts:tnDot1agCfmMepOWDelayRsltExtTable.setStatus(_A)
_TnDot1agCfmMepOWDelayRsltExtEntry_Object=MibTableRow
tnDot1agCfmMepOWDelayRsltExtEntry=_TnDot1agCfmMepOWDelayRsltExtEntry_Object((1,3,6,1,4,1,7483,6,1,2,52,7,10,1))
tnDot1agCfmMepOWDelayRsltExtEntry.setIndexNames((0,_F,_P),(0,_F,_O),(0,_F,_Q))
if mibBuilder.loadTexts:tnDot1agCfmMepOWDelayRsltExtEntry.setStatus(_A)
_TnDot1agCfmMepOWDelayRsltExtTnFD_Type=Integer32
_TnDot1agCfmMepOWDelayRsltExtTnFD_Object=MibTableColumn
tnDot1agCfmMepOWDelayRsltExtTnFD=_TnDot1agCfmMepOWDelayRsltExtTnFD_Object((1,3,6,1,4,1,7483,6,1,2,52,7,10,1,1),_TnDot1agCfmMepOWDelayRsltExtTnFD_Type())
tnDot1agCfmMepOWDelayRsltExtTnFD.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepOWDelayRsltExtTnFD.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepOWDelayRsltExtTnFD.setUnits(_J)
_TnDot1agCfmMepOWDelayRsltExtTnFDV_Type=Integer32
_TnDot1agCfmMepOWDelayRsltExtTnFDV_Object=MibTableColumn
tnDot1agCfmMepOWDelayRsltExtTnFDV=_TnDot1agCfmMepOWDelayRsltExtTnFDV_Object((1,3,6,1,4,1,7483,6,1,2,52,7,10,1,2),_TnDot1agCfmMepOWDelayRsltExtTnFDV_Type())
tnDot1agCfmMepOWDelayRsltExtTnFDV.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepOWDelayRsltExtTnFDV.setStatus(_A)
if mibBuilder.loadTexts:tnDot1agCfmMepOWDelayRsltExtTnFDV.setUnits(_J)
_TnDot1agCfmMepScalar1_Type=Unsigned32
_TnDot1agCfmMepScalar1_Object=MibScalar
tnDot1agCfmMepScalar1=_TnDot1agCfmMepScalar1_Object((1,3,6,1,4,1,7483,6,1,2,52,7,101),_TnDot1agCfmMepScalar1_Type())
tnDot1agCfmMepScalar1.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepScalar1.setStatus(_A)
_TnDot1agCfmMepScalar2_Type=Unsigned32
_TnDot1agCfmMepScalar2_Object=MibScalar
tnDot1agCfmMepScalar2=_TnDot1agCfmMepScalar2_Object((1,3,6,1,4,1,7483,6,1,2,52,7,102),_TnDot1agCfmMepScalar2_Type())
tnDot1agCfmMepScalar2.setMaxAccess(_C)
if mibBuilder.loadTexts:tnDot1agCfmMepScalar2.setStatus(_A)
_TnDot1agNotificationsPrefix_ObjectIdentity=ObjectIdentity
tnDot1agNotificationsPrefix=_TnDot1agNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,52))
_TnDot1agNotifications_ObjectIdentity=ObjectIdentity
tnDot1agNotifications=_TnDot1agNotifications_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,52,0))
dot1agCfmMaNetEntry.registerAugmentions((_D,_m))
tnDot1agCfmMaNetEntry.setIndexNames(*dot1agCfmMaNetEntry.getIndexNames())
dot1agCfmMaMepListEntry.registerAugmentions((_D,_n))
tnDot1agCfmMaMepListEntry.setIndexNames(*dot1agCfmMaMepListEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions((_D,_o))
tnDot1agCfmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions((_D,_p))
tnDot1agCfmMepCsfEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions((_D,_q))
tnDot1agCfmMepSlmTWTestEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions((_D,_r))
tnDot1agCfmMepSlmOWTestEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions((_D,_s))
tnDot1agCfmMepOndemandLmTestEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
tnDot1agCfmMepLbmTestComplete=NotificationType((1,3,6,1,4,1,7483,6,1,3,52,0,1))
tnDot1agCfmMepLbmTestComplete.setObjects((_F,_Y))
if mibBuilder.loadTexts:tnDot1agCfmMepLbmTestComplete.setStatus(_A)
tnDot1agCfmMepLtmTestComplete=NotificationType((1,3,6,1,4,1,7483,6,1,3,52,0,2))
tnDot1agCfmMepLtmTestComplete.setObjects((_F,_Z))
if mibBuilder.loadTexts:tnDot1agCfmMepLtmTestComplete.setStatus(_A)
tnDot1agCfmMepDMTestComplete=NotificationType((1,3,6,1,4,1,7483,6,1,3,52,0,4))
tnDot1agCfmMepDMTestComplete.setObjects((_D,_t))
if mibBuilder.loadTexts:tnDot1agCfmMepDMTestComplete.setStatus(_A)
tnDot1agCfmMepAisStateChanged=NotificationType((1,3,6,1,4,1,7483,6,1,3,52,0,5))
tnDot1agCfmMepAisStateChanged.setObjects((_D,_u))
if mibBuilder.loadTexts:tnDot1agCfmMepAisStateChanged.setStatus(_A)
tnDot1agCfmMepSLMTestComplete=NotificationType((1,3,6,1,4,1,7483,6,1,3,52,0,7))
tnDot1agCfmMepSLMTestComplete.setObjects(*((_D,_v),(_D,_w),(_D,_x),(_D,_y),(_D,_z),(_D,_A0),(_D,_A1)))
if mibBuilder.loadTexts:tnDot1agCfmMepSLMTestComplete.setStatus(_A)
tnDot1agCfmMepOndemandLmTestComplete=NotificationType((1,3,6,1,4,1,7483,6,1,3,52,0,8))
tnDot1agCfmMepOndemandLmTestComplete.setObjects(*((_D,_A2),(_D,_A3),(_D,_A4),(_D,_A5),(_D,_A6)))
if mibBuilder.loadTexts:tnDot1agCfmMepOndemandLmTestComplete.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'NokiaPmonUnitType':NokiaPmonUnitType,'tnIEEE8021CfmMIBModule':tnIEEE8021CfmMIBModule,'tnDot1agMIBObjs':tnDot1agMIBObjs,'tnDot1agCfmStack':tnDot1agCfmStack,'tnDot1agCfmStackTable':tnDot1agCfmStackTable,'tnDot1agCfmStackEntry':tnDot1agCfmStackEntry,_a:tnDot1agCfmStackifIndex,_b:tnDot1agCfmStackVlanIdOrNone,_c:tnDot1agCfmStackMdLevel,_d:tnDot1agCfmStackDirection,'tnDot1agCfmStackMdIndex':tnDot1agCfmStackMdIndex,'tnDot1agCfmStackMaIndex':tnDot1agCfmStackMaIndex,'tnDot1agCfmStackMepId':tnDot1agCfmStackMepId,'tnDot1agCfmStackMacAddress':tnDot1agCfmStackMacAddress,'tnDot1agCfmStackMPType':tnDot1agCfmStackMPType,'tnDot1agCfmGlobalObjs':tnDot1agCfmGlobalObjs,'tnDot1agCfmMcLagConfigTable':tnDot1agCfmMcLagConfigTable,'tnDot1agCfmMcLagConfigEntry':tnDot1agCfmMcLagConfigEntry,'tnDot1agCfmMcLagConfigStdbyInactive':tnDot1agCfmMcLagConfigStdbyInactive,'tnDot1agCfmMcLagConfigPropHoldTime':tnDot1agCfmMcLagConfigPropHoldTime,'tnDot1agCfmStatisticsGroup':tnDot1agCfmStatisticsGroup,'tnDot1agCfmComponentLimitTable':tnDot1agCfmComponentLimitTable,'tnDot1agCfmComponentLimitEntry':tnDot1agCfmComponentLimitEntry,_e:tnDot1agCfmCompMajorIndex,_f:tnDot1agCfmCompMinorIndex,'tnDot1agCfmCompName':tnDot1agCfmCompName,'tnDot1agCfmCompResourceUsage':tnDot1agCfmCompResourceUsage,'tnDot1agCfmCompResourceLimit':tnDot1agCfmCompResourceLimit,'tnDot1agCfmGlobalScalar1':tnDot1agCfmGlobalScalar1,'tnDot1agCfmGlobalScalar2':tnDot1agCfmGlobalScalar2,'tnDot1agCfmMa':tnDot1agCfmMa,'tnDot1agCfmMaNetTable':tnDot1agCfmMaNetTable,_m:tnDot1agCfmMaNetEntry,'tnDot1agCfmMaNetTotalMEPCount':tnDot1agCfmMaNetTotalMEPCount,'tnDot1agCfmMaMepListTable':tnDot1agCfmMaMepListTable,_n:tnDot1agCfmMaMepListEntry,'tnDot1agCfmMaMepListMacAddress':tnDot1agCfmMaMepListMacAddress,'tnDot1agCfmMaMepListSapSubType':tnDot1agCfmMaMepListSapSubType,'tnDot1agCfmMep':tnDot1agCfmMep,'tnDot1agCfmMepTable':tnDot1agCfmMepTable,_o:tnDot1agCfmMepEntry,'tnDot1agCfmMepSdpId':tnDot1agCfmMepSdpId,'tnDot1agCfmMepVcId':tnDot1agCfmMepVcId,'tnDot1agCfmMepMacAddress':tnDot1agCfmMepMacAddress,'tnDot1agCfmMepAisEnable':tnDot1agCfmMepAisEnable,'tnDot1agCfmMepAisMegLevel':tnDot1agCfmMepAisMegLevel,'tnDot1agCfmMepAisPriority':tnDot1agCfmMepAisPriority,'tnDot1agCfmMepAisInterval':tnDot1agCfmMepAisInterval,'tnDot1agCfmMepEthRxAisInterval':tnDot1agCfmMepEthRxAisInterval,_u:tnDot1agCfmMepEthRxAis,'tnDot1agCfmMepEthAisTxCount':tnDot1agCfmMepEthAisTxCount,'tnDot1agCfmMepEthTestEnable':tnDot1agCfmMepEthTestEnable,'tnDot1agCfmMepEthTestPattern':tnDot1agCfmMepEthTestPattern,'tnDot1agCfmMepEthTestMacAddr':tnDot1agCfmMepEthTestMacAddr,'tnDot1agCfmMepEthTestDataLen':tnDot1agCfmMepEthTestDataLen,'tnDot1agCfmMepEthTestPriority':tnDot1agCfmMepEthTestPriority,'tnDot1agCfmMepOWDTMacAddress':tnDot1agCfmMepOWDTMacAddress,'tnDot1agCfmMepOWDTPriority':tnDot1agCfmMepOWDTPriority,'tnDot1agCfmMepTWDTMacAddress':tnDot1agCfmMepTWDTMacAddress,'tnDot1agCfmMepTWDTPriority':tnDot1agCfmMepTWDTPriority,'tnDot1agCfmMepSvcId':tnDot1agCfmMepSvcId,'tnDot1agCfmMepControlMep':tnDot1agCfmMepControlMep,'tnDot1agCfmMepEthTestThreshold':tnDot1agCfmMepEthTestThreshold,'tnDot1agCfmMepOWDTThreshold':tnDot1agCfmMepOWDTThreshold,'tnDot1agCfmMepMcLagInactive':tnDot1agCfmMepMcLagInactive,'tnDot1agCfmMepTWDTDataSize':tnDot1agCfmMepTWDTDataSize,'tnDot1agCfmMepTransmitLbmDataTlvSize':tnDot1agCfmMepTransmitLbmDataTlvSize,'tnDot1agCfmMepType':tnDot1agCfmMepType,'tnDot1agCfmMepFaultPropagation':tnDot1agCfmMepFaultPropagation,'tnDot1agCfmMepOWDTDataSize':tnDot1agCfmMepOWDTDataSize,'tnDot1agCfmMepAlmProfName':tnDot1agCfmMepAlmProfName,'tnDot1agCfmMepDelayRsltTable':tnDot1agCfmMepDelayRsltTable,'tnDot1agCfmMepDelayRsltEntry':tnDot1agCfmMepDelayRsltEntry,_g:tnDot1agCfmMepDelaySrcMacAddr,_h:tnDot1agCfmMepDelayTestType,_t:tnDot1agCfmMepDelayTestDelay,'tnDot1agCfmMepDelayVariation':tnDot1agCfmMepDelayVariation,'tnDot1agCfmMepDelayNearEndTestDelay':tnDot1agCfmMepDelayNearEndTestDelay,'tnDot1agCfmMepDelayNearEndVariation':tnDot1agCfmMepDelayNearEndVariation,'tnDot1agCfmMepDelayFarEndTestDelay':tnDot1agCfmMepDelayFarEndTestDelay,'tnDot1agCfmMepDelayFarEndVariation':tnDot1agCfmMepDelayFarEndVariation,'tnDot1agCfmMepCsfTable':tnDot1agCfmMepCsfTable,_p:tnDot1agCfmMepCsfEntry,'tnDot1agCfmMepCsfInterval':tnDot1agCfmMepCsfInterval,'tnDot1agCfmMepCsfDirection':tnDot1agCfmMepCsfDirection,'tnDot1agCfmMepCsfPriority':tnDot1agCfmMepCsfPriority,'tnDot1agCfmMepSlmTWTestTable':tnDot1agCfmMepSlmTWTestTable,_q:tnDot1agCfmMepSlmTWTestEntry,'tnDot1agCfmMepSlmTWTestStatus':tnDot1agCfmMepSlmTWTestStatus,'tnDot1agCfmMepSlmTWTestId':tnDot1agCfmMepSlmTWTestId,'tnDot1agCfmMepSlmTWMacAddress':tnDot1agCfmMepSlmTWMacAddress,'tnDot1agCfmMepSlmTWPriority':tnDot1agCfmMepSlmTWPriority,'tnDot1agCfmMepSlmTWInterval':tnDot1agCfmMepSlmTWInterval,'tnDot1agCfmMepSlmTWTimeout':tnDot1agCfmMepSlmTWTimeout,'tnDot1agCfmMepSlmTWDataSize':tnDot1agCfmMepSlmTWDataSize,'tnDot1agCfmMepSlmTWSendCount':tnDot1agCfmMepSlmTWSendCount,'tnDot1agCfmMepSlmTWIntervalRedef':tnDot1agCfmMepSlmTWIntervalRedef,'tnDot1agCfmMepSlmTWIntrvlUnits':tnDot1agCfmMepSlmTWIntrvlUnits,'tnDot1agCfmMepSlmOWTestTable':tnDot1agCfmMepSlmOWTestTable,_r:tnDot1agCfmMepSlmOWTestEntry,'tnDot1agCfmMepSlmOWTestStatus':tnDot1agCfmMepSlmOWTestStatus,'tnDot1agCfmMepSlmOWTestId':tnDot1agCfmMepSlmOWTestId,'tnDot1agCfmMepSlmOWMacAddress':tnDot1agCfmMepSlmOWMacAddress,'tnDot1agCfmMepSlmOWPriority':tnDot1agCfmMepSlmOWPriority,'tnDot1agCfmMepSlmOWInterval':tnDot1agCfmMepSlmOWInterval,'tnDot1agCfmMepSlmOWDataSize':tnDot1agCfmMepSlmOWDataSize,'tnDot1agCfmMepSlmOWSendCount':tnDot1agCfmMepSlmOWSendCount,'tnDot1agCfmMepSlmTestRsltTable':tnDot1agCfmMepSlmTestRsltTable,'tnDot1agCfmMepSlmTestRsltEntry':tnDot1agCfmMepSlmTestRsltEntry,_k:tnDot1agCfmMepSlmTestType,_l:tnDot1agCfmMepSlmRemoteMacAddr,_v:tnDot1agCfmMepSlmTestId,_w:tnDot1agCfmMepSlmRemoteMepId,_x:tnDot1agCfmMepSlmLastTxSeqF,_y:tnDot1agCfmMepSlmPacketIn,_z:tnDot1agCfmMepSlmPacketLossIn,_A0:tnDot1agCfmMepSlmPacketLossOut,_A1:tnDot1agCfmMepSlmPacketUnack,'tnDot1agCfmMepOndemandLmTestTable':tnDot1agCfmMepOndemandLmTestTable,_s:tnDot1agCfmMepOndemandLmTestEntry,'tnDot1agCfmMepOndemandLmTestStatus':tnDot1agCfmMepOndemandLmTestStatus,'tnDot1agCfmMepOndemandLmDestMacAddress':tnDot1agCfmMepOndemandLmDestMacAddress,'tnDot1agCfmMepOndemandLmPriority':tnDot1agCfmMepOndemandLmPriority,'tnDot1agCfmMepOndemandLmInterval':tnDot1agCfmMepOndemandLmInterval,'tnDot1agCfmMepOndemandLmSendCount':tnDot1agCfmMepOndemandLmSendCount,'tnDot1agCfmMepOndemandLmTimeout':tnDot1agCfmMepOndemandLmTimeout,'tnDot1agCfmMepOndemandLmTestRsltTable':tnDot1agCfmMepOndemandLmTestRsltTable,'tnDot1agCfmMepOndemandLmTestRsltEntry':tnDot1agCfmMepOndemandLmTestRsltEntry,_A2:tnDot1agCfmMepOndemandLmTnTF,_A3:tnDot1agCfmMepOndemandLmTnLF,_A4:tnDot1agCfmMepOndemandLmTfTF,_A5:tnDot1agCfmMepOndemandLmTfLF,_A6:tnDot1agCfmMepOndemandLmUnack,'tnDot1agCfmMepOndemandLmRemoteMacAddr':tnDot1agCfmMepOndemandLmRemoteMacAddr,'tnDot1agCfmMepOWDelayRsltExtTable':tnDot1agCfmMepOWDelayRsltExtTable,'tnDot1agCfmMepOWDelayRsltExtEntry':tnDot1agCfmMepOWDelayRsltExtEntry,'tnDot1agCfmMepOWDelayRsltExtTnFD':tnDot1agCfmMepOWDelayRsltExtTnFD,'tnDot1agCfmMepOWDelayRsltExtTnFDV':tnDot1agCfmMepOWDelayRsltExtTnFDV,'tnDot1agCfmMepScalar1':tnDot1agCfmMepScalar1,'tnDot1agCfmMepScalar2':tnDot1agCfmMepScalar2,'tnDot1agNotificationsPrefix':tnDot1agNotificationsPrefix,'tnDot1agNotifications':tnDot1agNotifications,'tnDot1agCfmMepLbmTestComplete':tnDot1agCfmMepLbmTestComplete,'tnDot1agCfmMepLtmTestComplete':tnDot1agCfmMepLtmTestComplete,'tnDot1agCfmMepDMTestComplete':tnDot1agCfmMepDMTestComplete,'tnDot1agCfmMepAisStateChanged':tnDot1agCfmMepAisStateChanged,'tnDot1agCfmMepSLMTestComplete':tnDot1agCfmMepSLMTestComplete,'tnDot1agCfmMepOndemandLmTestComplete':tnDot1agCfmMepOndemandLmTestComplete})