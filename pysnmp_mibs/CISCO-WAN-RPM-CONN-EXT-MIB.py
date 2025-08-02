_S='ciscoWanRpmConnExtMIBGroup'
_R='cwrChanOamRetryInterval'
_Q='cwrChanOamRetryDownCount'
_P='cwrChanOamRetryUpCount'
_O='cwrChanOamManage'
_N='cwrChanOamLoopbkTxInterval'
_M='cwrChanInArpInterval'
_L='cwrChanVirtualTemplate'
_K='cwrChanAalEncapType'
_J='cwrChanVcd'
_I='cwrChanSubInterface'
_H='cwRpmChanExtEntry'
_G='seconds'
_F='TruthValue'
_E='Integer32'
_D='read-create'
_C='Unsigned32'
_B='CISCO-WAN-RPM-CONN-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cwAtmChanCnfgEntry,=mibBuilder.importSymbols('CISCO-WAN-ATM-CONN-MIB','cwAtmChanCnfgEntry')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
ciscoWanRpmConnExtMIB=ModuleIdentity((1,3,6,1,4,1,351,150,9))
if mibBuilder.loadTexts:ciscoWanRpmConnExtMIB.setRevisions(('2002-05-21 00:00','2002-03-18 00:00','1999-09-30 00:00'))
_CwRpmConnExtMIBObjects_ObjectIdentity=ObjectIdentity
cwRpmConnExtMIBObjects=_CwRpmConnExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,351,150,9,1))
_CwRpmConnExt_ObjectIdentity=ObjectIdentity
cwRpmConnExt=_CwRpmConnExt_ObjectIdentity((1,3,6,1,4,1,351,150,9,1,1))
_CwRpmChanExtTable_Object=MibTable
cwRpmChanExtTable=_CwRpmChanExtTable_Object((1,3,6,1,4,1,351,150,9,1,1,1))
if mibBuilder.loadTexts:cwRpmChanExtTable.setStatus(_A)
_CwRpmChanExtEntry_Object=MibTableRow
cwRpmChanExtEntry=_CwRpmChanExtEntry_Object((1,3,6,1,4,1,351,150,9,1,1,1,1))
if mibBuilder.loadTexts:cwRpmChanExtEntry.setStatus(_A)
class _CwrChanSubInterface_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwrChanSubInterface_Type.__name__=_C
_CwrChanSubInterface_Object=MibTableColumn
cwrChanSubInterface=_CwrChanSubInterface_Object((1,3,6,1,4,1,351,150,9,1,1,1,1,1),_CwrChanSubInterface_Type())
cwrChanSubInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:cwrChanSubInterface.setStatus(_A)
class _CwrChanVcd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CwrChanVcd_Type.__name__=_C
_CwrChanVcd_Object=MibTableColumn
cwrChanVcd=_CwrChanVcd_Object((1,3,6,1,4,1,351,150,9,1,1,1,1,2),_CwrChanVcd_Type())
cwrChanVcd.setMaxAccess('read-only')
if mibBuilder.loadTexts:cwrChanVcd.setStatus(_A)
class _CwrChanAalEncapType_Type(Integer32):defaultValue=11;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('aal5ciscoPPP',1),('aal5muxAPOLLO',2),('aal5muxAPPLETALK',3),('aal5muxDECNET',4),('aal5muxIP',5),('aal5muxIPX',6),('aal5muxPPP',7),('aal5muxVINES',8),('aal5muxXNS',9),('aal5nlpid',10),('aal5snap',11),('ilmi',12),('qsaal',13)))
_CwrChanAalEncapType_Type.__name__=_E
_CwrChanAalEncapType_Object=MibTableColumn
cwrChanAalEncapType=_CwrChanAalEncapType_Object((1,3,6,1,4,1,351,150,9,1,1,1,1,3),_CwrChanAalEncapType_Type())
cwrChanAalEncapType.setMaxAccess(_D)
if mibBuilder.loadTexts:cwrChanAalEncapType.setStatus(_A)
class _CwrChanVirtualTemplate_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_CwrChanVirtualTemplate_Type.__name__=_C
_CwrChanVirtualTemplate_Object=MibTableColumn
cwrChanVirtualTemplate=_CwrChanVirtualTemplate_Object((1,3,6,1,4,1,351,150,9,1,1,1,1,4),_CwrChanVirtualTemplate_Type())
cwrChanVirtualTemplate.setMaxAccess(_D)
if mibBuilder.loadTexts:cwrChanVirtualTemplate.setStatus(_A)
class _CwrChanInArpInterval_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_CwrChanInArpInterval_Type.__name__=_C
_CwrChanInArpInterval_Object=MibTableColumn
cwrChanInArpInterval=_CwrChanInArpInterval_Object((1,3,6,1,4,1,351,150,9,1,1,1,1,5),_CwrChanInArpInterval_Type())
cwrChanInArpInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cwrChanInArpInterval.setStatus(_A)
if mibBuilder.loadTexts:cwrChanInArpInterval.setUnits('minutes')
class _CwrChanOamLoopbkTxInterval_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_CwrChanOamLoopbkTxInterval_Type.__name__=_C
_CwrChanOamLoopbkTxInterval_Object=MibTableColumn
cwrChanOamLoopbkTxInterval=_CwrChanOamLoopbkTxInterval_Object((1,3,6,1,4,1,351,150,9,1,1,1,1,6),_CwrChanOamLoopbkTxInterval_Type())
cwrChanOamLoopbkTxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cwrChanOamLoopbkTxInterval.setStatus(_A)
if mibBuilder.loadTexts:cwrChanOamLoopbkTxInterval.setUnits(_G)
class _CwrChanOamManage_Type(TruthValue):defaultValue=2
_CwrChanOamManage_Type.__name__=_F
_CwrChanOamManage_Object=MibTableColumn
cwrChanOamManage=_CwrChanOamManage_Object((1,3,6,1,4,1,351,150,9,1,1,1,1,7),_CwrChanOamManage_Type())
cwrChanOamManage.setMaxAccess(_D)
if mibBuilder.loadTexts:cwrChanOamManage.setStatus(_A)
class _CwrChanOamRetryUpCount_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_CwrChanOamRetryUpCount_Type.__name__=_C
_CwrChanOamRetryUpCount_Object=MibTableColumn
cwrChanOamRetryUpCount=_CwrChanOamRetryUpCount_Object((1,3,6,1,4,1,351,150,9,1,1,1,1,8),_CwrChanOamRetryUpCount_Type())
cwrChanOamRetryUpCount.setMaxAccess(_D)
if mibBuilder.loadTexts:cwrChanOamRetryUpCount.setStatus(_A)
class _CwrChanOamRetryDownCount_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_CwrChanOamRetryDownCount_Type.__name__=_C
_CwrChanOamRetryDownCount_Object=MibTableColumn
cwrChanOamRetryDownCount=_CwrChanOamRetryDownCount_Object((1,3,6,1,4,1,351,150,9,1,1,1,1,9),_CwrChanOamRetryDownCount_Type())
cwrChanOamRetryDownCount.setMaxAccess(_D)
if mibBuilder.loadTexts:cwrChanOamRetryDownCount.setStatus(_A)
class _CwrChanOamRetryInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CwrChanOamRetryInterval_Type.__name__=_C
_CwrChanOamRetryInterval_Object=MibTableColumn
cwrChanOamRetryInterval=_CwrChanOamRetryInterval_Object((1,3,6,1,4,1,351,150,9,1,1,1,1,10),_CwrChanOamRetryInterval_Type())
cwrChanOamRetryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cwrChanOamRetryInterval.setStatus(_A)
if mibBuilder.loadTexts:cwrChanOamRetryInterval.setUnits(_G)
_CiscoWanRpmConnExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoWanRpmConnExtMIBConformance=_CiscoWanRpmConnExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,9,2))
_CiscoWanRpmConnExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWanRpmConnExtMIBCompliances=_CiscoWanRpmConnExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,9,2,1))
_CiscoWanRpmConnExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWanRpmConnExtMIBGroups=_CiscoWanRpmConnExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,9,2,2))
cwAtmChanCnfgEntry.registerAugmentions((_B,_H))
cwRpmChanExtEntry.setIndexNames(*cwAtmChanCnfgEntry.getIndexNames())
ciscoWanRpmConnExtMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,9,2,2,1))
ciscoWanRpmConnExtMIBGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ciscoWanRpmConnExtMIBGroup.setStatus(_A)
ciscoWanRpmConnExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,9,2,1,1))
ciscoWanRpmConnExtMIBCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:ciscoWanRpmConnExtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWanRpmConnExtMIB':ciscoWanRpmConnExtMIB,'cwRpmConnExtMIBObjects':cwRpmConnExtMIBObjects,'cwRpmConnExt':cwRpmConnExt,'cwRpmChanExtTable':cwRpmChanExtTable,_H:cwRpmChanExtEntry,_I:cwrChanSubInterface,_J:cwrChanVcd,_K:cwrChanAalEncapType,_L:cwrChanVirtualTemplate,_M:cwrChanInArpInterval,_N:cwrChanOamLoopbkTxInterval,_O:cwrChanOamManage,_P:cwrChanOamRetryUpCount,_Q:cwrChanOamRetryDownCount,_R:cwrChanOamRetryInterval,'ciscoWanRpmConnExtMIBConformance':ciscoWanRpmConnExtMIBConformance,'ciscoWanRpmConnExtMIBCompliances':ciscoWanRpmConnExtMIBCompliances,'ciscoWanRpmConnExtMIBCompliance':ciscoWanRpmConnExtMIBCompliance,'ciscoWanRpmConnExtMIBGroups':ciscoWanRpmConnExtMIBGroups,_S:ciscoWanRpmConnExtMIBGroup})