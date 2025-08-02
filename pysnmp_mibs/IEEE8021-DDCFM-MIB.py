_AC='ieee8021DdcfmSoGroup'
_AB='ieee8021DdcfmDrGroup'
_AA='ieee8021DdcfmRFMReceiverGroup'
_A9='ieee8021DdcfmRrGroup'
_A8='ieee8021DdcfmStackGroup'
_A7='ieee8021DdcfmSoRowStatus'
_A6='ieee8021DdcfmSoRemainDuration'
_A5='ieee8021DdcfmSoActivationStatus'
_A4='ieee8021DdcfmSoDuration'
_A3='ieee8021DdcfmSoDrMacAddress'
_A2='ieee8021DdcfmDrRowStatus'
_A1='ieee8021DdcfmDrSFMsequenceErrors'
_A0='ieee8021DdcfmDrRemainDuration'
_z='ieee8021DdcfmDrActivationStatus'
_y='ieee8021DdcfmDrDuration'
_x='ieee8021DdcfmDrFloodingFlag'
_w='ieee8021DdcfmDrSfmOriginator'
_v='ieee8021DdcfmDrSourceAddressStayFlag'
_u='ieee8021DdcfmRFMRowStatus'
_t='ieee8021DdcfmRrRowStatus'
_s='ieee8021DdcfmRrNextRfmTransID'
_r='ieee8021DdcfmRrRemainDuration'
_q='ieee8021DdcfmRrActivationStatus'
_p='ieee8021DdcfmRrTruncationFlag'
_o='ieee8021DdcfmRrFloodingFlag'
_n='ieee8021DdcfmRrVlanDropEligible'
_m='ieee8021DdcfmRrVlanPriority'
_l='ieee8021DdcfmRrDurationInTimeFlag'
_k='ieee8021DdcfmRrDuration'
_j='ieee8021DdcfmRrContinueFlag'
_i='ieee8021DdcfmRrTargetAddress'
_h='ieee8021DdcfmRrSamplingInterval'
_g='ieee8021DdcfmRrFilter'
_f='ieee8021DdcfmRrPrimaryVlanIdOrNone'
_e='ieee8021DdcfmStackSFMOriginatorDirection'
_d='ieee8021DdcfmStackSFMOriginatorVlanIdOrNone'
_c='ieee8021DdcfmStackSFMOriginatorMdLevel'
_b='ieee8021DdcfmStackDrVlanIdOrNone'
_a='ieee8021DdcfmStackDrMdLevel'
_Z='ieee8021DdcfmStackRFMreceiverMdLevel'
_Y='ieee8021DdcfmStackRrDirection'
_X='ieee8021DdcfmStackRrMdLevel'
_W='ieee8021DdcfmSoDirection'
_V='ieee8021DdcfmSoVlanIdOrNone'
_U='ieee8021DdcfmSoMdIndex'
_T='ieee8021DdcfmSfmIfIndex'
_S='ieee8021DdcfmDrVlanIdOrNone'
_R='ieee8021DdcfmDrMdIndex'
_Q='ieee8021DdcfmDrIfIndex'
_P='ieee8021DdcfmRfmReceiverMdIndex'
_O='ieee8021DdcfmRfmReceiverIfIndex'
_N='ieee8021DdcfmRrDirection'
_M='ieee8021DdcfmRrMdIndex'
_L='ieee8021DdcfmRrIfIndex'
_K='ieee8021DdcfmStackIfIndex'
_J='Integer32'
_I='VlanIdOrNone'
_H='OctetString'
_G='seconds'
_F='TruthValue'
_E='not-accessible'
_D='read-only'
_C='read-create'
_B='IEEE8021-DDCFM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dot1agCfmMDLevel,Dot1agCfmMpDirection=mibBuilder.importSymbols('IEEE8021-CFM-MIB','Dot1agCfmMDLevel','Dot1agCfmMpDirection')
ieee802dot1mibs,=mibBuilder.importSymbols('IEEE8021-TC-MIB','ieee802dot1mibs')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanIdOrNone,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_F)
ieee8021DdcfmMIB=ModuleIdentity((1,3,111,2,802,1,1,11))
if mibBuilder.loadTexts:ieee8021DdcfmMIB.setRevisions(('2018-06-28 00:00','2014-12-15 00:00','2011-02-27 00:00','2009-04-06 00:00'))
_Ieee8021MIBObjects_ObjectIdentity=ObjectIdentity
ieee8021MIBObjects=_Ieee8021MIBObjects_ObjectIdentity((1,3,111,2,802,1,1,11,1))
_Ieee8021DdcfmStack_ObjectIdentity=ObjectIdentity
ieee8021DdcfmStack=_Ieee8021DdcfmStack_ObjectIdentity((1,3,111,2,802,1,1,11,1,1))
_Ieee8021DdcfmStackTable_Object=MibTable
ieee8021DdcfmStackTable=_Ieee8021DdcfmStackTable_Object((1,3,111,2,802,1,1,11,1,1,1))
if mibBuilder.loadTexts:ieee8021DdcfmStackTable.setStatus(_A)
_Ieee8021DdcfmStackEntry_Object=MibTableRow
ieee8021DdcfmStackEntry=_Ieee8021DdcfmStackEntry_Object((1,3,111,2,802,1,1,11,1,1,1,1))
ieee8021DdcfmStackEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:ieee8021DdcfmStackEntry.setStatus(_A)
_Ieee8021DdcfmStackIfIndex_Type=InterfaceIndex
_Ieee8021DdcfmStackIfIndex_Object=MibTableColumn
ieee8021DdcfmStackIfIndex=_Ieee8021DdcfmStackIfIndex_Object((1,3,111,2,802,1,1,11,1,1,1,1,1),_Ieee8021DdcfmStackIfIndex_Type())
ieee8021DdcfmStackIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021DdcfmStackIfIndex.setStatus(_A)
_Ieee8021DdcfmStackRrMdLevel_Type=Dot1agCfmMDLevel
_Ieee8021DdcfmStackRrMdLevel_Object=MibTableColumn
ieee8021DdcfmStackRrMdLevel=_Ieee8021DdcfmStackRrMdLevel_Object((1,3,111,2,802,1,1,11,1,1,1,1,2),_Ieee8021DdcfmStackRrMdLevel_Type())
ieee8021DdcfmStackRrMdLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021DdcfmStackRrMdLevel.setStatus(_A)
_Ieee8021DdcfmStackRrDirection_Type=Dot1agCfmMpDirection
_Ieee8021DdcfmStackRrDirection_Object=MibTableColumn
ieee8021DdcfmStackRrDirection=_Ieee8021DdcfmStackRrDirection_Object((1,3,111,2,802,1,1,11,1,1,1,1,3),_Ieee8021DdcfmStackRrDirection_Type())
ieee8021DdcfmStackRrDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021DdcfmStackRrDirection.setStatus(_A)
_Ieee8021DdcfmStackRFMreceiverMdLevel_Type=Dot1agCfmMDLevel
_Ieee8021DdcfmStackRFMreceiverMdLevel_Object=MibTableColumn
ieee8021DdcfmStackRFMreceiverMdLevel=_Ieee8021DdcfmStackRFMreceiverMdLevel_Object((1,3,111,2,802,1,1,11,1,1,1,1,4),_Ieee8021DdcfmStackRFMreceiverMdLevel_Type())
ieee8021DdcfmStackRFMreceiverMdLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021DdcfmStackRFMreceiverMdLevel.setStatus(_A)
_Ieee8021DdcfmStackDrMdLevel_Type=Dot1agCfmMDLevel
_Ieee8021DdcfmStackDrMdLevel_Object=MibTableColumn
ieee8021DdcfmStackDrMdLevel=_Ieee8021DdcfmStackDrMdLevel_Object((1,3,111,2,802,1,1,11,1,1,1,1,5),_Ieee8021DdcfmStackDrMdLevel_Type())
ieee8021DdcfmStackDrMdLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021DdcfmStackDrMdLevel.setStatus(_A)
_Ieee8021DdcfmStackDrVlanIdOrNone_Type=VlanIdOrNone
_Ieee8021DdcfmStackDrVlanIdOrNone_Object=MibTableColumn
ieee8021DdcfmStackDrVlanIdOrNone=_Ieee8021DdcfmStackDrVlanIdOrNone_Object((1,3,111,2,802,1,1,11,1,1,1,1,6),_Ieee8021DdcfmStackDrVlanIdOrNone_Type())
ieee8021DdcfmStackDrVlanIdOrNone.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021DdcfmStackDrVlanIdOrNone.setStatus(_A)
_Ieee8021DdcfmStackSFMOriginatorMdLevel_Type=Dot1agCfmMDLevel
_Ieee8021DdcfmStackSFMOriginatorMdLevel_Object=MibTableColumn
ieee8021DdcfmStackSFMOriginatorMdLevel=_Ieee8021DdcfmStackSFMOriginatorMdLevel_Object((1,3,111,2,802,1,1,11,1,1,1,1,7),_Ieee8021DdcfmStackSFMOriginatorMdLevel_Type())
ieee8021DdcfmStackSFMOriginatorMdLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021DdcfmStackSFMOriginatorMdLevel.setStatus(_A)
_Ieee8021DdcfmStackSFMOriginatorVlanIdOrNone_Type=VlanIdOrNone
_Ieee8021DdcfmStackSFMOriginatorVlanIdOrNone_Object=MibTableColumn
ieee8021DdcfmStackSFMOriginatorVlanIdOrNone=_Ieee8021DdcfmStackSFMOriginatorVlanIdOrNone_Object((1,3,111,2,802,1,1,11,1,1,1,1,8),_Ieee8021DdcfmStackSFMOriginatorVlanIdOrNone_Type())
ieee8021DdcfmStackSFMOriginatorVlanIdOrNone.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021DdcfmStackSFMOriginatorVlanIdOrNone.setStatus(_A)
_Ieee8021DdcfmStackSFMOriginatorDirection_Type=Dot1agCfmMpDirection
_Ieee8021DdcfmStackSFMOriginatorDirection_Object=MibTableColumn
ieee8021DdcfmStackSFMOriginatorDirection=_Ieee8021DdcfmStackSFMOriginatorDirection_Object((1,3,111,2,802,1,1,11,1,1,1,1,9),_Ieee8021DdcfmStackSFMOriginatorDirection_Type())
ieee8021DdcfmStackSFMOriginatorDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021DdcfmStackSFMOriginatorDirection.setStatus(_A)
_Ieee8021DdcfmRr_ObjectIdentity=ObjectIdentity
ieee8021DdcfmRr=_Ieee8021DdcfmRr_ObjectIdentity((1,3,111,2,802,1,1,11,1,2))
_Ieee8021DdcfmRrTable_Object=MibTable
ieee8021DdcfmRrTable=_Ieee8021DdcfmRrTable_Object((1,3,111,2,802,1,1,11,1,2,1))
if mibBuilder.loadTexts:ieee8021DdcfmRrTable.setStatus(_A)
_Ieee8021DdcfmRrEntry_Object=MibTableRow
ieee8021DdcfmRrEntry=_Ieee8021DdcfmRrEntry_Object((1,3,111,2,802,1,1,11,1,2,1,1))
ieee8021DdcfmRrEntry.setIndexNames((0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:ieee8021DdcfmRrEntry.setStatus(_A)
_Ieee8021DdcfmRrIfIndex_Type=InterfaceIndex
_Ieee8021DdcfmRrIfIndex_Object=MibTableColumn
ieee8021DdcfmRrIfIndex=_Ieee8021DdcfmRrIfIndex_Object((1,3,111,2,802,1,1,11,1,2,1,1,1),_Ieee8021DdcfmRrIfIndex_Type())
ieee8021DdcfmRrIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021DdcfmRrIfIndex.setStatus(_A)
_Ieee8021DdcfmRrMdIndex_Type=Dot1agCfmMDLevel
_Ieee8021DdcfmRrMdIndex_Object=MibTableColumn
ieee8021DdcfmRrMdIndex=_Ieee8021DdcfmRrMdIndex_Object((1,3,111,2,802,1,1,11,1,2,1,1,2),_Ieee8021DdcfmRrMdIndex_Type())
ieee8021DdcfmRrMdIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021DdcfmRrMdIndex.setStatus(_A)
_Ieee8021DdcfmRrDirection_Type=Dot1agCfmMpDirection
_Ieee8021DdcfmRrDirection_Object=MibTableColumn
ieee8021DdcfmRrDirection=_Ieee8021DdcfmRrDirection_Object((1,3,111,2,802,1,1,11,1,2,1,1,3),_Ieee8021DdcfmRrDirection_Type())
ieee8021DdcfmRrDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021DdcfmRrDirection.setStatus(_A)
class _Ieee8021DdcfmRrPrimaryVlanIdOrNone_Type(VlanIdOrNone):defaultValue=0
_Ieee8021DdcfmRrPrimaryVlanIdOrNone_Type.__name__=_I
_Ieee8021DdcfmRrPrimaryVlanIdOrNone_Object=MibTableColumn
ieee8021DdcfmRrPrimaryVlanIdOrNone=_Ieee8021DdcfmRrPrimaryVlanIdOrNone_Object((1,3,111,2,802,1,1,11,1,2,1,1,4),_Ieee8021DdcfmRrPrimaryVlanIdOrNone_Type())
ieee8021DdcfmRrPrimaryVlanIdOrNone.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmRrPrimaryVlanIdOrNone.setStatus(_A)
class _Ieee8021DdcfmRrFilter_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1500))
_Ieee8021DdcfmRrFilter_Type.__name__=_H
_Ieee8021DdcfmRrFilter_Object=MibTableColumn
ieee8021DdcfmRrFilter=_Ieee8021DdcfmRrFilter_Object((1,3,111,2,802,1,1,11,1,2,1,1,5),_Ieee8021DdcfmRrFilter_Type())
ieee8021DdcfmRrFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmRrFilter.setStatus(_A)
_Ieee8021DdcfmRrSamplingInterval_Type=Unsigned32
_Ieee8021DdcfmRrSamplingInterval_Object=MibTableColumn
ieee8021DdcfmRrSamplingInterval=_Ieee8021DdcfmRrSamplingInterval_Object((1,3,111,2,802,1,1,11,1,2,1,1,6),_Ieee8021DdcfmRrSamplingInterval_Type())
ieee8021DdcfmRrSamplingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmRrSamplingInterval.setStatus(_A)
if mibBuilder.loadTexts:ieee8021DdcfmRrSamplingInterval.setUnits('miliseconds')
_Ieee8021DdcfmRrTargetAddress_Type=MacAddress
_Ieee8021DdcfmRrTargetAddress_Object=MibTableColumn
ieee8021DdcfmRrTargetAddress=_Ieee8021DdcfmRrTargetAddress_Object((1,3,111,2,802,1,1,11,1,2,1,1,7),_Ieee8021DdcfmRrTargetAddress_Type())
ieee8021DdcfmRrTargetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmRrTargetAddress.setStatus(_A)
class _Ieee8021DdcfmRrContinueFlag_Type(TruthValue):defaultValue=1
_Ieee8021DdcfmRrContinueFlag_Type.__name__=_F
_Ieee8021DdcfmRrContinueFlag_Object=MibTableColumn
ieee8021DdcfmRrContinueFlag=_Ieee8021DdcfmRrContinueFlag_Object((1,3,111,2,802,1,1,11,1,2,1,1,8),_Ieee8021DdcfmRrContinueFlag_Type())
ieee8021DdcfmRrContinueFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmRrContinueFlag.setStatus(_A)
_Ieee8021DdcfmRrDuration_Type=Unsigned32
_Ieee8021DdcfmRrDuration_Object=MibTableColumn
ieee8021DdcfmRrDuration=_Ieee8021DdcfmRrDuration_Object((1,3,111,2,802,1,1,11,1,2,1,1,9),_Ieee8021DdcfmRrDuration_Type())
ieee8021DdcfmRrDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmRrDuration.setStatus(_A)
class _Ieee8021DdcfmRrDurationInTimeFlag_Type(TruthValue):defaultValue=1
_Ieee8021DdcfmRrDurationInTimeFlag_Type.__name__=_F
_Ieee8021DdcfmRrDurationInTimeFlag_Object=MibTableColumn
ieee8021DdcfmRrDurationInTimeFlag=_Ieee8021DdcfmRrDurationInTimeFlag_Object((1,3,111,2,802,1,1,11,1,2,1,1,10),_Ieee8021DdcfmRrDurationInTimeFlag_Type())
ieee8021DdcfmRrDurationInTimeFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmRrDurationInTimeFlag.setStatus(_A)
class _Ieee8021DdcfmRrVlanPriority_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Ieee8021DdcfmRrVlanPriority_Type.__name__=_J
_Ieee8021DdcfmRrVlanPriority_Object=MibTableColumn
ieee8021DdcfmRrVlanPriority=_Ieee8021DdcfmRrVlanPriority_Object((1,3,111,2,802,1,1,11,1,2,1,1,11),_Ieee8021DdcfmRrVlanPriority_Type())
ieee8021DdcfmRrVlanPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmRrVlanPriority.setStatus(_A)
class _Ieee8021DdcfmRrVlanDropEligible_Type(TruthValue):defaultValue=2
_Ieee8021DdcfmRrVlanDropEligible_Type.__name__=_F
_Ieee8021DdcfmRrVlanDropEligible_Object=MibTableColumn
ieee8021DdcfmRrVlanDropEligible=_Ieee8021DdcfmRrVlanDropEligible_Object((1,3,111,2,802,1,1,11,1,2,1,1,12),_Ieee8021DdcfmRrVlanDropEligible_Type())
ieee8021DdcfmRrVlanDropEligible.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmRrVlanDropEligible.setStatus(_A)
class _Ieee8021DdcfmRrFloodingFlag_Type(TruthValue):defaultValue=1
_Ieee8021DdcfmRrFloodingFlag_Type.__name__=_F
_Ieee8021DdcfmRrFloodingFlag_Object=MibTableColumn
ieee8021DdcfmRrFloodingFlag=_Ieee8021DdcfmRrFloodingFlag_Object((1,3,111,2,802,1,1,11,1,2,1,1,13),_Ieee8021DdcfmRrFloodingFlag_Type())
ieee8021DdcfmRrFloodingFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmRrFloodingFlag.setStatus(_A)
class _Ieee8021DdcfmRrTruncationFlag_Type(TruthValue):defaultValue=1
_Ieee8021DdcfmRrTruncationFlag_Type.__name__=_F
_Ieee8021DdcfmRrTruncationFlag_Object=MibTableColumn
ieee8021DdcfmRrTruncationFlag=_Ieee8021DdcfmRrTruncationFlag_Object((1,3,111,2,802,1,1,11,1,2,1,1,14),_Ieee8021DdcfmRrTruncationFlag_Type())
ieee8021DdcfmRrTruncationFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmRrTruncationFlag.setStatus(_A)
class _Ieee8021DdcfmRrActivationStatus_Type(TruthValue):defaultValue=2
_Ieee8021DdcfmRrActivationStatus_Type.__name__=_F
_Ieee8021DdcfmRrActivationStatus_Object=MibTableColumn
ieee8021DdcfmRrActivationStatus=_Ieee8021DdcfmRrActivationStatus_Object((1,3,111,2,802,1,1,11,1,2,1,1,15),_Ieee8021DdcfmRrActivationStatus_Type())
ieee8021DdcfmRrActivationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021DdcfmRrActivationStatus.setStatus(_A)
_Ieee8021DdcfmRrRemainDuration_Type=Unsigned32
_Ieee8021DdcfmRrRemainDuration_Object=MibTableColumn
ieee8021DdcfmRrRemainDuration=_Ieee8021DdcfmRrRemainDuration_Object((1,3,111,2,802,1,1,11,1,2,1,1,16),_Ieee8021DdcfmRrRemainDuration_Type())
ieee8021DdcfmRrRemainDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021DdcfmRrRemainDuration.setStatus(_A)
if mibBuilder.loadTexts:ieee8021DdcfmRrRemainDuration.setUnits(_G)
_Ieee8021DdcfmRrNextRfmTransID_Type=Unsigned32
_Ieee8021DdcfmRrNextRfmTransID_Object=MibTableColumn
ieee8021DdcfmRrNextRfmTransID=_Ieee8021DdcfmRrNextRfmTransID_Object((1,3,111,2,802,1,1,11,1,2,1,1,17),_Ieee8021DdcfmRrNextRfmTransID_Type())
ieee8021DdcfmRrNextRfmTransID.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021DdcfmRrNextRfmTransID.setStatus(_A)
_Ieee8021DdcfmRrRowStatus_Type=RowStatus
_Ieee8021DdcfmRrRowStatus_Object=MibTableColumn
ieee8021DdcfmRrRowStatus=_Ieee8021DdcfmRrRowStatus_Object((1,3,111,2,802,1,1,11,1,2,1,1,18),_Ieee8021DdcfmRrRowStatus_Type())
ieee8021DdcfmRrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmRrRowStatus.setStatus(_A)
_Ieee8021DdcfmRFMReceiver_ObjectIdentity=ObjectIdentity
ieee8021DdcfmRFMReceiver=_Ieee8021DdcfmRFMReceiver_ObjectIdentity((1,3,111,2,802,1,1,11,1,3))
_Ieee8021DdcfmRFMReceiverTable_Object=MibTable
ieee8021DdcfmRFMReceiverTable=_Ieee8021DdcfmRFMReceiverTable_Object((1,3,111,2,802,1,1,11,1,3,1))
if mibBuilder.loadTexts:ieee8021DdcfmRFMReceiverTable.setStatus(_A)
_Ieee8021DdcfmRFMReceiverEntry_Object=MibTableRow
ieee8021DdcfmRFMReceiverEntry=_Ieee8021DdcfmRFMReceiverEntry_Object((1,3,111,2,802,1,1,11,1,3,1,1))
ieee8021DdcfmRFMReceiverEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:ieee8021DdcfmRFMReceiverEntry.setStatus(_A)
_Ieee8021DdcfmRfmReceiverIfIndex_Type=InterfaceIndex
_Ieee8021DdcfmRfmReceiverIfIndex_Object=MibTableColumn
ieee8021DdcfmRfmReceiverIfIndex=_Ieee8021DdcfmRfmReceiverIfIndex_Object((1,3,111,2,802,1,1,11,1,3,1,1,1),_Ieee8021DdcfmRfmReceiverIfIndex_Type())
ieee8021DdcfmRfmReceiverIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021DdcfmRfmReceiverIfIndex.setStatus(_A)
_Ieee8021DdcfmRfmReceiverMdIndex_Type=Dot1agCfmMDLevel
_Ieee8021DdcfmRfmReceiverMdIndex_Object=MibTableColumn
ieee8021DdcfmRfmReceiverMdIndex=_Ieee8021DdcfmRfmReceiverMdIndex_Object((1,3,111,2,802,1,1,11,1,3,1,1,2),_Ieee8021DdcfmRfmReceiverMdIndex_Type())
ieee8021DdcfmRfmReceiverMdIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021DdcfmRfmReceiverMdIndex.setStatus(_A)
_Ieee8021DdcfmRFMRowStatus_Type=RowStatus
_Ieee8021DdcfmRFMRowStatus_Object=MibTableColumn
ieee8021DdcfmRFMRowStatus=_Ieee8021DdcfmRFMRowStatus_Object((1,3,111,2,802,1,1,11,1,3,1,1,3),_Ieee8021DdcfmRFMRowStatus_Type())
ieee8021DdcfmRFMRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmRFMRowStatus.setStatus(_A)
_Ieee8021DdcfmDr_ObjectIdentity=ObjectIdentity
ieee8021DdcfmDr=_Ieee8021DdcfmDr_ObjectIdentity((1,3,111,2,802,1,1,11,1,4))
_Ieee8021DdcfmDrTable_Object=MibTable
ieee8021DdcfmDrTable=_Ieee8021DdcfmDrTable_Object((1,3,111,2,802,1,1,11,1,4,1))
if mibBuilder.loadTexts:ieee8021DdcfmDrTable.setStatus(_A)
_Ieee8021DdcfmDrEntry_Object=MibTableRow
ieee8021DdcfmDrEntry=_Ieee8021DdcfmDrEntry_Object((1,3,111,2,802,1,1,11,1,4,1,1))
ieee8021DdcfmDrEntry.setIndexNames((0,_B,_Q),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:ieee8021DdcfmDrEntry.setStatus(_A)
_Ieee8021DdcfmDrIfIndex_Type=InterfaceIndex
_Ieee8021DdcfmDrIfIndex_Object=MibTableColumn
ieee8021DdcfmDrIfIndex=_Ieee8021DdcfmDrIfIndex_Object((1,3,111,2,802,1,1,11,1,4,1,1,1),_Ieee8021DdcfmDrIfIndex_Type())
ieee8021DdcfmDrIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021DdcfmDrIfIndex.setStatus(_A)
_Ieee8021DdcfmDrMdIndex_Type=Dot1agCfmMDLevel
_Ieee8021DdcfmDrMdIndex_Object=MibTableColumn
ieee8021DdcfmDrMdIndex=_Ieee8021DdcfmDrMdIndex_Object((1,3,111,2,802,1,1,11,1,4,1,1,2),_Ieee8021DdcfmDrMdIndex_Type())
ieee8021DdcfmDrMdIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021DdcfmDrMdIndex.setStatus(_A)
_Ieee8021DdcfmDrVlanIdOrNone_Type=VlanIdOrNone
_Ieee8021DdcfmDrVlanIdOrNone_Object=MibTableColumn
ieee8021DdcfmDrVlanIdOrNone=_Ieee8021DdcfmDrVlanIdOrNone_Object((1,3,111,2,802,1,1,11,1,4,1,1,3),_Ieee8021DdcfmDrVlanIdOrNone_Type())
ieee8021DdcfmDrVlanIdOrNone.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021DdcfmDrVlanIdOrNone.setStatus(_A)
_Ieee8021DdcfmDrSfmOriginator_Type=MacAddress
_Ieee8021DdcfmDrSfmOriginator_Object=MibTableColumn
ieee8021DdcfmDrSfmOriginator=_Ieee8021DdcfmDrSfmOriginator_Object((1,3,111,2,802,1,1,11,1,4,1,1,4),_Ieee8021DdcfmDrSfmOriginator_Type())
ieee8021DdcfmDrSfmOriginator.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmDrSfmOriginator.setStatus(_A)
class _Ieee8021DdcfmDrSourceAddressStayFlag_Type(TruthValue):defaultValue=1
_Ieee8021DdcfmDrSourceAddressStayFlag_Type.__name__=_F
_Ieee8021DdcfmDrSourceAddressStayFlag_Object=MibTableColumn
ieee8021DdcfmDrSourceAddressStayFlag=_Ieee8021DdcfmDrSourceAddressStayFlag_Object((1,3,111,2,802,1,1,11,1,4,1,1,5),_Ieee8021DdcfmDrSourceAddressStayFlag_Type())
ieee8021DdcfmDrSourceAddressStayFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmDrSourceAddressStayFlag.setStatus(_A)
class _Ieee8021DdcfmDrFloodingFlag_Type(TruthValue):defaultValue=1
_Ieee8021DdcfmDrFloodingFlag_Type.__name__=_F
_Ieee8021DdcfmDrFloodingFlag_Object=MibTableColumn
ieee8021DdcfmDrFloodingFlag=_Ieee8021DdcfmDrFloodingFlag_Object((1,3,111,2,802,1,1,11,1,4,1,1,6),_Ieee8021DdcfmDrFloodingFlag_Type())
ieee8021DdcfmDrFloodingFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmDrFloodingFlag.setStatus(_A)
_Ieee8021DdcfmDrDuration_Type=Unsigned32
_Ieee8021DdcfmDrDuration_Object=MibTableColumn
ieee8021DdcfmDrDuration=_Ieee8021DdcfmDrDuration_Object((1,3,111,2,802,1,1,11,1,4,1,1,7),_Ieee8021DdcfmDrDuration_Type())
ieee8021DdcfmDrDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmDrDuration.setStatus(_A)
if mibBuilder.loadTexts:ieee8021DdcfmDrDuration.setUnits(_G)
class _Ieee8021DdcfmDrActivationStatus_Type(TruthValue):defaultValue=2
_Ieee8021DdcfmDrActivationStatus_Type.__name__=_F
_Ieee8021DdcfmDrActivationStatus_Object=MibTableColumn
ieee8021DdcfmDrActivationStatus=_Ieee8021DdcfmDrActivationStatus_Object((1,3,111,2,802,1,1,11,1,4,1,1,8),_Ieee8021DdcfmDrActivationStatus_Type())
ieee8021DdcfmDrActivationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021DdcfmDrActivationStatus.setStatus(_A)
_Ieee8021DdcfmDrRemainDuration_Type=Unsigned32
_Ieee8021DdcfmDrRemainDuration_Object=MibTableColumn
ieee8021DdcfmDrRemainDuration=_Ieee8021DdcfmDrRemainDuration_Object((1,3,111,2,802,1,1,11,1,4,1,1,9),_Ieee8021DdcfmDrRemainDuration_Type())
ieee8021DdcfmDrRemainDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021DdcfmDrRemainDuration.setStatus(_A)
if mibBuilder.loadTexts:ieee8021DdcfmDrRemainDuration.setUnits(_G)
_Ieee8021DdcfmDrSFMsequenceErrors_Type=Unsigned32
_Ieee8021DdcfmDrSFMsequenceErrors_Object=MibTableColumn
ieee8021DdcfmDrSFMsequenceErrors=_Ieee8021DdcfmDrSFMsequenceErrors_Object((1,3,111,2,802,1,1,11,1,4,1,1,10),_Ieee8021DdcfmDrSFMsequenceErrors_Type())
ieee8021DdcfmDrSFMsequenceErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021DdcfmDrSFMsequenceErrors.setStatus(_A)
if mibBuilder.loadTexts:ieee8021DdcfmDrSFMsequenceErrors.setUnits('integer')
_Ieee8021DdcfmDrRowStatus_Type=RowStatus
_Ieee8021DdcfmDrRowStatus_Object=MibTableColumn
ieee8021DdcfmDrRowStatus=_Ieee8021DdcfmDrRowStatus_Object((1,3,111,2,802,1,1,11,1,4,1,1,11),_Ieee8021DdcfmDrRowStatus_Type())
ieee8021DdcfmDrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmDrRowStatus.setStatus(_A)
_Ieee8021DdcfmSFMOriginator_ObjectIdentity=ObjectIdentity
ieee8021DdcfmSFMOriginator=_Ieee8021DdcfmSFMOriginator_ObjectIdentity((1,3,111,2,802,1,1,11,1,5))
_Ieee8021DdcfmSoTable_Object=MibTable
ieee8021DdcfmSoTable=_Ieee8021DdcfmSoTable_Object((1,3,111,2,802,1,1,11,1,5,1))
if mibBuilder.loadTexts:ieee8021DdcfmSoTable.setStatus(_A)
_Ieee8021DdcfmSoEntry_Object=MibTableRow
ieee8021DdcfmSoEntry=_Ieee8021DdcfmSoEntry_Object((1,3,111,2,802,1,1,11,1,5,1,1))
ieee8021DdcfmSoEntry.setIndexNames((0,_B,_T),(0,_B,_U),(0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:ieee8021DdcfmSoEntry.setStatus(_A)
_Ieee8021DdcfmSfmIfIndex_Type=InterfaceIndex
_Ieee8021DdcfmSfmIfIndex_Object=MibTableColumn
ieee8021DdcfmSfmIfIndex=_Ieee8021DdcfmSfmIfIndex_Object((1,3,111,2,802,1,1,11,1,5,1,1,1),_Ieee8021DdcfmSfmIfIndex_Type())
ieee8021DdcfmSfmIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021DdcfmSfmIfIndex.setStatus(_A)
_Ieee8021DdcfmSoMdIndex_Type=Dot1agCfmMDLevel
_Ieee8021DdcfmSoMdIndex_Object=MibTableColumn
ieee8021DdcfmSoMdIndex=_Ieee8021DdcfmSoMdIndex_Object((1,3,111,2,802,1,1,11,1,5,1,1,2),_Ieee8021DdcfmSoMdIndex_Type())
ieee8021DdcfmSoMdIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021DdcfmSoMdIndex.setStatus(_A)
_Ieee8021DdcfmSoVlanIdOrNone_Type=VlanIdOrNone
_Ieee8021DdcfmSoVlanIdOrNone_Object=MibTableColumn
ieee8021DdcfmSoVlanIdOrNone=_Ieee8021DdcfmSoVlanIdOrNone_Object((1,3,111,2,802,1,1,11,1,5,1,1,3),_Ieee8021DdcfmSoVlanIdOrNone_Type())
ieee8021DdcfmSoVlanIdOrNone.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021DdcfmSoVlanIdOrNone.setStatus(_A)
_Ieee8021DdcfmSoDirection_Type=Dot1agCfmMpDirection
_Ieee8021DdcfmSoDirection_Object=MibTableColumn
ieee8021DdcfmSoDirection=_Ieee8021DdcfmSoDirection_Object((1,3,111,2,802,1,1,11,1,5,1,1,4),_Ieee8021DdcfmSoDirection_Type())
ieee8021DdcfmSoDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021DdcfmSoDirection.setStatus(_A)
_Ieee8021DdcfmSoDrMacAddress_Type=MacAddress
_Ieee8021DdcfmSoDrMacAddress_Object=MibTableColumn
ieee8021DdcfmSoDrMacAddress=_Ieee8021DdcfmSoDrMacAddress_Object((1,3,111,2,802,1,1,11,1,5,1,1,5),_Ieee8021DdcfmSoDrMacAddress_Type())
ieee8021DdcfmSoDrMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmSoDrMacAddress.setStatus(_A)
_Ieee8021DdcfmSoDuration_Type=Unsigned32
_Ieee8021DdcfmSoDuration_Object=MibTableColumn
ieee8021DdcfmSoDuration=_Ieee8021DdcfmSoDuration_Object((1,3,111,2,802,1,1,11,1,5,1,1,6),_Ieee8021DdcfmSoDuration_Type())
ieee8021DdcfmSoDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmSoDuration.setStatus(_A)
if mibBuilder.loadTexts:ieee8021DdcfmSoDuration.setUnits(_G)
class _Ieee8021DdcfmSoActivationStatus_Type(TruthValue):defaultValue=2
_Ieee8021DdcfmSoActivationStatus_Type.__name__=_F
_Ieee8021DdcfmSoActivationStatus_Object=MibTableColumn
ieee8021DdcfmSoActivationStatus=_Ieee8021DdcfmSoActivationStatus_Object((1,3,111,2,802,1,1,11,1,5,1,1,7),_Ieee8021DdcfmSoActivationStatus_Type())
ieee8021DdcfmSoActivationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021DdcfmSoActivationStatus.setStatus(_A)
_Ieee8021DdcfmSoRemainDuration_Type=Unsigned32
_Ieee8021DdcfmSoRemainDuration_Object=MibTableColumn
ieee8021DdcfmSoRemainDuration=_Ieee8021DdcfmSoRemainDuration_Object((1,3,111,2,802,1,1,11,1,5,1,1,8),_Ieee8021DdcfmSoRemainDuration_Type())
ieee8021DdcfmSoRemainDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021DdcfmSoRemainDuration.setStatus(_A)
if mibBuilder.loadTexts:ieee8021DdcfmSoRemainDuration.setUnits(_G)
_Ieee8021DdcfmSoRowStatus_Type=RowStatus
_Ieee8021DdcfmSoRowStatus_Object=MibTableColumn
ieee8021DdcfmSoRowStatus=_Ieee8021DdcfmSoRowStatus_Object((1,3,111,2,802,1,1,11,1,5,1,1,9),_Ieee8021DdcfmSoRowStatus_Type())
ieee8021DdcfmSoRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021DdcfmSoRowStatus.setStatus(_A)
_Ieee8021DdcfmConformance_ObjectIdentity=ObjectIdentity
ieee8021DdcfmConformance=_Ieee8021DdcfmConformance_ObjectIdentity((1,3,111,2,802,1,1,11,2))
_Ieee8021DdcfmCompliances_ObjectIdentity=ObjectIdentity
ieee8021DdcfmCompliances=_Ieee8021DdcfmCompliances_ObjectIdentity((1,3,111,2,802,1,1,11,2,1))
_Ieee8021DdcfmGroups_ObjectIdentity=ObjectIdentity
ieee8021DdcfmGroups=_Ieee8021DdcfmGroups_ObjectIdentity((1,3,111,2,802,1,1,11,2,2))
ieee8021DdcfmStackGroup=ObjectGroup((1,3,111,2,802,1,1,11,2,2,1))
ieee8021DdcfmStackGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:ieee8021DdcfmStackGroup.setStatus(_A)
ieee8021DdcfmRrGroup=ObjectGroup((1,3,111,2,802,1,1,11,2,2,2))
ieee8021DdcfmRrGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:ieee8021DdcfmRrGroup.setStatus(_A)
ieee8021DdcfmRFMReceiverGroup=ObjectGroup((1,3,111,2,802,1,1,11,2,2,3))
ieee8021DdcfmRFMReceiverGroup.setObjects((_B,_u))
if mibBuilder.loadTexts:ieee8021DdcfmRFMReceiverGroup.setStatus(_A)
ieee8021DdcfmDrGroup=ObjectGroup((1,3,111,2,802,1,1,11,2,2,4))
ieee8021DdcfmDrGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:ieee8021DdcfmDrGroup.setStatus(_A)
ieee8021DdcfmSoGroup=ObjectGroup((1,3,111,2,802,1,1,11,2,2,5))
ieee8021DdcfmSoGroup.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:ieee8021DdcfmSoGroup.setStatus(_A)
ieee8021DdcfmCompliance=ModuleCompliance((1,3,111,2,802,1,1,11,2,1,1))
ieee8021DdcfmCompliance.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:ieee8021DdcfmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ieee8021DdcfmMIB':ieee8021DdcfmMIB,'ieee8021MIBObjects':ieee8021MIBObjects,'ieee8021DdcfmStack':ieee8021DdcfmStack,'ieee8021DdcfmStackTable':ieee8021DdcfmStackTable,'ieee8021DdcfmStackEntry':ieee8021DdcfmStackEntry,_K:ieee8021DdcfmStackIfIndex,_X:ieee8021DdcfmStackRrMdLevel,_Y:ieee8021DdcfmStackRrDirection,_Z:ieee8021DdcfmStackRFMreceiverMdLevel,_a:ieee8021DdcfmStackDrMdLevel,_b:ieee8021DdcfmStackDrVlanIdOrNone,_c:ieee8021DdcfmStackSFMOriginatorMdLevel,_d:ieee8021DdcfmStackSFMOriginatorVlanIdOrNone,_e:ieee8021DdcfmStackSFMOriginatorDirection,'ieee8021DdcfmRr':ieee8021DdcfmRr,'ieee8021DdcfmRrTable':ieee8021DdcfmRrTable,'ieee8021DdcfmRrEntry':ieee8021DdcfmRrEntry,_L:ieee8021DdcfmRrIfIndex,_M:ieee8021DdcfmRrMdIndex,_N:ieee8021DdcfmRrDirection,_f:ieee8021DdcfmRrPrimaryVlanIdOrNone,_g:ieee8021DdcfmRrFilter,_h:ieee8021DdcfmRrSamplingInterval,_i:ieee8021DdcfmRrTargetAddress,_j:ieee8021DdcfmRrContinueFlag,_k:ieee8021DdcfmRrDuration,_l:ieee8021DdcfmRrDurationInTimeFlag,_m:ieee8021DdcfmRrVlanPriority,_n:ieee8021DdcfmRrVlanDropEligible,_o:ieee8021DdcfmRrFloodingFlag,_p:ieee8021DdcfmRrTruncationFlag,_q:ieee8021DdcfmRrActivationStatus,_r:ieee8021DdcfmRrRemainDuration,_s:ieee8021DdcfmRrNextRfmTransID,_t:ieee8021DdcfmRrRowStatus,'ieee8021DdcfmRFMReceiver':ieee8021DdcfmRFMReceiver,'ieee8021DdcfmRFMReceiverTable':ieee8021DdcfmRFMReceiverTable,'ieee8021DdcfmRFMReceiverEntry':ieee8021DdcfmRFMReceiverEntry,_O:ieee8021DdcfmRfmReceiverIfIndex,_P:ieee8021DdcfmRfmReceiverMdIndex,_u:ieee8021DdcfmRFMRowStatus,'ieee8021DdcfmDr':ieee8021DdcfmDr,'ieee8021DdcfmDrTable':ieee8021DdcfmDrTable,'ieee8021DdcfmDrEntry':ieee8021DdcfmDrEntry,_Q:ieee8021DdcfmDrIfIndex,_R:ieee8021DdcfmDrMdIndex,_S:ieee8021DdcfmDrVlanIdOrNone,_w:ieee8021DdcfmDrSfmOriginator,_v:ieee8021DdcfmDrSourceAddressStayFlag,_x:ieee8021DdcfmDrFloodingFlag,_y:ieee8021DdcfmDrDuration,_z:ieee8021DdcfmDrActivationStatus,_A0:ieee8021DdcfmDrRemainDuration,_A1:ieee8021DdcfmDrSFMsequenceErrors,_A2:ieee8021DdcfmDrRowStatus,'ieee8021DdcfmSFMOriginator':ieee8021DdcfmSFMOriginator,'ieee8021DdcfmSoTable':ieee8021DdcfmSoTable,'ieee8021DdcfmSoEntry':ieee8021DdcfmSoEntry,_T:ieee8021DdcfmSfmIfIndex,_U:ieee8021DdcfmSoMdIndex,_V:ieee8021DdcfmSoVlanIdOrNone,_W:ieee8021DdcfmSoDirection,_A3:ieee8021DdcfmSoDrMacAddress,_A4:ieee8021DdcfmSoDuration,_A5:ieee8021DdcfmSoActivationStatus,_A6:ieee8021DdcfmSoRemainDuration,_A7:ieee8021DdcfmSoRowStatus,'ieee8021DdcfmConformance':ieee8021DdcfmConformance,'ieee8021DdcfmCompliances':ieee8021DdcfmCompliances,'ieee8021DdcfmCompliance':ieee8021DdcfmCompliance,'ieee8021DdcfmGroups':ieee8021DdcfmGroups,_A8:ieee8021DdcfmStackGroup,_A9:ieee8021DdcfmRrGroup,_AA:ieee8021DdcfmRFMReceiverGroup,_AB:ieee8021DdcfmDrGroup,_AC:ieee8021DdcfmSoGroup})