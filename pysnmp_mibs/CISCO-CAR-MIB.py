_h='ciscoCarMIBHCGroup'
_g='ccarStatHCFilteredBytes'
_f='ccarStatHCFilteredPkts'
_e='ccarStatHCSwitchedBytes'
_d='ccarStatHCSwitchedPkts'
_c='ccarStatFilteredBytesOverflow'
_b='ccarStatFilteredPktsOverflow'
_a='ccarStatSwitchedBytesOverflow'
_Z='ccarStatSwitchedPktsOverflow'
_Y='ccarStatCurBurst'
_X='ccarStatFilteredBytes'
_W='ccarStatFilteredPkts'
_V='ccarStatSwitchedBytes'
_U='ccarStatSwitchedPkts'
_T='ccarConfigExceedAction'
_S='ccarConfigConformAction'
_R='ccarConfigExtLimit'
_Q='ccarConfigLimit'
_P='ccarConfigRate'
_O='ccarConfigAccIdx'
_N='ccarConfigType'
_M='ccarStatEntry'
_L='not-accessible'
_K='ccarConfigRowIndex'
_J='ccarConfigDirection'
_I='Integer32'
_H='ifIndex'
_G='IF-MIB'
_F='ciscoCarMIBGroup'
_E='packets'
_D='bytes'
_C='read-only'
_B='CISCO-CAR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoCarMIB=ModuleIdentity((1,3,6,1,4,1,9,9,113))
if mibBuilder.loadTexts:ciscoCarMIB.setRevisions(('1997-07-18 00:00','1900-02-18 00:00'))
class PacketSource(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('input',1),('output',2)))
class RateLimitType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('quickAcc',2),('standardAcc',3)))
class RateLimitAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('drop',1),('xmit',2),('continue',3),('precedXmit',4),('precedCont',5)))
_CiscoCarMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCarMIBObjects=_CiscoCarMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,113,1))
_CcarConfigs_ObjectIdentity=ObjectIdentity
ccarConfigs=_CcarConfigs_ObjectIdentity((1,3,6,1,4,1,9,9,113,1,1))
_CcarConfigTable_Object=MibTable
ccarConfigTable=_CcarConfigTable_Object((1,3,6,1,4,1,9,9,113,1,1,1))
if mibBuilder.loadTexts:ccarConfigTable.setStatus(_A)
_CcarConfigEntry_Object=MibTableRow
ccarConfigEntry=_CcarConfigEntry_Object((1,3,6,1,4,1,9,9,113,1,1,1,1))
ccarConfigEntry.setIndexNames((0,_G,_H),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:ccarConfigEntry.setStatus(_A)
_CcarConfigDirection_Type=PacketSource
_CcarConfigDirection_Object=MibTableColumn
ccarConfigDirection=_CcarConfigDirection_Object((1,3,6,1,4,1,9,9,113,1,1,1,1,1),_CcarConfigDirection_Type())
ccarConfigDirection.setMaxAccess(_L)
if mibBuilder.loadTexts:ccarConfigDirection.setStatus(_A)
class _CcarConfigRowIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CcarConfigRowIndex_Type.__name__=_I
_CcarConfigRowIndex_Object=MibTableColumn
ccarConfigRowIndex=_CcarConfigRowIndex_Object((1,3,6,1,4,1,9,9,113,1,1,1,1,2),_CcarConfigRowIndex_Type())
ccarConfigRowIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:ccarConfigRowIndex.setStatus(_A)
_CcarConfigType_Type=RateLimitType
_CcarConfigType_Object=MibTableColumn
ccarConfigType=_CcarConfigType_Object((1,3,6,1,4,1,9,9,113,1,1,1,1,3),_CcarConfigType_Type())
ccarConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarConfigType.setStatus(_A)
_CcarConfigAccIdx_Type=Integer32
_CcarConfigAccIdx_Object=MibTableColumn
ccarConfigAccIdx=_CcarConfigAccIdx_Object((1,3,6,1,4,1,9,9,113,1,1,1,1,4),_CcarConfigAccIdx_Type())
ccarConfigAccIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarConfigAccIdx.setStatus(_A)
_CcarConfigRate_Type=Integer32
_CcarConfigRate_Object=MibTableColumn
ccarConfigRate=_CcarConfigRate_Object((1,3,6,1,4,1,9,9,113,1,1,1,1,5),_CcarConfigRate_Type())
ccarConfigRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarConfigRate.setStatus(_A)
if mibBuilder.loadTexts:ccarConfigRate.setUnits('bits/second')
_CcarConfigLimit_Type=Integer32
_CcarConfigLimit_Object=MibTableColumn
ccarConfigLimit=_CcarConfigLimit_Object((1,3,6,1,4,1,9,9,113,1,1,1,1,6),_CcarConfigLimit_Type())
ccarConfigLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarConfigLimit.setStatus(_A)
if mibBuilder.loadTexts:ccarConfigLimit.setUnits(_D)
_CcarConfigExtLimit_Type=Integer32
_CcarConfigExtLimit_Object=MibTableColumn
ccarConfigExtLimit=_CcarConfigExtLimit_Object((1,3,6,1,4,1,9,9,113,1,1,1,1,7),_CcarConfigExtLimit_Type())
ccarConfigExtLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarConfigExtLimit.setStatus(_A)
if mibBuilder.loadTexts:ccarConfigExtLimit.setUnits(_D)
_CcarConfigConformAction_Type=RateLimitAction
_CcarConfigConformAction_Object=MibTableColumn
ccarConfigConformAction=_CcarConfigConformAction_Object((1,3,6,1,4,1,9,9,113,1,1,1,1,8),_CcarConfigConformAction_Type())
ccarConfigConformAction.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarConfigConformAction.setStatus(_A)
_CcarConfigExceedAction_Type=RateLimitAction
_CcarConfigExceedAction_Object=MibTableColumn
ccarConfigExceedAction=_CcarConfigExceedAction_Object((1,3,6,1,4,1,9,9,113,1,1,1,1,9),_CcarConfigExceedAction_Type())
ccarConfigExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarConfigExceedAction.setStatus(_A)
_CcarStats_ObjectIdentity=ObjectIdentity
ccarStats=_CcarStats_ObjectIdentity((1,3,6,1,4,1,9,9,113,1,2))
_CcarStatTable_Object=MibTable
ccarStatTable=_CcarStatTable_Object((1,3,6,1,4,1,9,9,113,1,2,1))
if mibBuilder.loadTexts:ccarStatTable.setStatus(_A)
_CcarStatEntry_Object=MibTableRow
ccarStatEntry=_CcarStatEntry_Object((1,3,6,1,4,1,9,9,113,1,2,1,1))
if mibBuilder.loadTexts:ccarStatEntry.setStatus(_A)
_CcarStatSwitchedPkts_Type=Counter32
_CcarStatSwitchedPkts_Object=MibTableColumn
ccarStatSwitchedPkts=_CcarStatSwitchedPkts_Object((1,3,6,1,4,1,9,9,113,1,2,1,1,1),_CcarStatSwitchedPkts_Type())
ccarStatSwitchedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarStatSwitchedPkts.setStatus(_A)
if mibBuilder.loadTexts:ccarStatSwitchedPkts.setUnits(_E)
_CcarStatSwitchedBytes_Type=Counter32
_CcarStatSwitchedBytes_Object=MibTableColumn
ccarStatSwitchedBytes=_CcarStatSwitchedBytes_Object((1,3,6,1,4,1,9,9,113,1,2,1,1,2),_CcarStatSwitchedBytes_Type())
ccarStatSwitchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarStatSwitchedBytes.setStatus(_A)
if mibBuilder.loadTexts:ccarStatSwitchedBytes.setUnits(_D)
_CcarStatFilteredPkts_Type=Counter32
_CcarStatFilteredPkts_Object=MibTableColumn
ccarStatFilteredPkts=_CcarStatFilteredPkts_Object((1,3,6,1,4,1,9,9,113,1,2,1,1,3),_CcarStatFilteredPkts_Type())
ccarStatFilteredPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarStatFilteredPkts.setStatus(_A)
if mibBuilder.loadTexts:ccarStatFilteredPkts.setUnits(_E)
_CcarStatFilteredBytes_Type=Counter32
_CcarStatFilteredBytes_Object=MibTableColumn
ccarStatFilteredBytes=_CcarStatFilteredBytes_Object((1,3,6,1,4,1,9,9,113,1,2,1,1,4),_CcarStatFilteredBytes_Type())
ccarStatFilteredBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarStatFilteredBytes.setStatus(_A)
if mibBuilder.loadTexts:ccarStatFilteredBytes.setUnits(_D)
_CcarStatCurBurst_Type=Gauge32
_CcarStatCurBurst_Object=MibTableColumn
ccarStatCurBurst=_CcarStatCurBurst_Object((1,3,6,1,4,1,9,9,113,1,2,1,1,5),_CcarStatCurBurst_Type())
ccarStatCurBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarStatCurBurst.setStatus(_A)
if mibBuilder.loadTexts:ccarStatCurBurst.setUnits(_D)
_CcarStatSwitchedPktsOverflow_Type=Counter32
_CcarStatSwitchedPktsOverflow_Object=MibTableColumn
ccarStatSwitchedPktsOverflow=_CcarStatSwitchedPktsOverflow_Object((1,3,6,1,4,1,9,9,113,1,2,1,1,6),_CcarStatSwitchedPktsOverflow_Type())
ccarStatSwitchedPktsOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarStatSwitchedPktsOverflow.setStatus(_A)
if mibBuilder.loadTexts:ccarStatSwitchedPktsOverflow.setUnits(_E)
_CcarStatSwitchedBytesOverflow_Type=Counter32
_CcarStatSwitchedBytesOverflow_Object=MibTableColumn
ccarStatSwitchedBytesOverflow=_CcarStatSwitchedBytesOverflow_Object((1,3,6,1,4,1,9,9,113,1,2,1,1,7),_CcarStatSwitchedBytesOverflow_Type())
ccarStatSwitchedBytesOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarStatSwitchedBytesOverflow.setStatus(_A)
if mibBuilder.loadTexts:ccarStatSwitchedBytesOverflow.setUnits(_D)
_CcarStatFilteredPktsOverflow_Type=Counter32
_CcarStatFilteredPktsOverflow_Object=MibTableColumn
ccarStatFilteredPktsOverflow=_CcarStatFilteredPktsOverflow_Object((1,3,6,1,4,1,9,9,113,1,2,1,1,8),_CcarStatFilteredPktsOverflow_Type())
ccarStatFilteredPktsOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarStatFilteredPktsOverflow.setStatus(_A)
if mibBuilder.loadTexts:ccarStatFilteredPktsOverflow.setUnits(_E)
_CcarStatFilteredBytesOverflow_Type=Counter32
_CcarStatFilteredBytesOverflow_Object=MibTableColumn
ccarStatFilteredBytesOverflow=_CcarStatFilteredBytesOverflow_Object((1,3,6,1,4,1,9,9,113,1,2,1,1,9),_CcarStatFilteredBytesOverflow_Type())
ccarStatFilteredBytesOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarStatFilteredBytesOverflow.setStatus(_A)
if mibBuilder.loadTexts:ccarStatFilteredBytesOverflow.setUnits(_D)
_CcarStatHCSwitchedPkts_Type=Counter64
_CcarStatHCSwitchedPkts_Object=MibTableColumn
ccarStatHCSwitchedPkts=_CcarStatHCSwitchedPkts_Object((1,3,6,1,4,1,9,9,113,1,2,1,1,10),_CcarStatHCSwitchedPkts_Type())
ccarStatHCSwitchedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarStatHCSwitchedPkts.setStatus(_A)
if mibBuilder.loadTexts:ccarStatHCSwitchedPkts.setUnits(_E)
_CcarStatHCSwitchedBytes_Type=Counter64
_CcarStatHCSwitchedBytes_Object=MibTableColumn
ccarStatHCSwitchedBytes=_CcarStatHCSwitchedBytes_Object((1,3,6,1,4,1,9,9,113,1,2,1,1,11),_CcarStatHCSwitchedBytes_Type())
ccarStatHCSwitchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarStatHCSwitchedBytes.setStatus(_A)
if mibBuilder.loadTexts:ccarStatHCSwitchedBytes.setUnits(_D)
_CcarStatHCFilteredPkts_Type=Counter64
_CcarStatHCFilteredPkts_Object=MibTableColumn
ccarStatHCFilteredPkts=_CcarStatHCFilteredPkts_Object((1,3,6,1,4,1,9,9,113,1,2,1,1,12),_CcarStatHCFilteredPkts_Type())
ccarStatHCFilteredPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarStatHCFilteredPkts.setStatus(_A)
if mibBuilder.loadTexts:ccarStatHCFilteredPkts.setUnits(_E)
_CcarStatHCFilteredBytes_Type=Counter64
_CcarStatHCFilteredBytes_Object=MibTableColumn
ccarStatHCFilteredBytes=_CcarStatHCFilteredBytes_Object((1,3,6,1,4,1,9,9,113,1,2,1,1,13),_CcarStatHCFilteredBytes_Type())
ccarStatHCFilteredBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ccarStatHCFilteredBytes.setStatus(_A)
if mibBuilder.loadTexts:ccarStatHCFilteredBytes.setUnits(_D)
_CiscoCarMIBConformance_ObjectIdentity=ObjectIdentity
ciscoCarMIBConformance=_CiscoCarMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,113,3))
_CiscoCarMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCarMIBCompliances=_CiscoCarMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,113,3,1))
_CiscoCarMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCarMIBGroups=_CiscoCarMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,113,3,2))
ccarConfigEntry.registerAugmentions((_B,_M))
ccarStatEntry.setIndexNames(*ccarConfigEntry.getIndexNames())
ciscoCarMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,113,3,2,1))
ciscoCarMIBGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ciscoCarMIBGroup.setStatus(_A)
ciscoCarMIBHCGroup=ObjectGroup((1,3,6,1,4,1,9,9,113,3,2,2))
ciscoCarMIBHCGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ciscoCarMIBHCGroup.setStatus(_A)
ciscoCarMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,113,3,1,1))
ciscoCarMIBCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:ciscoCarMIBCompliance.setStatus(_A)
ciscoCarMIBComplianceHCCounters=ModuleCompliance((1,3,6,1,4,1,9,9,113,3,1,2))
ciscoCarMIBComplianceHCCounters.setObjects(*((_B,_F),(_B,_h)))
if mibBuilder.loadTexts:ciscoCarMIBComplianceHCCounters.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PacketSource':PacketSource,'RateLimitType':RateLimitType,'RateLimitAction':RateLimitAction,'ciscoCarMIB':ciscoCarMIB,'ciscoCarMIBObjects':ciscoCarMIBObjects,'ccarConfigs':ccarConfigs,'ccarConfigTable':ccarConfigTable,'ccarConfigEntry':ccarConfigEntry,_J:ccarConfigDirection,_K:ccarConfigRowIndex,_N:ccarConfigType,_O:ccarConfigAccIdx,_P:ccarConfigRate,_Q:ccarConfigLimit,_R:ccarConfigExtLimit,_S:ccarConfigConformAction,_T:ccarConfigExceedAction,'ccarStats':ccarStats,'ccarStatTable':ccarStatTable,_M:ccarStatEntry,_U:ccarStatSwitchedPkts,_V:ccarStatSwitchedBytes,_W:ccarStatFilteredPkts,_X:ccarStatFilteredBytes,_Y:ccarStatCurBurst,_Z:ccarStatSwitchedPktsOverflow,_a:ccarStatSwitchedBytesOverflow,_b:ccarStatFilteredPktsOverflow,_c:ccarStatFilteredBytesOverflow,_d:ccarStatHCSwitchedPkts,_e:ccarStatHCSwitchedBytes,_f:ccarStatHCFilteredPkts,_g:ccarStatHCFilteredBytes,'ciscoCarMIBConformance':ciscoCarMIBConformance,'ciscoCarMIBCompliances':ciscoCarMIBCompliances,'ciscoCarMIBCompliance':ciscoCarMIBCompliance,'ciscoCarMIBComplianceHCCounters':ciscoCarMIBComplianceHCCounters,'ciscoCarMIBGroups':ciscoCarMIBGroups,_F:ciscoCarMIBGroup,_h:ciscoCarMIBHCGroup})