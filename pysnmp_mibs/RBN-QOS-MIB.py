_Ad='rbnQosHierarchicalPolicyStatsGroup'
_Ac='rbnQosHierarchicalPClassDroppedPkts'
_Ab='rbnQosHierarchicalPClassDroppedOctets'
_Aa='rbnQosHierarchicalPClassName'
_AZ='rbnQosHierarchicalPolicyDroppedPkts'
_AY='rbnQosHierarchicalPolicyDroppedOctets'
_AX='rbnQosHierarchicalPolicyName'
_AW='rbnQosSubsRLClassViolateDroppedPkts'
_AV='rbnQosSubsRLClassViolateDroppedOctets'
_AU='rbnQosSubsRLClassViolatePkts'
_AT='rbnQosSubsRLClassViolateOctets'
_AS='rbnQosSubsRLClassExceedDroppedPkts'
_AR='rbnQosSubsRLClassExceedDroppedOctets'
_AQ='rbnQosSubsRLClassExceedPkts'
_AP='rbnQosSubsRLClassExceedOctets'
_AO='rbnQosSubsRLClassConformDroppedPkts'
_AN='rbnQosSubsRLClassConformDroppedOctets'
_AM='rbnQosSubsRLClassConformPkts'
_AL='rbnQosSubsRLClassConformOctets'
_AK='rbnQosSubsRLClassName'
_AJ='rbnQosSubsRLPolicyName'
_AI='rbnQosIfRLClassViolateDroppedPkts'
_AH='rbnQosIfRLClassViolateDroppedOctets'
_AG='rbnQosIfRLClassViolatePkts'
_AF='rbnQosIfRLClassViolateOctets'
_AE='rbnQosIfRLClassExceedDroppedPkts'
_AD='rbnQosIfRLClassExceedDroppedOctets'
_AC='rbnQosIfRLClassExceedPkts'
_AB='rbnQosIfRLClassExceedOctets'
_AA='rbnQosIfRLClassConformDroppedPkts'
_A9='rbnQosIfRLClassConformDroppedOctets'
_A8='rbnQosIfRLClassConformPkts'
_A7='rbnQosIfRLClassConformOctets'
_A6='rbnQosIfRLClassName'
_A5='rbnQosIfRLPolicyName'
_A4='rbnQosSubsQueueHCTailDroppedPkts'
_A3='rbnQosSubsQueueHCTailDroppedOctets'
_A2='rbnQosSubsQueueHCWredDroppedPkts'
_A1='rbnQosSubsQueueHCWredDroppedOctets'
_A0='rbnQosSubsQueueHCOutPkts'
_z='rbnQosSubsQueueHCOutOctets'
_y='rbnQosSubsQueueTailDroppedPkts'
_x='rbnQosSubsQueueTailDroppedOctets'
_w='rbnQosSubsQueueWredDroppedPkts'
_v='rbnQosSubsQueueWredDroppedOctets'
_u='rbnQosSubsQueueOutPkts'
_t='rbnQosSubsQueueOutOctets'
_s='rbnQosSubsQueuePolicyName'
_r='rbnQosIfQueueHCTailDroppedPkts'
_q='rbnQosIfQueueTailDroppedPkts'
_p='rbnQosIfQueueHCTailDroppedOctets'
_o='rbnQosIfQueueTailDroppedOctets'
_n='rbnQosIfQueueHCWredDroppedPkts'
_m='rbnQosIfQueueWredDroppedPkts'
_l='rbnQosIfQueueHCWredDroppedOctets'
_k='rbnQosIfQueueWredDroppedOctets'
_j='rbnQosIfQueueHCOutPkts'
_i='rbnQosIfQueueOutPkts'
_h='rbnQosIfQueueHCOutOctets'
_g='rbnQosIfQueueOutOctets'
_f='rbnQosIfHCOutDroppedOctets'
_e='rbnQosIfOutDroppedOctets'
_d='rbnQosIfHCInDroppedOctets'
_c='rbnQosIfInDroppedOctets'
_b='rbnQosIfHCOutOctets'
_a='rbnQosIfOutOctets'
_Z='rbnQosIfHCInOctets'
_Y='rbnQosIfInOctets'
_X='rbnQosHierarchicalPClassId'
_W='rbnQosSubsRLClassId'
_V='rbnQosSubsRLPolicyType'
_U='rbnQosIfRLClassId'
_T='rbnQosIfRLPolicyType'
_S='rbnQosSubsQueueId'
_R='rbnQosIfQueueId'
_Q='rbnQosSubscriberRLClassStatsGroup'
_P='rbnQosIfRLClassStatsGroup'
_O='rbnQosHierarchicalPolicyType'
_N='Unsigned32'
_M='rbnSubsActiveSessionId'
_L='rbnSubsActiveName'
_K='rbnQosSubscriberQueueGroup'
_J='rbnQosIfQueueGroup'
_I='RBN-SUBSCRIBER-ACTIVE-MIB'
_H='rbnQosIfGroup'
_G='ifIndex'
_F='IF-MIB'
_E='not-accessible'
_D='SnmpAdminString'
_C='read-only'
_B='RBN-QOS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
rbnSubsActiveName,rbnSubsActiveSessionId=mibBuilder.importSymbols(_I,_L,_M)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnQosMib=ModuleIdentity((1,3,6,1,4,1,2352,2,22))
if mibBuilder.loadTexts:rbnQosMib.setRevisions(('2007-07-30 00:00','2006-09-12 00:00','2005-09-26 00:00','2003-07-18 00:00','2002-03-22 00:00'))
class RbnQosPolicyType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('policing',1),('metering',2),('edrr',3),('mdrr',4),('pq',5),('atmwfq',6),('pwfq',7)))
class RbnQosClassId(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RbnQosMibObjects_ObjectIdentity=ObjectIdentity
rbnQosMibObjects=_RbnQosMibObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,22,1))
_RbnQosInterfaceTable_Object=MibTable
rbnQosInterfaceTable=_RbnQosInterfaceTable_Object((1,3,6,1,4,1,2352,2,22,1,1))
if mibBuilder.loadTexts:rbnQosInterfaceTable.setStatus(_A)
_RbnQosInterfaceEntry_Object=MibTableRow
rbnQosInterfaceEntry=_RbnQosInterfaceEntry_Object((1,3,6,1,4,1,2352,2,22,1,1,1))
rbnQosInterfaceEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:rbnQosInterfaceEntry.setStatus(_A)
_RbnQosIfInOctets_Type=Counter32
_RbnQosIfInOctets_Object=MibTableColumn
rbnQosIfInOctets=_RbnQosIfInOctets_Object((1,3,6,1,4,1,2352,2,22,1,1,1,1),_RbnQosIfInOctets_Type())
rbnQosIfInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfInOctets.setStatus(_A)
_RbnQosIfHCInOctets_Type=Counter64
_RbnQosIfHCInOctets_Object=MibTableColumn
rbnQosIfHCInOctets=_RbnQosIfHCInOctets_Object((1,3,6,1,4,1,2352,2,22,1,1,1,2),_RbnQosIfHCInOctets_Type())
rbnQosIfHCInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfHCInOctets.setStatus(_A)
_RbnQosIfOutOctets_Type=Counter32
_RbnQosIfOutOctets_Object=MibTableColumn
rbnQosIfOutOctets=_RbnQosIfOutOctets_Object((1,3,6,1,4,1,2352,2,22,1,1,1,3),_RbnQosIfOutOctets_Type())
rbnQosIfOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfOutOctets.setStatus(_A)
_RbnQosIfHCOutOctets_Type=Counter64
_RbnQosIfHCOutOctets_Object=MibTableColumn
rbnQosIfHCOutOctets=_RbnQosIfHCOutOctets_Object((1,3,6,1,4,1,2352,2,22,1,1,1,4),_RbnQosIfHCOutOctets_Type())
rbnQosIfHCOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfHCOutOctets.setStatus(_A)
_RbnQosIfInDroppedOctets_Type=Counter32
_RbnQosIfInDroppedOctets_Object=MibTableColumn
rbnQosIfInDroppedOctets=_RbnQosIfInDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,1,1,5),_RbnQosIfInDroppedOctets_Type())
rbnQosIfInDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfInDroppedOctets.setStatus(_A)
_RbnQosIfHCInDroppedOctets_Type=Counter64
_RbnQosIfHCInDroppedOctets_Object=MibTableColumn
rbnQosIfHCInDroppedOctets=_RbnQosIfHCInDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,1,1,6),_RbnQosIfHCInDroppedOctets_Type())
rbnQosIfHCInDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfHCInDroppedOctets.setStatus(_A)
_RbnQosIfOutDroppedOctets_Type=Counter32
_RbnQosIfOutDroppedOctets_Object=MibTableColumn
rbnQosIfOutDroppedOctets=_RbnQosIfOutDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,1,1,7),_RbnQosIfOutDroppedOctets_Type())
rbnQosIfOutDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfOutDroppedOctets.setStatus(_A)
_RbnQosIfHCOutDroppedOctets_Type=Counter64
_RbnQosIfHCOutDroppedOctets_Object=MibTableColumn
rbnQosIfHCOutDroppedOctets=_RbnQosIfHCOutDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,1,1,8),_RbnQosIfHCOutDroppedOctets_Type())
rbnQosIfHCOutDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfHCOutDroppedOctets.setStatus(_A)
_RbnQosInterfaceQueueStatsTable_Object=MibTable
rbnQosInterfaceQueueStatsTable=_RbnQosInterfaceQueueStatsTable_Object((1,3,6,1,4,1,2352,2,22,1,2))
if mibBuilder.loadTexts:rbnQosInterfaceQueueStatsTable.setStatus(_A)
_RbnQosInterfaceQueueStatsEntry_Object=MibTableRow
rbnQosInterfaceQueueStatsEntry=_RbnQosInterfaceQueueStatsEntry_Object((1,3,6,1,4,1,2352,2,22,1,2,1))
rbnQosInterfaceQueueStatsEntry.setIndexNames((0,_F,_G),(0,_B,_R))
if mibBuilder.loadTexts:rbnQosInterfaceQueueStatsEntry.setStatus(_A)
class _RbnQosIfQueueId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RbnQosIfQueueId_Type.__name__=_N
_RbnQosIfQueueId_Object=MibTableColumn
rbnQosIfQueueId=_RbnQosIfQueueId_Object((1,3,6,1,4,1,2352,2,22,1,2,1,1),_RbnQosIfQueueId_Type())
rbnQosIfQueueId.setMaxAccess(_E)
if mibBuilder.loadTexts:rbnQosIfQueueId.setStatus(_A)
_RbnQosIfQueueOutOctets_Type=Counter32
_RbnQosIfQueueOutOctets_Object=MibTableColumn
rbnQosIfQueueOutOctets=_RbnQosIfQueueOutOctets_Object((1,3,6,1,4,1,2352,2,22,1,2,1,2),_RbnQosIfQueueOutOctets_Type())
rbnQosIfQueueOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfQueueOutOctets.setStatus(_A)
_RbnQosIfQueueOutPkts_Type=Counter32
_RbnQosIfQueueOutPkts_Object=MibTableColumn
rbnQosIfQueueOutPkts=_RbnQosIfQueueOutPkts_Object((1,3,6,1,4,1,2352,2,22,1,2,1,3),_RbnQosIfQueueOutPkts_Type())
rbnQosIfQueueOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfQueueOutPkts.setStatus(_A)
_RbnQosIfQueueWredDroppedOctets_Type=Counter32
_RbnQosIfQueueWredDroppedOctets_Object=MibTableColumn
rbnQosIfQueueWredDroppedOctets=_RbnQosIfQueueWredDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,2,1,4),_RbnQosIfQueueWredDroppedOctets_Type())
rbnQosIfQueueWredDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfQueueWredDroppedOctets.setStatus(_A)
_RbnQosIfQueueWredDroppedPkts_Type=Counter32
_RbnQosIfQueueWredDroppedPkts_Object=MibTableColumn
rbnQosIfQueueWredDroppedPkts=_RbnQosIfQueueWredDroppedPkts_Object((1,3,6,1,4,1,2352,2,22,1,2,1,5),_RbnQosIfQueueWredDroppedPkts_Type())
rbnQosIfQueueWredDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfQueueWredDroppedPkts.setStatus(_A)
_RbnQosIfQueueTailDroppedOctets_Type=Counter32
_RbnQosIfQueueTailDroppedOctets_Object=MibTableColumn
rbnQosIfQueueTailDroppedOctets=_RbnQosIfQueueTailDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,2,1,6),_RbnQosIfQueueTailDroppedOctets_Type())
rbnQosIfQueueTailDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfQueueTailDroppedOctets.setStatus(_A)
_RbnQosIfQueueTailDroppedPkts_Type=Counter32
_RbnQosIfQueueTailDroppedPkts_Object=MibTableColumn
rbnQosIfQueueTailDroppedPkts=_RbnQosIfQueueTailDroppedPkts_Object((1,3,6,1,4,1,2352,2,22,1,2,1,7),_RbnQosIfQueueTailDroppedPkts_Type())
rbnQosIfQueueTailDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfQueueTailDroppedPkts.setStatus(_A)
_RbnQosIfQueueHCOutOctets_Type=Counter64
_RbnQosIfQueueHCOutOctets_Object=MibTableColumn
rbnQosIfQueueHCOutOctets=_RbnQosIfQueueHCOutOctets_Object((1,3,6,1,4,1,2352,2,22,1,2,1,8),_RbnQosIfQueueHCOutOctets_Type())
rbnQosIfQueueHCOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfQueueHCOutOctets.setStatus(_A)
_RbnQosIfQueueHCOutPkts_Type=Counter64
_RbnQosIfQueueHCOutPkts_Object=MibTableColumn
rbnQosIfQueueHCOutPkts=_RbnQosIfQueueHCOutPkts_Object((1,3,6,1,4,1,2352,2,22,1,2,1,9),_RbnQosIfQueueHCOutPkts_Type())
rbnQosIfQueueHCOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfQueueHCOutPkts.setStatus(_A)
_RbnQosIfQueueHCWredDroppedOctets_Type=Counter64
_RbnQosIfQueueHCWredDroppedOctets_Object=MibTableColumn
rbnQosIfQueueHCWredDroppedOctets=_RbnQosIfQueueHCWredDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,2,1,10),_RbnQosIfQueueHCWredDroppedOctets_Type())
rbnQosIfQueueHCWredDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfQueueHCWredDroppedOctets.setStatus(_A)
_RbnQosIfQueueHCWredDroppedPkts_Type=Counter64
_RbnQosIfQueueHCWredDroppedPkts_Object=MibTableColumn
rbnQosIfQueueHCWredDroppedPkts=_RbnQosIfQueueHCWredDroppedPkts_Object((1,3,6,1,4,1,2352,2,22,1,2,1,11),_RbnQosIfQueueHCWredDroppedPkts_Type())
rbnQosIfQueueHCWredDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfQueueHCWredDroppedPkts.setStatus(_A)
_RbnQosIfQueueHCTailDroppedOctets_Type=Counter64
_RbnQosIfQueueHCTailDroppedOctets_Object=MibTableColumn
rbnQosIfQueueHCTailDroppedOctets=_RbnQosIfQueueHCTailDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,2,1,12),_RbnQosIfQueueHCTailDroppedOctets_Type())
rbnQosIfQueueHCTailDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfQueueHCTailDroppedOctets.setStatus(_A)
_RbnQosIfQueueHCTailDroppedPkts_Type=Counter64
_RbnQosIfQueueHCTailDroppedPkts_Object=MibTableColumn
rbnQosIfQueueHCTailDroppedPkts=_RbnQosIfQueueHCTailDroppedPkts_Object((1,3,6,1,4,1,2352,2,22,1,2,1,13),_RbnQosIfQueueHCTailDroppedPkts_Type())
rbnQosIfQueueHCTailDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfQueueHCTailDroppedPkts.setStatus(_A)
_RbnQosSubscriberQueueStatsTable_Object=MibTable
rbnQosSubscriberQueueStatsTable=_RbnQosSubscriberQueueStatsTable_Object((1,3,6,1,4,1,2352,2,22,1,3))
if mibBuilder.loadTexts:rbnQosSubscriberQueueStatsTable.setStatus(_A)
_RbnQosSubscriberQueueStatsEntry_Object=MibTableRow
rbnQosSubscriberQueueStatsEntry=_RbnQosSubscriberQueueStatsEntry_Object((1,3,6,1,4,1,2352,2,22,1,3,1))
rbnQosSubscriberQueueStatsEntry.setIndexNames((0,_I,_L),(0,_I,_M),(0,_B,_S))
if mibBuilder.loadTexts:rbnQosSubscriberQueueStatsEntry.setStatus(_A)
class _RbnQosSubsQueueId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RbnQosSubsQueueId_Type.__name__=_N
_RbnQosSubsQueueId_Object=MibTableColumn
rbnQosSubsQueueId=_RbnQosSubsQueueId_Object((1,3,6,1,4,1,2352,2,22,1,3,1,1),_RbnQosSubsQueueId_Type())
rbnQosSubsQueueId.setMaxAccess(_E)
if mibBuilder.loadTexts:rbnQosSubsQueueId.setStatus(_A)
class _RbnQosSubsQueuePolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,39))
_RbnQosSubsQueuePolicyName_Type.__name__=_D
_RbnQosSubsQueuePolicyName_Object=MibTableColumn
rbnQosSubsQueuePolicyName=_RbnQosSubsQueuePolicyName_Object((1,3,6,1,4,1,2352,2,22,1,3,1,2),_RbnQosSubsQueuePolicyName_Type())
rbnQosSubsQueuePolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsQueuePolicyName.setStatus(_A)
_RbnQosSubsQueueOutOctets_Type=Counter32
_RbnQosSubsQueueOutOctets_Object=MibTableColumn
rbnQosSubsQueueOutOctets=_RbnQosSubsQueueOutOctets_Object((1,3,6,1,4,1,2352,2,22,1,3,1,3),_RbnQosSubsQueueOutOctets_Type())
rbnQosSubsQueueOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsQueueOutOctets.setStatus(_A)
_RbnQosSubsQueueOutPkts_Type=Counter32
_RbnQosSubsQueueOutPkts_Object=MibTableColumn
rbnQosSubsQueueOutPkts=_RbnQosSubsQueueOutPkts_Object((1,3,6,1,4,1,2352,2,22,1,3,1,4),_RbnQosSubsQueueOutPkts_Type())
rbnQosSubsQueueOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsQueueOutPkts.setStatus(_A)
_RbnQosSubsQueueWredDroppedOctets_Type=Counter32
_RbnQosSubsQueueWredDroppedOctets_Object=MibTableColumn
rbnQosSubsQueueWredDroppedOctets=_RbnQosSubsQueueWredDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,3,1,5),_RbnQosSubsQueueWredDroppedOctets_Type())
rbnQosSubsQueueWredDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsQueueWredDroppedOctets.setStatus(_A)
_RbnQosSubsQueueWredDroppedPkts_Type=Counter32
_RbnQosSubsQueueWredDroppedPkts_Object=MibTableColumn
rbnQosSubsQueueWredDroppedPkts=_RbnQosSubsQueueWredDroppedPkts_Object((1,3,6,1,4,1,2352,2,22,1,3,1,6),_RbnQosSubsQueueWredDroppedPkts_Type())
rbnQosSubsQueueWredDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsQueueWredDroppedPkts.setStatus(_A)
_RbnQosSubsQueueTailDroppedOctets_Type=Counter32
_RbnQosSubsQueueTailDroppedOctets_Object=MibTableColumn
rbnQosSubsQueueTailDroppedOctets=_RbnQosSubsQueueTailDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,3,1,7),_RbnQosSubsQueueTailDroppedOctets_Type())
rbnQosSubsQueueTailDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsQueueTailDroppedOctets.setStatus(_A)
_RbnQosSubsQueueTailDroppedPkts_Type=Counter32
_RbnQosSubsQueueTailDroppedPkts_Object=MibTableColumn
rbnQosSubsQueueTailDroppedPkts=_RbnQosSubsQueueTailDroppedPkts_Object((1,3,6,1,4,1,2352,2,22,1,3,1,8),_RbnQosSubsQueueTailDroppedPkts_Type())
rbnQosSubsQueueTailDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsQueueTailDroppedPkts.setStatus(_A)
_RbnQosSubsQueueHCOutOctets_Type=Counter64
_RbnQosSubsQueueHCOutOctets_Object=MibTableColumn
rbnQosSubsQueueHCOutOctets=_RbnQosSubsQueueHCOutOctets_Object((1,3,6,1,4,1,2352,2,22,1,3,1,9),_RbnQosSubsQueueHCOutOctets_Type())
rbnQosSubsQueueHCOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsQueueHCOutOctets.setStatus(_A)
_RbnQosSubsQueueHCOutPkts_Type=Counter64
_RbnQosSubsQueueHCOutPkts_Object=MibTableColumn
rbnQosSubsQueueHCOutPkts=_RbnQosSubsQueueHCOutPkts_Object((1,3,6,1,4,1,2352,2,22,1,3,1,10),_RbnQosSubsQueueHCOutPkts_Type())
rbnQosSubsQueueHCOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsQueueHCOutPkts.setStatus(_A)
_RbnQosSubsQueueHCWredDroppedOctets_Type=Counter64
_RbnQosSubsQueueHCWredDroppedOctets_Object=MibTableColumn
rbnQosSubsQueueHCWredDroppedOctets=_RbnQosSubsQueueHCWredDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,3,1,11),_RbnQosSubsQueueHCWredDroppedOctets_Type())
rbnQosSubsQueueHCWredDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsQueueHCWredDroppedOctets.setStatus(_A)
_RbnQosSubsQueueHCWredDroppedPkts_Type=Counter64
_RbnQosSubsQueueHCWredDroppedPkts_Object=MibTableColumn
rbnQosSubsQueueHCWredDroppedPkts=_RbnQosSubsQueueHCWredDroppedPkts_Object((1,3,6,1,4,1,2352,2,22,1,3,1,12),_RbnQosSubsQueueHCWredDroppedPkts_Type())
rbnQosSubsQueueHCWredDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsQueueHCWredDroppedPkts.setStatus(_A)
_RbnQosSubsQueueHCTailDroppedOctets_Type=Counter64
_RbnQosSubsQueueHCTailDroppedOctets_Object=MibTableColumn
rbnQosSubsQueueHCTailDroppedOctets=_RbnQosSubsQueueHCTailDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,3,1,13),_RbnQosSubsQueueHCTailDroppedOctets_Type())
rbnQosSubsQueueHCTailDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsQueueHCTailDroppedOctets.setStatus(_A)
_RbnQosSubsQueueHCTailDroppedPkts_Type=Counter64
_RbnQosSubsQueueHCTailDroppedPkts_Object=MibTableColumn
rbnQosSubsQueueHCTailDroppedPkts=_RbnQosSubsQueueHCTailDroppedPkts_Object((1,3,6,1,4,1,2352,2,22,1,3,1,14),_RbnQosSubsQueueHCTailDroppedPkts_Type())
rbnQosSubsQueueHCTailDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsQueueHCTailDroppedPkts.setStatus(_A)
_RbnQosIntfRLClassStatsTable_Object=MibTable
rbnQosIntfRLClassStatsTable=_RbnQosIntfRLClassStatsTable_Object((1,3,6,1,4,1,2352,2,22,1,4))
if mibBuilder.loadTexts:rbnQosIntfRLClassStatsTable.setStatus(_A)
_RbnQosIntfRLClassStatsEntry_Object=MibTableRow
rbnQosIntfRLClassStatsEntry=_RbnQosIntfRLClassStatsEntry_Object((1,3,6,1,4,1,2352,2,22,1,4,1))
rbnQosIntfRLClassStatsEntry.setIndexNames((0,_F,_G),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:rbnQosIntfRLClassStatsEntry.setStatus(_A)
_RbnQosIfRLPolicyType_Type=RbnQosPolicyType
_RbnQosIfRLPolicyType_Object=MibTableColumn
rbnQosIfRLPolicyType=_RbnQosIfRLPolicyType_Object((1,3,6,1,4,1,2352,2,22,1,4,1,1),_RbnQosIfRLPolicyType_Type())
rbnQosIfRLPolicyType.setMaxAccess(_E)
if mibBuilder.loadTexts:rbnQosIfRLPolicyType.setStatus(_A)
_RbnQosIfRLClassId_Type=RbnQosClassId
_RbnQosIfRLClassId_Object=MibTableColumn
rbnQosIfRLClassId=_RbnQosIfRLClassId_Object((1,3,6,1,4,1,2352,2,22,1,4,1,2),_RbnQosIfRLClassId_Type())
rbnQosIfRLClassId.setMaxAccess(_E)
if mibBuilder.loadTexts:rbnQosIfRLClassId.setStatus(_A)
class _RbnQosIfRLPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,39))
_RbnQosIfRLPolicyName_Type.__name__=_D
_RbnQosIfRLPolicyName_Object=MibTableColumn
rbnQosIfRLPolicyName=_RbnQosIfRLPolicyName_Object((1,3,6,1,4,1,2352,2,22,1,4,1,3),_RbnQosIfRLPolicyName_Type())
rbnQosIfRLPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfRLPolicyName.setStatus(_A)
class _RbnQosIfRLClassName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,39))
_RbnQosIfRLClassName_Type.__name__=_D
_RbnQosIfRLClassName_Object=MibTableColumn
rbnQosIfRLClassName=_RbnQosIfRLClassName_Object((1,3,6,1,4,1,2352,2,22,1,4,1,4),_RbnQosIfRLClassName_Type())
rbnQosIfRLClassName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfRLClassName.setStatus(_A)
_RbnQosIfRLClassConformOctets_Type=Counter64
_RbnQosIfRLClassConformOctets_Object=MibTableColumn
rbnQosIfRLClassConformOctets=_RbnQosIfRLClassConformOctets_Object((1,3,6,1,4,1,2352,2,22,1,4,1,5),_RbnQosIfRLClassConformOctets_Type())
rbnQosIfRLClassConformOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfRLClassConformOctets.setStatus(_A)
_RbnQosIfRLClassConformPkts_Type=Counter64
_RbnQosIfRLClassConformPkts_Object=MibTableColumn
rbnQosIfRLClassConformPkts=_RbnQosIfRLClassConformPkts_Object((1,3,6,1,4,1,2352,2,22,1,4,1,6),_RbnQosIfRLClassConformPkts_Type())
rbnQosIfRLClassConformPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfRLClassConformPkts.setStatus(_A)
_RbnQosIfRLClassConformDroppedOctets_Type=Counter64
_RbnQosIfRLClassConformDroppedOctets_Object=MibTableColumn
rbnQosIfRLClassConformDroppedOctets=_RbnQosIfRLClassConformDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,4,1,7),_RbnQosIfRLClassConformDroppedOctets_Type())
rbnQosIfRLClassConformDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfRLClassConformDroppedOctets.setStatus(_A)
_RbnQosIfRLClassConformDroppedPkts_Type=Counter64
_RbnQosIfRLClassConformDroppedPkts_Object=MibTableColumn
rbnQosIfRLClassConformDroppedPkts=_RbnQosIfRLClassConformDroppedPkts_Object((1,3,6,1,4,1,2352,2,22,1,4,1,8),_RbnQosIfRLClassConformDroppedPkts_Type())
rbnQosIfRLClassConformDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfRLClassConformDroppedPkts.setStatus(_A)
_RbnQosIfRLClassExceedOctets_Type=Counter64
_RbnQosIfRLClassExceedOctets_Object=MibTableColumn
rbnQosIfRLClassExceedOctets=_RbnQosIfRLClassExceedOctets_Object((1,3,6,1,4,1,2352,2,22,1,4,1,9),_RbnQosIfRLClassExceedOctets_Type())
rbnQosIfRLClassExceedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfRLClassExceedOctets.setStatus(_A)
_RbnQosIfRLClassExceedPkts_Type=Counter64
_RbnQosIfRLClassExceedPkts_Object=MibTableColumn
rbnQosIfRLClassExceedPkts=_RbnQosIfRLClassExceedPkts_Object((1,3,6,1,4,1,2352,2,22,1,4,1,10),_RbnQosIfRLClassExceedPkts_Type())
rbnQosIfRLClassExceedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfRLClassExceedPkts.setStatus(_A)
_RbnQosIfRLClassExceedDroppedOctets_Type=Counter64
_RbnQosIfRLClassExceedDroppedOctets_Object=MibTableColumn
rbnQosIfRLClassExceedDroppedOctets=_RbnQosIfRLClassExceedDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,4,1,11),_RbnQosIfRLClassExceedDroppedOctets_Type())
rbnQosIfRLClassExceedDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfRLClassExceedDroppedOctets.setStatus(_A)
_RbnQosIfRLClassExceedDroppedPkts_Type=Counter64
_RbnQosIfRLClassExceedDroppedPkts_Object=MibTableColumn
rbnQosIfRLClassExceedDroppedPkts=_RbnQosIfRLClassExceedDroppedPkts_Object((1,3,6,1,4,1,2352,2,22,1,4,1,12),_RbnQosIfRLClassExceedDroppedPkts_Type())
rbnQosIfRLClassExceedDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfRLClassExceedDroppedPkts.setStatus(_A)
_RbnQosIfRLClassViolateOctets_Type=Counter64
_RbnQosIfRLClassViolateOctets_Object=MibTableColumn
rbnQosIfRLClassViolateOctets=_RbnQosIfRLClassViolateOctets_Object((1,3,6,1,4,1,2352,2,22,1,4,1,13),_RbnQosIfRLClassViolateOctets_Type())
rbnQosIfRLClassViolateOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfRLClassViolateOctets.setStatus(_A)
_RbnQosIfRLClassViolatePkts_Type=Counter64
_RbnQosIfRLClassViolatePkts_Object=MibTableColumn
rbnQosIfRLClassViolatePkts=_RbnQosIfRLClassViolatePkts_Object((1,3,6,1,4,1,2352,2,22,1,4,1,14),_RbnQosIfRLClassViolatePkts_Type())
rbnQosIfRLClassViolatePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfRLClassViolatePkts.setStatus(_A)
_RbnQosIfRLClassViolateDroppedOctets_Type=Counter64
_RbnQosIfRLClassViolateDroppedOctets_Object=MibTableColumn
rbnQosIfRLClassViolateDroppedOctets=_RbnQosIfRLClassViolateDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,4,1,15),_RbnQosIfRLClassViolateDroppedOctets_Type())
rbnQosIfRLClassViolateDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfRLClassViolateDroppedOctets.setStatus(_A)
_RbnQosIfRLClassViolateDroppedPkts_Type=Counter64
_RbnQosIfRLClassViolateDroppedPkts_Object=MibTableColumn
rbnQosIfRLClassViolateDroppedPkts=_RbnQosIfRLClassViolateDroppedPkts_Object((1,3,6,1,4,1,2352,2,22,1,4,1,16),_RbnQosIfRLClassViolateDroppedPkts_Type())
rbnQosIfRLClassViolateDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosIfRLClassViolateDroppedPkts.setStatus(_A)
_RbnQosSubscriberRLClassStatsTable_Object=MibTable
rbnQosSubscriberRLClassStatsTable=_RbnQosSubscriberRLClassStatsTable_Object((1,3,6,1,4,1,2352,2,22,1,5))
if mibBuilder.loadTexts:rbnQosSubscriberRLClassStatsTable.setStatus(_A)
_RbnQosSubscriberRLClassStatsEntry_Object=MibTableRow
rbnQosSubscriberRLClassStatsEntry=_RbnQosSubscriberRLClassStatsEntry_Object((1,3,6,1,4,1,2352,2,22,1,5,1))
rbnQosSubscriberRLClassStatsEntry.setIndexNames((0,_I,_L),(0,_I,_M),(0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:rbnQosSubscriberRLClassStatsEntry.setStatus(_A)
_RbnQosSubsRLPolicyType_Type=RbnQosPolicyType
_RbnQosSubsRLPolicyType_Object=MibTableColumn
rbnQosSubsRLPolicyType=_RbnQosSubsRLPolicyType_Object((1,3,6,1,4,1,2352,2,22,1,5,1,1),_RbnQosSubsRLPolicyType_Type())
rbnQosSubsRLPolicyType.setMaxAccess(_E)
if mibBuilder.loadTexts:rbnQosSubsRLPolicyType.setStatus(_A)
_RbnQosSubsRLClassId_Type=RbnQosClassId
_RbnQosSubsRLClassId_Object=MibTableColumn
rbnQosSubsRLClassId=_RbnQosSubsRLClassId_Object((1,3,6,1,4,1,2352,2,22,1,5,1,2),_RbnQosSubsRLClassId_Type())
rbnQosSubsRLClassId.setMaxAccess(_E)
if mibBuilder.loadTexts:rbnQosSubsRLClassId.setStatus(_A)
class _RbnQosSubsRLPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,39))
_RbnQosSubsRLPolicyName_Type.__name__=_D
_RbnQosSubsRLPolicyName_Object=MibTableColumn
rbnQosSubsRLPolicyName=_RbnQosSubsRLPolicyName_Object((1,3,6,1,4,1,2352,2,22,1,5,1,3),_RbnQosSubsRLPolicyName_Type())
rbnQosSubsRLPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsRLPolicyName.setStatus(_A)
class _RbnQosSubsRLClassName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,39))
_RbnQosSubsRLClassName_Type.__name__=_D
_RbnQosSubsRLClassName_Object=MibTableColumn
rbnQosSubsRLClassName=_RbnQosSubsRLClassName_Object((1,3,6,1,4,1,2352,2,22,1,5,1,4),_RbnQosSubsRLClassName_Type())
rbnQosSubsRLClassName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsRLClassName.setStatus(_A)
_RbnQosSubsRLClassConformOctets_Type=Counter64
_RbnQosSubsRLClassConformOctets_Object=MibTableColumn
rbnQosSubsRLClassConformOctets=_RbnQosSubsRLClassConformOctets_Object((1,3,6,1,4,1,2352,2,22,1,5,1,5),_RbnQosSubsRLClassConformOctets_Type())
rbnQosSubsRLClassConformOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsRLClassConformOctets.setStatus(_A)
_RbnQosSubsRLClassConformPkts_Type=Counter64
_RbnQosSubsRLClassConformPkts_Object=MibTableColumn
rbnQosSubsRLClassConformPkts=_RbnQosSubsRLClassConformPkts_Object((1,3,6,1,4,1,2352,2,22,1,5,1,6),_RbnQosSubsRLClassConformPkts_Type())
rbnQosSubsRLClassConformPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsRLClassConformPkts.setStatus(_A)
_RbnQosSubsRLClassConformDroppedOctets_Type=Counter64
_RbnQosSubsRLClassConformDroppedOctets_Object=MibTableColumn
rbnQosSubsRLClassConformDroppedOctets=_RbnQosSubsRLClassConformDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,5,1,7),_RbnQosSubsRLClassConformDroppedOctets_Type())
rbnQosSubsRLClassConformDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsRLClassConformDroppedOctets.setStatus(_A)
_RbnQosSubsRLClassConformDroppedPkts_Type=Counter64
_RbnQosSubsRLClassConformDroppedPkts_Object=MibTableColumn
rbnQosSubsRLClassConformDroppedPkts=_RbnQosSubsRLClassConformDroppedPkts_Object((1,3,6,1,4,1,2352,2,22,1,5,1,8),_RbnQosSubsRLClassConformDroppedPkts_Type())
rbnQosSubsRLClassConformDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsRLClassConformDroppedPkts.setStatus(_A)
_RbnQosSubsRLClassExceedOctets_Type=Counter64
_RbnQosSubsRLClassExceedOctets_Object=MibTableColumn
rbnQosSubsRLClassExceedOctets=_RbnQosSubsRLClassExceedOctets_Object((1,3,6,1,4,1,2352,2,22,1,5,1,9),_RbnQosSubsRLClassExceedOctets_Type())
rbnQosSubsRLClassExceedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsRLClassExceedOctets.setStatus(_A)
_RbnQosSubsRLClassExceedPkts_Type=Counter64
_RbnQosSubsRLClassExceedPkts_Object=MibTableColumn
rbnQosSubsRLClassExceedPkts=_RbnQosSubsRLClassExceedPkts_Object((1,3,6,1,4,1,2352,2,22,1,5,1,10),_RbnQosSubsRLClassExceedPkts_Type())
rbnQosSubsRLClassExceedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsRLClassExceedPkts.setStatus(_A)
_RbnQosSubsRLClassExceedDroppedOctets_Type=Counter64
_RbnQosSubsRLClassExceedDroppedOctets_Object=MibTableColumn
rbnQosSubsRLClassExceedDroppedOctets=_RbnQosSubsRLClassExceedDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,5,1,11),_RbnQosSubsRLClassExceedDroppedOctets_Type())
rbnQosSubsRLClassExceedDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsRLClassExceedDroppedOctets.setStatus(_A)
_RbnQosSubsRLClassExceedDroppedPkts_Type=Counter64
_RbnQosSubsRLClassExceedDroppedPkts_Object=MibTableColumn
rbnQosSubsRLClassExceedDroppedPkts=_RbnQosSubsRLClassExceedDroppedPkts_Object((1,3,6,1,4,1,2352,2,22,1,5,1,12),_RbnQosSubsRLClassExceedDroppedPkts_Type())
rbnQosSubsRLClassExceedDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsRLClassExceedDroppedPkts.setStatus(_A)
_RbnQosSubsRLClassViolateOctets_Type=Counter64
_RbnQosSubsRLClassViolateOctets_Object=MibTableColumn
rbnQosSubsRLClassViolateOctets=_RbnQosSubsRLClassViolateOctets_Object((1,3,6,1,4,1,2352,2,22,1,5,1,13),_RbnQosSubsRLClassViolateOctets_Type())
rbnQosSubsRLClassViolateOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsRLClassViolateOctets.setStatus(_A)
_RbnQosSubsRLClassViolatePkts_Type=Counter64
_RbnQosSubsRLClassViolatePkts_Object=MibTableColumn
rbnQosSubsRLClassViolatePkts=_RbnQosSubsRLClassViolatePkts_Object((1,3,6,1,4,1,2352,2,22,1,5,1,14),_RbnQosSubsRLClassViolatePkts_Type())
rbnQosSubsRLClassViolatePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsRLClassViolatePkts.setStatus(_A)
_RbnQosSubsRLClassViolateDroppedOctets_Type=Counter64
_RbnQosSubsRLClassViolateDroppedOctets_Object=MibTableColumn
rbnQosSubsRLClassViolateDroppedOctets=_RbnQosSubsRLClassViolateDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,5,1,15),_RbnQosSubsRLClassViolateDroppedOctets_Type())
rbnQosSubsRLClassViolateDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsRLClassViolateDroppedOctets.setStatus(_A)
_RbnQosSubsRLClassViolateDroppedPkts_Type=Counter64
_RbnQosSubsRLClassViolateDroppedPkts_Object=MibTableColumn
rbnQosSubsRLClassViolateDroppedPkts=_RbnQosSubsRLClassViolateDroppedPkts_Object((1,3,6,1,4,1,2352,2,22,1,5,1,16),_RbnQosSubsRLClassViolateDroppedPkts_Type())
rbnQosSubsRLClassViolateDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosSubsRLClassViolateDroppedPkts.setStatus(_A)
_RbnQosHierarchicalPolicyStatsTable_Object=MibTable
rbnQosHierarchicalPolicyStatsTable=_RbnQosHierarchicalPolicyStatsTable_Object((1,3,6,1,4,1,2352,2,22,1,6))
if mibBuilder.loadTexts:rbnQosHierarchicalPolicyStatsTable.setStatus(_A)
_RbnQosHierarchicalPolicyStatsEntry_Object=MibTableRow
rbnQosHierarchicalPolicyStatsEntry=_RbnQosHierarchicalPolicyStatsEntry_Object((1,3,6,1,4,1,2352,2,22,1,6,1))
rbnQosHierarchicalPolicyStatsEntry.setIndexNames((0,_F,_G),(0,_B,_O))
if mibBuilder.loadTexts:rbnQosHierarchicalPolicyStatsEntry.setStatus(_A)
_RbnQosHierarchicalPolicyType_Type=RbnQosPolicyType
_RbnQosHierarchicalPolicyType_Object=MibTableColumn
rbnQosHierarchicalPolicyType=_RbnQosHierarchicalPolicyType_Object((1,3,6,1,4,1,2352,2,22,1,6,1,1),_RbnQosHierarchicalPolicyType_Type())
rbnQosHierarchicalPolicyType.setMaxAccess(_E)
if mibBuilder.loadTexts:rbnQosHierarchicalPolicyType.setStatus(_A)
class _RbnQosHierarchicalPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,39))
_RbnQosHierarchicalPolicyName_Type.__name__=_D
_RbnQosHierarchicalPolicyName_Object=MibTableColumn
rbnQosHierarchicalPolicyName=_RbnQosHierarchicalPolicyName_Object((1,3,6,1,4,1,2352,2,22,1,6,1,2),_RbnQosHierarchicalPolicyName_Type())
rbnQosHierarchicalPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosHierarchicalPolicyName.setStatus(_A)
_RbnQosHierarchicalPolicyDroppedOctets_Type=Counter64
_RbnQosHierarchicalPolicyDroppedOctets_Object=MibTableColumn
rbnQosHierarchicalPolicyDroppedOctets=_RbnQosHierarchicalPolicyDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,6,1,3),_RbnQosHierarchicalPolicyDroppedOctets_Type())
rbnQosHierarchicalPolicyDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosHierarchicalPolicyDroppedOctets.setStatus(_A)
_RbnQosHierarchicalPolicyDroppedPkts_Type=Counter64
_RbnQosHierarchicalPolicyDroppedPkts_Object=MibTableColumn
rbnQosHierarchicalPolicyDroppedPkts=_RbnQosHierarchicalPolicyDroppedPkts_Object((1,3,6,1,4,1,2352,2,22,1,6,1,4),_RbnQosHierarchicalPolicyDroppedPkts_Type())
rbnQosHierarchicalPolicyDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosHierarchicalPolicyDroppedPkts.setStatus(_A)
_RbnQosHierarchicalPClassStatsTable_Object=MibTable
rbnQosHierarchicalPClassStatsTable=_RbnQosHierarchicalPClassStatsTable_Object((1,3,6,1,4,1,2352,2,22,1,7))
if mibBuilder.loadTexts:rbnQosHierarchicalPClassStatsTable.setStatus(_A)
_RbnQosHierarchicalPClassStatsEntry_Object=MibTableRow
rbnQosHierarchicalPClassStatsEntry=_RbnQosHierarchicalPClassStatsEntry_Object((1,3,6,1,4,1,2352,2,22,1,7,1))
rbnQosHierarchicalPClassStatsEntry.setIndexNames((0,_F,_G),(0,_B,_O),(0,_B,_X))
if mibBuilder.loadTexts:rbnQosHierarchicalPClassStatsEntry.setStatus(_A)
_RbnQosHierarchicalPClassId_Type=RbnQosClassId
_RbnQosHierarchicalPClassId_Object=MibTableColumn
rbnQosHierarchicalPClassId=_RbnQosHierarchicalPClassId_Object((1,3,6,1,4,1,2352,2,22,1,7,1,1),_RbnQosHierarchicalPClassId_Type())
rbnQosHierarchicalPClassId.setMaxAccess(_E)
if mibBuilder.loadTexts:rbnQosHierarchicalPClassId.setStatus(_A)
class _RbnQosHierarchicalPClassName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,39))
_RbnQosHierarchicalPClassName_Type.__name__=_D
_RbnQosHierarchicalPClassName_Object=MibTableColumn
rbnQosHierarchicalPClassName=_RbnQosHierarchicalPClassName_Object((1,3,6,1,4,1,2352,2,22,1,7,1,2),_RbnQosHierarchicalPClassName_Type())
rbnQosHierarchicalPClassName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosHierarchicalPClassName.setStatus(_A)
_RbnQosHierarchicalPClassDroppedOctets_Type=Counter64
_RbnQosHierarchicalPClassDroppedOctets_Object=MibTableColumn
rbnQosHierarchicalPClassDroppedOctets=_RbnQosHierarchicalPClassDroppedOctets_Object((1,3,6,1,4,1,2352,2,22,1,7,1,3),_RbnQosHierarchicalPClassDroppedOctets_Type())
rbnQosHierarchicalPClassDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosHierarchicalPClassDroppedOctets.setStatus(_A)
_RbnQosHierarchicalPClassDroppedPkts_Type=Counter64
_RbnQosHierarchicalPClassDroppedPkts_Object=MibTableColumn
rbnQosHierarchicalPClassDroppedPkts=_RbnQosHierarchicalPClassDroppedPkts_Object((1,3,6,1,4,1,2352,2,22,1,7,1,4),_RbnQosHierarchicalPClassDroppedPkts_Type())
rbnQosHierarchicalPClassDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnQosHierarchicalPClassDroppedPkts.setStatus(_A)
_RbnQosMibConformance_ObjectIdentity=ObjectIdentity
rbnQosMibConformance=_RbnQosMibConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,22,2))
_RbnQosCompliances_ObjectIdentity=ObjectIdentity
rbnQosCompliances=_RbnQosCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,22,2,1))
_RbnQosGroups_ObjectIdentity=ObjectIdentity
rbnQosGroups=_RbnQosGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,22,2,2))
rbnQosIfGroup=ObjectGroup((1,3,6,1,4,1,2352,2,22,2,2,1))
rbnQosIfGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:rbnQosIfGroup.setStatus(_A)
rbnQosIfQueueGroup=ObjectGroup((1,3,6,1,4,1,2352,2,22,2,2,2))
rbnQosIfQueueGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:rbnQosIfQueueGroup.setStatus(_A)
rbnQosSubscriberQueueGroup=ObjectGroup((1,3,6,1,4,1,2352,2,22,2,2,3))
rbnQosSubscriberQueueGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:rbnQosSubscriberQueueGroup.setStatus(_A)
rbnQosIfRLClassStatsGroup=ObjectGroup((1,3,6,1,4,1,2352,2,22,2,2,4))
rbnQosIfRLClassStatsGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:rbnQosIfRLClassStatsGroup.setStatus(_A)
rbnQosSubscriberRLClassStatsGroup=ObjectGroup((1,3,6,1,4,1,2352,2,22,2,2,5))
rbnQosSubscriberRLClassStatsGroup.setObjects(*((_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:rbnQosSubscriberRLClassStatsGroup.setStatus(_A)
rbnQosHierarchicalPolicyStatsGroup=ObjectGroup((1,3,6,1,4,1,2352,2,22,2,2,6))
rbnQosHierarchicalPolicyStatsGroup.setObjects(*((_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac)))
if mibBuilder.loadTexts:rbnQosHierarchicalPolicyStatsGroup.setStatus(_A)
rbnQosCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,22,2,1,1))
rbnQosCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:rbnQosCompliance.setStatus('deprecated')
rbnQosCompliance2=ModuleCompliance((1,3,6,1,4,1,2352,2,22,2,1,2))
rbnQosCompliance2.setObjects(*((_B,_H),(_B,_J)))
if mibBuilder.loadTexts:rbnQosCompliance2.setStatus(_A)
rbnQosCompliance3=ModuleCompliance((1,3,6,1,4,1,2352,2,22,2,1,3))
rbnQosCompliance3.setObjects(*((_B,_H),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:rbnQosCompliance3.setStatus(_A)
rbnQosCompliance4=ModuleCompliance((1,3,6,1,4,1,2352,2,22,2,1,4))
rbnQosCompliance4.setObjects(*((_B,_H),(_B,_J),(_B,_K),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:rbnQosCompliance4.setStatus(_A)
rbnQosCompliance5=ModuleCompliance((1,3,6,1,4,1,2352,2,22,2,1,5))
rbnQosCompliance5.setObjects(*((_B,_H),(_B,_J),(_B,_K),(_B,_P),(_B,_Q),(_B,_Ad)))
if mibBuilder.loadTexts:rbnQosCompliance5.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RbnQosPolicyType':RbnQosPolicyType,'RbnQosClassId':RbnQosClassId,'rbnQosMib':rbnQosMib,'rbnQosMibObjects':rbnQosMibObjects,'rbnQosInterfaceTable':rbnQosInterfaceTable,'rbnQosInterfaceEntry':rbnQosInterfaceEntry,_Y:rbnQosIfInOctets,_Z:rbnQosIfHCInOctets,_a:rbnQosIfOutOctets,_b:rbnQosIfHCOutOctets,_c:rbnQosIfInDroppedOctets,_d:rbnQosIfHCInDroppedOctets,_e:rbnQosIfOutDroppedOctets,_f:rbnQosIfHCOutDroppedOctets,'rbnQosInterfaceQueueStatsTable':rbnQosInterfaceQueueStatsTable,'rbnQosInterfaceQueueStatsEntry':rbnQosInterfaceQueueStatsEntry,_R:rbnQosIfQueueId,_g:rbnQosIfQueueOutOctets,_i:rbnQosIfQueueOutPkts,_k:rbnQosIfQueueWredDroppedOctets,_m:rbnQosIfQueueWredDroppedPkts,_o:rbnQosIfQueueTailDroppedOctets,_q:rbnQosIfQueueTailDroppedPkts,_h:rbnQosIfQueueHCOutOctets,_j:rbnQosIfQueueHCOutPkts,_l:rbnQosIfQueueHCWredDroppedOctets,_n:rbnQosIfQueueHCWredDroppedPkts,_p:rbnQosIfQueueHCTailDroppedOctets,_r:rbnQosIfQueueHCTailDroppedPkts,'rbnQosSubscriberQueueStatsTable':rbnQosSubscriberQueueStatsTable,'rbnQosSubscriberQueueStatsEntry':rbnQosSubscriberQueueStatsEntry,_S:rbnQosSubsQueueId,_s:rbnQosSubsQueuePolicyName,_t:rbnQosSubsQueueOutOctets,_u:rbnQosSubsQueueOutPkts,_v:rbnQosSubsQueueWredDroppedOctets,_w:rbnQosSubsQueueWredDroppedPkts,_x:rbnQosSubsQueueTailDroppedOctets,_y:rbnQosSubsQueueTailDroppedPkts,_z:rbnQosSubsQueueHCOutOctets,_A0:rbnQosSubsQueueHCOutPkts,_A1:rbnQosSubsQueueHCWredDroppedOctets,_A2:rbnQosSubsQueueHCWredDroppedPkts,_A3:rbnQosSubsQueueHCTailDroppedOctets,_A4:rbnQosSubsQueueHCTailDroppedPkts,'rbnQosIntfRLClassStatsTable':rbnQosIntfRLClassStatsTable,'rbnQosIntfRLClassStatsEntry':rbnQosIntfRLClassStatsEntry,_T:rbnQosIfRLPolicyType,_U:rbnQosIfRLClassId,_A5:rbnQosIfRLPolicyName,_A6:rbnQosIfRLClassName,_A7:rbnQosIfRLClassConformOctets,_A8:rbnQosIfRLClassConformPkts,_A9:rbnQosIfRLClassConformDroppedOctets,_AA:rbnQosIfRLClassConformDroppedPkts,_AB:rbnQosIfRLClassExceedOctets,_AC:rbnQosIfRLClassExceedPkts,_AD:rbnQosIfRLClassExceedDroppedOctets,_AE:rbnQosIfRLClassExceedDroppedPkts,_AF:rbnQosIfRLClassViolateOctets,_AG:rbnQosIfRLClassViolatePkts,_AH:rbnQosIfRLClassViolateDroppedOctets,_AI:rbnQosIfRLClassViolateDroppedPkts,'rbnQosSubscriberRLClassStatsTable':rbnQosSubscriberRLClassStatsTable,'rbnQosSubscriberRLClassStatsEntry':rbnQosSubscriberRLClassStatsEntry,_V:rbnQosSubsRLPolicyType,_W:rbnQosSubsRLClassId,_AJ:rbnQosSubsRLPolicyName,_AK:rbnQosSubsRLClassName,_AL:rbnQosSubsRLClassConformOctets,_AM:rbnQosSubsRLClassConformPkts,_AN:rbnQosSubsRLClassConformDroppedOctets,_AO:rbnQosSubsRLClassConformDroppedPkts,_AP:rbnQosSubsRLClassExceedOctets,_AQ:rbnQosSubsRLClassExceedPkts,_AR:rbnQosSubsRLClassExceedDroppedOctets,_AS:rbnQosSubsRLClassExceedDroppedPkts,_AT:rbnQosSubsRLClassViolateOctets,_AU:rbnQosSubsRLClassViolatePkts,_AV:rbnQosSubsRLClassViolateDroppedOctets,_AW:rbnQosSubsRLClassViolateDroppedPkts,'rbnQosHierarchicalPolicyStatsTable':rbnQosHierarchicalPolicyStatsTable,'rbnQosHierarchicalPolicyStatsEntry':rbnQosHierarchicalPolicyStatsEntry,_O:rbnQosHierarchicalPolicyType,_AX:rbnQosHierarchicalPolicyName,_AY:rbnQosHierarchicalPolicyDroppedOctets,_AZ:rbnQosHierarchicalPolicyDroppedPkts,'rbnQosHierarchicalPClassStatsTable':rbnQosHierarchicalPClassStatsTable,'rbnQosHierarchicalPClassStatsEntry':rbnQosHierarchicalPClassStatsEntry,_X:rbnQosHierarchicalPClassId,_Aa:rbnQosHierarchicalPClassName,_Ab:rbnQosHierarchicalPClassDroppedOctets,_Ac:rbnQosHierarchicalPClassDroppedPkts,'rbnQosMibConformance':rbnQosMibConformance,'rbnQosCompliances':rbnQosCompliances,'rbnQosCompliance':rbnQosCompliance,'rbnQosCompliance2':rbnQosCompliance2,'rbnQosCompliance3':rbnQosCompliance3,'rbnQosCompliance4':rbnQosCompliance4,'rbnQosCompliance5':rbnQosCompliance5,'rbnQosGroups':rbnQosGroups,_H:rbnQosIfGroup,_J:rbnQosIfQueueGroup,_K:rbnQosSubscriberQueueGroup,_P:rbnQosIfRLClassStatsGroup,_Q:rbnQosSubscriberRLClassStatsGroup,_Ad:rbnQosHierarchicalPolicyStatsGroup})