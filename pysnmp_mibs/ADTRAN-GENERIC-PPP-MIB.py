_p='adGenPppGroupDayIntervalNumber'
_o='adGenPppGroupIntervalNumber'
_n='mismatch'
_m='verified'
_l='unverified'
_k='adGenPppLinkDayIntervalNumber'
_j='adGenPppLinkIntervalNumber'
_i='DisplayString'
_h='acksent'
_g='ackrcvd'
_f='reqsent'
_e='stopping'
_d='closing'
_c='stopped'
_b='closed'
_a='starting'
_Z='initial'
_Y='not-accessible'
_X='reset'
_W='opened'
_V='ADTRAN-GENERIC-PPP-MIB'
_U='critical'
_T='major'
_S='minor'
_R='alert'
_Q='info'
_P='OctetString'
_O='sysName'
_N='SNMPv2-MIB'
_M='adTAeSCUTrapAlarmLevel'
_L='ADTRAN-TAeSCUEXT1-MIB'
_K='adTrapInformSeqNum'
_J='ADTRAN-GENTRAPINFORM-MIB'
_I='TruthValue'
_H='adGenSlotInfoIndex'
_G='ADTRAN-GENSLOT-MIB'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPortTrapIdentifier,=mibBuilder.importSymbols('ADTRAN-GENPORT-MIB','adGenPortTrapIdentifier')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_G,_H)
adGenPpp,adGenPppID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adGenPpp','adGenPppID')
adTrapInformSeqNum,=mibBuilder.importSymbols(_J,_K)
adTAeSCUTrapAlarmLevel,=mibBuilder.importSymbols(_L,_M)
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_E,'InterfaceIndex',_F)
InetAddressIPv6,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_N,_O)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_i,'PhysAddress','RowStatus','TextualConvention',_I)
adGenPppMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,31,1))
_AdGenPppMIBObjects_ObjectIdentity=ObjectIdentity
adGenPppMIBObjects=_AdGenPppMIBObjects_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,31,1))
_AdGenPppLinkObjects_ObjectIdentity=ObjectIdentity
adGenPppLinkObjects=_AdGenPppLinkObjects_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,31,1,1))
_AdGenPppLinkProv_ObjectIdentity=ObjectIdentity
adGenPppLinkProv=_AdGenPppLinkProv_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,31,1,1,1))
_AdGenPppLinkAlarmProvTable_Object=MibTable
adGenPppLinkAlarmProvTable=_AdGenPppLinkAlarmProvTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,1,1))
if mibBuilder.loadTexts:adGenPppLinkAlarmProvTable.setStatus(_A)
_AdGenPppLinkAlarmProvEntry_Object=MibTableRow
adGenPppLinkAlarmProvEntry=_AdGenPppLinkAlarmProvEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,1,1,1))
adGenPppLinkAlarmProvEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:adGenPppLinkAlarmProvEntry.setStatus(_A)
class _AdGenPppLinkAlarmProvLCPAlarmSeverity_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*((_Q,2),(_R,3),(_S,4),(_T,5),(_U,6)))
_AdGenPppLinkAlarmProvLCPAlarmSeverity_Type.__name__=_D
_AdGenPppLinkAlarmProvLCPAlarmSeverity_Object=MibTableColumn
adGenPppLinkAlarmProvLCPAlarmSeverity=_AdGenPppLinkAlarmProvLCPAlarmSeverity_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,1,1,1,1),_AdGenPppLinkAlarmProvLCPAlarmSeverity_Type())
adGenPppLinkAlarmProvLCPAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppLinkAlarmProvLCPAlarmSeverity.setStatus(_A)
class _AdGenPppLinkAlarmProvLCPAlarmSuppression_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AdGenPppLinkAlarmProvLCPAlarmSuppression_Type.__name__=_D
_AdGenPppLinkAlarmProvLCPAlarmSuppression_Object=MibTableColumn
adGenPppLinkAlarmProvLCPAlarmSuppression=_AdGenPppLinkAlarmProvLCPAlarmSuppression_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,1,1,1,2),_AdGenPppLinkAlarmProvLCPAlarmSuppression_Type())
adGenPppLinkAlarmProvLCPAlarmSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppLinkAlarmProvLCPAlarmSuppression.setStatus(_A)
class _AdGenPppLinkAlarmProvLCPAlarmEnable_Type(TruthValue):defaultValue=1
_AdGenPppLinkAlarmProvLCPAlarmEnable_Type.__name__=_I
_AdGenPppLinkAlarmProvLCPAlarmEnable_Object=MibTableColumn
adGenPppLinkAlarmProvLCPAlarmEnable=_AdGenPppLinkAlarmProvLCPAlarmEnable_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,1,1,1,3),_AdGenPppLinkAlarmProvLCPAlarmEnable_Type())
adGenPppLinkAlarmProvLCPAlarmEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppLinkAlarmProvLCPAlarmEnable.setStatus(_A)
_AdGenPppLinkStatus_ObjectIdentity=ObjectIdentity
adGenPppLinkStatus=_AdGenPppLinkStatus_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,31,1,1,2))
_AdGenPppLinkStatusTable_Object=MibTable
adGenPppLinkStatusTable=_AdGenPppLinkStatusTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,2,1))
if mibBuilder.loadTexts:adGenPppLinkStatusTable.setStatus(_A)
_AdGenPppLinkStatusEntry_Object=MibTableRow
adGenPppLinkStatusEntry=_AdGenPppLinkStatusEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,2,1,1))
adGenPppLinkStatusEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenPppLinkStatusEntry.setStatus(_A)
class _AdGenPppLinkOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),('notopened',2)))
_AdGenPppLinkOperStatus_Type.__name__=_D
_AdGenPppLinkOperStatus_Object=MibTableColumn
adGenPppLinkOperStatus=_AdGenPppLinkOperStatus_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,2,1,1,1),_AdGenPppLinkOperStatus_Type())
adGenPppLinkOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkOperStatus.setStatus(_A)
class _AdGenPppLinkCurrentLCPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3),(_c,4),(_d,5),(_e,6),(_f,7),(_g,8),(_h,9),(_W,10)))
_AdGenPppLinkCurrentLCPState_Type.__name__=_D
_AdGenPppLinkCurrentLCPState_Object=MibTableColumn
adGenPppLinkCurrentLCPState=_AdGenPppLinkCurrentLCPState_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,2,1,1,2),_AdGenPppLinkCurrentLCPState_Type())
adGenPppLinkCurrentLCPState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkCurrentLCPState.setStatus(_A)
_AdGenPppLinkNegotiatedStatus_Type=DisplayString
_AdGenPppLinkNegotiatedStatus_Object=MibTableColumn
adGenPppLinkNegotiatedStatus=_AdGenPppLinkNegotiatedStatus_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,2,1,1,3),_AdGenPppLinkNegotiatedStatus_Type())
adGenPppLinkNegotiatedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkNegotiatedStatus.setStatus(_A)
_AdGenPppLinkPerfStats_ObjectIdentity=ObjectIdentity
adGenPppLinkPerfStats=_AdGenPppLinkPerfStats_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,31,1,1,3))
_AdGenPppLinkPerfTable_Object=MibTable
adGenPppLinkPerfTable=_AdGenPppLinkPerfTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,1))
if mibBuilder.loadTexts:adGenPppLinkPerfTable.setStatus(_A)
_AdGenPppLinkPerfEntry_Object=MibTableRow
adGenPppLinkPerfEntry=_AdGenPppLinkPerfEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,1,1))
adGenPppLinkPerfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenPppLinkPerfEntry.setStatus(_A)
_AdGenPppLinkInOctets_Type=Counter32
_AdGenPppLinkInOctets_Object=MibTableColumn
adGenPppLinkInOctets=_AdGenPppLinkInOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,1,1,1),_AdGenPppLinkInOctets_Type())
adGenPppLinkInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkInOctets.setStatus(_A)
_AdGenPppLinkInGoodOctets_Type=Counter32
_AdGenPppLinkInGoodOctets_Object=MibTableColumn
adGenPppLinkInGoodOctets=_AdGenPppLinkInGoodOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,1,1,2),_AdGenPppLinkInGoodOctets_Type())
adGenPppLinkInGoodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkInGoodOctets.setStatus(_A)
_AdGenPppLinkInPkts_Type=Counter32
_AdGenPppLinkInPkts_Object=MibTableColumn
adGenPppLinkInPkts=_AdGenPppLinkInPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,1,1,3),_AdGenPppLinkInPkts_Type())
adGenPppLinkInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkInPkts.setStatus(_A)
_AdGenPppLinkInDiscards_Type=Counter32
_AdGenPppLinkInDiscards_Object=MibTableColumn
adGenPppLinkInDiscards=_AdGenPppLinkInDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,1,1,4),_AdGenPppLinkInDiscards_Type())
adGenPppLinkInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkInDiscards.setStatus(_A)
_AdGenPppLinkInErrors_Type=Counter32
_AdGenPppLinkInErrors_Object=MibTableColumn
adGenPppLinkInErrors=_AdGenPppLinkInErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,1,1,5),_AdGenPppLinkInErrors_Type())
adGenPppLinkInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkInErrors.setStatus(_A)
_AdGenPppLinkOutOctets_Type=Counter32
_AdGenPppLinkOutOctets_Object=MibTableColumn
adGenPppLinkOutOctets=_AdGenPppLinkOutOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,1,1,6),_AdGenPppLinkOutOctets_Type())
adGenPppLinkOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkOutOctets.setStatus(_A)
_AdGenPppLinkOutPkts_Type=Counter32
_AdGenPppLinkOutPkts_Object=MibTableColumn
adGenPppLinkOutPkts=_AdGenPppLinkOutPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,1,1,7),_AdGenPppLinkOutPkts_Type())
adGenPppLinkOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkOutPkts.setStatus(_A)
_AdGenPppLinkOutDiscards_Type=Counter32
_AdGenPppLinkOutDiscards_Object=MibTableColumn
adGenPppLinkOutDiscards=_AdGenPppLinkOutDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,1,1,8),_AdGenPppLinkOutDiscards_Type())
adGenPppLinkOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkOutDiscards.setStatus(_A)
_AdGenPppLinkOutErrors_Type=Counter32
_AdGenPppLinkOutErrors_Object=MibTableColumn
adGenPppLinkOutErrors=_AdGenPppLinkOutErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,1,1,9),_AdGenPppLinkOutErrors_Type())
adGenPppLinkOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkOutErrors.setStatus(_A)
class _AdGenPppLinkValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_AdGenPppLinkValidIntervals_Type.__name__=_D
_AdGenPppLinkValidIntervals_Object=MibTableColumn
adGenPppLinkValidIntervals=_AdGenPppLinkValidIntervals_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,1,1,10),_AdGenPppLinkValidIntervals_Type())
adGenPppLinkValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkValidIntervals.setStatus(_A)
class _AdGenPppLinkInvalidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_AdGenPppLinkInvalidIntervals_Type.__name__=_D
_AdGenPppLinkInvalidIntervals_Object=MibTableColumn
adGenPppLinkInvalidIntervals=_AdGenPppLinkInvalidIntervals_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,1,1,11),_AdGenPppLinkInvalidIntervals_Type())
adGenPppLinkInvalidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkInvalidIntervals.setStatus(_A)
class _AdGenPppLinkTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_AdGenPppLinkTimeElapsed_Type.__name__=_D
_AdGenPppLinkTimeElapsed_Object=MibTableColumn
adGenPppLinkTimeElapsed=_AdGenPppLinkTimeElapsed_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,1,1,12),_AdGenPppLinkTimeElapsed_Type())
adGenPppLinkTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkTimeElapsed.setStatus(_A)
class _AdGenPppLinkResetStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_X,1))
_AdGenPppLinkResetStats_Type.__name__=_D
_AdGenPppLinkResetStats_Object=MibTableColumn
adGenPppLinkResetStats=_AdGenPppLinkResetStats_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,1,1,13),_AdGenPppLinkResetStats_Type())
adGenPppLinkResetStats.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppLinkResetStats.setStatus(_A)
class _AdGenPppLinkResetPerfHistory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_X,1))
_AdGenPppLinkResetPerfHistory_Type.__name__=_D
_AdGenPppLinkResetPerfHistory_Object=MibTableColumn
adGenPppLinkResetPerfHistory=_AdGenPppLinkResetPerfHistory_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,1,1,14),_AdGenPppLinkResetPerfHistory_Type())
adGenPppLinkResetPerfHistory.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppLinkResetPerfHistory.setStatus(_A)
_AdGenPppLinkCurrentTable_Object=MibTable
adGenPppLinkCurrentTable=_AdGenPppLinkCurrentTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,2))
if mibBuilder.loadTexts:adGenPppLinkCurrentTable.setStatus(_A)
_AdGenPppLinkCurrentEntry_Object=MibTableRow
adGenPppLinkCurrentEntry=_AdGenPppLinkCurrentEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,2,1))
adGenPppLinkCurrentEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenPppLinkCurrentEntry.setStatus(_A)
_AdGenPppLinkCurrentInOctets_Type=Gauge32
_AdGenPppLinkCurrentInOctets_Object=MibTableColumn
adGenPppLinkCurrentInOctets=_AdGenPppLinkCurrentInOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,2,1,1),_AdGenPppLinkCurrentInOctets_Type())
adGenPppLinkCurrentInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkCurrentInOctets.setStatus(_A)
_AdGenPppLinkCurrentInGoodOctets_Type=Gauge32
_AdGenPppLinkCurrentInGoodOctets_Object=MibTableColumn
adGenPppLinkCurrentInGoodOctets=_AdGenPppLinkCurrentInGoodOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,2,1,2),_AdGenPppLinkCurrentInGoodOctets_Type())
adGenPppLinkCurrentInGoodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkCurrentInGoodOctets.setStatus(_A)
_AdGenPppLinkCurrentInPkts_Type=Gauge32
_AdGenPppLinkCurrentInPkts_Object=MibTableColumn
adGenPppLinkCurrentInPkts=_AdGenPppLinkCurrentInPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,2,1,3),_AdGenPppLinkCurrentInPkts_Type())
adGenPppLinkCurrentInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkCurrentInPkts.setStatus(_A)
_AdGenPppLinkCurrentInDiscards_Type=Gauge32
_AdGenPppLinkCurrentInDiscards_Object=MibTableColumn
adGenPppLinkCurrentInDiscards=_AdGenPppLinkCurrentInDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,2,1,4),_AdGenPppLinkCurrentInDiscards_Type())
adGenPppLinkCurrentInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkCurrentInDiscards.setStatus(_A)
_AdGenPppLinkCurrentInErrors_Type=Gauge32
_AdGenPppLinkCurrentInErrors_Object=MibTableColumn
adGenPppLinkCurrentInErrors=_AdGenPppLinkCurrentInErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,2,1,5),_AdGenPppLinkCurrentInErrors_Type())
adGenPppLinkCurrentInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkCurrentInErrors.setStatus(_A)
_AdGenPppLinkCurrentOutOctets_Type=Gauge32
_AdGenPppLinkCurrentOutOctets_Object=MibTableColumn
adGenPppLinkCurrentOutOctets=_AdGenPppLinkCurrentOutOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,2,1,6),_AdGenPppLinkCurrentOutOctets_Type())
adGenPppLinkCurrentOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkCurrentOutOctets.setStatus(_A)
_AdGenPppLinkCurrentOutPkts_Type=Gauge32
_AdGenPppLinkCurrentOutPkts_Object=MibTableColumn
adGenPppLinkCurrentOutPkts=_AdGenPppLinkCurrentOutPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,2,1,7),_AdGenPppLinkCurrentOutPkts_Type())
adGenPppLinkCurrentOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkCurrentOutPkts.setStatus(_A)
_AdGenPppLinkCurrentOutDiscards_Type=Gauge32
_AdGenPppLinkCurrentOutDiscards_Object=MibTableColumn
adGenPppLinkCurrentOutDiscards=_AdGenPppLinkCurrentOutDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,2,1,8),_AdGenPppLinkCurrentOutDiscards_Type())
adGenPppLinkCurrentOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkCurrentOutDiscards.setStatus(_A)
_AdGenPppLinkCurrentOutErrors_Type=Gauge32
_AdGenPppLinkCurrentOutErrors_Object=MibTableColumn
adGenPppLinkCurrentOutErrors=_AdGenPppLinkCurrentOutErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,2,1,9),_AdGenPppLinkCurrentOutErrors_Type())
adGenPppLinkCurrentOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkCurrentOutErrors.setStatus(_A)
_AdGenPppLinkIntervalTable_Object=MibTable
adGenPppLinkIntervalTable=_AdGenPppLinkIntervalTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,3))
if mibBuilder.loadTexts:adGenPppLinkIntervalTable.setStatus(_A)
_AdGenPppLinkIntervalEntry_Object=MibTableRow
adGenPppLinkIntervalEntry=_AdGenPppLinkIntervalEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,3,1))
adGenPppLinkIntervalEntry.setIndexNames((0,_E,_F),(0,_V,_j))
if mibBuilder.loadTexts:adGenPppLinkIntervalEntry.setStatus(_A)
class _AdGenPppLinkIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AdGenPppLinkIntervalNumber_Type.__name__=_D
_AdGenPppLinkIntervalNumber_Object=MibTableColumn
adGenPppLinkIntervalNumber=_AdGenPppLinkIntervalNumber_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,3,1,1),_AdGenPppLinkIntervalNumber_Type())
adGenPppLinkIntervalNumber.setMaxAccess(_Y)
if mibBuilder.loadTexts:adGenPppLinkIntervalNumber.setStatus(_A)
_AdGenPppLinkIntervalInOctets_Type=Gauge32
_AdGenPppLinkIntervalInOctets_Object=MibTableColumn
adGenPppLinkIntervalInOctets=_AdGenPppLinkIntervalInOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,3,1,2),_AdGenPppLinkIntervalInOctets_Type())
adGenPppLinkIntervalInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkIntervalInOctets.setStatus(_A)
_AdGenPppLinkIntervalInGoodOctets_Type=Gauge32
_AdGenPppLinkIntervalInGoodOctets_Object=MibTableColumn
adGenPppLinkIntervalInGoodOctets=_AdGenPppLinkIntervalInGoodOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,3,1,3),_AdGenPppLinkIntervalInGoodOctets_Type())
adGenPppLinkIntervalInGoodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkIntervalInGoodOctets.setStatus(_A)
_AdGenPppLinkIntervalInPkts_Type=Gauge32
_AdGenPppLinkIntervalInPkts_Object=MibTableColumn
adGenPppLinkIntervalInPkts=_AdGenPppLinkIntervalInPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,3,1,4),_AdGenPppLinkIntervalInPkts_Type())
adGenPppLinkIntervalInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkIntervalInPkts.setStatus(_A)
_AdGenPppLinkIntervalInDiscards_Type=Gauge32
_AdGenPppLinkIntervalInDiscards_Object=MibTableColumn
adGenPppLinkIntervalInDiscards=_AdGenPppLinkIntervalInDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,3,1,5),_AdGenPppLinkIntervalInDiscards_Type())
adGenPppLinkIntervalInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkIntervalInDiscards.setStatus(_A)
_AdGenPppLinkIntervalInErrors_Type=Gauge32
_AdGenPppLinkIntervalInErrors_Object=MibTableColumn
adGenPppLinkIntervalInErrors=_AdGenPppLinkIntervalInErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,3,1,6),_AdGenPppLinkIntervalInErrors_Type())
adGenPppLinkIntervalInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkIntervalInErrors.setStatus(_A)
_AdGenPppLinkIntervalOutOctets_Type=Gauge32
_AdGenPppLinkIntervalOutOctets_Object=MibTableColumn
adGenPppLinkIntervalOutOctets=_AdGenPppLinkIntervalOutOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,3,1,7),_AdGenPppLinkIntervalOutOctets_Type())
adGenPppLinkIntervalOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkIntervalOutOctets.setStatus(_A)
_AdGenPppLinkIntervalOutPkts_Type=Gauge32
_AdGenPppLinkIntervalOutPkts_Object=MibTableColumn
adGenPppLinkIntervalOutPkts=_AdGenPppLinkIntervalOutPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,3,1,8),_AdGenPppLinkIntervalOutPkts_Type())
adGenPppLinkIntervalOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkIntervalOutPkts.setStatus(_A)
_AdGenPppLinkIntervalOutDiscards_Type=Gauge32
_AdGenPppLinkIntervalOutDiscards_Object=MibTableColumn
adGenPppLinkIntervalOutDiscards=_AdGenPppLinkIntervalOutDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,3,1,9),_AdGenPppLinkIntervalOutDiscards_Type())
adGenPppLinkIntervalOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkIntervalOutDiscards.setStatus(_A)
_AdGenPppLinkIntervalOutErrors_Type=Gauge32
_AdGenPppLinkIntervalOutErrors_Object=MibTableColumn
adGenPppLinkIntervalOutErrors=_AdGenPppLinkIntervalOutErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,3,1,10),_AdGenPppLinkIntervalOutErrors_Type())
adGenPppLinkIntervalOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkIntervalOutErrors.setStatus(_A)
_AdGenPppLinkIntervalTimeStamp_Type=DisplayString
_AdGenPppLinkIntervalTimeStamp_Object=MibTableColumn
adGenPppLinkIntervalTimeStamp=_AdGenPppLinkIntervalTimeStamp_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,3,1,11),_AdGenPppLinkIntervalTimeStamp_Type())
adGenPppLinkIntervalTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkIntervalTimeStamp.setStatus(_A)
_AdGenPppLinkTotalTable_Object=MibTable
adGenPppLinkTotalTable=_AdGenPppLinkTotalTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,4))
if mibBuilder.loadTexts:adGenPppLinkTotalTable.setStatus(_A)
_AdGenPppLinkTotalEntry_Object=MibTableRow
adGenPppLinkTotalEntry=_AdGenPppLinkTotalEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,4,1))
adGenPppLinkTotalEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenPppLinkTotalEntry.setStatus(_A)
_AdGenPppLinkTotalInOctets_Type=Gauge32
_AdGenPppLinkTotalInOctets_Object=MibTableColumn
adGenPppLinkTotalInOctets=_AdGenPppLinkTotalInOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,4,1,1),_AdGenPppLinkTotalInOctets_Type())
adGenPppLinkTotalInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkTotalInOctets.setStatus(_A)
_AdGenPppLinkTotalInGoodOctets_Type=Gauge32
_AdGenPppLinkTotalInGoodOctets_Object=MibTableColumn
adGenPppLinkTotalInGoodOctets=_AdGenPppLinkTotalInGoodOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,4,1,2),_AdGenPppLinkTotalInGoodOctets_Type())
adGenPppLinkTotalInGoodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkTotalInGoodOctets.setStatus(_A)
_AdGenPppLinkTotalInPkts_Type=Gauge32
_AdGenPppLinkTotalInPkts_Object=MibTableColumn
adGenPppLinkTotalInPkts=_AdGenPppLinkTotalInPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,4,1,3),_AdGenPppLinkTotalInPkts_Type())
adGenPppLinkTotalInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkTotalInPkts.setStatus(_A)
_AdGenPppLinkTotalInDiscards_Type=Gauge32
_AdGenPppLinkTotalInDiscards_Object=MibTableColumn
adGenPppLinkTotalInDiscards=_AdGenPppLinkTotalInDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,4,1,4),_AdGenPppLinkTotalInDiscards_Type())
adGenPppLinkTotalInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkTotalInDiscards.setStatus(_A)
_AdGenPppLinkTotalInErrors_Type=Gauge32
_AdGenPppLinkTotalInErrors_Object=MibTableColumn
adGenPppLinkTotalInErrors=_AdGenPppLinkTotalInErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,4,1,5),_AdGenPppLinkTotalInErrors_Type())
adGenPppLinkTotalInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkTotalInErrors.setStatus(_A)
_AdGenPppLinkTotalOutOctets_Type=Gauge32
_AdGenPppLinkTotalOutOctets_Object=MibTableColumn
adGenPppLinkTotalOutOctets=_AdGenPppLinkTotalOutOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,4,1,6),_AdGenPppLinkTotalOutOctets_Type())
adGenPppLinkTotalOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkTotalOutOctets.setStatus(_A)
_AdGenPppLinkTotalOutPkts_Type=Gauge32
_AdGenPppLinkTotalOutPkts_Object=MibTableColumn
adGenPppLinkTotalOutPkts=_AdGenPppLinkTotalOutPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,4,1,7),_AdGenPppLinkTotalOutPkts_Type())
adGenPppLinkTotalOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkTotalOutPkts.setStatus(_A)
_AdGenPppLinkTotalOutDiscards_Type=Gauge32
_AdGenPppLinkTotalOutDiscards_Object=MibTableColumn
adGenPppLinkTotalOutDiscards=_AdGenPppLinkTotalOutDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,4,1,8),_AdGenPppLinkTotalOutDiscards_Type())
adGenPppLinkTotalOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkTotalOutDiscards.setStatus(_A)
_AdGenPppLinkTotalOutErrors_Type=Gauge32
_AdGenPppLinkTotalOutErrors_Object=MibTableColumn
adGenPppLinkTotalOutErrors=_AdGenPppLinkTotalOutErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,4,1,9),_AdGenPppLinkTotalOutErrors_Type())
adGenPppLinkTotalOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkTotalOutErrors.setStatus(_A)
_AdGenPppLinkDayCurrentTable_Object=MibTable
adGenPppLinkDayCurrentTable=_AdGenPppLinkDayCurrentTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,5))
if mibBuilder.loadTexts:adGenPppLinkDayCurrentTable.setStatus(_A)
_AdGenPppLinkDayCurrentEntry_Object=MibTableRow
adGenPppLinkDayCurrentEntry=_AdGenPppLinkDayCurrentEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,5,1))
adGenPppLinkDayCurrentEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenPppLinkDayCurrentEntry.setStatus(_A)
_AdGenPppLinkDayCurrentInOctets_Type=Gauge32
_AdGenPppLinkDayCurrentInOctets_Object=MibTableColumn
adGenPppLinkDayCurrentInOctets=_AdGenPppLinkDayCurrentInOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,5,1,1),_AdGenPppLinkDayCurrentInOctets_Type())
adGenPppLinkDayCurrentInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayCurrentInOctets.setStatus(_A)
_AdGenPppLinkDayCurrentInGoodOctets_Type=Gauge32
_AdGenPppLinkDayCurrentInGoodOctets_Object=MibTableColumn
adGenPppLinkDayCurrentInGoodOctets=_AdGenPppLinkDayCurrentInGoodOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,5,1,2),_AdGenPppLinkDayCurrentInGoodOctets_Type())
adGenPppLinkDayCurrentInGoodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayCurrentInGoodOctets.setStatus(_A)
_AdGenPppLinkDayCurrentInPkts_Type=Gauge32
_AdGenPppLinkDayCurrentInPkts_Object=MibTableColumn
adGenPppLinkDayCurrentInPkts=_AdGenPppLinkDayCurrentInPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,5,1,3),_AdGenPppLinkDayCurrentInPkts_Type())
adGenPppLinkDayCurrentInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayCurrentInPkts.setStatus(_A)
_AdGenPppLinkDayCurrentInDiscards_Type=Gauge32
_AdGenPppLinkDayCurrentInDiscards_Object=MibTableColumn
adGenPppLinkDayCurrentInDiscards=_AdGenPppLinkDayCurrentInDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,5,1,4),_AdGenPppLinkDayCurrentInDiscards_Type())
adGenPppLinkDayCurrentInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayCurrentInDiscards.setStatus(_A)
_AdGenPppLinkDayCurrentInErrors_Type=Gauge32
_AdGenPppLinkDayCurrentInErrors_Object=MibTableColumn
adGenPppLinkDayCurrentInErrors=_AdGenPppLinkDayCurrentInErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,5,1,5),_AdGenPppLinkDayCurrentInErrors_Type())
adGenPppLinkDayCurrentInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayCurrentInErrors.setStatus(_A)
_AdGenPppLinkDayCurrentOutOctets_Type=Gauge32
_AdGenPppLinkDayCurrentOutOctets_Object=MibTableColumn
adGenPppLinkDayCurrentOutOctets=_AdGenPppLinkDayCurrentOutOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,5,1,6),_AdGenPppLinkDayCurrentOutOctets_Type())
adGenPppLinkDayCurrentOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayCurrentOutOctets.setStatus(_A)
_AdGenPppLinkDayCurrentOutPkts_Type=Gauge32
_AdGenPppLinkDayCurrentOutPkts_Object=MibTableColumn
adGenPppLinkDayCurrentOutPkts=_AdGenPppLinkDayCurrentOutPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,5,1,7),_AdGenPppLinkDayCurrentOutPkts_Type())
adGenPppLinkDayCurrentOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayCurrentOutPkts.setStatus(_A)
_AdGenPppLinkDayCurrentOutDiscards_Type=Gauge32
_AdGenPppLinkDayCurrentOutDiscards_Object=MibTableColumn
adGenPppLinkDayCurrentOutDiscards=_AdGenPppLinkDayCurrentOutDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,5,1,8),_AdGenPppLinkDayCurrentOutDiscards_Type())
adGenPppLinkDayCurrentOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayCurrentOutDiscards.setStatus(_A)
_AdGenPppLinkDayCurrentOutErrors_Type=Gauge32
_AdGenPppLinkDayCurrentOutErrors_Object=MibTableColumn
adGenPppLinkDayCurrentOutErrors=_AdGenPppLinkDayCurrentOutErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,5,1,9),_AdGenPppLinkDayCurrentOutErrors_Type())
adGenPppLinkDayCurrentOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayCurrentOutErrors.setStatus(_A)
_AdGenPppLinkDayIntervalTable_Object=MibTable
adGenPppLinkDayIntervalTable=_AdGenPppLinkDayIntervalTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,6))
if mibBuilder.loadTexts:adGenPppLinkDayIntervalTable.setStatus(_A)
_AdGenPppLinkDayIntervalEntry_Object=MibTableRow
adGenPppLinkDayIntervalEntry=_AdGenPppLinkDayIntervalEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,6,1))
adGenPppLinkDayIntervalEntry.setIndexNames((0,_E,_F),(0,_V,_k))
if mibBuilder.loadTexts:adGenPppLinkDayIntervalEntry.setStatus(_A)
class _AdGenPppLinkDayIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_AdGenPppLinkDayIntervalNumber_Type.__name__=_D
_AdGenPppLinkDayIntervalNumber_Object=MibTableColumn
adGenPppLinkDayIntervalNumber=_AdGenPppLinkDayIntervalNumber_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,6,1,1),_AdGenPppLinkDayIntervalNumber_Type())
adGenPppLinkDayIntervalNumber.setMaxAccess(_Y)
if mibBuilder.loadTexts:adGenPppLinkDayIntervalNumber.setStatus(_A)
_AdGenPppLinkDayIntervalInOctets_Type=Gauge32
_AdGenPppLinkDayIntervalInOctets_Object=MibTableColumn
adGenPppLinkDayIntervalInOctets=_AdGenPppLinkDayIntervalInOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,6,1,2),_AdGenPppLinkDayIntervalInOctets_Type())
adGenPppLinkDayIntervalInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayIntervalInOctets.setStatus(_A)
_AdGenPppLinkDayIntervalInGoodOctets_Type=Gauge32
_AdGenPppLinkDayIntervalInGoodOctets_Object=MibTableColumn
adGenPppLinkDayIntervalInGoodOctets=_AdGenPppLinkDayIntervalInGoodOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,6,1,3),_AdGenPppLinkDayIntervalInGoodOctets_Type())
adGenPppLinkDayIntervalInGoodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayIntervalInGoodOctets.setStatus(_A)
_AdGenPppLinkDayIntervalInPkts_Type=Gauge32
_AdGenPppLinkDayIntervalInPkts_Object=MibTableColumn
adGenPppLinkDayIntervalInPkts=_AdGenPppLinkDayIntervalInPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,6,1,4),_AdGenPppLinkDayIntervalInPkts_Type())
adGenPppLinkDayIntervalInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayIntervalInPkts.setStatus(_A)
_AdGenPppLinkDayIntervalInDiscards_Type=Gauge32
_AdGenPppLinkDayIntervalInDiscards_Object=MibTableColumn
adGenPppLinkDayIntervalInDiscards=_AdGenPppLinkDayIntervalInDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,6,1,5),_AdGenPppLinkDayIntervalInDiscards_Type())
adGenPppLinkDayIntervalInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayIntervalInDiscards.setStatus(_A)
_AdGenPppLinkDayIntervalInErrors_Type=Gauge32
_AdGenPppLinkDayIntervalInErrors_Object=MibTableColumn
adGenPppLinkDayIntervalInErrors=_AdGenPppLinkDayIntervalInErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,6,1,6),_AdGenPppLinkDayIntervalInErrors_Type())
adGenPppLinkDayIntervalInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayIntervalInErrors.setStatus(_A)
_AdGenPppLinkDayIntervalOutOctets_Type=Gauge32
_AdGenPppLinkDayIntervalOutOctets_Object=MibTableColumn
adGenPppLinkDayIntervalOutOctets=_AdGenPppLinkDayIntervalOutOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,6,1,7),_AdGenPppLinkDayIntervalOutOctets_Type())
adGenPppLinkDayIntervalOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayIntervalOutOctets.setStatus(_A)
_AdGenPppLinkDayIntervalOutPkts_Type=Gauge32
_AdGenPppLinkDayIntervalOutPkts_Object=MibTableColumn
adGenPppLinkDayIntervalOutPkts=_AdGenPppLinkDayIntervalOutPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,6,1,8),_AdGenPppLinkDayIntervalOutPkts_Type())
adGenPppLinkDayIntervalOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayIntervalOutPkts.setStatus(_A)
_AdGenPppLinkDayIntervalOutDiscards_Type=Gauge32
_AdGenPppLinkDayIntervalOutDiscards_Object=MibTableColumn
adGenPppLinkDayIntervalOutDiscards=_AdGenPppLinkDayIntervalOutDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,6,1,9),_AdGenPppLinkDayIntervalOutDiscards_Type())
adGenPppLinkDayIntervalOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayIntervalOutDiscards.setStatus(_A)
_AdGenPppLinkDayIntervalOutErrors_Type=Gauge32
_AdGenPppLinkDayIntervalOutErrors_Object=MibTableColumn
adGenPppLinkDayIntervalOutErrors=_AdGenPppLinkDayIntervalOutErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,6,1,10),_AdGenPppLinkDayIntervalOutErrors_Type())
adGenPppLinkDayIntervalOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayIntervalOutErrors.setStatus(_A)
_AdGenPppLinkDayIntervalTimeStamp_Type=DisplayString
_AdGenPppLinkDayIntervalTimeStamp_Object=MibTableColumn
adGenPppLinkDayIntervalTimeStamp=_AdGenPppLinkDayIntervalTimeStamp_Object((1,3,6,1,4,1,664,5,67,1,31,1,1,3,6,1,11),_AdGenPppLinkDayIntervalTimeStamp_Type())
adGenPppLinkDayIntervalTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppLinkDayIntervalTimeStamp.setStatus(_A)
_AdGenPppGroupObjects_ObjectIdentity=ObjectIdentity
adGenPppGroupObjects=_AdGenPppGroupObjects_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,31,1,2))
_AdGenPppGroupProv_ObjectIdentity=ObjectIdentity
adGenPppGroupProv=_AdGenPppGroupProv_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,31,1,2,1))
_AdGenPppGroupProvTable_Object=MibTable
adGenPppGroupProvTable=_AdGenPppGroupProvTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1))
if mibBuilder.loadTexts:adGenPppGroupProvTable.setStatus(_A)
_AdGenPppGroupProvEntry_Object=MibTableRow
adGenPppGroupProvEntry=_AdGenPppGroupProvEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1))
adGenPppGroupProvEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenPppGroupProvEntry.setStatus(_A)
_AdGenPppGroupSubscriberIpAddress_Type=IpAddress
_AdGenPppGroupSubscriberIpAddress_Object=MibTableColumn
adGenPppGroupSubscriberIpAddress=_AdGenPppGroupSubscriberIpAddress_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,1),_AdGenPppGroupSubscriberIpAddress_Type())
adGenPppGroupSubscriberIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupSubscriberIpAddress.setStatus(_A)
_AdGenPppGroupGatewayIpAddress_Type=IpAddress
_AdGenPppGroupGatewayIpAddress_Object=MibTableColumn
adGenPppGroupGatewayIpAddress=_AdGenPppGroupGatewayIpAddress_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,2),_AdGenPppGroupGatewayIpAddress_Type())
adGenPppGroupGatewayIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupGatewayIpAddress.setStatus(_A)
_AdGenPppGroupPrimaryDNSIpAddress_Type=IpAddress
_AdGenPppGroupPrimaryDNSIpAddress_Object=MibTableColumn
adGenPppGroupPrimaryDNSIpAddress=_AdGenPppGroupPrimaryDNSIpAddress_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,3),_AdGenPppGroupPrimaryDNSIpAddress_Type())
adGenPppGroupPrimaryDNSIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupPrimaryDNSIpAddress.setStatus(_A)
_AdGenPppGroupSecondaryDNSIpAddress_Type=IpAddress
_AdGenPppGroupSecondaryDNSIpAddress_Object=MibTableColumn
adGenPppGroupSecondaryDNSIpAddress=_AdGenPppGroupSecondaryDNSIpAddress_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,4),_AdGenPppGroupSecondaryDNSIpAddress_Type())
adGenPppGroupSecondaryDNSIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupSecondaryDNSIpAddress.setStatus(_A)
class _AdGenPppGroupConfigInitialMRU_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AdGenPppGroupConfigInitialMRU_Type.__name__=_D
_AdGenPppGroupConfigInitialMRU_Object=MibTableColumn
adGenPppGroupConfigInitialMRU=_AdGenPppGroupConfigInitialMRU_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,5),_AdGenPppGroupConfigInitialMRU_Type())
adGenPppGroupConfigInitialMRU.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupConfigInitialMRU.setStatus(_A)
class _AdGenPppGroupConfigMagicNumber_Type(TruthValue):defaultValue=2
_AdGenPppGroupConfigMagicNumber_Type.__name__=_I
_AdGenPppGroupConfigMagicNumber_Object=MibTableColumn
adGenPppGroupConfigMagicNumber=_AdGenPppGroupConfigMagicNumber_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,6),_AdGenPppGroupConfigMagicNumber_Type())
adGenPppGroupConfigMagicNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupConfigMagicNumber.setStatus(_A)
class _AdGenPppGroupConfigFcsSize_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('zerobits',1),('sixteenbits',2),('thirtytwobits',3)))
_AdGenPppGroupConfigFcsSize_Type.__name__=_D
_AdGenPppGroupConfigFcsSize_Object=MibTableColumn
adGenPppGroupConfigFcsSize=_AdGenPppGroupConfigFcsSize_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,7),_AdGenPppGroupConfigFcsSize_Type())
adGenPppGroupConfigFcsSize.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupConfigFcsSize.setStatus(_A)
class _AdGenPppGroupConfigACCompression_Type(TruthValue):defaultValue=2
_AdGenPppGroupConfigACCompression_Type.__name__=_I
_AdGenPppGroupConfigACCompression_Object=MibTableColumn
adGenPppGroupConfigACCompression=_AdGenPppGroupConfigACCompression_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,8),_AdGenPppGroupConfigACCompression_Type())
adGenPppGroupConfigACCompression.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupConfigACCompression.setStatus(_A)
class _AdGenPppGroupConfigPFCompression_Type(TruthValue):defaultValue=2
_AdGenPppGroupConfigPFCompression_Type.__name__=_I
_AdGenPppGroupConfigPFCompression_Object=MibTableColumn
adGenPppGroupConfigPFCompression=_AdGenPppGroupConfigPFCompression_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,9),_AdGenPppGroupConfigPFCompression_Type())
adGenPppGroupConfigPFCompression.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupConfigPFCompression.setStatus(_A)
class _AdGenPppGroupConfigLQM_Type(TruthValue):defaultValue=1
_AdGenPppGroupConfigLQM_Type.__name__=_I
_AdGenPppGroupConfigLQM_Object=MibTableColumn
adGenPppGroupConfigLQM=_AdGenPppGroupConfigLQM_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,10),_AdGenPppGroupConfigLQM_Type())
adGenPppGroupConfigLQM.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupConfigLQM.setStatus(_A)
class _AdGenPppGroupConfigRestartTimer_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_AdGenPppGroupConfigRestartTimer_Type.__name__=_D
_AdGenPppGroupConfigRestartTimer_Object=MibTableColumn
adGenPppGroupConfigRestartTimer=_AdGenPppGroupConfigRestartTimer_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,11),_AdGenPppGroupConfigRestartTimer_Type())
adGenPppGroupConfigRestartTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupConfigRestartTimer.setStatus(_A)
class _AdGenPppGroupConfigMaxTerminate_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,30))
_AdGenPppGroupConfigMaxTerminate_Type.__name__=_D
_AdGenPppGroupConfigMaxTerminate_Object=MibTableColumn
adGenPppGroupConfigMaxTerminate=_AdGenPppGroupConfigMaxTerminate_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,12),_AdGenPppGroupConfigMaxTerminate_Type())
adGenPppGroupConfigMaxTerminate.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupConfigMaxTerminate.setStatus(_A)
class _AdGenPppGroupConfigMaxConfigure_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,30))
_AdGenPppGroupConfigMaxConfigure_Type.__name__=_D
_AdGenPppGroupConfigMaxConfigure_Object=MibTableColumn
adGenPppGroupConfigMaxConfigure=_AdGenPppGroupConfigMaxConfigure_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,13),_AdGenPppGroupConfigMaxConfigure_Type())
adGenPppGroupConfigMaxConfigure.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupConfigMaxConfigure.setStatus(_A)
class _AdGenPppGroupConfigMaxFailure_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,30))
_AdGenPppGroupConfigMaxFailure_Type.__name__=_D
_AdGenPppGroupConfigMaxFailure_Object=MibTableColumn
adGenPppGroupConfigMaxFailure=_AdGenPppGroupConfigMaxFailure_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,14),_AdGenPppGroupConfigMaxFailure_Type())
adGenPppGroupConfigMaxFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupConfigMaxFailure.setStatus(_A)
class _AdGenPppGroupConfigKeepAliveRate_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_AdGenPppGroupConfigKeepAliveRate_Type.__name__=_D
_AdGenPppGroupConfigKeepAliveRate_Object=MibTableColumn
adGenPppGroupConfigKeepAliveRate=_AdGenPppGroupConfigKeepAliveRate_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,15),_AdGenPppGroupConfigKeepAliveRate_Type())
adGenPppGroupConfigKeepAliveRate.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupConfigKeepAliveRate.setStatus(_A)
class _AdGenPppGroupChapEnabled_Type(TruthValue):defaultValue=2
_AdGenPppGroupChapEnabled_Type.__name__=_I
_AdGenPppGroupChapEnabled_Object=MibTableColumn
adGenPppGroupChapEnabled=_AdGenPppGroupChapEnabled_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,16),_AdGenPppGroupChapEnabled_Type())
adGenPppGroupChapEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupChapEnabled.setStatus(_A)
class _AdGenPppGroupLocalUserName_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AdGenPppGroupLocalUserName_Type.__name__=_P
_AdGenPppGroupLocalUserName_Object=MibTableColumn
adGenPppGroupLocalUserName=_AdGenPppGroupLocalUserName_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,17),_AdGenPppGroupLocalUserName_Type())
adGenPppGroupLocalUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupLocalUserName.setStatus(_A)
class _AdGenPppGroupLocalPassword_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AdGenPppGroupLocalPassword_Type.__name__=_P
_AdGenPppGroupLocalPassword_Object=MibTableColumn
adGenPppGroupLocalPassword=_AdGenPppGroupLocalPassword_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,18),_AdGenPppGroupLocalPassword_Type())
adGenPppGroupLocalPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupLocalPassword.setStatus(_A)
class _AdGenPppGroupPeerUserName_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AdGenPppGroupPeerUserName_Type.__name__=_P
_AdGenPppGroupPeerUserName_Object=MibTableColumn
adGenPppGroupPeerUserName=_AdGenPppGroupPeerUserName_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,19),_AdGenPppGroupPeerUserName_Type())
adGenPppGroupPeerUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupPeerUserName.setStatus(_A)
class _AdGenPppGroupPeerPassword_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AdGenPppGroupPeerPassword_Type.__name__=_P
_AdGenPppGroupPeerPassword_Object=MibTableColumn
adGenPppGroupPeerPassword=_AdGenPppGroupPeerPassword_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,20),_AdGenPppGroupPeerPassword_Type())
adGenPppGroupPeerPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupPeerPassword.setStatus(_A)
class _AdGenPppGroupIpAddressAssignment_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('staticIpv4',1),('dhcpv4',2)))
_AdGenPppGroupIpAddressAssignment_Type.__name__=_D
_AdGenPppGroupIpAddressAssignment_Object=MibTableColumn
adGenPppGroupIpAddressAssignment=_AdGenPppGroupIpAddressAssignment_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,21),_AdGenPppGroupIpAddressAssignment_Type())
adGenPppGroupIpAddressAssignment.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupIpAddressAssignment.setStatus(_A)
class _AdGenPppGroupDhcpClientIdentfier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,80))
_AdGenPppGroupDhcpClientIdentfier_Type.__name__=_P
_AdGenPppGroupDhcpClientIdentfier_Object=MibTableColumn
adGenPppGroupDhcpClientIdentfier=_AdGenPppGroupDhcpClientIdentfier_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,22),_AdGenPppGroupDhcpClientIdentfier_Type())
adGenPppGroupDhcpClientIdentfier.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupDhcpClientIdentfier.setStatus(_A)
class _AdGenPppGroupDhcpHostname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,35))
_AdGenPppGroupDhcpHostname_Type.__name__=_i
_AdGenPppGroupDhcpHostname_Object=MibTableColumn
adGenPppGroupDhcpHostname=_AdGenPppGroupDhcpHostname_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,23),_AdGenPppGroupDhcpHostname_Type())
adGenPppGroupDhcpHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupDhcpHostname.setStatus(_A)
class _AdGenPppGroupConfigMultilink_Type(TruthValue):defaultValue=2
_AdGenPppGroupConfigMultilink_Type.__name__=_I
_AdGenPppGroupConfigMultilink_Object=MibTableColumn
adGenPppGroupConfigMultilink=_AdGenPppGroupConfigMultilink_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,24),_AdGenPppGroupConfigMultilink_Type())
adGenPppGroupConfigMultilink.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupConfigMultilink.setStatus(_A)
_AdGenPppGroupSubscriberIPv6Address_Type=InetAddressIPv6
_AdGenPppGroupSubscriberIPv6Address_Object=MibTableColumn
adGenPppGroupSubscriberIPv6Address=_AdGenPppGroupSubscriberIPv6Address_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,25),_AdGenPppGroupSubscriberIPv6Address_Type())
adGenPppGroupSubscriberIPv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupSubscriberIPv6Address.setStatus(_A)
class _AdGenPppGroupGatewayIPv6AddressAssignment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('auto',2)))
_AdGenPppGroupGatewayIPv6AddressAssignment_Type.__name__=_D
_AdGenPppGroupGatewayIPv6AddressAssignment_Object=MibTableColumn
adGenPppGroupGatewayIPv6AddressAssignment=_AdGenPppGroupGatewayIPv6AddressAssignment_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,26),_AdGenPppGroupGatewayIPv6AddressAssignment_Type())
adGenPppGroupGatewayIPv6AddressAssignment.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupGatewayIPv6AddressAssignment.setStatus(_A)
_AdGenPppGroupGatewayIPv6Address_Type=InetAddressIPv6
_AdGenPppGroupGatewayIPv6Address_Object=MibTableColumn
adGenPppGroupGatewayIPv6Address=_AdGenPppGroupGatewayIPv6Address_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,27),_AdGenPppGroupGatewayIPv6Address_Type())
adGenPppGroupGatewayIPv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupGatewayIPv6Address.setStatus(_A)
_AdGenPppGroupIpEnabled_Type=TruthValue
_AdGenPppGroupIpEnabled_Object=MibTableColumn
adGenPppGroupIpEnabled=_AdGenPppGroupIpEnabled_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,28),_AdGenPppGroupIpEnabled_Type())
adGenPppGroupIpEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupIpEnabled.setStatus(_A)
_AdGenPppGroupIpv6Enabled_Type=TruthValue
_AdGenPppGroupIpv6Enabled_Object=MibTableColumn
adGenPppGroupIpv6Enabled=_AdGenPppGroupIpv6Enabled_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,1,1,29),_AdGenPppGroupIpv6Enabled_Type())
adGenPppGroupIpv6Enabled.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupIpv6Enabled.setStatus(_A)
_AdGenPppGroupAlarmProvTable_Object=MibTable
adGenPppGroupAlarmProvTable=_AdGenPppGroupAlarmProvTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,2))
if mibBuilder.loadTexts:adGenPppGroupAlarmProvTable.setStatus(_A)
_AdGenPppGroupAlarmProvEntry_Object=MibTableRow
adGenPppGroupAlarmProvEntry=_AdGenPppGroupAlarmProvEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,2,1))
adGenPppGroupAlarmProvEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:adGenPppGroupAlarmProvEntry.setStatus(_A)
class _AdGenPppGroupAlarmProvNCPAlarmSeverity_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*((_Q,2),(_R,3),(_S,4),(_T,5),(_U,6)))
_AdGenPppGroupAlarmProvNCPAlarmSeverity_Type.__name__=_D
_AdGenPppGroupAlarmProvNCPAlarmSeverity_Object=MibTableColumn
adGenPppGroupAlarmProvNCPAlarmSeverity=_AdGenPppGroupAlarmProvNCPAlarmSeverity_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,2,1,1),_AdGenPppGroupAlarmProvNCPAlarmSeverity_Type())
adGenPppGroupAlarmProvNCPAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupAlarmProvNCPAlarmSeverity.setStatus(_A)
class _AdGenPppGroupAlarmProvNCPAlarmSuppression_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AdGenPppGroupAlarmProvNCPAlarmSuppression_Type.__name__=_D
_AdGenPppGroupAlarmProvNCPAlarmSuppression_Object=MibTableColumn
adGenPppGroupAlarmProvNCPAlarmSuppression=_AdGenPppGroupAlarmProvNCPAlarmSuppression_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,2,1,2),_AdGenPppGroupAlarmProvNCPAlarmSuppression_Type())
adGenPppGroupAlarmProvNCPAlarmSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupAlarmProvNCPAlarmSuppression.setStatus(_A)
class _AdGenPppGroupAlarmProvNCPAlarmEnable_Type(TruthValue):defaultValue=1
_AdGenPppGroupAlarmProvNCPAlarmEnable_Type.__name__=_I
_AdGenPppGroupAlarmProvNCPAlarmEnable_Object=MibTableColumn
adGenPppGroupAlarmProvNCPAlarmEnable=_AdGenPppGroupAlarmProvNCPAlarmEnable_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,2,1,3),_AdGenPppGroupAlarmProvNCPAlarmEnable_Type())
adGenPppGroupAlarmProvNCPAlarmEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupAlarmProvNCPAlarmEnable.setStatus(_A)
class _AdGenPppGroupAlarmProvIpv6NcpAlarmSeverity_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*((_Q,2),(_R,3),(_S,4),(_T,5),(_U,6)))
_AdGenPppGroupAlarmProvIpv6NcpAlarmSeverity_Type.__name__=_D
_AdGenPppGroupAlarmProvIpv6NcpAlarmSeverity_Object=MibTableColumn
adGenPppGroupAlarmProvIpv6NcpAlarmSeverity=_AdGenPppGroupAlarmProvIpv6NcpAlarmSeverity_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,2,1,4),_AdGenPppGroupAlarmProvIpv6NcpAlarmSeverity_Type())
adGenPppGroupAlarmProvIpv6NcpAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupAlarmProvIpv6NcpAlarmSeverity.setStatus(_A)
class _AdGenPppGroupAlarmProvIpv6NcpAlarmSuppression_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AdGenPppGroupAlarmProvIpv6NcpAlarmSuppression_Type.__name__=_D
_AdGenPppGroupAlarmProvIpv6NcpAlarmSuppression_Object=MibTableColumn
adGenPppGroupAlarmProvIpv6NcpAlarmSuppression=_AdGenPppGroupAlarmProvIpv6NcpAlarmSuppression_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,2,1,5),_AdGenPppGroupAlarmProvIpv6NcpAlarmSuppression_Type())
adGenPppGroupAlarmProvIpv6NcpAlarmSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupAlarmProvIpv6NcpAlarmSuppression.setStatus(_A)
class _AdGenPppGroupAlarmProvIpv6NcpAlarmEnable_Type(TruthValue):defaultValue=1
_AdGenPppGroupAlarmProvIpv6NcpAlarmEnable_Type.__name__=_I
_AdGenPppGroupAlarmProvIpv6NcpAlarmEnable_Object=MibTableColumn
adGenPppGroupAlarmProvIpv6NcpAlarmEnable=_AdGenPppGroupAlarmProvIpv6NcpAlarmEnable_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,2,1,6),_AdGenPppGroupAlarmProvIpv6NcpAlarmEnable_Type())
adGenPppGroupAlarmProvIpv6NcpAlarmEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupAlarmProvIpv6NcpAlarmEnable.setStatus(_A)
class _AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*((_Q,2),(_R,3),(_S,4),(_T,5),(_U,6)))
_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity_Type.__name__=_D
_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity_Object=MibTableColumn
adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity=_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,2,1,7),_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity_Type())
adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity.setStatus(_A)
class _AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression_Type.__name__=_D
_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression_Object=MibTableColumn
adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression=_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,2,1,8),_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression_Type())
adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression.setStatus(_A)
class _AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable_Type(TruthValue):defaultValue=1
_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable_Type.__name__=_I
_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable_Object=MibTableColumn
adGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable=_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,2,1,9),_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable_Type())
adGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable.setStatus(_A)
class _AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*((_Q,2),(_R,3),(_S,4),(_T,5),(_U,6)))
_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity_Type.__name__=_D
_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity_Object=MibTableColumn
adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity=_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,2,1,10),_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity_Type())
adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity.setStatus(_A)
class _AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression_Type.__name__=_D
_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression_Object=MibTableColumn
adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression=_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,2,1,11),_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression_Type())
adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression.setStatus(_A)
class _AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable_Type(TruthValue):defaultValue=1
_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable_Type.__name__=_I
_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable_Object=MibTableColumn
adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable=_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,1,2,1,12),_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable_Type())
adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable.setStatus(_A)
_AdGenPppGroupStatus_ObjectIdentity=ObjectIdentity
adGenPppGroupStatus=_AdGenPppGroupStatus_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,31,1,2,2))
_AdGenPppGroupStatusTable_Object=MibTable
adGenPppGroupStatusTable=_AdGenPppGroupStatusTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,2,1))
if mibBuilder.loadTexts:adGenPppGroupStatusTable.setStatus(_A)
_AdGenPppGroupStatusEntry_Object=MibTableRow
adGenPppGroupStatusEntry=_AdGenPppGroupStatusEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,2,1,1))
adGenPppGroupStatusEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenPppGroupStatusEntry.setStatus(_A)
class _AdGenPppGroupNCPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3),(_c,4),(_d,5),(_e,6),(_f,7),(_g,8),(_h,9),(_W,10)))
_AdGenPppGroupNCPState_Type.__name__=_D
_AdGenPppGroupNCPState_Object=MibTableColumn
adGenPppGroupNCPState=_AdGenPppGroupNCPState_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,2,1,1,1),_AdGenPppGroupNCPState_Type())
adGenPppGroupNCPState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupNCPState.setStatus(_A)
_AdGenPppGroupCurrentSubscriberIpAddress_Type=IpAddress
_AdGenPppGroupCurrentSubscriberIpAddress_Object=MibTableColumn
adGenPppGroupCurrentSubscriberIpAddress=_AdGenPppGroupCurrentSubscriberIpAddress_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,2,1,1,2),_AdGenPppGroupCurrentSubscriberIpAddress_Type())
adGenPppGroupCurrentSubscriberIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupCurrentSubscriberIpAddress.setStatus(_A)
_AdGenPppGroupCurrentGatewayIpAddress_Type=IpAddress
_AdGenPppGroupCurrentGatewayIpAddress_Object=MibTableColumn
adGenPppGroupCurrentGatewayIpAddress=_AdGenPppGroupCurrentGatewayIpAddress_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,2,1,1,3),_AdGenPppGroupCurrentGatewayIpAddress_Type())
adGenPppGroupCurrentGatewayIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupCurrentGatewayIpAddress.setStatus(_A)
_AdGenPppGroupCurrentPrimaryDNSIpAddress_Type=IpAddress
_AdGenPppGroupCurrentPrimaryDNSIpAddress_Object=MibTableColumn
adGenPppGroupCurrentPrimaryDNSIpAddress=_AdGenPppGroupCurrentPrimaryDNSIpAddress_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,2,1,1,4),_AdGenPppGroupCurrentPrimaryDNSIpAddress_Type())
adGenPppGroupCurrentPrimaryDNSIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupCurrentPrimaryDNSIpAddress.setStatus(_A)
_AdGenPppGroupCurrentSecondaryDNSIpAddress_Type=IpAddress
_AdGenPppGroupCurrentSecondaryDNSIpAddress_Object=MibTableColumn
adGenPppGroupCurrentSecondaryDNSIpAddress=_AdGenPppGroupCurrentSecondaryDNSIpAddress_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,2,1,1,5),_AdGenPppGroupCurrentSecondaryDNSIpAddress_Type())
adGenPppGroupCurrentSecondaryDNSIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupCurrentSecondaryDNSIpAddress.setStatus(_A)
_AdGenPppGroupNegotiatedStatus_Type=DisplayString
_AdGenPppGroupNegotiatedStatus_Object=MibTableColumn
adGenPppGroupNegotiatedStatus=_AdGenPppGroupNegotiatedStatus_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,2,1,1,6),_AdGenPppGroupNegotiatedStatus_Type())
adGenPppGroupNegotiatedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupNegotiatedStatus.setStatus(_A)
class _AdGenPppGroupIPv6AddressStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3)))
_AdGenPppGroupIPv6AddressStatus_Type.__name__=_D
_AdGenPppGroupIPv6AddressStatus_Object=MibTableColumn
adGenPppGroupIPv6AddressStatus=_AdGenPppGroupIPv6AddressStatus_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,2,1,1,7),_AdGenPppGroupIPv6AddressStatus_Type())
adGenPppGroupIPv6AddressStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupIPv6AddressStatus.setStatus(_A)
class _AdGenPppGroupIPv6GatewayAddressStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3),('na',4)))
_AdGenPppGroupIPv6GatewayAddressStatus_Type.__name__=_D
_AdGenPppGroupIPv6GatewayAddressStatus_Object=MibTableColumn
adGenPppGroupIPv6GatewayAddressStatus=_AdGenPppGroupIPv6GatewayAddressStatus_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,2,1,1,8),_AdGenPppGroupIPv6GatewayAddressStatus_Type())
adGenPppGroupIPv6GatewayAddressStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupIPv6GatewayAddressStatus.setStatus(_A)
class _AdGenPppGroupIPv6NCPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3),(_c,4),(_d,5),(_e,6),(_f,7),(_g,8),(_h,9),(_W,10)))
_AdGenPppGroupIPv6NCPState_Type.__name__=_D
_AdGenPppGroupIPv6NCPState_Object=MibTableColumn
adGenPppGroupIPv6NCPState=_AdGenPppGroupIPv6NCPState_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,2,1,1,9),_AdGenPppGroupIPv6NCPState_Type())
adGenPppGroupIPv6NCPState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupIPv6NCPState.setStatus(_A)
_AdGenPppGroupPerfStats_ObjectIdentity=ObjectIdentity
adGenPppGroupPerfStats=_AdGenPppGroupPerfStats_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,31,1,2,3))
_AdGenPppGroupPerfTable_Object=MibTable
adGenPppGroupPerfTable=_AdGenPppGroupPerfTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1))
if mibBuilder.loadTexts:adGenPppGroupPerfTable.setStatus(_A)
_AdGenPppGroupPerfEntry_Object=MibTableRow
adGenPppGroupPerfEntry=_AdGenPppGroupPerfEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1,1))
adGenPppGroupPerfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenPppGroupPerfEntry.setStatus(_A)
_AdGenPppGroupInOctets_Type=Counter32
_AdGenPppGroupInOctets_Object=MibTableColumn
adGenPppGroupInOctets=_AdGenPppGroupInOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1,1,1),_AdGenPppGroupInOctets_Type())
adGenPppGroupInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupInOctets.setStatus(_A)
_AdGenPppGroupInPkts_Type=Counter32
_AdGenPppGroupInPkts_Object=MibTableColumn
adGenPppGroupInPkts=_AdGenPppGroupInPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1,1,2),_AdGenPppGroupInPkts_Type())
adGenPppGroupInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupInPkts.setStatus(_A)
_AdGenPppGroupInDiscards_Type=Counter32
_AdGenPppGroupInDiscards_Object=MibTableColumn
adGenPppGroupInDiscards=_AdGenPppGroupInDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1,1,3),_AdGenPppGroupInDiscards_Type())
adGenPppGroupInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupInDiscards.setStatus(_A)
_AdGenPppGroupInErrors_Type=Counter32
_AdGenPppGroupInErrors_Object=MibTableColumn
adGenPppGroupInErrors=_AdGenPppGroupInErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1,1,4),_AdGenPppGroupInErrors_Type())
adGenPppGroupInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupInErrors.setStatus(_A)
_AdGenPppGroupOutOctets_Type=Counter32
_AdGenPppGroupOutOctets_Object=MibTableColumn
adGenPppGroupOutOctets=_AdGenPppGroupOutOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1,1,5),_AdGenPppGroupOutOctets_Type())
adGenPppGroupOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupOutOctets.setStatus(_A)
_AdGenPppGroupOutPkts_Type=Counter32
_AdGenPppGroupOutPkts_Object=MibTableColumn
adGenPppGroupOutPkts=_AdGenPppGroupOutPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1,1,6),_AdGenPppGroupOutPkts_Type())
adGenPppGroupOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupOutPkts.setStatus(_A)
_AdGenPppGroupOutDiscards_Type=Counter32
_AdGenPppGroupOutDiscards_Object=MibTableColumn
adGenPppGroupOutDiscards=_AdGenPppGroupOutDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1,1,7),_AdGenPppGroupOutDiscards_Type())
adGenPppGroupOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupOutDiscards.setStatus(_A)
_AdGenPppGroupOutErrors_Type=Counter32
_AdGenPppGroupOutErrors_Object=MibTableColumn
adGenPppGroupOutErrors=_AdGenPppGroupOutErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1,1,8),_AdGenPppGroupOutErrors_Type())
adGenPppGroupOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupOutErrors.setStatus(_A)
class _AdGenPppGroupValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_AdGenPppGroupValidIntervals_Type.__name__=_D
_AdGenPppGroupValidIntervals_Object=MibTableColumn
adGenPppGroupValidIntervals=_AdGenPppGroupValidIntervals_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1,1,9),_AdGenPppGroupValidIntervals_Type())
adGenPppGroupValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupValidIntervals.setStatus(_A)
class _AdGenPppGroupInvalidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_AdGenPppGroupInvalidIntervals_Type.__name__=_D
_AdGenPppGroupInvalidIntervals_Object=MibTableColumn
adGenPppGroupInvalidIntervals=_AdGenPppGroupInvalidIntervals_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1,1,10),_AdGenPppGroupInvalidIntervals_Type())
adGenPppGroupInvalidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupInvalidIntervals.setStatus(_A)
class _AdGenPppGroupTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_AdGenPppGroupTimeElapsed_Type.__name__=_D
_AdGenPppGroupTimeElapsed_Object=MibTableColumn
adGenPppGroupTimeElapsed=_AdGenPppGroupTimeElapsed_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1,1,11),_AdGenPppGroupTimeElapsed_Type())
adGenPppGroupTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupTimeElapsed.setStatus(_A)
class _AdGenPppGroupResetStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_X,1))
_AdGenPppGroupResetStats_Type.__name__=_D
_AdGenPppGroupResetStats_Object=MibTableColumn
adGenPppGroupResetStats=_AdGenPppGroupResetStats_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1,1,12),_AdGenPppGroupResetStats_Type())
adGenPppGroupResetStats.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupResetStats.setStatus(_A)
class _AdGenPppGroupResetPerfHistory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_X,1))
_AdGenPppGroupResetPerfHistory_Type.__name__=_D
_AdGenPppGroupResetPerfHistory_Object=MibTableColumn
adGenPppGroupResetPerfHistory=_AdGenPppGroupResetPerfHistory_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1,1,13),_AdGenPppGroupResetPerfHistory_Type())
adGenPppGroupResetPerfHistory.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenPppGroupResetPerfHistory.setStatus(_A)
_AdGenPppGroupInL3Pkts_Type=Counter32
_AdGenPppGroupInL3Pkts_Object=MibTableColumn
adGenPppGroupInL3Pkts=_AdGenPppGroupInL3Pkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1,1,14),_AdGenPppGroupInL3Pkts_Type())
adGenPppGroupInL3Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupInL3Pkts.setStatus(_A)
_AdGenPppGroupOutL3Pkts_Type=Counter32
_AdGenPppGroupOutL3Pkts_Object=MibTableColumn
adGenPppGroupOutL3Pkts=_AdGenPppGroupOutL3Pkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,1,1,15),_AdGenPppGroupOutL3Pkts_Type())
adGenPppGroupOutL3Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupOutL3Pkts.setStatus(_A)
_AdGenPppGroupCurrentTable_Object=MibTable
adGenPppGroupCurrentTable=_AdGenPppGroupCurrentTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,2))
if mibBuilder.loadTexts:adGenPppGroupCurrentTable.setStatus(_A)
_AdGenPppGroupCurrentEntry_Object=MibTableRow
adGenPppGroupCurrentEntry=_AdGenPppGroupCurrentEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,2,1))
adGenPppGroupCurrentEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenPppGroupCurrentEntry.setStatus(_A)
_AdGenPppGroupCurrentInOctets_Type=Gauge32
_AdGenPppGroupCurrentInOctets_Object=MibTableColumn
adGenPppGroupCurrentInOctets=_AdGenPppGroupCurrentInOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,2,1,1),_AdGenPppGroupCurrentInOctets_Type())
adGenPppGroupCurrentInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupCurrentInOctets.setStatus(_A)
_AdGenPppGroupCurrentInPkts_Type=Gauge32
_AdGenPppGroupCurrentInPkts_Object=MibTableColumn
adGenPppGroupCurrentInPkts=_AdGenPppGroupCurrentInPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,2,1,2),_AdGenPppGroupCurrentInPkts_Type())
adGenPppGroupCurrentInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupCurrentInPkts.setStatus(_A)
_AdGenPppGroupCurrentInDiscards_Type=Gauge32
_AdGenPppGroupCurrentInDiscards_Object=MibTableColumn
adGenPppGroupCurrentInDiscards=_AdGenPppGroupCurrentInDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,2,1,3),_AdGenPppGroupCurrentInDiscards_Type())
adGenPppGroupCurrentInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupCurrentInDiscards.setStatus(_A)
_AdGenPppGroupCurrentInErrors_Type=Gauge32
_AdGenPppGroupCurrentInErrors_Object=MibTableColumn
adGenPppGroupCurrentInErrors=_AdGenPppGroupCurrentInErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,2,1,4),_AdGenPppGroupCurrentInErrors_Type())
adGenPppGroupCurrentInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupCurrentInErrors.setStatus(_A)
_AdGenPppGroupCurrentOutOctets_Type=Gauge32
_AdGenPppGroupCurrentOutOctets_Object=MibTableColumn
adGenPppGroupCurrentOutOctets=_AdGenPppGroupCurrentOutOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,2,1,5),_AdGenPppGroupCurrentOutOctets_Type())
adGenPppGroupCurrentOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupCurrentOutOctets.setStatus(_A)
_AdGenPppGroupCurrentOutPkts_Type=Gauge32
_AdGenPppGroupCurrentOutPkts_Object=MibTableColumn
adGenPppGroupCurrentOutPkts=_AdGenPppGroupCurrentOutPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,2,1,6),_AdGenPppGroupCurrentOutPkts_Type())
adGenPppGroupCurrentOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupCurrentOutPkts.setStatus(_A)
_AdGenPppGroupCurrentOutDiscards_Type=Gauge32
_AdGenPppGroupCurrentOutDiscards_Object=MibTableColumn
adGenPppGroupCurrentOutDiscards=_AdGenPppGroupCurrentOutDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,2,1,7),_AdGenPppGroupCurrentOutDiscards_Type())
adGenPppGroupCurrentOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupCurrentOutDiscards.setStatus(_A)
_AdGenPppGroupCurrentOutErrors_Type=Gauge32
_AdGenPppGroupCurrentOutErrors_Object=MibTableColumn
adGenPppGroupCurrentOutErrors=_AdGenPppGroupCurrentOutErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,2,1,8),_AdGenPppGroupCurrentOutErrors_Type())
adGenPppGroupCurrentOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupCurrentOutErrors.setStatus(_A)
_AdGenPppGroupCurrentInL3Pkts_Type=Gauge32
_AdGenPppGroupCurrentInL3Pkts_Object=MibTableColumn
adGenPppGroupCurrentInL3Pkts=_AdGenPppGroupCurrentInL3Pkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,2,1,9),_AdGenPppGroupCurrentInL3Pkts_Type())
adGenPppGroupCurrentInL3Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupCurrentInL3Pkts.setStatus(_A)
_AdGenPppGroupCurrentOutL3Pkts_Type=Gauge32
_AdGenPppGroupCurrentOutL3Pkts_Object=MibTableColumn
adGenPppGroupCurrentOutL3Pkts=_AdGenPppGroupCurrentOutL3Pkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,2,1,10),_AdGenPppGroupCurrentOutL3Pkts_Type())
adGenPppGroupCurrentOutL3Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupCurrentOutL3Pkts.setStatus(_A)
_AdGenPppGroupIntervalTable_Object=MibTable
adGenPppGroupIntervalTable=_AdGenPppGroupIntervalTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,3))
if mibBuilder.loadTexts:adGenPppGroupIntervalTable.setStatus(_A)
_AdGenPppGroupIntervalEntry_Object=MibTableRow
adGenPppGroupIntervalEntry=_AdGenPppGroupIntervalEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,3,1))
adGenPppGroupIntervalEntry.setIndexNames((0,_E,_F),(0,_V,_o))
if mibBuilder.loadTexts:adGenPppGroupIntervalEntry.setStatus(_A)
class _AdGenPppGroupIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AdGenPppGroupIntervalNumber_Type.__name__=_D
_AdGenPppGroupIntervalNumber_Object=MibTableColumn
adGenPppGroupIntervalNumber=_AdGenPppGroupIntervalNumber_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,3,1,1),_AdGenPppGroupIntervalNumber_Type())
adGenPppGroupIntervalNumber.setMaxAccess(_Y)
if mibBuilder.loadTexts:adGenPppGroupIntervalNumber.setStatus(_A)
_AdGenPppGroupIntervalInOctets_Type=Gauge32
_AdGenPppGroupIntervalInOctets_Object=MibTableColumn
adGenPppGroupIntervalInOctets=_AdGenPppGroupIntervalInOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,3,1,2),_AdGenPppGroupIntervalInOctets_Type())
adGenPppGroupIntervalInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupIntervalInOctets.setStatus(_A)
_AdGenPppGroupIntervalInPkts_Type=Gauge32
_AdGenPppGroupIntervalInPkts_Object=MibTableColumn
adGenPppGroupIntervalInPkts=_AdGenPppGroupIntervalInPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,3,1,3),_AdGenPppGroupIntervalInPkts_Type())
adGenPppGroupIntervalInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupIntervalInPkts.setStatus(_A)
_AdGenPppGroupIntervalInDiscards_Type=Gauge32
_AdGenPppGroupIntervalInDiscards_Object=MibTableColumn
adGenPppGroupIntervalInDiscards=_AdGenPppGroupIntervalInDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,3,1,4),_AdGenPppGroupIntervalInDiscards_Type())
adGenPppGroupIntervalInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupIntervalInDiscards.setStatus(_A)
_AdGenPppGroupIntervalInErrors_Type=Gauge32
_AdGenPppGroupIntervalInErrors_Object=MibTableColumn
adGenPppGroupIntervalInErrors=_AdGenPppGroupIntervalInErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,3,1,5),_AdGenPppGroupIntervalInErrors_Type())
adGenPppGroupIntervalInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupIntervalInErrors.setStatus(_A)
_AdGenPppGroupIntervalOutOctets_Type=Gauge32
_AdGenPppGroupIntervalOutOctets_Object=MibTableColumn
adGenPppGroupIntervalOutOctets=_AdGenPppGroupIntervalOutOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,3,1,6),_AdGenPppGroupIntervalOutOctets_Type())
adGenPppGroupIntervalOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupIntervalOutOctets.setStatus(_A)
_AdGenPppGroupIntervalOutPkts_Type=Gauge32
_AdGenPppGroupIntervalOutPkts_Object=MibTableColumn
adGenPppGroupIntervalOutPkts=_AdGenPppGroupIntervalOutPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,3,1,7),_AdGenPppGroupIntervalOutPkts_Type())
adGenPppGroupIntervalOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupIntervalOutPkts.setStatus(_A)
_AdGenPppGroupIntervalOutDiscards_Type=Gauge32
_AdGenPppGroupIntervalOutDiscards_Object=MibTableColumn
adGenPppGroupIntervalOutDiscards=_AdGenPppGroupIntervalOutDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,3,1,8),_AdGenPppGroupIntervalOutDiscards_Type())
adGenPppGroupIntervalOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupIntervalOutDiscards.setStatus(_A)
_AdGenPppGroupIntervalOutErrors_Type=Gauge32
_AdGenPppGroupIntervalOutErrors_Object=MibTableColumn
adGenPppGroupIntervalOutErrors=_AdGenPppGroupIntervalOutErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,3,1,9),_AdGenPppGroupIntervalOutErrors_Type())
adGenPppGroupIntervalOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupIntervalOutErrors.setStatus(_A)
_AdGenPppGroupIntervalTimeStamp_Type=DisplayString
_AdGenPppGroupIntervalTimeStamp_Object=MibTableColumn
adGenPppGroupIntervalTimeStamp=_AdGenPppGroupIntervalTimeStamp_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,3,1,10),_AdGenPppGroupIntervalTimeStamp_Type())
adGenPppGroupIntervalTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupIntervalTimeStamp.setStatus(_A)
_AdGenPppGroupIntervalInL3Pkts_Type=Gauge32
_AdGenPppGroupIntervalInL3Pkts_Object=MibTableColumn
adGenPppGroupIntervalInL3Pkts=_AdGenPppGroupIntervalInL3Pkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,3,1,11),_AdGenPppGroupIntervalInL3Pkts_Type())
adGenPppGroupIntervalInL3Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupIntervalInL3Pkts.setStatus(_A)
_AdGenPppGroupIntervalOutL3Pkts_Type=Gauge32
_AdGenPppGroupIntervalOutL3Pkts_Object=MibTableColumn
adGenPppGroupIntervalOutL3Pkts=_AdGenPppGroupIntervalOutL3Pkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,3,1,12),_AdGenPppGroupIntervalOutL3Pkts_Type())
adGenPppGroupIntervalOutL3Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupIntervalOutL3Pkts.setStatus(_A)
_AdGenPppGroupTotalTable_Object=MibTable
adGenPppGroupTotalTable=_AdGenPppGroupTotalTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,4))
if mibBuilder.loadTexts:adGenPppGroupTotalTable.setStatus(_A)
_AdGenPppGroupTotalEntry_Object=MibTableRow
adGenPppGroupTotalEntry=_AdGenPppGroupTotalEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,4,1))
adGenPppGroupTotalEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenPppGroupTotalEntry.setStatus(_A)
_AdGenPppGroupTotalInOctets_Type=Gauge32
_AdGenPppGroupTotalInOctets_Object=MibTableColumn
adGenPppGroupTotalInOctets=_AdGenPppGroupTotalInOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,4,1,1),_AdGenPppGroupTotalInOctets_Type())
adGenPppGroupTotalInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupTotalInOctets.setStatus(_A)
_AdGenPppGroupTotalInPkts_Type=Gauge32
_AdGenPppGroupTotalInPkts_Object=MibTableColumn
adGenPppGroupTotalInPkts=_AdGenPppGroupTotalInPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,4,1,2),_AdGenPppGroupTotalInPkts_Type())
adGenPppGroupTotalInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupTotalInPkts.setStatus(_A)
_AdGenPppGroupTotalInDiscards_Type=Gauge32
_AdGenPppGroupTotalInDiscards_Object=MibTableColumn
adGenPppGroupTotalInDiscards=_AdGenPppGroupTotalInDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,4,1,3),_AdGenPppGroupTotalInDiscards_Type())
adGenPppGroupTotalInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupTotalInDiscards.setStatus(_A)
_AdGenPppGroupTotalInErrors_Type=Gauge32
_AdGenPppGroupTotalInErrors_Object=MibTableColumn
adGenPppGroupTotalInErrors=_AdGenPppGroupTotalInErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,4,1,4),_AdGenPppGroupTotalInErrors_Type())
adGenPppGroupTotalInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupTotalInErrors.setStatus(_A)
_AdGenPppGroupTotalOutOctets_Type=Gauge32
_AdGenPppGroupTotalOutOctets_Object=MibTableColumn
adGenPppGroupTotalOutOctets=_AdGenPppGroupTotalOutOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,4,1,5),_AdGenPppGroupTotalOutOctets_Type())
adGenPppGroupTotalOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupTotalOutOctets.setStatus(_A)
_AdGenPppGroupTotalOutPkts_Type=Gauge32
_AdGenPppGroupTotalOutPkts_Object=MibTableColumn
adGenPppGroupTotalOutPkts=_AdGenPppGroupTotalOutPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,4,1,6),_AdGenPppGroupTotalOutPkts_Type())
adGenPppGroupTotalOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupTotalOutPkts.setStatus(_A)
_AdGenPppGroupTotalOutDiscards_Type=Gauge32
_AdGenPppGroupTotalOutDiscards_Object=MibTableColumn
adGenPppGroupTotalOutDiscards=_AdGenPppGroupTotalOutDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,4,1,7),_AdGenPppGroupTotalOutDiscards_Type())
adGenPppGroupTotalOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupTotalOutDiscards.setStatus(_A)
_AdGenPppGroupTotalOutErrors_Type=Gauge32
_AdGenPppGroupTotalOutErrors_Object=MibTableColumn
adGenPppGroupTotalOutErrors=_AdGenPppGroupTotalOutErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,4,1,8),_AdGenPppGroupTotalOutErrors_Type())
adGenPppGroupTotalOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupTotalOutErrors.setStatus(_A)
_AdGenPppGroupTotalInL3Pkts_Type=Gauge32
_AdGenPppGroupTotalInL3Pkts_Object=MibTableColumn
adGenPppGroupTotalInL3Pkts=_AdGenPppGroupTotalInL3Pkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,4,1,9),_AdGenPppGroupTotalInL3Pkts_Type())
adGenPppGroupTotalInL3Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupTotalInL3Pkts.setStatus(_A)
_AdGenPppGroupTotalOutL3Pkts_Type=Gauge32
_AdGenPppGroupTotalOutL3Pkts_Object=MibTableColumn
adGenPppGroupTotalOutL3Pkts=_AdGenPppGroupTotalOutL3Pkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,4,1,10),_AdGenPppGroupTotalOutL3Pkts_Type())
adGenPppGroupTotalOutL3Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupTotalOutL3Pkts.setStatus(_A)
_AdGenPppGroupDayCurrentTable_Object=MibTable
adGenPppGroupDayCurrentTable=_AdGenPppGroupDayCurrentTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,5))
if mibBuilder.loadTexts:adGenPppGroupDayCurrentTable.setStatus(_A)
_AdGenPppGroupDayCurrentEntry_Object=MibTableRow
adGenPppGroupDayCurrentEntry=_AdGenPppGroupDayCurrentEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,5,1))
adGenPppGroupDayCurrentEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenPppGroupDayCurrentEntry.setStatus(_A)
_AdGenPppGroupDayCurrentInOctets_Type=Gauge32
_AdGenPppGroupDayCurrentInOctets_Object=MibTableColumn
adGenPppGroupDayCurrentInOctets=_AdGenPppGroupDayCurrentInOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,5,1,1),_AdGenPppGroupDayCurrentInOctets_Type())
adGenPppGroupDayCurrentInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayCurrentInOctets.setStatus(_A)
_AdGenPppGroupDayCurrentInPkts_Type=Gauge32
_AdGenPppGroupDayCurrentInPkts_Object=MibTableColumn
adGenPppGroupDayCurrentInPkts=_AdGenPppGroupDayCurrentInPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,5,1,2),_AdGenPppGroupDayCurrentInPkts_Type())
adGenPppGroupDayCurrentInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayCurrentInPkts.setStatus(_A)
_AdGenPppGroupDayCurrentInDiscards_Type=Gauge32
_AdGenPppGroupDayCurrentInDiscards_Object=MibTableColumn
adGenPppGroupDayCurrentInDiscards=_AdGenPppGroupDayCurrentInDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,5,1,3),_AdGenPppGroupDayCurrentInDiscards_Type())
adGenPppGroupDayCurrentInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayCurrentInDiscards.setStatus(_A)
_AdGenPppGroupDayCurrentInErrors_Type=Gauge32
_AdGenPppGroupDayCurrentInErrors_Object=MibTableColumn
adGenPppGroupDayCurrentInErrors=_AdGenPppGroupDayCurrentInErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,5,1,4),_AdGenPppGroupDayCurrentInErrors_Type())
adGenPppGroupDayCurrentInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayCurrentInErrors.setStatus(_A)
_AdGenPppGroupDayCurrentOutOctets_Type=Gauge32
_AdGenPppGroupDayCurrentOutOctets_Object=MibTableColumn
adGenPppGroupDayCurrentOutOctets=_AdGenPppGroupDayCurrentOutOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,5,1,5),_AdGenPppGroupDayCurrentOutOctets_Type())
adGenPppGroupDayCurrentOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayCurrentOutOctets.setStatus(_A)
_AdGenPppGroupDayCurrentOutPkts_Type=Gauge32
_AdGenPppGroupDayCurrentOutPkts_Object=MibTableColumn
adGenPppGroupDayCurrentOutPkts=_AdGenPppGroupDayCurrentOutPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,5,1,6),_AdGenPppGroupDayCurrentOutPkts_Type())
adGenPppGroupDayCurrentOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayCurrentOutPkts.setStatus(_A)
_AdGenPppGroupDayCurrentOutDiscards_Type=Gauge32
_AdGenPppGroupDayCurrentOutDiscards_Object=MibTableColumn
adGenPppGroupDayCurrentOutDiscards=_AdGenPppGroupDayCurrentOutDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,5,1,7),_AdGenPppGroupDayCurrentOutDiscards_Type())
adGenPppGroupDayCurrentOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayCurrentOutDiscards.setStatus(_A)
_AdGenPppGroupDayCurrentOutErrors_Type=Gauge32
_AdGenPppGroupDayCurrentOutErrors_Object=MibTableColumn
adGenPppGroupDayCurrentOutErrors=_AdGenPppGroupDayCurrentOutErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,5,1,8),_AdGenPppGroupDayCurrentOutErrors_Type())
adGenPppGroupDayCurrentOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayCurrentOutErrors.setStatus(_A)
_AdGenPppGroupDayCurrentInL3Pkts_Type=Gauge32
_AdGenPppGroupDayCurrentInL3Pkts_Object=MibTableColumn
adGenPppGroupDayCurrentInL3Pkts=_AdGenPppGroupDayCurrentInL3Pkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,5,1,9),_AdGenPppGroupDayCurrentInL3Pkts_Type())
adGenPppGroupDayCurrentInL3Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayCurrentInL3Pkts.setStatus(_A)
_AdGenPppGroupDayCurrentOutL3Pkts_Type=Gauge32
_AdGenPppGroupDayCurrentOutL3Pkts_Object=MibTableColumn
adGenPppGroupDayCurrentOutL3Pkts=_AdGenPppGroupDayCurrentOutL3Pkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,5,1,10),_AdGenPppGroupDayCurrentOutL3Pkts_Type())
adGenPppGroupDayCurrentOutL3Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayCurrentOutL3Pkts.setStatus(_A)
_AdGenPppGroupDayIntervalTable_Object=MibTable
adGenPppGroupDayIntervalTable=_AdGenPppGroupDayIntervalTable_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,6))
if mibBuilder.loadTexts:adGenPppGroupDayIntervalTable.setStatus(_A)
_AdGenPppGroupDayIntervalEntry_Object=MibTableRow
adGenPppGroupDayIntervalEntry=_AdGenPppGroupDayIntervalEntry_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,6,1))
adGenPppGroupDayIntervalEntry.setIndexNames((0,_E,_F),(0,_V,_p))
if mibBuilder.loadTexts:adGenPppGroupDayIntervalEntry.setStatus(_A)
class _AdGenPppGroupDayIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_AdGenPppGroupDayIntervalNumber_Type.__name__=_D
_AdGenPppGroupDayIntervalNumber_Object=MibTableColumn
adGenPppGroupDayIntervalNumber=_AdGenPppGroupDayIntervalNumber_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,6,1,1),_AdGenPppGroupDayIntervalNumber_Type())
adGenPppGroupDayIntervalNumber.setMaxAccess(_Y)
if mibBuilder.loadTexts:adGenPppGroupDayIntervalNumber.setStatus(_A)
_AdGenPppGroupDayIntervalInOctets_Type=Gauge32
_AdGenPppGroupDayIntervalInOctets_Object=MibTableColumn
adGenPppGroupDayIntervalInOctets=_AdGenPppGroupDayIntervalInOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,6,1,2),_AdGenPppGroupDayIntervalInOctets_Type())
adGenPppGroupDayIntervalInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayIntervalInOctets.setStatus(_A)
_AdGenPppGroupDayIntervalInPkts_Type=Gauge32
_AdGenPppGroupDayIntervalInPkts_Object=MibTableColumn
adGenPppGroupDayIntervalInPkts=_AdGenPppGroupDayIntervalInPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,6,1,3),_AdGenPppGroupDayIntervalInPkts_Type())
adGenPppGroupDayIntervalInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayIntervalInPkts.setStatus(_A)
_AdGenPppGroupDayIntervalInDiscards_Type=Gauge32
_AdGenPppGroupDayIntervalInDiscards_Object=MibTableColumn
adGenPppGroupDayIntervalInDiscards=_AdGenPppGroupDayIntervalInDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,6,1,4),_AdGenPppGroupDayIntervalInDiscards_Type())
adGenPppGroupDayIntervalInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayIntervalInDiscards.setStatus(_A)
_AdGenPppGroupDayIntervalInErrors_Type=Gauge32
_AdGenPppGroupDayIntervalInErrors_Object=MibTableColumn
adGenPppGroupDayIntervalInErrors=_AdGenPppGroupDayIntervalInErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,6,1,5),_AdGenPppGroupDayIntervalInErrors_Type())
adGenPppGroupDayIntervalInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayIntervalInErrors.setStatus(_A)
_AdGenPppGroupDayIntervalOutOctets_Type=Gauge32
_AdGenPppGroupDayIntervalOutOctets_Object=MibTableColumn
adGenPppGroupDayIntervalOutOctets=_AdGenPppGroupDayIntervalOutOctets_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,6,1,6),_AdGenPppGroupDayIntervalOutOctets_Type())
adGenPppGroupDayIntervalOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayIntervalOutOctets.setStatus(_A)
_AdGenPppGroupDayIntervalOutPkts_Type=Gauge32
_AdGenPppGroupDayIntervalOutPkts_Object=MibTableColumn
adGenPppGroupDayIntervalOutPkts=_AdGenPppGroupDayIntervalOutPkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,6,1,7),_AdGenPppGroupDayIntervalOutPkts_Type())
adGenPppGroupDayIntervalOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayIntervalOutPkts.setStatus(_A)
_AdGenPppGroupDayIntervalOutDiscards_Type=Gauge32
_AdGenPppGroupDayIntervalOutDiscards_Object=MibTableColumn
adGenPppGroupDayIntervalOutDiscards=_AdGenPppGroupDayIntervalOutDiscards_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,6,1,8),_AdGenPppGroupDayIntervalOutDiscards_Type())
adGenPppGroupDayIntervalOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayIntervalOutDiscards.setStatus(_A)
_AdGenPppGroupDayIntervalOutErrors_Type=Gauge32
_AdGenPppGroupDayIntervalOutErrors_Object=MibTableColumn
adGenPppGroupDayIntervalOutErrors=_AdGenPppGroupDayIntervalOutErrors_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,6,1,9),_AdGenPppGroupDayIntervalOutErrors_Type())
adGenPppGroupDayIntervalOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayIntervalOutErrors.setStatus(_A)
_AdGenPppGroupDayIntervalTimeStamp_Type=DisplayString
_AdGenPppGroupDayIntervalTimeStamp_Object=MibTableColumn
adGenPppGroupDayIntervalTimeStamp=_AdGenPppGroupDayIntervalTimeStamp_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,6,1,10),_AdGenPppGroupDayIntervalTimeStamp_Type())
adGenPppGroupDayIntervalTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayIntervalTimeStamp.setStatus(_A)
_AdGenPppGroupDayIntervalInL3Pkts_Type=Gauge32
_AdGenPppGroupDayIntervalInL3Pkts_Object=MibTableColumn
adGenPppGroupDayIntervalInL3Pkts=_AdGenPppGroupDayIntervalInL3Pkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,6,1,11),_AdGenPppGroupDayIntervalInL3Pkts_Type())
adGenPppGroupDayIntervalInL3Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayIntervalInL3Pkts.setStatus(_A)
_AdGenPppGroupDayIntervalOutL3Pkts_Type=Gauge32
_AdGenPppGroupDayIntervalOutL3Pkts_Object=MibTableColumn
adGenPppGroupDayIntervalOutL3Pkts=_AdGenPppGroupDayIntervalOutL3Pkts_Object((1,3,6,1,4,1,664,5,67,1,31,1,2,3,6,1,12),_AdGenPppGroupDayIntervalOutL3Pkts_Type())
adGenPppGroupDayIntervalOutL3Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPppGroupDayIntervalOutL3Pkts.setStatus(_A)
_AdGenPppAlarmsPrefix_ObjectIdentity=ObjectIdentity
adGenPppAlarmsPrefix=_AdGenPppAlarmsPrefix_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,31,2))
_AdGenPppAlarms_ObjectIdentity=ObjectIdentity
adGenPppAlarms=_AdGenPppAlarms_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,31,2,0))
adGenPppLinkLcpDownAlarmClr=NotificationType((1,3,6,1,4,1,664,5,67,1,31,2,0,2))
adGenPppLinkLcpDownAlarmClr.setObjects(*((_J,_K),(_N,_O),(_G,_H),(_E,_F),(_L,_M)))
if mibBuilder.loadTexts:adGenPppLinkLcpDownAlarmClr.setStatus(_A)
adGenPppLinkLcpDownAlarmAct=NotificationType((1,3,6,1,4,1,664,5,67,1,31,2,0,3))
adGenPppLinkLcpDownAlarmAct.setObjects(*((_J,_K),(_N,_O),(_G,_H),(_E,_F),(_L,_M)))
if mibBuilder.loadTexts:adGenPppLinkLcpDownAlarmAct.setStatus(_A)
adGenPppGroupNcpDownAlarmClr=NotificationType((1,3,6,1,4,1,664,5,67,1,31,2,0,4))
adGenPppGroupNcpDownAlarmClr.setObjects(*((_J,_K),(_N,_O),(_G,_H),(_E,_F),(_L,_M)))
if mibBuilder.loadTexts:adGenPppGroupNcpDownAlarmClr.setStatus(_A)
adGenPppGroupNcpDownAlarmAct=NotificationType((1,3,6,1,4,1,664,5,67,1,31,2,0,5))
adGenPppGroupNcpDownAlarmAct.setObjects(*((_J,_K),(_N,_O),(_G,_H),(_E,_F),(_L,_M)))
if mibBuilder.loadTexts:adGenPppGroupNcpDownAlarmAct.setStatus(_A)
adGenPppGroupIpv6NcpDownAlarmClr=NotificationType((1,3,6,1,4,1,664,5,67,1,31,2,0,6))
adGenPppGroupIpv6NcpDownAlarmClr.setObjects(*((_J,_K),(_N,_O),(_G,_H),(_E,_F),(_L,_M)))
if mibBuilder.loadTexts:adGenPppGroupIpv6NcpDownAlarmClr.setStatus(_A)
adGenPppGroupIpv6NcpDownAlarmAct=NotificationType((1,3,6,1,4,1,664,5,67,1,31,2,0,7))
adGenPppGroupIpv6NcpDownAlarmAct.setObjects(*((_J,_K),(_N,_O),(_G,_H),(_E,_F),(_L,_M)))
if mibBuilder.loadTexts:adGenPppGroupIpv6NcpDownAlarmAct.setStatus(_A)
adGenPppGroupIpv6AddrMismatchAlarmClr=NotificationType((1,3,6,1,4,1,664,5,67,1,31,2,0,8))
adGenPppGroupIpv6AddrMismatchAlarmClr.setObjects(*((_J,_K),(_N,_O),(_G,_H),(_E,_F),(_L,_M)))
if mibBuilder.loadTexts:adGenPppGroupIpv6AddrMismatchAlarmClr.setStatus(_A)
adGenPppGroupIpv6AddrMismatchAlarmAct=NotificationType((1,3,6,1,4,1,664,5,67,1,31,2,0,9))
adGenPppGroupIpv6AddrMismatchAlarmAct.setObjects(*((_J,_K),(_N,_O),(_G,_H),(_E,_F),(_L,_M)))
if mibBuilder.loadTexts:adGenPppGroupIpv6AddrMismatchAlarmAct.setStatus(_A)
adGenPppGroupIpv6GatewayAddrMismatchAlarmClr=NotificationType((1,3,6,1,4,1,664,5,67,1,31,2,0,10))
adGenPppGroupIpv6GatewayAddrMismatchAlarmClr.setObjects(*((_J,_K),(_N,_O),(_G,_H),(_E,_F),(_L,_M)))
if mibBuilder.loadTexts:adGenPppGroupIpv6GatewayAddrMismatchAlarmClr.setStatus(_A)
adGenPppGroupIpv6GatewayAddrMismatchAlarmAct=NotificationType((1,3,6,1,4,1,664,5,67,1,31,2,0,11))
adGenPppGroupIpv6GatewayAddrMismatchAlarmAct.setObjects(*((_J,_K),(_N,_O),(_G,_H),(_E,_F),(_L,_M)))
if mibBuilder.loadTexts:adGenPppGroupIpv6GatewayAddrMismatchAlarmAct.setStatus(_A)
mibBuilder.exportSymbols(_V,**{'adGenPppMIBObjects':adGenPppMIBObjects,'adGenPppLinkObjects':adGenPppLinkObjects,'adGenPppLinkProv':adGenPppLinkProv,'adGenPppLinkAlarmProvTable':adGenPppLinkAlarmProvTable,'adGenPppLinkAlarmProvEntry':adGenPppLinkAlarmProvEntry,'adGenPppLinkAlarmProvLCPAlarmSeverity':adGenPppLinkAlarmProvLCPAlarmSeverity,'adGenPppLinkAlarmProvLCPAlarmSuppression':adGenPppLinkAlarmProvLCPAlarmSuppression,'adGenPppLinkAlarmProvLCPAlarmEnable':adGenPppLinkAlarmProvLCPAlarmEnable,'adGenPppLinkStatus':adGenPppLinkStatus,'adGenPppLinkStatusTable':adGenPppLinkStatusTable,'adGenPppLinkStatusEntry':adGenPppLinkStatusEntry,'adGenPppLinkOperStatus':adGenPppLinkOperStatus,'adGenPppLinkCurrentLCPState':adGenPppLinkCurrentLCPState,'adGenPppLinkNegotiatedStatus':adGenPppLinkNegotiatedStatus,'adGenPppLinkPerfStats':adGenPppLinkPerfStats,'adGenPppLinkPerfTable':adGenPppLinkPerfTable,'adGenPppLinkPerfEntry':adGenPppLinkPerfEntry,'adGenPppLinkInOctets':adGenPppLinkInOctets,'adGenPppLinkInGoodOctets':adGenPppLinkInGoodOctets,'adGenPppLinkInPkts':adGenPppLinkInPkts,'adGenPppLinkInDiscards':adGenPppLinkInDiscards,'adGenPppLinkInErrors':adGenPppLinkInErrors,'adGenPppLinkOutOctets':adGenPppLinkOutOctets,'adGenPppLinkOutPkts':adGenPppLinkOutPkts,'adGenPppLinkOutDiscards':adGenPppLinkOutDiscards,'adGenPppLinkOutErrors':adGenPppLinkOutErrors,'adGenPppLinkValidIntervals':adGenPppLinkValidIntervals,'adGenPppLinkInvalidIntervals':adGenPppLinkInvalidIntervals,'adGenPppLinkTimeElapsed':adGenPppLinkTimeElapsed,'adGenPppLinkResetStats':adGenPppLinkResetStats,'adGenPppLinkResetPerfHistory':adGenPppLinkResetPerfHistory,'adGenPppLinkCurrentTable':adGenPppLinkCurrentTable,'adGenPppLinkCurrentEntry':adGenPppLinkCurrentEntry,'adGenPppLinkCurrentInOctets':adGenPppLinkCurrentInOctets,'adGenPppLinkCurrentInGoodOctets':adGenPppLinkCurrentInGoodOctets,'adGenPppLinkCurrentInPkts':adGenPppLinkCurrentInPkts,'adGenPppLinkCurrentInDiscards':adGenPppLinkCurrentInDiscards,'adGenPppLinkCurrentInErrors':adGenPppLinkCurrentInErrors,'adGenPppLinkCurrentOutOctets':adGenPppLinkCurrentOutOctets,'adGenPppLinkCurrentOutPkts':adGenPppLinkCurrentOutPkts,'adGenPppLinkCurrentOutDiscards':adGenPppLinkCurrentOutDiscards,'adGenPppLinkCurrentOutErrors':adGenPppLinkCurrentOutErrors,'adGenPppLinkIntervalTable':adGenPppLinkIntervalTable,'adGenPppLinkIntervalEntry':adGenPppLinkIntervalEntry,_j:adGenPppLinkIntervalNumber,'adGenPppLinkIntervalInOctets':adGenPppLinkIntervalInOctets,'adGenPppLinkIntervalInGoodOctets':adGenPppLinkIntervalInGoodOctets,'adGenPppLinkIntervalInPkts':adGenPppLinkIntervalInPkts,'adGenPppLinkIntervalInDiscards':adGenPppLinkIntervalInDiscards,'adGenPppLinkIntervalInErrors':adGenPppLinkIntervalInErrors,'adGenPppLinkIntervalOutOctets':adGenPppLinkIntervalOutOctets,'adGenPppLinkIntervalOutPkts':adGenPppLinkIntervalOutPkts,'adGenPppLinkIntervalOutDiscards':adGenPppLinkIntervalOutDiscards,'adGenPppLinkIntervalOutErrors':adGenPppLinkIntervalOutErrors,'adGenPppLinkIntervalTimeStamp':adGenPppLinkIntervalTimeStamp,'adGenPppLinkTotalTable':adGenPppLinkTotalTable,'adGenPppLinkTotalEntry':adGenPppLinkTotalEntry,'adGenPppLinkTotalInOctets':adGenPppLinkTotalInOctets,'adGenPppLinkTotalInGoodOctets':adGenPppLinkTotalInGoodOctets,'adGenPppLinkTotalInPkts':adGenPppLinkTotalInPkts,'adGenPppLinkTotalInDiscards':adGenPppLinkTotalInDiscards,'adGenPppLinkTotalInErrors':adGenPppLinkTotalInErrors,'adGenPppLinkTotalOutOctets':adGenPppLinkTotalOutOctets,'adGenPppLinkTotalOutPkts':adGenPppLinkTotalOutPkts,'adGenPppLinkTotalOutDiscards':adGenPppLinkTotalOutDiscards,'adGenPppLinkTotalOutErrors':adGenPppLinkTotalOutErrors,'adGenPppLinkDayCurrentTable':adGenPppLinkDayCurrentTable,'adGenPppLinkDayCurrentEntry':adGenPppLinkDayCurrentEntry,'adGenPppLinkDayCurrentInOctets':adGenPppLinkDayCurrentInOctets,'adGenPppLinkDayCurrentInGoodOctets':adGenPppLinkDayCurrentInGoodOctets,'adGenPppLinkDayCurrentInPkts':adGenPppLinkDayCurrentInPkts,'adGenPppLinkDayCurrentInDiscards':adGenPppLinkDayCurrentInDiscards,'adGenPppLinkDayCurrentInErrors':adGenPppLinkDayCurrentInErrors,'adGenPppLinkDayCurrentOutOctets':adGenPppLinkDayCurrentOutOctets,'adGenPppLinkDayCurrentOutPkts':adGenPppLinkDayCurrentOutPkts,'adGenPppLinkDayCurrentOutDiscards':adGenPppLinkDayCurrentOutDiscards,'adGenPppLinkDayCurrentOutErrors':adGenPppLinkDayCurrentOutErrors,'adGenPppLinkDayIntervalTable':adGenPppLinkDayIntervalTable,'adGenPppLinkDayIntervalEntry':adGenPppLinkDayIntervalEntry,_k:adGenPppLinkDayIntervalNumber,'adGenPppLinkDayIntervalInOctets':adGenPppLinkDayIntervalInOctets,'adGenPppLinkDayIntervalInGoodOctets':adGenPppLinkDayIntervalInGoodOctets,'adGenPppLinkDayIntervalInPkts':adGenPppLinkDayIntervalInPkts,'adGenPppLinkDayIntervalInDiscards':adGenPppLinkDayIntervalInDiscards,'adGenPppLinkDayIntervalInErrors':adGenPppLinkDayIntervalInErrors,'adGenPppLinkDayIntervalOutOctets':adGenPppLinkDayIntervalOutOctets,'adGenPppLinkDayIntervalOutPkts':adGenPppLinkDayIntervalOutPkts,'adGenPppLinkDayIntervalOutDiscards':adGenPppLinkDayIntervalOutDiscards,'adGenPppLinkDayIntervalOutErrors':adGenPppLinkDayIntervalOutErrors,'adGenPppLinkDayIntervalTimeStamp':adGenPppLinkDayIntervalTimeStamp,'adGenPppGroupObjects':adGenPppGroupObjects,'adGenPppGroupProv':adGenPppGroupProv,'adGenPppGroupProvTable':adGenPppGroupProvTable,'adGenPppGroupProvEntry':adGenPppGroupProvEntry,'adGenPppGroupSubscriberIpAddress':adGenPppGroupSubscriberIpAddress,'adGenPppGroupGatewayIpAddress':adGenPppGroupGatewayIpAddress,'adGenPppGroupPrimaryDNSIpAddress':adGenPppGroupPrimaryDNSIpAddress,'adGenPppGroupSecondaryDNSIpAddress':adGenPppGroupSecondaryDNSIpAddress,'adGenPppGroupConfigInitialMRU':adGenPppGroupConfigInitialMRU,'adGenPppGroupConfigMagicNumber':adGenPppGroupConfigMagicNumber,'adGenPppGroupConfigFcsSize':adGenPppGroupConfigFcsSize,'adGenPppGroupConfigACCompression':adGenPppGroupConfigACCompression,'adGenPppGroupConfigPFCompression':adGenPppGroupConfigPFCompression,'adGenPppGroupConfigLQM':adGenPppGroupConfigLQM,'adGenPppGroupConfigRestartTimer':adGenPppGroupConfigRestartTimer,'adGenPppGroupConfigMaxTerminate':adGenPppGroupConfigMaxTerminate,'adGenPppGroupConfigMaxConfigure':adGenPppGroupConfigMaxConfigure,'adGenPppGroupConfigMaxFailure':adGenPppGroupConfigMaxFailure,'adGenPppGroupConfigKeepAliveRate':adGenPppGroupConfigKeepAliveRate,'adGenPppGroupChapEnabled':adGenPppGroupChapEnabled,'adGenPppGroupLocalUserName':adGenPppGroupLocalUserName,'adGenPppGroupLocalPassword':adGenPppGroupLocalPassword,'adGenPppGroupPeerUserName':adGenPppGroupPeerUserName,'adGenPppGroupPeerPassword':adGenPppGroupPeerPassword,'adGenPppGroupIpAddressAssignment':adGenPppGroupIpAddressAssignment,'adGenPppGroupDhcpClientIdentfier':adGenPppGroupDhcpClientIdentfier,'adGenPppGroupDhcpHostname':adGenPppGroupDhcpHostname,'adGenPppGroupConfigMultilink':adGenPppGroupConfigMultilink,'adGenPppGroupSubscriberIPv6Address':adGenPppGroupSubscriberIPv6Address,'adGenPppGroupGatewayIPv6AddressAssignment':adGenPppGroupGatewayIPv6AddressAssignment,'adGenPppGroupGatewayIPv6Address':adGenPppGroupGatewayIPv6Address,'adGenPppGroupIpEnabled':adGenPppGroupIpEnabled,'adGenPppGroupIpv6Enabled':adGenPppGroupIpv6Enabled,'adGenPppGroupAlarmProvTable':adGenPppGroupAlarmProvTable,'adGenPppGroupAlarmProvEntry':adGenPppGroupAlarmProvEntry,'adGenPppGroupAlarmProvNCPAlarmSeverity':adGenPppGroupAlarmProvNCPAlarmSeverity,'adGenPppGroupAlarmProvNCPAlarmSuppression':adGenPppGroupAlarmProvNCPAlarmSuppression,'adGenPppGroupAlarmProvNCPAlarmEnable':adGenPppGroupAlarmProvNCPAlarmEnable,'adGenPppGroupAlarmProvIpv6NcpAlarmSeverity':adGenPppGroupAlarmProvIpv6NcpAlarmSeverity,'adGenPppGroupAlarmProvIpv6NcpAlarmSuppression':adGenPppGroupAlarmProvIpv6NcpAlarmSuppression,'adGenPppGroupAlarmProvIpv6NcpAlarmEnable':adGenPppGroupAlarmProvIpv6NcpAlarmEnable,'adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity':adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity,'adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression':adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression,'adGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable':adGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable,'adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity':adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity,'adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression':adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression,'adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable':adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable,'adGenPppGroupStatus':adGenPppGroupStatus,'adGenPppGroupStatusTable':adGenPppGroupStatusTable,'adGenPppGroupStatusEntry':adGenPppGroupStatusEntry,'adGenPppGroupNCPState':adGenPppGroupNCPState,'adGenPppGroupCurrentSubscriberIpAddress':adGenPppGroupCurrentSubscriberIpAddress,'adGenPppGroupCurrentGatewayIpAddress':adGenPppGroupCurrentGatewayIpAddress,'adGenPppGroupCurrentPrimaryDNSIpAddress':adGenPppGroupCurrentPrimaryDNSIpAddress,'adGenPppGroupCurrentSecondaryDNSIpAddress':adGenPppGroupCurrentSecondaryDNSIpAddress,'adGenPppGroupNegotiatedStatus':adGenPppGroupNegotiatedStatus,'adGenPppGroupIPv6AddressStatus':adGenPppGroupIPv6AddressStatus,'adGenPppGroupIPv6GatewayAddressStatus':adGenPppGroupIPv6GatewayAddressStatus,'adGenPppGroupIPv6NCPState':adGenPppGroupIPv6NCPState,'adGenPppGroupPerfStats':adGenPppGroupPerfStats,'adGenPppGroupPerfTable':adGenPppGroupPerfTable,'adGenPppGroupPerfEntry':adGenPppGroupPerfEntry,'adGenPppGroupInOctets':adGenPppGroupInOctets,'adGenPppGroupInPkts':adGenPppGroupInPkts,'adGenPppGroupInDiscards':adGenPppGroupInDiscards,'adGenPppGroupInErrors':adGenPppGroupInErrors,'adGenPppGroupOutOctets':adGenPppGroupOutOctets,'adGenPppGroupOutPkts':adGenPppGroupOutPkts,'adGenPppGroupOutDiscards':adGenPppGroupOutDiscards,'adGenPppGroupOutErrors':adGenPppGroupOutErrors,'adGenPppGroupValidIntervals':adGenPppGroupValidIntervals,'adGenPppGroupInvalidIntervals':adGenPppGroupInvalidIntervals,'adGenPppGroupTimeElapsed':adGenPppGroupTimeElapsed,'adGenPppGroupResetStats':adGenPppGroupResetStats,'adGenPppGroupResetPerfHistory':adGenPppGroupResetPerfHistory,'adGenPppGroupInL3Pkts':adGenPppGroupInL3Pkts,'adGenPppGroupOutL3Pkts':adGenPppGroupOutL3Pkts,'adGenPppGroupCurrentTable':adGenPppGroupCurrentTable,'adGenPppGroupCurrentEntry':adGenPppGroupCurrentEntry,'adGenPppGroupCurrentInOctets':adGenPppGroupCurrentInOctets,'adGenPppGroupCurrentInPkts':adGenPppGroupCurrentInPkts,'adGenPppGroupCurrentInDiscards':adGenPppGroupCurrentInDiscards,'adGenPppGroupCurrentInErrors':adGenPppGroupCurrentInErrors,'adGenPppGroupCurrentOutOctets':adGenPppGroupCurrentOutOctets,'adGenPppGroupCurrentOutPkts':adGenPppGroupCurrentOutPkts,'adGenPppGroupCurrentOutDiscards':adGenPppGroupCurrentOutDiscards,'adGenPppGroupCurrentOutErrors':adGenPppGroupCurrentOutErrors,'adGenPppGroupCurrentInL3Pkts':adGenPppGroupCurrentInL3Pkts,'adGenPppGroupCurrentOutL3Pkts':adGenPppGroupCurrentOutL3Pkts,'adGenPppGroupIntervalTable':adGenPppGroupIntervalTable,'adGenPppGroupIntervalEntry':adGenPppGroupIntervalEntry,_o:adGenPppGroupIntervalNumber,'adGenPppGroupIntervalInOctets':adGenPppGroupIntervalInOctets,'adGenPppGroupIntervalInPkts':adGenPppGroupIntervalInPkts,'adGenPppGroupIntervalInDiscards':adGenPppGroupIntervalInDiscards,'adGenPppGroupIntervalInErrors':adGenPppGroupIntervalInErrors,'adGenPppGroupIntervalOutOctets':adGenPppGroupIntervalOutOctets,'adGenPppGroupIntervalOutPkts':adGenPppGroupIntervalOutPkts,'adGenPppGroupIntervalOutDiscards':adGenPppGroupIntervalOutDiscards,'adGenPppGroupIntervalOutErrors':adGenPppGroupIntervalOutErrors,'adGenPppGroupIntervalTimeStamp':adGenPppGroupIntervalTimeStamp,'adGenPppGroupIntervalInL3Pkts':adGenPppGroupIntervalInL3Pkts,'adGenPppGroupIntervalOutL3Pkts':adGenPppGroupIntervalOutL3Pkts,'adGenPppGroupTotalTable':adGenPppGroupTotalTable,'adGenPppGroupTotalEntry':adGenPppGroupTotalEntry,'adGenPppGroupTotalInOctets':adGenPppGroupTotalInOctets,'adGenPppGroupTotalInPkts':adGenPppGroupTotalInPkts,'adGenPppGroupTotalInDiscards':adGenPppGroupTotalInDiscards,'adGenPppGroupTotalInErrors':adGenPppGroupTotalInErrors,'adGenPppGroupTotalOutOctets':adGenPppGroupTotalOutOctets,'adGenPppGroupTotalOutPkts':adGenPppGroupTotalOutPkts,'adGenPppGroupTotalOutDiscards':adGenPppGroupTotalOutDiscards,'adGenPppGroupTotalOutErrors':adGenPppGroupTotalOutErrors,'adGenPppGroupTotalInL3Pkts':adGenPppGroupTotalInL3Pkts,'adGenPppGroupTotalOutL3Pkts':adGenPppGroupTotalOutL3Pkts,'adGenPppGroupDayCurrentTable':adGenPppGroupDayCurrentTable,'adGenPppGroupDayCurrentEntry':adGenPppGroupDayCurrentEntry,'adGenPppGroupDayCurrentInOctets':adGenPppGroupDayCurrentInOctets,'adGenPppGroupDayCurrentInPkts':adGenPppGroupDayCurrentInPkts,'adGenPppGroupDayCurrentInDiscards':adGenPppGroupDayCurrentInDiscards,'adGenPppGroupDayCurrentInErrors':adGenPppGroupDayCurrentInErrors,'adGenPppGroupDayCurrentOutOctets':adGenPppGroupDayCurrentOutOctets,'adGenPppGroupDayCurrentOutPkts':adGenPppGroupDayCurrentOutPkts,'adGenPppGroupDayCurrentOutDiscards':adGenPppGroupDayCurrentOutDiscards,'adGenPppGroupDayCurrentOutErrors':adGenPppGroupDayCurrentOutErrors,'adGenPppGroupDayCurrentInL3Pkts':adGenPppGroupDayCurrentInL3Pkts,'adGenPppGroupDayCurrentOutL3Pkts':adGenPppGroupDayCurrentOutL3Pkts,'adGenPppGroupDayIntervalTable':adGenPppGroupDayIntervalTable,'adGenPppGroupDayIntervalEntry':adGenPppGroupDayIntervalEntry,_p:adGenPppGroupDayIntervalNumber,'adGenPppGroupDayIntervalInOctets':adGenPppGroupDayIntervalInOctets,'adGenPppGroupDayIntervalInPkts':adGenPppGroupDayIntervalInPkts,'adGenPppGroupDayIntervalInDiscards':adGenPppGroupDayIntervalInDiscards,'adGenPppGroupDayIntervalInErrors':adGenPppGroupDayIntervalInErrors,'adGenPppGroupDayIntervalOutOctets':adGenPppGroupDayIntervalOutOctets,'adGenPppGroupDayIntervalOutPkts':adGenPppGroupDayIntervalOutPkts,'adGenPppGroupDayIntervalOutDiscards':adGenPppGroupDayIntervalOutDiscards,'adGenPppGroupDayIntervalOutErrors':adGenPppGroupDayIntervalOutErrors,'adGenPppGroupDayIntervalTimeStamp':adGenPppGroupDayIntervalTimeStamp,'adGenPppGroupDayIntervalInL3Pkts':adGenPppGroupDayIntervalInL3Pkts,'adGenPppGroupDayIntervalOutL3Pkts':adGenPppGroupDayIntervalOutL3Pkts,'adGenPppAlarmsPrefix':adGenPppAlarmsPrefix,'adGenPppAlarms':adGenPppAlarms,'adGenPppLinkLcpDownAlarmClr':adGenPppLinkLcpDownAlarmClr,'adGenPppLinkLcpDownAlarmAct':adGenPppLinkLcpDownAlarmAct,'adGenPppGroupNcpDownAlarmClr':adGenPppGroupNcpDownAlarmClr,'adGenPppGroupNcpDownAlarmAct':adGenPppGroupNcpDownAlarmAct,'adGenPppGroupIpv6NcpDownAlarmClr':adGenPppGroupIpv6NcpDownAlarmClr,'adGenPppGroupIpv6NcpDownAlarmAct':adGenPppGroupIpv6NcpDownAlarmAct,'adGenPppGroupIpv6AddrMismatchAlarmClr':adGenPppGroupIpv6AddrMismatchAlarmClr,'adGenPppGroupIpv6AddrMismatchAlarmAct':adGenPppGroupIpv6AddrMismatchAlarmAct,'adGenPppGroupIpv6GatewayAddrMismatchAlarmClr':adGenPppGroupIpv6GatewayAddrMismatchAlarmClr,'adGenPppGroupIpv6GatewayAddrMismatchAlarmAct':adGenPppGroupIpv6GatewayAddrMismatchAlarmAct,'adGenPppMIB':adGenPppMIB})