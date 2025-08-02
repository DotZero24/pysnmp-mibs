_L='eltPolicyActionEntry'
_K='eltPolicyMeteringClassEntry'
_J='eltPolicyVlanCfgEntry'
_I='eltPolicyTrustModeEntry'
_H='eltPolicyClassifierEntry'
_G='eltPolicyVptValue'
_F='TruthValue'
_E='Integer32'
_D='Unsigned32'
_C='ELTEX-POLICY-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
diffServClassifierEntry,=mibBuilder.importSymbols('DIFF-SERV-MIB','diffServClassifierEntry')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
PortList,VlanId=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanId')
Percents,VlanPriority=mibBuilder.importSymbols('RADLAN-MIB','Percents','VlanPriority')
rlPolicyActionEntry,rlPolicyClassifierEntry,rlPolicyMeteringClassEntry,rlPolicyTrustModeEntry,rlPolicyVlanCfgEntry=mibBuilder.importSymbols('RADLAN-POLICY-MIB','rlPolicyActionEntry','rlPolicyClassifierEntry','rlPolicyMeteringClassEntry','rlPolicyTrustModeEntry','rlPolicyVlanCfgEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso','zeroDotZero')
DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','TextualConvention',_F)
eltMesPolicy=ModuleIdentity((1,3,6,1,4,1,35265,1,23,59))
class EltPolicyTrustTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('cos',1),('dscp',2),('cos-dscp',3)))
_EltPolicyClassifier_ObjectIdentity=ObjectIdentity
eltPolicyClassifier=_EltPolicyClassifier_ObjectIdentity((1,3,6,1,4,1,35265,1,23,59,2))
_EltPolicyClassifierTable_Object=MibTable
eltPolicyClassifierTable=_EltPolicyClassifierTable_Object((1,3,6,1,4,1,35265,1,23,59,2,4))
if mibBuilder.loadTexts:eltPolicyClassifierTable.setStatus(_A)
_EltPolicyClassifierEntry_Object=MibTableRow
eltPolicyClassifierEntry=_EltPolicyClassifierEntry_Object((1,3,6,1,4,1,35265,1,23,59,2,4,1))
if mibBuilder.loadTexts:eltPolicyClassifierEntry.setStatus(_A)
_EltPolicyClassifierInListVlanId1To1024_Type=OctetString
_EltPolicyClassifierInListVlanId1To1024_Object=MibTableColumn
eltPolicyClassifierInListVlanId1To1024=_EltPolicyClassifierInListVlanId1To1024_Object((1,3,6,1,4,1,35265,1,23,59,2,4,1,1),_EltPolicyClassifierInListVlanId1To1024_Type())
eltPolicyClassifierInListVlanId1To1024.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPolicyClassifierInListVlanId1To1024.setStatus(_A)
_EltPolicyClassifierInListVlanId1025To2048_Type=OctetString
_EltPolicyClassifierInListVlanId1025To2048_Object=MibTableColumn
eltPolicyClassifierInListVlanId1025To2048=_EltPolicyClassifierInListVlanId1025To2048_Object((1,3,6,1,4,1,35265,1,23,59,2,4,1,2),_EltPolicyClassifierInListVlanId1025To2048_Type())
eltPolicyClassifierInListVlanId1025To2048.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPolicyClassifierInListVlanId1025To2048.setStatus(_A)
_EltPolicyClassifierInListVlanId2049To3072_Type=OctetString
_EltPolicyClassifierInListVlanId2049To3072_Object=MibTableColumn
eltPolicyClassifierInListVlanId2049To3072=_EltPolicyClassifierInListVlanId2049To3072_Object((1,3,6,1,4,1,35265,1,23,59,2,4,1,3),_EltPolicyClassifierInListVlanId2049To3072_Type())
eltPolicyClassifierInListVlanId2049To3072.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPolicyClassifierInListVlanId2049To3072.setStatus(_A)
_EltPolicyClassifierInListVlanId3073To4096_Type=OctetString
_EltPolicyClassifierInListVlanId3073To4096_Object=MibTableColumn
eltPolicyClassifierInListVlanId3073To4096=_EltPolicyClassifierInListVlanId3073To4096_Object((1,3,6,1,4,1,35265,1,23,59,2,4,1,4),_EltPolicyClassifierInListVlanId3073To4096_Type())
eltPolicyClassifierInListVlanId3073To4096.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPolicyClassifierInListVlanId3073To4096.setStatus(_A)
_EltPolicyMapping_ObjectIdentity=ObjectIdentity
eltPolicyMapping=_EltPolicyMapping_ObjectIdentity((1,3,6,1,4,1,35265,1,23,59,3))
_EltPolicyVptDscpTable_Object=MibTable
eltPolicyVptDscpTable=_EltPolicyVptDscpTable_Object((1,3,6,1,4,1,35265,1,23,59,3,1))
if mibBuilder.loadTexts:eltPolicyVptDscpTable.setStatus(_A)
_EltPolicyVptDscpEntry_Object=MibTableRow
eltPolicyVptDscpEntry=_EltPolicyVptDscpEntry_Object((1,3,6,1,4,1,35265,1,23,59,3,1,1))
eltPolicyVptDscpEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:eltPolicyVptDscpEntry.setStatus(_A)
class _EltPolicyVptValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_EltPolicyVptValue_Type.__name__=_E
_EltPolicyVptValue_Object=MibTableColumn
eltPolicyVptValue=_EltPolicyVptValue_Object((1,3,6,1,4,1,35265,1,23,59,3,1,1,1),_EltPolicyVptValue_Type())
eltPolicyVptValue.setMaxAccess('read-only')
if mibBuilder.loadTexts:eltPolicyVptValue.setStatus(_A)
class _EltPolicyDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_EltPolicyDscpValue_Type.__name__=_E
_EltPolicyDscpValue_Object=MibTableColumn
eltPolicyDscpValue=_EltPolicyDscpValue_Object((1,3,6,1,4,1,35265,1,23,59,3,1,1,2),_EltPolicyDscpValue_Type())
eltPolicyDscpValue.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPolicyDscpValue.setStatus(_A)
_EltPolicyVptDscpStatus_Type=RowStatus
_EltPolicyVptDscpStatus_Object=MibTableColumn
eltPolicyVptDscpStatus=_EltPolicyVptDscpStatus_Object((1,3,6,1,4,1,35265,1,23,59,3,1,1,3),_EltPolicyVptDscpStatus_Type())
eltPolicyVptDscpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPolicyVptDscpStatus.setStatus(_A)
_EltPolicyTrustModeTable_Object=MibTable
eltPolicyTrustModeTable=_EltPolicyTrustModeTable_Object((1,3,6,1,4,1,35265,1,23,59,3,2))
if mibBuilder.loadTexts:eltPolicyTrustModeTable.setStatus(_A)
_EltPolicyTrustModeEntry_Object=MibTableRow
eltPolicyTrustModeEntry=_EltPolicyTrustModeEntry_Object((1,3,6,1,4,1,35265,1,23,59,3,2,1))
if mibBuilder.loadTexts:eltPolicyTrustModeEntry.setStatus(_A)
_EltPolicyTrustModePortMode_Type=EltPolicyTrustTypes
_EltPolicyTrustModePortMode_Object=MibTableColumn
eltPolicyTrustModePortMode=_EltPolicyTrustModePortMode_Object((1,3,6,1,4,1,35265,1,23,59,3,2,1,1),_EltPolicyTrustModePortMode_Type())
eltPolicyTrustModePortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPolicyTrustModePortMode.setStatus(_A)
_EltPolicyVlanConfiguration_ObjectIdentity=ObjectIdentity
eltPolicyVlanConfiguration=_EltPolicyVlanConfiguration_ObjectIdentity((1,3,6,1,4,1,35265,1,23,59,5))
_EltPolicyVlanConfigurationTable_Object=MibTable
eltPolicyVlanConfigurationTable=_EltPolicyVlanConfigurationTable_Object((1,3,6,1,4,1,35265,1,23,59,5,1))
if mibBuilder.loadTexts:eltPolicyVlanConfigurationTable.setStatus(_A)
_EltPolicyVlanCfgEntry_Object=MibTableRow
eltPolicyVlanCfgEntry=_EltPolicyVlanCfgEntry_Object((1,3,6,1,4,1,35265,1,23,59,5,1,1))
if mibBuilder.loadTexts:eltPolicyVlanCfgEntry.setStatus(_A)
class _EltPolicyVlanCfgCirPortRateLimitPps_Type(Unsigned32):defaultValue=0
_EltPolicyVlanCfgCirPortRateLimitPps_Type.__name__=_D
_EltPolicyVlanCfgCirPortRateLimitPps_Object=MibTableColumn
eltPolicyVlanCfgCirPortRateLimitPps=_EltPolicyVlanCfgCirPortRateLimitPps_Object((1,3,6,1,4,1,35265,1,23,59,5,1,1,1),_EltPolicyVlanCfgCirPortRateLimitPps_Type())
eltPolicyVlanCfgCirPortRateLimitPps.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPolicyVlanCfgCirPortRateLimitPps.setStatus(_A)
class _EltPolicyVlanCfgCbsPortRateLimitPackets_Type(Unsigned32):defaultValue=0
_EltPolicyVlanCfgCbsPortRateLimitPackets_Type.__name__=_D
_EltPolicyVlanCfgCbsPortRateLimitPackets_Object=MibTableColumn
eltPolicyVlanCfgCbsPortRateLimitPackets=_EltPolicyVlanCfgCbsPortRateLimitPackets_Object((1,3,6,1,4,1,35265,1,23,59,5,1,1,2),_EltPolicyVlanCfgCbsPortRateLimitPackets_Type())
eltPolicyVlanCfgCbsPortRateLimitPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPolicyVlanCfgCbsPortRateLimitPackets.setStatus(_A)
_EltPolicyMeterClass_ObjectIdentity=ObjectIdentity
eltPolicyMeterClass=_EltPolicyMeterClass_ObjectIdentity((1,3,6,1,4,1,35265,1,23,59,6))
_EltPolicyMeterClassTable_Object=MibTable
eltPolicyMeterClassTable=_EltPolicyMeterClassTable_Object((1,3,6,1,4,1,35265,1,23,59,6,1))
if mibBuilder.loadTexts:eltPolicyMeterClassTable.setStatus(_A)
_EltPolicyMeteringClassEntry_Object=MibTableRow
eltPolicyMeteringClassEntry=_EltPolicyMeteringClassEntry_Object((1,3,6,1,4,1,35265,1,23,59,6,1,1))
if mibBuilder.loadTexts:eltPolicyMeteringClassEntry.setStatus(_A)
class _EltPolicyMeteringClassAggregateMeterRatePps_Type(Unsigned32):defaultValue=0
_EltPolicyMeteringClassAggregateMeterRatePps_Type.__name__=_D
_EltPolicyMeteringClassAggregateMeterRatePps_Object=MibTableColumn
eltPolicyMeteringClassAggregateMeterRatePps=_EltPolicyMeteringClassAggregateMeterRatePps_Object((1,3,6,1,4,1,35265,1,23,59,6,1,1,1),_EltPolicyMeteringClassAggregateMeterRatePps_Type())
eltPolicyMeteringClassAggregateMeterRatePps.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPolicyMeteringClassAggregateMeterRatePps.setStatus(_A)
class _EltPolicyMeteringClassAggregateMeterBurstSizePackets_Type(Unsigned32):defaultValue=0
_EltPolicyMeteringClassAggregateMeterBurstSizePackets_Type.__name__=_D
_EltPolicyMeteringClassAggregateMeterBurstSizePackets_Object=MibTableColumn
eltPolicyMeteringClassAggregateMeterBurstSizePackets=_EltPolicyMeteringClassAggregateMeterBurstSizePackets_Object((1,3,6,1,4,1,35265,1,23,59,6,1,1,2),_EltPolicyMeteringClassAggregateMeterBurstSizePackets_Type())
eltPolicyMeteringClassAggregateMeterBurstSizePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPolicyMeteringClassAggregateMeterBurstSizePackets.setStatus(_A)
_EltPolicyAction_ObjectIdentity=ObjectIdentity
eltPolicyAction=_EltPolicyAction_ObjectIdentity((1,3,6,1,4,1,35265,1,23,59,7))
_EltPolicyActionTable_Object=MibTable
eltPolicyActionTable=_EltPolicyActionTable_Object((1,3,6,1,4,1,35265,1,23,59,7,2))
if mibBuilder.loadTexts:eltPolicyActionTable.setStatus(_A)
_EltPolicyActionEntry_Object=MibTableRow
eltPolicyActionEntry=_EltPolicyActionEntry_Object((1,3,6,1,4,1,35265,1,23,59,7,2,1))
if mibBuilder.loadTexts:eltPolicyActionEntry.setStatus(_A)
class _EltPolicyPpsActionNonDsOutProfileDropPrecedence_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('low',1),('medium',2),('high',3),('drop',4)))
_EltPolicyPpsActionNonDsOutProfileDropPrecedence_Type.__name__=_E
_EltPolicyPpsActionNonDsOutProfileDropPrecedence_Object=MibTableColumn
eltPolicyPpsActionNonDsOutProfileDropPrecedence=_EltPolicyPpsActionNonDsOutProfileDropPrecedence_Object((1,3,6,1,4,1,35265,1,23,59,7,2,1,1),_EltPolicyPpsActionNonDsOutProfileDropPrecedence_Type())
eltPolicyPpsActionNonDsOutProfileDropPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPolicyPpsActionNonDsOutProfileDropPrecedence.setStatus(_A)
class _EltPolicyPpsActionChangeDscpNonConform_Type(TruthValue):defaultValue=2
_EltPolicyPpsActionChangeDscpNonConform_Type.__name__=_F
_EltPolicyPpsActionChangeDscpNonConform_Object=MibTableColumn
eltPolicyPpsActionChangeDscpNonConform=_EltPolicyPpsActionChangeDscpNonConform_Object((1,3,6,1,4,1,35265,1,23,59,7,2,1,2),_EltPolicyPpsActionChangeDscpNonConform_Type())
eltPolicyPpsActionChangeDscpNonConform.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPolicyPpsActionChangeDscpNonConform.setStatus(_A)
rlPolicyClassifierEntry.registerAugmentions((_C,_H))
eltPolicyClassifierEntry.setIndexNames(*rlPolicyClassifierEntry.getIndexNames())
rlPolicyTrustModeEntry.registerAugmentions((_C,_I))
eltPolicyTrustModeEntry.setIndexNames(*rlPolicyTrustModeEntry.getIndexNames())
rlPolicyVlanCfgEntry.registerAugmentions((_C,_J))
eltPolicyVlanCfgEntry.setIndexNames(*rlPolicyVlanCfgEntry.getIndexNames())
rlPolicyMeteringClassEntry.registerAugmentions((_C,_K))
eltPolicyMeteringClassEntry.setIndexNames(*rlPolicyMeteringClassEntry.getIndexNames())
rlPolicyActionEntry.registerAugmentions((_C,_L))
eltPolicyActionEntry.setIndexNames(*rlPolicyActionEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'EltPolicyTrustTypes':EltPolicyTrustTypes,'eltMesPolicy':eltMesPolicy,'eltPolicyClassifier':eltPolicyClassifier,'eltPolicyClassifierTable':eltPolicyClassifierTable,_H:eltPolicyClassifierEntry,'eltPolicyClassifierInListVlanId1To1024':eltPolicyClassifierInListVlanId1To1024,'eltPolicyClassifierInListVlanId1025To2048':eltPolicyClassifierInListVlanId1025To2048,'eltPolicyClassifierInListVlanId2049To3072':eltPolicyClassifierInListVlanId2049To3072,'eltPolicyClassifierInListVlanId3073To4096':eltPolicyClassifierInListVlanId3073To4096,'eltPolicyMapping':eltPolicyMapping,'eltPolicyVptDscpTable':eltPolicyVptDscpTable,'eltPolicyVptDscpEntry':eltPolicyVptDscpEntry,_G:eltPolicyVptValue,'eltPolicyDscpValue':eltPolicyDscpValue,'eltPolicyVptDscpStatus':eltPolicyVptDscpStatus,'eltPolicyTrustModeTable':eltPolicyTrustModeTable,_I:eltPolicyTrustModeEntry,'eltPolicyTrustModePortMode':eltPolicyTrustModePortMode,'eltPolicyVlanConfiguration':eltPolicyVlanConfiguration,'eltPolicyVlanConfigurationTable':eltPolicyVlanConfigurationTable,_J:eltPolicyVlanCfgEntry,'eltPolicyVlanCfgCirPortRateLimitPps':eltPolicyVlanCfgCirPortRateLimitPps,'eltPolicyVlanCfgCbsPortRateLimitPackets':eltPolicyVlanCfgCbsPortRateLimitPackets,'eltPolicyMeterClass':eltPolicyMeterClass,'eltPolicyMeterClassTable':eltPolicyMeterClassTable,_K:eltPolicyMeteringClassEntry,'eltPolicyMeteringClassAggregateMeterRatePps':eltPolicyMeteringClassAggregateMeterRatePps,'eltPolicyMeteringClassAggregateMeterBurstSizePackets':eltPolicyMeteringClassAggregateMeterBurstSizePackets,'eltPolicyAction':eltPolicyAction,'eltPolicyActionTable':eltPolicyActionTable,_L:eltPolicyActionEntry,'eltPolicyPpsActionNonDsOutProfileDropPrecedence':eltPolicyPpsActionNonDsOutProfileDropPrecedence,'eltPolicyPpsActionChangeDscpNonConform':eltPolicyPpsActionChangeDscpNonConform})