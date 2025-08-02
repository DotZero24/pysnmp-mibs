_A6='rbnCctGrpPolicyStatsGroup'
_A5='rbnCctGrpQStatsGroup'
_A4='rbnCctGrpStatsGroup'
_A3='rbnCctGrpRLClassViolateDroppedPkts'
_A2='rbnCctGrpRLClassViolateDroppedOctets'
_A1='rbnCctGrpRLClassViolatePkts'
_A0='rbnCctGrpRLClassViolateOctets'
_z='rbnCctGrpRLClassExceedDroppedPkts'
_y='rbnCctGrpRLClassExceedDroppedOctets'
_x='rbnCctGrpRLClassExceedPkts'
_w='rbnCctGrpRLClassExceedOctets'
_v='rbnCctGrpRLClassConformDroppedPkts'
_u='rbnCctGrpRLClassConformDroppedOctets'
_t='rbnCctGrpRLClassConformPkts'
_s='rbnCctGrpRLClassConformOctets'
_r='rbnCctGrpRLClassName'
_q='rbnCctGrpRLPolicyViolateDroppedPkts'
_p='rbnCctGrpRLPolicyViolateDroppedOctets'
_o='rbnCctGrpRLPolicyViolatePkts'
_n='rbnCctGrpRLPolicyViolateOctets'
_m='rbnCctGrpRLPolicyExceedDroppedPkts'
_l='rbnCctGrpRLPolicyExceedDroppedOctets'
_k='rbnCctGrpRLPolicyExceedPkts'
_j='rbnCctGrpRLPolicyExceedOctets'
_i='rbnCctGrpRLPolicyConformPkts'
_h='rbnCctGrpRLPolicyConformOctets'
_g='rbnCctGrpRLPolicyName'
_f='rbnCctGrpQTailDroppedPkts'
_e='rbnCctGrpQTailDroppedOctets'
_d='rbnCctGrpQWredDroppedPkts'
_c='rbnCctGrpQWredDroppedOctets'
_b='rbnCctGrpQTxPackets'
_a='rbnCctGrpQTxOctets'
_Z='rbnCctGrpUnknownEncapsPackets'
_Y='rbnCctGrpUnknownEncapsOctets'
_X='rbnCctGrpUnreachDroppedPackets'
_W='rbnCctGrpUnreachDroppedOctets'
_V='rbnCctGrpDownDroppedPackets'
_U='rbnCctGrpDownDroppedOctets'
_T='rbnCctGrpAdjDroppedPackets'
_S='rbnCctGrpAdjDroppedOctets'
_R='rbnCctGrpRxMulticastPackets'
_Q='rbnCctGrpRxMulticastOctets'
_P='rbnCctGrpRxPackets'
_O='rbnCctGrpRxOctets'
_N='rbnCctGrpTxMulticastPackets'
_M='rbnCctGrpTxMulticastOctets'
_L='rbnCctGrpTxPackets'
_K='rbnCctGrpTxOctets'
_J='rbnCctGrpRLClassId'
_I='rbnCctGrpQueueId'
_H='Unsigned32'
_G='rbnCctGrpRLPolicyType'
_F='not-accessible'
_E='SnmpAdminString'
_D='rbnCctGrpName'
_C='read-only'
_B='RBN-CIRCUIT-GROUP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
RbnQosClassId,RbnQosPolicyType=mibBuilder.importSymbols('RBN-QOS-MIB','RbnQosClassId','RbnQosPolicyType')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnCircuitGroupMib=ModuleIdentity((1,3,6,1,4,1,2352,2,43))
if mibBuilder.loadTexts:rbnCircuitGroupMib.setRevisions(('2008-07-30 00:00','2007-07-25 00:00'))
_RbnCircuitGroupObjects_ObjectIdentity=ObjectIdentity
rbnCircuitGroupObjects=_RbnCircuitGroupObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,43,1))
_RbnCircuitGroupStatsTable_Object=MibTable
rbnCircuitGroupStatsTable=_RbnCircuitGroupStatsTable_Object((1,3,6,1,4,1,2352,2,43,1,1))
if mibBuilder.loadTexts:rbnCircuitGroupStatsTable.setStatus(_A)
_RbnCircuitGroupStatsEntry_Object=MibTableRow
rbnCircuitGroupStatsEntry=_RbnCircuitGroupStatsEntry_Object((1,3,6,1,4,1,2352,2,43,1,1,1))
rbnCircuitGroupStatsEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:rbnCircuitGroupStatsEntry.setStatus(_A)
class _RbnCctGrpName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,113))
_RbnCctGrpName_Type.__name__=_E
_RbnCctGrpName_Object=MibTableColumn
rbnCctGrpName=_RbnCctGrpName_Object((1,3,6,1,4,1,2352,2,43,1,1,1,1),_RbnCctGrpName_Type())
rbnCctGrpName.setMaxAccess(_F)
if mibBuilder.loadTexts:rbnCctGrpName.setStatus(_A)
_RbnCctGrpTxOctets_Type=Counter64
_RbnCctGrpTxOctets_Object=MibTableColumn
rbnCctGrpTxOctets=_RbnCctGrpTxOctets_Object((1,3,6,1,4,1,2352,2,43,1,1,1,2),_RbnCctGrpTxOctets_Type())
rbnCctGrpTxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpTxOctets.setStatus(_A)
_RbnCctGrpTxPackets_Type=Counter64
_RbnCctGrpTxPackets_Object=MibTableColumn
rbnCctGrpTxPackets=_RbnCctGrpTxPackets_Object((1,3,6,1,4,1,2352,2,43,1,1,1,3),_RbnCctGrpTxPackets_Type())
rbnCctGrpTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpTxPackets.setStatus(_A)
_RbnCctGrpTxMulticastOctets_Type=Counter64
_RbnCctGrpTxMulticastOctets_Object=MibTableColumn
rbnCctGrpTxMulticastOctets=_RbnCctGrpTxMulticastOctets_Object((1,3,6,1,4,1,2352,2,43,1,1,1,4),_RbnCctGrpTxMulticastOctets_Type())
rbnCctGrpTxMulticastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpTxMulticastOctets.setStatus(_A)
_RbnCctGrpTxMulticastPackets_Type=Counter64
_RbnCctGrpTxMulticastPackets_Object=MibTableColumn
rbnCctGrpTxMulticastPackets=_RbnCctGrpTxMulticastPackets_Object((1,3,6,1,4,1,2352,2,43,1,1,1,5),_RbnCctGrpTxMulticastPackets_Type())
rbnCctGrpTxMulticastPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpTxMulticastPackets.setStatus(_A)
_RbnCctGrpRxOctets_Type=Counter64
_RbnCctGrpRxOctets_Object=MibTableColumn
rbnCctGrpRxOctets=_RbnCctGrpRxOctets_Object((1,3,6,1,4,1,2352,2,43,1,1,1,6),_RbnCctGrpRxOctets_Type())
rbnCctGrpRxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRxOctets.setStatus(_A)
_RbnCctGrpRxPackets_Type=Counter64
_RbnCctGrpRxPackets_Object=MibTableColumn
rbnCctGrpRxPackets=_RbnCctGrpRxPackets_Object((1,3,6,1,4,1,2352,2,43,1,1,1,7),_RbnCctGrpRxPackets_Type())
rbnCctGrpRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRxPackets.setStatus(_A)
_RbnCctGrpRxMulticastOctets_Type=Counter64
_RbnCctGrpRxMulticastOctets_Object=MibTableColumn
rbnCctGrpRxMulticastOctets=_RbnCctGrpRxMulticastOctets_Object((1,3,6,1,4,1,2352,2,43,1,1,1,8),_RbnCctGrpRxMulticastOctets_Type())
rbnCctGrpRxMulticastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRxMulticastOctets.setStatus(_A)
_RbnCctGrpRxMulticastPackets_Type=Counter64
_RbnCctGrpRxMulticastPackets_Object=MibTableColumn
rbnCctGrpRxMulticastPackets=_RbnCctGrpRxMulticastPackets_Object((1,3,6,1,4,1,2352,2,43,1,1,1,9),_RbnCctGrpRxMulticastPackets_Type())
rbnCctGrpRxMulticastPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRxMulticastPackets.setStatus(_A)
_RbnCctGrpAdjDroppedOctets_Type=Counter64
_RbnCctGrpAdjDroppedOctets_Object=MibTableColumn
rbnCctGrpAdjDroppedOctets=_RbnCctGrpAdjDroppedOctets_Object((1,3,6,1,4,1,2352,2,43,1,1,1,10),_RbnCctGrpAdjDroppedOctets_Type())
rbnCctGrpAdjDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpAdjDroppedOctets.setStatus(_A)
_RbnCctGrpAdjDroppedPackets_Type=Counter64
_RbnCctGrpAdjDroppedPackets_Object=MibTableColumn
rbnCctGrpAdjDroppedPackets=_RbnCctGrpAdjDroppedPackets_Object((1,3,6,1,4,1,2352,2,43,1,1,1,11),_RbnCctGrpAdjDroppedPackets_Type())
rbnCctGrpAdjDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpAdjDroppedPackets.setStatus(_A)
_RbnCctGrpDownDroppedOctets_Type=Counter64
_RbnCctGrpDownDroppedOctets_Object=MibTableColumn
rbnCctGrpDownDroppedOctets=_RbnCctGrpDownDroppedOctets_Object((1,3,6,1,4,1,2352,2,43,1,1,1,12),_RbnCctGrpDownDroppedOctets_Type())
rbnCctGrpDownDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpDownDroppedOctets.setStatus(_A)
_RbnCctGrpDownDroppedPackets_Type=Counter64
_RbnCctGrpDownDroppedPackets_Object=MibTableColumn
rbnCctGrpDownDroppedPackets=_RbnCctGrpDownDroppedPackets_Object((1,3,6,1,4,1,2352,2,43,1,1,1,13),_RbnCctGrpDownDroppedPackets_Type())
rbnCctGrpDownDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpDownDroppedPackets.setStatus(_A)
_RbnCctGrpUnreachDroppedOctets_Type=Counter64
_RbnCctGrpUnreachDroppedOctets_Object=MibTableColumn
rbnCctGrpUnreachDroppedOctets=_RbnCctGrpUnreachDroppedOctets_Object((1,3,6,1,4,1,2352,2,43,1,1,1,14),_RbnCctGrpUnreachDroppedOctets_Type())
rbnCctGrpUnreachDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpUnreachDroppedOctets.setStatus(_A)
_RbnCctGrpUnreachDroppedPackets_Type=Counter64
_RbnCctGrpUnreachDroppedPackets_Object=MibTableColumn
rbnCctGrpUnreachDroppedPackets=_RbnCctGrpUnreachDroppedPackets_Object((1,3,6,1,4,1,2352,2,43,1,1,1,15),_RbnCctGrpUnreachDroppedPackets_Type())
rbnCctGrpUnreachDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpUnreachDroppedPackets.setStatus(_A)
_RbnCctGrpUnknownEncapsOctets_Type=Counter64
_RbnCctGrpUnknownEncapsOctets_Object=MibTableColumn
rbnCctGrpUnknownEncapsOctets=_RbnCctGrpUnknownEncapsOctets_Object((1,3,6,1,4,1,2352,2,43,1,1,1,16),_RbnCctGrpUnknownEncapsOctets_Type())
rbnCctGrpUnknownEncapsOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpUnknownEncapsOctets.setStatus(_A)
_RbnCctGrpUnknownEncapsPackets_Type=Counter64
_RbnCctGrpUnknownEncapsPackets_Object=MibTableColumn
rbnCctGrpUnknownEncapsPackets=_RbnCctGrpUnknownEncapsPackets_Object((1,3,6,1,4,1,2352,2,43,1,1,1,17),_RbnCctGrpUnknownEncapsPackets_Type())
rbnCctGrpUnknownEncapsPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpUnknownEncapsPackets.setStatus(_A)
_RbnCircuitGroupQTable_Object=MibTable
rbnCircuitGroupQTable=_RbnCircuitGroupQTable_Object((1,3,6,1,4,1,2352,2,43,1,2))
if mibBuilder.loadTexts:rbnCircuitGroupQTable.setStatus(_A)
_RbnCircuitGroupQEntry_Object=MibTableRow
rbnCircuitGroupQEntry=_RbnCircuitGroupQEntry_Object((1,3,6,1,4,1,2352,2,43,1,2,1))
rbnCircuitGroupQEntry.setIndexNames((0,_B,_D),(0,_B,_I))
if mibBuilder.loadTexts:rbnCircuitGroupQEntry.setStatus(_A)
class _RbnCctGrpQueueId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RbnCctGrpQueueId_Type.__name__=_H
_RbnCctGrpQueueId_Object=MibTableColumn
rbnCctGrpQueueId=_RbnCctGrpQueueId_Object((1,3,6,1,4,1,2352,2,43,1,2,1,1),_RbnCctGrpQueueId_Type())
rbnCctGrpQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:rbnCctGrpQueueId.setStatus(_A)
_RbnCctGrpQTxOctets_Type=Counter64
_RbnCctGrpQTxOctets_Object=MibTableColumn
rbnCctGrpQTxOctets=_RbnCctGrpQTxOctets_Object((1,3,6,1,4,1,2352,2,43,1,2,1,2),_RbnCctGrpQTxOctets_Type())
rbnCctGrpQTxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpQTxOctets.setStatus(_A)
_RbnCctGrpQTxPackets_Type=Counter64
_RbnCctGrpQTxPackets_Object=MibTableColumn
rbnCctGrpQTxPackets=_RbnCctGrpQTxPackets_Object((1,3,6,1,4,1,2352,2,43,1,2,1,3),_RbnCctGrpQTxPackets_Type())
rbnCctGrpQTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpQTxPackets.setStatus(_A)
_RbnCctGrpQWredDroppedOctets_Type=Counter64
_RbnCctGrpQWredDroppedOctets_Object=MibTableColumn
rbnCctGrpQWredDroppedOctets=_RbnCctGrpQWredDroppedOctets_Object((1,3,6,1,4,1,2352,2,43,1,2,1,4),_RbnCctGrpQWredDroppedOctets_Type())
rbnCctGrpQWredDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpQWredDroppedOctets.setStatus(_A)
_RbnCctGrpQWredDroppedPkts_Type=Counter64
_RbnCctGrpQWredDroppedPkts_Object=MibTableColumn
rbnCctGrpQWredDroppedPkts=_RbnCctGrpQWredDroppedPkts_Object((1,3,6,1,4,1,2352,2,43,1,2,1,5),_RbnCctGrpQWredDroppedPkts_Type())
rbnCctGrpQWredDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpQWredDroppedPkts.setStatus(_A)
_RbnCctGrpQTailDroppedOctets_Type=Counter64
_RbnCctGrpQTailDroppedOctets_Object=MibTableColumn
rbnCctGrpQTailDroppedOctets=_RbnCctGrpQTailDroppedOctets_Object((1,3,6,1,4,1,2352,2,43,1,2,1,6),_RbnCctGrpQTailDroppedOctets_Type())
rbnCctGrpQTailDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpQTailDroppedOctets.setStatus(_A)
_RbnCctGrpQTailDroppedPkts_Type=Counter64
_RbnCctGrpQTailDroppedPkts_Object=MibTableColumn
rbnCctGrpQTailDroppedPkts=_RbnCctGrpQTailDroppedPkts_Object((1,3,6,1,4,1,2352,2,43,1,2,1,7),_RbnCctGrpQTailDroppedPkts_Type())
rbnCctGrpQTailDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpQTailDroppedPkts.setStatus(_A)
_RbnCctGrpRLPolicyStatsTable_Object=MibTable
rbnCctGrpRLPolicyStatsTable=_RbnCctGrpRLPolicyStatsTable_Object((1,3,6,1,4,1,2352,2,43,1,3))
if mibBuilder.loadTexts:rbnCctGrpRLPolicyStatsTable.setStatus(_A)
_RbnCctGrpRLPolicyStatsEntry_Object=MibTableRow
rbnCctGrpRLPolicyStatsEntry=_RbnCctGrpRLPolicyStatsEntry_Object((1,3,6,1,4,1,2352,2,43,1,3,1))
rbnCctGrpRLPolicyStatsEntry.setIndexNames((0,_B,_D),(0,_B,_G))
if mibBuilder.loadTexts:rbnCctGrpRLPolicyStatsEntry.setStatus(_A)
_RbnCctGrpRLPolicyType_Type=RbnQosPolicyType
_RbnCctGrpRLPolicyType_Object=MibTableColumn
rbnCctGrpRLPolicyType=_RbnCctGrpRLPolicyType_Object((1,3,6,1,4,1,2352,2,43,1,3,1,1),_RbnCctGrpRLPolicyType_Type())
rbnCctGrpRLPolicyType.setMaxAccess(_F)
if mibBuilder.loadTexts:rbnCctGrpRLPolicyType.setStatus(_A)
class _RbnCctGrpRLPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,39))
_RbnCctGrpRLPolicyName_Type.__name__=_E
_RbnCctGrpRLPolicyName_Object=MibTableColumn
rbnCctGrpRLPolicyName=_RbnCctGrpRLPolicyName_Object((1,3,6,1,4,1,2352,2,43,1,3,1,2),_RbnCctGrpRLPolicyName_Type())
rbnCctGrpRLPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLPolicyName.setStatus(_A)
_RbnCctGrpRLPolicyConformOctets_Type=Counter64
_RbnCctGrpRLPolicyConformOctets_Object=MibTableColumn
rbnCctGrpRLPolicyConformOctets=_RbnCctGrpRLPolicyConformOctets_Object((1,3,6,1,4,1,2352,2,43,1,3,1,3),_RbnCctGrpRLPolicyConformOctets_Type())
rbnCctGrpRLPolicyConformOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLPolicyConformOctets.setStatus(_A)
_RbnCctGrpRLPolicyConformPkts_Type=Counter64
_RbnCctGrpRLPolicyConformPkts_Object=MibTableColumn
rbnCctGrpRLPolicyConformPkts=_RbnCctGrpRLPolicyConformPkts_Object((1,3,6,1,4,1,2352,2,43,1,3,1,4),_RbnCctGrpRLPolicyConformPkts_Type())
rbnCctGrpRLPolicyConformPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLPolicyConformPkts.setStatus(_A)
_RbnCctGrpRLPolicyExceedOctets_Type=Counter64
_RbnCctGrpRLPolicyExceedOctets_Object=MibTableColumn
rbnCctGrpRLPolicyExceedOctets=_RbnCctGrpRLPolicyExceedOctets_Object((1,3,6,1,4,1,2352,2,43,1,3,1,5),_RbnCctGrpRLPolicyExceedOctets_Type())
rbnCctGrpRLPolicyExceedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLPolicyExceedOctets.setStatus(_A)
_RbnCctGrpRLPolicyExceedPkts_Type=Counter64
_RbnCctGrpRLPolicyExceedPkts_Object=MibTableColumn
rbnCctGrpRLPolicyExceedPkts=_RbnCctGrpRLPolicyExceedPkts_Object((1,3,6,1,4,1,2352,2,43,1,3,1,6),_RbnCctGrpRLPolicyExceedPkts_Type())
rbnCctGrpRLPolicyExceedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLPolicyExceedPkts.setStatus(_A)
_RbnCctGrpRLPolicyExceedDroppedOctets_Type=Counter64
_RbnCctGrpRLPolicyExceedDroppedOctets_Object=MibTableColumn
rbnCctGrpRLPolicyExceedDroppedOctets=_RbnCctGrpRLPolicyExceedDroppedOctets_Object((1,3,6,1,4,1,2352,2,43,1,3,1,7),_RbnCctGrpRLPolicyExceedDroppedOctets_Type())
rbnCctGrpRLPolicyExceedDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLPolicyExceedDroppedOctets.setStatus(_A)
_RbnCctGrpRLPolicyExceedDroppedPkts_Type=Counter64
_RbnCctGrpRLPolicyExceedDroppedPkts_Object=MibTableColumn
rbnCctGrpRLPolicyExceedDroppedPkts=_RbnCctGrpRLPolicyExceedDroppedPkts_Object((1,3,6,1,4,1,2352,2,43,1,3,1,8),_RbnCctGrpRLPolicyExceedDroppedPkts_Type())
rbnCctGrpRLPolicyExceedDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLPolicyExceedDroppedPkts.setStatus(_A)
_RbnCctGrpRLPolicyViolateOctets_Type=Counter64
_RbnCctGrpRLPolicyViolateOctets_Object=MibTableColumn
rbnCctGrpRLPolicyViolateOctets=_RbnCctGrpRLPolicyViolateOctets_Object((1,3,6,1,4,1,2352,2,43,1,3,1,9),_RbnCctGrpRLPolicyViolateOctets_Type())
rbnCctGrpRLPolicyViolateOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLPolicyViolateOctets.setStatus(_A)
_RbnCctGrpRLPolicyViolatePkts_Type=Counter64
_RbnCctGrpRLPolicyViolatePkts_Object=MibTableColumn
rbnCctGrpRLPolicyViolatePkts=_RbnCctGrpRLPolicyViolatePkts_Object((1,3,6,1,4,1,2352,2,43,1,3,1,10),_RbnCctGrpRLPolicyViolatePkts_Type())
rbnCctGrpRLPolicyViolatePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLPolicyViolatePkts.setStatus(_A)
_RbnCctGrpRLPolicyViolateDroppedOctets_Type=Counter64
_RbnCctGrpRLPolicyViolateDroppedOctets_Object=MibTableColumn
rbnCctGrpRLPolicyViolateDroppedOctets=_RbnCctGrpRLPolicyViolateDroppedOctets_Object((1,3,6,1,4,1,2352,2,43,1,3,1,11),_RbnCctGrpRLPolicyViolateDroppedOctets_Type())
rbnCctGrpRLPolicyViolateDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLPolicyViolateDroppedOctets.setStatus(_A)
_RbnCctGrpRLPolicyViolateDroppedPkts_Type=Counter64
_RbnCctGrpRLPolicyViolateDroppedPkts_Object=MibTableColumn
rbnCctGrpRLPolicyViolateDroppedPkts=_RbnCctGrpRLPolicyViolateDroppedPkts_Object((1,3,6,1,4,1,2352,2,43,1,3,1,12),_RbnCctGrpRLPolicyViolateDroppedPkts_Type())
rbnCctGrpRLPolicyViolateDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLPolicyViolateDroppedPkts.setStatus(_A)
_RbnCctGrpRLClassStatsTable_Object=MibTable
rbnCctGrpRLClassStatsTable=_RbnCctGrpRLClassStatsTable_Object((1,3,6,1,4,1,2352,2,43,1,4))
if mibBuilder.loadTexts:rbnCctGrpRLClassStatsTable.setStatus(_A)
_RbnCctGrpRLClassStatsEntry_Object=MibTableRow
rbnCctGrpRLClassStatsEntry=_RbnCctGrpRLClassStatsEntry_Object((1,3,6,1,4,1,2352,2,43,1,4,1))
rbnCctGrpRLClassStatsEntry.setIndexNames((0,_B,_D),(0,_B,_G),(0,_B,_J))
if mibBuilder.loadTexts:rbnCctGrpRLClassStatsEntry.setStatus(_A)
_RbnCctGrpRLClassId_Type=RbnQosClassId
_RbnCctGrpRLClassId_Object=MibTableColumn
rbnCctGrpRLClassId=_RbnCctGrpRLClassId_Object((1,3,6,1,4,1,2352,2,43,1,4,1,1),_RbnCctGrpRLClassId_Type())
rbnCctGrpRLClassId.setMaxAccess(_F)
if mibBuilder.loadTexts:rbnCctGrpRLClassId.setStatus(_A)
class _RbnCctGrpRLClassName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,39))
_RbnCctGrpRLClassName_Type.__name__=_E
_RbnCctGrpRLClassName_Object=MibTableColumn
rbnCctGrpRLClassName=_RbnCctGrpRLClassName_Object((1,3,6,1,4,1,2352,2,43,1,4,1,2),_RbnCctGrpRLClassName_Type())
rbnCctGrpRLClassName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLClassName.setStatus(_A)
_RbnCctGrpRLClassConformOctets_Type=Counter64
_RbnCctGrpRLClassConformOctets_Object=MibTableColumn
rbnCctGrpRLClassConformOctets=_RbnCctGrpRLClassConformOctets_Object((1,3,6,1,4,1,2352,2,43,1,4,1,3),_RbnCctGrpRLClassConformOctets_Type())
rbnCctGrpRLClassConformOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLClassConformOctets.setStatus(_A)
_RbnCctGrpRLClassConformPkts_Type=Counter64
_RbnCctGrpRLClassConformPkts_Object=MibTableColumn
rbnCctGrpRLClassConformPkts=_RbnCctGrpRLClassConformPkts_Object((1,3,6,1,4,1,2352,2,43,1,4,1,4),_RbnCctGrpRLClassConformPkts_Type())
rbnCctGrpRLClassConformPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLClassConformPkts.setStatus(_A)
_RbnCctGrpRLClassConformDroppedOctets_Type=Counter64
_RbnCctGrpRLClassConformDroppedOctets_Object=MibTableColumn
rbnCctGrpRLClassConformDroppedOctets=_RbnCctGrpRLClassConformDroppedOctets_Object((1,3,6,1,4,1,2352,2,43,1,4,1,5),_RbnCctGrpRLClassConformDroppedOctets_Type())
rbnCctGrpRLClassConformDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLClassConformDroppedOctets.setStatus(_A)
_RbnCctGrpRLClassConformDroppedPkts_Type=Counter64
_RbnCctGrpRLClassConformDroppedPkts_Object=MibTableColumn
rbnCctGrpRLClassConformDroppedPkts=_RbnCctGrpRLClassConformDroppedPkts_Object((1,3,6,1,4,1,2352,2,43,1,4,1,6),_RbnCctGrpRLClassConformDroppedPkts_Type())
rbnCctGrpRLClassConformDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLClassConformDroppedPkts.setStatus(_A)
_RbnCctGrpRLClassExceedOctets_Type=Counter64
_RbnCctGrpRLClassExceedOctets_Object=MibTableColumn
rbnCctGrpRLClassExceedOctets=_RbnCctGrpRLClassExceedOctets_Object((1,3,6,1,4,1,2352,2,43,1,4,1,7),_RbnCctGrpRLClassExceedOctets_Type())
rbnCctGrpRLClassExceedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLClassExceedOctets.setStatus(_A)
_RbnCctGrpRLClassExceedPkts_Type=Counter64
_RbnCctGrpRLClassExceedPkts_Object=MibTableColumn
rbnCctGrpRLClassExceedPkts=_RbnCctGrpRLClassExceedPkts_Object((1,3,6,1,4,1,2352,2,43,1,4,1,8),_RbnCctGrpRLClassExceedPkts_Type())
rbnCctGrpRLClassExceedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLClassExceedPkts.setStatus(_A)
_RbnCctGrpRLClassExceedDroppedOctets_Type=Counter64
_RbnCctGrpRLClassExceedDroppedOctets_Object=MibTableColumn
rbnCctGrpRLClassExceedDroppedOctets=_RbnCctGrpRLClassExceedDroppedOctets_Object((1,3,6,1,4,1,2352,2,43,1,4,1,9),_RbnCctGrpRLClassExceedDroppedOctets_Type())
rbnCctGrpRLClassExceedDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLClassExceedDroppedOctets.setStatus(_A)
_RbnCctGrpRLClassExceedDroppedPkts_Type=Counter64
_RbnCctGrpRLClassExceedDroppedPkts_Object=MibTableColumn
rbnCctGrpRLClassExceedDroppedPkts=_RbnCctGrpRLClassExceedDroppedPkts_Object((1,3,6,1,4,1,2352,2,43,1,4,1,10),_RbnCctGrpRLClassExceedDroppedPkts_Type())
rbnCctGrpRLClassExceedDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLClassExceedDroppedPkts.setStatus(_A)
_RbnCctGrpRLClassViolateOctets_Type=Counter64
_RbnCctGrpRLClassViolateOctets_Object=MibTableColumn
rbnCctGrpRLClassViolateOctets=_RbnCctGrpRLClassViolateOctets_Object((1,3,6,1,4,1,2352,2,43,1,4,1,11),_RbnCctGrpRLClassViolateOctets_Type())
rbnCctGrpRLClassViolateOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLClassViolateOctets.setStatus(_A)
_RbnCctGrpRLClassViolatePkts_Type=Counter64
_RbnCctGrpRLClassViolatePkts_Object=MibTableColumn
rbnCctGrpRLClassViolatePkts=_RbnCctGrpRLClassViolatePkts_Object((1,3,6,1,4,1,2352,2,43,1,4,1,12),_RbnCctGrpRLClassViolatePkts_Type())
rbnCctGrpRLClassViolatePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLClassViolatePkts.setStatus(_A)
_RbnCctGrpRLClassViolateDroppedOctets_Type=Counter64
_RbnCctGrpRLClassViolateDroppedOctets_Object=MibTableColumn
rbnCctGrpRLClassViolateDroppedOctets=_RbnCctGrpRLClassViolateDroppedOctets_Object((1,3,6,1,4,1,2352,2,43,1,4,1,13),_RbnCctGrpRLClassViolateDroppedOctets_Type())
rbnCctGrpRLClassViolateDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLClassViolateDroppedOctets.setStatus(_A)
_RbnCctGrpRLClassViolateDroppedPkts_Type=Counter64
_RbnCctGrpRLClassViolateDroppedPkts_Object=MibTableColumn
rbnCctGrpRLClassViolateDroppedPkts=_RbnCctGrpRLClassViolateDroppedPkts_Object((1,3,6,1,4,1,2352,2,43,1,4,1,14),_RbnCctGrpRLClassViolateDroppedPkts_Type())
rbnCctGrpRLClassViolateDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCctGrpRLClassViolateDroppedPkts.setStatus(_A)
_RbnCircuitGroupConformance_ObjectIdentity=ObjectIdentity
rbnCircuitGroupConformance=_RbnCircuitGroupConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,43,2))
_RbnCircuitGroupCompliances_ObjectIdentity=ObjectIdentity
rbnCircuitGroupCompliances=_RbnCircuitGroupCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,43,2,1))
_RbnCircuitGroupConformGroups_ObjectIdentity=ObjectIdentity
rbnCircuitGroupConformGroups=_RbnCircuitGroupConformGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,43,2,2))
rbnCctGrpStatsGroup=ObjectGroup((1,3,6,1,4,1,2352,2,43,2,2,1))
rbnCctGrpStatsGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:rbnCctGrpStatsGroup.setStatus(_A)
rbnCctGrpQStatsGroup=ObjectGroup((1,3,6,1,4,1,2352,2,43,2,2,2))
rbnCctGrpQStatsGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:rbnCctGrpQStatsGroup.setStatus(_A)
rbnCctGrpPolicyStatsGroup=ObjectGroup((1,3,6,1,4,1,2352,2,43,2,2,3))
rbnCctGrpPolicyStatsGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:rbnCctGrpPolicyStatsGroup.setStatus(_A)
rbnCCircuitGroupCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,43,2,1,1))
rbnCCircuitGroupCompliance.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:rbnCCircuitGroupCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbnCircuitGroupMib':rbnCircuitGroupMib,'rbnCircuitGroupObjects':rbnCircuitGroupObjects,'rbnCircuitGroupStatsTable':rbnCircuitGroupStatsTable,'rbnCircuitGroupStatsEntry':rbnCircuitGroupStatsEntry,_D:rbnCctGrpName,_K:rbnCctGrpTxOctets,_L:rbnCctGrpTxPackets,_M:rbnCctGrpTxMulticastOctets,_N:rbnCctGrpTxMulticastPackets,_O:rbnCctGrpRxOctets,_P:rbnCctGrpRxPackets,_Q:rbnCctGrpRxMulticastOctets,_R:rbnCctGrpRxMulticastPackets,_S:rbnCctGrpAdjDroppedOctets,_T:rbnCctGrpAdjDroppedPackets,_U:rbnCctGrpDownDroppedOctets,_V:rbnCctGrpDownDroppedPackets,_W:rbnCctGrpUnreachDroppedOctets,_X:rbnCctGrpUnreachDroppedPackets,_Y:rbnCctGrpUnknownEncapsOctets,_Z:rbnCctGrpUnknownEncapsPackets,'rbnCircuitGroupQTable':rbnCircuitGroupQTable,'rbnCircuitGroupQEntry':rbnCircuitGroupQEntry,_I:rbnCctGrpQueueId,_a:rbnCctGrpQTxOctets,_b:rbnCctGrpQTxPackets,_c:rbnCctGrpQWredDroppedOctets,_d:rbnCctGrpQWredDroppedPkts,_e:rbnCctGrpQTailDroppedOctets,_f:rbnCctGrpQTailDroppedPkts,'rbnCctGrpRLPolicyStatsTable':rbnCctGrpRLPolicyStatsTable,'rbnCctGrpRLPolicyStatsEntry':rbnCctGrpRLPolicyStatsEntry,_G:rbnCctGrpRLPolicyType,_g:rbnCctGrpRLPolicyName,_h:rbnCctGrpRLPolicyConformOctets,_i:rbnCctGrpRLPolicyConformPkts,_j:rbnCctGrpRLPolicyExceedOctets,_k:rbnCctGrpRLPolicyExceedPkts,_l:rbnCctGrpRLPolicyExceedDroppedOctets,_m:rbnCctGrpRLPolicyExceedDroppedPkts,_n:rbnCctGrpRLPolicyViolateOctets,_o:rbnCctGrpRLPolicyViolatePkts,_p:rbnCctGrpRLPolicyViolateDroppedOctets,_q:rbnCctGrpRLPolicyViolateDroppedPkts,'rbnCctGrpRLClassStatsTable':rbnCctGrpRLClassStatsTable,'rbnCctGrpRLClassStatsEntry':rbnCctGrpRLClassStatsEntry,_J:rbnCctGrpRLClassId,_r:rbnCctGrpRLClassName,_s:rbnCctGrpRLClassConformOctets,_t:rbnCctGrpRLClassConformPkts,_u:rbnCctGrpRLClassConformDroppedOctets,_v:rbnCctGrpRLClassConformDroppedPkts,_w:rbnCctGrpRLClassExceedOctets,_x:rbnCctGrpRLClassExceedPkts,_y:rbnCctGrpRLClassExceedDroppedOctets,_z:rbnCctGrpRLClassExceedDroppedPkts,_A0:rbnCctGrpRLClassViolateOctets,_A1:rbnCctGrpRLClassViolatePkts,_A2:rbnCctGrpRLClassViolateDroppedOctets,_A3:rbnCctGrpRLClassViolateDroppedPkts,'rbnCircuitGroupConformance':rbnCircuitGroupConformance,'rbnCircuitGroupCompliances':rbnCircuitGroupCompliances,'rbnCCircuitGroupCompliance':rbnCCircuitGroupCompliance,'rbnCircuitGroupConformGroups':rbnCircuitGroupConformGroups,_A4:rbnCctGrpStatsGroup,_A5:rbnCctGrpQStatsGroup,_A6:rbnCctGrpPolicyStatsGroup})