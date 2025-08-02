_i='nbTcActGroup'
_h='nbTcGrpGroup'
_g='nbTcGrpSupportReflectors'
_f='nbTcActReslStatus'
_e='nbTcActStatus'
_d='nbTcGroupReslConfRedPackets'
_c='nbTcGroupReslConfRedOctets'
_b='nbTcGroupReslConfYellowPackets'
_a='nbTcGroupReslConfYellowOctets'
_Z='nbTcGroupReslConfGreenPackets'
_Y='nbTcGroupReslConfGreenOctets'
_X='nbTcGroupReslAggrPackets'
_W='nbTcGroupReslAggrOctets'
_V='nbTcGroupReslMeteringReds'
_U='nbTcGroupReslMeteringYellows'
_T='nbTcGroupReslMeteringGreens'
_S='nbTcGroupReslCnfrmncCntrSet'
_R='nbTcGroupReslStatus'
_Q='nbTcGroupDscrText'
_P='nbTcGroupCntrStatus'
_O='nbTcGrpSupportLists'
_N='nbTcGrpSupportGroups'
_M='nbTcActReslEntry'
_L='nbTcGrpReslEntry'
_K='nbTcActName'
_J='nbTcGroupDscrGrpName'
_I='nbTcGroupCntrActionName'
_H='nbTcGroupCntrGrpName'
_G='DisplayString'
_F='read-write'
_E='not-accessible'
_D='SnmpAdminString'
_C='read-only'
_B='TC-GROUPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
nbTcGroups=ModuleIdentity((1,3,6,1,4,1,629,1,50,12,9,10))
if mibBuilder.loadTexts:nbTcGroups.setRevisions(('2006-01-12 00:00','2005-07-07 00:00'))
class SupportValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
class EntryValidator(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_NbSwitchG1_ObjectIdentity=ObjectIdentity
nbSwitchG1=_NbSwitchG1_ObjectIdentity((1,3,6,1,4,1,629,1))
_NbSwitchG1Il_ObjectIdentity=ObjectIdentity
nbSwitchG1Il=_NbSwitchG1Il_ObjectIdentity((1,3,6,1,4,1,629,1,50))
_NbRouterConfig_ObjectIdentity=ObjectIdentity
nbRouterConfig=_NbRouterConfig_ObjectIdentity((1,3,6,1,4,1,629,1,50,12))
_NbRtActionLists_ObjectIdentity=ObjectIdentity
nbRtActionLists=_NbRtActionLists_ObjectIdentity((1,3,6,1,4,1,629,1,50,12,9))
_NbTcGrpCntrTable_Object=MibTable
nbTcGrpCntrTable=_NbTcGrpCntrTable_Object((1,3,6,1,4,1,629,1,50,12,9,10,1))
if mibBuilder.loadTexts:nbTcGrpCntrTable.setStatus(_A)
_NbTcGrpCntrEntry_Object=MibTableRow
nbTcGrpCntrEntry=_NbTcGrpCntrEntry_Object((1,3,6,1,4,1,629,1,50,12,9,10,1,1))
nbTcGrpCntrEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:nbTcGrpCntrEntry.setStatus(_A)
class _NbTcGroupCntrGrpName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NbTcGroupCntrGrpName_Type.__name__=_D
_NbTcGroupCntrGrpName_Object=MibTableColumn
nbTcGroupCntrGrpName=_NbTcGroupCntrGrpName_Object((1,3,6,1,4,1,629,1,50,12,9,10,1,1,1),_NbTcGroupCntrGrpName_Type())
nbTcGroupCntrGrpName.setMaxAccess(_E)
if mibBuilder.loadTexts:nbTcGroupCntrGrpName.setStatus(_A)
class _NbTcGroupCntrActionName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NbTcGroupCntrActionName_Type.__name__=_D
_NbTcGroupCntrActionName_Object=MibTableColumn
nbTcGroupCntrActionName=_NbTcGroupCntrActionName_Object((1,3,6,1,4,1,629,1,50,12,9,10,1,1,2),_NbTcGroupCntrActionName_Type())
nbTcGroupCntrActionName.setMaxAccess(_E)
if mibBuilder.loadTexts:nbTcGroupCntrActionName.setStatus(_A)
_NbTcGroupCntrStatus_Type=EntryValidator
_NbTcGroupCntrStatus_Object=MibTableColumn
nbTcGroupCntrStatus=_NbTcGroupCntrStatus_Object((1,3,6,1,4,1,629,1,50,12,9,10,1,1,3),_NbTcGroupCntrStatus_Type())
nbTcGroupCntrStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:nbTcGroupCntrStatus.setStatus(_A)
_NbTcGrpDscrTable_Object=MibTable
nbTcGrpDscrTable=_NbTcGrpDscrTable_Object((1,3,6,1,4,1,629,1,50,12,9,10,2))
if mibBuilder.loadTexts:nbTcGrpDscrTable.setStatus(_A)
_NbTcGrpDscrEntry_Object=MibTableRow
nbTcGrpDscrEntry=_NbTcGrpDscrEntry_Object((1,3,6,1,4,1,629,1,50,12,9,10,2,1))
nbTcGrpDscrEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:nbTcGrpDscrEntry.setStatus(_A)
class _NbTcGroupDscrGrpName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NbTcGroupDscrGrpName_Type.__name__=_D
_NbTcGroupDscrGrpName_Object=MibTableColumn
nbTcGroupDscrGrpName=_NbTcGroupDscrGrpName_Object((1,3,6,1,4,1,629,1,50,12,9,10,2,1,1),_NbTcGroupDscrGrpName_Type())
nbTcGroupDscrGrpName.setMaxAccess(_E)
if mibBuilder.loadTexts:nbTcGroupDscrGrpName.setStatus(_A)
class _NbTcGroupDscrText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_NbTcGroupDscrText_Type.__name__=_G
_NbTcGroupDscrText_Object=MibTableColumn
nbTcGroupDscrText=_NbTcGroupDscrText_Object((1,3,6,1,4,1,629,1,50,12,9,10,2,1,3),_NbTcGroupDscrText_Type())
nbTcGroupDscrText.setMaxAccess(_F)
if mibBuilder.loadTexts:nbTcGroupDscrText.setStatus(_A)
_NbTcGrpReslTable_Object=MibTable
nbTcGrpReslTable=_NbTcGrpReslTable_Object((1,3,6,1,4,1,629,1,50,12,9,10,3))
if mibBuilder.loadTexts:nbTcGrpReslTable.setStatus(_A)
_NbTcGrpReslEntry_Object=MibTableRow
nbTcGrpReslEntry=_NbTcGrpReslEntry_Object((1,3,6,1,4,1,629,1,50,12,9,10,3,1))
if mibBuilder.loadTexts:nbTcGrpReslEntry.setStatus(_A)
_NbTcGroupReslStatus_Type=OctetString
_NbTcGroupReslStatus_Object=MibTableColumn
nbTcGroupReslStatus=_NbTcGroupReslStatus_Object((1,3,6,1,4,1,629,1,50,12,9,10,3,1,3),_NbTcGroupReslStatus_Type())
nbTcGroupReslStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbTcGroupReslStatus.setStatus(_A)
_NbTcGroupReslCnfrmncCntrSet_Type=Integer32
_NbTcGroupReslCnfrmncCntrSet_Object=MibTableColumn
nbTcGroupReslCnfrmncCntrSet=_NbTcGroupReslCnfrmncCntrSet_Object((1,3,6,1,4,1,629,1,50,12,9,10,3,1,4),_NbTcGroupReslCnfrmncCntrSet_Type())
nbTcGroupReslCnfrmncCntrSet.setMaxAccess(_C)
if mibBuilder.loadTexts:nbTcGroupReslCnfrmncCntrSet.setStatus(_A)
_NbTcGroupReslMeteringGreens_Type=Counter64
_NbTcGroupReslMeteringGreens_Object=MibTableColumn
nbTcGroupReslMeteringGreens=_NbTcGroupReslMeteringGreens_Object((1,3,6,1,4,1,629,1,50,12,9,10,3,1,5),_NbTcGroupReslMeteringGreens_Type())
nbTcGroupReslMeteringGreens.setMaxAccess(_C)
if mibBuilder.loadTexts:nbTcGroupReslMeteringGreens.setStatus(_A)
_NbTcGroupReslMeteringYellows_Type=Counter64
_NbTcGroupReslMeteringYellows_Object=MibTableColumn
nbTcGroupReslMeteringYellows=_NbTcGroupReslMeteringYellows_Object((1,3,6,1,4,1,629,1,50,12,9,10,3,1,6),_NbTcGroupReslMeteringYellows_Type())
nbTcGroupReslMeteringYellows.setMaxAccess(_C)
if mibBuilder.loadTexts:nbTcGroupReslMeteringYellows.setStatus(_A)
_NbTcGroupReslMeteringReds_Type=Counter64
_NbTcGroupReslMeteringReds_Object=MibTableColumn
nbTcGroupReslMeteringReds=_NbTcGroupReslMeteringReds_Object((1,3,6,1,4,1,629,1,50,12,9,10,3,1,7),_NbTcGroupReslMeteringReds_Type())
nbTcGroupReslMeteringReds.setMaxAccess(_C)
if mibBuilder.loadTexts:nbTcGroupReslMeteringReds.setStatus(_A)
_NbTcGroupReslAggrOctets_Type=Counter64
_NbTcGroupReslAggrOctets_Object=MibTableColumn
nbTcGroupReslAggrOctets=_NbTcGroupReslAggrOctets_Object((1,3,6,1,4,1,629,1,50,12,9,10,3,1,9),_NbTcGroupReslAggrOctets_Type())
nbTcGroupReslAggrOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:nbTcGroupReslAggrOctets.setStatus(_A)
_NbTcGroupReslAggrPackets_Type=Counter64
_NbTcGroupReslAggrPackets_Object=MibTableColumn
nbTcGroupReslAggrPackets=_NbTcGroupReslAggrPackets_Object((1,3,6,1,4,1,629,1,50,12,9,10,3,1,10),_NbTcGroupReslAggrPackets_Type())
nbTcGroupReslAggrPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:nbTcGroupReslAggrPackets.setStatus(_A)
_NbTcGroupReslConfGreenOctets_Type=Counter64
_NbTcGroupReslConfGreenOctets_Object=MibTableColumn
nbTcGroupReslConfGreenOctets=_NbTcGroupReslConfGreenOctets_Object((1,3,6,1,4,1,629,1,50,12,9,10,3,1,12),_NbTcGroupReslConfGreenOctets_Type())
nbTcGroupReslConfGreenOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:nbTcGroupReslConfGreenOctets.setStatus(_A)
_NbTcGroupReslConfGreenPackets_Type=Counter64
_NbTcGroupReslConfGreenPackets_Object=MibTableColumn
nbTcGroupReslConfGreenPackets=_NbTcGroupReslConfGreenPackets_Object((1,3,6,1,4,1,629,1,50,12,9,10,3,1,13),_NbTcGroupReslConfGreenPackets_Type())
nbTcGroupReslConfGreenPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:nbTcGroupReslConfGreenPackets.setStatus(_A)
_NbTcGroupReslConfYellowOctets_Type=Counter64
_NbTcGroupReslConfYellowOctets_Object=MibTableColumn
nbTcGroupReslConfYellowOctets=_NbTcGroupReslConfYellowOctets_Object((1,3,6,1,4,1,629,1,50,12,9,10,3,1,14),_NbTcGroupReslConfYellowOctets_Type())
nbTcGroupReslConfYellowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:nbTcGroupReslConfYellowOctets.setStatus(_A)
_NbTcGroupReslConfYellowPackets_Type=Counter64
_NbTcGroupReslConfYellowPackets_Object=MibTableColumn
nbTcGroupReslConfYellowPackets=_NbTcGroupReslConfYellowPackets_Object((1,3,6,1,4,1,629,1,50,12,9,10,3,1,15),_NbTcGroupReslConfYellowPackets_Type())
nbTcGroupReslConfYellowPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:nbTcGroupReslConfYellowPackets.setStatus(_A)
_NbTcGroupReslConfRedOctets_Type=Counter64
_NbTcGroupReslConfRedOctets_Object=MibTableColumn
nbTcGroupReslConfRedOctets=_NbTcGroupReslConfRedOctets_Object((1,3,6,1,4,1,629,1,50,12,9,10,3,1,16),_NbTcGroupReslConfRedOctets_Type())
nbTcGroupReslConfRedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:nbTcGroupReslConfRedOctets.setStatus(_A)
_NbTcGroupReslConfRedPackets_Type=Counter64
_NbTcGroupReslConfRedPackets_Object=MibTableColumn
nbTcGroupReslConfRedPackets=_NbTcGroupReslConfRedPackets_Object((1,3,6,1,4,1,629,1,50,12,9,10,3,1,17),_NbTcGroupReslConfRedPackets_Type())
nbTcGroupReslConfRedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:nbTcGroupReslConfRedPackets.setStatus(_A)
_NbTcActCtrlTable_Object=MibTable
nbTcActCtrlTable=_NbTcActCtrlTable_Object((1,3,6,1,4,1,629,1,50,12,9,10,9))
if mibBuilder.loadTexts:nbTcActCtrlTable.setStatus(_A)
_NbTcActCtrlEntry_Object=MibTableRow
nbTcActCtrlEntry=_NbTcActCtrlEntry_Object((1,3,6,1,4,1,629,1,50,12,9,10,9,1))
nbTcActCtrlEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:nbTcActCtrlEntry.setStatus(_A)
class _NbTcActName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NbTcActName_Type.__name__=_D
_NbTcActName_Object=MibTableColumn
nbTcActName=_NbTcActName_Object((1,3,6,1,4,1,629,1,50,12,9,10,9,1,1),_NbTcActName_Type())
nbTcActName.setMaxAccess(_E)
if mibBuilder.loadTexts:nbTcActName.setStatus(_A)
_NbTcActStatus_Type=EntryValidator
_NbTcActStatus_Object=MibTableColumn
nbTcActStatus=_NbTcActStatus_Object((1,3,6,1,4,1,629,1,50,12,9,10,9,1,64),_NbTcActStatus_Type())
nbTcActStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:nbTcActStatus.setStatus(_A)
_NbTcActReslTable_Object=MibTable
nbTcActReslTable=_NbTcActReslTable_Object((1,3,6,1,4,1,629,1,50,12,9,10,10))
if mibBuilder.loadTexts:nbTcActReslTable.setStatus(_A)
_NbTcActReslEntry_Object=MibTableRow
nbTcActReslEntry=_NbTcActReslEntry_Object((1,3,6,1,4,1,629,1,50,12,9,10,10,1))
if mibBuilder.loadTexts:nbTcActReslEntry.setStatus(_A)
_NbTcActReslStatus_Type=OctetString
_NbTcActReslStatus_Object=MibTableColumn
nbTcActReslStatus=_NbTcActReslStatus_Object((1,3,6,1,4,1,629,1,50,12,9,10,10,1,3),_NbTcActReslStatus_Type())
nbTcActReslStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbTcActReslStatus.setStatus(_A)
_NbTcGrpSupport_ObjectIdentity=ObjectIdentity
nbTcGrpSupport=_NbTcGrpSupport_ObjectIdentity((1,3,6,1,4,1,629,1,50,12,9,10,100))
_NbTcGrpSupportGroups_Type=SupportValue
_NbTcGrpSupportGroups_Object=MibScalar
nbTcGrpSupportGroups=_NbTcGrpSupportGroups_Object((1,3,6,1,4,1,629,1,50,12,9,10,100,2),_NbTcGrpSupportGroups_Type())
nbTcGrpSupportGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:nbTcGrpSupportGroups.setStatus(_A)
_NbTcGrpSupportLists_Type=SupportValue
_NbTcGrpSupportLists_Object=MibScalar
nbTcGrpSupportLists=_NbTcGrpSupportLists_Object((1,3,6,1,4,1,629,1,50,12,9,10,100,9),_NbTcGrpSupportLists_Type())
nbTcGrpSupportLists.setMaxAccess(_C)
if mibBuilder.loadTexts:nbTcGrpSupportLists.setStatus(_A)
_NbTcGrpConformance_ObjectIdentity=ObjectIdentity
nbTcGrpConformance=_NbTcGrpConformance_ObjectIdentity((1,3,6,1,4,1,629,1,50,12,9,10,101))
_NbTcGrpMIBCompliances_ObjectIdentity=ObjectIdentity
nbTcGrpMIBCompliances=_NbTcGrpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,629,1,50,12,9,10,101,1))
_NbTcGrpMIBGroups_ObjectIdentity=ObjectIdentity
nbTcGrpMIBGroups=_NbTcGrpMIBGroups_ObjectIdentity((1,3,6,1,4,1,629,1,50,12,9,10,101,2))
nbTcGrpCntrEntry.registerAugmentions((_B,_L))
nbTcGrpReslEntry.setIndexNames(*nbTcGrpCntrEntry.getIndexNames())
nbTcActCtrlEntry.registerAugmentions((_B,_M))
nbTcActReslEntry.setIndexNames(*nbTcActCtrlEntry.getIndexNames())
nbTcGrpSupportReflectors=ObjectGroup((1,3,6,1,4,1,629,1,50,12,9,10,101,2,1))
nbTcGrpSupportReflectors.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:nbTcGrpSupportReflectors.setStatus(_A)
nbTcGrpGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,12,9,10,101,2,2))
nbTcGrpGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:nbTcGrpGroup.setStatus(_A)
nbTcActGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,12,9,10,101,2,3))
nbTcActGroup.setObjects(*((_B,_e),(_B,_f)))
if mibBuilder.loadTexts:nbTcActGroup.setStatus(_A)
nbTcGrpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,629,1,50,12,9,10,101,1,1))
nbTcGrpMIBCompliance.setObjects(*((_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:nbTcGrpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SupportValue':SupportValue,'EntryValidator':EntryValidator,'nbase':nbase,'nbSwitchG1':nbSwitchG1,'nbSwitchG1Il':nbSwitchG1Il,'nbRouterConfig':nbRouterConfig,'nbRtActionLists':nbRtActionLists,'nbTcGroups':nbTcGroups,'nbTcGrpCntrTable':nbTcGrpCntrTable,'nbTcGrpCntrEntry':nbTcGrpCntrEntry,_H:nbTcGroupCntrGrpName,_I:nbTcGroupCntrActionName,_P:nbTcGroupCntrStatus,'nbTcGrpDscrTable':nbTcGrpDscrTable,'nbTcGrpDscrEntry':nbTcGrpDscrEntry,_J:nbTcGroupDscrGrpName,_Q:nbTcGroupDscrText,'nbTcGrpReslTable':nbTcGrpReslTable,_L:nbTcGrpReslEntry,_R:nbTcGroupReslStatus,_S:nbTcGroupReslCnfrmncCntrSet,_T:nbTcGroupReslMeteringGreens,_U:nbTcGroupReslMeteringYellows,_V:nbTcGroupReslMeteringReds,_W:nbTcGroupReslAggrOctets,_X:nbTcGroupReslAggrPackets,_Y:nbTcGroupReslConfGreenOctets,_Z:nbTcGroupReslConfGreenPackets,_a:nbTcGroupReslConfYellowOctets,_b:nbTcGroupReslConfYellowPackets,_c:nbTcGroupReslConfRedOctets,_d:nbTcGroupReslConfRedPackets,'nbTcActCtrlTable':nbTcActCtrlTable,'nbTcActCtrlEntry':nbTcActCtrlEntry,_K:nbTcActName,_e:nbTcActStatus,'nbTcActReslTable':nbTcActReslTable,_M:nbTcActReslEntry,_f:nbTcActReslStatus,'nbTcGrpSupport':nbTcGrpSupport,_N:nbTcGrpSupportGroups,_O:nbTcGrpSupportLists,'nbTcGrpConformance':nbTcGrpConformance,'nbTcGrpMIBCompliances':nbTcGrpMIBCompliances,'nbTcGrpMIBCompliance':nbTcGrpMIBCompliance,'nbTcGrpMIBGroups':nbTcGrpMIBGroups,_g:nbTcGrpSupportReflectors,_h:nbTcGrpGroup,_i:nbTcActGroup})