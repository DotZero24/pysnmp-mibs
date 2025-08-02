_r='adSingleDs3EnhancedAISTrapActive'
_q='adSingleDs3EnhancedAISTrapClear'
_p='adSingleDs3EnhancedRAITrapActive'
_o='adSingleDs3EnhancedRAITrapClear'
_n='adSingleDs3EnhancedLOFTrapActive'
_m='adSingleDs3EnhancedLOFTrapClear'
_l='adSingleDs3EnhancedLOSTrapActive'
_k='adSingleDs3EnhancedLOSTrapClear'
_j='adSingleDs3IdleTrapActive'
_i='adSingleDs3IdleTrapClear'
_h='adSingleDs3LoopTrapActive'
_g='adSingleDs3LoopTrapClear'
_f='adSingleDs3AISTrapActive'
_e='adSingleDs3AISTrapClear'
_d='adSingleDs3RAITrapActive'
_c='adSingleDs3RAITrapClear'
_b='adSingleDs3LOFTrapActive'
_a='adSingleDs3LOFTrapClear'
_Z='adSingleDs3LOSTrapActive'
_Y='adSingleDs3LOSTrapClear'
_X='adTa5kSingleDS3PortScrambler'
_W='adTa5kSingleDS3PortLineType'
_V='ifIndex'
_U='IF-MIB'
_T='critical'
_S='major'
_R='minor'
_Q='alert'
_P='info'
_O='TruthValue'
_N='adTAeSCUTrapAlarmLevel'
_M='ADTRAN-TAeSCUEXT1-MIB'
_L='Integer32'
_K='read-write'
_J='sysName'
_I='SNMPv2-MIB'
_H='adTrapInformSeqNum'
_G='ADTRAN-GENTRAPINFORM-MIB'
_F='adGenPortInfoIndex'
_E='ADTRAN-GENPORT-MIB'
_D='adGenSlotInfoIndex'
_C='ADTRAN-GENSLOT-MIB'
_B='ADTRAN-TA5K-SingleDS3-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPortInfoIndex,adGenPortTrapIdentifier=mibBuilder.importSymbols(_E,_F,'adGenPortTrapIdentifier')
adGenSlotAlarmStatus,adGenSlotInfoIndex=mibBuilder.importSymbols(_C,'adGenSlotAlarmStatus',_D)
adTrapInformSeqNum,=mibBuilder.importSymbols(_G,_H)
adIdentity,adMgmt,adProducts=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity','adMgmt','adProducts')
adTAeSCUTrapAlarmLevel,=mibBuilder.importSymbols(_M,_N)
ifIndex,=mibBuilder.importSymbols(_U,_V)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_I,_J)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_O)
adTa5kSingleDs3ModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,896))
_AdTa5kSingleDs3TrapsPrefix_ObjectIdentity=ObjectIdentity
adTa5kSingleDs3TrapsPrefix=_AdTa5kSingleDs3TrapsPrefix_ObjectIdentity((1,3,6,1,4,1,664,1,896))
_AdTa5kSingleDS3Traps_ObjectIdentity=ObjectIdentity
adTa5kSingleDS3Traps=_AdTa5kSingleDS3Traps_ObjectIdentity((1,3,6,1,4,1,664,1,896,0))
_AdTa5kSingleDs3_ObjectIdentity=ObjectIdentity
adTa5kSingleDs3=_AdTa5kSingleDs3_ObjectIdentity((1,3,6,1,4,1,664,2,896))
_AdTa5kSingleDS3PortProv_ObjectIdentity=ObjectIdentity
adTa5kSingleDS3PortProv=_AdTa5kSingleDS3PortProv_ObjectIdentity((1,3,6,1,4,1,664,2,896,1))
_AdTa5kSingleDS3PortProvTable_Object=MibTable
adTa5kSingleDS3PortProvTable=_AdTa5kSingleDS3PortProvTable_Object((1,3,6,1,4,1,664,2,896,1,1))
if mibBuilder.loadTexts:adTa5kSingleDS3PortProvTable.setStatus(_A)
_AdTa5kSingleDS3PortProvEntry_Object=MibTableRow
adTa5kSingleDS3PortProvEntry=_AdTa5kSingleDS3PortProvEntry_Object((1,3,6,1,4,1,664,2,896,1,1,1))
adTa5kSingleDS3PortProvEntry.setIndexNames((0,_U,_V))
if mibBuilder.loadTexts:adTa5kSingleDS3PortProvEntry.setStatus(_A)
class _AdTa5kSingleDS3PortLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('dsx3other',1),('dsx3M23',2),('dsx3SYNTRAN',3),('dsx3CbitParity',4),('dsx3ClearChannel',5),('e3other',6),('e3Framed',7),('e3Plcp',8),('dsx3CbitParityPlcp',9),('dsx3M23Plcp',10)))
_AdTa5kSingleDS3PortLineType_Type.__name__=_L
_AdTa5kSingleDS3PortLineType_Object=MibTableColumn
adTa5kSingleDS3PortLineType=_AdTa5kSingleDS3PortLineType_Object((1,3,6,1,4,1,664,2,896,1,1,1,1),_AdTa5kSingleDS3PortLineType_Type())
adTa5kSingleDS3PortLineType.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kSingleDS3PortLineType.setStatus(_A)
class _AdTa5kSingleDS3PortScrambler_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_AdTa5kSingleDS3PortScrambler_Type.__name__=_L
_AdTa5kSingleDS3PortScrambler_Object=MibTableColumn
adTa5kSingleDS3PortScrambler=_AdTa5kSingleDS3PortScrambler_Object((1,3,6,1,4,1,664,2,896,1,1,1,2),_AdTa5kSingleDS3PortScrambler_Type())
adTa5kSingleDS3PortScrambler.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kSingleDS3PortScrambler.setStatus(_A)
_AdTa5kSingleDS3AlmProv_ObjectIdentity=ObjectIdentity
adTa5kSingleDS3AlmProv=_AdTa5kSingleDS3AlmProv_ObjectIdentity((1,3,6,1,4,1,664,2,896,3))
_AdTa5kSingleDS3EnhancedAlmSlotProvTable_Object=MibTable
adTa5kSingleDS3EnhancedAlmSlotProvTable=_AdTa5kSingleDS3EnhancedAlmSlotProvTable_Object((1,3,6,1,4,1,664,2,896,3,1))
if mibBuilder.loadTexts:adTa5kSingleDS3EnhancedAlmSlotProvTable.setStatus(_A)
_AdTa5kSingleDS3EnhancedAlmSlotProvEntry_Object=MibTableRow
adTa5kSingleDS3EnhancedAlmSlotProvEntry=_AdTa5kSingleDS3EnhancedAlmSlotProvEntry_Object((1,3,6,1,4,1,664,2,896,3,1,1))
adTa5kSingleDS3EnhancedAlmSlotProvEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adTa5kSingleDS3EnhancedAlmSlotProvEntry.setStatus(_A)
class _AdSingleDs3EnhancedAlmSlotLOSSeverity_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*((_P,2),(_Q,3),(_R,4),(_S,5),(_T,6)))
_AdSingleDs3EnhancedAlmSlotLOSSeverity_Type.__name__=_L
_AdSingleDs3EnhancedAlmSlotLOSSeverity_Object=MibTableColumn
adSingleDs3EnhancedAlmSlotLOSSeverity=_AdSingleDs3EnhancedAlmSlotLOSSeverity_Object((1,3,6,1,4,1,664,2,896,3,1,1,1),_AdSingleDs3EnhancedAlmSlotLOSSeverity_Type())
adSingleDs3EnhancedAlmSlotLOSSeverity.setMaxAccess(_K)
if mibBuilder.loadTexts:adSingleDs3EnhancedAlmSlotLOSSeverity.setStatus(_A)
class _AdSingleDs3EnhancedAlmSlotLOSSuppression_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AdSingleDs3EnhancedAlmSlotLOSSuppression_Type.__name__=_L
_AdSingleDs3EnhancedAlmSlotLOSSuppression_Object=MibTableColumn
adSingleDs3EnhancedAlmSlotLOSSuppression=_AdSingleDs3EnhancedAlmSlotLOSSuppression_Object((1,3,6,1,4,1,664,2,896,3,1,1,2),_AdSingleDs3EnhancedAlmSlotLOSSuppression_Type())
adSingleDs3EnhancedAlmSlotLOSSuppression.setMaxAccess(_K)
if mibBuilder.loadTexts:adSingleDs3EnhancedAlmSlotLOSSuppression.setStatus(_A)
class _AdSingleDs3EnhancedAlmSlotLOFSeverity_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*((_P,2),(_Q,3),(_R,4),(_S,5),(_T,6)))
_AdSingleDs3EnhancedAlmSlotLOFSeverity_Type.__name__=_L
_AdSingleDs3EnhancedAlmSlotLOFSeverity_Object=MibTableColumn
adSingleDs3EnhancedAlmSlotLOFSeverity=_AdSingleDs3EnhancedAlmSlotLOFSeverity_Object((1,3,6,1,4,1,664,2,896,3,1,1,3),_AdSingleDs3EnhancedAlmSlotLOFSeverity_Type())
adSingleDs3EnhancedAlmSlotLOFSeverity.setMaxAccess(_K)
if mibBuilder.loadTexts:adSingleDs3EnhancedAlmSlotLOFSeverity.setStatus(_A)
class _AdSingleDs3EnhancedAlmSlotLOFSuppression_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AdSingleDs3EnhancedAlmSlotLOFSuppression_Type.__name__=_L
_AdSingleDs3EnhancedAlmSlotLOFSuppression_Object=MibTableColumn
adSingleDs3EnhancedAlmSlotLOFSuppression=_AdSingleDs3EnhancedAlmSlotLOFSuppression_Object((1,3,6,1,4,1,664,2,896,3,1,1,4),_AdSingleDs3EnhancedAlmSlotLOFSuppression_Type())
adSingleDs3EnhancedAlmSlotLOFSuppression.setMaxAccess(_K)
if mibBuilder.loadTexts:adSingleDs3EnhancedAlmSlotLOFSuppression.setStatus(_A)
class _AdSingleDs3EnhancedAlmSlotAISSeverity_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*((_P,2),(_Q,3),(_R,4),(_S,5),(_T,6)))
_AdSingleDs3EnhancedAlmSlotAISSeverity_Type.__name__=_L
_AdSingleDs3EnhancedAlmSlotAISSeverity_Object=MibTableColumn
adSingleDs3EnhancedAlmSlotAISSeverity=_AdSingleDs3EnhancedAlmSlotAISSeverity_Object((1,3,6,1,4,1,664,2,896,3,1,1,5),_AdSingleDs3EnhancedAlmSlotAISSeverity_Type())
adSingleDs3EnhancedAlmSlotAISSeverity.setMaxAccess(_K)
if mibBuilder.loadTexts:adSingleDs3EnhancedAlmSlotAISSeverity.setStatus(_A)
class _AdSingleDs3EnhancedAlmSlotAISSuppression_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AdSingleDs3EnhancedAlmSlotAISSuppression_Type.__name__=_L
_AdSingleDs3EnhancedAlmSlotAISSuppression_Object=MibTableColumn
adSingleDs3EnhancedAlmSlotAISSuppression=_AdSingleDs3EnhancedAlmSlotAISSuppression_Object((1,3,6,1,4,1,664,2,896,3,1,1,6),_AdSingleDs3EnhancedAlmSlotAISSuppression_Type())
adSingleDs3EnhancedAlmSlotAISSuppression.setMaxAccess(_K)
if mibBuilder.loadTexts:adSingleDs3EnhancedAlmSlotAISSuppression.setStatus(_A)
class _AdSingleDs3EnhancedAlmSlotRAISeverity_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*((_P,2),(_Q,3),(_R,4),(_S,5),(_T,6)))
_AdSingleDs3EnhancedAlmSlotRAISeverity_Type.__name__=_L
_AdSingleDs3EnhancedAlmSlotRAISeverity_Object=MibTableColumn
adSingleDs3EnhancedAlmSlotRAISeverity=_AdSingleDs3EnhancedAlmSlotRAISeverity_Object((1,3,6,1,4,1,664,2,896,3,1,1,7),_AdSingleDs3EnhancedAlmSlotRAISeverity_Type())
adSingleDs3EnhancedAlmSlotRAISeverity.setMaxAccess(_K)
if mibBuilder.loadTexts:adSingleDs3EnhancedAlmSlotRAISeverity.setStatus(_A)
class _AdSingleDs3EnhancedAlmSlotRAISuppression_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AdSingleDs3EnhancedAlmSlotRAISuppression_Type.__name__=_L
_AdSingleDs3EnhancedAlmSlotRAISuppression_Object=MibTableColumn
adSingleDs3EnhancedAlmSlotRAISuppression=_AdSingleDs3EnhancedAlmSlotRAISuppression_Object((1,3,6,1,4,1,664,2,896,3,1,1,8),_AdSingleDs3EnhancedAlmSlotRAISuppression_Type())
adSingleDs3EnhancedAlmSlotRAISuppression.setMaxAccess(_K)
if mibBuilder.loadTexts:adSingleDs3EnhancedAlmSlotRAISuppression.setStatus(_A)
class _AdSingleDS3EnhancedAlmSlotLOSEnable_Type(TruthValue):defaultValue=1
_AdSingleDS3EnhancedAlmSlotLOSEnable_Type.__name__=_O
_AdSingleDS3EnhancedAlmSlotLOSEnable_Object=MibTableColumn
adSingleDS3EnhancedAlmSlotLOSEnable=_AdSingleDS3EnhancedAlmSlotLOSEnable_Object((1,3,6,1,4,1,664,2,896,3,1,1,9),_AdSingleDS3EnhancedAlmSlotLOSEnable_Type())
adSingleDS3EnhancedAlmSlotLOSEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:adSingleDS3EnhancedAlmSlotLOSEnable.setStatus(_A)
class _AdSingleDS3EnhancedAlmSlotLOFEnable_Type(TruthValue):defaultValue=1
_AdSingleDS3EnhancedAlmSlotLOFEnable_Type.__name__=_O
_AdSingleDS3EnhancedAlmSlotLOFEnable_Object=MibTableColumn
adSingleDS3EnhancedAlmSlotLOFEnable=_AdSingleDS3EnhancedAlmSlotLOFEnable_Object((1,3,6,1,4,1,664,2,896,3,1,1,10),_AdSingleDS3EnhancedAlmSlotLOFEnable_Type())
adSingleDS3EnhancedAlmSlotLOFEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:adSingleDS3EnhancedAlmSlotLOFEnable.setStatus(_A)
class _AdSingleDS3EnhancedAlmSlotAISEnable_Type(TruthValue):defaultValue=1
_AdSingleDS3EnhancedAlmSlotAISEnable_Type.__name__=_O
_AdSingleDS3EnhancedAlmSlotAISEnable_Object=MibTableColumn
adSingleDS3EnhancedAlmSlotAISEnable=_AdSingleDS3EnhancedAlmSlotAISEnable_Object((1,3,6,1,4,1,664,2,896,3,1,1,11),_AdSingleDS3EnhancedAlmSlotAISEnable_Type())
adSingleDS3EnhancedAlmSlotAISEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:adSingleDS3EnhancedAlmSlotAISEnable.setStatus(_A)
class _AdSingleDS3EnhancedAlmSlotRAIEnable_Type(TruthValue):defaultValue=1
_AdSingleDS3EnhancedAlmSlotRAIEnable_Type.__name__=_O
_AdSingleDS3EnhancedAlmSlotRAIEnable_Object=MibTableColumn
adSingleDS3EnhancedAlmSlotRAIEnable=_AdSingleDS3EnhancedAlmSlotRAIEnable_Object((1,3,6,1,4,1,664,2,896,3,1,1,12),_AdSingleDS3EnhancedAlmSlotRAIEnable_Type())
adSingleDS3EnhancedAlmSlotRAIEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:adSingleDS3EnhancedAlmSlotRAIEnable.setStatus(_A)
_AdTa5kSingleDS3MibConformance_ObjectIdentity=ObjectIdentity
adTa5kSingleDS3MibConformance=_AdTa5kSingleDS3MibConformance_ObjectIdentity((1,3,6,1,4,1,664,2,896,6))
_AdTa5kSingleDS3MibGroups_ObjectIdentity=ObjectIdentity
adTa5kSingleDS3MibGroups=_AdTa5kSingleDS3MibGroups_ObjectIdentity((1,3,6,1,4,1,664,2,896,6,1))
adTa5kSingleDS3PortProvGroup=ObjectGroup((1,3,6,1,4,1,664,2,896,6,1,1))
adTa5kSingleDS3PortProvGroup.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:adTa5kSingleDS3PortProvGroup.setStatus(_A)
adSingleDs3LOSTrapClear=NotificationType((1,3,6,1,4,1,664,1,896,0,2))
adSingleDs3LOSTrapClear.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F)))
if mibBuilder.loadTexts:adSingleDs3LOSTrapClear.setStatus(_A)
adSingleDs3LOSTrapActive=NotificationType((1,3,6,1,4,1,664,1,896,0,3))
adSingleDs3LOSTrapActive.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F)))
if mibBuilder.loadTexts:adSingleDs3LOSTrapActive.setStatus(_A)
adSingleDs3LOFTrapClear=NotificationType((1,3,6,1,4,1,664,1,896,0,4))
adSingleDs3LOFTrapClear.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F)))
if mibBuilder.loadTexts:adSingleDs3LOFTrapClear.setStatus(_A)
adSingleDs3LOFTrapActive=NotificationType((1,3,6,1,4,1,664,1,896,0,5))
adSingleDs3LOFTrapActive.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F)))
if mibBuilder.loadTexts:adSingleDs3LOFTrapActive.setStatus(_A)
adSingleDs3RAITrapClear=NotificationType((1,3,6,1,4,1,664,1,896,0,6))
adSingleDs3RAITrapClear.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F)))
if mibBuilder.loadTexts:adSingleDs3RAITrapClear.setStatus(_A)
adSingleDs3RAITrapActive=NotificationType((1,3,6,1,4,1,664,1,896,0,7))
adSingleDs3RAITrapActive.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F)))
if mibBuilder.loadTexts:adSingleDs3RAITrapActive.setStatus(_A)
adSingleDs3AISTrapClear=NotificationType((1,3,6,1,4,1,664,1,896,0,8))
adSingleDs3AISTrapClear.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F)))
if mibBuilder.loadTexts:adSingleDs3AISTrapClear.setStatus(_A)
adSingleDs3AISTrapActive=NotificationType((1,3,6,1,4,1,664,1,896,0,9))
adSingleDs3AISTrapActive.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F)))
if mibBuilder.loadTexts:adSingleDs3AISTrapActive.setStatus(_A)
adSingleDs3LoopTrapClear=NotificationType((1,3,6,1,4,1,664,1,896,0,10))
adSingleDs3LoopTrapClear.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F)))
if mibBuilder.loadTexts:adSingleDs3LoopTrapClear.setStatus(_A)
adSingleDs3LoopTrapActive=NotificationType((1,3,6,1,4,1,664,1,896,0,11))
adSingleDs3LoopTrapActive.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F)))
if mibBuilder.loadTexts:adSingleDs3LoopTrapActive.setStatus(_A)
adSingleDs3IdleTrapClear=NotificationType((1,3,6,1,4,1,664,1,896,0,12))
adSingleDs3IdleTrapClear.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F)))
if mibBuilder.loadTexts:adSingleDs3IdleTrapClear.setStatus(_A)
adSingleDs3IdleTrapActive=NotificationType((1,3,6,1,4,1,664,1,896,0,13))
adSingleDs3IdleTrapActive.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F)))
if mibBuilder.loadTexts:adSingleDs3IdleTrapActive.setStatus(_A)
adSingleDs3EnhancedLOSTrapClear=NotificationType((1,3,6,1,4,1,664,1,896,0,14))
adSingleDs3EnhancedLOSTrapClear.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F),(_M,_N)))
if mibBuilder.loadTexts:adSingleDs3EnhancedLOSTrapClear.setStatus(_A)
adSingleDs3EnhancedLOSTrapActive=NotificationType((1,3,6,1,4,1,664,1,896,0,15))
adSingleDs3EnhancedLOSTrapActive.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F),(_M,_N)))
if mibBuilder.loadTexts:adSingleDs3EnhancedLOSTrapActive.setStatus(_A)
adSingleDs3EnhancedLOFTrapClear=NotificationType((1,3,6,1,4,1,664,1,896,0,16))
adSingleDs3EnhancedLOFTrapClear.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F),(_M,_N)))
if mibBuilder.loadTexts:adSingleDs3EnhancedLOFTrapClear.setStatus(_A)
adSingleDs3EnhancedLOFTrapActive=NotificationType((1,3,6,1,4,1,664,1,896,0,17))
adSingleDs3EnhancedLOFTrapActive.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F),(_M,_N)))
if mibBuilder.loadTexts:adSingleDs3EnhancedLOFTrapActive.setStatus(_A)
adSingleDs3EnhancedRAITrapClear=NotificationType((1,3,6,1,4,1,664,1,896,0,18))
adSingleDs3EnhancedRAITrapClear.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F),(_M,_N)))
if mibBuilder.loadTexts:adSingleDs3EnhancedRAITrapClear.setStatus(_A)
adSingleDs3EnhancedRAITrapActive=NotificationType((1,3,6,1,4,1,664,1,896,0,19))
adSingleDs3EnhancedRAITrapActive.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F),(_M,_N)))
if mibBuilder.loadTexts:adSingleDs3EnhancedRAITrapActive.setStatus(_A)
adSingleDs3EnhancedAISTrapClear=NotificationType((1,3,6,1,4,1,664,1,896,0,20))
adSingleDs3EnhancedAISTrapClear.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F),(_M,_N)))
if mibBuilder.loadTexts:adSingleDs3EnhancedAISTrapClear.setStatus(_A)
adSingleDs3EnhancedAISTrapActive=NotificationType((1,3,6,1,4,1,664,1,896,0,21))
adSingleDs3EnhancedAISTrapActive.setObjects(*((_G,_H),(_I,_J),(_C,_D),(_E,_F),(_M,_N)))
if mibBuilder.loadTexts:adSingleDs3EnhancedAISTrapActive.setStatus(_A)
adTa5kSingleDS3TrapGroup=NotificationGroup((1,3,6,1,4,1,664,2,896,6,1,2))
adTa5kSingleDS3TrapGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:adTa5kSingleDS3TrapGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adTa5kSingleDs3TrapsPrefix':adTa5kSingleDs3TrapsPrefix,'adTa5kSingleDS3Traps':adTa5kSingleDS3Traps,_Y:adSingleDs3LOSTrapClear,_Z:adSingleDs3LOSTrapActive,_a:adSingleDs3LOFTrapClear,_b:adSingleDs3LOFTrapActive,_c:adSingleDs3RAITrapClear,_d:adSingleDs3RAITrapActive,_e:adSingleDs3AISTrapClear,_f:adSingleDs3AISTrapActive,_g:adSingleDs3LoopTrapClear,_h:adSingleDs3LoopTrapActive,_i:adSingleDs3IdleTrapClear,_j:adSingleDs3IdleTrapActive,_k:adSingleDs3EnhancedLOSTrapClear,_l:adSingleDs3EnhancedLOSTrapActive,_m:adSingleDs3EnhancedLOFTrapClear,_n:adSingleDs3EnhancedLOFTrapActive,_o:adSingleDs3EnhancedRAITrapClear,_p:adSingleDs3EnhancedRAITrapActive,_q:adSingleDs3EnhancedAISTrapClear,_r:adSingleDs3EnhancedAISTrapActive,'adTa5kSingleDs3':adTa5kSingleDs3,'adTa5kSingleDS3PortProv':adTa5kSingleDS3PortProv,'adTa5kSingleDS3PortProvTable':adTa5kSingleDS3PortProvTable,'adTa5kSingleDS3PortProvEntry':adTa5kSingleDS3PortProvEntry,_W:adTa5kSingleDS3PortLineType,_X:adTa5kSingleDS3PortScrambler,'adTa5kSingleDS3AlmProv':adTa5kSingleDS3AlmProv,'adTa5kSingleDS3EnhancedAlmSlotProvTable':adTa5kSingleDS3EnhancedAlmSlotProvTable,'adTa5kSingleDS3EnhancedAlmSlotProvEntry':adTa5kSingleDS3EnhancedAlmSlotProvEntry,'adSingleDs3EnhancedAlmSlotLOSSeverity':adSingleDs3EnhancedAlmSlotLOSSeverity,'adSingleDs3EnhancedAlmSlotLOSSuppression':adSingleDs3EnhancedAlmSlotLOSSuppression,'adSingleDs3EnhancedAlmSlotLOFSeverity':adSingleDs3EnhancedAlmSlotLOFSeverity,'adSingleDs3EnhancedAlmSlotLOFSuppression':adSingleDs3EnhancedAlmSlotLOFSuppression,'adSingleDs3EnhancedAlmSlotAISSeverity':adSingleDs3EnhancedAlmSlotAISSeverity,'adSingleDs3EnhancedAlmSlotAISSuppression':adSingleDs3EnhancedAlmSlotAISSuppression,'adSingleDs3EnhancedAlmSlotRAISeverity':adSingleDs3EnhancedAlmSlotRAISeverity,'adSingleDs3EnhancedAlmSlotRAISuppression':adSingleDs3EnhancedAlmSlotRAISuppression,'adSingleDS3EnhancedAlmSlotLOSEnable':adSingleDS3EnhancedAlmSlotLOSEnable,'adSingleDS3EnhancedAlmSlotLOFEnable':adSingleDS3EnhancedAlmSlotLOFEnable,'adSingleDS3EnhancedAlmSlotAISEnable':adSingleDS3EnhancedAlmSlotAISEnable,'adSingleDS3EnhancedAlmSlotRAIEnable':adSingleDS3EnhancedAlmSlotRAIEnable,'adTa5kSingleDS3MibConformance':adTa5kSingleDS3MibConformance,'adTa5kSingleDS3MibGroups':adTa5kSingleDS3MibGroups,'adTa5kSingleDS3PortProvGroup':adTa5kSingleDS3PortProvGroup,'adTa5kSingleDS3TrapGroup':adTa5kSingleDS3TrapGroup,'adTa5kSingleDs3ModuleIdentity':adTa5kSingleDs3ModuleIdentity})