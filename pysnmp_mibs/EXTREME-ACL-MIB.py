_N='aclCounterStatsGroup'
_M='extremeAclStatsByteCount'
_L='extremeAclStatsPktCount'
_K='read-only'
_J='extremeAclStatsCounterName'
_I='extremeAclStatsPortIfIndex'
_H='extremeAclStatsVlanIfIndex'
_G='DisplayString'
_F='Integer32'
_E='EXTREME-CLEARFLOW-MIB'
_D='extremeAclDirection'
_C='not-accessible'
_B='EXTREME-ACL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
extremeAclDirection,=mibBuilder.importSymbols(_E,_D)
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
extremeAcl=ModuleIdentity((1,3,6,1,4,1,1916,1,48))
if mibBuilder.loadTexts:extremeAcl.setRevisions(('2015-12-11 00:00',))
_ExtremeAclObjects_ObjectIdentity=ObjectIdentity
extremeAclObjects=_ExtremeAclObjects_ObjectIdentity((1,3,6,1,4,1,1916,1,48,1))
_ExtremeAclStatsTable_Object=MibTable
extremeAclStatsTable=_ExtremeAclStatsTable_Object((1,3,6,1,4,1,1916,1,48,1,1))
if mibBuilder.loadTexts:extremeAclStatsTable.setStatus(_A)
_ExtremeAclStatsEntry_Object=MibTableRow
extremeAclStatsEntry=_ExtremeAclStatsEntry_Object((1,3,6,1,4,1,1916,1,48,1,1,1))
extremeAclStatsEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_E,_D),(0,_B,_J))
if mibBuilder.loadTexts:extremeAclStatsEntry.setStatus(_A)
_ExtremeAclStatsVlanIfIndex_Type=InterfaceIndexOrZero
_ExtremeAclStatsVlanIfIndex_Object=MibTableColumn
extremeAclStatsVlanIfIndex=_ExtremeAclStatsVlanIfIndex_Object((1,3,6,1,4,1,1916,1,48,1,1,1,1),_ExtremeAclStatsVlanIfIndex_Type())
extremeAclStatsVlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeAclStatsVlanIfIndex.setStatus(_A)
_ExtremeAclStatsPortIfIndex_Type=InterfaceIndexOrZero
_ExtremeAclStatsPortIfIndex_Object=MibTableColumn
extremeAclStatsPortIfIndex=_ExtremeAclStatsPortIfIndex_Object((1,3,6,1,4,1,1916,1,48,1,1,1,2),_ExtremeAclStatsPortIfIndex_Type())
extremeAclStatsPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeAclStatsPortIfIndex.setStatus(_A)
class _ExtremeAclDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ExtremeAclDirection_Type.__name__=_F
_ExtremeAclDirection_Object=MibTableColumn
extremeAclDirection=_ExtremeAclDirection_Object((1,3,6,1,4,1,1916,1,48,1,1,1,3),_ExtremeAclDirection_Type())
extremeAclDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeAclDirection.setStatus(_A)
class _ExtremeAclStatsCounterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeAclStatsCounterName_Type.__name__=_G
_ExtremeAclStatsCounterName_Object=MibTableColumn
extremeAclStatsCounterName=_ExtremeAclStatsCounterName_Object((1,3,6,1,4,1,1916,1,48,1,1,1,4),_ExtremeAclStatsCounterName_Type())
extremeAclStatsCounterName.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeAclStatsCounterName.setStatus(_A)
_ExtremeAclStatsPktCount_Type=Counter64
_ExtremeAclStatsPktCount_Object=MibTableColumn
extremeAclStatsPktCount=_ExtremeAclStatsPktCount_Object((1,3,6,1,4,1,1916,1,48,1,1,1,5),_ExtremeAclStatsPktCount_Type())
extremeAclStatsPktCount.setMaxAccess(_K)
if mibBuilder.loadTexts:extremeAclStatsPktCount.setStatus(_A)
_ExtremeAclStatsByteCount_Type=Counter64
_ExtremeAclStatsByteCount_Object=MibTableColumn
extremeAclStatsByteCount=_ExtremeAclStatsByteCount_Object((1,3,6,1,4,1,1916,1,48,1,1,1,6),_ExtremeAclStatsByteCount_Type())
extremeAclStatsByteCount.setMaxAccess(_K)
if mibBuilder.loadTexts:extremeAclStatsByteCount.setStatus(_A)
_AclConformance_ObjectIdentity=ObjectIdentity
aclConformance=_AclConformance_ObjectIdentity((1,3,6,1,4,1,1916,1,48,9))
_AclGroups_ObjectIdentity=ObjectIdentity
aclGroups=_AclGroups_ObjectIdentity((1,3,6,1,4,1,1916,1,48,9,1))
_AclCompliances_ObjectIdentity=ObjectIdentity
aclCompliances=_AclCompliances_ObjectIdentity((1,3,6,1,4,1,1916,1,48,9,2))
aclCounterStatsGroup=ObjectGroup((1,3,6,1,4,1,1916,1,48,9,1,1))
aclCounterStatsGroup.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:aclCounterStatsGroup.setStatus(_A)
aclStatistics=ModuleCompliance((1,3,6,1,4,1,1916,1,48,9,2,1))
aclStatistics.setObjects((_B,_N))
if mibBuilder.loadTexts:aclStatistics.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'extremeAcl':extremeAcl,'extremeAclObjects':extremeAclObjects,'extremeAclStatsTable':extremeAclStatsTable,'extremeAclStatsEntry':extremeAclStatsEntry,_H:extremeAclStatsVlanIfIndex,_I:extremeAclStatsPortIfIndex,_D:extremeAclDirection,_J:extremeAclStatsCounterName,_L:extremeAclStatsPktCount,_M:extremeAclStatsByteCount,'aclConformance':aclConformance,'aclGroups':aclGroups,_N:aclCounterStatsGroup,'aclCompliances':aclCompliances,'aclStatistics':aclStatistics})