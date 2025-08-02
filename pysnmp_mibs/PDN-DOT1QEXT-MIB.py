_Z='pdnDot1dVlanStackingGroup'
_Y='pdnDot1GeneralGroup'
_X='pdnDot1BasePortPIWGGroup'
_W='pdnDot1qVlanExtGroup'
_V='pdnDot1qVlanStaticOuterEthertype'
_U='pdnDot1qVlanStaticOuterDefaultPriority'
_T='pdnDot1qVlanStaticOuterTag'
_S='pdnDot1TpFdbClear'
_R='pdnDot1BasePortPIWGCircuit'
_Q='pdnDot1BasePortPIWGId'
_P='pdnDot1qVlanStaticDefaultNHR'
_O='pdnDot1qVlanStaticUplink'
_N='pdnDot1qVlanStaticProxyArpStatus'
_M='pdnDot1qVlanStaticSecureModeStatus'
_L='pdnDot1qVlanStaticExtEntry'
_K='read-only'
_J='pdnDot1BasePort'
_I='disable'
_H='enable'
_G='ifIndex'
_F='IF-MIB'
_E='Unsigned32'
_D='Integer32'
_C='read-write'
_B='PDN-DOT1QEXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
pdn_dot1q,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-dot1q')
TblCmd,=mibBuilder.importSymbols('PDN-TC','TblCmd')
dot1qVlanStaticEntry,=mibBuilder.importSymbols('Q-BRIDGE-MIB','dot1qVlanStaticEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnDot1qExt=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,39,1))
if mibBuilder.loadTexts:pdnDot1qExt.setRevisions(('2005-07-26 00:00','2003-11-12 00:00','2002-11-30 00:00'))
_PdnDot1qExtObjects_ObjectIdentity=ObjectIdentity
pdnDot1qExtObjects=_PdnDot1qExtObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,39,1,1))
_PdnDot1qVlanStaticExtTable_Object=MibTable
pdnDot1qVlanStaticExtTable=_PdnDot1qVlanStaticExtTable_Object((1,3,6,1,4,1,1795,2,24,2,39,1,1,1))
if mibBuilder.loadTexts:pdnDot1qVlanStaticExtTable.setStatus(_A)
_PdnDot1qVlanStaticExtEntry_Object=MibTableRow
pdnDot1qVlanStaticExtEntry=_PdnDot1qVlanStaticExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,39,1,1,1,1))
if mibBuilder.loadTexts:pdnDot1qVlanStaticExtEntry.setStatus(_A)
class _PdnDot1qVlanStaticSecureModeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_PdnDot1qVlanStaticSecureModeStatus_Type.__name__=_D
_PdnDot1qVlanStaticSecureModeStatus_Object=MibTableColumn
pdnDot1qVlanStaticSecureModeStatus=_PdnDot1qVlanStaticSecureModeStatus_Object((1,3,6,1,4,1,1795,2,24,2,39,1,1,1,1,1),_PdnDot1qVlanStaticSecureModeStatus_Type())
pdnDot1qVlanStaticSecureModeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDot1qVlanStaticSecureModeStatus.setStatus(_A)
class _PdnDot1qVlanStaticProxyArpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_PdnDot1qVlanStaticProxyArpStatus_Type.__name__=_D
_PdnDot1qVlanStaticProxyArpStatus_Object=MibTableColumn
pdnDot1qVlanStaticProxyArpStatus=_PdnDot1qVlanStaticProxyArpStatus_Object((1,3,6,1,4,1,1795,2,24,2,39,1,1,1,1,2),_PdnDot1qVlanStaticProxyArpStatus_Type())
pdnDot1qVlanStaticProxyArpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDot1qVlanStaticProxyArpStatus.setStatus(_A)
_PdnDot1qVlanStaticUplink_Type=Integer32
_PdnDot1qVlanStaticUplink_Object=MibTableColumn
pdnDot1qVlanStaticUplink=_PdnDot1qVlanStaticUplink_Object((1,3,6,1,4,1,1795,2,24,2,39,1,1,1,1,3),_PdnDot1qVlanStaticUplink_Type())
pdnDot1qVlanStaticUplink.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDot1qVlanStaticUplink.setStatus(_A)
_PdnDot1qVlanStaticDefaultNHR_Type=IpAddress
_PdnDot1qVlanStaticDefaultNHR_Object=MibTableColumn
pdnDot1qVlanStaticDefaultNHR=_PdnDot1qVlanStaticDefaultNHR_Object((1,3,6,1,4,1,1795,2,24,2,39,1,1,1,1,4),_PdnDot1qVlanStaticDefaultNHR_Type())
pdnDot1qVlanStaticDefaultNHR.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDot1qVlanStaticDefaultNHR.setStatus(_A)
class _PdnDot1qVlanStaticOuterTag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_PdnDot1qVlanStaticOuterTag_Type.__name__=_D
_PdnDot1qVlanStaticOuterTag_Object=MibTableColumn
pdnDot1qVlanStaticOuterTag=_PdnDot1qVlanStaticOuterTag_Object((1,3,6,1,4,1,1795,2,24,2,39,1,1,1,1,5),_PdnDot1qVlanStaticOuterTag_Type())
pdnDot1qVlanStaticOuterTag.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDot1qVlanStaticOuterTag.setStatus(_A)
class _PdnDot1qVlanStaticOuterDefaultPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PdnDot1qVlanStaticOuterDefaultPriority_Type.__name__=_D
_PdnDot1qVlanStaticOuterDefaultPriority_Object=MibTableColumn
pdnDot1qVlanStaticOuterDefaultPriority=_PdnDot1qVlanStaticOuterDefaultPriority_Object((1,3,6,1,4,1,1795,2,24,2,39,1,1,1,1,6),_PdnDot1qVlanStaticOuterDefaultPriority_Type())
pdnDot1qVlanStaticOuterDefaultPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDot1qVlanStaticOuterDefaultPriority.setStatus(_A)
class _PdnDot1qVlanStaticOuterEthertype_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PdnDot1qVlanStaticOuterEthertype_Type.__name__=_D
_PdnDot1qVlanStaticOuterEthertype_Object=MibTableColumn
pdnDot1qVlanStaticOuterEthertype=_PdnDot1qVlanStaticOuterEthertype_Object((1,3,6,1,4,1,1795,2,24,2,39,1,1,1,1,7),_PdnDot1qVlanStaticOuterEthertype_Type())
pdnDot1qVlanStaticOuterEthertype.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDot1qVlanStaticOuterEthertype.setStatus(_A)
_PdnDot1BasePortPIWGTable_Object=MibTable
pdnDot1BasePortPIWGTable=_PdnDot1BasePortPIWGTable_Object((1,3,6,1,4,1,1795,2,24,2,39,1,1,2))
if mibBuilder.loadTexts:pdnDot1BasePortPIWGTable.setStatus(_A)
_PdnDot1BasePortPIWGEntry_Object=MibTableRow
pdnDot1BasePortPIWGEntry=_PdnDot1BasePortPIWGEntry_Object((1,3,6,1,4,1,1795,2,24,2,39,1,1,2,1))
pdnDot1BasePortPIWGEntry.setIndexNames((0,_F,_G),(0,_B,_J))
if mibBuilder.loadTexts:pdnDot1BasePortPIWGEntry.setStatus(_A)
class _PdnDot1BasePort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PdnDot1BasePort_Type.__name__=_E
_PdnDot1BasePort_Object=MibTableColumn
pdnDot1BasePort=_PdnDot1BasePort_Object((1,3,6,1,4,1,1795,2,24,2,39,1,1,2,1,1),_PdnDot1BasePort_Type())
pdnDot1BasePort.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:pdnDot1BasePort.setStatus(_A)
class _PdnDot1BasePortPIWGId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PdnDot1BasePortPIWGId_Type.__name__=_E
_PdnDot1BasePortPIWGId_Object=MibTableColumn
pdnDot1BasePortPIWGId=_PdnDot1BasePortPIWGId_Object((1,3,6,1,4,1,1795,2,24,2,39,1,1,2,1,2),_PdnDot1BasePortPIWGId_Type())
pdnDot1BasePortPIWGId.setMaxAccess(_K)
if mibBuilder.loadTexts:pdnDot1BasePortPIWGId.setStatus(_A)
_PdnDot1BasePortPIWGCircuit_Type=ObjectIdentifier
_PdnDot1BasePortPIWGCircuit_Object=MibTableColumn
pdnDot1BasePortPIWGCircuit=_PdnDot1BasePortPIWGCircuit_Object((1,3,6,1,4,1,1795,2,24,2,39,1,1,2,1,3),_PdnDot1BasePortPIWGCircuit_Type())
pdnDot1BasePortPIWGCircuit.setMaxAccess(_K)
if mibBuilder.loadTexts:pdnDot1BasePortPIWGCircuit.setStatus(_A)
_PdnDot1TpFdbClear_Type=TblCmd
_PdnDot1TpFdbClear_Object=MibScalar
pdnDot1TpFdbClear=_PdnDot1TpFdbClear_Object((1,3,6,1,4,1,1795,2,24,2,39,1,1,3),_PdnDot1TpFdbClear_Type())
pdnDot1TpFdbClear.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDot1TpFdbClear.setStatus(_A)
_PdnDot1qExtConformance_ObjectIdentity=ObjectIdentity
pdnDot1qExtConformance=_PdnDot1qExtConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,39,1,2))
_PdnDot1qExtGroups_ObjectIdentity=ObjectIdentity
pdnDot1qExtGroups=_PdnDot1qExtGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,39,1,2,1))
_PdnDot1qExtCompliances_ObjectIdentity=ObjectIdentity
pdnDot1qExtCompliances=_PdnDot1qExtCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,39,1,2,2))
dot1qVlanStaticEntry.registerAugmentions((_B,_L))
pdnDot1qVlanStaticExtEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
pdnDot1qVlanExtGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,39,1,2,1,1))
pdnDot1qVlanExtGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:pdnDot1qVlanExtGroup.setStatus(_A)
pdnDot1BasePortPIWGGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,39,1,2,1,2))
pdnDot1BasePortPIWGGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:pdnDot1BasePortPIWGGroup.setStatus(_A)
pdnDot1GeneralGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,39,1,2,1,3))
pdnDot1GeneralGroup.setObjects((_B,_S))
if mibBuilder.loadTexts:pdnDot1GeneralGroup.setStatus(_A)
pdnDot1dVlanStackingGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,39,1,2,1,4))
pdnDot1dVlanStackingGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:pdnDot1dVlanStackingGroup.setStatus(_A)
pdnDot1qExtCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,39,1,2,2,1))
pdnDot1qExtCompliance.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:pdnDot1qExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnDot1qExt':pdnDot1qExt,'pdnDot1qExtObjects':pdnDot1qExtObjects,'pdnDot1qVlanStaticExtTable':pdnDot1qVlanStaticExtTable,_L:pdnDot1qVlanStaticExtEntry,_M:pdnDot1qVlanStaticSecureModeStatus,_N:pdnDot1qVlanStaticProxyArpStatus,_O:pdnDot1qVlanStaticUplink,_P:pdnDot1qVlanStaticDefaultNHR,_T:pdnDot1qVlanStaticOuterTag,_U:pdnDot1qVlanStaticOuterDefaultPriority,_V:pdnDot1qVlanStaticOuterEthertype,'pdnDot1BasePortPIWGTable':pdnDot1BasePortPIWGTable,'pdnDot1BasePortPIWGEntry':pdnDot1BasePortPIWGEntry,_J:pdnDot1BasePort,_Q:pdnDot1BasePortPIWGId,_R:pdnDot1BasePortPIWGCircuit,_S:pdnDot1TpFdbClear,'pdnDot1qExtConformance':pdnDot1qExtConformance,'pdnDot1qExtGroups':pdnDot1qExtGroups,_W:pdnDot1qVlanExtGroup,_X:pdnDot1BasePortPIWGGroup,_Y:pdnDot1GeneralGroup,_Z:pdnDot1dVlanStackingGroup,'pdnDot1qExtCompliances':pdnDot1qExtCompliances,'pdnDot1qExtCompliance':pdnDot1qExtCompliance})