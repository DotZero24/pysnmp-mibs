_K='tnSvcBaseInfoExtnEntry'
_J='tnSapBaseInfoExtnEntry'
_I='tnSapBaseStatsExtnEntry'
_H='undefined'
_G='TSapIngressAggrMeterBurstSize'
_F='TN-SAS-SERV-MIB'
_E='Integer32'
_D='TruthValue'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
tnSapBaseInfoEntry,tnSapBaseStatsEntry=mibBuilder.importSymbols('TN-SAP-MIB','tnSapBaseInfoEntry','tnSapBaseStatsEntry')
tnSvcBaseInfoEntry,=mibBuilder.importSymbols('TN-SERV-MIB','tnSvcBaseInfoEntry')
tnSASModules,tnSASObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSASModules','tnSASObjs')
tnSASServicesMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,7,2,1,1,9))
if mibBuilder.loadTexts:tnSASServicesMIBModule.setRevisions(('2020-08-14 00:00','2019-08-30 00:00','2017-11-10 00:00','2017-02-28 00:00','2015-04-07 00:00','2012-12-05 00:00','2012-08-22 00:00','2009-07-07 00:00'))
class TSapIngressAggrMeterBurstSize(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,2146959))
_TnSASServObjs_ObjectIdentity=ObjectIdentity
tnSASServObjs=_TnSASServObjs_ObjectIdentity((1,3,6,1,4,1,7483,7,2,2,2,8))
_TnSASSapObjs_ObjectIdentity=ObjectIdentity
tnSASSapObjs=_TnSASSapObjs_ObjectIdentity((1,3,6,1,4,1,7483,7,2,2,2,8,1))
_TnSapBaseStatsExtnTable_Object=MibTable
tnSapBaseStatsExtnTable=_TnSapBaseStatsExtnTable_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,1))
if mibBuilder.loadTexts:tnSapBaseStatsExtnTable.setStatus(_A)
_TnSapBaseStatsExtnEntry_Object=MibTableRow
tnSapBaseStatsExtnEntry=_TnSapBaseStatsExtnEntry_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,1,1))
if mibBuilder.loadTexts:tnSapBaseStatsExtnEntry.setStatus(_A)
_TnSapBaseStatsQosClassifiersUsed_Type=Unsigned32
_TnSapBaseStatsQosClassifiersUsed_Object=MibTableColumn
tnSapBaseStatsQosClassifiersUsed=_TnSapBaseStatsQosClassifiersUsed_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,1,1,1),_TnSapBaseStatsQosClassifiersUsed_Type())
tnSapBaseStatsQosClassifiersUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapBaseStatsQosClassifiersUsed.setStatus(_A)
_TnSapBaseStatsQosMetersUsed_Type=Unsigned32
_TnSapBaseStatsQosMetersUsed_Object=MibTableColumn
tnSapBaseStatsQosMetersUsed=_TnSapBaseStatsQosMetersUsed_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,1,1,2),_TnSapBaseStatsQosMetersUsed_Type())
tnSapBaseStatsQosMetersUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapBaseStatsQosMetersUsed.setStatus(_A)
_TnSapBaseStatsIngressForwardedPackets_Type=Counter64
_TnSapBaseStatsIngressForwardedPackets_Object=MibTableColumn
tnSapBaseStatsIngressForwardedPackets=_TnSapBaseStatsIngressForwardedPackets_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,1,1,3),_TnSapBaseStatsIngressForwardedPackets_Type())
tnSapBaseStatsIngressForwardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapBaseStatsIngressForwardedPackets.setStatus(_A)
_TnSapBaseStatsIngressForwardedOctets_Type=Counter64
_TnSapBaseStatsIngressForwardedOctets_Object=MibTableColumn
tnSapBaseStatsIngressForwardedOctets=_TnSapBaseStatsIngressForwardedOctets_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,1,1,4),_TnSapBaseStatsIngressForwardedOctets_Type())
tnSapBaseStatsIngressForwardedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapBaseStatsIngressForwardedOctets.setStatus(_A)
_TnSapBaseStatsEgressForwardedPackets_Type=Counter64
_TnSapBaseStatsEgressForwardedPackets_Object=MibTableColumn
tnSapBaseStatsEgressForwardedPackets=_TnSapBaseStatsEgressForwardedPackets_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,1,1,5),_TnSapBaseStatsEgressForwardedPackets_Type())
tnSapBaseStatsEgressForwardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapBaseStatsEgressForwardedPackets.setStatus(_A)
_TnSapBaseStatsEgressForwardedOctets_Type=Counter64
_TnSapBaseStatsEgressForwardedOctets_Object=MibTableColumn
tnSapBaseStatsEgressForwardedOctets=_TnSapBaseStatsEgressForwardedOctets_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,1,1,6),_TnSapBaseStatsEgressForwardedOctets_Type())
tnSapBaseStatsEgressForwardedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapBaseStatsEgressForwardedOctets.setStatus(_A)
_TnSapBaseStatsIngressExtraTagDroppedPackets_Type=Counter64
_TnSapBaseStatsIngressExtraTagDroppedPackets_Object=MibTableColumn
tnSapBaseStatsIngressExtraTagDroppedPackets=_TnSapBaseStatsIngressExtraTagDroppedPackets_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,1,1,7),_TnSapBaseStatsIngressExtraTagDroppedPackets_Type())
tnSapBaseStatsIngressExtraTagDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapBaseStatsIngressExtraTagDroppedPackets.setStatus(_A)
_TnSapBaseStatsIngressExtraTagDroppedOctets_Type=Counter64
_TnSapBaseStatsIngressExtraTagDroppedOctets_Object=MibTableColumn
tnSapBaseStatsIngressExtraTagDroppedOctets=_TnSapBaseStatsIngressExtraTagDroppedOctets_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,1,1,8),_TnSapBaseStatsIngressExtraTagDroppedOctets_Type())
tnSapBaseStatsIngressExtraTagDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapBaseStatsIngressExtraTagDroppedOctets.setStatus(_A)
_TnSapBaseStatsIngressDroppedPackets_Type=Counter64
_TnSapBaseStatsIngressDroppedPackets_Object=MibTableColumn
tnSapBaseStatsIngressDroppedPackets=_TnSapBaseStatsIngressDroppedPackets_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,1,1,9),_TnSapBaseStatsIngressDroppedPackets_Type())
tnSapBaseStatsIngressDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapBaseStatsIngressDroppedPackets.setStatus(_A)
_TnSapBaseStatsIngressDroppedOctets_Type=Counter64
_TnSapBaseStatsIngressDroppedOctets_Object=MibTableColumn
tnSapBaseStatsIngressDroppedOctets=_TnSapBaseStatsIngressDroppedOctets_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,1,1,10),_TnSapBaseStatsIngressDroppedOctets_Type())
tnSapBaseStatsIngressDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapBaseStatsIngressDroppedOctets.setStatus(_A)
_TnSapBaseInfoExtnTable_Object=MibTable
tnSapBaseInfoExtnTable=_TnSapBaseInfoExtnTable_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,2))
if mibBuilder.loadTexts:tnSapBaseInfoExtnTable.setStatus(_A)
_TnSapBaseInfoExtnEntry_Object=MibTableRow
tnSapBaseInfoExtnEntry=_TnSapBaseInfoExtnEntry_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,2,1))
if mibBuilder.loadTexts:tnSapBaseInfoExtnEntry.setStatus(_A)
class _TnSapBaseInfoEgressStatsPktsMode_Type(TruthValue):defaultValue=2
_TnSapBaseInfoEgressStatsPktsMode_Type.__name__=_D
_TnSapBaseInfoEgressStatsPktsMode_Object=MibTableColumn
tnSapBaseInfoEgressStatsPktsMode=_TnSapBaseInfoEgressStatsPktsMode_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,2,1,1),_TnSapBaseInfoEgressStatsPktsMode_Type())
tnSapBaseInfoEgressStatsPktsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseInfoEgressStatsPktsMode.setStatus(_A)
class _TnSapBaseInfoIngressCounterMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('packet',1),('octet',2)))
_TnSapBaseInfoIngressCounterMode_Type.__name__=_E
_TnSapBaseInfoIngressCounterMode_Object=MibTableColumn
tnSapBaseInfoIngressCounterMode=_TnSapBaseInfoIngressCounterMode_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,2,1,2),_TnSapBaseInfoIngressCounterMode_Type())
tnSapBaseInfoIngressCounterMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseInfoIngressCounterMode.setStatus(_A)
class _TnSapBaseInfoIngressAggregateMeterRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100000000))
_TnSapBaseInfoIngressAggregateMeterRate_Type.__name__=_E
_TnSapBaseInfoIngressAggregateMeterRate_Object=MibTableColumn
tnSapBaseInfoIngressAggregateMeterRate=_TnSapBaseInfoIngressAggregateMeterRate_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,2,1,3),_TnSapBaseInfoIngressAggregateMeterRate_Type())
tnSapBaseInfoIngressAggregateMeterRate.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseInfoIngressAggregateMeterRate.setStatus(_A)
class _TnSapBaseInfoIngressAggregateMeterBurst_Type(TSapIngressAggrMeterBurstSize):defaultValue=-1
_TnSapBaseInfoIngressAggregateMeterBurst_Type.__name__=_G
_TnSapBaseInfoIngressAggregateMeterBurst_Object=MibTableColumn
tnSapBaseInfoIngressAggregateMeterBurst=_TnSapBaseInfoIngressAggregateMeterBurst_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,2,1,4),_TnSapBaseInfoIngressAggregateMeterBurst_Type())
tnSapBaseInfoIngressAggregateMeterBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseInfoIngressAggregateMeterBurst.setStatus(_A)
class _TnSapBaseInfoIngressWithAggregateMeter_Type(TruthValue):defaultValue=2
_TnSapBaseInfoIngressWithAggregateMeter_Type.__name__=_D
_TnSapBaseInfoIngressWithAggregateMeter_Object=MibTableColumn
tnSapBaseInfoIngressWithAggregateMeter=_TnSapBaseInfoIngressWithAggregateMeter_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,2,1,5),_TnSapBaseInfoIngressWithAggregateMeter_Type())
tnSapBaseInfoIngressWithAggregateMeter.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseInfoIngressWithAggregateMeter.setStatus(_A)
class _TnSapBaseInfoIngressExtraTagDropCount_Type(TruthValue):defaultValue=2
_TnSapBaseInfoIngressExtraTagDropCount_Type.__name__=_D
_TnSapBaseInfoIngressExtraTagDropCount_Object=MibTableColumn
tnSapBaseInfoIngressExtraTagDropCount=_TnSapBaseInfoIngressExtraTagDropCount_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,2,1,6),_TnSapBaseInfoIngressExtraTagDropCount_Type())
tnSapBaseInfoIngressExtraTagDropCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseInfoIngressExtraTagDropCount.setStatus(_A)
class _TnSapBaseInfoEgressStatsEnable_Type(TruthValue):defaultValue=2
_TnSapBaseInfoEgressStatsEnable_Type.__name__=_D
_TnSapBaseInfoEgressStatsEnable_Object=MibTableColumn
tnSapBaseInfoEgressStatsEnable=_TnSapBaseInfoEgressStatsEnable_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,2,1,7),_TnSapBaseInfoEgressStatsEnable_Type())
tnSapBaseInfoEgressStatsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseInfoEgressStatsEnable.setStatus(_A)
class _TnSapBaseInfoIngressStatsEnable_Type(TruthValue):defaultValue=2
_TnSapBaseInfoIngressStatsEnable_Type.__name__=_D
_TnSapBaseInfoIngressStatsEnable_Object=MibTableColumn
tnSapBaseInfoIngressStatsEnable=_TnSapBaseInfoIngressStatsEnable_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,2,1,8),_TnSapBaseInfoIngressStatsEnable_Type())
tnSapBaseInfoIngressStatsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseInfoIngressStatsEnable.setStatus(_A)
class _TnSapBaseInfoIngressCounterType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in-out-profile-count',1),('forward-drop-count',2)))
_TnSapBaseInfoIngressCounterType_Type.__name__=_E
_TnSapBaseInfoIngressCounterType_Object=MibTableColumn
tnSapBaseInfoIngressCounterType=_TnSapBaseInfoIngressCounterType_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,2,1,9),_TnSapBaseInfoIngressCounterType_Type())
tnSapBaseInfoIngressCounterType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseInfoIngressCounterType.setStatus(_A)
class _TnSapBaseInfoEthRingShgEnable_Type(TruthValue):defaultValue=2
_TnSapBaseInfoEthRingShgEnable_Type.__name__=_D
_TnSapBaseInfoEthRingShgEnable_Object=MibTableColumn
tnSapBaseInfoEthRingShgEnable=_TnSapBaseInfoEthRingShgEnable_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,2,1,11),_TnSapBaseInfoEthRingShgEnable_Type())
tnSapBaseInfoEthRingShgEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseInfoEthRingShgEnable.setStatus(_A)
class _TnSapBaseInfoMacSwapEnable_Type(TruthValue):defaultValue=2
_TnSapBaseInfoMacSwapEnable_Type.__name__=_D
_TnSapBaseInfoMacSwapEnable_Object=MibTableColumn
tnSapBaseInfoMacSwapEnable=_TnSapBaseInfoMacSwapEnable_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,2,1,12),_TnSapBaseInfoMacSwapEnable_Type())
tnSapBaseInfoMacSwapEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:tnSapBaseInfoMacSwapEnable.setStatus(_A)
class _TnSapBaseInfoStatsCounterEnable_Type(TruthValue):defaultValue=1
_TnSapBaseInfoStatsCounterEnable_Type.__name__=_D
_TnSapBaseInfoStatsCounterEnable_Object=MibTableColumn
tnSapBaseInfoStatsCounterEnable=_TnSapBaseInfoStatsCounterEnable_Object((1,3,6,1,4,1,7483,7,2,2,2,8,1,2,1,13),_TnSapBaseInfoStatsCounterEnable_Type())
tnSapBaseInfoStatsCounterEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseInfoStatsCounterEnable.setStatus('deprecated')
_TnSASSvcObjs_ObjectIdentity=ObjectIdentity
tnSASSvcObjs=_TnSASSvcObjs_ObjectIdentity((1,3,6,1,4,1,7483,7,2,2,2,8,2))
_TnSvcBaseInfoExtnTable_Object=MibTable
tnSvcBaseInfoExtnTable=_TnSvcBaseInfoExtnTable_Object((1,3,6,1,4,1,7483,7,2,2,2,8,2,1))
if mibBuilder.loadTexts:tnSvcBaseInfoExtnTable.setStatus(_A)
_TnSvcBaseInfoExtnEntry_Object=MibTableRow
tnSvcBaseInfoExtnEntry=_TnSvcBaseInfoExtnEntry_Object((1,3,6,1,4,1,7483,7,2,2,2,8,2,1,1))
if mibBuilder.loadTexts:tnSvcBaseInfoExtnEntry.setStatus(_A)
class _TnSvcMtuCheck_Type(TruthValue):defaultValue=1
_TnSvcMtuCheck_Type.__name__=_D
_TnSvcMtuCheck_Object=MibTableColumn
tnSvcMtuCheck=_TnSvcMtuCheck_Object((1,3,6,1,4,1,7483,7,2,2,2,8,2,1,1,1),_TnSvcMtuCheck_Type())
tnSvcMtuCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcMtuCheck.setStatus(_A)
class _TnSvcSapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_H,0),('null-star',1),('dot1q',2),('dot1q-preserve',3),('any',4),('dot1q-range',5),('qinq-inner-tag-preserve',6)))
_TnSvcSapType_Type.__name__=_E
_TnSvcSapType_Object=MibTableColumn
tnSvcSapType=_TnSvcSapType_Object((1,3,6,1,4,1,7483,7,2,2,2,8,2,1,1,2),_TnSvcSapType_Type())
tnSvcSapType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcSapType.setStatus(_A)
class _TnSvcUplinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('l2',1),('mpls',2)))
_TnSvcUplinkType_Type.__name__=_E
_TnSvcUplinkType_Object=MibTableColumn
tnSvcUplinkType=_TnSvcUplinkType_Object((1,3,6,1,4,1,7483,7,2,2,2,8,2,1,1,3),_TnSvcUplinkType_Type())
tnSvcUplinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcUplinkType.setStatus(_A)
class _TnSvcCustomerVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_TnSvcCustomerVid_Type.__name__=_E
_TnSvcCustomerVid_Object=MibTableColumn
tnSvcCustomerVid=_TnSvcCustomerVid_Object((1,3,6,1,4,1,7483,7,2,2,2,8,2,1,1,4),_TnSvcCustomerVid_Type())
tnSvcCustomerVid.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcCustomerVid.setStatus(_A)
class _TnSvcEpipeType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('pbbepipe',2)))
_TnSvcEpipeType_Type.__name__=_E
_TnSvcEpipeType_Object=MibTableColumn
tnSvcEpipeType=_TnSvcEpipeType_Object((1,3,6,1,4,1,7483,7,2,2,2,8,2,1,1,5),_TnSvcEpipeType_Type())
tnSvcEpipeType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcEpipeType.setStatus(_A)
_TnSASSvcScalar1_Type=Unsigned32
_TnSASSvcScalar1_Object=MibScalar
tnSASSvcScalar1=_TnSASSvcScalar1_Object((1,3,6,1,4,1,7483,7,2,2,2,8,2,101),_TnSASSvcScalar1_Type())
tnSASSvcScalar1.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSASSvcScalar1.setStatus(_A)
_TnSASSvcScalar2_Type=Unsigned32
_TnSASSvcScalar2_Object=MibScalar
tnSASSvcScalar2=_TnSASSvcScalar2_Object((1,3,6,1,4,1,7483,7,2,2,2,8,2,102),_TnSASSvcScalar2_Type())
tnSASSvcScalar2.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSASSvcScalar2.setStatus(_A)
tnSapBaseStatsEntry.registerAugmentions((_F,_I))
tnSapBaseStatsExtnEntry.setIndexNames(*tnSapBaseStatsEntry.getIndexNames())
tnSapBaseInfoEntry.registerAugmentions((_F,_J))
tnSapBaseInfoExtnEntry.setIndexNames(*tnSapBaseInfoEntry.getIndexNames())
tnSvcBaseInfoEntry.registerAugmentions((_F,_K))
tnSvcBaseInfoExtnEntry.setIndexNames(*tnSvcBaseInfoEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{_G:TSapIngressAggrMeterBurstSize,'tnSASServicesMIBModule':tnSASServicesMIBModule,'tnSASServObjs':tnSASServObjs,'tnSASSapObjs':tnSASSapObjs,'tnSapBaseStatsExtnTable':tnSapBaseStatsExtnTable,_I:tnSapBaseStatsExtnEntry,'tnSapBaseStatsQosClassifiersUsed':tnSapBaseStatsQosClassifiersUsed,'tnSapBaseStatsQosMetersUsed':tnSapBaseStatsQosMetersUsed,'tnSapBaseStatsIngressForwardedPackets':tnSapBaseStatsIngressForwardedPackets,'tnSapBaseStatsIngressForwardedOctets':tnSapBaseStatsIngressForwardedOctets,'tnSapBaseStatsEgressForwardedPackets':tnSapBaseStatsEgressForwardedPackets,'tnSapBaseStatsEgressForwardedOctets':tnSapBaseStatsEgressForwardedOctets,'tnSapBaseStatsIngressExtraTagDroppedPackets':tnSapBaseStatsIngressExtraTagDroppedPackets,'tnSapBaseStatsIngressExtraTagDroppedOctets':tnSapBaseStatsIngressExtraTagDroppedOctets,'tnSapBaseStatsIngressDroppedPackets':tnSapBaseStatsIngressDroppedPackets,'tnSapBaseStatsIngressDroppedOctets':tnSapBaseStatsIngressDroppedOctets,'tnSapBaseInfoExtnTable':tnSapBaseInfoExtnTable,_J:tnSapBaseInfoExtnEntry,'tnSapBaseInfoEgressStatsPktsMode':tnSapBaseInfoEgressStatsPktsMode,'tnSapBaseInfoIngressCounterMode':tnSapBaseInfoIngressCounterMode,'tnSapBaseInfoIngressAggregateMeterRate':tnSapBaseInfoIngressAggregateMeterRate,'tnSapBaseInfoIngressAggregateMeterBurst':tnSapBaseInfoIngressAggregateMeterBurst,'tnSapBaseInfoIngressWithAggregateMeter':tnSapBaseInfoIngressWithAggregateMeter,'tnSapBaseInfoIngressExtraTagDropCount':tnSapBaseInfoIngressExtraTagDropCount,'tnSapBaseInfoEgressStatsEnable':tnSapBaseInfoEgressStatsEnable,'tnSapBaseInfoIngressStatsEnable':tnSapBaseInfoIngressStatsEnable,'tnSapBaseInfoIngressCounterType':tnSapBaseInfoIngressCounterType,'tnSapBaseInfoEthRingShgEnable':tnSapBaseInfoEthRingShgEnable,'tnSapBaseInfoMacSwapEnable':tnSapBaseInfoMacSwapEnable,'tnSapBaseInfoStatsCounterEnable':tnSapBaseInfoStatsCounterEnable,'tnSASSvcObjs':tnSASSvcObjs,'tnSvcBaseInfoExtnTable':tnSvcBaseInfoExtnTable,_K:tnSvcBaseInfoExtnEntry,'tnSvcMtuCheck':tnSvcMtuCheck,'tnSvcSapType':tnSvcSapType,'tnSvcUplinkType':tnSvcUplinkType,'tnSvcCustomerVid':tnSvcCustomerVid,'tnSvcEpipeType':tnSvcEpipeType,'tnSASSvcScalar1':tnSASSvcScalar1,'tnSASSvcScalar2':tnSASSvcScalar2})