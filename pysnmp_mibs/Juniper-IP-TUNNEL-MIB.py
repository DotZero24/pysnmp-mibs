_U='juniIpTunnelInterfaceGroup2'
_T='juniIpTunnelInterfaceGroup'
_S='juniIpTunnelSequenceNumbers'
_R='obsolete'
_Q='juniIpTunnelIfIndex'
_P='DisplayString'
_O='JuniName'
_N='juniIpTunnelRowStatus'
_M='juniIpTunnelDestination'
_L='juniIpTunnelSource'
_K='juniIpTunnelMtu'
_J='juniIpTunnelChecksum'
_I='juniIpTunnelVirtualRouter'
_H='juniIpTunnelMode'
_G='juniIpTunnelName'
_F='juniIpTunnelNextIfIndex'
_E='TruthValue'
_D='Integer32'
_C='read-create'
_B='current'
_A='Juniper-IP-TUNNEL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniName,JuniNextIfIndex=mibBuilder.importSymbols('Juniper-TC',_O,'JuniNextIfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_P,'PhysAddress','RowStatus','TextualConvention',_E)
juniIpTunnelMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,51))
if mibBuilder.loadTexts:juniIpTunnelMIB.setRevisions(('2003-09-29 17:29','2002-09-16 21:44','2002-01-14 18:16','2001-07-23 20:57'))
_JuniIpTunnelInterfaceObjects_ObjectIdentity=ObjectIdentity
juniIpTunnelInterfaceObjects=_JuniIpTunnelInterfaceObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,51,1))
_JuniIpTunnelNextIfIndex_Type=JuniNextIfIndex
_JuniIpTunnelNextIfIndex_Object=MibScalar
juniIpTunnelNextIfIndex=_JuniIpTunnelNextIfIndex_Object((1,3,6,1,4,1,4874,2,2,51,1,1),_JuniIpTunnelNextIfIndex_Type())
juniIpTunnelNextIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:juniIpTunnelNextIfIndex.setStatus(_B)
_JuniIpTunnelInterfaceTable_Object=MibTable
juniIpTunnelInterfaceTable=_JuniIpTunnelInterfaceTable_Object((1,3,6,1,4,1,4874,2,2,51,1,2))
if mibBuilder.loadTexts:juniIpTunnelInterfaceTable.setStatus(_B)
_JuniIpTunnelInterfaceEntry_Object=MibTableRow
juniIpTunnelInterfaceEntry=_JuniIpTunnelInterfaceEntry_Object((1,3,6,1,4,1,4874,2,2,51,1,2,1))
juniIpTunnelInterfaceEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:juniIpTunnelInterfaceEntry.setStatus(_B)
_JuniIpTunnelIfIndex_Type=InterfaceIndex
_JuniIpTunnelIfIndex_Object=MibTableColumn
juniIpTunnelIfIndex=_JuniIpTunnelIfIndex_Object((1,3,6,1,4,1,4874,2,2,51,1,2,1,1),_JuniIpTunnelIfIndex_Type())
juniIpTunnelIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:juniIpTunnelIfIndex.setStatus(_B)
class _JuniIpTunnelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_JuniIpTunnelName_Type.__name__=_P
_JuniIpTunnelName_Object=MibTableColumn
juniIpTunnelName=_JuniIpTunnelName_Object((1,3,6,1,4,1,4874,2,2,51,1,2,1,2),_JuniIpTunnelName_Type())
juniIpTunnelName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpTunnelName.setStatus(_B)
class _JuniIpTunnelMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ipTunnelModeGre',0),('ipTunnelModeDvmrp',1)))
_JuniIpTunnelMode_Type.__name__=_D
_JuniIpTunnelMode_Object=MibTableColumn
juniIpTunnelMode=_JuniIpTunnelMode_Object((1,3,6,1,4,1,4874,2,2,51,1,2,1,3),_JuniIpTunnelMode_Type())
juniIpTunnelMode.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpTunnelMode.setStatus(_B)
class _JuniIpTunnelVirtualRouter_Type(JuniName):defaultValue=OctetString('default')
_JuniIpTunnelVirtualRouter_Type.__name__=_O
_JuniIpTunnelVirtualRouter_Object=MibTableColumn
juniIpTunnelVirtualRouter=_JuniIpTunnelVirtualRouter_Object((1,3,6,1,4,1,4874,2,2,51,1,2,1,4),_JuniIpTunnelVirtualRouter_Type())
juniIpTunnelVirtualRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpTunnelVirtualRouter.setStatus(_B)
class _JuniIpTunnelChecksum_Type(TruthValue):defaultValue=2
_JuniIpTunnelChecksum_Type.__name__=_E
_JuniIpTunnelChecksum_Object=MibTableColumn
juniIpTunnelChecksum=_JuniIpTunnelChecksum_Object((1,3,6,1,4,1,4874,2,2,51,1,2,1,5),_JuniIpTunnelChecksum_Type())
juniIpTunnelChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpTunnelChecksum.setStatus(_B)
class _JuniIpTunnelMtu_Type(Integer32):defaultValue=10240;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,10240))
_JuniIpTunnelMtu_Type.__name__=_D
_JuniIpTunnelMtu_Object=MibTableColumn
juniIpTunnelMtu=_JuniIpTunnelMtu_Object((1,3,6,1,4,1,4874,2,2,51,1,2,1,6),_JuniIpTunnelMtu_Type())
juniIpTunnelMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpTunnelMtu.setStatus(_B)
_JuniIpTunnelDestination_Type=IpAddress
_JuniIpTunnelDestination_Object=MibTableColumn
juniIpTunnelDestination=_JuniIpTunnelDestination_Object((1,3,6,1,4,1,4874,2,2,51,1,2,1,7),_JuniIpTunnelDestination_Type())
juniIpTunnelDestination.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpTunnelDestination.setStatus(_B)
_JuniIpTunnelSource_Type=IpAddress
_JuniIpTunnelSource_Object=MibTableColumn
juniIpTunnelSource=_JuniIpTunnelSource_Object((1,3,6,1,4,1,4874,2,2,51,1,2,1,8),_JuniIpTunnelSource_Type())
juniIpTunnelSource.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpTunnelSource.setStatus(_B)
_JuniIpTunnelRowStatus_Type=RowStatus
_JuniIpTunnelRowStatus_Object=MibTableColumn
juniIpTunnelRowStatus=_JuniIpTunnelRowStatus_Object((1,3,6,1,4,1,4874,2,2,51,1,2,1,9),_JuniIpTunnelRowStatus_Type())
juniIpTunnelRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpTunnelRowStatus.setStatus(_B)
class _JuniIpTunnelSequenceNumbers_Type(TruthValue):defaultValue=2
_JuniIpTunnelSequenceNumbers_Type.__name__=_E
_JuniIpTunnelSequenceNumbers_Object=MibTableColumn
juniIpTunnelSequenceNumbers=_JuniIpTunnelSequenceNumbers_Object((1,3,6,1,4,1,4874,2,2,51,1,2,1,10),_JuniIpTunnelSequenceNumbers_Type())
juniIpTunnelSequenceNumbers.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpTunnelSequenceNumbers.setStatus(_B)
_JuniIpTunnelConformance_ObjectIdentity=ObjectIdentity
juniIpTunnelConformance=_JuniIpTunnelConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,51,2))
_JuniIpTunnelCompliances_ObjectIdentity=ObjectIdentity
juniIpTunnelCompliances=_JuniIpTunnelCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,51,2,1))
_JuniIpTunnelGroups_ObjectIdentity=ObjectIdentity
juniIpTunnelGroups=_JuniIpTunnelGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,51,2,2))
juniIpTunnelInterfaceGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,51,2,2,1))
juniIpTunnelInterfaceGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:juniIpTunnelInterfaceGroup.setStatus(_R)
juniIpTunnelInterfaceGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,51,2,2,2))
juniIpTunnelInterfaceGroup2.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_S)))
if mibBuilder.loadTexts:juniIpTunnelInterfaceGroup2.setStatus(_B)
juniIpTunnnelCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,51,2,1,1))
juniIpTunnnelCompliance.setObjects((_A,_T))
if mibBuilder.loadTexts:juniIpTunnnelCompliance.setStatus(_R)
juniIpTunnnelCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,51,2,1,2))
juniIpTunnnelCompliance2.setObjects((_A,_U))
if mibBuilder.loadTexts:juniIpTunnnelCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniIpTunnelMIB':juniIpTunnelMIB,'juniIpTunnelInterfaceObjects':juniIpTunnelInterfaceObjects,_F:juniIpTunnelNextIfIndex,'juniIpTunnelInterfaceTable':juniIpTunnelInterfaceTable,'juniIpTunnelInterfaceEntry':juniIpTunnelInterfaceEntry,_Q:juniIpTunnelIfIndex,_G:juniIpTunnelName,_H:juniIpTunnelMode,_I:juniIpTunnelVirtualRouter,_J:juniIpTunnelChecksum,_K:juniIpTunnelMtu,_M:juniIpTunnelDestination,_L:juniIpTunnelSource,_N:juniIpTunnelRowStatus,_S:juniIpTunnelSequenceNumbers,'juniIpTunnelConformance':juniIpTunnelConformance,'juniIpTunnelCompliances':juniIpTunnelCompliances,'juniIpTunnnelCompliance':juniIpTunnnelCompliance,'juniIpTunnnelCompliance2':juniIpTunnnelCompliance2,'juniIpTunnelGroups':juniIpTunnelGroups,_T:juniIpTunnelInterfaceGroup,_U:juniIpTunnelInterfaceGroup2})