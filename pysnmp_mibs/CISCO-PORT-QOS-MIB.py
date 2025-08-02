_Ah='ciscoPortQosStatsMIBGroupRev2Supp8'
_Ag='ciscoPortQosStatsMIBGroupRev2Supp7'
_Af='ciscoPortQosStatsMIBGroupRev2Supp6'
_Ae='ciscoPortQosStatsMIBGroupRev2Supp5'
_Ad='ciscoPortQosStatsMIBGroupRev2Supp4'
_Ac='ciscoPortQosStatsMIBGroupRev1'
_Ab='ciscoPortQosStatsMIBGroup'
_Aa='cportQosCosEgressOctets'
_AZ='cportQosCosEgressPkts'
_AY='cportQosCosIngressOctets'
_AX='cportQosCosIngressPkts'
_AW='cportQosDscpEgressOctets'
_AV='cportQosDscpEgressPkts'
_AU='cportQosDscpIngressOctets'
_AT='cportQosDscpIngressPkts'
_AS='cportQosPoliceDiscontinuityTime'
_AR='cportQosPoliceViolateRate'
_AQ='cportQosPoliceExceedRate'
_AP='cportQosPoliceConformRate'
_AO='cportQosPoliceViolateOctets'
_AN='cportQosPoliceViolatePkts'
_AM='cportQosPoliceExceedOctets'
_AL='cportQosPoliceExceedPkts'
_AK='cportQosPoliceConformOctets'
_AJ='cportQosPoliceConformPkts'
_AI='cportQosClassNameLevel2'
_AH='cportQosClassNameLevel1'
_AG='cportQosClassDiscontinuityTime'
_AF='cportQosClassDropPkts'
_AE='cportQosClassEnqueuePkts'
_AD='cportQosClassName'
_AC='cportQosQueueDropPkts'
_AB='cportQosQueueEnqueuePkts'
_AA='cportQosVlanViolateProfPolicyOctets'
_A9='cportQosVlanViolateProfPolicyPkts'
_A8='cportQosVlanOutOfProfPolicyOctets'
_A7='cportQosVlanInProfPolicyOctets'
_A6='cportQosViolateProfPolicyOctets'
_A5='cportQosViolateProfPolicyPkts'
_A4='cportQosOutOfProfPolicyOctets'
_A3='cportQosInProfPolicyOctets'
_A2='cportQosVlanOutOfProfPolicyPkts'
_A1='cportQosVlanInProfPolicyPkts'
_A0='cportQosOutOfProfPolicyPkts'
_z='cportQosInProfPolicyPkts'
_y='cportQosIndexTypeNew'
_x='cportQosTSConfigBurstSize'
_w='cportQosTSConfigRate'
_v='cportQosTSConfigEnable'
_u='cportQosRLConfigBurstSize'
_t='cportQosRLConfigRate'
_s='cportQosRLConfigEnable'
_r='cportQosCosValue'
_q='cportQosDscpValue'
_p='cportQosClassIdLevel2'
_o='cportQosClassIdLevel1'
_n='cportQosClassThreshold'
_m='cportQosClassId'
_l='cportQosQueueThreshold'
_k='cportQosQueueId'
_j='cportQosDirection'
_i='ipPrecedence'
_h='cportQosRLConfigDirection'
_g='vtpVlanIndex'
_f='CISCO-VTP-MIB'
_e='ciscoPortQosStatsMIBGroupRev2Supp3'
_d='cportQosNoChangeOctets'
_c='cportQosNoChangePkts'
_b='cportQosIndexType'
_a='cportQosIndex'
_Z='ciscoPortQosStatsMIBGroupRev2Supp2'
_Y='cportQosClassifiedPkts'
_X='cportQosClassifiedOctets'
_W='cportQosDropOctets'
_V='cportQosDropPkts'
_U='cportQosPostPolicyPkts'
_T='cportQosPostPolicyOctets'
_S='cportQosPrePolicyOctets'
_R='cportQosPrePolicyPkts'
_Q='ciscoPortQosStatsMIBGroupRev2Supp1'
_P='bits per second'
_O='ciscoPortQosStatsMIBGroupRev2'
_N='Octets'
_M='read-write'
_L='Unsigned32'
_K='ciscoPortQosMIBGroup'
_J='Integer32'
_I='ifIndex'
_H='IF-MIB'
_G='Packets'
_F='octets'
_E='packets'
_D='not-accessible'
_C='read-only'
_B='deprecated'
_A='CISCO-PORT-QOS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dscp,QosLayer2Cos=mibBuilder.importSymbols('CISCO-QOS-PIB-MIB','Dscp','QosLayer2Cos')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
vtpVlanIndex,=mibBuilder.importSymbols(_f,_g)
ifIndex,=mibBuilder.importSymbols(_H,_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
ciscoPortQosMIB=ModuleIdentity((1,3,6,1,4,1,9,9,189))
if mibBuilder.loadTexts:ciscoPortQosMIB.setRevisions(('2015-09-25 00:00','2008-09-10 00:00','2008-03-05 00:00','2008-01-09 00:00','2006-02-17 00:00','2005-02-23 00:00','2004-05-20 00:00','2004-01-30 00:00','2002-03-20 00:00','2001-05-15 00:00','2000-12-20 00:00'))
_CiscoPortQosMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPortQosMIBObjects=_CiscoPortQosMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,189,1))
_CportQosRLConfig_ObjectIdentity=ObjectIdentity
cportQosRLConfig=_CportQosRLConfig_ObjectIdentity((1,3,6,1,4,1,9,9,189,1,1))
_CportQosRLConfigTable_Object=MibTable
cportQosRLConfigTable=_CportQosRLConfigTable_Object((1,3,6,1,4,1,9,9,189,1,1,1))
if mibBuilder.loadTexts:cportQosRLConfigTable.setStatus(_B)
_CportQosRLConfigEntry_Object=MibTableRow
cportQosRLConfigEntry=_CportQosRLConfigEntry_Object((1,3,6,1,4,1,9,9,189,1,1,1,1))
cportQosRLConfigEntry.setIndexNames((0,_H,_I),(0,_A,_h))
if mibBuilder.loadTexts:cportQosRLConfigEntry.setStatus(_B)
class _CportQosRLConfigDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('input',1),('output',2)))
_CportQosRLConfigDirection_Type.__name__=_J
_CportQosRLConfigDirection_Object=MibTableColumn
cportQosRLConfigDirection=_CportQosRLConfigDirection_Object((1,3,6,1,4,1,9,9,189,1,1,1,1,1),_CportQosRLConfigDirection_Type())
cportQosRLConfigDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:cportQosRLConfigDirection.setStatus(_B)
_CportQosRLConfigEnable_Type=TruthValue
_CportQosRLConfigEnable_Object=MibTableColumn
cportQosRLConfigEnable=_CportQosRLConfigEnable_Object((1,3,6,1,4,1,9,9,189,1,1,1,1,2),_CportQosRLConfigEnable_Type())
cportQosRLConfigEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:cportQosRLConfigEnable.setStatus(_B)
class _CportQosRLConfigRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32000,2147483647))
_CportQosRLConfigRate_Type.__name__=_J
_CportQosRLConfigRate_Object=MibTableColumn
cportQosRLConfigRate=_CportQosRLConfigRate_Object((1,3,6,1,4,1,9,9,189,1,1,1,1,3),_CportQosRLConfigRate_Type())
cportQosRLConfigRate.setMaxAccess(_M)
if mibBuilder.loadTexts:cportQosRLConfigRate.setStatus(_B)
if mibBuilder.loadTexts:cportQosRLConfigRate.setUnits(_P)
class _CportQosRLConfigBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64000))
_CportQosRLConfigBurstSize_Type.__name__=_J
_CportQosRLConfigBurstSize_Object=MibTableColumn
cportQosRLConfigBurstSize=_CportQosRLConfigBurstSize_Object((1,3,6,1,4,1,9,9,189,1,1,1,1,4),_CportQosRLConfigBurstSize_Type())
cportQosRLConfigBurstSize.setMaxAccess(_M)
if mibBuilder.loadTexts:cportQosRLConfigBurstSize.setStatus(_B)
if mibBuilder.loadTexts:cportQosRLConfigBurstSize.setUnits('bytes')
_CportQosTSConfig_ObjectIdentity=ObjectIdentity
cportQosTSConfig=_CportQosTSConfig_ObjectIdentity((1,3,6,1,4,1,9,9,189,1,2))
_CportQosTSConfigTable_Object=MibTable
cportQosTSConfigTable=_CportQosTSConfigTable_Object((1,3,6,1,4,1,9,9,189,1,2,1))
if mibBuilder.loadTexts:cportQosTSConfigTable.setStatus(_B)
_CportQosTSConfigEntry_Object=MibTableRow
cportQosTSConfigEntry=_CportQosTSConfigEntry_Object((1,3,6,1,4,1,9,9,189,1,2,1,1))
cportQosTSConfigEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cportQosTSConfigEntry.setStatus(_B)
_CportQosTSConfigEnable_Type=TruthValue
_CportQosTSConfigEnable_Object=MibTableColumn
cportQosTSConfigEnable=_CportQosTSConfigEnable_Object((1,3,6,1,4,1,9,9,189,1,2,1,1,1),_CportQosTSConfigEnable_Type())
cportQosTSConfigEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:cportQosTSConfigEnable.setStatus(_B)
class _CportQosTSConfigRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32000,2147483647))
_CportQosTSConfigRate_Type.__name__=_J
_CportQosTSConfigRate_Object=MibTableColumn
cportQosTSConfigRate=_CportQosTSConfigRate_Object((1,3,6,1,4,1,9,9,189,1,2,1,1,2),_CportQosTSConfigRate_Type())
cportQosTSConfigRate.setMaxAccess(_M)
if mibBuilder.loadTexts:cportQosTSConfigRate.setStatus(_B)
if mibBuilder.loadTexts:cportQosTSConfigRate.setUnits(_P)
class _CportQosTSConfigBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512000))
_CportQosTSConfigBurstSize_Type.__name__=_J
_CportQosTSConfigBurstSize_Object=MibTableColumn
cportQosTSConfigBurstSize=_CportQosTSConfigBurstSize_Object((1,3,6,1,4,1,9,9,189,1,2,1,1,3),_CportQosTSConfigBurstSize_Type())
cportQosTSConfigBurstSize.setMaxAccess(_M)
if mibBuilder.loadTexts:cportQosTSConfigBurstSize.setStatus(_B)
if mibBuilder.loadTexts:cportQosTSConfigBurstSize.setUnits('bits')
_CportQosStatistics_ObjectIdentity=ObjectIdentity
cportQosStatistics=_CportQosStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,189,1,3))
class _CportQosIndexType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('dscp',2),(_i,3),('cos',4)))
_CportQosIndexType_Type.__name__=_J
_CportQosIndexType_Object=MibScalar
cportQosIndexType=_CportQosIndexType_Object((1,3,6,1,4,1,9,9,189,1,3,1),_CportQosIndexType_Type())
cportQosIndexType.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosIndexType.setStatus(_B)
_CportQosStatsTable_Object=MibTable
cportQosStatsTable=_CportQosStatsTable_Object((1,3,6,1,4,1,9,9,189,1,3,2))
if mibBuilder.loadTexts:cportQosStatsTable.setStatus(_B)
_CportQosStatsEntry_Object=MibTableRow
cportQosStatsEntry=_CportQosStatsEntry_Object((1,3,6,1,4,1,9,9,189,1,3,2,1))
cportQosStatsEntry.setIndexNames((0,_H,_I),(0,_A,_j),(0,_A,_a))
if mibBuilder.loadTexts:cportQosStatsEntry.setStatus(_B)
class _CportQosDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ingress',1),('egress',2)))
_CportQosDirection_Type.__name__=_J
_CportQosDirection_Object=MibTableColumn
cportQosDirection=_CportQosDirection_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,1),_CportQosDirection_Type())
cportQosDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:cportQosDirection.setStatus(_B)
_CportQosIndex_Type=Unsigned32
_CportQosIndex_Object=MibTableColumn
cportQosIndex=_CportQosIndex_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,2),_CportQosIndex_Type())
cportQosIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cportQosIndex.setStatus(_B)
_CportQosPrePolicyPkts_Type=Counter64
_CportQosPrePolicyPkts_Object=MibTableColumn
cportQosPrePolicyPkts=_CportQosPrePolicyPkts_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,3),_CportQosPrePolicyPkts_Type())
cportQosPrePolicyPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosPrePolicyPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosPrePolicyPkts.setUnits(_E)
_CportQosPrePolicyOctets_Type=Counter64
_CportQosPrePolicyOctets_Object=MibTableColumn
cportQosPrePolicyOctets=_CportQosPrePolicyOctets_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,4),_CportQosPrePolicyOctets_Type())
cportQosPrePolicyOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosPrePolicyOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosPrePolicyOctets.setUnits(_F)
_CportQosPostPolicyPkts_Type=Counter64
_CportQosPostPolicyPkts_Object=MibTableColumn
cportQosPostPolicyPkts=_CportQosPostPolicyPkts_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,5),_CportQosPostPolicyPkts_Type())
cportQosPostPolicyPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosPostPolicyPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosPostPolicyPkts.setUnits(_E)
_CportQosPostPolicyOctets_Type=Counter64
_CportQosPostPolicyOctets_Object=MibTableColumn
cportQosPostPolicyOctets=_CportQosPostPolicyOctets_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,6),_CportQosPostPolicyOctets_Type())
cportQosPostPolicyOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosPostPolicyOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosPostPolicyOctets.setUnits(_F)
_CportQosDropPkts_Type=Counter64
_CportQosDropPkts_Object=MibTableColumn
cportQosDropPkts=_CportQosDropPkts_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,7),_CportQosDropPkts_Type())
cportQosDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosDropPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosDropPkts.setUnits(_E)
_CportQosDropOctets_Type=Counter64
_CportQosDropOctets_Object=MibTableColumn
cportQosDropOctets=_CportQosDropOctets_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,8),_CportQosDropOctets_Type())
cportQosDropOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosDropOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosDropOctets.setUnits(_F)
_CportQosClassifiedOctets_Type=Counter64
_CportQosClassifiedOctets_Object=MibTableColumn
cportQosClassifiedOctets=_CportQosClassifiedOctets_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,9),_CportQosClassifiedOctets_Type())
cportQosClassifiedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosClassifiedOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosClassifiedOctets.setUnits(_F)
_CportQosClassifiedPkts_Type=Counter64
_CportQosClassifiedPkts_Object=MibTableColumn
cportQosClassifiedPkts=_CportQosClassifiedPkts_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,10),_CportQosClassifiedPkts_Type())
cportQosClassifiedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosClassifiedPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosClassifiedPkts.setUnits(_E)
_CportQosNoChangePkts_Type=Counter64
_CportQosNoChangePkts_Object=MibTableColumn
cportQosNoChangePkts=_CportQosNoChangePkts_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,11),_CportQosNoChangePkts_Type())
cportQosNoChangePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosNoChangePkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosNoChangePkts.setUnits(_E)
_CportQosNoChangeOctets_Type=Counter64
_CportQosNoChangeOctets_Object=MibTableColumn
cportQosNoChangeOctets=_CportQosNoChangeOctets_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,12),_CportQosNoChangeOctets_Type())
cportQosNoChangeOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosNoChangeOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosNoChangeOctets.setUnits(_F)
_CportQosInProfPolicyPkts_Type=Counter64
_CportQosInProfPolicyPkts_Object=MibTableColumn
cportQosInProfPolicyPkts=_CportQosInProfPolicyPkts_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,13),_CportQosInProfPolicyPkts_Type())
cportQosInProfPolicyPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosInProfPolicyPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosInProfPolicyPkts.setUnits(_E)
_CportQosOutOfProfPolicyPkts_Type=Counter64
_CportQosOutOfProfPolicyPkts_Object=MibTableColumn
cportQosOutOfProfPolicyPkts=_CportQosOutOfProfPolicyPkts_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,14),_CportQosOutOfProfPolicyPkts_Type())
cportQosOutOfProfPolicyPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosOutOfProfPolicyPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosOutOfProfPolicyPkts.setUnits(_E)
_CportQosInProfPolicyOctets_Type=Counter64
_CportQosInProfPolicyOctets_Object=MibTableColumn
cportQosInProfPolicyOctets=_CportQosInProfPolicyOctets_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,15),_CportQosInProfPolicyOctets_Type())
cportQosInProfPolicyOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosInProfPolicyOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosInProfPolicyOctets.setUnits(_F)
_CportQosOutOfProfPolicyOctets_Type=Counter64
_CportQosOutOfProfPolicyOctets_Object=MibTableColumn
cportQosOutOfProfPolicyOctets=_CportQosOutOfProfPolicyOctets_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,16),_CportQosOutOfProfPolicyOctets_Type())
cportQosOutOfProfPolicyOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosOutOfProfPolicyOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosOutOfProfPolicyOctets.setUnits(_F)
_CportQosViolateProfPolicyPkts_Type=Counter64
_CportQosViolateProfPolicyPkts_Object=MibTableColumn
cportQosViolateProfPolicyPkts=_CportQosViolateProfPolicyPkts_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,17),_CportQosViolateProfPolicyPkts_Type())
cportQosViolateProfPolicyPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosViolateProfPolicyPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosViolateProfPolicyPkts.setUnits(_E)
_CportQosViolateProfPolicyOctets_Type=Counter64
_CportQosViolateProfPolicyOctets_Object=MibTableColumn
cportQosViolateProfPolicyOctets=_CportQosViolateProfPolicyOctets_Object((1,3,6,1,4,1,9,9,189,1,3,2,1,18),_CportQosViolateProfPolicyOctets_Type())
cportQosViolateProfPolicyOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosViolateProfPolicyOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosViolateProfPolicyOctets.setUnits(_F)
class _CportQosIndexTypeNew_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('dscp',2),(_i,3),('cos',4),('police',5)))
_CportQosIndexTypeNew_Type.__name__=_J
_CportQosIndexTypeNew_Object=MibScalar
cportQosIndexTypeNew=_CportQosIndexTypeNew_Object((1,3,6,1,4,1,9,9,189,1,3,3),_CportQosIndexTypeNew_Type())
cportQosIndexTypeNew.setMaxAccess(_M)
if mibBuilder.loadTexts:cportQosIndexTypeNew.setStatus(_B)
_CportQosInVlanStatsTable_Object=MibTable
cportQosInVlanStatsTable=_CportQosInVlanStatsTable_Object((1,3,6,1,4,1,9,9,189,1,3,4))
if mibBuilder.loadTexts:cportQosInVlanStatsTable.setStatus(_B)
_CportQosInVlanStatsEntry_Object=MibTableRow
cportQosInVlanStatsEntry=_CportQosInVlanStatsEntry_Object((1,3,6,1,4,1,9,9,189,1,3,4,1))
cportQosInVlanStatsEntry.setIndexNames((0,_H,_I),(0,_f,_g),(0,_A,_a))
if mibBuilder.loadTexts:cportQosInVlanStatsEntry.setStatus(_B)
_CportQosVlanInProfPolicyPkts_Type=Counter64
_CportQosVlanInProfPolicyPkts_Object=MibTableColumn
cportQosVlanInProfPolicyPkts=_CportQosVlanInProfPolicyPkts_Object((1,3,6,1,4,1,9,9,189,1,3,4,1,1),_CportQosVlanInProfPolicyPkts_Type())
cportQosVlanInProfPolicyPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosVlanInProfPolicyPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosVlanInProfPolicyPkts.setUnits(_E)
_CportQosVlanOutOfProfPolicyPkts_Type=Counter64
_CportQosVlanOutOfProfPolicyPkts_Object=MibTableColumn
cportQosVlanOutOfProfPolicyPkts=_CportQosVlanOutOfProfPolicyPkts_Object((1,3,6,1,4,1,9,9,189,1,3,4,1,2),_CportQosVlanOutOfProfPolicyPkts_Type())
cportQosVlanOutOfProfPolicyPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosVlanOutOfProfPolicyPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosVlanOutOfProfPolicyPkts.setUnits(_E)
_CportQosVlanInProfPolicyOctets_Type=Counter64
_CportQosVlanInProfPolicyOctets_Object=MibTableColumn
cportQosVlanInProfPolicyOctets=_CportQosVlanInProfPolicyOctets_Object((1,3,6,1,4,1,9,9,189,1,3,4,1,3),_CportQosVlanInProfPolicyOctets_Type())
cportQosVlanInProfPolicyOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosVlanInProfPolicyOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosVlanInProfPolicyOctets.setUnits(_F)
_CportQosVlanOutOfProfPolicyOctets_Type=Counter64
_CportQosVlanOutOfProfPolicyOctets_Object=MibTableColumn
cportQosVlanOutOfProfPolicyOctets=_CportQosVlanOutOfProfPolicyOctets_Object((1,3,6,1,4,1,9,9,189,1,3,4,1,4),_CportQosVlanOutOfProfPolicyOctets_Type())
cportQosVlanOutOfProfPolicyOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosVlanOutOfProfPolicyOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosVlanOutOfProfPolicyOctets.setUnits(_F)
_CportQosVlanViolateProfPolicyPkts_Type=Counter64
_CportQosVlanViolateProfPolicyPkts_Object=MibTableColumn
cportQosVlanViolateProfPolicyPkts=_CportQosVlanViolateProfPolicyPkts_Object((1,3,6,1,4,1,9,9,189,1,3,4,1,5),_CportQosVlanViolateProfPolicyPkts_Type())
cportQosVlanViolateProfPolicyPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosVlanViolateProfPolicyPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosVlanViolateProfPolicyPkts.setUnits(_E)
_CportQosVlanViolateProfPolicyOctets_Type=Counter64
_CportQosVlanViolateProfPolicyOctets_Object=MibTableColumn
cportQosVlanViolateProfPolicyOctets=_CportQosVlanViolateProfPolicyOctets_Object((1,3,6,1,4,1,9,9,189,1,3,4,1,6),_CportQosVlanViolateProfPolicyOctets_Type())
cportQosVlanViolateProfPolicyOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosVlanViolateProfPolicyOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosVlanViolateProfPolicyOctets.setUnits(_F)
_CportQosEgressQueueStatsTable_Object=MibTable
cportQosEgressQueueStatsTable=_CportQosEgressQueueStatsTable_Object((1,3,6,1,4,1,9,9,189,1,3,5))
if mibBuilder.loadTexts:cportQosEgressQueueStatsTable.setStatus(_B)
_CportQosEgressQueueStatsEntry_Object=MibTableRow
cportQosEgressQueueStatsEntry=_CportQosEgressQueueStatsEntry_Object((1,3,6,1,4,1,9,9,189,1,3,5,1))
cportQosEgressQueueStatsEntry.setIndexNames((0,_H,_I),(0,_A,_k),(0,_A,_l))
if mibBuilder.loadTexts:cportQosEgressQueueStatsEntry.setStatus(_B)
class _CportQosQueueId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CportQosQueueId_Type.__name__=_L
_CportQosQueueId_Object=MibTableColumn
cportQosQueueId=_CportQosQueueId_Object((1,3,6,1,4,1,9,9,189,1,3,5,1,1),_CportQosQueueId_Type())
cportQosQueueId.setMaxAccess(_D)
if mibBuilder.loadTexts:cportQosQueueId.setStatus(_B)
class _CportQosQueueThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CportQosQueueThreshold_Type.__name__=_L
_CportQosQueueThreshold_Object=MibTableColumn
cportQosQueueThreshold=_CportQosQueueThreshold_Object((1,3,6,1,4,1,9,9,189,1,3,5,1,2),_CportQosQueueThreshold_Type())
cportQosQueueThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cportQosQueueThreshold.setStatus(_B)
_CportQosQueueEnqueuePkts_Type=Counter64
_CportQosQueueEnqueuePkts_Object=MibTableColumn
cportQosQueueEnqueuePkts=_CportQosQueueEnqueuePkts_Object((1,3,6,1,4,1,9,9,189,1,3,5,1,3),_CportQosQueueEnqueuePkts_Type())
cportQosQueueEnqueuePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosQueueEnqueuePkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosQueueEnqueuePkts.setUnits(_G)
_CportQosQueueDropPkts_Type=Counter64
_CportQosQueueDropPkts_Object=MibTableColumn
cportQosQueueDropPkts=_CportQosQueueDropPkts_Object((1,3,6,1,4,1,9,9,189,1,3,5,1,4),_CportQosQueueDropPkts_Type())
cportQosQueueDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosQueueDropPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosQueueDropPkts.setUnits(_G)
_CportQosClassEgressStatsTable_Object=MibTable
cportQosClassEgressStatsTable=_CportQosClassEgressStatsTable_Object((1,3,6,1,4,1,9,9,189,1,3,6))
if mibBuilder.loadTexts:cportQosClassEgressStatsTable.setStatus(_B)
_CportQosClassEgressStatsEntry_Object=MibTableRow
cportQosClassEgressStatsEntry=_CportQosClassEgressStatsEntry_Object((1,3,6,1,4,1,9,9,189,1,3,6,1))
cportQosClassEgressStatsEntry.setIndexNames((0,_H,_I),(0,_A,_m),(0,_A,_n))
if mibBuilder.loadTexts:cportQosClassEgressStatsEntry.setStatus(_B)
class _CportQosClassId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CportQosClassId_Type.__name__=_L
_CportQosClassId_Object=MibTableColumn
cportQosClassId=_CportQosClassId_Object((1,3,6,1,4,1,9,9,189,1,3,6,1,1),_CportQosClassId_Type())
cportQosClassId.setMaxAccess(_D)
if mibBuilder.loadTexts:cportQosClassId.setStatus(_B)
class _CportQosClassThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CportQosClassThreshold_Type.__name__=_L
_CportQosClassThreshold_Object=MibTableColumn
cportQosClassThreshold=_CportQosClassThreshold_Object((1,3,6,1,4,1,9,9,189,1,3,6,1,2),_CportQosClassThreshold_Type())
cportQosClassThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cportQosClassThreshold.setStatus(_B)
if mibBuilder.loadTexts:cportQosClassThreshold.setUnits('Number of buffers')
_CportQosClassName_Type=SnmpAdminString
_CportQosClassName_Object=MibTableColumn
cportQosClassName=_CportQosClassName_Object((1,3,6,1,4,1,9,9,189,1,3,6,1,3),_CportQosClassName_Type())
cportQosClassName.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosClassName.setStatus(_B)
_CportQosClassEnqueuePkts_Type=Counter64
_CportQosClassEnqueuePkts_Object=MibTableColumn
cportQosClassEnqueuePkts=_CportQosClassEnqueuePkts_Object((1,3,6,1,4,1,9,9,189,1,3,6,1,4),_CportQosClassEnqueuePkts_Type())
cportQosClassEnqueuePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosClassEnqueuePkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosClassEnqueuePkts.setUnits(_G)
_CportQosClassDropPkts_Type=Counter64
_CportQosClassDropPkts_Object=MibTableColumn
cportQosClassDropPkts=_CportQosClassDropPkts_Object((1,3,6,1,4,1,9,9,189,1,3,6,1,5),_CportQosClassDropPkts_Type())
cportQosClassDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosClassDropPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosClassDropPkts.setUnits(_G)
_CportQosClassDiscontinuityTime_Type=TimeStamp
_CportQosClassDiscontinuityTime_Object=MibTableColumn
cportQosClassDiscontinuityTime=_CportQosClassDiscontinuityTime_Object((1,3,6,1,4,1,9,9,189,1,3,6,1,6),_CportQosClassDiscontinuityTime_Type())
cportQosClassDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosClassDiscontinuityTime.setStatus(_B)
_CportQosClassIngressStatsTable_Object=MibTable
cportQosClassIngressStatsTable=_CportQosClassIngressStatsTable_Object((1,3,6,1,4,1,9,9,189,1,3,7))
if mibBuilder.loadTexts:cportQosClassIngressStatsTable.setStatus(_B)
_CportQosClassIngressStatsEntry_Object=MibTableRow
cportQosClassIngressStatsEntry=_CportQosClassIngressStatsEntry_Object((1,3,6,1,4,1,9,9,189,1,3,7,1))
cportQosClassIngressStatsEntry.setIndexNames((0,_H,_I),(0,_A,_o),(0,_A,_p))
if mibBuilder.loadTexts:cportQosClassIngressStatsEntry.setStatus(_B)
class _CportQosClassIdLevel1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CportQosClassIdLevel1_Type.__name__=_L
_CportQosClassIdLevel1_Object=MibTableColumn
cportQosClassIdLevel1=_CportQosClassIdLevel1_Object((1,3,6,1,4,1,9,9,189,1,3,7,1,1),_CportQosClassIdLevel1_Type())
cportQosClassIdLevel1.setMaxAccess(_D)
if mibBuilder.loadTexts:cportQosClassIdLevel1.setStatus(_B)
class _CportQosClassIdLevel2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CportQosClassIdLevel2_Type.__name__=_L
_CportQosClassIdLevel2_Object=MibTableColumn
cportQosClassIdLevel2=_CportQosClassIdLevel2_Object((1,3,6,1,4,1,9,9,189,1,3,7,1,2),_CportQosClassIdLevel2_Type())
cportQosClassIdLevel2.setMaxAccess(_D)
if mibBuilder.loadTexts:cportQosClassIdLevel2.setStatus(_B)
_CportQosClassNameLevel1_Type=SnmpAdminString
_CportQosClassNameLevel1_Object=MibTableColumn
cportQosClassNameLevel1=_CportQosClassNameLevel1_Object((1,3,6,1,4,1,9,9,189,1,3,7,1,3),_CportQosClassNameLevel1_Type())
cportQosClassNameLevel1.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosClassNameLevel1.setStatus(_B)
_CportQosClassNameLevel2_Type=SnmpAdminString
_CportQosClassNameLevel2_Object=MibTableColumn
cportQosClassNameLevel2=_CportQosClassNameLevel2_Object((1,3,6,1,4,1,9,9,189,1,3,7,1,4),_CportQosClassNameLevel2_Type())
cportQosClassNameLevel2.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosClassNameLevel2.setStatus(_B)
_CportQosPoliceConformPkts_Type=Counter64
_CportQosPoliceConformPkts_Object=MibTableColumn
cportQosPoliceConformPkts=_CportQosPoliceConformPkts_Object((1,3,6,1,4,1,9,9,189,1,3,7,1,5),_CportQosPoliceConformPkts_Type())
cportQosPoliceConformPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosPoliceConformPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosPoliceConformPkts.setUnits(_G)
_CportQosPoliceConformOctets_Type=Counter64
_CportQosPoliceConformOctets_Object=MibTableColumn
cportQosPoliceConformOctets=_CportQosPoliceConformOctets_Object((1,3,6,1,4,1,9,9,189,1,3,7,1,6),_CportQosPoliceConformOctets_Type())
cportQosPoliceConformOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosPoliceConformOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosPoliceConformOctets.setUnits(_N)
_CportQosPoliceExceedPkts_Type=Counter64
_CportQosPoliceExceedPkts_Object=MibTableColumn
cportQosPoliceExceedPkts=_CportQosPoliceExceedPkts_Object((1,3,6,1,4,1,9,9,189,1,3,7,1,7),_CportQosPoliceExceedPkts_Type())
cportQosPoliceExceedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosPoliceExceedPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosPoliceExceedPkts.setUnits(_G)
_CportQosPoliceExceedOctets_Type=Counter64
_CportQosPoliceExceedOctets_Object=MibTableColumn
cportQosPoliceExceedOctets=_CportQosPoliceExceedOctets_Object((1,3,6,1,4,1,9,9,189,1,3,7,1,8),_CportQosPoliceExceedOctets_Type())
cportQosPoliceExceedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosPoliceExceedOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosPoliceExceedOctets.setUnits(_N)
_CportQosPoliceViolatePkts_Type=Counter64
_CportQosPoliceViolatePkts_Object=MibTableColumn
cportQosPoliceViolatePkts=_CportQosPoliceViolatePkts_Object((1,3,6,1,4,1,9,9,189,1,3,7,1,9),_CportQosPoliceViolatePkts_Type())
cportQosPoliceViolatePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosPoliceViolatePkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosPoliceViolatePkts.setUnits(_G)
_CportQosPoliceViolateOctets_Type=Counter64
_CportQosPoliceViolateOctets_Object=MibTableColumn
cportQosPoliceViolateOctets=_CportQosPoliceViolateOctets_Object((1,3,6,1,4,1,9,9,189,1,3,7,1,10),_CportQosPoliceViolateOctets_Type())
cportQosPoliceViolateOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosPoliceViolateOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosPoliceViolateOctets.setUnits(_N)
_CportQosPoliceConformRate_Type=Gauge32
_CportQosPoliceConformRate_Object=MibTableColumn
cportQosPoliceConformRate=_CportQosPoliceConformRate_Object((1,3,6,1,4,1,9,9,189,1,3,7,1,11),_CportQosPoliceConformRate_Type())
cportQosPoliceConformRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosPoliceConformRate.setStatus(_B)
if mibBuilder.loadTexts:cportQosPoliceConformRate.setUnits(_P)
_CportQosPoliceExceedRate_Type=Gauge32
_CportQosPoliceExceedRate_Object=MibTableColumn
cportQosPoliceExceedRate=_CportQosPoliceExceedRate_Object((1,3,6,1,4,1,9,9,189,1,3,7,1,12),_CportQosPoliceExceedRate_Type())
cportQosPoliceExceedRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosPoliceExceedRate.setStatus(_B)
if mibBuilder.loadTexts:cportQosPoliceExceedRate.setUnits(_P)
_CportQosPoliceViolateRate_Type=Gauge32
_CportQosPoliceViolateRate_Object=MibTableColumn
cportQosPoliceViolateRate=_CportQosPoliceViolateRate_Object((1,3,6,1,4,1,9,9,189,1,3,7,1,13),_CportQosPoliceViolateRate_Type())
cportQosPoliceViolateRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosPoliceViolateRate.setStatus(_B)
if mibBuilder.loadTexts:cportQosPoliceViolateRate.setUnits(_P)
_CportQosPoliceDiscontinuityTime_Type=TimeStamp
_CportQosPoliceDiscontinuityTime_Object=MibTableColumn
cportQosPoliceDiscontinuityTime=_CportQosPoliceDiscontinuityTime_Object((1,3,6,1,4,1,9,9,189,1,3,7,1,14),_CportQosPoliceDiscontinuityTime_Type())
cportQosPoliceDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosPoliceDiscontinuityTime.setStatus(_B)
_CportQosDscpStatsTable_Object=MibTable
cportQosDscpStatsTable=_CportQosDscpStatsTable_Object((1,3,6,1,4,1,9,9,189,1,3,8))
if mibBuilder.loadTexts:cportQosDscpStatsTable.setStatus(_B)
_CportQosDscpStatsEntry_Object=MibTableRow
cportQosDscpStatsEntry=_CportQosDscpStatsEntry_Object((1,3,6,1,4,1,9,9,189,1,3,8,1))
cportQosDscpStatsEntry.setIndexNames((0,_H,_I),(0,_A,_q))
if mibBuilder.loadTexts:cportQosDscpStatsEntry.setStatus(_B)
_CportQosDscpValue_Type=Dscp
_CportQosDscpValue_Object=MibTableColumn
cportQosDscpValue=_CportQosDscpValue_Object((1,3,6,1,4,1,9,9,189,1,3,8,1,1),_CportQosDscpValue_Type())
cportQosDscpValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cportQosDscpValue.setStatus(_B)
_CportQosDscpIngressPkts_Type=Counter64
_CportQosDscpIngressPkts_Object=MibTableColumn
cportQosDscpIngressPkts=_CportQosDscpIngressPkts_Object((1,3,6,1,4,1,9,9,189,1,3,8,1,2),_CportQosDscpIngressPkts_Type())
cportQosDscpIngressPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosDscpIngressPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosDscpIngressPkts.setUnits(_G)
_CportQosDscpIngressOctets_Type=Counter64
_CportQosDscpIngressOctets_Object=MibTableColumn
cportQosDscpIngressOctets=_CportQosDscpIngressOctets_Object((1,3,6,1,4,1,9,9,189,1,3,8,1,3),_CportQosDscpIngressOctets_Type())
cportQosDscpIngressOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosDscpIngressOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosDscpIngressOctets.setUnits(_N)
_CportQosDscpEgressPkts_Type=Counter64
_CportQosDscpEgressPkts_Object=MibTableColumn
cportQosDscpEgressPkts=_CportQosDscpEgressPkts_Object((1,3,6,1,4,1,9,9,189,1,3,8,1,4),_CportQosDscpEgressPkts_Type())
cportQosDscpEgressPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosDscpEgressPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosDscpEgressPkts.setUnits(_G)
_CportQosDscpEgressOctets_Type=Counter64
_CportQosDscpEgressOctets_Object=MibTableColumn
cportQosDscpEgressOctets=_CportQosDscpEgressOctets_Object((1,3,6,1,4,1,9,9,189,1,3,8,1,5),_CportQosDscpEgressOctets_Type())
cportQosDscpEgressOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosDscpEgressOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosDscpEgressOctets.setUnits(_N)
_CportQosCosStatsTable_Object=MibTable
cportQosCosStatsTable=_CportQosCosStatsTable_Object((1,3,6,1,4,1,9,9,189,1,3,9))
if mibBuilder.loadTexts:cportQosCosStatsTable.setStatus(_B)
_CportQosCosStatsEntry_Object=MibTableRow
cportQosCosStatsEntry=_CportQosCosStatsEntry_Object((1,3,6,1,4,1,9,9,189,1,3,9,1))
cportQosCosStatsEntry.setIndexNames((0,_H,_I),(0,_A,_r))
if mibBuilder.loadTexts:cportQosCosStatsEntry.setStatus(_B)
_CportQosCosValue_Type=QosLayer2Cos
_CportQosCosValue_Object=MibTableColumn
cportQosCosValue=_CportQosCosValue_Object((1,3,6,1,4,1,9,9,189,1,3,9,1,1),_CportQosCosValue_Type())
cportQosCosValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cportQosCosValue.setStatus(_B)
_CportQosCosIngressPkts_Type=Counter64
_CportQosCosIngressPkts_Object=MibTableColumn
cportQosCosIngressPkts=_CportQosCosIngressPkts_Object((1,3,6,1,4,1,9,9,189,1,3,9,1,2),_CportQosCosIngressPkts_Type())
cportQosCosIngressPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosCosIngressPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosCosIngressPkts.setUnits(_G)
_CportQosCosIngressOctets_Type=Counter64
_CportQosCosIngressOctets_Object=MibTableColumn
cportQosCosIngressOctets=_CportQosCosIngressOctets_Object((1,3,6,1,4,1,9,9,189,1,3,9,1,3),_CportQosCosIngressOctets_Type())
cportQosCosIngressOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosCosIngressOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosCosIngressOctets.setUnits(_N)
_CportQosCosEgressPkts_Type=Counter64
_CportQosCosEgressPkts_Object=MibTableColumn
cportQosCosEgressPkts=_CportQosCosEgressPkts_Object((1,3,6,1,4,1,9,9,189,1,3,9,1,4),_CportQosCosEgressPkts_Type())
cportQosCosEgressPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosCosEgressPkts.setStatus(_B)
if mibBuilder.loadTexts:cportQosCosEgressPkts.setUnits(_G)
_CportQosCosEgressOctets_Type=Counter64
_CportQosCosEgressOctets_Object=MibTableColumn
cportQosCosEgressOctets=_CportQosCosEgressOctets_Object((1,3,6,1,4,1,9,9,189,1,3,9,1,5),_CportQosCosEgressOctets_Type())
cportQosCosEgressOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cportQosCosEgressOctets.setStatus(_B)
if mibBuilder.loadTexts:cportQosCosEgressOctets.setUnits(_N)
_CiscoPortQosMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoPortQosMIBNotifications=_CiscoPortQosMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,189,2))
_CiscoPortQosMIBConformance_ObjectIdentity=ObjectIdentity
ciscoPortQosMIBConformance=_CiscoPortQosMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,189,3))
_CiscoPortQosMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoPortQosMIBCompliances=_CiscoPortQosMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,189,3,1))
_CiscoPortQosMIBGroups_ObjectIdentity=ObjectIdentity
ciscoPortQosMIBGroups=_CiscoPortQosMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,189,3,2))
ciscoPortQosMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,189,3,2,1))
ciscoPortQosMIBGroup.setObjects(*((_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:ciscoPortQosMIBGroup.setStatus(_B)
ciscoPortQosStatsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,189,3,2,2))
ciscoPortQosStatsMIBGroup.setObjects(*((_A,_b),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:ciscoPortQosStatsMIBGroup.setStatus(_B)
ciscoPortQosStatsMIBGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,189,3,2,3))
ciscoPortQosStatsMIBGroupRev1.setObjects(*((_A,_b),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:ciscoPortQosStatsMIBGroupRev1.setStatus(_B)
ciscoPortQosStatsMIBGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,189,3,2,4))
ciscoPortQosStatsMIBGroupRev2.setObjects(*((_A,_y),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_c),(_A,_d),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:ciscoPortQosStatsMIBGroupRev2.setStatus(_B)
ciscoPortQosStatsMIBGroupRev2Supp1=ObjectGroup((1,3,6,1,4,1,9,9,189,3,2,5))
ciscoPortQosStatsMIBGroupRev2Supp1.setObjects(*((_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:ciscoPortQosStatsMIBGroupRev2Supp1.setStatus(_B)
ciscoPortQosStatsMIBGroupRev2Supp2=ObjectGroup((1,3,6,1,4,1,9,9,189,3,2,6))
ciscoPortQosStatsMIBGroupRev2Supp2.setObjects(*((_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:ciscoPortQosStatsMIBGroupRev2Supp2.setStatus(_B)
ciscoPortQosStatsMIBGroupRev2Supp3=ObjectGroup((1,3,6,1,4,1,9,9,189,3,2,7))
ciscoPortQosStatsMIBGroupRev2Supp3.setObjects(*((_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:ciscoPortQosStatsMIBGroupRev2Supp3.setStatus(_B)
ciscoPortQosStatsMIBGroupRev2Supp4=ObjectGroup((1,3,6,1,4,1,9,9,189,3,2,8))
ciscoPortQosStatsMIBGroupRev2Supp4.setObjects(*((_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:ciscoPortQosStatsMIBGroupRev2Supp4.setStatus(_B)
ciscoPortQosStatsMIBGroupRev2Supp5=ObjectGroup((1,3,6,1,4,1,9,9,189,3,2,9))
ciscoPortQosStatsMIBGroupRev2Supp5.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:ciscoPortQosStatsMIBGroupRev2Supp5.setStatus(_B)
ciscoPortQosStatsMIBGroupRev2Supp6=ObjectGroup((1,3,6,1,4,1,9,9,189,3,2,10))
ciscoPortQosStatsMIBGroupRev2Supp6.setObjects(*((_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:ciscoPortQosStatsMIBGroupRev2Supp6.setStatus(_B)
ciscoPortQosStatsMIBGroupRev2Supp7=ObjectGroup((1,3,6,1,4,1,9,9,189,3,2,11))
ciscoPortQosStatsMIBGroupRev2Supp7.setObjects(*((_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW)))
if mibBuilder.loadTexts:ciscoPortQosStatsMIBGroupRev2Supp7.setStatus(_B)
ciscoPortQosStatsMIBGroupRev2Supp8=ObjectGroup((1,3,6,1,4,1,9,9,189,3,2,12))
ciscoPortQosStatsMIBGroupRev2Supp8.setObjects(*((_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:ciscoPortQosStatsMIBGroupRev2Supp8.setStatus(_B)
ciscoPortQosMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,189,3,1,1))
ciscoPortQosMIBCompliance.setObjects(*((_A,_K),(_A,_Ab)))
if mibBuilder.loadTexts:ciscoPortQosMIBCompliance.setStatus(_B)
ciscoPortQosMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,189,3,1,2))
ciscoPortQosMIBComplianceRev1.setObjects(*((_A,_K),(_A,_Ac)))
if mibBuilder.loadTexts:ciscoPortQosMIBComplianceRev1.setStatus(_B)
ciscoPortQosMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,189,3,1,3))
ciscoPortQosMIBComplianceRev2.setObjects(*((_A,_K),(_A,_O)))
if mibBuilder.loadTexts:ciscoPortQosMIBComplianceRev2.setStatus(_B)
ciscoPortQosMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,189,3,1,4))
ciscoPortQosMIBComplianceRev3.setObjects(*((_A,_K),(_A,_O),(_A,_Q)))
if mibBuilder.loadTexts:ciscoPortQosMIBComplianceRev3.setStatus(_B)
ciscoPortQosMIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,9,189,3,1,5))
ciscoPortQosMIBComplianceRev4.setObjects(*((_A,_K),(_A,_O),(_A,_Q),(_A,_Z)))
if mibBuilder.loadTexts:ciscoPortQosMIBComplianceRev4.setStatus(_B)
ciscoPortQosMIBComplianceRev5=ModuleCompliance((1,3,6,1,4,1,9,9,189,3,1,6))
ciscoPortQosMIBComplianceRev5.setObjects(*((_A,_K),(_A,_O),(_A,_Q),(_A,_Z),(_A,_e)))
if mibBuilder.loadTexts:ciscoPortQosMIBComplianceRev5.setStatus(_B)
ciscoPortQosMIBComplianceRev6=ModuleCompliance((1,3,6,1,4,1,9,9,189,3,1,7))
ciscoPortQosMIBComplianceRev6.setObjects(*((_A,_K),(_A,_O),(_A,_Q),(_A,_Z),(_A,_e),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:ciscoPortQosMIBComplianceRev6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoPortQosMIB':ciscoPortQosMIB,'ciscoPortQosMIBObjects':ciscoPortQosMIBObjects,'cportQosRLConfig':cportQosRLConfig,'cportQosRLConfigTable':cportQosRLConfigTable,'cportQosRLConfigEntry':cportQosRLConfigEntry,_h:cportQosRLConfigDirection,_s:cportQosRLConfigEnable,_t:cportQosRLConfigRate,_u:cportQosRLConfigBurstSize,'cportQosTSConfig':cportQosTSConfig,'cportQosTSConfigTable':cportQosTSConfigTable,'cportQosTSConfigEntry':cportQosTSConfigEntry,_v:cportQosTSConfigEnable,_w:cportQosTSConfigRate,_x:cportQosTSConfigBurstSize,'cportQosStatistics':cportQosStatistics,_b:cportQosIndexType,'cportQosStatsTable':cportQosStatsTable,'cportQosStatsEntry':cportQosStatsEntry,_j:cportQosDirection,_a:cportQosIndex,_R:cportQosPrePolicyPkts,_S:cportQosPrePolicyOctets,_U:cportQosPostPolicyPkts,_T:cportQosPostPolicyOctets,_V:cportQosDropPkts,_W:cportQosDropOctets,_X:cportQosClassifiedOctets,_Y:cportQosClassifiedPkts,_c:cportQosNoChangePkts,_d:cportQosNoChangeOctets,_z:cportQosInProfPolicyPkts,_A0:cportQosOutOfProfPolicyPkts,_A3:cportQosInProfPolicyOctets,_A4:cportQosOutOfProfPolicyOctets,_A5:cportQosViolateProfPolicyPkts,_A6:cportQosViolateProfPolicyOctets,_y:cportQosIndexTypeNew,'cportQosInVlanStatsTable':cportQosInVlanStatsTable,'cportQosInVlanStatsEntry':cportQosInVlanStatsEntry,_A1:cportQosVlanInProfPolicyPkts,_A2:cportQosVlanOutOfProfPolicyPkts,_A7:cportQosVlanInProfPolicyOctets,_A8:cportQosVlanOutOfProfPolicyOctets,_A9:cportQosVlanViolateProfPolicyPkts,_AA:cportQosVlanViolateProfPolicyOctets,'cportQosEgressQueueStatsTable':cportQosEgressQueueStatsTable,'cportQosEgressQueueStatsEntry':cportQosEgressQueueStatsEntry,_k:cportQosQueueId,_l:cportQosQueueThreshold,_AB:cportQosQueueEnqueuePkts,_AC:cportQosQueueDropPkts,'cportQosClassEgressStatsTable':cportQosClassEgressStatsTable,'cportQosClassEgressStatsEntry':cportQosClassEgressStatsEntry,_m:cportQosClassId,_n:cportQosClassThreshold,_AD:cportQosClassName,_AE:cportQosClassEnqueuePkts,_AF:cportQosClassDropPkts,_AG:cportQosClassDiscontinuityTime,'cportQosClassIngressStatsTable':cportQosClassIngressStatsTable,'cportQosClassIngressStatsEntry':cportQosClassIngressStatsEntry,_o:cportQosClassIdLevel1,_p:cportQosClassIdLevel2,_AH:cportQosClassNameLevel1,_AI:cportQosClassNameLevel2,_AJ:cportQosPoliceConformPkts,_AK:cportQosPoliceConformOctets,_AL:cportQosPoliceExceedPkts,_AM:cportQosPoliceExceedOctets,_AN:cportQosPoliceViolatePkts,_AO:cportQosPoliceViolateOctets,_AP:cportQosPoliceConformRate,_AQ:cportQosPoliceExceedRate,_AR:cportQosPoliceViolateRate,_AS:cportQosPoliceDiscontinuityTime,'cportQosDscpStatsTable':cportQosDscpStatsTable,'cportQosDscpStatsEntry':cportQosDscpStatsEntry,_q:cportQosDscpValue,_AT:cportQosDscpIngressPkts,_AU:cportQosDscpIngressOctets,_AV:cportQosDscpEgressPkts,_AW:cportQosDscpEgressOctets,'cportQosCosStatsTable':cportQosCosStatsTable,'cportQosCosStatsEntry':cportQosCosStatsEntry,_r:cportQosCosValue,_AX:cportQosCosIngressPkts,_AY:cportQosCosIngressOctets,_AZ:cportQosCosEgressPkts,_Aa:cportQosCosEgressOctets,'ciscoPortQosMIBNotifications':ciscoPortQosMIBNotifications,'ciscoPortQosMIBConformance':ciscoPortQosMIBConformance,'ciscoPortQosMIBCompliances':ciscoPortQosMIBCompliances,'ciscoPortQosMIBCompliance':ciscoPortQosMIBCompliance,'ciscoPortQosMIBComplianceRev1':ciscoPortQosMIBComplianceRev1,'ciscoPortQosMIBComplianceRev2':ciscoPortQosMIBComplianceRev2,'ciscoPortQosMIBComplianceRev3':ciscoPortQosMIBComplianceRev3,'ciscoPortQosMIBComplianceRev4':ciscoPortQosMIBComplianceRev4,'ciscoPortQosMIBComplianceRev5':ciscoPortQosMIBComplianceRev5,'ciscoPortQosMIBComplianceRev6':ciscoPortQosMIBComplianceRev6,'ciscoPortQosMIBGroups':ciscoPortQosMIBGroups,_K:ciscoPortQosMIBGroup,_Ab:ciscoPortQosStatsMIBGroup,_Ac:ciscoPortQosStatsMIBGroupRev1,_O:ciscoPortQosStatsMIBGroupRev2,_Q:ciscoPortQosStatsMIBGroupRev2Supp1,_Z:ciscoPortQosStatsMIBGroupRev2Supp2,_e:ciscoPortQosStatsMIBGroupRev2Supp3,_Ad:ciscoPortQosStatsMIBGroupRev2Supp4,_Ae:ciscoPortQosStatsMIBGroupRev2Supp5,_Af:ciscoPortQosStatsMIBGroupRev2Supp6,_Ag:ciscoPortQosStatsMIBGroupRev2Supp7,_Ah:ciscoPortQosStatsMIBGroupRev2Supp8})