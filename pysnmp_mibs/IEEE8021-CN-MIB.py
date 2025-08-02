_Ap='ieee8021CnRpGroup'
_Ao='ieee8021CnRpppGroup'
_An='ieee8021CnRpgMinRate'
_Am='ieee8021CnRpgMinDecFac'
_Al='ieee8021CnRpgGd'
_Ak='ieee8021CnRpgHaiRate'
_Aj='ieee8021CnRpgAiRate'
_Ai='ieee8021CnRpgMaxRate'
_Ah='ieee8021CnRpgThreshold'
_Ag='ieee8021CnRpgByteReset'
_Af='ieee8021CnRpgTimeReset'
_Ae='ieee8021CnRpgEnable'
_Ad='ieee8021CnRpPortPriCentiseconds'
_Ac='ieee8021CnRpPortPriCreatedRps'
_Ab='ieee8021CnRpPortPriMaxRps'
_Aa='ieee8021CnCpMinHeaderOctets'
_AZ='ieee8021CnCpTransmittedCnms'
_AY='ieee8021CnCpTransmittedFrames'
_AX='ieee8021CnCpDiscardedFrames'
_AW='ieee8021CnCpMinSampleBase'
_AV='ieee8021CnCpFeedbackWeight'
_AU='ieee8021CnCpQueueSizeSetPoint'
_AT='ieee8021CnCpIdentifier'
_AS='ieee8021CnCpMacAddress'
_AR='ieee8021CnCpPriority'
_AQ='ieee8021CnPortPriAlternatePriority'
_AP='ieee8021CnPortPriLldpInstanceSelector'
_AO='ieee8021CnPortPriLldpInstanceChoice'
_AN='ieee8021CnPortPriAutoDefenseMode'
_AM='ieee8021CnPortPriAdminDefenseMode'
_AL='ieee8021CnPortPriDefModeChoice'
_AK='ieee8021CnComPriAutoAltPri'
_AJ='ieee8021CnComPriAlternatePriority'
_AI='ieee8021CnComPriRowStatus'
_AH='ieee8021CnComPriCreation'
_AG='ieee8021CnComPriAdminDefenseMode'
_AF='ieee8021CnComPriDefModeChoice'
_AE='ieee8021CnCpidToIfCpIndex'
_AD='ieee8021CnCpidToIfIfIndex'
_AC='ieee8021CnCpidToIfComponentId'
_AB='ieee8021CnGlobalDiscardedFrames'
_AA='ieee8021CnGlobalCnmTransmitPriority'
_A9='ieee8021CnComPriLldpInstanceSelector'
_A8='ieee8021CnComPriLldpInstanceChoice'
_A7='ieee8021CnGlobalMasterEnable'
_A6='ieee8021CnRpgIdentifier'
_A5='ieee8021CnRpgIfIndex'
_A4='ieee8021CnRpgPriority'
_A3='ieee8021CnRpgComponentId'
_A2='ieee8021CnRpPortPriIfIndex'
_A1='ieee8021CnRpPortPriPriority'
_A0='ieee8021CnRpPortPriComponentId'
_z='ieee8021CnCpidToIfCpid'
_y='ieee8021CnCpIndex'
_x='ieee8021CnCpIfIndex'
_w='ieee8021CnCpComponentId'
_v='ieee8021CnPortPriIfIndex'
_u='ieee8021CnPortPriority'
_t='ieee8021CnPortPriComponentId'
_s='ieee8021CnComPriPriority'
_r='ieee8021CnComPriComponentId'
_q='ieee8021CnEpPriority'
_p='ieee8021CnEpComponentId'
_o='ieee8021CnGlobalComponentId'
_n='cnlAdmin'
_m='cnlNone'
_l='cptEdge'
_k='cptInteriorReady'
_j='cptInterior'
_i='cpcAuto'
_h='cpcAdmin'
_g='TruthValue'
_f='TimeInterval'
_e='ieee8021CnCpGroup'
_d='ieee8021CnCpPriPortGroup'
_c='ieee8021CnGlobalPriPortGroup'
_b='ieee8021CnCpPriGroup'
_a='ieee8021CnComPriGroup'
_Z='ieee8021CnEplGroup'
_Y='ieee8021CnCpidTranslateGroup'
_X='ieee8021CnCpGlobalGroup'
_W='ieee8021CnGlobalReqdGroup'
_V='Ieee8021CnLldpChoice'
_U='Ieee8021CnControlChoice'
_T='ieee8021CnEpIfIndex'
_S='systemGroup'
_R='SNMPv2-MIB'
_Q='LldpV2DestAddressTableIndex'
_P='ifGeneralInformationGroup'
_O='IF-MIB'
_N='IEEE8021PriorityValue'
_M='OctetString'
_L='Mb/s'
_K='octets'
_J='Ieee8021CnDefenseMode'
_I='frames'
_H='Integer32'
_G='read-create'
_F='Unsigned32'
_E='read-only'
_D='not-accessible'
_C='read-write'
_B='IEEE8021-CN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IEEE8021PbbComponentIdentifier,IEEE8021PriorityValue,ieee802dot1mibs=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021PbbComponentIdentifier',_N,'ieee802dot1mibs')
InterfaceIndex,ifGeneralInformationGroup=mibBuilder.importSymbols(_O,'InterfaceIndex',_P)
LldpV2DestAddressTableIndex,=mibBuilder.importSymbols('LLDP-V2-TC-MIB',_Q)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
systemGroup,=mibBuilder.importSymbols(_R,_S)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_f,_g)
ieee8021CnMib=ModuleIdentity((1,3,111,2,802,1,1,18))
if mibBuilder.loadTexts:ieee8021CnMib.setRevisions(('2018-06-28 00:00','2014-12-15 00:00','2011-02-27 00:00','2009-12-18 00:00'))
class Ieee8021CnControlChoice(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_h,1),(_i,2),('cpcComp',3)))
class Ieee8021CnDefenseMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('cptDisabled',1),(_j,2),(_k,3),(_l,4)))
class Ieee8021CnLldpChoice(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_m,1),(_n,2),('cnlComponent',3)))
_Ieee8021CnMIBObjects_ObjectIdentity=ObjectIdentity
ieee8021CnMIBObjects=_Ieee8021CnMIBObjects_ObjectIdentity((1,3,111,2,802,1,1,18,1))
_Ieee8021CnGlobalTable_Object=MibTable
ieee8021CnGlobalTable=_Ieee8021CnGlobalTable_Object((1,3,111,2,802,1,1,18,1,1))
if mibBuilder.loadTexts:ieee8021CnGlobalTable.setStatus(_A)
_Ieee8021CnGlobalEntry_Object=MibTableRow
ieee8021CnGlobalEntry=_Ieee8021CnGlobalEntry_Object((1,3,111,2,802,1,1,18,1,1,1))
ieee8021CnGlobalEntry.setIndexNames((0,_B,_o))
if mibBuilder.loadTexts:ieee8021CnGlobalEntry.setStatus(_A)
_Ieee8021CnGlobalComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021CnGlobalComponentId_Object=MibTableColumn
ieee8021CnGlobalComponentId=_Ieee8021CnGlobalComponentId_Object((1,3,111,2,802,1,1,18,1,1,1,1),_Ieee8021CnGlobalComponentId_Type())
ieee8021CnGlobalComponentId.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnGlobalComponentId.setStatus(_A)
_Ieee8021CnGlobalMasterEnable_Type=TruthValue
_Ieee8021CnGlobalMasterEnable_Object=MibTableColumn
ieee8021CnGlobalMasterEnable=_Ieee8021CnGlobalMasterEnable_Object((1,3,111,2,802,1,1,18,1,1,1,2),_Ieee8021CnGlobalMasterEnable_Type())
ieee8021CnGlobalMasterEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnGlobalMasterEnable.setStatus(_A)
_Ieee8021CnGlobalCnmTransmitPriority_Type=IEEE8021PriorityValue
_Ieee8021CnGlobalCnmTransmitPriority_Object=MibTableColumn
ieee8021CnGlobalCnmTransmitPriority=_Ieee8021CnGlobalCnmTransmitPriority_Object((1,3,111,2,802,1,1,18,1,1,1,3),_Ieee8021CnGlobalCnmTransmitPriority_Type())
ieee8021CnGlobalCnmTransmitPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnGlobalCnmTransmitPriority.setStatus(_A)
_Ieee8021CnGlobalDiscardedFrames_Type=Counter64
_Ieee8021CnGlobalDiscardedFrames_Object=MibTableColumn
ieee8021CnGlobalDiscardedFrames=_Ieee8021CnGlobalDiscardedFrames_Object((1,3,111,2,802,1,1,18,1,1,1,4),_Ieee8021CnGlobalDiscardedFrames_Type())
ieee8021CnGlobalDiscardedFrames.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CnGlobalDiscardedFrames.setStatus(_A)
if mibBuilder.loadTexts:ieee8021CnGlobalDiscardedFrames.setUnits(_I)
_Ieee8021CnErroredPortTable_Object=MibTable
ieee8021CnErroredPortTable=_Ieee8021CnErroredPortTable_Object((1,3,111,2,802,1,1,18,1,2))
if mibBuilder.loadTexts:ieee8021CnErroredPortTable.setStatus(_A)
_Ieee8021CnErroredPortEntry_Object=MibTableRow
ieee8021CnErroredPortEntry=_Ieee8021CnErroredPortEntry_Object((1,3,111,2,802,1,1,18,1,2,1))
ieee8021CnErroredPortEntry.setIndexNames((0,_B,_p),(0,_B,_q),(0,_B,_T))
if mibBuilder.loadTexts:ieee8021CnErroredPortEntry.setStatus(_A)
_Ieee8021CnEpComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021CnEpComponentId_Object=MibTableColumn
ieee8021CnEpComponentId=_Ieee8021CnEpComponentId_Object((1,3,111,2,802,1,1,18,1,2,1,1),_Ieee8021CnEpComponentId_Type())
ieee8021CnEpComponentId.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnEpComponentId.setStatus(_A)
_Ieee8021CnEpPriority_Type=IEEE8021PriorityValue
_Ieee8021CnEpPriority_Object=MibTableColumn
ieee8021CnEpPriority=_Ieee8021CnEpPriority_Object((1,3,111,2,802,1,1,18,1,2,1,2),_Ieee8021CnEpPriority_Type())
ieee8021CnEpPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnEpPriority.setStatus(_A)
_Ieee8021CnEpIfIndex_Type=InterfaceIndex
_Ieee8021CnEpIfIndex_Object=MibTableColumn
ieee8021CnEpIfIndex=_Ieee8021CnEpIfIndex_Object((1,3,111,2,802,1,1,18,1,2,1,3),_Ieee8021CnEpIfIndex_Type())
ieee8021CnEpIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CnEpIfIndex.setStatus(_A)
_Ieee8021CnCompntPriTable_Object=MibTable
ieee8021CnCompntPriTable=_Ieee8021CnCompntPriTable_Object((1,3,111,2,802,1,1,18,1,3))
if mibBuilder.loadTexts:ieee8021CnCompntPriTable.setStatus(_A)
_Ieee8021CnCompntPriEntry_Object=MibTableRow
ieee8021CnCompntPriEntry=_Ieee8021CnCompntPriEntry_Object((1,3,111,2,802,1,1,18,1,3,1))
ieee8021CnCompntPriEntry.setIndexNames((0,_B,_r),(0,_B,_s))
if mibBuilder.loadTexts:ieee8021CnCompntPriEntry.setStatus(_A)
_Ieee8021CnComPriComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021CnComPriComponentId_Object=MibTableColumn
ieee8021CnComPriComponentId=_Ieee8021CnComPriComponentId_Object((1,3,111,2,802,1,1,18,1,3,1,1),_Ieee8021CnComPriComponentId_Type())
ieee8021CnComPriComponentId.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnComPriComponentId.setStatus(_A)
_Ieee8021CnComPriPriority_Type=IEEE8021PriorityValue
_Ieee8021CnComPriPriority_Object=MibTableColumn
ieee8021CnComPriPriority=_Ieee8021CnComPriPriority_Object((1,3,111,2,802,1,1,18,1,3,1,2),_Ieee8021CnComPriPriority_Type())
ieee8021CnComPriPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnComPriPriority.setStatus(_A)
class _Ieee8021CnComPriDefModeChoice_Type(Ieee8021CnControlChoice):defaultValue=2;subtypeSpec=Ieee8021CnControlChoice.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_Ieee8021CnComPriDefModeChoice_Type.__name__=_U
_Ieee8021CnComPriDefModeChoice_Object=MibTableColumn
ieee8021CnComPriDefModeChoice=_Ieee8021CnComPriDefModeChoice_Object((1,3,111,2,802,1,1,18,1,3,1,3),_Ieee8021CnComPriDefModeChoice_Type())
ieee8021CnComPriDefModeChoice.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021CnComPriDefModeChoice.setStatus(_A)
class _Ieee8021CnComPriAlternatePriority_Type(IEEE8021PriorityValue):defaultValue=0
_Ieee8021CnComPriAlternatePriority_Type.__name__=_N
_Ieee8021CnComPriAlternatePriority_Object=MibTableColumn
ieee8021CnComPriAlternatePriority=_Ieee8021CnComPriAlternatePriority_Object((1,3,111,2,802,1,1,18,1,3,1,4),_Ieee8021CnComPriAlternatePriority_Type())
ieee8021CnComPriAlternatePriority.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021CnComPriAlternatePriority.setStatus(_A)
_Ieee8021CnComPriAutoAltPri_Type=IEEE8021PriorityValue
_Ieee8021CnComPriAutoAltPri_Object=MibTableColumn
ieee8021CnComPriAutoAltPri=_Ieee8021CnComPriAutoAltPri_Object((1,3,111,2,802,1,1,18,1,3,1,5),_Ieee8021CnComPriAutoAltPri_Type())
ieee8021CnComPriAutoAltPri.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CnComPriAutoAltPri.setStatus(_A)
class _Ieee8021CnComPriAdminDefenseMode_Type(Ieee8021CnDefenseMode):defaultValue=2
_Ieee8021CnComPriAdminDefenseMode_Type.__name__=_J
_Ieee8021CnComPriAdminDefenseMode_Object=MibTableColumn
ieee8021CnComPriAdminDefenseMode=_Ieee8021CnComPriAdminDefenseMode_Object((1,3,111,2,802,1,1,18,1,3,1,6),_Ieee8021CnComPriAdminDefenseMode_Type())
ieee8021CnComPriAdminDefenseMode.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021CnComPriAdminDefenseMode.setStatus(_A)
class _Ieee8021CnComPriCreation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cncpAutoEnable',1),('cncpAutoDisable',2)))
_Ieee8021CnComPriCreation_Type.__name__=_H
_Ieee8021CnComPriCreation_Object=MibTableColumn
ieee8021CnComPriCreation=_Ieee8021CnComPriCreation_Object((1,3,111,2,802,1,1,18,1,3,1,7),_Ieee8021CnComPriCreation_Type())
ieee8021CnComPriCreation.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021CnComPriCreation.setStatus(_A)
class _Ieee8021CnComPriLldpInstanceChoice_Type(Ieee8021CnLldpChoice):defaultValue=2;subtypeSpec=Ieee8021CnLldpChoice.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_m,1),(_n,2)))
_Ieee8021CnComPriLldpInstanceChoice_Type.__name__=_V
_Ieee8021CnComPriLldpInstanceChoice_Object=MibTableColumn
ieee8021CnComPriLldpInstanceChoice=_Ieee8021CnComPriLldpInstanceChoice_Object((1,3,111,2,802,1,1,18,1,3,1,8),_Ieee8021CnComPriLldpInstanceChoice_Type())
ieee8021CnComPriLldpInstanceChoice.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021CnComPriLldpInstanceChoice.setStatus(_A)
class _Ieee8021CnComPriLldpInstanceSelector_Type(LldpV2DestAddressTableIndex):defaultValue=1
_Ieee8021CnComPriLldpInstanceSelector_Type.__name__=_Q
_Ieee8021CnComPriLldpInstanceSelector_Object=MibTableColumn
ieee8021CnComPriLldpInstanceSelector=_Ieee8021CnComPriLldpInstanceSelector_Object((1,3,111,2,802,1,1,18,1,3,1,9),_Ieee8021CnComPriLldpInstanceSelector_Type())
ieee8021CnComPriLldpInstanceSelector.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021CnComPriLldpInstanceSelector.setStatus(_A)
_Ieee8021CnComPriRowStatus_Type=RowStatus
_Ieee8021CnComPriRowStatus_Object=MibTableColumn
ieee8021CnComPriRowStatus=_Ieee8021CnComPriRowStatus_Object((1,3,111,2,802,1,1,18,1,3,1,10),_Ieee8021CnComPriRowStatus_Type())
ieee8021CnComPriRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021CnComPriRowStatus.setStatus(_A)
_Ieee8021CnPortPriTable_Object=MibTable
ieee8021CnPortPriTable=_Ieee8021CnPortPriTable_Object((1,3,111,2,802,1,1,18,1,4))
if mibBuilder.loadTexts:ieee8021CnPortPriTable.setStatus(_A)
_Ieee8021CnPortPriEntry_Object=MibTableRow
ieee8021CnPortPriEntry=_Ieee8021CnPortPriEntry_Object((1,3,111,2,802,1,1,18,1,4,1))
ieee8021CnPortPriEntry.setIndexNames((0,_B,_t),(0,_B,_u),(0,_B,_v))
if mibBuilder.loadTexts:ieee8021CnPortPriEntry.setStatus(_A)
_Ieee8021CnPortPriComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021CnPortPriComponentId_Object=MibTableColumn
ieee8021CnPortPriComponentId=_Ieee8021CnPortPriComponentId_Object((1,3,111,2,802,1,1,18,1,4,1,1),_Ieee8021CnPortPriComponentId_Type())
ieee8021CnPortPriComponentId.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnPortPriComponentId.setStatus(_A)
_Ieee8021CnPortPriority_Type=IEEE8021PriorityValue
_Ieee8021CnPortPriority_Object=MibTableColumn
ieee8021CnPortPriority=_Ieee8021CnPortPriority_Object((1,3,111,2,802,1,1,18,1,4,1,2),_Ieee8021CnPortPriority_Type())
ieee8021CnPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnPortPriority.setStatus(_A)
_Ieee8021CnPortPriIfIndex_Type=InterfaceIndex
_Ieee8021CnPortPriIfIndex_Object=MibTableColumn
ieee8021CnPortPriIfIndex=_Ieee8021CnPortPriIfIndex_Object((1,3,111,2,802,1,1,18,1,4,1,3),_Ieee8021CnPortPriIfIndex_Type())
ieee8021CnPortPriIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnPortPriIfIndex.setStatus(_A)
class _Ieee8021CnPortPriDefModeChoice_Type(Ieee8021CnControlChoice):defaultValue=3
_Ieee8021CnPortPriDefModeChoice_Type.__name__=_U
_Ieee8021CnPortPriDefModeChoice_Object=MibTableColumn
ieee8021CnPortPriDefModeChoice=_Ieee8021CnPortPriDefModeChoice_Object((1,3,111,2,802,1,1,18,1,4,1,4),_Ieee8021CnPortPriDefModeChoice_Type())
ieee8021CnPortPriDefModeChoice.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnPortPriDefModeChoice.setStatus(_A)
class _Ieee8021CnPortPriAdminDefenseMode_Type(Ieee8021CnDefenseMode):defaultValue=1
_Ieee8021CnPortPriAdminDefenseMode_Type.__name__=_J
_Ieee8021CnPortPriAdminDefenseMode_Object=MibTableColumn
ieee8021CnPortPriAdminDefenseMode=_Ieee8021CnPortPriAdminDefenseMode_Object((1,3,111,2,802,1,1,18,1,4,1,5),_Ieee8021CnPortPriAdminDefenseMode_Type())
ieee8021CnPortPriAdminDefenseMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnPortPriAdminDefenseMode.setStatus(_A)
class _Ieee8021CnPortPriAutoDefenseMode_Type(Ieee8021CnDefenseMode):subtypeSpec=Ieee8021CnDefenseMode.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_j,2),(_k,3),(_l,4)))
_Ieee8021CnPortPriAutoDefenseMode_Type.__name__=_J
_Ieee8021CnPortPriAutoDefenseMode_Object=MibTableColumn
ieee8021CnPortPriAutoDefenseMode=_Ieee8021CnPortPriAutoDefenseMode_Object((1,3,111,2,802,1,1,18,1,4,1,6),_Ieee8021CnPortPriAutoDefenseMode_Type())
ieee8021CnPortPriAutoDefenseMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CnPortPriAutoDefenseMode.setStatus(_A)
class _Ieee8021CnPortPriLldpInstanceChoice_Type(Ieee8021CnLldpChoice):defaultValue=3
_Ieee8021CnPortPriLldpInstanceChoice_Type.__name__=_V
_Ieee8021CnPortPriLldpInstanceChoice_Object=MibTableColumn
ieee8021CnPortPriLldpInstanceChoice=_Ieee8021CnPortPriLldpInstanceChoice_Object((1,3,111,2,802,1,1,18,1,4,1,7),_Ieee8021CnPortPriLldpInstanceChoice_Type())
ieee8021CnPortPriLldpInstanceChoice.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnPortPriLldpInstanceChoice.setStatus(_A)
class _Ieee8021CnPortPriLldpInstanceSelector_Type(LldpV2DestAddressTableIndex):defaultValue=3
_Ieee8021CnPortPriLldpInstanceSelector_Type.__name__=_Q
_Ieee8021CnPortPriLldpInstanceSelector_Object=MibTableColumn
ieee8021CnPortPriLldpInstanceSelector=_Ieee8021CnPortPriLldpInstanceSelector_Object((1,3,111,2,802,1,1,18,1,4,1,8),_Ieee8021CnPortPriLldpInstanceSelector_Type())
ieee8021CnPortPriLldpInstanceSelector.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnPortPriLldpInstanceSelector.setStatus(_A)
class _Ieee8021CnPortPriAlternatePriority_Type(IEEE8021PriorityValue):defaultValue=0
_Ieee8021CnPortPriAlternatePriority_Type.__name__=_N
_Ieee8021CnPortPriAlternatePriority_Object=MibTableColumn
ieee8021CnPortPriAlternatePriority=_Ieee8021CnPortPriAlternatePriority_Object((1,3,111,2,802,1,1,18,1,4,1,9),_Ieee8021CnPortPriAlternatePriority_Type())
ieee8021CnPortPriAlternatePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnPortPriAlternatePriority.setStatus(_A)
_Ieee8021CnCpTable_Object=MibTable
ieee8021CnCpTable=_Ieee8021CnCpTable_Object((1,3,111,2,802,1,1,18,1,5))
if mibBuilder.loadTexts:ieee8021CnCpTable.setStatus(_A)
_Ieee8021CnCpEntry_Object=MibTableRow
ieee8021CnCpEntry=_Ieee8021CnCpEntry_Object((1,3,111,2,802,1,1,18,1,5,1))
ieee8021CnCpEntry.setIndexNames((0,_B,_w),(0,_B,_x),(0,_B,_y))
if mibBuilder.loadTexts:ieee8021CnCpEntry.setStatus(_A)
_Ieee8021CnCpComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021CnCpComponentId_Object=MibTableColumn
ieee8021CnCpComponentId=_Ieee8021CnCpComponentId_Object((1,3,111,2,802,1,1,18,1,5,1,1),_Ieee8021CnCpComponentId_Type())
ieee8021CnCpComponentId.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnCpComponentId.setStatus(_A)
_Ieee8021CnCpIfIndex_Type=InterfaceIndex
_Ieee8021CnCpIfIndex_Object=MibTableColumn
ieee8021CnCpIfIndex=_Ieee8021CnCpIfIndex_Object((1,3,111,2,802,1,1,18,1,5,1,2),_Ieee8021CnCpIfIndex_Type())
ieee8021CnCpIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnCpIfIndex.setStatus(_A)
class _Ieee8021CnCpIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_Ieee8021CnCpIndex_Type.__name__=_F
_Ieee8021CnCpIndex_Object=MibTableColumn
ieee8021CnCpIndex=_Ieee8021CnCpIndex_Object((1,3,111,2,802,1,1,18,1,5,1,3),_Ieee8021CnCpIndex_Type())
ieee8021CnCpIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnCpIndex.setStatus(_A)
_Ieee8021CnCpPriority_Type=IEEE8021PriorityValue
_Ieee8021CnCpPriority_Object=MibTableColumn
ieee8021CnCpPriority=_Ieee8021CnCpPriority_Object((1,3,111,2,802,1,1,18,1,5,1,4),_Ieee8021CnCpPriority_Type())
ieee8021CnCpPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CnCpPriority.setStatus(_A)
_Ieee8021CnCpMacAddress_Type=MacAddress
_Ieee8021CnCpMacAddress_Object=MibTableColumn
ieee8021CnCpMacAddress=_Ieee8021CnCpMacAddress_Object((1,3,111,2,802,1,1,18,1,5,1,5),_Ieee8021CnCpMacAddress_Type())
ieee8021CnCpMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CnCpMacAddress.setStatus(_A)
class _Ieee8021CnCpIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_Ieee8021CnCpIdentifier_Type.__name__=_M
_Ieee8021CnCpIdentifier_Object=MibTableColumn
ieee8021CnCpIdentifier=_Ieee8021CnCpIdentifier_Object((1,3,111,2,802,1,1,18,1,5,1,6),_Ieee8021CnCpIdentifier_Type())
ieee8021CnCpIdentifier.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CnCpIdentifier.setStatus(_A)
class _Ieee8021CnCpQueueSizeSetPoint_Type(Unsigned32):defaultValue=26000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,4294967295))
_Ieee8021CnCpQueueSizeSetPoint_Type.__name__=_F
_Ieee8021CnCpQueueSizeSetPoint_Object=MibTableColumn
ieee8021CnCpQueueSizeSetPoint=_Ieee8021CnCpQueueSizeSetPoint_Object((1,3,111,2,802,1,1,18,1,5,1,7),_Ieee8021CnCpQueueSizeSetPoint_Type())
ieee8021CnCpQueueSizeSetPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnCpQueueSizeSetPoint.setStatus(_A)
if mibBuilder.loadTexts:ieee8021CnCpQueueSizeSetPoint.setUnits(_K)
class _Ieee8021CnCpFeedbackWeight_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10,10))
_Ieee8021CnCpFeedbackWeight_Type.__name__=_H
_Ieee8021CnCpFeedbackWeight_Object=MibTableColumn
ieee8021CnCpFeedbackWeight=_Ieee8021CnCpFeedbackWeight_Object((1,3,111,2,802,1,1,18,1,5,1,8),_Ieee8021CnCpFeedbackWeight_Type())
ieee8021CnCpFeedbackWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnCpFeedbackWeight.setStatus(_A)
class _Ieee8021CnCpMinSampleBase_Type(Unsigned32):defaultValue=150000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10000,4294967295))
_Ieee8021CnCpMinSampleBase_Type.__name__=_F
_Ieee8021CnCpMinSampleBase_Object=MibTableColumn
ieee8021CnCpMinSampleBase=_Ieee8021CnCpMinSampleBase_Object((1,3,111,2,802,1,1,18,1,5,1,9),_Ieee8021CnCpMinSampleBase_Type())
ieee8021CnCpMinSampleBase.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnCpMinSampleBase.setStatus(_A)
if mibBuilder.loadTexts:ieee8021CnCpMinSampleBase.setUnits(_K)
_Ieee8021CnCpDiscardedFrames_Type=Counter64
_Ieee8021CnCpDiscardedFrames_Object=MibTableColumn
ieee8021CnCpDiscardedFrames=_Ieee8021CnCpDiscardedFrames_Object((1,3,111,2,802,1,1,18,1,5,1,10),_Ieee8021CnCpDiscardedFrames_Type())
ieee8021CnCpDiscardedFrames.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CnCpDiscardedFrames.setStatus(_A)
if mibBuilder.loadTexts:ieee8021CnCpDiscardedFrames.setUnits(_I)
_Ieee8021CnCpTransmittedFrames_Type=Counter64
_Ieee8021CnCpTransmittedFrames_Object=MibTableColumn
ieee8021CnCpTransmittedFrames=_Ieee8021CnCpTransmittedFrames_Object((1,3,111,2,802,1,1,18,1,5,1,11),_Ieee8021CnCpTransmittedFrames_Type())
ieee8021CnCpTransmittedFrames.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CnCpTransmittedFrames.setStatus(_A)
if mibBuilder.loadTexts:ieee8021CnCpTransmittedFrames.setUnits(_I)
_Ieee8021CnCpTransmittedCnms_Type=Counter64
_Ieee8021CnCpTransmittedCnms_Object=MibTableColumn
ieee8021CnCpTransmittedCnms=_Ieee8021CnCpTransmittedCnms_Object((1,3,111,2,802,1,1,18,1,5,1,12),_Ieee8021CnCpTransmittedCnms_Type())
ieee8021CnCpTransmittedCnms.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CnCpTransmittedCnms.setStatus(_A)
if mibBuilder.loadTexts:ieee8021CnCpTransmittedCnms.setUnits(_I)
class _Ieee8021CnCpMinHeaderOctets_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_Ieee8021CnCpMinHeaderOctets_Type.__name__=_F
_Ieee8021CnCpMinHeaderOctets_Object=MibTableColumn
ieee8021CnCpMinHeaderOctets=_Ieee8021CnCpMinHeaderOctets_Object((1,3,111,2,802,1,1,18,1,5,1,13),_Ieee8021CnCpMinHeaderOctets_Type())
ieee8021CnCpMinHeaderOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnCpMinHeaderOctets.setStatus(_A)
if mibBuilder.loadTexts:ieee8021CnCpMinHeaderOctets.setUnits(_K)
_Ieee8021CnCpidToInterfaceTable_Object=MibTable
ieee8021CnCpidToInterfaceTable=_Ieee8021CnCpidToInterfaceTable_Object((1,3,111,2,802,1,1,18,1,6))
if mibBuilder.loadTexts:ieee8021CnCpidToInterfaceTable.setStatus(_A)
_Ieee8021CnCpidToInterfaceEntry_Object=MibTableRow
ieee8021CnCpidToInterfaceEntry=_Ieee8021CnCpidToInterfaceEntry_Object((1,3,111,2,802,1,1,18,1,6,1))
ieee8021CnCpidToInterfaceEntry.setIndexNames((0,_B,_z))
if mibBuilder.loadTexts:ieee8021CnCpidToInterfaceEntry.setStatus(_A)
class _Ieee8021CnCpidToIfCpid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_Ieee8021CnCpidToIfCpid_Type.__name__=_M
_Ieee8021CnCpidToIfCpid_Object=MibTableColumn
ieee8021CnCpidToIfCpid=_Ieee8021CnCpidToIfCpid_Object((1,3,111,2,802,1,1,18,1,6,1,1),_Ieee8021CnCpidToIfCpid_Type())
ieee8021CnCpidToIfCpid.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnCpidToIfCpid.setStatus(_A)
_Ieee8021CnCpidToIfComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021CnCpidToIfComponentId_Object=MibTableColumn
ieee8021CnCpidToIfComponentId=_Ieee8021CnCpidToIfComponentId_Object((1,3,111,2,802,1,1,18,1,6,1,2),_Ieee8021CnCpidToIfComponentId_Type())
ieee8021CnCpidToIfComponentId.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CnCpidToIfComponentId.setStatus(_A)
_Ieee8021CnCpidToIfIfIndex_Type=InterfaceIndex
_Ieee8021CnCpidToIfIfIndex_Object=MibTableColumn
ieee8021CnCpidToIfIfIndex=_Ieee8021CnCpidToIfIfIndex_Object((1,3,111,2,802,1,1,18,1,6,1,3),_Ieee8021CnCpidToIfIfIndex_Type())
ieee8021CnCpidToIfIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CnCpidToIfIfIndex.setStatus(_A)
class _Ieee8021CnCpidToIfCpIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_Ieee8021CnCpidToIfCpIndex_Type.__name__=_F
_Ieee8021CnCpidToIfCpIndex_Object=MibTableColumn
ieee8021CnCpidToIfCpIndex=_Ieee8021CnCpidToIfCpIndex_Object((1,3,111,2,802,1,1,18,1,6,1,4),_Ieee8021CnCpidToIfCpIndex_Type())
ieee8021CnCpidToIfCpIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CnCpidToIfCpIndex.setStatus(_A)
_Ieee8021CnRpPortPriTable_Object=MibTable
ieee8021CnRpPortPriTable=_Ieee8021CnRpPortPriTable_Object((1,3,111,2,802,1,1,18,1,7))
if mibBuilder.loadTexts:ieee8021CnRpPortPriTable.setStatus(_A)
_Ieee8021CnRpPortPriEntry_Object=MibTableRow
ieee8021CnRpPortPriEntry=_Ieee8021CnRpPortPriEntry_Object((1,3,111,2,802,1,1,18,1,7,1))
ieee8021CnRpPortPriEntry.setIndexNames((0,_B,_A0),(0,_B,_A1),(0,_B,_A2))
if mibBuilder.loadTexts:ieee8021CnRpPortPriEntry.setStatus(_A)
_Ieee8021CnRpPortPriComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021CnRpPortPriComponentId_Object=MibTableColumn
ieee8021CnRpPortPriComponentId=_Ieee8021CnRpPortPriComponentId_Object((1,3,111,2,802,1,1,18,1,7,1,1),_Ieee8021CnRpPortPriComponentId_Type())
ieee8021CnRpPortPriComponentId.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnRpPortPriComponentId.setStatus(_A)
_Ieee8021CnRpPortPriPriority_Type=IEEE8021PriorityValue
_Ieee8021CnRpPortPriPriority_Object=MibTableColumn
ieee8021CnRpPortPriPriority=_Ieee8021CnRpPortPriPriority_Object((1,3,111,2,802,1,1,18,1,7,1,2),_Ieee8021CnRpPortPriPriority_Type())
ieee8021CnRpPortPriPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnRpPortPriPriority.setStatus(_A)
_Ieee8021CnRpPortPriIfIndex_Type=InterfaceIndex
_Ieee8021CnRpPortPriIfIndex_Object=MibTableColumn
ieee8021CnRpPortPriIfIndex=_Ieee8021CnRpPortPriIfIndex_Object((1,3,111,2,802,1,1,18,1,7,1,3),_Ieee8021CnRpPortPriIfIndex_Type())
ieee8021CnRpPortPriIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnRpPortPriIfIndex.setStatus(_A)
class _Ieee8021CnRpPortPriMaxRps_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_Ieee8021CnRpPortPriMaxRps_Type.__name__=_F
_Ieee8021CnRpPortPriMaxRps_Object=MibTableColumn
ieee8021CnRpPortPriMaxRps=_Ieee8021CnRpPortPriMaxRps_Object((1,3,111,2,802,1,1,18,1,7,1,4),_Ieee8021CnRpPortPriMaxRps_Type())
ieee8021CnRpPortPriMaxRps.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnRpPortPriMaxRps.setStatus(_A)
_Ieee8021CnRpPortPriCreatedRps_Type=Counter32
_Ieee8021CnRpPortPriCreatedRps_Object=MibTableColumn
ieee8021CnRpPortPriCreatedRps=_Ieee8021CnRpPortPriCreatedRps_Object((1,3,111,2,802,1,1,18,1,7,1,5),_Ieee8021CnRpPortPriCreatedRps_Type())
ieee8021CnRpPortPriCreatedRps.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CnRpPortPriCreatedRps.setStatus(_A)
_Ieee8021CnRpPortPriCentiseconds_Type=Counter64
_Ieee8021CnRpPortPriCentiseconds_Object=MibTableColumn
ieee8021CnRpPortPriCentiseconds=_Ieee8021CnRpPortPriCentiseconds_Object((1,3,111,2,802,1,1,18,1,7,1,6),_Ieee8021CnRpPortPriCentiseconds_Type())
ieee8021CnRpPortPriCentiseconds.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CnRpPortPriCentiseconds.setStatus(_A)
if mibBuilder.loadTexts:ieee8021CnRpPortPriCentiseconds.setUnits('centiseconds')
_Ieee8021CnRpGroupTable_Object=MibTable
ieee8021CnRpGroupTable=_Ieee8021CnRpGroupTable_Object((1,3,111,2,802,1,1,18,1,8))
if mibBuilder.loadTexts:ieee8021CnRpGroupTable.setStatus(_A)
_Ieee8021CnRpGroupEntry_Object=MibTableRow
ieee8021CnRpGroupEntry=_Ieee8021CnRpGroupEntry_Object((1,3,111,2,802,1,1,18,1,8,1))
ieee8021CnRpGroupEntry.setIndexNames((0,_B,_A3),(0,_B,_A4),(0,_B,_A5),(0,_B,_A6))
if mibBuilder.loadTexts:ieee8021CnRpGroupEntry.setStatus(_A)
_Ieee8021CnRpgComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021CnRpgComponentId_Object=MibTableColumn
ieee8021CnRpgComponentId=_Ieee8021CnRpgComponentId_Object((1,3,111,2,802,1,1,18,1,8,1,1),_Ieee8021CnRpgComponentId_Type())
ieee8021CnRpgComponentId.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnRpgComponentId.setStatus(_A)
_Ieee8021CnRpgPriority_Type=IEEE8021PriorityValue
_Ieee8021CnRpgPriority_Object=MibTableColumn
ieee8021CnRpgPriority=_Ieee8021CnRpgPriority_Object((1,3,111,2,802,1,1,18,1,8,1,2),_Ieee8021CnRpgPriority_Type())
ieee8021CnRpgPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnRpgPriority.setStatus(_A)
_Ieee8021CnRpgIfIndex_Type=InterfaceIndex
_Ieee8021CnRpgIfIndex_Object=MibTableColumn
ieee8021CnRpgIfIndex=_Ieee8021CnRpgIfIndex_Object((1,3,111,2,802,1,1,18,1,8,1,3),_Ieee8021CnRpgIfIndex_Type())
ieee8021CnRpgIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnRpgIfIndex.setStatus(_A)
class _Ieee8021CnRpgIdentifier_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_Ieee8021CnRpgIdentifier_Type.__name__=_F
_Ieee8021CnRpgIdentifier_Object=MibTableColumn
ieee8021CnRpgIdentifier=_Ieee8021CnRpgIdentifier_Object((1,3,111,2,802,1,1,18,1,8,1,4),_Ieee8021CnRpgIdentifier_Type())
ieee8021CnRpgIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CnRpgIdentifier.setStatus(_A)
class _Ieee8021CnRpgEnable_Type(TruthValue):defaultValue=1
_Ieee8021CnRpgEnable_Type.__name__=_g
_Ieee8021CnRpgEnable_Object=MibTableColumn
ieee8021CnRpgEnable=_Ieee8021CnRpgEnable_Object((1,3,111,2,802,1,1,18,1,8,1,5),_Ieee8021CnRpgEnable_Type())
ieee8021CnRpgEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnRpgEnable.setStatus(_A)
class _Ieee8021CnRpgTimeReset_Type(TimeInterval):defaultValue=15
_Ieee8021CnRpgTimeReset_Type.__name__=_f
_Ieee8021CnRpgTimeReset_Object=MibTableColumn
ieee8021CnRpgTimeReset=_Ieee8021CnRpgTimeReset_Object((1,3,111,2,802,1,1,18,1,8,1,6),_Ieee8021CnRpgTimeReset_Type())
ieee8021CnRpgTimeReset.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnRpgTimeReset.setStatus(_A)
if mibBuilder.loadTexts:ieee8021CnRpgTimeReset.setUnits('milliseconds')
class _Ieee8021CnRpgByteReset_Type(Unsigned32):defaultValue=150000
_Ieee8021CnRpgByteReset_Type.__name__=_F
_Ieee8021CnRpgByteReset_Object=MibTableColumn
ieee8021CnRpgByteReset=_Ieee8021CnRpgByteReset_Object((1,3,111,2,802,1,1,18,1,8,1,7),_Ieee8021CnRpgByteReset_Type())
ieee8021CnRpgByteReset.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnRpgByteReset.setStatus(_A)
if mibBuilder.loadTexts:ieee8021CnRpgByteReset.setUnits(_K)
class _Ieee8021CnRpgThreshold_Type(Unsigned32):defaultValue=5
_Ieee8021CnRpgThreshold_Type.__name__=_F
_Ieee8021CnRpgThreshold_Object=MibTableColumn
ieee8021CnRpgThreshold=_Ieee8021CnRpgThreshold_Object((1,3,111,2,802,1,1,18,1,8,1,8),_Ieee8021CnRpgThreshold_Type())
ieee8021CnRpgThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnRpgThreshold.setStatus(_A)
_Ieee8021CnRpgMaxRate_Type=Unsigned32
_Ieee8021CnRpgMaxRate_Object=MibTableColumn
ieee8021CnRpgMaxRate=_Ieee8021CnRpgMaxRate_Object((1,3,111,2,802,1,1,18,1,8,1,9),_Ieee8021CnRpgMaxRate_Type())
ieee8021CnRpgMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnRpgMaxRate.setStatus(_A)
if mibBuilder.loadTexts:ieee8021CnRpgMaxRate.setUnits(_L)
class _Ieee8021CnRpgAiRate_Type(Unsigned32):defaultValue=5
_Ieee8021CnRpgAiRate_Type.__name__=_F
_Ieee8021CnRpgAiRate_Object=MibTableColumn
ieee8021CnRpgAiRate=_Ieee8021CnRpgAiRate_Object((1,3,111,2,802,1,1,18,1,8,1,10),_Ieee8021CnRpgAiRate_Type())
ieee8021CnRpgAiRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnRpgAiRate.setStatus(_A)
if mibBuilder.loadTexts:ieee8021CnRpgAiRate.setUnits(_L)
class _Ieee8021CnRpgHaiRate_Type(Unsigned32):defaultValue=50
_Ieee8021CnRpgHaiRate_Type.__name__=_F
_Ieee8021CnRpgHaiRate_Object=MibTableColumn
ieee8021CnRpgHaiRate=_Ieee8021CnRpgHaiRate_Object((1,3,111,2,802,1,1,18,1,8,1,11),_Ieee8021CnRpgHaiRate_Type())
ieee8021CnRpgHaiRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnRpgHaiRate.setStatus(_A)
if mibBuilder.loadTexts:ieee8021CnRpgHaiRate.setUnits(_L)
class _Ieee8021CnRpgGd_Type(Integer32):defaultValue=7
_Ieee8021CnRpgGd_Type.__name__=_H
_Ieee8021CnRpgGd_Object=MibTableColumn
ieee8021CnRpgGd=_Ieee8021CnRpgGd_Object((1,3,111,2,802,1,1,18,1,8,1,12),_Ieee8021CnRpgGd_Type())
ieee8021CnRpgGd.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnRpgGd.setStatus(_A)
class _Ieee8021CnRpgMinDecFac_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_Ieee8021CnRpgMinDecFac_Type.__name__=_F
_Ieee8021CnRpgMinDecFac_Object=MibTableColumn
ieee8021CnRpgMinDecFac=_Ieee8021CnRpgMinDecFac_Object((1,3,111,2,802,1,1,18,1,8,1,13),_Ieee8021CnRpgMinDecFac_Type())
ieee8021CnRpgMinDecFac.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnRpgMinDecFac.setStatus(_A)
if mibBuilder.loadTexts:ieee8021CnRpgMinDecFac.setUnits('percent')
class _Ieee8021CnRpgMinRate_Type(Unsigned32):defaultValue=5
_Ieee8021CnRpgMinRate_Type.__name__=_F
_Ieee8021CnRpgMinRate_Object=MibTableColumn
ieee8021CnRpgMinRate=_Ieee8021CnRpgMinRate_Object((1,3,111,2,802,1,1,18,1,8,1,14),_Ieee8021CnRpgMinRate_Type())
ieee8021CnRpgMinRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021CnRpgMinRate.setStatus(_A)
if mibBuilder.loadTexts:ieee8021CnRpgMinRate.setUnits(_L)
_Ieee8021CnConformance_ObjectIdentity=ObjectIdentity
ieee8021CnConformance=_Ieee8021CnConformance_ObjectIdentity((1,3,111,2,802,1,1,18,2))
_Ieee8021CnCompliances_ObjectIdentity=ObjectIdentity
ieee8021CnCompliances=_Ieee8021CnCompliances_ObjectIdentity((1,3,111,2,802,1,1,18,2,1))
_Ieee8021CnGroups_ObjectIdentity=ObjectIdentity
ieee8021CnGroups=_Ieee8021CnGroups_ObjectIdentity((1,3,111,2,802,1,1,18,2,2))
ieee8021CnGlobalReqdGroup=ObjectGroup((1,3,111,2,802,1,1,18,2,2,1))
ieee8021CnGlobalReqdGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:ieee8021CnGlobalReqdGroup.setStatus(_A)
ieee8021CnCpGlobalGroup=ObjectGroup((1,3,111,2,802,1,1,18,2,2,2))
ieee8021CnCpGlobalGroup.setObjects(*((_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:ieee8021CnCpGlobalGroup.setStatus(_A)
ieee8021CnCpidTranslateGroup=ObjectGroup((1,3,111,2,802,1,1,18,2,2,3))
ieee8021CnCpidTranslateGroup.setObjects(*((_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:ieee8021CnCpidTranslateGroup.setStatus(_A)
ieee8021CnEplGroup=ObjectGroup((1,3,111,2,802,1,1,18,2,2,4))
ieee8021CnEplGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:ieee8021CnEplGroup.setStatus(_A)
ieee8021CnComPriGroup=ObjectGroup((1,3,111,2,802,1,1,18,2,2,5))
ieee8021CnComPriGroup.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:ieee8021CnComPriGroup.setStatus(_A)
ieee8021CnCpPriGroup=ObjectGroup((1,3,111,2,802,1,1,18,2,2,6))
ieee8021CnCpPriGroup.setObjects(*((_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:ieee8021CnCpPriGroup.setStatus(_A)
ieee8021CnGlobalPriPortGroup=ObjectGroup((1,3,111,2,802,1,1,18,2,2,7))
ieee8021CnGlobalPriPortGroup.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:ieee8021CnGlobalPriPortGroup.setStatus(_A)
ieee8021CnCpPriPortGroup=ObjectGroup((1,3,111,2,802,1,1,18,2,2,8))
ieee8021CnCpPriPortGroup.setObjects((_B,_AQ))
if mibBuilder.loadTexts:ieee8021CnCpPriPortGroup.setStatus(_A)
ieee8021CnCpGroup=ObjectGroup((1,3,111,2,802,1,1,18,2,2,9))
ieee8021CnCpGroup.setObjects(*((_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:ieee8021CnCpGroup.setStatus(_A)
ieee8021CnRpppGroup=ObjectGroup((1,3,111,2,802,1,1,18,2,2,10))
ieee8021CnRpppGroup.setObjects(*((_B,_Ab),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:ieee8021CnRpppGroup.setStatus(_A)
ieee8021CnRpGroup=ObjectGroup((1,3,111,2,802,1,1,18,2,2,11))
ieee8021CnRpGroup.setObjects(*((_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An)))
if mibBuilder.loadTexts:ieee8021CnRpGroup.setStatus(_A)
ieee8021CnBridgeCompliance=ModuleCompliance((1,3,111,2,802,1,1,18,2,1,1))
ieee8021CnBridgeCompliance.setObjects(*((_R,_S),(_O,_P),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:ieee8021CnBridgeCompliance.setStatus(_A)
ieee8021CnStationCompliance=ModuleCompliance((1,3,111,2,802,1,1,18,2,1,2))
ieee8021CnStationCompliance.setObjects(*((_R,_S),(_O,_P),(_B,_W),(_B,_a),(_B,_c),(_B,_Ao),(_B,_Ap),(_B,_X),(_B,_Y),(_B,_Z),(_B,_b),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:ieee8021CnStationCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_U:Ieee8021CnControlChoice,_J:Ieee8021CnDefenseMode,_V:Ieee8021CnLldpChoice,'ieee8021CnMib':ieee8021CnMib,'ieee8021CnMIBObjects':ieee8021CnMIBObjects,'ieee8021CnGlobalTable':ieee8021CnGlobalTable,'ieee8021CnGlobalEntry':ieee8021CnGlobalEntry,_o:ieee8021CnGlobalComponentId,_A7:ieee8021CnGlobalMasterEnable,_AA:ieee8021CnGlobalCnmTransmitPriority,_AB:ieee8021CnGlobalDiscardedFrames,'ieee8021CnErroredPortTable':ieee8021CnErroredPortTable,'ieee8021CnErroredPortEntry':ieee8021CnErroredPortEntry,_p:ieee8021CnEpComponentId,_q:ieee8021CnEpPriority,_T:ieee8021CnEpIfIndex,'ieee8021CnCompntPriTable':ieee8021CnCompntPriTable,'ieee8021CnCompntPriEntry':ieee8021CnCompntPriEntry,_r:ieee8021CnComPriComponentId,_s:ieee8021CnComPriPriority,_AF:ieee8021CnComPriDefModeChoice,_AJ:ieee8021CnComPriAlternatePriority,_AK:ieee8021CnComPriAutoAltPri,_AG:ieee8021CnComPriAdminDefenseMode,_AH:ieee8021CnComPriCreation,_A8:ieee8021CnComPriLldpInstanceChoice,_A9:ieee8021CnComPriLldpInstanceSelector,_AI:ieee8021CnComPriRowStatus,'ieee8021CnPortPriTable':ieee8021CnPortPriTable,'ieee8021CnPortPriEntry':ieee8021CnPortPriEntry,_t:ieee8021CnPortPriComponentId,_u:ieee8021CnPortPriority,_v:ieee8021CnPortPriIfIndex,_AL:ieee8021CnPortPriDefModeChoice,_AM:ieee8021CnPortPriAdminDefenseMode,_AN:ieee8021CnPortPriAutoDefenseMode,_AO:ieee8021CnPortPriLldpInstanceChoice,_AP:ieee8021CnPortPriLldpInstanceSelector,_AQ:ieee8021CnPortPriAlternatePriority,'ieee8021CnCpTable':ieee8021CnCpTable,'ieee8021CnCpEntry':ieee8021CnCpEntry,_w:ieee8021CnCpComponentId,_x:ieee8021CnCpIfIndex,_y:ieee8021CnCpIndex,_AR:ieee8021CnCpPriority,_AS:ieee8021CnCpMacAddress,_AT:ieee8021CnCpIdentifier,_AU:ieee8021CnCpQueueSizeSetPoint,_AV:ieee8021CnCpFeedbackWeight,_AW:ieee8021CnCpMinSampleBase,_AX:ieee8021CnCpDiscardedFrames,_AY:ieee8021CnCpTransmittedFrames,_AZ:ieee8021CnCpTransmittedCnms,_Aa:ieee8021CnCpMinHeaderOctets,'ieee8021CnCpidToInterfaceTable':ieee8021CnCpidToInterfaceTable,'ieee8021CnCpidToInterfaceEntry':ieee8021CnCpidToInterfaceEntry,_z:ieee8021CnCpidToIfCpid,_AC:ieee8021CnCpidToIfComponentId,_AD:ieee8021CnCpidToIfIfIndex,_AE:ieee8021CnCpidToIfCpIndex,'ieee8021CnRpPortPriTable':ieee8021CnRpPortPriTable,'ieee8021CnRpPortPriEntry':ieee8021CnRpPortPriEntry,_A0:ieee8021CnRpPortPriComponentId,_A1:ieee8021CnRpPortPriPriority,_A2:ieee8021CnRpPortPriIfIndex,_Ab:ieee8021CnRpPortPriMaxRps,_Ac:ieee8021CnRpPortPriCreatedRps,_Ad:ieee8021CnRpPortPriCentiseconds,'ieee8021CnRpGroupTable':ieee8021CnRpGroupTable,'ieee8021CnRpGroupEntry':ieee8021CnRpGroupEntry,_A3:ieee8021CnRpgComponentId,_A4:ieee8021CnRpgPriority,_A5:ieee8021CnRpgIfIndex,_A6:ieee8021CnRpgIdentifier,_Ae:ieee8021CnRpgEnable,_Af:ieee8021CnRpgTimeReset,_Ag:ieee8021CnRpgByteReset,_Ah:ieee8021CnRpgThreshold,_Ai:ieee8021CnRpgMaxRate,_Aj:ieee8021CnRpgAiRate,_Ak:ieee8021CnRpgHaiRate,_Al:ieee8021CnRpgGd,_Am:ieee8021CnRpgMinDecFac,_An:ieee8021CnRpgMinRate,'ieee8021CnConformance':ieee8021CnConformance,'ieee8021CnCompliances':ieee8021CnCompliances,'ieee8021CnBridgeCompliance':ieee8021CnBridgeCompliance,'ieee8021CnStationCompliance':ieee8021CnStationCompliance,'ieee8021CnGroups':ieee8021CnGroups,_W:ieee8021CnGlobalReqdGroup,_X:ieee8021CnCpGlobalGroup,_Y:ieee8021CnCpidTranslateGroup,_Z:ieee8021CnEplGroup,_a:ieee8021CnComPriGroup,_b:ieee8021CnCpPriGroup,_c:ieee8021CnGlobalPriPortGroup,_d:ieee8021CnCpPriPortGroup,_e:ieee8021CnCpGroup,_Ao:ieee8021CnRpppGroup,_Ap:ieee8021CnRpGroup})