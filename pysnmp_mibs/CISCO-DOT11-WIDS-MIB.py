_p='ciscoDot11WidsProtectFailGroup'
_o='ciscoDot11WidsAuthFailGroup'
_n='cDot11WidsCkipCmicErrors'
_m='cDot11WidsCkipReplays'
_l='cDot11WidsWepIcvErrors'
_k='cDot11WidsWepReplays'
_j='cDot11WidsTkipReplays'
_i='cDot11WidsCcmpDecryptErrors'
_h='cDot11WidsCcmpReplays'
_g='cDot11WidsTkipRemoteMicFailures'
_f='cDot11WidsTkipLocalMicFailures'
_e='cDot11WidsTkipIcvErrors'
_d='cDot11WidsSelPairWiseCipher'
_c='cDot11WidsBlackListTime'
_b='cDot11WidsBlackListAttemptCount'
_a='cDot11WidsEapolFloodStopTime'
_Z='cDot11WidsEapolFloodStartTime'
_Y='cDot11WidsEapolFloodClientCount'
_X='cDot11WidsEapolFloodClientMac'
_W='cDot11WidsEapolFloodTotalCount'
_V='cDot11WidsFloodMaxEntriesPerIntf'
_U='cDot11WidsBlackListDuration'
_T='cDot11WidsBlackListThreshold'
_S='cDot11WidsEapolFloodInterval'
_R='cDot11WidsEapolFloodThreshold'
_Q='cDot11WidsFloodDetectEnable'
_P='cDot11WidsClientMacAddress'
_O='cDot11WidsSsid'
_N='cDot11WidsBlackListClientMac'
_M='cDot11WidsEapolFloodIndex'
_L='seconds'
_K='attempts'
_J='Integer32'
_I='OctetString'
_H='not-accessible'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='Unsigned32'
_C='read-only'
_B='CISCO-DOT11-WIDS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp','TruthValue')
ciscoDot11WidsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,456))
if mibBuilder.loadTexts:ciscoDot11WidsMIB.setRevisions(('2004-11-30 00:00',))
_CiscoDot11WidsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoDot11WidsMIBNotifs=_CiscoDot11WidsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,456,0))
_CiscoDot11WidsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDot11WidsMIBObjects=_CiscoDot11WidsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,456,1))
_CiscoDot11WidsAuthFailures_ObjectIdentity=ObjectIdentity
ciscoDot11WidsAuthFailures=_CiscoDot11WidsAuthFailures_ObjectIdentity((1,3,6,1,4,1,9,9,456,1,1))
_CDot11WidsFloodDetectEnable_Type=TruthValue
_CDot11WidsFloodDetectEnable_Object=MibScalar
cDot11WidsFloodDetectEnable=_CDot11WidsFloodDetectEnable_Object((1,3,6,1,4,1,9,9,456,1,1,1),_CDot11WidsFloodDetectEnable_Type())
cDot11WidsFloodDetectEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cDot11WidsFloodDetectEnable.setStatus(_A)
class _CDot11WidsEapolFloodThreshold_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CDot11WidsEapolFloodThreshold_Type.__name__=_D
_CDot11WidsEapolFloodThreshold_Object=MibScalar
cDot11WidsEapolFloodThreshold=_CDot11WidsEapolFloodThreshold_Object((1,3,6,1,4,1,9,9,456,1,1,2),_CDot11WidsEapolFloodThreshold_Type())
cDot11WidsEapolFloodThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cDot11WidsEapolFloodThreshold.setStatus(_A)
if mibBuilder.loadTexts:cDot11WidsEapolFloodThreshold.setUnits(_K)
class _CDot11WidsEapolFloodInterval_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_CDot11WidsEapolFloodInterval_Type.__name__=_D
_CDot11WidsEapolFloodInterval_Object=MibScalar
cDot11WidsEapolFloodInterval=_CDot11WidsEapolFloodInterval_Object((1,3,6,1,4,1,9,9,456,1,1,3),_CDot11WidsEapolFloodInterval_Type())
cDot11WidsEapolFloodInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cDot11WidsEapolFloodInterval.setStatus(_A)
if mibBuilder.loadTexts:cDot11WidsEapolFloodInterval.setUnits(_L)
class _CDot11WidsBlackListThreshold_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CDot11WidsBlackListThreshold_Type.__name__=_D
_CDot11WidsBlackListThreshold_Object=MibScalar
cDot11WidsBlackListThreshold=_CDot11WidsBlackListThreshold_Object((1,3,6,1,4,1,9,9,456,1,1,4),_CDot11WidsBlackListThreshold_Type())
cDot11WidsBlackListThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cDot11WidsBlackListThreshold.setStatus(_A)
if mibBuilder.loadTexts:cDot11WidsBlackListThreshold.setUnits(_K)
class _CDot11WidsBlackListDuration_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_CDot11WidsBlackListDuration_Type.__name__=_D
_CDot11WidsBlackListDuration_Object=MibScalar
cDot11WidsBlackListDuration=_CDot11WidsBlackListDuration_Object((1,3,6,1,4,1,9,9,456,1,1,5),_CDot11WidsBlackListDuration_Type())
cDot11WidsBlackListDuration.setMaxAccess(_E)
if mibBuilder.loadTexts:cDot11WidsBlackListDuration.setStatus(_A)
if mibBuilder.loadTexts:cDot11WidsBlackListDuration.setUnits(_L)
class _CDot11WidsFloodMaxEntriesPerIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CDot11WidsFloodMaxEntriesPerIntf_Type.__name__=_J
_CDot11WidsFloodMaxEntriesPerIntf_Object=MibScalar
cDot11WidsFloodMaxEntriesPerIntf=_CDot11WidsFloodMaxEntriesPerIntf_Object((1,3,6,1,4,1,9,9,456,1,1,6),_CDot11WidsFloodMaxEntriesPerIntf_Type())
cDot11WidsFloodMaxEntriesPerIntf.setMaxAccess(_E)
if mibBuilder.loadTexts:cDot11WidsFloodMaxEntriesPerIntf.setStatus(_A)
_CDot11WidsEapolFloodTable_Object=MibTable
cDot11WidsEapolFloodTable=_CDot11WidsEapolFloodTable_Object((1,3,6,1,4,1,9,9,456,1,1,7))
if mibBuilder.loadTexts:cDot11WidsEapolFloodTable.setStatus(_A)
_CDot11WidsEapolFloodEntry_Object=MibTableRow
cDot11WidsEapolFloodEntry=_CDot11WidsEapolFloodEntry_Object((1,3,6,1,4,1,9,9,456,1,1,7,1))
cDot11WidsEapolFloodEntry.setIndexNames((0,_F,_G),(0,_B,_M))
if mibBuilder.loadTexts:cDot11WidsEapolFloodEntry.setStatus(_A)
class _CDot11WidsEapolFloodIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CDot11WidsEapolFloodIndex_Type.__name__=_D
_CDot11WidsEapolFloodIndex_Object=MibTableColumn
cDot11WidsEapolFloodIndex=_CDot11WidsEapolFloodIndex_Object((1,3,6,1,4,1,9,9,456,1,1,7,1,1),_CDot11WidsEapolFloodIndex_Type())
cDot11WidsEapolFloodIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cDot11WidsEapolFloodIndex.setStatus(_A)
_CDot11WidsEapolFloodClientMac_Type=MacAddress
_CDot11WidsEapolFloodClientMac_Object=MibTableColumn
cDot11WidsEapolFloodClientMac=_CDot11WidsEapolFloodClientMac_Object((1,3,6,1,4,1,9,9,456,1,1,7,1,2),_CDot11WidsEapolFloodClientMac_Type())
cDot11WidsEapolFloodClientMac.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsEapolFloodClientMac.setStatus(_A)
_CDot11WidsEapolFloodClientCount_Type=Unsigned32
_CDot11WidsEapolFloodClientCount_Object=MibTableColumn
cDot11WidsEapolFloodClientCount=_CDot11WidsEapolFloodClientCount_Object((1,3,6,1,4,1,9,9,456,1,1,7,1,3),_CDot11WidsEapolFloodClientCount_Type())
cDot11WidsEapolFloodClientCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsEapolFloodClientCount.setStatus(_A)
_CDot11WidsEapolFloodStartTime_Type=TimeStamp
_CDot11WidsEapolFloodStartTime_Object=MibTableColumn
cDot11WidsEapolFloodStartTime=_CDot11WidsEapolFloodStartTime_Object((1,3,6,1,4,1,9,9,456,1,1,7,1,4),_CDot11WidsEapolFloodStartTime_Type())
cDot11WidsEapolFloodStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsEapolFloodStartTime.setStatus(_A)
_CDot11WidsEapolFloodStopTime_Type=TimeStamp
_CDot11WidsEapolFloodStopTime_Object=MibTableColumn
cDot11WidsEapolFloodStopTime=_CDot11WidsEapolFloodStopTime_Object((1,3,6,1,4,1,9,9,456,1,1,7,1,5),_CDot11WidsEapolFloodStopTime_Type())
cDot11WidsEapolFloodStopTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsEapolFloodStopTime.setStatus(_A)
_CDot11WidsEapolFloodTotalCount_Type=Counter32
_CDot11WidsEapolFloodTotalCount_Object=MibTableColumn
cDot11WidsEapolFloodTotalCount=_CDot11WidsEapolFloodTotalCount_Object((1,3,6,1,4,1,9,9,456,1,1,7,1,6),_CDot11WidsEapolFloodTotalCount_Type())
cDot11WidsEapolFloodTotalCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsEapolFloodTotalCount.setStatus(_A)
_CDot11WidsBlackListTable_Object=MibTable
cDot11WidsBlackListTable=_CDot11WidsBlackListTable_Object((1,3,6,1,4,1,9,9,456,1,1,8))
if mibBuilder.loadTexts:cDot11WidsBlackListTable.setStatus(_A)
_CDot11WidsBlackListEntry_Object=MibTableRow
cDot11WidsBlackListEntry=_CDot11WidsBlackListEntry_Object((1,3,6,1,4,1,9,9,456,1,1,8,1))
cDot11WidsBlackListEntry.setIndexNames((0,_F,_G),(0,_B,_N))
if mibBuilder.loadTexts:cDot11WidsBlackListEntry.setStatus(_A)
_CDot11WidsBlackListClientMac_Type=MacAddress
_CDot11WidsBlackListClientMac_Object=MibTableColumn
cDot11WidsBlackListClientMac=_CDot11WidsBlackListClientMac_Object((1,3,6,1,4,1,9,9,456,1,1,8,1,1),_CDot11WidsBlackListClientMac_Type())
cDot11WidsBlackListClientMac.setMaxAccess(_H)
if mibBuilder.loadTexts:cDot11WidsBlackListClientMac.setStatus(_A)
_CDot11WidsBlackListAttemptCount_Type=Counter32
_CDot11WidsBlackListAttemptCount_Object=MibTableColumn
cDot11WidsBlackListAttemptCount=_CDot11WidsBlackListAttemptCount_Object((1,3,6,1,4,1,9,9,456,1,1,8,1,2),_CDot11WidsBlackListAttemptCount_Type())
cDot11WidsBlackListAttemptCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsBlackListAttemptCount.setStatus(_A)
_CDot11WidsBlackListTime_Type=TimeStamp
_CDot11WidsBlackListTime_Object=MibTableColumn
cDot11WidsBlackListTime=_CDot11WidsBlackListTime_Object((1,3,6,1,4,1,9,9,456,1,1,8,1,3),_CDot11WidsBlackListTime_Type())
cDot11WidsBlackListTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsBlackListTime.setStatus(_A)
_CiscoDot11WidsProtectFailures_ObjectIdentity=ObjectIdentity
ciscoDot11WidsProtectFailures=_CiscoDot11WidsProtectFailures_ObjectIdentity((1,3,6,1,4,1,9,9,456,1,2))
_CDot11WidsProtectFailClientTable_Object=MibTable
cDot11WidsProtectFailClientTable=_CDot11WidsProtectFailClientTable_Object((1,3,6,1,4,1,9,9,456,1,2,1))
if mibBuilder.loadTexts:cDot11WidsProtectFailClientTable.setStatus(_A)
_CDot11WidsProtectFailClientEntry_Object=MibTableRow
cDot11WidsProtectFailClientEntry=_CDot11WidsProtectFailClientEntry_Object((1,3,6,1,4,1,9,9,456,1,2,1,1))
cDot11WidsProtectFailClientEntry.setIndexNames((0,_F,_G),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:cDot11WidsProtectFailClientEntry.setStatus(_A)
class _CDot11WidsSsid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CDot11WidsSsid_Type.__name__=_I
_CDot11WidsSsid_Object=MibTableColumn
cDot11WidsSsid=_CDot11WidsSsid_Object((1,3,6,1,4,1,9,9,456,1,2,1,1,1),_CDot11WidsSsid_Type())
cDot11WidsSsid.setMaxAccess(_H)
if mibBuilder.loadTexts:cDot11WidsSsid.setStatus(_A)
_CDot11WidsClientMacAddress_Type=MacAddress
_CDot11WidsClientMacAddress_Object=MibTableColumn
cDot11WidsClientMacAddress=_CDot11WidsClientMacAddress_Object((1,3,6,1,4,1,9,9,456,1,2,1,1,2),_CDot11WidsClientMacAddress_Type())
cDot11WidsClientMacAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:cDot11WidsClientMacAddress.setStatus(_A)
class _CDot11WidsSelPairWiseCipher_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_CDot11WidsSelPairWiseCipher_Type.__name__=_I
_CDot11WidsSelPairWiseCipher_Object=MibTableColumn
cDot11WidsSelPairWiseCipher=_CDot11WidsSelPairWiseCipher_Object((1,3,6,1,4,1,9,9,456,1,2,1,1,3),_CDot11WidsSelPairWiseCipher_Type())
cDot11WidsSelPairWiseCipher.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsSelPairWiseCipher.setStatus(_A)
_CDot11WidsTkipIcvErrors_Type=Counter32
_CDot11WidsTkipIcvErrors_Object=MibTableColumn
cDot11WidsTkipIcvErrors=_CDot11WidsTkipIcvErrors_Object((1,3,6,1,4,1,9,9,456,1,2,1,1,4),_CDot11WidsTkipIcvErrors_Type())
cDot11WidsTkipIcvErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsTkipIcvErrors.setStatus(_A)
_CDot11WidsTkipLocalMicFailures_Type=Counter32
_CDot11WidsTkipLocalMicFailures_Object=MibTableColumn
cDot11WidsTkipLocalMicFailures=_CDot11WidsTkipLocalMicFailures_Object((1,3,6,1,4,1,9,9,456,1,2,1,1,5),_CDot11WidsTkipLocalMicFailures_Type())
cDot11WidsTkipLocalMicFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsTkipLocalMicFailures.setStatus(_A)
_CDot11WidsTkipRemoteMicFailures_Type=Counter32
_CDot11WidsTkipRemoteMicFailures_Object=MibTableColumn
cDot11WidsTkipRemoteMicFailures=_CDot11WidsTkipRemoteMicFailures_Object((1,3,6,1,4,1,9,9,456,1,2,1,1,6),_CDot11WidsTkipRemoteMicFailures_Type())
cDot11WidsTkipRemoteMicFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsTkipRemoteMicFailures.setStatus(_A)
_CDot11WidsCcmpReplays_Type=Counter32
_CDot11WidsCcmpReplays_Object=MibTableColumn
cDot11WidsCcmpReplays=_CDot11WidsCcmpReplays_Object((1,3,6,1,4,1,9,9,456,1,2,1,1,7),_CDot11WidsCcmpReplays_Type())
cDot11WidsCcmpReplays.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsCcmpReplays.setStatus(_A)
_CDot11WidsCcmpDecryptErrors_Type=Counter32
_CDot11WidsCcmpDecryptErrors_Object=MibTableColumn
cDot11WidsCcmpDecryptErrors=_CDot11WidsCcmpDecryptErrors_Object((1,3,6,1,4,1,9,9,456,1,2,1,1,8),_CDot11WidsCcmpDecryptErrors_Type())
cDot11WidsCcmpDecryptErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsCcmpDecryptErrors.setStatus(_A)
_CDot11WidsTkipReplays_Type=Counter32
_CDot11WidsTkipReplays_Object=MibTableColumn
cDot11WidsTkipReplays=_CDot11WidsTkipReplays_Object((1,3,6,1,4,1,9,9,456,1,2,1,1,9),_CDot11WidsTkipReplays_Type())
cDot11WidsTkipReplays.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsTkipReplays.setStatus(_A)
_CDot11WidsWepReplays_Type=Counter32
_CDot11WidsWepReplays_Object=MibTableColumn
cDot11WidsWepReplays=_CDot11WidsWepReplays_Object((1,3,6,1,4,1,9,9,456,1,2,1,1,10),_CDot11WidsWepReplays_Type())
cDot11WidsWepReplays.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsWepReplays.setStatus(_A)
_CDot11WidsWepIcvErrors_Type=Counter32
_CDot11WidsWepIcvErrors_Object=MibTableColumn
cDot11WidsWepIcvErrors=_CDot11WidsWepIcvErrors_Object((1,3,6,1,4,1,9,9,456,1,2,1,1,11),_CDot11WidsWepIcvErrors_Type())
cDot11WidsWepIcvErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsWepIcvErrors.setStatus(_A)
_CDot11WidsCkipReplays_Type=Counter32
_CDot11WidsCkipReplays_Object=MibTableColumn
cDot11WidsCkipReplays=_CDot11WidsCkipReplays_Object((1,3,6,1,4,1,9,9,456,1,2,1,1,12),_CDot11WidsCkipReplays_Type())
cDot11WidsCkipReplays.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsCkipReplays.setStatus(_A)
_CDot11WidsCkipCmicErrors_Type=Counter32
_CDot11WidsCkipCmicErrors_Object=MibTableColumn
cDot11WidsCkipCmicErrors=_CDot11WidsCkipCmicErrors_Object((1,3,6,1,4,1,9,9,456,1,2,1,1,13),_CDot11WidsCkipCmicErrors_Type())
cDot11WidsCkipCmicErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11WidsCkipCmicErrors.setStatus(_A)
_CiscoDot11WidsMIBConform_ObjectIdentity=ObjectIdentity
ciscoDot11WidsMIBConform=_CiscoDot11WidsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,456,2))
_CiscoDot11WidsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDot11WidsMIBCompliances=_CiscoDot11WidsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,456,2,1))
_CiscoDot11WidsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDot11WidsMIBGroups=_CiscoDot11WidsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,456,2,2))
ciscoDot11WidsAuthFailGroup=ObjectGroup((1,3,6,1,4,1,9,9,456,2,2,1))
ciscoDot11WidsAuthFailGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:ciscoDot11WidsAuthFailGroup.setStatus(_A)
ciscoDot11WidsProtectFailGroup=ObjectGroup((1,3,6,1,4,1,9,9,456,2,2,2))
ciscoDot11WidsProtectFailGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:ciscoDot11WidsProtectFailGroup.setStatus(_A)
ciscoDot11WidsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,456,2,1,1))
ciscoDot11WidsMIBCompliance.setObjects(*((_B,_o),(_B,_p)))
if mibBuilder.loadTexts:ciscoDot11WidsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoDot11WidsMIB':ciscoDot11WidsMIB,'ciscoDot11WidsMIBNotifs':ciscoDot11WidsMIBNotifs,'ciscoDot11WidsMIBObjects':ciscoDot11WidsMIBObjects,'ciscoDot11WidsAuthFailures':ciscoDot11WidsAuthFailures,_Q:cDot11WidsFloodDetectEnable,_R:cDot11WidsEapolFloodThreshold,_S:cDot11WidsEapolFloodInterval,_T:cDot11WidsBlackListThreshold,_U:cDot11WidsBlackListDuration,_V:cDot11WidsFloodMaxEntriesPerIntf,'cDot11WidsEapolFloodTable':cDot11WidsEapolFloodTable,'cDot11WidsEapolFloodEntry':cDot11WidsEapolFloodEntry,_M:cDot11WidsEapolFloodIndex,_X:cDot11WidsEapolFloodClientMac,_Y:cDot11WidsEapolFloodClientCount,_Z:cDot11WidsEapolFloodStartTime,_a:cDot11WidsEapolFloodStopTime,_W:cDot11WidsEapolFloodTotalCount,'cDot11WidsBlackListTable':cDot11WidsBlackListTable,'cDot11WidsBlackListEntry':cDot11WidsBlackListEntry,_N:cDot11WidsBlackListClientMac,_b:cDot11WidsBlackListAttemptCount,_c:cDot11WidsBlackListTime,'ciscoDot11WidsProtectFailures':ciscoDot11WidsProtectFailures,'cDot11WidsProtectFailClientTable':cDot11WidsProtectFailClientTable,'cDot11WidsProtectFailClientEntry':cDot11WidsProtectFailClientEntry,_O:cDot11WidsSsid,_P:cDot11WidsClientMacAddress,_d:cDot11WidsSelPairWiseCipher,_e:cDot11WidsTkipIcvErrors,_f:cDot11WidsTkipLocalMicFailures,_g:cDot11WidsTkipRemoteMicFailures,_h:cDot11WidsCcmpReplays,_i:cDot11WidsCcmpDecryptErrors,_j:cDot11WidsTkipReplays,_k:cDot11WidsWepReplays,_l:cDot11WidsWepIcvErrors,_m:cDot11WidsCkipReplays,_n:cDot11WidsCkipCmicErrors,'ciscoDot11WidsMIBConform':ciscoDot11WidsMIBConform,'ciscoDot11WidsMIBCompliances':ciscoDot11WidsMIBCompliances,'ciscoDot11WidsMIBCompliance':ciscoDot11WidsMIBCompliance,'ciscoDot11WidsMIBGroups':ciscoDot11WidsMIBGroups,_o:ciscoDot11WidsAuthFailGroup,_p:ciscoDot11WidsProtectFailGroup})